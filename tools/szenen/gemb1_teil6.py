"""GEMB 1, Teil 6 (kap6_stufen.tex): Kristallgitter.

Aufruf: python tools/szenen/gemb1_teil6.py, danach python tools/szenen_ansehen.py out.png gemb1/k6gitter ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap6.py.

Die räumlichen Szenen sind echte 3D-Szenen (Kamera wie Raum in hm1_teil9.py). Atome sind Scheiben, die zur Kamera zeigen: So bleiben sie aus
jeder Richtung rund, und die Tiefensortierung der Engine verdeckt sie richtig. Der Engine-Typ Sphere wäre im SVG ein Netz aus Hunderten Vierecken.
"""
import json
import sys
from math import cos, pi, sin, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24
HELLBLAU, HELLROT, HELLGRUEN, HELLORANGE = "#a9cdf3", "#f0a9a9", "#9fd8b8", "#f7c3ad"
TH, PH = 0.42, 0.30                          # Blick: x nach links vorn, y nach rechts, z nach oben


def viel(s, on, ecken, farbe=BLAU, deckung=0.3, rand=0, randfarbe=None):
    return s._add("Polygon", {"vertices": [[x, y, 0] for x, y in ecken], "color": randfarbe or farbe, "fill_color": farbe, "fill_opacity": deckung,
                              "stroke_width": rand}, on)


def kreissektor(c, r, w0, w1, n=24):
    """Ecken eines Kreissektors um c, Winkel in Bogenmaß."""
    return [c] + [(c[0] + r * cos(w0 + (w1 - w0) * i / n), c[1] + r * sin(w0 + (w1 - w0) * i / n)) for i in range(n + 1)]


class Raum:
    """3D-Szene mit Kamera (theta, phi). Punkte kommen als Modellkoordinaten, Teilbilder über feld()."""

    def __init__(self, name, theta=TH, phi=PH, skala=1.0, margin=10):
        self.s = Szene(name, margin=margin)
        self.theta, self.phi, self.skala = theta, phi, skala
        ct, st, ce, se = cos(theta), sin(theta), cos(phi), sin(phi)
        cam = np.array([ce * ct, ce * st, se])
        rechts = np.cross(-cam, (0.0, 0.0, 1.0))
        rechts /= np.linalg.norm(rechts)
        oben = np.cross(rechts, -cam)
        self.R = np.array([rechts, oben, cam])
        self.versatz = np.zeros(3)
        self.mitte = np.zeros(3)

    def feld(self, x, y, mitte=(0.5, 0.5, 0.5)):
        """Teilbild: Modellpunkt mitte liegt im Bild bei (x, y)."""
        self.versatz = np.array([x, y, 0.0])
        self.mitte = np.asarray(mitte, dtype=float)

    def welt(self, p):
        return self.skala * (np.asarray(p, dtype=float) - self.mitte) + self.R.T @ self.versatz

    def bild(self, p):
        """Modellpunkt -> (x, y, Tiefe) im Bild."""
        return self.R @ self.welt(p)

    def ebene(self, x, y, tiefe=0.0):
        """Punkt der Bildebene -> Weltkoordinaten."""
        return self.R.T @ np.array([x, y, tiefe])

    def lin(self, p, q, farbe=SCHWARZ, d=3, dash="", ab=0.0, bis=0.0):
        """Linie; ab, bis: Stücke an den Enden (Bildlänge), die frei bleiben, damit die Linie am Rand einer Atomscheibe endet."""
        a, b = self.welt(p), self.welt(q)
        L = float(np.linalg.norm((self.R @ (b - a))[:2])) or 1.0
        a2, b2 = a + (b - a) * ab / L, b - (b - a) * bis / L
        return self.s._add("Line", {"start": [float(c) for c in a2], "end": [float(c) for c in b2], "color": farbe, "stroke_width": d, "dash": dash})

    def vek(self, p, q, farbe=ROT, d=4, spitze=0.17, ab=0.0, vorn=0.0):
        """Pfeil: Schaft als Linie, Spitze als Dreieck in der Bildebene. vorn: Tiefenzuschlag, damit er vor den Atomen liegt."""
        a, b = self.R @ self.welt(p), self.R @ self.welt(q)
        dr = b[:2] - a[:2]
        L = float(np.hypot(*dr))
        e = dr / L
        n = np.array([-e[1], e[0]])
        a2 = a[:2] + ab * e
        fuss = b[:2] - spitze * e
        z0, z1 = a[2] + vorn, b[2] + vorn
        w = lambda u, z: self.R.T @ np.array([u[0], u[1], z])
        self.s._add("Line", {"start": [float(c) for c in w(a2, z0)], "end": [float(c) for c in w(fuss, z1)], "color": farbe, "stroke_width": d, "dash": ""})
        pts = [w(b[:2], z1), w(fuss + 0.42 * spitze * n, z1), w(fuss - 0.42 * spitze * n, z1)]
        return self.s._add("Polygon", {"vertices": [[float(c) for c in e2] for e2 in pts], "color": farbe, "fill_color": farbe, "fill_opacity": 1, "stroke_width": 1})

    def flaeche(self, ecken, farbe=BLAU, deckung=0.25, rand=0, randfarbe=None):
        pts = [self.welt(e) for e in ecken]
        return self.s._add("Polygon", {"vertices": [[float(c) for c in e] for e in pts], "color": randfarbe or farbe, "fill_color": farbe, "fill_opacity": deckung,
                                       "stroke_width": rand})

    def atom(self, p, r=0.1, farbe=BLAU, hell=HELLBLAU, n=26):
        """Kugel als Scheibe zur Kamera mit Lichtfleck."""
        c = self.bild(p)
        for rad, f, dz, rand, ox in ((r, farbe, 0.0, 1.5, 0.0), (0.42 * r, hell, 0.002, 0, 0.32 * r)):
            pts = [self.R.T @ np.array([c[0] - ox + rad * cos(2 * pi * i / n), c[1] + ox + rad * sin(2 * pi * i / n), c[2] + dz]) for i in range(n)]
            self.s._add("Polygon", {"vertices": [[float(v) for v in e] for e in pts], "color": SCHWARZ, "fill_color": f, "fill_opacity": 1, "stroke_width": rand})

    def txt(self, z, p=None, verschub=(0, 0), farbe=SCHWARZ, g=KL, ausr="center", bild=None):
        """Text an Modellpunkt p oder an der Bildstelle bild = (x, y); immer vor allem anderen."""
        if bild is not None:
            a = self.ebene(bild[0], bild[1], 40.0)
        else:
            c = self.bild(p)
            a = self.ebene(c[0] + verschub[0], c[1] + verschub[1], 40.0)
        return self.s._add("Text", {"text": z, "position": [float(c) for c in a], "font_size": g, "align": ausr, "color": farbe})

    def scheibe(self, x, y, r, farbe, deckung=1.0, rand=2, randfarbe=SCHWARZ, tiefe=0.0, dash=False, n=30):
        """Kreis in der Bildebene (für ebene Teilbilder einer 3D-Szene)."""
        pts = [self.ebene(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n), tiefe) for i in range(n)]
        return self.s._add("Polygon", {"vertices": [[float(v) for v in e] for e in pts], "color": randfarbe, "fill_color": farbe, "fill_opacity": deckung, "stroke_width": rand})

    def speichern(self):
        m = self.s.model()
        m["model"]["camera"] = {"mode": "3d", "theta": self.theta, "phi": self.phi, "zoom": 1.0}
        p = SZENEN / (self.s.name + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")


ECKEN = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
KANTEN = [(p, q) for p in ECKEN for q in ECKEN if p < q and sum(abs(u - v) for u, v in zip(p, q)) == 1]
FLAECHEN = [(.5, .5, 0), (.5, .5, 1), (.5, 0, .5), (.5, 1, .5), (0, .5, .5), (1, .5, .5)]


def wuerfel(r, frei=0.09, farbe=GRAU, d=2.5, dash=""):
    """Kanten der Zelle. frei: Kanten enden am Rand der Eckatome."""
    hinten = min(ECKEN, key=lambda e: float(r.R[2] @ np.array(e, dtype=float)))
    for p, q in KANTEN:
        r.lin(p, q, farbe, d, dash if dash else (DASH if hinten in (p, q) else ""), ab=frei, bis=frei)


# ------------------------------------------------------------------------------------------ Stufe 1
def k6gitter():
    """Punktgitter + Basis = Kristall."""
    s = Szene("gemb1/k6gitter")
    a1, a2 = (0.72, 0.0), (0.26, 0.62)
    d = (0.36, 0.22)

    def punkte(x0, y0):
        out = []
        for i in range(-4, 6):
            for j in range(-2, 4):
                x, y = i * a1[0] + j * a2[0], i * a1[1] + j * a2[1]
                if -0.02 <= x <= 2.2 and -0.02 <= y <= 1.9:
                    out.append((x0 + x, y0 + y))
        return out

    # Teilbild 1
    x0, y0 = -3.55, -1.0
    P = punkte(x0, y0)
    o = (x0 + a1[0] + a2[0], y0 + a2[1])
    viel(s, None, [o, (o[0] + a1[0], o[1]), (o[0] + a1[0] + a2[0], o[1] + a2[1]), (o[0] + a2[0], o[1] + a2[1])], GRAU, 0.22)
    for x, y in P:
        s.punkt(None, x, y, farbe=SCHWARZ, r=0.05)
    s.pfeil(o, (o[0] + a1[0], o[1]), "", farbe=ROT, dicke=4, spitze=0.16)
    s.pfeil(o, (o[0] + a2[0], o[1] + a2[1]), "", farbe=GRUEN, dicke=4, spitze=0.16)
    s.text(None, "a_1", (o[0] + 0.28, o[1] - 0.24), groesse=KL, farbe=ROT)
    s.text(None, "a_2", (o[0] - 0.22, o[1] + 0.2), groesse=KL, farbe=GRUEN, ausrichtung="center")
    s.text(None, s.tr("t1", "Punktgitter", "point lattice", "red de puntos", "点阵"), (x0 + 1.05, y0 + 2.25), groesse=26, ausrichtung="center")
    # Plus
    s.text(None, "+", (-1.12, -0.05), groesse=34, ausrichtung="center")
    # Teilbild 2
    c = (-0.82, -0.28)
    s.punkt(None, c[0], c[1], farbe=SCHWARZ, r=0.05)
    s.kreis(None, c[0], c[1], 0.17, farbe=SCHWARZ, dicke=2, fuellung=BLAU, deckung=1.0)
    s.kreis(None, c[0] + d[0] * 1.6, c[1] + d[1] * 1.6, 0.11, farbe=SCHWARZ, dicke=2, fuellung=ROT, deckung=1.0)
    s.pfeil(c, (c[0] + d[0] * 1.6, c[1] + d[1] * 1.6), "", farbe=SCHWARZ, dicke=3, spitze=0.13)
    s.text(None, "d", (c[0] + 0.22, c[1] + 0.32), groesse=KL)
    s.text(None, s.tr("t2", "Basis", "basis", "base", "基元"), (c[0] + 0.3, y0 + 2.25), groesse=26, ausrichtung="center")
    # Gleich
    s.text(None, "=", (0.42, -0.05), groesse=34, ausrichtung="center")
    # Teilbild 3
    x2 = 0.95
    for x, y in punkte(x2, y0):
        s.kreis(None, x, y, 0.13, farbe=SCHWARZ, dicke=2, fuellung=BLAU, deckung=1.0)
        if x + d[0] <= x2 + 2.4 and y + d[1] <= y0 + 2.0:
            s.kreis(None, x + d[0], y + d[1], 0.085, farbe=SCHWARZ, dicke=2, fuellung=ROT, deckung=1.0)
    s.text(None, s.tr("t3", "Kristall", "crystal", "cristal", "晶体"), (x2 + 1.1, y0 + 2.25), groesse=26, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def tafel(s, mx, my, a1, a2, titel, zelle=True, farbe=SCHWARZ, w=1.05, h=0.58, zusatz=None, start=None):
    """Ein Teilbild: Punkte im Fenster um (mx, my), eine primitive Zelle, Titel darüber."""
    pk = []
    for i in range(-9, 10):
        for j in range(-9, 10):
            x, y = i * a1[0] + j * a2[0], i * a1[1] + j * a2[1]
            if abs(x) <= w + 1e-6 and abs(y) <= h + 1e-6:
                pk.append((mx + x, my + y))
    if zelle:
        o = (mx + (start[0] if start else 0.0), my + (start[1] if start else 0.0))
        viel(s, None, [o, (o[0] + a1[0], o[1] + a1[1]), (o[0] + a1[0] + a2[0], o[1] + a1[1] + a2[1]), (o[0] + a2[0], o[1] + a2[1])], BLAU, 0.25)
    for x, y in pk:
        s.punkt(None, x, y, farbe=farbe, r=0.055)
    if zelle:
        s.pfeil(o, (o[0] + a1[0], o[1] + a1[1]), "", farbe=ROT, dicke=3, spitze=0.13)
        s.pfeil(o, (o[0] + a2[0], o[1] + a2[1]), "", farbe=ROT, dicke=3, spitze=0.13)
    s.text(None, titel, (mx, my + h + 0.3), groesse=24, ausrichtung="center")


def k6bravais():
    """Die fünf Gitter der Ebene und die Wabe."""
    s = Szene("gemb1/k6bravais")
    xs = (-2.4, 0.0, 2.4)
    y1, y2 = 1.0, -0.95
    tafel(s, xs[0], y1, (0.62, 0.0), (0.2, 0.46), s.tr("b1", "schiefwinklig", "oblique", "oblicua", "斜方"), start=(-0.1, -0.2))
    tafel(s, xs[1], y1, (0.66, 0.0), (0.0, 0.44), s.tr("b2", "rechteckig", "rectangular", "rectangular", "矩形"), start=(0.0, 0.0))
    tafel(s, xs[2], y1, (0.33, 0.33), (0.33, -0.33), s.tr("b3", "zentriert rechteckig", "centred rectangular", "rectangular centrada", "中心矩形"), start=(-0.33, 0.0))
    tafel(s, xs[0], y2, (0.48, 0.0), (0.0, 0.48), s.tr("b4", "quadratisch", "square", "cuadrada", "正方"), start=(0.0, 0.0))
    tafel(s, xs[1], y2, (0.5, 0.0), (0.25, 0.433), s.tr("b5", "hexagonal", "hexagonal", "hexagonal", "六方"), start=(-0.25, -0.433 + 0.433))
    # Wabe: hexagonales Gitter mit zwei Atomen je Zelle
    mx, my = xs[2], y2
    a1, a2 = (0.5196, 0.0), (0.2598, 0.45)
    d = (0.2598, 0.15)
    pa, pb = [], []
    for i in range(-7, 8):
        for j in range(-7, 8):
            x, y = i * a1[0] + j * a2[0], i * a1[1] + j * a2[1]
            pa.append((x, y))
            pb.append((x + d[0], y + d[1]))
    inside = lambda p: abs(p[0]) <= 1.05 and abs(p[1]) <= 0.58
    for u in pa:
        for dv in ((d[0], d[1]), (d[0] - a1[0], d[1] - a1[1]), (d[0] - a2[0], d[1] - a2[1])):
            v = (u[0] + dv[0], u[1] + dv[1])
            if inside(u) and inside(v):
                s.linie(None, (mx + u[0], my + u[1]), (mx + v[0], my + v[1]), farbe=GRAU, dicke=2)
    o = (mx - a1[0] * 0, my)
    viel(s, None, [o, (o[0] + a1[0], o[1]), (o[0] + a1[0] + a2[0], o[1] + a2[1]), (o[0] + a2[0], o[1] + a2[1])], BLAU, 0.25)
    for p in pa:
        if inside(p):
            s.punkt(None, mx + p[0], my + p[1], farbe=SCHWARZ, r=0.06)
    for p in pb:
        if inside(p):
            s.kreis(None, mx + p[0], my + p[1], 0.06, farbe=ROT, dicke=2, fuellung="#ffffff", deckung=1.0)
    s.pfeil(o, (o[0] + a1[0], o[1]), "", farbe=ROT, dicke=3, spitze=0.13)
    s.pfeil(o, (o[0] + a2[0], o[1] + a2[1]), "", farbe=ROT, dicke=3, spitze=0.13)
    s.text(None, s.tr("b6", "Wabe: kein Bravais-Gitter", "honeycomb: not Bravais", "panal: no es de Bravais", "蜂窝：非布拉维格子"), (mx, my + 0.88), groesse=24, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k6wigner():
    """Links die Konstruktion, rechts verschiedene primitive Zellen desselben Gitters."""
    s = Szene("gemb1/k6wigner")
    f = 2.75
    a, b = 0.40 * f, 0.60 * f
    # Gitter: Rechteck a x b mit Mittelpunkt
    def gitter(mx, my, wx, wy):
        out = []
        for i in range(-6, 7):
            for j in range(-6, 7):
                x, y = (i + j) * a / 2, (i - j) * b / 2
                if abs(x) <= wx + 1e-6 and abs(y) <= wy + 1e-6:
                    out.append((mx + x, my + y))
        return out

    def hexa(mx, my):
        y1, ym = 0.0833 * f, 0.2167 * f
        return [(mx + a / 2, my + y1), (mx, my + ym), (mx - a / 2, my + y1), (mx - a / 2, my - y1), (mx, my - ym), (mx + a / 2, my - y1)]

    # links
    mx, my = -2.05, 0.0
    viel(s, None, hexa(mx, my), BLAU, 0.3, 3, BLAU)
    for n in ((a / 2, b / 2), (-a / 2, b / 2), (a / 2, -b / 2), (-a / 2, -b / 2), (a, 0), (-a, 0)):
        s.linie(None, (mx, my), (mx + n[0], my + n[1]), farbe=GRUEN, dicke=3, dash=DASH)
        e = sqrt(n[0]**2 + n[1]**2)
        ux, uy = -n[1] / e, n[0] / e
        L = 0.85 if abs(n[1]) > 0 else 0.8
        c = (mx + n[0] / 2, my + n[1] / 2)
        s.linie(None, (c[0] - L * ux, c[1] - L * uy), (c[0] + L * ux, c[1] + L * uy), farbe=ROT, dicke=2, dash="6,5")
    for x, y in gitter(mx, my, 1.4, 1.1):
        s.punkt(None, x, y, r=0.075)
    s.kreis(None, mx, my, 0.1, farbe=ROT, dicke=3, fuellung="#ffffff", deckung=1.0)
    s.text(None, s.tr("w1", "Konstruktion", "construction", "construcción", "作图"), (mx, 1.72), groesse=26, ausrichtung="center")
    # rechts
    mx = 1.95
    P = gitter(mx, my, 1.7, 1.4)
    # Rhombus, Parallelogramm, Sechseck: alle gleiche Fläche
    o = (mx - a, my)
    viel(s, None, [o, (o[0] + a / 2, o[1] + b / 2), (o[0] + a, o[1]), (o[0] + a / 2, o[1] - b / 2)], ORANGE, 0.35, 3, ORANGE)
    o = (mx - a / 2, my - b / 2)
    viel(s, None, [o, (o[0] + a, o[1]), (o[0] + 3 * a / 2, o[1] + b / 2), (o[0] + a / 2, o[1] + b / 2)], GRUEN, 0.3, 3, GRUEN)
    viel(s, None, hexa(mx + a / 2, my + b / 2), BLAU, 0.3, 3, BLAU)
    for x, y in P:
        s.punkt(None, x, y, r=0.075)
    s.text(None, s.tr("w2", "gleiche Fläche, je 1 Punkt", "same area, 1 point each", "misma área, 1 punto cada una", "面积相同，各含 1 个点"), (mx, 1.72), groesse=26, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def polyeder(r, normalen, grenze, farbe, deckung=0.3):
    """Konvexes Polyeder aus {x: n·x <= g}: Ecken werden je Fläche gesammelt und im Kreis geordnet."""
    N = [np.asarray(n, dtype=float) for n in normalen]
    G = list(grenze)
    ecken = []
    for i in range(len(N)):
        for j in range(i + 1, len(N)):
            for k in range(j + 1, len(N)):
                A = np.array([N[i], N[j], N[k]])
                if abs(np.linalg.det(A)) < 1e-9:
                    continue
                x = np.linalg.solve(A, [G[i], G[j], G[k]])
                if all(n @ x <= g + 1e-9 for n, g in zip(N, G)) and not any(np.linalg.norm(x - e) < 1e-9 for e in ecken):
                    ecken.append(x)
    for n, g in zip(N, G):
        fl = [e for e in ecken if abs(n @ e - g) < 1e-9]
        c = sum(fl) / len(fl)
        u = fl[0] - c
        u /= np.linalg.norm(u)
        v = np.cross(n / np.linalg.norm(n), u)
        fl.sort(key=lambda e: np.arctan2((e - c) @ v, (e - c) @ u))
        r.flaeche([e + r.mitte for e in fl], farbe, deckung, 2, randfarbe=BLAU)
    return ecken


def k6kubisch():
    """Oben die Würfelzellen mit primitiven Vektoren, unten die Wigner-Seitz-Zellen."""
    S = 1.06
    r = Raum("gemb1/k6kubisch", skala=S)
    xs = (-2.5, 0.0, 2.5)
    y1, y2 = 0.98, -0.92
    R0, R1 = 0.095, 0.095
    # SC
    r.feld(xs[0], y1)
    wuerfel(r)
    for e in ECKEN:
        r.atom(e, R0)
    r.vek((0, 0, 0), (1, 0, 0), ROT, ab=R0, vorn=9)
    r.vek((0, 0, 0), (0, 1, 0), ROT, ab=R0, vorn=9)
    r.vek((0, 0, 0), (0, 0, 1), ROT, ab=R0, vorn=9)
    r.txt("SC", bild=(xs[0], y1 + 1.0), g=26)
    # BCC
    r.feld(xs[1], y1)
    wuerfel(r)
    for e in ECKEN:
        r.atom(e, R0)
    c = (.5, .5, .5)
    r.atom(c, R1, ORANGE, HELLORANGE)
    for z in ((1, 1, 0), (0, 1, 1), (1, 0, 1)):
        r.vek(c, z, ROT, ab=R1, vorn=9)
    r.txt("BCC", bild=(xs[1], y1 + 1.0), g=26)
    # FCC
    r.feld(xs[2], y1)
    wuerfel(r)
    for e in ECKEN:
        r.atom(e, R0)
    for f in FLAECHEN:
        r.atom(f, R1, ORANGE, HELLORANGE)
    for z in ((.5, .5, 0), (.5, 0, .5), (0, .5, .5)):
        r.vek((0, 0, 0), z, ROT, ab=R0, vorn=9)
    r.txt("FCC", bild=(xs[2], y1 + 1.0), g=26)

    # Wigner-Seitz-Zellen: Maßstab wie oben, Zelle um den Gitterpunkt in der Bildmitte
    h = 0.5
    r.feld(xs[0], y2, (0, 0, 0))
    wc = [(i, j, k) for i in (-h, h) for j in (-h, h) for k in (-h, h)]
    polyeder(r, [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], [.5] * 6, BLAU, 0.28)
    r.atom((0, 0, 0), R0)

    r.feld(xs[1], y2, (0, 0, 0))
    n1 = [(s1, 0, 0) for s1 in (1, -1)] + [(0, s1, 0) for s1 in (1, -1)] + [(0, 0, s1) for s1 in (1, -1)]
    n2 = [(a, b, c2) for a in (1, -1) for b in (1, -1) for c2 in (1, -1)]
    polyeder(r, n1 + n2, [.5] * 6 + [.75] * 8, BLAU, 0.28)
    r.atom((0, 0, 0), R0, ORANGE, HELLORANGE)

    r.feld(xs[2], y2, (0, 0, 0))
    n3 = [(a, b, 0) for a in (1, -1) for b in (1, -1)] + [(a, 0, c2) for a in (1, -1) for c2 in (1, -1)] + [(0, b, c2) for b in (1, -1) for c2 in (1, -1)]
    polyeder(r, n3, [.5] * 12, BLAU, 0.28)
    r.atom((0, 0, 0), R0, ORANGE, HELLORANGE)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k6packung():
    """Schnitte durch die Zellen: Wo die Kugeln einander berühren."""
    s = Szene("gemb1/k6packung")
    a = 1.62
    y0 = -0.95

    def rahmen(x0, w, h):
        s.linie(None, (x0, y0), (x0 + w, y0), dicke=3)
        s.linie(None, (x0, y0 + h), (x0 + w, y0 + h), dicke=3)
        s.linie(None, (x0, y0), (x0, y0 + h), dicke=3)
        s.linie(None, (x0 + w, y0), (x0 + w, y0 + h), dicke=3)

    def ecke(x, y, r, w0):
        viel(s, None, kreissektor((x, y), r, w0, w0 + pi / 2), BLAU, 0.55, 2, SCHWARZ)

    # SC: Würfelfläche
    x0 = -3.55
    r = a / 2
    for x, y, w in ((x0, y0, 0), (x0 + a, y0, pi / 2), (x0 + a, y0 + a, pi), (x0, y0 + a, 3 * pi / 2)):
        ecke(x, y, r, w)
    rahmen(x0, a, a)
    s.text(None, "SC", (x0 + a / 2, y0 + a + 0.42), groesse=26, ausrichtung="center")
    s.text(None, "a = 2r_at", (x0 + a / 2, y0 - 0.32), groesse=KL, ausrichtung="center", farbe=ROT)
    s.linie(None, (x0, y0), (x0 + a, y0), farbe=ROT, dicke=5)

    # BCC: Schnitt durch zwei Raumdiagonalen
    x0 = -1.5
    w = sqrt(2) * a
    r = sqrt(3) * a / 4
    for x, y, wi in ((x0, y0, 0), (x0 + w, y0, pi / 2), (x0 + w, y0 + a, pi), (x0, y0 + a, 3 * pi / 2)):
        ecke(x, y, r, wi)
    s.kreis(None, x0 + w / 2, y0 + a / 2, r, farbe=SCHWARZ, dicke=2, fuellung=ORANGE, deckung=0.55)
    rahmen(x0, w, a)
    s.linie(None, (x0, y0), (x0 + w, y0 + a), farbe=ROT, dicke=4)
    s.text(None, "BCC", (x0 + w / 2, y0 + a + 0.42), groesse=26, ausrichtung="center")
    s.text(None, "√3 a = 4r_at", (x0 + w / 2, y0 - 0.32), groesse=KL, ausrichtung="center", farbe=ROT)
    s.text(None, "a", (x0 - 0.2, y0 + a / 2), groesse=KL, ausrichtung="center")

    # FCC: Würfelfläche
    x0 = 1.55
    r = sqrt(2) * a / 4
    for x, y, wi in ((x0, y0, 0), (x0 + a, y0, pi / 2), (x0 + a, y0 + a, pi), (x0, y0 + a, 3 * pi / 2)):
        ecke(x, y, r, wi)
    s.kreis(None, x0 + a / 2, y0 + a / 2, r, farbe=SCHWARZ, dicke=2, fuellung=ORANGE, deckung=0.55)
    rahmen(x0, a, a)
    s.linie(None, (x0, y0), (x0 + a, y0 + a), farbe=ROT, dicke=4)
    s.text(None, "FCC", (x0 + a / 2, y0 + a + 0.42), groesse=26, ausrichtung="center")
    s.text(None, "√2 a = 4r_at", (x0 + a / 2, y0 - 0.32), groesse=KL, ausrichtung="center", farbe=ROT)
    s.text(None, "a", (x0 + a + 0.2, y0 + a / 2), groesse=KL, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def miller_zelle(r, x, y, name, ecken, n, achsen=False):
    r.feld(x, y)
    wuerfel(r, frei=0.0, farbe=GRAU, d=2.5)
    r.flaeche(ecken, BLAU, 0.42, 2, randfarbe=BLAU)
    c = np.mean(np.array(ecken, dtype=float), axis=0)
    e = np.asarray(n, dtype=float)
    e = e / np.linalg.norm(e)
    r.vek(c, c + 0.62 * e, ROT, d=4, vorn=9, spitze=0.15)
    r.txt(name, bild=(x, y + 0.94), g=26)
    if achsen:
        S = 0.72
        for u, nm in (((S + 0.5, 0, 0), "x"), ((0, S + 0.5, 0), "y"), ((0, 0, S + 0.5), "z")):
            pass


def k6miller():
    """Sechs Ebenen im Würfel, rot die Richtung mit denselben Indizes."""
    r = Raum("gemb1/k6miller", skala=1.02)
    xs = (-2.5, 0.0, 2.5)
    y1, y2 = 0.98, -0.98
    miller_zelle(r, xs[0], y1, "(100)", [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)], (1, 0, 0))
    miller_zelle(r, xs[1], y1, "(110)", [(1, 0, 0), (0, 1, 0), (0, 1, 1), (1, 0, 1)], (1, 1, 0))
    miller_zelle(r, xs[2], y1, "(111)", [(1, 0, 0), (0, 1, 0), (0, 0, 1)], (1, 1, 1))
    miller_zelle(r, xs[0], y2, "(200)", [(.5, 0, 0), (.5, 1, 0), (.5, 1, 1), (.5, 0, 1)], (1, 0, 0))
    miller_zelle(r, xs[1], y2, "(102)", [(1, 0, 0), (1, 1, 0), (0, 1, .5), (0, 0, .5)], (1, 0, 2))
    miller_zelle(r, xs[2], y2, "(210)", [(1, 0, 0), (.5, 1, 0), (.5, 1, 1), (1, 0, 1)], (2, 1, 0))
    # Achsen am ersten Würfel
    r.feld(xs[0], y1)
    o = np.array([0.0, 0.0, 0.0])
    for u, nm, v in (((1, 0, 0), "x", (-0.14, -0.14)), ((0, 1, 0), "y", (0.16, -0.02)), ((0, 0, 1), "z", (-0.15, 0.03))):
        r.txt(nm, u, v, g=KL, farbe=GRAU)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def fcc_punkte():
    return ECKEN + FLAECHEN


def k6struktur():
    """Oben die Stapelfolgen, unten Diamant und Kochsalz."""
    r = Raum("gemb1/k6struktur", skala=1.48)
    # oben links: eine Lage in der Draufsicht mit den beiden Muldenarten
    mx, my, q = -2.62, 1.42, 0.6
    for i in range(-3, 4):
        for j in range(-3, 4):
            x, y = (i + j / 2) * q, j * q * sqrt(3) / 2
            if x * x + y * y < (1.05 * q)**2 * 1.05:
                r.scheibe(mx + x, my + y, q / 2, BLAU, 0.25, 2)
    for x, y in ((q / 2, q * sqrt(3) / 6), (-q / 2, q * sqrt(3) / 6), (0, -q * sqrt(3) / 3)):
        r.txt("B", bild=(mx + x, my + y - 0.1), g=26, farbe=GRUEN)
    for x, y in ((0, q * sqrt(3) / 3), (q / 2, -q * sqrt(3) / 6), (-q / 2, -q * sqrt(3) / 6)):
        r.txt("C", bild=(mx + x, my + y - 0.1), g=26, farbe=ROT)
    r.txt(r.s.tr("s1", "Lage A mit Mulden", "layer A with hollows", "capa A con huecos", "A 层及其凹位"), bild=(mx, my + 1.02), g=24)

    # oben Mitte und rechts: Seitenansicht
    FA = {"A": (BLAU, 0.0), "B": (GRUEN, 1 / 3), "C": (ROT, 2 / 3)}

    def stapel(x0, y0, folge, titel):
        p, h = 0.42, 0.33
        for z, ch in enumerate(folge):
            f, o = FA[ch]
            for i in range(4):
                r.scheibe(x0 + (i + o) * p, y0 + z * h, 0.165, f, 1.0, 2)
            r.txt(ch, bild=(x0 - 0.3, y0 + z * h - 0.09), g=22, farbe=f)
        r.txt(titel, bild=(x0 + 0.76, y0 + len(folge) * h + 0.06), g=24)

    stapel(-0.72, 0.7, "ABABA", r.s.tr("s2", "hexagonal: ABAB", "hexagonal: ABAB", "hexagonal: ABAB", "六方：ABAB"))
    stapel(1.82, 0.7, "ABCAB", r.s.tr("s3", "kubisch: ABCABC", "cubic: ABCABC", "cúbica: ABCABC", "立方：ABCABC"))

    # unten links: Diamant
    S = 1.0
    x, y = -1.8, -1.32
    r.feld(x, y)
    wuerfel(r, frei=0.08, farbe=GRAU, d=2.5)
    innen = [(.25, .25, .25), (.75, .75, .25), (.75, .25, .75), (.25, .75, .75)]
    for p in innen:
        for dv in ((-.25, -.25, -.25), (.25, .25, -.25), (.25, -.25, .25), (-.25, .25, .25)):
            q2 = tuple(u + v for u, v in zip(p, dv))
            r.lin(p, q2, SCHWARZ, 4, ab=0.08, bis=0.08)
    for e in fcc_punkte():
        r.atom(e, 0.085, BLAU, HELLBLAU)
    for p in innen:
        r.atom(p, 0.085, GRUEN, HELLGRUEN)
    r.vek((0, 0, 0), (.25, .25, .25), ROT, d=5, ab=0.07, vorn=9, spitze=0.14)
    r.txt("d", (.12, .12, .12), (-0.2, 0.12), ROT, 26)
    r.txt(r.s.tr("s4", "Diamant", "diamond", "diamante", "金刚石"), bild=(x, y + 1.2), g=26)

    # unten rechts: Kochsalz
    x = 1.85
    r.feld(x, y)
    wuerfel(r, frei=0.0, farbe=GRAU, d=2.5)
    na = [(.5, 0, 0), (.5, 1, 0), (.5, 0, 1), (.5, 1, 1), (0, .5, 0), (1, .5, 0), (0, .5, 1), (1, .5, 1), (0, 0, .5), (1, 0, .5), (0, 1, .5), (1, 1, .5), (.5, .5, .5)]
    for e in fcc_punkte():
        r.atom(e, 0.125, BLAU, HELLBLAU)
    for e in na:
        r.atom(e, 0.07, ORANGE, HELLORANGE)
    r.txt(r.s.tr("s5", "Kochsalz", "rock salt", "sal gema", "岩盐"), bild=(x, y + 1.2), g=26)
    r.txt("Cl^−", bild=(x + 1.3, y + 0.45), g=24, farbe=BLAU)
    r.txt("Na^+", bild=(x + 1.3, y + 0.1), g=24, farbe=ORANGE)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k6luecken():
    """Packungsdichte der AB-Ionenkristalle über dem Radienverhältnis."""
    s = Szene("gemb1/k6luecken")
    xl = s.tr("rv", "Radienverhältnis r_+/r_−", "radius ratio r_+/r_−", "razón de radios r_+/r_−", "半径比 r_+/r_−")
    yl = s.tr("pd", "Packungsdichte P", "packing density P", "compacidad P", "堆积密度 P")
    a = s.achsen((0.2, 1.05, 0.2), (0.45, 0.85, 0.1), breite=6.0, hoehe=2.15, mitte=(0.1, 0.0), xl=xl, yl=yl)
    z0, o0, w0 = 0.2247, 0.4142, 0.7321
    s.band(a, z0, o0, 0.45, 0.85, farbe=BLAU, deckung=0.08)
    s.band(a, o0, w0, 0.45, 0.85, farbe=ROT, deckung=0.08)
    s.band(a, w0, 1.0, 0.45, 0.85, farbe=GRUEN, deckung=0.08)
    fn = "(1+x*x*x)/((1+x)*(1+x)*(1+x))"
    s.kurve(a, "1.36035*" + fn, x=(z0, o0), farbe=BLAU)
    s.kurve(a, "2.0944*" + fn, x=(o0, w0), farbe=ROT)
    s.kurve(a, "2.7207*" + fn, x=(w0, 1.0), farbe=GRUEN)
    for x0, y0, y1, f in ((o0, 0.515, 0.793, ROT), (w0, 0.561, 0.729, GRUEN)):
        s.linie(a, (x0, y0), (x0, y1), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (1.0, 0.45), (1.0, 0.85), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (1.0, 0.7405), (1.05, 0.7405), farbe=ORANGE, dicke=5)
    s.text(a, "0.225", (z0 + 0.055, 0.775), ausrichtung="center", groesse=KL, farbe=BLAU)
    s.text(a, "0.414", (o0 + 0.005, 0.815), ausrichtung="center", groesse=KL, farbe=ROT)
    s.text(a, "0.732", (w0 + 0.05, 0.755), ausrichtung="center", groesse=KL, farbe=GRUEN)
    n4 = s.tr("n4", "4 Nachbarn", "4 neighbours", "4 vecinos", "4 个近邻")
    n6 = s.tr("n6", "6 Nachbarn", "6 neighbours", "6 vecinos", "6 个近邻")
    n8 = s.tr("n8", "8 Nachbarn", "8 neighbours", "8 vecinos", "8 个近邻")
    s.text(a, "ZnS", (0.32, 0.545), ausrichtung="center", farbe=BLAU)
    s.text(a, n4, (0.32, 0.49), ausrichtung="center", farbe=BLAU, groesse=KL)
    s.text(a, "NaCl", (0.62, 0.765), ausrichtung="center", farbe=ROT)
    s.text(a, n6, (0.62, 0.71), ausrichtung="center", farbe=ROT, groesse=KL)
    s.text(a, "CsCl", (0.865, 0.585), ausrichtung="center", farbe=GRUEN)
    s.text(a, n8, (0.865, 0.53), ausrichtung="center", farbe=GRUEN, groesse=KL)
    s.text(a, "68 %", (0.945, 0.635), ausrichtung="center", farbe=GRUEN, groesse=KL)
    s.text(a, "74 %", (1.045, 0.775), ausrichtung="center", farbe=ORANGE, groesse=KL)
    s.speichern()


for f in (k6gitter, k6bravais, k6wigner, k6kubisch, k6packung, k6miller, k6struktur, k6luecken):
    f()
