"""Exportierte Artikelbilder (SVG) als PDF für die Prüf-PDFs der Hefte: So steht in LaTeX und auf der Website dieselbe Abbildung.

    python tools/szenen_pdf.py et1 "C:/Bücher/ET1/Arbeitshefte"            alle Szenen web/abbildungen/<lang>/et1/*.svg
    python tools/szenen_pdf.py et1 "C:/Bücher/ET1/Arbeitshefte" k3teiler   nur diese

Ziel: <heftordner>/abb/<lang>/<name>.pdf (Vektor-PDF aus Chromium), eingebunden mit \\szene{name} oder als nummerierte
Abbildung mit \\szenenabb{name}{Bildunterschrift}{label} aus der Präambel. Eine Szene mit Zeitachse zeigt hier ihr
Endbild (export_szenen.py schreibt es als <name>.svg); die animierte Fassung <name>.anim.svg bleibt der Website.
Der Vorschau-Server ist nicht nötig, das SVG wird direkt in die Seite geschrieben.
"""
import asyncio
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8")
LANGS = ("de", "en", "es", "zh", "fr", "tr")


async def main(modul, ziel, namen):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        n = 0
        for lang in LANGS:
            src = ROOT / "web" / "abbildungen" / lang / modul
            if not src.is_dir():
                continue
            out = Path(ziel) / "abb" / lang
            out.mkdir(parents=True, exist_ok=True)
            for f in sorted(src.glob("*.svg")):
                if f.name.endswith(".anim.svg"):          # animierte Fassung: im PDF steht das Endbild (<szene>.svg)
                    continue
                if namen and f.stem not in namen:
                    continue
                svg = f.read_text(encoding="utf-8")
                m = re.search(r'<svg\b[^>]*?\swidth="([\d.]+)"[^>]*?\sheight="([\d.]+)"', svg)
                w, h = float(m.group(1)), float(m.group(2))
                await pg.set_content(f'<!doctype html><html><body style="margin:0">{svg}</body></html>')
                await pg.pdf(path=str(out / (f.stem + ".pdf")), width=f"{w + 1}px", height=f"{h + 1}px", print_background=True, page_ranges="1")
                n += 1
        await b.close()
    print(n, "PDF-Abbildungen")


asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3:]))
