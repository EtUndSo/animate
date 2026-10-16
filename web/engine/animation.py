import numpy as np
from .rate_functions import smooth, linear
from .bezier import partial_bezier, resegment
from .AnimObject import AnimObject


class Animation:
    """Base class. An animation sets its target's state as a function of progress alpha in [0,1]."""

    appears = False      # True for animations that make their target appear (Create/FadeIn/Grow)

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

    appears = True

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

    appears = True

    def begin(self):
        super().begin()
        _set_opacity(self.target, self.start, 0.0)   # start invisible

    def interpolate(self, a):
        _set_opacity(self.target, self.start, a)


class FadeOut(Animation):
    """Fade the target out to fully transparent (reverse of FadeIn)."""

    def interpolate(self, a):
        _set_opacity(self.target, self.start, 1.0 - a)


def _path_leaves(obj, out):
    """Collect every drawable leaf (an object that owns a path) under obj, in build order."""
    if len(obj.points) >= 2:
        out.append(obj)
    for s in obj.subObjects:
        _path_leaves(s, out)


class Create(Animation):
    """Draw an object progressively, as if it were being drawn in real time.

    - single path (a line, a continuous graph, an outline): traced end-to-end via partial_bezier;
    - a SURFACE (z=f(x,y), whose faces are tagged with their anti-diagonal rank _diag): revealed as a
      growing TRIANGULAR WAVEFRONT sweeping diagonally from one corner to the full landscape;
    - any other group (e.g. a discontinuous graph split into pieces, a vector): each piece is traced
      together - so Create never silently does nothing on a grouped object.
    """

    appears = True

    def begin(self):
        super().begin()
        self._leaves = []; _path_leaves(self.target, self._leaves)
        self._start = []; _path_leaves(self.start, self._start)
        self._diag = [getattr(l, "_diag", None) for l in self._leaves]
        self._is_surface = any(d is not None for d in self._diag)
        if self._is_surface:
            ds = [d for d in self._diag if d is not None]
            self._max_diag = max(ds) if ds else 1
            self._op = [(l.fill_opacity, l.stroke_opacity) for l in self._start]
        # A 2D function graph grows from the CENTRE of the view out to both ends. The centre of the
        # x/y value ranges maps to the world origin (the axes are centred), so we anchor at the curve
        # point nearest world x=0 and trace both halves outward from there.
        self._center_out = False
        if (not self._is_surface and getattr(self.target, "_center_create", False)
                and len(self.start.points) >= 7):
            pts = self.start.points
            anchors = np.arange(0, len(pts), 3)
            ai = int(anchors[int(np.argmin(np.abs(pts[anchors, 0])))])
            if 0 < ai < len(pts) - 1:
                self._center_out = True
                self._right = pts[ai:].copy()               # anchor -> right end
                self._left_rev = pts[:ai + 1][::-1].copy()  # anchor -> left end (reversed curve)

    def interpolate(self, a):
        if self._is_surface:
            band = 0.18                                     # soft edge: bands fade in, not pop in
            span = 1.0 + band
            for leaf, d, (fo, so) in zip(self._leaves, self._diag, self._op):
                frac = (d / self._max_diag) if (self._max_diag and d is not None) else 0.0
                t = (a * span - frac) / band                # wavefront position vs this face's diagonal
                t = 0.0 if t < 0.0 else (1.0 if t > 1.0 else t)
                leaf.fill_opacity = fo * t
                leaf.stroke_opacity = so * t
        elif self._center_out:
            Ln = partial_bezier(self._left_rev, a)[::-1]    # left half, back in normal order
            Rp = partial_bezier(self._right, a)             # right half
            self.target.points = np.vstack([Ln, Rp[1:]]) if len(Rp) > 1 else Ln
        elif len(self.target.points) >= 2:
            self.target.points = partial_bezier(self.start.points, a)
        else:
            for leaf, start in zip(self._leaves, self._start):
                leaf.points = partial_bezier(start.points, a)


class ChangeValue(Animation):
    """Animate a ValueTracker from its current value to `value`. Everything whose updater reads the
    tracker then recomputes each frame - the one animation drives the whole dependent scene."""

    def __init__(self, tracker, value, **kwargs):
        super().__init__(tracker, **kwargs)
        self.end_value = float(value)

    def interpolate(self, a):
        self.target.set_value(self.start.value + (self.end_value - self.start.value) * a)


class Pulse(Animation):
    """Briefly scale the target up and back (1 -> factor -> 1 over the run time). Used e.g. to hint that
    a '+' springs out of the Σ sign. Pure function of alpha (sin bump), so it scrubs cleanly."""

    def __init__(self, target, factor=1.35, **kwargs):
        super().__init__(target, **kwargs)
        self.factor = factor

    def begin(self):
        super().begin()
        self.center = self.start.get_center()

    def interpolate(self, a):
        self.target.become(self.start)
        s = 1.0 + (self.factor - 1.0) * np.sin(np.pi * max(0.0, min(1.0, a)))
        self.target.scale(s if s > 1e-6 else 1e-6, around=self.center)


class PulseColor(Animation):
    """Briefly scale the target up and back AND tint it toward `color` and back (sin bump) - e.g. the big
    Σ grows and flashes light blue when a '+' springs out of it. Pure function of alpha (scrubs cleanly)."""

    def __init__(self, target, factor=1.4, color=(0.40, 0.70, 1.0), **kwargs):
        super().__init__(target, **kwargs)
        self.factor = factor
        self.color = np.asarray(color, dtype=float)

    def begin(self):
        super().begin()
        self.center = self.start.get_center()

    def interpolate(self, a):
        self.target.become(self.start)
        w = np.sin(np.pi * max(0.0, min(1.0, a)))
        s = 1.0 + (self.factor - 1.0) * w
        self.target.scale(s if s > 1e-6 else 1e-6, around=self.center)
        stack = [self.target]
        while stack:
            o = stack.pop()
            if len(o.points):
                base = np.asarray(o.fill_color if o.fill_color is not None else o.color, dtype=float)
                o.fill_color = tuple(base + (self.color - base) * w)
            stack.extend(o.subObjects)


class AppearPulseColor(Animation):
    """Fade the target IN (ends fully visible) while giving it ONE scale-up + colour-flash bump - e.g. a
    '+' that springs out of the sum, grows and flashes light blue, then settles to its normal size/colour.
    Combines FadeIn + PulseColor in a single contract-safe animation (pure function of alpha)."""

    appears = True

    def __init__(self, target, factor=1.4, color=(0.40, 0.70, 1.0), **kwargs):
        super().__init__(target, **kwargs)
        self.factor = factor
        self.color = np.asarray(color, dtype=float)

    def begin(self):
        super().begin()
        self.center = self.start.get_center()
        _set_opacity(self.target, self.start, 0.0)       # start invisible

    def interpolate(self, a):
        self.target.become(self.start)
        ca = max(0.0, min(1.0, a))
        _set_opacity(self.target, self.start, ca)        # fade in, ends fully visible
        w = np.sin(np.pi * ca)
        s = 1.0 + (self.factor - 1.0) * w
        self.target.scale(s if s > 1e-6 else 1e-6, around=self.center)
        stack = [self.target]
        while stack:
            o = stack.pop()
            if len(o.points):
                base = np.asarray(o.fill_color if o.fill_color is not None else o.color, dtype=float)
                o.fill_color = tuple(base + (self.color - base) * w)
            stack.extend(o.subObjects)


class Recolor(Animation):
    """Fade the target's FILL colour from its current colour to `color`."""

    def __init__(self, target, color, **kwargs):
        super().__init__(target, **kwargs)
        self.end_color = np.asarray(color, dtype=float)

    def interpolate(self, a):
        self.target.become(self.start)
        c0 = np.asarray(self.start.fill_color if self.start.fill_color is not None else self.start.color, dtype=float)
        self.target.fill_color = tuple(c0 + (self.end_color - c0) * a)


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


# ---------------------------------------------------------------------------
#  Transform (Manim-style): morph one mobject into another by INTERPOLATING their control points.
#  Both mobjects are reduced to a flat list of path leaves; the lists are padded to equal length with
#  collapsed (point-sized, transparent) stand-ins so extra pieces grow in / shrink out; each pair of
#  leaves is given the SAME number of Bézier points (resegment) so the morph is a plain point lerp.
#  Attributes (colour, fill/stroke opacity, stroke width) are interpolated too.
# ---------------------------------------------------------------------------

def _path_leaves_tf(m, out):
    if len(m.points) >= 2:
        out.append(m)
    for s in m.subObjects:
        _path_leaves_tf(s, out)


def _collapsed_like(ref):
    """A copy of ref with all its points collapsed to its centre and fully transparent - a 'nothing'
    that a real leaf can grow out of (or shrink into)."""
    c = ref.copy()
    center = ref.get_center()
    stack = [c]
    while stack:
        o = stack.pop()
        if len(o.points):
            o.points = np.tile(center, (len(o.points), 1))
        stack.extend(o.subObjects)
    c.fill_opacity = 0.0
    c.stroke_opacity = 0.0
    return c


def _as_rgb(col, fallback):
    if col is None:
        return np.asarray(fallback, dtype=float)
    return np.asarray(col, dtype=float)


class Transform(Animation):
    """Morph `mobject` into `target_mobject` (it becomes the target; the target itself is not added)."""

    appears = False

    def __init__(self, mobject, target_mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        self.target_mobject = target_mobject

    def _reset_target(self):
        self.target.points = np.zeros((0, 3))          # rebuild the target as a flat group of morphing leaves
        self.target.subObjects = []
        self._pairs = []

    def _add_pair(self, sa, ea):
        """One morphing child: start-leaf sa -> end-leaf ea (point counts aligned, attrs interpolated)."""
        ka = (len(sa.points) - 1) // 3 if len(sa.points) >= 4 else 0
        kb = (len(ea.points) - 1) // 3 if len(ea.points) >= 4 else 0
        K = max(ka, kb, 1)
        sp = resegment(sa.points, K)
        ep = resegment(ea.points, K)
        child = AnimObject()
        child.points = sp.copy()
        child.stroke_width = sa.stroke_width
        self.target.add(child)
        self._pairs.append({
            "child": child, "sp": sp, "ep": ep,
            "sc": _as_rgb(sa.color, (0, 0, 0)), "ec": _as_rgb(ea.color, (0, 0, 0)),
            "sfc": _as_rgb(sa.fill_color, sa.color or (0, 0, 0)),
            "efc": _as_rgb(ea.fill_color, ea.color or (0, 0, 0)),
            "sfo": sa.fill_opacity, "efo": ea.fill_opacity,
            "sso": sa.stroke_opacity, "eso": ea.stroke_opacity,
            "ssw": sa.stroke_width, "esw": ea.stroke_width,
        })

    def begin(self):
        self.start = self.target.copy()
        starts = []; _path_leaves_tf(self.start, starts)
        ends = []; _path_leaves_tf(self.target_mobject, ends)
        if not starts and not ends:
            self._pairs = []
            return
        n = max(len(starts), len(ends), 1)
        while len(starts) < n:                         # new pieces grow out of a transparent point
            starts.append(_collapsed_like(ends[len(starts)]))
        while len(ends) < n:                           # vanishing pieces shrink into a transparent point
            ends.append(_collapsed_like(starts[len(ends)]))
        self._reset_target()
        for sa, ea in zip(starts, ends):
            self._add_pair(sa, ea)

    def interpolate(self, a):
        for p in self._pairs:
            c = p["child"]
            c.points = p["sp"] + (p["ep"] - p["sp"]) * a
            c.color = tuple(p["sc"] + (p["ec"] - p["sc"]) * a)
            c.fill_color = tuple(p["sfc"] + (p["efc"] - p["sfc"]) * a)
            c.fill_opacity = p["sfo"] + (p["efo"] - p["sfo"]) * a
            c.stroke_opacity = p["sso"] + (p["eso"] - p["sso"]) * a
            c.stroke_width = p["ssw"] + (p["esw"] - p["ssw"]) * a


class ReplacementTransform(Transform):
    """Same morph as Transform; semantically `mobject` is REPLACED by `target_mobject` (same visual
    result here - the distinction matters for which id later animations refer to)."""
    pass


def _glyph_key(g):
    return getattr(g, "_tex", "") or ""


class TransformMatchingTex(Transform):
    """Morph one MathTex into another by MATCHING glyphs that share the same character (their `_tex`
    tag): matched glyphs move/scale into their counterpart's place, unmatched source glyphs fade out
    where they are, and new target glyphs fade in where they belong. This is what makes 'i -> value'
    and formula rearrangements read as the SAME symbols moving (Manim's TransformMatchingTex)."""

    def begin(self):
        self.start = self.target.copy()
        src = list(self.start.subObjects) or [self.start]
        tgt = list(self.target_mobject.subObjects) or [self.target_mobject]

        def leaves(g):
            out = []; _path_leaves_tf(g, out); return out

        pairs, used = [], [False] * len(tgt)
        for sg in src:
            j = next((k for k, tg in enumerate(tgt) if not used[k] and _glyph_key(tg) == _glyph_key(sg)), -1)
            if j >= 0:
                used[j] = True
                ls, lt = leaves(sg), leaves(tgt[j])
                m = max(len(ls), len(lt), 1)
                while len(ls) < m:
                    ls.append(_collapsed_like(lt[len(ls)]))
                while len(lt) < m:
                    lt.append(_collapsed_like(ls[len(lt)]))
                pairs += list(zip(ls, lt))
            else:
                pairs += [(lf, _collapsed_like(lf)) for lf in leaves(sg)]   # unmatched source -> fade out in place
        for k, tg in enumerate(tgt):
            if not used[k]:
                pairs += [(_collapsed_like(lf), lf) for lf in leaves(tg)]   # new target glyph -> fade in in place

        self._reset_target()
        for sa, ea in pairs:
            self._add_pair(sa, ea)
