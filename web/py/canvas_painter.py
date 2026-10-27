# Web rendering backend: the same three painter methods as CairoPainter, but on an HTML5
# Canvas 2D context (passed in from JavaScript via Pyodide). Cubic Béziers map 1:1 to Canvas'
# bezierCurveTo, so there is no quality loss. Labels go through engine.richtext, so every label
# may carry subscripts, superscripts, Greek letters and line breaks (U_{GS}, 10^{-16}, \alpha).
from engine.richtext import parse as _parse_rich, is_plain as _is_plain, layout as _layout

try:                                                # Pyodide: a JS method wants a real JS array
    from pyodide.ffi import to_js as _to_js
except Exception:                                   # plain CPython (tests): pass the list through
    def _to_js(x):
        return x


def _rgb(color):
    r, g, b = (int(round(c * 255)) for c in color)
    return f"rgb({r},{g},{b})"

def _rgba(color, alpha):
    r, g, b = (int(round(c * 255)) for c in color)
    return f"rgba({r},{g},{b},{alpha})"


_LINE_H = 1.25                                      # line height for multi-line labels


class CanvasPainter:
    def __init__(self, ctx, width, height):
        self.ctx = ctx
        self.w = width
        self.h = height

    def background(self, color):
        if color is None:                               # transparent
            self.ctx.clearRect(0, 0, self.w, self.h)
        else:
            self.ctx.fillStyle = _rgb(color)
            self.ctx.fillRect(0, 0, self.w, self.h)

    def _trace(self, pts):
        ctx = self.ctx
        ctx.moveTo(pts[0][0], pts[0][1])
        for i in range(1, len(pts) - 2, 3):
            ctx.bezierCurveTo(pts[i][0], pts[i][1],
                              pts[i + 1][0], pts[i + 1][1],
                              pts[i + 2][0], pts[i + 2][1])

    def draw_path(self, pts, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity,
                  contours=None, dash=None):
        ctx = self.ctx
        ctx.beginPath()
        if contours:                                    # several contours (e.g. a glyph with a hole)
            off = 0
            for n in contours:
                self._trace(pts[off:off + n]); off += n
            fill_rule = "evenodd"                       # so holes are cut out, not filled
        else:
            self._trace(pts)
            fill_rule = "nonzero"
        if fill_opacity > 0:
            ctx.fillStyle = _rgba(fill_color, fill_opacity)
            ctx.fill(fill_rule)
        if stroke_width > 0:
            ctx.strokeStyle = _rgba(stroke_color, stroke_opacity)
            ctx.lineWidth = stroke_width
            if dash:
                ctx.setLineDash(_to_js([float(d) for d in dash]))
                ctx.stroke()
                ctx.setLineDash(_to_js([]))
            else:
                ctx.stroke()

    def _measure(self, s):
        try:
            return float(self.ctx.measureText(s).width)
        except Exception:                               # stub contexts (tests): rough estimate
            return 0.55 * self._size * len(s)

    def draw_text(self, text, px, py, font_size, color, opacity, align="center"):
        ctx = self.ctx
        ctx.fillStyle = _rgba(color, opacity)
        ctx.textBaseline = "middle"
        if _is_plain(text):                             # fast path: exactly the classic single-run label
            ctx.font = f"{font_size}px sans-serif"
            ctx.textAlign = align if align in ("left", "right", "center") else "center"
            ctx.fillText(text, px, py)
            return
        self._size = float(font_size)
        lines = _parse_rich(text)
        lh = _LINE_H * float(font_size)
        n = len(lines)
        ctx.textAlign = "left"
        for i, runs in enumerate(lines):
            y = py + (i - (n - 1) / 2.0) * lh
            laid = []
            for s_, lvl in runs:
                size, dy = _layout(lvl, font_size)
                ctx.font = f"{size}px sans-serif"
                laid.append((s_, size, dy, self._measure(s_)))
            W = sum(w for *_r, w in laid)
            x = px - W / 2.0 if align == "center" else (px if align == "left" else px - W)
            for s_, size, dy, w in laid:
                ctx.font = f"{size}px sans-serif"
                ctx.fillText(s_, x, y + dy)
                x += w
