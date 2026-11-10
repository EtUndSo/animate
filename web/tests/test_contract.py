"""ENGINE CONTRACT TEST — the watertight foundation (run: `python tests/test_contract.py` from web/).

seek(t) must be a PURE function of t:
  (a) idempotent        seek(t) twice == once
  (b) path-independent   direct to t == after wandering elsewhere first
  (c) stepping == jump   many small steps to t == one jump to t

Every object / animation / operation type is probed here. ANY NEW PRIMITIVE MUST BE ADDED BELOW AND
PASS, so the timeline can never drift into an inconsistent state. See ENGINE_CONTRACT.md for the rules.
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import numpy as np
from engine.scene import Scene
from engine.scene_model import ModelScene
from engine.simpleShape import Square, Circle
from engine.svg import MathTex
from engine.animation import (Shift, FadeIn, FadeOut, Create, GrowFromCenter, Recolor, Pulse,
                              Transform, ReplacementTransform, TransformMatchingTex)


def snap(scene):
    rows = []
    def w(o):
        if len(o.points):
            rows.append((np.round(o.points, 4).tobytes(), round(o.fill_opacity, 4),
                         round(o.stroke_opacity, 4), tuple(np.round(np.asarray(o.color, float), 3)),
                         getattr(o, "text", None), round(float(getattr(o, "font_size", 0) or 0), 4)))   # a label's content too
        for s in o.subObjects:
            w(s)
    for o in scene.objectList:
        w(o)
    c = scene.camera                                     # L4: the camera is part of the frame too
    rows.append(("cam", round(c.theta, 6), round(c.phi, 6), round(c.zoom, 6), tuple(np.round(c.center, 6))))
    return tuple(rows)


def probe(name, scene):
    D = scene.duration
    ts = [0.0, 0.17 * D, 0.5 * D, 0.83 * D, D]
    issues = []
    for t in ts:
        scene.seek(t); a = snap(scene); scene.seek(t); b = snap(scene)
        if a != b: issues.append(f"not idempotent @ {t:.2f}")
    direct = {}
    for t in ts:
        scene.seek(t); direct[t] = snap(scene)
    for t in ts:
        scene.seek(D); scene.seek(0.0); scene.seek(0.5 * D); scene.seek(t)
        if snap(scene) != direct[t]: issues.append(f"path-dependent @ {t:.2f}")
    scene.seek(0.0)
    for t in np.linspace(0, D, 23): scene.seek(float(t))
    scene.seek(ts[2])
    if snap(scene) != direct[ts[2]]: issues.append("stepping != jump")
    print(("  OK   " if not issues else " FAIL  ") + name + ("" if not issues else "  :: " + "; ".join(sorted(set(issues)))))
    return not issues


def model_scene(model):
    s = ModelScene(model); s.animating = True; s.build_timeline(); return s


def eng(build):
    s = Scene(); build(s); return s


sq = "M0 0 L10 0 L10 10 L0 10 Z"
AX = {"id": "ax", "type": "Axes", "args": {"x_range": [-5, 5], "y_range": [-3, 3], "x_length": 12, "y_length": 6}}
mt = lambda chars: MathTex([{"d": sq, "m": [1, 0, 0, 1, 20 * i, 0], "c": c} for i, c in enumerate(chars)], height=1.0)

cases = []
cases.append(("Shift", model_scene({"objects": [{"id": "s", "type": "Square", "args": {"side": 1}}],
    "animations": [{"type": "Shift", "target": "s", "run_time": 2, "args": {"vector": [3, 1, 0]}}], "background": [1, 1, 1]})))
cases.append(("Create+FadeIn sequence", model_scene({"objects": [AX, {"id": "g", "type": "FunctionGraph", "args": {"func": "sin(x)"}},
    {"id": "c", "type": "Circle", "args": {"radius": 1}}],
    "animations": [{"type": "Create", "target": "g", "run_time": 2}, {"type": "FadeIn", "target": "c", "run_time": 1}], "background": [1, 1, 1]})))
cases.append(("parallel step (2 objs)", model_scene({"objects": [{"id": "s", "type": "Square", "args": {"side": 1}}, {"id": "c", "type": "Circle", "args": {"radius": 1}}],
    "animations": [{"type": "Shift", "target": "s", "run_time": 2, "step": 0, "args": {"vector": [2, 0, 0]}},
                   {"type": "FadeIn", "target": "c", "run_time": 2, "step": 0}], "background": [1, 1, 1]})))
cases.append(("Convolution (op)", model_scene({"objects": [AX, {"id": "f", "type": "FunctionGraph", "args": {"func": "exp(-x^2)"}},
    {"id": "g", "type": "FunctionGraph", "args": {"func": "exp(-x^2)"}}],
    "computations": [{"id": "k", "type": "Convolution", "inputs": {"f": "f", "g": "g"}, "props": {"run_time": 4, "tau_range": [-5, 5]}}],
    "animations": [], "background": [1, 1, 1]})))
cases.append(("Arithmetic (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "Multiplication", "numbers": [3, 4], "props": {"run_time": 4, "mode": "squares"}}],
    "animations": [], "background": [1, 1, 1]})))
cases.append(("Summation vec (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "Summation", "props": {
    "sum_mode": "number", "term": "1/i^2", "from": 1, "to": 6, "show_terms": 3, "run_time": 4,
    "glyphs": [{"d": sq, "m": [1, 0, 0, 1, 20 * i, 0], "c": c} for i, c in enumerate("abc")]}}],
    "animations": [], "background": [1, 1, 1]})))

def _tf(s): a = Square(side=1); s.play(Transform(a, Circle(radius=1)), run_time=2)
cases.append(("Transform", eng(_tf)))
def _rtf(s): a = Square(side=1); s.play(ReplacementTransform(a, Circle(radius=1)), run_time=2)
cases.append(("ReplacementTransform", eng(_rtf)))
def _tmt(s): s.play(TransformMatchingTex(mt("ab"), mt("ba")), run_time=2)
cases.append(("TransformMatchingTex", eng(_tmt)))
def _seq(s):
    a = Square(side=1); s.add(a); s.play(Shift(a, [2, 0, 0]), run_time=1); s.play(FadeOut(a), run_time=1)
cases.append(("Shift then FadeOut (same obj)", eng(_seq)))
def _grow(s): a = Square(side=1); s.play(GrowFromCenter(a), run_time=1)
cases.append(("GrowFromCenter", eng(_grow)))
def _rec(s): a = Square(side=1); a.fill_opacity = 1.0; s.add(a); s.play(Recolor(a, (1, 0, 0)), run_time=1)
cases.append(("Recolor", eng(_rec)))
def _pulse(s): a = Square(side=1); s.add(a); s.play(Pulse(a), run_time=1)
cases.append(("Pulse", eng(_pulse)))
# P0 movement/emphasis animations
def _mscene(anim):
    m = {"objects": [{"id": "s", "type": "Square", "args": {"side": 1}}],
         "animations": [dict({"target": "s", "run_time": 1}, **anim)], "background": [1, 1, 1]}
    return model_scene(m)
cases.append(("Rotate", _mscene({"type": "Rotate", "args": {"angle": 1.57}})))
cases.append(("Scale", _mscene({"type": "Scale", "args": {"factor": 2}})))
cases.append(("MoveTo", _mscene({"type": "MoveTo", "args": {"point": [2, 1, 0]}})))
cases.append(("Indicate", _mscene({"type": "Indicate", "args": {}})))
cases.append(("Write", _mscene({"type": "Write", "args": {}})))
# L1/L2/L9 in the model (editor menu): FadeOut, morph into a template object (`to`, never drawn), Indicate on one
# Table cell / row, a pause step (Wait), Rotate about a point
cases.append(("FadeOut (model)", _mscene({"type": "FadeOut", "args": {}})))
_MORPH_M = lambda typ: model_scene({"objects": [{"id": "s", "type": "Square", "args": {"side": 1}},
                                                {"id": "c", "type": "Circle", "args": {"radius": 1.5}}],
                                    "animations": [{"type": typ, "target": "s", "run_time": 2, "args": {"to": "c"}},
                                                   {"type": "Shift", "target": "s", "run_time": 1, "args": {"vector": [1, 0, 0]}}],
                                    "background": [1, 1, 1]})
cases.append(("Transform to template (model)", _MORPH_M("Transform")))
cases.append(("ReplacementTransform to template (model)", _MORPH_M("ReplacementTransform")))
_TAB = {"id": "t", "type": "Table", "args": {"cells": "1,2;3,4", "position": [0, 0, 0]}}
cases.append(("Indicate cell + row (model)", model_scene({"objects": [_TAB], "background": [1, 1, 1], "animations": [
    {"type": "FadeIn", "target": "t", "run_time": 1, "step": 0},
    {"type": "Indicate", "target": "t", "run_time": 1, "step": 1, "args": {"cell": [1, 0]}},
    {"type": "Wait", "target": None, "run_time": 0.5, "step": 2},
    {"type": "Indicate", "target": "t", "run_time": 1, "step": 3, "args": {"row": 0}}]})))
cases.append(("Rotate about a point (model)", _mscene({"type": "Rotate", "args": {"angle": 1.57, "around": [2, 0, 0]}})))
# E1 (10.11.2026): a label changes its content (Transform Text -> Text: text, colour, size, place; fade out / in), twice
# in a row and shifted afterwards; typewriter / raw text; draw order of creation (only the painting order changes).
_T = lambda i, t, x, col, **kw: {"id": i, "type": "Text", "args": dict({"text": t, "position": [x, 0, 0], "font_size": 24,
                                                                        "color": col}, **kw)}
cases.append(("Transform text -> text, twice (model)", model_scene({"objects": [
    _T("t", "alt.txt", 0, [0, 0, 0], font="mono", raw=True), _T("v", "neu.txt", 1, [1, 0, 0], font="mono", raw=True),
    _T("w", "C:\\ende_1", -1, [0, 0, 1], raw=True), {"id": "k", "type": "Square", "args": {"side": 1}}],
    "animations": [{"type": "FadeIn", "target": "t", "run_time": 1, "step": 0},
                   {"type": "Transform", "target": "t", "run_time": 1, "step": 1, "args": {"to": "v"}},
                   {"type": "TransformMatchingTex", "target": "t", "run_time": 1, "step": 2, "args": {"to": "w"}},
                   {"type": "Shift", "target": "t", "run_time": 1, "step": 3, "args": {"vector": [0, 1, 0]}},
                   {"type": "GrowFromCenter", "target": "k", "run_time": 1, "step": 3}],
    "background": [1, 1, 1], "draw_order": "creation"})))
from engine.animation import FadeInLines  # noqa: E402
def _lines(s):                               # a formula with three rows (glyphs stacked) appears row by row
    m = MathTex([{"d": sq, "m": [1, 0, 0, 1, 20 * (i % 2), -30 * (i // 2)], "c": c} for i, c in enumerate("abcdef")], height=2.0)
    s.play(FadeInLines(m), run_time=3)
cases.append(("FadeIn lines (formula row by row)", eng(_lines)))

# Σ step-by-step choreography (number mode) with synthetic glyph data
_G = lambda ch: [{"d": sq, "m": [1, 0, 0, 1, 0, 0], "c": ch}]
_choreo = {"head": _G("S"), "cols": [
    {"t": "op", "g": _G("=")},
    {"t": "term", "abstract": _G("a"), "subst": _G("1"), "value": _G("1")},
    {"t": "plus", "g": _G("+")},
    {"t": "term", "abstract": _G("a"), "subst": _G("2"), "value": None},   # symbolic tail (no value)
    {"t": "op", "g": _G("=")}, {"t": "total", "g": _G("3")}]}
cases.append(("Summation choreo (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "Summation",
    "props": {"sum_mode": "number", "run_time": 6, "size": 0.9, "choreo": _choreo}}],
    "animations": [], "background": [1, 1, 1]})))
# the same, wrapped into several rows (max_width) and sized by font_size
cases.append(("Summation choreo wrapped (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "Summation",
    "props": {"sum_mode": "number", "run_time": 6, "max_width": 0.6, "font_size": 30, "choreo": _choreo}}],
    "animations": [], "background": [1, 1, 1]})))
# scalar product: two column vectors (glyphs tagged with their table cell), terms abstract -> index -> subst -> value,
# the component pair of each term pulses while it is put in
_Gc = lambda ch, cell, x, y: {"d": sq, "m": [1, 0, 0, 1, x, y], "c": ch, "cell": cell}
_dot = {"head": _G("S") + [{"d": sq, "m": [1, 0, 0, 1, 20, 0], "c": "j"}], "var": "j", "rows": 3,
        "vectors": [{"d": sq, "m": [1, 0, 0, 1, 0, 0], "c": "w"}] + [_Gc(str(r), r, 20, -12 * r) for r in range(3)]
                   + [_Gc(str(r), 3 + r, 60, -12 * r) for r in range(3)],
        "stages": ["index", "subst", "value"], "cols": [
    {"t": "op", "g": _G("=")},
    {"t": "term", "abstract": _G("a"), "index": _G("b"), "subst": _G("c"), "value": _G("1"), "row": 0},
    {"t": "plus", "g": _G("+")},
    {"t": "term", "abstract": _G("a"), "index": _G("b"), "subst": _G("c"), "value": _G("2"), "row": 1},
    {"t": "plus", "g": _G("+")}, {"t": "ell", "g": _G(".")}, {"t": "plus", "g": _G("+")},
    {"t": "term", "abstract": _G("a"), "index": _G("b"), "subst": _G("c"), "value": _G("3"), "row": 2},
    {"t": "op", "g": _G("=")}, {"t": "total", "g": _G("6")}]}
cases.append(("DotProduct choreo (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "DotProduct",
    "props": {"run_time": 6, "size": 0.9, "all_steps": True, "choreo": _dot}}],
    "animations": [], "background": [1, 1, 1]})))
cases.append(("DotProduct choreo wrapped (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "DotProduct",
    "props": {"run_time": 6, "max_width": 1.0, "font_size": 30, "choreo": _dot}}],
    "animations": [], "background": [1, 1, 1]})))
# the other two forms (dot_display): marks, '·', '= product' per row ('komponenten'); u turns into the row vector
# (Rotate + MoveAlongPath on arcs), v is laid onto it, products after '=' ('matrix'). Row 1 is a ⋮ / ⋯ row.
_col = lambda x0: [{"d": sq, "m": [1, 0, 0, 3, x0 - 8, -24], "c": "("}] + [_Gc(str(r), r, x0, -12 * r) for r in range(3)]
_grid = ([_Gc("u", c, 20 * c, 0) for c in range(3)] + [_Gc(".", 3 + c, 20 * c, -12) for c in (0, 2)]
         + [_Gc("v", 6 + c, 20 * c, -24) for c in range(3)])
_dot_g = {"nameU": _G("w"), "nameV": _G("x"), "nameUT": _G("W"), "lhs": _G("L"), "colU": _col(0), "colV": _col(0),
          "cdot": _G("."), "eq": _G("="), "vdots": _G(":"), "grid": _grid,
          "rowU": [{"d": sq, "m": [1, 0, 0, 1, -12, 0], "c": "("}, {"d": sq, "m": [1, 0, 0, 1, 60, 0], "c": ")"}]
                  + [_Gc("u", c, 20 * c, 0) for c in range(3)]}
for _mode in ("komponenten", "matrix"):
    _dm = dict(_dot, dot={"mode": _mode, "m": 3, "ell": [False, True, False], "g": _dot_g, "vals": [_G("1"), None, _G("3")]})
    cases.append((f"DotProduct {_mode} (op)", model_scene({"objects": [], "computations": [{"id": "k", "type": "DotProduct",
        "props": {"run_time": 6, "size": 0.9, "choreo": _dm}}], "animations": [], "background": [1, 1, 1]})))

# Article-figure primitives (figures.py, circuit.py, panels, log axes, parameters): every type animated
# (Create / FadeIn / Shift / Write / GrowFromCenter), several panels, dashed strokes, rich labels.
_PANEL = {"id": "p2", "type": "Axes", "args": {"x_range": [1, 1000], "y_range": [1e-3, 1], "x_length": 4, "y_length": 3,
                                              "origin": [3, 0, 0], "x_log": True, "y_log": True, "title": "(b)"}}
_FIG_OBJS = [AX, _PANEL, {"id": "par", "type": "Parameter", "args": {"name": "k", "value": 1.5}},
    {"id": "dc", "type": "DataCurve", "args": {"data": "1 0.001\n10 0.01\n100 0.1", "markers": True, "dash": "8,6"}, "on": "p2"},
    {"id": "bd", "type": "Band", "args": {"x_min": -1, "x_max": 1, "full_height": True, "label": "B", "fill_opacity": 0.2}},
    {"id": "st", "type": "Stem", "args": {"x": "1;2;3", "y": "1;0.5;0.25", "labels": "a;b;c"}},
    {"id": "pc", "type": "PointCloud", "args": {"n": 12, "seed": 2}},
    {"id": "tb", "type": "TextBox", "args": {"text": "U_{BE}\\\\steigt", "center": [-3, 2, 0], "shape": "diamond"}},
    {"id": "br", "type": "Brace", "args": {"start": [-2, -2, 0], "end": [2, -2, 0], "label": "T"}},
    {"id": "mk", "type": "Mark", "args": {"center": [4, -2, 0], "kind": "check"}},
    {"id": "sh", "type": "Shape", "args": {"points": "-4,-1;-3,-1;-3,0", "material": "p+", "label": "p^+"}},
    {"id": "tbl", "type": "Table", "args": {"cells": "1,2;3,4", "highlight": "0,0", "brackets": True}},
    {"id": "cp", "type": "Component", "args": {"kind": "vccs", "start": [-4, 1, 0], "end": [-4, 3, 0], "label": "g_m u", "current": "i", "voltage": "u"}},
    {"id": "dv", "type": "Device", "args": {"kind": "nmos4", "center": [2, 2, 0], "rotation": 90}},
    {"id": "wr", "type": "Wire", "args": {"points": "0,0;1,1;2,0", "route": "hv", "dots": "all"}},
    {"id": "nd", "type": "Node", "args": {"center": [1, 1, 0], "label": "K"}},
    {"id": "el", "type": "Ellipse", "args": {"center": [0, 1, 0], "width": 2, "height": 1, "dash": "4,4"}},
    {"id": "la", "type": "LabeledArrow", "args": {"start": [0, -1, 0], "end": [2, 0, 0], "label": "I", "elbow": "vh", "thick": 0.2}},
    {"id": "fam", "type": "CurveFamily", "args": {"func": "k*x*p", "param": "p", "values": "0.5;1", "labels": "a;b", "x_min": 0, "x_max": 2}},
    {"id": "mr", "type": "Marker", "args": {"point": [1, 0, 0], "func": "x^2", "func2": "k*2 - x", "label": "AP"}}]
_FIG_ANIMS = [{"type": "Create", "target": "dc", "run_time": 1, "step": 0}, {"type": "FadeIn", "target": "bd", "run_time": 1, "step": 0},
              {"type": "Create", "target": "st", "run_time": 1, "step": 1}, {"type": "GrowFromCenter", "target": "tb", "run_time": 1, "step": 1},
              {"type": "Shift", "target": "cp", "run_time": 1, "step": 2, "args": {"vector": [1, 0, 0]}},
              {"type": "Write", "target": "tbl", "run_time": 1, "step": 2}, {"type": "Create", "target": "wr", "run_time": 1, "step": 3},
              {"type": "FadeIn", "target": "dv", "run_time": 1, "step": 3}, {"type": "Create", "target": "fam", "run_time": 1, "step": 4},
              {"type": "Indicate", "target": "mr", "run_time": 1, "step": 4}]
cases.append(("article figures (panels, log, circuit, figures)", model_scene({"objects": _FIG_OBJS, "animations": _FIG_ANIMS,
                                                                               "background": [1, 1, 1]})))
# P3: a graph split into styled pieces (F1) and a legend anchored in data with scene-unit spacing,
# animated like any other object (the piece styles are build-time state, the timeline stays pure).
_AXN = {"id": "ax", "type": "Axes", "args": {"x_range": [-6, 6], "y_range": [-1.2, 1.2], "x_length": 10, "y_length": 4}}
cases.append(("split graph + legend (P3)", model_scene({"objects": [_AXN,
    {"id": "g", "type": "FunctionGraph", "args": {"func": "1.5*sin(3x)", "color": [1, 0, 0], "stroke_width": 9, "dash": "8,4"}},
    {"id": "lg", "type": "Legend", "args": {"labels": "f_\\mathrm{A};g", "position": [-5, 1, 0]}}],
    "animations": [{"type": "Create", "target": "g", "run_time": 1, "step": 0}, {"type": "FadeIn", "target": "lg", "run_time": 1, "step": 1},
                   {"type": "Shift", "target": "lg", "run_time": 1, "step": 2, "args": {"vector": [1, 0, 0]}}],
    "background": [1, 1, 1]})))

# L3 (10.11.2026): parameters over time. A Parameter is a ValueTracker, ChangeValue moves it, and every object whose
# props name it is redrawn per frame (updater): curve (also growing x_range), point on the curve with guides,
# tangent, area up to the parameter, number display, line from coordinate expressions; Create before and FadeOut
# after the parameter moves; two parameters at once; a whole-number parameter; a curve that splits and joins again.
_AXL = {"id": "ax", "type": "Axes", "args": {"x_range": [0, 7], "y_range": [-1.5, 1.5], "x_length": 8, "y_length": 4}}
_P = lambda i, n, v, **kw: {"id": i, "type": "Parameter", "args": dict({"name": n, "value": v}, **kw)}
_CV = lambda tgt, v, step, rt=2, **kw: {"type": "ChangeValue", "target": tgt, "run_time": rt, "step": step,
                                        "args": dict({"value": v}, **kw)}
_L3_WAVE = {"objects": [_AXL, _P("p", "t", 0),
    {"id": "g", "type": "FunctionGraph", "args": {"func": "sin(x - t)", "color": [0, 0, 1]}},
    {"id": "h", "type": "FunctionGraph", "args": {"func": "cos(x)", "x_range": [0, "t"], "samples": 40}},
    {"id": "mk", "type": "Marker", "args": {"point": [0, 0, 0], "x_expr": "t", "func": "sin(x)", "show_guides": True, "label": "P"}},
    {"id": "tg", "type": "TangentLine", "args": {"func": "sin(x)", "x0": "t", "half_len": 1}},
    {"id": "ar", "type": "Area", "args": {"func": "sin(x)", "x_min": 0, "x_max": "t", "samples": 30, "fill_opacity": 0.3}},
    {"id": "dn", "type": "DecimalNumber", "args": {"value": "t", "prefix": "t = ", "suffix": " s", "position": [1, 1.2, 0],
                                                    "decimals": 2, "align": "left", "font_size": 26}},
    {"id": "ln", "type": "Line", "args": {"start": ["t", -1, 0], "end": ["t", 1, 0]}}],
    "animations": [{"type": "Create", "target": "g", "run_time": 1, "step": 0}, _CV("p", "2*pi", 1, 4, rate="linear"),
                   {"type": "FadeOut", "target": "ln", "run_time": 1, "step": 2}],
    "background": [1, 1, 1], "lang": "de"}
cases.append(("L3 parameter: curve, point, tangent, area, number, line (model)", model_scene(_L3_WAVE)))
cases.append(("L3 two parameters at once: pointer turns and shrinks (model)", model_scene({"objects": [
    {"id": "ax", "type": "Axes", "args": {"x_range": [-2, 2], "y_range": [-2, 2], "x_length": 4, "y_length": 4}},
    _P("pr", "r", 1.5), _P("pp", "phi", 0),
    {"id": "z", "type": "LabeledArrow", "args": {"start": [0, 0, 0], "end": ["r*cos(phi)", "r*sin(phi)", 0], "label": "z"}},
    {"id": "c", "type": "Circle", "args": {"center": [0, 0, 0], "radius": "r", "fill_opacity": 0}},
    {"id": "d", "type": "Dot", "args": {"center": ["r*cos(phi)", "r*sin(phi)", 0]}}],
    "animations": [{"type": "FadeIn", "target": "z", "run_time": 1, "step": 0},
                   _CV("pr", 0.5, 1, 3), _CV("pp", "3*pi/2", 1, 3, rate="linear")],
    "background": [1, 1, 1]})))
_L3_INT = {"objects": [_AXL, _P("pn", "n", 1, integer=True),
    {"id": "g", "type": "FunctionGraph", "args": {"func": "(1 + x/n)^n", "x_range": [0, 1.5]}},
    {"id": "dn", "type": "DecimalNumber", "args": {"value": "n", "decimals": 0, "prefix": "n = ", "position": [5, 1, 0]}}],
    "animations": [_CV("pn", 8, 0, 4, rate="linear"), {"type": "Indicate", "target": "dn", "run_time": 1, "step": 1}],
    "background": [1, 1, 1]}
cases.append(("L3 whole-number parameter n = 1 ... 8 (model)", model_scene(_L3_INT)))
cases.append(("L3 curve splits at a moving pole and joins again (model)", model_scene({"objects": [_AXL, _P("pa", "a", -2),
    {"id": "g", "type": "FunctionGraph", "args": {"func": "0.3/(x - a)"}},
    {"id": "k", "type": "FunctionGraph", "args": {"func": "sqrt(x - a)/3", "x_range": [0, 7]}}],
    "animations": [{"type": "FadeIn", "target": "g", "run_time": 1, "step": 0}, _CV("pa", 9, 1, 4, rate="linear"),
                   _CV("pa", 3.5, 2, 1)],
    "background": [1, 1, 1]})))


def l3_checks():
    """Values behind the probes: the whole-number parameter gives each n the same share of the time; the number
    display follows the language; the final frame shows the end values; the editor scene file (szenen_lib) and its
    engine model (export_szenen.python_model, the same mapping as editor.js animArgs) agree."""
    s = model_scene(_L3_INT)
    seen = []
    for k in range(400):
        s.seek(4.0 * k / 400)
        seen.append(s.objects_by_id["pn"].value)
    assert all(v == int(v) for v in seen) and sorted(set(seen)) == list(range(1, 9)), set(seen)
    shares = [seen.count(n) for n in range(1, 9)]
    assert max(shares) - min(shares) <= 1, shares
    s.seek(0.0)
    assert s.objects_by_id["dn"].text == "n = 1", s.objects_by_id["dn"].text
    s.seek(4.0)
    assert s.objects_by_id["dn"].text == "n = 8", s.objects_by_id["dn"].text
    w = model_scene(_L3_WAVE)
    w.seek(w.duration)
    assert w.objects_by_id["dn"].text == "t = 6,28 s", w.objects_by_id["dn"].text
    w.seek(0.0)
    assert w.objects_by_id["dn"].text == "t = 0,00 s"
    assert len(w.objects_by_id["g"].points) == 1                          # Create at its start: nothing drawn yet
    en = model_scene(dict(_L3_WAVE, lang="en"))
    en.seek(3.0)
    assert en.objects_by_id["dn"].text == "t = 3.14 s", en.objects_by_id["dn"].text
    # editor scene file <-> engine model
    import json as _json
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "tools")))
    from szenen_lib import Szene
    from export_szenen import python_model
    sz = Szene("test/l3")
    a = sz.achsen((0, 7), (-1.5, 1.5))
    sz.parameter("t", 0)
    n = sz.parameter("n", 1, ganzzahlig=True)
    sz.kurve(a, "sin(x - t)")
    sz.zahl(a, "t", (1, 1.2), vor="t = ", nach=" s")
    with sz.gleichzeitig():
        sz.verstellen("t", "2*pi", dauer=3, rate="linear")
        sz.verstellen(n, 5, dauer=3)
    data = _json.loads(_json.dumps(sz.model()))
    anims = data["model"]["animations"]
    assert anims[0] == {"id": "a1", "type": "ChangeValue", "target": "o2", "run_time": 3.0, "step": 0,
                        "value": "2*pi", "rate": "linear"}, anims[0]
    assert anims[1] == {"id": "a2", "type": "ChangeValue", "target": "o3", "run_time": 3.0, "step": 0, "value": 5.0}
    assert data["model"]["objects"][2]["props"]["max"] == 5.0 and data["model"]["objects"][2]["props"]["integer"] is True
    pm = python_model(data, None, None, "de", [])
    assert pm["animations"][0] == {"type": "ChangeValue", "target": "o2", "step": 0, "run_time": 3.0,
                                   "args": {"value": "2*pi", "rate": "linear"}}, pm["animations"][0]
    assert pm["animations"][1]["args"] == {"value": 5.0}
    ms = ModelScene(pm); ms.animating = True; ms.build_timeline()
    assert abs(ms.duration - 3.0) < 1e-9
    ms.seek(3.0)
    assert ms.objects_by_id["o5"].text == "t = 6,28 s" and ms.objects_by_id["o3"].value == 5
    ok = probe("L3 scene file -> python_model -> engine", ms)
    print("  OK   L3 values (whole-number shares, number format, scene file round trip)")
    return ok


# L5 (10.11.2026): plane maps. ApplyMatrix moves its target and args.objects (grid, dot, polygon, circle, graph, arrow,
# label, point cloud) from p to A p; a second map starts from the image of the first; ApplyFunction maps pointwise.
_AX5 = {"id": "ax", "type": "Axes", "args": {"x_range": [-3, 3], "y_range": [-2, 2], "x_length": 6, "y_length": 4}}
_L5_OBJS = [_AX5,
    {"id": "g", "type": "Grid", "args": {"x_step": 1, "y_step": 1, "extend": 1.0, "color": [0.5, 0.6, 0.8]}},
    {"id": "g0", "type": "Grid", "args": {"x_step": 1, "extend": 0, "stroke_opacity": 0.4}},          # ghost: stays
    {"id": "d", "type": "Dot", "args": {"center": [1, 1, 0]}},
    {"id": "q", "type": "Polygon", "args": {"vertices": [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]], "fill_opacity": 0.3}},
    {"id": "c", "type": "Circle", "args": {"center": [0, 0, 0], "radius": 1, "fill_opacity": 0}},
    {"id": "f", "type": "FunctionGraph", "args": {"func": "0.5*sin(2*x)", "x_range": [-2, 2], "samples": 30}},
    {"id": "e", "type": "LabeledArrow", "args": {"start": [0, 0, 0], "end": [1, 0, 0], "label": "e_1", "label_at": "end"}},
    {"id": "t", "type": "Text", "args": {"text": "P", "position": [1.2, 1.2, 0]}},
    {"id": "pc", "type": "PointCloud", "args": {"n": 6, "seed": 3, "x_min": -1, "x_max": 1, "y_min": -1, "y_max": 1}}]
_MOVED = ["d", "q", "c", "f", "e", "t", "pc"]
_L5_TWO = {"objects": _L5_OBJS, "background": [1, 1, 1], "animations": [
    {"type": "FadeIn", "target": "q", "run_time": 1, "step": 0},
    {"type": "ApplyMatrix", "target": "g", "run_time": 2, "step": 1, "args": {"matrix": [[1, 1], [0, 1]], "objects": _MOVED}},
    {"type": "ApplyMatrix", "target": "g", "run_time": 2, "step": 2,
     "args": {"matrix": [["cos(pi/2)", "-sin(pi/2)"], ["sin(pi/2)", "cos(pi/2)"]], "objects": _MOVED, "path": "rotate"}}]}
cases.append(("L5 matrix on grid, dot, polygon, circle, graph, arrow, label, cloud (model)", model_scene({
    "objects": _L5_OBJS, "background": [1, 1, 1], "animations": [
        {"type": "ApplyMatrix", "target": "g", "run_time": 2, "step": 0, "args": {"matrix": [[2, 1], [1, 1.5]], "objects": _MOVED}},
        {"type": "Indicate", "target": "t", "run_time": 1, "step": 1}]})))
cases.append(("L5 two maps in a row: shear, then rotation path (model)", model_scene(_L5_TWO)))
cases.append(("L5 nonlinear map: polar coordinates (model)", model_scene({"objects": [
    {"id": "ax", "type": "Axes", "args": {"x_range": [-2.5, 2.5], "y_range": [-2.5, 4.5], "x_length": 5, "y_length": 7}},
    {"id": "g", "type": "Grid", "args": {"x_step": 0.5, "y_step": 0.5, "extend": 0, "clip": False, "samples": 17,
                                         "x_range": [0, 2], "y_range": [0, 4]}}],
    "animations": [{"type": "ApplyFunction", "target": "g", "run_time": 3, "step": 0,
                    "args": {"func": ["x*cos(pi*y/2)", "x*sin(pi*y/2)"], "rate": "linear"}}], "background": [1, 1, 1]})))
# L4 (10.11.2026): camera rides. MoveCamera turns (theta, turn), tilts (phi), zooms and moves the look-at point; two in a
# row; one together with a FadeIn and a parameter that moves a ball and a label in 3D; layers and discs facing the camera.
_L4_OBJS = [{"id": "b", "type": "Cube", "args": {"side": 1.2, "fill_opacity": 0.4}},
            {"id": "l", "type": "Line", "args": {"start": [-1, -1, -1], "end": [1, 1, 1]}},
            {"id": "s", "type": "Sphere", "args": {"radius": 0.4, "center": [1.5, 0, 0], "resolution": 5}},
            {"id": "k", "type": "Ball", "args": {"center": ["a", 0, 1], "radius": 0.2, "layer": 1}},
            {"id": "p", "type": "Parameter", "args": {"name": "a", "value": -1}},
            {"id": "tx", "type": "Text", "args": {"text": "A", "position": ["a", 0, 1.4]}}]
_L4_RIDE = {"objects": _L4_OBJS, "camera": {"mode": "3d", "theta": 0.6, "phi": 0.4}, "background": [1, 1, 1], "animations": [
    {"type": "MoveCamera", "target": None, "run_time": 2, "step": 0, "args": {"turn": 6.283185307, "rate": "linear"}},
    {"type": "MoveCamera", "target": None, "run_time": 1.5, "step": 1, "args": {"phi": 1.0, "zoom": 2, "center": [0.5, 0, 0.5]}},
    {"type": "FadeIn", "target": "s", "run_time": 1, "step": 1}, _CV("p", 1, 1, 1.5),
    {"type": "MoveCamera", "target": None, "run_time": 1, "step": 2, "args": {"theta": 0.2, "zoom": 1, "center": [0, 0, 0]}}]}
cases.append(("L4 camera ride: turn, tilt + zoom + look-at with FadeIn and a parameter, back (model)", model_scene(_L4_RIDE)))
cases.append(("L4 2D zoom (model)", model_scene({"objects": [_AXL, {"id": "g", "type": "FunctionGraph", "args": {"func": "sin(x)"}}],
    "animations": [{"type": "MoveCamera", "target": None, "run_time": 2, "step": 0, "args": {"zoom": 4, "center": [1, 0.5, 0]}}],
    "background": [1, 1, 1]})))


def l5_l4_checks():
    """Values behind the L5/L4 probes: states at intermediate times, the composition of two maps, a dot staying round,
    the camera between keyframes, and the scene file (szenen_lib) -> python_model -> engine for both."""
    s = model_scene(_L5_TWO)
    ax = s.objects_by_id["ax"]
    w2d = lambda p: np.asarray(ax.coords_to_point(*p), dtype=float)
    def corners():
        P = s.objects_by_id["q"].points
        return [P[i] for i in (0, 3, 6, 9)]
    s.seek(2.0)                                           # halfway through the shear (smooth: alpha = 1/2)
    assert np.allclose(corners()[2], w2d((1.5, 1)), atol=1e-6), corners()[2]
    s.seek(3.0)                                           # sheared: (1, 1) -> (2, 1)
    assert np.allclose(corners()[2], w2d((2, 1)), atol=1e-6)
    s.seek(4.0)                                           # rotation path halfway: |p| is kept (no shrinking)
    r = np.linalg.norm(corners()[2] - w2d((0, 0)))
    assert abs(r - np.linalg.norm(w2d((2, 1)) - w2d((0, 0)))) < 1e-6, r
    s.seek(5.0)                                           # rotated by 90 degrees: (2, 1) -> (-1, 2)
    assert np.allclose(corners()[2], w2d((-1, 2)), atol=1e-6), corners()[2]
    d = s.objects_by_id["d"].points
    assert abs((d[:, 0].max() - d[:, 0].min()) - (d[:, 1].max() - d[:, 1].min())) < 1e-9   # the dot stays round
    assert np.allclose((d.min(axis=0) + d.max(axis=0)) / 2, w2d((-1, 2)), atol=1e-6)
    g0 = s.objects_by_id["g0"]
    s.seek(0.0); a0 = [c.points.copy() for c in g0.subObjects]
    s.seek(5.0); assert all(np.array_equal(x, c.points) for x, c in zip(a0, g0.subObjects))   # the ghost grid stays
    c = model_scene(_L4_RIDE)
    c.seek(1.0)
    assert abs(c.camera.theta - (0.6 + np.pi)) < 1e-6 and abs(c.camera.zoom - 1) < 1e-12
    c.seek(2.75)                                          # second ride halfway: phi, zoom geometric, look-at point
    assert abs(c.camera.phi - 0.7) < 1e-6 and abs(c.camera.zoom - 2 ** 0.5) < 1e-6
    assert np.allclose(c.camera.center, [0.25, 0, 0.25]), c.camera.center
    c.seek(c.duration)
    assert abs(c.camera.theta - 0.2) < 1e-9 and c.camera.zoom == 1 and not c.camera._has_center
    c.seek(0.0)
    assert abs(c.camera.theta - 0.6) < 1e-12 and abs(c.camera.phi - 0.4) < 1e-12
    # editor scene file <-> engine model
    import json as _json
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "tools")))
    from szenen_lib import Szene, det_ausdruck
    from export_szenen import python_model
    sz = Szene("test/l5")
    a = sz.achsen((-3, 3), (-2, 2), breite=6, hoehe=4)
    g = sz.gitter(a, 1)
    q = sz.vieleck(a, [(0, 0), (1, 0), (1, 1), (0, 1)])
    e = sz.vektor(a, (1, 0), label="e_1")
    sz.zahl(None, "abs(" + det_ausdruck([[3, 1], [1, 2]], "s") + ")", (2, 1))
    sz.abbilden([[3, 1], [1, 2]], [g, q, e], dauer=2, parameter="s")
    sz.abbilden([[0, -1], [1, 0]], [g, q, e], dauer=1, weg="drehung")
    data = _json.loads(_json.dumps(sz.model()))
    an = data["model"]["animations"]
    assert an[0] == {"id": "a1", "type": "ApplyMatrix", "target": g, "run_time": 2.0, "step": 0,
                     "matrix": [[3, 1], [1, 2]], "objects": [q, e]}, an[0]
    assert an[1]["type"] == "ChangeValue" and an[1]["step"] == 0 and an[2]["path"] == "rotate"
    pm = python_model(data, None, None, "de", [])
    assert pm["animations"][0]["args"] == {"objects": [q, e], "matrix": [[3, 1], [1, 2]]}, pm["animations"][0]
    assert pm["animations"][2]["args"]["path"] == "rotate"
    ms = ModelScene(pm); ms.animating = True; ms.build_timeline()
    ms.seek(2.0)
    assert ms.objects_by_id["o5"].text == "5,00", ms.objects_by_id["o5"].text      # area of the image = det A
    ok = probe("L5 scene file -> python_model -> engine", ms)
    sk = Szene("test/l4")
    sk.kamera_start(theta=30, phi=20)
    b = sk.kugel(None, (0, 0, 0), r=0.3)
    sk.einblenden(b)
    sk.kamera(drehen=90, phi=40, zoom=1.5, dauer=2)
    sk.kamera_kreisen(360, dauer=3)
    data = _json.loads(_json.dumps(sk.model()))
    assert data["model"]["camera"]["mode"] == "3d" and abs(data["model"]["camera"]["theta"] - np.radians(30)) < 1e-6
    an = data["model"]["animations"]
    assert an[1] == {"id": "a2", "type": "MoveCamera", "target": None, "run_time": 2.0, "step": 1, "phi": 40.0,
                     "turn": 90.0, "zoom": 1.5}, an[1]
    pm = python_model(data, None, None, "de", [])
    assert abs(pm["animations"][1]["args"]["turn"] - np.pi / 2) < 1e-12 and pm["animations"][2]["args"]["rate"] == "linear"
    ms = ModelScene(pm); ms.animating = True; ms.build_timeline()
    ms.seek(ms.duration)
    assert abs(ms.camera.theta - np.radians(30 + 90 + 360)) < 1e-6 and abs(ms.camera.phi - np.radians(40)) < 1e-9
    ok = probe("L4 scene file -> python_model -> engine", ms) and ok
    print("  OK   L5/L4 values (maps in a row, rotation path, round dot, ghost grid, camera between keyframes, round trips)")
    return ok


if __name__ == "__main__":
    print("=== ENGINE CONTRACT PROBE ===")
    ok = all(probe(n, s) for n, s in cases)
    ok = l3_checks() and ok
    ok = l5_l4_checks() and ok
    print("\nENGINE CONTRACT: WATERTIGHT" if ok else "\nENGINE CONTRACT: VIOLATIONS FOUND")
    assert ok, "engine contract violated"
    print("CONTRACT TESTS PASSED")
