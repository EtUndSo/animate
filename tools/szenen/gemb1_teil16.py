"""GEMB 1 Teil 16 (kap16_stufen.tex): Der reale MOS-Kondensator.

Aufruf: python tools/szenen/gemb1_teil16.py, danach python tools/szenen_ansehen.py out.png gemb1/k16austritt ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap16.py (dasselbe Rechenmodell).
"""
import sys
from math import exp, log, pi, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN, HELLGRAU2, HELLORANGE = "#f6dede", "#dceafa", "#ddf0e4", "#ececec", "#fbe3d8"

# ------------------------------------------------------------ Rechenmodell (wie rechnung_kap16.py), SI-Einheiten
e = 1.602176634e-19
h = 6.62607015e-34
m0 = 9.1093837e-31
kB = 1.380649e-23 / e
eps0 = 8.8541878e-12
T = 300.0
VT = kB * T
EG = 1.12
EPS = eps0 * 11.7
EPSIS = eps0 * 3.9
CHISC = 4.05


def Nmass(m):
    return 2 * (2 * pi * m * m0 * 1.380649e-23 * T / h**2)**1.5


NI = sqrt(Nmass(1.08) * Nmass(0.81)) * exp(-EG / (2 * VT))
NA = 3e22
DIS = 20e-9
CIS = EPSIS / DIS
GAMMA = sqrt(2 * EPS * e * NA) / CIS
PWI = VT * log(NA / NI)
PSI = 2 * PWI
N0 = NI**2 / NA
LMAX = sqrt(2 * EPS * PSI / (e * NA))
PHIM = 4.10
PHISC = CHISC + EG / 2 + PWI
DPHI = PHIM - PHISC
QIS, QSS = 8e-5, 3.2e-5              # C/m^2
VFB = DPHI - (QIS + QSS) / CIS
VTHID = PSI + GAMMA * sqrt(PSI)
VWIID = PWI + GAMMA * sqrt(PWI)
VTH = VFB + VTHID
VWI = VFB + VWIID
DIT = 5e15                           # 1/(eV m^2)
CIT = e * DIT                        # F/m^2
TAU = 1e-6


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR, on=None):
    s.text(on, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit, key=None):
    return s.tr(key or ("a_" + name + einheit), name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def F(phi):
    u = phi / VT
    return NA * (VT * np.exp(-u) + phi - VT) + N0 * (VT * np.exp(u) - phi - VT)


def dF(phi):
    u = phi / VT
    return NA * (1 - np.exp(-u)) + N0 * (np.exp(u) - 1)


def Qex(phi):
    if phi == 0:
        return 0.0
    return -(1 if phi > 0 else -1) * sqrt(2 * e * EPS * max(F(phi), 0.0))


def CSC(phi):
    if abs(phi) < 1e-7:
        return sqrt(e * EPS * (NA + N0) / VT)
    return e * EPS * abs(dF(phi)) / sqrt(2 * e * EPS * max(F(phi), 1e-300))


def CSChf(phi):
    """Nur die Löcher antworten: Anteil der Majoritätsträger aus F."""
    if abs(phi) < 1e-7:
        return sqrt(e * EPS * NA / VT)
    u = phi / VT
    Fp = NA * (VT * exp(-u) + phi - VT)
    return e * EPS * abs(NA * (1 - exp(-u))) / sqrt(2 * e * EPS * Fp)


def rei(a, b):
    return a * b / (a + b)


def VG(phi, vfb=VFB, c=0.0):
    return vfb + phi - Qex(phi) / CIS + c * phi / CIS


def phi_aus_V(V, vfb=VFB, c=0.0):
    a, b = -0.5, 1.4
    for _ in range(120):
        m = (a + b) / 2
        if VG(m, vfb, c) < V:
            a = m
        else:
            b = m
    return m


def phi_kasten(U):
    return (-GAMMA / 2 + sqrt(GAMMA**2 / 4 + U))**2


def Ldep(phi):
    return sqrt(2 * EPS * phi / (e * NA))


def jgen(L):
    return e * NI * L / (2 * TAU)


# ------------------------------------------------------------------------------------------ Stufe 1
def k16austritt():
    """Niveaus vor dem Kontakt und Bänderdiagramm nach dem Kontakt bei V_G = 0 (nur Austrittsarbeitsdifferenz)."""
    s = Szene("gemb1/k16austritt")
    sc, y0 = 0.52, -1.55

    def y(E):
        return y0 + sc * E

    Ec, Ei, Ev, Evac = 0.951, 0.389, -0.171, 4.999
    unten = -0.75
    phi0 = phi_kasten(-DPHI)
    vis0 = -DPHI - phi0
    # ----- links: vor dem Kontakt
    xm0, xm1, xi0, xi1, xs0, xs1 = -3.6, -2.8, -2.5, -2.05, -1.75, -0.55
    t(s, s.tr("vor", "vor dem Kontakt", "before contact", "antes del contacto", "接触前"), (-2.05, y(Evac) + 0.68), g=26)
    s.linie(None, (xm0, y(Evac)), (xs1, y(Evac)), farbe=SCHWARZ, dicke=3)
    t(s, "E_{vac}", (-2.05, y(Evac) + 0.22), g=22)
    s.band(None, xm0, xm1, y(unten), y(0.899), farbe=BLAU, deckung=0.22)
    s.linie(None, (xm0, y(0.899)), (xm1, y(0.899)), farbe=ROT, dicke=3)
    s.band(None, xi0, xi1, y(unten), y(Evac - 0.9), farbe=GRAU, deckung=0.22)
    s.linie(None, (xs0, y(Ec)), (xs1, y(Ec)), farbe=GRUEN, dicke=4)
    s.linie(None, (xs0, y(Ei)), (xs1, y(Ei)), farbe=GRUEN, dicke=2.5, dash=DOT)
    s.linie(None, (xs0, y(0)), (xs1, y(0)), farbe=ROT, dicke=3, dash=DASH)
    s.linie(None, (xs0, y(Ev)), (xs1, y(Ev)), farbe=GRUEN, dicke=4)
    pf = dict(farbe=SCHWARZ, dicke=2.5, spitze=0.11, doppelt=True, on=None)
    s.pfeil((-3.5, y(Evac)), (-3.5, y(0.899)), "", **pf)
    t(s, "\u03a6_M", (-3.43, y(3.3)), a="left", g=22)
    t(s, "4.10 eV", (-3.43, y(2.6)), a="left", g=22)
    s.pfeil((-1.42, y(Evac)), (-1.42, y(Ec)), "", **pf)
    t(s, "\u03c7_{SC}", (-1.48, y(3.3)), a="right", g=22)
    s.pfeil((-0.85, y(Evac)), (-0.85, y(0)), "", **pf)
    t(s, "\u03a6_{SC}", (-0.79, y(3.3)), a="left", g=22)
    t(s, "5.00 eV", (-0.79, y(2.6)), a="left", g=22)
    t(s, "Al", ((xm0 + xm1) / 2, y(unten) - 0.26), g=22)
    t(s, "SiO_2", ((xi0 + xi1) / 2, y(unten) - 0.26), g=22)
    t(s, "p-Si", ((xs0 + xs1) / 2, y(unten) - 0.26), g=22)
    # ----- rechts: nach dem Kontakt, V_G = 0
    xm0, xm1, xi1, xs1 = 0.35, 1.0, 1.45, 3.05
    xnm = np.linspace(0, 300, 121)
    pp = (e * NA / (2 * EPS)) * np.clip(Ldep(phi0) - xnm * 1e-9, 0, None)**2
    xw = xi1 + xnm / 300 * (xs1 - xi1)
    t(s, s.tr("nach", "nach dem Kontakt", "after contact", "tras el contacto", "接触后"), (1.7, y(Evac) + 0.68), g=26)
    s.band(None, xi1, xi1 + Ldep(phi0) * 1e9 / 300 * (xs1 - xi1), y(unten), y(Evac), farbe=ORANGE, deckung=0.10)
    s.band(None, xm0, xm1, y(unten), y(0), farbe=BLAU, deckung=0.22)
    s.band(None, xm1, xi1, y(unten), y(unten) + 0.001, farbe=GRAU, deckung=0.0)
    s.linie(None, (xm1, y(unten)), (xm1, y(4.10 - 0.9)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xi1, y(unten)), (xi1, y(Evac - phi0 - 0.9)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm1, y(4.10 - 0.9)), (xi1, y(Evac - phi0 - 0.9)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm0, y(4.10)), (xm1, y(4.10)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm1, y(4.10)), (xi1, y(Evac - phi0)), farbe=SCHWARZ, dicke=3)
    s.daten(None, list(zip(xw, y(Evac - pp))), farbe=SCHWARZ, dicke=3)
    s.daten(None, list(zip(xw, y(Ec - pp))), farbe=GRUEN, dicke=4)
    s.daten(None, list(zip(xw, y(Ei - pp))), farbe=GRUEN, dicke=2.5, dash=DOT)
    s.daten(None, list(zip(xw, y(Ev - pp))), farbe=GRUEN, dicke=4)
    s.linie(None, (xm0, y(0)), (xs1, y(0)), farbe=ROT, dicke=3, dash=DASH)
    t(s, "E_{vac}", (xs1 + 0.06, y(Evac)), a="left", g=22)
    t(s, "E_C", (xs1 + 0.06, y(Ec)), a="left", farbe=GRUEN, g=22)
    t(s, "E_{Fi}", (xs1 + 0.06, y(Ei) + 0.03), a="left", farbe=GRUEN, g=22)
    t(s, "E_F", (xs1 + 0.06, y(0) + 0.06), a="left", farbe=ROT, g=22)
    t(s, "E_V", (xs1 + 0.06, y(Ev) - 0.13), a="left", farbe=GRUEN, g=22)
    # Abstände rechts
    s.linie(None, (xm1, y(Evac)), (xi1, y(Evac)), farbe=GRAU, dicke=2, dash=DOT)
    s.linie(None, (xi1, y(Evac - phi0)), (2.5, y(Evac - phi0)), farbe=GRAU, dicke=2, dash=DOT)
    s.linie(None, (xi1, y(Evac)), (2.5, y(Evac)), farbe=GRAU, dicke=2, dash=DOT)
    s.pfeil((2.45, y(Evac)), (2.45, y(Evac - phi0)), "", **pf)
    t(s, "e\u03c6_{s0}", (2.5, y(Evac - phi0 / 2) - 0.32), a="left", g=22)
    s.pfeil((1.22, y(Evac - phi0)), (1.22, y(4.10)), "", **pf)
    s.linie(None, (xm0, y(4.10)), (xm1, y(4.10)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm1, y(4.10)), (1.3, y(4.10)), farbe=GRAU, dicke=2, dash=DOT)
    t(s, "eV_{IS,0}", (1.0, y(4.32)), a="right", g=22)
    t(s, "+ + +", (0.67, y(0.62)), g=24, farbe=ROT)
    t(s, "\u2212 \u2212 \u2212", (1.86, y(2.4)), g=24, farbe=BLAU)
    t(s, "Al", ((xm0 + xm1) / 2, y(unten) - 0.26), g=22)
    t(s, "SiO_2", ((xm1 + xi1) / 2, y(unten) - 0.26), g=22)
    t(s, "p-Si", (2.3, y(unten) - 0.26), g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k16ladung():
    """Ladungsverteilung ohne Spannung und bei der Flachbandspannung, drei Fälle (Höhen schematisch)."""
    s = Szene("gemb1/k16ladung")
    bx = (-2.4, 0.65)                  # linker Rand je Spalte
    by = (1.7, 0.2, -1.3)              # Nullinie je Zeile
    b = 2.65
    gm, gi = 0.3, 0.75                  # Breite Metall, Isolator

    def rahmen(x0, y0):
        s.band(None, x0, x0 + gm, y0 - 0.68, y0 + 0.68, farbe=GRAU, deckung=0.35)
        s.band(None, x0 + gm, x0 + gm + gi, y0 - 0.68, y0 + 0.68, farbe=GRAU, deckung=0.10)
        s.linie(None, (x0, y0), (x0 + b, y0), farbe=SCHWARZ, dicke=2.5)
        s.linie(None, (x0 + gm + gi, y0 - 0.68), (x0 + gm + gi, y0 + 0.68), farbe=GRAU, dicke=2)

    def balken(x0, x1, y0, hoehe, farbe):
        s.band(None, x0, x1, min(y0, y0 + hoehe), max(y0, y0 + hoehe), farbe=farbe, deckung=0.75)

    t(s, "V_G = 0", (bx[0] + b / 2, by[0] + 0.92), g=26)
    t(s, "V_G = V_{FB}", (bx[1] + b / 2, by[0] + 0.92), g=26)
    for i, lab in enumerate(("a)  \u0394\u03a6", "b)  Q'_{IS}", "c)  Q'_{SS}")):
        t(s, lab, (-3.6, by[i]), a="left", g=26)
    for x0 in bx:
        for y0 in by:
            rahmen(x0, y0)
    xM = gm                             # Grenze Metall/Isolator
    xS = gm + gi                        # Grenze Isolator/Halbleiter
    # Zeile a
    x0, y0 = bx[0], by[0]
    balken(x0 + xM - 0.12, x0 + xM, y0, 0.56, ROT)
    balken(x0 + xS, x0 + xS + 1.1, y0, -0.24, BLAU)
    t(s, "Q'_M", (x0 + xM + 0.03, y0 + 0.46), a="left", g=22, farbe=ROT)
    t(s, "Q'_{SC}", (x0 + xS + 0.55, y0 - 0.45), g=22, farbe=BLAU)
    t(s, s.tr("keine", "keine Ladung", "no charge", "sin carga", "无电荷"), (bx[1] + xS + 0.8, by[0] + 0.35), g=22, farbe=GRAU)
    # Zeile b
    x0, y0 = bx[0], by[1]
    balken(x0 + xM, x0 + xS, y0, 0.36, ROT)
    balken(x0 + xS, x0 + xS + 0.75, y0, -0.24, BLAU)
    balken(x0 + xM - 0.12, x0 + xM, y0, -0.24, BLAU)
    t(s, "Q'_{IS}", (x0 + xM + 0.38, y0 + 0.5), g=22, farbe=ROT)
    t(s, "Q'_{SC}", (x0 + xS + 0.4, y0 - 0.45), g=22, farbe=BLAU)
    t(s, "Q'_M", (x0 + xM - 0.06, y0 - 0.45), a="right", g=22, farbe=BLAU)
    x0 = bx[1]
    balken(x0 + xM, x0 + xS, y0, 0.36, ROT)
    balken(x0 + xM - 0.12, x0 + xM, y0, -0.56, BLAU)
    t(s, "Q'_{IS}", (x0 + xM + 0.38, y0 + 0.5), g=22, farbe=ROT)
    t(s, "Q'_M", (x0 + xM + 0.03, y0 - 0.45), a="left", g=22, farbe=BLAU)
    # Zeile c
    x0, y0 = bx[0], by[2]
    balken(x0 + xS - 0.12, x0 + xS, y0, 0.56, ROT)
    balken(x0 + xS, x0 + xS + 0.75, y0, -0.24, BLAU)
    balken(x0 + xM - 0.12, x0 + xM, y0, -0.24, BLAU)
    t(s, "Q'_{SS}", (x0 + xS + 0.05, y0 + 0.44), a="left", g=22, farbe=ROT)
    t(s, "Q'_{SC}", (x0 + xS + 0.4, y0 - 0.45), g=22, farbe=BLAU)
    t(s, "Q'_M", (x0 + xM - 0.06, y0 - 0.45), a="right", g=22, farbe=BLAU)
    x0 = bx[1]
    balken(x0 + xS - 0.12, x0 + xS, y0, 0.56, ROT)
    balken(x0 + xM - 0.12, x0 + xM, y0, -0.56, BLAU)
    t(s, "Q'_{SS}", (x0 + xS + 0.05, y0 + 0.44), a="left", g=22, farbe=ROT)
    t(s, "Q'_M", (x0 + xM + 0.03, y0 - 0.45), a="left", g=22, farbe=BLAU)
    t(s, "Al", (bx[0] + gm / 2, by[2] - 0.9), g=22)
    t(s, "SiO_2", (bx[0] + gm + gi / 2, by[2] - 0.9), g=22)
    t(s, "p-Si", (bx[0] + xS + 0.9, by[2] - 0.9), g=22)
    t(s, "Al", (bx[1] + gm / 2, by[2] - 0.9), g=22)
    t(s, "SiO_2", (bx[1] + gm + gi / 2, by[2] - 0.9), g=22)
    t(s, "p-Si", (bx[1] + xS + 0.9, by[2] - 0.9), g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k16schwelle():
    """Oberflächenpotential über der Gatespannung: ideal und real, um V_FB verschoben."""
    s = Szene("gemb1/k16schwelle")
    a = s.achsen((-3, 3), (-0.2, 1.1), breite=6.2, hoehe=2.6, mitte=(0.1, 0.1), xl=achse(s, "V_G", "V", "a_vg"), yl=achse(s, "\u03c6_s", "V", "a_phis"),
                 xticks="-3;-2;-1;0;1;2;3", yticks="0;0.25;0.5;0.75;1")
    ps = [i / 1000 for i in range(-200, 1001, 5)]
    id_ = [(VG(p, 0.0), p) for p in ps]
    re_ = [(VG(p, VFB), p) for p in ps]
    s.daten(a, id_, farbe=GRAU, dicke=4, dash=DASH)
    s.daten(a, re_, farbe=BLAU, dicke=5)
    s.linie(a, (-3, PSI), (3, PSI), farbe=ROT, dicke=2, dash=DOT)
    s.linie(a, (-3, PWI), (3, PWI), farbe=GRUEN, dicke=2, dash=DOT)
    s.linie(a, (-3, 0), (3, 0), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "\u03c6_{s,SI}", (-2.9, PSI + 0.08), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "\u03c6_{s,WI}", (-2.9, PWI + 0.08), groesse=22, ausrichtung="left", farbe=GRUEN)
    for x, y_, f in ((VFB, 0.0, BLAU), (VWI, PWI, BLAU), (VTH, PSI, BLAU), (0.0, 0.0, GRAU), (VWIID, PWI, GRAU), (VTHID, PSI, GRAU)):
        s.punkt(a, x, y_, farbe=f, r=0.075)
    s.text(a, "V_{FB}", (VFB - 0.1, 0.09), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(a, "V_{WI}", (VWI - 0.2, PWI - 0.02), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(a, "V_{th}", (VTH - 0.08, PSI + 0.09), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(a, s.tr("real", "real", "real", "real", "实际"), (1.15, 0.97), groesse=24, ausrichtung="right", farbe=BLAU)
    s.text(a, s.tr("ideal", "ideal", "ideal", "ideal", "理想"), (2.15, 0.70), groesse=24, ausrichtung="left", farbe=GRAU)
    s.pfeil((VTHID - 0.03, 0.5), (VTH + 0.03, 0.5), "", on=a, farbe=ROT, dicke=3, spitze=0.13)
    s.text(a, "V_{FB} = \u22120.96 V", (1.55, 0.44), groesse=22, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k16zustaende():
    """Besetzung der Interfacezustände im Flachbandfall und bei Bandverbiegung."""
    s = Szene("gemb1/k16zustaende")
    sc, y0 = 1.55, -0.3

    def y(E):
        return y0 + sc * E

    Ec, Ei, Ev = 0.951, 0.389, -0.171

    def teil(xI, breite, phi, titel):
        xs1 = xI + breite
        L = 2.0 * sqrt(phi / 0.6) if phi > 0 else 0.0
        xx = np.linspace(0, breite, 91)
        pp = phi * np.clip(1 - xx / L, 0, None)**2 if phi > 0 else 0 * xx
        xw = xI + xx
        t(s, titel, (xI + breite / 2 - 0.25, y(Ec) + 0.55), g=26)
        s.daten(None, list(zip(xw, y(Ec - pp))), farbe=GRUEN, dicke=4)
        s.daten(None, list(zip(xw, y(Ei - pp))), farbe=GRUEN, dicke=2.5, dash=DOT)
        s.daten(None, list(zip(xw, y(Ev - pp))), farbe=GRUEN, dicke=4)
        s.linie(None, (xI - 0.42, y(0)), (xs1, y(0)), farbe=ROT, dicke=3, dash=DASH)
        # Zustände als Streifen an der Grenzfläche
        b = 0.36
        ec0, ev0, cnl = Ec - phi, Ev - phi, Ei - phi
        s.band(None, xI - b, xI, y(ev0), y(0), farbe=BLAU, deckung=0.45)
        s.band(None, xI - b, xI, y(0), y(ec0), farbe=GRAU, deckung=0.10)
        s.linie(None, (xI, y(ev0 - 0.08)), (xI, y(ec0 + 0.08)), farbe=SCHWARZ, dicke=3)
        s.linie(None, (xI - b, y(ev0)), (xI - b, y(ec0)), farbe=GRAU, dicke=2)
        s.linie(None, (xI - b, y(ev0)), (xI, y(ev0)), farbe=GRAU, dicke=2)
        s.linie(None, (xI - b, y(ec0)), (xI, y(ec0)), farbe=GRAU, dicke=2)
        s.linie(None, (xI - b - 0.08, y(cnl)), (xI + 0.03, y(cnl)), farbe=SCHWARZ, dicke=4)
        t(s, "E_{CNL}", (xI - b - 0.12, y(cnl)), a="right", g=22)
        return cnl, b

    cnl, b = teil(-1.8, 1.55, 0.0, "V_G = V_{FB}")
    t(s, "+", (-1.8 - b / 2, y(0.19)), g=26, farbe=ROT)
    t(s, s.tr("bes", "besetzt", "filled", "ocupado", "占据"), (-1.8 - b - 0.1, y(-0.1)), a="right", g=22, farbe=BLAU)
    t(s, s.tr("leer", "leer", "empty", "vacío", "空"), (-1.8 - b - 0.1, y(0.75)), a="right", g=22, farbe=GRAU)
    t(s, "E_F", (-0.22, y(0) + 0.15), a="right", g=22, farbe=ROT)
    t(s, "E_C", (-0.22, y(Ec) + 0.17), a="right", g=22, farbe=GRUEN)
    t(s, "E_V", (-0.22, y(Ev) - 0.17), a="right", g=22, farbe=GRUEN)
    cnl, b = teil(1.75, 1.85, 0.6, "V_G > V_{FB}")
    t(s, "\u2212", (1.75 - b / 2, y(-0.105)), g=26, farbe=BLAU)
    t(s, "E_F", (3.6, y(0) + 0.15), a="right", g=22, farbe=ROT)
    t(s, "E_C", (3.6, y(Ec) + 0.17), a="right", g=22, farbe=GRUEN)
    t(s, "E_V", (3.6, y(Ev) - 0.17), a="right", g=22, farbe=GRUEN)
    pf = dict(farbe=SCHWARZ, dicke=2.5, spitze=0.11, doppelt=True, on=None)
    s.linie(None, (1.75, y(Ec)), (2.9, y(Ec)), farbe=GRAU, dicke=2, dash=DOT)
    s.pfeil((2.1, y(Ec)), (2.1, y(Ec - 0.6)), "", **pf)
    t(s, "e\u03c6_s", (2.17, y(Ec - 0.42)), a="left", g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def kurven(c=0.0, vmin=-3.0, vmax=3.0):
    """Liefert (V_G, C_nf/C_IS, C_hf/C_IS) mit konstanter Interfacekapazität c."""
    ps = sorted(set([i / 1000 for i in range(-240, 1001, 4)]))
    nf, hf = [], []
    for p in ps:
        v = VG(p, VFB, c)
        if vmin <= v <= vmax:
            nf.append((v, rei(CIS, CSC(p) + c) / CIS))
            hf.append((v, rei(CIS, CSChf(p)) / CIS))
    return nf, hf


def k16kennlinie():
    """C-V-Kennlinien bei niedriger und hoher Frequenz, ohne und mit Interfacezuständen."""
    s = Szene("gemb1/k16kennlinie")
    yl = "C'_{ges} / C'_{IS}"
    a = s.achsen((-3, 3), (0, 1.1), breite=6.2, hoehe=1.8, mitte=(0.1, 1.25), xl="", yl=yl, xticks="-3;-2;-1;0;1;2;3", yticks="0;0.5;1", xzahlen=False)
    nf0, hf0 = kurven(0.0)
    s.daten(a, nf0, farbe=BLAU, dicke=4)
    s.daten(a, hf0, farbe=GRUEN, dicke=4)
    s.linie(a, (VFB, 0), (VFB, 1.1), farbe=GRAU, dicke=2, dash=DOT)
    s.linie(a, (VTH, 0), (VTH, 1.1), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "V_{FB}", (VFB - 0.07, 0.1), groesse=22, ausrichtung="right")
    s.text(a, "V_{th}", (VTH + 0.07, 0.1), groesse=22, ausrichtung="left")
    s.text(a, s.tr("akk", "Akkumulation", "accumulation", "acumulación", "积累"), (-1.75, 1.2), groesse=22, ausrichtung="center")
    s.text(a, s.tr("ver", "Verarmung", "depletion", "vaciamiento", "耗尽"), ((VFB + VTH) / 2, 1.2), groesse=22, ausrichtung="center")
    s.text(a, s.tr("inv", "Inversion", "inversion", "inversión", "反型"), (1.7, 1.2), groesse=22, ausrichtung="center")
    s.text(a, s.tr("nfk", "niedrige Frequenz", "low frequency", "baja frecuencia", "低频"), (1.55, 0.72), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, s.tr("hfk", "hohe Frequenz", "high frequency", "alta frecuencia", "高频"), (1.55, 0.36), groesse=22, ausrichtung="left", farbe=GRUEN)
    b = s.achsen((-3, 3), (0, 1.1), breite=6.2, hoehe=1.8, mitte=(0.1, -0.95), xl=achse(s, "V_G", "V", "a_vg"), yl=yl, xticks="-3;-2;-1;0;1;2;3", yticks="0;0.5;1")
    nf1, hf1 = kurven(CIT)
    s.daten(b, nf0, farbe=HELLGRAU, dicke=2.5, dash=DASH)
    s.daten(b, hf0, farbe=HELLGRAU, dicke=2.5, dash=DASH)
    s.daten(b, nf1, farbe=BLAU, dicke=4)
    s.daten(b, hf1, farbe=GRUEN, dicke=4)
    V2 = VTH + CIT / CIS * PSI
    s.linie(b, (VFB, 0), (VFB, 1.1), farbe=GRAU, dicke=2, dash=DOT)
    s.linie(b, (V2, 0), (V2, 1.1), farbe=GRAU, dicke=2, dash=DOT)
    s.text(b, "V_{FB}", (VFB - 0.07, 0.1), groesse=22, ausrichtung="right")
    s.text(b, "V_{th}", (V2 + 0.07, 0.1), groesse=22, ausrichtung="left")
    s.text(b, "D_{it} = 5\u00b710^{11} /(eV cm^2)", (2.95, 0.5), groesse=22, ausrichtung="right")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def relax(V, dt=0.01, tmax=60.0):
    Q, tt = 0.0, 0.0
    out = []
    pE = phi_aus_V(V)
    while tt < tmax:
        p = phi_kasten(V - VFB - Q / CIS)
        if p <= pE:
            out.append((tt, rei(CIS, EPS / Ldep(pE)) / CIS))
            break
        L = Ldep(p)
        out.append((tt, rei(CIS, EPS / L) / CIS))
        Q += jgen(L) * dt
        tt += dt
    return out


def k16tief():
    """Tiefenverarmung: Kennlinie nach schnellem Hochfahren und Rückkehr ins Gleichgewicht nach einem Sprung."""
    s = Szene("gemb1/k16tief")
    yl = "C'_{ges} / C'_{IS}"
    a = s.achsen((-1, 5), (0, 0.8), breite=2.85, hoehe=2.3, mitte=(-1.9, 0.1), xl=achse(s, "V_G", "V", "a_vg"), yl=yl, xticks="-1;1;3;5", yticks="0;0.2;0.4;0.6;0.8")
    nf, hf = kurven(0.0, -1, 5)
    # Hochfrequenz im Gleichgewicht bis 5 V
    gg = []
    for i in range(-100, 501, 5):
        v = i / 100
        gg.append((v, rei(CIS, CSChf(phi_aus_V(v))) / CIS))
    s.daten(a, gg, farbe=GRUEN, dicke=4)
    tv = []
    for i in range(int(VTH * 100), 501, 5):
        v = i / 100
        tv.append((v, rei(CIS, EPS / Ldep(phi_kasten(v - VFB))) / CIS))
    s.daten(a, tv, farbe=ROT, dicke=4)
    s.linie(a, (VTH, 0), (VTH, 0.8), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "V_{th}", (VTH + 0.1, 0.72), groesse=22, ausrichtung="left")
    s.text(a, s.tr("glgw", "langsam", "slow", "lento", "慢速"), (2.0, 0.335), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, s.tr("schn", "schnell", "fast", "rápido", "快速"), (1.0, 0.075), groesse=22, ausrichtung="left", farbe=ROT)
    V = 3.0
    r0 = rei(CIS, EPS / Ldep(phi_kasten(V - VFB))) / CIS
    r1 = rei(CIS, EPS / Ldep(phi_aus_V(V))) / CIS
    s.punkt(a, V, r0, farbe=ROT)
    s.pfeil((V, r0 + 0.012), (V, r1 - 0.012), "", on=a, farbe=SCHWARZ, dicke=3, spitze=0.13)
    b = s.achsen((0, 25), (0, 0.3), breite=2.45, hoehe=2.3, mitte=(1.95, 0.1), xl=s.tr("a_ts", "t in s", "t in s", "t en s", "t / s"), yl="", xticks="0;10;20", yticks="0;0.1;0.2;0.3")
    rr = relax(V)
    s.daten(b, duenn(rr, 2e-3) + [(25, rr[-1][1])], farbe=ROT, dicke=4)
    s.linie(b, (0, rr[-1][1]), (25, rr[-1][1]), farbe=GRUEN, dicke=2, dash=DOT)
    s.text(b, "V_G = 3 V", (1.5, 0.045), groesse=22, ausrichtung="left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k16auswertung():
    """Hochfrequenzkurve in nF/cm^2 mit Ablesewerten und Gerade 1/C'^2."""
    s = Szene("gemb1/k16auswertung")
    a = s.achsen((-4, 3), (0, 190), breite=2.7, hoehe=2.3, mitte=(-2.05, 0.1), xl=achse(s, "V_G", "V", "a_vg"), yl=achse(s, "C'", "nF/cm^2", "a_cn"), xticks="-4;-2;0;2", yticks="0;50;100;150")
    ps = [i / 1000 for i in range(-280, 1001, 4)]
    pts = [(VG(p), rei(CIS, CSChf(p)) * 1e5) for p in ps]
    pts = [(v, c) for v, c in pts if -4 <= v <= 3]
    s.daten(a, pts, farbe=GRUEN, dicke=4)
    ci, cfb = CIS * 1e5, rei(CIS, sqrt(e * EPS * NA / VT)) * 1e5
    s.linie(a, (-4, ci), (3, ci), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "C'_{IS}", (2.9, ci - 15), groesse=22, ausrichtung="right")
    cm = rei(CIS, EPS / LMAX) * 1e5
    s.linie(a, (-4, cm), (3, cm), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "C'_{min}", (-3.6, cm + 13), groesse=22, ausrichtung="left")
    s.punkt(a, VFB, cfb, farbe=BLAU)
    s.text(a, "V_{FB}", (VFB + 0.25, cfb + 7), groesse=22, ausrichtung="left", farbe=BLAU)
    s.punkt(a, VTH, rei(CIS, CSChf(PSI)) * 1e5, farbe=ROT)
    s.text(a, "V_{th}", (VTH + 0.15, 62), groesse=22, ausrichtung="left", farbe=ROT)
    b = s.achsen((-1.5, 1.0), (0, 7), breite=2.45, hoehe=2.3, mitte=(1.75, 0.1), xl=achse(s, "V_G", "V", "a_vg"), yl=achse(s, "1/C'^2", "10^{-4} cm^4/nF^2", "a_c2"), xticks="-1;0;1", yticks="0;2;4;6")
    # 1/C^2 in 10^-4 cm^4/nF^2
    e2 = [(v, 1e4 / c**2) for v, c in pts if -1.5 <= v <= 1.0]
    s.daten(b, e2, farbe=GRUEN, dicke=4)
    sl = 2 / (e * EPS * NA) * 1e-10 * 1e4       # 10^-4 cm^4/(nF^2 V)
    y0 = 1e4 / ci**2
    s.linie(b, (VFB, y0), (VTH + 0.15, y0 + sl * (VTH + 0.15 - VFB)), farbe=ROT, dicke=2.5, dash=DASH)
    s.linie(b, (-1.5, y0), (1.0, y0), farbe=GRAU, dicke=2, dash=DOT)
    s.punkt(b, VFB, y0, farbe=BLAU)
    s.text(b, "1/C'_{IS}^2", (0.95, y0 + 0.34), groesse=22, ausrichtung="right")
    s.linie(b, (VFB, y0), (VFB, 1.45), farbe=BLAU, dicke=2, dash=DOT)
    s.text(b, "V_{FB}", (VFB, 1.75), groesse=22, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k16ccd():
    """Drei-Phasen-CCD: drei Takte, Topf unter den Elektroden, Ladungspaket wandert nach rechts."""
    s = Szene("gemb1/k16ccd")
    xl = -3.1                  # linker Rand der ersten Elektrode
    gb, gl = 0.72, 0.24        # Elektrodenbreite, Lücke
    n = 6
    ytop = 2.5

    def xg(i):
        return xl + i * (gb + gl)

    # Elektroden und Oxid
    s.band(None, xl - 0.25, xg(n - 1) + gb + 0.25, ytop - 0.22, ytop - 0.02, farbe=GRAU, deckung=0.3)
    for i in range(n):
        s.band(None, xg(i), xg(i) + gb, ytop, ytop + 0.16, farbe=SCHWARZ, deckung=0.9)
        t(s, "V_%d" % (i % 3 + 1), (xg(i) + gb / 2, ytop + 0.42), g=24, farbe=(BLAU if i % 3 == 0 else (ROT if i % 3 == 1 else GRUEN)))
    s.linie(None, (xg(3) - gl / 2, ytop + 0.72), (xg(3) - gl / 2, -1.95), farbe=GRAU, dicke=2, dash=DASH)
    t(s, s.tr("z1", "Zelle 1", "cell 1", "celda 1", "单元 1"), (xg(1) + gb / 2, ytop + 0.86), g=24)
    t(s, s.tr("z2", "Zelle 2", "cell 2", "celda 2", "单元 2"), (xg(4) + gb / 2, ytop + 0.86), g=24)
    t(s, "SiO_2", (xg(5) + gb + 0.32, ytop - 0.12), a="left", g=22)

    def zeile(y0, tiefen, elek, label):
        """tiefen: Tiefe je Elektrode (Einheiten), elek: Liste (x, y) der Elektronen."""
        pts = [(xl - 0.25, y0 - tiefen[2])]
        for i in range(n):
            d = tiefen[i % 3]
            pts += [(xg(i) + 0.03, y0 - d), (xg(i) + gb - 0.03, y0 - d)]
        pts.append((xg(n - 1) + gb + 0.25, y0 - tiefen[0]))
        s.daten(None, pts, farbe=SCHWARZ, dicke=3)
        t(s, label, (xl - 0.55, y0 - 0.0), a="right", g=26)
        for (x, y_) in elek:
            s.punkt(None, x, y_, farbe=BLAU, r=0.085)

    def paket(x0, y0, anz):
        return [(x0 + k * 0.17, y0) for k in range(anz)]

    y1, y2, y3 = 1.7, 0.4, -1.1
    d1 = (0.62, 0.2, 0.2)
    zeile(y1, d1, paket(xg(0) + 0.11, y1 - 0.52, 4) + paket(xg(3) + 0.2, y1 - 0.52, 2), "a")
    d2 = (0.62, 0.92, 0.2)
    zeile(y2, d2, paket(xg(0) + 0.32, y2 - 0.52, 2) + paket(xg(1) + 0.2, y2 - 0.82, 2) + paket(xg(3) + 0.36, y2 - 0.52, 1) + paket(xg(4) + 0.28, y2 - 0.82, 1), "b")
    s.pfeil((xg(0) + 0.5, y2 - 0.34), (xg(1) + 0.3, y2 - 0.62), "", farbe=SCHWARZ, dicke=2.5, spitze=0.11)
    d3 = (0.2, 0.62, 0.2)
    zeile(y3, d3, paket(xg(1) + 0.11, y3 - 0.52, 4) + paket(xg(4) + 0.2, y3 - 0.52, 2), "c")
    t(s, "V_1 > V_2 = V_3", (xg(1) + gb / 2, y1 + 0.1), g=22)
    t(s, "V_2 > V_1 > V_3", (xg(1) + gb / 2, y2 + 0.1), g=22)
    t(s, "V_2 > V_1 = V_3", (xg(1) + gb / 2, y3 + 0.1), g=22)
    s.speichern()


ALLE = [k16austritt, k16ladung, k16schwelle, k16zustaende, k16kennlinie, k16tief, k16auswertung, k16ccd]
if __name__ == "__main__":
    for f in ALLE:
        f()
    print("fertig", len(ALLE))
