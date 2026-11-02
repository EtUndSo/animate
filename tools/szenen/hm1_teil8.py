"""HM1 Teil 8 (kap8_stufen.tex): Vektoren und Skalarprodukt.

Rechenmodell: a = (3,1), b = (1,2); c = (2,1,0), d = (0,1,2), f = 2c - d = (4,1,-2); p = x²-1, q = x+1, r = p+q;
H: 2x1 + x2 + 2x3 = 6 mit n = (2,1,2)/3, beta = 2; P = (3,3,3), Q = (1,2,1); G: (1,0,-1) + alpha (2,0,1), S = (3,0,0).

Aufruf: python tools/szenen/hm1_teil8.py, danach python tools/szenen_ansehen.py out.png hm1/k8pfeile ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/HöMa1/Arbeitshefte/rechnung_kap8.py.
Alle Ebenen haben in beiden Richtungen denselben Maßstab, sonst stimmen die rechten Winkel im Bild nicht.
Die Editor-Schrift hat keinen Vektorpfeil. name() und formel() zeichnen ihn deshalb als kleinen Pfeil über den Buchstaben.
Raumbilder laufen über die echte 3D-Kamera (wie speichern3d in et1_teil10.py). Der Engine-Typ Vector zeigt von vorn eine große
Kegelspitze, darum entstehen Pfeilspitzen und Punkte hier als flache Polygone senkrecht zur Blickrichtung.
"""
import json
import sys
from math import atan2, cos, pi, sin, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24                        # Punktbeschriftung
A, B = (3, 1), (1, 2)
# Breiten der Schrift (Arial) in 1/1000 Geviert, für Formeln aus mehreren Stücken
ARIAL = {" ": 278, "+": 584, "−": 584, "=": 584, "(": 333, ")": 333, ",": 278, "{": 334, "}": 334, "‖": 260, "c": 500, "f": 278, "i": 222, "j": 222,
         "k": 500, "l": 222, "m": 833, "r": 333, "s": 500, "t": 278, "v": 500, "w": 722, "x": 500, "y": 500, "z": 500}


def breite(z, g=KL):
    """Textbreite in Szeneneinheiten (1 Einheit = 135 Szenenpixel)."""
    return sum(ARIAL.get(c, 556) for c in z) / 1000 * g / 135


def ebene(s, x, y, m, mitte=(0, 0), xt="", yt="", **kw):
    """Achsenkreuz mit m Szeneneinheiten je Zahlschritt, in beiden Richtungen gleich."""
    return s.achsen(x, y, breite=(x[1] - x[0]) * m, hoehe=(y[1] - y[0]) * m, mitte=mitte, kreuz=True, xticks=xt, yticks=yt,
                    xl="x_1", yl="x_2", **kw)


def pf(s, on, a, b, farbe=BLAU, dicke=4, dash="", spitze=0.2):
    return s.pfeil(a, b, "", farbe=farbe, spitze=spitze, dicke=dicke, on=on, dash=dash)


def deckel(s, on, m, x, y, farbe, br=0.11):
    """Vektorpfeil über einem Buchstaben, dessen Mitte bei (x, y) liegt."""
    s.pfeil((x - br / 2 / m, y + 0.125 / m), (x + br / 2 / m, y + 0.125 / m), "", farbe=farbe, dicke=1.5, spitze=0.055, on=on)


def name(s, on, m, x, y, z, farbe=SCHWARZ):
    """Ein Buchstabe mit Vektorpfeil."""
    formel(s, on, m, x, y, "[%s]" % z, farbe, "center")


def formel(s, on, m, x, y, text, farbe=SCHWARZ, ausr="left"):
    """Formel aus Stücken; in eckigen Klammern steht, was einen Vektorpfeil bekommt: "[a] + [b]". x ist der linke Rand, die Mitte oder der rechte Rand."""
    stuecke = [t for t in text.replace("[", "\0[").replace("]", "]\0").split("\0") if t]
    ges = sum(breite(t.strip("[]")) for t in stuecke)
    xx = x - {"left": 0, "center": ges / 2, "right": ges}[ausr] / m
    for t in stuecke:
        z = t.strip("[]")
        w = breite(z)
        kern = z.lstrip(" ")
        if kern:
            s.text(on, kern.replace("{", "\\{").replace("}", "\\}"), (xx + breite(z[:len(z) - len(kern)]) / m, y), KL, "left", farbe)
        if t.startswith("["):
            deckel(s, on, m, xx + w / 2 / m, y, farbe, w)
        xx += w / m


def rechter(s, on, p, e1, e2, g):
    """Haken für den rechten Winkel bei p längs der Einheitsrichtungen e1, e2, g in Datenschritten."""
    k1, k2 = (p[0] + g * e1[0], p[1] + g * e1[1]), (p[0] + g * e2[0], p[1] + g * e2[1])
    k3 = (p[0] + g * (e1[0] + e2[0]), p[1] + g * (e1[1] + e2[1]))
    s.linie(on, k1, k3, dicke=2)
    s.linie(on, k2, k3, dicke=2)


# ------------------------------------------------------------------------------------------ Raumbilder
class Raum:
    """Szene mit echter 3D-Kamera: Daten = (x1, x2, x3), m Szeneneinheiten je Datenschritt in allen Richtungen."""

    def __init__(self, nm, m, theta, phi, L=9):
        self.s = Szene(nm, margin=10)
        self.m, self.th, self.ph = m, theta, phi
        self.a = self.s._add("Axes", {"x_range": [-L, L, 1], "y_range": [-L, L, 1], "z_range": [-L, L, 1], "x_length": 2 * L * m, "y_length": 2 * L * m,
                                      "z_length": 2 * L * m, "origin": [0, 0, 0], "title": "", "x_label": "", "y_label": "", "number_size": 24,
                                      "label_size": 26, "axis_width": 3, "show_axes": False, "x_numbers": False, "y_numbers": False})
        ct, st, cp, sp = cos(theta), sin(theta), cos(phi), sin(phi)
        self.cam = (cp * ct, cp * st, sp)
        self.re = (-st, ct, 0)
        self.ob = (-sp * ct, -sp * st, cp)

    def _v(self, p, ri, ob):
        return tuple(p[i] + ri * self.re[i] + ob * self.ob[i] for i in range(3))

    def linie(self, p, q, farbe=SCHWARZ, d=3, dash=""):
        self.s._add("Line", {"start": list(p), "end": list(q), "color": farbe, "stroke_width": d, "dash": dash}, self.a)

    def flaeche(self, ecken, farbe=BLAU, deckung=0.28, d=1.5):
        self.s._add("Polygon", {"vertices": [list(e) for e in ecken], "color": farbe, "fill_color": farbe, "fill_opacity": deckung, "stroke_width": d}, self.a)

    def punkt(self, p, farbe=SCHWARZ, r=0.075):
        r /= self.m
        self.flaeche([self._v(p, r * cos(2 * pi * k / 14), r * sin(2 * pi * k / 14)) for k in range(14)], farbe, 1.0, 0)

    def pfeil(self, p, q, farbe=BLAU, d=4, dash=""):
        h, b = 0.2 / self.m, 0.075 / self.m
        di = [q[i] - p[i] for i in range(3)]
        n = sqrt(sum(x * x for x in di))
        e = [x / n for x in di]
        fuss = [q[i] - h * e[i] for i in range(3)]
        c = self.cam
        qu = (e[1] * c[2] - e[2] * c[1], e[2] * c[0] - e[0] * c[2], e[0] * c[1] - e[1] * c[0])
        nq = sqrt(sum(x * x for x in qu))
        qu = [x / nq for x in qu]
        self.linie(p, fuss, farbe, d, dash)
        self.flaeche([q, [fuss[i] + b * qu[i] for i in range(3)], [fuss[i] - b * qu[i] for i in range(3)]], farbe, 1.0, 0)

    def text(self, z, p, ausr="center", farbe=SCHWARZ, g=KL):
        self.s._add("Text", {"text": z, "position": list(p), "font_size": g, "align": ausr, "color": farbe}, self.a)

    def formel(self, text, p, farbe=SCHWARZ, ausr="center"):
        """Wie formel() oben, p ist der Bezugspunkt im Raum."""
        stuecke = [t for t in text.replace("[", "\0[").replace("]", "]\0").split("\0") if t]
        ges = sum(breite(t.strip("[]")) for t in stuecke)
        xx = -{"left": 0, "center": ges / 2, "right": ges}[ausr] / self.m
        for t in stuecke:
            z = t.strip("[]")
            w = breite(z) / self.m
            kern = z.lstrip(" ")
            if kern:
                self.text(kern, self._v(p, xx + breite(z[:len(z) - len(kern)]) / self.m, 0), "left", farbe)
            if t.startswith("["):
                o = 0.125 / self.m
                li, re_ = self._v(p, xx, o), self._v(p, xx + w, o)
                self.linie(li, re_, farbe, 1.5)
                sp_, zu = 0.05 / self.m, 0.022 / self.m
                self.flaeche([re_, self._v(re_, -sp_, zu), self._v(re_, -sp_, -zu)], farbe, 1.0, 0)
            xx += w

    def an(self, p, dx, dy):
        """Punkt, der im Bild um (dx, dy) Szeneneinheiten neben p liegt."""
        return self._v(p, dx / self.m, dy / self.m)

    def rechter(self, p, d1, d2, g=0.3, farbe=SCHWARZ):
        """Rechter-Winkel-Haken bei p, g in Datenschritten längs der Einheitsrichtungen d1, d2."""
        a = [p[i] + g * d1[i] for i in range(3)]
        b = [p[i] + g * d2[i] for i in range(3)]
        c = [p[i] + g * (d1[i] + d2[i]) for i in range(3)]
        self.linie(a, c, farbe, 2)
        self.linie(b, c, farbe, 2)

    def speichern(self):
        m = self.s.model()
        m["model"]["camera"] = {"mode": "3d", "theta": self.th, "phi": self.ph, "zoom": 1.0}
        p = SZENEN / (self.s.name + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")


# ------------------------------------------------------------------------------------------ Stufe 1
def k8pfeile():
    """Links Addition als Parallelogramm, rechts Streckung."""
    s = Szene("hm1/k8pfeile")
    m = 0.44
    a = ebene(s, (-0.4, 4.6), (-0.4, 3.5), m, mitte=(-2.05, 0), xt="1;2;3;4", yt="1;2;3")
    S = (4, 3)
    pf(s, a, A, S, GRAU, 3, DASH)
    pf(s, a, B, S, GRAU, 3, DASH)
    pf(s, a, (0, 0), S, ROT)
    pf(s, a, (0, 0), A, BLAU)
    pf(s, a, (0, 0), B, GRUEN)
    name(s, a, m, 1.75, 0.27, "a", BLAU)
    name(s, a, m, 0.25, 1.25, "b", GRUEN)
    formel(s, a, m, 2.6, 1.4, "[a] + [b]", ROT, "center")
    s.text(a, "(3, 1)", (3.1, 0.65), KL, "left", BLAU)
    s.text(a, "(1, 2)", (0.72, 2.42), KL, "center", GRUEN)
    s.text(a, "(4, 3)", (3.75, 3.3), KL, "center", ROT)
    m = 0.31
    b = ebene(s, (-1.7, 6.8), (-2.5, 2.7), m, mitte=(1.4, 0.0), xt="2;4;6", yt="1;2")
    pf(s, b, (0, 0), (6, 2), ROT)
    pf(s, b, (0, 0), A, BLAU, dicke=5)
    pf(s, b, (0, 0), B, GRUEN)
    pf(s, b, (0, 0), (-1, -2), ORANGE)
    formel(s, b, m, 4.2, 2.1, "2 [a]", ROT, "center")
    s.text(b, "(6, 2)", (6.1, 1.25), KL, "center", ROT)
    name(s, b, m, 1.9, 1.2, "a", BLAU)
    name(s, b, m, 0.3, 2.1, "b", GRUEN)
    formel(s, b, m, -0.45, -1.95, "− [b]", ORANGE, "left")
    s.speichern()


def k8gerade():
    """Links Gerade mit Parameterwerten, rechts Strecke."""
    s = Szene("hm1/k8gerade")
    m = 0.25
    a = ebene(s, (-3.9, 7.0), (-0.5, 5.2), m, mitte=(-2.05, 0), xt="-3;3;6", yt="2;4")
    s.linie(a, (-3.6, 0.8), (6.9, 4.3), farbe=BLAU, dicke=3)
    pf(s, a, (0, 0), (0, 2), GRAU, 3)
    pf(s, a, (0, 2), (3, 3), ROT, dicke=5)
    for t in (-1, 0, 1, 2):
        s.punkt(a, 3 * t, 2 + t, farbe=SCHWARZ, r=0.07)
    s.text(a, "t = −1", (-2.75, 2.0), KL, "center")
    s.text(a, "t = 0", (-1.3, 2.95), KL, "center")
    s.text(a, "t = 1", (2.4, 4.05), KL, "center")
    s.text(a, "t = 2", (5.5, 5.0), KL, "center")
    name(s, a, m, 0.6, 1.15, "p", GRAU)
    name(s, a, m, 1.95, 2.0, "v", ROT)
    m = 0.37
    b = ebene(s, (-0.5, 5.6), (-0.4, 3.7), m, mitte=(1.4, 0.0), xt="1;3;5", yt="1;2;3")
    pf(s, b, (0, 0), (1, 1), GRAU, 3)
    pf(s, b, (0, 0), (5, 3), GRAU, 3)
    s.linie(b, (1, 1), (5, 3), farbe=BLAU, dicke=5)
    for x, y in ((1, 1), (3, 2), (5, 3)):
        s.punkt(b, x, y, farbe=SCHWARZ, r=0.07)
    s.text(b, "P", (0.72, 1.35), KL, "center")
    s.text(b, "Q", (5.0, 3.4), KL, "center")
    s.text(b, "t = 0", (1.75, 0.62), KL, "center", GRAU)
    s.text(b, "t = 1/2", (2.7, 2.5), KL, "center", BLAU)
    s.text(b, "t = 1", (5.05, 2.3), KL, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k8polynome():
    """p, q, r = p + q; bei x = 2 stapeln sich die Werte."""
    s = Szene("hm1/k8polynome")
    a = s.achsen((-2.5, 3.5), (-1.3, 7), breite=4.6, hoehe=1.75, kreuz=True, xticks="-2;-1;1;2;3", yticks="2;4;6", xl="x", yl="y")
    s.kurve(a, "x^2-1", x=(-2.3, 2.55), farbe=BLAU)
    s.kurve(a, "x+1", x=(-2.3, 3.2), farbe=GRUEN)
    s.kurve(a, "x^2+x", x=(-2.3, 2.2), farbe=ROT)
    pf(s, a, (2, 0), (2, 3), BLAU, spitze=0.16)
    pf(s, a, (2, 3), (2, 6), GRUEN, spitze=0.16)
    for y in (3, 6):
        s.punkt(a, 2, y, r=0.06)
    s.punkt(a, -1, 0, r=0.07)
    s.text(a, "p(2) = 3", (2.12, 1.45), KL, "left", BLAU)
    s.text(a, "q(2) = 3", (2.5, 4.5), KL, "left", GRUEN)
    s.text(a, "r(2) = 6", (1.85, 6.5), KL, "right", ROT)
    s.text(a, "p", (2.68, 5.6), KL, "center", BLAU)
    s.text(a, "q", (3.3, 3.75), KL, "center", GRUEN)
    s.text(a, "r = p + q", (-1.75, 2.7), KL, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k8span():
    """Links Unterraum und verschobene Gerade, rechts Gitter der Kombinationen."""
    s = Szene("hm1/k8span")
    m = 0.24
    a = ebene(s, (-3.7, 6.9), (-1.7, 4.8), m, mitte=(-2.0, 0), xt="3;6", yt="2;4")
    s.linie(a, (-3.6, -1.2), (6.6, 2.2), farbe=BLAU, dicke=4)
    s.linie(a, (-3.6, 0.8), (6.6, 4.2), farbe=ORANGE, dicke=3, dash=DASH)
    pf(s, a, (0, 0), A, ROT, dicke=5)
    s.punkt(a, 0, 0, r=0.07)
    name(s, a, m, 1.75, 0.15, "a", ROT)
    formel(s, a, m, 6.8, 1.15, "span{[a]}", BLAU, "right")
    s.text(a, s.tr("kein", "kein Unterraum", "not a subspace", "no es subespacio", "不是子空间"), (6.6, 4.65), KL, "right", ORANGE)
    b = ebene(s, (-3.0, 7.3), (-2.7, 4.6), m, mitte=(1.3, 0), xt="", yt="", xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    x0, x1, y0, y1 = -2.9, 7.2, -2.6, 4.5

    def klipp(p, d):
        t0, t1 = -99.0, 99.0
        for pp, di, lo, hi in ((p[0], d[0], x0, x1), (p[1], d[1], y0, y1)):
            ta, tb = (lo - pp) / di, (hi - pp) / di
            t0, t1 = max(t0, min(ta, tb)), min(t1, max(ta, tb))
        return (p[0] + t0 * d[0], p[1] + t0 * d[1]), (p[0] + t1 * d[0], p[1] + t1 * d[1]), t1 > t0

    for k in range(-6, 8):
        for p, d in (((k * 1, k * 2), A), ((k * 3, k * 1), B)):
            q0, q1, ok = klipp(p, d)
            if ok:
                s.linie(b, q0, q1, farbe=HELLGRAU, dicke=1.5)
    pf(s, b, (0, 0), (6, 2), BLAU)
    pf(s, b, (6, 2), (5, 0), GRUEN)
    pf(s, b, (0, 0), A, BLAU, dicke=5)
    pf(s, b, (0, 0), B, GRUEN)
    s.punkt(b, 5, 0, farbe=ROT)
    name(s, b, m, 2.0, 0.27, "a", BLAU)
    name(s, b, m, 1.25, 2.55, "b", GRUEN)
    formel(s, b, m, 7.2, -1.05, "(5, 0) = 2 [a] − [b]", ROT, "right")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k8abhaengig():
    """c, d, f in einer Ebene durch O, (0,0,2) ragt heraus."""
    r = Raum("hm1/k8abhaengig", 0.37, -0.42, 0.27)
    u, v = (2, 1, 0), (0, 1, 2)
    ecke = lambda s_, t: tuple(s_ * u[i] + t * v[i] for i in range(3))
    r.flaeche([ecke(-0.6, -1.5), ecke(2.5, -1.5), ecke(2.5, 1.6), ecke(-0.6, 1.6)], BLAU, 0.12, 1.5)
    r.pfeil((0, 0, 0), (4, 1, -2), ROT)
    r.pfeil((0, 0, 0), (4, 2, 0), GRAU, 3, DASH)
    r.pfeil((4, 2, 0), (4, 1, -2), GRAU, 3, DASH)
    r.pfeil((0, 0, 0), u, BLAU)
    r.pfeil((0, 0, 0), v, GRUEN)
    r.linie((0, 0, 2), (-1 / 3, 2 / 3, 5 / 3), ORANGE, 2.5, DASH)
    r.pfeil((0, 0, 0), (0, 0, 2), ORANGE)
    r.punkt((0, 0, 0))
    r.text("O", r.an((0, 0, 0), -0.2, -0.05))
    r.formel("[c]", r.an((2, 1, 0), -0.1, -0.2), BLAU)
    r.formel("[d]", r.an((0, 1, 2), 0.2, -0.02), GRUEN)
    r.formel("[f] = 2 [c] − [d]", r.an((4, 1, -2), 0.34, 0.0), ROT, "left")
    r.formel("2 [c]", r.an((4, 2, 0), -0.02, 0.17), GRAU)
    r.text("(0, 0, 2)", r.an((0, 0, 2), -0.12, 0.25), "center", ORANGE)
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k8norm():
    """Quader 2 x 1 x 2 mit den Diagonalen, Pythagoras zweimal."""
    r = Raum("hm1/k8norm", 0.85, -0.62, 0.33)
    a, b, c = 2, 1, 2
    for p, q in (((0, 0, 0), (a, 0, 0)), ((0, 0, 0), (0, b, 0)), ((0, 0, 0), (0, 0, c)), ((a, 0, 0), (a, b, 0)), ((0, b, 0), (a, b, 0)),
                 ((a, 0, 0), (a, 0, c)), ((0, b, 0), (0, b, c)), ((0, 0, c), (a, 0, c)), ((0, 0, c), (0, b, c)), ((a, 0, c), (a, b, c)), ((0, b, c), (a, b, c))):
        r.linie(p, q, HELLGRAU, 2)
    r.linie((0, 0, 0), (2, 1, 0), ORANGE, 4)
    r.linie((2, 1, 0), (2, 1, 2), GRUEN, 4)
    r.pfeil((0, 0, 0), (2, 1, 2), BLAU)
    d = sqrt(5)
    r.rechter((2, 1, 0), (-2 / d, -1 / d, 0), (0, 0, 1), 0.18)
    r.punkt((0, 0, 0))
    r.text("O", (0, -0.16, -0.12))
    r.text("2", (1.0, -0.14, -0.14), "center", GRAU)
    r.text("1", (2.14, 0.5, -0.1), "center", GRAU)
    r.text("√5", (1.2, 0.46, -0.13), "center", ORANGE)
    r.text("2", (2.1, 1.1, 1.0), "left", GRUEN)
    r.formel("‖[x]‖ = 3", (0.85, 0.32, 1.2), BLAU, "right")
    r.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k8projektion():
    """Links Abstand Punkt-Gerade, rechts Orthogonalprojektion."""
    s = Szene("hm1/k8projektion")
    m = 0.26
    a = ebene(s, (-1.2, 7.3), (-0.4, 6.9), m, mitte=(-2.1, 0), xt="2;4;6", yt="4;6")
    s.linie(a, (-1.1, 2 - 1.1 / 3), (7.2, 2 + 7.2 / 3), farbe=BLAU, dicke=3)
    s.linie(a, (0, 2), (2, 6), farbe=GRAU, dicke=2.5, dash=DASH)
    pf(s, a, (0, 2), (3, 3), GRUEN)
    pf(s, a, (3, 3), (2, 6), ROT)
    e1, e2 = (3 / sqrt(10), 1 / sqrt(10)), (-1 / sqrt(10), 3 / sqrt(10))
    rechter(s, a, (3, 3), (-e1[0], -e1[1]), e2, 0.45)
    for x, y, z, dx, dy in ((0, 2, "P", -0.45, 0.55), (3, 3, "R", 0.45, -0.5), (2, 6, "Q", 0.0, 0.5)):
        s.punkt(a, x, y)
        s.text(a, z, (x + dx, y + dy), KL, "center")
    name(s, a, m, 1.65, 2.0, "v", GRUEN)
    name(s, a, m, 3.0, 4.75, "u", ROT)
    s.text(a, "√10", (2.95, 3.95), KL, "left", ROT)
    s.text(a, "√20", (1.85, 4.05), KL, "center", GRAU)
    s.text(a, "g", (7.0, 4.75), KL, "center", BLAU)

    m = 0.54
    b = ebene(s, (-0.4, 3.7), (-0.9, 2.7), m, mitte=(1.45, 0.0), xt="1;2;3", yt="1;2", xzahlen=False, yzahlen=False)
    P = (1.5, 0.5)
    pf(s, b, (0, 0), A, BLAU)
    pf(s, b, (0, 0), B, GRUEN)
    pf(s, b, (0, 0), P, ROT, dicke=6)
    pf(s, b, P, B, ORANGE)
    rechter(s, b, P, (-e1[0], -e1[1]), e2, 0.2)
    name(s, b, m, 3.05, 1.3, "a", BLAU)
    name(s, b, m, 0.8, 2.15, "b", GRUEN)
    s.text(b, "Proj_a(b) = (1.5; 0.5)", (1.75, -0.55), KL, "center", ROT)
    rest = s.tr("rest", "Rest", "remainder", "resto", "余量")
    s.text(b, rest, (1.42, 1.42), KL, "left", ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def bogen(s, on, r, w0, w1, farbe):
    s.weg(on, "%.5f*cos(t)" % r, "%.5f*sin(t)" % r, w0, w1, farbe=farbe, dicke=3)


def k8winkel():
    """Links Argumente und Differenz, rechts Parallelogramm mit Diagonalen."""
    s = Szene("hm1/k8winkel")
    m = 0.55
    a = ebene(s, (-0.4, 3.9), (-0.4, 2.7), m, mitte=(-2.0, 0), xt="1;2;3", yt="1;2")
    wa, wb = atan2(1, 3), atan2(2, 1)
    pf(s, a, (0, 0), A, BLAU)
    pf(s, a, (0, 0), B, GRUEN)
    bogen(s, a, 2.3, 0, wa, GRAU)
    bogen(s, a, 0.8, 0, wb, GRAU)
    bogen(s, a, 1.55, wa, wb, ROT)
    s.text(a, "45°", (1.5, 1.05), KL, "center", ROT)
    s.text(a, "18.43°", (2.45, 0.32), KL, "left", GRAU)
    s.text(a, "63.43°", (1.2, 2.2), KL, "left", GRAU)
    name(s, a, m, 3.1, 1.27, "a", BLAU)
    name(s, a, m, 0.72, 2.2, "b", GRUEN)

    m = 0.42
    b = ebene(s, (-0.4, 4.7), (-0.5, 3.6), m, mitte=(1.3, 0.0), xt="1;2;3;4", yt="1;2;3")
    S = (4, 3)
    pf(s, b, (0, 0), A, BLAU)
    pf(s, b, (0, 0), B, GRUEN)
    pf(s, b, B, S, BLAU, 3, DASH)
    pf(s, b, A, S, GRUEN, 3, DASH)
    pf(s, b, (0, 0), S, ROT)
    pf(s, b, B, A, ORANGE)
    name(s, b, m, 1.75, 0.27, "a", BLAU)
    name(s, b, m, 0.25, 1.25, "b", GRUEN)
    s.text(b, "25", (3.05, 1.8), KL, "center", ROT)
    s.text(b, "5", (2.05, 1.15), KL, "center", ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k8hyperebene():
    """H: 2x1 + x2 + 2x3 = 6 im ersten Oktanten mit Normaleneinheitsvektor, O, beta n, P, Q."""
    r = Raum("hm1/k8hyperebene", 0.56, -0.95, 0.26)
    n = (2 / 3, 1 / 3, 2 / 3)
    Q, P = (1, 2, 1), (3, 3, 3)
    bn = (4 / 3, 2 / 3, 4 / 3)
    T = (Q[0] + n[0], Q[1] + n[1], Q[2] + n[2])
    O = (0, 0, 0)
    for e in ((3, 0, 0), (0, 6, 0), (0, 0, 3)):
        r.linie(O, e, GRAU, 2, DASH)
    r.linie((3, 0, 0), (4.4, 0, 0), GRAU, 2)
    r.linie((0, 6, 0), (0, 7.2, 0), GRAU, 2)
    r.linie((0, 0, 3), (0, 0, 3.9), GRAU, 2)
    r.flaeche([(3, 0, 0), (0, 6, 0), (0, 0, 3)], BLAU, 0.2, 2)
    r.pfeil(O, bn, ORANGE)
    r.linie(T, P, GRAU, 2.5, DASH)
    r.pfeil(Q, T, ROT, 5)
    r.punkt(O)
    r.punkt(Q)
    r.punkt(P)
    r.punkt(bn, ORANGE)
    r.text("x_1", r.an((4.4, 0, 0), 0.18, -0.03), "center", GRAU)
    r.text("x_2", r.an((0, 7.2, 0), 0.2, 0.03), "center", GRAU)
    r.text("x_3", r.an((0, 0, 3.9), 0, 0.15), "center", GRAU)
    r.text("3", r.an((3, 0, 0), 0, -0.17), "center", GRAU)
    r.text("6", r.an((0, 6, 0), 0.02, 0.17), "center", GRAU)
    r.text("3", r.an((0, 0, 3), -0.13, 0.03), "center", GRAU)
    r.text("O", r.an(O, -0.17, -0.04))
    r.text("P = (3, 3, 3)", r.an(P, 0, 0.18), "center")
    r.text("Q = (1, 2, 1)", r.an(Q, 0.12, -0.17), "left")
    r.formel("[n]", r.an(T, -0.17, 0.05), ROT)
    r.formel("β [n]", r.an(bn, -0.24, 0.08), ORANGE)
    r.text("H", (0.2, 0.6, 2.5), "center", BLAU)
    r.speichern()


def k8geradewinkel():
    """H waagerecht, n senkrecht in S, G und Projektion G', Winkel gamma und delta."""
    r = Raum("hm1/k8geradewinkel", 0.74, -1.25, 0.38)
    gam = atan2(2, 1)
    d = (cos(gam), 0, sin(gam))
    r.flaeche([(-2.4, -1.5, 0), (2.4, -1.5, 0), (2.4, 1.5, 0), (-2.4, 1.5, 0)], BLAU, 0.2, 1.5)
    r.linie((-2.3, 0, 0), (2.3, 0, 0), ORANGE, 3)
    r.linie((-1.05 * d[0], 0, -1.05 * d[2]), (0, 0, 0), GRAU, 2.5, DASH)
    r.pfeil((0, 0, 0), (0, 0, 1.8), ROT)
    r.pfeil((0, 0, 0), (2.0 * d[0], 0, 2.0 * d[2]), BLAU)

    def bg(ra, w0, w1, f):
        n_ = 24
        pts = [(ra * cos(w0 + (w1 - w0) * k / n_), 0, ra * sin(w0 + (w1 - w0) * k / n_)) for k in range(n_ + 1)]
        for p, q in zip(pts, pts[1:]):
            r.linie(p, q, f, 3)

    bg(0.72, 0, gam, GRUEN)
    bg(1.15, gam, pi / 2, ROT)
    r.punkt((0, 0, 0))
    r.text("S", (-0.28, 0, -0.26))
    r.text("γ", (0.62, 0, 0.4), "center", GRUEN)
    r.text("δ", (0.3, 0, 1.38), "center", ROT)
    r.formel("[n]", (-0.26, 0, 1.6), ROT)
    r.text("G", (1.15, 0, 1.75), "center", BLAU)
    r.text("G′", (2.15, 0, 0.22), "center", ORANGE)
    r.text("H", (-2.05, 1.2, 0.0), "center", BLAU)
    r.speichern()


if __name__ == "__main__":
    k8pfeile()
    k8gerade()
    k8polynome()
    k8span()
    k8abhaengig()
    k8norm()
    k8projektion()
    k8winkel()
    k8hyperebene()
    k8geradewinkel()
