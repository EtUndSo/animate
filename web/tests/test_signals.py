import sys, numpy as np
sys.path.insert(0, ".")
from engine import scene_model as SM
from engine.scene_model import func_from_expr, ModelScene
from engine.text import DecimalNumber

# ET3 standard functions (t works as the variable)
assert func_from_expr("epsilon(t)")(-1) == 0 and func_from_expr("epsilon(t)")(2) == 1
assert func_from_expr("rect(t)")(0) == 1 and func_from_expr("rect(t)")(1) == 0
assert abs(func_from_expr("tri(t)")(0.5) - 0.5) < 1e-9 and func_from_expr("tri(t)")(2) == 0
assert func_from_expr("ramp(t)")(3) == 3 and func_from_expr("ramp(t)")(-2) == 0
assert abs(func_from_expr("si(t)")(0) - 1.0) < 1e-9                 # sin(t)/t -> 1 at 0
assert abs(func_from_expr("2 rect(t) + epsilon(t-1)")(0) - 2.0) < 1e-9   # implicit mult + shift
print("ET3 signals OK: epsilon/rect/tri/ramp/si, t-variable, implicit mult")

# complex: j is the imaginary unit; e^(j*t) = cos t + j sin t
f = func_from_expr("exp(j*t)")
assert abs(np.real(f(0)) - 1) < 1e-9 and abs(np.imag(f(np.pi/2)) - 1) < 1e-9
print("complex expr OK: exp(j*t) @0 real=1, @pi/2 imag=1")

# complex DOMAIN: a FunctionGraph builds Re and Im parts
model = {
    "domain": "complex",
    "objects": [
        {"id": "ax", "type": "Axes", "args": {"x_range": [-6, 6], "y_range": [-1.5, 1.5], "x_length": 12, "y_length": 5}},
        {"id": "g", "type": "FunctionGraph", "args": {"func": "exp(j*t)", "color": [0.2, 0.4, 0.9], "stroke_width": 4}},
    ],
    "animations": [], "background": [1, 1, 1],
}
sc = ModelScene(model); sc.construct()
g = sc.objects_by_id["g"]
assert hasattr(g, "_cx_parts") and len(g.subObjects) == 2, "complex graph should have Re + Im"
print("complex domain OK: FunctionGraph -> Re + Im (2 curves)")

# real domain unchanged (single curve)
model["domain"] = "real"; model["objects"][1]["args"]["func"] = "sin(t)"
sc2 = ModelScene(model); sc2.construct()
g2 = sc2.objects_by_id["g"]
assert not hasattr(g2, "_cx_parts")
print("real domain OK: single curve")
print("\nSIGNALS/COMPLEX TESTS PASSED")
