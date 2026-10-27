"""General figure primitives for the article graphics (data curves, bands, stems, point clouds,
text boxes, braces, marks, free shapes, tables). Each builder takes (args, style, axes) like the
annotation builders in scene_model and returns an AnimObject in WORLD coordinates (data coordinates
are mapped through the axes where it makes sense, sizes/fonts stay in world/pixel units so nothing
distorts on a non-uniform axes)."""
import re
import numpy as np

from .AnimObject import AnimObject
from .simpleShape import Line, Polygon, Circle, Dot, Ellipse
from .bezier import line_points, smooth_points
from .text import Text
from .richtext import plain as _plain
from .constants import FRAME_HEIGHT, PIXEL_HEIGHT

UPP = FRAME_HEIGHT / PIXEL_HEIGHT                     # world units per pixel (unzoomed frame)
_NUM = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def c2p_fn(axes):
    if axes is not None:
        return lambda x, y, z=0.0: np.asarray(axes.coords_to_point(x, y, z), dtype=float)
    return lambda x, y, z=0.0: np.array([x, y, z], dtype=float)


def xyz(p):
    p = list(p) + [0.0, 0.0, 0.0]
    return float(p[0]), float(p[1]), float(p[2])


def numbers(s):
    """All numbers in a free-form string ("1 2; 3,4\n5e-3 ...")."""
    return [float(m) for m in _NUM.findall(str(s).replace(",", " ") if ";" in str(s) or "\n" in str(s) else str(s))]


def number_list(s):
    """A ';'-, ','-, space- or newline-separated list of numbers."""
    return [float(m) for m in _NUM.findall(str(s))]


def pairs(s):
    """Point list "x,y;x,y;…" or "x y" per line -> [(x, y), ...]."""
    nums = number_list(s)
    return [(nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2)]


def str_list(s):
    return [t.strip() for t in str(s).split(";")] if str(s).strip() else []


def text_width(text, font_size):
    """Rough on-screen width (world units) of a label - for auto-sized boxes and table cells."""
    lines = _plain(text).split("\n")
    return max((0.56 * float(font_size) * len(l) for l in lines), default=0.0) * UPP


def text_height(text, font_size):
    n = max(1, len(_plain(text).split("\n")))
    return (1.25 * n - 0.25) * float(font_size) * UPP


def _styled(obj, style, fill=None, default_color=(0.0, 0.0, 0.0)):
    col = style.get("color", default_color)
    obj.color = col
    obj.stroke_width = float(style.get("stroke_width", obj.stroke_width))
    if fill is not None:
        obj.fill_color = fill
    return obj


# ---------------------------------------------------------------------------------------------
def build_data_curve(args, style, axes):
    """Curve through pasted data points (from the article's Zahlenwerk): a polyline (or a smooth
    Bézier spline) in data coords, optional dot markers. Non-finite values and values that a log
    axis cannot show are dropped (the curve splits there)."""
    c2p = c2p_fn(axes)
    pts = pairs(args.get("data", ""))
    obj = AnimObject()
    col = style.get("color", (0.35, 0.60, 0.92))
    runs, cur = [], []
    for x, y in pts:
        ok = np.isfinite(x) and np.isfinite(y)
        if ok and axes is not None:
            if (getattr(axes, "x_log", False) and x <= 0) or (getattr(axes, "y_log", False) and y <= 0):
                ok = False
        if ok:
            cur.append(c2p(x, y))
        elif cur:
            runs.append(cur); cur = []
    if cur:
        runs.append(cur)
    smooth = bool(args.get("smooth", False))
    leaves = []
    for run in runs:
        if len(run) < 2:
            continue
        leaf = AnimObject()
        leaf.points = smooth_points(run) if (smooth and len(run) >= 3) else line_points(run)
        leaf.color = col
        leaf.stroke_width = float(style.get("stroke_width", 4.0))
        leaves.append(leaf)
    if len(leaves) == 1:
        obj.points = leaves[0].points
    else:
        for leaf in leaves:
            obj.add(leaf)
    if args.get("markers", False):
        r = float(args.get("marker_radius", 0.06))
        for run in runs:
            for w in run:
                d = Dot(center=w, radius=r)
                d.color = col; d.fill_color = col; d.fill_opacity = 1.0; d.stroke_width = 0.0
                d._no_dash = True
                obj.add(d)
    obj.color = col
    return obj


def build_band(args, style, axes):
    """Shaded rectangular region in data coords; full_height / full_width stretch it over the whole
    axes (operating regions, depletion zones, frequency bands). Optional label (top/center/bottom)."""
    c2p = c2p_fn(axes)
    x0, x1 = float(args.get("x_min", 0.0)), float(args.get("x_max", 1.0))
    y0, y1 = float(args.get("y_min", 0.0)), float(args.get("y_max", 1.0))
    if args.get("full_height", False):
        y0, y1 = (axes.y_min, axes.y_max) if axes is not None else (-4.0, 4.0)
    if args.get("full_width", False):
        x0, x1 = (axes.x_min, axes.x_max) if axes is not None else (-7.0, 7.0)
    if x1 < x0:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0
    poly = Polygon([c2p(x0, y0), c2p(x1, y0), c2p(x1, y1), c2p(x0, y1)])
    col = style.get("color", (0.35, 0.60, 0.92))
    poly.color = col
    poly.fill_color = style.get("fill_color", col)
    poly.fill_opacity = float(style.get("fill_opacity", 0.18))
    poly.stroke_width = float(style.get("stroke_width", 0.0))
    obj = AnimObject()
    obj.add(poly)
    label = str(args.get("label", "")).strip()
    if label:
        where = str(args.get("label_at", "top"))
        fs = float(args.get("font_size", 26))
        if where == "top":
            pos = 0.5 * (c2p(x0, y1) + c2p(x1, y1)) + np.array([0.0, -0.9 * fs * UPP, 0.0])
        elif where == "bottom":
            pos = 0.5 * (c2p(x0, y0) + c2p(x1, y0)) + np.array([0.0, 0.9 * fs * UPP, 0.0])
        else:
            pos = 0.5 * (c2p(x0, y0) + c2p(x1, y1))
        obj.add(Text(label, position=pos, font_size=fs, color=col))
    return obj


def build_stem(args, style, axes):
    """Stem plot / line spectrum: vertical stems from `baseline` to y_k at x_k, optional markers and
    one label per stem (";"-separated, formula shorthand allowed)."""
    c2p = c2p_fn(axes)
    xs = number_list(args.get("x", ""))
    ys = number_list(args.get("y", ""))
    labels = str_list(args.get("labels", ""))
    base = float(args.get("baseline", 0.0))
    if axes is not None and getattr(axes, "y_log", False) and base <= 0:
        base = float(axes.y_min)                       # a log axis has no 0: stems start at the bottom
    col = style.get("color", (0.35, 0.60, 0.92))
    sw = float(style.get("stroke_width", 3.0))
    fs = float(args.get("font_size", 24))
    r = float(args.get("marker_radius", 0.07))
    obj = AnimObject()
    for i, (x, y) in enumerate(zip(xs, ys)):
        p0, p1 = c2p(x, base), c2p(x, y)
        ln = Line(p0, p1); ln.color = col; ln.stroke_width = sw
        obj.add(ln)
        if args.get("markers", True):
            d = Dot(center=p1, radius=r); d.color = col; d.fill_color = col; d.fill_opacity = 1.0; d.stroke_width = 0.0
            d._no_dash = True
            obj.add(d)
        if i < len(labels) and labels[i]:
            up = 1.0 if y >= base else -1.0
            obj.add(Text(labels[i], position=p1 + np.array([0.0, up * (r + 0.7 * fs * UPP), 0.0]), font_size=fs, color=col))
    obj.color = col
    return obj


def build_point_cloud(args, style, axes):
    """n random points in a rectangle (data coords), reproducible via `seed`. distribution: uniform,
    exp_y (density decays upward from y_min with scale `decay`), exp_x (decays rightward from x_min).
    hollow = ring markers (holes), else filled dots (electrons)."""
    c2p = c2p_fn(axes)
    n = max(0, int(args.get("n", 50)))
    x0, x1 = float(args.get("x_min", -1.0)), float(args.get("x_max", 1.0))
    y0, y1 = float(args.get("y_min", -1.0)), float(args.get("y_max", 1.0))
    rng = np.random.default_rng(int(args.get("seed", 1)))
    dist = str(args.get("distribution", "uniform"))
    decay = max(1e-9, float(args.get("decay", 0.5)))
    pts = []
    tries = 0
    while len(pts) < n and tries < 50 * max(1, n):
        tries += 1
        if dist == "exp_y":
            x = rng.uniform(x0, x1); y = y0 + rng.exponential(decay * (y1 - y0))
            if y > y1:
                continue
        elif dist == "exp_x":
            y = rng.uniform(y0, y1); x = x0 + rng.exponential(decay * (x1 - x0))
            if x > x1:
                continue
        else:
            x, y = rng.uniform(x0, x1), rng.uniform(y0, y1)
        pts.append((x, y))
    col = style.get("color", (0.35, 0.60, 0.92))
    r = float(args.get("radius", 0.05))
    hollow = bool(args.get("hollow", False))
    obj = AnimObject()
    for x, y in pts:
        d = Circle(center=c2p(x, y), radius=r)
        d.color = col
        d.fill_color = col
        d.fill_opacity = 0.0 if hollow else 1.0
        d.stroke_width = float(style.get("stroke_width", 2.0)) if hollow else 0.0
        obj.add(d)
    obj.color = col
    return obj


def _rounded_rect(c, w, h, r, n=6):
    """Rounded rectangle outline (polyline) centred at c, corner radius r."""
    r = max(0.0, min(r, w / 2.0, h / 2.0))
    pts = []
    corners = [(c[0] + w / 2 - r, c[1] + h / 2 - r, 0.0), (c[0] - w / 2 + r, c[1] + h / 2 - r, np.pi / 2),
               (c[0] - w / 2 + r, c[1] - h / 2 + r, np.pi), (c[0] + w / 2 - r, c[1] - h / 2 + r, 1.5 * np.pi)]
    for cx, cy, a0 in corners:
        for k in range(n + 1):
            a = a0 + (np.pi / 2) * k / n
            pts.append(np.array([cx + r * np.cos(a), cy + r * np.sin(a), c[2]]))
    pts.append(pts[0])
    return pts


def build_text_box(args, style, axes):
    """Text inside a box: rect | round | diamond | ellipse; width/height 0 = fitted to the text (world
    units). Building block for block diagrams, chains of effect and callouts."""
    c2p = c2p_fn(axes)
    text = str(args.get("text", ""))
    fs = float(args.get("font_size", 28))
    c = c2p(*xyz(args.get("center", [0.0, 0.0, 0.0])))
    pad = float(args.get("padding", 0.25))
    w = float(args.get("width", 0.0)) or (text_width(text, fs) + 2 * pad)
    h = float(args.get("height", 0.0)) or (text_height(text, fs) + 2 * pad)
    shape = str(args.get("shape", "rect"))
    if shape == "diamond":
        w2, h2 = w * 1.35, h * 1.6
        body = Polygon([c + np.array([-w2 / 2, 0, 0]), c + np.array([0, -h2 / 2, 0]), c + np.array([w2 / 2, 0, 0]), c + np.array([0, h2 / 2, 0])])
    elif shape == "ellipse":
        body = Ellipse(center=c, width=w * 1.3, height=h * 1.4)
    elif shape == "round":
        body = AnimObject(); body.points = line_points(_rounded_rect(c, w, h, 0.3 * min(w, h)))
    else:
        body = Polygon([c + np.array([-w / 2, -h / 2, 0]), c + np.array([w / 2, -h / 2, 0]), c + np.array([w / 2, h / 2, 0]), c + np.array([-w / 2, h / 2, 0])])
    col = style.get("color", (0.0, 0.0, 0.0))
    body.color = col
    body.fill_color = style.get("fill_color", (1.0, 1.0, 1.0))
    body.fill_opacity = float(style.get("fill_opacity", 1.0))
    body.stroke_width = float(style.get("stroke_width", 3.0))
    obj = AnimObject()
    obj.add(body)
    if text:
        obj.add(Text(text, position=c, font_size=fs, color=col))
    obj.color = col
    return obj


def build_brace(args, style, axes):
    """Curly brace from start to end (data coords); the label sits beyond the cusp. `size` = brace
    depth in world units; flip = other side of the span."""
    c2p = c2p_fn(axes)
    A = c2p(*xyz(args.get("start", [-1.0, 0.0, 0.0])))
    B = c2p(*xyz(args.get("end", [1.0, 0.0, 0.0])))
    d = B - A
    L = float(np.linalg.norm(d))
    obj = AnimObject()
    col = style.get("color", (0.0, 0.0, 0.0))
    if L < 1e-9:
        return obj
    u = d / L
    v = np.array([-u[1], u[0], 0.0]) * (-1.0 if args.get("flip", False) else 1.0)
    r = max(1e-6, min(float(args.get("size", 0.3)), L / 4.0))

    def P(t, off):
        return A + u * t + v * off

    # four quarter circles joined by straight arms: end hook, rise into the cusp, mirror image
    q = [0.5 * np.pi * k / 10 for k in range(11)]
    pts = [P(r - r * np.cos(a), r * np.sin(a)) for a in q]                      # end A: (0,0) -> (r,r)
    pts += [P(L / 2 - r + r * np.sin(a), 2 * r - r * np.cos(a)) for a in q]     # arm -> cusp (L/2, 2r)
    pts += [P(L / 2 + r - r * np.cos(a), 2 * r - r * np.sin(a)) for a in q]     # cusp -> arm
    pts += [P(L - r + r * np.sin(a), r * np.cos(a)) for a in q]                 # arm -> end B (L,0)
    br = AnimObject(); br.points = line_points(pts)
    br.color = col; br.stroke_width = float(style.get("stroke_width", 3.0))
    obj.add(br)
    label = str(args.get("label", "")).strip()
    if label:
        fs = float(args.get("font_size", 26))
        obj.add(Text(label, position=A + u * (L / 2) + v * (2 * r + 0.9 * fs * UPP), font_size=fs, color=col))
    obj.color = col
    return obj


def build_mark(args, style, axes):
    """Check mark (right), cross (wrong) or strike-through (diagonal across width x height)."""
    c2p = c2p_fn(axes)
    c = c2p(*xyz(args.get("center", [0.0, 0.0, 0.0])))
    s = float(args.get("size", 0.5))
    kind = str(args.get("kind", "check"))
    col = style.get("color", (0.17, 0.63, 0.17))
    sw = float(style.get("stroke_width", 5.0))
    obj = AnimObject()
    if kind == "cross":
        for a, b in (((-s / 2, -s / 2), (s / 2, s / 2)), ((-s / 2, s / 2), (s / 2, -s / 2))):
            ln = Line(c + np.array([a[0], a[1], 0.0]), c + np.array([b[0], b[1], 0.0])); ln.color = col; ln.stroke_width = sw
            obj.add(ln)
    elif kind == "strike":
        w, h = float(args.get("width", 1.0)), float(args.get("height", 1.0))
        ln = Line(c + np.array([-w / 2, -h / 2, 0.0]), c + np.array([w / 2, h / 2, 0.0])); ln.color = col; ln.stroke_width = sw
        obj.add(ln)
    else:
        chk = AnimObject()
        chk.points = line_points([c + np.array([-s / 2, 0.0, 0.0]), c + np.array([-s / 8, -s / 2, 0.0]), c + np.array([s / 2, s / 2, 0.0])])
        chk.color = col; chk.stroke_width = sw
        obj.add(chk)
    obj.color = col
    return obj


MATERIALS = {                                         # fill presets for device cross-sections (RGB 0..1)
    "n": (0.80, 0.88, 0.98), "p": (0.98, 0.82, 0.82), "n+": (0.52, 0.70, 0.95), "p+": (0.95, 0.52, 0.52),
    "oxide": (0.86, 0.90, 0.86), "poly": (0.93, 0.66, 0.33), "metal": (0.62, 0.64, 0.70),
    "depletion": (0.93, 0.93, 0.93), "substrate": (0.97, 0.95, 0.88),
}


def build_shape(args, style, axes):
    """Free polygon from a point list (data coords) with optional label at the centroid; `material`
    presets the fill colour (n, p, n+, p+, oxide, poly, metal, depletion, substrate)."""
    c2p = c2p_fn(axes)
    pts = [c2p(x, y) for x, y in pairs(args.get("points", ""))]
    obj = AnimObject()
    if len(pts) < 2:
        return obj
    closed = bool(args.get("closed", True))
    poly = Polygon(pts, closed=closed)
    col = style.get("color", (0.0, 0.0, 0.0))
    mat = str(args.get("material", "custom"))
    fill = MATERIALS.get(mat, style.get("fill_color", col))
    poly.color = col
    poly.fill_color = fill
    poly.fill_opacity = float(style.get("fill_opacity", 0.5)) if closed else 0.0
    if mat in MATERIALS:
        poly.fill_opacity = max(poly.fill_opacity, 0.9)
    poly.stroke_width = float(style.get("stroke_width", 2.0))
    obj.add(poly)
    label = str(args.get("label", "")).strip()
    if label:
        cen = np.mean(np.asarray(pts), axis=0)
        obj.add(Text(label, position=cen, font_size=float(args.get("font_size", 24)), color=col))
    obj.color = col
    return obj


def build_table(args, style, axes):
    """Table / matrix: cells "a,b;c,d", optional row/column headers, highlighted cells "r,c;r,c",
    `brackets` draws matrix parentheses instead of grid lines. position = top-left corner (data coords),
    cell_w / cell_h in world units. Cell text may use formula shorthand."""
    c2p = c2p_fn(axes)
    rows = [[t.strip() for t in r.split(",")] for r in str(args.get("cells", "")).split(";")] if str(args.get("cells", "")).strip() else []
    rl = str_list(args.get("row_labels", ""))
    cl = str_list(args.get("col_labels", ""))
    ncol = max([len(r) for r in rows] + [len(cl)]) if (rows or cl) else 0
    nrow = len(rows)
    cw, ch = float(args.get("cell_w", 1.2)), float(args.get("cell_h", 0.6))
    fs = float(args.get("font_size", 24))
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 1.5))
    tl = c2p(*xyz(args.get("position", [0.0, 0.0, 0.0])))
    off_x = cw if rl else 0.0                          # header column / header row offsets
    off_y = ch if cl else 0.0
    obj = AnimObject()
    hl = set()
    for a, b in pairs(args.get("highlight", "")):
        hl.add((int(a), int(b)))

    def cell_center(i, j):                            # i = row (0 = first data row), j = column
        return tl + np.array([off_x + (j + 0.5) * cw, -(off_y + (i + 0.5) * ch), 0.0])

    fill = style.get("fill_color", (0.96, 0.77, 0.26))
    fo = float(style.get("fill_opacity", 0.35))
    for (i, j) in hl:                                 # highlighted cells first (under the text)
        c = cell_center(i, j)
        box = Polygon([c + np.array([-cw / 2, -ch / 2, 0]), c + np.array([cw / 2, -ch / 2, 0]), c + np.array([cw / 2, ch / 2, 0]), c + np.array([-cw / 2, ch / 2, 0])])
        box.color = fill; box.fill_color = fill; box.fill_opacity = fo; box.stroke_width = 0.0
        obj.add(box)
    if args.get("brackets", False):                   # matrix parentheses left and right of the body
        H = nrow * ch
        for side in (-1, 1):
            x = tl[0] + off_x + (0.0 if side < 0 else ncol * cw) + side * 0.12
            top = np.array([x, tl[1] - off_y, 0.0]); bot = np.array([x, tl[1] - off_y - H, 0.0])
            bulge = np.array([-side * 0.22, 0.0, 0.0])
            arc = AnimObject()
            arc.points = np.array([top - np.array([side * 0.1, 0, 0]), top + bulge * 1.2, bot + bulge * 1.2, bot - np.array([side * 0.1, 0, 0])])
            arc.color = col; arc.stroke_width = 2.0 * sw
            obj.add(arc)
    else:                                             # grid lines around the data cells
        x0, x1 = tl[0] + off_x, tl[0] + off_x + ncol * cw
        y0, y1 = tl[1] - off_y, tl[1] - off_y - nrow * ch
        for k in range(nrow + 1):
            ln = Line(np.array([x0, y0 - k * ch, 0.0]), np.array([x1, y0 - k * ch, 0.0])); ln.color = col; ln.stroke_width = sw; obj.add(ln)
        for k in range(ncol + 1):
            ln = Line(np.array([x0 + k * cw, y0, 0.0]), np.array([x0 + k * cw, y1, 0.0])); ln.color = col; ln.stroke_width = sw; obj.add(ln)
    for i, r in enumerate(rows):
        for j, t in enumerate(r):
            if t:
                obj.add(Text(t, position=cell_center(i, j), font_size=fs, color=col))
    for i, t in enumerate(rl):
        if t:
            obj.add(Text(t, position=tl + np.array([0.5 * cw, -(off_y + (i + 0.5) * ch), 0.0]), font_size=fs, color=col))
    for j, t in enumerate(cl):
        if t:
            obj.add(Text(t, position=tl + np.array([off_x + (j + 0.5) * cw, -0.5 * ch, 0.0]), font_size=fs, color=col))
    obj.color = col
    return obj


BUILDERS = {
    "DataCurve": build_data_curve, "Band": build_band, "Stem": build_stem, "PointCloud": build_point_cloud,
    "TextBox": build_text_box, "Brace": build_brace, "Mark": build_mark, "Shape": build_shape, "Table": build_table,
}
