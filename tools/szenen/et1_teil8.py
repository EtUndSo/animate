"""ET1 Teil 8 (kap8_stufen.tex): Maschenstrom- und Knotenpotentialverfahren.

Aufruf: python tools/szenen/et1_teil8.py, danach python tools/szenen_ansehen.py out.png et1/k8netz ... [--lang de]
Alle Zahlen stammen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap8.py.
"""
import sys
from math import atan2, cos, degrees, hypot, pi, sin
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLBLAU = "#dceafa"
BRAUN = "#a84a22"
GR = 24           # Beschriftung in Schaltbildern


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def wid(s, a, b, size=0.46, farbe=SCHWARZ):
    return bau(s, "resistor", a, b, size=size, farbe=farbe)


def uq(s, a, b, size=0.58, farbe=SCHWARZ):
    return bau(s, "vsource", a, b, size=size, farbe=farbe)


def iq(s, a, b, size=0.58, farbe=SCHWARZ):
    return bau(s, "isource", a, b, size=size, farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.06):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def masse(s, x, y, groesse=0.6):
    """Massezeichen unter der Leitung y."""
    s.draht((x, y), (x, y - 0.17))
    return s._add("Device", {"kind": "ground", "center": [x, y - 0.32, 0], "rotation": 0, "flip": False, "label": "", "pins": False, "size": groesse,
                             "font_size": 22, "color": SCHWARZ, "stroke_width": 3, "symbol_style": "europäisch"})


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center", g=GR, dicke=3):
    """Strompfeil, Text an der Stelle p."""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=dicke)
    if txt:
        t(s, txt, p, ausr, farbe, g)


def kreisstrom(s, x, y, r, name, farbe=BLAU):
    """Maschenstrom im Uhrzeigersinn: offener Kreis mit Spitze, Name in der Mitte."""
    w0, w1 = 0.42 * pi, 2.28 * pi
    s.weg(None, f"{x}+{r}*cos(t)", f"{y}+{r}*sin(t)", w0, w1, farbe=farbe, dicke=3.5, n=61)
    xa, ya = x + r * cos(w0), y + r * sin(w0)
    s.pfeil((xa - 0.14, ya + 0.04), (xa + 0.1, ya), "", farbe=farbe, spitze=0.2, dicke=3.5)
    t(s, name, (x, y), "center", farbe, 28)


def matrix(s, x0, y0, b, h):
    """Eckige Klammern um ein Feld mit linker oberer Ecke (x0, y0)."""
    d = 0.09
    s.draht((x0 + d, y0), (x0, y0), (x0, y0 - h), (x0 + d, y0 - h), dicke=2.5)
    s.draht((x0 + b - d, y0), (x0 + b, y0), (x0 + b, y0 - h), (x0 + b - d, y0 - h), dicke=2.5)


# ------------------------------------------------------------------------------------------ Stufe 1
def k8netz():
    """Das Rechenmodell mit Batterie und realer Stromquelle."""
    s = Szene("et1/k8netz")
    yo, yu = 1.0, -1.0
    xq, x1, x2, x5, xi = -2.85, -0.85, 0.7, 1.65, 2.55
    s.draht((xq, yo), (-2.45, yo))
    s.draht((-1.4, yo), (-0.65, yo))
    s.draht((0.2, yo), (xi, yo))
    s.draht((xq, yu), (xi, yu))
    uq(s, (xq, yo), (xq, yu), size=0.62)
    wid(s, (-2.45, yo), (-1.4, yo))
    wid(s, (x1, yo), (x1, yu))
    wid(s, (-0.65, yo), (0.2, yo))
    wid(s, (x2, yo), (x2, yu))
    wid(s, (x5, yo), (x5, yu))
    iq(s, (xi, yu), (xi, yo), size=0.62)
    t(s, "+", (xq - 0.34, 0.42), "center", ROT)
    t(s, "U_q", (xq - 0.42, 0.17), "right")
    t(s, "9 V", (xq - 0.42, -0.17), "right")
    t(s, "R_1 = 1 kΩ", (-1.93, yo + 0.34))
    t(s, "R_2", (x1 - 0.2, 0.17), "right")
    t(s, "4 kΩ", (x1 - 0.2, -0.17), "right")
    t(s, "R_3 = 2 kΩ", (-0.22, yo + 0.34))
    t(s, "R_4", (x2 + 0.2, 0.17), "left")
    t(s, "10 kΩ", (x2 + 0.2, -0.17), "left")
    t(s, "R_5", (x5 + 0.2, 0.17), "left")
    t(s, "5 kΩ", (x5 + 0.2, -0.17), "left")
    t(s, "I_q", (xi + 0.42, 0.17), "left")
    t(s, "4 mA", (xi + 0.42, -0.17), "left")
    s.pfeil((xi + 0.27, -0.5), (xi + 0.27, 0.5), "", farbe=ROT, spitze=0.17, dicke=3)
    for x in (x1, x2, x5):
        kn(s, x, yo)
        kn(s, x, yu)
    kn(s, x1, yo, ROT, 0.08)
    kn(s, x2, yo, ROT, 0.08)
    t(s, "1", (x1 - 0.2, yo - 0.27), "center", ROT, 28)
    t(s, "2", (x2 + 0.2, yo + 0.3), "center", ROT, 28)
    t(s, "0", (x2 + 0.2, yu - 0.3), "center", ROT, 28)
    masse(s, x1, yu)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k8kreis():
    """Knoten 1: links die Kreisströme, rechts dieselbe Lage als Zweigströme."""
    s = Szene("et1/k8kreis")

    def knoten(xc, yc):
        s.draht((xc - 1.45, yc), (xc + 1.45, yc))
        s.draht((xc, yc), (xc, yc - 1.45))
        wid(s, (xc - 1.25, yc), (xc - 0.55, yc), size=0.34)
        wid(s, (xc + 0.55, yc), (xc + 1.25, yc), size=0.34)
        wid(s, (xc, yc - 0.55), (xc, yc - 1.25), size=0.34)
        kn(s, xc, yc, ROT, 0.08)
        t(s, "1", (xc, yc + 0.3), "center", ROT, 28)
        t(s, "R_1", (xc - 0.9, yc + 0.33))
        t(s, "R_3", (xc + 0.9, yc + 0.33))

    yc = 0.8
    # links: Kreisströme als Winkel neben den Leitungen
    xc = -1.85
    knoten(xc, yc)
    s.draht((xc - 1.4, yc - 0.2), (xc - 0.2, yc - 0.2), farbe=BLAU, dicke=4)
    s.pfeil((xc - 0.2, yc - 0.2), (xc - 0.2, yc - 1.4), "", farbe=BLAU, spitze=0.2, dicke=4)
    s.draht((xc + 0.2, yc - 1.4), (xc + 0.2, yc - 0.2), farbe=GRUEN, dicke=4)
    s.pfeil((xc + 0.2, yc - 0.2), (xc + 1.4, yc - 0.2), "", farbe=GRUEN, spitze=0.2, dicke=4)
    t(s, "I_I", (xc - 0.8, yc - 0.55), "center", BLAU, 26)
    t(s, "I_{II}", (xc + 0.8, yc - 0.55), "center", GRUEN, 26)
    t(s, "R_2", (xc + 0.8, yc - 1.15), "center")
    # rechts: Zweigströme
    xc = 1.85
    knoten(xc, yc)
    t(s, "R_2", (xc - 0.22, yc - 0.9), "right")
    ipfeil(s, (xc - 0.5, yc), (xc - 0.14, yc), "", None, BLAU, dicke=4)
    t(s, "I_I", (xc - 0.33, yc - 0.3), "center", BLAU, 26)
    ipfeil(s, (xc + 0.14, yc), (xc + 0.5, yc), "", None, GRUEN, dicke=4)
    t(s, "I_{II}", (xc + 0.36, yc - 0.3), "center", GRUEN, 26)
    ipfeil(s, (xc, yc - 0.1), (xc, yc - 0.5), "", None, ROT, dicke=4)
    t(s, "I_I − I_{II}", (xc + 0.16, yc - 1.0), "left", ROT, 26)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k8maschen():
    """Umgewandelte Stromquelle, drei Fenster, drei Maschenströme."""
    s = Szene("et1/k8maschen")
    yo, yu = 1.1, -1.1
    xq, x1, x2, xr = -2.85, -1.0, 0.75, 2.55
    s.draht((xq, yo), (-2.45, yo))
    s.draht((-1.45, yo), (-0.6, yo))
    s.draht((0.4, yo), (xr, yo))
    s.draht((xq, yu), (xr, yu))
    s.draht((xr, -0.15), (xr, 0.0))
    uq(s, (xq, yo), (xq, yu), size=0.62)
    wid(s, (-2.45, yo), (-1.45, yo))
    wid(s, (-0.6, yo), (0.4, yo))
    wid(s, (x1, yo), (x1, yu), farbe=ROT)
    wid(s, (x2, yo), (x2, yu), farbe=ROT)
    wid(s, (xr, yo), (xr, 0.0))
    uq(s, (xr, -0.15), (xr, yu), size=0.54)
    t(s, "+", (xq - 0.34, 0.45), "center", ROT)
    t(s, "+", (xr + 0.32, -0.32), "center", ROT)
    t(s, "U_q", (xq - 0.42, 0.17), "right")
    t(s, "9 V", (xq - 0.42, -0.17), "right")
    t(s, "R_1 = 1 kΩ", (-1.95, yo + 0.33))
    t(s, "R_3 = 2 kΩ", (-0.1, yo + 0.33))
    t(s, "R_5", (xr + 0.22, 0.72), "left")
    t(s, "5 kΩ", (xr + 0.22, 0.4), "left")
    t(s, "U_{q5}", (xr + 0.42, -0.6), "left")
    t(s, "20 V", (xr + 0.42, -0.92), "left")
    t(s, "R_2", (x1 - 0.2, 0.17), "right", ROT)
    t(s, "4 kΩ", (x1 - 0.2, -0.17), "right", ROT)
    t(s, "R_4", (x2 + 0.2, 0.17), "left", ROT)
    t(s, "10 kΩ", (x2 + 0.2, -0.17), "left", ROT)
    for x in (x1, x2):
        kn(s, x, yo)
        kn(s, x, yu)
    kreisstrom(s, -2.08, -0.1, 0.36, "I")
    kreisstrom(s, -0.12, -0.1, 0.46, "II")
    kreisstrom(s, 1.98, -0.1, 0.36, "III")
    masse(s, 0.0, yu)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k8hoehen():
    """Knoten als Höhen: Der Umlauf kehrt zum Ausgangswert zurück."""
    s = Szene("et1/k8hoehen")
    a = s.achsen((0, 7.5), (0, 12, 2), breite=5.6, hoehe=2.2, mitte=(0.2, 0), xl="",
                 yl=s.tr("pot", "Potenzial in V", "potential in V", "potencial en V", "电位 / V"), xzahlen=False, xmarks=False)
    s.tr("kn", "Knoten", "node", "nudo", "节点")
    for x0, x1, h, name in ((0.4, 1.6, 0, "0"), (2.4, 3.6, 8, "1"), (4.2, 5.4, 10, "2"), (6.2, 7.4, 0, "0")):
        s.linie(a, (x0, h), (x1, h), farbe=BLAU, dicke=7)
        s.text(a, f"@{{kn}} {name}", (0.5 * (x0 + x1), h + 1.0), groesse=24, ausrichtung="center", farbe=BLAU)
    s.pfeil((1.6, 0.0), (2.4, 8.0), "", farbe=GRUEN, spitze=0.2, dicke=3.5, on=a)
    s.text(a, "+8 V", (1.85, 5.2), groesse=25, ausrichtung="right", farbe=GRUEN)
    s.pfeil((3.6, 8.0), (4.2, 10.0), "", farbe=GRUEN, spitze=0.17, dicke=3.5, on=a)
    s.text(a, "+2 V", (3.8, 10.6), groesse=25, ausrichtung="right", farbe=GRUEN)
    s.pfeil((5.4, 10.0), (6.2, 0.0), "", farbe=ROT, spitze=0.2, dicke=3.5, on=a)
    s.text(a, "−10 V", (6.0, 5.6), groesse=25, ausrichtung="left", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k8yspalte():
    """Links das Netz in Stromquellenform, rechts der Versuch zur Spalte 1 von Y."""
    s = Szene("et1/k8yspalte")
    yo, yu = 0.95, -0.95
    # ------- links
    xq1, xg1, x1, x2, xg5, xq2 = -3.17, -2.68, -2.2, -0.95, -0.42, 0.1
    s.draht((xq1, yo), (-1.95, yo))
    s.draht((-1.2, yo), (xq2, yo))
    s.draht((xq1, yu), (xq2, yu))
    iq(s, (xq1, yu), (xq1, yo), size=0.42)
    wid(s, (xg1, yo), (xg1, yu), size=0.32)
    wid(s, (x1, yo), (x1, yu), size=0.32)
    wid(s, (-1.95, yo), (-1.2, yo), size=0.32)
    wid(s, (x2, yo), (x2, yu), size=0.32)
    wid(s, (xg5, yo), (xg5, yu), size=0.32)
    iq(s, (xq2, yu), (xq2, yo), size=0.42)
    for x in (xg1, x1, x2, xg5):
        kn(s, x, yo)
        kn(s, x, yu)
    kn(s, x1, yo, ROT, 0.08)
    kn(s, x2, yo, ROT, 0.08)
    t(s, "U_1", (x1, yo + 0.3), "center", ROT)
    t(s, "U_2", (x2, yo + 0.3), "center", ROT)
    t(s, "G_3", (-1.57, yo - 0.33), "center")
    for x, n in ((xg1, "G_1"), (x1, "G_2"), (x2, "G_4"), (xg5, "G_5")):
        t(s, n, (x + 0.1, -0.68), "left", SCHWARZ, 22)
    ipfeil(s, (xq1 - 0.22, -0.4), (xq1 - 0.22, 0.4), "", None)
    ipfeil(s, (xq2 + 0.22, -0.4), (xq2 + 0.22, 0.4), "", None)
    t(s, "9 mA", (xq1 + 0.05, yu - 0.28), "center")
    t(s, "4 mA", (xq2 - 0.05, yu - 0.28), "center")
    # ------- rechts
    xa, xb, xd, xe, xf = 1.05, 1.62, 2.62, 3.02, 3.42
    s.draht((xa, yo), (1.77, yo))
    s.draht((2.47, yo), (xf, yo))
    s.draht((xa, yu), (xf, yu))
    wid(s, (xa, yo), (xa, yu), size=0.32)
    wid(s, (xb, yo), (xb, yu), size=0.32)
    wid(s, (1.77, yo), (2.47, yo), size=0.32)
    wid(s, (xe, yo), (xe, yu), size=0.32, farbe=HELLGRAU)
    wid(s, (xf, yo), (xf, yu), size=0.32, farbe=HELLGRAU)
    kn(s, xb, yo, ROT, 0.08)
    kn(s, xd, yo, ROT, 0.08)
    kn(s, xb, yu)
    kn(s, xe, yu)
    t(s, "1 V", (xb + 0.24, yo + 0.28), "center", ROT)
    t(s, "0 V", (xd - 0.24, yo + 0.28), "center", ROT)
    ipfeil(s, (xb - 0.3, yo + 0.3), (xb - 0.05, yo + 0.06), "1.75 mA", (xb - 0.33, yo + 0.34), BRAUN, "right", 23)
    ipfeil(s, (xd + 0.05, yo + 0.06), (xd + 0.3, yo + 0.3), "0.5 mA", (xd + 0.33, yo + 0.34), BRAUN, "left", 23)
    ipfeil(s, (xa + 0.13, 0.62), (xa + 0.13, 0.3), "", None, BLAU)
    ipfeil(s, (xb + 0.13, 0.62), (xb + 0.13, 0.3), "", None, BLAU)
    ipfeil(s, (1.92, yo - 0.2), (2.32, yo - 0.2), "", None, BLAU)
    t(s, "1", (xa + 0.13, -0.68), "left", BLAU, 23)
    t(s, "0.25", (xb + 0.13, -0.68), "left", BLAU, 23)
    t(s, "0.5", (2.12, yo - 0.46), "center", BLAU, 23)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k8zahl():
    """Welche Netze liegen über der Grenze z = 2k - 2?"""
    s = Szene("et1/k8zahl")
    a = s.achsen((1, 7, 1), (0, 14, 2), breite=5.0, hoehe=2.7, mitte=(0.15, 0), xl="k", yl="z", gitter=True)
    s.flaeche(a, "2*x-2", 1, 7, "14", farbe=BLAU, deckung=0.08)
    s.kurve(a, "2*x-2", farbe=ROT, dicke=4)
    s.kurve(a, "x-1", farbe=GRAU, dicke=3, dash=DASH)
    s.text(a, "z = 2k − 2", (6.1, 12.1), groesse=25, ausrichtung="right", farbe=ROT)
    s.text(a, "z = k − 1", (6.95, 3.9), groesse=24, ausrichtung="right", farbe=GRAU)
    s.text(a, s.tr("obenk", "Knoten kürzer", "nodes shorter", "nudos más corto", "节点法更短"), (1.2, 12.6), groesse=25, ausrichtung="left", farbe=BLAU)
    s.text(a, s.tr("untenm", "Maschen kürzer", "meshes shorter", "mallas más corto", "网孔法更短"), (6.95, 8.0), groesse=25, ausrichtung="right", farbe=GRUEN)
    pkte = [(2, 4, "par", "parallel", "parallel", "paralelo", "并联", "left", 0.14, 0.45),
            (3, 5, "rm", "Rechenmodell", "model network", "red modelo", "模型电路", "right", -0.1, 1.0),
            (4, 6, "br", "Brücke", "bridge", "puente", "电桥", "left", 0.12, -1.0),
            (5, 10, "vo", "jeder mit jedem", "all connected", "todos unidos", "全连接", "right", -0.14, 0.5),
            (6, 6, "ri", "Ring", "ring", "anillo", "环", "left", 0.14, 0.0)]
    for x, y, key, de, en, es, zh, aus, dx, dy in pkte:
        s.punkt(a, x, y, farbe=SCHWARZ, r=0.08)
        s.text(a, s.tr(key, de, en, es, zh), (x + dx, y + dy), groesse=24, ausrichtung=aus)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k8stempel():
    """Eintragsmuster von Leitwert, Stromquelle und gesteuerter Quelle."""
    s = Szene("et1/k8stempel")
    yo, yu = 0.7, -0.7

    def feld(x0, spalten, zeilen, werte):
        """Zwei mal zwei Einträge mit Zeilen- und Spaltenköpfen."""
        dx, dy = 0.6, 0.52
        xm, ytop = x0 + 0.26, 0.5
        matrix(s, xm, ytop, 2 * dx + 0.04, 2 * dy)
        for j, c in enumerate(spalten):
            t(s, c, (xm + 0.02 + (j + 0.5) * dx, ytop + 0.26), "center", GRAU, 23)
        for i, c in enumerate(zeilen):
            t(s, c, (xm - 0.14, ytop - (i + 0.5) * dy), "right", GRAU, 23)
            for j in range(2):
                wert, farbe = werte[i][j]
                t(s, wert, (xm + 0.02 + (j + 0.5) * dx, ytop - (i + 0.5) * dy), "center", farbe, 25)

    def enden(x):
        kn(s, x, yo)
        kn(s, x, yu)
        t(s, "i", (x, yo + 0.26))
        t(s, "k", (x, yu - 0.26))

    # Leitwert
    xs = -3.2
    s.draht((xs, yo), (xs, yu))
    wid(s, (xs, yo - 0.2), (xs, yu + 0.2), size=0.36)
    enden(xs)
    t(s, "G", (xs + 0.2, 0.0), "left")
    feld(xs + 0.48, ("i", "k"), ("i", "k"), [[("+G", BLAU), ("−G", ROT)], [("−G", ROT), ("+G", BLAU)]])
    # Stromquelle
    xs = -0.5
    iq(s, (xs, yu), (xs, yo), size=0.5)
    enden(xs)
    s.pfeil((xs + 0.24, -0.36), (xs + 0.24, 0.36), "", farbe=ROT, spitze=0.17, dicke=3)
    t(s, "I_q", (xs + 0.3, -0.6), "left", ROT)
    xm, ytop = xs + 0.92, 0.5
    matrix(s, xm, ytop, 0.7, 1.04)
    t(s, s.tr("rs", "rechts", "right", "derecha", "右端"), (xm + 0.35, ytop + 0.26), "center", GRAU, 23)
    t(s, "+I_q", (xm + 0.35, ytop - 0.26), "center", BLAU, 25)
    t(s, "−I_q", (xm + 0.35, ytop - 0.78), "center", ROT, 25)
    t(s, "i", (xm - 0.1, ytop - 0.26), "right", GRAU, 23)
    t(s, "k", (xm - 0.1, ytop - 0.78), "right", GRAU, 23)
    # gesteuerte Quelle
    xs = 1.5
    bau(s, "vccs", (xs, yo), (xs, yu), size=0.46)
    enden(xs)
    t(s, "g U_{pq}", (xs, yu - 0.58), "center")
    feld(xs + 0.42, ("p", "q"), ("i", "k"), [[("+g", BLAU), ("−g", ROT)], [("−g", ROT), ("+g", BLAU)]])
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k8verstaerker():
    """Verstärker mit Gegenkopplung: Knoten 3 hebt sich mit dem Ausgangsstrom."""
    s = Szene("et1/k8verstaerker")
    yo, ym, yu = 1.2, -0.15, -1.3
    xi, xq, x1, xr, xs, xg, xo, x2, xl = -3.25, -2.45, -1.75, -1.2, -0.45, 0.35, 1.2, 1.6, 2.6
    s.draht((xi, yo), (xr, yo))
    s.draht((xg, yo), (xl, yo))
    s.draht((xi, yu), (xl, yu))
    s.draht((xr, ym), (xo, ym))
    iq(s, (xi, yu), (xi, yo), size=0.58)
    wid(s, (xq, yo), (xq, yu), size=0.42)
    wid(s, (xr, yo), (xr, ym), size=0.42)
    bau(s, "vccs", (xg, yo), (xg, ym), size=0.56)
    wid(s, (xo, yo), (xo, ym), size=0.42)
    wid(s, (xl, yo), (xl, yu), size=0.42)
    wid(s, (xs, ym), (xs, yu), size=0.42)
    for x, y in ((xq, yo), (xq, yu), (xs, yu), (xo, yo)):
        kn(s, x, y)
    kn(s, x1, yo, ROT, 0.08)
    kn(s, x2, yo, ROT, 0.08)
    kn(s, xs, ym, ROT, 0.08)
    t(s, "1", (x1, yo + 0.3), "center", ROT, 28)
    t(s, "2", (x2, yo + 0.3), "center", ROT, 28)
    t(s, "3", (xs - 0.2, ym + 0.27), "center", ROT, 28)
    t(s, "0", (xl - 0.75, yu - 0.3), "center", ROT, 28)
    ipfeil(s, (xi - 0.25, -0.45), (xi - 0.25, 0.35), "I_q", (xi - 0.32, 0.0), BLAU, "right")
    t(s, "G_q", (xq + 0.2, -0.05), "left")
    t(s, "G_i", (xr + 0.2, 0.52), "left")
    t(s, "G_S", (xs + 0.2, -0.73), "left")
    t(s, "G_o", (xo + 0.2, 0.52), "left")
    t(s, "G_L", (xl + 0.2, -0.05), "left")
    t(s, "g (U_1 − U_3)", (xg + 0.1, yo + 0.3), "center", BRAUN)
    masse(s, xs, yu)
    # Pfad des Ausgangsstroms: Knoten 2, Quelle, Knoten 3, G_S, Masse, G_L
    s.pfeil((xg - 0.33, 0.85), (xg - 0.33, 0.15), "", farbe=ROT, spitze=0.18, dicke=4)
    s.pfeil((xg - 0.1, ym - 0.15), (xs + 0.15, ym - 0.15), "", farbe=ROT, spitze=0.18, dicke=4)
    s.pfeil((xs - 0.2, -0.4), (xs - 0.2, -1.05), "", farbe=ROT, spitze=0.18, dicke=4)
    s.pfeil((xl - 0.22, -0.5), (xl - 0.22, 0.4), "", farbe=ROT, spitze=0.18, dicke=4)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k8mna():
    """Erweiterung der Matrix um Quellenstrom und Quellengleichung."""
    s = Szene("et1/k8mna")
    # Quelle
    xs, yo, yu = -3.35, 0.95, -0.95
    uq(s, (xs, yo), (xs, yu), size=0.6)
    kn(s, xs, yo)
    kn(s, xs, yu)
    t(s, "i", (xs, yo + 0.26))
    t(s, "k", (xs, yu - 0.26))
    t(s, "+", (xs - 0.33, 0.42), "center", ROT)
    t(s, "U_q", (xs - 0.36, 0.0), "right", ROT)
    s.pfeil((xs + 0.22, 0.75), (xs + 0.22, 0.42), "", farbe=GRUEN, spitze=0.17, dicke=3)
    t(s, "I_V", (xs + 0.3, 0.6), "left", GRUEN)
    # Matrix
    x0, ytop, b, h = -2.05, 1.1, 2.75, 2.2
    matrix(s, x0, ytop, b, h)
    block_b, block_h = 1.95, 1.5
    s.box("Y", (x0 + 0.1 + 0.5 * block_b, ytop - 0.1 - 0.5 * block_h), breite=block_b, hoehe=block_h, farbe=BLAU, fuellung=HELLBLAU, dicke=2.5, groesse=30)
    xn, yn = x0 + 2.4, ytop - 1.9          # neue Spalte, neue Zeile
    yi, yk = ytop - 0.5, ytop - 1.2
    xi_, xk_ = x0 + 0.55, x0 + 1.5
    s.linie(None, (x0 + 0.08, yi), (x0 + 2.08, yi), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(None, (x0 + 0.08, yk), (x0 + 2.08, yk), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(None, (xi_, ytop - 0.08), (xi_, ytop - 1.6), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(None, (xk_, ytop - 0.08), (xk_, ytop - 1.6), farbe=GRAU, dicke=1.5, dash=DOT)
    t(s, "+1", (xn, yi), "center", GRUEN, 25)
    t(s, "−1", (xn, yk), "center", GRUEN, 25)
    t(s, "+1", (xi_, yn), "center", ROT, 25)
    t(s, "−1", (xk_, yn), "center", ROT, 25)
    t(s, "0", (xn, yn), "center", SCHWARZ, 25)
    t(s, "i", (xi_, ytop + 0.24), "center", GRAU, 23)
    t(s, "k", (xk_, ytop + 0.24), "center", GRAU, 23)
    t(s, "i", (x0 - 0.12, yi), "right", GRAU, 23)
    t(s, "k", (x0 - 0.12, yk), "right", GRAU, 23)
    # Vektoren
    x1 = x0 + b + 0.16
    matrix(s, x1, ytop, 0.62, h)
    t(s, "U", (x1 + 0.31, ytop - 0.85), "center", SCHWARZ, 27)
    t(s, "I_V", (x1 + 0.31, yn), "center", GRUEN, 25)
    t(s, "=", (x1 + 0.84, ytop - 1.1), "center", SCHWARZ, 28)
    x2 = x1 + 1.05
    matrix(s, x2, ytop, 0.66, h)
    t(s, "I_q", (x2 + 0.33, ytop - 0.85), "center", SCHWARZ, 27)
    t(s, "U_q", (x2 + 0.33, yn), "center", ROT, 25)
    s.speichern()


ALLE = (k8netz, k8kreis, k8maschen, k8hoehen, k8yspalte, k8zahl, k8stempel, k8verstaerker, k8mna)

if __name__ == "__main__":
    for f in ALLE:
        f()
    print(len(ALLE), "Szenen")
