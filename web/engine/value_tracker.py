from .AnimObject import AnimObject


class ValueTracker(AnimObject):
    """An invisible object that just holds ONE number. It is the knob everything else reads:
    animate the tracker (ChangeValue) and any object whose updater reads it moves/recomputes in
    lockstep. Because it is an AnimObject it rides the normal timeline (copy/become/seek) - no
    special plumbing. It has no points, so the renderer draws nothing for it."""

    def __init__(self, value=0.0):
        super().__init__()
        self.value = float(value)

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = float(v)
        return self

    def increment_value(self, dv):
        self.value += float(dv)
        return self

    def become(self, other):
        super().become(other)            # points/colour/opacity (all empty here) ...
        self.value = other.value         # ... plus the number itself
        return self


def always_redraw(builder):
    """Create an object that REBUILDS itself from `builder()` every frame. Use it when the shape
    depends on live state, e.g. always_redraw(lambda: axes.plot(lambda x: f(x, k.get_value()))).
    `builder` must return the same tree structure each call (become() maps onto it)."""
    obj = builder()
    obj.add_updater(lambda m: m.become(builder()))
    return obj
