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
                         round(o.stroke_opacity, 4), tuple(np.round(np.asarray(o.color, float), 3))))
        for s in o.subObjects:
            w(s)
    for o in scene.objectList:
        w(o)
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

if __name__ == "__main__":
    print("=== ENGINE CONTRACT PROBE ===")
    ok = all(probe(n, s) for n, s in cases)
    print("\nENGINE CONTRACT: WATERTIGHT" if ok else "\nENGINE CONTRACT: VIOLATIONS FOUND")
    assert ok, "engine contract violated"
    print("CONTRACT TESTS PASSED")
