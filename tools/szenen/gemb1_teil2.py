"""GEMB 1 Teil 2 (kap2_stufen.tex): Das Teilchen in der Box.

Aufruf: python tools/szenen/gemb1_teil2.py, danach python tools/szenen_ansehen.py out.png gemb1/k2gitter ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap2.py.
"""
import sys
from math import asin, cos, pi, radians, sin, sqrt, tan
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#ddf0e4"
C0, C1 = 0.03811, 0.37611          # hbar^2/(2m_e), hbar^2 pi^2/(2m_e) in eV nm^2
T0 = C0 / 0.2 ** 2                 # Rechenmodell a = 0,2 nm
E1 = C1 / 2.0 ** 2                 # Rechenmodell L = 2 nm


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    return s.tr("a_" + name + einheit, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def poly(s, on, ecken, farbe, deckung=0.3, dicke=0):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": farbe, "fill_color": farbe,
                              "fill_opacity": deckung, "stroke_width": dicke}, on)


# ------------------------------------------------------------------------------------------ Stufe 1
def k2gitter():
    """Punkte auf dem Gitter und zweite Differenz als Änderung der Steigung."""
    s = Szene("gemb1/k2gitter")
    w = s.welt()
    g = lambda u: -0.05 + 0.95 * sin(0.42 * (u - 0.9))
    X = lambda i: -3.25 + 0.48 * i
    y0 = -1.15
    s.pfeil((-3.5, y0), (-0.3, y0), "", farbe=SCHWARZ, spitze=0.17)
    t(s, "x", (-0.3, y0 - 0.26), "center")
    s.daten(w, [(X(i / 20), g(i / 20)) for i in range(-3, 125)], farbe=SCHWARZ, dicke=4)
    for i in range(7):
        s.linie(w, (X(i), y0), (X(i), g(i)), farbe=ROT, dicke=2, dash=DASH)
        s.punkt(w, X(i), y0, r=0.05, farbe=SCHWARZ)
        s.punkt(w, X(i), g(i), r=0.075, farbe=ROT)
    for i, n in ((2, "%sell-1" % chr(92)), (3, chr(92) + "ell"), (4, "%sell+1" % chr(92))):
        t(s, n, (X(i), y0 - 0.28))
    t(s, "\\psi_\\ell", (X(3) - 0.04, g(3) + 0.3), "right", ROT)
    s.pfeil((X(5), y0 + 0.22), (X(6), y0 + 0.22), "", farbe=SCHWARZ, spitze=0.12, doppelt=True, dicke=2)
    t(s, "a", (0.5 * (X(5) + X(6)), y0 + 0.42))
    # Rechts: Ausschnitt
    P = [(0.6, -0.85), (1.9, 0.35), (3.2, 0.85)]
    # Parabel durch die drei Punkte
    (x0, y00), (x1, y1), (x2, y2) = P
    c = ((y2 - y1) / (x2 - x1) - (y1 - y00) / (x1 - x0)) / (x2 - x0)
    b = (y1 - y00) / (x1 - x0) - c * (x0 + x1)
    a_ = y00 - b * x0 - c * x0 * x0
    kurve = [(0.42 + i * 0.03, a_ + b * (0.42 + i * 0.03) + c * (0.42 + i * 0.03) ** 2) for i in range(101)]
    s.daten(w, kurve, farbe=SCHWARZ, dicke=4)
    s.linie(w, P[0], P[1], farbe=GRUEN, dicke=4)
    s.linie(w, P[1], P[2], farbe=ORANGE, dicke=4)
    for p in P:
        s.punkt(w, p[0], p[1], r=0.08, farbe=ROT)
    t(s, "\\psi_{\\ell-1}", (P[0][0] + 0.12, P[0][1] - 0.04), "left", ROT)
    t(s, "\\psi_\\ell", (P[1][0] - 0.08, P[1][1] + 0.22), "right", ROT)
    t(s, "\\psi_{\\ell+1}", (P[2][0], P[2][1] + 0.26), "center", ROT)
    t(s, s.tr("st1", "Steigung links", "left slope", "pendiente izquierda", "左侧斜率"), (1.55, -0.62), "left", GRUEN)
    t(s, s.tr("st2", "Steigung rechts", "right slope", "pendiente derecha", "右侧斜率"), (3.3, -0.05), "right", ORANGE)
    s.pfeil((P[0][0], -1.15), (P[1][0], -1.15), "", farbe=SCHWARZ, spitze=0.12, doppelt=True, dicke=2)
    s.pfeil((P[1][0], -1.15), (P[2][0], -1.15), "", farbe=SCHWARZ, spitze=0.12, doppelt=True, dicke=2)
    t(s, "a", (0.5 * (P[0][0] + P[1][0]), -1.4))
    t(s, "a", (0.5 * (P[1][0] + P[2][0]), -1.4))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k2kosinus():
    """Kosinus-Band und Geschwindigkeit im Rechenmodell a = 0,2 nm."""
    s = Szene("gemb1/k2kosinus")
    xl = s.tr("k_zone", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)")
    a = s.achsen((-1.6, 1.6), (0, 6), breite=2.95, hoehe=1.95, mitte=(-1.85, 0), xl=xl, yl=achse(s, "E", "eV"), xticks="-1;0;1", yticks="0;2;4;6")
    s.band(a, -1, 1, 0, 6, farbe=BLAU, deckung=0.08)
    s.kurve(a, "%.4f*(1-cos(pi*x))" % (2 * T0), x=(-1.6, -1), farbe=BLAU, dicke=3, dash=DOT)
    s.kurve(a, "%.4f*(1-cos(pi*x))" % (2 * T0), x=(1, 1.6), farbe=BLAU, dicke=3, dash=DOT)
    par = [(i / 100, T0 * (pi * i / 100) ** 2) for i in range(-80, 81)]
    s.daten(a, [p for p in par if p[1] <= 6], farbe=GRAU, dicke=3, dash=DASH)
    s.kurve(a, "%.4f*(1-cos(pi*x))" % (2 * T0), x=(-1, 1), farbe=BLAU, dicke=5)
    s.linie(a, (1, 0), (1, 6), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (-1, 0), (-1, 6), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "4t_0", (0.0, 4.25), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("par", "Parabel", "parabola", "parábola", "抛物线"), (0.0, 5.45), groesse=22, ausrichtung="center", farbe=GRAU)
    b = s.achsen((-1.6, 1.6), (-8, 8), breite=2.7, hoehe=1.95, mitte=(1.9, 0), xl=xl, yl=s.tr("v_einheit", "v in 10^5 m/s", "v in 10^5 m/s", "v en 10^5 m/s", "v / (10^5 m/s)"),
                 xticks="-1;0;1", yticks="-6;0;6")
    s.band(b, -1, 1, -8, 8, farbe=BLAU, deckung=0.08)
    s.kurve(b, "5.79*pi*x", x=(-0.43, 0.43), farbe=GRAU, dicke=3, dash=DASH)
    s.kurve(b, "5.79*sin(pi*x)", x=(-1, 1), farbe=BLAU, dicke=5)
    s.linie(b, (-1.6, 0), (1.6, 0), farbe=GRAU, dicke=1.5)
    s.punkt(b, 0.5, 5.79, farbe=ROT)
    s.text(b, "v_{max}", (0.82, 6.9), groesse=GR, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k2box():
    """Box L = 2 nm: Niveaus mit Wellenfunktionen, Parabel mit erlaubten k, Dichte für n = 1, 2, 3, 30."""
    s = Szene("gemb1/k2box")
    ep = 1.15
    a = s.achsen((-0.5, 2.5), (0, ep), breite=2.85, hoehe=1.5, mitte=(-1.95, 1.1), xl=achse(s, "x", "nm"), yl=achse(s, "E", "eV"), xticks="0;2", yticks="0;0.5;1")
    s.band(a, -0.5, 0, 0, ep, farbe=GRAU, deckung=0.3)
    s.band(a, 2, 2.5, 0, ep, farbe=GRAU, deckung=0.3)
    s.linie(a, (0, 0), (0, ep), farbe=SCHWARZ, dicke=4)
    s.linie(a, (2, 0), (2, ep), farbe=SCHWARZ, dicke=4)
    Fall = (1, 2, 3)
    for n in Fall:
        E = E1 * n * n
        s.linie(a, (0, E), (2, E), farbe=ROT, dicke=3)
        s.kurve(a, "%.4f+0.085*sin(%d*pi*x/2)" % (E, n), x=(0, 2), farbe=BLAU, dicke=4)
        s.text(a, "E_%d" % n, (-0.25, E), groesse=GR, ausrichtung="center", farbe=ROT)
    b = s.achsen((0, 6.3), (0, ep), breite=2.4, hoehe=1.5, mitte=(1.75, 1.1), xl=s.tr("k_nm", "k in 1/nm", "k in 1/nm", "k en 1/nm", "k / nm^{-1}"), yl="", xticks="0;2;4;6", yticks="0;0.5;1")
    s.kurve(b, "%.5f*x*x" % C0, x=(0, 5.45), farbe=GRUEN, dicke=4)
    for n in Fall:
        k, E = n * pi / 2, E1 * n * n
        s.linie(b, (0, E), (k, E), farbe=ROT, dicke=2, dash=DASH)
        s.linie(b, (k, 0), (k, E), farbe=ROT, dicke=2, dash=DASH)
        s.punkt(b, k, E, farbe=ROT, r=0.08)
        s.text(b, "k_%d" % n, (k + 0.42, E - 0.02), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b, "E(k)", (3.3, 1.02), groesse=GR, ausrichtung="center", farbe=GRUEN)
    for i, n in enumerate((1, 2, 3, 30)):
        c = s.achsen((0, 1), (0, 2.3), breite=1.2, hoehe=0.75, mitte=(-2.6 + 1.7 * i, -1.4), xl="x/L", yl="L|\\psi|^2" if i == 0 else "",
                     xticks="1", yticks="0;1;2")
        s.text(c, "n = %d" % n, (0.5, 2.75), groesse=GR, ausrichtung="center")
        m = 1400 if n == 30 else 120
        s.daten(c, [(j / m, 2 * sin(n * pi * j / m) ** 2) for j in range(m + 1)], farbe=BLAU, dicke=2.5 if n == 30 else 4)
        s.linie(c, (0, 1), (1, 1), farbe=ROT, dicke=2.5, dash=DASH)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def kontur(cx, cy, w, h, c, n=48):
    """Höhenlinie sin(u)*sin(v) = c in der Zelle mit Mitte (cx, cy): geschlossener Zug."""
    u0 = asin(c)
    us = [u0 + (pi - 2 * u0) * i / n for i in range(n + 1)]
    ob, un = [], []
    for u in us:
        q = min(1.0, c / sin(u)) if sin(u) > 0 else 1.0
        v = asin(q)
        ob.append((cx + (u / pi - 0.5) * w, cy + (0.5 - v / pi) * h))
        un.append((cx + (u / pi - 0.5) * w, cy + (v / pi - 0.5) * h))
    return ob + un[::-1]


def k2schach():
    """Muster psi_{n_x,n_y} in der quadratischen Box und Paraboloid E(k_x, k_y)."""
    s = Szene("gemb1/k2schach")
    w = s.welt()
    seite = 1.08
    plaetze = {(1, 1): (-3.15, -1.45), (2, 1): (-1.75, -1.45), (1, 2): (-3.15, 0.1), (2, 2): (-1.75, 0.1)}
    for (nx, ny), (x0, y0) in plaetze.items():
        bx, by = seite / nx, seite / ny
        for i in range(nx):
            for j in range(ny):
                f = ROT if (i + j) % 2 == 0 else BLAU
                cx, cy = x0 + (i + 0.5) * bx, y0 + (j + 0.5) * by
                for c in (0.15, 0.4, 0.65, 0.88):
                    poly(s, w, kontur(cx, cy, bx, by, c), f, deckung=0.22)
                t(s, "+" if f == ROT else "\u2212", (cx, cy), farbe=f, g=26)
        s.box("", (x0 + seite / 2, y0 + seite / 2), breite=seite, hoehe=seite, deckung=0.0, dicke=2.5)
        for i in range(1, nx):
            s.linie(w, (x0 + i * bx, y0), (x0 + i * bx, y0 + seite), farbe=SCHWARZ, dicke=2, dash=DASH)
        for j in range(1, ny):
            s.linie(w, (x0, y0 + j * by), (x0 + seite, y0 + j * by), farbe=SCHWARZ, dicke=2, dash=DASH)
        t(s, "\\psi_{%d,%d}" % (nx, ny), (x0 + seite / 2, y0 + seite + 0.2))
    t(s, "x", (-1.21, -1.66))
    t(s, "y", (-3.31, -0.91))
    # Paraboloid: Parallelprojektion, k_x nach rechts vorn, k_y nach links vorn
    el, az = radians(20), radians(42)
    S, Sz, ox, oy = 0.95, 0.62, 1.85, -1.3

    def pr(kx, ky, z):
        X = kx * cos(az) - ky * cos(az)
        T = -(kx * sin(az) + ky * sin(az))
        return (ox + S * X, oy + S * T * sin(el) + Sz * z * cos(el))

    rand = 1.55
    for E_ in (0.6, 1.2):
        r = sqrt(E_)
        s.daten(w, [pr(r * cos(2 * pi * i / 90), r * sin(2 * pi * i / 90), E_) for i in range(91)], farbe="#9fc3ec", dicke=2)
    r = rand
    s.daten(w, [pr(r * cos(2 * pi * i / 120), r * sin(2 * pi * i / 120), r * r) for i in range(121)], farbe=BLAU, dicke=4)
    # Umriss: Einhüllende der Ringe
    ce, se = cos(el), sin(el)
    q = Sz * ce
    wst = S * se / (2 * q)
    xe = sqrt(r * r - wst * wst)
    um = [(i / 60 * xe, q * (i / 60 * xe) ** 2 + (q * wst * wst - S * se * wst)) for i in range(-60, 61)]
    s.daten(w, [(ox + S * x, oy + y) for x, y in um], farbe=BLAU, dicke=4)
    s.pfeil(pr(0, 0, 0), pr(2.0, 0, 0), "", farbe=SCHWARZ, spitze=0.15, dicke=2.5)
    s.pfeil(pr(0, 0, 0), pr(0, 2.0, 0), "", farbe=SCHWARZ, spitze=0.15, dicke=2.5)
    s.pfeil(pr(0, 0, 0), (ox, oy + 2.4), "", farbe=SCHWARZ, spitze=0.15, dicke=2.5)
    a, b_ = pr(2.0, 0, 0), pr(0, 2.0, 0)
    t(s, "k_x", (a[0] + 0.12, a[1] - 0.05), "left")
    t(s, "k_y", (b_[0] - 0.12, b_[1] - 0.05), "right")
    t(s, "E", (ox + 0.14, oy + 2.4), "left")
    k1 = 0.5
    for nx, ny in ((1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (1, 3)):
        kx, ky = nx * k1, ny * k1
        e_ = kx * kx + ky * ky
        if e_ > rand * rand:
            continue
        s.linie(w, pr(kx, ky, 0), pr(kx, ky, e_), farbe=ROT, dicke=1.5, dash=DOT)
        s.punkt(w, *pr(kx, ky, 0), r=0.045, farbe=ROT)
        s.punkt(w, *pr(kx, ky, e_), r=0.075, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k2entartung():
    """Niveaus der quadratischen Box und einer um 10 % gestreckten Box."""
    s = Szene("gemb1/k2entartung")
    w = s.welt()
    sk, y0 = 0.225, -1.55
    Y = lambda e: y0 + sk * e
    xa = -2.75
    s.pfeil((xa, y0), (xa, Y(14)), "", farbe=SCHWARZ, spitze=0.17)
    t(s, "E/E_0", (xa - 0.12, Y(13.4)), "right")
    for e in (0, 5, 10):
        s.linie(w, (xa - 0.06, Y(e)), (xa + 0.06, Y(e)), dicke=2)
        t(s, str(e), (xa - 0.14, Y(e)), "right", g=22)
    x1, x2 = -2.35, -1.05
    x3, x4 = 0.75, 2.05
    t(s, "L_x = L_y", (0.5 * (x1 + x2), Y(14.6)))
    t(s, "L_x = 1.1 L_y", (0.5 * (x3 + x4), Y(14.6)))
    links = [(2, ["1,1"]), (5, ["1,2", "2,1"]), (8, ["2,2"]), (10, ["1,3", "3,1"]), (13, ["2,3", "3,2"])]
    rechts = {"1,1": 1.826, "2,1": 4.306, "1,2": 4.826, "2,2": 7.306, "3,1": 8.438, "1,3": 9.826, "3,2": 11.438, "2,3": 12.306}
    for e, st in links:
        f = ROT if len(st) == 2 else BLAU
        if len(st) == 2:
            mx = 0.5 * (x1 + x2)
            s.linie(w, (x1, Y(e)), (mx - 0.05, Y(e)), farbe=f, dicke=5)
            s.linie(w, (mx + 0.05, Y(e)), (x2, Y(e)), farbe=f, dicke=5)
        else:
            s.linie(w, (x1, Y(e)), (x2, Y(e)), farbe=f, dicke=5)
        t(s, ("(%s), (%s)" % tuple(st)) if len(st) == 2 else "(%s)" % st[0], (0.5 * (x1 + x2), Y(e) + 0.15), farbe=f, g=22)
        for z in st:
            s.linie(w, (x2 + 0.03, Y(e)), (x3 - 0.03, Y(rechts[z])), farbe=GRAU, dicke=2, dash=DASH)
    versatz = {"2,1": 0.72}
    for z, e in rechts.items():
        f = BLAU
        s.linie(w, (x3, Y(e)), (x4, Y(e)), farbe=f, dicke=5)
        t(s, "(%s)" % z, (x4 + 0.1 + versatz.get(z, 0), Y(e)), "left", f, g=22)
    t(s, s.tr("symm", "symmetrisch: entartet", "symmetric: degenerate", "simétrico: degenerado", "对称：简并"), (0.5 * (x1 + x2), y0 - 0.26), farbe=ROT, g=22)
    t(s, s.tr("brech", "gestreckt: aufgespalten", "stretched: split", "estirado: desdoblado", "拉伸：分裂"), (0.5 * (x3 + x4), y0 - 0.26), farbe=BLAU, g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def wuerfel(s, w, ox, oy, b=1.08):
    d = lambda x, y, z: (ox + b * (x + 0.42 * y), oy + b * (z + 0.3 * y))
    kanten_h = [((1, 1, 0), (0, 1, 0)), ((0, 1, 0), (0, 1, 1)), ((0, 1, 0), (0, 0, 0))]
    for p, q in kanten_h:
        s.linie(w, d(*p), d(*q), farbe=GRAU, dicke=2, dash=DASH)
    return d


def wuerfel_vorn(s, w, d):
    z = [((0, 0, 0), (1, 0, 0)), ((1, 0, 0), (1, 0, 1)), ((1, 0, 1), (0, 0, 1)), ((0, 0, 1), (0, 0, 0)),
         ((1, 0, 0), (1, 1, 0)), ((1, 0, 1), (1, 1, 1)), ((0, 0, 1), (0, 1, 1)), ((0, 1, 1), (1, 1, 1)), ((1, 1, 1), (1, 1, 0))]
    for p, q in z:
        s.linie(w, d(*p), d(*q), farbe=SCHWARZ, dicke=2.5)


def wolke(s, w, p, r, plus):
    f = ROT if plus else BLAU
    for q, de in ((1.0, 0.2), (0.72, 0.3), (0.45, 0.45)):
        s.kreis(w, p[0], p[1], r * q, farbe=f, dicke=0, fuellung=f, deckung=de)
    t(s, "+" if plus else "\u2212", p, farbe=f, g=26)


def k2knoten():
    """Vier Zustände der Würfelbox: Vorzeichen von psi und Knotenflächen."""
    s = Szene("gemb1/k2knoten")
    w = s.welt()
    oy = -0.75
    xs = (-3.45, -1.7, 0.05, 1.8)
    # (1,1,1)
    d = wuerfel(s, w, xs[0], oy)
    wolke(s, w, d(0.5, 0.5, 0.5), 0.42, True)
    wuerfel_vorn(s, w, d)
    s.pfeil(d(0, 0, 0), d(1.32, 0, 0), "", farbe=SCHWARZ, spitze=0.12, dicke=2)
    t(s, "x", (d(1.32, 0, 0)[0] + 0.03, d(1.32, 0, 0)[1] - 0.17), "left", g=22)
    s.pfeil(d(0, 0, 0), d(0, 0, 1.3), "", farbe=SCHWARZ, spitze=0.12, dicke=2)
    t(s, "z", (d(0, 0, 1.3)[0] - 0.1, d(0, 0, 1.3)[1]), "right", g=22)
    t(s, "y", (d(0, 1, 0)[0] - 0.14, d(0, 1, 0)[1] + 0.02), "right", GRAU, g=22)
    # (2,1,1): Knotenfläche x = 1/2
    d = wuerfel(s, w, xs[1], oy)
    poly(s, w, [d(.5, 0, 0), d(.5, 1, 0), d(.5, 1, 1), d(.5, 0, 1)], GRUEN, deckung=0.25)
    wolke(s, w, d(.25, .5, .5), 0.27, True)
    wolke(s, w, d(.75, .5, .5), 0.27, False)
    wuerfel_vorn(s, w, d)
    # (1,2,1): Knotenfläche y = 1/2
    d = wuerfel(s, w, xs[2], oy)
    wolke(s, w, d(.5, .78, .5), 0.27, False)
    poly(s, w, [d(0, .5, 0), d(1, .5, 0), d(1, .5, 1), d(0, .5, 1)], GRUEN, deckung=0.25)
    wolke(s, w, d(.5, .22, .5), 0.27, True)
    wuerfel_vorn(s, w, d)
    # (1,1,2): Knotenfläche z = 1/2
    d = wuerfel(s, w, xs[3], oy)
    wolke(s, w, d(.5, .5, .75), 0.27, False)
    poly(s, w, [d(0, 0, .5), d(1, 0, .5), d(1, 1, .5), d(0, 1, .5)], GRUEN, deckung=0.25)
    wolke(s, w, d(.5, .5, .25), 0.27, True)
    wuerfel_vorn(s, w, d)
    yt = oy + 1.68
    for x, n in zip(xs, ("(1,1,1)", "(2,1,1)", "(1,2,1)", "(1,1,2)")):
        t(s, n, (x + 0.75, yt))
    yu = oy - 0.42
    t(s, "E = 3 E_0", (xs[0] + 0.75, yu), farbe=BLAU)
    s.linie(w, (xs[1] + 0.05, yu + 0.12), (xs[3] + 1.5, yu + 0.12), farbe=ROT, dicke=2.5)
    t(s, s.tr("drei", "E = 6 E_0, dreifach entartet", "E = 6 E_0, threefold degenerate", "E = 6 E_0, triplemente degenerado", "E = 6 E_0，三重简并"), (0.5 * (xs[1] + xs[3] + 1.65), yu - 0.14), farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def quader(s, w, ox, oy, lx, ly, lz, f):
    d = lambda x, y, z: (ox + x + 0.5 * y, oy + z + 0.36 * y)
    poly(s, w, [d(0, 0, lz), d(lx, 0, lz), d(lx, ly, lz), d(0, ly, lz)], f, deckung=0.3, dicke=2)
    poly(s, w, [d(lx, 0, 0), d(lx, ly, 0), d(lx, ly, lz), d(lx, 0, lz)], f, deckung=0.5, dicke=2)
    poly(s, w, [d(0, 0, 0), d(lx, 0, 0), d(lx, 0, lz), d(0, 0, lz)], f, deckung=0.15, dicke=2)
    return d


def k2film():
    """Film, Draht, Punkt: Geometrie und Energien, schematisch mit quadratischem Querschnitt."""
    s = Szene("gemb1/k2film")
    w = s.welt()
    xm = (-2.3, 0.05, 2.35)
    titel = (s.tr("film", "Quantenfilm", "quantum film", "película cuántica", "量子薄膜"),
             s.tr("draht", "Quantendraht", "quantum wire", "hilo cuántico", "量子线"),
             s.tr("punkt", "Quantenpunkt", "quantum dot", "punto cuántico", "量子点"))
    yg = 0.75
    for x, ti in zip(xm, titel):
        t(s, ti, (x, yg + 0.95))
    d = quader(s, w, xm[0] - 0.95, yg, 1.3, 1.3, 0.13, BLAU)
    s.pfeil(d(0.65, 0.5, 0.3), d(1.55, 0.5, 0.3), "", farbe=ROT, spitze=0.13, dicke=3)
    s.pfeil(d(0.65, 0.5, 0.3), d(0.65, 1.45, 0.3), "", farbe=ROT, spitze=0.13, dicke=3)
    d = quader(s, w, xm[1] - 0.85, yg + 0.1, 1.6, 0.2, 0.2, BLAU)
    s.pfeil(d(0.5, 0.1, 0.45), d(1.45, 0.1, 0.45), "", farbe=ROT, spitze=0.13, dicke=3)
    d = quader(s, w, xm[2] - 0.15, yg + 0.1, 0.24, 0.24, 0.24, BLAU)
    t(s, s.tr("frei2", "2 Richtungen frei", "2 free directions", "2 direcciones libres", "2 个自由方向"), (xm[0], yg - 0.32), farbe=ROT, g=22)
    t(s, s.tr("frei1", "1 Richtung frei", "1 free direction", "1 dirección libre", "1 个自由方向"), (xm[1], yg - 0.32), farbe=ROT, g=22)
    t(s, s.tr("frei0", "keine Richtung frei", "no free direction", "ninguna dirección libre", "无自由方向"), (xm[2], yg - 0.32), farbe=ROT, g=22)
    yk = -1.25
    h = 1.6
    br = 1.6
    achsen = dict(breite=br, hoehe=h, yticks="0;5;10", xmarks=False)
    a = s.achsen((-2, 2), (0, 12), mitte=(xm[0] + 0.1, yk), xl="", yl="E/E_0", xzahlen=False, **achsen)
    s.text(a, "k_x, k_y", (0, -1.6), groesse=GR, ausrichtung="center")
    for e, f in ((1, BLAU), (4, GRUEN), (9, ORANGE)):
        s.kurve(a, "%g+1.6*x*x" % e, x=(-sqrt((12 - e) / 1.6), sqrt((12 - e) / 1.6)), farbe=f, dicke=4)
    b = s.achsen((-2, 2), (0, 12), mitte=(xm[1] + 0.1, yk), xl="", yl="", xzahlen=False, **achsen)
    s.text(b, "k_x", (0, -1.6), groesse=GR, ausrichtung="center")
    for e, f in ((2, BLAU), (5, GRUEN), (8, ORANGE)):
        s.kurve(b, "%g+1.6*x*x" % e, x=(-sqrt((12 - e) / 1.6), sqrt((12 - e) / 1.6)), farbe=f, dicke=4)
    s.text(b, "2\\times", (0.0, 6.0), groesse=22, ausrichtung="center", farbe=GRUEN)
    c = s.achsen((-2, 2), (0, 12), mitte=(xm[2] + 0.1, yk), xl="", yl="", xzahlen=False, **achsen)
    for e, f, m_ in ((3, BLAU, ""), (6, GRUEN, "3\\times"), (9, ORANGE, "3\\times"), (11, ROT, "3\\times")):
        s.linie(c, (-1.3, e), (1.3, e), farbe=f, dicke=5)
        if m_:
            s.text(c, m_, (0.0, e + 0.6), groesse=22, ausrichtung="center", farbe=f)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k2dichte():
    """Zählen in der Ebene der Quantenzahlen; wirkliche Niveaus und mittlere Dichte in 1D, 2D, 3D."""
    s = Szene("gemb1/k2dichte")
    a = s.achsen((0, 7.5), (0, 7.5), breite=2.3, hoehe=2.3, mitte=(-2.1, 0.0), xl="n_x", yl="n_y", xticks="0;2;4;6", yticks="0;2;4;6")
    R = 6.0
    poly(s, a, [(0, 0)] + [(R * cos(pi / 2 * i / 60), R * sin(pi / 2 * i / 60)) for i in range(61)], BLAU, deckung=0.12)
    s.daten(a, [(R * cos(pi / 2 * i / 60), R * sin(pi / 2 * i / 60)) for i in range(61)], farbe=BLAU, dicke=4)
    for i in range(1, 8):
        for j in range(1, 8):
            innen = i * i + j * j <= R * R
            s.punkt(a, i, j, r=0.05, farbe=ROT if innen else HELLGRAU)
    s.text(a, "n'", (4.55, 4.52), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.linie(a, (0, 0), (R * cos(0.8), R * sin(0.8)), farbe=BLAU, dicke=2, dash=DASH)
    # Wirkliche Niveaus einer leicht unsymmetrischen Box, damit keine Entartung die Dichte verdeckt
    emax = 60.0
    r2, r3 = 1.17, 1.31
    n1 = sorted(n * n for n in range(1, 9) if n * n <= emax)
    n2 = sorted(a_ * a_ + b_ * b_ / r2 ** 2 for a_ in range(1, 9) for b_ in range(1, 10))
    n3 = sorted(a_ * a_ + b_ * b_ / r2 ** 2 + c_ * c_ / r3 ** 2 for a_ in range(1, 9) for b_ in range(1, 10) for c_ in range(1, 12))
    streifen = (("1D", n1, 1.45), ("2D", n2, 1.12), ("3D", n3, 0.79))
    xb, br = 1.85, 2.9
    for name, e, y in streifen:
        h = s.achsen((0, emax), (0, 1), breite=br, hoehe=0.26, mitte=(xb, y), xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, unsichtbar=True)
        kamm = []
        for v in e:
            if v <= emax:
                kamm += [(v, 0), (v, 1), (v, 0)]
        s.daten(h, kamm, farbe=GRAU, dicke=1.2)
        s.text(h, name, (-2.0, 0.5), groesse=GR, ausrichtung="right", farbe=SCHWARZ)
    c = s.achsen((0, emax), (0, 2.4), breite=br, hoehe=1.35, mitte=(xb, -0.72), xl="E", yl="D(E)", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.kurve(c, "sqrt(30/x)", x=(5.3, emax), farbe=ORANGE, dicke=4)
    s.kurve(c, "1", x=(0, emax), farbe=GRUEN, dicke=4)
    s.kurve(c, "sqrt(x/30)", x=(0.05, emax), farbe=BLAU, dicke=4)
    s.text(c, "1D: E^{-1/2}", (16, 2.1), groesse=GR, ausrichtung="left", farbe=ORANGE)
    s.text(c, "2D: E^0", (3, 1.17), groesse=GR, ausrichtung="left", farbe=GRUEN)
    s.text(c, "3D: E^{1/2}", (58, 1.75), groesse=GR, ausrichtung="right", farbe=BLAU)
    s.speichern()


if __name__ == "__main__":
    k2gitter()
    k2kosinus()
    k2box()
    k2schach()
    k2entartung()
    k2knoten()
    k2film()
    k2dichte()
