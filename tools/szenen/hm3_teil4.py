"""Abbildungen zu Höhere Mathematik 3, Teil 4: Koordinatentransformationen."""
import sys
from math import cos, sin, pi, radians
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

AZ, EL = radians(115), radians(20)
HELLBLAU = "#8fb4e3"


def form(s, a, punkte, farbe=BLAU, deckung=0.2, rand=SCHWARZ, dicke=0, dash=""):
    pl = ";".join("%.4f,%.4f" % p for p in punkte)
    return s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": rand,
                            "fill_color": farbe, "fill_opacity": deckung, "stroke_width": dicke, "dash": dash}, a)


def proj(x, y, z, S=1.0, o=(0.0, 0.0)):
    """Parallelprojektion: x zeigt nach vorn links, y nach rechts, z nach oben."""
    rx, ry = cos(AZ), sin(AZ)
    ux, uy, uz = -sin(EL) * sin(AZ), sin(EL) * cos(AZ), cos(EL)
    return (o[0] + S * (x * rx + y * ry), o[1] + S * (x * ux + y * uy + z * uz))


def k4gitter():
    """Gitter in B, gekrümmtes Gitter in D, eine Zelle hervorgehoben."""
    s = Szene("hm3/k4gitter")
    a = s.welt()
    x0, y0, w = -3.55, -1.05, 2.1
    n = 5

    def bild(u, v):
        return (0.15 + 2.5 * u + 0.75 * v * v, -1.2 + 0.55 * u * u + 2.0 * v + 0.35 * u * v)

    for i in range(n + 1):
        s.linie(a, (x0 + w * i / n, y0), (x0 + w * i / n, y0 + w), farbe=HELLBLAU, dicke=2)
        s.linie(a, (x0, y0 + w * i / n), (x0 + w, y0 + w * i / n), farbe=HELLBLAU, dicke=2)
    i0, j0 = 3, 2
    c = w / n
    form(s, a, [(x0 + i0 * c, y0 + j0 * c), (x0 + (i0 + 1) * c, y0 + j0 * c), (x0 + (i0 + 1) * c, y0 + (j0 + 1) * c), (x0 + i0 * c, y0 + (j0 + 1) * c)], deckung=0.45, dicke=3, rand=BLAU)
    s.text(a, "B", (x0 + 0.02, y0 + w + 0.26), groesse=28)
    s.text(a, "Z", (x0 + (i0 + 0.5) * c, y0 + (j0 + 0.5) * c), groesse=24, ausrichtung="center")
    s.pfeil((-1.2, 0.0), (-0.3, 0.0), "Φ", groesse=26, spitze=0.2)
    for i in range(n + 1):
        u = i / n
        s.daten(a, [bild(u, k / 30) for k in range(31)], farbe=HELLBLAU, dicke=2)
        s.daten(a, [bild(k / 30, u) for k in range(31)], farbe=HELLBLAU, dicke=2)
    u0, v0, d = i0 / n, j0 / n, 1 / n
    rand = [bild(u0 + d * k / 8, v0) for k in range(9)] + [bild(u0 + d, v0 + d * k / 8) for k in range(1, 9)] + \
           [bild(u0 + d * (8 - k) / 8, v0 + d) for k in range(1, 9)] + [bild(u0, v0 + d * (8 - k) / 8) for k in range(1, 8)]
    form(s, a, rand, deckung=0.45, dicke=3, rand=BLAU)
    p = bild(u0, v0)
    ex = (2.5, 1.1 * u0 + 0.35 * v0)
    ey = (1.5 * v0, 2.0 + 0.35 * u0)
    s.pfeil(p, (p[0] + ex[0] * d, p[1] + ex[1] * d), "", farbe=ROT, dicke=3, spitze=0.13)
    s.pfeil(p, (p[0] + ey[0] * d, p[1] + ey[1] * d), "", farbe=GRUEN, dicke=3, spitze=0.13)
    s.text(a, "D", (3.15, 1.82), groesse=28)
    z = bild(u0 + d * 0.8, v0)
    s.pfeil((2.3, -1.0), (z[0], z[1] - 0.04), "", dicke=2, spitze=0.13)
    s.text(a, "Φ(Z)", (2.3, -1.25), groesse=24, ausrichtung="center", farbe=BLAU)
    s.speichern()


def k4rand():
    """Randkurve von B, Bild bei positiver und negativer Determinante."""
    s = Szene("hm3/k4rand")
    a = s.welt()
    fuell = [(cos(2 * pi * k / 60) * (1 + 0.2 * sin(6 * pi * k / 60)), sin(2 * pi * k / 60) * (1 + 0.2 * sin(6 * pi * k / 60))) for k in range(60)]
    for cx, sx, sy, sp, sch, far, name, titel, wort in (
            (-2.45, 0.8, 0.8, 1, 0.0, BLAU, "B", "γ", s.tr("li", "Inneres links", "interior on the left", "interior a la izquierda", "内部在左")),
            (0.0, 0.95, 0.68, 1, 0.3, GRUEN, "D", "det DΦ > 0", s.tr("li2", "Inneres links", "interior on the left", "interior a la izquierda", "内部在左")),
            (2.45, 0.95, 0.68, -1, 0.3, ROT, "D", "det DΦ < 0", s.tr("re", "Inneres rechts", "interior on the right", "interior a la derecha", "内部在右"))):
        pk = [(cx + sp * sx * p[0], sy * p[1] + sch * p[0]) for p in fuell]
        form(s, a, pk, farbe=far, deckung=0.1)
        s.daten(a, pk + [pk[0]], farbe=far, dicke=4)
        for k in (5, 24, 44):                       # Richtungsmarken als kleine Pfeile längs der Kurve
            s.pfeil(pk[k], pk[k + 3], "", farbe=far, dicke=4, spitze=0.2)
        o = (cx - sp * 0.05, -0.05)
        s.pfeil(o, (o[0] + sp * 0.5, o[1] + sch * 0.5), "", farbe=SCHWARZ, dicke=3, spitze=0.13)
        s.pfeil(o, (o[0], o[1] + 0.45), "", farbe=ORANGE, dicke=3, spitze=0.13)
        s.text(a, name, (cx - sp * 0.42, -0.42), groesse=26, ausrichtung="center")
        s.text(a, titel, (cx, 1.25), groesse=26, ausrichtung="center", farbe=far)
        s.text(a, wort, (cx, -1.25), groesse=24, ausrichtung="center", farbe=far)
    s.speichern()


def k4polar():
    """Rechteck der (r, phi) und Kreisscheibe mit Ringzelle und Ausnahmemenge."""
    s = Szene("hm3/k4polar")
    a = s.welt()
    x0, y0, bw, bh = -3.25, -1.3, 2.0, 2.6
    e = 0.14
    form(s, a, [(x0, y0), (x0 + e, y0), (x0 + e, y0 + bh), (x0, y0 + bh)], farbe=ORANGE, deckung=0.4)
    form(s, a, [(x0, y0), (x0 + bw, y0), (x0 + bw, y0 + e), (x0, y0 + e)], farbe=ORANGE, deckung=0.4)
    for i in range(5):
        s.linie(a, (x0 + bw * i / 4, y0), (x0 + bw * i / 4, y0 + bh), farbe=HELLBLAU, dicke=2)
    for j in range(7):
        s.linie(a, (x0, y0 + bh * j / 6), (x0 + bw, y0 + bh * j / 6), farbe=HELLBLAU, dicke=2)
    s.linie(a, (x0, y0), (x0 + bw, y0), dicke=3)
    s.linie(a, (x0, y0), (x0, y0 + bh), dicke=3)
    s.linie(a, (x0 + bw, y0), (x0 + bw, y0 + bh), dicke=3)
    s.linie(a, (x0, y0 + bh), (x0 + bw, y0 + bh), dicke=3)
    i0, j0 = 2, 1
    cx, cy = bw / 4, bh / 6
    form(s, a, [(x0 + i0 * cx, y0 + j0 * cy), (x0 + (i0 + 1) * cx, y0 + j0 * cy), (x0 + (i0 + 1) * cx, y0 + (j0 + 1) * cy), (x0 + i0 * cx, y0 + (j0 + 1) * cy)], deckung=0.5, dicke=3, rand=BLAU)
    s.text(a, "dr", (x0 + (i0 + 0.5) * cx, y0 + j0 * cy - 0.2), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, "dφ", (x0 + (i0 + 1) * cx + 0.06, y0 + (j0 + 0.45) * cy), groesse=22, farbe=GRUEN)
    s.text(a, "r", (x0 + bw / 2, y0 - 0.3), groesse=26, ausrichtung="center")
    s.text(a, "φ", (x0 - 0.12, y0 + bh / 2), groesse=26, ausrichtung="right")
    s.text(a, "R", (x0 + bw, y0 - 0.3), groesse=24, ausrichtung="center")
    s.text(a, "2π", (x0 - 0.1, y0 + bh - 0.05), groesse=24, ausrichtung="right")
    s.text(a, "ε", (x0 + e / 2, y0 - 0.3), groesse=24, ausrichtung="center", farbe=ORANGE)
    s.pfeil((-1.0, 0.0), (-0.2, 0.0), "Φ", groesse=26, spitze=0.2)
    o = (1.5, 0.0)
    Rr = 1.35
    pk = [(o[0] + Rr * cos(2 * pi * i / 90), o[1] + Rr * sin(2 * pi * i / 90)) for i in range(90)]
    form(s, a, pk, farbe=BLAU, deckung=0.06)
    for m in range(1, 5):
        s.kreis(a, o[0], o[1], Rr * m / 4, farbe=HELLBLAU, dicke=2)
    for j in range(6):
        w = 2 * pi * j / 6
        s.linie(a, o, (o[0] + Rr * cos(w), o[1] + Rr * sin(w)), farbe=HELLBLAU, dicke=2)
    s.kreis(a, o[0], o[1], Rr, farbe=SCHWARZ, dicke=3)
    r1, r2 = Rr * i0 / 4, Rr * (i0 + 1) / 4
    w1, w2 = 2 * pi * j0 / 6, 2 * pi * (j0 + 1) / 6
    zelle = [(o[0] + r1 * cos(w1 + (w2 - w1) * i / 12), o[1] + r1 * sin(w1 + (w2 - w1) * i / 12)) for i in range(13)] + \
            [(o[0] + r2 * cos(w2 - (w2 - w1) * i / 12), o[1] + r2 * sin(w2 - (w2 - w1) * i / 12)) for i in range(13)]
    form(s, a, zelle, deckung=0.5, dicke=3, rand=BLAU)
    es, keil = 0.12, 0.09                            # Ausnahmemenge: kleiner Kreis und schmaler Keil
    form(s, a, [o, (o[0] + Rr, o[1]), (o[0] + Rr * cos(keil), o[1] + Rr * sin(keil))], farbe=ORANGE, deckung=0.7)
    s.kreis(a, o[0], o[1], es, farbe=ORANGE, dicke=2, fuellung=ORANGE, deckung=0.7)
    s.text(a, "r dφ", (o[0], o[1] + (r1 + r2) / 2), groesse=22, ausrichtung="center")
    s.text(a, "dr", (o[0] + (r1 + r2) / 2 * cos(w1) + 0.17, o[1] + (r1 + r2) / 2 * sin(w1) - 0.06), groesse=22, farbe=ROT)
    s.pfeil((3.05, -1.0), (o[0] + Rr * 0.72, o[1] + 0.06), "", farbe=ORANGE, dicke=2, spitze=0.13)
    s.text(a, s.tr("fehlt", "fehlt", "missing", "falta", "缺失"), (3.05, -1.27), groesse=24, ausrichtung="center", farbe=ORANGE)
    s.speichern()


def k4kugel():
    """Kugelkoordinaten eines Punkts und die Kantenlängen der Zelle."""
    s = Szene("hm3/k4kugel")
    a = s.welt()
    Rr = 1.42
    o = (-1.85, -0.1)
    t0, p0 = radians(58), radians(78)
    b = (cos(EL) * sin(AZ), -cos(EL) * cos(AZ), sin(EL))

    def K(rr, th, ph):
        return (rr * sin(th) * cos(ph), rr * sin(th) * sin(ph), rr * cos(th))

    def lauf(pkte, farbe, dicke, dash_hinten="6,5", hinten="#b5b5b5"):
        """3D-Punkte auf der Kugel: vorn durchgezogen, hinten gestrichelt."""
        cur, st = [], None
        for q in pkte:
            v = q[0] * b[0] + q[1] * b[1] + q[2] * b[2] > 0
            p = proj(*q, 1, o)
            if st is None or v == st:
                cur.append(p)
            else:
                s.daten(a, cur + [p], farbe=farbe if st else hinten, dicke=dicke, dash="" if st else dash_hinten)
                cur = [p]
            st = v
        s.daten(a, cur, farbe=farbe if st else hinten, dicke=dicke, dash="" if st else dash_hinten)

    s.kreis(a, o[0], o[1], Rr, farbe=GRAU, dicke=2)
    lauf([K(Rr, pi / 2, 2 * pi * i / 90) for i in range(91)], GRAU, 2)
    lauf([K(Rr, t0, 2 * pi * i / 90) for i in range(91)], GRUEN, 3)
    lauf([K(Rr, pi * i / 60, p0) for i in range(61)], ORANGE, 3)
    for x, y, z, n, dx, dy in ((1.85, 0, 0, "x", -0.16, -0.14), (0, 1.95, 0, "y", 0.16, -0.05), (0, 0, 1.72, "z", 0.14, 0.02)):
        q = proj(x, y, z, 1, o)
        s.pfeil(o, q, "", dicke=2, spitze=0.14)
        s.text(a, n, (q[0] + dx, q[1] + dy), groesse=24)
    P = proj(*K(Rr, t0, p0), 1, o)
    M = proj(0, 0, Rr * cos(t0), 1, o)
    F = proj(*K(Rr * sin(t0), pi / 2, p0), 1, o)
    s.linie(a, o, P, farbe=ROT, dicke=4)
    s.linie(a, M, P, farbe=GRUEN, dicke=3, dash="8,5")
    s.linie(a, P, F, farbe=GRAU, dicke=2, dash="6,5")
    s.linie(a, o, F, farbe=GRAU, dicke=2, dash="6,5")
    s.punkt(a, P[0], P[1], r=0.07)
    s.daten(a, [proj(*K(0.55, t0 * i / 20, p0), 1, o) for i in range(21)], farbe=SCHWARZ, dicke=3)
    s.daten(a, [proj(*K(0.6, pi / 2, p0 * i / 20), 1, o) for i in range(21)], farbe=SCHWARZ, dicke=3)
    q = proj(*K(0.72, t0 * 0.5, p0), 1, o)
    s.text(a, "θ", (q[0] - 0.03, q[1] + 0.02), groesse=24, ausrichtung="center")
    q = proj(*K(0.8, pi / 2, p0 * 0.5), 1, o)
    s.text(a, "φ", (q[0] + 0.02, q[1] - 0.16), groesse=24, ausrichtung="center")
    s.text(a, "r", ((o[0] + P[0]) / 2 + 0.14, (o[1] + P[1]) / 2 - 0.13), groesse=26, farbe=ROT)
    s.text(a, "P", (P[0] + 0.12, P[1] + 0.12), groesse=24)
    s.text(a, "r sin θ", (P[0] + 0.1, P[1] - 0.05 + 0.42), groesse=24, ausrichtung="left", farbe=GRUEN)
    x0, y0 = 1.3, -0.95
    A_, B_, C_ = (1.4, 0.0), (0.0, 1.2), (0.55, 0.36)
    v = [(x0, y0), (x0 + A_[0], y0 + A_[1]), (x0 + A_[0] + B_[0], y0 + A_[1] + B_[1]), (x0 + B_[0], y0 + B_[1])]
    form(s, a, v, deckung=0.16, dicke=3, rand=SCHWARZ)
    form(s, a, [v[1], (v[1][0] + C_[0], v[1][1] + C_[1]), (v[2][0] + C_[0], v[2][1] + C_[1]), v[2]], deckung=0.3, dicke=3, rand=SCHWARZ)
    form(s, a, [v[3], v[2], (v[2][0] + C_[0], v[2][1] + C_[1]), (v[3][0] + C_[0], v[3][1] + C_[1])], deckung=0.08, dicke=3, rand=SCHWARZ)
    s.linie(a, v[0], v[1], farbe=GRUEN, dicke=5)
    s.linie(a, v[0], v[3], farbe=ORANGE, dicke=5)
    s.linie(a, v[1], (v[1][0] + C_[0], v[1][1] + C_[1]), farbe=ROT, dicke=5)
    s.text(a, "r sin θ dφ", (x0 + A_[0] / 2, y0 - 0.3), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(a, "r dθ", (x0 - 0.1, y0 + B_[1] / 2 - 0.08), groesse=24, ausrichtung="right", farbe=ORANGE)
    s.text(a, "dr", (v[1][0] + C_[0] / 2 + 0.17, v[1][1] + C_[1] / 2 - 0.2), groesse=24, farbe=ROT)
    s.speichern()


def k4singulaer():
    """r^(2-alpha) für mehrere alpha: Die Fläche unter der Kurve entscheidet."""
    s = Szene("hm3/k4singulaer")
    a = s.achsen((0, 1, 0.25), (0, 6, 2), breite=4.4, hoehe=1.95, mitte=(-0.3, 0), xl="r", yl="r^{2-α}", gitter=True)
    s.flaeche(a, "x^(-0.5)", 0.03, 1, farbe=BLAU, deckung=0.13)
    s.kurve(a, "1/x", x=(0.17, 1), farbe=ROT)
    s.kurve(a, "x^(-0.5)", x=(0.03, 1), farbe=BLAU)
    s.kurve(a, "1+0*x", x=(0, 1), farbe=GRUEN)
    s.kurve(a, "x", x=(0, 1), farbe=ORANGE)
    s.text(a, s.tr("drei", "α = 3: Fläche unendlich", "α = 3: infinite area", "α = 3: área infinita", "α = 3：面积无限"), (0.47, 4.2), groesse=24, farbe=ROT)
    s.text(a, s.tr("fuenf", "α = 5/2: Fläche endlich", "α = 5/2: finite area", "α = 5/2: área finita", "α = 5/2：面积有限"), (0.47, 2.7), groesse=24, farbe=BLAU)
    s.text(a, "α = 2", (1.03, 1.1), groesse=24, farbe=GRUEN)
    s.text(a, "α = 1", (1.03, 0.3), groesse=24, farbe=ORANGE)
    s.speichern()


def k4schale():
    """Geometrie der Kugelschale und Potential entlang des Abstands."""
    s = Szene("hm3/k4schale")
    a = s.welt()
    o = (-2.65, -0.45)
    k = 0.48
    r1, r2 = k, 2 * k
    s.kreis(a, o[0], o[1], r2, farbe=BLAU, dicke=3, fuellung=BLAU, deckung=0.22)
    s.kreis(a, o[0], o[1], r1, farbe=BLAU, dicke=3, fuellung="#ffffff", deckung=1.0)
    h = 3 * k
    X = (o[0], o[1] + h)
    tw = radians(50)
    ry = 1.6 * k
    Y = (o[0] + ry * sin(tw), o[1] + ry * cos(tw))
    s.linie(a, o, X, dicke=3)
    s.linie(a, o, Y, farbe=GRUEN, dicke=4)
    s.linie(a, Y, X, farbe=ROT, dicke=4)
    s.punkt(a, X[0], X[1], r=0.07)
    s.punkt(a, Y[0], Y[1], r=0.07)
    s.punkt(a, o[0], o[1], r=0.05)
    s.weg(a, "%g+0.3*sin(t)" % o[0], "%g+0.3*cos(t)" % o[1], 0, tw, farbe=SCHWARZ, dicke=2)
    s.text(a, "θ", (o[0] + 0.15, o[1] + 0.38), groesse=22, ausrichtung="center")
    s.text(a, "x", (X[0] + 0.14, X[1] + 0.08), groesse=24)
    s.text(a, "y", (Y[0] + 0.14, Y[1] - 0.02), groesse=24)
    s.text(a, "a", (o[0] - 0.14, o[1] + 1.15), groesse=24, ausrichtung="right")
    s.text(a, "r", ((o[0] + Y[0]) / 2 + 0.17, (o[1] + Y[1]) / 2 - 0.13), groesse=24, farbe=GRUEN)
    s.text(a, "|x − y|", ((X[0] + Y[0]) / 2 + 0.16, (X[1] + Y[1]) / 2 + 0.2), groesse=24, farbe=ROT)
    b = s.achsen((0, 6, 1), (0, 2, 0.5), breite=3.4, hoehe=1.95, mitte=(1.45, 0), xl="a", yl="u(a)", gitter=True)
    s.kurve(b, "1.5+0*x", x=(0, 1), farbe=BLAU)
    s.kurve(b, "7/(3*x)", x=(2, 6), farbe=BLAU)
    s.kurve(b, "7/(3*x)", x=(1.18, 2), farbe=GRAU, dash=DASH, dicke=3)
    s.punkt(b, 1, 1.5, r=0.06, farbe=BLAU)
    s.punkt(b, 2, 7 / 6, r=0.06, farbe=BLAU)
    s.text(b, s.tr("hohl", "Hohlraum", "cavity", "cavidad", "空腔"), (0.08, 1.7), groesse=22, farbe=BLAU)
    s.text(b, s.tr("aussen", "außen", "outside", "exterior", "外部"), (3.2, 1.0), groesse=22, farbe=BLAU)
    s.text(b, s.tr("pkt", "Punktquelle", "point source", "fuente puntual", "点源"), (1.95, 1.72), groesse=22, farbe=GRAU)
    s.speichern()


def k4basis():
    """Polarkoordinaten: Basis dreht sich mit; kartesisch: überall gleich."""
    s = Szene("hm3/k4basis")
    a = s.welt()
    o = (-1.95, -0.1)
    k = 0.6
    for m in (1, 2):
        s.kreis(a, o[0], o[1], k * m, farbe=HELLBLAU, dicke=2)
    for j in range(8):
        w = pi * j / 4
        s.linie(a, o, (o[0] + 2.2 * k * cos(w), o[1] + 2.2 * k * sin(w)), farbe=HELLBLAU, dicke=2)
    L = 0.5
    for rr, wd in ((1, 30), (2, 150)):
        w = radians(wd)
        p = (o[0] + k * rr * cos(w), o[1] + k * rr * sin(w))
        s.pfeil(p, (p[0] + L * cos(w), p[1] + L * sin(w)), "", farbe=ROT, dicke=4, spitze=0.14)
        s.pfeil(p, (p[0] - L * sin(w), p[1] + L * cos(w)), "", farbe=GRUEN, dicke=4, spitze=0.14)
        s.punkt(a, p[0], p[1], r=0.06)
    w = radians(30)
    p = (o[0] + k * cos(w), o[1] + k * sin(w))
    s.text(a, "ê_r", (p[0] + L * cos(w) + 0.05, p[1] + L * sin(w) - 0.15), groesse=24, farbe=ROT)
    s.text(a, "ê_φ", (p[0] - L * sin(w), p[1] + L * cos(w) + 0.14), groesse=24, farbe=GRUEN, ausrichtung="center")
    w = radians(150)
    p = (o[0] + 2 * k * cos(w), o[1] + 2 * k * sin(w))
    s.text(a, "ê_r", (p[0] + L * cos(w) - 0.02, p[1] + L * sin(w) + 0.15), groesse=24, farbe=ROT, ausrichtung="center")
    s.text(a, "ê_φ", (p[0] - L * sin(w) + 0.17, p[1] + L * cos(w) - 0.2), groesse=24, farbe=GRUEN, ausrichtung="center")
    s.text(a, s.tr("kr", "Polarkoordinaten", "polar coordinates", "coordenadas polares", "极坐标"), (o[0], 1.6), groesse=26, ausrichtung="center")
    x0, c = 0.95, 0.5
    for i in range(6):
        s.linie(a, (x0 + c * i, -1.35), (x0 + c * i, 1.15), farbe=HELLBLAU, dicke=2)
        s.linie(a, (x0, -1.35 + c * i), (x0 + 5 * c, -1.35 + c * i), farbe=HELLBLAU, dicke=2)
    for p in ((x0 + c, -0.85), (x0 + 3 * c, 0.15)):
        s.pfeil(p, (p[0] + L, p[1]), "", farbe=ROT, dicke=4, spitze=0.14)
        s.pfeil(p, (p[0], p[1] + L), "", farbe=GRUEN, dicke=4, spitze=0.14)
        s.punkt(a, p[0], p[1], r=0.06)
    s.text(a, "ê_x", (x0 + c + L + 0.05, -0.85 - 0.16), groesse=24, farbe=ROT)
    s.text(a, "ê_y", (x0 + c, -0.85 + L + 0.13), groesse=24, farbe=GRUEN, ausrichtung="center")
    s.text(a, s.tr("ka", "kartesisch", "Cartesian", "cartesianas", "直角坐标"), (x0 + 2.5 * c, 1.6), groesse=26, ausrichtung="center")
    s.speichern()


def k4drehung():
    """Links: das Feld ê_r läuft auseinander. Rechts: Differenz zweier Basisvektoren."""
    s = Szene("hm3/k4drehung")
    a = s.welt()
    o = (-2.3, 0.0)
    for rr in (0.42, 0.85):
        s.kreis(a, o[0], o[1], rr, farbe=HELLGRAU, dicke=2, dash=DASH)
    for k in range(12):
        w = pi * k / 6
        for rr in (0.42, 0.85):
            s.pfeil((o[0] + rr * cos(w), o[1] + rr * sin(w)), (o[0] + (rr + 0.36) * cos(w), o[1] + (rr + 0.36) * sin(w)), "", farbe=ROT, dicke=2, spitze=0.1)
    s.text(a, s.tr("gl", "ê_r: gleich lang, doch auseinander", "ê_r: equal length, yet spreading", "ê_r: igual longitud, pero se abren", "ê_r：等长却彼此分开"), (o[0] + 0.25, -1.5), groesse=22, ausrichtung="center", farbe=ROT)
    p = (0.75, -1.25)
    Lg = 2.0
    w0, dw = radians(26), radians(28)
    w1 = w0 + dw
    s.weg(a, "%g+%g*cos(t)" % (p[0], Lg), "%g+%g*sin(t)" % (p[1], Lg), w0, w1, farbe=HELLGRAU, dicke=2, dash=DASH)
    t1 = (p[0] + Lg * cos(w0), p[1] + Lg * sin(w0))
    t2 = (p[0] + Lg * cos(w1), p[1] + Lg * sin(w1))
    s.pfeil(p, t1, "", farbe=ROT, dicke=4, spitze=0.17)
    s.pfeil(p, t2, "", farbe=ROT, dicke=4, spitze=0.17)
    s.pfeil(t1, t2, "", farbe=GRUEN, dicke=4, spitze=0.15)
    s.text(a, "ê_r(φ)", (t1[0] - 0.75, t1[1] - 0.6), groesse=24, farbe=ROT)
    s.text(a, "ê_r(φ+Δφ)", (t2[0] - 1.05, t2[1] + 0.05), groesse=24, farbe=ROT, ausrichtung="center")
    m = ((t1[0] + t2[0]) / 2, (t1[1] + t2[1]) / 2)
    s.text(a, "≈ Δφ ê_φ", (m[0] + 0.14, m[1] + 0.1), groesse=24, farbe=GRUEN)
    s.punkt(a, p[0], p[1], r=0.05)
    s.speichern()


for f in (k4gitter, k4rand, k4polar, k4kugel, k4singulaer, k4schale, k4basis, k4drehung):
    f()
