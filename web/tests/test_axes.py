import sys, numpy as np
sys.path.insert(0, ".")  # run from web/
from engine.scene_model import ModelScene
from engine.axes import _nice_step, Axes
from engine.renderer import paint_scene

# --- nice step adapts to range ---
assert _nice_step(-100, 100) == 20.0, _nice_step(-100, 100)
assert _nice_step(-6, 6) in (1.0, 2.0), _nice_step(-6, 6)
assert _nice_step(0, 1) in (0.1, 0.2), _nice_step(0, 1)
print("nice_step OK:", _nice_step(-100,100), _nice_step(-6,6), _nice_step(0,1))

# --- fixed size: the x-axis LINE stays 12 wide in world, no matter the range ---
ax = Axes(x_range=(-100, 100), y_range=(-100, 100), x_length=12, y_length=6)
xline = ax.subObjects[0]                       # first child = x-axis line (grid off, so index 0)
w = xline.points[:,0].max() - xline.points[:,0].min()
assert abs(w - 12) < 1e-9, w
ax2 = Axes(x_range=(-6, 6), y_range=(-3, 3), x_length=12, y_length=6)
w2 = ax2.subObjects[0].points[:,0].max() - ax2.subObjects[0].points[:,0].min()
assert abs(w2 - 12) < 1e-9, w2
print("fixed size OK: axis line width", w, "(range -100..100) ==", w2, "(range -6..6)")

# --- object placed in DATA coords lands on the tick: center=50 -> coords_to_point(50,0) ---
model = {
    "objects": [
        {"id": "ax", "type": "Axes", "args": {"x_range": [-100, 100], "y_range": [-100, 100], "x_length": 12, "y_length": 6}},
        {"id": "c", "type": "Circle", "args": {"center": [50, 0, 0], "radius": 10, "color": [0.2,0.4,0.9], "fill_color":[0.9,0.1,0.1], "fill_opacity": 0.5, "stroke_width": 4, "show_center": True}},
    ],
    "animations": [], "background": [1,1,1],
}
sc = ModelScene(model); sc.construct()
circ = sc.objects_by_id["c"]
center_world = (circ.points.min(axis=0) + circ.points.max(axis=0)) / 2.0
expect = sc.objects_by_id["ax"].coords_to_point(50, 0)
assert np.allclose(center_world, expect, atol=1e-9), (center_world, expect)
print("data-coord placement OK: center world", center_world, "expected", expect)

# radius 10 data units -> world ax = 12/200 = 0.06 -> world radius 0.6
rx = (circ.points[:,0].max() - circ.points[:,0].min())/2
assert abs(rx - 0.6) < 1e-6, rx
print("data-coord size OK: world radius x", rx)

# --- renderer: fill_color used for fill, color for stroke; show_center adds a marker ---
class Stub:
    def __init__(self): self.paths=[]; self.texts=0
    def background(self, c): pass
    def draw_path(self, pts, fill, fo, sc, sw, so, contours=None): self.paths.append((tuple(fill), fo, tuple(sc), sw))
    def draw_text(self, *a): self.texts+=1

p = Stub()
paint_scene(p, sc.objectList, sc.camera, background=[1,1,1])
# find the circle outline path (stroke width 4, fill opacity 0.5)
circ_paths = [x for x in p.paths if abs(x[1]-0.5) < 1e-9 and abs(x[3]-4) < 1e-9]
assert circ_paths, p.paths
fill, fo, stroke, sw = circ_paths[0]
assert np.allclose(fill, [0.9,0.1,0.1]), fill      # fill_color
assert np.allclose(stroke, [0.2,0.4,0.9]), stroke  # outline color
print("fill/stroke split OK: fill", fill, "stroke", stroke)
# center marker: a path with the marker colour (0.90,0.25,0.20)
markers = [x for x in p.paths if np.allclose(x[0], [0.90,0.25,0.20], atol=1e-9)]
assert markers, "no center marker drawn"
print("center marker OK:", len(markers), "marker(s)")

# --- Riemann template builds + renders ---
tpl = {
    "objects": [
        {"id":"ax","type":"Axes","args":{"x_range":[0,3.2],"y_range":[-0.2,1.2],"x_length":12,"y_length":6}},
        {"id":"r","type":"Riemann","args":{"func":"sin(x)","count":12,"color":[0.35,0.6,0.92],"fill_opacity":0.5}},
        {"id":"g","type":"FunctionGraph","args":{"func":"sin(x)","x_range":[0,3.2],"color":[0.1,0.1,0.1],"stroke_width":5}},
    ],
    "animations":[{"type":"Create","target":"g","run_time":2.0}], "background":[1,1,1],
}
s2 = ModelScene(tpl).build_timeline()
s2.seek(s2.duration)   # end frame
p2 = Stub(); paint_scene(p2, s2.objectList, s2.camera, background=[1,1,1])
rects = sum(1 for x in p2.paths if abs(x[1]-0.5) < 1e-9)
assert rects >= 12, rects
print("Riemann OK: duration", s2.duration, "filled rects", rects)
print("\nALL TESTS PASSED")
