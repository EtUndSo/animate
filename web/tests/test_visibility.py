"""Hiding an operation's INPUT function (eye toggle) must NOT hide the operation's OUTPUT graph.

A Convolution/Product/Sum/Difference graph is a result in its own right: the user may want to show only
the result and hide the inputs. So hidden objects are still BUILT (available as operands) - just not
drawn statically. See scene_model.construct()."""
from engine.scene_model import ModelScene


def _build(g_visible):
    model = {"objects": [
        {"id": "ax", "type": "Axes", "args": {}},
        {"id": "f", "type": "FunctionGraph", "visible": True, "args": {"func": "sin(x)", "x_range": [-3, 3]}},
        {"id": "g", "type": "FunctionGraph", "visible": g_visible, "args": {"func": "cos(x)", "x_range": [-3, 3]}},
    ], "animations": [], "computations": [
        {"id": "k1", "type": "Sum", "inputs": {"f": "f", "g": "g"}, "props": {"color": "#8b2fd6", "stroke_width": 4}},
    ], "camera": {"mode": "2d"}}
    sc = ModelScene(model)
    sc.construct()
    return len(sc.objectList)


def test_operation_survives_hidden_input():
    vis = _build(True)
    hid = _build(False)
    # hiding g removes exactly g from the drawn list; the Sum result stays
    assert hid == vis - 1, f"expected only g hidden, got vis={vis} hid={hid}"
    print(f"operation output independent of input visibility OK: vis={vis} hid={hid} (Sum result kept)")


if __name__ == "__main__":
    test_operation_survives_hidden_input()
    print("\nVISIBILITY TESTS PASSED")
