"""GEMB 1 Teil 10 (kap10_stufen.tex): Zustandsdichte und Fermi-Verteilung.

Aufruf: python tools/szenen/gemb1_teil10.py, danach python tools/szenen_ansehen.py out.png gemb1/k10band ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap10.py.
"""
import sys
from collections import defaultdict
from math import acos, comb, cos, exp, pi, sin, sqrt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#ddf0e4"
C0 = 0.038100                       # hbar^2/(2 m0) in eV nm^2
KB = 8.617333e-5                    # eV/K
KT = KB * 300
EG, MC, MV = 1.12, 1.08, 0.81       # Silizium
D3M0 = 6.8122                       # D(1 eV) für m0 in 1/(eV nm^3), also 6,81e21 1/(eV cm^3)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def poly(s, on, ecken, farbe, deckung=0.2, rand=None, dicke=0):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": rand or farbe, "fill_color": farbe,
                              "fill_opacity": deckung, "stroke_width": dicke}, on)


def achse(s, name, einheit):
    return s.tr("a_" + name + einheit, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def d3(e, m):
    """Zustandsdichte in 10^21/(eV cm^3)."""
    return D3M0 * m**1.5 * sqrt(max(e, 0.0))


# ------------------------------------------------------------------------------------------ Stufe 1
def k10band():
    """Kosinus-Band: gleich breite Energiefenster schneiden verschieden lange k-Stücke aus; daneben D(E)."""
    s = Szene("gemb1/k10band")
    em = 2.2
    a = s.achsen((-1, 1), (0, em), breite=3.0, hoehe=2.1, mitte=(-1.85, 0.1), xl=s.tr("k_pi", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)"),
                 yl=achse(s, "E", "eV"), xticks="-1;0;1", yticks="0;1;2")
    fenster = ((0.05, 0.25), (0.9, 1.1))
    for (e0, e1), farbe in zip(fenster, (GRUEN, ORANGE)):
        s.band(a, -1, 1, e0, e1, farbe=farbe, deckung=0.16)
        x0, x1 = acos(1 - e0) / pi, acos(1 - e1) / pi
        for x in (x0, x1):
            s.linie(a, (x, 0), (x, 1 - cos(pi * x)), farbe=farbe, dicke=1.5, dash=DASH)
        s.linie(a, (x0, 0.04), (x1, 0.04), farbe=farbe, dicke=8)
    s.kurve(a, "1-cos(pi*x)", farbe=BLAU, dicke=5)
    xm = sqrt(2.2 / (0.5 * pi * pi))
    s.kurve(a, "0.5*pi*pi*x*x", x=(-xm, xm), farbe=ROT, dicke=3, dash=DASH)
    for i in range(-10, 11):
        s.punkt(a, i / 10, 0.0, farbe=SCHWARZ, r=0.03)
    b = s.achsen((0, 10), (0, em), breite=2.4, hoehe=2.1, mitte=(1.9, 0.1), xl=s.tr("d_einheit", "D in 1/(eV nm)", "D in 1/(eV nm)", "D en 1/(eV nm)", "D / (1/(eV nm))"),
                 yl="", xticks="0;5;10", yticks="0;1;2", yzahlen=False)
    for (e0, e1), farbe in zip(fenster, (GRUEN, ORANGE)):
        s.band(b, 0, 10, e0, e1, farbe=farbe, deckung=0.16)
    ko = []
    for i in range(1, 400):
        e = 2 * i / 400
        d = 2.54648 / sqrt(e * (2 - e))
        if d <= 10:
            ko.append((d, e))
    s.daten(b, ko, farbe=BLAU, dicke=5)
    s.daten(b, [(1.8006 / sqrt(e / 100), e / 100) for e in range(4, 215)], farbe=ROT, dicke=3, dash=DASH)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k10kugel():
    """Fläche gleicher Energie in 1D, 2D, 3D und die zugehörige Zustandsdichte."""
    s = Szene("gemb1/k10kugel")
    s.welt()
    xm = (-2.4, 0.0, 2.4)
    y = 0.8
    tit = (s.tr("zwei", "1D: zwei Punkte", "1D: two points", "1D: dos puntos", "一维：两点"),
           s.tr("ring", "2D: Kreisring", "2D: circular ring", "2D: anillo", "二维：圆环"),
           s.tr("schale", "3D: Kugelschale", "3D: spherical shell", "3D: capa esférica", "三维：球壳"))
    for x, ti in zip(xm, tit):
        t(s, ti, (x, 1.8))
    # 1D
    s.pfeil((xm[0] - 1.05, y), (xm[0] + 1.05, y), "", farbe=SCHWARZ, spitze=0.14, dicke=2.5)
    for i in range(-5, 6):
        s.punkt(None, xm[0] + i * 0.18, y, farbe=GRAU, r=0.03)
    for sg in (-1, 1):
        s.linie(None, (xm[0] + sg * 0.64, y), (xm[0] + sg * 0.82, y), farbe=ROT, dicke=8)
    t(s, "-k", (xm[0] - 0.73, y - 0.34), farbe=ROT, g=22)
    t(s, "+k", (xm[0] + 0.73, y - 0.34), farbe=ROT, g=22)
    t(s, "k", (xm[0] + 1.02, y + 0.26), g=22)
    # 2D
    r0, r1 = 0.6, 0.76
    s.kreis(None, xm[1], y, r1, farbe=ROT, dicke=2.5, fuellung=ROT, deckung=0.22)
    s.kreis(None, xm[1], y, r0, farbe=ROT, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    for i in range(-5, 6):
        for j in range(-5, 6):
            x_, y_ = i * 0.19, j * 0.19
            if x_ * x_ + y_ * y_ <= 0.8:
                s.punkt(None, xm[1] + x_, y + y_, farbe=SCHWARZ if r0 * r0 <= x_ * x_ + y_ * y_ <= r1 * r1 else HELLGRAU, r=0.022)
    # 3D
    s.kreis(None, xm[2], y, r1, farbe=ROT, dicke=2.5, fuellung=ROT, deckung=0.22)
    s.kreis(None, xm[2], y, r0, farbe=ROT, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    s.weg(None, "%.3f+%.3f*cos(t)" % (xm[2], r0), "%.3f+%.3f*sin(t)" % (y, 0.26 * r0), 0, pi, farbe=GRAU, dicke=1.8, dash=DASH)
    s.weg(None, "%.3f+%.3f*cos(t)" % (xm[2], r0), "%.3f+%.3f*sin(t)" % (y, 0.26 * r0), pi, 2 * pi, farbe=GRAU, dicke=2.2)
    s.linie(None, (xm[2], y), (xm[2] + 0.42, y + 0.42), farbe=SCHWARZ, dicke=2.5)
    t(s, "k", (xm[2] + 0.16, y + 0.32), g=22)
    # Zustandsdichten
    yk = -1.05
    achsen = dict(breite=1.75, hoehe=1.05, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    for j, (x, f, xb, lab) in enumerate(zip(xm, ("0.32/sqrt(x)", "0.7", "0.72*sqrt(x)"), ((0.032, 1.0), (0, 1.0), (0, 1.0)), ("\\propto E^{-1/2}", "\\propto E^{0}", "\\propto E^{1/2}"))):
        a = s.achsen((0, 1), (0, 1.15), mitte=(x + 0.08, yk), xl="E", yl="D(E)", **achsen)
        s.kurve(a, f, x=xb, farbe=BLAU, dicke=5)
        s.text(a, lab, (0.97, 0.98 if j != 2 else 0.2), groesse=GR, ausrichtung="right", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k10kante():
    """Silizium: Täler im k-Raum, Zustandsdichte an den Bandrändern."""
    s = Szene("gemb1/k10kante")
    s.welt()
    cx, cy, r = -1.95, 0.0, 1.3
    s.pfeil((cx - r - 0.1, cy), (cx + r + 0.2, cy), "", farbe=SCHWARZ, spitze=0.14, dicke=2.5)
    s.pfeil((cx, cy - r - 0.1), (cx, cy + r + 0.2), "", farbe=SCHWARZ, spitze=0.14, dicke=2.5)
    t(s, "k_x", (cx + r + 0.2, cy - 0.3), g=GR)
    t(s, "k_y", (cx + 0.33, cy + r + 0.12), g=GR)
    lang, kurz = 0.42, 0.42 / 2.2        # Verhältnis der Halbachsen sqrt(0,92/0,19) = 2,2
    d = 0.85 * r
    for sx, sy, a_, b_ in ((1, 0, lang, kurz), (-1, 0, lang, kurz), (0, 1, kurz, lang), (0, -1, kurz, lang)):
        mx, my = cx + sx * d, cy + sy * d
        ecken = [(mx + a_ * cos(2 * pi * i / 60), my + b_ * sin(2 * pi * i / 60)) for i in range(61)]
        poly(s, None, ecken, BLAU, deckung=0.28, rand=BLAU, dicke=2.5)
    s.kreis(None, cx, cy, kurz, farbe=ORANGE, dicke=2.5, fuellung=ORANGE, deckung=0.2)
    t(s, s.tr("zwei_t", "6 Täler", "6 valleys", "6 valles", "6 个能谷"), (cx - 0.9, cy + 1.05), farbe=BLAU)
    # rechts: D(E)
    emin, emax = -0.45, 1.6
    a = s.achsen((0, 5), (emin, emax), breite=2.4, hoehe=2.35, mitte=(1.65, 0.0), xl=s.tr("d_cm", "D in 10^{21}/(eV cm^3)", "D in 10^{21}/(eV cm^3)", "D en 10^{21}/(eV cm^3)", "D / (10^{21}/(eV cm^3))"),
                 yl=s.tr("e_ev", "E-E_V in eV", "E-E_V in eV", "E-E_V en eV", "E-E_V / eV"), xticks="0;2;4", yticks="0;1")
    s.band(a, 0, 5, 0, EG, farbe=GRAU, deckung=0.16)
    s.linie(a, (0, EG), (5, EG), farbe=GRUEN, dicke=3)
    s.linie(a, (0, 0), (5, 0), farbe=SCHWARZ, dicke=3)
    pc = [(d3(e / 200, MC), EG + e / 200) for e in range(0, 97)]
    pv = [(d3(e / 200, MV), -e / 200) for e in range(0, 91)]
    s.daten(a, pc, farbe=BLAU, dicke=5)
    s.daten(a, pv, farbe=BLAU, dicke=5)
    s.text(a, "E_C", (4.95, EG + 0.13), groesse=GR, ausrichtung="right", farbe=GRUEN)
    s.text(a, "E_V", (4.95, 0.13), groesse=GR, ausrichtung="right", farbe=SCHWARZ)
    s.text(a, "D_C", (2.0, 1.47), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "D_V", (1.75, -0.3), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("luecke", "Lücke", "gap", "brecha", "带隙"), (2.5, 0.56), groesse=GR, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def kasten(s, x, y, n, besetzt, b=0.27, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0):
    for i in range(n):
        poly(s, None, [(x + i * b, y), (x + (i + 1) * b, y), (x + (i + 1) * b, y + b), (x + i * b, y + b)], fuellung, deckung=deckung, rand=farbe, dicke=2)
        if i in besetzt:
            s.kreis(None, x + (i + 0.5) * b, y + 0.5 * b, 0.075, farbe=BLAU, dicke=1, fuellung=BLAU, deckung=1.0)


def k10mikro():
    """Gruppen, Mikrozustände einer Gruppe, Gewicht zweier Gruppen."""
    s = Szene("gemb1/k10mikro")
    s.welt()
    b = 0.27
    x0 = -3.1
    t(s, s.tr("gruppen", "Gruppen", "groups", "grupos", "能量组"), (-2.55, 1.55))
    for j, (e, g) in enumerate((("E_1", 5), ("E_2", 4), ("E_3", 3), ("E_4", 2))):
        y = -0.8 + j * 0.58
        hell = g == 4
        t(s, e, (x0 - 0.1, y + 0.13), a="right", g=GR)
        kasten(s, x0, y, g, (), farbe=ROT if hell else SCHWARZ, fuellung=HELLROT if hell else "#ffffff")
        t(s, "g=%d" % g, (x0 + g * b + 0.12, y + 0.13), a="left", g=22, farbe=ROT if hell else SCHWARZ)
    s.pfeil((-1.3, -0.1 + 0.1), (-0.9, -0.1 + 0.1), "", farbe=ROT, spitze=0.14, dicke=2.5)
    t(s, s.tr("sechs", "6 Mikrozustände", "6 microstates", "6 microestados", "6 个微观状态"), (-0.15, 1.55), farbe=ROT)
    paare = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
    for j, p in enumerate(paare):
        kasten(s, -0.7, 1.0 - j * 0.38, 4, p, farbe=SCHWARZ)
    a = s.achsen((-0.6, 4.6), (0, 40), breite=1.75, hoehe=2.0, mitte=(2.55, -0.1), xl="N_1", yl="W", xticks="0;1;2;3;4", yticks="0;16;36")
    s.stems(a, [0, 1, 2, 3, 4], [1, 16, 36, 16, 1], farbe=BLAU, breite=0.62, marker="none")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def zaehle(m, ne, eges, fest=None):
    c = {(0, 0): 1}
    for j in range(m):
        neu = defaultdict(int)
        for (n, e), v in c.items():
            if j != fest:
                neu[(n, e)] += v
            if n + 1 <= ne and e + j <= eges:
                neu[(n + 1, e + j)] += v
        c = neu
    return c.get((ne, eges), 0)


def k10abzaehlen():
    """Exakt ausgezählte Besetzung gegen die Fermi-Verteilung (Zahlen wie rechnung_kap10.py)."""
    s = Szene("gemb1/k10abzaehlen")
    m, ne, q = 40, 20, 30
    eges = ne * (ne - 1) // 2 + q
    ges = zaehle(m, ne, eges)
    pj = [zaehle(m, ne, eges, fest=j) / ges for j in range(m)]
    ef, kt = 19.5, 4.433
    a = s.achsen((0, 40), (0, 1.05), breite=5.6, hoehe=1.8, mitte=(0.2, 0), xl=s.tr("e_eps", "E in \\Delta E", "E in \\Delta E", "E en \\Delta E", "E / \\Delta E"),
                 yl=s.tr("bes", "Besetzung", "occupation", "ocupación", "占据"), xticks="0;10;20;30;40", yticks="0;0.5;1")
    s.linie(a, (ef, 0), (ef, 1.05), farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(a, "1/(1+exp((x-%g)/%g))" % (ef, kt), x=(0, 39.5), farbe=BLAU, dicke=4)
    for j, p in enumerate(pj):
        s.punkt(a, j, p, farbe=ROT, r=0.05)
    s.text(a, "E_F", (ef + 1.0, 0.95), groesse=GR, ausrichtung="left", farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k10fermi():
    """Fermi-Verteilung für drei Temperaturen und logarithmisch mit dem Boltzmann-Faktor."""
    s = Szene("gemb1/k10fermi")
    ex = 0.5
    a = s.achsen((-ex, ex), (0, 1.1), breite=2.75, hoehe=2.1, mitte=(-2.0, 0.1), xl=s.tr("emef", "E-E_F in eV", "E-E_F in eV", "E-E_F en eV", "E-E_F / eV"), yl="f",
                 xticks="-0.4;0;0.4", yticks="0;0.5;1")
    s.linie(a, (0, 0), (0, 1.1), farbe=GRAU, dicke=1.8, dash=DASH)
    s.daten(a, [(-ex, 1), (0, 1), (0, 0), (ex, 0)], farbe=SCHWARZ, dicke=3)
    k3, k10 = KB * 300, KB * 1000
    s.kurve(a, "1/(1+exp(x/%.6f))" % k3, farbe=BLAU, dicke=4)
    s.kurve(a, "1/(1+exp(x/%.6f))" % k10, farbe=ROT, dicke=4)
    s.linie(a, (-2 * k10, 1), (2 * k10, 0), farbe=ROT, dicke=2.5, dash=DASH)
    s.punkt(a, 0, 0.5, farbe=SCHWARZ, r=0.06)
    s.text(a, "0 K", (0.04, 0.98), groesse=22, ausrichtung="left")
    s.text(a, "300 K", (0.08, 0.34), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "1000 K", (0.2, 0.17), groesse=22, ausrichtung="left", farbe=ROT)
    b = s.achsen((0, 8), (1e-4, 1), breite=2.35, hoehe=2.1, mitte=(1.8, 0.1), xl=s.tr("x_kt", "(E-E_F)/(k_BT)", "(E-E_F)/(k_BT)", "(E-E_F)/(k_BT)", "(E-E_F)/(k_BT)"), yl="f", ylog=True,
                 xticks="0;2;4;6;8", gitter=True)
    s.kurve(b, "exp(-x)", x=(0.05, 8), farbe=ROT, dicke=3, dash=DASH)
    s.kurve(b, "1/(1+exp(x))", x=(0, 8), farbe=BLAU, dicke=4)
    s.text(b, "f", (0.7, 0.13), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b, "\\mathrm{e}^{-u}", (2.4, 0.3), groesse=GR, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k10dichte():
    """Silizium: D(E), f und 1-f, Produkt am Rand."""
    s = Szene("gemb1/k10dichte")
    ey = (-0.4, 1.52)
    ef = EG / 2
    gem = dict(breite=1.4, hoehe=2.15)
    a = s.achsen((0, 5), ey, mitte=(-2.6, 0.1), xl="D", yl=s.tr("e_ev", "E-E_V in eV", "E-E_V in eV", "E-E_V en eV", "E-E_V / eV"), xzahlen=False, xmarks=False, yticks="0;0.56;1.12", **gem)
    s.band(a, 0, 5, 0, EG, farbe=GRAU, deckung=0.16)
    s.linie(a, (0, ef), (5, ef), farbe=ORANGE, dicke=2.5, dash=DASH)
    s.daten(a, [(d3(e / 200, MC), EG + e / 200) for e in range(0, 81)], farbe=BLAU, dicke=5)
    s.daten(a, [(d3(e / 200, MV), -e / 200) for e in range(0, 81)], farbe=BLAU, dicke=5)
    s.text(a, "E_F", (4.8, ef + 0.13), groesse=22, ausrichtung="right", farbe=ORANGE)
    b = s.achsen((0, 1), ey, mitte=(-0.8, 0.1), xl="", yl="", xticks="0;1", yzahlen=False, ymarks=False, **gem)
    s.band(b, 0, 1, 0, EG, farbe=GRAU, deckung=0.16)
    s.linie(b, (0, ef), (1, ef), farbe=ORANGE, dicke=2.5, dash=DASH)
    pf = [(1 / (1 + exp((e / 200 - 0.4 - ef) / KT)), e / 200 - 0.4) for e in range(0, 385)]
    s.daten(b, pf, farbe=ROT, dicke=4)
    s.daten(b, [(1 - x_, y_) for x_, y_ in pf], farbe=GRUEN, dicke=4)
    s.text(b, "f", (0.84, -0.22), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b, "1-f", (0.78, 1.36), groesse=GR, ausrichtung="center", farbe=GRUEN)
    c = s.achsen((0, 6), (0, 1.1), breite=2.05, hoehe=2.15, mitte=(1.95, 0.1), xl=s.tr("u_kt", "(E-E_C)/(k_BT)", "(E-E_C)/(k_BT)", "(E-E_C)/(k_BT)", "(E-E_C)/(k_BT)"),
                 yl="D_C f", xticks="0;2;4;6", yzahlen=False, ymarks=False)
    norm = "(sqrt(x)*exp(-x)/%.6f)" % (sqrt(0.5) * exp(-0.5))
    s.flaeche(c, norm, 0, 6, farbe=GRUEN, deckung=0.25)
    s.kurve(c, norm, x=(0, 6), farbe=GRUEN, dicke=4)
    s.linie(c, (0.5, 0), (0.5, 1.0), farbe=GRAU, dicke=2, dash=DASH)
    s.text(c, "n", (2.0, 0.9), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k10metall():
    """Potentialtopf, Fermi-Kugel, besetzte Plätze."""
    s = Szene("gemb1/k10metall")
    s.welt()
    xm = -2.45
    t(s, s.tr("topf", "Potentialtopf", "potential well", "pozo de potencial", "势阱"), (xm, 1.6))
    br, y0 = 1.8, -0.85
    # Rümpfe grau, Topf blau
    pts = []
    for i in range(0, 241):
        x = i / 240
        u = 0.0
        for j in range(5):
            u += -0.11 / (abs(x - (0.1 + j * 0.2)) + 0.04)
        pts.append((xm - br / 2 + br * x, 0.75 + u * 0.3))
    s.daten(s.objects[0]["id"], pts, farbe=GRAU, dicke=3)
    s.linie(None, (xm - br / 2, 1.3), (xm - br / 2, y0), farbe=BLAU, dicke=4)
    s.linie(None, (xm - br / 2, y0), (xm + br / 2, y0), farbe=BLAU, dicke=4)
    s.linie(None, (xm + br / 2, y0), (xm + br / 2, 1.3), farbe=BLAU, dicke=4)
    s.linie(None, (xm - br / 2, y0 + 1.4), (xm + br / 2, y0 + 1.4), farbe=ROT, dicke=3, dash=DASH)
    t(s, "E_{F0}", (xm, y0 + 1.65), farbe=ROT, g=22)
    t(s, "L", (xm, y0 - 0.3), farbe=BLAU, g=22)
    # Fermi-Kugel
    cx, cy = 0.05, 0.1
    r = 0.9
    t(s, s.tr("kugel", "Fermi-Kugel", "Fermi sphere", "esfera de Fermi", "费米球"), (cx, 1.6))
    s.kreis(None, cx, cy, r + 0.1, farbe=BLAU, dicke=1.5, fuellung=BLAU, deckung=0.08, dash=DASH)
    s.kreis(None, cx, cy, r, farbe=BLAU, dicke=3, fuellung=BLAU, deckung=0.25)
    s.pfeil((cx - r - 0.32, cy), (cx + r + 0.32, cy), "", farbe=SCHWARZ, spitze=0.13, dicke=2)
    s.pfeil((cx, cy - r - 0.3), (cx, cy + r + 0.32), "", farbe=SCHWARZ, spitze=0.13, dicke=2)
    s.pfeil((cx, cy), (cx + r * 0.71, cy + r * 0.71), "", farbe=ROT, spitze=0.14, dicke=3)
    t(s, "k_F", (cx + 0.28, cy + 0.64), farbe=ROT, g=GR)
    t(s, "k_x", (cx + r + 0.2, cy - 0.28), g=22)
    t(s, "k_y", (cx + 0.3, cy + r + 0.22), g=22)
    # Besetzte Plätze: Maßstab übertrieben
    b_ = 0.06
    a = s.achsen((0, 1.4), (0, 1.3), breite=1.65, hoehe=1.9, mitte=(2.45, 0.05), xl="E", yl="D", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.flaeche(a, "sqrt(x)/(1+exp((x-1)/%g))" % b_, 0, 1.4, farbe=BLAU, deckung=0.3)
    s.kurve(a, "sqrt(x)", x=(0, 1.4), farbe=SCHWARZ, dicke=3)
    s.kurve(a, "sqrt(x)/(1+exp((x-1)/%g))" % b_, x=(0, 1.4), farbe=BLAU, dicke=3)
    s.linie(a, (1, 0), (1, 1.15), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(a, "E_{F0}", (1, 1.2), groesse=22, ausrichtung="center", farbe=ROT)
    s.speichern()


if __name__ == "__main__":
    k10band()
    k10kugel()
    k10kante()
    k10mikro()
    k10abzaehlen()
    k10fermi()
    k10dichte()
    k10metall()
