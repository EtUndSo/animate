import numpy as np
from .AnimObject import AnimObject
from .constants import ORIGIN


class Text(AnimObject):
    """A text label. Cairo draws it directly (via show_text), so a Text is NOT made of
    Bézier points. Its position is stored as the single 'point', so shift/scale/rotate move
    the label exactly like any other object.
    """
    def __init__(self, text, position=ORIGIN, font_size=28, color=(0.0, 0.0, 0.0), align="center"):
        super().__init__()
        self.text = text                                           # may be rich: U_{GS}, 10^{-3}, \alpha (richtext.py)
        self.font_size = font_size                                 # in pixels
        self.color = color
        self.align = align                                         # "center" | "left" | "right" (relative to the anchor)
        self.points = np.array([np.asarray(position, dtype=float)])  # (1,3): the anchor


class DecimalNumber(Text):
    """A Text that displays a NUMBER and can be updated live. Drive it from a ValueTracker with
    an updater, e.g.  num.add_updater(lambda d: d.set_value(k.get_value())) , so the shown value
    tracks the animation frame by frame. This is how computed results appear on screen (3B1B-style)."""

    def __init__(self, value=0.0, position=ORIGIN, font_size=40, color=(0.0, 0.0, 0.0),
                 decimals=2, prefix="", suffix=""):
        self.value = float(value)
        self.decimals = decimals
        self.prefix = prefix
        self.suffix = suffix
        super().__init__(self._fmt(value), position, font_size=font_size, color=color)

    def _fmt(self, v):
        return f"{self.prefix}{v:.{self.decimals}f}{self.suffix}"

    def set_value(self, v):
        self.value = float(v)
        self.text = self._fmt(self.value)
        return self
