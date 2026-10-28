"""Robustness of scene building: an unknown prop must not abort the whole scene, and a Parameter
whose name is a built-in variable/function must fail loudly instead of silently giving a wrong curve."""
import sys
sys.path.insert(0, ".")
from engine.scene_model import ModelScene


def build(objs):
    sc = ModelScene({"objects": objs, "animations": [], "background": [1, 1, 1]})
    sc.construct()
    return sc


# unknown props are skipped (older scene files, typos), the rest of the scene still builds
sc = build([{"id": "t", "type": "Text", "args": {"text": "A", "rotation": 30}},
            {"id": "c", "type": "Circle", "args": {"radius": 1, "foo": 2}},
            {"id": "d", "type": "Dot", "args": {"point": [1, 0, 0]}}])
assert {"t", "c", "d"} <= set(sc.objects_by_id), sc.objects_by_id.keys()
print("unknown props skipped, scene built")

# reserved parameter names are rejected with a clear message
for bad in ["u", "e", "x", "max", "ln", "sin", "step", "1a", "a-b"]:
    try:
        build([{"id": "p", "type": "Parameter", "args": {"name": bad, "value": 1}}])
    except ValueError as err:
        assert "Parametername" in str(err), err
        continue
    raise AssertionError(f"parameter name not rejected: {bad}")
for good in ["UB", "fg", "p", "U_B", "k2"]:
    build([{"id": "p", "type": "Parameter", "args": {"name": good, "value": 1}},
           {"id": "ax", "type": "Axes", "args": {}},
           {"id": "g", "type": "FunctionGraph", "args": {"func": f"{good}*x"}}])
print("parameter names checked")
print("ROBUST TESTS PASSED")
