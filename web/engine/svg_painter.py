"""SVG painter: the same three painter methods as the Canvas painter, but writing an SVG document.
Used for the editor's "Photo -> SVG" export (vector graphics for the website) and for tests.
Labels go through richtext (sub/superscripts as <tspan>, several lines as several <text> rows).
Geometry stays in the scene's pixel space (1920x1080); to_svg(view, size) crops it with the viewBox
and sets the displayed size (engine/export.py decides both for article figures)."""
from .richtext import (parse as _parse_rich, is_plain as _is_plain, layout as _layout, text_lines as _text_lines,
                       mono_line as _mono_line, MONO_CELL)

# A FIXED, metric-compatible font family: Arial, Helvetica, Liberation Sans and Nimbus Sans share the same
# advance widths, so on Windows, macOS/iOS and most Linux systems the text is exactly as wide as
# export.text_box estimates (the crop is computed from those widths). The editor canvas draws
# "sans-serif", which is Arial in Chrome/Edge/Firefox on Windows. Android falls back to Roboto.
# An SVG shown through <img> cannot load web fonts, so Chinese labels use the reader's system CJK font.
SVG_FONT = ("Arial, Helvetica, 'Liberation Sans', 'Nimbus Sans', 'Noto Sans CJK SC', 'Microsoft YaHei', "
            "'PingFang SC', sans-serif")
# Typewriter font (Text.font = "mono"): system monospace fonts only (an SVG in <img> cannot load web fonts). Consolas
# first: it is part of every Windows, so the editor (Chrome), the article and the PDF (headless Chromium) all draw the
# same font here (Cascadia Mono is visible to Chrome only through Windows Terminal and would make them differ); then
# macOS, Linux, Android. Chinese characters in a mono line come from the CJK fonts at the end. Every character is
# PLACED at the centre of its cell (richtext.mono_line), so the font only decides the look, never the width or the
# columns. canvas_painter uses the same list.
MONO_FONT = ("Consolas, Menlo, 'DejaVu Sans Mono', 'Liberation Mono', 'Courier New', "
             "'Noto Sans Mono CJK SC', 'Microsoft YaHei', 'PingFang SC', monospace")


def _hex(color):
    r, g, b = (max(0, min(255, int(round(c * 255)))) for c in color)
    return "#%02x%02x%02x" % (r, g, b)


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _num(v):
    return ("%.2f" % float(v)).rstrip("0").rstrip(".")


_LINE_H = 1.25


class SvgPainter:
    def __init__(self, width, height, font_family=SVG_FONT):
        self.w, self.h = int(width), int(height)
        self.font = font_family
        self.parts = []
        self.bg = None

    def background(self, color):
        self.parts = []
        self.bg = color                                  # drawn by to_svg over exactly the visible view

    def _d(self, pts):
        out = ["M%s %s" % (_num(pts[0][0]), _num(pts[0][1]))]
        for i in range(1, len(pts) - 2, 3):
            out.append("C%s %s %s %s %s %s" % (_num(pts[i][0]), _num(pts[i][1]), _num(pts[i + 1][0]), _num(pts[i + 1][1]),
                                              _num(pts[i + 2][0]), _num(pts[i + 2][1])))
        return "".join(out)

    def draw_path(self, pts, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity,
                  contours=None, dash=None):
        if contours:
            d, off = [], 0
            for n in contours:
                d.append(self._d(pts[off:off + n])); off += n
            d = "".join(d)
            rule = ' fill-rule="evenodd"'
        else:
            d = self._d(pts)
            rule = ""
        a = []
        if fill_opacity > 0:
            a.append('fill="%s"' % _hex(fill_color))
            if fill_opacity < 1:
                a.append('fill-opacity="%s"' % _num(fill_opacity))
        else:
            a.append('fill="none"')
        if stroke_width > 0:
            a.append('stroke="%s" stroke-width="%s"' % (_hex(stroke_color), _num(stroke_width)))
            if stroke_opacity < 1:
                a.append('stroke-opacity="%s"' % _num(stroke_opacity))
            if dash:
                a.append('stroke-dasharray="%s"' % " ".join(_num(v) for v in dash))
            a.append('stroke-linejoin="round" stroke-linecap="butt"')
        self.parts.append('<path d="%s" %s%s/>' % (d, " ".join(a), rule))

    def draw_text(self, text, px, py, font_size, color, opacity, align="center", font=None, raw=False):
        anchor = {"left": "start", "right": "end"}.get(align, "middle")
        op = '' if opacity >= 1 else ' fill-opacity="%s"' % _num(opacity)
        if font == "mono" or raw:
            self._draw_lines(text, px, py, font_size, color, op, align, anchor, font == "mono", raw)
            return
        if _is_plain(text):
            self.parts.append('<text x="%s" y="%s" font-size="%s" font-family="%s" fill="%s" text-anchor="%s" '
                              'dominant-baseline="central"%s>%s</text>'
                              % (_num(px), _num(py), _num(font_size), self.font, _hex(color), anchor, op, _esc(text)))
            return
        lines = _parse_rich(text)
        n = len(lines)
        lh = _LINE_H * float(font_size)
        for i, runs in enumerate(lines):
            y = py + (i - (n - 1) / 2.0) * lh
            spans, cur = [], 0.0                         # dy accumulates in SVG -> emit the difference
            for s_, lvl in runs:
                size, dy = _layout(lvl, font_size)
                attrs = ""
                if abs(dy - cur) > 1e-9:
                    attrs += ' dy="%s"' % _num(dy - cur)
                    cur = dy
                if lvl:
                    attrs += ' font-size="%s"' % _num(size)
                spans.append('<tspan%s>%s</tspan>' % (attrs, _esc(s_)) if attrs else _esc(s_))
            self.parts.append('<text x="%s" y="%s" font-size="%s" font-family="%s" fill="%s" text-anchor="%s" '
                              'dominant-baseline="central"%s>%s</text>'
                              % (_num(px), _num(y), _num(font_size), self.font, _hex(color), anchor, op, "".join(spans)))

    def _draw_lines(self, text, px, py, font_size, color, op, align, anchor, mono, raw):
        """Raw and/or typewriter text: one <text> per line, no rich syntax. Mono: every character (spaces too, so copied
        text keeps them) at the centre of its cell (x list, text-anchor middle, xml:space preserve), so columns and runs
        of spaces hold in any monospace font. Raw in the
        normal font: the line as written, spaces kept (xml:space) when it has runs of them or spaces at its ends."""
        lines = _text_lines(text, raw)
        n = len(lines)
        fs = float(font_size)
        lh = _LINE_H * fs
        for i, line in enumerate(lines):
            y = py + (i - (n - 1) / 2.0) * lh
            if mono:
                cells, chars = _mono_line(line)
                if not chars:
                    continue
                cw = MONO_CELL * fs
                w = cells * cw
                left = px - w / 2.0 if align not in ("left", "right") else (px if align == "left" else px - w)
                xs = " ".join(_num(left + c * cw) for _, c in chars)       # one x per character, spaces included
                self.parts.append('<text x="%s" y="%s" font-size="%s" font-family="%s" fill="%s" text-anchor="middle" '
                                  'dominant-baseline="central" xml:space="preserve"%s>%s</text>'
                                  % (xs, _num(y), _num(fs), MONO_FONT, _hex(color), op, _esc("".join(ch for ch, _ in chars))))
            else:
                if not line.strip():
                    continue
                keep = ' xml:space="preserve"' if ("  " in line or line != line.strip()) else ""
                self.parts.append('<text x="%s" y="%s" font-size="%s" font-family="%s" fill="%s" text-anchor="%s" '
                                  'dominant-baseline="central"%s%s>%s</text>'
                                  % (_num(px), _num(y), _num(fs), self.font, _hex(color), anchor, op, keep, _esc(line)))

    def to_svg(self, view=None, size=None):
        """The SVG document. view = (x0, y0, x1, y1) in scene pixels shown through the viewBox (default: the
        whole frame); size = (width, height) the document is displayed at (default: the view's size). The
        background rectangle covers exactly the view."""
        x0, y0, x1, y1 = view if view is not None else (0, 0, self.w, self.h)
        vw, vh = x1 - x0, y1 - y0
        dw, dh = size if size is not None else (vw, vh)
        def f4(v):
            return ("%.4f" % float(v)).rstrip("0").rstrip(".")
        bg = ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>\n' % (f4(x0), f4(y0), f4(vw), f4(vh), _hex(self.bg))
              if self.bg is not None else "")
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="%s %s %s %s">\n%s%s\n</svg>\n'
                % (f4(dw), f4(dh), f4(x0), f4(y0), f4(vw), f4(vh), bg, "\n".join(self.parts)))
