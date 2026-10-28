"""Expressions in scene files are untrusted (scenes can be opened via ?scene= links).
An eval namespace without builtins is not a sandbox, so every expression must pass the
whitelist of scene_model._safe_compile: escapes are rejected, normal formulas still work."""
import sys
sys.path.insert(0, ".")
import numpy as np
from engine import scene_model as sm

ESCAPES = [
    "heaviside.__globals__['__builtins__']['len']([1,2,3])+0*x",   # module globals -> builtins
    "(1).__class__.__bases__",                                        # attribute walk
    "x[0]",                                                           # subscript
    "__import__('js')",                                               # dunder name
    "sin(x=1)",                                                       # keyword call
    "'text'",                                                         # string constant
    "lambda: 1",                                                      # lambda
    "[t for t in (1,2)]",                                             # comprehension
]
for src in ESCAPES:
    for build in (sm.func_from_expr, sm.func2_from_expr, sm.term_from_expr_i, sm.term_from_expr_ix):
        try:
            build(src)
        except ValueError:
            continue
        except SyntaxError:
            continue
        raise AssertionError(f"not rejected by {build.__name__}: {src}")
print("escapes rejected:", len(ESCAPES))

# the whitelist must not break ordinary formulas
x = np.array([0.5])
cases = {
    "3x^2": 0.75,
    "-x**2 + 1": 0.75,
    "where(x>0, x, 0)": 0.5,
    "max(x,0)+heaviside(x)": 1.5,
    "2pi*x": np.pi,
    "1e-14*exp(x/0.02585)": 1e-14 * np.exp(0.5 / 0.02585),
}
for src, want in cases.items():
    got = float(sm.func_from_expr(src)(x)[0])
    assert abs(got - want) <= 1e-12 * max(1.0, abs(want)), (src, got, want)
assert abs(sm.func2_from_expr("x*y + 1")(2.0, 3.0) - 7.0) < 1e-12
assert abs(sm.term_from_expr_i("1/i^2")(2) - 0.25) < 1e-12
assert abs(sm._eval_const("2*pi") - 2 * np.pi) < 1e-12
print("formulas ok:", len(cases) + 3)
print("SECURITY TESTS PASSED")
