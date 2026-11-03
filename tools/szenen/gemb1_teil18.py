"""GEMB 1 Teil 18 (kap18_stufen.tex): Skalierung und Kurzkanaleffekte.

Aufruf: python tools/szenen/gemb1_teil18.py, danach python tools/szenen_ansehen.py out.png gemb1/k18gut ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap18.py, die zweidimensionalen Daten aus daten/k18_poisson.json
(python rechnung_kap18.py --2d).
"""
import json
import re
import sys
from math import exp, log, log10, pi, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HEFT = Path("C:/Bücher/GEMB/Arbeitshefte")
sys.path.insert(0, str(HEFT))
import rechnung_kap18 as R  # noqa: E402

GR = 24
WEISS = "#ffffff"
LILA = "#6a3fa0"
D2 = json.loads((HEFT / "daten" / "k18_poisson.json").read_text(encoding="utf-8"))


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR, on=None):
    s.text(on, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit, key=None):
    key = key or "a_" + re.sub(r"[^A-Za-z0-9]", "", name + "_" + einheit.replace("\u00b5", "u"))
    return s.tr(key, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def transfer(V, Vt, Sx, L, W=R.W):
    """I_D(V_GS): unter der Schwelle I_th 10^((V-V_th)/S), darüber geglättet in das quadratische Gesetz."""
    n = Sx / (R.VT * log(10))
    K = R.Kf(L, W)
    Is = 2 * n * R.VT**2 * K
    x = (V - Vt) / (n * R.VT) + log(R.Ith(L) / Is)
    return Is * np.log1p(np.exp(x / 2))**2


def schnitt(s, x0, x1, yo, yu, xs, xd, tiefe, gate=0.42, ox=0.1):
    """Querschnitt eines MOSFET in Weltkoordinaten."""
    s.band(None, x0, x1, yu, yo, farbe=GRAU, deckung=0.2)
    s.band(None, x0, xs, yo - tiefe, yo, farbe=ORANGE, deckung=0.6)
    s.band(None, xd, x1, yo - tiefe, yo, farbe=ORANGE, deckung=0.6)
    s.band(None, xs, xd, yo, yo + ox, farbe=GRUEN, deckung=0.35)
    s.band(None, xs, xd, yo + ox, yo + ox + gate, farbe=SCHWARZ, deckung=0.65)


# ------------------------------------------------------------------------------------------ Stufe 1
def k18gut():
    """Links: Transistor 1 lädt das Gate von Transistor 2 um. Rechts: Schaltzeit über der Kanallänge."""
    s = Szene("gemb1/k18gut")
    s.welt()
    m = 0.5
    x1, y1 = -3.0, -0.15
    s.geraet("nmos", (x1, y1), groesse=m)
    xD, yD, yS = x1 + 0.5 * m, y1 + m, y1 - m
    yk = yD + 0.55
    s.draht((xD, yD), (xD, yk), (-1.35, yk))
    s.draht((xD, yS), (xD, yS - 0.3))
    s.geraet("ground", (xD, yS - 0.3), groesse=0.45)
    s.draht((x1 - m, y1), (x1 - m - 0.2, y1))
    # Lastkapazität, gestrichelt angedeutet durch die Beschriftung
    xc = -1.85
    s.linie(None, (xc, yk), (xc, 0.05), dicke=3)
    s.bauteil("capacitor", (xc, -0.25), drehung=270, laenge=0.6, label="C_g", font_size=24, size=0.55, label_flip=False)
    s.linie(None, (xc, -0.55), (xc, yS - 0.3), dicke=3)
    s.geraet("ground", (xc, yS - 0.3), groesse=0.45)
    s.punkt(None, xc, yk, r=0.07)
    # zweiter Transistor
    x2 = -0.7
    s.geraet("nmos", (x2, y1), groesse=m)
    s.draht((-1.35, yk), (-1.35, y1), (x2 - m, y1))
    s.draht((x2 + 0.5 * m, yD), (x2 + 0.5 * m, yD + 0.3))
    s.draht((x2 + 0.5 * m, yS), (x2 + 0.5 * m, yS - 0.3))
    s.geraet("ground", (x2 + 0.5 * m, yS - 0.3), groesse=0.45)
    s.pfeil((xD + 0.16, yD + 0.45), (xD + 0.16, yD + 0.05), "", farbe=ROT, spitze=0.14, dicke=3)
    t(s, "I_D", (xD + 0.25, yD + 0.25), a="left", farbe=ROT)
    t(s, s.tr("t1", "Transistor 1", "transistor 1", "transistor 1", "晶体管 1"), (x1 + 0.1, yk + 0.4), g=22)
    t(s, s.tr("t2", "Transistor 2", "transistor 2", "transistor 2", "晶体管 2"), (-0.85, yk + 0.4), g=22)
    a = s.achsen((10, 2000), (0.01, 1000), breite=2.7, hoehe=2.9, mitte=(1.9, -0.1), xl=achse(s, "L", "nm"), yl=achse(s, "\u03c4", "ps"),
                 xlog=True, ylog=True, xticks="10;100;1000", yticks="0.01;0.1;1;10;100;1000", gitter=True)
    Ls = np.logspace(1, log10(2000), 40)
    s.daten(a, [(l, R.tauL2(l * 1e-9) * 1e12) for l in Ls], farbe=BLAU, dicke=4.5)
    s.daten(a, [(l, R.tauL2(l * 1e-9, R.VDD, 0.8) * 1e12) for l in Ls], farbe=GRUEN, dicke=4)
    s.punkt(a, 1000, R.tauL2(1e-6) * 1e12, farbe=ROT)
    s.punkt(a, 100, R.tauL2(1e-7) * 1e12, farbe=ROT)
    s.text(a, "188 ps", (1300, 30), groesse=22, ausrichtung="right", farbe=ROT)
    s.text(a, "1.9 ps", (130, 0.9), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "V_{th} = 0.8 V", (14, 6), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, "V_{th} = 0.4 V", (45, 0.04), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k18skal():
    """Links: Alle Längen schrumpfen gemeinsam. Rechts: Die Schwellspannung kann nicht mitgehen."""
    s = Szene("gemb1/k18skal")
    s.welt()
    schnitt(s, -3.6, -0.6, 1.25, 0.2, -2.9, -1.3, 0.42, gate=0.32, ox=0.1)
    t(s, "L", (-2.1, 0.95), g=24)
    s.pfeil((-2.9, 0.75), (-1.3, 0.75), "", farbe=SCHWARZ, dicke=2.5, spitze=0.11, doppelt=True)
    t(s, "N_A", (-2.1, 0.45), g=24)
    t(s, "V_{dd}", (-1.25, 1.55), a="left", farbe=BLAU, g=24)
    t(s, s.tr("tief", "Tiefe", "depth", "prof.", "深度"), (-3.25, 0.62), g=22)
    schnitt(s, -2.85, -1.35, -0.85, -1.38, -2.5, -1.7, 0.21, gate=0.16, ox=0.05)
    s.pfeil((-2.1, 0.05), (-2.1, -0.45), "", farbe=ROT, dicke=3, spitze=0.17)
    t(s, "\u00f7 \u03b1_s", (-1.95, -0.2), a="left", farbe=ROT, g=24)
    t(s, "L / \u03b1_s", (-1.15, -0.95), a="left", g=24)
    t(s, "V_{dd} / \u03b1_s", (-1.15, -0.55), a="left", farbe=BLAU, g=24)
    t(s, "N_A \u03b1_s", (-1.15, -1.35), a="left", g=24)
    a = s.achsen((0, 1.2), (1e-14, 1e-2), breite=2.7, hoehe=3.0, mitte=(2.0, 0.05), xl=achse(s, "V_{GS}", "V"), yl=achse(s, "I_D", "A"),
                 ylog=True, xticks="0;0.4;0.8;1.2", yticks="1e-14;1e-12;1e-10;1e-8;1e-6;1e-4;1e-2", gitter=True)
    Vs = np.linspace(0, 1.2, 121)
    L = 1e-7
    i1 = transfer(Vs, 0.40, R.SLANG, L)
    v2 = np.linspace(0, 0.7, 71)
    i2 = transfer(v2, 0.10, R.SLANG, L)
    s.daten(a, list(zip(Vs, i1)), farbe=GRUEN, dicke=4.5)
    s.daten(a, list(zip(v2, i2)), farbe=BLAU, dicke=4.5)
    s.punkt(a, 0, float(transfer(0.0, 0.40, R.SLANG, L)), farbe=GRUEN)
    s.punkt(a, 0, float(transfer(0.0, 0.10, R.SLANG, L)), farbe=BLAU)
    s.punkt(a, 1.2, float(i1[-1]), farbe=GRUEN)
    s.punkt(a, 0.7, float(i2[-1]), farbe=BLAU)
    s.text(a, "V_{th} = 0.40 V", (0.62, 4e-9), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(a, "V_{th} = 0.10 V", (0.04, 1.5e-3), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "I_{leak}", (0.05, 2e-13), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
FARBEN = {"0.05": "#2a78d6", "0.25": "#2f9e8f", "0.45": "#00823c", "0.65": "#8a9a1e", "0.85": "#d9a400", "1.05": "#eb6834", "1.45": "#c82828", "1.85": "#8c1c1c"}


def karte(s, L, mitte, breite, x0, x1, titel):
    h = 132 * breite / (x1 - x0)
    a = s.achsen((x0, x1), (-110, 22), breite=breite, hoehe=h, mitte=mitte, xl="", yl="", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False, rahmen=True, titel=titel)
    s.band(a, x0, 0, -30, 0, farbe=ORANGE, deckung=0.45)
    s.band(a, L, x1, -30, 0, farbe=ORANGE, deckung=0.45)
    s.band(a, 0, L, 2, 21, farbe=SCHWARZ, deckung=0.7)
    for lv, segs in D2["karten"][str(L)].items():
        for seg in segs:
            s.daten(a, [(p[0], -p[1]) for p in seg], farbe=FARBEN[lv], dicke=3)
    return a


def k18zonen():
    """Linien gleichen Potentials bei V_GS = 0 und V_DS = 1,2 V, gleicher Maßstab."""
    s = Szene("gemb1/k18zonen")
    s.welt()
    breite = 6.6
    q = breite / 410.0
    a = karte(s, 300, (0.0, 1.85), breite, -55, 355, "L = 300 nm")
    s.text(a, "Source", (-50, -20), groesse=22, ausrichtung="left")
    s.text(a, "Drain", (350, -20), groesse=22, ausrichtung="right")
    s.text(a, "Gate", (150, 11.5), groesse=22, ausrichtung="center", farbe=WEISS)
    b0 = 160 * q
    xm = -3.3 + b0 / 2
    b = karte(s, 50, (xm, -0.95), b0, -55, 105, "L = 50 nm")
    s.text(b, "S", (-27, -20), groesse=22, ausrichtung="center")
    s.text(b, "D", (78, -20), groesse=22, ausrichtung="center")
    s.pfeil((-3.3, -2.2), (-3.3 + 100 * q, -2.2), "", farbe=SCHWARZ, dicke=2.5, spitze=0.1, doppelt=True)
    t(s, "100 nm", (-3.3 + 50 * q, -2.42), g=22)
    # Legende der Pegel
    x, y = 0.1, -0.45
    t(s, s.tr("pegel", "Potential \u03c6 in V:", "potential \u03c6 in V:", "potencial \u03c6 en V:", "电势 \u03c6 / V:"), (x, y + 0.02), a="left", g=22)
    pegel = ["0.05", "0.25", "0.45", "0.65", "0.85", "1.05", "1.45", "1.85"]
    for i, p in enumerate(pegel):
        sp, ze = i // 4, i % 4
        xx, yy = x + sp * 1.5, y - 0.38 - ze * 0.34
        s.linie(None, (xx, yy), (xx + 0.4, yy), farbe=FARBEN[p], dicke=4)
        t(s, p, (xx + 0.5, yy), a="left", g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def profil(s, L, mitte, x1, xt):
    br, ho = 2.65, 2.2
    a = s.achsen((-25, x1), (-1.3, 0.7), breite=br, hoehe=ho, mitte=mitte, xl=achse(s, "y", "nm"), yl=s.tr("a_ec", "E_C in eV", "E_C in eV", "E_C en eV", "E_C / eV"),
                 xticks=xt, yticks="-1;-0.5;0;0.5", titel="L = %d nm" % L)
    s.band(a, 0, L, -1.3, 0.7, farbe=GRAU, deckung=0.12)
    s.daten(a, D2["profile"]["%d_0.05" % L], farbe=GRAU, dicke=4)
    s.daten(a, D2["profile"]["%d_1.2" % L], farbe=BLAU, dicke=4.5)
    top = next(z for z in D2["tabelle"] if z["L"] == 300)["top1"]
    s.linie(a, (-25, top), (x1, top), farbe=ROT, dicke=2.5, dash=DASH)
    return a


def k18barriere():
    """Vier Teilbilder: Barriere bei langem und kurzem Kanal, Transferkennlinien, Schwellspannung über der Kanallänge."""
    s = Szene("gemb1/k18barriere")
    s.welt()
    a = profil(s, 100, (-1.8, 1.75), 125, "0;50;100")
    s.text(a, "V_{DS} = 0.05 V", (3, -0.35), groesse=22, ausrichtung="left", farbe=GRAU)
    s.text(a, "1.2 V", (120, -1.05), groesse=22, ausrichtung="right", farbe=BLAU)
    b = profil(s, 50, (1.85, 1.75), 75, "0;25;50;75")
    s.text(b, "\u03b4E_B", (22, 0.56), groesse=22, ausrichtung="center", farbe=ROT)
    t2 = {z["L"]: z for z in D2["tabelle"]}
    # Transferkennlinien
    c = s.achsen((0, 1.2), (1e-14, 1e-2), breite=2.65, hoehe=2.25, mitte=(-1.8, -1.75), xl=achse(s, "V_{GS}", "V"), yl=achse(s, "I_D", "A"), ylog=True,
                 xticks="0;0.4;0.8;1.2", yticks="1e-14;1e-10;1e-6;1e-2", gitter=True)
    Vs = np.linspace(0, 1.2, 121)
    Ll = 1e-6
    s.daten(c, list(zip(Vs, transfer(Vs, R.Vth(Ll, 1.2), R.S(Ll), Ll))), farbe=GRAU, dicke=4)
    Lk = 5e-8
    s.daten(c, list(zip(Vs, transfer(Vs, R.Vth(Lk, 0.05), R.S(Lk), Lk))), farbe=GRUEN, dicke=4)
    s.daten(c, list(zip(Vs, transfer(Vs, R.Vth(Lk, 1.2), R.S(Lk), Lk))), farbe=BLAU, dicke=4.5)
    s.text(c, "L = 1 \u00b5m", (0.5, 1e-12), groesse=22, ausrichtung="left", farbe=GRAU)
    s.text(c, "50 nm, 1.2 V", (0.04, 3e-4), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(c, "50 nm, 0.05 V", (0.42, 6e-10), groesse=22, ausrichtung="left", farbe=GRUEN)
    # Schwellspannung über L
    d = s.achsen((30, 1000), (0, 0.45), breite=2.65, hoehe=2.25, mitte=(1.85, -1.75), xl=achse(s, "L", "nm"), yl=achse(s, "V_{th}", "V"), xlog=True,
                 xticks="100;1000", yticks="0;0.1;0.2;0.3;0.4", gitter=True)
    Ls = np.logspace(log10(30), 3, 60)
    s.daten(d, [(l, max(R.Vth(l * 1e-9, 0.05), -1)) for l in Ls], farbe=GRUEN, dicke=4)
    s.daten(d, [(l, max(R.Vth(l * 1e-9, 1.2), -1)) for l in Ls], farbe=BLAU, dicke=4.5)
    for z in D2["tabelle"]:
        s.punkt(d, z["L"], z["vth1"], farbe=GRUEN, r=0.075)
        if z["vth2"] and z["vth2"] > 0.01:
            s.punkt(d, z["L"], z["vth2"], farbe=BLAU, r=0.075)
    x3 = 3 * R.LAM * 1e9
    s.linie(d, (x3, 0), (x3, 0.45), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(d, "3 \u03bb_{ch}", (x3 * 1.08, 0.415), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(d, "0.05 V", (120, 0.19), groesse=22, ausrichtung="left", farbe=GRUEN)
    s.text(d, "1.2 V", (60, 0.05), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k18clm():
    """Oben: abgeschnürter Kanal. Unten: Ausgangskennlinien mit Early-Geraden und mit Barrierenabsenkung."""
    s = Szene("gemb1/k18clm")
    s.welt()
    x0, x1, yo, yu = -3.4, 3.4, 3.05, 1.65
    xs, xd = -2.2, 2.2
    s.band(None, x0, x1, yu, yo, farbe=GRAU, deckung=0.2)
    s.band(None, x0, xs, yo - 0.55, yo, farbe=ORANGE, deckung=0.6)
    s.band(None, xd, x1, yo - 0.55, yo, farbe=ORANGE, deckung=0.6)
    s.band(None, xs, xd, yo, yo + 0.1, farbe=GRUEN, deckung=0.35)
    s.band(None, xs, xd, yo + 0.1, yo + 0.4, farbe=SCHWARZ, deckung=0.65)
    xp = 1.35

    # Kanal als Keil
    n = 44
    for i in range(n):
        xa = xs + (xp - xs) * i / n
        xb = xs + (xp - xs) * (i + 1) / n
        tiefe = 0.3 * sqrt(max(1 - (i + 0.5) / n, 0))
        s.band(None, xa, xb, yo - tiefe, yo, farbe=BLAU, deckung=0.75)
    s.band(None, xp, xd, yo - 0.5, yo, farbe=ROT, deckung=0.16)
    s.punkt(None, xp, yo, farbe=ROT, r=0.07)
    s.pfeil((xp, yo - 0.72), (xd, yo - 0.72), "", farbe=ROT, dicke=2.5, spitze=0.11, doppelt=True)
    t(s, "\u0394L", ((xp + xd) / 2, yo - 0.92), farbe=ROT, g=24)
    s.pfeil((xs, yo - 0.72), (xp, yo - 0.72), "", farbe=BLAU, dicke=2.5, spitze=0.11, doppelt=True)
    t(s, "L - \u0394L", ((xs + xp) / 2, yo - 0.92), farbe=BLAU, g=24)
    t(s, "Source", (-2.85, yo - 0.28), g=22)
    t(s, "Drain", (2.8, yo - 0.28), g=22)
    s.text(None, "Gate", (0, yo + 0.25), groesse=22, ausrichtung="center", farbe=WEISS)
    # links: Early
    K = R.Kf(5e-7)
    VE = 15.0
    a = s.achsen((-16, 2), (0, 300), breite=2.8, hoehe=2.75, mitte=(-1.8, -0.95), xl=achse(s, "V_{DS}", "V"), yl=achse(s, "I_D", "\u00b5A"), xticks="-15;-10;-5;0",
                 yticks="0;100;200;300", titel="L = 500 nm", gitter=True)
    for vg in (0.7, 0.85, 1.0, 1.2):
        ov = vg - R.VTHL
        v = np.linspace(0, 2, 81)
        i = [K * ((ov * x - x * x / 2) if x < ov else ov * ov / 2) * (1 + x / VE) * 1e6 for x in v]
        s.daten(a, list(zip(v, i)), farbe=BLAU, dicke=4)
        s.linie(a, (-VE, 0), (ov, K * ov * ov / 2 * (1 + ov / VE) * 1e6), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, -VE, 0, farbe=ROT)
    s.text(a, "-V_{Early}", (-15.5, 40), groesse=22, ausrichtung="left", farbe=ROT)
    # rechts: kurzer Kanal
    L = 5e-8
    K2 = R.Kf(L)
    b = s.achsen((0, 2), (0, 3.2), breite=2.65, hoehe=2.75, mitte=(1.85, -0.95), xl=achse(s, "V_{DS}", "V"), yl=achse(s, "I_D", "mA"), xticks="0;1;2", yticks="0;1;2;3",
                 titel="L = 50 nm", gitter=True)
    for vg in (0.6, 0.8, 1.0):
        v = np.linspace(0, 2, 161)
        i = []
        for x in v:
            ov = vg - R.Vth(L, x)
            i.append(K2 * ((ov * x - x * x / 2) if x < ov else ov * ov / 2) * 1e3)
        s.daten(b, list(zip(v, i)), farbe=BLAU, dicke=4)
        ov0 = vg - R.Vth(L, 0.0)
        s.linie(b, (ov0, K2 * ov0**2 / 2 * 1e3), (2, K2 * ov0**2 / 2 * 1e3), farbe=GRAU, dicke=2, dash=DASH)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k18vsat():
    """Links: Driftgeschwindigkeit über dem Feld. Rechts: Sättigungsstrom über der Spannungsreserve bei L = 100 nm."""
    s = Szene("gemb1/k18vsat")
    a = s.achsen((1e2, 1e6), (1e4, 3e7), breite=2.7, hoehe=3.0, mitte=(-1.8, 0.1), xl=s.tr("a_e", "Feld in V/cm", "field in V/cm", "campo en V/cm", "电场 / (V/cm)"),
                 yl=achse(s, "v", "cm/s"), xlog=True, ylog=True, xticks="1e2;1e3;1e4;1e5;1e6", yticks="1e4;1e5;1e6;1e7", gitter=True)
    Es = np.logspace(2, 6, 60)
    for mu, f in ((1350.0, BLAU), (200.0, GRUEN)):
        s.daten(a, [(E, mu * E / sqrt(1 + (mu * E / 1e7)**2)) for E in Es], farbe=f, dicke=4.5)
    s.daten(a, [(E, 1350 * E) for E in np.logspace(2, 4.1, 12)], farbe=GRAU, dicke=2.5, dash=DASH)
    s.linie(a, (1e2, 1e7), (1e6, 1e7), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(a, "v_{max}", (130, 1.5e7), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, "\u00b5 = 1350", (1.3e2, 2.2e6), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, "\u00b5 = 200", (1.5e4, 3e5), groesse=22, ausrichtung="left", farbe=GRUEN)
    b = s.achsen((0, 1.2), (0, 2.6), breite=2.65, hoehe=3.0, mitte=(1.85, 0.1), xl=achse(s, "V_{GS}-V_{th}", "V"), yl=achse(s, "I_{D,sat}", "mA"),
                 xticks="0;0.4;0.8;1.2", yticks="0;1;2", gitter=True, titel="L = 100 nm")
    Kx = R.Kf(1e-7)
    v = np.linspace(0, 1.2, 61)
    s.daten(b, [(x, Kx / 2 * x * x * 1e3) for x in v], farbe=GRAU, dicke=3, dash=DASH)
    s.daten(b, [(x, R.W * R.CIS * R.VMAX * x * 1e3) for x in v], farbe=ROT, dicke=3, dash=DASH)
    Ek = 2 * R.VMAX / R.MU
    s.daten(b, [(x, R.W * R.CIS * R.VMAX * x * x / (x + Ek * 1e-7 + 1e-12) * 1e3) for x in v], farbe=BLAU, dicke=4.5)
    s.punkt(b, 0.8, R.W * R.CIS * R.VMAX * 0.64 / 1.8 * 1e3, farbe=BLAU)
    s.text(b, s.tr("quad", "quadratisch", "quadratic", "cuadrática", "平方"), (0.52, 1.75), groesse=22, ausrichtung="right", farbe=GRAU)
    s.text(b, s.tr("lin", "linear", "linear", "lineal", "线性"), (1.18, 1.25), groesse=22, ausrichtung="right", farbe=ROT)
    s.text(b, s.tr("beide", "beides", "both", "ambos", "两者"), (1.18, 0.6), groesse=22, ausrichtung="right", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k18tunnel():
    """Links: Elektronenwelle an der Isolatorbarriere. Rechts: Dichte des Tunnelstroms über der Isolatordicke."""
    s = Szene("gemb1/k18tunnel")
    a = s.achsen((-1, 3), (-1.4, 3.6), breite=2.75, hoehe=3.0, mitte=(-1.85, 0.1), xl=s.tr("a_weg", "Weg in nm", "path in nm", "recorrido en nm", "路程 / nm"), yl=s.tr("a_ee", "E in eV", "E in eV", "E en eV", "E / eV"),
                 xticks="0;1;2", yticks="-1;0;1;2;3")
    # Weg vom Silizium (links) zum Gate (rechts), Null an der Grenzfläche
    s.band(a, 0, 2, -1.4, 3.6, farbe=GRUEN, deckung=0.12)
    s.linie(a, (-1, 0), (0, 0), farbe=SCHWARZ, dicke=4)
    s.linie(a, (0, 0), (0, 3.15), farbe=SCHWARZ, dicke=4)
    s.linie(a, (0, 3.15), (2, 2.15), farbe=SCHWARZ, dicke=4)
    s.linie(a, (2, 2.15), (2, -1.0), farbe=SCHWARZ, dicke=4)
    s.band(a, 2, 3, -1.4, -1.0, farbe=GRAU, deckung=0.45)
    s.linie(a, (2, -1.0), (3, -1.0), farbe=ROT, dicke=3, dash=DASH)
    k0 = 5.30
    xw = np.linspace(-1, 0, 60)
    s.daten(a, [(x, 0.1 + 0.45 * np.cos(7 * x)) for x in xw], farbe=BLAU, dicke=3.5)
    xw = np.linspace(0, 2, 40)
    s.daten(a, [(x, 0.1 + 0.45 * exp(-k0 * x)) for x in xw], farbe=BLAU, dicke=3.5)
    s.text(a, "Si", (-0.5, 3.2), groesse=24, ausrichtung="center")
    s.text(a, "SiO_2", (1.0, -1.1), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(a, "Gate", (2.5, 3.2), groesse=24, ausrichtung="center")
    s.text(a, "E_C", (-0.95, -0.28), groesse=22, ausrichtung="left")
    s.text(a, "3.15 eV", (0.12, 3.38), groesse=22, ausrichtung="left")
    s.text(a, "\u03c8", (-0.55, 0.85), groesse=24, ausrichtung="center", farbe=BLAU)
    PhiB, E0, VIS = 3.15, 0.1, 1.0
    b = s.achsen((0.8, 3.0), (1e-8, 1e4), breite=2.7, hoehe=3.0, mitte=(1.9, 0.1), xl=achse(s, "d_{IS}", "nm"), yl=s.tr("a_j", "J_G in A/cm^2", "J_G in A/cm^2", "J_G en A/cm^2", "J_G / (A/cm^2)"),
                 ylog=True, xticks="1;1.5;2;2.5;3", yticks="1e-8;1e-6;1e-4;1e-2;1;100;1e4", gitter=True)
    pre = R.e * (R.CIS * (R.VDD - R.VTHL) / R.e) * (2e5 / (2 * 3e-9)) * 1e-4
    V0 = PhiB - VIS / 2

    def Tn(d):
        kap = sqrt(2 * 0.42 * R.m0 * (V0 - E0) * R.e) / R.hq
        return 16 * E0 / V0 * (1 - E0 / V0) * exp(-2 * kap * d)

    ds = np.linspace(0.8, 3.0, 45)
    s.daten(b, [(d, pre * Tn(d * 1e-9)) for d in ds], farbe=BLAU, dicke=4.5)
    s.punkt(b, 2.0, pre * Tn(2e-9), farbe=ROT)
    s.punkt(b, 1.2, pre * Tn(1.2e-9), farbe=ROT)
    s.text(b, "0.016", (2.08, 0.09), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(b, "80", (1.28, 300), groesse=22, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k18gates():
    """Vier Querschnitte quer zum Strom: Gate oben, beidseitig, Finne, rundum."""
    s = Szene("gemb1/k18gates")
    s.welt()
    GATE, OX, KAN = "#6b6b6b", GRUEN, ORANGE

    def titel(x, de, en, es, zh, key, n):
        t(s, s.tr(key, de, en, es, zh), (x, 1.75), g=22)
        t(s, "N = %s" % n, (x, -1.35), g=24, farbe=ROT)

    # planar
    x = -2.5
    s.band(None, x - 0.75, x + 0.75, -0.9, 0.3, farbe=GRAU, deckung=0.2)
    s.band(None, x - 0.75, x + 0.75, -0.25, 0.3, farbe=KAN, deckung=0.55)
    s.band(None, x - 0.75, x + 0.75, 0.3, 0.42, farbe=OX, deckung=0.6)
    s.band(None, x - 0.75, x + 0.75, 0.42, 1.0, farbe=GATE, deckung=0.8)
    titel(x, "planar", "planar", "planar", "平面型", "n1", "1")
    s.pfeil((x - 0.87, -0.25), (x - 0.87, 0.3), "", farbe=SCHWARZ, dicke=2.5, spitze=0.1, doppelt=True)
    t(s, "d_{ch}", (x - 0.95, 0.03), a="right", g=22)
    # Doppelgate
    x = -0.8
    s.band(None, x - 0.65, x + 0.65, -0.1, 0.25, farbe=KAN, deckung=0.8)
    s.band(None, x - 0.65, x + 0.65, 0.25, 0.37, farbe=OX, deckung=0.6)
    s.band(None, x - 0.65, x + 0.65, -0.22, -0.1, farbe=OX, deckung=0.6)
    s.band(None, x - 0.65, x + 0.65, 0.37, 0.95, farbe=GATE, deckung=0.8)
    s.band(None, x - 0.65, x + 0.65, -0.8, -0.22, farbe=GATE, deckung=0.8)
    titel(x, s_doppel[0], s_doppel[1], s_doppel[2], s_doppel[3], "n2", "2")
    # Finne
    x = 0.85
    s.band(None, x - 0.8, x + 0.8, -0.9, -0.45, farbe=BLAU, deckung=0.3)
    s.band(None, x - 0.62, x + 0.62, -0.45, 1.1, farbe=GATE, deckung=0.8)
    s.band(None, x - 0.3, x + 0.3, -0.45, 0.72, farbe=OX, deckung=1.0)
    s.band(None, x - 0.18, x + 0.18, -0.45, 0.6, farbe=KAN, deckung=1.0)
    titel(x, "FinFET", "FinFET", "FinFET", "FinFET", "n3", "2 \u2026 3")
    # Draht
    x = 2.45
    s.kreis(None, x, 0.1, 0.8, farbe=GATE, dicke=2, fuellung=GATE, deckung=0.8)
    s.kreis(None, x, 0.1, 0.42, farbe=OX, dicke=2, fuellung=OX, deckung=1.0)
    s.kreis(None, x, 0.1, 0.3, farbe=KAN, dicke=2, fuellung=KAN, deckung=1.0)
    titel(x, s_draht[0], s_draht[1], s_draht[2], s_draht[3], "n4", "4")
    # Legende
    y = -1.95
    for i, (f, key, de, en, es, zh, deck) in enumerate(((GATE, "lg", "Gate", "gate", "puerta", "栅极", 0.8), (OX, "li", "Isolator", "insulator", "aislante", "绝缘体", 0.6),
                                                        (KAN, "lk", "Kanal", "channel", "canal", "沟道", 0.8))):
        xx = -2.6 + i * 2.1
        s.band(None, xx, xx + 0.4, y - 0.13, y + 0.13, farbe=f, deckung=deck)
        t(s, s.tr(key, de, en, es, zh), (xx + 0.5, y), a="left", g=22)
    s.speichern()


s_doppel = ("Doppelgate", "double gate", "doble puerta", "双栅")
s_draht = ("Nanodraht", "nanowire", "nanohilo", "纳米线")

if __name__ == "__main__":
    k18gut()
    k18skal()
    k18zonen()
    k18barriere()
    k18clm()
    k18vsat()
    k18tunnel()
    k18gates()
