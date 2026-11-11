#!/usr/bin/env python3
"""EtUndSo — Wissens-Generator (zero dependencies, nur Stdlib).

Liest Artikel-Quellen aus  content/<fach>/<thema>/NN-slug.md  (Markdown + einfacher Kopf)
und erzeugt daraus die ausgelieferte Wissens-Sektion unter  web/wissen/ :
  * eine HTML-Seite pro Artikel (brand-styled, mit Sidebar-Baum, Breadcrumb, Inhaltsverzeichnis,
    Zurück/Weiter), KaTeX für Mathe;
  * web/wissen/index.html  (Übersicht aller Fächer);
  * web/wissen/data/tree.json  (Navigationsbaum) und  search.json  (Suchindex);
  * web/wissen/assets/wissen.css + wissen.js  (Sidebar/Suche/Inhaltsverzeichnis).

Aufruf (vom Repo-Root):  python build_wissen.py
Danach committen + pushen wie den Rest der Seite.

Artikel-Kopf (zwischen zwei '---'-Zeilen):
    ---
    title: Das Ohmsche Gesetz
    fach: Elektrotechnik
    thema: Schaltungstechnik
    order: 1
    summary: Kurzbeschreibung für Übersicht & Suche.
    tags: Ohm, Widerstand, Spannung
    ---
Reihenfolge der Fächer/Themen: über das kleinste `order` ihrer Artikel; Dateiname-Präfix NN- sortiert innerhalb.

Fassungen eines Themas (alle mit demselben `pfad:`, im selben Ordner):
    NN-slug.md                      kompakte KI-Fassung (steht im Baum)
    NN-slug-ausfuehrlich.md         ausführliche KI-Fassung      (fassung: ausfuehrlich)
    NN-slug-mensch.md               von Hand geschriebene Fassung (autor: mensch; der Suffix -mensch genügt)
    NN-slug-mensch-ausfuehrlich.md  von Hand, ausführlich
Eine Hand-Fassung mit KI-Gegenstück wird gebaut, aber nicht verlinkt und nicht durchsucht; ohne Gegenstück steht sie im Baum.

Sprachen (de, en, es, zh, fr, tr): NN-slug.en.md neben NN-slug.md ist die Übersetzung, mit übersetztem `pfad:`. Sie
landet unter web/wissen/en/<dieselbe Adresse wie der deutsche Artikel>, jede Sprache hat ihren eigenen Baum, ihre
Übersicht und ihren Suchindex. Das Sprachmenü (Knopf „DE ▾“ in der Kopfleiste, auf schmalen Bildschirmen unter dem
Titel) führt zur selben Seite in der anderen Sprache; Sprachen ohne Übersetzung dieser Seite sind ausgegraut.

Weitere Kopffelder (tools/heft_zu_artikel.py schreibt sie für alle Hefte):
    adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
                                                  Adresse der pfad-Knoten (je Knoten ein Slug, so viele wie pfad: Teile hat):
                                                  Die Seite liegt dann unter adresse/<artikel>.html, auch wenn pfad: die Namen
                                                  ändert („ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme“).
                                                  Ohne adresse: kommen die Slugs aus den deutschen pfad:-Namen.
    knoten: Kapitel 1: Vektoren und Matrizen      Aufschrift des letzten pfad-Knotens im Baum, in Brotkrumen und Suche;
                                                  die Adresse kommt weiter aus pfad: bzw. adresse: (bleibt bei neuer Nummerierung).
    nachschlagen: ja                              Nachschlage-Artikel: Darunter steht „Verwendet in“ mit allen Artikeln
                                                  derselben Sprache, die ihn (oder einen Anker darin) verlinken.
Dateien content/**/_<name>[.<lang>].md sind keine Artikel, sondern ein kurzer Text zu einem Knoten der Übersicht:
    ---
    hinweis: Informatik / Machine Learning        (Pfad des Knotens in dieser Sprache)
    ---
    Text (Markdown, eine Zeile oder ein Absatz)
Seiten unter web/wissen/, die ein Build nicht mehr schreibt (alte Adressen), löscht er am Ende; Ordner mit „_“ bleiben.
"""
import datetime, json, re, html, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC  = ROOT / "content"
OUT  = ROOT / "web" / "wissen"
# Abbildungen aus dem Editor (:::abbildung <szene>): tools/export_szenen.py schreibt aus web/szenen/<szene>.json
# das Artikelbild web/abbildungen/<sprache>/<szene>.svg. Szenenname = Pfad unter web/szenen/ ohne .json, Teile aus
# A-Z a-z 0-9 _ - (dieselbe Regel wie der Szenen-Link im Editor, editor.js SCENE_LINK_RE).
SZENEN   = ROOT / "web" / "szenen"
ABB_DIR  = ROOT / "web" / "abbildungen"
ABB_URL  = "/abbildungen"
SZENE_NAME_RE = re.compile(r"[A-Za-z0-9_-]+(?:/[A-Za-z0-9_-]+)*")
SITE = "https://etundso.de"           # für hreflang

LANGS = ("de", "en", "es", "zh", "fr", "tr")
LANG_NAME = {"de": "DE", "en": "EN", "es": "ES", "zh": "中文", "fr": "FR", "tr": "TR"}   # Aufschrift des Sprachknopfs
LANG_VOLL = {"de": "Deutsch", "en": "English", "es": "Español", "fr": "Français", "tr": "Türkçe", "zh": "中文"}   # im Menü, in eigener Schreibweise
LANG_MENU = ("de", "en", "es", "fr", "tr", "zh")   # Reihenfolge im Menü
LANG_FILE = re.compile(r"\.(%s)$" % "|".join(l for l in LANGS if l != "de"))   # NN-slug.en.md
LANG_NOW = ["de"]                     # Sprache der gerade gebauten Seite (main setzt sie)

# Oberfläche je Sprache. Deutsch ist die Quelle; fehlt ein Wort, steht das deutsche da.
UI = {
    "de": {"wissen": "Wissen", "alle_module": "Alle Module", "abbildung": "Abbildung", "abb_vorb": "in Vorbereitung",
           "editor_offen": "Szene im Editor öffnen", "editor_title": "Die Szene dieser Abbildung im Editor öffnen",
           "herleitung": "Herleitung", "beweis": "Beweis", "frage": "Frage", "hintergrund": "Hintergrund", "loesung": "Lösung", "zweck": "Worum es geht:",
           "zusatz": "Vertiefung, für den Rest nicht nötig", "analogie": "Analogie (ein Bild zur Orientierung, keine Mathematik)",
           "kern": "Das Wichtigste", "merke": "Merke", "satz": "Satz", "definition": "Definition", "lemma": "Lemma",
           "suchen": "Suchen", "suche_ph": "Thema, Begriff, Formel …", "nichts": "Nichts gefunden für",
           "suche_hint": 'Teilwörter erlaubt (z. B. „teiler" findet „Spannungsteiler"). <kbd>Esc</kbd> schließt.',
           "auf_seite": "Auf dieser Seite", "im_artikel": "In diesem Artikel", "vorher": "Vorheriger Artikel", "weiter": "Nächster Artikel",
           "lede": "Verständliche, animierte Erklärungen — von Grund auf und in kleinen Schritten. Wähle ein Modul oder nutze die Suche.",
           "leer": "Hier entstehen nach und nach die Artikel.", "beispiel": "Beispiel", "ki_pill": "KI-generiert",
           "hand_pill": "von Hand geschrieben", "quiz": "Quiz — teste dein Verständnis", "impressum": "Impressum", "datenschutz": "Datenschutz",
           "warnung": "Achtung", "konsole": "Konsole", "sprache": "Sprache", "nicht_uebersetzt": "noch nicht übersetzt",
           "fremd": "Rechtliche Seiten sind auf Deutsch.", "verwendet": "Verwendet in"},
    "en": {"wissen": "Knowledge", "alle_module": "All modules", "abbildung": "Figure", "abb_vorb": "in preparation",
           "editor_offen": "Open scene in editor", "editor_title": "Open this figure's scene in the editor",
           "herleitung": "Derivation", "beweis": "Proof", "frage": "Question", "hintergrund": "Background", "loesung": "Solution", "zweck": "What this stage is about:",
           "zusatz": "Going deeper, not needed for the rest", "analogie": "Analogy (a picture for orientation, not mathematics)",
           "kern": "Key points", "merke": "Note", "satz": "Theorem", "definition": "Definition", "lemma": "Lemma",
           "suchen": "Search", "suche_ph": "Topic, term, formula …", "nichts": "Nothing found for",
           "suche_hint": 'Parts of words work (“divider” finds “voltage divider”). <kbd>Esc</kbd> closes.',
           "auf_seite": "On this page", "im_artikel": "In this article", "vorher": "Previous article", "weiter": "Next article",
           "lede": "Clear, illustrated explanations, from the ground up and in small steps. Pick a module or use the search.",
           "leer": "Articles are on their way.", "beispiel": "Example", "ki_pill": "AI-generated",
           "hand_pill": "hand-written", "quiz": "Quiz — test your understanding", "impressum": "Legal notice", "datenschutz": "Privacy",
           "warnung": "Caution", "konsole": "Terminal", "sprache": "Language", "nicht_uebersetzt": "not translated yet",
           "verwendet": "Used in"},
    "es": {"wissen": "Conocimiento", "alle_module": "Todos los módulos", "abbildung": "Figura", "abb_vorb": "en preparación",
           "editor_offen": "Abrir la escena en el editor", "editor_title": "Abrir la escena de esta figura en el editor",
           "herleitung": "Deducción", "beweis": "Demostración", "frage": "Pregunta", "hintergrund": "Contexto", "loesung": "Solución", "zweck": "De qué trata esta etapa:",
           "zusatz": "Ampliación, no necesaria para el resto", "analogie": "Analogía (una imagen para orientarse, no matemática)",
           "kern": "Lo esencial", "merke": "Nota", "satz": "Teorema", "definition": "Definición", "lemma": "Lema",
           "suchen": "Buscar", "suche_ph": "Tema, término, fórmula …", "nichts": "Nada encontrado para",
           "suche_hint": 'Se admiten partes de palabras. <kbd>Esc</kbd> cierra.',
           "auf_seite": "En esta página", "im_artikel": "En este artículo", "vorher": "Artículo anterior", "weiter": "Artículo siguiente",
           "lede": "Explicaciones claras e ilustradas, desde la base y en pasos pequeños. Elige un módulo o usa la búsqueda.",
           "leer": "Los artículos están en camino.", "beispiel": "Ejemplo", "ki_pill": "generado por IA",
           "hand_pill": "escrito a mano", "quiz": "Cuestionario — comprueba lo aprendido", "impressum": "Aviso legal", "datenschutz": "Privacidad",
           "warnung": "Atención", "konsole": "Terminal", "sprache": "Idioma", "nicht_uebersetzt": "aún sin traducir",
           "verwendet": "Se usa en"},
    "zh": {"wissen": "知识库", "alle_module": "全部模块", "abbildung": "图", "abb_vorb": "准备中",
           "editor_offen": "在编辑器中打开场景", "editor_title": "在编辑器中打开此图的场景",
           "herleitung": "推导", "beweis": "证明", "frage": "问题", "hintergrund": "背景", "loesung": "解答", "zweck": "本阶段内容：",
           "zusatz": "拓展阅读（后续内容不需要）", "analogie": "类比（帮助理解的图景，不是数学）",
           "kern": "要点", "merke": "注意", "satz": "定理", "definition": "定义", "lemma": "引理",
           "suchen": "搜索", "suche_ph": "主题、术语、公式 …", "nichts": "未找到",
           "suche_hint": '可以输入词的一部分。<kbd>Esc</kbd> 关闭。',
           "auf_seite": "本页内容", "im_artikel": "本文目录", "vorher": "上一篇", "weiter": "下一篇",
           "lede": "清晰、配图的讲解，从基础出发，循序渐进。请选择模块或使用搜索。",
           "leer": "文章正在陆续添加。", "beispiel": "例", "ki_pill": "AI 生成",
           "hand_pill": "人工撰写", "quiz": "测验：检验你的理解", "impressum": "法律声明", "datenschutz": "隐私",
           "warnung": "注意", "konsole": "终端", "sprache": "语言", "nicht_uebersetzt": "尚未翻译",
           "verwendet": "引用本节的文章"},
    # Französisch: Leser wird gesiezt (vous), Leerzeichen vor : ; ! ? und in « » sind geschützt (\u00a0, \u202f)
    "fr": {"wissen": "Connaissances", "alle_module": "Tous les modules", "abbildung": "Figure", "abb_vorb": "en préparation",
           "editor_offen": "Ouvrir la scène dans l’éditeur", "editor_title": "Ouvrir la scène de cette figure dans l’éditeur",
           "herleitung": "Démonstration", "beweis": "Preuve", "frage": "Question", "hintergrund": "Contexte", "loesung": "Solution",
           "zweck": "De quoi traite cette étape\u00a0:",
           "zusatz": "Pour aller plus loin, pas nécessaire pour la suite", "analogie": "Analogie (une image pour s’orienter, pas des mathématiques)",
           "kern": "L’essentiel", "merke": "À retenir", "satz": "Théorème", "definition": "Définition", "lemma": "Lemme",
           "suchen": "Rechercher", "suche_ph": "Sujet, notion, formule …", "nichts": "Aucun résultat pour",
           "suche_hint": 'Un fragment de mot suffit («\u00a0diviseur\u00a0» trouve «\u00a0diviseur de tension\u00a0»). <kbd>Échap</kbd> pour fermer.',
           "auf_seite": "Sur cette page", "im_artikel": "Dans cet article", "vorher": "Article précédent", "weiter": "Article suivant",
           "lede": "Des explications claires et illustrées, en partant des bases et par petites étapes. Choisissez un module ou utilisez la recherche.",
           "leer": "Les articles arrivent peu à peu.", "beispiel": "Exemple", "ki_pill": "généré par IA",
           "hand_pill": "écrit à la main", "quiz": "Quiz — testez votre compréhension", "impressum": "Mentions légales", "datenschutz": "Confidentialité",
           "warnung": "Attention", "konsole": "Terminal", "sprache": "Langue", "nicht_uebersetzt": "pas encore traduit",
           "verwendet": "Utilisé dans"},
    # Türkisch: Leser wird gesiezt (siz)
    "tr": {"wissen": "Bilgi", "alle_module": "Tüm modüller", "abbildung": "Şekil", "abb_vorb": "hazırlanıyor",
           "editor_offen": "Sahneyi düzenleyicide aç", "editor_title": "Bu şeklin sahnesini düzenleyicide aç",
           "herleitung": "Türetme", "beweis": "İspat", "frage": "Soru", "hintergrund": "Arka plan", "loesung": "Çözüm",
           "zweck": "Bu aşamanın konusu:",
           "zusatz": "Ek okuma, devamı için gerekli değil", "analogie": "Benzetme (yol gösteren bir imge, matematik değil)",
           "kern": "Temel noktalar", "merke": "Not", "satz": "Teorem", "definition": "Tanım", "lemma": "Lemma",
           "suchen": "Ara", "suche_ph": "Konu, kavram, formül …", "nichts": "Sonuç bulunamadı",
           "suche_hint": 'Kelimenin bir parçası da yeterli (“bölücü”, “gerilim bölücü”yü de bulur). <kbd>Esc</kbd> ile kapanır.',
           "auf_seite": "Bu sayfada", "im_artikel": "Bu makalede", "vorher": "Önceki makale", "weiter": "Sonraki makale",
           "lede": "Temelden başlayan, küçük adımlarla ilerleyen, anlaşılır ve görsellerle desteklenen açıklamalar. Bir modül seçin ya da aramayı kullanın.",
           "leer": "Makaleler yavaş yavaş ekleniyor.", "beispiel": "Örnek", "ki_pill": "yapay zekâ ile üretildi",
           "hand_pill": "elle yazıldı", "quiz": "Test — anladıklarınızı sınayın", "impressum": "Künye", "datenschutz": "Gizlilik",
           "warnung": "Dikkat", "konsole": "Terminal", "sprache": "Dil", "nicht_uebersetzt": "henüz çevrilmedi",
           "verwendet": "Kullanıldığı yerler"},
}

# Artikelkopf (Kennzahlenzeile), Zusammenfassung am Artikelende, Sprunglink „Zum Inhalt“, Ankerlink an Überschriften (11.11.2026)
_UI_ARTIKEL = {
    "de": {"zf": "Zusammenfassung", "zf_begriffe": "Begriffe", "zf_formeln": "Formeln", "zf_zusammenhaenge": "Zusammenhänge",
           "zf_mehr": "{n} weitere zeigen", "zf_sprung": "Zur Zusammenfassung", "lesezeit": "{n} min Lesezeit",
           "abb_1": "1 Abbildung", "abb_n": "{n} Abbildungen", "aufg_1": "1 Aufgabe", "aufg_n": "{n} Aufgaben",
           "zum_inhalt": "Zum Inhalt", "anker": "Link zu diesem Abschnitt"},
    "en": {"zf": "Summary", "zf_begriffe": "Terms", "zf_formeln": "Formulas", "zf_zusammenhaenge": "Key relationships",
           "zf_mehr": "Show {n} more", "zf_sprung": "Jump to summary", "lesezeit": "{n} min read",
           "abb_1": "1 figure", "abb_n": "{n} figures", "aufg_1": "1 exercise", "aufg_n": "{n} exercises",
           "zum_inhalt": "Skip to content", "anker": "Link to this section"},
    "es": {"zf": "Resumen", "zf_begriffe": "Términos", "zf_formeln": "Fórmulas", "zf_zusammenhaenge": "Relaciones clave",
           "zf_mehr": "Mostrar {n} más", "zf_sprung": "Ir al resumen", "lesezeit": "{n} min de lectura",
           "abb_1": "1 figura", "abb_n": "{n} figuras", "aufg_1": "1 ejercicio", "aufg_n": "{n} ejercicios",
           "zum_inhalt": "Ir al contenido", "anker": "Enlace a esta sección"},
    "zh": {"zf": "小结", "zf_begriffe": "术语", "zf_formeln": "公式", "zf_zusammenhaenge": "关键联系",
           "zf_mehr": "再显示 {n} 项", "zf_sprung": "跳到小结", "lesezeit": "阅读约 {n} 分钟",
           "abb_1": "1 幅图", "abb_n": "{n} 幅图", "aufg_1": "1 道练习", "aufg_n": "{n} 道练习",
           "zum_inhalt": "跳到正文", "anker": "本节链接"},
    "fr": {"zf": "Résumé", "zf_begriffe": "Notions", "zf_formeln": "Formules", "zf_zusammenhaenge": "Relations clés",
           "zf_mehr": "Afficher {n} de plus", "zf_sprung": "Aller au résumé", "lesezeit": "{n} min de lecture",
           "abb_1": "1 figure", "abb_n": "{n} figures", "aufg_1": "1 exercice", "aufg_n": "{n} exercices",
           "zum_inhalt": "Aller au contenu", "anker": "Lien vers cette section"},
    "tr": {"zf": "Özet", "zf_begriffe": "Kavramlar", "zf_formeln": "Formüller", "zf_zusammenhaenge": "Temel ilişkiler",
           "zf_mehr": "{n} tane daha göster", "zf_sprung": "Özete git", "lesezeit": "{n} dk okuma",
           "abb_1": "1 şekil", "abb_n": "{n} şekil", "aufg_1": "1 alıştırma", "aufg_n": "{n} alıştırma",
           "zum_inhalt": "İçeriğe geç", "anker": "Bu bölümün bağlantısı"},
}
for _l, _w in _UI_ARTIKEL.items():
    UI[_l].update(_w)

# Lernen (W2, 11.11.2026): Lesefortschritt, Begriffsverzeichnis, Link-Vorschau, Selbsttest, Lernkarten. Die Wörter unter
# LERNEN_JS braucht auch wissen.js; main schreibt sie beim Erzeugen der Datei hinein (/*UI_LERNEN*/{}).
_UI_LERNEN = {
    "de": {"begriffe": "Begriffe", "lernkarten": "Lernkarten",
           "bg_lede": "Die Fachbegriffe dieses Moduls mit ihrer Bestimmung. Ein Klick auf einen Begriff führt an die Stelle, an der er eingeführt wird.",
           "bg_filter": "Begriffe filtern", "bg_leer": "Kein Begriff passt.", "bg_anzahl": "{n} Begriffe", "bg_abc": "Anfangsbuchstaben",
           "bg_keine": "Für dieses Modul gibt es noch keine Begriffe.",
           "lk_lede": "Karten aus den Artikeln dieses Moduls: Begriffe, benannte Formeln und Lückentexte. Was du weißt, kommt nach "
                      "wachsenden Abständen wieder (1, 3, 7, 14 und 30 Tage). Der Lernstand bleibt nur in diesem Browser.",
           "lk_kapitel": "Kapitel", "lk_alle_kap": "Alle Kapitel", "lk_faellig": "Heute fällig: {n}", "lk_davon_neu": "davon neu: {n}",
           "lk_umdrehen": "Umdrehen", "lk_gut": "Wusste ich", "lk_mittel": "Unsicher", "lk_schlecht": "Wusste ich nicht",
           "lk_stelle": "Zur Stelle im Artikel", "lk_fertig": "Für heute ist in dieser Auswahl nichts mehr fällig.",
           "lk_mehr_neu": "{n} weitere neue Karten", "lk_liste": "Alle Karten als Liste ({n})", "lk_begriff": "Begriff",
           "lk_formel": "Formel", "lk_luecke": "Lückentext", "lk_reset": "Lernstand zurücksetzen", "reset_sicher": "Wirklich zurücksetzen?",
           "lk_ohne_speicher": "Dieser Browser speichert gerade nichts. Der Lernstand gilt nur, solange die Seite offen ist.",
           "lk_heute": "gleich noch einmal", "lk_morgen": "morgen", "lk_tage": "in {n} Tagen",
           "lk_keine": "Für dieses Modul gibt es noch keine Lernkarten.", "lk_zum_kapitel": "Lernkarten zu diesem Kapitel",
           "lk_tasten": "Tasten: Leertaste dreht um, 1 / 2 / 3 bewerten.",
           "zf_test": "Selbsttest", "zf_test_t": "Punkte zudecken, erst selbst erinnern, dann einzeln aufdecken", "aufdecken": "Aufdecken",
           "zf_zu": "Zu „{h}“:", "gelesen": "Gelesen", "lf_kapitel": "{n} von {m} gelesen", "lf_artikel": "Gelesen. In diesem Kapitel: {n} von {m}.",
           "weiterlesen": "Weiterlesen", "fs_reset": "Fortschritt zurücksetzen", "fs_lokal": "Der Lesefortschritt bleibt nur in diesem Browser.",
           "vs_oeffnen": "Öffnen", "vs_schliessen": "Schließen"},
    "en": {"begriffe": "Glossary", "lernkarten": "Flashcards",
           "bg_lede": "The technical terms of this module with their definitions. Selecting a term takes you to the place where it is introduced.",
           "bg_filter": "Filter terms", "bg_leer": "No term matches.", "bg_anzahl": "{n} terms", "bg_abc": "Initial letters",
           "bg_keine": "There are no terms for this module yet.",
           "lk_lede": "Cards from the articles of this module: terms, named formulas and fill-in-the-blank sentences. What you know comes "
                      "back after growing intervals (1, 3, 7, 14 and 30 days). Your progress stays in this browser only.",
           "lk_kapitel": "Chapter", "lk_alle_kap": "All chapters", "lk_faellig": "Due today: {n}", "lk_davon_neu": "new: {n}",
           "lk_umdrehen": "Flip", "lk_gut": "I knew it", "lk_mittel": "Unsure", "lk_schlecht": "I didn't know",
           "lk_stelle": "Go to the place in the article", "lk_fertig": "Nothing more is due today in this selection.",
           "lk_mehr_neu": "{n} more new cards", "lk_liste": "All cards as a list ({n})", "lk_begriff": "Term",
           "lk_formel": "Formula", "lk_luecke": "Fill in the blank", "lk_reset": "Reset learning progress", "reset_sicher": "Really reset?",
           "lk_ohne_speicher": "This browser is not saving anything right now. Progress lasts only while the page is open.",
           "lk_heute": "again shortly", "lk_morgen": "tomorrow", "lk_tage": "in {n} days",
           "lk_keine": "There are no flashcards for this module yet.", "lk_zum_kapitel": "Flashcards for this chapter",
           "lk_tasten": "Keys: Space flips, 1 / 2 / 3 rate.",
           "zf_test": "Self-test", "zf_test_t": "Cover the points, recall each one yourself, then reveal them one by one", "aufdecken": "Reveal",
           "zf_zu": "On “{h}”:", "gelesen": "Read", "lf_kapitel": "{n} of {m} read", "lf_artikel": "Read. In this chapter: {n} of {m}.",
           "weiterlesen": "Continue reading", "fs_reset": "Reset reading progress", "fs_lokal": "Reading progress stays in this browser only.",
           "vs_oeffnen": "Open", "vs_schliessen": "Close"},
    "es": {"begriffe": "Glosario", "lernkarten": "Tarjetas de estudio",
           "bg_lede": "Los términos técnicos de este módulo con su definición. Al pulsar un término llegas al lugar donde se introduce.",
           "bg_filter": "Filtrar términos", "bg_leer": "Ningún término coincide.", "bg_anzahl": "{n} términos", "bg_abc": "Letras iniciales",
           "bg_keine": "Todavía no hay términos para este módulo.",
           "lk_lede": "Tarjetas sacadas de los artículos de este módulo: términos, fórmulas con nombre y frases para completar. Lo que "
                      "sabes vuelve tras intervalos crecientes (1, 3, 7, 14 y 30 días). Tu progreso se queda solo en este navegador.",
           "lk_kapitel": "Capítulo", "lk_alle_kap": "Todos los capítulos", "lk_faellig": "Pendientes hoy: {n}", "lk_davon_neu": "nuevas: {n}",
           "lk_umdrehen": "Dar la vuelta", "lk_gut": "Lo sabía", "lk_mittel": "Dudoso", "lk_schlecht": "No lo sabía",
           "lk_stelle": "Ir al lugar en el artículo", "lk_fertig": "Hoy no queda nada pendiente en esta selección.",
           "lk_mehr_neu": "{n} tarjetas nuevas más", "lk_liste": "Todas las tarjetas en lista ({n})", "lk_begriff": "Término",
           "lk_formel": "Fórmula", "lk_luecke": "Completar", "lk_reset": "Reiniciar el progreso de estudio", "reset_sicher": "¿Reiniciar de verdad?",
           "lk_ohne_speicher": "Este navegador no guarda nada ahora mismo. El progreso solo dura mientras la página esté abierta.",
           "lk_heute": "otra vez enseguida", "lk_morgen": "mañana", "lk_tage": "en {n} días",
           "lk_keine": "Todavía no hay tarjetas para este módulo.", "lk_zum_kapitel": "Tarjetas de este capítulo",
           "lk_tasten": "Teclas: Espacio da la vuelta, 1 / 2 / 3 valoran.",
           "zf_test": "Autoevaluación", "zf_test_t": "Tapa los puntos, recuerda cada uno y luego descúbrelos uno a uno", "aufdecken": "Descubrir",
           "zf_zu": "Sobre «{h}»:", "gelesen": "Leído", "lf_kapitel": "{n} de {m} leídos", "lf_artikel": "Leído. En este capítulo: {n} de {m}.",
           "weiterlesen": "Seguir leyendo", "fs_reset": "Reiniciar el progreso de lectura",
           "fs_lokal": "El progreso de lectura se queda solo en este navegador.", "vs_oeffnen": "Abrir", "vs_schliessen": "Cerrar"},
    "zh": {"begriffe": "术语表", "lernkarten": "学习卡片",
           "bg_lede": "本模块的专业术语及其释义，按章节排列。点击术语即可跳到它被引入的位置。",
           "bg_filter": "筛选术语", "bg_leer": "没有匹配的术语。", "bg_anzahl": "共 {n} 个术语", "bg_abc": "章节",
           "bg_keine": "本模块暂时还没有术语。",
           "lk_lede": "卡片取自本模块的文章：术语、有名称的公式和填空句。答对的卡片会按逐渐拉长的间隔再次出现（1、3、7、14 和 30 天）。"
                      "学习进度只保存在本浏览器中。",
           "lk_kapitel": "章节", "lk_alle_kap": "全部章节", "lk_faellig": "今天到期：{n}", "lk_davon_neu": "其中新卡：{n}",
           "lk_umdrehen": "翻面", "lk_gut": "记得", "lk_mittel": "不确定", "lk_schlecht": "不记得",
           "lk_stelle": "跳到文章中的位置", "lk_fertig": "此范围内今天已没有到期的卡片。",
           "lk_mehr_neu": "再学 {n} 张新卡", "lk_liste": "以列表显示全部卡片（{n}）", "lk_begriff": "术语",
           "lk_formel": "公式", "lk_luecke": "填空", "lk_reset": "重置学习进度", "reset_sicher": "确定要重置吗？",
           "lk_ohne_speicher": "此浏览器目前无法保存数据，学习进度只在页面打开期间有效。",
           "lk_heute": "稍后再来一次", "lk_morgen": "明天", "lk_tage": "{n} 天后",
           "lk_keine": "本模块暂时还没有学习卡片。", "lk_zum_kapitel": "本章学习卡片",
           "lk_tasten": "按键：空格翻面，1 / 2 / 3 评分。",
           "zf_test": "自测", "zf_test_t": "先遮住各条，自己回想，再逐条揭开", "aufdecken": "揭开",
           "zf_zu": "关于“{h}”：", "gelesen": "已读", "lf_kapitel": "已读 {n} / {m}", "lf_artikel": "已读。本章已读 {n} / {m}。",
           "weiterlesen": "继续阅读", "fs_reset": "重置阅读进度", "fs_lokal": "阅读进度只保存在本浏览器中。",
           "vs_oeffnen": "打开", "vs_schliessen": "关闭"},
    "fr": {"begriffe": "Glossaire", "lernkarten": "Fiches de révision",
           "bg_lede": "Les termes techniques de ce module avec leur définition. Un clic sur un terme mène à l’endroit où il est introduit.",
           "bg_filter": "Filtrer les termes", "bg_leer": "Aucun terme ne correspond.", "bg_anzahl": "{n} termes", "bg_abc": "Lettres initiales",
           "bg_keine": "Il n’y a pas encore de termes pour ce module.",
           "lk_lede": "Des fiches tirées des articles de ce module : termes, formules nommées et phrases à compléter. Ce que vous savez "
                      "revient après des intervalles croissants (1, 3, 7, 14 et 30 jours). Votre progression reste uniquement dans ce navigateur.",
           "lk_kapitel": "Chapitre", "lk_alle_kap": "Tous les chapitres", "lk_faellig": "À revoir aujourd’hui : {n}",
           "lk_davon_neu": "dont nouvelles : {n}", "lk_umdrehen": "Retourner", "lk_gut": "Je savais", "lk_mittel": "Incertain",
           "lk_schlecht": "Je ne savais pas", "lk_stelle": "Aller à l’endroit dans l’article",
           "lk_fertig": "Plus rien à revoir aujourd’hui dans cette sélection.", "lk_mehr_neu": "{n} nouvelles fiches de plus",
           "lk_liste": "Toutes les fiches en liste ({n})", "lk_begriff": "Terme", "lk_formel": "Formule", "lk_luecke": "Texte à trous",
           "lk_reset": "Réinitialiser la progression", "reset_sicher": "Vraiment réinitialiser ?",
           "lk_ohne_speicher": "Ce navigateur n’enregistre rien pour le moment. La progression ne dure que tant que la page est ouverte.",
           "lk_heute": "encore une fois tout de suite", "lk_morgen": "demain", "lk_tage": "dans {n} jours",
           "lk_keine": "Il n’y a pas encore de fiches pour ce module.", "lk_zum_kapitel": "Fiches de ce chapitre",
           "lk_tasten": "Touches : Espace retourne, 1 / 2 / 3 évaluent.",
           "zf_test": "Auto-test", "zf_test_t": "Masquer les points, se les rappeler soi-même, puis les révéler un à un", "aufdecken": "Révéler",
           "zf_zu": "À propos de « {h} » :", "gelesen": "Lu", "lf_kapitel": "{n} sur {m} lus", "lf_artikel": "Lu. Dans ce chapitre : {n} sur {m}.",
           "weiterlesen": "Reprendre la lecture", "fs_reset": "Réinitialiser la progression de lecture",
           "fs_lokal": "La progression de lecture reste uniquement dans ce navigateur.", "vs_oeffnen": "Ouvrir", "vs_schliessen": "Fermer"},
    "tr": {"begriffe": "Sözlük", "lernkarten": "Çalışma kartları",
           "bg_lede": "Bu modüldeki terimler ve tanımları. Bir terime tıklayınca onun ilk tanıtıldığı yere gidersiniz.",
           "bg_filter": "Terimleri süz", "bg_leer": "Eşleşen terim yok.", "bg_anzahl": "{n} terim", "bg_abc": "Baş harfler",
           "bg_keine": "Bu modül için henüz terim yok.",
           "lk_lede": "Bu modülün makalelerinden kartlar: terimler, adı olan formüller ve boşluk doldurma cümleleri. Bildiğiniz kartlar "
                      "giderek uzayan aralıklarla geri gelir (1, 3, 7, 14 ve 30 gün). İlerlemeniz yalnızca bu tarayıcıda kalır.",
           "lk_kapitel": "Bölüm", "lk_alle_kap": "Tüm bölümler", "lk_faellig": "Bugün sırası gelen: {n}", "lk_davon_neu": "yeni: {n}",
           "lk_umdrehen": "Çevir", "lk_gut": "Biliyordum", "lk_mittel": "Emin değilim", "lk_schlecht": "Bilmiyordum",
           "lk_stelle": "Makaledeki yerine git", "lk_fertig": "Bu seçimde bugün için başka kart yok.",
           "lk_mehr_neu": "{n} yeni kart daha", "lk_liste": "Tüm kartlar liste olarak ({n})", "lk_begriff": "Terim",
           "lk_formel": "Formül", "lk_luecke": "Boşluk doldurma", "lk_reset": "Öğrenme ilerlemesini sıfırla", "reset_sicher": "Gerçekten sıfırlansın mı?",
           "lk_ohne_speicher": "Bu tarayıcı şu anda hiçbir şey kaydetmiyor. İlerleme yalnızca sayfa açıkken geçerli.",
           "lk_heute": "birazdan tekrar", "lk_morgen": "yarın", "lk_tage": "{n} gün sonra",
           "lk_keine": "Bu modül için henüz çalışma kartı yok.", "lk_zum_kapitel": "Bu bölümün çalışma kartları",
           "lk_tasten": "Tuşlar: Boşluk çevirir, 1 / 2 / 3 değerlendirir.",
           "zf_test": "Kendini sına", "zf_test_t": "Maddeleri kapatın, önce kendiniz hatırlayın, sonra tek tek açın", "aufdecken": "Aç",
           "zf_zu": "“{h}” hakkında:", "gelesen": "Okundu", "lf_kapitel": "{m} makaleden {n} tanesi okundu",
           "lf_artikel": "Okundu. Bu bölümde: {m} makaleden {n} tanesi.", "weiterlesen": "Okumaya devam et",
           "fs_reset": "Okuma ilerlemesini sıfırla", "fs_lokal": "Okuma ilerlemesi yalnızca bu tarayıcıda kalır.",
           "vs_oeffnen": "Aç", "vs_schliessen": "Kapat"},
}
for _l, _w in _UI_LERNEN.items():
    UI[_l].update(_w)
LERNEN_JS = ("bg_leer", "bg_anzahl", "lk_faellig", "lk_davon_neu", "lk_fertig", "lk_mehr_neu", "lk_begriff", "lk_formel", "lk_luecke",
             "reset_sicher", "lk_heute", "lk_morgen", "lk_tage", "lk_ohne_speicher", "aufdecken", "gelesen", "lf_kapitel", "lf_artikel",
             "weiterlesen", "fs_reset", "fs_lokal", "vs_oeffnen", "vs_schliessen", "baum_laedt", "baum_fehler", "suche_volltext",
             "begriffe", "lernkarten")

# Finden (W3a, 11.11.2026): Modulkarten der Übersicht, nachgeladene Seitenleiste, geteilte Suche
_UI_FINDEN = {
    "de": {"n_kapitel": "{n} Kapitel", "n_kapitel_1": "1 Kapitel", "n_artikel": "{n} Artikel", "n_artikel_1": "1 Artikel",
           "nur_de": "Bisher nur auf Deutsch:", "baum_mehr": "In der Übersicht ansehen",
           "suche_feld": "Thema, Begriff oder Teilwort suchen …", "baum_laedt": "Wird geladen …",
           "baum_fehler": "Konnte nicht geladen werden.", "suche_volltext": "Volltext wird durchsucht …"},
    "en": {"n_kapitel": "{n} chapters", "n_kapitel_1": "1 chapter", "n_artikel": "{n} articles", "n_artikel_1": "1 article",
           "nur_de": "So far only in German:", "baum_mehr": "View in the overview",
           "suche_feld": "Search for a topic, term or part of a word …", "baum_laedt": "Loading …",
           "baum_fehler": "Could not be loaded.", "suche_volltext": "Searching the full text …"},
    "es": {"n_kapitel": "{n} capítulos", "n_kapitel_1": "1 capítulo", "n_artikel": "{n} artículos", "n_artikel_1": "1 artículo",
           "nur_de": "Por ahora solo en alemán:", "baum_mehr": "Ver en la vista general",
           "suche_feld": "Buscar un tema, un término o parte de una palabra …", "baum_laedt": "Cargando …",
           "baum_fehler": "No se pudo cargar.", "suche_volltext": "Buscando en el texto completo …"},
    "zh": {"n_kapitel": "{n} 章", "n_kapitel_1": "1 章", "n_artikel": "{n} 篇文章", "n_artikel_1": "1 篇文章",
           "nur_de": "目前只有德语版：", "baum_mehr": "在总览中查看",
           "suche_feld": "搜索主题、术语或词的一部分 …", "baum_laedt": "加载中 …",
           "baum_fehler": "无法加载。", "suche_volltext": "正在搜索全文 …"},
    "fr": {"n_kapitel": "{n} chapitres", "n_kapitel_1": "1 chapitre", "n_artikel": "{n} articles", "n_artikel_1": "1 article",
           "nur_de": "Pour l’instant uniquement en allemand :", "baum_mehr": "Voir dans la vue d’ensemble",
           "suche_feld": "Rechercher un thème, une notion ou une partie de mot …", "baum_laedt": "Chargement …",
           "baum_fehler": "Chargement impossible.", "suche_volltext": "Recherche dans le texte intégral …"},
    "tr": {"n_kapitel": "{n} bölüm", "n_kapitel_1": "1 bölüm", "n_artikel": "{n} makale", "n_artikel_1": "1 makale",
           "nur_de": "Şimdilik yalnızca Almanca:", "baum_mehr": "Genel bakışta gör",
           "suche_feld": "Konu, kavram veya kelime parçası ara …", "baum_laedt": "Yükleniyor …",
           "baum_fehler": "Yüklenemedi.", "suche_volltext": "Tam metinde aranıyor …"},
}
for _l, _w in _UI_FINDEN.items():
    UI[_l].update(_w)

# Ansichten (W4a, 11.11.2026): Ausführlich | Kurz | Formeln je Artikel, Formelsammlung und „Kapitel auf einer Seite“ je Modul
_UI_ANSICHT = {
    "de": {"ans": "Ansicht", "ans_voll": "Ausführlich", "ans_kurz": "Kurz", "ans_formeln": "Formeln",
           "ans_kurz_min": "Kurz: {n} min", "fb_leer": "Dieser Artikel hat keine Formeln.", "fb_zu_kurz": "Zur Kurzansicht",
           "fb_modul": "Alle Formeln des Moduls", "fb_titel": "Formelsammlung", "fb_sprung": "An die Stelle im Artikel",
           "fb_lede": "Die Sätze, Definitionen und nummerierten Formeln aller Artikel dieses Moduls, nach Kapiteln geordnet. "
                      "Jeder Eintrag führt an seine Stelle im Artikel.",
           "fb_keine": "Für dieses Modul gibt es noch keine Formeln.",
           "sz_titel": "Kapitel auf einer Seite", "sz_kurz": "Kapitel auf einer Seite",
           "sz_lede": "Die Zusammenfassungen aller Artikel, Kapitel für Kapitel: Begriffe, Formeln und Zusammenhänge. "
                      "Wähle ein Kapitel, dann druckt der Browser nur dieses.",
           "sz_keine": "Für dieses Modul gibt es noch keine Zusammenfassungen.",
           "kap_wahl": "Kapitel", "kap_alle": "Alle Kapitel", "drucken": "Drucken",
           "dl": "Herunterladen", "dl_laeuft": "Wird erstellt …", "dl_fehler": "Das Erstellen hat nicht geklappt.",
           "dl_gross": "Zu lang für ein Bild. Wähle ein Kapitel oder nimm PDF.", "fb_quelle": "Formeln"},
    "en": {"ans": "View", "ans_voll": "Detailed", "ans_kurz": "Short", "ans_formeln": "Formulas",
           "ans_kurz_min": "Short: {n} min", "fb_leer": "This article has no formulas.", "fb_zu_kurz": "Go to the short view",
           "fb_modul": "All formulas of the module", "fb_titel": "Formula collection", "fb_sprung": "Go to the place in the article",
           "fb_lede": "The theorems, definitions and numbered formulas of all articles in this module, ordered by chapter. "
                      "Each entry takes you to its place in the article.",
           "fb_keine": "There are no formulas for this module yet.",
           "sz_titel": "Chapter on one page", "sz_kurz": "Chapter on one page",
           "sz_lede": "The summaries of all articles, chapter by chapter: terms, formulas and key relationships. "
                      "Choose a chapter and the browser prints only that one.",
           "sz_keine": "There are no summaries for this module yet.",
           "kap_wahl": "Chapter", "kap_alle": "All chapters", "drucken": "Print",
           "dl": "Download", "dl_laeuft": "Creating …", "dl_fehler": "Creating the file did not work.",
           "dl_gross": "Too long for one image. Choose a chapter or use PDF.", "fb_quelle": "Formulas"},
    "es": {"ans": "Vista", "ans_voll": "Detallada", "ans_kurz": "Breve", "ans_formeln": "Fórmulas",
           "ans_kurz_min": "Breve: {n} min", "fb_leer": "Este artículo no tiene fórmulas.", "fb_zu_kurz": "Ir a la vista breve",
           "fb_modul": "Todas las fórmulas del módulo", "fb_titel": "Formulario", "fb_sprung": "Ir al lugar en el artículo",
           "fb_lede": "Los teoremas, definiciones y fórmulas numeradas de todos los artículos de este módulo, por capítulos. "
                      "Cada entrada lleva a su lugar en el artículo.",
           "fb_keine": "Todavía no hay fórmulas para este módulo.",
           "sz_titel": "El capítulo en una página", "sz_kurz": "Capítulo en una página",
           "sz_lede": "Los resúmenes de todos los artículos, capítulo a capítulo: términos, fórmulas y relaciones clave. "
                      "Elige un capítulo y el navegador imprime solo ese.",
           "sz_keine": "Todavía no hay resúmenes para este módulo.",
           "kap_wahl": "Capítulo", "kap_alle": "Todos los capítulos", "drucken": "Imprimir",
           "dl": "Descargar", "dl_laeuft": "Creando …", "dl_fehler": "No se pudo crear el archivo.",
           "dl_gross": "Demasiado largo para una imagen. Elige un capítulo o usa PDF.", "fb_quelle": "Fórmulas"},
    "zh": {"ans": "视图", "ans_voll": "详细", "ans_kurz": "简要", "ans_formeln": "公式",
           "ans_kurz_min": "简要：{n} 分钟", "fb_leer": "本文没有公式。", "fb_zu_kurz": "转到简要视图",
           "fb_modul": "本模块全部公式", "fb_titel": "公式汇编", "fb_sprung": "跳到文章中的位置",
           "fb_lede": "本模块所有文章中的定理、定义和带编号的公式，按章节排列。每一条都可以跳到它在文章中的位置。",
           "fb_keine": "本模块暂时还没有公式。",
           "sz_titel": "一页看完一章", "sz_kurz": "一页看完一章",
           "sz_lede": "所有文章的小结，逐章排列：术语、公式和关键联系。选择一章后，浏览器只打印这一章。",
           "sz_keine": "本模块暂时还没有小结。",
           "kap_wahl": "章节", "kap_alle": "全部章节", "drucken": "打印",
           "dl": "下载", "dl_laeuft": "正在生成 …", "dl_fehler": "文件生成失败。",
           "dl_gross": "内容太长，无法生成一张图片。请选择一章或使用 PDF。", "fb_quelle": "公式"},
    "fr": {"ans": "Affichage", "ans_voll": "Détaillé", "ans_kurz": "Court", "ans_formeln": "Formules",
           "ans_kurz_min": "Court : {n} min", "fb_leer": "Cet article ne contient pas de formules.", "fb_zu_kurz": "Passer à l’affichage court",
           "fb_modul": "Toutes les formules du module", "fb_titel": "Formulaire", "fb_sprung": "Aller à l’endroit dans l’article",
           "fb_lede": "Les théorèmes, définitions et formules numérotées de tous les articles de ce module, classés par chapitre. "
                      "Chaque entrée mène à sa place dans l’article.",
           "fb_keine": "Il n’y a pas encore de formules pour ce module.",
           "sz_titel": "Le chapitre sur une page", "sz_kurz": "Chapitre sur une page",
           "sz_lede": "Les résumés de tous les articles, chapitre par chapitre : notions, formules et relations clés. "
                      "Choisissez un chapitre et le navigateur n’imprime que celui-ci.",
           "sz_keine": "Il n’y a pas encore de résumés pour ce module.",
           "kap_wahl": "Chapitre", "kap_alle": "Tous les chapitres", "drucken": "Imprimer",
           "dl": "Télécharger", "dl_laeuft": "Création …", "dl_fehler": "La création du fichier a échoué.",
           "dl_gross": "Trop long pour une image. Choisissez un chapitre ou utilisez le PDF.", "fb_quelle": "Formules"},
    "tr": {"ans": "Görünüm", "ans_voll": "Ayrıntılı", "ans_kurz": "Kısa", "ans_formeln": "Formüller",
           "ans_kurz_min": "Kısa: {n} dk", "fb_leer": "Bu makalede formül yok.", "fb_zu_kurz": "Kısa görünüme geç",
           "fb_modul": "Modülün tüm formülleri", "fb_titel": "Formül derlemesi", "fb_sprung": "Makaledeki yerine git",
           "fb_lede": "Bu modüldeki tüm makalelerin teoremleri, tanımları ve numaralı formülleri, bölümlere göre sıralı. "
                      "Her kayıt sizi makaledeki yerine götürür.",
           "fb_keine": "Bu modül için henüz formül yok.",
           "sz_titel": "Tek sayfada bölüm", "sz_kurz": "Tek sayfada bölüm",
           "sz_lede": "Tüm makalelerin özetleri, bölüm bölüm: kavramlar, formüller ve temel ilişkiler. "
                      "Bir bölüm seçerseniz tarayıcı yalnızca onu yazdırır.",
           "sz_keine": "Bu modül için henüz özet yok.",
           "kap_wahl": "Bölüm", "kap_alle": "Tüm bölümler", "drucken": "Yazdır",
           "dl": "İndir", "dl_laeuft": "Oluşturuluyor …", "dl_fehler": "Dosya oluşturulamadı.",
           "dl_gross": "Tek bir resim için çok uzun. Bir bölüm seçin ya da PDF kullanın.", "fb_quelle": "Formüller"},
}
for _l, _w in _UI_ANSICHT.items():
    UI[_l].update(_w)
# Informatik-Reihen (User 11.11.2026 abends): Die dritte Ansicht heißt dort „Übersicht“ (Befehls- und Syntaxübersicht), die
# Modulseite „Befehlsübersicht“ (uebersicht.html). Inhalt später aus ::::formelsammlung; bis dahin automatisch: Kästen und
# die Eingabezeilen der Konsolen-Blöcke je Abschnitt (siehe md_to_html).
_UI_REF = {
    "de": {"ans_formeln_ref": "Übersicht", "fb_titel_ref": "Befehlsübersicht", "fb_modul_ref": "Befehlsübersicht des Moduls",
           "fb_leer_ref": "Für diesen Artikel gibt es noch keine Übersicht.", "fb_befehle": "Befehle",
           "fb_lede_ref": "Die Definitionen, Regeln und Befehle aller Artikel dieses Moduls, nach Kapiteln geordnet. "
                          "Jeder Eintrag führt an seine Stelle im Artikel.",
           "fb_keine_ref": "Für dieses Modul gibt es noch keine Übersicht."},
    "en": {"ans_formeln_ref": "Reference", "fb_titel_ref": "Command reference", "fb_modul_ref": "Command reference of the module",
           "fb_leer_ref": "There is no reference for this article yet.", "fb_befehle": "Commands",
           "fb_lede_ref": "The definitions, rules and commands of all articles in this module, ordered by chapter. "
                          "Each entry takes you to its place in the article.",
           "fb_keine_ref": "There is no reference for this module yet."},
    "es": {"ans_formeln_ref": "Referencia", "fb_titel_ref": "Referencia de comandos", "fb_modul_ref": "Referencia de comandos del módulo",
           "fb_leer_ref": "Este artículo aún no tiene referencia.", "fb_befehle": "Comandos",
           "fb_lede_ref": "Las definiciones, reglas y comandos de todos los artículos de este módulo, por capítulos. "
                          "Cada entrada lleva a su lugar en el artículo.",
           "fb_keine_ref": "Todavía no hay referencia para este módulo."},
    "zh": {"ans_formeln_ref": "速查", "fb_titel_ref": "命令速查", "fb_modul_ref": "本模块命令速查",
           "fb_leer_ref": "本文暂无速查内容。", "fb_befehle": "命令",
           "fb_lede_ref": "本模块所有文章中的定义、规则和命令，按章节排列。每一条都可以跳到它在文章中的位置。",
           "fb_keine_ref": "本模块暂时还没有速查内容。"},
    "fr": {"ans_formeln_ref": "Aide-mémoire", "fb_titel_ref": "Aide-mémoire des commandes", "fb_modul_ref": "Aide-mémoire des commandes du module",
           "fb_leer_ref": "Cet article n’a pas encore d’aide-mémoire.", "fb_befehle": "Commandes",
           "fb_lede_ref": "Les définitions, règles et commandes de tous les articles de ce module, classées par chapitre. "
                          "Chaque entrée mène à sa place dans l’article.",
           "fb_keine_ref": "Il n’y a pas encore d’aide-mémoire pour ce module."},
    "tr": {"ans_formeln_ref": "Hızlı başvuru", "fb_titel_ref": "Komut başvurusu", "fb_modul_ref": "Modülün komut başvurusu",
           "fb_leer_ref": "Bu makale için henüz başvuru yok.", "fb_befehle": "Komutlar",
           "fb_lede_ref": "Bu modüldeki tüm makalelerin tanımları, kuralları ve komutları, bölümlere göre sıralı. "
                          "Her kayıt sizi makaledeki yerine götürür.",
           "fb_keine_ref": "Bu modül için henüz başvuru yok."},
}
for _l, _w in _UI_REF.items():
    UI[_l].update(_w)
UEBERSICHT_REIHEN = {"linux", "prog", "cyber", "c", "cpp"}   # Ordner unter content/ mit „Übersicht“ statt „Formeln“
MODUL_REF = set()                                             # Moduladressen dieser Reihen, alle Sprachen (main)
LERNEN_JS += ("ans_kurz_min", "dl_laeuft", "dl_fehler", "dl_gross", "fb_titel", "ans_formeln", "fb_titel_ref")

# Bereiche (W4b, 11.11.2026): Wissen · Lernkarten · Aufgaben · Editor in der Kopfleiste; Lernkarten/Quiz/Mischtest unter
# /lernen/, Aufgaben unter /aufgaben/, Verweise unter jedem Artikel. Die Wörter unter BEREICHE_JS braucht bereiche.js.
_UI_BEREICHE = {
    "de": {"b_wissen": "Wissen", "b_lernen": "Lernkarten", "b_aufgaben": "Aufgaben", "b_editor": "Editor", "b_menue": "Bereiche",
           "lw_titel": "Lernkarten und Quiz",
           "lw_lede": "Begriffe, Formeln, Herleitungen und Zusammenhänge aus den Artikeln, für ein ganzes Modul, ein Kapitel oder einen "
                      "einzelnen Artikel. Lerne mit dem Karteikasten, prüfe dich im Quiz oder mische Fragen und Aufgaben zu einem Test. "
                      "Der Lernstand bleibt nur in diesem Browser.",
           "lw_modul": "Modul", "lw_artikel": "Artikel", "lw_alle_art": "Alle Artikel", "lw_arten": "Kartenarten",
           "typ_h": "Herleitungen", "typ1_l": "Zusammenhang", "mod_lernen": "Lernen", "mod_quiz": "Quiz", "mod_test": "Mischtest",
           "lw_waehle": "Wähle ein Modul.", "lw_keine": "In dieser Auswahl gibt es keine Karten.", "lw_karten_n": "{n} Karten",
           "lw_statisch": "Ohne JavaScript stehen die Begriffe, Formeln und Aufgaben jedes Moduls auf eigenen Seiten:",
           "lw_umgezogen": "Die Lernkarten haben jetzt einen eigenen Bereich:",
           "hl_ziel": "Ziel", "hl_start": "Ausgangspunkt", "hl_weiter": "Nächster Schritt", "hl_schritt": "Schritt {n} von {m}",
           "quiz_zahl": "Fragen", "quiz_start": "Quiz starten", "quiz_frage": "Frage {n} von {m}",
           "quiz_p_b": "Welche Bestimmung passt zu diesem Begriff?", "quiz_p_f": "Welche Formel gehört dazu?",
           "quiz_p_l": "Was gehört in die Lücke?", "quiz_p_w": "Welche Antwort passt?", "quiz_weiter": "Weiter",
           "quiz_ende": "Zur Auswertung", "quiz_auswertung": "Auswertung", "quiz_ergebnis": "{n} von {m} richtig",
           "quiz_falsch": "Noch einmal ansehen", "quiz_alle": "Alles richtig.", "quiz_neu": "Neues Quiz",
           "quiz_deine": "Deine Antwort", "quiz_richtig": "Richtig ist", "q_ok": "richtig", "q_nein": "falsch",
           "quiz_zu_wenig": "Für ein Quiz braucht diese Auswahl mindestens vier Karten einer Art (Begriffe, Formeln oder Zusammenhänge).",
           "quiz_tasten": "Tasten: 1 bis 4 wählen, Eingabe geht weiter.",
           "test_lede": "Eine zufällige Mischung aus Quizfragen und Aufgaben der gewählten Kapitel. Lösungen und Auswertung kommen erst "
                        "am Ende; die Aufgaben bewertest du dann selbst.",
           "test_kapitel": "Kapitel für den Test", "test_alle": "Alle", "test_start": "Test starten",
           "test_aufg_hinweis": "Löse die Aufgabe auf Papier. Die Lösung folgt in der Auswertung.", "test_selbst": "Wie lief es?",
           "bew_richtig": "Richtig", "bew_teil": "Teilweise", "bew_falsch": "Falsch", "test_punkte": "{p} von {m} Punkten",
           "test_offen": "Noch {n} Aufgaben selbst bewerten.",
           "test_ohne_aufg": "Die Aufgaben konnten nicht geladen werden; der Test enthält nur Quizfragen.",
           "test_kein_kap": "Wähle mindestens ein Kapitel.", "test_fortsetzen": "Laufenden Test fortsetzen", "test_neu": "Neuer Test",
           "w_aufgabe": "Aufgabe",
           "ag_lede": "Alle Aufgaben aus den Artikeln mit ausführlichen Lösungen, nach Modul, Kapitel und Artikel geordnet. Welche du "
                      "gelöst hast, merkt sich nur dieser Browser.",
           "ag_modul_lede": "Alle Aufgaben dieses Moduls, nach Kapiteln und Artikeln geordnet. Die Lösung ist zugeklappt; jede Aufgabe "
                            "führt auch an ihre Stelle im Artikel.",
           "ag_geloest": "gelöst", "ag_stand": "{n} von {m} gelöst", "ag_zufall": "Zufällige Aufgabe", "ag_offen": "Nur ungelöste",
           "ag_keine": "Für dieses Modul gibt es noch keine Aufgaben.", "ag_leer": "Keine Aufgabe passt zu dieser Auswahl.",
           "ag_reset": "Gelöst-Häkchen zurücksetzen", "ag_test": "Mischtest mit diesen Aufgaben",
           "vw_lernen": "Lernkarten:", "vw_aufgaben": "Aufgaben:", "vw_artikel": "dieser Artikel", "vw_kapitel": "Kapitel",
           "vw_modul": "Modul", "vw_label": "Weiter üben", "b_thema": "Hell/Dunkel"},
    "en": {"b_wissen": "Knowledge", "b_lernen": "Flashcards", "b_aufgaben": "Exercises", "b_editor": "Editor", "b_menue": "Sections",
           "lw_titel": "Flashcards and quiz",
           "lw_lede": "Terms, formulas, derivations and key relationships from the articles, for a whole module, a chapter or a single "
                      "article. Learn with the card box, check yourself in a quiz or mix questions and exercises into a test. Your "
                      "progress stays in this browser only.",
           "lw_modul": "Module", "lw_artikel": "Article", "lw_alle_art": "All articles", "lw_arten": "Card types",
           "typ_h": "Derivations", "typ1_l": "Key relationship", "mod_lernen": "Learn", "mod_quiz": "Quiz", "mod_test": "Mixed test",
           "lw_waehle": "Choose a module.", "lw_keine": "There are no cards in this selection.", "lw_karten_n": "{n} cards",
           "lw_statisch": "Without JavaScript, the terms, formulas and exercises of each module are on their own pages:",
           "lw_umgezogen": "Flashcards now have their own section:",
           "hl_ziel": "Goal", "hl_start": "Starting point", "hl_weiter": "Next step", "hl_schritt": "Step {n} of {m}",
           "quiz_zahl": "Questions", "quiz_start": "Start quiz", "quiz_frage": "Question {n} of {m}",
           "quiz_p_b": "Which definition fits this term?", "quiz_p_f": "Which formula belongs to it?",
           "quiz_p_l": "What goes in the gap?", "quiz_p_w": "Which answer fits?", "quiz_weiter": "Next",
           "quiz_ende": "See results", "quiz_auswertung": "Results", "quiz_ergebnis": "{n} of {m} correct",
           "quiz_falsch": "Worth another look", "quiz_alle": "All correct.", "quiz_neu": "New quiz",
           "quiz_deine": "Your answer", "quiz_richtig": "Correct answer", "q_ok": "correct", "q_nein": "wrong",
           "quiz_zu_wenig": "A quiz needs at least four cards of one type in this selection (terms, formulas or key relationships).",
           "quiz_tasten": "Keys: 1 to 4 choose, Enter continues.",
           "test_lede": "A random mix of quiz questions and exercises from the chosen chapters. Solutions and results come only at the "
                        "end; you then rate the exercises yourself.",
           "test_kapitel": "Chapters for the test", "test_alle": "All", "test_start": "Start test",
           "test_aufg_hinweis": "Solve the exercise on paper. The solution follows in the results.", "test_selbst": "How did it go?",
           "bew_richtig": "Correct", "bew_teil": "Partly", "bew_falsch": "Wrong", "test_punkte": "{p} of {m} points",
           "test_offen": "Rate {n} more exercises yourself.",
           "test_ohne_aufg": "The exercises could not be loaded; the test contains only quiz questions.",
           "test_kein_kap": "Choose at least one chapter.", "test_fortsetzen": "Continue the current test", "test_neu": "New test",
           "w_aufgabe": "Exercise",
           "ag_lede": "All exercises from the articles with detailed solutions, ordered by module, chapter and article. Which ones you "
                      "have solved is remembered by this browser only.",
           "ag_modul_lede": "All exercises of this module, ordered by chapter and article. The solution is collapsed; each exercise also "
                            "links to its place in the article.",
           "ag_geloest": "solved", "ag_stand": "{n} of {m} solved", "ag_zufall": "Random exercise", "ag_offen": "Unsolved only",
           "ag_keine": "There are no exercises for this module yet.", "ag_leer": "No exercise matches this selection.",
           "ag_reset": "Reset solved marks", "ag_test": "Mixed test with these exercises",
           "vw_lernen": "Flashcards:", "vw_aufgaben": "Exercises:", "vw_artikel": "this article", "vw_kapitel": "chapter",
           "vw_modul": "module", "vw_label": "Keep practising", "b_thema": "Light/dark"},
    "es": {"b_wissen": "Conocimiento", "b_lernen": "Tarjetas", "b_aufgaben": "Ejercicios", "b_editor": "Editor", "b_menue": "Secciones",
           "lw_titel": "Tarjetas y cuestionario",
           "lw_lede": "Términos, fórmulas, deducciones y relaciones clave de los artículos, para un módulo entero, un capítulo o un solo "
                      "artículo. Aprende con el fichero de tarjetas, ponte a prueba en un cuestionario o mezcla preguntas y ejercicios "
                      "en una prueba. Tu progreso se queda solo en este navegador.",
           "lw_modul": "Módulo", "lw_artikel": "Artículo", "lw_alle_art": "Todos los artículos", "lw_arten": "Tipos de tarjeta",
           "typ_h": "Deducciones", "typ1_l": "Relación clave", "mod_lernen": "Aprender", "mod_quiz": "Cuestionario", "mod_test": "Prueba mixta",
           "lw_waehle": "Elige un módulo.", "lw_keine": "No hay tarjetas en esta selección.", "lw_karten_n": "{n} tarjetas",
           "lw_statisch": "Sin JavaScript, los términos, fórmulas y ejercicios de cada módulo están en páginas propias:",
           "lw_umgezogen": "Las tarjetas tienen ahora su propia sección:",
           "hl_ziel": "Objetivo", "hl_start": "Punto de partida", "hl_weiter": "Siguiente paso", "hl_schritt": "Paso {n} de {m}",
           "quiz_zahl": "Preguntas", "quiz_start": "Empezar el cuestionario", "quiz_frage": "Pregunta {n} de {m}",
           "quiz_p_b": "¿Qué definición corresponde a este término?", "quiz_p_f": "¿Qué fórmula le corresponde?",
           "quiz_p_l": "¿Qué va en el hueco?", "quiz_p_w": "¿Qué respuesta corresponde?", "quiz_weiter": "Siguiente",
           "quiz_ende": "Ver resultados", "quiz_auswertung": "Resultados", "quiz_ergebnis": "{n} de {m} correctas",
           "quiz_falsch": "Para repasar", "quiz_alle": "Todo correcto.", "quiz_neu": "Nuevo cuestionario",
           "quiz_deine": "Tu respuesta", "quiz_richtig": "Respuesta correcta", "q_ok": "correcta", "q_nein": "incorrecta",
           "quiz_zu_wenig": "Para un cuestionario, esta selección necesita al menos cuatro tarjetas de un mismo tipo (términos, fórmulas "
                            "o relaciones clave).",
           "quiz_tasten": "Teclas: 1 a 4 eligen, Intro continúa.",
           "test_lede": "Una mezcla aleatoria de preguntas y ejercicios de los capítulos elegidos. Las soluciones y los resultados llegan "
                        "al final; entonces valoras tú mismo los ejercicios.",
           "test_kapitel": "Capítulos para la prueba", "test_alle": "Todos", "test_start": "Empezar la prueba",
           "test_aufg_hinweis": "Resuelve el ejercicio en papel. La solución aparece en los resultados.", "test_selbst": "¿Cómo te fue?",
           "bew_richtig": "Bien", "bew_teil": "En parte", "bew_falsch": "Mal", "test_punkte": "{p} de {m} puntos",
           "test_offen": "Faltan {n} ejercicios por valorar.",
           "test_ohne_aufg": "No se pudieron cargar los ejercicios; la prueba solo contiene preguntas.",
           "test_kein_kap": "Elige al menos un capítulo.", "test_fortsetzen": "Continuar la prueba en curso", "test_neu": "Nueva prueba",
           "w_aufgabe": "Ejercicio",
           "ag_lede": "Todos los ejercicios de los artículos con soluciones detalladas, ordenados por módulo, capítulo y artículo. Cuáles "
                      "has resuelto solo lo recuerda este navegador.",
           "ag_modul_lede": "Todos los ejercicios de este módulo, ordenados por capítulos y artículos. La solución está plegada; cada "
                            "ejercicio enlaza también con su lugar en el artículo.",
           "ag_geloest": "resuelto", "ag_stand": "{n} de {m} resueltos", "ag_zufall": "Ejercicio al azar", "ag_offen": "Solo sin resolver",
           "ag_keine": "Todavía no hay ejercicios para este módulo.", "ag_leer": "Ningún ejercicio corresponde a esta selección.",
           "ag_reset": "Restablecer las marcas de resuelto", "ag_test": "Prueba mixta con estos ejercicios",
           "vw_lernen": "Tarjetas:", "vw_aufgaben": "Ejercicios:", "vw_artikel": "este artículo", "vw_kapitel": "capítulo",
           "vw_modul": "módulo", "vw_label": "Seguir practicando", "b_thema": "Claro/oscuro"},
    "zh": {"b_wissen": "知识库", "b_lernen": "学习卡片", "b_aufgaben": "练习", "b_editor": "编辑器", "b_menue": "栏目",
           "lw_titel": "学习卡片与测验",
           "lw_lede": "文章中的术语、公式、推导和关键联系，可按整个模块、某一章或单篇文章选择。用卡片盒学习，用测验检验自己，"
                      "或把问题和练习混合成一次测试。学习进度只保存在本浏览器中。",
           "lw_modul": "模块", "lw_artikel": "文章", "lw_alle_art": "全部文章", "lw_arten": "卡片类型",
           "typ_h": "推导", "typ1_l": "关键联系", "mod_lernen": "学习", "mod_quiz": "测验", "mod_test": "综合测试",
           "lw_waehle": "请选择一个模块。", "lw_keine": "当前选择中没有卡片。", "lw_karten_n": "{n} 张卡片",
           "lw_statisch": "未启用 JavaScript 时，各模块的术语、公式和练习可在单独的页面中查看：",
           "lw_umgezogen": "学习卡片现已移至单独的栏目：",
           "hl_ziel": "目标", "hl_start": "出发点", "hl_weiter": "下一步", "hl_schritt": "第 {n} 步，共 {m} 步",
           "quiz_zahl": "题数", "quiz_start": "开始测验", "quiz_frage": "第 {n} 题，共 {m} 题",
           "quiz_p_b": "哪条说明符合这个术语？", "quiz_p_f": "对应的是哪个公式？",
           "quiz_p_l": "空白处应填什么？", "quiz_p_w": "哪个答案正确？", "quiz_weiter": "下一题",
           "quiz_ende": "查看结果", "quiz_auswertung": "结果", "quiz_ergebnis": "答对 {n} 题，共 {m} 题",
           "quiz_falsch": "值得再看一遍", "quiz_alle": "全部正确。", "quiz_neu": "再测一次",
           "quiz_deine": "你的答案", "quiz_richtig": "正确答案", "q_ok": "正确", "q_nein": "错误",
           "quiz_zu_wenig": "测验需要当前选择中至少有四张同类卡片（术语、公式或关键联系）。",
           "quiz_tasten": "按键：1–4 选择，回车继续。",
           "test_lede": "从所选章节中随机混合测验题和练习。答案和结果最后才显示，练习由你自己评分。",
           "test_kapitel": "测试章节", "test_alle": "全选", "test_start": "开始测试",
           "test_aufg_hinweis": "请在纸上完成这道练习，答案在结果中给出。", "test_selbst": "做得怎么样？",
           "bew_richtig": "正确", "bew_teil": "部分正确", "bew_falsch": "错误", "test_punkte": "{m} 分中得 {p} 分",
           "test_offen": "还有 {n} 道练习需要自评。",
           "test_ohne_aufg": "练习无法加载，本次测试只包含测验题。",
           "test_kein_kap": "请至少选择一章。", "test_fortsetzen": "继续当前测试", "test_neu": "新测试",
           "w_aufgabe": "练习",
           "ag_lede": "文章中的全部练习及详细解答，按模块、章节和文章排列。你做过哪些题只记录在本浏览器中。",
           "ag_modul_lede": "本模块的全部练习，按章节和文章排列。解答默认折叠；每道题都可以跳到它在文章中的位置。",
           "ag_geloest": "已完成", "ag_stand": "已完成 {n} / {m}", "ag_zufall": "随机一题", "ag_offen": "只看未完成",
           "ag_keine": "本模块暂时还没有练习。", "ag_leer": "没有符合当前选择的练习。",
           "ag_reset": "清除完成标记", "ag_test": "用这些练习做综合测试",
           "vw_lernen": "学习卡片：", "vw_aufgaben": "练习：", "vw_artikel": "本文", "vw_kapitel": "本章",
           "vw_modul": "本模块", "vw_label": "继续练习", "b_thema": "浅色/深色"},
    "fr": {"b_wissen": "Connaissances", "b_lernen": "Fiches", "b_aufgaben": "Exercices", "b_editor": "Éditeur", "b_menue": "Rubriques",
           "lw_titel": "Fiches et quiz",
           "lw_lede": "Notions, formules, démonstrations et relations clés des articles, pour un module entier, un chapitre ou un seul "
                      "article. Apprenez avec la boîte à fiches, testez-vous avec un quiz ou mélangez questions et exercices dans un "
                      "test. Votre progression reste uniquement dans ce navigateur.",
           "lw_modul": "Module", "lw_artikel": "Article", "lw_alle_art": "Tous les articles", "lw_arten": "Types de fiches",
           "typ_h": "Démonstrations", "typ1_l": "Relation clé", "mod_lernen": "Apprendre", "mod_quiz": "Quiz", "mod_test": "Test mixte",
           "lw_waehle": "Choisissez un module.", "lw_keine": "Il n’y a pas de fiches dans cette sélection.", "lw_karten_n": "{n} fiches",
           "lw_statisch": "Sans JavaScript, les notions, formules et exercices de chaque module se trouvent sur des pages dédiées\u00a0:",
           "lw_umgezogen": "Les fiches ont désormais leur propre rubrique\u00a0:",
           "hl_ziel": "Objectif", "hl_start": "Point de départ", "hl_weiter": "Étape suivante", "hl_schritt": "Étape {n} sur {m}",
           "quiz_zahl": "Questions", "quiz_start": "Commencer le quiz", "quiz_frage": "Question {n} sur {m}",
           "quiz_p_b": "Quelle définition correspond à cette notion\u202f?", "quiz_p_f": "Quelle formule lui correspond\u202f?",
           "quiz_p_l": "Que faut-il mettre dans le blanc\u202f?", "quiz_p_w": "Quelle réponse convient\u202f?", "quiz_weiter": "Suivant",
           "quiz_ende": "Voir les résultats", "quiz_auswertung": "Résultats", "quiz_ergebnis": "{n} sur {m} correctes",
           "quiz_falsch": "À revoir", "quiz_alle": "Tout est correct.", "quiz_neu": "Nouveau quiz",
           "quiz_deine": "Votre réponse", "quiz_richtig": "Bonne réponse", "q_ok": "correcte", "q_nein": "incorrecte",
           "quiz_zu_wenig": "Pour un quiz, cette sélection doit contenir au moins quatre fiches d’un même type (notions, formules ou "
                            "relations clés).",
           "quiz_tasten": "Touches\u00a0: 1 à 4 pour choisir, Entrée pour continuer.",
           "test_lede": "Un mélange aléatoire de questions et d’exercices des chapitres choisis. Les solutions et les résultats ne "
                        "viennent qu’à la fin\u202f; vous évaluez alors vous-même les exercices.",
           "test_kapitel": "Chapitres du test", "test_alle": "Tous", "test_start": "Commencer le test",
           "test_aufg_hinweis": "Résolvez l’exercice sur papier. La solution suit dans les résultats.",
           "test_selbst": "Comment cela s’est-il passé\u202f?",
           "bew_richtig": "Juste", "bew_teil": "En partie", "bew_falsch": "Faux", "test_punkte": "{p} points sur {m}",
           "test_offen": "Encore {n} exercices à évaluer vous-même.",
           "test_ohne_aufg": "Les exercices n’ont pas pu être chargés\u202f; le test ne contient que des questions.",
           "test_kein_kap": "Choisissez au moins un chapitre.", "test_fortsetzen": "Reprendre le test en cours", "test_neu": "Nouveau test",
           "w_aufgabe": "Exercice",
           "ag_lede": "Tous les exercices des articles avec des solutions détaillées, classés par module, chapitre et article. Seul ce "
                      "navigateur retient ceux que vous avez résolus.",
           "ag_modul_lede": "Tous les exercices de ce module, classés par chapitre et par article. La solution est repliée\u202f; chaque "
                            "exercice renvoie aussi à sa place dans l’article.",
           "ag_geloest": "résolu", "ag_stand": "{n} sur {m} résolus", "ag_zufall": "Exercice au hasard", "ag_offen": "Non résolus seulement",
           "ag_keine": "Il n’y a pas encore d’exercices pour ce module.", "ag_leer": "Aucun exercice ne correspond à cette sélection.",
           "ag_reset": "Réinitialiser les coches «\u00a0résolu\u00a0»", "ag_test": "Test mixte avec ces exercices",
           "vw_lernen": "Fiches\u00a0:", "vw_aufgaben": "Exercices\u00a0:", "vw_artikel": "cet article", "vw_kapitel": "chapitre",
           "vw_modul": "module", "vw_label": "Continuer à s’exercer", "b_thema": "Clair/sombre"},
    "tr": {"b_wissen": "Bilgi", "b_lernen": "Kartlar", "b_aufgaben": "Alıştırmalar", "b_editor": "Editör", "b_menue": "Bölümler",
           "lw_titel": "Kartlar ve test",
           "lw_lede": "Makalelerdeki kavramlar, formüller, türetmeler ve temel ilişkiler; bütün bir modül, bir bölüm ya da tek bir makale "
                      "için. Kart kutusuyla öğrenin, testle kendinizi sınayın ya da soruları ve alıştırmaları karışık bir sınavda "
                      "birleştirin. İlerlemeniz yalnızca bu tarayıcıda kalır.",
           "lw_modul": "Modül", "lw_artikel": "Makale", "lw_alle_art": "Tüm makaleler", "lw_arten": "Kart türleri",
           "typ_h": "Türetmeler", "typ1_l": "Temel ilişki", "mod_lernen": "Öğren", "mod_quiz": "Test", "mod_test": "Karma sınav",
           "lw_waehle": "Bir modül seçin.", "lw_keine": "Bu seçimde kart yok.", "lw_karten_n": "{n} kart",
           "lw_statisch": "JavaScript olmadan her modülün kavramları, formülleri ve alıştırmaları ayrı sayfalarda yer alır:",
           "lw_umgezogen": "Kartların artık kendi bölümü var:",
           "hl_ziel": "Hedef", "hl_start": "Başlangıç noktası", "hl_weiter": "Sonraki adım", "hl_schritt": "Adım {n} / {m}",
           "quiz_zahl": "Soru sayısı", "quiz_start": "Testi başlat", "quiz_frage": "Soru {n} / {m}",
           "quiz_p_b": "Bu kavrama hangi tanım uyar?", "quiz_p_f": "Hangi formül buna aittir?",
           "quiz_p_l": "Boşluğa ne gelir?", "quiz_p_w": "Hangi cevap uyar?", "quiz_weiter": "İleri",
           "quiz_ende": "Sonuçlara git", "quiz_auswertung": "Sonuçlar", "quiz_ergebnis": "{m} sorudan {n} doğru",
           "quiz_falsch": "Tekrar bakın", "quiz_alle": "Hepsi doğru.", "quiz_neu": "Yeni test",
           "quiz_deine": "Cevabınız", "quiz_richtig": "Doğru cevap", "q_ok": "doğru", "q_nein": "yanlış",
           "quiz_zu_wenig": "Test için bu seçimde aynı türden en az dört kart olmalı (kavramlar, formüller veya temel ilişkiler).",
           "quiz_tasten": "Tuşlar: 1–4 seçer, Enter devam eder.",
           "test_lede": "Seçilen bölümlerden rastgele karıştırılmış test soruları ve alıştırmalar. Çözümler ve sonuçlar en sonda gelir; "
                        "alıştırmaları o zaman kendiniz değerlendirirsiniz.",
           "test_kapitel": "Sınav bölümleri", "test_alle": "Tümü", "test_start": "Sınavı başlat",
           "test_aufg_hinweis": "Alıştırmayı kâğıt üzerinde çözün. Çözüm sonuçlarda gelir.", "test_selbst": "Nasıl geçti?",
           "bew_richtig": "Doğru", "bew_teil": "Kısmen", "bew_falsch": "Yanlış", "test_punkte": "{m} puandan {p}",
           "test_offen": "{n} alıştırmayı daha kendiniz değerlendirin.",
           "test_ohne_aufg": "Alıştırmalar yüklenemedi; sınav yalnızca test sorularından oluşuyor.",
           "test_kein_kap": "En az bir bölüm seçin.", "test_fortsetzen": "Süren sınava devam et", "test_neu": "Yeni sınav",
           "w_aufgabe": "Alıştırma",
           "ag_lede": "Makalelerdeki tüm alıştırmalar ayrıntılı çözümleriyle; modül, bölüm ve makaleye göre sıralı. Hangilerini "
                      "çözdüğünüzü yalnızca bu tarayıcı hatırlar.",
           "ag_modul_lede": "Bu modülün tüm alıştırmaları, bölümlere ve makalelere göre sıralı. Çözüm kapalıdır; her alıştırma "
                            "makaledeki yerine de bağlanır.",
           "ag_geloest": "çözüldü", "ag_stand": "{m} alıştırmadan {n} çözüldü", "ag_zufall": "Rastgele alıştırma",
           "ag_offen": "Yalnızca çözülmemiş",
           "ag_keine": "Bu modül için henüz alıştırma yok.", "ag_leer": "Bu seçime uyan alıştırma yok.",
           "ag_reset": "Çözüldü işaretlerini sıfırla", "ag_test": "Bu alıştırmalarla karma sınav",
           "vw_lernen": "Kartlar:", "vw_aufgaben": "Alıştırmalar:", "vw_artikel": "bu makale", "vw_kapitel": "bölüm",
           "vw_modul": "modül", "vw_label": "Pratiğe devam", "b_thema": "Açık/koyu"},
}
for _l, _w in _UI_BEREICHE.items():
    UI[_l].update(_w)
BEREICHE_JS = ("lw_modul", "lw_artikel", "lw_alle_art", "lw_arten", "typ_h", "typ1_l", "mod_lernen", "mod_quiz", "mod_test",
               "lw_waehle", "lw_keine", "lw_karten_n", "hl_ziel", "hl_start", "hl_weiter", "hl_schritt", "quiz_zahl", "quiz_start",
               "quiz_frage", "quiz_p_b", "quiz_p_f", "quiz_p_l", "quiz_p_w", "quiz_weiter", "quiz_ende", "quiz_auswertung",
               "quiz_ergebnis", "quiz_falsch", "quiz_alle", "quiz_neu", "quiz_deine", "quiz_richtig", "q_ok", "q_nein",
               "quiz_zu_wenig", "quiz_tasten", "test_lede", "test_kapitel", "test_alle", "test_start", "test_aufg_hinweis",
               "test_selbst", "bew_richtig", "bew_teil", "bew_falsch", "test_punkte", "test_offen", "test_ohne_aufg",
               "test_kein_kap", "test_fortsetzen", "test_neu", "w_aufgabe", "ag_geloest", "ag_stand", "ag_leer",
               "zf_begriffe", "zf_formeln", "zf_zusammenhaenge", "lk_begriff", "lk_formel", "herleitung", "loesung",
               "lk_kapitel", "lk_alle_kap", "lk_faellig", "lk_davon_neu", "lk_umdrehen", "lk_gut", "lk_mittel", "lk_schlecht",
               "lk_stelle", "lk_fertig", "lk_mehr_neu", "lk_heute", "lk_morgen", "lk_tage", "lk_reset", "lk_ohne_speicher",
               "lk_tasten", "baum_laedt", "baum_fehler", "reset_sicher")

def ist_ref(art):
    return art.get("reihe") in UEBERSICHT_REIHEN

def blatt_datei(mp):
    """Modulseite der dritten Ansicht: Formelsammlung (formeln.html) bzw. Befehlsübersicht (uebersicht.html)."""
    return "uebersicht.html" if mp in MODUL_REF else "formeln.html"

def TR(key, ref):
    """Wort der dritten Ansicht: in den Informatik-Reihen die Fassung *_ref („Übersicht“ statt „Formeln“)."""
    return T(key + "_ref") if ref and key + "_ref" in UI["de"] else T(key)

def anzahl(n, wort):
    """„1 Kapitel“ / „12 Kapitel“ in der Sprache der Seite (wort = n_kapitel, n_artikel)."""
    return T(wort + "_1") if n == 1 else T(wort).format(n=n)

def T(key):
    """Wort der Oberfläche in der Sprache der gerade gebauten Seite."""
    return UI[LANG_NOW[0]].get(key) or UI["de"][key]

def home():
    return "/wissen/" if LANG_NOW[0] == "de" else f"/wissen/{LANG_NOW[0]}/"

# ---------------------------------------------------------------- helpers ----
_ZERLEGT = str.maketrans({"ı": "i", "œ": "oe", "Œ": "OE", "æ": "ae", "Æ": "AE"})   # zerfallen nicht per NFKD

def slugify(s):
    s = unicodedata.normalize("NFKD", s.translate(_ZERLEGT)).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "x"

def fold(s):
    """Normalise for search: lowercase, strip diacritics, ß->ss, ı->i, œ->oe — so 'Übertragung' matches 'ubertragung'."""
    s = s.lower().replace("ß", "ss").translate(_ZERLEGT)
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))

def parse_frontmatter(text):
    meta, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            head = text[3:end].strip("\n")
            body = text[end + 4:].lstrip("\n")
            for line in head.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().lower()] = v.strip()
    return meta, body

# ---------------------------------------------------------- markdown (subset) ----
# Supported: # ## ### headings (with ids), paragraphs, **bold** *italic* `code`, [t](u),
# ![alt](src), - / 1. lists, ``` fenced code ```, > blockquote, --- rule, raw <html> lines,
# callouts ':::konzept' / ':::kern' / ':::merke ... :::', and $…$ / $$…$$ left intact for KaTeX.
# Editor figures: ':::abbildung <szene>' + caption lines + ':::' (see abbildung_html; placeholder: ':::grafik').
_PROTECT = []
def _protect(m):
    _PROTECT.append(m.group(0)); return f"\x00{len(_PROTECT)-1}\x00"

_MC_LINKS, _MC_REL, _MC_RECHTS = "#1b7f4a", "#15633a", "#c2410c"   # linke Seite grün (heller), Relation grün, rechte Seite orange
def colorize_math(s):
    """Colour an (in)equation: left-hand side RED, every relation ('=' or '\\approx') BLUE, the
    part after it GOLD (via KaTeX \\textcolor). Splits only on a *top-level* relation (brace depth 0),
    so \\frac{..}{..}, \\text{..} and units stay intact. An expression without any relation (a lone
    symbol) is left in the normal colour — it then follows the surrounding text colour. A trailing
    equation number \\tag{..} stays outside the colours."""
    mt = re.search(r"\s*\\tag\{[^{}]*\}\s*$", s)
    if mt:
        return colorize_math(s[:mt.start()]) + mt.group(0)
    segs, rels, depth, last, i = [], [], 0, 0, 0
    while i < len(s):
        c = s[i]
        # Umgebungen (cases, pmatrix …) zählen wie eine Klammer: ein '=' darin (etwa „x=0" in einer
        # Fallunterscheidung) darf nie trennen, sonst landen \begin und \end in verschiedenen \textcolor-Gruppen.
        if s.startswith("\\begin{", i):
            j = s.find("}", i + 7)
            depth += 1; i = (j + 1) if j != -1 else len(s); continue
        if s.startswith("\\end{", i):
            j = s.find("}", i + 5)
            depth -= 1; i = (j + 1) if j != -1 else len(s); continue
        if c == "{":
            depth += 1; i += 1; continue
        if c == "}":
            depth -= 1; i += 1; continue
        if depth == 0:
            if c == "=" and (s[i - 1] if i else "") not in "<>!:" and (s[i + 1] if i + 1 < len(s) else "") != "=":
                segs.append(s[last:i]); rels.append("="); last = i + 1; i += 1; continue
            if s.startswith(r"\approx", i):
                segs.append(s[last:i]); rels.append(r"\approx"); last = i + 7; i += 7; continue
        i += 1
    segs.append(s[last:])
    if not rels:
        return s
    out = r"\textcolor{%s}{%s}" % (_MC_LINKS, segs[0])
    for rel, seg in zip(rels, segs[1:]):
        out += r"\textcolor{%s}{%s}\textcolor{%s}{%s}" % (_MC_REL, rel, _MC_RECHTS, seg)
    return out

def inline(text):
    """Inline markdown -> HTML. Math ($…$, $$…$$) and `code` are protected from other rules."""
    _PROTECT.clear()
    # `` a ` b ``: Code mit Gravis darin (CommonMark-Form, heft_zu_artikel.code_span, seit 10.11.2026)
    text = re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$|`` .+? ``|`[^`]+?`", _protect, text, flags=re.S)
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # Namen (Größen-/Begriffsnamen) -> blau: __Name__; erste Nennung eines Fachbegriffs mit Sprungziel (_zf_begriffe)
    text = re.sub(r"__(?:\x01([\w-]+)\x01)?([^_]+)__",
                  lambda m: '<strong class="nm"' + (f' id="{m.group(1)}"' if m.group(1) else "") + ">" + m.group(2) + "</strong>", text)
    # Wichtige Wörter -> orange (Standard); Schritt-Marken „**Schritt 3**" -> rot
    def _bold(m):
        t = m.group(1)
        if re.match(r"^\s*Schritt\s+\d+\s*$", t):
            return '<strong class="step">' + t + "</strong>"
        return "<strong>" + t + "</strong>"
    text = re.sub(r"\*\*((?:[^*]|\*(?!\*))+?)\*\*", _bold, text)   # darf ein *kursives* Wort enthalten
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    def restore(m):
        lead, raw, tail = m.group(1), _PROTECT[int(m.group(2))], m.group(3)
        if raw.startswith("`` "):
            return lead + "<code>" + html.escape(raw[3:-3], quote=False) + "</code>" + tail
        if raw.startswith("`"):
            return lead + "<code>" + html.escape(raw[1:-1], quote=False) + "</code>" + tail
        # Mathe HTML-maskieren: „a<X" würde der Browser sonst als Tag-Anfang lesen und die Formel verschlucken;
        # KaTeX liest den Textinhalt und bekommt so wieder das echte „<", „>" und „&".
        if raw.startswith("$$"):
            return lead + "$$" + html.escape(colorize_math(raw[2:-2]), quote=False) + "$$" + tail
        if raw.startswith("$"):
            body = "$" + html.escape(colorize_math(raw[1:-1]), quote=False) + "$"
            # Neben einer KaTeX-Formel darf der Browser umbrechen (auch ein Wortverbinder hilft in Chrome nicht);
            # ein Punkt, eine Klammer oder „-Achse" stünde dann allein am Zeilenanfang. Kurze Formeln werden darum mit
            # ihren anliegenden Satzzeichen untrennbar geklammert; lange behalten ihre Umbruchstellen.
            if (lead or tail) and len(re.sub(r"[{}\s]", "", re.sub(r"\\[A-Za-z]+", "#", raw[1:-1]))) <= 24:
                return '<span class="nobr">' + lead + body + tail + "</span>"
            return lead + body + tail
        return lead + raw + tail
    return re.sub(r"([(„]?)\x00(\d+)\x00([.,;:!?)“”-]?)", restore, text)

def split_display(txt):
    """Absatz, der nur aus EINER abgesetzten Formel $$…$$ besteht und mehrere durch \\qquad getrennte Teile hat
    -> Liste der Teile (sonst None). Getrennt wird nur auf oberster Ebene (nicht in {…}, \\begin…\\end, \\left…\\right),
    damit die Teile in schmalen Spalten untereinander umbrechen können, statt abgeschnitten zu werden."""
    m = re.fullmatch(r"\$\$(.+)\$\$", txt, flags=re.S)
    if not m or "$$" in m.group(1):
        return None
    s, parts, depth, last, i = m.group(1), [], 0, 0, 0
    def cmd(name):                                        # Befehl \name an Stelle i (nicht Anfang eines längeren Namens)?
        return s.startswith(name, i) and not s[i + len(name):i + len(name) + 1].isalpha()
    while i < len(s):
        if s.startswith("\\begin{", i) or s.startswith("\\end{", i):   # Umgebung zählt wie eine Klammer
            depth += 1 if s.startswith("\\begin{", i) else -1
            j = s.find("}", i); i = (j + 1) if j != -1 else len(s); continue
        if cmd("\\left"):
            depth += 1; i += 5; continue
        if cmd("\\right"):
            depth -= 1; i += 6; continue
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            if depth == 0 and cmd("\\qquad"):
                parts.append(s[last:i]); last = i + 6; i += 6; continue
            i += 2; continue                              # Escape (\{, \\ …) bzw. Befehlsanfang überspringen
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    parts.append(s[last:])
    parts = [p.strip() for p in parts if p.strip()]
    return parts if len(parts) >= 2 else None

# ---------------------------------------------------------- Klartext (Titel, Beschreibung) ----
# <title>, meta description und Attribute (title, aria-label) zeigen kein KaTeX: $U_\mathrm{BE}$ -> „U_BE“, $\pi$ -> „π“,
# $\mathrm{e}^{pt}$ -> „eᵖᵗ“. Die sichtbare Überschrift bleibt TeX und wird von KaTeX gesetzt.
_TEX_ZEICHEN = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε", "zeta": "ζ", "eta": "η",
    "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π",
    "rho": "ρ", "varrho": "ϱ", "sigma": "σ", "tau": "τ", "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ",
    "Omega": "Ω", "cdot": "·", "times": "×", "to": "→", "rightarrow": "→", "infty": "∞", "le": "≤", "leq": "≤", "ge": "≥",
    "geq": "≥", "neq": "≠", "ne": "≠", "approx": "≈", "pm": "±", "sum": "Σ", "prod": "∏", "int": "∫", "partial": "∂",
    "nabla": "∇", "in": "∈", "ldots": "…", "dots": "…", "cdots": "⋯", "circ": "∘", "ast": "∗", "R": "ℝ", "C": "ℂ", "N": "ℕ",
    "Z": "ℤ", "Q": "ℚ", "top": "T", "lVert": "‖", "rVert": "‖", "Vert": "‖", "lvert": "|", "rvert": "|", "mid": "|",
    "langle": "⟨", "rangle": "⟩", "mapsto": "↦", "Rightarrow": "⇒", "Longrightarrow": "⇒", "Leftrightarrow": "⇔",
    "subset": "⊂", "subseteq": "⊆", "cup": "∪", "cap": "∩", "emptyset": "∅", "forall": "∀", "exists": "∃", "sim": "∼",
    "equiv": "≡", "propto": "∝", "ell": "ℓ", "hbar": "ℏ", "deg": "deg", "log": "log", "ln": "ln", "exp": "exp",
    "sin": "sin", "cos": "cos", "tan": "tan", "max": "max", "min": "min", "lim": "lim", "det": "det"}
_TEX_BB = {"R": "ℝ", "C": "ℂ", "N": "ℕ", "Z": "ℤ", "Q": "ℚ"}
_HOCH = dict(zip("0123456789+-=()nipthTabcdekmosxj", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵖᵗʰᵀᵃᵇᶜᵈᵉᵏᵐᵒˢˣʲ"))
_TIEF = dict(zip("0123456789+-=()aeoxhklmnpstijruv", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ"))

def _tex_klar(t):
    """Eine TeX-Formel als lesbarer Klartext (nur für Titel und Beschreibungen, keine vollständige Umsetzung)."""
    t = t.replace("\\{", "\x03").replace("\\}", "\x04")       # Mengenklammern bleiben, Gruppenklammern fallen weg
    t = re.sub(r"\\([%_#&$])", r"\1", t)
    t = re.sub(r"\\(?:vec|hat|bar|dot|ddot|tilde|overline|underline|widehat)\s*(?=[{\w])", "", t)
    t = re.sub(r"\\mathcal\s*\{L\}", "ℒ", t)
    t = re.sub(r"\\mathbb\s*\{(\w)\}", lambda m: _TEX_BB.get(m.group(1), m.group(1)), t)
    t = re.sub(r"\\(?:mathrm|text|textrm|operatorname|mathit|mathbf|boldsymbol|textbf|mathsf)\s*(\{[^{}]*\}|\w)",
               lambda m: "{" + m.group(1).strip("{}") + "}", t)
    t = re.sub(r"\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"\1/\2", t)
    t = re.sub(r"\\sqrt\s*\{([^{}]*)\}", r"√\1", t)
    t = re.sub(r"\\(?:left|right|big|Big|displaystyle)\b", "", t)
    t = re.sub(r"\\[,;:! ]|\\q?quad\b", " ", t)
    t = re.sub(r"\\([A-Za-z]+)", lambda m: _TEX_ZEICHEN.get(m.group(1), m.group(1)), t)
    def index(m, tabelle, zeichen):
        inhalt = m.group(1)[1:-1] if m.group(1).startswith("{") else m.group(1)
        inhalt = inhalt.replace("{", "").replace("}", "")
        if inhalt and all(c in tabelle for c in inhalt):
            return "".join(tabelle[c] for c in inhalt)
        return zeichen + inhalt
    t = re.sub(r"\^\s*(\{[^{}]*\}|.)", lambda m: index(m, _HOCH, "^"), t)
    t = re.sub(r"_\s*(\{[^{}]*\}|.)", lambda m: index(m, _TIEF, "_"), t)
    t = t.replace("{", "").replace("}", "").replace("\x03", "{").replace("\x04", "}")
    return re.sub(r"\s+", " ", t).strip()

def klartext(s):
    """Markdown mit $…$-Formeln als einzeiliger Klartext: für <title>, meta description, title- und aria-Attribute."""
    s = re.sub(r"\$\$(.+?)\$\$|\$([^$\n]+?)\$", lambda m: _tex_klar(m.group(1) or m.group(2)), s or "", flags=re.S)
    s = re.sub(r"\\([%_#&])", r"\1", s)                     # Reste aus summary: (Formeln schon ohne $): „\%“, „span\vec“
    s = re.sub(r"\\([A-Za-z]+)", lambda m: _TEX_ZEICHEN.get(m.group(1), ""), s)
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\*\*|__|`", "", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r" +([.,])(?=\s|$)", r"\1", s)            # „in p .“ (Formel am Satzende war im Kopf schon entfernt)

# ---------------------------------------------- Zusammenfassung am Artikelende ----
# Der Kasten „Zusammenfassung“ entsteht ganz aus dem Markdown, ohne eigenen Heft-Kasten (User 11.11.2026: „die wichtigsten
# Begriffe, Formeln und Zusammenhänge stichpunktartig“):
#   Begriffe       = __Fachbegriff__ (\fb im Heft) bei seiner ersten Nennung, mit dem Satz dieser Nennung als Bestimmung;
#   Formeln        = abgesetzte Formeln in Satz-, Definitions-, Lemma- und Merke-Kästen, dazu nummerierte Formeln (\tag);
#   Zusammenhänge  = die „Kurz gesagt“-Sätze.
# Es zählt nur der Haupttext: Beispiele, Aufgaben, Lösungen, Herleitungen, Hintergrund und andere ergänzende Kästen bleiben
# draußen. md_to_html sammelt nur, solange ZF["an"] gilt (render_article, für den Artikel selbst); jede gesammelte Stelle
# bekommt eine id (kb-, kf-, kg-), auf die der Stichpunkt springt.
ZF = {"an": False}
_KASTEN = []                                              # Kästen um die gerade gesetzte Stelle, innen zuletzt: [(Art, Titel)]
ZF_NEBEN = {"beispiel", "vorwissen", "quiz", "herleitung", "beweis", "aufgabe", "loesung", "ltspice", "frage", "grafik",
            "zusatz", "hintergrund", "analogie", "zweck", "zitat", "kern", "konzept"}
ZF_FORMELKASTEN = ("satz", "definition", "lemma", "merke", "formel")
ZF_SICHTBAR = 5                                           # je Gruppe sichtbar, der Rest unter „N weitere zeigen“
ZF_BESTIMMUNG_MAX = 200                                   # längere Sätze: nur der Begriff
KURZ_RE = re.compile(r"\u2060?\*\*(?:Kurz gesagt|In short|En resumen|En bref|Kısacası|简而言之)\s*[:：]\s*\*\*\s*")
_MASKE_RE = re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$|`` .+? ``|`[^`]+?`", re.S)   # Formeln und Code wie in inline()
_ABKUERZUNG = {"bzw", "ca", "vgl", "usw", "etc", "evtl", "ggf", "inkl", "nr", "abb", "kap", "gl", "sog", "bspw", "bsp", "resp",
               "vs", "cf", "eq", "eqs", "fig", "approx", "max", "min", "bzgl", "ff", "st", "dr", "prof", "no", "art", "abs", "zb"}
# Satzanfang mit Rückbezug („Das ist das Pol-Nullstellen-Diagramm.“): Dann gehört der Satz davor zur Bestimmung.
_RUECKBEZUG = re.compile(r"(?:(?:das|dies|diese|dieser|dieses|diesen|sie|er|es|so|man nennt|this|that|these|those|such|it|they|"
                         r"esto|eso|esta|este|estos|estas|ello|así|cela|ceci|ce|cette|ces|cet|il|elle|ils|elles|bu|buna|bunu|"
                         r"bunun|bunlar|bunlara|böyle|şu)\b|[这此它该])", re.I)

def zf_start(ref=False):
    ZF.clear()
    # blatt/ku/nk (W4a): Einträge des Formelblatts und Ersatzformeln; eigener Zähler, die Nummern von kb/kf/kg bleiben gleich.
    # ref: Informatik-Reihe („Übersicht“): alle Kästen, dazu die Befehle der Konsolen-Blöcke
    ZF.update(an=True, fb=[], fm=[], kg=[], schon=set(), n=0, h="", blatt=[], ku=[], nk=0, ref=ref,
              hl=[], ag=[])                            # W4b: Herleitungen (Lernkarten) und Aufgaben (Bereich „Aufgaben“)

_EINGABE_RE = re.compile(r"^(?:\$ |# |>>> |\.\.\. |PS> )\S")   # Eingabezeile einer Konsolen-Sitzung (wie codeText in wissen.js)

def _blatt_befehle(info, code):
    """Übersicht (Informatik-Reihen): Eingabezeilen eines Konsolen-Blocks im Haupttext merken; Rückgabe: id oder ""."""
    if not (ZF.get("ref") and _zf_haupt()) or info.partition(" ")[0].lower() != "console":
        return ""
    zeilen = []
    for z in code.split("\n"):
        z = z.rstrip()
        if _EINGABE_RE.match(z) and "cmd:" + z not in ZF["schon"]:
            ZF["schon"].add("cmd:" + z)
            zeilen.append(z)
    if not zeilen:
        return ""
    ZF["nk"] += 1
    kid = f"kc-{ZF['nk']}"
    ZF["blatt"].append({"typ": "cmd", "id": kid, "zeilen": zeilen, "h": ZF["h"]})
    return kid

# Ansichten (W4a, 11.11.2026): Die Blöcke der obersten Ebene eines Artikels tragen eine Klasse, nach der die Ansicht „Kurz“
# filtert (dieselbe Seite, Umschalten per Klasse an <html>): kz bleibt, kw fällt weg. Je Abschnitt (## oder ###) bleiben
# Überschrift, „Kurz gesagt“, Kästen aus KZ_KAESTEN, nummerierte Formeln und die erste Abbildung; ohne „Kurz gesagt“ auch
# der erste richtige Absatz. Fließtext, Listen, Tabellen, Code, Beispiele, Hintergrund, Herleitungen und Aufgaben fallen weg.
KZ_KAESTEN = {"satz", "definition", "lemma", "merke", "formel", "kern", "warnung", "zweck"}
FB_KAESTEN = ("satz", "definition", "lemma", "merke", "formel")   # Formelblatt: diese Kästen, sofern sie Mathe enthalten
KZ_ERST_MIN = 80                                                  # „erster Absatz“: mindestens so viele Zeichen Klartext
_NUR_ETIKETT = re.compile(r"^\W*\*\*[^*]+\*\*\W*$")               # „**Die Idee in vier Schritten.**“: nur ein Etikett
_BLOCK_RE = re.compile(r"(?ms)^::::(kurzfassung|formelsammlung|lernkarten)[ \t]*\n(.*?)^::::[ \t]*$\n?")   # W4b: lernkarten

def ansicht_bloecke(body):
    """Geschriebene Fassungen (später aus eigenen Heftdateien): ::::kurzfassung … :::: und ::::formelsammlung … ::::
    stehen im Artikel-Markdown, erscheinen aber nur in ihrer Ansicht. Rückgabe (Text ohne die Blöcke, {Art: Markdown})."""
    bloecke = {}
    def weg(m):
        bloecke[m.group(1)] = m.group(2)
        return ""
    return _BLOCK_RE.sub(weg, body), bloecke

def _oben():
    """Block auf der obersten Ebene des gerade gesetzten Artikels (nicht in einem Kasten)?"""
    return bool(ZF.get("an")) and not _KASTEN

def _klasse(h, cls):
    """cls an das erste Tag von h hängen."""
    m = re.match(r"<([a-zA-Z][a-zA-Z0-9]*)([^>]*)>", h)
    if not m:
        return h
    attrs = m.group(2)
    attrs = attrs.replace(' class="', f' class="{cls} ', 1) if ' class="' in attrs else f' class="{cls}"' + attrs
    return f"<{m.group(1)}{attrs}>" + h[m.end():]

def _kz(h, bleibt):
    """Klasse der Ansicht „Kurz“ an einen Block der obersten Ebene (sonst unverändert)."""
    return _klasse(h, "kz" if bleibt else "kw") if _oben() else h

def _id_setzen(h, wert):
    m = re.match(r"<([a-zA-Z][a-zA-Z0-9]*)", h)
    return h if not m else h[:m.end()] + f' id="{wert}"' + h[m.end():]

def _ohne_tag(h, tag, start=""):
    """Alle Elemente <tag …>…</tag> (verschachtelt gezählt), deren Anfang mit start beginnt, aus h entfernen."""
    auf, zu = re.compile(rf"<{tag}\b[^>]*>"), f"</{tag}>"
    i, raus = 0, []
    while True:
        m = auf.search(h, i)
        while m and start and not m.group(0).startswith(start):
            m = auf.search(h, m.end())
        if not m:
            break
        tiefe, j = 1, m.end()
        while tiefe and j < len(h):
            a, z = auf.search(h, j), h.find(zu, j)
            if z < 0:
                j = len(h); break
            if a and a.start() < z:
                tiefe += 1; j = a.end()
            else:
                tiefe -= 1; j = z + len(zu)
        raus.append((m.start(), j))
        i = j
    for a, b in reversed(raus):
        h = h[:a] + h[b:]
    return h

def _blatt_html(h):
    """Inhalt eines Kastens fürs Formelblatt: ohne Herleitungen, Beweise, Abbildungen und Ankerlinks, ohne ids (der
    Kasten steht schon im Artikel)."""
    h = _ohne_tag(h, "details")
    h = _ohne_tag(h, "figure")
    h = _ohne_tag(h, "aside", '<aside class="callout cx-grafik"')
    h = re.sub(r'<a class="h-anker"[^>]*>#</a>', "", h)
    return re.sub(r'\s(?:id|aria-labelledby)="[^"]*"', "", h)

def _blatt_kasten(kind, titel_html, inner_md, inner_html):
    """Kasten (Satz, Definition, …) fürs Formelblatt merken, wenn er Mathe enthält; Rückgabe: id für den Kasten oder ""."""
    if not (_zf_haupt() and kind in FB_KAESTEN and not any(k in FB_KAESTEN for k, _ in _KASTEN)):
        return ""
    t = re.sub(r"```.*?```|`` .+? ``|`[^`\n]+?`", " ", "\n".join(inner_md), flags=re.S)   # $HOME in Code ist keine Mathe
    if not ZF.get("ref") and not re.search(r"\$\$.+?\$\$|\$[^$\n]+?\$", t, flags=re.S):
        return ""                                          # Formelblatt: nur Kästen mit Mathe; Übersicht: alle
    ZF["nk"] += 1
    kid = f"kk-{ZF['nk']}"
    ZF["blatt"].append({"typ": "box", "id": kid, "titel": titel_html, "html": _blatt_html(inner_html), "h": ZF["h"]})
    return kid

def _zf_haupt():
    return ZF.get("an") and not any(k in ZF_NEBEN for k, _ in _KASTEN)

def _zf_id(vor):
    ZF["n"] += 1
    return f"{vor}-{ZF['n']}"

def _innen(art, titel, zeilen):
    """Inhalt eines Kastens setzen; der Kasten steht dabei auf _KASTEN (was darin steht, zählt nicht als Haupttext)."""
    _KASTEN.append((art, titel))
    try:
        return md_to_html("\n".join(zeilen))[0]
    finally:
        _KASTEN.pop()

def _maskiert(t):
    return _MASKE_RE.sub(lambda m: "\x02" * len(m.group(0)), t)

def _saetze(t):
    """[(Anfang, Ende)] der Sätze eines Absatzes (Markdown). Formeln und Code sind maskiert, Abkürzungen („z. B.“,
    „bzw.“) und Ordnungszahlen („3.“) trennen nicht."""
    m, grenzen = _maskiert(t), [0]
    for x in re.finditer(r"[.!?](?=\s)|[。！？]", m):
        if x.group(0) == ".":
            vor = re.search(r"(\S+)$", m[:x.start()])
            wort = vor.group(1).strip("(„“\"'*_") if vor else ""
            if len(wort) <= 1 or wort.isdigit() or wort.lower().replace(".", "") in _ABKUERZUNG:
                continue
        grenzen.append(x.end())
    grenzen.append(len(t))
    return [(a, b) for a, b in zip(grenzen, grenzen[1:]) if t[a:b].strip()]

def _zf_bestimmung(txt, pos, begriff):
    """Satz der ersten Nennung eines Begriffs (Markdown), bei Rückbezug mit dem Satz davor; zu lang oder kaum mehr als
    der Begriff selbst: leer."""
    saetze = _saetze(txt)
    k = next((i for i, (a, b) in enumerate(saetze) if a <= pos < b), None)
    if k is None:
        return ""
    a, b = saetze[k]
    anfang = re.sub(r"^[\W_]+", "", klartext(txt[a:b]))
    vorher = txt[saetze[k - 1][0]:saetze[k - 1][1]].strip().lstrip("_*„“\"'(")[:1] if k > 0 else ""
    if vorher and _RUECKBEZUG.match(anfang) and not (vorher.isalpha() and vorher.islower()):   # Satz davor kein Bruchstück
        a = saetze[k - 1][0]
    def fertig(s):
        """Satzteile um abgesetzte Formeln kenntlich machen: „:“ am Ende -> Punkt; ohne Satzende „ …“; Anfang klein „… “."""
        s = re.sub(r"\s*：$", "。", re.sub(r"\s*:$", ".", s.strip()))
        rein = klartext(s)
        if not re.search(r"[.!?。！？…][)\]»“”\"']*$", rein):
            s += " …"
        erstes = s.lstrip("_*„“\"'(")[:1]                          # Formel oder Code am Anfang ($x$, `ls`): kein Bruchstück
        if erstes.isalpha() and erstes.islower():
            s = "… " + s
        return s
    satz = fertig(txt[a:b])
    rein = klartext(satz)
    if len(rein) > ZF_BESTIMMUNG_MAX and a != saetze[k][0]:       # mit dem Satz davor zu lang: nur der eigene Satz
        satz = fertig(txt[saetze[k][0]:b])
        rein = klartext(satz)
    if len(rein) > ZF_BESTIMMUNG_MAX or len(rein) - len(klartext(begriff)) < 15:
        return ""
    return satz

def _zf_begriffe(txt, bestimmung=True):
    """Neue Fachbegriffe (__…__) eines Absatzes, Listenpunkts oder einer Tabellenzelle sammeln. Die erste Nennung bekommt
    eine id: Rückgabe ist txt mit einer Marke (\\x01id\\x01) hinter dem öffnenden __, inline() macht daraus id="…"."""
    if "__" not in txt or not _zf_haupt():
        return txt
    neu = []
    for x in re.finditer(r"__([^_\n]+?)__", _maskiert(txt)):
        roh = txt[x.start(1):x.end(1)]
        key = fold(klartext(roh)).strip()
        if not key or key in ZF["schon"]:
            continue
        ZF["schon"].add(key)
        hid = _zf_id("kb")
        ZF["fb"].append({"id": hid, "md": roh, "satz": _zf_bestimmung(txt, x.start(), roh) if bestimmung else ""})
        neu.append((x.start() + 2, hid))
    for pos, hid in reversed(neu):
        txt = txt[:pos] + f"\x01{hid}\x01" + txt[pos:]
    return txt

def _zf_formel(tex, nr):
    """Abgesetzte Formel sammeln: in einem Satz-, Definitions-, Lemma- oder Merke-Kasten immer, sonst nur mit Nummer."""
    if not _zf_haupt():
        return ""
    kasten = next(((k, t) for k, t in reversed(_KASTEN) if k in ZF_FORMELKASTEN), None)
    if kasten is None and not nr:
        return ""
    schluessel = re.sub(r"\s+", "", tex)
    if schluessel in ZF["schon"]:
        return ""
    ZF["schon"].add(schluessel)
    hid = _zf_id("kf")
    ZF["fm"].append({"id": hid, "tex": tex, "nr": nr, "titel": kasten[1] if kasten else ZF["h"], "rang": 0 if kasten else 1})
    if kasten is None:                                    # Formelblatt (W4a): Formeln in Kästen kommen mit dem ganzen Kasten
        ZF["blatt"].append({"typ": "gl", "id": hid, "tex": tex, "nr": nr, "h": ZF["h"]})
    return hid

def _zf_ersatzformel(tex):
    """Unnummerierte abgesetzte Formel des Haupttexts (außerhalb von Kästen): Ersatz fürs Formelblatt eines Artikels ohne
    Kästen und nummerierte Formeln. Rückgabe: id oder ""."""
    if not _zf_haupt() or any(k in FB_KAESTEN for k, _ in _KASTEN):
        return ""
    schluessel = "ku:" + re.sub(r"\s+", "", tex)
    if schluessel in ZF["schon"]:
        return ""
    ZF["schon"].add(schluessel)
    ZF["nk"] += 1
    hid = f"ku-{ZF['nk']}"
    ZF["ku"].append({"typ": "gl", "id": hid, "tex": tex, "nr": "", "h": ZF["h"]})
    return hid

def _zf_kurz(txt):
    """„Kurz gesagt: …“ sammeln (alle Sprachen); Rückgabe: id für den Absatz oder ""."""
    m = KURZ_RE.match(txt)
    if not m or not _zf_haupt():
        return ""
    hid = _zf_id("kg")
    ZF["kg"].append({"id": hid, "md": txt[m.end():].strip(), "h": ZF["h"]})   # h: Abschnitt, Stichwort im Selbsttest
    return hid

def _ohne_links(md):
    return re.sub(r"(?<!!)\[([^\]]+)\]\([^)]+\)", r"\1", md)

def zusammenfassung_html(z, fuss="", art_path=None):
    """Kasten „Zusammenfassung“ (am Artikelende, immer offen) aus dem Sammler ZF; ohne Material: "".
    Dazu (W2) der Knopf „Selbsttest“ (ohne Skript verborgen, wissen.js deckt die Punkte zu) und fuss (Link auf die Lernkarten).
    Mit art_path (W4a, „Kapitel auf einer Seite“): nur die Gruppen, alle Punkte offen, Links auf den Artikel."""
    gruppen = []
    basis = f"/wissen/{art_path}" if art_path else ""
    def gruppe(wort, cls, punkte):
        if not punkte:
            return
        rest = len(punkte) - ZF_SICHTBAR
        if rest <= 1 or art_path:                              # „1 weitere zeigen“ lohnt nicht
            sichtbar, mehr = punkte, []
        else:
            sichtbar, mehr = punkte[:ZF_SICHTBAR], punkte[ZF_SICHTBAR:]
        h = f'<div class="zf-g zf-{cls}"><div class="zf-gh">{T(wort)}</div><ul class="zf-l">' + "".join(sichtbar) + "</ul>"
        if mehr:
            h += (f'<details class="zf-mehr"><summary>{html.escape(T("zf_mehr").format(n=len(mehr)))}</summary>'
                  f'<ul class="zf-l">' + "".join(mehr) + "</ul></details>")
        gruppen.append(h + "</div>")
    # Begriffe: Begriffe mit demselben Satz (zwei Fachbegriffe in einer Definition) stehen in einem Punkt
    punkte, i = [], 0
    while i < len(z["fb"]):
        b, gleich = z["fb"][i], [z["fb"][i]]
        while b["satz"] and i + len(gleich) < len(z["fb"]) and z["fb"][i + len(gleich)]["satz"] == b["satz"]:
            gleich.append(z["fb"][i + len(gleich)])
        namen = ", ".join(f'<a class="zf-b" href="{basis}#{x["id"]}">{inline(_ohne_links(x["md"]))}</a>' for x in gleich)
        punkte.append(f"<li>{namen}" + (f'<span class="zf-d"> – {inline(b["satz"])}</span>' if b["satz"] else "") + "</li>")
        i += len(gleich)
    gruppe("zf_begriffe", "begriffe", punkte)
    formeln = sorted(z["fm"], key=lambda f: f["rang"])             # Kästen zuerst, dann nummerierte Formeln; je in Textfolge
    punkte = []
    for f in formeln:
        titel = inline(_ohne_links(f["titel"])) if f["titel"] else ""
        nr = "".join(f" ({n})" for n in f["nr"].split("|")) if f["nr"] else ""
        kopf = (titel + html.escape(nr)).strip() or html.escape(T("zf_formeln"))
        teile = split_display("$$" + f["tex"] + "$$")              # mehrteilige Formel (\qquad): Teile dürfen umbrechen
        formel = ('<div class="mrow">' + "".join(f'<div class="mcell">{inline("$$" + t + "$$")}</div>' for t in teile) + "</div>"
                  if teile else inline("$$" + f["tex"] + "$$"))
        punkte.append(f'<li><a class="zf-fl" href="{basis}#{f["id"]}">{kopf}</a><div class="zf-f">{formel}</div></li>')
    gruppe("zf_formeln", "formeln", punkte)
    def _stichwort(k):                                             # Selbsttest: Abschnitt als Stichwort über dem zugedeckten Satz
        h = re.sub(r"^\s*(?:\d+(?:\.\d+)*\.?|Stufe\s+\d+\s*:)\s*", "", _ohne_links(k.get("h") or "")).strip()
        return (f'<span class="zf-cue" hidden>{T("zf_zu").format(h=inline(h))} </span>' if h else "")
    gruppe("zf_zusammenhaenge", "zusammenhaenge",
           [f'<li>{"" if art_path else _stichwort(k)}<a class="zf-a" href="{basis}#{k["id"]}">{inline(_ohne_links(k["md"]))}</a></li>' for k in z["kg"]])
    if not gruppen:
        return ""
    if art_path:
        return "".join(gruppen)
    test = (f'<button type="button" class="zf-test" aria-pressed="false" title="{html.escape(T("zf_test_t"))}" hidden>'
            f'{T("zf_test")}</button>')
    return (f'<aside class="zf" id="zusammenfassung" aria-labelledby="zf-titel"><div class="zf-kopf">'
            f'<h2 class="zf-t" id="zf-titel">{T("zf")}</h2>{test}</div>'
            + "".join(gruppen) + fuss + "</aside>")

ABB_N = [0]                                               # laufende Abbildungsnummer im Artikel (render_article setzt 0)
_ABB_GEMELDET = set()                                     # jede fehlende Szene/SVG nur einmal melden

_SVG_SIZE = {}                                            # svg_size je Pfad, einmal je Build (Dateien ändern sich nicht)


def svg_size(path):
    """(Breite, Höhe) aus dem <svg>-Kopf einer exportierten Abbildung, None wenn sie fehlt. Jede Datei wird je Build nur
    einmal gelesen (Messung 10.11.2026: das Öffnen kostet unter Windows etwa 5 ms, jede Abbildung kam bis zu dreimal)."""
    key = str(path)
    if key not in _SVG_SIZE:
        _SVG_SIZE[key] = _svg_size_lesen(path)
    return _SVG_SIZE[key]


def _svg_size_lesen(path):
    try:
        head = path.read_text(encoding="utf-8")[:800]
    except OSError:
        return None
    m = re.search(r'<svg\b[^>]*?\swidth="([\d.]+)"[^>]*?\sheight="([\d.]+)"', head)
    return (round(float(m.group(1))), round(float(m.group(2)))) if m else None

def caption_alt(md):
    """Bildunterschrift als Alternativtext: ohne Markdown und $; \\mathrm{A}, \\text{..} -> Inhalt, \\omega -> omega."""
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    t = re.sub(r"\\(?:mathrm|text|textrm|operatorname|mathit|mathbf)\s*\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\([A-Za-z]+)", r"\1", t)
    t = re.sub(r"[$*`{}_^]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def _abb_melden(key, text):
    if key not in _ABB_GEMELDET:
        _ABB_GEMELDET.add(key); print("  Abbildung:", text)

def abbildung_html(name, inner):
    """:::abbildung <szene> mit der Bildunterschrift als Inhalt -> nummerierte <figure> mit dem exportierten SVG
    (natürliche Größe, höchstens spaltenbreit), Alternativtext aus der Bildunterschrift und dem Link
    „In Editor öffnen“. Der Link nutzt nur den Namen (editor.html?scene=szenen/<szene>.json); der Editor lädt
    damit ausschließlich Dateien unter szenen/ und führt aus der Adresse nichts aus. Fehlt das SVG, steht wie
    bei :::grafik ein Platzhalter da (Nummer bleibt reserviert)."""
    teile = (name or "").split()                      # :::abbildung <szene> <nr>: Nummer läuft über ein ganzes Kapitel
    name = teile[0] if teile else ""
    if len(teile) > 1 and teile[1].isdigit():
        ABB_N[0] = int(teile[1]) - 1
    ABB_N[0] += 1
    k = ABB_N[0]
    cap_md = " ".join(l.strip() for l in inner if l.strip())
    cap = inline(cap_md) if cap_md else ""
    name = (name or "").strip()
    gueltig = bool(SZENE_NAME_RE.fullmatch(name))
    lang = LANG_NOW[0]
    size = svg_size(ABB_DIR / lang / (name + ".svg")) if gueltig else None
    if size is None:
        _abb_melden(("svg", name), (f"ungültiger Szenenname „{name}“ (erlaubt: a-z A-Z 0-9 _ - und /)" if not gueltig else
                    f"{ABB_URL}/{lang}/{name}.svg fehlt — python tools/export_szenen.py {name}") + " -> Platzhalter")
        return (f'<aside class="callout cx-grafik" data-szene="{html.escape(name)}" id="abb-{k}"><div class="callout-h">{T("abbildung")} {k} {T("abb_vorb")}</div>'
                + (f"<p>{cap}</p>" if cap else "") + f'<div class="gr-szene">Editor-Szene: {html.escape(name)}</div></aside>')
    edit = ""
    if (SZENEN / (name + ".json")).is_file():
        edit = (f'<a class="abb-edit" href="/editor.html?scene=szenen/{name}.json{"" if lang == "de" else "&amp;lang=" + lang}" target="_blank" rel="noopener" '
                f'title="{T("editor_title")}"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/>'
                f'<path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>{T("editor_offen")}</a>')
    else:
        _abb_melden(("json", name), f"web/szenen/{name}.json fehlt -> ohne Editor-Link")
    alt = caption_alt(cap_md) or f"{T('abbildung')} {k}"
    # Animierte Fassung (tools/export_szenen.py --animiert): Der Spieler in wissen.js setzt sie an die Stelle des Bilds.
    # Ohne sie (oder ohne Skript) bleibt das statische Bild, es zeigt das Endbild der Szene. Ist das statische Bild neuer
    # (später ohne --animiert exportiert), wäre die Animation veraltet: dann bleibt das Bild, mit Meldung.
    anim, a_svg = "", ABB_DIR / lang / (name + ".anim.svg")
    if a_svg.is_file():
        if a_svg.stat().st_mtime + 2 >= (ABB_DIR / lang / (name + ".svg")).stat().st_mtime:
            anim = f' data-anim="{ABB_URL}/{lang}/{name}.anim.svg"'
        else:
            _abb_melden(("anim", lang, name), f"{ABB_URL}/{lang}/{name}.anim.svg ist älter als das Bild — "
                        f"python tools/export_szenen.py --animiert {name} (bis dahin statisch)")
    return (f'<figure class="abb" id="abb-{k}"{anim}><img src="{ABB_URL}/{lang}/{name}.svg" width="{size[0]}" height="{size[1]}" '
            f'alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async"/>'
            + (f'<div class="abb-knopf">{edit}</div>' if edit else "")
            + f'<figcaption><span class="abb-n">{T("abbildung")} {k}</span>{(" " + cap) if cap else ""}</figcaption></figure>')

# Code-Blöcke (Hefte der Zusatzreihen): ```<sprache> <titel>. Farben per Pygments als CSS-Klassen (.hl …), damit Tag- und
# Nachtmodus dieselben Seiten nutzen; ohne Pygments bleibt der Code einfarbig. console = Sitzung im Terminal ($/# am
# Zeilenanfang = Eingabe), mit „>>> " wird daraus die Python-Konsole, mit „PS> " (und ohne $/#) die PowerShell-Sitzung.
CODE_NAME = {"python": "Python", "bash": "Bash", "c": "C", "cpp": "C++", "nasm": "x86-64", "gas": "x86-64 (AT&T)"}

def _konsolen_lexer(code):
    if re.search(r"(?m)^>>> ", code):
        return "pycon"
    if re.search(r"(?m)^PS> ", code) and not re.search(r"(?m)^[$#] ", code):
        return "ps1con"
    return "console"

def code_html(info, code):
    lang, _, titel = info.partition(" ")
    lang = lang.lower()
    lexer_name = {"console": _konsolen_lexer(code), "text": "", "": ""}.get(lang, lang)
    body = html.escape(code, quote=False)
    if lexer_name:
        try:
            from pygments import highlight
            from pygments.lexers import get_lexer_by_name
            from pygments.formatters import HtmlFormatter
            # Zeilenende anhängen: Die Sitzungs-Lexer (console, pycon) lassen eine letzte Zeile ohne \n sonst fallen
            body = highlight(code + "\n", get_lexer_by_name(lexer_name, stripnl=False, ensurenl=True), HtmlFormatter(nowrap=True))
            body = re.sub(r"\n(</span>)*$", lambda m: m.group(0)[1:], body)
        except Exception:                                 # Pygments fehlt oder kennt die Sprache nicht: einfarbig
            pass
    name = T("konsole") if lang == "console" else CODE_NAME.get(lang, "")
    kopf = ""
    if titel or name:
        kopf = ('<div class="code-kopf"><span class="code-t">' + html.escape(titel) + '</span>'
                + (f'<span class="code-l">{html.escape(name)}</span>' if name else "") + "</div>")
    return f'<div class="code-block code-{html.escape(lang or "text")}">{kopf}<pre class="hl"><code>{body}</code></pre></div>'

CALLOUTS = {"konzept": "Zur Idee", "kern": "kern", "merke": "merke", "grafik": "abbildung", "satz": "satz",
            "definition": "definition", "lemma": "lemma", "analogie": "analogie"}   # Schlüssel in UI

def md_to_html(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, toc, i, n = [], [], 0, len(lines)
    toc3 = []                                             # ###-Überschriften: Verzeichnis, wenn der Artikel keine ## hat
    section_open = False                                 # jeder ##-Abschnitt wird als Karte <section class="sect"> eingefasst
    formel_n = 0                                          # fortlaufende Nummer der :::formel-Boxen (zum Referenzieren, wie im Skript)
    para = []
    h_ids = set()
    sek = {"kurz": False, "erst": None, "abb": False}       # Abschnitt der Ansicht „Kurz“ (nur oberste Ebene)
    ziel = [None, 0]                                      # W4b: letzte Formel (Markdown) vor einer Herleitung, Blöcke seitdem
    def sek_ende():                                       # ohne „Kurz gesagt“ bleibt der erste richtige Absatz stehen
        if _oben() and not sek["kurz"] and sek["erst"] is not None:
            out[sek["erst"]] = out[sek["erst"]].replace(' class="kw', ' class="kz', 1)
        sek.update(kurz=False, erst=None, abb=False)
    def beispiel(arg, inner):                             # Beispiel: zugeklappte Box „Beispiel: Titel“, ohne Nummer (wie im Heft)
        wort, titel = T("beispiel"), arg                  # Kopf: „[Rechenbeispiel 2] Titel“, „[Gegenbeispiel]“, „Titel“ oder leer
        mw = re.match(r"\[([^\]]*)\]\s*(.*)$", arg)
        if mw:
            wort, titel = (mw.group(1).strip() or T("beispiel")), mw.group(2).strip()
        out.append(_kz(f'<details class="beispiel"><summary><span class="bsp-k">{inline(wort)}</span>' + inline(titel) + '</summary>'
                       '<div class="bsp-body">' + _innen("beispiel", titel, inner) + '</div></details>', False))
    def vorwissen(arg, inner):                            # „Was du dafür brauchst: Titel“: zugeklappte Box (User, 10.11.2026)
        kopf, titel = arg, ""                             # Kopf bis zum ersten Doppelpunkt (auch „：“ und „ :“), dann der Titel
        mk = re.match(r"(.+?)\s*[:：]\s*(.*)$", arg)
        if mk:
            kopf, titel = mk.group(1).strip(), mk.group(2).strip()
        out.append(_kz(f'<details class="vorwissen"><summary><span class="vo-k">{inline(kopf)}</span>' + inline(titel) + '</summary>'
                       '<div class="vo-body">' + _innen("vorwissen", titel, inner) + '</div></details>', False))
    def flush():
        if para:
            txt = " ".join(para).strip()
            if not txt.startswith("**Worum es geht"):   # Einstiegs-Absatz entfällt – Artikel startet mit dem Inhaltsverzeichnis
                # Gleichungsnummer \\tag{2.3} (mehrere: 2.3|2.4): eigene Spalte neben der Formel. KaTeX legte sie über
                # die Formel, sobald der Platz knapp wird; so bleibt sie frei und die Formel verkleinert sich (fitMath).
                mt = re.fullmatch(r"(\$\$.*?)\s*\\tag\{([^{}]*)\}\$\$", txt, flags=re.S)
                nummer, nr_roh = "", ""
                if mt:
                    txt = mt.group(1) + "$$"
                    nr_roh = mt.group(2)
                    nummer = "".join(f"<span>({n})</span>" for n in mt.group(2).split("|"))
                # Zusammenfassung: abgesetzte Formel, „Kurz gesagt“, neue Fachbegriffe; id = Sprungziel des Stichpunkts
                mf = re.fullmatch(r"\$\$(.+)\$\$", txt, flags=re.S)
                formel = bool(mf and "$$" not in mf.group(1))
                if formel:
                    zid = _zf_formel(mf.group(1).strip(), nr_roh) or (_zf_ersatzformel(mf.group(1).strip()) if not nr_roh else "")
                    ziel[:] = ["$$" + mf.group(1).strip() + "$$", 0]
                else:
                    ziel[1] += 1
                    zid = _zf_kurz(txt)
                    txt = _zf_begriffe(txt)
                ida = f' id="{zid}"' if zid else ""
                parts = split_display(txt)
                if parts:                                # mehrteilige Formelzeile: Teile dürfen umbrechen
                    inhalt = (f'<div class="mrow"{"" if nummer else ida}>' + "".join('<div class="mcell">' + inline("$$" + p + "$$") + "</div>"
                                                             for p in parts) + "</div>")
                else:
                    inhalt = inline(txt) if nummer else f"<p{ida}>" + inline(txt) + "</p>"
                if nummer:                               # Ansicht „Kurz“: nummerierte Formeln und „Kurz gesagt“ bleiben
                    out.append(_kz(f'<div class="gl-zeile"{ida}><div class="gl-f">{inhalt}</div><div class="gl-nr">{nummer}</div></div>', True))
                else:
                    kurz = zid.startswith("kg-")
                    out.append(_kz(inhalt, kurz))
                    if kurz:
                        sek["kurz"] = True
                    elif (_oben() and not formel and sek["erst"] is None and not _NUR_ETIKETT.match(txt)
                          and len(klartext(txt)) >= KZ_ERST_MIN):
                        sek["erst"] = len(out) - 1
            para.clear()
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:                                     # blank -> paragraph break
            flush(); i += 1; continue
        if s.startswith("```"):                       # fenced code: ```<sprache> <titel>
            flush(); info = s[3:].strip(); i += 1; code = []; ziel[1] += 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            h = code_html(info, "\n".join(code))
            kid = _blatt_befehle(info, "\n".join(code))  # Übersicht (Informatik): Befehle des Blocks
            out.append(_kz(_id_setzen(h, kid) if kid else h, False))
            continue
        mv = re.match(r":::::vorwissen(?:\s+(.+?))?\s*$", s)   # :::::vorwissen Titel … ::::: (fünf Doppelpunkte, darf ::::beispiel enthalten)
        if mv:
            flush(); i += 1; inner = []
            while i < n and lines[i].strip() != ":::::":
                inner.append(lines[i]); i += 1
            i += 1
            vorwissen((mv.group(1) or "").strip(), inner)
            continue
        mb = re.match(r"::::beispiel(?:\s+(.+?))?\s*$", s)   # ::::beispiel [Wort] Titel … :::: (vier Doppelpunkte, darf :::-Blöcke enthalten)
        if mb:
            flush(); i += 1; inner = []
            while i < n and lines[i].strip() != "::::":
                inner.append(lines[i]); i += 1
            i += 1
            beispiel((mb.group(1) or "").strip(), inner)
            continue
        if re.match(r":::quiz\s*$", s):               # quiz block: Q:/A: pairs -> collapsible items
            flush()
            if section_open:                          # Quiz steht als eigene Box außerhalb der Abschnitts-Karten
                out.append("</section>"); section_open = False
            i += 1; inner = []
            while i < n and lines[i].strip() != ":::":
                inner.append(lines[i]); i += 1
            i += 1
            items, cur, role = [], None, None
            for raw in inner:
                t = raw.strip()
                mq = re.match(r"(?:Q|F|Frage)\s*[:.]\s*(.*)$", t, re.I)
                ma = re.match(r"(?:A|Antwort)\s*[:.]\s*(.*)$", t, re.I)
                if mq:
                    cur = {"q": mq.group(1), "a": ""}; items.append(cur); role = "q"
                elif ma and cur is not None:
                    cur["a"] = ma.group(1); role = "a"
                elif t and cur is not None and role:
                    cur[role] += " " + t                 # continuation line of the current Q or A
            body = []
            for k, it in enumerate(items, 1):
                q_html = inline(it["q"].strip())
                a_html = _innen("quiz", "", [it["a"].strip()])
                body.append(f'<details class="quiz-item"><summary><span class="quiz-n">{k}.</span> {q_html}</summary>'
                            f'<div class="quiz-a">{a_html}</div></details>')
            out.append(_kz(f'<aside class="callout cx-quiz"><div class="callout-h">{T("quiz")}</div>'
                           + "".join(body) + "</aside>", False))
            continue
        m = re.match(r":::(\w+)(?:\s+(.+?))?\s*$", s)  # callout block  :::konzept / :::formel Definition ... :::
        if m:
            flush(); kind = m.group(1).lower(); label_arg = (m.group(2) or "").strip(); i += 1; inner = []
            tiefe = 1                                 # Blöcke dürfen verschachtelt sein (Lösung in Aufgabe, Abbildung in Vertiefung)
            while i < n:
                t = lines[i].strip()
                if t == ":::":
                    tiefe -= 1
                    if tiefe == 0:
                        break
                elif re.match(r":::\w", t):
                    tiefe += 1
                inner.append(lines[i]); i += 1
            i += 1
            if kind == "konzept":                         # „Zur Idee"-Einstiegskasten entfällt – Start ist das Inhaltsverzeichnis
                continue
            if kind in ZF_FORMELKASTEN and "$" in "".join(inner):   # W4b: Ziel einer folgenden Herleitung
                ziel[:] = ["\n".join(inner), 0]
            elif kind not in ("herleitung", "beweis"):
                ziel[1] += 1
            if kind == "beispiel":                        # Kurzform :::beispiel … ::: (ohne innere Blöcke)
                beispiel(label_arg, inner)
                continue
            if kind == "kern" and section_open:           # „Das Wichtigste" steht als eigene Box außerhalb der Abschnitts-Karten
                out.append("</section>"); section_open = False
            if kind == "formel":                          # wichtige Formel: Box mit Typ-Label (Definition/Satz/…) + Nummer
                formel_n += 1
                lbl = label_arg or "Formel"
                innen = _innen("formel", lbl, inner)
                h = (f'<div class="fbox"><div class="fbox-h"><span class="fbox-t">{html.escape(lbl)}</span>'
                     f'<span class="fbox-n">({formel_n})</span></div>' + innen + '</div>')
                kid = _blatt_kasten("formel", f"{html.escape(lbl)} ({formel_n})", inner, innen)
                out.append(_kz(_id_setzen(h, kid) if kid else h, True))
                continue
            if kind in ("herleitung", "beweis"):          # Herleitung oder Beweis als ausklappbare Box an der Formel
                anker = ""
                if kind == "herleitung" and ZF.get("an"):  # W4b: Lernkarte „Herleitung“ (Ziel = Formel kurz davor, Schritte)
                    anker = f"hl-{len(ZF['hl']) + 1}"
                    ZF["hl"].append({"titel": label_arg, "zeilen": list(inner), "id": anker,
                                     "ziel": ziel[0] if ziel[0] and ziel[1] <= 2 else None})
                out.append(_kz(f'<details class="herleitung"><summary>{T(kind)}' + (": " + inline(label_arg) if label_arg else "") + '</summary>'
                               '<div class="hl-body">' + (f'<span class="anker" id="{anker}"></span>' if anker else "")
                               + _innen(kind, label_arg, inner) + '</div></details>', False))
                continue
            if kind == "zweck":                           # Einstieg einer Stufe: wozu sie da ist
                out.append(_kz(f'<div class="zweck"><span class="zw-k">{T("zweck")}</span> ' + _innen("zweck", "", inner) + '</div>', True))
                continue
            if kind == "aufgabe":                         # Aufgabe mit Nummer und Sternen, Lösung als Ausklappblock darin
                h = ('<div class="aufg"><div class="aufg-h">' + inline(label_arg) + '</div>'
                     '<div class="aufg-b">' + _innen("aufgabe", label_arg, inner) + '</div></div>')
                if ZF.get("an"):                          # W4b: Bereich „Aufgaben“ und Mischtest
                    ma = re.search(r'\sid="(aufg-[^"]+)"', h)
                    ZF["ag"].append({"titel": label_arg, "html": h, "id": ma.group(1) if ma else ""})
                out.append(_kz(h, False))
                continue
            if kind == "loesung":
                out.append(_kz(f'<details class="loesung"><summary>{T("loesung")}</summary>'
                               '<div class="lo-body">' + _innen("loesung", "", inner) + '</div></details>', False))
                continue
            if kind == "zusatz":                          # Vertiefung: darf übersprungen werden
                out.append(_kz(f'<aside class="callout cx-zusatz"><div class="callout-h">{T("zusatz")}'
                               + (": " + inline(label_arg) if label_arg else "") + '</div>' + _innen("zusatz", label_arg, inner) + "</aside>", False))
                continue
            if kind == "warnung":                         # Achtung (Recht, Datenverlust, Sicherheit): immer offen
                out.append(_kz(f'<aside class="callout cx-warnung"><div class="callout-h">{T("warnung")}'
                               + (": " + inline(label_arg) if label_arg else "") + '</div>' + _innen("warnung", label_arg, inner) + "</aside>", True))
                continue
            if kind == "ltspice":                         # LTspice-Hinweis (nachbauen und messen): standardmaessig geschlossen
                out.append(_kz('<details class="ltspice"><summary><span class="lt-k">LTspice</span>'
                               + inline(label_arg) + '</summary>'
                               '<div class="lt-body">' + _innen("ltspice", label_arg, inner) + '</div></details>', False))
                continue
            if kind == "hintergrund":                     # Hintergrundwissen: Titel sichtbar, Inhalt zugeklappt (Haupttext bleibt skriptgeordnet)
                out.append(_kz(f'<details class="hintergrund"><summary><span class="hg-k">{T("hintergrund")}</span>' + inline(label_arg) + '</summary>'
                               '<div class="hg-body">' + _innen("hintergrund", label_arg, inner) + '</div></details>', False))
                continue
            if kind == "frage":                           # Frage-Kasten (wie im Lernskript): Frage sichtbar, Antwort ausklappbar
                if label_arg:
                    frage, rest = label_arg, inner
                else:
                    k0 = next((j for j, l in enumerate(inner) if l.strip()), len(inner))
                    frage, rest = (inner[k0].strip() if k0 < len(inner) else ""), inner[k0 + 1:]
                out.append(_kz(f'<details class="frage"><summary><span class="fr-k">{T("frage")}</span>' + inline(frage) + '</summary>'
                               '<div class="fr-body">' + _innen("frage", frage, rest) + '</div></details>', False))
                continue
            if kind == "abbildung":                       # Editor-Abbildung: exportiertes SVG, nummerierte Bildunterschrift, Link in den Editor
                h = abbildung_html(label_arg, inner)      # Ansicht „Kurz“: die erste Abbildung eines Abschnitts bleibt
                erste = _oben() and not sek["abb"] and h.startswith("<figure")
                out.append(_kz(h, erste))
                if erste:
                    sek["abb"] = True
                continue
            if kind == "grafik":                          # Platzhalter einer Editor-Abbildung: Beschreibung als Text, Szene-Zeile klein darunter
                k0 = next((j for j, l in enumerate(inner) if l.strip()), len(inner))
                szene = ""
                if k0 < len(inner) and inner[k0].strip().startswith("Szene:"):
                    szene, inner = inner[k0].strip()[len("Szene:"):].strip(), inner[k0 + 1:]
                out.append(_kz('<aside class="callout cx-grafik"' + (f' data-szene="{html.escape(szene)}"' if szene else "")
                               + '><div class="callout-h">Abbildung in Vorbereitung</div>' + _innen("grafik", "", inner)
                               + (f'<div class="gr-szene">Editor-Szene: {html.escape(szene)}</div>' if szene else "") + "</aside>", False))
                continue
            key = CALLOUTS.get(kind, kind.title())
            label = inline(label_arg) if label_arg else html.escape(UI["de"].get(key) and T(key) or key)
            innen = _innen(kind, label_arg or (T(key) if key in UI["de"] else key), inner)
            h = f'<aside class="callout cx-{kind}"><div class="callout-h">{label}</div>' + innen + "</aside>"
            kid = _blatt_kasten(kind, label, inner, innen)  # Satz, Definition, … mit Mathe: Eintrag im Formelblatt
            out.append(_kz(_id_setzen(h, kid) if kid else h, kind in KZ_KAESTEN))
            continue
        if re.match(r"(---|\*\*\*|___)\s*$", s):      # horizontal rule
            flush(); out.append(_kz("<hr/>", False)); i += 1; continue
        hm = re.match(r"(#{1,4})\s+(.*)$", s)         # heading
        if hm:
            flush(); lvl = len(hm.group(1)); txt = hm.group(2).strip(); ziel[0] = None
            if lvl in (2, 3):                              # neuer Abschnitt der Ansicht „Kurz“
                sek_ende()
            hid = slugify(txt)
            if hid == "x" or hid in h_ids:                 # chinesische Überschrift oder gleicher Titel: Nummer anhängen
                hid = f"{hid}-{len(h_ids)}"
            h_ids.add(hid)
            if lvl == 2:                                   # neuer ##-Abschnitt -> alte Karte schließen, neue öffnen
                toc.append((hid, txt, 2))
                if section_open:
                    out.append("</section>")
                out.append('<section class="sect">')
                section_open = True
            elif lvl == 3:
                toc3.append((hid, txt, 3))
            if ZF.get("an") and not _KASTEN:
                ZF["h"] = txt                              # Abschnitt einer nummerierten Formel (Zusammenfassung)
            # Ankerlink: „#“ erscheint erst bei Hover oder Fokus; Klick setzt die Adresse und kopiert den Link (wissen.js)
            anker = f'<a class="h-anker" href="#{hid}" aria-label="{html.escape(T("anker"))}">#</a>' if lvl >= 2 else ""
            out.append(f'<h{lvl} id="{hid}">{inline(txt)}{anker}</h{lvl}>')
            i += 1; continue
        if s.startswith(">"):                         # blockquote
            flush(); quote = []; ziel[1] += 1
            while i < n and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append(_kz("<blockquote>" + _innen("zitat", "", quote) + "</blockquote>", False))
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i + 1].strip()):
            flush(); ziel[1] += 1                     # GitHub-Tabelle: Kopfzeile + |---|---|-Trenner + Zeilen
            cells = lambda row: [c.strip().replace("\\|", "|")          # \| (GFM) ist ein | im Zelleninhalt, z. B. in `ls | wc`
                                 for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]
            header = cells(s); i += 2; body = []
            while i < n and lines[i].strip().startswith("|"):
                body.append(cells(lines[i].strip())); i += 1
            thead = "<tr>" + "".join(f"<th>{inline(_zf_begriffe(c, False))}</th>" for c in header) + "</tr>"
            tbody = "".join("<tr>" + "".join(f"<td>{inline(_zf_begriffe(c, False))}</td>" for c in r) + "</tr>" for r in body)
            out.append(_kz(f'<div class="table-wrap"><table class="md-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>', False))
            continue
        if re.match(r"[-*]\s+", s) or re.match(r"\d+\.\s+", s):   # list (ul/ol)
            flush(); ziel[1] += 1; ordered = bool(re.match(r"\d+\.\s+", s)); items = []
            while i < n:
                raw = lines[i]; st = raw.strip()
                if not st:
                    break                                               # Leerzeile beendet die Liste
                if re.match(r"[-*]\s+", st) or re.match(r"\d+\.\s+", st):
                    items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", st)); i += 1   # neuer Punkt
                elif items and raw[:1] in (" ", "\t"):
                    items[-1] += " " + st; i += 1                        # eingerückte Fortsetzungszeile -> an aktuellen Punkt anhängen
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append(_kz(f"<{tag}>" + "".join(f"<li>{inline(_zf_begriffe(it))}</li>" for it in items) + f"</{tag}>", False))
            continue
        if s.startswith("<"):                         # raw HTML / SVG / editor embed -> passthrough
            flush(); out.append(ln); i += 1; continue
        para.append(s); i += 1                         # ordinary paragraph line
    flush()
    sek_ende()
    if section_open:                                   # letzte Abschnitts-Karte schließen
        out.append("</section>")
    # Verzeichnis: die ##-Abschnitte; ohne sie die ###-Unterabschnitte, sobald es mindestens zwei sind
    return "\n".join(out), (toc or (toc3 if len(toc3) >= 2 else []))

# ---------------------------------------------------------- plain text (search) ----
def to_plain(md):
    txt = re.sub(r"```.*?```", " ", md, flags=re.S)
    txt = re.sub(r"\$\$?.+?\$\$?", " ", txt, flags=re.S)        # drop math
    txt = re.sub(r"</?[a-z][^>]*>", " ", txt)                  # Listen und Anker aus den Heften
    txt = re.sub(r"^:::::vorwissen\s*", "", txt, flags=re.M)   # Titel des Vorwissen-Kastens bleibt suchbar (wie früher die Überschrift)
    txt = re.sub(r"^:::.*$", " ", txt, flags=re.M)
    txt = re.sub(r"[#>*`_:\-\[\]()!]", " ", txt)
    txt = re.sub(r"https?://\S+", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()

# ---------------------------------------------------------- build the tree ----
# Hierarchie beliebig tief, gesteuert über das Frontmatter-Feld `pfad:` (Ebenen durch " / " getrennt),
# z. B.:  pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
# Der Artikel (das „Thema") hängt am letzten Knoten dieser Kette. Reihenfolge je Ebene über das kleinste
# `order` der darunterliegenden Artikel (globale Sequenznummer, z. B. 50200 = Kap 5, Abschnitt 2).
def _new_node(name):
    return {"name": name, "slug": slugify(name), "order": 10**9, "children": {}, "articles": []}

def collect():
    """{Sprache: Baum}. Eine Übersetzung NN-slug.en.md übernimmt die Adresse des deutschen Artikels neben ihr."""
    roots, ausf = {l: {} for l in LANGS}, []
    de_pfad, de_ordner = {}, {}                        # (Ordner, Stamm) bzw. Quellordner -> Adresse auf der Website (Deutsch)
    hinweise = []                                      # _<name>.md: kurzer Text zu einem Knoten (hinweis: <Pfad>), kein Artikel
    def deutsch_zuerst(p):
        return (bool(LANG_FILE.search(p.stem)), p)
    for md_file in sorted(SRC.rglob("*.md"), key=deutsch_zuerst):
        meta, body = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        ml = LANG_FILE.search(md_file.stem)
        lang = ml.group(1) if ml else "de"
        stem = md_file.stem[:ml.start()] if ml else md_file.stem
        if md_file.name.startswith("_"):
            if (meta.get("hinweis") or "").strip() and body.strip():
                hinweise.append((lang, meta["hinweis"].strip(), body.strip()))
            continue
        pfad = (meta.get("pfad") or "").strip()
        if not pfad:
            print("  übersprungen (kein pfad:):", md_file.relative_to(SRC)); continue
        parts = [p.strip() for p in pfad.split("/") if p.strip()]
        adr = [p.strip() for p in (meta.get("adresse") or "").split("/") if p.strip()]   # feste Slugs der Knoten
        if adr and len(adr) != len(parts):
            print("  adresse: passt nicht zu pfad: (Slugs aus pfad):", md_file.relative_to(SRC)); adr = []
        title = meta.get("title") or md_file.stem
        ov = (meta.get("order") or "").strip()
        order = int(ov) if ov.isdigit() else (int(re.match(r"(\d+)", stem).group(1)) if re.match(r"\d+", stem) else 999999)
        container, chain = roots[lang], []
        for i, part in enumerate(parts):
            slug = adr[i] if adr else slugify(part)
            nd = container.setdefault(slug if lang == "de" else part, _new_node(part))
            if lang == "de":
                nd["slug"] = slug
            chain.append(nd); container = nd["children"]
        if (meta.get("knoten") or "").strip():         # Aufschrift des letzten Knotens („Grundlagen 1: Vektoren und Matrizen“),
            chain[-1]["name"] = meta["knoten"].strip()  # die Adresse kommt weiter aus pfad: (bleibt bei neuer Nummerierung)
        a_slug = re.sub(r"^\d+-", "", stem) or slugify(title)
        key = (str(md_file.parent), stem)
        if lang == "de":
            path = "/".join(nd["slug"] for nd in chain) + "/" + a_slug + ".html"
            de_pfad[key] = path
            de_ordner.setdefault(str(md_file.parent), path.rsplit("/", 1)[0])
        else:                                          # ohne deutsches Gegenstück (veraltete Übersetzung): in den Ordner der
            ordner = de_ordner.get(str(md_file.parent), "/".join(adr) if adr else "/".join(nd["slug"] for nd in chain))   # übrigen Artikel, sonst
            path = lang + "/" + de_pfad.get(key, ordner + "/" + a_slug + ".html")               # laufen ihre Links ins Leere
        autor = (meta.get("autor") or "").strip().lower()
        if re.search(r"-mensch(-ausfuehrlich)?$", a_slug):   # Dateiname-Suffix genügt
            autor = autor or "mensch"
        title = title.replace("`", "")                 # Code in Titeln (`float`) als normaler Text: Kopfleiste, Seitentitel, Suche
        body, bloecke = ansicht_bloecke(body)          # geschriebene Kurzfassung/Formelsammlung: nur in ihrer Ansicht (W4a)
        art = {"title": title, "kurz": meta.get("kurz", "").replace("`", ""), "slug": a_slug, "order": order, "path": path,
               "summary": meta.get("summary", ""), "tags": meta.get("tags", ""), "body": body, "bloecke": bloecke,
               "reihe": md_file.relative_to(SRC).parts[0],   # Ordner unter content/ (Informatik-Reihen: „Übersicht“)
               "crumbs": [(nd["name"], nd["slug"]) for nd in chain], "lang": lang, "key": key,
               "fassung": (meta.get("fassung") or "").strip().lower(),
               # Nachschlagebereich (ML-Grundlagen): unter dem Artikel steht „Verwendet in“ mit den Artikeln, die ihn verlinken
               "nachschlagen": (meta.get("nachschlagen") or "").strip().lower() in ("ja", "yes", "true", "1"),
               "autor": "mensch" if autor in ("mensch", "hand", "human") else "ki"}
        if art["fassung"] == "ausfuehrlich":           # zweite Fassung eines Themas: kein eigener Eintrag im Baum
            ausf.append((art, chain[-1], re.sub(r"-ausfuehrlich$", "", a_slug)))
            continue
        chain[-1]["articles"].append(art)
        for nd in chain:
            nd["order"] = min(nd["order"], order)
    for art, node, base in ausf:                       # ausführliche Fassung an die kompakte desselben Themas hängen
        partner = next((a for a in node["articles"] if a["slug"] == base), None)
        if partner:
            partner["alt"], art["alt"] = art, partner
            partner["fassung"] = partner["fassung"] or "kompakt"
        else:                                          # (noch) ohne kompakte Fassung: normal im Baum führen
            node["articles"].append(art)
    for lang, pfad, text in hinweise:                  # Hinweis an seinen Knoten hängen (fehlt der Knoten in der Sprache: entfällt)
        container, nd = roots[lang], None
        for part in [p.strip() for p in pfad.split("/") if p.strip()]:
            nd = container.get(slugify(part) if lang == "de" else part) or next(
                (n for n in container.values() if n["name"] == part), None)   # Knoten mit adresse: (Slug ≠ Name)
            if nd is None:
                break
            container = nd["children"]
        if nd is not None:
            nd["hinweis"] = text
    def pair_humans(nd):
        """Von Hand geschriebene Fassung (slug-mensch) an die KI-Fassung desselben Themas hängen;
        ohne KI-Gegenstück bleibt sie als eigener Eintrag im Baum."""
        for art in list(nd["articles"]):
            if art["autor"] != "mensch" or not art["slug"].endswith("-mensch"):
                continue
            partner = next((a for a in nd["articles"] if a["slug"] == art["slug"][:-7] and a["autor"] == "ki"), None)
            if partner:
                partner["human"], art["human_of"] = art, partner
                nd["articles"].remove(art)
    def to_list(container):
        nodes = sorted(container.values(), key=lambda x: (x["order"], x["name"]))
        for nd in nodes:
            pair_humans(nd)
            nd["articles"].sort(key=lambda a: (a["order"], a["title"]))
            nd["children"] = to_list(nd["children"])
        return nodes
    return {l: to_list(roots[l]) for l in LANGS if roots[l] or l == "de"}

def flatten(nodes):
    """Articles in reading order (a node's own Themen first, then its sub-levels)."""
    out = []
    for nd in nodes:
        out += nd["articles"]
        out += flatten(nd["children"])
    return out

# ------------------------------------------------------------------ render ----
def _has_active(nd, active_path):
    return any(a["path"] == active_path for a in nd["articles"]) or any(_has_active(c, active_path) for c in nd["children"])

def _node_label(nd, depth):
    return html.escape(nd["name"])

_KNOTEN_VON = {}                                       # id(Baum) -> {Artikeladresse: Knoten, an dem der Artikel hängt}

def knoten_von(tree, path):
    """Knoten (Kapitel), an dem der Artikel mit dieser Adresse im Baum hängt, sonst None."""
    tab = _KNOTEN_VON.get(id(tree))
    if tab is None:
        tab = _KNOTEN_VON[id(tree)] = {}
        def walk(nodes):
            for nd in nodes:
                for a in nd["articles"]:
                    tab[a["path"]] = nd
                walk(nd["children"])
        walk(tree)
    return tab.get(path)

def _uebersicht_anker(nd, tiefe=1):
    """Anker eines Knotens in der Wissensübersicht: Modul m-<Ordner>, sonst Bereich (tiefe 0) b-<Ordner>, Gruppe g-<Ordner>.
    Die Ordner kommen aus den Artikeladressen, die in allen Sprachen die deutschen sind: Die Anker sind überall gleich."""
    mp = _modul_von(nd)
    if mp:
        return "m-" + mp.rsplit("/", 1)[-1]
    a = next(iter(flatten([nd])), None)
    if a is None:
        return ("b-" if tiefe == 0 else "g-") + nd["slug"]
    teile = (a["path"].split("/", 1)[1] if a["lang"] != "de" else a["path"]).split("/")
    return ("b-" if tiefe == 0 else "g-") + teile[min(tiefe, len(teile) - 2)]

def sidebar_html(tree, active_path=None, art=None):
    # Seit 11.11.2026 (Wunsch des Users): immer nur die oberste Ebene (Studiengang/Bereich, z. B. Elektrotechnik) offen,
    # darunter sieht man nur die nächste Ebene (z. B. 1. Semester) zugeklappt; auch der Ast des geöffneten Artikels
    # bleibt zu (der Artikel ist weiter als aktiv markiert, falls man ihn aufklappt).
    # W3a (11.11.2026): Nur diese oberen Ebenen stehen im HTML (vorher ~140 KB je deutscher Seite). Den Inhalt einer Gruppe
    # setzt wissen.js beim ersten Aufklappen aus data/tree*.json ein (data-baum = Platz im Baum: Bereich.Gruppe). Ohne
    # Skript führt der Link in der Gruppe zur Übersicht. Für den Lesefortschritt trägt die Leiste den aktiven Artikel, den
    # Namen seines Kapitels und die Adressen aller Themen des Kapitels (data-aktiv, data-kapitel, data-kap).
    rows = []
    for i, nd in enumerate(tree):
        rows.append(f'<details class="lvl lvl0" open><summary>{_node_label(nd, 0)}</summary>')
        mp = _modul_von(nd)                            # Modul: Begriffe und Lernkarten als leise Zeile über den Kapiteln
        if mp:
            rows.append(lernen_links(mp, "side-lernen"))
        if nd["articles"]:                             # Themen direkt am Bereich (gibt es derzeit nicht)
            rows.append("<ul>")
            for a in nd["articles"]:
                cls = ' class="active"' if a["path"] == active_path else ""
                rows.append(f'<li><a{cls} href="/wissen/{a["path"]}"{alt_attr(a)}>{html.escape(a["kurz"] or a["title"])}</a></li>')
            rows.append("</ul>")
        for j, c in enumerate(nd["children"]):
            rows.append(f'<details class="lvl lvl1" data-baum="{i}.{j}"><summary>{_node_label(c, 1)}</summary>'
                        f'<a class="side-mehr" href="{home()}#{_uebersicht_anker(c)}">{T("baum_mehr")}</a></details>')
        rows.append("</details>")
    suffix = "" if LANG_NOW[0] == "de" else "." + LANG_NOW[0]
    attr = f' data-baum-url="/wissen/data/tree{suffix}.json"'
    kap = knoten_von(tree, active_path) if active_path else None
    if kap is not None:
        attr += (f' data-aktiv="/wissen/{html.escape(active_path)}" data-kapitel="{html.escape(kap["name"])}"'
                 f' data-kap="{html.escape(" ".join(a["path"] for a in kap["articles"]))}"')
    return (f'<nav class="side" aria-label="Wissensbaum"{attr}>'
            + f'<a class="side-home" href="{home()}">{T("alle_module")}</a>' + "".join(rows) + "</nav>")

def page_shell(title, desc, body, depth, alternates=None, js=()):
    up = "../" * depth
    mehr_js = "".join(f'\n<script src="{s}"></script>' for s in js)   # W4b: bereiche.js auf den Seiten der Bereiche
    links = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in (alternates or {}).items())
    return f"""<!doctype html>
<html lang="{LANG_NOW[0]}"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(klartext(title))} — EtUndSo</title>
<link rel="icon" href="/favicon.ico" sizes="32x32"/><link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<meta name="description" content="{html.escape(klartext(desc))}"/>{links}
<script>try{{var t=localStorage.getItem("animate-theme");if(t==="dark"||(!t&&matchMedia("(prefers-color-scheme: dark)").matches))document.documentElement.setAttribute("data-theme","dark");}}catch(e){{}}
try{{var a=new URLSearchParams(location.search).get("ansicht");if(a==="uebersicht")a="formeln";if(!/^(voll|kurz|formeln)$/.test(a||""))a=localStorage.getItem("etundso-ansicht");if(a==="kurz"||a==="formeln")document.documentElement.setAttribute("data-ansicht",a);}}catch(e){{}}</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css"/>
<link rel="stylesheet" href="/wissen/assets/wissen.css"/>
</head><body data-root="{home()}">
{body}
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>
<script src="/wissen/assets/wissen.js"></script>{mehr_js}
</body></html>"""

def alt_attr(a):
    """Daten-Attribut an Links auf die kompakte Fassung eines Themas: wer „Ausführlich“ gewählt hat, wird per JS
    dorthin gelenkt (data-alt)."""
    if not a:
        return ""
    return f' data-alt="/wissen/{a["alt"]["path"]}"' if a.get("alt") and a.get("fassung") == "kompakt" else ""

def tree_art(art):
    """Der Eintrag im Baum, zu dem eine Seite gehört: die kompakte KI-Fassung des Themas."""
    a = art["alt"] if art.get("fassung") == "ausfuehrlich" and art.get("alt") else art
    return a.get("human_of") or a

def sprachen(art):
    """{Sprache: Adresse} derselben Seite; art = None: die Übersichten."""
    if art is None:
        return {l: ("/wissen/" if l == "de" else f"/wissen/{l}/") for l in TREES}
    if "ziele" in art:                                 # Seiten eines Moduls (Begriffe, Lernkarten): von lernen_seiten gesetzt
        return art["ziele"]
    base = art.get("human_of") or art
    return {l: "/wissen/" + a["path"] for l, a in ART_LANG.get(base["key"], {}).items()}

_L_PFEIL = ('<svg class="l-pfeil" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>')
_L_HAKEN = ('<svg class="l-haken" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="5 12.5 10 17.5 19 7"/></svg>')

def lang_switch(art=None, where="top"):
    """Sprachmenü: ein Knopf mit der aktuellen Sprache („DE ▾“), darunter die Liste aller Sprachen in eigener
    Schreibweise. Sprachen ohne Übersetzung dieser Seite sind ausgegraut und kein Link. where: "top" = Kopfleiste;
    auf schmalen Bildschirmen passt der Knopf dort nicht mehr und steht unter dem Titel ("art"). wissen.js öffnet und
    schließt das Menü (Esc, Klick daneben, Pfeiltasten, aria-expanded)."""
    ziele, jetzt = sprachen(art), LANG_NOW[0]
    mid = f"lmenu-{where}"
    rows = ""
    for l in LANG_MENU:
        name = html.escape(LANG_VOLL[l])
        if l == jetzt:
            rows += (f'<li><a class="l-item on" href="{ziele.get(l, home())}" hreflang="{l}" lang="{l}" aria-current="true">'
                     f'<span class="l-name">{name}</span>{_L_HAKEN}</a></li>')
        elif l in ziele:
            rows += f'<li><a class="l-item" href="{ziele[l]}" hreflang="{l}" lang="{l}"><span class="l-name">{name}</span></a></li>'
        else:
            rows += (f'<li><span class="l-item off" lang="{l}" aria-disabled="true" title="{html.escape(T("nicht_uebersetzt"))}">'
                     f'<span class="l-name">{name}</span></span></li>')
    knopf = (f'<button type="button" class="l-toggle" aria-expanded="false" aria-controls="{mid}" '
             f'aria-label="{html.escape(T("sprache"))}: {html.escape(LANG_VOLL[jetzt])}" title="{html.escape(T("sprache"))}">'
             f'<span class="l-cur">{LANG_NAME[jetzt]}</span>{_L_PFEIL}</button>')
    return (f'<nav class="langs langs-{where}" aria-label="{html.escape(T("sprache"))}" data-langmenu>{knopf}'
            f'<ul class="l-menu" id="{mid}" hidden>{rows}</ul></nav>')

def lesezeit(body):
    """Lesezeit des Hauptpfads in Minuten (170 Wörter/min; ohne Vorwissen, Herleitungen, Beispiele, Quiz, Formeln, Abbildungen)."""
    t = re.sub(r"^:::::\s*vorwissen.*?^:::::\s*$", " ", body, flags=re.S | re.M)
    t = re.sub(r"^::::\s*beispiel.*?^::::\s*$", " ", t, flags=re.S | re.M)
    t = re.sub(r"^:::\s*(?:herleitung|beweis|quiz|frage|ltspice)\b.*?^:::\s*$", " ", t, flags=re.S | re.M)   # eingeklappte Kästen
    t = re.sub(r"^:::\s*(?:grafik|abbildung)\b.*?^:::\s*$", " ", t, flags=re.S | re.M)   # Abbildungen zählen nicht (wie früher die Bildunterschriften)
    t = re.sub(r"\$\$.+?\$\$", " ", t, flags=re.S)
    t = re.sub(r"^\s*<.*$", " ", t, flags=re.M)
    return max(1, round(len([w for w in t.split() if re.search(r"[A-Za-zÄÖÜäöüß0-9]", w)]) / 170))

ANSICHTEN = (("voll", "ans_voll"), ("kurz", "ans_kurz"), ("formeln", "ans_formeln"))

def ansicht_schalter(ref=False):
    """Umschalter Ausführlich | Kurz | Formeln (W4a) an der Stelle der früheren Pfeile: breit ein Segmentschalter, schmal eine
    Auswahl; ohne Skript verborgen (dann gilt „Ausführlich“). wissen.js setzt data-ansicht an <html> und merkt die Wahl.
    In den Informatik-Reihen heißt die dritte Ansicht „Übersicht“ (intern dieselbe: formeln)."""
    knoepfe = "".join(f'<button type="button" class="ans-b" data-ansicht="{k}" aria-pressed="{"true" if k == "voll" else "false"}">'
                      f'{TR(w, ref)}</button>' for k, w in ANSICHTEN)
    optionen = "".join(f'<option value="{k}">{TR(w, ref)}</option>' for k, w in ANSICHTEN)
    return (f'<div class="ansicht" role="group" aria-label="{html.escape(T("ans"))}" hidden>{knoepfe}</div>'
            f'<select class="ans-sel" aria-label="{html.escape(T("ans"))}" hidden>{optionen}</select>')

BEREICHE = (("wissen", "b_wissen"), ("lernen", "b_lernen"), ("aufgaben", "b_aufgaben"), ("editor", "b_editor"))
_B_ICON = ('<svg class="b-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
           'stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" '
           'width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" '
           'height="7" rx="1.5"/></svg>')

def bereich_url(b, lang=None):
    """Einstieg eines Bereichs in der Sprache (Deutsch ohne Kürzel): /wissen/, /lernen/en/, /aufgaben/zh/; der Editor ist einer."""
    l = lang or LANG_NOW[0]
    if b == "editor":
        return "/editor.html"
    return f"/{b}/" if l == "de" else f"/{b}/{l}/"

def bereiche_nav(aktiv=None):
    """Die vier Bereiche (W4b): breit als Linkreihe (aktiver Bereich orange unterstrichen), schmal als Menü hinter einem Knopf
    mit dem Namen des Bereichs (sehr schmal nur ein Symbol). Das Menü bedient wissen.js wie das Sprachmenü (data-langmenu).
    Auf sehr schmalen Artikelseiten steht dort auch „Hell/Dunkel“ (der Knopf in der Leiste hat keinen Platz mehr)."""
    reihe, menue = "", ""
    for b, w in BEREICHE:
        on = b == aktiv
        cur = ' aria-current="true"' if on else ""
        reihe += f'<li><a class="b-l{" on" if on else ""}" href="{bereich_url(b)}"{cur}>{html.escape(T(w))}</a></li>'
        menue += (f'<li><a class="l-item{" on" if on else ""}" href="{bereich_url(b)}"{cur}><span class="l-name">{html.escape(T(w))}'
                  f'</span>{_L_HAKEN if on else ""}</a></li>')
    menue += f'<li class="b-thema"><button type="button" class="l-item b-thema-b">{html.escape(T("b_thema"))}</button></li>'
    name = T(dict(BEREICHE)[aktiv]) if aktiv in dict(BEREICHE) else T("b_menue")
    return (f'<nav class="bereiche" aria-label="{html.escape(T("b_menue"))}"><ul class="b-liste">{reihe}</ul>'
            f'<div class="b-menu" data-langmenu><button type="button" class="l-toggle b-toggle" aria-expanded="false" '
            f'aria-controls="bmenu" aria-label="{html.escape(T("b_menue"))}: {html.escape(name)}" title="{html.escape(T("b_menue"))}">'
            f'{_B_ICON}<span class="b-cur">{html.escape(name)}</span>{_L_PFEIL}</button>'
            f'<ul class="l-menu" id="bmenu" hidden>{menue}</ul></div></nav>')

def topbar(panels=False, prev_a=None, next_a=None, art=None, bereich="wissen"):
    # Nur Artikelseiten, mittig: Knopf für den Themenbaum und der Umschalter der Ansicht (W4a, 11.11.2026; vorher standen
    # hier die Pfeile zum vorherigen/nächsten Artikel, sie sind jetzt nur noch am Artikelende). prev_a/next_a bleiben als
    # Parameter, damit Aufrufer unverändert bleiben. W4b: links die Bereiche (statt des Editor-Links rechts), die Sprachwahl
    # rechts vor der Suche; Klasse mit-mitte: Artikelseite, die Bereiche klappen dann früher zum Menü zusammen.
    pbtns = ('<div class="panelCenter">'
             + '<button id="toggleLeft" class="panelBtn" aria-label="Themenbaum ein-/ausblenden" title="Themenbaum ein-/ausblenden" aria-pressed="false">'
             '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="9" y1="4" x2="9" y2="20"/></svg></button>'
             + ansicht_schalter(bool(art) and ist_ref(art)) + '</div>') if panels else ''
    return (f'<a class="skip" href="#inhalt">{T("zum_inhalt")}</a>'   # Sprunglink für die Tastatur: erst beim Fokus sichtbar
            f'<div class="topbar{" mit-mitte" if panels else ""}"><a class="brand" href="/">Et<span>Und</span><span class="so">So</span></a>'
            + bereiche_nav(bereich) + pbtns + lang_switch(art)
            + f'<button id="searchBtn" class="searchBtn" aria-label="{T("suchen")}">'   # ohne Lupen-Symbol (User 2026-10-21)
            f'<span class="lbl">{T("suchen")}</span><kbd>/</kbd></button>'
            # Hell/Dunkel-Umschalter — immer oben rechts, auf allen Wissensseiten an gleicher Stelle.
            '<button id="themeBtn" class="iconBtn" aria-label="Hell/Dunkel umschalten" title="Hell/Dunkel umschalten">'
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M21 12.8A8 8 0 1 1 11.2 3 6 6 0 0 0 21 12.8z"/></svg></button></div>'
            '<div id="searchOverlay" class="searchOverlay" hidden><div class="searchBox">'
            f'<input id="searchInput" type="search" placeholder="{T("suche_ph")}" autocomplete="off"/>'
            '<div id="searchResults" class="searchResults"></div>'
            f'<div class="searchHint">{T("suche_hint")}</div></div></div>')

_TOC = {}                                              # Artikeltext -> Abschnittsliste (für die Nachbar-Karten)

# ---------------------------------------------------------------- Ansichten, Formelblatt (W4a) ----
KAPITEL_NR = {}                                        # Kapitelordner (Adresse) -> Nummer im Modul, 1 … n (build_lang)
FB_DL = ("png", "jpg", "svg", "pdf")                   # Formate des Download-Knopfs (assets/formel-export.js)

def kapitel_ordner(path):
    return path.rsplit("/", 1)[0]

def spickzettel_url(art):
    """„Kapitel auf einer Seite“: eine Seite je Modul und Sprache, ?kapitel=N zeigt und druckt nur Kapitel N."""
    kap = kapitel_ordner(art["path"])
    return f'/wissen/{modul_pfad(art["path"])}/spickzettel.html?kapitel={KAPITEL_NR.get(kap, 1)}#k-{kap.rsplit("/", 1)[-1]}'

def _art_anker(art):
    """Sprungmarke eines Artikels auf den Modulseiten (Kapitel-Slug + Artikel-Slug, eindeutig im Modul)."""
    return "a-" + kapitel_ordner(art["path"]).rsplit("/", 1)[-1] + "-" + art["path"].rsplit("/", 1)[-1][:-5]

def _formel_html(tex):
    """Abgesetzte Formel; mehrteilige (\\qquad) als Zeile, deren Teile umbrechen dürfen."""
    teile = split_display("$$" + tex + "$$")
    return ('<div class="mrow">' + "".join(f'<div class="mcell">{inline("$$" + t + "$$")}</div>' for t in teile) + "</div>"
            if teile else inline("$$" + tex + "$$"))

def _links_absolut(h, art_path):
    """Links eines Artikel-Ausschnitts für eine andere Seite: #anker -> Artikel#anker, relative Adressen -> absolut."""
    ordner = kapitel_ordner(art_path)
    def ersetze(m):
        u = m.group(1)
        if u.startswith(("/", "http:", "https:", "mailto:")):
            return m.group(0)
        return f'href="/wissen/{art_path}{u}"' if u.startswith("#") else f'href="/wissen/{ordner}/{u}"'
    return re.sub(r'href="([^"]*)"', ersetze, h)

def blatt_eintraege(z):
    """Formelblatt eines Artikels: Kästen mit Mathe und nummerierte Formeln; gibt es beides nicht, die unnummerierten
    abgesetzten Formeln des Haupttexts."""
    return (z or {}).get("blatt") or (z or {}).get("ku") or []

def blatt_html(eintraege, art_path=None):
    """Einträge als HTML, nach Abschnitten gruppiert. art_path: Seite außerhalb des Artikels (Links absolut)."""
    teile, h_alt = [], None
    basis = f"/wissen/{art_path}" if art_path else ""
    for e in eintraege:
        if e["h"] != h_alt:
            if e["h"]:
                teile.append(f'<div class="fb-h">{inline(_ohne_links(e["h"]))}</div>')
            h_alt = e["h"]
        ziel = f'{basis}#{e["id"]}'
        if e["typ"] == "box":
            inhalt = _links_absolut(e["html"], art_path) if art_path else e["html"]
            teile.append(f'<div class="fb-e fb-k"><a class="fb-n" href="{ziel}">{e["titel"]}</a><div class="fb-i">{inhalt}</div></div>')
        elif e["typ"] == "cmd":                            # Übersicht (Informatik): Eingabezeilen eines Konsolen-Blocks
            teile.append(f'<div class="fb-e fb-cmd"><pre class="fb-code"><code>{html.escape(chr(10).join(e["zeilen"]), quote=False)}</code></pre>'
                         f'<a class="fb-nr fb-ohne" href="{ziel}" title="{html.escape(T("fb_sprung"))}" '
                         f'aria-label="{html.escape(T("fb_sprung"))}">&#8599;</a></div>')
        else:
            nr = " ".join(f"({n})" for n in e["nr"].split("|")) if e["nr"] else ""
            teile.append(f'<div class="fb-e fb-gl"><div class="fb-f">{_formel_html(e["tex"])}</div>'
                         f'<a class="fb-nr{"" if nr else " fb-ohne"}" href="{ziel}" title="{html.escape(T("fb_sprung"))}"'
                         f' aria-label="{html.escape(T("fb_sprung") + (" " + nr if nr else ""))}">{html.escape(nr) or "&#8599;"}</a></div>')
    return "".join(teile)

def _block_html(md, praefix):
    """Geschriebene Kurzfassung/Formelsammlung setzen: eigene Abbildungsnummern, ids mit Präfix (keine Dopplung mit dem
    Artikel), ohne Ankerlinks an den Überschriften."""
    alt = ABB_N[0]
    ABB_N[0] = 0
    try:
        h = md_to_html(md)[0]
    finally:
        ABB_N[0] = alt
    h = re.sub(r'<a class="h-anker"[^>]*>#</a>', "", h)
    return re.sub(r'\sid="([^"]*)"', lambda m: f' id="{praefix}{m.group(1)}"', h)

def dl_knopf():
    """Download-Knopf des Formelblatts: ohne Skript verborgen; Dateien entstehen erst beim Klick im Browser."""
    return (f'<div class="fb-dl" role="group" aria-label="{html.escape(T("dl"))}" hidden><span class="fb-dl-t">{T("dl")}:</span>'
            + "".join(f'<button type="button" class="fb-dl-b" data-format="{f}">{f.upper()}</button>' for f in FB_DL)
            + '<span class="fb-dl-s" aria-live="polite"></span></div>')

def formelblatt_html(art, z, block_html=""):
    """Ansicht „Formeln“ (W4a): Formelblatt des Artikels, ohne Skript verborgen. Mit geschriebener Formelsammlung
    (::::formelsammlung) steht diese da, sonst die Einträge des Sammlers; ohne Formeln ein Hinweis mit dem Wechsel zu
    „Kurz“. Die Formeln setzt KaTeX erst beim ersten Öffnen (Klasse fb-spaeter)."""
    eintraege = blatt_eintraege(z)
    mp, ref = modul_pfad(art["path"]), ist_ref(art)       # ref: Informatik-Reihe, „Übersicht“ statt „Formeln“
    kopf_rechts = f'<a class="fb-modul" href="/wissen/{mp}/{blatt_datei(mp)}#{_art_anker(art)}">{TR("fb_modul", ref)}</a>'
    unter = " · ".join(klartext(x) for x in (art["crumbs"][-2][0].split(" – ")[0] if len(art["crumbs"]) > 1 else "",
                                             art["crumbs"][-1][0] if art["crumbs"] else "") if x)
    if block_html or eintraege:
        inhalt = (f'<div class="fb-inhalt" data-titel="{html.escape(TR("ans_formeln", ref) + ": " + klartext(art["title"]))}" '
                  f'data-unter="{html.escape(unter)}" data-datei="{"uebersicht" if ref else "formeln"}-{art["path"].rsplit("/", 1)[-1][:-5]}">'
                  + (f'<div class="fb-block">{block_html}</div>' if block_html else blatt_html(eintraege)) + "</div>")
        werkzeug = dl_knopf() + kopf_rechts
    else:
        inhalt = (f'<p class="fb-leer">{TR("fb_leer", ref)} <button type="button" class="fb-zu-kurz" data-ansicht-setzen="kurz">'
                  f'{T("fb_zu_kurz")}</button></p>')
        werkzeug = kopf_rechts
    return (f'<section class="fb-blatt fb-spaeter" id="formelblatt" aria-labelledby="fb-titel"><div class="fb-kopf">'
            f'<h2 id="fb-titel">{TR("ans_formeln", ref)}</h2><div class="fb-werkzeug">{werkzeug}</div></div>'
            + inhalt + '<div class="fb-ende"></div></section>')


def render_article(art, tree, prev_a, next_a):
    ABB_N[0] = 0                                       # Abbildungen je Artikel ab 1 nummerieren
    zf_start(ist_ref(art))                             # Sammler der Zusammenfassung: nur für den Artikel selbst
    body_html, toc = md_to_html(art["body"])
    zdaten = dict(ZF)
    ZF["an"] = False
    SAMMEL[art["path"]] = zdaten                       # Begriffsverzeichnis und Lernkarten des Moduls (lernen_seiten)
    body_html = _vorschau_markieren(body_html)         # Links auf Artikel: Link-Vorschau (data-vs)
    _TOC[art["body"]] = toc
    quiz_html = ""                                     # Quiz ganz unten, unter den Nachbar-Spalten (User 2026-10-21)
    mq = re.search(r'<aside class="(?:k[zw] )?callout cx-quiz">', body_html)
    if mq:
        qa = mq.start()
        qe = body_html.index("</aside>", qa) + len("</aside>")
        quiz_html, body_html = body_html[qa:qe], body_html[:qa] + body_html[qe:]
    n_abb = len(re.findall(r'<figure class="(?:k[zw] )?abb"', body_html))
    n_aufg = len(re.findall(r'<div class="(?:k[zw] )?aufg">', body_html))
    if not any(lvl == 2 for _, _, lvl in toc):         # ohne ##-Abschnitte (kurz oder nur ###): eine einzige Karte
        body_html = f'<section class="sect">{body_html}</section>'
    body_html = f'<div class="art-body">{body_html}</div>'   # Ansicht „Kurz“ filtert darin (W4a)
    # am Artikelende, vor den Nachbar-Artikeln (User 11.11.2026); nicht in „Das Wichtigste (bis hier)“: Der Artikel ist
    # mit seinem Kasten :::kern schon die Zusammenfassung des Kapitels
    # W4b: Die Lernkarten des Kapitels stehen jetzt in den Verweisen darunter (Lernkarten und Aufgaben, BEREICH_PLATZ)
    kap_links = f'<a href="{spickzettel_url(art)}">{T("sz_kurz")}</a>'
    fuss = f'<p class="zf-fuss">{kap_links}</p>'
    zf_html = "" if re.search(r"(?m)^:::kern\b", art["body"]) else zusammenfassung_html(zdaten, fuss)
    if not zf_html:                                    # ohne Zusammenfassung: die Kapitel-Links trotzdem am Artikelende
        zf_html = f'<p class="zf-fuss art-ende">{kap_links}</p>'
    # Ansichten (W4a): geschriebene Kurzfassung (sonst filtert „Kurz“ den Artikel) und Formelblatt
    bloecke = art.get("bloecke") or {}
    kurz_html = (f'<div class="ans-kurz" id="kurzfassung">{_block_html(bloecke["kurzfassung"], "kzf-")}</div>'
                 if bloecke.get("kurzfassung") else "")
    blatt = formelblatt_html(art, zdaten, _block_html(bloecke["formelsammlung"], "fsb-") if bloecke.get("formelsammlung") else "")
    pill = (f'<span class="apill apill-mensch">{T("hand_pill")}</span>' if art["autor"] == "mensch"
            else f'<span class="apill">{T("ki_pill")}</span>')
    # Brotkrumen; am Handy nur die letzten zwei Glieder, der Modulname kurz („ET3“ statt „ET3 – Grundgebiete …“)
    n_cr = len(art["crumbs"])
    def _crumb(k, nm):
        cls = "cr cr-alt" if k < n_cr - 2 else ("cr cr-erst" if k == max(0, n_cr - 2) else "cr")
        kurz, _, lang = nm.partition(" – ")
        name = (f'<span class="cr-k">{html.escape(kurz)}</span><span class="cr-l"> – {html.escape(lang)}</span>' if lang
                else html.escape(nm))
        return f'<span class="{cls}"><span class="cr-sep" aria-hidden="true"> › </span>{name}</span>'
    crumb = (f'<nav class="crumbs"><a class="cr-home" href="{home()}">{T("wissen")}</a>'
             + "".join(_crumb(k, nm) for k, (nm, sl) in enumerate(art["crumbs"])) + "</nav>")
    # Kennzahlenzeile: Lesezeit, Abbildungen, Aufgaben, Sprung zur Zusammenfassung; dazu das Schildchen und (schmal) die Sprachwahl
    zahlen = [T("lesezeit").format(n=lesezeit(art["body"]))]
    if n_abb:
        zahlen.append(T("abb_1") if n_abb == 1 else T("abb_n").format(n=n_abb))
    if n_aufg:
        zahlen.append(T("aufg_1") if n_aufg == 1 else T("aufg_n").format(n=n_aufg))
    meta = ('<div class="art-meta"><span class="am-zahlen">'
            + "".join(("<span class=\"am-zeit\">" if k == 0 else "<span>") + f"{html.escape(z)}</span>" for k, z in enumerate(zahlen))
            + "</span>"
            + (f'<a class="am-zf" href="#zusammenfassung">{T("zf_sprung")}</a>' if 'id="zusammenfassung"' in zf_html else "")
            + pill + lang_switch(art, "art") + "</div>")
    toc_html = ""
    arttoc = ""
    if toc:
        eintraege = "".join(f'<li><a href="#{hid}">{inline(_ohne_links(txt))}</a></li>' for hid, txt, _ in toc)
        if 'id="zusammenfassung"' in zf_html:
            eintraege += f'<li class="toc-zf"><a href="#zusammenfassung">{T("zf")}</a></li>'
        toc_html = f'<aside class="toc"><div class="toc-h">{T("auf_seite")}</div><ul>{eintraege}</ul></aside>'
        arttoc = f'<nav class="arttoc" aria-label="{T("im_artikel")}"><div class="arttoc-h">{T("im_artikel")}</div><ul>{eintraege}</ul></nav>'
    def _topics(a):                                    # Themen-Stichpunkte (Abschnitte) eines Nachbarartikels, höchstens 6
        if a["body"] not in _TOC:                      # einmal je Text (Messung 10.11.2026: sonst jeder Artikel dreimal gesetzt)
            _TOC[a["body"]] = md_to_html(a["body"])[1]
        t = _TOC[a["body"]]
        return ("".join(f"<li>{inline(_ohne_links(x))}</li>" for _, x, _ in t[:6])
                + (f'<li class="nb-mehr">…</li>' if len(t) > 6 else ""))
    switch = ""                                        # Umschalter kompakt | ausführlich, mit Lesezeit
    if art.get("alt"):
        kompakt, ausf = (art, art["alt"]) if art["fassung"] == "kompakt" else (art["alt"], art)
        def _fbtn(x, label):
            on = x is art
            return (f'<a class="f-btn{" on" if on else ""}" href="/wissen/{x["path"]}" data-fassung="{x["fassung"]}"'
                    + (' aria-current="page"' if on else "") + f'>{label}<span>{lesezeit(x["body"])} min</span></a>')
        switch = '<nav class="fassung" aria-label="Fassung wählen">' + _fbtn(kompakt, "Kompakt") + _fbtn(ausf, "Ausführlich") + "</nav>"
    nav = '<div class="neighbors">'
    if prev_a:
        nav += (f'<a class="nb" href="/wissen/{prev_a["path"]}"{alt_attr(prev_a)}><div class="nb-dir">← {T("vorher")}</div>'
                f'<div class="nb-t">{html.escape(prev_a["title"])}</div><ul>{_topics(prev_a)}</ul></a>')
    else:
        nav += '<div class="nb empty"></div>'
    if next_a:
        nav += (f'<a class="nb" href="/wissen/{next_a["path"]}"{alt_attr(next_a)}><div class="nb-dir next">{T("weiter")} →</div>'
                f'<div class="nb-t">{html.escape(next_a["title"])}</div><ul>{_topics(next_a)}</ul></a>')
    else:
        nav += '<div class="nb empty"></div>'
    nav += "</div>"
    hat = (" hat-kurz" if kurz_html else "") + (" hat-formeln" if bloecke.get("formelsammlung") else "") + (" ref" if ist_ref(art) else "")
    main = (f'<main class="article" id="inhalt" tabindex="-1"><article class="art{hat}">{crumb}<h1>{html.escape(art["title"])}</h1>'
            + meta + switch + arttoc + kurz_html
            + body_html + blatt + zf_html + verwendet_html(art) + BEREICH_PLATZ.format(tree_art(art)["path"])
            + nav + quiz_html + legal_footer() + "</article>" + toc_html + "</main>")
    nav_path = tree_art(art)["path"]
    body = (topbar(panels=True, prev_a=prev_a, next_a=next_a, art=art)
            + '<div class="layout">'
            + sidebar_html(tree, nav_path, art) + main + "</div>")
    depth = 1 + art["path"].count("/")               # web/wissen/<…chain…>/<a>.html
    return page_shell(art["title"], beschreibung(art), body, depth, sprachen(art))

def beschreibung(art):
    """meta description: Anfang von „Worum es geht“ (:::zweck) als Klartext, mit echten Formeln statt der im Kopf schon
    zerlegten (summary: „lVerty-AxrVert 2“); ohne :::zweck das summary:. Ist der erste Satz kurz (oft ein Rückbezug wie
    „In allen Beispielen war …“), kommt der zweite dazu."""
    m = re.search(r"(?ms)^:::zweck[ \t]*\n(.*?)\n:::[ \t]*$", art["body"])
    text = " ".join(l.strip() for l in m.group(1).split("\n") if l.strip() and not l.strip().startswith("<")) if m else ""
    saetze = [text[a:b].strip() for a, b in _saetze(text)] if text else []
    if not saetze:
        return klartext(art["summary"] or art["title"])
    d = klartext(saetze[0])
    if len(d) < 90 and len(saetze) > 1 and len(d) + len(klartext(saetze[1])) < 260:
        d += ("" if re.search(r"[。！？]$", d) else " ") + klartext(saetze[1])
    return d

LINK_RE = re.compile(r"\]\(/wissen/([^)#\s]+)(?:#([^)\s]*))?\)")

def rueckverweise(tree):
    """{Adresse eines Nachschlage-Artikels: {Adresse des verlinkenden Artikels: (Artikel, {Anker})}} aus den Links aller
    übrigen Artikel derselben Sprache. Links der Nachschlage-Artikel untereinander zählen nicht (Grundlagen 2 -> 1)."""
    flat = flatten(tree)
    ziele = {a["path"]: a for a in flat if a.get("nachschlagen")}
    out = {}
    if not ziele:
        return out
    for a in flat:
        if a.get("nachschlagen"):
            continue
        for m in LINK_RE.finditer(re.sub(r"(?ms)^```.*?^```[ \t]*$", "", a["body"])):
            z = ziele.get(m.group(1))
            if z is not None:
                out.setdefault(z["path"], {}).setdefault(a["path"], (a, set()))[1].add(m.group(2) or "")
    return out

RUECK = {}                                             # rueckverweise() der gerade gebauten Sprache (build_lang setzt es)

def verwendet_html(art):
    """Dezenter Block „Verwendet in“ unter einem Nachschlage-Artikel: die Artikel, die ihn oder seine Abschnitte verlinken,
    in Lesereihenfolge, dazu die verlinkten Unterabschnitte („13.5 Rang“). Ohne solche Links: nichts."""
    eintr = RUECK.get(art["path"]) if art.get("nachschlagen") else None
    if not eintr:
        return ""
    titel = {m.group(2): m.group(1) for m in
             re.finditer(r'(?m)^(?:###|:::::vorwissen)\s+(.+?)\s*\n\s*\n<span class="anker" id="(stufe-\d+-\d+)"></span>', art["body"])}
    rows = []
    for a, anker in sorted(eintr.values(), key=lambda x: (x[0]["order"], x[0]["title"])):
        heft = a["crumbs"][-1][0] if a["crumbs"] else ""      # „Kapitel 2: …“, davor Bereich bzw. Modulkürzel („Python“, „ET3“)
        oben = a["crumbs"][-2][0].split(" – ")[0] if len(a["crumbs"]) > 1 else ""
        text = "".join(x + " › " for x in (oben, heft) if x) + (a["kurz"] or a["title"])
        zu = [k[6:].replace("-", ".") + " " + titel[k] for k in sorted(anker, key=lambda k: [int(x) for x in re.findall(r"\d+", k)] or [0])
              if k in titel]
        rows.append(f'<li><a href="/wissen/{a["path"]}">{html.escape(text)}</a>'
                    + (f'<span class="vw-zu"> · {html.escape(", ".join(zu))}</span>' if zu else "") + "</li>")
    return f'<aside class="verwendet" aria-label="{html.escape(T("verwendet"))}"><div class="vw-h">{T("verwendet")}</div><ul>{"".join(rows)}</ul></aside>'

def legal_footer():
    return (f'<footer class="wfoot">EtUndSo.de · <a href="/impressum.html">{T("impressum")}</a> · '
            f'<a href="/datenschutz.html">{T("datenschutz")}</a></footer>')

# ------------------------------------------ Lernen: Begriffe, Link-Vorschau, Lernkarten (W2, 11.11.2026) ----
# Was ein Leser liest und lernt, bleibt in seinem Browser (localStorage, wissen.js). Der Build legt nur die Inhalte an, je
# Modul und Sprache drei Dateien im Modulordner (…/<modul>/<kapitel>/<artikel>.html -> …/<modul>/):
#   begriffe.html    Begriffsverzeichnis: Begriff, Bestimmung, Link auf die Stelle (alphabetisch; Chinesisch nach Kapiteln)
#   lernkarten.html  seit W4b nur noch Weiterleitung in den Bereich /lernen/ (die Karten stehen in /lernen/daten/)
#   vorschau.json    Titel, Kapitel und „Worum es geht“ jedes Artikels: das Kärtchen der Link-Vorschau
# Quelle ist der Sammler der Zusammenfassung (ZF), den render_article je Artikel in SAMMEL ablegt; nichts wird neu gesucht.
SAMMEL = {}                                            # Artikeladresse -> Sammler-Daten (fb, fm, kg) des Artikels
VORSCHAU = set()                                       # Adressen aller Artikel aller Sprachen (main): Ziele der Link-Vorschau
MODUL_SPRACHEN = {}                                    # Moduladresse (deutsch) -> Sprachen, in denen es das Modul gibt
KARTEN_STAT = {}                                       # Sprache -> {Modul: Zähler} für die Ausgabe des Builds
VORSCHAU_MAX = 230                                     # Zeichen „Worum es geht“ im Kärtchen (Chinesisch: die Hälfte)
_LUECKE, _AN, _AUS = "\x06", "\x07", "\x0e"            # Marken im Markdown der Lückentexte (inline() lässt sie stehen)
_ETIKETT_RE = re.compile(r"^⁠?\*\*[^*\n]{1,48}?[.:：]\*\*\s*")   # „**Quantisierung.** “, „**So liest man das:** “ vor dem Satz
_LINK_A_RE = re.compile(r'<a href="/wissen/([^"#?]+\.html)(?:#[^"]*)?"')
# Karten müssen ohne den Artikel verständlich sein: Bestimmungen, die mit einem Rückbezug beginnen („Ihre Wurzel, die
# Standardabweichung …“, „Hängt er nur …“, „其中 …“), fallen weg; ebenso Formeln, deren Name nur ein Beispiel ankündigt.
_LK_RUECKBEZUG = re.compile(
    r"(?:(?:ihr|ihre|ihren|ihrem|ihrer|ihres|sein|seine|seinen|seinem|seiner|seines|dessen|deren|dies|diese|dieser|dieses|diesen|"
    r"dabei|damit|dafür|dazu|daraus|davon|darin|darauf|daher|deshalb|dort|hier|sie|er|es|so|also|außerdem|ebenso|genauso|dann|nun|"
    r"its|their|this|these|those|it|they|here|there|thus|hence|then|"
    r"su|sus|este|esta|esto|estos|estas|ese|esa|eso|ello|así|aquí|entonces|"
    r"son|sa|ses|leur|leurs|ce|cet|cette|ces|cela|ceci|il|elle|ils|elles|ainsi|alors|donc|"
    r"bu|bunun|buna|bunu|bunlar|şu|onun|ona|onu|böylece|yani|ayrıca)\b|\w+\s+(?:er|sie|it|they)\b|[其这此它该那])", re.I)
_LK_VERWEIS = re.compile(r"(?:\b(?:Unterabschnitt|Abschnitt|Kapitel|Abbildung|Gleichung|Subsection|Section|Chapter|Figure|Equation|"
                         r"Subsección|Sección|Capítulo|Figura|Ecuación|Chapitre|Équation|Bölüm|Şekil|Denklem)\s*\d|"
                         r"第\s*[\d.]+\s*[章节]|图\s*\d)", re.I)
_LK_BEISPIEL = re.compile(r"(?:Beispiel|Example|Ejemplo|Exemple|Örnek|例)", re.I)

def modul_pfad(path):
    """Moduladresse zu einer Artikeladresse: …/<modul>/<kapitel>/<artikel>.html -> …/<modul> (gilt für alle Artikel)."""
    return path.rsplit("/", 2)[0]

def _modul_von(nd):
    """Moduladresse, wenn nd ein Modul ist (seine Unterknoten tragen die Artikel), sonst None."""
    for c in nd["children"]:
        if c["articles"]:
            return modul_pfad(c["articles"][0]["path"])
    return None

def lernen_links(mp, cls):
    """Leise Zeile „Begriffe · Lernkarten“ unter einem Modul (Seitenleiste, Übersicht)."""
    return (f'<div class="{cls}"><a href="/wissen/{mp}/begriffe.html">{T("begriffe")}</a><span aria-hidden="true"> · </span>'
            f'<a href="{html.escape(lernen_url(mp))}">{T("lernkarten")}</a><span aria-hidden="true"> · </span>'
            f'<a href="/wissen/{mp}/{blatt_datei(mp)}">{TR("fb_titel", mp in MODUL_REF) if mp in MODUL_REF else T("ans_formeln")}</a></div>')

def _vorschau_markieren(h):
    """Links auf Artikel bekommen data-vs: wissen.js zeigt dann beim Überfahren, beim Tastaturfokus oder langem Tippen ein
    Kärtchen aus der vorschau.json des Zielmoduls. Nur bekannte Ziele, so bleibt jeder Abruf erfolgreich."""
    return _LINK_A_RE.sub(lambda m: m.group(0) + (" data-vs" if m.group(1) in VORSCHAU else ""), h)

def _kurztext(t, lang, n):
    if len(t) <= n:
        return t
    if lang == "zh":
        return t[:n].rstrip("，、；：") + "…"
    return t[:n].rsplit(" ", 1)[0].rstrip(",;:–") + " …"

def _kapitel_kurz(name):
    """„Kapitel 2: Laplace-Transformation“ -> „Kapitel 2“ (Chinesisch „第 2 章：…“ -> „第 2 章“)."""
    return re.split(r"\s*[:：]\s*", name, maxsplit=1)[0]

def _bestimmung_md(satz):
    return _ohne_links(_ETIKETT_RE.sub("", satz)).strip()

def _sortier(text, lang):
    """Sortierschlüssel eines Begriffs: ohne Umlaute und Akzente; Türkisch mit eigenem Alphabet (ç nach c, ı vor i …)."""
    t = re.sub(r"^[\W_]+", "", klartext(text)).strip()
    if lang == "tr":
        abc = "abcçdefgğhıijklmnoöprsştuüvyz"
        return tuple(abc.index(c) + 1 if c in abc else 100 + ord(c) for c in t.replace("I", "ı").replace("İ", "i").lower()), t
    return fold(t), t

def _buchstabe(text, lang):
    """Gruppe im Verzeichnis: Anfangsbuchstabe (Türkisch mit Ç, Ğ, İ, Ö, Ş, Ü), „0–9“ für Ziffern und Zeichen, „α–ω“ für
    andere Schriften (griechische Formelzeichen)."""
    t = re.sub(r"^[\W_]+", "", klartext(text)).strip()
    if not t or not t[0].isalpha():
        return "0–9"
    c = t[0]
    if lang == "tr":
        c = {"i": "İ", "ı": "I"}.get(c, c.upper())
        return c if c in "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX" else "α–ω"
    c = fold(c)[:1].upper()
    return c if "A" <= c <= "Z" else "α–ω"

def _modul_begriffe(arts):
    """{Schlüssel: Begriff} eines Moduls: je Begriff die erste Nennung mit Bestimmung, sonst die erste überhaupt."""
    begriffe = {}
    for a in arts:
        for b in (SAMMEL.get(a["path"]) or {}).get("fb", []):
            key = fold(klartext(b["md"])).strip()
            if not key:
                continue
            alt = begriffe.get(key)
            if alt is None or (not alt["satz"] and b["satz"]):
                begriffe[key] = {"md": b["md"], "satz": b["satz"], "id": b["id"], "art": a,
                                 "pos": alt["pos"] if alt else len(begriffe)}
    return begriffe

def _modul_kopf(arts, wort, datei, lang):
    """Brotkrumen, Titel und Sprachwahl der Modulseiten (Begriffe, Lernkarten); Rückgabe (Seitenkopf, Pseudo-Artikel, Name)."""
    chain = arts[0]["crumbs"][:-1]                     # bis zum Modul
    name = chain[-1][0]
    kurz = name.split(" – ")[0]
    de_mp = modul_pfad(arts[0]["path"])
    de_mp = de_mp.split("/", 1)[1] if lang != "de" else de_mp
    ziele = {l: f"/wissen/{'' if l == 'de' else l + '/'}{de_mp}/{datei}" for l in LANGS if l in MODUL_SPRACHEN.get(de_mp, ())}
    n = len(chain)
    def _cr(k, nm):                                    # am Handy nur die letzten zwei Glieder: Modul › Begriffe
        cls = "cr cr-alt" if k < n - 1 else "cr cr-erst"
        k_, _, lang_ = nm.partition(" – ")
        inhalt = (f'<span class="cr-k">{html.escape(k_)}</span><span class="cr-l"> – {html.escape(lang_)}</span>' if lang_
                  else html.escape(nm))
        return f'<span class="{cls}"><span class="cr-sep" aria-hidden="true"> › </span>{inhalt}</span>'
    crumb = (f'<nav class="crumbs"><a class="cr-home" href="{home()}">{T("wissen")}</a>'
             + "".join(_cr(k, nm) for k, (nm, _) in enumerate(chain))
             + f'<span class="cr"><span class="cr-sep" aria-hidden="true"> › </span>{html.escape(T(wort))}</span></nav>')
    pseudo = {"ziele": ziele}
    voll = f'<span class="lern-modul">{html.escape(name)}</span>' if name != kurz else ""   # „ET3 – Grundgebiete …“
    kopf = (crumb + f'<h1>{html.escape(T(wort))}: {html.escape(kurz)}</h1>'
            + f'<div class="art-meta lern-meta">{voll}{lang_switch(pseudo, "art")}</div>')
    return kopf, pseudo, name

def _modul_seite(tree, titel, desc, kopf, inhalt, pseudo, mp, depth_datei, cls=""):
    main = (f'<main class="article lern-seite{" " + cls if cls else ""}" id="inhalt" tabindex="-1"><article>{kopf}{inhalt}'
            f'{legal_footer()}</article></main>')
    body = topbar(art=pseudo) + '<div class="layout">' + sidebar_html(tree, None) + main + "</div>"
    return page_shell(titel, desc, body, depth_datei, pseudo["ziele"])

def begriffe_html(tree, mp, arts, begriffe, lang):
    """Seite „Begriffe“ eines Moduls: Buchstabenleiste, Filter (mit Skript), je Begriff Bestimmung und Link zur Stelle."""
    kopf, pseudo, name = _modul_kopf(arts, "begriffe", "begriffe.html", lang)
    kap_nr = {a["path"]: _kapitel_kurz(a["crumbs"][-1][0]) for a in arts}
    nach_kapitel = lang == "zh"                        # ohne Pinyin keine alphabetische Ordnung: nach Kapiteln in Lesefolge
    gruppen = {}
    for key, b in begriffe.items():
        if nach_kapitel:
            g = b["art"]["crumbs"][-1][0]
        else:
            g = _buchstabe(b["md"], lang)
        gruppen.setdefault(g, []).append(b)
    if nach_kapitel:
        kap_folge = {}
        for a in arts:
            kap_folge.setdefault(a["crumbs"][-1][0], len(kap_folge))
        reihe = sorted(gruppen, key=lambda g: kap_folge.get(g, 10**6))
        for g in reihe:
            gruppen[g].sort(key=lambda x: x["pos"])
        marke = {g: (re.search(r"\d+", g).group(0) if re.search(r"\d+", g) else str(i + 1)) for i, g in enumerate(reihe)}
    else:
        reihe = sorted(gruppen, key=lambda g: (0 if g == "0–9" else 2 if g == "α–ω" else 1,
                                               _sortier(g, lang) if g not in ("0–9", "α–ω") else ((), "")))
        for g in reihe:
            gruppen[g].sort(key=lambda x: _sortier(x["md"], lang))
        marke = {g: g for g in reihe}
    abc = "".join(f'<a href="#b-{i}" title="{html.escape(g)}">{html.escape(marke[g])}</a>' for i, g in enumerate(reihe))
    teile = []
    for i, g in enumerate(reihe):
        zeilen = []
        for b in gruppen[g]:
            a = b["art"]
            satz = b["satz"] and _bestimmung_md(b["satz"])
            wo = f'<span class="bg-wo">{html.escape(kap_nr[a["path"]])} · {html.escape(a["kurz"] or a["title"])}</span>'
            zeilen.append(f'<div class="bg-e"><dt><a href="/wissen/{a["path"]}#{b["id"]}">{inline(_ohne_links(b["md"]))}</a></dt>'
                          f'<dd>{inline(satz) + " " if satz else ""}{wo}</dd></div>')
        teile.append(f'<section class="bg-g" id="b-{i}"><h2>{html.escape(g)}</h2><dl class="bg-l">{"".join(zeilen)}</dl></section>')
    anzahl = html.escape(T("bg_anzahl").format(n=len(begriffe)))
    if begriffe:
        inhalt = (f'<p class="lede lern-lede">{T("bg_lede")}</p>'
                  f'<p class="lern-nav"><a href="{html.escape(lernen_url(mp))}">{T("lernkarten")}</a></p>'
                  f'<nav class="bg-abc" aria-label="{html.escape(T("bg_abc"))}">{abc}</nav>'
                  f'<div class="bg-such" hidden><input type="search" class="bg-filter" placeholder="{html.escape(T("bg_filter"))}" '
                  f'aria-label="{html.escape(T("bg_filter"))}" autocomplete="off"/><span class="bg-n" aria-live="polite">{anzahl}</span></div>'
                  + "".join(teile) + f'<p class="bg-nichts" hidden>{T("bg_leer")}</p>')
    else:
        inhalt = f'<p class="lede lern-lede">{T("bg_keine")}</p>'
    titel = f'{T("begriffe")}: {name}'
    return _modul_seite(tree, titel, f'{T("begriffe")} – {name}. {anzahl}.', kopf, inhalt, pseudo, mp, 2 + mp.count("/"))

def _lueckentext(md, woerter, lang):
    """„Kurz gesagt“-Satz als Lückentext: Das erste Wort aus dem Begriffsverzeichnis des Moduls (außerhalb von Formeln und
    Code; Deutsch u. a. mit Endung, z. B. „rückwirkungsfrei|en“) wird zur Lücke. Rückgabe (Vorderseite, Rückseite, Wort) als
    Markdown mit Marken oder None, wenn kein Begriff vorkommt oder vom Satz kaum etwas bliebe. Das Wort ist die richtige
    Antwort im Quiz (W4b)."""
    maske = _maskiert(md)
    best = None
    for w, rx in woerter:
        m = rx.search(maske)
        if m and (best is None or m.start() < best[0] or (m.start() == best[0] and m.end() > best[1])):
            best = (m.start(), m.end())
    if best is None:
        return None
    a, b = best
    rest = klartext(md[:a] + md[b:])
    if len(rest) < (12 if lang == "zh" else 30):
        return None
    return md[:a] + _LUECKE + md[b:], md[:a] + _AN + md[a:b] + _AUS + md[b:], md[a:b]

def _md_html(md):
    return (inline(md).replace(_LUECKE, '<span class="lk-luecke" aria-label="…">______</span>')
            .replace(_AN, '<strong class="lk-wort">').replace(_AUS, "</strong>"))

# ------------------------------------------------------------------------- Bereiche (W4b) ----
# Lernkarten/Quiz/Mischtest: eine App-Seite je Sprache (/lernen/, /lernen/<l>/), Daten je Modul und Sprache unter
# /lernen/daten/<m>[.<l>].json. Aufgaben: Startseite je Sprache (/aufgaben/, /aufgaben/<l>/) und eine statische Seite je
# Modul und Sprache (/aufgaben/<Moduladresse>.html, für Suchmaschinen), die auch der Mischtest liest (keine zweite Kopie der
# Aufgaben). Die W2-Seiten …/lernkarten.html leiten auf den Bereich weiter (gleiche Zahl Dateien, keine toten Links).
# Adressen: m = Ordner unter content/ (et3, linux, ml …), k = Kapitelnummer im Modul, a = Dateiname des Artikels ohne .html;
# ?m=et3&k=2&a=… gilt so in allen Sprachen.
LERNEN_OUT = ROOT / "web" / "lernen"
AUFG_OUT = ROOT / "web" / "aufgaben"
MODUL_ID = {}                                          # Moduladresse (jede Sprache) -> m (main)
BEREICH_N = {"karten": {}, "aufg": {}, "kap_k": {}, "kap_a": {}, "mod_k": {}}   # Zahl der Karten/Aufgaben je Artikel, Kapitel, Modul
PFAD_ART = {}                                          # Artikeladresse -> Artikel (Verweise unter dem Artikel)
BEREICH_PLATZ = "<!--bereich-links:{}-->"            # setzt render_article; build_lang ersetzt ihn, sobald die Zahlen stehen
_BEREICH_PLATZ_RE = re.compile(r"<!--bereich-links:([^>]*?)-->")
TYP_ART = {"begriff": "b", "formel": "f", "herleitung": "h", "zusammenhang": "l"}   # ::::lernkarten: Kartenart -> Kürzel
_KARTE_RE = re.compile(r"(?ms)^:::karte[ \t]+(\S+)[ \t]*\n(.*?)^:::[ \t]*$")
_TRENNER_RE = re.compile(r"(?m)^---[ \t]*$")
GESCHRIEBEN_BEREICH = set()                            # Dateien unter web/lernen und web/aufgaben aus diesem Build
BEREICH_STAT = {}                                      # Sprache -> Zähler (Karten je Art, Herleitungen, Aufgaben je Modul)

def art_stamm(a):
    """Dateiname eines Artikels ohne .html (in allen Sprachen der deutsche): Parameter a der Bereichsadressen."""
    return a["path"].rsplit("/", 1)[-1][:-5]

def lernen_url(mp, art=None, kapitel=None, lang=None):
    """Adresse im Bereich Lernkarten: Modul, dazu Kapitel (Nummer) und Artikel (Dateiname); roh, für href escapen."""
    q = f"?m={MODUL_ID.get(mp, '')}"
    if art is not None:
        kapitel = kapitel_ordner(art["path"])
    if kapitel:
        q += f"&k={KAPITEL_NR.get(kapitel, 1)}"
    if art is not None:
        q += f"&a={art_stamm(art)}"
    return bereich_url("lernen", lang) + q

def aufgaben_url(mp, art=None, kapitel=None):
    """Statische Aufgabenseite eines Moduls; Kapitel/Artikel als Filter (?k=, ?a=) und als Sprungmarke (ohne Skript)."""
    u = f"/aufgaben/{mp}.html"
    if art is not None:
        kapitel = kapitel_ordner(art["path"])
    if not kapitel:
        return u
    n = KAPITEL_NR.get(kapitel, 1)
    if art is None:
        return f"{u}?k={n}#k{n}"
    return f"{u}?k={n}&a={art_stamm(art)}#k{n}-{art_stamm(art)}"

def bereich_schreiben(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
    GESCHRIEBEN_BEREICH.add(path.resolve())

def bereiche_aufraeumen():
    """Dateien unter web/lernen und web/aufgaben, die dieser Build nicht geschrieben hat (Modul umbenannt), und leere Ordner."""
    n = 0
    for wurzel in (LERNEN_OUT, AUFG_OUT):
        if not wurzel.exists():
            continue
        for p in sorted(wurzel.rglob("*")):
            if p.is_file() and p.resolve() not in GESCHRIEBEN_BEREICH:
                p.unlink()
                n += 1
        for d in sorted((d for d in wurzel.rglob("*") if d.is_dir()), key=lambda d: -len(d.parts)):
            if not any(d.iterdir()):
                d.rmdir()
    return n

def _karte_md(md, art_path):
    """Markdown einer Karte (Herleitung, geschriebene Karte) als HTML: ohne Sprungziele, Links absolut."""
    h = re.sub(r'\sid="[^"]*"', "", _block_html(md, "lk-"))
    return _links_absolut(h, art_path).strip()

def _hl_bloecke(zeilen):
    """Blöcke eines Kasteninhalts: Leerzeilen trennen; abgesetzte Formeln über mehrere Zeilen und :::-Kästen bleiben ganz."""
    bloecke, cur, tiefe, formel = [], [], 0, False
    for z in zeilen:
        s = z.strip()
        if not s and not tiefe and not formel:
            if cur:
                bloecke.append("\n".join(cur))
                cur = []
            continue
        cur.append(z)
        if re.match(r":::+\w", s):
            tiefe += 1
        elif re.fullmatch(r":::+", s) and tiefe:
            tiefe -= 1
        elif s.count("$$") % 2:
            formel = not formel
    if cur:
        bloecke.append("\n".join(cur))
    return bloecke

def _hl_schritte(zeilen):
    """Schritte einer Herleitung (Markdown): Jeder Textabsatz beginnt einen Schritt, abgesetzte Formeln gehören zum Schritt
    davor. Bleibt nur ein Schritt, teilen ihn seine Sätze (Formeln danach bleiben beim letzten Satz); Listen und HTML nicht."""
    schritte = []
    for b in _hl_bloecke(zeilen):
        if b.lstrip().startswith("$$") and schritte:
            schritte[-1] += "\n\n" + b
        else:
            schritte.append(b)
    if len(schritte) == 1:
        text, _, rest = schritte[0].partition("\n\n")
        if not re.search(r"<\w|^\s*(?:[-*]|\d+\.)\s|\$\$", text, re.M):
            flach = text.replace("\n", " ")
            teile = [flach[a:b].strip() for a, b in _saetze(flach)]
            teile = [t for t in teile if t]
            if len(teile) >= 2:
                schritte = teile[:-1] + [teile[-1] + ("\n\n" + rest if rest else "")]
    return [s for s in schritte if s.strip()]

def _ziel_md(z):
    """Ziel einer Herleitung: die Formel davor; aus einem langen Satz- oder Definitionskasten nur seine abgesetzten Formeln."""
    if not z or z.lstrip().startswith("$$"):
        return z
    if len(klartext(z)) > 280:
        f = re.findall(r"\$\$.+?\$\$", z, re.S)
        if f:
            return "\n\n".join(f)
    return z

def geschriebene_karten(md):
    """Block ::::lernkarten eines Artikels: [(Kürzel, Frage, [Antwort] bzw. [Schritte])] als Markdown. Format je Karte:
    „:::karte <begriff|formel|herleitung|zusammenhang>“, Frage, eine Zeile „---“, Antwort, „:::“; bei Herleitungen trennen
    weitere „---“ die Schritte. Unbekannte Arten und Karten ohne Antwort fallen weg (Meldung beim Bauen)."""
    karten = []
    for m in _KARTE_RE.finditer(md):
        typ = TYP_ART.get(m.group(1).lower())
        teile = [t.strip() for t in _TRENNER_RE.split(m.group(2))]
        if not typ or len(teile) < 2 or not teile[0] or not any(teile[1:]):
            print("  ::::lernkarten: Karte übersprungen (Art oder ---):", m.group(1), (teile[0] if teile else "")[:50])
            continue
        antwort = [t for t in teile[1:] if t]
        if typ != "h":
            antwort = ["\n\n".join(antwort)]
        karten.append((typ, teile[0], antwort))
    return karten

def modul_karten(mp, arts, begriffe, lang):
    """Lernkarten eines Moduls in Lesefolge: [Karte] und Zähler (gut, aussortiert je Grund). Karte = {id, typ, vorne,
    hinten, anker, _a (Artikel)}, dazu q (Antwort im Quiz, sonst hinten), z/s0/s (Herleitung: Ziel, Ausgangspunkt, Schritte),
    w (geschrieben). Begriff -> Bestimmung; benannte Formel -> Formel; „Kurz gesagt“ -> Lückentext (Art Zusammenhang);
    Herleitung (W4b) -> Ziel (die Formel kurz vor dem Kasten), Ausgangspunkt (erster Schritt) und die übrigen Schritte.
    Ausgesondert: Begriffe ohne Bestimmung, mit Bruchstück („…“) oder Rückbezug am Anfang, Sätze mit Verweis
    („Abschnitt 1.1“), Formeln ohne Namen oder zu einem Beispiel, Sätze ohne Begriff aus dem Verzeichnis, Herleitungen ohne
    Ziel und Titel, Doppel. Hat ein Artikel einen Block ::::lernkarten, gelten für ihn nur dessen Karten. Die ids von
    Begriff, Formel und Lückentext sind dieselben wie in W2: Der Lernstand im Browser bleibt."""
    import hashlib
    stat = {"gut": 0, "ohne Bestimmung": 0, "Bruchstück": 0, "Rückbezug": 0, "Verweis": 0, "Formel ohne Namen": 0,
            "Formel eines Beispiels": 0, "Lückentext ohne Begriff": 0, "Herleitung ohne Ziel und Titel": 0,
            "Herleitung leer": 0, "doppelt": 0}
    woerter = []                                       # Begriffe des Verzeichnisses als Suchmuster, längste zuerst
    for b in begriffe.values():
        w = re.sub(r"\s+", " ", klartext(b["md"])).strip()
        if len(w) < (2 if lang == "zh" else 4) or not re.search(r"\w", w) or re.fullmatch(r"[\d\W]+", w):
            continue
        rx = (re.compile(re.escape(w)) if lang == "zh" else
              re.compile(r"(?<![\w-])" + re.escape(w) + r"\w{0,3}(?![\w])", re.I))
        woerter.append((w, rx))
    woerter.sort(key=lambda x: -len(x[0]))
    karten, ids = [], set()
    def neu(a, typ, key, vorne, hinten, anker, **extra):
        kid = hashlib.sha1(f"{mp}|{typ}|{key}".encode("utf-8")).hexdigest()[:10]
        if kid in ids:
            stat["doppelt"] += 1
            return
        ids.add(kid)
        stat["gut"] += 1
        k = {"id": kid, "typ": typ, "vorne": vorne, "hinten": hinten, "anker": anker, "_a": a}
        k.update({x: v for x, v in extra.items() if v})
        karten.append(k)
    gewaehlt = {b["id"] + "|" + b["art"]["path"]: b for b in begriffe.values()}
    for a in arts:
        z = SAMMEL.get(a["path"]) or {}
        eigene = (a.get("bloecke") or {}).get("lernkarten")
        if eigene:                                     # geschriebene Karten: nur diese, keine automatischen
            for typ, frage, antwort in geschriebene_karten(eigene):
                key = f"w|{art_stamm(a)}|{fold(klartext(frage))}"
                if typ == "h":
                    neu(a, "h", key, _karte_md(frage, a["path"]), "", "", s=[_karte_md(x, a["path"]) for x in antwort], w=1)
                else:
                    neu(a, typ, key, _karte_md(frage, a["path"]), _karte_md(antwort[0], a["path"]), "", w=1)
            continue
        fb = [b for b in z.get("fb", []) if b["id"] + "|" + a["path"] in gewaehlt]
        i = 0                                          # Begriffe mit demselben Satz: eine Karte (wie in der Zusammenfassung)
        while i < len(fb):
            gleich = [fb[i]]
            while fb[i]["satz"] and i + len(gleich) < len(fb) and fb[i + len(gleich)]["satz"] == fb[i]["satz"]:
                gleich.append(fb[i + len(gleich)])
            i += len(gleich)
            satz = gleich[0]["satz"]
            if not satz:
                stat["ohne Bestimmung"] += len(gleich)
                continue
            if "…" in satz:
                stat["Bruchstück"] += len(gleich)
                continue
            bestimmung = _bestimmung_md(satz)
            if _LK_RUECKBEZUG.match(re.sub(r"^[\W_]+", "", klartext(bestimmung))):
                stat["Rückbezug"] += len(gleich)
                continue
            if _LK_VERWEIS.search(klartext(bestimmung)):        # „… aus Unterabschnitt 1.1 …“: ohne den Artikel unverständlich
                stat["Verweis"] += len(gleich)
                continue
            vorne = ", ".join(inline(_ohne_links(b["md"])) for b in gleich)
            neu(a, "b", "|".join(fold(klartext(b["md"])) for b in gleich), vorne, inline(bestimmung), gleich[0]["id"])
        formeln = {}                                   # benannte Formeln: je Name (Kastentitel, Abschnitt) eine Karte
        for f in z.get("fm", []):
            titel = (f["titel"] or "").strip()
            if not klartext(titel):
                stat["Formel ohne Namen"] += 1
                continue
            if _LK_BEISPIEL.match(klartext(titel)):
                stat["Formel eines Beispiels"] += 1
                continue
            formeln.setdefault(titel, []).append(f)
        for titel, fs in formeln.items():
            hinten = "".join(f'<div class="lk-formel">{inline("$$" + f["tex"] + "$$")}</div>' for f in fs)
            neu(a, "f", fold(klartext(titel)) + "|" + re.sub(r"\s+", "", fs[0]["tex"]), inline(_ohne_links(titel)), hinten, fs[0]["id"])
        for k in z.get("kg", []):
            if _LK_VERWEIS.search(klartext(k["md"])):
                stat["Verweis"] += 1
                continue
            lt = _lueckentext(_ohne_links(k["md"]), woerter, lang)
            if lt is None:
                stat["Lückentext ohne Begriff"] += 1
                continue
            neu(a, "l", fold(klartext(k["md"])), _md_html(lt[0]), _md_html(lt[1]), k["id"], q=inline(lt[2]))
        for hl in z.get("hl", []):                     # W4b: Herleitungen, Schritt für Schritt
            titel = (hl["titel"] or "").strip()
            schritte = _hl_schritte(hl["zeilen"])
            if not schritte or not klartext(" ".join(schritte)).strip():
                stat["Herleitung leer"] += 1
                continue
            zmd = _ziel_md(hl["ziel"])
            if not zmd and not klartext(titel):
                stat["Herleitung ohne Ziel und Titel"] += 1
                continue
            zkey = re.sub(r"\s+", "", zmd or "")
            neu(a, "h", f"{art_stamm(a)}|{fold(klartext(titel))}|{zkey}",
                inline(_ohne_links(titel)) if titel else html.escape(T("herleitung")), "", hl["id"],
                z=_karte_md(zmd, a["path"]) if zmd else "",
                s0=_karte_md(schritte[0], a["path"]) if len(schritte) > 1 else "",
                s=[_karte_md(x, a["path"]) for x in (schritte[1:] if len(schritte) > 1 else schritte)])
    return karten, stat

def _modul_name(arts):
    return arts[0]["crumbs"][:-1][-1][0]

def lernen_daten(mp, arts, karten):
    """Inhalt von /lernen/daten/<m>[.<l>].json: Kapitel mit Artikeln (Dateiname, Titel, Adresse, Zahl der Aufgaben) und die
    Karten (k = Kapitelnummer, a = Platz des Artikels im Kapitel, h = Sprungmarke im Artikel)."""
    platz, kap = {}, []
    for k, kname, nr, ks in _kapitel_folge(arts):
        eintraege = []
        for i, a in enumerate(ks):
            platz[a["path"]] = (nr, i)
            eintraege.append([art_stamm(a), klartext(a["kurz"] or a["title"]), "/wissen/" + a["path"],
                              len((SAMMEL.get(a["path"]) or {}).get("ag", []))])
        kap.append({"n": nr, "t": klartext(kname), "a": eintraege})
    kj = []
    for c in karten:
        nr, i = platz[c["_a"]["path"]]
        d = {"id": c["id"], "t": c["typ"], "k": nr, "a": i, "v": c["vorne"]}
        if c["hinten"]:
            d["r"] = c["hinten"]
        if c["anker"]:
            d["h"] = c["anker"]
        for x in ("q", "z", "s0", "s", "w"):
            if c.get(x):
                d[x] = c[x]
        kj.append(d)
    return {"m": MODUL_ID.get(mp, ""), "mp": mp, "name": klartext(_modul_name(arts)), "aufg": f"/aufgaben/{mp}.html",
            "kap": kap, "karten": kj}

def umleitung_html(mp, arts, lang):
    """Frühere Lernkarten-Seite eines Moduls (W2): leitet auf den Bereich weiter, #k-<Kapitel> auf ?k=<Nummer>."""
    ziel = lernen_url(mp, lang=lang)
    karte = {k.rsplit("/", 1)[-1]: nr for k, _, nr, _ in _kapitel_folge(arts)}
    z = html.escape(ziel)
    return (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8"/>'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"/>\n'
            f'<title>{html.escape(T("lernkarten"))}: {html.escape(klartext(_modul_name(arts)))} — EtUndSo</title>'
            f'<meta name="robots" content="noindex"/><link rel="canonical" href="{SITE}{z}"/>\n'
            f'<script>(function(){{var k={json.dumps(karte, ensure_ascii=False)},m=location.hash.match(/^#k-(.+)$/),'
            f'z={json.dumps(ziel)};if(m&&k[m[1]])z+="&k="+k[m[1]];location.replace(z);}})();</script>\n'
            f'<meta http-equiv="refresh" content="0; url={z}"/></head>\n'
            f'<body><p>{html.escape(T("lw_umgezogen"))} <a href="{z}">{html.escape(T("lw_titel"))}</a></p></body></html>\n')

def bereich_links_html(path):
    """Verweise unter einem Artikel (W4b): „Lernkarten: dieser Artikel · Kapitel · Modul“ und „Aufgaben: dieser Artikel ·
    Kapitel“, nur was es gibt."""
    a = PFAD_ART.get(path)
    if a is None:
        return ""
    n, kap, mp = BEREICH_N, kapitel_ordner(path), modul_pfad(path)
    def zeile(wort, links):
        links = [(w, u) for w, u, da in links if da]
        if not links:
            return ""
        return (f'<p><span class="bl-k">{html.escape(T(wort))}</span> '
                + '<span aria-hidden="true"> · </span>'.join(f'<a href="{html.escape(u)}">{html.escape(T(w))}</a>' for w, u in links)
                + "</p>")
    z1 = zeile("vw_lernen", [("vw_artikel", lernen_url(mp, a), n["karten"].get(path)),
                             ("vw_kapitel", lernen_url(mp, kapitel=kap), n["kap_k"].get(kap)),
                             ("vw_modul", lernen_url(mp), n["mod_k"].get(mp))])
    z2 = zeile("vw_aufgaben", [("vw_artikel", aufgaben_url(mp, a), n["aufg"].get(path)),
                               ("vw_kapitel", aufgaben_url(mp, kapitel=kap), n["kap_a"].get(kap))])
    if not (z1 or z2):
        return ""
    return f'<nav class="bereich-links" aria-label="{html.escape(T("vw_label"))}">{z1}{z2}</nav>'

def _bereich_ziele(datei):
    """{Sprache: Adresse} einer Seite der Bereiche, die es in jeder Sprache gibt (/lernen/, /aufgaben/)."""
    return {l: bereich_url(datei, l) for l in TREES}

def bereich_seite(titel, desc, inhalt, bereich, ziele, cls=""):
    """Seite eines Bereichs (Lernkarten, Aufgaben): Kopfleiste mit dem Bereich, ohne Themenbaum, schmale Spalte."""
    pseudo = {"ziele": ziele}
    body = (topbar(art=pseudo, bereich=bereich)
            + f'<main class="article bereich-seite{" " + cls if cls else ""}" id="inhalt" tabindex="-1"><article>{inhalt}'
            + f'{legal_footer()}</article></main>')
    return page_shell(titel, desc, body, 0, ziele, js=("/wissen/assets/bereiche.js",))

def _bereich_kopf(wort_bereich, titel_html, ziele, extra=""):
    """Brotkrumen (Bereich), Titel und schmale Sprachwahl der Bereichsseiten."""
    crumb = (f'<nav class="crumbs"><a class="cr-home" href="{html.escape(bereich_url(wort_bereich))}">'
             f'{html.escape(T(dict(BEREICHE)[wort_bereich]))}</a>{extra}</nav>')
    return crumb + titel_html + f'<div class="art-meta lern-meta">{lang_switch({"ziele": ziele}, "art")}</div>'

def _modul_liste(module, zeile):
    """Module nach Bereich der Website (Elektrotechnik, Informatik) gruppiert; zeile(eintrag) -> <li>…</li>."""
    gruppen = {}
    for e in module:
        gruppen.setdefault(e["gruppe"], []).append(e)
    return "".join(f'<h2 class="bm-g">{html.escape(g)}</h2><ul class="bm-liste">{"".join(zeile(e) for e in es)}</ul>'
                   for g, es in gruppen.items())

def lernen_app_html(lang, module):
    """App-Seite des Bereichs Lernkarten/Quiz/Mischtest einer Sprache. Ohne Skript: die Module mit ihren statischen Seiten
    (Begriffe, Formeln bzw. Übersicht, Aufgaben). Mit Skript (bereiche.js): Auswahl Modul → Kapitel → Artikel, Kartenarten,
    Lernen (Leitner wie W2), Quiz, Mischtest; Adresse ?m=&k=&a=&arten=&modus= teilbar."""
    def zeile(e):
        n = sum(e["n"].values())
        statisch = [(T("begriffe"), f'/wissen/{e["mp"]}/begriffe.html'),
                    (TR("fb_titel", e["mp"] in MODUL_REF), f'/wissen/{e["mp"]}/{blatt_datei(e["mp"])}')]
        if e["na"]:
            statisch.append((T("b_aufgaben"), f'/aufgaben/{e["mp"]}.html'))
        return (f'<li class="bm"><a class="bm-t" href="?m={e["m"]}" data-m="{e["m"]}">{html.escape(e["name"])}</a>'
                f'<span class="bm-n">{html.escape(T("lw_karten_n").format(n=n))}</span>'
                f'<span class="bm-s">' + '<span aria-hidden="true"> · </span>'.join(
                    f'<a href="{html.escape(u)}">{html.escape(w)}</a>' for w, u in statisch) + "</span></li>")
    ziele = _bereich_ziele("lernen")
    daten = [{k: e[k] for k in ("m", "mp", "name", "kurz", "n", "na", "d", "ref")} for e in module]
    inhalt = (_bereich_kopf("lernen", f'<h1>{html.escape(T("lw_titel"))}</h1>', ziele)
              + f'<p class="lede lern-lede">{T("lw_lede")}</p>'
              + '<div class="lw-app" hidden></div>'
              + f'<noscript><p class="lw-ohne">{T("lw_statisch")}</p></noscript>'
              + f'<section class="lw-module">{_modul_liste(module, zeile)}</section>'
              + '<script type="application/json" id="lw-daten">'
              + json.dumps(daten, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>")
    return bereich_seite(T("lw_titel"), T("lw_lede"), inhalt, "lernen", ziele, "lw-seite")

def aufgaben_start_html(lang, module):
    """Startseite des Bereichs Aufgaben einer Sprache: die Module mit Zahl der Aufgaben."""
    ziele = _bereich_ziele("aufgaben")
    def zeile(e):
        n = e["na"]
        return (f'<li class="bm"><a class="bm-t" href="/aufgaben/{e["mp"]}.html">{html.escape(e["name"])}</a>'
                f'<span class="bm-n">{html.escape(T("aufg_1") if n == 1 else T("aufg_n").format(n=n))}</span></li>')
    mit = [e for e in module if e["na"]]
    inhalt = (_bereich_kopf("aufgaben", f'<h1>{html.escape(T("b_aufgaben"))}</h1>', ziele)
              + f'<p class="lede lern-lede">{T("ag_lede")}</p>'
              + f'<section class="ag-module">{_modul_liste(mit, zeile)}</section>')
    return bereich_seite(T("b_aufgaben"), T("ag_lede"), inhalt, "aufgaben", ziele, "ag-start")

def aufgaben_modul_html(mp, arts, lang):
    """Aufgaben eines Moduls (statisch, für Suchmaschinen): Kapitel und Artikel als Gliederung, je Aufgabe Nummer, Text,
    zugeklappte Lösung (KaTeX erst beim Aufklappen: mathe-spaeter) und „Zur Stelle im Artikel“. Mit Skript (bereiche.js):
    Filter Kapitel/Artikel (?k=, ?a=), „gelöst“-Häkchen, „Nur ungelöste“, „Zufällige Aufgabe“. ids in den Aufgaben
    bekommen den Präfix k<N>-<Artikel>- (im Modul eindeutig)."""
    name = _modul_name(arts)
    kurz = name.split(" – ")[0]
    de_mp = mp.split("/", 1)[1] if lang != "de" else mp
    ziele = {l: f"/aufgaben/{'' if l == 'de' else l + '/'}{de_mp}.html" for l in LANGS if l in MODUL_SPRACHEN.get(de_mp, ())}
    teile, nav, n_alle, kap_opt = [], [], 0, ""
    for k, kname, nr, ks in _kapitel_folge(arts):
        abschnitte, n_kap = [], 0
        for a in ks:
            ags = (SAMMEL.get(a["path"]) or {}).get("ag", [])
            if not ags:
                continue
            st = art_stamm(a)
            praefix = f"k{nr}-{st}-"
            items = []
            for g in ags:
                h = _links_absolut(g["html"], a["path"])
                h = re.sub(r'\sid="([^"]*)"', lambda m: f' id="{praefix}{m.group(1)}"', h)
                h = h.replace('class="lo-body"', 'class="lo-body mathe-spaeter"')
                stelle = f'/wissen/{a["path"]}' + (f'#{g["id"]}' if g["id"] else "")
                items.append(f'<div class="ag" data-id="{html.escape(a["path"] + "#" + (g["id"] or str(len(items))))}">{h}'
                             f'<div class="ag-fuss"><a class="ag-stelle" href="{html.escape(stelle)}">{T("lk_stelle")}</a></div></div>')
            n_kap += len(items)
            abschnitte.append(f'<section class="ag-art" id="k{nr}-{st}" data-a="{st}"><h3><a href="/wissen/{a["path"]}">'
                              f'{html.escape(a["title"])}</a></h3>{"".join(items)}</section>')
        if abschnitte:
            n_alle += n_kap
            nav.append(f'<li><a href="#k{nr}">{html.escape(kname)}</a> <span class="ag-zahl">({n_kap})</span></li>')
            kap_opt += f'<option value="{nr}">{html.escape(kname)}</option>'
            teile.append(f'<section class="ag-kap" id="k{nr}" data-k="{nr}"><h2>{html.escape(kname)}</h2>{"".join(abschnitte)}</section>')
    extra = f'<span class="cr"><span class="cr-sep" aria-hidden="true"> › </span>{html.escape(kurz)}</span>'
    titel = f'{T("b_aufgaben")}: {name}'
    kopf = _bereich_kopf("aufgaben", f'<h1>{html.escape(T("b_aufgaben"))}: {html.escape(kurz)}</h1>', ziele, extra)
    if name != kurz:
        kopf = kopf.replace('<div class="art-meta lern-meta">', f'<div class="art-meta lern-meta"><span class="lern-modul">{html.escape(name)}</span>', 1)
    if teile:
        mischtest = lernen_url(mp) + "&modus=test"
        inhalt = (kopf + f'<p class="lede lern-lede">{T("ag_modul_lede")}</p>'
                  f'<p class="lern-nav"><span>{html.escape(T("aufg_1") if n_alle == 1 else T("aufg_n").format(n=n_alle))}</span>'
                  f'<span aria-hidden="true"> · </span><a href="{html.escape(lernen_url(mp))}">{T("lernkarten")}</a>'
                  f'<span aria-hidden="true"> · </span><a href="{html.escape(mischtest)}">{T("ag_test")}</a></p>'
                  f'<nav class="kap-nav ag-nav" aria-label="{html.escape(T("kap_wahl"))}"><ol>{"".join(nav)}</ol></nav>'
                  f'<div class="ag-leiste" hidden><label class="lw-feld"><span>{T("lk_kapitel")}</span> <select class="lw-sel ag-k">'
                  f'<option value="">{T("lk_alle_kap")}</option>{kap_opt}</select></label>'
                  f'<label class="lw-feld"><span>{T("lw_artikel")}</span> <select class="lw-sel ag-a"><option value="">'
                  f'{T("lw_alle_art")}</option></select></label>'
                  f'<label class="ag-offen"><input type="checkbox" class="ag-o"/> {T("ag_offen")}</label>'
                  f'<button type="button" class="ag-zufall">{T("ag_zufall")}</button>'
                  f'<span class="ag-stand" aria-live="polite"></span></div>'
                  + "".join(teile) + f'<p class="ag-nichts" hidden>{T("ag_leer")}</p>'
                  f'<button type="button" class="lern-reset ag-reset" hidden>{T("ag_reset")}</button>')
    else:
        inhalt = kopf + f'<p class="lede lern-lede">{T("ag_keine")}</p>'
    return bereich_seite(titel, f'{titel}. {T("ag_modul_lede")}', inhalt, "aufgaben", ziele, "ag-seite")

def _kapitel_folge(arts):
    """[(Kapitelordner, Name, Nummer, [Artikel])] eines Moduls in Lesefolge."""
    kap = []
    for a in arts:
        k = kapitel_ordner(a["path"])
        if not kap or kap[-1][0] != k:
            kap.append((k, a["crumbs"][-1][0], KAPITEL_NR.get(k, len(kap) + 1), []))
        kap[-1][3].append(a)
    return kap

def _kapitel_leiste(kapitel):
    """Kapitel der Modulseiten (Formelsammlung, Kapitel auf einer Seite): ohne Skript Sprunglinks; mit Skript dazu eine
    Auswahl (?kapitel=N: nur dieses Kapitel zeigen und drucken) und „Drucken“."""
    links = "".join(f'<li><a href="#k-{k.rsplit("/", 1)[-1]}">{html.escape(name)}</a></li>' for k, name, _, _ in kapitel)
    optionen = "".join(f'<option value="{n}">{html.escape(name)}</option>' for _, name, n, _ in kapitel)
    return (f'<nav class="kap-nav" aria-label="{html.escape(T("kap_wahl"))}"><ol>{links}</ol></nav>'
            f'<div class="kap-leiste" hidden><label class="kap-wahl"><span>{T("kap_wahl")}</span> <select class="kap-sel">'
            f'<option value="">{T("kap_alle")}</option>{optionen}</select></label>'
            f'<button type="button" class="kap-druck">{T("drucken")}</button></div>')

def _modul_kurzname(arts):
    return arts[0]["crumbs"][:-1][-1][0].split(" – ")[0]

def formeln_html(tree, mp, arts, lang):
    """Formelsammlung eines Moduls (W4a): je Kapitel und Artikel die Einträge des Formelblatts (Kästen mit Mathe, nummerierte
    Formeln mit Abschnitt); jeder Eintrag verlinkt seine Stelle. Druckbar (A4, ohne Leisten), Download wie am Artikel."""
    ref = mp in MODUL_REF                              # Informatik-Reihe: „Befehlsübersicht“ (uebersicht.html)
    wort = "fb_titel_ref" if ref else "fb_titel"
    kopf, pseudo, name = _modul_kopf(arts, wort, blatt_datei(mp), lang)
    kapitel, teile, n = _kapitel_folge(arts), [], 0
    for k, kname, nr, ks in kapitel:
        abschnitte = []
        for a in ks:
            e = blatt_eintraege(SAMMEL.get(a["path"]))
            if not e:
                continue
            n += len(e)
            abschnitte.append(f'<section class="fs-art" id="{_art_anker(a)}"><h3><a href="/wissen/{a["path"]}">'
                              f'{html.escape(a["title"])}</a></h3>{blatt_html(e, a["path"])}</section>')
        if abschnitte:
            teile.append(f'<section class="fs-kap" id="k-{k.rsplit("/", 1)[-1]}" data-k="{nr}"><h2>{html.escape(kname)}</h2>'
                         + "".join(abschnitte) + "</section>")
    kurz = _modul_kurzname(arts)
    if teile:
        inhalt = (f'<p class="lede lern-lede">{TR("fb_lede", ref)}</p>'
                  f'<p class="lern-nav"><a href="/wissen/{mp}/spickzettel.html">{T("sz_kurz")}</a>'
                  f'<span aria-hidden="true"> · </span><a href="/wissen/{mp}/begriffe.html">{T("begriffe")}</a></p>'
                  + _kapitel_leiste([x for x in kapitel if any(blatt_eintraege(SAMMEL.get(a["path"])) for a in x[3])])
                  + f'<div class="fb-werkzeug fs-werkzeug">{dl_knopf()}</div>'
                  f'<div class="fb-inhalt fs-inhalt" data-titel="{html.escape(T(wort) + ": " + klartext(name))}" '
                  f'data-datei="{"befehlsuebersicht" if ref else "formelsammlung"}-{slugify(kurz)}">' + "".join(teile) + "</div>")
    else:
        inhalt = f'<p class="lede lern-lede">{TR("fb_keine", ref)}</p>'
    titel = f'{T(wort)}: {name}'
    return _modul_seite(tree, titel, f'{T(wort)} – {name}.', kopf, inhalt, pseudo, mp, 2 + mp.count("/"), "fs-seite")

def spickzettel_html(tree, mp, arts, lang):
    """„Kapitel auf einer Seite“ (W4a): die Zusammenfassungen (Begriffe, Formeln, Zusammenhänge) aller Artikel, Kapitel für
    Kapitel; ?kapitel=N zeigt und druckt nur Kapitel N. Artikel „Das Wichtigste“ (Kasten :::kern) haben keine eigene
    Zusammenfassung, sie stehen als Link im Kapitelkopf."""
    kopf, pseudo, name = _modul_kopf(arts, "sz_titel", "spickzettel.html", lang)
    kapitel, teile = _kapitel_folge(arts), []
    for k, kname, nr, ks in kapitel:
        abschnitte, kern = [], []
        for a in ks:
            if re.search(r"(?m)^:::kern\b", a["body"]):
                kern.append(f'<a href="/wissen/{a["path"]}">{html.escape(a["title"])}</a>')
                continue
            zf = zusammenfassung_html(SAMMEL.get(a["path"]) or {"fb": [], "fm": [], "kg": []}, art_path=a["path"])
            if zf:
                abschnitte.append(f'<section class="sz-art"><h3><a href="/wissen/{a["path"]}">{html.escape(a["title"])}</a></h3>'
                                  f'{_links_absolut(zf, a["path"])}</section>')
        if abschnitte:
            teile.append(f'<section class="sz-kap" id="k-{k.rsplit("/", 1)[-1]}" data-k="{nr}"><h2>{html.escape(kname)}</h2>'
                         + (f'<p class="sz-kern">{" · ".join(kern)}</p>' if kern else "") + "".join(abschnitte) + "</section>")
    if teile:
        inhalt = (f'<p class="lede lern-lede">{T("sz_lede")}</p>'
                  f'<p class="lern-nav"><a href="/wissen/{mp}/{blatt_datei(mp)}">{TR("fb_titel", mp in MODUL_REF)}</a>'
                  f'<span aria-hidden="true"> · </span><a href="{html.escape(lernen_url(mp))}">{T("lernkarten")}</a></p>'
                  + _kapitel_leiste([x for x in kapitel if f'data-k="{x[2]}"' in "".join(teile)])
                  + '<div class="sz-inhalt">' + "".join(teile) + "</div>")
    else:
        inhalt = f'<p class="lede lern-lede">{T("sz_keine")}</p>'
    titel = f'{T("sz_titel")}: {name}'
    return _modul_seite(tree, titel, f'{T("sz_titel")} – {name}.', kopf, inhalt, pseudo, mp, 2 + mp.count("/"), "sz-seite")

def vorschau_daten(arts, lang):
    """Inhalt der vorschau.json eines Moduls: {Artikeladresse: [Titel, „Modul · Kapitel“, „Worum es geht“ (gekürzt)]}."""
    d = {}
    for a in arts:
        kap = a["crumbs"][-1][0] if a["crumbs"] else ""
        mod = a["crumbs"][-2][0].split(" – ")[0] if len(a["crumbs"]) > 1 else ""
        lim = VORSCHAU_MAX // 2 if lang == "zh" else VORSCHAU_MAX
        d[a["path"]] = [klartext(a["title"]), " · ".join(x for x in (klartext(mod), klartext(kap)) if x),
                        _kurztext(beschreibung(a), lang, lim)]
    return d

def lernen_seiten(lang, tree, flat, weitere):
    """Je Modul dieser Sprache: begriffe.html, lernkarten.html, vorschau.json (siehe oben). weitere = ausführliche und von
    Hand geschriebene Fassungen (Ziele von Links, aber ohne eigene Begriffe und Karten)."""
    module = {}
    for a in flat:
        module.setdefault(modul_pfad(a["path"]), []).append(a)
    alle = {}
    for a in flat + weitere:
        alle.setdefault(modul_pfad(a["path"]), []).append(a)
    KARTEN_STAT[lang] = {}
    BEREICH_STAT[lang] = {"karten": {}, "aufg": {}, "geschrieben": 0}
    eintraege = []                                     # W4b: Module der Startseiten von Lernkarten und Aufgaben
    suffix = "" if lang == "de" else "." + lang
    n = BEREICH_N
    for mp, arts in module.items():
        ordner = OUT / Path(mp)
        ordner.mkdir(parents=True, exist_ok=True)
        begriffe = _modul_begriffe(arts)
        schreibe(ordner / "begriffe.html", begriffe_html(tree, mp, arts, begriffe, lang))
        karten, stat = modul_karten(mp, arts, begriffe, lang)
        schreibe(ordner / "lernkarten.html", umleitung_html(mp, arts, lang))            # W4b: alte Adresse leitet weiter
        schreibe(ordner / blatt_datei(mp), formeln_html(tree, mp, arts, lang))           # W4a: Formelsammlung/Befehlsübersicht
        schreibe(ordner / "spickzettel.html", spickzettel_html(tree, mp, arts, lang))    # W4a: Kapitel auf einer Seite
        (ordner / "vorschau.json").write_text(json.dumps(vorschau_daten(alle[mp], lang), ensure_ascii=False, separators=(",", ":")),
                                             encoding="utf-8")
        KARTEN_STAT[lang][mp] = stat
        # W4b: Zahlen für die Verweise unter den Artikeln, Daten der Lernkarten, Aufgabenseite des Moduls
        for a in arts:
            PFAD_ART[a["path"]] = a
            na = len((SAMMEL.get(a["path"]) or {}).get("ag", []))
            n["aufg"][a["path"]] = na
            n["kap_a"][kapitel_ordner(a["path"])] = n["kap_a"].get(kapitel_ordner(a["path"]), 0) + na
        je_art = {}
        for c in karten:
            p = c["_a"]["path"]
            n["karten"][p] = n["karten"].get(p, 0) + 1
            n["kap_k"][kapitel_ordner(p)] = n["kap_k"].get(kapitel_ordner(p), 0) + 1
            je_art[c["typ"]] = je_art.get(c["typ"], 0) + 1
            BEREICH_STAT[lang]["geschrieben"] += 1 if c.get("w") else 0
        n["mod_k"][mp] = len(karten)
        m = MODUL_ID.get(mp, "")
        bereich_schreiben(LERNEN_OUT / "daten" / f"{m}{suffix}.json",
                          json.dumps(lernen_daten(mp, arts, karten), ensure_ascii=False, separators=(",", ":")))
        na = sum(n["aufg"].get(a["path"], 0) for a in arts)
        bereich_schreiben(AUFG_OUT / f"{mp}.html", aufgaben_modul_html(mp, arts, lang))
        name = klartext(_modul_name(arts))
        eintraege.append({"m": m, "mp": mp, "name": name, "kurz": name.split(" – ")[0], "gruppe": klartext(arts[0]["crumbs"][0][0]),
                          "n": {t: je_art.get(t, 0) for t in "bfhl"}, "na": na, "d": f"/lernen/daten/{m}{suffix}.json",
                          "ref": 1 if mp in MODUL_REF else 0})
        BEREICH_STAT[lang]["karten"][m] = {t: je_art.get(t, 0) for t in "bfhl"}
        BEREICH_STAT[lang]["aufg"][m] = na
    start = "" if lang == "de" else lang + "/"
    bereich_schreiben(LERNEN_OUT / start / "index.html", lernen_app_html(lang, eintraege))
    bereich_schreiben(AUFG_OUT / start / "index.html", aufgaben_start_html(lang, eintraege))

def _minuten(a):
    """Lesezeit eines Artikels in Minuten, einmal je Artikel berechnet."""
    if "_min" not in a:
        a["_min"] = lesezeit(a["body"])
    return a["_min"]

def _themen_karte(arts):
    """Themenliste eines Kapitels (Klasse theme-card: Häkchen und Balken des Lesefortschritts, wissen.js)."""
    links = "".join(f'<li><a href="/wissen/{a["path"]}"{alt_attr(a)}>{html.escape(a["kurz"] or a["title"])}</a></li>' for a in arts)
    return f'<div class="theme-card"><ul>{links}</ul></div>'

def _hinweis(nd):
    return f'<p class="idx-hinweis">{inline(nd["hinweis"])}</p>' if nd.get("hinweis") else ""   # content/**/_*.md

def _kapitel_html(nd):
    """Kapitel in einer Modulkarte: zugeklappt, mit Zahl der Artikel und Lesezeit; darin die Themen (und Unterkapitel)."""
    arts = flatten([nd])
    zahl = f'{anzahl(len(arts), "n_artikel")} · {T("lesezeit").format(n=sum(_minuten(a) for a in arts))}'
    seite = ""                                         # W4a: „Kapitel auf einer Seite“ (Spickzettel des Kapitels)
    if nd["articles"]:
        a0 = nd["articles"][0]
        seite = f'<p class="kap-seite"><a href="{spickzettel_url(a0).split("#")[0]}">{T("sz_kurz")}</a></p>'
    return (f'<details class="mk-kap"><summary><span class="kap-name">{html.escape(nd["name"])}</span>'
            f'<span class="kap-zahl">{html.escape(zahl)}</span></summary>{_hinweis(nd)}'
            + (_themen_karte(nd["articles"]) if nd["articles"] else "") + seite
            + "".join(_kapitel_html(c) for c in nd["children"]) + "</details>")

def _modul_karte(nd, mp):
    """Karte eines Moduls: Kurzname, voller Name, Zahl der Kapitel und Artikel, Platz für den Fortschrittsbalken; ein Klick
    klappt die Karte über die ganze Breite auf und zeigt die Kapitel. Begriffe und Lernkarten stehen unter der Karte."""
    arts = flatten([nd])
    kurz, _, voll = nd["name"].partition(" – ")
    n_kap = len(nd["children"]) + (1 if nd["articles"] else 0)
    kopf = (f'<summary class="mk-kopf" id="{_uebersicht_anker(nd)}"><span class="mk-titel">{html.escape(kurz)}</span>'
            + (f'<span class="mk-voll">{html.escape(voll)}</span>' if voll else "")
            + f'<span class="mk-zahl">{html.escape(anzahl(n_kap, "n_kapitel"))} · {html.escape(anzahl(len(arts), "n_artikel"))}</span>'
            + '<span class="mk-lf"></span></summary>')
    inhalt = ('<div class="mk-inhalt">' + _hinweis(nd) + (_themen_karte(nd["articles"]) if nd["articles"] else "")
              + "".join(_kapitel_html(c) for c in nd["children"]) + "</div>")
    return f'<div class="mk"><details class="mk-det">{kopf}{inhalt}</details>{lernen_links(mp, "mk-lernen")}</div>'

def _gruppe_html(nd, tiefe):
    """Gruppe (Semester, Reihe): Überschrift und eine Reihe Modulkarten. Ist die Gruppe selbst ein Modul (Linux,
    Cybersecurity), trägt die Reihe genau dessen Karte; Untergruppen folgen als eigene Gruppen."""
    mp = _modul_von(nd)
    karten, weitere = [], []
    if mp:
        karten.append(_modul_karte(nd, mp))
    else:
        for c in nd["children"]:
            cmp_ = _modul_von(c)
            if cmp_:
                karten.append(_modul_karte(c, cmp_))
            elif c["children"] or c["articles"]:
                weitere.append(_gruppe_html(c, tiefe + 1))
        if nd["articles"]:
            karten.append(f'<div class="mk">{_themen_karte(nd["articles"])}</div>')
    anker = "" if mp else f' id="{_uebersicht_anker(nd, tiefe)}"'
    n = min(max(len(karten), 1), 3)
    return (f'<div class="gruppe gr-n{n}"{anker}><h3 class="gr-h">{html.escape(nd["name"])}</h3>{"" if mp else _hinweis(nd)}'
            + (f'<div class="mk-grid">{"".join(karten)}</div>' if karten else "") + "</div>" + "".join(weitere))

def _nur_deutsch(tree):
    """Übersicht einer Übersetzung: Module, die es bisher nur auf Deutsch gibt, als eine Zeile mit Links (einheitlich auf
    Übersicht und Startseite: nicht als Karte, sondern als Hinweis am Ende)."""
    if LANG_NOW[0] == "de" or "de" not in TREES:
        return ""
    fehlt = []
    def walk(nodes):
        for nd in nodes:
            mp = _modul_von(nd)
            if mp:
                if LANG_NOW[0] not in MODUL_SPRACHEN.get(mp, ()):
                    fehlt.append((nd["name"].split(" – ")[0], "/wissen/#" + _uebersicht_anker(nd)))
            else:
                walk(nd["children"])
    walk(TREES["de"])
    if not fehlt:
        return ""
    links = ", ".join(f'<a href="{u}" hreflang="de" lang="de">{html.escape(n)}</a>' for n, u in fehlt)
    return f'<p class="idx-nur-de">{html.escape(T("nur_de"))} {links}</p>'

def render_index(tree):
    """Wissensübersicht (W3a, 11.11.2026; vorher alle Artikeltitel untereinander, ~32 000 px): je Bereich ein Abschnitt,
    darin je Gruppe eine Reihe Modulkarten. Eine Karte zeigt Name, Zahl der Kapitel und Artikel und (wissen.js) den
    Lesefortschritt; ein Klick klappt sie auf und zeigt die Kapitel, jedes wieder zugeklappt mit seinen Themen. Alles sind
    <details> mit festen Links: Ohne Skript lässt sich jede Seite erreichen, Suchmaschinen sehen alle Artikel."""
    teile = [f'<main class="article idx" id="inhalt" tabindex="-1"><article><h1>{T("wissen")}</h1>{lang_switch(None, "art")}'
             f'<p class="lede">{T("lede")}</p>'
             f'<button type="button" class="idx-suche" data-suche hidden><span>{html.escape(T("suche_feld"))}</span><kbd>/</kbd></button>']
    if not tree:
        teile.append(f'<p class="empty">{T("leer")}</p>')
    for nd in tree:
        teile.append(f'<section class="field-block" id="{_uebersicht_anker(nd, 0)}"><h2>{html.escape(nd["name"])}</h2>{_hinweis(nd)}'
                     f'<div class="gruppen">' + "".join(_gruppe_html(c, 1) for c in nd["children"]) + "</div>"
                     + (_themen_karte(nd["articles"]) if nd["articles"] else "") + "</section>")
    teile.append(_nur_deutsch(tree))
    teile.append(legal_footer() + "</article></main>")
    body = topbar() + '<div class="layout">' + sidebar_html(tree, None) + "".join(teile) + "</div>"
    return page_shell(T("wissen"), T("lede"), body, 1, sprachen(None))

# --------------------------------------------------------------------- main ----
TREES = {}                                             # {Sprache: Baum}, von main gesetzt
ART_LANG = {}                                          # (Ordner, Stamm) -> {Sprache: Artikel}: der Sprachumschalter

GESCHRIEBEN = set()                                    # alle Seiten dieses Builds; main löscht danach die übrigen (alte Adressen)
GESCHRIEBEN_DATEN = set()                              # Dateien unter data/suche/ dieses Builds; main löscht die übrigen

def schreibe(path, text):
    path.write_text(text, encoding="utf-8")
    GESCHRIEBEN.add(path.resolve())

def build_lang(lang, tree):
    LANG_NOW[0] = lang
    RUECK.clear()
    RUECK.update(rueckverweise(tree))
    flat = flatten(tree)
    zaehler = {}                                       # Kapitelnummer im Modul (?kapitel=N der Modulseiten), in Lesefolge
    for art in flat:
        kap = kapitel_ordner(art["path"])
        if kap not in KAPITEL_NR:
            mp = modul_pfad(art["path"])
            zaehler[mp] = zaehler.get(mp, 0) + 1
            KAPITEL_NR[kap] = zaehler[mp]
    seiten = []                                        # W4b: (Ziel, HTML); geschrieben nach lernen_seiten
    for idx, art in enumerate(flat):
        prev_a = flat[idx - 1] if idx > 0 else None
        nxt = flat[idx + 1] if idx + 1 < len(flat) else None
        dest = OUT / Path(art["path"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        seiten.append((dest, render_article(art, tree, prev_a, nxt)))
        p2 = (prev_a.get("alt") or prev_a) if prev_a else None   # Nachbarn der ausführlichen Fassung möglichst ebenfalls ausführlich
        n2 = (nxt.get("alt") or nxt) if nxt else None
        if art.get("alt"):
            seiten.append((OUT / Path(art["alt"]["path"]), render_article(art["alt"], tree, p2, n2)))
        h = art.get("human")                           # von Hand geschriebene Fassung(en) desselben Themas
        if h:
            seiten.append((OUT / Path(h["path"]), render_article(h, tree, prev_a, nxt)))
            if h.get("alt"):
                seiten.append((OUT / Path(h["alt"]["path"]), render_article(h["alt"], tree, p2, n2)))

    start = OUT if lang == "de" else OUT / lang
    start.mkdir(parents=True, exist_ok=True)
    schreibe(start / "index.html", render_index(tree))

    # Navigationsbaum (Seitenleiste, Startseite): schlank, ohne Texte; beliebig tief
    def jnode(nd):
        d = {"name": nd["name"], "slug": nd["slug"]}
        mp = _modul_von(nd)
        if mp:
            d["mp"] = mp                               # Modul: Adresse für „Begriffe · Lernkarten“
            d["m"] = MODUL_ID.get(mp, "")                # W4b: Lernkarten unter /lernen/?m=…
            if mp in MODUL_REF:
                d["ref"] = 1                           # W4a: Befehlsübersicht (uebersicht.html) statt Formeln
        d["articles"] = []
        for a in nd["articles"]:
            e = {"title": a["title"], "path": a["path"]}
            if a["kurz"] and a["kurz"] != a["title"]:
                e["kurz"] = a["kurz"]                  # Aufschrift in der Seitenleiste
            if klartext(a["title"]) != a["title"]:
                e["klar"] = klartext(a["title"])       # ohne TeX (Startseite, ohne KaTeX)
            if a.get("alt"):
                e["alt"] = a["alt"]["path"]
            d["articles"].append(e)
        d["children"] = [jnode(c) for c in nd["children"]]
        return d
    tree_json = [jnode(n) for n in tree]
    suffix = "" if lang == "de" else "." + lang
    (OUT / "data" / f"tree{suffix}.json").write_text(json.dumps(tree_json, ensure_ascii=False, separators=(",", ":")),
                                                   encoding="utf-8")

    alts = [a["alt"] for a in flat if a.get("alt")]
    humans = [a["human"] for a in flat if a.get("human")]
    humans += [h["alt"] for h in humans if h.get("alt")]
    suchindex_schreiben(lang, flat + alts)
    lernen_seiten(lang, tree, flat, alts + humans)     # je Modul: Begriffe, Lernkarten, Daten der Link-Vorschau
    for dest, text in seiten:                          # W4b: Artikel erst jetzt, mit den Verweisen auf Lernkarten und Aufgaben
        schreibe(dest, _BEREICH_PLATZ_RE.sub(lambda m: bereich_links_html(m.group(1)), text))
    return len(flat), len(alts), len(humans)

# ------------------------------------------------------------- Suchindex (W3a) ----
# Vorher eine Datei search<.l>.json je Sprache (Deutsch 8,4 MB: Text zweimal, einmal gefaltet), beim ersten Öffnen der
# Suche ganz geladen. Jetzt unter data/suche/<l>/:
#   titel.json    sofort: je Artikel Titel, Brotkrumen, Adresse, Schlagwörter, summary und Abschnitte (Anker, Überschrift),
#                 dazu die Module mit ihrer Volltext-Datei;
#   woerter.json  beim ersten Suchwort: alle Wörter des gefalteten Volltexts, gruppiert nach der Menge der Module, in denen
#                 sie vorkommen ({"0,3": "wort1 wort2 …"}). Ein Suchwort ohne Leerzeichen steht genau dann im Text eines
#                 Moduls, wenn es Teil eines seiner Wörter ist: Geladen werden also nur Module, die wirklich treffen (bei
#                 Leerzeichen: die alle Teile enthalten). Nur ab drei Modulen und wenn das Verzeichnis klein gegen den Text
#                 ist (Chinesisch hat keine Leerzeichen zwischen Wörtern: dort fehlt es, es laden alle Module);
#   <modul>.json  bei Bedarf: der Volltext jedes Artikels des Moduls (ungefaltet; suche.js faltet beim Laden).
# Treffer wie vorher: Teilwort im Titel, in den Schlagwörtern, im Text (summary + Text), gefaltet wie fold(); neu nur der
# Rang für Abschnittsüberschriften zwischen Schlagwort und Text und der Sprung an den Abschnitt.
SUCH_WORT_ANTEIL = 0.25                                # Verzeichnis höchstens ein Viertel so lang wie der Text, sonst keins

def fold_js(s):
    """fold() genau wie suche.js faltet (toLowerCase, ß, ı, œ, æ, NFKD, ohne U+0300–036F): Grundlage des Wortverzeichnisses."""
    s = s.lower().replace("ß", "ss").replace("ı", "i").replace("œ", "oe").replace("æ", "ae")
    return re.sub("[̀-ͯ]", "", unicodedata.normalize("NFKD", s))

def suchindex_schreiben(lang, arts):
    ordner = OUT / "data" / "suche" / lang
    ordner.mkdir(parents=True, exist_ok=True)
    docs, module, texte = [], [], {}
    for a in arts:
        mp = modul_pfad(a["path"])
        if mp not in texte:
            texte[mp] = []
            module.append(mp)
        title = a["title"] + (" (ausführlich)" if a.get("fassung") == "ausfuehrlich" and a.get("alt") else "") \
            + (" (von Hand)" if a["autor"] == "mensch" else "")
        if a["body"] not in _TOC:
            _TOC[a["body"]] = md_to_html(a["body"])[1]
        abschnitte = [[hid, klartext(_ohne_links(txt))] for hid, txt, _ in _TOC[a["body"]]]
        d = [title, " › ".join(nm for nm, _ in a["crumbs"]), a["path"], a["tags"], a["summary"], module.index(mp), abschnitte]
        if klartext(title) != title:
            d.append(klartext(title))                  # Anzeige ohne TeX
        texte[mp].append([len(docs), to_plain(a["body"])])
        docs.append(d)
    eintraege, wort, zeichen = [], {}, 0
    for k, mp in enumerate(module):
        datei = (mp if lang == "de" else mp.split("/", 1)[1]).replace("/", "_") + ".json"
        (ordner / datei).write_text(json.dumps(texte[mp], ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        GESCHRIEBEN_DATEN.add((ordner / datei).resolve())
        gesamt = " ".join(fold_js(docs[i][4] + " " + t) for i, t in texte[mp])   # so durchsucht suche.js den Text
        zeichen += len(gesamt)
        for w in set(gesamt.split(" ")):
            if w:
                wort.setdefault(w, set()).add(k)
        eintraege.append({"p": mp, "f": datei})
    mit_woertern = len(module) >= 3 and sum(len(w) + 1 for w in wort) <= SUCH_WORT_ANTEIL * max(zeichen, 1)
    if mit_woertern:
        gruppen = {}
        for w, ks in wort.items():
            gruppen.setdefault(",".join(str(k) for k in sorted(ks)), []).append(w)
        (ordner / "woerter.json").write_text(json.dumps({m: " ".join(sorted(ws)) for m, ws in sorted(gruppen.items())},
                                                        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        GESCHRIEBEN_DATEN.add((ordner / "woerter.json").resolve())
    (ordner / "titel.json").write_text(json.dumps({"m": eintraege, "w": mit_woertern, "d": docs}, ensure_ascii=False,
                                                  separators=(",", ":")), encoding="utf-8")
    GESCHRIEBEN_DATEN.add((ordner / "titel.json").resolve())
    alt = OUT / "data" / f"search{'' if lang == 'de' else '.' + lang}.json"   # Index von vor W3a
    if alt.exists():
        alt.unlink()

def main():
    TREES.update(collect())
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "data").mkdir(exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)
    for lang, tree in TREES.items():
        for a in flatten(tree):
            ART_LANG.setdefault(a["key"], {})[lang] = a
            for x in (a, a.get("alt"), a.get("human"), (a.get("human") or {}).get("alt")):
                if x:
                    VORSCHAU.add(x["path"])            # Ziele der Link-Vorschau (alle Fassungen, alle Sprachen)
            p = a["path"] if lang == "de" else a["path"].split("/", 1)[1]
            MODUL_SPRACHEN.setdefault(modul_pfad(p), set()).add(lang)
            if ist_ref(a):
                MODUL_REF.add(modul_pfad(a["path"]))     # W4a: Modul mit „Übersicht“ (Adresse dieser Sprache)
    reihen = {}                                        # W4b: m = Ordner unter content/ (bei mehreren Modulen darin: Ordner-Modul)
    for lang, tree in TREES.items():
        for a in flatten(tree):
            p = a["path"] if lang == "de" else a["path"].split("/", 1)[1]
            reihen.setdefault(a["reihe"], set()).add(modul_pfad(p))
    for lang, tree in TREES.items():
        for a in flatten(tree):
            p = a["path"] if lang == "de" else a["path"].split("/", 1)[1]
            r = a["reihe"]
            MODUL_ID[modul_pfad(a["path"])] = r if len(reihen[r]) == 1 else f"{r}-{modul_pfad(p).rsplit('/', 1)[-1]}"
    counts = {lang: build_lang(lang, tree) for lang, tree in TREES.items()}
    alt = alte_seiten_entfernen()
    alt_bereich = bereiche_aufraeumen()                # W4b: alte Dateien unter web/lernen, web/aufgaben
    for p in sorted((OUT / "data" / "suche").rglob("*.json")):   # Suchteile alter Module oder Sprachen
        if p.resolve() not in GESCHRIEBEN_DATEN:
            p.unlink()
    LANG_NOW[0] = "de"
    (OUT / "assets" / "wissen.css").write_text(WISSEN_CSS, encoding="utf-8")
    ui_js = {l: {k: UI[l][k] for k in LERNEN_JS if k in UI[l]} for l in LANGS}   # Oberflächenwörter für wissen.js
    (OUT / "assets" / "wissen.js").write_text(
        WISSEN_JS.replace("/*UI_LERNEN*/{}", json.dumps(ui_js, ensure_ascii=False, separators=(",", ":"))), encoding="utf-8")
    (OUT / "assets" / "suche.js").write_text(SUCHE_JS, encoding="utf-8")
    (OUT / "assets" / "formel-export.js").write_text(FORMEL_EXPORT_JS, encoding="utf-8")   # W4a: lädt erst beim Klick
    ui_b = {l: {k: UI[l][k] for k in BEREICHE_JS if k in UI[l]} for l in LANGS}   # W4b: Wörter für bereiche.js
    (OUT / "assets" / "bereiche.js").write_text(
        BEREICHE_JS_CODE.replace("/*UI_BEREICHE*/{}", json.dumps(ui_b, ensure_ascii=False, separators=(",", ":"))), encoding="utf-8")
    for lang, st in BEREICH_STAT.items():               # W4b: Karten je Art, Aufgaben je Modul
        arten = {t: sum(k[t] for k in st["karten"].values()) for t in "bfhl"}
        print(f"  Bereiche {lang}: Karten " + ", ".join(f"{t} {v}" for t, v in arten.items())
              + f" (geschrieben {st['geschrieben']}); Aufgaben {sum(st['aufg'].values())}: "
              + ", ".join(f"{m} {v}" for m, v in st["aufg"].items()) + (f"; {alt_bereich} alte Dateien entfernt" if alt_bereich and lang == "de" else ""))
    n_start = startseiten_schreiben()
    print(f"  Startseiten: {n_start} Übersetzungen von web/index.html")
    day = write_version()
    for lang, st in KARTEN_STAT.items():               # Lernkarten je Sprache: gute und aussortierte (Gründe siehe modul_karten)
        gut = sum(s["gut"] for s in st.values())
        weg = sum(v for s in st.values() for k, v in s.items() if k != "gut")
        print(f"  Lernkarten {lang}: {gut} in {len(st)} Modulen, {weg} aussortiert")
    n_mod, n_alt, n_hand = counts["de"]
    andere = ", ".join(f"{l}: {c[0]}" for l, c in counts.items() if l != "de")
    print(f"✓ {n_mod} Artikel (+{n_alt} ausführliche Fassungen, +{n_hand} von Hand)"
          + (f", übersetzt {andere}" if andere else "") + f" -> {OUT} · Stand {day}"
          + (f" · {alt} alte Seiten entfernt" if alt else ""))

def alte_seiten_entfernen():
    """Seiten unter web/wissen/, die dieser Build nicht geschrieben hat, sind alte Adressen (umbenannter Artikel, neuer pfad:):
    löschen, dazu leer gewordene Ordner. Ordner mit „_“ am Anfang (Design-Tests) bleiben unberührt, ebenso alte Seiten, auf
    die eine neue Seite noch verlinkt (veraltete Übersetzung mit alten Dateinamen): Sonst entstünden tote Links."""
    alt = [p for p in sorted(OUT.rglob("*.html")) if not p.relative_to(OUT).parts[0].startswith("_") and p.resolve() not in GESCHRIEBEN]
    if not alt:
        return 0
    verlinkt = set()
    for seite in GESCHRIEBEN:
        for href in re.findall(r'href="([^"#?]+\.html)', seite.read_text(encoding="utf-8")):
            ziel = (ROOT / "web" / href.lstrip("/")) if href.startswith("/") else (seite.parent / href)
            verlinkt.add(ziel.resolve())
    n = 0
    for p in alt:
        if p.resolve() in verlinkt:
            print("  alte Seite bleibt (noch verlinkt):", p.relative_to(OUT))
            continue
        p.unlink()
        n += 1
    for d in sorted((d for d in OUT.rglob("*") if d.is_dir()), key=lambda d: -len(d.parts)):
        rel = d.relative_to(OUT)
        if not rel.parts[0].startswith("_") and rel.parts[0] not in ("assets", "data", "img") and not any(d.iterdir()):
            d.rmdir()
    return n

def write_version():
    """web/version.json für die Meldung „Letztes Update“ der Startseite (User 2026-10-21: blieb nach dem Push stehen).
    Datum = jüngste Änderung an Artikeln, diesem Build oder den Dateien unter web/ außer den erzeugten Seiten;
    ein Build ohne Änderungen lässt das Datum also stehen."""
    web = ROOT / "web"
    srcs = list(SRC.rglob("*.md")) + [Path(__file__).resolve()] + \
        [p for p in web.rglob("*") if p.is_file() and OUT not in p.parents and p.name != "version.json"]
    day = datetime.date.fromtimestamp(max(p.stat().st_mtime for p in srcs)).isoformat()
    (web / "version.json").write_text(f'{{ "updated": "{day}" }}\n', encoding="utf-8")
    return day

# ------------------------------------------------------- Startseite in sechs Sprachen (W3a) ----
# web/index.html bleibt die deutsche Startseite und die Vorlage (von Hand gepflegt). Der Build schreibt daraus
# web/<l>/index.html: Inhalt der Elemente mit data-i18n="schlüssel" und Attribute aus data-i18n-attr="attr:schlüssel;…"
# kommen aus STARTSEITE_TEXTE, die Wörter der Skripte (<script id="seite-text">) aus deren "js", die Sprachwahl aus
# lang_switch, Bilder aus web/abbildungen/<l>/ (wenn es sie gibt), Links auf /wissen/ zeigen auf /wissen/<l>/. Module,
# die es in der Sprache noch nicht gibt, nennt eine Zeile unter der Übersicht (wie auf /wissen/<l>/). Fehlt ein Text,
# bleibt der deutsche stehen (Meldung beim Bauen). Impressum und Datenschutz bleiben deutsch.
STARTSEITE_TEXTE = {
    "en": {
        "titel": "EtUndSo — Explanations & tools for electrical engineering",
        "beschreibung": "EtUndSo: clear, animated explanations and tools for electrical engineering and mathematics modules — and so on. "
                        "With the browser editor to rebuild them yourself.",
        "banner": "Still under construction, expanded continuously.", "update": "Last update:",
        "nav_wissen": "Knowledge", "nav_editor": "Editor", "nav_videos": "Videos", "editor_oeffnen": "Open editor",
        "nav_lernen": "Flashcards", "nav_aufgaben": "Exercises", "nav_bereiche": "Sections",
        "be_wissen": "Explanations from the ground up: detailed, short or as a formula collection.",
        "be_lernen": "Terms, formulas, derivations and key relationships as a card box, quiz or mixed test.",
        "be_aufgaben": "All exercises from the articles, with detailed solutions.",
        "be_editor": "Build animations and figures right in the browser.",
        "eyebrow": "Electrical engineering — and so on",
        "h1": 'Electrical engineering and so on, explained <span class="u">in depth</span> and animated.',
        "hero_p": "EtUndSo brings together step-by-step explanations, animations and tools for electrical engineering and mathematics "
                  "modules — plus a few other subjects along the way. Anything you see, you can rebuild yourself in the <strong>editor</strong>.",
        "editor_oeffnen_pfeil": "Open editor →", "module_ansehen": "Browse modules",
        "foto1_t": "Field lines – open in the editor",
        "foto1_alt": "Field line diagrams: opposite and like charges, a pair of plates, a metal tube between plates",
        "foto2_t": "Dot product – open in the editor",
        "foto2_alt": "Dot product of two vectors, worked out step by step: 360 + 30 + (−100) = 290",
        "foto3_t": "3D surface – open in the editor",
        "foto3_alt": "3D surface: collector current I_C of a transistor over U_BE and U_CE",
        "hero_cap": "Three figures from the articles, built in the editor. A click opens them there.",
        "editor_h2": "The editor", "editor_titel": "Mathematical animations right in the browser",
        "editor_p": "A browser-based evolution of Manim: put together objects and operations, play them back and export them as an image "
                    "or video. No installation, nothing to set up.",
        "editor_li1": "Functions, 3D surfaces, sums & products, convolutions",
        "editor_li2": "Step-by-step choreography instead of a mere graphic", "editor_li3": "Export as an image or smooth video",
        "video_label": "Animation: The Fourier series builds a square wave term by term, with harmonics and amplitude spectrum",
        "video_cap": "Fourier series of a square wave, term by term", "im_editor": "Open in the editor →",
        "mod_eyebrow": "Modules", "mod_h2": "Subjects & topics",
        "mod_p": "An overview of all modules — click a module to expand its topics, or search directly: for a module, a topic or a term "
                 "anywhere in the article text.",
        "suche_label": "Search the knowledge base",
        "suche_ph": "Search for a module, topic or term — parts of words work too (e.g. “divider”)",
        "laedt": "Loading the overview …", "zum_wissen": "Go to the knowledge base →", "ganzer_bereich": "Open the whole knowledge base →",
        "how_eyebrow": "How it works", "how_h2": "From concept to clarity",
        "how1_h": "The picture first",
        "how1_p": "Every topic starts with something you can picture — an analogy and the big picture, before any formulas.",
        "how2_h": "Then the physics", "how2_p": "Derived carefully, always with the “why”: which mechanism produces the effect.",
        "how3_h": "Rebuild it yourself",
        "how3_p": "The animations are made in the editor — you can open them, change them and experiment on your own.",
        "videos_eyebrow": "soon", "videos_h2": "Explainer videos",
        "videos_p": "Short animated videos on individual topics — built with the editor. Coming soon.",
        "stats_label": "Usage figures", "stat_site": "Page views", "stat_editor": "Editor opened",
        "fuss": "EtUndSo.de · Explanations & tools for electrical engineering — and so on.",
        "impressum": "Legal notice", "datenschutz": "Privacy", "recht_de": "The legal pages are in German.",
        "js": {"artikel": "{n} articles", "nichts": "Nothing found for “{q}”.", "fehler": "The overview could not be loaded.",
               "zum_wissen": "Go to the knowledge base →", "weiterlesen": "Continue reading", "volltext": "Searching the full text …",
               "locale": "en-GB"},
    },
    "es": {
        "titel": "EtUndSo — Explicaciones y herramientas de ingeniería eléctrica",
        "beschreibung": "EtUndSo: explicaciones claras y animadas, y herramientas para módulos de ingeniería eléctrica y matemáticas — y más. "
                        "Con el editor en el navegador para reconstruirlas tú mismo.",
        "banner": "Todavía en construcción; se amplía continuamente.", "update": "Última actualización:",
        "nav_wissen": "Conocimiento", "nav_editor": "Editor", "nav_videos": "Vídeos", "editor_oeffnen": "Abrir el editor",
        "nav_lernen": "Tarjetas", "nav_aufgaben": "Ejercicios", "nav_bereiche": "Secciones",
        "be_wissen": "Explicaciones desde la base: detalladas, breves o como formulario.",
        "be_lernen": "Términos, fórmulas, deducciones y relaciones clave: fichero de tarjetas, cuestionario o prueba mixta.",
        "be_aufgaben": "Todos los ejercicios de los artículos, con soluciones detalladas.",
        "be_editor": "Crea animaciones y figuras directamente en el navegador.",
        "eyebrow": "Ingeniería eléctrica — y más",
        "h1": 'Ingeniería eléctrica y más, explicada <span class="u">a fondo</span> y animada.',
        "hero_p": "EtUndSo reúne explicaciones paso a paso, animaciones y herramientas para módulos de ingeniería eléctrica y matemáticas "
                  "— y, de paso, algunas otras materias. Lo que ves puedes reconstruirlo tú mismo en el <strong>editor</strong>.",
        "editor_oeffnen_pfeil": "Abrir el editor →", "module_ansehen": "Ver los módulos",
        "foto1_t": "Líneas de campo – abrir en el editor",
        "foto1_alt": "Diagramas de líneas de campo: cargas opuestas e iguales, un par de placas, un tubo metálico entre placas",
        "foto2_t": "Producto escalar – abrir en el editor",
        "foto2_alt": "Producto escalar de dos vectores, calculado paso a paso: 360 + 30 + (−100) = 290",
        "foto3_t": "Superficie 3D – abrir en el editor",
        "foto3_alt": "Superficie 3D: corriente de colector I_C de un transistor en función de U_BE y U_CE",
        "hero_cap": "Tres figuras de los artículos, creadas en el editor. Un clic las abre allí.",
        "editor_h2": "El editor", "editor_titel": "Animaciones matemáticas directamente en el navegador",
        "editor_p": "Una evolución de Manim en el navegador: combina objetos y operaciones, reprodúcelos y expórtalos como imagen o "
                    "vídeo. Sin instalación, nada que configurar.",
        "editor_li1": "Funciones, superficies 3D, sumas y productos, convoluciones",
        "editor_li2": "Coreografía paso a paso en lugar de un simple gráfico", "editor_li3": "Exportación como imagen o vídeo fluido",
        "video_label": "Animación: la serie de Fourier construye una onda cuadrada término a término, con armónicos y espectro de amplitud",
        "video_cap": "Serie de Fourier de una onda cuadrada, término a término", "im_editor": "Abrir en el editor →",
        "mod_eyebrow": "Módulos", "mod_h2": "Materias y temas",
        "mod_p": "Una vista general de todos los módulos: haz clic en un módulo para desplegar sus temas, o busca directamente un "
                 "módulo, un tema o un término en el texto de los artículos.",
        "suche_label": "Buscar en el conocimiento",
        "suche_ph": "Buscar módulo, tema o término — también partes de palabras (p. ej., «divisor»)",
        "laedt": "Cargando la vista general …", "zum_wissen": "Ir al conocimiento →", "ganzer_bereich": "Abrir todo el conocimiento →",
        "how_eyebrow": "Cómo funciona", "how_h2": "Del concepto a la claridad",
        "how1_h": "Primero la imagen",
        "how1_p": "Cada tema empieza de forma intuitiva — con una analogía y el contexto general, antes de las fórmulas.",
        "how2_h": "Luego la física", "how2_p": "Deducida con cuidado, siempre con el «porqué»: qué mecanismo produce el efecto.",
        "how3_h": "Reconstruirlo tú mismo",
        "how3_p": "Las animaciones se crean en el editor — puedes abrirlas, modificarlas y experimentar por tu cuenta.",
        "videos_eyebrow": "pronto", "videos_h2": "Vídeos explicativos",
        "videos_p": "Vídeos cortos y animados sobre temas concretos — hechos con el editor. Próximamente.",
        "stats_label": "Cifras de uso", "stat_site": "Visitas", "stat_editor": "Editor abierto",
        "fuss": "EtUndSo.de · Explicaciones y herramientas de ingeniería eléctrica — y más.",
        "impressum": "Aviso legal", "datenschutz": "Privacidad", "recht_de": "Las páginas legales están en alemán.",
        "js": {"artikel": "{n} artículos", "nichts": "No se encontró nada para «{q}».", "fehler": "No se pudo cargar la vista general.",
               "zum_wissen": "Ir al conocimiento →", "weiterlesen": "Seguir leyendo", "volltext": "Buscando en el texto completo …",
               "locale": "es-ES"},
    },
    "zh": {
        "titel": "EtUndSo — 电气工程讲解与工具",
        "beschreibung": "EtUndSo：清晰的动画讲解和工具，涵盖电气工程与数学课程模块，还有更多。借助浏览器中的编辑器亲手重现。",
        "banner": "仍在建设中，持续扩充", "update": "最近更新：",
        "nav_wissen": "知识库", "nav_editor": "编辑器", "nav_videos": "视频", "editor_oeffnen": "打开编辑器",
        "nav_lernen": "学习卡片", "nav_aufgaben": "练习", "nav_bereiche": "栏目",
        "be_wissen": "从基础讲起的讲解：详细、简要或公式汇编。",
        "be_lernen": "术语、公式、推导和关键联系：卡片盒、测验或综合测试。",
        "be_aufgaben": "文章中的全部练习，附详细解答。",
        "be_editor": "直接在浏览器中制作动画和插图。",
        "eyebrow": "电气工程及更多",
        "h1": '电气工程及更多，<span class="u">详细</span>讲解，配有动画。',
        "hero_p": "EtUndSo 汇集电气工程和数学课程模块的分步讲解、动画和工具，也顺带涉及其他一些学科。你看到的内容，都可以在"
                  "<strong>编辑器</strong>中亲手重现。",
        "editor_oeffnen_pfeil": "打开编辑器 →", "module_ansehen": "浏览模块",
        "foto1_t": "电场线 – 在编辑器中打开", "foto1_alt": "电场线图：异号和同号电荷、一对极板、极板之间的金属管",
        "foto2_t": "标量积 – 在编辑器中打开", "foto2_alt": "两个向量的标量积，逐步计算：360 + 30 + (−100) = 290",
        "foto3_t": "三维曲面 – 在编辑器中打开", "foto3_alt": "三维曲面：晶体管集电极电流 I_C 随 U_BE 和 U_CE 的变化",
        "hero_cap": "三幅插图取自文章，均用编辑器制作。点击即可在编辑器中打开。",
        "editor_h2": "编辑器", "editor_titel": "直接在浏览器中制作数学动画",
        "editor_p": "在浏览器中运行、以 Manim 为基础进一步发展的工具：组合对象和操作，播放，并导出为图片或视频。无需安装，无需配置。",
        "editor_li1": "函数、三维曲面、求和与乘积、卷积", "editor_li2": "分步编排，而不只是一张静态图", "editor_li3": "导出为图片或流畅的视频",
        "video_label": "动画：傅里叶级数逐项构建方波，附谐波和幅度谱",
        "video_cap": "方波的傅里叶级数，逐项展开", "im_editor": "在编辑器中打开 →",
        "mod_eyebrow": "模块", "mod_h2": "学科与主题",
        "mod_p": "所有模块一览：点击模块即可展开其主题；也可以直接搜索模块、主题或文章正文中的术语。",
        "suche_label": "搜索知识库", "suche_ph": "搜索模块、主题或术语，也可以只输入词的一部分（例如“分压”）",
        "laedt": "正在加载总览 …", "zum_wissen": "前往知识库 →", "ganzer_bereich": "打开整个知识库 →",
        "how_eyebrow": "学习方式", "how_h2": "从概念到清晰",
        "how1_h": "先看图景", "how1_p": "每个主题都从直观入手：先用类比和整体联系，再引入公式。",
        "how2_h": "再讲物理", "how2_p": "严谨推导，始终回答“为什么”：是哪种机制产生了这种效果。",
        "how3_h": "亲手重现", "how3_p": "动画都在编辑器中制作：你可以打开、修改并自己动手实验。",
        "videos_eyebrow": "即将推出", "videos_h2": "讲解视频", "videos_p": "针对单个主题的简短动画视频，用编辑器制作。即将推出。",
        "stats_label": "使用统计", "stat_site": "页面访问", "stat_editor": "编辑器打开次数",
        "fuss": "EtUndSo.de · 电气工程讲解与工具，以及更多。",
        "impressum": "法律声明", "datenschutz": "隐私", "recht_de": "法律页面为德语。",
        "js": {"artikel": "{n} 篇文章", "nichts": "未找到“{q}”。", "fehler": "无法加载总览。", "zum_wissen": "前往知识库 →",
               "weiterlesen": "继续阅读", "volltext": "正在搜索全文 …", "locale": "zh-CN"},
    },
    "fr": {
        "titel": "EtUndSo — Explications et outils pour l’électrotechnique",
        "beschreibung": "EtUndSo : des explications claires et animées et des outils pour les modules d’électrotechnique et de "
                        "mathématiques — et plus encore. Avec l’éditeur dans le navigateur pour les reconstruire soi-même.",
        "banner": "Encore en construction, enrichi en continu.", "update": "Dernière mise à jour :",
        "nav_wissen": "Connaissances", "nav_editor": "Éditeur", "nav_videos": "Vidéos", "editor_oeffnen": "Ouvrir l’éditeur",
        "nav_lernen": "Fiches", "nav_aufgaben": "Exercices", "nav_bereiche": "Rubriques",
        "be_wissen": "Des explications en partant des bases\u00a0: détaillées, courtes ou sous forme de formulaire.",
        "be_lernen": "Notions, formules, démonstrations et relations clés\u00a0: boîte à fiches, quiz ou test mixte.",
        "be_aufgaben": "Tous les exercices des articles, avec des solutions détaillées.",
        "be_editor": "Créez des animations et des figures directement dans le navigateur.",
        "eyebrow": "Électrotechnique — et plus",
        "h1": 'L’électrotechnique et plus, expliquée <span class="u">en détail</span> et animée.',
        "hero_p": "EtUndSo réunit des explications pas à pas, des animations et des outils pour les modules d’électrotechnique et de "
                  "mathématiques — et, au passage, quelques autres matières. Ce que vous voyez, vous pouvez le reconstruire vous-même "
                  "dans l’<strong>éditeur</strong>.",
        "editor_oeffnen_pfeil": "Ouvrir l’éditeur →", "module_ansehen": "Voir les modules",
        "foto1_t": "Lignes de champ – ouvrir dans l’éditeur",
        "foto1_alt": "Lignes de champ : charges de signes opposés et de même signe, paire de plaques, tube métallique entre des plaques",
        "foto2_t": "Produit scalaire – ouvrir dans l’éditeur",
        "foto2_alt": "Produit scalaire de deux vecteurs, calculé pas à pas : 360 + 30 + (−100) = 290",
        "foto3_t": "Surface 3D – ouvrir dans l’éditeur",
        "foto3_alt": "Surface 3D : courant de collecteur I_C d’un transistor en fonction de U_BE et U_CE",
        "hero_cap": "Trois figures tirées des articles, construites dans l’éditeur. Un clic les y ouvre.",
        "editor_h2": "L’éditeur", "editor_titel": "Des animations mathématiques directement dans le navigateur",
        "editor_p": "Une évolution de Manim dans le navigateur : assembler des objets et des opérations, les lire et les exporter "
                    "en image ou en vidéo. Aucune installation, rien à configurer.",
        "editor_li1": "Fonctions, surfaces 3D, sommes et produits, convolutions",
        "editor_li2": "Une chorégraphie pas à pas plutôt qu’un simple graphique", "editor_li3": "Export en image ou en vidéo fluide",
        "video_label": "Animation : la série de Fourier construit un signal carré terme par terme, avec les harmoniques et le "
                       "spectre d’amplitude",
        "video_cap": "Série de Fourier d’un signal carré, terme par terme", "im_editor": "Ouvrir dans l’éditeur →",
        "mod_eyebrow": "Modules", "mod_h2": "Matières et thèmes",
        "mod_p": "Un aperçu de tous les modules — cliquez sur un module pour déplier ses thèmes, ou cherchez directement un module, un "
                 "thème ou une notion dans le texte des articles.",
        "suche_label": "Rechercher dans les connaissances",
        "suche_ph": "Chercher un module, un thème ou une notion — aussi une partie de mot (p. ex. « diviseur »)",
        "laedt": "Chargement de l’aperçu …", "zum_wissen": "Vers les connaissances →", "ganzer_bereich": "Ouvrir toutes les connaissances →",
        "how_eyebrow": "Comment ça marche", "how_h2": "Du concept à la clarté",
        "how1_h": "D’abord l’image",
        "how1_p": "Chaque thème commence de façon concrète — par une analogie et la vue d’ensemble, avant les formules.",
        "how2_h": "Ensuite la physique",
        "how2_p": "Établie avec soin, toujours avec le « pourquoi » : quel mécanisme produit l’effet.",
        "how3_h": "Reconstruire soi-même",
        "how3_p": "Les animations sont créées dans l’éditeur — vous pouvez les ouvrir, les modifier et expérimenter vous-même.",
        "videos_eyebrow": "bientôt", "videos_h2": "Vidéos explicatives",
        "videos_p": "De courtes vidéos animées sur des thèmes précis — réalisées avec l’éditeur. Bientôt disponibles.",
        "stats_label": "Chiffres d’utilisation", "stat_site": "Pages vues", "stat_editor": "Éditeur ouvert",
        "fuss": "EtUndSo.de · Explications et outils pour l’électrotechnique — et plus.",
        "impressum": "Mentions légales", "datenschutz": "Confidentialité", "recht_de": "Les pages juridiques sont en allemand.",
        "js": {"artikel": "{n} articles", "nichts": "Aucun résultat pour « {q} ».", "fehler": "Impossible de charger l’aperçu.",
               "zum_wissen": "Vers les connaissances →", "weiterlesen": "Reprendre la lecture",
               "volltext": "Recherche dans le texte intégral …", "locale": "fr-FR"},
    },
    "tr": {
        "titel": "EtUndSo — Elektrik mühendisliği için açıklamalar ve araçlar",
        "beschreibung": "EtUndSo: elektrik mühendisliği ve matematik modülleri için anlaşılır, animasyonlu açıklamalar ve araçlar — ve daha "
                        "fazlası. Tarayıcıdaki editörle kendiniz yeniden oluşturabilirsiniz.",
        "banner": "Hâlâ yapım aşamasında, sürekli genişletiliyor.", "update": "Son güncelleme:",
        "nav_wissen": "Bilgi", "nav_editor": "Editör", "nav_videos": "Videolar", "editor_oeffnen": "Editörü aç",
        "nav_lernen": "Kartlar", "nav_aufgaben": "Alıştırmalar", "nav_bereiche": "Bölümler",
        "be_wissen": "Temelden başlayan açıklamalar: ayrıntılı, kısa ya da formül derlemesi olarak.",
        "be_lernen": "Kavramlar, formüller, türetmeler ve temel ilişkiler: kart kutusu, test ya da karma sınav.",
        "be_aufgaben": "Makalelerdeki tüm alıştırmalar, ayrıntılı çözümleriyle.",
        "be_editor": "Animasyonları ve şekilleri doğrudan tarayıcıda oluşturun.",
        "eyebrow": "Elektrik mühendisliği — ve daha fazlası",
        "h1": 'Elektrik mühendisliği ve daha fazlası, <span class="u">ayrıntılı</span> açıklamalı ve animasyonlu.',
        "hero_p": "EtUndSo, elektrik mühendisliği ve matematik modülleri için adım adım açıklamaları, animasyonları ve araçları bir araya "
                  "getirir; yanı sıra birkaç başka dersi de. Gördüğünüz her şeyi <strong>editörde</strong> kendiniz yeniden "
                  "oluşturabilirsiniz.",
        "editor_oeffnen_pfeil": "Editörü aç →", "module_ansehen": "Modüllere göz at",
        "foto1_t": "Alan çizgileri – editörde aç",
        "foto1_alt": "Alan çizgisi resimleri: zıt ve aynı işaretli yükler, plaka çifti, plakalar arasında metal boru",
        "foto2_t": "Skaler çarpım – editörde aç",
        "foto2_alt": "İki vektörün skaler çarpımı, adım adım hesaplanmış: 360 + 30 + (−100) = 290",
        "foto3_t": "3B yüzey – editörde aç",
        "foto3_alt": "3B yüzey: bir transistörün kolektör akımı I_C, U_BE ve U_CE’ye göre",
        "hero_cap": "Makalelerden üç şekil, editörde oluşturuldu. Tıklayınca orada açılır.",
        "editor_h2": "Editör", "editor_titel": "Doğrudan tarayıcıda matematiksel animasyonlar",
        "editor_p": "Manim’in tarayıcıda çalışan bir geliştirmesi: nesneleri ve işlemleri bir araya getirin, oynatın ve resim ya da "
                    "video olarak dışa aktarın. Kurulum yok, ayarlanacak bir şey yok.",
        "editor_li1": "Fonksiyonlar, 3B yüzeyler, toplamlar ve çarpımlar, konvolüsyonlar",
        "editor_li2": "Salt bir grafik yerine adım adım koreografi", "editor_li3": "Resim ya da akıcı video olarak dışa aktarma",
        "video_label": "Animasyon: Fourier serisi kare dalgayı terim terim oluşturur; harmonikler ve genlik spektrumuyla",
        "video_cap": "Kare dalganın Fourier serisi, terim terim", "im_editor": "Editörde aç →",
        "mod_eyebrow": "Modüller", "mod_h2": "Dersler ve konular",
        "mod_p": "Tüm modüllere genel bakış: konularını açmak için bir modüle tıklayın ya da doğrudan arayın — modül, konu veya makale "
                 "metnindeki bir kavram.",
        "suche_label": "Bilgide ara", "suche_ph": "Modül, konu veya kavram arayın — kelime parçaları da olur (ör. “bölücü”)",
        "laedt": "Genel bakış yükleniyor …", "zum_wissen": "Bilgi alanına git →", "ganzer_bereich": "Bilgi alanının tamamını aç →",
        "how_eyebrow": "Nasıl işler", "how_h2": "Kavramdan berraklığa",
        "how1_h": "Önce resim", "how1_p": "Her konu somut başlar — formüllerden önce bir benzetme ve büyük resimle.",
        "how2_h": "Sonra fizik", "how2_p": "Özenle türetilir, her zaman “neden” sorusuyla: etkiyi hangi mekanizma oluşturur.",
        "how3_h": "Kendiniz oluşturun",
        "how3_p": "Animasyonlar editörde oluşturulur — onları açabilir, değiştirebilir ve kendiniz deneyebilirsiniz.",
        "videos_eyebrow": "yakında", "videos_h2": "Açıklayıcı videolar",
        "videos_p": "Tek tek konular hakkında kısa, animasyonlu videolar — editörle yapılır. Yakında.",
        "stats_label": "Kullanım sayıları", "stat_site": "Sayfa görüntüleme", "stat_editor": "Editör açıldı",
        "fuss": "EtUndSo.de · Elektrik mühendisliği için açıklamalar ve araçlar — ve daha fazlası.",
        "impressum": "Künye", "datenschutz": "Gizlilik", "recht_de": "Yasal sayfalar Almancadır.",
        "js": {"artikel": "{n} makale", "nichts": "“{q}” için sonuç bulunamadı.", "fehler": "Genel bakış yüklenemedi.",
               "zum_wissen": "Bilgi alanına git →", "weiterlesen": "Okumaya devam et", "volltext": "Tam metinde aranıyor …",
               "locale": "tr-TR"},
    },
}

_I18N_EL = re.compile(r'(<(\w+)\b[^>]*?\sdata-i18n="([\w-]+)"[^>]*>)(.*?)(</\2>)', re.S)
_I18N_ATTR = re.compile(r'<[^>]*?\sdata-i18n-attr="([^"]+)"[^>]*>', re.S)
_SPRACHWAHL = re.compile(r"<!-- sprachwahl-(top|art) -->.*?<!-- /sprachwahl-\1 -->", re.S)

def _attr_setzen(tag, name, wert):
    """Attribut name im Start-Tag tag auf wert setzen (vorhanden: ersetzen, sonst vor dem Ende anfügen)."""
    w = html.escape(wert, quote=True)
    m = re.search(r'\s%s="[^"]*"' % re.escape(name), tag)
    if m:
        return tag[:m.start()] + f' {name}="{w}"' + tag[m.end():]
    ende = len(tag) - (2 if tag.endswith("/>") else 1)
    return tag[:ende] + f' {name}="{w}"' + tag[ende:]

def startseite_html(vorlage, l):
    """Startseite der Sprache l aus der deutschen Vorlage (web/index.html)."""
    texte, fehlt = STARTSEITE_TEXTE[l], set()
    LANG_NOW[0] = l
    def el(m):
        key = m.group(3)
        if key == "nur_de":                            # Module nur auf Deutsch: Zeile wie in der Übersicht, sonst leer
            zeile = _nur_deutsch(TREES.get(l, []))
            if not zeile:
                return m.group(0)
            inhalt = zeile[zeile.index(">") + 1:zeile.rindex("</p>")]
            return m.group(1).replace(" hidden", "", 1) + inhalt + m.group(5)
        if key not in texte:
            fehlt.add(key)
            return m.group(0)
        return m.group(1) + texte[key] + m.group(5)
    t = _I18N_EL.sub(el, vorlage)
    def attr(m):
        tag = m.group(0)
        for paar in m.group(1).split(";"):
            name, _, key = paar.partition(":")
            if key in texte:
                tag = _attr_setzen(tag, name.strip(), texte[key])
            else:
                fehlt.add(key)
        return tag
    t = _I18N_ATTR.sub(attr, t)
    t = re.sub(r'<html lang="de">', f'<html lang="{l}">', t, count=1)
    ziele = {x: "/" if x == "de" else f"/{x}/" for x in LANGS}
    t = _SPRACHWAHL.sub(lambda m: f"<!-- sprachwahl-{m.group(1)} -->" + lang_switch({"ziele": ziele}, m.group(1))
                        + f"<!-- /sprachwahl-{m.group(1)} -->", t)
    t = t.replace('href="/wissen/"', f'href="/wissen/{l}/"')
    for b in ("lernen", "aufgaben"):                # W4b: Bereiche Lernkarten und Aufgaben
        t = t.replace(f'href="/{b}/"', f'href="/{b}/{l}/"')
    def bild(m):
        rel = m.group(1)
        return f'src="/abbildungen/{l}/{rel}"' if (ABB_DIR / l / rel).exists() else m.group(0)
    t = re.sub(r'src="/abbildungen/de/([^"]+)"', bild, t)
    js = re.search(r'(<script type="application/json" id="seite-text">)(.*?)(</script>)', t, re.S)
    if js:
        d = json.loads(js.group(2))
        d.update(texte.get("js", {}))
        t = t[:js.start(2)] + json.dumps(d, ensure_ascii=False) + t[js.end(2):]
    LANG_NOW[0] = "de"
    return t, fehlt

def startseiten_schreiben():
    """web/<l>/index.html für alle Sprachen außer Deutsch; schreibt nur bei geänderter Seite (Datum „Letztes Update“)."""
    pfad = ROOT / "web" / "index.html"
    if not pfad.exists():
        return 0
    vorlage = pfad.read_text(encoding="utf-8")
    n = 0
    for l in LANGS:
        if l == "de" or l not in STARTSEITE_TEXTE:
            continue
        t, fehlt = startseite_html(vorlage, l)
        if fehlt:
            print(f"  Startseite {l}: ohne Übersetzung (deutsch gelassen): {', '.join(sorted(fehlt))}")
        ziel = ROOT / "web" / l / "index.html"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        if not ziel.exists() or ziel.read_text(encoding="utf-8") != t:
            ziel.write_text(t, encoding="utf-8")
        n += 1
    return n

# --------------------------------------------------------- shared CSS / JS ----
WISSEN_CSS = r"""
/* Vorlage „Grüne Leiste“ (User 2026-11-04, Variante B des Design-Tests): nur Grün und Orange plus Neutraltöne,
   kein Lila, kein Rot; reinweißer Grund; dunkelgrüne Leiste, dunkelgrüne Überschriften, Abschnitte als weiße Karten.
   Tag Standard, Nacht via data-theme=dark (folgt dem Editor-Theme); nachts helle Rahmen um alle Kästen.
   Alle Textfarben mindestens 4,5 : 1 auf Karte und Grund. --accent2 = Überschriftfarbe (früher Lila). */
:root{ --bg:#ffffff; --panel:#ffffff; --ink:#16191a; --muted:#5b6360; --border:#e6e8e6; --soft:#f6f7f6;
  --accent:#15633a; --accent2:#1b7f4a; --accent3:#c2410c; --on-accent:#ffffff; --aufg:#15633a; --rahmen:var(--border);
  --bar:#123d29; --bar-ink:#eaf3ec; --bar-rand:#1f5a3d; --bar-soft:#1a4d35; --bar-hl:#ff9650; --radius:14px;
  --fdisp:"Segoe UI",system-ui,-apple-system,Roboto,sans-serif; --fbody:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --fmono:ui-monospace,"Cascadia Code",Consolas,monospace; }
:root[data-theme="dark"]{ --bg:#0e1110; --panel:#141816; --ink:#eef1ef; --muted:#a3aca6; --border:#262c29; --soft:#181d1a;
  --accent:#6ad19b; --accent2:#8fdcb2; --accent3:#ff9650; --on-accent:#0d1f15; --aufg:#1d5c3b; --rahmen:rgba(255,255,255,.32);
  --bar:#0b2a1c; --bar-ink:#dcebe1; --bar-rand:#174630; --bar-soft:#123a27; }
/* Formelfarben (\textcolor der Build-Färbung) nachts in den hellen Varianten, die dunklen wären kaum zu lesen.
   KaTeX setzt die Farbe per Skript, der Browser schreibt sie dann als rgb(…) ins style-Attribut.
   Linke Seite grün (#1b7f4a; bis 04.11. abends #123d29, zu dunkel), Relation grün, rechte Seite orange; #3f1a78 = Lila aus Artikeln vor dem 04.11.2026. */
:root[data-theme="dark"] .katex [style*="rgb(27, 127, 74)"],:root[data-theme="dark"] .katex [style*="#1b7f4a"]{color:var(--accent2)!important;}
.katex [style*="rgb(63, 26, 120)"],.katex [style*="#3f1a78"]{color:var(--accent2)!important;}
:root[data-theme="dark"] .katex [style*="rgb(21, 99, 58)"],:root[data-theme="dark"] .katex [style*="#15633a"]{color:var(--accent)!important;}
:root[data-theme="dark"] .katex [style*="rgb(194, 65, 12)"],:root[data-theme="dark"] .katex [style*="#c2410c"]{color:var(--accent3)!important;}
*{box-sizing:border-box;} html{scroll-behavior:smooth;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--fbody);line-height:1.68;-webkit-font-smoothing:antialiased;}
a{color:var(--accent);text-decoration:none;} a:hover{text-decoration:underline;}
kbd{font-family:var(--fmono);font-size:.82em;background:var(--soft);border:1px solid var(--border);border-radius:5px;padding:1px 5px;}
.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:14px;padding:11px 18px;background:var(--bar);border-bottom:1px solid var(--bar-rand);}
.brand{font-family:var(--fdisp);font-weight:800;font-size:19px;letter-spacing:-.02em;color:#ff9650;}   /* Logo: „Et“ orange wie „Editor öffnen“, „So“ rot (Wunsch des Users 09.11.2026) */
.brand span{color:var(--bar-ink);} .brand span.so{color:#ff4d4d;}
.topbar .searchBtn{margin-left:auto;display:flex;align-items:center;gap:8px;background:var(--bar-soft);border:1px solid var(--bar-rand);color:var(--bar-ink);
  border-radius:10px;padding:8px 13px;font:inherit;font-size:14px;cursor:pointer;}
.topbar .searchBtn:hover{border-color:var(--bar-hl);}
.topbar kbd{background:transparent;border-color:var(--bar-rand);color:var(--bar-ink);}
.topbar .editorlink{font-weight:600;color:var(--bar-ink);} .topbar .editorlink:hover{color:var(--bar-hl);}
.topbar .iconBtn,.topbar .panelBtn,.topbar .navBtn{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;background:var(--bar-soft);border:1px solid var(--bar-rand);color:var(--bar-ink);border-radius:10px;cursor:pointer;}
.topbar .iconBtn:hover{border-color:var(--bar-hl);}
.topbar .panelBtn:hover{background:color-mix(in srgb,var(--bar-hl) 18%,var(--bar-soft));}   /* Hover nur über den Hintergrund: der Rand zeigt den Zustand */
.topbar .panelBtn.is-open{color:var(--bar-hl);border-color:var(--bar-hl);}   /* Panel offen = orange, zu = Grundfarbe */
.topbar .panelCenter{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:8px;}  /* Einklapp-Knopf und Ansicht mittig in der Leiste */
/* Ansicht Ausführlich | Kurz | Formeln (W4a, an der Stelle der früheren Pfeile): breit Segmentschalter, schmal Auswahl */
.topbar .ansicht{display:inline-flex;align-items:stretch;height:36px;padding:2px;border:1px solid var(--bar-rand);border-radius:999px;background:var(--bar-soft);}
.topbar .ans-b{border:0;background:transparent;color:var(--bar-ink);font:inherit;font-size:13.5px;font-weight:600;padding:0 13px;border-radius:999px;cursor:pointer;white-space:nowrap;}
.topbar .ans-b:hover{color:var(--bar-hl);}
.topbar .ans-b[aria-pressed="true"]{background:var(--bar-hl);color:#14301f;}
.topbar .ans-b:focus-visible,.topbar .ans-sel:focus-visible{outline:2px solid var(--bar-hl);outline-offset:2px;}
.topbar .ans-sel{height:36px;max-width:118px;padding:0 26px 0 12px;border:1px solid var(--bar-hl);border-radius:999px;background-color:var(--bar-soft);color:var(--bar-ink);
  font:inherit;font-size:13.5px;font-weight:600;cursor:pointer;appearance:none;-webkit-appearance:none;text-overflow:ellipsis;
  background-image:linear-gradient(45deg,transparent 50%,var(--bar-hl) 50%),linear-gradient(135deg,var(--bar-hl) 50%,transparent 50%);
  background-position:calc(100% - 15px) 52%,calc(100% - 10px) 52%;background-size:5px 5px,5px 5px;background-repeat:no-repeat;}
.topbar .ans-sel option{color:#16191a;background:#fff;}
.topbar .ansicht[hidden],.topbar .ans-sel[hidden]{display:none!important;}
@media(min-width:821px){ .topbar .ans-sel{display:none!important;} }
@media(max-width:820px){ .topbar .ansicht{display:none!important;} }
.apill{display:inline-block;margin-left:6px;padding:0 8px;border:1px solid var(--border);border-radius:999px;font-size:11.5px;font-weight:600;color:var(--muted);line-height:1.6;}
.apill-mensch{color:var(--accent3);border-color:var(--accent3);}
/* Fokusmodus: Themenbaum (links) bzw. Gliederung (rechts) einklappen; Mittelbereich bleibt gleich breit (zentriert) */
/* hide-left: EINE Spalte (nicht 0+1fr) - sonst rutscht der einzige verbleibende Grid-Child (main) in die
   0-breite erste Spalte, der Text wird links gequetscht und die Gliederung überlappt ihn. */
.layout.hide-left{grid-template-columns:260px minmax(0,1fr);} .layout.hide-left>.side{display:none;} .layout.hide-left>main{grid-column:2;}  /* Baum zu, aber Textblock bleibt an gleicher Position (main bleibt in Spalte 2) */
.layout.hide-right .toc{display:none;}  /* Gliederung aus, aber die Spalte bleibt -> Artikel-Block verschiebt sich nicht */
.layout{display:grid;grid-template-columns:260px minmax(0,1fr);gap:0;max-width:1180px;margin:0 auto;}
.side{position:sticky;top:53px;align-self:start;max-height:calc(100vh - 53px);overflow:auto;padding:18px 10px 40px 18px;border-right:1px solid var(--border);font-size:14.5px;}
.side-home{display:block;font-weight:700;color:var(--ink);margin-bottom:10px;}
.side details{margin:2px 0;} .side summary{cursor:pointer;font-weight:600;padding:4px 6px;border-radius:7px;list-style:none;}
.side summary::-webkit-details-marker{display:none;}
.side summary::before{content:"▸";color:var(--muted);display:inline-block;width:1em;transition:transform .15s;}
.side details[open]>summary::before{transform:rotate(90deg);}
.side details details{margin-left:11px;}                 /* jede tiefere Ebene etwas eingerückt */
.side .lvl0>summary{font-weight:700;color:var(--ink);}  /* Fach/Studiengang: schwarz */
.side .lvl1>summary{font-weight:600;color:var(--accent3);}  /* Semester: orange */
.side .lvl2>summary,.side .lvl3>summary,.side .lvl4>summary{font-weight:500;}
.side .lvl2>summary{color:var(--accent);}                 /* Modul: grün */
.side ul{list-style:none;margin:0 0 4px;padding-left:22px;} .side li{margin:1px 0;}
.side li a{display:block;color:var(--ink);padding:3px 7px;border-radius:7px;}   /* Unterthemen/Themen: schwarz (im Dunkelmodus hell) */
/* kleiner Punkt vor jedem Unterthema, damit man sieht, wo ein Titel endet und der nächste beginnt (User 2026-11-04);
   Folgezeilen langer Titel rücken unter den Text ein, nicht unter den Punkt */
/* absolut gesetzt statt Flexbox: Flex würde Titel mit Formel (KaTeX) in einzelne Stücke zerreißen */
.side li a{position:relative;padding-left:20px;}
.side li a::before{content:"";position:absolute;left:8px;top:calc(3px + .84em - 2.5px);width:5px;height:5px;border-radius:50%;background:currentColor;opacity:.5;}
.side li a.active::before{opacity:.9;}
.side li a:hover{color:var(--ink);background:var(--soft);text-decoration:none;}
.side li a.active{color:var(--on-accent);background:var(--accent);font-weight:600;}
.article{min-width:0;padding:26px 30px 70px;display:grid;grid-template-columns:minmax(0,1fr) 210px;gap:34px;align-items:start;}
.article>article{min-width:0;width:100%;max-width:72ch;margin-inline:auto;}   /* zentriert -> bleibt beim Einklappen der Panels gleich breit; width:100%: sonst zieht die breiteste Formel den Artikel (auto-Ränder = fit-content) über die Spalte hinaus -> Text läuft auf Handy/Tablet rechts raus */
.crumbs{font-size:13px;color:var(--muted);margin-bottom:10px;} .crumbs a{color:var(--muted);}
.article h1{font-family:var(--fdisp);font-size:clamp(26px,4vw,38px);line-height:1.1;letter-spacing:-.02em;margin:.1em 0 .3em;text-wrap:balance;color:var(--accent2);}  /* Titel: lila */
.article h2{font-family:var(--fdisp);font-size:24px;margin:2.5em 0 .5em;letter-spacing:-.01em;scroll-margin-top:66px;color:var(--accent2);}   /* Zwischenüberschrift: lila, mehr Luft davor */
.article h3{font-family:var(--fdisp);font-size:19px;margin:1.9em 0 .7em;scroll-margin-top:66px;color:var(--accent2);}
.article p,.article li{font-size:17.5px;} .article p{margin:0 0 1.35em;} .article li{margin:.3em 0;} .article ul,.article ol{margin:0 0 1.35em;} .article .lede{font-size:18.5px;color:var(--muted);margin:.2em 0 1.3em;}
/* --- Farbkategorien (je eine Zeile): wichtige Wörter = orange, Namen = grün, Schritt-Marken = lila --- */
.article strong{color:var(--accent3);}             /* wichtige Ausdrücke/Wörter */
.article strong.nm{color:var(--accent);}           /* Namen (Größen, Begriffe, Einheiten) */
.article strong.step{color:var(--accent);}         /* „Schritt N" */
/* Formeln/Gleichungen hervorheben: eigene Box mit blauer Border, deutlich größer */
.article .katex-display{font-size:1.3em;margin:1.3em 0;overflow-x:auto;overflow-y:hidden;}   /* Formel auf eigener Zeile, NICHT geboxt */
.article .fbox{margin:1.5em 0;padding:9px 18px 14px;border:1.5px solid var(--accent);border-radius:12px;background:color-mix(in srgb,var(--accent) 6%,var(--panel));}  /* nur die wichtigsten Formeln */
.article .fbox-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:2px;}
.article .fbox-t{font-family:var(--fdisp);font-weight:700;color:var(--accent);font-size:12.5px;text-transform:uppercase;letter-spacing:.04em;}
.article .fbox-n{color:var(--muted);font-variant-numeric:tabular-nums;font-size:13px;}
.article .fbox .katex-display{margin:.15em 0;padding:0;border:none;background:none;}
.article .katex{font-size:1.12em;}                  /* Inline-Mathe – gut lesbar, auch mobil */
.nobr{white-space:nowrap;}                           /* kurze Formel + anliegendes Satzzeichen: kein Umbruch dazwischen */
/* Mehrteilige Formelzeilen (im Quelltext durch \qquad getrennt): Teile nebeneinander, bei Platzmangel untereinander */
.mrow{display:flex;flex-wrap:wrap;justify-content:center;align-items:baseline;column-gap:2.6em;row-gap:0;margin:1.3em 0;}
.mcell{min-width:0;max-width:100%;}
.article .mrow .katex-display{margin:.2em 0;}
.article .fbox .mrow{margin:.3em 0;}
.article img{max-width:100%;border-radius:10px;} .article code{font-family:var(--fmono);font-size:.9em;background:var(--soft);padding:1px 5px;border-radius:5px;}
.article pre{background:var(--soft);border:1px solid var(--border);border-radius:10px;padding:14px 16px;overflow:auto;} .article pre code{background:none;padding:0;}
/* Code-Blöcke der Zusatzreihen: Kopfzeile (Titel links, Sprache rechts), Farben aus den Pygments-Klassen, Tag und Nacht */
.code-block{margin:1.2em 0;} .code-block pre{margin:0;}
.code-kopf{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding:5px 14px;border:1px solid var(--border);border-bottom:none;
  border-radius:10px 10px 0 0;background:var(--soft);font-family:var(--fmono);font-size:13px;}
.code-kopf+pre{border-top-left-radius:0;border-top-right-radius:0;}
.code-t{color:var(--ink);overflow-wrap:anywhere;}
.code-l{margin-left:auto;color:var(--muted);font-family:var(--fdisp);font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap;}
.article pre.hl{font-size:14px;line-height:1.5;tab-size:4;} .article pre.hl code{font-size:1em;}
/* nur Grün, Orange und Grautöne: Schlüsselwörter grün, Namen schwarz, Zeichenketten braun-orange, Zahlen orange */
.hl .k,.hl .kc,.hl .kd,.hl .kn,.hl .kp,.hl .kr,.hl .ow,.hl .cp{color:#15633a;font-weight:600;}
.hl .kt,.hl .nb,.hl .bp,.hl .nf,.hl .fm,.hl .nc,.hl .nn{color:#16191a;}
.hl .nf,.hl .fm,.hl .nc{font-weight:600;}
.hl .s,.hl .s1,.hl .s2,.hl .sa,.hl .sb,.hl .sc,.hl .sd,.hl .se,.hl .sh,.hl .si,.hl .sx,.hl .sr,.hl .ss,.hl .dl{color:#9a3412;}
.hl .c,.hl .c1,.hl .cm,.hl .cs,.hl .ch,.hl .cpf{color:#5f6662;font-style:italic;}
.hl .m,.hl .mi,.hl .mf,.hl .mh,.hl .mo,.hl .mb,.hl .il{color:#b33a0b;}
.hl .nv,.hl .vc,.hl .vg,.hl .vi,.hl .nd,.hl .na{color:#3d4542;}
.hl .gp{color:#b33a0b;font-weight:700;user-select:none;}           /* Prompt: beim Kopieren nicht mit markieren */
.hl .go{color:var(--muted);} .hl .err{color:inherit;border:none;background:none;}
:root[data-theme="dark"] .hl .k,:root[data-theme="dark"] .hl .kc,:root[data-theme="dark"] .hl .kd,:root[data-theme="dark"] .hl .kn,
:root[data-theme="dark"] .hl .kp,:root[data-theme="dark"] .hl .kr,:root[data-theme="dark"] .hl .ow,:root[data-theme="dark"] .hl .cp{color:#6ad19b;}
:root[data-theme="dark"] .hl .kt,:root[data-theme="dark"] .hl .nb,:root[data-theme="dark"] .hl .bp,:root[data-theme="dark"] .hl .nf,
:root[data-theme="dark"] .hl .fm,:root[data-theme="dark"] .hl .nc,:root[data-theme="dark"] .hl .nn{color:#eef1ef;}
:root[data-theme="dark"] .hl [class^="s"],:root[data-theme="dark"] .hl .dl{color:#ffb27a;}
:root[data-theme="dark"] .hl [class^="c"]:not(.cp){color:#98a29b;}
:root[data-theme="dark"] .hl [class^="m"],:root[data-theme="dark"] .hl .il,:root[data-theme="dark"] .hl .gp{color:#ff9650;}
:root[data-theme="dark"] .hl .nv,:root[data-theme="dark"] .hl .vc,:root[data-theme="dark"] .hl .vg,:root[data-theme="dark"] .hl .vi,
:root[data-theme="dark"] .hl .nd,:root[data-theme="dark"] .hl .na{color:#c9d1cc;}
/* Achtung-Kasten (Recht, Datenverlust, Sicherheit): immer offen, orange */
.callout.cx-warnung{border-left:4px solid var(--accent3);background:color-mix(in srgb,var(--accent3) 7%,var(--panel));}
.callout.cx-warnung .callout-h{color:var(--accent3);}
.article blockquote{margin:1em 0;padding:2px 16px;border-left:3px solid var(--accent);color:var(--muted);}
.table-wrap{overflow-x:auto;margin:1.2em 0;}
.md-table{border-collapse:collapse;width:100%;font-size:15.5px;}
.md-table th,.md-table td{padding:8px 12px;border:1px solid var(--border);text-align:left;vertical-align:top;}
.md-table thead th{background:var(--soft);font-family:var(--fdisp);color:var(--accent);font-weight:700;}
.md-table tbody tr:nth-child(even){background:color-mix(in srgb,var(--soft) 55%,transparent);}
.callout{margin:1.7em 0;padding:16px 18px;border:1px solid var(--border);border-radius:12px;background:var(--soft);}
.callout-h{font-weight:700;font-family:var(--fdisp);margin-bottom:4px;color:var(--accent);}   /* Box-Überschrift: grün */
.callout.cx-konzept{border-left:4px solid var(--accent);} .callout.cx-kern{border-left:4px solid var(--accent);background:color-mix(in srgb,var(--accent) 6%,var(--panel));}
.callout.cx-kern .callout-h{color:var(--accent);}  /* Kernbox: grün wie ihr Rand */
.callout.cx-merke{border-left:4px solid var(--accent3);}
.callout.cx-satz,.callout.cx-lemma,.callout.cx-definition{border-left:4px solid var(--accent);background:color-mix(in srgb,var(--accent) 6%,var(--panel));}
/* Abbildungs-Platzhalter: gestrichelte Box mit Beschreibung, bis echte Editor-Grafik eingesetzt wird */
.callout.cx-grafik{border:1.5px dashed var(--accent);background:color-mix(in srgb,var(--accent) 4%,var(--panel));color:var(--muted);}
.callout.cx-grafik .callout-h{color:var(--accent);text-transform:uppercase;letter-spacing:.04em;font-size:12.5px;}
.callout.cx-grafik p{font-size:15px;margin:.2em 0;}
.callout.cx-grafik .gr-szene{font-size:12px;color:var(--muted);margin-top:6px;font-family:ui-monospace,Consolas,monospace;overflow-wrap:anywhere;}
/* Echte Abbildung (SVG) mit Bildunterschrift – ersetzt nach und nach die cx-grafik-Platzhalter */
.article figure.fig{margin:1.8em 0;text-align:center;}
.article figure.fig svg{width:min(560px,100%);height:auto;}
.article figure.fig figcaption{margin-top:9px;font-size:14px;color:var(--muted);line-height:1.5;max-width:52ch;margin-inline:auto;}
.article figure.fig img{width:min(680px,100%);height:auto;border-radius:8px;background:#fff;}   /* berechnete Abbildung (SVG, weißer Grund) */
/* Editor-Abbildung (:::abbildung): das SVG in seiner natürlichen Größe (Beschriftung 13–15 px), höchstens so breit wie
   die Spalte; darunter die nummerierte Bildunterschrift und der Link in den Editor. Kasten wie die übrigen Boxen. */
.article figure.abb{margin:1.7em 0;padding:10px 10px 9px;border:1px solid var(--border);border-radius:12px;background:var(--soft);}
.article figure.abb img{display:block;margin:0 auto;max-width:100%;height:auto;border-radius:8px;background:#fff;}
.article figure.abb figcaption{margin:9px 4px 0;font-size:14.5px;line-height:1.5;color:var(--muted);}
.article figure.abb .abb-n{font-family:var(--fdisp);font-weight:700;color:var(--accent);margin-right:4px;}
/* Knopf unter dem Bild: öffnet genau die Szene, aus der das Bild exportiert wurde (web/szenen/<name>.json) */
.article figure.abb .abb-knopf{display:flex;justify-content:flex-end;margin:8px 2px 0;}
.article figure.abb .abb-edit{display:inline-flex;align-items:center;gap:6px;padding:5px 11px;border:1px solid var(--accent);border-radius:8px;
  background:var(--panel);color:var(--accent);font-size:13px;font-weight:600;line-height:1.3;white-space:nowrap;}
.article figure.abb .abb-edit:hover{text-decoration:none;background:color-mix(in srgb,var(--accent) 10%,var(--panel));}
/* Animierte Abbildung (data-anim, wissen.js): das bewegte SVG an der Stelle des Bilds, darunter die Spielerleiste
   (Start/Stopp gefüllt grün, Neustart, Schritt zurück/vor, Zeitleiste mit orangen Sprungmarken, Zeit). */
.article figure.abb svg.abb-anim{display:block;margin:0 auto;max-width:100%;height:auto;border-radius:8px;background:#fff;}
.abb-spieler{display:flex;align-items:center;gap:6px;margin:8px 2px 0;}
.abb-spieler button{flex:none;display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;padding:0;
  border:1px solid var(--accent);border-radius:8px;background:var(--panel);color:var(--accent);cursor:pointer;}
.abb-spieler button:hover{background:color-mix(in srgb,var(--accent) 12%,var(--panel));}
.abb-spieler button.as-play{background:var(--accent);color:var(--on-accent);}
.abb-spieler button.as-play:hover{background:color-mix(in srgb,var(--accent) 85%,var(--ink));}
.abb-spieler button:focus-visible,.abb-spieler input:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.abb-spieler svg{width:16px;height:16px;fill:currentColor;}
.abb-spieler .as-leiste{position:relative;flex:1;min-width:64px;height:32px;display:flex;align-items:center;}
.abb-spieler input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:32px;margin:0;background:transparent;cursor:pointer;}
.abb-spieler input[type=range]::-webkit-slider-runnable-track{height:4px;border-radius:2px;
  background:linear-gradient(to right,var(--accent) var(--as-p,0%),color-mix(in srgb,var(--muted) 35%,transparent) var(--as-p,0%));}
.abb-spieler input[type=range]::-moz-range-track{height:4px;border-radius:2px;background:color-mix(in srgb,var(--muted) 35%,transparent);}
.abb-spieler input[type=range]::-moz-range-progress{height:4px;border-radius:2px;background:var(--accent);}
.abb-spieler input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;margin-top:-5px;border-radius:50%;
  background:var(--accent);border:2px solid var(--panel);box-shadow:0 0 0 1px var(--accent);}
.abb-spieler input[type=range]::-moz-range-thumb{width:10px;height:10px;border-radius:50%;background:var(--accent);border:2px solid var(--panel);
  box-shadow:0 0 0 1px var(--accent);}
.abb-spieler .as-marke{position:absolute;top:50%;width:2px;height:10px;margin:-5px 0 0 -1px;border-radius:1px;background:var(--accent3);
  pointer-events:none;}
.abb-spieler .as-zeit{flex:none;min-width:6.2em;text-align:right;font-size:12.5px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap;}
@media(max-width:480px){ .abb-spieler{gap:5px;} .abb-spieler .as-zeit{display:none;} .abb-spieler button{width:30px;height:30px;} }
/* Fassung wählen: kompakt | ausführlich, jeweils mit Lesezeit */
.fassung{display:inline-flex;margin:.1em 0 1.2em;border:1px solid var(--border);border-radius:10px;overflow:hidden;background:var(--soft);}
.fassung .f-btn{display:flex;align-items:baseline;gap:8px;padding:7px 15px;color:var(--muted);font-weight:600;font-size:14.5px;}
.fassung .f-btn span{font-weight:500;font-size:12.5px;}
.fassung .f-btn.on{background:var(--panel);color:var(--ink);box-shadow:inset 0 -2px 0 var(--accent);}
.fassung .f-btn:hover{text-decoration:none;color:var(--ink);}
/* Frage-Kasten: die Frage ist sichtbar, die Antwort klappt auf */
details.frage{margin:1.1em 0;border:1px solid var(--border);border-radius:10px;background:var(--panel);}
details.frage>summary{cursor:pointer;padding:10px 14px;list-style:none;font-weight:600;line-height:1.45;}
details.frage>summary::-webkit-details-marker{display:none;}
details.frage>summary::before{content:"▸";display:inline-block;margin-right:9px;color:var(--accent);transition:transform .15s;}
details.frage[open]>summary::before{transform:rotate(90deg);}
details.frage .fr-k{font-family:var(--fdisp);font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent);margin-right:9px;}
.fr-body{padding:0 16px 8px;border-top:1px solid var(--border);}
.fr-body>p:first-child{margin-top:12px;}
/* Hintergrund-Kasten: Warum und Woher zum Haupttext, zugeklappt, neutral grau mit grüner Linie */
details.hintergrund{margin:1.1em 0;border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:10px;
  background:var(--soft);}
details.hintergrund>summary{cursor:pointer;padding:10px 14px;list-style:none;font-weight:600;line-height:1.45;}
details.hintergrund>summary::-webkit-details-marker{display:none;}
details.hintergrund>summary::before{content:"▸";display:inline-block;margin-right:9px;color:var(--accent);transition:transform .15s;}
details.hintergrund[open]>summary::before{transform:rotate(90deg);}
details.hintergrund .hg-k{font-family:var(--fdisp);font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent);margin-right:9px;}
.hg-body{padding:0 16px 8px;border-top:1px solid var(--border);}
.hg-body>p:first-child{margin-top:12px;}
.callout.cx-fehlvorstellung{border-left:4px solid var(--accent3);} .callout.cx-fehlvorstellung .callout-h{color:var(--accent3);}
.callout.cx-analogie{border-left:4px solid var(--muted);} .callout.cx-analogie .callout-h{color:var(--muted);}
.callout.cx-vertiefung{border-left:4px solid var(--border);} .callout.cx-vertiefung .callout-h{color:var(--muted);}
/* Abschnitte als Karten: klar getrennt, in Stücken lernen */
.article .sect{border:1px solid var(--border);border-radius:14px;background:var(--panel);padding:2px 22px 18px;margin:0 0 18px;}
.article .sect>h2{margin:.7em 0 .9em;} .article .sect>h2:first-child{margin-top:.5em;}  /* Text beginnt klar eine Zeile unter der Überschrift */
/* „Das Wichtigste" als klare Stichpunkte statt Textblock */
.callout.cx-kern ul{margin:.2em 0 0;padding-left:1.2em;} .callout.cx-kern li{margin:.45em 0;}
.callout ul{padding-left:1.2em;margin:.4em 0;}
/* Nachbar-Artikel: zwei Spalten mit Themen-Stichpunkten (vorher | nächstes) */
.neighbors{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:30px 0 8px;}
.neighbors .nb{display:block;border:1px solid var(--border);border-radius:12px;padding:13px 16px;background:var(--panel);color:inherit;}
.neighbors .nb:hover{border-color:var(--accent);text-decoration:none;}
/* „Verwendet in“ unter Nachschlage-Artikeln (ML-Grundlagen): dezent, klein, grau */
.verwendet{margin:30px 0 4px;padding:10px 16px 11px;border:1px solid var(--border);border-radius:12px;background:var(--soft);color:var(--muted);}
.verwendet .vw-h{font-size:12.5px;font-weight:600;letter-spacing:.03em;margin-bottom:3px;}
.verwendet ul{margin:0;padding-left:18px;} .article .verwendet li{font-size:14.5px;margin:.2em 0;line-height:1.5;}
.verwendet .vw-zu{color:var(--muted);}
.article .idx-hinweis{font-size:15px;color:var(--muted);margin:.15em 0 .7em;max-width:70ch;}
.nb-dir{font-size:12px;color:var(--muted);font-weight:600;} .nb-dir.next{text-align:right;}
.nb-t{font-weight:700;color:var(--ink);margin:3px 0 8px;font-family:var(--fdisp);}
.nb ul{list-style:none;margin:0;padding:0;} .nb li{font-size:13.5px;color:var(--muted);margin:3px 0;padding-left:14px;position:relative;}
.nb li::before{content:"▸";position:absolute;left:0;top:1px;color:var(--accent);font-size:.8em;}
.nb.empty{border:none;background:none;}
.callout.cx-quiz{border-left:4px solid var(--accent3);background:color-mix(in srgb,var(--accent3) 5%,var(--panel));}
.callout.cx-quiz .callout-h{color:var(--accent3);}
details.quiz-item{margin:.5em 0;border:1px solid var(--border);border-radius:10px;background:var(--panel);}
details.quiz-item>summary{cursor:pointer;font-weight:600;padding:9px 12px;list-style:none;}
details.quiz-item>summary::-webkit-details-marker{display:none;}
details.quiz-item>summary:before{content:"▸";color:var(--accent);margin-right:8px;}
details.quiz-item[open]>summary:before{content:"▾";}
.quiz-n{display:inline-block;min-width:1.7em;color:var(--muted);font-variant-numeric:tabular-nums;}
.quiz-a{padding:2px 14px 12px 34px;border-top:1px solid var(--border);}
.quiz-a>p:first-child{margin-top:8px;}
/* Herleitung: ausklappbare Box direkt an der Formel */
details.herleitung{margin:1.1em 0;border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:10px;background:color-mix(in srgb,var(--accent) 4%,var(--panel));}
details.herleitung>summary{cursor:pointer;font-weight:700;font-family:var(--fdisp);color:var(--accent);padding:10px 14px;list-style:none;}
details.herleitung>summary::-webkit-details-marker{display:none;}
details.herleitung>summary::before{content:"▸";display:inline-block;margin-right:9px;transition:transform .15s;}
details.herleitung[open]>summary::before{transform:rotate(90deg);}
details.herleitung>summary:hover{text-decoration:underline;}
.hl-body{padding:0 16px 10px;border-top:1px solid var(--border);}
.hl-body>p:first-child{margin-top:12px;}
/* LTspice-Hinweis: nachbauen und messen, standardmaessig geschlossen */
.anker{display:block;height:0;scroll-margin-top:72px;}
.gl-zeile{display:flex;align-items:center;gap:10px;margin:1.1em 0;}
.gl-f{flex:1 1 auto;min-width:0;} .gl-f .katex-display{margin:0;} .gl-f .mrow{margin:0;}
.gl-nr{flex:none;display:flex;flex-direction:column;justify-content:space-around;align-self:stretch;font-size:15px;color:var(--muted);font-variant-numeric:tabular-nums;}
.zweck{margin:.4em 0 1.5em;padding:12px 16px;border-radius:10px;background:var(--soft);}
.zweck .zw-k{font-weight:700;font-family:var(--fdisp);}
.zweck p{display:inline;margin:0;} .zweck p+p{display:block;margin-top:.7em;}
.aufg{margin:1.5em 0;border:1px solid color-mix(in srgb,var(--aufg) 50%,var(--border));border-radius:12px;overflow:hidden;background:var(--panel);}
.aufg-h{padding:9px 16px;font-weight:700;font-family:var(--fdisp);font-size:16px;color:#fff;background:var(--aufg);}
.aufg-h .katex{color:#fff;}
.aufg-b{padding:13px 16px 12px;}
.aufg-b>p:last-of-type{margin-bottom:.7em;}
details.loesung{margin:.7em 0 .2em;border-top:1px dashed var(--border);padding-top:8px;}
details.loesung>summary{cursor:pointer;list-style:none;font-weight:600;color:var(--accent);}
details.loesung>summary::-webkit-details-marker{display:none;}
details.loesung>summary::before{content:"▸";display:inline-block;margin-right:9px;transition:transform .15s;}
details.loesung[open]>summary::before{transform:rotate(90deg);}
.lo-body{padding-top:9px;}
.callout.cx-zusatz{border-left:4px solid var(--muted);}
.callout.cx-zusatz .callout-h{color:var(--muted);}
.callout.cx-analogie{border-left:4px solid var(--muted);}
.callout.cx-analogie .callout-h{color:var(--muted);font-size:14.5px;}
.article ol.al{list-style:none;counter-reset:al;padding-left:2em;}
.article ol.al>li{counter-increment:al;position:relative;}
.article ol.al>li::before{content:"(" counter(al,lower-alpha) ")";position:absolute;left:-2em;font-weight:600;font-size:16px;line-height:1.75;}
.article ol.rm{list-style:none;counter-reset:rm;padding-left:2.3em;}
.article ol.rm>li{counter-increment:rm;position:relative;}
.article ol.rm>li::before{content:"(" counter(rm,lower-roman) ")";position:absolute;left:-2.3em;font-weight:600;font-size:16px;line-height:1.75;}
.article li>p{margin:0 0 .5em;} .article li>p:last-child{margin-bottom:0;}
/* Sprachmenü (User 2026-11-04: sechs Sprachen, ein Auswahlknopf): runder Knopf mit der aktuellen Sprache, darunter die
   Liste aller Sprachen in eigener Schreibweise; offen = orange wie die übrigen Knöpfe der Leiste. Ohne Übersetzung
   ausgegraut. Breit in der Kopfleiste, schmal (bis 900 px) unter dem Titel, wo vorher die Sprachknöpfe standen. */
.langs{position:relative;display:inline-flex;margin-left:10px;}
.langs .l-toggle{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 11px 0 14px;border-radius:999px;border:1px solid var(--border);
  background:var(--soft);color:var(--ink);font:inherit;font-size:13.5px;font-weight:700;letter-spacing:.03em;line-height:1;cursor:pointer;}
.langs .l-toggle:hover{border-color:var(--accent3);}
.langs .l-toggle[aria-expanded="true"]{border-color:var(--accent3);color:var(--accent3);}
.langs .l-pfeil{opacity:.85;transition:transform .15s;}
.langs .l-toggle[aria-expanded="true"] .l-pfeil{transform:rotate(180deg);}
.topbar .langs .l-toggle{background:var(--bar-soft);border-color:var(--bar-rand);color:var(--bar-ink);}
.topbar .langs .l-toggle:hover{border-color:var(--bar-hl);}
.topbar .langs .l-toggle[aria-expanded="true"]{border-color:var(--bar-hl);color:var(--bar-hl);}
.langs .l-toggle:focus-visible,.langs .l-item:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.topbar .langs .l-toggle:focus-visible{outline-color:var(--bar-hl);}
.langs .l-menu{position:absolute;top:calc(100% + 6px);left:0;z-index:40;min-width:180px;margin:0;padding:6px;list-style:none;background:var(--panel);
  border:1px solid var(--border);border-radius:12px;box-shadow:0 12px 32px rgba(10,20,15,.16),0 2px 6px rgba(10,20,15,.08);}
.langs .l-menu[hidden]{display:none;}
.langs .l-menu li{margin:0;padding:0;font-size:14.5px;line-height:1.3;}
.langs .l-item{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:8px 12px;border-radius:8px;color:var(--ink);
  font-weight:500;text-decoration:none;}
.langs a.l-item:hover,.langs a.l-item:focus{background:var(--soft);text-decoration:none;}
.langs .l-item.on{color:var(--accent3);font-weight:700;background:color-mix(in srgb,var(--accent3) 9%,var(--panel));}
.langs .l-item.off{color:var(--muted);opacity:.55;cursor:not-allowed;}
:root[data-theme="dark"] .langs .l-menu{border-color:var(--rahmen);box-shadow:0 12px 32px rgba(0,0,0,.55);}
html[lang="zh"] body{font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif;}
.langs-art{display:none;margin:0 0 12px;}
@media (max-width:900px){.langs-top{display:none;}.langs-art{display:inline-flex;}}
details.ltspice{margin:1.1em 0;border:1px solid var(--border);border-left:4px solid var(--accent3);border-radius:10px;background:color-mix(in srgb,var(--accent3) 5%,var(--panel));}
details.ltspice>summary{cursor:pointer;font-weight:600;padding:10px 14px;list-style:none;line-height:1.45;}
details.ltspice>summary::-webkit-details-marker{display:none;}
details.ltspice>summary::before{content:"▸";display:inline-block;margin-right:9px;color:var(--accent3);transition:transform .15s;}
details.ltspice[open]>summary::before{transform:rotate(90deg);}
details.ltspice .lt-k{font-family:var(--fdisp);font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent3);margin-right:9px;}
.lt-body{padding:0 16px 10px;border-top:1px solid var(--border);}
.lt-body>p:first-child{margin-top:12px;}
.prevnext{display:flex;justify-content:space-between;gap:14px;margin:36px 0 10px;flex-wrap:wrap;}
.pn{flex:1 1 200px;border:1px solid var(--border);border-radius:12px;padding:12px 15px;font-weight:600;background:var(--panel);}
.pn span{display:block;font-size:12px;color:var(--muted);font-weight:500;margin-bottom:2px;} .pn.next{text-align:right;}
.toc{position:sticky;top:66px;align-self:start;font-size:13.5px;border-left:1px solid var(--border);padding-left:16px;}
.toc-h{text-transform:uppercase;letter-spacing:.05em;font-size:11px;color:var(--muted);font-weight:700;margin-bottom:8px;}
.toc ul{list-style:none;margin:0;padding:0;} .toc li{margin:5px 0;} .toc a{color:var(--muted);} .toc a.active{color:var(--accent);font-weight:600;}
.field-block{margin:26px 0;} .field-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;}
.idx-node{margin:10px 0 10px 4px;padding-left:14px;border-left:2px solid var(--border);}
.idx-node h3{font-size:16px;margin:.4em 0 .3em;color:var(--ink);} .lvl-h{font-size:14.5px;margin:.5em 0 .2em;color:var(--accent3);font-weight:700;letter-spacing:.01em;}  /* Semester: orange */
.idx-node h3.idx-lvl2{color:var(--accent);}              /* Modul: grün (Oberthemen bleiben Standard-Ink/schwarz) */
.theme-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px;}
.theme-card h3{font-family:var(--fdisp);margin:0 0 6px;font-size:16px;} .theme-card ul{list-style:none;margin:0;padding:0;} .theme-card li{margin:4px 0;}
.theme-card a{color:var(--ink);} .theme-card a:hover{color:var(--accent);}   /* Unterthemen schwarz, Hover grün */
.field-block>h2{color:var(--accent2);}   /* Fach/Studiengang: lila (wie Sidebar lvl0) */
.empty{color:var(--muted);}
.wfoot{margin-top:40px;padding-top:18px;border-top:1px solid var(--border);color:var(--muted);font-size:13.5px;}
.searchOverlay{position:fixed;inset:0;z-index:50;background:rgba(10,14,22,.5);backdrop-filter:blur(2px);display:flex;justify-content:center;padding:10vh 16px 16px;}
.searchOverlay[hidden]{display:none;}              /* the `hidden` attribute must win over display:flex */
.searchBox{background:var(--panel);border:1px solid var(--border);border-radius:16px;width:min(680px,100%);max-height:78vh;display:flex;flex-direction:column;box-shadow:0 20px 60px rgba(0,0,0,.3);overflow:hidden;}
#searchInput{font:inherit;font-size:18px;padding:16px 18px;border:none;border-bottom:1px solid var(--border);background:none;color:var(--ink);outline:none;}
.searchResults{overflow:auto;} .searchResults a{display:block;padding:11px 18px;border-bottom:1px solid var(--border);color:var(--ink);}
.searchResults a:hover,.searchResults a.sel{background:var(--soft);text-decoration:none;}
.searchResults .r-crumb{font-size:12px;color:var(--muted);} .searchResults .r-title{font-weight:600;}
.searchResults .r-snip{font-size:13.5px;color:var(--muted);margin-top:2px;} .searchResults mark{background:color-mix(in srgb,var(--accent3) 55%,transparent);color:inherit;border-radius:3px;}
.searchHint{padding:10px 18px;font-size:12.5px;color:var(--muted);border-top:1px solid var(--border);}
.menuBtn{display:none;}
/* Inhaltsverzeichnis am Artikelanfang (ersetzt die früheren Einstiegs-Boxen Lede / „Zur Idee" / „Worum es geht") */
.arttoc{margin:.3em 0 2.2em;padding:16px 20px;background:var(--soft);border:1px solid var(--border);border-radius:12px;}
.arttoc-h{text-transform:uppercase;letter-spacing:.05em;font-size:12px;color:var(--muted);font-weight:700;margin-bottom:10px;}
.arttoc ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:2px 26px;}
.arttoc li{margin:0;}
.arttoc a{display:block;padding:5px 0;color:var(--ink);font-weight:500;}
.arttoc a::before{content:"→";color:var(--accent);margin-right:10px;font-weight:700;}  /* Pfeil = springt zur Stelle (kein Aufklapp-Dreieck) */
.arttoc a:hover{color:var(--accent);text-decoration:none;}
/* ---------- Beispiel-Kasten (::::beispiel): ausgearbeitetes Beispiel, zugeklappt; weiß mit oranger Kopfleiste (Orange = Praxis),
   so vom Hintergrund-Kasten (grau, grüne Linie links) und vom LTspice-Hinweis (orange Linie links, getönt) zu unterscheiden ---------- */
details.beispiel{margin:1.1em 0;border:1px solid var(--border);border-top:3px solid var(--accent3);border-radius:10px;background:var(--panel);}
details.beispiel>summary{cursor:pointer;padding:10px 14px;list-style:none;font-weight:600;line-height:1.45;}
details.beispiel>summary::-webkit-details-marker{display:none;}
details.beispiel>summary::before{content:"▸";display:inline-block;margin-right:9px;color:var(--accent3);transition:transform .15s;}
details.beispiel[open]>summary::before{transform:rotate(90deg);}
details.beispiel .bsp-k{font-family:var(--fdisp);font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent3);margin-right:9px;}
.bsp-body{padding:0 16px 10px;border-top:1px solid var(--border);}
.bsp-body>p:first-child{margin-top:12px;}
/* ---------- Vorwissen-Kasten (:::::vorwissen, „Was du dafür brauchst: …“): zugeklappt; weiß mit grüner Kopfleiste,
   so vom Beispiel (orange Kopfleiste) und vom Hintergrund (grau, grüne Linie links) zu unterscheiden ---------- */
details.vorwissen{margin:1.1em 0;border:1px solid var(--border);border-top:3px solid var(--accent);border-radius:10px;background:var(--panel);}
details.vorwissen>summary{cursor:pointer;padding:10px 14px;list-style:none;font-weight:600;line-height:1.45;}
details.vorwissen>summary::-webkit-details-marker{display:none;}
details.vorwissen>summary::before{content:"▸";display:inline-block;margin-right:9px;color:var(--accent);transition:transform .15s;}
details.vorwissen[open]>summary::before{transform:rotate(90deg);}
details.vorwissen .vo-k{font-family:var(--fdisp);font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent);margin-right:9px;}
.vo-body{padding:0 16px 10px;border-top:1px solid var(--border);}
.vo-body>p:first-child,.vo-body>.anker:first-child+p{margin-top:12px;}
.article figure.abb,.article details [id]{scroll-margin-top:72px;}   /* Sprung auf eine Abbildung (auch im Kasten): nicht unter der Kopfleiste */
/* ---------- Grüne Leiste, modern (Variante B, 04.11.2026) ---------- */
.article h1{font-weight:800;letter-spacing:-.03em;line-height:1.08;}
.article h2{font-weight:700;letter-spacing:-.022em;} .article h3{font-weight:700;letter-spacing:-.015em;}
.article p,.article li{line-height:1.72;}
.topbar .searchBtn,.topbar .iconBtn,.topbar .panelBtn,.topbar .navBtn,.topbar .l-toggle{border-radius:999px;}
.article .sect{border-radius:16px;box-shadow:0 1px 2px rgba(16,24,20,.04),0 4px 14px rgba(16,24,20,.04);}
.callout{border-radius:12px;}
.aufg{border-color:var(--border);border-radius:14px;}
.side li a.active{border-radius:8px;}   /* rechteckig mit leicht runden Ecken (User 2026-11-04: keine Ellipse) */
/* Nacht: Karten ohne Schatten, dafür helle Rahmen um alle Kästen (Wunsch des Users); farbige Randstreifen links bleiben */
:root[data-theme="dark"] .article .sect{box-shadow:none;}
:root[data-theme="dark"] :is(.article .sect,.callout,details.hintergrund,details.herleitung,details.frage,details.ltspice,details.quiz-item,
  .aufg,.article figure.abb,.arttoc,.zweck,.neighbors .nb,.pn,.theme-card,.fassung,.verwendet){
  border-top:1px solid var(--rahmen);border-right:1px solid var(--rahmen);border-bottom:1px solid var(--rahmen);}
:root[data-theme="dark"] :is(details.beispiel,details.vorwissen){border-right:1px solid var(--rahmen);border-bottom:1px solid var(--rahmen);}
:root[data-theme="dark"] :is(.article .sect,.callout:not([class*="cx-"]),.callout.cx-zusatz,details.frage,details.quiz-item,
  .aufg,.article figure.abb,.arttoc,.zweck,.neighbors .nb,.pn,.theme-card,details.beispiel,details.vorwissen,.fassung,.verwendet){border-left:1px solid var(--rahmen);}
@media(max-width:620px){ .arttoc ul{grid-template-columns:1fr;} }
@media(max-width:920px){ .article{grid-template-columns:1fr;} .toc{display:none;} #toggleRight{display:none;} }   /* keine Gliederung -> ihr Toggle weg */
@media(max-width:720px){ .layout{grid-template-columns:1fr;} .side{display:none;border-right:none;}
  /* Themenbaum als Overlay (über #toggleLeft geöffnet); muss das Desktop-Einklappen überstimmen */
  .layout .side.open{display:block;position:fixed;inset:56px 0 0;z-index:30;background:var(--panel);max-height:none;overflow:auto;padding:14px 16px 48px;
    align-self:stretch;}   /* stretch: sonst richtet sich das Overlay nach dem Inhalt (align-self:start der Spalte) und rutscht über die Leiste */
  .topbar{gap:8px;padding:10px 12px;} .topbar .searchBtn{padding:8px;}
  .topbar .panelCenter{position:static;transform:none;margin-left:auto;gap:4px;}   /* im Fluss: zwischen Logo und Suche, nichts überlappt */
  .topbar .searchBtn kbd{display:none;}   /* Suchknopf nur mit dem Wort, ohne Tastenhinweis */
  .article{padding:22px 14px 64px;}                               /* etwas Luft an den Rändern auf dem Handy */
  .article p,.article li{font-size:17px;}                         /* Fließtext auf dem Handy nicht verkleinern */
  .article .katex{font-size:1.14em;}                              /* Inline-Formeln auf dem Handy nicht zu klein */
  .article .katex-display{font-size:1.2em;} .article .fbox{padding:8px 13px 12px;}     /* abgesetzte Formeln gut lesbar */
  .arttoc{padding:14px 16px;}
  .article .sect{padding:2px 15px 14px;}
  .neighbors{grid-template-columns:1fr;}
}
@media(max-width:400px){   /* schmale Handys: Leiste kompakter, damit Pfeile und Knöpfe nebeneinander passen (Höhe bleibt 57 px) */
  .topbar{gap:4px;padding:12px 8px;} .brand{font-size:17px;}
  .topbar .iconBtn,.topbar .panelBtn,.topbar .navBtn{width:32px;height:32px;padding:0;justify-content:center;border-radius:9px;}
  .topbar .searchBtn{height:32px;padding:0 9px;border-radius:9px;font-size:13px;}
}
@media(max-width:379px){ .topbar .editorlink{display:none;} }   /* schmal: Editor-Link weg (Desktop-Werkzeug), Platz für das Wort „Suchen“ */
@media(max-width:330px){ .brand{font-size:15px;} .topbar .searchBtn{padding:0 6px;} }   /* sehr schmal (320 px): Logo und Suchknopf kleiner */
/* ---------- Artikel lesen (11.11.2026): Sprunglink, Kennzahlenzeile, Zusammenfassung, Ankerlinks, Kopierknopf, Vergrößern,
   Handy ohne Karte in Karte, Druckansicht ---------- */
.skip{position:absolute;left:12px;top:-80px;z-index:100;padding:8px 14px;border:2px solid var(--accent3);border-radius:10px;
  background:var(--panel);color:var(--accent);font-weight:700;}
.skip:focus{top:10px;text-decoration:none;}
main.article:focus{outline:none;}
.crumbs .cr-sep{color:var(--muted);}
.art-meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px;margin:.15em 0 1.3em;font-size:14px;color:var(--muted);}
.art-meta .am-zahlen{display:inline-flex;flex-wrap:wrap;align-items:baseline;}
.art-meta .am-zahlen>span+span::before{content:"·";margin:0 .5em;}
.art-meta .am-zf{color:var(--accent);font-weight:600;}
.art-meta .am-lf{color:var(--accent);}
.art-meta .apill{margin-left:0;}
.art-meta .langs-art{margin:0 0 0 auto;}
/* Zusammenfassung am Artikelende: Begriffe, Formeln, Zusammenhänge; jeder Punkt springt an seine Stelle */
.zf{margin:2.2em 0 1.4em;padding:14px 20px 10px;border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:12px;
  background:var(--soft);scroll-margin-top:72px;}
.article .zf-t{margin:0 0 .3em;font-size:21px;color:var(--accent2);scroll-margin-top:72px;}
.zf-g{margin:.8em 0 .6em;}
.zf-gh{font-family:var(--fdisp);font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:2px;}
.article .zf-l{margin:0;padding-left:1.15em;}
.article .zf-l li{font-size:16px;line-height:1.6;margin:.32em 0;}
.zf-l li::marker{color:var(--accent);}
.zf .zf-b{font-weight:700;}
.zf .zf-a{color:var(--ink);} .zf .zf-a:hover{color:var(--accent);}
.zf .zf-fl{font-size:13.5px;font-weight:600;}
.article .zf-f .katex-display{font-size:1.08em;margin:.1em 0 .35em;}
.article .zf-f .katex-display>.katex{text-align:left;}
.article .zf-f .mrow{justify-content:flex-start;column-gap:1.8em;margin:0;}
.article .zf-f .mrow .katex-display{margin:.1em 0 .3em;}
details.zf-mehr>summary{display:inline-block;margin:.1em 0 .2em 1.15em;cursor:pointer;list-style:none;font-size:14.5px;font-weight:600;color:var(--accent);}
details.zf-mehr>summary::-webkit-details-marker{display:none;}
details.zf-mehr>summary:hover{text-decoration:underline;}
details.zf-mehr[open]>summary{display:none;}
:root[data-theme="dark"] .zf{border-color:var(--rahmen);border-left-color:var(--accent);}
/* Sprungziele der Zusammenfassung: nicht unter der Kopfleiste, kurz orange hinterlegt */
.article :is([id^="kb-"],[id^="kf-"],[id^="kg-"]){scroll-margin-top:84px;}
@keyframes zf-ziel{from{background-color:color-mix(in srgb,var(--accent3) 24%,transparent);}to{background-color:transparent;}}
.article :is([id^="kb-"],[id^="kf-"],[id^="kg-"]):target{animation:zf-ziel 2.6s ease-out;border-radius:5px;}
/* Ankerlink an Überschriften: „#“ erst bei Hover oder Fokus; am Touchgerät ohne */
.article h4{scroll-margin-top:66px;}
.h-anker{margin-left:.35em;padding:0 .15em;color:var(--muted);font-weight:500;opacity:0;transition:opacity .15s;}
.article :is(h2,h3,h4):hover>.h-anker,.h-anker:focus-visible{opacity:1;}
.h-anker:hover{color:var(--accent);text-decoration:none;}
.h-anker.kopiert{opacity:1;}
.h-anker.kopiert::after{content:attr(data-kopiert);margin-left:.5em;font-family:var(--fbody);font-size:12.5px;font-weight:600;
  letter-spacing:0;color:var(--accent);}
@media(hover:none){ .h-anker{display:none;} }
/* Kopierknopf an Code-Blöcken (wissen.js): in der Kopfzeile, sonst oben rechts im Block */
.code-block{position:relative;}
.code-kopie{font:inherit;font-family:var(--fdisp);font-size:12px;font-weight:600;line-height:1.5;color:var(--muted);background:var(--panel);
  border:1px solid var(--border);border-radius:7px;padding:1px 9px;cursor:pointer;}
.code-kopie:hover,.code-kopie:focus-visible{color:var(--accent);border-color:var(--accent);}
.code-kopie.ok{color:var(--accent);border-color:var(--accent);}
.code-kopf .code-kopie{flex:none;margin-left:2px;}
.code-kopf .code-l+.code-kopie{margin-left:0;}
.code-block>.code-kopie{position:absolute;top:7px;right:8px;z-index:1;opacity:.92;}
@media(hover:hover){ .code-block>.code-kopie{opacity:0;} .code-block:hover>.code-kopie,.code-block>.code-kopie:focus-visible{opacity:1;} }
/* Abbildung antippen: Overlay mit voller Breite (wissen.js); Bild bzw. Animation samt Spieler wandern hinein */
.article figure.abb>img,.article figure.abb>svg.abb-anim{cursor:zoom-in;}
.article figure.abb>img:focus-visible,.article figure.abb>svg.abb-anim:focus-visible{outline:2px solid var(--accent3);outline-offset:3px;}
html.abb-offen,html.abb-offen body{overflow:hidden;}
.abb-gross{position:fixed;inset:0;z-index:60;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;
  padding:56px 10px 14px;background:rgba(8,14,11,.94);}
.abb-gross[hidden]{display:none;}
.abb-gross .ag-buehne{width:min(100%,1500px);max-height:calc(100% - 40px);overflow:auto;padding:8px;border-radius:12px;background:var(--panel);}
.abb-gross .ag-buehne>img,.abb-gross .ag-buehne>svg{display:block;width:100%;height:auto;max-height:calc(100vh - 170px);object-fit:contain;
  margin:0 auto;border-radius:8px;background:#fff;cursor:zoom-out;}
.abb-gross .abb-spieler{margin:8px 2px 0;}
.abb-gross .ag-text{max-width:min(100%,80ch);color:#e9eeea;font-size:14px;line-height:1.5;text-align:center;}
.abb-gross .ag-text .abb-n{font-weight:700;margin-right:4px;}
.abb-gross .ag-zu{position:absolute;top:10px;right:12px;display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;
  padding:0;border:1px solid rgba(255,255,255,.45);border-radius:999px;background:rgba(0,0,0,.35);color:#fff;cursor:pointer;}
.abb-gross .ag-zu:hover,.abb-gross .ag-zu:focus-visible{border-color:var(--bar-hl);color:var(--bar-hl);outline:none;}
.abb-platz{display:block;}
/* Handy: Abschnittskarte ohne Rand und Innenabstand (Kästen behalten ihren Rahmen), kompakter Kopf, kurze Brotkrumen */
@media(max-width:620px){
  .article{padding:14px 12px 56px;}
  .article .sect,:root[data-theme="dark"] .article>article .sect{border:0;border-radius:0;box-shadow:none;background:transparent;padding:0;}
  .article .sect>h2:first-child{margin-top:.2em;}
  .crumbs{margin-bottom:4px;font-size:12.5px;line-height:1.45;}
  .crumbs .cr-home,.crumbs .cr-alt,.crumbs .cr-erst>.cr-sep,.crumbs .cr-l{display:none;}
  .article h1{margin-bottom:.25em;}
  .art-meta{margin-bottom:1em;font-size:13.5px;gap:6px 10px;}
  .arttoc{padding:11px 14px 10px;margin-bottom:1.5em;}                 /* Verzeichnis als Fließzeile statt langer Spalte */
  .arttoc-h{margin-bottom:5px;}
  .arttoc ul{display:flex;flex-wrap:wrap;gap:1px 16px;}
  .arttoc a{padding:3px 0;font-size:15px;line-height:1.4;}
  .arttoc a::before{margin-right:6px;}
  .callout{padding:13px 14px;}
  .zf{padding:12px 14px 8px;}
  .aufg-b{padding:12px 13px 11px;}
}
/* Druckansicht: ohne Leisten, Menüs und Spieler; Kästen aufgeklappt (Lösungen bleiben weg), helle Farben auch nachts */
@media print{
  :root,:root[data-theme="dark"]{--bg:#fff;--panel:#fff;--ink:#111;--muted:#454b48;--border:#cfd4d1;--soft:#f5f6f5;--accent:#15633a;
    --accent2:#1b7f4a;--accent3:#c2410c;--on-accent:#fff;--aufg:#15633a;--rahmen:#cfd4d1;}
  body{background:#fff;color:#111;}
  .skip,.topbar,.side,.toc,.neighbors,.langs,.abb-spieler,.abb-knopf,.searchOverlay,.h-anker,.code-kopie,.abb-gross,.am-zf,.toc-zf,
  .fassung,details.loesung,details.zf-mehr>summary{display:none!important;}
  .layout,.article{display:block;max-width:none;margin:0;padding:0;}
  .article>article{max-width:none;}
  .article .sect{border:0;box-shadow:none;padding:0;margin:0;}
  details::details-content{content-visibility:visible;display:block;}
  .article a{color:inherit;}
  .article a[href^="http"]::after{content:" (" attr(href) ")";font-size:.85em;color:#454b48;overflow-wrap:anywhere;}
  .article :is(figure,.callout,.aufg,.code-block,.gl-zeile,.fbox,.zf-l li,table){break-inside:avoid;}
  .article :is(h2,h3,h4){break-after:avoid;}
  .article pre{white-space:pre-wrap;overflow-wrap:anywhere;overflow:visible;}
  :root[data-theme="dark"] .hl [class]{color:#111!important;}
}
/* ---------- Lernen (W2, 11.11.2026): Lesefortschritt, Modul-Links, Link-Vorschau, Selbsttest, Begriffe, Lernkarten.
   Nur Grün, Orange und Neutraltöne; keine Symbole als Marker, keine Punkte oder Abzeichen. ---------- */
.lern-seite [hidden],.zf [hidden],.lf-weiter[hidden],.vs-karte[hidden]{display:none!important;}
.lf-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;}
/* gelesene Artikel: dezentes Häkchen statt des Punkts (Seitenleiste) bzw. hinter dem Titel (Übersicht); Kapitel „5/12“ */
.side li a.gelesen::before{width:4px;height:8px;left:9px;top:calc(3px + .84em - 6px);border-radius:0;background:none;
  border:solid var(--accent);border-width:0 1.8px 1.8px 0;transform:rotate(45deg);opacity:.9;}
.side li a.active.gelesen::before{border-color:currentColor;}
.theme-card a.gelesen::after{content:"";display:inline-block;width:4px;height:8px;margin-left:9px;border:solid var(--accent);
  border-width:0 1.8px 1.8px 0;transform:translateY(-2px) rotate(45deg);opacity:.9;}
.side summary .lf-z{float:right;margin-left:6px;font-size:11.5px;font-weight:500;color:var(--muted);line-height:2;}
/* schmaler Fortschrittsbalken: grün auf neutral */
.lf-balken{height:4px;border-radius:2px;background:var(--border);overflow:hidden;}
.lf-balken>span{display:block;height:100%;border-radius:2px;background:var(--accent);}
:root[data-theme="dark"] .lf-balken{background:rgba(255,255,255,.16);}
.lf-kap{display:flex;align-items:center;gap:10px;margin:-3px 0 9px;}
.lf-kap .lf-balken{flex:1;}
.lf-kap .lf-text,.lf-art .lf-text{font-size:12.5px;color:var(--muted);white-space:nowrap;}
.lf-art{display:flex;align-items:center;gap:12px;margin:22px 0 4px;}
.lf-art .lf-balken{flex:0 0 96px;}
.lf-art .lf-text{white-space:normal;font-size:13.5px;}
/* Übersicht: „Weiterlesen“ und „Fortschritt zurücksetzen“ */
.lf-weiter{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 16px;margin:-.5em 0 1.5em;padding:10px 14px 10px 16px;
  border:1px solid var(--border);border-left:4px solid var(--accent3);border-radius:12px;background:var(--soft);}
:root[data-theme="dark"] .lf-weiter{border-color:var(--rahmen);border-left-color:var(--accent3);}
.lf-weiter-a{display:flex;flex-direction:column;min-width:0;}
.lf-weiter-a:hover{text-decoration:none;} .lf-weiter-a:hover .lf-wt{text-decoration:underline;}
.lf-wh{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent3);}
.lf-wt{font-weight:600;color:var(--accent);overflow-wrap:anywhere;}
.lern-reset{font:inherit;font-size:13px;line-height:1.5;color:var(--muted);background:none;border:1px solid var(--border);border-radius:8px;
  padding:3px 10px;cursor:pointer;}
.lern-reset:hover,.lern-reset:focus-visible{color:var(--ink);border-color:var(--muted);}
.lern-reset.frage{color:var(--accent3);border-color:var(--accent3);}
/* Begriffe und Lernkarten eines Moduls: leise Zeile unter dem Modul (Seitenleiste, Übersicht) */
.side-lernen{margin:1px 0 3px 22px;font-size:13px;color:var(--muted);}
.side-lernen a{color:var(--muted);} .side-lernen a:hover{color:var(--accent);}
.idx-lernen{margin:-.15em 0 .45em;font-size:13.5px;color:var(--muted);}
/* Link-Vorschau */
.vs-karte{position:absolute;z-index:40;padding:11px 14px 12px;background:var(--panel);color:var(--ink);border:1px solid var(--border);
  border-radius:12px;box-shadow:0 8px 28px rgba(16,24,20,.16);font-family:var(--fbody);font-size:14px;line-height:1.5;}
:root[data-theme="dark"] .vs-karte{border-color:var(--rahmen);box-shadow:0 8px 28px rgba(0,0,0,.5);}
.vs-k{font-size:12px;color:var(--muted);margin-bottom:2px;}
.vs-t{font-family:var(--fdisp);font-size:15.5px;font-weight:700;line-height:1.3;color:var(--accent2);}
.vs-p{margin:.45em 0 0;}
.vs-f{display:flex;gap:10px;margin-top:10px;}
.vs-o,.vs-s{font:inherit;font-size:14px;font-weight:600;padding:5px 14px;border:1px solid var(--border);border-radius:8px;background:var(--soft);
  color:var(--ink);cursor:pointer;}
.vs-o{background:var(--accent);border-color:var(--accent);color:var(--on-accent);} .vs-o:hover{text-decoration:none;}
@media(hover:none){ a[data-vs]{-webkit-touch-callout:none;} }
/* Selbsttest in der Zusammenfassung: zugedeckte Punkte als graue Fläche mit „Aufdecken“ */
.zf-kopf{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:4px 12px;}
.zf-test{font:inherit;font-size:13px;font-weight:600;line-height:1.6;color:var(--accent);background:var(--panel);border:1px solid var(--border);
  border-radius:999px;padding:1px 12px;cursor:pointer;}
.zf-test:hover,.zf-test:focus-visible{border-color:var(--accent);}
.zf-test[aria-pressed="true"]{color:var(--on-accent);background:var(--accent);border-color:var(--accent);}
.zf .zu{cursor:pointer;border-radius:5px;background:color-mix(in srgb,var(--muted) 17%,var(--panel));
  -webkit-box-decoration-break:clone;box-decoration-break:clone;}
.zf .zu,.zf .zu *{color:transparent!important;text-decoration:none!important;border-color:transparent!important;}
.zf .zu .katex,.zf .zu img,.zf .zu svg{visibility:hidden;}
.zf .zu::before{content:attr(data-auf);padding:0 .55em;font-size:12.5px;font-weight:600;color:var(--muted)!important;}
.zf div.zu{display:block;min-height:2.2em;margin:.15em 0 .3em;}
.zf .zu:hover{background:color-mix(in srgb,var(--accent) 15%,var(--panel));}
.zf .zu:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.zf-cue{color:var(--muted);}
.article p.zf-fuss{margin:.7em 0 .25em;font-size:14px;}
/* Seiten „Begriffe“ und „Lernkarten“ */
.lern-meta .lern-modul{color:var(--muted);}
.article p.lern-lede{font-size:17px;margin-bottom:.7em;}
.article p.lern-nav{font-size:15px;margin:0 0 1.2em;}
.bg-abc{display:flex;flex-wrap:wrap;gap:5px;margin:0 0 12px;}
.bg-abc a{min-width:32px;padding:3px 8px;text-align:center;font-size:14px;font-weight:600;border:1px solid var(--border);border-radius:7px;background:var(--panel);}
.bg-abc a:hover{border-color:var(--accent);text-decoration:none;}
.bg-such{position:sticky;top:53px;z-index:5;display:flex;align-items:center;gap:12px;margin:0 0 6px;padding:8px 0;background:var(--bg);}
.bg-filter{flex:1;min-width:0;font:inherit;font-size:16px;padding:8px 12px;border:1px solid var(--border);border-radius:10px;background:var(--panel);color:var(--ink);}
.bg-filter:focus{outline:2px solid var(--accent);outline-offset:1px;}
.bg-n{font-size:13.5px;color:var(--muted);white-space:nowrap;}
.bg-g{scroll-margin-top:118px;}
.article .bg-g>h2{margin:1.1em 0 .2em;padding-bottom:3px;font-size:20px;color:var(--accent2);border-bottom:1px solid var(--border);}
.bg-l{margin:0;}
.bg-e{padding:8px 0 9px;border-bottom:1px solid var(--border);}
.bg-e dt{font-size:16.5px;font-weight:700;}
.bg-e dd{margin:2px 0 0;font-size:15.5px;line-height:1.55;}
.bg-wo{display:block;margin-top:2px;font-size:13px;color:var(--muted);}
.article p.bg-nichts{color:var(--muted);font-size:15.5px;}
.lk-leiste{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 14px;margin:0 0 12px;}
.lk-wahl{display:flex;align-items:center;gap:8px;min-width:0;max-width:100%;font-size:14px;color:var(--muted);}
.lk-sel{min-width:0;max-width:min(100%,430px);font:inherit;font-size:14.5px;padding:5px 8px;border:1px solid var(--border);border-radius:8px;
  background:var(--panel);color:var(--ink);}
.lk-zahl{font-size:14.5px;font-weight:600;color:var(--accent);}
.lk-karte{min-height:210px;padding:16px 22px 20px;background:var(--panel);border:1px solid var(--border);border-top:4px solid var(--accent);
  border-radius:14px;box-shadow:0 2px 10px rgba(16,24,20,.05);cursor:pointer;outline:none;overflow-wrap:anywhere;}
.lk-karte:focus-visible{box-shadow:0 0 0 2px var(--accent3);}
:root[data-theme="dark"] .lk-karte{border-color:var(--rahmen);border-top-color:var(--accent);}
.lk-kopf{margin-bottom:8px;font-size:12.5px;font-weight:600;letter-spacing:.02em;color:var(--muted);}
.lk-vorne{font-size:20px;font-weight:600;line-height:1.45;}
.lk-hinten{margin-top:14px;padding-top:14px;border-top:1px dashed var(--border);font-size:17px;line-height:1.6;}
:root[data-theme="dark"] .lk-hinten{border-top-color:var(--rahmen);}
.lk-steuer{margin:14px 0 8px;}
.lk-um,.lk-neu{font:inherit;font-size:15.5px;font-weight:600;padding:9px 22px;border:1px solid var(--accent);border-radius:10px;
  background:var(--accent);color:var(--on-accent);cursor:pointer;}
.lk-um{width:100%;}
.lk-um:hover,.lk-neu:hover{filter:brightness(1.08);}
.lk-bew{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;}
.lk-b{display:flex;flex-direction:column;align-items:center;gap:1px;font:inherit;font-size:15px;font-weight:600;line-height:1.3;padding:9px 6px 8px;
  border:1.5px solid var(--border);border-radius:10px;background:var(--panel);color:var(--ink);cursor:pointer;}
.lk-b small{font-size:12px;font-weight:500;color:var(--muted);}
.lk-b1{border-color:color-mix(in srgb,var(--accent3) 60%,var(--border));}
.lk-b2{border-color:var(--accent);color:var(--accent);}
.lk-b:hover{background:var(--soft);}
.lk-b:focus-visible,.lk-um:focus-visible,.lk-neu:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.lk-fuss{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 14px;margin:4px 0 12px;font-size:14px;}
.lk-tasten{font-size:13px;color:var(--muted);}
@media(hover:none){ .lk-tasten{display:none;} }
.lk-ende{padding:16px 20px;border:1px solid var(--border);border-radius:14px;background:var(--soft);}
.article .lk-ende p{margin:0 0 .7em;font-size:16px;}
.article p.lk-hinweis{font-size:14px;color:var(--muted);}
.lk-reset{margin:4px 0 6px;}
details.lk-alle{margin:24px 0 0;}
details.lk-alle>summary{cursor:pointer;font-size:15px;font-weight:600;color:var(--accent);margin-bottom:4px;}
.lk-kap{scroll-margin-top:70px;}
.article .lk-kap>h2{margin:1.1em 0 .3em;font-size:19px;color:var(--accent2);}
.article ol.lk-l{list-style:none;margin:0;padding:0;}
.article .lk-l li.lk{margin:0;padding:10px 0;font-size:16px;border-bottom:1px solid var(--border);}
.lk-v{font-weight:600;}
.lk-typ{display:inline-block;margin-right:8px;font-size:11.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);}
.lk-r{margin-top:3px;}
.lk-q{display:inline-block;margin-top:3px;font-size:13px;}
.lk-luecke{font-weight:700;letter-spacing:.04em;color:var(--accent3);}
.lk-wort{color:var(--accent);}
@media(max-width:620px){
  .lk-karte{min-height:180px;padding:14px 15px 16px;}
  .lk-vorne{font-size:18px;} .lk-hinten{font-size:16px;}
  .lk-b{font-size:14px;padding:8px 4px 7px;}
  .bg-such{top:49px;}
}
@media print{
  .lf-weiter,.lf-art,.lf-z,.side-lernen,.idx-lernen,.vs-karte,.zf-test,.zf-fuss,.zf-cue,.bg-abc,.bg-such,.lk-app,.lern-reset{display:none!important;}
}
/* ---------- Finden (W3a, 11.11.2026): nachgeladene Seitenleiste, Modulkarten der Übersicht, Suchfeld ---------- */
.side .side-mehr,.side .baum-hinweis{display:block;margin:2px 0 6px 22px;font-size:13px;color:var(--muted);}
.side .side-mehr:hover{color:var(--accent);}
.article.idx{grid-template-columns:minmax(0,1fr);}         /* Übersicht ohne rechte Spalte: Platz für drei Karten nebeneinander */
.article.idx>article{max-width:none;}
.article.idx .lede,.article.idx .idx-hinweis{max-width:70ch;}
.idx-suche{display:flex;align-items:center;gap:10px;width:100%;max-width:620px;margin:-.3em 0 1.6em;padding:12px 16px;
  border:1px solid var(--border);border-radius:12px;background:var(--panel);color:var(--muted);font:inherit;font-size:16px;text-align:left;cursor:text;}
.idx-suche span{flex:1;min-width:0;}
.idx-suche:hover,.idx-suche:focus-visible{border-color:var(--accent);}
.idx-suche[hidden]{display:none;}
:root[data-theme="dark"] .idx-suche{border-color:var(--rahmen);}
.field-block>h2{scroll-margin-top:70px;}
.gruppen{display:flex;flex-wrap:wrap;gap:22px 18px;margin:.4em 0 .6em;}
.gruppe{flex:1 1 250px;min-width:0;scroll-margin-top:70px;}
.gruppe.gr-n2{flex-basis:520px;} .gruppe.gr-n3{flex-basis:790px;}
.gruppe:has(.mk-det[open]){flex-basis:100%;}                 /* aufgeklappte Karte: die Gruppe nimmt die ganze Breite */
.article .gruppe h3.gr-h{margin:0 0 8px;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent3);}
.mk-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;align-items:start;}
.mk{display:flex;flex-direction:column;min-width:0;background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);}
.mk:has(.mk-det[open]){grid-column:1/-1;}
:root[data-theme="dark"] .mk{border-color:var(--rahmen);}
.mk>.theme-card{border:0;}
.mk-det>summary{list-style:none;cursor:pointer;}
.mk-det>summary::-webkit-details-marker{display:none;}
.mk-kopf{display:flex;flex-direction:column;gap:2px;padding:14px 16px 8px;border-radius:var(--radius) var(--radius) 0 0;scroll-margin-top:70px;}
.mk-kopf:hover{background:var(--soft);}
.mk-kopf:focus-visible{outline:2px solid var(--accent);outline-offset:-2px;}
.mk-titel{font-family:var(--fdisp);font-weight:700;font-size:17px;color:var(--accent);}
.mk-titel::after{content:"";display:inline-block;width:.42em;height:.42em;margin:0 0 .16em .5em;border:solid var(--muted);
  border-width:0 2px 2px 0;transform:rotate(45deg);transition:transform .15s;}  /* Winkel: zu = nach unten, offen = nach oben */
.mk-det[open]>.mk-kopf .mk-titel::after{transform:rotate(-135deg);margin-bottom:-.05em;}
.mk-voll{font-size:14px;line-height:1.35;color:var(--ink);}
.mk-zahl{margin-top:4px;font-size:13px;color:var(--muted);}
.mk-lf:empty{display:none;}
.mk-lf{display:flex;align-items:center;gap:8px;margin-top:6px;}
.mk-lf .lf-balken{flex:1;} .mk-lf .lf-text{font-size:12.5px;color:var(--muted);white-space:nowrap;}
.mk-inhalt{padding:4px 16px 8px;border-top:1px solid var(--border);}
:root[data-theme="dark"] .mk-inhalt{border-top-color:var(--rahmen);}
.mk-lernen{margin-top:auto;padding:4px 16px 12px;font-size:13.5px;color:var(--muted);}
.mk-lernen a{color:var(--muted);} .mk-lernen a:hover{color:var(--accent);}
details.mk-kap{border-bottom:1px solid var(--border);}
details.mk-kap:last-child{border-bottom:0;}
details.mk-kap>summary{display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 12px;padding:9px 2px;cursor:pointer;list-style:none;}
details.mk-kap>summary::-webkit-details-marker{display:none;}
details.mk-kap>summary::before{content:"▸";color:var(--muted);display:inline-block;width:.9em;transition:transform .15s;}
details.mk-kap[open]>summary::before{transform:rotate(90deg);}
.kap-name{flex:1 1 260px;min-width:0;font-weight:600;color:var(--ink);}
.kap-zahl{font-size:13px;color:var(--muted);white-space:nowrap;}
details.mk-kap>summary .lf-z{font-size:12px;color:var(--muted);}
details.mk-kap .theme-card,:root[data-theme="dark"] details.mk-kap .theme-card{margin:0 0 10px;padding:0 0 0 1.15em;border:0;background:transparent;}
.article details.mk-kap .theme-card li{font-size:15.5px;margin:3px 0;}
details.mk-kap details.mk-kap{margin-left:1em;}
.article p.idx-nur-de{font-size:15px;color:var(--muted);margin:1.6em 0 0;}
.searchResults .r-abschnitt{color:var(--accent);}
.searchHint.laedt{border-top:0;}
@media(max-width:620px){
  .gruppe,.gruppe.gr-n2,.gruppe.gr-n3{flex-basis:100%;}
  .mk-grid{grid-template-columns:1fr;}
  .mk-inhalt{padding:2px 12px 6px;}
}
@media print{ .idx-suche,.mk-lf{display:none!important;} }
/* ---------- Ansichten (W4a, 11.11.2026): Ausführlich | Kurz | Formeln auf derselben Seite, Formelsammlung und
   „Kapitel auf einer Seite“ je Modul. <html data-ansicht> setzt der Kopf der Seite (Adresse ?ansicht=, sonst gemerkte Wahl);
   ohne Skript gilt „Ausführlich“. Kurz: Blöcke mit Klasse kw fallen weg, rohe Listen ohne bleibenden Inhalt ebenso. ---------- */
@media(max-width:400px){
  .topbar .ans-sel{height:32px;max-width:104px;padding:0 21px 0 9px;font-size:13px;background-position:calc(100% - 12px) 52%,calc(100% - 7px) 52%;}
}
@media(max-width:330px){ .topbar .ans-sel{max-width:92px;font-size:12.5px;} }
.ans-kurz,.fb-blatt{display:none;}
:root[data-ansicht="kurz"] .art .kw,
:root[data-ansicht="kurz"] .art-body :is(ol,ul,li):not(.kz *):not(:has(.kz)),
:root[data-ansicht="kurz"] .art-body .sect:not(:has(.kz,h2,h3)),
:root[data-ansicht="kurz"] .art-body hr{display:none!important;}
:root[data-ansicht="kurz"] .art-body .sect>h3:first-child{margin-top:.7em;}
:root[data-ansicht="kurz"] .art.hat-kurz .art-body{display:none!important;}
:root[data-ansicht="kurz"] .art.hat-kurz .ans-kurz{display:block;}
:root[data-ansicht="formeln"] .art :is(.art-body,.ans-kurz,.arttoc,.zf,.zf-fuss,.verwendet,.cx-quiz,.am-zf),
:root[data-ansicht="formeln"] .article .toc{display:none!important;}
:root[data-ansicht="formeln"] .art .fb-blatt{display:block;}
.art.ansicht-anker .art-body{scroll-margin-top:72px;}
/* Formelblatt am Artikel und Formelsammlung des Moduls: Name bzw. Abschnitt, darunter die Formel; jeder Eintrag springt an
   seine Stelle im Artikel (ausführliche Ansicht) */
.fb-blatt{margin:0 0 1.6em;padding:6px 22px 16px;border:1px solid var(--border);border-radius:16px;background:var(--panel);}
:root[data-theme="dark"] .fb-blatt{border-color:var(--rahmen);}
.fb-kopf{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:6px 14px;margin:.5em 0 .6em;}
.article .fb-kopf h2{margin:0;font-size:22px;color:var(--accent2);}
.fb-werkzeug{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;font-size:14px;}
.fb-modul{font-weight:600;}
.fb-dl{display:inline-flex;flex-wrap:wrap;align-items:center;gap:4px;}
.fb-dl[hidden]{display:none;}
.fb-dl-t{color:var(--muted);margin-right:2px;}
.fb-dl-b{font:inherit;font-size:12.5px;font-weight:700;letter-spacing:.03em;padding:3px 9px;border:1px solid var(--border);border-radius:999px;
  background:var(--soft);color:var(--accent);cursor:pointer;}
.fb-dl-b:hover,.fb-dl-b:focus-visible{border-color:var(--accent);}
.fb-dl-b[aria-busy="true"]{opacity:.55;cursor:progress;}
:root[data-theme="dark"] .fb-dl-b{border-color:var(--rahmen);}
.fb-dl-s{font-size:13px;color:var(--muted);}
.fb-dl-s.fehler{color:var(--accent3);}
.fb-h{margin:1.1em 0 .3em;font-size:12.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--accent3);}
.fb-e{margin:.35em 0;padding:8px 0 8px;border-top:1px solid var(--border);}
:root[data-theme="dark"] .fb-e{border-top-color:var(--rahmen);}
.fb-h+.fb-e,.fb-inhalt>.fb-e:first-child{border-top:0;}
.fb-n{display:inline-block;font-weight:700;color:var(--accent2);}
.fb-i>p:first-child{margin-top:.25em;} .fb-i>:last-child{margin-bottom:.1em;}
.fb-i .anker{display:none;}
.fb-gl{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:10px;}
.fb-f{min-width:0;} .fb-f .katex-display{margin:.3em 0;}
.fb-nr{font-size:14px;color:var(--muted);white-space:nowrap;}
.fb-nr:hover{color:var(--accent);}
.fb-leer{color:var(--muted);}
.fb-cmd{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:start;gap:10px;}   /* Übersicht: Befehle eines Blocks */
.fb-code{margin:.15em 0;padding:7px 12px;background:var(--soft);border:1px solid var(--border);border-radius:8px;font-family:var(--fmono);
  font-size:14px;line-height:1.55;white-space:pre-wrap;overflow-wrap:anywhere;}
:root[data-theme="dark"] .fb-code{border-color:var(--rahmen);}
.fb-cmd .fb-nr{padding-top:6px;}
.fb-zu-kurz{font:inherit;font-weight:600;color:var(--accent);background:none;border:0;padding:0;cursor:pointer;text-decoration:underline;}
.fb-block>.sect{border:0;padding:0;box-shadow:none;}
.ans-kurz{margin:0 0 18px;}
/* Modulseiten: Kapitelwahl, Formelsammlung, Kapitel auf einer Seite */
.kap-nav[hidden]{display:none;}
.kap-nav ol{margin:.2em 0 1.2em;padding:0;list-style:none;columns:2 260px;column-gap:28px;}
.article .kap-nav li{margin:0 0 4px;font-size:15px;line-height:1.45;break-inside:avoid;}
.kap-leiste{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin:0 0 1.2em;}
.kap-leiste[hidden]{display:none;}
.kap-wahl{display:inline-flex;align-items:center;gap:8px;font-size:14.5px;color:var(--muted);}
.kap-sel{font:inherit;font-size:15px;max-width:min(78vw,460px);padding:6px 10px;border:1px solid var(--border);border-radius:10px;background:var(--panel);color:var(--ink);}
.kap-druck{font:inherit;font-size:14.5px;font-weight:600;padding:6px 14px;border:1px solid var(--accent);border-radius:999px;background:var(--panel);color:var(--accent);cursor:pointer;}
.kap-druck:hover{background:var(--soft);}
:root[data-theme="dark"] :is(.kap-sel,.kap-druck){border-color:var(--rahmen);}
.fs-werkzeug{margin:0 0 1em;}
.fs-kap,.sz-kap{margin:0 0 1.8em;scroll-margin-top:70px;}
.article .fs-kap>h2,.article .sz-kap>h2{margin:1.2em 0 .4em;padding-bottom:4px;border-bottom:2px solid var(--accent);font-size:22px;}
.fs-art,.sz-art{margin:.6em 0 1.2em;padding:4px 18px 10px;border:1px solid var(--border);border-radius:12px;background:var(--panel);scroll-margin-top:70px;}
:root[data-theme="dark"] :is(.fs-art,.sz-art){border-color:var(--rahmen);}
.article .fs-art>h3,.article .sz-art>h3{margin:.6em 0 .2em;font-size:17px;}
.sz-art .zf-g{margin:.5em 0 .4em;}
.sz-kern{font-size:14.5px;color:var(--muted);}
[data-kapitel-filter] :is(.fs-kap,.sz-kap):not(.kap-an){display:none;}
.kap-seite{margin:0 0 10px 1.15em;font-size:14px;}
.zf-fuss.art-ende{margin:2em 0 1em;}
@media(max-width:620px){                                     /* Handy: ohne Karte, wie die Abschnitte */
  .fb-blatt,:root[data-theme="dark"] .fb-blatt{border:0;padding:0;background:transparent;}
  .fs-art,.sz-art{padding:2px 12px 8px;}
  .fb-gl{gap:6px;}
}
@page{size:A4;margin:14mm 13mm;}
@media print{
  .fb-dl,.fb-modul,.fb-zu-kurz,.kap-nav,.kap-leiste,.fs-werkzeug,.lern-nav,.kap-seite{display:none!important;}
  .fb-blatt{border:0;padding:0;margin:0;}
  .fb-e,.sz-art .zf-l li,.sz-art .zf-gh{break-inside:avoid;}
  .fs-art>h3,.sz-art>h3,.fs-kap>h2,.sz-kap>h2,.zf-gh,.fb-h,.fb-n{break-after:avoid;}
  .fs-art,.sz-art{border:0;border-top:1px solid #cfd4d1;border-radius:0;padding:4px 0 6px;margin:.4em 0 .6em;}
  main:not([data-kapitel-filter]) :is(.fs-kap+.fs-kap,.sz-kap+.sz-kap){break-before:page;}
  .sz-seite .zf-g{margin:.3em 0;} .sz-seite .zf-l li{margin:.1em 0;font-size:11.5pt;}
  .fb-nr{color:#454b48;}
}
/* ---------- Bereiche (W4b, 11.11.2026): Wissen · Lernkarten · Aufgaben · Editor in der Kopfleiste; breit eine Linkreihe
   (aktiver Bereich orange unterstrichen), schmal ein Menü. Die Sprachwahl steht rechts vor der Suche. ---------- */
.topbar .bereiche{display:flex;align-items:center;min-width:0;}
.topbar .b-liste{display:flex;align-items:center;gap:2px;margin:0;padding:0;list-style:none;}
.topbar .b-liste li{margin:0;}
.topbar .b-l{display:block;padding:7px 10px 5px;color:var(--bar-ink);font-weight:600;font-size:14.5px;line-height:1.2;white-space:nowrap;
  border-bottom:2px solid transparent;}
.topbar .b-l:hover{color:var(--bar-hl);text-decoration:none;}
.topbar .b-l.on{color:var(--bar-hl);border-bottom-color:var(--bar-hl);}
.topbar .b-l:focus-visible{outline:2px solid var(--bar-hl);outline-offset:2px;border-radius:6px;}
.topbar .b-menu{display:none;position:relative;}
.topbar .b-toggle{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 11px 0 13px;border-radius:999px;border:1px solid var(--bar-rand);
  background:var(--bar-soft);color:var(--bar-ink);font:inherit;font-size:13.5px;font-weight:700;line-height:1;cursor:pointer;white-space:nowrap;}
.topbar .b-toggle:hover{border-color:var(--bar-hl);}
.topbar .b-toggle[aria-expanded="true"]{border-color:var(--bar-hl);color:var(--bar-hl);}
.topbar .b-toggle:focus-visible{outline:2px solid var(--bar-hl);outline-offset:2px;}
.topbar .b-toggle .l-pfeil{opacity:.85;transition:transform .15s;}
.topbar .b-toggle[aria-expanded="true"] .l-pfeil{transform:rotate(180deg);}
.topbar .b-icon{display:none;flex:0 0 auto;}
.b-menu .l-menu{position:absolute;top:calc(100% + 6px);left:0;z-index:40;min-width:200px;margin:0;padding:6px;list-style:none;background:var(--panel);
  border:1px solid var(--border);border-radius:12px;box-shadow:0 12px 32px rgba(10,20,15,.16),0 2px 6px rgba(10,20,15,.08);}
.b-menu .l-menu[hidden]{display:none;}
.b-menu .l-menu li{margin:0;padding:0;font-size:14.5px;line-height:1.3;}
.b-menu .l-item{display:flex;align-items:center;justify-content:space-between;gap:14px;width:100%;padding:9px 12px;border:0;border-radius:8px;
  background:none;color:var(--ink);font:inherit;font-weight:500;text-align:left;text-decoration:none;cursor:pointer;}
.b-menu a.l-item:hover,.b-menu a.l-item:focus,.b-menu button.l-item:hover{background:var(--soft);text-decoration:none;}
.b-menu .l-item.on{color:var(--accent3);font-weight:700;background:color-mix(in srgb,var(--accent3) 9%,var(--panel));}
.b-menu .l-item:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.b-menu .b-thema{display:none;margin-top:4px;padding-top:4px;border-top:1px solid var(--border);}
:root[data-theme="dark"] .b-menu .l-menu{border-color:var(--rahmen);box-shadow:0 12px 32px rgba(0,0,0,.55);}
.topbar .langs-top{margin-left:auto;}
.topbar .langs-top~.searchBtn{margin-left:0;}
@media(max-width:900px){ .topbar .langs-top~.searchBtn{margin-left:auto;} }
@media(max-width:1239px){ .topbar.mit-mitte .b-liste{display:none;} .topbar.mit-mitte .b-menu{display:block;} }   /* Artikel: Mitte belegt */
@media(max-width:719px){ .topbar .b-liste{display:none;} .topbar .b-menu{display:block;} }
@media(max-width:560px){ .topbar .b-cur,.topbar .b-toggle .l-pfeil{display:none;} .topbar .b-icon{display:block;}
  .topbar .b-toggle{width:36px;padding:0;justify-content:center;} }
@media(max-width:400px){ .topbar .b-toggle{width:32px;height:32px;border-radius:9px;} }
@media(max-width:379px){ .topbar.mit-mitte #themeBtn{display:none;} .topbar.mit-mitte .b-menu .b-thema{display:block;} }   /* sehr schmal: Hell/Dunkel im Menü */
/* Seiten der Bereiche: ohne Themenbaum, eine Spalte */
.article.bereich-seite{grid-template-columns:minmax(0,1fr);max-width:900px;margin:0 auto;}
.bereich-seite [hidden]{display:none!important;}
.article .bm-g{margin:1.5em 0 .45em;font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);}
.article ul.bm-liste{list-style:none;margin:0 0 1em;padding:0;}
.article .bm-liste li.bm{display:flex;flex-wrap:wrap;align-items:baseline;gap:3px 12px;margin:0 0 8px;padding:11px 15px;border:1px solid var(--border);
  border-radius:12px;background:var(--panel);font-size:16px;}
:root[data-theme="dark"] .article .bm-liste li.bm{border-color:var(--rahmen);}
.bm-t{font-weight:700;font-size:17px;}
.bm-n{font-size:14px;color:var(--muted);}
.bm-s{flex-basis:100%;font-size:14px;}
.article p.lw-ohne{font-size:15.5px;color:var(--muted);}
/* Lernkarten-App: Auswahl, Kartenarten, Modus */
.lw-app{margin:0 0 1.6em;}
.lw-wahl,.ag-leiste{display:flex;flex-wrap:wrap;align-items:flex-end;gap:10px 14px;margin:0 0 12px;}
.lw-feld{display:flex;flex-direction:column;gap:3px;min-width:0;flex:1 1 200px;font-size:13px;font-weight:600;color:var(--muted);}
.lw-sel{min-width:0;width:100%;font:inherit;font-size:15px;font-weight:500;color:var(--ink);padding:7px 9px;border:1px solid var(--border);
  border-radius:9px;background:var(--panel);}
.lw-sel:focus-visible,.lw-art input:focus-visible,.mt-kap input:focus-visible,.ag-offen input:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.lw-arten,.mt-kap{display:flex;flex-wrap:wrap;gap:4px 18px;margin:0 0 12px;padding:7px 13px 10px;border:1px solid var(--border);border-radius:10px;}
.lw-arten legend,.mt-kap legend{padding:0 4px;font-size:13px;font-weight:600;color:var(--muted);}
:root[data-theme="dark"] :is(.lw-arten,.mt-kap,.lw-sel){border-color:var(--rahmen);}
.lw-art,.mt-k,.mt-alle,.ag-offen{font-size:15px;cursor:pointer;}
.lw-art{white-space:nowrap;}
.lw-n{font-size:13px;color:var(--muted);}
.mt-kap{flex-direction:column;}
.mt-alle{font-weight:600;}
.lw-modi{display:inline-flex;flex-wrap:wrap;gap:2px;max-width:100%;margin:0 0 16px;padding:3px;border:1px solid var(--border);border-radius:999px;background:var(--soft);}
.lw-modus{border:0;background:transparent;color:var(--ink);font:inherit;font-size:15px;font-weight:600;padding:7px 16px;border-radius:999px;cursor:pointer;}
.lw-modus:hover{color:var(--accent);}
.lw-modus[aria-pressed="true"]{background:var(--accent);color:var(--on-accent);}
.lw-modus:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.article p.lw-hinweis{font-size:15.5px;color:var(--muted);}
.article .lw-buehne p.lern-lede{font-size:16.5px;}
.lw-buehne .lk-zahl{margin:0 0 10px;}
.article p.lk-tasten{margin:6px 0 0;font-size:13px;color:var(--muted);}
/* Herleitung auf der Karte: Ziel, Ausgangspunkt, Schritte */
.hl-teil{margin:12px 0 0;padding:8px 13px 10px;border-left:3px solid var(--accent);border-radius:0 8px 8px 0;
  background:color-mix(in srgb,var(--accent) 5%,var(--panel));font-size:16.5px;font-weight:400;line-height:1.6;}
.hl-ziel{border-left-color:var(--accent3);background:var(--soft);}
.lk-hinten .hl-teil:first-child{margin-top:0;}
.hl-k{display:block;margin-bottom:2px;font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);}
.article .hl-i p,.article .hl-i li{font-size:16.5px;} .article .hl-i p{margin:.3em 0;}
.hl-i .katex-display{margin:.5em 0;}
/* Quiz und Mischtest */
.qz-setup{display:flex;flex-wrap:wrap;align-items:flex-end;gap:10px 14px;margin:0 0 10px;}
.qz-setup .lw-feld{flex:0 0 130px;}
.qz-setup .lk-um,.mt-fort{width:auto;}
.mt-fort{margin:0 0 14px;}
.article p.qz-kopf{margin:0 0 8px;font-size:13px;font-weight:600;letter-spacing:.02em;color:var(--muted);}
.qz-frage{padding:14px 18px 16px;border:1px solid var(--border);border-top:4px solid var(--accent);border-radius:14px;background:var(--panel);}
.article p.qz-p{margin:0 0 6px;font-size:14px;color:var(--muted);}
.qz-vorne{margin:0 0 12px;font-size:19px;font-weight:600;line-height:1.45;}
.article ol.qz-opt{display:grid;grid-template-columns:minmax(0,1fr);gap:8px;list-style:none;margin:0;padding:0;}
.article .qz-opt li{margin:0;min-width:0;}
.qz-b{display:flex;align-items:flex-start;gap:10px;width:100%;max-width:100%;min-width:0;padding:10px 12px;border:1px solid var(--border);border-radius:10px;background:var(--panel);
  color:var(--ink);font:inherit;font-size:16px;line-height:1.5;text-align:left;cursor:pointer;}
.qz-b:hover:not(:disabled){border-color:var(--accent);}
.qz-b:focus-visible,.mt-b:focus-visible,.ag-zufall:focus-visible{outline:2px solid var(--accent3);outline-offset:2px;}
.qz-b:disabled{cursor:default;}
.qz-nr{flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;margin-top:1px;border-radius:50%;
  background:var(--soft);color:var(--muted);font-size:13px;font-weight:700;}
.qz-a{flex:1;min-width:0;overflow-wrap:anywhere;}
.qz-a .lk-formel .katex-display,.qz-a .katex-display{margin:.1em 0;}
.qz-b.gewaehlt{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent);}
.qz-b.ok{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 8%,var(--panel));color:var(--ink);box-shadow:none;}
.qz-b.ok .qz-nr{background:var(--accent);color:var(--on-accent);}
.qz-b.nein{border-color:var(--accent3);background:var(--soft);color:var(--ink);box-shadow:none;}
.qz-b.nein .qz-nr{background:var(--accent3);color:#fff;}
:root[data-theme="dark"] :is(.qz-frage,.qz-b,.lk-karte){border-color:var(--rahmen);}
:root[data-theme="dark"] .qz-frage{border-top-color:var(--accent);}
:root[data-theme="dark"] .qz-b.ok,:root[data-theme="dark"] .qz-b.gewaehlt{border-color:var(--accent);}
:root[data-theme="dark"] .qz-b.nein{border-color:var(--accent3);}
.qz-weiter{margin-top:12px;}
.article h2.qz-h{margin:.4em 0 .3em;}
.article h3.qz-h3{margin:1.2em 0 .4em;}
.article p.qz-ergebnis{margin:0 0 .6em;font-size:20px;font-weight:700;color:var(--accent);}
.article ol.qz-fehler,.article ol.mt-liste{margin:0 0 1.2em;padding-left:1.5em;}
.article .qz-fehler li{padding:8px 0;border-bottom:1px solid var(--border);}
.qz-fehler .qz-vorne{margin:0 0 4px;font-size:16.5px;}
.qz-deine,.qz-richtig{margin:3px 0;font-size:15.5px;}
.qz-richtig .hl-k{color:var(--accent);} .qz-deine .hl-k{color:var(--accent3);}
.article .mt-liste>li.mt-e{margin:0 0 14px;padding:12px 15px;border:1px solid var(--border);border-left:4px solid var(--border);border-radius:10px;}
:root[data-theme="dark"] .article .mt-liste>li.mt-e{border-color:var(--rahmen);}
.article .mt-liste>li.mt-ok{border-left-color:var(--accent);}
.article .mt-liste>li.mt-teil{border-left-color:color-mix(in srgb,var(--accent3) 50%,var(--border));}
.article .mt-liste>li.mt-nein{border-left-color:var(--accent3);}
.mt-aufg .aufg{margin:0;}
.mt-selbst{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:10px 0 6px;}
.mt-selbst .hl-k{display:inline;margin:0 4px 0 0;}
.mt-b{padding:6px 14px;border:1px solid var(--border);border-radius:999px;background:var(--panel);color:var(--ink);font:inherit;font-size:14.5px;font-weight:600;cursor:pointer;}
.mt-b:hover{border-color:var(--accent);}
.mt-b[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent);}
.article ul.mt-links{margin:0 0 1em;padding-left:1.2em;}
.article .mt-links li{font-size:15.5px;}
.mt-links .hl-k{display:inline;}
/* Aufgabenseite eines Moduls */
.ag-leiste{padding:12px 14px;border:1px solid var(--border);border-radius:12px;background:var(--soft);}
:root[data-theme="dark"] .ag-leiste{border-color:var(--rahmen);}
.ag-leiste .lw-feld{flex:1 1 190px;}
.ag-offen{align-self:center;white-space:nowrap;}
.ag-zufall{padding:7px 14px;border:1px solid var(--accent);border-radius:9px;background:var(--accent);color:var(--on-accent);font:inherit;font-size:15px;
  font-weight:600;cursor:pointer;}
.ag-zufall:hover{filter:brightness(1.08);}
.ag-stand{align-self:center;font-size:14.5px;font-weight:600;color:var(--accent);}
.ag-kap,.ag-art,.ag{scroll-margin-top:72px;}
.article .ag-art>h3{font-size:18px;}
.ag{margin:0 0 18px;}
.ag .aufg{margin-bottom:6px;}
.ag-fuss{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:6px 14px;margin:0 0 4px;font-size:14px;}
.ag-ok{font-weight:600;color:var(--muted);cursor:pointer;}
.ag-geloest .ag-ok{color:var(--accent);}
.ag-hl .aufg{box-shadow:0 0 0 3px color-mix(in srgb,var(--accent3) 55%,transparent);}
.ag-zahl{font-size:.9em;color:var(--muted);}
/* Verweise unter dem Artikel: Lernkarten und Aufgaben */
.bereich-links{margin:1.6em 0 1.1em;padding:9px 16px;border:1px solid var(--border);border-radius:12px;background:var(--soft);}
:root[data-theme="dark"] .bereich-links{border-color:var(--rahmen);}
.article .bereich-links p{margin:.2em 0;font-size:15.5px;}
.bl-k{margin-right:4px;font-weight:700;color:var(--muted);}
@media(max-width:620px){ .lw-modus{padding:7px 12px;font-size:14.5px;} .qz-frage{padding:12px 13px 14px;} .qz-vorne{font-size:17.5px;}
  .lw-feld{flex-basis:100%;} .qz-setup .lw-feld{flex-basis:120px;} }
@media print{ .bereich-links,.lw-app,.ag-leiste,.ag-fuss,.ag-reset,.ag-nav{display:none!important;} }
"""

WISSEN_JS = r"""
var NICHTS={de:"Nichts gefunden für „{q}\".",en:"Nothing found for „{q}\".",es:"Nada encontrado para „{q}\".",zh:"未找到 „{q}\".",
            fr:"Aucun résultat pour «\u00a0{q}\u00a0».",tr:"“{q}” için sonuç bulunamadı."};
// Suche: Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben. Der Kern steht in suche.js (W3a, gemeinsam
// mit der Startseite) und wird erst beim ersten Öffnen geladen; er holt zuerst nur Titel und Abschnitte, den Volltext je
// Modul, sobald gesucht wird (und nur Module, die das Wort enthalten können).
var KATEX_OPT={delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}],strict:false,ignoredClasses:["fb-spaeter","mathe-spaeter"]};   // Formelblatt (W4a): erst beim Öffnen setzen
function mathe(el){ if(window.renderMathInElement) try{ renderMathInElement(el,KATEX_OPT); }catch(e){} }
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var S=null, P=null, sel=-1, rows=[], frage="";
  var LANG=(document.documentElement.lang||"de").slice(0,2);
  function kern(){                                     // suche.js einmal einbinden, Index starten
    if(!P) P=new Promise(function(ok,nein){
      if(window.ETSuche){ ok(); return; }
      var s=document.createElement("script"); s.src="/wissen/assets/suche.js"; s.onload=ok; s.onerror=nein; document.head.appendChild(s);
    }).then(function(){ S=window.ETSuche(LANG); return S.start(); }).catch(function(){ P=null; throw 0; });
    return P;
  }
  function esc(s){ return (s||"").replace(/[&<>]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c];}); }
  function zeigen(raw,res){
    if(raw!==frage) return;                            // inzwischen anders getippt
    results.innerHTML=""; rows=[];
    if(res.q.length<2) return;
    res.hits.slice(0,25).forEach(function(h){ var d=h.d;
      var a=document.createElement("a"); a.href="/wissen/"+d.path+(h.anker?"#"+encodeURIComponent(h.anker):"");
      a.innerHTML='<div class="r-crumb">'+esc(d.crumb)+(h.abschnitt?' › <span class="r-abschnitt">'+esc(h.abschnitt)+'</span>':"")+'</div>'+
                  '<div class="r-title">'+esc(d.klar)+'</div>'+
                  '<div class="r-snip">'+S.snippet(d,res.q)+'</div>';
      results.appendChild(a); rows.push(a);
    });
    if(sel>=rows.length) sel=rows.length-1;
    paintSel();
    if(res.laedt){ var w=document.createElement("div"); w.className="searchHint laedt"; w.textContent=LERNEN.w("suche_volltext"); results.appendChild(w); }
    else if(!rows.length) results.innerHTML='<div class="searchHint">'+esc(NICHTS[LANG]||NICHTS.de).split("{q}").join(esc(raw.trim()))+'</div>';
  }
  function search(raw){
    frage=raw; sel=-1;
    if(S && S.fold(raw.trim()).length<2){ results.innerHTML=""; rows=[]; return; }
    kern().then(function(){ S.suche(raw,function(res){ zeigen(raw,res); }); }).catch(function(){});
  }
  function open(){ if(!overlay) return; overlay.hidden=false; input.value=""; results.innerHTML=""; rows=[]; sel=-1; input.focus();
    kern().catch(function(){}); }
  function close(){ if(overlay) overlay.hidden=true; }
  if(btn) btn.addEventListener("click",open);
  [].forEach.call(document.querySelectorAll("[data-suche]"),function(b){ b.hidden=false; b.addEventListener("click",open); });
  document.addEventListener("keydown",function(e){
    if(e.key==="/" && !/input|textarea|select/i.test((document.activeElement||{}).tagName) && (!overlay||overlay.hidden)){ e.preventDefault(); open(); }
    else if(e.key==="Escape"){ close(); }
    else if(!overlay||overlay.hidden) return;
    else if(e.key==="ArrowDown"){ e.preventDefault(); sel=Math.min(rows.length-1,sel+1); paintSel(); }
    else if(e.key==="ArrowUp"){ e.preventDefault(); sel=Math.max(0,sel-1); paintSel(); }
    else if(e.key==="Enter" && rows[sel]){ location.href=rows[sel].href; }
  });
  function paintSel(){ rows.forEach(function(r,i){ r.classList.toggle("sel",i===sel); }); if(rows[sel]) rows[sel].scrollIntoView({block:"nearest"}); }
  if(input) input.addEventListener("input",function(){ search(input.value); });
  if(overlay) overlay.addEventListener("click",function(e){ if(e.target===overlay) close(); });
})();
// Sprachmenü (build_wissen.lang_switch): Der Knopf öffnet und schließt die Liste. Esc, ein Klick daneben oder Tab aus dem
// Menü schließen sie; Esc bringt den Fokus zurück auf den Knopf. Mit der Tastatur geöffnet (Enter, Leertaste, Pfeil)
// steht der Fokus auf der aktuellen Sprache, Pfeiltasten, Pos1 und Ende wandern durch die übersetzten Sprachen.
(function(){
  var menus=[].slice.call(document.querySelectorAll("[data-langmenu]"));
  function btn(m){ return m.querySelector(".l-toggle"); }
  function list(m){ return m.querySelector(".l-menu"); }
  function links(m){ return [].slice.call(m.querySelectorAll("a.l-item")); }
  function isOpen(m){ var l=list(m); return !!(l && !l.hidden); }
  function close(m, focusBtn){ if(!isOpen(m)) return; list(m).hidden=true; btn(m).setAttribute("aria-expanded","false"); if(focusBtn) btn(m).focus(); }
  function open(m, focus){
    menus.forEach(function(o){ if(o!==m) close(o,false); });
    list(m).hidden=false; btn(m).setAttribute("aria-expanded","true");
    if(focus){ var ls=links(m), t=(focus==="last") ? ls[ls.length-1] : (m.querySelector("a.l-item.on")||ls[0]); if(t) t.focus(); }
  }
  function move(m, d){ var ls=links(m); if(!ls.length) return; var i=ls.indexOf(document.activeElement);
    i=(i<0) ? (d>0 ? 0 : ls.length-1) : (i+d+ls.length)%ls.length; ls[i].focus(); }
  menus.forEach(function(m){
    var b=btn(m), l=list(m); if(!b || !l) return;
    b.addEventListener("click",function(e){ if(isOpen(m)) close(m,false); else open(m, e.detail===0); });   // detail 0: Tastatur
    b.addEventListener("keydown",function(e){
      if(e.key==="ArrowDown"){ e.preventDefault(); open(m,true); }
      else if(e.key==="ArrowUp"){ e.preventDefault(); open(m,"last"); }
    });
    l.addEventListener("keydown",function(e){
      var ls=links(m);
      if(e.key==="ArrowDown"){ e.preventDefault(); move(m,1); }
      else if(e.key==="ArrowUp"){ e.preventDefault(); move(m,-1); }
      else if(e.key==="Home" && ls.length){ e.preventDefault(); ls[0].focus(); }
      else if(e.key==="End" && ls.length){ e.preventDefault(); ls[ls.length-1].focus(); }
    });
    m.addEventListener("focusout",function(e){ if(e.relatedTarget && !m.contains(e.relatedTarget)) close(m,false); });   // Tab hinaus
  });
  document.addEventListener("keydown",function(e){
    if(e.key==="Escape") menus.forEach(function(m){ if(isOpen(m)) close(m, m.contains(document.activeElement)); });
  });
  document.addEventListener("click",function(e){ menus.forEach(function(m){ if(isOpen(m) && !m.contains(e.target)) close(m,false); }); });
  // W4b: „Hell/Dunkel“ im Bereichsmenü (nur sehr schmale Artikelseiten, dort fehlt der Knopf in der Leiste)
  [].forEach.call(document.querySelectorAll(".b-thema-b"),function(b){ b.addEventListener("click",function(){
    var t=document.getElementById("themeBtn"); if(t) t.click(); menus.forEach(function(m){ close(m,false); }); }); });
})();
// Inhaltsverzeichnis: aktuellen Abschnitt beim Scrollen markieren.
(function(){
  var links=[].slice.call(document.querySelectorAll(".toc a")); if(!links.length) return;
  var map=links.map(function(a){ var el=document.getElementById(a.getAttribute("href").slice(1)); return {a:a,el:el}; }).filter(function(x){return x.el;});
  function onScroll(){ var y=window.scrollY+80, cur=map[0];
    map.forEach(function(x){ if(x.el.offsetTop<=y) cur=x; });
    links.forEach(function(a){a.classList.remove("active");}); if(cur) cur.a.classList.add("active");
  }
  window.addEventListener("scroll",onScroll,{passive:true}); onScroll();
})();
// Hell/Dunkel-Umschalter + einklappbare Panels (Fokusmodus) + Mobil-Menü für den Themenbaum.
(function(){
  var root=document.documentElement, layout=document.querySelector(".layout");
  var tb=document.getElementById("themeBtn");
  if(tb) tb.addEventListener("click",function(){
    var dark=root.getAttribute("data-theme")==="dark";          // Wissen-Konvention: dunkel = data-theme="dark"
    if(dark) root.removeAttribute("data-theme"); else root.setAttribute("data-theme","dark");
    try{ localStorage.setItem("animate-theme", dark?"light":"dark"); }catch(e){}   // Schlüssel mit dem Editor geteilt
  });
  // Ohne eigene Wahl folgt die Seite der Systemeinstellung (der Kopf setzt sie beim Laden), auch wenn sie sich ändert.
  var sys=window.matchMedia?window.matchMedia("(prefers-color-scheme: dark)"):null;
  function folge(e){ var s=null; try{ s=localStorage.getItem("animate-theme"); }catch(x){} if(s) return;
    if(e.matches) root.setAttribute("data-theme","dark"); else root.removeAttribute("data-theme"); }
  if(sys){ if(sys.addEventListener) sys.addEventListener("change",folge); else if(sys.addListener) sys.addListener(folge); }
  if(!layout) return;
  var side=layout.querySelector(".side"), mq=window.matchMedia("(max-width:720px)");
  var bL=document.getElementById("toggleLeft"), bR=document.getElementById("toggleRight");
  // Knopffarbe: Panel offen = orange (Klasse is-open), zu = Grundfarbe; aria-pressed folgt „offen".
  function mark(btn,open){ if(btn){ btn.classList.toggle("is-open",!!open); btn.setAttribute("aria-pressed",open?"true":"false"); } }
  function L(k){ try{ return localStorage.getItem(k)==="1"; }catch(e){ return false; } }
  function S(k,v){ try{ localStorage.setItem(k,v?"1":"0"); }catch(e){} }
  // Ist der Themenbaum sichtbar? Mobil ist er ein Overlay, sonst eine Spalte.
  function leftOpen(){
    return mq.matches ? !!(side&&side.classList.contains("open")) : !layout.classList.contains("hide-left"); }
  // Rechts (Gliederung): nur am Desktop sinnvoll, Zustand merken.
  if(bR){ if(L("wissen-hide-right")) layout.classList.add("hide-right");
    mark(bR,!layout.classList.contains("hide-right"));
    bR.addEventListener("click",function(){ var hidden=layout.classList.toggle("hide-right"); mark(bR,!hidden); S("wissen-hide-right",hidden); }); }
  // Links (Themenbaum): Desktop = beim Öffnen IMMER eingeklappt (Toggle gilt nur für die aktuelle Seite); Mobil = Overlay auf/zu.
  if(bL){ if(!mq.matches) layout.classList.add("hide-left");
    mark(bL,leftOpen());
    bL.addEventListener("click",function(){
      if(mq.matches){ if(side) side.classList.toggle("open"); }
      else layout.classList.toggle("hide-left");
      mark(bL,leftOpen());
    });
  }
  // Breitenwechsel aufräumen: Overlay nur mobil, am Desktop wieder eingeklappt.
  (mq.addEventListener?mq.addEventListener.bind(mq,"change"):mq.addListener.bind(mq))(function(e){
    if(e.matches) layout.classList.remove("hide-left");
    else { if(side) side.classList.remove("open"); layout.classList.add("hide-left"); }
    mark(bL,leftOpen());
  });
})();
// Sprung auf einen Anker in einem zugeklappten Kasten (Beispiel, Hintergrund, Herleitung, Lösung …): erst alle umgebenden
// Kästen aufklappen, dann hinscrollen. Gilt für Adressen mit #anker (Link aus einem anderen Artikel, Lesezeichen), für Links
// innerhalb der Seite und für einen zweiten Klick auf denselben Anker (dann gibt es kein hashchange).
(function(){
  var start=null;                                                  // beim Laden aufgeklapptes Ziel
  function zeige(id, immer){
    if(!id) return null;
    try{ id=decodeURIComponent(id); }catch(e){}
    var el=document.getElementById(id); if(!el) return null;
    var auf=false, A=window.ETAnsicht;                             // W4a: Ziel in der gewählten Ansicht versteckt -> „Ausführlich“
    if(A && id==="formelblatt"){ if(A.jetzt()!=="formeln"){ A.setze("formeln",false); auf=true; } }
    else if(A && id==="kurzfassung"){ if(A.jetzt()!=="kurz"){ A.setze("kurz",false); auf=true; } }
    else if(A && A.verborgen(el)){ A.setze("voll",false); auf=true; }
    for(var d=el.parentElement; d; d=d.parentElement){ if(d.tagName==="DETAILS" && !d.open){ d.open=true; auf=true; } }
    if(auf || immer) el.scrollIntoView();
    return auf ? el : null;
  }
  window.addEventListener("hashchange", function(){ zeige(location.hash.slice(1), false); });
  document.addEventListener("click", function(e){
    var a=e.target.closest && e.target.closest('a[href*="#"]'); if(!a) return;
    var u=new URL(a.href, location.href);
    if(u.pathname===location.pathname && u.hash && u.hash===location.hash) zeige(u.hash.slice(1), true);
  });
  function beimLaden(){ start=zeige(location.hash.slice(1), false); }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded", beimLaden); else beimLaden();
  window.addEventListener("load", function(){ if(start) start.scrollIntoView(); });   // nach KaTeX und Bildern stimmt die Lage erst ganz
})();
// KaTeX automatisch rendern; zu breite abgesetzte Formeln danach passend verkleinern (höchstens auf 70 %),
// statt sie abzuschneiden – wichtig auf dem Handy.
(function(){
  function fitMath(){
    var ds=[].slice.call(document.querySelectorAll(".katex-display"));
    ds.forEach(function(d){ d.style.fontSize=""; });
    for(var pass=0;pass<2;pass++){                               // zweiter Durchgang: Skalierung ist nicht ganz linear
      var m=ds.map(function(d){ return [d.clientWidth,d.scrollWidth,parseFloat(getComputedStyle(d).fontSize)]; });
      ds.forEach(function(d,i){ var w=m[i][0],s=m[i][1];          // w=0: eingeklappte Herleitung -> beim Aufklappen
        if(w && s>w+1) d.style.fontSize=(m[i][2]*Math.max(0.7,w/s))+"px"; });
    }
  }
  var t=null; function later(){ clearTimeout(t); t=setTimeout(fitMath,120); }
  window.addEventListener("DOMContentLoaded",function(){
    if(window.renderMathInElement) renderMathInElement(document.body,KATEX_OPT);
    fitMath();
  });
  window.addEventListener("resize",later);
  window.addEventListener("load",fitMath);
  document.addEventListener("toggle",later,true);                  // Herleitung aufgeklappt -> Formeln darin einpassen
})();
// Kopierknopf an Code-Blöcken (Konsole: nur die Eingaben, ohne Prompt), Ankerlink an Überschriften (Klick kopiert die
// Adresse des Abschnitts), Druck: zugeklappte Kästen aufklappen und danach wieder schließen (Lösungen bleiben zu).
(function(){
  var L=(document.documentElement.lang||"de").slice(0,2);
  var W={de:{k:"Kopieren",ok:"Kopiert",link:"Link kopiert"},en:{k:"Copy",ok:"Copied",link:"Link copied"},
    es:{k:"Copiar",ok:"Copiado",link:"Enlace copiado"},zh:{k:"复制",ok:"已复制",link:"链接已复制"},
    fr:{k:"Copier",ok:"Copié",link:"Lien copié"},tr:{k:"Kopyala",ok:"Kopyalandı",link:"Bağlantı kopyalandı"}};
  var w=W[L]||W.en;
  function kopiere(text){
    if(navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function(ok,fehler){ var t=document.createElement("textarea"); t.value=text; t.setAttribute("readonly","");
      t.style.position="fixed"; t.style.opacity="0"; document.body.appendChild(t); t.select();
      try{ if(document.execCommand("copy")) ok(); else fehler(); }catch(e){ fehler(e); } document.body.removeChild(t); });
  }
  function codeText(block){
    var c=block.querySelector("pre code"), t=c?c.textContent:"";
    if(/\bcode-console\b/.test(block.className)){                  // Sitzung: Eingabezeilen ohne $, #, >>>, ..., PS>
      var ein=[]; t.split("\n").forEach(function(z){ var m=/^(?:\$ |# |>>> |\.\.\. |PS> )(.*)$/.exec(z); if(m) ein.push(m[1]); });
      if(ein.length) return ein.join("\n");
    }
    return t.replace(/\n+$/,"");
  }
  [].forEach.call(document.querySelectorAll(".code-block"),function(block){
    var b=document.createElement("button"); b.type="button"; b.className="code-kopie"; b.textContent=w.k;
    var kopf=block.querySelector(".code-kopf"); if(kopf) kopf.appendChild(b); else block.insertBefore(b,block.firstChild);
    b.addEventListener("click",function(){ kopiere(codeText(block)).then(function(){ b.textContent=w.ok; b.classList.add("ok");
      setTimeout(function(){ b.textContent=w.k; b.classList.remove("ok"); },1600); },function(){}); });
  });
  document.addEventListener("click",function(e){
    var a=e.target.closest && e.target.closest("a.h-anker"); if(!a) return;
    kopiere(location.href.split("#")[0]+a.getAttribute("href")).then(function(){ a.setAttribute("data-kopiert",w.link); a.classList.add("kopiert");
      setTimeout(function(){ a.classList.remove("kopiert"); },1800); },function(){});
  });
  var zu=[];
  window.addEventListener("beforeprint",function(){
    zu=[].filter.call(document.querySelectorAll("details:not([open])"),function(d){ return !d.classList.contains("loesung") && !d.closest(".side"); });
    zu.forEach(function(d){ d.open=true; });
  });
  window.addEventListener("afterprint",function(){ zu.forEach(function(d){ d.open=false; }); zu=[]; });
})();
// Abbildung antippen: groß in einem Overlay mit voller Breite. Das Bild bzw. die animierte Fassung samt Spielerleiste wandert
// hinein und beim Schließen zurück an ihren Platz, so laufen Animation und Knöpfe weiter. Schließen: Klick (außer auf den
// Spieler), Esc, Knopf oder Zurück im Browser. Mit der Tastatur: Bild fokussieren (Tab), Enter oder Leertaste.
(function(){
  if(!document.querySelector("figure.abb")) return;
  var L=(document.documentElement.lang||"de").slice(0,2);
  var W={de:["Abbildung vergrößern","Schließen"],en:["Enlarge figure","Close"],es:["Ampliar figura","Cerrar"],zh:["放大图","关闭"],
    fr:["Agrandir la figure","Fermer"],tr:["Şekli büyüt","Kapat"]};
  var w=W[L]||W.en, SEL="figure.abb>img,figure.abb>svg.abb-anim";
  var ov=null, buehne=null, text=null, zuBtn=null, fig=null, platz=null, verlauf=false;
  window.abbVergroesserbar=function(m){ m.setAttribute("tabindex","0"); if(!m.getAttribute("title")) m.setAttribute("title",w[0]); };
  [].forEach.call(document.querySelectorAll(SEL),window.abbVergroesserbar);
  function bauen(){
    ov=document.createElement("div"); ov.className="abb-gross"; ov.hidden=true; ov.setAttribute("role","dialog"); ov.setAttribute("aria-modal","true");
    zuBtn=document.createElement("button"); zuBtn.type="button"; zuBtn.className="ag-zu"; zuBtn.setAttribute("aria-label",w[1]); zuBtn.title=w[1];
    zuBtn.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>';
    buehne=document.createElement("div"); buehne.className="ag-buehne";
    text=document.createElement("div"); text.className="ag-text";
    ov.appendChild(zuBtn); ov.appendChild(buehne); ov.appendChild(text); document.body.appendChild(ov);
    ov.addEventListener("click",function(e){ if(e.target.closest(".abb-spieler")) return; zu(); });
  }
  function auf(f){
    if(fig) return; if(!ov) bauen();
    var teile=[].filter.call(f.children,function(k){ return k.matches(SEL) || k.classList.contains("abb-spieler"); });
    if(!teile.length) return;
    fig=f;
    platz=document.createElement("div"); platz.className="abb-platz";
    platz.style.height=teile.reduce(function(s,k){ return s+k.getBoundingClientRect().height; },0)+"px";
    f.insertBefore(platz,teile[0]);
    teile.forEach(function(k){ buehne.appendChild(k); });
    var cap=f.querySelector("figcaption"); text.innerHTML=cap?cap.innerHTML:"";
    ov.setAttribute("aria-label",(cap && cap.textContent.trim()) || w[0]);
    ov.hidden=false; document.documentElement.classList.add("abb-offen");
    try{ history.pushState({abbGross:1},""); verlauf=true; }catch(e){ verlauf=false; }
    zuBtn.focus();
  }
  function schliessen(){
    if(!fig) return;
    while(buehne.firstChild) fig.insertBefore(buehne.firstChild,platz);
    platz.parentNode.removeChild(platz);
    ov.hidden=true; document.documentElement.classList.remove("abb-offen"); text.innerHTML="";
    var m=fig.querySelector(SEL); fig=null; platz=null;
    if(m) try{ m.focus({preventScroll:true}); }catch(e){}
  }
  function zu(){ if(!fig) return; if(verlauf){ verlauf=false; history.back(); } else schliessen(); }
  window.addEventListener("popstate",function(){ if(fig){ verlauf=false; schliessen(); } });
  document.addEventListener("click",function(e){
    var m=e.target.closest && e.target.closest(SEL); if(!m || (ov && ov.contains(m))) return;
    auf(m.parentNode);
  });
  document.addEventListener("keydown",function(e){
    if(fig){
      if(e.key==="Escape"){ e.preventDefault(); zu(); }
      else if(e.key==="Tab"){                                    // Fokus bleibt im Overlay
        var f=[].slice.call(ov.querySelectorAll("button,input,a[href]")); if(!f.length) return;
        var i=f.indexOf(document.activeElement);
        if(e.shiftKey && i<=0){ e.preventDefault(); f[f.length-1].focus(); }
        else if(!e.shiftKey && (i<0 || i===f.length-1)){ e.preventDefault(); f[0].focus(); }
      }
      return;
    }
    var t=e.target; if(t && t.matches && t.matches(SEL) && (e.key==="Enter" || e.key===" ")){ e.preventDefault(); auf(t.parentNode); }
  });
})();
/* Fassung (kompakt | ausführlich): Wahl merken; Themen-Links (Baum, Nachbarn, Übersicht) führen dann zur gewählten
   Fassung desselben Themas, soweit es sie gibt (data-alt). */
(function(){
  function get(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function set(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  document.addEventListener("click",function(ev){
    var f=ev.target.closest&&ev.target.closest(".fassung .f-btn");
    if(f) set("wissen-fassung",f.getAttribute("data-fassung"));
  });
  function apply(){
    if(get("wissen-fassung")!=="ausfuehrlich") return;
    document.querySelectorAll("a[data-alt]").forEach(function(a){ a.setAttribute("href",a.getAttribute("data-alt")); });
  }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",apply); else apply();
})();
/* Animierte Abbildungen: figure.abb[data-anim] = Adresse der Datei <szene>.anim.svg (tools/szenen_animation.py). Sie ist
   das Endbild plus Datenblock <metadata class="szenen-animation">; der Spieler setzt sie an die Stelle des Bilds und
   bewegt die Elemente mit data-a. Start, wenn die Abbildung ins Bild kommt (in zugeklappten Kästen also erst beim
   Aufklappen), Halt, wenn sie es verlässt; bei „Bewegung reduzieren“ kein Selbststart (Endbild). Ohne Skript, ohne
   Datei oder bei einem Fehler bleibt das statische Bild. */
(function(){
  var figs=[].slice.call(document.querySelectorAll("figure.abb[data-anim]"));
  if(!figs.length || !window.fetch || !window.DOMParser || !window.IntersectionObserver) return;
  var L=(document.documentElement.lang||"de").slice(0,2);
  var TX={de:{play:"Abspielen",pause:"Anhalten",neu:"Von vorn",zur:"Schritt zurück",vor:"Schritt vor",zeit:"Zeitleiste der Animation",von:"von",anim:"Animation"},
    en:{play:"Play",pause:"Pause",neu:"Restart",zur:"Previous step",vor:"Next step",zeit:"Animation timeline",von:"of",anim:"Animation"},
    es:{play:"Reproducir",pause:"Pausa",neu:"Reiniciar",zur:"Paso anterior",vor:"Paso siguiente",zeit:"Línea de tiempo de la animación",von:"de",anim:"Animación"},
    zh:{play:"播放",pause:"暂停",neu:"重新开始",zur:"上一步",vor:"下一步",zeit:"动画时间轴",von:"/",anim:"动画"},
    fr:{play:"Lire",pause:"Pause",neu:"Recommencer",zur:"Étape précédente",vor:"Étape suivante",zeit:"Chronologie de l’animation",von:"sur",anim:"Animation"},
    tr:{play:"Oynat",pause:"Duraklat",neu:"Baştan başlat",zur:"Önceki adım",vor:"Sonraki adım",zeit:"Animasyon zaman çizelgesi",von:"/",anim:"Animasyon"}};
  var tx=TX[L]||TX.en;
  var reduce=window.matchMedia?window.matchMedia("(prefers-reduced-motion: reduce)"):{matches:false};
  var ICON={play:'<path d="M5 3.5v13l11-6.5z"/>',pause:'<path d="M4.5 3.5h4v13h-4zM11.5 3.5h4v13h-4z"/>',
    neu:'<path d="M10 3.2a6.8 6.8 0 1 1-6.6 8.4h2.1A4.8 4.8 0 1 0 10 5.2v2.6L5.8 4.2 10 .6z"/>',
    zur:'<path d="M3.5 3.5h2.2v13H3.5zM16.5 3.5v13L7 10z"/>',vor:'<path d="M14.3 3.5h2.2v13h-2.2zM3.5 3.5v13L13 10z"/>'};
  function knopf(cls,ic,lab){ var b=document.createElement("button"); b.type="button"; b.className=cls; b.setAttribute("aria-label",lab); b.title=lab;
    b.innerHTML='<svg viewBox="0 0 20 20" aria-hidden="true">'+ICON[ic]+'</svg>'; return b; }
  function zahl(t){ var s=(Math.round(t*10)/10).toFixed(1); return (L==="en"||L==="zh")?s:s.replace(".",","); }
  // Wert einer Spur [k0,v0,k1,v1,…] im (gebrochenen) Bild f: Stufe = letzter Wert davor, sonst linear
  function such(tr,f){ var n=tr.length>>1, lo=0, hi=n-1;
    if(f<=tr[0]) return [0,0,0]; if(f>=tr[2*hi]) return [hi,hi,0];
    while(hi-lo>1){ var m=(lo+hi)>>1; if(tr[2*m]<=f) lo=m; else hi=m; }
    return [lo,hi,(f-tr[2*lo])/(tr[2*hi]-tr[2*lo])]; }
  function stufe(tr,f){ return tr[2*such(tr,f)[0]+1]; }
  function linear(tr,f){ var s=such(tr,f), a=tr[2*s[0]+1], b=tr[2*s[1]+1], w=s[2];
    if(typeof a==="number") return a+(b-a)*w;
    var o=[]; for(var i=0;i<a.length;i++) o.push(a[i]+(b[i]-a[i])*w); return o; }
  function r(v,n){ var p=Math.pow(10,n); return Math.round(v*p)/p; }
  function mische(a,b,w){ var o=new Array(a.length); for(var i=0;i<a.length;i++) o[i]=a[i]+(b[i]-a[i])*w; return o; }
  function pfad(v,qc){ var o="", i=0;                    // Bézier-Kette(n) wie engine/svg_painter: M p0 C p1 p2 p3 …
    for(var c=0;c<qc.length;c++){ var n=qc[c];
      if(n){ o+="M"+r(v[2*i],1)+" "+r(v[2*i+1],1);
        for(var k=1;k<n-2;k+=3){ var j=2*(i+k); o+="C"+r(v[j],1)+" "+r(v[j+1],1)+" "+r(v[j+2],1)+" "+r(v[j+3],1)+" "+r(v[j+4],1)+" "+r(v[j+5],1); } }
      i+=n; }
    return o; }
  function rgb(c){ return "rgb("+Math.round(c[0])+","+Math.round(c[1])+","+Math.round(c[2])+")"; }
  function setze(el,cache,name,v){ if(cache[name]===v) return; cache[name]=v; if(v===null) el.removeAttribute(name); else el.setAttribute(name,v); }
  function texte(el){ return el.tagName.toLowerCase()==="g"?[].slice.call(el.querySelectorAll("text")):[el]; }
  // Kamerafahrt in 3D (L4): Die Datei trägt je Element Weltpunkte (w; wl = nur Ecken gerader Stücke) und eine
  // Kamera-Spur cam [theta, phi, zoom, Blickpunkt]; projiziert wird wie engine/camera.py (z oben, orthografisch),
  // gezeichnet von hinten nach vorn wie engine/renderer (Tiefe = Mittel aller Punkte, Achsen bei top zuletzt).
  function kamera(c){ var ct=Math.cos(c[0]), st=Math.sin(c[0]), ce=Math.cos(c[1]), se=Math.sin(c[1]);
    var cam=[ce*ct,ce*st,se], fw=[-cam[0],-cam[1],-cam[2]], rt=[fw[1],-fw[0],0], n=Math.sqrt(rt[0]*rt[0]+rt[1]*rt[1]);
    rt=n>1e-9?[rt[0]/n,rt[1]/n,0]:[1,0,0];
    var up=[rt[1]*fw[2]-rt[2]*fw[1],rt[2]*fw[0]-rt[0]*fw[2],rt[0]*fw[1]-rt[1]*fw[0]], m=Math.sqrt(up[0]*up[0]+up[1]*up[1]+up[2]*up[2]);
    return {r:rt,u:[up[0]/m,up[1]/m,up[2]/m],c:cam,z:c[2],o:[c[3],c[4],c[5]]}; }
  function gerade(w){ var o=[w[0],w[1],w[2]];
    for(var i=3;i<w.length;i+=3){ for(var k=1;k<=3;k++){ var q=k/3; o.push(w[i-3]+(w[i]-w[i-3])*q,w[i-2]+(w[i+1]-w[i-2])*q,w[i-1]+(w[i+2]-w[i-1])*q); } }
    return o; }
  function punkte3(e,tr,f){ if(!e._w) e._w=tr.wl?gerade(tr.w):tr.w;
    if(tr.Q){ var s=such(tr.Q,f), a=tr.Q[2*s[0]+1], b=tr.Q[2*s[1]+1]; if(a===null) return e._w; if(b===null||s[2]===0) return a; return mische(a,b,s[2]); }
    if(tr.D){ var d=stufe(tr.D,f); return d===null?e._w:d; }
    return e._w; }
  function drehe(P,K){ var n=P.length/3-1, cx=P[3*n], cy=P[3*n+1], cz=P[3*n+2], o=new Array(3*n);   // bb: Scheibe zur Kamera
    for(var i=0;i<n;i++){ var dx=P[3*i]-cx, dy=P[3*i+1]-cy;
      o[3*i]=cx+dx*K.r[0]+dy*K.u[0]; o[3*i+1]=cy+dx*K.r[1]+dy*K.u[1]; o[3*i+2]=cz+dx*K.r[2]+dy*K.u[2]; }
    return o; }
  function projiziere(P,K,pj){ var n=P.length/3, o=new Array(2*n), s=K.z/pj[2], W2=pj[0]/2, H2=pj[1]/2, t=0;
    for(var i=0;i<n;i++){ var x=P[3*i]-K.o[0], y=P[3*i+1]-K.o[1], z=P[3*i+2]-K.o[2];
      o[2*i]=W2+(K.r[0]*x+K.r[1]*y+K.r[2]*z)*s; o[2*i+1]=H2-(K.u[0]*x+K.u[1]*y+K.u[2]*z)*s; t+=K.c[0]*x+K.c[1]*y+K.c[2]*z; }
    o.tiefe=n?t/n:0; return o; }

  function Spieler(fig){
    this.fig=fig; this.img=fig.querySelector("img"); this.t=0; this.lauf=false; this.gestartet=false; this.nutzer=false; this.auto=false;
  }
  Spieler.prototype.laden=function(){
    var sp=this; if(sp.ladung) return sp.ladung;
    sp.ladung=fetch(sp.fig.getAttribute("data-anim")).then(function(r){ if(!r.ok) throw new Error(r.status); return r.text(); }).then(function(txt){
      var doc=new DOMParser().parseFromString(txt,"image/svg+xml"), svg=doc.documentElement;
      var meta=svg&&svg.getElementsByTagName("metadata")[0];
      if(!svg || svg.nodeName!=="svg" || !meta) throw new Error("kein animiertes SVG");
      var D=JSON.parse(meta.textContent); meta.parentNode.removeChild(meta);
      svg=document.importNode(svg,true);
      var w=svg.getAttribute("width"), h=svg.getAttribute("height");
      svg.setAttribute("class","abb-anim"); svg.setAttribute("role","img");
      svg.setAttribute("aria-label",(sp.img&&sp.img.getAttribute("alt"))||tx.anim);
      svg.style.aspectRatio=w+" / "+h;
      sp.D=D; sp.dauer=D.dauer; sp.N=D.bilder; sp.svg=svg; sp.el=[]; sp.cache=[];
      var nodes=svg.querySelectorAll("[data-a]");
      for(var i=0;i<nodes.length;i++){ var e=nodes[i], k=+e.getAttribute("data-a"); sp.el[k]=e; sp.cache[k]={};
        e._d0=e.getAttribute("d"); e._h0=e.innerHTML; }
      if(sp.img) sp.img.parentNode.replaceChild(svg,sp.img); else sp.fig.insertBefore(svg,sp.fig.firstChild);
      if(window.abbVergroesserbar) window.abbVergroesserbar(svg);  // antippen zum Vergrößern wie beim Bild
      sp.leiste();
      sp.zeige(sp.dauer);                                // bis zum Abspielen das Endbild (kein fast leeres Startbild)
      return sp;
    });
    sp.ladung.catch(function(){});                       // Fehler: das statische Bild bleibt stehen
    return sp.ladung;
  };
  Spieler.prototype.leiste=function(){
    var sp=this, bar=document.createElement("div"); bar.className="abb-spieler"; bar.setAttribute("role","group"); bar.setAttribute("aria-label",tx.anim);
    sp.bPlay=knopf("as-play","play",tx.play); sp.bNeu=knopf("as-neu","neu",tx.neu);
    bar.appendChild(sp.bPlay); bar.appendChild(sp.bNeu);
    var marken=(sp.D.marken||[]).filter(function(m){ return m>0 && m<sp.dauer; });
    sp.marken=marken;
    if(marken.length){ sp.bZur=knopf("as-zur","zur",tx.zur); sp.bVor=knopf("as-vor","vor",tx.vor); bar.appendChild(sp.bZur); bar.appendChild(sp.bVor); }
    var box=document.createElement("div"); box.className="as-leiste";
    var rg=document.createElement("input"); rg.type="range"; rg.min="0"; rg.max=String(sp.N); rg.step="1"; rg.value="0"; rg.setAttribute("aria-label",tx.zeit);
    box.appendChild(rg);
    marken.forEach(function(m){ var s=document.createElement("span"); s.className="as-marke"; s.style.left="calc(7px + (100% - 14px) * "+(m/sp.dauer).toFixed(4)+")"; box.appendChild(s); });
    bar.appendChild(box);
    sp.zeit=document.createElement("span"); sp.zeit.className="as-zeit"; sp.zeit.setAttribute("aria-hidden","true"); bar.appendChild(sp.zeit);
    sp.rg=rg; sp.svg.parentNode.insertBefore(bar,sp.svg.nextSibling);
    sp.bPlay.addEventListener("click",function(){ if(sp.lauf){ sp.nutzer=true; sp.halt(); } else { sp.nutzer=false; sp.spiel(sp.t>=sp.dauer-1e-3?0:sp.t); } });
    sp.bNeu.addEventListener("click",function(){ sp.nutzer=false; sp.spiel(0); });
    if(sp.bZur){
      sp.bZur.addEventListener("click",function(){ var z=0; for(var i=0;i<marken.length;i++) if(marken[i]<sp.t-0.15) z=marken[i]; sp.nutzer=true; sp.halt(); sp.zeige(z); });
      sp.bVor.addEventListener("click",function(){ var z=sp.dauer; for(var i=marken.length-1;i>=0;i--) if(marken[i]>sp.t+0.05) z=marken[i]; sp.nutzer=true; sp.halt(); sp.zeige(z); });
    }
    rg.addEventListener("input",function(){ sp.nutzer=true; sp.halt(); sp.zeige(sp.dauer*(+rg.value)/sp.N); });
  };
  Spieler.prototype.zeige=function(t){
    var sp=this; t=Math.max(0,Math.min(sp.dauer,t)); sp.t=t;
    var f=sp.N*t/sp.dauer, data=sp.D.el, K=sp.D.pj?kamera(linear(sp.D.cam,f)):null;
    for(var k=0;k<data.length;k++){
      var e=sp.el[k], tr=data[k], c=sp.cache[k]; if(!e) continue;
      if(tr.v) setze(e,c,"display",stufe(tr.v,f)?null:"none");
      if(tr.h){ var hh=stufe(tr.h,f); if(c.h!==hh){ c.h=hh; e.innerHTML=hh===null?e._h0:hh; c.fo=c.fc=undefined; c.kinder=null; } }
      if(K && tr.w){ var P3=punkte3(e,tr,f), o3=projiziere(tr.bb?drehe(P3,K):P3,K,sp.D.pj); e._tiefe=o3.tiefe;
        if(tr.b){ var s3=tr.s?linear(tr.s,f):1, x3=o3[0]-s3*tr.b[0], y3=o3[1]-s3*tr.b[1];
          setze(e,c,"transform",(Math.abs(s3-1)<1e-4&&Math.abs(x3)<0.005&&Math.abs(y3)<0.005)?null:
            "matrix("+r(s3,4)+" 0 0 "+r(s3,4)+" "+r(x3,2)+" "+r(y3,2)+")"); }
        else setze(e,c,"d",pfad(o3,(tr.wc&&!tr.D)?tr.wc:[o3.length>>1])); }
      if(tr.d){ var d=stufe(tr.d,f); setze(e,c,"d",d===null?e._d0:d); }
      if(tr.q){ var s=such(tr.q,f), qa=tr.q[2*s[0]+1], qb=tr.q[2*s[1]+1];   // Punkte wandern (Umformen): linear
        setze(e,c,"d",qa===null?e._d0:pfad((qb===null||s[2]===0)?qa:mische(qa,qb,s[2]),tr.qc)); }
      if(tr.m){ var m=linear(tr.m,f);
        setze(e,c,"transform",(Math.abs(m[0]-1)+Math.abs(m[1])+Math.abs(m[2])+Math.abs(m[3]-1)+Math.abs(m[4])+Math.abs(m[5])<1e-4)?null:
          "matrix("+r(m[0],4)+" "+r(m[1],4)+" "+r(m[2],4)+" "+r(m[3],4)+" "+r(m[4],2)+" "+r(m[5],2)+")"); }
      if(tr.p){ var p=linear(tr.p,f);
        setze(e,c,"stroke-dasharray",(p[0]<0.05&&p[1]>999.95)?null:(p[0]<0.05?r(p[1],2)+" 2000":"0 "+r(p[0],2)+" "+r(p[1],2)+" 2000")); }
      if(tr.so) setze(e,c,"stroke-opacity",String(r(linear(tr.so,f),3)));
      if(tr.sw) setze(e,c,"stroke-width",String(r(linear(tr.sw,f),2)));
      if(tr.sc) setze(e,c,"stroke",rgb(linear(tr.sc,f)));
      if(tr.fo||tr.fc){
        var ziele=(e.tagName.toLowerCase()==="g")?(c.kinder||(c.kinder=texte(e))):[e];
        var fo=tr.fo?String(r(linear(tr.fo,f),3)):null, fc=tr.fc?rgb(linear(tr.fc,f)):null;
        for(var j=0;j<ziele.length;j++){ var cc=ziele[j]===e?c:(ziele[j]._c||(ziele[j]._c={}));
          if(fo!==null) setze(ziele[j],cc,"fill-opacity",fo); if(fc!==null) setze(ziele[j],cc,"fill",fc); }
      }
    }
    if(K){ var top=sp.D.top, li=[];                     // Maler-Algorithmus: hinten zuerst, bei Gleichstand der Rang r
      for(var k2=0;k2<data.length;k2++) if(sp.el[k2]&&data[k2].w) li.push(k2);
      li.sort(function(a,b){ var A=data[a], B=data[b], ga=(top&&A.ax)?1:0, gb=(top&&B.ax)?1:0;
        if(ga!==gb) return ga-gb; if((A.ly||0)!==(B.ly||0)) return (A.ly||0)-(B.ly||0);
        var dd=sp.el[a]._tiefe-sp.el[b]._tiefe; return dd?dd:A.r-B.r; });
      var reihe=li.join(",");
      if(li.length && reihe!==sp.reihe){ sp.reihe=reihe; var par=sp.el[li[0]].parentNode;
        for(var i2=0;i2<li.length;i2++) par.appendChild(sp.el[li[i2]]); } }
    if(sp.rg){ sp.rg.value=String(Math.round(f)); sp.rg.style.setProperty("--as-p",(100*t/sp.dauer).toFixed(2)+"%");
      var txt=zahl(t)+" "+tx.von+" "+zahl(sp.dauer)+" s"; sp.rg.setAttribute("aria-valuetext",txt); sp.zeit.textContent=zahl(t)+" / "+zahl(sp.dauer)+" s"; }
  };
  Spieler.prototype.spiel=function(ab){
    var sp=this; if(!sp.D) return;
    if(ab!=null) sp.zeige(ab);
    sp.lauf=true; sp.gestartet=true; sp.auto=false; sp.knopf();
    var t0=performance.now(), s0=sp.t;
    function tick(now){ if(!sp.lauf) return;
      var t=s0+(now-t0)/1000; if(t>=sp.dauer){ sp.zeige(sp.dauer); sp.lauf=false; sp.knopf(); return; }
      sp.zeige(t); sp.raf=requestAnimationFrame(tick); }
    sp.raf=requestAnimationFrame(tick);
  };
  Spieler.prototype.halt=function(){ this.lauf=false; if(this.raf) cancelAnimationFrame(this.raf); this.knopf(); };
  Spieler.prototype.knopf=function(){ var b=this.bPlay; if(!b) return; var l=this.lauf?tx.pause:tx.play;
    b.setAttribute("aria-label",l); b.title=l; b.innerHTML='<svg viewBox="0 0 20 20" aria-hidden="true">'+ICON[this.lauf?"pause":"play"]+'</svg>'; };
  Spieler.prototype.sichtbar=function(ja){
    var sp=this; if(!sp.D) return; sp.imBild=ja;
    if(ja){ if(reduce.matches || sp.nutzer || document.hidden) return;
      if(!sp.gestartet) sp.spiel(0); else if(sp.auto){ sp.spiel(); } }
    else if(sp.lauf){ sp.halt(); sp.auto=true; }
  };
  var spieler=figs.map(function(f){ return new Spieler(f); });
  var nah=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ var sp=e.target._sp; nah.unobserve(e.target);
      sp.laden().then(function(){ seh.observe(sp.fig); }); } }); },{rootMargin:"400px 0px"});
  var seh=new IntersectionObserver(function(es){ es.forEach(function(e){ e.target._sp.sichtbar(e.isIntersecting && e.intersectionRatio>=0.35); }); },{threshold:[0,0.35,0.6]});
  spieler.forEach(function(sp){ sp.fig._sp=sp; nah.observe(sp.fig); });
  document.addEventListener("visibilitychange",function(){ spieler.forEach(function(sp){        // Tab im Hintergrund: anhalten
    if(document.hidden){ if(sp.lauf){ sp.halt(); sp.auto=true; } } else if(sp.imBild) sp.sichtbar(true); }); });
  window.addEventListener("beforeprint",function(){ spieler.forEach(function(sp){ if(sp.D){ if(sp.lauf){ sp.halt(); sp.auto=true; } sp.zeige(sp.dauer); } }); });   // Druck: Endbild
})();
/* ---------- Lernen (W2, 11.11.2026): Lesefortschritt, Link-Vorschau, Selbsttest, Begriffe-Filter, Lernkarten ----------
   Alles bleibt in diesem Browser (localStorage), nichts wird übertragen. Ohne Speicher (privates Fenster, gesperrt) gilt
   es nur, solange die Seite offen ist; Fehler beim Lesen und Schreiben werden abgefangen. Wörter: _UI_LERNEN im Build. */
var LERNEN_UI=/*UI_LERNEN*/{};
var LERNEN=(function(){
  var L=(document.documentElement.lang||"de").slice(0,2), W=LERNEN_UI[L]||{}, D=LERNEN_UI.de||{}, ok=false, mem={};
  try{ localStorage.setItem("etundso-probe","1"); localStorage.removeItem("etundso-probe"); ok=true; }catch(e){}
  function get(k,d){ var v=null;
    if(ok){ try{ v=localStorage.getItem(k); }catch(e){ v=null; } }
    if(v==null && Object.prototype.hasOwnProperty.call(mem,k)) v=mem[k];
    if(v==null) return d;
    try{ var x=JSON.parse(v); return (x==null || typeof x!==typeof d || Array.isArray(x)!==Array.isArray(d)) ? d : x; }catch(e){ return d; } }
  function set(k,v){ var s=JSON.stringify(v); mem[k]=s; if(ok){ try{ localStorage.setItem(k,s); }catch(e){} } }
  function del(k){ delete mem[k]; if(ok){ try{ localStorage.removeItem(k); }catch(e){} } }
  function w(k,o){ var s=W[k]||D[k]||""; if(o) for(var x in o) s=s.split("{"+x+"}").join(o[x]); return s; }
  function pfad(h){ try{ return new URL(h,location.href).pathname; }catch(e){ return h||""; } }
  function el(tag,cls,text){ var e=document.createElement(tag); if(cls) e.className=cls; if(text!=null) e.textContent=text; return e; }
  // Zurücksetzen in zwei Schritten: Der erste Klick fragt („Wirklich zurücksetzen?“), ein zweiter binnen 5 s führt aus.
  function sicher(btn,tun){ var t=null, text=btn.textContent;
    function zurueck(){ clearTimeout(t); btn.classList.remove("frage"); btn.textContent=text; }
    btn.addEventListener("click",function(){
      if(btn.classList.contains("frage")){ zurueck(); tun(); return; }
      btn.classList.add("frage"); btn.textContent=w("reset_sicher"); t=setTimeout(zurueck,5000); }); }
  return {lang:L, ok:ok, get:get, set:set, del:del, w:w, pfad:pfad, el:el, sicher:sicher};
})();
// Seitenleiste (W3a): Im HTML stehen nur Bereich (offen) und Gruppen (zu). Beim ersten Aufklappen einer Gruppe holt
// dieser Teil den Baum der Sprache (data/tree*.json; einmal je Seite, danach aus dem Zwischenspeicher des Browsers) und
// setzt Module, Kapitel und Themen ein, wie sie früher im HTML standen: alles zugeklappt, der aktive Artikel markiert.
// Danach meldet er „etundso-baum“; der Lesefortschritt malt dann Häkchen und „N/M“ auch in den neuen Zeilen.
(function(){
  var $=LERNEN, side=document.querySelector(".side[data-baum-url]"); if(!side) return;
  var P=null, aktiv=side.getAttribute("data-aktiv")||"";
  var lang=($.lang==="de"?"":$.lang+"/"), fassung=null;
  try{ fassung=localStorage.getItem("wissen-fassung"); }catch(e){}
  function laden(){ if(!P) P=fetch(side.getAttribute("data-baum-url")).then(function(r){ if(!r.ok) throw r.status; return r.json(); })
    .catch(function(e){ P=null; throw e; }); return P; }
  function knoten(nd,tiefe){                          // wie build_wissen.sidebar_html vor W3a
    var d=$.el("details","lvl lvl"+tiefe), s=$.el("summary",null,nd.name); d.appendChild(s); inhalt(d,nd,tiefe); return d; }
  function inhalt(d,nd,tiefe){
    if(nd.mp){ var z=$.el("div","side-lernen"), a1=$.el("a",null,$.w("begriffe")||"Begriffe"), a2=$.el("a",null,$.w("lernkarten")||"Lernkarten"),
        a3=$.el("a",null,nd.ref?$.w("fb_titel_ref"):($.w("ans_formeln")||"Formeln"));   // W4a: Informatik: Befehlsübersicht
      a1.href="/wissen/"+nd.mp+"/begriffe.html"; a2.href="/lernen/"+lang+"?m="+nd.m; a3.href="/wissen/"+nd.mp+(nd.ref?"/uebersicht.html":"/formeln.html");
      [a1,a2,a3].forEach(function(a,i){ if(i){ var p=$.el("span",null," · "); p.setAttribute("aria-hidden","true"); z.appendChild(p); } z.appendChild(a); });
      d.appendChild(z); }
    if(nd.articles && nd.articles.length){ var ul=$.el("ul");
      nd.articles.forEach(function(x){ var li=$.el("li"), a=$.el("a",null,x.kurz||x.title), p="/wissen/"+x.path;
        a.href=(x.alt && fassung==="ausfuehrlich")?"/wissen/"+x.alt:p; a.setAttribute("data-lf",p);
        if(x.alt) a.setAttribute("data-alt","/wissen/"+x.alt);
        if(p===aktiv){ a.className="active"; a.setAttribute("aria-current","page"); }
        li.appendChild(a); ul.appendChild(li); });
      d.appendChild(ul); }
    (nd.children||[]).forEach(function(c){ d.appendChild(knoten(c,tiefe+1)); });
  }
  function fuellen(d){
    if(d.getAttribute("data-gefuellt")) return;
    var ix=d.getAttribute("data-baum").split(".").map(Number), mehr=d.querySelector(".side-mehr");
    var warte=$.el("span","baum-hinweis",$.w("baum_laedt")); d.appendChild(warte);
    laden().then(function(baum){
      var b=baum[ix[0]], nd=b&&b.children&&b.children[ix[1]];
      if(!nd || nd.name!==d.firstElementChild.firstChild.nodeValue) throw 0;   // Baum passt nicht zur Seite (anderer Stand)
      d.removeChild(warte); if(mehr) d.removeChild(mehr);
      inhalt(d,nd,1); d.setAttribute("data-gefuellt","1"); mathe(d);
      document.dispatchEvent(new CustomEvent("etundso-baum"));
    }).catch(function(){ warte.textContent=$.w("baum_fehler"); setTimeout(function(){ if(warte.parentNode) d.removeChild(warte); },4000); });
  }
  [].forEach.call(side.querySelectorAll("details[data-baum]"),function(d){
    d.addEventListener("toggle",function(){ if(d.open) fuellen(d); });
    if(d.open) fuellen(d);
  });
  function vorab(){ laden().catch(function(){}); }    // Leiste in Sicht oder unter dem Zeiger: Baum schon einmal holen
  side.addEventListener("pointerenter",vorab,{once:true}); side.addEventListener("focusin",vorab,{once:true});
  var bL=document.getElementById("toggleLeft"); if(bL) bL.addEventListener("click",vorab,{once:true});
})();
// Lesefortschritt: Ein Artikel gilt als gelesen, wenn seine Zusammenfassung (sonst sein Ende) 1 s lang sichtbar war.
// Häkchen in der Seitenleiste und in der Übersicht, „N/M“ an Kapiteln, Balken je Kapitel in der Übersicht, Zeile am
// Artikelende, „Weiterlesen“ (zuletzt geöffnet, nicht gelesen) auf der Übersicht, Knopf „Fortschritt zurücksetzen“.
(function(){
  var $=LERNEN, G="etundso-gelesen", V="etundso-verlauf";
  // Adresse jedes Themen-Links festhalten, bevor „Fassung“ ihn auf die ausführliche Fassung umlenkt (data-alt)
  [].forEach.call(document.querySelectorAll(".side li a, .theme-card a"),function(a){ a.setAttribute("data-lf",$.pfad(a.getAttribute("href"))); });
  function gelesen(){ return $.get(G,{}); }
  function zahl(as,g){ var n=0; as.forEach(function(a){ if(g[a.getAttribute("data-lf")]) n++; }); return n; }
  function balken(n,m){ var d=$.el("div","lf-balken"), s=$.el("span");
    d.setAttribute("role","progressbar"); d.setAttribute("aria-valuemin","0"); d.setAttribute("aria-valuemax",String(m));
    d.setAttribute("aria-valuenow",String(n)); d.setAttribute("aria-label",$.w("lf_kapitel",{n:n,m:m}));
    s.style.width=(m?Math.round(100*n/m):0)+"%"; d.appendChild(s); return d; }
  // Artikel: Adresse, Kapitelname und Themen des Kapitels stehen an der Seitenleiste (W3a: deren Kapitel lädt erst beim Aufklappen)
  var art=document.querySelector("main.article > article"), side=document.querySelector(".side"), aktiv=document.querySelector(".side li a.active");
  var key=(side&&side.getAttribute("data-aktiv"))||(aktiv?aktiv.getAttribute("data-lf"):null);
  var kapitel=((side&&side.getAttribute("data-kap"))||"").split(" ").filter(Boolean).map(function(p){ return "/wissen/"+p; });
  function malen(){
    var g=gelesen();
    [].forEach.call(document.querySelectorAll("a[data-lf]"),function(a){
      var on=!!g[a.getAttribute("data-lf")], sr=a.querySelector(".lf-sr");
      a.classList.toggle("gelesen",on);
      if(on && !sr) a.appendChild($.el("span","lf-sr"," ("+$.w("gelesen")+")"));
      if(!on && sr) a.removeChild(sr); });
    [].forEach.call(document.querySelectorAll(".side details, details.mk-kap"),function(d){   // Kapitel (Leiste, Modulkarte): „5/12“
      var ul=null; for(var c=d.firstElementChild;c;c=c.nextElementSibling){
        if(c.tagName==="UL"){ ul=c; break; } if(c.classList.contains("theme-card")){ ul=c.querySelector("ul"); break; } }
      var s=d.firstElementChild; if(!ul || !s || s.tagName!=="SUMMARY") return;
      var as=[].slice.call(ul.querySelectorAll("a[data-lf]")), n=zahl(as,g), z=s.querySelector(".lf-z");
      if(!n){ if(z) s.removeChild(z); return; }
      if(!z){ z=$.el("span","lf-z"); s.appendChild(z); }
      z.textContent=n+"/"+as.length; z.title=$.w("lf_kapitel",{n:n,m:as.length}); });
    [].forEach.call(document.querySelectorAll(".theme-card"),function(c){         // Übersicht: Balken je Kapitel
      var as=[].slice.call(c.querySelectorAll("a[data-lf]")), n=zahl(as,g), alt=c.querySelector(".lf-kap");
      if(alt) c.removeChild(alt);
      if(!n) return;
      var box=$.el("div","lf-kap"); box.appendChild(balken(n,as.length)); box.appendChild($.el("span","lf-text",$.w("lf_kapitel",{n:n,m:as.length})));
      c.insertBefore(box,c.firstChild); });
    [].forEach.call(document.querySelectorAll(".mk"),function(k){                // Übersicht: Balken je Modulkarte
      var as=[].slice.call(k.querySelectorAll("a[data-lf]")), n=zahl(as,g), f=k.querySelector(".mk-lf");
      if(!f) return; f.innerHTML="";
      if(n){ f.appendChild(balken(n,as.length)); f.appendChild($.el("span","lf-text",$.w("lf_kapitel",{n:n,m:as.length}))); } });
    if(art && key){                                                              // Artikel: „Gelesen …“ in der Kennzahlenzeile neben der Lesezeit (User, 11.11.2026)
      var zl=document.querySelector(".art-meta .am-zahlen"), z=zl?zl.querySelector(".am-lf"):null;
      if(g[key] && zl){
        var m=kapitel.length?kapitel:[key], n=0; m.forEach(function(p){ if(g[p]) n++; });
        if(!z){ z=$.el("span","am-lf"); zl.appendChild(z); }
        z.textContent=$.w("lf_artikel",{n:n,m:m.length});
      } else if(z) z.parentNode.removeChild(z);
    }
    weiter();
  }
  document.addEventListener("etundso-baum",malen);                               // Seitenleiste hat Zeilen nachgeladen
  if(art && key){
    var titel=document.title.replace(/\s+—\s+EtUndSo$/,"");
    var v=$.get(V,[]).filter(function(e){ return e && e.p!==key; });
    v.unshift({p:key, t:titel, k:(side&&side.getAttribute("data-kapitel"))||"", l:$.lang, z:Date.now()});
    $.set(V,v.slice(0,12));
    // W4a: in „Formeln“ ist die Zusammenfassung verborgen, dort zählt das Ende des Formelblatts
    var enden=[document.getElementById("zusammenfassung")||art.querySelector(".neighbors"), art.querySelector(".fb-ende")].filter(Boolean);
    if(enden.length && !gelesen()[key] && window.IntersectionObserver){
      var t=null, io=new IntersectionObserver(function(es){
        es.forEach(function(e){ e.target._lfSicht=e.isIntersecting; });
        clearTimeout(t);
        if(enden.some(function(x){ return x._lfSicht; }))
          t=setTimeout(function(){ var g=gelesen(); g[key]=Date.now(); $.set(G,g); io.disconnect(); malen(); },1000); });
      enden.forEach(function(x){ io.observe(x); });
    }
  }
  // Übersicht: „Weiterlesen“ und „Fortschritt zurücksetzen“ unter dem Einleitungssatz
  var box=null;
  function weiter(){
    if(!document.querySelector(".field-block")) return;
    var g=gelesen(), v=$.get(V,[]), e=null;
    for(var i=0;i<v.length;i++){ if(v[i] && v[i].l===$.lang && v[i].p && !g[v[i].p]){ e=v[i]; break; } }
    if(!box){
      var lede=document.querySelector("main.article .idx-suche")||document.querySelector("main.article .lede"); if(!lede) return;
      box=$.el("div","lf-weiter"); box.hidden=true; lede.parentNode.insertBefore(box,lede.nextSibling);
    }
    box.innerHTML="";
    if(e){ var a=$.el("a","lf-weiter-a"); a.href=e.p; a.appendChild($.el("span","lf-wh",$.w("weiterlesen")));
      a.appendChild($.el("span","lf-wt",(e.k?e.k+" › ":"")+e.t)); box.appendChild(a); }
    var r=$.el("button","lern-reset lf-reset",$.w("fs_reset")); r.type="button"; r.title=$.w("fs_lokal");
    $.sicher(r,function(){ $.del(G); $.del(V); malen(); });
    box.appendChild(r);
    box.hidden=!(e || Object.keys(g).length);
  }
  malen();
})();
// Link-Vorschau: Links auf Artikel (data-vs, vom Build gesetzt) zeigen ein Kärtchen mit Titel, Kapitel und „Worum es geht“
// aus der vorschau.json des Zielmoduls. Maus: nach kurzem Verweilen; Tastatur: beim Fokus; Handy: langes Tippen (dann mit
// „Öffnen“ und „Schließen“). Schließt beim Verlassen, mit Esc, beim Tippen daneben und bei Größenänderung.
(function(){
  var $=LERNEN; if(!document.querySelector("a[data-vs]") || !window.fetch) return;
  var cache={}, karte=null, ziel=null, tAuf=null, tZu=null, tLang=null, unterdr=null, sx=0, sy=0;
  function modul(p){ var s=p.replace(/^\/wissen\//,"").split("/"); return s.slice(0,-2).join("/"); }
  function daten(p){ var m=modul(p);
    if(!cache[m]) cache[m]=fetch("/wissen/"+m+"/vorschau.json").then(function(r){ return r.ok?r.json():{}; }).catch(function(){ return {}; });
    return cache[m]; }
  function bau(){ if(karte) return karte;
    karte=$.el("div","vs-karte"); karte.id="vs-karte"; karte.setAttribute("role","tooltip"); karte.hidden=true;
    karte.addEventListener("pointerenter",function(){ clearTimeout(tZu); });
    karte.addEventListener("pointerleave",function(e){ if(e.pointerType==="mouse") spaeter(); });
    document.body.appendChild(karte); return karte; }
  function zu(){ clearTimeout(tAuf); clearTimeout(tZu); if(karte) karte.hidden=true; if(ziel) ziel.removeAttribute("aria-describedby"); ziel=null; }
  function spaeter(){ clearTimeout(tZu); tZu=setTimeout(zu,220); }
  function lage(a,k){
    var r=a.getClientRects()[0]||a.getBoundingClientRect(), vw=document.documentElement.clientWidth, b=Math.min(340,vw-16);
    k.style.width=b+"px";
    var x=Math.max(8,Math.min(r.left,vw-b-8)), h=k.offsetHeight, y=r.bottom+8;
    if(y+h>window.innerHeight-8 && r.top-h-8>64) y=r.top-h-8;
    k.style.left=(x+window.scrollX)+"px"; k.style.top=(y+window.scrollY)+"px"; }
  function auf(a,touch){
    var u; try{ u=new URL(a.href); }catch(e){ return; }
    if(u.pathname===location.pathname) return;
    ziel=a;
    daten(u.pathname).then(function(d){
      var e=d[u.pathname.replace(/^\/wissen\//,"")]; if(ziel!==a || !e) return;
      var k=bau(); k.innerHTML="";
      if(e[1]) k.appendChild($.el("div","vs-k",e[1]));
      k.appendChild($.el("div","vs-t",e[0]));
      if(e[2]) k.appendChild($.el("p","vs-p",e[2]));
      if(touch){ var f=$.el("div","vs-f"), o=$.el("a","vs-o",$.w("vs_oeffnen")), s=$.el("button","vs-s",$.w("vs_schliessen"));
        o.href=a.href; s.type="button"; s.addEventListener("click",zu); f.appendChild(o); f.appendChild(s); k.appendChild(f); }
      k.hidden=false; lage(a,k); a.setAttribute("aria-describedby","vs-karte");
    }); }
  function link(e){ return e.target && e.target.closest ? e.target.closest("a[data-vs]") : null; }
  document.addEventListener("pointerover",function(e){ if(e.pointerType!=="mouse") return; var a=link(e); if(!a) return;
    if(a===ziel){ clearTimeout(tZu); return; } clearTimeout(tAuf); tAuf=setTimeout(function(){ auf(a,false); },350); });
  document.addEventListener("pointerout",function(e){ if(e.pointerType!=="mouse") return; var a=link(e); if(!a) return;
    if(e.relatedTarget && a.contains(e.relatedTarget)) return; clearTimeout(tAuf); if(a===ziel) spaeter(); });
  var beruehrt=0;                                                   // Fokus nach Antippen: kein zweites Kärtchen (ohne „Öffnen“)
  document.addEventListener("focusin",function(e){ var a=link(e); if(!a || (a===ziel && karte && !karte.hidden) || Date.now()-beruehrt<1500) return;
    clearTimeout(tAuf); tAuf=setTimeout(function(){ auf(a,false); },250); });
  document.addEventListener("focusout",function(e){ var a=link(e); if(!a) return;
    if(karte && e.relatedTarget && karte.contains(e.relatedTarget)) return; clearTimeout(tAuf); if(a===ziel) zu(); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape" && karte && !karte.hidden) zu(); });
  document.addEventListener("touchstart",function(e){ var a=link(e); unterdr=null; beruehrt=Date.now();
    if(karte && !karte.hidden && !karte.contains(e.target)) zu();
    if(!a || e.touches.length>1) return;
    sx=e.touches[0].clientX; sy=e.touches[0].clientY; clearTimeout(tLang);
    tLang=setTimeout(function(){ tLang=null; unterdr=a; auf(a,true); },500); },{passive:true});
  document.addEventListener("touchmove",function(e){ if(!tLang) return; var t=e.touches[0];
    if(Math.abs(t.clientX-sx)>10 || Math.abs(t.clientY-sy)>10){ clearTimeout(tLang); tLang=null; } },{passive:true});
  function ab(){ clearTimeout(tLang); tLang=null; }
  document.addEventListener("touchend",ab,{passive:true}); document.addEventListener("touchcancel",ab,{passive:true});
  document.addEventListener("click",function(e){ var a=link(e); if(a && a===unterdr){ e.preventDefault(); } unterdr=null; },true);
  document.addEventListener("contextmenu",function(e){ var a=link(e); if(a && a===unterdr) e.preventDefault(); });
  window.addEventListener("resize",zu);
})();
// Selbsttest in der Zusammenfassung: Der Knopf deckt Bestimmungen, Formeln und Zusammenhänge zu (die Begriffe, Formelnamen
// und der Abschnitt bleiben als Stichwort stehen); Antippen, Enter oder Leertaste deckt einen Punkt auf.
(function(){
  var $=LERNEN, zf=document.querySelector(".zf"), knopf=zf&&zf.querySelector(".zf-test"); if(!knopf) return;
  var teile=[].slice.call(zf.querySelectorAll(".zf-d,.zf-f,.zf-a")); if(!teile.length) return;
  knopf.hidden=false;
  function decke(el,zu){
    el.classList.toggle("zu",zu);
    if(zu){ el.setAttribute("tabindex","0"); el.setAttribute("role","button"); el.setAttribute("aria-label",$.w("aufdecken")); el.setAttribute("data-auf",$.w("aufdecken")); }
    else { el.removeAttribute("role"); el.removeAttribute("aria-label"); el.removeAttribute("tabindex"); } }
  function an(on){
    zf.classList.toggle("zf-abgedeckt",on); knopf.setAttribute("aria-pressed",on?"true":"false");
    teile.forEach(function(el){ decke(el,on); });
    [].forEach.call(zf.querySelectorAll(".zf-cue"),function(c){ c.hidden=!on; });
    if(on) [].forEach.call(zf.querySelectorAll("details.zf-mehr"),function(d){ d.open=true; }); }
  knopf.addEventListener("click",function(){ an(knopf.getAttribute("aria-pressed")!=="true"); });
  zf.addEventListener("click",function(e){ var t=e.target.closest&&e.target.closest(".zu"); if(!t || !zf.contains(t)) return;
    e.preventDefault(); e.stopPropagation(); decke(t,false); },true);
  zf.addEventListener("keydown",function(e){ var t=e.target; if((e.key!=="Enter" && e.key!==" ") || !t.classList || !t.classList.contains("zu")) return;
    e.preventDefault(); decke(t,false); });
})();
// Begriffe: Filter über die Begriffe der Seite (Teilwörter, ohne Umlaute und Akzente wie die Suche)
(function(){
  var $=LERNEN, such=document.querySelector(".bg-such"); if(!such) return;
  var inp=such.querySelector(".bg-filter"), n=such.querySelector(".bg-n"), nichts=document.querySelector(".bg-nichts");
  var es=[].slice.call(document.querySelectorAll(".bg-e")), gs=[].slice.call(document.querySelectorAll(".bg-g")), dt=null;
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").replace(/ı/g,"i").replace(/œ/g,"oe").replace(/æ/g,"ae")
    .normalize("NFKD").replace(/[̀-ͯ]/g,""); }
  function text(e){ var d=e.querySelector("dt"); return fold(d?d.textContent:""); }
  such.hidden=false;
  inp.addEventListener("input",function(){
    if(!dt) dt=es.map(text);
    var q=fold(inp.value.trim()), k=0;
    es.forEach(function(e,i){ var on=!q || dt[i].indexOf(q)>=0; e.hidden=!on; if(on) k++; });
    gs.forEach(function(g){ g.hidden=!g.querySelector(".bg-e:not([hidden])"); });
    n.textContent=$.w("bg_anzahl",{n:k}); if(nichts) nichts.hidden=k>0; });
})();
// Lernkarten (W2) sind seit W4b ein eigener Bereich: /lernen/, Code in assets/bereiche.js (Leitner wie hier früher).
/* ---------- Ansichten (W4a, 11.11.2026): Ausführlich | Kurz | Formeln ----------
   Der Kopf der Seite setzt data-ansicht an <html> schon vor dem ersten Zeichnen (?ansicht= in der Adresse, sonst die Wahl
   unter „etundso-ansicht“; sie gilt für alle Artikel). Umschalten = Attribut ändern; die Adresse bekommt ?ansicht= zum
   Teilen. Ein Sprung auf ein Ziel, das die Ansicht verbirgt (Anker, Link aus Zusammenfassung, Suche, Begriffen), schaltet
   für diese Seite auf „Ausführlich“, ohne die Wahl zu ändern (Teil „Sprung auf einen Anker“ ruft dazu ETAnsicht). */
window.ETAnsicht=(function(){
  var $=LERNEN, root=document.documentElement, K="etundso-ansicht";
  var art=document.querySelector("main.article > article.art");
  function jetzt(){ var a=root.getAttribute("data-ansicht"); return a==="kurz"||a==="formeln"?a:"voll"; }
  function verborgen(el){ for(var x=el; x && x!==document.body; x=x.parentElement){ if(getComputedStyle(x).display==="none") return true; } return false; }
  if(!art){ root.removeAttribute("data-ansicht"); return {jetzt:jetzt, verborgen:function(){ return false; }, setze:function(){}}; }
  var seg=document.querySelector(".topbar .ansicht"), sel=document.querySelector(".topbar .ans-sel");
  var blatt=document.getElementById("formelblatt"), zeit=art.querySelector(".am-zeit"), zeitVoll=zeit?zeit.textContent:"";
  // Formelblatt: KaTeX erst beim ersten Öffnen (vor DOMContentLoaded übernimmt das der Durchgang über die ganze Seite)
  function blattSetzen(){ if(!blatt || !blatt.classList.contains("fb-spaeter")) return;
    blatt.classList.remove("fb-spaeter"); if(document.readyState!=="loading") mathe(blatt); }
  // Lesezeit der Kurzansicht: sichtbare Wörter (ohne Formeln und Code) / 170, wie lesezeit() im Build
  function kurzZeit(){ var n=0, wurzel=art.querySelector(art.classList.contains("hat-kurz")?".ans-kurz":".art-body"); if(!wurzel) return 1;
    [].forEach.call(wurzel.querySelectorAll("p,li,dt,dd,td,th,figcaption"),function(x){
      if(!x.getClientRects().length || x.querySelector("p,li")) return;
      var c=x.cloneNode(true); [].forEach.call(c.querySelectorAll(".katex,code,.katex-display"),function(k){ k.parentNode.removeChild(k); });
      n+=c.textContent.split(/\s+/).filter(function(w){ return /[A-Za-zÄÖÜäöüß0-9]/.test(w); }).length; });
    return Math.max(1,Math.round(n/170)); }
  function malen(){
    var a=jetzt();
    if(seg) [].forEach.call(seg.querySelectorAll(".ans-b"),function(b){ b.setAttribute("aria-pressed",String(b.getAttribute("data-ansicht")===a)); });
    if(sel) sel.value=a;
    if(a==="formeln") blattSetzen();
    if(zeit) zeit.textContent=a==="kurz" ? $.w("ans_kurz_min",{n:kurzZeit()}) : zeitVoll;
  }
  function setze(a,merken){
    a=(a==="kurz"||a==="formeln")?a:"voll";
    var vorher=jetzt(), oben=null;
    if(scrollY>200 && a!=="formeln"){                               // Lage halten: Abschnitt oben im Fenster merken
      var hs=art.querySelectorAll(".art-body h2,.art-body h3");
      for(var i=0;i<hs.length;i++){ var r=hs[i].getBoundingClientRect(); if(!r.height) continue; if(r.top<=130) oben=hs[i]; else break; } }
    if(a==="voll") root.removeAttribute("data-ansicht"); else root.setAttribute("data-ansicht",a);
    if(merken){ try{ localStorage.setItem(K,a); }catch(e){} }
    try{ var u=new URL(location.href); if(a==="voll") u.searchParams.delete("ansicht");    // Informatik: ?ansicht=uebersicht
      else u.searchParams.set("ansicht",a==="formeln" && art.classList.contains("ref")?"uebersicht":a);
      if(u.href!==location.href) history.replaceState(history.state,"",u.href); }catch(e){}
    malen();
    if(a!==vorher && merken){                                       // ohne weiches Scrollen (html hat scroll-behavior:smooth)
      root.style.scrollBehavior="auto";
      if(a==="formeln" && blatt){ if(blatt.getBoundingClientRect().top<0) blatt.scrollIntoView({block:"start"}); }
      else if(oben && oben.getClientRects().length) oben.scrollIntoView({block:"start"});
      else if(scrollY>art.offsetTop) window.scrollTo(0,0);
      root.style.scrollBehavior="";
    }
    window.dispatchEvent(new Event("resize"));                      // abgesetzte Formeln neu einpassen (fitMath)
  }
  if(seg){ seg.hidden=false;
    seg.addEventListener("click",function(e){ var b=e.target.closest(".ans-b"); if(b) setze(b.getAttribute("data-ansicht"),true); });
    seg.addEventListener("keydown",function(e){                      // Pfeiltasten wandern und wählen (wie eine Optionsgruppe)
      if(e.key!=="ArrowLeft" && e.key!=="ArrowRight" && e.key!=="Home" && e.key!=="End") return;
      var bs=[].slice.call(seg.querySelectorAll(".ans-b")), i=bs.indexOf(document.activeElement); if(i<0) return;
      e.preventDefault();
      i=e.key==="Home"?0:e.key==="End"?bs.length-1:(i+(e.key==="ArrowRight"?1:-1)+bs.length)%bs.length;
      bs[i].focus(); setze(bs[i].getAttribute("data-ansicht"),true); }); }
  if(sel){ sel.hidden=false; sel.addEventListener("change",function(){ setze(sel.value,true); }); }
  [].forEach.call(document.querySelectorAll("[data-ansicht-setzen]"),function(b){
    b.addEventListener("click",function(){ setze(b.getAttribute("data-ansicht-setzen"),true); }); });
  malen();
  if(jetzt()==="kurz" && zeit) window.addEventListener("load",malen);   // Lesezeit nach dem Setzen der Formeln
  window.addEventListener("pageshow",function(e){ if(e.persisted) malen(); });
  return {jetzt:jetzt, verborgen:verborgen, setze:setze};
})();
// Modulseiten (Formelsammlung, Kapitel auf einer Seite): ?kapitel=N zeigt und druckt nur Kapitel N; die Kapitelliste
// wechselt dann das Kapitel, statt an eine ausgeblendete Stelle zu springen. „Drucken“ öffnet den Druckdialog.
(function(){
  var leiste=document.querySelector(".kap-leiste"); if(!leiste) return;
  var sel=leiste.querySelector(".kap-sel"), main=document.querySelector("main.article");
  var kaps=[].slice.call(document.querySelectorAll(".fs-kap,.sz-kap"));
  function hat(n){ return kaps.some(function(k){ return k.getAttribute("data-k")===n; }); }
  function zeige(n,schreiben){
    if(!hat(n)) n="";
    if(n) main.setAttribute("data-kapitel-filter",n); else main.removeAttribute("data-kapitel-filter");
    kaps.forEach(function(k){ k.classList.toggle("kap-an",k.getAttribute("data-k")===n); });
    sel.value=n;
    if(schreiben){ try{ var u=new URL(location.href); if(n) u.searchParams.set("kapitel",n); else u.searchParams.delete("kapitel");
      u.hash=""; history.replaceState(null,"",u.href); }catch(e){} }
  }
  leiste.hidden=false;
  zeige(new URLSearchParams(location.search).get("kapitel")||"",false);
  sel.addEventListener("change",function(){ zeige(sel.value,true); });
  leiste.querySelector(".kap-druck").addEventListener("click",function(){ window.print(); });
  document.addEventListener("click",function(e){                    // Kapitelliste bei aktivem Filter: Kapitel wechseln
    var a=e.target.closest && e.target.closest(".kap-nav a"); if(!a || !main.hasAttribute("data-kapitel-filter")) return;
    var k=document.getElementById(a.getAttribute("href").slice(1)); if(!k) return;
    e.preventDefault(); zeige(k.getAttribute("data-k"),true); k.scrollIntoView({block:"start"}); });
})();
// Download des Formelblatts (Artikel) bzw. der Formelsammlung (Modul) als PNG, JPG, SVG oder PDF. Die Dateien entstehen
// im Browser aus der angezeigten Seite; assets/formel-export.js (setzt die Formeln mit MathJax als SVG, PDF ohne fremde
// Bibliothek) lädt erst beim ersten Klick.
(function(){
  var boxen=[].slice.call(document.querySelectorAll(".fb-dl")); if(!boxen.length) return;
  var $=LERNEN, P=null;
  function laden(){ if(!P) P=new Promise(function(ok,fehler){ var s=document.createElement("script"); s.src="/wissen/assets/formel-export.js";
      s.onload=function(){ window.ETFormelExport ? ok(window.ETFormelExport) : fehler(new Error("laden")); };
      s.onerror=function(){ P=null; fehler(new Error("laden")); }; document.head.appendChild(s); });
    return P; }
  boxen.forEach(function(box){
    var status=box.querySelector(".fb-dl-s"), seite=box.closest(".fb-blatt")||document.querySelector("main.article"), quelle=seite.querySelector(".fb-inhalt");
    if(!quelle) return;
    box.hidden=false;
    box.addEventListener("click",function(e){
      var b=e.target.closest(".fb-dl-b"); if(!b || b.getAttribute("aria-busy")==="true") return;
      var main=document.querySelector("main.article"), kap=main && main.getAttribute("data-kapitel-filter");
      b.setAttribute("aria-busy","true"); status.textContent=$.w("dl_laeuft"); status.classList.remove("fehler");
      laden().then(function(X){ return X(quelle,b.getAttribute("data-format"),{kapitel:kap||"", lang:$.lang}); })
        .then(function(){ status.textContent=""; },
              function(err){ status.textContent=(err && err.message==="zu-gross")?$.w("dl_gross"):$.w("dl_fehler"); status.classList.add("fehler");
                if(window.console) console.warn("Formel-Export:",err); })
        .then(function(){ b.removeAttribute("aria-busy"); });
    });
  });
})();
"""

# Kern der Suche (W3a, 11.11.2026), als /wissen/assets/suche.js: wissen.js lädt ihn beim ersten Öffnen der Suche, die
# Startseite für ihr Filterfeld. Daten und Treffer-Regeln: suchindex_schreiben.
SUCHE_JS = r"""/* EtUndSo-Suche: ETSuche(sprache) -> Index mit start(), suche(text, rückruf), snippet(doc, q), fold(text).
   start() lädt titel.json (Titel, Brotkrumen, Schlagwörter, summary, Abschnitte). suche() meldet sofort die Treffer aus
   diesen Feldern und den schon geladenen Volltexten, holt dann die Volltexte der Module, deren Wörter das Suchwort
   enthalten (woerter.json; ohne Verzeichnis: alle), und meldet nach jedem Modul neu. Rang wie zuvor: Titel 0,
   Schlagwort 1, Abschnittsüberschrift 1,5, Text 2 + Lage (früher = besser). Nichts verlässt den Browser. */
window.ETSuche=(function(){
  var INDEX={};
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").replace(/ı/g,"i").replace(/œ/g,"oe").replace(/æ/g,"ae")
    .normalize("NFKD").replace(/[̀-ͯ]/g,""); }          // wie fold_js() in build_wissen.py
  function esc(s){ return (s||"").replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];}); }
  function json(u){ return fetch(u).then(function(r){ if(!r.ok) throw new Error(u+": "+r.status); return r.json(); }); }
  function Index(lang){
    var B="/wissen/data/suche/"+lang+"/", self=this, T=null, WP=null, WG=null, mods=[], docs=[], jetzt=null, warte=null;
    self.fold=fold; self.esc=esc; self.docs=docs;
    self.start=function(){
      if(!T) T=json(B+"titel.json").then(function(d){
        d.m.forEach(function(m){ mods.push({f:m.f, p:m.p, da:false, P:null}); });
        d.d.forEach(function(x,i){ var sec=x[6]||[];
          docs.push({i:i, title:x[0], crumb:x[1], path:x[2], tags:x[3]||"", summary:x[4]||"", m:x[5], sec:sec, klar:x[7]||x[0],
            fTitle:fold(x[0]), fTags:fold(x[3]||""), fSum:fold(x[4]||""), fSec:sec.map(function(s){ return fold(s[1]); }),
            ft:null, text:null}); });
        self.w=!!d.w; return self;
      }).catch(function(e){ T=null; throw e; });
      return T; };
    function woerter(){                                                 // Wortverzeichnis: [{m:[Modul…], w:" wort wort … "}]
      if(!WP) WP=(self.w ? json(B+"woerter.json").then(function(d){
        WG=Object.keys(d).map(function(k){ return {m:k.split(",").map(Number), w:" "+d[k]+" "}; });
      }) : Promise.resolve()).catch(function(){ WG=null; });          // ohne Verzeichnis: alle Module laden
      return WP; }
    function moeglich(q){                                               // Module, deren Text q enthalten kann (Menge) oder null = alle
      if(!WG) return null;
      var erg=null;
      q.split(" ").filter(Boolean).forEach(function(t){                 // ein Teil ohne Leerzeichen liegt in einem Wort
        var s={}; WG.forEach(function(g){ if(g.w.indexOf(t)>=0) g.m.forEach(function(k){ s[k]=1; }); });
        if(erg) Object.keys(erg).forEach(function(k){ if(!s[k]) delete erg[k]; }); else erg=s; });
      return erg; }
    function laden(m){
      if(!m.P) m.P=json(B+m.f).then(function(rows){
        rows.forEach(function(r){ var d=docs[r[0]]; d.text=r[1]; d.ft=fold(d.summary+" "+r[1]); }); m.da=true;
      }).catch(function(){ m.P=null; m.fehler=true; });
      return m.P; }
    function rang(d,q){
      if(d.fTitle.indexOf(q)>=0) return [0];                            // Titel-Treffer: höchster Rang
      if(d.fTags.indexOf(q)>=0) return [1];                             // Schlagwort
      for(var k=0;k<d.fSec.length;k++) if(d.fSec[k].indexOf(q)>=0) return [1.5,d.sec[k][0],d.sec[k][1]];   // Abschnitt
      var p=(d.ft!==null?d.ft:d.fSum).indexOf(q);                       // Text (summary steht vorn, gilt also schon vorher)
      return p>=0 ? [2+Math.min(p/500,1)] : null; }
    function treffer(q){
      var hits=[]; docs.forEach(function(d){ var r=rang(d,q); if(r) hits.push({d:d, sc:r[0], anker:r[1]||null, abschnitt:r[2]||null}); });
      hits.sort(function(a,b){ return a.sc-b.sc; });                    // stabil: gleicher Rang in Lese-Reihenfolge
      return hits; }
    self.suche=function(raw,cb){
      var q=fold((raw||"").trim()), ich={}; jetzt=ich; clearTimeout(warte);
      if(q.length<2){ cb({q:q, hits:[], laedt:false}); return; }
      self.start().then(function(){
        if(jetzt!==ich) return;
        var ok0=moeglich(q), offen=mods.filter(function(m,k){ return !m.da && !m.fehler && (!ok0 || ok0[k]); }).length;
        function melden(){ if(jetzt===ich) cb({q:q, hits:treffer(q), laedt:offen>0}); }
        melden();
        if(!offen) return;
        woerter();                                                      // schon holen, während noch getippt wird
        warte=setTimeout(function(){                                    // erst nach einer kurzen Tipp-Pause nachladen
          woerter().then(function(){
            if(jetzt!==ich) return;
            var ok=moeglich(q);
            var noetig=mods.filter(function(m,k){ return !m.da && !m.fehler && (!ok || ok[k]); });
            offen=noetig.length; if(!offen){ melden(); return; }
            noetig.forEach(function(m){ laden(m).then(function(){ offen--; melden(); }); });
          });
        },180);
      }).catch(function(){ if(jetzt===ich) cb({q:q, hits:[], laedt:false, fehler:true}); });
    };
    self.snippet=function(d,q){
      var t=d.text||d.summary||"", ft=fold(t), i=ft.indexOf(q);
      if(i<0) return esc(t.slice(0,130))+(t.length>130?"…":"");
      // Die Fundstelle i gilt im gefalteten Text. fold() ändert die Länge („ß“→„ss“, „…“→„...“, Ligaturen), deshalb
      // Zeichen für Zeichen zurück auf den Originaltext abbilden; sonst rutscht die Markierung (Fehler vom 11.11.2026).
      var von=-1, bis=t.length, n=0;
      for(var k=0;k<t.length && n<i+q.length;k++){
        var g=fold(t[k]).length;
        if(von<0 && n+g>i) von=k;
        n+=g;
        if(n>=i+q.length){ bis=k+1; break; }
      }
      if(von<0) von=Math.min(i,t.length);
      var a=Math.max(0,von-45);
      return (a>0?"…":"")+esc(t.slice(a,von))+"<mark>"+esc(t.slice(von,bis))+"</mark>"+esc(t.slice(bis,bis+70))+"…";
    };
  }
  return function(lang){ lang=lang||"de"; return INDEX[lang]||(INDEX[lang]=new Index(lang)); };
})();
"""

# Download des Formelblatts (W4a, 11.11.2026), als /wissen/assets/formel-export.js: wissen.js lädt es beim ersten Klick auf
# PNG, JPG, SVG oder PDF. Es liest die angezeigte Formelseite (.fb-inhalt; nur sichtbare Teile, also auch nur das gewählte
# Kapitel), setzt Text und Formeln selbst neu als ein SVG (Formeln: MathJax, dasselbe wie im Editor, als Pfade; Text: Arial
# mit gemessener Breite) und macht daraus die Datei: SVG direkt, PNG/JPG über ein Canvas (doppelte Auflösung), PDF als
# A4-Seiten (je Seite ein JPEG mit 2,5-facher Auflösung) mit einem kleinen eigenen PDF-Schreiber, ohne fremde Bibliothek.
# Keine vorab gespeicherten Dateien: jede Datei entsteht erst im Browser des Lesers.
FORMEL_EXPORT_JS = r"""/* EtUndSo Formel-Export: ETFormelExport(quelle, format, {kapitel, lang}) -> Promise (lädt die Datei herunter). */
(function(){
  var MJ="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js";   // dieselbe Fassung wie der Editor
  var W=794, H_SEITE=1123, RAND=48, INNEN=W-2*RAND;                   // A4 bei 96 dpi (Pixel = CSS-Pixel)
  var SCHRIFT="Arial, Helvetica, sans-serif", EXF=0.45;              // Mathe: 1 ex = 0,45 der Schriftgröße
  var FARBE={text:"#16191a", leise:"#5b6360", gruen:"#15633a", gruen2:"#1b7f4a", orange:"#c2410c", linie:"#d5dad7"};
  var mjP=null, messer=null;
  function mathjax(){
    if(mjP) return mjP;
    mjP=new Promise(function(ok,fehler){
      if(window.MathJax && window.MathJax.tex2svg){ ok(); return; }
      window.MathJax={loader:{load:["[tex]/color"]},tex:{packages:{"[+]":["color"]}},svg:{fontCache:"none"},
        startup:{typeset:false,ready:function(){ MathJax.startup.defaultReady(); MathJax.startup.promise.then(function(){ ok(); }); }}};
      var s=document.createElement("script"); s.src=MJ; s.async=true;
      s.onerror=function(){ mjP=null; fehler(new Error("mathjax")); }; document.head.appendChild(s);
    });
    return mjP;
  }
  function esc(t){ return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }
  function font(st){ return (st.i?"italic ":"")+(st.b?"bold ":"")+st.fs+"px "+(st.mono?"Consolas, 'Courier New', monospace":SCHRIFT); }
  function breite(t,st){ if(!messer) messer=document.createElement("canvas").getContext("2d"); messer.font=font(st); return messer.measureText(t).width; }
  // ---- Formeln: TeX aus der KaTeX-Ausgabe (annotation), Satz mit MathJax als SVG ----
  function tex(k){ var a=k.querySelector('annotation[encoding="application/x-tex"]'); return a?a.textContent:""; }
  function mathe(t,display,fs){
    var ex=fs*EXF, node;
    try{ node=MathJax.tex2svg(t,{display:display,em:fs,ex:ex,containerWidth:INNEN}); }catch(e){ return null; }
    var svg=node.querySelector("svg"); if(!svg || node.querySelector('[data-mml-node="merror"]')) return null;
    var w=parseFloat(svg.getAttribute("width"))*ex, h=parseFloat(svg.getAttribute("height"))*ex;
    var va=/vertical-align:\s*(-?[\d.]+)ex/.exec(svg.getAttribute("style")||""), tief=va?-parseFloat(va[1])*ex:0;
    svg.removeAttribute("style"); svg.removeAttribute("role"); svg.removeAttribute("focusable"); svg.removeAttribute("aria-hidden");
    var inner=new XMLSerializer().serializeToString(svg);
    return {w:w,h:h,tief:tief,svg:function(x,y,s){ s=s||1;
      return inner.replace(/^<svg\b/,'<svg x="'+x.toFixed(2)+'" y="'+y.toFixed(2)+'" style="color:'+FARBE.text+'" overflow="visible"')
        .replace(/ width="[^"]*"/,' width="'+(w*s).toFixed(2)+'"').replace(/ height="[^"]*"/,' height="'+(h*s).toFixed(2)+'"'); }};
  }
  // ---- Inhalt sammeln: Blöcke (Titel, Etikett, Name, Absatz, Formel, Trennlinie) aus den sichtbaren Elementen ----
  var BLOCK=/^(P|DIV|SECTION|ASIDE|UL|OL|LI|H1|H2|H3|H4|H5|H6|TABLE|PRE|BLOCKQUOTE|DL|DT|DD|FIGURE|DETAILS|NAV|HR|FIGCAPTION|ARTICLE|TR|TBODY|THEAD)$/;
  var WEG=/^(FIGURE|IMG|DETAILS|BUTTON|SCRIPT|STYLE|NAV|SELECT|INPUT|HR)$/;
  function versteckt(n){ return n.hidden || getComputedStyle(n).display==="none"; }
  function sammeln(quelle){
    var aus=[], vorWartet="";                                       // Aufzählungszeichen für den ersten Absatz eines Listenpunkts
    function absatz(z,einzug,art){
      if(z.runs.some(function(r){ return r.m || (r.t && r.t.trim()); })){ aus.push({typ:art||"absatz",runs:z.runs,einzug:einzug||0,vor:vorWartet}); vorWartet=""; }
      z.runs=[]; }
    function fluss(el,st,z,einzug){
      for(var n=el.firstChild;n;n=n.nextSibling){
        if(n.nodeType===3){ z.runs.push({t:n.nodeValue,st:st}); continue; }
        if(n.nodeType!==1 || versteckt(n)) continue;
        var c=n.classList, tag=n.tagName;
        if(c.contains("katex-display") || c.contains("mrow") || c.contains("gl-zeile") || c.contains("fb-gl") || c.contains("fb-n")
           || c.contains("fb-h") || c.contains("callout-h") || c.contains("fbox-h")){ absatz(z,einzug); block(n,einzug); continue; }
        if(c.contains("katex")){ z.runs.push({m:tex(n),st:st}); continue; }
        if(c.contains("katex-mathml") || c.contains("fb-nr") || WEG.test(tag) || tag==="svg") continue;
        if(tag==="BR"){ z.runs.push({br:true,st:st}); continue; }
        if(BLOCK.test(tag)){ absatz(z,einzug); block(n,einzug); continue; }
        var s2={fs:st.fs,b:st.b||/^(STRONG|B|TH)$/.test(tag),i:st.i||/^(EM|I)$/.test(tag),mono:st.mono||tag==="CODE",farbe:st.farbe};
        fluss(n,s2,z,einzug);
      }
    }
    function formel(n,einzug){                                     // eine Formelzeile: Teile (mrow) und Nummer
      var ks=[].slice.call(n.classList.contains("katex-display")?[n]:n.querySelectorAll(".katex-display")).map(tex).filter(Boolean);
      if(!ks.length) ks=[].slice.call(n.querySelectorAll(".katex")).map(tex).filter(Boolean);
      var nr=n.querySelector(".gl-nr, .fb-nr:not(.fb-ohne)");
      if(ks.length) aus.push({typ:"formel",tex:ks,nr:nr?nr.textContent.replace(/\)\s*\(/g,") (").trim():"",einzug:einzug||0});
    }
    function block(el,einzug){
      if(versteckt(el)) return;
      var c=el.classList, tag=el.tagName;
      if(WEG.test(tag) || c.contains("fb-dl") || c.contains("abb-knopf") || c.contains("gr-szene") || c.contains("zf-cue")) return;
      if(c.contains("fb-e")){ aus.push({typ:"trenn"}); }
      if(c.contains("katex-display") || c.contains("mrow") || c.contains("gl-zeile") || c.contains("fb-gl")){ formel(el,einzug); return; }
      if(c.contains("fb-h")){ aus.push({typ:"etikett",runs:[{t:el.textContent.toUpperCase(),st:{fs:11.5,b:true,farbe:FARBE.orange}}]}); return; }
      if(c.contains("fb-n") || c.contains("callout-h") || c.contains("fbox-h") || c.contains("zf-gh")){
        var z0={runs:[]}; fluss(el,{fs:15,b:true,farbe:FARBE.gruen2},z0,einzug); absatz(z0,einzug,"name"); return; }
      if(/^H[1-4]$/.test(tag)){ var lv=+tag.charAt(1), zh={runs:[]};
        fluss(el,{fs:lv<=2?20:16.5,b:true,farbe:lv<=2?FARBE.gruen:FARBE.text},zh,einzug); absatz(zh,einzug,"h"+Math.max(2,lv)); return; }
      if(tag==="UL" || tag==="OL"){ var k=0;
        [].forEach.call(el.children,function(li){ if(li.tagName!=="LI" || versteckt(li)) return; k++;
          var zl={runs:[]}; vorWartet=tag==="OL"?k+".":"•"; fluss(li,{fs:15},zl,(einzug||0)+22); absatz(zl,(einzug||0)+22); vorWartet=""; });
        return; }
      if(tag==="TABLE"){ [].forEach.call(el.querySelectorAll("tr"),function(tr){ var zt={runs:[]};
          [].forEach.call(tr.children,function(td,i){ if(i) zt.runs.push({t:"   |   ",st:{fs:14,farbe:FARBE.leise}}); fluss(td,{fs:14,b:td.tagName==="TH"},zt,einzug); });
          absatz(zt,einzug); }); return; }
      if(tag==="PRE"){ var zs=el.textContent.replace(/\n$/,"").split("\n");
        zs.forEach(function(l,k){ aus.push({typ:k===zs.length-1?"code-ende":"code",runs:[{t:l||" ",st:{fs:13,mono:true}}],einzug:einzug||0}); }); return; }
      var z={runs:[]}; fluss(el,{fs:15},z,einzug); absatz(z,einzug);
    }
    var t=quelle.getAttribute("data-titel")||"", u=quelle.getAttribute("data-unter")||"";
    aus.push({typ:"titel",runs:[{t:t,st:{fs:22,b:true,farbe:FARBE.gruen}}]});
    if(u) aus.push({typ:"unter",runs:[{t:u,st:{fs:13,farbe:FARBE.leise}}]});
    block(quelle,0);
    return aus;
  }
  // ---- Setzen: jeder Block bekommt Höhe und eine Zeichenfunktion (SVG-Text ab Höhe y) ----
  var CJK=/[⺀-鿿豈-﫿＀-￯　-〿]/;
  function tokens(runs){                                            // Wörter, Leerzeichen, CJK-Zeichen einzeln, Formeln
    var out=[];
    runs.forEach(function(r){
      if(r.br){ out.push({br:true}); return; }
      if(r.m!=null){ var m=mathe(r.m,false,r.st.fs); if(m) out.push({m:m,st:r.st}); else out.push({t:r.m,st:r.st}); return; }
      var t=r.t.replace(/\s+/g," ");
      var teile=t.match(/ |[^ ]+/g)||[];
      teile.forEach(function(w){
        if(w===" "){ out.push({sp:true,st:r.st}); return; }
        if(CJK.test(w)){ (w.match(/[⺀-鿿豈-﫿＀-￯　-〿][,.;:!?)\]，。；：！？）」』]*|[^⺀-鿿豈-﫿＀-￯　-〿]+/g)||[]).forEach(function(x){ out.push({t:x,st:r.st,cjk:true}); }); }
        else out.push({t:w,st:r.st});
      });
    });
    return out;
  }
  function absatzSetzen(b,breiteMax){
    var tk=tokens(b.runs), zeilen=[], z={el:[],w:0,auf:0,ab:0}, x0=b.einzug||0;
    function neu(){ zeilen.push(z); z={el:[],w:0,auf:0,ab:0}; }
    var fs0=(b.runs[0]&&b.runs[0].st&&b.runs[0].st.fs)||15;
    tk.forEach(function(t){
      if(t.br){ neu(); return; }
      if(t.sp){ if(z.el.length){ var ws=breite(" ",t.st); z.el.push({sp:true,w:ws}); z.w+=ws; } return; }
      var w=t.m?t.m.w:breite(t.t,t.st);
      if(z.el.length && z.w+w>breiteMax-x0){ while(z.el.length && z.el[z.el.length-1].sp){ z.w-=z.el.pop().w; } neu(); }
      z.el.push(t.m?{m:t.m,w:w}:{t:t.t,w:w,st:t.st}); z.w+=w;
      if(t.m){ z.auf=Math.max(z.auf,t.m.h-t.m.tief); z.ab=Math.max(z.ab,t.m.tief); }
    });
    if(z.el.length) neu();
    var zh=fs0*1.5, ys=[], h=0;
    zeilen.forEach(function(zz){ var auf=Math.max(fs0*1.05,zz.auf+3), ab=Math.max(fs0*0.45,zz.ab+3); ys.push({auf:auf,ab:ab}); h+=Math.max(zh,auf+ab); });
    return {h:h,zeichne:function(y){
      var s="", yy=y;
      zeilen.forEach(function(zz,k){
        var hz=Math.max(zh,ys[k].auf+ys[k].ab), base=yy+(hz-(ys[k].auf+ys[k].ab))/2+ys[k].auf, x=RAND+x0;
        if(k===0 && b.vor) s+='<text x="'+(RAND+x0-16).toFixed(2)+'" y="'+base.toFixed(2)+'" font-family="'+SCHRIFT+'" font-size="'+fs0+'" fill="'+FARBE.leise+'" text-anchor="middle">'+esc(b.vor)+'</text>';
        zz.el.forEach(function(e){
          if(e.m){ s+=e.m.svg(x,base+e.m.tief-e.m.h); }
          else if(!e.sp){ var st=e.st; s+='<text x="'+x.toFixed(2)+'" y="'+base.toFixed(2)+'" font-family="'+(st.mono?"Consolas, Courier New, monospace":SCHRIFT)+'" font-size="'+st.fs+'"'
              +(st.b?' font-weight="bold"':'')+(st.i?' font-style="italic"':'')+' fill="'+(st.farbe||FARBE.text)+'">'+esc(e.t)+'</text>'; }
          x+=e.w; });
        yy+=hz; });
      return s; }};
  }
  function formelSetzen(b){
    var teile=b.tex.map(function(t){ return mathe(t,true,16); }), nrB=b.nr?breite(b.nr,{fs:14})+14:0, platz=INNEN-(b.einzug||0)-nrB;
    var gut=teile.filter(Boolean); if(!gut.length) return absatzSetzen({runs:[{t:b.tex.join("   "),st:{fs:14,mono:true}}],einzug:b.einzug},INNEN);
    var luecke=28, summe=gut.reduce(function(a,m){ return a+m.w; },0)+luecke*(gut.length-1);
    var reihen=summe<=platz?[gut]:gut.map(function(m){ return [m]; });   // nebeneinander oder untereinander
    var hs=reihen.map(function(r){ var wR=r.reduce(function(a,m){ return a+m.w; },0)+luecke*(r.length-1), s=Math.min(1,platz/wR);
      return {r:r,s:s,w:wR*s,h:Math.max.apply(null,r.map(function(m){ return m.h; }))*s}; });
    var h=hs.reduce(function(a,x){ return a+x.h+10; },0)+6;
    return {h:h,zeichne:function(y){ var s="", yy=y+6;
      hs.forEach(function(x,k){ var xx=RAND+(b.einzug||0)+Math.max(0,(platz-x.w)/2);
        x.r.forEach(function(m){ s+=m.svg(xx,yy+(x.h-m.h*x.s)/2,x.s); xx+=(m.w+luecke)*x.s; });
        if(k===hs.length-1 && b.nr) s+='<text x="'+(W-RAND).toFixed(2)+'" y="'+(yy+x.h/2+5).toFixed(2)+'" font-family="'+SCHRIFT+'" font-size="14" fill="'+FARBE.leise+'" text-anchor="end">'+esc(b.nr)+'</text>';
        yy+=x.h+10; });
      return s; }};
  }
  function setzen(items){
    var lay=[];
    items.forEach(function(b,i){
      if(b.typ==="trenn"){ if(lay.length && !/^(titel|unter|h2|h3|etikett|trenn)$/.test(lay[lay.length-1].typ)) lay.push({typ:"trenn",h:14,zeichne:function(y){ return '<line x1="'+RAND+'" x2="'+(W-RAND)+'" y1="'+(y+7)+'" y2="'+(y+7)+'" stroke="'+FARBE.linie+'" stroke-width="1"/>'; }}); return; }
      if(b.typ==="formel"){ var f=formelSetzen(b); f.typ="formel"; lay.push(f); return; }
      var V={titel:0,unter:2,etikett:14,name:6,h2:22,h3:14,code:0,"code-ende":0}, N={titel:4,unter:18,etikett:2,name:2,h2:8,h3:4,code:0,"code-ende":6};
      var a=absatzSetzen(b,INNEN), vor=b.typ in V?V[b.typ]:4, nach=b.typ in N?N[b.typ]:4;
      if(b.typ==="h2") nach+=6;
      lay.push({typ:b.typ,h:a.h+vor+nach,zeichne:function(y){ var s=a.zeichne(y+vor);
        if(b.typ==="h2") s+='<line x1="'+RAND+'" x2="'+(W-RAND)+'" y1="'+(y+vor+a.h+4).toFixed(2)+'" y2="'+(y+vor+a.h+4).toFixed(2)+'" stroke="'+FARBE.gruen+'" stroke-width="2"/>';
        return s; }});
    });
    return lay;
  }
  function svgDoc(stuecke,h,skala){                                 // stuecke: [{y, s}] in CSS-Pixeln
    return '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+Math.round(W*skala)+'" height="'+Math.round(h*skala)
      +'" viewBox="0 0 '+W+' '+Math.ceil(h)+'"><rect width="'+W+'" height="'+Math.ceil(h)+'" fill="#ffffff"/>'+stuecke+'</svg>';
  }
  function fuss(y,text){ return '<text x="'+(W-RAND)+'" y="'+y.toFixed(2)+'" font-family="'+SCHRIFT+'" font-size="10.5" fill="'+FARBE.leise+'" text-anchor="end">'+esc(text)+'</text>'; }
  function lang(lay){                                               // eine lange Seite (SVG, PNG, JPG)
    var y=RAND, s="";
    lay.forEach(function(b){ s+=b.zeichne(y); y+=b.h; });
    y+=18; s+=fuss(y,"etundso.de"); y+=RAND-18;
    return {s:s,h:y};
  }
  function seiten(lay){                                             // A4-Seiten (PDF): Überschriften und Namen bleiben beim Folgenden
    var unten=H_SEITE-RAND-20, out=[], y=RAND, s="";
    function umbruch(){ out.push(s); s=""; y=RAND; }
    for(var i=0;i<lay.length;i++){
      var b=lay[i], need=b.h, j=i;
      while(j<lay.length-1 && /^(h2|h3|etikett|name|titel|unter|trenn)$/.test(lay[j].typ)){ j++; need+=lay[j].h; }
      if(b.typ==="trenn" && y===RAND) continue;
      if(y+need>unten && y>RAND && need<=unten-RAND) umbruch();
      else if(y+b.h>unten && y>RAND) umbruch();
      if(b.typ==="trenn" && y===RAND) continue;
      s+=b.zeichne(y); y+=b.h;
    }
    if(s) out.push(s);
    return out.map(function(x,k){ return x+fuss(H_SEITE-RAND+14,"etundso.de · "+(k+1)+" / "+out.length); });
  }
  function rastern(svg,w,h,typ,q){
    return new Promise(function(ok,fehler){
      var url=URL.createObjectURL(new Blob([svg],{type:"image/svg+xml"})), img=new Image();
      img.onload=function(){ try{
          var c=document.createElement("canvas"); c.width=w; c.height=h; var x=c.getContext("2d");
          x.fillStyle="#ffffff"; x.fillRect(0,0,w,h); x.drawImage(img,0,0,w,h); URL.revokeObjectURL(url);
          c.toBlob(function(b){ b?ok(b):fehler(new Error("canvas")); },typ,q); }catch(e){ fehler(e); } };
      img.onerror=function(){ URL.revokeObjectURL(url); fehler(new Error("svg")); };
      img.src=url;
    });
  }
  function pdfDatei(bilder){                                        // bilder: [{w,h,bytes}] JPEG, je eine A4-Seite
    var teile=[], len=0, off=[], enc=new TextEncoder();
    function add(x){ var b=typeof x==="string"?enc.encode(x):x; teile.push(b); len+=b.length; }
    function obj(n,body){ off[n]=len; add(n+" 0 obj\n"+body+"\nendobj\n"); }
    add("%PDF-1.4\n%âãÏÓ\n");
    var kids=bilder.map(function(_,i){ return (3+3*i)+" 0 R"; }).join(" ");
    obj(1,"<< /Type /Catalog /Pages 2 0 R >>");
    obj(2,"<< /Type /Pages /Kids ["+kids+"] /Count "+bilder.length+" >>");
    bilder.forEach(function(b,i){
      var p=3+3*i, c=p+1, im=p+2, cs="q 595.28 0 0 841.89 0 0 cm /Im0 Do Q";
      obj(p,"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] /Resources << /XObject << /Im0 "+im+" 0 R >> >> /Contents "+c+" 0 R >>");
      obj(c,"<< /Length "+cs.length+" >>\nstream\n"+cs+"\nendstream");
      off[im]=len;
      add(im+" 0 obj\n<< /Type /XObject /Subtype /Image /Width "+b.w+" /Height "+b.h+" /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length "+b.bytes.length+" >>\nstream\n");
      add(b.bytes); add("\nendstream\nendobj\n");
    });
    var n=2+3*bilder.length, xref=len, z="xref\n0 "+(n+1)+"\n0000000000 65535 f \n";
    for(var i=1;i<=n;i++) z+=("0000000000"+off[i]).slice(-10)+" 00000 n \n";
    add(z+"trailer\n<< /Size "+(n+1)+" /Root 1 0 R >>\nstartxref\n"+xref+"\n%%EOF\n");
    return new Blob(teile,{type:"application/pdf"});
  }
  function speichern(blob,name){
    var a=document.createElement("a"), url=URL.createObjectURL(blob); a.href=url; a.download=name; a.rel="noopener";
    document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(url); a.parentNode.removeChild(a); },4000);
  }
  window.ETFormelExport=function(quelle,format,opt){
    opt=opt||{};
    return mathjax().then(function(){
      var lay=setzen(sammeln(quelle));
      var datei=(quelle.getAttribute("data-datei")||"formeln")+(opt.kapitel?"-kapitel-"+opt.kapitel:"");
      if(format==="svg"){ var l=lang(lay); speichern(new Blob(['<?xml version="1.0" encoding="UTF-8"?>\n'+svgDoc(l.s,l.h,1)],{type:"image/svg+xml"}),datei+".svg"); return; }
      if(format==="png" || format==="jpg"){
        var g=lang(lay), sk=Math.min(2,32000/g.h,Math.sqrt(2.6e8/(W*g.h)));
        if(sk<1) throw new Error("zu-gross");
        return rastern(svgDoc(g.s,g.h,sk),Math.round(W*sk),Math.round(g.h*sk),format==="png"?"image/png":"image/jpeg",0.93)
          .then(function(b){ speichern(b,datei+"."+format); });
      }
      if(format==="pdf"){
        var sk2=2.5, ps=seiten(lay);
        return ps.reduce(function(p,s){ return p.then(function(liste){
            return rastern(svgDoc(s,H_SEITE,sk2),Math.round(W*sk2),Math.round(H_SEITE*sk2),"image/jpeg",0.9)
              .then(function(b){ return b.arrayBuffer(); })
              .then(function(buf){ liste.push({w:Math.round(W*sk2),h:Math.round(H_SEITE*sk2),bytes:new Uint8Array(buf)}); return liste; }); }); },
          Promise.resolve([])).then(function(bilder){ speichern(pdfDatei(bilder),datei+".pdf"); });
      }
      throw new Error("format");
    });
  };
})();
"""

BEREICHE_JS_CODE = r"""/* EtUndSo Bereiche (W4b, 11.11.2026): Lernkarten/Quiz/Mischtest (/lernen/) und Aufgaben (/aufgaben/). Lernstand, gelöste
   Aufgaben und ein laufender Mischtest bleiben in diesem Browser (localStorage über LERNEN aus wissen.js); nichts wird
   übertragen. Wörter: _UI_BEREICHE im Build. */
var BEREICHE_UI=/*UI_BEREICHE*/{};
(function(){
  "use strict";
  var $=window.LERNEN; if(!$) return;
  var W=BEREICHE_UI[$.lang]||{}, D0=BEREICHE_UI.de||{};
  function w(k,o){ var s=W[k]||D0[k]||""; if(o) for(var x in o) s=s.split("{"+x+"}").join(o[x]); return s; }
  function tx(tag,cls,text){ var e=document.createElement(tag); if(cls) e.className=cls; if(text!=null) e.textContent=text; return e; }
  function hx(tag,cls,h){ var e=document.createElement(tag); if(cls) e.className=cls; if(h!=null) e.innerHTML=h; return e; }
  function knopf(cls,text){ var b=tx("button",cls,text); b.type="button"; return b; }
  function setze(e){ if(typeof mathe==="function") mathe(e); try{ window.dispatchEvent(new Event("resize")); }catch(x){} }   // resize: wissen.js passt breite Formeln ein
  function mische(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
  function heute(){ var d=new Date(); return Math.floor((d.getTime()-d.getTimezoneOffset()*60000)/864e5); }
  function param(){ var p=new URLSearchParams(location.search), o={}; p.forEach(function(v,k){ o[k]=v; }); return o; }
  // Sprachwahl: Auswahl (?m=&k=&a=…) mitnehmen; Kapitelnummer und Dateiname gelten in allen Sprachen
  function sprachLinks(){ [].forEach.call(document.querySelectorAll(".langs a.l-item"),function(a){
    try{ var u=new URL(a.getAttribute("href"),location.href); u.search=location.search; a.setAttribute("href",u.pathname+u.search); }catch(e){} }); }
  function adresse(o){ var p=new URLSearchParams();
    Object.keys(o).forEach(function(k){ if(o[k]!=null && o[k]!=="") p.set(k,o[k]); });
    var q=p.toString(); try{ history.replaceState(null,"",location.pathname+(q?"?"+q:"")+location.hash); }catch(e){}
    sprachLinks(); }
  // Formeln in zugeklappten Lösungen erst beim Aufklappen setzen (Klasse mathe-spaeter, KATEX_OPT in wissen.js)
  document.addEventListener("toggle",function(e){ var d=e.target; if(!d || d.tagName!=="DETAILS" || !d.open) return;
    [].forEach.call(d.querySelectorAll(".mathe-spaeter"),function(x){ x.classList.remove("mathe-spaeter"); setze(x); }); },true);
  function ohneTags(h){ var d=document.createElement("div"); d.innerHTML=h||""; return (d.textContent||"").replace(/\s+/g," ").trim().toLowerCase(); }

  /* ---------- Aufgabenseite eines Moduls ---------- */
  function aufgaben(leiste){
    var S="etundso-aufgaben", seite=document.querySelector(".ag-seite");
    var alle=[].slice.call(seite.querySelectorAll(".ag")), kaps=[].slice.call(seite.querySelectorAll(".ag-kap")),
        arts=[].slice.call(seite.querySelectorAll(".ag-art"));
    if(!alle.length) return;
    var kSel=leiste.querySelector(".ag-k"), aSel=leiste.querySelector(".ag-a"), oCb=leiste.querySelector(".ag-o"),
        zufall=leiste.querySelector(".ag-zufall"), zahl=leiste.querySelector(".ag-stand"), nichts=seite.querySelector(".ag-nichts"),
        reset=seite.querySelector(".ag-reset");
    function stand(){ return $.get(S,{}); }
    function artikelOptionen(){ var k=kSel.value, alt=aSel.value; aSel.length=1;
      arts.forEach(function(sec){ if(k && sec.closest(".ag-kap").getAttribute("data-k")===k)
        aSel.appendChild(new Option(sec.querySelector("h3").textContent, sec.getAttribute("data-a"))); });
      aSel.value=alt; if(aSel.value!==alt) aSel.value=""; aSel.disabled=!k; }
    function malen(){ var s=stand();
      alle.forEach(function(x){ var g=!!s[x.getAttribute("data-id")], cb=x.querySelector(".ag-ok input");
        x.classList.toggle("ag-geloest",g); if(cb) cb.checked=g; }); }
    function zaehlen(){ var s=stand(), n=0, m=0, k=kSel.value, a=aSel.value;
      alle.forEach(function(x){ var sec=x.closest(".ag-art"), kap=x.closest(".ag-kap");
        if((!k || kap.getAttribute("data-k")===k) && (!a || sec.getAttribute("data-a")===a)){ m++; if(s[x.getAttribute("data-id")]) n++; } });
      zahl.textContent=w("ag_stand",{n:n,m:m}); }
    function filtern(){ var k=kSel.value, a=aSel.value, nur=oCb.checked, s=stand(), sichtbar=0;
      arts.forEach(function(sec){ var kap=sec.closest(".ag-kap"), ok=(!k || kap.getAttribute("data-k")===k) && (!a || sec.getAttribute("data-a")===a), n=0;
        [].forEach.call(sec.querySelectorAll(".ag"),function(x){ var z=ok && !(nur && s[x.getAttribute("data-id")]); x.hidden=!z; if(z) n++; });
        sec.hidden=!n; sichtbar+=n; });
      kaps.forEach(function(sec){ sec.hidden=!sec.querySelector(".ag-art:not([hidden])"); });
      nichts.hidden=!!sichtbar; zaehlen();
      adresse({k:k, a:a}); }
    alle.forEach(function(x){ var f=x.querySelector(".ag-fuss"), l=tx("label","ag-ok"), cb=document.createElement("input");
      cb.type="checkbox"; l.appendChild(cb); l.appendChild(document.createTextNode(" "+w("ag_geloest"))); if(f) f.insertBefore(l,f.firstChild);
      cb.addEventListener("change",function(){ var s=stand(), id=x.getAttribute("data-id");
        if(cb.checked) s[id]=heute(); else delete s[id]; $.set(S,s); malen(); zaehlen(); }); });
    kSel.addEventListener("change",function(){ artikelOptionen(); filtern(); });
    aSel.addEventListener("change",filtern);
    oCb.addEventListener("change",filtern);
    zufall.addEventListener("click",function(){ var s=stand(), sicht=alle.filter(function(x){ return !x.hidden && !x.closest("[hidden]"); }),
        offen=sicht.filter(function(x){ return !s[x.getAttribute("data-id")]; }), pool=offen.length ? offen : sicht;
      if(!pool.length) return; var x=pool[Math.floor(Math.random()*pool.length)];
      alle.forEach(function(y){ y.classList.remove("ag-hl"); }); x.classList.add("ag-hl"); x.setAttribute("tabindex","-1");
      x.scrollIntoView({block:"start",behavior:"instant"}); x.focus({preventScroll:true}); });   // weite Sprünge ohne Gleiten
    if(reset){ reset.hidden=false; $.sicher(reset,function(){ var s=stand(); alle.forEach(function(x){ delete s[x.getAttribute("data-id")]; });
      $.set(S,s); malen(); filtern(); }); }
    var p=param(); if(p.k){ kSel.value=p.k; if(kSel.value!==p.k) kSel.value=""; }
    artikelOptionen(); if(p.a){ aSel.value=p.a; if(aSel.value!==p.a) aSel.value=""; }
    leiste.hidden=false; malen(); filtern();
    if(location.hash){ var z=document.getElementById(decodeURIComponent(location.hash.slice(1))); if(z && !z.closest("[hidden]")) z.scrollIntoView(); }
  }

  /* ---------- Lernkarten, Quiz, Mischtest ---------- */
  function lernen(app){
    var MODULE=[]; try{ MODULE=JSON.parse(document.getElementById("lw-daten").textContent); }catch(e){}
    if(!MODULE.length) return;
    var liste=document.querySelector(".lw-module");
    var TYPEN=["b","f","h","l"], TYP_N={b:w("zf_begriffe"),f:w("zf_formeln"),h:w("typ_h"),l:w("zf_zusammenhaenge")},
        TYP_1={b:w("lk_begriff"),f:w("lk_formel"),h:w("herleitung"),l:w("typ1_l")};
    var K="etundso-karten", N="etundso-karten-neu", T="etundso-mischtest", AB=[0,1,3,7,14,30], NEU=20;
    var p=param(), st={m:p.m||"", k:p.k||"", a:p.a||"", arten:(p.arten||"bfhl").split("").filter(function(t){ return TYPEN.indexOf(t)>=0; }),
        modus:(/^(lernen|quiz|test)$/.test(p.modus||"") ? p.modus : "lernen")};
    if(!st.arten.length) st.arten=TYPEN.slice();
    var D=null, cache={}, laeuft=null;            // laeuft: Tastatur-Handler des aktuellen Modus
    // Gerüst: Auswahl, Kartenarten, Modus, Bühne
    var wahl=tx("div","lw-wahl"), mSel=tx("select","lw-sel"), kSel=tx("select","lw-sel"), aSel=tx("select","lw-sel");
    function feld(lbl,sel){ var l=tx("label","lw-feld"); l.appendChild(tx("span",null,lbl)); l.appendChild(sel); return l; }
    mSel.appendChild(new Option(w("lw_waehle"),""));
    MODULE.forEach(function(e){ mSel.appendChild(new Option(e.name, e.m)); });
    wahl.appendChild(feld(w("lw_modul"),mSel)); var kFeld=feld(w("lk_kapitel"),kSel), aFeld=feld(w("lw_artikel"),aSel);
    wahl.appendChild(kFeld); wahl.appendChild(aFeld);
    var arten=tx("fieldset","lw-arten"); arten.appendChild(tx("legend",null,w("lw_arten")));
    var artCb={};
    TYPEN.forEach(function(t){ var l=tx("label","lw-art"), cb=document.createElement("input"); cb.type="checkbox"; cb.value=t;
      cb.checked=st.arten.indexOf(t)>=0; artCb[t]={cb:cb, n:tx("span","lw-n")}; l.appendChild(cb); l.appendChild(document.createTextNode(" "+TYP_N[t]+" "));
      l.appendChild(artCb[t].n); arten.appendChild(l);
      cb.addEventListener("change",function(){ st.arten=TYPEN.filter(function(x){ return artCb[x].cb.checked; }); neu(); }); });
    var modi=tx("div","lw-modi"); modi.setAttribute("role","group"); var modB={};
    [["lernen","mod_lernen"],["quiz","mod_quiz"],["test","mod_test"]].forEach(function(x){ var b=knopf("lw-modus",w(x[1]));
      b.setAttribute("data-modus",x[0]); modB[x[0]]=b; modi.appendChild(b);
      b.addEventListener("click",function(){ st.modus=x[0]; neu(); }); });
    var buehne=tx("div","lw-buehne"); buehne.setAttribute("aria-live","polite");
    app.appendChild(wahl); app.appendChild(arten); app.appendChild(modi); app.appendChild(buehne);
    app.hidden=false;

    function eintrag(m){ for(var i=0;i<MODULE.length;i++) if(MODULE[i].m===m) return MODULE[i]; return null; }
    function kapitel(n){ if(!D) return null; for(var i=0;i<D.kap.length;i++) if(String(D.kap[i].n)===String(n)) return D.kap[i]; return null; }
    function artIndex(){ var k=kapitel(st.k); if(!k || !st.a) return -1; for(var i=0;i<k.a.length;i++) if(k.a[i][0]===st.a) return i; return -1; }
    function artikelVon(c){ var k=kapitel(c.k); return k ? k.a[c.a] : null; }
    function stelle(c){ var a=artikelVon(c); return a ? a[2]+(c.h?"#"+c.h:"") : "#"; }
    function kopfText(c){ var k=kapitel(c.k), a=artikelVon(c); return TYP_1[c.t]+" · "+(k?k.t.split(/\s*[:：]\s*/)[0]:"")+(a?" · "+a[1]:""); }
    function antwort(c){ return c.q || c.r || ""; }
    // Auswahl: Modul -> Kapitel -> Artikel; ohne Kartenarten-Filter (für die Zahlen an den Kästchen)
    function ausschnitt(){ if(!D) return []; var ai=artIndex();
      return D.karten.filter(function(c){ return (!st.k || String(c.k)===String(st.k)) && (ai<0 || c.a===ai); }); }
    function auswahl(){ return ausschnitt().filter(function(c){ return st.arten.indexOf(c.t)>=0; }); }
    function schreibeAdresse(){ adresse({m:st.m, k:st.k, a:st.a, arten:(st.arten.length===4?"":st.arten.join("")), modus:(st.modus==="lernen"?"":st.modus)}); }
    function optionenFuellen(){
      kSel.length=0; aSel.length=0; kSel.appendChild(new Option(w("lk_alle_kap"),"")); aSel.appendChild(new Option(w("lw_alle_art"),""));
      if(D) D.kap.forEach(function(k){ kSel.appendChild(new Option(k.t, String(k.n))); });
      kSel.value=st.k; if(kSel.value!==String(st.k)){ st.k=""; kSel.value=""; }
      var k=kapitel(st.k); if(k) k.a.forEach(function(a){ aSel.appendChild(new Option(a[1], a[0])); });
      aSel.value=st.a; if(aSel.value!==st.a){ st.a=""; aSel.value=""; }
      kFeld.hidden=!D; aFeld.hidden=!D || !st.k; }
    function zahlen(){ var a=ausschnitt(), n={b:0,f:0,h:0,l:0}; a.forEach(function(c){ n[c.t]++; });
      TYPEN.forEach(function(t){ artCb[t].n.textContent="("+n[t]+")"; }); }
    mSel.addEventListener("change",function(){ st.m=mSel.value; st.k=""; st.a=""; laden(); });
    kSel.addEventListener("change",function(){ st.k=kSel.value; st.a=""; neu(); });
    aSel.addEventListener("change",function(){ st.a=aSel.value; neu(); });
    if(liste) liste.addEventListener("click",function(e){ var a=e.target.closest && e.target.closest("a.bm-t[data-m]"); if(!a) return;
      e.preventDefault(); st.m=a.getAttribute("data-m"); st.k=""; st.a=""; laden(); window.scrollTo(0,0); });
    document.addEventListener("keydown",function(e){
      if(!laeuft || e.ctrlKey || e.metaKey || e.altKey) return;
      var t=e.target, tag=t && t.tagName; if(tag==="INPUT" || tag==="SELECT" || tag==="TEXTAREA" || (t && t.isContentEditable)) return;
      var ov=document.getElementById("searchOverlay"); if(ov && !ov.hidden) return;
      laeuft(e, tag); });

    function laden(){
      var e=eintrag(st.m); mSel.value=e ? e.m : ""; D=null; laeuft=null;
      if(!e){ st.m=""; optionenFuellen(); zahlen(); arten.hidden=modi.hidden=true; buehne.innerHTML=""; buehne.appendChild(tx("p","lw-hinweis",w("lw_waehle")));
        if(liste) liste.hidden=false; schreibeAdresse(); return; }
      if(liste) liste.hidden=true;
      buehne.innerHTML=""; buehne.appendChild(tx("p","lw-hinweis",w("baum_laedt")));
      (cache[e.m] || (cache[e.m]=fetch(e.d).then(function(r){ if(!r.ok) throw r.status; return r.json(); })))
        .then(function(d){ if(st.m!==e.m) return; D=d; neu(); })
        .catch(function(){ delete cache[e.m]; buehne.innerHTML=""; buehne.appendChild(tx("p","lw-hinweis",w("baum_fehler"))); });
    }
    function neu(){ laeuft=null; optionenFuellen(); zahlen(); arten.hidden=modi.hidden=!D;
      Object.keys(modB).forEach(function(m){ modB[m].setAttribute("aria-pressed", m===st.modus ? "true" : "false"); });
      schreibeAdresse(); buehne.innerHTML="";
      if(!D) return;
      if(st.modus==="quiz") quizStart(); else if(st.modus==="test") testStart(); else lernStapel(); }

    /* Lernen: Leitner-Fächer wie W2 (Fach 1–5 = 1, 3, 7, 14, 30 Tage; neue Karten 20 je Tag und Modul) */
    function lernStapel(){
      var karten=auswahl(), gerade={}, extra=0, schlange=[], jetzt=null, schritt=0;
      var zahlEl=tx("p","lk-zahl"), karte=tx("div","lk-karte"), kopf=tx("div","lk-kopf"), vorne=tx("div","lk-vorne"), hinten=tx("div","lk-hinten"),
          steuer=tx("div","lk-steuer"), um=knopf("lk-um",w("lk_umdrehen")), bew=tx("div","lk-bew"), ende=tx("div","lk-ende"), neuB=knopf("lk-neu",""),
          fuss=tx("div","lk-fuss"), stelleA=tx("a","lk-stelle",w("lk_stelle")), reset=knopf("lern-reset lk-reset",w("lk_reset"));
      zahlEl.setAttribute("aria-live","polite"); karte.tabIndex=-1;
      karte.appendChild(kopf); karte.appendChild(vorne); karte.appendChild(hinten);
      [["lk_schlecht",0],["lk_mittel",1],["lk_gut",2]].forEach(function(x){ var b=knopf("lk-b lk-b"+x[1],w(x[0])); b.appendChild(tx("small"));
        b.addEventListener("click",function(){ bewerten(x[1]); }); bew.appendChild(b); });
      steuer.appendChild(um); steuer.appendChild(bew);
      ende.appendChild(tx("p",null,w("lk_fertig"))); ende.appendChild(neuB);
      fuss.appendChild(stelleA); fuss.appendChild(tx("span","lk-tasten",w("lk_tasten")));
      if(!karten.length){ buehne.appendChild(tx("p","lw-hinweis",w("lw_keine"))); return; }
      [zahlEl,karte,steuer,ende,fuss].forEach(function(e){ buehne.appendChild(e); });
      if(!$.ok) buehne.appendChild(tx("p","lk-hinweis",w("lk_ohne_speicher")));
      buehne.appendChild(reset);
      function stand(){ return $.get(K,{}); }
      function neuHeute(){ var e=$.get(N,{})[D.mp]; return (e && e[0]===heute()) ? e[1] : 0; }
      function neuZaehlen(){ var n=$.get(N,{}); n[D.mp]=[heute(),neuHeute()+1]; $.set(N,n); }
      function fach(b,r,id){ return r===0 ? 1 : r===1 ? Math.max(1,b) : gerade[id] ? 1 : Math.min(5,Math.max(1,b)+1); }
      function tage(d){ return d===0 ? w("lk_heute") : d===1 ? w("lk_morgen") : w("lk_tage",{n:d}); }
      function baue(){ var s=stand(), t=heute(), faellig=[], neue=[];
        karten.forEach(function(c){ var x=s[c.id]; if(x){ if(x[1]<=t) faellig.push(c); } else neue.push(c); });
        faellig.sort(function(a,b){ return s[a.id][1]-s[b.id][1] || s[a.id][0]-s[b.id][0]; });
        schlange=faellig.concat(neue.slice(0,Math.max(0,NEU-neuHeute())+extra)); zeige(); }
      function abschnitt(label,h,cls){ var d=hx("div",cls||"hl-teil"); d.appendChild(tx("span","hl-k",label)); d.appendChild(hx("div","hl-i",h)); return d; }
      function schritte(c){ return c.t==="h" ? (c.s||[]) : []; }
      function zeige(){
        var s=stand(), n=0; schlange.forEach(function(c){ if(!s[c.id]) n++; });
        zahlEl.textContent=w("lk_faellig",{n:schlange.length})+(n?" · "+w("lk_davon_neu",{n:n}):"");
        jetzt=schlange[0]||null; karte.hidden=steuer.hidden=fuss.hidden=!jetzt; ende.hidden=!!jetzt;
        if(!jetzt){ var rest=karten.filter(function(c){ return !s[c.id]; }).length; neuB.hidden=!rest; neuB.textContent=w("lk_mehr_neu",{n:Math.min(NEU,rest)}); return; }
        kopf.textContent=kopfText(jetzt); vorne.innerHTML=jetzt.v; hinten.innerHTML=""; hinten.hidden=true; schritt=0;
        if(jetzt.t==="h"){ if(jetzt.z) vorne.appendChild(abschnitt(w("hl_ziel"),jetzt.z,"hl-teil hl-ziel"));
          if(jetzt.s0) vorne.appendChild(abschnitt(w("hl_start"),jetzt.s0));
          var ss=schritte(jetzt), off=jetzt.s0?1:0;
          ss.forEach(function(h,i){ var d=abschnitt(w("hl_schritt",{n:i+1+off,m:ss.length+off}),h); d.hidden=true; hinten.appendChild(d); });
        } else hinten.innerHTML=jetzt.r||"";
        stelleA.href=stelle(jetzt); um.hidden=false; bew.hidden=true; um.textContent=jetzt.t==="h" ? w("hl_weiter") : w("lk_umdrehen");
        var x=s[jetzt.id], b=x?x[0]:0;
        [0,1,2].forEach(function(r){ var sm=bew.querySelector(".lk-b"+r+" small"); if(sm) sm.textContent=tage(r===0?0:AB[fach(b,r,jetzt.id)]); });
        setze(karte); }
      function umdrehen(){ if(!jetzt) return; if(!bew.hidden) return;
        if(jetzt.t==="h"){ var teile=hinten.children; hinten.hidden=false;
          if(schritt<teile.length){ teile[schritt].hidden=false; schritt++; }
          if(schritt<teile.length) return; }
        hinten.hidden=false; um.hidden=true; bew.hidden=false; karte.focus({preventScroll:true});
        var r=bew.getBoundingClientRect(); if(r.bottom>window.innerHeight) bew.scrollIntoView({block:"end",behavior:"smooth"}); }
      function bewerten(r){ if(!jetzt || bew.hidden) return;
        var s=stand(), x=s[jetzt.id], c=jetzt, f=fach(x?x[0]:0,r,c.id);
        if(!x) neuZaehlen();
        s[c.id]=[f, heute()+(r===0?0:AB[f])]; $.set(K,s); schlange.shift();
        if(r===0){ gerade[c.id]=1; schlange.push(c); }
        zeige(); if(!karte.hidden) karte.focus({preventScroll:true}); else if(!neuB.hidden) neuB.focus(); }
      um.addEventListener("click",umdrehen);
      karte.addEventListener("click",function(e){ if(!(e.target.closest && e.target.closest("a"))) umdrehen(); });
      neuB.addEventListener("click",function(){ extra+=NEU; baue(); });
      $.sicher(reset,function(){ var s=stand(), n=$.get(N,{}); karten.forEach(function(c){ delete s[c.id]; }); delete n[D.mp];
        $.set(K,s); $.set(N,n); extra=0; gerade={}; baue(); });
      laeuft=function(e,tag){
        if((e.key===" " || e.key==="Enter") && jetzt && bew.hidden){ if(tag==="BUTTON" || tag==="A") return; e.preventDefault(); umdrehen(); }
        else if(jetzt && !bew.hidden && (e.key==="1" || e.key==="2" || e.key==="3")){ e.preventDefault(); bewerten(+e.key-1); } };
      baue();
    }

    /* Quiz und Mischtest: Mehrfachauswahl. Falsche Antworten sind echte Antworten anderer Karten derselben Art, zuerst aus
       demselben Kapitel, sonst aus dem Modul; Herleitungen kommen nicht vor. */
    function quizfaehig(c){ return c.t!=="h" && !!antwort(c); }
    function optionen(c){ var ant=antwort(c), seen={}, pool=[]; seen[ohneTags(ant)]=1;
      var kap=D.karten.filter(function(x){ return x.t===c.t && x.k===c.k && x.id!==c.id && quizfaehig(x); }),
          mod=D.karten.filter(function(x){ return x.t===c.t && x.k!==c.k && quizfaehig(x); });
      mische(kap).concat(mische(mod)).forEach(function(x){ var n=ohneTags(antwort(x)); if(pool.length<3 && n && !seen[n]){ seen[n]=1; pool.push(x.id); } });
      return pool.length<3 ? null : mische([c.id].concat(pool)); }
    function karteVon(id){ for(var i=0;i<D.karten.length;i++) if(D.karten[i].id===id) return D.karten[i]; return null; }
    function frageText(c){ return c.w ? w("quiz_p_w") : w("quiz_p_"+c.t); }
    function zahlWahl(){ var l=tx("label","lw-feld"), s=tx("select","lw-sel lw-zahl"); l.appendChild(tx("span",null,w("quiz_zahl"))); l.appendChild(s);
      [10,20,30].forEach(function(n){ s.appendChild(new Option(String(n),String(n))); }); return [l,s]; }
    // Eine Mehrfachauswahl-Frage zeichnen. modus "quiz": nach der Wahl gleich zeigen, ob richtig; "test": nur die Wahl
    // merken (Mischtest); "zeigen": Ergebnis zeigen, nichts mehr wählbar (Auswertung des Mischtests)
    function mcFrage(ziel, f, modus, fertig){ var sofort=modus==="quiz";
      var c=karteVon(f.id), box=tx("div","qz-frage");
      box.appendChild(tx("p","qz-p",frageText(c))); box.appendChild(hx("div","qz-vorne",c.v));
      var ol=tx("ol","qz-opt"), bs=[];
      f.o.forEach(function(id,i){ var x=karteVon(id), li=tx("li"), b=knopf("qz-b"); b.innerHTML='<span class="qz-nr">'+(i+1)+'</span><span class="qz-a">'+(x?antwort(x):"")+'</span>';
        if(f.w===i) b.classList.add("gewaehlt");
        b.addEventListener("click",function(){ waehle(i); }); li.appendChild(b); ol.appendChild(li); bs.push(b); });
      box.appendChild(ol); ziel.appendChild(box);
      function markieren(){ var r=f.o.indexOf(f.id);
        bs.forEach(function(b,i){ b.disabled=true; if(i===r){ b.classList.add("ok"); b.setAttribute("aria-label",w("q_ok")+": "+b.textContent); }
          else if(i===f.w){ b.classList.add("nein"); b.setAttribute("aria-label",w("q_nein")+": "+b.textContent); } }); }
      function waehle(i){ if(sofort && f.w>=0) return; f.w=i; bs.forEach(function(b,j){ b.classList.toggle("gewaehlt",j===i); });
        if(sofort) markieren(); if(fertig) fertig(); }
      if((sofort && f.w>=0) || modus==="zeigen") markieren();
      setze(box);
      return waehle; }
    function fehlerListe(items){ var ol=tx("ol","qz-fehler");
      items.forEach(function(f){ var c=karteVon(f.id), li=tx("li"); if(!c) return;
        li.appendChild(hx("div","qz-vorne",c.v));
        if(f.w>=0){ var d=karteVon(f.o[f.w]); li.appendChild(hx("div","qz-deine",'<span class="hl-k">'+w("quiz_deine")+'</span> '+(d?antwort(d):""))); }
        li.appendChild(hx("div","qz-richtig",'<span class="hl-k">'+w("quiz_richtig")+'</span> '+antwort(c)));
        var a=tx("a","lk-stelle",w("lk_stelle")); a.href=stelle(c); li.appendChild(a); ol.appendChild(li); });
      return ol; }

    function quizStart(){
      var kandidaten=auswahl().filter(quizfaehig), zw=zahlWahl(), start=knopf("lk-um qz-start",w("quiz_start")), box=tx("div","qz-setup");
      box.appendChild(zw[0]); box.appendChild(start); buehne.appendChild(box);
      var moeglich=kandidaten.filter(function(c){ return !!optionen(c); });
      if(!moeglich.length){ start.disabled=true; buehne.appendChild(tx("p","lw-hinweis",w("quiz_zu_wenig"))); return; }
      start.addEventListener("click",function(){ var n=+zw[1].value, fr=[];
        mische(moeglich).forEach(function(c){ if(fr.length<n){ var o=optionen(c); if(o) fr.push({id:c.id,o:o,w:-1}); } });
        quizLauf(fr); });
    }
    function quizLauf(fr){
      var i=0; buehne.innerHTML="";
      var kopf=tx("p","qz-kopf"), platz=tx("div"), weiter=knopf("lk-um qz-weiter",""), hinweis=tx("p","lk-tasten",w("quiz_tasten"));
      buehne.appendChild(kopf); buehne.appendChild(platz); buehne.appendChild(weiter); buehne.appendChild(hinweis);
      var waehle=null;
      function zeige(){ platz.innerHTML=""; kopf.textContent=w("quiz_frage",{n:i+1,m:fr.length})+" · "+TYP_1[karteVon(fr[i].id).t];
        weiter.hidden=true; weiter.textContent=i+1<fr.length ? w("quiz_weiter") : w("quiz_ende");
        waehle=mcFrage(platz,fr[i],"quiz",function(){ weiter.hidden=false; weiter.focus({preventScroll:true}); }); }
      weiter.addEventListener("click",function(){ if(i+1<fr.length){ i++; zeige(); kopf.scrollIntoView({block:"nearest"}); } else quizEnde(fr); });
      laeuft=function(e){ var z=parseInt(e.key,10); if(z>=1 && z<=4 && fr[i].w<0){ e.preventDefault(); waehle(z-1); }
        else if(e.key==="Enter" && !weiter.hidden && document.activeElement!==weiter){ e.preventDefault(); weiter.click(); } };
      zeige();
    }
    function quizEnde(fr){ laeuft=null; buehne.innerHTML="";
      var ok=fr.filter(function(f){ return f.w>=0 && f.o[f.w]===f.id; }).length, falsch=fr.filter(function(f){ return !(f.w>=0 && f.o[f.w]===f.id); });
      buehne.appendChild(tx("h2","qz-h",w("quiz_auswertung")));
      buehne.appendChild(tx("p","qz-ergebnis",w("quiz_ergebnis",{n:ok,m:fr.length})));
      if(falsch.length){ buehne.appendChild(tx("h3","qz-h3",w("quiz_falsch"))); buehne.appendChild(fehlerListe(falsch)); }
      else buehne.appendChild(tx("p",null,w("quiz_alle")));
      var nb=knopf("lk-um",w("quiz_neu")); nb.addEventListener("click",neu); buehne.appendChild(nb);
      setze(buehne); buehne.querySelector(".qz-h").scrollIntoView({block:"start"}); }

    /* Mischtest: Kapitel wählen, Zahl der Fragen; Quizfragen und Aufgaben gemischt. Aufgaben stammen aus der statischen
       Aufgabenseite des Moduls (einmal geladen). Lösungen und Auswertung erst am Ende; Aufgaben bewertet der Leser selbst
       (richtig 1, teilweise ½, falsch 0). Ein laufender Test bleibt gespeichert (etundso-mischtest). */
    var AUFG={};                                         // Moduladresse -> Promise {id: {k, html, stelle, titel}}
    function aufgabenLaden(){ var u=D.aufg;
      if(!AUFG[u]) AUFG[u]=fetch(u).then(function(r){ if(!r.ok) throw r.status; return r.text(); }).then(function(t){
        var doc=new DOMParser().parseFromString(t,"text/html"), o={};
        [].forEach.call(doc.querySelectorAll(".ag-kap"),function(kap){ var k=kap.getAttribute("data-k");
          [].forEach.call(kap.querySelectorAll(".ag"),function(x){ var a=x.querySelector(".aufg"), s=x.querySelector(".ag-stelle");
            if(a) o[x.getAttribute("data-id")]={k:k, html:a.outerHTML, stelle:s?s.getAttribute("href"):"#"}; }); });
        return o; }).catch(function(e){ delete AUFG[u]; throw e; });
      return AUFG[u]; }
    function testLaden(){ var t=$.get(T,{}); return (t.m===D.m && t.l===$.lang && t.f && t.f.length) ? t : null; }
    function testStart(){
      buehne.appendChild(tx("p","lede lern-lede",w("test_lede")));
      var alt=testLaden();
      if(alt){ var fb=knopf("lk-um mt-fort",w("test_fortsetzen")); buehne.appendChild(fb); fb.addEventListener("click",function(){ testLauf(alt); }); }
      var fs=tx("fieldset","mt-kap"); fs.appendChild(tx("legend",null,w("test_kapitel")));
      var alleL=tx("label","mt-alle"), alleCb=document.createElement("input"); alleCb.type="checkbox"; alleL.appendChild(alleCb);
      alleL.appendChild(document.createTextNode(" "+w("test_alle"))); fs.appendChild(alleL);
      var cbs=D.kap.map(function(k){ var l=tx("label","mt-k"), cb=document.createElement("input"); cb.type="checkbox"; cb.value=String(k.n);
        cb.checked=!st.k || String(k.n)===String(st.k); l.appendChild(cb); l.appendChild(document.createTextNode(" "+k.t)); fs.appendChild(l); return cb; });
      function alleStand(){ alleCb.checked=cbs.every(function(c){ return c.checked; }); }
      alleCb.addEventListener("change",function(){ cbs.forEach(function(c){ c.checked=alleCb.checked; }); });
      cbs.forEach(function(c){ c.addEventListener("change",alleStand); }); alleStand();
      var zw=zahlWahl(), start=knopf("lk-um mt-start",w("test_start")), meldung=tx("p","lw-hinweis");
      buehne.appendChild(fs); var box=tx("div","qz-setup"); box.appendChild(zw[0]); box.appendChild(start); buehne.appendChild(box); buehne.appendChild(meldung);
      start.addEventListener("click",function(){
        var kap=cbs.filter(function(c){ return c.checked; }).map(function(c){ return c.value; });
        if(!kap.length){ meldung.textContent=w("test_kein_kap"); return; }
        var n=+zw[1].value; start.disabled=true; meldung.textContent=w("baum_laedt");
        var karten=D.karten.filter(function(c){ return kap.indexOf(String(c.k))>=0 && st.arten.indexOf(c.t)>=0 && quizfaehig(c) && optionen(c); });
        function bauen(auf,ohne){ var ids=Object.keys(auf).filter(function(id){ return kap.indexOf(String(auf[id].k))>=0; });
          var nA=Math.min(ids.length, Math.round(n/2)), nQ=Math.min(karten.length, n-nA); nA=Math.min(ids.length, n-nQ);
          var f=mische(karten).slice(0,nQ).map(function(c){ return {t:"q", id:c.id, o:optionen(c), w:-1}; })
            .concat(mische(ids).slice(0,nA).map(function(id){ return {t:"a", id:id, b:null}; }));
          if(!f.length){ start.disabled=false; meldung.textContent=w("lw_keine"); return; }
          var t={m:D.m, l:$.lang, f:mische(f), i:0, ende:false, ohne:!!ohne}; $.set(T,t); testLauf(t); }
        aufgabenLaden().then(function(a){ bauen(a,false); },function(){ bauen({},true); });
      });
    }
    function testLauf(t){
      aufgabenLaden().catch(function(){ return {}; }).then(function(auf){
        t.f=t.f.filter(function(f){ return f.t==="q" ? !!karteVon(f.id) : !!auf[f.id]; });
        if(!t.f.length){ $.del(T); neu(); return; }
        if(t.ende){ testEnde(t,auf); return; }
        buehne.innerHTML="";
        var kopf=tx("p","qz-kopf"), platz=tx("div"), weiter=knopf("lk-um qz-weiter",""), hinweis=tx("p","lk-tasten",w("quiz_tasten"));
        if(t.ohne) buehne.appendChild(tx("p","lw-hinweis",w("test_ohne_aufg")));
        [kopf,platz,weiter,hinweis].forEach(function(e){ buehne.appendChild(e); });
        var waehle=null;
        function zeige(){ var f=t.f[t.i]; platz.innerHTML=""; waehle=null;
          kopf.textContent=w("quiz_frage",{n:t.i+1,m:t.f.length})+" · "+(f.t==="q" ? TYP_1[karteVon(f.id).t] : w("w_aufgabe"));
          weiter.textContent=t.i+1<t.f.length ? w("quiz_weiter") : w("quiz_ende");
          if(f.t==="q") waehle=mcFrage(platz,f,"test",function(){ $.set(T,t); });
          else { var d=hx("div","mt-aufg",auf[f.id].html); [].forEach.call(d.querySelectorAll("details.loesung"),function(x){ x.parentNode.removeChild(x); });
            platz.appendChild(d); platz.appendChild(tx("p","lw-hinweis",w("test_aufg_hinweis"))); setze(d); } }
        weiter.addEventListener("click",function(){ if(t.i+1<t.f.length){ t.i++; $.set(T,t); zeige(); kopf.scrollIntoView({block:"nearest"}); }
          else { t.ende=true; $.set(T,t); testEnde(t,auf); } });
        laeuft=function(e){ var z=parseInt(e.key,10); if(waehle && z>=1 && z<=4){ e.preventDefault(); waehle(z-1); }
          else if(e.key==="Enter" && document.activeElement!==weiter){ e.preventDefault(); weiter.click(); } };
        zeige();
      });
    }
    function testEnde(t,auf){ laeuft=null; buehne.innerHTML="";
      var kopf=tx("h2","qz-h",w("quiz_auswertung")), erg=tx("p","qz-ergebnis"), offen=tx("p","lw-hinweis"), nochmal=tx("div","mt-nochmal");
      [kopf,erg,offen,nochmal].forEach(function(e){ buehne.appendChild(e); });
      var ol=tx("ol","mt-liste"); buehne.appendChild(ol);
      function rechnen(){ var p=0, m=t.f.length, o=0, falsch=[];
        t.f.forEach(function(f){ if(f.t==="q"){ if(f.w>=0 && f.o[f.w]===f.id) p++; else falsch.push(f); }
          else { if(f.b==null) o++; else { p+=f.b; if(f.b<1) falsch.push(f); } } });
        erg.textContent=w("test_punkte",{p:String(Math.round(p*10)/10).replace(".",$.lang==="en"||$.lang==="zh"?".":","),m:m});
        offen.textContent=o ? w("test_offen",{n:o}) : ""; offen.hidden=!o;
        nochmal.innerHTML=""; if(falsch.length){ nochmal.appendChild(tx("h3","qz-h3",w("quiz_falsch")));
          var ul=tx("ul","mt-links"); falsch.forEach(function(f){ var li=tx("li"), a=tx("a");
            if(f.t==="q"){ var c=karteVon(f.id); a.innerHTML=c.v; a.href=stelle(c); li.appendChild(tx("span","hl-k",TYP_1[c.t]+": ")); }
            else { var x=hx("div",null,auf[f.id].html), h=x.querySelector(".aufg-h"); a.innerHTML=h?h.innerHTML:w("w_aufgabe"); a.href=auf[f.id].stelle;
              li.appendChild(tx("span","hl-k",w("w_aufgabe")+": ")); }
            li.appendChild(a); ul.appendChild(li); }); nochmal.appendChild(ul); setze(nochmal); } }
      t.f.forEach(function(f,i){ var li=tx("li","mt-e");
        if(f.t==="q"){ var c=karteVon(f.id), r=f.w>=0 && f.o[f.w]===f.id;
          li.classList.add(r?"mt-ok":"mt-nein"); li.appendChild(tx("p","qz-kopf",TYP_1[c.t]+" · "+(r?w("q_ok"):w("q_nein"))));
          var platz=tx("div"); li.appendChild(platz); mcFrage(platz,f,"zeigen",null);
          var a=tx("a","lk-stelle",w("lk_stelle")); a.href=stelle(c); li.appendChild(a); }
        else { li.appendChild(tx("p","qz-kopf",w("w_aufgabe")));
          var d=hx("div","mt-aufg",auf[f.id].html); [].forEach.call(d.querySelectorAll("details.loesung"),function(x){ x.open=true; });
          [].forEach.call(d.querySelectorAll(".mathe-spaeter"),function(x){ x.classList.remove("mathe-spaeter"); });
          li.appendChild(d); var s=tx("div","mt-selbst"); s.appendChild(tx("span","hl-k",w("test_selbst")));
          [["bew_richtig",1],["bew_teil",0.5],["bew_falsch",0]].forEach(function(x){ var b=knopf("mt-b",w(x[0]));
            b.setAttribute("aria-pressed",f.b===x[1]?"true":"false");
            b.addEventListener("click",function(){ f.b=x[1]; $.set(T,t); [].forEach.call(s.querySelectorAll(".mt-b"),function(y){ y.setAttribute("aria-pressed",y===b?"true":"false"); });
              li.classList.toggle("mt-ok",f.b===1); li.classList.toggle("mt-teil",f.b===0.5); li.classList.toggle("mt-nein",f.b===0); rechnen(); });
            s.appendChild(b); });
          if(f.b!=null) li.classList.add(f.b===1?"mt-ok":f.b===0?"mt-nein":"mt-teil");
          li.appendChild(s); var a2=tx("a","lk-stelle",w("lk_stelle")); a2.href=auf[f.id].stelle; li.appendChild(a2); }
        ol.appendChild(li); });
      var nb=knopf("lk-um",w("test_neu")); nb.addEventListener("click",function(){ $.del(T); neu(); }); buehne.appendChild(nb);
      rechnen(); setze(ol); kopf.scrollIntoView({block:"start"}); }

    // Start: Auswahl aus der Adresse
    if(st.m) laden(); else { optionenFuellen(); zahlen(); arten.hidden=modi.hidden=true; sprachLinks(); }
  }

  var leiste=document.querySelector(".ag-seite .ag-leiste"); if(leiste) aufgaben(leiste);
  var app=document.querySelector(".lw-app"); if(app) lernen(app);
})();
"""

if __name__ == "__main__":
    main()
