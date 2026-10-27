"""Rendert eine Editor-Szene im echten Browser (Pyodide) und fotografiert die Zeichenfläche.
Aufruf: editor_shot.py <szene.json> <ausgabe.png> [dark]
Voraussetzung: Vorschau-Server, z. B. python -m http.server 8000 --directory web
Die Szene ist ein Editor-Modell {objects:[{id,type,props}], animations, computations, background, camera}
oder das Save-Format {v:1, model:{...}}."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright  # noqa: E402

SCENE, OUT = Path(sys.argv[1]), Path(sys.argv[2])
scheme = sys.argv[3] if len(sys.argv) > 3 else "light"
data = json.loads(SCENE.read_text(encoding="utf-8"))
if "model" not in data:
    data = {"v": 1, "model": data}
OUT.parent.mkdir(parents=True, exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 1600, "height": 1000}, color_scheme=scheme)
    ctx.add_init_script(
        'try{localStorage.setItem("animate-theme","%s");localStorage.setItem("animate.scene.v1",%s)}catch(e){}'
        % (scheme, json.dumps(json.dumps(data))))
    pg = ctx.new_page()
    errors = []
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto("http://localhost:8000/editor.html", wait_until="domcontentloaded")
    try:
        pg.wait_for_function("document.getElementById('status') && document.getElementById('status').textContent.startsWith('Ready')", timeout=90000)
        pg.wait_for_timeout(2500)
    except Exception as e:  # noqa: BLE001
        print("TIMEOUT:", type(e).__name__)
    status = pg.locator("#status").text_content()
    pg.locator("#view").screenshot(path=str(OUT))
    print("status:", status)
    for e in errors[:10]:
        print("console:", e[-1500:])
    b.close()
print("ok", OUT)
