import numpy as np
from .AnimObject import AnimObject
from .simpleShape import Line
from .text import Text
from .constants import ORIGIN

# A general-purpose legend / key for ANY set of curves or objects — not tied to one scene.
# Entries are a ';'-separated `labels` string; `colors` is an optional ';'-separated list of hex
# colours (WITHOUT a leading '#', e.g. "59a0eb;ea5959"), falling back to an automatic palette so the
# common case is just typing the labels. One row per entry = a coloured swatch line + a text label.
# Only the ANCHOR (`position`) is a data coordinate. Row gap, swatch length and gap are SCENE (world) units,
# like a Dot's radius: the interpreter maps the anchor through the Axes and shifts the finished key there
# (scene_model._ANCHORED_TYPES) instead of scaling it with the data (axes.place). Otherwise the spacing
# changed with every axes (0.8 became 1.33 on y_length 4 over a span of 2.4) and the key was unusable on
# log or unevenly scaled axes. This is how matplotlib does it too: legend spacing is in font/screen units.

_PALETTE = [                                   # default auto-colours (RGB 0..1), used when `colors` is empty
    (0.35, 0.63, 0.92), (0.92, 0.35, 0.35), (0.17, 0.71, 0.45),
    (0.95, 0.60, 0.15), (0.61, 0.35, 0.80), (0.20, 0.70, 0.75),
    (0.85, 0.45, 0.60), (0.55, 0.55, 0.20),
]


def _hex_to_rgb(h):
    """'59a0eb' / '#59a0eb' / 'abc' -> (r,g,b) in 0..1, or None if unparseable."""
    h = str(h).strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        n = int(h, 16)
    except ValueError:
        return None
    return (((n >> 16) & 255) / 255.0, ((n >> 8) & 255) / 255.0, (n & 255) / 255.0)


class Legend(AnimObject):
    """Key/legend: one row per entry (colour swatch + label). See module docstring for the format.

    labels      ';'-separated entry labels, e.g. "sin;cos;tan".
    colors      optional ';'-separated hex colours (no '#'); empty -> automatic palette.
    position    anchor = left end of the first swatch, in DATA coordinates (the Axes maps it on screen).
    font_size   label size in pixels (axis-independent, stays readable at any range).
    row_gap     vertical spacing between rows (scene units; 1 unit = 135 px of the 1920x1080 frame).
    swatch_len  length of the colour swatch line (scene units).
    gap         space between swatch and the start of the label (scene units); labels are left-aligned.
    color       label text colour. stroke_width = swatch line thickness (px).
    Defaults at 26 px text: row pitch 0.35 = 1.8 em, swatch 0.4 = 2.1 em, gap 0.15 = 0.8 em (matplotlib:
    labelspacing 0.5 em plus the text height, handlelength 2 em, handletextpad 0.8 em).
    """

    def __init__(self, labels="f(x);g(x)", colors="", position=ORIGIN, font_size=26,
                 row_gap=0.35, swatch_len=0.4, gap=0.15, color=(0.0, 0.0, 0.0), stroke_width=6.0):
        super().__init__()
        self.color = color
        p0 = np.asarray(position, dtype=float).reshape(-1)
        x0, y0 = float(p0[0]), float(p0[1])
        items = [s.strip() for s in str(labels).split(";") if s.strip() != ""]
        cols_raw = [c.strip() for c in str(colors).split(";")] if str(colors).strip() else []
        for i, text in enumerate(items):
            y = y0 - i * float(row_gap)
            rgb = _hex_to_rgb(cols_raw[i]) if i < len(cols_raw) and cols_raw[i] else None
            if rgb is None:
                rgb = _PALETTE[i % len(_PALETTE)]
            sw = Line([x0, y, 0.0], [x0 + float(swatch_len), y, 0.0])
            sw.color = rgb
            sw.stroke_width = float(stroke_width)
            lab = Text(text, position=[x0 + float(swatch_len) + float(gap), y, 0.0],   # starts `gap` after the swatch
                       font_size=float(font_size), color=color, align="left")
            self.add(sw, lab)
