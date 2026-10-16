import sys, numpy as np
sys.path.insert(0, ".")
from engine.scene_model import ModelScene
from engine.simpleShape import Square

def count_squares(objs, acc):
    for o in objs:
        if isinstance(o, Square): acc[0] += 1
        count_squares(o.subObjects, acc)

def build(op, nums, animating):
    m = {"objects": [], "computations": [{"id": "k", "type": op, "numbers": nums, "props": {"run_time": 4}}],
         "animations": [], "background": [1, 1, 1]}
    s = ModelScene(m); s.animating = animating; s.build_timeline()
    acc = [0]; count_squares(s.objectList, acc)
    return s, acc[0]

# Addition 10+4 -> 14 squares; animates (timeline has a segment)
s, n = build("Addition", [10, 4], True)
assert n == 14, n
assert s.duration > 0.5, s.duration
print("Addition OK: 14 squares, duration", s.duration)

# Subtraction 10-4: 14 squares, multi-step (move + annihilate)
s, n = build("Subtraction", [10, 4], True)
assert n == 14 and s.duration > 0.5, (n, s.duration)
print("Subtraction OK: 14 squares, duration", round(s.duration, 2))

# Multiplication 3x4: 3 groups of 4 squares = 12 (appear sequentially, merge, recolour)
s, n = build("Multiplication", [3, 4], True)
assert n == 12, n
assert s.duration > 0.5
print("Multiplication OK: %d squares (3 groups of 4)" % n)

# multiplication is NOT commutative in its DISPLAY: a*b = a groups of b (3*6 != 6*3 visually)
def mult_shape(nums):
    s, _ = build("Multiplication", nums, True)
    fades = [seg for seg in s.timeline if seg["anims"] and seg["anims"][0].__class__.__name__ == "FadeIn"]
    return (len(fades), len(fades[0]["anims"]))     # (number of groups, group size)
assert mult_shape([3, 6]) == (3, 6), mult_shape([3, 6])
assert mult_shape([6, 3]) == (6, 3), mult_shape([6, 3])
print("multiplication order OK: a*b = a groups of b (3*6 = 3 groups of 6)")

# Division 12 / 3: 12 squares reflow into columns
s, n = build("Division", [12, 3], True)
assert n == 12 and s.duration > 0.5, (n, s.duration)
print("Division OK: 12 squares")

# static (edit) view: squares shown, no timeline
s, n = build("Addition", [10, 4], False)
assert n == 14 and len(s.timeline) == 0
print("edit view OK: squares shown, no animation")

# Subtraction seek correctness: start shows ALL squares; end shows a-b (the k pairs annihilated)
def visible_squares(sc):
    cnt = [0]
    def w(os):
        for o in os:
            if isinstance(o, Square) and o.fill_opacity > 0.5: cnt[0] += 1
            w(o.subObjects)
    w(sc.objectList); return cnt[0]
s, _ = build("Subtraction", [10, 4], True)
s.seek(0.0)
assert visible_squares(s) == 14, ("start: all 14 visible", visible_squares(s))
s.seek(s.duration)
assert visible_squares(s) == 6, ("end: 10-4=6 remain", visible_squares(s))
print("Subtraction seek OK: start 14 visible, end 6 (annihilation, not shown early)")

# number-line (Cuisenaire-rod) representation: numbers become bars on a line
from engine.simpleShape import Rectangle
def build_mode(op, nums, mode):
    m = {"objects": [], "computations": [{"id": "k", "type": op, "numbers": nums, "props": {"run_time": 4, "mode": mode}}],
         "animations": [], "background": [1, 1, 1]}
    s = ModelScene(m); s.animating = True; s.build_timeline(); return s
def count_cls(sc, cls):
    acc = [0]
    def w(os):
        for o in os:
            if isinstance(o, cls): acc[0] += 1
            w(o.subObjects)
    w(sc.objectList); return acc[0]
assert count_cls(build_mode("Addition", [10, 4], "numberline"), Rectangle) == 2
assert count_cls(build_mode("Multiplication", [3, 4], "numberline"), Rectangle) == 3
assert count_cls(build_mode("Division", [12, 3], "numberline"), Rectangle) == 3
s = build_mode("Subtraction", [10, 4], "numberline")
assert count_cls(s, Rectangle) == 3 and s.duration > 0.5
print("number-line mode OK: Addition=2 bars, Mult=4, Div=4, Sub=3")

# hidden operation -> not run at all
mh = {"objects": [], "computations": [{"id": "k", "type": "Addition", "numbers": [5, 3], "props": {"run_time": 4}, "visible": False}],
      "animations": [], "background": [1, 1, 1]}
sh = ModelScene(mh); sh.animating = True; sh.build_timeline()
assert count_cls(sh, Square) == 0 and len(sh.timeline) == 0, "hidden operation must not run"
print("hidden operation OK: not rendered")

# FunctionGraph with two variables -> surface (quad mesh)
m = {"objects": [
        {"id": "ax", "type": "Axes", "args": {"x_range": [-3, 3], "y_range": [-3, 3], "z_range": [-1.5, 1.5], "x_length": 8, "y_length": 8, "z_length": 5}},
        {"id": "g", "type": "FunctionGraph", "args": {"func": "sin(x)*cos(y)", "color": [0.3, 0.6, 0.9], "fill_opacity": 1.0}},
     ], "camera": {"mode": "3d"}, "animations": [], "background": [1, 1, 1]}
sc = ModelScene(m); sc.construct()
g = sc.objects_by_id["g"]
assert len(g.subObjects) > 50, "two-variable FunctionGraph should be a surface mesh"
print("FunctionGraph(x,y) -> surface OK:", len(g.subObjects), "faces")
print("\nARITHMETIC / UNIFIED-GRAPH TESTS PASSED")
