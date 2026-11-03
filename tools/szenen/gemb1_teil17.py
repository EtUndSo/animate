"""GEMB 1 Teil 17 (kap17_stufen.tex): Der MOSFET.

Aufruf: python tools/szenen/gemb1_teil17.py, danach python tools/szenen_ansehen.py out.png gemb1/k17aufbau ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap17.py (dasselbe Rechenmodell).
"""
import re
import sys
from math import exp, log, pi, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#ddf0e4"

# ------------------------------------------------------------ Rechenmodell (wie rechnung_kap17.py)
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


def Nmass(m):
    return 2 * (2 * pi * m * m0 * 1.380649e-23 * T / h**2)**1.5


NI = sqrt(Nmass(1.08) * Nmass(0.81)) * exp(-EG / (2 * VT))
NA = 3e22
ND = 5e24
N0 = NI**2 / NA
DIS = 20e-9
CIS = EPSIS / DIS
GAMMA = sqrt(2 * EPS * e * NA) / CIS
PWI = VT * log(NA / NI)
PSI = 2 * PWI
QF = 11.2e-5                    # C/m^2: Q'_IS + Q'_SS wie Teil 16
PHIM = 4.10
VFB = PHIM - (4.05 + EG / 2 + PWI) - QF / CIS
VTH = VFB + PSI + GAMMA * sqrt(PSI)
VWI = VFB + PWI + GAMMA * sqrt(PWI)
MUN = 500e-4
WL = 10.0
K = MUN * CIS * WL
PHIBI = VT * log(NA * ND / NI**2)
E0 = VT * log(Nmass(1.08) / ND)  # E_C - E_F in der Source
SMIN = VT * log(10)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR, on=None):
    s.text(on, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit, key=None):
    key = key or "a_" + re.sub(r"\W", "", name + einheit)
    return s.tr(key, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def ID(VGS, VDS):
    ov = VGS - VTH
    if ov <= 0:
        return 0.0
    return K * (ov * VDS - VDS**2 / 2) if VDS < ov else K * ov**2 / 2


def phi_aus_VG(V):
    return (-GAMMA / 2 + sqrt(GAMMA**2 / 4 + V - VFB))**2


def Isub(phi):
    Es = sqrt(2 * e * NA * phi / EPS)
    return WL * e * VT * MUN * N0 * exp(phi / VT) * VT / Es


def schichtmodell(VGS, VDS, nst=500):
    """Drift und Diffusion, Verarmungsladung wächst zum Drain, wie rechnung_kap17.py."""
    def phi(V):
        a, b = 3 * VT, 12.0
        for _ in range(70):
            m = (a + b) / 2
            F = NA * (m - VT) + N0 * VT * exp(min((m - V) / VT, 600))
            if VGS - VFB - m - sqrt(2 * e * EPS * F) / CIS > 0:
                a = m
            else:
                b = m
        return m

    def Qinv(ph, V):
        A = NA * (ph - VT)
        B = N0 * VT * exp(min((ph - V) / VT, 600))
        return 2 * e * EPS * B / (sqrt(2 * e * EPS * (A + B)) + sqrt(2 * e * EPS * A))

    vs = [VDS * i / nst for i in range(nst + 1)]
    ps = [phi(v) for v in vs]
    qs = [Qinv(p, v) for p, v in zip(ps, vs)]
    I = sum(0.5 * (qs[i] + qs[i + 1]) * (ps[i + 1] - ps[i]) for i in range(nst))
    return MUN * WL * (I + VT * (qs[0] - qs[-1]))


def kl(s, x, y, name="", dx=0.0, dy=0.27, farbe=SCHWARZ):
    s.kreis(None, x, y, 0.07, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        t(s, name, (x + dx, y + dy), farbe=farbe)


# ------------------------------------------------------------------------------------------ Stufe 1
def k17aufbau():
    """Querschnitt des n-Kanal-MOSFET und Schaltzeichen."""
    s = Szene("gemb1/k17aufbau")
    s.welt()
    x0, x1, yo, yu = -3.6, 0.65, 0.35, -1.75
    xs, xd = -2.5, -0.45
    s.band(None, x0, x1, yu, yo, farbe=GRAU, deckung=0.2)
    s.band(None, x0, xs, yo - 0.62, yo, farbe=ORANGE, deckung=0.6)
    s.band(None, xd, x1, yo - 0.62, yo, farbe=ORANGE, deckung=0.6)
    s.band(None, xs, xd, yo - 0.09, yo, farbe=BLAU, deckung=0.9)
    s.band(None, xs, xd, yo, yo + 0.3, farbe=GRUEN, deckung=0.3)
    s.band(None, xs, xd, yo + 0.3, yo + 0.72, farbe=SCHWARZ, deckung=0.65)
    s.band(None, x0 + 0.25, xs - 0.2, yo, yo + 0.16, farbe=SCHWARZ, deckung=0.65)
    s.band(None, xd + 0.2, x1 - 0.25, yo, yo + 0.16, farbe=SCHWARZ, deckung=0.65)
    s.band(None, -1.7, -0.8, yu - 0.13, yu, farbe=SCHWARZ, deckung=0.65)
    # Anschlüsse
    xqs, xqd, xg = (x0 + xs) / 2 - 0.1, (xd + x1) / 2 + 0.1, (xs + xd) / 2
    s.linie(None, (xqs, yo + 0.16), (xqs, 1.5), dicke=3)
    s.linie(None, (xqd, yo + 0.16), (xqd, 1.5), dicke=3)
    s.linie(None, (xg, yo + 0.72), (xg, 1.5), dicke=3)
    s.linie(None, (-1.25, yu - 0.13), (-1.25, yu - 0.4), dicke=3)
    kl(s, xqs, 1.5, "S")
    kl(s, xqd, 1.5, "D")
    kl(s, xg, 1.5, "G")
    kl(s, -1.25, yu - 0.47, "B", dx=0.2, dy=0.0)
    t(s, "n^+", ((x0 + xs) / 2, yo - 0.34), g=26)
    t(s, "n^+", ((xd + x1) / 2, yo - 0.34), g=26)
    t(s, s.tr("psub", "p-Substrat", "p-type substrate", "sustrato p", "p 型衬底"), (-1.25, -1.05), g=26)
    s.text(None, "Gate", (xg, yo + 0.51), groesse=24, ausrichtung="center", farbe="#ffffff")
    t(s, s.tr("isol", "Isolator", "insulator", "aislante", "绝缘体"), (xg, yo + 0.15), g=22)
    t(s, s.tr("kanal", "Kanal", "channel", "canal", "沟道"), (xg, -0.1), farbe=BLAU, g=24)
    s.pfeil((xg + 0.42, -0.1), (xg + 0.7, yo - 0.09), "", farbe=BLAU, spitze=0.12, dicke=2.5)
    # Maße
    pf = dict(farbe=SCHWARZ, dicke=2.5, spitze=0.12, doppelt=True, on=None)
    s.pfeil((xs, -0.5), (xd, -0.5), "", **pf)
    t(s, "L", (xg, -0.68))
    s.linie(None, (xs, -0.6), (xs, yo - 0.09), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(None, (xd, -0.6), (xd, yo - 0.09), farbe=GRAU, dicke=1.5, dash=DOT)
    s.pfeil((xd + 0.09, yo), (xd + 0.09, yo + 0.3), "", farbe=SCHWARZ, dicke=2, spitze=0.09, doppelt=True)
    s.linie(None, (xd, yo + 0.3), (xd + 0.15, yo + 0.3), farbe=GRAU, dicke=1.5, dash=DOT)
    t(s, "d_{IS}", (xd + 0.1, yo + 0.46), a="left", g=22)
    # Koordinaten
    cx, cy = -3.25, -1.05
    s.pfeil((cx, cy), (cx + 0.55, cy), "", farbe=SCHWARZ, dicke=2.5, spitze=0.13)
    s.pfeil((cx, cy), (cx, cy - 0.55), "", farbe=SCHWARZ, dicke=2.5, spitze=0.13)
    s.kreis(None, cx, cy, 0.07, farbe=SCHWARZ, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    s.punkt(None, cx, cy, r=0.025)
    t(s, "y", (cx + 0.62, cy), a="left", g=22)
    t(s, "x", (cx + 0.13, cy - 0.5), a="left", g=22)
    t(s, "z", (cx - 0.13, cy + 0.16), g=22)
    # Schaltzeichen
    xc, yc, m = 1.98, 0.1, 0.68
    s.geraet("nmos4", (xc, yc), groesse=m)
    xG, xD, yD, yS, xB = xc - m, xc + 0.5 * m, yc + m, yc - m, xc + m
    s.draht((xB, yc), (xB + 0.25, yc), (xB + 0.25, yS - 0.25), (xD, yS - 0.25))
    s.draht((xD, yS), (xD, yS - 0.75))
    s.draht((xD, yD), (xD, yD + 0.45))
    s.draht((xG, yc), (xG - 0.55, yc))
    kl(s, xG - 0.55, yc, "G", dx=0.0, dy=0.25)
    kl(s, xD, yD + 0.45, "D", dx=0.22, dy=0.0)
    kl(s, xD, yS - 0.75, "S", dx=0.22, dy=0.0)
    t(s, "B", (xB + 0.42, yc), g=22)
    s.pfeil((xD, yD + 0.36), (xD, yD + 0.08), "", farbe=ROT, spitze=0.15, dicke=3)
    t(s, "I_D", (xD - 0.12, yD + 0.24), a="right", farbe=ROT)
    s.pfeil((xG - 0.55, yc - 0.18), (xD - 0.1, yS - 0.75), "", farbe=BLAU, spitze=0.15, dicke=2.5)
    t(s, "V_{GS}", (xG - 0.55, yS - 0.55), a="center", farbe=BLAU)
    s.pfeil((xB + 0.62, yD + 0.45), (xB + 0.62, yS - 0.75), "", farbe=BLAU, spitze=0.15, dicke=2.5)
    t(s, "V_{DS}", (xB + 0.55, yc + 0.6), a="right", farbe=BLAU, g=22)
    s.linie(None, (xD + 0.07, yD + 0.45), (xB + 0.62, yD + 0.45), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(None, (xD + 0.07, yS - 0.75), (xB + 0.62, yS - 0.75), farbe=GRAU, dicke=1.5, dash=DOT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k17barriere():
    """Leitungsbandkante längs der Oberfläche: Gate senkt die Barriere, Drain leert die Halbparabel mit k < 0."""
    s = Szene("gemb1/k17barriere")
    s.welt()
    ys = np.linspace(-0.3, 1.3, 241)

    def r(y):
        return 0.5 * (1 + np.tanh((y - 0.09) / 0.03))

    def q(y):
        return 0.5 * (1 + np.tanh((y - 0.91) / 0.03))

    def ec(phi):
        return E0 + (PHIBI - phi) * r(ys) * (1 - q(ys))

    def ecv(phi, V):
        b = PHIBI - phi
        li = np.clip((ys - 0.09) / 0.82, 0, 1)
        return E0 + b * r(ys) - 0.5 * V * li**1.6 - (b + 0.5 * V) * q(ys)

    def rahmen(a, drainabs=0.0):
        s.band(a, -0.3, 0.09, -1.3, 1.85, farbe=ORANGE, deckung=0.14)
        s.band(a, 0.91, 1.3, -1.3, 1.85, farbe=ORANGE, deckung=0.14)
        s.text(a, "Source", (-0.1, -1.18), groesse=22, ausrichtung="center")
        s.text(a, "Drain", (1.1, -1.18), groesse=22, ausrichtung="center")
        s.text(a, s.tr("kanal", "Kanal", "channel", "canal", "沟道"), (0.5, -1.18), groesse=22, ausrichtung="center", farbe=BLAU)

    def para(cx, ybar, fill_neg):
        """Kleine Parabel E(k) an der Spitze; rot von der Source besetzt (k>0), orange vom Drain (k<0)."""
        c = s.achsen((-1, 1), (0, 1.05), breite=1.0, hoehe=0.72, mitte=(cx, 1.92), unsichtbar=True)
        s.flaeche(c, "x*x", 0, sqrt(0.6), f2="0.6", farbe=ROT, deckung=0.75)
        if fill_neg > 0:
            s.flaeche(c, "x*x", -sqrt(fill_neg), 0, f2=str(fill_neg), farbe=ORANGE, deckung=0.85)
        s.kurve(c, "x*x", x=(-1, 1), farbe=GRUEN, dicke=3.5)
        s.linie(c, (-1.05, 0), (1.05, 0), farbe=GRAU, dicke=1.5)
        s.text(c, "-k", (-0.8, -0.2), groesse=22, ausrichtung="center", farbe=ORANGE)
        s.text(c, "+k", (0.8, -0.2), groesse=22, ausrichtung="center", farbe=ROT)

    # links: V_DS = 0
    a = s.achsen((-0.3, 1.3), (-1.3, 1.85), breite=2.85, hoehe=3.05, mitte=(-1.72, -0.55), yl=s.tr("a_e", "E-E_F in eV", "E-E_F in eV", "E-E_F en eV", "E-E_F / eV"),
                 xzahlen=False, xmarks=False, yticks="-1;-0.5;0;0.5;1;1.5")
    s.text(a, "V_{DS} = 0", (1.27, 1.55), groesse=24, ausrichtung="right")
    rahmen(a)
    p0 = phi_aus_VG(0.0)
    s.daten(a, list(zip(ys, ec(0.0))), farbe=GRAU, dicke=3.5)
    s.daten(a, list(zip(ys, ec(p0))), farbe=BLAU, dicke=3.5)
    s.daten(a, list(zip(ys, ec(PSI))), farbe=GRUEN, dicke=4.5)
    s.linie(a, (-0.3, 0), (1.3, 0), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(a, "E_F", (-0.27, -0.13), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "E_C", (-0.27, 0.17), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, "V_{GS} = V_{FB}", (0.5, PHIBI + E0 + 0.14), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "V_{GS} = 0", (0.5, PHIBI + E0 - p0 + 0.13), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "V_{GS} = V_{th}", (0.5, PHIBI + E0 - PSI + 0.115), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.linie(a, (0.5, 1.2), (0.5, 1.85), farbe=GRAU, dicke=1.5, dash=DOT)
    para(-1.72, 0, 0.6)
    # rechts: V_DS = 1 V
    V = 1.0
    b = s.achsen((-0.3, 1.3), (-1.3, 1.85), breite=2.85, hoehe=3.05, mitte=(1.82, -0.55), yl=s.tr("a_e", "E-E_F in eV", "E-E_F in eV", "E-E_F en eV", "E-E_F / eV"),
                 xzahlen=False, xmarks=False, yticks="-1;-0.5;0;0.5;1;1.5")
    s.text(b, "V_{DS} = 1 V", (1.27, 1.55), groesse=24, ausrichtung="right")
    rahmen(b)
    y2 = ecv(PSI, V)
    s.daten(b, list(zip(ys, y2)), farbe=GRUEN, dicke=4.5)
    s.linie(b, (-0.3, 0), (0.09, 0), farbe=ROT, dicke=2.5, dash=DASH)
    s.linie(b, (0.91, -V), (1.3, -V), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(b, "E_F", (-0.27, -0.13), groesse=22, ausrichtung="left", farbe=ROT)
    s.pfeil((1.2, 0), (1.2, -V), "", farbe=SCHWARZ, dicke=2.5, spitze=0.12, doppelt=True, on=b)
    s.linie(b, (0.09, 0), (1.25, 0), farbe=GRAU, dicke=1.5, dash=DOT)
    s.text(b, "eV_{DS}", (1.15, -0.52), groesse=22, ausrichtung="right", farbe=SCHWARZ)
    i = int(np.argmax(y2))
    ytop, etop = float(ys[i]), float(y2[i])
    s.punkt(b, ytop, etop, farbe=ROT, r=0.07)
    s.linie(b, (ytop, etop), (ytop + 0.2, 1.85), farbe=GRAU, dicke=1.5, dash=DOT)
    s.pfeil((-0.14, 0.5), (ytop - 0.03, 0.5), "", farbe=ROT, dicke=3, spitze=0.13, on=b)
    s.text(b, s.tr("diffu", "Diffusion", "diffusion", "difusión", "扩散"), (-0.12, 0.68), groesse=22, ausrichtung="left", farbe=ROT)
    s.pfeil((0.38, 0.18), (0.72, -0.14), "", farbe=BLAU, dicke=3, spitze=0.13, on=b)
    s.text(b, s.tr("drift", "Drift", "drift", "deriva", "漂移"), (0.62, 0.24), groesse=22, ausrichtung="left", farbe=BLAU)
    xk = 1.82 + (ytop + 0.2 - 0.5) / 1.6 * 2.85
    para(xk, 0, 0.06)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k17kanal():
    """V(y) und |Q'_inv(y)| bei V_GS = 3 V für drei Drainspannungen."""
    s = Szene("gemb1/k17kanal")
    s.welt()
    ov = 3 - VTH
    yy = np.linspace(0, 1, 201)

    def Vy(u, VDS):
        return ov - np.sqrt(np.maximum(ov**2 - 2 * u * (ov * VDS - VDS**2 / 2), 0))

    a = s.achsen((0, 1), (0, 3), breite=2.3, hoehe=2.4, mitte=(-2.1, 0.1), xl="y/L", yl=achse(s, "V(y)", "V"), xticks="0;0.5;1", yticks="0;1;2;3")
    b = s.achsen((0, 1), (0, 500), breite=2.3, hoehe=2.4, mitte=(1.6, 0.1), xl="y/L", yl=achse(s, "|Q'_{inv}|", "nC/cm^2", "a_q"), xticks="0;0.5;1", yticks="0;100;200;300;400;500")
    cq = CIS * 1e5
    for VDS, f in ((1.0, GRUEN), (2.0, BLAU), (ov, ROT)):
        v = Vy(yy, VDS)
        s.daten(a, list(zip(yy, v)), farbe=f, dicke=4)
        s.daten(b, list(zip(yy, cq * (ov - v))), farbe=f, dicke=4)
    s.linie(a, (0, 0), (1, ov), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (0, ov), (1, ov), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "V_{GS}-V_{th}", (0.03, ov + 0.17), groesse=22, ausrichtung="left", farbe=GRAU)
    s.text(a, "1 V", (1.03, 1.0), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, "2 V", (1.03, 2.0), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "2.68 V", (1.03, ov), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(b, "1 V", (1.03, cq * (ov - 1)), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(b, "2 V", (1.03, cq * (ov - 2)), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(b, "2.68 V", (1.03, 18), groesse=22, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def schnitt(s, cy, wert, titel_key, de, en, es, zh, xm=2.5):
    """Kleiner Querschnitt: Kanal als Keil, Dicke proportional zur Ladung."""
    a = s.achsen((-0.35, 1.35), (-0.55, 0.3), breite=2.0, hoehe=0.72, mitte=(xm, cy), unsichtbar=True)
    s.band(a, -0.35, 1.35, -0.55, 0, farbe=GRAU, deckung=0.2)
    s.band(a, -0.35, 0, -0.26, 0, farbe=ORANGE, deckung=0.6)
    s.band(a, 1, 1.35, -0.26, 0, farbe=ORANGE, deckung=0.6)
    s.band(a, 0, 1, 0, 0.09, farbe=GRUEN, deckung=0.35)
    s.band(a, 0, 1, 0.09, 0.26, farbe=SCHWARZ, deckung=0.65)
    h0 = 0.17
    ov = 3 - VTH
    if wert < ov:
        f = "-%g*sqrt(1-%g*x)" % (h0, (2 * (ov * wert - wert**2 / 2)) / ov**2)
        s.flaeche(a, f, 0, 1, f2="0", farbe=BLAU, deckung=0.85)
    else:
        xp = 0.86 if wert > ov else 1.0
        f = "-%g*sqrt(max(1-x/%g,0))" % (h0, xp)
        s.flaeche(a, f, 0, xp, f2="0", farbe=BLAU, deckung=0.85)
    s.text(a, s.tr(titel_key, de, en, es, zh), (0.5, 0.42), groesse=22, ausrichtung="center", farbe=SCHWARZ)


def k17ausgang():
    """Ausgangskennlinienfeld und Kanal in drei Fällen."""
    s = Szene("gemb1/k17ausgang")
    s.welt()
    a = s.achsen((0, 5), (0, 7), breite=4.0, hoehe=3.3, mitte=(-1.42, -0.05), xl=achse(s, "V_{DS}", "V"), yl=achse(s, "I_D", "mA"), xticks="0;1;2;3;4;5", yticks="0;2;4;6")
    ko = K * 1e3
    s.flaeche(a, "%g/2*x*x" % ko, 0, 3.81, f2="7", farbe=GRAU, deckung=0.13)
    s.kurve(a, "%g/2*x*x" % ko, x=(0, 3.81), farbe=ROT, dicke=2.5, dash=DOT)
    for VG in (1, 2, 3, 4):
        o = VG - VTH
        vs = np.linspace(0, o, 60)
        s.daten(a, [(v, ko * (o * v - v**2 / 2)) for v in vs] + [(5, ko * o**2 / 2)], farbe=BLAU, dicke=4.5)
        vg = np.linspace(o, min(1.5 * o, 5), 30)
        s.daten(a, [(v, ko * (o * v - v**2 / 2)) for v in vg], farbe=GRAU, dicke=2, dash=DASH)
        s.punkt(a, o, ko * o**2 / 2, farbe=ROT, r=0.06)
        s.text(a, "V_{GS} = %d V" % VG, (4.95, ko * o**2 / 2 + 0.3), groesse=22, ausrichtung="right", farbe=BLAU)
    s.linie(a, (0, 0), (3.2 / (ko * 2.677), 3.2), farbe=ROT, dicke=2)
    s.linie(a, (0, 0), (4.0 / (ko * 3.677), 4.0), farbe=ROT, dicke=2)
    s.text(a, s.tr("unges", "ungesättigt", "unsaturated", "no saturada", "非饱和"), (0.08, 6.45), groesse=22, ausrichtung="left")
    s.text(a, s.tr("satt", "Sättigung", "saturation", "saturación", "饱和"), (4.95, 6.72), groesse=22, ausrichtung="right")
    schnitt(s, 1.35, 1.0, "s1", "V_{DS} < V_{DS,sat}", "V_{DS} < V_{DS,sat}", "V_{DS} < V_{DS,sat}", "V_{DS} < V_{DS,sat}", xm=2.2)
    schnitt(s, 0.05, 2.677, "s2", "V_{DS} = V_{DS,sat}", "V_{DS} = V_{DS,sat}", "V_{DS} = V_{DS,sat}", "V_{DS} = V_{DS,sat}", xm=2.2)
    schnitt(s, -1.25, 5.0, "s3", "V_{DS} > V_{DS,sat}", "V_{DS} > V_{DS,sat}", "V_{DS} > V_{DS,sat}", "V_{DS} > V_{DS,sat}", xm=2.2)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k17schwelle():
    """Links Transferkennlinie mit den vier Zuständen, rechts V_th über der Dotierung."""
    s = Szene("gemb1/k17schwelle")
    s.welt()
    ko = K * 1e3
    a = s.achsen((-1.5, 3), (0, 3.6), breite=2.95, hoehe=2.5, mitte=(-1.98, 0.05), xl=achse(s, "V_{GS}", "V"), yl=achse(s, "I_{D,sat}", "mA"), xticks="-1;0;1;2;3", yticks="0;1;2;3")
    s.band(a, -1.5, VFB, 0, 3.6, farbe=GRAU, deckung=0.3)
    s.band(a, VFB, VWI, 0, 3.6, farbe=ORANGE, deckung=0.22)
    s.band(a, VWI, VTH, 0, 3.6, farbe=BLAU, deckung=0.13)
    s.band(a, VTH, 3, 0, 3.6, farbe=BLAU, deckung=0.3)
    xs = np.linspace(VTH, 3, 80)
    s.linie(a, (-1.5, 0), (VTH, 0), farbe=BLAU, dicke=4.5)
    s.daten(a, [(x, ko * (x - VTH)**2 / 2) for x in xs], farbe=BLAU, dicke=4.5)
    s.text(a, "V_{FB}", (VFB - 0.05, 3.2), groesse=22, ausrichtung="right")
    s.text(a, "V_{WI}", (VWI - 0.06, 2.75), groesse=22, ausrichtung="right")
    s.text(a, "V_{th}", (VTH + 0.08, 3.2), groesse=22, ausrichtung="left", farbe=ROT)
    s.linie(a, (VTH, 0), (VTH, 3.6), farbe=ROT, dicke=2.5)
    s.linie(a, (VFB, 0), (VFB, 3.6), farbe=SCHWARZ, dicke=2)
    s.linie(a, (VWI, 0), (VWI, 3.6), farbe=GRAU, dicke=2)
    b = s.achsen((1e15, 1e18), (-0.5, 3.5), breite=2.2, hoehe=2.5, mitte=(1.8, 0.05), xl=achse(s, "N_A", "cm^{-3}", "a_na"), yl=achse(s, "V_{th}", "V", "a_vth"), xlog=True, xticks="1e15;1e16;1e17;1e18", yticks="0;1;2;3")

    def vth(N, Pm):
        c = N * 1e6
        w = VT * log(c / NI)
        g = sqrt(2 * EPS * e * c) / CIS
        return Pm - (4.05 + EG / 2 + w) - QF / CIS + 2 * w + g * sqrt(2 * w)

    Ns = np.logspace(15, 18, 80)
    s.daten(b, [(n, vth(n, 4.10)) for n in Ns], farbe=BLAU, dicke=4)
    s.daten(b, [(n, vth(n, 5.10)) for n in Ns], farbe=GRUEN, dicke=4)
    s.linie(b, (1e15, 0), (1e18, 0), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(b, 3e16, VTH, farbe=ROT)
    s.text(b, "\u03a6_M = 4.1 eV", (2.4e16, -0.3), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(b, "\u03a6_M = 5.1 eV", (1.2e15, 1.5), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k17unterschwelle():
    """Kapazitiver Teiler und halblogarithmische Transferkennlinie."""
    s = Szene("gemb1/k17unterschwelle")
    s.welt()
    x0 = -2.75
    s.linie(None, (x0, 1.75), (x0, 1.2), dicke=3)
    kl(s, x0, 1.82, "V_{GS}", dx=0.0, dy=0.27)
    s.bauteil("capacitor", (x0, 0.75), drehung=270, laenge=0.9, label="C'_{IS}", font_size=24, size=0.7, label_flip=False)
    s.linie(None, (x0, 0.3), (x0, 0.05), dicke=3)
    s.punkt(None, x0, 0.05, farbe=ROT, r=0.08)
    t(s, "\u03c6_s", (x0 - 0.15, 0.05), a="right", farbe=ROT)
    s.linie(None, (x0, 0.05), (x0, -0.2), dicke=3)
    s.bauteil("capacitor", (x0, -0.65), drehung=270, laenge=0.9, label="C'_{depl}", font_size=24, size=0.7, label_flip=False)
    s.linie(None, (x0, -1.1), (x0, -1.3), dicke=3)
    s.geraet("ground", (x0, -1.3), groesse=0.5)
    a = s.achsen((-0.6, 2.0), (1e-13, 1e-2), breite=4.0, hoehe=3.2, mitte=(0.85, 0.05), xl=achse(s, "V_{GS}", "V"), yl=achse(s, "I_D", "A"), ylog=True,
                 xticks="-0.5;0;0.5;1;1.5;2", yticks="1e-12;1e-10;1e-8;1e-6;1e-4;1e-2", gitter=True)
    Vs = np.arange(-0.6, 2.001, 0.02)
    Is = [schichtmodell(float(v), 5.0) for v in Vs]
    s.daten(a, list(zip(Vs, Is)), farbe=BLAU, dicke=4.5)
    # Grenzformeln
    vv = np.arange(-0.6, VTH + 0.001, 0.02)
    s.daten(a, [(v, Isub(phi_aus_VG(float(v)))) for v in vv], farbe=ROT, dicke=2.5, dash=DASH)
    v2 = np.linspace(VTH + 0.04, 2.0, 50)
    s.daten(a, [(v, K * (v - VTH)**2 / 2) for v in v2], farbe=GRUEN, dicke=2.5, dash=DASH)
    s.linie(a, (VTH, 1e-13), (VTH, 1e-2), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "V_{th}", (VTH + 0.04, 3e-13), groesse=22, ausrichtung="left", farbe=GRAU)
    s.text(a, s.tr("expf", "Diffusionsformel", "diffusion formula", "fórmula de difusión", "扩散公式"), (0.42, 1.2e-10), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, s.tr("qform", "quadratisches Gesetz", "square law", "ley cuadrática", "平方律"), (1.95, 1.5e-6), groesse=22, ausrichtung="right", farbe=GRUEN)
    s.text(a, s.tr("num", "numerisch", "numerical", "numérico", "数值解"), (-0.05, 3e-7), groesse=22, ausrichtung="right", farbe=BLAU)
    # eine Dekade am Beispiel V_GS = 0
    v1, v2 = 0.0, 0.0
    i1 = schichtmodell(0.0, 5.0)
    i2 = 10 * i1
    a_, b_ = 0.0, 0.3
    for _ in range(40):
        m = (a_ + b_) / 2
        if schichtmodell(m, 5.0) < i2:
            a_ = m
        else:
            b_ = m
    v2 = m
    s.linie(a, (v1, i1), (v2, i1), farbe=SCHWARZ, dicke=2.5)
    s.linie(a, (v2, i1), (v2, i2), farbe=SCHWARZ, dicke=2.5)
    s.text(a, "S", ((v1 + v2) / 2 + 0.02, i1 / 7), groesse=22, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def fet(s, art, cx, cy, m=0.5):
    """Schaltzeichen; p-Kanal-Verarmung fehlt im Katalog und entsteht aus Linien in derselben Geometrie."""
    if art != "pdep":
        s.geraet(art, (cx, cy), groesse=m)
    else:
        P = lambda x, y: (cx + m * x, cy + m * y)
        s.linie(None, P(-1, 0), P(-0.35, 0), dicke=3)
        s.linie(None, P(-0.35, -0.45), P(-0.35, 0.45), dicke=5)
        s.linie(None, P(-0.2, -0.55), P(-0.2, 0.55), dicke=5)
        s.draht(P(-0.2, 0.4), P(0.5, 0.4), P(0.5, 1))
        s.draht(P(-0.2, -0.4), P(0.5, -0.4), P(0.5, -1))
        s.linie(None, P(-0.2, 0), P(1, 0), dicke=3)
        s.pfeil(P(-0.12, 0), P(0.35, 0), "", farbe=SCHWARZ, dicke=3, spitze=0.14)
    t(s, "G", (cx - m * 1.0, cy + 0.17), g=22)
    t(s, "D", (cx + m * 0.5 + 0.17, cy + m * 0.9), g=22)
    t(s, "S", (cx + m * 0.5 + 0.17, cy - m * 0.9), g=22)


def zelle(s, art, cx, cy, key, de, en, es, zh, vt, vz):
    t(s, s.tr(key, de, en, es, zh), (cx + 0.1, cy + 1.2), g=24)
    fet(s, art, cx - 1.0, cy - 0.05, 0.42)
    ax, ay, br = cx + 0.65, cy - 0.05, 1.5
    a = s.achsen((-2.3, 2.3), (-2.4, 2.4), breite=br, hoehe=1.75, mitte=(ax, ay), kreuz=True, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    xs = np.linspace(vt, vz * 2.2, 40)
    sg = 1 if vz > 0 else -1
    s.daten(a, [(x, sg * 0.55 * (x - vt)**2) for x in xs], farbe=BLAU, dicke=4)
    s.linie(a, (vt, 0), (-sg * 2.1, 0), farbe=BLAU, dicke=4)
    s.punkt(a, vt, 0, farbe=ROT, r=0.06)
    s.text(a, "V_{th}", (vt, -sg * 0.42), groesse=22, ausrichtung="center", farbe=ROT)
    t(s, "V_{GS}", (ax + br / 2 + 0.06, ay), a="left", g=22)
    t(s, "I_D", (ax + 0.1, ay + 0.8), a="left", g=22)


def k17typen():
    """Die vier Typen: Schaltzeichen und Transferkennlinie."""
    s = Szene("gemb1/k17typen")
    s.welt()
    zelle(s, "nmos4", -1.85, 1.3, "t1", "n-Kanal, Anreicherung", "n-channel, enhancement", "canal n, enriquecimiento", "n 沟道增强型", 0.9, 1)
    zelle(s, "nmos_dep", 1.8, 1.3, "t2", "n-Kanal, Verarmung", "n-channel, depletion", "canal n, vaciamiento", "n 沟道耗尽型", -0.9, 1)
    zelle(s, "pmos4", -1.85, -1.3, "t3", "p-Kanal, Anreicherung", "p-channel, enhancement", "canal p, enriquecimiento", "p 沟道增强型", -0.9, -1)
    zelle(s, "pdep", 1.8, -1.3, "t4", "p-Kanal, Verarmung", "p-channel, depletion", "canal p, vaciamiento", "p 沟道耗尽型", 0.9, -1)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k17inverter():
    """Source-Schaltung als Inverter: Schaltung und V_out(V_in)."""
    s = Szene("gemb1/k17inverter")
    s.welt()
    xc, yc, m = -2.4, -0.6, 0.62
    xD, yD, yS = xc + 0.5 * m, yc + m, yc - m
    xB = xc + m
    s.geraet("nmos4", (xc, yc), groesse=m)
    ym = 0.45
    s.draht((xD, yD), (xD, ym))
    s.bauteil("resistor", (xD, 1.05), drehung=270, laenge=1.2, label="", size=0.5)
    t(s, "R_D", (xD - 0.32, 1.05), a="right")
    s.linie(None, (xD, 1.65), (xD, 1.8), dicke=3)
    kl(s, xD, 1.87, "V_{DD}", dx=0.0, dy=0.27)
    s.draht((xD, ym), (xD + 1.0, ym))
    kl(s, xD + 1.07, ym)
    s.punkt(None, xD, ym, r=0.06)
    s.draht((xB, yc), (xB + 0.2, yc), (xB + 0.2, yS - 0.2), (xD, yS - 0.2))
    s.draht((xD, yS), (xD, yS - 0.5))
    s.punkt(None, xD, yS - 0.2, r=0.06)
    s.geraet("ground", (xD, yS - 0.5), groesse=0.45)
    s.draht((xc - m, yc), (xc - m - 0.3, yc))
    kl(s, xc - m - 0.37, yc)
    s.pfeil((xc - m - 0.37, yc - 0.13), (xc - m - 0.37, yS - 0.42), "", farbe=BLAU, spitze=0.15, dicke=2.5)
    t(s, "V_{in}", (xc - m - 0.28, yS - 0.05), a="left", farbe=BLAU, g=22)
    s.pfeil((xD + 1.07, ym - 0.13), (xD + 1.07, yS - 0.42), "", farbe=BLAU, spitze=0.15, dicke=2.5)
    t(s, "V_{out}", (xD + 0.98, -0.3), a="right", farbe=BLAU, g=22)
    t(s, "I_D", (xD + 0.13, 0.15), a="left", farbe=ROT, g=22)
    s.pfeil((xD, 0.32), (xD, 0.02), "", farbe=ROT, spitze=0.15, dicke=3)
    a = s.achsen((0, 5), (0, 5), breite=3.2, hoehe=2.8, mitte=(1.8, 0.1), xl=achse(s, "V_{in}", "V"), yl=achse(s, "V_{out}", "V"), xticks="0;1;2;3;4;5", yticks="0;1;2;3;4;5", gitter=True)

    def vout(Vin, VDD=5.0, RD=5e3):
        a_, b_ = 0.0, VDD
        for _ in range(70):
            m_ = (a_ + b_) / 2
            if (VDD - m_) / RD - ID(Vin, m_) > 0:
                a_ = m_
            else:
                b_ = m_
        return m_

    xs = np.linspace(0, 5, 251)
    s.daten(a, [(float(x), vout(float(x))) for x in xs], farbe=BLAU, dicke=4.5)
    s.linie(a, (VTH, 0), (VTH, 5), farbe=ROT, dicke=2, dash=DOT)
    s.text(a, "V_{th}", (VTH + 0.1, 0.3), groesse=22, ausrichtung="left", farbe=ROT)
    s.punkt(a, 1.631, 1.308, farbe=ROT, r=0.07)
    s.text(a, s.tr("satt2", "Sättigung", "saturation", "saturación", "饱和"), (1.75, 3.2), groesse=22, ausrichtung="left")
    s.text(a, s.tr("unges2", "ungesättigt", "unsaturated", "no saturada", "非饱和"), (2.3, 1.1), groesse=22, ausrichtung="left")
    s.speichern()


if __name__ == "__main__":
    for f in (k17aufbau, k17barriere, k17kanal, k17ausgang, k17schwelle, k17unterschwelle, k17typen, k17inverter):
        f()
    print("gemb1 Teil 17: Szenen geschrieben")
