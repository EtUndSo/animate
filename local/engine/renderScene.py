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

    def draw_path(self, pixel_points, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity):
        ctx = self.ctx
        ctx.move_to(*pixel_points[0])                      # first anchor
        for i in range(1, len(pixel_points), 3):           # one cubic segment at a time
            ctx.curve_to(*pixel_points[i], *pixel_points[i + 1], *pixel_points[i + 2])
        if fill_opacity > 0:
            ctx.set_source_rgba(*fill_color, fill_opacity)
            ctx.fill_preserve()                            # fill, keep path for the stroke
        ctx.set_source_rgba(*stroke_color, stroke_opacity)
        ctx.set_line_width(stroke_width)
        ctx.stroke()

    def draw_text(self, text, px, py, font_size, color, opacity):
        ctx = self.ctx
        ctx.select_font_face("sans-serif")
        ctx.set_font_size(font_size)
        ctx.set_source_rgba(*color, opacity)
        xb, yb, w, h, xa, ya = ctx.text_extents(text)
        ctx.move_to(px - w / 2 - xb, py - h / 2 - yb)      # center the text box at (px, py)
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
