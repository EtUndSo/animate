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
from .animation import ChangeValue
from .bezier import line_points, partial_bezier
from .calc import make_convolution
from .svg import MathTex
from .constants import BLUE, GREEN, UP


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
