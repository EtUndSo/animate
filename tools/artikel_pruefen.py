"""Prüft gebaute Artikel im Browser: KaTeX-Fehler, tote Anker, zu breite Formeln, Reste aus den PDF-Heften.

    python tools/artikel_pruefen.py [Pfadteil ...]     z. B. signale-und-systeme   (Standard: alle Artikel)
Der Vorschau-Server muss auf localhost:8000 laufen.
"""
import asyncio
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "web" / "wissen"
sys.stdout.reconfigure(encoding="utf-8")
REST = re.compile(r"@@|\bHeft|cuaderno|workbook|本册|Lösungen am Ende|solutions at the end|soluciones al final|解答附在")

JS = r"""() => {
  const R = {};
  R.err = [...document.querySelectorAll('.katex-error')].slice(0, 6).map(e => (e.title || '').slice(0, 140) + ' :: ' + e.textContent.slice(0, 100));
  R.math = document.querySelectorAll('.katex').length;
  const body = document.querySelector('main.article article');
  const w0 = document.createTreeWalker(body, NodeFilter.SHOW_TEXT); let n0; R.roh = [];
  while (n0 = w0.nextNode()) { if (/\$|\\[a-zA-Z]+[{ ]/.test(n0.textContent) && !n0.parentElement.closest('.katex,code,pre')) R.roh.push(n0.textContent.slice(0, 120)); }
  R.dead = [...new Set([...document.querySelectorAll('article a[href^="#"]')].map(a => a.getAttribute('href').slice(1)))].filter(i => !document.getElementById(decodeURIComponent(i)));
  document.querySelectorAll('details').forEach(d => d.open = true);
  const sec = document.querySelector('section.sect');
  const w = sec ? sec.clientWidth : 600;
  R.wide = [...document.querySelectorAll('.katex-display')].filter(d => d.scrollWidth > d.clientWidth + 2).length;
  R.over = [...document.querySelectorAll('.katex-display')].filter(d => d.scrollWidth > d.clientWidth + 2).slice(0, 3).map(d => d.textContent.slice(0, 60));
  R.text = body ? body.innerText : '';
  return R;
}"""


async def main(teile):
    from playwright.async_api import async_playwright
    pages = sorted(p for p in OUT.rglob("*.html") if "_farbtest" not in p.parts and p.name != "index.html")
    if teile:
        pages = [p for p in pages if any(t in p.as_posix() for t in teile)]
    bad = 0
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1280, "height": 900})
        for p in pages:
            url = "http://localhost:8000/wissen/" + p.relative_to(OUT).as_posix()
            await pg.goto(url, wait_until="load")
            await pg.wait_for_timeout(900)
            r = await pg.evaluate(JS)
            rest = sorted(set(m.group(0) for m in REST.finditer(r["text"])))
            msgs = []
            if r["err"]:
                msgs.append("KaTeX: " + " || ".join(r["err"]))
            if r["roh"]:
                msgs.append(f"{len(r['roh'])} ungesetzte Formeln: " + " | ".join(r["roh"][:3]))
            if r["dead"]:
                msgs.append("tote Anker: " + ", ".join(r["dead"][:8]))
            if r["wide"]:
                msgs.append(f"{r['wide']} zu breite Formeln: " + " | ".join(r["over"]))
            if rest:
                msgs.append("Reste: " + ", ".join(rest))
            name = p.relative_to(OUT).as_posix()
            print(("⚠ " if msgs else "✓ ") + name + f" ({r['math']} Formeln)")
            for m in msgs:
                print("    " + m)
                bad += 1
        await b.close()
    print("Probleme:", bad)


asyncio.run(main(sys.argv[1:]))
