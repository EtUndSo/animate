"""GEMB 1 Teil 19 (kap19_stufen.tex): Ergänzung: Licht und Laser.

Aufruf: python tools/szenen/gemb1_teil19.py, danach python tools/szenen_ansehen.py out.png gemb1/k19uebergaenge ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap19.py.
"""
import sys
from math import hypot, pi
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
VIOLETT, BLAUGRUEN, GELBGRUEN = "#6a3fb5", "#0f9d8a", "#8f9c00"
E2, E3 = 1.80, 2.40                     # Rechenmodell in eV
EG, FAK = 1.74, 11.18                   # CdSe: Lücke in eV, Vorfaktor in eV nm^2
C1 = 0.3760                             # hbar^2 pi^2/(2 m0) in eV nm^2
MC, MV = 0.13, 0.45
UV = 3.40                               # 365 nm in eV


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR, on=None):
    s.text(on, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    return s.tr("a_" + name.replace("\\", "") + einheit, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def poly(s, on, ecken, farbe, deckung=0.2, rand=None, dicke=2):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": rand or farbe, "fill_color": farbe,
                              "fill_opacity": deckung, "stroke_width": dicke}, on)


def ring(s, x, y, r=0.085, farbe=BLAU, on=None):
    return s._add("Dot", {"center": [x, y, 0], "radius": r, "color": farbe, "fill_color": "#ffffff", "fill_opacity": 1, "stroke_width": 2.5}, on)


def photon(s, a, b, farbe, n=4, amp=0.07, dicke=2.5, spitze=0.15):
    """Wellenlinie von a nach b mit Pfeilspitze am Ende."""
    L = hypot(b[0] - a[0], b[1] - a[1])
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    nx, ny = -uy, ux
    W = L - 0.13
    w = 2 * pi * n
    fx = "%.5f+%.5f*t+%.5f*sin(%.4f*t)" % (a[0], W * ux, amp * nx, w)
    fy = "%.5f+%.5f*t+%.5f*sin(%.4f*t)" % (a[1], W * uy, amp * ny, w)
    s.weg(None, fx, fy, 0, 1, farbe=farbe, dicke=dicke, n=121)
    s.pfeil((a[0] + (W - 0.04) * ux, a[1] + (W - 0.04) * uy), b, "", farbe=farbe, dicke=dicke, spitze=spitze)


# ------------------------------------------------------------------------------------------ Stufe 1
def k19uebergaenge():
    """Absorption und Emission im Rechenmodell, Höhen maßstäblich."""
    s = Szene("gemb1/k19uebergaenge")

    def y(E):
        return -1.3 + 1.05 * E
    Y1, Y2, Y3 = y(0), y(E2), y(E3)
    for x0, x1 in ((-3.5, -0.85), (-0.5, 2.85)):
        for Y in (Y1, Y2, Y3):
            s.linie(None, (x0, Y), (x1, Y), farbe=SCHWARZ, dicke=3)
    for Y, n in ((Y1, "E_1"), (Y2, "E_2"), (Y3, "E_3")):
        t(s, n, (-3.72, Y), g=24)
    t(s, s.tr("abs", "Absorption", "absorption", "absorción", "吸收"), (-2.2, 1.65), g=26)
    t(s, s.tr("emi", "Emission", "emission", "emisión", "发射"), (1.2, 1.65), g=26)

    def hoch(x, a, b, farbe, lab, dm=0.0, dl=0.27):
        s.pfeil((x, a + 0.07), (x, b - 0.03), "", farbe=BLAU, dicke=3.5, spitze=0.17)
        m = (a + b) / 2 + dm
        photon(s, (x - 0.55, m), (x - 0.06, m), farbe, n=3)
        t(s, lab, (x - 0.32, m + dl), g=22, farbe=farbe)

    def runter(x, a, b, farbe, lab, dm=0.0, dl=0.27):
        s.pfeil((x, a - 0.07), (x, b + 0.03), "", farbe=BLAU, dicke=3.5, spitze=0.17)
        m = (a + b) / 2 + dm
        photon(s, (x + 0.06, m), (x + 0.55, m), farbe, n=3)
        t(s, lab, (x + 0.32, m + dl), g=22, farbe=farbe)

    h21, h31, h32 = "\\hbar\\omega_{21}", "\\hbar\\omega_{31}", "\\hbar\\omega_{32}"
    hoch(-3.0, Y1, Y2, ROT, h21)
    s.punkt(None, -3.0, Y1, farbe=BLAU)
    hoch(-2.1, Y1, Y3, GRUEN, h31)
    s.punkt(None, -2.1, Y1, farbe=BLAU)
    hoch(-1.2, Y1, Y2, ROT, h21)
    hoch(-1.2, Y2, Y3, ORANGE, h32, dm=-0.14, dl=0.24)
    s.punkt(None, -1.2, Y1, farbe=BLAU)

    runter(-0.2, Y2, Y1, ROT, h21)
    s.punkt(None, -0.2, Y2, farbe=BLAU)
    runter(0.7, Y3, Y1, GRUEN, h31)
    s.punkt(None, 0.7, Y3, farbe=BLAU)
    runter(1.6, Y2, Y1, ROT, h21)
    runter(1.6, Y3, Y2, ORANGE, h32, dm=-0.14, dl=0.24)
    s.punkt(None, 1.6, Y3, farbe=BLAU)
    s.pfeil((2.5, Y2 - 0.07), (2.5, Y1 + 0.03), "", farbe=GRAU, dicke=3.5, spitze=0.17, dash=DASH)
    s.punkt(None, 2.5, Y2, farbe=BLAU)
    t(s, s.tr("waerme", "Wärme", "heat", "calor", "热"), (2.58, (Y1 + Y2) / 2), a="left", g=23, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k19nanokristall():
    """Links Ablauf der Fluoreszenz in zwei Würfeln, rechts Photonenenergie über der Kante."""
    s = Szene("gemb1/k19nanokristall")
    s.welt()

    def y(E):
        return -1.45 + 0.75 * E
    yC, yV = y(EG), y(0)
    for Y, n in ((yC, "E_C"), (yV, "E_V")):
        s.linie(None, (-3.45, Y), (-0.45, Y), farbe=GRAU, dicke=2, dash=DASH)
        t(s, n, (-3.68, Y), g=22, farbe=GRAU)

    def saeule(x, L, farbe, name):
        e = EG + 3 * C1 / (MC * L**2)
        h = -3 * C1 / (MV * L**2)
        o = h + UV
        ye, yh, yo = y(e), y(h), y(o)
        for Y, f in ((ye, SCHWARZ), (yh, SCHWARZ), (yo, GRAU)):
            s.linie(None, (x - 0.46, Y), (x + 0.46, Y), farbe=f, dicke=3)
        s.pfeil((x - 0.3, yh + 0.04), (x - 0.3, yo - 0.03), "", farbe=VIOLETT, dicke=3.5, spitze=0.16)
        s.pfeil((x, yo - 0.05), (x, ye + 0.03), "", farbe=GRAU, dicke=3, spitze=0.15, dash=DASH)
        s.pfeil((x + 0.3, ye - 0.04), (x + 0.3, yh + 0.03), "", farbe=farbe, dicke=3.5, spitze=0.16)
        m = (ye + yh) / 2
        photon(s, (x + 0.34, m), (x + 0.72, m), farbe, n=2, amp=0.06)
        t(s, name, (x, yh - 0.36), g=22)

    saeule(-2.75, 7, ROT, "L = 7 nm")
    saeule(-1.35, 4, BLAUGRUEN, "L = 4 nm")
    t(s, "UV", (-3.05, y(UV - 0.05) + 0.2), g=22, farbe=VIOLETT)
    t(s, "UV", (-1.65, y(UV - 0.16) + 0.2), g=22, farbe=VIOLETT)

    a = s.achsen((2.5, 10), (1.5, 3.2), breite=2.75, hoehe=2.15, mitte=(1.75, -0.15), xl=achse(s, "L", "nm"), yl=achse(s, "\\hbar\\omega", "eV"),
                 xticks="3;4;5;6;7;8;9;10", yticks="1.5;2;2.5;3")
    s.linie(a, (2.5, EG), (10, EG), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "E_g", (9.2, EG - 0.12), groesse=22, ausrichtung="center", farbe=GRAU)
    s.kurve(a, "1.74+11.18/(x*x)", x=(2.92, 10), farbe=BLAU, dicke=4.5)
    for L, f, nm in ((3, VIOLETT, 416), (4, BLAUGRUEN, 508), (5, GELBGRUEN, 567), (7, ROT, 630)):
        w = EG + FAK / L**2
        s.punkt(a, L, w, farbe=f, r=0.085)
        s.text(a, "%d nm" % nm, (L + 0.35, w + 0.1), groesse=22, ausrichtung="left", farbe=f)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k19drei():
    """Absorption, spontane und stimulierte Emission."""
    s = Szene("gemb1/k19drei")
    yo, yu = 0.75, -0.65
    xs = (-2.3, 0.0, 2.3)
    tit = (s.tr("t1", "Absorption", "absorption", "absorción", "吸收"), s.tr("t2", "spontane Emission", "spontaneous emission", "emisión espontánea", "自发发射"),
           s.tr("t3", "stimulierte Emission", "stimulated emission", "emisión estimulada", "受激发射"))
    ph = s.tr("ph", "Photonen", "photons", "fotones", "光子数")
    zahl = ("1 \\to 0", "0 \\to 1", "1 \\to 2")
    for x, ti, z in zip(xs, tit, zahl):
        s.linie(None, (x - 1.02, yo), (x + 1.02, yo), dicke=3)
        s.linie(None, (x - 1.02, yu), (x + 1.02, yu), dicke=3)
        t(s, ti, (x, 1.3), g=25)
        t(s, "@{ph}: " + z, (x, -1.13), g=23)
    t(s, "E_2", (xs[0] - 1.22, yo), g=24)
    t(s, "E_1", (xs[0] - 1.22, yu), g=24)
    lab = "\\hbar\\omega_{21}"
    # Absorption
    x = xs[0]
    s.pfeil((x, yu + 0.09), (x, yo - 0.1), "", farbe=BLAU, dicke=3.5, spitze=0.18)
    s.punkt(None, x, yu, farbe=BLAU, r=0.1)
    ring(s, x, yo, r=0.1)
    photon(s, (x - 0.95, 0.05), (x - 0.08, 0.05), ROT, n=5)
    t(s, lab, (x - 0.55, 0.36), g=22, farbe=ROT)
    # spontan
    x = xs[1]
    s.pfeil((x, yo - 0.09), (x, yu + 0.1), "", farbe=BLAU, dicke=3.5, spitze=0.18)
    s.punkt(None, x, yo, farbe=BLAU, r=0.1)
    ring(s, x, yu, r=0.1)
    photon(s, (x + 0.1, -0.1), (x + 0.92, 0.5), ROT, n=5)
    t(s, lab, (x + 0.6, -0.25), g=22, farbe=ROT)
    # stimuliert
    x = xs[2]
    s.pfeil((x, yo - 0.09), (x, yu + 0.1), "", farbe=BLAU, dicke=3.5, spitze=0.18)
    s.punkt(None, x, yo, farbe=BLAU, r=0.1)
    ring(s, x, yu, r=0.1)
    photon(s, (x - 0.95, 0.05), (x - 0.08, 0.05), ROT, n=5)
    t(s, lab, (x - 0.55, 0.36), g=22, farbe=ROT)
    photon(s, (x + 0.1, 0.27), (x + 0.97, 0.27), ROT, n=5)
    photon(s, (x + 0.1, -0.17), (x + 0.97, -0.17), ROT, n=5)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k19umkehr():
    """Links zwei Besetzungen und ihre Wirkung auf das Licht, rechts N2/N mit zwei Niveaus."""
    s = Szene("gemb1/k19umkehr")
    s.welt()
    yo, yu = 0.8, -0.15

    def teil(x, oben, unten, titel, zeile, a0, k):
        s.linie(None, (x - 0.85, yo), (x + 0.85, yo), dicke=3)
        s.linie(None, (x - 0.85, yu), (x + 0.85, yu), dicke=3)
        t(s, titel, (x, 1.35), g=24)
        for Y, n in ((yo, oben), (yu, unten)):
            for i in range(n):
                s.punkt(None, x + (i - (n - 1) / 2) * 0.19, Y + 0.13, farbe=BLAU, r=0.07)
        w = 2 * pi * 6
        x0, W = x - 0.85, 1.57
        s.weg(None, "%.4f+%.4f*t" % (x0, W), "-0.72+%.4f*exp(%.3f*t)*sin(%.4f*t)" % (a0, k, w), 0, 1, farbe=ROT, dicke=2.5, n=241)
        s.pfeil((x0 + W - 0.03, -0.72), (x + 0.85, -0.72), "", farbe=ROT, dicke=2.5, spitze=0.14)
        t(s, zeile, (x, -1.25), g=23)

    t(s, "E_2", (-3.66, yo), g=24)
    t(s, "E_1", (-3.66, yu), g=24)
    teil(-2.6, 2, 8, s.tr("gg", "Gleichgewicht", "equilibrium", "equilibrio", "平衡"), s.tr("sw", "Licht schwächer", "light weakens", "luz más débil", "光减弱"), 0.2, -1.2)
    teil(-0.75, 7, 3, s.tr("um", "Umkehr", "inversion", "inversión", "反转"), s.tr("st", "Licht stärker", "light grows", "luz más fuerte", "光增强"), 0.06, 1.2)
    a = s.achsen((0.01, 100), (0, 0.6), breite=2.3, hoehe=1.75, mitte=(1.9, 0.12), xl="r_{st}\\tau_{21}", yl="N_2/N", xlog=True, gitter=True, rahmen=True, yticks="0;0.1;0.2;0.3;0.4;0.5;0.6")
    X = np.logspace(-2, 2, 81)
    s.daten(a, [(float(x), float(x / (1 + 2 * x))) for x in X], farbe=BLAU, dicke=4.5)
    s.linie(a, (0.01, 0.5), (100, 0.5), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(a, s.tr("gl", "Gleichstand", "parity", "igualdad", "相等"), (0.02, 0.445), groesse=22, ausrichtung="left", farbe=ROT)
    for x in (1, 10):
        s.punkt(a, x, x / (1 + 2 * x), farbe=BLAU, r=0.08)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k19laser():
    """Oben die zwei Varianten, unten Resonator und Vergleich der Besetzung."""
    s = Szene("gemb1/k19laser")
    s.welt()

    def y(E):
        return 0.4 + 0.95 * E
    Y1, Y2, Y3 = y(0), y(E2), y(E3)

    def rahmen(x, titel):
        for Y, n in ((Y1, "E_1"), (Y2, "E_2"), (Y3, "E_3")):
            s.linie(None, (x - 1.2, Y), (x + 1.25, Y), dicke=3)
            t(s, n, (x - 1.42, Y), g=23)
        t(s, titel, (x + 0.05, 3.1), g=24)
        s.pfeil((x - 0.7, Y1 + 0.05), (x - 0.7, Y3 - 0.03), "", farbe=GRUEN, dicke=4, spitze=0.18)
        photon(s, (x - 1.2, 1.0), (x - 0.75, 1.0), GRUEN, n=3)
        t(s, "\\hbar\\omega_{31}", (x - 1.05, 1.28), g=22, farbe=GRUEN)

    def verstaerkt(x, a, b, lab):
        s.pfeil((x, a - 0.04), (x, b + 0.03), "", farbe=ROT, dicke=4, spitze=0.18)
        m = (a + b) / 2
        photon(s, (x - 0.42, m), (x - 0.05, m), ROT, n=2, amp=0.06)
        photon(s, (x + 0.05, m + 0.14), (x + 0.75, m + 0.14), ROT, n=4, amp=0.05)
        photon(s, (x + 0.05, m - 0.14), (x + 0.75, m - 0.14), ROT, n=4, amp=0.05)
        t(s, lab, (x + 0.78, m), a="left", g=22, farbe=ROT)

    schnell = s.tr("sn", "schnell", "fast", "rápido", "快")
    waerme = s.tr("wa", "Wärme", "heat", "calor", "热")
    # Variante 1
    x = -1.8
    rahmen(x, s.tr("v1", "Variante 1", "variant 1", "variante 1", "方案 1"))
    verstaerkt(x + 0.05, Y3, Y2, "\\hbar\\omega_{32}")
    s.pfeil((x + 0.05, Y2 - 0.05), (x + 0.05, Y1 + 0.03), "", farbe=GRAU, dicke=3.5, spitze=0.16, dash=DASH)
    t(s, schnell, (x + 0.17, 1.42), a="left", g=22, farbe=GRAU)
    t(s, waerme, (x + 0.17, 1.1), a="left", g=22, farbe=GRAU)
    # Variante 2
    x = 1.72
    rahmen(x, s.tr("v2", "Variante 2", "variant 2", "variante 2", "方案 2"))
    s.pfeil((x + 0.05, Y3 - 0.05), (x + 0.05, Y2 + 0.03), "", farbe=GRAU, dicke=3.5, spitze=0.16, dash=DASH)
    t(s, schnell, (x + 0.17, (Y2 + Y3) / 2), a="left", g=22, farbe=GRAU)
    verstaerkt(x + 0.05, Y2, Y1, "\\hbar\\omega_{21}")

    # Resonator
    yc = -1.15
    poly(s, None, [(-2.95, yc - 0.35), (-1.0, yc - 0.35), (-1.0, yc + 0.35), (-2.95, yc + 0.35)], ROT, deckung=0.14, rand=ROT, dicke=2)
    s.linie(None, (-3.25, yc - 0.6), (-3.25, yc + 0.6), dicke=7)
    s.linie(None, (-0.7, yc - 0.6), (-0.7, yc + 0.6), farbe=GRAU, dicke=4)
    s.pfeil((-3.2, yc - 0.1), (-0.75, yc - 0.1), "", farbe=ROT, dicke=3, spitze=0.15)
    s.pfeil((-0.75, yc + 0.1), (-3.2, yc + 0.1), "", farbe=ROT, dicke=3, spitze=0.15)
    s.pfeil((-0.68, yc), (0.05, yc), "", farbe=ROT, dicke=4.5, spitze=0.2)
    t(s, s.tr("strahl", "Strahl", "beam", "haz", "光束"), (-0.3, yc + 0.28), g=22, farbe=ROT)
    for xp in (-2.55, -1.97, -1.4):
        s.pfeil((xp, yc + 1.0), (xp, yc + 0.4), "", farbe=GRUEN, dicke=3.5, spitze=0.15)
    t(s, s.tr("pu", "Pumpen", "pumping", "bombeo", "泵浦"), (-1.97, yc + 1.2), g=22, farbe=GRUEN)
    t(s, s.tr("spiegel", "Spiegel", "mirror", "espejo", "反射镜"), (-3.1, yc - 0.85), g=22)
    t(s, s.tr("teil", "teildurchlässig", "partly transparent", "semitransparente", "半透"), (-0.75, yc - 0.85), g=22)

    # Vergleich
    a = s.achsen((0.01, 100), (0, 1), breite=2.4, hoehe=1.55, mitte=(2.0, -1.05), xl="r\\tau_{21}", yl="N_2/N", xlog=True, gitter=True, rahmen=True, yticks="0;0.5;1")
    X = np.logspace(-2, 2, 81)
    s.daten(a, [(float(x), float(x / (1 + 2 * x))) for x in X], farbe=BLAU, dicke=4.5)
    s.daten(a, [(float(x), float(x / (1 + x))) for x in X], farbe=ROT, dicke=4.5)
    s.linie(a, (0.01, 0.5), (100, 0.5), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, s.tr("n3", "drei Niveaus", "three levels", "tres niveles", "三能级"), (0.014, 0.8), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(a, s.tr("n2", "zwei Niveaus", "two levels", "dos niveles", "二能级"), (1.3, 0.2), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


if __name__ == "__main__":
    k19uebergaenge()
    k19nanokristall()
    k19drei()
    k19umkehr()
    k19laser()
