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


class ArrowHead(Polygon):
    """A flat, filled 2D arrowhead (triangle) with its TIP at `tip`, pointing along `direction`.
    `size` = length in world units; `width` = base width relative to the length. Cheap (one polygon)
    compared with Vector's 3D cone, so circuits/annotations can carry many of them."""
    def __init__(self, tip, direction, size=0.25, width=0.8):
        tip = np.asarray(tip, dtype=float)
        d = np.asarray(direction, dtype=float)
        n = float(np.linalg.norm(d))
        d = d / n if n > 1e-12 else RIGHT
        perp = np.array([-d[1], d[0], 0.0])
        back = tip - size * d
        super().__init__([tip, back + 0.5 * width * size * perp, back - 0.5 * width * size * perp])
        self.fill_opacity = 1.0
        self.stroke_width = 1.0
        self._no_dash = True


class Ellipse(AnimObject):
    """An axis-aligned ellipse: `width` along x, `height` along y (four Bézier arcs)."""
    def __init__(self, center=ORIGIN, width=2.0, height=1.0):
        super().__init__()
        c = np.asarray(center, dtype=float)
        self.points = circle_points(c, 1.0, RIGHT, UP)
        self.points = (self.points - c) * np.array([width / 2.0, height / 2.0, 1.0]) + c


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
