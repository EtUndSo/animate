"""Declarative scene model.

A scene is described as plain data (objects + animations). This single representation is the
bridge for the web app: the visual editor edits it, we generate code from it (for the code
page), and the interpreter builds a renderable Scene from it (for the live preview / export).
So editor, code page, preview and export always stay in sync.
"""
import numpy as np

from .scene import Scene
from .axes import Axes
from .simpleShape import (Circle, Dot, Line, Polygon, Triangle, Rectangle, Square, FunctionGraph)
from .text import Text
from . import animation as _anim
from . import constants as _const

# --- registries: add a class here to expose it to the editor + code + interpreter ---
OBJECT_TYPES = {
    "Axes": Axes, "Circle": Circle, "Dot": Dot, "Line": Line, "Polygon": Polygon,
    "Triangle": Triangle, "Rectangle": Rectangle, "Square": Square,
    "FunctionGraph": FunctionGraph, "Text": Text,
}
ANIMATION_TYPES = {
    "Create": _anim.Create, "FadeIn": _anim.FadeIn,
    "Shift": _anim.Shift, "GrowFromCenter": _anim.GrowFromCenter,
}
# Animations that make their target APPEAR, so we must NOT pre-add that target.
_APPEARANCE = {"Create", "FadeIn", "GrowFromCenter"}

# Whitelisted names for user math expressions (no builtins -> safe even server-side).
_SAFE_NAMES = {n: getattr(np, n) for n in
               ["sin", "cos", "tan", "exp", "log", "sqrt", "abs", "pi", "e",
                "sinh", "cosh", "tanh", "arctan", "sign"]}


def func_from_expr(expr):
    """'sin(x)' -> f(x), evaluated in a restricted namespace (no builtins): safe."""
    code = compile(str(expr), "<func>", "eval")
    return lambda x: eval(code, {"__builtins__": {}}, {"x": x, **_SAFE_NAMES})


def _resolve_arg(key, value):
    """Turn a model arg value into a real Python value."""
    if isinstance(value, str):
        if value.isupper() and hasattr(_const, value):     # BLUE, RIGHT, ORIGIN, ...
            return getattr(_const, value)
        if key == "func":
            return func_from_expr(value)
    return value


def _build_object(spec, objects):
    args = {k: _resolve_arg(k, v) for k, v in spec.get("args", {}).items()}
    if spec["type"] == "plot":                              # a graph on an axes: axes.plot(...)
        return objects[spec["on"]].plot(**args)
    return OBJECT_TYPES[spec["type"]](**args)


def _build_animation(spec, objects):
    args = {k: _resolve_arg(k, v) for k, v in spec.get("args", {}).items()}
    return ANIMATION_TYPES[spec["type"]](objects[spec["target"]], **args)


class ModelScene(Scene):
    """A Scene built from a declarative model. Render it like any scene (render / render_video)."""

    def __init__(self, model):
        super().__init__()
        self.model = model

    def construct(self):
        objects = {}
        appearing = {a["target"] for a in self.model.get("animations", [])
                     if a["type"] in _APPEARANCE}
        for spec in self.model.get("objects", []):
            obj = _build_object(spec, objects)
            oid = spec.get("id")
            if oid is not None:
                objects[oid] = obj
            if oid not in appearing:                        # appearance targets are added by play()
                self.add(obj)
        for spec in self.model.get("animations", []):
            self.play(_build_animation(spec, objects), run_time=spec.get("run_time", 1.0))
        if self.model.get("wait"):
            self.wait(self.model["wait"])


# ---------------------------------------------------------------------------
#  Code generation: model -> Python source (what the "programming page" shows)
# ---------------------------------------------------------------------------
def _arg_to_code(key, value):
    if key == "func" and isinstance(value, str):
        return f"lambda x: {value}"
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
    for spec in model.get("animations", []):
        extra = _args_code(spec.get("args", {}))
        extra = (", " + extra) if extra else ""
        lines.append(f"        self.play({spec['type']}({spec['target']}{extra}), "
                     f"run_time={spec.get('run_time', 1.0)})")
    if model.get("wait"):
        lines.append(f"        self.wait({model['wait']})")
    return "\n".join(lines)
