import sys, json
sys.path.insert(0, ".")   # run from web/
from engine.scene_model import ModelScene
from engine.renderer import paint_scene

class StubCtx:
    """Records attribute sets + method calls, like a Canvas 2D context."""
    def __init__(self): self.calls = []
    def __setattr__(self, k, v):
        if k == "calls": object.__setattr__(self, k, v)
        else: self.calls.append((k, v))
    def __getattr__(self, name):
        def m(*a): self.calls.append((name, a))
        return m

sys.path.insert(0, "py")
from canvas_painter import CanvasPainter

# EXACT default model the editor sends on boot (one Axes, white bg).
default = {
    "objects": [{"id": "o1", "type": "Axes",
                 "args": {"x_range": [-6, 6], "y_range": [-3, 3], "x_length": 12, "y_length": 6}}],
    "animations": [],
    "background": [1.0, 1.0, 1.0],
}

ctx = StubCtx()
painter = CanvasPainter(ctx, 1920, 1080)
scene = ModelScene(default)
scene.construct()
paint_scene(painter, scene.objectList, scene.camera, background=default["background"])
draws = sum(1 for c in ctx.calls if c[0] in ("stroke", "fill", "fillText"))
print("default scene: calls", len(ctx.calls), "draw ops", draws)
assert draws > 0, "nothing drawn!"

# Each template too.
import importlib.util
print("default render OK")
