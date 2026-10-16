# Web rendering backend: the same three painter methods as CairoPainter, but on an HTML5
# Canvas 2D context (passed in from JavaScript via Pyodide). Cubic Béziers map 1:1 to Canvas'
# bezierCurveTo, so there is no quality loss.

def _rgb(color):
    r, g, b = (int(round(c * 255)) for c in color)
    return f"rgb({r},{g},{b})"

def _rgba(color, alpha):
    r, g, b = (int(round(c * 255)) for c in color)
    return f"rgba({r},{g},{b},{alpha})"


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

    def draw_path(self, pts, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity, contours=None):
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
            ctx.stroke()

    def draw_text(self, text, px, py, font_size, color, opacity):
        ctx = self.ctx
        ctx.font = f"{font_size}px sans-serif"
        ctx.fillStyle = _rgba(color, opacity)
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillText(text, px, py)
