import numpy as np
from .AnimObject import AnimObject
from .simpleShape import Line, Polygon
from .constants import RIGHT, UP, TOWARDS, ORIGIN, BLACK

# 3D objects. All are built as meshes of flat faces (Polygons) or lines, so the existing renderer
# draws them with no 3D-specific code: in 3D the camera depth-sorts the faces (painter's algorithm)
# and the shape reads correctly from any orbit angle. Mapping: x -> RIGHT, y -> UP, z -> TOWARDS.


def _perp_basis(n):
    """Two unit vectors spanning the plane perpendicular to n."""
    n = np.asarray(n, dtype=float)
    n = n / (np.linalg.norm(n) + 1e-12)
    a = RIGHT if abs(np.dot(n, RIGHT)) < 0.9 else UP
    u = np.cross(n, a); u = u / (np.linalg.norm(u) + 1e-12)
    v = np.cross(n, u)
    return u, v


def _face(points, color, fill_opacity, stroke_width=1.0):
    poly = Polygon([np.asarray(p, dtype=float) for p in points])
    poly.color = color
    poly.fill_color = color
    poly.fill_opacity = fill_opacity
    poly.stroke_width = stroke_width
    return poly


class ThreeDAxes(AnimObject):
    """Three axis lines along RIGHT (x), UP (y) and TOWARDS (z). View with a 3D camera and orbit."""

    def __init__(self, length=3.0):
        super().__init__()
        L = float(length)
        for vec in (RIGHT, UP, TOWARDS):
            self.add(Line(-L * vec, L * vec))


class Surface(AnimObject):
    """A surface z = f(x, y) as a mesh of quad faces (x->RIGHT, y->UP, height along TOWARDS)."""

    def __init__(self, func, x_range=(-2.0, 2.0), y_range=(-2.0, 2.0), resolution=14,
                 color=(0.35, 0.60, 0.92), fill_opacity=0.75):
        super().__init__()
        n = int(resolution)
        xs = np.linspace(x_range[0], x_range[1], n + 1)
        ys = np.linspace(y_range[0], y_range[1], n + 1)

        def P(x, y):
            return x * RIGHT + y * UP + float(func(x, y)) * TOWARDS

        for i in range(n):
            for j in range(n):
                self.add(_face([P(xs[i], ys[j]), P(xs[i + 1], ys[j]),
                                P(xs[i + 1], ys[j + 1]), P(xs[i], ys[j + 1])], color, fill_opacity))


class Box(AnimObject):
    """An axis-aligned cuboid: width along x (RIGHT), height UP along z (TOWARDS, the vertical screen
    axis), depth along y (UP). Height is the z-axis so the box stands upright in the z-up world."""

    def __init__(self, width=2.0, height=1.0, depth=1.0, center=ORIGIN,
                 color=(0.35, 0.60, 0.92), fill_opacity=0.5):
        super().__init__()
        c = np.asarray(center, dtype=float)
        hx = (width / 2.0) * RIGHT
        hy = (height / 2.0) * TOWARDS            # height -> vertical (world z)
        hz = (depth / 2.0) * UP                  # depth  -> horizontal (world y)
        corner = {(sx, sy, sz): c + sx * hx + sy * hy + sz * hz
                  for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)}
        faces = [
            [(1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1)],      # +x
            [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)],  # -x
            [(-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, 1, -1)],      # +y
            [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)],  # -y
            [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)],      # +z
            [(-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1)],  # -z
        ]
        for f in faces:
            self.add(_face([corner[k] for k in f], color, fill_opacity))


class Cube(Box):
    def __init__(self, side=1.0, center=ORIGIN, color=(0.35, 0.60, 0.92), fill_opacity=0.5):
        super().__init__(side, side, side, center, color, fill_opacity)


class Sphere(AnimObject):
    """A sphere as a latitude/longitude quad mesh (pole along the vertical z-axis / TOWARDS)."""

    def __init__(self, radius=1.0, center=ORIGIN, resolution=12,
                 color=(0.35, 0.60, 0.92), fill_opacity=0.5):
        super().__init__()
        c = np.asarray(center, dtype=float)
        r = float(radius)
        n = int(resolution)
        thetas = np.linspace(0, np.pi, n + 1)            # polar angle from the z (vertical) pole
        phis = np.linspace(0, 2 * np.pi, 2 * n + 1)      # azimuth in the x-y plane

        def P(t, p):
            return c + r * (np.sin(t) * np.cos(p) * RIGHT + np.sin(t) * np.sin(p) * UP + np.cos(t) * TOWARDS)

        for i in range(n):
            for j in range(2 * n):
                self.add(_face([P(thetas[i], phis[j]), P(thetas[i + 1], phis[j]),
                                P(thetas[i + 1], phis[j + 1]), P(thetas[i], phis[j + 1])], color, fill_opacity))


class Pyramid(AnimObject):
    """A square-based pyramid: base in the x-y ground plane (RIGHT/UP), apex pointing up the z-axis."""

    def __init__(self, base=2.0, height=2.0, center=ORIGIN,
                 color=(0.35, 0.60, 0.92), fill_opacity=0.5):
        super().__init__()
        c = np.asarray(center, dtype=float)
        b = base / 2.0
        bottom = c - (height / 2.0) * TOWARDS        # base sits below, apex rises along +z
        apex = c + (height / 2.0) * TOWARDS
        corners = [bottom + sx * b * RIGHT + sy * b * UP
                   for sx, sy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
        self.add(_face(corners, color, fill_opacity))                      # base
        for i in range(4):
            self.add(_face([corners[i], corners[(i + 1) % 4], apex], color, fill_opacity))  # sides


class Vector(AnimObject):
    """An arrow from start to end (a line shaft + a cone tip). Works in 2D (z=0) and 3D."""

    def __init__(self, end=RIGHT, start=ORIGIN, color=BLACK, stroke_width=4.0):
        super().__init__()
        s = np.asarray(start, dtype=float)
        e = np.asarray(end, dtype=float)
        shaft = Line(s, e)
        shaft.color = color
        shaft.stroke_width = stroke_width
        self.add(shaft)
        d = e - s
        L = float(np.linalg.norm(d))
        if L > 1e-9:
            direction = d / L
            head = min(0.28, 0.3 * L)
            rb = head * 0.45
            base_c = e - head * direction
            u, v = _perp_basis(direction)
            ring = [base_c + rb * (np.cos(a) * u + np.sin(a) * v)
                    for a in np.linspace(0, 2 * np.pi, 9)[:-1]]
            for i in range(len(ring)):
                tri = _face([ring[i], ring[(i + 1) % len(ring)], e], color, 1.0)   # cone side
                self.add(tri)
            self.add(_face(ring, color, 1.0))                                      # cone base cap
