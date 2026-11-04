"""UI-Test der Operation Skalarprodukt im Editor (echter Browser, Pyodide, MathJax): anlegen, Zahlen eingeben,
abspielen, speichern und laden, Autosave, Szene-Link, SVG-/PNG-/Video-Export; dazu Σ und ∏ aus dem Menü,
Umbenennen eines Objekts und die einklappbaren Scene-Bereiche.

Aufruf: python tools/editor_skalarprodukt_test.py <ausgabeordner>
Voraussetzung: Vorschau-Server auf Port 8000 (web/), web/szenen/beispiel/skalarprodukt.json und ihr Artikelbild
web/abbildungen/de/beispiel/skalarprodukt.svg (python tools/szenen/beispiel_summen.py, dann tools/export_szenen.py)."""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
BASE = "http://localhost:8000/editor.html"
ok_all = True


def check(name, cond, extra=""):
    global ok_all
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)) if extra else ""))
    ok_all = ok_all and bool(cond)


def canvas_hash(pg):
    return hashlib.md5(pg.locator("#view").screenshot()).hexdigest()


def wait_ready(pg):
    pg.wait_for_function("document.getElementById('status') && /Ready|Szene geladen/.test(document.getElementById('status').textContent)", timeout=120000)
    pg.wait_for_timeout(1500)


def wait_formula(pg):
    """Until MathJax has set every piece: the KaTeX stand-in disappears and the engine draws the formula."""
    pg.wait_for_timeout(800)
    pg.wait_for_function("getComputedStyle(document.getElementById('sum-overlay')).display === 'none'", timeout=60000)
    pg.wait_for_function("/Ready/.test(document.getElementById('status').textContent)", timeout=60000)
    pg.wait_for_timeout(600)


def aufklappen(pg, sec):
    btn = pg.locator(f'.sub-toggle[data-sec="{sec}"]')
    if btn.get_attribute("aria-expanded") == "false":
        btn.click(); pg.wait_for_timeout(300)


def prop(pg, key):
    """The input of the operation property `key` (label text exactly key)."""
    return pg.locator("#comp-props .prop").filter(has=pg.locator("label", has_text=re.compile("^" + re.escape(key) + "$"))).locator("input").first


def set_prop(pg, key, value):
    inp = prop(pg, key)
    inp.fill(value); inp.press("Enter")


def op_rows(pg):
    return [t.strip() for t in pg.locator("#computations .obj-row .nm").all_text_contents()]


def add_operation(pg, label):
    grp = pg.locator("#comp-palette details", has=pg.locator("summary", has_text="Reihen"))
    if not grp.evaluate("d => d.open"):
        grp.locator("summary").click()
    grp.locator(".palette-item", has_text=label).click()


EMPTY = {"v": 1, "model": {"objects": [], "animations": [], "computations": [], "lang": "de"}}

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 1500, "height": 1100}, accept_downloads=True)
    # clear the autosave once per tab (sessionStorage survives a reload -> the autosave test below sees it)
    ctx.add_init_script('try{if(!sessionStorage.getItem("t")){localStorage.clear();sessionStorage.setItem("t","1");}'
                        'localStorage.setItem("animate-theme","light")}catch(e){}')
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(BASE, wait_until="domcontentloaded")
    wait_ready(pg)

    # 1. empty scene (load a file), then add the scalar product from the operations menu
    leer = OUT / "leer.json"; leer.write_text(json.dumps(EMPTY), encoding="utf-8")
    pg.set_input_files("#load-input", str(leer)); pg.wait_for_timeout(1500)
    aufklappen(pg, "comps")
    h_empty = canvas_hash(pg)
    add_operation(pg, "Skalarprodukt")
    wait_formula(pg)
    rows = op_rows(pg)
    check("Skalarprodukt im Menü 'Reihen' und in der Operationsliste", any(r.startswith("Skalarprodukt") for r in rows), rows)
    check("Standardzahlen ergeben eine vollständige Operation", not any("incomplete" in r for r in rows), rows)
    check("Rechnung wird gezeichnet (MathJax-Glyphen in der Engine)", canvas_hash(pg) != h_empty)
    pg.locator("#view").screenshot(path=str(OUT / "dot_standard.png"))

    # 2. typed-in numbers; lists of different length are refused and reported
    set_prop(pg, "u", "1, 2, 3"); set_prop(pg, "v", "4, -5, 6")
    wait_formula(pg)
    h1 = canvas_hash(pg)
    pg.locator("#view").screenshot(path=str(OUT / "dot_eingabe.png"))
    set_prop(pg, "v", "4, -5")
    pg.wait_for_timeout(1200)
    warn = pg.locator("#comp-props .hint").all_text_contents()
    check("Ungleich lange Listen: Warnung im Eigenschaftenfeld", any("gleich viele Zahlen" in w for w in warn), warn)
    check("Ungleich lange Listen: Operation als unvollständig markiert", any("incomplete" in r for r in op_rows(pg)), op_rows(pg))
    set_prop(pg, "v", "4, -5, 6")
    wait_formula(pg)
    check("Wieder gleich lang: vollständig, gleiches Bild wie vorher", not any("incomplete" in r for r in op_rows(pg)) and canvas_hash(pg) == h1)

    # 3. play: the step-by-step animation runs to the end (several different frames on the way)
    pg.click("#play-btn")
    seen = set()
    for _ in range(400):
        st = pg.locator("#status").text_content() or ""
        if st.startswith("Playing"):
            seen.add(canvas_hash(pg))
        if "Ended" in st:
            break
        pg.wait_for_timeout(150)
    st = pg.locator("#status").text_content() or ""
    check("Abspielen läuft bis zum Ende", "Ended" in st, st)
    check("Animation zeigt verschiedene Schritte", len(seen) >= 3, f"{len(seen)} verschiedene Bilder")
    pg.locator("#view").screenshot(path=str(OUT / "dot_ende.png"))
    pg.click("#reset-btn"); pg.wait_for_timeout(1500)

    # 4. Σ and ∏ from the same menu still render (all steps as rows in the edit view)
    for lab in ("Summation", "Product  (∏)"):
        add_operation(pg, lab)
        wait_formula(pg)
        st = pg.locator("#status").text_content() or ""
        check(f"{lab.strip()} aus dem Menü rendert ohne Fehler", st.startswith("Ready"), st)
    pg.locator("#view").screenshot(path=str(OUT / "dot_sum_prod.png"))
    for _ in range(2):                                       # remove Σ and ∏ again (last two rows)
        pg.locator("#computations .obj-row").last.locator("button.del").click(); pg.wait_for_timeout(500)
    wait_formula(pg)

    # 5. save -> file contains the operation; load it back (changed name) -> restored
    with pg.expect_download(timeout=30000) as dl:
        pg.click("#save-btn")
    saved = json.loads(Path(dl.value.path()).read_text(encoding="utf-8"))
    comps = saved["model"]["computations"]
    check("Speichern: DotProduct mit den eingegebenen Listen", len(comps) == 1 and comps[0]["type"] == "DotProduct"
          and comps[0]["props"]["u"] == "1, 2, 3" and comps[0]["props"]["v"] == "4, -5, 6", comps)
    comps[0]["props"]["u_name"] = "a"
    datei = OUT / "geladen.json"; datei.write_text(json.dumps(saved), encoding="utf-8")
    pg.evaluate("document.getElementById('status').textContent=''")
    pg.set_input_files("#load-input", str(datei)); pg.wait_for_timeout(1500)
    st = pg.locator("#status").text_content() or ""
    aufklappen(pg, "comps")
    pg.locator("#computations .obj-row").first.click(); pg.wait_for_timeout(500)
    check("Laden: ohne Fehler, Operation wieder da (und die einzige)", re.match(r"Scene loaded|Ready", st)
          and op_rows(pg) == ["Skalarprodukt  (uᵀv)"], f"{st} | {op_rows(pg)}")
    check("Laden: geänderter Vektorname kommt an", prop(pg, "u_name").input_value() == "a")
    wait_formula(pg)

    # 6. rename an object and fold the scene sections (must keep working next to the new operation)
    grp = pg.locator("#palette details", has=pg.locator("summary", has_text="Text & LaTeX"))
    grp.locator("summary").click(); grp.locator(".palette-item", has_text=re.compile("^Text$")).click()
    pg.wait_for_timeout(1200)
    aufklappen(pg, "objs")
    pg.locator("#scene-objs .obj-row[data-id]").first.dblclick()
    pg.wait_for_timeout(300)
    ren = pg.locator("#scene-objs input.rename")
    check("Doppelklick öffnet das Umbenennen-Feld", ren.count() == 1)
    if ren.count():
        ren.fill("Beschriftung"); ren.press("Enter"); pg.wait_for_timeout(500)
    check("Objekt umbenannt", pg.locator("#scene-objs .obj-row .nm", has_text="Beschriftung").count() == 1)
    btn = pg.locator('.sub-toggle[data-sec="comps"]')
    btn.click(); pg.wait_for_timeout(200)
    zu = btn.get_attribute("aria-expanded") == "false" and pg.locator("#computations").is_hidden()
    btn.click(); pg.wait_for_timeout(200)
    check("Operations-Bereich klappt zu und wieder auf", zu and btn.get_attribute("aria-expanded") == "true")
    check("Zähler der Operations-Überschrift", (pg.locator("#cnt-comps").text_content() or "") == "(1)")

    # 7. autosave: a reload restores the scene with the operation
    pg.reload(wait_until="domcontentloaded"); wait_ready(pg)
    aufklappen(pg, "comps")
    check("Autosave: nach dem Neuladen ist das Skalarprodukt wieder da", any(r.startswith("Skalarprodukt") for r in op_rows(pg)), op_rows(pg))

    # 8. scene link + exports (SVG like the batch export, PNG, video)
    pg2 = ctx.new_page()
    pg2.on("pageerror", lambda e: errors.append(str(e)))
    pg2.goto(BASE + "?scene=szenen/beispiel/skalarprodukt.json", wait_until="domcontentloaded")
    wait_ready(pg2)
    wait_formula(pg2)
    aufklappen(pg2, "comps")
    st = pg2.locator("#status").text_content() or ""
    check("Szene-Link lädt das Beispiel-Skalarprodukt", "Vorlage geladen" in st or any(r.startswith("Skalarprodukt") for r in op_rows(pg2)), st)
    pg2.locator("#view").screenshot(path=str(OUT / "dot_link.png"))
    pg2.click("#dl-png-caret")
    with pg2.expect_download(timeout=30000) as dl:
        pg2.locator("#dl-png-menu .export-item", has_text="SVG").click()
    svg = Path(dl.value.path()).read_text(encoding="utf-8")
    (OUT / "dot_editor.svg").write_text(svg, encoding="utf-8")
    batch = (ROOT / "web" / "abbildungen" / "de" / "beispiel" / "skalarprodukt.svg").read_text(encoding="utf-8")
    size = lambda s: re.match(r'<svg[^>]*width="(\d+)" height="(\d+)"', s).groups()
    check("SVG-Export: Formel als Pfade", svg.count("<path") >= 40, f"{svg.count('<path')} Pfade")
    check("SVG-Export im Editor = Artikelbild des Stapel-Exports (Größe, Pfade)",
          size(svg) == size(batch) and svg.count("<path") == batch.count("<path"),
          f"Editor {size(svg)} / {svg.count('<path')} Pfade, Stapel {size(batch)} / {batch.count('<path')} Pfade")
    pg2.click("#dl-png-caret")
    with pg2.expect_download(timeout=30000) as dl:
        pg2.locator("#dl-png-menu .export-item", has_text="PNG").click()
    png = Path(dl.value.path()).read_bytes()
    check("PNG-Export", png[:4] == b"\x89PNG" and len(png) > 5000, f"{len(png)} Bytes")
    with pg2.expect_download(timeout=120000) as dl:
        pg2.click("#dl-video")
    vid = Path(dl.value.path()).stat().st_size
    check("Video-Export liefert eine Datei", vid > 10000, f"{vid} Bytes, {dl.value.suggested_filename}")

    check("keine Seitenfehler (pageerror)", not errors, "; ".join(errors[:3]))
    b.close()
print("ALLE SKALARPRODUKT-TESTS OK" if ok_all else "SKALARPRODUKT-TESTS MIT FEHLERN")
sys.exit(0 if ok_all else 1)
