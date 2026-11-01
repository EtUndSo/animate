"""Article-figure export (package P1): crop, size, background, and the browser-free batch tool.
Run from web/:  python tests/test_export.py"""
import json
import math
import re
import sys
import tempfile
import xml.dom.minidom
from pathlib import Path

sys.path.insert(0, "."); sys.path.insert(0, "py")
TOOLS = Path(__file__).resolve().parents[2] / "tools"
sys.path.insert(0, str(TOOLS))
import numpy as np
from engine.scene_model import ModelScene
from engine.renderer import paint_scene
from engine import export as ex
from engine.svg_painter import SvgPainter

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)) if extra != "" and not cond else ""))
    ok = ok and bool(cond)


def build(objects, extra=None):
    model = {"objects": objects, "animations": [], "background": [1, 1, 1]}
    if extra:
        model.update(extra)
    sc = ModelScene(model); sc.construct(); sc.show_static()
    return sc


class Recorder:
    """Painter that records every visible path box and text box (to check the crop contains them)."""
    def __init__(self): self.boxes = []
    def background(self, c): pass
    def draw_path(self, pts, fc, fo, sc, sw, so, contours=None, dash=None):
        if fo > 0 or (sw > 0 and so > 0):
            a = np.asarray(pts, float).reshape(-1, 2); h = sw / 2 if sw > 0 and so > 0 else 0
            self.boxes.append(("path", a[:, 0].min() - h, a[:, 1].min() - h, a[:, 0].max() + h, a[:, 1].max() + h))
    def draw_text(self, text, px, py, fs, color, op, align="center"):
        b = ex.text_box(text, px, py, fs, align)
        if b and op > 0:
            self.boxes.append(("text " + text, *b))


# 1. text extents use the Arial/Helvetica advance widths and the SVG layout
b = ex.text_box("Hallo", 100, 50, 20, "center")
w = 20 * (722 + 556 + 222 + 222 + 556) / 1000.0
check("text_box: width of 'Hallo' from the Helvetica/Arial metrics", abs((b[2] - b[0]) - w) < 1e-9, b)
check("text_box: centred on the anchor, +-0.56 em high", abs((b[0] + b[2]) / 2 - 100) < 1e-9 and abs(b[1] - (50 - 11.2)) < 1e-9)
bl, br = ex.text_box("Hallo", 100, 50, 20, "left"), ex.text_box("Hallo", 100, 50, 20, "right")
check("text_box: left/right alignment", abs(bl[0] - 100) < 1e-9 and abs(br[2] - 100) < 1e-9)
r = ex.text_box("f_\\mathrm{A}", 0, 0, 30, "left")
check("text_box: subscript run is smaller and lower", abs(r[2] - 30 * (0.278 + 0.7 * 0.667)) < 1e-9 and r[3] > 0.56 * 30, r)
two = ex.text_box("a\\\\b", 0, 0, 20, "center")
check("text_box: two lines are 1.25 em apart", abs((two[3] - two[1]) - (1.25 * 20 + 2 * 0.56 * 20)) < 1e-9)
check("text_box: blank label draws nothing", ex.text_box("  ", 0, 0, 20) is None)

# 2. content crop: contains every visible path and label (+ margin), much smaller than the frame
AX = {"id": "ax", "type": "Axes", "args": {"x_range": [0, 4], "y_range": [-1.5, 1.5], "x_length": 5, "y_length": 3,
                                           "x_label": "t in s", "y_label": "f_\\mathrm{A}(t)", "x_axis_at": "bottom"}}
OBJS = [AX, {"id": "g", "type": "FunctionGraph", "args": {"func": "sin(2x)", "color": [0.8, 0.1, 0.1], "stroke_width": 4}},
        {"id": "t", "type": "Text", "args": {"text": "Eingang", "position": [3, 1.2, 0], "font_size": 26, "color": [0, 0, 0]}},
        {"id": "inv", "type": "Text", "args": {"text": " ", "position": [-5, 3.5, 0], "color": [0, 0, 0]}}]
sc = build(OBJS)
st = ex.settings(None)
check("settings: defaults content / margin 24 / scale 0.55", st == {"mode": "content", "margin": 24.0, "scale": 0.55, "frame": None}, st)
rect, size = ex.export_rect(sc.objectList, sc.camera, st)
rec = Recorder(); paint_scene(rec, sc.objectList, sc.camera, background=None)
inside = all(rect[0] <= bx0 and rect[1] <= by0 and bx1 <= rect[2] and by1 <= rect[3] for _, bx0, by0, bx1, by1 in rec.boxes)
check("content crop contains every drawn path and label", inside)
ub = [min(b[1] for b in rec.boxes), min(b[2] for b in rec.boxes), max(b[3] for b in rec.boxes), max(b[4] for b in rec.boxes)]
check("content crop = union box + 24 px margin (+ < 2 px rounding)",
      all(abs(d - 24) < 24 + 2 / 0.55 and d >= 24 - 1e-9 for d in (ub[0] - rect[0], ub[1] - rect[1], rect[2] - ub[2], rect[3] - ub[3])),
      (ub, rect))
check("blank text and empty space do not widen the crop", rect[0] > 400, rect)
check("displayed size = crop x 0.55 in whole pixels",
      size == (math.ceil((rect[2] - rect[0]) * 0.55 - 1e-9), math.ceil((rect[3] - rect[1]) * 0.55 - 1e-9))
      and abs((rect[2] - rect[0]) * 0.55 - size[0]) < 1e-6, (size, rect))
svg, info = ex.render(sc.objectList, sc.camera, background=[1, 1, 1], raw_settings=None)
try:
    xml.dom.minidom.parseString(svg.encode("utf-8")); okxml = True
except Exception as e:  # noqa: BLE001
    okxml = False; print("   XML:", e)
check("article SVG is well-formed XML", okxml)
m = re.match(r'<svg xmlns="http://www.w3.org/2000/svg" width="(\d+)" height="(\d+)" viewBox="([-\d. ]+)"', svg)
vb = [float(v) for v in m.group(3).split()] if m else []
check("SVG width/height = displayed size, viewBox = crop", m and (int(m.group(1)), int(m.group(2))) == size
      and np.allclose(vb, [rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]], atol=1e-3), (m and m.groups(), rect))
check("SVG uses the fixed Arial-compatible font", "font-family=\"Arial, Helvetica, 'Liberation Sans', 'Nimbus Sans', " in svg)
check("white background rectangle covers exactly the crop", re.search(r'<rect x="%s" y="%s" ' % (
    ("%.4f" % rect[0]).rstrip("0").rstrip("."), ("%.4f" % rect[1]).rstrip("0").rstrip(".")), svg) and 'fill="#ffffff"' in svg)
check("info: narrow figure -> 26 px text appears at 26 x 0.55 = 14.3 px", info["fits"] and abs(info["text_px"] - 14.3) < 1e-9, info)

# 3. canvas mode (old behaviour) and the text size of a too-wide figure
svg_c, info_c = ex.render(sc.objectList, sc.camera, raw_settings={"mode": "canvas"})
check("canvas mode: whole 1920x1080 frame at 0.55 -> 1056x594", (info_c["width"], info_c["height"]) == (1056, 594)
      and info_c["rect"] == [0.0, 0.0, 1920.0, 1080.0], info_c)
check("canvas mode: too wide for the column, text shrinks to 26*0.55*548/1056",
      not info_c["fits"] and abs(info_c["text_px"] - 26 * 0.55 * ex.COLUMN_PX / 1056) < 1e-9, info_c["text_px"])

# 4. frame mode: world units of the 2D view, also under camera zoom
_, info_f = ex.render(sc.objectList, sc.camera, raw_settings={"mode": "frame", "frame": [-2, -1, 2, 1]})
check("frame [-2,-1,2,1] -> 540x270 scene px -> 297x149 px", (info_f["width"], info_f["height"]) == (297, 149), info_f)
check("frame maps to the canvas around its centre", abs(info_f["rect"][0] - 690) < 1e-6 and abs(info_f["rect"][2] - 1230) < 1e-6
      and abs((info_f["rect"][1] + info_f["rect"][3]) / 2 - 540) < 1e-6, info_f["rect"])
check("info.frame gives the crop back in world units", np.allclose(info_f["frame"][0::2], [-2, 2], atol=1e-3), info_f["frame"])
scz = build(OBJS, {"camera": {"mode": "2d", "zoom": 2.0}})
_, info_z = ex.render(scz.objectList, scz.camera, raw_settings={"mode": "frame", "frame": [-2, -1, 2, 1]})
check("frame under zoom 2: the same world region, twice as many scene px", info_z["width"] == 594, info_z)
check("invalid settings fall back to defaults", ex.settings({"mode": "x", "margin": -3, "scale": "a", "frame": [1, 2]})
      == {"mode": "content", "margin": 24.0, "scale": 0.55, "frame": None})
check("degenerate frame falls back to the content crop", ex.settings({"mode": "frame", "frame": [1, 1, 1, 3]})["frame"] is None)

# 5. background: the editor's night grey is never exported, transparency is kept, custom colours too
check("night-mode grey #d4d7dc -> white", ex.article_background([212 / 255, 215 / 255, 220 / 255]) == (1.0, 1.0, 1.0))
check("transparent stays transparent", ex.article_background(None) is None)
check("custom colour is kept", ex.article_background([1.0, 0.9, 0.6]) == (1.0, 0.9, 0.6))
svg_t, _ = ex.render(sc.objectList, sc.camera, background=None)
check("transparent background -> no <rect>", "<rect" not in svg_t)

# 6. empty scene: nothing drawn -> whole frame
sce = build([])
_, info_e = ex.render(sce.objectList, sce.camera)
check("empty scene -> whole frame", info_e["rect"] == [0.0, 0.0, 1920.0, 1080.0])

# 7. old SvgPainter default call still gives the whole frame
sp = SvgPainter(1920, 1080); paint_scene(sp, sc.objectList, sc.camera, background=[1, 1, 1])
check("SvgPainter.to_svg() without arguments: 1920x1080, viewBox 0 0 1920 1080",
      sp.to_svg().startswith('<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">'))

# 8. batch tool: editor scene format -> engine model, like editor.js toPythonModel
import export_szenen as es  # noqa: E402
defaults, kinds = es.load_editor_tables()
check("batch: editor catalogue read through node", defaults is not None and "Legend" in defaults and kinds.get("Summation") == "summation",
      "node missing?" if defaults is None else "")
scene = {"v": 1, "model": {
    "objects": [{"id": "o1", "type": "Axes", "props": {"x_range": [0, 4], "y_range": [-1.5, 1.5], "x_length": 5, "y_length": 3}},
                {"id": "o2", "type": "FunctionGraph", "props": {"func": "sin(2x)", "color": "#ff0000", "y_range": [0, 1]}},
                {"id": "o3", "type": "Component", "props": {"kind": "resistor", "start": [0, 0, 0], "end": [0, 2, 0]}},
                {"id": "o4", "type": "Dot", "visible": False, "props": {"center": [1, 0, 0]}, "on": "o1"}],
    "animations": [{"id": "a1", "type": "Shift", "target": "o2", "run_time": 2, "vector": [1, 0, 0]},
                   {"id": "a2", "type": "FadeIn", "target": "o3", "visible": False},
                   {"id": "a3", "type": "Rotate", "target": "o2", "angle": 90}],
    "computations": [{"id": "c1", "type": "Summation", "props": {"sum_mode": "number", "term": "1/i^2"}}],
    "background": {"color": "#d4d7dc", "transparent": False, "axes_on_top": True},
    "playMode": "sequential", "angleUnit": "deg", "camera": {"mode": "2d", "zoom": 1.0},
    "export": {"mode": "frame", "frame": [-3, -2, 3, 2], "scale": 0.5}}}
notes = []
pm = es.python_model(json.loads(json.dumps(scene)), defaults, kinds, "de", notes)
o = {s["id"]: s for s in pm["objects"]}
check("batch: hex colours -> RGB (toArgs)", o["o2"]["args"]["color"] == [1.0, 0.0, 0.0])
check("batch: FunctionGraph y_range dropped, catalogue props backfilled (ensureDefaults)",
      "y_range" not in o["o2"]["args"] and o["o2"]["args"].get("stroke_width") == 4)
check("batch: start/end component -> centre/rotation/length (ensureDefaults)",
      o["o3"]["args"].get("center") == [0.0, 1.0, 0] and o["o3"]["args"].get("rotation") == 90 and o["o3"]["args"].get("length") == 2
      and "start" not in o["o3"]["args"], o["o3"]["args"])
check("batch: hidden object keeps visible:false and its panel", o["o4"].get("visible") is False and o["o4"].get("on") == "o1")
check("batch: hidden animation skipped, sequential steps, Shift vector, Rotate in radians",
      [a["type"] for a in pm["animations"]] == ["Shift", "Rotate"] and [a["step"] for a in pm["animations"]] == [0, 1]
      and pm["animations"][0]["args"] == {"vector": [1, 0, 0]} and abs(pm["animations"][1]["args"]["angle"] - math.pi / 2) < 1e-12)
check("batch: background, axes_on_top, angle unit, export, lang, no WebGL",
      np.allclose(pm["background"], [212 / 255, 215 / 255, 220 / 255]) and pm["axes_on_top"] is True and pm["angle_unit"] == "deg"
      and pm["export"]["mode"] == "frame" and pm["lang"] == "de" and pm["gl"] is False)
check("batch: Σ in number mode is reported (browser only)", any("Summation" in n for n in notes), notes)
with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    (td / "szenen" / "et3").mkdir(parents=True)
    (td / "szenen" / "et3" / "demo.json").write_text(json.dumps(scene), encoding="utf-8")
    old = es.SZENEN; es.SZENEN = td / "szenen"
    try:
        info_b, _ = es.export_scene("et3/demo", td / "out", "de", defaults, kinds)
        out = (td / "out" / "de" / "et3" / "demo.svg")
        check("batch: writes <out>/<lang>/<scene>.svg (subfolders kept)", out.is_file())
        txt = out.read_text(encoding="utf-8")
        check("batch: frame [-3,-2,3,2] at scale 0.5 -> 405x270 px, grey -> white",
              (info_b["width"], info_b["height"]) == (405, 270) and 'width="405" height="270"' in txt and 'fill="#ffffff"' in txt, info_b)
        check("batch: names are validated", es.main(["../x", "--out", str(td / "out")]) == 1)
    finally:
        es.SZENEN = old

print("EXPORT TESTS PASSED" if ok else "EXPORT TESTS FAILED")
sys.exit(0 if ok else 1)
