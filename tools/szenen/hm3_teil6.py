"""Abbildungen zu Höhere Mathematik 3, Teil 6: Konvergenz von Funktionenfolgen.

Aufruf: python tools/szenen/hm3_teil6.py, danach python tools/szenen_ansehen.py out.png hm3/k6punkt ... [--lang de]
Alle Zahlen stehen im Heft und in C:/Bücher/HöMa3/Arbeitshefte/rechnung_kap6.py.
"""
import sys
from math import cos, exp, pi, sin
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24
HB, MB, DB = "#8fb4e3", "#5f96da", "#1b4f91"


def stuetz(f, x0, x1, n=500):
    return [(x0 + (x1 - x0) * i / n, f(x0 + (x1 - x0) * i / n)) for i in range(n + 1)]


def polygon(s, a, pkte, fuellung=BLAU, deckung=0.2, farbe=SCHWARZ, dicke=0, dash=""):
    pl = ";".join("%.4f,%.4f" % (x, y) for x, y in pkte)
    return s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": farbe, "fill_color": fuellung,
                            "fill_opacity": deckung, "stroke_width": dicke, "dash": dash}, a)


def k6punkt():
    s = Szene("hm3/k6punkt")
    a = s.achsen((0, 1, 0.5), (0, 1.2, 0.5), breite=2.6, hoehe=2.0, mitte=(-1.88, 0), xl="x", yl="uₙ(x)")
    for n, c in ((1, HB), (4, BLAU), (16, DB)):
        s.daten(a, stuetz(lambda x: exp(-n * x), 0, 1), farbe=c, dicke=4)
    s.linie(a, (0, 0), (1, 0), farbe=ROT, dicke=5)
    s.punkt(a, 0, 1, farbe=ROT, r=0.085)
    s.punkt(a, 0, 0, farbe=ROT, r=0.085)
    s.punkt(a, 0, 0, farbe="#ffffff", r=0.05)
    s.text(a, "n = 1", (0.66, 0.60), KL, "left", HB)
    s.text(a, "n = 4", (0.36, 0.40), KL, "left", BLAU)
    s.text(a, "n = 16", (0.17, 0.14), KL, "left", DB)
    b = s.achsen((0, 1, 0.5), (0, 3.2, 1), breite=2.6, hoehe=2.0, mitte=(1.88, 0), xl="x", yl="bₙ(x)")
    for n, c in ((2, MB), (4, BLAU), (8, DB)):
        s.flaeche(b, "%d*%d*x*exp(-%d*x)" % (n, n, n), 0, 1, farbe=c, deckung=0.12)
        s.daten(b, stuetz(lambda x: n * n * x * exp(-n * x), 0, 1), farbe=c, dicke=4)
    s.linie(b, (0, 0), (1, 0), farbe=ROT, dicke=5)
    s.text(b, "n = 2", (0.72, 1.0), KL, "left", MB)
    s.text(b, "n = 4", (0.46, 1.62), KL, "left", BLAU)
    s.text(b, "n = 8", (0.27, 2.72), KL, "left", DB)
    s.speichern()


def k6schlauch():
    s = Szene("hm3/k6schlauch")
    a = s.achsen((0, 3.2, 1), (-0.4, 0.4, 0.2), breite=2.6, hoehe=2.0, mitte=(-1.88, 0), xl="x",
                 titel=s.tr("gl", "im Schlauch", "inside the tube", "dentro del tubo", "在管内"), titel_mitte=True)
    s.band(a, 0, 3.2, -0.2, 0.2, farbe=ORANGE, deckung=0.2)
    s.linie(a, (0, 0), (3.2, 0), farbe=ROT, dicke=4)
    s.daten(a, stuetz(lambda x: sin(12 * x) / 12, 0, pi, 700), farbe=BLAU, dicke=4)
    s.text(a, "w₁₂", (2.4, 0.26), KL, "left", BLAU)
    b = s.achsen((0, 1, 0.5), (-0.4, 1.2, 0.4), breite=2.6, hoehe=2.0, mitte=(1.88, 0), xl="x",
                 titel=s.tr("ng", "ragt hinaus", "sticks out", "sobresale", "伸出管外"), titel_mitte=True)
    s.band(b, 0, 1, -0.2, 0.2, farbe=ORANGE, deckung=0.2)
    s.linie(b, (0, 0), (1, 0), farbe=ROT, dicke=4)
    s.daten(b, stuetz(lambda x: exp(-16 * x), 0, 1), farbe=BLAU, dicke=4)
    s.text(b, "u₁₆", (0.14, 0.72), KL, "left", BLAU)
    s.text(b, "ε = 0.2", (0.55, 0.28), KL, "left", ORANGE)
    s.speichern()


def k6drittel():
    s = Szene("hm3/k6drittel")
    a = s.achsen((0, 1), (0, 1.1), breite=4.8, hoehe=2.2, mitte=(0, 0), xl="", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    fx = "0.62+0.2*sin(3*x+0.4)"
    e = 0.2

    def f(x):
        return 0.62 + 0.2 * sin(3 * x + 0.4)

    def f0(x):
        return f(x) - 0.14 - 0.03 * sin(9 * x)

    s.flaeche(a, fx + "+%g" % e, 0, 1, f2=fx + "-%g" % e, farbe=ORANGE, deckung=0.18)
    s.daten(a, stuetz(f, 0, 1), farbe=SCHWARZ, dicke=4)
    s.daten(a, stuetz(f0, 0, 1), farbe=BLAU, dicke=4)
    x0, y0 = 0.3, 0.6
    s.linie(a, (x0, 0), (x0, f0(x0)), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (y0, 0), (y0, f0(y0)), farbe=GRAU, dicke=2, dash=DASH)
    s.daten(a, stuetz(f0, x0, y0, 60), farbe=GRUEN, dicke=7)
    s.linie(a, (x0, f(x0)), (x0, f0(x0)), farbe=ROT, dicke=6)
    s.linie(a, (y0, f(y0)), (y0, f0(y0)), farbe=ROT, dicke=6)
    for x, y in ((x0, f(x0)), (y0, f(y0))):
        s.punkt(a, x, y, r=0.075)
    for x, y in ((x0, f0(x0)), (y0, f0(y0))):
        s.punkt(a, x, y, farbe=BLAU, r=0.075)
    s.text(a, "x", (x0, -0.09), KL, "center")
    s.text(a, "y", (y0, -0.09), KL, "center")
    s.text(a, "f", (0.95, 0.62), 26, "left", SCHWARZ)
    s.text(a, "fₙ₀", (0.95, 0.27), 26, "left", BLAU)
    s.text(a, "ε/3", (x0 - 0.02, f(x0) - 0.07), 26, "right", ROT)
    s.text(a, "ε/3", (y0 + 0.02, f(y0) - 0.07), 26, "left", ROT)
    s.text(a, s.tr("st", "stetig", "continuous", "continua", "连续"), (0.45, 0.41), KL, "center", GRUEN)
    s.speichern()


def k6rippel():
    s = Szene("hm3/k6rippel")
    a = s.achsen((0, 3.2, 1), (-0.3, 0.3, 0.1), breite=2.6, hoehe=1.9, mitte=(-1.88, 0), xl="x",
                 titel=s.tr("wn", "Rippel wₙ", "ripple wₙ", "rizado wₙ", "纹波 wₙ"), titel_mitte=True)
    s.daten(a, stuetz(lambda x: sin(4 * x) / 4, 0, pi, 400), farbe=BLAU, dicke=4)
    s.daten(a, stuetz(lambda x: sin(16 * x) / 16, 0, pi, 900), farbe=ROT, dicke=3)
    s.text(a, "n = 4", (0.72, 0.21), KL, "left", BLAU)
    s.text(a, "n = 16", (1.5, -0.2), KL, "left", ROT)
    b = s.achsen((0, 3.2, 1), (-1.2, 1.2, 0.5), breite=2.6, hoehe=1.9, mitte=(1.88, 0), xl="x",
                 titel=s.tr("ab", "Ableitung wₙ′", "derivative wₙ′", "derivada wₙ′", "导数 wₙ′"), titel_mitte=True)
    s.daten(b, stuetz(lambda x: cos(16 * x), 0, pi, 900), farbe=ROT, dicke=3)
    s.daten(b, stuetz(lambda x: cos(4 * x), 0, pi, 400), farbe=BLAU, dicke=4)
    s.speichern()


def k6mtest():
    s = Szene("hm3/k6mtest")

    def partial(n):
        return lambda x: sum(x ** k / k ** 2 for k in range(1, n + 1))

    a = s.achsen((-1, 1, 1), (-1, 1.8, 1), breite=2.6, hoehe=2.0, mitte=(-1.88, 0), xl="x")
    for n, c in ((1, HB), (2, MB), (4, BLAU)):
        s.daten(a, stuetz(partial(n), -1, 1, 200), farbe=c, dicke=3)
    # Summe: 3000 Glieder reichen für die Bildauflösung, Fehler unter 1/3000
    s.daten(a, stuetz(partial(3000), -1, 1, 60), farbe=ROT, dicke=3, dash=DASH)
    s.text(a, "f₁", (0.72, 0.42), KL, "left", HB)
    s.text(a, "f₂", (0.42, 1.02), KL, "right", MB)
    s.text(a, "f₄", (0.66, 1.42), KL, "right", BLAU)
    s.text(a, "f", (0.84, 1.68), KL, "right", ROT)
    b = s.achsen((0, 9, 1), (0, 1.1, 0.5), breite=2.6, hoehe=2.0, mitte=(1.88, 0), xl="k", yl="Mₖ")
    s.stems(b, [1, 2, 3], ys=[1, 0.25, 1 / 9], farbe=BLAU)
    s.stems(b, [4, 5, 6, 7, 8], ys=[1 / k ** 2 for k in (4, 5, 6, 7, 8)], farbe=ROT)
    s.text(b, s.tr("rest", "Rest", "tail", "resto", "余项"), (4.2, 0.2), KL, "left", ROT)
    s.speichern()


def k6radius():
    s = Szene("hm3/k6radius")
    a = s.welt()
    ox, oy = -2.05, -0.05
    R, r = 1.2, 0.8

    def kreis(q):
        return [(ox + q * cos(2 * pi * i / 90), oy + q * sin(2 * pi * i / 90)) for i in range(90)]

    polygon(s, a, kreis(R), fuellung=BLAU, deckung=0.1)
    polygon(s, a, kreis(r), fuellung=GRUEN, deckung=0.18)
    s.weg(a, "%g+%g*cos(t)" % (ox, R), "%g+%g*sin(t)" % (oy, R), 0, 6.28319, farbe=BLAU, dicke=4, dash=DASH)
    s.weg(a, "%g+%g*cos(t)" % (ox, r), "%g+%g*sin(t)" % (oy, r), 0, 6.28319, farbe=GRUEN, dicke=3)
    s.punkt(a, ox, oy, r=0.07)
    s.text(a, "z₀", (ox - 0.12, oy - 0.3), 26, "right")
    q = 0.7854
    s.pfeil((ox, oy), (ox + R * cos(q), oy + R * sin(q)), "", farbe=BLAU, dicke=3, spitze=0.16)
    s.text(a, "R", (ox + 0.88, oy + 0.98), 26, "left", BLAU)
    s.pfeil((ox, oy), (ox + r, oy), "", farbe=GRUEN, dicke=3, spitze=0.16)
    s.text(a, "r", (ox + 0.36, oy + 0.13), 26, "left", GRUEN)
    s.text(a, s.tr("rd", "am Rand: offen", "boundary: open", "borde: abierto", "边界：不定"), (ox, oy - 1.42), KL, "center", BLAU)
    s.text(a, s.tr("div", "außen: divergent", "outside: divergent", "fuera: divergente", "外部：发散"), (ox, oy + 1.42), KL, "center", SCHWARZ)
    b = s.achsen((-1, 1, 1), (0, 8, 2), breite=2.5, hoehe=2.1, mitte=(1.75, 0), xl="x")
    s.daten(b, stuetz(lambda x: 1 / (1 - x), -1, 0.875, 300), farbe=ROT, dicke=4)
    for n, c in ((2, HB), (5, MB), (10, DB)):
        s.daten(b, stuetz(lambda x: sum(x ** k for k in range(n + 1)), -1, 1, 300), farbe=c, dicke=4)
    s.text(b, "1/(1−x)", (0.66, 7.0), KL, "right", ROT)
    s.text(b, "f₂", (0.93, 1.6), KL, "center", HB)
    s.text(b, "f₅", (1.03, 4.4), KL, "left", MB)
    s.text(b, "f₁₀", (0.42, 5.2), KL, "right", DB)
    s.linie(b, (0.44, 5.2), (0.86, 5.2), farbe=DB, dicke=2)
    s.speichern()


def k6norm():
    s = Szene("hm3/k6norm")
    a = s.achsen((0, 1, 0.5), (0, 1.5, 0.5), breite=2.6, hoehe=2.0, mitte=(-1.88, 0), xl="x")

    def f(x):
        return 0.75 + 0.45 * sin(3.2 * x)

    def g(x):
        return 0.5 + 0.4 * x * x

    xm = max((i / 2000 for i in range(2001)), key=lambda x: abs(f(x) - g(x)))
    s.daten(a, stuetz(f, 0, 1), farbe=BLAU, dicke=4)
    s.daten(a, stuetz(g, 0, 1), farbe=GRUEN, dicke=4)
    s.pfeil((xm, g(xm)), (xm, f(xm)), "", farbe=ROT, dicke=4, spitze=0.14, on=a, doppelt=True)
    s.text(a, "f", (0.78, 1.2), 26, "left", BLAU)
    s.text(a, "g", (0.8, 0.55), 26, "left", GRUEN)
    s.text(a, "‖f − g‖", (xm - 0.03, 0.8), KL, "right", ROT)
    b = s.achsen((-1, 1, 1), (0, 1.1, 0.5), breite=2.6, hoehe=2.0, mitte=(1.88, 0), xl="x")
    for n, c in ((1, HB), (2, MB), (8, DB)):
        s.daten(b, stuetz(lambda x: abs(x) ** (1 + 1 / n), -1, 1, 300), farbe=c, dicke=4)
    s.daten(b, stuetz(lambda x: abs(x), -1, 1, 4), farbe=ROT, dicke=3, dash=DASH)
    s.text(b, "|x|", (0.28, 0.72), KL, "right", ROT)
    s.text(b, "n = 1", (0.52, 0.12), KL, "left", HB)
    s.speichern()


def k6mittel():
    s = Szene("hm3/k6mittel")

    def v(n):
        return lambda x: max(-1.0, min(1.0, n * x))

    def sgn(x):
        return (x > 0) - (x < 0)

    a = s.achsen((-1, 1, 1), (-1.2, 1.2, 1), breite=2.6, hoehe=1.8, mitte=(-1.88, 0), xl="x")
    s.linie(a, (-1, -1), (0, -1), farbe=ROT, dicke=5)
    s.linie(a, (0, 1), (1, 1), farbe=ROT, dicke=5)
    s.daten(a, stuetz(v(2), -1, 1, 400), farbe=HB, dicke=4)
    s.daten(a, stuetz(v(6), -1, 1, 1200), farbe=BLAU, dicke=4)
    s.text(a, "v₂", (0.5, 0.2), KL, "left", HB)
    s.text(a, "v₆", (-0.12, 0.72), KL, "right", BLAU)
    s.text(a, "sgn", (0.55, 0.72), KL, "left", ROT)
    b = s.achsen((-1, 1, 1), (0, 1.2, 0.5), breite=2.6, hoehe=1.8, mitte=(1.88, 0), xl="x",
                 titel=s.tr("q", "quadrierte Abweichung", "squared deviation", "desviación al cuadrado", "偏差平方"), titel_mitte=True)
    pl = [(-1.0 / 6 + i / 6.0 / 40, (1 + 6 * (-1.0 / 6 + i / 6.0 / 40)) ** 2) for i in range(41)]
    pr = [(i / 6.0 / 40, (1 - 6 * (i / 6.0 / 40)) ** 2) for i in range(41)]
    polygon(s, b, [(-1 / 6, 0)] + pl[:] + [(0, 0)], fuellung=BLAU, deckung=0.3)
    polygon(s, b, [(0, 0)] + pr + [(1 / 6, 0)], fuellung=BLAU, deckung=0.3)
    s.daten(b, pl, farbe=BLAU, dicke=4)
    s.daten(b, pr, farbe=BLAU, dicke=4)
    s.linie(b, (-1, 0), (-1 / 6, 0), farbe=BLAU, dicke=4)
    s.linie(b, (1 / 6, 0), (1, 0), farbe=BLAU, dicke=4)
    s.text(b, s.tr("fl", "Fläche", "area", "área", "面积"), (0.24, 0.62), KL, "left", BLAU)
    s.text(b, "2/(3n)", (0.24, 0.42), KL, "left", BLAU)
    s.speichern()


for f_ in (k6punkt, k6schlauch, k6drittel, k6rippel, k6mtest, k6radius, k6norm, k6mittel):
    f_()
