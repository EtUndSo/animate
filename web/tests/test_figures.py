"""Render smoke test for the article-figure primitives (run from web/: python tests/test_figures.py).
Every new object type is built through the model interpreter, painted with the Canvas stub AND the
SVG painter, and must produce draw calls without raising. Also checks: dash reaches the painter,
rich labels parse, log axes map decades evenly, several Axes (panels) with `on`, Parameters in expressions."""
import sys, json
sys.path.insert(0, "."); sys.path.insert(0, "py")
import numpy as np
from engine.scene_model import ModelScene, _PARAMS
from engine.renderer import paint_scene
from engine.svg_painter import SvgPainter
from engine.axes import Axes
from engine.richtext import parse
from canvas_painter import CanvasPainter


class StubCtx:
    def __init__(self): self.calls = []; self.dashes = []
    def __setattr__(self, k, v):
        if k in ("calls", "dashes"): object.__setattr__(self, k, v)
        else: self.calls.append((k, v))
    def __getattr__(self, name):
        def m(*a):
            self.calls.append((name, a))
            if name == "setLineDash" and a and len(a[0]): self.dashes.append(list(a[0]))
            if name == "measureText":
                class W: width = 10.0
                return W()
        return m


def render(objects, extra=None):
    model = {"objects": objects, "animations": [], "background": [1, 1, 1]}
    if extra: model.update(extra)
    ctx = StubCtx()
    sc = ModelScene(model); sc.construct(); sc.show_static()
    paint_scene(CanvasPainter(ctx, 1920, 1080), sc.objectList, sc.camera, background=[1, 1, 1])
    sp = SvgPainter(1920, 1080)
    paint_scene(sp, sc.objectList, sc.camera, background=[1, 1, 1])
    draws = sum(1 for c in ctx.calls if c[0] in ("stroke", "fill", "fillText"))
    return sc, ctx, draws, sp.to_svg()


AX = {"id": "ax", "type": "Axes", "args": {"x_range": [-6, 6], "y_range": [-3, 3], "x_length": 12, "y_length": 6}}
ok = True
def check(name, cond):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name)
    ok = ok and bool(cond)

# 1. every new primitive renders
NEW = [
    {"id": "o1", "type": "DataCurve", "args": {"data": "0 0\n1 1\n2 0.5\n3 1.5", "markers": True, "color": [0, 0, 1], "stroke_width": 3, "dash": "8,6"}},
    {"id": "o2", "type": "Band", "args": {"x_min": 1, "x_max": 2, "full_height": True, "label": "Sättigung", "color": [0, 0, 1], "fill_color": [0, 0, 1], "fill_opacity": 0.2}},
    {"id": "o3", "type": "Stem", "args": {"x": "1;2;3", "y": "1;0.5;0.25", "labels": "f_0;2f_0;3f_0", "color": [0, 0, 1]}},
    {"id": "o4", "type": "PointCloud", "args": {"n": 30, "x_min": -2, "x_max": 2, "y_min": 0, "y_max": 2, "seed": 3, "distribution": "exp_y", "decay": 0.4, "hollow": True, "color": [1, 0, 0]}},
    {"id": "o5", "type": "TextBox", "args": {"text": "U_{BE}\\\\steigt", "center": [-3, 2, 0], "shape": "round", "color": [0, 0, 0], "fill_color": [1, 1, 1], "fill_opacity": 1}},
    {"id": "o6", "type": "TextBox", "args": {"text": "ja?", "center": [3, 2, 0], "shape": "diamond", "color": [0, 0, 0]}},
    {"id": "o7", "type": "Brace", "args": {"start": [-2, -2, 0], "end": [2, -2, 0], "label": "T", "color": [0, 0, 0]}},
    {"id": "o8", "type": "Mark", "args": {"center": [4, -2, 0], "kind": "cross", "color": [1, 0, 0]}},
    {"id": "o9", "type": "Shape", "args": {"points": "-5,-1;-3,-1;-3,0;-5,0", "material": "n+", "label": "n^+", "color": [0, 0, 0]}},
    {"id": "o10", "type": "Table", "args": {"cells": "G_1,-G_1;-G_1,G_1+G_2", "row_labels": "1;2", "col_labels": "1;2", "highlight": "1,1", "position": [-5.5, 2.8, 0], "color": [0, 0, 0], "fill_color": [1, 0.8, 0.2], "fill_opacity": 0.4}},
    {"id": "o11", "type": "Component", "args": {"kind": "resistor", "start": [-5, -2.5, 0], "end": [-3, -2.5, 0], "label": "R_1", "value": "1\\,k\\Omega", "current": "I_1", "voltage": "U_1", "color": [0, 0, 0]}},
    {"id": "o12", "type": "Device", "args": {"kind": "npn", "center": [4, 0, 0], "label": "T_1", "color": [0, 0, 0]}},
    {"id": "o13", "type": "Wire", "args": {"points": "-3,-2.5;-1,-2.5;-1,-1", "route": "hv", "dots": "1", "color": [0, 0, 0]}},
    {"id": "o14", "type": "Node", "args": {"center": [-1, -1, 0], "label": "K_1", "color": [0, 0, 0]}},
    {"id": "o15", "type": "Ellipse", "args": {"center": [0, 0, 0], "width": 2, "height": 1, "color": [0, 0, 1], "dash": "4,4"}},
    {"id": "o16", "type": "LabeledArrow", "args": {"start": [0, -3, 0], "end": [2, -1, 0], "label": "I_D", "elbow": "hv", "double": True, "color": [0, 0, 0], "stroke_width": 3}},
    {"id": "o17", "type": "LabeledArrow", "args": {"start": [-6, 1, 0], "end": [-4, 1, 0], "label": "10 mA", "thick": 0.4, "color": [0, 0.5, 0]}},
    {"id": "o18", "type": "TangentLine", "args": {"func": "0.2*x^2", "x0": 2, "triangle_dx": 1.5, "color": [0, 0, 0]}},
    {"id": "o19", "type": "LoopArrow", "args": {"center": [0, 0, 0], "radius": 0.6, "start_angle": 0, "end_angle": 60, "head": False, "label": "\\alpha", "color": [0, 0, 0]}},
    {"id": "o20", "type": "Text", "args": {"text": "10^{-16} A", "position": [4, 2.5, 0], "align": "left", "color": [0, 0, 0]}},
]
for spec in NEW:
    try:
        sc, ctx, draws, svg = render([AX, spec])
        check(f"{spec['type']} renders ({draws} draw ops)", draws > 0 and "<path" in svg)
    except Exception as e:
        check(f"{spec['type']} renders :: {type(e).__name__}: {e}", False)

# all together (also checks dash reaches the canvas painter)
sc, ctx, draws, svg = render([AX] + NEW)
check("all new objects together", draws > 50)
check("dash pattern reaches the canvas painter", [8.0, 6.0] in ctx.dashes)
check("dash pattern reaches the SVG", 'stroke-dasharray="8 6"' in svg)
check("rich text in SVG (tspan with dy shift)", '<tspan dy=' in svg)
from engine.circuit import COMPONENT_KINDS, DEVICE_KINDS
for name, spec in (("each kind of Component", "Component"), ("each kind of Device", "Device")):
    kinds = COMPONENT_KINDS if spec == "Component" else DEVICE_KINDS
    bad = []
    for k in kinds:
        a = {"kind": k, "color": [0, 0, 0]}
        a.update({"start": [-1, 0, 0], "end": [1, 0, 0], "current": "I", "voltage": "U", "label": "X", "value": "1"} if spec == "Component" else {"center": [0, 0, 0], "label": "X", "rotation": 90, "flip": True})
        try:
            _, _, d, _ = render([AX, {"id": "k", "type": spec, "args": a}])
            if d == 0: bad.append(k)
        except Exception as e:
            bad.append(f"{k}:{type(e).__name__}:{e}")
    check(name + (" :: " + ", ".join(bad) if bad else ""), not bad)

# 2. log axes: decades evenly spaced, 10^k labels, plot samples log-uniformly
ax = Axes(x_range=[1, 1000], y_range=[1e-3, 1], x_length=6, y_length=4, x_log=True, y_log=True)
p1, p10, p100 = ax.c2p(1, 1e-3), ax.c2p(10, 1e-3), ax.c2p(100, 1e-3)
check("log x: equal decade spacing", abs((p10 - p1)[0] - (p100 - p10)[0]) < 1e-9)
texts = [o.text for o in ax.subObjects if getattr(o, "text", None) is not None]
check("log axis labels 10^{k}", "10^{-3}" in texts and "10^{3}" in texts)
g = ax.plot(lambda x: 1.0 / x, x_range=[1, 1000], y_range=[1e-3, 1])
check("log plot of 1/x is a straight line", len(g.points) > 4 and abs(np.std(np.diff(g.points[::3, 1]) / np.maximum(1e-9, np.diff(g.points[::3, 0]))) ) < 1e-6)

# 3. panels: two Axes with origin, object bound via `on`
objs = [{"id": "a1", "type": "Axes", "args": {"x_range": [0, 1], "y_range": [0, 1], "x_length": 4, "y_length": 3, "origin": [-4, 0, 0], "title": "(a)"}},
        {"id": "a2", "type": "Axes", "args": {"x_range": [0, 1], "y_range": [0, 1], "x_length": 4, "y_length": 3, "origin": [4, 0, 0], "title": "(b)"}},
        {"id": "d1", "type": "Dot", "args": {"center": [0, 0, 0], "radius": 0.1, "color": [1, 0, 0]}},
        {"id": "d2", "type": "Dot", "args": {"center": [0, 0, 0], "radius": 0.1, "color": [0, 0, 1]}, "on": "a2"}]
sc, ctx, draws, svg = render(objs)
c1, c2 = sc.objects_by_id["d1"].get_center(), sc.objects_by_id["d2"].get_center()
check("panel binding: dot on (a) left, dot on (b) right", abs(c1[0] - (-6.0)) < 1e-6 and abs(c2[0] - 2.0) < 1e-6)

# 4. parameters in expressions
objs = [AX, {"id": "p", "type": "Parameter", "args": {"name": "k", "value": 2.0, "min": 0, "max": 5, "step": 0.1}},
        {"id": "g", "type": "FunctionGraph", "args": {"func": "k*x", "x_range": [-2, 2], "color": [0, 0, 1]}}]
sc, ctx, draws, svg = render(objs)
g = sc.objects_by_id["g"]
y_at_end = g.points[-1][1] - g.points[0][1]
x_at_end = g.points[-1][0] - g.points[0][0]
check("parameter k=2 used in k*x (slope 2 in data units)", abs((y_at_end / x_at_end) - 2.0) < 0.05)

# 5. richtext parse
check("richtext U_{GS}", parse("U_{GS}") == [[("U", ""), ("GS", "_")]])
check("richtext 10^{-16}", parse("10^{-16} A") == [[("10", ""), ("-16", "^"), (" A", "")]])
check("richtext nested e^{U/U_T}", parse("e^{U/U_T}") == [[("e", ""), ("U/U", "^"), ("T", "^_")]])
check("richtext two lines", len(parse("a\\\\b")) == 2)

# 6. computed markers: intersection of a diode-like curve and a load line, point on a curve, x from a parameter
objs = [{"id": "ax", "type": "Axes", "args": {"x_range": [0, 5], "y_range": [0, 5], "x_length": 10, "y_length": 5}},
        {"id": "p", "type": "Parameter", "args": {"name": "U0", "value": 4.0}},
        {"id": "m1", "type": "Marker", "args": {"point": [1, 0, 0], "func": "x^2", "func2": "U0 - x", "label": "AP"}},
        {"id": "m2", "type": "Marker", "args": {"point": [0, 0, 0], "x_expr": "U0/2", "func": "x^2", "label": "Q"}}]
sc, ctx, draws, svg = render(objs)
ax = sc.axes_by_id["ax"]
x_ap = (-1 + np.sqrt(17)) / 2                      # x^2 = 4 - x
dot = [s for s in sc.objects_by_id["m1"].subObjects if type(s).__name__ == "Dot"][0]
check("Marker at the intersection x^2 = U0 - x", np.allclose(dot.get_center()[:2], ax.c2p(x_ap, x_ap ** 2)[:2], atol=1e-4))
dot = [s for s in sc.objects_by_id["m2"].subObjects if type(s).__name__ == "Dot"][0]
check("Marker x from a parameter, y on the curve", np.allclose(dot.get_center()[:2], ax.c2p(2.0, 4.0)[:2], atol=1e-6))

# 7. tangent on a semi-log axes is straight in plot space (exponential -> constant decades per unit)
objs = [{"id": "ax", "type": "Axes", "args": {"x_range": [0, 1], "y_range": [1e-12, 1e-2], "x_length": 8, "y_length": 5, "y_log": True}},
        {"id": "t", "type": "TangentLine", "args": {"func": "1e-15*exp(x/0.02585)", "x0": 0.6, "half_len": 0.1, "triangle_dx": 0.0595, "show_point": False}}]
sc, ctx, draws, svg = render(objs)
ax = sc.axes_by_id["ax"]
ln = sc.objects_by_id["t"].subObjects[0]
a, b = ln.points[0], ln.points[-1]
y_dec_per_world = 10.0 / 5.0                        # 10 decades on 5 world units
slope_dec_per_V = (b[1] - a[1]) * y_dec_per_world / ((b[0] - a[0]) / 8.0)
check("semi-log tangent: 1/(U_T ln10) decades per volt", abs(slope_dec_per_V - 1.0 / (0.02585 * np.log(10))) < 0.05)

# 8. CurveFamily with explicit values + labels
objs = [AX, {"id": "f", "type": "CurveFamily", "args": {"func": "k*x", "param": "k", "values": "0.5;1;2", "labels": "a;b;c", "x_min": 0, "x_max": 2, "fade": False, "color": [0, 0, 1]}}]
sc, ctx, draws, svg = render(objs)
fam = sc.objects_by_id["f"]
check("CurveFamily: 3 curves + 3 labels from explicit values", sum(1 for s in fam.subObjects if getattr(s, "text", None)) == 3 and len(fam.subObjects) == 6)

# 9. SVG export contains every label once and is well-formed XML
import xml.dom.minidom
sc, ctx, draws, svg = render([AX] + NEW)
try:
    xml.dom.minidom.parseString(svg.encode("utf-8")); okxml = True
except Exception as e:
    okxml = False; print("   XML:", e)
check("SVG export is well-formed XML", okxml)

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
