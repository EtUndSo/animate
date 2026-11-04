"""Animated operation 'directors'. A computation is not just a number - it ANIMATES the process of
the operation. Each director adds the visual pieces to the scene and plays the process, driven by a
ValueTracker (so it scrubs/plays on the timeline). run_time = the animation speed.

v1: convolution (slide g(t-τ) across f, show the overlap product + the result curve being traced).
Summation, Riemann, derivative-as-tangent-slide, etc. follow the same pattern.
"""
import math

import numpy as np

from .AnimObject import AnimObject
from .simpleShape import Dot, Rectangle
from .text import DecimalNumber
from .value_tracker import ValueTracker, always_redraw
from .animation import ChangeValue, FadeIn, FadeOut, Pulse, PulseColor, AppearPulseColor, Rotate, MoveTo, MoveAlongPath
from .rate_functions import smooth
from .bezier import line_points, partial_bezier
from .plotting import sync_pieces
from .calc import make_convolution
from .svg import MathTex
from .constants import BLUE, GREEN, UP, FRAME_HEIGHT, PIXEL_WIDTH, PIXEL_HEIGHT

_FRAME_W = FRAME_HEIGHT * PIXEL_WIDTH / PIXEL_HEIGHT     # world width of the frame
_PX_PER_UNIT = PIXEL_HEIGHT / FRAME_HEIGHT              # canvas pixels per world unit (135)


def _styled(graph, color, stroke_width=4, fill=0.0):
    graph.color = color
    graph.stroke_width = stroke_width
    if fill:
        graph.fill_opacity = fill
    return sync_pieces(graph)                            # a graph split at a gap: every piece takes the style


def convolution(scene, f, g, axes, run_time=6.0, tau_range=None, color=(0.89, 0.29, 0.20),
                f_color=BLUE, g_color=GREEN):
    """Show f(τ) fixed and g(t−τ) sliding across it (entering from the far left, 'from −∞'); fill
    their product (the overlap, whose area is the convolution value) and TRACE the result curve
    (f∗g)(t) up to the current t."""
    x0, x1 = axes.x_min, axes.x_max
    tr = tau_range or (x0, x1)
    conv = make_convolution(f, g, float(tr[0]), float(tr[1]), n=1200)   # fine integration -> clean result

    margin = 0.35 * (x1 - x0)                            # g enters from far left ("−∞") and leaves to
    k = ValueTracker(x0 - margin)                        # the far right ("+∞"), sliding right off-screen
    scene.add(k)

    fgraph = _styled(axes.plot(f), f_color)              # f(τ): fixed
    gslide = always_redraw(lambda: _styled(axes.plot(lambda t: g(k.get_value() - t)), g_color))
    prod = always_redraw(lambda: _styled(axes.plot(lambda t: f(t) * g(k.get_value() - t)),
                                         (0.55, 0.20, 0.75), fill=0.35))   # overlap product (filled)

    # Result curve, sampled UNIFORMLY in x and revealed exactly up to the slide position k, so the
    # drawn leading edge is always (k, conv(k)) - the trace matches the computed value at every t
    # (an earlier version revealed by Bézier parameter on an adaptively-sampled curve, which raced
    # ahead through flat regions and showed values before the overlap).
    N = 420                                              # dense uniform sampling -> smooth, no wobble
    gx = np.linspace(x0, x1, N)
    gw = np.array([axes.coords_to_point(float(gx[i]), float(conv(gx[i]))) for i in range(N)])
    trace = AnimObject(); trace.color = color; trace.stroke_width = 5; trace._role = "conv_trace"

    def _reveal(m):
        idx = int(np.clip((k.get_value() - x0) / (x1 - x0), 0.0, 1.0) * (N - 1))
        m.points = line_points(gw[:idx + 1]) if idx >= 1 else np.zeros((0, 3))
    trace.add_updater(_reveal)

    dot = Dot([0, 0, 0], radius=0.09); dot.color = color
    dot.add_updater(lambda d: setattr(d, "points",
                                      Dot(axes.coords_to_point(k.get_value(), conv(k.get_value())), 0.09).points))

    val = DecimalNumber(0.0, position=axes.coords_to_point(x0, 0) + 2.4 * UP, font_size=30,
                        color=color, decimals=3, prefix="(f∗g)(t) = ")
    val.add_updater(lambda d: d.set_value(conv(k.get_value())))

    scene.add(prod, fgraph, gslide, trace, dot, val)
    scene.play(ChangeValue(k, x1 + margin), run_time=run_time)   # slide all the way across and out


# ---------------------------------------------------------------------------
#  Summation (Σ). The Σ TYPOGRAPHY (sign, limits, step-by-step expansion) is rendered as real LaTeX by
#  a KaTeX overlay in the web editor (editor.js) - a canvas cannot match LaTeX quality. So:
#    * number mode  -> the engine only RESERVES the timeline duration; the overlay draws everything;
#    * function mode -> the engine draws the partial-sum CURVE S_N(x) on the axes (that is graphics,
#      not typography); the overlay draws the Σ expression on top.
# ---------------------------------------------------------------------------

def summation_number(scene, term, i0, i1, symbolic=False, end_label="n", run_time=5.0,
                     color=(0.89, 0.29, 0.20), show_terms=3, animating=False, label_expr=""):
    """Number-mode Σ is drawn by the editor's KaTeX overlay. Here we only reserve the timeline duration
    so the transport clock runs for the right length (the overlay reveals in step with it)."""
    if animating:
        scene.wait(float(run_time))


def summation_function(scene, term, i0, i1, axes, symbolic=False, end_label="n", run_time=5.0,
                       color=(0.89, 0.29, 0.20), show_terms=3, animating=False, label_expr=""):
    """Σ_{i=i0}^{i1} term(i, x): the partial-sum CURVE S_N(x) built as N grows (Fourier-style). Numeric
    limit steps N = i0 … i0+show_terms-1, ⋯, i1-1, i1; a symbolic 'n' shows the first `show_terms` partial
    sums (a drawn curve needs a concrete N). The Σ expression itself is drawn by the KaTeX overlay."""
    i0 = int(i0)

    def partial(m):
        def f(x):
            s = 0.0
            for i in range(i0, m + 1):
                try:
                    s += term(i, x)
                except Exception:
                    pass
            return s
        return f

    if symbolic or i1 is None:
        stops = list(range(i0, i0 + max(1, int(show_terms))))
    else:
        i1 = int(i1)
        if i1 < i0:
            i0, i1 = i1, i0
        n = max(1, int(show_terms))
        stops = list(range(i0, i1 + 1)) if (i1 - i0 + 1) <= n + 2 else list(range(i0, i0 + n)) + [i1 - 1, i1]

    if not animating:                                       # EDIT view: the final partial sum
        scene.add(_styled(axes.plot(partial(stops[-1])), color, stroke_width=4))
        return

    idx = ValueTracker(0.0); scene.add(idx)

    def cur_stop():
        k = int(np.floor(idx.get_value() + 1e-9))
        return stops[0 if k < 0 else (len(stops) - 1 if k > len(stops) - 1 else k)]

    curve = always_redraw(lambda: _styled(axes.plot(partial(cur_stop())), color, stroke_width=4))
    label = DecimalNumber(stops[0], position=axes.coords_to_point(axes.x_max, 0) + 2.4 * UP,
                          font_size=28, color=color, decimals=0, prefix="N = ")
    label.add_updater(lambda d: d.set_value(cur_stop()))
    scene.add(curve, label)
    scene.play(ChangeValue(idx, len(stops) - 1), run_time=run_time)


def _tex_leaves(o, out):
    if len(o.points) >= 2:
        out.append(o)
    for s in o.subObjects:
        _tex_leaves(s, out)


def summation_tex(scene, glyphs, run_time=5.0, color=(0.1, 0.1, 0.1), animating=False,
                  position=(0.0, 2.4, 0.0), height=1.2):
    """Σ as real LaTeX VMobjects (MathTex, from MathJax glyph data), living in the scene graph. During
    play the glyphs are REVEALED in reading order over the run time (positions stay fixed - the
    ground-state layout from KaTeX/MathJax), so the formula builds up step by step and can be scrubbed,
    zoomed and orbited like any object. Per-glyph moves/morphs can build on the same handles later."""
    mt = MathTex(glyphs, height=height, color=color, position=position)
    scene.add(mt)
    groups = mt.subObjects
    if not animating or not groups:
        return
    leafmap = []
    for g in groups:
        ls = []; _tex_leaves(g, ls); leafmap.append(ls)
    n = len(groups)
    rev = ValueTracker(0.0); scene.add(rev)

    def _reveal(_m):
        k = rev.get_value() * n
        for idx, ls in enumerate(leafmap):
            v = 1.0 if idx < k else 0.0                     # glyph fully in once the wavefront passes it
            for lf in ls:
                lf.fill_opacity = v
                lf.stroke_opacity = v
    mt.add_updater(_reveal)
    scene.play(ChangeValue(rev, 1.0), run_time=run_time)


def _color_head_bounds(head, bound_color, var_color, color, var="i"):
    """Tint the Σ/∏ BOUNDS (lower 'i=a', upper 'n'/number) with bound_color. The bounds sit stacked
    OVER/UNDER the big operator (x-centre within the operator's column, y-centre above or below it); the
    summand sits to its RIGHT, a left-hand side such as 'wᵀx =' to its LEFT. So: biggest glyph = the
    operator; a glyph in its column and above/below it is a bound -> the running variable `var` keeps
    var_color, '='/'-' stay `color` (black), the rest (the actual limit numbers/letters) become bound_color.
    Robust even for fraction summands."""
    subs = list(head.subObjects)
    if not subs or bound_color is None:
        return
    def pts(s):
        p = s.all_points()
        return p if len(p) else None
    hs = [(float(np.ptp(p[:, 1])) if (p := pts(s)) is not None else 0.0) for s in subs]
    si = int(np.argmax(hs))                                  # the big operator (tallest glyph)
    sp = pts(subs[si])
    if sp is None:
        return
    sx0, sx1 = float(sp[:, 0].min()), float(sp[:, 0].max())
    sy0, sy1 = float(sp[:, 1].min()), float(sp[:, 1].max())
    pad = 0.5 * (sx1 - sx0)                                  # a wide lower limit ('i=10') may reach past the left edge
    for j, s in enumerate(subs):
        if j == si:
            continue
        p = pts(s)
        if p is None:
            continue
        xc, yc = float(p[:, 0].mean()), float(p[:, 1].mean())
        if sx0 - pad <= xc <= sx1 and (yc > sy1 or yc < sy0):   # stacked on the operator -> a bound
            tex = getattr(s, "_tex", "")
            col = var_color if tex == var else (color if tex in ("=", "-", "−") else bound_color)
            stack = [s]
            while stack:
                o = stack.pop()
                if len(o.points):
                    o.color = col
                    o.fill_color = col
                stack.extend(o.subObjects)


_FORM_KEYS = ("abstract", "index", "subst", "value")   # the forms a term column passes through, in order


def _first_half(t):                                      # a fade that is done halfway through its step ...
    return smooth(min(1.0, 2.0 * t))


def _second_half(t):                                     # ... and one that only starts there: no double exposure
    return smooth(max(0.0, 2.0 * t - 1.0))


def _tex_em(glyphs):
    """The em of a glyph list in its own units. MathJax places normal-size glyphs with scale 1 (scripts 0.707)
    in font units of 1000 per em, so em = 1000 x the largest glyph scale (0 = unknown)."""
    s = 0.0
    for g in glyphs or []:
        m = g.get("m")
        if m and len(m) >= 2:
            s = max(s, math.hypot(float(m[0]), float(m[1])))
    return 1000.0 * s


def _form_at(col, key):
    """(key, glyphs) a term column shows in the row `key` of the all-steps figure: that form, or the last one
    before it (a symbolic term has no value -> its substituted form stays)."""
    best = None
    for k in _FORM_KEYS:
        if col.get(k):
            best = (k, col[k])
        if k == key:
            break
    return best


def summation_choreo(scene, choreo, run_time=6.0, color=(0.0, 0.0, 0.0), value_color=(0.17, 0.63, 0.17),
                     var_color=(1.0, 0.50, 0.05), end_color=(0.58, 0.40, 0.74),
                     flash_color=(0.40, 0.70, 1.0), bound_color=(0.84, 0.15, 0.16),
                     animating=False, position=(-6.2, 2.4, 0.0), height=0.9,
                     all_steps=False, max_width=0.0, font_size=0.0):
    """Step-by-step Σ / ∏ / scalar product uᵀv (number mode). PLAY: the head (Σ expression) appears, then for
    each term the ABSTRACT summand appears, its index is SUBSTITUTED (crossfade), then it is COMPUTED to a
    value (crossfade); a '+' fades in with a short Σ pulse (the '+' springs from the sum). The scalar
    product also shows its two vectors first; each term passes through one more form (w_j x_j -> w_1 x_1 ->
    3·120 -> 360) and its pair of components lights up while the index and the numbers are put in. All via
    FadeIn/FadeOut/Pulse (contract-safe, scrubbable).

    `choreo` = {head, cols: [ {t:'op'|'plus'|'ell'|'total', g} | {t:'term', abstract, index?, subst,
    value|null, row?} ], var?, vectors?, rows?, stages?} (glyph lists from MathJax; var = running index,
    default 'i'; vectors = both column vectors, glyphs tagged with their table `cell`; rows = rows per vector;
    stages = the forms of the rows of the all-steps figure).

    Layout: one shared scale, the head is `height` tall (or the formula has the em `font_size` canvas px).
    STATIC (edit view / article figure): all_steps=False -> head = final forms = total in one row (as the
    animation ends); all_steps=True -> every step as its own row, '=' under '=' (head = substituted =
    values = total). max_width > 0 (world units) wraps long rows before a '+' or '=' (continuation indented
    after the '='); without it one row is shrunk to the frame width.

    A scalar product shown as 'komponenten' or 'matrix' (choreo['dot']) is drawn by dot_display instead."""
    if choreo.get("dot"):
        return dot_display(scene, choreo, run_time=run_time, color=color, value_color=value_color, var_color=var_color,
                           end_color=end_color, flash_color=flash_color, animating=animating, position=position,
                           height=height, max_width=max_width, font_size=font_size)
    gap = 0.14
    var = str(choreo.get("var") or "i")

    def raw(glyphs, col, tint=False, keep=False):
        # tint: the running-variable glyph (`var`) gets var_color (per-glyph col; the rest stay `col`).
        # keep: leave it in MathJax's frame (the parts of the vectors must stay where they are relative to
        # each other); otherwise centred at the origin.
        gl = glyphs or []
        if tint and var_color is not None:
            gl = [dict(g, col=var_color) if g.get("c") == var else g for g in gl]
        return MathTex(gl, scale=1.0, color=col, position=None if keep else (0.0, 0.0, 0.0))   # RAW MathJax units

    def dims(objs):
        p = [o.all_points() for o in objs]
        p = np.vstack([q for q in p if len(q)]) if any(len(q) for q in p) else np.zeros((0, 3))
        return (float(np.ptp(p[:, 0])), float(np.ptp(p[:, 1]))) if len(p) else (0.0, 0.0)

    def form(key, glyphs):
        return (key, raw(glyphs, value_color if key == "value" else color, tint=(key == "abstract")))

    def slot(col):
        # one column: a term passes through its forms (abstract -> index -> subst -> value), the rest is one piece
        t = col.get("t")
        if t == "term":
            forms = [form(k, col[k]) for k in _FORM_KEYS if col.get(k)]
        else:
            forms = [("g", raw(col.get("g"), end_color if t == "total" else color))]   # the total is the end result
        return {"t": t, "forms": forms, "row": col.get("row")}

    head = raw(choreo.get("head"), color, tint=True)        # the running variable under the Σ is tinted
    _color_head_bounds(head, bound_color, var_color, color, var)   # lower/upper limits -> bound_color
    hw, hh = dims([head])
    cols = choreo.get("cols", [])
    head_slot = {"t": "head", "forms": [("g", head)], "row": None}

    # the two column vectors (scalar product): names/brackets as one part, every table cell as its own part
    vparts, vcells = [], {}
    vg = choreo.get("vectors") or []
    if vg:
        rest = [g for g in vg if g.get("cell") is None]
        if rest:
            vparts.append(raw(rest, color, keep=True))
        for c in sorted({g["cell"] for g in vg if g.get("cell") is not None}):
            vcells[c] = raw([g for g in vg if g.get("cell") == c], color, keep=True)
            vparts.append(vcells[c])
    nrows = int(choreo.get("rows") or 0)

    def pair(row):                                           # the two components w_j, x_j of a term
        if row is None or not nrows:
            return []
        return [vcells[c] for c in (row, nrows + row) if c in vcells]

    steps = all_steps and not animating
    if steps:                                                # rows "= …" per step, the total after the last one
        eq = cols[0] if cols and cols[0].get("t") == "op" else None
        k0 = 1 if eq is not None else 0
        k1 = next((i for i in range(k0, len(cols)) if cols[i].get("t") == "op"), len(cols))
        body, tail = cols[k0:k1], cols[k1:]
        terms = [c for c in body if c.get("t") == "term"]
        keys = [k for k in (choreo.get("stages") or ["subst", "value"]) if k in _FORM_KEYS]
        keys = [k for k in keys if any(c.get(k) for c in terms)]
        lines = []
        for n, key in enumerate(keys):
            items = [head_slot] if n == 0 else []
            if eq is not None:
                items.append(slot(eq))
            for c in body:
                if c.get("t") == "term":
                    f = _form_at(c, key)
                    items.append({"t": "term", "forms": [form(*f)] if f else [], "row": c.get("row")})
                else:
                    items.append(slot(c))
            lines.append(items)
        if not lines:
            lines = [[head_slot]]
        lines[-1].extend(slot(c) for c in tail)
    else:                                                    # the column choreography, one logical row
        lines = [[head_slot] + [slot(c) for c in cols]]

    items_all = [it for ln in lines for it in ln]
    objs = [m for it in items_all for _, m in it["forms"]] + vparts
    rawdim = {id(it): dims([m for _, m in it["forms"]]) for it in items_all}
    vw, vh = dims(vparts) if vparts else (0.0, 0.0)

    # --- one shared scale K: the head `height` tall, or the em = font_size canvas px ---
    em = _tex_em(choreo.get("head"))
    if font_size and font_size > 0 and em > 0:
        K0 = (float(font_size) / _PX_PER_UNIT) / em
    else:
        K0 = (height / hh) if hh > 1e-9 else 1.0
    wrap = steps or (max_width and max_width > 0)
    avail = float(max_width) if (max_width and max_width > 0) else _FRAME_W * 0.94

    def row_gap(K):                                          # between rows: ~0.45 em (a Σ head with limits is ~2.9 em)
        return 0.16 * K * hh

    def chunks(items):                                       # break only before '+' / '=' (an '=' after the head stays)
        out, cur = [], []
        for it in items:
            if it["t"] in ("plus", "op") and cur and not (len(cur) == 1 and cur[0]["t"] == "head"):
                out.append(cur); cur = []
            cur.append(it)
        if cur:
            out.append(cur)
        return out

    def layout(K):
        """Rows [(item, x)] (x = left edge relative to the block's left) at scale K, and whether it fits."""
        w = lambda it: K * rawdim[id(it)][0]
        eqw = next((w(it) for ln in lines for it in ln if it["t"] == "op"), 0.0)
        x_eq = K * hw + gap                                  # the column of the first '='
        cont = x_eq + eqw + gap                              # a continuation row starts after the '='
        rows = []
        for li, items in enumerate(lines):
            row, x = [], (0.0 if li == 0 else x_eq)
            for ch in chunks(items):
                cw = sum(w(it) for it in ch) + gap * (len(ch) - 1)
                if row and x + gap + cw > avail + 1e-9:     # '= total' stays under the '=', '+ term' moves in
                    rows.append(row); row, x = [], (x_eq if ch[0]["t"] == "op" else cont)
                for it in ch:
                    if row:
                        x += gap
                    row.append((it, x)); x += w(it)
            rows.append(row)
        right = max((x + w(it) for row in rows for it, x in row[-1:]), default=0.0)
        hts = [K * max((rawdim[id(it)][1] for it, _ in row), default=0.0) for row in rows]
        vgap = row_gap(K)
        tall = sum(hts) + vgap * (len(rows) - 1) + ((K * vh + vgap) if vparts else 0.0)
        fits = max(right, K * vw) <= avail + 1e-9 and tall <= FRAME_HEIGHT * 0.94
        return rows, fits, hts, vgap

    if wrap:
        K = K0
        if not layout(K)[1]:                                 # too wide or too tall -> largest scale that fits
            lo, hi = K0 * 1e-3, K0                           # (bounds relative to K0: glyphs come in font units,
            for _ in range(40):                              #  1000 per em, so K is small, ~5e-4)
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if layout(mid)[1] else (lo, mid)
            K = lo
    else:                                                    # one row, shrunk to the frame width (as before)
        total_w = sum(rawdim[id(it)][0] for it in lines[0])
        ncol = len(lines[0])
        K, floor = K0, K0 * 0.02
        if total_w > 1e-9:
            K = min(K, max(floor, (avail - ncol * gap) / total_w))
        if vw > 1e-9:                                        # the vectors above the row must fit as well
            K = min(K, max(floor, avail / vw))
            rh = max((rawdim[id(it)][1] for it in lines[0]), default=0.0)
            K = min(K, max(floor, FRAME_HEIGHT * 0.94 / max(1e-9, rh + vh + 0.16 * hh)))
    for m in objs:
        m.scale(K, around=np.zeros(3))

    def W(it):
        return dims([m for _, m in it["forms"]])[0]

    def place(it, left, yc):
        for _, m in it["forms"]:
            m.move_to(np.array([left + W(it) / 2.0, yc, 0.0]))

    def place_vectors(left, yc):
        if vparts:
            p = np.vstack([q.all_points() for q in vparts if len(q.all_points())])
            d = np.array([left - p[:, 0].min(), yc - (p[:, 1].min() + p[:, 1].max()) / 2.0, 0.0])
            for q in vparts:
                q.shift(d)

    if wrap:
        rows, _fits, hts, vgap = layout(K)
        bw = max((x + W(it) for row in rows for it, x in row[-1:]), default=0.0)
        bw = max(bw, dims(vparts)[0] if vparts else 0.0)
        vh2 = dims(vparts)[1] if vparts else 0.0
        tall = sum(hts) + vgap * (len(rows) - 1) + ((vh2 + vgap) if vparts else 0.0)
        left = float(position[0]) - bw / 2.0
        top = float(position[1]) + tall / 2.0
        if vparts:
            place_vectors(left, top - vh2 / 2.0); top -= vh2 + vgap
        for row, h in zip(rows, hts):
            for it, x in row:
                place(it, left + x, top - h / 2.0)
            top -= h + vgap
        order = [it for row in rows for it, _ in row]
    else:                                                    # left to right, centred on position x
        widths = [W(it) for it in lines[0]]
        total = sum(widths) + len(widths) * gap
        x = float(position[0]) - total / 2.0
        y = float(position[1])
        for it, sw in zip(lines[0], widths):
            for _, m in it["forms"]:
                m.move_to(np.array([x + sw / 2.0, y, 0.0]))  # centred in its slot (the forms differ in width)
            x += sw + gap
        if vparts:                                           # the vectors above the row, flush left
            rh = max((dims([m for _, m in it["forms"]])[1] for it in lines[0]), default=0.0)
            vh2 = dims(vparts)[1]
            vgap = row_gap(K)
            place_vectors(float(position[0]) - total / 2.0, y + rh / 2.0 + vgap + vh2 / 2.0)
        order = lines[0]

    if not animating:                                       # EDIT view / article figure: static
        scene.add(*vparts)
        for it in order:
            if it["forms"]:
                scene.add(it["forms"][-1][1])              # a term shows its last form (the computed value)
        return

    # the big Σ glyph = the tallest sub-group of the head; only IT pulses + flashes light blue on a '+'
    def _biggest(mt):
        best, bh = None, -1.0
        for sub in mt.subObjects:
            p = sub.all_points()
            if len(p):
                h = float(np.ptp(p[:, 1]))
                if h > bh:
                    bh, best = h, sub
        return best
    sigma = _biggest(head)

    plays = [[FadeIn(q) for q in vparts]] if vparts else []  # 0) the two vectors (scalar product)
    plays.append([FadeIn(head)])                             # 1) the Σ expression appears
    for it in order[1:]:
        t = it["t"]
        if t in ("op", "plus", "ell", "total"):
            m = it["forms"][0][1]
            if t == "plus":
                # the '+' springs in (grows + flashes flash_color) AND the big Σ pulses the same colour
                sig = PulseColor(sigma, color=flash_color) if sigma is not None else Pulse(head)
                plays.append([AppearPulseColor(m, color=flash_color), sig])
            else:
                plays.append([FadeIn(m)])
        else:                                                # term: abstract -> (index ->) substitute -> compute
            prev = None
            # Σ/∏: abstract, substituted and value nearly cover each other (1/i² -> 1/1²), a crossfade reads as one
            # sharp formula. The scalar product's forms do not (w₁x₁ -> 3·120 -> 360): crossfaded they would sit
            # half-transparent on top of each other, so there the old form leaves before the new one comes.
            crisp = it["row"] is not None
            for key, m in it["forms"]:
                if prev is None:
                    anims = [FadeIn(m)]
                elif crisp:
                    anims = [FadeOut(prev, rate_func=_first_half), FadeIn(m, rate_func=_second_half)]
                else:
                    anims = [FadeOut(prev), FadeIn(m)]
                if key in ("index", "subst"):                # the pair w_j, x_j lights up (colour only) while it is put in
                    anims += [PulseColor(q, factor=1.0, color=var_color) for q in pair(it["row"])]
                plays.append(anims)
                prev = m

    per = run_time / max(1, len(plays))
    for anims in plays:
        scene.play(*anims, run_time=per)


# ---------------------------------------------------------------------------
#  Scalar product, two more representations (dot_display). Same glyph pieces, same MathTex drawing as Σ.
# ---------------------------------------------------------------------------
def _mt(glyphs, col, keep=False):
    """A piece in raw MathJax units: centred at the origin, or (keep) where MathJax put it."""
    return MathTex(glyphs or [], scale=1.0, color=col, position=None if keep else (0.0, 0.0, 0.0))


def _bbox(objs):
    """[x0, y0, x1, y1] of all points of objs, or None."""
    ps = [p for p in (o.all_points() for o in objs) if len(p)]
    if not ps:
        return None
    p = np.vstack(ps)
    return np.array([p[:, 0].min(), p[:, 1].min(), p[:, 0].max(), p[:, 1].max()], dtype=float)


def _cen(objs):
    b = _bbox(objs)
    return np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0, 0.0]) if b is not None else np.zeros(3)


def _put(objs, centre=None, left=None, right=None, y=None):
    """Move a group rigidly: its centre to `centre`, or its left (right) edge to x = left (right), centred at height y."""
    b = _bbox(objs)
    if b is None:
        return
    if centre is not None:
        d = (float(centre[0]) - (b[0] + b[2]) / 2.0, float(centre[1]) - (b[1] + b[3]) / 2.0)
    else:
        d = ((left - b[0]) if left is not None else (right - b[2]), (y - (b[1] + b[3]) / 2.0) if y is not None else 0.0)
    for o in objs:
        o.shift(np.array([d[0], d[1], 0.0]))


def _split_cells(glyphs, col):
    """A matrix piece in its parts (MathJax's frame): brackets/names as one part, one part per table cell."""
    gl = glyphs or []
    rest = [g for g in gl if g.get("cell") is None]
    cells = {c: _mt([g for g in gl if g.get("cell") == c], col, keep=True)
             for c in sorted({g["cell"] for g in gl if g.get("cell") is not None})}
    return (_mt(rest, col, keep=True) if rest else None), cells


def _spiral(c, p0, p1, n=48):
    """Path p0 -> p1 turning around c (angle and radius interpolated): the entries of a vector that turns by 90°
    travel on arcs and stay upright."""
    v0, v1 = p0 - c, p1 - c
    r0, r1 = float(np.hypot(v0[0], v0[1])), float(np.hypot(v1[0], v1[1]))
    if min(r0, r1) < 1e-9:
        return np.array([p0 + (p1 - p0) * t for t in np.linspace(0.0, 1.0, n)])
    a0, a1 = math.atan2(v0[1], v0[0]), math.atan2(v1[1], v1[0])
    da = (a1 - a0 + math.pi) % (2.0 * math.pi) - math.pi
    return np.array([c + np.array([(r0 + (r1 - r0) * t) * math.cos(a0 + da * t), (r0 + (r1 - r0) * t) * math.sin(a0 + da * t), 0.0])
                     for t in np.linspace(0.0, 1.0, n)])


def _lay_down(p0, p1, n=48):
    """Path p0 -> p1 that runs sideways first and then settles (the second vector laid onto the row vector)."""
    c = np.array([p1[0], p0[1], 0.0])
    t = np.linspace(0.0, 1.0, n)[:, None]
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * c + t ** 2 * p1


def dot_display(scene, choreo, run_time=6.0, color=(0.0, 0.0, 0.0), value_color=(0.17, 0.63, 0.17),
                var_color=(1.0, 0.50, 0.05), end_color=(0.58, 0.40, 0.74), flash_color=(0.40, 0.70, 1.0),
                animating=False, position=(0.0, 0.0, 0.0), height=0.9, max_width=0.0, font_size=0.0):
    """Scalar product uᵀv as 'komponenten' or 'matrix' (choreo['dot'] = {mode, m, ell, g: {LaTeX pieces}, vals}).

    komponenten: both vectors as columns side by side. Row by row the pair is marked, a '·' appears between the
      vectors and '= product' behind them; at the end the sum line uᵀv = … = total.
    matrix: u turns by 90° into the row vector uᵀ (its brackets turn, its entries travel on arcs and stay
      upright), v is laid onto the row so that each v_j sits under u_j; pair by pair the mark, the '·' and the
      product after '=' (resp. '+'), at the end '= total'.
    The static view (edit view, article figure) is the end state. Sizes as in summation_choreo (font_size /
    head height); max_width > 0 limits the width (the formula shrinks)."""
    D = choreo.get("dot") or {}
    G = D.get("g") or {}
    mode = D.get("mode")
    R = int(D.get("m") or 0)
    ell = ([bool(x) for x in (D.get("ell") or [])] + [False] * R)[:R]
    vals = (list(D.get("vals") or []) + [None] * R)[:R]
    head_g = choreo.get("head") or []
    em = _tex_em(head_g)
    hb = _bbox([_mt(head_g, color)])
    hh = float(hb[3] - hb[1]) if hb is not None else 0.0
    e = em if em > 0 else (hh / 2.9 if hh > 0 else 1.0)    # one em in raw units
    gap, pad = 0.5 * e, 0.15 * e

    def piece(key, col=color):
        return _mt(G.get(key), col)

    def width(o):
        b = _bbox([o])
        return float(b[2] - b[0]) if b is not None else 0.0

    # the result line from the column choreography ('=' value '+' value … '=' total), one group per term
    groups, cur = [], []
    for col in choreo.get("cols", []):
        t = col.get("t")
        g = (col.get("value") or col.get("subst")) if t == "term" else col.get("g")
        cur.append(_mt(g, value_color if t == "term" else (end_color if t == "total" else color)))
        if t in ("term", "ell", "total"):
            groups.append((t, col.get("row"), cur)); cur = []
    if cur:
        groups.append(("op", None, cur))

    def lay_line(items, left, y):                            # left to right, centred on height y
        x = left
        for m in items:
            if _bbox([m]) is not None:
                _put([m], left=x, y=y); x += width(m) + gap

    u_rest, u_cells = _split_cells(G.get("colU"), color)
    v_rest, v_cells = _split_cells(G.get("colV"), color)
    U = [o for o in [u_rest] if o is not None] + list(u_cells.values())
    V = [o for o in [v_rest] if o is not None] + list(v_cells.values())
    marks = []                                               # per shown term: raw rectangles [x0, y0, x1, y1]
    moves = []                                               # animation: (obj, kind, raw start centre, raw end centre)
    start_only, plays_spec = [], {}

    if mode == "matrix":
        g_rest, g_cells = _split_cells(G.get("grid"), color)  # targets of both rows, the '·' row, ⋯ of a long vector
        grid = list(g_cells.values())
        _put(grid, left=0.0, y=0.0)
        tU = {r: _cen([g_cells[r]]) for r in range(R) if r in g_cells}
        tV = {r: _cen([g_cells[2 * R + r]]) for r in range(R) if (2 * R + r) in g_cells}
        dots = {r: g_cells[R + r] for r in range(R) if (R + r) in g_cells}
        mean_y = lambda d: float(np.mean([p[1] for p in d.values()])) if d else 0.0
        y0, y2 = mean_y(tU), mean_y(tV)
        y1 = mean_y({r: _cen([o]) for r, o in dots.items()}) if dots else (y0 + y2) / 2.0
        bU = _bbox([g_cells[r] for r in range(R) if r in g_cells])
        r_rest, _ = _split_cells(G.get("rowU"), color)       # only its brackets are used
        lp, rp = AnimObject(), AnimObject()
        if r_rest is not None:
            mid = _cen([r_rest])[0]
            for sub in list(r_rest.subObjects):
                (lp if _cen([sub])[0] < mid else rp).add(sub)
        _put([lp], right=bU[0] - pad, y=y0)
        _put([rp], left=bU[2] + pad, y=y0)
        br = [o for o in (lp, rp) if _bbox([o]) is not None]
        lbl_ut, lbl_v = piece("nameUT"), piece("nameV")    # names left of both rows (left of the widest column)
        lab_r = min(_bbox(grid)[0], _bbox([lp])[0] if _bbox([lp]) is not None else bU[0]) - gap
        _put([lbl_ut], right=lab_r, y=y0)
        _put([lbl_v], right=lab_r, y=y2)
        right = max(_bbox(grid + br)[2], bU[2])
        lay_line([m for _, _, ms in groups for m in ms], right + 1.5 * gap, y1)
        # the end state: entries at the targets (a ⋮ of a long vector becomes the grid's ⋯), brackets, labels
        in_col = {id(o): _cen([o]) for o in list(u_cells.values()) + list(v_cells.values())}   # place inside its column
        for r in range(R):
            if r in u_cells and r in tU:
                _put([u_cells[r]], centre=tU[r])
            if r in v_cells and r in tV:
                _put([v_cells[r]], centre=tV[r])
            if not ell[r] and r in tU and r in tV:
                b = _bbox([g_cells[r], g_cells[2 * R + r]] + ([dots[r]] if r in dots else []))
                marks.append((r, [b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad]))
        ell_u = [g_cells[r] for r in range(R) if ell[r] and r in g_cells]
        ell_v = [g_cells[2 * R + r] for r in range(R) if ell[r] and (2 * R + r) in g_cells]
        final = ([u_cells[r] for r in range(R) if not ell[r] and r in u_cells] + [v_cells[r] for r in range(R) if not ell[r] and r in v_cells]
                 + ell_u + ell_v + list(dots.values()) + br + [lbl_ut, lbl_v] + [m for _, _, ms in groups for m in ms])
        bf = _bbox(final)                                    # the end state (before the animation's start is set up)
        if animating:                                        # start: both columns side by side, u's centre = row centre
            for o in list(u_cells.values()) + list(v_cells.values()):
                _put([o], centre=in_col[id(o)])               # back into the column vectors
            c_row = np.array([(bU[0] + bU[2]) / 2.0, y0, 0.0])
            shift = c_row - _cen([u_cells[r] for r in u_cells])
            for o in U:
                o.shift(shift)
            bu = _bbox(U)
            _put(V, left=max(bu[2], _bbox(br)[2] if br else bu[2]) + 2.5 * gap, y=_cen(U)[1])
            lbl_u = piece("nameU")
            lbl_v_end = _cen([lbl_v])
            for nm, grp in ((lbl_u, U), (lbl_v, V)):
                b, nb = _bbox(grp), _bbox([nm])
                _put([nm], centre=((b[0] + b[2]) / 2.0, b[3] + 0.35 * e + (nb[3] - nb[1]) / 2.0))
            for r in range(R):
                if r in u_cells and r in tU:
                    moves.append((u_cells[r], "turn", _cen([u_cells[r]]), tU[r]))
                if r in v_cells and r in tV:
                    moves.append((v_cells[r], "lay", _cen([v_cells[r]]), tV[r]))
            moves.append((lbl_v, "move", _cen([lbl_v]), lbl_v_end))
            start_only = U + V + [lbl_u, lbl_v]
            plays_spec = dict(c_row=c_row, u_rest=u_rest, v_rest=v_rest, lbl_u=lbl_u, lbl_ut=lbl_ut, lbl_v=lbl_v, br=br,
                              ell_swap_u=[(u_cells[r], g_cells[r]) for r in range(R) if ell[r] and r in u_cells and r in g_cells],
                              ell_swap_v=[(v_cells[r], g_cells[2 * R + r]) for r in range(R) if ell[r] and r in v_cells and (2 * R + r) in g_cells],
                              dots=dots)
    else:                                                    # komponenten
        _put(U, left=0.0, y=0.0)
        bu = _bbox(U)
        _put(V, left=bu[2] + width(piece("cdot")) + 1.4 * e, y=0.0)   # room for the '·' between the vectors
        bv = _bbox(V)
        lbl_u, lbl_v = piece("nameU"), piece("nameV")
        for nm, b in ((lbl_u, bu), (lbl_v, bv)):
            nb = _bbox([nm])
            if nb is not None:
                _put([nm], centre=((b[0] + b[2]) / 2.0, b[3] + 0.35 * e + (nb[3] - nb[1]) / 2.0))

        def ry(r):
            ys = [_cen([cells[r]])[1] for cells in (u_cells, v_cells) if r in cells]
            return float(np.mean(ys)) if ys else 0.0
        val_m = [(_mt(vals[r], value_color) if (vals[r] and not ell[r]) else None) for r in range(R)]
        eq_x = bv[2] + 1.2 * gap
        val_x = eq_x + width(piece("eq")) + gap
        val_w = max([width(m) for m in val_m if m is not None] or [0.0])
        rows, row_objs = [], []                              # per row: '·', '=', product (or ⋮ in a long vector)
        for r in range(R):
            y = ry(r)
            if ell[r]:
                vd = piece("vdots"); _put([vd], centre=(val_x + val_w / 2.0, y))
                rows.append({"ell": vd}); row_objs.append(vd)
                continue
            d, q = piece("cdot"), piece("eq")
            _put([d], centre=((bu[2] + bv[0]) / 2.0, y))
            _put([q], left=eq_x, y=y)
            row_objs += [d, q]
            if val_m[r] is not None:
                _put([val_m[r]], left=val_x, y=y); row_objs.append(val_m[r])
            rows.append({"r": r, "dot": d, "eq": q, "val": val_m[r]})
            for cells in (u_cells, v_cells):
                if r in cells:
                    b = _bbox([cells[r]])
                    marks.append((r, [b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad]))
        lhs = piece("lhs")
        line = [lhs] + [m for _, _, ms in groups for m in ms]
        top_part = U + V + [lbl_u, lbl_v] + row_objs
        bottom = _bbox(top_part)[1]
        lh = max([float(_bbox([m])[3] - _bbox([m])[1]) for m in line if _bbox([m]) is not None] or [e])
        lay_line(line, 0.0, bottom - 0.9 * e - lh / 2.0)   # the sum below, flush left
        final = top_part + line
        bf = _bbox(final)
        plays_spec = dict(rows=rows, lhs=lhs, lbl=[lbl_u, lbl_v])

    # --- one scale K (like summation_choreo), centred on `position` by the end state; the start must fit too ---
    if font_size and font_size > 0 and em > 0:
        K0 = (float(font_size) / _PX_PER_UNIT) / em
    else:
        K0 = (height / hh) if hh > 1e-9 else 1.0
    avail = float(max_width) if (max_width and max_width > 0) else _FRAME_W * 0.94
    if bf is None:
        return
    cf = np.array([(bf[0] + bf[2]) / 2.0, (bf[1] + bf[3]) / 2.0, 0.0])
    ext = [bf] + ([_bbox(start_only)] if start_only else [])
    half_w = max(max(cf[0] - b[0], b[2] - cf[0]) for b in ext if b is not None)
    half_h = max(max(cf[1] - b[1], b[3] - cf[1]) for b in ext if b is not None)
    K = min(K0, avail / max(1e-9, 2.0 * half_w), FRAME_HEIGHT * 0.94 / max(1e-9, 2.0 * half_h))
    off = np.asarray(position, dtype=float) - K * cf
    every = list({id(o): o for o in final + start_only}.values())
    for o in every:
        o.scale(K, around=np.zeros(3))
        o.shift(off)

    if not animating:                                        # EDIT view / article figure: the end state
        scene.add(*final)
        return

    boxes = {}
    for r, b in marks:                                       # the marks, behind everything else
        x0, y0b, x1, y1b = [K * v for v in b]
        rect = Rectangle(center=np.array([(x0 + x1) / 2.0, (y0b + y1b) / 2.0, 0.0]) + off, height=y1b - y0b, width=x1 - x0)
        rect.color = rect.fill_color = var_color
        rect.fill_opacity, rect.stroke_width = 0.22, 0.0
        scene.add(rect)
        boxes.setdefault(r, []).append(rect)

    plays = []
    prev = []                                                # marks of the previous term (they leave with the next step)

    def mark(r):
        nonlocal prev
        out = [FadeIn(b) for b in boxes.get(r, [])] + [FadeOut(b) for b in prev]
        prev = boxes.get(r, [])
        return out

    if mode == "matrix":
        P = plays_spec
        plays.append([FadeIn(o) for o in U + V + [P["lbl_u"], P["lbl_v"]]])   # both columns
        c = K * P["c_row"] + off                             # the turning point = centre of the row vector
        turn = [Rotate(P["u_rest"], angle=np.pi / 2, around=c)] if P["u_rest"] is not None else []
        turn += [MoveAlongPath(o, _spiral(c, K * s + off, K * t + off)) for o, kind, s, t in moves if kind == "turn"]
        plays.append(turn + [FadeOut(P["lbl_u"]), FadeIn(P["lbl_ut"])])                   # u turns into uᵀ
        plays.append(([FadeOut(P["u_rest"])] if P["u_rest"] is not None else []) + [FadeIn(o) for o in P["br"]]
                     + [a for old, new in P["ell_swap_u"] for a in (FadeOut(old), FadeIn(new))])
        lay = [MoveAlongPath(o, _lay_down(K * s + off, K * t + off)) for o, kind, s, t in moves if kind == "lay"]
        lay += [MoveTo(o, K * t + off) for o, kind, s, t in moves if kind == "move"]
        plays.append(lay + ([FadeOut(P["v_rest"])] if P["v_rest"] is not None else []))   # v laid onto the row
        if P["ell_swap_v"]:
            plays.append([a for old, new in P["ell_swap_v"] for a in (FadeOut(old), FadeIn(new))])
        for t, r, ms in groups:
            if t == "term":
                plays.append(mark(r))                        # the pair (u_j over v_j) is marked
                if r in P["dots"]:
                    plays.append([AppearPulseColor(P["dots"][r], color=flash_color)])   # '·' between them
                plays.append([FadeIn(m) for m in ms])        # '=' / '+' and the product
            else:                                            # '+ ⋯' / '= total'
                plays.append([FadeIn(m) for m in ms] + [FadeOut(b) for b in prev])
                prev = []
    else:
        P = plays_spec
        plays.append([FadeIn(o) for o in U + V + P["lbl"]])
        for rw in P["rows"]:
            if "ell" in rw:
                plays.append([FadeIn(rw["ell"])] + [FadeOut(b) for b in prev]); prev = []
                continue
            plays.append(mark(rw["r"]))                       # the pair is marked
            plays.append([AppearPulseColor(rw["dot"], color=flash_color)])   # '·' between the vectors
            plays.append([FadeIn(rw["eq"])] + ([AppearPulseColor(rw["val"], color=flash_color)] if rw["val"] is not None else []))
        body = [m for t, _, ms in groups if t != "total" for m in ms]
        tail = [m for t, _, ms in groups if t == "total" for m in ms]
        plays.append([FadeIn(P["lhs"])] + [FadeIn(m) for m in body] + [FadeOut(b) for b in prev])
        if tail:
            plays.append([FadeIn(m) for m in tail])

    per = run_time / max(1, len(plays))
    for anims in plays:
        scene.play(*anims, run_time=per)
