"""GEMB 1 Teil 15 (kap15_stufen.tex): Die MOS-Kapazität.

Aufruf: python tools/szenen/gemb1_teil15.py, danach python tools/szenen_ansehen.py out.png gemb1/k15aufbau ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap15.py (dasselbe Rechenmodell).
"""
import sys
from math import exp, log, pi, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN, HELLGRAU2 = "#f6dede", "#dceafa", "#ddf0e4", "#ececec"

# ------------------------------------------------------------ Rechenmodell (wie rechnung_kap15.py)
e = 1.602176634e-19
h = 6.62607015e-34
hq = h / (2 * pi)
m0 = 9.1093837e-31
kB = 1.380649e-23 / e
eps0 = 8.8541878e-12
T = 300.0
VT = kB * T
EG = 1.12
EPS = eps0 * 11.7
EPSIS = eps0 * 3.9
NC, NV = 2.816e25, 1.829e25
NI = sqrt(NC * NV) * exp(-EG / (2 * VT))
NA = 3e22
DIS = 20e-9
CIS = EPSIS / DIS
GAMMA = sqrt(2 * EPS * e * NA) / CIS
PWI = VT * log(NA / NI)
PSI = 2 * PWI
N0 = NI**2 / NA
LD = sqrt(EPS * VT / (e * NA))
VTH = PSI + GAMMA * sqrt(PSI)
VWI = PWI + GAMMA * sqrt(PWI)
A0 = hq**2 * pi**2 / (2 * m0 * 1e-18) / e      # eV nm^2
D0 = m0 / (pi * hq**2) * e * 1e-4              # 1/(eV cm^2)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR, on=None):
    s.text(on, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit, key=None):
    return s.tr(key or ("a_" + name + einheit), name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def xlab(s):
    return achse(s, "x", "nm", "a_xnm")


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


def VG(phi):
    return phi - Qex(phi) / CIS


def phi_aus_V(V):
    a, b = -0.4, 1.3
    for _ in range(200):
        m = (a + b) / 2
        if VG(m) < V:
            a = m
        else:
            b = m
    return m


def profil(phis, xmax=400e-9):
    """Exakter Verlauf phi(x) im Halbleiter: x(phi) aus dphi/dx = -sign*sqrt(2eF/eps). Rückgabe x (nm), phi (V)."""
    ts = np.arange(0, 16, 0.01)
    ph = phis * np.exp(-ts)
    xs = [0.0]
    for a, b in zip(ph[:-1], ph[1:]):
        m = 0.5 * (a + b)
        xs.append(xs[-1] + abs(a - b) / sqrt(2 * e / EPS * F(m)))
    x = np.array(xs)
    k = np.searchsorted(x, xmax)
    return x[:k] * 1e9, ph[:k]


def phi_von(x, phis):
    xp, pp = profil(phis)
    return np.interp(x, xp, pp, right=0.0)


# ------------------------------------------------------------------------------------------ Stufe 1
def k15aufbau():
    """Energieniveaus des idealen MIS-Kondensators im Rechenmodell, Flachbandfall."""
    s = Szene("gemb1/k15aufbau")
    sc, y0 = 0.52, -1.3

    def y(E):
        return y0 + sc * E

    xm0, xm1, xi1, xs1 = -3.5, -1.75, -0.75, 2.45
    s.band(None, xm0, xm1, y(-0.9), y(0), farbe=BLAU, deckung=0.22)
    s.band(None, xm1, xi1, y(-0.9), y(4.1), farbe=GRAU, deckung=0.22)
    s.linie(None, (xm1, y(-0.9)), (xm1, y(4.1)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xi1, y(-0.9)), (xi1, y(4.1)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm1, y(4.1)), (xi1, y(4.1)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm0, y(5.0)), (xs1, y(5.0)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm0, y(0)), (xs1, y(0)), farbe=ROT, dicke=3, dash=DASH)
    s.linie(None, (xi1, y(0.949)), (xs1, y(0.949)), farbe=GRUEN, dicke=4)
    s.linie(None, (xi1, y(0.389)), (xs1, y(0.389)), farbe=GRUEN, dicke=2.5, dash=DOT)
    s.linie(None, (xi1, y(-0.171)), (xs1, y(-0.171)), farbe=GRUEN, dicke=4)
    t(s, s.tr("met", "Metall", "metal", "metal", "金属"), ((xm0 + xm1) / 2, y(5.0) + 0.27))
    t(s, s.tr("iso", "Isolator", "insulator", "aislante", "绝缘体"), ((xm1 + xi1) / 2, y(5.0) + 0.27))
    t(s, s.tr("hl", "p-Silizium", "p-type silicon", "silicio p", "p 型硅"), ((xi1 + xs1) / 2, y(5.0) + 0.27))
    t(s, "E_{vac}", (xs1 + 0.1, y(5.0)), a="left")
    t(s, "E_C", (xs1 + 0.1, y(0.949)), a="left", farbe=GRUEN)
    t(s, "E_{Fi}", (xs1 + 0.1, y(0.389) + 0.03), a="left", farbe=GRUEN)
    t(s, "E_F", (xs1 + 0.1, y(0) + 0.03), a="left", farbe=ROT)
    t(s, "E_V", (xs1 + 0.1, y(-0.171) - 0.17), a="left", farbe=GRUEN)
    t(s, "E_{C,IS}", (xm1 + 0.5, y(4.1) - 0.24))
    # Abstände
    pf = dict(farbe=SCHWARZ, dicke=2.5, spitze=0.12, doppelt=True, on=None)
    s.pfeil((-3.05, y(5.0)), (-3.05, y(0)), "", **pf)
    t(s, "\u03a6_M", (-2.95, y(2.9)), a="left")
    t(s, "5.00 eV", (-2.95, y(2.2)), a="left", g=22)
    s.pfeil((-1.98, y(4.1)), (-1.98, y(0)), "", **pf)
    s.linie(None, (-2.15, y(4.1)), (xm1, y(4.1)), farbe=GRAU, dicke=2, dash=DOT)
    t(s, "\u03a6_B", (-2.08, y(1.3)), a="right")
    t(s, "4.10 eV", (-2.08, y(0.6)), a="right", g=22)
    s.pfeil((-1.0, y(5.0)), (-1.0, y(4.1)), "", **pf)
    t(s, "\u03c7_{IS}", (-1.09, y(4.55)), a="right")
    s.pfeil((-0.45, y(5.0)), (-0.45, y(0.949)), "", **pf)
    t(s, "\u03c7_{SC}", (-0.35, y(3.0)), a="left")
    t(s, "4.05 eV", (-0.35, y(2.3)), a="left", g=22)
    s.pfeil((1.0, y(5.0)), (1.0, y(0)), "", **pf)
    t(s, "\u03a6_{SC}", (1.1, y(3.0)), a="left")
    t(s, "5.00 eV", (1.1, y(2.3)), a="left", g=22)
    s.pfeil((0.45, y(0.949)), (0.45, y(-0.171)), "", **pf)
    t(s, "E_g", (0.37, y(1.32)), a="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k15teilung():
    """Bänderdiagramm über die ganze Struktur bei V_G = 0,6 V und Ladungen."""
    s = Szene("gemb1/k15teilung")
    s.welt()
    V = 0.6
    ph = (-GAMMA / 2 + sqrt(GAMMA**2 / 4 + V))**2
    VI = V - ph
    sc, y0 = 0.56, -1.15

    def y(E):
        return y0 + sc * E

    xm0, xm1, xi1, xs1 = -3.7, -2.95, -2.2, 0.55
    xnm = np.linspace(0, 200, 121)
    pp = (e * NA / (2 * EPS)) * np.clip(sqrt(2 * EPS * ph / (e * NA)) - xnm * 1e-9, 0, None)**2
    xw = xi1 + xnm / 200 * (xs1 - xi1)
    s.band(None, xm0, xm1, y(-1.0), y(-V), farbe=BLAU, deckung=0.22)
    s.linie(None, (xm0, y(-V)), (xm1, y(-V)), farbe=ROT, dicke=3)
    s.linie(None, (xm1, y(-1.0)), (xm1, y(4.1 - V)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xi1, y(-1.0)), (xi1, y(4.1 - ph)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm0, y(5 - V)), (xm1, y(5 - V)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm1, y(5 - V)), (xi1, y(5 - ph)), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xm1, y(4.1 - V)), (xi1, y(4.1 - ph)), farbe=SCHWARZ, dicke=3)
    s.daten(None, list(zip(xw, y(5 - pp))), farbe=SCHWARZ, dicke=3)
    s.daten(None, list(zip(xw, y(0.949 - pp))), farbe=GRUEN, dicke=4)
    s.daten(None, list(zip(xw, y(0.389 - pp))), farbe=GRUEN, dicke=2.5, dash=DOT)
    s.daten(None, list(zip(xw, y(-0.171 - pp))), farbe=GRUEN, dicke=4)
    s.linie(None, (xi1, y(0)), (xs1, y(0)), farbe=ROT, dicke=3, dash=DASH)
    # Hilfslinien und Abstände
    s.linie(None, (xm0, y(0)), (xi1, y(0)), farbe=ROT, dicke=1.8, dash=DOT)
    pf = dict(farbe=SCHWARZ, dicke=2.5, spitze=0.08, doppelt=True, on=None)
    s.pfeil((-3.05, y(0)), (-3.05, y(-V)), "", **pf)
    t(s, "eV_G", (-3.13, y(-0.3)), a="right", g=22)
    s.linie(None, (xm1, y(5 - ph)), (xi1, y(5 - ph)), farbe=GRAU, dicke=2, dash=DOT)
    s.pfeil((xm1, y(5 - ph)), (xm1, y(5 - V)), "", **pf)
    t(s, "eV_{IS}", (xm1 - 0.08, y(5 - 0.45) + 0.04), a="right", g=22)
    s.linie(None, (xi1, y(5)), (xs1, y(5)), farbe=GRAU, dicke=2, dash=DOT)
    s.pfeil((xi1 + 0.14, y(5)), (xi1 + 0.14, y(5 - ph)), "", **pf)
    t(s, "e\u03c6_s", (xi1 + 0.26, y(5 + 0.3)), a="left", g=22)
    t(s, "E_{vac}", (xs1 + 0.08, y(5)), a="left")
    t(s, "E_C", (xs1 + 0.08, y(0.949)), a="left", farbe=GRUEN)
    t(s, "E_{Fi}", (xs1 + 0.08, y(0.389) + 0.05), a="left", farbe=GRUEN)
    t(s, "E_F", (xs1 + 0.08, y(0) + 0.03), a="left", farbe=ROT)
    t(s, "E_V", (xs1 + 0.08, y(-0.171) - 0.17), a="left", farbe=GRUEN)
    t(s, "E_{F,M}", (-3.33, y(-V) - 0.2), farbe=ROT, a="center", g=22)
    t(s, "E_{C,IS}", ((xm1 + xi1) / 2 + 0.05, y(4.1 - 0.45) - 0.28), g=22)
    t(s, s.tr("met", "Metall", "metal", "metal", "金属"), ((xm0 + xm1) / 2 - 0.05, y(5) + 0.42), g=22)
    t(s, s.tr("iso", "Isolator", "insulator", "aislante", "绝缘体"), ((xm1 + xi1) / 2, y(5) + 0.42), g=22)
    t(s, s.tr("hl", "p-Silizium", "p-type silicon", "silicio p", "p 型硅"), ((xi1 + xs1) / 2 + 0.1, y(5) + 0.42), g=22)
    # Ladungen
    a = s.achsen((-60, 220), (-1.25, 1.25), breite=1.7, hoehe=2.3, mitte=(2.4, 0.1), xl=xlab(s), yl=s.tr("rho", "Ladung", "charge", "carga", "电荷"),
                 yzahlen=False, ymarks=False, xticks="0;100;200", kreuz=False)
    s.band(a, -20, 0, -1.25, 1.25, farbe=GRAU, deckung=0.22)
    s.band(a, -34, -20, 0, 1.2, farbe=ROT, deckung=0.75)
    s.band(a, 0, 1e9 * sqrt(2 * EPS * ph / (e * NA)), -0.5, 0, farbe=BLAU, deckung=0.55)
    s.linie(a, (-60, 0), (220, 0), farbe=GRAU, dicke=2)
    s.text(a, "Q'_M", (20, 0.85), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, "Q'_{SC}", (60, -0.85), groesse=22, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k15debye():
    """Links abklingender Überschuss, rechts L_D über der Dotierung."""
    s = Szene("gemb1/k15debye")
    s.welt()
    a = s.achsen((0, 100), (0, 1.05), breite=2.7, hoehe=2.3, mitte=(-1.95, 0.05), xl=xlab(s), yl=s.tr("dpn", "\u0394p(x) / \u0394p(0)", "\u0394p(x) / \u0394p(0)", "\u0394p(x) / \u0394p(0)", "\u0394p(x) / \u0394p(0)"),
                 xticks="0;50;100", yticks="0;0.5;1")
    ld = LD * 1e9
    s.kurve(a, "exp(-x/%.4f)" % ld, farbe=BLAU)
    s.linie(a, (0, 1), (ld, 0), farbe=GRAU, dicke=2.5, dash=DASH)
    s.linie(a, (ld, 0), (ld, exp(-1)), farbe=ROT, dicke=2, dash=DOT)
    s.punkt(a, ld, exp(-1), farbe=ROT)
    s.text(a, "L_D = 23.6 nm", (ld + 5, 0.46), groesse=22, ausrichtung="left", farbe=ROT)
    b = s.achsen((1e14, 1e19), (1, 1000), breite=2.2, hoehe=2.3, mitte=(1.9, 0.05), xl=achse(s, "N", "cm^{-3}", "a_n"), yl=achse(s, "L_D", "nm", "a_ld"), xlog=True, ylog=True,
                 xticks="1e14;1e16;1e18", yticks="1;10;100;1000")
    pts = [(10**u, sqrt(EPS * VT / (e * 1e6 * 10**u)) * 1e9) for u in np.linspace(14, 19, 41)]
    s.daten(b, pts, farbe=BLAU, dicke=4)
    for N in (1e14, 1e16, 1e18):
        s.punkt(b, N, sqrt(EPS * VT / (e * 1e6 * N)) * 1e9, farbe=BLAU)
    s.punkt(b, 3e16, ld, farbe=ROT, r=0.1)
    s.text(b, "409 nm", (2e14, 700), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(b, "41 nm", (2e16, 90), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(b, "4.1 nm", (1.8e17, 2.2), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k15verarmung():
    """Kastenprofil: rho, Feld, Potential bei phi_s = 0,3 V; grau der exakte Verlauf."""
    s = Szene("gemb1/k15verarmung")
    s.welt()
    ph = 0.3
    L = sqrt(2 * EPS * ph / (e * NA)) * 1e9
    x = np.linspace(0, 170, 171)
    xp, pp = profil(ph)
    pv = np.interp(x, xp, pp, right=0.0)
    gem = dict(breite=1.5, hoehe=2.2, xl=xlab(s), xticks="0;100")
    a = s.achsen((0, 170), (-1.15, 0.1), mitte=(-2.32, 0.05), yl="\u03c1 / (eN_A)", yticks="-1;0", **gem)
    s.daten(a, [(u, -(1 - exp(-v / VT))) for u, v in zip(x, pv)], farbe=GRAU, dicke=3)
    s.daten(a, [(0, -1), (L, -1), (L, 0), (170, 0)], farbe=BLAU, dicke=4)
    b = s.achsen((0, 170), (0, 6.5), mitte=(0.0, 0.05), yl=achse(s, "\u2130", "MV/m", "a_feld"), yticks="0;2;4;6", **gem)
    Ef = 2 * ph / (L * 1e-9) / 1e6
    fe = np.gradient(pv, x * 1e-9) * (-1e-6)
    s.daten(b, list(zip(x[1:], fe[1:])), farbe=GRAU, dicke=3)
    s.daten(b, [(0, Ef), (L, 0), (170, 0)], farbe=BLAU, dicke=4)
    s.text(b, "5.3", (16, 5.75), groesse=22, ausrichtung="left", farbe=BLAU)
    c = s.achsen((0, 170), (0, 0.34), mitte=(2.32, 0.05), yl=achse(s, "\u03c6", "V", "a_phi"), yticks="0;0.1;0.2;0.3", **gem)
    s.daten(c, list(zip(x, pv)), farbe=GRAU, dicke=3)
    s.daten(c, [(u, ph * (1 - min(u, L) / L)**2) for u in x], farbe=BLAU, dicke=4)
    s.linie(a, (L, -1.15), (L, 0.1), farbe=ROT, dicke=2, dash=DOT)
    s.linie(b, (L, 0), (L, 6.5), farbe=ROT, dicke=2, dash=DOT)
    s.linie(c, (L, 0), (L, 0.34), farbe=ROT, dicke=2, dash=DOT)
    s.text(a, "L_{depl}", (L + 3, -0.55), groesse=22, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k15bereiche():
    """Vier Bereiche: Bandkanten im Halbleiter, exakte Verläufe."""
    s = Szene("gemb1/k15bereiche")
    s.welt()
    fall = [("ak", "Akkumulation", "accumulation", "acumulación", "积累", -0.15, -1.95, 1.3, True, True),
            ("ve", "Verarmung", "depletion", "vaciamiento", "耗尽", 0.25, 1.6, 1.3, False, True),
            ("sw", "schwache Inversion", "weak inversion", "inversión débil", "弱反型", 0.58, -1.95, -1.15, True, False),
            ("st", "starke Inversion", "strong inversion", "inversión fuerte", "强反型", 0.86, 1.6, -1.15, False, False)]
    xmax = 150
    for key, de, en, es, zh, ph, mx, my, links, oben in fall:
        a = s.achsen((0, xmax), (-0.6, 1.25), breite=2.75, hoehe=1.7, mitte=(mx, my), xl="" if oben else xlab(s), yl=achse(s, "E-E_F", "eV") if (links and oben) else "",
                     xticks="0;50;100;150", yticks="0;1", label=24, zahl=22)
        s.text(a, s.tr("t" + key, de, en, es, zh), (146, 1.15), groesse=24, ausrichtung="right")
        xp, pp = profil(ph)
        xf = np.unique(np.concatenate(([0.0], np.geomspace(0.05, xmax, 90))))     # feine Stützstellen an der Grenzfläche
        pv = np.interp(xf, xp, pp, right=0.0)
        s.daten(a, list(zip(xf, 0.949 - pv)), farbe=GRUEN, dicke=4)
        s.daten(a, list(zip(xf, 0.389 - pv)), farbe=GRUEN, dicke=2.5, dash=DOT)
        s.daten(a, list(zip(xf, -0.171 - pv)), farbe=GRUEN, dicke=4)
        s.linie(a, (0, 0), (xmax, 0), farbe=ROT, dicke=3, dash=DASH)
        if ph > 0:
            Ld = sqrt(2 * EPS * min(ph, PSI) / (e * NA)) * 1e9
            s.band(a, 0, min(Ld, xmax), -0.6, 1.25, farbe=ORANGE, deckung=0.10)
        s.text(a, "E_C", (xmax - 4, 0.78), groesse=22, ausrichtung="right", farbe=GRUEN)
        s.text(a, "E_{Fi}", (xmax - 4, 0.5), groesse=22, ausrichtung="right", farbe=GRUEN)
        s.text(a, "E_F", (xmax - 4, 0.12), groesse=22, ausrichtung="right", farbe=ROT)
        s.text(a, "E_V", (xmax - 4, -0.38), groesse=22, ausrichtung="right", farbe=GRUEN)
        def kante(u):
            return float(np.interp(u, xp, pp, right=0.0))
        if key == "ak":
            for i in range(6):
                for j in range(2):
                    u = 0.6 + 2.2 * i
                    s.punkt(a, u, -0.171 - kante(u) - 0.07 - 0.09 * j, farbe=ROT, r=0.04)
        if key == "st":
            for i in range(4):
                for j in range(3):
                    u = 0.5 + 1.8 * i
                    s.punkt(a, u, 0.949 - kante(u) + 0.07 + 0.09 * j, farbe=BLAU, r=0.04)
        if key == "sw":
            for i in range(3):
                u = 1.0 + 3.0 * i
                s.punkt(a, u, 0.949 - kante(u) + 0.07, farbe=BLAU, r=0.04)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k15schwelle():
    """Links phi_s(V_G), rechts Ladungen über V_G; exakte Lösung."""
    s = Szene("gemb1/k15schwelle")
    s.welt()
    Vs = np.arange(-1.0, 3.001, 0.02)
    Pp = [phi_aus_V(float(v)) for v in Vs]
    a = s.achsen((-1, 3), (-0.2, 1.1), breite=2.55, hoehe=2.1, mitte=(-2.05, 0.1), xl=achse(s, "V_G", "V"), yl=achse(s, "\u03c6_s", "V", "a_phis"), xticks="-1;0;1;2;3", yticks="0;0.4;0.8")
    s.daten(a, list(zip(Vs, Pp)), farbe=BLAU, dicke=4)
    s.linie(a, (-1, PSI), (3, PSI), farbe=ROT, dicke=2, dash=DASH)
    s.linie(a, (-1, PWI), (3, PWI), farbe=GRUEN, dicke=2, dash=DASH)
    s.linie(a, (VTH, -0.2), (VTH, PSI), farbe=ROT, dicke=2, dash=DOT)
    s.linie(a, (VWI, -0.2), (VWI, PWI), farbe=GRUEN, dicke=2, dash=DOT)
    s.punkt(a, VTH, PSI, farbe=ROT)
    s.punkt(a, VWI, PWI, farbe=GRUEN)
    s.text(a, "\u03c6_{s,SI}", (-0.92, PSI + 0.1), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "\u03c6_{s,WI}", (-0.92, PWI + 0.1), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, "V_{th}", (VTH + 0.08, -0.1), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "V_{WI}", (VWI - 0.07, -0.1), groesse=22, ausrichtung="right", farbe=GRUEN)
    b = s.achsen((0, 3), (0, 300), breite=2.4, hoehe=2.1, mitte=(1.95, 0.1), xl=achse(s, "V_G", "V"), yl=achse(s, "|Q'|", "nC/cm^2", "a_q"), xticks="0;1;2;3", yticks="0;100;200;300")
    Vp = Vs[Vs >= 0.02]
    Qg, Qd, Qi = [], [], []
    for v in Vp:
        p = phi_aus_V(float(v))
        q = abs(Qex(p)) * 1e5
        d = sqrt(2 * EPS * e * NA * max(p, 0)) * 1e5
        Qg.append(q)
        Qd.append(min(d, q))
        Qi.append(max(q - d, 0))
    s.daten(b, list(zip(Vp, Qg)), farbe=SCHWARZ, dicke=4)
    s.daten(b, list(zip(Vp, Qd)), farbe=ORANGE, dicke=4)
    s.daten(b, list(zip(Vp, Qi)), farbe=BLAU, dicke=4)
    s.linie(b, (VTH, 0), (3, CIS * (3 - VTH) * 1e5), farbe=GRAU, dicke=2.5, dash=DASH)
    s.linie(b, (VTH, 0), (VTH, 300), farbe=ROT, dicke=2, dash=DOT)
    s.text(b, s.tr("qge", "gesamt", "total", "total", "总电荷"), (2.2, 262), groesse=22, ausrichtung="right", farbe=SCHWARZ)
    s.text(b, s.tr("qde", "Verarmung", "depletion", "vaciamiento", "耗尽"), (0.1, 122), groesse=22, ausrichtung="left", farbe=ORANGE)
    s.text(b, s.tr("qin", "Inversion", "inversion", "inversión", "反型"), (2.95, 20), groesse=22, ausrichtung="right", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k15topf():
    """Links Kasten als Näherung des Topfs an der Grenzfläche, rechts Stufen der Zustandsdichte."""
    s = Szene("gemb1/k15topf")
    s.welt()
    Lx = 5.0
    Eh = [A0 / 0.92 / Lx**2 * n**2 * 1000 for n in (1, 2, 3)]
    El = [A0 / 0.19 / Lx**2 * n**2 * 1000 for n in (1,)]
    a = s.achsen((-3, 14), (0, 240), breite=2.95, hoehe=2.25, mitte=(-1.85, 0.05), xl=xlab(s), yl=s.tr("emec", "E-E_{C,0} in meV", "E-E_{C,0} in meV", "E-E_{C,0} en meV", "E-E_{C,0} / meV"), xticks="0;5;10", yticks="0;100;200")
    s.band(a, -3, 0, 0, 240, farbe=GRAU, deckung=0.3)
    s.band(a, 0, Lx, 0, 240, farbe=BLAU, deckung=0.06)
    s.text(a, "SiO_2", (-1.5, 222), groesse=22, ausrichtung="center")
    # Wirklicher Verlauf von E_C bei V_G = V_th + 1 V, klassisch gerechnet
    ph = phi_aus_V(VTH + 1.0)
    xp, pp = profil(ph)
    xs = np.linspace(0, 14, 71)
    pv = np.interp(xs, xp, pp)
    s.daten(a, [(u, (ph - v) * 1000) for u, v in zip(xs, pv)], farbe=GRAU, dicke=3)
    s.daten(a, [(0, 240), (0, 0), (Lx, 0), (Lx, 240)], farbe=GRUEN, dicke=4)
    for k, E in enumerate(Eh):
        if E < 240:
            s.linie(a, (0, E), (Lx, E), farbe=BLAU, dicke=3)
    for E in El:
        s.linie(a, (0, E), (Lx, E), farbe=ORANGE, dicke=3)
    s.text(a, "L_x", (Lx / 2, 214), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.text(a, "E_1^h", (Lx + 0.25, Eh[0] + 6), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "E_2^h", (Lx + 0.25, Eh[1] - 16), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "E_3^h", (Lx + 0.25, Eh[2]), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "E_1^l", (Lx + 0.25, El[0] + 12), groesse=22, ausrichtung="left", farbe=ORANGE)
    Dh, Dl = 2 * 0.19 * D0 / 1e14, 4 * sqrt(0.92 * 0.19) * D0 / 1e14
    b = s.achsen((0, 12), (0, 240), breite=1.85, hoehe=2.25, mitte=(2.1, 0.05), xl=achse(s, "D_s", "10^{14}/(eV cm^2)", "a_ds"), yl="", xticks="0;5;10", yticks="0;100;200", yzahlen=True)
    st = sorted([(E, Dh) for E in Eh] + [(E, Dl) for E in El] + [(4 * El[0], Dl)])
    pts, d, E0 = [], 0.0, 0.0
    for E, dd in st:
        if E > 240:
            break
        pts += [(d, E0), (d, E)]
        d += dd
        E0 = E
    pts.append((d, E0))
    pts.append((d, 240))
    s.daten(b, pts, farbe=BLAU, dicke=4)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k15kapazitaet():
    """Ersatzschaltbild und C'_ges/C'_IS über phi_s."""
    s = Szene("gemb1/k15kapazitaet")
    s.welt()
    x0 = -2.4
    s.geraet("terminal", (x0, 1.5), drehung=0, label="", groesse=0.6)
    t(s, "V_G", (x0 + 0.2, 1.55), a="left")
    s.bauteil("capacitor", (x0, 1.0), drehung=270, laenge=1.0, label="C'_{IS}", font_size=24, size=0.7, label_flip=False)
    s.draht((x0, 0.5), (x0, 0.3))
    s.draht((x0 - 0.55, 0.3), (x0 + 0.55, 0.3))
    s.punkt(None, x0, 0.3, farbe=SCHWARZ, r=0.06)
    t(s, "\u03c6_s", (x0 + 0.13, 0.5), a="left")
    s.bauteil("capacitor", (x0 - 0.55, -0.25), drehung=270, laenge=1.1, label="C'_{depl}", font_size=24, size=0.7, label_flip=True)
    s.bauteil("capacitor", (x0 + 0.55, -0.25), drehung=270, laenge=1.1, label="C'_{inv/acc}", font_size=24, size=0.7, label_flip=False)
    s.draht((x0 - 0.55, -0.8), (x0 + 0.55, -0.8))
    s.draht((x0, -0.8), (x0, -1.0))
    s.geraet("ground", (x0, -1.15), drehung=0, label="", groesse=0.6)
    a = s.achsen((-0.2, 0.9), (0, 1.05), breite=3.1, hoehe=2.3, mitte=(1.6, 0.1), xl=achse(s, "\u03c6_s", "V", "a_phis"), yl="C'_{ges} / C'_{IS}", xticks="-0.2;0;0.2;0.4;0.6;0.8", yticks="0;0.5;1")
    ps = [i / 1000 for i in range(-200, 901, 5)]
    r = []
    for p in ps:
        c = CSC(p)
        r.append((p, c / (CIS + c)))
    s.daten(a, r, farbe=BLAU, dicke=4)
    dep = [(i / 1000, (lambda c: c / (CIS + c))(EPS / sqrt(2 * EPS * i / 1000 / (e * NA)))) for i in range(30, 901, 10)]
    s.daten(a, dep, farbe=GRAU, dicke=2.5, dash=DASH)
    s.linie(a, (-0.2, 1), (0.9, 1), farbe=GRAU, dicke=2, dash=DOT)
    s.linie(a, (PWI, 0), (PWI, 1.05), farbe=GRUEN, dicke=2, dash=DOT)
    s.linie(a, (PSI, 0), (PSI, 1.05), farbe=ROT, dicke=2, dash=DOT)
    s.linie(a, (0, 0), (0, 1.05), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "\u03c6_{s,WI}", (PWI + 0.015, 0.1), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, "\u03c6_{s,SI}", (PSI - 0.015, 0.1), groesse=22, ausrichtung="right", farbe=ROT)
    s.punkt(a, 0, sqrt(e * EPS * (NA + N0) / VT) / (CIS + sqrt(e * EPS * (NA + N0) / VT)), farbe=BLAU)
    s.text(a, s.tr("kflach", "Flachband: 0.72", "flat band: 0.72", "banda plana: 0.72", "平带：0.72"), (0.03, 0.8), groesse=22, ausrichtung="left", farbe=SCHWARZ)
    s.speichern()


ALLE = [k15aufbau, k15teilung, k15debye, k15verarmung, k15bereiche, k15schwelle, k15topf, k15kapazitaet]
if __name__ == "__main__":
    for f in ALLE:
        f()
    print("fertig", len(ALLE))
