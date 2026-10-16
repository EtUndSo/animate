import sys, numpy as np
sys.path.insert(0, ".")
from engine.camera import Camera
from engine.scene_model import ModelScene, func2_from_expr
from engine.renderer import paint_scene

# --- camera: Z-UP convention. World +z must ALWAYS point straight up on screen (no sideways shift)
# and above the centre, for every orbit angle; +z is nearer the viewer than -z (camera above plane). ---
tilt = Camera(mode="3d", theta=0.6, phi=1.0)
for th in (0.0, 0.6, 2.0, -1.3):
    for ph in (0.2, 1.0, 1.4):
        cam = Camera(mode="3d", theta=th, phi=ph)
        pz = cam.project([0, 0, 1])
        assert abs(pz[0] - cam.pixel_width / 2) < 1e-6, ("z must project straight up", th, ph, pz)
        assert pz[1] < cam.pixel_height / 2 - 10, ("z must point UP on screen", th, ph, pz)
print("camera z-up OK: +z projects straight up on screen for every orbit angle")

# depth ordering: +z (towards the viewer, who sits above the plane) has larger depth than -z
assert tilt.depth([0, 0, 1]) > tilt.depth([0, 0, -1])
print("depth OK")

# --- func2 / GeoGebra-style 2-var input ---
f = func2_from_expr("x*y + x^2")
assert abs(f(2, 3) - (6 + 4)) < 1e-9, f(2, 3)
print("func2 OK: x*y+x^2 @ (2,3) =", f(2, 3))

# --- full 3D scene builds + renders, colours reach faces ---
class Stub:
    def __init__(s): s.paths = 0; s.texts = 0
    def background(s, c): pass
    def draw_path(s, *a): s.paths += 1
    def draw_text(s, *a): s.texts += 1

model = {
    "camera": {"mode": "3d", "theta": 0.6, "phi": 1.0},
    "shadows": False,                                   # flat faces -> the surface face keeps the exact base colour
    "objects": [
        {"id": "ax", "type": "Axes", "args": {"x_range": [-3, 3], "y_range": [-3, 3], "z_range": [-3, 3]}},
        # a FunctionGraph whose term uses x AND y renders as a surface (Surface type removed)
        {"id": "s", "type": "FunctionGraph", "args": {"func": "sin(x)*cos(y)", "adaptive": False,
                                                "res_max": 8, "color": [0.3, 0.6, 0.9], "fill_opacity": 0.7}},
        {"id": "sp", "type": "Sphere", "args": {"radius": 1, "center": [2, 0, 0], "resolution": 6,
                                                "color": [0.9, 0.2, 0.2], "fill_opacity": 0.5}},
        {"id": "bx", "type": "Box", "args": {"width": 1, "height": 1, "depth": 1, "center": [-2, 0, 0],
                                             "color": [0.2, 0.8, 0.3], "fill_opacity": 0.5}},
        {"id": "py", "type": "Pyramid", "args": {"base": 1.5, "height": 2, "center": [0, 0, -2],
                                                 "color": [0.8, 0.6, 0.1], "fill_opacity": 0.5}},
        {"id": "v", "type": "Vector", "args": {"end": [0, 2, 0], "color": [0, 0, 0], "stroke_width": 4}},
    ],
    "animations": [], "background": [1, 1, 1],
}
sc = ModelScene(model); sc.construct()
assert sc.camera.mode == "3d"
p = Stub(); paint_scene(p, sc.objectList, sc.camera, background=[1, 1, 1])
assert p.paths > 100, p.paths           # axes + many surface/sphere/box/pyramid faces
print("3D scene renders OK:", p.paths, "paths")

# style reached the faces (not just the group)
surf = sc.objects_by_id["s"]
assert np.allclose(surf.subObjects[0].fill_color, [0.3, 0.6, 0.9]), "surface face colour missing"
vec = sc.objects_by_id["v"]
assert np.allclose(vec.subObjects[0].color, [0, 0, 0]), "vector colour missing"
assert len(vec.subObjects) > 1, "vector should have a shaft + arrowhead faces"
print("face styling OK (surface + vector)")
print("\n3D TESTS PASSED")
