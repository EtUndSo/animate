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
"""
import json, re, html, unicodedata
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
def _protect(m):
    _PROTECT.append(m.group(0)); return f"\x00{len(_PROTECT)-1}\x00"

def inline(text):
    """Inline markdown -> HTML. Math ($…$, $$…$$) and `code` are protected from other rules."""
    _PROTECT.clear()
    text = re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$|`[^`]+?`", _protect, text, flags=re.S)
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    def restore(m):
        raw = _PROTECT[int(m.group(1))]
        if raw.startswith("`"):
            return "<code>" + html.escape(raw[1:-1], quote=False) + "</code>"
        return raw                                    # math: hand to KaTeX verbatim
    return re.sub(r"\x00(\d+)\x00", restore, text)

CALLOUTS = {"konzept": ("💡", "Konzept"), "kern": ("🎯", "Das Wichtigste"), "merke": ("📌", "Merke")}

def md_to_html(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, toc, i, n = [], [], 0, len(lines)
    para = []
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para).strip()) + "</p>")
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
        m = re.match(r":::(\w+)\s*$", s)              # callout block  :::konzept ... :::
        if m:
            flush(); kind = m.group(1).lower(); i += 1; inner = []
            while i < n and lines[i].strip() != ":::":
                inner.append(lines[i]); i += 1
            i += 1
            icon, label = CALLOUTS.get(kind, ("", kind.title()))
            out.append(f'<aside class="callout cx-{kind}"><div class="callout-h">{icon} {html.escape(label)}</div>'
                       + md_to_html("\n".join(inner))[0] + "</aside>")
            continue
        if re.match(r"(---|\*\*\*|___)\s*$", s):      # horizontal rule
            flush(); out.append("<hr/>"); i += 1; continue
        hm = re.match(r"(#{1,4})\s+(.*)$", s)         # heading
        if hm:
            flush(); lvl = len(hm.group(1)); txt = hm.group(2).strip()
            hid = slugify(txt)
            if lvl == 2:
                toc.append((hid, txt))
            out.append(f'<h{lvl} id="{hid}">{inline(txt)}</h{lvl}>')
            i += 1; continue
        if s.startswith(">"):                         # blockquote
            flush(); quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>" + md_to_html("\n".join(quote))[0] + "</blockquote>")
            continue
        if re.match(r"[-*]\s+", s) or re.match(r"\d+\.\s+", s):   # list (ul/ol)
            flush(); ordered = bool(re.match(r"\d+\.\s+", s)); items = []
            while i < n and (re.match(r"[-*]\s+", lines[i].strip()) or re.match(r"\d+\.\s+", lines[i].strip())):
                items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", lines[i].strip())); i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it)}</li>" for it in items) + f"</{tag}>")
            continue
        if s.startswith("<"):                         # raw HTML / SVG / editor embed -> passthrough
            flush(); out.append(ln); i += 1; continue
        para.append(s); i += 1                         # ordinary paragraph line
    flush()
    return "\n".join(out), toc

# ---------------------------------------------------------- plain text (search) ----
def to_plain(md):
    txt = re.sub(r"```.*?```", " ", md, flags=re.S)
    txt = re.sub(r"\$\$?.+?\$\$?", " ", txt, flags=re.S)        # drop math
    txt = re.sub(r"[#>*`_:\-\[\]()!]", " ", txt)
    txt = re.sub(r"https?://\S+", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()

# ---------------------------------------------------------- build the tree ----
def collect():
    fields = {}
    for md_file in sorted(SRC.rglob("*.md")):
        rel = md_file.relative_to(SRC)
        if len(rel.parts) < 3:                        # need fach/thema/file
            print("  übersprungen (zu flach):", rel); continue
        meta, body = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        fach = meta.get("fach") or rel.parts[0]
        thema = meta.get("thema") or rel.parts[1]
        title = meta.get("title") or md_file.stem
        order = int(meta.get("order") or re.match(r"(\d+)", md_file.stem).group(1) if re.match(r"\d+", md_file.stem) else 999)
        f_slug, t_slug = slugify(fach), slugify(thema)
        a_slug = re.sub(r"^\d+-", "", md_file.stem) or slugify(title)
        path = f"{f_slug}/{t_slug}/{a_slug}.html"
        art = {"title": title, "fach": fach, "thema": thema, "slug": a_slug, "order": order,
               "path": path, "summary": meta.get("summary", ""), "tags": meta.get("tags", ""),
               "body": body, "f_slug": f_slug, "t_slug": t_slug}
        fields.setdefault(f_slug, {"name": fach, "slug": f_slug, "order": 10**9, "themen": {}})
        th = fields[f_slug]["themen"].setdefault(t_slug, {"name": thema, "slug": t_slug, "order": 10**9, "articles": []})
        th["articles"].append(art); th["order"] = min(th["order"], order)
        fields[f_slug]["order"] = min(fields[f_slug]["order"], order)
    # sort
    tree = []
    for f in sorted(fields.values(), key=lambda x: (x["order"], x["name"])):
        themen = []
        for t in sorted(f["themen"].values(), key=lambda x: (x["order"], x["name"])):
            t["articles"].sort(key=lambda a: (a["order"], a["title"]))
            themen.append(t)
        f["themen"] = themen; tree.append(f)
    return tree

# ------------------------------------------------------------------ render ----
def sidebar_html(tree, active_path=None):
    rows = ['<nav class="side" aria-label="Wissensbaum"><a class="side-home" href="/wissen/">Alle Fächer</a>']
    for f in tree:
        rows.append(f'<details class="fach" open><summary>{html.escape(f["name"])}</summary>')
        for t in f["themen"]:
            rows.append(f'<details class="thema" open><summary>{html.escape(t["name"])}</summary><ul>')
            for a in t["articles"]:
                cls = ' class="active"' if a["path"] == active_path else ""
                rows.append(f'<li><a{cls} href="/wissen/{a["path"]}">{html.escape(a["title"])}</a></li>')
            rows.append("</ul></details>")
        rows.append("</details>")
    rows.append("</nav>")
    return "".join(rows)

def page_shell(title, desc, body, depth):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="de"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(title)} — EtUndSo</title>
<meta name="description" content="{html.escape(desc)}"/>
<script>try{{if(localStorage.getItem("animate-theme")==="dark")document.documentElement.setAttribute("data-theme","dark");}}catch(e){{}}</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css"/>
<link rel="stylesheet" href="/wissen/assets/wissen.css"/>
</head><body data-root="/wissen/">
{body}
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"></script>
<script src="/wissen/assets/wissen.js"></script>
</body></html>"""

def topbar():
    return ('<div class="topbar"><a class="brand" href="/">Et<span>UndSo</span></a>'
            '<button id="searchBtn" class="searchBtn" aria-label="Suche">🔎 Suchen <kbd>/</kbd></button>'
            '<a class="editorlink" href="/editor.html">Editor</a></div>'
            '<div id="searchOverlay" class="searchOverlay" hidden><div class="searchBox">'
            '<input id="searchInput" type="search" placeholder="Thema, Begriff, Formel …" autocomplete="off"/>'
            '<div id="searchResults" class="searchResults"></div>'
            '<div class="searchHint">Teilwörter erlaubt (z. B. „teiler" findet „Spannungsteiler"). '
            '<kbd>Esc</kbd> schließt.</div></div></div>')

def render_article(art, tree, prev_a, next_a):
    body_html, toc = md_to_html(art["body"])
    crumb = (f'<nav class="crumbs"><a href="/wissen/">Wissen</a> › '
             f'<a href="/wissen/{art["f_slug"]}/">{html.escape(art["fach"])}</a> › '
             f'<span>{html.escape(art["thema"])}</span></nav>')
    toc_html = ""
    if toc:
        toc_html = '<aside class="toc"><div class="toc-h">Auf dieser Seite</div><ul>' + \
            "".join(f'<li><a href="#{hid}">{html.escape(txt)}</a></li>' for hid, txt in toc) + "</ul></aside>"
    nav = '<div class="prevnext">'
    if prev_a: nav += f'<a class="pn prev" href="/wissen/{prev_a["path"]}"><span>← Zurück</span>{html.escape(prev_a["title"])}</a>'
    else: nav += "<span></span>"
    if next_a: nav += f'<a class="pn next" href="/wissen/{next_a["path"]}"><span>Weiter →</span>{html.escape(next_a["title"])}</a>'
    nav += "</div>"
    main = (f'<main class="article"><article>{crumb}<h1>{html.escape(art["title"])}</h1>'
            + (f'<p class="lede">{html.escape(art["summary"])}</p>' if art["summary"] else "")
            + body_html + nav + legal_footer() + "</article>" + toc_html + "</main>")
    body = topbar() + '<div class="layout">' + sidebar_html(tree, art["path"]) + main + "</div>"
    depth = 1 + art["path"].count("/")               # web/wissen/<f>/<t>/<a>.html
    return page_shell(art["title"], art["summary"] or art["title"], body, depth)

def legal_footer():
    return ('<footer class="wfoot">EtUndSo.de · <a href="/impressum.html">Impressum</a> · '
            '<a href="/datenschutz.html">Datenschutz</a></footer>')

def render_index(tree):
    cards = ['<main class="article"><article><h1>Wissen</h1>'
             '<p class="lede">Verständliche, animierte Erklärungen — von Grund auf und in kleinen Schritten. '
             'Wähle ein Fach oder nutze die Suche.</p>']
    if not tree:
        cards.append('<p class="empty">Hier entstehen nach und nach die Artikel.</p>')
    for f in tree:
        cards.append(f'<section class="field-block"><h2 id="{f["slug"]}">{html.escape(f["name"])}</h2><div class="field-grid">')
        for t in f["themen"]:
            links = "".join(f'<li><a href="/wissen/{a["path"]}">{html.escape(a["title"])}</a></li>' for a in t["articles"])
            cards.append(f'<div class="theme-card"><h3>{html.escape(t["name"])}</h3><ul>{links}</ul></div>')
        cards.append("</div></section>")
    cards.append(legal_footer() + "</article></main>")
    body = topbar() + '<div class="layout">' + sidebar_html(tree, None) + "".join(cards) + "</div>"
    return page_shell("Wissen", "Verständliche Erklärungen zu Elektrotechnik, Mathematik und mehr.", body, 1)

# --------------------------------------------------------------------- main ----
def main():
    tree = collect()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "data").mkdir(exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)

    flat = [a for f in tree for t in f["themen"] for a in t["articles"]]
    for idx, art in enumerate(flat):
        prev_a = flat[idx - 1] if idx > 0 else None
        nxt = flat[idx + 1] if idx + 1 < len(flat) else None
        dest = OUT / Path(art["path"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_article(art, tree, prev_a, nxt), encoding="utf-8")

    (OUT / "index.html").write_text(render_index(tree), encoding="utf-8")

    # navigation tree (без bodies) + search index
    def strip(a): return {k: a[k] for k in ("title", "slug", "path", "summary", "order")}
    tree_json = [{"name": f["name"], "slug": f["slug"],
                  "themen": [{"name": t["name"], "slug": t["slug"], "articles": [strip(a) for a in t["articles"]]}
                             for t in f["themen"]]} for f in tree]
    (OUT / "data" / "tree.json").write_text(json.dumps(tree_json, ensure_ascii=False), encoding="utf-8")

    search = []
    for a in flat:
        plain = to_plain(a["body"])
        search.append({"title": a["title"], "fach": a["fach"], "thema": a["thema"], "path": a["path"],
                       "summary": a["summary"], "tags": a["tags"],
                       # pre-folded fields for fast infix matching; 'text' kept (original) for snippets
                       "ft_title": fold(a["title"]), "ft_tags": fold(a["tags"]),
                       "ft_text": fold(a["summary"] + " " + plain), "text": plain})
    (OUT / "data" / "search.json").write_text(json.dumps(search, ensure_ascii=False), encoding="utf-8")

    (OUT / "assets" / "wissen.css").write_text(WISSEN_CSS, encoding="utf-8")
    (OUT / "assets" / "wissen.js").write_text(WISSEN_JS, encoding="utf-8")

    print(f"✓ {len(flat)} Artikel, {len(tree)} Fächer -> {OUT}")

# --------------------------------------------------------- shared CSS / JS ----
WISSEN_CSS = r"""
/* Palette „Signal & Ink" — Tag Standard, Nacht via data-theme=dark (folgt dem Editor-Theme). */
:root{ --bg:#f4f6fa; --panel:#ffffff; --ink:#10161f; --muted:#56617a; --border:#e0e5ee; --soft:#eef1f7;
  --accent:#2b6def; --accent2:#e5383b; --accent3:#ff9f1c; --radius:14px;
  --fdisp:"Segoe UI",system-ui,-apple-system,Roboto,sans-serif; --fbody:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --fmono:ui-monospace,"Cascadia Code",Consolas,monospace; }
:root[data-theme="dark"]{ --bg:#0d1017; --panel:#1a2130; --ink:#edf1f7; --muted:#99a4b8; --border:#27303f; --soft:#141a26;
  --accent:#5c94ff; --accent2:#ff5e60; --accent3:#ffb54d; }
*{box-sizing:border-box;} html{scroll-behavior:smooth;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--fbody);line-height:1.62;-webkit-font-smoothing:antialiased;}
a{color:var(--accent);text-decoration:none;} a:hover{text-decoration:underline;}
kbd{font-family:var(--fmono);font-size:.82em;background:var(--soft);border:1px solid var(--border);border-radius:5px;padding:1px 5px;}
.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:14px;padding:11px 18px;background:var(--panel);border-bottom:1px solid var(--border);}
.brand{font-family:var(--fdisp);font-weight:800;font-size:19px;letter-spacing:-.02em;color:var(--accent2);}
.brand span{color:var(--accent);}
.topbar .searchBtn{margin-left:auto;display:flex;align-items:center;gap:8px;background:var(--soft);border:1px solid var(--border);color:var(--muted);
  border-radius:10px;padding:8px 13px;font:inherit;font-size:14px;cursor:pointer;}
.topbar .searchBtn:hover{border-color:var(--accent);color:var(--ink);}
.topbar .editorlink{font-weight:600;color:var(--muted);} .topbar .editorlink:hover{color:var(--ink);}
.layout{display:grid;grid-template-columns:260px minmax(0,1fr);gap:0;max-width:1180px;margin:0 auto;}
.side{position:sticky;top:53px;align-self:start;max-height:calc(100vh - 53px);overflow:auto;padding:18px 10px 40px 18px;border-right:1px solid var(--border);font-size:14.5px;}
.side-home{display:block;font-weight:700;color:var(--ink);margin-bottom:10px;}
.side details{margin:2px 0;} .side summary{cursor:pointer;font-weight:600;padding:4px 6px;border-radius:7px;list-style:none;}
.side summary::-webkit-details-marker{display:none;}
.side summary::before{content:"▸";color:var(--muted);display:inline-block;width:1em;transition:transform .15s;}
.side details[open]>summary::before{transform:rotate(90deg);}
.side .thema{margin-left:12px;} .side .thema summary{font-weight:500;}
.side ul{list-style:none;margin:0 0 4px;padding-left:22px;} .side li{margin:1px 0;}
.side li a{display:block;color:var(--muted);padding:3px 7px;border-radius:7px;}
.side li a:hover{color:var(--ink);background:var(--soft);text-decoration:none;}
.side li a.active{color:#fff;background:var(--accent);font-weight:600;}
.article{min-width:0;padding:26px 30px 70px;display:grid;grid-template-columns:minmax(0,1fr) 210px;gap:34px;align-items:start;}
.article>article{min-width:0;max-width:72ch;}
.crumbs{font-size:13px;color:var(--muted);margin-bottom:10px;} .crumbs a{color:var(--muted);}
.article h1{font-family:var(--fdisp);font-size:clamp(26px,4vw,38px);line-height:1.1;letter-spacing:-.02em;margin:.1em 0 .3em;text-wrap:balance;}
.article h2{font-family:var(--fdisp);font-size:24px;margin:1.6em 0 .4em;letter-spacing:-.01em;scroll-margin-top:66px;}
.article h3{font-family:var(--fdisp);font-size:19px;margin:1.3em 0 .3em;scroll-margin-top:66px;}
.article p,.article li{font-size:16.5px;} .article .lede{font-size:18.5px;color:var(--muted);margin:.2em 0 1.1em;}
.article img{max-width:100%;border-radius:10px;} .article code{font-family:var(--fmono);font-size:.9em;background:var(--soft);padding:1px 5px;border-radius:5px;}
.article pre{background:var(--soft);border:1px solid var(--border);border-radius:10px;padding:14px 16px;overflow:auto;} .article pre code{background:none;padding:0;}
.article blockquote{margin:1em 0;padding:2px 16px;border-left:3px solid var(--accent);color:var(--muted);}
.callout{margin:1.2em 0;padding:14px 16px;border:1px solid var(--border);border-radius:12px;background:var(--soft);}
.callout-h{font-weight:700;font-family:var(--fdisp);margin-bottom:4px;}
.callout.cx-konzept{border-left:4px solid var(--accent);} .callout.cx-kern{border-left:4px solid var(--accent2);background:color-mix(in srgb,var(--accent2) 7%,var(--panel));}
.callout.cx-merke{border-left:4px solid var(--accent3);}
.prevnext{display:flex;justify-content:space-between;gap:14px;margin:36px 0 10px;flex-wrap:wrap;}
.pn{flex:1 1 200px;border:1px solid var(--border);border-radius:12px;padding:12px 15px;font-weight:600;background:var(--panel);}
.pn span{display:block;font-size:12px;color:var(--muted);font-weight:500;margin-bottom:2px;} .pn.next{text-align:right;}
.toc{position:sticky;top:66px;align-self:start;font-size:13.5px;border-left:1px solid var(--border);padding-left:16px;}
.toc-h{text-transform:uppercase;letter-spacing:.05em;font-size:11px;color:var(--muted);font-weight:700;margin-bottom:8px;}
.toc ul{list-style:none;margin:0;padding:0;} .toc li{margin:5px 0;} .toc a{color:var(--muted);} .toc a.active{color:var(--accent);font-weight:600;}
.field-block{margin:26px 0;} .field-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;}
.theme-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px;}
.theme-card h3{font-family:var(--fdisp);margin:0 0 6px;font-size:16px;} .theme-card ul{list-style:none;margin:0;padding:0;} .theme-card li{margin:4px 0;}
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
@media(max-width:920px){ .article{grid-template-columns:1fr;} .toc{display:none;} }
@media(max-width:720px){ .layout{grid-template-columns:1fr;} .side{display:none;border-right:none;} .side.open{display:block;position:fixed;inset:53px 0 0;z-index:30;background:var(--panel);max-height:none;}
  .menuBtn{display:inline-flex;}
}
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
      a.innerHTML='<div class="r-crumb">'+esc(d.fach)+' › '+esc(d.thema)+'</div>'+
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
// KaTeX automatisch rendern.
window.addEventListener("DOMContentLoaded",function(){
  if(window.renderMathInElement) renderMathInElement(document.body,{delimiters:[
    {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}]});
});
"""

if __name__ == "__main__":
    main()
