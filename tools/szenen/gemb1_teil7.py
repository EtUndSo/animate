"""GEMB 1 Teil 7 (kap7_stufen.tex): Kristallwachstum und reziprokes Gitter.

Aufruf: python tools/szenen/gemb1_teil7.py, danach python tools/szenen_ansehen.py out.png gemb1/k7ofen ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap7.py.
"""
import sys
from itertools import combinations
from math import atan2, cos, pi, sin, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
KLEIN = 22
HELLBLAU, HELLROT, HELLGRUEN = "#dceafa", "#f6dede", "#ddf0e4"
DUNKEL = "#555555"


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def poly(s, on, ecken, farbe, deckung=0.3, dicke=0, rand=None):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": rand or farbe, "fill_color": farbe,
                              "fill_opacity": deckung, "stroke_width": dicke}, on)


def rechteck(s, on, x0, x1, y0, y1, farbe, deckung=1.0, dicke=0, rand=None):
    return poly(s, on, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], farbe, deckung, dicke, rand)


def drehpfeil(s, on, x, y, rx, ry, links, farbe=DUNKEL):
    """Flacher Ellipsenbogen mit Spitze: Drehsinn einer Achse. links=True: vorn nach links."""
    t0, t1 = (0.12 * pi, 1.88 * pi) if links else (0.88 * pi, -0.88 * pi)
    n = 40
    pk = [(x + rx * cos(t0 + (t1 - t0) * i / n), y + ry * sin(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    s.daten(on, pk, farbe=farbe, dicke=2.5)
    a, b = pk[-3], pk[-1]
    s.pfeil(a, b, "", farbe=farbe, spitze=0.12, dicke=2.5, on=on)


# ------------------------------------------------------------------------------------------ Stufe 1
def k7ofen():
    """Lichtbogenofen: heiße Zone unten, Gas steigt, Festes sinkt; rechts die Reaktionen je Temperaturzone."""
    s = Szene("gemb1/k7ofen")
    w = s.welt()
    x0, x1 = -3.3, -0.75
    wand = 0.14
    y = [-1.55, -1.05, -0.4, 0.12, 0.62, 1.12]    # Schmelze, >2000, 1700-1900, 1500-1700, <1500
    farben = ["#8f8f8f", "#e0483a", "#ef8a3c", "#f6bb5e", "#f8e3a8"]
    for i, f in enumerate(farben):
        rechteck(s, w, x0, x1, y[i], y[i + 1], f, deckung=0.85 if i else 0.75)
    rechteck(s, w, x0 - wand, x0, y[0] - wand, y[-1], DUNKEL)
    rechteck(s, w, x1, x1 + wand, y[0] - wand, y[-1], DUNKEL)
    rechteck(s, w, x0 - wand, x1 + wand, y[0] - wand, y[0], DUNKEL)
    xe = 0.5 * (x0 + x1)
    rechteck(s, w, xe - 0.2, xe + 0.2, -0.5, 1.6, "#3a3a3a")
    t(s, s.tr("elek", "Elektrode", "electrode", "electrodo", "电极"), (xe, 1.77), g=KLEIN)
    # Lichtbogen
    zack = [(xe, -0.5), (xe - 0.1, -0.6), (xe + 0.08, -0.7), (xe - 0.08, -0.8), (xe + 0.06, -0.9), (xe, -1.0)]
    s.daten(w, zack, farbe="#ffffff", dicke=4)
    t(s, s.tr("bogen", "Lichtbogen", "arc", "arco", "电弧"), (xe + 0.22, -0.78), "left", "#ffffff", g=KLEIN)
    # Gas steigt, Festes sinkt
    s.pfeil((x1 - 0.32, -0.7), (x1 - 0.32, 0.98), "", farbe=BLAU, spitze=0.17, dicke=4)
    t(s, "SiO, CO", (x1 - 0.42, 0.8), "right", BLAU, g=KLEIN)
    s.pfeil((x0 + 0.3, 0.98), (x0 + 0.3, -0.7), "", farbe=ROT, spitze=0.17, dicke=4)
    t(s, s.tr("sinkt1", "Festes", "solids", "sólido", "固体"), (x0 + 0.42, 0.86), "left", ROT, g=KLEIN)
    t(s, s.tr("sinkt2", "sinkt", "sink", "baja", "下沉"), (x0 + 0.42, 0.64), "left", ROT, g=KLEIN)
    t(s, s.tr("schm", "flüssiges Si", "liquid Si", "Si líquido", "液态硅"), (xe, -1.3), farbe="#ffffff")
    # Zufuhr und Abgang
    s.pfeil((x0 + 0.42, 1.75), (x0 + 0.42, 1.17), "", farbe=SCHWARZ, spitze=0.16)
    t(s, s.tr("zufuhr", "Quarz + Koks", "quartz + coke", "cuarzo + coque", "石英 + 焦炭"), (x0 - 0.1, 1.93), "left", g=KLEIN)
    s.pfeil((x1 - 0.42, 1.17), (x1 - 0.42, 1.75), "", farbe=BLAU, spitze=0.16)
    t(s, "CO", (x1 - 0.42, 1.93), farbe=BLAU, g=KLEIN)
    # Reaktionen rechts
    xr = -0.3
    zeilen = [(0.87, "< 1500 °C", "SiO + CO → SiO₂ + C"), (0.37, "1500–1700 °C", "SiO + 2C → SiC + CO"),
              (-0.14, "1700–1900 °C", "SiO₂ + C → SiO + CO"), (-0.72, "> 2000 °C", "SiO₂ + SiC → Si + SiO + CO")]
    for yz, T, re_ in zeilen:
        t(s, T, (xr, yz + 0.13), "left", ROT, g=KLEIN)
        t(s, re_, (xr, yz - 0.13), "left", g=GR)
        s.linie(w, (x1 + wand + 0.03, yz), (xr - 0.05, yz), farbe=GRAU, dicke=1.5, dash=DOT)
    t(s, s.tr("gesamt", "Gesamt:", "Overall:", "Total:", "总反应："), (xr, -1.2), "left", BLAU, g=KLEIN)
    t(s, "SiO₂ + 2C → Si + 2CO", (xr, -1.46), "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k7siede():
    """Links Siedetemperaturen der Chloride, rechts die Abscheidung am heißen Stab."""
    s = Szene("gemb1/k7siede")
    w = s.welt()
    werte = [("BCl₃", 12), ("SiHCl₃", 31.8), ("CCl₄", 76), ("PCl₃", 76), ("GeCl₄", 83), ("AsCl₃", 132), ("AlCl₃", 188), ("SbCl₃", 223)]
    xa, sk = -2.6, 1.75 / 223
    y0 = 1.3
    t(s, s.tr("siedet", "Siedetemperatur in °C", "boiling point in °C", "temperatura de ebullición en °C", "沸点 / °C"), (-3.4, 1.72), "left")
    for i, (n, T) in enumerate(werte):
        y = y0 - 0.36 * i
        f = ROT if i == 1 else BLAU
        rechteck(s, w, xa, xa + sk * T, y - 0.12, y + 0.12, f, deckung=0.85 if i == 1 else 0.45)
        t(s, n, (xa - 0.07, y), "right", f if i == 1 else SCHWARZ, g=KLEIN)
        t(s, ("%.1f" % T) if T != int(T) else "%d" % T, (xa + sk * T + 0.08, y), "left", f if i == 1 else SCHWARZ, g=KLEIN)
    s.linie(w, (xa, y0 + 0.18), (xa, y0 - 0.36 * 7 - 0.18), dicke=2.5)
    # Reaktor
    xm, r = 2.05, 1.05
    yb = -0.95
    kuppel = [(xm - r, yb)] + [(xm - r * cos(pi * i / 40), 0.4 + r * sin(pi * i / 40)) for i in range(41)] + [(xm + r, yb)]
    s.daten(w, kuppel, farbe=BLAU, dicke=6)
    rechteck(s, w, xm - r - 0.3, xm + r + 0.3, yb - 0.25, yb, DUNKEL)
    # U-förmiger Stab: dünner Impfstab, darum Polysilizium
    st = 0.5
    ob = 0.68
    for x in (xm - st, xm + st):
        rechteck(s, w, x - 0.16, x + 0.16, yb, ob, "#a9a9a9")
        rechteck(s, w, x - 0.04, x + 0.04, yb, ob, ROT, deckung=0.9)
    rechteck(s, w, xm - st - 0.16, xm + st + 0.16, ob, ob + 0.3, "#a9a9a9")
    rechteck(s, w, xm - st - 0.04, xm + st + 0.04, ob + 0.11, ob + 0.19, ROT, deckung=0.9)
    t(s, s.tr("heiss", "1000–1150 °C", "1000–1150 °C", "1000–1150 °C", "1000–1150 °C"), (xm, 1.2), farbe=ROT, g=KLEIN)
    t(s, s.tr("bell", "Quarzglocke", "quartz bell", "campana de cuarzo", "石英钟罩"), (xm - 0.75, 1.68), "right", BLAU, g=KLEIN)
    s.pfeil((xm, -1.72), (xm, -0.5), "", farbe=SCHWARZ, spitze=0.16)
    t(s, "SiHCl₃ + H₂", (xm, -1.93), g=KLEIN)
    # Strom
    s.draht((xm - st, yb - 0.25), (xm - st, -1.45), (xm - 1.1, -1.45), dicke=2.5)
    s.punkt(w, xm - 1.1, -1.45, r=0.06)
    s.draht((xm + st, yb - 0.25), (xm + st, -1.45), (xm + 1.1, -1.45), dicke=2.5)
    s.punkt(w, xm + 1.1, -1.45, r=0.06)
    t(s, s.tr("strom", "Strom heizt", "current heats", "corriente calienta", "电流加热"), (xm - 1.2, -1.45), "right", g=KLEIN)
    s.pfeil((xm - 1.25, 0.5), (xm - st - 0.15, 0.2), "", farbe=SCHWARZ, spitze=0.13, dicke=2)
    t(s, s.tr("poly", "Polysilizium", "polysilicon", "polisilicio", "多晶硅"), (xm - 1.3, 0.55), "right", g=KLEIN)
    s.pfeil((xm - 1.25, -0.1), (xm - st - 0.03, -0.2), "", farbe=ROT, spitze=0.13, dicke=2)
    t(s, s.tr("impf", "dünner Si-Stab", "thin Si rod", "varilla fina de Si", "细硅棒"), (xm - 1.3, -0.05), "right", ROT, g=KLEIN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k7ziehen():
    """Links die Ziehanlage, rechts die Form des Kristalls mit den Ziehphasen."""
    s = Szene("gemb1/k7ziehen")
    w = s.welt()
    # Tiegel
    xm = -1.75
    bt = 1.25
    y0, ys, yr = -1.95, -0.85, -0.3
    rechteck(s, w, xm - bt - 0.22, xm + bt + 0.22, y0 - 0.22, yr, DUNKEL)
    rechteck(s, w, xm - bt, xm + bt, y0, yr, "#d5e6f5")
    rechteck(s, w, xm - bt + 0.1, xm + bt - 0.1, y0 + 0.1, yr, "#ffffff")
    rechteck(s, w, xm - bt + 0.1, xm + bt - 0.1, y0 + 0.1, ys, "#f2b63c", deckung=0.95)
    t(s, s.tr("sm", "flüssiges Si", "liquid Si", "Si líquido", "液态硅"), (xm - 0.05, y0 + 0.42), g=KLEIN)
    # Kristall
    rk = 0.58
    kristall = [(xm - rk, ys), (xm - rk, 0.1), (xm - 0.5, 0.35), (xm - 0.1, 0.7), (xm - 0.05, 0.9), (xm - 0.05, 1.25), (xm + 0.05, 1.25),
                (xm + 0.05, 0.9), (xm + 0.1, 0.7), (xm + 0.5, 0.35), (xm + rk, 0.1), (xm + rk, ys)]
    poly(s, w, kristall, "#b9bec6", deckung=1.0, dicke=2, rand=SCHWARZ)
    t(s, s.tr("barren", "Barren", "ingot", "lingote", "晶锭"), (xm, -0.25), g=KLEIN)
    # Stange und Drehsinn
    rechteck(s, w, xm - 0.12, xm + 0.12, 1.25, 1.5, DUNKEL)
    s.pfeil((xm, 1.5), (xm, 2.05), "", farbe=SCHWARZ, spitze=0.2, dicke=4)
    drehpfeil(s, w, xm, 1.73, 0.3, 0.08, True)
    rechteck(s, w, xm - 0.17, xm + 0.17, y0 - 0.62, y0 - 0.22, DUNKEL)
    drehpfeil(s, w, xm, y0 - 0.75, 0.32, 0.08, False)
    # Heizung
    for i in range(4):
        y = y0 + 0.2 + 0.42 * i
        s.kreis(w, xm - bt - 0.42, y, 0.075, farbe=ROT, fuellung=ROT, deckung=1.0)
        s.kreis(w, xm + bt + 0.42, y, 0.075, farbe=ROT, fuellung=ROT, deckung=1.0)
    t(s, s.tr("hz", "Heizung", "heater", "calefactor", "加热器"), (xm + bt + 0.62, 0.02), "right", ROT, g=KLEIN)
    s.pfeil((xm + bt + 0.55, -0.05), (xm + bt + 0.45, -0.45), "", farbe=ROT, spitze=0.12, dicke=2)
    t(s, s.tr("argon", "Argon", "argon", "argón", "氩气"), (xm + 0.75, 0.4), "left", g=KLEIN)
    t(s, s.tr("gt", "Graphit", "graphite", "grafito", "石墨"), (xm - bt - 0.3, -2.42), "left", DUNKEL, g=KLEIN)
    s.pfeil((xm - bt - 0.05, -2.25), (xm - bt - 0.1, -2.05), "", farbe=DUNKEL, spitze=0.1, dicke=2)
    t(s, s.tr("qz", "Quarz", "quartz", "cuarzo", "石英"), (xm + bt + 0.3, -2.42), "right", BLAU, g=KLEIN)
    s.pfeil((xm + bt - 0.1, -2.27), (xm + bt - 0.06, -1.95), "", farbe=BLAU, spitze=0.1, dicke=2)
    # Rechts: Form des Kristalls von oben nach unten
    xk = 0.92
    rr = 0.62
    prof = [(0.09, 1.95), (0.09, 1.55), (0.03, 1.3), (0.03, 0.7), (0.1, 0.48), (0.3, 0.18), (0.52, -0.14), (rr, -0.35), (rr, -2.1)]
    gesamt = [(xk - x, y) for x, y in prof] + [(xk + x, y) for x, y in reversed(prof)]
    poly(s, w, gesamt, "#b9bec6", deckung=1.0, dicke=2, rand=SCHWARZ)
    # Versetzungen im Hals: laufen schräg und enden an der Oberfläche
    for y1 in (1.53, 1.37, 1.17):
        s.linie(w, (xk - 0.06, y1), (xk + 0.04, y1 - 0.16), farbe=ROT, dicke=2.5)
    xl = xk + rr + 0.12
    eintraege = [(1.75, xk + 0.09, "seed", "Impfkristall", "seed crystal", "cristal semilla", "籽晶", SCHWARZ),
                 (1.0, xk + 0.03, "neck", "Hals, 3 mm: schnell", "neck, 3 mm: fast", "cuello, 3 mm: rápido", "缩颈，3 mm：快拉", ROT),
                 (0.18, xk + 0.3, "kon", "Konus: langsamer", "cone: slower", "cono: más lento", "放肩：减速", SCHWARZ),
                 (-0.3, xk + rr, "sch", "Schulter", "shoulder", "hombro", "转肩", SCHWARZ),
                 (-1.2, xk + rr, "zyl", "Zylinder: 2–250 mm/h", "cylinder: 2–250 mm/h", "cilindro: 2–250 mm/h", "等径：2–250 mm/h", SCHWARZ)]
    for y, xp, key, de, en, es, zh, f in eintraege:
        s.linie(w, (xp + 0.03, y), (xl - 0.03, y), farbe=GRAU, dicke=1.5)
        t(s, s.tr(key, de, en, es, zh), (xl, y), "left", f, g=KLEIN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k7periodisch():
    """Oben das Kosinus-Band als periodische Kurve, unten die Parabel ausgedehnt und in die Zone gefaltet."""
    s = Szene("gemb1/k7periodisch")
    w = s.welt()
    T0 = 0.03811 / 0.2 ** 2
    a = s.achsen((-3.5, 3.5), (0, 4.6), breite=6.0, hoehe=1.25, mitte=(0.15, 1.05), yl=s.tr("ee", "E in eV", "E in eV", "E en eV", "E / eV"),
                 xticks="-3;-2;-1;0;1;2;3", yticks="0;2;4", xzahlen=False)
    s.band(a, -1, 1, 0, 4.6, farbe=BLAU, deckung=0.10)
    s.kurve(a, "%.4f*(1-cos(pi*x))" % (2 * T0), x=(-3.5, 3.5), farbe=BLAU, dicke=4)
    for k in (-2, 0, 2):
        s.punkt(a, k, 0.0, farbe=ROT, r=0.09)
    for k, txt in ((-3, "-3\\pi/a"), (-2, "-2\\pi/a"), (-1, "-\\pi/a"), (0, "0"), (1, "\\pi/a"), (2, "2\\pi/a"), (3, "3\\pi/a")):
        s.text(a, txt, (k, -1.15), groesse=KLEIN, ausrichtung="center", farbe=ROT if k % 2 == 0 else SCHWARZ)
    s.text(a, "k", (3.62, 0.3), groesse=GR, ausrichtung="center")
    s.pfeil((-2, 4.3), (0, 4.3), "", on=a, farbe=ROT, spitze=0.13, dicke=2.5, doppelt=True)
    s.text(a, "2\\pi/a", (-1, 4.85), groesse=KLEIN, ausrichtung="center", farbe=ROT)
    # Unten: Parabelschar
    e = "E/E_{\\pi/a}"
    xlab = s.tr("kz", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)")
    b = s.achsen((-3.3, 3.3), (0, 10), breite=3.1, hoehe=1.3, mitte=(-1.65, -1.08), xl=xlab, yl=e, xticks="-2;0;2", yticks="0;5;10")
    s.band(b, -1, 1, 0, 10, farbe=BLAU, deckung=0.10)
    for n, f, d in ((-2, GRAU, 2.5), (2, GRAU, 2.5)):
        c = sqrt(10)
        s.kurve(b, "(x-(%d))^2" % n, x=(max(-3.3, n - c), min(3.3, n + c)), farbe=f, dicke=d)
    s.kurve(b, "x^2", x=(-3.162, 3.162), farbe=BLAU, dicke=5)
    s.text(b, s.tr("sch", "Schar: Scheitel bei G", "family: apex at G", "familia: vértice en G", "抛物线族：顶点在 G"), (0, 11.4), groesse=KLEIN, ausrichtung="center")
    c_ = s.achsen((-1.3, 1.3), (0, 10), breite=2.1, hoehe=1.3, mitte=(1.9, -1.08), xl=xlab, yl="", xticks="-1;0;1", yticks="0;5;10")
    s.band(c_, -1, 1, 0, 10, farbe=BLAU, deckung=0.10)
    s.kurve(c_, "x^2", x=(-1, 1), farbe=BLAU, dicke=5)
    s.kurve(c_, "(abs(x)-2)^2", x=(-1, 1), farbe=GRUEN, dicke=4)
    s.kurve(c_, "(abs(x)+2)^2", x=(-1, 1), farbe=ORANGE, dicke=4)
    s.kurve(c_, "(abs(x)-4)^2", x=(-1, 1), farbe=ROT, dicke=4)
    s.text(c_, "1", (0.0, 1.1), groesse=KLEIN, ausrichtung="center", farbe=BLAU)
    s.text(c_, "2", (0.0, 2.9), groesse=KLEIN, ausrichtung="center", farbe=GRUEN)
    s.text(c_, "3", (0.0, 5.2), groesse=KLEIN, ausrichtung="center", farbe=ORANGE)
    s.text(c_, s.tr("red", "in die Zone gefaltet", "folded into the zone", "plegada en la zona", "折叠到区内"), (0, 11.4), groesse=KLEIN, ausrichtung="center")
    s.linie(c_, (-1, 0), (-1, 10), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(c_, (1, 0), (1, 10), farbe=GRAU, dicke=2, dash=DASH)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def gitterbild(s, w, o, v1, v2, rx, ry, box, r=0.06, farbe=SCHWARZ):
    """Punkte o + i v1 + j v2 innerhalb des Rahmens box = (x0, x1, y0, y1)."""
    for i in range(-rx, rx + 1):
        for j in range(-ry, ry + 1):
            x, y = o[0] + i * v1[0] + j * v2[0], o[1] + i * v1[1] + j * v2[1]
            if box[0] - 1e-6 <= x <= box[1] + 1e-6 and box[2] - 1e-6 <= y <= box[3] + 1e-6:
                s.punkt(w, x, y, r=r, farbe=farbe)


def k7rezi2d():
    """Rechteckgitter und zentriert-rechteckiges Gitter mit ihren reziproken Gittern."""
    s = Szene("gemb1/k7rezi2d")
    w = s.welt()
    sr, sk = 1.75, 0.052          # Einheiten je nm und je 1/nm
    ax, ay = 0.40 * sr, 0.60 * sr
    b1, b2 = 15.708 * sk, 10.472 * sk
    t(s, s.tr("orts", "Ortsraum", "real space", "espacio real", "实空间"), (-1.85, 2.42), g=26)
    t(s, s.tr("kraum", "k-Raum: reziprokes Gitter", "k-space: reciprocal lattice", "espacio k: red recíproca", "k 空间：倒易点阵"), (1.85, 2.42), g=26)

    def pa(p, q, f, name, seite=(0.0, 0.0)):
        s.pfeil(p, q, "", farbe=f, spitze=0.15, dicke=4)
        t(s, name, (0.5 * (p[0] + q[0]) + seite[0], 0.5 * (p[1] + q[1]) + seite[1]), farbe=f)

    # Zeile 1: rechteckig
    o = (-2.6, 0.72)
    bx = (-3.45, -0.25, 0.25, 2.2)
    poly(s, w, [o, (o[0] + ax, o[1]), (o[0] + ax, o[1] + ay), (o[0], o[1] + ay)], BLAU, deckung=0.2)
    gitterbild(s, w, o, (ax, 0), (0, ay), 4, 3, bx)
    pa(o, (o[0] + ax, o[1]), ROT, "a_1", (0.0, -0.22))
    pa(o, (o[0], o[1] + ay), ROT, "a_2", (-0.2, 0.0))
    o2 = (1.75, 1.05)
    bx = (0.35, 3.3, 0.25, 2.2)
    poly(s, w, [o2, (o2[0] + b1, o2[1]), (o2[0] + b1, o2[1] + b2), (o2[0], o2[1] + b2)], GRUEN, deckung=0.18)
    gitterbild(s, w, o2, (b1, 0), (0, b2), 3, 3, bx)
    pa(o2, (o2[0] + b1, o2[1]), GRUEN, "b_1", (0.0, -0.22))
    pa(o2, (o2[0], o2[1] + b2), GRUEN, "b_2", (-0.2, 0.0))
    # Zeile 2: zentriert-rechteckig
    o = (-2.6, -1.4)
    bx = (-3.45, -0.25, -2.05, -0.1)
    v1, v2 = (ax, 0), (ax / 2, ay / 2)
    poly(s, w, [o, (o[0] + v1[0], o[1]), (o[0] + v1[0] + v2[0], o[1] + v2[1]), (o[0] + v2[0], o[1] + v2[1])], BLAU, deckung=0.2)
    gitterbild(s, w, o, v1, v2, 7, 6, bx)
    pa(o, (o[0] + v1[0], o[1]), ROT, "a_1", (0.0, -0.22))
    pa(o, (o[0] + v2[0], o[1] + v2[1]), ROT, "a_2", (-0.2, 0.1))
    o2 = (1.75, -1.2)
    bx = (0.35, 3.3, -2.05, -0.1)
    v1, v2 = (b1, -b2), (0.0, 2 * b2)
    poly(s, w, [o2, (o2[0] + v1[0], o2[1] + v1[1]), (o2[0] + v1[0] + v2[0], o2[1] + v1[1] + v2[1]), (o2[0] + v2[0], o2[1] + v2[1])], GRUEN, deckung=0.18)
    gitterbild(s, w, o2, v1, v2, 5, 5, bx)
    pa(o2, (o2[0] + v1[0], o2[1] + v1[1]), GRUEN, "b_1", (-0.22, -0.2))
    pa(o2, (o2[0] + v2[0], o2[1] + v2[1]), GRUEN, "b_2", (-0.2, 0.0))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def clip(pol, n, d):
    """Sutherland-Hodgman: Teil des Polygons mit n·p <= d."""
    aus = []
    for i, p in enumerate(pol):
        q = pol[(i + 1) % len(pol)]
        dp, dq = n[0] * p[0] + n[1] * p[1] - d, n[0] * q[0] + n[1] * q[1] - d
        if dp <= 1e-12:
            aus.append(p)
        if (dp < -1e-12 and dq > 1e-12) or (dp > 1e-12 and dq < -1e-12):
            f = dp / (dp - dq)
            aus.append((p[0] + f * (q[0] - p[0]), p[1] + f * (q[1] - p[1])))
    return aus


def ws2d(v1, v2, rand=5.0):
    pol = [(-rand, -rand), (rand, -rand), (rand, rand), (-rand, rand)]
    for i in range(-3, 4):
        for j in range(-3, 4):
            if i or j:
                g = (i * v1[0] + j * v2[0], i * v1[1] + j * v2[1])
                pol = clip(pol, g, 0.5 * (g[0] ** 2 + g[1] ** 2))
    return pol


def poly3d(ebenen):
    """Konvexer Körper aus Ebenen (n, d) mit n·p <= d: Ecken je Fläche, gegen den Uhrzeigersinn um die Normale."""
    def dot(u, v):
        return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

    def cross(u, v):
        return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])

    ecken = []
    for (n1, d1), (n2, d2), (n3, d3) in combinations(ebenen, 3):
        c23 = cross(n2, n3)
        det = dot(n1, c23)
        if abs(det) < 1e-9:
            continue
        c31, c12 = cross(n3, n1), cross(n1, n2)
        p = tuple((d1 * c23[i] + d2 * c31[i] + d3 * c12[i]) / det for i in range(3))
        if all(dot(n, p) <= d + 1e-9 for n, d in ebenen) and not any(max(abs(p[i] - q[i]) for i in range(3)) < 1e-7 for q in ecken):
            ecken.append(p)
    flaechen = []
    for n, d in ebenen:
        f = [p for p in ecken if abs(dot(n, p) - d) < 1e-7]
        if len(f) < 3:
            continue
        m = tuple(sum(p[i] for p in f) / len(f) for i in range(3))
        u = tuple(f[0][i] - m[i] for i in range(3))
        v = cross(n, u)
        f.sort(key=lambda p: atan2(dot(v, tuple(p[i] - m[i] for i in range(3))) / sqrt(dot(v, v)), dot(u, tuple(p[i] - m[i] for i in range(3))) / sqrt(dot(u, u))))
        flaechen.append((n, f))
    return flaechen


AZ, EL = 0.42, 0.33


def proj3(p, S, o):
    x, y, z = p
    X = y * cos(AZ) - x * sin(AZ)
    Y = z * cos(EL) - (x * cos(AZ) + y * sin(AZ)) * sin(EL)
    return (o[0] + S * X, o[1] + S * Y)


def sicht(n):
    b = (cos(AZ) * cos(EL), sin(AZ) * cos(EL), sin(EL))
    return n[0] * b[0] + n[1] * b[1] + n[2] * b[2] > 1e-9


def koerper(s, w, ebenen, S, o, farbe):
    fl = poly3d(ebenen)
    kanten = {}
    for n, f in fl:
        v = sicht(n)
        for i in range(len(f)):
            p, q = f[i], f[(i + 1) % len(f)]
            key = tuple(sorted((tuple(round(c, 6) for c in p), tuple(round(c, 6) for c in q))))
            kanten[key] = kanten.get(key, False) or v
    for (p, q), v in kanten.items():
        if not v:
            s.linie(w, proj3(p, S, o), proj3(q, S, o), farbe=GRAU, dicke=1.5, dash="6,5")
    for n, f in fl:
        if sicht(n):
            poly(s, w, [proj3(p, S, o) for p in f], farbe, deckung=0.16 + 0.28 * max(0.0, n[0] * 0.2 + n[2] * 0.4 + n[1] * 0.1) / sqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2))
    for (p, q), v in kanten.items():
        if v:
            s.linie(w, proj3(p, S, o), proj3(q, S, o), farbe=farbe, dicke=2.5)


def achsen3(s, w, S, o, l):
    for e, name, sh in (((2.1 * l, 0, 0), "k_x", (-0.12, -0.1)), ((0, l, 0), "k_y", (0.2, 0.0)), ((0, 0, l), "k_z", (0.2, 0.0))):
        p = proj3(e, S, o)
        s.pfeil(o, p, "", farbe=SCHWARZ, spitze=0.12, dicke=2)
        t(s, name, (p[0] + sh[0], p[1] + sh[1]), g=KLEIN)


def k7zonen():
    """Oben die Konstruktion der Zone in zwei Dimensionen, unten die drei kubischen Fälle."""
    s = Szene("gemb1/k7zonen")
    w = s.welt()
    sk = 0.046
    b1, b2 = 15.708 * sk, 10.472 * sk

    def tafel(o, v1, v2, box):
        zone = [(o[0] + x, o[1] + y) for x, y in ws2d(v1, v2)]
        poly(s, w, zone, GRAU, deckung=0.3, dicke=2.5, rand=SCHWARZ)
        for i in range(-3, 4):
            for j in range(-3, 4):
                if not (i or j):
                    continue
                g = (i * v1[0] + j * v2[0], i * v1[1] + j * v2[1])
                ll = sqrt(g[0] ** 2 + g[1] ** 2)
                if ll > 1.15 * max(sqrt(v1[0] ** 2 + v1[1] ** 2), sqrt(v2[0] ** 2 + v2[1] ** 2)):
                    continue
                m = (o[0] + g[0] / 2, o[1] + g[1] / 2)
                u = (-g[1] / ll, g[0] / ll)
                s.linie(w, (o[0], o[1]), (o[0] + g[0], o[1] + g[1]), farbe=GRUEN, dicke=2)
                s.linie(w, (m[0] - 0.55 * u[0], m[1] - 0.55 * u[1]), (m[0] + 0.55 * u[0], m[1] + 0.55 * u[1]), farbe=ROT, dicke=1.8, dash=DASH)
        gitterbild(s, w, o, v1, v2, 5, 5, box)
        s.punkt(w, o[0], o[1], r=0.08, farbe=ROT)

    tafel((-1.95, 2.0), (b1, 0), (0, b2), (-3.0, -0.9, 1.0, 2.98))
    tafel((1.85, 2.0), (b1, -b2), (0, 2 * b2), (0.8, 2.9, 1.0, 2.98))
    t(s, s.tr("zrect", "Rechteck: Zone ist Rechteck", "rectangle: zone is a rectangle", "rectángulo: zona rectangular", "矩形：区为矩形"), (-1.95, 3.2), g=KLEIN)
    t(s, s.tr("zhex", "zentriert: Zone ist Sechseck", "centred: zone is a hexagon", "centrada: zona hexagonal", "有心：区为六边形"), (1.85, 3.2), g=KLEIN)
    # Unten: Körper in Einheiten 2 pi / a
    ycen = -0.5
    S = 0.74
    wuerfel = [((1, 0, 0), .5), ((-1, 0, 0), .5), ((0, 1, 0), .5), ((0, -1, 0), .5), ((0, 0, 1), .5), ((0, 0, -1), .5)]
    from itertools import product
    rhomb = []
    for (p, q) in ((0, 1), (0, 2), (1, 2)):
        for sa, sb in product((1, -1), repeat=2):
            n = [0, 0, 0]
            n[p], n[q] = sa, sb
            rhomb.append((tuple(n), 1.0))
    okta = [((1, 0, 0), 1.0), ((-1, 0, 0), 1.0), ((0, 1, 0), 1.0), ((0, -1, 0), 1.0), ((0, 0, 1), 1.0), ((0, 0, -1), 1.0)]
    for sx, sy, sz in product((1, -1), repeat=3):
        okta.append(((sx, sy, sz), 1.5))
    fuelle = [(-2.5, wuerfel, BLAU, S * 1.25), (-0.1, rhomb, ROT, S), (2.3, okta, GRUEN, S * 0.86)]
    for x, e, f, sc in fuelle:
        o = (x, ycen)
        koerper(s, w, e, sc, o, f)
    for x, l in ((-2.5, 0.95), (-0.1, 1.2), (2.3, 1.3)):
        achsen3(s, w, S * (1.25 if x < -1 else (1 if x < 1 else 0.86)), (x, ycen), l)
    for x, key, de, en, es, zh in ((-2.5, "t1", "SC-Kristall", "SC crystal", "cristal SC", "SC 晶体"), (-0.1, "t2", "BCC-Kristall", "BCC crystal", "cristal BCC", "BCC 晶体"), (2.3, "t3", "FCC-Kristall", "FCC crystal", "cristal FCC", "FCC 晶体")):
        t(s, s.tr(key, de, en, es, zh), (x, 0.62), g=KLEIN)
    for x, key, de, en, es, zh in ((-2.5, "f1", "Würfel", "cube", "cubo", "立方体"), (-0.1, "f2", "Rhombendodekaeder", "rhombic dodecahedron", "dodecaedro rómbico", "菱形十二面体"), (2.3, "f3", "abgestumpftes Oktaeder", "truncated octahedron", "octaedro truncado", "截角八面体")):
        t(s, s.tr(key, de, en, es, zh), (x, -1.72), g=KLEIN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k7ebenen():
    """Geradenscharen (1 1) und (2 1) des Rechteckgitters und ihre reziproken Vektoren."""
    s = Szene("gemb1/k7ebenen")
    w = s.welt()
    sr = 1.05
    ax, ay = 0.40 * sr, 0.60 * sr
    sk = 0.042
    b1, b2 = 15.708 * sk, 10.472 * sk

    def tafel(ox, h1, h2, f, name, start):
        """start = Punkt in Gittereinheiten auf einer Geraden, dort beginnt der Pfeil d."""
        x0, y0 = ox, -1.1
        nx, ny = 4, 3
        bx = (x0 - 0.12, x0 + nx * ax + 0.12, y0 - 0.15, y0 + ny * ay + 0.15)
        # Geraden h1 x/ax + h2 y/ay = m, am Rahmen abgeschnitten
        for m in range(-3, 16):
            p = ((m - h2 * (bx[2] - y0) / ay) * ax / h1 + x0, bx[2])
            q = ((m - h2 * (bx[3] - y0) / ay) * ax / h1 + x0, bx[3])
            dx = q[0] - p[0]
            ta, tb = (bx[0] - p[0]) / dx, (bx[1] - p[0]) / dx
            t0, t1 = max(0.0, min(ta, tb)), min(1.0, max(ta, tb))
            if t1 > t0:
                s.linie(w, (p[0] + t0 * dx, p[1] + t0 * (q[1] - p[1])), (p[0] + t1 * dx, p[1] + t1 * (q[1] - p[1])), farbe=f, dicke=2.2)
        gitterbild(s, w, (x0, y0), (ax, 0), (0, ay), nx, ny, bx, r=0.05)
        G = (2 * pi * h1 / 0.40, 2 * pi * h2 / 0.60)
        ll = sqrt(G[0] ** 2 + G[1] ** 2)
        d = 2 * pi / ll * sr
        ge = (G[0] / ll, G[1] / ll)
        p = (x0 + start[0] * ax, y0 + start[1] * ay)
        q = (p[0] + d * ge[0], p[1] + d * ge[1])
        s.pfeil(p, q, "", farbe=SCHWARZ, spitze=0.09, dicke=2.5, doppelt=True)
        t(s, "d", (0.5 * (p[0] + q[0]) + 0.3 * ge[1], 0.5 * (p[1] + q[1]) - 0.3 * ge[0]), "center", g=GR)
        t(s, name, (0.5 * (bx[0] + bx[1]), bx[3] + 0.22), farbe=f)

    tafel(-3.42, 1, 1, BLAU, "(1 1)", (1.5, 0.5))
    tafel(-1.17, 2, 1, ORANGE, "(2 1)", (1.25, 0.5))
    o = (1.9, -0.6)
    bx = (0.92, 3.05, -1.28, 0.75)
    gitterbild(s, w, o, (b1, 0), (0, b2), 4, 5, bx, r=0.05)
    p1 = (o[0] + b1, o[1] + b2)
    p2 = (o[0] + 2 * b1, o[1] + b2)
    s.pfeil(o, p1, "", farbe=BLAU, spitze=0.14, dicke=3.5)
    s.pfeil(o, p2, "", farbe=ORANGE, spitze=0.14, dicke=3.5)
    t(s, "G_{11}", (p1[0] - 0.05, p1[1] + 0.17), "right", BLAU, g=KLEIN)
    t(s, "G_{21}", (p2[0] + 0.08, p2[1] + 0.17), "center", ORANGE, g=KLEIN)
    s.punkt(w, o[0], o[1], r=0.08, farbe=ROT)
    t(s, s.tr("rez", "reziprokes Gitter", "reciprocal lattice", "red recíproca", "倒易点阵"), (2.0, 1.03))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k7ueberblick():
    """Zwei Spalten: Ortsraum und k-Raum, verbunden durch dieselben Konstruktionen."""
    s = Szene("gemb1/k7ueberblick")
    xl, xr = -2.25, 2.4
    bl, br = 2.45, 2.1
    ho = 0.5
    t(s, s.tr("sp1", "Ortsraum", "real space", "espacio real", "实空间"), (xl, 2.0), farbe=BLAU, g=26)
    t(s, s.tr("sp2", "k-Raum", "k-space", "espacio k", "k 空间"), (xr, 2.0), farbe=GRUEN, g=26)
    links = [(1.58, "b0", "Bindungstyp", "bond type", "tipo de enlace", "键型"),
             (0.8, "b1", "Kristall = Gitter + Basis", "crystal = lattice + basis", "cristal = red + base", "晶体 = 点阵 + 基元"),
             (0.0, "b2", "Bravais-Gitter: R", "Bravais lattice: R", "red de Bravais: R", "布拉维点阵：R"),
             (-0.75, "b3", "Wigner-Seitz-Zelle", "Wigner-Seitz cell", "celda de Wigner-Seitz", "维格纳-塞茨原胞"),
             (-1.5, "b4", "Ebenenschar mit d", "plane family with d", "familia de planos, d", "晶面族，间距 d")]
    for y, key, de, en, es, zh in links:
        s.box(s.tr(key, de, en, es, zh), (xl, y), breite=bl, hoehe=ho, groesse=KLEIN, farbe=BLAU, fuellung=HELLBLAU)
    rechts = [(0.0, "c2", "reziprokes Gitter: G", "reciprocal lattice: G", "red recíproca: G", "倒易点阵：G"),
              (-0.75, "c3", "1. Brillouin-Zone", "1st Brillouin zone", "1.ª zona de Brillouin", "第一布里渊区"),
              (-1.5, "c4", "ein Punkt G", "one point G", "un punto G", "一个点 G")]
    for y, key, de, en, es, zh in rechts:
        s.box(s.tr(key, de, en, es, zh), (xr, y), breite=br, hoehe=ho, groesse=KLEIN, farbe=GRUEN, fuellung=HELLGRUEN)
    for y0, y1 in ((1.58, 0.8), (0.8, 0.0)):
        s.pfeil((xl, y0 - ho / 2 - 0.01), (xl, y1 + ho / 2 + 0.01), "", spitze=0.15)
    xa, xb = xl + bl / 2 + 0.02, xr - br / 2 - 0.02
    xm = 0.5 * (xa + xb)
    for y in (0.0, -0.75, -1.5):
        s.pfeil((xa, y), (xb, y), "", spitze=0.14, doppelt=True)
    t(s, "a_i · b_j = 2π δ_{ij}", (xm, 0.17), g=KLEIN)
    t(s, s.tr("gleich", "gleiche Konstruktion", "same construction", "misma construcción", "相同作法"), (xm, -0.58), g=KLEIN)
    t(s, s.tr("senk", "G ⟂ Ebene, |G| = 2π/d", "G ⟂ plane, |G| = 2π/d", "G ⟂ plano, |G| = 2π/d", "G ⟂ 晶面，|G| = 2π/d"), (xm, -1.33), g=KLEIN)
    s.speichern()


if __name__ == "__main__":
    k7ofen()
    k7siede()
    k7ziehen()
    k7periodisch()
    k7rezi2d()
    k7zonen()
    k7ebenen()
    k7ueberblick()
