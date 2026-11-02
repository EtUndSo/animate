"""GEMB 1 Teil 9 (kap9_stufen.tex): Bandstrukturen lesen.

Aufruf: python tools/szenen/gemb1_teil9.py, danach python tools/szenen_ansehen.py out.png gemb1/k9quadrat ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap9.py.
Die Bandskizzen von Silizium und GaAs (k9silizium, k9gaas) sind qualitativ: nur Lage der Extrema und Reihenfolge der Bänder
stimmen, die Kurven sind einfache Funktionen, keine gerechneten Daten. Deshalb tragen ihre Achsen keine Zahlen.
"""
import sys
from math import acos, atan2, cos, pi, sin, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#ddf0e4"
Es, Vss, A0 = -5.0, 0.5, 0.25       # Quadratgitter und Kette
V_PI, A_G = 2.8, 0.246              # Graphen
MH, ML, MGA = 0.92, 0.19, 0.067     # Massen in m0
C0 = 0.038100                       # hbar^2/(2 m0) in eV nm^2


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def poly(s, on, ecken, farbe, deckung=0.2, rand=None, dicke=2):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": rand or farbe, "fill_color": farbe,
                              "fill_opacity": deckung, "stroke_width": dicke}, on)


def achse(s, name, einheit):
    return s.tr("a_" + name + einheit, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


# ------------------------------------------------------------------------------------------ Stufe 1
def kontur(c, n=161):
    """Geschlossene Linie cos x + cos y = c um den Ursprung, x, y in Einheiten pi."""
    xm = acos(c - 1)
    xs = xm * np.sin(np.linspace(-pi / 2, pi / 2, n))
    ob = [(float(x) / pi, acos(max(min(c - cos(x), 1.0), -1.0)) / pi) for x in xs]
    return ob + [(x, -y) for x, y in reversed(ob)]


def k9quadrat():
    """Zone des Quadratgitters mit Weg und Linien konstanter Energie, rechts E längs des Wegs."""
    s = Szene("gemb1/k9quadrat")
    a = s.achsen((-1.15, 1.15), (-1.15, 1.15), breite=2.75, hoehe=2.75, mitte=(-2.15, 0), kreuz=True, xl="k_x", yl="k_y", xzahlen=False, yzahlen=False, xticks="-1;1", yticks="-1;1")
    poly(s, a, [(-1, -1), (1, -1), (1, 1), (-1, 1)], GRAU, deckung=0.1, rand=SCHWARZ, dicke=2.5)
    for c in (1.5, 0.75, 0.0):
        s.daten(a, kontur(c), farbe=BLAU, dicke=2.8)
    s.text(a, "-6.5", (-0.56, 0.22), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "-5", (-0.72, 0.72), groesse=22, ausrichtung="center", farbe=BLAU)
    s.pfeil((0, 0), (1, 0), "", farbe=GRUEN, dicke=4, spitze=0.14, on=a)
    s.pfeil((1, 0), (1, 1), "", farbe=ROT, dicke=4, spitze=0.14, on=a)
    s.pfeil((1, 1), (0, 0), "", farbe=ORANGE, dicke=4, spitze=0.14, on=a)
    s.text(a, "\\Gamma", (-0.14, -0.15), groesse=24, ausrichtung="center")
    s.text(a, "X", (1.12, -0.15), groesse=24, ausrichtung="center")
    s.text(a, "M", (1.12, 1.1), groesse=24, ausrichtung="center")
    s.text(a, "\\pi/a", (1.0, -1.17), groesse=22, ausrichtung="center")
    L = 2 + sqrt(2)
    b = s.achsen((0, L), (-7.4, -2.6), breite=2.8, hoehe=2.4, mitte=(1.95, 0.05), xl="", yl=achse(s, "E", "eV"), xzahlen=False, xticks="0;1;2;%.3f" % L, yticks="-7;-5;-3")
    X = np.linspace(0, 1, 41)
    s.daten(b, [(x, -6 - cos(pi * x)) for x in X], farbe=GRUEN, dicke=4.5)
    s.daten(b, [(1 + x, -4 - cos(pi * x)) for x in X], farbe=ROT, dicke=4.5)
    s.daten(b, [(2 + sqrt(2) * x, -5 + 2 * cos(pi * x)) for x in X], farbe=ORANGE, dicke=4.5)
    for x, n in ((0, "\\Gamma"), (1, "X"), (2, "M"), (L, "\\Gamma")):
        s.linie(b, (x, -7.4), (x, -2.6), farbe=GRAU, dicke=1.5)
        s.text(b, n, (x, -7.75), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def fg(kx, ky):
    th, cc = sqrt(3) / 2 * kx * A_G, cos(ky * A_G / 2)
    return sqrt(max(1 + 4 * cos(th) * cc + 4 * cc * cc, 0.0))


def k9graphen():
    """Wabe mit primitiver Zelle und Gittervektoren, Zone mit Weg, Bänder längs Gamma-M-K-Gamma."""
    s = Szene("gemb1/k9graphen")
    w = s.welt()
    # Wabe: ac in Szeneneinheiten
    ac = 0.45
    aa = sqrt(3) * ac
    o = (-3.75, 1.72)
    v1 = (aa * sqrt(3) / 2, aa / 2)
    v2 = (aa * sqrt(3) / 2, -aa / 2)
    # primitive Zellen: um das Atom A herum, Mitte der Raute liegt auf der Bindung
    def zelle(i, j, f, d, r=None, dk=1.5):
        c = (o[0] + i * v1[0] + j * v2[0], o[1] + i * v1[1] + j * v2[1])
        ecke = (c[0] - (v1[0] + v2[0]) / 2 + ac / 2, c[1] - (v1[1] + v2[1]) / 2)
        poly(s, w, [ecke, (ecke[0] + v1[0], ecke[1] + v1[1]), (ecke[0] + v1[0] + v2[0], ecke[1] + v1[1] + v2[1]), (ecke[0] + v2[0], ecke[1] + v2[1])], f, deckung=d, rand=r or GRAU, dicke=dk)
    for (i, j) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        zelle(1 + i, 1 + j, GRAU, 0.14)
    zelle(1, 1, GRAU, 0.42, r=SCHWARZ, dk=2.5)
    atome = []
    for i in range(-3, 7):
        for j in range(-3, 7):
            ax_ = o[0] + i * v1[0] + j * v2[0]
            ay_ = o[1] + i * v1[1] + j * v2[1]
            atome.append((ax_, ay_, BLAU))
            atome.append((ax_ + ac, ay_, GRUEN))
    box = (-3.62, -0.72, 0.72, 2.72)
    drin = lambda p: box[0] <= p[0] <= box[1] and box[2] <= p[1] <= box[3]
    A = [p for p in atome if p[2] == BLAU]
    B = [p for p in atome if p[2] == GRUEN]
    for p in A:
        for d in ((ac, 0), (-ac / 2, aa / 2), (-ac / 2, -aa / 2)):
            q = (p[0] + d[0], p[1] + d[1])
            if drin(p) and drin(q):
                s.linie(w, p[:2], q, farbe=SCHWARZ, dicke=2.2)
    for p in atome:
        if drin(p):
            s.punkt(w, p[0], p[1], farbe=p[2], r=0.075)
    ca = (o[0] + v1[0] + v2[0], o[1] + v1[1] + v2[1])
    s.pfeil(ca, (ca[0] + v1[0], ca[1] + v1[1]), "", farbe=ROT, dicke=3.5, spitze=0.16)
    s.pfeil(ca, (ca[0] + v2[0], ca[1] + v2[1]), "", farbe=ROT, dicke=3.5, spitze=0.16)
    t(s, "a_1", (ca[0] + v1[0] + 0.0, ca[1] + v1[1] + 0.23), farbe=ROT)
    t(s, "a_2", (ca[0] + v2[0] + 0.05, ca[1] + v2[1] - 0.23), farbe=ROT)
    t(s, "A", (ca[0] - 0.24, ca[1] + 0.02), farbe=BLAU)
    t(s, "B", (ca[0] + ac + 0.2, ca[1] + 0.0), farbe=GRUEN)
    # Zone
    km = 2 * pi / (sqrt(3) * A_G)
    kk = 2 * pi / (3 * A_G)
    z = s.achsen((-21, 21), (-21, 21), breite=2.0, hoehe=2.0, mitte=(1.45, 1.72), kreuz=True, xl="k_x", yl="k_y", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    hexa = [(kk * 2 * 0 + 0, 2 * kk), (km, kk), (km, -kk), (0, -2 * kk), (-km, -kk), (-km, kk)]
    poly(s, z, hexa, GRAU, deckung=0.12, rand=SCHWARZ, dicke=2.5)
    s.pfeil((0, 0), (km, 0), "", farbe=ORANGE, dicke=3.5, spitze=0.14, on=z)
    s.pfeil((km, 0), (km, kk), "", farbe=ORANGE, dicke=3.5, spitze=0.14, on=z)
    s.pfeil((km, kk), (0, 0), "", farbe=ORANGE, dicke=3.5, spitze=0.14, on=z)
    for i, p in enumerate(hexa):
        s.punkt(z, p[0], p[1], farbe=ROT, r=0.085)
    s.text(z, "\\Gamma", (-2.6, -3.0), groesse=24, ausrichtung="center")
    s.text(z, "M", (17.8, 2.4), groesse=24, ausrichtung="center")
    s.text(z, "K", (17.2, 11.5), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(z, "K'", (3.6, 19.3), groesse=24, ausrichtung="center", farbe=ROT)
    # Bänder
    lg, lm, lk = km, kk, 2 * kk * 1.0
    L = km + kk + 2 * kk
    b = s.achsen((0, L), (-9.5, 9.5), breite=5.6, hoehe=1.3, mitte=(0.2, -0.75), xl="", yl=s.tr("e_ep", "E - E_p in eV", "E - E_p in eV", "E - E_p en eV", "E - E_p / eV"), xzahlen=False, xticks="0;%.3f;%.3f;%.3f" % (km, km + kk, L), yticks="-8;-4;0;4;8")
    pts = []
    n = 90
    for i in range(n + 1):
        u = i / n
        pts.append((u * km, fg(u * km, 0.0)))
    for i in range(n + 1):
        u = i / n
        pts.append((km + u * kk, fg(km, u * kk)))
    for i in range(n + 1):
        u = i / n
        pts.append((km + kk + u * 2 * kk, fg(km * (1 - u), kk * (1 - u))))
    s.daten(b, [(x, V_PI * f) for x, f in pts], farbe=ROT, dicke=4.5)
    s.daten(b, [(x, -V_PI * f) for x, f in pts], farbe=BLAU, dicke=4.5)
    s.linie(b, (0, 0), (L, 0), farbe=GRAU, dicke=1.5, dash=DASH)
    for x, nm in ((0, "\\Gamma"), (km, "M"), (km + kk, "K"), (L, "\\Gamma")):
        s.linie(b, (x, -9.5), (x, 9.5), farbe=GRAU, dicke=1.5)
        s.text(b, nm, (x, -13.2), groesse=24, ausrichtung="center")
    s.text(b, "\\pi^*", (kk * 0.8, 3.9), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(b, "\\pi", (kk * 0.8, -3.9), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(b, s.tr("dirac", "Dirac-Punkt", "Dirac point", "punto de Dirac", "狄拉克点"), (km + kk + 2.0, 6.2), groesse=22, ausrichtung="left", farbe=SCHWARZ)
    s.pfeil((km + kk + 3.0, 5.0), (km + kk + 0.25, 0.7), "", farbe=SCHWARZ, dicke=2, spitze=0.12, on=b)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def lb_si(x, x0=0.85):
    """Unterstes Leitungsband längs Gamma-X in der Skizze: waagerecht bei Gamma, Minimum bei x0."""
    return 1.0 + 1.1 * (1 + cos(pi * x / x0)) if x <= x0 else 1.0 + 1.1 * (1 - cos(pi * (x - x0) / x0))


def k9silizium():
    """Qualitative Skizze der Silizium-Bänder längs L-Gamma-X, rechts Schnitt durch die Zone mit den Tälern."""
    s = Szene("gemb1/k9silizium")
    a = s.achsen((-1, 1), (-5.4, 4.2), breite=2.65, hoehe=2.55, mitte=(-2.2, 0.1), xl="", yl="E", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.band(a, -1, 1, 0, 1, farbe=GRAU, deckung=0.22)
    # Valenzbänder: flach, steil, tief
    X = np.linspace(0, 1, 41)
    k1 = lambda x: 1 - cos(pi * x)
    s.daten(a, [(x, -0.5 * k1(x)) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(a, [(-x, -0.2 * k1(x)) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(a, [(x, -1.55 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    s.daten(a, [(-x, -1.25 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    s.daten(a, [(x, -4.9 + 0.9 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    s.daten(a, [(-x, -4.9 + 0.5 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    # Leitungsbänder
    x0 = 0.85
    s.daten(a, [(x, lb_si(x)) for x in X], farbe=ROT, dicke=4.5)
    s.daten(a, [(-x, 3.2 - 0.75 * k1(x)) for x in X], farbe=ROT, dicke=3)
    s.daten(a, [(x, 3.2 + 0.28 * k1(x)) for x in X], farbe=ROT, dicke=3)
    s.daten(a, [(-x, 3.2 + 0.2 * k1(x)) for x in X], farbe=ROT, dicke=3)
    s.linie(a, (0, -5.4), (0, 4.2), farbe=GRAU, dicke=1.5)
    s.punkt(a, 0, 0, farbe=SCHWARZ, r=0.075)
    s.punkt(a, x0, 1.0, farbe=SCHWARZ, r=0.075)
    s.text(a, "E_V", (-0.27, 0.42), groesse=24, ausrichtung="center")
    s.text(a, "E_C", (0.64, 0.5), groesse=24, ausrichtung="center")
    s.pfeil((0.965, 0.0), (0.965, 1.0), "", farbe=SCHWARZ, dicke=2, spitze=0.1, doppelt=True, on=a)
    s.text(a, "E_g", (1.12, 0.5), groesse=24, ausrichtung="left")
    for x, n in ((-1, "L"), (0, "\\Gamma"), (1, "X")):
        s.text(a, n, (x, -6.05), groesse=24, ausrichtung="center")
    s.text(a, s.tr("skizze", "qualitative Skizze", "qualitative sketch", "esbozo cualitativo", "定性示意图"), (0, 4.65), groesse=24, ausrichtung="center", farbe=ROT)
    # Zone, Schnitt k_z = 0, Einheiten 2 pi / a
    b = s.achsen((-1.25, 1.25), (-1.25, 1.25), breite=2.5, hoehe=2.5, mitte=(1.35, 0.05), kreuz=True, xl="k_x", yl="k_y", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    okt = [(1, 0.5), (0.5, 1), (-0.5, 1), (-1, 0.5), (-1, -0.5), (-0.5, -1), (0.5, -1), (1, -0.5)]
    poly(s, b, okt, GRAU, deckung=0.1, rand=SCHWARZ, dicke=2.5)
    la, lb = 0.145, 0.145 / 2.2
    for (cx, cy, ax_, ay_) in ((0.85, 0, la, lb), (-0.85, 0, la, lb), (0, 0.85, lb, la), (0, -0.85, lb, la)):
        poly(s, b, [(cx + ax_ * cos(u), cy + ay_ * sin(u)) for u in np.linspace(0, 2 * pi, 40)], ROT, deckung=0.25, rand=ROT, dicke=2.5)
    s.weg(b, "%.4f*cos(t)" % lb, "%.4f*sin(t)" % lb, 0, 6.2832, farbe=ROT, dicke=2.5, dash=DASH)
    s.text(b, "\\Gamma", (-0.14, -0.14), groesse=24, ausrichtung="center")
    s.punkt(b, 1, 0, farbe=SCHWARZ, r=0.07)
    s.text(b, "X", (1.1, 0.15), groesse=24, ausrichtung="center")
    s.pfeil((0.3, 0.42), (0.03, 0.09), "", farbe=SCHWARZ, dicke=2, spitze=0.11, on=b)
    s.text(b, "\\pm k_z", (0.31, 0.53), groesse=22, ausrichtung="left", farbe=SCHWARZ)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k9gaas():
    """Qualitative Skizzen: GaAs mit direktem Übergang, Silizium mit Photon und Phonon."""
    s = Szene("gemb1/k9gaas")
    k1 = lambda x: 1 - cos(pi * x)
    X = np.linspace(0, 1, 61)
    # links GaAs
    a = s.achsen((-1, 1), (-2.2, 3.3), breite=3.0, hoehe=2.1, mitte=(-1.95, 0), xl="", yl="E", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, titel="GaAs", titel_mitte=True)
    s.band(a, -1, 1, 0, 1.2, farbe=GRAU, deckung=0.2)
    s.daten(a, [(x, -0.75 * k1(x)) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(a, [(-x, -0.45 * k1(x)) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(a, [(x, -1.6 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    s.daten(a, [(-x, -1.3 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    # Leitungsband: Mulde bei Gamma, Nebentäler bei L und X
    fl = lambda x: 1.2 + 0.95 * (1 - np.exp(-(x / 0.16)**2)) + 0.75 * (x**2) - 0.25 * x**6
    ff = lambda x: 1.2 + 1.45 * (1 - np.exp(-(x / 0.16)**2)) + 0.55 * (1 - x**2) * 1.0 - 0.55 * np.exp(-(x / 0.16)**2)
    GL = 1.2 + 0.5
    GX = 1.2 + 0.85
    def cb(x, E1):
        # Mulde bei 0 (eng), Scheitel in der Mitte, Tal am Rand bei x = 1 mit Energie E1
        return 1.2 + (E1 + 0.9 - 1.2) * (1 - np.exp(-(x / 0.2)**2)) + 0.0 * x - 0.9 * np.exp(-((x - 1) / 0.42)**2)
    s.daten(a, [(x, cb(x, GX)) for x in X], farbe=ROT, dicke=4.5)
    s.daten(a, [(-x, cb(x, GL)) for x in X], farbe=ROT, dicke=4.5)
    s.linie(a, (0, -2.2), (0, 3.3), farbe=GRAU, dicke=1.5)
    s.pfeil((0, 0), (0, 1.2), "", farbe=ORANGE, dicke=4, spitze=0.14, on=a)
    s.text(a, s.tr("photon", "Photon", "photon", "fotón", "光子"), (0.1, 0.42), groesse=24, ausrichtung="left", farbe=ORANGE)
    for x, n in ((-1, "L"), (0, "\\Gamma"), (1, "X")):
        s.text(a, n, (x, -3.05), groesse=24, ausrichtung="center")
    # rechts Silizium
    b = s.achsen((-1, 1), (-2.2, 3.3), breite=3.0, hoehe=2.1, mitte=(1.95, 0), xl="", yl="E", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, titel="Si", titel_mitte=True)
    s.band(b, -1, 1, 0, 1.0, farbe=GRAU, deckung=0.2)
    s.daten(b, [(x, -0.5 * k1(x)) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(b, [(-x, -0.2 * k1(x)) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(b, [(x, -1.55 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    s.daten(b, [(-x, -1.25 * k1(x)) for x in X], farbe=BLAU, dicke=3)
    x0 = 0.85
    s.daten(b, [(x, lb_si(x)) for x in X], farbe=ROT, dicke=4.5)
    s.daten(b, [(-x, 3.2 - 0.75 * k1(x)) for x in X], farbe=ROT, dicke=4.5)
    s.linie(b, (0, -2.2), (0, 3.3), farbe=GRAU, dicke=1.5)
    s.pfeil((0, 0), (0, 0.94), "", farbe=ORANGE, dicke=4, spitze=0.14, on=b)
    s.pfeil((0.03, 1.0), (x0, 1.0), "", farbe=GRUEN, dicke=4, spitze=0.14, on=b)
    s.text(b, s.tr("photon2", "Photon", "photon", "fotón", "光子"), (-0.08, 0.42), groesse=24, ausrichtung="right", farbe=ORANGE)
    s.text(b, s.tr("phonon", "Phonon", "phonon", "fonón", "声子"), (0.42, 0.45), groesse=24, ausrichtung="center", farbe=GRUEN)
    for x, n in ((-1, "L"), (0, "\\Gamma"), (1, "X")):
        s.text(b, n, (x, -3.05), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k9masse():
    """Energie, Geschwindigkeit und effektive Masse über der Zone für das Kosinus-Band."""
    s = Szene("gemb1/k9masse")
    ks = s.tr("k_pa", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)")
    w = 5.8
    xc = 0.35
    a = s.achsen((-1, 1), (-6.25, -3.75), breite=w, hoehe=0.68, mitte=(xc, 1.26), yl=achse(s, "E", "eV"), xzahlen=False, xticks="-1;-0.5;0;0.5;1", yticks="-6;-5;-4")
    s.kurve(a, "-5-cos(pi*x)", farbe=BLAU, dicke=4.5)
    s.kurve(a, "-6+0.5*(pi*x)^2", x=(-0.62, 0.62), farbe=GRUEN, dicke=2.8, dash=DASH)
    s.kurve(a, "-4-0.5*(pi*(x-1))^2", x=(0.38, 1), farbe=GRUEN, dicke=2.8, dash=DASH)
    s.kurve(a, "-4-0.5*(pi*(x+1))^2", x=(-1, -0.38), farbe=GRUEN, dicke=2.8, dash=DASH)
    b = s.achsen((-1, 1), (-4.4, 4.4), breite=w, hoehe=0.68, mitte=(xc, 0.0), yl=s.tr("v_e5", "v in 10^5 m/s", "v in 10^5 m/s", "v en 10^5 m/s", "v / (10^5 m/s)"), xzahlen=False, xticks="-1;-0.5;0;0.5;1", yticks="-3.8;0;3.8")
    s.kurve(b, "3.8*sin(pi*x)", farbe=ROT, dicke=4.5)
    s.linie(b, (-1, 0), (1, 0), farbe=GRAU, dicke=1.5)
    c = s.achsen((-1, 1), (-6, 6), breite=w, hoehe=0.68, mitte=(xc, -1.26), xl=ks, yl="m^*/m_0", xticks="-1;-0.5;0;0.5;1", yticks="-5;0;5")
    s.band(c, -1, -0.5, -6, 6, farbe=ROT, deckung=0.08)
    s.band(c, 0.5, 1, -6, 6, farbe=ROT, deckung=0.08)
    x1 = 0.4349
    x2 = 1 - x1
    s.kurve(c, "1.219/cos(pi*x)", x=(-x1, x1), farbe=BLAU, dicke=4.5)
    s.kurve(c, "1.219/cos(pi*x)", x=(x2, 1), farbe=BLAU, dicke=4.5)
    s.kurve(c, "1.219/cos(pi*x)", x=(-1, -x2), farbe=BLAU, dicke=4.5)
    s.linie(c, (-1, 0), (1, 0), farbe=GRAU, dicke=1.5)
    for q in (-0.5, 0.5):
        s.linie(c, (q, -6), (q, 6), farbe=GRAU, dicke=2, dash=DASH)
    s.text(c, "1.22", (0, 2.9), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(c, "-1.22", (0.82, -3.6), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(c, "-1.22", (-0.82, -3.6), groesse=22, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k9ellipse():
    """Links Schnitt durch die Flächen konstanter Energie, rechts die Parabeln längs und quer."""
    s = Szene("gemb1/k9ellipse")
    a = s.achsen((-1, 1), (-1, 1), breite=2.3, hoehe=2.3, mitte=(-2.15, 0), kreuz=True, xl="q_x", yl="q_y", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    kh, kl, kg = 0.792, 0.360, 0.214
    poly(s, a, [(kh * cos(u), kl * sin(u)) for u in np.linspace(0, 2 * pi, 80)], BLAU, deckung=0.18, rand=BLAU, dicke=3)
    poly(s, a, [(kg * cos(u), kg * sin(u)) for u in np.linspace(0, 2 * pi, 60)], GRUEN, deckung=0.3, rand=GRUEN, dicke=3)
    s.text(a, "Si", (0.5, 0.46), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "GaAs", (-0.54, 0.46), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.pfeil((-0.42, 0.36), (-0.1, 0.13), "", farbe=GRUEN, dicke=2, spitze=0.1, on=a)
    s.text(a, "0.79", (0.84, -0.17), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "0.36", (0.19, -0.5), groesse=22, ausrichtung="center", farbe=BLAU)
    b = s.achsen((-1, 1), (0, 60), breite=2.75, hoehe=1.85, mitte=(1.95, 0.05), xl=s.tr("q_nm", "q in 1/nm", "q in 1/nm", "q en 1/nm", "q / (1/nm)"), yl=s.tr("de", "E - E_C in meV", "E - E_C in meV", "E - E_C en meV", "E - E_C / meV"), xticks="-1;0;1", yticks="0;26;50")
    f = 1000 * C0
    s.kurve(b, "%.4f*x^2" % (f / MH), farbe=BLAU, dicke=4.5)
    s.kurve(b, "%.4f*x^2" % (f / ML), x=(-0.535, 0.535), farbe=ROT, dicke=4.5)
    s.kurve(b, "%.4f*x^2" % (f / MGA), x=(-0.283, 0.283), farbe=GRUEN, dicke=4.5)
    s.linie(b, (-1, 26), (1, 26), farbe=GRAU, dicke=2, dash=DASH)
    s.text(b, "m_h^*", (0.8, 37), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(b, "m_l^*", (0.68, 56), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(b, "GaAs", (0, 54), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k9loch():
    """Oben volles Band und Band mit einem fehlenden Elektron, unten die wandernde Lücke in der Ortsdarstellung."""
    s = Szene("gemb1/k9loch")
    w = s.welt()
    ks = s.tr("k_pa2", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)")
    N = 15
    ka = [(-1 + (2 * i + 1) / N) for i in range(N)]
    a = s.achsen((-1, 1), (-2.3, 0.45), breite=2.8, hoehe=1.1, mitte=(-1.95, 1.05), xl=ks, yl="E - E_V", xticks="-1;0;1", yzahlen=False, ymarks=False, titel=s.tr("voll", "volles Band", "full band", "banda llena", "满带"))
    s.kurve(a, "-(1-cos(pi*x))", farbe=GRAU, dicke=3)
    for q in ka:
        s.punkt(a, q, -(1 - cos(pi * q)), farbe=BLAU, r=0.075)
    b = s.achsen((-1, 1), (-2.3, 0.45), breite=2.8, hoehe=1.1, mitte=(1.65, 1.05), xl=ks, yl="E - E_V", xticks="-1;0;1", yzahlen=False, ymarks=False, titel=s.tr("eines", "ein Elektron fehlt", "one electron missing", "falta un electrón", "缺一个电子"))
    s.kurve(b, "-(1-cos(pi*x))", farbe=GRAU, dicke=3)
    ke = ka[9]
    for q in ka:
        if q == ke:
            continue
        s.punkt(b, q, -(1 - cos(pi * q)), farbe=BLAU, r=0.075)
    s.kreis(w, 1.65 + ke * 1.4, 1.05 + (-(1 - cos(pi * ke)) + 0.925) * 1.1 / 2.75, 0.095, farbe=ROT, dicke=3.5)
    s.text(b, "k_e", (ke + 0.08, 0.25), groesse=24, ausrichtung="center", farbe=ROT)
    s.linie(b, (ke, -2.3), (ke, 0.05), farbe=ROT, dicke=1.8, dash=DASH)
    s.linie(b, (-ke, -2.3), (-ke, 0.05), farbe=ORANGE, dicke=1.8, dash=DASH)
    s.text(b, "k_h", (-ke - 0.08, 0.25), groesse=24, ausrichtung="center", farbe=ORANGE)
    # Unten: Reihe von Plätzen
    y0 = -0.72
    dy = 0.4
    dx = 0.62
    x0 = -2.05
    n = 7
    for z, (lk, nm) in enumerate(((1, "t_1"), (2, "t_2"), (3, "t_3"))):
        y = y0 - z * dy
        t(s, nm, (x0 - 0.7, y))
        for i in range(n):
            s.linie(w, (x0 + i * dx - 0.28, y - 0.17), (x0 + i * dx + 0.28, y - 0.17), farbe=HELLGRAU, dicke=2)
            if i == lk:
                s.kreis(w, x0 + i * dx, y, 0.12, farbe=ROT, dicke=3.5)
            else:
                s.punkt(w, x0 + i * dx, y, farbe=BLAU, r=0.12)
        if z < 2:
            s.pfeil((x0 + (lk + 1) * dx, y - 0.25), (x0 + lk * dx, y - 0.25), "", farbe=BLAU, dicke=2.5, spitze=0.12)
    xr = x0 + n * dx - 0.02
    s.pfeil((xr, -0.72), (xr + 1.05, -0.72), "", farbe=SCHWARZ, dicke=3, spitze=0.16)
    t(s, "ℰ", (xr + 0.52, -0.48))
    s.pfeil((xr + 1.05, -1.1), (xr, -1.1), "", farbe=BLAU, dicke=3, spitze=0.16)
    t(s, s.tr("el", "Elektronen", "electrons", "electrones", "电子"), (xr + 0.52, -1.32), farbe=BLAU, g=22)
    s.pfeil((xr, -1.56), (xr + 1.05, -1.56), "", farbe=ROT, dicke=3, spitze=0.16)
    t(s, s.tr("lo", "Loch", "hole", "hueco", "空穴"), (xr + 0.52, -1.78), farbe=ROT, g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k9lesen():
    """Vier Schemabilder: Metall, Halbleiter, Isolator, Graphen, jeweils mit Fermi-Energie."""
    s = Szene("gemb1/k9lesen")
    W = 1.43
    H = 2.0
    xs = (-2.68, -0.95, 0.78, 2.51)
    nm = (("met", "Metall", "metal", "metal", "金属"), ("hl", "Halbleiter", "semiconductor", "semiconductor", "半导体"), ("iso", "Isolator", "insulator", "aislante", "绝缘体"), ("gr", "Graphen", "graphene", "grafeno", "石墨烯"))
    for i, xc in enumerate(xs):
        a = s.achsen((-1, 1), (-3, 3), breite=W, hoehe=H, mitte=(xc, 0.15), xl="", yl="E" if i == 0 else "", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, xticks="", yticks="")
        s.text(a, s.tr(nm[i][0], *nm[i][1:]), (0, -3.85), groesse=24, ausrichtung="center")
        if i == 0:
            s.kurve(a, "-1.9*cos(pi*x)", x=(-0.5, 0.5), farbe=BLAU, dicke=5)
            s.kurve(a, "-1.9*cos(pi*x)", x=(0.5, 1), farbe=GRAU, dicke=3)
            s.kurve(a, "-1.9*cos(pi*x)", x=(-1, -0.5), farbe=GRAU, dicke=3)
        elif i == 1:
            s.band(a, -1, 1, -0.4, 0.4, farbe=GRAU, deckung=0.22)
            s.kurve(a, "-0.4-0.95*(1-cos(pi*x))", farbe=BLAU, dicke=5)
            s.kurve(a, "0.4+0.95*(1-cos(pi*x))", farbe=GRAU, dicke=3)
        elif i == 2:
            s.band(a, -1, 1, -1.5, 1.5, farbe=GRAU, deckung=0.22)
            s.kurve(a, "-1.5-0.6*(1-cos(pi*x))", farbe=BLAU, dicke=5)
            s.kurve(a, "1.5+0.6*(1-cos(pi*x))", farbe=GRAU, dicke=3)
        else:
            s.kurve(a, "-2.6*abs(sin(pi*x/2))", farbe=BLAU, dicke=5)
            s.kurve(a, "2.6*abs(sin(pi*x/2))", farbe=GRAU, dicke=3)
        s.linie(a, (-1, 0), (1, 0), farbe=ROT, dicke=2.5, dash=DASH)
        if i == 3:
            s.text(a, "E_F", (1.12, 0.0), groesse=24, ausrichtung="left", farbe=ROT)
    s.speichern()


if __name__ == "__main__":
    k9quadrat()
    k9graphen()
    k9silizium()
    k9gaas()
    k9masse()
    k9ellipse()
    k9loch()
    k9lesen()
