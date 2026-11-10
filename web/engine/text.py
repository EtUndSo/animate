import re
import numpy as np
from .AnimObject import AnimObject
from .constants import ORIGIN

# Number language of the current scene (ModelScene.construct sets it from model["lang"]). "" = neutral, as in
# scenes without a language: 0.5 and -1. de/es/fr/tr write the decimal comma, en/zh the point; every language
# with a set language gets the typographic minus.
_NUM_LANG = [""]
COMMA_LANGS = ("de", "es", "fr", "tr")


def set_number_lang(lang):
    _NUM_LANG[0] = str(lang or "")


def fmt_number(s):
    """A formatted number string in the scene's language: 0.5 -> 0,5 (de, es, fr, tr), -1 -> \u22121."""
    if not _NUM_LANG[0]:
        return s
    if _NUM_LANG[0] in COMMA_LANGS:
        s = s.replace(".", ",")
    return s.replace("-", "\u2212")


def localize_digits(s):
    """Decimal points between digits inside a label follow the language: "t = 0.5 s" -> "t = 0,5 s" (de, es, fr, tr).
    Only numbers with ONE point: chains such as an IP address (10.0.2.15) or a version (1.2.3) stay as written."""
    if _NUM_LANG[0] not in COMMA_LANGS:
        return s
    return re.sub(r"(?<![\d.])(\d+)\.(\d+)(?!\d)(?!\.\d)", r"\1,\2", s)


FONTS = ("sans", "mono")                                           # Text.font: normal labels / typewriter (terminal, code)


class Text(AnimObject):
    """A text label. Cairo draws it directly (via show_text), so a Text is NOT made of
    Bézier points. Its position is stored as the single 'point', so shift/scale/rotate move
    the label exactly like any other object.
    font: "sans" (default, Arial-compatible) or "mono" (typewriter font on a fixed grid of cells, richtext.MONO_CELL).
    raw:  True = the text is taken literally (no rich syntax: _ ^ \\ $ { } are ordinary characters, richtext.text_lines).
    """
    def __init__(self, text, position=ORIGIN, font_size=28, color=(0.0, 0.0, 0.0), align="center", font="sans", raw=False):
        super().__init__()
        self.text = text                                           # may be rich: U_{GS}, 10^{-3}, \alpha (richtext.py)
        self.font_size = font_size                                 # in pixels
        self.color = color
        self.align = align                                         # "center" | "left" | "right" (relative to the anchor)
        self.font = font if font in FONTS else "sans"
        self.raw = bool(raw)
        self.points = np.array([np.asarray(position, dtype=float)])  # (1,3): the anchor


def text_style(obj):
    """The painter keywords of a Text beyond the classic seven arguments: {} for an ordinary label (so painters written
    before font/raw existed keep working), else {"font": "mono"} and/or {"raw": True}."""
    st = {}
    if getattr(obj, "font", "sans") == "mono":
        st["font"] = "mono"
    if getattr(obj, "raw", False):
        st["raw"] = True
    return st


class DecimalNumber(Text):
    """A Text that displays a NUMBER and can be updated live. Drive it from a ValueTracker with
    an updater, e.g.  num.add_updater(lambda d: d.set_value(k.get_value())) , so the shown value
    tracks the animation frame by frame. This is how computed results appear on screen (3B1B-style)."""

    def __init__(self, value=0.0, position=ORIGIN, font_size=40, color=(0.0, 0.0, 0.0),
                 decimals=2, prefix="", suffix="", align="center"):
        self.value = float(value)
        self.decimals = max(0, int(decimals))
        self.prefix = prefix
        self.suffix = suffix
        super().__init__(self._fmt(value), position, font_size=font_size, color=color, align=align)

    def _fmt(self, v):
        if not np.isfinite(v):                              # sqrt(t - 1) before t = 1: a dash, not "nan"
            return f"{self.prefix}–{self.suffix}"
        s = f'{v:.{self.decimals}f}'
        if s.startswith("-") and not s.strip("-0."):        # -0.001 shown with 2 decimals is 0.00, not −0.00
            s = s[1:]
        return f"{self.prefix}{fmt_number(s)}{self.suffix}"

    def set_value(self, v):
        self.value = float(v)
        self.text = self._fmt(self.value)
        return self
