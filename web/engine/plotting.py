"""GeoGebra-grade function plotting: combined (uniform + adaptive) sampling.

Based on T. Bayer, "Efficient plotting the functions with discontinuities based on combined sampling"
(Geoinformatics FCE CTU, 2018) - the same family GeoGebra's CurvePlotter uses. Key ideas:

  * ADAPTIVE angle criterion: refine a pair of segments while their bend angle exceeds ~5 deg
    (dense in high curvature, sparse on straight parts -> smooth with few points).
  * UNIFORM seed phase (recurse unconditionally while depth <= d_min) so fast oscillations are not
    skipped the way pure endpoint-recursion would skip them.
  * RANDOMISED split points r in [0.45, 0.55]: the crucial trick - it stops periodic functions
    (e.g. sin(1000 x)) from aliasing into a clean but WRONG slow wave at a regular grid.
  * DISCONTINUITY breaks: at NaN / inf / poles the curve is split into separate pieces, never a
    vertical line drawn across an asymptote (e.g. tan).

Output: a list of point-arrays (cubic Bézier chains), one per continuous piece.
"""
import math
import random
import numpy as np
from .bezier import line_points
from .constants import FRAME_HEIGHT, PIXEL_HEIGHT

_UNITS_PER_PIXEL = FRAME_HEIGHT / PIXEL_HEIGHT
_V_CUTOFF = 3.0 * FRAME_HEIGHT       # world |vertical| beyond this = off-screen -> pole/discontinuity


def _angle(pa, pb, pc):
    """Bend angle (radians) at pb between segments pa->pb and pb->pc. 0 = straight."""
    v1 = pb - pa
    v2 = pc - pb
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    if n1 < 1e-12 or n2 < 1e-12:
        return 0.0
    c = float(np.dot(v1, v2) / (n1 * n2))
    return math.acos(max(-1.0, min(1.0, c)))


def plot_graph(value_at, x0, x1, to_world, world_width,
               angle_deg=5.0, d_min=3, d_max=18, max_points=8000):
    """Adaptively sample y=value_at(x) over [x0,x1]. Returns a list of Bézier point-arrays
    (one per continuous piece). to_world(x,y)->world point; world_width = on-screen width."""
    thr = math.radians(angle_deg)
    min_dx = (x1 - x0) / 4000.0                        # resolution floor (~ sub-pixel)
    # Deterministic jitter: seed from the x-range so the SAME range always samples at the same
    # (irregular) positions. Keeps the anti-aliasing benefit but makes plots reproducible and
    # stable across re-renders / animation frames (no shimmer), independent of the function.
    rng = random.Random(repr((round(x0, 9), round(x1, 9))))

    def P(x):
        """World point for x, or None at a discontinuity: non-finite, or far off-screen (a pole:
        numpy's tan gives huge FINITE values at asymptotes, so we judge by on-screen position)."""
        try:
            y = float(value_at(x))
        except Exception:
            return None
        if not math.isfinite(y):
            return None
        w = np.asarray(to_world(x, y), dtype=float)
        return None if abs(w[1]) > _V_CUTOFF else w

    def bend(A, B, C):                                 # True -> refine (discontinuity or too bent)
        if A is None or B is None or C is None:
            return True
        return _angle(A, B, C) > thr

    out = [(x0, P(x0))]                                # ordered (x, worldpoint|None)

    def rec(a, Pa, b, Pb, depth):
        if depth > d_max or (b - a) < min_dx or len(out) >= max_points:
            return
        r1 = 0.45 + 0.1 * rng.random()
        r2 = 0.45 + 0.1 * rng.random()
        r3 = 0.45 + 0.1 * rng.random()
        xa1 = a + 0.5 * r1 * (b - a)                   # ~1/4, 1/2, 3/4, randomly jittered so periodic
        xa2 = a + r2 * (b - a)                         # functions are not skipped at a regular grid
        xa3 = a + 1.5 * r3 * (b - a)
        P1, P2, P3 = P(xa1), P(xa2), P(xa3)
        force = depth <= d_min                         # uniform seed phase: guaranteed base density
        a1, a2, a3 = bend(Pa, P1, P2), bend(P1, P2, P3), bend(P2, P3, Pb)
        if force or a1:
            rec(a, Pa, xa1, P1, depth + 1)
        out.append((xa1, P1))
        if force or a1 or a2:
            rec(xa1, P1, xa2, P2, depth + 1)
        out.append((xa2, P2))
        if force or a2 or a3:
            rec(xa2, P2, xa3, P3, depth + 1)
        out.append((xa3, P3))
        if force or a3:
            rec(xa3, P3, b, Pb, depth + 1)

    rec(x0, out[0][1], x1, P(x1), 1)
    out.append((x1, P(x1)))

    # split into continuous runs at discontinuities, build a Bézier chain per run (thinned: see _thin)
    segments, run = [], []
    for _x, w in out:
        if w is None:
            if len(run) >= 2:
                segments.append(line_points(_thin(run)))
            run = []
        else:
            run.append(w)
    if len(run) >= 2:
        segments.append(line_points(_thin(run)))
    return segments


def plot_graph_fixed(value_at, x0, x1, to_world, n):
    """y = value_at(x) at exactly n evenly spaced x (no adaptivity, no jitter, no thinning): a graph that is redrawn
    every frame under a scene parameter (L3). The same parameter-free shape always has the same number of points, so
    the animated export stores the frames as moving numbers (track "q") instead of a new path per frame. The samples
    are joined by a Catmull-Rom spline (smooth cubic Bézier through them): 8-12 samples per wiggle look round.
    Non-finite values and points far off screen (poles) split the curve, as in plot_graph."""
    n = max(2, int(n))
    xs = np.linspace(float(x0), float(x1), n)
    with np.errstate(all="ignore"):                        # sqrt(x - a) left of a, 1/(x - a) at a: just gaps
        try:                                               # vectorised when the expression allows it
            ys = np.asarray(value_at(xs), dtype=float)
            if ys.shape != xs.shape:
                raise ValueError
        except Exception:
            ys = np.empty(n)
            for k, x in enumerate(xs):
                try:
                    ys[k] = float(value_at(float(x)))
                except Exception:
                    ys[k] = float("nan")
    segments, run = [], []
    for x, y in zip(xs, ys):
        w = None
        if math.isfinite(y):
            w = np.asarray(to_world(float(x), float(y)), dtype=float)
            if abs(w[1]) > _V_CUTOFF:
                w = None
        if w is None:
            if len(run) >= 2:
                segments.append(smooth_points(run))
            run = []
        else:
            run.append(w)
    if len(run) >= 2:
        segments.append(smooth_points(run))
    return segments


def smooth_points(anchors):
    """Cubic Bézier chain through the anchors with Catmull-Rom handles (tangent at P_i parallel to P_{i+1} - P_{i-1},
    one sided at the ends). Exact for straight runs, C1-smooth elsewhere."""
    P = np.asarray(anchors, dtype=float)
    if len(P) < 3:
        return line_points(P)
    T = np.empty_like(P)
    T[1:-1] = (P[2:] - P[:-2]) / 2.0
    T[0] = P[1] - P[0]
    T[-1] = P[-1] - P[-2]
    out = np.empty((3 * (len(P) - 1) + 1, P.shape[1]))
    out[0::3] = P
    out[1::3] = P[:-1] + T[:-1] / 3.0
    out[2::3] = P[1:] - T[1:] / 3.0
    return out


THIN_PX = 0.2                        # a sample closer than this (screen px) to the line through its neighbours goes
THIN_MIN = 17                        # ...but every curve keeps at least this many evenly spread samples (Create from the
#                                      centre needs an anchor near x = 0; MoveAlongPath and tests read the anchors)


def _thin(run, eps=THIN_PX * _UNITS_PER_PIXEL):
    """Ramer-Douglas-Peucker on one continuous run: drop the samples the polyline does not need (deviation below eps,
    0.2 px). The adaptive sampler puts thousands of samples on a curve (up to max_points per curve, i.e. three times
    as many Bézier points); after thinning a smooth curve keeps a few hundred, the drawing is the same within 0.2 px
    and the article SVG and its animation stay small."""
    P = np.asarray(run, dtype=float)
    n = len(P)
    if n <= 2:
        return run
    keep = np.zeros(n, dtype=bool)
    keep[0] = keep[-1] = True
    keep[np.linspace(0, n - 1, min(n, THIN_MIN)).round().astype(int)] = True   # a straight piece keeps a few anchors
    stack = [(0, n - 1)]
    while stack:
        i, j = stack.pop()
        if j <= i + 1:
            continue
        a, b = P[i], P[j]
        ab = b - a
        L2 = float(ab @ ab)
        seg = P[i + 1:j] - a
        if L2 < 1e-24:
            d = np.sqrt((seg ** 2).sum(axis=1))
        else:
            t = np.clip(seg @ ab / L2, 0.0, 1.0)
            d = np.sqrt(((seg - t[:, None] * ab) ** 2).sum(axis=1))
        k = int(np.argmax(d))
        if d[k] > eps:
            m = i + 1 + k
            keep[m] = True
            stack += [(i, m), (m, j)]
    return [p for p, k in zip(run, keep) if k]


def build_graph(segments, color):
    """Turn plot_graph's segments into one AnimObject: a single open curve when continuous, or a
    group of pieces when the function has discontinuities (so Create still works in the common case).
    The pieces are flagged `_graph_piece`: they carry no style of their own but mirror the graph's
    (see sync_pieces), so a split graph looks exactly like an unsplit one."""
    from .AnimObject import AnimObject
    obj = AnimObject()
    obj.color = color
    if len(segments) == 1:
        obj.points = segments[0]
    else:
        for seg in segments:
            child = AnimObject()
            child.points = seg
            child.color = color
            child._graph_piece = True
            obj.add(child)
    return obj


_PIECE_STYLE = ("color", "stroke_width", "stroke_opacity", "fill_color", "fill_opacity", "dash")


def sync_pieces(graph):
    """Copy the graph's stroke/fill style onto its pieces (Fehler F1). Whoever styles a graph after
    build_graph (scene_model, operations, processes) calls this, otherwise the pieces of a split curve keep
    the default blue 4 px. Only the `_graph_piece` children are touched, never result children."""
    for sub in graph.subObjects:
        if getattr(sub, "_graph_piece", False):
            for attr in _PIECE_STYLE:
                setattr(sub, attr, getattr(graph, attr))
    return graph
