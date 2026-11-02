"""ET1 Teil 5 (kap5_stufen.tex): Quellen und Ersatzquellen.

Aufruf: python tools/szenen/et1_teil5.py, danach python tools/szenen_ansehen.py out.png et1/k5gruppe ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap5.py.
"""
import sys
from math import atan2, degrees, hypot
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

BRAUN = "#a84a22"
GR = 24           # Beschriftung in Schaltbildern


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def wid(s, a, b, size=0.5, farbe=SCHWARZ):
    return bau(s, "resistor", a, b, size=size, farbe=farbe)


def uq(s, a, b, size=0.62, farbe=SCHWARZ):
    return bau(s, "vsource", a, b, size=size, farbe=farbe)


def iq(s, a, b, size=0.62, farbe=SCHWARZ):
    """Stromquelle zwischen a und b, der Strom fließt von a nach b (Pfeil getrennt zeichnen)."""
    return bau(s, "isource", a, b, size=size, farbe=farbe)


def plus(s, x, y, g=GR):
    """Pluspol neben einer Spannungsquelle."""
    t(s, "+", (x, y), g=g, farbe=ROT)


def kl(s, x, y, name="", dx=0.0, dy=0.3, farbe=SCHWARZ):
    """Klemme als kleiner Ring, Name daneben."""
    s.kreis(None, x, y, 0.07, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        s.text(None, name, (x + dx, y + dy), groesse=GR, ausrichtung="center", farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.06):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def spfeil(s, x, y0, y1, txt="", seite=1, farbe=BLAU, dx=0.1):
    """Senkrechter Spannungspfeil mit Text rechts (seite=1) oder links (seite=-1)."""
    s.pfeil((x, y0), (x, y1), "", farbe=farbe, spitze=0.17, dicke=2.5)
    if txt:
        t(s, txt, (x + seite * dx, 0.5 * (y0 + y1)), "left" if seite > 0 else "right", farbe)


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center"):
    """Kurzer Strompfeil auf einer Leitung."""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=3)
    if txt:
        t(s, txt, p, ausr, farbe)


def schritt(s, x, y, b=0.42):
    """Dicker Umformungspfeil zwischen zwei Teilbildern."""
    s.pfeil((x, y), (x + b, y), "", farbe=GRAU, spitze=0.24, dicke=4.5)


def plot_ui(s, mitte, breite, hoehe, xmax=5, ymax=10, xs=1, ys=2, gitter=True):
    return s.achsen((0, xmax, xs), (0, ymax, ys), breite=breite, hoehe=hoehe, mitte=mitte, gitter=gitter,
                    xl=s.tr("i_in_a", "I_A in A", "I_A in A", "I_A en A", "I_A / A"), yl=s.tr("u_in_v", "U_{AB} in V", "U_{AB} in V", "U_{AB} en V", "U_{AB} / V"))


# ------------------------------------------------------------------------------------------ Stufe 1
def k5gruppe():
    """Lastnetz aus sechs Widerständen und seine erste Vereinfachung."""
    s = Szene("et1/k5gruppe")
    yo, yu = 1.0, -1.0
    xa = -3.4
    kl(s, xa, yo, "A", dx=-0.05)
    kl(s, xa, yu, "B", dx=-0.05, dy=-0.3)
    wid(s, (xa + 0.07, yo), (-2.55, yo))
    t(s, "R_a", (-2.97, yo + 0.3))
    t(s, "6 Ω", (-2.97, yo - 0.3))
    xk = -2.45
    kn(s, xk, yo)
    wid(s, (xk, yo), (xk, yu))
    t(s, "R_b", (xk + 0.15, 0.17), "left")
    t(s, "30 Ω", (xk + 0.15, -0.17), "left")
    wid(s, (xk, yo), (-1.35, yo))
    t(s, "R_c", (-1.9, yo + 0.3))
    t(s, "5 Ω", (-1.9, yo - 0.3))
    # drei gestapelte Widerstände
    xl, xr = -1.25, 0.15
    for y, n, v in ((1.5, "R_d", "20 Ω"), (0.95, "R_e", "30 Ω"), (0.4, "R_f", "60 Ω")):
        wid(s, (xl, y), (xr, y), size=0.42)
        t(s, n + " = " + v, (0.5 * (xl + xr), y + 0.2), g=22)
    s.draht((xl, 1.5), (xl, 0.4))
    s.draht((xr, 1.5), (xr, 0.4))
    s.draht((-1.35, yo), (xl, yo))
    kn(s, xl, yo)
    kn(s, xr, yo)
    s.draht((xr, yo), (0.4, yo), (0.4, yu), (xa + 0.07, yu))
    kn(s, xk, yu)
    schritt(s, 0.62, 0.0)
    # zweites Teilbild
    xb = 1.25
    kl(s, xb, yo, "A", dx=-0.05)
    kl(s, xb, yu, "B", dx=-0.05, dy=-0.3)
    wid(s, (xb + 0.07, yo), (2.15, yo))
    t(s, "6 Ω", (1.72, yo + 0.3))
    kn(s, 2.15, yo)
    wid(s, (2.15, yo), (2.15, yu))
    t(s, "30 Ω", (2.05, 0), "right")
    s.draht((2.15, yo), (2.9, yo))
    wid(s, (2.9, yo), (2.9, yu))
    t(s, "15 Ω", (3.02, 0), "left")
    s.draht((2.9, yu), (xb + 0.07, yu))
    kn(s, 2.15, yu)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k5symmetrie():
    """Sieben gleiche Widerstände: Spiegelachse und Halbschaltung."""
    s = Szene("et1/k5symmetrie")
    xl, xr, xm = -3.0, -1.0, -2.0
    yo, yu = 1.5, -1.5
    ye, yf = 0.55, -0.55
    s.draht((xl, yo), (xr, yo))
    s.draht((xl, yu), (xr, yu))
    s.draht((xm, yo), (xm, yo + 0.28))
    s.draht((xm, yu), (xm, yu - 0.28))
    kl(s, xm, yo + 0.35)
    kl(s, xm, yu - 0.35)
    t(s, "A: 16 V", (xm + 0.18, yo + 0.35), "left")
    t(s, "B: 0 V", (xm + 0.18, yu - 0.35), "left")
    wid(s, (xl, yo), (xl, 0))
    wid(s, (xl, 0), (xl, yu))
    wid(s, (xr, yo), (xr, ye), size=0.42)
    wid(s, (xr, ye), (xr, yf), size=0.42)
    wid(s, (xr, yf), (xr, yu), size=0.42)
    wid(s, (xl, 0), (xr, ye), size=0.42)
    wid(s, (xl, 0), (xr, yf), size=0.42)
    kn(s, xl, 0, farbe=ROT, r=0.08)
    kn(s, xr, ye)
    kn(s, xr, yf)
    t(s, "L", (xl - 0.15, 0.28), "right", ROT)
    t(s, "E: 10 V", (xr + 0.15, ye), "left")
    t(s, "F: 6 V", (xr + 0.15, yf), "left")
    s.linie(None, (xl - 0.55, 0), (xr + 0.75, 0), farbe=ROT, dicke=3, dash=DASH)
    t(s, "8 V", (xl - 0.15, -0.28), "right", ROT)
    schritt(s, 0.12, 0.0)
    # Halbschaltung
    xa, xb, xc = 1.2, 2.2, 3.05
    yo2, yu2 = 1.35, -1.35
    s.draht((xa, yo2), (xb, yo2))
    s.draht((1.7, yo2), (1.7, yo2 + 0.25))
    kl(s, 1.7, yo2 + 0.32)
    t(s, "A", (1.88, yo2 + 0.32), "left")
    wid(s, (xa, yo2), (xa, yu2))
    t(s, "14 Ω", (xa + 0.12, 0.0), "left", g=22)
    wid(s, (xb, yo2), (xb, 0.3), size=0.42)
    t(s, "14 Ω", (xb + 0.12, 0.85), "left", g=22)
    s.draht((xb, 0.3), (xc, 0.3))
    kn(s, xb, 0.3)
    t(s, "E", (xb - 0.12, 0.42), "right")
    wid(s, (xb, 0.3), (xb, yu2), size=0.42)
    t(s, "14 Ω", (xb - 0.15, -0.55), "right", g=22)
    wid(s, (xc, 0.3), (xc, yu2), size=0.42)
    t(s, "7 Ω", (xc + 0.1, -0.5), "left", g=22)
    s.linie(None, (xa - 0.35, yu2), (xc + 0.3, yu2), farbe=ROT, dicke=4, dash=DASH)
    t(s, s.tr("achse", "Achse: 8 V", "axis: 8 V", "eje: 8 V", "对称轴：8 V"), (0.5 * (xa + xc), yu2 - 0.32), farbe=ROT)
    s.speichern()


def k5wuerfel():
    """Würfel aus zwölf Widerständen: Ecken gleichen Potenzials und die gefaltete Kette."""
    s = Szene("et1/k5wuerfel")
    # Würfel im Schrägbild: Ecken als Bits (x, y, z)
    ox, oy, a, kx, ky = -3.05, -1.4, 1.75, 0.7, 0.6

    def p(c):
        x, y, z = c
        return (ox + a * x + kx * z, oy + a * y + ky * z)
    ecken = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    for e in ecken:
        for k in range(3):
            if e[k] == 0:
                f = list(e)
                f[k] = 1
                n = sum(e)
                s.linie(None, p(e), p(tuple(f)), farbe=(ROT if n == 0 else GRAU if n == 1 else BLAU), dicke=3)
    farbe = {0: ROT, 1: GRUEN, 2: ORANGE, 3: BLAU}
    for e in ecken:
        kn(s, *p(e), farbe=farbe[sum(e)], r=0.09)
    t(s, "A", (p((0, 0, 0))[0] - 0.2, p((0, 0, 0))[1] - 0.1), "right", ROT)
    t(s, "B", (p((1, 1, 1))[0] + 0.2, p((1, 1, 1))[1] + 0.1), "left", BLAU)
    schritt(s, -0.42, 0.1)
    # Kette
    y = 0.1
    xs = [0.45, 1.45, 2.45, 3.4]
    kl(s, 0.28, y, "A", dy=0.32, farbe=ROT)
    s.draht((0.35, y), (0.45, y))
    for a0, a1 in zip(xs, xs[1:]):
        wid(s, (a0, y), (a1 - 0.0, y), size=0.42)
    kn(s, xs[1], y, farbe=GRUEN, r=0.09)
    kn(s, xs[2], y, farbe=ORANGE, r=0.09)
    kl(s, 3.47, y, "B", dy=0.32, farbe=BLAU)
    for x, w, n in ((0.95, "4 Ω", "R/3"), (1.95, "2 Ω", "R/6"), (2.92, "4 Ω", "R/3")):
        t(s, n, (x, y + 0.4))
        t(s, w, (x, y - 0.4))
    t(s, s.tr("drei", "3 Kanten", "3 edges", "3 aristas", "3 条棱"), (0.95, y - 0.8), g=22, farbe=GRAU)
    t(s, s.tr("sechs", "6 Kanten", "6 edges", "6 aristas", "6 条棱"), (1.95, y - 0.8), g=22, farbe=GRAU)
    t(s, s.tr("drei", "3 Kanten", "3 edges", "3 aristas", "3 条棱"), (2.92, y - 0.8), g=22, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k5bruecke():
    """Brücke: das Dreieck 1-2-3 wird zum Stern."""
    s = Szene("et1/k5bruecke")
    cx = -1.95
    p1, p2, p3 = (cx, 1.25), (cx + 1.35, 0.0), (cx - 1.35, 0.0)
    pb = (cx, -1.25)
    wid(s, p1, p2, size=0.42, farbe=BLAU)
    wid(s, p3, p1, size=0.42, farbe=BLAU)
    wid(s, p3, p2, size=0.42, farbe=BLAU)
    wid(s, p2, pb, size=0.42)
    wid(s, p3, pb, size=0.42)
    s.draht(p1, (cx, 1.55))
    s.draht(pb, (cx, -1.55))
    kl(s, cx, 1.62, "A", dx=0.22, dy=0.0)
    kl(s, cx, -1.62, "B", dx=0.22, dy=0.0)
    for p in (p1, p2, p3, pb):
        kn(s, *p)
    t(s, "1", (cx - 0.18, 1.42), farbe=BLAU)
    t(s, "2", (cx + 1.58, 0.0), farbe=BLAU)
    t(s, "3", (cx - 1.58, 0.0), farbe=BLAU)
    t(s, "10 Ω", (cx + 0.82, 0.86), "left", BLAU)
    t(s, "20 Ω", (cx - 0.82, 0.86), "right", BLAU)
    t(s, "20 Ω", (cx, 0.3), farbe=BLAU)
    t(s, "20 Ω", (cx + 0.82, -0.86), "left")
    t(s, "16 Ω", (cx - 0.82, -0.86), "right")
    schritt(s, 0.05, 0.0)
    # Stern
    cx = 2.1
    pa = (cx, 1.55)
    p0 = (cx, 0.5)
    q2, q3 = (cx + 1.0, -0.35), (cx - 1.0, -0.35)
    pb = (cx, -1.25)
    wid(s, pa, p0, size=0.42, farbe=ROT)
    wid(s, p0, q2, size=0.42, farbe=ROT)
    wid(s, p0, q3, size=0.42, farbe=ROT)
    wid(s, q2, pb, size=0.42)
    wid(s, q3, pb, size=0.42)
    s.draht(pb, (cx, -1.55))
    kl(s, cx, 1.62, "A", dx=0.22, dy=0.0)
    kl(s, cx, -1.62, "B", dx=0.22, dy=0.0)
    for p in (p0, q2, q3, pb):
        kn(s, *p)
    t(s, "0", (cx - 0.2, 0.62), farbe=ROT)
    t(s, "2", (cx + 1.2, -0.3), farbe=ROT)
    t(s, "3", (cx - 1.2, -0.3), farbe=ROT)
    t(s, "4 Ω", (cx + 0.12, 1.05), "left", ROT)
    t(s, "4 Ω", (cx + 0.62, 0.35), "left", ROT)
    t(s, "8 Ω", (cx - 0.62, 0.35), "right", ROT)
    t(s, "20 Ω", (cx + 0.62, -0.95), "left")
    t(s, "16 Ω", (cx - 0.62, -0.95), "right")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k5ideal():
    """Ideale Spannungs- und Stromquelle im selben Diagramm."""
    s = Szene("et1/k5ideal")
    ir = s.welt()
    y0 = 0.1
    # links: Spannungsquelle
    x = -2.75
    uq(s, (x, y0 + 1.0), (x, y0 - 1.0))
    s.draht((x, y0 + 1.0), (x + 0.88, y0 + 1.0))
    s.draht((x, y0 - 1.0), (x + 0.88, y0 - 1.0))
    kl(s, x + 0.95, y0 + 1.0, "A", dy=0.28)
    kl(s, x + 0.95, y0 - 1.0, "B", dy=-0.3)
    spfeil(s, x - 0.33, y0 + 0.62, y0 - 0.62, "U_q", seite=-1, farbe=SCHWARZ)
    spfeil(s, x + 0.95, y0 + 0.82, y0 - 0.82, "U_{AB}", seite=-1, dx=0.08)
    ipfeil(s, (x + 0.3, y0 + 1.0), (x + 0.65, y0 + 1.0), "I_A", (x + 0.48, y0 + 1.3))
    a = s.achsen((0, 4, 1), (0, 4, 1), breite=1.1, hoehe=1.9, mitte=(-0.95, y0), kreuz=True, xl="I_A", yl="U_{AB}", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.linie(a, (0, 2.6), (3.6, 2.6), farbe=BLAU, dicke=5)
    s.text(a, "U_q", (3.5, 3.15), groesse=GR, ausrichtung="right", farbe=BLAU)
    t(s, s.tr("ideal_u", "Spannung fest, Strom frei", "voltage fixed, current free", "tensión fija, corriente libre", "电压固定，电流自由"), (-1.9, y0 - 1.62), g=22)
    # rechts: Stromquelle
    x = 0.55
    iq(s, (x, y0 - 1.0), (x, y0 + 1.0))
    s.draht((x, y0 + 1.0), (x + 0.88, y0 + 1.0))
    s.draht((x, y0 - 1.0), (x + 0.88, y0 - 1.0))
    kl(s, x + 0.95, y0 + 1.0, "A", dy=0.28)
    kl(s, x + 0.95, y0 - 1.0, "B", dy=-0.3)
    ipfeil(s, (x, y0 + 0.5), (x, y0 + 0.82), "I_q", (x - 0.14, y0 + 0.65), ausr="right")
    spfeil(s, x + 0.95, y0 + 0.82, y0 - 0.82, "U_{AB}", seite=-1, dx=0.08)
    ipfeil(s, (x + 0.3, y0 + 1.0), (x + 0.65, y0 + 1.0), "I_A", (x + 0.48, y0 + 1.3))
    b = s.achsen((0, 4, 1), (0, 4, 1), breite=1.1, hoehe=1.9, mitte=(2.35, y0), kreuz=True, xl="I_A", yl="U_{AB}", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.linie(b, (2.4, 0), (2.4, 3.7), farbe=BLAU, dicke=5)
    s.text(b, "I_q", (2.4, -0.42), groesse=GR, ausrichtung="center", farbe=BLAU)
    t(s, s.tr("ideal_i", "Strom fest, Spannung frei", "current fixed, voltage free", "corriente fija, tensión libre", "电流固定，电压自由"), (1.75, y0 - 1.62), g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def batterie_esb(s, x, yo, yu, xr, ri="2 Ω"):
    """Ideale Quelle und Innenwiderstand bis zu den Klemmen xr."""
    uq(s, (x, yo), (x, yu))
    s.draht((x, yo), (x + 0.2, yo))
    wid(s, (x + 0.2, yo), (xr - 0.3, yo), size=0.45)
    s.draht((xr - 0.3, yo), (xr - 0.07, yo))
    s.draht((x, yu), (xr - 0.07, yu))
    kl(s, xr, yo, "A", dy=0.3)
    kl(s, xr, yu, "B", dy=-0.3)


def k5arbeitsgerade():
    """Quelle und Last: Kennlinie der Quelle, zwei Arbeitsgeraden, zwei Arbeitspunkte."""
    s = Szene("et1/k5arbeitsgerade")
    s.welt()
    yo, yu = 1.0, -1.0
    x = -3.2
    xr = -1.9
    batterie_esb(s, x, yo, yu, xr)
    t(s, "R_q", ((x + xr) / 2 + 0.02, yo + 0.3))
    t(s, "2 Ω", ((x + xr) / 2 + 0.02, yo - 0.3))
    spfeil(s, x - 0.32, 0.62, -0.62, "", farbe=SCHWARZ)
    t(s, "U_q", (x - 0.25, 0.92), farbe=SCHWARZ)
    t(s, "9 V", (x + 0.3, 0), "left")
    s.draht((xr + 0.07, yo), (xr + 0.75, yo))
    s.draht((xr + 0.07, yu), (xr + 0.75, yu))
    wid(s, (xr + 0.75, yo), (xr + 0.75, yu), farbe=ORANGE)
    t(s, "R_L", (xr + 0.87, 0.0), "left", BRAUN)
    spfeil(s, xr, yo - 0.2, yu + 0.2, "U_{AB}", seite=1, dx=0.07)
    ipfeil(s, (xr + 0.2, yo), (xr + 0.55, yo), "I_A", (xr + 0.38, yo + 0.3))
    a = plot_ui(s, (1.7, 0.15), 3.2, 2.5)
    s.linie(a, (0, 9), (5, 9), farbe=GRAU, dicke=2.5, dash=DASH)
    s.text(a, s.tr("ideal", "ideal: R_q = 0", "ideal: R_q = 0", "ideal: R_q = 0", "理想：R_q = 0"), (2.35, 9.45), groesse=22, farbe=GRAU)
    s.kurve(a, "9-2*x", x=(0, 4.5), farbe=BLAU, dicke=5)
    s.linie(a, (0, 0), (0.6, 9.6), farbe=ORANGE, dicke=4)
    s.linie(a, (0, 0), (4.75, 9.5), farbe=GRUEN, dicke=4)
    for px, py in ((0.5, 8), (2.25, 4.5)):
        s.linie(a, (px, 0), (px, py), farbe=GRAU, dicke=2, dash=DASH)
        s.linie(a, (0, py), (px, py), farbe=GRAU, dicke=2, dash=DASH)
        s.punkt(a, px, py, farbe=ROT, r=0.09)
    s.punkt(a, 0, 9, farbe=BLAU, r=0.08)
    s.punkt(a, 4.5, 0, farbe=BLAU, r=0.08)
    s.text(a, s.tr("ll", "Leerlauf", "open circuit", "circuito abierto", "开路"), (0.72, 8.55), groesse=22, farbe=BLAU)
    s.text(a, s.tr("ks", "Kurzschluss", "short circuit", "cortocircuito", "短路"), (3.7, 0.8), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(a, "(0.5 A; 8 V)", (0.95, 7.75), groesse=22, farbe=ROT)
    s.text(a, "(2.25 A; 4.5 V)", (2.55, 4.5), groesse=22, farbe=ROT)
    s.text(a, "R_L = 16 Ω", (0.62, 3.75), groesse=22, farbe=BRAUN)
    s.text(a, "R_L = 2 Ω", (2.55, 7.6), groesse=22, farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k5umwandlung():
    """Dieselbe Batterie als Spannungs- und als Stromquelle, am selben Arbeitspunkt."""
    s = Szene("et1/k5umwandlung")
    yo, yu = 1.0, -1.0
    # links
    x, xr = -3.25, -1.6
    batterie_esb(s, x, yo, yu, xr)
    t(s, "2 Ω", (0.5 * (x + xr) + 0.05, yo + 0.3))
    t(s, "9 V", (x + 0.3, 0), "left")
    plus(s, x + 0.2, 0.42)
    s.draht((xr + 0.07, yo), (xr + 0.7, yo))
    s.draht((xr + 0.07, yu), (xr + 0.7, yu))
    wid(s, (xr + 0.7, yo), (xr + 0.7, yu), size=0.42, farbe=GRAU)
    t(s, "16 Ω", (xr + 0.8, 0.0), "left", GRAU, g=22)
    spfeil(s, xr, yo - 0.2, yu + 0.2, "8 V", seite=1, dx=0.07)
    ipfeil(s, (xr + 0.2, yo), (xr + 0.55, yo), "0.5 A", (xr + 0.4, yo + 0.3))
    s.text(None, "≙", (0.0, 0.0), groesse=38, ausrichtung="center")
    # rechts
    x, xg, xr = 0.5, 1.45, 2.3
    iq(s, (x, yu), (x, yo))
    s.draht((x, yo), (xr - 0.07, yo))
    s.draht((x, yu), (xr - 0.07, yu))
    wid(s, (xg, yo), (xg, yu), size=0.42)
    kn(s, xg, yo)
    kn(s, xg, yu)
    kl(s, xr, yo, "A", dy=0.3)
    kl(s, xr, yu, "B", dy=-0.3)
    ipfeil(s, (x, 0.5), (x, 0.82))
    t(s, "4.5 A", (x + 0.12, 0.68), "left", ROT, g=22)
    t(s, "0.5 S", (xg - 0.1, -0.5), "right", g=22)
    ipfeil(s, (xg, 0.82), (xg, 0.5), "4 A", (xg + 0.1, 0.62), ausr="left")
    s.draht((xr + 0.07, yo), (xr + 0.7, yo))
    s.draht((xr + 0.07, yu), (xr + 0.7, yu))
    wid(s, (xr + 0.7, yo), (xr + 0.7, yu), size=0.42, farbe=GRAU)
    t(s, "16 Ω", (xr + 0.8, 0.0), "left", GRAU, g=22)
    spfeil(s, xr, yo - 0.2, yu + 0.2, "8 V", seite=1, dx=0.07)
    ipfeil(s, (xr + 0.2, yo), (xr + 0.55, yo), "0.5 A", (xr + 0.4, yo + 0.3))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k5zusammen():
    """Zwei Batterien parallel, drei Kennlinien."""
    s = Szene("et1/k5zusammen")
    s.welt()
    yo, yu = 1.1, -1.1
    xs = (-3.2, -2.25)
    for x, n in zip(xs, ("1", "2")):
        wid(s, (x, yo), (x, 0.35), size=0.42)
        uq(s, (x, 0.35), (x, yu), size=0.55)
        t(s, "2 Ω", (x + 0.12, 0.75), "left", g=22)
        t(s, "9 V", (x + 0.3, -0.45), "left", g=22)
        plus(s, x + 0.2, -0.07, g=22)
    s.draht((xs[0], yo), (-1.57, yo))
    s.draht((xs[0], yu), (-1.57, yu))
    kn(s, xs[1], yo)
    kn(s, xs[1], yu)
    kl(s, -1.5, yo, "A", dy=0.28)
    kl(s, -1.5, yu, "B", dy=-0.3)
    ipfeil(s, (-2.0, yo), (-1.65, yo), "I_A", (-1.85, yo + 0.3))
    spfeil(s, -1.5, yo - 0.2, yu + 0.2, "U_{AB}", seite=1, dx=0.08)
    a = s.achsen((0, 10, 2), (0, 20, 5), breite=3.2, hoehe=2.5, mitte=(1.85, 0.2), gitter=True,
                 xl=s.tr("i_in_a", "I_A in A", "I_A in A", "I_A en A", "I_A / A"), yl=s.tr("u_in_v", "U_{AB} in V", "U_{AB} in V", "U_{AB} en V", "U_{AB} / V"))
    s.kurve(a, "9-2*x", x=(0, 4.5), farbe=BLAU)
    s.kurve(a, "9-x", x=(0, 9), farbe=GRUEN)
    s.kurve(a, "18-4*x", x=(0, 4.5), farbe=ORANGE)
    s.linie(a, (0, 0), (1.25, 20), farbe=GRAU, dicke=2.5, dash=DASH)
    s.text(a, "16 Ω", (1.45, 18.3), groesse=22, farbe=GRAU)
    for (px, py, f) in ((0.5, 8, BLAU), (0.5294, 8.4706, GRUEN), (0.9, 14.4, ORANGE)):
        s.punkt(a, px, py, farbe=f, r=0.07)
    s.text(a, s.tr("reihe", "zwei in Reihe", "two in series", "dos en serie", "两节串联"), (3.0, 11.5), groesse=22, farbe=BRAUN)
    s.text(a, s.tr("eine", "eine", "one", "una", "一节"), (0.9, 2.6), groesse=22, farbe=BLAU)
    s.text(a, s.tr("zwei", "zwei parallel", "two in parallel", "dos en paralelo", "两节并联"), (5.5, 5.5), groesse=22, farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def netz_n(s, x0, y0, u=True, i=True, grau_u=False, grau_i=False, mess=""):
    """Netzwerk N. u=False: Spannungsquelle durch Draht ersetzt, i=False: Stromquelle offen. x0 = linke Leitung."""
    yo, yu = y0 + 0.85, y0 - 0.85
    xk, xq, xr = x0 + 1.0, x0 + 1.72, x0 + 1.72
    if u:
        uq(s, (x0, yo), (x0, yu), size=0.5)
        t(s, "18 V", (x0 + 0.24, y0), "left", g=22)
        plus(s, x0 + 0.2, y0 + 0.36, g=22)
    else:
        s.draht((x0, yo), (x0, yu))
        t(s, "0 V", (x0 + 0.1, y0), "left", ROT, g=22)
    s.draht((x0, yo), (x0 + 0.1, yo))
    wid(s, (x0 + 0.1, yo), (xk, yo), size=0.38)
    t(s, "R_1", (0.5 * (x0 + xk), yo + 0.27), g=22)
    t(s, "6 Ω", (0.5 * (x0 + xk), yo - 0.27), g=22)
    wid(s, (xk, yo), (xk, yu), size=0.38)
    t(s, "R_2", (xk + 0.1, y0 + 0.17), "left", g=22)
    t(s, "3 Ω", (xk + 0.1, y0 - 0.17), "left", g=22)
    s.draht((x0, yu), (xr - 0.07, yu))
    s.draht((xk, yo), (xr - 0.07, yo))
    kn(s, xk, yo)
    kn(s, xk, yu)
    if i:
        iq(s, (xq, yu), (xq, yo), size=0.42)
        ipfeil(s, (xq, y0 + 0.42), (xq, y0 + 0.72), "", None)
        t(s, "1.5 A", (xq - 0.13, yu - 0.28), "right", ROT, g=22)
    else:
        s.linie(None, (xq, yo), (xq, y0 + 0.2), farbe=SCHWARZ, dicke=3)
        s.linie(None, (xq, yu), (xq, y0 - 0.2), farbe=SCHWARZ, dicke=3)
        t(s, "0 A", (xq - 0.13, yu - 0.28), "right", ROT, g=22)
    kl(s, xr, yo, "A", dx=0.0, dy=0.27)
    kl(s, xr, yu, "B", dx=0.0, dy=-0.28)
    if mess:
        t(s, mess, (x0 + 0.85, y0 - 1.5), farbe=BLAU, g=24)


def k5ueberlagerung():
    """Netzwerk N und die beiden Teilbilder."""
    s = Szene("et1/k5ueberlagerung")
    netz_n(s, -3.3, 0.0, mess="U_{AB} = 9 V")
    t(s, "=", (-1.22, 0), g=30)
    netz_n(s, -0.82, 0.0, i=False, mess="U' = 6 V")
    t(s, "+", (1.15, 0), g=30)
    netz_n(s, 1.55, 0.0, u=False, mess="U'' = 3 V")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k5ersatz():
    """Netzwerk N, Ersatzspannungsquelle, Ersatzstromquelle."""
    s = Szene("et1/k5ersatz")
    netz_n(s, -3.4, 0.0)
    s.box("", (-2.55, 0.0), breite=2.65, hoehe=2.6, farbe=GRAU, fuellung="#ffffff", deckung=0.0, dicke=2, dash=DASH)
    # Ersatzspannungsquelle
    x, xr = 0.6, 2.6
    yo, yu = 1.7, 0.25
    uq(s, (x, yo), (x, yu), size=0.5)
    s.draht((x, yo), (x + 0.3, yo))
    wid(s, (x + 0.3, yo), (xr - 0.3, yo), size=0.38)
    s.draht((xr - 0.3, yo), (xr - 0.07, yo))
    s.draht((x, yu), (xr - 0.07, yu))
    kl(s, xr, yo, "A", dx=0.2, dy=0.0)
    kl(s, xr, yu, "B", dx=0.2, dy=0.0)
    t(s, "U_i = 9 V", (x + 0.3, 0.98), "left", g=22)
    plus(s, x + 0.2, 1.34, g=22)
    t(s, "R_i = 2 Ω", (0.5 * (x + xr) + 0.05, yo + 0.28), g=22)
    # Ersatzstromquelle
    yo, yu = -0.25, -1.7
    xg = 1.7
    iq(s, (x, yu), (x, yo), size=0.5)
    s.draht((x, yo), (xr - 0.07, yo))
    s.draht((x, yu), (xr - 0.07, yu))
    wid(s, (xg, yo), (xg, yu), size=0.38)
    kn(s, xg, yo)
    kn(s, xg, yu)
    kl(s, xr, yo, "A", dx=0.2, dy=0.0)
    kl(s, xr, yu, "B", dx=0.2, dy=0.0)
    ipfeil(s, (x, -0.72), (x, -0.42))
    t(s, "I_i = 4.5 A", (x + 0.15, -0.5), "left", ROT, g=22)
    t(s, "G_i = 0.5 S", (xg + 0.16, -0.98), "left", g=22)
    s.pfeil((-0.7, 0.5), (0.0, 1.0), "", farbe=GRAU, spitze=0.22, dicke=4)
    s.pfeil((-0.7, -0.5), (0.0, -1.0), "", farbe=GRAU, spitze=0.22, dicke=4)
    s.speichern()


def k5geraden():
    """Jede Quelle verschiebt die Gerade parallel; die Steigung bleibt."""
    s = Szene("et1/k5geraden")
    a = plot_ui(s, (0.0, 0.0), 5.0, 2.2)
    s.kurve(a, "3-2*x", x=(0, 1.5), farbe=ORANGE)
    s.kurve(a, "6-2*x", x=(0, 3), farbe=GRUEN)
    s.kurve(a, "9-2*x", x=(0, 4.5), farbe=BLAU, dicke=6)
    s.linie(a, (0, 0), (0.56, 9), farbe=GRAU, dicke=2.5, dash=DASH)
    s.punkt(a, 0.5, 8, farbe=ROT, r=0.09)
    s.text(a, "(0.5 A; 8 V)", (0.68, 8.2), groesse=23, farbe=ROT)
    s.legende(a, [(s.tr("beide", "beide Quellen: 9 V, 4.5 A", "both sources: 9 V, 4.5 A", "ambas fuentes: 9 V, 4.5 A", "两个电源：9 V，4.5 A"), BLAU, "-"),
                  (s.tr("nur_u", "nur 18 V: 6 V, 3 A", "18 V only: 6 V, 3 A", "solo 18 V: 6 V, 3 A", "仅 18 V：6 V，3 A"), GRUEN, "-"),
                  (s.tr("nur_i", "nur 1.5 A: 3 V, 1.5 A", "1.5 A only: 3 V, 1.5 A", "solo 1.5 A: 3 V, 1.5 A", "仅 1.5 A：3 V，1.5 A"), ORANGE, "-")], (2.3, 9.3))
    s.text(a, "R_L = 16 Ω", (0.72, 5.0), groesse=23, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def k5r2r():
    """Drei-Bit-Wandler aus R und 2R, Schalterstellung 101."""
    s = Szene("et1/k5r2r")
    yo, ym, yk, yref, ygnd = 1.5, 0.25, -0.65, -1.15, -1.85
    xs = [-1.95, -0.35, 1.25]
    xe = -3.1
    wid(s, (xe, yo), (xe, ygnd), size=0.42)
    t(s, "2R", (xe - 0.17, 0.0), "right")
    s.draht((xe, yo), (xs[0], yo))
    kn(s, xs[0], yo)
    for a, b in zip(xs, xs[1:]):
        wid(s, (a, yo), (b, yo), size=0.42)
        t(s, "R", (0.5 * (a + b), yo + 0.3))
        kn(s, b, yo)
    for k, (x, name, bit) in enumerate(zip(xs, ("d_0", "d_1", "d_2"), (1, 0, 1))):
        wid(s, (x, yo), (x, ym), size=0.42)
        t(s, "2R", (x - 0.17, 0.9), "right")
        ziel = x + (0.28 if bit else -0.28)
        s.linie(None, (x, ym), (ziel, yk + 0.05), dicke=3)
        kn(s, x, ym)
        t(s, name + " = %d" % bit, (x + 0.25, -0.05), "left", ROT)
        for sx in (x - 0.28, x + 0.28):
            s.kreis(None, sx, yk, 0.05, farbe=SCHWARZ, dicke=2, fuellung="#ffffff", deckung=1.0)
        s.draht((x + 0.28, yk - 0.05), (x + 0.28, yref))
        kn(s, x + 0.28, yref)
        s.draht((x - 0.28, yk - 0.05), (x - 0.28, ygnd))
        kn(s, x - 0.28, ygnd)
    s.draht((xs[0] + 0.28, yref), (2.05, yref))
    s.draht((xe, ygnd), (2.68, ygnd))
    s.draht((xs[2], yo), (2.68, yo))
    kl(s, 2.75, yo)
    kl(s, 2.75, ygnd)
    spfeil(s, 2.75, yo - 0.2, ygnd + 0.2, s.tr("uaus", "U_{aus}", "U_{out}", "U_{sal}", "U_{out}"), seite=1, dx=0.08)
    uq(s, (2.05, yref), (2.05, ygnd), size=0.3)
    kn(s, 2.05, ygnd)
    t(s, "U_{ref}", (1.8, -1.5), "right", farbe=ROT, g=22)
    plus(s, 2.25, -1.28, g=22)
    s.speichern()


if __name__ == "__main__":
    for f in (k5gruppe, k5symmetrie, k5wuerfel, k5bruecke, k5ideal, k5arbeitsgerade, k5umwandlung, k5zusammen, k5ueberlagerung, k5ersatz, k5geraden, k5r2r):
        f()
