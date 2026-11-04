"""Article block :::abbildung <szene> in build_wissen.py (package P1).
Run from web/:  python tests/test_abbildung.py
Checks the HTML (exported SVG at its size, numbered caption, alt text, editor link), the fallbacks, that
:::grafik still works, and that the editor's scene-link rule accepts exactly the names the build accepts."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
import build_wissen as bw  # noqa: E402

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)[:300]) if extra != "" and not cond else ""))
    ok = ok and bool(cond)


BODY = r"""## Abtastung

Text davor.

:::abbildung et3/demo
Spektrum bei $f_\mathrm{A} = 1$ kHz: **getrennt**
und ohne Überlappung.
:::

:::grafik
Szene: alt/platzhalter
Beschreibung der geplanten Abbildung.
:::

:::abbildung et3/demo
:::

:::abbildung et3/fehlt
Diese Szene ist noch nicht exportiert.
:::

:::abbildung ../geheim
Böser Name.
:::

:::abbildung et3/ohnejson
Ohne Szenendatei.
:::
"""

with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    (td / "abb" / "de" / "et3").mkdir(parents=True)
    (td / "szenen" / "et3").mkdir(parents=True)
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="412" height="233" viewBox="10 20 749.0909 423.6364">\n</svg>\n'
    (td / "abb" / "de" / "et3" / "demo.svg").write_text(svg, encoding="utf-8")
    (td / "abb" / "de" / "et3" / "ohnejson.svg").write_text(svg, encoding="utf-8")
    (td / "szenen" / "et3" / "demo.json").write_text("{}", encoding="utf-8")
    old = bw.ABB_DIR, bw.SZENEN
    bw.ABB_DIR, bw.SZENEN = td / "abb", td / "szenen"
    try:
        bw.ABB_N[0] = 0
        out, toc = bw.md_to_html(BODY)
    finally:
        bw.ABB_DIR, bw.SZENEN = old

figs = re.findall(r'<figure class="abb" id="abb-(\d+)">(.*?)</figure>', out, flags=re.S)
check("two real figures (abb-1, abb-2) and one without link (abb-5); :::grafik takes no number",
      [k for k, _ in figs] == ["1", "2", "5"], [k for k, _ in figs])
f1 = figs[0][1] if figs else ""
check("img: exported SVG of the article language at its own size",
      '<img src="/abbildungen/de/et3/demo.svg" width="412" height="233"' in f1, f1)
check("img: lazy loading", 'loading="lazy"' in f1 and 'decoding="async"' in f1)
alt = re.search(r'alt="([^"]*)"', f1)
check("alt text = caption without markup (f_\\mathrm{A} -> f A)",
      alt and alt.group(1) == "Spektrum bei f A = 1 kHz: getrennt und ohne Überlappung.", alt and alt.group(1))
check("caption numbered per article, inline markdown + math kept for KaTeX",
      '<figcaption><span class="abb-n">Abbildung 1</span> Spektrum bei $' in f1 and "<strong>getrennt</strong>" in f1, f1)
# Der Editor-Knopf steht unter dem Bild (div.abb-knopf) mit Stift-Symbol und dem Text „Szene im Editor öffnen“
check("editor button under the image, scene name only",
      '<div class="abb-knopf"><a class="abb-edit" href="/editor.html?scene=szenen/et3/demo.json" target="_blank" rel="noopener"' in f1
      and ">Szene im Editor öffnen</a></div>" in f1, f1)
f2 = figs[1][1] if len(figs) > 1 else ""
check("empty caption: number only, alt 'Abbildung 2'", 'alt="Abbildung 2"' in f2 and '<span class="abb-n">Abbildung 2</span></figcaption>' in f2, f2)
f6 = figs[2][1] if len(figs) > 2 else ""
check("scene file missing -> figure without editor link", "abb-edit" not in f6 and "ohnejson.svg" in f6)
check(":::grafik placeholder unchanged", '<div class="callout-h">Abbildung in Vorbereitung</div>' in out
      and "Editor-Szene: alt/platzhalter" in out)
ph = dict(re.findall(r'<aside class="callout cx-grafik" data-szene="([^"]*)"[^>]*><div class="callout-h">([^<]*)</div>', out))
check("missing SVG -> placeholder, its number 3 stays reserved", ph.get("et3/fehlt") == "Abbildung 3 in Vorbereitung", ph)
check("invalid name -> placeholder 4, never an <img> or link for it",
      ph.get("../geheim") == "Abbildung 4 in Vorbereitung" and "geheim.svg" not in out and "szenen/../" not in out, ph)
check("figures sit inside the section card", out.index('<section class="sect">') < out.index('<figure class="abb"') < out.rindex("</section>"))
check("reading time ignores figure captions", bw.lesezeit(":::abbildung x\n" + "wort " * 400 + "\n:::\n") == 1)
check("CSS for figure.abb is in the stylesheet", ".article figure.abb{" in bw.WISSEN_CSS and ".article figure.abb .abb-edit{" in bw.WISSEN_CSS)

# The editor accepts editor.html?scene=szenen/<name>.json exactly for the names the build accepts.
node = shutil.which("node")
if node:
    names = ["demo", "et3/k1-bode", "a_b/C-9", "x", "../x", "et3/../x", "et3//x", "/abs", "a.b", "a b", "a%2e", "", "ä", "et3/"]
    js = ("const fs=require('fs');const s=fs.readFileSync(process.argv[1],'utf8');"
          "const m=/const SCENE_LINK_RE = (\\/.*\\/);/.exec(s);const re=eval(m[1]);"
          "process.stdout.write(JSON.stringify(JSON.parse(process.argv[2]).map(n=>re.test('szenen/'+n+'.json'))));")
    r = subprocess.run([node, "-e", js, str(REPO / "web" / "editor.js"), json.dumps(names)], capture_output=True, text=True)
    editor = json.loads(r.stdout) if r.returncode == 0 else None
    build = [bool(bw.SZENE_NAME_RE.fullmatch(n)) for n in names]
    check("editor SCENE_LINK_RE == build SZENE_NAME_RE on 14 names", editor == build, (editor, build, r.stderr[-200:]))
else:
    print("  (node fehlt: Abgleich der Link-Regel übersprungen)")

print("ABBILDUNG TESTS PASSED" if ok else "ABBILDUNG TESTS FAILED")
sys.exit(0 if ok else 1)
