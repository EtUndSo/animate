"""GEMB 1 Teil 14 (kap14_stufen.tex): Der p-n-Übergang.

Aufruf: python tools/szenen/gemb1_teil14.py, danach python tools/szenen_ansehen.py out.png gemb1/k14baender ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap14.py.
"""
import re
import sys
from math import exp, log, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
QE = 1.602176634e-19
KB = 8.617333e-5
EPS = 8.8541878e-12 * 11.7
T0 = 300.0
KT = KB * T0
EG, NC, NV = 1.12, 2.82e19, 1.83e19
NI = sqrt(NC * NV) * exp(-EG / (2 * KT))
NA, ND = 5e16, 1e16
VD = KT * log(NA * ND / NI**2)
DN, DP = KT * 925, KT * 419
LN, LP = sqrt(DN * 1e-6) * 1e4, sqrt(DP * 1e-6) * 1e4      # um
PN0, NP0 = NI**2 / ND, NI**2 / NA
ECF, EFV = KT * log(NC / ND), KT * log(NV / NA)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    key = "a_" + re.sub(r"\W", "", name + einheit)
    return s.tr(key, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def feld_l(s):
    return s.tr("feld_l", "ℰ in MV/m", "ℰ in MV/m", "ℰ en MV/m", "ℰ / (MV/m)")


def rhoe_l(s):
    return s.tr("rhoe_l", "\\rho/e in 10^{16}\\,cm^{-3}", "\\rho/e in 10^{16}\\,cm^{-3}", "\\rho/e en 10^{16}\\,cm^{-3}", "\\rho/e / 10^{16}\\,cm^{-3}")


def dichte_l(s):
    return s.tr("dichte_l", "Dichte in cm^{-3}", "density in cm^{-3}", "densidad en cm^{-3}", "密度 / cm^{-3}")


def ring(s, on, x, y, r=0.075, farbe=ROT):
    return s._add("Dot", {"center": [x, y, 0], "radius": r, "color": farbe, "fill_color": "#ffffff", "fill_opacity": 1, "stroke_width": 2.5}, on)


def weiten(V):
    """L^A, L^D in nm bei der Spannung V über der Zone."""
    na, nd = NA * 1e6, ND * 1e6
    return (sqrt(2 * EPS * V / QE * nd / (na * (na + nd))) * 1e9, sqrt(2 * EPS * V / QE * na / (nd * (na + nd))) * 1e9)


def bieg(x, V):
    """Bandverbiegung Phi(x) in eV, bezogen auf die n-Seite. x in nm, V = Barriere in eV."""
    la, ld = weiten(V)
    if x <= -la:
        return V
    if x >= ld:
        return 0.0
    if x >= 0:
        return (ld - x)**2 * 1e-18 * QE * ND * 1e6 / (2 * EPS)
    return V - (la + x)**2 * 1e-18 * QE * NA * 1e6 / (2 * EPS)


def xachse(a, b, n=240):
    return [float(v) for v in np.linspace(a, b, n)]


# ------------------------------------------------------------------------------------------ Stufe 1
def k14baender():
    """Vorgegebene Ladung: Schicht 200 nm mit N = 1e16 und Gegenladung an der Oberfläche; Feld und Bänder im selben Maßstab."""
    s = Szene("gemb1/k14baender")
    s.welt()
    w, x0 = 4.5, 0.15
    D = 200.0
    a = s.achsen((0, 400), (-2, 2), breite=w, hoehe=0.85, mitte=(x0, 2.15), xl="", yl=s.tr("rho_l", "\\rho in 10^3\\,C/m^3", "\\rho in 10^3\\,C/m^3", "\\rho en 10^3\\,C/m^3", "\\rho / 10^3\\,C/m^3"), xticks="0;100;200;300;400", xzahlen=False, yticks="-1.6;0;1.6")
    s.band(a, 0, D, -2, 2, farbe=GRAU, deckung=0.12)
    s.linie(a, (0, 0), (400, 0), farbe=GRAU, dicke=1.5)
    s.daten(a, [(0, 1.602), (D, 1.602), (D, 0), (400, 0)], farbe=BLAU, dicke=4.5)
    s.pfeil((0.0, 0), (0.0, -1.9), "", farbe=ROT, dicke=4, spitze=0.13, on=a)
    s.text(a, "-Q'", (22, -1.2), groesse=GR, ausrichtung="left", farbe=ROT)
    s.text(a, "+Q'", (100, 0.72), groesse=GR, ausrichtung="center", farbe=BLAU)
    b = s.achsen((0, 400), (-3.6, 0.6), breite=w, hoehe=0.85, mitte=(x0, 0.7), xl="", yl=feld_l(s), xticks="0;100;200;300;400", xzahlen=False, yticks="-3;0")
    s.band(b, 0, D, -3.6, 0.6, farbe=GRAU, deckung=0.12)
    s.linie(b, (0, 0), (400, 0), farbe=GRAU, dicke=1.5)
    s.daten(b, [(0, -3.093), (D, 0), (400, 0)], farbe=GRUEN, dicke=4.5)
    s.text(b, "-3.09", (52, -2.9), groesse=22, ausrichtung="left", farbe=GRUEN)
    c = s.achsen((0, 400), (-1.05, 0.65), breite=w, hoehe=1.65, mitte=(x0, -1.15), xl=achse(s, "x", "nm"), yl=achse(s, "E-E_F", "eV"), xticks="0;100;200;300;400", yticks="-1;-0.5;0;0.5")
    s.band(c, 0, D, -1.05, 0.65, farbe=GRAU, deckung=0.12)
    phi = lambda x: 0.309 * (1 - x / D)**2 if x < D else 0.0
    xs = xachse(0, 400, 120)
    s.daten(c, [(x, ECF + phi(x)) for x in xs], farbe=SCHWARZ, dicke=4.5)
    s.daten(c, [(x, ECF - EG + phi(x)) for x in xs], farbe=SCHWARZ, dicke=4.5)
    s.linie(c, (0, 0), (400, 0), farbe=ORANGE, dicke=3, dash=DASH)
    s.text(c, "E_C", (415, ECF), groesse=GR, ausrichtung="left")
    s.text(c, "E_V", (415, ECF - EG), groesse=GR, ausrichtung="left")
    s.text(c, "E_F", (415, 0), groesse=GR, ausrichtung="left", farbe=ORANGE)
    # Elektron rollt bergab, Loch steigt
    xe = 70.0
    s.punkt(c, xe, ECF + phi(xe) + 0.07, farbe=BLAU, r=0.085)
    s.pfeil((xe + 16, ECF + phi(xe) + 0.1), (xe + 70, ECF + phi(xe + 70) + 0.1), "", farbe=BLAU, dicke=3, spitze=0.13, on=c)
    xh = 130.0
    ring(s, c, xh, ECF - EG + phi(xh) - 0.08)
    s.pfeil((xh - 16, ECF - EG + phi(xh) - 0.13), (xh - 72, ECF - EG + phi(xh - 72) - 0.13), "", farbe=ROT, dicke=3, spitze=0.13, on=c)
    s.text(c, s.tr("rollt", "Elektron rollt bergab", "electron rolls downhill", "el electrón baja", "电子向下滚"), (205, 0.46), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(c, s.tr("steigt", "Loch steigt auf", "hole rises", "el hueco sube", "空穴上浮"), (205, -0.72), groesse=22, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k14kontakt():
    """Links die getrennten Stücke mit eigener Fermi-Energie, rechts der Übergang mit gemeinsamer Fermi-Energie."""
    s = Szene("gemb1/k14kontakt")
    s.welt()
    y0, yh = -0.1, 2.7            # Mitte, Höhe
    a = s.achsen((0, 2.1), (-0.2, 1.3), breite=2.1, hoehe=yh, mitte=(-2.2, y0), xl="", yl=achse(s, "E-E_V", "eV"), xzahlen=False, xmarks=False, yticks="0;0.5;1")
    t(s, s.tr("getrennt", "getrennt", "separate", "separados", "分离"), (-2.2, 1.95))
    for x1, x2 in ((0, 0.95), (1.15, 2.1)):
        s.linie(a, (x1, EG), (x2, EG), dicke=4.5)
        s.linie(a, (x1, 0), (x2, 0), dicke=4.5)
    Ep, En = EFV, EG - ECF
    s.linie(a, (0, Ep), (0.95, Ep), farbe=ORANGE, dicke=3.5, dash=DASH)
    s.linie(a, (1.15, En), (2.1, En), farbe=ORANGE, dicke=3.5, dash=DASH)
    s.text(a, "E_{Fp}", (0.47, Ep + 0.11), groesse=GR, ausrichtung="center", farbe=ORANGE)
    s.text(a, "E_{Fn}", (1.62, En - 0.12), groesse=GR, ausrichtung="center", farbe=ORANGE)
    s.text(a, s.tr("pstueck", "p-Stück", "p piece", "pieza p", "p 型块"), (0.47, 0.72), groesse=22, ausrichtung="center")
    s.text(a, s.tr("nstueck", "n-Stück", "n piece", "pieza n", "n 型块"), (1.62, 0.42), groesse=22, ausrichtung="center")
    s.text(a, "E_C", (2.13, EG), groesse=GR, ausrichtung="left")
    s.text(a, "E_V", (2.13, 0), groesse=GR, ausrichtung="left")
    s.linie(a, (0.95, Ep), (1.15, Ep), farbe=ROT, dicke=1.5, dash=DOT)
    s.linie(a, (0.95, En), (1.15, En), farbe=ROT, dicke=1.5, dash=DOT)
    s.pfeil((1.05, Ep), (1.05, En), "", farbe=ROT, dicke=3, spitze=0.13, on=a, doppelt=True)
    s.text(a, "\\Phi_{bi}", (1.05, 1.0), groesse=GR, ausrichtung="center", farbe=ROT)
    # rechts: Übergang
    la, ld = weiten(VD)
    b = s.achsen((-250, 550), (-1.05, 1.15), breite=2.9, hoehe=yh, mitte=(1.8, y0), xl=achse(s, "x", "nm"), yl=achse(s, "E-E_F", "eV"), xticks="-200;0;200;400", yticks="-1;-0.5;0;0.5;1")
    t(s, s.tr("verbunden", "verbunden, Gleichgewicht", "joined, equilibrium", "unidos, equilibrio", "接触，平衡"), (1.8, 1.95))
    s.band(b, -la, ld, -1.05, 1.15, farbe=GRAU, deckung=0.13)
    xs = xachse(-250, 550, 200)
    s.daten(b, [(x, ECF + bieg(x, VD)) for x in xs], farbe=SCHWARZ, dicke=4.5)
    s.daten(b, [(x, ECF - EG + bieg(x, VD)) for x in xs], farbe=SCHWARZ, dicke=4.5)
    s.linie(b, (-250, 0), (550, 0), farbe=ORANGE, dicke=3.5, dash=DASH)
    s.text(b, "E_F", (440, 0.09), groesse=GR, ausrichtung="center", farbe=ORANGE)
    s.linie(b, (-250, ECF + VD), (540, ECF + VD), farbe=ROT, dicke=1.5, dash=DOT)
    s.pfeil((470, ECF), (470, ECF + VD), "", farbe=ROT, dicke=3, spitze=0.13, on=b, doppelt=True)
    s.text(b, "\\Phi_{bi}", (395, 0.6), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b, "E_C", (-160, 0.84), groesse=GR, ausrichtung="center")
    s.text(b, "E_V", (-160, -0.32), groesse=GR, ausrichtung="center")
    s.text(b, s.tr("rlz", "Zone", "zone", "zona", "耗尽区"), (130, -0.97), groesse=22, ausrichtung="center", farbe=GRAU)
    for x in (-42, -14):
        s.text(b, "-", (x, 1.06), groesse=26, ausrichtung="center", farbe=ROT)
    for x in (40, 100, 160, 220):
        s.text(b, "+", (x, 1.06), groesse=24, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def poisson(xa=-0.4e-6, xb=0.7e-6, nx=2201):
    x = np.linspace(xa, xb, nx)
    h = x[1] - x[0]
    na, nd, nii = NA * 1e6, ND * 1e6, NI * 1e6
    dop = np.where(x < 0, -na, nd)
    psi = np.where(x < 0, -log(na / nii), log(nd / nii)).astype(float)
    c = QE / (EPS * KT)
    for _ in range(200):
        n = nii * np.exp(psi)
        p = nii * np.exp(-psi)
        f = np.zeros(nx)
        f[1:-1] = (psi[2:] - 2 * psi[1:-1] + psi[:-2]) / h**2 + c * (p[1:-1] - n[1:-1] + dop[1:-1])
        dia = np.full(nx, 1.0)
        dia[1:-1] = -2 / h**2 - c * (p[1:-1] + n[1:-1])
        up, lo = np.zeros(nx - 1), np.zeros(nx - 1)
        up[1:] = 1 / h**2
        lo[:-1] = 1 / h**2
        cp, dp = np.zeros(nx), np.zeros(nx)
        cp[0] = up[0] / dia[0]
        dp[0] = -f[0] / dia[0]
        for i in range(1, nx):
            m = dia[i] - lo[i - 1] * cp[i - 1]
            cp[i] = (up[i] / m) if i < nx - 1 else 0.0
            dp[i] = (-f[i] - lo[i - 1] * dp[i - 1]) / m
        d = np.zeros(nx)
        d[-1] = dp[-1]
        for i in range(nx - 2, -1, -1):
            d[i] = dp[i] - cp[i] * d[i + 1]
        d = np.clip(d, -2, 2)
        psi = psi + d
        if np.max(np.abs(d)) < 1e-10:
            break
    return x * 1e9, nii * np.exp(psi) * 1e-6, nii * np.exp(-psi) * 1e-6, (nii * np.exp(-psi) - nii * np.exp(psi) + dop) * 1e-6


def k14schottky():
    """Vollständige Lösung der Gleichungen gegen die Kastenform."""
    s = Szene("gemb1/k14schottky")
    s.welt()
    x, n, p, r = poisson()
    la, ld = weiten(VD)
    xr = (-200, 500)
    idx = [i for i in range(0, len(x), 6)]
    a = s.achsen(xr, (1e2, 1e18), breite=5.0, hoehe=1.55, mitte=(0.25, 1.3), xl="", yl=dichte_l(s), ylog=True, yticks="1e2;1e6;1e10;1e14;1e18", xticks="-200;-100;0;100;200;300;400;500", xzahlen=False)
    s.band(a, -la, ld, 1e2, 1e18, farbe=GRAU, deckung=0.12)
    s.daten(a, [(float(x[i]), float(n[i])) for i in idx if xr[0] <= x[i] <= xr[1]], farbe=BLAU, dicke=4.5)
    s.daten(a, [(float(x[i]), float(p[i])) for i in idx if xr[0] <= x[i] <= xr[1]], farbe=ROT, dicke=4.5)
    s.linie(a, (xr[0], NI), (xr[1], NI), farbe=GRAU, dicke=2, dash=DOT)
    s.text(a, "n_i", (-170, 2.5e11), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "n", (450, 2.5e14), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "n", (-140, 2e4), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "p", (-140, 3e15), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, "p", (450, 2.5e5), groesse=GR, ausrichtung="center", farbe=ROT)
    b = s.achsen(xr, (-6, 2), breite=5.0, hoehe=1.55, mitte=(0.25, -0.85), xl=achse(s, "x", "nm"), yl=rhoe_l(s), xticks="-200;-100;0;100;200;300;400;500", yticks="-5;-2.5;0;1")
    s.band(b, -la, ld, -6, 2, farbe=GRAU, deckung=0.12)
    s.linie(b, (xr[0], 0), (xr[1], 0), farbe=GRAU, dicke=1.5)
    s.daten(b, [(float(x[i]), float(r[i]) / 1e16) for i in range(0, len(x), 2) if xr[0] <= x[i] <= xr[1]], farbe=BLAU, dicke=4.5)
    s.daten(b, [(xr[0], 0), (-la, 0), (-la, -5), (0, -5), (0, 1), (ld, 1), (ld, 0), (xr[1], 0)], farbe=ROT, dicke=3, dash=DASH)
    s.text(b, s.tr("voll", "vollständige Lösung", "full solution", "solución completa", "完整解"), (150, -3.0), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(b, s.tr("kasten", "Schottky-Näherung", "Schottky approximation", "aproximación de Schottky", "肖特基近似"), (150, -4.3), groesse=22, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k14verlauf():
    """Rho, Feld, Potential und Bänder des Rechenmodells untereinander, Schottky-Näherung."""
    s = Szene("gemb1/k14verlauf")
    s.welt()
    la, ld = weiten(VD)
    xr = (-150, 400)
    w, x0 = 4.75, 0.05
    tk = "-100;0;100;200;300;400"
    ys = (2.55, 1.17, -0.21, -1.94)
    a = s.achsen(xr, (-6, 2), breite=w, hoehe=0.8, mitte=(x0, ys[0]), xl="", yl=rhoe_l(s), xticks=tk, xzahlen=False, yticks="-5;0")
    s.band(a, -la, ld, -6, 2, farbe=GRAU, deckung=0.12)
    s.linie(a, (xr[0], 0), (xr[1], 0), farbe=GRAU, dicke=1.5)
    s.daten(a, [(xr[0], 0), (-la, 0), (-la, -5), (0, -5), (0, 1), (ld, 1), (ld, 0), (xr[1], 0)], farbe=BLAU, dicke=4.5)
    s.text(a, "-N_A", (-100, -4.2), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "+N_D", (150, -1.6), groesse=22, ausrichtung="center", farbe=BLAU)
    s.pfeil((0, -3.9), (ld, -3.9), "", farbe=GRAU, dicke=2.5, spitze=0.11, on=a, doppelt=True)
    s.text(a, "287 nm", (150, -5.1), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "57 nm", (-66, 1.1), groesse=22, ausrichtung="right", farbe=GRAU)
    Em = 4.432
    b = s.achsen(xr, (-5.2, 0.8), breite=w, hoehe=0.8, mitte=(x0, ys[1]), xl="", yl=feld_l(s), xticks=tk, xzahlen=False, yticks="-4;-2;0")
    s.band(b, -la, ld, -5.2, 0.8, farbe=GRAU, deckung=0.12)
    s.linie(b, (xr[0], 0), (xr[1], 0), farbe=GRAU, dicke=1.5)
    s.daten(b, [(xr[0], 0), (-la, 0), (0, -Em), (ld, 0), (xr[1], 0)], farbe=GRUEN, dicke=4.5)
    s.text(b, "-4.43", (14, -4.5), groesse=22, ausrichtung="left", farbe=GRUEN)
    c = s.achsen(xr, (-0.1, 0.9), breite=w, hoehe=0.8, mitte=(x0, ys[2]), xl="", yl=s.tr("phi_l", "\\varphi in V", "\\varphi in V", "\\varphi en V", "\\varphi / V"), xticks=tk, xzahlen=False, yticks="0;0.4;0.8")
    s.band(c, -la, ld, -0.1, 0.9, farbe=GRAU, deckung=0.12)
    xs = xachse(*xr, 200)
    s.daten(c, [(x, VD - bieg(x, VD)) for x in xs], farbe=ORANGE, dicke=4.5)
    s.text(c, "U_d = 0.762\\,V", (240, 0.42), groesse=22, ausrichtung="left", farbe=ORANGE)
    d = s.achsen(xr, (-1.05, 1.15), breite=w, hoehe=1.5, mitte=(x0, ys[3]), xl=achse(s, "x", "nm"), yl=achse(s, "E-E_F", "eV"), xticks=tk, yticks="-1;0;1")
    s.band(d, -la, ld, -1.05, 1.15, farbe=GRAU, deckung=0.12)
    s.daten(d, [(x, ECF + bieg(x, VD)) for x in xs], farbe=SCHWARZ, dicke=4.5)
    s.daten(d, [(x, ECF - EG + bieg(x, VD)) for x in xs], farbe=SCHWARZ, dicke=4.5)
    s.linie(d, (xr[0], 0), (xr[1], 0), farbe=ORANGE, dicke=3, dash=DASH)
    s.text(d, "E_C", (412, ECF), groesse=GR, ausrichtung="left")
    s.text(d, "E_V", (412, ECF - EG), groesse=GR, ausrichtung="left")
    s.text(d, "E_F", (412, 0), groesse=GR, ausrichtung="left", farbe=ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def bandfeld(s, xm, V, links=False):
    Vb = VD - V
    la, ld = weiten(Vb)
    xr = (-260, 520)
    a = s.achsen(xr, (-1.1, 1.75), breite=1.9, hoehe=2.75, mitte=(xm, -0.1), xl=achse(s, "x", "nm"), yl=achse(s, "E-E_{Fn}", "eV") if links else "", xticks="0;400", yticks="-1;0;1" if links else "", yzahlen=links, ymarks=links)
    s.band(a, -la, ld, -1.1, 1.75, farbe=GRAU, deckung=0.12)
    xs = xachse(*xr, 160)
    s.daten(a, [(x, ECF + bieg(x, Vb)) for x in xs], farbe=SCHWARZ, dicke=4)
    s.daten(a, [(x, ECF - EG + bieg(x, Vb)) for x in xs], farbe=SCHWARZ, dicke=4)
    if V:
        s.linie(a, (-la, 0), (xr[1], 0), farbe=BLAU, dicke=3.5, dash=DASH)
        s.linie(a, (xr[0], -V), (ld, -V), farbe=ROT, dicke=3.5, dash=DASH)
    else:
        s.linie(a, (xr[0], 0), (xr[1], 0), farbe=ORANGE, dicke=3.5, dash=DASH)
    xp = 440
    s.linie(a, (-120, ECF + Vb), (xp + 30, ECF + Vb), farbe=GRAU, dicke=1.5, dash=DOT)
    s.pfeil((xp, ECF), (xp, ECF + Vb), "", farbe=ORANGE, dicke=2.8, spitze=0.12, on=a, doppelt=True)
    return a


def k14spannung():
    """Bänder bei V_pn = +0,4 V, 0 und -0,4 V: gleiche Achse, n-Seite festgehalten."""
    s = Szene("gemb1/k14spannung")
    s.welt()
    xa, xb, xc = -2.2, 0.05, 2.3
    a = bandfeld(s, xa, 0.4, True)
    b = bandfeld(s, xb, 0.0)
    c = bandfeld(s, xc, -0.4)
    yt = 1.95
    t(s, s.tr("durch", "Durchlass, +0.4 V", "forward, +0.4 V", "directa, +0.4 V", "正向，+0.4 V"), (xa, yt), g=22)
    t(s, s.tr("gg", "Gleichgewicht", "equilibrium", "equilibrio", "平衡"), (xb, yt), g=22)
    t(s, s.tr("sperr", "Sperrung, -0.4 V", "reverse, -0.4 V", "inversa, -0.4 V", "反向，-0.4 V"), (xc, yt), g=22)
    s.text(a, "0.36", (400, 0.42), groesse=22, ausrichtung="right", farbe=ORANGE)
    s.text(b, "0.76", (400, 0.62), groesse=22, ausrichtung="right", farbe=ORANGE)
    s.text(c, "1.16", (400, 0.8), groesse=22, ausrichtung="right", farbe=ORANGE)
    s.text(a, "E_{Fn}", (510, 0.11), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(a, "E_{Fp}", (-245, -0.29), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(b, "E_F", (510, 0.11), groesse=22, ausrichtung="right", farbe=ORANGE)
    s.text(c, "E_{Fn}", (510, -0.12), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(c, "E_{Fp}", (-245, 0.52), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "E_C", (-245, 0.68), groesse=22, ausrichtung="left")
    s.text(a, "E_V", (-245, -0.68), groesse=22, ausrichtung="left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def inj_spalte(s, xm, V, links):
    L1, L2 = LN, LP
    xr = (-120, 120)
    fa = exp(V / KT) - 1
    a = s.achsen(xr, (-1.05, 1.25), breite=2.85, hoehe=1.25, mitte=(xm, 1.55), xl="", yl=achse(s, "E-E_{Fn}", "eV") if links else "", xticks="-100;0;100", xzahlen=False, yticks="-1;0;1" if links else "", yzahlen=links, ymarks=links)
    xp = [float(v) for v in np.linspace(-120, 0, 120)]
    xn = [float(v) for v in np.linspace(0, 120, 120)]
    ec = lambda x: ECF + (VD - V if x < 0 else 0.0)
    pts = [(x, ec(x)) for x in xp] + [(x, ec(x)) for x in xn]
    s.daten(a, pts, farbe=SCHWARZ, dicke=3.5)
    s.daten(a, [(x, y - EG) for x, y in pts], farbe=SCHWARZ, dicke=3.5)
    Efp = -V
    s.daten(a, [(x, Efp) for x in xp] + [(x, -KT * log(1 + fa * exp(-x / L2))) for x in xn], farbe=ROT, dicke=3.5, dash=DASH)
    s.daten(a, [(x, Efp + KT * log(1 + fa * exp(x / L1))) for x in xp] + [(x, 0.0) for x in xn], farbe=BLAU, dicke=3.5, dash=DASH)
    b = s.achsen(xr, (1e-1, 1e18), breite=2.85, hoehe=1.6, mitte=(xm, -0.5), xl=achse(s, "x", "µm"), yl=dichte_l(s) if links else "", ylog=True, xticks="-100;0;100", yticks="1;1e4;1e8;1e12;1e16" if links else "", yzahlen=links, ymarks=links)
    s.daten(b, [(x, NP0 * (1 + fa * exp(x / L1))) for x in xp], farbe=BLAU, dicke=4.5)
    s.daten(b, [(x, PN0 * (1 + fa * exp(-x / L2))) for x in xn], farbe=ROT, dicke=4.5)
    s.linie(b, (xr[0], NP0), (0, NP0), farbe=BLAU, dicke=1.8, dash=DOT)
    s.linie(b, (0, PN0), (xr[1], PN0), farbe=ROT, dicke=1.8, dash=DOT)
    s.linie(b, (xr[0], NA), (0, NA), farbe=ROT, dicke=4.5)
    s.linie(b, (0, ND), (xr[1], ND), farbe=BLAU, dicke=4.5)
    s.linie(b, (0, 1e-1), (0, 1e18), farbe=GRAU, dicke=2)
    s.linie(a, (0, -1.05), (0, 1.25), farbe=GRAU, dicke=1.5)
    return a, b


def k14injektion():
    """Quasi-Fermi-Niveaus und Dichten bei +0,5 V und -0,2 V, Maßstab Mikrometer."""
    s = Szene("gemb1/k14injektion")
    s.welt()
    xa, xb = -1.45, 1.75
    a1, b1 = inj_spalte(s, xa, 0.5, True)
    a2, b2 = inj_spalte(s, xb, -0.2, False)
    t(s, s.tr("d05", "Durchlass, +0.5 V", "forward, +0.5 V", "directa, +0.5 V", "正向，+0.5 V"), (xa, 2.95), g=22)
    t(s, s.tr("s02", "Sperrung, -0.2 V", "reverse, -0.2 V", "inversa, -0.2 V", "反向，-0.2 V"), (xb, 2.95), g=22)
    s.text(a1, "E_{Fn}", (100, -0.24), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a1, "E_{Fp}", (-100, -0.3), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a1, "E_C", (-100, 0.68), groesse=22, ausrichtung="center")
    s.text(a1, "E_V", (100, -0.72), groesse=22, ausrichtung="center")
    s.text(a2, "E_{Fn}", (80, 0.48), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a2, "E_{Fp}", (-80, 0.42), groesse=22, ausrichtung="center", farbe=ROT)
    s.linie(a2, (80, 0.3), (80, 0.03), farbe=GRAU, dicke=1)
    s.text(b1, "p", (-100, 2e13), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b1, "n", (100, 3e13), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b1, "n_p", (-60, 2e7), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b1, "p_n", (60, 1e8), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b2, "n_p", (-72, 15), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b2, "p_n", (72, 1e2), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b2, "p", (-100, 2e13), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b2, "n", (100, 3e13), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k14strom():
    """Anteile am Gesamtstrom über dem Ort: Die Summe ist überall gleich."""
    s = Szene("gemb1/k14strom")
    s.welt()
    jn = (DN * NP0 / LN) / (DN * NP0 / LN + DP * PN0 / LP)
    jp = 1 - jn
    xr = (-150, 150)
    a = s.achsen(xr, (0, 1.2), breite=5.1, hoehe=1.75, mitte=(0.2, 0.05), xl=achse(s, "x", "µm"), yl=s.tr("anteil_j", "Anteil an j", "share of j", "fracción de j", "占 j 的比例"), xticks="-150;-100;-50;0;50;100;150", yticks="0;0.25;0.5;0.75;1")
    xp = [float(v) for v in np.linspace(-150, 0, 100)]
    xn = [float(v) for v in np.linspace(0, 150, 100)]
    s.daten(a, [(x, jn * exp(x / LN)) for x in xp] + [(x, 1 - jp * exp(-x / LP)) for x in xn], farbe=BLAU, dicke=4.5)
    s.daten(a, [(x, 1 - jn * exp(x / LN)) for x in xp] + [(x, jp * exp(-x / LP)) for x in xn], farbe=ROT, dicke=4.5)
    s.linie(a, (-150, 1), (150, 1), farbe=SCHWARZ, dicke=3.5, dash=DASH)
    s.linie(a, (0, 0), (0, 1.2), farbe=GRAU, dicke=2)
    s.text(a, "j_n + j_p = j", (45, 1.1), groesse=GR, ausrichtung="center")
    s.text(a, "j_p", (-105, 0.86), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, "j_n", (-105, 0.2), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "j_n", (105, 0.86), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "j_p", (105, 0.17), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("pseite", "p-Gebiet", "p region", "región p", "p 区"), (-110, 0.52), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, s.tr("nseite", "n-Gebiet", "n region", "región n", "n 区"), (110, 0.52), groesse=22, ausrichtung="center", farbe=GRAU)
    s.punkt(a, 0, jn, farbe=BLAU, r=0.07)
    s.punkt(a, 0, jp, farbe=ROT, r=0.07)
    s.text(a, "0.23", (8, jn - 0.02), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "0.77", (-8, jp - 0.12), groesse=22, ausrichtung="right", farbe=ROT)
    s.speichern()


def k14kennlinie():
    """Kennlinie des Rechenmodells linear und halblogarithmisch."""
    s = Szene("gemb1/k14kennlinie")
    s.welt()
    js = 1.602176634e-19 * (DN * NP0 / (LN * 1e-4) + DP * PN0 / (LP * 1e-4))
    Is = js * 0.01
    a = s.achsen((-0.3, 0.75), (-2, 12), breite=2.55, hoehe=2.1, mitte=(-1.95, 0), xl=achse(s, "U_{pn}", "V"), yl=achse(s, "I", "mA"), xticks="-0.2;0;0.2;0.4;0.6", yticks="0;4;8;12")
    s.linie(a, (-0.3, 0), (0.75, 0), farbe=GRAU, dicke=1.5)
    vs = [float(v) for v in np.linspace(-0.3, 0.68, 240)]
    s.daten(a, [(v, Is * (exp(v / KT) - 1) * 1e3) for v in vs if Is * (exp(v / KT) - 1) * 1e3 < 12.5], farbe=BLAU, dicke=4.5)
    b = s.achsen((0, 0.75), (1e-13, 1e-1), breite=2.85, hoehe=2.1, mitte=(1.75, 0), xl=achse(s, "U_{pn}", "V"), yl=achse(s, "I", "A"), ylog=True, xticks="0;0.2;0.4;0.6", yticks="1e-13;1e-10;1e-7;1e-4;1e-1")
    us = [float(v) for v in np.linspace(0.015, 0.75, 120)]
    s.daten(b, [(v, Is * (exp(v / KT) - 1)) for v in us], farbe=BLAU, dicke=4.5)
    s.linie(b, (0, Is), (0.75, Is), farbe=GRAU, dicke=2, dash=DASH)
    s.text(b, "I_S", (0.5, 6e-13), groesse=GR, ausrichtung="center", farbe=GRAU)
    v1 = 0.3
    i1 = Is * exp(v1 / KT)
    v2 = v1 + KT * log(1000)
    s.linie(b, (v1, i1), (v2, i1), farbe=ROT, dicke=2.5)
    s.linie(b, (v2, i1), (v2, i1 * 1000), farbe=ROT, dicke=2.5)
    s.text(b, s.tr("dek", "60 mV je Dekade", "60 mV per decade", "60 mV por década", "每十倍 60 mV"), (0.39, 3e-10), groesse=22, ausrichtung="left", farbe=ROT)
    s.linie(b, (0.661, 1e-13), (0.661, 1e-1), farbe=GRAU, dicke=2, dash=DOT)
    s.text(b, s.tr("grenz", "Ende schwache Injektion", "end of low injection", "fin de inyección débil", "弱注入极限"), (0.64, 2e-11), groesse=22, ausrichtung="right", farbe=GRAU)
    s.speichern()


if __name__ == "__main__":
    for f in (k14baender, k14kontakt, k14schottky, k14verlauf, k14spannung, k14injektion, k14strom, k14kennlinie):
        f()
    print("gemb1 Teil 14: Szenen geschrieben")
