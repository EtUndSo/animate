"""Lädt Wissensseiten und meldet KaTeX-Fehler (Konsole) sowie übrig gebliebene $$ im sichtbaren Text.
Aufruf: python -I katexcheck.py            -> alle Seiten
        python -I katexcheck.py <name>     -> nur Seiten, deren Dateiname <name> enthält (z. B. rechenregeln-div-rot)"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright  # noqa: E402

ROOT = pathlib.Path(r"C:\Users\info\PycharmProjects\pythonanimation\web")
flt = sys.argv[1] if len(sys.argv) > 1 else ""
pages = sorted(p for p in (ROOT / "wissen").rglob("*.html") if p.name != "index.html" and flt in p.name)
bad = 0
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    errs = []
    pg.on("console", lambda m: errs.append(m.text) if ("KaTeX" in m.text or "ParseError" in m.text) else None)
    for p in pages:
        errs.clear()
        url = "http://127.0.0.1:8000/" + p.relative_to(ROOT).as_posix()
        pg.goto(url, wait_until="networkidle")
        left = pg.evaluate("() => (document.querySelector('main').innerText.match(/[$][$]/g)||[]).length")
        if errs or left:
            bad += 1
            print("FEHLER", p.relative_to(ROOT).as_posix(), "| KaTeX:", len(errs), "| $$ übrig:", left)
            for e in errs[:3]:
                print("    ", e[:160])
    b.close()
print(f"{len(pages)} Seiten geprüft, {bad} mit Fehlern")
