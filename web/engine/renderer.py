import numpy as np
from .camera import Camera
from .bezier import circle_points
from .constants import RIGHT, UP

# Backend- AND dimension-agnostic rendering core. It walks the object tree, projects world
# coordinates to pixels through a CAMERA, and calls a "painter" (drawing backend) for every
# path / text. Swapping the camera (2D -> 3D) or the painter (Cairo -> Canvas) needs no change
# here. A painter implements three methods:
#     background(color)
#     draw_path(pixel_points, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity)
#     draw_text(text, px, py, font_size, color, opacity)

_DEFAULT_CAMERA = Camera()
_CENTER_COLOR = (0.90, 0.25, 0.20)       # the little "this is where it's measured from" dot
_CENTER_RADIUS = 0.05                     # world units -> a small, fixed on-screen dot (2D camera)


def world_to_pixel(point, camera=None):
    """Convenience: project one world point with the given camera (or the default 2D camera)."""
    return (camera or _DEFAULT_CAMERA).project(point)


def _fill_of(obj):
    return obj.fill_color if getattr(obj, "fill_color", None) is not None else obj.color


def _paint_leaf(painter, obj, camera):
    """Draw ONE object (its own geometry), without recursing into children (scalar projection)."""
    text = getattr(obj, "text", None)
    if text is not None:                                          # a Text object
        px, py = camera.project(obj.points[0])
        painter.draw_text(text, px, py, obj.font_size, obj.color, obj.stroke_opacity)
    elif len(obj.points) >= 4:                                    # a Bézier-based object
        pixel_points = [camera.project(p) for p in obj.points]
        painter.draw_path(pixel_points, _fill_of(obj), obj.fill_opacity,
                          obj.color, obj.stroke_width, obj.stroke_opacity,
                          getattr(obj, "_contours", None))
    _paint_center(painter, obj, camera)


def _paint_center(painter, obj, camera):
    if getattr(obj, "show_center", False) and len(obj.points):    # optional centre marker
        c = (obj.points.min(axis=0) + obj.points.max(axis=0)) / 2.0
        marker = [camera.project(p) for p in circle_points(c, _CENTER_RADIUS, RIGHT, UP)]
        painter.draw_path(marker, _CENTER_COLOR, 1.0, _CENTER_COLOR, 1.0, 1.0)


def paint_object(painter, obj, camera):
    """Draw one object and recursively its children (children on top). Used in 2D."""
    if getattr(obj, "_only_3d", False) and getattr(camera, "mode", "2d") != "3d":
        return                                                    # e.g. the z-axis: hidden in 2D view
    _paint_leaf(painter, obj, camera)
    for sub in obj.subObjects:
        paint_object(painter, sub, camera)


def _collect(obj, is_axis, out):
    """Flatten the tree into drawable leaves for 3D, carrying an is_axis flag down the subtree so the
    axes (and everything attached to them) can be lifted ABOVE all other objects after depth sort."""
    # The coordinate grid (_is_grid) is NOT lifted on top: it sits on the z=0 plane and must be OCCLUDED
    # by 3D objects (a surface should cover the floor grid under it), so it is treated as non-axis here
    # and depth-sorts with the scene - otherwise its coarse lines paint over the fine surface mesh.
    axis_here = (is_axis or bool(getattr(obj, "_is_axis", False))) and not bool(getattr(obj, "_is_grid", False))
    if getattr(obj, "text", None) is not None or len(obj.points) >= 4:
        out.append((obj, axis_here))
    for sub in obj.subObjects:
        _collect(sub, axis_here, out)


def _paint_3d(painter, objectList, camera, axes_on_top=True):
    """3D paint: project ALL path vertices in a SINGLE batched matmul (fast in Pyodide), depth-sort,
    draw far-to-near (painter's algorithm). With axes_on_top the axes are drawn LAST (always visible
    through surfaces); otherwise they are depth-sorted with everything else (realistic occlusion)."""
    leaves = []
    for obj in objectList:
        _collect(obj, False, leaves)

    paths = [(o, a) for (o, a) in leaves if getattr(o, "text", None) is None and len(o.points) >= 4]
    texts = [(o, a) for (o, a) in leaves if getattr(o, "text", None) is not None and len(o.points)]

    record = []                                                   # (depth, is_axis, obj, pixels|None)
    if paths:
        counts = [len(o.points) for o, _ in paths]
        allpts = np.concatenate([o.points for o, _ in paths], axis=0)
        cam = camera.view_array(allpts)                           # ONE matmul for the whole scene
        upp = camera._upp
        px = camera.pixel_width / 2 + cam[:, 0] / upp
        py = camera.pixel_height / 2 - cam[:, 1] / upp
        proj = np.column_stack([px, py])
        depth = cam[:, 2]
        off = 0
        for (o, a), c in zip(paths, counts):
            sl = slice(off, off + c); off += c
            record.append((float(depth[sl].mean()), a, o, proj[sl]))
    for o, a in texts:
        record.append((camera.depth(o.points[0]), a, o, None))

    if axes_on_top:
        groups = ([r for r in record if not r[1]], [r for r in record if r[1]])   # axes last -> on top
    else:
        groups = (record,)                                        # one depth-sorted pass (realistic)
    for group in groups:
        group.sort(key=lambda r: r[0])                            # far (small depth) first
        for _d, _a, o, pix in group:
            if getattr(o, "text", None) is not None:
                px0, py0 = camera.project(o.points[0])
                painter.draw_text(o.text, px0, py0, o.font_size, o.color, o.stroke_opacity)
            else:
                painter.draw_path(pix.tolist(), _fill_of(o), o.fill_opacity,
                                  o.color, o.stroke_width, o.stroke_opacity,
                                  getattr(o, "_contours", None))
                _paint_center(painter, o, camera)


def paint_scene(painter, objectList, camera=None, background=(1.0, 1.0, 1.0), axes_on_top=True, skip_gl=False):
    """Paint the background, then every object. In 3D, leaves are drawn far-to-near (painter's
    algorithm) so nearer faces correctly cover farther ones. With axes_on_top (default) the coordinate
    axes are drawn last so they stay visible in front of all objects; with axes_on_top=False the axes
    sit in the normal draw/depth order (realistic occlusion).

    skip_gl: omit objects flagged `_gl` (rendered by the WebGL layer instead) — the editor then paints
    this 2D canvas transparently ON TOP of the WebGL surface."""
    camera = camera or _DEFAULT_CAMERA
    painter.background(background)
    if skip_gl:
        objectList = [o for o in objectList if not getattr(o, "_gl", False)]
    if getattr(camera, "mode", "2d") == "3d":
        _paint_3d(painter, objectList, camera, axes_on_top)
    elif axes_on_top:
        nonaxis = [o for o in objectList if not getattr(o, "_is_axis", False)]
        axis = [o for o in objectList if getattr(o, "_is_axis", False)]
        for obj in nonaxis:
            paint_object(painter, obj, camera)
        for obj in axis:
            paint_object(painter, obj, camera)
    else:
        for obj in objectList:                                    # natural order (axes where inserted)
            paint_object(painter, obj, camera)
