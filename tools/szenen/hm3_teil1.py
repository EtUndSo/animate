"""Abbildungen zu Höhere Mathematik 3, Teil 1: Differentialrechnung für Vektorfelder."""
import sys
from math import cos, sin, pi, sqrt, radians
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403


def f_abb(x, y):
    """Rechenmodell f(x, y) = (x^2 - y^2, 2xy)."""
    return (x * x - y * y, 2 * x * y)


def polygon(s, a, pkte, farbe=BLAU, fuellung=BLAU, deckung=0.15, dicke=3, dash=""):
    s._add("Shape", {"points": ";".join("%.4f,%.4f" % p for p in pkte), "closed": True, "label": "", "material": "custom", "font_size": 24,
                     "color": farbe, "fill_color": fuellung, "fill_opacity": deckung, "stroke_width": dicke, "dash": dash}, a)


def k1jacobi():
    """Kleines Quadrat um (1, 1/2) und sein Bild; die Spalten der Matrix sind die Bilder der Kanten."""
    s = Szene("hm3/k1jacobi")
    a = s.welt()
    d = 0.3
    Sl, ol = 1.9, (-3.55, -1.25)
    Sr, or_ = 1.15, (0.5, -1.25)

    def L(x, y):
        return (ol[0] + Sl * x, ol[1] + Sl * y)

    def R(x, y):
        return (or_[0] + Sr * x, or_[1] + Sr * y)
    # Achsen als Pfeile
    s.pfeil(L(0, 0), L(1.65, 0), "", spitze=0.15, dicke=2)
    s.pfeil(L(0, 0), L(0, 1.15), "", spitze=0.15, dicke=2)
    s.text(a, "x", (L(1.65, 0)[0] - 0.05, L(1.65, 0)[1] - 0.3), groesse=24)
    s.text(a, "y", (L(0, 1.15)[0] - 0.25, L(0, 1.15)[1] - 0.1), groesse=24)
    s.pfeil(R(0, 0), R(2.2, 0), "", spitze=0.15, dicke=2)
    s.pfeil(R(0, 0), R(0, 2.2), "", spitze=0.15, dicke=2)
    s.text(a, "f₁", (R(2.2, 0)[0] - 0.1, R(2.2, 0)[1] - 0.32), groesse=24)
    s.text(a, "f₂", (R(0, 2.2)[0] - 0.33, R(0, 2.2)[1] - 0.12), groesse=24)
    # Quadrat links
    x0, y0 = 1.0, 0.5
    polygon(s, a, [L(x0 - d, y0 - d), L(x0 + d, y0 - d), L(x0 + d, y0 + d), L(x0 - d, y0 + d)])
    s.pfeil(L(x0, y0), L(x0 + d, y0), "", farbe=ROT, dicke=4, spitze=0.16)
    s.pfeil(L(x0, y0), L(x0, y0 + d), "", farbe=GRUEN, dicke=4, spitze=0.16)
    s.punkt(a, *L(x0, y0), r=0.07)
    s.text(a, "(1, 1/2)", (L(x0 - d, y0)[0] - 0.1, L(x0, y0)[1] - 0.1), groesse=24, ausrichtung="right")
    # Bild des Quadrats rechts
    n = 24
    rand = []
    for i in range(n):
        rand.append(R(*f_abb(x0 - d + 2 * d * i / n, y0 - d)))
    for i in range(n):
        rand.append(R(*f_abb(x0 + d, y0 - d + 2 * d * i / n)))
    for i in range(n):
        rand.append(R(*f_abb(x0 + d - 2 * d * i / n, y0 + d)))
    for i in range(n):
        rand.append(R(*f_abb(x0 - d, y0 + d - 2 * d * i / n)))
    polygon(s, a, rand)
    # Näherung: Parallelogramm aus den Spalten
    px, py = f_abb(x0, y0)
    u = (2 * d, 1 * d)
    v = (-1 * d, 2 * d)
    polygon(s, a, [R(px - u[0] - v[0], py - u[1] - v[1]), R(px + u[0] - v[0], py + u[1] - v[1]), R(px + u[0] + v[0], py + u[1] + v[1]),
                   R(px - u[0] + v[0], py - u[1] + v[1])], farbe=GRAU, deckung=0.0, dicke=3, dash=DASH)
    s.pfeil(R(px, py), R(px + u[0], py + u[1]), "", farbe=ROT, dicke=4, spitze=0.16)
    s.pfeil(R(px, py), R(px + v[0], py + v[1]), "", farbe=GRUEN, dicke=4, spitze=0.16)
    s.punkt(a, *R(px, py), r=0.07)
    s.pfeil((-0.72, 0.1), (-0.05, 0.1), "f", groesse=26, spitze=0.2)
    s.text(a, s.tr("sp1", "Spalte 1", "column 1", "columna 1", "第 1 列"), (R(px + u[0], py + u[1])[0] + 0.25, R(px + u[0], py + u[1])[1] - 0.2), groesse=24, farbe=ROT)
    s.text(a, s.tr("sp2", "Spalte 2", "column 2", "columna 2", "第 2 列"), (R(px + v[0], py + v[1])[0] + 0.1, R(px + v[0], py + v[1])[1] + 0.78), groesse=24, farbe=GRUEN, ausrichtung="center")
    s.text(a, s.tr("q", "Quadrat", "square", "cuadrado", "正方形"), (L(x0, y0)[0], L(x0, y0)[1] + 0.9), groesse=24, ausrichtung="center", farbe=BLAU)
    s.speichern()


def k1schraeg():
    """f = xy/(x^2+y^2): auf Strahlen konstant. Links die Werte, rechts die Schnitte längs Achse und Diagonale."""
    s = Szene("hm3/k1schraeg")
    a = s.welt()
    c = (-1.95, -0.05)
    R_ = 1.4
    for k in range(16):
        w = k * pi / 8
        wert = 0.5 * sin(2 * w)
        p = (c[0] + R_ * cos(w), c[1] + R_ * sin(w))
        if k % 4 == 0:
            s.linie(a, c, p, farbe=ROT, dicke=4)
        elif k % 4 == 2:
            s.linie(a, c, p, farbe=BLAU, dicke=4)
        else:
            s.linie(a, c, p, farbe=HELLGRAU, dicke=2)
        if k % 2 == 0:
            q = (c[0] + (R_ + 0.3) * cos(w), c[1] + (R_ + 0.24) * sin(w) - 0.1)
            txt = "0" if k % 4 == 0 else ("1/2" if wert > 0 else "−1/2")
            s.text(a, txt, q, groesse=24, ausrichtung="center", farbe=ROT if k % 4 == 0 else BLAU)
    s.punkt(a, c[0], c[1], r=0.08)
    b = s.achsen((-1, 1, 1), (0, 0.6, 0.5), breite=2.4, hoehe=2.1, mitte=(1.85, -0.05), xl="t", yl="f", xmarks=True, zahl=24)
    s.daten(b, [(-1, 0.5), (-0.03, 0.5)], farbe=BLAU, dicke=4)
    s.daten(b, [(0.03, 0.5), (1, 0.5)], farbe=BLAU, dicke=4)
    s.daten(b, [(-1, 0), (1, 0)], farbe=ROT, dicke=4)
    s.punkt(b, 0, 0, r=0.08)
    s.kreis(a, 1.85, -0.05 - 1.05 + 2.1 * 0.5 / 0.6, 0.07, farbe=BLAU, dicke=3, fuellung="#ffffff", deckung=1.0)
    s.text(b, s.tr("dia", "auf y = x", "on y = x", "en y = x", "在 y = x 上"), (0.0, 0.58), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(b, s.tr("ach", "auf der Achse", "on the axis", "en el eje", "在坐标轴上"), (0.1, 0.08), groesse=24, ausrichtung="center", farbe=ROT)
    s.speichern()


def k1gradient():
    """Höhenlinien der Schale, Gradient senkrecht dazu, Kurve mit Tangente."""
    s = Szene("hm3/k1gradient")
    a = s.welt()
    S = 0.92
    o = (-1.2, 0.0)

    def W(x, y):
        return (o[0] + S * x, o[1] + S * y)
    for wert, f in ((1, BLAU), (3, BLAU), (6, BLAU)):
        ax, by = sqrt(wert), sqrt(wert / 2)
        s.weg(a, "%g+%g*cos(t)" % (o[0], S * ax), "%g+%g*sin(t)" % (o[1], S * by), 0, 6.28319, farbe="#8fb4e3", dicke=3)
        q = W(ax * cos(radians(-22)), by * sin(radians(-22)))
        s.text(a, "φ = %d" % wert, (q[0] + 0.07, q[1] - 0.1), groesse=24, farbe=BLAU)
    # Gradient auf der Linie φ = 3
    for k in range(8):
        if k == 1:
            continue
        t = k * pi / 4
        x, y = sqrt(3) * cos(t), sqrt(1.5) * sin(t)
        p = W(x, y)
        q = (p[0] + S * 0.2 * 2 * x, p[1] + S * 0.2 * 4 * y)
        s.pfeil(p, q, "", farbe=GRAU, dicke=2, spitze=0.12)
    # Kurve durch P = (1, 1): y = (x^2 + 1)/2
    pk = [W(-0.8 + 2.65 * i / 60, ((-0.8 + 2.65 * i / 60) ** 2 + 1) / 2) for i in range(61)]
    s.daten(a, pk, farbe=GRUEN, dicke=4)
    P = W(1, 1)
    s.pfeil(P, (P[0] + S * 0.2 * 2, P[1] + S * 0.2 * 4), "", farbe=ROT, dicke=4, spitze=0.17)
    s.pfeil(P, (P[0] + S * 0.75, P[1] + S * 0.75), "", farbe=GRUEN, dicke=4, spitze=0.17)
    s.punkt(a, P[0], P[1], r=0.08)
    s.text(a, "∇φ", (P[0] + 0.1, P[1] + S * 0.8 + 0.12), groesse=26, farbe=ROT, ausrichtung="right")
    s.text(a, "γ̇", (P[0] + S * 0.75 + 0.14, P[1] + S * 0.75 - 0.3), groesse=26, farbe=GRUEN)
    s.text(a, "γ", (W(-0.8, 0.82)[0] - 0.08, W(-0.8, 0.82)[1] + 0.2), groesse=26, farbe=GRUEN, ausrichtung="center")
    xr = 1.72
    s.text(a, s.tr("stg", "Gradient:", "gradient:", "gradiente:", "梯度："), (xr, 1.15), groesse=24, farbe=ROT)
    s.text(a, s.tr("stg2", "senkrecht zur", "perpendicular to", "perpendicular a la", "垂直于等高线"), (xr, 0.8), groesse=24, farbe=ROT)
    s.text(a, s.tr("stg3", "Höhenlinie", "the level curve", "curva de nivel", " "), (xr, 0.45), groesse=24, farbe=ROT)
    s.text(a, s.tr("kur", "Änderung längs γ:", "change along γ:", "cambio sobre γ:", "沿 γ 的变化："), (xr, -0.3), groesse=24, farbe=GRUEN)
    s.text(a, "∇φ · γ̇", (xr, -0.65), groesse=24, farbe=GRUEN)
    s.speichern()


def k1radial():
    """Gleicher Inhalt wie k5radial, eigene Szene für Teil 1."""
    s = Szene("hm3/k1radial")
    a = s.welt()
    x0 = -2.35
    for r, z, y in ((0.4, "1", 0.2), (0.78, "4", 0.59), (1.16, "9", 0.97)):
        s.kreis(a, x0, 0, r, farbe=BLAU, dicke=3)
        s.text(a, z, (x0, y), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "u = f(r)", (x0, 1.5), groesse=26, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("z", "Zahlen", "numbers", "números", "数"), (x0, -1.5), groesse=24, ausrichtung="center", farbe=BLAU)
    for x0, laenge, titel, wort, farbe in (
            (0.0, lambda r, t: 0.34 if r < 0.5 else 0.22, "F = f(r) ê_r",
             s.tr("g", "gleich lang", "equal length", "misma longitud", "等长"), ROT),
            (2.35, lambda r, t: 0.05 + 0.17 * (1 + cos(t)), "F = g(x) ê_r",
             s.tr("u", "verschieden lang", "unequal length", "longitud distinta", "不等长"), GRUEN)):
        for r in (0.4, 0.85):
            s.kreis(a, x0, 0, r, farbe=HELLGRAU, dicke=2, dash=DASH)
            for k in range(8):
                t = radians(45 * k + (22.5 if r > 0.5 else 0))
                l = laenge(r, t)
                s.pfeil((x0 + r * cos(t), r * sin(t)), (x0 + (r + l) * cos(t), (r + l) * sin(t)), "", farbe=farbe, dicke=2, spitze=0.09)
        s.text(a, titel, (x0, 1.5), groesse=26, ausrichtung="center", farbe=farbe)
        s.text(a, wort, (x0, -1.5), groesse=24, ausrichtung="center", farbe=farbe)
    s.speichern()


def feld(s, a, x0, fx, fy, farbe, n=5, w=1.8, g=0.13, box=True):
    """Pfeilfeld im Quadrat [-1, 1]^2 um (x0, 0)."""
    for i in range(n):
        for j in range(n):
            x, y = -1 + 2 * i / (n - 1), -1 + 2 * j / (n - 1)
            u, v = fx(x, y), fy(x, y)
            if abs(u) + abs(v) < 1e-9:
                continue
            px, py = x0 + x * w / 2, y * w / 2
            s.pfeil((px - g * u, py - g * v), (px + g * u, py + g * v), "", farbe=farbe, dicke=2, spitze=0.09)
    if box:
        c = w / 4
        polygon(s, a, [(x0 - c, -c), (x0 + c, -c), (x0 + c, c), (x0 - c, c)], farbe=SCHWARZ, deckung=0.0, dicke=2, dash=DASH)


def k1quelle():
    s = Szene("hm3/k1quelle")
    a = s.welt()
    for x0, fx, fy, tit, farbe in (
            (-2.45, lambda x, y: x, lambda x, y: y, "div E = 2", ROT),
            (0.0, lambda x, y: 1.0, lambda x, y: 0.0, "div E = 0", BLAU),
            (2.45, lambda x, y: x, lambda x, y: -y, "div E = 0", BLAU)):
        feld(s, a, x0, fx, fy, farbe)
        s.text(a, tit, (x0, 1.42), groesse=26, ausrichtung="center", farbe=farbe)
    s.text(a, "E = (x, y)", (-2.45, -1.42), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "E = (1, 0)", (0.0, -1.42), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "E = (x, −y)", (2.45, -1.42), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("mehr", "mehr hinaus als hinein", "more out than in", "sale más que entra", "流出多于流入"), (-2.45, -1.82), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("gl", "hinein = hinaus", "in = out", "entra = sale", "流入 = 流出"), (0.0, -1.82), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "@gl", (2.45, -1.82), groesse=22, ausrichtung="center", farbe=BLAU)
    s.speichern()


def k1wirbel():
    s = Szene("hm3/k1wirbel")
    a = s.welt()
    feld(s, a, -2.45, lambda x, y: x, lambda x, y: y, BLAU, box=False)
    feld(s, a, 0.0, lambda x, y: -y, lambda x, y: x, ROT, box=False)
    feld(s, a, 2.45, lambda x, y: y, lambda x, y: 0.0, ROT, box=False)
    s.text(a, "F = (x, y)", (-2.45, 1.42), groesse=26, ausrichtung="center", farbe=BLAU)
    s.text(a, "F^⊥ = (−y, x)", (0.0, 1.42), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(a, "G = (y, 0)", (2.45, 1.42), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(a, "rot F = 0", (-2.45, -1.42), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "rot F^⊥ = 2", (0.0, -1.42), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "rot G = −1", (2.45, -1.42), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "div F = 2", (-2.45, -1.8), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "div F^⊥ = 0", (0.0, -1.8), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "div G = 0", (2.45, -1.8), groesse=24, ausrichtung="center", farbe=ROT)
    s.speichern()


def k1rechteck():
    s = Szene("hm3/k1rechteck")
    a = s.welt()
    x0, y0, w, h = -1.45, -0.85, 2.9, 1.75
    polygon(s, a, [(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], farbe=SCHWARZ, deckung=0.06, dicke=0)
    for p, q in (((x0, y0), (x0 + w, y0)), ((x0 + w, y0), (x0 + w, y0 + h)), ((x0 + w, y0 + h), (x0, y0 + h)), ((x0, y0 + h), (x0, y0))):
        s.pfeil(p, q, "", farbe=ROT, dicke=4, spitze=0.2)
    # Ecken P_0 ... P_3 (nicht P, Q, R, S: Q ist im Heft die Ladung, R ein Radius)
    for p, name, dx, dy in (((x0, y0), "P_0", -0.1, -0.3), ((x0 + w, y0), "P_1", 0.1, -0.3), ((x0 + w, y0 + h), "P_2", 0.1, 0.15), ((x0, y0 + h), "P_3", -0.1, 0.15)):
        s.punkt(a, p[0], p[1], r=0.07)
        s.text(a, name, (p[0] + dx, p[1] + dy), groesse=24, ausrichtung="right" if dx < 0 else "left")
    s.text(a, "a F_j(P_0)", (0, y0 - 0.35), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "b F_k(P_1)", (x0 + w + 0.2, 0.0), groesse=24, farbe=ROT)
    s.text(a, "−a F_j(P_3)", (0, y0 + h + 0.15), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, "−b F_k(P_0)", (x0 - 0.2, 0.0), groesse=24, ausrichtung="right", farbe=ROT)
    s.pfeil((2.65, -1.2), (3.3, -1.2), "", spitze=0.14, dicke=2)
    s.pfeil((2.65, -1.2), (2.65, -0.55), "", spitze=0.14, dicke=2)
    s.text(a, "x_j", (3.05, -1.55), groesse=24)
    s.text(a, "x_k", (2.3, -0.7), groesse=24, ausrichtung="center")
    s.speichern()


def k1operatoren():
    s = Szene("hm3/k1operatoren")
    a = s.welt()
    xs = (-2.85, -0.95, 0.95, 2.85)
    koepfe = (s.tr("fn", "Funktion", "function", "función", "函数"), s.tr("vf", "Vektorfeld", "vector field", "campo vectorial", "矢量场"),
              "@vf", "@fn")
    for x, k in zip(xs, koepfe):
        s.text(a, k, (x, 1.15), groesse=24, ausrichtung="center", farbe=GRAU)
    y1, y2 = 0.35, -0.65

    def kasten(x, y, t, farbe=SCHWARZ, f="#ffffff"):
        s.box(t, (x, y), breite=1.05, hoehe=0.56, groesse=24, farbe=farbe, fuellung=f)
    kasten(xs[0], y1, "φ")
    kasten(xs[1], y1, "F = ∇φ")
    kasten(xs[2], y1, "0", ROT)
    kasten(xs[1], y2, "A")
    kasten(xs[2], y2, "B = rot A")
    kasten(xs[3], y2, "0", ROT)
    s.pfeil((xs[0] + 0.56, y1), (xs[1] - 0.56, y1), "∇", spitze=0.15, groesse=24)
    s.pfeil((xs[1] + 0.56, y1), (xs[2] - 0.56, y1), "rot", spitze=0.15, groesse=24)
    s.pfeil((xs[1] + 0.56, y2), (xs[2] - 0.56, y2), "rot", spitze=0.15, groesse=24)
    s.pfeil((xs[2] + 0.56, y2), (xs[3] - 0.56, y2), "div", spitze=0.15, groesse=24)
    s.speichern()


# ------------------------------------------------------------------ neu seit der Überarbeitung (03.11.2026)
HELLBLAU = "#8fb4e3"


def ellipsen(s, a, o, S, farbe=BLAU, dicke=3):
    """Höhenlinien der Schale x^2 + 2y^2 = 1, 3, 6 um den Punkt o, Maßstab S."""
    for w in (1, 3, 6):
        s.weg(a, "%g+%g*cos(t)" % (o[0], S * sqrt(w)), "%g+%g*sin(t)" % (o[1], S * sqrt(w / 2)), 0, 6.28319, farbe=farbe, dicke=dicke)


def kreuz(s, a, o, S, x0, x1, y0, y1, xl="x", yl="y"):
    s.pfeil((o[0] + S * x0, o[1]), (o[0] + S * x1, o[1]), "", farbe=GRAU, dicke=2, spitze=0.14)
    s.pfeil((o[0], o[1] + S * y0), (o[0], o[1] + S * y1), "", farbe=GRAU, dicke=2, spitze=0.14)
    s.text(a, xl, (o[0] + S * x1 - 0.05, o[1] - 0.28), groesse=24, ausrichtung="right")
    s.text(a, yl, (o[0] - 0.12, o[1] + S * y1 - 0.12), groesse=24, ausrichtung="right")


def k1hoehen():
    """Die Schale als Landkarte: Höhenlinien und vier Funktionswerte."""
    s = Szene("hm3/k1hoehen")
    a = s.welt()
    o, S = (0.0, 0.0), 0.95

    def W(x, y):
        return (o[0] + S * x, o[1] + S * y)
    kreuz(s, a, o, S, -2.9, 3.1, -2.0, 2.2)
    ellipsen(s, a, o, S)
    for x, t in ((1, "1"), (2, "2"), (-1, "−1"), (-2, "−2")):
        s.linie(a, (W(x, 0)[0], -0.06), (W(x, 0)[0], 0.06), farbe=GRAU, dicke=2)
        s.text(a, t, (W(x, 0)[0], -0.3), groesse=22, ausrichtung="center", farbe=GRAU)
    for (x, y), t in (((-0.62, 0.74), "1"), ((-1.02, 1.22), "3"), ((-1.42, 1.64), "6")):
        s.text(a, t, W(x, y), groesse=24, ausrichtung="center", farbe=BLAU)
    for (x, y), t, dx, dy in (((0, 0), "0", 0.12, 0.2), ((2, 0), "4", 0.12, 0.2), ((-1, -1), "3", -0.12, -0.22), ((1, 1), "3", 0.12, 0.2)):
        p = W(x, y)
        s.punkt(a, p[0], p[1], r=0.07)
        s.text(a, t, (p[0] + dx, p[1] + dy), groesse=24, ausrichtung="left" if dx > 0 else "right")
    s.speichern()


def k1partiell():
    """Links die Gerade y = 1 in der Landkarte, rechts der Schnitt φ(x, 1) = x^2 + 2 mit Tangente."""
    s = Szene("hm3/k1partiell")
    a = s.welt()
    o, S = (-2.15, 0.0), 0.6

    def W(x, y):
        return (o[0] + S * x, o[1] + S * y)
    kreuz(s, a, o, S, -2.7, 2.9, -1.9, 2.1)
    ellipsen(s, a, o, S, farbe=HELLBLAU, dicke=2)
    s.linie(a, W(-2.5, 1), W(2.6, 1), farbe=ROT, dicke=5)
    s.text(a, "y = 1", (W(2.6, 1)[0], W(2.6, 1)[1] + 0.25), groesse=24, ausrichtung="right", farbe=ROT)
    p = W(1, 1)
    s.punkt(a, p[0], p[1], r=0.07)
    b = s.achsen((0, 2.4, 1), (0, 8, 2), breite=2.7, hoehe=2.6, mitte=(2.0, 0.0), xl="x", yl="φ(x, 1)", zahl=22)
    s.kurve(b, "x*x+2", x=(0, 2.35), farbe=ROT, dicke=5)
    s.kurve(b, "2*x+1", x=(0.2, 1.95), farbe=SCHWARZ, dicke=3, dash=DASH)
    s.punkt(b, 1, 3, r=0.07)
    s.text(b, s.tr("stg", "Steigung 2", "slope 2", "pendiente 2", "斜率 2"), (1.15, 2.1), groesse=24)
    s.speichern()


def k1offen():
    """Offene Kreisscheibe (Rand gestrichelt) und Kreisscheibe mit Rand."""
    s = Szene("hm3/k1offen")
    a = s.welt()
    R, r = 1.25, 0.4
    for x0, offen in ((-1.75, True), (1.75, False)):
        s.kreis(a, x0, 0, R, farbe=BLAU, dicke=3, fuellung=BLAU, deckung=0.1, dash=DASH if offen else "")
        if offen:
            c, f = (x0 + 0.45, 0.35), GRUEN
            s.text(a, s.tr("off", "offen", "open", "abierto", "开集"), (x0, -1.75), groesse=26, ausrichtung="center")
        else:
            c, f = (x0 + R, 0.0), ROT
            s.text(a, s.tr("noff", "nicht offen", "not open", "no abierto", "非开集"), (x0, -1.75), groesse=26, ausrichtung="center")
        s.kreis(a, c[0], c[1], r, farbe=f, dicke=3, fuellung=f, deckung=0.2)
        s.punkt(a, c[0], c[1], r=0.06)
        s.text(a, "x_0", (c[0], c[1] - 0.24), groesse=24, ausrichtung="center")
    s.speichern()


def k1feld():
    """Das Drehfeld (−y, x) auf einem Gitter, Pfeile auf 0,3 ihrer Länge verkleinert."""
    s = Szene("hm3/k1feld")
    a = s.welt()
    d = 0.72
    kreuz(s, a, (0, 0), d, -2.7, 2.8, -2.7, 2.8)
    for i in range(-2, 3):
        for j in range(-2, 3):
            p = (i * d, j * d)
            s.punkt(a, p[0], p[1], farbe=GRAU, r=0.04)
            if i or j:
                s.pfeil(p, (p[0] - 0.3 * d * j, p[1] + 0.3 * d * i), "", farbe=BLAU, dicke=2.5, spitze=0.09)
    s.pfeil((d, 0), (d, 0.3 * d), "", farbe=ROT, dicke=4, spitze=0.1)
    s.text(a, "E(1, 0)", (d, -0.27), groesse=22, ausrichtung="center", farbe=ROT)
    s.speichern()


def k1gradpfeil():
    """Gradient der Schale in (1, 1) aus den beiden Steigungen, auf ein Viertel verkleinert."""
    s = Szene("hm3/k1gradpfeil")
    a = s.welt()
    o, S = (-0.9, -0.15), 1.0

    def W(x, y):
        return (o[0] + S * x, o[1] + S * y)
    kreuz(s, a, o, S, -2.7, 2.9, -1.9, 2.4)
    ellipsen(s, a, o, S, farbe=HELLBLAU, dicke=2)
    s.linie(a, W(1.5, 1), W(1.5, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, W(1.5, 2), W(1, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.pfeil(W(1, 1), W(1.5, 1), "", farbe=ROT, dicke=4, spitze=0.13)
    s.pfeil(W(1, 1), W(1, 2), "", farbe=GRUEN, dicke=4, spitze=0.13)
    s.pfeil(W(1, 1), W(1.5, 2), "", farbe=SCHWARZ, dicke=4, spitze=0.13)
    p = W(1, 1)
    s.punkt(a, p[0], p[1], r=0.07)
    s.text(a, "∂φ/∂x = 2", (W(1.05, 0.8)[0], W(1.05, 0.8)[1]), groesse=22, farbe=ROT)
    s.text(a, "∂φ/∂y = 4", (W(0.93, 1.75)[0], W(0.93, 1.75)[1]), groesse=22, ausrichtung="right", farbe=GRUEN)
    s.text(a, "∇φ(1, 1) = (2, 4)", (W(1.6, 2.05)[0], W(1.6, 2.05)[1]), groesse=22)
    s.speichern()


def k1kette():
    """Wege x_k → y_j → f der Kettenregel."""
    s = Szene("hm3/k1kette")
    a = s.welt()
    xs, xm, xf = -3.0, 0.0, 3.0
    ys = (1.45, 0.45, -1.45)
    s.box("x_k", (xs, 0), breite=0.75, hoehe=0.6, form="ellipse", groesse=26)
    s.box("f", (xf, 0), breite=0.75, hoehe=0.6, form="ellipse", groesse=26)
    for y, t in zip(ys, ("y_1", "y_2", "y_m")):
        s.box(t, (xm, y), breite=0.75, hoehe=0.6, form="ellipse", groesse=26)
    s.text(a, "⋮", (xm, -0.45), groesse=28, ausrichtung="center")
    for y in ys:
        s.pfeil((xs + 0.4, 0.05 * y), (xm - 0.42, y - 0.08 * y), "", farbe=BLAU, dicke=3, spitze=0.15)
        s.pfeil((xm + 0.42, y - 0.08 * y), (xf - 0.4, 0.05 * y), "", farbe=ROT, dicke=3, spitze=0.15)
    s.text(a, "∂g_1/∂x_k", (-1.65, 1.2), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "∂g_m/∂x_k", (-1.65, -1.2), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "∂f/∂y_1", (1.6, 1.2), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, "∂f/∂y_m", (1.6, -1.2), groesse=22, ausrichtung="center", farbe=ROT)
    s.speichern()


def k1kurve():
    """Kreis γ(t) = (cos t, sin t) mit dem Tangentenvektor bei t = π/4."""
    s = Szene("hm3/k1kurve")
    a = s.welt()
    R = 1.5
    kreuz(s, a, (0, 0), R, -1.5, 1.75, -1.4, 1.65)
    s.weg(a, "%g*cos(t)" % R, "%g*sin(t)" % R, 0, 6.28319, farbe=BLAU, dicke=4, pfeile="0.4")
    s.punkt(a, R, 0, r=0.07)
    s.text(a, "γ(0)", (R + 0.1, -0.25), groesse=24)
    c = R / sqrt(2)
    s.punkt(a, c, c, r=0.07)
    s.text(a, "γ(π/4)", (c + 0.14, c + 0.12), groesse=24)
    s.pfeil((c, c), (c - R / sqrt(2), c + R / sqrt(2)), "", farbe=ROT, dicke=4, spitze=0.16)
    s.text(a, "γ̇(π/4)", (0.1, 2 * c + 0.05), groesse=24, farbe=ROT)
    s.speichern()


for f in (k1jacobi, k1schraeg, k1gradient, k1radial, k1quelle, k1wirbel, k1rechteck, k1operatoren,
          k1hoehen, k1partiell, k1offen, k1feld, k1gradpfeil, k1kette, k1kurve):
    f()
