"""Höhere Mathematik 1, Teil 7 (kap7_stufen.tex): Potenzreihen und Eulersche Formel.

Aufruf: python tools/szenen/hm1_teil7.py, danach python tools/szenen_ansehen.py out.png hm1/k7kreis ... [--lang de]
Alle Zahlen stehen im Heft und in C:/Bücher/HöMa1/Arbeitshefte/rechnung_kap7.py. Rechenmodell: f(x) = Σ x^n/(n 2^n) mit R = 2,
g(x) = Σ x^(2n)/4^n, z1 = 3 + i, z2 = 1 + 2i, z^3 = 8i. Alle komplexen Ebenen haben in x und y denselben Maßstab.
"""
import sys
from math import atan2, cos, exp, factorial, pi, sin, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24                    # Beschriftung in den Bildern
R_P = 0.055                # Punktradius einer Folge
HELLBLAU, HELLGRUEN, HELLORANGE, HELLROT, HELLGR = "#dceafa", "#d6efe0", "#fbe3d9", "#f8dcdc", "#eeeeee"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche


def ebene(s, x, y, m, mitte=(0, 0), xt="", yt="", **kw):
    """Achsenkreuz mit m Szeneneinheiten je Zahlschritt, in beiden Richtungen gleich."""
    kw.setdefault("xzahlen", False)
    kw.setdefault("yzahlen", False)
    return s.achsen(x, y, breite=(x[1] - x[0]) * m, hoehe=(y[1] - y[0]) * m, mitte=mitte, kreuz=True, xticks=xt, yticks=yt,
                    xl="Re", yl="Im", **kw)


def zeiger(s, on, a, b, farbe=BLAU, dicke=4, dash="", spitze=0.2):
    return s.pfeil(a, b, "", farbe=farbe, spitze=spitze, dicke=dicke, on=on, dash=dash)


def kreis(s, on, r, farbe=GRAU, dicke=2.5, dash=""):
    return s.weg(on, "%.5f*cos(t)" % r, "%.5f*sin(t)" % r, 0, 2 * pi, farbe=farbe, dicke=dicke, dash=dash)


def bogen(s, on, r, w0, w1, farbe=GRAU, dicke=3, pfeile=""):
    return s.weg(on, "%.5f*cos(t)" % r, "%.5f*sin(t)" % r, w0, w1, farbe=farbe, dicke=dicke, pfeile=pfeile, n=61)


def polar(r, w):
    return (r * cos(w), r * sin(w))


# ------------------------------------------------------------------------------------------ Stufe 1
def k7kreis():
    """Links die Glieder des Rechenmodells für x = 1, 2, 3, rechts der Konvergenzkreis mit R = 2."""
    s = Szene("hm1/k7kreis")
    glieder = s.tr("gl", "Glieder |a_n x^n|", "Terms |a_n x^n|", "Términos |a_n x^n|", "各项 |a_n x^n|")
    a = s.achsen((0, 13), (0, 2.2), breite=2.36, hoehe=2.1, mitte=(-1.78, 0), xticks="1;5;10", yticks="0;1;2", xl="n", xl_mitte=False, titel=glieder)
    for n in range(1, 13):
        s.punkt(a, n, 1 / (n * 2 ** n), farbe=GRUEN, r=R_P)
        s.punkt(a, n, 1 / n, farbe=BLAU, r=R_P)
        w = 1.5 ** n / n
        if w <= 2.2:
            s.punkt(a, n, w, farbe=ROT, r=R_P)
    s.text(a, s.tr("x3", "x = 3 wächst", "x = 3 grows", "x = 3 crece", "x = 3 增长"), (6.7, 1.98), KL, "left", ROT)
    s.text(a, s.tr("x2", "x = 2 wie 1/n", "x = 2 like 1/n", "x = 2 como 1/n", "x = 2 如 1/n"), (3.3, 0.74), KL, "left", BLAU)
    s.text(a, s.tr("x1", "x = 1 fällt", "x = 1 falls", "x = 1 cae", "x = 1 下降"), (3.3, 0.47), KL, "left", GRUEN)

    b = ebene(s, (-2.45, 2.6), (-2.3, 2.5), 0.45, mitte=(1.5, 0.1), xt="-2;-1;1;2", yt="-2;-1;1;2")
    s.flaeche(b, "sqrt(4-x^2)", -2, 2, f2="-sqrt(4-x^2)", farbe=BLAU, deckung=0.16)
    kreis(s, b, 2, GRAU, 2.5, DASH)
    s.linie(b, (0, 0), polar(2, -0.8), farbe=SCHWARZ, dicke=2.5)
    s.text(b, "R = 2", (0.62, -0.42), KL, "left")
    s.punkt(b, -2, 0, farbe=GRUEN, r=0.085)
    s.punkt(b, 2, 0, farbe=ROT, r=0.085)
    s.text(b, "−2", (-2.32, -0.45), KL, "center", GRUEN)
    s.text(b, "2", (2.22, -0.42), KL, "center", ROT)
    s.text(b, s.tr("abs", "innen absolut konvergent", "inside absolutely convergent", "dentro absolutamente convergente", "圆内绝对收敛"), (0, -2.72), KL, "center", BLAU)
    s.text(b, s.tr("div", "außen\ndivergent", "outside\ndivergent", "fuera\ndivergente", "圆外\n发散"), (1.5, 2.0), KL, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k7limsup():
    """Die Wurzeln der Koeffizienten: links konvergent, rechts zwei Häufungspunkte."""
    s = Szene("hm1/k7limsup")
    y = (0, 1.0)
    H = 1.65
    t1 = s.tr("t1", "f: eine Grenze", "f: one limit", "f: un límite", "f：一个极限")
    t2 = s.tr("t2", "g: Lücken", "g: gaps", "g: huecos", "g：有空缺")
    a = s.achsen((0, 25), y, breite=2.7, hoehe=H, mitte=(-1.75, 0), xticks="1;10;20", yticks="0;0.5;1", xl="n", xl_mitte=False, yl="ⁿ√|a_n|", titel=t1)
    s.linie(a, (0, 0.5), (25, 0.5), farbe=ROT, dicke=2.5, dash=DASH)
    for n in range(1, 25):
        s.punkt(a, n, 0.5 / n ** (1 / n), farbe=BLAU, r=R_P)
    s.text(a, "B = 1/2", (24.5, 0.62), KL, "right", ROT)
    b = s.achsen((0, 25), y, breite=2.7, hoehe=H, mitte=(1.75, 0), xticks="1;10;20", yticks="0;0.5;1", xl="n", xl_mitte=False, yl="ⁿ√|a_n|", titel=t2)
    s.linie(b, (0, 0.5), (25, 0.5), farbe=ROT, dicke=2.5, dash=DASH)
    for n in range(1, 25):
        s.punkt(b, n, 0.5 if n % 2 == 0 else 0, farbe=BLAU if n % 2 == 0 else ORANGE, r=R_P)
    s.text(b, "lim sup = 1/2", (24.5, 0.62), KL, "right", ROT)
    s.text(b, s.tr("zw", "Häufungspunkt 0", "cluster point 0", "punto de acumulación 0", "聚点 0"), (24.5, 0.13), KL, "right", ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k7sinus():
    """Teilsummen der Sinusreihe s_0 bis s_4 gegen den Sinus."""
    s = Szene("hm1/k7sinus")
    a = s.achsen((0, 7.3), (-2.05, 2.05), breite=5.8, hoehe=2.45, kreuz=True, xticks="1;2;3;4;5;6;7", yticks="-2;-1;1;2", xl="x", yl="y")

    def teil(x, N):
        return sum((-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1) for n in range(N + 1))
    farben = (GRAU, ORANGE, GRUEN, ROT, "#7a4fb5")
    orte = ((2.05, 1.72), (2.45, -1.72), (3.28, 1.55), (5.0, -1.72), (5.72, 1.72))
    for N, (f, ort) in enumerate(zip(farben, orte)):
        pts = [(0.02 * i, teil(0.02 * i, N)) for i in range(0, 366)]
        s.daten(a, [p for p in pts], farbe=f, dicke=3)
        s.text(a, "s_%d" % N, ort, KL, "left", f)
    s.kurve(a, "sin(x)", farbe=BLAU, dicke=5)
    s.text(a, "sin x", (6.35, 1.0), KL, "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k7cauchy():
    """Produkt zweier Potenzreihen als Tabelle; gleiche Farbe heißt gleiche Potenz von x."""
    s = Szene("hm1/k7cauchy")
    B, H = 1.12, 0.46
    x0, y0 = -1.65, 1.2
    farben = {0: (BLAU, HELLBLAU), 1: (GRUEN, HELLGRUEN), 2: (BRAUN, HELLORANGE), 3: (ROT, HELLROT)}

    def pot(k):
        return "" if k == 0 else (" x" if k == 1 else " x^%d" % k)
    for n in range(4):
        s.box("a_%d%s" % (n, pot(n)), (x0 + B * n, y0 + H), B, H, groesse=KL, farbe=SCHWARZ, fuellung="#ffffff", dicke=0)
    for m in range(4):
        s.box("b_%d%s" % (m, pot(m)), (x0 - B, y0 - H * m), B, H, groesse=KL, farbe=SCHWARZ, fuellung="#ffffff", dicke=0)
    for m in range(4):
        for n in range(4):
            k = n + m
            f, h = farben.get(k, (GRAU, HELLGR))
            s.box("a_%d b_%d%s" % (n, m, pot(k)), (x0 + B * n, y0 - H * m), B, H, groesse=KL, farbe=f, fuellung=h, dicke=1.5)
    s.text(None, "…", (x0 + 3.62 * B, y0 - H), KL, "left", GRAU)
    s.text(None, "…", (x0 + 1.5 * B, y0 - 3.72 * H), KL, "center", GRAU)
    leg = s.tr("leg", "Gleiche Farbe, gleiche Potenz, Summe je Diagonale:", "Same colour, same power, sum along each diagonal:", "Mismo color, misma potencia, suma por diagonal:", "同色即同次幂，沿对角线求和：")
    s.text(None, leg, (x0 - 1.5 * B, y0 - 4.15 * H), KL, "left")
    for k, (f, h) in farben.items():
        s.text(None, "c_%d%s" % (k, pot(k)), (x0 - 1.5 * B + 1.25 * k, y0 - 4.95 * H), KL, "left", f)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k7zweiwege():
    """Zwei Wege zu e: Teilsummen der Reihe und die Folge (1 + 1/k)^k."""
    s = Szene("hm1/k7zweiwege")
    a = s.achsen((0, 12.5), (1.9, 2.8), breite=5.4, hoehe=2.0, mitte=(-0.5, 0), xticks="1;2;3;4;5;6;7;8;9;10;11;12", yticks="2;2.2;2.4;2.6;2.8", xl="k", xl_mitte=False)
    s.linie(a, (0, exp(1)), (12.5, exp(1)), farbe=GRAU, dicke=2.5, dash=DASH)
    for k in range(1, 13):
        s.punkt(a, k, sum(1 / factorial(j) for j in range(k + 1)), farbe=BLAU, r=0.07)
        s.punkt(a, k, (1 + 1 / k) ** k, farbe=ORANGE, r=0.07)
    s.text(a, "e = 2.718…", (12.7, exp(1)), KL, "left", GRAU)
    s.text(a, s.tr("rh", "Reihe s_k", "series s_k", "serie s_k", "级数 s_k"), (3.1, 2.55), KL, "left", BLAU)
    s.text(a, s.tr("fg", "Folge (1 + 1/k)^k", "sequence (1 + 1/k)^k", "sucesión (1 + 1/k)^k", "数列 (1 + 1/k)^k"), (6.2, 2.42), KL, "left", BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k7euler():
    """Links der Einheitskreis mit e^{iφ} für φ = 1, rechts die Glieder der Reihe für φ = 2 als Polygonzug."""
    s = Szene("hm1/k7euler")
    m = 0.8
    a = ebene(s, (-1.42, 1.5), (-1.3, 1.5), m, mitte=(-1.85, 0))
    kreis(s, a, 1, GRAU)
    p = polar(1, 1)
    s.linie(a, (p[0], 0), p, farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (0, 0), (0, p[1]), farbe=GRUEN, dicke=4)
    s.linie(a, (0, 0), (p[0], 0), farbe=BLAU, dicke=4)
    s.linie(a, (0, 0), p, farbe=SCHWARZ, dicke=3)
    s.linie(a, (0, p[1]), p, farbe=GRAU, dicke=2, dash=DASH)
    bogen(s, a, 1, 0, 1, ROT, 5)
    s.punkt(a, *p, farbe=ROT, r=0.085)
    for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        s.punkt(a, x, y, farbe=GRAU, r=0.055)
    s.text(a, "e^{iφ}", (p[0] + 0.08, p[1] + 0.12), KL, "left", ROT)
    s.text(a, "cos φ", (p[0] / 2, -0.2), KL, "center", BLAU)
    s.text(a, "sin φ", (-0.1, p[1] * 0.5), KL, "right", GRUEN)
    s.text(a, "φ", (1.06, 0.5), KL, "left", ROT)
    s.text(a, "1", (1.08, -0.2), KL, "left", GRAU)
    s.text(a, "i", (-0.12, 1.18), KL, "right", GRAU)
    s.text(a, "−1", (-1.08, 0.2), KL, "right", GRAU)
    s.text(a, "−i", (-0.1, -1.17), KL, "right", GRAU)

    b = ebene(s, (-1.5, 1.5), (-0.28, 2.36), m, mitte=(1.8, 0))
    kreis(s, b, 1, HELLGRAU, 2.5, DASH)
    z, pkt = 0j, [0j]
    for n in range(9):
        z += (2j) ** n / factorial(n)
        pkt.append(z)
    for n in range(8):
        q0, q1 = pkt[n], pkt[n + 1]
        d = BLAU if n % 2 == 0 else GRUEN
        if n < 6:
            zeiger(s, b, (q0.real, q0.imag), (q1.real, q1.imag), d, 3.5, spitze=0.16)
    s.punkt(b, cos(2), sin(2), farbe=ROT, r=0.085)
    s.text(b, "e^{2i}", (-0.5, 1.22), KL, "center", ROT)
    s.text(b, "1", (0.5, -0.22), KL, "center", BLAU)
    s.text(b, "2i", (1.08, 1.0), KL, "left", GRUEN)
    s.text(b, "−2", (0.5, 2.16), KL, "center", BLAU)
    s.text(b, "−4i/3", (-1.08, 1.35), KL, "right", GRUEN)
    s.text(b, "2/3", (-0.66, 0.46), KL, "center", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k7pi():
    """Cosinus und Sinus von 0 bis 2π mit den Punkten der Wertetabelle; χ = π/2 ist die Nullstelle des Cosinus."""
    s = Szene("hm1/k7pi")
    a = s.achsen((0, 6.6), (-1.25, 1.35), breite=6.2, hoehe=2.15, xticks="%.5f;%.5f;%.5f;%.5f;%.5f" % (pi / 4, pi / 2, pi, 3 * pi / 2, 2 * pi),
                 yticks="-1;0;1", xzahlen=False, xl="φ", xl_mitte=False)
    s.band(a, 0, 2, -1.25, 1.35, farbe=ORANGE, deckung=0.09)
    s.linie(a, (0, 0), (6.6, 0), farbe=GRAU, dicke=2)
    s.kurve(a, "cos(x)", x=(0, 2 * pi), farbe=BLAU, dicke=4.5)
    s.kurve(a, "sin(x)", x=(0, 2 * pi), farbe=GRUEN, dicke=4.5)
    for w in (0, pi / 4, pi / 2, pi, 3 * pi / 2, 2 * pi):
        s.punkt(a, w, cos(w), farbe=BLAU, r=0.07)
        s.punkt(a, w, sin(w), farbe=GRUEN, r=0.07)
    for w, t in ((pi / 4, "π/4"), (pi / 2, "π/2"), (pi, "π"), (3 * pi / 2, "3π/2"), (2 * pi, "2π")):
        s.text(a, t, (w, -1.52), KL, "center")
    s.punkt(a, pi / 2, 0, farbe=ROT, r=0.095)
    s.text(a, "χ = π/2", (1.68, 0.2), KL, "left", ROT)
    s.text(a, "cos φ", (4.55, 0.92), KL, "left", BLAU)
    s.text(a, "sin φ", (2.42, 1.0), KL, "left", GRUEN)
    s.text(a, "[0, 2]", (1.0, 1.12), KL, "center", BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k7dreh():
    """Links dreht und streckt z1 das Dreieck (0, 1, z2), rechts entsteht 1/z2 aus Kehrwert des Betrags und Spiegelung."""
    s = Szene("hm1/k7dreh")
    z1, z2, p = (3, 1), (1, 2), (1, 7)
    a = ebene(s, (-0.5, 3.9), (-0.45, 7.45), 0.38, mitte=(-2.15, 0.05), xt="1;2;3", yt="1;2;3;4;5;6;7")
    for u, v, f, d in (((0, 0), (1, 0), ORANGE, 4), ((1, 0), z2, ORANGE, 3), ((0, 0), z2, ORANGE, 4)):
        s.linie(a, u, v, farbe=f, dicke=d)
    s.linie(a, z1, p, farbe=ROT, dicke=3)
    zeiger(s, a, (0, 0), z1, BLAU, 4)
    zeiger(s, a, (0, 0), p, ROT, 4)
    w1, w2 = atan2(1, 3), atan2(2, 1)
    bogen(s, a, 2.15, 0, w1, BLAU, 3)
    bogen(s, a, 2.9, w1, w1 + w2, GRAU, 3, "0.6")
    s.text(a, "1", (1.0, -0.62), KL, "center", BRAUN)
    s.text(a, "z_2", (1.15, 2.2), KL, "left", BRAUN)
    s.text(a, "z_1", (3.14, 1.15), KL, "left", BLAU)
    s.text(a, "z_1 z_2 = 1 + 7i", (1.2, 7.18), KL, "left", ROT)
    s.text(a, "φ_1", (2.32, 0.33), KL, "left", BLAU)
    s.text(a, "φ_2", (2.28, 2.9), KL, "left", GRAU)

    b = ebene(s, (-2.35, 2.5), (-2.5, 2.5), 0.58, mitte=(1.45, 0.05), xt="-2;-1;1;2", yt="-2;-1;1;2")
    kreis(s, b, 1, GRAU)
    q, u, k = (1, -2), (0.2, 0.4), (0.2, -0.4)
    s.linie(b, (0, 0), z2, farbe=GRUEN, dicke=3)
    s.linie(b, (0, 0), q, farbe=HELLGRAU, dicke=2.5, dash=DASH)
    s.linie(b, u, k, farbe=GRAU, dicke=2.5, dash=DASH)
    s.punkt(b, *z2, farbe=GRUEN, r=0.085)
    s.punkt(b, *u, farbe=ORANGE, r=0.075)
    s.punkt(b, *k, farbe=ROT, r=0.085)
    s.punkt(b, *q, farbe=GRAU, r=0.07)
    s.text(b, "z_2", (1.15, 2.05), KL, "left", GRUEN)
    s.text(b, "z̄_2", (1.15, -2.05), KL, "left", GRAU)
    s.linie(b, u, (1.12, 0.62), farbe=ORANGE, dicke=2)
    s.text(b, "z_2/|z_2|^2", (1.16, 0.62), KL, "left", BRAUN)
    s.text(b, "1/z_2", (-0.12, -0.55), KL, "right", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k7wurzeln():
    """Links die drei Lösungen von z^3 = 8i, rechts die fünf Lösungen von z^5 = 1."""
    s = Szene("hm1/k7wurzeln")
    a = ebene(s, (-2.6, 2.65), (-2.6, 2.75), 0.47, mitte=(-1.85, 0.05), xt="-2;2", yt="-2;2")
    wl = [(pi / 2 + 2 * pi * k) / 3 for k in range(3)]
    pl = [polar(2, w) for w in wl]
    kreis(s, a, 2, GRAU)
    for k in range(3):
        s.linie(a, pl[k], pl[(k + 1) % 3], farbe=ORANGE, dicke=3)
    bogen(s, a, 2.32, wl[0], wl[1], ROT, 3, "0.7")
    for p in pl:
        s.punkt(a, *p, farbe=BLAU, r=0.085)
    s.text(a, "z_0", (2.05, 0.68), KL, "left", BLAU)
    s.text(a, "z_1", (-2.05, 0.68), KL, "right", BLAU)
    s.text(a, "z_2", (0.2, -2.32), KL, "left", BLAU)
    s.text(a, "2π/3", (0.05, 2.52), KL, "left", ROT)
    s.text(a, "|z| = 2", (0.15, 0.3), KL, "left", GRAU)

    b = ebene(s, (-1.3, 1.42), (-1.32, 1.4), 0.92, mitte=(1.62, 0.05))
    wr = [2 * pi * k / 5 for k in range(5)]
    pr = [polar(1, w) for w in wr]
    kreis(s, b, 1, GRAU)
    for k in range(5):
        s.linie(b, pr[k], pr[(k + 1) % 5], farbe=ORANGE, dicke=3)
    bogen(s, b, 1.16, wr[0], wr[1], ROT, 3, "0.7")
    for k, p in enumerate(pr):
        s.punkt(b, *p, farbe=BLAU, r=0.085)
    orte = (((1.08, -0.2), "left"), ((0.3, 0.64), "right"), ((-0.94, 0.8), "right"), ((-0.94, -0.84), "right"), ((0.42, -1.14), "left"))
    for k, (ort, ausr) in enumerate(orte):
        s.text(b, "z_%d" % k, ort, KL, ausr, BLAU)
    s.text(b, "2π/5", (1.03, 0.76), KL, "left", ROT)
    s.speichern()


if __name__ == "__main__":
    for f in (k7kreis, k7limsup, k7sinus, k7cauchy, k7zweiwege, k7euler, k7pi, k7dreh, k7wurzeln):
        f()
