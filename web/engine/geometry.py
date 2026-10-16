"""Geometry interaction: boolean regions of shapes (the computation layer for 2D).

v1: INTERSECTION of two shapes via the Sutherland-Hodgman algorithm, which is exact when the clip
polygon is convex - true for all our basic shapes (circle, rectangle, square, triangle, regular
polygon). Area via the shoelace formula. Union / difference (non-convex results) need the general
Greiner-Hormann algorithm and come next.
"""
import numpy as np


def _cubic(p0, p1, p2, p3, t):
    mt = 1.0 - t
    return mt ** 3 * p0 + 3 * mt ** 2 * t * p1 + 3 * mt * t ** 2 * p2 + t ** 3 * p3


def outline_polygon(obj, per_seg=12):
    """Sample a shape's closed Bézier outline into a dense (x, y) polygon (points ON the curve)."""
    pts = np.asarray(obj.points, dtype=float)
    k = (len(pts) - 1) // 3
    poly = []
    for i in range(k):
        p0, p1, p2, p3 = pts[3 * i:3 * i + 4]
        for s in range(per_seg):
            P = _cubic(p0, p1, p2, p3, s / per_seg)
            poly.append((float(P[0]), float(P[1])))
    return poly


def signed_area(poly):
    x = np.array([p[0] for p in poly])
    y = np.array([p[1] for p in poly])
    return 0.5 * float(np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y))


def area(poly):
    return abs(signed_area(poly))


def _ccw(poly):
    return poly if signed_area(poly) >= 0 else poly[::-1]


def _inside(p, a, b):
    """Is p on the interior (left) side of the directed edge a->b (clip must be CCW)?"""
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= -1e-12


def _line_cross(s, e, a, b):
    """Intersection of segment s->e with the infinite line through a, b."""
    x1, y1 = s; x2, y2 = e; x3, y3 = a; x4, y4 = b
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-15:
        return e
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def intersect_region(subject, clip):
    """Sutherland-Hodgman: clip the subject polygon against the CONVEX clip polygon. Returns the
    intersection polygon (list of (x,y)), empty if they do not overlap."""
    clip = _ccw(list(clip))
    out = list(subject)
    for i in range(len(clip)):
        A, B = clip[i], clip[(i + 1) % len(clip)]
        inp, out = out, []
        if not inp:
            break
        S = inp[-1]
        for E in inp:
            if _inside(E, A, B):
                if not _inside(S, A, B):
                    out.append(_line_cross(S, E, A, B))
                out.append(E)
            elif _inside(S, A, B):
                out.append(_line_cross(S, E, A, B))
            S = E
    return out


def intersection(objA, objB, per_seg=12):
    """Intersection region (list of (x,y)) and its area for two shapes."""
    region = intersect_region(outline_polygon(objA, per_seg), outline_polygon(objB, per_seg))
    return region, (area(region) if len(region) >= 3 else 0.0)
