import cairo
from .constants import PIXEL_WIDTH, PIXEL_HEIGHT
from .renderer import paint_scene, world_to_pixel   # world_to_pixel re-exported for convenience


class CairoPainter:
    """Local rendering backend: draws onto a Cairo context. (The web version implements the
    same three methods on an HTML5 Canvas context - see CanvasPainter in the web project.)"""

    def __init__(self, ctx):
        self.ctx = ctx

    def background(self, color):
        self.ctx.set_source_rgb(*color)
        self.ctx.paint()

    def _trace(self, pts):
        ctx = self.ctx
        ctx.move_to(*pts[0])                               # starts a new sub-path
        for i in range(1, len(pts) - 2, 3):                # one cubic segment at a time
            ctx.curve_to(*pts[i], *pts[i + 1], *pts[i + 2])

    def draw_path(self, pixel_points, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity, contours=None, dash=None):
        ctx = self.ctx
        ctx.set_dash(list(dash) if dash else [])
        if contours:                                       # several contours (glyph with a hole) -> even-odd
            off = 0
            for n in contours:
                self._trace(pixel_points[off:off + n]); off += n
            ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        else:
            self._trace(pixel_points)
            ctx.set_fill_rule(cairo.FILL_RULE_WINDING)
        if fill_opacity > 0:
            ctx.set_source_rgba(*fill_color, fill_opacity)
            ctx.fill_preserve()                            # fill, keep path for the stroke
        if stroke_width > 0:
            ctx.set_source_rgba(*stroke_color, stroke_opacity)
            ctx.set_line_width(stroke_width)
            ctx.stroke()
        else:
            ctx.new_path()                                 # clear the kept path

    def draw_text(self, text, px, py, font_size, color, opacity, align="center"):
        from .richtext import plain
        text = plain(text)                                 # Cairo path: sub/superscripts flattened to plain text
        ctx = self.ctx
        ctx.select_font_face("sans-serif")
        ctx.set_font_size(font_size)
        ctx.set_source_rgba(*color, opacity)
        xb, yb, w, h, xa, ya = ctx.text_extents(text)
        x0 = px - xb - (0.0 if align == "left" else (w if align == "right" else w / 2))
        ctx.move_to(x0, py - h / 2 - yb)                   # anchor the text box at (px, py)
        ctx.show_text(text)


def render_to_surface(objectList, camera=None):
    """Render all objects onto a fresh Cairo surface and return it (reused by image + video)."""
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, PIXEL_WIDTH, PIXEL_HEIGHT)
    painter = CairoPainter(cairo.Context(surface))
    paint_scene(painter, objectList, camera)
    return surface


def renderScene(sceneObject, filename="out.png"):
    surface = render_to_surface(sceneObject.objectList, getattr(sceneObject, "camera", None))
    surface.write_to_png(filename)
    return filename
