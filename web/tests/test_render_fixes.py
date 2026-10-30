"""Rendering bugs that block article figures (package P3 of ABBILDUNGEN_INVENTAR.md).
Run from web/:  python tests/test_render_fixes.py

F1  A function graph that the plotter splits into pieces (it leaves the y-range, or is <= 0 on a log
    axis, or has a pole) must keep its colour, line width, opacity and dash on EVERY piece.
RT  `\\mathrm{...}` / `\\text{...}` directly after `_` or `^` (f_\\mathrm{A}, f_\\mathrm A) is the script
    itself, not the macro name: f_\\mathrm{A} reads "f" + subscript "A", never "fmathrmA".
LG  A Legend is anchored at a DATA point, but its row gap, swatch length and gap are SCENE (world) units,
    so the key looks the same on every axes; labels start right of the swatch (left-aligned)."""
import sys
sys.path.insert(0, "."); sys.path.insert(0, "py")
import numpy as np
from engine.scene_model import ModelScene
from engine.renderer import paint_scene
from engine.svg_painter import SvgPainter
from engine.richtext import parse

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)) if extra and not cond else ""))
    ok = ok and bool(cond)


def build(objects, extra=None):
    model = {"objects": objects, "animations": [], "background": [1, 1, 1]}
    if extra:
        model.update(extra)
    sc = ModelScene(model); sc.construct(); sc.show_static()
    return sc


def svg_of(sc):
    sp = SvgPainter(1920, 1080)
    paint_scene(sp, sc.objectList, sc.camera, background=[1, 1, 1])
    return sp.to_svg()


def leaves(obj):
    out = [obj] if len(obj.points) >= 4 else []
    for s in obj.subObjects:
        out += leaves(s)
    return out


# ---------------------------------------------------------------- F1 -------------------------------
RED = [1.0, 0.0, 0.0]
AX = {"id": "ax", "type": "Axes", "args": {"x_range": [-6, 6], "y_range": [-1.2, 1.2], "x_length": 10, "y_length": 4}}
sc = build([AX, {"id": "g", "type": "FunctionGraph",
                 "args": {"func": "1.5*sin(3x)", "x_range": [-6, 6], "color": RED, "stroke_width": 9,
                          "stroke_opacity": 0.6, "dash": "8,4"}}])
g = sc.objects_by_id["g"]
pcs = leaves(g)
check("F1 setup: 1.5 sin(3x) on y in [-1.2, 1.2] is split into several pieces", len(pcs) > 1, len(pcs))
check("F1 every piece keeps the colour", all(tuple(p.color) == tuple(RED) for p in pcs),
      [tuple(p.color) for p in pcs][:3])
check("F1 every piece keeps the line width", all(p.stroke_width == 9 for p in pcs), [p.stroke_width for p in pcs][:3])
check("F1 every piece keeps the stroke opacity", all(abs(p.stroke_opacity - 0.6) < 1e-12 for p in pcs))
check("F1 every piece keeps the dash pattern", all(p.dash == [8.0, 4.0] for p in pcs))
svg = svg_of(sc)
n_red = svg.count('stroke="#ff0000" stroke-width="9"')
check("F1 SVG: every piece is drawn red, 9 px", n_red == len(pcs), f"{n_red} of {len(pcs)}")

# a log y-axis: values <= 0 split the curve
AXL = {"id": "ax", "type": "Axes", "args": {"x_range": [-3, 3], "y_range": [0.01, 10], "x_length": 8, "y_length": 4, "y_log": True}}
sc = build([AXL, {"id": "g", "type": "FunctionGraph", "args": {"func": "x^3 - x", "x_range": [-3, 3], "color": RED, "stroke_width": 7}}])
pcs = leaves(sc.objects_by_id["g"])
check("F1 log axis: x^3-x splits into pieces", len(pcs) > 1, len(pcs))
check("F1 log axis: every piece red, 7 px", all(tuple(p.color) == tuple(RED) and p.stroke_width == 7 for p in pcs))

# operation results are graphs too (Sum of tan and 0 has poles -> pieces)
sc = build([AX, {"id": "f", "type": "FunctionGraph", "args": {"func": "tan(x)", "color": [0, 0, 1]}},
            {"id": "h", "type": "FunctionGraph", "args": {"func": "0*x", "color": [0, 0, 1]}}],
           {"computations": [{"id": "c1", "type": "Sum", "inputs": {"f": "f", "g": "h"},
                              "props": {"color": [0.5, 0.2, 0.8], "stroke_width": 6}}]})
res = [o for o in sc.objectList if o not in sc.objects_by_id.values()]
pcs = leaves(res[-1]) if res else []
check("F1 operation result (tan + 0) is split into pieces", len(pcs) > 1, len(pcs))
check("F1 operation result: every piece takes the operation's colour and width",
      pcs and all(tuple(p.color) == (0.5, 0.2, 0.8) and p.stroke_width == 6 for p in pcs))

# ---------------------------------------------------------------- rich text -------------------------
check("RT f_\\mathrm{A} -> f + subscript A", parse("f_\\mathrm{A}") == [[("f", ""), ("A", "_")]], parse("f_\\mathrm{A}"))
check("RT f_\\mathrm A (no braces, as in the LaTeX sources) -> f + subscript A",
      parse("f_\\mathrm A") == [[("f", ""), ("A", "_")]], parse("f_\\mathrm A"))
check("RT f_\\mathrm{AB} keeps the whole group", parse("f_\\mathrm{AB}") == [[("f", ""), ("AB", "_")]], parse("f_\\mathrm{AB}"))
check("RT x^\\text{max}", parse("x^\\text{max}") == [[("x", ""), ("max", "^")]], parse("x^\\text{max}"))
check("RT |H_\\mathrm{a}(f)| (script ends after the group)",
      parse("|H_\\mathrm{a}(f)|") == [[("|H", ""), ("a", "_"), ("(f)|", "")]], parse("|H_\\mathrm{a}(f)|"))
check("RT \\mathrm A without braces at base level -> A", parse("\\mathrm A") == [[("A", "")]], parse("\\mathrm A"))
check("RT \\mathrm{d}t stays plain", parse("\\mathrm{d}t") == [[("dt", "")]], parse("\\mathrm{d}t"))
check("RT unchanged: U_{GS}", parse("U_{GS}") == [[("U", ""), ("GS", "_")]])
check("RT unchanged: x_\\alpha", parse("x_\\alpha") == [[("x", ""), ("α", "_")]], parse("x_\\alpha"))
check("RT unchanged: 10^{-16} A", parse("10^{-16} A") == [[("10", ""), ("-16", "^"), (" A", "")]])
sc = build([AX, {"id": "t", "type": "Text", "args": {"text": "f_\\mathrm{A} = 1 kHz", "position": [0, 0, 0], "color": [0, 0, 0]}}])
svg = svg_of(sc)
check("RT SVG of f_\\mathrm{A} contains no macro name", "mathrm" not in svg)

# ---------------------------------------------------------------- legend ---------------------------
LEG = {"labels": "Eingang;Ausgang (exakt)", "colors": "ff0000;0000ff", "position": [1, 2, 0], "font_size": 26,
       "row_gap": 0.5, "swatch_len": 0.6, "gap": 0.2, "color": [0, 0, 0], "stroke_width": 6}


def legend_geom(ax_args):
    sc = build([{"id": "ax", "type": "Axes", "args": ax_args}, {"id": "L", "type": "Legend", "args": dict(LEG)}])
    L, ax = sc.objects_by_id["L"], sc.axes_by_id["ax"]
    sw = [s for s in L.subObjects if getattr(s, "text", None) is None]
    tx = [s for s in L.subObjects if getattr(s, "text", None) is not None]
    return ax, sw, tx


for name, axa in (("uniform 1:1", {"x_range": [-5, 5], "y_range": [-3, 3], "x_length": 10, "y_length": 6}),
                  ("y_length 4 over 2.4 (the analysis probe)", {"x_range": [0, 6], "y_range": [0, 2.4], "x_length": 6, "y_length": 4}),
                  ("x 0..100 over 6", {"x_range": [0, 100], "y_range": [0, 3], "x_length": 6, "y_length": 3})):
    ax, sw, tx = legend_geom(axa)
    gap_rows = sw[0].points[0][1] - sw[1].points[0][1]
    sw_len = sw[0].points[-1][0] - sw[0].points[0][0]
    check(f"LG {name}: row gap is 0.5 scene units", abs(gap_rows - 0.5) < 1e-9, gap_rows)
    check(f"LG {name}: swatch is 0.6 scene units long", abs(sw_len - 0.6) < 1e-9, sw_len)
    anchor = np.asarray(ax.coords_to_point(1, 2), dtype=float)
    check(f"LG {name}: first swatch starts at the data anchor (1, 2)", np.allclose(sw[0].points[0][:2], anchor[:2], atol=1e-9),
          (sw[0].points[0][:2], anchor[:2]))
    check(f"LG {name}: labels are left-aligned 0.2 right of the swatch",
          all(t.align == "left" for t in tx) and abs(tx[0].points[0][0] - (sw[0].points[-1][0] + 0.2)) < 1e-9,
          [(t.align, t.points[0][0]) for t in tx])

print("RENDER FIX TESTS PASSED" if ok else "RENDER FIX TESTS FAILED")
sys.exit(0 if ok else 1)
