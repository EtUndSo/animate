"""UI-Test des Editors im echten Browser (Pyodide): Vorlagenmenü, Parameter-Regler, Panel-Auswahl,
SVG-Export, Szene per Link. Aufruf: editor_ui_test.py <ausgabeordner>
Voraussetzung: Vorschau-Server auf Port 8000 (python -m http.server 8000 --directory web) und
web/szenen/beispiel-emitterschaltung.json."""
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright  # noqa: E402

OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
BASE = "http://localhost:8000/editor.html"
ok_all = True


def check(name, cond, extra=""):
    global ok_all
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + extra) if extra else ""))
    ok_all = ok_all and bool(cond)


def canvas_hash(pg):
    return hashlib.md5(pg.locator("#view").screenshot()).hexdigest()


def wait_ready(pg):
    pg.wait_for_function("document.getElementById('status') && /Ready|Szene geladen/.test(document.getElementById('status').textContent)", timeout=120000)
    pg.wait_for_timeout(1500)


with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 1500, "height": 1100}, accept_downloads=True)
    ctx.add_init_script('try{localStorage.clear();localStorage.setItem("animate-theme","light")}catch(e){}')
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(BASE, wait_until="domcontentloaded")
    wait_ready(pg)

    # 1. every ET template loads and renders without an engine error
    names = pg.evaluate("Array.from(document.querySelectorAll('#templates optgroup')).filter(g=>g.label.startsWith('Elektrotechnik')).flatMap(g=>Array.from(g.children).map(o=>o.value))")
    check("ET-Vorlagen im Menü", len(names) == 7, str(names))
    hashes = set()
    for i, n in enumerate(names, 1):
        pg.select_option("#templates", n)
        pg.wait_for_timeout(2500)
        st = pg.locator("#status").text_content() or ""
        bad = st.startswith("⚠") or "error" in st.lower() or "Fehler" in st
        h = canvas_hash(pg)
        hashes.add(h)
        pg.locator("#view").screenshot(path=str(OUT / f"ui_tpl_{i}.png"))
        check(f"Vorlage lädt: {n}", not bad, st)
    check("Vorlagen sehen verschieden aus", len(hashes) == len(names))

    # 2. Parameter slider: load the characteristic-field template, move U_B, the picture changes
    pg.select_option("#templates", "Kennlinienfeld mit Arbeitspunkt")
    pg.wait_for_timeout(2500)
    h0 = canvas_hash(pg)
    row = pg.locator("#scene-objs .obj-row", has_text="UB = 5")
    check("Parameter in der Szenenliste (Name = Wert)", row.count() == 1)
    row.first.click()
    pg.wait_for_timeout(500)
    slider = pg.locator("#props input[type=range]")
    check("Schieberegler im Eigenschaftenfeld", slider.count() == 1)
    slider.first.evaluate("(el)=>{ el.value='3.5'; el.dispatchEvent(new Event('input',{bubbles:true})); el.dispatchEvent(new Event('change',{bubbles:true})); }")
    pg.wait_for_timeout(2500)
    h1 = canvas_hash(pg)
    check("Regler ändert das Bild (Arbeitspunkt wandert)", h1 != h0)
    pg.locator("#view").screenshot(path=str(OUT / "ui_param_UB35.png"))
    check("Szenenliste zeigt den neuen Wert", pg.locator("#scene-objs .obj-row", has_text="UB = 3.5").count() == 1)

    # 3. Panel choice: Bode template has 2 Axes -> a FunctionGraph shows the 'axes' dropdown; moving it changes the picture
    pg.select_option("#templates", "Bode-Diagramm Tiefpass")
    pg.wait_for_timeout(2500)
    h0 = canvas_hash(pg)
    fg_rows = pg.locator("#scene-objs .obj-row", has_text="FunctionGraph")
    fg_rows.first.click()
    pg.wait_for_timeout(500)
    sel = pg.locator("#props .prop", has_text="axes").locator("select")
    check("Panel-Auswahl 'axes' bei mehreren Achsensystemen", sel.count() == 1)
    if sel.count():
        opts = sel.first.evaluate("(s)=>Array.from(s.options).map(o=>o.value)")
        sel.first.select_option(opts[-1])
        pg.wait_for_timeout(2500)
        check("Kurve wechselt das Panel (Bild ändert sich)", canvas_hash(pg) != h0)

    # 4. SVG export: choose 'SVG (Vektor)' in the photo menu -> a download with an <svg> document
    pg.click("#dl-png-caret")
    with pg.expect_download(timeout=30000) as dl:
        pg.locator("#dl-png-menu .export-item", has_text="SVG").click()
    path = dl.value.path()
    svg = Path(path).read_text(encoding="utf-8")
    (OUT / "ui_export.svg").write_text(svg, encoding="utf-8")
    check("SVG-Export liefert ein SVG-Dokument", svg.startswith("<svg") and "<path" in svg and "<text" in svg,
          f"{len(svg)} Zeichen")

    # 5. scene link: ?scene=szenen/<file> loads that scene
    pg2 = ctx.new_page()
    pg2.on("pageerror", lambda e: errors.append(str(e)))
    pg2.goto(BASE + "?scene=szenen/beispiel-emitterschaltung.json", wait_until="domcontentloaded")
    wait_ready(pg2)
    st = pg2.locator("#status").text_content() or ""
    n_objs = pg2.locator("#scene-objs .obj-row").count()
    check("Szene per Link geladen", "Szene geladen" in st or n_objs > 5, f"{st} | {n_objs} Zeilen")
    pg2.locator("#view").screenshot(path=str(OUT / "ui_link.png"))

    check("keine Seitenfehler (pageerror)", not errors, "; ".join(errors[:3]))
    b.close()
print("ALLE UI-TESTS OK" if ok_all else "UI-TESTS MIT FEHLERN")
