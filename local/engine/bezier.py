import numpy as np

# Point format of a Bézier curve:  anchor, handle, handle, anchor, handle, handle, anchor, ...
# For k cubic segments that is  N = 3*k + 1  points. The anchors (index 0, 3, 6, ...) lie ON
# the curve; the two points in between are the control points ("handles") that pull the curve
# into shape.


def line_points(anchors):
    """Build a cubic Bézier chain with STRAIGHT segments through the given anchor points
    (the two handles sit at 1/3 and 2/3 of each segment). Every straight-edged shape
    (line, polygon, rectangle, ...) is expressed this way, so the renderer only ever deals
    with ONE format: cubic Bézier control points."""
    anchors = np.asarray(anchors, dtype=float)
    if len(anchors) < 2:
        return anchors.reshape(-1, 3)
    points = [anchors[0]]
    for i in range(len(anchors) - 1):
        a, b = anchors[i], anchors[i + 1]
        points.append(a + (b - a) / 3)         # first handle
        points.append(a + (b - a) * 2 / 3)     # second handle
        points.append(b)                       # next anchor
    return np.array(points)


def circle_points(center, radius, u, v, n_arcs=4):
    """Circle as n_arcs cubic Bézier arcs.

    The circle lies in the plane spanned by the unit vectors u ("right") and v ("up"),
    so it automatically follows your coordinate convention (RIGHT / UP).

    n_arcs=4 (four quarter circles) already gives a visually perfect circle.
    """
    center = np.asarray(center, dtype=float)
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    d = 2 * np.pi / n_arcs            # angle spanned by one arc
    k = (4 / 3) * np.tan(d / 4)       # handle length - standard formula for circular arcs

    def anchor(a):   return center + radius * (np.cos(a) * u + np.sin(a) * v)
    def tangent(a):  return radius * (-np.sin(a) * u + np.cos(a) * v)  # direction along the circle

    angles = np.linspace(0, 2 * np.pi, n_arcs + 1)
    points = [anchor(angles[0])]
    for i in range(n_arcs):
        a0, a1 = angles[i], angles[i + 1]
        points.append(anchor(a0) + k * tangent(a0))   # handle after the start anchor
        points.append(anchor(a1) - k * tangent(a1))   # handle before the end anchor
        points.append(anchor(a1))                     # next anchor
    return np.array(points)


def split_cubic(p0, p1, p2, p3, t):
    """Split one cubic segment at parameter t (de Casteljau) -> (first_half, second_half).
    Each half is again a full cubic (4 control points)."""
    p0, p1, p2, p3 = (np.asarray(p, dtype=float) for p in (p0, p1, p2, p3))
    a = p0 + (p1 - p0) * t
    b = p1 + (p2 - p1) * t
    c = p2 + (p3 - p2) * t
    d = a + (b - a) * t
    e = b + (c - b) * t
    f = d + (e - d) * t                               # the point on the curve at t
    return (p0, a, d, f), (f, e, c, p3)


def partial_bezier(points, a):
    """Return the first fraction 'a' (0..1) of a cubic Bézier chain: the curve drawn from its
    start up to progress a. The last, partial segment is cut exactly with de Casteljau.
    Used by the Create animation to reveal a curve gradually."""
    points = np.asarray(points, dtype=float)
    k = (len(points) - 1) // 3                        # number of segments
    if k <= 0 or a >= 1.0:
        return points.copy()
    a = max(a, 0.0)
    t = a * k
    full = int(t)                                     # complete segments to keep
    rem = t - full                                    # fraction of the next segment
    kept = points[:3 * full + 1].copy()               # complete part (ends on an anchor)
    if rem > 0 and full < k:
        p0, p1, p2, p3 = points[3 * full:3 * full + 4]
        (q0, q1, q2, q3), _ = split_cubic(p0, p1, p2, p3, rem)
        kept = np.vstack([kept, [q1, q2, q3]])
    return kept
