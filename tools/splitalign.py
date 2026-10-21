"""Geteilte Ansicht (1600x1000): für jedes Beispiel k den Verweis anklicken und prüfen, ob Formel und Karte
auf der Bezugslinie stehen; zum Schluss Screenshot beim letzten Beispiel."""
import sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
U, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome"); ctx = b.new_context(viewport={"width": 1600, "height": 1000}); pg = ctx.new_page()
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(U, wait_until="networkidle"); pg.wait_for_timeout(500)
    pg.click("#toggleBsp"); pg.wait_for_timeout(500)
    n = pg.evaluate("document.querySelectorAll('.bsp-ref').length")
    for k in range(1, n + 1):
        pg.click(f"#bspref-{k} a"); pg.wait_for_timeout(1300)
        print(k, pg.evaluate("""k => { const r=document.getElementById('bspref-'+k); const a=r.previousElementSibling||r;
            const c=document.getElementById('bsp-'+k); return {anker:Math.round(a.getBoundingClientRect().top),
            karte:Math.round(c.getBoundingClientRect().top), ref:Math.round(window.innerHeight*0.35)}; }""", k))
    pg.screenshot(path=out)
    print("Fehler:", errs or "keine"); b.close()
