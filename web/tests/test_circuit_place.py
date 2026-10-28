"""Schematic placement like KiCad/LTspice: fixed-size symbols at a centre with rotation and a standard pin
distance (pins on the 0.5 grid), European (IEC) and American (ANSI) symbols per element, pin tables for
the editor's wiring. Legacy start/end components must keep working."""
import sys
sys.path.insert(0, ".")
import numpy as np
from engine import circuit as C
from engine.scene_model import ModelScene

PANEL = {"id": "pa", "type": "Axes", "args": {"x_range": [-7, 7], "y_range": [-4, 4], "x_length": 14,
                                               "y_length": 8, "show_axes": False}}


def build(objs):
    sc = ModelScene({"objects": [PANEL] + objs, "animations": [], "background": [1, 1, 1]})
    sc.construct()
    return sc


# 1. pins from centre / rotation / length, exact on the grid
a, b = C.component_ends({"center": [0.5, 1.0], "rotation": 0})
assert a == (-0.5, 1.0, 0.0) and b == (1.5, 1.0, 0.0), (a, b)
a, b = C.component_ends({"center": [0, 0], "rotation": 90, "length": 3})
assert a == (0.0, -1.5, 0.0) and b == (0.0, 1.5, 0.0), (a, b)
a, b = C.component_ends({"center": [0, 0], "rotation": 270})
assert a == (0.0, 1.0, 0.0) and b == (0.0, -1.0, 0.0), (a, b)
a, b = C.component_ends({"start": [-2, 0], "end": [2, 0]})          # legacy file
assert a == (-2.0, 0.0, 0.0) and b == (2.0, 0.0, 0.0)
print("pins from centre/rotation/length OK, legacy start/end OK")

# 2. every kind builds in both styles; the styles differ where the norms differ
differ = {"resistor", "resistor_nl", "resistor_var", "fuse", "inductor", "vsource", "isource", "vcvs", "ccvs"}
for kind in C.COMPONENT_KINDS:
    geo = {}
    for style in ("europäisch", "amerikanisch"):
        sc = build([{"id": "c", "type": "Component", "on": "pa",
                     "args": {"kind": kind, "center": [0, 0], "rotation": 90, "symbol_style": style, "label": ""}}])
        pts = sc.objects_by_id["c"].all_points()
        geo[style] = np.round(pts, 6)
    same = geo["europäisch"].shape == geo["amerikanisch"].shape and np.allclose(geo["europäisch"], geo["amerikanisch"])
    assert same != (kind in differ), (kind, "styles should " + ("differ" if kind in differ else "match"))
print("all", len(C.COMPONENT_KINDS), "kinds build in both styles; IEC/ANSI differ exactly where the norms do")

# 3. IEC resistor proportion 3 : 1, independent of the pin distance
for L in (2.0, 3.0, 4.0):
    sc = build([{"id": "r", "type": "Component", "on": "pa",
                 "args": {"kind": "resistor", "center": [0, 0], "length": L, "label": ""}}])
    box = [s for s in sc.objects_by_id["r"].subObjects if s.__class__.__name__ == "Polygon"][0]
    lo, hi = box.get_bounding_box()
    w, h = hi[0] - lo[0], hi[1] - lo[1]
    assert abs(w / h - 3.0) < 0.05, (L, w, h)
print("IEC resistor box 3 : 1 for every pin distance")

# 4. device pins follow rotation and flip; the opamp has an IEC box and an ANSI triangle
pins = dict((n, (round(x, 9), round(y, 9))) for n, x, y in C.device_pin_offsets({"kind": "npn", "rotation": 90}))
assert pins == {"B": (0.0, -1.0), "C": (-1.0, 0.5), "E": (1.0, 0.5)}, pins
pins = dict((n, (x, y)) for n, x, y in C.device_pin_offsets({"kind": "npn", "flip": True}))
assert pins["C"] == (0.5, -1.0) and pins["E"] == (0.5, 1.0), pins
iec = build([{"id": "o", "type": "Device", "on": "pa", "args": {"kind": "opamp", "label": ""}}]).objects_by_id["o"]
ansi = build([{"id": "o", "type": "Device", "on": "pa",
               "args": {"kind": "opamp", "label": "", "symbol_style": "amerikanisch"}}]).objects_by_id["o"]
assert len(iec.all_points()) != len(ansi.all_points())
print("device pins rotate/flip correctly; opamp IEC box vs ANSI triangle")

# 5. pins_world in world coordinates of a 1:1 panel = data coordinates
sc = build([])
ax = sc.axes_by_id["pa"]
w = C.pins_world("Component", {"center": [1.0, 0.5], "rotation": 0}, ax)
assert np.allclose(w[0][1][:2], [0.0, 0.5]) and np.allclose(w[1][1][:2], [2.0, 0.5]), w
w = C.pins_world("Wire", {"points": "0,0;1,0;1,2"}, ax)
assert [n for n, _ in w] == ["a", "b"] and np.allclose(w[1][1][:2], [1.0, 2.0])
w = C.pins_world("Device", {"kind": "npn", "center": [2, 0]}, ax)
assert np.allclose(dict(w)["B"][:2], [1.0, 0.0])
print("pins_world OK")
print("CIRCUIT PLACEMENT TESTS PASSED")
