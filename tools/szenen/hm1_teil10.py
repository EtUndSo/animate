"""Höhere Mathematik 1, Teil 10 (kap10_stufen.tex): Matrizen und lineare Gleichungssysteme.

Aufruf: python tools/szenen/hm1_teil10.py, danach python tools/szenen_ansehen.py out.png hm1/k10quadrat ... [--lang de]
Alle Zahlen stehen im Heft und in C:/Bücher/HöMa1/Arbeitshefte/rechnung_kap10.py. Rechenmodell: Drehung D, Scherung S,
Presse P = (1 2; 2 4), Spiegelung an der Geraden durch v = (3/5, 4/5). Alle Ebenen haben in x und y denselben Maßstab.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24                    # Beschriftung in den Bildern
HELLBLAU, HELLGRUEN, HELLORANGE, HELLROT, HELLGR = "#dceafa", "#d6efe0", "#fbe3d9", "#f8dcdc", "#eeeeee"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche


def ganz(v):
    """Ganzzahlige Ticks ohne die Null."""
    import math
    return ";".join(str(k) for k in range(math.ceil(v[0] + 0.05), math.floor(v[1] - 0.05) + 1) if k)


def ebene(s, x, y, m, mitte=(0, 0), xt=None, yt=None, xl="x_1", yl="x_2", titel="", **kw):
    """Achsenkreuz mit m Szeneneinheiten je Zahlschritt, in beiden Richtungen gleich; Ticks ganzzahlig."""
    kw.setdefault("xzahlen", False)
    kw.setdefault("yzahlen", False)
    xt = ganz(x) if xt is None else xt
    yt = ganz(y) if yt is None else yt
    return s.achsen(x, y, breite=(x[1] - x[0]) * m, hoehe=(y[1] - y[0]) * m, mitte=mitte, kreuz=True, xticks=xt, yticks=yt,
                    xl=xl, yl=yl, titel=titel, **kw)


def vek(s, on, a, b, farbe=BLAU, dicke=4, spitze=0.18, dash=""):
    return s.pfeil(a, b, "", farbe=farbe, spitze=spitze, dicke=dicke, on=on, dash=dash)


def viereck(s, on, ecken, farbe=BLAU, deckung=0.18, rand=2.5):
    return s._add("Polygon", {"vertices": [[x, y, 0] for x, y in ecken], "color": farbe, "fill_color": farbe, "fill_opacity": deckung,
                              "stroke_width": rand}, on)


def mal(m, x):
    return (m[0][0] * x[0] + m[0][1] * x[1], m[1][0] * x[0] + m[1][1] * x[1])


D = ((0, -1), (1, 0))
S = ((1, 1), (0, 1))
QUADRAT = ((0, 0), (1, 0), (1, 1), (0, 1))


def bild_quadrat(s, on, spalte1, spalte2, farbe=BLAU, f1=ROT, f2=GRUEN):
    """Bild des Einheitsquadrats, die Pfeile sind die Spalten der Matrix."""
    ecke = (spalte1[0] + spalte2[0], spalte1[1] + spalte2[1])
    viereck(s, on, ((0, 0), spalte1, ecke, spalte2), farbe=farbe)
    vek(s, on, (0, 0), spalte1, farbe=f1)
    vek(s, on, (0, 0), spalte2, farbe=f2)


# ------------------------------------------------------------------------------------------ Stufe 1
def k10linear():
    """Parallelogramm aus a und b, rechts sein Bild unter der Scherung S."""
    s = Szene("hm1/k10linear")
    s.welt()
    m = 0.68
    a = ebene(s, (-1.5, 2.3), (-0.4, 2.7), m, mitte=(-1.95, 0), xl="", yl="", titel=s.tr("vor", "vorher", "before", "antes", "变换前"))
    b = ebene(s, (-0.4, 3.9), (-0.4, 2.7), m, mitte=(1.75, 0), xl="", yl="", titel=s.tr("nach", "nachher", "after", "después", "变换后"))
    pa, pb, ps = (2, 1), (-1, 1), (1, 2)
    viereck(s, a, ((0, 0), pa, ps, pb), farbe=BLAU, deckung=0.12, rand=0)
    vek(s, a, (0, 0), pa, farbe=ROT)
    vek(s, a, (0, 0), pb, farbe=GRUEN)
    vek(s, a, (0, 0), ps, farbe=BLAU)
    s.linie(a, pa, ps, farbe=GRAU, dash=DASH, dicke=2.5)
    s.linie(a, pb, ps, farbe=GRAU, dash=DASH, dicke=2.5)
    s.text(a, "a", (1.72, 0.52), KL, "left", ROT)
    s.text(a, "b", (-0.86, 0.5), KL, "right", GRUEN)
    s.text(a, "a + b", (1.1, 2.3), KL, "left", BLAU)
    qa, qb, qs = mal(S, pa), mal(S, pb), mal(S, ps)
    viereck(s, b, ((0, 0), qa, qs, qb), farbe=BLAU, deckung=0.12, rand=0)
    vek(s, b, (0, 0), qa, farbe=ROT)
    vek(s, b, (0, 0), qb, farbe=GRUEN)
    vek(s, b, (0, 0), qs, farbe=BLAU)
    s.linie(b, qa, qs, farbe=GRAU, dash=DASH, dicke=2.5)
    s.linie(b, qb, qs, farbe=GRAU, dash=DASH, dicke=2.5)
    s.text(b, "S a", (2.1, 0.32), KL, "left", ROT)
    s.text(b, "S b", (0.1, 1.42), KL, "left", GRUEN)
    s.text(b, "S (a + b) = S a + S b", (3.75, 2.35), KL, "right", BLAU)
    s.pfeil((-0.62, 0.2), (-0.1, 0.2), "S", farbe=SCHWARZ, spitze=0.18, dicke=3)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k10quadrat():
    """Einheitsquadrat, sein Bild unter der Drehung D und unter der Scherung S. Die Pfeile sind die Spalten der Matrix."""
    s = Szene("hm1/k10quadrat")
    m = 0.58
    xb, yb = (-1.3, 2.2), (-0.9, 2.1)
    leer = dict(xl="", yl="", titel_mitte=True)
    a = ebene(s, xb, yb, m, mitte=(-2.22, 0), titel=s.tr("aus", "Ausgang", "Start", "Inicio", "原图"), **leer)
    b = ebene(s, xb, yb, m, mitte=(0, 0), titel=s.tr("dr", "Drehung D", "Rotation D", "Rotación D", "旋转 D"), **leer)
    c = ebene(s, xb, yb, m, mitte=(2.22, 0), titel=s.tr("sc", "Scherung S", "Shear S", "Cizalla S", "剪切 S"), **leer)
    bild_quadrat(s, a, (1, 0), (0, 1), farbe=GRAU)
    s.text(a, "e_1", (1.12, 0.32), KL, "left", ROT)
    s.text(a, "e_2", (0.14, 1.42), KL, "left", GRUEN)
    bild_quadrat(s, b, (0, 1), (-1, 0))
    s.text(b, "D e_1", (0.14, 1.42), KL, "left", ROT)
    s.text(b, "D e_2", (-0.5, -0.46), KL, "center", GRUEN)
    bild_quadrat(s, c, (1, 0), (1, 1))
    s.text(c, "S e_1", (0.62, -0.46), KL, "center", ROT)
    s.text(c, "S e_2", (0.2, 1.42), KL, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k10kern():
    """Die Presse P: Jede Parallele zum Kern fällt auf einen Punkt des Bilds. Die Bildgerade hat Richtung (1, 2)."""
    s = Szene("hm1/k10kern")
    s.welt()
    a = ebene(s, (-3.4, 4.1), (-2.4, 3.0), 0.44, mitte=(-1.75, 0), xl="", yl="")
    b = ebene(s, (-2.8, 4.4), (-5.2, 7.2), 0.27, mitte=(2.0, 0), xl="", yl="", xt="-2;2;4", yt="-4;-2;2;4;6")

    def gerade(on, c, farbe, dicke=4):
        return s.linie(on, (-3.2, (c + 3.2) / 2), (4.0, (c - 4.0) / 2), farbe=farbe, dicke=dicke)
    gerade(a, 0, ROT, 5)
    gerade(a, 3, BLAU)
    gerade(a, -2, GRUEN)
    for p in ((1, 1), (3, 0), (-1, 2)):
        s.punkt(a, p[0], p[1], farbe=BLAU)
    s.punkt(a, -2, 0, farbe=GRUEN)
    s.punkt(a, 0, -1, farbe=GRUEN)
    s.punkt(a, 0, 0, farbe=ROT)
    s.punkt(a, -2, 1, farbe=ROT)
    s.text(a, s.tr("kern", "Kern", "Kernel", "Núcleo", "核"), (-3.1, 2.0), KL, "left", ROT)
    s.text(a, "x_1 + 2 x_2 = 3", (3.9, 1.2), KL, "right", BLAU)
    s.text(a, "x_1 + 2 x_2 = -2", (-3.2, -1.75), KL, "left", GRUEN)

    s.linie(b, (-2.6, -5.2), (3.6, 7.2), farbe=GRAU, dicke=4)
    s.punkt(b, 0, 0, farbe=ROT, r=0.1)
    s.punkt(b, 3, 6, farbe=BLAU, r=0.1)
    s.punkt(b, -2, -4, farbe=GRUEN, r=0.1)
    s.text(b, "(3, 6)", (2.4, 6.4), KL, "right", BLAU)
    s.text(b, "(-2, -4)", (0.35, -4.2), KL, "left", GRUEN)
    s.text(b, "0", (0.5, -0.9), KL, "left", ROT)
    s.text(b, s.tr("bild", "Bild", "Image", "Imagen", "像"), (2.4, 2.6), KL, "left", GRAU)
    s.pfeil((-0.05, 1.5), (0.55, 1.5), "P", farbe=SCHWARZ, spitze=0.18, dicke=3)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k10schema():
    """Oben die Abbildung im Vektorraum, unten dieselbe Abbildung in Koordinaten."""
    s = Szene("hm1/k10schema")
    hell = dict(breite=1.5, hoehe=0.72, form="round", dicke=2.5)
    xl, xr, yo, yu = -1.75, 1.75, 1.0, -1.0
    s.box("V", (xl, yo), fuellung=HELLBLAU, **hell)
    s.box("W", (xr, yo), fuellung=HELLBLAU, **hell)
    s.box("𝕂ⁿ", (xl, yu), fuellung=HELLGRUEN, **hell)
    s.box("𝕂ᵐ", (xr, yu), fuellung=HELLGRUEN, **hell)
    s.pfeil((xl + 0.8, yo), (xr - 0.8, yo), "L", farbe=BLAU, spitze=0.2, dicke=3.5)
    s.pfeil((xl + 0.8, yu), (xr - 0.8, yu), "ℒ", farbe=GRUEN, spitze=0.2, dicke=3.5, label_seite="right")
    s.pfeil((xl, yu + 0.4), (xl, yo - 0.4), "", farbe=GRAU, spitze=0.18, dicke=3, doppelt=True)
    s.pfeil((xr, yu + 0.4), (xr, yo - 0.4), "", farbe=GRAU, spitze=0.18, dicke=3, doppelt=True)
    s.text(None, "Φ_B", (xl - 0.15, 0.0), KL, "right", SCHWARZ)
    s.text(None, "Φ_C", (xr + 0.15, 0.0), KL, "left", SCHWARZ)
    s.text(None, "v", (xl, yo + 0.62), KL, "center", BLAU)
    s.text(None, "w = L(v)", (xr, yo + 0.62), KL, "center", BLAU)
    s.text(None, "v_B", (xl, yu - 0.62), KL, "center", GRUEN)
    s.text(None, "w_C = ℒ v_B", (xr, yu - 0.62), KL, "center", GRUEN)
    s.speichern()


def k10spiegel():
    """Links die Spiegelung an G, rechts dieselbe Abbildung in zwei Basen."""
    s = Szene("hm1/k10spiegel")
    s.welt()
    m = 0.95
    v, w = (0.6, 0.8), (-0.8, 0.6)
    a = ebene(s, (-0.7, 2.6), (-0.4, 2.9), m, mitte=(-1.75, 0), xl="", yl="")
    b = ebene(s, (-1.4, 1.6), (-1.15, 1.75), m, mitte=(1.75, 0), xl="", yl="")

    def g(on, t0, t1):
        return s.linie(on, (t0 * v[0], t0 * v[1]), (t1 * v[0], t1 * v[1]), farbe=GRAU, dash=DASH, dicke=2.5)
    g(a, -0.5, 3.3)
    s.text(a, "G", (1.98, 2.62), KL, "left", GRAU)
    pa, pp, pl = (2, 1), (1.2, 1.6), (0.4, 2.2)
    vek(s, a, (0, 0), pa, farbe=BLAU)
    vek(s, a, (0, 0), pl, farbe=ROT)
    vek(s, a, pa, pp, farbe=GRUEN)
    vek(s, a, pp, pl, farbe=GRUEN)
    s.punkt(a, pp[0], pp[1], farbe=SCHWARZ)
    s.text(a, "a", (2.08, 0.78), KL, "left", BLAU)
    s.text(a, "L(a)", (0.3, 2.58), KL, "center", ROT)
    s.text(a, "Proj_G(a)", (1.38, 1.76), KL, "left", SCHWARZ)
    s.text(a, "b", (1.72, 1.46), KL, "left", GRUEN)
    s.text(a, "b", (0.9, 2.08), KL, "left", GRUEN)

    g(b, -1.3, 1.9)
    vek(s, b, (0, 0), v, farbe=BLAU)
    vek(s, b, (0, 0), w, farbe=GRUEN)
    vek(s, b, (0, 0), (0.8, -0.6), farbe=GRUEN, dash=DASH)
    s.text(b, "L(v) = v", (0.66, 0.3), KL, "left", BLAU)
    s.text(b, "u", (-0.98, 0.7), KL, "center", GRUEN)
    s.text(b, "L(u) = -u", (0.9, -0.72), KL, "center", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k10produkt():
    """Oben erst D, dann S; unten erst S, dann D. Das Ergebnis ist verschieden."""
    s = Szene("hm1/k10produkt")
    s.welt()
    m = 0.5
    xb, yb = (-1.5, 2.2), (-0.35, 2.4)
    xs = (-2.4, 0.0, 2.4)
    yo, yu = 0.82, -0.88
    panels = {}
    for z, y in enumerate((yo, yu)):
        for sp, x in enumerate(xs):
            panels[z, sp] = ebene(s, xb, yb, m, mitte=(x, y), xl="", yl="")

    def zeile(z, y, erste, zweite, f1, name1, name2):
        p0, p1, p2 = panels[z, 0], panels[z, 1], panels[z, 2]
        bild_quadrat(s, p0, (1, 0), (0, 1), farbe=GRAU)
        s1, s2 = mal(erste, (1, 0)), mal(erste, (0, 1))
        bild_quadrat(s, p1, s1, s2, farbe=f1)
        t1, t2 = mal(zweite, s1), mal(zweite, s2)
        bild_quadrat(s, p2, t1, t2, farbe=f1)
        s.pfeil((xs[0] + 0.96, y + 0.2), (xs[1] - 0.96, y + 0.2), name1, farbe=SCHWARZ, spitze=0.15, dicke=3)
        s.pfeil((xs[1] + 0.96, y + 0.2), (xs[2] - 0.96, y + 0.2), name2, farbe=SCHWARZ, spitze=0.15, dicke=3)

    zeile(0, yo, D, S, BLAU, "D", "S")
    zeile(1, yu, S, D, ORANGE, "S", "D")
    s.text(panels[0, 2], "S D", (1.2, 2.05), KL, "left", BLAU)
    s.text(panels[1, 2], "D S", (0.3, 1.5), KL, "left", BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k10faelle():
    """Zwei Gleichungen, zwei Unbekannte: Schnittpunkt, parallel, gleich."""
    s = Szene("hm1/k10faelle")
    m = 0.52
    xb, yb = (-0.6, 3.3), (-0.6, 3.3)
    t1 = s.tr("f1", "genau eine Lösung", "exactly one solution", "una solución", "唯一解")
    t2 = s.tr("f2", "keine Lösung", "no solution", "sin solución", "无解")
    t3 = s.tr("f3", "unendlich viele", "infinitely many", "infinitas", "无穷多解")
    leer = dict(xl="", yl="", xzahlen=True, yzahlen=True, titel_mitte=True)
    a = ebene(s, xb, yb, m, mitte=(-2.26, 0), titel=t1, **leer)
    b = ebene(s, xb, yb, m, mitte=(0, 0), titel=t2, **leer)
    c = ebene(s, xb, yb, m, mitte=(2.26, 0), titel=t3, **leer)

    def z1(on, f=BLAU, d=4, dash=""):
        return s.linie(on, (-0.2, 3.2), (3.2, -0.2), farbe=f, dicke=d, dash=dash)
    z1(a)
    s.linie(a, (1.2, -0.6), (3.1, 3.2), farbe=ROT, dicke=4)
    s.punkt(a, 2, 1, farbe=SCHWARZ, r=0.09)
    s.text(a, "(2, 1)", (0.85, 0.72), KL, "center", SCHWARZ)
    z1(b)
    s.linie(b, (-0.2, 1.2), (1.2, -0.2), farbe=ROT, dicke=4)
    z1(c, ROT, 8)
    z1(c, BLAU, 3)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k10gauss():
    """Zeilenumformungen drehen die Geraden um den Lösungspunkt, der Punkt bleibt."""
    s = Szene("hm1/k10gauss")
    m = 0.52
    xb, yb = (-0.6, 3.3), (-0.6, 3.3)
    t1 = s.tr("g1", "Ausgang", "Start", "Inicio", "原方程组")
    leer = dict(xl="", yl="", xzahlen=True, yzahlen=True, titel_mitte=True)
    a = ebene(s, xb, yb, m, mitte=(-2.26, 0), titel=t1, **leer)
    b = ebene(s, xb, yb, m, mitte=(0, 0), titel="Z_2 - 2 Z_1", **leer)
    c = ebene(s, xb, yb, m, mitte=(2.26, 0), titel="Z_1 + Z_2 / 3", **leer)
    # x1 + x2 = 3, 2 x1 - x2 = 3, nach Z2 - 2 Z1: -3 x2 = -3, nach Z1 + Z2/3: x1 = 2
    s.linie(a, (-0.2, 3.2), (3.2, -0.2), farbe=BLAU, dicke=4)
    s.linie(a, (1.2, -0.6), (3.1, 3.2), farbe=ROT, dicke=4)
    s.linie(b, (-0.2, 3.2), (3.2, -0.2), farbe=BLAU, dicke=4)
    s.linie(b, (-0.5, 1), (3.2, 1), farbe=ROT, dicke=4)
    s.linie(c, (2, -0.5), (2, 3.2), farbe=BLAU, dicke=4)
    s.linie(c, (-0.5, 1), (3.2, 1), farbe=ROT, dicke=4)
    for p in (a, b, c):
        s.punkt(p, 2, 1, farbe=SCHWARZ, r=0.09)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k10stufen():
    """Zeilenstufenform: Treppe aus Pivots, darunter Nullen, freie Spalten ohne Pivot."""
    s = Szene("hm1/k10stufen")
    b = 0.6
    zeilen = ("p*****", "00p***", "000p**", "000000")
    x0, y0 = -2.6, 1.15
    for i, z in enumerate(zeilen):
        for j, c in enumerate(z):
            mx, my = x0 + b * j, y0 - b * i
            if c == "p":
                s.box("≠ 0", (mx, my), breite=b, hoehe=b, dicke=1.5, fuellung=HELLROT, farbe=ROT, groesse=KL)
            elif c == "*":
                s.box("*", (mx, my), breite=b, hoehe=b, dicke=1.5, fuellung=HELLGR, farbe=GRAU, groesse=KL)
            else:
                s.box("0", (mx, my), breite=b, hoehe=b, dicke=1.5, fuellung="#ffffff", farbe=HELLGRAU, groesse=KL)
    # Treppe
    li, ob = x0 - b / 2, y0 + b / 2
    pkte = ((li, ob - b), (li + 2 * b, ob - b), (li + 2 * b, ob - 2 * b), (li + 3 * b, ob - 2 * b), (li + 3 * b, ob - 3 * b), (li + 6 * b, ob - 3 * b))
    s.draht(*pkte, farbe=ROT, dicke=4)
    re = x0 + 5.5 * b + 0.2
    s.linie(None, (re, ob), (re, ob - 3 * b + 0.04), farbe=SCHWARZ, dicke=2.5)
    s.linie(None, (re, ob - 3 * b - 0.04), (re, ob - 4 * b), farbe=GRAU, dicke=2.5)
    s.text(None, s.tr("rz", "r = 3 Zeilen mit Pivot", "r = 3 rows with pivot", "r = 3 filas con pivote", "r = 3 行含主元"), (re + 0.15, ob - 1.5 * b), KL, "left", SCHWARZ)
    s.text(None, s.tr("nz", "m - r = 1 Nullzeile", "m - r = 1 zero row", "m - r = 1 fila nula", "m - r = 1 零行"), (re + 0.15, ob - 3.5 * b), KL, "left", GRAU)
    for j in (1, 4, 5):
        s.text(None, s.tr("fr%d" % j, "frei", "free", "libre", "自由"), (x0 + b * j, y0 - 3.5 * b - 0.3), KL, "center", BLAU)
    s.speichern()


if __name__ == "__main__":
    for f in (k10linear, k10quadrat, k10kern, k10schema, k10spiegel, k10produkt, k10faelle, k10gauss, k10stufen):
        f()
