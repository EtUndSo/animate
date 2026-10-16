"""SVG path -> VMobject (Manim's SVGMobject, browser-independent core).

An SVG `<path d="...">` is parsed into our ONE geometry format: cubic Bézier control points
(anchor, handle, handle, anchor, ...). Lines become cubics with collinear handles; quadratic
segments are degree-elevated to cubics. Each sub-path (M ... Z) becomes one leaf VMobject, so a
glyph/symbol made of several contours is a group of leaves - ready for Transform / per-piece
animation. This is the foundation MathTex builds on (LaTeX -> MathJax SVG -> these paths).
"""
import re
import numpy as np

from .AnimObject import AnimObject

# MathJax's getCTM already maps glyphs to upright final coords, so MathTex needs NO extra y-flip
# (1.0). Set to -1.0 only if formulas come out upside-down. (SVGMobject flips separately: raw SVG
# is y-down.)
_TEX_FLIP_Y = 1.0

_NUM = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?')
_CMDS = set("MmLlHhVvCcSsQqTtZz")


def _lex(d):
    """Split a path 'd' string into tokens: command letters and float numbers."""
    out, i, n = [], 0, len(d)
    while i < n:
        ch = d[i]
        if ch in _CMDS:
            out.append(ch); i += 1
        elif ch in ", \t\r\n":
            i += 1
        else:
            m = _NUM.match(d, i)
            if m and m.end() > i:
                out.append(float(m.group())); i = m.end()
            else:
                i += 1
    return out


def _quad_to_cubic(p0, p1, p2):
    """Degree-elevate a quadratic (p0, control p1, p2) to a cubic (two handles)."""
    c1 = p0 + 2.0 / 3.0 * (p1 - p0)
    c2 = p2 + 2.0 / 3.0 * (p1 - p2)
    return c1, c2


def _line_cubic(p0, p1):
    """A straight segment as a cubic (handles at 1/3 and 2/3)."""
    return p0 + (p1 - p0) / 3.0, p0 + (p1 - p0) * 2.0 / 3.0


def path_to_cubics(d):
    """Parse one SVG path string into a list of sub-paths, each an (N,3) cubic Bézier chain
    (N = 3k+1). SVG's y-axis points DOWN; coordinates are returned as-is (y is flipped later, in
    SVGMobject, where the whole picture is oriented and scaled)."""
    toks = _lex(d)
    i, n = 0, len(toks)
    subpaths, pts = [], None
    cur = np.zeros(2); start = np.zeros(2)
    prev_c2 = None; prev_q = None           # for S (smooth cubic) / T (smooth quad) reflection
    cmd = None

    def num():
        nonlocal i
        v = toks[i]; i += 1
        return float(v)

    def finish():
        nonlocal pts
        if pts is not None and len(pts) >= 4:
            subpaths.append(np.array([[p[0], p[1], 0.0] for p in pts]))
        pts = None

    while i < n:
        t = toks[i]
        if isinstance(t, str):
            cmd = t; i += 1
        # else: an implicit repeat of the previous command
        rel = cmd.islower()
        C = cmd.upper()
        if C == "M":
            finish()
            x = num(); y = num(); p = np.array([x, y])
            if rel: p = cur + p
            cur = start = p; pts = [cur.copy()]
            prev_c2 = prev_q = None
            cmd = "l" if rel else "L"       # subsequent coords after M are implicit L
        elif C == "Z":
            if pts is not None:
                h1, h2 = _line_cubic(cur, start); pts += [h1, h2, start.copy()]
                cur = start.copy()
            finish()
            prev_c2 = prev_q = None
        elif C == "L":
            x = num(); y = num(); p = np.array([x, y])
            if rel: p = cur + p
            h1, h2 = _line_cubic(cur, p); pts += [h1, h2, p]; cur = p; prev_c2 = prev_q = None
        elif C == "H":
            x = num(); p = np.array([(cur[0] + x) if rel else x, cur[1]])
            h1, h2 = _line_cubic(cur, p); pts += [h1, h2, p]; cur = p; prev_c2 = prev_q = None
        elif C == "V":
            y = num(); p = np.array([cur[0], (cur[1] + y) if rel else y])
            h1, h2 = _line_cubic(cur, p); pts += [h1, h2, p]; cur = p; prev_c2 = prev_q = None
        elif C == "C":
            c1 = np.array([num(), num()]); c2 = np.array([num(), num()]); p = np.array([num(), num()])
            if rel: c1 = cur + c1; c2 = cur + c2; p = cur + p
            pts += [c1, c2, p]; prev_c2 = c2; cur = p; prev_q = None
        elif C == "S":
            c2r = np.array([num(), num()]); p = np.array([num(), num()])
            if rel: c2r = cur + c2r; p = cur + p
            c1 = (2 * cur - prev_c2) if prev_c2 is not None else cur.copy()
            pts += [c1, c2r, p]; prev_c2 = c2r; cur = p; prev_q = None
        elif C == "Q":
            q = np.array([num(), num()]); p = np.array([num(), num()])
            if rel: q = cur + q; p = cur + p
            c1, c2 = _quad_to_cubic(cur, q, p); pts += [c1, c2, p]; prev_q = q; cur = p; prev_c2 = None
        elif C == "T":
            p = np.array([num(), num()])
            if rel: p = cur + p
            q = (2 * cur - prev_q) if prev_q is not None else cur.copy()
            c1, c2 = _quad_to_cubic(cur, q, p); pts += [c1, c2, p]; prev_q = q; cur = p; prev_c2 = None
        else:
            i += 1                           # unsupported (e.g. arcs) -> skip the token
    finish()
    return subpaths


def _leaf_from_path(d, color, fill_opacity, stroke_width):
    """One `<path>` -> ONE leaf. All its contours are concatenated into `points`, and `_contours`
    records each contour's length, so the painter can fill the whole glyph with the EVEN-ODD rule
    (holes in 6/8/0/… are cut out instead of filled). y is flipped to our (up) convention."""
    chains = []
    for chain in path_to_cubics(d):
        chain[:, 1] *= -1.0
        chains.append(chain)
    if not chains:
        return None
    leaf = AnimObject()
    leaf.points = np.vstack(chains)
    leaf._contours = [len(c) for c in chains]             # contour lengths within points
    leaf.color = color; leaf.fill_color = color
    leaf.fill_opacity = fill_opacity; leaf.stroke_width = stroke_width
    return leaf


class SVGMobject(AnimObject):
    """Import an SVG (its `<path>` outlines) as a VMobject: ONE leaf per `<path>` (contours kept
    together for even-odd fill). y is flipped to our convention (up); scaled to `height`, centred."""

    def __init__(self, svg, height=1.0, color=(0.0, 0.0, 0.0), fill_opacity=1.0, stroke_width=0.0):
        super().__init__()
        ds = re.findall(r'\bd\s*=\s*"([^"]*)"', svg) if ("<" in svg or "d=" in svg) else [svg]
        for d in ds:
            leaf = _leaf_from_path(d, color, fill_opacity, stroke_width)
            if leaf is not None:
                self.add(leaf)
        _fit_height(self, height)


def _fit_height(mobject, height):
    """Scale a mobject to `height` world units and centre it at the origin (shared by SVG / MathTex)."""
    pts = mobject.all_points()
    if len(pts) == 0 or height is None:
        return
    lo, hi = pts.min(axis=0), pts.max(axis=0)
    h = hi[1] - lo[1]
    if h > 1e-9:
        mobject.scale(float(height) / h, around=(lo + hi) / 2.0)
    mobject.move_to(np.zeros(3))


def _affine(chain, m):
    """Apply an SVG 2x3 matrix m=[a,b,c,d,e,f] to an (N,3) chain: (x,y) -> (a x + c y + e, b x + d y + f)."""
    a, b, c, d, e, f = m
    out = chain.copy()
    x, y = chain[:, 0], chain[:, 1]
    out[:, 0] = a * x + c * y + e
    out[:, 1] = b * x + d * y + f
    return out


class MathTex(AnimObject):
    """A LaTeX formula as a VMobject - the Manim MathTex, browser edition. It is built from GLYPH DATA
    produced by MathJax in the browser: a list of {"d": <svg path>, "m": [a,b,c,d,e,f] absolute
    transform, "c": <char, optional>}. Each glyph becomes a SUB-GROUP of path leaves (so a glyph with a
    hole keeps both contours), and glyphs are kept as separate submobjects so they can be matched and
    morphed individually (TransformMatchingTex). y is flipped to our convention and the whole formula is
    scaled to `height` and centred. The editor fills in the glyph data via MathJax (see editor.js)."""

    def __init__(self, glyphs, height=1.0, color=(0.0, 0.0, 0.0), fill_opacity=1.0, position=(0.0, 0.0, 0.0)):
        super().__init__()
        for g in glyphs or []:
            grp = AnimObject()
            grp._tex = g.get("c", "")
            m = g.get("m")
            gc = g.get("col") or color                     # per-glyph colour from MathJax (\color), else default
            chains = []
            for chain in path_to_cubics(g.get("d", "")):
                if m is not None:
                    chain = _affine(chain, m)              # MathJax getCTM already maps to final (upright) coords
                chain[:, 1] *= _TEX_FLIP_Y                 # ... so no extra flip (set -1 only if upside-down)
                chains.append(chain)
            if chains:
                leaf = AnimObject()
                leaf.points = np.vstack(chains)
                leaf._contours = [len(c) for c in chains]  # one glyph = one path, contours -> even-odd fill
                leaf.color = gc; leaf.fill_color = gc
                leaf.fill_opacity = fill_opacity; leaf.stroke_width = 0.0
                grp.add(leaf)
                self.add(grp)
        _fit_height(self, height)
        if position is not None:
            self.move_to(np.asarray(position, dtype=float))
