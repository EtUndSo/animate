"""Exportiert Szenen und baut daraus ein PNG-Kontaktblatt zum Ansehen (eine Sprache, weißer Grund, Spaltenbreite 548 px).

    python tools/szenen_ansehen.py out.png et3/k1elementar et3/k3kamm [--lang de] [--breite 600]

Meldet Text, der über andere Texte läuft, und Szenen, die breiter als die Spalte sind.
"""
import argparse
import asyncio
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8")


async def shot(out, names, lang, breite):
    from playwright.async_api import async_playwright
    rows = "".join(
        f'<figure style="margin:0 0 14px;width:{breite}px"><figcaption style="font:12px monospace;color:#888">{n} [{lang}]</figcaption>'
        f'<div style="max-width:548px;border:1px dashed #ccc"><img style="display:block;max-width:100%" src="/abbildungen/{lang}/{n}.svg"/></div></figure>'
        for n in names)
    html = f'<!doctype html><meta charset="utf-8"><body style="margin:8px;background:#fff;columns:{1 if len(names) < 4 else 2};width:{(breite + 16) * (1 if len(names) < 4 else 2)}px">{rows}</body>'
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": (breite + 24) * (1 if len(names) < 4 else 2), "height": 800})
        await pg.route("**/__blatt", lambda r: r.fulfill(status=200, content_type="text/html", body=html))
        await pg.goto("http://localhost:8000/__blatt")
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=out, full_page=True)
        await b.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("szenen", nargs="+")
    ap.add_argument("--lang", default="de")
    ap.add_argument("--breite", type=int, default=560)
    a = ap.parse_args()
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "export_szenen.py"), "--lang", a.lang] + a.szenen,
                       capture_output=True, text=True, encoding="utf-8", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    print(r.stdout[-1500:], r.stderr[-1500:])
    for n in a.szenen:
        svg = (ROOT / "web" / "abbildungen" / a.lang / (n + ".svg")).read_text(encoding="utf-8")
        for bad in sorted(set(re.findall(r">([^<]*@[\w.{}-]+[^<]*)<", svg))):
            print(f"⚠ {n}: unaufgelöster Text {bad!r}")
    asyncio.run(shot(a.out, a.szenen, a.lang, a.breite))
    print("→", a.out)


if __name__ == "__main__":
    main()
