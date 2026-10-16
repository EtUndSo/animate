import numpy as np
from .AnimObject import AnimObject
from .bezier import circle_points, line_points
from .plotting import plot_graph
from .constants import ORIGIN, RIGHT, UP

# Every shape stores its geometry as a cubic Bézier point array (N = 3k+1), so the renderer
# only ever handles ONE format. Straight-edged shapes go through line_points(); the circle
# (and the dot) use circle_points().


class Circle(AnimObject):
    def __init__(self, center=ORIGIN, radius=1.0):
        super().__init__()
        self.points = circle_points(center, radius, RIGHT, UP)


class Dot(Circle):
    # A dot is just a small filled circle - that keeps everything Bézier-based.
    def __init__(self, center=ORIGIN, radius=0.08):
        super().__init__(center, radius)
        self.fill_opacity = 1.0


class Line(AnimObject):
    def __init__(self, start, end):
        super().__init__()
        self.points = line_points([start, end])     # one straight Bézier segment -> (4,3)


class Polygon(AnimObject):
    def __init__(self, vertices=None, closed=True):
        super().__init__()
        if vertices is not None:
            verts = [np.asarray(v, dtype=float) for v in vertices]
            if closed:
                verts.append(verts[0])              # repeat first vertex to close the outline
            self.points = line_points(verts)


class Triangle(Polygon):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError(f"Triangle needs 3 points but received {len(vertices)}")
        super().__init__(vertices)


class Rectangle(Polygon):
    def __init__(self, center=ORIGIN, height=1.0, width=2.0):
        center = np.asarray(center, dtype=float)
        hw = (width / 2.0) * RIGHT                  # half-width vector along RIGHT
        hh = (height / 2.0) * UP                    # half-height vector along UP
        corners = [center - hw - hh,                # bottom-left
                   center + hw - hh,                # bottom-right
                   center + hw + hh,                # top-right
                   center - hw + hh]                # top-left
        super().__init__(corners)


class Square(Rectangle):
    def __init__(self, center=ORIGIN, side=1.0):
        super().__init__(center, side, side)        # a square is a rectangle with equal sides


class FunctionGraph(AnimObject):
    # Standalone graph in WORLD coordinates (data = world). For a scaled/framed plot use
    # Axes.plot(func) instead, which maps data coordinates through the axes.
    def __init__(self, func, x_range=(-4.0, 4.0), **_):
        super().__init__()
        x0, x1 = x_range[0], x_range[1]
        # GeoGebra-style combined sampling (data = world here); split at discontinuities.
        segments = plot_graph(func, x0, x1, lambda x, y: x * RIGHT + y * UP, x1 - x0)
        if segments:
            self.points = segments[0]
            for seg in segments[1:]:                  # extra continuous pieces (after poles) as children
                child = AnimObject()
                child.points = seg
                self.add(child)
