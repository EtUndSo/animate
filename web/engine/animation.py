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
    - a SURFACE (z=f(x,y), whose faces carry a radial rank _diag = distance from the domain centre):
      revealed as a HARD wavefront growing OUTWARD from the middle; each face snaps to full opacity when
      the front reaches it (no soft fade, so the backdrop never shows through as a colour->white band);
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
        if getattr(self.target, "_param_link", None) is not None:
            self.target._create_alpha = a                  # an object under a scene parameter (L3) redraws itself
            #                                                each frame and applies this progress again
        if self._is_surface:
            # HARD wavefront: a face is either FULLY shown (its own static opacity) or not yet — no
            # opacity ramp. A soft ramp left edge faces semi-transparent, so the white background showed
            # through as a colour->white gradient along the front; a clean on/off edge keeps it crisp.
            for leaf, d, (fo, so) in zip(self._leaves, self._diag, self._op):
                frac = (d / self._max_diag) if (self._max_diag and d is not None) else 0.0
                on = 1.0 if (a >= 1.0 or a > frac) else 0.0   # empty at a=0, fully covered at a=1
                leaf.fill_opacity = fo * on
                leaf.stroke_opacity = so * on
        elif self._center_out:
            Ln = partial_bezier(self._left_rev, a)[::-1]    # left half, back in normal order
            Rp = partial_bezier(self._right, a)             # right half
            self.target.points = np.vstack([Ln, Rp[1:]]) if len(Rp) > 1 else Ln
        else:
            # Every path leaf (the object's own path AND its children's) is traced from its begin()
            # snapshot. The leaf set is fixed in begin(): deciding per frame from the CURRENT point
            # count broke seek purity (at a=0 the own path shrinks to one point, so the next frame
            # took a different branch - e.g. a data curve with marker dots).
            for leaf, start in zip(self._leaves, self._start):
                leaf.points = partial_bezier(start.points, a)


class ChangeValue(Animation):
    """Animate a ValueTracker from its current value to `value`. Everything whose updater reads the
    tracker then recomputes each frame - the one animation drives the whole dependent scene."""

    def __init__(self, tracker, value, integer=False, **kwargs):
        super().__init__(tracker, **kwargs)
        self.end_value = float(value)
        self.integer = bool(integer)       # whole numbers only (n = 1, 2, 3 ...): jumps instead of gliding

    def interpolate(self, a):
        v0, v1 = self.start.value, self.end_value
        if not self.integer:
            self.target.set_value(v0 + (v1 - v0) * a)
            return
        # Every whole number from n0 to n1 is shown for the same share of the (eased) run time: n0 at a = 0,
        # n1 from a = |d|/(|d|+1) on. A plain round() would give the first and the last value half a share.
        n0, n1 = int(round(v0)), int(round(v1))
        d = n1 - n0
        k = min(abs(d), int(np.floor((abs(d) + 1) * min(max(a, 0.0), 1.0))))
        self.target.set_value(n0 + (k if d >= 0 else -k))


class CameraState(AnimObject):
    """The camera as an object of the timeline (L4, 10.11.2026): orbit angles theta/phi (radians), zoom and the
    point looked at (center). MoveCamera animates it like any target; the scene copies it onto its Camera after the
    animations of a frame ran (ModelScene.seek). It has no points, so nothing is drawn for it."""

    def __init__(self, theta=0.0, phi=0.0, zoom=1.0, center=(0.0, 0.0, 0.0)):
        super().__init__()
        self.theta, self.phi, self.zoom = float(theta), float(phi), float(zoom) or 1.0
        self.center = np.asarray(center, dtype=float).reshape(3).copy()

    def become(self, other):
        super().become(other)
        self.theta, self.phi, self.zoom, self.center = other.theta, other.phi, other.zoom, other.center.copy()
        return self

    def apply_to(self, camera):
        camera.zoom = self.zoom
        camera.set_center(self.center)
        camera.orient(self.theta, self.phi)
        return camera


class MoveCamera(Animation):
    """Move the camera (a CameraState) to new orbit angles, zoom and/or look-at point over the run time (Manim:
    move_camera). Values left out stay. `turn` adds an angle to theta (a full turn = 2*pi: ambient rotation; use
    rate_func=linear for an even spin). Angles interpolate as numbers (no wrapping: the end value is reached
    exactly as given), the zoom geometrically (an even feel when magnifying), the center linearly."""

    def __init__(self, state, theta=None, phi=None, zoom=None, center=None, turn=0.0, **kwargs):
        super().__init__(state, **kwargs)
        self.theta = None if theta is None else float(theta)
        self.phi = None if phi is None else float(phi)
        self.zoom = None if zoom is None else max(1e-6, float(zoom))
        self.center = None if center is None else np.asarray(list(center) + [0.0] * (3 - len(center)), dtype=float)[:3]
        self.turn = float(turn or 0.0)

    def interpolate(self, a):
        s, t = self.start, self.target
        th1 = (s.theta if self.theta is None else self.theta) + self.turn
        ph1 = s.phi if self.phi is None else self.phi
        t.theta = s.theta + (th1 - s.theta) * a
        t.phi = s.phi + (ph1 - s.phi) * a
        t.zoom = s.zoom if self.zoom is None else s.zoom * (self.zoom / s.zoom) ** a
        t.center = s.center.copy() if self.center is None else s.center + (self.center - s.center) * a


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
                if getattr(o, "text", None) is not None:  # a label is drawn in `color`: tint that (Indicate on Text)
                    o.color = o.fill_color
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


class Rotate(Animation):
    """Rotate the target by `angle` radians about its centre (or `around`) over the run time."""

    def __init__(self, target, angle=np.pi / 2, around=None, **kwargs):
        super().__init__(target, **kwargs)
        self.angle = float(angle)
        self.around = around

    def begin(self):
        super().begin()
        self.center = self.around if self.around is not None else self.start.get_center()

    def interpolate(self, a):
        self.target.become(self.start)
        self.target.rotate(self.angle * a, around=self.center)


class Scale(Animation):
    """Scale the target to `factor`x its size about its centre (or `around`) over the run time."""

    def __init__(self, target, factor=2.0, around=None, **kwargs):
        super().__init__(target, **kwargs)
        self.factor = float(factor)
        self.around = around

    def begin(self):
        super().begin()
        self.center = self.around if self.around is not None else self.start.get_center()

    def interpolate(self, a):
        self.target.become(self.start)
        s = 1.0 + (self.factor - 1.0) * a
        self.target.scale(s if abs(s) > 1e-6 else 1e-6, around=self.center)


class MoveTo(Animation):
    """Move the target so its centre ends at world point `point`."""

    def __init__(self, target, point, **kwargs):
        super().__init__(target, **kwargs)
        self.point = np.asarray(point, dtype=float)

    def begin(self):
        super().begin()
        self.center = self.start.get_center()

    def interpolate(self, a):
        self.target.become(self.start)
        self.target.shift((self.point - self.center) * a)


class MoveAlongPath(Animation):
    """Move the target's centre along `path` (any object whose points trace the path, or an (N,3) array)."""

    def __init__(self, target, path, **kwargs):
        super().__init__(target, **kwargs)
        self._path = path

    def begin(self):
        super().begin()
        self.center = self.start.get_center()
        pts = self._path.all_points() if hasattr(self._path, "all_points") else np.asarray(self._path, dtype=float)
        self.pts = pts.reshape(-1, 3) if len(pts) else np.zeros((1, 3))

    def interpolate(self, a):
        self.target.become(self.start)
        n = len(self.pts)
        if n == 0:
            return
        f = max(0.0, min(1.0, a)) * (n - 1)
        i = int(np.floor(f)); t = f - i
        p = self.pts[i] if i >= n - 1 else self.pts[i] * (1 - t) + self.pts[i + 1] * t
        self.target.shift(p - self.center)


class Indicate(PulseColor):
    """Briefly enlarge + tint the target to draw attention, then return to normal (amber by default)."""

    def __init__(self, target, color=(1.0, 0.78, 0.25), factor=1.25, **kwargs):
        super().__init__(target, factor=factor, color=color, **kwargs)


def text_rows(obj, gap=1e-3):
    """The children of a formula (glyph groups of a MathTex) grouped into display rows, top to bottom: children whose
    vertical extents overlap belong to one row (a fraction or a Σ with limits stays in its row; rows of an `aligned`
    block are separated by their row spacing). Returns a list of lists of children."""
    spans = []
    for g in obj.subObjects:
        p = g.all_points()
        if len(p):
            spans.append((float(p[:, 1].max()), float(p[:, 1].min()), g))
    spans.sort(key=lambda s: -s[0])
    rows, lo = [], None
    for top, bot, g in spans:
        if rows and top >= lo - gap:                    # overlaps the current row (y up: rows go downwards)
            rows[-1].append(g)
            lo = min(lo, bot)
        else:
            rows.append([g])
            lo = bot
    return rows


class FadeInLines(Animation):
    """A formula appears row by row (FadeIn with lines=true): the rows of text_rows() fade in one after another within
    the run time, each over its own share. Pure function of alpha; `marks` = the relative start of each row."""

    appears = True

    def __init__(self, target, **kwargs):
        kwargs.setdefault("rate_func", linear)
        super().__init__(target, **kwargs)

    def begin(self):
        super().begin()
        self.rows = [[self.target.subObjects.index(g) for g in row] for row in text_rows(self.target)]
        n = max(1, len(self.rows))
        self.marks = [i / float(n) for i in range(n)]
        _set_opacity(self.target, self.start, 0.0)

    def interpolate(self, a):
        n = max(1, len(self.rows))
        for i, row in enumerate(self.rows):
            w = smooth(max(0.0, min(1.0, a * n - i)))
            for j in row:
                _set_opacity(self.target.subObjects[j], self.start.subObjects[j], w)


class IndicateCells(Animation):
    """Light up single cells of a Table (L9): their highlight boxes (added at build time, transparent) fade to
    `opacity` and back (sin bump). Pure function of alpha; the table itself is not touched."""

    def __init__(self, target, boxes, opacity=0.55, **kwargs):
        super().__init__(target, **kwargs)
        self.boxes = list(boxes)
        self.opacity = float(opacity)

    def begin(self):
        self.start = None                              # no snapshot: the boxes are set absolutely

    def interpolate(self, a):
        w = float(np.sin(np.pi * max(0.0, min(1.0, a))))
        for b in self.boxes:
            b.fill_opacity = self.opacity * w


class Write(Create):
    """Write the target on (progressive stroke/glyph reveal) - Create, framed as 'Write' for text/formulas."""
    pass


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


def _copy_opacity(o, s):
    o.fill_opacity, o.stroke_opacity = s.fill_opacity, s.stroke_opacity
    for a, b in zip(o.subObjects, s.subObjects):
        _copy_opacity(a, b)


def _zero_opacity(o):
    o.fill_opacity = o.stroke_opacity = 0.0
    for a in o.subObjects:
        _zero_opacity(a)


def _as_rgb(col, fallback):
    if col is None:
        return np.asarray(fallback, dtype=float)
    return np.asarray(col, dtype=float)


def _is_text(o):
    """A Text label (one anchor point, drawn by the painter's draw_text, no children)."""
    return getattr(o, "text", None) is not None and not o.subObjects


class Transform(Animation):
    """Morph `mobject` into `target_mobject` (it becomes the target; the target itself is not added).
    Text -> Text: a label has no path to morph, so the label changes its CONTENT: anchor, size and colour move to the
    template's, the old text fades out in the first half and the new text (with the template's align, font, raw) fades
    in in the second half. At the end the label IS the template's text: one object, nothing invisible left behind."""

    appears = False

    def __init__(self, mobject, target_mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        self.target_mobject = target_mobject

    def _text_morph(self):
        """Begin a Text -> Text morph (called from begin when both are labels)."""
        self.start = self.target.copy()
        self._text = True

    def _interp_text(self, a):
        s, e, t = self.start, self.target_mobject, self.target
        t.points = s.points + (e.points - s.points) * a
        t.font_size = s.font_size + (e.font_size - s.font_size) * a
        t.color = tuple(_as_rgb(s.color, (0, 0, 0)) + (_as_rgb(e.color, (0, 0, 0)) - _as_rgb(s.color, (0, 0, 0))) * a)
        src, k = (s, 1.0 - 2.0 * a) if a < 0.5 else (e, 2.0 * a - 1.0)
        t.text, t.align = src.text, getattr(src, "align", "center")
        t.font, t.raw = getattr(src, "font", "sans"), getattr(src, "raw", False)
        t.spans = getattr(src, "spans", None)            # coloured sections (F1) come with the text
        t.fill_opacity = src.fill_opacity * k
        t.stroke_opacity = src.stroke_opacity * k

    def _reset_target(self):
        # Rebuild the target as a flat group of morphing leaves. The ORIGINAL geometry (own points, children) stays in
        # the object: until the morph starts (alpha = 0) it is what is drawn, so animations before the morph (Create,
        # FadeIn, Write on the same object) still act on it; once the morph runs, only the morphing leaves are drawn.
        self._orig_points = self.target.points.copy()
        self._orig = list(self.target.subObjects)
        self.target.points = np.zeros((0, 3))
        self.target.subObjects = list(self._orig)
        self._pairs = []

    def _show_original(self, on):
        if on:
            self.target.points = self._orig_points.copy()
            for o, s in zip(self._orig, self.start.subObjects):
                _copy_opacity(o, s)
        else:
            self.target.points = np.zeros((0, 3))
            for o in self._orig:
                _zero_opacity(o)

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
        if _is_text(self.target) and _is_text(self.target_mobject):
            return self._text_morph()
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
        if getattr(self, "_text", False):              # Text -> Text: the content changes
            return self._interp_text(a)
        if not hasattr(self, "_orig"):                 # nothing to morph (no paths on either side)
            return
        if a <= 0.0:                                   # not started: the object as it was, morph leaves hidden
            self._show_original(True)
            for p in self._pairs:
                c = p["child"]
                c.points = p["sp"].copy()
                c.fill_opacity = 0.0
                c.stroke_opacity = 0.0
            return
        self._show_original(False)
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
        if _is_text(self.target) and _is_text(self.target_mobject):
            return self._text_morph()                  # two labels: the content changes (Transform)
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
