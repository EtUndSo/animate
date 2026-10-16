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

# --- registries: add a class here to expose it to the editor + code + interpreter ---
OBJECT_TYPES = {
    "Axes": Axes, "Circle": Circle, "Dot": Dot, "Line": Line, "Polygon": Polygon,
    "Triangle": Triangle, "Rectangle": Rectangle, "Square": Square,
    "FunctionGraph": FunctionGraph, "Text": Text,
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
            obj = axes.plot_surface(func2_from_expr(raw), shade=_SHADOWS, **_surface_kw(args, style))
        else:
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
        global _ANGLE_UNIT, _DOMAIN, _SHADOWS, _CAM_ZOOM, _CAM_MODE
        _ANGLE_UNIT = self.model.get("angle_unit", "rad")   # set before any func is compiled
        _DOMAIN = self.model.get("domain", "real")
        _SHADOWS = bool(self.model.get("shadows", True))    # surface shading on/off
        cam = self.model.get("camera") or {}
        zoom = cam.get("zoom", 1.0)                         # orthographic zoom (>1 = magnified)
        _CAM_ZOOM = float(zoom)                             # so the Axes can refine its ticks with zoom (2D)
        _CAM_MODE = "3d" if cam.get("mode") == "3d" else "2d"
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
