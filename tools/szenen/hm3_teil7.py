"""Abbildungen zu Höhere Mathematik 3, Teil 7: Fourier-Reihen."""
import sys
from math import cos, sin, pi, exp, sqrt, log, atan2
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

ZWEIPI = 2 * pi
PI_S, ZWEI_S = "%.5f" % pi, "%.5f" % ZWEIPI


def rechteck_summe(N, faktor="4/pi"):
    """T_N q als Ausdruck: 4/pi * Summe über ungerade k <= N von sin(kx)/k."""
    return faktor + "*(" + "+".join("sin(%d*x)/%d" % (k, k) for k in range(1, N + 1, 2)) + ")"


def saege_summe(N):
    return "+".join("sin(%d*x)/%d" % (k, k) for k in range(1, N + 1))


def pi_marken(s, a, y, zweipi=True, minus=False, groesse=24):
    """Beschriftung der Stellen 0, π, 2π (bzw. -π, 0, π) unter der Achse."""
    s.text(a, "0", (0, y), groesse=groesse, ausrichtung="center")
    s.text(a, "π", (pi, y), groesse=groesse, ausrichtung="center")
    if zweipi:
        s.text(a, "2π", (ZWEIPI, y), groesse=groesse, ausrichtung="center")
    if minus:
        s.text(a, "−π", (-pi, y), groesse=groesse, ausrichtung="center")


def k7ortho():
    """Verschiedene Frequenzen: Fläche hebt sich auf. Gleiche Frequenz: Mittelwert 1/2."""
    s = Szene("hm3/k7ortho")
    a = s.achsen((0, ZWEIPI), (-1.2, 1.2), breite=2.7, hoehe=1.8, mitte=(-1.7, 0), xticks="0;%s;%s" % (PI_S, ZWEI_S), yticks="-1;0;1", xzahlen=False,
                 titel="cos x · cos 2x", xl="x", xl_mitte=False)
    s.linie(a, (0, 0), (ZWEIPI, 0), farbe=HELLGRAU, dicke=2)
    s.flaeche(a, "cos(x)*cos(2*x)", 0, ZWEIPI, farbe=BLAU, deckung=0.22)
    s.kurve(a, "cos(x)*cos(2*x)", farbe=BLAU, dicke=4)
    pi_marken(s, a, -1.52)
    b = s.achsen((0, ZWEIPI), (-1.2, 1.2), breite=2.7, hoehe=1.8, mitte=(1.75, 0), xticks="0;%s;%s" % (PI_S, ZWEI_S), yticks="-1;0;1", xzahlen=False,
                 titel="cos x · cos x", xl="x", xl_mitte=False)
    s.linie(b, (0, 0), (ZWEIPI, 0), farbe=HELLGRAU, dicke=2)
    s.flaeche(b, "cos(x)^2", 0, ZWEIPI, farbe=ROT, deckung=0.22)
    s.kurve(b, "cos(x)^2", farbe=ROT, dicke=4)
    s.linie(b, (0, 0.5), (ZWEIPI, 0.5), farbe=SCHWARZ, dicke=3, dash=DASH)
    s.text(b, s.tr("mit", "Mittelwert 1/2", "mean 1/2", "media 1/2", "平均值 1/2"), (pi, -0.55), groesse=24, ausrichtung="center")
    pi_marken(s, b, -1.52)
    s.speichern()


def k7rechteck():
    s = Szene("hm3/k7rechteck")
    a = s.achsen((0, ZWEIPI), (-1.5, 1.5), breite=3.4, hoehe=2.2, mitte=(-1.4, 0), xticks="0;%s;%s" % (PI_S, ZWEI_S), yticks="-1;0;1", xzahlen=False, xl="x", xl_mitte=False)
    s.linie(a, (0, 0), (ZWEIPI, 0), farbe=HELLGRAU, dicke=2)
    s.daten(a, [(0, 1), (pi, 1)], farbe=SCHWARZ, dicke=3)
    s.daten(a, [(pi, -1), (ZWEIPI, -1)], farbe=SCHWARZ, dicke=3)
    s.kurve(a, rechteck_summe(1), farbe=GRUEN, dicke=3)
    s.kurve(a, rechteck_summe(3), farbe=ORANGE, dicke=3)
    s.kurve(a, rechteck_summe(15), farbe=BLAU, dicke=4)
    pi_marken(s, a, -1.83)
    s.text(a, "q", (3.45, 1.05), groesse=26)
    s.text(a, "T_1 q", (1.57, 0.5), groesse=24, farbe=GRUEN, ausrichtung="center")
    s.text(a, "T_3 q", (3.75, -0.32), groesse=24, farbe=ORANGE)
    s.text(a, "T_{15} q", (4.8, -0.32), groesse=24, farbe=BLAU)
    b = s.achsen((0, 10), (0, 1.5), breite=2.05, hoehe=2.2, mitte=(2.1, 0), xticks="1;3;5;7;9", yticks="0;0.5;1;1.5", xl="k", yl="b_k", xl_mitte=False)
    xs = list(range(1, 10))
    s.stems(b, xs, [4 / (pi * k) if k % 2 else 0 for k in xs], farbe=BLAU, dicke=4, r=0.06)
    s.speichern()


def k7regeln():
    s = Szene("hm3/k7regeln")
    a = s.achsen((-pi, pi), (0, 3.5), breite=2.75, hoehe=0.85, mitte=(-1.75, 0.7), xticks="-%s;0;%s" % (PI_S, PI_S), yticks="0;%s" % PI_S, xzahlen=False, yzahlen=False,
                 titel="w")
    s.daten(a, [(-pi, pi), (0, 0), (pi, pi)], farbe=BLAU, dicke=4)
    s.text(a, "π", (-3.42, pi - 0.25), groesse=24, ausrichtung="right")
    s.text(a, s.tr("knick", "Knick", "kink", "pico", "折点"), (0, 1.5), groesse=24, ausrichtung="center")
    b = s.achsen((-pi, pi), (-1.4, 1.4), breite=2.75, hoehe=0.85, mitte=(-1.75, -0.85), xticks="-%s;0;%s" % (PI_S, PI_S), yticks="-1;0;1", xzahlen=False, titel="q = w′")
    s.linie(b, (-pi, 0), (pi, 0), farbe=HELLGRAU, dicke=2)
    s.daten(b, [(-pi, -1), (0, -1)], farbe=ROT, dicke=4)
    s.daten(b, [(0, 1), (pi, 1)], farbe=ROT, dicke=4)
    pi_marken(s, b, -2.2, zweipi=False, minus=True)
    s.text(b, s.tr("sprung", "Sprung", "jump", "salto", "跳变"), (0.25, -0.75), groesse=24)
    c = s.achsen((0, 10), (0, 0.8), breite=2.4, hoehe=2.25, mitte=(1.9, -0.08), xticks="1;3;5;7;9", yticks="0;0.2;0.4;0.6;0.8", xl="k", titel="|c_k|", xl_mitte=False)
    xs = [1, 3, 5, 7, 9]
    s.stems(c, [k + 0.18 for k in xs], [2 / (pi * k * k) for k in xs], farbe=BLAU, dicke=4, r=0.06)
    s.stems(c, [k - 0.18 for k in xs], [2 / (pi * k) for k in xs], farbe=ROT, dicke=4, r=0.06)
    s.text(c, "q: 2/(πk)", (3.9, 0.56), groesse=24, farbe=ROT)
    s.text(c, "w: 2/(πk²)", (3.9, 0.45), groesse=24, farbe=BLAU)
    s.speichern()


def k7saege():
    s = Szene("hm3/k7saege")
    a = s.achsen((-1.3, 7.6), (-2.3, 2.3), breite=6.15, hoehe=2.3, mitte=(0.1, 0.1), xticks="0;1;%.5f;%s" % (ZWEIPI - 1, ZWEI_S), yticks="-1.57080;0;1.57080", xzahlen=False, yzahlen=False,
                 xl="x", xl_mitte=False)
    s.band(a, 1, ZWEIPI - 1, -2.3, 2.3, farbe=BLAU, deckung=0.09)
    s.linie(a, (-1.3, 0), (7.6, 0), farbe=HELLGRAU, dicke=2)
    s.daten(a, [(-1.3, (-pi + 1.3) / 2), (0, -pi / 2)], farbe=SCHWARZ, dicke=3)
    s.daten(a, [(0, pi / 2), (ZWEIPI, -pi / 2)], farbe=SCHWARZ, dicke=3)
    s.daten(a, [(ZWEIPI, pi / 2), (7.6, pi / 2 - (7.6 - ZWEIPI) / 2)], farbe=SCHWARZ, dicke=3)
    s.kurve(a, saege_summe(5), farbe=GRUEN, dicke=3)
    s.kurve(a, saege_summe(25), farbe=BLAU, dicke=4)
    s.punkt(a, 0, 0, farbe=ROT, r=0.08)
    s.punkt(a, ZWEIPI, 0, farbe=ROT, r=0.08)
    y = -2.75
    for x, t in ((0, "0"), (1, "α"), (ZWEIPI - 1, "2π − α"), (ZWEIPI, "2π")):
        s.text(a, t, (x, y), groesse=24, ausrichtung="center" if x != ZWEIPI - 1 else "right")
    s.text(a, "π/2", (-1.42, pi / 2 - 0.12), groesse=24, ausrichtung="right")
    s.text(a, "−π/2", (-1.42, -pi / 2 - 0.12), groesse=24, ausrichtung="right")
    s.text(a, "s", (2.05, 1.05), groesse=26)
    s.text(a, "T_5 s", (3.7, 0.72), groesse=24, farbe=GRUEN)
    s.text(a, "T_{25} s", (0.32, 2.05), groesse=24, farbe=BLAU)
    s.speichern()


def k7projektion():
    s = Szene("hm3/k7projektion")
    a = s.welt()
    pl = "-3.4,-1.4;1.6,-1.4;3.2,0.1;-1.8,0.1"
    s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": BLAU, "fill_color": BLAU, "fill_opacity": 0.13,
                     "stroke_width": 3, "dash": ""}, a)
    T, f, S = (-0.75, -0.7), (-0.75, 1.05), (1.75, -0.4)
    s.linie(a, T, f, farbe=ROT, dicke=4)
    s.linie(a, T, S, farbe=GRUEN, dicke=4)
    s.linie(a, f, S, farbe=SCHWARZ, dicke=3)
    e = 0.2
    v = (S[0] - T[0], S[1] - T[1])
    n = sqrt(v[0] ** 2 + v[1] ** 2)
    u = (v[0] / n * e, v[1] / n * e)
    s.draht((T[0] + u[0], T[1] + u[1]), (T[0] + u[0], T[1] + u[1] + e), (T[0], T[1] + e), farbe=GRAU, dicke=2)
    for p in (T, f, S):
        s.punkt(a, p[0], p[1], r=0.08)
    s.text(a, "f", (f[0] - 0.14, f[1] + 0.12), groesse=28, ausrichtung="right")
    s.text(a, "T_N f", (T[0] - 0.16, T[1] - 0.24), groesse=26, ausrichtung="right")
    s.text(a, "S_N", (S[0] + 0.14, S[1] - 0.26), groesse=26)
    s.text(a, "V_N", (-2.8, -1.2), groesse=26, farbe=BLAU)
    s.text(a, "f − T_N f", (T[0] - 0.14, 0.22), groesse=24, ausrichtung="right", farbe=ROT)
    s.text(a, "T_N f − S_N", (0.75, -0.98), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(a, "f − S_N", (0.62, 0.55), groesse=24)
    s.speichern()


def rest_q(N):
    return 1 - sum(8 / (pi ** 2 * k ** 2) for k in range(1, N + 1, 2))


def rest_w(N):
    n = pi ** 2 / 3
    return 1 - (pi ** 2 / 4 + sum(8 / (pi ** 2 * k ** 4) for k in range(1, N + 1, 2))) / n


def k7energie():
    s = Szene("hm3/k7energie")
    a = s.achsen((0, 12), (0, 1.25), breite=2.45, hoehe=2.1, mitte=(-1.85, 0), xticks="1;3;5;7;9;11", yticks="0;0.5;1", xl="N", titel="‖T_N q‖²", xl_mitte=False)
    xs = [1, 3, 5, 7, 9, 11]
    s.stems(a, xs, [1 - rest_q(N) for N in xs], farbe=BLAU, dicke=2, breite=1.1)
    s.linie(a, (0, 1), (12, 1), farbe=ROT, dicke=3, dash=DASH)
    s.text(a, "‖q‖² = 1", (11.8, 1.12), groesse=24, ausrichtung="right", farbe=ROT)
    b = s.achsen((0, 16), (1e-5, 1), breite=2.45, hoehe=2.1, mitte=(1.8, 0), xticks="1;5;9;13", yticks="0.00001;0.001;0.1;1", ylog=True, xl="N", xl_mitte=False,
                 titel="‖f − T_N f‖² / ‖f‖²")
    xs = list(range(1, 16, 2))
    s.daten(b, [(N, rest_q(N)) for N in xs], farbe=ROT, dicke=3, marker=True)
    s.daten(b, [(N, rest_w(N)) for N in xs], farbe=BLAU, dicke=3, marker=True)
    s.text(b, "f = q", (6.0, 0.13), groesse=24, farbe=ROT)
    s.text(b, "f = w", (7.0, 0.002), groesse=24, farbe=BLAU)
    s.speichern()


KAPPA = 0.443994


def eta(x):
    return exp(1 / (x * x - 1)) / KAPPA if abs(x) < 1 else 0.0


def k7dirac():
    s = Szene("hm3/k7dirac")
    a = s.achsen((-1.5, 1.5), (0, 3.6), breite=2.65, hoehe=2.1, mitte=(-1.95, 0), xticks="-1;0;1", yticks="0;1;2;3", xl="x", xl_mitte=False)
    for e, f in ((1, BLAU), (0.5, GRUEN), (0.25, ROT)):
        s.kurve(a, "where(abs(x/%g)<0.9999,exp(1/((x/%g)^2-1))/%g/%g,0)" % (e, e, KAPPA, e), x=(-1.5, 1.5), farbe=f, dicke=4)
    s.text(a, "ε = 1", (0.62, 1.0), groesse=24, farbe=BLAU)
    s.text(a, "ε = 1/2", (0.45, 1.7), groesse=24, farbe=GRUEN)
    s.text(a, "ε = 1/4", (0.3, 3.2), groesse=24, farbe=ROT)
    b = s.achsen((-2, 2), (0, 2), breite=2.65, hoehe=2.1, mitte=(1.75, 0), xticks="-2;-1;0;1;2", yticks="0;1;2", xl="x", xl_mitte=False)
    s.daten(b, [(-2, 2), (0, 0), (2, 2)], farbe=SCHWARZ, dicke=3)
    e = 0.8
    pts = []
    for i in range(0, 121):
        x = -2 + 4 * i / 120
        m = 400
        su = 0.0
        for j in range(m):
            y = -1 + (2 * j + 1) / m
            su += eta(y) * abs(x - e * y)
        pts.append((x, su * 2 / m))
    s.daten(b, pts, farbe=BLAU, dicke=4)
    s.text(b, "w", (-1.1, 1.5), groesse=26, ausrichtung="right")
    s.text(b, "w_{0.8}", (0.42, 0.28), groesse=24, farbe=BLAU)
    s.speichern()


def dirichlet(N):
    return "1+2*(" + "+".join("cos(%d*x)" % k for k in range(1, N + 1)) + ")"


def k7dirichlet():
    s = Szene("hm3/k7dirichlet")
    a = s.achsen((-pi, pi), (-6, 22), breite=3.05, hoehe=2.2, mitte=(-1.7, 0), xticks="-%s;0;%s" % (PI_S, PI_S), yticks="0;7;21", xzahlen=False, xl="x", xl_mitte=False)
    s.linie(a, (-pi, 0), (pi, 0), farbe=HELLGRAU, dicke=2)
    s.kurve(a, dirichlet(3), farbe=ORANGE, dicke=3)
    s.kurve(a, dirichlet(10), farbe=BLAU, dicke=3)
    pi_marken(s, a, -9.4, zweipi=False, minus=True)
    s.text(a, "D_{10}", (0.55, 19), groesse=24, farbe=BLAU)
    s.text(a, "D_3", (1.05, 6.6), groesse=24, farbe=ORANGE)
    b = s.achsen((-1, 1), (-1.5, 1.5), breite=2.25, hoehe=2.2, mitte=(1.9, 0), xticks="-1;0;1", yticks="-1;0;1", xl="x", xl_mitte=False)
    s.linie(b, (-1, 0), (1, 0), farbe=HELLGRAU, dicke=2)
    s.daten(b, [(-1, -1), (0, -1)], farbe=SCHWARZ, dicke=3)
    s.daten(b, [(0, 1), (1, 1)], farbe=SCHWARZ, dicke=3)
    s.kurve(b, rechteck_summe(9), x=(-1, 1), farbe=GRUEN, dicke=3)
    s.kurve(b, rechteck_summe(39), x=(-1, 1), farbe=BLAU, dicke=3)
    s.punkt(b, 0, 0, farbe=ROT, r=0.09)
    s.text(b, "T_9 q", (0.52, 0.55), groesse=24, farbe=GRUEN)
    s.text(b, "T_{39} q", (-0.92, 0.32), groesse=24, farbe=BLAU)
    s.text(b, s.tr("mw", "Mittelwert 0", "mean 0", "media 0", "平均值 0"), (0.1, -0.42), groesse=24, farbe=ROT)
    s.speichern()


def sup_w(N):
    return 4 / pi * (pi ** 2 / 8 - sum(1 / k ** 2 for k in range(1, N + 1, 2)))


def k7glatt():
    s = Szene("hm3/k7glatt")
    a = s.achsen((0, 26), (0, 1.2), breite=2.55, hoehe=2.1, mitte=(-1.85, 0), xticks="1;9;17;25", yticks="0;0.5;1", xl="N", titel="sup |f − T_N f|", xl_mitte=False)
    xs = list(range(1, 26, 2))
    s.daten(a, [(N, 1.0) for N in xs], farbe=ROT, dicke=3, marker=True)
    s.daten(a, [(N, sup_w(N)) for N in xs], farbe=BLAU, dicke=3, marker=True)
    s.text(a, "f = q", (17, 0.83), groesse=24, farbe=ROT)
    s.text(a, "f = w", (15, 0.2), groesse=24, farbe=BLAU)
    b = s.achsen((0, ZWEIPI), (0, 9), breite=2.55, hoehe=2.1, mitte=(1.7, 0), xticks="0;%s;%s" % (PI_S, ZWEI_S), yticks="0;3;6;9", xzahlen=False, xl="x", xl_mitte=False)
    u = "2*pi+16/pi*(" + "+".join("cos(%d*x)/(%d*%d)" % (k, k * k, 4 * k * k - 1) for k in (1, 3, 5, 7, 9)) + ")"
    s.kurve(b, u, farbe=BLAU, dicke=4)
    s.daten(b, [(0, 0), (pi, pi), (ZWEIPI, 0)], farbe=ROT, dicke=4)
    pi_marken(s, b, -1.65)
    s.text(b, "u", (1.35, 7.9), groesse=26, farbe=BLAU)
    s.text(b, "w", (0.9, 2.1), groesse=26, farbe=ROT)
    s.speichern()


def k7poisson():
    s = Szene("hm3/k7poisson")
    a = s.achsen((-pi, pi), (0, 13), breite=3.0, hoehe=2.2, mitte=(-1.85, 0), xticks="-%s;0;%s" % (PI_S, PI_S), yticks="0;1;4;12", xzahlen=False, xl="φ", xl_mitte=False)
    for r, f in ((0.3, GRUEN), (0.6, ORANGE), (0.85, BLAU)):
        s.kurve(a, "(1-%g^2)/(1-2*%g*cos(x)+%g^2)" % (r, r, r), farbe=f, dicke=4)
    pi_marken(s, a, -2.45, zweipi=False, minus=True)
    s.linie(a, (-pi, 1), (pi, 1), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.text(a, "r = 0.85", (0.5, 10.5), groesse=24, farbe=BLAU)
    s.text(a, "r = 0.6", (0.72, 4.4), groesse=24, farbe=ORANGE)
    s.text(a, "r = 0.3", (1.55, 2.2), groesse=24, farbe=GRUEN)
    b = s.achsen((-1.15, 1.15), (-1.15, 1.15), breite=2.3, hoehe=2.3, mitte=(1.6, 0), unsichtbar=True)
    s.kreis(b, 0, 0, 1, farbe=SCHWARZ, dicke=4, fuellung=BLAU, deckung=0.07)
    for c in (0.1, 0.25, 0.5, 0.75, 0.9):
        w = 2 * c - 1
        if abs(w) < 1e-12:
            s.linie(b, (-sqrt(0.5), -sqrt(0.5)), (sqrt(0.5), sqrt(0.5)), farbe=BLAU, dicke=3)
            s.linie(b, (-sqrt(0.5), sqrt(0.5)), (sqrt(0.5), -sqrt(0.5)), farbe=BLAU, dicke=3)
            continue
        # x^2 - y^2 = w innerhalb des Einheitskreises
        ym = sqrt((1 - abs(w)) / 2)
        for vz in (1, -1):
            pts = []
            for i in range(41):
                t = -ym + 2 * ym * i / 40
                p = sqrt(abs(w) + t * t) * vz
                pts.append((p, t) if w > 0 else (t, p))
            s.daten(b, pts, farbe=BLAU, dicke=3)
    s.text(b, "u = 1", (1.04, -0.05), groesse=24)
    s.text(b, "u = 0", (0, 1.2), groesse=24, ausrichtung="center")
    s.punkt(b, 0, 0, farbe=ROT, r=0.08)
    s.text(b, "u = 1/2", (0.12, 0.03), groesse=24, farbe=ROT)
    s.speichern()


for f in (k7ortho, k7rechteck, k7regeln, k7saege, k7projektion, k7energie, k7dirac, k7dirichlet, k7glatt, k7poisson):
    f()
