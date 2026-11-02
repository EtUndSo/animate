"""HM1 Teil 1 (C:/Bücher/HöMa1/Arbeitshefte/kap1_stufen.tex): Mengen, Logik und reelle Zahlen.

Aufruf: python tools/szenen/hm1_teil1.py, danach python tools/szenen_ansehen.py out.png hm1/k1venn ... [--lang de]
Zahlen und Punkte stammen aus dem Rechenmodell des Hefts (rechnung_kap1.py).
"""
import sys
from math import sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22                 # Untergrenze
MITTEL = 24
HELLBLAU, HELLROT, HELLGRUEN, HELLGRAU_F = "#dceafa", "#f6dede", "#dcefe3", "#ececec"


def minus(v):
    return ("%g" % v).replace("-", "−")


# ------------------------------------------------------------------------------------------ Stufe 1
def k1venn():
    """Links die Elemente von G in den vier Bereichen, rechts das Komplement des Durchschnitts."""
    s = Szene("hm1/k1venn")
    s.welt()
    h, w = 0.86, 1.65                            # halbe Höhe und Breite des Rechtecks
    r, d = 0.64, 0.38                           # Kreisradius, halber Mittenabstand
    ym = 0.02                                   # Höhe der Kreismitten

    def rahmen(mx, fuellung=None):
        if fuellung:
            s.band(None, mx - w, mx + w, -h, h, farbe=fuellung, deckung=1.0)
        for a, b in (((-w, -h), (w, -h)), ((w, -h), (w, h)), ((w, h), (-w, h)), ((-w, h), (-w, -h))):
            s.linie(None, (mx + a[0], a[1]), (mx + b[0], b[1]), farbe=GRAU, dicke=2.5)

    def namen(mx):
        s.text(None, "G", (mx - w + 0.14, h - 0.18), MITTEL, "center", GRAU)
        s.text(None, "A", (mx - d - 0.56, 0.6), MITTEL, "center", BLAU)
        s.text(None, "B", (mx + d + 0.56, 0.6), MITTEL, "center", ROT)

    # links: Elemente
    mx = -1.75
    rahmen(mx)
    s.kreis(None, mx - d, ym, r, farbe=BLAU, dicke=3)
    s.kreis(None, mx + d, ym, r, farbe=ROT, dicke=3)
    namen(mx)
    s.text(None, "1   4\n6  12", (mx - d - 0.3, ym), KLEIN, "center", BLAU)
    s.text(None, "2\n3", (mx, ym), KLEIN, "center", SCHWARZ)
    s.text(None, "5   7\n11", (mx + d + 0.3, ym), KLEIN, "center", ROT)
    s.text(None, "8   9   10", (mx, -0.74), KLEIN, "center", GRAU)

    # rechts: (A ∩ B)^c ist alles außer der Linse. Die Linse liegt weiß über der Fläche, in eigenen Achsen 1:1.
    mx = 1.75
    rahmen(mx, HELLBLAU)
    a = s.achsen((-1.65, 1.65), (-0.86, 0.86), breite=3.3, hoehe=1.72, mitte=(mx, 0), unsichtbar=True, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    wur = "sqrt(max(0,%g-(x%+g)^2))" % (r * r, d)
    wur2 = "sqrt(max(0,%g-(x%+g)^2))" % (r * r, -d)
    s.flaeche(a, "min(%s,%s)+%g" % (wur, wur2, ym), -(r - d), r - d, f2="-min(%s,%s)+%g" % (wur, wur2, ym), farbe="#ffffff", deckung=1.0)
    s.kreis(None, mx - d, ym, r, farbe=BLAU, dicke=3)
    s.kreis(None, mx + d, ym, r, farbe=ROT, dicke=3)
    namen(mx)
    s.text(None, "A ∩ B", (mx, ym), KLEIN, "center")
    s.text(None, "(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ", (mx, -0.74), KLEIN, "center", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k1quantoren():
    """Geräte und Sicherungen: links für jedes Gerät eine Sicherung, rechts eine Sicherung für alle."""
    s = Szene("hm1/k1quantoren")
    dy = 0.5

    def panel(mx, ziele, titel, farbe):
        xg, xs = mx - 1.05, mx + 1.05
        for k in range(3):
            y = dy - dy * k
            s.box("g%d" % (k + 1), (xg, y), breite=0.72, hoehe=0.4, form="round", groesse=MITTEL, dicke=2.5, fuellung=HELLBLAU)
            s.box("s%d" % (k + 1), (xs, y), breite=0.72, hoehe=0.4, form="round", groesse=MITTEL, dicke=2.5, fuellung=HELLGRAU_F)
            yz = dy - dy * ziele[k]
            s.pfeil((xg + 0.36, y), (xs - 0.4, yz), "", farbe=farbe, spitze=0.17, dicke=3)
        s.text(None, titel, (mx, 0.95), MITTEL, "center", farbe)
    panel(-1.75, (1, 2, 0), s.tr("t1", "∀g ∃s: jedes Gerät eine Sicherung", "∀g ∃s: each device has a fuse", "∀g ∃s: cada aparato, un fusible", "∀g ∃s：每台设备都有一个保险丝"), BLAU)
    panel(1.75, (1, 1, 1), s.tr("t2", "∃s ∀g: eine Sicherung für alle", "∃s ∀g: one fuse for all", "∃s ∀g: un fusible para todos", "∃s ∀g：一个保险丝供全部"), ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k1zahlbereiche():
    """Vier ineinanderliegende Zahlbereiche. In jedem Ring die Gleichung, die erst dort lösbar ist."""
    s = Szene("hm1/k1zahlbereiche")
    #          links  rechts  halbe Höhe  Füllung
    ringe = ((-3.5, 3.45, 0.66, HELLGRAU_F), (-3.37, 1.72, 0.54, HELLBLAU), (-3.24, -0.2, 0.42, HELLGRUEN), (-3.11, -1.95, 0.3, "#ffffff"))
    for li, re, hh, f in ringe:
        s.box("", (0.5 * (li + re), 0), breite=re - li, hoehe=2 * hh, form="round", dicke=2.5, fuellung=f)
    s.text(None, "ℕ", (-2.52, 0.0), 30, "center")
    for x, name, gl, f in ((-1.08, "ℤ", "x + 3 = 1\nx = −2", GRUEN), (0.76, "ℚ", "3x = 1\nx = 1/3", BLAU), (2.64, "ℝ", "x² = 2\nx = √2", SCHWARZ)):
        s.text(None, name, (x - 0.58, 0.0), 30, "center", f)
        s.text(None, gl, (x + 0.2, 0.0), MITTEL, "center", f)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k1spiegel():
    """x = -3 < y = 2: Mal 2 bleibt die Reihenfolge, mal -1 dreht sie sich."""
    s = Szene("hm1/k1spiegel")
    s.welt()
    sk, mx = 0.31, -1.3
    ys = (0.62, 0.0, -0.62)
    tit = ("x = −3 < y = 2",
           s.tr("z2", "mal 2: Reihenfolge bleibt", "times 2: order stays", "por 2: el orden se mantiene", "乘 2：顺序不变"),
           s.tr("z1", "mal −1: Reihenfolge dreht sich", "times −1: order flips", "por −1: el orden se invierte", "乘 −1：顺序反转"))
    for yy, t, (a, b) in zip(ys, tit, ((-3, 2), (-6, 4), (3, -2))):
        s.pfeil((mx - 7 * sk, yy), (mx + 7 * sk, yy), "", farbe=GRAU, spitze=0.16, dicke=2.5)
        s.linie(None, (mx, yy - 0.08), (mx, yy + 0.08), farbe=GRAU, dicke=2.5)
        s.text(None, "0", (mx, yy - 0.25), KLEIN, "center", GRAU)
        s.punkt(None, mx + sk * a, yy, farbe=BLAU, r=0.09)
        s.punkt(None, mx + sk * b, yy, farbe=ROT, r=0.09)
        s.text(None, minus(a), (mx + sk * a, yy + 0.25), MITTEL, "center", BLAU)
        s.text(None, minus(b), (mx + sk * b, yy + 0.25), MITTEL, "center", ROT)
        s.text(None, t, (1.05, yy + 0.02), MITTEL, "left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k1induktion():
    """Links 1 + 3 + 5 + 7 = 4^2 als Winkelstücke, rechts der Induktionsschritt: n^2 + 2n + 1 = (n+1)^2."""
    s = Szene("hm1/k1induktion")
    a, x0, y0 = 0.28, -3.3, -0.6
    farben = (BLAU, GRUEN, ORANGE, ROT)
    for i in range(4):
        for j in range(4):
            s.box("", (x0 + a * (i + 0.5), y0 + a * (j + 0.5)), breite=a, hoehe=a, dicke=2, fuellung=farben[max(i, j)], deckung=0.3, farbe=GRAU)
    s.text(None, "1 + 3 + 5 + 7 = 4²", (x0 + 2 * a, y0 - 0.28), MITTEL, "center")
    for k, t in enumerate(("1", "3", "5", "7")):
        s.text(None, t, (x0 + a * (k + 0.5), y0 + a * 4 + 0.2), MITTEL, "center", farben[k])

    x1, y1 = -0.85, -0.6
    n, st = 0.86, 0.28
    s.box("n²", (x1 + n / 2, y1 + n / 2), breite=n, hoehe=n, dicke=2.5, fuellung=BLAU, deckung=0.2, farbe=BLAU, groesse=26)
    s.box("n", (x1 + n + st / 2, y1 + n / 2), breite=st, hoehe=n, dicke=2.5, fuellung=ROT, deckung=0.2, farbe=ROT, groesse=MITTEL)
    s.box("n", (x1 + n / 2, y1 + n + st / 2), breite=n, hoehe=st, dicke=2.5, fuellung=ROT, deckung=0.2, farbe=ROT, groesse=MITTEL)
    s.box("1", (x1 + n + st / 2, y1 + n + st / 2), breite=st, hoehe=st, dicke=2.5, fuellung=ORANGE, deckung=0.3, farbe=ORANGE, groesse=MITTEL)
    s.text(None, "n² + (2n + 1) = (n + 1)²", (x1 + 0.6, y1 - 0.28), MITTEL, "center")
    s.text(None, s.tr("schritt", "Schritt: das nächste\nWinkelstück anlegen", "Step: attach the\nnext L-shaped piece", "Paso: añadir la\nsiguiente pieza en L", "归纳步骤：\n再加一层 L 形"),
           (x1 + n + st + 0.45, y1 + 0.6), MITTEL, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k1luecke():
    """Brüche links und rechts von der Stelle, an der x^2 = 2 wäre."""
    s = Szene("hm1/k1luecke")
    x0, x1, y0, y1 = 1.2, 1.7, 0.9, 2.75
    br, ho = 5.2, 1.4
    a = s.achsen((x0, x1), (y0, y1), breite=br, hoehe=ho, mitte=(0, 0), xl="x", xl_mitte=False, yl="x²", xticks="1.2;1.3;1.4;1.5;1.6;1.7", yticks="1;1.5;2;2.5")
    r2 = sqrt(2)
    s.kurve(a, "x^2", farbe=GRAU, dicke=3)
    s.linie(a, (x0, 2), (x1, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (r2, y0), (r2, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.band(a, x0, r2 - 0.002, y0, 1.0, farbe=BLAU, deckung=0.3)
    s.band(a, r2 + 0.002, x1, y0, 1.0, farbe=ROT, deckung=0.25)
    for p in (1.25, 1.3, 1.35, 1.4, 1.41, 1.414):
        s.punkt(a, p, 0.95, farbe=BLAU, r=0.05)
    for p in (1.415, 1.42, 1.45, 1.5, 1.55, 1.6, 1.65):
        s.punkt(a, p, 0.95, farbe=ROT, r=0.05)
    # runder Ring: in den Datenachsen hat er verschiedene Halbachsen
    rx, ry = 0.085 * (x1 - x0) / br, 0.085 * (y1 - y0) / ho
    s.punkt(a, r2, 2, farbe="#ffffff", r=0.085)
    s.weg(a, "%.6f+%.6f*cos(t)" % (r2, rx), "2+%.6f*sin(t)" % ry, 0, 6.2832, farbe=SCHWARZ, dicke=3, n=61)
    s.text(a, s.tr("d", "D: Brüche mit x² < 2", "D: fractions with x² < 2", "D: fracciones con x² < 2", "D：x² < 2 的分数"), (1.21, 1.14), MITTEL, "left", BLAU)
    s.text(a, s.tr("ob", "Brüche mit x² > 2:\nobere Schranken von D", "fractions with x² > 2:\nupper bounds of D", "fracciones con x² > 2:\ncotas superiores de D", "x² > 2 的分数：\nD 的上界"), (1.695, 1.33), MITTEL, "right", ROT)
    s.text(a, s.tr("loch", "kein Bruch trifft\ndiese Stelle", "no fraction hits\nthis point", "ninguna fracción\nllega aquí", "没有分数\n落在此处"), (1.3, 2.42), MITTEL, "center")
    s.pfeil((1.355, 2.33), (1.405, 2.09), "", farbe=SCHWARZ, spitze=0.14, dicke=2, on=a)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k1schachtelung():
    """Halbierung für x^2 = 2: sechs Intervalle aus rechnung_kap1.py."""
    s = Szene("hm1/k1schachtelung")
    iv = [(1, 2), (1, 1.5), (1.25, 1.5), (1.375, 1.5), (1.375, 1.4375), (1.40625, 1.4375)]
    a = s.achsen((1, 2), (0.4, 6.6), breite=4.4, hoehe=1.5, mitte=(-0.85, 0), xl="", xticks="1;1.25;1.5;1.75;2", yticks="", yzahlen=False, ymarks=False)
    r2 = sqrt(2)
    s.linie(a, (r2, 0.4), (r2, 6.6), farbe=GRAU, dicke=2, dash=DASH)
    for k, (u, o) in enumerate(iv):
        y = 6 - k
        s.linie(a, (u, y), (o, y), farbe=BLAU, dicke=5)
        s.linie(a, (u, y - 0.28), (u, y + 0.28), farbe=BLAU, dicke=3)
        s.linie(a, (o, y - 0.28), (o, y + 0.28), farbe=ROT, dicke=3)
        s.text(a, "n = %d" % (k + 1), (0.985, y), KLEIN, "right")
        s.text(a, "[%g; %g]" % (u, o), (2.03, y), KLEIN, "left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k1betrag():
    """x = -3 und y = 5: direkter Abstand 8, Umweg über z = 7 ergibt 12."""
    s = Szene("hm1/k1betrag")
    s.welt()
    sk = 0.46

    def px(v):
        return (v - 2) * sk

    y = -0.3
    s.pfeil((px(-5), y), (px(9), y), "", farbe=GRAU, spitze=0.17, dicke=2.5)
    for m in (-3, 0, 1, 5, 7):
        s.linie(None, (px(m), y - 0.08), (px(m), y + 0.08), farbe=GRAU, dicke=2.5)
        s.text(None, minus(m), (px(m), y - 0.3), KLEIN, "center", GRAU)

    def spanne(a, b, yy, text, farbe):
        s.pfeil((px(a), yy), (px(b), yy), "", farbe=farbe, spitze=0.14, dicke=3, doppelt=True)
        s.text(None, text, (0.5 * (px(a) + px(b)), yy + 0.2), KLEIN, "center", farbe)
    s.linie(None, (px(7), y), (px(7), 0.62), farbe=GRUEN, dicke=2, dash=DASH)
    s.linie(None, (px(-3), y), (px(-3), 0.62), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(None, (px(5), y), (px(5), 0.2), farbe=GRAU, dicke=2, dash=DASH)
    spanne(-3, 5, 0.2, "d(x, y) = 8", SCHWARZ)
    spanne(-3, 7, 0.62, "d(x, z) = 10", GRUEN)
    spanne(5, 7, 0.2, "d(z, y) = 2", GRUEN)
    s.text(None, "x", (px(-3) - 0.16, y + 0.17), MITTEL, "center", BLAU)
    s.text(None, "y", (px(5) - 0.16, y + 0.17), MITTEL, "center", ROT)
    s.text(None, "z", (px(7) + 0.16, y + 0.17), MITTEL, "center", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k1mittel():
    """Links Halbkreis zu x = 2, y = 8, rechts Bernoulli für n = 3."""
    s = Szene("hm1/k1mittel")
    s.welt()
    m = 0.29                                    # Einheiten je Zahlwert
    x0, y0 = -3.4, -0.7
    r = 5 * m
    cx = x0 + r
    s.weg(None, "%g+%g*cos(t)" % (cx, r), "%g+%g*sin(t)" % (y0, r), 0, 3.14159265, farbe=GRAU, dicke=3)
    s.linie(None, (x0, y0), (x0 + 10 * m, y0), farbe=SCHWARZ, dicke=3)
    fx = x0 + 2 * m
    s.linie(None, (fx, y0), (fx, y0 + 4 * m), farbe=ROT, dicke=4)
    s.linie(None, (cx, y0), (cx, y0 + r), farbe=BLAU, dicke=4)
    for p in (x0, fx, cx, x0 + 10 * m):
        s.punkt(None, p, y0, r=0.06)
    s.text(None, "x = 2", (0.5 * (x0 + fx), y0 - 0.27), KLEIN, "center")
    s.text(None, "y = 8", (0.5 * (fx + x0 + 10 * m), y0 - 0.27), KLEIN, "center")
    s.text(None, "√(xy) = 4", (fx - 0.1, y0 + 4 * m + 0.26), KLEIN, "center", ROT)
    s.text(None, "(x + y)/2 = 5", (cx + 0.1, y0 + 0.5 * r), KLEIN, "left", BLAU)

    a = s.achsen((-1.5, 1), (-3.5, 8), breite=2.4, hoehe=1.75, mitte=(1.65, 0.0), kreuz=True, xticks="1", yticks="1;5", xl="x")
    s.linie(a, (-1, -3.5), (-1, 8), farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(a, "(1+x)^3", x=(-1.5, 1), farbe=BLAU, dicke=4)
    s.kurve(a, "1+3*x", x=(-1.5, 1), farbe=ROT, dicke=3)
    s.text(a, "(1 + x)³", (0.18, 7.4), KLEIN, "left", BLAU)
    s.text(a, "1 + 3x", (0.62, 1.7), KLEIN, "left", ROT)
    s.text(a, "x = −1", (-1.04, 7.4), KLEIN, "right", GRAU)
    s.speichern()


for f in (k1venn, k1quantoren, k1zahlbereiche, k1spiegel, k1induktion, k1luecke, k1schachtelung, k1betrag, k1mittel):
    f()
