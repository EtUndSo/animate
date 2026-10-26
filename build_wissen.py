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
Der Umschalter „KI | Mensch“ in der Kopfleiste wechselt zwischen den Fassungen desselben Themas; fehlt das
Gegenstück, ist der Knopf grau. Die Wahl wird gemerkt (localStorage), Themen-Links folgen ihr.
"""
import datetime, json, re, html, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC  = ROOT / "content"
OUT  = ROOT / "web" / "wissen"

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
_PROTECT = []
# Beispiel-Seite: render_article setzt hier eine Liste; md_to_html legt jedes ::::beispiel dort ab und lässt im
# Artikel nur einen Verweis stehen. None = Beispiele verwerfen (z. B. beim Lesen der Nachbar-Stichpunkte).
BSP_SINK = None
def _protect(m):
    _PROTECT.append(m.group(0)); return f"\x00{len(_PROTECT)-1}\x00"

_MC_RED, _MC_BLUE, _MC_GOLD = "#e5383b", "#2b6def", "#ff9f1c"   # Et-rot / UndSo-blau / Palette-gelb
def colorize_math(s):
    """Colour an (in)equation: left-hand side RED, every relation ('=' or '\\approx') BLUE, the
    part after it GOLD (via KaTeX \\textcolor). Splits only on a *top-level* relation (brace depth 0),
    so \\frac{..}{..}, \\text{..} and units stay intact. An expression without any relation (a lone
    symbol) is left in the normal colour — it then follows the surrounding text colour."""
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
    out = r"\textcolor{%s}{%s}" % (_MC_RED, segs[0])
    for rel, seg in zip(rels, segs[1:]):
        out += r"\textcolor{%s}{%s}\textcolor{%s}{%s}" % (_MC_BLUE, rel, _MC_GOLD, seg)
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
    text = re.sub(r"\*\*([^*]+)\*\*", _bold, text)
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

CALLOUTS = {"konzept": ("", "Zur Idee"), "kern": ("", "Das Wichtigste"), "merke": ("", "Merke"),
            "grafik": ("", "Abbildung"), "satz": ("", "Satz"), "definition": ("", "Definition"),
            "lemma": ("", "Lemma")}

def md_to_html(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, toc, i, n = [], [], 0, len(lines)
    section_open = False                                  # jeder ##-Abschnitt wird als Karte <section class="sect"> eingefasst
    formel_n = 0                                          # fortlaufende Nummer der :::formel-Boxen (zum Referenzieren, wie im Skript)
    cur_sect = ""                                         # Titel des aktuellen ##-Abschnitts (Bezug der Beispiele)
    para = []
    def beispiel(title, inner):                           # Beispiel -> Beispiel-Seite; im Artikel bleibt nur der Verweis
        if BSP_SINK is None:
            return
        k = len(BSP_SINK) + 1
        BSP_SINK.append({"k": k, "title": title, "sect": cur_sect, "html": md_to_html("\n".join(inner))[0]})
        out.append(f'<div class="bsp-ref" id="bspref-{k}" data-bsp="{k}"><a href="#bsp-{k}">'
                   f'<span class="bsp-n">Beispiel {k}</span><span class="bsp-tt">{inline(title)}</span>'
                   '<span class="bsp-arr" aria-hidden="true">→</span></a></div>')
    def flush():
        if para:
            txt = " ".join(para).strip()
            if not txt.startswith("**Worum es geht"):   # Einstiegs-Absatz entfällt – Artikel startet mit dem Inhaltsverzeichnis
                parts = split_display(txt)
                if parts:                                # mehrteilige Formelzeile: Teile dürfen umbrechen
                    out.append('<div class="mrow">' + "".join('<div class="mcell">' + inline("$$" + p + "$$") + "</div>"
                                                              for p in parts) + "</div>")
                else:
                    out.append("<p>" + inline(txt) + "</p>")
            para.clear()
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:                                     # blank -> paragraph break
            flush(); i += 1; continue
        if s.startswith("```"):                       # fenced code
            flush(); i += 1; code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + html.escape("\n".join(code), quote=False) + "</code></pre>")
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
            out.append('<aside class="callout cx-quiz"><div class="callout-h">Quiz — teste dein Verständnis</div>'
                       + "".join(body) + "</aside>")
            continue
        m = re.match(r":::(\w+)(?:\s+(.+?))?\s*$", s)  # callout block  :::konzept / :::formel Definition ... :::
        if m:
            flush(); kind = m.group(1).lower(); label_arg = (m.group(2) or "").strip(); i += 1; inner = []
            while i < n and lines[i].strip() != ":::":
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
            if kind == "herleitung":                      # Herleitung als ausklappbare Box an der Formel
                out.append('<details class="herleitung"><summary>Herleitung</summary>'
                           '<div class="hl-body">' + md_to_html("\n".join(inner))[0] + '</div></details>')
                continue
            if kind == "frage":                           # Frage-Kasten (wie im Lernskript): Frage sichtbar, Antwort ausklappbar
                if label_arg:
                    frage, rest = label_arg, inner
                else:
                    k0 = next((j for j, l in enumerate(inner) if l.strip()), len(inner))
                    frage, rest = (inner[k0].strip() if k0 < len(inner) else ""), inner[k0 + 1:]
                out.append('<details class="frage"><summary><span class="fr-k">Frage</span>' + inline(frage) + '</summary>'
                           '<div class="fr-body">' + md_to_html("\n".join(rest))[0] + '</div></details>')
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
            icon, label = CALLOUTS.get(kind, ("", kind.title()))
            out.append(f'<aside class="callout cx-{kind}"><div class="callout-h">{(icon + " " if icon else "") + html.escape(label)}</div>'
                       + md_to_html("\n".join(inner))[0] + "</aside>")
            continue
        if re.match(r"(---|\*\*\*|___)\s*$", s):      # horizontal rule
            flush(); out.append("<hr/>"); i += 1; continue
        hm = re.match(r"(#{1,4})\s+(.*)$", s)         # heading
        if hm:
            flush(); lvl = len(hm.group(1)); txt = hm.group(2).strip()
            hid = slugify(txt)
            if lvl == 2:                                   # neuer ##-Abschnitt -> alte Karte schließen, neue öffnen
                toc.append((hid, txt)); cur_sect = txt
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
    roots, ausf = {}, []
    for md_file in sorted(SRC.rglob("*.md")):
        meta, body = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        pfad = (meta.get("pfad") or "").strip()
        if not pfad:
            print("  übersprungen (kein pfad:):", md_file.relative_to(SRC)); continue
        parts = [p.strip() for p in pfad.split("/") if p.strip()]
        title = meta.get("title") or md_file.stem
        ov = (meta.get("order") or "").strip()
        order = int(ov) if ov.isdigit() else (int(re.match(r"(\d+)", md_file.stem).group(1)) if re.match(r"\d+", md_file.stem) else 999999)
        container, chain = roots, []
        for part in parts:
            nd = container.setdefault(slugify(part), _new_node(part))
            chain.append(nd); container = nd["children"]
        a_slug = re.sub(r"^\d+-", "", md_file.stem) or slugify(title)
        path = "/".join(nd["slug"] for nd in chain) + "/" + a_slug + ".html"
        autor = (meta.get("autor") or "").strip().lower()
        if re.search(r"-mensch(-ausfuehrlich)?$", a_slug):   # Dateiname-Suffix genügt
            autor = autor or "mensch"
        art = {"title": title, "slug": a_slug, "order": order, "path": path,
               "summary": meta.get("summary", ""), "tags": meta.get("tags", ""), "body": body,
               "crumbs": [(nd["name"], nd["slug"]) for nd in chain],
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
    return to_list(roots)

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
                    rows.append(f'<li><a{cls} href="/wissen/{a["path"]}"{alt_attr(a)}>{html.escape(a["title"])}</a></li>')
                rows.append("</ul>")
            if nd["children"]:
                rows.append(render(nd["children"], depth + 1))
            rows.append("</details>")
        return "".join(rows)
    return ('<nav class="side" aria-label="Wissensbaum">' + autor_switch(art, "side")
            + '<a class="side-home" href="/wissen/">Alle Module</a>' + render(tree, 0) + "</nav>")

def page_shell(title, desc, body, depth):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="de"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(title)} — EtUndSo</title>
<meta name="description" content="{html.escape(desc)}"/>
<script>try{{if(localStorage.getItem("animate-theme")==="dark")document.documentElement.setAttribute("data-theme","dark");}}catch(e){{}}
try{{if(/[?&]bsp=1/.test(location.search)||(localStorage.getItem("wissen-split")==="1"&&matchMedia("(min-width:1180px)").matches))document.documentElement.classList.add("bsp-on");}}catch(e){{}}</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css"/>
<link rel="stylesheet" href="/wissen/assets/wissen.css"/>
</head><body data-root="/wissen/">
{body}
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>
<script src="/wissen/assets/wissen.js"></script>
</body></html>"""

def alt_attr(a):
    """Daten-Attribute an Links auf die kompakte KI-Fassung eines Themas: wer „Ausführlich“ bzw. „Mensch“ gewählt hat,
    wird per JS zur passenden Fassung gelenkt (data-alt, data-mensch, data-mensch-alt)."""
    if not a:
        return ""
    s = f' data-alt="/wissen/{a["alt"]["path"]}"' if a.get("alt") and a.get("fassung") == "kompakt" else ""
    h = a.get("human")
    if h:
        s += f' data-mensch="/wissen/{h["path"]}"'
        if h.get("alt"):
            s += f' data-mensch-alt="/wissen/{h["alt"]["path"]}"'
    return s

def tree_art(art):
    """Der Eintrag im Baum, zu dem eine Seite gehört: die kompakte KI-Fassung des Themas."""
    a = art["alt"] if art.get("fassung") == "ausfuehrlich" and art.get("alt") else art
    return a.get("human_of") or a

def counterpart(art, kind):
    """Gegenstück desselben Themas mit autor=kind, möglichst in derselben Fassung; None, wenn es keins gibt."""
    if art.get("autor") == kind:
        return art
    base = art["alt"] if art.get("fassung") == "ausfuehrlich" and art.get("alt") else art   # kompakte Fassung
    other = base.get("human") if kind == "mensch" else base.get("human_of")
    if not other:
        return None
    return other["alt"] if base is not art and other.get("alt") else other

def autor_switch(art=None, where="top"):
    # Umschalter KI | Mensch in der Kopfleiste (User 2026-10-26: eigene, von Hand geschriebene Artikel neben den
    # KI-Fassungen). Auf Artikelseiten: Links zum Gegenstück desselben Themas, grau ohne Gegenstück; auf der
    # Übersicht: Knöpfe, die nur die Vorliebe setzen. Die Wahl wird gemerkt, Themen-Links folgen ihr (wissen.js).
    icons = {"ki": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                   'stroke-linecap="round" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="2"/>'
                   '<path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
             "mensch": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                       'stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7.5 8-7.5s8 3.1 8 7.5"/></svg>'}
    fehlt = {"ki": "Zu diesem Thema gibt es noch keine KI-Fassung",
             "mensch": "Zu diesem Thema gibt es noch keine von Hand geschriebene Fassung"}
    btns = ""
    for kind, label in (("ki", "KI"), ("mensch", "Mensch")):
        inner = icons[kind] + f'<span class="lbl">{label}</span>'
        if art is None:
            btns += f'<button type="button" class="a-btn" data-autor="{kind}" title="{label}-Fassungen bevorzugen">{inner}</button>'
            continue
        tgt = counterpart(art, kind)
        if tgt is art:
            btns += f'<a class="a-btn on" href="/wissen/{art["path"]}" data-autor="{kind}" aria-current="page" title="{label}-Fassung (diese Seite)">{inner}</a>'
        elif tgt:
            btns += f'<a class="a-btn" href="/wissen/{tgt["path"]}" data-autor="{kind}" title="Zur {label}-Fassung dieses Themas">{inner}</a>'
        else:
            btns += f'<span class="a-btn off" title="{fehlt[kind]}" aria-disabled="true">{inner}</span>'
    # where: "top" = Kopfleiste (ab Tablet-Breite); auf dem Handy passt er dort nicht mehr neben Pfeile, Suche und
    # Hell/Dunkel, deshalb steht er dann unter dem Titel ("art", neben Kompakt | Ausführlich) und oben im Themenbaum ("side").
    return f'<nav class="autor autor-{where}" aria-label="KI- oder von Hand geschriebene Fassung">{btns}</nav>'

def lesezeit(body):
    """Lesezeit des Hauptpfads in Minuten (170 Wörter/min; ohne Herleitungen, Beispiele, Quiz, Formeln, Abbildungen)."""
    t = re.sub(r"^::::\s*beispiel.*?^::::\s*$", " ", body, flags=re.S | re.M)
    t = re.sub(r"^:::\s*(?:herleitung|quiz|frage)\b.*?^:::\s*$", " ", t, flags=re.S | re.M)   # eingeklappte Kästen
    t = re.sub(r"^:::\s*grafik\b.*?^:::\s*$", " ", t, flags=re.S | re.M)   # Abbildungen zählen nicht (wie früher die Bildunterschriften)
    t = re.sub(r"\$\$.+?\$\$", " ", t, flags=re.S)
    t = re.sub(r"^\s*<.*$", " ", t, flags=re.M)
    return max(1, round(len([w for w in t.split() if re.search(r"[A-Za-zÄÖÜäöüß0-9]", w)]) / 170))

def nav_arrow(a, prev):
    # Pfeil neben den Panel-Buttons zum vorherigen/nächsten Artikel (dieselbe Reihenfolge wie unten
    # „Vorheriger/Nächster Artikel"); am Anfang bzw. Ende grau und ohne Funktion.
    bid, word = ("navPrev", "Vorheriger") if prev else ("navNext", "Nächster")
    svg = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           + ('<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>' if prev else
              '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>') + '</svg>')
    if a:
        t = html.escape(f'{word} Artikel: {a["title"]}')
        return f'<a id="{bid}" class="navBtn" href="/wissen/{a["path"]}"{alt_attr(a)} title="{t}" aria-label="{t}">{svg}</a>'
    return f'<span id="{bid}" class="navBtn disabled" aria-disabled="true" title="Kein {word.lower()} Artikel">{svg}</span>'

def topbar(panels=False, bsp=False, prev_a=None, next_a=None, art=None):
    # Panel-Buttons (nur Artikelseiten, mittig): links=Themenbaum, rechts=Gliederung, dritter=geteilte Ansicht
    # mit der Beispiel-Seite (Theorie links, Beispiele rechts) – ausgegraut, solange der Artikel keine Beispiele hat.
    # Davor und dahinter je ein Pfeil zum vorherigen/nächsten Artikel. Farbe: offen = blau, zu = grau.
    bsp_btn = ('<button id="toggleBsp" class="panelBtn" aria-pressed="false" '
               + ('aria-label="Beispiel-Seite ein-/ausblenden" title="Beispiel-Seite: Theorie links, Beispiele rechts"'
                  if bsp else 'aria-label="Beispiel-Seite" title="Für diesen Artikel gibt es noch keine Beispiel-Seite" disabled')
               + '><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
               '<rect x="2.5" y="4" width="19" height="16" rx="2"/><line x1="12" y1="4" x2="12" y2="20"/>'
               '<line x1="14.5" y1="9" x2="19" y2="9"/><line x1="14.5" y1="12.5" x2="19" y2="12.5"/><line x1="14.5" y1="16" x2="17.5" y2="16"/></svg></button>')
    pbtns = ('<div class="panelCenter">' + nav_arrow(prev_a, True)
             + '<button id="toggleLeft" class="panelBtn" aria-label="Themenbaum ein-/ausblenden" title="Themenbaum ein-/ausblenden" aria-pressed="false">'
             '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="9" y1="4" x2="9" y2="20"/></svg></button>'
             '<button id="toggleRight" class="panelBtn is-open" aria-label="Gliederung ein-/ausblenden" title="Gliederung ein-/ausblenden" aria-pressed="true">'
             '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="15" y1="4" x2="15" y2="20"/></svg></button>'
             + bsp_btn + nav_arrow(next_a, False) + '</div>') if panels else ''
    return ('<div class="topbar"><a class="brand" href="/">Et<span>Und</span><span class="so">So</span></a>'
            + autor_switch(art) + pbtns
            + '<button id="searchBtn" class="searchBtn" aria-label="Suche">'   # ohne Lupen-Symbol (User 2026-10-21)
            '<span class="lbl">Suchen</span><kbd>/</kbd></button>'
            # Hell/Dunkel-Umschalter — immer oben rechts, auf allen Wissensseiten an gleicher Stelle.
            '<button id="themeBtn" class="iconBtn" aria-label="Hell/Dunkel umschalten" title="Hell/Dunkel umschalten">'
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M21 12.8A8 8 0 1 1 11.2 3 6 6 0 0 0 21 12.8z"/></svg></button>'
            + '<a class="editorlink" href="/editor.html">Editor</a></div>'
            '<div id="searchOverlay" class="searchOverlay" hidden><div class="searchBox">'
            '<input id="searchInput" type="search" placeholder="Thema, Begriff, Formel …" autocomplete="off"/>'
            '<div id="searchResults" class="searchResults"></div>'
            '<div class="searchHint">Teilwörter erlaubt (z. B. „teiler" findet „Spannungsteiler"). '
            '<kbd>Esc</kbd> schließt.</div></div></div>')

def render_article(art, tree, prev_a, next_a):
    global BSP_SINK
    BSP_SINK = []
    body_html, toc = md_to_html(art["body"])
    examples, BSP_SINK = BSP_SINK, None
    quiz_html = ""                                     # Quiz ganz unten, unter den Nachbar-Spalten (User 2026-10-21)
    qa = body_html.find('<aside class="callout cx-quiz">')
    if qa >= 0:
        qe = body_html.index("</aside>", qa) + len("</aside>")
        quiz_html, body_html = body_html[qa:qe], body_html[:qa] + body_html[qe:]
    pane = ""
    if examples:                                       # Beispiel-Seite (rechts in der geteilten Ansicht)
        cards = "".join(
            f'<section class="bsp-card" id="bsp-{e["k"]}"><div class="bsp-card-h"><span class="bsp-card-n">Beispiel {e["k"]}</span>'
            f'<a class="bsp-back" href="#bspref-{e["k"]}" data-bsp="{e["k"]}" title="Zur Stelle im Artikel">↖ {html.escape(e["sect"])}</a></div>'
            + (f'<div class="bsp-card-t">{inline(e["title"])}</div>' if e["title"] else "")
            + e["html"] + "</section>" for e in examples)
        pane = ('<aside class="bsp-pane" id="bspPane" aria-label="Beispiele zu diesem Artikel">'
                '<div class="bsp-pane-h">Beispiele <span>– die Aussagen des Artikels, an konkreten Fällen durchgerechnet</span></div>'
                + cards + "</aside>")
    pill = ('<span class="apill apill-mensch">von Hand geschrieben</span>' if art["autor"] == "mensch"
            else '<span class="apill">KI-generiert</span>')
    crumb = '<nav class="crumbs"><a href="/wissen/">Wissen</a>' + \
            "".join(f' › <span>{html.escape(nm)}</span>' for nm, sl in art["crumbs"]) + " " + pill + "</nav>"
    toc_html = ""
    arttoc = ""
    if toc:
        toc_html = '<aside class="toc"><div class="toc-h">Auf dieser Seite</div><ul>' + \
            "".join(f'<li><a href="#{hid}">{html.escape(txt)}</a></li>' for hid, txt in toc) + "</ul></aside>"
        arttoc = '<nav class="arttoc" aria-label="Inhalt dieses Artikels"><div class="arttoc-h">In diesem Artikel</div><ul>' + \
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
        nav += (f'<a class="nb" href="/wissen/{prev_a["path"]}"{alt_attr(prev_a)}><div class="nb-dir">← Vorheriger Artikel</div>'
                f'<div class="nb-t">{html.escape(prev_a["title"])}</div><ul>{_topics(prev_a)}</ul></a>')
    else:
        nav += '<div class="nb empty"></div>'
    if next_a:
        nav += (f'<a class="nb" href="/wissen/{next_a["path"]}"{alt_attr(next_a)}><div class="nb-dir next">Nächster Artikel →</div>'
                f'<div class="nb-t">{html.escape(next_a["title"])}</div><ul>{_topics(next_a)}</ul></a>')
    else:
        nav += '<div class="nb empty"></div>'
    nav += "</div>"
    main = (f'<main class="article"><article>{crumb}<h1>{html.escape(art["title"])}</h1>'
            + autor_switch(art, "art") + switch + arttoc
            + body_html + nav + quiz_html + legal_footer() + "</article>" + toc_html + pane + "</main>")
    nav_path = tree_art(art)["path"]
    body = (topbar(panels=True, bsp=bool(examples), prev_a=prev_a, next_a=next_a, art=art)
            + f'<div class="layout{" has-bsp" if examples else ""}">'
            + sidebar_html(tree, nav_path, art) + main + "</div>")
    depth = 1 + art["path"].count("/")               # web/wissen/<…chain…>/<a>.html
    return page_shell(art["title"], art["summary"] or art["title"], body, depth)

def legal_footer():
    return ('<footer class="wfoot">EtUndSo.de · <a href="/impressum.html">Impressum</a> · '
            '<a href="/datenschutz.html">Datenschutz</a></footer>')

def render_index(tree):
    cards = ['<main class="article"><article><h1>Wissen</h1>'
             '<p class="lede">Verständliche, animierte Erklärungen — von Grund auf und in kleinen Schritten. '
             'Wähle ein Modul oder nutze die Suche.</p>']
    if not tree:
        cards.append('<p class="empty">Hier entstehen nach und nach die Artikel.</p>')
    # Übersicht: oberste Ebene(n) als Abschnitt, darunter der Baum rekursiv; Themen als verlinkte Karten.
    def block(nodes, depth):
        rows = []
        for nd in nodes:
            leaf_cards = ""
            if nd["articles"]:
                links = "".join(f'<li><a href="/wissen/{a["path"]}">{html.escape(a["title"])}</a></li>' for a in nd["articles"])
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
def main():
    tree = collect()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "data").mkdir(exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)

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

    (OUT / "index.html").write_text(render_index(tree), encoding="utf-8")

    # navigation tree (ohne bodies, beliebig tief) + search index
    def jnode(nd):
        return {"name": nd["name"], "slug": nd["slug"],
                "articles": [{"title": a["title"], "path": a["path"], "summary": a["summary"],
                              **({"alt": a["alt"]["path"]} if a.get("alt") else {}),
                              **({"mensch": a["human"]["path"]} if a.get("human") else {})} for a in nd["articles"]],
                "children": [jnode(c) for c in nd["children"]]}
    tree_json = [jnode(n) for n in tree]
    (OUT / "data" / "tree.json").write_text(json.dumps(tree_json, ensure_ascii=False), encoding="utf-8")

    search = []
    alts = [a["alt"] for a in flat if a.get("alt")]
    humans = [a["human"] for a in flat if a.get("human")]
    humans += [h["alt"] for h in humans if h.get("alt")]
    for a in flat + alts + humans:
        plain = to_plain(a["body"])
        crumb = " › ".join(nm for nm, sl in a["crumbs"])
        title = a["title"] + (" (ausführlich)" if a.get("fassung") == "ausfuehrlich" and a.get("alt") else "") \
            + (" (von Hand)" if a["autor"] == "mensch" else "")
        search.append({"title": title, "crumb": crumb, "path": a["path"],
                       "summary": a["summary"], "tags": a["tags"],
                       # pre-folded fields for fast infix matching; 'text' kept (original) for snippets
                       "ft_title": fold(title), "ft_tags": fold(a["tags"]),
                       "ft_text": fold(a["summary"] + " " + plain), "text": plain})
    (OUT / "data" / "search.json").write_text(json.dumps(search, ensure_ascii=False), encoding="utf-8")

    (OUT / "assets" / "wissen.css").write_text(WISSEN_CSS, encoding="utf-8")
    (OUT / "assets" / "wissen.js").write_text(WISSEN_JS, encoding="utf-8")
    day = write_version()

    n_mod = sum(1 for _ in flat)
    print(f"✓ {n_mod} Artikel (+{len(alts)} ausführliche Fassungen, +{len(humans)} von Hand), {len(tree)} Studiengänge -> {OUT} · Stand {day}")

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
/* Palette „Signal & Ink" — Tag Standard, Nacht via data-theme=dark (folgt dem Editor-Theme). */
:root{ --bg:#f4f6fa; --panel:#ffffff; --ink:#10161f; --muted:#56617a; --border:#e0e5ee; --soft:#eef1f7;
  --accent:#2b6def; --accent2:#e5383b; --accent3:#ff9f1c; --radius:14px;
  --fdisp:"Segoe UI",system-ui,-apple-system,Roboto,sans-serif; --fbody:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --fmono:ui-monospace,"Cascadia Code",Consolas,monospace; }
/* Nacht (User 2026-10-21): Flächen aus der verbreiteten Slate-Skala (Dunkelblau-Grau, kein Schwarz; Tiefe durch hellere
   Karten wie bei Material Design), Hauptfarben bleiben Rot, Orange und Hellblau, alle mit mindestens 4,5 : 1 auf den Karten. */
:root[data-theme="dark"]{ --bg:#0f172a; --panel:#1e293b; --ink:#f1f5f9; --muted:#94a3b8; --border:#334155; --soft:#162032;
  --accent:#5c94ff; --accent2:#ff5e60; --accent3:#ffb54d; }
/* Formelfarben (\textcolor der Build-Färbung) nachts in den hellen Varianten, sonst nur gut 3 : 1 Kontrast.
   KaTeX setzt die Farbe per Skript, der Browser schreibt sie dann als rgb(…) ins style-Attribut. */
:root[data-theme="dark"] .katex [style*="rgb(229, 56, 59)"],:root[data-theme="dark"] .katex [style*="#e5383b"]{color:var(--accent2)!important;}
:root[data-theme="dark"] .katex [style*="rgb(43, 109, 239)"],:root[data-theme="dark"] .katex [style*="#2b6def"]{color:var(--accent)!important;}
:root[data-theme="dark"] .katex [style*="rgb(255, 159, 28)"],:root[data-theme="dark"] .katex [style*="#ff9f1c"]{color:var(--accent3)!important;}
*{box-sizing:border-box;} html{scroll-behavior:smooth;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--fbody);line-height:1.68;-webkit-font-smoothing:antialiased;}
a{color:var(--accent);text-decoration:none;} a:hover{text-decoration:underline;}
kbd{font-family:var(--fmono);font-size:.82em;background:var(--soft);border:1px solid var(--border);border-radius:5px;padding:1px 5px;}
.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:14px;padding:11px 18px;background:var(--panel);border-bottom:1px solid var(--border);}
.brand{font-family:var(--fdisp);font-weight:800;font-size:19px;letter-spacing:-.02em;color:var(--accent2);}
.brand span{color:var(--accent);} .brand span.so{color:var(--accent3);}
.topbar .searchBtn{margin-left:auto;display:flex;align-items:center;gap:8px;background:var(--soft);border:1px solid var(--border);color:var(--muted);
  border-radius:10px;padding:8px 13px;font:inherit;font-size:14px;cursor:pointer;}
.topbar .searchBtn:hover{border-color:var(--accent);color:var(--ink);}
.topbar .editorlink{font-weight:600;color:var(--muted);} .topbar .editorlink:hover{color:var(--ink);}
.topbar .iconBtn,.topbar .panelBtn,.topbar .navBtn{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;background:var(--soft);border:1px solid var(--border);color:var(--muted);border-radius:10px;cursor:pointer;}
.topbar .iconBtn:hover{border-color:var(--accent);color:var(--ink);}
.topbar .panelBtn:hover{background:color-mix(in srgb,var(--accent) 12%,var(--soft));}   /* Hover nur über den Hintergrund: der Rand zeigt den Zustand */
.topbar .panelBtn.is-open{color:var(--accent);border-color:var(--accent);}   /* Panel offen = blau, zu = grau (Grundfarbe) */
.topbar .navBtn{color:var(--accent);border-color:var(--accent);}             /* Pfeile zum vorherigen/nächsten Artikel */
.topbar .navBtn:hover{text-decoration:none;background:color-mix(in srgb,var(--accent) 12%,var(--soft));}
.topbar .navBtn.disabled{color:var(--muted);border-color:var(--border);opacity:.45;cursor:default;pointer-events:none;}   /* erster/letzter Artikel: grau, ohne Funktion */
.topbar .panelCenter{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;gap:8px;}  /* Einklapp-Buttons mittig in der Leiste */
/* Umschalter KI | Mensch (neben dem Logo): aktive Fassung blau unterstrichen wie der Fassungs-Umschalter; ohne Gegenstück grau.
   Auf dem Handy (≤720 px) verschwindet er aus der Leiste und erscheint unter dem Titel (.autor-art) und oben im Themenbaum (.autor-side). */
.autor{display:inline-flex;height:36px;border:1px solid var(--border);border-radius:10px;overflow:hidden;background:var(--soft);flex:none;vertical-align:middle;}
.autor .a-btn{display:inline-flex;align-items:center;gap:6px;padding:0 11px;font:inherit;font-size:13.5px;font-weight:600;color:var(--muted);background:none;border:0;cursor:pointer;}
.autor .a-btn:hover{color:var(--ink);text-decoration:none;}
.autor .a-btn.on{background:var(--panel);color:var(--accent);box-shadow:inset 0 -2px 0 var(--accent);}
.autor .a-btn.off{opacity:.4;cursor:default;} .autor .a-btn.off:hover{color:var(--muted);}
.autor-art,.autor-side{display:none;}
.article .autor-art{margin:.1em 10px 1.2em 0;}
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
.side .lvl0>summary{font-weight:700;color:var(--accent2);}  /* Fach/Studiengang: rot */
.side .lvl1>summary{font-weight:600;color:var(--accent3);}  /* Semester: orange */
.side .lvl2>summary,.side .lvl3>summary,.side .lvl4>summary{font-weight:500;}
.side .lvl2>summary{color:var(--accent);}                 /* Modul: blau */
.side ul{list-style:none;margin:0 0 4px;padding-left:22px;} .side li{margin:1px 0;}
.side li a{display:block;color:var(--ink);padding:3px 7px;border-radius:7px;}   /* Unterthemen/Themen: schwarz (im Dunkelmodus hell) */
.side li a:hover{color:var(--ink);background:var(--soft);text-decoration:none;}
.side li a.active{color:#fff;background:var(--accent);font-weight:600;}
.article{min-width:0;padding:26px 30px 70px;display:grid;grid-template-columns:minmax(0,1fr) 210px;gap:34px;align-items:start;}
.article>article{min-width:0;width:100%;max-width:72ch;margin-inline:auto;}   /* zentriert -> bleibt beim Einklappen der Panels gleich breit; width:100%: sonst zieht die breiteste Formel den Artikel (auto-Ränder = fit-content) über die Spalte hinaus -> Text läuft auf Handy/Tablet rechts raus */
.crumbs{font-size:13px;color:var(--muted);margin-bottom:10px;} .crumbs a{color:var(--muted);}
.article h1{font-family:var(--fdisp);font-size:clamp(26px,4vw,38px);line-height:1.1;letter-spacing:-.02em;margin:.1em 0 .3em;text-wrap:balance;color:var(--accent2);}  /* Titel: Et-rot */
.article h2{font-family:var(--fdisp);font-size:24px;margin:2.5em 0 .5em;letter-spacing:-.01em;scroll-margin-top:66px;color:var(--accent2);}   /* Zwischenüberschrift: Et-rot, mehr Luft davor */
.article h3{font-family:var(--fdisp);font-size:19px;margin:1.9em 0 .7em;scroll-margin-top:66px;color:var(--accent2);}
.article p,.article li{font-size:17.5px;} .article p{margin:0 0 1.35em;} .article li{margin:.3em 0;} .article ul,.article ol{margin:0 0 1.35em;} .article .lede{font-size:18.5px;color:var(--muted);margin:.2em 0 1.3em;}
/* --- Farbkategorien (je eine Zeile): wichtige Wörter = orange, Namen = blau, Schritt-Marken = rot --- */
.article strong{color:var(--accent3);}             /* wichtige Ausdrücke/Wörter */
.article strong.nm{color:var(--accent);}           /* Namen (Größen, Begriffe, Einheiten) */
.article strong.step{color:var(--accent2);}        /* „Schritt N" */
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
.article blockquote{margin:1em 0;padding:2px 16px;border-left:3px solid var(--accent);color:var(--muted);}
.table-wrap{overflow-x:auto;margin:1.2em 0;}
.md-table{border-collapse:collapse;width:100%;font-size:15.5px;}
.md-table th,.md-table td{padding:8px 12px;border:1px solid var(--border);text-align:left;vertical-align:top;}
.md-table thead th{background:var(--soft);font-family:var(--fdisp);color:var(--accent);font-weight:700;}
.md-table tbody tr:nth-child(even){background:color-mix(in srgb,var(--soft) 55%,transparent);}
.callout{margin:1.7em 0;padding:16px 18px;border:1px solid var(--border);border-radius:12px;background:var(--soft);}
.callout-h{font-weight:700;font-family:var(--fdisp);margin-bottom:4px;color:var(--accent);}   /* Box-Überschrift: UndSo-blau */
.callout.cx-konzept{border-left:4px solid var(--accent);} .callout.cx-kern{border-left:4px solid var(--accent2);background:color-mix(in srgb,var(--accent2) 7%,var(--panel));}
.callout.cx-kern .callout-h{color:var(--accent2);}  /* Kernbox: Titel in Rot, passend zum roten Rand */
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
.callout.cx-fehlvorstellung{border-left:4px solid var(--accent2);} .callout.cx-fehlvorstellung .callout-h{color:var(--accent2);}
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
.nb-t{font-weight:700;color:var(--accent2);margin:3px 0 8px;font-family:var(--fdisp);}
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
.prevnext{display:flex;justify-content:space-between;gap:14px;margin:36px 0 10px;flex-wrap:wrap;}
.pn{flex:1 1 200px;border:1px solid var(--border);border-radius:12px;padding:12px 15px;font-weight:600;background:var(--panel);}
.pn span{display:block;font-size:12px;color:var(--muted);font-weight:500;margin-bottom:2px;} .pn.next{text-align:right;}
.toc{position:sticky;top:66px;align-self:start;font-size:13.5px;border-left:1px solid var(--border);padding-left:16px;}
.toc-h{text-transform:uppercase;letter-spacing:.05em;font-size:11px;color:var(--muted);font-weight:700;margin-bottom:8px;}
.toc ul{list-style:none;margin:0;padding:0;} .toc li{margin:5px 0;} .toc a{color:var(--muted);} .toc a.active{color:var(--accent);font-weight:600;}
.field-block{margin:26px 0;} .field-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;}
.idx-node{margin:10px 0 10px 4px;padding-left:14px;border-left:2px solid var(--border);}
.idx-node h3{font-size:16px;margin:.4em 0 .3em;color:var(--ink);} .lvl-h{font-size:14.5px;margin:.5em 0 .2em;color:var(--accent3);font-weight:700;letter-spacing:.01em;}  /* Semester: orange */
.idx-node h3.idx-lvl2{color:var(--accent);}              /* Modul: blau (Oberthemen bleiben Standard-Ink/schwarz) */
.theme-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px;}
.theme-card h3{font-family:var(--fdisp);margin:0 0 6px;font-size:16px;} .theme-card ul{list-style:none;margin:0;padding:0;} .theme-card li{margin:4px 0;}
.theme-card a{color:var(--ink);} .theme-card a:hover{color:var(--accent);}   /* Unterthemen schwarz, Hover blau */
.field-block>h2{color:var(--accent2);}   /* Fach/Studiengang: rot (wie Sidebar lvl0) */
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
/* ---------- Beispiel-Seite: geteilte Ansicht (Theorie links | Beispiele rechts, Farbe Orange = Praxis) ---------- */
.topbar .panelBtn:disabled{opacity:.35;cursor:not-allowed;}   /* Beispiel-Knopf: offen = blau wie die anderen Panels (is-open) */
.topbar .panelBtn:disabled:hover{border-color:var(--border);color:var(--muted);}
.bsp-ref{margin:-.4em 0 1.4em;display:flex;justify-content:flex-end;position:relative;z-index:1;}  /* Verweis im Artikel, wo das Beispiel hingehört; über den KaTeX-Hilfsboxen des Folgetexts */
.bsp-ref a{display:inline-flex;align-items:baseline;gap:8px;max-width:100%;font-size:14.5px;line-height:1.4;color:var(--ink);
  border:1px solid color-mix(in srgb,var(--accent3) 55%,var(--border));background:color-mix(in srgb,var(--accent3) 8%,var(--panel));
  border-radius:999px;padding:4px 14px;}
.bsp-ref a:hover{text-decoration:none;border-color:var(--accent3);}
.bsp-ref .bsp-n{font-family:var(--fdisp);font-weight:700;color:var(--accent3);white-space:nowrap;}
.bsp-ref .bsp-tt{color:var(--muted);min-width:0;}
.bsp-ref .bsp-arr{color:var(--accent3);font-weight:700;}
.bsp-pane{display:none;}
.bsp-pane-h{font-family:var(--fdisp);font-weight:800;color:var(--accent3);font-size:13px;text-transform:uppercase;letter-spacing:.05em;margin:4px 2px 14px;}
.bsp-pane-h span{font-weight:500;text-transform:none;letter-spacing:0;color:var(--muted);font-size:13.5px;}
.bsp-card{border:1px solid var(--border);border-top:4px solid var(--accent3);border-radius:14px;background:var(--panel);padding:4px 20px 14px;margin:0 0 18px;transition:box-shadow .35s;}
.bsp-card.flash{box-shadow:0 0 0 4px color-mix(in srgb,var(--accent3) 40%,transparent);}
.bsp-card-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin:9px 0 2px;}
.bsp-card-n{font-family:var(--fdisp);font-weight:700;font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent3);white-space:nowrap;}
.bsp-back{font-size:13px;color:var(--muted);text-align:right;}
.bsp-card-t{font-family:var(--fdisp);font-weight:700;font-size:19px;line-height:1.3;color:var(--ink);margin:2px 0 .7em;}
/* geteilt: Baum-Spalte entfällt, Artikel rückt nach links, rechts die Beispiel-Seite in gleicher Breite (eigene Scroll-Spalte) */
.bsp-on .layout.has-bsp{grid-template-columns:minmax(0,1fr);max-width:none;}
.bsp-on .layout.has-bsp>.side{display:none;}
.bsp-on .layout.has-bsp>main{grid-column:1;}
.bsp-on .layout.has-bsp .toc,.bsp-on #toggleRight{display:none;}
.bsp-on .layout.has-bsp .article{grid-template-columns:minmax(0,72ch) minmax(0,72ch);justify-content:center;gap:30px;}
.bsp-on .layout.has-bsp .article>article{margin-inline:0;}
.bsp-on .layout.has-bsp .bsp-pane{display:block;position:sticky;top:59px;align-self:start;height:calc(100vh - 59px);overflow:auto;
  overscroll-behavior:contain;padding:18px 6px 45vh 2px;scrollbar-width:thin;}
.bsp-on .layout.has-bsp .bsp-ref a{border-color:var(--accent3);}
.bsp-on .layout.has-bsp .article .katex-display{font-size:1.16em;}   /* schmalere Spalten: lange Formeln passen eher */
.bsp-pane .katex-display{font-size:1.16em;}
.bsp-on .layout.has-bsp>.side.open{display:block;position:fixed;top:59px;left:0;bottom:0;width:min(320px,88vw);z-index:30;
  background:var(--panel);max-height:none;box-shadow:8px 0 30px rgba(0,0,0,.18);align-self:stretch;}   /* Themenbaum als Overlay (stretch: zwischen Leiste und Unterkante) */
@media(max-width:1179px){   /* zu schmal für zwei Spalten: Beispiel-Seite legt sich über den Artikel */
  .bsp-on .layout.has-bsp .article{grid-template-columns:minmax(0,1fr);}
  .bsp-on .layout.has-bsp .bsp-pane{position:fixed;inset:59px 0 0;z-index:25;height:auto;align-self:stretch;background:var(--bg);
    padding:16px max(14px,calc((100vw - 76ch) / 2)) 64px;}   /* stretch: sonst hängt die Ebene in voller Inhaltshöhe am oberen Rand */
}
@media(max-width:720px){ .bsp-on .layout.has-bsp .bsp-pane{top:57px;} .bsp-card{padding:4px 15px 12px;} }
@media(max-width:620px){ .arttoc ul{grid-template-columns:1fr;} }
@media(max-width:920px){ .article{grid-template-columns:1fr;} .toc{display:none;} #toggleRight{display:none;} }   /* keine Gliederung -> ihr Toggle weg */
@media(max-width:720px){ .layout{grid-template-columns:1fr;} .side{display:none;border-right:none;}
  /* Themenbaum als Overlay (über #toggleLeft geöffnet); muss das Desktop-Einklappen überstimmen */
  .layout .side.open{display:block;position:fixed;inset:56px 0 0;z-index:30;background:var(--panel);max-height:none;overflow:auto;padding:14px 16px 48px;
    align-self:stretch;}   /* stretch: sonst richtet sich das Overlay nach dem Inhalt (align-self:start der Spalte) und rutscht über die Leiste */
  .topbar{gap:8px;padding:10px 12px;} .topbar .searchBtn{padding:8px;}
  .topbar .panelCenter{position:static;transform:none;margin-left:auto;gap:4px;}   /* im Fluss: zwischen Logo und Suche, nichts überlappt */
  .topbar .searchBtn kbd{display:none;}   /* Suchknopf nur mit dem Wort, ohne Tastenhinweis */
  .topbar .autor-top{display:none;} .autor-art{display:inline-flex;} .side .autor-side{display:inline-flex;margin-bottom:12px;}   /* Handy: Umschalter unter dem Titel und im Themenbaum statt in der Leiste */
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
// Suche: vorab gebauter Index (search.json), Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben.
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var DOCS=null, sel=-1, rows=[];
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").normalize("NFKD").replace(/[̀-ͯ]/g,""); }
  function load(){ if(DOCS) return Promise.resolve(DOCS);
    return fetch("/wissen/data/search.json").then(function(r){return r.json();}).then(function(d){DOCS=d;return d;}).catch(function(){DOCS=[];return [];}); }
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
    if(!rows.length) results.innerHTML='<div class="searchHint">Nichts gefunden für „'+esc(raw.trim())+'".</div>';
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
  // Knopffarbe: Panel offen = blau (Klasse is-open), zu = grau; aria-pressed folgt „offen".
  function mark(btn,open){ if(btn){ btn.classList.toggle("is-open",!!open); btn.setAttribute("aria-pressed",open?"true":"false"); } }
  function L(k){ try{ return localStorage.getItem(k)==="1"; }catch(e){ return false; } }
  function S(k,v){ try{ localStorage.setItem(k,v?"1":"0"); }catch(e){} }
  // Ist der Themenbaum sichtbar? Mobil und in der geteilten Ansicht ist er ein Overlay, sonst eine Spalte.
  function leftOpen(){ var split=root.classList.contains("bsp-on")&&layout.classList.contains("has-bsp");
    return (mq.matches||split) ? !!(side&&side.classList.contains("open")) : !layout.classList.contains("hide-left"); }
  // Rechts (Gliederung): nur am Desktop sinnvoll, Zustand merken.
  if(bR){ if(L("wissen-hide-right")) layout.classList.add("hide-right");
    mark(bR,!layout.classList.contains("hide-right"));
    bR.addEventListener("click",function(){ var hidden=layout.classList.toggle("hide-right"); mark(bR,!hidden); S("wissen-hide-right",hidden); }); }
  // Links (Themenbaum): Desktop = beim Öffnen IMMER eingeklappt (Toggle gilt nur für die aktuelle Seite); Mobil = Overlay auf/zu.
  if(bL){ if(!mq.matches) layout.classList.add("hide-left");
    mark(bL,leftOpen());
    bL.addEventListener("click",function(){
      var split=root.classList.contains("bsp-on")&&layout.classList.contains("has-bsp");   // geteilte Ansicht: Baum als Overlay
      if(mq.matches||split){ if(side) side.classList.toggle("open"); }
      else layout.classList.toggle("hide-left");
      mark(bL,leftOpen());
    });
    document.addEventListener("wissen:layout",function(){ mark(bL,leftOpen()); });   // geteilte Ansicht an/aus
  }
  // Breitenwechsel aufräumen: Overlay nur mobil, am Desktop wieder eingeklappt.
  (mq.addEventListener?mq.addEventListener.bind(mq,"change"):mq.addListener.bind(mq))(function(e){
    if(e.matches) layout.classList.remove("hide-left");
    else { if(side) side.classList.remove("open"); layout.classList.add("hide-left"); }
    mark(bL,leftOpen());
  });
})();
// Beispiel-Seite (geteilte Ansicht): Theorie links, Beispiele rechts. Beide Spalten laufen synchron – jedes Beispiel
// steht auf Höhe der Formel, zu der es gehört (Bezugslinie bei 35 % der Fensterhöhe, dazwischen linear überblendet).
// Zu schmale Fenster: Die Beispiel-Seite legt sich als Ebene über den Artikel.
(function(){
  var root=document.documentElement, btn=document.getElementById("toggleBsp"),
      layout=document.querySelector(".layout.has-bsp"), pane=document.getElementById("bspPane");
  if(!btn) return;
  if(!layout||!pane){ root.classList.remove("bsp-on"); return; }
  var wide=window.matchMedia("(min-width:1180px)"), REF=0.35;
  var refs=[].slice.call(document.querySelectorAll(".bsp-ref[data-bsp]"));
  var cards=refs.map(function(r){ return document.getElementById("bsp-"+r.getAttribute("data-bsp")); });
  function isOn(){ return root.classList.contains("bsp-on"); }
  function paint(){ var v=isOn(); btn.classList.toggle("is-open",v); btn.setAttribute("aria-pressed",v?"true":"false"); }
  function set(v,remember){
    root.classList.toggle("bsp-on",v); paint();
    var sd=layout.querySelector(".side");                         // Overlay-Baum schließen; seine Knopffarbe folgt über wissen:layout
    if(sd && !window.matchMedia("(max-width:720px)").matches && sd.classList.contains("open")) sd.classList.remove("open");
    if(remember && wide.matches){ try{ localStorage.setItem("wissen-split",v?"1":"0"); }catch(e){} }
    try{ document.dispatchEvent(new Event("wissen:layout")); }catch(e){}   // Spaltenbreite geändert -> Formeln neu einpassen
    if(v) requestAnimationFrame(sync);
  }
  function anchorEl(r){ return r.previousElementSibling || r; }     // Formel/Aussage direkt vor dem Verweis
  function sync(){
    if(!isOn() || !wide.matches || !refs.length) return;
    var ref=window.innerHeight*REF, k=-1, A=[], P=[];
    for(var i=0;i<refs.length;i++){ A.push(anchorEl(refs[i]).getBoundingClientRect().top); P.push(cards[i].offsetTop); if(A[i]<=ref) k=i; }
    var p;                                                       // Stelle der Beispiel-Seite, die auf die Bezugslinie gehört
    if(k<0) p=P[0]-(A[0]-ref);
    else if(k===refs.length-1) p=P[k]+(ref-A[k]);
    else { var t=(ref-A[k])/Math.max(1,A[k+1]-A[k]); p=P[k]+t*(P[k+1]-P[k]); }
    pane.scrollTop=p-(ref-pane.getBoundingClientRect().top);
  }
  var tick=false;
  function later(){ if(tick) return; tick=true; requestAnimationFrame(function(){ tick=false; sync(); }); }
  window.addEventListener("scroll",later,{passive:true});
  window.addEventListener("resize",later);
  window.addEventListener("load",later);                          // nach Schriften/KaTeX noch einmal ausrichten
  document.addEventListener("toggle",later,true);                 // Herleitung auf-/zugeklappt -> Höhen ändern sich
  document.addEventListener("wissen:fitted",later);               // Formeln eingepasst -> Höhen ändern sich
  function flash(c){ if(!c) return; c.classList.remove("flash"); void c.offsetWidth; c.classList.add("flash");
    setTimeout(function(){ c.classList.remove("flash"); },1600); }
  function toAnchor(i){                                          // Artikel so scrollen, dass die Formel auf der Bezugslinie steht
    var y=window.scrollY+anchorEl(refs[i]).getBoundingClientRect().top-window.innerHeight*REF;
    window.scrollTo({top:Math.max(0,y),behavior:"smooth"});
  }
  refs.forEach(function(r,i){ var a=r.querySelector("a"); if(!a) return;
    a.addEventListener("click",function(e){ e.preventDefault(); if(!isOn()) set(true,true);
      requestAnimationFrame(function(){ if(wide.matches){ toAnchor(i); sync(); } else { pane.scrollTop=cards[i].offsetTop-12; } flash(cards[i]); });
    }); });
  [].slice.call(pane.querySelectorAll(".bsp-back")).forEach(function(a){
    a.addEventListener("click",function(e){ e.preventDefault();
      var i=refs.indexOf(document.getElementById("bspref-"+a.getAttribute("data-bsp"))); if(i<0) return;
      if(!wide.matches) set(false,false);
      requestAnimationFrame(function(){ toAnchor(i); });
    }); });
  btn.addEventListener("click",function(){ set(!isOn(),true); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape" && isOn() && !wide.matches) set(false,false); });
  (wide.addEventListener?wide.addEventListener.bind(wide,"change"):wide.addListener.bind(wide))(function(e){
    if(!e.matches){ set(false,false); }
    else { var st=false; try{ st=localStorage.getItem("wissen-split")==="1"; }catch(x){} set(st,false); }
  });
  paint(); if(isOn()) requestAnimationFrame(sync);
})();
// KaTeX automatisch rendern; zu breite abgesetzte Formeln danach passend verkleinern (höchstens auf 70 %),
// statt sie abzuschneiden – wichtig in der geteilten Ansicht und auf dem Handy.
(function(){
  function fitMath(){
    var ds=[].slice.call(document.querySelectorAll(".katex-display"));
    ds.forEach(function(d){ d.style.fontSize=""; });
    for(var pass=0;pass<2;pass++){                               // zweiter Durchgang: Skalierung ist nicht ganz linear
      var m=ds.map(function(d){ return [d.clientWidth,d.scrollWidth,parseFloat(getComputedStyle(d).fontSize)]; });
      ds.forEach(function(d,i){ var w=m[i][0],s=m[i][1];          // w=0: eingeklappte Herleitung -> beim Aufklappen
        if(w && s>w+1) d.style.fontSize=(m[i][2]*Math.max(0.7,w/s))+"px"; });
    }
    try{ document.dispatchEvent(new Event("wissen:fitted")); }catch(e){}   // Höhen haben sich geändert -> Beispiele neu ausrichten
  }
  var t=null; function later(){ clearTimeout(t); t=setTimeout(fitMath,120); }
  window.addEventListener("DOMContentLoaded",function(){
    if(window.renderMathInElement) renderMathInElement(document.body,{delimiters:[
      {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}]});
    fitMath();
  });
  window.addEventListener("resize",later);
  window.addEventListener("load",fitMath);
  document.addEventListener("toggle",later,true);                  // Herleitung aufgeklappt -> Formeln darin einpassen
  document.addEventListener("wissen:layout",later);               // geteilte Ansicht an/aus
})();
/* Fassung (kompakt | ausführlich) und Autor (KI | Mensch): Wahl merken; Themen-Links (Baum, Nachbarn, Übersicht)
   führen dann zur gewählten Fassung desselben Themas, soweit es sie gibt (data-alt, data-mensch, data-mensch-alt). */
(function(){
  function get(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function set(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  document.addEventListener("click",function(ev){
    var f=ev.target.closest&&ev.target.closest(".fassung .f-btn");
    if(f) set("wissen-fassung",f.getAttribute("data-fassung"));
    var b=ev.target.closest&&ev.target.closest(".autor .a-btn[data-autor]");
    if(b){ set("wissen-autor",b.getAttribute("data-autor")); if(b.tagName==="BUTTON"){ paint(); apply(); } }   // Übersicht: nur umschalten
  });
  function paint(){ var p=get("wissen-autor")||"ki";                 // Knöpfe der Übersicht zeigen die gemerkte Wahl
    document.querySelectorAll(".autor button.a-btn[data-autor]").forEach(function(b){ b.classList.toggle("on",b.getAttribute("data-autor")===p); }); }
  function apply(){
    var m=get("wissen-autor")==="mensch", f=get("wissen-fassung")==="ausfuehrlich";
    document.querySelectorAll("a[data-alt],a[data-mensch]").forEach(function(a){
      var h=a.getAttribute("data-href0"); if(!h){ h=a.getAttribute("href"); a.setAttribute("data-href0",h); }
      if(m&&a.getAttribute("data-mensch")) h=(f&&a.getAttribute("data-mensch-alt"))||a.getAttribute("data-mensch");
      else if(f&&a.getAttribute("data-alt")) h=a.getAttribute("data-alt");
      a.setAttribute("href",h);
    });
  }
  function init(){ paint(); apply(); }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init); else init();
})();
"""

if __name__ == "__main__":
    main()
