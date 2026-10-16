import sys, numpy as np
sys.path.insert(0, ".")
from engine.calc import make_convolution
from engine.simpleShape import Circle
from engine import geometry as geom
from engine.scene_model import ModelScene
from engine.text import DecimalNumber

# --- convolution: Gaussian * Gaussian = sqrt(pi/2) * exp(-t^2/2) ---
f = lambda x: np.exp(-x**2)
h = make_convolution(f, f, -6, 6, 400)
assert abs(h(0) - np.sqrt(np.pi/2)) < 1e-3, (h(0), np.sqrt(np.pi/2))
assert abs(h(1) - np.sqrt(np.pi/2)*np.exp(-0.5)) < 1e-3, h(1)
print("convolution OK: (G*G)(0)=%.4f (exact %.4f)" % (h(0), np.sqrt(np.pi/2)))

# --- intersection area of two unit circles, centres distance 1 apart (lens formula) ---
A = Circle(center=[-0.5, 0, 0], radius=1.0)
B = Circle(center=[0.5, 0, 0], radius=1.0)
_, ar = geom.intersection(A, B)
r, d = 1.0, 1.0
lens = 2*r*r*np.arccos(d/(2*r)) - (d/2)*np.sqrt(4*r*r - d*d)
assert abs(ar - lens) < 0.03, (ar, lens)
print("intersection OK: area=%.4f (exact lens %.4f)" % (ar, lens))

# disjoint circles -> no overlap
C = Circle(center=[5, 0, 0], radius=1.0)
_, ar0 = geom.intersection(A, C)
assert ar0 == 0.0, ar0
print("disjoint OK: area 0")

# --- full model: Intersection as a COMPUTATION with an area result child ---
model = {
    "objects": [
        {"id": "c1", "type": "Circle", "args": {"center": [-0.5, 0, 0], "radius": 1.0, "color": [0.3,0.6,0.9], "fill_opacity": 0.3}},
        {"id": "c2", "type": "Circle", "args": {"center": [0.5, 0, 0], "radius": 1.0, "color": [0.9,0.3,0.3], "fill_opacity": 0.3}},
    ],
    "computations": [
        {"id": "k1", "type": "Intersection", "inputs": {"a": "c1", "b": "c2"}, "props": {"color": [0.4,0.1,0.6], "fill_opacity": 0.6},
         "children": [{"id": "ar", "type": "DecimalNumber", "result": {"key": "area"},
                       "args": {"position": [0, 1.4, 0], "font_size": 34, "color": [0,0,0], "decimals": 3, "prefix": "Schnitt = "}}]},
    ],
    "animations": [], "background": [1, 1, 1],
}
sc = ModelScene(model); sc.construct()
nums = []
def _find(objs):
    for o in objs:
        if isinstance(o, DecimalNumber): nums.append(o)
        _find(o.subObjects)
_find(sc.objectList)
assert nums and abs(nums[0].value - lens) < 0.03, (nums[0].value if nums else None, lens)
assert nums[0].text.startswith("Schnitt = ")
print("computation Intersection+result OK:", nums[0].text)

# wrong operand type -> computation is skipped (dead), no crash
bad = dict(model); bad = {**model, "computations": [{"id":"k2","type":"Intersection","inputs":{"a":"c1"},"props":{}}]}
ModelScene(bad).construct()   # missing operand b -> skipped, must not raise
print("invalid computation skipped OK")
print("\nCALC/GEOMETRY TESTS PASSED")
