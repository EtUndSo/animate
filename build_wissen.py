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

Sprachen (de, en, es, zh): NN-slug.en.md neben NN-slug.md ist die Übersetzung, mit übersetztem `pfad:`. Sie landet
unter web/wissen/en/<dieselbe Adresse wie der deutsche Artikel>, jede Sprache hat ihren eigenen Baum, ihre Übersicht
und ihren Suchindex. Der Umschalter DE | EN | ES | 中文 führt zur selben Seite in der anderen Sprache.
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

LANGS = ("de", "en", "es", "zh")
LANG_NAME = {"de": "DE", "en": "EN", "es": "ES", "zh": "中文"}
LANG_FILE = re.compile(r"\.(en|es|zh)$")   # NN-slug.en.md
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
           "warnung": "Achtung", "konsole": "Konsole",
           "fremd": "Rechtliche Seiten sind auf Deutsch."},
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
           "warnung": "Caution", "konsole": "Terminal"},
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
           "warnung": "Atención", "konsole": "Terminal"},
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
           "warnung": "注意", "konsole": "终端"},
}

def T(key):
    """Wort der Oberfläche in der Sprache der gerade gebauten Seite."""
    return UI[LANG_NOW[0]].get(key) or UI["de"][key]

def home():
    return "/wissen/" if LANG_NOW[0] == "de" else f"/wissen/{LANG_NOW[0]}/"

# ---------------------------------------------------------------- helpers ----
def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "x"

def fold(s):
    """Normalise for search: lowercase, strip diacritics, ß->ss — so 'Übertragung' matches 'ubertragung'."""
    s = s.lower().replace("ß", "ss")
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
    text = re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$|`[^`]+?`", _protect, text, flags=re.S)
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # Namen (Größen-/Begriffsnamen) -> blau: __Name__
    text = re.sub(r"__([^_]+)__", r'<strong class="nm">\1</strong>', text)
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

ABB_N = [0]                                               # laufende Abbildungsnummer im Artikel (render_article setzt 0)
_ABB_GEMELDET = set()                                     # jede fehlende Szene/SVG nur einmal melden

def svg_size(path):
    """(Breite, Höhe) aus dem <svg>-Kopf einer exportierten Abbildung, None wenn sie fehlt."""
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
    return (f'<figure class="abb" id="abb-{k}"><img src="{ABB_URL}/{lang}/{name}.svg" width="{size[0]}" height="{size[1]}" '
            f'alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async"/>'
            + (f'<div class="abb-knopf">{edit}</div>' if edit else "")
            + f'<figcaption><span class="abb-n">{T("abbildung")} {k}</span>{(" " + cap) if cap else ""}</figcaption></figure>')

# Code-Blöcke (Hefte der Zusatzreihen): ```<sprache> <titel>. Farben per Pygments als CSS-Klassen (.hl …), damit Tag- und
# Nachtmodus dieselben Seiten nutzen; ohne Pygments bleibt der Code einfarbig. console = Sitzung im Terminal ($/# am
# Zeilenanfang = Eingabe), mit „>>> " wird daraus die Python-Konsole.
CODE_NAME = {"python": "Python", "bash": "Bash", "c": "C", "cpp": "C++", "nasm": "x86-64", "gas": "x86-64 (AT&T)"}

def code_html(info, code):
    lang, _, titel = info.partition(" ")
    lang = lang.lower()
    lexer_name = {"console": "pycon" if re.search(r"(?m)^>>> ", code) else "console", "text": "", "": ""}.get(lang, lang)
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
    section_open = False                                  # jeder ##-Abschnitt wird als Karte <section class="sect"> eingefasst
    formel_n = 0                                          # fortlaufende Nummer der :::formel-Boxen (zum Referenzieren, wie im Skript)
    para = []
    h_ids = set()
    bsp_n = [0]
    def beispiel(title, inner):                           # Beispiel: eigene Karte an der Stelle, an der es steht
        bsp_n[0] += 1
        out.append(f'<section class="bsp-card"><div class="bsp-card-n">{T("beispiel")} {bsp_n[0]}</div>'
                   + (f'<div class="bsp-card-t">{inline(title)}</div>' if title else "")
                   + md_to_html("\n".join(inner))[0] + "</section>")
    def flush():
        if para:
            txt = " ".join(para).strip()
            if not txt.startswith("**Worum es geht"):   # Einstiegs-Absatz entfällt – Artikel startet mit dem Inhaltsverzeichnis
                # Gleichungsnummer \\tag{2.3} (mehrere: 2.3|2.4): eigene Spalte neben der Formel. KaTeX legte sie über
                # die Formel, sobald der Platz knapp wird; so bleibt sie frei und die Formel verkleinert sich (fitMath).
                mt = re.fullmatch(r"(\$\$.*?)\s*\\tag\{([^{}]*)\}\$\$", txt, flags=re.S)
                nummer = ""
                if mt:
                    txt = mt.group(1) + "$$"
                    nummer = "".join(f"<span>({n})</span>" for n in mt.group(2).split("|"))
                parts = split_display(txt)
                if parts:                                # mehrteilige Formelzeile: Teile dürfen umbrechen
                    inhalt = ('<div class="mrow">' + "".join('<div class="mcell">' + inline("$$" + p + "$$") + "</div>"
                                                             for p in parts) + "</div>")
                else:
                    inhalt = inline(txt) if nummer else "<p>" + inline(txt) + "</p>"
                out.append(f'<div class="gl-zeile"><div class="gl-f">{inhalt}</div><div class="gl-nr">{nummer}</div></div>' if nummer else inhalt)
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
        mb = re.match(r"::::beispiel(?:\s+(.+?))?\s*$", s)   # ::::beispiel … :::: (vier Doppelpunkte, darf :::-Blöcke enthalten)
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
                a_html = md_to_html(it["a"].strip())[0]
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
                           + md_to_html("\n".join(inner))[0] + '</div>')
                continue
            if kind in ("herleitung", "beweis"):          # Herleitung oder Beweis als ausklappbare Box an der Formel
                out.append(f'<details class="herleitung"><summary>{T(kind)}' + (": " + inline(label_arg) if label_arg else "") + '</summary>'
                           '<div class="hl-body">' + md_to_html("\n".join(inner))[0] + '</div></details>')
                continue
            if kind == "zweck":                           # Einstieg einer Stufe: wozu sie da ist
                out.append(f'<div class="zweck"><span class="zw-k">{T("zweck")}</span> ' + md_to_html("\n".join(inner))[0] + '</div>')
                continue
            if kind == "aufgabe":                         # Aufgabe mit Nummer und Sternen, Lösung als Ausklappblock darin
                out.append('<div class="aufg"><div class="aufg-h">' + inline(label_arg) + '</div>'
                           '<div class="aufg-b">' + md_to_html("\n".join(inner))[0] + '</div></div>')
                continue
            if kind == "loesung":
                out.append(f'<details class="loesung"><summary>{T("loesung")}</summary>'
                           '<div class="lo-body">' + md_to_html("\n".join(inner))[0] + '</div></details>')
                continue
            if kind == "zusatz":                          # Vertiefung: darf übersprungen werden
                out.append(f'<aside class="callout cx-zusatz"><div class="callout-h">{T("zusatz")}'
                           + (": " + inline(label_arg) if label_arg else "") + '</div>' + md_to_html("\n".join(inner))[0] + "</aside>")
                continue
            if kind == "warnung":                         # Achtung (Recht, Datenverlust, Sicherheit): immer offen
                out.append(f'<aside class="callout cx-warnung"><div class="callout-h">{T("warnung")}'
                           + (": " + inline(label_arg) if label_arg else "") + '</div>' + md_to_html("\n".join(inner))[0] + "</aside>")
                continue
            if kind == "ltspice":                         # LTspice-Hinweis (nachbauen und messen): standardmaessig geschlossen
                out.append('<details class="ltspice"><summary><span class="lt-k">LTspice</span>'
                           + inline(label_arg) + '</summary>'
                           '<div class="lt-body">' + md_to_html("\n".join(inner))[0] + '</div></details>')
                continue
            if kind == "hintergrund":                     # Hintergrundwissen: Titel sichtbar, Inhalt zugeklappt (Haupttext bleibt skriptgeordnet)
                out.append(f'<details class="hintergrund"><summary><span class="hg-k">{T("hintergrund")}</span>' + inline(label_arg) + '</summary>'
                           '<div class="hg-body">' + md_to_html("\n".join(inner))[0] + '</div></details>')
                continue
            if kind == "frage":                           # Frage-Kasten (wie im Lernskript): Frage sichtbar, Antwort ausklappbar
                if label_arg:
                    frage, rest = label_arg, inner
                else:
                    k0 = next((j for j, l in enumerate(inner) if l.strip()), len(inner))
                    frage, rest = (inner[k0].strip() if k0 < len(inner) else ""), inner[k0 + 1:]
                out.append(f'<details class="frage"><summary><span class="fr-k">{T("frage")}</span>' + inline(frage) + '</summary>'
                           '<div class="fr-body">' + md_to_html("\n".join(rest))[0] + '</div></details>')
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
                           + '><div class="callout-h">Abbildung in Vorbereitung</div>' + md_to_html("\n".join(inner))[0]
                           + (f'<div class="gr-szene">Editor-Szene: {html.escape(szene)}</div>' if szene else "") + "</aside>")
                continue
            key = CALLOUTS.get(kind, kind.title())
            label = inline(label_arg) if label_arg else html.escape(UI["de"].get(key) and T(key) or key)
            out.append(f'<aside class="callout cx-{kind}"><div class="callout-h">{label}</div>'
                       + md_to_html("\n".join(inner))[0] + "</aside>")
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
                toc.append((hid, txt))
                if section_open:
                    out.append("</section>")
                out.append('<section class="sect">')
                section_open = True
            out.append(f'<h{lvl} id="{hid}">{inline(txt)}</h{lvl}>')
            i += 1; continue
        if s.startswith(">"):                         # blockquote
            flush(); quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>" + md_to_html("\n".join(quote))[0] + "</blockquote>")
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i + 1].strip()):
            flush()                                   # GitHub-Tabelle: Kopfzeile + |---|---|-Trenner + Zeilen
            cells = lambda row: [c.strip() for c in row.strip().strip("|").split("|")]
            header = cells(s); i += 2; body = []
            while i < n and lines[i].strip().startswith("|"):
                body.append(cells(lines[i].strip())); i += 1
            thead = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr>"
            tbody = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
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
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it)}</li>" for it in items) + f"</{tag}>")
            continue
        if s.startswith("<"):                         # raw HTML / SVG / editor embed -> passthrough
            flush(); out.append(ln); i += 1; continue
        para.append(s); i += 1                         # ordinary paragraph line
    flush()
    if section_open:                                   # letzte Abschnitts-Karte schließen
        out.append("</section>")
    return "\n".join(out), toc

# ---------------------------------------------------------- plain text (search) ----
def to_plain(md):
    txt = re.sub(r"```.*?```", " ", md, flags=re.S)
    txt = re.sub(r"\$\$?.+?\$\$?", " ", txt, flags=re.S)        # drop math
    txt = re.sub(r"</?[a-z][^>]*>", " ", txt)                  # Listen und Anker aus den Heften
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
    de_pfad = {}
    def deutsch_zuerst(p):
        return (bool(LANG_FILE.search(p.stem)), p)
    for md_file in sorted(SRC.rglob("*.md"), key=deutsch_zuerst):
        meta, body = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        ml = LANG_FILE.search(md_file.stem)
        lang = ml.group(1) if ml else "de"
        stem = md_file.stem[:ml.start()] if ml else md_file.stem
        pfad = (meta.get("pfad") or "").strip()
        if not pfad:
            print("  übersprungen (kein pfad:):", md_file.relative_to(SRC)); continue
        parts = [p.strip() for p in pfad.split("/") if p.strip()]
        title = meta.get("title") or md_file.stem
        ov = (meta.get("order") or "").strip()
        order = int(ov) if ov.isdigit() else (int(re.match(r"(\d+)", stem).group(1)) if re.match(r"\d+", stem) else 999999)
        container, chain = roots[lang], []
        for part in parts:
            nd = container.setdefault(slugify(part) if lang == "de" else part, _new_node(part))
            chain.append(nd); container = nd["children"]
        a_slug = re.sub(r"^\d+-", "", stem) or slugify(title)
        key = (str(md_file.parent), stem)
        if lang == "de":
            path = "/".join(nd["slug"] for nd in chain) + "/" + a_slug + ".html"
            de_pfad[key] = path
        else:
            path = lang + "/" + de_pfad.get(key, "/".join(nd["slug"] for nd in chain) + "/" + a_slug + ".html")
        autor = (meta.get("autor") or "").strip().lower()
        if re.search(r"-mensch(-ausfuehrlich)?$", a_slug):   # Dateiname-Suffix genügt
            autor = autor or "mensch"
        art = {"title": title, "kurz": meta.get("kurz", ""), "slug": a_slug, "order": order, "path": path,
               "summary": meta.get("summary", ""), "tags": meta.get("tags", ""), "body": body,
               "crumbs": [(nd["name"], nd["slug"]) for nd in chain], "lang": lang, "key": key,
               "fassung": (meta.get("fassung") or "").strip().lower(),
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
    # Standard: bis zur Modul-Ebene offen, Module selbst ZUgeklappt (Oberthemen erst auf Klick);
    # der Ast des aktuell geöffneten Artikels wird automatisch aufgeklappt.
    def render(nodes, depth):
        rows = []
        for nd in nodes:
            is_open = depth <= 1 or (active_path and _has_active(nd, active_path))
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
<title>{html.escape(title)} — EtUndSo</title>
<meta name="description" content="{html.escape(desc)}"/>{links}
<script>try{{if(localStorage.getItem("animate-theme")==="dark")document.documentElement.setAttribute("data-theme","dark");}}catch(e){{}}</script>
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

def lang_switch(art=None, where="top"):
    # where: "top" = Kopfleiste; auf dem Handy passt er dort nicht mehr und steht unter dem Titel ("art")
    ziele = sprachen(art)
    btn = ""
    for l in LANGS:
        if l == LANG_NOW[0]:
            btn += f'<a class="l-btn on" aria-current="true" href="{ziele.get(l, home())}" hreflang="{l}">{LANG_NAME[l]}</a>'
        elif l in ziele:
            btn += f'<a class="l-btn" href="{ziele[l]}" hreflang="{l}">{LANG_NAME[l]}</a>'
        else:
            btn += f'<span class="l-btn off" aria-disabled="true">{LANG_NAME[l]}</span>'
    return f'<nav class="langs langs-{where}" aria-label="Sprache">{btn}</nav>'

def lesezeit(body):
    """Lesezeit des Hauptpfads in Minuten (170 Wörter/min; ohne Herleitungen, Beispiele, Quiz, Formeln, Abbildungen)."""
    t = re.sub(r"^::::\s*beispiel.*?^::::\s*$", " ", body, flags=re.S | re.M)
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
        t = html.escape(f'{word}: {a["title"]}')
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
    return ('<div class="topbar"><a class="brand" href="/">Et<span>Und</span><span class="so">So</span></a>'
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

def render_article(art, tree, prev_a, next_a):
    ABB_N[0] = 0                                       # Abbildungen je Artikel ab 1 nummerieren
    body_html, toc = md_to_html(art["body"])
    quiz_html = ""                                     # Quiz ganz unten, unter den Nachbar-Spalten (User 2026-10-21)
    qa = body_html.find('<aside class="callout cx-quiz">')
    if qa >= 0:
        qe = body_html.index("</aside>", qa) + len("</aside>")
        quiz_html, body_html = body_html[qa:qe], body_html[:qa] + body_html[qe:]
    if not toc:                                        # kurzer Artikel ohne Abschnitte: eine einzige Karte
        body_html = f'<section class="sect">{body_html}</section>'
    pill = (f'<span class="apill apill-mensch">{T("hand_pill")}</span>' if art["autor"] == "mensch"
            else f'<span class="apill">{T("ki_pill")}</span>')
    crumb = f'<nav class="crumbs"><a href="{home()}">{T("wissen")}</a>' + \
            "".join(f' › <span>{html.escape(nm)}</span>' for nm, sl in art["crumbs"]) + " " + pill + "</nav>"
    toc_html = ""
    arttoc = ""
    if toc:
        toc_html = f'<aside class="toc"><div class="toc-h">{T("auf_seite")}</div><ul>' + \
            "".join(f'<li><a href="#{hid}">{html.escape(txt)}</a></li>' for hid, txt in toc) + "</ul></aside>"
        arttoc = f'<nav class="arttoc" aria-label="{T("im_artikel")}"><div class="arttoc-h">{T("im_artikel")}</div><ul>' + \
            "".join(f'<li><a href="#{hid}">{html.escape(txt)}</a></li>' for hid, txt in toc) + "</ul></nav>"
    def _topics(a):                                    # Themen-Stichpunkte (##-Überschriften) eines Nachbarartikels
        return "".join(f"<li>{html.escape(t)}</li>" for _, t in md_to_html(a["body"])[1])
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
    main = (f'<main class="article"><article>{crumb}<h1>{html.escape(art["title"])}</h1>'
            + lang_switch(art, "art") + switch + arttoc
            + body_html + nav + quiz_html + legal_footer() + "</article>" + toc_html + "</main>")
    nav_path = tree_art(art)["path"]
    body = (topbar(panels=True, prev_a=prev_a, next_a=next_a, art=art)
            + '<div class="layout">'
            + sidebar_html(tree, nav_path, art) + main + "</div>")
    depth = 1 + art["path"].count("/")               # web/wissen/<…chain…>/<a>.html
    return page_shell(art["title"], art["summary"] or art["title"], body, depth, sprachen(art))

def legal_footer():
    return (f'<footer class="wfoot">EtUndSo.de · <a href="/impressum.html">{T("impressum")}</a> · '
            f'<a href="/datenschutz.html">{T("datenschutz")}</a></footer>')

def render_index(tree):
    cards = [f'<main class="article"><article><h1>{T("wissen")}</h1>{lang_switch(None, "art")}<p class="lede">{T("lede")}</p>']
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
            if depth == 0:
                rows.append(f'<section class="field-block"><h2 id="{nd["slug"]}">{html.escape(nd["name"])}</h2>')
                rows.append(block(nd["children"], depth + 1) + (f'<div class="field-grid">{leaf_cards}</div>' if leaf_cards else ""))
                rows.append("</section>")
            else:
                hd = (f'<h3 class="idx-lvl{depth}">{html.escape(nd["name"])}</h3>' if depth >= 2
                      else f'<h4 class="lvl-h idx-lvl{depth}">{_node_label(nd, depth)}</h4>')
                inner = block(nd["children"], depth + 1)
                rows.append(f'<div class="idx-node">{hd}{leaf_cards}{inner}</div>' if (inner or leaf_cards) else "")
        return "".join(rows)
    cards.append(block(tree, 0))
    cards.append(legal_footer() + "</article></main>")
    body = topbar() + '<div class="layout">' + sidebar_html(tree, None) + "".join(cards) + "</div>"
    return page_shell("Wissen", "Verständliche Erklärungen zu Elektrotechnik, Mathematik und mehr.", body, 1)

# --------------------------------------------------------------------- main ----
TREES = {}                                             # {Sprache: Baum}, von main gesetzt
ART_LANG = {}                                          # (Ordner, Stamm) -> {Sprache: Artikel}: der Sprachumschalter

def build_lang(lang, tree):
    LANG_NOW[0] = lang
    flat = flatten(tree)
    for idx, art in enumerate(flat):
        prev_a = flat[idx - 1] if idx > 0 else None
        nxt = flat[idx + 1] if idx + 1 < len(flat) else None
        dest = OUT / Path(art["path"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_article(art, tree, prev_a, nxt), encoding="utf-8")
        p2 = (prev_a.get("alt") or prev_a) if prev_a else None   # Nachbarn der ausführlichen Fassung möglichst ebenfalls ausführlich
        n2 = (nxt.get("alt") or nxt) if nxt else None
        if art.get("alt"):
            (OUT / Path(art["alt"]["path"])).write_text(render_article(art["alt"], tree, p2, n2), encoding="utf-8")
        h = art.get("human")                           # von Hand geschriebene Fassung(en) desselben Themas
        if h:
            (OUT / Path(h["path"])).write_text(render_article(h, tree, prev_a, nxt), encoding="utf-8")
            if h.get("alt"):
                (OUT / Path(h["alt"]["path"])).write_text(render_article(h["alt"], tree, p2, n2), encoding="utf-8")

    start = OUT if lang == "de" else OUT / lang
    start.mkdir(parents=True, exist_ok=True)
    (start / "index.html").write_text(render_index(tree), encoding="utf-8")

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
    LANG_NOW[0] = "de"
    (OUT / "assets" / "wissen.css").write_text(WISSEN_CSS, encoding="utf-8")
    (OUT / "assets" / "wissen.js").write_text(WISSEN_JS, encoding="utf-8")
    day = write_version()
    n_mod, n_alt, n_hand = counts["de"]
    andere = ", ".join(f"{l}: {c[0]}" for l, c in counts.items() if l != "de")
    print(f"✓ {n_mod} Artikel (+{n_alt} ausführliche Fassungen, +{n_hand} von Hand)"
          + (f", übersetzt {andere}" if andere else "") + f" -> {OUT} · Stand {day}")

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
.brand{font-family:var(--fdisp);font-weight:800;font-size:19px;letter-spacing:-.02em;color:var(--bar-ink);}
.brand span{color:var(--bar-ink);} .brand span.so{color:var(--bar-hl);}
.topbar .searchBtn{margin-left:auto;display:flex;align-items:center;gap:8px;background:var(--bar-soft);border:1px solid var(--bar-rand);color:var(--bar-ink);
  border-radius:10px;padding:8px 13px;font:inherit;font-size:14px;cursor:pointer;}
.topbar .searchBtn:hover{border-color:var(--bar-hl);}
.topbar kbd{background:transparent;border-color:var(--bar-rand);color:var(--bar-ink);}
.topbar .langs{background:var(--bar-soft);border-color:var(--bar-rand);}
.topbar .langs .l-btn{color:var(--bar-ink);} .topbar .langs .l-btn.on{background:var(--bar-hl);color:#2a1205;}
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
  color:var(--bar-ink);opacity:.82;line-height:1.3;}
.topbar .navTitel.vor{text-align:right;} .topbar .navTitel.nach{text-align:left;}
.topbar a.navTitel:hover{opacity:1;color:var(--bar-hl);text-decoration:none;}
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
.langs{display:inline-flex;margin-left:10px;border:1px solid var(--border);border-radius:9px;overflow:hidden;background:var(--soft);}
.langs .l-btn{padding:6px 8px;font-size:12.5px;font-weight:600;color:var(--muted);text-decoration:none;}
.langs .l-btn.on{background:var(--accent);color:var(--on-accent);}
.langs .l-btn.off{opacity:.4;cursor:default;}
html[lang="zh"] body{font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif;}
.langs-art{display:none;margin:0 0 10px 8px;}
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
/* ---------- Beispiel-Karte im Artikel (Farbe Orange = Praxis) ---------- */
.bsp-card{border:1px solid var(--border);border-top:4px solid var(--accent3);border-radius:14px;background:var(--panel);padding:4px 20px 14px;margin:0 0 18px;transition:box-shadow .35s;}
.bsp-card-n{font-family:var(--fdisp);font-weight:700;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent3);white-space:nowrap;}
.bsp-card-t{font-family:var(--fdisp);font-weight:700;font-size:19px;line-height:1.3;color:var(--ink);margin:2px 0 .7em;}
/* ---------- Grüne Leiste, modern (Variante B, 04.11.2026) ---------- */
.article h1{font-weight:800;letter-spacing:-.03em;line-height:1.08;}
.article h2{font-weight:700;letter-spacing:-.022em;} .article h3{font-weight:700;letter-spacing:-.015em;}
.article p,.article li{line-height:1.72;}
.topbar .searchBtn,.topbar .iconBtn,.topbar .panelBtn,.topbar .navBtn,.topbar .langs{border-radius:999px;}
.article .sect{border-radius:16px;box-shadow:0 1px 2px rgba(16,24,20,.04),0 4px 14px rgba(16,24,20,.04);}
.callout{border-radius:12px;}
.aufg{border-color:var(--border);border-radius:14px;}
.side li a.active{border-radius:999px;}
/* Nacht: Karten ohne Schatten, dafür helle Rahmen um alle Kästen (Wunsch des Users); farbige Randstreifen links bleiben */
:root[data-theme="dark"] .article .sect{box-shadow:none;}
:root[data-theme="dark"] :is(.article .sect,.callout,details.hintergrund,details.herleitung,details.frage,details.ltspice,details.quiz-item,
  .aufg,.article figure.abb,.arttoc,.zweck,.neighbors .nb,.pn,.theme-card,.fassung){
  border-top:1px solid var(--rahmen);border-right:1px solid var(--rahmen);border-bottom:1px solid var(--rahmen);}
:root[data-theme="dark"] .bsp-card{border-right:1px solid var(--rahmen);border-bottom:1px solid var(--rahmen);}
:root[data-theme="dark"] :is(.article .sect,.callout:not([class*="cx-"]),.callout.cx-zusatz,details.frage,details.quiz-item,
  .aufg,.article figure.abb,.arttoc,.zweck,.neighbors .nb,.pn,.theme-card,.bsp-card,.fassung){border-left:1px solid var(--rahmen);}
@media(max-width:720px){ .bsp-card{padding:4px 15px 12px;} }
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
"""

WISSEN_JS = r"""
var NICHTS={de:"Nichts gefunden für",en:"Nothing found for",es:"Nada encontrado para",zh:"未找到"};
// Suche: vorab gebauter Index (search.json), Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben.
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var DOCS=null, sel=-1, rows=[];
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").normalize("NFKD").replace(/[̀-ͯ]/g,""); }
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
    if(!rows.length) results.innerHTML='<div class="searchHint">'+esc(NICHTS[document.documentElement.lang]||NICHTS.de)+' „'+esc(raw.trim())+'".</div>';
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
"""

if __name__ == "__main__":
    main()
