"""Result registry: which computed value each object type can expose (see RESULTS.md).

Each entry is compute(parent_args, axes) -> float, where parent_args are the parent object's
(resolved) construction args in DATA units, and axes is the scene's Axes (or None). The interpreter
runs the matching function for a `result`-tagged child and feeds the number into its DecimalNumber;
the child's prefix carries the symbol/formula ("A = pr^2 = "), so the label reads symbol = formula = value.
Only STATIC scalar results for now; geometric (roots/extrema -> points) and dynamic
(animation-driven) results follow.
"""
import numpy as np


def _integral(f, x0, x1, n=400):
    # Trapezoidal rule, computed directly (no np.trapz / np.trapezoid - the name differs across
    # numpy versions, and this must also run under Pyodide's numpy).
    xs = np.linspace(x0, x1, n)
    ys = np.array([f(x) for x in xs], dtype=float)
    return float(np.sum((ys[:-1] + ys[1:]) * 0.5 * np.diff(xs)))


def _xrange(args, axes):
    if axes is not None:
        return axes.x_min, axes.x_max                 # what is actually drawn follows the axes
    r = args.get("x_range", (-4, 4))
    return r[0], r[1]


def _slope(a):
    s = np.asarray(a["start"], dtype=float)
    e = np.asarray(a["end"], dtype=float)
    dx = e[0] - s[0]
    return float((e[1] - s[1]) / dx) if abs(dx) > 1e-12 else float("inf")


def _riemann_area(a, axes):
    f, n = a["func"], int(a.get("count", 8))
    x0, x1 = _xrange(a, axes)
    dx = (x1 - x0) / n
    return float(sum(f(x0 + (i + 0.5) * dx) for i in range(n)) * dx)


RESULTS = {
    "Circle": {
        "radius":        lambda a, ax: float(a["radius"]),
        "area":          lambda a, ax: float(np.pi * a["radius"] ** 2),
        "circumference": lambda a, ax: float(2 * np.pi * a["radius"]),
    },
    "Rectangle": {
        "width":     lambda a, ax: float(a["width"]),
        "height":    lambda a, ax: float(a["height"]),
        "area":      lambda a, ax: float(a["width"] * a["height"]),
        "perimeter": lambda a, ax: float(2 * (a["width"] + a["height"])),
        "diagonal":  lambda a, ax: float(np.hypot(a["width"], a["height"])),
    },
    "Square": {
        "side":      lambda a, ax: float(a["side"]),
        "area":      lambda a, ax: float(a["side"] ** 2),
        "perimeter": lambda a, ax: float(4 * a["side"]),
        "diagonal":  lambda a, ax: float(np.sqrt(2) * a["side"]),
    },
    "Line": {
        "length": lambda a, ax: float(np.linalg.norm(np.asarray(a["end"], float) - np.asarray(a["start"], float))),
        "slope":  lambda a, ax: _slope(a),
    },
    "FunctionGraph": {
        "integral": lambda a, ax: _integral(a["func"], *_xrange(a, ax)),
    },
    "Riemann": {
        "area":  lambda a, ax: _riemann_area(a, ax),
        "error": lambda a, ax: abs(_riemann_area(a, ax) - _integral(a["func"], *_xrange(a, ax))),
    },
}


def result_value(parent_type, key, parent_args, axes):
    """Compute one result, or None if that (type, key) is not in the registry."""
    fn = RESULTS.get(parent_type, {}).get(key)
    return None if fn is None else fn(parent_args, axes)
