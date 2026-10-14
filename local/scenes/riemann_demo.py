import numpy as np
from engine.scene import Scene
from engine.axes import Axes
from engine.AnimObject import AnimObject
from engine.animation import Refine
from engine.constants import BLUE, RED


class RiemannDemo(Scene):
    def construct(self):
        func = lambda x: 3 * np.exp(-(x - 2) ** 2)            # a smooth, positive bump
        axes = Axes(x_range=(0, 4, 1), y_range=(0, 3, 1), x_length=10.0, y_length=6.0)

        rects = AnimObject()                                  # empty container (filled by Refine)
        graph = axes.plot(func, color=BLUE)
        self.add(axes, rects, graph)                          # order: rectangles under the graph

        # 1 -> 20 rectangles, each centered on its x (midpoint rule), approximating the area
        self.play(Refine(rects, lambda n: axes.riemann_rectangles(func, n, color=RED), n=20),
                  run_time=5.0)
        self.wait(1.0)
