import numpy as np
from engine.scene import Scene
from engine.axes import Axes
from engine.renderer import paint_scene
from canvas_painter import CanvasPainter

# js_ctx / js_w / js_h are provided from JavaScript (pyodide.globals.set in main.js).
painter = CanvasPainter(js_ctx, js_w, js_h)

scene = Scene()
axes = Axes(x_range=(-6, 6, 1), y_range=(-1.5, 1.5, 0.5), x_length=12.0, y_length=5.0)
graph = axes.plot(lambda x: np.sin(x), color=(0.35, 0.60, 0.92))
scene.add(axes, graph)

paint_scene(painter, scene.objectList, scene.camera)   # same core, Canvas backend
