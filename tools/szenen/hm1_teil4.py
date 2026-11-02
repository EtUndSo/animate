"""Höhere Mathematik 1, Teil 4 (kap4_stufen.tex): Folgen und Grenzwerte.

Aufruf: python tools/szenen/hm1_teil4.py, danach python tools/szenen_ansehen.py out.png hm1/k4folgen ... [--lang de]
Alle Zahlen stehen im Heft und in rechnung_kap4.py: a_n = 2 + (-1)^n 3/n, s_n = 2 - 2^(-n), Heron-Folge x_n für Wurzel 2.
Folgen sind Punkte, keine Linien: zwischen den Indizes gibt es nichts. Die Treppen in k4trichter sind die Hüllen b_n, c_n.
"""
import sys
from math import factorial, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 24                 # Beschriftung in den Bildern
HELLBLAU, HELLORANGE, HELLGRUEN = "#dceafa", "#fbe3d9", "#d6efe0"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche
R = 0.055                  # Punktradius einer Folge


def a(n):
    return 2 + (-1) ** n * 3 / n


def d(n):
    return (-1) ** n * 3 / n


def s_(n):
    return 2 - 0.5 ** n


def glieder(s, on, pts, farbe=BLAU, r=R):
    for x, y in pts:
        s.punkt(on, x, y, farbe=farbe, r=r)


def zahlengerade(s, y, x0, breite, v0, v1, ticks, werte, farbe=BLAU):
    """Zahlengerade in Szeneneinheiten; die Werte landen als Punkte darauf."""
    def p(v):
        return x0 + breite * (v - v0) / (v1 - v0)
    s.pfeil((x0 - 0.1, y), (x0 + breite + 0.2, y), "", spitze=0.14, dicke=2.5)
    for t in ticks:
        s.linie(None, (p(t), y - 0.07), (p(t), y + 0.07), dicke=2.5)
        s.text(None, str(t).replace("-", "−"), (p(t), y - 0.27), KLEIN, "center")
    for v in werte:
        s.punkt(None, p(v), y, farbe=farbe, r=0.05)


# ------------------------------------------------------------------------------------------ Stufe 1
def k4folgen():
    """Zwei Folgen des Rechenmodells als Punkte über n und auf der Zahlengeraden."""
    s = Szene("hm1/k4folgen")
    s.welt()
    t1 = s.tr("pendel", "Pendelfolge a_n", "Oscillating sequence a_n", "Sucesión oscilante a_n", "振荡数列 a_n")
    t2 = s.tr("summe", "Summenfolge s_n", "Sum sequence s_n", "Sucesión de sumas s_n", "和数列 s_n")
    links = s.achsen((0, 13), (-1.5, 4), breite=2.6, hoehe=1.5, mitte=(-1.75, 0.7), xticks="1;5;10", yticks="-1;0;1;2;3", xl="n", xl_mitte=False, titel=t1)
    s.linie(links, (0, 2), (13, 2), farbe=GRAU, dicke=2, dash=DASH)
    glieder(s, links, [(n, a(n)) for n in range(1, 13)])
    rechts = s.achsen((-0.6, 12.4), (0.8, 2.2), breite=2.6, hoehe=1.5, mitte=(1.75, 0.7), xticks="0;5;10", yticks="1;1.5;2", xl="n", xl_mitte=False, titel=t2)
    s.linie(rechts, (-0.6, 2), (12.4, 2), farbe=GRAU, dicke=2, dash=DASH)
    glieder(s, rechts, [(n, s_(n)) for n in range(0, 12)], farbe=GRUEN)
    zahlengerade(s, -0.75, -3.05, 2.6, -1, 4, (-1, 0, 1, 2, 3), [a(n) for n in range(1, 13)])
    zahlengerade(s, -0.75, 0.45, 2.6, 0, 2, (0, 1, 2), [s_(n) for n in range(0, 12)], farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k4spiel():
    """Zwei Runden des Spiels für d_n = (-1)^n 3/n."""
    s = Szene("hm1/k4spiel")
    runden = (("r1", "Runde 1: ε = 0.5", "Round 1: ε = 0.5", "Ronda 1: ε = 0.5", "第 1 轮：ε = 0.5", 0.5, 6, -1.75),
              ("r2", "Runde 2: ε = 0.25", "Round 2: ε = 0.25", "Ronda 2: ε = 0.25", "第 2 轮：ε = 0.25", 0.25, 12, 1.75))
    for key, de, en, es, zh, eps, N, mitte in runden:
        t = s.tr(key, de, en, es, zh)
        b = s.achsen((0, 21), (-3.4, 2), breite=2.6, hoehe=2.0, mitte=(mitte, 0), xticks="1;5;10;15;20", yticks="-3;-2;-1;0;1", xl="n", xl_mitte=False, titel=t)
        s.band(b, 0, 21, -eps, eps, farbe=BLAU, deckung=0.2)
        s.linie(b, (0, 0), (21, 0), farbe=GRAU, dicke=2)
        s.linie(b, (N, -3.4), (N, 2), farbe=ROT, dicke=2.5, dash=DASH)
        s.text(b, "N_0 = %d" % N, (N + 0.5, 1.35), KLEIN, "left", ROT)
        s.text(b, "d_n", (-3.1, 1.8), KLEIN, "center")
        glieder(s, b, [(n, d(n)) for n in range(1, N + 1)], farbe=GRAU)
        glieder(s, b, [(n, d(n)) for n in range(N + 1, 21)])
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k4majorante():
    """b_n unter der Majorante 2/sqrt(n), mit gemeinsamem Schlauch."""
    s = Szene("hm1/k4majorante")
    b = s.achsen((0, 31), (0, 2.25), breite=5.4, hoehe=2.1, mitte=(-0.6, 0), xticks="1;5;10;15;20;25;30", yticks="0;0.5;1;1.5;2", xl="n", xl_mitte=False)
    s.band(b, 0, 31, 0, 0.5, farbe=BLAU, deckung=0.2)
    s.linie(b, (16, 0), (16, 2.25), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(b, "N_0 = 16", (16.4, 2.0), KLEIN, "left", ROT)
    s.text(b, "ε = 0.5", (31.5, 0.5), KLEIN, "left", BLAU)
    glieder(s, b, [(n, 2 / sqrt(n)) for n in range(1, 31)], farbe=ORANGE)
    glieder(s, b, [(n, sqrt(n + 4) - sqrt(n)) for n in range(1, 31)])
    t = s.tr("maj", "Majorante 2/√n", "Majorant 2/√n", "Mayorante 2/√n", "强数列 2/√n")
    s.text(b, t, (3.4, 1.62), KLEIN, "left", BRAUN)
    s.text(b, "b_n = √(n + 4) − √n", (1.0, 0.2), KLEIN, "left", BLAU)
    s.speichern()


def k4tempo():
    """n q^n und x^n/n!: Erst überwiegt der Anstieg, dann der Faktor kleiner 1."""
    s = Szene("hm1/k4tempo")
    links = s.achsen((0, 26), (0, 1.9), breite=2.6, hoehe=1.75, mitte=(-1.75, 0), xticks="1;5;10;15;20;25", yticks="0;0.5;1;1.5", xl="n", xl_mitte=False, titel="n · 0.8^n")
    s.linie(links, (4.5, 0), (4.5, 1.9), farbe=ROT, dicke=2.5, dash=DASH)
    glieder(s, links, [(n, n * 0.8 ** n) for n in range(1, 26)])
    rechts = s.achsen((0, 17), (0, 12), breite=2.6, hoehe=1.75, mitte=(1.75, 0), xticks="1;5;10;15", yticks="0;5;10", xl="n", xl_mitte=False, titel="4^n / n!")
    s.linie(rechts, (3.5, 0), (3.5, 12), farbe=ROT, dicke=2.5, dash=DASH)
    glieder(s, rechts, [(n, 4 ** n / factorial(n)) for n in range(1, 17)], farbe=GRUEN)
    s.text(links, s.tr("f1", "nächster Faktor\n0.8 (n+1)/n < 1", "next factor\n0.8 (n+1)/n < 1", "factor siguiente\n0.8 (n+1)/n < 1", "下一因子\n0.8 (n+1)/n < 1"),
           (9.5, 1.5), KLEIN, "left", ROT)
    s.text(rechts, s.tr("f2", "nächster Faktor\n4/(n+1) < 1", "next factor\n4/(n+1) < 1", "factor siguiente\n4/(n+1) < 1", "下一因子\n4/(n+1) < 1"),
           (6.3, 9.4), KLEIN, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k4schlauch():
    """Der Epsilon-Schlauch um a = 2 mit den Gliedern von a_n, eps = 0,5."""
    s = Szene("hm1/k4schlauch")
    b = s.achsen((0, 25), (-1.4, 4), breite=5.1, hoehe=2.75, mitte=(-0.95, 0), xticks="1;6;10;15;20;25", yticks="-1;0;1;2;3", xl="n", xl_mitte=False)
    s.band(b, 0, 25, 1.5, 2.5, farbe=BLAU, deckung=0.2)
    s.linie(b, (0, 2), (25, 2), farbe=SCHWARZ, dicke=2.5)
    s.linie(b, (6, -1.4), (6, 4), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(b, "N_0 = 6", (6.5, 3.65), KLEIN, "left", ROT)
    glieder(s, b, [(n, a(n)) for n in range(1, 7)], farbe=GRAU)
    glieder(s, b, [(n, a(n)) for n in range(7, 25)])
    s.text(b, "a + ε = 2.5", (25.6, 2.68), KLEIN, "left", BLAU)
    s.text(b, "a = 2", (25.6, 2.0), KLEIN, "left")
    s.text(b, "a − ε = 1.5", (25.6, 1.32), KLEIN, "left", BLAU)
    t = s.tr("drin", "ab n = 7 liegen alle\nGlieder im Schlauch", "from n = 7 on, all\nterms lie in the tube", "desde n = 7, todos los\ntérminos están en el tubo", "从 n = 7 起所有项\n都在管内")
    s.text(b, t, (9.5, 0.45), KLEIN, "left", BLAU)
    t = s.tr("drau", "bis n = 6: endlich viele\nGlieder, sie zählen nicht", "up to n = 6: finitely many\nterms, they do not count", "hasta n = 6: finitos términos,\nno cuentan", "到 n = 6 为止：有限多项，\n不计入")
    s.text(b, t, (9.5, -0.75), KLEIN, "left", GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k4produkt():
    """Produktregel als Fläche: a_n b_n - a b = (a_n - a) b_n + a (b_n - b)."""
    s = Szene("hm1/k4produkt")

    def recht(x0, y0, aa, bb, an, bn):
        s.box("", (x0 + aa / 2, y0 + bb / 2), breite=aa, hoehe=bb, farbe=BLAU, fuellung=HELLBLAU, dicke=2)
        s.box("", (x0 + aa / 2, y0 + bb + (bn - bb) / 2), breite=aa, hoehe=bn - bb, farbe=ORANGE, fuellung=HELLORANGE, dicke=2)
        s.box("", (x0 + aa + (an - aa) / 2, y0 + bn / 2), breite=an - aa, hoehe=bn, farbe=GRUEN, fuellung=HELLGRUEN, dicke=2)
        s.text(None, "a · b", (x0 + aa / 2, y0 + bb / 2), KLEIN, "center", BLAU)

    x0, y0 = -2.75, -0.8
    recht(x0, y0, 1.9, 1.05, 2.8, 1.7)
    s.text(None, "a (b_n − b)", (x0 + 0.95, y0 + 1.375), KLEIN, "center", BRAUN)
    s.text(None, "(a_n − a) b_n", (x0 + 2.35, y0 + 1.95), KLEIN, "center", GRUEN)
    s.text(None, "a", (x0 + 0.95, y0 - 0.24), KLEIN, "center")
    s.text(None, "a_n − a", (x0 + 2.35, y0 - 0.24), KLEIN, "center")
    s.text(None, "b", (x0 - 0.1, y0 + 0.525), KLEIN, "right")
    s.text(None, "b_n − b", (x0 - 0.1, y0 + 1.375), KLEIN, "right")
    recht(0.95, y0, 1.9, 1.05, 2.2, 1.25)
    t = s.tr("gross", "größeres n: Streifen schmaler", "larger n: narrower strips", "n mayor: franjas más estrechas", "n 更大：条带更窄")
    s.text(None, t, (2.0, y0 + 1.95), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k4sandwich():
    """n-te Wurzel aus n, eingeklemmt zwischen 1 und (1 + 1/sqrt n)^2."""
    s = Szene("hm1/k4sandwich")
    b = s.achsen((0, 41), (0.8, 3.1), breite=5.6, hoehe=2.05, mitte=(-0.2, 0), xticks="2;10;20;30;40", yticks="1;1.5;2;2.5;3", xl="n", xl_mitte=False)
    glieder(s, b, [(n, (1 + 1 / sqrt(n)) ** 2) for n in range(2, 41)], farbe=ORANGE, r=0.05)
    glieder(s, b, [(n, n ** (1 / n)) for n in range(2, 41)], r=0.05)
    glieder(s, b, [(n, 1) for n in range(2, 41)], farbe=GRUEN, r=0.05)
    s.text(b, "(1 + 1/√n)^2", (8, 2.35), KLEIN, "left", BRAUN)
    s.text(b, "ⁿ√n", (41.5, 1.1), KLEIN, "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k4monoton():
    """Links: s_n unter der Decke 2. Rechts: Heron-Folge, die in Q keinen Boden findet."""
    s = Szene("hm1/k4monoton")
    t1 = s.tr("mo1", "s_n steigt zur Decke 2", "s_n rises to the ceiling 2", "s_n sube hasta el techo 2", "s_n 升向上界 2")
    t2 = s.tr("mo2", "x_n fällt zur Lücke √2", "x_n falls to the gap √2", "x_n baja hasta el hueco √2", "x_n 降向空隙 √2")
    links = s.achsen((-0.5, 11), (0.9, 2.2), breite=2.6, hoehe=1.75, mitte=(-1.75, 0), xticks="0;3;5;10", yticks="1;1.5;2", xl="n", xl_mitte=False, titel=t1)
    s.band(links, -0.5, 11, 1.9, 2.0, farbe=ROT, deckung=0.2)
    s.linie(links, (-0.5, 2), (11, 2), farbe=ROT, dicke=3)
    s.linie(links, (3, 0.9), (3, 2.2), farbe=ROT, dicke=2.5, dash=DASH)
    glieder(s, links, [(n, s_(n)) for n in range(0, 11)], farbe=GRUEN)
    s.text(links, "N_0 = 3", (3.4, 1.18), KLEIN, "left", ROT)
    s.text(links, "ε = 0.1", (5.6, 1.62), KLEIN, "left", ROT)
    rechts = s.achsen((0.4, 7), (1.25, 2.1), breite=2.5, hoehe=1.75, mitte=(1.75, 0), xticks="1;2;3;4;5;6", yticks="1.5;2", xl="n", xl_mitte=False, titel=t2)
    s.linie(rechts, (0.4, sqrt(2)), (7, sqrt(2)), farbe=ROT, dicke=2.5, dash=DASH)
    h = [2.0]
    for _ in range(5):
        h.append((h[-1] + 2 / h[-1]) / 2)
    glieder(s, rechts, [(k + 1, h[k]) for k in range(6)])
    s.text(rechts, s.tr("loch", "√2 fehlt in ℚ", "√2 is missing in ℚ", "√2 falta en ℚ", "√2 不在 ℚ 中"), (2.9, 1.62), KLEIN, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k4trichter():
    """a_n mit oberer und unterer Hülle b_n und c_n."""
    s = Szene("hm1/k4trichter")
    b = s.achsen((0, 31), (-1.4, 4), breite=5.3, hoehe=2.0, mitte=(-0.3, 0), xticks="1;5;10;15;20;25;30", yticks="-1;0;1;2;3", xl="n", xl_mitte=False)
    N = range(1, 31)

    def ob(n):
        m = n if n % 2 == 0 else n + 1
        return 2 + 3 / m

    def un(n):
        m = n if n % 2 == 1 else n + 1
        return 2 - 3 / m
    s.daten(b, [(n, ob(n)) for n in N], farbe=ORANGE, dicke=3.5, treppe="post")
    s.daten(b, [(n, un(n)) for n in N], farbe=GRUEN, dicke=3.5, treppe="post")
    s.linie(b, (0, 2), (31, 2), farbe=GRAU, dicke=2, dash=DASH)
    glieder(s, b, [(n, a(n)) for n in N])
    s.text(b, "b_n", (5.5, 3.1), KLEIN, "left", BRAUN)
    s.text(b, "c_n", (5.5, 0.7), KLEIN, "left", GRUEN)
    s.text(b, "a_n", (31.5, 2.0), KLEIN, "left", BLAU)
    s.speichern()


for f in (k4folgen, k4spiel, k4majorante, k4tempo, k4schlauch, k4produkt, k4sandwich, k4monoton, k4trichter):
    f()
