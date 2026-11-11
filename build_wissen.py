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

def zf_start():
    ZF.clear()
    ZF.update(an=True, fb=[], fm=[], kg=[], schon=set(), n=0, h="")

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
    return hid

def _zf_kurz(txt):
    """„Kurz gesagt: …“ sammeln (alle Sprachen); Rückgabe: id für den Absatz oder ""."""
    m = KURZ_RE.match(txt)
    if not m or not _zf_haupt():
        return ""
    hid = _zf_id("kg")
    ZF["kg"].append({"id": hid, "md": txt[m.end():].strip()})
    return hid

def _ohne_links(md):
    return re.sub(r"(?<!!)\[([^\]]+)\]\([^)]+\)", r"\1", md)

def zusammenfassung_html(z):
    """Kasten „Zusammenfassung“ (am Artikelende, immer offen) aus dem Sammler ZF; ohne Material: ""."""
    gruppen = []
    def gruppe(wort, cls, punkte):
        if not punkte:
            return
        rest = len(punkte) - ZF_SICHTBAR
        if rest <= 1:                                          # „1 weitere zeigen“ lohnt nicht
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
        namen = ", ".join(f'<a class="zf-b" href="#{x["id"]}">{inline(_ohne_links(x["md"]))}</a>' for x in gleich)
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
        punkte.append(f'<li><a class="zf-fl" href="#{f["id"]}">{kopf}</a><div class="zf-f">{formel}</div></li>')
    gruppe("zf_formeln", "formeln", punkte)
    gruppe("zf_zusammenhaenge", "zusammenhaenge",
           [f'<li><a class="zf-a" href="#{k["id"]}">{inline(_ohne_links(k["md"]))}</a></li>' for k in z["kg"]])
    if not gruppen:
        return ""
    return (f'<aside class="zf" id="zusammenfassung" aria-labelledby="zf-titel"><h2 class="zf-t" id="zf-titel">{T("zf")}</h2>'
            + "".join(gruppen) + "</aside>")

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
    def beispiel(arg, inner):                             # Beispiel: zugeklappte Box „Beispiel: Titel“, ohne Nummer (wie im Heft)
        wort, titel = T("beispiel"), arg                  # Kopf: „[Rechenbeispiel 2] Titel“, „[Gegenbeispiel]“, „Titel“ oder leer
        mw = re.match(r"\[([^\]]*)\]\s*(.*)$", arg)
        if mw:
            wort, titel = (mw.group(1).strip() or T("beispiel")), mw.group(2).strip()
        out.append(f'<details class="beispiel"><summary><span class="bsp-k">{inline(wort)}</span>' + inline(titel) + '</summary>'
                   '<div class="bsp-body">' + _innen("beispiel", titel, inner) + '</div></details>')
    def vorwissen(arg, inner):                            # „Was du dafür brauchst: Titel“: zugeklappte Box (User, 10.11.2026)
        kopf, titel = arg, ""                             # Kopf bis zum ersten Doppelpunkt (auch „：“ und „ :“), dann der Titel
        mk = re.match(r"(.+?)\s*[:：]\s*(.*)$", arg)
        if mk:
            kopf, titel = mk.group(1).strip(), mk.group(2).strip()
        out.append(f'<details class="vorwissen"><summary><span class="vo-k">{inline(kopf)}</span>' + inline(titel) + '</summary>'
                   '<div class="vo-body">' + _innen("vorwissen", titel, inner) + '</div></details>')
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
                if mf and "$$" not in mf.group(1):
                    zid = _zf_formel(mf.group(1).strip(), nr_roh)
                else:
                    zid = _zf_kurz(txt)
                    txt = _zf_begriffe(txt)
                ida = f' id="{zid}"' if zid else ""
                parts = split_display(txt)
                if parts:                                # mehrteilige Formelzeile: Teile dürfen umbrechen
                    inhalt = (f'<div class="mrow"{"" if nummer else ida}>' + "".join('<div class="mcell">' + inline("$$" + p + "$$") + "</div>"
                                                             for p in parts) + "</div>")
                else:
                    inhalt = inline(txt) if nummer else f"<p{ida}>" + inline(txt) + "</p>"
                out.append(f'<div class="gl-zeile"{ida}><div class="gl-f">{inhalt}</div><div class="gl-nr">{nummer}</div></div>' if nummer else inhalt)
            para.clear()
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:                                     # blank -> paragraph break
            flush(); i += 1; continue
        if s.startswith("```"):                       # fenced code: ```<sprache> <titel>
            flush(); info = s[3:].strip(); i += 1; code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            out.append(code_html(info, "\n".join(code)))
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
            out.append(f'<aside class="callout cx-quiz"><div class="callout-h">{T("quiz")}</div>'
                       + "".join(body) + "</aside>")
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
            if kind == "beispiel":                        # Kurzform :::beispiel … ::: (ohne innere Blöcke)
                beispiel(label_arg, inner)
                continue
            if kind == "kern" and section_open:           # „Das Wichtigste" steht als eigene Box außerhalb der Abschnitts-Karten
                out.append("</section>"); section_open = False
            if kind == "formel":                          # wichtige Formel: Box mit Typ-Label (Definition/Satz/…) + Nummer
                formel_n += 1
                lbl = label_arg or "Formel"
                out.append(f'<div class="fbox"><div class="fbox-h"><span class="fbox-t">{html.escape(lbl)}</span>'
                           f'<span class="fbox-n">({formel_n})</span></div>'
                           + _innen("formel", lbl, inner) + '</div>')
                continue
            if kind in ("herleitung", "beweis"):          # Herleitung oder Beweis als ausklappbare Box an der Formel
                out.append(f'<details class="herleitung"><summary>{T(kind)}' + (": " + inline(label_arg) if label_arg else "") + '</summary>'
                           '<div class="hl-body">' + _innen(kind, label_arg, inner) + '</div></details>')
                continue
            if kind == "zweck":                           # Einstieg einer Stufe: wozu sie da ist
                out.append(f'<div class="zweck"><span class="zw-k">{T("zweck")}</span> ' + _innen("zweck", "", inner) + '</div>')
                continue
            if kind == "aufgabe":                         # Aufgabe mit Nummer und Sternen, Lösung als Ausklappblock darin
                out.append('<div class="aufg"><div class="aufg-h">' + inline(label_arg) + '</div>'
                           '<div class="aufg-b">' + _innen("aufgabe", label_arg, inner) + '</div></div>')
                continue
            if kind == "loesung":
                out.append(f'<details class="loesung"><summary>{T("loesung")}</summary>'
                           '<div class="lo-body">' + _innen("loesung", "", inner) + '</div></details>')
                continue
            if kind == "zusatz":                          # Vertiefung: darf übersprungen werden
                out.append(f'<aside class="callout cx-zusatz"><div class="callout-h">{T("zusatz")}'
                           + (": " + inline(label_arg) if label_arg else "") + '</div>' + _innen("zusatz", label_arg, inner) + "</aside>")
                continue
            if kind == "warnung":                         # Achtung (Recht, Datenverlust, Sicherheit): immer offen
                out.append(f'<aside class="callout cx-warnung"><div class="callout-h">{T("warnung")}'
                           + (": " + inline(label_arg) if label_arg else "") + '</div>' + _innen("warnung", label_arg, inner) + "</aside>")
                continue
            if kind == "ltspice":                         # LTspice-Hinweis (nachbauen und messen): standardmaessig geschlossen
                out.append('<details class="ltspice"><summary><span class="lt-k">LTspice</span>'
                           + inline(label_arg) + '</summary>'
                           '<div class="lt-body">' + _innen("ltspice", label_arg, inner) + '</div></details>')
                continue
            if kind == "hintergrund":                     # Hintergrundwissen: Titel sichtbar, Inhalt zugeklappt (Haupttext bleibt skriptgeordnet)
                out.append(f'<details class="hintergrund"><summary><span class="hg-k">{T("hintergrund")}</span>' + inline(label_arg) + '</summary>'
                           '<div class="hg-body">' + _innen("hintergrund", label_arg, inner) + '</div></details>')
                continue
            if kind == "frage":                           # Frage-Kasten (wie im Lernskript): Frage sichtbar, Antwort ausklappbar
                if label_arg:
                    frage, rest = label_arg, inner
                else:
                    k0 = next((j for j, l in enumerate(inner) if l.strip()), len(inner))
                    frage, rest = (inner[k0].strip() if k0 < len(inner) else ""), inner[k0 + 1:]
                out.append(f'<details class="frage"><summary><span class="fr-k">{T("frage")}</span>' + inline(frage) + '</summary>'
                           '<div class="fr-body">' + _innen("frage", frage, rest) + '</div></details>')
                continue
            if kind == "abbildung":                       # Editor-Abbildung: exportiertes SVG, nummerierte Bildunterschrift, Link in den Editor
                out.append(abbildung_html(label_arg, inner))
                continue
            if kind == "grafik":                          # Platzhalter einer Editor-Abbildung: Beschreibung als Text, Szene-Zeile klein darunter
                k0 = next((j for j, l in enumerate(inner) if l.strip()), len(inner))
                szene = ""
                if k0 < len(inner) and inner[k0].strip().startswith("Szene:"):
                    szene, inner = inner[k0].strip()[len("Szene:"):].strip(), inner[k0 + 1:]
                out.append('<aside class="callout cx-grafik"' + (f' data-szene="{html.escape(szene)}"' if szene else "")
                           + '><div class="callout-h">Abbildung in Vorbereitung</div>' + _innen("grafik", "", inner)
                           + (f'<div class="gr-szene">Editor-Szene: {html.escape(szene)}</div>' if szene else "") + "</aside>")
                continue
            key = CALLOUTS.get(kind, kind.title())
            label = inline(label_arg) if label_arg else html.escape(UI["de"].get(key) and T(key) or key)
            out.append(f'<aside class="callout cx-{kind}"><div class="callout-h">{label}</div>'
                       + _innen(kind, label_arg or (T(key) if key in UI["de"] else key), inner) + "</aside>")
            continue
        if re.match(r"(---|\*\*\*|___)\s*$", s):      # horizontal rule
            flush(); out.append("<hr/>"); i += 1; continue
        hm = re.match(r"(#{1,4})\s+(.*)$", s)         # heading
        if hm:
            flush(); lvl = len(hm.group(1)); txt = hm.group(2).strip()
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
            flush(); quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>" + _innen("zitat", "", quote) + "</blockquote>")
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i + 1].strip()):
            flush()                                   # GitHub-Tabelle: Kopfzeile + |---|---|-Trenner + Zeilen
            cells = lambda row: [c.strip().replace("\\|", "|")          # \| (GFM) ist ein | im Zelleninhalt, z. B. in `ls | wc`
                                 for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]
            header = cells(s); i += 2; body = []
            while i < n and lines[i].strip().startswith("|"):
                body.append(cells(lines[i].strip())); i += 1
            thead = "<tr>" + "".join(f"<th>{inline(_zf_begriffe(c, False))}</th>" for c in header) + "</tr>"
            tbody = "".join("<tr>" + "".join(f"<td>{inline(_zf_begriffe(c, False))}</td>" for c in r) + "</tr>" for r in body)
            out.append(f'<div class="table-wrap"><table class="md-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>')
            continue
        if re.match(r"[-*]\s+", s) or re.match(r"\d+\.\s+", s):   # list (ul/ol)
            flush(); ordered = bool(re.match(r"\d+\.\s+", s)); items = []
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
            out.append(f"<{tag}>" + "".join(f"<li>{inline(_zf_begriffe(it))}</li>" for it in items) + f"</{tag}>")
            continue
        if s.startswith("<"):                         # raw HTML / SVG / editor embed -> passthrough
            flush(); out.append(ln); i += 1; continue
        para.append(s); i += 1                         # ordinary paragraph line
    flush()
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
        art = {"title": title, "kurz": meta.get("kurz", "").replace("`", ""), "slug": a_slug, "order": order, "path": path,
               "summary": meta.get("summary", ""), "tags": meta.get("tags", ""), "body": body,
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

def sidebar_html(tree, active_path=None, art=None):
    # Seit 11.11.2026 (Wunsch des Users): immer nur die oberste Ebene (Studiengang/Bereich, z. B. Elektrotechnik) offen,
    # darunter sieht man nur die nächste Ebene (z. B. 1. Semester) zugeklappt; auch der Ast des geöffneten Artikels
    # bleibt zu (der Artikel ist weiter als aktiv markiert, falls man ihn aufklappt).
    def render(nodes, depth):
        rows = []
        for nd in nodes:
            is_open = depth == 0
            rows.append(f'<details class="lvl lvl{depth}"{" open" if is_open else ""}><summary>{_node_label(nd, depth)}</summary>')
            if nd["articles"]:
                rows.append("<ul>")
                for a in nd["articles"]:
                    cls = ' class="active"' if a["path"] == active_path else ""
                    rows.append(f'<li><a{cls} href="/wissen/{a["path"]}"{alt_attr(a)}>{html.escape(a["kurz"] or a["title"])}</a></li>')
                rows.append("</ul>")
            if nd["children"]:
                rows.append(render(nd["children"], depth + 1))
            rows.append("</details>")
        return "".join(rows)
    return ('<nav class="side" aria-label="Wissensbaum">'
            + f'<a class="side-home" href="{home()}">{T("alle_module")}</a>' + render(tree, 0) + "</nav>")

def page_shell(title, desc, body, depth, alternates=None):
    up = "../" * depth
    links = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in (alternates or {}).items())
    return f"""<!doctype html>
<html lang="{LANG_NOW[0]}"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(klartext(title))} — EtUndSo</title>
<link rel="icon" href="/favicon.ico" sizes="32x32"/><link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<meta name="description" content="{html.escape(klartext(desc))}"/>{links}
<script>try{{var t=localStorage.getItem("animate-theme");if(t==="dark"||(!t&&matchMedia("(prefers-color-scheme: dark)").matches))document.documentElement.setAttribute("data-theme","dark");}}catch(e){{}}</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css"/>
<link rel="stylesheet" href="/wissen/assets/wissen.css"/>
</head><body data-root="{home()}">
{body}
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>
<script src="/wissen/assets/wissen.js"></script>
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

def nav_arrow(a, prev):
    # Pfeil neben den Panel-Buttons zum vorherigen/nächsten Artikel (dieselbe Reihenfolge wie unten
    # „Vorheriger/Nächster Artikel"); am Anfang bzw. Ende grau und ohne Funktion.
    bid, word = ("navPrev", T("vorher")) if prev else ("navNext", T("weiter"))
    svg = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           + ('<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>' if prev else
              '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>') + '</svg>')
    if a:
        t = html.escape(f'{word}: {klartext(a["title"])}')     # Attribute ohne TeX (KaTeX setzt nur den Text der Seite)
        knopf = f'<a id="{bid}" class="navBtn" href="/wissen/{a["path"]}"{alt_attr(a)} title="{t}" aria-label="{t}">{svg}</a>'
        # Titel des Nachbarartikels neben dem Pfeil (User 2026-11-04: „sonst weiß man gar nicht was kommt“);
        # links vom Zurück-Pfeil, rechts vom Weiter-Pfeil; lange Titel enden mit …
        name = (f'<a class="navTitel {"vor" if prev else "nach"}" href="/wissen/{a["path"]}"{alt_attr(a)} title="{t}" '
                f'tabindex="-1" aria-hidden="true">{html.escape(a["title"])}</a>')
        return name + knopf if prev else knopf + name
    knopf = f'<span id="{bid}" class="navBtn disabled" aria-disabled="true" title="{word}">{svg}</span>'
    leer = f'<span class="navTitel {"vor" if prev else "nach"}"></span>'   # Platzhalter: die Knöpfe bleiben mittig
    return leer + knopf if prev else knopf + leer

def topbar(panels=False, prev_a=None, next_a=None, art=None):
    # Nur Artikelseiten, mittig: Knopf für den Themenbaum, davor und dahinter je ein Pfeil zum vorherigen/nächsten
    # Artikel mit dessen Titel. (Der Knopf für die rechte Gliederung ist weg: rechts steht nichts mehr, User 2026-11-04.)
    pbtns = ('<div class="panelCenter">' + nav_arrow(prev_a, True)
             + '<button id="toggleLeft" class="panelBtn" aria-label="Themenbaum ein-/ausblenden" title="Themenbaum ein-/ausblenden" aria-pressed="false">'
             '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="9" y1="4" x2="9" y2="20"/></svg></button>'
             + nav_arrow(next_a, False) + '</div>') if panels else ''
    return (f'<a class="skip" href="#inhalt">{T("zum_inhalt")}</a>'   # Sprunglink für die Tastatur: erst beim Fokus sichtbar
            '<div class="topbar"><a class="brand" href="/">Et<span>Und</span><span class="so">So</span></a>'
            + pbtns + lang_switch(art)
            + f'<button id="searchBtn" class="searchBtn" aria-label="{T("suchen")}">'   # ohne Lupen-Symbol (User 2026-10-21)
            f'<span class="lbl">{T("suchen")}</span><kbd>/</kbd></button>'
            # Hell/Dunkel-Umschalter — immer oben rechts, auf allen Wissensseiten an gleicher Stelle.
            '<button id="themeBtn" class="iconBtn" aria-label="Hell/Dunkel umschalten" title="Hell/Dunkel umschalten">'
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M21 12.8A8 8 0 1 1 11.2 3 6 6 0 0 0 21 12.8z"/></svg></button>'
            + '<a class="editorlink" href="/editor.html">Editor</a></div>'
            '<div id="searchOverlay" class="searchOverlay" hidden><div class="searchBox">'
            f'<input id="searchInput" type="search" placeholder="{T("suche_ph")}" autocomplete="off"/>'
            '<div id="searchResults" class="searchResults"></div>'
            f'<div class="searchHint">{T("suche_hint")}</div></div></div>')

_TOC = {}                                              # Artikeltext -> Abschnittsliste (für die Nachbar-Karten)


def render_article(art, tree, prev_a, next_a):
    ABB_N[0] = 0                                       # Abbildungen je Artikel ab 1 nummerieren
    zf_start()                                         # Sammler der Zusammenfassung: nur für den Artikel selbst
    body_html, toc = md_to_html(art["body"])
    zdaten = dict(ZF)
    ZF["an"] = False
    _TOC[art["body"]] = toc
    quiz_html = ""                                     # Quiz ganz unten, unter den Nachbar-Spalten (User 2026-10-21)
    qa = body_html.find('<aside class="callout cx-quiz">')
    if qa >= 0:
        qe = body_html.index("</aside>", qa) + len("</aside>")
        quiz_html, body_html = body_html[qa:qe], body_html[:qa] + body_html[qe:]
    n_abb, n_aufg = body_html.count('<figure class="abb"'), body_html.count('<div class="aufg">')
    if not any(lvl == 2 for _, _, lvl in toc):         # ohne ##-Abschnitte (kurz oder nur ###): eine einzige Karte
        body_html = f'<section class="sect">{body_html}</section>'
    # am Artikelende, vor den Nachbar-Artikeln (User 11.11.2026); nicht in „Das Wichtigste (bis hier)“: Der Artikel ist
    # mit seinem Kasten :::kern schon die Zusammenfassung des Kapitels
    zf_html = "" if re.search(r"(?m)^:::kern\b", art["body"]) else zusammenfassung_html(zdaten)
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
    meta = ('<div class="art-meta"><span class="am-zahlen">' + "".join(f"<span>{html.escape(z)}</span>" for z in zahlen) + "</span>"
            + (f'<a class="am-zf" href="#zusammenfassung">{T("zf_sprung")}</a>' if zf_html else "")
            + pill + lang_switch(art, "art") + "</div>")
    toc_html = ""
    arttoc = ""
    if toc:
        eintraege = "".join(f'<li><a href="#{hid}">{inline(_ohne_links(txt))}</a></li>' for hid, txt, _ in toc)
        if zf_html:
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
    main = (f'<main class="article" id="inhalt" tabindex="-1"><article>{crumb}<h1>{html.escape(art["title"])}</h1>'
            + meta + switch + arttoc
            + body_html + zf_html + verwendet_html(art) + nav + quiz_html + legal_footer() + "</article>" + toc_html + "</main>")
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

def render_index(tree):
    cards = [f'<main class="article" id="inhalt" tabindex="-1"><article><h1>{T("wissen")}</h1>{lang_switch(None, "art")}<p class="lede">{T("lede")}</p>']
    if not tree:
        cards.append(f'<p class="empty">{T("leer")}</p>')
    # Übersicht: oberste Ebene(n) als Abschnitt, darunter der Baum rekursiv; Themen als verlinkte Karten.
    def block(nodes, depth):
        rows = []
        for nd in nodes:
            leaf_cards = ""
            if nd["articles"]:
                links = "".join(f'<li><a href="/wissen/{a["path"]}">{html.escape(a["kurz"] or a["title"])}</a></li>' for a in nd["articles"])
                leaf_cards = f'<div class="theme-card"><ul>{links}</ul></div>'
            hw = f'<p class="idx-hinweis">{inline(nd["hinweis"])}</p>' if nd.get("hinweis") else ""   # content/**/_*.md
            if depth == 0:
                rows.append(f'<section class="field-block"><h2 id="{nd["slug"]}">{html.escape(nd["name"])}</h2>{hw}')
                rows.append(block(nd["children"], depth + 1) + (f'<div class="field-grid">{leaf_cards}</div>' if leaf_cards else ""))
                rows.append("</section>")
            else:
                hd = (f'<h3 class="idx-lvl{depth}">{html.escape(nd["name"])}</h3>' if depth >= 2
                      else f'<h4 class="lvl-h idx-lvl{depth}">{_node_label(nd, depth)}</h4>')
                inner = block(nd["children"], depth + 1)
                rows.append(f'<div class="idx-node">{hd}{hw}{leaf_cards}{inner}</div>' if (inner or leaf_cards) else "")
        return "".join(rows)
    cards.append(block(tree, 0))
    cards.append(legal_footer() + "</article></main>")
    body = topbar() + '<div class="layout">' + sidebar_html(tree, None) + "".join(cards) + "</div>"
    return page_shell("Wissen", "Verständliche Erklärungen zu Elektrotechnik, Mathematik und mehr.", body, 1)

# --------------------------------------------------------------------- main ----
TREES = {}                                             # {Sprache: Baum}, von main gesetzt
ART_LANG = {}                                          # (Ordner, Stamm) -> {Sprache: Artikel}: der Sprachumschalter

GESCHRIEBEN = set()                                    # alle Seiten dieses Builds; main löscht danach die übrigen (alte Adressen)

def schreibe(path, text):
    path.write_text(text, encoding="utf-8")
    GESCHRIEBEN.add(path.resolve())

def build_lang(lang, tree):
    LANG_NOW[0] = lang
    RUECK.clear()
    RUECK.update(rueckverweise(tree))
    flat = flatten(tree)
    for idx, art in enumerate(flat):
        prev_a = flat[idx - 1] if idx > 0 else None
        nxt = flat[idx + 1] if idx + 1 < len(flat) else None
        dest = OUT / Path(art["path"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        schreibe(dest, render_article(art, tree, prev_a, nxt))
        p2 = (prev_a.get("alt") or prev_a) if prev_a else None   # Nachbarn der ausführlichen Fassung möglichst ebenfalls ausführlich
        n2 = (nxt.get("alt") or nxt) if nxt else None
        if art.get("alt"):
            schreibe(OUT / Path(art["alt"]["path"]), render_article(art["alt"], tree, p2, n2))
        h = art.get("human")                           # von Hand geschriebene Fassung(en) desselben Themas
        if h:
            schreibe(OUT / Path(h["path"]), render_article(h, tree, prev_a, nxt))
            if h.get("alt"):
                schreibe(OUT / Path(h["alt"]["path"]), render_article(h["alt"], tree, p2, n2))

    start = OUT if lang == "de" else OUT / lang
    start.mkdir(parents=True, exist_ok=True)
    schreibe(start / "index.html", render_index(tree))

    # navigation tree (ohne bodies, beliebig tief) + search index
    def jnode(nd):
        return {"name": nd["name"], "slug": nd["slug"],
                "articles": [{"title": a["title"], "path": a["path"], "summary": a["summary"],
                              **({"alt": a["alt"]["path"]} if a.get("alt") else {})} for a in nd["articles"]],
                "children": [jnode(c) for c in nd["children"]]}
    tree_json = [jnode(n) for n in tree]
    suffix = "" if lang == "de" else "." + lang
    (OUT / "data" / f"tree{suffix}.json").write_text(json.dumps(tree_json, ensure_ascii=False), encoding="utf-8")

    search = []
    alts = [a["alt"] for a in flat if a.get("alt")]
    humans = [a["human"] for a in flat if a.get("human")]
    humans += [h["alt"] for h in humans if h.get("alt")]
    for a in flat + alts:
        plain = to_plain(a["body"])
        crumb = " › ".join(nm for nm, sl in a["crumbs"])
        title = a["title"] + (" (ausführlich)" if a.get("fassung") == "ausfuehrlich" and a.get("alt") else "") \
            + (" (von Hand)" if a["autor"] == "mensch" else "")
        search.append({"title": title, "crumb": crumb, "path": a["path"],
                       "summary": a["summary"], "tags": a["tags"],
                       # pre-folded fields for fast infix matching; 'text' kept (original) for snippets
                       "ft_title": fold(title), "ft_tags": fold(a["tags"]),
                       "ft_text": fold(a["summary"] + " " + plain), "text": plain})
    (OUT / "data" / f"search{suffix}.json").write_text(json.dumps(search, ensure_ascii=False), encoding="utf-8")
    return len(flat), len(alts), len(humans)

def main():
    TREES.update(collect())
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "data").mkdir(exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)
    for lang, tree in TREES.items():
        for a in flatten(tree):
            ART_LANG.setdefault(a["key"], {})[lang] = a
    counts = {lang: build_lang(lang, tree) for lang, tree in TREES.items()}
    alt = alte_seiten_entfernen()
    LANG_NOW[0] = "de"
    (OUT / "assets" / "wissen.css").write_text(WISSEN_CSS, encoding="utf-8")
    (OUT / "assets" / "wissen.js").write_text(WISSEN_JS, encoding="utf-8")
    day = write_version()
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
.topbar .navBtn{color:var(--bar-hl);border-color:var(--bar-hl);}             /* Pfeile zum vorherigen/nächsten Artikel */
.topbar .navBtn:hover{text-decoration:none;background:color-mix(in srgb,var(--bar-hl) 18%,var(--bar-soft));}
.topbar .navBtn.disabled{color:var(--bar-ink);border-color:var(--bar-rand);opacity:.45;cursor:default;pointer-events:none;}   /* erster/letzter Artikel: grau, ohne Funktion */
.topbar .panelCenter{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:8px;}  /* Einklapp-Buttons mittig in der Leiste */
/* Titel des vorherigen/nächsten Artikels neben den Pfeilen; beide Seiten gleich breit, damit die Knöpfe mittig bleiben */
.topbar .navTitel{width:min(280px,calc(50vw - 350px));overflow:hidden;white-space:nowrap;text-overflow:ellipsis;font-size:13.5px;font-weight:500;
  color:#ffffff;height:36px;line-height:36px;}   /* weiß; Zeilenhöhe = Höhe der Pfeil-Kreise -> Text genau auf deren Mitte */
.topbar .navTitel.vor{text-align:right;} .topbar .navTitel.nach{text-align:left;}
.topbar a.navTitel:hover{color:var(--bar-hl);text-decoration:none;}
@media(max-width:1000px){ .topbar .navTitel{display:none;} }
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
"""

WISSEN_JS = r"""
var NICHTS={de:"Nichts gefunden für „{q}\".",en:"Nothing found for „{q}\".",es:"Nada encontrado para „{q}\".",zh:"未找到 „{q}\".",
            fr:"Aucun résultat pour «\u00a0{q}\u00a0».",tr:"“{q}” için sonuç bulunamadı."};
// Suche: vorab gebauter Index (search.json), Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben.
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var DOCS=null, sel=-1, rows=[];
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").replace(/ı/g,"i").replace(/œ/g,"oe").replace(/æ/g,"ae")
    .normalize("NFKD").replace(/[̀-ͯ]/g,""); }                // wie fold() in build_wissen.py
  function load(){ if(DOCS) return Promise.resolve(DOCS);
    var L=document.documentElement.lang; L=(L&&L!=="de")?"."+L:"";
    return fetch("/wissen/data/search"+L+".json").then(function(r){return r.json();}).then(function(d){DOCS=d;return d;}).catch(function(){DOCS=[];return [];}); }
  function esc(s){ return s.replace(/[&<>]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c];}); }
  function safeSnippet(doc,q){
    var t=doc.text||doc.summary||"", ft=fold(t), i=ft.indexOf(q);
    if(i<0) return esc(t.slice(0,130))+(t.length>130?"…":"");
    var a=Math.max(0,i-45);
    return (a>0?"…":"")+esc(t.slice(a,i))+"<mark>"+esc(t.slice(i,i+q.length))+"</mark>"+esc(t.slice(i+q.length,i+q.length+70))+"…";
  }
  function search(raw){
    var q=fold(raw.trim()); results.innerHTML=""; rows=[]; sel=-1;
    if(q.length<2 || !DOCS) return;
    var hits=[];
    for(var k=0;k<DOCS.length;k++){ var d=DOCS[k], sc=-1;
      if(d.ft_title.indexOf(q)>=0) sc=0;                 // Titel-Treffer: höchster Rang
      else if((d.ft_tags||"").indexOf(q)>=0) sc=1;       // Tag
      else { var p=d.ft_text.indexOf(q); if(p>=0) sc=2+Math.min(p/500,1); }  // Text, früher = besser
      if(sc>=0) hits.push([sc,d]);
    }
    hits.sort(function(a,b){return a[0]-b[0];});
    hits.slice(0,25).forEach(function(h){ var d=h[1];
      var a=document.createElement("a"); a.href="/wissen/"+d.path;
      a.innerHTML='<div class="r-crumb">'+esc(d.crumb||"")+'</div>'+
                  '<div class="r-title">'+esc(d.title)+'</div>'+
                  '<div class="r-snip">'+safeSnippet(d,q)+'</div>';
      results.appendChild(a); rows.push(a);
    });
    if(!rows.length) results.innerHTML='<div class="searchHint">'+esc(NICHTS[document.documentElement.lang]||NICHTS.de).split("{q}").join(esc(raw.trim()))+'</div>';
  }
  function open(){ if(!overlay) return; overlay.hidden=false; load().then(function(){ input.value=""; results.innerHTML=""; input.focus(); }); }
  function close(){ if(overlay) overlay.hidden=true; }
  if(btn) btn.addEventListener("click",open);
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
    var auf=false;
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
    if(window.renderMathInElement) renderMathInElement(document.body,{delimiters:[
      {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}],strict:false});
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
"""

if __name__ == "__main__":
    main()
