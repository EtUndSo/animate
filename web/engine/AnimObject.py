import copy as _copy
import numpy as np
from .constants import ORIGIN, TOWARDS


def rotation_matrix(angle, axis):
    """3x3 rotation matrix (Rodrigues' formula) around an arbitrary axis.
    For 2D the axis is TOWARDS (out of the screen); this rotates within the x-y plane."""
    axis = np.asarray(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis
    c, s = np.cos(angle), np.sin(angle)
    C = 1.0 - c
    return np.array([
        [c + x * x * C,     x * y * C - z * s, x * z * C + y * s],
        [y * x * C + z * s, c + y * y * C,     y * z * C - x * s],
        [z * x * C - y * s, z * y * C + x * s, c + z * z * C],
    ])


class Mobject:
    """Base animatable object - Manim's Mobject/VMobject (same design: geometry is a cubic Bézier
    control-point array, children in `subObjects`, direct point transforms). `VMobject` and the legacy
    `AnimObject` are aliases of this class so Manim-style code and older code both work."""

    def __init__(self):
        self.points = np.zeros((0, 3))           # cubic Bézier control points, shape (N,3), N = 3k+1
        self.subObjects: list["Mobject"] = []    # child objects (a group is a Mobject with children)
        self.updaters = []                       # functions fn(self) re-run each frame (see run_updaters)
        self.color = (0.0, 0.0, 0.0)             # outline / stroke colour
        self.stroke_width = 4.0                  # pen thickness (pixels)
        self.fill_color = None                   # fill colour; None -> same as the outline colour
        self.fill_opacity = 0.0
        self.stroke_opacity = 1.0                # outline opacity (used by FadeIn)
        self.show_center = False                 # draw a small dot at the centre (positioning aid)
        self.dash = None                         # stroke dash pattern in pixels, e.g. [8, 6]; None = solid

    # ---------- structure ----------
    def add(self, *objects):
        """Add child objects. A composite object (group, axes, ...) is an AnimObject
        whose geometry lives in its children."""
        self.subObjects.extend(objects)
        return self

    # ---------- updaters ----------
    # An updater is a function fn(obj) re-run every frame, AFTER the timeline has set the frame's
    # state. It lets an object recompute itself from the current scene (e.g. a graph that follows a
    # ValueTracker, or a DecimalNumber that shows its value). This is the core of "object interaction":
    # the drawn result is computed each frame from the maths, not stored statically.
    def add_updater(self, fn):
        self.updaters.append(fn)
        return self

    def clear_updaters(self):
        self.updaters = []
        return self

    def run_updaters(self):
        """Run own updaters, then children's (so a group updates before its parts rely on it)."""
        for fn in self.updaters:
            fn(self)
        for sub in self.subObjects:
            sub.run_updaters()
        return self

    # ---------- queries ----------
    def all_points(self):
        """Own points plus all descendants' points, stacked (for center / bounding box)."""
        parts = [self.points] if len(self.points) else []
        for sub in self.subObjects:
            p = sub.all_points()
            if len(p):
                parts.append(p)
        return np.vstack(parts) if parts else np.zeros((0, 3))

    def get_bounding_box(self):
        """(min_corner, max_corner) over all points of this object and its children."""
        pts = self.all_points()
        if len(pts) == 0:
            return ORIGIN.copy(), ORIGIN.copy()
        return pts.min(axis=0), pts.max(axis=0)

    def get_center(self):
        pts = self.all_points()
        if len(pts) == 0:
            return ORIGIN.copy()
        return (pts.min(axis=0) + pts.max(axis=0)) / 2.0     # center of the bounding box

    # ---------- affine transforms ----------
    # All transforms act DIRECTLY on the Bézier control points. Because every point on a
    # Bézier curve is an affine combination of its control points (weights sum to 1),
    # transforming the control points transforms the whole curve exactly - no re-sampling.
    def shift(self, vec):
        vec = np.asarray(vec, dtype=float)
        self.points = self.points + vec
        for sub in self.subObjects:
            sub.shift(vec)
        return self                              # allows chaining

    def scale(self, scaling_factor, around=None):
        if around is None:
            around = self.get_center()           # computed once; same pivot for the whole group
        around = np.asarray(around, dtype=float)
        self.points = (self.points - around) * scaling_factor + around
        for sub in self.subObjects:
            sub.scale(scaling_factor, around)
        return self

    def rotate(self, angle, axis=TOWARDS, around=None):
        if around is None:
            around = self.get_center()
        around = np.asarray(around, dtype=float)
        R = rotation_matrix(angle, axis)
        self.points = (self.points - around) @ R.T + around
        for sub in self.subObjects:
            sub.rotate(angle, axis, around)
        return self

    def move_to(self, point):
        point = np.asarray(point, dtype=float)
        return self.shift(point - self.get_center())

    def set_dash(self, dash):
        """Set the stroke dash pattern on this object and every descendant that may be dashed
        (leaves flagged `_no_dash`, e.g. arrowheads and dots, keep a solid outline)."""
        if not getattr(self, "_no_dash", False):
            self.dash = dash
        for sub in self.subObjects:
            sub.set_dash(dash)
        return self

    # ---------- animation support ----------
    def copy(self):
        """A full, independent deep copy (used to snapshot the start state of an animation)."""
        return _copy.deepcopy(self)

    def become(self, other):
        """Copy other's drawable state into self. Assumes the same tree structure (as produced
        by copy()). Used each frame to reset to the start before applying progress."""
        self.points = other.points.copy()
        self.color = other.color
        self.stroke_width = other.stroke_width
        self.fill_color = other.fill_color
        self.fill_opacity = other.fill_opacity
        self.stroke_opacity = other.stroke_opacity
        self.show_center = other.show_center
        self.dash = other.dash
        for mine, theirs in zip(self.subObjects, other.subObjects):
            mine.become(theirs)
        return self


# Manim-compatible names. Our object IS a vectorized (Bézier) mobject, so VMobject is the precise
# name; Mobject is the base name Manim users reach for; AnimObject stays for existing code.
VMobject = Mobject
AnimObject = Mobject
