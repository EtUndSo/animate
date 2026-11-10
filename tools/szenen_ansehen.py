"""Exportiert Szenen und baut daraus ein PNG-Kontaktblatt zum Ansehen (eine Sprache, weißer Grund, Spaltenbreite 548 px).

    python tools/szenen_ansehen.py out.png et3/k1elementar et3/k3kamm [--lang de] [--breite 600]
    python tools/szenen_ansehen.py out.png linux/k3cp linux/k3mv --ohne-export      nur ansehen, nichts exportieren

Der Export läuft mit --animiert (tools/export_szenen.py): .svg und .anim.svg entstehen zusammen, eine vorhandene
Animation veraltet also nicht. Szenen ohne Zeitachse bekommen wie immer keine .anim.svg.
--ohne-export: nimmt die fertigen Dateien aus web/abbildungen/<sprache>/ (z. B. nach einem Export aller Sprachen).
Das Blatt zeigt das statische Bild (= Endbild der Animation), so wie es im <img> der Seite und im PDF steht; der
Vorschau-Server ist nicht nötig. Für die Vektor-PDFs eines Hefts gibt es tools/kontaktblatt_pdf.py.
Meldet unaufgelöste @schlüssel im Bild; Warnungen des Exports (zu breit, verdeckter Text, Endbild weicht ab) stehen
in seiner Ausgabe.
"""
import argparse
import asyncio
import base64
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8")


async def shot(out, names, lang, breite):
    from playwright.async_api import async_playwright

    def src(n):
        f = ROOT / "web" / "abbildungen" / lang / (n + ".svg")
        return "data:image/svg+xml;base64," + base64.b64encode(f.read_bytes()).decode() if f.is_file() else ""
    rows = "".join(
        f'<figure style="margin:0 0 14px;width:{breite}px"><figcaption style="font:12px monospace;color:#888">{n} [{lang}]</figcaption>'
        f'<div style="max-width:548px;border:1px dashed #ccc"><img style="display:block;max-width:100%" src="{src(n)}" alt="fehlt"/></div></figure>'
        for n in names)
    html = f'<!doctype html><meta charset="utf-8"><body style="margin:8px;background:#fff;columns:{1 if len(names) < 4 else 2};width:{(breite + 16) * (1 if len(names) < 4 else 2)}px">{rows}</body>'
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": (breite + 24) * (1 if len(names) < 4 else 2), "height": 800})
        await pg.set_content(html)
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=out, full_page=True)
        await b.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("szenen", nargs="+")
    ap.add_argument("--lang", default="de")
    ap.add_argument("--breite", type=int, default=560)
    ap.add_argument("--ohne-export", action="store_true", help="nur die fertigen Bilder ansehen, nichts exportieren")
    a = ap.parse_args()
    if not a.ohne_export:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "export_szenen.py"), "--animiert", "--lang", a.lang] + a.szenen,
                           capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        print(r.stdout[-1500:], r.stderr[-1500:])
    for n in a.szenen:
        f = ROOT / "web" / "abbildungen" / a.lang / (n + ".svg")
        if not f.is_file():
            print(f"⚠ {n}: {f.relative_to(ROOT)} fehlt")
            continue
        svg = f.read_text(encoding="utf-8")
        for bad in sorted(set(re.findall(r">([^<]*@[\w.{}-]+[^<]*)<", svg))):
            print(f"⚠ {n}: unaufgelöster Text {bad!r}")
        anim = f.with_name(n.split("/")[-1] + ".anim.svg")
        if anim.is_file() and anim.stat().st_mtime < f.stat().st_mtime:
            print(f"⚠ {n}: .anim.svg ist älter als das Bild (mit --animiert neu exportieren)")
    asyncio.run(shot(a.out, a.szenen, a.lang, a.breite))
    print("→", a.out)


if __name__ == "__main__":
    main()
