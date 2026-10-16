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
                 show_ticks=True, show_numbers=True, show_labels=True, show_grid=True,
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

        # Background coordinate grid: light lines at every tick, spanning the range. Shown by default;
        # it is rebuilt from the ticks on every (re)build, so it grows/shrinks automatically with the
        # range. Added FIRST (so the axis lines/ticks sit over it) and tagged so it follows the same
        # axes_on_top setting as the rest of the axes.
        if show_grid:
            grid = AnimObject()
            for x in self._ticks(self.x_min, self.x_max, self.x_step):
                grid.add(Line(self.coords_to_point(x, self.y_min), self.coords_to_point(x, self.y_max)))
            for y in self._ticks(self.y_min, self.y_max, self.y_step):
                grid.add(Line(self.coords_to_point(self.x_min, y), self.coords_to_point(self.x_max, y)))
            for ln in grid.subObjects:
                ln.color = (0.85, 0.86, 0.90)
                ln.stroke_width = 1.0
            grid._is_grid = True
            self.add(grid)

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

    def plot_surface(self, func, resolution=18, color=(0.35, 0.60, 0.92), fill_opacity=1.0, shade=True,
                     grid_color=None, grid_width=0.5, res_min=6, adaptive=True):
        """Surface z = func(x, y) as a CURVATURE-ADAPTIVE quad mesh (GeoGebra-style): start from a coarse
        grid and recursively subdivide a cell where the surface BENDS. Flat regions stay coarse, curved
        regions get fine - fewer faces for the same look than a uniform grid. `res_min` = the MINIMUM
        cells per axis forced everywhere (a floor against faceting even on flat parts); `resolution` =
        the MAXIMUM cells per axis (the finest adaptive level). With shade=True each face is
        Lambert-shaded; faces whose z leaves the box are dropped (no plateau)."""
        x0a, x1a, y0a, y1a = self.x_min, self.x_max, self.y_min, self.y_max
        zlo, zhi = self.z_min, self.z_max
        maxn = max(2, int(resolution))
        minn = min(maxn, max(1, int(res_min)))
        base = 2                                                # coarse starting grid (per axis)
        min_depth = max(0, int(np.ceil(np.log2(max(1.0, minn / base)))))   # forced everywhere
        max_depth = min(8, max(min_depth, int(np.floor(np.log2(max(1.0, maxn / base))))))
        tol = 0.008 * (zhi - zlo if zhi > zlo else 1.0)         # flatness tolerance in z units (smaller = finer;
        #   0.008 makes curved regions - a Gaussian hill/slope - actually subdivide while truly flat parts stay
        #   coarse; 0.02 was too loose so slopes looked as coarse as the flat background)

        def _z(x, y):
            try:
                return float(func(x, y))
            except Exception:
                return float("nan")

        def _flat(ax, ay, bx, by):
            z = [_z(ax, ay), _z(bx, ay), _z(bx, by), _z(ax, by)]   # corners
            if not all(np.isfinite(z)):
                return False
            cx, cy = (ax + bx) / 2, (ay + by) / 2
            checks = [(_z(cx, cy), sum(z) / 4),                     # centre vs corner average
                      (_z(cx, ay), (z[0] + z[1]) / 2), (_z(cx, by), (z[3] + z[2]) / 2),
                      (_z(ax, cy), (z[0] + z[3]) / 2), (_z(bx, cy), (z[1] + z[2]) / 2)]   # edge mids
            return all(np.isfinite(s) and abs(s - est) <= tol for s, est in checks)

        leaves = []
        if not adaptive:                                        # STATIC: a plain uniform resolution×resolution grid
            xs = np.linspace(x0a, x1a, maxn + 1)
            ys = np.linspace(y0a, y1a, maxn + 1)
            leaves = [(xs[i], ys[j], xs[i + 1], ys[j + 1]) for i in range(maxn) for j in range(maxn)]
        else:                                                   # ADAPTIVE: curvature quadtree (res_min floor, res_max cap)
            def recurse(ax, ay, bx, by, depth):
                force = depth < min_depth                       # below res_min: always subdivide (floor)
                if force or (depth < max_depth and not _flat(ax, ay, bx, by)):
                    mx, my = (ax + bx) / 2, (ay + by) / 2
                    recurse(ax, ay, mx, my, depth + 1); recurse(mx, ay, bx, my, depth + 1)
                    recurse(ax, my, mx, by, depth + 1); recurse(mx, my, bx, by, depth + 1)
                else:
                    leaves.append((ax, ay, bx, by))
            xs = np.linspace(x0a, x1a, base + 1)
            ys = np.linspace(y0a, y1a, base + 1)
            for i in range(base):
                for j in range(base):
                    recurse(xs[i], ys[j], xs[i + 1], ys[j + 1], 0)

        light = np.array([0.4, 0.6, 0.75]); light = light / np.linalg.norm(light)
        basecol = np.asarray(color, dtype=float)
        span = (x1a - x0a) + (y1a - y0a)
        group = AnimObject()

        def _ok(z):
            return (z == z) and (zlo <= z <= zhi)

        # STITCH T-junctions: index every leaf corner so a coarse cell can insert the "hanging" vertices
        # a finer neighbour put on its shared edge -> adjacent cells use identical edge vertices (no cracks).
        R = lambda v: round(float(v), 7)
        xs_at_y, ys_at_x = {}, {}
        for (ax, ay, bx, by) in leaves:
            for px, py in ((ax, ay), (bx, ay), (bx, by), (ax, by)):
                xs_at_y.setdefault(R(py), set()).add(px)
                ys_at_x.setdefault(R(px), set()).add(py)
        eps = 1e-9
        def _h(y, lo, hi):
            return sorted(x for x in xs_at_y.get(R(y), ()) if lo + eps < x < hi - eps)
        def _v(x, lo, hi):
            return sorted(y for y in ys_at_x.get(R(x), ()) if lo + eps < y < hi - eps)

        for (ax, ay, bx, by) in leaves:
            verts2d = [(ax, ay)]                                 # CCW perimeter with hanging nodes inserted
            verts2d += [(x, ay) for x in _h(ay, ax, bx)]
            verts2d.append((bx, ay))
            verts2d += [(bx, y) for y in _v(bx, ay, by)]
            verts2d.append((bx, by))
            verts2d += [(x, by) for x in reversed(_h(by, ax, bx))]
            verts2d.append((ax, by))
            verts2d += [(ax, y) for y in reversed(_v(ax, ay, by))]
            zs = [_z(x, y) for (x, y) in verts2d]
            if not all(_ok(z) for z in zs):                      # any vertex out of the box -> drop the face
                continue
            P = [self.coords_to_point(x, y, z) for (x, y), z in zip(verts2d, zs)]
            nrm = np.cross(P[1] - P[0], P[2] - P[0])             # normal from the first corner triangle
            nn = np.linalg.norm(nrm)
            nrm = nrm / nn if nn > 1e-12 else np.array([0.0, 0.0, 1.0])
            if nrm[2] < 0:
                nrm = -nrm
            bright = (0.4 + 0.6 * max(0.0, float(np.dot(nrm, light)))) if shade else 1.0
            fc = tuple(float(min(1.0, c * bright)) for c in basecol)
            quad = Polygon(P)
            quad.fill_color = fc
            # mesh (raster) lines = the quad edges: own colour+width if given, else the fill colour
            # (invisible, just covers seams). grid_color lets the mesh show; grid_width sets thickness.
            quad.color = tuple(grid_color) if grid_color is not None else fc
            quad.fill_opacity = fill_opacity; quad.stroke_width = float(grid_width)
            quad._diag = (ax + bx) / 2 - x0a + (ay + by) / 2 - y0a   # centroid diagonal -> Create wavefront
            group.add(quad)
        group._surface_max_diag = span
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
