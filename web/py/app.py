import numpy as np
from engine.scene import Scene
from engine.axes import Axes
from engine.simpleShape import Circle
from engine.animation import Create, GrowFromCenter, Shift
from engine.renderer import paint_scene
from engine.constants import RIGHT
from canvas_painter import CanvasPainter

# js_ctx / js_w / js_h come from JavaScript (pyodide.globals.set in main.js).
painter = CanvasPainter(js_ctx, js_w, js_h)


class WebDemo(Scene):
    def construct(self):
        axes = Axes(x_range=(-6, 6, 1), y_range=(-1.5, 1.5, 0.5), x_length=12.0, y_length=5.0)
        self.add(axes)

        graph = axes.plot(lambda x: np.sin(x), color=(0.35, 0.60, 0.92))
        self.play(Create(graph), run_time=2.0)               # draw the sine

        dot = Circle(center=axes.coords_to_point(-6, np.sin(-6)), radius=0.12)
        dot.color = (0.89, 0.29, 0.20)
        dot.fill_opacity = 1.0
        self.play(GrowFromCenter(dot), run_time=0.6)         # dot appears
        self.play(Shift(dot, RIGHT * 2.0), run_time=1.0)     # dot slides
        self.wait(0.6)


scene = WebDemo().build_timeline()
DURATION = scene.duration


def draw(t):
    """Called by the JS player each frame: set the scene to time t, paint to the Canvas."""
    scene.seek(t)
    paint_scene(painter, scene.objectList, scene.camera)
