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
    """Die Linse in zwei Beschreibungen (seit 04.11.2026 ohne die Kreisscheibe; die steht in k2kreis)."""
    s = Szene("hm3/k2normal")
    w, h = 2.0, 2.0
    a = s.achsen((0, 1, 1), (0, 1, 1), breite=w, hoehe=h, mitte=(-1.6, 0), xl="x", yl="y", xl_mitte=False, titel=s.tr("t2", "Typ 2", "Type 2", "Tipo 2", "第 2 型"), titel_mitte=True)
    s.flaeche(a, "x", 0, 1, f2="x^2", farbe=BLAU, deckung=0.2)
    s.kurve(a, "x", x=(0, 1), farbe=BLAU, dicke=4)
    s.kurve(a, "x^2", x=(0, 1), farbe=GRUEN, dicke=4)
    x0 = 0.5
    s.flaeche(a, "x", x0 - 0.03, x0 + 0.03, f2="x^2", farbe=ROT, deckung=0.75)
    s.text(a, "ν = x", (0.22, 0.72), KL, "center", BLAU)
    s.text(a, "μ = x²", (0.78, 0.22), KL, "center", GRUEN)
    b = s.achsen((0, 1, 1), (0, 1, 1), breite=w, hoehe=h, mitte=(1.6, 0), xl="x", yl="y", xl_mitte=False, titel=s.tr("t1", "Typ 1", "Type 1", "Tipo 1", "第 1 型"), titel_mitte=True)
    s.flaeche(b, "x", 0, 1, f2="x^2", farbe=BLAU, deckung=0.2)
    s.kurve(b, "x", x=(0, 1), farbe=BLAU, dicke=4)
    s.kurve(b, "x^2", x=(0, 1), farbe=GRUEN, dicke=4)
    y0 = 0.42
    s.band(b, y0, sqrt(y0), y0 - 0.025, y0 + 0.025, farbe=ROT, deckung=0.75)
    s.text(b, "α = y", (0.2, 0.72), KL, "center", BLAU)
    s.text(b, "β = √y", (0.78, 0.22), KL, "center", GRUEN)
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


# ------------------------------------------------------------------ neu seit der Überarbeitung (04.11.2026)
KLEIN = 22


def k2gleich():
    """1/t auf (0, 1]: zwei Fenster der Breite 0,1 mit sehr verschiedenen Änderungen."""
    s = Szene("hm3/k2gleich")
    a = s.achsen((0, 1.12), (0, 8.6), breite=5.0, hoehe=3.0, mitte=(-0.45, 0), xl="t", yl="1/t", xticks="0.25;0.5;0.75;1",
                 yticks="1;2;4;6;8", zahl=KLEIN)
    s.band(a, 0.15, 0.25, 0, 1 / 0.15, farbe=ROT, deckung=0.15)
    s.band(a, 0.9, 1.0, 0, 1 / 0.9, farbe=BLAU, deckung=0.2)
    s.kurve(a, "1/x", x=(0.118, 1.1), farbe=SCHWARZ, dicke=4)
    s.linie(a, (0.27, 4), (0.27, 1 / 0.15), farbe=ROT, dicke=5)
    s.linie(a, (0.25, 4), (0.29, 4), farbe=ROT, dicke=2)
    s.linie(a, (0.15, 1 / 0.15), (0.29, 1 / 0.15), farbe=ROT, dicke=2)
    s.text(a, s.tr("a1", "Änderung 2.67", "change 2.67", "cambio 2.67", "变化 2.67"), (0.31, 5.0), KL, "left", ROT)
    s.linie(a, (1.03, 1), (1.03, 1 / 0.9), farbe=BLAU, dicke=5)
    s.text(a, s.tr("a2", "Änderung 0.11", "change 0.11", "cambio 0.11", "变化 0.11"), (0.95, 1.9), KL, "center", BLAU)
    s.text(a, "δ = 0.1", (0.2, 7.3), KL, "center", ROT)
    s.speichern()


def k2spitze():
    """Die Kurven (1/x) e^(-t/x) für x = 1, 1/2, 1/5: die Fläche sammelt sich in einer Spitze bei t = 0."""
    s = Szene("hm3/k2spitze")
    a = s.achsen((0, 1.05), (0, 5.4), breite=5.0, hoehe=3.0, mitte=(-0.6, 0), xl="t", yl="f(x, t)", xticks="0.5;1", yticks="1;2;5", zahl=KLEIN)
    s.flaeche(a, "exp(-x)", 0, 1, farbe=BLAU, deckung=0.12)
    s.kurve(a, "exp(-x)", x=(0, 1), farbe=BLAU, dicke=4)
    s.kurve(a, "2*exp(-2*x)", x=(0, 1), farbe=ORANGE, dicke=4)
    s.kurve(a, "5*exp(-5*x)", x=(0, 1), farbe=ROT, dicke=4)
    s.tr("fl", "Fläche", "area", "área", "面积")
    s.text(a, "x = 1: @{fl} 0.632", (0.55, 0.85), KL, "left", BLAU)
    s.text(a, "x = 1/2: @{fl} 0.865", (0.33, 1.45), KL, "left", ORANGE)
    s.text(a, "x = 1/5: @{fl} 0.993", (0.13, 3.6), KL, "left", ROT)
    s.speichern()


def k2dach():
    """e^(-t) cos(xt) für x = 0, 2, 5 zwischen -e^(-t) und e^(-t)."""
    s = Szene("hm3/k2dach")
    a = s.achsen((0, 5.3), (-1.1, 1.15), breite=5.6, hoehe=3.0, mitte=(-0.2, 0), xl="t", xticks="1;2;3;4;5", yticks="-1;-0.5;0.5;1",
                 kreuz=True, zahl=KLEIN)
    s.kurve(a, "exp(-x)", x=(0, 5), farbe=GRAU, dicke=3)
    s.kurve(a, "exp(-x)*cos(2*x)", x=(0, 5), farbe=BLAU, dicke=3)
    s.kurve(a, "exp(-x)*cos(5*x)", x=(0, 5), farbe=GRUEN, dicke=3)
    s.kurve(a, "exp(-x)", x=(0, 5), farbe=ROT, dicke=4, dash=DASH)
    s.kurve(a, "-exp(-x)", x=(0, 5), farbe=ROT, dicke=4, dash=DASH)
    s.text(a, "g(t) = e^{−t}", (0.55, 0.85), KL, "left", ROT)
    s.text(a, "−g(t)", (0.55, -0.85), KL, "left", ROT)
    s.text(a, "x = 2", (2.2, 0.3), KL, "left", BLAU)
    s.text(a, "x = 5", (3.25, -0.5), KL, "left", GRUEN)
    s.speichern()


def k2flucht():
    """Drei Fluchtwege der Fläche: nach oben, in die Breite, nach rechts."""
    s = Szene("hm3/k2flucht")
    w, h = 1.65, 1.7
    t1 = s.tr("ob", "nach oben", "upwards", "hacia arriba", "向上")
    t2 = s.tr("br", "in die Breite", "into the width", "a lo ancho", "向宽处")
    t3 = s.tr("re", "nach rechts", "to the right", "hacia la derecha", "向右")
    a = s.achsen((0, 3), (0, 4.3), breite=w, hoehe=h, mitte=(-2.3, 0), xl="t", xl_mitte=False, xticks="1;2;3", yticks="1;2;4",
                 titel=t1, titel_mitte=True, zahl=KLEIN)
    for f, farbe in (("exp(-x)", BLAU), ("2*exp(-2*x)", ORANGE), ("4*exp(-4*x)", ROT)):
        s.kurve(a, f, x=(0, 3), farbe=farbe, dicke=3)
    b = s.achsen((0, 12), (0, 1.05), breite=w, hoehe=h, mitte=(0.0, 0), xl="t", xl_mitte=False, xticks="4;8;12", yticks="0.25;0.5;1",
                 titel=t2, titel_mitte=True, zahl=KLEIN)
    for f, farbe in (("exp(-x)", BLAU), ("0.5*exp(-0.5*x)", ORANGE), ("0.25*exp(-0.25*x)", ROT)):
        s.kurve(b, f, x=(0, 12), farbe=farbe, dicke=3)
    c = s.achsen((0, 7.5), (0, 1.1), breite=w, hoehe=h, mitte=(2.3, 0), xl="t", xl_mitte=False, xticks="1;3;6", yticks="1",
                 titel=t3, titel_mitte=True, zahl=KLEIN)
    s.daten(c, [(0, 0), (1, 1), (2, 0), (7.5, 0)], farbe=BLAU, dicke=3)
    s.daten(c, [(2, 0), (3, 1), (4, 0)], farbe=ORANGE, dicke=3)
    s.daten(c, [(5, 0), (6, 1), (7, 0)], farbe=ROT, dicke=3)
    s.speichern()


def k2riemann():
    """Säulensumme über einem Gitter: zeilenweise oder spaltenweise addiert."""
    s = Szene("hm3/k2riemann")
    a = s.welt()
    d = 0.55
    oy = -0.55
    zeile = s.tr("zl", "erst jede Zeile (über x),\ndann die Zeilen addieren", "first each row (over x),\nthen add the rows",
                 "primero cada fila (sobre x),\nluego sumar las filas", "先对每一行（对 x）求和，\n再把各行相加")
    spalte = s.tr("sp", "erst jede Spalte (über y),\ndann die Spalten addieren", "first each column (over y),\nthen add the columns",
                  "primero cada columna (sobre y),\nluego sumar las columnas", "先对每一列（对 y）求和，\n再把各列相加")
    for ox, zeilen, txt in ((-3.25, True, zeile), (0.75, False, spalte)):
        def P(x, y):
            return (ox + d * x, oy + d * y)
        if zeilen:
            for k in range(3):
                polygon(s, a, [P(0, k), P(4, k), P(4, k + 1), P(0, k + 1)], fuellung=BLAU, deckung=0.28 if k % 2 == 0 else 0.1, farbe=BLAU, dicke=0)
        else:
            for j in range(4):
                polygon(s, a, [P(j, 0), P(j + 1, 0), P(j + 1, 3), P(j, 3)], fuellung=ORANGE, deckung=0.35 if j % 2 == 0 else 0.14, farbe=ORANGE, dicke=0)
        for j in range(5):
            s.linie(a, P(j, 0), P(j, 3), farbe=GRAU, dicke=2)
        for k in range(4):
            s.linie(a, P(0, k), P(4, k), farbe=GRAU, dicke=2)
        for j in range(4):
            for k in range(3):
                s.punkt(a, *P(j + 0.5, k + 0.5), farbe=SCHWARZ, r=0.045)
        if zeilen:
            for k in range(3):
                s.pfeil(P(0.12, k + 0.5), P(3.88, k + 0.5), "", farbe=BLAU, dicke=3, spitze=0.12)
        else:
            for j in range(4):
                s.pfeil(P(j + 0.5, 0.12), P(j + 0.5, 2.88), "", farbe=ORANGE, dicke=3, spitze=0.12)
        s.pfeil(P(0, 0), P(4.6, 0), "", farbe=SCHWARZ, dicke=2, spitze=0.12)
        s.pfeil(P(0, 0), P(0, 3.6), "", farbe=SCHWARZ, dicke=2, spitze=0.12)
        s.text(a, "x", (P(4.6, 0)[0], P(4.6, 0)[1] - 0.3), KL, "center")
        s.text(a, "y", (P(0, 3.6)[0] - 0.2, P(0, 3.6)[1] - 0.15), KL, "center")
        s.text(a, txt, (P(2, 0)[0], oy - 0.3), KLEIN, "center")
    s.speichern()


def k2fortsetzung():
    """Menge M im Quader Q, rechts die Fortsetzung durch null längs einer Linie mit festem y."""
    s = Szene("hm3/k2fortsetzung")
    a = s.welt()
    S, o = 0.6, (-3.35, -0.82)

    def P(x, y):
        return (o[0] + S * x, o[1] + S * y)
    polygon(s, a, [P(0, 0), P(4, 0), P(4, 2.6), P(0, 2.6)], fuellung="#ffffff", deckung=0.0, farbe=GRAU, dicke=2)
    polygon(s, a, [P(2 + 1.4 * cos(2 * pi * k / 72), 1.3 + 0.95 * sin(2 * pi * k / 72)) for k in range(72)], fuellung=BLAU, deckung=0.15,
            farbe=BLAU, dicke=3)
    s.text(a, "M", P(2, 0.62), 26, "center", BLAU)
    s.text(a, s.tr("qu", "Quader Q", "box Q", "caja Q", "长方体 Q"), (P(4, 2.6)[0], P(4, 2.6)[1] + 0.12), KLEIN, "right")
    s.linie(a, P(0, 1.6), P(4, 1.6), farbe=ROT, dicke=3, dash=DASH)
    s.text(a, s.tr("yf", "y fest", "y fixed", "y fijo", "固定 y"), (P(4, 1.6)[0] + 0.08, P(4, 1.6)[1] - 0.1), KLEIN, "left", ROT)
    for xx in (0.672, 3.328):
        s.punkt(a, *P(xx, 1.6), farbe=ROT, r=0.06)
    # rechts: f-quer längs der Linie
    mx, my, bw, bh, xr, yr = 1.8, -0.05, 2.75, 1.7, 4.3, 2.2
    b = s.achsen((0, xr), (0, yr), breite=bw, hoehe=bh, mitte=(mx, my), xl="x", xl_mitte=False, xticks="", yticks="", xzahlen=False,
                 yzahlen=False, xmarks=False, ymarks=False)

    def W(x, y):
        return (mx - bw / 2 + bw * x / xr, my - bh / 2 + bh * y / yr)
    s.daten(b, [(0, 0), (0.672, 0)], farbe=ROT, dicke=5)
    s.kurve(b, "1.1+0.45*sin(1.6*x)", x=(0.672, 3.328), farbe=ROT, dicke=5)
    s.daten(b, [(3.328, 0), (4.1, 0)], farbe=ROT, dicke=5)
    for xx in (0.672, 3.328):
        yy = 1.1 + 0.45 * sin(1.6 * xx)
        s.linie(a, W(xx, 0), W(xx, yy), farbe=ROT, dicke=2, dash=DASH)
        s.punkt(a, *W(xx, yy), farbe=ROT, r=0.06)
        s.kreis(a, *W(xx, 0), 0.06, farbe=ROT, dicke=3, fuellung="#ffffff", deckung=1.0)
        s.text(a, s.tr("sp", "Sprung", "jump", "salto", "跳跃"), (W(xx, 0)[0], W(xx, 0)[1] - 0.3), KLEIN, "center", ROT)
    s.text(a, s.tr("fq", "f̄ längs der Linie", "f̄ along the line", "f̄ a lo largo de la recta", "沿该直线的 f̄"), (mx, my + bh / 2 + 0.12), KLEIN,
           "center", ROT)
    s.speichern()


def k2kreis():
    """Kreisscheibe mit Radius 2: Mittelstreifen vom Typ 1, zwei Kappen vom Typ 2."""
    s = Szene("hm3/k2kreis")
    a = s.welt()
    S, c = 0.85, (-0.7, 0.0)
    q, n = sqrt(2), 40

    def P(x, y):
        return (c[0] + S * x, c[1] + S * y)

    def bogen(w0, w1):
        return [P(2 * cos(radians(w0 + (w1 - w0) * k / n)), 2 * sin(radians(w0 + (w1 - w0) * k / n))) for k in range(n + 1)]
    polygon(s, a, bogen(-45, 45) + bogen(135, 225), fuellung=BLAU, deckung=0.22, farbe=BLAU, dicke=0)
    polygon(s, a, bogen(45, 135), fuellung=ORANGE, deckung=0.35, farbe=ORANGE, dicke=0)
    polygon(s, a, bogen(225, 315), fuellung=ORANGE, deckung=0.35, farbe=ORANGE, dicke=0)
    s.kreis(a, c[0], c[1], 2 * S, farbe=SCHWARZ, dicke=3)
    s.linie(a, P(-q, q), P(q, q), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, P(-q, -q), P(q, -q), farbe=GRAU, dicke=2, dash=DASH)
    s.pfeil(P(-2.5, 0), P(2.7, 0), "", farbe=GRAU, dicke=2, spitze=0.12)
    s.pfeil(P(0, -2.5), P(0, 2.7), "", farbe=GRAU, dicke=2, spitze=0.12)
    s.text(a, "x", (P(2.7, 0)[0], P(2.7, 0)[1] - 0.3), KL, "center")
    s.text(a, "y", (P(0, 2.7)[0] - 0.2, P(0, 2.7)[1] - 0.15), KL, "center")
    t1 = s.tr("ty1", "Typ 1", "Type 1", "Tipo 1", "第 1 型")
    t2 = s.tr("ty2", "Typ 2", "Type 2", "Tipo 2", "第 2 型")
    s.text(a, t1, P(0.95, 0.35), KLEIN, "center", BLAU)
    s.text(a, t2, P(0.5, 1.68), KLEIN, "center", ORANGE)
    s.text(a, "@ty2", P(0.5, -1.66), KLEIN, "center", ORANGE)
    s.text(a, "y = √2", (P(2.05, q)[0], P(2.05, q)[1] - 0.1), KLEIN, "left")
    s.text(a, "y = −√2", (P(2.05, -q)[0], P(2.05, -q)[1] - 0.1), KLEIN, "left")
    s.speichern()


for f in (k2schar, k2leibniz, k2sprung, k2majorante, k2fubini, k2cavalieri, k2normal, k2raum,
          k2gleich, k2spitze, k2dach, k2flucht, k2riemann, k2fortsetzung, k2kreis):
    f()
