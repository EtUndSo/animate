import sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
J = """() => [...document.querySelectorAll('article .katex-display')].filter(d => !d.closest('details:not([open])') && d.scrollWidth > d.clientWidth + 1)
   .map(d => [d.scrollWidth, d.clientWidth, (d.querySelector('annotation') || {}).textContent.slice(0, 140)])"""
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, device_scale_factor=3)
    pg = ctx.new_page(); pg.goto(sys.argv[1], wait_until="networkidle"); pg.wait_for_timeout(900); pg.evaluate("() => document.querySelectorAll(\"details\").forEach(d => d.open = true)"); pg.wait_for_timeout(600)
    for row in pg.evaluate(J): print(row)
    b.close()
