"""Animated operation 'directors'. A computation is not just a number - it ANIMATES the process of
the operation. Each director adds the visual pieces to the scene and plays the process, driven by a
ValueTracker (so it scrubs/plays on the timeline). run_time = the animation speed.

v1: convolution (slide g(t-τ) across f, show the overlap product + the result curve being traced).
Summation, Riemann, derivative-as-tangent-slide, etc. follow the same pattern.
"""
import math

import numpy as np

from .AnimObject import AnimObject
from .simpleShape import Dot
from .text import DecimalNumber
from .value_tracker import ValueTracker, always_redraw
from .animation import ChangeValue, FadeIn, FadeOut, Pulse, PulseColor, AppearPulseColor
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
    after the '='); without it one row is shrunk to the frame width."""
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
            lo, hi = 1e-3, K0
            for _ in range(40):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if layout(mid)[1] else (lo, mid)
            K = lo
    else:                                                    # one row, shrunk to the frame width (as before)
        total_w = sum(rawdim[id(it)][0] for it in lines[0])
        ncol = len(lines[0])
        K = K0
        if total_w > 1e-9:
            K = min(K, max(1e-3, (avail - ncol * gap) / total_w))
        if vw > 1e-9:
            K = min(K, max(1e-3, avail / vw))
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
            for key, m in it["forms"]:
                anims = [FadeOut(prev), FadeIn(m)] if prev is not None else [FadeIn(m)]
                if key in ("index", "subst"):                # the pair w_j, x_j lights up while it is put in
                    anims += [PulseColor(q, factor=1.08, color=var_color) for q in pair(it["row"])]
                plays.append(anims)
                prev = m

    per = run_time / max(1, len(plays))
    for anims in plays:
        scene.play(*anims, run_time=per)
