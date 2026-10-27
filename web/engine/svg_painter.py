"""SVG painter: the same three painter methods as the Canvas painter, but writing an SVG document.
Used for the editor's "Photo -> SVG" export (vector graphics for the website) and for tests.
Labels go through richtext (sub/superscripts as <tspan>, several lines as several <text> rows)."""
from .richtext import parse as _parse_rich, is_plain as _is_plain, layout as _layout


def _hex(color):
    r, g, b = (max(0, min(255, int(round(c * 255)))) for c in color)
    return "#%02x%02x%02x" % (r, g, b)


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _num(v):
    return ("%.2f" % float(v)).rstrip("0").rstrip(".")


_LINE_H = 1.25


class SvgPainter:
    def __init__(self, width, height, font_family="system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"):
        self.w, self.h = int(width), int(height)
        self.font = font_family
        self.parts = []

    def background(self, color):
        self.parts = []
        if color is not None:
            self.parts.append('<rect width="100%%" height="100%%" fill="%s"/>' % _hex(color))

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

    def draw_text(self, text, px, py, font_size, color, opacity, align="center"):
        anchor = {"left": "start", "right": "end"}.get(align, "middle")
        op = '' if opacity >= 1 else ' fill-opacity="%s"' % _num(opacity)
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

    def to_svg(self):
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">\n%s\n</svg>\n'
                % (self.w, self.h, self.w, self.h, "\n".join(self.parts)))
