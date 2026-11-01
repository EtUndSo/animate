import re
import numpy as np
from .AnimObject import AnimObject
from .constants import ORIGIN

# Number language of the current scene (ModelScene.construct sets it from model["lang"]). "" = neutral, as in
# scenes without a language: 0.5 and -1. de/es write the decimal comma, en/zh the point; every language with
# a set language gets the typographic minus.
_NUM_LANG = [""]
COMMA_LANGS = ("de", "es")


def set_number_lang(lang):
    _NUM_LANG[0] = str(lang or "")


def fmt_number(s):
    """A formatted number string in the scene's language: 0.5 -> 0,5 (de, es), -1 -> \u22121."""
    if not _NUM_LANG[0]:
        return s
    if _NUM_LANG[0] in COMMA_LANGS:
        s = s.replace(".", ",")
    return s.replace("-", "\u2212")


def localize_digits(s):
    """Decimal points between digits inside a label follow the language: "t = 0.5 s" -> "t = 0,5 s" (de, es)."""
    return re.sub(r"(?<=\d)\.(?=\d)", ",", s) if _NUM_LANG[0] in COMMA_LANGS else s


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
        return f"{self.prefix}{fmt_number(f'{v:.{self.decimals}f}')}{self.suffix}"

    def set_value(self, v):
        self.value = float(v)
        self.text = self._fmt(self.value)
        return self
