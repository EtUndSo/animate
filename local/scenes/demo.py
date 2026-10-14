import numpy as np
from engine.scene import Scene
from engine.axes import Axes


class Demo(Scene):
    def construct(self):
        axes = Axes(x_range=(-6, 6, 1), y_range=(-1.5, 1.5, 0.5),
                    x_length=12.0, y_length=5.0)
        graph = axes.plot(lambda x: np.sin(x))
        self.add(axes, graph)
