import numpy as np
from engine.scene import Scene
from engine.axes import Axes
from engine.animation import Create
from engine.rate_functions import linear


class AnimDemo(Scene):
    def construct(self):
        axes = Axes(x_range=(-6, 6, 1), y_range=(-1.5, 1.5, 0.5),
                    x_length=12.0, y_length=5.0)
        graph = axes.plot(lambda x: np.sin(x))

        self.add(axes)                                        # static axes
        # draw the graph from smallest x to largest x, at a steady pace
        self.play(Create(graph, rate_func=linear), run_time=2.5)
        self.wait(0.5)
