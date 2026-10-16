import json
from engine.scene_model import ModelScene
from engine.renderer import paint_scene
from canvas_painter import CanvasPainter

# js_ctx / js_w / js_h come from JavaScript (pyodide.globals.set in editor.js).
painter = CanvasPainter(js_ctx, js_w, js_h)
_last_scene = None
_last_bg = [1.0, 1.0, 1.0]
_last_axtop = True                               # axes drawn on top of objects (vs realistic occlusion)
_play = None                                     # {"scene":..., "bg":..., "axtop":...} while playing


def render_model(json_str):
    """Build the scene described by the editor's model (JSON) and paint it to the canvas.
    If the model is (temporarily) invalid — e.g. a half-typed function like 'exp(x' — we keep
    the last good frame and report the error, instead of crashing. Objects only for now."""
    global _last_scene, _last_bg, _last_axtop, _lod_scene
    try:
        model = json.loads(json_str)
        scene = ModelScene(model)
        scene.construct()                       # may fail on an incomplete function expression
    except Exception as e:
        return "error: " + str(e)               # invalid -> leave the previous frame untouched
    bg = model.get("background", [1.0, 1.0, 1.0])       # None -> transparent
    axtop = bool(model.get("axes_on_top", True))
    paint_scene(painter, scene.objectList, scene.camera, background=bg, axes_on_top=axtop)
    _last_scene = scene
    _last_bg = bg
    _last_axtop = axtop
    _lod_scene = None                           # any edit invalidates a stale low-detail copy
    return "ok"


_lod_scene = None                                # a reduced-resolution copy shown during camera moves


def _active():
    return _lod_scene if _lod_scene is not None else _last_scene


def begin_lod(json_str):
    """Build a REDUCED-detail scene once (from the capped model) and show it, WITHOUT discarding the
    full scene. Camera moves then repaint this light scene; end_lod() restores the full one instantly."""
    global _lod_scene
    try:
        model = json.loads(json_str)
        scene = ModelScene(model)
        scene.construct()
    except Exception:
        _lod_scene = None
        return
    _lod_scene = scene
    paint_scene(painter, scene.objectList, scene.camera,
                background=model.get("background", [1.0, 1.0, 1.0]),
                axes_on_top=bool(model.get("axes_on_top", True)))


def end_lod():
    """Leave LOD: copy the camera aim/zoom onto the (already built) full scene and repaint it - NO
    rebuild, so returning to full detail is instant."""
    global _lod_scene
    if _lod_scene is None:
        return
    if _last_scene is not None:
        c = _lod_scene.camera
        _last_scene.camera.orient(c.theta, c.phi)
        _last_scene.camera.zoom = c.zoom
    _lod_scene = None
    if _last_scene is not None:
        paint_scene(painter, _last_scene.objectList, _last_scene.camera, background=_last_bg, axes_on_top=_last_axtop)


def orbit(theta, phi):
    """Fast 3D orbit: re-aim the ACTIVE scene's camera and repaint (no rebuild). For drag."""
    sc = _active()
    if sc is None or getattr(sc.camera, "mode", "2d") != "3d":
        return
    sc.camera.orient(theta, phi)
    paint_scene(painter, sc.objectList, sc.camera, background=_last_bg, axes_on_top=_last_axtop)


def zoom_to(z):
    """Fast zoom: set the ACTIVE scene's orthographic zoom and repaint (no rebuild). For wheel/buttons."""
    sc = _active()
    if sc is None:
        return
    sc.camera.zoom = float(z) or 1.0
    paint_scene(painter, sc.objectList, sc.camera, background=_last_bg, axes_on_top=_last_axtop)


def pick(px, py):
    """Return the id of the topmost object whose bounding box contains the clicked pixel
    (empty string if none). Lets the editor select objects by clicking the canvas."""
    if _last_scene is None:
        return ""
    world = _last_scene.camera.unproject(px, py)
    m = 0.15                                     # small margin so thin objects stay clickable
    for oid, obj in reversed(list(_last_scene.objects_by_id.items())):
        lo, hi = obj.get_bounding_box()
        if lo[0] - m <= world[0] <= hi[0] + m and lo[1] - m <= world[1] <= hi[1] + m:
            return oid
    return ""


def prepare_play(json_str):
    """Build the scene + its animation timeline once; return the total duration (seconds).
    Afterwards the JS player calls play_frame(t) for each frame."""
    global _play
    try:
        model = json.loads(json_str)
        scene = ModelScene(model)
        scene.animating = True                       # animated operators take over their operands
        scene.build_timeline()
    except Exception:
        _play = None
        return 0.0
    _play = {"scene": scene, "bg": model.get("background", [1.0, 1.0, 1.0]),
             "axtop": bool(model.get("axes_on_top", True))}
    return float(scene.duration)


def play_frame(t):
    """Paint the prepared scene at time t (seconds)."""
    if _play is None:
        return
    sc = _play["scene"]
    sc.seek(t)
    paint_scene(painter, sc.objectList, sc.camera, background=_play["bg"], axes_on_top=_play["axtop"])
