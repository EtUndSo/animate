import sys, numpy as np
sys.path.insert(0, ".")
from engine.axes import Axes
from engine.camera import Camera
from engine.renderer import paint_scene
from engine.scene_model import ModelScene, func2_from_expr

ax = Axes(x_range=(-3, 3), y_range=(-3, 3), z_range=(-2, 2), x_length=6, y_length=6, z_length=4)

# coords_to_point: data z=0 stays on the x-y plane; z scales from there
assert np.allclose(ax.coords_to_point(0, 0, 0), [0, 0, 0])
p = ax.coords_to_point(0, 0, 2)                      # z_max -> +z_length/2 along TOWARDS
assert abs(p[2] - 2 * (4 / 4)) < 1e-9 and p[0] == 0 and p[1] == 0, p
print("coords_to_point(x,y,z) OK: plane at z=0, z scales up")

# the z-axis is a 3D-only subgroup (hidden in 2D)
z_only = [s for s in ax.subObjects if getattr(s, "_only_3d", False)]
assert len(z_only) == 1 and len(z_only[0].subObjects) > 0, "z-axis group missing"
print("z-axis group present (labelled), tagged 3D-only")

# 2D view hides the z-axis; 3D view shows it -> more draw ops in 3D
class Stub:
    def __init__(s): s.n = 0
    def background(s, c): pass
    def draw_path(s, *a): s.n += 1
    def draw_text(s, *a): s.n += 1
cam2 = Camera(mode="2d"); cam3 = Camera(mode="3d", theta=0.6, phi=1.0)
a2 = Stub(); paint_scene(a2, [ax], cam2); b3 = Stub(); paint_scene(b3, [ax], cam3)
assert b3.n > a2.n, (a2.n, b3.n)
print("2D hides z-axis, 3D shows it OK: 2D=%d, 3D=%d draw ops" % (a2.n, b3.n))

# surface z=f(x,y): CURVATURE-ADAPTIVE quad mesh, Lambert-shaded (faces have varying colour)
surf = ax.plot_surface(func2_from_expr("sin(x)*cos(y)"), resolution=16, res_min=2)  # low floor -> adaptivity visible
assert len(surf.subObjects) > 16, ("adaptive mesh should refine a wavy surface", len(surf.subObjects))
cols = {tuple(round(c, 3) for c in q.fill_color) for q in surf.subObjects}
assert len(cols) > 10, "surface not shaded (all faces same colour)"
# a peak face sits above the plane (positive z world)
zmax = max(q.points[:, 2].max() for q in surf.subObjects)
assert zmax > 0.3, zmax
# ADAPTIVITY: a flat plane needs FAR fewer faces than a wavy surface at the same resolution
flat = ax.plot_surface(func2_from_expr("0*x+0*y"), resolution=16, res_min=2)
assert len(flat.subObjects) < len(surf.subObjects), ("flat must be coarser", len(flat.subObjects), len(surf.subObjects))
print("adaptive surface OK: wavy=%d faces vs flat=%d faces, %d shaded colours" % (len(surf.subObjects), len(flat.subObjects), len(cols)))

# via the model: Surface uses the scene's axes (2-variable function works)
model = {"camera": {"mode": "3d", "theta": 0.6, "phi": 1.0},
         "objects": [
             {"id": "ax", "type": "Axes", "args": {"x_range": [-3, 3], "y_range": [-3, 3], "z_range": [-1.5, 1.5], "x_length": 8, "y_length": 8, "z_length": 5}},
             {"id": "s", "type": "Surface", "args": {"func": "sin(x)*cos(y)", "resolution": 12, "color": [0.3, 0.6, 0.9], "fill_opacity": 1.0}},
         ], "animations": [], "background": [1, 1, 1]}
sc = ModelScene(model); sc.construct()
assert len(sc.objects_by_id["s"].subObjects) > 16
print("model Surface on axes OK (2-variable function renders)")
print("\nUNIFIED AXES / SURFACE TESTS PASSED")
