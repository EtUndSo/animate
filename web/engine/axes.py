import numpy as np
from .AnimObject import AnimObject
from .simpleShape import Line, Polygon
from .text import Text
from .bezier import line_points
from .plotting import plot_graph, build_graph
from .constants import RIGHT, UP, DOWN, LEFT, TOWARDS


def _fmt(value):
    """Format a tick value compactly: 6, -1.5, 0.5 (no trailing zeros)."""
    return f"{value:g}"


def _nice_step(lo, hi, target=10):
    """A readable tick step (1, 2, 2.5 or 5 x 10^k) giving ~target ticks over [lo, hi].
    This is what makes the SUBDIVISION adapt to the range while the axes keeps a fixed
    on-screen size: -100..100 gets a step of 20 (11 ticks), not 200 ticks of 1 crammed together."""
    span = float(hi) - float(lo)
    if span <= 0:
        return 1.0
    raw = span / target                                  # the ideal step for ~target ticks
    mag = 10.0 ** np.floor(np.log10(raw))                # largest power of ten <= raw
    for m in (1.0, 2.0, 2.5, 5.0, 10.0):                 # snap up to a "nice" multiple of it
        if m * mag >= raw:
            return m * mag
    return 10.0 * mag


class Axes(AnimObject):
    """A 2D coordinate system.

    It owns the mapping from DATA coordinates (the numbers a graph is defined in, e.g. x
    from -6 to 6) to WORLD coordinates (the units the renderer draws in). Plot graphs on it
    with axes.plot(func); they then automatically use this scale and fit the frame.

    Size vs. range are independent: x_length / y_length fix the on-screen SIZE (world units),
    while x_range / y_range say which DATA values map onto it. So a huge range (-100..100) does
    NOT make the axes grow out of the frame - it just rescales. The tick step may be given as a
    third range entry; if omitted, it is chosen automatically (see _nice_step) so the subdivision
    stays readable at any range.

    Which parts are built is controlled by flags: show_ticks, show_numbers, show_labels
    (and the label strings x_label / y_label). That is the general pattern - a composite
    object exposes a setting for each element it contains.
    """

    def __init__(self, x_range=(-5, 5), y_range=(-3, 3), z_range=(-3, 3),
                 x_length=12.0, y_length=6.0, z_length=6.0, tick_size=0.1,
                 show_ticks=True, show_numbers=True, show_labels=True,
                 x_label="x", y_label="y", z_label="z",
                 number_size=24, label_size=34):
        super().__init__()
        self._is_axis = True                                 # renderer draws axes on TOP of everything
        self.x_min, self.x_max = x_range[0], x_range[1]
        self.y_min, self.y_max = y_range[0], y_range[1]
        self.z_min, self.z_max = z_range[0], z_range[1]
        # Third entry = explicit step; otherwise pick a nice step that adapts to the range.
        self.x_step = x_range[2] if len(x_range) > 2 and x_range[2] else _nice_step(self.x_min, self.x_max)
        self.y_step = y_range[2] if len(y_range) > 2 and y_range[2] else _nice_step(self.y_min, self.y_max)
        self.z_step = z_range[2] if len(z_range) > 2 and z_range[2] else _nice_step(self.z_min, self.z_max)
        self.x_length = x_length
        self.y_length = y_length
        self.z_length = z_length
        number_offset = tick_size + 0.22

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

        # z-axis: built the same way, but grouped and tagged _only_3d so it is HIDDEN in the 2D view
        # (looking at the x-y plane) and appears, fully labelled, as soon as you orbit into 3D.
        z0 = min(max(0.0, self.z_min), self.z_max)
        zg = AnimObject()
        zg.add(Line(self.coords_to_point(x0, y0, self.z_min), self.coords_to_point(x0, y0, self.z_max)))
        if show_ticks:
            for z in self._ticks(self.z_min, self.z_max, self.z_step):
                p = self.coords_to_point(x0, y0, z)
                zg.add(Line(p - tick_size * RIGHT, p + tick_size * RIGHT))
        if show_numbers:
            for z in self._ticks(self.z_min, self.z_max, self.z_step):
                if z == 0:
                    continue
                zg.add(Text(_fmt(z), self.coords_to_point(x0, y0, z) + LEFT * number_offset, font_size=number_size))
        if show_labels and z_label:
            zg.add(Text(z_label, self.coords_to_point(x0, y0, self.z_max) + TOWARDS * 0.35, font_size=label_size))
        zg._only_3d = True
        self.add(zg)

    @staticmethod
    def _ticks(lo, hi, step):
        """All multiples of step within [lo, hi]."""
        first = int(np.ceil(lo / step))
        last = int(np.floor(hi / step))
        return [k * step for k in range(first, last + 1)]

    def coords_to_point(self, x, y, z=0.0):
        """Map a data coordinate (x, y, z) to a world point (the core data->world mapping). z scales
        from the x-y plane (data z=0 -> world z=0), so 2D graphs stay on the plane and surfaces rise."""
        px = (x - self.x_min) / (self.x_max - self.x_min) * self.x_length - self.x_length / 2.0
        py = (y - self.y_min) / (self.y_max - self.y_min) * self.y_length - self.y_length / 2.0
        pz = z * (self.z_length / (self.z_max - self.z_min))
        return px * RIGHT + py * UP + pz * TOWARDS

    c2p = coords_to_point                                # Manim-style short alias

    def data_to_world(self, points):
        """Vectorised coords_to_point: map an (N,3) array of DATA coordinates to WORLD points
        with this axes' affine scale + offset. The depth (z) component is passed through."""
        pts = np.asarray(points, dtype=float).reshape(-1, 3)
        ax = self.x_length / (self.x_max - self.x_min)
        ay = self.y_length / (self.y_max - self.y_min)
        out = np.empty_like(pts)
        out[:, 0] = pts[:, 0] * ax - self.x_min * ax - self.x_length / 2.0
        out[:, 1] = pts[:, 1] * ay - self.y_min * ay - self.y_length / 2.0
        out[:, 2] = pts[:, 2]
        return out

    def place(self, obj):
        """Re-interpret obj's points as DATA coordinates and map them onto this axes (recursively).
        So an object built at data (1, 0) lands exactly on the tick '1', and its size scales with
        the axes - no matter the axes' fixed on-screen size. This is how the editor keeps objects
        aligned to the grid regardless of the chosen range."""
        if len(obj.points):
            obj.points = self.data_to_world(obj.points)
        for sub in obj.subObjects:
            self.place(sub)
        return obj

    def plot(self, func, color=(0.35, 0.60, 0.92), **_):
        """Graph of y = func(x) on this coordinate system, sampled with GeoGebra-style combined
        sampling (plotting.plot_graph): adaptive, anti-aliased-looking, split at discontinuities."""
        segments = plot_graph(func, self.x_min, self.x_max, self.coords_to_point, self.x_length)
        return build_graph(segments, color)

    def plot_surface(self, func, resolution=18, color=(0.35, 0.60, 0.92), fill_opacity=1.0, shade=True):
        """Surface z = func(x, y) over the axes' x/y ranges, mapped through coords_to_point so it sits
        in (and scales with) this coordinate system. With shade=True each quad face is LAMBERT-SHADED
        by its normal vs a fixed light (matplotlib/GeoGebra style) so the 3D form reads; with shade=False
        the surface is drawn FLAT (one colour, no 'shadows'). Faces are depth-sorted by the renderer."""
        n = int(resolution)
        xs = np.linspace(self.x_min, self.x_max, n + 1)
        ys = np.linspace(self.y_min, self.y_max, n + 1)
        zlo, zhi = self.z_min, self.z_max

        Z = [[float(func(xs[i], ys[j])) for j in range(n + 1)] for i in range(n + 1)]

        def _ok(z):
            """True if z is finite AND within the z-range. A face touching an out-of-range (or NaN)
            value is simply NOT DRAWN - no fake constant plateau at the boundary, the surface just ends."""
            return (z == z) and (zlo <= z <= zhi)

        light = np.array([0.4, 0.6, 0.75]); light = light / np.linalg.norm(light)
        base = np.asarray(color, dtype=float)
        group = AnimObject()
        for i in range(n):
            for j in range(n):
                z00, z10, z11, z01 = Z[i][j], Z[i + 1][j], Z[i + 1][j + 1], Z[i][j + 1]
                if not (_ok(z00) and _ok(z10) and _ok(z11) and _ok(z01)):
                    continue                                # any corner out of the box -> drop the face
                P = [self.coords_to_point(xs[i], ys[j], z00),
                     self.coords_to_point(xs[i + 1], ys[j], z10),
                     self.coords_to_point(xs[i + 1], ys[j + 1], z11),
                     self.coords_to_point(xs[i], ys[j + 1], z01)]
                nrm = np.cross(P[1] - P[0], P[2] - P[0])
                nn = np.linalg.norm(nrm)
                nrm = nrm / nn if nn > 1e-12 else np.array([0.0, 0.0, 1.0])
                if nrm[2] < 0:
                    nrm = -nrm                                  # orient normals upward (consistent shading)
                bright = (0.4 + 0.6 * max(0.0, float(np.dot(nrm, light)))) if shade else 1.0
                fc = tuple(float(min(1.0, c * bright)) for c in base)
                quad = Polygon(P)
                quad.color = fc
                quad.fill_color = fc
                quad.fill_opacity = fill_opacity
                quad.stroke_width = 0.5
                quad._diag = i + j                          # anti-diagonal rank -> Create reveals the
                group.add(quad)                             # surface as a growing triangular wavefront
        group._surface_max_diag = 2 * (n - 1)
        return group

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
