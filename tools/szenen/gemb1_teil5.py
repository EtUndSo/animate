"""GEMB 1, Teil 5 (kap5_stufen.tex): Chemische Bindung.

Aufruf: python tools/szenen/gemb1_teil5.py, danach python tools/szenen_ansehen.py out.png gemb1/k5kurve ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap5.py.
"""
import sys
from math import cos, pi, radians, sin, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
GROSS = 24
C = 1.44                  # e^2/(4 pi eps0) in eV nm


def viel(s, ecken, farbe=BLAU, deckung=0.35, rand=2.0, fuellung=None):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": farbe, "fill_color": fuellung or farbe,
                              "fill_opacity": deckung, "stroke_width": rand}, None)


def keule(s, x0, y0, winkel, laenge, breite=0.5, farbe=BLAU, deckung=0.4, n=48):
    """Tropfenförmige Keule vom Punkt (x0, y0) aus in Richtung winkel (Grad)."""
    w = radians(winkel)
    pk = []
    for i in range(n):
        t = 2 * pi * i / n
        u = laenge * (1 + cos(t)) / 2
        v = breite * laenge * sin(t) * (1 + cos(t)) / 2
        pk.append((x0 + u * cos(w) - v * sin(w), y0 + u * sin(w) + v * cos(w)))
    return viel(s, pk, farbe=farbe, deckung=deckung)


def ellipse(s, x0, y0, a, b, farbe=BLAU, deckung=0.35, winkel=0.0, n=60, rand=2.0):
    w = radians(winkel)
    pk = []
    for i in range(n):
        t = 2 * pi * i / n
        u, v = a * cos(t), b * sin(t)
        pk.append((x0 + u * cos(w) - v * sin(w), y0 + u * sin(w) + v * cos(w)))
    return viel(s, pk, farbe=farbe, deckung=deckung, rand=rand)


def kaestchen(s, x, y, belegung, a=0.32):
    """Orbital als Kästchen; belegung: "ud", "u", "d", ""."""
    s.box("", (x, y), breite=a, hoehe=a, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0, dicke=2.5)
    if "u" in belegung:
        dx = -0.07 if len(belegung) == 2 else 0
        s.pfeil((x + dx, y - 0.12), (x + dx, y + 0.12), "", spitze=0.09, dicke=2.5, farbe=ROT)
    if "d" in belegung:
        dx = 0.07 if len(belegung) == 2 else 0
        s.pfeil((x + dx, y + 0.12), (x + dx, y - 0.12), "", spitze=0.09, dicke=2.5, farbe=BLAU)


def nullstelle(f, a, b):
    fa = f(a)
    for _ in range(100):
        m = (a + b) / 2
        if f(m) * fa > 0:
            a, fa = m, f(m)
        else:
            b = m
    return (a + b) / 2


# ------------------------------------------------------------------------------------------ Stufe 1
def k5kurve():
    """Kraft und Energie eines Paars, rechts die Mulde mit den Umkehrpunkten bei drei Temperaturen."""
    s = Szene("gemb1/k5kurve")
    s.welt()
    fan = lambda x: -1.125 / x**2
    fab = lambda x: 1.125 / x**10
    x0 = (0.6, 2.6)
    a = s.achsen((0.6, 2.6, 0.4), (-3, 3, 1.5), breite=2.7, hoehe=1.25, mitte=(-1.75, 1.08), xl="", yl="F r_0 / E_B", yticks="-3;0;3",
                 xzahlen=False)
    s.linie(a, (0.6, 0), (2.6, 0), farbe=GRAU, dicke=2)
    s.linie(a, (1, -3), (1, 3), farbe=GRAU, dicke=2.5, dash=DASH)
    x_ab = nullstelle(lambda x: fab(x) - 2.9, 0.7, 1.2)
    x_ges = nullstelle(lambda x: fab(x) + fan(x) - 2.9, 0.7, 1.2)
    x_an = nullstelle(lambda x: fan(x) + 2.9, 0.5, 1.2)
    s.kurve(a, "1.125/x^10", x=(x_ab, 2.6), farbe=ORANGE, dicke=3.5)
    s.kurve(a, "-1.125/x^2", x=(x_an, 2.6), farbe=GRUEN, dicke=3.5)
    s.kurve(a, "1.125/x^10-1.125/x^2", x=(x_ges, 2.6), farbe=BLAU)
    s.text(a, "F_{ab}", (1.13, 2.2), farbe=ORANGE, groesse=GROSS)
    s.text(a, "F_{an}", (1.45, -1.55), farbe=GRUEN, groesse=GROSS, ausrichtung="left")
    s.text(a, "F", (1.75, 0.55), farbe=BLAU, groesse=GROSS, ausrichtung="center")

    b = s.achsen((0.6, 2.6, 0.4), (-2, 2, 1), breite=2.7, hoehe=1.45, mitte=(-1.75, -0.8), xl="r / r_0", yl="E / E_B", yticks="-2;-1;0;1;2")
    s.linie(b, (0.6, 0), (2.6, 0), farbe=GRAU, dicke=2)
    s.linie(b, (1, -2), (1, 2), farbe=GRAU, dicke=2.5, dash=DASH)
    eab = lambda x: 0.125 / x**9
    ean = lambda x: -1.125 / x
    x_ab = nullstelle(lambda x: eab(x) - 1.95, 0.6, 1.2)
    x_ges = nullstelle(lambda x: eab(x) + ean(x) - 1.95, 0.6, 1.2)
    x_an = nullstelle(lambda x: ean(x) + 1.95, 0.5, 1.2)
    s.kurve(b, "0.125/x^9", x=(x_ab, 2.6), farbe=ORANGE, dicke=3.5)
    s.kurve(b, "-1.125/x", x=(x_an, 2.6), farbe=GRUEN, dicke=3.5)
    s.kurve(b, "0.125/x^9-1.125/x", x=(x_ges, 2.6), farbe=BLAU)
    s.punkt(b, 1, -1, farbe=ROT, r=0.07)
    s.text(b, "E_{ab}", (1.12, 0.5), farbe=ORANGE, groesse=GROSS, ausrichtung="left")
    s.text(b, "E_{an}", (1.5, -1.25), farbe=GRUEN, groesse=GROSS, ausrichtung="left")
    s.text(b, "E_{pot}", (2.0, -0.2), farbe=BLAU, groesse=GROSS, ausrichtung="center")
    s.text(b, "r_0", (1.06, 1.6), groesse=GROSS)

    # Rechts: die Mulde des Modellpaars in meV über dem Minimum
    r0, Kab, EB = 0.267, 4.132e-6, 4.794
    ek = lambda r: -C / r + Kab / r**9 + EB
    c = s.achsen((0.24, 0.32, 0.02), (0, 200, 50), breite=2.6, hoehe=2.4, mitte=(2.0, 0.12), xl=s.tr("rnm", "r in nm", "r in nm", "r en nm", "r / nm"),
                 yl="E_{pot} + E_B  in meV", xticks="0.24;0.28;0.32", yticks="0;100;200")
    xl = nullstelle(lambda r: ek(r) * 1000 - 200, 0.2, r0)
    s.kurve(c, f"1000*(-1.44/x+{Kab}/x^9+{EB})", x=(xl, 0.32), farbe=BLAU)
    s.linie(c, (r0, 0), (r0, 200), farbe=GRAU, dicke=2.5, dash=DASH)
    mitten = []
    for T in (300, 1000, 2000):
        de = 8.617333e-5 * T
        rm = nullstelle(lambda r: ek(r) - de, 0.2, r0)
        rp = nullstelle(lambda r: ek(r) - de, r0, 0.4)
        s.linie(c, (rm, de * 1000), (rp, de * 1000), farbe=ROT, dicke=3)
        s.punkt(c, (rm + rp) / 2, de * 1000, farbe=ROT, r=0.065)
        mitten.append(((rm + rp) / 2, de * 1000))
    s.text(c, "300 K", (0.2895, 10), farbe=ROT, groesse=GROSS, ausrichtung="center")
    s.text(c, "1000 K", (0.3005, 84), farbe=ROT, groesse=GROSS, ausrichtung="center")
    s.text(c, "2000 K", (0.3095, 154), farbe=ROT, groesse=GROSS, ausrichtung="center")
    s.text(c, "r_0", (0.2685, 192), groesse=GROSS)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k5bilanz():
    """Elektronenübergang von K nach Cl und Energiebilanz."""
    s = Szene("gemb1/k5bilanz")
    # links: Elektronen
    x_k, y_o = -3.05, 0.95
    s.text(None, "K: [Ar] 4s^1", (-3.0, 1.5), ausrichtung="center", groesse=GROSS)
    s.text(None, "Cl: [Ne] 3s^2 3p^5", (-1.4, 1.5), ausrichtung="center", groesse=GROSS)
    s.text(None, "4s", (x_k - 0.33, y_o), ausrichtung="right", groesse=GROSS)
    kaestchen(s, x_k, y_o, "u")
    xs = -2.1
    s.text(None, "3s", (xs - 0.33 + 0.1, y_o), ausrichtung="right", groesse=GROSS)
    kaestchen(s, xs + 0.1, y_o, "ud")
    s.text(None, "3p", (xs + 0.76, y_o - 0.0), ausrichtung="center", groesse=GROSS)
    for i, b in enumerate(("ud", "ud", "u")):
        kaestchen(s, xs + 1.1 + i * 0.4, y_o, b)
    s.pfeil((x_k + 0.15, y_o + 0.2), (xs + 1.95, y_o + 0.24), "", knick="none", farbe=BLAU, dicke=2.5, spitze=0.12)
    s.text(None, "e^−", (-1.75, 1.22), farbe=BLAU, groesse=GROSS, ausrichtung="center")
    s.pfeil((-2.1, 0.6), (-2.1, 0.25), "", farbe=SCHWARZ, dicke=3, spitze=0.16)
    ellipse(s, -2.85, -0.45, 0.46, 0.46, farbe=ROT, deckung=0.22)
    ellipse(s, -1.35, -0.45, 0.60, 0.60, farbe=BLAU, deckung=0.22)
    s.text(None, "K^+", (-2.85, -0.45), ausrichtung="center", groesse=26)
    s.text(None, "Cl^−", (-1.35, -0.45), ausrichtung="center", groesse=26)
    s.text(None, s.tr("wiear", "beide wie Argon", "both like argon", "ambos como el argón", "都与氩相同"), (-2.1, -1.25), ausrichtung="center", groesse=GROSS)

    # rechts: Energiestufen
    y = lambda e: -1.45 + (e + 6.44) * 0.27

    def stufe(x0, x1, e, txt, farbe=SCHWARZ, unten=False):
        s.linie(None, (x0, y(e)), (x1, y(e)), farbe=farbe, dicke=4.5)
        s.text(None, txt, ((x0 + x1) / 2, y(e) + (-0.2 if unten else 0.2)), ausrichtung="center", groesse=KLEIN, farbe=farbe)

    s.pfeil((-0.1, -1.8), (-0.1, 1.75), "", farbe=GRAU, dicke=2.5, spitze=0.15)
    s.text(None, s.tr("ev", "E in eV", "E in eV", "E en eV", "E / eV"), (0.03, 1.72), groesse=GROSS, farbe=GRAU)
    s.linie(None, (0.0, y(0)), (3.4, y(0)), farbe=HELLGRAU, dicke=1.5, dash=DOT)
    stufe(0.0, 0.9, 0, "K + Cl")
    stufe(0.6, 1.95, 4.34, "K^+ + e^− + Cl")
    stufe(1.6, 3.3, 0.73, "K^+ + Cl^−")
    stufe(1.65, 2.45, -4.06, s.tr("paar", "Ionenpaar", "ion pair", "par iónico", "离子对"), farbe=BLAU, unten=True)
    stufe(2.65, 3.4, -6.44, s.tr("krist", "Salzkristall", "salt crystal", "cristal", "盐晶体"), farbe=ROT, unten=True)
    s.pfeil((0.75, y(0)), (0.75, y(4.34)), "", farbe=SCHWARZ, dicke=2.5, spitze=0.13)
    s.text(None, "+4.34", (0.8, y(2.2)), groesse=GROSS)
    s.pfeil((1.8, y(4.34)), (1.8, y(0.73)), "", farbe=SCHWARZ, dicke=2.5, spitze=0.13)
    s.text(None, "−3.61", (1.85, y(2.6)), groesse=GROSS)
    s.pfeil((2.05, y(0.73)), (2.05, y(-4.06)), "", farbe=BLAU, dicke=2.5, spitze=0.13)
    s.text(None, "−4.79", (2.1, y(-1.8)), groesse=GROSS, farbe=BLAU)
    s.pfeil((3.0, y(0.73)), (3.0, y(-6.44)), "", farbe=ROT, dicke=2.5, spitze=0.13)
    s.text(None, "−7.17", (2.95, y(-3.2)), groesse=GROSS, farbe=ROT, ausrichtung="right")
    s.text(None, "0", (-0.17, y(0)), groesse=GROSS, ausrichtung="right", farbe=GRAU)
    s.text(None, "−4.06", (1.6, y(-4.06)), groesse=GROSS, farbe=BLAU, ausrichtung="right")
    s.text(None, "−6.44", (2.6, y(-6.44)), groesse=GROSS, farbe=ROT, ausrichtung="right")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k5molekuel():
    """Links die Aufspaltung im H2-Molekül, rechts die Elektronendichte auf der Kernachse."""
    s = Szene("gemb1/k5molekuel")
    s.welt()
    xa, xm, xb = -3.0, -1.85, -0.7
    w = 0.3
    y0, ys, yu = 0.1, -0.65, 0.85
    s.pfeil((-3.55, -1.2), (-3.55, 1.55), "", farbe=GRAU, dicke=2.5, spitze=0.15)
    s.text(None, "E", (-3.43, 1.48), groesse=GROSS, farbe=GRAU)
    s.linie(None, (xa + w, y0), (xb - w, y0), farbe=HELLGRAU, dicke=1.5, dash=DOT)
    s.pfeil((xm - 0.42, y0), (xm - 0.42, ys), "", farbe=GRAU, dicke=2, spitze=0.1, doppelt=True)
    s.pfeil((xm - 0.42, y0), (xm - 0.42, yu), "", farbe=GRAU, dicke=2, spitze=0.1, doppelt=True)
    s.text(None, "V_{ss}", (xm - 0.36, (y0 + yu) / 2), groesse=KLEIN, farbe=GRAU)
    s.text(None, "V_{ss}", (xm - 0.36, (y0 + ys) / 2), groesse=KLEIN, farbe=GRAU)
    s.text(None, "E_{AO}", (xb + 0.02, y0 - 0.26), groesse=KLEIN, farbe=GRAU, ausrichtung="center")
    for x, yy in ((xa, y0), (xb, y0), (xm, ys), (xm, yu)):
        s.linie(None, (x - w, yy), (x + w, yy), farbe=SCHWARZ, dicke=5)
    for (a, b) in (((xa + w, y0), (xm - w, ys)), ((xa + w, y0), (xm - w, yu)), ((xb - w, y0), (xm + w, ys)), ((xb - w, y0), (xm + w, yu))):
        s.linie(None, a, b, farbe=ROT, dicke=2, dash=DASH)
    s.pfeil((xa, y0 - 0.17), (xa, y0 + 0.17), "", spitze=0.1, dicke=2.5, farbe=ROT)
    s.pfeil((xb, y0 + 0.17), (xb, y0 - 0.17), "", spitze=0.1, dicke=2.5, farbe=BLAU)
    s.pfeil((xm - 0.08, ys - 0.17), (xm - 0.08, ys + 0.17), "", spitze=0.1, dicke=2.5, farbe=ROT)
    s.pfeil((xm + 0.08, ys + 0.17), (xm + 0.08, ys - 0.17), "", spitze=0.1, dicke=2.5, farbe=BLAU)
    s.text(None, "1s", (xa, y0 + 0.33), ausrichtung="center", groesse=GROSS)
    s.text(None, "1s", (xb, y0 + 0.33), ausrichtung="center", groesse=GROSS)
    s.text(None, "σ", (xm, ys - 0.3), ausrichtung="center", groesse=26, farbe=BLAU)
    s.text(None, "σ^*", (xm, yu + 0.3), ausrichtung="center", groesse=26, farbe=ROT)
    s.text(None, s.tr("bind", "bindend", "bonding", "enlazante", "成键"), (xm + 0.42, ys - 0.02), groesse=KLEIN, farbe=BLAU)
    s.text(None, s.tr("anti", "antibindend", "antibonding", "antienlazante", "反键"), (xm + 0.42, yu + 0.02), ausrichtung="left", groesse=KLEIN, farbe=ROT)
    s.text(None, "H", (xa, -1.28), ausrichtung="center", groesse=GROSS)
    s.text(None, "H_2", (xm, -1.28), ausrichtung="center", groesse=GROSS)
    s.text(None, "H", (xb, -1.28), ausrichtung="center", groesse=GROSS)

    xl = s.tr("xr", "x / r_1", "x / r_1", "x / r_1", "x / r_1")
    an = "(exp(-2*abs(x+0.7))+exp(-2*abs(x-0.7)))/2"
    d1 = "(exp(-abs(x+0.7))+exp(-abs(x-0.7)))^2/3.506"
    d2 = "(exp(-abs(x+0.7))-exp(-abs(x-0.7)))^2/0.494"
    a = s.achsen((-3.5, 3.5, 1), (0, 1.2, 0.4), breite=2.85, hoehe=1.05, mitte=(1.95, 0.85), xl="", yl="|ψ|^2", xticks="-3;0;3", yticks="0;0.4;0.8;1.2", xzahlen=False)
    s.text(a, s.tr("t1", "bindend", "bonding", "enlazante", "成键"), (3.45, 1.08), ausrichtung="right", groesse=KLEIN, farbe=BLAU)
    s.kurve(a, an, farbe=GRAU, dicke=3, dash=DASH)
    s.kurve(a, d1, farbe=BLAU)
    s.punkt(a, -0.7, 0, farbe=SCHWARZ, r=0.06)
    s.punkt(a, 0.7, 0, farbe=SCHWARZ, r=0.06)
    b = s.achsen((-3.5, 3.5, 1), (0, 1.2, 0.4), breite=2.85, hoehe=1.05, mitte=(1.95, -0.82), xl=xl, yl="|ψ|^2", xticks="-3;0;3", yticks="0;0.4;0.8;1.2")
    s.text(b, s.tr("t2", "antibindend", "antibonding", "antienlazante", "反键"), (3.45, 1.08), ausrichtung="right", groesse=KLEIN, farbe=ROT)
    s.kurve(b, an, farbe=GRAU, dicke=3, dash=DASH)
    s.kurve(b, d2, farbe=ROT)
    s.punkt(b, -0.7, 0, farbe=SCHWARZ, r=0.06)
    s.punkt(b, 0.7, 0, farbe=SCHWARZ, r=0.06)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def lappen(s, x, y, art, vz):
    """Orbital am Atom bei (x, y). art "s", "z" (Keulen auf der Achse), "q" (Keulen quer zur Achse). vz=+1: Pluskeule nach rechts/oben."""
    pl, mi = BLAU, ROT
    if art == "s":
        ellipse(s, x, y, 0.36, 0.36, farbe=pl if vz > 0 else mi, deckung=0.42, rand=2)
    else:
        w = 0 if art == "z" else 90
        keule(s, x, y, w, 0.6, 0.62, farbe=pl if vz > 0 else mi)
        keule(s, x, y, w + 180, 0.6, 0.62, farbe=mi if vz > 0 else pl)
    s.punkt(None, x, y, farbe=SCHWARZ, r=0.04)


def zelle(s, x, y, l, r, titel, wert, farbe=SCHWARZ, d=0.86):
    s.linie(None, (x - 1.0, y), (x + 1.0, y), farbe=HELLGRAU, dicke=1.5, dash=DOT)
    lappen(s, x - d / 2, y, *l)
    lappen(s, x + d / 2, y, *r)
    s.text(None, titel, (x, y + 0.78), ausrichtung="center", groesse=GROSS)
    s.text(None, wert, (x, y - 0.8), ausrichtung="center", groesse=GROSS, farbe=farbe)


def k5ueberlapp():
    """Sechs Paare von Orbitalen: Kopplung je nach Lage und Vorzeichen."""
    s = Szene("gemb1/k5ueberlapp")
    dx, y1, y2 = 2.38, 1.0, -1.0
    zelle(s, -dx, y1, ("s", 1), ("s", 1), "s – s:  σ", "−V_{ss}")
    zelle(s, 0, y1, ("s", 1), ("z", -1), "s – p_z:  σ", "−V_{spσ}")
    zelle(s, dx, y1, ("z", 1), ("z", -1), "p_z – p_z:  σ", "−V_{ppσ}", d=1.0)
    zelle(s, -dx, y2, ("q", 1), ("q", 1), "p_x – p_x:  π", "−V_{ppπ}")
    zelle(s, 0, y2, ("s", 1), ("q", 1), "s – p_x", "0", farbe=GRAU)
    zelle(s, dx, y2, ("z", 1), ("q", 1), "p_z – p_x", "0", farbe=GRAU, d=1.0)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def polar(s, x0, y0, f, r, richtung=0.0, plus=BLAU, minus=ROT, deckung=0.42, n=240):
    """Polardiagramm von f(t) mit t = Winkel zur Richtung (Grad). r ist die Länge von |f| = 1. Zusammenhängende Stücke gleichen Vorzeichens."""
    w = radians(richtung)
    werte = [(2 * pi * i / n, f(2 * pi * i / n)) for i in range(n)]
    start = next((i for i in range(n) if werte[i][1] * werte[i - 1][1] < 0), 0)
    werte = werte[start:] + werte[:start]
    stuecke, cur, vz = [], [], None
    for t, v in werte:
        z = 1 if v >= 0 else -1
        if vz is None or z == vz:
            cur.append((t, v))
        else:
            stuecke.append((vz, cur))
            cur = [(t, v)]
        vz = z
    stuecke.append((vz, cur))
    for z, st in stuecke:
        pts = [(x0 + r * abs(v) * cos(t + w), y0 + r * abs(v) * sin(t + w)) for t, v in st]
        if len(st) < n:
            pts.append((x0, y0))
        viel(s, pts, farbe=plus if z > 0 else minus, deckung=deckung)


def projektion():
    """Vier Tetraederrichtungen, gedreht und leicht von oben gesehen: (x, y) je Richtung."""
    v = [(0, 1, 0), (0.9428, -0.3333, 0), (-0.4714, -0.3333, 0.8165), (-0.4714, -0.3333, -0.8165)]
    aus = []
    for x, y, z in v:
        a = radians(38)
        x1 = x * cos(a) + z * sin(a)
        z1 = -x * sin(a) + z * cos(a)
        b = radians(16)
        y1 = y * cos(b) - z1 * sin(b)
        aus.append((x1, y1))
    return aus


def molekuel(s, x0, y0, zentrum, freie, name, winkel):
    """Zentralatom mit vier Tetraederrichtungen; die ersten freie davon tragen ein freies Elektronenpaar."""
    r = 0.78
    richt = projektion()
    for i, (dx, dy) in enumerate(richt):
        x, y = x0 + r * dx, y0 + r * dy
        from math import atan2, degrees
        w = degrees(atan2(dy, dx))
        ist_frei = i < freie
        keule(s, x0, y0, w, r * (dx**2 + dy**2)**0.5 * (0.95 if ist_frei else 1.0), 0.6, farbe=ORANGE if ist_frei else BLAU, deckung=0.4)
        if ist_frei:
            xm, ym = x0 + 0.62 * r * dx, y0 + 0.62 * r * dy
            ux, uy = -dy, dx
            n = (ux**2 + uy**2)**0.5
            s.punkt(None, xm + 0.055 * ux / n, ym + 0.055 * uy / n, farbe=SCHWARZ, r=0.03)
            s.punkt(None, xm - 0.055 * ux / n, ym - 0.055 * uy / n, farbe=SCHWARZ, r=0.03)
        else:
            s.box("H", (x, y), breite=0.3, hoehe=0.3, form="ellipse", groesse=KLEIN, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0, dicke=2)
    s.box(zentrum, (x0, y0), breite=0.32, hoehe=0.32, form="ellipse", groesse=GROSS, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0, dicke=2.5)
    s.text(None, name, (x0, y0 - 1.1), ausrichtung="center", groesse=26)
    s.text(None, winkel, (x0, y0 - 1.42), ausrichtung="center", groesse=GROSS, farbe=ROT)


def k5hybrid():
    """Oben: vom Grundzustand zu vier Hybridorbitalen, s + p = Keule. Unten: CH4, NH3, H2O."""
    s = Szene("gemb1/k5hybrid")
    y_s, y_p, yt = 0.85, 1.5, 2.05
    d = 0.35
    # Grundzustand
    s.text(None, s.tr("gz", "Grundzustand", "ground state", "estado fundamental", "基态"), (-2.95, yt), ausrichtung="center", groesse=KLEIN)
    s.text(None, "2s", (-3.6, y_s), ausrichtung="center", groesse=GROSS)
    kaestchen(s, -3.25, y_s, "ud")
    s.text(None, "2p", (-3.6, y_p), ausrichtung="center", groesse=GROSS)
    for i, b in enumerate(("u", "u", "")):
        kaestchen(s, -3.25 + i * d, y_p, b)
    s.pfeil((-2.5, 1.2), (-2.15, 1.2), "", farbe=SCHWARZ, dicke=2.5, spitze=0.13)
    # angehoben
    s.text(None, s.tr("ang", "angehoben", "promoted", "promovido", "激发"), (-1.6, yt), ausrichtung="center", groesse=KLEIN)
    kaestchen(s, -1.95, y_s, "u")
    for i in range(3):
        kaestchen(s, -1.95 + i * d, y_p, "u")
    s.pfeil((-1.15, 1.2), (-0.8, 1.2), "", farbe=SCHWARZ, dicke=2.5, spitze=0.13)
    # gemischt
    s.text(None, s.tr("gem", "gemischt", "mixed", "mezclado", "混合"), (-0.12, yt), ausrichtung="center", groesse=KLEIN)
    for i in range(4):
        kaestchen(s, -0.62 + i * 0.33, 1.2, "u")
    s.text(None, "4 · sp^3", (-0.12, 0.8), ausrichtung="center", groesse=GROSS)
    # s + p = Keule, gleicher Maßstab
    u = 0.27
    x1, x2, x3 = 0.95, 1.86, 2.84
    ym = 1.3
    polar(s, x1, ym, lambda t: 1.0, u)
    s.text(None, "+", (x1 + 0.37, ym), ausrichtung="center", groesse=26)
    polar(s, x2 - 0.05, ym, lambda t: sqrt(3) * cos(t), u)
    s.text(None, "=", (x2 + 0.52, ym), ausrichtung="center", groesse=26)
    polar(s, x3 - 0.1, ym, lambda t: (1 + 3 * cos(t)) / 2, u)
    s.text(None, "s", (x1, 0.8), ausrichtung="center", groesse=GROSS)
    s.text(None, "p", (x2 - 0.05, 0.8), ausrichtung="center", groesse=GROSS)
    s.text(None, "sp^3", (x3 + 0.1, 0.8), ausrichtung="center", groesse=GROSS)
    # Moleküle
    molekuel(s, -2.55, -0.55, "C", 0, "CH_4", "109.47°")
    molekuel(s, 0, -0.55, "N", 1, "NH_3", "107°")
    molekuel(s, 2.55, -0.55, "O", 2, "H_2O", "104.5°")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def sechseck(s, x0, y0, r, farbe=SCHWARZ, dicke=3, start=30):
    pk = [(x0 + r * cos(radians(start + 60 * i)), y0 + r * sin(radians(start + 60 * i))) for i in range(6)]
    for i in range(6):
        s.linie(None, pk[i], pk[(i + 1) % 6], farbe=farbe, dicke=dicke)
    return pk


def k5doppel():
    """Hybride sp und sp2, Doppelbindung im Ethen, Benzolring und Graphen."""
    s = Szene("gemb1/k5doppel")
    ko = 0.85
    # sp
    x0 = -2.3
    keule(s, x0, ko, 0, 0.85, 0.5, farbe=BLAU)
    keule(s, x0, ko, 180, 0.85, 0.5, farbe=BLAU)
    keule(s, x0, ko, 90, 0.55, 0.5, farbe=GRAU, deckung=0.3)
    keule(s, x0, ko, 270, 0.55, 0.5, farbe=GRAU, deckung=0.3)
    s.punkt(None, x0, ko, farbe=SCHWARZ, r=0.05)
    s.text(None, "sp:  180°", (x0, ko + 0.86), ausrichtung="center", groesse=26)
    s.text(None, s.tr("sp2p", "2 p-Orbitale übrig (eines gezeigt)", "2 p orbitals left (one shown)", "quedan 2 p (se muestra uno)", "余 2 个 p 轨道（示 1 个）"), (x0, ko - 0.86), ausrichtung="center", groesse=KLEIN, farbe=GRAU)
    # sp2
    x1 = 1.6
    for w in (90, 210, 330):
        keule(s, x1, ko - 0.1, w, 0.8, 0.5, farbe=BLAU)
    s.kreis(None, x1, ko - 0.1, 0.12, farbe=GRAU, dicke=2.5)
    s.punkt(None, x1, ko - 0.1, farbe=GRAU, r=0.04)
    s.text(None, "sp^2:  120°", (x1, ko + 0.86), ausrichtung="center", groesse=26)
    s.text(None, s.tr("sp21", "1 p-Orbital übrig, senkrecht", "1 p orbital left, perpendicular", "queda 1 orbital p, perpendicular", "余 1 个 p 轨道，垂直于平面"), (x1, ko - 0.86), ausrichtung="center", groesse=KLEIN, farbe=GRAU)

    y = -1.25
    # Ethen von der Seite
    xe = -2.4
    d = 0.4
    for x in (xe - d, xe + d):
        keule(s, x, y, 90, 0.66, 0.55, farbe=BLAU)
        keule(s, x, y, 270, 0.66, 0.55, farbe=ROT)
    ellipse(s, xe, y + 0.42, 0.72, 0.17, farbe=BLAU, deckung=0.18, rand=1.5)
    ellipse(s, xe, y - 0.42, 0.72, 0.17, farbe=ROT, deckung=0.18, rand=1.5)
    s.linie(None, (xe - d, y), (xe + d, y), farbe=SCHWARZ, dicke=4)
    s.linie(None, (xe - d, y), (xe - d - 0.34, y), farbe=SCHWARZ, dicke=3)
    s.linie(None, (xe + d, y), (xe + d + 0.34, y), farbe=SCHWARZ, dicke=3)
    s.text(None, "2 H", (xe - d - 0.38, y), ausrichtung="right", groesse=KLEIN)
    s.text(None, "2 H", (xe + d + 0.38, y), ausrichtung="left", groesse=KLEIN)
    s.punkt(None, xe - d, y, farbe=SCHWARZ, r=0.06)
    s.punkt(None, xe + d, y, farbe=SCHWARZ, r=0.06)
    s.text(None, "σ", (xe, y + 0.1), ausrichtung="center", groesse=KLEIN)
    s.text(None, "π", (xe + 0.0, y + 0.82), ausrichtung="center", groesse=GROSS, farbe=BLAU)
    s.text(None, s.tr("ethen", "Ethen, C_2H_4", "ethene, C_2H_4", "eteno, C_2H_4", "乙烯，C_2H_4"), (xe, y - 1.02), ausrichtung="center", groesse=GROSS)
    # Benzol
    xb = 0.0
    r = 0.6
    pk = sechseck(s, xb, y, r, start=30, dicke=3.5)
    for (px, py) in pk:
        ux, uy = (px - xb) / r, (py - y) / r
        s.linie(None, (px, py), (px + 0.25 * ux, py + 0.25 * uy), farbe=GRAU, dicke=2.5)
    s.kreis(None, xb, y, 0.36, farbe=BLAU, dicke=4, dash=DASH)
    s.text(None, s.tr("benzol", "Benzol, C_6H_6", "benzene, C_6H_6", "benceno, C_6H_6", "苯，C_6H_6"), (xb, y - 1.02), ausrichtung="center", groesse=GROSS)
    # Graphen
    xg = 2.42
    a = 0.26
    h = a * sqrt(3)
    for zeile in range(4):
        for sp in range(4):
            x = xg - 1.5 * h + (sp + (zeile % 2) / 2) * h - h / 4
            yy = y + 0.72 - zeile * 1.5 * a
            sechseck(s, x, yy, a, farbe=SCHWARZ, dicke=2.5, start=30)
    s.text(None, s.tr("graph", "Graphen", "graphene", "grafeno", "石墨烯"), (xg, y - 1.02), ausrichtung="center", groesse=GROSS)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k5metall():
    """Links: Abschirmung am Beispiel Lithium. Rechts: Atomrümpfe im Elektronengas."""
    s = Szene("gemb1/k5metall")
    s.welt()
    a = s.achsen((0, 0.5, 0.1), (-40, 0, 10), breite=2.75, hoehe=2.5, mitte=(-1.85, 0.0), xl=s.tr("x", "r in nm", "r in nm", "r en nm", "r / nm"), yl=s.tr("v", "V in eV", "V in eV", "V en eV", "V / eV"),
                 xticks="0;0.1;0.2;0.3;0.4;0.5", yticks="-40;-30;-20;-10;0")
    # blau: Kern mit Z = 3 ohne Abschirmung, grün: mit den beiden 1s-Elektronen
    rb = 4.32 / 40
    s.kurve(a, "-4.32/x", x=(rb, 0.5), farbe=BLAU)
    v = lambda r: -1.44 / r * (1 + 2 * __import__("math").exp(-r / 0.02))
    rg = nullstelle(lambda r: v(r) + 40, 0.01, 0.2)
    s.kurve(a, "-1.44/x*(1+2*exp(-x/0.02))", x=(rg, 0.5), farbe=GRUEN)
    ru = C / 5.39
    s.linie(a, (0, -5.39), (ru, -5.39), farbe=GRUEN, dicke=4)
    r2 = 4.32 / 30.6
    s.linie(a, (0, -30.6), (r2, -30.6), farbe=BLAU, dicke=4)
    s.text(a, "−5.39 eV", (0.21, -8.6), ausrichtung="left", farbe=GRUEN, groesse=GROSS)
    s.text(a, "−30.6 eV", (0.165, -30.6), ausrichtung="left", farbe=BLAU, groesse=GROSS)
    s.text(a, s.tr("ohne", "ohne Abschirmung", "without screening", "sin apantallar", "无屏蔽"), (0.5, -21.5), ausrichtung="right", farbe=BLAU, groesse=KLEIN)
    s.text(a, s.tr("mit", "mit Abschirmung", "with screening", "con apantallar", "有屏蔽"), (0.5, -1.4), ausrichtung="right", farbe=GRUEN, groesse=KLEIN)

    # rechts: Rümpfe im See
    x0, y0, bx, by = 1.82, 0.1, 1.45, 1.05
    viel(s, [(x0 - bx, y0 - by), (x0 + bx, y0 - by), (x0 + bx, y0 + by), (x0 - bx, y0 + by)], farbe=BLAU, deckung=0.16, rand=0)
    d = 0.68
    for z in range(4):
        for sp in range(5):
            x = x0 - 1.2 + sp * 0.6 + (0.0 if z % 2 == 0 else 0.3)
            if x > x0 + 1.4:
                continue
            y = y0 + 0.75 - z * 0.5
            s.box("+", (x, y), breite=0.36, hoehe=0.36, form="ellipse", groesse=GROSS, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0, dicke=2)
    s.text(None, s.tr("rumpf", "Atomrümpfe (positiv)", "ion cores (positive)", "núcleos iónicos (positivos)", "原子实（正）"), (x0, y0 + by + 0.2), ausrichtung="center", groesse=GROSS)
    s.text(None, s.tr("see", "Elektronengas (negativ)", "electron gas (negative)", "gas de electrones (negativo)", "电子气（负）"), (x0, y0 - by - 0.22), ausrichtung="center", groesse=GROSS, farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def dipol(s, x, y, w=0, a=0.38, b=0.2, links="δ−", rechts="δ+"):
    ellipse(s, x, y, a, b, farbe=GRAU, deckung=0.14, winkel=w, rand=2.5)
    u, v = cos(radians(w)), sin(radians(w))
    s.text(None, links, (x - 0.19 * u, y - 0.19 * v), ausrichtung="center", groesse=KLEIN)
    s.text(None, rechts, (x + 0.19 * u, y + 0.19 * v), ausrichtung="center", groesse=KLEIN)


def k5schwach():
    """Oben die drei Dipol-Bindungen, unten alle Bindungstypen als Karte."""
    s = Szene("gemb1/k5schwach")
    s.welt()
    y = 2.3
    x1, x2, x3 = -2.4, 0.0, 2.4
    # Ion-Dipol: Moleküle zeigen mit der negativen Seite zum Kation
    for w in (0, 90, 180, 270):
        c, si = cos(radians(w)), sin(radians(w))
        ax, ay = 0.82 * c, 0.6 * si
        ellipse(s, x1 + ax, y + ay, 0.3 if w % 180 == 0 else 0.27, 0.19, farbe=GRAU, deckung=0.14, winkel=w, rand=2.5)
        s.text(None, "δ−", (x1 + 0.72 * c, y + 0.52 * si), ausrichtung="center", groesse=KLEIN)
    s.box("+", (x1, y), breite=0.38, hoehe=0.38, form="ellipse", groesse=26, farbe=ROT, fuellung="#ffffff", deckung=1.0, dicke=3)
    # Dipol-Dipol
    dipol(s, x2 - 0.44, y + 0.23)
    dipol(s, x2 + 0.44, y + 0.23)
    dipol(s, x2 - 0.44, y - 0.23)
    dipol(s, x2 + 0.44, y - 0.23)
    # London
    ellipse(s, x3 - 0.48, y, 0.42, 0.34, farbe=GRAU, deckung=0.14, rand=2.5)
    ellipse(s, x3 + 0.48, y, 0.42, 0.34, farbe=GRAU, deckung=0.14, rand=2.5)
    s.text(None, "δ−", (x3 - 0.67, y), ausrichtung="center", groesse=KLEIN)
    s.text(None, "δ+", (x3 - 0.29, y), ausrichtung="center", groesse=KLEIN)
    s.text(None, "δ−", (x3 + 0.29, y), ausrichtung="center", groesse=KLEIN)
    s.text(None, "δ+", (x3 + 0.67, y), ausrichtung="center", groesse=KLEIN)
    s.text(None, s.tr("idip", "Ion–Dipol", "ion–dipole", "ion–dipolo", "离子–偶极"), (x1, y + 0.98), ausrichtung="center", groesse=GROSS)
    s.text(None, s.tr("ddip", "Dipol–Dipol", "dipole–dipole", "dipolo–dipolo", "偶极–偶极"), (x2, y + 0.98), ausrichtung="center", groesse=GROSS)
    s.text(None, "London", (x3, y + 0.98), ausrichtung="center", groesse=GROSS)
    s.text(None, "E ∝ 1/r^2", (x1, y - 1.06), ausrichtung="center", groesse=GROSS, farbe=BLAU)
    s.text(None, "E ∝ 1/r^3", (x2, y - 1.06), ausrichtung="center", groesse=GROSS, farbe=BLAU)
    s.text(None, "E ∝ 1/r^6", (x3, y - 1.06), ausrichtung="center", groesse=GROSS, farbe=BLAU)

    # Karte: Mittelwert und Differenz der Elektronegativität
    a = s.achsen((2, 11, 1), (0, 8.5, 2), breite=5.7, hoehe=1.95, mitte=(0.15, -0.55), xl=s.tr("mit2", "mittlere Elektronegativität in eV", "mean electronegativity in eV", "electronegatividad media en eV", "平均电负性 / eV"),
                 yl=s.tr("dif", "Differenz in eV", "difference in eV", "diferencia en eV", "差值 / eV"), yticks="0;2;4;6;8", xticks="2;4;6;8;10")
    s.linie(a, (2.18, 0), (6.295, 8.23), farbe=HELLGRAU, dicke=2.5)
    s.linie(a, (10.41, 0), (6.295, 8.23), farbe=HELLGRAU, dicke=2.5)
    s.text(a, s.tr("ion", "ionisch", "ionic", "iónico", "离子键"), (8.05, 7.6), ausrichtung="left", farbe=ROT, groesse=26)
    s.text(a, s.tr("met", "metallisch", "metallic", "metálico", "金属键"), (2.15, 3.5), ausrichtung="left", farbe=ORANGE, groesse=26)
    s.text(a, s.tr("kov", "kovalent", "covalent", "covalente", "共价键"), (8.8, 3.5), ausrichtung="left", farbe=BLAU, groesse=26)
    pkt = [("CsF", 6.295, 8.23, -0.6, 0.0, ROT), ("LiF", 6.71, 7.41, 0.55, 0.0, ROT), ("KCl", 5.36, 5.87, -0.62, 0.0, ROT), ("NaCl", 5.57, 5.45, 0.75, 0.0, ROT),
           ("Al_2O_3", 5.38, 4.33, 0.98, 0.32, GRAU), ("MgO", 5.68, 3.72, 0.72, -0.15, GRAU), ("SiO_2", 6.16, 2.77, 0.72, 0.0, GRAU), ("GaAs", 4.26, 2.08, -0.72, 0.0, GRAU),
           ("Si", 4.77, 0, 0, 1.15, BLAU), ("C", 6.26, 0, 0, 1.15, BLAU), ("H_2", 7.18, 0, 0, 1.15, BLAU), ("F_2", 10.41, 0, 0, 1.15, BLAU),
           ("Cs", 2.18, 0, 0.0, 1.15, ORANGE), ("Na", 2.84, 0, 0.1, 1.15, ORANGE), ("Al", 3.21, 0, 0.42, 1.15, ORANGE)]
    for nam, x, yy, dx, dy, f in pkt:
        s.punkt(a, x, yy, farbe=f, r=0.06)
        s.text(a, nam, (x + dx, yy + dy), ausrichtung="center", groesse=KLEIN, farbe=f)
    s.speichern()


ALLE = [k5kurve, k5bilanz, k5molekuel, k5ueberlapp, k5hybrid, k5doppel, k5metall, k5schwach]

if __name__ == "__main__":
    for f in ALLE:
        f()
