"""GEMB 1 Teil 13 (kap13_stufen.tex): Diffusion, Rekombination und Grundgleichungen.

Aufruf: python tools/szenen/gemb1_teil13.py, danach python tools/szenen_ansehen.py out.png gemb1/k13fick ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap13.py.
"""
import random
import re
import sys
from math import atan2, cosh, degrees, erfc, exp, hypot, pi, sinh, sqrt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLBLAU, HELLROT, HELLGRUEN = "#dceafa", "#f6dede", "#ddf0e4"


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    key = "a_" + re.sub(r"\W", "", name + einheit)
    return s.tr(key, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def rahmen(s, x0, x1, y0, y1, farbe=SCHWARZ, dicke=3, dash=""):
    s.linie(None, (x0, y0), (x1, y0), farbe=farbe, dicke=dicke, dash=dash)
    s.linie(None, (x1, y0), (x1, y1), farbe=farbe, dicke=dicke, dash=dash)
    s.linie(None, (x1, y1), (x0, y1), farbe=farbe, dicke=dicke, dash=dash)
    s.linie(None, (x0, y1), (x0, y0), farbe=farbe, dicke=dicke, dash=dash)


# ------------------------------------------------------------------------------------------ Stufe 1
def k13fick():
    """Links Teilchen mit fallender Dichte und drei Ebenen, rechts N(x)."""
    s = Szene("gemb1/k13fick")
    s.welt()
    x0, x1, y0, y1 = -3.4, -0.45, -0.85, 0.75
    s.band(None, x0, x1, y0, y1, farbe=GRAU, deckung=0.07)
    rahmen(s, x0, x1, y0, y1, farbe=GRAU, dicke=2)
    rnd = random.Random(13)
    n = 0
    while n < 110:
        u = rnd.random()
        if rnd.random() > 0.97 - 0.83 * u:
            continue
        x = x0 + 0.08 + u * (x1 - x0 - 0.16)
        y = y0 + 0.08 + rnd.random() * (y1 - y0 - 0.16)
        s.punkt(None, x, y, farbe=BLAU, r=0.035)
        n += 1
    xe, l = 0.5 * (x0 + x1), 0.7
    s.linie(None, (xe, y0 - 0.1), (xe, y1 + 0.1), farbe=ROT, dicke=4)
    s.linie(None, (xe - l, y0 - 0.1), (xe - l, y1 + 0.1), farbe=GRAU, dicke=2.5, dash=DASH)
    s.linie(None, (xe + l, y0 - 0.1), (xe + l, y1 + 0.1), farbe=GRAU, dicke=2.5, dash=DASH)
    t(s, "x_E", (xe, y1 + 0.3), farbe=ROT)
    t(s, "x_E-l_{mfp}", (xe - l - 0.1, y0 - 0.34), g=22, a="right")
    t(s, "x_E+l_{mfp}", (xe + l + 0.1, y0 - 0.34), g=22, a="left")
    s.pfeil((xe - 1.15, y1 + 0.5), (xe - 0.05, y1 + 0.5), "", farbe=BLAU, dicke=4.5, spitze=0.17)
    s.pfeil((xe + 0.62, y1 + 0.5), (xe + 0.05, y1 + 0.5), "", farbe=BLAU, dicke=2.5, spitze=0.13)
    t(s, s.tr("viel", "viele", "many", "muchas", "多"), (xe - 1.05, y1 + 0.28), g=22, farbe=BLAU)
    t(s, s.tr("wenig", "wenige", "few", "pocas", "少"), (xe + 1.0, y1 + 0.28), g=22, farbe=BLAU)
    a = s.achsen((0, 10), (0, 10), breite=2.5, hoehe=1.95, mitte=(1.75, -0.05), xl="x", yl="N", kreuz=True, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.kurve(a, "8.8-0.68*x", x=(0.3, 9.7), farbe=BLAU, dicke=4.5)
    xE, lm = 5.0, 2.3
    for xx, fa in ((xE - lm, GRAU), (xE, ROT), (xE + lm, GRAU)):
        yy = 8.8 - 0.68 * xx
        s.linie(a, (xx, 0), (xx, yy), farbe=fa, dicke=2.5, dash=DASH)
        s.punkt(a, xx, yy, farbe=fa, r=0.07)
    s.text(a, "x_E", (xE, -1.0), groesse=22, ausrichtung="center", farbe=ROT)
    s.pfeil((5.6, 7.2), (8.0, 7.2), "", farbe=ROT, dicke=3.5, spitze=0.14, on=a)
    s.text(a, "𝒥", (6.8, 8.1), groesse=24, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k13kontinuitaet():
    """Links Volumenelement über N(x), rechts Ausgleich einer Stufe."""
    s = Szene("gemb1/k13kontinuitaet")
    s.welt()
    xa, xb = -2.45, -1.35
    yu, yo = 0.45, 1.15
    s.band(None, xa, xb, yu, yo, farbe=BLAU, deckung=0.18)
    rahmen(s, xa, xb, yu, yo, farbe=SCHWARZ, dicke=2.5)
    s.pfeil((xa - 0.95, 0.8), (xa - 0.05, 0.8), "", farbe=ROT, dicke=5, spitze=0.2)
    s.pfeil((xb + 0.05, 0.8), (xb + 0.55, 0.8), "", farbe=ROT, dicke=3, spitze=0.15)
    t(s, "𝒥(x)", (xa - 0.5, 1.1), farbe=ROT, g=24)
    t(s, "𝒥(x+\\Delta x)", (xb + 0.42, 1.1), farbe=ROT, g=24, a="center")
    t(s, "\\Delta x", (0.5 * (xa + xb), 0.8), g=22)
    a = s.achsen((0, 10), (0, 10), breite=3.1, hoehe=1.3, mitte=(-1.85, -0.85), xl="x", yl="N", kreuz=True, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.kurve(a, "1.2+8.3*exp(-0.3*x)", x=(0.2, 9.8), farbe=BLAU, dicke=4)
    ax, bx = (xa + 1.85 + 1.55) / 3.1 * 10, (xb + 1.85 + 1.55) / 3.1 * 10
    s.linie(a, (ax, 0), (ax, 1.2 + 8.3 * exp(-0.3 * ax)), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (bx, 0), (bx, 1.2 + 8.3 * exp(-0.3 * bx)), farbe=GRAU, dicke=2, dash=DASH)
    b = s.achsen((-3, 3), (0, 1.05), breite=2.7, hoehe=1.95, mitte=(1.85, -0.1), xl="x", yl="N/N_1", xticks="-3;0;3", yticks="0;0.5;1", xzahlen=False, xl_mitte=False)
    s.text(b, "0", (0, -0.12), groesse=22, ausrichtung="center")
    s.daten(b, [(-3, 1), (0, 1), (0, 0), (3, 0)], farbe=GRAU, dicke=3)
    werte = [(0.25, GRUEN), (0.6, ORANGE), (1.3, BLAU), (3.5, ROT)]
    for w, fa in werte:
        s.daten(b, [(-3 + 0.05 * i, 0.5 * erfc((-3 + 0.05 * i) / w)) for i in range(121)], farbe=fa, dicke=3.5)
    for y, (txt, fa) in zip((0.98, 0.86, 0.74, 0.62, 0.5), (("t_0", GRAU), ("t_1", GRUEN), ("t_2", ORANGE), ("t_3", BLAU), ("t_4", ROT))):
        s.text(b, txt, (2.5, y), groesse=22, ausrichtung="center", farbe=fa)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def spalte(s, on, x, ys):
    s.text(on, "x_0 =", (x, ys[0]), groesse=22, ausrichtung="center")
    s.text(on, "0.5 µm", (x, ys[1]), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(on, "1 µm", (x, ys[2]), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(on, "2 µm", (x, ys[3]), groesse=22, ausrichtung="center", farbe=GRUEN)


def k13quellen():
    """N/N_0 für die unendliche Quelle und N·1 µm/(N_0 d) für die endliche Quelle, je drei Eindringtiefen."""
    s = Szene("gemb1/k13quellen")
    s.welt()
    fa = {0.5: BLAU, 1.0: ROT, 2.0: GRUEN}
    a = s.achsen((0, 5), (0, 1), breite=2.2, hoehe=1.9, mitte=(-2.0, 0.0), xl=achse(s, "x", "µm"), yl="", xticks="0;1;2;3;4;5", yticks="0;0.5;1", xl_mitte=False)
    t(s, s.tr("unend", "unendliche Quelle", "infinite source", "fuente infinita", "无限源"), (-2.0, 1.45), g=25)
    s.text(a, "N/N_0", (0.15, 1.08), groesse=24, ausrichtung="left")
    for x0, c in fa.items():
        s.daten(a, [(0.05 * i, erfc(0.05 * i / x0)) for i in range(101)], farbe=c, dicke=4)
    spalte(s, a, 3.9, (0.95, 0.82, 0.69, 0.56))
    b = s.achsen((0, 5), (0, 2.5), breite=2.2, hoehe=1.9, mitte=(1.4, 0.0), xl=achse(s, "x", "µm"), yl="", xticks="0;1;2;3;4;5", yticks="0;1;2", xl_mitte=False)
    t(s, s.tr("end", "endliche Quelle", "finite source", "fuente finita", "有限源"), (1.4, 1.45), g=25)
    s.text(b, "N/(N_0 d/µm)", (0.15, 2.7), groesse=24, ausrichtung="left")
    for x0, c in fa.items():
        h = 2 / (sqrt(pi) * x0)
        s.daten(b, [(0.05 * i, h * exp(-(0.05 * i / x0)**2)) for i in range(101)], farbe=c, dicke=4)
    spalte(s, b, 3.9, (2.37, 2.05, 1.72, 1.4))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k13vorzeichen():
    """Vier Felder: Drift und Diffusion für Elektronen und Löcher, Teilchenstrom blau, elektrischer Strom rot."""
    s = Szene("gemb1/k13vorzeichen")
    xs = (-0.85, 2.05)
    ys = (0.4, -0.5)
    w, h = 1.35, 0.42
    t(s, s.tr("sp1", "Drift", "drift", "deriva", "漂移"), (xs[0], 1.5), g=26)
    t(s, s.tr("sp2", "Diffusion", "diffusion", "difusión", "扩散"), (xs[1], 1.5), g=26)
    s.pfeil((xs[0] - 0.55, 1.1), (xs[0] + 0.55, 1.1), "", farbe=GRUEN, dicke=4, spitze=0.17)
    t(s, "ℰ", (xs[0] + 0.85, 1.1), farbe=GRUEN, g=26)
    s.linie(None, (xs[1] - 0.6, 1.23), (xs[1] + 0.6, 0.95), farbe=GRUEN, dicke=4)
    t(s, "n, p", (xs[1] + 0.95, 1.05), farbe=GRUEN, g=24)
    zeilen = [(s.tr("ze", "Elektronen", "electrons", "electrones", "电子"), ys[0], (-1, +1), (+1, -1)),
              (s.tr("zl", "Löcher", "holes", "huecos", "空穴"), ys[1], (+1, +1), (+1, +1))]
    for name, y, dr, di in zeilen:
        t(s, name, (-2.35, y), a="right", g=24)
        for x, (pa, st) in zip(xs, (dr, di)):
            rahmen(s, x - w, x + w, y - h, y + h, farbe=GRAU, dicke=2)
            s.pfeil((x - 0.6 * pa, y + 0.17), (x + 0.6 * pa, y + 0.17), "", farbe=BLAU, dicke=4.5, spitze=0.18)
            s.pfeil((x - 0.6 * st, y - 0.17), (x + 0.6 * st, y - 0.17), "", farbe=ROT, dicke=4.5, spitze=0.18)
    s.pfeil((-1.95, -1.25), (-1.35, -1.25), "", farbe=BLAU, dicke=4.5, spitze=0.18)
    t(s, s.tr("leg1", "Teilchenstrom", "particle flow", "flujo de partículas", "粒子流"), (-1.25, -1.25), a="left", g=24)
    s.pfeil((1.05, -1.25), (1.65, -1.25), "", farbe=ROT, dicke=4.5, spitze=0.18)
    t(s, s.tr("leg2", "elektrischer Strom", "electric current", "corriente eléctrica", "电流"), (1.75, -1.25), a="left", g=24)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k13rekomb():
    """Links Generation und drei Wege der Rekombination, rechts Anstieg und Abklingen."""
    s = Szene("gemb1/k13rekomb")
    s.welt()
    xc = (-3.15, -2.25, -1.35, -0.45)
    yo, yu = 0.9, -0.7
    titel = (s.tr("wG", "Generation", "generation", "generación", "产生"), s.tr("wL", "Licht", "light", "luz", "发光"),
             s.tr("wW", "Wärme", "heat", "calor", "发热"), s.tr("wS", "tiefes Niveau", "deep level", "nivel profundo", "深能级"))
    for x in xc:
        s.linie(None, (x - 0.38, yo), (x + 0.38, yo), farbe=GRUEN, dicke=5)
        s.linie(None, (x - 0.38, yu), (x + 0.38, yu), farbe=GRUEN, dicke=5)
    t(s, "E_C", (xc[0] - 0.42, yo + 0.25), g=22, a="left", farbe=GRUEN)
    t(s, "E_V", (xc[0] - 0.42, yu + 0.22), g=22, a="left", farbe=GRUEN)
    s.pfeil((xc[0], yu + 0.08), (xc[0], yo - 0.1), "", farbe=BLAU, dicke=3.5, spitze=0.17)
    s.weg(None, "t", "0.1+0.07*sin(52*t)", xc[0] - 0.42, xc[0] - 0.05, farbe=ORANGE, dicke=2.5, n=91)
    s.text(None, "\\hbar\\omega", (xc[0] - 0.24, 0.42), groesse=22, ausrichtung="center", farbe=ORANGE)
    s.pfeil((xc[1], yo - 0.08), (xc[1], yu + 0.1), "", farbe=ROT, dicke=3.5, spitze=0.17)
    s.weg(None, "t", "0.1+0.07*sin(52*t)", xc[1] + 0.05, xc[1] + 0.42, farbe=ORANGE, dicke=2.5, n=91)
    s.text(None, "\\hbar\\omega", (xc[1] + 0.24, 0.42), groesse=22, ausrichtung="center", farbe=ORANGE)
    s.pfeil((xc[2], yo - 0.08), (xc[2], yu + 0.1), "", farbe=ROT, dicke=3.5, spitze=0.17)
    s.pfeil((xc[3], yo - 0.08), (xc[3], 0.2), "", farbe=ROT, dicke=3.5, spitze=0.15)
    s.linie(None, (xc[3] - 0.22, 0.1), (xc[3] + 0.22, 0.1), farbe=ORANGE, dicke=4)
    s.pfeil((xc[3], 0.0), (xc[3], yu + 0.1), "", farbe=ROT, dicke=3.5, spitze=0.15)
    for x, n in zip(xc, titel):
        t(s, n, (x, -1.03), g=22)
    a = s.achsen((0, 12), (0, 1.2), breite=2.25, hoehe=1.9, mitte=(1.7, 0.05), xl="t/\\tau_{rec}", yl="", xticks="0;2;4;6;8;10;12", yticks="0;0.5;1", xl_mitte=False)
    s.text(a, "\\Delta p_n/(G_p\\tau_{rec})", (0.3, 1.27), groesse=24, ausrichtung="left")
    s.kurve(a, "1-exp(-x)", x=(0, 6), farbe=BLAU, dicke=4.5)
    s.kurve(a, "(1-exp(-6))*exp(-(x-6))", x=(6, 12), farbe=BLAU, dicke=4.5)
    s.linie(a, (6, 0), (6, 1.2), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (6, 1), (7, 0), farbe=ROT, dicke=3, dash=DASH)
    s.text(a, "\\tau_{rec}", (7.45, 0.1), groesse=22, ausrichtung="left", farbe=ROT)
    s.band(a, 0, 6, 1.1, 1.17, farbe=ORANGE, deckung=0.8)
    s.text(a, s.tr("lan", "Licht an", "light on", "luz encendida", "开灯"), (3.0, 0.62), groesse=22, ausrichtung="center", farbe=ORANGE)
    s.text(a, s.tr("laus", "Licht aus", "light off", "luz apagada", "关灯"), (9.3, 0.62), groesse=22, ausrichtung="center", farbe=ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k13kreis():
    """Vier Kästen im Kreis, zwei Zuflüsse von außen."""
    s = Szene("gemb1/k13kreis")
    xl, xr, yo, yu = -1.75, 1.75, 0.52, -0.52
    bw, bh = 2.75, 0.62
    s.pfeil((xl + 0.5 * bw + 0.05, yo), (xr - 0.5 * bw - 0.05, yo), "", farbe=BLAU, dicke=4, spitze=0.2)
    s.pfeil((xr, yo - 0.5 * bh - 0.05), (xr, yu + 0.5 * bh + 0.05), "", farbe=BLAU, dicke=4, spitze=0.2)
    s.pfeil((xr - 0.5 * bw - 0.05, yu), (xl + 0.5 * bw + 0.05, yu), "", farbe=BLAU, dicke=4, spitze=0.2)
    s.pfeil((xl, yu + 0.5 * bh + 0.05), (xl, yo - 0.5 * bh - 0.05), "", farbe=BLAU, dicke=4, spitze=0.2)
    s.box(s.tr("b1", "Dichten n, p", "densities n, p", "densidades n, p", "密度 n, p"), (xl, yo), bw, bh, groesse=25, fuellung=HELLBLAU, farbe=BLAU)
    s.box(s.tr("b2", "Poisson: Feld ℰ", "Poisson: field ℰ", "Poisson: campo ℰ", "泊松：电场 ℰ"), (xr, yo), bw, bh, groesse=25, fuellung=HELLBLAU, farbe=BLAU)
    s.box(s.tr("b3", "Ströme j_n, j_p", "currents j_n, j_p", "corrientes j_n, j_p", "电流 j_n, j_p"), (xr, yu), bw, bh, groesse=25, fuellung=HELLBLAU, farbe=BLAU)
    s.box(s.tr("b4", "Kontinuität", "continuity", "continuidad", "连续性"), (xl, yu), bw, bh, groesse=25, fuellung=HELLBLAU, farbe=BLAU)
    s.pfeil((xr, yo + 0.62), (xr, yo + 0.5 * bh + 0.05), "", farbe=ROT, dicke=3.5, spitze=0.17)
    t(s, s.tr("io", "feste Ionen N_D^+, N_A^-", "fixed ions N_D^+, N_A^-", "iones fijos N_D^+, N_A^-", "固定离子 N_D^+, N_A^-"), (xr, yo + 0.8), farbe=ROT, g=24)
    s.pfeil((xl, yu - 0.62), (xl, yu - 0.5 * bh - 0.05), "", farbe=ROT, dicke=3.5, spitze=0.17)
    t(s, "G, R", (xl, yu - 0.8), farbe=ROT, g=24)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k13relax():
    """Links RC-Ersatz eines Halbleiterstücks, rechts ambipolares Paket."""
    s = Szene("gemb1/k13relax")
    s.welt()
    yo, yu, xc, xr = 0.75, -0.75, -3.4, -2.4
    bau(s, "capacitor", (xc, yo), (xc, yu), size=0.42)
    bau(s, "resistor", (xr, yo), (xr, yu), size=0.42)
    s.draht((xc, yo), (xr, yo))
    s.draht((xc, yu), (xr, yu))
    t(s, "C", (xc + 0.3, 0.3), g=24, a="left")
    t(s, "R", (xr + 0.25, 0.3), g=24, a="left")
    t(s, "=", (-1.78, 0.0), g=30)
    s.band(None, -1.45, -0.4, -0.55, 0.55, farbe=GRUEN, deckung=0.3)
    rahmen(s, -1.45, -0.4, -0.55, 0.55, farbe=GRUEN, dicke=2.5)
    t(s, "\\sigma", (-0.92, 0.25), g=26)
    t(s, "\\varepsilon_0\\varepsilon_r", (-0.92, -0.25), g=24)
    t(s, "A", (-0.92, 0.76), g=24)
    t(s, "d", (-0.92, -0.82), g=24)
    a = s.achsen((-4, 4), (0, 1.1), breite=2.7, hoehe=1.95, mitte=(1.75, 0.0), xl="x", yl="", xticks="-4;0;4", xzahlen=False, yzahlen=False, ymarks=False, xl_mitte=False)
    s.text(a, "\\Delta n, \\Delta p", (-3.8, 1.14), groesse=24, ausrichtung="left")
    s.kurve(a, "0.62*exp(-x*x/3.6)", x=(-4, 4), farbe=GRUEN, dicke=4.5)
    s.kurve(a, "1.0*exp(-x*x/1.3)", x=(-4, 4), farbe=ROT, dicke=4.5)
    s.text(a, "p", (0.72, 0.95), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "n", (-2.05, 0.42), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(a, "+", (0, 0.12), groesse=28, ausrichtung="center", farbe=ROT)
    s.text(a, "−", (2.15, 0.05), groesse=30, ausrichtung="center", farbe=GRUEN)
    s.text(a, "−", (-2.15, 0.05), groesse=30, ausrichtung="center", farbe=GRUEN)
    s.pfeil((1.5, 0.72), (3.1, 0.72), "", farbe=SCHWARZ, dicke=3.5, spitze=0.16, on=a)
    s.pfeil((-1.5, 0.72), (-3.1, 0.72), "", farbe=SCHWARZ, dicke=3.5, spitze=0.16, on=a)
    s.text(a, "ℰ", (2.3, 0.84), groesse=26, ausrichtung="center")
    s.text(a, "ℰ", (-2.3, 0.84), groesse=26, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k13laenge():
    """Drei Bilder: exponentielles Profil mit Tangente, dünne Platte, Paket nach dem Blitz."""
    s = Szene("gemb1/k13laenge")
    s.welt()
    w, h = 1.85, 1.85
    a = s.achsen((0, 4), (0, 1.05), breite=w, hoehe=h, mitte=(-2.2, -0.1), xl="x/L_{diff,p}", yl="", xticks="0;1;2;3", yticks="0;0.5;1")
    s.text(a, "\\Delta p_n/\\Delta p_n(0)", (0.1, 1.17), groesse=22, ausrichtung="left")
    s.kurve(a, "exp(-x)", x=(0, 4), farbe=BLAU, dicke=4.5)
    s.kurve(a, "1-x", x=(0, 1), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(a, 1, 0, farbe=ROT, r=0.07)
    s.linie(a, (1, 0), (1, exp(-1)), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "0.37", (1.15, 0.42), groesse=22, ausrichtung="left", farbe=BLAU)
    b = s.achsen((0, 1), (0, 1.05), breite=w, hoehe=h, mitte=(0.12, -0.1), xl="x/d", yl="", xticks="0;0.5;1", yticks="0.5;1")
    for r, c in ((0.5, BLAU), (1.0, ROT), (2.0, GRUEN)):
        s.daten(b, [(0.02 * i, sinh((1 - 0.02 * i) * r) / sinh(r)) for i in range(51)], farbe=c, dicke=4)
    s.kurve(b, "1-x", x=(0, 1), farbe=GRAU, dicke=2, dash=DASH)
    s.text(b, "d/L_{diff,p}", (1.0, 1.0), groesse=22, ausrichtung="right")
    s.text(b, "0.5", (0.82, 0.84), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(b, "1", (0.82, 0.71), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(b, "2", (0.82, 0.58), groesse=22, ausrichtung="center", farbe=GRUEN)
    c = s.achsen((-3, 3), (0, 1.05), breite=w, hoehe=h, mitte=(2.3, -0.1), xl="x", yl="", xticks="-3;0;3", yticks="0;0.5;1", xzahlen=False, yzahlen=False)
    s.text(c, "\\Delta p_n", (-2.85, 1.17), groesse=22, ausrichtung="left")
    for tt, fa in ((0.05, BLAU), (0.15, ROT), (0.4, GRUEN)):
        hh = sqrt(0.05 / tt) * exp(-(tt - 0.05) / 0.5)
        v = 4 * tt
        s.kurve(c, "%.4f*exp(-x*x/%.4f)" % (hh, v * 2), x=(-3, 3), farbe=fa, dicke=4)
    s.text(c, "t_1", (0.72, 0.8), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(c, "t_2", (1.12, 0.33), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(c, "t_3", (2.05, 0.26), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.speichern()


if __name__ == "__main__":
    for f in (k13fick, k13kontinuitaet, k13quellen, k13vorzeichen, k13rekomb, k13kreis, k13relax, k13laenge):
        f()
