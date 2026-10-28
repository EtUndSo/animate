"""Browser test for schematic editing (run: editor_schematic_test.py <out-dir>): auto panel + grid, placing with snap, rotate, wiring pin->pin,
rubber-band drag, black default colours, IEC/ANSI switch. Needs: python -m http.server 8000 --directory web"""
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8000/editor.html"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "schematic_test_out")
OUT.mkdir(exist_ok=True)
SEED = {"v": 1, "model": {"objects": [{"id": "t0", "type": "Text", "props": {"text": " ", "position": [6, 3.5, 0]}}],
                          "animations": [], "computations": [], "camera": {"mode": "2d", "zoom": 1, "theta": 0, "phi": 0}}}
ok = True
def check(name, cond, info=""):
    global ok
    ok &= bool(cond)
    print(("  OK   " if cond else "  FAIL ") + name + (f"  :: {info}" if info else ""))

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 1600, "height": 1000})
    ctx.add_init_script("try{ if(!sessionStorage.getItem('s')){ localStorage.setItem('animate.scene.v1', %s); sessionStorage.setItem('s','1'); } }catch(e){}" % json.dumps(json.dumps(SEED)))
    pg = ctx.new_page()
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(BASE, wait_until="domcontentloaded")
    pg.wait_for_function("document.getElementById('status') && /Ready/.test(document.getElementById('status').textContent)", timeout=120000)
    pg.wait_for_timeout(1500)
    box = pg.locator("#view").bounding_box()
    def page_xy(x, y):                       # data coords of the 1:1 schematic panel -> page pixels
        cx, cy = 960 + x * 135.0, 540 - y * 135.0
        return box["x"] + cx / 1920 * box["width"], box["y"] + cy / 1080 * box["height"]
    def model():
        return json.loads(pg.evaluate("localStorage.getItem('animate.scene.v1')"))["model"]
    labels = pg.evaluate("Array.from(document.querySelectorAll('#palette .palette-item')).map(s=>s.textContent)")
    def add(name):
        pg.evaluate("(i)=>document.querySelectorAll('#palette .palette-item')[i].click()", labels.index(name))
        pg.wait_for_timeout(1500)
    def wait_render():
        pg.wait_for_timeout(900)

    # 1. place a resistor at (-2, 1): moves with the cursor, snaps, click places
    add("Component")
    m = model()
    panels = [o for o in m["objects"] if o["type"] == "Axes" and o.get("schematic")]
    check("Schaltplanfeld automatisch angelegt", len(panels) == 1, panels[0]["props"].get("x_range") if panels else "")
    pg.mouse.move(*page_xy(-2.1, 1.12)); wait_render()
    pg.mouse.move(*page_xy(-1.93, 0.96)); wait_render()
    pg.mouse.click(*page_xy(-1.93, 0.96)); wait_render()
    r1 = [o for o in model()["objects"] if o["type"] == "Component"][-1]
    check("Bauteil rastet ein (Mitte -2|1)", r1["props"]["center"][:2] == [-2, 1], r1["props"]["center"])
    check("Bauteil auf dem Schaltplanfeld", r1.get("on") == panels[0]["id"])
    check("Standardfarbe schwarz", r1["props"]["color"] == "#000000", r1["props"]["color"])
    check("Mitte/Drehung/Länge statt Start/Ende", "start" not in r1["props"] and r1["props"]["length"] == 2)

    # 2. second resistor, rotated with R while placing, at (2, -1)
    add("Component")
    pg.mouse.move(*page_xy(2.04, -0.97)); wait_render()
    pg.keyboard.press("r"); wait_render()
    pg.mouse.click(*page_xy(2.04, -0.97)); wait_render()
    r2 = [o for o in model()["objects"] if o["type"] == "Component"][-1]
    check("R dreht beim Platzieren (90°)", r2["props"]["rotation"] == 90 and r2["props"]["center"][:2] == [2, -1], r2["props"])
    pg.locator("#view").screenshot(path=str(OUT / "1_zwei_widerstaende.png"))

    # 3. wire: drag from the right pin of R1 (-1|1) to the top pin of R2 (2|0)
    pg.mouse.move(*page_xy(-1.0, 1.0)); wait_render()
    pg.mouse.down(); pg.mouse.move(*page_xy(0.5, 0.9), steps=6); pg.mouse.move(*page_xy(2.02, 0.03), steps=8); wait_render()
    pg.locator("#view").screenshot(path=str(OUT / "2_leitung_vorschau.png"))
    pg.mouse.up(); wait_render(); wait_render()
    wires = [o for o in model()["objects"] if o["type"] == "Wire"]
    check("Leitung durch Ziehen von Pin zu Pin angelegt", len(wires) == 1, wires[0]["props"] if wires else "")
    if wires:
        check("Leitung rechtwinklig und an den Pins", wires[0]["props"]["points"] == "-1,1;2,0" and wires[0]["props"]["route"] == "hv", wires[0]["props"])
        check("Leitung schwarz", wires[0]["props"]["color"] == "#000000")
    pg.locator("#view").screenshot(path=str(OUT / "3_verdrahtet.png"))

    # 4. drag R2 by its body to (3, -1): the wire end follows
    pg.mouse.move(*page_xy(2.05, -1.0)); pg.mouse.down()
    pg.mouse.move(*page_xy(2.6, -1.0), steps=5); pg.mouse.move(*page_xy(3.04, -1.02), steps=5); wait_render()
    pg.mouse.up(); wait_render(); wait_render()
    m = model()
    r2 = [o for o in m["objects"] if o["id"] == r2["id"]][0]
    w = [o for o in m["objects"] if o["type"] == "Wire"][0]
    check("Bauteil am Körper verschoben (Raster)", r2["props"]["center"][:2] == [3, -1], r2["props"]["center"])
    check("Leitungsende folgt dem Pin", w["props"]["points"] == "-1,1;3,0", w["props"]["points"])

    # 5. T-junction: wire from R1's left pin (-3|1) down to the middle of nothing, then a wire ending on the first wire
    pg.mouse.move(*page_xy(-3.0, 1.0)); pg.mouse.down(); pg.mouse.move(*page_xy(-3.0, -1.0), steps=8); wait_render(); pg.mouse.up(); wait_render(); wait_render()
    pg.mouse.move(*page_xy(-3.0, -1.0)); pg.mouse.down(); pg.mouse.move(*page_xy(1.0, -1.0), steps=8); wait_render(); pg.mouse.up(); wait_render(); wait_render()
    pg.keyboard.down("Shift")                                 # Shift-drag: start in the middle of a wire
    pg.mouse.move(*page_xy(0.0, -1.0)); pg.mouse.down(); pg.mouse.move(*page_xy(0.0, 1.0), steps=8); wait_render(); pg.mouse.up(); wait_render(); wait_render()
    pg.keyboard.up("Shift")
    wires = [o for o in model()["objects"] if o["type"] == "Wire"]
    tj = [w for w in wires if w["props"]["points"] == "0,-1;0,1"]
    check("Umschalt-Ziehen beginnt eine Leitung mitten auf einer Leitung", len(tj) == 1, [w["props"]["points"] for w in wires])
    check("Lötpunkte an beiden T-Verbindungen", tj and tj[0]["props"]["dots"] == "0;1", tj[0]["props"] if tj else "")
    pg.locator("#view").screenshot(path=str(OUT / "3b_t_verbindung.png"))

    # 6. M mirrors (label side), style switch to ANSI
    pg.mouse.click(*page_xy(-2.0, 1.0)); wait_render()
    pg.keyboard.press("m"); wait_render()
    r1 = [o for o in model()["objects"] if o["id"] == r1["id"]][0]
    check("M spiegelt die Beschriftung", r1["props"]["label_flip"] is True)
    pg.evaluate("""()=>{ const s=[...document.querySelectorAll('#props select')].find(x=>[...x.options].some(o=>o.value==='amerikanisch')); if(s){ s.value='amerikanisch'; s.dispatchEvent(new Event('change')); } }""")
    wait_render(); wait_render()
    r1 = [o for o in model()["objects"] if o["id"] == r1["id"]][0]
    check("Darstellung pro Element umschaltbar", r1["props"]["symbol_style"] == "amerikanisch")
    pg.mouse.click(*page_xy(6.5, -3.5)); wait_render()      # deselect for a clean picture
    pg.locator("#view").screenshot(path=str(OUT / "4_fertig.png"))
    pg.keyboard.press("g"); wait_render()
    pg.locator("#view").screenshot(path=str(OUT / "5_ohne_raster.png"))
    check("keine Seitenfehler", not errs, "; ".join(errs)[:300])
    b.close()
print("SCHALTPLAN-PROBE OK" if ok else "SCHALTPLAN-PROBE FEHLER")
