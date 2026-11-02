"""Höhere Mathematik 1, Teil 9 (kap9_stufen.tex): Vektorprodukt und Basen.

Aufruf: python tools/szenen/hm1_teil9.py, danach python tools/szenen_ansehen.py out.png hm1/k9kreuz ... [--lang de]
Alle Zahlen stehen im Heft und in C:/Bücher/HöMa1/Arbeitshefte/rechnung_kap9.py. Rechenmodell: u = (2,1,0), v = (0,1,2), k = (1,0,2),
Orthonormalbasis f1, f2, f3, Vektor x = (5,1,-1), schiefe Basis a = (3,1), b = (1,2).

Die räumlichen Szenen sind echte 3D-Szenen (Kamera wie speichern3d in et1_teil10.py) ohne Achsen, also in Weltkoordinaten. Die Figuren haben kein
Koordinatenkreuz: k9kreuz, k9spat und k9proj sind starr so gedreht, dass die Grundfläche waagerecht liegt. Längen und Winkel bleiben dabei wahr.
"""
import json
import sys
from math import acos, atan2, cos, pi, sin, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24
HELLBLAU, HELLGRUEN, HELLORANGE, HELLROT, HELLGR = "#dceafa", "#d6efe0", "#fbe3d9", "#f8dcdc", "#eeeeee"
BRAUN = "#a84a22"


class Raum:
    """3D-Szene mit Kamera (theta, phi), Maßstab und Versatz auf dem Bildschirm. Punkte kommen als Modellkoordinaten."""

    def __init__(self, name, theta, phi, skala=1.0, versatz=(0, 0), margin=10):
        self.s = Szene(name, margin=margin)
        self.theta, self.phi, self.skala = theta, phi, skala
        ct, st, ce, se = cos(theta), sin(theta), cos(phi), sin(phi)
        cam = np.array([ce * ct, ce * st, se])
        rechts = np.cross(-cam, (0.0, 0.0, 1.0))
        rechts /= np.linalg.norm(rechts)
        oben = np.cross(rechts, -cam)
        self.R = np.array([rechts, oben, cam])
        self.versatz = np.array([versatz[0], versatz[1], 0.0])

    def welt(self, p):
        """Modellpunkt -> Weltkoordinaten (Maßstab, Versatz auf dem Bildschirm)."""
        return self.skala * np.asarray(p, dtype=float) + self.R.T @ self.versatz

    def bild(self, x, y, tiefe=0.0):
        """Punkt in der Bildebene (x, y in Szeneneinheiten) -> Weltkoordinaten: So lassen sich ebene Teilbilder einsetzen."""
        return self.R.T @ np.array([x, y, tiefe])

    def lin(self, p, q, farbe=SCHWARZ, d=3, dash="", roh=False):
        a, b = (p, q) if roh else (self.welt(p), self.welt(q))
        return self.s._add("Line", {"start": [float(c) for c in a], "end": [float(c) for c in b], "color": farbe, "stroke_width": d, "dash": dash})

    def vek(self, p, q, farbe=SCHWARZ, d=5, roh=False, spitze=0.2):
        """Pfeil: Schaft als Linie, Spitze als flaches Dreieck in Bildebene, damit sie aus jeder Richtung wie ein Pfeil aussieht."""
        a, b = (np.asarray(p, dtype=float), np.asarray(q, dtype=float)) if roh else (self.welt(p), self.welt(q))
        sa, sb = self.R @ a, self.R @ b
        dr = sb[:2] - sa[:2]
        L = float(np.hypot(*dr))
        e = dr / L
        n = np.array([-e[1], e[0]])
        sp = min(spitze, 0.45 * L)
        fuss2 = sb[:2] - sp * e
        tiefe = sb[2]
        fuss = self.R.T @ np.array([fuss2[0], fuss2[1], tiefe])
        l1 = self.R.T @ np.array([*(fuss2 + 0.42 * sp * n), tiefe])
        l2 = self.R.T @ np.array([*(fuss2 - 0.42 * sp * n), tiefe])
        self.lin(a, fuss, farbe, d, roh=True)
        return self.flaeche([b, l1, l2], farbe, 1.0, 1, roh=True)

    def flaeche(self, ecken, farbe=BLAU, deckung=0.25, rand=0, roh=False):
        pts = ecken if roh else [self.welt(e) for e in ecken]
        return self.s._add("Polygon", {"vertices": [[float(c) for c in e] for e in pts], "color": farbe, "fill_color": farbe, "fill_opacity": deckung,
                                       "stroke_width": rand})

    def txt(self, z, p, verschub=(0, 0), farbe=SCHWARZ, g=KL, ausr="center", roh=False):
        a = (np.asarray(p, dtype=float) if roh else self.welt(p)) + self.R.T @ np.array([verschub[0], verschub[1], 0.0])
        return self.s._add("Text", {"text": z, "position": [float(c) for c in a], "font_size": g, "align": ausr, "color": farbe})

    def speichern(self):
        m = self.s.model()
        m["model"]["camera"] = {"mode": "3d", "theta": self.theta, "phi": self.phi, "zoom": 1.0}
        p = SZENEN / (self.s.name + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")


def einheit(p):
    p = np.asarray(p, dtype=float)
    return p / np.linalg.norm(p)


def rechter_winkel(r, o, a, b, g=0.3, farbe=GRAU, roh=False):
    """Kleines Quadrat bei o zwischen den Richtungen a und b."""
    o, a, b = np.asarray(o, dtype=float), einheit(a), einheit(b)
    r.lin(o + g * a, o + g * a + g * b, farbe, 2.5, roh=roh)
    r.lin(o + g * b, o + g * a + g * b, farbe, 2.5, roh=roh)


# ------------------------------------------------------------------------------------------ Stufe 1
def k9kreuz():
    """Links im Raum, rechts der Blick von oben. Das Parallelogramm liegt waagerecht."""
    S = 0.56
    r = Raum("hm1/k9kreuz", -0.9, 0.46, skala=S, versatz=(-2.15, -1.2))
    s = r.s
    # Bilder von u, v, u x v nach der Drehung: u auf der x-Achse, u x v nach oben
    u, v, n = (sqrt(5), 0, 0), (1 / sqrt(5), sqrt(24 / 5), 0), (0, 0, sqrt(24))
    O = (0, 0, 0)
    uv = tuple(a + b for a, b in zip(u, v))
    r.flaeche([O, u, uv, v], BLAU, 0.2)
    r.lin(u, uv, BLAU, 2.5, DASH)
    r.lin(v, uv, GRUEN, 2.5, DASH)
    r.vek(O, u, BLAU)
    r.vek(O, v, GRUEN)
    r.vek(O, n, ROT)
    rechter_winkel(r, r.welt(O), u, n, 0.2, roh=True)
    rechter_winkel(r, r.welt(O), v, n, 0.2, roh=True)
    r.txt("u", u, (0.1, -0.2), BLAU)
    r.txt("v", v, (0.05, 0.2), GRUEN)
    r.txt("u \\times v", n, (0.55, -0.1), ROT)
    r.txt("A", (1.35, 1.1, 0), (0, 0), BLAU)

    # Blick von oben: ebenes Teilbild in der Bildebene, gleicher Maßstab
    x0, y0 = 0.55, -0.95

    def B(x, y):
        return r.bild(x0 + S * x, y0 + S * y, 3)

    r.txt(s.tr("oben", "Blick von oben", "View from above", "Vista desde arriba", "俯视"), B(1.35, 3.5), roh=True, farbe=GRAU)
    u2, v2 = (sqrt(5), 0), (1 / sqrt(5), sqrt(24 / 5))
    uv2 = (u2[0] + v2[0], u2[1] + v2[1])
    r.flaeche([B(0, 0), B(*u2), B(*uv2), B(*v2)], BLAU, 0.2, roh=True)
    r.lin(B(*u2), B(*uv2), BLAU, 2.5, DASH, roh=True)
    r.lin(B(*v2), B(*uv2), GRUEN, 2.5, DASH, roh=True)
    r.vek(B(0, 0), B(*u2), BLAU, roh=True)
    r.vek(B(0, 0), B(*v2), GRUEN, roh=True)
    fuss = (v2[0], 0)
    r.lin(B(*v2), B(*fuss), ORANGE, 4, roh=True)
    rechter_winkel(r, B(*fuss), r.bild(1, 0), r.bild(0, 1), 0.13, roh=True)
    alpha = acos(1 / 5)
    n_ = 16
    rb = 0.3
    for i in range(n_):
        a0, a1 = alpha * i / n_, alpha * (i + 1) / n_
        r.lin(B(rb * cos(a0), rb * sin(a0)), B(rb * cos(a1), rb * sin(a1)), GRAU, 2.5, roh=True)
    r.txt("\\alpha", B(0.2, 0.0), (0.0, -0.17), roh=True, farbe=GRAU, g=22)
    r.txt("u", B(u2[0], 0), (0.05, -0.2), roh=True, farbe=BLAU)
    r.txt("v", B(*v2), (-0.05, 0.2), roh=True, farbe=GRUEN)
    r.txt("h", B(v2[0], 1.1), (0.15, 0), roh=True, farbe=BRAUN)
    r.txt("A", B(1.6, 1.1), roh=True, farbe=BLAU)
    r.txt("h = 2.191", B(uv2[0], 1.45), (0.12, 0.0), roh=True, farbe=BRAUN, ausr="left", g=22)
    r.txt("A = 4.899", B(uv2[0], 0.95), (0.12, 0.0), roh=True, farbe=BLAU, ausr="left", g=22)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k9ebenen(name="hm1/k9ebenen", theta=1.2, phi=0.32):
    """H: 2x1 + x2 + 2x3 = 6 und x3 = 1 mit Schnittgerade G."""
    S = 0.62
    w = np.array([8 / 5, 4 / 5, 1.0])
    d = einheit((1, -2, 0))
    n1 = np.array([2, 1, 2]) / 3
    n2 = np.array([0, 0, 1.0])
    e2 = einheit((2, 1, 0))                       # in x3 = 1, senkrecht auf G
    e1 = einheit(np.cross(n1, d))                 # in H, senkrecht auf G
    if e1[2] < 0:
        e1 = -e1
    L, T = 2.7, 2.2
    r = Raum(name, theta, phi, skala=S, versatz=(0.2, 0))
    c = w

    def quad(richt, t0, t1, s0=-L, s1=L):
        return [c + s0 * d + t0 * richt, c + s1 * d + t0 * richt, c + s1 * d + t1 * richt, c + s0 * d + t1 * richt]

    r.flaeche(quad(e2, -T, 0), BLAU, 0.32, 1)
    r.flaeche(quad(e1, -T, 0), ORANGE, 0.42, 1)
    r.flaeche(quad(e2, 0, T), BLAU, 0.32, 1)
    r.flaeche(quad(e1, 0, T), ORANGE, 0.42, 1)
    r.lin(c - (L + 0.5) * d, c + (L + 0.5) * d, SCHWARZ, 4)
    p = c + 0.6 * d
    r.vek(p, p + 1.9 * n1, BRAUN)
    r.vek(p, p + 1.9 * n2, BLAU)
    r.vek(p, p + 1.9 * d, ROT, 6)
    rechter_winkel(r, r.welt(p), n1, d, 0.2, GRAU, roh=True)
    rechter_winkel(r, r.welt(p), n2, d, 0.2, GRAU, roh=True)
    r.txt("n^{(1)}", p + 1.9 * n1, (0.28, 0.06), BRAUN)
    r.txt("n^{(2)}", p + 1.9 * n2, (0.0, 0.2), BLAU)
    r.txt("v", p + 1.9 * d, (-0.02, 0.22), ROT)
    r.txt("G", c - (L + 0.5) * d, (0.2, -0.04), SCHWARZ)
    r.txt("H", c - (L - 0.5) * d + T * 0.72 * e1, (0, 0), BRAUN, g=26)
    r.txt("x_3 = 1", c - (L - 0.5) * d - T * 0.92 * e2, (0, 0.02), BLAU)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k9spat():
    """Grundfläche aus u, v waagerecht, dritte Kante k, Höhe längs u x v (der Pfeil ist verkürzt gezeichnet)."""
    S = 0.82
    r = Raum("hm1/k9spat", -0.75, 0.33, skala=S, versatz=(0, -1.0))
    eu = einheit((2, 1, 0))
    en = einheit((1, -2, 1))
    ev = np.cross(en, eu)

    def T(p):
        p = np.asarray(p, dtype=float)
        return np.array([p @ eu, p @ ev, p @ en])

    u, v, k = T((2, 1, 0)), T((0, 1, 2)), T((1, 0, 2))
    n = T((2, -4, 2))
    O = np.zeros(3)
    ecken = {(i, j, l): i * u + j * v + l * k for i in (0, 1) for j in (0, 1) for l in (0, 1)}
    hinten = min(ecken, key=lambda e: float(r.R[2] @ ecken[e]))     # die drei Kanten an dieser Ecke sind verdeckt
    # Flächen
    for a, b, c, dd in [(O, u, u + k, k), (O, v, v + k, k), (u, u + v, u + v + k, u + k), (v, u + v, u + v + k, v + k), (k, u + k, u + v + k, v + k)]:
        r.flaeche([a, b, c, dd], GRAU, 0.07)
    r.flaeche([O, u, u + v, v], BLAU, 0.28)
    for e in ecken:
        for achse in range(3):
            if e[achse] == 0:
                f = list(e)
                f[achse] = 1
                f = tuple(f)
                verdeckt = hinten in (e, f)
                r.lin(ecken[e], ecken[f], GRAU, 2.5, DASH if verdeckt else "")
    r.vek(O, u, BLAU)
    r.vek(O, v, GRUEN)
    r.vek(O, k, ORANGE)
    h = (6 / 24) * n
    r.vek(O, 0.56 * n, ROT)
    r.lin(O, h, BRAUN, 6)
    r.lin(k, h, SCHWARZ, 2.5, DOT)
    rechter_winkel(r, r.welt(h), -n, k - h, 0.13, GRAU, roh=True)
    r.txt("u", u, (0.17, -0.14), BLAU)
    r.txt("v", v, (0.24, 0.02), GRUEN)
    r.txt("k", k, (-0.02, 0.2), BRAUN)
    r.txt("u \\times v", 0.56 * n, (-0.5, -0.05), ROT)
    r.txt("h", h * 0.6, (-0.2, 0), BRAUN)
    r.txt("F = 4.899", (u + v) * 0.5, (0.2, -0.04), BLAU, g=22)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k9proj():
    """U = span{f1, f2} waagerecht: f1 und f2 sind die Achsen der Ebene, x = 3f1 - 3f2 + 3f3."""
    S = 0.6
    r = Raum("hm1/k9proj", -2.356, 0.5, skala=S, versatz=(-1.3, -0.75))
    O = np.zeros(3)
    f1, f2 = np.array([1.0, 0, 0]), np.array([0, 1.0, 0])
    p, q = np.array([3.0, -3.0, 3.0]), np.array([3.0, -3.0, 0.0])
    a0, a1, b0, b1 = -0.9, 3.9, -3.9, 0.9
    r.flaeche([(a0, b1, 0), (a1, b1, 0), (a1, b0, 0), (a0, b0, 0)], BLAU, 0.13, 1)
    for i in range(0, 4):
        r.lin((i, b0, 0), (i, b1, 0), "#c6d8ef", 1.5)
    for j in range(-3, 1):
        r.lin((a0, j, 0), (a1, j, 0), "#c6d8ef", 1.5)
    r.lin(f1, 3 * f1, GRAU, 2.5, DASH)
    r.lin(3 * f1, q, GRAU, 2.5, DASH)
    r.vek(O, q, BLAU, 5)
    r.vek(O, p, SCHWARZ, 5)
    r.vek(q, p, ROT, 5)
    r.vek(O, f1, GRUEN, 5)
    r.vek(O, f2, GRUEN, 5)
    rechter_winkel(r, r.welt(q), -q, (0, 0, 1), 0.16, GRAU, roh=True)
    for z_, f_ in ((p, SCHWARZ), (q, BLAU), (O, SCHWARZ)):
        r.s._add("Dot", {"center": [float(c) for c in r.welt(z_)], "radius": 0.06, "color": f_, "fill_color": f_, "fill_opacity": 1, "stroke_width": 0})
    r.txt("O", O, (-0.2, -0.08), SCHWARZ)
    r.txt("P", p, (0.2, 0.1), SCHWARZ)
    r.txt("Q", q, (0.0, -0.22), BLAU)
    r.txt("f_1", f1, (0.12, 0.16), GRUEN)
    r.txt("f_2", f2, (-0.05, 0.2), GRUEN)
    r.txt("p", 0.72 * p, (-0.16, 0.16), SCHWARZ)
    r.txt("q", 0.5 * q, (0.0, -0.18), BLAU)
    r.txt("p \\minus q", (p + q) / 2, (0.42, 0), ROT)
    r.txt("U", (-0.3, -3.3, 0), (0, 0), BLAU, g=26)
    r.txt("3 f_1", 1.9 * f1, (0.3, -0.12), GRAU, g=22)
    r.txt("\\minus 3 f_2", 3 * f1 - 1.5 * f2, (0.42, 0.08), GRAU, g=22)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def gitter_kreuz(s, x, y, m, mitte, titel):
    return s.achsen(x, y, breite=(x[1] - x[0]) * m, hoehe=(y[1] - y[0]) * m, mitte=mitte, kreuz=True, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False,
                    xl="", yl="", titel=titel, titel_mitte=True)


def schnitt_rechteck(p, d, x, y):
    """Gerade p + t d im Rechteck x[0..1] × y[0..1] (Liang-Barsky); None, wenn sie es nicht trifft."""
    t0, t1 = -1e9, 1e9
    for pi_, di, lo, hi in ((p[0], d[0], x[0], x[1]), (p[1], d[1], y[0], y[1])):
        if abs(di) < 1e-12:
            if pi_ < lo or pi_ > hi:
                return None
            continue
        a, b = sorted(((lo - pi_) / di, (hi - pi_) / di))
        t0, t1 = max(t0, a), min(t1, b)
    if t0 >= t1:
        return None
    return (p[0] + t0 * d[0], p[1] + t0 * d[1]), (p[0] + t1 * d[0], p[1] + t1 * d[1])


def k9basis():
    s = Szene("hm1/k9basis")
    x, y, m = (-1.0, 6.4), (-1.0, 3.2), 0.4
    st = s.tr("std", "Standardbasis", "Standard basis", "Base estándar", "标准基")
    bs = s.tr("schief", "Basis (a, b)", "Basis (a, b)", "Base (a, b)", "基 (a, b)")
    li = gitter_kreuz(s, x, y, m, (-1.83, 0), st)
    for i in (-1, 1, 2, 3, 4, 5, 6):
        s.linie(li, (i, y[0]), (i, y[1]), "#d9d9d9", 1.5)
    for j in (-1, 1, 2, 3):
        s.linie(li, (x[0], j), (x[1], j), "#d9d9d9", 1.5)
    s.pfeil((0, 0), (1, 0), "", farbe=BLAU, dicke=4, spitze=0.16, on=li)
    s.pfeil((0, 0), (0, 1), "", farbe=GRUEN, dicke=4, spitze=0.16, on=li)
    s.pfeil((0, 0), (5, 0), "", farbe=ROT, dicke=4, spitze=0.18, on=li)
    s.text(li, "e_1", (0.45, 0.5), farbe=BLAU, groesse=KL)
    s.text(li, "e_2", (-0.75, 1.0), farbe=GRUEN, groesse=KL)
    s.text(li, "(5, 0)", (4.35, 0.55), farbe=ROT, groesse=KL)

    re = gitter_kreuz(s, x, y, m, (1.83, 0), bs)
    a, b = (3, 1), (1, 2)
    for t in range(-5, 7):
        for p, dr in (((t * a[0], t * a[1]), b), ((t * b[0], t * b[1]), a)):
            st_ = schnitt_rechteck(p, dr, x, y)
            if st_:
                s.linie(re, st_[0], st_[1], "#cfdcec", 1.5)
    s.pfeil((0, 0), a, "", farbe=BLAU, dicke=4, spitze=0.16, on=re)
    s.pfeil((0, 0), b, "", farbe=GRUEN, dicke=4, spitze=0.16, on=re)
    s.pfeil((3, 1), (6, 2), "", farbe=GRAU, dicke=3, spitze=0.14, on=re, dash=DASH)
    s.pfeil((6, 2), (5, 0), "", farbe=GRAU, dicke=3, spitze=0.14, on=re, dash=DASH)
    s.pfeil((0, 0), (5, 0), "", farbe=ROT, dicke=4, spitze=0.18, on=re)
    s.text(re, "a", (1.9, 1.15), farbe=BLAU, groesse=KL)
    s.text(re, "b", (0.15, 2.3), farbe=GRUEN, groesse=KL)
    s.text(re, "2a", (4.5, 2.2), farbe=GRAU, groesse=KL)
    s.text(re, "\\minus b", (6.2, 0.75), farbe=GRAU, groesse=KL)
    s.text(re, "2a \\minus b", (3.3, -0.65), farbe=ROT, groesse=KL)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k9dim():
    s = Szene("hm1/k9dim")
    x, y, m = (-1.9, 2.9), (-0.35, 3.1), 0.66
    t1 = s.tr("drei", "Drei Vektoren", "Three vectors", "Tres vectores", "三个向量")
    t2 = s.tr("weg", "Anteil längs e_1 weggerechnet", "Part along e_1 removed", "Parte según e_1 eliminada", "消去沿 e_1 的分量")
    li = gitter_kreuz(s, x, y, m, (-1.75, 0), t1)
    a1, a2, a3 = (2, 1), (1, 2), (-1, 2)
    for v_, f in ((a1, BLAU), (a2, GRUEN), (a3, ORANGE)):
        s.pfeil((0, 0), v_, "", farbe=f, dicke=4, spitze=0.18, on=li)
    s.text(li, "a_1", (2.15, 0.75), farbe=BLAU, groesse=KL)
    s.text(li, "a_2", (1.0, 2.3), farbe=GRUEN, groesse=KL)
    s.text(li, "a_3", (-1.25, 2.3), farbe=BRAUN, groesse=KL)

    re = gitter_kreuz(s, x, y, m, (1.75, 0), t2)
    s.linie(re, (0, -0.35), (0, 3.1), ROT, 2.5, DASH)
    s.pfeil((0, 0), a1, "", farbe=BLAU, dicke=3, spitze=0.16, on=re)
    c2, c3 = (0, 1.5), (0, 2.5)
    s.pfeil((0, 0), a2, "", farbe="#9fcfb4", dicke=3, spitze=0.14, on=re)
    s.pfeil((0, 0), a3, "", farbe="#f2b89e", dicke=3, spitze=0.14, on=re)
    s.pfeil(a2, c2, "", farbe=GRAU, dicke=2.5, spitze=0.13, on=re, dash=DASH)
    s.pfeil(a3, c3, "", farbe=GRAU, dicke=2.5, spitze=0.13, on=re, dash=DASH)
    s.pfeil((0, 0), c3, "", farbe=BRAUN, dicke=5, spitze=0.2, on=re)
    s.pfeil((0, 0), c2, "", farbe=GRUEN, dicke=5, spitze=0.2, on=re)
    s.text(re, "c_2", (-0.5, 1.2), farbe=GRUEN, groesse=KL)
    s.text(re, "c_3", (-0.5, 2.75), farbe=BRAUN, groesse=KL)
    s.text(re, "a_1", (2.15, 0.75), farbe=BLAU, groesse=KL)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k9gs():
    s = Szene("hm1/k9gs")
    x, y, m = (-1.0, 3.3), (-0.45, 2.55), 0.5
    t = (s.tr("gs1", "1. Normieren", "1. Normalise", "1. Normalizar", "1. 归一化"),
         s.tr("gs2", "2. Projektion abziehen", "2. Subtract projection", "2. Restar la proyección", "2. 减去投影"),
         s.tr("gs3", "3. Normieren", "3. Normalise", "3. Normalizar", "3. 归一化"))
    pan = [gitter_kreuz(s, x, y, m, (mx, 0), tt) for mx, tt in zip((-2.25, 0, 2.25), t)]
    a, b = (3, 1), (1, 2)
    c1 = (3 / sqrt(10), 1 / sqrt(10))
    c2 = (-1 / sqrt(10), 3 / sqrt(10))
    pr = (1.5, 0.5)
    d2 = (-0.5, 1.5)

    p = pan[0]
    s.pfeil((0, 0), a, "", farbe=GRAU, dicke=3, spitze=0.14, on=p)
    s.pfeil((0, 0), b, "", farbe=GRAU, dicke=3, spitze=0.14, on=p)
    s.pfeil((0, 0), c1, "", farbe=ROT, dicke=5, spitze=0.17, on=p)
    s.text(p, "a", (3.0, 1.35), farbe=GRAU, groesse=KL)
    s.text(p, "b", (1.25, 2.2), farbe=GRAU, groesse=KL)
    s.text(p, "c_1", (0.95, -0.2), farbe=ROT, groesse=KL)

    p = pan[1]
    s.linie(p, (-1.0, -1.0 / 3), (3.3, 1.1), "#c9cfd6", 2)
    s.pfeil((0, 0), b, "", farbe=GRAU, dicke=3, spitze=0.14, on=p)
    s.pfeil((0, 0), pr, "", farbe=BLAU, dicke=5, spitze=0.17, on=p)
    s.pfeil(pr, b, "", farbe=ROT, dicke=2.5, spitze=0.13, on=p, dash=DASH)
    s.pfeil((0, 0), d2, "", farbe=ROT, dicke=5, spitze=0.17, on=p)
    g = 0.22
    e, n = c1, c2
    q1, q2 = (pr[0] + g * n[0], pr[1] + g * n[1]), (pr[0] + g * n[0] - g * e[0], pr[1] + g * n[1] - g * e[1])
    s.linie(p, q1, q2, GRAU, 2)
    s.linie(p, q2, (pr[0] - g * e[0], pr[1] - g * e[1]), GRAU, 2)
    s.text(p, "b", (1.3, 2.2), farbe=GRAU, groesse=KL)
    s.text(p, "Proj(b)", (2.15, -0.27), farbe=BLAU, groesse=22)
    s.text(p, "d_2", (-0.75, 1.75), farbe=ROT, groesse=KL)

    p = pan[2]
    s.weg(p, "cos(t)", "sin(t)", 0, 2 * pi, farbe="#c9cfd6", dicke=2)
    s.pfeil((0, 0), c1, "", farbe=BLAU, dicke=5, spitze=0.17, on=p)
    s.pfeil((0, 0), c2, "", farbe=ROT, dicke=5, spitze=0.17, on=p)
    s.linie(p, (g * e[0], g * e[1]), (g * e[0] + g * n[0], g * e[1] + g * n[1]), GRAU, 2)
    s.linie(p, (g * n[0], g * n[1]), (g * e[0] + g * n[0], g * e[1] + g * n[1]), GRAU, 2)
    s.text(p, "c_1", (1.35, 0.5), farbe=BLAU, groesse=KL)
    s.text(p, "c_2", (-0.55, 1.2), farbe=ROT, groesse=KL)
    s.text(p, "||c_i|| = 1", (1.9, 1.75), farbe=GRAU, groesse=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k9poly():
    s = Szene("hm1/k9poly")
    t2 = s.tr("onb", "Orthonormalbasis", "Orthonormal basis", "Base ortonormal", "标准正交基")
    li = s.achsen((-1.1, 1.1), (-1.15, 1.15), breite=2.4, hoehe=2.3, mitte=(-1.8, 0), kreuz=True, xticks="-1;1", yticks="-1", xl="x", yl="", titel="\\langle 1, x \\rangle = 0", titel_mitte=True)
    s.flaeche(li, "x", 0, 1, farbe=BLAU, deckung=0.3)
    s.flaeche(li, "x", -1, 0, farbe=ROT, deckung=0.3)
    s.kurve(li, "x", x=(-1, 1), farbe=BLAU, dicke=4)
    s.kurve(li, "1", x=(-1, 1), farbe=GRUEN, dicke=4)
    s.text(li, "+", (0.68, 0.28), farbe=BLAU, groesse=30)
    s.text(li, "\\minus", (-0.68, -0.32), farbe=ROT, groesse=30)
    s.text(li, "y = 1", (-0.72, 0.8), farbe=GRUEN, groesse=KL)
    s.text(li, "y = x", (0.38, 0.86), farbe=BLAU, groesse=KL)

    re = s.achsen((-1.1, 1.1), (-1.0, 1.75), breite=2.9, hoehe=2.3, mitte=(1.75, 0), kreuz=True, xticks="-1;1", yticks="-1;1", xl="x", yl="", titel=t2, titel_mitte=True)
    s.kurve(re, "1/sqrt(2)", x=(-1, 1), farbe=GRUEN, dicke=4)
    s.kurve(re, "sqrt(1.5)*x", x=(-1, 1), farbe=BLAU, dicke=4)
    s.kurve(re, "sqrt(45/8)*(x*x-1/3)", x=(-1, 1), farbe=ROT, dicke=4)
    s.text(re, "c_0", (-0.55, 0.92), farbe=GRUEN, groesse=KL)
    s.text(re, "c_1", (-0.82, -0.62), farbe=BLAU, groesse=KL)
    s.text(re, "c_2", (0.72, 1.45), farbe=ROT, groesse=KL)
    s.speichern()


if __name__ == "__main__":
    for f in (k9kreuz, k9ebenen, k9spat, k9proj, k9basis, k9dim, k9gs, k9poly):
        f()
    print("ok")
