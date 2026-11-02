"""Abbildungen zu Höhere Mathematik 3, Teil 2: Integralrechnung im R^n.

Aufruf: python tools/szenen/hm3_teil2.py, danach python tools/szenen_ansehen.py out.png hm3/k2schar ... [--lang de]
Alle Zahlen stehen im Heft und in C:/Bücher/HöMa3/Arbeitshefte/rechnung_kap2.py.
"""
import sys
from math import cos, exp, pi, radians, sin, sqrt
from pathlib import Path

import numpy as np
from scipy.special import sici

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24
HELLBLAU = "#8fb4e3"


def polygon(s, a, pkte, fuellung=BLAU, deckung=0.2, farbe=SCHWARZ, dicke=0, dash=""):
    """Gefüllte Fläche aus Punkten (Shape des Editors)."""
    pl = ";".join("%.4f,%.4f" % (x, y) for x, y in pkte)
    return s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": farbe, "fill_color": fuellung,
                            "fill_opacity": deckung, "stroke_width": dicke, "dash": dash}, a)


def kamera(az, el, skala, ursprung):
    """Parallelprojektion: Blick aus Richtung (az, el), z zeigt nach oben. Liefert p(x, y, z) -> (u, v)."""
    a, e = radians(az), radians(el)

    def p(x, y, z):
        u = -x * sin(a) + y * cos(a)
        v = -x * cos(a) * sin(e) - y * sin(a) * sin(e) + z * cos(e)
        return (ursprung[0] + skala * u, ursprung[1] + skala * v)
    return p


def k2schar():
    s = Szene("hm3/k2schar")
    a = s.achsen((0, 1, 0.5), (0, 1.25, 0.5), breite=2.6, hoehe=1.9, mitte=(-1.95, 0), xl="t", yl="f(x, t)")
    s.flaeche(a, "exp(-x)", 0, 1, farbe=BLAU, deckung=0.18)
    s.flaeche(a, "exp(-3*x)", 0, 1, farbe=ROT, deckung=0.22)
    s.kurve(a, "1", x=(0, 1), farbe=GRAU, dicke=4)
    s.kurve(a, "exp(-x)", x=(0, 1), farbe=BLAU)
    s.kurve(a, "exp(-3*x)", x=(0, 1), farbe=ROT)
    s.text(a, "x = 0", (0.68, 1.09), KL, "left", GRAU)
    s.text(a, "x = 1", (0.68, 0.61), KL, "left", BLAU)
    s.text(a, "x = 3", (0.68, 0.22), KL, "left", ROT)
    b = s.achsen((0, 4, 1), (0, 1.25, 0.5), breite=2.6, hoehe=1.9, mitte=(1.95, 0), xl="x", yl="F(x)")
    F1, F3, Sf = (1 - exp(-1)), (1 - exp(-3)) / 3, 2 / exp(1) - 1
    s.kurve(b, "(1-exp(-x))/x", x=(0.001, 4), farbe=SCHWARZ, dicke=4)
    s.linie(b, (0.0, F1 - Sf), (2.9, F1 + 1.9 * Sf), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(b, 0, 1, farbe=GRAU, r=0.085)
    s.punkt(b, 1, F1, farbe=BLAU, r=0.085)
    s.punkt(b, 3, F3, farbe=ROT, r=0.085)
    s.text(b, "F(0) = 1", (0.28, 1.1), KL, "left", GRAU)
    s.text(b, "F(1) = 0.632", (1.1, 0.82), KL, "left", BLAU)
    s.text(b, "F(3) = 0.317", (2.3, 0.47), KL, "left", ROT)
    s.speichern()


def k2leibniz():
    s = Szene("hm3/k2leibniz")
    a = s.achsen((0, 5.2), (0, 2.6), breite=5.6, hoehe=2.45, mitte=(-0.1, -0.2), xl="x", xl_mitte=False, yl="f", xmarks=False, ymarks=False,
                 xticks="", yticks="", xzahlen=False, yzahlen=False)
    f1, f2 = "1.05+0.3*sin(x)", "1.5+0.3*sin(x)"
    al0, al1, be0, be1 = 1.0, 1.5, 3.2, 3.9
    s.flaeche(a, f1, al1, be0, farbe=BLAU, deckung=0.1)
    s.flaeche(a, f2, al1, be0, f2=f1, farbe=ORANGE, deckung=0.42)
    s.flaeche(a, f2, be0, be1, farbe=GRUEN, deckung=0.38)
    s.flaeche(a, f1, al0, al1, farbe=ROT, deckung=0.38)
    s.kurve(a, f1, x=(0.35, 4.75), farbe=BLAU, dicke=4)
    s.kurve(a, f2, x=(0.35, 4.75), farbe=BLAU, dicke=3, dash=DASH)
    s.text(a, "f(x, y)", (4.05, 0.95), KL, "left", BLAU)
    s.text(a, "f(x, y + Δy)", (3.95, 1.56), KL, "left", BLAU)
    for x in (al0, al1, be0, be1):
        s.linie(a, (x, 0), (x, -0.08), dicke=3)
    s.text(a, "α(y)", (al0 - 0.02, -0.3), KL, "right", ROT)
    s.text(a, "β(y)", (be0 + 0.02, -0.3), KL, "right", GRUEN)
    s.text(a, "α + α′Δy", (al1 - 0.08, -0.3), KL, "left", ROT)
    s.text(a, "β + β′Δy", (be1 - 0.12, -0.3), KL, "left", GRUEN)
    s.text(a, "Δy ∫ ∂f/∂y dx", (2.35, 2.05), KL, "center", ORANGE)
    s.linie(a, (2.35, 1.95), (2.35, 1.63), farbe=ORANGE, dicke=2)
    s.text(a, "+ f(β, y) β′ Δy", (3.7, 2.3), KL, "center", GRUEN)
    s.linie(a, (3.55, 2.18), (3.55, 1.25), farbe=GRUEN, dicke=2)
    s.text(a, "− f(α, y) α′ Δy", (0.75, 2.3), KL, "center", ROT)
    s.linie(a, (1.25, 2.18), (1.25, 1.0), farbe=ROT, dicke=2)
    s.speichern()


def si(v):
    return float(sici(v)[0])


def k2sprung():
    s = Szene("hm3/k2sprung")
    a = s.achsen((0, 40, 10), (0, 2, 0.5), breite=2.2, hoehe=1.75, mitte=(-2.0, 0), xl="T", xl_mitte=False, yticks="0.5;1;1.5;2", yl="F_T(x)")
    s.linie(a, (0, pi / 2), (40, pi / 2), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "π/2", (40.6, pi / 2 - 0.1), KL, "left", GRAU)
    Ts = np.linspace(0, 40, 601)
    s.daten(a, duenn([(float(T), si(T)) for T in Ts], 5e-4), farbe=BLAU)
    s.daten(a, duenn([(float(T), si(0.2 * T)) for T in Ts], 5e-4), farbe=ROT)
    s.text(a, "x = 1", (3.2, 2.02), KL, "left", BLAU)
    s.text(a, "x = 0.2", (18, 1.05), KL, "left", ROT)
    b = s.achsen((-1, 1, 1), (-2, 2, 1), breite=2.2, hoehe=1.75, mitte=(1.62, 0), xl="x", xl_mitte=False, yl="F_T(x)", kreuz=True, xticks="-1;1", yticks="-1;1")
    xs = np.linspace(-1, 1, 2001)
    for T, farbe, dicke in ((5, GRAU, 3), (20, ORANGE, 3), (100, BLAU, 3)):
        s.daten(b, duenn([(float(v), si(T * v)) for v in xs], 2e-4), farbe=farbe, dicke=dicke)
    s.text(b, "T = 5", (-0.92, 0.95), KL, "left", GRAU)
    s.text(b, "T = 20", (0.22, -0.65), KL, "left", ORANGE)
    s.text(b, "T = 100", (0.22, -1.15), KL, "left", BLAU)
    s.speichern()


def k2majorante():
    s = Szene("hm3/k2majorante")
    a = s.achsen((0, 8, 2), (0, 1.1, 0.5), breite=4.8, hoehe=2.3, mitte=(-0.6, 0), xl="t", xl_mitte=False)
    s.flaeche(a, "exp(-0.5*x)", 0, 8, farbe=ROT, deckung=0.1)
    s.kurve(a, "exp(-0.2*x)", x=(0, 8), farbe=GRAU, dicke=3, dash=DASH)
    for x, farbe in ((0.6, BLAU), (1, BLAU), (2, BLAU)):
        s.kurve(a, "exp(-%g*x)" % x, x=(0, 8), farbe=farbe, dicke=3)
    s.kurve(a, "exp(-0.5*x)", x=(0, 8), farbe=ROT, dicke=5)
    s.legende(a, [("g(t) = e^{−t/2}", ROT, "-"), ("x = 0.6 | 1 | 2", BLAU, "-"), ("x = 0.2", GRAU, "--")], (4.3, 1.03))
    s.speichern()


def k2fubini():
    s = Szene("hm3/k2fubini")
    a = s.welt()

    def gebirge(ox, y0=None, x0=None, titel="", farbe=BLAU):
        p0 = kamera(38, 24, 0.9, (ox, -0.95))

        def p(x, y, z):                              # x aus [0, 1] gestreckt, z gestaucht
            return p0(1.7 * x, y, 0.42 * z)

        def h(x, y):
            return 4 - x * x - y * y
        n = 28
        rand = [p(0, -1, 0), p(1, -1, 0), p(1, 1, 0), p(0, 1, 0)]
        polygon(s, a, rand, fuellung=HELLGRAU, deckung=0.35, farbe=GRAU, dicke=2)
        for x, y in ((1, -1), (1, 1), (0, 1)):
            s.linie(a, p(x, y, 0), p(x, y, h(x, y)), farbe=GRAU, dicke=2)
        for i in range(5):
            x = i / 4
            s.daten(a, [p(x, -1 + 2 * k / n, h(x, -1 + 2 * k / n)) for k in range(n + 1)], farbe=HELLBLAU, dicke=2)
        for j in range(9):
            y = -1 + j / 4
            s.daten(a, [p(k / n, y, h(k / n, y)) for k in range(n + 1)], farbe=HELLBLAU, dicke=2)
        if y0 is not None:
            kante = [p(k / n, y0, h(k / n, y0)) for k in range(n + 1)]
            polygon(s, a, [p(0, y0, 0)] + kante + [p(1, y0, 0)], fuellung=farbe, deckung=0.45, farbe=farbe, dicke=3)
        else:
            kante = [p(x0, -1 + 2 * k / n, h(x0, -1 + 2 * k / n)) for k in range(n + 1)]
            polygon(s, a, [p(x0, -1, 0)] + kante + [p(x0, 1, 0)], fuellung=farbe, deckung=0.45, farbe=farbe, dicke=3)
        s.text(a, titel, (ox + 0.1, 1.08), 26, "center", farbe)

    gebirge(-2.0, y0=0.15, titel=s.tr("yf", "y fest: ∫ f dx", "y fixed: ∫ f dx", "y fijo: ∫ f dx", "固定 y：∫ f dx"), farbe=BLAU)
    gebirge(1.9, x0=0.55, titel=s.tr("xf", "x fest: ∫ f dy", "x fixed: ∫ f dy", "x fijo: ∫ f dy", "固定 x：∫ f dy"), farbe=ROT)
    s.speichern()


def k2cavalieri():
    s = Szene("hm3/k2cavalieri")
    a = s.welt()
    S, q = 0.66, 0.27              # Maßstab, Stauchung der Ellipsen

    def kegel(ox, schub, farbe):
        y0 = -1.25

        def mitte(z):
            return (ox + schub * z, y0 + S * z)

        def ell(z, n=48):
            c = mitte(z)
            r = S * 2 * z / 3
            return [(c[0] + r * cos(2 * pi * k / n), c[1] + q * r * sin(2 * pi * k / n)) for k in range(n)]
        for k in range(1, 8):
            polygon(s, a, ell(3 * k / 7), fuellung=BLAU, deckung=0.1, farbe=HELLBLAU, dicke=2)
        r3 = S * 2
        c3 = mitte(3)
        s.linie(a, mitte(0), (c3[0] - r3, c3[1]), farbe=SCHWARZ, dicke=3)
        s.linie(a, mitte(0), (c3[0] + r3, c3[1]), farbe=SCHWARZ, dicke=3)
        polygon(s, a, ell(2), fuellung=farbe, deckung=0.4, farbe=farbe, dicke=3)
        return mitte
    m1 = kegel(-1.95, 0.0, ROT)
    m2 = kegel(1.15, 0.26, ROT)
    z = 2
    s.linie(a, m1(z), (m1(z)[0] + S * 4 / 3, m1(z)[1]), farbe=SCHWARZ, dicke=3)
    s.text(a, "2z/3", (m1(z)[0] + 0.1, m1(z)[1] + 0.13), 24, "left")
    s.pfeil((-3.55, -1.25), (-3.55, 1.0), "", dicke=3, spitze=0.17)
    s.text(a, "z", (-3.42, 0.85), 26)
    s.text(a, s.tr("gl", "gleiche Fläche", "same area", "misma área", "面积相同"), (0.0, 1.3), 24, "center", ROT)
    s.speichern()


def k2normal():
    s = Szene("hm3/k2normal")
    w, h = 1.55, 1.55
    a = s.achsen((0, 1, 1), (0, 1, 1), breite=w, hoehe=h, mitte=(-2.42, 0), xl="x", yl="y", xl_mitte=False, titel=s.tr("t2", "Typ 2", "Type 2", "Tipo 2", "第 2 型"), titel_mitte=True)
    s.flaeche(a, "x", 0, 1, f2="x^2", farbe=BLAU, deckung=0.2)
    s.kurve(a, "x", x=(0, 1), farbe=BLAU, dicke=4)
    s.kurve(a, "x^2", x=(0, 1), farbe=GRUEN, dicke=4)
    x0 = 0.5
    s.flaeche(a, "x", x0 - 0.035, x0 + 0.035, f2="x^2", farbe=ROT, deckung=0.75)
    s.text(a, "ν = x", (0.24, 0.72), KL, "center", BLAU)
    s.text(a, "μ = x²", (0.76, 0.2), KL, "center", GRUEN)
    b = s.achsen((0, 1, 1), (0, 1, 1), breite=w, hoehe=h, mitte=(-0.3, 0), xl="x", yl="y", xl_mitte=False, titel=s.tr("t1", "Typ 1", "Type 1", "Tipo 1", "第 1 型"), titel_mitte=True)
    s.flaeche(b, "x", 0, 1, f2="x^2", farbe=BLAU, deckung=0.2)
    s.kurve(b, "x", x=(0, 1), farbe=BLAU, dicke=4)
    s.kurve(b, "x^2", x=(0, 1), farbe=GRUEN, dicke=4)
    y0 = 0.42
    s.band(b, y0, sqrt(y0), y0 - 0.03, y0 + 0.03, farbe=ROT, deckung=0.75)
    s.text(b, "α = y", (0.2, 0.72), KL, "center", BLAU)
    s.text(b, "β = √y", (0.77, 0.2), KL, "center", GRUEN)
    c = s.achsen((-2.2, 2.2, 2), (-2.2, 2.2, 2), breite=1.7, hoehe=1.7, mitte=(1.95, 0), xl="x", yl="y", xl_mitte=False, kreuz=True, xticks="-2;2", yticks="-2;2",
                 titel=s.tr("zl", "Zerlegung", "decomposition", "descomposición", "分解"), titel_mitte=True)
    q = sqrt(2)
    n = 40
    oben = [(-q + 2 * q * k / n, sqrt(4 - (-q + 2 * q * k / n) ** 2)) for k in range(n + 1)]
    polygon(s, c, oben, fuellung=ORANGE, deckung=0.4, farbe=ORANGE, dicke=3)
    polygon(s, c, [(x, -y) for x, y in oben], fuellung=ORANGE, deckung=0.4, farbe=ORANGE, dicke=3)
    rechts = [(sqrt(4 - v * v), v) for v in (-q + 2 * q * k / n for k in range(n + 1))]
    polygon(s, c, rechts + [(-x, -y) for x, y in rechts], fuellung=BLAU, deckung=0.25, farbe=BLAU, dicke=3)
    s.speichern()


def k2raum():
    s = Szene("hm3/k2raum")
    a = s.welt()
    p = kamera(42, 22, 0.95, (-0.75, -0.85))
    n = 48

    def w(x):
        return sqrt(max(4 - x * x, 0.0))
    xs = [2 * k / n for k in range(n + 1)]
    # Schatten D in z = 0
    polygon(s, a, [p(0, 0, 0)] + [p(x, w(x), 0) for x in xs], fuellung=ORANGE, deckung=0.35, farbe=ORANGE, dicke=3)
    # Seite y = sqrt(4 - x^2), Deckel z = sqrt(4 - x^2)
    polygon(s, a, [p(x, w(x), 0) for x in xs] + [p(x, w(x), w(x)) for x in reversed(xs)], fuellung=BLAU, deckung=0.1, farbe=HELLBLAU, dicke=2)
    polygon(s, a, [p(x, 0, w(x)) for x in xs] + [p(x, w(x), w(x)) for x in reversed(xs)], fuellung=BLAU, deckung=0.24, farbe=BLAU, dicke=3)
    # Achsen
    s.pfeil(p(0, 0, 0), p(2.5, 0, 0), "", dicke=3, spitze=0.17)
    s.pfeil(p(0, 2, 0), p(0, 2.6, 0), "", dicke=3, spitze=0.17)
    s.linie(a, p(0, 0, 0), p(0, 2, 0), dicke=3, dash=DASH)
    s.pfeil(p(0, 0, 2), p(0, 0, 2.6), "", dicke=3, spitze=0.17)
    s.linie(a, p(0, 0, 0), p(0, 0, 2), dicke=3, dash=DASH)
    u = p(2.6, 0, 0)
    s.text(a, "x", (u[0] - 0.05, u[1] - 0.26), 26, "center")
    u = p(0, 2.72, 0)
    s.text(a, "y", (u[0] + 0.02, u[1] + 0.03), 26)
    u = p(0, 0, 2.7)
    s.text(a, "z", (u[0] + 0.12, u[1] - 0.03), 26)
    # Stab
    x0, y0 = 0.7, 1.35
    s.linie(a, p(x0, y0, 0), p(x0, y0, w(x0)), farbe=ROT, dicke=5)
    s.punkt(a, *p(x0, y0, 0), farbe=ROT, r=0.08)
    s.punkt(a, *p(x0, y0, w(x0)), farbe=ROT, r=0.08)
    u = p(x0, y0, 0)
    s.text(a, "(x, y)", (u[0] + 0.1, u[1] - 0.27), KL, "left", ROT)
    # Beschriftung rechts daneben
    s.text(a, s.tr("de", "Deckel: z = √(4 − x²)", "lid: z = √(4 − x²)", "tapa: z = √(4 − x²)", "顶：z = √(4 − x²)"), (0.8, 0.95), KL, "left", BLAU)
    s.text(a, s.tr("bo", "Boden: z = 0", "floor: z = 0", "suelo: z = 0", "底：z = 0"), (0.8, 0.53), KL, "left", SCHWARZ)
    s.text(a, s.tr("sc", "Schatten D", "shadow D", "sombra D", "投影 D"), (0.8, 0.11), KL, "left", ORANGE)
    s.speichern()


for f in (k2schar, k2leibniz, k2sprung, k2majorante, k2fubini, k2cavalieri, k2normal, k2raum):
    f()
