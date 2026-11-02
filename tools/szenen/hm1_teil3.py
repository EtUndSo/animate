"""HM1 Teil 3 (kap3_stufen.tex): Funktionen und Polynome, zehn Abbildungen.

Aufruf: python tools/szenen/hm1_teil3.py, danach python tools/szenen_ansehen.py out.png hm1/k3zuordnung ... [--lang de]
Zahlen wie im Heft und in rechnung_kap3.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 24
H = "x^2-4*x+3"
P = "2*x^3-3*x^2-11*x+6"
R = "(2*x^3-3*x^2-11*x+6)/(x^2-x-2)"
HELLBLAU = "#dceafa"


def ellipse(s, x, y, b, h, farbe=GRAU, fuellung="#f2f2f2", on=None):
    return s._add("Ellipse", {"center": [x, y, 0], "width": b, "height": h, "color": farbe, "fill_color": fuellung, "fill_opacity": 1.0,
                              "stroke_width": 2.5, "dash": ""}, on)


def k3zuordnung():
    """Drei Teilbilder: Funktion, zwei Bilder, kein Bild."""
    s = Szene("hm1/k3zuordnung")
    t1 = s.tr("t1", "Funktion", "function", "función", "函数")
    t2 = s.tr("t2", "zwei Bilder:\nkeine Funktion", "two images:\nnot a function", "dos imágenes:\nno es función", "两个像：\n不是函数")
    t3 = s.tr("t3", "kein Bild:\nkeine Funktion", "no image:\nnot a function", "sin imagen:\nno es función", "没有像：\n不是函数")
    ys = (0.55, 0.0, -0.55)
    # (von, nach, rot) als Indizes in ys
    feld = ((-2.45, t1, BLAU, ((0, 0, 0), (1, 0, 0), (2, 1, 0))),
            (0.0, t2, ROT, ((0, 0, 0), (1, 1, 1), (1, 2, 1), (2, 2, 0))),
            (2.45, t3, ROT, ((0, 0, 0), (2, 1, 0))))
    for cx, titel, farbe, pfeile in feld:
        xa, xb = cx - 0.68, cx + 0.68
        ellipse(s, xa, 0, 0.72, 1.75)
        ellipse(s, xb, 0, 0.72, 1.75)
        s.text(None, "A", (xa, 1.1), ausrichtung="center")
        s.text(None, "B", (xb, 1.1), ausrichtung="center")
        for y in ys:
            s.punkt(None, xa, y, r=0.065)
            s.punkt(None, xb, y, r=0.065)
        for i, j, rot in pfeile:
            s.pfeil((xa + 0.1, ys[i]), (xb - 0.1, ys[j]), farbe=ROT if rot else BLAU, dicke=3, spitze=0.17)
        if cx > 2:                                 # das Element ohne Bild
            s.kreis(None, xa, 0, 0.14, farbe=ROT, dicke=3)
        s.text(None, titel, (cx, -1.26), ausrichtung="center", farbe=farbe)
    s.speichern()


def k3graph():
    """Graph der Parabel mit Wertebereich, Kreis als Nichtbeispiel."""
    s = Szene("hm1/k3graph")
    a = s.achsen((-1.2, 5.2), (-2, 6.5), breite=2.9, hoehe=2.05, mitte=(-1.85, 0), kreuz=True, xticks="4", yticks="-1;3", xl="x", yl="y")
    s.linie(a, (0, -1), (0, 6.2), farbe=ROT, dicke=6)
    s.kurve(a, H, x=(-0.7, 4.7), farbe=BLAU)
    s.linie(a, (4, -2), (4, 6.5), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, 4, 3, farbe=BLAU)
    s.text(a, "W(h)", (0.2, 5.1), farbe=ROT)
    s.text(a, "h", (4.75, 5.4), farbe=BLAU)
    b = s.achsen((-1.6, 1.6), (-1.6, 1.6), breite=2.05, hoehe=2.05, mitte=(1.8, 0), kreuz=True, xticks="0.6", yticks="1", xl="x", yl="y")
    s.weg(b, "cos(t)", "sin(t)", 0, 6.2832, farbe=BLAU, n=181)
    s.linie(b, (0.6, -1.6), (0.6, 1.6), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(b, 0.6, 0.8, farbe=ROT)
    s.punkt(b, 0.6, -0.8, farbe=ROT)
    t = s.tr("zwei", "zwei Bilder", "two images", "dos imágenes", "两个像")
    s.text(b, t, (0.72, -1.33), KLEIN, farbe=ROT)
    s.speichern()


def k3eigenschaften():
    """Gerade Glocke, ungerade Funktion, Monotonie mit waagerechtem Stück."""
    s = Szene("hm1/k3eigenschaften")
    s.welt()
    breite, hoehe, dx = 1.6, 1.7, 2.28
    t1 = s.tr("ger", "gerade", "even", "par", "偶函数")
    t2 = s.tr("ung", "ungerade", "odd", "impar", "奇函数")
    t3 = s.tr("mon", "monoton, nicht streng", "monotonic, not strict", "monótona, no estricta", "单调，但非严格")
    a = s.achsen((-3, 3), (-0.15, 1.25), breite=breite, hoehe=hoehe, mitte=(-dx, 0), kreuz=True, xticks="-1.5;1.5", yticks="1", xl="x", yl="y")
    s.kurve(a, "1/(1+x^2)", farbe=BLAU)
    s.linie(a, (-1.5, 0), (-1.5, 0.3077), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (1.5, 0), (1.5, 0.3077), farbe=GRAU, dicke=2, dash=DASH)
    s.pfeil((-1.5, 0.3077), (1.5, 0.3077), farbe=ROT, dicke=2.5, spitze=0.15, on=a, doppelt=True)
    s.punkt(a, -1.5, 0.3077, farbe=ROT)
    s.punkt(a, 1.5, 0.3077, farbe=ROT)
    b = s.achsen((-2.3, 2.3), (-3.2, 3.2), breite=breite, hoehe=hoehe, mitte=(0, 0), kreuz=True, xticks="-1.5;1.5", xzahlen=False, ymarks=False, yzahlen=False, xl="x", yl="y")
    s.kurve(b, "x^3-3*x", x=(-2.1, 2.1), farbe=BLAU)
    s.text(b, "−1.5", (-1.15, -0.8), KLEIN, "center")
    s.text(b, "1.5", (1.25, 0.8), KLEIN, "center")
    s.pfeil((-1.5, 1.125), (1.5, -1.125), farbe=ROT, dicke=2.5, spitze=0.15, on=b, doppelt=True)
    s.punkt(b, -1.5, 1.125, farbe=ROT)
    s.punkt(b, 1.5, -1.125, farbe=ROT)
    c = s.achsen((-2.3, 2.3), (-2.1, 2.1), breite=breite, hoehe=hoehe, mitte=(dx, 0), kreuz=True, xticks="-1;1", ymarks=False, yzahlen=False, xl="x", yl="y")
    links = [(-2.2 + 0.05 * k, (-1.2 + 0.05 * k) ** 3) for k in range(25)]
    rechts = [(1 + 0.05 * k, (0.05 * k) ** 3) for k in range(25)]
    s.daten(c, links, farbe=BLAU, dicke=5)
    s.daten(c, rechts, farbe=BLAU, dicke=5)
    s.linie(c, (-1, 0), (1, 0), farbe=ROT, dicke=6)
    for x, t in ((-dx, t1), (0, t2), (dx, t3)):
        s.text(None, t, (x, -1.28), ausrichtung="center")
    s.speichern()


def k3rueckwaerts():
    """Waagerechte in der Höhe y: Schnittpunkte sind die Lösungen."""
    s = Szene("hm1/k3rueckwaerts")
    s.welt()
    breite, hoehe, dx, unten = 1.6, 1.75, 2.28, -1.27
    t1 = s.tr("t1", "surjektiv,\nnicht injektiv", "surjective,\nnot injective", "sobreyectiva,\nno inyectiva", "满射，\n非单射")
    t2 = s.tr("t2", "injektiv,\nnicht surjektiv", "injective,\nnot surjective", "inyectiva,\nno sobreyectiva", "单射，\n非满射")
    t3 = s.tr("t3", "bijektiv", "bijective", "biyectiva", "双射")
    a = s.achsen((-1.4, 5.4), (-2, 6), breite=breite, hoehe=hoehe, mitte=(-dx, 0), kreuz=True, xticks="4", yticks="3", xl="x", yl="y")
    s.kurve(a, H, x=(-0.95, 4.95), farbe=BLAU)
    s.linie(a, (-1.4, 3), (5.4, 3), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, 0, 3, farbe=ROT)
    s.punkt(a, 4, 3, farbe=ROT)
    b = s.achsen((-0.5, 4.2), (-0.3, 1.8), breite=breite, hoehe=hoehe, mitte=(0, 0), kreuz=True, xticks="1", yticks="0.5;1;1.5", xl="x", yl="y")
    s.kurve(b, "1/(1+x^2)", x=(0, 4.2), farbe=BLAU)
    s.linie(b, (-0.5, 1.5), (4.2, 1.5), farbe=ROT, dicke=2, dash=DASH)
    s.linie(b, (-0.5, 0.5), (4.2, 0.5), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(b, 1, 0.5, farbe=BLAU)
    c = s.achsen((-1.9, 1.9), (-5, 5), breite=breite, hoehe=hoehe, mitte=(dx, 0), kreuz=True, xticks="1", yticks="2", xl="x", yl="y")
    s.kurve(c, "x^3", x=(-1.7, 1.7), farbe=BLAU)
    s.linie(c, (-1.9, 2), (1.9, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(c, 1.26, 2, farbe=BLAU)
    for x, t, f in ((-dx, t1, ROT), (0, t2, ROT), (dx, t3, BLAU)):
        s.text(None, t, (x, unten), ausrichtung="center", farbe=f)
    s.speichern()


def k3spiegel():
    """Hin- und Rückweg, Spiegelung an y = x."""
    s = Szene("hm1/k3spiegel")
    s.welt()
    hell = dict(form="round", fuellung=HELLBLAU, deckung=1.0, dicke=2.5)
    xa, xb = -2.9, -1.35
    s.box("x = 5", (xa, 0), breite=1.0, hoehe=0.6, **hell)
    s.box("y = 8", (xb, 0), breite=1.0, hoehe=0.6, **hell)
    s.pfeil((xa + 0.3, 0.32), (xb - 0.3, 0.32), knick="none", farbe=BLAU, spitze=0.18, dicke=3)
    s.pfeil((xb - 0.3, -0.32), (xa + 0.3, -0.32), knick="none", farbe=ROT, spitze=0.18, dicke=3)
    s.text(None, "h", (0.5 * (xa + xb), 0.56), ausrichtung="center", farbe=BLAU)
    s.text(None, "h^{−1}", (0.5 * (xa + xb), -0.58), ausrichtung="center", farbe=ROT)
    a = s.achsen((-1.8, 6.4), (-1.8, 6.4), breite=2.75, hoehe=2.75, mitte=(1.45, 0), kreuz=True, xticks="1;2;3;4;5;6", yticks="1;2;3;4;5;6", zahl=22, xl="x", yl="y")
    s.linie(a, (-1.8, -1.8), (6.3, 6.3), farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(a, H, x=(2, 4.65), farbe=BLAU)
    s.kurve(a, "2+sqrt(x+1)", x=(-1, 6.2), farbe=ROT)
    s.linie(a, (4, 3), (3, 4), farbe=GRAU, dicke=2, dash=DOT)
    s.punkt(a, 4, 3, farbe=BLAU)
    s.punkt(a, 3, 4, farbe=ROT)
    s.text(a, "h", (4.3, 1.5), farbe=BLAU)
    s.text(a, "h^{−1}", (1.25, 4.6), farbe=ROT)
    s.text(a, "y = x", (6.35, 5.1), KLEIN, "right", GRAU)
    s.speichern()


def k3nahnull():
    """P im Großen, Ausschnitt um 0 mit der Geraden a0 + a1 x."""
    s = Szene("hm1/k3nahnull")
    s.welt()
    t1 = s.tr("gross", "im Großen", "large scale", "a gran escala", "整体")
    t2 = s.tr("nah", "nahe x = 0", "near x = 0", "cerca de x = 0", "x = 0 附近")
    a = s.achsen((-2.8, 3.8), (-20, 20), breite=2.85, hoehe=1.9, mitte=(-1.95, 0), kreuz=True, xticks="-1;2", ymarks=False, yzahlen=False, xl="x")
    s.kurve(a, P, x=(-2.55, 3.55), farbe=BLAU)
    s.band(a, -0.3, 0.3, 2, 10, farbe=ROT, deckung=0.2)
    s.text(a, "P", (3.35, 3.5), farbe=BLAU)
    b = s.achsen((-0.34, 0.34), (2, 10), breite=2.85, hoehe=1.9, mitte=(1.95, 0), xl="x", xticks="-0.2;0;0.2", yticks="2;4;6;8;10", gitter=True)
    s.kurve(b, "6-11*x", x=(-0.34, 0.34), farbe=ROT, dicke=3, dash=DASH)
    s.kurve(b, P, x=(-0.34, 0.34), farbe=BLAU, dicke=4)
    s.punkt(b, 0, 6, farbe=SCHWARZ)
    s.text(b, "a₀ = 6", (0.03, 6.6), KLEIN)
    s.text(b, "6 − 11x", (-0.31, 3.4), KLEIN, farbe=ROT)
    s.text(b, "P", (0.27, 3.7), farbe=BLAU)
    s.text(None, t1, (-1.95, 1.4), ausrichtung="center")
    s.text(None, t2, (1.95, 1.4), ausrichtung="center")
    s.speichern()


def k3division():
    """Koeffizienten je Potenz in den drei Schritten der Division P : Q."""
    s = Szene("hm1/k3division")
    s.welt()
    t = s.tr("grad", "Grad", "degree", "grado", "次数")
    felder = (("P", "@{grad} 3", (2, -3, -11, 6), BLAU),
              ("P − 2x·Q", "@{grad} 2", (0, -1, -7, 6), BLAU),
              ("P − 2x·Q + Q", "@{grad} 1", (0, 0, -8, 4), ROT))
    potenz = ("x³", "x²", "x", "1")
    dx = 2.42
    for k, (titel, grad, werte, farbe) in enumerate(felder):
        mx = dx * (k - 1)
        a = s.achsen((-0.6, 3.6), (-13, 9), breite=2.1, hoehe=1.75, mitte=(mx, 0), xticks="", yticks="", xmarks=False, ymarks=False, xzahlen=False, yzahlen=False,
                     unsichtbar=True)
        s.linie(a, (-0.6, 0), (3.6, 0), farbe=SCHWARZ, dicke=2.5)
        s.stems(a, [0, 1, 2, 3], werte, farbe=farbe, breite=0.6, marker="none", r=0.0)
        for i, w in enumerate(werte):
            if w:
                txt = ("−%d" % -w) if w < 0 else "%d" % w
                s.text(a, txt, (i, w + (2.0 if w > 0 else -2.0)), KLEIN, "center", farbe)
            else:
                s.text(a, "0", (i, 2.0), KLEIN, "center", GRAU)
            s.text(a, potenz[i], (i, -16.2), KLEIN, "center")
        s.text(None, titel, (mx, 1.26), ausrichtung="center")
        s.text(None, grad, (mx, -1.62), ausrichtung="center", farbe=farbe)
    s.pfeil((-1.33, 0), (-1.09, 0), farbe=GRAU, spitze=0.15, dicke=2.5)
    s.pfeil((1.09, 0), (1.33, 0), farbe=GRAU, spitze=0.15, dicke=2.5)
    s.speichern()


def k3horner():
    """Schema für P an der Stelle 2 mit dem Ablauf als Pfeile."""
    s = Szene("hm1/k3horner")
    gr = 30
    sp = (-1.35, 0.2, 1.75, 3.3)                   # Spalten a3..a0
    z1, z2, z3 = 0.9, 0.0, -0.9
    oben, mitte, unten = (2, -3, -11, 6), (None, 4, 2, -18), (2, 1, -9, -12)
    fmt = lambda w: ("−%d" % -w) if w < 0 else "%d" % w
    for x, a, b, c in zip(sp, oben, mitte, unten):
        s.text(None, fmt(a), (x, z1), gr, "center")
        if b is not None:
            s.text(None, fmt(b), (x, z2), gr, "center", ORANGE)
        s.text(None, fmt(c), (x, z3), gr, "center", ROT if c == -12 else BLAU)
    s.text(None, "x₀ = 2", (-2.85, z2), gr, "center", ORANGE)
    s.linie(None, (-2.1, z2 - 0.45), (3.85, z2 - 0.45), dicke=2.5)
    s.linie(None, (-2.1, z1 + 0.32), (-2.1, z3 - 0.32), dicke=2.5)
    for i in range(3):
        s.pfeil((sp[i] + 0.34, z3 + 0.14), (sp[i + 1] - 0.36, z2 - 0.14), farbe=ORANGE, spitze=0.16, dicke=2.5)
        s.text(None, "·2", (0.5 * (sp[i] + sp[i + 1]) + 0.16, z2 - 0.08), KLEIN + 2, "center", ORANGE)
        x = sp[i + 1]
        s.pfeil((x, z1 - 0.22), (x, z2 + 0.2), farbe=GRUEN, spitze=0.14, dicke=2.5)
        s.pfeil((x, z2 - 0.2), (x, z3 + 0.22), farbe=GRUEN, spitze=0.14, dicke=2.5)
        s.text(None, "+", (x + 0.2, z1 - 0.44), KLEIN + 2, "center", GRUEN)
    t1 = s.tr("q", "Koeffizienten des Quotienten", "coefficients of the quotient", "coeficientes del cociente", "商的系数")
    t2 = s.tr("r", "Rest = P(2)", "remainder = P(2)", "resto = P(2)", "余数 = P(2)")
    s.text(None, t1, (0.2, z3 - 0.5), KLEIN, "center", BLAU)
    s.text(None, t2, (3.15, z3 - 0.5), KLEIN, "center", ROT)
    s.speichern()


def k3vielfach():
    """(x-1)^m (x+2) für m = 1, 2, 3 bei gleichem Maßstab."""
    s = Szene("hm1/k3vielfach")
    s.welt()
    dx = 2.28
    t = (s.tr("m1", "m = 1: kreuzt", "m = 1: crosses", "m = 1: cruza", "m = 1：穿过"),
         s.tr("m2", "m = 2: berührt", "m = 2: touches", "m = 2: toca", "m = 2：相切"),
         s.tr("m3", "m = 3: kreuzt flach", "m = 3: crosses flat", "m = 3: cruza plana", "m = 3：平缓穿过"))
    for m in (1, 2, 3):
        a = s.achsen((-0.7, 2.4), (-6, 6), breite=1.6, hoehe=1.7, mitte=(dx * (m - 2), 0), kreuz=True, xticks="1", ymarks=False, yzahlen=False, xl="x", yl="y")
        f = "(x-1)^%d*(x+2)" % m
        s.kurve(a, f, x=(-0.6, 2.25), farbe=BLAU)
        s.punkt(a, 1, 0, farbe=ROT)
        s.text(None, t[m - 1], (dx * (m - 2), -1.25), ausrichtung="center")
    s.speichern()


def grenze(f, a, b, y):
    """Bisektion: Stelle in [a, b] mit f = y."""
    fa = f(a) - y
    for _ in range(60):
        c = 0.5 * (a + b)
        if (f(c) - y) * fa > 0:
            a, fa = c, f(c) - y
        else:
            b = c
    return a


def k3pole():
    """R mit zwei Polen und Asymptote, daneben eine Lücke."""
    s = Szene("hm1/k3pole")
    s.welt()
    r = lambda x: (2 * x ** 3 - 3 * x ** 2 - 11 * x + 6) / (x ** 2 - x - 2)
    ymax = 13
    a = s.achsen((-4.2, 5.4), (-14, 14), breite=3.8, hoehe=2.6, mitte=(-1.25, 0), kreuz=True, xticks="-2;-1;2;3", yticks="10", xl="x", yl="y")
    s.linie(a, (-1, -14), (-1, 14), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (2, -14), (2, 14), farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(a, "2*x-1", x=(-4.2, 5.4), farbe=ORANGE, dicke=3, dash=DASH)
    x1 = grenze(r, -4, -1.01, ymax)
    x2, x3 = grenze(r, -0.99, 0.5, -ymax), grenze(r, 0.5, 1.99, ymax)
    x4 = grenze(r, 2.01, 3, -ymax)
    s.kurve(a, R, x=(-4.2, x1), farbe=BLAU)
    s.kurve(a, R, x=(x2, x3), farbe=BLAU)
    s.kurve(a, R, x=(x4, 5.4), farbe=BLAU)
    for x in (-2, 0.5, 3):
        s.punkt(a, x, 0, farbe=ROT)
    t = s.tr("pol", "Pol", "pole", "polo", "极点")
    s.text(a, t, (-1.2, -11.6), KLEIN, "right", GRAU)
    s.text(a, t, (2.2, 11.6), KLEIN, "left", GRAU)
    s.text(a, "2x − 1", (5.3, 12.2), KLEIN, "right", ORANGE)
    s.text(a, "R", (4.3, 2.8), farbe=BLAU)
    t2 = s.tr("lu", "Lücke", "gap", "hueco", "间断")
    b = s.achsen((-0.6, 3.8), (-1, 7), breite=1.7, hoehe=2.6, mitte=(2.32, 0), kreuz=True, xticks="2", yticks="4", xl="x", yl="y")
    s.kurve(b, "x+2", x=(-0.5, 3.6), farbe=BLAU)
    s.kreis(b, 2, 4, 0.1, farbe=BLAU, dicke=3, fuellung="#ffffff", deckung=1.0)
    s.text(b, "L", (3.1, 6.0), farbe=BLAU)
    s.text(b, t2, (2.3, 3.2), KLEIN, farbe=ROT)
    s.speichern()


for f in (k3zuordnung, k3graph, k3eigenschaften, k3rueckwaerts, k3spiegel, k3nahnull, k3division, k3horner, k3vielfach, k3pole):
    f()
