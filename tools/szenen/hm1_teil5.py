"""Höhere Mathematik 1, Teil 5 (kap5_stufen.tex): Exponentialfunktion und Stetigkeit.

Aufruf: python tools/szenen/hm1_teil5.py, danach python tools/szenen_ansehen.py out.png hm1/k5zins ... [--lang de]
Alle Zahlen stehen im Heft und in rechnung_kap5.py: z_n(x) = (1+x/n)^n, k(x) = e^x + x, p(x) = k(x) - 2, x* = 0,4429.
Folgen sind Punkte, keine Linien. Offene Kreise: Stelle gehört nicht dazu, volle Punkte: Funktionswert.
"""
import sys
from math import exp
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 24                 # Beschriftung in den Bildern
R = 0.055                  # Punktradius einer Folge
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche
XSTERN = 0.44285           # Nullstelle von p
K = "exp(x)+x"


def glieder(s, on, pts, farbe=BLAU, r=R):
    for x, y in pts:
        s.punkt(on, x, y, farbe=farbe, r=r)


def offen(s, on, x, y, farbe=BLAU, r=0.085):
    s._add("Dot", {"center": [x, y, 0], "radius": r, "color": farbe, "fill_color": "#ffffff", "fill_opacity": 1, "stroke_width": 3}, on)


# ------------------------------------------------------------------------------------------ Stufe 1
def k5zins():
    """Links z_n(1) steigt gegen e, rechts die Kurven z_1, z_2, z_5 unter e^x."""
    s = Szene("hm1/k5zins")
    s.welt()
    a = s.achsen((0, 31), (1.9, 2.9), breite=2.5, hoehe=1.75, mitte=(-1.95, 0), xticks="1;10;20;30", yticks="2;2.5", xl="n", xl_mitte=False, titel="z_n(1)")
    s.linie(a, (0, 2.71828), (31, 2.71828), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(a, "e = 2.718", (31, 2.8), KLEIN, "right", ROT)
    glieder(s, a, [(n, (1 + 1 / n) ** n) for n in range(1, 31)])
    b = s.achsen((-1, 2), (0, 7.8), breite=2.3, hoehe=1.75, mitte=(1.25, 0), xticks="-1;0;1;2", yticks="1;3;5;7", xl="x", xl_mitte=False)
    s.kurve(b, "1+x", farbe=GRUEN, dicke=3.5)
    s.kurve(b, "(1+x/2)^2", farbe=ORANGE, dicke=3.5)
    s.kurve(b, "(1+x/5)^5", farbe=GRAU, dicke=3.5)
    s.kurve(b, "exp(x)", farbe=BLAU, dicke=4.5)
    s.text(b, "e^x", (2.08, 7.39), KLEIN, "left", BLAU)
    s.text(b, "z_5", (2.08, 5.38), KLEIN, "left", GRAU)
    s.text(b, "z_2", (2.08, 4.0), KLEIN, "left", BRAUN)
    s.text(b, "z_1", (2.08, 3.0), KLEIN, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k5explog():
    """e^x und log x, Spiegelbilder an y = x, mit den Geraden y = x + 1 und y = x - 1."""
    s = Szene("hm1/k5explog")
    a = s.achsen((-2.5, 4.5), (-2.5, 4.5), breite=2.6, hoehe=2.6, mitte=(0, 0), kreuz=True, xticks="-2;1;2;3;4", yticks="-2;1;2;3;4", xl="x", yl="y")
    s.kurve(a, "x", x=(-2.5, 4.5), farbe=GRAU, dicke=2.5, dash=DASH)
    s.kurve(a, "x+1", x=(-2.5, 3.5), farbe=GRUEN, dicke=2.5, dash=DOT)
    s.kurve(a, "x-1", x=(-1.5, 4.5), farbe=ORANGE, dicke=2.5, dash=DOT)
    s.kurve(a, "exp(x)", x=(-2.5, 1.5), farbe=BLAU)
    s.kurve(a, "ln(x)", x=(0.09, 4.5), farbe=ROT)
    glieder(s, a, [(0, 1), (1, 2.71828)], farbe=BLAU, r=0.07)
    glieder(s, a, [(1, 0), (2.71828, 1)], farbe=ROT, r=0.07)
    s.text(a, "e^x", (1.1, 3.9), KLEIN, "right", BLAU)
    s.text(a, "log x", (4.5, 1.05), KLEIN, "left", ROT)
    s.text(a, "y = x", (4.55, 4.5), KLEIN, "left", GRAU)
    s.text(a, "y = x + 1", (3.4, 4.75), KLEIN, "right", GRUEN)
    s.text(a, "y = x − 1", (4.55, 3.5), KLEIN, "left", BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k5grenzwert():
    """Drei Stellen: Lücke mit Grenzwert, Sprung, schnelles Wechseln ohne Grenzwert."""
    s = Szene("hm1/k5grenzwert")
    s.welt()
    t1 = s.tr("t1", "Lücke L", "Gap L", "Hueco L", "间断 L")
    t2 = s.tr("t2", "Sprung H", "Jump H", "Salto H", "跳跃 H")
    t3 = s.tr("t3", "Schwingen w", "Oscillation w", "Oscilación w", "振荡 w")
    a = s.achsen((0, 4), (0, 6), breite=1.7, hoehe=1.65, mitte=(-2.25, 0), xticks="0;2;4", yticks="0;2;4;6", xl="x", xl_mitte=False, titel=t1)
    s.linie(a, (0, 4), (2, 4), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (2, 0), (2, 4), farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(a, "x+2", farbe=BLAU)
    offen(s, a, 2, 4)
    b = s.achsen((-2, 2), (-0.5, 1.5), breite=1.7, hoehe=1.65, mitte=(0, 0), xticks="-2;0;2", yticks="0;1", xl="x", xl_mitte=False, titel=t2)
    s.linie(b, (-2, 0), (0, 0), farbe=BLAU, dicke=5)
    s.linie(b, (0, 1), (2, 1), farbe=BLAU, dicke=5)
    offen(s, b, 0, 0)
    s.punkt(b, 0, 1, farbe=BLAU, r=0.085)
    c = s.achsen((0, 1.05), (-1.4, 1.4), breite=1.7, hoehe=1.65, mitte=(2.25, 0), xticks="0;0.5;1", yticks="-1;0;1", xl="x", xl_mitte=False, titel=t3)
    pts = []
    for m in range(40, 0, -1):                 # 1/(m+1) < x <= 1/m: floor(1/x) = m
        v = (-1) ** m
        pts += [(1 / (m + 1), v), (1 / m, v)]
    s.daten(c, pts, farbe=BLAU, dicke=2.5)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k5epsdelta():
    """x^2 bei x0 = 2: waagerechter eps-Streifen, senkrechter delta-Streifen."""
    s = Szene("hm1/k5epsdelta")
    a = s.achsen((1.5, 2.5), (2.5, 5.5), breite=3.6, hoehe=1.8, mitte=(-0.5, 0), xticks="1.5;1.9;2;2.1;2.5", yticks="3;3.5;4;4.5;5", xl="x", xl_mitte=False)
    s.band(a, 1.5, 2.5, 3.5, 4.5, farbe=ROT, deckung=0.13)
    s.band(a, 1.9, 2.1, 2.5, 5.5, farbe=BLAU, deckung=0.2)
    s.kurve(a, "x^2", x=(1.58, 2.34), farbe=BLAU)
    s.punkt(a, 2, 4, farbe=SCHWARZ, r=0.075)
    s.linie(a, (1.9, 3.61), (2.1, 3.61), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (1.9, 4.41), (2.1, 4.41), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "(x_0 | f(x_0))", (1.96, 4.75), KLEIN, "right")
    s.text(a, "ε = 0.5", (2.53, 4.0), KLEIN, "left", ROT)
    s.text(a, "δ_0 = 0.1", (2.53, 2.95), KLEIN, "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k5folgenstetig():
    """Links folgen die Bilder der Folge, rechts bleiben sie beim Sprung zurück."""
    s = Szene("hm1/k5folgenstetig")
    s.welt()
    t1 = s.tr("st", "k ist stetig", "k is continuous", "k es continua", "k 连续")
    t2 = s.tr("sp", "H springt", "H jumps", "H salta", "H 跳跃")
    a = s.achsen((0, 1), (1, 3.8), breite=2.5, hoehe=1.65, mitte=(-1.75, 0), xticks="0;0.5;1", yticks="1;2;3", xl="x", xl_mitte=False, titel=t1)
    s.kurve(a, K, farbe=BLAU)
    xs = [0.5 + (-1) ** n * 0.4 / n for n in range(1, 11)]
    glieder(s, a, [(x, 1) for x in xs], farbe=ORANGE)
    glieder(s, a, [(0, exp(x) + x) for x in xs], farbe=GRUEN)
    glieder(s, a, [(x, exp(x) + x) for x in xs], farbe=GRAU, r=0.045)
    y0 = exp(0.5) + 0.5
    s.linie(a, (0.5, 1), (0.5, y0), farbe=ROT, dicke=2.5, dash=DASH)
    s.linie(a, (0, y0), (0.5, y0), farbe=ROT, dicke=2.5, dash=DASH)
    s.punkt(a, 0.5, y0, farbe=ROT, r=0.08)
    b = s.achsen((-1.1, 0.6), (-0.3, 1.4), breite=2.5, hoehe=1.65, mitte=(1.75, 0), xticks="-1;0", yticks="0;1", xl="x", xl_mitte=False, titel=t2)
    s.linie(b, (-1.1, 0), (0, 0), farbe=BLAU, dicke=5)
    s.linie(b, (0, 1), (0.6, 1), farbe=BLAU, dicke=5)
    offen(s, b, 0, 0)
    s.punkt(b, 0, 1, farbe=ROT, r=0.085)
    glieder(s, b, [(-1 / n, 0) for n in range(1, 11)], farbe=ORANGE)
    s.text(b, "H(0) = 1", (-0.06, 1.15), KLEIN, "right", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k5haeufung():
    """Links q_n mit zwei Teilfolgen, rechts das Halbieren aus dem Beweis."""
    s = Szene("hm1/k5haeufung")
    s.welt()

    def q(n):
        return (-1) ** n * n / (n + 1)
    a = s.achsen((0, 31), (-1.3, 1.3), breite=2.4, hoehe=1.75, mitte=(-2.05, 0), xticks="1;10;20;30", yticks="-1;0;1", xl="n", xl_mitte=False)
    s.linie(a, (0, 1), (31, 1), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (0, -1), (31, -1), farbe=GRAU, dicke=2, dash=DASH)
    glieder(s, a, [(n, q(n)) for n in range(2, 31, 2)])
    glieder(s, a, [(n, q(n)) for n in range(1, 31, 2)], farbe=ORANGE)
    x0, breite = 0.7, 2.5

    def p(v):
        return x0 + breite * (v + 1) / 2
    werte = [q(n) for n in range(1, 41)]
    for k in range(4):
        y = 0.75 - 0.5 * k
        r = -1 + 2 * 0.5 ** k
        s.linie(None, (p(-1), y), (p(1), y), farbe=HELLGRAU, dicke=2)
        s.linie(None, (p(-1), y), (p(r), y), farbe=ROT, dicke=6)
        for v in werte:
            s.punkt(None, p(v), y, farbe=BLAU, r=0.03)
        s.text(None, str(r).replace("-", "−").replace(".0", ""), (p(r), y + 0.2), KLEIN, "center", ROT)
    s.text(None, "−1", (p(-1), 0.95), KLEIN, "center", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k5maximum():
    """Drei Gegenbeispiele zum Satz vom Maximum, je eine Voraussetzung fehlt."""
    s = Szene("hm1/k5maximum")
    s.welt()
    t2 = s.tr("m2", "nicht abgeschlossen", "not closed", "no cerrado", "非闭区间")
    t3 = s.tr("m3", "nicht stetig", "not continuous", "no continua", "不连续")
    t4 = s.tr("m4", "unbeschränkt", "unbounded", "no acotado", "无界")
    br, ho = 1.7, 1.45
    b = s.achsen((0, 1.1), (0, 11), breite=br, hoehe=ho, mitte=(-2.25, 0), xticks="0;1", yticks="0;5;10", xl="x", xl_mitte=False, titel=t2)
    s.kurve(b, "1/x", x=(0.095, 1), farbe=BLAU)
    s.punkt(b, 1, 1, farbe=BLAU, r=0.07)
    s.text(b, "1/x", (0.35, 5.0), KLEIN, "left", BLAU)
    c = s.achsen((0, 1.1), (0, 1.25), breite=br, hoehe=ho, mitte=(0, 0), xticks="0;1", yticks="0;1", xl="x", xl_mitte=False, titel=t3)
    s.linie(c, (0, 1), (1.1, 1), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(c, (0, 0), (1, 1), farbe=BLAU, dicke=5)
    offen(s, c, 1, 1)
    s.punkt(c, 1, 0, farbe=BLAU, r=0.085)
    s.text(c, "v", (0.42, 0.6), KLEIN, "right", BLAU)
    d = s.achsen((0, 3.2), (0, 26), breite=br, hoehe=ho, mitte=(2.25, 0), xticks="0;1;2;3", yticks="0;10;20", xl="x", xl_mitte=False, titel=t4)
    s.kurve(d, "exp(x)", farbe=BLAU)
    s.text(d, "e^x", (2.2, 13), KLEIN, "right", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k5zws():
    """Links k trifft mu = 2, rechts k und die Umkehrfunktion."""
    s = Szene("hm1/k5zws")
    s.welt()
    a = s.achsen((0, 1), (0.5, 4), breite=2.5, hoehe=1.65, mitte=(-2.0, 0), xticks="0;0.4429;1", yticks="1;2;3", xl="x", xl_mitte=False)
    s.linie(a, (0, 2), (1, 2), farbe=ROT, dicke=2.5, dash=DASH)
    s.linie(a, (XSTERN, 0.5), (XSTERN, 2), farbe=ROT, dicke=2.5, dash=DASH)
    s.kurve(a, K, farbe=BLAU)
    s.punkt(a, XSTERN, 2, farbe=ROT, r=0.08)
    s.text(a, "μ = 2", (0.03, 2.3), KLEIN, "left", ROT)
    s.text(a, "k", (0.86, 3.5), KLEIN, "right", BLAU)
    b = s.achsen((0, 4), (0, 4), breite=2.1, hoehe=1.65, mitte=(1.65, 0), xticks="0;1;2;3;4", yticks="1;2;3;4", xl="x", xl_mitte=False)
    s.kurve(b, "x", farbe=GRAU, dicke=2.5, dash=DASH)
    s.kurve(b, K, x=(0, 1), farbe=BLAU)
    s.weg(b, "exp(t)+t", "t", 0, 1, farbe=ROT, dicke=5)
    s.punkt(b, 1, 3.71828, farbe=BLAU, r=0.07)
    s.punkt(b, 3.71828, 1, farbe=ROT, r=0.07)
    s.text(b, "k", (0.45, 2.9), KLEIN, "right", BLAU)
    s.text(b, "k^{−1}", (3.05, 0.45), KLEIN, "center", ROT)
    s.text(b, "y = x", (4.1, 3.75), KLEIN, "left", GRAU)
    s.speichern()


def k5nullstelle():
    """Halbieren, Sekante, Fixpunkt."""
    s = Szene("hm1/k5nullstelle")
    s.welt()
    t1 = s.tr("n1", "Halbieren", "Bisection", "Bisección", "二分法")
    t2 = s.tr("n2", "Sekante", "Secant", "Secante", "割线法")
    t3 = s.tr("n3", "Fixpunkt", "Fixed point", "Punto fijo", "不动点")
    P = "exp(x)+x-2"
    br = 1.7
    a = s.achsen((0, 1), (-1.2, 1.9), breite=br, hoehe=1.6, mitte=(-2.25, 0), xticks="0;0.5;1", yticks="-1;0;1", titel=t1)
    s.linie(a, (0, 0), (1, 0), farbe=GRAU, dicke=2)
    s.kurve(a, P, farbe=BLAU)
    for k, (l, r) in enumerate(((0, 0.5), (0.25, 0.5), (0.375, 0.5), (0.4375, 0.5))):
        y = 1.65 - 0.3 * k
        s.linie(a, (l, y), (r, y), farbe=ROT, dicke=5)
    b = s.achsen((0, 1), (-1.2, 1.9), breite=br, hoehe=1.6, mitte=(0, 0), xticks="0;0.5;1", yticks="-1;0;1", titel=t2)
    s.linie(b, (0, 0), (1, 0), farbe=GRAU, dicke=2)
    s.kurve(b, P, farbe=BLAU)
    al1, p1 = 0.36788, -0.18745
    s.linie(b, (0, -1), (1, 1.71828), farbe=ROT, dicke=2.5, dash=DASH)
    s.linie(b, (al1, p1), (1, 1.71828), farbe=ORANGE, dicke=2.5, dash=DASH)
    s.punkt(b, al1, 0, farbe=ROT, r=0.07)
    s.punkt(b, 0.43006, 0, farbe=BRAUN, r=0.07)
    s.punkt(b, al1, p1, farbe=BLAU, r=0.06)
    c = s.achsen((0, 1), (0, 1), breite=br, hoehe=1.6, mitte=(2.25, 0), xticks="0;0.5;1", yticks="0;0.5;1", titel=t3)
    s.kurve(c, "x", farbe=GRAU, dicke=2.5, dash=DASH)
    s.kurve(c, "exp(-x)", farbe=BLAU)
    s.punkt(c, 0.56714, 0.56714, farbe=ROT, r=0.08)
    s.speichern()


for f in (k5zins, k5explog, k5grenzwert, k5epsdelta, k5folgenstetig, k5haeufung, k5maximum, k5zws, k5nullstelle):
    f()
