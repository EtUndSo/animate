"""Declarative scene model.

A scene is described as plain data (objects + animations). This single representation is the
bridge for the web app: the visual editor edits it, we generate code from it (for the code
page), and the interpreter builds a renderable Scene from it (for the live preview / export).
So editor, code page, preview and export always stay in sync.
"""
import inspect
import re
import numpy as np

from .scene import Scene
from .camera import Camera
from .axes import Axes
from .simpleShape import (Circle, Dot, Line, Polygon, Triangle, Rectangle, Square, FunctionGraph)
from .text import Text, DecimalNumber
from .value_tracker import ValueTracker
from .threed import ThreeDAxes, Box, Cube, Sphere, Pyramid, Vector
from .svg import MathTex, SVGMobject
from .legend import Legend
from .AnimObject import AnimObject
from .results import result_value
from . import calc as _calc
from . import geometry as _geom
from . import processes as _proc
from . import arithmetic as _arith
from . import animation as _anim
from . import constants as _const

_ARITH = {"Addition", "Subtraction", "Multiplication", "Division"}


def _has_var(expr, v):
    return re.search(r"(?<![A-Za-z_0-9])" + v + r"(?![A-Za-z_0-9])", normalize_expr(expr)) is not None

def _is_surface(expr):
    """A FunctionGraph is a SURFACE only when it uses BOTH x and y (a function of two variables).
    'cos(y)' alone is still a one-variable curve (y is just its single variable)."""
    return _has_var(expr, "x") and _has_var(expr, "y")

def _surface_kw(args, style):
    """Collect the keyword args for axes.plot_surface: colour/opacity (from style), resolution (max
    mesh density) and the mesh-line look (grid_color / grid_width) from args."""
    kw = {k: style[k] for k in ("color", "fill_opacity") if k in style}
    if "res_max" in args:                                   # editor name for the maximum (engine: resolution)
        kw["resolution"] = int(args["res_max"])
    elif "resolution" in args:                              # back-compat with older scenes
        kw["resolution"] = int(args["resolution"])
    if "res_min" in args:
        kw["res_min"] = int(args["res_min"])
    if "adaptive" in args:
        kw["adaptive"] = bool(args["adaptive"])
    if "grid_width" in args:
        kw["grid_width"] = float(args["grid_width"])
    if "grid_color" in args:
        kw["grid_color"] = args["grid_color"]
    if "height_color" in args:                              # colour faces by height (z) instead of a flat tint
        kw["height_color"] = bool(args["height_color"])
    return kw


def _gl_surface_mesh(func2, axes, n):
    """WebGL-ready surface mesh in WORLD coordinates: positions + per-vertex (smooth) normals +
    triangle indices + a 0..1 height field. Uses the SAME affine mapping as coords_to_point so the
    GPU surface lines up pixel-perfect with the 2D-painted axes. Returns raw little-endian bytes
    (handed straight to typed arrays in JS)."""
    xs = np.linspace(axes.x_min, axes.x_max, n + 1)
    ys = np.linspace(axes.y_min, axes.y_max, n + 1)
    X, Y = np.meshgrid(xs, ys)
    try:                                                    # vectorised eval (sin/cos/exp/… over arrays)
        Z = np.asarray(func2(X, Y), dtype=float)
        if Z.shape != X.shape:
            raise ValueError
    except Exception:                                       # fall back to element-wise for odd functions
        Z = np.empty_like(X)
        for j in range(X.shape[0]):
            for i in range(X.shape[1]):
                try:
                    Z[j, i] = float(func2(X[j, i], Y[j, i]))
                except Exception:
                    Z[j, i] = np.nan
    Z = np.nan_to_num(Z, nan=0.0, posinf=0.0, neginf=0.0)
    z0, z1 = float(Z.min()), float(Z.max())
    ax = axes.x_length / (axes.x_max - axes.x_min)
    ay = axes.y_length / (axes.y_max - axes.y_min)
    az = axes.z_length / (axes.z_max - axes.z_min)
    pos = np.empty((X.size, 3), dtype=np.float32)
    pos[:, 0] = (X * ax - axes.x_min * ax - axes.x_length / 2.0).ravel()
    pos[:, 1] = (Y * ay - axes.y_min * ay - axes.y_length / 2.0).ravel()
    pos[:, 2] = (Z * az).ravel()
    m = n + 1
    rng = np.arange(n)
    ii, jj = np.meshgrid(rng, rng)
    a = (jj * m + ii).ravel()
    tris = np.empty((a.size, 6), dtype=np.int64)
    tris[:, 0] = a; tris[:, 1] = a + m; tris[:, 2] = a + 1          # two triangles per cell
    tris[:, 3] = a + 1; tris[:, 4] = a + m; tris[:, 5] = a + m + 1
    idx = tris.reshape(-1)
    t = idx.reshape(-1, 3)
    fn = np.cross(pos[t[:, 1]] - pos[t[:, 0]], pos[t[:, 2]] - pos[t[:, 0]])   # per-face normals
    nrm = np.zeros((pos.shape[0], 3), dtype=np.float64)
    np.add.at(nrm, t[:, 0], fn); np.add.at(nrm, t[:, 1], fn); np.add.at(nrm, t[:, 2], fn)
    ln = np.linalg.norm(nrm, axis=1, keepdims=True); ln[ln == 0] = 1.0
    nrm = (nrm / ln).astype(np.float32)
    zt = ((Z - z0) / (z1 - z0 + 1e-9)).ravel().astype(np.float32)
    return {"pos": pos.tobytes(), "nrm": nrm.tobytes(), "idx": idx.astype(np.uint16).tobytes(),
            "zt": zt.tobytes(), "count": int(idx.size), "z0": z0, "z1": z1}


def _gl_solid_mesh(obj, smooth=False, center=(0.0, 0.0, 0.0)):
    """WebGL mesh for a 3D SOLID (Box/Cube/Pyramid/Sphere) in world coords, from its face corners
    (stashed as poly._corners). Polyhedra get FLAT per-face normals (sharp edges); a sphere gets SMOOTH
    radial normals (smooth=True). Opaque — no depth sorting needed. u16 indices (solids are small)."""
    def faces(o):
        if getattr(o, "_corners", None) is not None:
            yield o
        for s in getattr(o, "subObjects", []):
            yield from faces(s)
    face_corners = [[np.asarray(c, dtype=float) for c in f._corners] for f in faces(obj)
                    if len(getattr(f, "_corners", [])) >= 3]
    if not face_corners:
        return None
    allpts = np.array([p for C in face_corners for p in C])
    gc = allpts.mean(axis=0)                                  # geometric centroid -> orient normals OUTWARD
    cen = np.asarray(center, dtype=float) if np.any(center) else gc   # sphere centre (smooth), else centroid
    verts, norms, idx = [], [], []
    for C in face_corners:
        nrm = np.zeros(3)                                    # Newell face normal (robust, any vertex count)
        for i in range(len(C)):
            a, b = C[i], C[(i + 1) % len(C)]
            nrm[0] += (a[1] - b[1]) * (a[2] + b[2])
            nrm[1] += (a[2] - b[2]) * (a[0] + b[0])
            nrm[2] += (a[0] - b[0]) * (a[1] + b[1])
        ln = np.linalg.norm(nrm); nrm = nrm / ln if ln > 1e-12 else np.array([0.0, 0.0, 1.0])
        fcent = np.mean(C, axis=0)                            # flip to point AWAY from the centroid (outward)
        if np.dot(nrm, fcent - gc) < 0:
            nrm = -nrm
        base = len(verts)
        for c in C:
            verts.append(c)
            if smooth:
                d = c - cen; dl = np.linalg.norm(d)
                norms.append(d / dl if dl > 1e-9 else nrm)
            else:
                norms.append(nrm)
        for k in range(1, len(C) - 1):                       # fan triangulation
            idx += [base, base + k, base + k + 1]
    if len(verts) < 3 or len(verts) >= 65536:
        return None
    V = np.asarray(verts, dtype=np.float32)
    N = np.asarray(norms, dtype=np.float32)
    I = np.asarray(idx, dtype=np.uint16)
    return {"pos": V.tobytes(), "nrm": N.tobytes(), "idx": I.tobytes(),
            "zt": np.zeros(len(verts), dtype=np.float32).tobytes(), "count": int(I.size), "z0": 0.0, "z1": 1.0}

# --- registries: add a class here to expose it to the editor + code + interpreter ---
OBJECT_TYPES = {
    "Axes": Axes, "Circle": Circle, "Dot": Dot, "Line": Line, "Polygon": Polygon,
    "Triangle": Triangle, "Rectangle": Rectangle, "Square": Square,
    "FunctionGraph": FunctionGraph, "Text": Text, "Legend": Legend,
    "ValueTracker": ValueTracker, "DecimalNumber": DecimalNumber,
    # 3D
    "ThreeDAxes": ThreeDAxes, "Box": Box, "Cube": Cube,
    "Sphere": Sphere, "Pyramid": Pyramid, "Vector": Vector,
    # LaTeX as vector glyphs (glyph data comes from the browser's MathJax -> see editor.js)
    "MathTex": MathTex, "SVGMobject": SVGMobject,
}
ANIMATION_TYPES = {
    "Create": _anim.Create, "FadeIn": _anim.FadeIn, "Write": _anim.Write,
    "Shift": _anim.Shift, "GrowFromCenter": _anim.GrowFromCenter,
    "Rotate": _anim.Rotate, "Scale": _anim.Scale, "MoveTo": _anim.MoveTo,
    "MoveAlongPath": _anim.MoveAlongPath, "Indicate": _anim.Indicate,
    "ChangeValue": _anim.ChangeValue,
}
# Animations that make their target APPEAR, so we must NOT pre-add that target.
_APPEARANCE = {"Create", "FadeIn", "GrowFromCenter", "Write"}

# Whitelisted names for user math expressions (no builtins -> safe even server-side).
_SAFE_NAMES = {n: getattr(np, n) for n in
               ["sin", "cos", "tan", "exp", "log", "sqrt", "abs", "pi", "e",
                "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan", "sign"]}


# Standard ET3 / signals-and-systems functions (all numpy-vectorised, so they also work for
# convolution which evaluates on arrays).
def _epsilon(t):
    return np.where(np.asarray(t, dtype=float) >= 0.0, 1.0, 0.0)      # unit step ε(t)


def _rect(t):
    return np.where(np.abs(np.asarray(t, dtype=float)) <= 0.5, 1.0, 0.0)   # rect, width 1 at 0


def _tri(t):
    a = np.abs(np.asarray(t, dtype=float))
    return np.where(a < 1.0, 1.0 - a, 0.0)                           # triangle, base [-1,1]


def _ramp(t):
    t = np.asarray(t, dtype=float)
    return np.where(t >= 0.0, t, 0.0)                                # ramp t·ε(t)


def _si(t):
    return np.sinc(np.asarray(t, dtype=float) / np.pi)               # si(t) = sin(t)/t


_SAFE_NAMES.update({
    "epsilon": _epsilon, "step": _epsilon, "u": _epsilon,            # unit step (aliases)
    "rect": _rect, "tri": _tri, "ramp": _ramp,
    "si": _si, "sinc": np.sinc,                                      # sinc = sin(πt)/(πt)
    "j": 1j,                                                         # imaginary unit (complex mode)
})

# Angle unit for trig in user expressions. In "deg" mode sin(x) is 0 at x=180, not at x=pi.
# Set once per build from the model; read when a func expression is compiled.
_ANGLE_UNIT = "rad"
# Number domain: "real" or "complex". In complex mode a FunctionGraph (e.g. e^(j·t)) is drawn as
# its real AND imaginary parts. Set once per build.
_DOMAIN = "real"
_CAM_ZOOM = 1.0
_CAM_MODE = "2d"
_GL = False                                          # JS reports WebGL availability; if True + 3D, surfaces
#                                                      build ONLY the GPU mesh (skip the costly 2D polygon surface)
# Surface shading ("shadows"): when False, surfaces are drawn FLAT (one colour, no Lambert light).
_SHADOWS = True


def _safe_names():
    names = dict(_SAFE_NAMES)
    if _ANGLE_UNIT == "deg":                            # interpret trig arguments in degrees
        names["sin"] = lambda a: np.sin(np.radians(a))
        names["cos"] = lambda a: np.cos(np.radians(a))
        names["tan"] = lambda a: np.tan(np.radians(a))
        names["arcsin"] = lambda a: np.degrees(np.arcsin(a))
        names["arccos"] = lambda a: np.degrees(np.arccos(a))
        names["arctan"] = lambda a: np.degrees(np.arctan(a))
    return names


# Names that are FUNCTION calls (not variables/constants) - so "sin(x)" stays a call while
# "x(x+1)" or "2pi" get an implicit multiplication. pi and e are values, not functions.
_FUNC_NAMES = set(_SAFE_NAMES) - {"pi", "e", "j"}   # pi, e, j are VALUES (implicit mult), not calls


def normalize_expr(s):
    """Accept GeoGebra-style input and return valid Python:
      - '^'  -> '**'  (x^2 -> x**2)
      - implicit multiplication: 3x -> 3*x, 2sin(x) -> 2*sin(x), x(x+1) -> x*(x+1),
        (x+1)(x-1) -> (x+1)*(x-1), 2pi -> 2*pi
    Function names stay calls (sin( is not sin*( ). A '*' is inserted between a VALUE-END token
    (number, ')', or a non-function name) and a VALUE-START token (number, '(', or any name)."""
    s = str(s).replace("^", "**")
    tokens = re.findall(r"\s+|\d+\.?\d*|[A-Za-z_]\w*|\*\*|[-+*/(),]|.", s)
    val_end = lambda t: bool(t) and (t[-1].isdigit() or t == ")" or (t[0].isalpha() and t not in _FUNC_NAMES))
    val_start = lambda t: bool(t) and (t[0].isdigit() or t == "(" or t[0].isalpha())
    out, prev = [], None
    for tok in tokens:
        if tok.strip() == "":
            continue                                  # drop whitespace (tokens stay separated)
        if prev is not None and val_end(prev) and val_start(tok):
            out.append("*")
        out.append(tok)
        prev = tok
    return "".join(out)


def func_from_expr(expr):
    """'sin(x)' / '3x^2' -> f(x), evaluated in a restricted namespace (no builtins): safe. Input is
    normalised (GeoGebra style) first; trig respects the current angle unit (_ANGLE_UNIT)."""
    code = compile(normalize_expr(expr), "<func>", "eval")
    names = _safe_names()
    # x, t and y all alias the single independent variable, so a 1-var curve works whichever letter it
    # uses (sin(x), si(t), cos(y)). A SURFACE (both x and y) goes through func2_from_expr instead.
    return lambda x: eval(code, {"__builtins__": {}}, {"x": x, "t": x, "y": x, **names})


def func2_from_expr(expr):
    """Two-variable version: 'sin(x)*cos(y)' -> f(x, y) (for Surface). Same safe namespace + input
    normalisation + angle unit as func_from_expr."""
    code = compile(normalize_expr(expr), "<func2>", "eval")
    names = _safe_names()
    return lambda x, y: eval(code, {"__builtins__": {}}, {"x": x, "y": y, **names})


def term_from_expr_i(expr):
    """Summation term aᵢ: a NUMBER expression in the running index i (e.g. '1/i^2')."""
    code = compile(normalize_expr(expr), "<sum_i>", "eval")
    names = _safe_names()
    return lambda i: eval(code, {"__builtins__": {}}, {"i": i, **names})


def term_from_expr_ix(expr):
    """Summation term as a FUNCTION of x for each index i (function partial sums / Fourier)."""
    code = compile(normalize_expr(expr), "<sum_ix>", "eval")
    names = _safe_names()
    return lambda i, x: eval(code, {"__builtins__": {}}, {"i": i, "x": x, "t": x, **names})


def _resolve_arg(key, value):
    """Turn a model arg value into a real Python value."""
    if isinstance(value, str):
        if value.isupper() and hasattr(_const, value):     # BLUE, RIGHT, ORIGIN, ...
            return getattr(_const, value)
        if key == "func":
            return func_from_expr(value)
    return value


_STYLE_ATTRS = ("color", "fill_color", "fill_opacity", "stroke_width", "stroke_opacity", "show_center")
# Types that live in WORLD (3D) coordinates, NOT in the axes' data coordinates: they must not be
# re-mapped by axes.place (which would distort a solid by the x/y data scaling).
_WORLD_TYPES = {"Axes", "ThreeDAxes", "Box", "Cube", "Sphere", "Pyramid", "Vector",
                "MathTex", "SVGMobject"}


def _init_params(cls):
    try:
        return set(inspect.signature(cls).parameters)
    except (ValueError, TypeError):
        return set()


def _c2p_fn(axes):
    """Data->world mapper that also works WITHOUT an axes (then data == world).
    Lets annotation objects (Marker/Measure) be built in world coordinates so arrow cones/dots
    never distort under a non-uniform axes (same reason Dot maps only its centre)."""
    if axes is not None:
        return lambda x, y, z=0.0: np.asarray(axes.coords_to_point(x, y, z), dtype=float)
    return lambda x, y, z=0.0: np.array([x, y, z], dtype=float)


def _xyz(p):
    p = list(p) + [0.0, 0.0, 0.0]
    return float(p[0]), float(p[1]), float(p[2])


def _build_marker(args, style, axes):
    """A point marker in DATA coords: a dot at (x,y), an optional label, and optional thin guide
    lines down to the x-axis and across to the y-axis. General: works for any marked point."""
    c2p = _c2p_fn(axes)
    x, y, z = _xyz(args.get("point", [0.0, 0.0, 0.0]))
    col = style.get("color", (0.0, 0.0, 0.0))
    obj = AnimObject()
    if args.get("show_guides", False):
        for end in ((x, 0.0, z), (0.0, y, z)):                      # to x-axis (y=0), to y-axis (x=0)
            g = Line(c2p(x, y, z), c2p(*end))
            g.color = (0.6, 0.6, 0.6)
            g.stroke_width = 1.5
            obj.add(g)
    wc = c2p(x, y, z)
    dot = OBJECT_TYPES["Dot"](center=wc, radius=float(args.get("radius", 0.08)))
    dot.color = col
    dot.fill_color = col
    dot.fill_opacity = 1.0
    obj.add(dot)
    label = str(args.get("label", "")).strip()
    if label:
        lab = Text(label, position=wc + np.array([0.22, 0.22, 0.0]),
                   font_size=float(args.get("font_size", 28)), color=col)
        obj.add(lab)
    return obj


def _build_measure(args, style, axes):
    """A dimension double-arrow between two DATA points with a centred label (amplitude, period,
    distance d, jump height, ...). `offset` shifts the whole arrow perpendicular to the span. General
    measuring annotation, dockable to any curve/graph by giving the two endpoints."""
    c2p = _c2p_fn(axes)
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 4.0))
    A = c2p(*_xyz(args.get("start", [0.0, 0.0, 0.0])))
    B = c2p(*_xyz(args.get("end", [1.0, 0.0, 0.0])))
    d = B - A
    L = float(np.linalg.norm(d))
    perp = np.array([0.0, 0.0, 0.0]) if L < 1e-9 else np.array([-d[1], d[0], 0.0]) / L
    off = float(args.get("offset", 0.0))
    A2, B2 = A + off * perp, B + off * perp
    obj = AnimObject()
    obj.add(Vector(end=B2, start=A2, color=col, stroke_width=sw),     # heads at BOTH ends
            Vector(end=A2, start=B2, color=col, stroke_width=sw))
    label = str(args.get("label", "")).strip()
    if label:
        lab = Text(label, position=0.5 * (A2 + B2) + 0.3 * perp,
                   font_size=float(args.get("font_size", 28)), color=col)
        obj.add(lab)
    return obj


def _build_area(args, style, axes):
    """Filled area UNDER a curve y=f(x) over [x_min,x_max], or BETWEEN two curves f and g (g = `func2`;
    empty -> baseline y=0). A closed polygon sampled along the top (a->b) and bottom (b->a), filled with
    the style colour/opacity. General: any function(s) via expression, any interval."""
    f = func_from_expr(str(args.get("func", "0")))
    g_raw = str(args.get("func2", "")).strip()
    g = func_from_expr(g_raw) if g_raw else None
    a, b = float(args.get("x_min", 0.0)), float(args.get("x_max", 1.0))
    if b < a:
        a, b = b, a
    n = max(2, int(args.get("samples", 64)))
    lo, hi = (axes.y_min, axes.y_max) if axes is not None else (-1e9, 1e9)

    def ev(fn, x):                                            # safe eval, clamped into the y-range (tames poles)
        try:
            v = float(fn(x))
        except Exception:
            v = lo
        if not np.isfinite(v):
            v = lo
        return min(hi, max(lo, v))

    xs = np.linspace(a, b, n + 1)
    top = [(float(x), ev(f, x), 0.0) for x in xs]
    bot = ([(float(x), ev(g, x), 0.0) for x in xs[::-1]] if g is not None
           else [(b, 0.0, 0.0), (a, 0.0, 0.0)])
    poly = Polygon([np.asarray(p, dtype=float) for p in top + bot], closed=True)
    col = style.get("color", (0.35, 0.60, 0.92))
    poly.color = col
    poly.fill_color = style.get("fill_color", col)
    poly.fill_opacity = float(style.get("fill_opacity", 0.4))
    poly.stroke_width = float(style.get("stroke_width", 0.0))
    if axes is not None:
        axes.place(poly)
    return poly


_CMAP_STOPS = [(0.0, (0.23, 0.30, 0.75)), (0.5, (0.95, 0.88, 0.25)), (1.0, (0.85, 0.20, 0.15))]  # blue->yellow->red


def _cmap(t):
    t = 0.0 if t < 0 else (1.0 if t > 1 else float(t))
    for i in range(len(_CMAP_STOPS) - 1):
        t0, c0 = _CMAP_STOPS[i]
        t1, c1 = _CMAP_STOPS[i + 1]
        if t <= t1:
            f = (t - t0) / (t1 - t0) if t1 > t0 else 0.0
            return tuple(c0[k] + f * (c1[k] - c0[k]) for k in range(3))
    return _CMAP_STOPS[-1][1]


def _build_scalar_field(args, style, axes):
    """A scalar field f(x,y) as a colour heatmap (nx×ny cells) + contour/level lines (marching squares)
    + an optional gradient arrow (⟂ to the level line) at `gradient_at`="x,y". General: any expression."""
    c2p = _c2p_fn(axes)
    f = func2_from_expr(str(args.get("func", "0")))
    if axes is not None:
        x0 = float(args.get("x_min", axes.x_min)); x1 = float(args.get("x_max", axes.x_max))
        y0 = float(args.get("y_min", axes.y_min)); y1 = float(args.get("y_max", axes.y_max))
    else:
        x0, x1 = float(args.get("x_min", -3.0)), float(args.get("x_max", 3.0))
        y0, y1 = float(args.get("y_min", -3.0)), float(args.get("y_max", 3.0))
    nx, ny = max(2, int(args.get("nx", 24))), max(2, int(args.get("ny", 24)))
    levels = int(args.get("levels", 6))
    show_heat = bool(args.get("show_heat", True))
    show_cont = bool(args.get("show_contours", True))
    cont_col = style.get("color", (0.1, 0.1, 0.1))
    fop = float(style.get("fill_opacity", 0.8))
    csw = float(style.get("stroke_width", 2.0))

    def ev(x, y):
        try:
            return float(f(x, y))
        except Exception:
            return float("nan")

    nc = 40                                                  # dense grid for min/max + contour lines
    gx = np.linspace(x0, x1, nc + 1)
    gy = np.linspace(y0, y1, nc + 1)
    Z = np.array([[ev(gx[i], gy[j]) for j in range(nc + 1)] for i in range(nc + 1)])
    fin = Z[np.isfinite(Z)]
    fmin = float(fin.min()) if fin.size else 0.0
    fmax = float(fin.max()) if fin.size else 1.0
    if fmax - fmin < 1e-12:
        fmax = fmin + 1.0
    obj = AnimObject()
    if show_heat:
        xe = np.linspace(x0, x1, nx + 1)
        ye = np.linspace(y0, y1, ny + 1)
        for i in range(nx):
            for j in range(ny):
                v = ev(0.5 * (xe[i] + xe[i + 1]), 0.5 * (ye[j] + ye[j + 1]))
                if not np.isfinite(v):
                    continue
                cell = Polygon([c2p(xe[i], ye[j]), c2p(xe[i + 1], ye[j]),
                                c2p(xe[i + 1], ye[j + 1]), c2p(xe[i], ye[j + 1])], closed=True)
                col = _cmap((v - fmin) / (fmax - fmin))
                cell.color = col
                cell.fill_color = col
                cell.fill_opacity = fop
                cell.stroke_width = 0.0
                obj.add(cell)
    if show_cont and levels > 0:
        for lev in np.linspace(fmin, fmax, levels + 2)[1:-1]:
            for i in range(nc):
                for j in range(nc):
                    v = (Z[i, j], Z[i + 1, j], Z[i + 1, j + 1], Z[i, j + 1])
                    if not all(np.isfinite(vv) for vv in v):
                        continue
                    corner = ((gx[i], gy[j]), (gx[i + 1], gy[j]), (gx[i + 1], gy[j + 1]), (gx[i], gy[j + 1]))
                    pts = []
                    for e in range(4):
                        a, b = e, (e + 1) % 4
                        va, vb = v[a] - lev, v[b] - lev
                        if va * vb < 0:
                            fr = (lev - v[a]) / (v[b] - v[a])
                            pA, pB = corner[a], corner[b]
                            pts.append((pA[0] + fr * (pB[0] - pA[0]), pA[1] + fr * (pB[1] - pA[1])))
                    for k in range(0, len(pts) - 1, 2):      # 2 crossings -> 1 segment; 4 -> 2 segments
                        ln = Line(c2p(*pts[k]), c2p(*pts[k + 1]))
                        ln.color = cont_col
                        ln.stroke_width = csw
                        obj.add(ln)
    ga = str(args.get("gradient_at", "")).strip()
    if ga:
        try:
            parts = [float(s) for s in ga.replace(";", ",").split(",")[:2]]
            px, py = parts[0], parts[1]
            h = 1e-4 * max(1.0, abs(px), abs(py))
            dfx = (ev(px + h, py) - ev(px - h, py)) / (2 * h)
            dfy = (ev(px, py + h) - ev(px, py - h)) / (2 * h)
            nrm = float(np.hypot(dfx, dfy))
            if np.isfinite(nrm) and nrm > 1e-9:
                gs = float(args.get("grad_scale", 0.4))
                obj.add(Vector(end=c2p(px + gs * dfx / nrm, py + gs * dfy / nrm),
                               start=c2p(px, py), color=cont_col, stroke_width=csw + 1.0))
        except Exception:
            pass
    return obj


_VF_PRESETS = {                                              # preset name -> (fx, fy) component expressions
    "radial": ("x", "y"), "source": ("x", "y"), "sink": ("-x", "-y"),
    "vortex": ("-y", "x"), "uniform": ("1", "0"),
}
_VF_LOW = np.array([0.20, 0.40, 0.90])                        # colour ramp for color_by_mag: small -> large
_VF_HIGH = np.array([0.90, 0.25, 0.20])


def _build_vector_field(args, style, axes):
    """A 2D vector field as an arrow grid. Direction from free component expressions fx(x,y), fy(x,y) OR
    a preset (radial/source/sink/vortex/uniform). Arrow length scales with magnitude (or `normalize` =
    all equal), capped at `max_len`; optional colour-by-magnitude ramp. General for any planar field."""
    c2p = _c2p_fn(axes)
    preset = str(args.get("preset", "custom")).strip().lower()
    fxs, fys = str(args.get("fx", "0")), str(args.get("fy", "0"))
    if preset in _VF_PRESETS:
        fxs, fys = _VF_PRESETS[preset]
    fx, fy = func2_from_expr(fxs), func2_from_expr(fys)
    if axes is not None:
        x0 = float(args.get("x_min", axes.x_min)); x1 = float(args.get("x_max", axes.x_max))
        y0 = float(args.get("y_min", axes.y_min)); y1 = float(args.get("y_max", axes.y_max))
    else:
        x0, x1 = float(args.get("x_min", -3.0)), float(args.get("x_max", 3.0))
        y0, y1 = float(args.get("y_min", -3.0)), float(args.get("y_max", 3.0))
    nx, ny = max(2, int(args.get("nx", 11))), max(2, int(args.get("ny", 11)))
    scale = float(args.get("scale", 0.3))
    maxlen = float(args.get("max_len", 0.8))
    norm = bool(args.get("normalize", False))
    cbm = bool(args.get("color_by_mag", False))
    base = style.get("color", (0.35, 0.60, 0.92))
    sw = float(style.get("stroke_width", 3.0))

    def uv(xi, yj):
        try:
            u, v = float(fx(xi, yj)), float(fy(xi, yj))
        except Exception:
            return 0.0, 0.0
        return (u, v) if (np.isfinite(u) and np.isfinite(v)) else (0.0, 0.0)

    grid = [(xi, yj, *uv(xi, yj)) for xi in np.linspace(x0, x1, nx) for yj in np.linspace(y0, y1, ny)]
    mmax = max((np.hypot(u, v) for _, _, u, v in grid), default=1.0) or 1.0
    obj = AnimObject()
    for (xi, yj, u, v) in grid:
        m = float(np.hypot(u, v))
        if m < 1e-12:
            continue
        L = scale if norm else min(maxlen, scale * m)
        a = c2p(xi, yj)
        b = c2p(xi + L * u / m, yj + L * v / m)
        col = base
        if cbm:
            t = min(1.0, m / mmax)
            col = tuple((1.0 - t) * _VF_LOW + t * _VF_HIGH)
        obj.add(Vector(end=b, start=a, color=col, stroke_width=sw))
    return obj


def _build_labeled_arrow(args, style, axes):
    """A straight arrow start->end (DATA coords) with a LaTeX/text label at its midpoint or tip.
    General current/voltage/force/field arrow. `label_at`: 'mid' or 'end'."""
    c2p = _c2p_fn(axes)
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 4.0))
    A = c2p(*_xyz(args.get("start", [0.0, 0.0, 0.0])))
    B = c2p(*_xyz(args.get("end", [2.0, 1.0, 0.0])))
    obj = AnimObject()
    obj.add(Vector(end=B, start=A, color=col, stroke_width=sw))
    label = str(args.get("label", "")).strip()
    if label:
        d = B - A
        L = float(np.linalg.norm(d))
        perp = np.array([0.0, 0.0, 0.0]) if L < 1e-9 else np.array([-d[1], d[0], 0.0]) / L
        anchor = B + 0.25 * perp if str(args.get("label_at", "mid")) == "end" else 0.5 * (A + B) + 0.3 * perp
        obj.add(Text(label, position=anchor, font_size=float(args.get("font_size", 28)), color=col))
    return obj


def _build_loop_arrow(args, style, axes):
    """A curved (arc) arrow — circulation / mesh loop / feedback. Arc around `center` (DATA coords) with
    world-unit `radius` from `start_angle` to `end_angle` (degrees), an arrowhead at the end, optional
    label. `radius` is in world units so the arc stays circular on any axes."""
    c2p = _c2p_fn(axes)
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 4.0))
    c = c2p(*_xyz(args.get("center", [0.0, 0.0, 0.0])))
    r = float(args.get("radius", 0.8))
    a0 = np.radians(float(args.get("start_angle", 30.0)))
    a1 = np.radians(float(args.get("end_angle", 320.0)))
    ts = np.linspace(a0, a1, 48)
    pts = [c + r * np.array([np.cos(t), np.sin(t), 0.0]) for t in ts]
    obj = AnimObject()
    arc = Polygon(pts, closed=False)                            # open polyline through all arc samples
    arc.color = col
    arc.stroke_width = sw
    obj.add(arc)
    s = 1.0 if a1 >= a0 else -1.0                               # sweep direction -> tangent at the end
    tan = s * np.array([-np.sin(a1), np.cos(a1), 0.0])
    tip = pts[-1]
    head = max(0.12, 0.22 * r)
    back = tip - head * tan
    perp = np.array([-tan[1], tan[0], 0.0])
    ah = Polygon([tip, back + 0.5 * head * perp, back - 0.5 * head * perp], closed=True)
    ah.color = col
    ah.fill_color = col
    ah.fill_opacity = 1.0
    ah.stroke_width = sw
    obj.add(ah)
    label = str(args.get("label", "")).strip()
    if label:
        obj.add(Text(label, position=c, font_size=float(args.get("font_size", 28)), color=col))
    return obj


def _build_tangent(args, style, axes):
    """Tangent (or secant) line to a graph y=f(x). Tangent slope via central difference at x0; secant
    slope via (f(x1)-f(x0))/(x1-x0). The line runs ±half_len in x; optional touch-point dot(s) and a
    slope label. General: any function/expression, any point(s). Built in world coords (no distortion)."""
    c2p = _c2p_fn(axes)
    f = func_from_expr(str(args.get("func", "0")))

    def fx(x):
        try:
            v = float(f(x))
            return v if np.isfinite(v) else 0.0
        except Exception:
            return 0.0

    x0 = float(args.get("x0", 0.0))
    y0 = fx(x0)
    half = float(args.get("half_len", 2.0))
    secant = bool(args.get("secant", False))
    pts = [(x0, y0)]
    if secant:
        x1 = float(args.get("x1", x0 + 1.0))
        y1 = fx(x1)
        m = (y1 - y0) / (x1 - x0) if abs(x1 - x0) > 1e-12 else 0.0
        xa, xb = min(x0, x1) - half, max(x0, x1) + half
        pts.append((x1, y1))
    else:
        h = 1e-4 * max(1.0, abs(x0))
        m = (fx(x0 + h) - fx(x0 - h)) / (2.0 * h)
        xa, xb = x0 - half, x0 + half
    col = style.get("color", (0.0, 0.0, 0.0))
    obj = AnimObject()
    ln = Line(c2p(xa, y0 + m * (xa - x0)), c2p(xb, y0 + m * (xb - x0)))
    ln.color = col
    ln.stroke_width = float(style.get("stroke_width", 3.0))
    obj.add(ln)
    if args.get("show_point", True):
        for (px, py) in pts:
            d = OBJECT_TYPES["Dot"](center=c2p(px, py), radius=0.08)
            d.color = col
            d.fill_color = col
            d.fill_opacity = 1.0
            obj.add(d)
    if args.get("show_slope", False):
        lab = Text(f"m = {m:.2f}", position=c2p(x0, y0) + np.array([0.25, 0.25, 0.0]),
                   font_size=float(args.get("font_size", 26)), color=col)
        obj.add(lab)
    return obj


def _build_object(spec, objects, axes=None):
    args = {k: _resolve_arg(k, v) for k, v in spec.get("args", {}).items()}
    # Styling is set as attributes AFTER construction (shapes don't take color in __init__).
    style = {k: args.pop(k) for k in list(args) if k in _STYLE_ATTRS}
    t = spec["type"]
    if t == "plot":                                         # a graph on an explicit axes
        obj = objects[spec["on"]].plot(**args)
    elif t == "FunctionGraph" and axes is not None:         # follow the scene's axes (range + scale)
        raw = str(spec.get("args", {}).get("func", "0"))
        if _is_surface(raw):                                # BOTH x and y -> it IS a surface
            func2 = func2_from_expr(raw)
            res = int(args.get("res_max", args.get("resolution", 64)) or 64)
            use_gl = _GL and _CAM_MODE == "3d"
            mesh = None
            if use_gl:                                      # try the GPU path FIRST (skip the costly 2D mesh)
                try:
                    n_gl = max(16, min(max(res, 120), 200))  # GPU handles high res cheaply -> smooth silhouette
                    mesh = _gl_surface_mesh(func2, axes, n_gl)
                except Exception:
                    mesh = None
            if mesh is not None:
                # GPU renders the surface smoothly. We DON'T build the expensive adaptive polygon mesh;
                # a tiny proxy (the 8 world-AABB corners) gives selection/pick a bounding box. Not drawn
                # by the 2D painter (flagged `_gl`), not part of GL (that uses `_gl_mesh`).
                import numpy as _np
                pos = _np.frombuffer(mesh["pos"], dtype=_np.float32).reshape(-1, 3)
                lo, hi = pos.min(axis=0), pos.max(axis=0)
                corners = _np.array([[x, y, z] for x in (lo[0], hi[0]) for y in (lo[1], hi[1]) for z in (lo[2], hi[2])], dtype=float)
                obj = AnimObject(); obj.points = corners
                obj._gl_mesh = mesh
                obj._gl_color = [float(c) for c in style.get("color", (0.35, 0.60, 0.92))]
                obj._gl_opacity = float(style.get("fill_opacity", 1.0))
                obj._gl_height = bool(args.get("height_color", False))
                obj._gl_surf = True                          # terrain: up-flip shading in the GL fragment shader
                obj._gl = True
            else:                                           # 2D fallback: the flat CPU-painted surface
                obj = axes.plot_surface(func2, shade=_SHADOWS, **_surface_kw(args, style))
                obj._gl = False
        else:
            style.pop("fill_opacity", None); style.pop("fill_color", None)   # a 1D curve is a STROKE, never a filled area
            f = args["func"]
            xr = args.get("x_range")                        # x = plotted domain (per function)
            yr = (axes.y_min, axes.y_max)                   # y value range (Wertebereich) ALWAYS from the Axes
            if _DOMAIN == "complex":                        # draw real AND imaginary parts
                obj = AnimObject()
                re_g = axes.plot(lambda x: np.real(f(x)), x_range=xr, y_range=yr)
                im_g = axes.plot(lambda x: np.imag(f(x)), x_range=xr, y_range=yr)
                im_g.color = (0.95, 0.55, 0.15)             # Im in orange (Re keeps the chosen colour)
                obj.add(re_g, im_g)
                obj._cx_parts = (re_g, im_g)
            else:
                obj = axes.plot(f, x_range=xr, y_range=yr)
                # (no _center_create: a 1D graph is drawn LEFT -> RIGHT, the natural reading/sampling
                #  order — partial_bezier traces from the first sampled point at x_min onward.)
    elif t == "Riemann" and axes is not None:               # midpoint Riemann rectangles on the axes
        kw = {k: style[k] for k in ("color", "fill_opacity") if k in style}
        obj = axes.riemann_rectangles(args["func"], int(args.get("count", 8)), **kw)
    elif t == "Dot":                                        # a dot is a ROUND marker: map only its CENTRE to
        c = args.get("center", [0.0, 0.0, 0.0])              # the axes, keep a fixed world radius -> never
        r = float(args.get("radius", 0.08))                  # stretched into an ellipse on a non-uniform axes
        wc = (axes.coords_to_point(c[0], c[1], c[2] if len(c) > 2 else 0.0) if axes is not None
              else np.array([c[0], c[1], c[2] if len(c) > 2 else 0.0], dtype=float))
        obj = OBJECT_TYPES["Dot"](center=np.asarray(wc, dtype=float), radius=r)
    elif t == "Marker":                                     # point marker (dot + label + guides)
        obj = _build_marker(args, style, axes)
    elif t == "Measure":                                    # dimension double-arrow with label
        obj = _build_measure(args, style, axes)
    elif t == "Area":                                       # filled area under / between curve(s)
        obj = _build_area(args, style, axes)
    elif t == "TangentLine":                                # tangent / secant line to a graph
        obj = _build_tangent(args, style, axes)
    elif t == "LabeledArrow":                               # straight arrow + label
        obj = _build_labeled_arrow(args, style, axes)
    elif t == "LoopArrow":                                  # curved circulation / feedback arrow
        obj = _build_loop_arrow(args, style, axes)
    elif t == "VectorField":                                # 2D arrow-grid field (preset or free fx,fy)
        obj = _build_vector_field(args, style, axes)
    elif t == "ScalarField":                                # heatmap + contour lines + gradient arrow
        obj = _build_scalar_field(args, style, axes)
    else:
        # Some classes (3D solids, Vector) take color/fill_opacity/stroke_width in __init__ so the
        # style reaches every face; pass those through when the constructor accepts them.
        kwargs = dict(args)
        if t == "Axes":                                     # zoom-aware tick refinement (2D) comes from the camera
            kwargs["zoom"] = _CAM_ZOOM
            kwargs["dynamic_ticks"] = (_CAM_MODE == "2d")
        accepted = _init_params(OBJECT_TYPES[t])
        for k in ("color", "fill_opacity", "stroke_width"):
            if k in style and k in accepted:
                kwargs[k] = style[k]
        obj = OBJECT_TYPES[t](**kwargs)
        # A 2D/data object's coordinates are DATA coordinates: map them onto the axes so e.g.
        # center=(1,0) sits on the tick '1'. WORLD/3D objects (solids) are left in world coordinates.
        if axes is not None and t not in _WORLD_TYPES:
            axes.place(obj)
        # 3D SOLIDS on the GPU (smooth/opaque). The cheap 2D faces stay (bbox/pick/fallback); flag `_gl`
        # so the 2D painter skips drawing them and the GPU draws a clean mesh instead. Sphere = smooth.
        if _GL and _CAM_MODE == "3d" and t in ("Sphere", "Box", "Cube", "Pyramid"):
            try:
                mesh = _gl_solid_mesh(obj, smooth=(t == "Sphere"), center=args.get("center", (0.0, 0.0, 0.0)))
                if mesh is not None:
                    obj._gl_mesh = mesh
                    obj._gl_color = [float(c) for c in style.get("color", (0.35, 0.60, 0.92))]
                    obj._gl_opacity = float(style.get("fill_opacity", 1.0))   # fix #3: honour the object's transparency (GL blends + masks depth)
                    obj._gl_height = False
                    obj._gl_surf = False                     # solid: true outward normals (no terrain up-flip)
                    obj._gl = True
            except Exception:
                obj._gl = False
    for k, v in style.items():
        setattr(obj, k, v)
    if hasattr(obj, "_cx_parts"):                           # complex graph: Re takes the chosen style
        re_g, im_g = obj._cx_parts
        re_g.color = obj.color
        re_g.stroke_width = im_g.stroke_width = obj.stroke_width
    if t == "FunctionGraph":                                # remember the expression so computations
        obj._func_expr = str(spec.get("args", {}).get("func", "0"))   # (e.g. Convolution) can read it
    # Child / result objects: build them as sub-objects so the editor can expand the parent and
    # configure each result (shown?, where, size, colour - the same settings as any shape).
    for child_spec in spec.get("children", []):
        if not child_spec.get("visible", True):
            continue                                        # hidden -> not built / not drawn
        child = _build_object(child_spec, objects, axes=axes)
        obj.add(child)
        if child_spec.get("id") is not None:
            objects[child_spec["id"]] = child
        # A result-tagged DecimalNumber shows a value computed from its PARENT (see results.py).
        res = child_spec.get("result")
        if res and isinstance(child, DecimalNumber):
            value = result_value(t, res["key"], args, axes)
            if value is None and hasattr(obj, "_result_value"):
                value = obj._result_value                   # geometric results (e.g. intersection area)
            if value is not None:
                child.set_value(value)                      # prefix (symbol/formula) stays from props
    return obj


def _build_animation(spec, objects):
    args = {k: _resolve_arg(k, v) for k, v in spec.get("args", {}).items()}
    return ANIMATION_TYPES[spec["type"]](objects[spec["target"]], **args)


# --- Computations: operations OVER objects (not objects themselves). Each references existing
# objects by id as operands, validated by type, and produces a result object (+ result children). ---
_SHAPES = {"Circle", "Rectangle", "Square", "Triangle", "Polygon"}
_COMP_ACCEPT = {
    "Convolution": {"f": {"FunctionGraph"}, "g": {"FunctionGraph"}},
    "Product":     {"f": {"FunctionGraph"}, "g": {"FunctionGraph"}},
    "Sum":         {"f": {"FunctionGraph"}, "g": {"FunctionGraph"}},
    "Difference":  {"f": {"FunctionGraph"}, "g": {"FunctionGraph"}},
    "Intersection": {"a": _SHAPES, "b": _SHAPES},
}
# Operand roles an ANIMATED operator takes over while playing: those operand objects are then not
# drawn statically (the operator renders them as part of its process, e.g. the sliding graph).
_COMP_CONSUMES = {"Convolution": {"f", "g"}}

# What KIND of result each operation produces, so its result can be reused as an operand:
#   function ops -> a callable f(x) (reusable anywhere a FunctionGraph is accepted)
#   Intersection -> a region polygon (reusable where shapes are accepted)
_COMP_RESULT_KIND = {"Convolution": "function", "Product": "function", "Sum": "function",
                     "Difference": "function", "Intersection": "region"}


def _operand_func(oid, objects, results):
    """Callable f(x) for a function operand - from a FunctionGraph object OR a prior operation's result."""
    r = results.get(oid)
    if r is not None and r.get("kind") == "function":
        return r["func"]
    o = objects.get(oid)
    if o is not None and getattr(o, "_func_expr", None) is not None:
        return func_from_expr(o._func_expr)
    return None


def _operand_shape(oid, objects, results):
    """Shape/region object for a geometry operand - from a shape object OR a prior region result."""
    r = results.get(oid)
    if r is not None and r.get("kind") == "region" and r.get("obj") is not None:
        return r["obj"]
    return objects.get(oid)


def _topo_order(comps):
    """Order operations so an operation runs AFTER any operation whose result it uses as an operand
    (depth-first topological sort). Cycles are broken (the offending edge is skipped)."""
    by_id = {c.get("id"): c for c in comps if c.get("id")}
    seen, order = set(), []

    def visit(c, stack):
        cid = c.get("id")
        if cid in seen or cid in stack:
            return
        stack.add(cid)
        for dep in (c.get("inputs") or {}).values():
            if dep in by_id:
                visit(by_id[dep], stack)
        stack.discard(cid); seen.add(cid); order.append(c)

    for c in comps:
        visit(c, set())
    return order


def _comp_valid(cspec, objects, types, comps_by_id=None):
    comps_by_id = comps_by_id or {}
    for role, allowed in _COMP_ACCEPT.get(cspec["type"], {}).items():
        oid = cspec.get("inputs", {}).get(role)
        if oid is None:
            return False
        if oid in objects and types.get(oid) in allowed:
            continue                                        # an object operand of the right type
        dep = comps_by_id.get(oid)                          # OR another operation's result of a matching kind
        if dep is not None:
            kind = _COMP_RESULT_KIND.get(dep.get("type"))
            if (kind == "function" and "FunctionGraph" in allowed) or (kind == "region" and (allowed & _SHAPES)):
                continue
        return False
    return True


def _run_computation(scene, cspec, objects, types, axes, results=None, comps_by_id=None):
    """Run one computation: an OPERATION over objects/other results, shown as an animated PROCESS. Its
    result is recorded in `results` (by id) so LATER operations can use it as an operand (chaining).
    Invalid/unconfigured operands -> skipped. Adds its visual pieces to the scene."""
    if results is None:
        results = {}
    if comps_by_id is None:
        comps_by_id = {}
    t = cspec["type"]
    if t in _ARITH:                                         # number operators: operands are typed-in numbers
        nums = cspec.get("numbers", [])
        p = cspec.get("props", {})
        if len(nums) >= 1:
            _arith.run(t, scene, nums, float(p.get("run_time", 4.0)), scene.animating, p.get("mode", "squares"))
        return
    if t in ("Summation", "BigProduct"):                    # Σ sum / ∏ product over an index i (no object operands)
        p = cspec.get("props", {})
        i0 = int(p.get("from", 1))
        end_raw = str(p.get("to", "n")).strip()
        try:                                                # numeric limit, or symbolic ('n')
            i1, symbolic, end_label = int(float(end_raw)), False, str(int(float(end_raw)))
        except (ValueError, TypeError):
            i1, symbolic, end_label = None, True, (end_raw or "n")
        expr = str(p.get("term", "1/i^2"))
        color = p.get("color", (0.89, 0.29, 0.20))
        rt, st = float(p.get("run_time", 5.0)), int(p.get("show_terms", 3))
        if p.get("sum_mode", "number") == "function":
            if axes is not None:
                _proc.summation_function(scene, term_from_expr_ix(expr), i0, i1, axes, symbolic=symbolic,
                                         end_label=end_label, run_time=rt, color=color, show_terms=st,
                                         animating=scene.animating, label_expr=expr)
        else:
            pos = p.get("position", (0.0, 2.4, 0.0))
            sz = float(p.get("size", 0.9))
            vc = p.get("value_color", (0.17, 0.63, 0.17))
            varc = p.get("var_color", (1.0, 0.50, 0.05))     # running variable i (orange)
            endc = p.get("end_color", (0.58, 0.40, 0.74))    # end result (total)
            flc = p.get("pulse_color", (0.40, 0.70, 1.0))    # '+' / Σ flash colour (light blue)
            bdc = p.get("bound_color", (0.84, 0.15, 0.16))  # Σ/∏ limits (lower/upper bounds), red
            choreo = p.get("choreo")                         # step-by-step pieces (abstract->subst->value) from editor
            glyphs = p.get("glyphs")                         # or the whole ground-state as one MathTex
            if choreo:
                _proc.summation_choreo(scene, choreo, run_time=rt, color=color, value_color=vc,
                                       var_color=varc, end_color=endc, flash_color=flc, bound_color=bdc,
                                       animating=scene.animating, position=pos, height=sz)
            elif glyphs:                                     # fallback: real LaTeX vector Σ (ground state)
                _proc.summation_tex(scene, glyphs, run_time=rt, color=color, animating=scene.animating,
                                    position=pos, height=float(p.get("size", 1.4)))
            else:                                            # not ready -> reserve duration (KaTeX overlay shows)
                _proc.summation_number(scene, term_from_expr_i(expr), i0, i1, symbolic=symbolic,
                                       end_label=end_label, run_time=rt, color=color, show_terms=st,
                                       animating=scene.animating, label_expr=expr)
        return
    inputs = cspec.get("inputs", {})
    if not _comp_valid(cspec, objects, types, comps_by_id):  # missing / wrong-type operands -> dead
        return
    props = {k: _resolve_arg(k, v) for k, v in cspec.get("props", {}).items()}
    style = {k: props.pop(k) for k in list(props) if k in _STYLE_ATTRS}
    cid = cspec.get("id")

    if t == "Convolution":
        if axes is None:
            return
        f = _operand_func(inputs["f"], objects, results)    # object OR a prior result's callable
        g = _operand_func(inputs["g"], objects, results)
        if f is None or g is None:
            return
        color = style.get("color", (0.89, 0.29, 0.20))
        tr = props.get("tau_range") or [axes.x_min, axes.x_max]
        conv = _calc.make_convolution(f, g, float(tr[0]), float(tr[1]))
        both_objs = inputs["f"] in objects and inputs["g"] in objects
        if scene.animating and both_objs:                   # PLAY: slide g(t−τ) across f (operands consumed)
            A, B = objects[inputs["f"]], objects[inputs["g"]]
            _proc.convolution(scene, f, g, axes, run_time=float(props.get("run_time", 6.0)),
                              tau_range=props.get("tau_range"), color=color, f_color=A.color, g_color=B.color)
        else:                                               # EDIT view / result operand: finished result curve
            obj = axes.plot(conv); obj.color = color; obj.stroke_width = style.get("stroke_width", 5)
            scene.add(obj)
        if cid:
            results[cid] = {"kind": "function", "func": conv}   # reusable: convolution is a function
        return

    if t in ("Product", "Sum", "Difference"):               # combined function (object/result operands)
        if axes is None:
            return
        f = _operand_func(inputs["f"], objects, results)
        g = _operand_func(inputs["g"], objects, results)
        if f is None or g is None:
            return
        maker = {"Product": _calc.make_product, "Sum": _calc.make_sum, "Difference": _calc.make_difference}[t]
        combined = maker(f, g)
        obj = axes.plot(combined)
        if cid:
            results[cid] = {"kind": "function", "func": combined}
    elif t == "Intersection":                               # region + area; region is reusable in geometry ops
        A = _operand_shape(inputs["a"], objects, results)
        B = _operand_shape(inputs["b"], objects, results)
        if A is None or B is None:
            return
        region, ar = _geom.intersection(A, B)
        obj = Polygon([np.array([p[0], p[1], 0.0]) for p in region]) if len(region) >= 3 else AnimObject()
        obj._result_value = ar
        if cid:
            results[cid] = {"kind": "region", "obj": obj}
    else:
        return

    for k, v in style.items():
        setattr(obj, k, v)
    for child_spec in cspec.get("children", []):            # result children (e.g. area)
        if not child_spec.get("visible", True):
            continue
        child = _build_object(child_spec, objects, axes=axes)
        obj.add(child)
        res = child_spec.get("result")
        if res and isinstance(child, DecimalNumber):
            value = result_value(t, res["key"], props, axes)
            if value is None and hasattr(obj, "_result_value"):
                value = obj._result_value
            if value is not None:
                child.set_value(value)
    scene.add(obj)


def _group_by_step(anim_specs):
    """Group animation specs by their 'step' (default: list position = each its own step),
    and return the groups ordered by step. Same step -> simultaneous; ascending steps -> sequence."""
    groups, order = {}, []
    for i, spec in enumerate(anim_specs):
        step = spec.get("step", i)
        if step not in groups:
            groups[step] = []
            order.append(step)
        groups[step].append(spec)
    return [groups[s] for s in sorted(order)]


class ModelScene(Scene):
    """A Scene built from a declarative model. Render it like any scene (render / render_video)."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.animating = False      # True while building the playable timeline (prepare_play);
        #                             then animated operators take over their operands' display.

    def construct(self):
        global _ANGLE_UNIT, _DOMAIN, _SHADOWS, _CAM_ZOOM, _CAM_MODE, _GL
        _ANGLE_UNIT = self.model.get("angle_unit", "rad")   # set before any func is compiled
        _DOMAIN = self.model.get("domain", "real")
        _SHADOWS = bool(self.model.get("shadows", True))    # surface shading on/off
        cam = self.model.get("camera") or {}
        zoom = cam.get("zoom", 1.0)                         # orthographic zoom (>1 = magnified)
        _CAM_ZOOM = float(zoom)                             # so the Axes can refine its ticks with zoom (2D)
        _CAM_MODE = "3d" if cam.get("mode") == "3d" else "2d"
        _GL = bool(self.model.get("gl", False))             # WebGL layer available (set by the editor)?
        if cam.get("mode") == "3d":                         # orbit camera (theta, phi in radians)
            self.camera = Camera(mode="3d", theta=cam.get("theta", 0.0), phi=cam.get("phi", 0.0), zoom=zoom)
        else:
            self.camera = Camera(zoom=zoom)
        objects = {}
        self.objects_by_id = objects                    # id -> object, for picking by click
        specs = self.model.get("objects", [])
        appearing = {a["target"] for a in self.model.get("animations", [])
                     if a["type"] in _APPEARANCE}
        # Build the first Axes first (if any) so FunctionGraphs can be plotted onto it (and thus
        # follow its value range + scaling), regardless of the order objects were added.
        axes = None
        for spec in specs:
            if spec["type"] == "Axes":
                axes = _build_object(spec, objects)
                if spec.get("id") is not None:
                    objects[spec["id"]] = axes
                break
        built = []
        for spec in specs:
            oid = spec.get("id")
            if oid is not None and oid in objects:          # the axes we already built above
                obj = objects[oid]
            else:
                obj = _build_object(spec, objects, axes=axes)
                if oid is not None:
                    objects[oid] = obj
            # Hidden objects are still BUILT (so operations can use them as operands - a Convolution/
            # Product/… graph stays visible even when its input functions are hidden via the eye), they
            # are just not DRAWN statically.
            if spec.get("visible", True):
                built.append((oid, obj))
        # While PLAYING, objects consumed by an animated operator are drawn by that operator, not
        # statically (e.g. the convolution's two graphs). In the edit view all objects are shown.
        types = {s.get("id"): s["type"] for s in specs if s.get("id")}
        consumed = set()
        if self.animating:
            for cspec in self.model.get("computations", []):
                roles = _COMP_CONSUMES.get(cspec["type"], set())
                if cspec.get("visible", True) and roles and _comp_valid(cspec, objects, types):
                    for r in roles:
                        cid = cspec.get("inputs", {}).get(r)
                        if cid:
                            consumed.add(cid)
        for oid, obj in built:
            if oid not in appearing and oid not in consumed:   # appearance targets are added by play()
                self.add(obj)
        comps = self.model.get("computations", [])
        comps_by_id = {c.get("id"): c for c in comps if c.get("id")}
        results = {}                                           # operation id -> {kind, func|obj} for chaining
        for cspec in _topo_order(comps):                       # run deps before dependents
            if not cspec.get("visible", True):                 # hidden operation -> not built
                continue
            _run_computation(self, cspec, objects, types, axes, results, comps_by_id)
        # Animations are grouped into STEPS: same step -> played together (simultaneously),
        # steps run in ascending order. No step given -> each animation is its own step (sequential,
        # in list order), which keeps the old behaviour.
        for step in _group_by_step(self.model.get("animations", [])):
            anims = []
            for spec in step:
                if spec.get("target") not in objects:       # dangling reference (deleted object) -> skip
                    continue
                a = _build_animation(spec, objects)
                a.run_time = spec.get("run_time", 1.0)
                anims.append(a)
            if anims:
                self.play(*anims)                           # run_time=None -> each keeps its own
        if self.model.get("wait"):
            self.wait(self.model["wait"])
        self.run_updaters()          # settle updater-driven objects for the static (first) frame


# ---------------------------------------------------------------------------
#  Code generation: model -> Python source (what the "programming page" shows)
# ---------------------------------------------------------------------------
def _arg_to_code(key, value):
    if key == "func" and isinstance(value, str):
        return f"lambda x: {normalize_expr(value)}"     # GeoGebra-style input -> valid Python
    if isinstance(value, str) and value.isupper() and hasattr(_const, value):
        return value                                        # a constant name (BLUE, RIGHT, ...)
    return repr(value)


def _args_code(args):
    return ", ".join(f"{k}={_arg_to_code(k, v)}" for k, v in args.items())


def model_to_code(model, class_name="MyScene"):
    """Generate the Python source for a model (one-way: editor -> code)."""
    lines = [
        "from engine.scene import Scene",
        "from engine.axes import Axes",
        "from engine.simpleShape import *",
        "from engine.text import Text",
        "from engine.animation import *",
        "from engine.constants import *",
        "from numpy import sin, cos, tan, exp, log, sqrt, pi, e, sinh, cosh, tanh, arctan, sign",
        "",
        f"class {class_name}(Scene):",
        "    def construct(self):",
    ]
    appearing = {a["target"] for a in model.get("animations", [])
                 if a["type"] in _APPEARANCE}
    for spec in model.get("objects", []):
        oid, argstr = spec.get("id", "obj"), _args_code(spec.get("args", {}))
        if spec["type"] == "plot":
            lines.append(f"        {oid} = {spec['on']}.plot({argstr})")
        else:
            lines.append(f"        {oid} = {spec['type']}({argstr})")
        if oid not in appearing:
            lines.append(f"        self.add({oid})")
    for step in _group_by_step(model.get("animations", [])):
        calls = []
        for spec in step:
            extra = _args_code(spec.get("args", {}))
            extra = (", " + extra) if extra else ""
            calls.append(f"{spec['type']}({spec['target']}{extra}, run_time={spec.get('run_time', 1.0)})")
        lines.append(f"        self.play({', '.join(calls)})")
    if model.get("wait"):
        lines.append(f"        self.wait({model['wait']})")
    return "\n".join(lines)
