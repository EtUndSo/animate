import numpy as np
from .AnimObject import AnimObject
from .simpleShape import Line, Polygon
from .text import Text
from .bezier import line_points
from .constants import RIGHT, UP, DOWN, LEFT


def _fmt(value):
    """Format a tick value compactly: 6, -1.5, 0.5 (no trailing zeros)."""
    return f"{value:g}"


class Axes(AnimObject):
    """A 2D coordinate system.

    It owns the mapping from DATA coordinates (the numbers a graph is defined in, e.g. x
    from -6 to 6) to WORLD coordinates (the units the renderer draws in). Plot graphs on it
    with axes.plot(func); they then automatically use this scale and fit the frame.

    Which parts are built is controlled by flags: show_ticks, show_numbers, show_labels
    (and the label strings x_label / y_label). That is the general pattern - a composite
    object exposes a setting for each element it contains.
    """

    def __init__(self, x_range=(-5, 5, 1), y_range=(-3, 3, 1),
                 x_length=10.0, y_length=6.0, tick_size=0.1,
                 show_ticks=True, show_numbers=True, show_labels=True,
                 x_label="x", y_label="y",
                 number_size=24, label_size=34):
        super().__init__()
        self.x_min, self.x_max, self.x_step = x_range
        self.y_min, self.y_max, self.y_step = y_range
        self.x_length = x_length
        self.y_length = y_length

        # Axis lines run through the data origin (clamped into the visible range).
        x0 = min(max(0.0, self.x_min), self.x_max)
        y0 = min(max(0.0, self.y_min), self.y_max)
        self.add(Line(self.coords_to_point(self.x_min, y0), self.coords_to_point(self.x_max, y0)))
        self.add(Line(self.coords_to_point(x0, self.y_min), self.coords_to_point(x0, self.y_max)))

        # Tick marks.
        if show_ticks:
            for x in self._ticks(self.x_min, self.x_max, self.x_step):
                p = self.coords_to_point(x, y0)
                self.add(Line(p - tick_size * UP, p + tick_size * UP))
            for y in self._ticks(self.y_min, self.y_max, self.y_step):
                p = self.coords_to_point(x0, y)
                self.add(Line(p - tick_size * RIGHT, p + tick_size * RIGHT))

        # Numbers at the ticks (as Text). Shown by default; hide them all with show_numbers=False.
        if show_numbers:
            number_offset = tick_size + 0.22
            for x in self._ticks(self.x_min, self.x_max, self.x_step):
                if x == 0:
                    continue                                   # the origin gets a single "0" below
                pos = self.coords_to_point(x, y0) + DOWN * number_offset
                self.add(Text(_fmt(x), pos, font_size=number_size))
            for y in self._ticks(self.y_min, self.y_max, self.y_step):
                if y == 0:
                    continue
                pos = self.coords_to_point(x0, y) + LEFT * number_offset
                self.add(Text(_fmt(y), pos, font_size=number_size))
            # a single "0" at the origin (offset diagonally so it clears both axes)
            if self.x_min <= 0 <= self.x_max and self.y_min <= 0 <= self.y_max:
                pos = self.coords_to_point(0, 0) + (DOWN + LEFT) * number_offset
                self.add(Text("0", pos, font_size=number_size))

        # Axis labels (e.g. "x" and "y") at the ends of the axes.
        if show_labels:
            if x_label:
                self.add(Text(x_label, self.coords_to_point(self.x_max, y0) + RIGHT * 0.35,
                              font_size=label_size))
            if y_label:
                self.add(Text(y_label, self.coords_to_point(x0, self.y_max) + UP * 0.35,
                              font_size=label_size))

    @staticmethod
    def _ticks(lo, hi, step):
        """All multiples of step within [lo, hi]."""
        first = int(np.ceil(lo / step))
        last = int(np.floor(hi / step))
        return [k * step for k in range(first, last + 1)]

    def coords_to_point(self, x, y):
        """Map a data coordinate (x, y) to a world point (the core data->world mapping)."""
        px = (x - self.x_min) / (self.x_max - self.x_min) * self.x_length - self.x_length / 2.0
        py = (y - self.y_min) / (self.y_max - self.y_min) * self.y_length - self.y_length / 2.0
        return px * RIGHT + py * UP

    def plot(self, func, samples=200, color=(0.35, 0.60, 0.92)):
        """Create a graph of y = func(x), mapped onto this coordinate system."""
        xs = np.linspace(self.x_min, self.x_max, samples)
        anchors = [self.coords_to_point(x, func(x)) for x in xs]
        graph = AnimObject()
        graph.points = line_points(anchors)       # OPEN Bézier chain (a graph never closes)
        graph.color = color
        return graph

    def riemann_rectangles(self, func, count, color=(0.35, 0.60, 0.92), fill_opacity=0.5):
        """Return a group of `count` rectangles approximating the area under func by the
        MIDPOINT rule: each rectangle is centered at its sample x, with height func(x_center)."""
        group = AnimObject()
        dx = (self.x_max - self.x_min) / count
        for i in range(count):
            xc = self.x_min + (i + 0.5) * dx            # center x (midpoint rule)
            h = func(xc)
            rect = Polygon([self.coords_to_point(xc - dx / 2, 0),
                            self.coords_to_point(xc + dx / 2, 0),
                            self.coords_to_point(xc + dx / 2, h),
                            self.coords_to_point(xc - dx / 2, h)])
            rect.color = color
            rect.fill_opacity = fill_opacity
            group.add(rect)
        return group
