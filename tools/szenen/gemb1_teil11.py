"""GEMB 1 Teil 11 (kap11_stufen.tex): Eigenhalbleiter und Dotierung.

Aufruf: python tools/szenen/gemb1_teil11.py, danach python tools/szenen_ansehen.py out.png gemb1/k11bereiche ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap11.py.
"""
import sys
from math import asinh, exp, log, log10, pi, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN, HELLGRAU2 = "#f6dede", "#dceafa", "#ddf0e4", "#ececec"
KB = 8.617333e-5
EG = 1.12
NC300, NV300 = 2.816e19, 1.829e19    # aus m_C* = 1,08 m0 und m_V* = 0,81 m0 (Teil 10)
ND0, DED, DEA = 1e16, 0.045, 0.045
ER, MD = 11.7, 0.19
E1, R1 = 13.606, 0.05292
RD = R1 * ER / MD
ED_ION = E1 * MD / ER**2 * 1000      # meV


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    return s.tr("a_" + name + einheit, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def ex(x):
    return exp(max(min(x, 690.0), -690.0))


def Nc(T):
    return NC300 * (T / 300)**1.5


def Nv(T):
    return NV300 * (T / 300)**1.5


def ni(T, Eg=EG):
    return sqrt(Nc(T) * Nv(T)) * ex(-Eg / (2 * KB * T))


def efi(T):
    return EG / 2 + KB * T / 2 * log(Nv(T) / Nc(T))


def loesen(T, Nd=0.0, Na=0.0, dD=DED, dA=DEA, gA=4.0):
    """Neutralität p + Nd+ - n - Na- = 0, E_F relativ zu E_V; wie rechnung_kap11.py."""
    kt = KB * T
    nc, nv = Nc(T), Nv(T)

    def q(E):
        n = nc * ex(-(EG - E) / kt)
        p = nv * ex(-E / kt)
        nd = Nd / (1 + 2 * ex((E - (EG - dD)) / kt)) if Nd else 0.0
        na = Na / (1 + gA * ex((dA - E) / kt)) if Na else 0.0
        return p + nd - n - na, n, p, nd, na

    a, b = -0.3, EG + 0.3
    for _ in range(200):
        m = (a + b) / 2
        if q(m)[0] > 0:
            a = m
        else:
            b = m
    return (m, *q(m)[1:])


def varshni(T, E0, al, be):
    return E0 - al * T**2 / (T + be)


# ------------------------------------------------------------------------------------------ Stufe 1
def gitter(s, x0, y0, d, namen, farben):
    """Drei mal drei Rümpfe, je Bindung zwei Elektronen."""
    for i in range(3):
        for j in range(3):
            xa, ya = x0 + i * d, y0 + j * d
            if i < 2:
                for v in (-0.055, 0.055):
                    s.punkt(None, xa + 0.5 * d, ya + v, farbe=SCHWARZ, r=0.03)
            if j < 2:
                for v in (-0.055, 0.055):
                    s.punkt(None, xa + v, ya + 0.5 * d, farbe=SCHWARZ, r=0.03)
            nam, fa = namen((i + j) % 2), farben((i + j) % 2)
            s.kreis(None, xa, ya, 0.23, farbe=fa, dicke=1.6, fuellung="#ffffff", deckung=1.0)
            t(s, nam, (xa, ya), farbe=fa, g=22)


def k11material():
    """Links die Bindung in der Ebene für Si und GaAs, rechts die Bandabstände."""
    s = Szene("gemb1/k11material")
    s.welt()
    gitter(s, -3.1, 0.2, 0.72, lambda k: "Si", lambda k: SCHWARZ)
    gitter(s, -3.1, -2.0, 0.72, lambda k: ("Ga", "As")[k], lambda k: (BLAU, ROT)[k])
    t(s, s.tr("sik", "Silizium: 8 Elektronen je Atom", "silicon: 8 electrons per atom", "silicio: 8 electrones por átomo", "硅：每原子 8 个电子"), (-2.38, 2.03), g=22)
    t(s, s.tr("gaask", "GaAs: 3 + 5 = 8", "GaAs: 3 + 5 = 8", "GaAs: 3 + 5 = 8", "GaAs：3 + 5 = 8"), (-2.38, -0.17), g=22)
    daten_ = [("InSb", 0.18, "0.18"), ("InAs", 0.35, "0.35"), ("Ge", 0.67, "0.67"), ("Si", 1.12, "1.12"), ("GaAs", 1.42, "1.42"), ("CdTe", 1.45, "1.45"), ("CdS", 2.42, "2.42"), ("AgI", 2.8, "2.8"), ("ZnO", 3.2, "3.2"), ("C", 5.5, "5.5")]
    n = len(daten_)
    a = s.achsen((0, 6), (0, n), breite=3.05, hoehe=3.7, mitte=(1.95, -0.05), xl=achse(s, "E_g", "eV"), yl="", yzahlen=False, ymarks=False, xticks="0;1;2;3;4;5;6", rahmen=False)
    s.band(a, 0.1, 3.0, 0, n, farbe=GRUEN, deckung=0.10)
    for i, (nam, Eg, txt) in enumerate(daten_):
        y = n - i - 0.5
        s.band(a, 0, Eg, y - 0.3, y + 0.3, farbe=BLAU if nam != "C" else GRAU, deckung=0.85)
        s.text(a, nam, (-0.15, y), groesse=22, ausrichtung="right")
        s.text(a, txt, (Eg + 0.12, y), groesse=22, ausrichtung="left")
    s.text(a, s.tr("hlber", "Halbleiter", "semiconductors", "semiconductores", "半导体"), (4.6, 7.5), groesse=22, ausrichtung="center", farbe=GRUEN)
    s.text(a, s.tr("isol", "Isolator", "insulator", "aislante", "绝缘体"), (4.75, 1.2), groesse=22, ausrichtung="center", farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k11ni():
    """n_i(1000/T) für Ge, Si, GaAs mit E_g(T); rechts E_g(T)."""
    s = Szene("gemb1/k11ni")
    s.welt()
    a = s.achsen((0.7, 4.0), (1e4, 1e20), breite=3.35, hoehe=2.9, mitte=(-1.5, 0.0), xl="1000/T in 1/K", yl="n_i in cm^{-3}", ylog=True, yticks="1e4;1e8;1e12;1e16;1e20", xticks="1;2;3;4")
    V = {"Ge": (0.7437, 4.774e-4, 235, 1.04e19, 6.0e18, GRUEN), "Si": (1.170, 4.73e-4, 636, NC300, NV300, BLAU), "GaAs": (1.519, 5.405e-4, 204, 4.7e17, 7.0e18, ROT)}
    for nam, (E0, al, be, c, v, fa) in V.items():
        pts = []
        for u in np.linspace(0.83 if nam == "Ge" else 0.7, 4.0, 60):
            T = 1000 / u
            pts.append((u, sqrt(c * v) * (T / 300)**1.5 * ex(-varshni(T, E0, al, be) / (2 * KB * T))))
        s.daten(a, pts, farbe=fa, dicke=4)
    s.linie(a, (1000 / 300, 1e4), (1000 / 300, 1e20), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "300 K", (3.7, 3e18), groesse=22, ausrichtung="center", farbe=GRAU)
    s.linie(a, (1.0, 1e4), (1.0, 1e20), farbe=GRAU, dicke=1.5, dash=DOT)
    s.text(a, "1000 K", (1.5, 3e18), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "Ge", (2.9, 5e15), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.text(a, "Si", (3.0, 2e12), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "GaAs", (1.55, 3e9), groesse=GR, ausrichtung="center", farbe=ROT)
    b = s.achsen((0, 800), (0.4, 1.6), breite=1.6, hoehe=2.9, mitte=(2.3, 0.0), xl=achse(s, "T", "K"), yl=achse(s, "E_g", "eV"), xticks="0;400;800", yticks="0.4;0.8;1.2;1.6")
    for nam, (E0, al, be, c, v, fa) in V.items():
        s.daten(b, [(T, varshni(T, E0, al, be)) for T in range(0, 801, 20)], farbe=fa, dicke=4)
        s.text(b, nam, (620, varshni(620, E0, al, be) + 0.09), groesse=GR, ausrichtung="center", farbe=fa)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def dotgitter(s, x0, y0, d, mitte, farbe, zeichen):
    for i in range(3):
        for j in range(3):
            xa, ya = x0 + i * d, y0 + j * d
            if i < 2:
                for v in (-0.05, 0.05):
                    if not (mitte == "B" and i == 0 and j == 1 and v > 0):
                        s.punkt(None, xa + 0.5 * d, ya + v, farbe=SCHWARZ, r=0.03)
            if j < 2:
                for v in (-0.05, 0.05):
                    s.punkt(None, xa + v, ya + 0.5 * d, farbe=SCHWARZ, r=0.03)
            istm = i == 1 and j == 1
            s.kreis(None, xa, ya, 0.225, farbe=farbe if istm else SCHWARZ, dicke=2.4 if istm else 1.5, fuellung="#ffffff", deckung=1.0)
            t(s, mitte if istm else "Si", (xa, ya), farbe=farbe if istm else SCHWARZ, g=22)
    t(s, zeichen, (x0 + d - 0.27, y0 + d - 0.28), farbe=farbe, g=26)


def k11dotierung():
    """Donator und Akzeptor im Gitter, rechts die Niveaus in Silizium im echten Maßstab."""
    s = Szene("gemb1/k11dotierung")
    s.welt()
    d = 0.78
    dotgitter(s, -3.45, 0.3, d, "P", BLAU, "+")
    # frei werdendes Elektron
    s.kreis(None, -2.28, 1.47, 0.11, farbe=BLAU, dicke=2, fuellung=BLAU, deckung=1.0)
    t(s, "-", (-2.28, 1.5), farbe="#ffffff", g=24)
    s.pfeil((-2.51, 1.24), (-2.37, 1.38), "", farbe=BLAU, dicke=2.5, spitze=0.09, on=None)
    dotgitter(s, -3.45, -2.2, d, "B", ROT, "-")
    s.kreis(None, -3.06, -1.42, 0.11, farbe=ROT, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    t(s, "+", (-3.06, -1.42), farbe=ROT, g=22)
    t(s, s.tr("fuenf", "5 Außenelektronen", "5 valence electrons", "5 electrones de valencia", "5 个价电子"), (-2.67, 2.26), g=22, farbe=BLAU)
    t(s, s.tr("drei", "3 Außenelektronen", "3 valence electrons", "3 electrones de valencia", "3 个价电子"), (-2.67, -0.16), g=22, farbe=ROT)
    # Niveaus
    a = s.achsen((0, 7), (0, 1120), breite=3.15, hoehe=3.5, mitte=(1.5, 0.0), xl="", yl="", xzahlen=False, xmarks=False, yzahlen=False, ymarks=False, unsichtbar=True)
    s.band(a, 0, 7, 1120, 1190, farbe=BLAU, deckung=0.2)
    s.band(a, 0, 7, -70, 0, farbe=ROT, deckung=0.2)
    s.linie(a, (0, 1120), (7, 1120), farbe=SCHWARZ, dicke=3.5)
    s.linie(a, (0, 0), (7, 0), farbe=SCHWARZ, dicke=3.5)
    s.text(a, "E_C", (7.0, 1120), groesse=GR, ausrichtung="left")
    s.text(a, "E_V", (7.0, 0), groesse=GR, ausrichtung="left")
    for i, (nam, w) in enumerate((("Sb", 39), ("P", 45), ("As", 54), ("Bi", 69), ("Te", 140), ("Ti", 210), ("Cr", 410))):
        x = i + 0.5
        s.linie(a, (x - 0.38, 1120 - w), (x + 0.38, 1120 - w), farbe=BLAU, dicke=3, dash="6,4")
        s.text(a, nam, (x, 1120 + 118), groesse=22, ausrichtung="center", farbe=BLAU)
        s.text(a, "%d" % w, (x, 1120 - w - 62), groesse=22, ausrichtung="center", farbe=BLAU)
    for i, (nam, w) in enumerate((("B", 45), ("Al", 67), ("Ga", 72), ("In", 160), ("Tl", 300), ("Pd", 340), ("Be", 170))):
        x = i + 0.5
        s.linie(a, (x - 0.38, w), (x + 0.38, w), farbe=ROT, dicke=3, dash="6,4")
        s.text(a, nam, (x, -118), groesse=22, ausrichtung="center", farbe=ROT)
        s.text(a, "%d" % w, (x, w + 62), groesse=22, ausrichtung="center", farbe=ROT)
    s.linie(a, (0, 560), (7, 560), farbe=GRAU, dicke=1.5, dash=DOT)
    s.text(a, s.tr("abst_me", "Abstand zur Bandkante in meV", "distance from band edge in meV", "distancia al borde en meV", "距带边 / meV"), (3.5, 620), groesse=22, ausrichtung="center", farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k11wasserstoff():
    """Coulomb-Trichter im Vakuum und im Silizium: gleiche Form, andere Achsen."""
    s = Szene("gemb1/k11wasserstoff")
    s.welt()
    V0 = 1.44                 # e^2/(4 pi eps0) in eV nm
    a = s.achsen((-0.5, 0.5), (-16, 0), breite=2.45, hoehe=2.5, mitte=(-1.9, 0.0), xl=achse(s, "r", "nm"), yl=achse(s, "E", "eV"), xticks="-0.4;0;0.4", yticks="-15;-10;-5;0", titel=s.tr("vak", "Wasserstoff im Vakuum", "hydrogen in vacuum", "hidrógeno en vacío", "真空中的氢"), titel_mitte=True)
    xs = [x for x in np.linspace(-0.5, 0.5, 201) if abs(x) > 0.08]
    s.daten(a, [(x, -V0 / abs(x)) for x in xs if x < 0], farbe=SCHWARZ, dicke=4)
    s.daten(a, [(x, -V0 / abs(x)) for x in xs if x > 0], farbe=SCHWARZ, dicke=4)
    rg = V0 / E1
    s.linie(a, (-rg, -E1), (rg, -E1), farbe=ROT, dicke=4)
    s.text(a, "-13.6\\,\\mathrm{eV}", (0.28, -13.6), groesse=GR, ausrichtung="center", farbe=ROT)
    s.linie(a, (-0.5, 0), (0.5, 0), farbe=GRAU, dicke=2, dash=DASH)
    b = s.achsen((-12, 12), (-80, 0), breite=2.7, hoehe=2.5, mitte=(1.9, 0.0), xl=achse(s, "r", "nm"), yl=achse(s, "E-E_C", "meV"), xticks="-10;0;10", yticks="-80;-40;0", titel=s.tr("sili", "Elektron am Donator in Si", "electron at a donor in Si", "electrón en un donador en Si", "硅中施主上的电子"), titel_mitte=True)
    W = V0 / ER * 1000
    xs = [x for x in np.linspace(-12, 12, 481) if abs(x) > W / 80]
    s.daten(b, [(x, -W / abs(x)) for x in xs if x < 0], farbe=SCHWARZ, dicke=4)
    s.daten(b, [(x, -W / abs(x)) for x in xs if x > 0], farbe=SCHWARZ, dicke=4)
    rg = W / ED_ION
    s.linie(b, (-rg, -ED_ION), (rg, -ED_ION), farbe=ROT, dicke=4)
    s.text(b, "-19\\,\\mathrm{meV}", (8.2, -ED_ION - 11), groesse=GR, ausrichtung="center", farbe=ROT)
    s.linie(b, (-12, 0), (12, 0), farbe=BLAU, dicke=3)
    s.text(b, "E_C", (10.2, -7), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.pfeil((0, -60), (RD, -60), "", farbe=ORANGE, dicke=2.5, spitze=0.1, doppelt=True, on=b)
    s.text(b, "r_D = 3.3\\,\\mathrm{nm}", (7.4, -60), groesse=GR, ausrichtung="center", farbe=ORANGE)
    for i in range(-22, 23):
        s.punkt(b, i * 0.543, -74, farbe=GRAU, r=0.022)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k11neutral():
    """Links Zustände mit Donatorniveau, rechts Ladungen über E_F: Schnittpunkt legt E_F fest."""
    s = Szene("gemb1/k11neutral")
    s.welt()
    # Zustandsdichte
    a = s.achsen((0, 1), (-0.25, 1.37), breite=1.6, hoehe=2.8, mitte=(-2.62, 0.05), xl="D(E)", yl="E", xzahlen=False, xmarks=False, yzahlen=False, ymarks=False)
    s.band(a, 0, 1, 0, EG, farbe=GRAU, deckung=0.12)
    s.daten(a, [(0.9 * sqrt(max(e, 0) / 0.25), EG + e) for e in np.linspace(0, 0.25, 40)], farbe=BLAU, dicke=4)
    s.daten(a, [(0.75 * sqrt(max(e, 0) / 0.25), -e) for e in np.linspace(0, 0.25, 40)], farbe=ROT, dicke=4)
    s.linie(a, (0, EG), (1, EG), farbe=SCHWARZ, dicke=2)
    s.linie(a, (0, 0), (1, 0), farbe=SCHWARZ, dicke=2)
    s.pfeil((0, EG - 0.13), (0.8, EG - 0.13), "", farbe=GRUEN, dicke=3, spitze=0.12, on=a)
    Ef = EG - 0.2055
    s.linie(a, (0, Ef), (1, Ef), farbe=ORANGE, dicke=3, dash=DASH)
    s.text(a, "E_C", (-0.05, EG), groesse=GR, ausrichtung="right")
    s.text(a, "E_V", (-0.05, 0), groesse=GR, ausrichtung="right")
    s.text(a, "E_D", (1.03, EG - 0.1), groesse=GR, ausrichtung="left", farbe=GRUEN)
    s.text(a, "E_F", (1.03, Ef - 0.05), groesse=GR, ausrichtung="left", farbe=ORANGE)
    s.text(a, "D_C", (0.45, EG + 0.2), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "D_V", (0.42, -0.17), groesse=GR, ausrichtung="center", farbe=ROT)
    # Ladungen
    b = s.achsen((0, EG), (1e2, 1e20), breite=3.55, hoehe=2.8, mitte=(1.33, 0.05), xl=s.tr("ef_achse", "E_F - E_V in eV", "E_F - E_V in eV", "E_F - E_V en eV", "E_F - E_V / eV"), yl=s.tr("dichte", "Dichte in cm^{-3}", "density in cm^{-3}", "densidad en cm^{-3}", "密度 / cm^{-3}"), ylog=True, yticks="1e4;1e8;1e12;1e16;1e20", xticks="0;0.28;0.56;0.84;1.12")
    kt = KB * 300
    ef = np.linspace(0.0, EG, 141)
    pn = [(float(x), Nc(300) * ex(-(EG - x) / kt)) for x in ef]
    pp = [(float(x), Nv(300) * ex(-x / kt)) for x in ef]
    pd = [(float(x), ND0 / (1 + 2 * ex((x - (EG - DED)) / kt))) for x in ef]
    s.daten(b, pn, farbe=BLAU, dicke=4)
    s.daten(b, pp, farbe=ROT, dicke=4)
    s.daten(b, pd, farbe=GRUEN, dicke=4)
    s.daten(b, [(p1[0], p1[1] + p2[1]) for p1, p2 in zip(pp, pd)], farbe=SCHWARZ, dicke=2, dash=DASH)
    s.linie(b, (Ef, 1e2), (Ef, ND0), farbe=ORANGE, dicke=2.5, dash=DASH)
    s.punkt(b, Ef, ND0, farbe=ORANGE, r=0.09)
    s.text(b, "n", (0.66, 3e13), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b, "p", (0.40, 3e13), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b, "N_D^+", (0.43, 1.2e17), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.text(b, "E_F", (Ef - 0.07, 1e3), groesse=GR, ausrichtung="center", farbe=ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k11bereiche():
    """n über 1000/T für N_D = 1e16 mit den drei Bereichen; darunter E_F im selben Maßstab."""
    s = Szene("gemb1/k11bereiche")
    s.welt()
    xa, xb = 0.0, 22.0
    gI, gII = 1000 / 719.0, 1000 / 94.6
    us = sorted(set(list(np.linspace(0.8, 2.4, 80)) + list(np.linspace(2.4, 22, 90))))
    rows = []
    for u in us:
        T = 1000 / u
        Ef, n, p, nd, _ = loesen(T, Nd=ND0)
        rows.append((u, T, Ef, n, p))
    a = s.achsen((xa, xb), (1e10, 1e18), breite=5.6, hoehe=2.1, mitte=(0.35, 1.1), xl="", yl="n in cm^{-3}", ylog=True, yticks="1e10;1e12;1e14;1e16;1e18", xticks="0;5;10;15;20", xzahlen=False)
    s.band(a, xa, gI, 1e10, 1e18, farbe=ROT, deckung=0.10)
    s.band(a, gI, gII, 1e10, 1e18, farbe=GRUEN, deckung=0.10)
    s.band(a, gII, xb, 1e10, 1e18, farbe=BLAU, deckung=0.10)
    s.daten(a, [(u, ni(1000 / u)) for u in np.linspace(0.8, 3.5, 40)], farbe=GRAU, dicke=3, dash=DASH)
    s.linie(a, (0, ND0), (xb, ND0), farbe=GRAU, dicke=2, dash=DOT)
    s.daten(a, [(u, sqrt(Nc(1000 / u) * ND0 / 2) * ex(-DED * u / (2 * KB * 1000))) for u in np.linspace(7, 22, 40)], farbe=ORANGE, dicke=3, dash=DASH)
    s.daten(a, [(r[0], r[3]) for r in rows], farbe=BLAU, dicke=5)
    s.text(a, "n_i", (3.6, 3e10), groesse=GR, ausrichtung="center", farbe=GRAU)
    s.text(a, "N_D", (18.8, 2.2e16), groesse=GR, ausrichtung="center", farbe=GRAU)
    s.text(a, "I", (0.75, 3e17), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, "II", (6, 3e17), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.text(a, "III", (16.5, 3e17), groesse=GR, ausrichtung="center", farbe=BLAU)
    for T in (1000, 300, 100, 50):
        u = 1000 / T
        s.linie(a, (u, 8e17), (u, 1e18), farbe=SCHWARZ, dicke=2)
        s.text(a, "%d\\,\\mathrm{K}" % T, (u, 2.4e18), groesse=22, ausrichtung="center")
    b = s.achsen((xa, xb), (0, EG), breite=5.6, hoehe=1.4, mitte=(0.35, -1.25), xl="1000/T in 1/K", yl=achse(s, "E-E_V", "eV"), xticks="0;5;10;15;20", yticks="0;0.56;1.12")
    s.band(b, xa, gI, 0, EG, farbe=ROT, deckung=0.10)
    s.band(b, gI, gII, 0, EG, farbe=GRUEN, deckung=0.10)
    s.band(b, gII, xb, 0, EG, farbe=BLAU, deckung=0.10)
    s.linie(b, (0, EG - DED), (xb, EG - DED), farbe=GRUEN, dicke=2, dash=DASH)
    s.linie(b, (0, EG), (xb, EG), farbe=SCHWARZ, dicke=3)
    s.daten(b, [(u, efi(1000 / u)) for u in np.linspace(0.8, 22, 40)], farbe=GRAU, dicke=2.5, dash=DASH)
    s.daten(b, [(r[0], r[2]) for r in rows], farbe=ORANGE, dicke=5)
    s.text(b, "E_{Fi}", (19, 0.67), groesse=GR, ausrichtung="center", farbe=GRAU)
    s.text(b, "E_F", (5.4, 0.72), groesse=GR, ausrichtung="center", farbe=ORANGE)
    s.text(b, "E_C", (22.9, 1.17), groesse=GR, ausrichtung="center")
    s.text(b, "E_D", (22.9, 1.0), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k11fermi():
    """E_F über T für n- und p-Dotierung, Silizium, drei Dichten."""
    s = Szene("gemb1/k11fermi")
    s.welt()
    a = s.achsen((0, 800), (0, EG), breite=5.5, hoehe=3.0, mitte=(0.15, 0.0), xl=achse(s, "T", "K"), yl=achse(s, "E-E_V", "eV"), xticks="0;200;400;600;800", yticks="0;0.2;0.4;0.6;0.8;1;1.12")
    s.daten(a, [(T, efi(T)) for T in range(0, 801, 40) if T > 0], farbe=GRAU, dicke=3, dash=DASH)
    s.linie(a, (0, EG), (800, EG), farbe=SCHWARZ, dicke=3.5)
    s.linie(a, (0, 0), (800, 0), farbe=SCHWARZ, dicke=3.5)
    s.linie(a, (0, EG - DED), (800, EG - DED), farbe=GRUEN, dicke=2, dash=DASH)
    s.linie(a, (0, DEA), (800, DEA), farbe=GRUEN, dicke=2, dash=DASH)
    Ts = [8, 12, 16, 20, 25, 30, 40, 50, 60, 80, 100, 130, 160, 200] + list(range(240, 801, 30))
    for N, dk, lab, Tl in ((1e14, 2.5, "10^{14}", 330), (1e16, 3.5, "10^{16}", 420), (1e18, 4.5, "10^{18}", 560)):
        pn, pp = [], []
        for T in Ts:
            pn.append((T, loesen(T, Nd=N)[0]))
            pp.append((T, loesen(T, Na=N)[0]))
        pn.insert(0, (0, EG - DED / 2))
        pp.insert(0, (0, DEA / 2))
        s.daten(a, pn, farbe=BLAU, dicke=dk)
        s.daten(a, pp, farbe=ROT, dicke=dk)
        en = loesen(Tl, Nd=N)[0]
        ep = loesen(Tl, Na=N)[0]
        s.text(a, lab, (Tl - 6, en + 0.075), groesse=22, ausrichtung="left", farbe=BLAU)
        s.text(a, lab, (Tl - 6, ep - 0.075), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "E_C", (838, EG), groesse=GR, ausrichtung="left")
    s.text(a, "E_V", (838, 0), groesse=GR, ausrichtung="left")
    s.text(a, "E_D", (838, EG - 0.095), groesse=GR, ausrichtung="left", farbe=GRUEN)
    s.text(a, "E_A", (838, 0.095), groesse=GR, ausrichtung="left", farbe=GRUEN)
    s.text(a, "E_{Fi}", (838, efi(790)), groesse=GR, ausrichtung="left", farbe=GRAU)
    s.text(a, s.tr("ntyp", "n-Typ, N_D in cm^{-3}", "n-type, N_D in cm^{-3}", "tipo n, N_D en cm^{-3}", "n 型，N_D / cm^{-3}"), (155, 0.68), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("ptyp", "p-Typ, N_A in cm^{-3}", "p-type, N_A in cm^{-3}", "tipo p, N_A en cm^{-3}", "p 型，N_A / cm^{-3}"), (155, 0.44), groesse=22, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k11hoch():
    """Oben die Donator-Orbitale im Maßstab, unten die Zustandsdichte: Niveau, Störstellenband, Verschmelzen."""
    s = Szene("gemb1/k11hoch")
    s.welt()
    fen = (2.0, 1.0)                   # Fenster in Szeneneinheiten: 44 nm x 22 nm
    sk = fen[0] / 44.0
    faelle = (("10^{17}", 21.5, 0), ("10^{18}", 10.0, 1), ("10^{19}", 4.64, 2))
    for j, (lab, d, stufe) in enumerate(faelle):
        mx = -2.2 + j * 2.3
        x0, y0 = mx - fen[0] / 2, 1.5
        s.linie(None, (x0, y0), (x0 + fen[0], y0), farbe=GRAU, dicke=1.5)
        s.linie(None, (x0, y0 + fen[1]), (x0 + fen[0], y0 + fen[1]), farbe=GRAU, dicke=1.5)
        s.linie(None, (x0, y0), (x0, y0 + fen[1]), farbe=GRAU, dicke=1.5)
        s.linie(None, (x0 + fen[0], y0), (x0 + fen[0], y0 + fen[1]), farbe=GRAU, dicke=1.5)
        nx = int(44 / d)
        ny = int(22 / d)
        ox = (44 - (nx - 1) * d) / 2
        oy = (22 - (ny - 1) * d) / 2
        for ix in range(nx):
            for iy in range(max(ny, 1)):
                cx, cy = x0 + (ox + ix * d) * sk, y0 + (oy + iy * d) * sk
                s.kreis(None, cx, cy, RD * sk, farbe=BLAU, dicke=1.5, fuellung=BLAU, deckung=0.3)
                s.punkt(None, cx, cy, farbe=ROT, r=0.022)
        t(s, "N_D = " + lab + "\\,\\mathrm{cm^{-3}}", (mx, y0 + fen[1] + 0.27), g=22)
        a = s.achsen((0, 1), (-0.2, 1.5), breite=1.85, hoehe=2.3, mitte=(mx + 0.05, 0.0), xl="", yl="E" if j == 0 else "", xzahlen=False, xmarks=False, yzahlen=False, ymarks=False)
        s.text(a, "D(E)", (0.84, -0.3), groesse=GR, ausrichtung="center")
        ec = 1.0
        ev = 0.0
        ed = 0.88
        s.daten(a, [(0.62 * sqrt(max(-e, 0) / 0.2), ev + e) for e in np.linspace(-0.2, 0, 30)], farbe=GRUEN, dicke=4)
        if stufe == 0:
            s.daten(a, [(0.62 * sqrt((e) / 0.5), ec + e) for e in np.linspace(0, 0.5, 40)], farbe=GRUEN, dicke=4)
            s.pfeil((0, ed), (0.85, ed), "", farbe=BLAU, dicke=3, spitze=0.12, on=a)
            ef = 0.70
        elif stufe == 1:
            s.daten(a, [(0.62 * sqrt((e) / 0.5), ec + e) for e in np.linspace(0, 0.5, 40)], farbe=GRUEN, dicke=4)
            br = 0.045
            ys = np.linspace(ed - 3.2 * br, ed + 3.2 * br, 50)
            s.daten(a, [(0.6 * exp(-((y - ed) / br)**2 / 2), y) for y in ys], farbe=BLAU, dicke=4)
            ef = 0.85
        else:
            br = 0.09
            ys = np.linspace(0.62, 1.5, 90)
            s.daten(a, [(0.62 * sqrt(max(y - ec, 0) / 0.5) + 0.34 * exp(-((y - ed) / br)**2 / 2), y) for y in ys], farbe=SCHWARZ, dicke=4)
            ef = 1.03
        s.linie(a, (0, ef), (1, ef), farbe=ROT, dicke=2.5, dash=DASH)
        s.text(a, "E_F", (0.85, ef - 0.085), groesse=GR, ausrichtung="center", farbe=ROT)
        if j == 0:
            s.text(a, "E_C", (-0.05, ec), groesse=GR, ausrichtung="right")
            s.text(a, "E_D", (-0.05, ed - 0.03), groesse=GR, ausrichtung="right", farbe=BLAU)
            s.text(a, "E_V", (-0.05, ev), groesse=GR, ausrichtung="right")
        if stufe == 2:
            un = 0.68
            s.pfeil((0.72, ev), (0.72, un), "", farbe=ORANGE, dicke=2.5, spitze=0.1, doppelt=True, on=a)
            s.text(a, "E_g^{eff}", (0.47, 0.36), groesse=GR, ausrichtung="center", farbe=ORANGE)
            s.linie(a, (0, un), (0.85, un), farbe=ORANGE, dicke=1.5, dash=DOT)
    s.speichern()


if __name__ == "__main__":
    for f in (k11material, k11ni, k11dotierung, k11wasserstoff, k11neutral, k11bereiche, k11fermi, k11hoch):
        f()
    print("gemb1 Teil 11: Szenen geschrieben")
