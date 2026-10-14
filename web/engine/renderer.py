from .camera import Camera

# Backend- AND dimension-agnostic rendering core. It walks the object tree, projects world
# coordinates to pixels through a CAMERA, and calls a "painter" (drawing backend) for every
# path / text. Swapping the camera (2D -> 3D) or the painter (Cairo -> Canvas) needs no change
# here. A painter implements three methods:
#     background(color)
#     draw_path(pixel_points, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity)
#     draw_text(text, px, py, font_size, color, opacity)

_DEFAULT_CAMERA = Camera()


def world_to_pixel(point, camera=None):
    """Convenience: project one world point with the given camera (or the default 2D camera)."""
    return (camera or _DEFAULT_CAMERA).project(point)


def paint_object(painter, obj, camera):
    """Draw one object (and recursively its children) through the painter, projected by camera."""
    text = getattr(obj, "text", None)
    if text is not None:                                          # a Text object
        px, py = camera.project(obj.points[0])
        painter.draw_text(text, px, py, obj.font_size, obj.color, obj.stroke_opacity)
    elif len(obj.points) >= 4:                                    # a Bézier-based object
        pixel_points = [camera.project(p) for p in obj.points]
        painter.draw_path(pixel_points, obj.color, obj.fill_opacity,
                          obj.color, obj.stroke_width, obj.stroke_opacity)
    for sub in obj.subObjects:                                    # children on top
        paint_object(painter, sub, camera)


def paint_scene(painter, objectList, camera=None, background=(1.0, 1.0, 1.0)):
    """Paint the background and then every object, projected through the camera."""
    camera = camera or _DEFAULT_CAMERA
    painter.background(background)
    for obj in objectList:
        paint_object(painter, obj, camera)
