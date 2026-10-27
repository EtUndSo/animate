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
from .simpleShape import (Circle, Dot, Line, Polygon, Triangle, Rectangle, Square, FunctionGraph, Ellipse, ArrowHead)
from .text import Text, DecimalNumber
from . import figures as _fig
from . import circuit as _circ
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
    "Triangle": Triangle, "Rectangle": Rectangle, "Square": Square, "Ellipse": Ellipse,
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


# Scene PARAMETERS (editor object `Parameter`: name + value with a slider). Every expression in the
# scene (functions, areas, families, ...) may use the parameter's name like a constant; moving the
# slider rebuilds the scene with the new value. Filled by ModelScene.construct() before any build.
_PARAMS = {}
# Extra expression helpers for piecewise / clipped signals (rectifier, saturation, ramps).
_SAFE_NAMES.update({
    "max": np.maximum, "min": np.minimum, "clip": np.clip, "floor": np.floor, "ceil": np.ceil,
    "mod": np.mod, "where": np.where, "log10": np.log10, "log2": np.log2, "ln": np.log,
    "heaviside": lambda t: np.where(np.asarray(t, dtype=float) >= 0.0, 1.0, 0.0),
})
_RESERVED_PARAM_NAMES = {"x", "y", "t", "i", "e", "pi", "j", "theta"}


def _safe_names():
    names = dict(_SAFE_NAMES)
    for k, v in _PARAMS.items():                        # scene parameters act as constants
        if k and k not in _RESERVED_PARAM_NAMES and k not in _SAFE_NAMES:   # never shadow x/t or a function name
            names[k] = v
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
    # numbers incl. scientific notation (1e-15, 2.5E3, .5) are ONE token, so 1e-15 is not read as 1*e-15
    tokens = re.findall(r"\s+|(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?|[A-Za-z_]\w*|\*\*|[-+*/(),]|.", s)
    is_num = lambda t: t[0].isdigit() or (t[0] == "." and len(t) > 1)
    is_name = lambda t: t[0].isalpha() or t[0] == "_"
    # a VALUE ends with a number, ')' or a non-function name ('log10' is a function although it ends in a digit)
    val_end = lambda t: bool(t) and (is_num(t) or t == ")" or (is_name(t) and t not in _FUNC_NAMES))
    val_start = lambda t: bool(t) and (t[0].isdigit() or t == "(" or t[0].isalpha()
                                       or (t[0] == "." and len(t) > 1 and t[1].isdigit()))
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


def _as_func(v):
    """A callable from a model `func` value: already compiled by _resolve_arg, or an expression string."""
    return v if callable(v) else func_from_expr(str(v))


# Free-text props: never interpreted as constant names (a label "UP" must stay the text "UP").
_TEXT_KEYS = {"text", "label", "labels", "value", "title", "x_label", "y_label", "z_label", "current", "voltage",
              "name", "cells", "row_labels", "col_labels", "dx_label", "dy_label", "tex", "prefix", "suffix",
              "data", "points", "x", "y", "values", "kind", "material", "shape"}


def _resolve_arg(key, value):
    """Turn a model arg value into a real Python value."""
    if isinstance(value, str):
        if key not in _TEXT_KEYS and value.isupper() and hasattr(_const, value):   # BLUE, RIGHT, ORIGIN, ...
            return getattr(_const, value)
        if key == "func":
            return func_from_expr(value) if value.strip() else ""   # empty = "no function" (e.g. a Marker)
    return value


_STYLE_ATTRS = ("color", "fill_color", "fill_opacity", "stroke_width", "stroke_opacity", "show_center", "dash")


def _parse_dash(value):
    """'8,6' / '8 6' / [8, 6] -> [8.0, 6.0]; empty / 'solid' / None -> None (solid stroke)."""
    if value is None or value is False:
        return None
    if isinstance(value, (list, tuple)):
        vals = [float(v) for v in value if str(v).strip() != ""]
    else:
        s = str(value).strip().lower()
        if s in ("", "solid", "none", "0", "false"):
            return None
        if s in ("dashed", "dash"):
            return [10.0, 7.0]
        if s in ("dotted", "dot"):
            return [2.0, 5.0]
        vals = [float(p) for p in re.split(r"[,\s;]+", s) if p]
    vals = [v for v in vals if v >= 0]
    return vals if vals and any(v > 0 for v in vals) else None
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


def _eval_const(expr):
    """A number from an expression that may use scene parameters ('U0/2', '2*pi*f')."""
    code = compile(normalize_expr(str(expr)), "<const>", "eval")
    return float(eval(code, {"__builtins__": {}}, dict(_safe_names())))


def _axis_ref(axes):
    """(x, y) data position of the axis lines - guide lines end there (not at 0, which a log axis or
    a range without 0 does not contain)."""
    if axes is None:
        return 0.0, 0.0
    return float(getattr(axes, "_x0", 0.0)), float(getattr(axes, "_y0", 0.0))


def _nearest_root(h, x_guess, axes):
    """Root of h(x) = 0 nearest to x_guess: scan the axes' x-range (log-spaced on a log axis) for sign
    changes and refine each by bisection. Returns x_guess when h has no root there."""
    if axes is not None:
        lo, hi = float(axes.x_min), float(axes.x_max)
    else:
        lo, hi = x_guess - 10.0, x_guess + 10.0
    logx = axes is not None and getattr(axes, "x_log", False)
    xs = np.logspace(np.log10(lo), np.log10(hi), 2001) if logx else np.linspace(lo, hi, 2001)

    def hv(x):
        try:
            v = float(h(x))
        except Exception:
            return float("nan")
        return v

    try:                                                        # vectorised when the expression allows it
        vals = np.asarray(h(xs), dtype=float)
        if vals.shape != xs.shape:
            raise ValueError
    except Exception:
        vals = np.array([hv(x) for x in xs])
    roots = []
    for k in range(len(xs) - 1):
        a, b, fa, fb = xs[k], xs[k + 1], vals[k], vals[k + 1]
        if not (np.isfinite(fa) and np.isfinite(fb)):
            continue
        if fa == 0.0:
            roots.append(float(a))
            continue
        if fa * fb < 0:
            for _ in range(60):
                m = 0.5 * (a + b)
                fm = hv(m)
                if not np.isfinite(fm):
                    break
                if fa * fm <= 0:
                    b, fb = m, fm
                else:
                    a, fa = m, fm
            roots.append(float(0.5 * (a + b)))
    if not roots:
        return x_guess
    return min(roots, key=lambda r: abs(r - x_guess))


_LABEL_DIRS = {"ne": (1, 1), "nw": (-1, 1), "se": (1, -1), "sw": (-1, -1),
               "n": (0, 1), "s": (0, -1), "e": (1, 0), "w": (-1, 0)}


def _build_marker(args, style, axes):
    """A point marker in DATA coords: a dot at (x,y), an optional label, and optional thin guide
    lines to the axis lines. General: works for any marked point.
    The point may also be COMPUTED: x_expr (expression, may use scene parameters) replaces x; with
    `func` the marker sits ON that curve (y = f(x)); with `func` AND `func2` it sits at their
    intersection nearest to x (operating point = characteristic ∩ load line); y_expr sets y directly."""
    c2p = _c2p_fn(axes)
    x, y, z = _xyz(args.get("point", [0.0, 0.0, 0.0]))
    xe = str(args.get("x_expr", "")).strip()
    if xe:
        try:
            x = _eval_const(xe)
        except Exception:
            pass
    f = args.get("func", "")
    if isinstance(f, str):
        f = func_from_expr(f) if f.strip() else None
    g_raw = str(args.get("func2", "")).strip()
    if f is not None:
        if g_raw:
            gf = func_from_expr(g_raw)
            x = _nearest_root(lambda t: f(t) - gf(t), x, axes)
        try:
            yv = float(f(x))
            if np.isfinite(yv):
                y = yv
        except Exception:
            pass
    else:
        ye = str(args.get("y_expr", "")).strip()
        if ye:
            try:
                y = _eval_const(ye)
            except Exception:
                pass
    col = style.get("color", (0.0, 0.0, 0.0))
    obj = AnimObject()
    if args.get("show_guides", False):
        xr, yr = _axis_ref(axes)
        gd = _parse_dash(args.get("guide_dash", "5,5"))
        for end in ((x, yr, z), (xr, y, z)):                      # down/up to the x-axis, across to the y-axis
            g = Line(c2p(x, y, z), c2p(*end))
            g.color = (0.55, 0.55, 0.55)
            g.stroke_width = 1.5
            g.dash = gd
            obj.add(g)
    wc = c2p(x, y, z)
    dot = OBJECT_TYPES["Dot"](center=wc, radius=float(args.get("radius", 0.08)))
    dot.color = col
    dot.fill_color = col
    dot.fill_opacity = 1.0
    obj.add(dot)
    label = str(args.get("label", "")).strip()
    if label:
        fs = float(args.get("font_size", 28))
        dx, dy = _LABEL_DIRS.get(str(args.get("label_pos", "ne")), (1, 1))
        off = np.array([dx * 0.2, dy * (0.12 + 0.5 * fs * _fig.UPP), 0.0])
        align = "left" if dx > 0 else ("right" if dx < 0 else "center")
        obj.add(Text(label, position=wc + off, font_size=fs, color=col, align=align))
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
        fs = float(args.get("font_size", 28))
        align = "left" if perp[0] > 0.3 else ("right" if perp[0] < -0.3 else "center")
        off = 0.2 if align != "center" else 0.15 + 0.5 * fs * _fig.UPP
        lab = Text(label, position=0.5 * (A2 + B2) + off * perp, font_size=fs, color=col, align=align)
        obj.add(lab)
    return obj


def _build_area(args, style, axes):
    """Filled area UNDER a curve y=f(x) over [x_min,x_max], or BETWEEN two curves f and g (g = `func2`;
    empty -> baseline y=0). A closed polygon sampled along the top (a->b) and bottom (b->a), filled with
    the style colour/opacity. General: any function(s) via expression, any interval."""
    f = _as_func(args.get("func", "0"))
    g_raw = str(args.get("func2", "")).strip()
    g = func_from_expr(g_raw) if g_raw else None
    a, b = float(args.get("x_min", 0.0)), float(args.get("x_max", 1.0))
    if b < a:
        a, b = b, a
    n = max(2, int(args.get("samples", 64)))
    lo, hi = (axes.y_min, axes.y_max) if axes is not None else (-1e9, 1e9)
    base_y = float(axes.y_min) if (axes is not None and getattr(axes, "y_log", False)) else 0.0   # log axis has no 0

    def ev(fn, x):                                            # safe eval, clamped into the y-range (tames poles)
        try:
            v = float(fn(x))
        except Exception:
            v = lo
        if not np.isfinite(v):
            v = lo
        return min(hi, max(lo, v))

    if axes is not None and getattr(axes, "x_log", False) and a > 0:
        xs = np.logspace(np.log10(a), np.log10(b), n + 1)     # log axis: even density per decade
    else:
        xs = np.linspace(a, b, n + 1)
    top = [(float(x), ev(f, x), 0.0) for x in xs]
    bot = ([(float(x), ev(g, x), 0.0) for x in xs[::-1]] if g is not None
           else [(b, base_y, 0.0), (a, base_y, 0.0)])
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


def _build_polar_curve(args, style, axes):
    """A polar curve r(theta): points (r·cos θ, r·sin θ) as a polyline with orientation arrowhead.
    Variable `theta` (alias `t`). General: cardioids, roses, spirals, ..."""
    c2p = _c2p_fn(axes)
    names = _safe_names()
    code = compile(normalize_expr(str(args.get("func", "1+cos(theta)"))), "<polar>", "eval")

    def rval(a):
        try:
            return float(eval(code, {"__builtins__": {}}, {"theta": a, "t": a, **names}))
        except Exception:
            return float("nan")

    a0, a1 = float(args.get("theta_min", 0.0)), float(args.get("theta_max", 6.283185))
    n = max(2, int(args.get("samples", 200)))
    th = np.linspace(a0, a1, n)
    col = style.get("color", (0.35, 0.60, 0.92))
    sw = float(style.get("stroke_width", 4.0))

    def XY(a):
        r = rval(a)
        return r * np.cos(a), r * np.sin(a)

    raw = [XY(a) for a in th]
    pts = [np.array([x, y, 0.0]) for (x, y) in raw if np.isfinite(x) and np.isfinite(y)]
    obj = AnimObject()
    if len(pts) >= 2:
        poly = Polygon(pts, closed=False)
        poly.color = col
        poly.stroke_width = sw
        obj.add(poly)
    if axes is not None:
        axes.place(obj)
    if args.get("show_arrow", True) and n >= 3:
        i = max(1, min(n - 2, int(0.55 * (n - 1))))
        wa = c2p(*XY(th[i - 1]))
        wb = c2p(*XY(th[i + 1]))
        d = wb - wa
        L = float(np.linalg.norm(d))
        if L > 1e-9:
            tdir = d / L
            perp = np.array([-tdir[1], tdir[0], 0.0])
            tip = c2p(*XY(th[i]))
            head = 0.22
            back = tip - head * tdir
            tri = Polygon([tip, back + 0.5 * head * perp, back - 0.5 * head * perp], closed=True)
            tri.color = col
            tri.fill_color = col
            tri.fill_opacity = 1.0
            tri.stroke_width = sw
            obj.add(tri)
    return obj


def _build_number_line(args, style, axes):
    """A standalone 1D number line (independent of the scene Axes): a main line of world length `length`
    centred at `center`, with tick marks at multiples of `step` from x_min to x_max and optional labels."""
    c2p = _c2p_fn(axes)
    RIGHT = np.array([1.0, 0.0, 0.0])
    UP = np.array([0.0, 1.0, 0.0])
    x0, x1 = float(args.get("x_min", -5.0)), float(args.get("x_max", 5.0))
    if x1 <= x0:
        x1 = x0 + 1.0
    step = float(args.get("step", 1.0)) or 1.0
    length = float(args.get("length", 10.0))
    c = c2p(*_xyz(args.get("center", [0.0, 0.0, 0.0])))
    col = style.get("color", (0.1, 0.1, 0.1))
    sw = float(style.get("stroke_width", 3.0))
    labels = bool(args.get("tick_labels", True))
    dec = int(args.get("decimals", 0))
    fs = float(args.get("font_size", 24))
    obj = AnimObject()
    main = Line(c - 0.5 * length * RIGHT, c + 0.5 * length * RIGHT)
    main.color = col
    main.stroke_width = sw
    obj.add(main)
    v = x0
    vals = []
    while v <= x1 + step * 0.5:
        vals.append(round(v, 9))
        v += step
    for val in vals:
        frac = (val - x0) / (x1 - x0)
        p = c + (frac - 0.5) * length * RIGHT
        tick = Line(p - 0.12 * UP, p + 0.12 * UP)
        tick.color = col
        tick.stroke_width = sw
        obj.add(tick)
        if labels:
            obj.add(Text(f"{val:.{dec}f}", position=p - 0.38 * UP, font_size=fs, color=col))
    return obj


def _build_parametric_curve(args, style, axes):
    """A parametric curve (x(t), y(t)) as a polyline, with an orientation arrowhead along the sweep and
    an optional running point with tangent/normal vectors. General: any expressions in t."""
    c2p = _c2p_fn(axes)
    names = _safe_names()
    cx = compile(normalize_expr(str(args.get("fx", "cos(t)"))), "<px>", "eval")
    cy = compile(normalize_expr(str(args.get("fy", "sin(t)"))), "<py>", "eval")

    def ev(code, t):
        try:
            return float(eval(code, {"__builtins__": {}}, {"t": t, **names}))
        except Exception:
            return float("nan")

    def P(t):
        return ev(cx, t), ev(cy, t)

    t0, t1 = float(args.get("t_min", 0.0)), float(args.get("t_max", 6.283185))
    n = max(2, int(args.get("samples", 160)))
    ts = np.linspace(t0, t1, n)
    col = style.get("color", (0.35, 0.60, 0.92))
    sw = float(style.get("stroke_width", 4.0))
    raw = [P(t) for t in ts]
    pts = [np.array([x, y, 0.0]) for (x, y) in raw if np.isfinite(x) and np.isfinite(y)]
    obj = AnimObject()
    if len(pts) >= 2:
        poly = Polygon(pts, closed=False)
        poly.color = col
        poly.stroke_width = sw
        obj.add(poly)
    if axes is not None:
        axes.place(obj)                                      # map the polyline; decorations below are world-space

    def world(t):
        x, y = P(t)
        return c2p(x, y)

    if args.get("show_arrow", True) and n >= 3:
        i = max(1, min(n - 2, int(0.55 * (n - 1))))
        a, b = world(ts[i - 1]), world(ts[i + 1])
        d = b - a
        L = float(np.linalg.norm(d))
        if L > 1e-9:
            tdir = d / L
            perp = np.array([-tdir[1], tdir[0], 0.0])
            tip = world(ts[i])
            head = 0.22
            back = tip - head * tdir
            tri = Polygon([tip, back + 0.5 * head * perp, back - 0.5 * head * perp], closed=True)
            tri.color = col
            tri.fill_color = col
            tri.fill_opacity = 1.0
            tri.stroke_width = sw
            obj.add(tri)
    pa = str(args.get("point_at", "")).strip()
    if pa:
        try:
            tp = float(pa)
            x, y = P(tp)
            if np.isfinite(x) and np.isfinite(y):
                w = c2p(x, y)
                dot = OBJECT_TYPES["Dot"](center=w, radius=0.09)
                dot.color = col
                dot.fill_color = col
                dot.fill_opacity = 1.0
                obj.add(dot)
                h = 1e-4 * max(1.0, abs(tp))
                tdx = (ev(cx, tp + h) - ev(cx, tp - h)) / (2 * h)
                tdy = (ev(cy, tp + h) - ev(cy, tp - h)) / (2 * h)
                tn = float(np.hypot(tdx, tdy))
                if np.isfinite(tn) and tn > 1e-9:
                    sc = 0.8
                    if args.get("show_tangent", False):
                        obj.add(Vector(end=c2p(x + sc * tdx / tn, y + sc * tdy / tn), start=w, color=col, stroke_width=sw))
                    if args.get("show_normal", False):
                        obj.add(Vector(end=c2p(x - sc * tdy / tn, y + sc * tdx / tn), start=w,
                                       color=(0.9, 0.45, 0.15), stroke_width=sw))
        except Exception:
            pass
    return obj


def _build_curve_family(args, style, axes):
    """A family of curves f(x; p): the parameter `param` sweeps `count` values from p_min to p_max, each
    drawn as its own polyline (optionally fading light->colour with rising p), plus an optional limit
    curve. General: any expression in x and one named parameter (Fourier harmonics, Fermi-Dirac over T,
    kernels over r/ε, ...)."""
    c2p = _c2p_fn(axes)
    param = str(args.get("param", "k")).strip() or "k"
    code = compile(normalize_expr(str(args.get("func", "0"))), "<fam>", "eval")
    names = _safe_names()

    def fval(x, p):
        try:
            v = float(eval(code, {"__builtins__": {}}, {"x": x, param: p, **names}))
        except Exception:
            return float("nan")
        return v

    if axes is not None:
        x0 = float(args.get("x_min", axes.x_min)); x1 = float(args.get("x_max", axes.x_max))
        ylo, yhi = axes.y_min, axes.y_max
    else:
        x0, x1 = float(args.get("x_min", -6.0)), float(args.get("x_max", 6.0))
        ylo, yhi = -1e9, 1e9
    n = max(2, int(args.get("samples", 120)))
    count = max(1, int(args.get("count", 5)))
    p0, p1 = float(args.get("p_min", 1.0)), float(args.get("p_max", 5.0))
    fade = bool(args.get("fade", True))
    base = np.array(style.get("color", (0.35, 0.60, 0.92)), dtype=float)
    white = np.array([1.0, 1.0, 1.0])
    sw = float(style.get("stroke_width", 3.0))
    if axes is not None and getattr(axes, "x_log", False) and x0 > 0 and x1 > 0:
        xs = np.logspace(np.log10(x0), np.log10(x1), n)
    else:
        xs = np.linspace(x0, x1, n)
    # explicit parameter values ("1;1.5;2;2.5") win over the p_min..p_max sweep (characteristic fields)
    vals = [float(v) for v in re.findall(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?", str(args.get("values", "")))]
    ps = np.array(vals) if vals else np.linspace(p0, p1, count)
    count = len(ps)
    labels = [t.strip() for t in str(args.get("labels", "")).split(";")] if str(args.get("labels", "")).strip() else []
    fs = float(args.get("font_size", 24))

    def clamp(v):
        if not np.isfinite(v):
            return ylo
        return min(yhi, max(ylo, v))

    obj = AnimObject()
    label_objs = []
    for i, p in enumerate(ps):
        pts = [np.array([float(x), clamp(fval(x, p)), 0.0]) for x in xs]
        poly = Polygon(pts, closed=False)
        if fade and count > 1:
            mix = 0.3 + 0.7 * (i / (count - 1))
            poly.color = tuple(white * (1.0 - mix) + base * mix)
        else:
            poly.color = tuple(base)
        poly.stroke_width = sw
        obj.add(poly)
        if i < len(labels) and labels[i]:                   # label at the right end of curve i
            label_objs.append((labels[i], pts[-1], poly.color))
    lim = str(args.get("limit_func", "")).strip()
    if bool(args.get("show_limit", False)) and lim:
        g = func_from_expr(lim)
        pts = []
        for x in xs:
            try:
                v = float(g(x))
            except Exception:
                v = float("nan")
            pts.append(np.array([float(x), clamp(v), 0.0]))
        lp = Polygon(pts, closed=False)
        lp.color = (0.1, 0.1, 0.1)
        lp.stroke_width = sw + 2.0
        obj.add(lp)
    if axes is not None:
        axes.place(obj)
    for text, end, colr in label_objs:                      # labels in world units (no data scaling of the offset)
        obj.add(Text(text, position=c2p(end[0], end[1]) + np.array([0.15, 0.0, 0.0]), font_size=fs,
                     color=colr, align="left"))
    return obj


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
    head = float(args.get("head_size", 0.3))
    thick = float(args.get("thick", 0.0))
    elbow = str(args.get("elbow", "none"))
    # route: straight, or right-angled (hv = horizontal first, vh = vertical first) through a corner
    pts = [A, B]
    if elbow in ("hv", "vh") and abs(B[0] - A[0]) > 1e-9 and abs(B[1] - A[1]) > 1e-9:
        corner = np.array([B[0], A[1], 0.0]) if elbow == "hv" else np.array([A[0], B[1], 0.0])
        pts = [A, corner, B]
    if thick > 0:                                       # filled quantity/flow arrow of width `thick`
        last_d = pts[-1] - pts[-2]
        Ld = float(np.linalg.norm(last_d))
        u = last_d / Ld if Ld > 1e-9 else np.array([1.0, 0.0, 0.0])
        hl = min(1.6 * thick, 0.5 * Ld)                 # head length
        base = pts[-1] - hl * u
        perp = np.array([-u[1], u[0], 0.0])
        # polygon along the (possibly bent) spine with half-width thick/2 (straight segments only)
        left, right = [], []
        for i in range(len(pts) - 1):
            a, b = pts[i], (base if i == len(pts) - 2 else pts[i + 1])
            dd = b - a; n = float(np.linalg.norm(dd)); dd = dd / n if n > 1e-9 else u
            pp = np.array([-dd[1], dd[0], 0.0]) * (thick / 2)
            left += [a + pp, b + pp]; right += [a - pp, b - pp]
        outline = left + [base + perp * thick, pts[-1], base - perp * thick] + right[::-1]
        poly = Polygon(outline, closed=True)
        poly.color = col; poly.fill_color = col; poly.fill_opacity = 0.9; poly.stroke_width = 0.0
        poly._no_dash = True
        obj.add(poly)
    else:
        for i in range(len(pts) - 1):
            seg = Line(pts[i], pts[i + 1]); seg.color = col; seg.stroke_width = sw
            obj.add(seg)
        d_end = pts[-1] - pts[-2]
        obj.add(_ah(pts[-1], d_end, col, head))
        if args.get("double", False):
            obj.add(_ah(pts[0], pts[0] - pts[1], col, head))
    label = str(args.get("label", "")).strip()
    if label:
        fs = float(args.get("font_size", 28))
        # label beside the longest straight segment, on its left-hand side; text reads AWAY from the line
        segs = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
        P, Q = max(segs, key=lambda s: float(np.linalg.norm(s[1] - s[0])))
        d = Q - P
        L = float(np.linalg.norm(d))
        perp = np.array([0.0, 0.0, 0.0]) if L < 1e-9 else np.array([-d[1], d[0], 0.0]) / L
        align = "left" if perp[0] > 0.3 else ("right" if perp[0] < -0.3 else "center")
        off = thick / 2 + (0.18 if align != "center" else 0.15 + 0.5 * fs * _fig.UPP)
        if str(args.get("label_at", "mid")) == "end":
            anchor = B + (0.18 + 0.5 * fs * _fig.UPP) * perp
        else:
            anchor = 0.5 * (P + Q) + off * perp
        obj.add(Text(label, position=anchor, font_size=fs, color=col, align=align))
    return obj


def _ah(tip, direction, col, size):
    h = ArrowHead(tip, direction, size=size)
    h.color = col
    h.fill_color = col
    return h


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
    if args.get("head", True):                                  # head:false -> a plain arc (angle mark, arc)
        s = 1.0 if a1 >= a0 else -1.0                           # sweep direction -> tangent at the end
        tan = s * np.array([-np.sin(a1), np.cos(a1), 0.0])
        obj.add(_ah(pts[-1], tan, col, max(0.12, 0.3 * r)))
    label = str(args.get("label", "")).strip()
    if label:
        obj.add(Text(label, position=c, font_size=float(args.get("font_size", 28)), color=col))
    return obj


def _build_tangent(args, style, axes):
    """Tangent (or secant) line to a graph y=f(x). Tangent slope via central difference at x0; secant
    slope via (f(x1)-f(x0))/(x1-x0). The line runs ±half_len in x; optional touch-point dot(s) and a
    slope label. General: any function/expression, any point(s). Built in world coords (no distortion)."""
    c2p = _c2p_fn(axes)
    f = _as_func(args.get("func", "0"))
    # Work in PLOT space (u, w): u = x or log10 x, w = y or log10 y, so on a (semi)logarithmic axes the
    # tangent is the straight line the reader sees (an exponential on a log-y axis has a constant slope
    # in decades per unit x). On linear axes this is exactly the data-space tangent.
    xl = axes is not None and getattr(axes, "x_log", False)
    yl = axes is not None and getattr(axes, "y_log", False)
    X = (lambda x: float(np.log10(x))) if xl else (lambda x: float(x))
    Xi = (lambda u: 10.0 ** u) if xl else (lambda u: u)
    Yi = (lambda w: 10.0 ** w) if yl else (lambda w: w)

    def F(u):
        try:
            v = float(f(Xi(u)))
            if yl:
                v = float(np.log10(v)) if v > 0 else float("nan")
            return v if np.isfinite(v) else 0.0
        except Exception:
            return 0.0

    def P(u, w):
        return c2p(Xi(u), Yi(w))

    x0 = float(args.get("x0", 0.0))
    if xl and x0 <= 0:
        x0 = float(axes.x_min)
    u0 = X(x0)
    w0 = F(u0)
    half = float(args.get("half_len", 2.0))
    secant = bool(args.get("secant", False))
    pts = [(u0, w0)]
    if secant:
        x1 = float(args.get("x1", x0 + 1.0))
        if xl and x1 <= 0:
            x1 = float(axes.x_max)
        u1 = X(x1)
        w1 = F(u1)
        m = (w1 - w0) / (u1 - u0) if abs(u1 - u0) > 1e-12 else 0.0
        ua, ub = min(u0, u1) - half, max(u0, u1) + half
        pts.append((u1, w1))
    else:
        h = 1e-4 * max(1.0, abs(u0))
        m = (F(u0 + h) - F(u0 - h)) / (2.0 * h)
        ua, ub = u0 - half, u0 + half
    col = style.get("color", (0.0, 0.0, 0.0))
    obj = AnimObject()
    ln = Line(P(ua, w0 + m * (ua - u0)), P(ub, w0 + m * (ub - u0)))
    ln.color = col
    ln.stroke_width = float(style.get("stroke_width", 3.0))
    obj.add(ln)
    if args.get("show_point", True):
        for (pu, pw) in pts:
            d = OBJECT_TYPES["Dot"](center=P(pu, pw), radius=0.08)
            d.color = col
            d.fill_color = col
            d.fill_opacity = 1.0
            d._no_dash = True
            obj.add(d)
    if args.get("show_slope", False):
        lab = Text(f"m = {m:.3g}", position=P(u0, w0) + np.array([0.25, 0.25, 0.0]),
                   font_size=float(args.get("font_size", 26)), color=col, align="left")
        obj.add(lab)
    tdx = float(args.get("triangle_dx", 0.0))
    if tdx > 0:                                             # slope triangle: Δx along, Δy up, both labelled
        Pa, Pb, Pc = P(u0, w0), P(u0 + tdx, w0), P(u0 + tdx, w0 + m * tdx)
        tri = Polygon([Pa, Pb, Pc], closed=True)
        tri.color = col; tri.fill_color = col; tri.fill_opacity = 0.12; tri.stroke_width = 0.6 * float(style.get("stroke_width", 3.0))
        tri._no_dash = True
        obj.add(tri)
        fs = float(args.get("font_size", 26))
        dxl = str(args.get("dx_label", "\\Delta x")).strip()
        dyl = str(args.get("dy_label", "\\Delta y")).strip()
        sgn = 1.0 if m >= 0 else -1.0
        if dxl:
            obj.add(Text(dxl, position=0.5 * (Pa + Pb) + np.array([0.0, -sgn * 0.75 * fs * _fig.UPP, 0.0]), font_size=fs, color=col))
        if dyl:
            obj.add(Text(dyl, position=0.5 * (Pb + Pc) + np.array([0.3, 0.0, 0.0]), font_size=fs, color=col, align="left"))
    return obj


# Builders that compile `func` themselves with extra variables (theta, a family parameter, x AND y):
# they must receive the expression TEXT, not the one-variable function _resolve_arg would make of it.
_RAW_FUNC_TYPES = {"PolarCurve", "CurveFamily", "ScalarField"}


def _build_object(spec, objects, axes=None):
    t = spec["type"]
    args = {k: (v if (k == "func" and t in _RAW_FUNC_TYPES) else _resolve_arg(k, v))
            for k, v in spec.get("args", {}).items()}
    # Styling is set as attributes AFTER construction (shapes don't take color in __init__).
    style = {k: args.pop(k) for k in list(args) if k in _STYLE_ATTRS}
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
    elif t == "CurveFamily":                                # family of curves f(x;p) over a parameter
        obj = _build_curve_family(args, style, axes)
    elif t == "ParametricCurve":                            # (x(t),y(t)) with orientation / running point
        obj = _build_parametric_curve(args, style, axes)
    elif t == "PolarCurve":                                 # r(theta) polar plot
        obj = _build_polar_curve(args, style, axes)
    elif t == "NumberLine":                                 # standalone 1D axis with ticks + labels
        obj = _build_number_line(args, style, axes)
    elif t == "Parameter":                                  # a scene parameter: no geometry (value lives in _PARAMS)
        obj = AnimObject()
    elif t in _fig.BUILDERS:                                # data curves, bands, stems, clouds, boxes, braces, marks, shapes, tables
        obj = _fig.BUILDERS[t](args, style, axes)
    elif t in _circ.BUILDERS:                               # circuit symbols: components, devices, wires, nodes
        obj = _circ.BUILDERS[t](args, style, axes)
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
    dash = _parse_dash(style.pop("dash", None))
    for k, v in style.items():
        setattr(obj, k, v)
    if dash is not None:                                    # dashed stroke: the object and its strokable parts
        obj.set_dash(dash)
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
        # Scene parameters first: their names must be known before any expression is compiled.
        _PARAMS.clear()
        for spec in specs:
            if spec["type"] == "Parameter":
                a = spec.get("args", {})
                name = str(a.get("name", "")).strip()
                if name:
                    try:
                        _PARAMS[name] = float(a.get("value", 0.0))
                    except (TypeError, ValueError):
                        pass
        # Build ALL Axes first so FunctionGraphs can be plotted onto them (and thus follow their value
        # range + scaling), regardless of the order objects were added. Several Axes = sub-figures: an
        # object names its panel with `on` (an Axes id); without it, the first Axes is used.
        axes = None
        axes_by_id = {}
        for spec in specs:
            if spec["type"] == "Axes":
                ax = _build_object(spec, objects)
                if spec.get("id") is not None:
                    objects[spec["id"]] = ax
                    axes_by_id[spec["id"]] = ax
                if axes is None:
                    axes = ax
        self.axes_by_id = axes_by_id
        built = []
        for spec in specs:
            oid = spec.get("id")
            if oid is not None and oid in objects:          # the axes we already built above
                obj = objects[oid]
            else:
                on = axes_by_id.get(spec.get("on"), axes)
                obj = _build_object(spec, objects, axes=on)
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
        self._appearance_anims = []                         # Create/FadeIn/... (kept fully shown statically)
        for step in _group_by_step(self.model.get("animations", [])):
            anims = []
            for spec in step:
                if spec.get("target") not in objects:       # dangling reference (deleted object) -> skip
                    continue
                a = _build_animation(spec, objects)
                a.run_time = spec.get("run_time", 1.0)
                anims.append(a)
                if spec.get("type") in _APPEARANCE:
                    self._appearance_anims.append(a)
            if anims:
                self.play(*anims)                           # run_time=None -> each keeps its own
        if self.model.get("wait"):
            self.wait(self.model["wait"])
        self.run_updaters()          # settle updater-driven objects for the static (first) frame

    def show_static(self):
        """Edit-view (non-playing) state. construct() leaves animation targets at their END state (play()
        advances each to the end so the next begin() is correct). For the static editor we instead want
        TRANSFORM targets (Rotate/Shift/Scale/MoveTo) at their START — where they begin — so the resting
        view matches the animation's first frame, not its last. Appearance targets (Create/FadeIn/Write/
        GrowFromCenter) are then forced fully shown so they stay visible and selectable in the editor."""
        if self.timeline:
            self.seek(0.0)                                   # all animations -> their t=0 (start) state
            for a in getattr(self, "_appearance_anims", []):
                a.update(1.0)                                # ...but appearance targets stay fully shown
            self.run_updaters()
        return self


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
