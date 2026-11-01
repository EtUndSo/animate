"""ET3 Teil 1 (kap1_stufen.tex): die neun Abbildungen der Faltung als Editor-Szenen.

Aufruf: python tools/szenen/et3_teil1.py, danach python tools/szenen_ansehen.py out.png et3/k1elementar ... [--lang de]
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")

HELLBLAU_40 = "#aac9ef"    # elblue!40 im Heft
HELLBLAU_50 = "#94bbea"    # elblue!50
HELLBLAU_70 = "#6aa1e2"    # elblue!70
TREPPE_TEXT = "#5a94dc"    # Beschriftung der Treppe: etwas dunkler als die Linie, sonst zu blass
HELLROT = "#e49494"        # holered!50 (holered!40 aus dem Heft ist am Schirm kaum zu sehen)
ORANGE_DUNKEL = "#bc5329"  # minor!80!black
GRUEN_DUNKEL = "#005b2a"   # vecgreen!70!black


def grect(arg="x"):
    """Antwort des RC-Glieds (RC = 1 s) auf das Rechteck der Dauer 1 s, wie grect im Kopf von kap1_stufen.tex."""
    return f"where(({arg})<0,0,where(({arg})<=1,1-exp(-({arg})),(e-1)*exp(-({arg}))))"


def t_in_s(s):
    return s.tr("t_in_s", "t in s", "t in s", "t en s", "t / s")


def k1elementar():
    """Sechs Elementarsignale, 3 x 2 Felder wie im Heft (die Bildunterschrift sagt „unten rechts“). Im Heft stehen einige Tick-Zahlen
    auf den Kurven; hier rücken sie neben die Kurve, die Striche bleiben an der Achse."""
    s = Szene("et3/k1elementar")
    B, H, WS, WZ = 1.85, 1.15, 2.38, 2.25
    feld = [("sin(2πt)", -1.2, 1.4, -1.25, "-1;1", "-1;1"),
            ("e^{−πt^2}", -2, 2.2, -0.3, "-2;-1;1;2", "0.5;1"),
            ("ε(t)", -1.5, 2, -0.3, "-1;1", "0.5;1"),
            ("rect(t)", -1.5, 1.7, -0.3, "-1;1", "0.5;1"),
            ("Λ(t)", -1.6, 1.8, -0.3, "-1;1", "0.5;1"),
            ("0.8 rect((t − 2)/2)", -0.5, 4.2, -0.3, "1;2;3", "0.5;1")]
    frei_x, frei_y = {0}, {0, 1, 3, 4}         # Teilbilder, deren Zahlen von Hand neben die Kurve rücken
    ax = []
    for k, (titel, x0, x1, y0, xt, yt) in enumerate(feld):
        a = s.achsen((x0, x1), (y0, 1.35), breite=B, hoehe=H, mitte=((k % 3 - 1) * WS - 0.14, 1.05 - WZ * (k // 3)), titel=titel, titel_mitte=True, kreuz=True,
                     xticks=xt, yticks=yt, label=26, zahl=22, xzahlen=k not in frei_x, yzahlen=k not in frei_y)
        s.text(a, "t", (x1 + 0.17 * (x1 - x0) / B, 0.2 * (1.35 - y0) / H), groesse=24, ausrichtung="center")
        ax.append(a)
    z = dict(groesse=22, ausrichtung="right")
    # sin: rechts von jedem Tick liegt die Kurve oberhalb der Achse, darunter ist Platz
    s.text(ax[0], "−1", (-0.97, -0.72), groesse=22)
    s.text(ax[0], "1", (1.03, -0.72), groesse=22)
    s.text(ax[0], "1", (-0.19, 1), **z)
    s.text(ax[0], "−1", (0.19, -1), groesse=22)
    # Gauß, rect, Λ: 0,5 (und bei rect die 1) links der Kurve
    s.text(ax[1], "0.5", (-0.68, 0.5), **z)
    s.text(ax[1], "1", (-0.5, 1), **z)
    s.text(ax[3], "0.5", (-0.6, 0.5), **z)
    s.text(ax[3], "1", (-0.6, 1), **z)
    s.text(ax[4], "0.5", (-0.72, 0.5), **z)
    s.text(ax[4], "1", (-0.4, 1), **z)
    s.kurve(ax[0], "sin(2*pi*x)", x=(-1.2, 1.2), dicke=4)
    s.kurve(ax[1], "exp(-pi*x^2)", x=(-2, 2), dicke=4)
    s.kurve(ax[2], "0", x=(-1.5, 0), dicke=4)
    s.kurve(ax[2], "1", x=(0, 1.8), dicke=4)
    s.punkt(ax[2], 0, 1, farbe=BLAU, r=0.055)
    s.kurve(ax[3], "rect(x)", x=(-1.5, 1.5), dicke=4)
    s.kurve(ax[4], "tri(x)", x=(-1.5, 1.5), dicke=4)
    s.linie(ax[5], (2, 0), (2, 1.1), farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(ax[5], "0.8*rect((x-2)/2)", x=(-0.5, 4), farbe=ROT, dicke=4)
    s.speichern()


def k1rcschaltung():
    """RC-Tiefpass, Maße wie im Heft (x, y aus dem tikz-Bild) mal k."""
    s = Szene("et3/k1rcschaltung")
    k = 1.4

    def p(x, y):
        return ((x - 2.0) * k, (y - 1.0) * k)

    s.draht(p(0, 2), p(1, 2))
    s.bauteil("resistor", p(1.6, 2), laenge=1.2 * k, label="", size=k)
    s.text(None, "R", p(1.6, 2), ausrichtung="center")
    s.draht(p(2.2, 2), p(3.6, 2))
    s.bauteil("capacitor", p(3, 1), drehung=270, laenge=2 * k, label="C", size=1.55)
    s.draht(p(0.5, 0), p(3.6, 0))
    for x, y in ((0.5, 2), (0.5, 0), (3.6, 2), (3.6, 0), (3, 2), (3, 0)):
        s.punkt(None, *p(x, y), r=0.07)
    s.pfeil(p(0.3, 1.8), p(0.3, 0.2), "u_1(t)", farbe=BLAU, label_seite="right", spitze=0.2)
    s.pfeil(p(3.9, 1.8), p(3.9, 0.2), "u_2(t)", farbe=ROT, spitze=0.2)
    s.speichern()


def k1bode():
    """Betrag und Phase über x = 2πFRC, logarithmisch, Punkte bei x = 1."""
    s = Szene("et3/k1bode")
    xl = "x = 2πFRC"
    a = s.achsen((0.01, 100), (0, 1.05), breite=2.75, hoehe=2.0, mitte=(-1.6, 0), xl=xl, yl="|H|", xlog=True, gitter=True, rahmen=True, yticks="0;0.5;1")
    s.kurve(a, "1/sqrt(1+x^2)", x=(0.01, 100), farbe=BLAU, dicke=4)
    s.punkt(a, 1, 0.7071, r=0.065)
    s.text(a, "0.707", (1.25, 0.8), groesse=24)
    phi = s.tr("phi_grad", "φ in Grad", "φ in degrees", "φ en grados", "φ / °")
    b = s.achsen((0.01, 100), (-95, 5), breite=2.75, hoehe=2.0, mitte=(1.9, 0), xl=xl, yl=phi, xlog=True, gitter=True, rahmen=True, yticks="-90;-45;0")
    s.kurve(b, "-arctan(x)*180/pi", x=(0.01, 100), farbe=ROT, dicke=4)
    s.punkt(b, 1, -45, r=0.065)
    s.speichern()


def k1doppel():
    """Links Rechteck und RC-Antwort, rechts Doppelimpuls mit den beiden Teilantworten (gestrichelt)."""
    s = Szene("et3/k1doppel")
    gem = dict(breite=2.75, hoehe=1.9, xl=t_in_s(s), gitter=True, rahmen=True, xticks="0;2;4;6", yticks="0;0.5;1", titel_mitte=True)
    a = s.achsen((-0.5, 6), (-0.05, 1.15), mitte=(-1.6, 0), titel=s.tr("ein_rechteck", "ein Rechteck", "one rectangle", "un rectángulo", "单个矩形"), **gem)
    s.kurve(a, "rect(x-0.5)", dicke=4)
    s.kurve(a, grect(), farbe=ROT, dicke=4)
    s.text(a, "s_0", (1.1, 1.0), groesse=24, farbe=BLAU)
    s.text(a, "g_0", (1.6, 0.45), groesse=24, farbe=ROT)
    b = s.achsen((-0.5, 6), (-0.05, 1.15), mitte=(1.75, 0), titel="s_0(t) + 0.5 s_0(t − 2)", **gem)
    s.kurve(b, "rect(x-0.5)+0.5*rect(x-2.5)", dicke=4)
    s.kurve(b, grect(), farbe=HELLROT, dicke=3, dash=DASH)
    s.kurve(b, "0.5*" + grect("x-2"), farbe=HELLROT, dicke=3, dash=DASH)
    s.kurve(b, grect() + "+0.5*" + grect("x-2"), farbe=ROT, dicke=4)
    s.speichern()


def k1treppe():
    """Oben Dreieck und Treppe, unten exakte und genäherte RC-Antwort. s und Treppe als Formel, g und g_a aus den Daten."""
    s = Szene("et3/k1treppe")
    gem = dict(breite=6.05, hoehe=1.55, gitter=True, rahmen=True, label=26, zahl=22)
    a = s.achsen((-0.5, 5, 0.5), (-0.05, 1.15), mitte=(0.2, 1.42), yl=s.tr("eingang", "Eingang", "Input", "Entrada", "输入"), yticks="0;0.5;1", **gem)
    s.kurve(a, "tri(x-1)", dicke=4)
    s.kurve(a, "tri(0.5*floor(x/0.5)-1)", farbe=HELLBLAU_50, dicke=4)
    s.text(a, "s(t)", (0.33, 0.8), groesse=24, farbe=BLAU, ausrichtung="right")
    s.text(a, s.tr("treppe", "Treppe, T_0 = 0.5 s", "staircase, T_0 = 0.5 s", "escalera, T_0 = 0.5 s", "阶梯近似，T_0 = 0.5 s"), (1.62, 0.85), groesse=24,
           farbe=TREPPE_TEXT)
    b = s.achsen((-0.5, 5, 0.5), (-0.02, 0.62), mitte=(0.2, -1.1), yl=s.tr("ausgang", "Ausgang", "Output", "Salida", "输出"), xl=t_in_s(s), yticks="0;0.2;0.4;0.6", **gem)
    p05, p01 = DAT / "k1_treppe_0.5.dat", DAT / "k1_treppe_0.1.dat"
    s.daten(b, duenn(daten(p05, 1, 4), 3e-4), farbe=ROT, dicke=5)
    s.daten(b, duenn(daten(p05, 1, 5), 3e-4), farbe=ORANGE, dicke=3, dash=DASH)
    s.daten(b, duenn(daten(p01, 1, 5), 3e-4), farbe=GRUEN_DUNKEL, dicke=3, dash=DASH)
    s.tr("g_exakt", "g(t) exakt", "g(t) exact", "g(t) exacta", "g(t)（精确）")
    s.tr("ga05", "g_a, T_0 = 0.5 s", "g_a, T_0 = 0.5 s", "g_a, T_0 = 0.5 s", "g_a，T_0 = 0.5 s")
    s.tr("ga01", "g_a, T_0 = 0.1 s", "g_a, T_0 = 0.1 s", "g_a, T_0 = 0.1 s", "g_a，T_0 = 0.1 s")
    # Legende statt Direktbeschriftung: Die drei Kurven liegen fast aufeinander. Mehrere Einträge brauchen die Form @{schluessel}.
    leg = [("@{g_exakt}", ROT, "-"), ("@{ga05}", ORANGE, "--"), ("@{ga01}", GRUEN_DUNKEL, "--")]
    s.legende(b, leg, (3.05, 0.55), zeile=0.31, groesse=24)
    s.speichern()


def k1schieben():
    """Grafische Faltung bei t = 0.5 s und 2 s mit der Fläche, rechts das Ergebnis."""
    s = Szene("et3/k1schieben")
    gem = dict(breite=1.7, hoehe=1.75, gitter=True, rahmen=True, titel_mitte=True, zahl=22, label=24)
    ws, dx = 2.38, 0.24
    a = s.achsen((-2.5, 2.5), (-0.05, 1.2), mitte=(dx - ws, 0), titel="t = 0.5 s", xl="τ", xticks="-2;0;2", yticks="0;0.5;1", **gem)
    s.flaeche(a, "exp(-(0.5-x))", 0, 0.5, farbe=ORANGE, deckung=0.35)
    s.kurve(a, "rect(x-0.5)", dicke=4)
    s.kurve(a, "exp(-(0.5-x))*epsilon(0.5-x)", farbe=ROT, dicke=4)
    b = s.achsen((-1.5, 3.5), (-0.05, 1.2), mitte=(dx, 0), titel="t = 2 s", xl="τ", xticks="0;2", yticks="0;0.5;1", **gem)
    s.flaeche(b, "exp(-(2-x))", 0, 1, farbe=ORANGE, deckung=0.35)
    s.kurve(b, "rect(x-0.5)", dicke=4)
    s.kurve(b, "exp(-(2-x))*epsilon(2-x)", farbe=ROT, dicke=4)
    c = s.achsen((-0.5, 4.5), (-0.05, 0.75), mitte=(dx + ws, 0), titel=s.tr("ergebnis", "Ergebnis g(t)", "Result g(t)", "resultado g(t)", "结果 g(t)"), xl="t",
                 xticks="0;2;4", yticks="0;0.2;0.4;0.6", **gem)
    s.kurve(c, grect(), farbe=ORANGE_DUNKEL, dicke=4)
    s.punkt(c, 0.5, 0.3935, r=0.065)
    s.punkt(c, 2, 0.2325, r=0.065)
    s.speichern()


def k1bloecke():
    """Oben Kettenschaltung, unten Parallelschaltung; rechts jeweils das gleichwertige Einzelsystem."""
    s = Szene("et3/k1bloecke")
    B, H, ko = 0.76, 0.46, 0.16
    y1, y2 = 1.05, -0.45

    def kasten(t, x, y, w=B):
        s.box(t, (x, y), breite=w, hoehe=H, groesse=26)

    def pf(a, b, knick="none"):
        s.pfeil(a, b, knick=knick, spitze=ko)

    def rechts(y, inhalt):
        s.text(None, "=", (0.26, y), groesse=28, ausrichtung="center")
        s.text(None, "s", (0.82, y), ausrichtung="center")
        pf((0.94, y), (1.38, y))
        kasten(inhalt, 2.03, y, w=1.3)
        pf((2.68, y), (3.12, y))
        s.text(None, "g", (3.24, y), ausrichtung="center")

    # Kette
    s.text(None, "s", (-3.38, y1), ausrichtung="center")
    pf((-3.26, y1), (-2.82, y1))
    kasten("h_1", -2.44, y1)
    pf((-2.06, y1), (-1.62, y1))
    kasten("h_2", -1.24, y1)
    pf((-0.86, y1), (-0.42, y1))
    s.text(None, "g", (-0.3, y1), ausrichtung="center")
    rechts(y1, "h_1 ∗ h_2")
    # Parallel
    v = (-2.9, y2)
    s.text(None, "s", (-3.38, y2), ausrichtung="center")
    s.linie(None, (-3.26, y2), v)
    s.punkt(None, *v, r=0.055)
    yo, yu = y2 + 0.42, y2 - 0.42
    kasten("h_1", -1.95, yo)
    kasten("h_2", -1.95, yu)
    pf(v, (-2.33, yo), "vh")
    pf(v, (-2.33, yu), "vh")
    xs = -1.0
    s.box("+", (xs, y2), breite=0.3, hoehe=0.3, form="ellipse", groesse=26)
    pf((-1.57, yo), (xs, y2 + 0.21), "hv")
    pf((-1.57, yu), (xs, y2 - 0.21), "hv")
    pf((xs + 0.195, y2), (-0.42, y2))
    s.text(None, "g", (-0.3, y2), ausrichtung="center")
    rechts(y2, "h_1 + h_2")
    s.speichern()


def k1dirac():
    """Links Rechtecke der Fläche 1 (immer schmaler), rechts das Symbol des Grenzobjekts. Die Höhen stehen neben den Rechteckecken:
    Direkt an der Achse lägen sie auf den waagerechten Rechteckkanten."""
    s = Szene("et3/k1dirac")
    a = s.achsen((-1.2, 1.2), (0, 4.6), breite=3.2, hoehe=2.7, mitte=(-1.7, 0), kreuz=True, xl="t", xticks="-0.5;0.5", yticks="1;2;4", yzahlen=False)
    s.kurve(a, "rect(x)", x=(-1.2, 1.2), farbe=HELLBLAU_40, dicke=4)
    s.kurve(a, "2*rect(2*x)", x=(-0.2501, 0.2501), farbe=HELLBLAU_70, dicke=4)
    s.kurve(a, "4*rect(4*x)", x=(-0.1251, 0.1251), farbe=BLAU, dicke=4)
    for y, x in ((1, -0.54), (2, -0.29), (4, -0.165)):
        s.text(a, str(y), (x, y), groesse=24, ausrichtung="right")
    s.text(a, "T_0 = 1", (0.53, 1.2), groesse=24)
    s.text(a, "T_0 = 0.5", (0.29, 2.2), groesse=24)
    s.text(a, "T_0 = 0.25", (0.16, 4.2), groesse=24)
    b = s.achsen((-1.2, 2.2), (0, 2.4), breite=2.2, hoehe=2.7, mitte=(1.8, 0), kreuz=True, xl="t", xticks="1.5", ymarks=False, yzahlen=False)
    s.stems(b, [0], [1], pfeile=True, farbe=BLAU)
    s.text(b, "δ(t)", (0.1, 1.0), groesse=24, farbe=BLAU)
    s.stems(b, [1.5], [2], pfeile=True, farbe=ROT)
    s.text(b, "2δ(t − 1.5)", (1.6, 2.0), groesse=24, farbe=ROT)
    s.speichern()


def k1wuerfel():
    """Verteilung der Augensumme bei 1, 2 und 3 Würfeln; in allen Teilbildern gleich breite Balken."""
    s = Szene("et3/k1wuerfel")
    B, ws, dx = 1.68, 2.33, 0.27
    xl = s.tr("augensumme", "Augensumme k", "sum of the dice k", "suma de los dados k", "骰子点数之和 k")
    feld = [(0, 7, "1;2;3;4;5;6", 2, BLAU, s.tr("w1", "ein Würfel", "one die", "un dado", "一个骰子")),
            (1, 13, "2;7;12", 3, ROT, s.tr("w2", "zwei Würfel", "two dice", "dos dados", "两个骰子")),
            (2, 19, "3;10;18", 4, GRUEN_DUNKEL, s.tr("w3", "drei Würfel", "three dice", "tres dados", "三个骰子"))]
    for i, (x0, x1, xt, spalte, farbe, titel) in enumerate(feld):
        a = s.achsen((x0, x1), (0, 0.2), breite=B, hoehe=1.75, mitte=(dx + ws * (i - 1), 0), titel=titel, titel_mitte=True, xl=xl, xticks=xt, yticks="0;0.05;0.1;0.15",
                     rahmen=True, zahl=22, label=24)
        pts = [(k, p) for k, p in daten(DAT / "k1_wuerfel.dat", 1, spalte) if x0 < k < x1 and p > 0]
        s.stems(a, [k for k, _ in pts], [p for _, p in pts], farbe=farbe, breite=0.075 * (x1 - x0) / B)
    s.speichern()


for f in (k1elementar, k1rcschaltung, k1bode, k1doppel, k1treppe, k1schieben, k1bloecke, k1dirac, k1wuerfel):
    f()
