"""Animated operation 'directors'. A computation is not just a number - it ANIMATES the process of
the operation. Each director adds the visual pieces to the scene and plays the process, driven by a
ValueTracker (so it scrubs/plays on the timeline). run_time = the animation speed.

v1: convolution (slide g(t-τ) across f, show the overlap product + the result curve being traced).
Summation, Riemann, derivative-as-tangent-slide, etc. follow the same pattern.
"""
import numpy as np

from .AnimObject import AnimObject
from .simpleShape import Dot
from .text import DecimalNumber
from .value_tracker import ValueTracker, always_redraw
from .animation import ChangeValue, FadeIn, FadeOut, Pulse, PulseColor, AppearPulseColor
from .bezier import line_points, partial_bezier
from .calc import make_convolution
from .svg import MathTex
from .constants import BLUE, GREEN, UP, FRAME_HEIGHT, PIXEL_WIDTH, PIXEL_HEIGHT

_FRAME_W = FRAME_HEIGHT * PIXEL_WIDTH / PIXEL_HEIGHT     # world width of the frame


def _styled(graph, color, stroke_width=4, fill=0.0):
    graph.color = color
    graph.stroke_width = stroke_width
    if fill:
        graph.fill_opacity = fill
    return graph


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


def _color_head_bounds(head, bound_color, var_color, color):
    """Tint the Σ/∏ BOUNDS (lower 'i=a', upper 'n'/number) with bound_color. The bounds sit stacked
    OVER/UNDER the big operator (x-centre within the operator's column); the summand sits to its RIGHT.
    So: biggest glyph = the operator; any other glyph whose x-centre is left of the operator's right
    edge is a bound -> running variable 'i' keeps var_color, '='/'-' stay `color` (black), the rest
    (the actual limit numbers/letters) become bound_color. Robust even for fraction summands."""
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
    sx1 = float(sp[:, 0].max())
    for j, s in enumerate(subs):
        if j == si:
            continue
        p = pts(s)
        if p is None:
            continue
        if float(p[:, 0].mean()) <= sx1:                     # stacked on the operator -> a bound
            tex = getattr(s, "_tex", "")
            col = var_color if tex == "i" else (color if tex in ("=", "-", "−") else bound_color)
            stack = [s]
            while stack:
                o = stack.pop()
                if len(o.points):
                    o.color = col
                    o.fill_color = col
                stack.extend(o.subObjects)


def summation_choreo(scene, choreo, run_time=6.0, color=(0.0, 0.0, 0.0), value_color=(0.17, 0.63, 0.17),
                     var_color=(1.0, 0.50, 0.05), end_color=(0.58, 0.40, 0.74),
                     flash_color=(0.40, 0.70, 1.0), bound_color=(0.09, 0.75, 0.81),
                     animating=False, position=(-6.2, 2.4, 0.0), height=0.9):
    """Step-by-step Σ (number mode): the Σ expression appears, then for each term the ABSTRACT summand
    appears, its i is SUBSTITUTED (crossfade), then it is COMPUTED to a value (crossfade); a '+' fades
    in with a short Σ pulse (the '+' springs from the sum). All via FadeIn/FadeOut/Pulse (contract-safe,
    scrubbable). `choreo` = {head: glyphs, cols: [ {t:'op'|'plus'|'ell'|'total', g} |
    {t:'term', abstract, subst, value|null} ]}. Layout is left-to-right by measured width."""
    gap = 0.14
    y = float(position[1])

    def raw(glyphs, col, var_i=False):
        # var_i: tint the running-variable glyph 'i' with var_color (per-glyph col; the rest stay `col`).
        gl = glyphs or []
        if var_i and var_color is not None:
            gl = [dict(g, col=var_color) if g.get("c") == "i" else g for g in gl]
        return MathTex(gl, scale=1.0, color=col)             # RAW MathJax units (no per-piece height fit)

    def dims(mt):
        p = mt.all_points()
        return (float(np.ptp(p[:, 0])), float(np.ptp(p[:, 1]))) if len(p) else (0.0, 0.0)

    # --- build every piece at raw scale, so we can pick ONE shared scale (consistent sizes) ---
    head = raw(choreo.get("head", []), color, var_i=True)    # i under the Σ is the running variable
    _color_head_bounds(head, bound_color, var_color, color)  # lower/upper limits -> bound_color
    hw, hh = dims(head)
    built = []                                             # per column: {t, forms:[(mt, is_value)], w}
    for col in choreo.get("cols", []):
        t = col.get("t")
        if t == "term":
            forms = []
            for key in ("abstract", "subst", "value"):
                if col.get(key):
                    is_val = (key == "value")               # abstract still contains i -> tint it var_color
                    forms.append((raw(col[key], value_color if is_val else color, var_i=(key == "abstract")), is_val))
            w = max((dims(m)[0] for m, _ in forms), default=0.0)
            built.append({"t": "term", "forms": forms, "w": w})
        else:
            m = raw(col.get("g", []), end_color if t == "total" else color)   # the total is the end result
            built.append({"t": t, "forms": [(m, False)], "w": dims(m)[0]})

    # --- one shared scale K: tall enough (head = `height`) but small enough to FIT the frame width ---
    total_w = hw + sum(b["w"] for b in built)
    ncol = 1 + len(built)
    avail = _FRAME_W * 0.94
    K = (height / hh) if hh > 1e-9 else 1.0
    if total_w > 1e-9:
        K = min(K, max(1e-3, (avail - ncol * gap) / total_w))
    for mt in [head] + [m for b in built for (m, _) in b["forms"]]:
        mt.scale(K, around=np.zeros(3))

    # --- layout left-to-right, centred on position x ---
    def W(mt):
        return dims(mt)[0]
    widths = [W(head)] + [max((W(m) for m, _ in b["forms"]), default=0.0) for b in built]
    total = sum(widths) + ncol * gap
    x = [float(position[0]) - total / 2.0]

    def place(mt, slotw):
        mt.move_to(np.array([x[0] + slotw / 2.0, y, 0.0]))

    place(head, widths[0]); x[0] += widths[0] + gap

    if not animating:                                       # EDIT view: final forms, static
        scene.add(head)
        for b, sw in zip(built, widths[1:]):
            if b["t"] == "term":
                m = (b["forms"][-1][0] if b["forms"] else None)   # the computed value (or last available)
            else:
                m = b["forms"][0][0]
            if m is not None:
                place(m, sw); scene.add(m)
            x[0] += sw + gap
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

    plays = [[FadeIn(head)]]                                 # 1) the Σ expression appears
    for b, sw in zip(built, widths[1:]):
        if b["t"] in ("op", "plus", "ell", "total"):
            m = b["forms"][0][0]; place(m, sw)
            if b["t"] == "plus":
                # the '+' springs in (grows + flashes flash_color) AND the big Σ pulses the same colour
                sig = PulseColor(sigma, color=flash_color) if sigma is not None else Pulse(head)
                plays.append([AppearPulseColor(m, color=flash_color), sig])
            else:
                plays.append([FadeIn(m)])
        else:                                                # term: abstract -> substitute -> compute
            for m, _ in b["forms"]:
                place(m, sw)
            prev = None
            for m, _ in b["forms"]:
                plays.append([FadeOut(prev), FadeIn(m)] if prev is not None else [FadeIn(m)])
                prev = m
        x[0] += sw + gap

    per = run_time / max(1, len(plays))
    for anims in plays:
        scene.play(*anims, run_time=per)
