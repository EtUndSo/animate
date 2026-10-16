import numpy as np
from .AnimObject import AnimObject
from .simpleShape import Line, Polygon
from .text import Text
from .bezier import line_points
from .plotting import plot_graph, build_graph
from .constants import RIGHT, UP, DOWN, LEFT, TOWARDS, FRAME_HEIGHT, PIXEL_WIDTH, PIXEL_HEIGHT


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

    def __init__(self, x_range=(-10, 10), y_range=(-10, 10), z_range=(-10, 10),
                 x_length=7.0, y_length=7.0, z_length=7.0, tick_size=0.1,
                 show_ticks=True, show_numbers=True, show_labels=True,
                 grid_x=False, grid_y=False, grid_z=False,
                 grid_color=(0.0, 0.0, 0.0), grid_width=1.0,
                 x_color=(0.0, 0.0, 0.0), y_color=(0.0, 0.0, 0.0), z_color=(0.0, 0.0, 0.0),
                 x_label="x", y_label="y", z_label="z",
                 number_size=24, label_size=34, zoom=1.0, dynamic_ticks=False):
        super().__init__()
        self._is_axis = True                                 # renderer draws axes on TOP of everything
        self.x_min, self.x_max = x_range[0], x_range[1]
        self.y_min, self.y_max = y_range[0], y_range[1]
        self.z_min, self.z_max = z_range[0], z_range[1]
        self.x_length = x_length
        self.y_length = y_length
        self.z_length = z_length
        number_offset = tick_size + 0.22

        # Tick step + the tick WINDOW per axis. Normally ticks span the whole range at a nice step.
        # With dynamic_ticks (2D) and zoom>1 the step REFINES and the ticks are limited to the visible
        # window (centred on the origin), so zooming in shows finer numbers (…, 1, 2, …) instead of the
        # same coarse step - and the tick count stays bounded.
        frame_w = FRAME_HEIGHT * PIXEL_WIDTH / PIXEL_HEIGHT
        def _axis_ticks(lo, hi, length, frame_extent, explicit):
            if explicit:
                return explicit, lo, hi
            span = hi - lo
            if dynamic_ticks and zoom > 1.0001 and span > 0 and length > 0:
                vis = min(span, max(span / 500.0, frame_extent * span / length / zoom))  # visible data span
                step = _nice_step(0.0, vis)
                half = min(span / 2.0, vis * 0.6)
                c = min(max(0.0, lo), hi)                     # origin, clamped into range
                return step, max(lo, c - half), min(hi, c + half)
            return _nice_step(lo, hi), lo, hi
        self.x_step, self._x_tlo, self._x_thi = _axis_ticks(self.x_min, self.x_max, x_length, frame_w, x_range[2] if len(x_range) > 2 and x_range[2] else None)
        self.y_step, self._y_tlo, self._y_thi = _axis_ticks(self.y_min, self.y_max, y_length, FRAME_HEIGHT, y_range[2] if len(y_range) > 2 and y_range[2] else None)
        self.z_step, self._z_tlo, self._z_thi = _axis_ticks(self.z_min, self.z_max, z_length, FRAME_HEIGHT, z_range[2] if len(z_range) > 2 and z_range[2] else None)

        # Background coordinate grid, TOGGLEABLE PER AXIS (grid_x / grid_y / grid_z, all off by default).
        # It rebuilds from the ticks on every (re)build, so it grows/shrinks with the range. Tagged
        # `_is_grid` so the renderer depth-sorts it (it sits in the plane, not on top of objects).
        def _grid_group(lines, only_3d=False):
            g = AnimObject()
            for p0, p1 in lines:
                ln = Line(p0, p1); ln.color = tuple(grid_color); ln.stroke_width = float(grid_width)
                g.add(ln)
            g._is_grid = True
            if only_3d:
                g._only_3d = True
            return g
        if grid_x:                                          # lines at each x value (parallel to the y-axis)
            self.add(_grid_group([(self.coords_to_point(x, self.y_min), self.coords_to_point(x, self.y_max))
                                  for x in self._ticks(self._x_tlo, self._x_thi, self.x_step)]))
        if grid_y:                                          # lines at each y value (parallel to the x-axis)
            self.add(_grid_group([(self.coords_to_point(self.x_min, y), self.coords_to_point(self.x_max, y))
                                  for y in self._ticks(self._y_tlo, self._y_thi, self.y_step)]))
        if grid_z:                                          # 3D only: z grid on the back wall (y = y_min)
            yw = self.y_min
            lines = [(self.coords_to_point(self.x_min, yw, z), self.coords_to_point(self.x_max, yw, z))
                     for z in self._ticks(self._z_tlo, self._z_thi, self.z_step)]            # per z (parallel x)
            lines += [(self.coords_to_point(x, yw, self.z_min), self.coords_to_point(x, yw, self.z_max))
                      for x in self._ticks(self._x_tlo, self._x_thi, self.x_step)]           # per x (parallel z)
            self.add(_grid_group(lines, only_3d=True))

        # Axis lines run through the data origin (clamped into the visible range). Each axis gets its
        # classic colour (x=red, y=green, z=blue), so orientation is readable at a glance.
        x0 = min(max(0.0, self.x_min), self.x_max)
        y0 = min(max(0.0, self.y_min), self.y_max)
        xax = Line(self.coords_to_point(self.x_min, y0), self.coords_to_point(self.x_max, y0)); xax.color = tuple(x_color)
        yax = Line(self.coords_to_point(x0, self.y_min), self.coords_to_point(x0, self.y_max)); yax.color = tuple(y_color)
        self.add(xax); self.add(yax)

        # Tick marks (coloured to match their axis).
        if show_ticks:
            for x in self._ticks(self._x_tlo, self._x_thi, self.x_step):
                p = self.coords_to_point(x, y0)
                t = Line(p - tick_size * UP, p + tick_size * UP); t.color = tuple(x_color); self.add(t)
            for y in self._ticks(self._y_tlo, self._y_thi, self.y_step):
                p = self.coords_to_point(x0, y)
                t = Line(p - tick_size * RIGHT, p + tick_size * RIGHT); t.color = tuple(y_color); self.add(t)

        # Numbers at the ticks (as Text). Shown by default; hide them all with show_numbers=False.
        if show_numbers:
            for x in self._ticks(self._x_tlo, self._x_thi, self.x_step):
                if x == 0:
                    continue                                   # the origin gets a single "0" below
                pos = self.coords_to_point(x, y0) + DOWN * number_offset
                self.add(Text(_fmt(x), pos, font_size=number_size))
            for y in self._ticks(self._y_tlo, self._y_thi, self.y_step):
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
                lx = Text(x_label, self.coords_to_point(self.x_max, y0) + RIGHT * 0.35, font_size=label_size)
                lx.color = tuple(x_color); self.add(lx)
            if y_label:
                ly = Text(y_label, self.coords_to_point(x0, self.y_max) + UP * 0.35, font_size=label_size)
                ly.color = tuple(y_color); self.add(ly)

        # z-axis: built the same way, but grouped and tagged _only_3d so it is HIDDEN in the 2D view
        # (looking at the x-y plane) and appears, fully labelled, as soon as you orbit into 3D.
        z0 = min(max(0.0, self.z_min), self.z_max)
        zg = AnimObject()
        zln = Line(self.coords_to_point(x0, y0, self.z_min), self.coords_to_point(x0, y0, self.z_max))
        zln.color = tuple(z_color); zg.add(zln)
        if show_ticks:
            for z in self._ticks(self._z_tlo, self._z_thi, self.z_step):
                p = self.coords_to_point(x0, y0, z)
                t = Line(p - tick_size * RIGHT, p + tick_size * RIGHT); t.color = tuple(z_color); zg.add(t)
        if show_numbers:
            for z in self._ticks(self._z_tlo, self._z_thi, self.z_step):
                if z == 0:
                    continue
                zg.add(Text(_fmt(z), self.coords_to_point(x0, y0, z) + LEFT * number_offset, font_size=number_size))
        if show_labels and z_label:
            zlab = Text(z_label, self.coords_to_point(x0, y0, self.z_max) + TOWARDS * 0.35, font_size=label_size)
            zlab.color = tuple(z_color); zg.add(zlab)
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

    def plot(self, func, color=(0.35, 0.60, 0.92), x_range=None, y_range=None, **_):
        """Graph of y = func(x) on this coordinate system, sampled with GeoGebra-style combined
        sampling (plotting.plot_graph): adaptive, anti-aliased-looking, split at discontinuities.
        `x_range` limits the plotted DOMAIN (clamped to the axes); `y_range` clips VERTICALLY - values
        outside it are dropped (the curve splits there), which tames poles/steep parts."""
        xlo, xhi = self.x_min, self.x_max
        if x_range:
            xlo = max(self.x_min, float(x_range[0]))
            xhi = min(self.x_max, float(x_range[1]))
            if xhi <= xlo:
                xlo, xhi = self.x_min, self.x_max           # nonsensical range -> fall back to the full axis
        f = func
        if y_range:
            ylo, yhi = float(y_range[0]), float(y_range[1])
            def f(x, _g=func, _lo=ylo, _hi=yhi):
                v = _g(x)
                return v if (v == v and _lo <= v <= _hi) else float("nan")   # NaN -> plot_graph splits (clip)
        segments = plot_graph(f, xlo, xhi, self.coords_to_point, self.x_length)
        return build_graph(segments, color)

    def plot_surface(self, func, resolution=18, color=(0.35, 0.60, 0.92), fill_opacity=1.0, shade=True,
                     grid_color=None, grid_width=0.5, res_min=15, adaptive=True, height_color=False):
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

        # Height (depth) colouring: the chosen colour is the value AT z=0; above it the colour lightens
        # toward white, below it it darkens toward black — hue kept, so the surface reads like a height map.
        _white = np.array([1.0, 1.0, 1.0])
        _AMT = 0.70                                          # how far to push toward white/black at the extremes
        def _height_base(zc):
            if not height_color:
                return basecol
            if zc >= 0:
                t = min(1.0, zc / (zhi if zhi > 1e-9 else 1.0))
                return basecol + (_white - basecol) * (_AMT * t)     # lighter above
            s = min(1.0, (-zc) / (-zlo if zlo < -1e-9 else 1.0))
            return basecol * (1.0 - _AMT * s)                        # darker below

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
            # Face normal via NEWELL'S method over the WHOLE polygon (robust for any vertex count and for
            # the hanging-node vertices stitching inserts). The old cross(P1-P0, P2-P0) used just the first
            # three perimeter points, which on a stitched edge are ~collinear -> garbage normal -> adjacent
            # faces flipped between very dark and very bright instead of a smooth gradient.
            Pa = np.asarray(P, dtype=float)
            Pb = np.roll(Pa, -1, axis=0)
            nrm = np.array([
                float(np.sum((Pa[:, 1] - Pb[:, 1]) * (Pa[:, 2] + Pb[:, 2]))),
                float(np.sum((Pa[:, 2] - Pb[:, 2]) * (Pa[:, 0] + Pb[:, 0]))),
                float(np.sum((Pa[:, 0] - Pb[:, 0]) * (Pa[:, 1] + Pb[:, 1]))),
            ])
            nn = np.linalg.norm(nrm)
            nrm = nrm / nn if nn > 1e-12 else np.array([0.0, 0.0, 1.0])
            if nrm[2] < 0:
                nrm = -nrm
            bright = (0.4 + 0.6 * max(0.0, float(np.dot(nrm, light)))) if shade else 1.0
            hbase = _height_base(sum(zs) / len(zs))          # face colour from its mean height (z), or flat
            # In height-colour mode the colour must encode HEIGHT alone, so Lambert shading is skipped —
            # otherwise the lighting darkens high faces and the "lighter above" reading is lost.
            fc = tuple(float(min(1.0, c * (1.0 if height_color else bright))) for c in hbase)
            quad = Polygon(P)
            quad.fill_color = fc
            # mesh (raster) lines = the quad edges: own colour+width if given, else the fill colour
            # (invisible, just covers seams). grid_color lets the mesh show; grid_width sets thickness.
            quad.color = tuple(grid_color) if grid_color is not None else fc
            quad.fill_opacity = fill_opacity; quad.stroke_width = float(grid_width)
            quad._diag = float(np.hypot((ax + bx) / 2 - (x0a + x1a) / 2,     # radial distance of the face centroid
                                        (ay + by) / 2 - (y0a + y1a) / 2))    # from the domain CENTRE -> Create reveals
            #                                                                   the surface growing OUTWARD from the middle
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
