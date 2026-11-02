"""Abbildungen zu Höhere Mathematik 3, Teil 8: Wahrscheinlichkeitsrechnung.

Aufruf: python tools/szenen/hm3_teil8.py, danach python tools/szenen_ansehen.py out.png hm3/k8wuerfel ... [--lang de]
Alle Zahlen stehen im Heft und in rechnung_kap8.py. Rechenmodelle: zwei Vierer-Würfel, LED mit Dichte exp(-x/2)/2.
"""
import random
import sys
from math import comb, cos, erf, exp, factorial, pi, sin, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLBLAU = "#dceafa"
KLEIN = 24


def form(s, a, pts, farbe=BLAU, deckung=0.2, dicke=0, rand=None, dash=""):
    pl = ";".join("%.4f,%.4f" % p for p in pts)
    return s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": rand or farbe,
                            "fill_color": farbe, "fill_opacity": deckung, "stroke_width": dicke, "dash": dash}, a)


def rechteck(s, a, x0, y0, x1, y1, **kw):
    return form(s, a, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], **kw)


def Phi(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


def k8wuerfel():
    """Der Stichprobenraum als Gitter, A und B farbig."""
    s = Szene("hm3/k8wuerfel")
    a = s.welt()
    c, x0, y0 = 0.5, -3.0, -1.0
    for i in range(1, 5):
        for j in range(1, 5):
            x, y = x0 + (i - 1) * c, y0 + (j - 1) * c
            ina, inb = i + j == 5, i >= 3
            if ina and inb:
                rechteck(s, a, x, y, x + c, y + c, farbe=ROT, deckung=0.55)
            elif ina:
                rechteck(s, a, x, y, x + c, y + c, farbe=BLAU, deckung=0.45)
            elif inb:
                rechteck(s, a, x, y, x + c, y + c, farbe=ORANGE, deckung=0.3)
    for i in range(5):
        s.linie(a, (x0 + i * c, y0), (x0 + i * c, y0 + 4 * c), dicke=2)
        s.linie(a, (x0, y0 + i * c), (x0 + 4 * c, y0 + i * c), dicke=2)
    for i in range(1, 5):
        s.text(a, str(i), (x0 + (i - 0.5) * c, y0 - 0.28), groesse=KLEIN, ausrichtung="center")
        s.text(a, str(i), (x0 - 0.2, y0 + (i - 0.5) * c - 0.08), groesse=KLEIN, ausrichtung="center")
    s.text(a, s.tr("w1", "erster Würfel", "first die", "primer dado", "第一枚骰子"), (x0 + 2 * c, y0 - 0.66), groesse=KLEIN, ausrichtung="center")
    s.text(a, s.tr("w2", "zweiter", "second", "segundo", "第二枚"), (x0 + 2 * c, y0 + 4 * c + 0.16), groesse=KLEIN, ausrichtung="center")
    x, y, h = -0.3, 0.42, 0.56
    for titel, farbe, d in ((s.tr("la", "A: Summe 5", "A: sum 5", "A: suma 5", "A：和为 5"), BLAU, 0.45),
                            (s.tr("lb", "B: erster mindestens 3", "B: first at least 3", "B: primero al menos 3", "B：第一枚至少为 3"), ORANGE, 0.3),
                            ("A ∩ B", ROT, 0.55)):
        rechteck(s, a, x, y, x + 0.36, y + 0.36, farbe=farbe, deckung=d, dicke=2, rand=SCHWARZ)
        s.text(a, titel, (x + 0.52, y + 0.09), groesse=26)
        y -= h
    s.speichern()


def k8kollision():
    s = Szene("hm3/k8kollision")
    a = s.achsen((0, 41), (0, 1), breite=5.4, hoehe=1.35, mitte=(0, 0), xl="k", xl_mitte=False, xticks="1;5;10;15;20;25;30;35;40", yticks="0;0.5;1",
                 titel=s.tr("t", "P(zwei gleiche Adressen)", "P(two equal addresses)", "P(dos direcciones iguales)", "P(两个地址相同)"))
    q, xs, ys = 1.0, [], []
    for k in range(1, 41):
        q *= (256 - k + 1) / 256
        xs.append(k)
        ys.append(1 - q)
    s.stems(a, [k for k in xs if k != 20], [v for k, v in zip(xs, ys) if k != 20], farbe=BLAU, breite=0.72, marker="none", r=0.0)
    s.stems(a, [20], [ys[19]], farbe=ROT, breite=0.72, marker="none", r=0.0)
    s.linie(a, (0, 0.5), (41, 0.5), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "k = 20: 0.533", (17.5, 0.62), groesse=KLEIN, ausrichtung="right", farbe=ROT)
    s.speichern()


def k8mosaik():
    s = Szene("hm3/k8mosaik")
    a = s.welt()
    x0, y0, W, H = -2.6, -1.0, 3.6, 2.0
    br = [0.5, 1 / 3, 1 / 6]
    ho = [0.1, 0.2, 0.3]
    namen = ["A_1", "A_2", "A_3"]
    txt = ["1/2", "1/3", "1/6"]
    tho = ["1/10", "1/5", "3/10"]
    x = x0
    for b, h, n, t, th in zip(br, ho, namen, txt, tho):
        w = b * W
        rechteck(s, a, x, y0, x + w, y0 + h * H, farbe=BLAU, deckung=0.55)
        rechteck(s, a, x, y0, x + w, y0 + H, farbe=BLAU, deckung=0.0, dicke=3, rand=SCHWARZ)
        s.text(a, n, (x + w / 2, y0 + H * 0.62), groesse=26, ausrichtung="center")
        s.text(a, t, (x + w / 2, y0 - 0.32), groesse=KLEIN, ausrichtung="center")
        s.text(a, th, (x + w / 2, y0 + h * H + 0.1), groesse=KLEIN, ausrichtung="center", farbe=BLAU)
        x += w
    s.text(a, s.tr("b", "blau: B", "blue: B", "azul: B", "蓝色：B"), (1.3, 0.6), groesse=26, farbe=BLAU)
    s.text(a, "P(B) = 1/6", (1.3, 0.15), groesse=26, farbe=BLAU)
    s.text(a, "P(A_3 | B) = 3/10", (1.3, -0.3), groesse=26)
    s.speichern()


def k8treppe():
    s = Szene("hm3/k8treppe")
    p = [1, 2, 3, 4, 3, 2, 1]
    a = s.achsen((1, 9), (0, 0.3), breite=2.6, hoehe=1.4, mitte=(-1.85, 0), xticks="2;3;4;5;6;7;8", yticks="0;0.1;0.2;0.3", titel="P(S = s)")
    s.stems(a, range(2, 9), [v / 16 for v in p], farbe=BLAU, breite=0.62, marker="none", r=0.0)
    b = s.achsen((1, 9), (0, 1), breite=2.6, hoehe=1.4, mitte=(1.85, 0), xticks="2;3;4;5;6;7;8", yticks="0;0.5;1", titel="F_S(x)")
    F = [0, 1, 3, 6, 10, 13, 15, 16]
    pts = [(1, 0)]
    for i, x in enumerate(range(2, 9)):
        pts.append((x, F[i] / 16))
        pts.append((x, F[i + 1] / 16))
    pts.append((9, 1))
    s.daten(b, pts, farbe=BLAU, dicke=4)
    for i, x in enumerate(range(2, 9)):
        s.punkt(b, x, F[i + 1] / 16, farbe=BLAU, r=0.06)
    s.speichern()


def k8poisson():
    s = Szene("hm3/k8poisson")
    a = s.achsen((-0.6, 7.6), (0, 0.3), breite=4.6, hoehe=1.4, mitte=(0, 0), xl="k", xl_mitte=False, xticks="0;1;2;3;4;5;6;7", yticks="0;0.1;0.2;0.3", titel="P(X = k)")
    xs = list(range(8))
    bi = [comb(200, k) * 0.01 ** k * 0.99 ** (200 - k) for k in xs]
    po = [2 ** k / factorial(k) * exp(-2) for k in xs]
    s.stems(a, [k - 0.19 for k in xs], bi, farbe=BLAU, breite=0.36, marker="none", r=0.0)
    s.stems(a, [k + 0.19 for k in xs], po, farbe=ORANGE, breite=0.36, marker="none", r=0.0)
    s.legende(a, [(s.tr("bi", "Binomial, n = 200, p = 0.01", "binomial, n = 200, p = 0.01", "binomial, n = 200, p = 0.01", "二项分布，n = 200，p = 0.01"), BLAU, "-"),
                  (s.tr("po", "Poisson, λ = 2", "Poisson, λ = 2", "Poisson, λ = 2", "泊松分布，λ = 2"), ORANGE, "-")], (3.0, 0.285), zeile=0.34)
    s.speichern()


def k8dichte():
    s = Szene("hm3/k8dichte")
    a = s.achsen((0, 8), (0, 0.6), breite=2.6, hoehe=1.4, mitte=(-1.9, 0), xticks="0;1;3;5;7", yticks="0;0.25;0.5", titel="f_X(x)")
    s.flaeche(a, "0.5*exp(-x/2)", 1, 3, farbe=BLAU, deckung=0.35)
    s.kurve(a, "0.5*exp(-x/2)", farbe=BLAU, dicke=4)
    s.text(a, "0.383", (2.0, 0.09), groesse=KLEIN, ausrichtung="center")
    b = s.achsen((-5, 5), (0, 0.9), breite=2.6, hoehe=1.4, mitte=(1.8, 0), xticks="-4;-2;0;2;4", yticks="0;0.4;0.8", titel=s.tr("no", "Normalverteilungen", "normal distributions", "distribuciones normales", "正态分布"))
    def glocke(m, t):
        return "exp(-0.5*((x-(%g))/%g)^2)/(%g*sqrt(2*pi))" % (m, t, t)
    s.kurve(b, glocke(0, 1), farbe=BLAU, dicke=4)
    s.kurve(b, glocke(0, 2), farbe=GRUEN, dicke=4)
    s.kurve(b, glocke(2, 0.5), farbe=ORANGE, dicke=4)
    s.text(b, "σ = 1", (-1.0, 0.45), groesse=KLEIN, ausrichtung="right", farbe=BLAU)
    s.text(b, "σ = 2", (-2.4, 0.2), groesse=KLEIN, ausrichtung="right", farbe=GRUEN)
    s.text(b, "σ = 0.5", (1.2, 0.72), groesse=KLEIN, ausrichtung="right", farbe=ORANGE)
    s.speichern()


def k8schwerpunkt():
    s = Szene("hm3/k8schwerpunkt")
    p = [1, 2, 3, 4, 3, 2, 1]
    a = s.achsen((1, 9), (0, 0.3), breite=2.6, hoehe=1.4, mitte=(-1.85, 0), xticks="2;3;4;5;6;7;8", yticks="0;0.1;0.2;0.3", titel="P(S = s)")
    s.stems(a, range(2, 9), [v / 16 for v in p], farbe=BLAU, breite=0.62, marker="none", r=0.0)
    s.linie(a, (5, 0), (5, 0.3), farbe=ROT, dicke=3, dash=DASH)
    s.text(a, "E(S) = 5", (5.25, 0.27), groesse=KLEIN, farbe=ROT)
    b = s.achsen((0, 8), (0, 0.6), breite=2.6, hoehe=1.4, mitte=(1.85, 0), xticks="0;2;4;6;8", yticks="0;0.25;0.5", titel="f_X(x)")
    s.flaeche(b, "0.5*exp(-x/2)", 0, 8, farbe=BLAU, deckung=0.2)
    s.kurve(b, "0.5*exp(-x/2)", farbe=BLAU, dicke=4)
    s.linie(b, (2, 0), (2, 0.6), farbe=ROT, dicke=3, dash=DASH)
    s.text(b, "E(X) = 2", (2.35, 0.53), groesse=KLEIN, farbe=ROT)
    s.speichern()


def k8tscheb():
    s = Szene("hm3/k8tscheb")
    a = s.achsen((0, 4.2), (0, 1), breite=4.6, hoehe=1.5, mitte=(-0.6, 0), xl="k", xl_mitte=False, xticks="0;1;2;3;4", yticks="0;0.5;1", titel="P(|X − μ| ≥ kσ)")
    s.band(a, 0, 1, 0, 1, farbe=GRAU, deckung=0.12)
    s.kurve(a, "1/x^2", x=[1, 4.2], farbe=ROT, dicke=4)
    k = [i * 0.05 for i in range(0, 85)]
    s.daten(a, [(v, 2 * (1 - Phi(v))) for v in k], farbe=BLAU, dicke=4)
    def led(v):
        return 1 - exp(v - 1) + exp(-1 - v) if v < 1 else exp(-1 - v)
    s.daten(a, [(v, led(v)) for v in k], farbe=ORANGE, dicke=4)
    s.text(a, "1/k²", (1.25, 0.72), groesse=KLEIN, farbe=ROT)
    s.legende(a, [(s.tr("sch", "Schranke", "bound", "cota", "界"), ROT, "-"), (s.tr("nv", "Normalverteilung", "normal distribution", "distribución normal", "正态分布"), BLAU, "-"), ("LED", ORANGE, "-")], (2.0, 0.96), zeile=0.34)
    s.speichern()


def k8gitter():
    s = Szene("hm3/k8gitter")
    a = s.achsen((0, 5), (0, 5), breite=1.5, hoehe=1.4, mitte=(-2.0, 0), xl="W_1", xl_mitte=False, xticks="1;2;3;4", yticks="1;2;3;4",
                 titel=s.tr("un", "unabhängig: (W_1, W_2)", "independent: (W_1, W_2)", "independientes: (W_1, W_2)", "独立：(W_1, W_2)"))
    for i in range(1, 5):
        for j in range(1, 5):
            s.punkt(a, i, j, farbe=BLAU, r=0.07)
    b = s.achsen((1, 9), (-4, 4), breite=2.6, hoehe=1.4, mitte=(1.5, 0), xl="S", xl_mitte=False, xticks="2;4;5;6;8", yticks="-3;0;3",
                 titel=s.tr("ka", "unkorreliert, abhängig: (S, D)", "uncorrelated, dependent: (S, D)", "incorreladas, dependientes: (S, D)", "不相关但相依：(S, D)"))
    for i in range(1, 5):
        for j in range(1, 5):
            s.punkt(b, i + j, i - j, farbe=ORANGE, r=0.07)
    s.linie(b, (1, 0), (9, 0), farbe=GRAU, dicke=2, dash=DASH)
    s.speichern()


def k8hoehen():
    s = Szene("hm3/k8hoehen")
    for mitte, rho, t in (((-1.7, 0), 0.0, "ρ = 0"), ((1.7, 0), 0.7, "ρ = 0.7")):
        a = s.achsen((-3.4, 3.4), (-3.4, 3.4), breite=1.7, hoehe=1.7, mitte=mitte, xticks="-3;0;3", yticks="-3;0;3", titel=t, kreuz=False)
        q = sqrt(1 - rho * rho)
        for c, d in ((1, 5), (2, 4), (3, 3)):
            s.weg(a, "%g*cos(t)" % c, "%g*(%g*cos(t)+%g*sin(t))" % (c, rho, q), 0, 6.2832, farbe=BLAU, dicke=d)
    s.speichern()


def k8mittel():
    s = Szene("hm3/k8mittel")
    a = s.achsen((1, 1000), (1, 4), breite=4.8, hoehe=1.5, mitte=(0, 0), xl="n", xl_mitte=False, xlog=True, xticks="1;10;100;1000", yticks="1;2;2.5;3;4", titel="X̄_n")
    random.seed(8)
    N = 1000
    nn = sorted(set(list(range(1, 41)) + [int(1.08 ** i) for i in range(48, 90)] + [1000]))
    for farbe in (BLAU, ORANGE, GRUEN):
        su, pts = 0, []
        for n in range(1, N + 1):
            su += random.randint(1, 4)
            if n in nn:
                pts.append((n, su / n))
        s.daten(a, pts, farbe=farbe, dicke=3)
    sg = sqrt(5 / 4)
    s.linie(a, (1, 2.5), (1000, 2.5), farbe=SCHWARZ, dicke=2)
    gr = [i for i in range(1, 1001) if i in nn]
    s.daten(a, [(v, 2.5 + sg / sqrt(v)) for v in gr], farbe=GRAU, dicke=2, dash=DASH)
    s.daten(a, [(v, 2.5 - sg / sqrt(v)) for v in gr], farbe=GRAU, dicke=2, dash=DASH)
    s.speichern()


def k8zgs():
    s = Szene("hm3/k8zgs")
    sg = sqrt(5 / 4)
    for (n, mitte) in ((1, (-2.3, 0)), (4, (0, 0)), (16, (2.3, 0))):
        a = s.achsen((-3.5, 3.5), (0, 0.5), breite=1.9, hoehe=1.05, mitte=mitte, xticks="-2;0;2", yticks="0;0.4", titel="n = %d" % n)
        d = {0: 1.0}
        for _ in range(n):
            e = {}
            for w, q in d.items():
                for v in (1, 2, 3, 4):
                    e[w + v] = e.get(w + v, 0) + q / 4
            d = e
        h = 1 / (sqrt(n) * sg)
        xs, ys = [], []
        for w, q in sorted(d.items()):
            z = (w - n * 2.5) * h
            if -3.5 <= z <= 3.5:
                xs.append(z)
                ys.append(q / h)
        s.stems(a, xs, ys, farbe=BLAU, breite=h * 0.86, marker="none", r=0.0)
        s.kurve(a, "exp(-x^2/2)/sqrt(2*pi)", farbe=ROT, dicke=3)
    s.speichern()


for f in (k8wuerfel, k8kollision, k8mosaik, k8treppe, k8poisson, k8dichte, k8schwerpunkt, k8tscheb, k8gitter, k8hoehen, k8mittel, k8zgs):
    f()
print("12 Szenen geschrieben")
