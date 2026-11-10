"""Article-figure export (package P1 in ABBILDUNGEN_INVENTAR.md): from a scene to an SVG for the article column.

Convention (the same as matplotlib's savefig(bbox_inches="tight", pad_inches=...), Inkscape's "export
drawing" and GeoGebra's "export graphics view / selected area"):

  mode "content" (default)  crop to the bounding box of everything that is DRAWN (paths with half their
                            stroke, text with its estimated extent) plus `margin` scene pixels on every
                            side, limited to the visible 1920x1080 frame (what the editor shows);
  mode "frame"              crop to a rectangle stored in the scene: `frame` = [x0, y0, x1, y1] in world units
                            of the 2D view (x right, y up; the default frame spans x = -7.11..7.11,
                            y = -4..4), like Inkscape's custom area or GeoGebra's export corners;
  mode "canvas"             the whole 1920x1080 frame (the previous, uncropped export).

Size: the SVG keeps the scene's pixel geometry in its viewBox and is DISPLAYED at crop size x `scale`.
The default scale 0.55 maps the editor's ordinary label sizes 24/26/28 px to 13.2/14.3/15.4 px, so the
scene's normal text renders at 13-15 px in the article. That holds while the figure is not wider than the
column; a wider one is shrunk by the browser (max-width: 100 %) and its text with it, which `info` reports
(text_px). Text sizes are fixed in pixels, so the way to fit the column is to make the drawing narrower
(e.g. shorter x_length), exactly as with a fixed font size and width=\\linewidth in pgfplots.

The article column was measured in Chrome on the built pages: the article is 72ch = 616 px wide, a section
card has 22 px padding + 1 px border on each side (570 px inside), the :::abbildung box 10 px padding +
1 px border (548 px for the image). Phones are narrower (about 330 px), there every figure shrinks.
"""
import math

import numpy as np

from .renderer import paint_scene
from .richtext import (parse as _parse_rich, layout as _layout, plain as _plain, text_lines as _text_lines,
                       mono_line as _mono_line, MONO_CELL)
from .svg_painter import SvgPainter, SVG_FONT

SCALE = 0.55              # scene px -> article px (24-28 px labels -> 13.2-15.4 px)
MARGIN = 24               # scene px around the content box (= 13 article px at SCALE)
COLUMN_PX = 548           # widest image in an :::abbildung box on desktop (see module docstring)
REF_TEXT_PX = 26          # "normal" label size of the editor catalogue (Legend, Component, Band: 26; ticks 24; arrows 28)
MODES = ("content", "frame", "canvas")
# The editor paints its canvas grey (#d4d7dc) in night mode and stores that as the background while it is
# still the theme default (editor.js THEME_BG). An article figure is never grey: it becomes white.
_THEME_GREY = (212 / 255.0, 215 / 255.0, 220 / 255.0)

# Advance widths in 1/1000 em of Helvetica = Arial = Liberation Sans (Adobe core-font AFM metrics), ASCII
# 32..126, plus German letters. Everything else is estimated at 600 (Greek, symbols), CJK at 1000.
_W = dict(zip(
    " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
    [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
     556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556, 1015,
     667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667, 611,
     722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556, 333,
     556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278,
     556, 500, 722, 500, 500, 500, 334, 260, 334, 584]))
_W.update({"ä": 556, "ö": 556, "ü": 556, "Ä": 667, "Ö": 778, "Ü": 722, "ß": 611, "°": 400, "·": 278,
           "×": 584, "±": 584, "−": 584, "µ": 556, "…": 1000, "→": 1000, "≈": 584, "≤": 584, "≥": 584})
# French and Turkish letters (same AFM). é and ê are left out on purpose: older figures already contain them and keep
# the estimate 600 (a little wider than 556), so their crop stays exactly as it was. Arial has all these glyphs.
_W.update({"à": 556, "â": 556, "æ": 889, "ç": 500, "è": 556, "ë": 556, "î": 278, "ï": 278, "ô": 556, "ù": 556,
           "û": 556, "ÿ": 500, "œ": 944, "À": 667, "Â": 667, "Æ": 1000, "Ç": 722, "È": 667, "É": 667, "Ê": 667,
           "Ë": 667, "Î": 278, "Ï": 278, "Ô": 778, "Ù": 722, "Û": 722, "Ÿ": 667, "Œ": 1000, "«": 556, "»": 556,
           "‹": 333, "›": 333, "’": 222, " ": 278,
           "ğ": 556, "Ğ": 778, "ş": 500, "Ş": 667, "ı": 278, "İ": 278})
_ASCENT = 0.56            # glyph extent above/below the "central" baseline in em (Arial: ascent 0.905,
#                           descent 0.212, central = their middle -> +-0.5585 em)
_LINE_H = 1.25            # line pitch of multi-line labels (svg_painter._LINE_H)


def char_em(ch):
    """Advance width of one character in em."""
    if ch in _W:
        return _W[ch] / 1000.0
    o = ord(ch)
    if 0x2E80 <= o <= 0x9FFF or 0xAC00 <= o <= 0xD7AF or 0xFF00 <= o <= 0xFFEF:
        return 1.0                                               # CJK and full-width forms
    return 0.6


def _lines_box(text, px, py, font_size, align, mono, raw):
    """text_box of a raw and/or typewriter label (SvgPainter._draw_lines): mono lines are cells x MONO_CELL em wide."""
    lines = _text_lines(text, raw)
    n = len(lines)
    fs = float(font_size)
    lh = _LINE_H * fs
    x0 = y0 = math.inf
    x1 = y1 = -math.inf
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        yc = py + (i - (n - 1) / 2.0) * lh
        if mono:
            cells, _chars = _mono_line(line)
            w = cells * MONO_CELL * fs
        else:
            w = fs * sum(char_em(c) for c in line)
        left = px if align == "left" else (px - w if align == "right" else px - w / 2.0)
        x0, x1 = min(x0, left), max(x1, left + w)
        y0, y1 = min(y0, yc - _ASCENT * fs), max(y1, yc + _ASCENT * fs)
    if not math.isfinite(x0) or not math.isfinite(y0):
        return None
    return x0, y0, x1, y1


def text_box(text, px, py, font_size, align="center", font=None, raw=False):
    """Pixel box (x0, y0, x1, y1) of a label exactly as SvgPainter.draw_text lays it out (rich runs with
    their sizes and baseline shifts, lines stacked around py, text-anchor from `align`), or None if the
    label draws nothing visible. font="mono" / raw=True: typewriter cells / literal text (richtext)."""
    if font == "mono" or raw:
        return _lines_box(text, px, py, font_size, align, font == "mono", raw)
    if not _plain(text).strip():
        return None
    lines = _parse_rich(text)
    n = len(lines)
    lh = _LINE_H * float(font_size)
    x0 = y0 = math.inf
    x1 = y1 = -math.inf
    for i, runs in enumerate(lines):
        yc = py + (i - (n - 1) / 2.0) * lh
        w = 0.0
        for s, lvl in runs:
            size, dy = _layout(lvl, font_size)
            w += size * sum(char_em(c) for c in s)
            y0 = min(y0, yc + dy - _ASCENT * size)
            y1 = max(y1, yc + dy + _ASCENT * size)
        if w <= 0:
            continue
        left = px if align == "left" else (px - w if align == "right" else px - w / 2.0)
        x0, x1 = min(x0, left), max(x1, left + w)
    if not math.isfinite(x0) or not math.isfinite(y0):
        return None
    return x0, y0, x1, y1


class BBoxPainter:
    """A painter (same three methods as SvgPainter/CanvasPainter) that draws nothing and records the pixel
    box of everything visible: paths with half their stroke width, labels via text_box."""

    def __init__(self):
        self.box = None

    def _add(self, x0, y0, x1, y1):
        if self.box is None:
            self.box = [x0, y0, x1, y1]
        else:
            b = self.box
            b[0], b[1], b[2], b[3] = min(b[0], x0), min(b[1], y0), max(b[2], x1), max(b[3], y1)

    def background(self, color):
        pass

    def draw_path(self, pts, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity,
                  contours=None, dash=None):
        stroked = stroke_width > 0 and stroke_opacity > 0
        if not (fill_opacity > 0 or stroked) or len(pts) == 0:
            return
        a = np.asarray(pts, dtype=float).reshape(-1, 2)
        a = a[np.isfinite(a).all(axis=1)]
        if not len(a):
            return
        h = 0.5 * float(stroke_width) if stroked else 0.0
        lo, hi = a.min(axis=0), a.max(axis=0)
        self._add(lo[0] - h, lo[1] - h, hi[0] + h, hi[1] + h)

    def draw_text(self, text, px, py, font_size, color, opacity, align="center", font=None, raw=False):
        if opacity <= 0:
            return
        b = text_box(text, px, py, font_size, align, font, raw)
        if b is not None:
            self._add(*b)


def settings(raw=None):
    """Normalised export settings from the scene's `export` entry (missing or invalid -> defaults)."""
    raw = raw if isinstance(raw, dict) else {}
    mode = raw.get("mode") if raw.get("mode") in MODES else "content"
    def num(key, default, lo):
        try:
            v = float(raw.get(key, default))
        except (TypeError, ValueError):
            return default
        return v if math.isfinite(v) and v >= lo else default
    frame = raw.get("frame")
    try:
        frame = [float(v) for v in frame][:4] if frame is not None else None
        if frame is not None and (len(frame) != 4 or not all(math.isfinite(v) for v in frame)
                                  or frame[0] == frame[2] or frame[1] == frame[3]):
            frame = None
    except (TypeError, ValueError):
        frame = None
    return {"mode": mode, "margin": num("margin", MARGIN, 0.0), "scale": num("scale", SCALE, 1e-3) or SCALE,
            "frame": frame}


def content_box(objectList, camera, axes_on_top=True):
    """Pixel box of everything that is drawn (None for an empty scene)."""
    bp = BBoxPainter()
    paint_scene(bp, objectList, camera, background=None, axes_on_top=axes_on_top)
    return bp.box


def _view_to_px(camera, x, y):
    """World units of the 2D view (screen-plane units in 3D) -> scene pixels, with the camera zoom."""
    upp = camera._upp
    return camera.pixel_width / 2.0 + x / upp, camera.pixel_height / 2.0 - y / upp


def _px_to_view(camera, px, py):
    upp = camera._upp
    return (px - camera.pixel_width / 2.0) * upp, (camera.pixel_height / 2.0 - py) * upp


def export_rect(objectList, camera, st, axes_on_top=True, box=None):
    """(rect, out_size): the cropped view in scene pixels and the displayed size in whole pixels. box (content mode):
    use this pixel box instead of the drawn content (a camera ride: the union over all its frames)."""
    W, H = float(camera.pixel_width), float(camera.pixel_height)
    rect = None
    if st["mode"] == "frame" and st["frame"]:
        fx0, fy0, fx1, fy1 = st["frame"]
        ax, ay = _view_to_px(camera, min(fx0, fx1), max(fy0, fy1))
        bx, by = _view_to_px(camera, max(fx0, fx1), min(fy0, fy1))
        rect = [ax, ay, bx, by]
    elif st["mode"] == "content":
        b = box if box is not None else content_box(objectList, camera, axes_on_top)
        if b is not None:
            m = st["margin"]
            rect = [max(0.0, b[0] - m), max(0.0, b[1] - m), min(W, b[2] + m), min(H, b[3] + m)]
            if rect[2] <= rect[0] or rect[3] <= rect[1]:
                rect = None
    if rect is None:                                             # "canvas", or nothing drawn yet
        rect = [0.0, 0.0, W, H]
    s = st["scale"]
    out = []
    for i in (0, 1):                                             # whole displayed pixels: grow the view evenly
        lo, hi = rect[i], rect[i + 2]
        n = max(1, int(math.ceil((hi - lo) * s - 1e-9)))
        grow = (n / s - (hi - lo)) / 2.0
        if abs(grow) < 1e-6:                                     # already whole (1920 x 0.55 = 1056): keep it exact
            grow = 0.0
        rect[i], rect[i + 2] = lo - grow, hi + grow
        out.append(n)
    return rect, tuple(out)


def article_background(bg):
    """The figure background: transparent stays transparent, the editor's night-mode grey becomes white."""
    if bg is None:
        return None
    c = tuple(float(v) for v in bg)[:3]
    if all(abs(a - b) < 1.5 / 255.0 for a, b in zip(c, _THEME_GREY)):
        return (1.0, 1.0, 1.0)
    return c


def info(rect, size, st, camera):
    """What the export will look like in the article (shown in the editor, printed by the batch tool)."""
    w = size[0]
    shrink = min(1.0, COLUMN_PX / float(w))
    vx0, vy1 = _px_to_view(camera, rect[0], rect[1])
    vx1, vy0 = _px_to_view(camera, rect[2], rect[3])
    return {"mode": st["mode"], "rect": [float(v) for v in rect], "width": int(size[0]), "height": int(size[1]),
            "scale": st["scale"], "column": COLUMN_PX, "fits": w <= COLUMN_PX,
            "ref_text": REF_TEXT_PX, "text_px": REF_TEXT_PX * st["scale"] * shrink,
            "frame": [round(vx0, 4), round(vy0, 4), round(vx1, 4), round(vy1, 4)]}


def render(objectList, camera, background=(1.0, 1.0, 1.0), axes_on_top=True, raw_settings=None, box=None):
    """The article SVG of a built scene and its info dict: (svg_text, info). box: see export_rect."""
    st = settings(raw_settings)
    rect, size = export_rect(objectList, camera, st, axes_on_top, box)
    sp = SvgPainter(camera.pixel_width, camera.pixel_height, font_family=SVG_FONT)
    paint_scene(sp, objectList, camera, background=article_background(background), axes_on_top=axes_on_top)
    return sp.to_svg(view=rect, size=size), info(rect, size, st, camera)
