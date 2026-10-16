import sys, numpy as np
sys.path.insert(0, ".")   # run from web/
from engine.scene import Scene
from engine.axes import Axes
from engine.simpleShape import Dot
from engine.text import DecimalNumber
from engine.value_tracker import ValueTracker, always_redraw
from engine.animation import ChangeValue
from engine.rate_functions import smooth


class Motor(Scene):
    def construct(self):
        ax = Axes(x_range=(-6, 6), y_range=(-2, 2), x_length=12, y_length=5)
        k = ValueTracker(0.0)
        self.add(ax, k)
        # Dot follows (k, sin k) ; number shows k ; graph is sin(x + k) — all driven by the ONE tracker.
        self.k, self.ax = k, ax
        self.dot = always_redraw(lambda: Dot(ax.coords_to_point(k.get_value(), np.sin(k.get_value())), radius=0.1))
        self.num = DecimalNumber(0.0, position=[0, 2.5, 0], decimals=2)
        self.num.add_updater(lambda d: d.set_value(k.get_value()))
        self.graph = always_redraw(lambda: ax.plot(lambda x: np.sin(x + k.get_value())))
        self.add(self.graph, self.dot, self.num)
        self.play(ChangeValue(k, 6.0), run_time=2.0)


s = Motor().build_timeline()
print("duration", s.duration)

for t in (0.0, 1.0, 2.0):
    s.seek(t)
    kv = s.k.get_value()
    expect_k = 0 + 6.0 * smooth(min(t / 2.0, 1.0))
    assert abs(kv - expect_k) < 1e-9, (t, kv, expect_k)
    # number text tracks k
    assert s.num.text == f"{kv:.2f}", (s.num.text, kv)
    # dot sits at coords_to_point(k, sin k)
    dot_center = (s.dot.points.min(axis=0) + s.dot.points.max(axis=0)) / 2.0
    expect = s.ax.coords_to_point(kv, np.sin(kv))
    assert np.allclose(dot_center, expect, atol=1e-9), (dot_center, expect)
    print(f"t={t}: k={kv:.4f}  number='{s.num.text}'  dot@({dot_center[0]:.3f},{dot_center[1]:.3f}) OK")

# graph must actually change shape between t=0 and t=2
s.seek(0.0); g0 = s.graph.points.copy()
s.seek(2.0); g2 = s.graph.points.copy()
# adaptive sampling may yield a different number of points per frame -> different shape = reacted
reacted = (g0.shape != g2.shape) or (not np.allclose(g0, g2))
assert reacted, "graph did not react to the tracker"
print("graph reacts to tracker OK (shapes %s vs %s)" % (g0.shape, g2.shape))

# number at the very end
s.seek(s.duration)
assert s.num.text == "6.00", s.num.text
print("end value OK:", s.num.text)
print("\nMOTOR TESTS PASSED")
