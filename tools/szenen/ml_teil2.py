"""Machine Learning Teil 2 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap2_stufen.tex, kap2_stufen_b.tex): Abbildungen.

Szenenname ml/k2<name> = \\label{fig:k2<name>} im Heft. Stil wie tools/szenen/ml_teil1.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil2.py
Export: python tools/export_szenen.py ml/k2<name> ...   (jedes Bild höchstens 548 px breit)
Szenen mit mehreren Teilbildern rufen zuerst s.welt() auf: Danach sind Texte ohne on= in Szeneneinheiten.
Die Rechenbilder ml/k2r<name> zeigen eine Summe oder ein Skalarprodukt Schritt für Schritt (skalarprodukt, formel);
Formeln ohne Dezimalzahlen, weil MathTex sie nicht je Sprache umschreibt.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24
HELLBLAU = "#9ec3ec"
ROT_HELL = "#f4c7c7"
GRUEN_HELL = "#c4e3cf"
BLAU_HELL = "#cfe0f5"
ORANGE_HELL = "#f5c4a8"


def zug(s, on, pts, farbe=SCHWARZ, dicke=3, dash=""):
    """Linienzug in Datenkoordinaten."""
    return s.daten(on, pts, farbe=farbe, dicke=dicke, dash=dash)


def ellipse(mx, my, ax, ay, phi=0.0, n=97):
    """Punkte einer Ellipse mit den Halbachsen ax, ay, um phi (Grad) gedreht."""
    c, s_ = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / (n - 1)
        x, y = ax * math.cos(t), ay * math.sin(t)
        pts.append((mx + c * x - s_ * y, my + s_ * x + c * y))
    return pts


def rechter_winkel(s, on, p, u, v, g=0.2, farbe=GRAU):
    """Winkelzeichen am Punkt p zwischen den Richtungen u und v (Einheitsvektoren)."""
    a = (p[0] + g * u[0], p[1] + g * u[1])
    b = (a[0] + g * v[0], a[1] + g * v[1])
    c = (p[0] + g * v[0], p[1] + g * v[1])
    zug(s, on, [a, b, c], farbe=farbe, dicke=2)


# ------------------------------------------------------------------ Abschnitt 1
def k2onb():
    s = Szene("ml/k2onb")
    a = s.achsen((-1.4, 3.6), (-1.5, 2.9), breite=4.6, hoehe=4.05, kreuz=True, xticks="1;2;3", yticks="1;2", xl="x₁", yl="x₂")
    s.linie(a, (-0.6, -0.8), (1.95, 2.6), farbe=HELLGRAU, dicke=2)
    s.linie(a, (1.92, -1.44), (-1.2, 0.9), farbe=HELLGRAU, dicke=2)
    s.linie(a, (3, 1), (1.56, 2.08), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (3, 1), (1.44, -1.08), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (0, 0), (1.56, 2.08), farbe=HELLBLAU, dicke=10)
    s.linie(a, (0, 0), (1.44, -1.08), farbe=ORANGE_HELL, dicke=10)
    s.pfeil((0, 0), (0.6, 0.8), on=a, farbe=GRUEN, dicke=5, spitze=0.15)
    s.pfeil((0, 0), (-0.8, 0.6), on=a, farbe=GRUEN, dicke=5, spitze=0.15)
    s.pfeil((0, 0), (3, 1), on=a, farbe=ROT, dicke=4, spitze=0.17)
    s.punkt(a, 1.56, 2.08, farbe=BLAU, r=0.07)
    s.punkt(a, 1.44, -1.08, farbe=ORANGE, r=0.07)
    s.text(a, "q₁", (0.75, 0.55), MITTEL, "left", GRUEN)
    s.text(a, "q₂", (-0.85, 0.85), MITTEL, "center", GRUEN)
    s.text(a, "x", (3.1, 1.05), MITTEL, "left", ROT)
    s.text(a, "2.6 q₁", (1.4, 2.25), MITTEL, "right", BLAU)
    s.text(a, "−1.8 q₂", (1.3, -1.2), MITTEL, "right", ORANGE)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k2lot():
    s = Szene("ml/k2lot")
    a = s.achsen((-0.5, 5.0), (-0.7, 5.0), breite=4.4, hoehe=4.56, kreuz=True, xticks="1;2;3;4", yticks="1;2;3;4", xl="x₁", yl="x₂")
    s.linie(a, (-0.3, -0.6), (2.45, 4.9), farbe=HELLGRAU, dicke=2)
    s.linie(a, (1, 2), (4, 3), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (2, 4), (4, 3), farbe=BLAU, dicke=5)
    rechter_winkel(s, a, (2, 4), (0.894, -0.447), (-0.447, -0.894))
    s.pfeil((0, 0), (1, 2), on=a, farbe=GRUEN, dicke=5, spitze=0.17)
    s.pfeil((0, 0), (4, 3), on=a, farbe=ROT, dicke=4, spitze=0.18)
    s.punkt(a, 2, 4, farbe=BLAU, r=0.08)
    s.punkt(a, 1, 2, farbe=GRAU, r=0.07)
    s.text(a, "a", (0.35, 1.15), MITTEL, "right", GRUEN)
    s.text(a, "y", (4.1, 2.95), MITTEL, "left", ROT)
    s.text(a, "ŷ = (2, 4)ᵀ", (1.85, 4.3), MITTEL, "right", BLAU)
    s.text(a, "r = y − ŷ", (3.1, 3.75), MITTEL, "left", BLAU)
    s.text(a, "(1, 2)ᵀ", (1.12, 1.75), KLEIN, "left", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3
def k2ebene():
    s = Szene("ml/k2ebene")
    w = s.welt()
    f, ox, oy = 1.25, -0.4, -1.2

    def P(x, y, z):
        return (ox + f * (-0.62 * x + 1.45 * y), oy + f * (-0.42 * x + 1.45 * z))

    ecken = [(-0.35, -0.35, -0.7), (1.55, -0.35, 1.2), (1.55, 1.45, 3.0), (-0.35, 1.45, 1.1)]
    for k in range(1, 6):                                     # Gitterlinien der Ebene als leichte Fläche
        t = k / 6
        p0 = [ecken[0][i] + t * (ecken[3][i] - ecken[0][i]) for i in range(3)]
        p1 = [ecken[1][i] + t * (ecken[2][i] - ecken[1][i]) for i in range(3)]
        zug(s, w, [P(*p0), P(*p1)], farbe=BLAU_HELL, dicke=2)
        q0 = [ecken[0][i] + t * (ecken[1][i] - ecken[0][i]) for i in range(3)]
        q1 = [ecken[3][i] + t * (ecken[2][i] - ecken[3][i]) for i in range(3)]
        zug(s, w, [P(*q0), P(*q1)], farbe=BLAU_HELL, dicke=2)
    zug(s, w, [P(*e) for e in ecken + [ecken[0]]], farbe=HELLBLAU, dicke=3)
    for ende, name, d in (((2.3, 0, 0), "x₁", (-0.3, -0.15)), ((0, 2.2, 0), "x₂", (0.15, 0)), ((0, 0, 2.3), "x₃", (0.05, 0.15))):
        s.pfeil(P(0, 0, 0), P(*ende), on=w, farbe=GRAU, dicke=2, spitze=0.13)
        q = P(*ende)
        s.text(w, name, (q[0] + d[0], q[1] + d[1]), KLEIN, "center", GRAU)
    s.pfeil(P(0, 0, 0), P(1, 0, 1), on=w, farbe=GRUEN, dicke=5, spitze=0.15)
    s.pfeil(P(0, 0, 0), P(0, 1, 1), on=w, farbe=GRUEN, dicke=5, spitze=0.15)
    s.pfeil(P(0, 0, 0), P(1, 1, 1), on=w, farbe=ROT, dicke=4, spitze=0.16)
    s.pfeil(P(0, 0, 0), P(2 / 3, 2 / 3, 4 / 3), on=w, farbe=BLAU, dicke=4, spitze=0.16)
    s.linie(w, P(2 / 3, 2 / 3, 4 / 3), P(1, 1, 1), farbe=BLAU, dicke=5)
    s.punkt(w, *P(2 / 3, 2 / 3, 4 / 3), farbe=BLAU, r=0.07)
    for (x, y, z), t, d, al, fa in (((1, 0, 1), "a₁", (-0.15, 0.05), "right", GRUEN), ((0, 1, 1), "a₂", (0.15, -0.15), "left", GRUEN),
                                    ((1, 1, 1), "y", (0.05, -0.28), "center", ROT), ((2 / 3, 2 / 3, 4 / 3), "ŷ = Ax̂", (0, 0.2), "center", BLAU),
                                    ((0.85, 0.85, 1.17), "r", (0.2, 0.05), "left", BLAU)):
        q = P(x, y, z)
        s.text(w, t, (q[0] + d[0], q[1] + d[1]), MITTEL, al, fa)
    q = P(1.5, 1.3, 2.55)
    s.text(w, s.tr("spr", "Spaltenraum", "column space", "espacio columna", "列空间", fr="espace des colonnes", tr="sütun uzayı"), q,
           KLEIN, "center", BLAU)
    s.speichern()


def k2ausgleich():
    s = Szene("ml/k2ausgleich")
    a = s.achsen((-0.3, 2.6), (-0.3, 4.9), breite=3.6, hoehe=3.4, kreuz=True, xticks="1;2", yticks="1;2;3;4", xl="t", yl="y")
    s.linie(a, (-0.2, 5 / 6 - 0.3), (2.4, 5 / 6 + 3.6), farbe=BLAU, dicke=4)
    for t, yv in ((0, 1), (1, 2), (2, 4)):
        s.linie(a, (t, yv), (t, 5 / 6 + 1.5 * t), farbe=ROT, dicke=8)
        s.punkt(a, t, yv, farbe=SCHWARZ, r=0.07)
    s.text(a, "y = 5/6 + 3/2 · t", (1.3, 3.75), KLEIN, "right", BLAU)
    s.text(a, "r₁ = 1/6", (0.12, 0.45), KLEIN, "left", ROT)
    s.text(a, "r₂ = −1/3", (1.08, 1.75), KLEIN, "left", ROT)
    s.text(a, "r₃ = 1/6", (1.92, 4.3), KLEIN, "right", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k2gramschmidt():
    s = Szene("ml/k2gramschmidt")
    a = s.achsen((-0.9, 2.4), (-0.3, 2.3), breite=4.6, hoehe=3.62, kreuz=True, xticks="1;2", yticks="1;2", xl="x₁", yl="x₂")
    s.linie(a, (-0.4, -0.2), (2.3, 1.15), farbe=HELLGRAU, dicke=2)
    s.linie(a, (0, 0), (1.6, 0.8), farbe=HELLBLAU, dicke=10)
    s.linie(a, (1, 2), (1.6, 0.8), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (-0.6, 1.2), (1, 2), farbe=GRAU, dicke=2, dash=DOT)
    s.pfeil((0, 0), (2, 1), on=a, farbe=SCHWARZ, dicke=4, spitze=0.16)
    s.pfeil((0, 0), (1, 2), on=a, farbe=ROT, dicke=4, spitze=0.16)
    s.pfeil((0, 0), (-0.6, 1.2), on=a, farbe=ORANGE, dicke=5, spitze=0.16)
    s.pfeil((0, 0), (0.894, 0.447), on=a, farbe=GRUEN, dicke=5, spitze=0.14)
    s.pfeil((0, 0), (-0.447, 0.894), on=a, farbe=GRUEN, dicke=5, spitze=0.14)
    s.text(a, "a₁", (2.05, 1.0), MITTEL, "left")
    s.text(a, "a₂", (1.0, 2.1), MITTEL, "center", ROT)
    s.text(a, "q̃₂", (-0.65, 1.3), MITTEL, "right", ORANGE)
    s.text(a, "q₁", (0.75, 0.2), MITTEL, "center", GRUEN)
    s.text(a, "q₂", (-0.3, 0.55), MITTEL, "right", GRUEN)
    s.text(a, "(q₁ᵀa₂) q₁", (1.3, 0.55), KLEIN, "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 5
def k2formen():
    s = Szene("ml/k2formen")
    w = s.welt()
    az, el, zf = math.radians(35), math.radians(30), 0.42
    flaechen = ((lambda x, y: x * x + 2 * y * y, BLAU, "sch", ("Schüssel", "bowl", "cuenco", "碗形", "cuvette", "çanak")),
                (lambda x, y: x * x, GRUEN, "rin", ("Rinne", "trough", "canal", "槽形", "gouttière", "oluk")),
                (lambda x, y: x * x - y * y, ROT, "sat", ("Sattel", "saddle", "silla", "鞍形", "selle", "eyer")))
    for k, (fz, farbe, key, worte) in enumerate(flaechen):
        mx, my = -2.15 + 2.15 * k, 1.05

        def P(x, y, z):
            return (mx + 0.82 * (x * math.cos(az) + y * math.sin(az)),
                    my + 0.82 * ((-x * math.sin(az) + y * math.cos(az)) * math.sin(el) + zf * z * math.cos(el)))

        werte = [i / 4 - 1 for i in range(9)]
        for c in werte:
            zug(s, w, [P(c, t, fz(c, t)) for t in [j / 20 - 1 for j in range(41)]], farbe=farbe, dicke=2)
            zug(s, w, [P(t, c, fz(t, c)) for t in [j / 20 - 1 for j in range(41)]], farbe=farbe, dicke=2)
        s.text(w, s.tr(key, *worte[:4], fr=worte[4], tr=worte[5]), (mx, 2.5), MITTEL, "center", farbe)
    # Höhenlinien darunter
    for k, farbe in enumerate((BLAU, GRUEN, ROT)):
        a = s.achsen((-1.1, 1.1), (-1.1, 1.1), breite=1.35, hoehe=1.35, mitte=(-2.15 + 2.15 * k, -1.35), kreuz=True, xticks="1",
                     yticks="1", xl="x₁", yl="x₂")
        if k == 0:
            for c in (0.25, 0.5, 1.0):
                zug(s, a, ellipse(0, 0, math.sqrt(c), math.sqrt(c / 2)), farbe=BLAU, dicke=3)
        elif k == 1:
            for c in (0.5, 0.7071, 1.0):
                for sg in (1, -1):
                    s.linie(a, (sg * c, -1.1), (sg * c, 1.1), farbe=GRUEN, dicke=3)
            s.linie(a, (0, -1.1), (0, 1.1), farbe=GRUEN, dicke=4, dash=DASH)
        else:
            ts = [j / 20 * 1.2 for j in range(-20, 21)]
            for c in (0.25, 0.5):
                r = math.sqrt(c)
                for sg in (1, -1):
                    zug(s, a, [(sg * r * math.cosh(t), r * math.sinh(t)) for t in ts], farbe=ROT, dicke=3)
                    zug(s, a, [(r * math.sinh(t), sg * r * math.cosh(t)) for t in ts], farbe=ROT_HELL, dicke=3)
            s.linie(a, (-1.1, -1.1), (1.1, 1.1), farbe=GRAU, dicke=2, dash=DASH)
            s.linie(a, (-1.1, 1.1), (1.1, -1.1), farbe=GRAU, dicke=2, dash=DASH)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k2eigen():
    s = Szene("ml/k2eigen")
    a = s.achsen((-1.5, 4.9), (-2.3, 4.2), breite=4.7, hoehe=4.75, kreuz=True, xticks="1;2;3;4", yticks="-2;-1;1;2;3;4", xl="x₁", yl="x₂")
    s.linie(a, (-1.3, -1.3), (4.0, 4.0), farbe=HELLGRAU, dicke=2)
    s.linie(a, (-1.0, 2.0), (1.15, -2.3), farbe=HELLGRAU, dicke=2)
    s.kreis(a, 0, 0, 1, farbe=GRAU, dicke=2)
    bild = [(4 * math.cos(t) + math.sin(t), 2 * math.cos(t) + 3 * math.sin(t)) for t in [2 * math.pi * k / 120 for k in range(121)]]
    zug(s, a, bild, farbe=HELLBLAU, dicke=4)
    s.linie(a, (0, 0), (3.536, 3.536), farbe=ROT_HELL, dicke=10)
    s.linie(a, (0, 0), (0.894, -1.789), farbe=GRUEN_HELL, dicke=10)
    s.pfeil((0, 0), (0.707, 0.707), on=a, farbe=ROT, dicke=5, spitze=0.15)
    s.pfeil((0, 0), (0.447, -0.894), on=a, farbe=GRUEN, dicke=5, spitze=0.15)
    s.pfeil((0, 0), (4, 2), on=a, farbe=GRAU, dicke=3, spitze=0.16, dash=DASH)
    s.pfeil((0, 0), (1, 0), on=a, farbe=SCHWARZ, dicke=5, spitze=0.15)
    s.text(a, "Av₁ = 5 v₁", (3.0, 3.85), MITTEL, "right", ROT)
    s.text(a, "Av₂ = 2 v₂", (1.25, -2.05), MITTEL, "left", GRUEN)
    s.text(a, "Ae₁", (4.25, 1.85), MITTEL, "left", GRAU)
    s.text(a, "e₁", (0.5, -0.32), MITTEL, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 7
def k2ellipse():
    s = Szene("ml/k2ellipse")
    a = s.achsen((-1.05, 1.1), (-1.15, 1.2), breite=3.8, hoehe=4.15, kreuz=True, xticks="0.5", yticks="0.5", xl="x₁", yl="x₂")
    s.linie(a, (-0.95, -0.475), (1.0, 0.5), farbe=HELLGRAU, dicke=2)
    s.linie(a, (-0.55, 1.1), (0.55, -1.1), farbe=HELLGRAU, dicke=2)
    phi = math.degrees(math.atan2(1, 2))
    zug(s, a, ellipse(0, 0, 1 / math.sqrt(6), 1, phi), farbe=BLAU, dicke=4)
    zug(s, a, ellipse(0, 0, 0.5 / math.sqrt(6), 0.5, phi), farbe=HELLBLAU, dicke=3)
    s.pfeil((0, 0), (0.3651, 0.1826), on=a, farbe=ROT, dicke=5, spitze=0.12)
    s.pfeil((0, 0), (0.4472, -0.8944), on=a, farbe=GRUEN, dicke=5, spitze=0.14)
    s.text(a, "q₁/√6", (0.42, 0.3), MITTEL, "left", ROT)
    s.text(a, "1 · q₂", (0.56, -0.97), MITTEL, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 9
def k2svd():
    s = Szene("ml/k2svd")
    w = s.welt()
    f, ox, oy = 0.47, -2.8, 2.15

    def T(x, y):
        return (ox + f * x, oy + f * y)

    def Tp(pts):
        return [T(x, y) for x, y in pts]

    u2 = (-0.4472, 0.8944)
    v1, v2 = (0.4472, 0.8944), (-0.8944, 0.4472)
    tafeln = (((0, 0), ellipse(0, 0, 1, 1), (1.35, 1.35), (v1, v2), ("v₁", "v₂"), (0, 1)),
              ((0, -5.5), ellipse(0, 0, 1, 1), (1.35, 1.35), ((1, 0), (0, 1)), ("e₁", "e₂"), (0.8944, 0.4472)),
              ((8, -5.5), ellipse(0, 0, 4, 1), (4.4, 1.35), ((4, 0), (0, 1)), ("4 e₁", "e₂"), (3.578, 0.4472)),
              ((8, 0), ellipse(0, 0, 4, 1, 26.565), (4.4, 2.2), ((3.578, 1.789), u2), ("4 u₁", "u₂"), (3, 2)))
    for (mx, my), kurve, (hx, hy), (p1, p2), (n1, n2), dot in tafeln:
        s.linie(w, T(mx - hx, my), T(mx + hx, my), farbe=HELLGRAU, dicke=2)
        s.linie(w, T(mx, my - hy), T(mx, my + hy), farbe=HELLGRAU, dicke=2)
        zug(s, w, Tp([(mx + x, my + y) for x, y in kurve]), farbe=BLAU, dicke=4)
        s.pfeil(T(mx, my), T(mx + p1[0], my + p1[1]), on=w, farbe=ROT, dicke=5, spitze=0.13)
        s.pfeil(T(mx, my), T(mx + p2[0], my + p2[1]), on=w, farbe=GRUEN, dicke=5, spitze=0.13)
        s.punkt(w, *T(mx + dot[0], my + dot[1]), farbe=SCHWARZ, r=0.06)
        q1 = T(mx + p1[0], my + p1[1])
        q2 = T(mx + p2[0], my + p2[1])
        s.text(w, n1, (q1[0] + 0.08, q1[1] - 0.22), KLEIN, "left", ROT)
        s.text(w, n2, (q2[0] - 0.08, q2[1] + 0.12), KLEIN, "right", GRUEN)
    s.text(w, "x", (T(0, 1)[0] - 0.12, T(0, 1)[1] + 0.12), KLEIN, "right")
    s.text(w, "Ax", (T(11, 2)[0] - 0.1, T(11, 2)[1] + 0.2), KLEIN, "center")
    s.pfeil(T(1.5, 1.9), T(4.6, 1.9), label="A", on=w, farbe=SCHWARZ, dicke=3, spitze=0.13, groesse=MITTEL)
    s.pfeil(T(0, -1.55), T(0, -4.0), on=w, farbe=SCHWARZ, dicke=3, spitze=0.13)
    s.pfeil(T(1.5, -5.5), T(3.4, -5.5), on=w, farbe=SCHWARZ, dicke=3, spitze=0.13)
    s.pfeil(T(12.7, -4.9), T(12.7, -0.6), on=w, farbe=SCHWARZ, dicke=3, spitze=0.13)
    dr = s.tr("drehen", "drehen", "rotate", "girar", "旋转", fr="tourner", tr="döndürme")
    st = s.tr("strecken", "strecken", "stretch", "estirar", "拉伸", fr="étirer", tr="germe")
    s.text(w, "Vᵀ: @{drehen}", T(0.25, -2.8), KLEIN, "left")
    s.text(w, "D: @{strecken}", T(2.45, -4.6), KLEIN, "center")
    s.text(w, "U: @{drehen}", T(12.45, -2.75), KLEIN, "right")
    del dr, st
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 10
def k2bild():
    s = Szene("ml/k2bild")
    z = 0.62
    grau = {"0": ("#111111", "#ffffff"), "1": ("#ffffff", SCHWARZ), "1/3": ("#545454", "#ffffff"), "2/3": ("#aaaaaa", SCHWARZ),
            "4/3": ("#ffffff", SCHWARZ)}
    bilder = ((("0", "1", "0"), ("1", "1", "1"), ("0", "1", "0")),
              (("1/3", "2/3", "1/3"), ("2/3", "4/3", "2/3"), ("1/3", "2/3", "1/3")),
              (("−1/3", "1/3", "−1/3"), ("1/3", "−1/3", "1/3"), ("−1/3", "1/3", "−1/3")))
    titel = ("C", s.tr("rang1", "C₁ (Rang 1)", "C₁ (rank 1)", "C₁ (rango 1)", "C₁（秩 1）", fr="C₁ (rang 1)", tr="C₁ (rank 1)"), "C − C₁")
    for b, (zeilen, t) in enumerate(zip(bilder, titel)):
        x0 = -2.55 + 2.55 * b - z
        for i, zeile in enumerate(zeilen):
            for j, wert in enumerate(zeile):
                if b < 2:
                    fuellung, schrift = grau[wert]
                else:
                    fuellung, schrift = ("#b4d0f1" if wert.startswith("−") else "#ecb4b4"), SCHWARZ
                s.box(wert, (x0 + j * z, 0.75 - i * z), breite=z, hoehe=z, groesse=KLEIN, farbe=schrift, fuellung=fuellung, dicke=1.5)
        s.text(None, t, (x0 + z, 0.75 - 2 * z - 0.6), MITTEL, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 12
def _gerade_im_rechteck(p, winkel, r):
    """Schnittstrecke der Geraden durch p mit Richtung winkel (Grad) mit dem Rechteck r = (x0, x1, y0, y1)."""
    dx, dy = math.cos(math.radians(winkel)), math.sin(math.radians(winkel))
    ts = []
    for wert, pv, dv in ((r[0], p[0], dx), (r[1], p[0], dx), (r[2], p[1], dy), (r[3], p[1], dy)):
        if abs(dv) > 1e-12:
            ts.append((wert - pv) / dv)
    pkte = []
    for t in ts:
        x, y = p[0] + t * dx, p[1] + t * dy
        if r[0] - 1e-9 <= x <= r[1] + 1e-9 and r[2] - 1e-9 <= y <= r[3] + 1e-9:
            pkte.append((t, (x, y)))
    pkte.sort()
    return [pkte[0][1], pkte[-1][1]]


def k2kondition():
    s = Szene("ml/k2kondition")
    w = s.welt()
    rr = (-0.6, 2.4, -0.4, 2.6)
    for ox, wb, neu, key, worte, weg in ((-3.4, 45, (0.8586, 1.1414), "senk", ("Geraden senkrecht", "lines perpendicular",
                                                                               "rectas perpendiculares", "两直线垂直",
                                                                               "droites perpendiculaires", "dik doğrular"), "0.2"),
                                         (0.4, -37, (-0.0162, 2.0162), "flach", ("Geraden unter 8°", "lines at 8°", "rectas a 8°",
                                                                                 "两直线夹角 8°", "droites à 8°",
                                                                                 "8° açılı doğrular"), "1.44")):
        def T(x, y, ox=ox):
            return (ox + (x - rr[0]), -1.6 + (y - rr[2]))

        zug(s, w, [T(rr[0], rr[2]), T(rr[1], rr[2]), T(rr[1], rr[3]), T(rr[0], rr[3]), T(rr[0], rr[2])], farbe=HELLGRAU, dicke=2)
        a1, a2 = _gerade_im_rechteck((1, 1), -45, rr)
        s.linie(w, T(*a1), T(*a2), farbe=BLAU, dicke=4)
        b1, b2 = _gerade_im_rechteck((1, 1), wb, rr)
        s.linie(w, T(*b1), T(*b2), farbe=ROT, dicke=4)
        c1, c2 = _gerade_im_rechteck(neu, wb, rr)
        s.linie(w, T(*c1), T(*c2), farbe=ROT, dicke=4, dash=DASH)
        s.punkt(w, *T(1, 1), farbe=SCHWARZ, r=0.07)
        s.punkt(w, *T(*neu), farbe=SCHWARZ, r=0.07)
        s.pfeil(T(1, 1), T(*neu), on=w, farbe=SCHWARZ, dicke=4, spitze=0.13)
        s.text(w, s.tr(key, *worte[:4], fr=worte[4], tr=worte[5]), T(0.9, 2.8), KLEIN, "center")
        wd = s.tr("wand" + key, "Schnittpunkt wandert um " + weg, "intersection moves by " + weg,
                  "el punto de corte se mueve " + weg, "交点移动 " + weg, fr="l’intersection se déplace de " + weg,
                  tr="kesişim noktası " + weg + " kayar")
        s.text(w, wd, T(0.9, -0.75), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Rechenbilder (Summen und Skalarprodukte)
def _formel(name, tex, hoehe):
    s = Szene("ml/" + name)
    s.formel(tex, hoehe=hoehe)
    s.speichern()


def _al(*zeilen):
    return r"\begin{aligned}" + r"\\".join(zeilen) + r"\end{aligned}"


QQ = r"\mathbf q_1=\begin{pmatrix}3/5\\4/5\end{pmatrix},\quad \mathbf q_2=\begin{pmatrix}-4/5\\3/5\end{pmatrix}"


def k2rorth():
    _formel("k2rorth", _al(r"&" + QQ,
                           r"\mathbf q_1^\top\mathbf q_2&=\tfrac35\cdot\left(-\tfrac45\right)+\tfrac45\cdot\tfrac35",
                           r"&=-\tfrac{12}{25}+\tfrac{12}{25}", r"&=0"), 1.75)


def k2rkoord():
    _formel("k2rkoord", _al(r"&" + QQ + r",\quad \mathbf x=\begin{pmatrix}3\\1\end{pmatrix}",
                            r"c_1=\mathbf q_1^\top\mathbf x&=\tfrac35\cdot3+\tfrac45\cdot1=\tfrac95+\tfrac45=\tfrac{13}5",
                            r"c_2=\mathbf q_2^\top\mathbf x&=\left(-\tfrac45\right)\cdot3+\tfrac35\cdot1=-\tfrac{12}5+\tfrac35=-\tfrac95",
                            r"c_1^2+c_2^2&=\tfrac{169}{25}+\tfrac{81}{25}=\tfrac{250}{25}=10"), 1.85)


def k2rproj():
    s = Szene("ml/k2rproj")
    s.skalarprodukt([1, 2], [4, 3], namen=("a", "y"), index="j", mitte=(0, 0.9))
    s.skalarprodukt([1, 2], [1, 2], namen=("a", "a"), index="j", mitte=(0, -1.15), vektoren=False)
    s.speichern()


def k2rnormal():
    _formel("k2rnormal", _al(r"&\mathbf a_1=\begin{pmatrix}1\\0\\1\end{pmatrix},\quad \mathbf a_2=\begin{pmatrix}0\\1\\1\end{pmatrix},"
                             r"\quad \mathbf y=\begin{pmatrix}1\\1\\1\end{pmatrix}",
                             r"(\mathbf H^\top\mathbf H)_{12}=\mathbf a_1^\top\mathbf a_2&=1\cdot0+0\cdot1+1\cdot1=0+0+1=1",
                             r"(\mathbf H^\top\mathbf y)_1=\mathbf a_1^\top\mathbf y&=1\cdot1+0\cdot1+1\cdot1=1+0+1=2"), 1.7)


def k2rausgleich():
    _formel("k2rausgleich", _al(r"(\mathbf A^\top\mathbf A)_{22}=\sum_{i=1}^3t_i^2&=t_1^2+t_2^2+t_3^2=0^2+1^2+2^2=0+1+4=5",
                                r"(\mathbf A^\top\mathbf y)_2=\sum_{i=1}^3t_i\,y_i&=t_1y_1+t_2y_2+t_3y_3=0\cdot1+1\cdot2+2\cdot4=0+2+8=10"), 1.2)


def k2rwohnungen():
    _formel("k2rwohnungen", _al(r"(\mathbf A^\top\mathbf A)_{12}=\mathbf a_1^\top\mathbf a_2&=60\cdot2+40\cdot1+90\cdot4+70\cdot3",
                                r"&=120+40+360+210=730",
                                r"(\mathbf A^\top\mathbf y)_1=\mathbf a_1^\top\mathbf y&=60\cdot200+40\cdot130+90\cdot290+70\cdot240",
                                r"&=12\,000+5\,200+26\,100+16\,800=60\,100"), 1.25)


def k2rgs():
    _formel("k2rgs", _al(r"\mathbf q_1^\top\mathbf a_2&=\tfrac1{\sqrt2}\,(1\cdot0+0\cdot1+1\cdot1)=\tfrac1{\sqrt2}\,(0+0+1)=\tfrac1{\sqrt2}",
                         r"\lVert\tilde{\mathbf q}_2\rVert^2&=\left(-\tfrac12\right)^2+1^2+\left(\tfrac12\right)^2=\tfrac14+1+\tfrac14=\tfrac32"), 0.9)


def k2rqr():
    _formel("k2rqr", _al(r"\mathbf q_1^\top\mathbf y&=\tfrac1{\sqrt2}\,(1\cdot1+0\cdot1+1\cdot1)=\tfrac1{\sqrt2}\,(1+0+1)=\tfrac2{\sqrt2}=\sqrt2",
                         r"\mathbf q_2^\top\mathbf y&=\tfrac1{\sqrt6}\,\left((-1)\cdot1+2\cdot1+1\cdot1\right)=\tfrac1{\sqrt6}\,(-1+2+1)=\tfrac2{\sqrt6}"), 0.86)


def k2rqf():
    _formel("k2rqf", _al(r"f(\mathbf x)=\sum_{i=1}^2\sum_{l=1}^2a_{il}\,x_ix_l&=a_{11}x_1x_1+a_{12}x_1x_2+a_{21}x_2x_1+a_{22}x_2x_2",
                         r"&=5\cdot1\cdot1+2\cdot1\cdot(-1)+2\cdot(-1)\cdot1+2\cdot(-1)\cdot(-1)",
                         r"&=5-2-2+2", r"&=3"), 1.4)


def k2rkomplex():
    _formel("k2rkomplex", _al(r"&\mathbf v^*=\begin{pmatrix}1\\\mathrm j\end{pmatrix},\quad \mathbf v=\begin{pmatrix}1\\-\mathrm j\end{pmatrix}",
                              r"(\mathbf v^*)^\top\mathbf v=\sum_{i=1}^2v_i^*\,v_i&=v_1^*v_1+v_2^*v_2=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2"), 1.2)


def k2rspur():
    _formel("k2rspur", r"\sum_{i=1}^2a_{ii}=a_{11}+a_{22}=4+3=7=5+2=\lambda_1+\lambda_2", 0.6)


def k2rsenkrecht():
    _formel("k2rsenkrecht", r"\begin{pmatrix}2\\1\end{pmatrix}^{\!\top}\begin{pmatrix}1\\-2\end{pmatrix}=2\cdot1+1\cdot(-2)=2-2=0", 0.6)


def k2rrayleigh():
    _formel("k2rrayleigh", _al(r"\mathbf x^\top\mathbf A\mathbf x&=5\cdot1\cdot1+2\cdot1\cdot1+2\cdot1\cdot1+2\cdot1\cdot1=5+2+2+2=11",
                               r"\mathbf x^\top\mathbf x&=1\cdot1+1\cdot1=1+1=2",
                               r"\frac{\mathbf x^\top\mathbf A\mathbf x}{\mathbf x^\top\mathbf x}&=\frac{11}2"), 1.2)


def k2rsvdidee():
    _formel("k2rsvdidee", _al(r"(\mathbf A\mathbf v_1)^\top(\mathbf A\mathbf v_2)&=\tfrac15\,\left(8\cdot(-1)+4\cdot2\right)=\tfrac15\,(-8+8)=0",
                              r"\lVert\mathbf A\mathbf v_1\rVert^2&=\tfrac15\,(8\cdot8+4\cdot4)=\tfrac15\,(64+16)=16",
                              r"\lVert\mathbf A\mathbf v_2\rVert^2&=\tfrac15\,\left((-1)\cdot(-1)+2\cdot2\right)=\tfrac15\,(1+4)=1"), 1.25)


def k2rfrobenius():
    _formel("k2rfrobenius", _al(r"\lVert\mathbf A\rVert_F^2=\sum_{i=1}^2\sum_{j=1}^2a_{ij}^2&=a_{11}^2+a_{12}^2+a_{21}^2+a_{22}^2=2^2+3^2+0^2+2^2",
                                r"&=4+9+0+4=17=4^2+1^2=d_1^2+d_2^2"), 1.1)


def k2rfehler():
    _formel("k2rfehler", _al(r"\lVert\mathbf A-\mathbf A_1\rVert_F^2&=\left(\tfrac25\right)^2+\left(-\tfrac15\right)^2+\left(-\tfrac45\right)^2"
                             r"+\left(\tfrac25\right)^2",
                             r"&=\tfrac4{25}+\tfrac1{25}+\tfrac{16}{25}+\tfrac4{25}=\tfrac{25}{25}=1"), 0.8)


def k2rmittel():
    _formel("k2rmittel", _al(r"\mathbf 1^\top\mathbf y=\sum_{i=1}^3y_i&=y_1+y_2+y_3=4+5+9=18",
                             r"x^+=\tfrac13\,\mathbf 1^\top\mathbf y&=\tfrac{18}3=6"), 0.95)


def k2rnormy():
    s = Szene("ml/k2rnormy")
    s.skalarprodukt([2, 2.01], [2, 2.01], namen=("y", "y"), index="j")
    s.speichern()


SZENEN = (k2onb, k2lot, k2ebene, k2ausgleich, k2gramschmidt, k2formen, k2eigen, k2ellipse, k2svd, k2bild, k2kondition,
          k2rorth, k2rkoord, k2rproj, k2rnormal, k2rausgleich, k2rwohnungen, k2rgs, k2rqr, k2rqf, k2rkomplex, k2rspur,
          k2rsenkrecht, k2rrayleigh, k2rsvdidee, k2rfrobenius, k2rfehler, k2rmittel, k2rnormy)

for f in SZENEN:
    f()
