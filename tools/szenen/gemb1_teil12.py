"""GEMB 1 Teil 12 (kap12_stufen.tex): Strom im Halbleiter.

Aufruf: python tools/szenen/gemb1_teil12.py, danach python tools/szenen_ansehen.py out.png gemb1/k12besetzung ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap12.py.
"""
import re
import sys
from math import cos, exp, log, pi, sin, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLBLAU, HELLROT, HELLGRUEN = "#dceafa", "#f6dede", "#ddf0e4"
KB = 8.617333e-5
QE = 1.602176634e-19
EG, NC300, NV300 = 1.12, 2.82e19, 1.83e19
MUN, MUP, MIN, MIP = 1400.0, 450.0, 8400.0, 6000.0


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    key = "a_" + re.sub(r"\W", "", name + einheit)
    return s.tr(key, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def ring(s, on, x, y, r=0.075, farbe=ROT):
    """Offener Kreis mit gleichem Radius in x und y, auch auf verzerrten Achsen."""
    return s._add("Dot", {"center": [x, y, 0], "radius": r, "color": farbe, "fill_color": "#ffffff", "fill_opacity": 1, "stroke_width": 2.5}, on)


def ex(x):
    return exp(max(min(x, 690.0), -690.0))


def Nc(T):
    return NC300 * (T / 300)**1.5


def Nv(T):
    return NV300 * (T / 300)**1.5


def ni(T):
    return sqrt(Nc(T) * Nv(T)) * ex(-EG / (2 * KB * T))


def loesen(T, Nd=0.0, Na=0.0, dD=0.045, dA=0.045, gA=4.0):
    kt = KB * T
    nc, nv = Nc(T), Nv(T)

    def q(E):
        n = nc * ex(-(EG - E) / kt)
        p = nv * ex(-E / kt)
        nd = Nd / (1 + 2 * ex((E - (EG - dD)) / kt)) if Nd else 0.0
        na = Na / (1 + gA * ex((dA - E) / kt)) if Na else 0.0
        return p + nd - n - na, n, p

    lo, hi = -0.3, EG + 0.3
    for _ in range(200):
        m = (lo + hi) / 2
        if q(m)[0] > 0:
            lo = m
        else:
            hi = m
    return q(m)[1], q(m)[2]


def muph(T, m300=MUN):
    return m300 * (T / 300)**-1.5


def muion(T, N, m300=MIN):
    return m300 * (N / 1e16)**-0.7 * (T / 300)**1.5


def mu(T, N, mp=MUN, mi=MIN):
    return 1 / (1 / muph(T, mp) + 1 / muion(T, N, mi))


# ------------------------------------------------------------------------------------------ Stufe 1
def bandbild(s, mitte, titel, sh):
    a = s.achsen((-1.12, 1.12), (-3.5, 3.5), breite=2.8, hoehe=2.95, mitte=mitte, kreuz=True, xl="k", yl="", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.kurve(a, "1+(1-cos(pi*x))", x=(-1, 1), farbe=GRUEN, dicke=3)
    s.kurve(a, "-1-(1-cos(pi*x))", x=(-1, 1), farbe=GRUEN, dicke=3)
    frei = [n + sh for n in (-1, 0, 1)]
    for n in range(-7, 9):
        u = n / 8
        el = n in frei
        if el:
            s.punkt(a, u, 1 + (1 - cos(pi * u)), farbe=BLAU, r=0.075)
            ring(s, a, u, -1 - (1 - cos(pi * u)))
        else:
            s.punkt(a, u, -1 - (1 - cos(pi * u)), farbe=BLAU, r=0.075)
    s.linie(a, (-1, -3.5), (-1, 3.3), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(a, (1, -3.5), (1, 3.3), farbe=GRAU, dicke=1.5, dash=DOT)
    s.text(a, "-\\pi/a", (-0.8, -3.3), groesse=22, ausrichtung="center")
    s.text(a, "\\pi/a", (0.82, -3.3), groesse=22, ausrichtung="center")
    s.text(a, "E", (0.12, 3.4), groesse=24, ausrichtung="left")
    t(s, titel, (mitte[0], 1.92), g=26)
    return a


def k12besetzung():
    """Links Gleichgewicht, rechts mit Kraft: Elektronen im Leitungsband und leere Plätze im Valenzband rutschen nach rechts."""
    s = Szene("gemb1/k12besetzung")
    s.welt()
    a = bandbild(s, (-1.75, 0.0), s.tr("glg", "Gleichgewicht", "equilibrium", "equilibrio", "平衡"), 0)
    b = bandbild(s, (1.75, 0.0), s.tr("mkraft", "mit Kraft F", "with force F", "con fuerza F", "有外力 F"), 2)
    s.text(a, "j = 0", (0.62, 0.62), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, "j = 0", (0.62, -0.62), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("lb", "Leitungsband", "conduction band", "banda de conducción", "导带"), (-0.56, 0.6), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.text(a, s.tr("vb", "Valenzband", "valence band", "banda de valencia", "价带"), (-0.56, -0.6), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.pfeil((0.26, 1.0), (0.74, 1.0), "", farbe=ROT, dicke=3.5, spitze=0.13, on=b)
    s.text(b, "v>0", (0.5, 0.62), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(b, "j<0", (-0.55, 1.7), groesse=GR, ausrichtung="center", farbe=ROT)
    s.pfeil((0.74, -0.95), (0.26, -0.95), "", farbe=ROT, dicke=3.5, spitze=0.13, on=b)
    s.text(b, "v<0", (0.5, -0.58), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(b, "j<0", (-0.55, -0.55), groesse=GR, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k12bloch():
    """Links ohne Stöße: k läuft durch die Zone, v pendelt. Rechts mit Stößen: k bleibt in der Nähe von null."""
    s = Szene("gemb1/k12bloch")
    s.welt()
    a = s.achsen((0, 2), (-1.2, 1.2), breite=2.75, hoehe=2.3, mitte=(-1.75, 0.05), xl="t/T_B", yl="", xticks="0;0.5;1;1.5;2", yticks="-1;0;1")
    t(s, s.tr("ohne", "ohne Stöße", "without collisions", "sin colisiones", "无碰撞"), (-1.75, 1.55), g=26)
    for t0, t1 in ((0, 0.5), (0.5, 1.5), (1.5, 2.0)):
        s.daten(a, [(t0, 2 * t0 if t0 == 0 else 2 * (t0 - 1)), (t1, 2 * t1 if t0 == 0 else 2 * (t1 - 1))], farbe=BLAU, dicke=4)
    s.linie(a, (0.5, 1), (0.5, -1), farbe=BLAU, dicke=1.5, dash=DOT)
    s.linie(a, (1.5, 1), (1.5, -1), farbe=BLAU, dicke=1.5, dash=DOT)
    s.kurve(a, "sin(2*pi*x)", x=(0, 2), farbe=ROT, dicke=4)
    s.text(a, "ka/\\pi", (0.25, -0.62), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "v/v_{max}", (1.75, 0.8), groesse=24, ausrichtung="center", farbe=ROT)
    zeiten = [1.3, 0.4, 2.1, 0.8, 0.2, 1.6, 0.9, 0.5, 1.2, 2.2, 0.7]
    b = s.achsen((0, 12), (0, 3), breite=2.75, hoehe=2.3, mitte=(1.95, 0.05), xl="t/\\tau", yl="", xticks="0;3;6;9;12", yticks="0;1;2;3")
    t(s, s.tr("mit", "mit Stößen", "with collisions", "con colisiones", "有碰撞"), (1.95, 1.55), g=26)
    s.text(b, "\\hbar k/(F\\tau)", (0.4, 2.8), groesse=22, ausrichtung="left")
    tt = 0.0
    pts = [(0.0, 0.0)]
    for z in zeiten:
        pts += [(tt + z, z), (tt + z, 0.0)]
        tt += z
    pts.append((12.0, 12.0 - tt))
    s.daten(b, pts, farbe=BLAU, dicke=3.5)
    s.linie(b, (0, 1), (12, 1), farbe=ROT, dicke=3, dash=DASH)
    s.text(b, s.tr("mittel", "Mittelwert", "mean", "media", "平均"), (6.2, 2.1), groesse=22, ausrichtung="center", farbe=ROT)
    s.pfeil((6.2, 1.9), (6.2, 1.05), "", farbe=ROT, dicke=2, spitze=0.1, on=b)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k12phasenraum():
    """Links das Wellenpaket und sein Kästchen in der x-k-Ebene, rechts die Bewegung des Kästchens längs der Bahn."""
    s = Szene("gemb1/k12phasenraum")
    s.welt()
    a = s.achsen((-3, 3), (-1.25, 1.25), breite=2.6, hoehe=0.9, mitte=(-1.9, 1.3), xl="", yl="\\psi", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, kreuz=True)
    s.kurve(a, "exp(-x*x)*cos(12*x)", x=(-2.6, 2.6), farbe=BLAU, dicke=2.5)
    s.kurve(a, "exp(-x*x)", x=(-2.6, 2.6), farbe=ROT, dicke=2.5)
    b = s.achsen((-3, 3), (0, 4), breite=2.6, hoehe=1.5, mitte=(-1.9, -0.82), xl="x", yl="k", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, kreuz=True)
    s.band(b, -0.72, 0.72, 1.3, 2.7, farbe=BLAU, deckung=0.3)
    s.punkt(b, 0, 2, farbe=SCHWARZ, r=0.07)
    s.pfeil((-0.72, 0.85), (0.72, 0.85), "", farbe=ROT, dicke=2.5, spitze=0.1, on=b, doppelt=True)
    s.text(b, "2\\Delta x", (1.5, 0.85), groesse=22, ausrichtung="center", farbe=ROT)
    s.pfeil((1.0, 1.3), (1.0, 2.7), "", farbe=ROT, dicke=2.5, spitze=0.1, on=b, doppelt=True)
    s.text(b, "2\\Delta k", (1.85, 2.0), groesse=22, ausrichtung="center", farbe=ROT)
    c = s.achsen((0, 10), (0, 10), breite=2.95, hoehe=3.1, mitte=(1.72, -0.05), xl="x", yl="k", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, kreuz=True)
    s.weg(c, "1+0.08*t*t", "t", 0.3, 9.6, farbe=GRAU, dicke=3)
    t1, t2 = 3.4, 6.4
    x1, x2 = 1 + 0.08 * t1**2, 1 + 0.08 * t2**2
    wx, wk = 0.95, 0.72
    s.band(c, x1 - wx, x1 + wx, t1 - wk, t1 + wk, farbe=GRAU, deckung=0.3)
    s.band(c, x2 - wx, x2 + wx, t2 - wk, t2 + wk, farbe=BLAU, deckung=0.35)
    s.punkt(c, x1, t1, farbe=SCHWARZ, r=0.065)
    s.punkt(c, x2, t2, farbe=SCHWARZ, r=0.065)
    s.pfeil((x1, t1), (x2, t1), "", farbe=ROT, dicke=3, spitze=0.12, on=c)
    s.pfeil((x2, t1), (x2, t2), "", farbe=GRUEN, dicke=3, spitze=0.12, on=c)
    s.text(c, "v\\,dt", ((x1 + x2) / 2 + 0.2, t1 - 0.72), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(c, "F\\,dt/\\hbar", (x2 + 2.05, (t1 + t2) / 2 - 0.1), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.text(c, "t", (x2 - 1.0, t2 + 1.1), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(c, "t-dt", (x1 - 0.1, t1 + 1.1), groesse=22, ausrichtung="center", farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k12gleichgewicht():
    """Links Dotierverlauf mit waagerechtem E_F, rechts homogene Dotierung mit geneigtem E_F."""
    s = Szene("gemb1/k12gleichgewicht")
    s.welt()
    a = s.achsen((0, 100), (-120, 320), breite=2.6, hoehe=2.3, mitte=(-1.7, 0.0), xl=achse(s, "x", "µm"), yl="", xticks="0;50;100", yticks="-100;0;100;200;300")
    t(s, s.tr("g1", "Dotierverlauf, kein Strom", "graded doping, no current", "dopado variable, sin corriente", "渐变掺杂，无电流"), (-1.7, 1.5), g=24)
    s.text(a, achse(s, "E", "meV"), (4, 305), groesse=22, ausrichtung="left")
    Ec = lambda x: 145.8 + 119.1 * x / 100
    s.daten(a, [(x, Ec(x)) for x in (0, 100)], farbe=GRUEN, dicke=4.5)
    s.linie(a, (0, 0), (100, 0), farbe=ROT, dicke=3.5, dash=DASH)
    s.text(a, "E_C(x)", (62, 165), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.text(a, "E_F", (88, 30), groesse=GR, ausrichtung="center", farbe=ROT)
    x = 3.0
    while x < 100:
        s.punkt(a, x, Ec(x) + 28, farbe=BLAU, r=0.045)
        x += 3.2 * ex(x * 0.0165)
    b = s.achsen((0, 100), (-120, 320), breite=2.6, hoehe=2.3, mitte=(1.75, 0.0), xl=achse(s, "x", "µm"), yl="", xticks="0;50;100", yticks="-100;0;100;200;300")
    t(s, s.tr("g2", "homogen, Strom", "uniform, current flows", "homogéneo, con corriente", "均匀，有电流"), (1.75, 1.5), g=24)
    s.daten(b, [(0, 205.3), (100, 105.3)], farbe=GRUEN, dicke=4.5)
    s.daten(b, [(0, 0), (100, -100)], farbe=ROT, dicke=3.5, dash=DASH)
    s.text(b, "E_C(x)", (70, 45), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.text(b, "E_F(x)", (32, -72), groesse=GR, ausrichtung="center", farbe=ROT)
    x = 3.0
    while x < 100:
        s.punkt(b, x, 205.3 - x + 28, farbe=BLAU, r=0.045)
        x += 8.5
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k12streuung():
    """Links Streuung hinein und heraus im Band, rechts Abklingen der Abweichung bei den Zeiten des Rechenmodells."""
    s = Szene("gemb1/k12streuung")
    s.welt()
    a = s.achsen((-1.15, 1.15), (0, 2.2), breite=2.7, hoehe=2.3, mitte=(-1.95, 0.0), kreuz=True, xl="k", yl="", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    t(s, s.tr("zk", "ein Zustand k", "one state k", "un estado k", "一个状态 k"), (-1.95, 1.72), g=24)
    s.text(a, "E", (0.08, 2.15), groesse=24, ausrichtung="left")
    s.kurve(a, "1.6*x*x", x=(-1.1, 1.1), farbe=GRUEN, dicke=3.5)
    kk, kp = 0.55, -0.82
    Ek, Ep = 1.6 * kk**2, 1.6 * kp**2
    s.punkt(a, kk, Ek, farbe=BLAU, r=0.09)
    ring(s, a, kp, Ep, r=0.09, farbe=BLAU)
    s.pfeil((kp + 0.1, Ep + 0.13), (kk - 0.08, Ek + 0.14), "", farbe=ROT, dicke=3.5, spitze=0.13, on=a)
    s.pfeil((kk - 0.1, Ek - 0.12), (kp + 0.12, Ep - 0.13), "", farbe=BLAU, dicke=3.5, spitze=0.13, on=a)
    s.text(a, "k", (kk + 0.1, Ek - 0.16), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "k'", (kp - 0.12, Ep - 0.16), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("hinein", "hinein", "in", "entrada", "入"), (-0.42, 1.38), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("heraus", "heraus", "out", "salida", "出"), (0.98, 0.32), groesse=22, ausrichtung="center", farbe=BLAU)
    b = s.achsen((0, 1.5), (0, 1.05), breite=2.8, hoehe=2.3, mitte=(1.85, 0.0), xl=achse(s, "t", "ps"), yl="", xticks="0;0.5;1;1.5", yticks="0;0.25;0.5;0.75;1")
    t(s, "\\delta f(t)/\\delta f(0)", (1.85, 1.72), g=24)
    TS = {"ion": (1.242, GRUEN), "ph": (0.207, ORANGE), "sc": (0.177, BLAU)}
    for k_, (ta, fa) in TS.items():
        s.kurve(b, "exp(-x/%g)" % ta, x=(0, 1.5), farbe=fa, dicke=4 if k_ != "sc" else 4.5)
    s.text(b, "\\tau_{ion}=1.24\\,ps", (1.05, 0.56), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.text(b, "\\tau_{ph}=0.21\\,ps", (0.98, 0.25), groesse=22, ausrichtung="center", farbe=ORANGE)
    s.text(b, "\\tau_{scat}=0.18\\,ps", (0.98, 0.13), groesse=22, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k12verschoben():
    """Oben f0 und f, unten f - f0: Halbleiter (Boltzmann) und Metall (Fermi-Kante). Verschiebung stark übertrieben."""
    s = Szene("gemb1/k12verschoben")
    s.welt()
    dk = 0.45
    fh = lambda k: exp(-k * k / 2)
    a = s.achsen((-3.3, 3.3), (0, 1.1), breite=2.75, hoehe=1.2, mitte=(-1.75, 0.75), xl="", yl="", xzahlen=False, xmarks=False, xticks="", yticks="0;1")
    t(s, s.tr("hl", "Halbleiter", "semiconductor", "semiconductor", "半导体"), (-1.75, 1.62), g=26)
    X = np.linspace(-3.3, 3.3, 121)
    s.daten(a, [(x, fh(x)) for x in X], farbe=GRAU, dicke=3, dash=DASH)
    s.daten(a, [(x, fh(x - dk)) for x in X], farbe=BLAU, dicke=4)
    s.text(a, "f^0", (-1.9, 0.75), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "f", (2.0, 0.55), groesse=22, ausrichtung="center", farbe=BLAU)
    s.pfeil((0, 1.05), (dk, 1.05), "", farbe=ROT, dicke=3, spitze=0.1, on=a)
    s.text(a, "\\delta k", (1.0, 1.02), groesse=22, ausrichtung="center", farbe=ROT)
    b = s.achsen((-3.3, 3.3), (-0.5, 0.5), breite=2.75, hoehe=0.95, mitte=(-1.75, -0.8), xl="k", yl="", xzahlen=False, xmarks=False, xticks="", yzahlen=False, ymarks=False)
    s.text(b, "f-f^0", (-2.5, 0.38), groesse=22, ausrichtung="center", farbe=ROT)
    s.linie(b, (-3.3, 0), (3.3, 0), farbe=GRAU, dicke=1.5)
    s.daten(b, [(x, fh(x - dk) - fh(x)) for x in X], farbe=ROT, dicke=4)
    fm = lambda k: 1 / (1 + ex((k * k - 4) / 0.45))
    c = s.achsen((-3.3, 3.3), (0, 1.1), breite=2.75, hoehe=1.2, mitte=(1.95, 0.75), xl="", yl="", xzahlen=False, xmarks=False, xticks="", yticks="0;1")
    t(s, s.tr("mt", "Metall", "metal", "metal", "金属"), (1.95, 1.62), g=26)
    Y = np.linspace(-3.3, 3.3, 241)
    s.daten(c, [(x, fm(x)) for x in Y], farbe=GRAU, dicke=3, dash=DASH)
    s.daten(c, [(x, fm(x - dk)) for x in Y], farbe=BLAU, dicke=4)
    s.linie(c, (2, 0), (2, 1.1), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(c, (-2, 0), (-2, 1.1), farbe=GRAU, dicke=1.5, dash=DOT)
    s.text(c, "k_F", (2.75, 0.82), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(c, "-k_F", (-2.75, 0.82), groesse=22, ausrichtung="center", farbe=GRAU)
    d = s.achsen((-3.3, 3.3), (-1.0, 1.0), breite=2.75, hoehe=0.95, mitte=(1.95, -0.8), xl="k", yl="", xzahlen=False, xmarks=False, xticks="", yzahlen=False, ymarks=False)
    s.linie(d, (-3.3, 0), (3.3, 0), farbe=GRAU, dicke=1.5)
    s.daten(d, [(x, fm(x - dk) - fm(x)) for x in Y], farbe=ROT, dicke=4)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k12beweglichkeit():
    """Beweglichkeit über T und N, Leitfähigkeit über 1000/T, spezifischer Widerstand über N."""
    s = Szene("gemb1/k12beweglichkeit")
    Ts = list(np.logspace(2, 3, 41))
    w, h_ = 2.48, 1.5
    xl, xr, yo, yu = -1.8, 2.08, 1.4, -1.5
    einh = "cm^2/(V\\,s)"
    a = s.achsen((100, 1000), (50, 2e4), breite=w, hoehe=h_, mitte=(xl, yo), xl=achse(s, "T", "K"), yl=s.tr("mu_a", "\\mu_n in " + einh, "\\mu_n in " + einh, "\\mu_n en " + einh, "\\mu_n / " + einh), xlog=True, ylog=True, xticks="100;1000", yticks="100;1000;10000")
    s.daten(a, [(T, muph(T)) for T in Ts], farbe=ORANGE, dicke=3, dash=DASH)
    s.daten(a, [(T, muion(T, 1e16)) for T in Ts], farbe=GRUEN, dicke=3, dash=DASH)
    for N, d in ((1e16, 4.5), (1e17, 3.2), (1e18, 3.2)):
        s.daten(a, [(T, mu(T, N)) for T in Ts], farbe=BLAU, dicke=d)
    s.text(a, "T^{-3/2}", (200, 7500), groesse=22, ausrichtung="center", farbe=ORANGE)
    s.text(a, "T^{+3/2}", (480, 6200), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.text(a, "10^{16}", (150, 820), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "10^{17}", (160, 225), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "10^{18}", (240, 72), groesse=22, ausrichtung="center", farbe=BLAU)
    Ns = list(np.logspace(14, 19, 41))
    b = s.achsen((1e14, 1e19), (30, 3000), breite=w, hoehe=h_, mitte=(xr, yo), xl=achse(s, "N", "cm^{-3}"), yl=s.tr("mu_b", "\\mu in " + einh, "\\mu in " + einh, "\\mu en " + einh, "\\mu / " + einh), xlog=True, ylog=True, xticks="1e14;1e16;1e18", yticks="100;1000")
    s.daten(b, [(N, mu(300, N)) for N in Ns], farbe=BLAU, dicke=4)
    s.daten(b, [(N, mu(300, N, MUP, MIP)) for N in Ns], farbe=ROT, dicke=4)
    s.text(b, "\\mu_n", (6e15, 1900), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b, "\\mu_p", (6e15, 260), groesse=GR, ausrichtung="center", farbe=ROT)
    c = s.achsen((1, 12), (0.1, 20), breite=w, hoehe=h_, mitte=(xl, yu), xl=achse(s, "1000/T", "1/K"), yl=achse(s, "\\sigma", "S/cm"), ylog=True, xticks="2;4;6;8;10;12", yticks="0.1;1;10")
    pts = []
    for u in np.linspace(1, 12, 111):
        T = 1000 / u
        n, p = loesen(T, Nd=1e16)
        pts.append((u, QE * (n * mu(T, 1e16) + p * mu(T, 1e16, MUP, MIP))))
    s.daten(c, pts, farbe=BLAU, dicke=4)
    s.text(c, "I", (2.0, 8), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(c, "II", (4.5, 5.0), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(c, "III", (10.8, 2.6), groesse=GR, ausrichtung="center", farbe=ROT)
    d = s.achsen((1e14, 1e19), (1e-3, 1e2), breite=w, hoehe=h_, mitte=(xr, yu), xl=achse(s, "N", "cm^{-3}"), yl=achse(s, "\\rho", "\\Omega\\,cm"), xlog=True, ylog=True, xticks="1e14;1e16;1e18", yticks="0.01;1;100")
    s.daten(d, [(N, 1 / (QE * N * mu(300, N))) for N in Ns], farbe=BLAU, dicke=4)
    s.daten(d, [(N, 1 / (QE * N * mu(300, N, MUP, MIP))) for N in Ns], farbe=ROT, dicke=4)
    s.text(d, "n", (2e15, 0.25), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(d, "p", (6e15, 9), groesse=GR, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k12hall():
    """Links die Platte von oben, rechts der Hall-Koeffizient von n- und p-Silizium über 1000/T."""
    s = Szene("gemb1/k12hall")
    s.welt()
    x0, x1, y0, y1 = -3.1, 0.2, -1.15, 1.15
    s.band(None, x0, x1, y0, y1, farbe=BLAU, deckung=0.09)
    s.draht((x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0), dicke=3)
    s.pfeil((x0 - 0.42, 0), (x0 - 0.02, 0), "", farbe=SCHWARZ, dicke=3.5, spitze=0.14)
    t(s, "I", (x0 - 0.3, 0.3), g=26)
    s.pfeil((x1 + 0.02, 0), (x1 + 0.42, 0), "", farbe=SCHWARZ, dicke=3.5, spitze=0.14)
    for i in range(7):
        xm = x0 + 0.3 + i * 0.45
        t(s, "-", (xm, y0 + 0.2), farbe=BLAU, g=30)
        t(s, "+", (xm, y1 - 0.2), farbe=ROT, g=26)
    for (bx, by) in ((-2.75, 0.55), (-0.15, -0.55), (-0.15, 0.55), (-2.75, -0.55)):
        s.kreis(None, bx, by, 0.12, farbe=GRAU, dicke=2, fuellung="#ffffff", deckung=1.0)
        s.punkt(None, bx, by, farbe=GRAU, r=0.035)
    t(s, "B", (-2.4, 0.55), farbe=GRAU, g=24)
    xe, ye = -1.4, 0.02
    s.punkt(None, xe, ye, farbe=BLAU, r=0.1)
    s.pfeil((xe - 0.1, ye), (xe - 0.82, ye), "", farbe=BLAU, dicke=3.5, spitze=0.13)
    t(s, "v_d", (xe - 0.62, ye + 0.25), farbe=BLAU, g=24)
    s.pfeil((xe, ye - 0.1), (xe, ye - 0.62), "", farbe=ROT, dicke=3.5, spitze=0.13)
    t(s, "F_L", (xe + 0.3, ye - 0.42), farbe=ROT, g=24)
    s.pfeil((xe, ye + 0.1), (xe, ye + 0.62), "", farbe=GRUEN, dicke=3.5, spitze=0.13)
    t(s, "F_H", (xe + 0.3, ye + 0.42), farbe=GRUEN, g=24)
    s.pfeil((-0.62, 0.62), (-0.62, -0.62), "", farbe=ORANGE, dicke=3.5, spitze=0.13)
    t(s, "ℰ_H", (-0.72, 0.0), farbe=ORANGE, g=24, a="right")
    s.draht((-1.4, y1), (-1.4, y1 + 0.45), dicke=2.5)
    s.draht((-1.4, y0), (-1.4, y0 - 0.45), dicke=2.5)
    s.punkt(None, -1.4, y1 + 0.45, farbe=SCHWARZ, r=0.05)
    s.punkt(None, -1.4, y0 - 0.45, farbe=SCHWARZ, r=0.05)
    t(s, "U_H", (-0.98, y1 + 0.38), g=24)
    ox, oy = -3.1, -2.05
    s.pfeil((ox, oy), (ox + 0.45, oy), "", farbe=SCHWARZ, dicke=2.5, spitze=0.11)
    s.pfeil((ox, oy), (ox, oy + 0.45), "", farbe=SCHWARZ, dicke=2.5, spitze=0.11)
    t(s, "x", (ox + 0.62, oy), g=22)
    t(s, "y", (ox - 0.18, oy + 0.42), g=22)
    s.kreis(None, ox, oy, 0.09, farbe=SCHWARZ, dicke=2, fuellung="#ffffff", deckung=1.0)
    s.punkt(None, ox, oy, farbe=SCHWARZ, r=0.03)
    t(s, "z", (ox - 0.26, oy - 0.05), g=22)
    a = s.achsen((1, 4), (1, 3000), breite=2.5, hoehe=2.5, mitte=(2.15, 0.0), xl=achse(s, "1000/T", "1/K"), yl=achse(s, "|R_H|", "cm^3/C"), ylog=True, xticks="1;2;3;4", yticks="1;10;100;1000")
    b = MUN / MUP

    def rh(T, Nd=0.0, Na=0.0):
        n, p = loesen(T, Nd=Nd, Na=Na)
        return (p - n * b * b) / (QE * (p + n * b)**2)

    X = list(np.linspace(1, 4, 121))
    s.daten(a, [(u, abs(rh(1000 / u, Nd=1e16))) for u in X], farbe=BLAU, dicke=4)
    Y = sorted(set(list(np.linspace(1, 4, 121)) + list(np.linspace(1.45, 1.6, 121))))
    s.daten(a, [(u, max(abs(rh(1000 / u, Na=1e16)), 1.0)) for u in Y], farbe=ROT, dicke=4)
    s.text(a, "n: R_H<0", (2.9, 1500), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "p: R_H>0", (2.9, 250), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, "R_H=0", (2.25, 4), groesse=22, ausrichtung="center", farbe=ROT)
    s.speichern()


if __name__ == "__main__":
    for f in (k12besetzung, k12bloch, k12phasenraum, k12gleichgewicht, k12streuung, k12verschoben, k12beweglichkeit, k12hall):
        f()
    print("gemb1 Teil 12: Szenen geschrieben")
