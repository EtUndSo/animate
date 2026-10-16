import sys, numpy as np
sys.path.insert(0, ".")
from engine.scene_model import ModelScene
from engine.text import DecimalNumber

def find(objs, pred, out):
    for o in objs:
        if pred(o): out.append(o)
        find(o.subObjects, pred, out)

model = {
    "objects": [
        {"id": "ax", "type": "Axes", "args": {"x_range": [-5, 5], "y_range": [-0.3, 1.4], "x_length": 12, "y_length": 5}},
        {"id": "f", "type": "FunctionGraph", "args": {"func": "exp(-x^2)", "color": [0.3, 0.6, 0.9], "stroke_width": 4}},
        {"id": "g", "type": "FunctionGraph", "args": {"func": "exp(-x^2)", "color": [0.5, 0.76, 0.42], "stroke_width": 4}},
    ],
    "computations": [
        {"id": "k1", "type": "Convolution", "inputs": {"f": "f", "g": "g"},
         "props": {"run_time": 4.0, "color": [0.89, 0.29, 0.2], "tau_range": [-5, 5]}},
    ],
    "animations": [], "background": [1, 1, 1],
}

s = ModelScene(model); s.animating = True; s.build_timeline()   # PLAY mode -> animated process
assert s.duration >= 4.0, s.duration            # the convolution slide is on the timeline
print("duration OK:", s.duration)

# PLAY: the two operand graphs are consumed by the operator (not drawn as separate top-level objects)
from engine.value_tracker import ValueTracker
assert any(isinstance(o, ValueTracker) for o in s.objectList), "convolution needs a ValueTracker"

# EDIT (static) mode: all objects shown + a finished convolution curve, no ValueTracker / no timeline
st = ModelScene(model); st.construct()
assert st.duration <= 1e-5 + 0.0 or len(st.timeline) == 0, "edit view must not animate"
assert not any(isinstance(o, ValueTracker) for o in st.objectList), "edit view has no ValueTracker"
assert st.objects_by_id["f"] in st.objectList and st.objects_by_id["g"] in st.objectList, "operands shown in edit view"
print("edit vs play mode OK (operands shown statically, consumed while playing)")

labels = []
find(s.objectList, lambda o: isinstance(o, DecimalNumber), labels)
assert labels, "no value label"
val = labels[0]

from engine.calc import make_convolution
from engine.value_tracker import ValueTracker as _VT
conv = make_convolution(lambda x: np.exp(-x**2), lambda x: np.exp(-x**2), -5, 5, 240)
tracker = [o for o in s.objectList if isinstance(o, _VT)][0]
s.seek(s.duration / 2.0)                         # value label must equal conv(current slide position)
assert abs(val.value - conv(tracker.get_value())) < 0.02, (val.value, conv(tracker.get_value()))
print("convolution animates: value tracks conv(t) (k=%.2f -> %.4f)" % (tracker.get_value(), val.value))

s.seek(0.0)
assert val.value < 0.1, val.value                # at the start g is off to the left -> ~0 overlap
print("start value ~0 OK:", round(val.value, 4))

# a trace object that grows: compare total drawn points near start vs near end
def total_pts(sc):
    tot = [0]
    def walk(os):
        for o in os:
            tot[0] += len(o.points); walk(o.subObjects)
    walk(sc.objectList); return tot[0]
s.seek(0.05 * s.duration); n_early = total_pts(s)
s.seek(0.95 * s.duration); n_late = total_pts(s)
assert n_late > n_early, (n_early, n_late)       # the result curve is traced out over time
print("result curve traced OK: pts %d -> %d" % (n_early, n_late))

# --- CORRECTNESS: rect*rect = triangle, and the DRAWN trace matches the math exactly ---
from engine.scene_model import func_from_expr
rect = func_from_expr("rect(t)")
cv = make_convolution(rect, rect, -5, 5, 1200)
assert abs(cv(0) - 1) < 0.02 and abs(cv(0.5) - 0.5) < 0.03 and cv(2) < 0.02 and cv(-2) < 0.02, \
    (cv(0), cv(0.5), cv(2))
print("rect*rect = triangle OK: conv(0)=%.3f conv(.5)=%.3f conv(2)=%.3f" % (cv(0), cv(0.5), cv(2)))

m2 = {"objects": [
        {"id": "ax", "type": "Axes", "args": {"x_range": [-5, 5], "y_range": [-0.3, 1.4], "x_length": 12, "y_length": 5}},
        {"id": "f", "type": "FunctionGraph", "args": {"func": "rect(t)"}},
        {"id": "g", "type": "FunctionGraph", "args": {"func": "rect(t)"}},
     ], "computations": [{"id": "k", "type": "Convolution", "inputs": {"f": "f", "g": "g"},
                          "props": {"run_time": 4, "tau_range": [-5, 5]}}],
      "animations": [], "background": [1, 1, 1]}
s2 = ModelScene(m2); s2.animating = True; s2.build_timeline()
trk = [o for o in s2.objectList if isinstance(o, _VT)][0]
def _role(objs, role, out):
    for o in objs:
        if getattr(o, "_role", None) == role: out.append(o)
        _role(o.subObjects, role, out)
s2.seek(0.42 * s2.duration)                       # g is inside the window but not yet overlapping
k = trk.get_value()
assert -5.0 < k < -1.0, k                         # inside the axis range, left of the overlap
tr = []; _role(s2.objectList, "conv_trace", tr); trace = tr[0]
assert len(trace.points) >= 2, "trace should have been revealed up to k"
assert cv(k) < 0.05, ("math: no overlap yet", k, cv(k))
ax2 = s2.objects_by_id["ax"]
lead_x = float(trace.points[:, 0].max())
kx = float(ax2.coords_to_point(k, 0)[0])
assert abs(lead_x - kx) < 0.5, ("leading edge != k", lead_x, kx)               # not racing ahead
flat_y = float(ax2.coords_to_point(0, 0)[1])                                    # world y where conv = 0
assert float(np.abs(trace.points[:, 1] - flat_y).max()) < 0.15, "trace not flat before overlap"
print("convolution trace matches the math: leading edge = k, flat (conv≈0) before overlap")
print("\nPROCESS (animated convolution) TESTS PASSED")
