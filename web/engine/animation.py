import numpy as np
from .rate_functions import smooth, linear
from .bezier import partial_bezier


class Animation:
    """Base class. An animation sets its target's state as a function of progress alpha in [0,1]."""

    def __init__(self, target, run_time=1.0, rate_func=smooth):
        self.target = target
        self.run_time = run_time
        self.rate_func = rate_func
        self.start = None

    def begin(self):
        """Called once before the first frame: snapshot the start state."""
        self.start = self.target.copy()

    def update(self, alpha):
        """alpha is raw linear progress in [0,1]; ease it, then set the state."""
        self.interpolate(self.rate_func(alpha))

    def interpolate(self, a):
        """Set the target's state for eased progress a in [0,1]. Override in subclasses."""
        raise NotImplementedError


class Shift(Animation):
    """Move the target by 'vector' over the run time."""

    def __init__(self, target, vector, **kwargs):
        super().__init__(target, **kwargs)
        self.vector = np.asarray(vector, dtype=float)

    def interpolate(self, a):
        self.target.become(self.start)          # reset to the start state ...
        self.target.shift(self.vector * a)      # ... then move a fraction of the way


class GrowFromCenter(Animation):
    """Grow the target from a point at its center to full size."""

    def begin(self):
        super().begin()
        self.center = self.start.get_center()

    def interpolate(self, a):
        self.target.become(self.start)
        self.target.scale(max(a, 1e-6), around=self.center)   # a=0 -> point, a=1 -> full size


def _set_opacity(target, start, a):
    """Scale fill/stroke opacity of target (and all children) by a, relative to start."""
    target.fill_opacity = start.fill_opacity * a
    target.stroke_opacity = start.stroke_opacity * a
    for t, s in zip(target.subObjects, start.subObjects):
        _set_opacity(t, s, a)


class FadeIn(Animation):
    """Fade the target in from fully transparent to its normal opacity."""

    def begin(self):
        super().begin()
        _set_opacity(self.target, self.start, 0.0)   # start invisible

    def interpolate(self, a):
        _set_opacity(self.target, self.start, a)


class Create(Animation):
    """Draw a curve (graph, line, outline) progressively from its start point to its end -
    as if it were being drawn in real time. Works on single-path objects (not groups)."""

    def interpolate(self, a):
        self.target.points = partial_bezier(self.start.points, a)


class Refine(Animation):
    """General '1 -> n' refinement: steps a count from 1 up to n and rebuilds the target's
    children each step via build_func(count). The SAME mechanism serves Riemann rectangles,
    Fourier partial sums, histogram bins, ... - each just supplies its own build_func(count)."""

    def __init__(self, target, build_func, n, rate_func=linear, **kwargs):
        super().__init__(target, rate_func=rate_func, **kwargs)
        self.build_func = build_func
        self.n = n
        self._last_count = None

    def begin(self):
        self._last_count = None                        # no snapshot needed; we rebuild each step

    def interpolate(self, a):
        count = max(1, min(self.n, int(round(1 + a * (self.n - 1)))))
        if count != self._last_count:                  # only rebuild when the count actually changes
            self.target.subObjects = self.build_func(count).subObjects
            self._last_count = count
