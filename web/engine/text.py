import numpy as np
from .AnimObject import AnimObject
from .constants import ORIGIN


class Text(AnimObject):
    """A text label. Cairo draws it directly (via show_text), so a Text is NOT made of
    Bézier points. Its position is stored as the single 'point', so shift/scale/rotate move
    the label exactly like any other object.
    """
    def __init__(self, text, position=ORIGIN, font_size=28, color=(0.0, 0.0, 0.0)):
        super().__init__()
        self.text = text
        self.font_size = font_size                                 # in pixels
        self.color = color
        self.points = np.array([np.asarray(position, dtype=float)])  # (1,3): the anchor
