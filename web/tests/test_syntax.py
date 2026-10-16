import sys, numpy as np
sys.path.insert(0, ".")
from engine.scene_model import normalize_expr, func_from_expr

cases = {
    "3x": "3*x",
    "x^2": "x**2",
    "3x^2+2x": "3*x**2+2*x",
    "2sin(x)": "2*sin(x)",
    "sin(x)": "sin(x)",
    "x(x+1)": "x*(x+1)",
    "(x+1)(x-1)": "(x+1)*(x-1)",
    "2pi": "2*pi",
    "exp(x)": "exp(x)",
    "3 x": "3*x",
    "x sin(x)": "x*sin(x)",
    "2x^2 - 3x + 1": "2*x**2-3*x+1",
    "sqrt(x)": "sqrt(x)",
    "e^x": "e**x",
}
for src, want in cases.items():
    got = normalize_expr(src)
    assert got == want, f"{src!r} -> {got!r}  (want {want!r})"
print("normalize_expr OK (%d cases)" % len(cases))

# evaluates correctly
f = func_from_expr("3x^2")
assert abs(f(2) - 12) < 1e-9, f(2)
g = func_from_expr("(x+1)(x-1)")
assert abs(g(3) - 8) < 1e-9, g(3)        # 4*2 = 8
h = func_from_expr("2sin(x)")
assert abs(h(np.pi/2) - 2) < 1e-9, h(np.pi/2)
print("func eval OK: 3x^2 @2=12, (x+1)(x-1) @3=8, 2sin(pi/2)=2")
print("\nSYNTAX TESTS PASSED")
