"""Circuit symbols (DIN / ET-script style, like circuitikz "european"): two-terminal components
between two points, multi-terminal devices at a centre with rotation, wires with junction dots and
named nodes. Everything is built in WORLD coordinates from data-coordinate endpoints, so symbol
sizes stay the same on any axes. Labels accept the formula shorthand (R_1, U_{BE}, 1\\,k\\Omega).

Pin positions of Device (size 1, rotation 0, no flip; multiply by `size`, then rotate about `center`):
    npn, pnp               B (-1, 0)   C (0.5, 1)   E (0.5, -1)
    nmos, pmos, *_dig, jfet_n
                           G (-1, 0)   D (0.5, 1)   S (0.5, -1)       (+ B (1, 0) for nmos4/pmos4/nmos_dep)
    opamp                  - (-1.5, 0.5)   + (-1.5, -0.5)   out (1.5, 0)
    amp, filter_*, adc     in (-1.5, 0)    out (1.5, 0)
    mixer, sum, oscillator in (-1, 0) / out (1, 0), mixer/sum also (0, -1)
    twoport                1 (-1.5, 0.5)   1' (-1.5, -0.5)   2 (1.5, 0.5)   2' (1.5, -0.5)
    vtube (triode)         A (0, 1.5)   G (-1.5, 0)   K (0, -1.5)
    ground, terminal, node, antenna   (0, 0)
"""
import math

import numpy as np

from .AnimObject import AnimObject
from .simpleShape import Line, Polygon, Circle, Dot, ArrowHead
from .bezier import line_points
from .text import Text
from .figures import c2p_fn, xyz, pairs, UPP


def _line(a, b, col, sw):
    ln = Line(a, b); ln.color = col; ln.stroke_width = sw
    return ln


def _poly(pts, col, sw, fill=None, closed=True):
    p = Polygon(pts, closed=closed); p.color = col; p.stroke_width = sw
    if fill is not None:
        p.fill_color = fill; p.fill_opacity = 1.0
    return p


def _polyline(pts, col, sw):
    o = AnimObject(); o.points = line_points([np.asarray(p, dtype=float) for p in pts]); o.color = col; o.stroke_width = sw
    return o


def _circle(c, r, col, sw, fill=None):
    ci = Circle(center=c, radius=r); ci.color = col; ci.stroke_width = sw
    if fill is not None:
        ci.fill_color = fill; ci.fill_opacity = 1.0
    return ci


def _dot(c, r, col):
    d = Dot(center=c, radius=r); d.color = col; d.fill_color = col; d.fill_opacity = 1.0; d.stroke_width = 0.0
    d._no_dash = True
    return d


def _head(tip, direction, col, size):
    h = ArrowHead(tip, direction, size=size); h.color = col; h.fill_color = col
    return h


def _align_for(dx):
    return "left" if dx > 0.3 else ("right" if dx < -0.3 else "center")


# ---------------------------------------------------------------------------------------------
# Placement like KiCad / LTspice: a symbol of FIXED size sits at `center`, turned by `rotation` (degrees,
# usually 0/90/180/270); its two pins are `length` apart (default STD_LENGTH = 4 grid steps of GRID, so
# with the centre on the grid both pins land on the grid too). Older scenes give the pins directly as
# start/end; that still works (center wins if both are present).
GRID = 0.5
STD_LENGTH = 2.0
_EXACT_DIRS = {0: (1.0, 0.0), 90: (0.0, 1.0), 180: (-1.0, 0.0), 270: (0.0, -1.0)}


def _direction(deg):
    """Unit vector for `deg`; exact for multiples of 90 (no 6e-17 offsets that knock pins off the grid)."""
    d = float(deg) % 360.0
    k = int(round(d))
    if abs(d - k) < 1e-9 and k % 90 == 0:
        return _EXACT_DIRS[k % 360]
    r = math.radians(d)
    return math.cos(r), math.sin(r)


def symbol_style(args):
    """'iec' (European, DIN/IEC 60617: box resistor, filled-bar inductor) or 'ansi' (American, IEEE 315:
    zigzag resistor, humped inductor, +/- sources). Per element; European is the default."""
    s = str(args.get("symbol_style", "europäisch")).strip().lower()
    return "ansi" if s in ("ansi", "us", "american", "amerikanisch") else "iec"


def component_ends(args):
    """The two pins of a component in DATA coordinates (start = pin 1, end = pin 2)."""
    if "center" in args or "start" not in args or "end" not in args:
        cx, cy, cz = xyz(args.get("center", [0.0, 0.0, 0.0]))
        h = 0.5 * float(args.get("length", STD_LENGTH))
        ux, uy = _direction(args.get("rotation", 0.0))
        return (cx - h * ux, cy - h * uy, cz), (cx + h * ux, cy + h * uy, cz)
    return xyz(args["start"]), xyz(args["end"])


# Two-terminal components. Local frame: u = unit vector pin 1 -> pin 2, v = u rotated by +90 deg.
# `body` = length of the symbol along u (the leads fill the rest of the span); the body HEIGHT is 0.4*size
# for all box-like symbols, so resistor/fuse/inductor have the IEC proportion 3 : 1.
_BODY = {"resistor": 1.2, "resistor_nl": 1.2, "resistor_var": 1.2, "capacitor": 0.24, "capacitor_var": 0.24,
         "inductor": 1.2, "diode": 0.55, "zener": 0.55, "led": 0.55, "vsource": 0.8, "vsource_dc": 0.3,
         "isource": 0.8, "ac_source": 0.8, "vcvs": 1.0, "vccs": 1.0, "cccs": 1.0, "ccvs": 1.0, "switch": 1.0,
         "lamp": 0.8, "ammeter": 0.8, "voltmeter": 0.8, "fuse": 1.2, "wire": 0.0, "nullator": 0.9, "norator": 1.0}
COMPONENT_KINDS = list(_BODY)


def _zigzag(P0, P1, u, v, h, col, sw, zigs=3):
    """ANSI resistor: `zigs` full periods (2*zigs peaks) of amplitude h between P0 and P1."""
    n = 2 * zigs
    body = float(np.linalg.norm(P1 - P0))
    pts = [P0] + [P0 + ((k + 0.5) / n) * body * u + (h if k % 2 == 0 else -h) * v for k in range(n)] + [P1]
    return _polyline(pts, col, sw)


def _plus_minus(M, r, u, col, sw):
    """'+' near pin 2, '-' near pin 1, always drawn upright (horizontal dash, upright cross)."""
    ex, ey = np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0])
    p, m, s = M + 0.45 * r * u, M - 0.45 * r * u, 0.18 * r
    return [_line(p - s * ex, p + s * ex, col, 0.8 * sw), _line(p - s * ey, p + s * ey, col, 0.8 * sw),
            _line(m - s * ex, m + s * ex, col, 0.8 * sw)]


def build_component(args, style, axes):
    c2p = c2p_fn(axes)
    kind = str(args.get("kind", "resistor"))
    ansi = symbol_style(args) == "ansi"
    pa, pb = component_ends(args)
    A, B = c2p(*pa), c2p(*pb)
    S = float(args.get("size", 1.0))
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 3.0))
    fs = float(args.get("font_size", 26))
    obj = AnimObject()
    obj.color = col
    d = B - A
    L = float(np.linalg.norm(d))
    if L < 1e-9:
        return obj
    u = d / L
    v = np.array([-u[1], u[0], 0.0])
    M = 0.5 * (A + B)
    body = min(_BODY.get(kind, 1.0) * S, L)
    P0, P1 = M - 0.5 * body * u, M + 0.5 * body * u      # body ends
    if body < L - 1e-9:                                  # leads
        obj.add(_line(A, P0, col, sw)); obj.add(_line(P1, B, col, sw))
    elif kind == "wire":
        obj.add(_line(A, B, col, sw))
    w = 0.4 * S                                          # body height scale
    if kind in ("resistor", "resistor_nl", "resistor_var", "fuse"):
        if ansi and kind == "fuse":                      # ANSI fuse: one S-shaped period along the lead axis
            ts = np.linspace(0.0, 2.0 * np.pi, 32)
            obj.add(_polyline([P0 + (t / (2.0 * np.pi)) * body * u + 0.5 * w * np.sin(t) * v for t in ts], col, sw))
        elif ansi:                                       # ANSI resistor: zigzag, 3 periods
            obj.add(_zigzag(P0, P1, u, v, 0.5 * w, col, sw))
        else:                                            # IEC: box 3 : 1
            obj.add(_poly([P0 - 0.5 * w * v, P1 - 0.5 * w * v, P1 + 0.5 * w * v, P0 + 0.5 * w * v], col, sw))
            if kind == "fuse":
                obj.add(_line(P0, P1, col, sw))
        if kind == "resistor_nl":                        # kinked characteristic line through the box
            obj.add(_polyline([P0 - 0.15 * body * u - 0.75 * w * v, M - 0.12 * body * u - 0.75 * w * v,
                               M + 0.25 * body * u + 0.75 * w * v], col, 0.8 * sw))
        if kind == "resistor_var":                       # adjustable: diagonal arrow through the box
            tip = M + 0.45 * body * u + 1.0 * w * v
            obj.add(_line(M - 0.45 * body * u - 1.0 * w * v, tip, col, 0.8 * sw))
            obj.add(_head(tip, tip - (M - 0.45 * body * u - 1.0 * w * v), col, 0.22 * S))
    elif kind in ("capacitor", "capacitor_var"):
        for P in (P0, P1):
            obj.add(_line(P - 0.9 * w * v, P + 0.9 * w * v, col, 1.5 * sw))
        if kind == "capacitor_var":
            a, tip = M - 0.45 * S * u - 1.2 * w * v, M + 0.45 * S * u + 1.2 * w * v
            obj.add(_line(a, tip, col, 0.8 * sw))
            obj.add(_head(tip, tip - a, col, 0.22 * S))
    elif kind == "inductor" and not ansi:                # IEC/DIN: filled bar, same size as the resistor box
        obj.add(_poly([P0 - 0.5 * w * v, P1 - 0.5 * w * v, P1 + 0.5 * w * v, P0 + 0.5 * w * v], col, sw, fill=col))
    elif kind == "inductor":                             # ANSI: four half-circle humps on the +v side
        n = 4
        seg = body / n
        for k in range(n):
            c = P0 + (k + 0.5) * seg * u
            ts = np.linspace(np.pi, 0.0, 16)
            obj.add(_polyline([c + (seg / 2) * (np.cos(t) * u + np.sin(t) * v) for t in ts], col, sw))
    elif kind in ("diode", "zener", "led"):
        obj.add(_poly([P0 - 0.5 * w * v, P0 + 0.5 * w * v, P1], col, sw, fill=col))
        obj.add(_line(P1 - 0.5 * w * v, P1 + 0.5 * w * v, col, 1.3 * sw))
        if kind == "zener":
            obj.add(_line(P1 + 0.5 * w * v, P1 + 0.5 * w * v - 0.15 * S * u, col, 1.3 * sw))
            obj.add(_line(P1 - 0.5 * w * v, P1 - 0.5 * w * v + 0.15 * S * u, col, 1.3 * sw))
        if kind == "led":
            for k in (0.0, 0.25):
                a = M + (k - 0.15) * S * u + 0.6 * w * v
                b = a + 0.32 * S * (0.6 * u + 0.8 * v)
                obj.add(_line(a, b, col, 0.7 * sw)); obj.add(_head(b, b - a, col, 0.14 * S))
    elif kind in ("vsource", "isource", "ac_source", "lamp", "ammeter", "voltmeter"):
        r = 0.5 * body
        obj.add(_circle(M, r, col, sw))
        if kind == "vsource" and ansi:                   # ANSI: + towards pin 2, - towards pin 1
            for part in _plus_minus(M, r, u, col, sw):
                obj.add(part)
        elif kind == "vsource":                          # DIN/IEC: line along the connection
            obj.add(_line(M - r * u, M + r * u, col, sw))
        elif kind == "isource" and ansi:                 # ANSI: arrow towards pin 2
            obj.add(_line(M - 0.6 * r * u, M + 0.3 * r * u, col, sw)); obj.add(_head(M + 0.65 * r * u, u, col, 0.25 * S))
        elif kind == "isource":                          # DIN/IEC: line across the connection
            obj.add(_line(M - r * v, M + r * v, col, sw))
        elif kind == "ac_source":
            ts = np.linspace(-np.pi, np.pi, 24)
            obj.add(_polyline([M + (0.6 * r * t / np.pi) * u + 0.35 * r * np.sin(t) * v for t in ts], col, 0.8 * sw))
        elif kind == "lamp":
            k = r / np.sqrt(2)
            obj.add(_line(M - k * (u + v), M + k * (u + v), col, sw)); obj.add(_line(M - k * (u - v), M + k * (u - v), col, sw))
        else:
            obj.add(Text("A" if kind == "ammeter" else "V", position=M, font_size=fs, color=col))
    elif kind == "vsource_dc":                           # battery: long thin + short thick plate
        obj.add(_line(P0 - 0.9 * w * v, P0 + 0.9 * w * v, col, sw))
        obj.add(_line(P1 - 0.45 * w * v, P1 + 0.45 * w * v, col, 2.2 * sw))
    elif kind in ("vcvs", "vccs", "cccs", "ccvs"):     # controlled source: diamond
        h = 0.5 * body
        obj.add(_poly([M - h * u, M - 0.6 * h * v, M + h * u, M + 0.6 * h * v], col, sw))
        if kind in ("vccs", "cccs"):                     # current source: arrow along u
            obj.add(_line(M - 0.55 * h * u, M + 0.3 * h * u, col, sw)); obj.add(_head(M + 0.6 * h * u, u, col, 0.25 * S))
        elif ansi:                                       # ANSI voltage source: + / -
            for part in _plus_minus(M, h, u, col, sw):
                obj.add(part)
        else:                                            # IEC voltage source: line along u
            obj.add(_line(M - h * u, M + h * u, col, sw))
    elif kind == "nullator":                             # oval
        ts = np.linspace(0, 2 * np.pi, 40)
        obj.add(_polyline([M + 0.5 * body * np.cos(t) * u + 0.22 * S * np.sin(t) * v for t in ts], col, sw))
    elif kind == "norator":                              # two overlapping circles
        r = 0.3 * body
        obj.add(_circle(M - 0.2 * body * u, r, col, sw)); obj.add(_circle(M + 0.2 * body * u, r, col, sw))
    elif kind == "switch":
        obj.add(_dot(P0, 0.06 * S, col)); obj.add(_dot(P1, 0.06 * S, col))
        obj.add(_line(P0, P0 + 0.95 * body * (np.cos(0.45) * u + np.sin(0.45) * v), col, sw))
    # --- name and value: one block on the +v side (label_flip: -v side) ---
    sgn = -1.0 if args.get("label_flip", False) else 1.0
    nv = sgn * v
    label = str(args.get("label", "")).strip()
    value = str(args.get("value", "")).strip()
    txt = "\\\\".join(t for t in (label, value) if t)
    if txt:
        lines = 2 if (label and value) else 1
        side_text = abs(nv[0]) > 0.7                      # text sits beside a vertical component
        off = (0.5 * S * (0.5 if kind in ("capacitor", "capacitor_var", "vsource_dc") else 0.4) + 0.25) if side_text \
            else (0.25 * S + 0.15 + 0.62 * lines * fs * UPP)
        if kind in ("resistor_var", "capacitor_var", "led"):        # the arrows reach beyond the body
            off += 0.3 * S
        if kind in ("vsource", "isource", "ac_source", "lamp", "ammeter", "voltmeter", "vcvs", "vccs", "cccs", "ccvs"):
            off += 0.1 * S
        obj.add(Text(txt, position=M + off * nv, font_size=fs, color=col, align=_align_for(nv[0])))
    # --- current arrow on a lead (start or end), voltage arrow on the other side ---
    cur = str(args.get("current", "")).strip()
    vol = str(args.get("voltage", "")).strip()
    if cur:
        cu = -u if args.get("current_reverse", False) else u
        if str(args.get("current_at", "start")) == "end":
            mid = 0.5 * (P1 + B) if body < L - 1e-9 else A + 0.8 * L * u
        else:
            mid = 0.5 * (A + P0) if body < L - 1e-9 else A + 0.2 * L * u
        obj.add(_head(mid + 0.13 * S * cu, cu, col, 0.26 * S))
        obj.add(Text(cur, position=mid + (0.3 * S + 0.45 * fs * UPP) * nv, font_size=fs, color=col, align=_align_for(nv[0])))
    if vol:
        vv = -nv                                          # opposite side of the name block
        off = 0.45 * S + 0.12
        a, b = A + off * vv + 0.12 * L * u, B + off * vv - 0.12 * L * u
        if args.get("voltage_reverse", False):
            a, b = b, a
        dd = b - a
        nd = float(np.linalg.norm(dd))
        if nd > 1e-9:
            obj.add(_line(a, b - 0.2 * S * dd / nd, col, 0.7 * sw)); obj.add(_head(b, dd, col, 0.26 * S))
        obj.add(Text(vol, position=0.5 * (a + b) + (0.12 + (0.0 if abs(vv[0]) > 0.7 else 0.5 * fs * UPP)) * vv,
                     font_size=fs, color=col, align=_align_for(vv[0])))
    return obj


# ---------------------------------------------------------------------------------------------
# Multi-terminal devices: built in a local frame (x right, y up, unit = size), then rotated about the
# centre by `rotation` degrees; flip mirrors y (emitter up/down, inputs swapped).
DEVICE_KINDS = ["npn", "pnp", "nmos", "pmos", "nmos4", "pmos4", "nmos_dep", "nmos_dig", "pmos_dig", "jfet_n",
                "opamp", "amp", "twoport", "ground", "terminal", "node", "vtube", "mixer", "sum", "oscillator",
                "filter_lp", "filter_bp", "filter_hp", "adc", "antenna"]


def build_device(args, style, axes):
    c2p = c2p_fn(axes)
    kind = str(args.get("kind", "npn"))
    C = c2p(*xyz(args.get("center", [0.0, 0.0, 0.0])))
    S = float(args.get("size", 1.0))
    rot = np.radians(float(args.get("rotation", 0.0)))
    fy = -1.0 if args.get("flip", False) else 1.0
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 3.0))
    fs = float(args.get("font_size", 24))
    pins = bool(args.get("pins", True))
    cr, sr = _direction(float(args.get("rotation", 0.0)))   # exact for 0/90/180/270 (pins stay on the grid)
    white = (1.0, 1.0, 1.0)

    def D(x, y):                                        # local direction -> world direction
        y = y * fy
        return np.array([x * cr - y * sr, x * sr + y * cr, 0.0])

    def P(x, y):                                        # local point -> world point
        return C + S * D(x, y)

    obj = AnimObject(); obj.color = col

    def L_(pts, w=1.0):
        obj.add(_polyline([P(*p) for p in pts], col, w * sw))

    def text(t, x, y, dx=0.0, scale=1.0):               # a label at local (x, y); dx = which side it reads from
        obj.add(Text(t, position=P(x, y), font_size=scale * fs, color=col, align=_align_for(D(dx, 0.0)[0])))

    def pin(name, x, y, dx):
        if pins:
            text(name, x, y, dx, 0.85)

    label = str(args.get("label", "")).strip()
    label_at = (0.75, 0.0, 1.0)                          # default: right of the body, reading rightwards
    if kind in ("npn", "pnp"):
        L_([(-1.0, 0.0), (-0.3, 0.0)])                                   # base lead
        L_([(-0.3, -0.45), (-0.3, 0.45)], 2.0)                           # base bar
        L_([(-0.3, 0.2), (0.5, 0.6), (0.5, 1.0)])                        # collector
        L_([(-0.3, -0.2), (0.5, -0.6), (0.5, -1.0)])                     # emitter
        if kind == "npn":
            obj.add(_head(P(0.38, -0.54), D(0.8, -0.4), col, 0.28 * S))
        else:
            obj.add(_head(P(-0.06, -0.32), D(-0.8, 0.4), col, 0.28 * S))
        pin("B", -0.8, 0.2, 0.0); pin("C", 0.65, 0.85, 1.0); pin("E", 0.65, -0.85, 1.0)
    elif kind in ("nmos", "pmos", "nmos4", "pmos4", "nmos_dep", "nmos_dig", "pmos_dig", "jfet_n"):
        four = kind in ("nmos4", "pmos4", "nmos_dep")
        bubble = kind == "pmos_dig"
        if kind == "jfet_n":
            L_([(-0.2, -0.55), (-0.2, 0.55)], 2.0)
            L_([(-1.0, 0.0), (-0.2, 0.0)])
            obj.add(_head(P(-0.2, 0.0), D(1.0, 0.0), col, 0.26 * S))
        else:
            L_([(-0.35, -0.45), (-0.35, 0.45)], 2.0)                    # gate electrode
            if four and kind != "nmos_dep":                              # enhancement: interrupted channel
                for y0, y1 in ((-0.55, -0.25), (-0.15, 0.15), (0.25, 0.55)):
                    L_([(-0.2, y0), (-0.2, y1)], 2.0)
            else:
                L_([(-0.2, -0.55), (-0.2, 0.55)], 2.0)
            if bubble:
                obj.add(_circle(P(-0.47, 0.0), 0.1 * S, col, sw))
                L_([(-1.0, 0.0), (-0.57, 0.0)])
            else:
                L_([(-1.0, 0.0), (-0.35, 0.0)])
        L_([(-0.2, 0.4), (0.5, 0.4), (0.5, 1.0)])                        # drain
        L_([(-0.2, -0.4), (0.5, -0.4), (0.5, -1.0)])                     # source
        if four:                                                         # bulk with arrow (DIN)
            L_([(-0.2, 0.0), (1.0, 0.0)])
            if kind == "pmos4":
                obj.add(_head(P(0.25, 0.0), D(1.0, 0.0), col, 0.24 * S))   # p-channel: arrow away from the channel
            else:
                obj.add(_head(P(-0.2, 0.0), D(-1.0, 0.0), col, 0.24 * S))  # n-channel: arrow into the channel
            pin("B", 0.85, 0.2, 1.0)
            label_at = (0.75, 0.55, 1.0)
        elif kind == "nmos":                                             # bipolar-like: arrow out of the source
            obj.add(_head(P(0.35, -0.4), D(1.0, 0.0), col, 0.22 * S))
        elif kind == "pmos":                                             # arrow into the source
            obj.add(_head(P(0.0, -0.4), D(-1.0, 0.0), col, 0.22 * S))
        pin("G", -0.8, 0.2, 0.0); pin("D", 0.65, 0.85, 1.0); pin("S", 0.65, -0.85, 1.0)
    elif kind in ("opamp", "amp"):
        if symbol_style(args) == "ansi":                 # ANSI: triangle
            obj.add(_poly([P(-1.0, 1.0), P(-1.0, -1.0), P(1.0, 0.0)], col, sw, fill=white))
        else:                                            # IEC 60617-13: box with the amplifier sign (and ∞)
            obj.add(_poly([P(-1.0, -1.0), P(1.0, -1.0), P(1.0, 1.0), P(-1.0, 1.0)], col, sw, fill=white))
            L_([(-0.3, 0.75), (-0.3, 0.25), (0.15, 0.5), (-0.3, 0.75)], 0.7)
            if kind == "opamp":
                text("∞", 0.5, 0.5, 0.0, 1.4)
        L_([(1.0, 0.0), (1.5, 0.0)])
        if kind == "opamp":
            L_([(-1.5, 0.5), (-1.0, 0.5)]); L_([(-1.5, -0.5), (-1.0, -0.5)])
            text("\\minus", -0.72, 0.5); text("+", -0.72, -0.5)
        else:
            L_([(-1.5, 0.0), (-1.0, 0.0)])
        label_at = (0.3, 0.85, 1.0) if symbol_style(args) == "ansi" else (0.0, 1.3, 0.0)   # IEC: above the box
    elif kind in ("filter_lp", "filter_bp", "filter_hp", "adc"):
        obj.add(_poly([P(-1.0, -0.7), P(1.0, -0.7), P(1.0, 0.7), P(-1.0, 0.7)], col, sw, fill=white))
        L_([(-1.5, 0.0), (-1.0, 0.0)]); L_([(1.0, 0.0), (1.5, 0.0)])
        if kind == "adc":
            L_([(-1.0, -0.7), (1.0, 0.7)], 0.6)
            text("A", -0.5, 0.25, 0.0, 0.9); text("D", 0.5, -0.3, 0.0, 0.9)
        else:                                            # three stacked waves, struck through per type
            for k, y in enumerate((0.35, 0.0, -0.35)):
                ts = np.linspace(-np.pi, np.pi, 16)
                L_([(-0.45 + 0.9 * (t + np.pi) / (2 * np.pi), y + 0.08 * np.sin(t)) for t in ts], 0.7)
            strike = {"filter_lp": (0.35,), "filter_hp": (-0.35,), "filter_bp": (0.35, -0.35)}[kind]
            for y in strike:
                L_([(-0.25, y - 0.15), (0.25, y + 0.15)], 0.7)
        label_at = (0.0, 1.0, 0.0)
    elif kind in ("mixer", "sum", "oscillator"):
        obj.add(_circle(C, 0.5 * S, col, sw, fill=white))
        if kind == "mixer":
            k = 0.5 / np.sqrt(2)
            L_([(-k, -k), (k, k)]); L_([(-k, k), (k, -k)])
        elif kind == "sum":
            text("+", 0.0, 0.0, 0.0, 1.1)
        else:
            ts = np.linspace(-np.pi, np.pi, 20)
            L_([(0.3 * t / np.pi, 0.15 * np.sin(t)) for t in ts], 0.8)
        L_([(-1.0, 0.0), (-0.5, 0.0)]); L_([(0.5, 0.0), (1.0, 0.0)])
        if kind != "oscillator":
            L_([(0.0, -0.5), (0.0, -1.0)])
        label_at = (0.0, 0.85, 0.0)
    elif kind == "antenna":
        L_([(0.0, 0.0), (0.0, 0.9)]); L_([(-0.35, 1.3), (0.0, 0.9), (0.35, 1.3)]); L_([(-0.35, 1.3), (0.35, 1.3)])
        label_at = (0.45, 1.1, 1.0)
    elif kind == "twoport":
        obj.add(_poly([P(-1.0, -0.75), P(1.0, -0.75), P(1.0, 0.75), P(-1.0, 0.75)], col, sw))
        for y in (0.5, -0.5):
            L_([(-1.5, y), (-1.0, y)]); L_([(1.0, y), (1.5, y)])
            obj.add(_circle(P(-1.5, y), 0.06 * S, col, 0.7 * sw, fill=white)); obj.add(_circle(P(1.5, y), 0.06 * S, col, 0.7 * sw, fill=white))
        pin("1", -1.7, 0.5, -1.0); pin("1'", -1.7, -0.5, -1.0); pin("2", 1.7, 0.5, 1.0); pin("2'", 1.7, -0.5, 1.0)
        label_at = (0.0, 0.0, 0.0)
    elif kind == "ground":
        L_([(0.0, 0.0), (0.0, -0.3)])
        for k, hw in enumerate((0.4, 0.27, 0.14)):
            L_([(-hw, -0.3 - 0.12 * k), (hw, -0.3 - 0.12 * k)])
        label_at = (0.55, -0.4, 1.0)
    elif kind == "terminal":
        obj.add(_circle(C, 0.09 * S, col, sw, fill=white))
        label_at = (0.0, 0.35, 0.0)
    elif kind == "node":
        obj.add(_dot(C, 0.08 * S, col))
        label_at = (0.25, 0.3, 1.0)
    elif kind == "vtube":                                # triode: anode plate, dashed grid, cathode in a bulb
        obj.add(_circle(C, 1.0 * S, col, sw))
        L_([(-0.45, 0.5), (0.45, 0.5)], 1.6); L_([(0.0, 0.5), (0.0, 1.5)])
        for x in (-0.55, -0.25, 0.05, 0.35):
            L_([(x, 0.0), (x + 0.15, 0.0)])
        L_([(-0.6, 0.0), (-1.5, 0.0)])
        L_([(-0.4, -0.45), (0.4, -0.45)]); L_([(0.0, -0.45), (0.0, -1.5)])
        pin("A", 0.15, 1.3, 1.0); pin("G", -1.3, 0.2, 0.0); pin("K", 0.15, -1.3, 1.0)
        label_at = (1.15, 0.6, 1.0)
    if label:
        x, y, dx = label_at
        text(label, x, y, dx)
    return obj


# ---------------------------------------------------------------------------------------------
def build_wire(args, style, axes):
    """Wire through the given points (data coords). route hv/vh inserts a right-angle corner between
    consecutive points. dots: indices of the GIVEN points that get a junction dot ("0;2") or "all"."""
    c2p = c2p_fn(axes)
    pts = pairs(args.get("points", ""))
    col = style.get("color", (0.0, 0.0, 0.0))
    sw = float(style.get("stroke_width", 3.0))
    obj = AnimObject(); obj.color = col
    if len(pts) < 2:
        return obj
    route = str(args.get("route", "direct"))
    path = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        if route == "hv" and x0 != x1 and y0 != y1:
            path.append((x1, y0))
        elif route == "vh" and x0 != x1 and y0 != y1:
            path.append((x0, y1))
        path.append((x1, y1))
    obj.add(_polyline([c2p(x, y) for x, y in path], col, sw))
    dots = str(args.get("dots", "")).strip().lower()
    idx = []
    if dots == "all":
        idx = list(range(len(pts)))
    elif dots:
        idx = [int(float(t)) for t in dots.replace(",", ";").split(";") if t.strip()]
    r = float(args.get("dot_radius", 0.07))
    for i in idx:
        if 0 <= i < len(pts):
            obj.add(_dot(c2p(*pts[i]), r, col))
    return obj


def build_node(args, style, axes):
    """Named junction / potential node: a dot with a label (offset in world units)."""
    c2p = c2p_fn(axes)
    x, y, _ = xyz(args.get("center", [0.0, 0.0, 0.0]))
    ox, oy, _ = xyz(args.get("offset", [0.25, 0.25, 0.0]))
    col = style.get("color", (0.0, 0.0, 0.0))
    obj = AnimObject(); obj.color = col
    w = c2p(x, y)
    if args.get("dot", True):
        obj.add(_dot(w, float(args.get("radius", 0.08)), col))
    label = str(args.get("label", "")).strip()
    if label:
        obj.add(Text(label, position=w + np.array([ox, oy, 0.0]), font_size=float(args.get("font_size", 26)),
                     color=col, align=_align_for(ox * 4)))
    return obj


BUILDERS = {"Component": build_component, "Device": build_device, "Wire": build_wire, "Node": build_node}


# ---------------------------------------------------------------------------------------------
# Connection points, so the editor can show pins, snap wires to them and route new wires.
_TRANSISTOR = [("B", -1.0, 0.0), ("C", 0.5, 1.0), ("E", 0.5, -1.0)]
_FET = [("G", -1.0, 0.0), ("D", 0.5, 1.0), ("S", 0.5, -1.0)]
_ONE = [("", 0.0, 0.0)]
DEVICE_PINS = {
    "npn": _TRANSISTOR, "pnp": _TRANSISTOR,
    "nmos": _FET, "pmos": _FET, "nmos_dig": _FET, "pmos_dig": _FET, "jfet_n": _FET,
    "nmos4": _FET + [("B", 1.0, 0.0)], "pmos4": _FET + [("B", 1.0, 0.0)], "nmos_dep": _FET + [("B", 1.0, 0.0)],
    "opamp": [("-", -1.5, 0.5), ("+", -1.5, -0.5), ("out", 1.5, 0.0)],
    "amp": [("in", -1.5, 0.0), ("out", 1.5, 0.0)], "adc": [("in", -1.5, 0.0), ("out", 1.5, 0.0)],
    "filter_lp": [("in", -1.5, 0.0), ("out", 1.5, 0.0)], "filter_bp": [("in", -1.5, 0.0), ("out", 1.5, 0.0)],
    "filter_hp": [("in", -1.5, 0.0), ("out", 1.5, 0.0)],
    "mixer": [("in", -1.0, 0.0), ("out", 1.0, 0.0), ("lo", 0.0, -1.0)],
    "sum": [("in", -1.0, 0.0), ("out", 1.0, 0.0), ("in2", 0.0, -1.0)],
    "oscillator": [("in", -1.0, 0.0), ("out", 1.0, 0.0)],
    "twoport": [("1", -1.5, 0.5), ("1'", -1.5, -0.5), ("2", 1.5, 0.5), ("2'", 1.5, -0.5)],
    "vtube": [("A", 0.0, 1.5), ("G", -1.5, 0.0), ("K", 0.0, -1.5)],
    "ground": _ONE, "terminal": _ONE, "node": _ONE, "antenna": _ONE,
}


def device_pin_offsets(args):
    """Pins of a Device as (name, dx, dy) offsets from its centre in WORLD units (size, rotation, flip
    applied the same way build_device draws them)."""
    S = float(args.get("size", 1.0))
    ux, uy = _direction(args.get("rotation", 0.0))
    fy = -1.0 if args.get("flip", False) else 1.0
    out = []
    for name, x, y in DEVICE_PINS.get(str(args.get("kind", "npn")), _ONE):
        y = y * fy
        out.append((name, S * (x * ux - y * uy), S * (x * uy + y * ux)))
    return out


def pins_world(kind_type, args, axes):
    """All connection points of a circuit element as (name, world point). Components: pin 1/2; devices:
    their pins; wires: both ends; nodes: the node itself."""
    c2p = c2p_fn(axes)
    if kind_type == "Component":
        pa, pb = component_ends(args)
        return [("1", c2p(*pa)), ("2", c2p(*pb))]
    if kind_type == "Device":
        C = c2p(*xyz(args.get("center", [0.0, 0.0, 0.0])))
        return [(n, C + np.array([dx, dy, 0.0])) for n, dx, dy in device_pin_offsets(args)]
    if kind_type == "Wire":
        pts = pairs(args.get("points", ""))
        return [("a", c2p(*pts[0])), ("b", c2p(*pts[-1]))] if len(pts) >= 2 else []
    if kind_type == "Node":
        return [("", c2p(*xyz(args.get("center", [0.0, 0.0, 0.0]))))]
    return []
