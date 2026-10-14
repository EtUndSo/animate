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
        self.ctx.fillStyle = _rgb(color)
        self.ctx.fillRect(0, 0, self.w, self.h)

    def draw_path(self, pts, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity):
        ctx = self.ctx
        ctx.beginPath()
        ctx.moveTo(pts[0][0], pts[0][1])
        for i in range(1, len(pts), 3):
            ctx.bezierCurveTo(pts[i][0], pts[i][1],
                              pts[i + 1][0], pts[i + 1][1],
                              pts[i + 2][0], pts[i + 2][1])
        if fill_opacity > 0:
            ctx.fillStyle = _rgba(fill_color, fill_opacity)
            ctx.fill()
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
