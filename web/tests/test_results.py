import sys, numpy as np
sys.path.insert(0, ".")
from engine.results import result_value

# scalar results (data units)
assert abs(result_value("Circle","area",{"radius":2.0},None) - np.pi*4) < 1e-9
assert abs(result_value("Circle","circumference",{"radius":2.0},None) - 4*np.pi) < 1e-9
assert abs(result_value("Line","length",{"start":[0,0,0],"end":[3,4,0]},None) - 5.0) < 1e-9
assert abs(result_value("Line","slope",{"start":[0,0,0],"end":[2,4,0]},None) - 2.0) < 1e-9
assert abs(result_value("Square","diagonal",{"side":2.0},None) - 2*np.sqrt(2)) < 1e-9
f = lambda x: x    # integral of x over [0,2] = 2
assert abs(result_value("FunctionGraph","integral",{"func":f,"x_range":[0,2]},None) - 2.0) < 1e-6
assert result_value("Axes","area",{},None) is None
print("results registry OK")
print("\nRESULTS TESTS PASSED")
