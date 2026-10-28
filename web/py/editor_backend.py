import json
import numpy as np
from engine.scene_model import ModelScene
from engine.renderer import paint_scene
from engine.constants import PIXEL_WIDTH, PIXEL_HEIGHT, FRAME_HEIGHT
from engine.svg_painter import SvgPainter
from engine import circuit as _circ
from canvas_painter import CanvasPainter

_CIRCUIT_TYPES = ("Component", "Device", "Wire", "Node")


def _axes_for(sc, spec):
    """The panel an object is drawn on: its `on` Axes, else the first Axes (as in ModelScene.construct)."""
    abi = getattr(sc, "axes_by_id", None) or {}
    return abi.get(spec.get("on")) or next(iter(abi.values()), None)


def _world_to_data(ax, w):
    """Inverse of Axes.coords_to_point in x and y (linear or log axes)."""
    if ax is None:
        return float(w[0]), float(w[1])
    fx = (w[0] - ax.origin[0] + ax.x_length / 2.0) / ax.x_length
    fy = (w[1] - ax.origin[1] + ax.y_length / 2.0) / ax.y_length
    if ax.x_log:
        lo, hi = np.log10(ax.x_min), np.log10(ax.x_max); x = 10.0 ** (lo + fx * (hi - lo))
    else:
        x = ax.x_min + fx * (ax.x_max - ax.x_min)
    if ax.y_log:
        lo, hi = np.log10(ax.y_min), np.log10(ax.y_max); y = 10.0 ** (lo + fy * (hi - lo))
    else:
        y = ax.y_min + fy * (ax.y_max - ax.y_min)
    return float(x), float(y)


def circuit_pins():
    """Connection points of every circuit element (component pins, device pins, wire ends, nodes) as JSON
    [{id, type, pin, x, y, px, py}]: data coordinates of its panel and canvas pixels. The editor draws
    them, snaps wires to them and moves attached wire ends along when a part is dragged."""
    sc = _last_scene
    if sc is None:
        return "[]"
    out = []
    for spec in sc.model.get("objects", []):
        t = spec.get("type")
        if t not in _CIRCUIT_TYPES:
            continue
        ax = _axes_for(sc, spec)
        try:
            pins = _circ.pins_world(t, spec.get("args", {}), ax)
        except Exception:
            continue
        for name, w in pins:
            px, py = sc.camera.project(np.asarray(w, dtype=float))
            x, y = _world_to_data(ax, w)
            out.append({"id": spec.get("id"), "type": t, "pin": name, "x": round(x, 9), "y": round(y, 9),
                        "px": float(px), "py": float(py)})
    return json.dumps(out)


def panel_affine(axes_id):
    """Data -> canvas-pixel mapping of a (linear 2D) panel as JSON {ox, oy, xx, xy, yx, yy, x_range, y_range}:
    px = ox + xx*x + yx*y, py = oy + xy*x + yy*y. The editor uses it to draw the schematic grid and to turn
    pointer positions into snapped data coordinates without a Python call per mouse move."""
    sc = _active()
    ax = getattr(sc, "axes_by_id", {}).get(axes_id) if sc is not None else None
    if ax is None:
        return "null"
    def P(x, y):
        return sc.camera.project(np.asarray(ax.coords_to_point(x, y, 0.0), dtype=float))
    p0, px_, py_ = P(0.0, 0.0), P(1.0, 0.0), P(0.0, 1.0)
    return json.dumps({"ox": float(p0[0]), "oy": float(p0[1]),
                       "xx": float(px_[0] - p0[0]), "xy": float(px_[1] - p0[1]),
                       "yx": float(py_[0] - p0[0]), "yy": float(py_[1] - p0[1]),
                       "x_range": [float(ax.x_min), float(ax.x_max)], "y_range": [float(ax.y_min), float(ax.y_max)]})


def export_svg():
    """The current (edit-view) scene as an SVG document string (vector export for the website).
    3D surfaces are drawn by the flat CPU painter here (the WebGL layer has no vector form)."""
    sc = _active()
    if sc is None:
        return ""
    sp = SvgPainter(PIXEL_WIDTH, PIXEL_HEIGHT)
    paint_scene(sp, sc.objectList, sc.camera, background=_last_bg, axes_on_top=_last_axtop)
    return sp.to_svg()

# js_ctx / js_w / js_h come from JavaScript (pyodide.globals.set in editor.js).
painter = CanvasPainter(js_ctx, js_w, js_h)
_last_scene = None
_last_bg = [1.0, 1.0, 1.0]
_last_axtop = True                               # axes drawn on top of objects (vs realistic occlusion)
_play = None                                     # {"scene":..., "bg":..., "axtop":...} while playing
_GL_ENABLED = False                              # set by JS once WebGL inits; gates the hybrid 3D path


def render_model(json_str):
    """Build the scene described by the editor's model (JSON) and paint it to the canvas.
    If the model is (temporarily) invalid — e.g. a half-typed function like 'exp(x' — we keep
    the last good frame and report the error, instead of crashing. Objects only for now."""
    global _last_scene, _last_bg, _last_axtop, _lod_scene
    try:
        model = json.loads(json_str)
        scene = ModelScene(model)
        scene.construct()                       # may fail on an incomplete function expression
        scene.show_static()                     # resting view: transform targets at START, not END
    except Exception as e:
        return "error: " + str(e)               # invalid -> leave the previous frame untouched
    bg = model.get("background", [1.0, 1.0, 1.0])       # None -> transparent
    axtop = bool(model.get("axes_on_top", False))
    _last_scene = scene
    _last_bg = bg
    _last_axtop = axtop
    _lod_scene = None                           # any edit invalidates a stale low-detail copy
    _paint(scene, bg, axtop)
    return "ok:gl" if _gl_on(scene) else "ok"   # ':gl' tells JS to draw the WebGL surface layer


_lod_scene = None                                # a reduced-resolution copy shown during camera moves


def _active():
    return _lod_scene if _lod_scene is not None else _last_scene


# ---------- WebGL hybrid layer: the GPU draws 3D surfaces, the 2D canvas paints everything else ----------
def set_gl_enabled(flag):
    """JS reports whether the WebGL layer initialised. If not, we never skip the surface in the 2D
    painter, so the scene falls back to the (flat) CPU-painted surface — the editor still works."""
    global _GL_ENABLED
    _GL_ENABLED = bool(flag)


def gl_constants():
    """Fixed projection constants so JS can build a camera matrix matching camera.project() exactly."""
    return json.dumps({"w": PIXEL_WIDTH, "h": PIXEL_HEIGHT, "upp": FRAME_HEIGHT / PIXEL_HEIGHT})


def _gl_objs(scene):
    out = []
    def scan(o):
        if getattr(o, "_gl_mesh", None) is not None and getattr(o, "_gl", False):
            out.append(o)
        for s in getattr(o, "subObjects", []):
            scan(s)
    for o in getattr(scene, "objectList", []):
        scan(o)
    return out


def _gl_on(scene):
    return (_GL_ENABLED and scene is not None
            and getattr(getattr(scene, "camera", None), "mode", "2d") == "3d"
            and bool(_gl_objs(scene)))


def _paint(scene, bg, axtop):
    """Paint `scene` to the 2D canvas. When the WebGL layer owns the 3D surface: paint TRANSPARENT and
    SKIP the surface, so the GPU surface (behind) shows through and axes/labels sit on top. Otherwise
    the normal opaque 2D paint (unchanged behaviour)."""
    if _gl_on(scene):
        paint_scene(painter, scene.objectList, scene.camera, background=None, axes_on_top=axtop, skip_gl=True)
    else:
        paint_scene(painter, scene.objectList, scene.camera, background=bg, axes_on_top=axtop)


def gl_active():
    return _gl_on(_active())


def gl_meshes():
    """Surface meshes (WORLD coords) of the ACTIVE scene for the WebGL layer; [] when GL isn't active.
    Byte fields become Uint8Array on the JS side; JS views them as Float32/Uint16 arrays."""
    sc = _active()
    if not _gl_on(sc):
        return []
    out = []
    for o in _gl_objs(sc):
        g = o._gl_mesh
        out.append({"pos": g["pos"], "nrm": g["nrm"], "idx": g["idx"], "zt": g["zt"],
                    "count": g["count"], "z0": g["z0"], "z1": g["z1"],
                    "color": list(getattr(o, "_gl_color", [0.35, 0.60, 0.92])),
                    "opacity": float(getattr(o, "_gl_opacity", 1.0)),
                    "height": bool(getattr(o, "_gl_height", False)),
                    "surf": bool(getattr(o, "_gl_surf", True))})
    return out


def begin_lod(json_str):
    """Build a REDUCED-detail scene once (from the capped model) and show it, WITHOUT discarding the
    full scene. Camera moves then repaint this light scene; end_lod() restores the full one instantly."""
    global _lod_scene
    try:
        model = json.loads(json_str)
        scene = ModelScene(model)
        scene.construct()
        scene.show_static()
    except Exception:
        _lod_scene = None
        return
    _lod_scene = scene
    _paint(scene, model.get("background", [1.0, 1.0, 1.0]), bool(model.get("axes_on_top", False)))


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
        _paint(_last_scene, _last_bg, _last_axtop)


def orbit(theta, phi):
    """Fast 3D orbit: re-aim the ACTIVE scene's camera and repaint (no rebuild). For drag."""
    sc = _active()
    if sc is None or getattr(sc.camera, "mode", "2d") != "3d":
        return
    sc.camera.orient(theta, phi)
    _paint(sc, _last_bg, _last_axtop)


def zoom_to(z):
    """Fast zoom: set the ACTIVE scene's orthographic zoom and repaint (no rebuild). For wheel/buttons."""
    sc = _active()
    if sc is None:
        return
    sc.camera.zoom = float(z) or 1.0
    _paint(sc, _last_bg, _last_axtop)


def pick(px, py):
    """Return the id of the SMALLEST (most specific) object whose bounding box contains the click - so a
    small object isn't shadowed by a bigger one's rectangular box (e.g. a dot sitting inside a function
    graph's wide bbox). The coordinate axes are skipped (pick them from the sidebar), so an empty click
    doesn't grab them. Empty string if nothing matches."""
    if _last_scene is None:
        return ""
    cam = _last_scene.camera
    world = cam.unproject(px, py)
    m = max(0.15, 10.0 * cam._upp)               # world margin, with a ~10px floor so thin objects stay clickable
    best, best_area = "", None
    for oid, obj in _last_scene.objects_by_id.items():
        if getattr(obj, "_is_axis", False):       # don't grab the axes by clicking the canvas
            continue
        if not len(obj.all_points()):             # invisible helpers (Parameter) are picked from the sidebar
            continue
        lo, hi = obj.get_bounding_box()
        if lo[0] - m <= world[0] <= hi[0] + m and lo[1] - m <= world[1] <= hi[1] + m:
            area = max(hi[0] - lo[0], 1e-6) * max(hi[1] - lo[1], 1e-6)
            if best_area is None or area < best_area:
                best, best_area = oid, area
    return best


def unproj(px, py):
    """Screen pixel -> world coordinate (on the camera's focal plane). Lets the editor convert a drag in
    pixels into a world-space move when dragging an object."""
    if _last_scene is None:
        return [0.0, 0.0, 0.0]
    w = _last_scene.camera.unproject(px, py)
    return [float(w[0]), float(w[1]), float(w[2])]


def proj(x, y, z):
    """World coordinate -> screen pixel [px, py] (for drawing the move-gizmo axis arrows)."""
    sc = _active()
    if sc is None:
        return [0.0, 0.0]
    px, py = sc.camera.project(np.array([x, y, z], dtype=float))
    return [float(px), float(py)]


def obj_screen_bbox(oid):
    """Pixel bounding box [x0, y0, x1, y1] of object `oid` (project its world bbox corners). The editor
    draws the selection/move box from this. None if the object is unknown."""
    sc = _active()
    if sc is None or oid not in getattr(sc, "objects_by_id", {}):
        return None
    obj = sc.objects_by_id[oid]
    lo, hi = obj.get_bounding_box()
    xs, ys = [], []
    for x in (lo[0], hi[0]):
        for y in (lo[1], hi[1]):
            for z in (lo[2], hi[2]):
                px, py = sc.camera.project(np.array([x, y, z], dtype=float))
                xs.append(px); ys.append(py)
    return [float(min(xs)), float(min(ys)), float(max(xs)), float(max(ys))]


def nudge_object(oid, dx, dy, dz):
    """FAST object move: translate the ALREADY-BUILT object by a world-space delta and repaint — NO
    scene rebuild. Dragging a heavy mesh (e.g. a Sphere's resolution×resolution quads) used to call
    render_model() every pointer frame, which re-tessellated the whole scene each time and stuttered.
    Translating control points is a cheap array add (see AnimObject.shift); this mirrors the orbit/zoom
    fast path. The editor keeps the model props in sync and does ONE authoritative rebuild on drag end."""
    sc = _active()
    if sc is None:
        return
    obj = getattr(sc, "objects_by_id", {}).get(oid)
    if obj is None:
        return
    obj.shift(np.array([float(dx), float(dy), float(dz)], dtype=float))
    _paint(sc, _last_bg, _last_axtop)


def set_background(bg_json):
    """FAST background change: repaint the ALREADY-BUILT scene with a new backdrop colour — NO rebuild.
    The theme toggle (and the background colour picker) only recolour the canvas; rebuilding the whole
    scene via construct() just to change the backdrop was the lag. Mirrors the orbit/zoom/nudge fast path.
    `bg_json` is a [r,g,b] list, or null for a transparent background."""
    global _last_bg
    sc = _active()
    if sc is None:
        return
    try:
        bg = json.loads(bg_json)
    except Exception:
        return
    _last_bg = bg
    _paint(sc, bg, _last_axtop)


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
             "axtop": bool(model.get("axes_on_top", False))}
    return float(scene.duration)


def play_frame(t):
    """Paint the prepared scene at time t (seconds)."""
    if _play is None:
        return
    sc = _play["scene"]
    sc.seek(t)
    _paint(sc, _play["bg"], _play["axtop"])
