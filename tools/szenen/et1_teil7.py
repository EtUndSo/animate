"""ET1 Teil 7 (kap7_stufen.tex): Leistung, Anpassung und Wirkungsgrad.

Aufruf: python tools/szenen/et1_teil7.py, danach python tools/szenen_ansehen.py out.png et1/k7ladung ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap7.py.
"""
import sys
from math import atan2, degrees, hypot
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

BRAUN = "#a84a22"
HELLROT, HELLBLAU = "#f6dede", "#dceafa"
GR = 24           # Beschriftung in Schaltbildern


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def wid(s, a, b, size=0.5, farbe=SCHWARZ):
    return bau(s, "resistor", a, b, size=size, farbe=farbe)


def uq(s, a, b, size=0.62, farbe=SCHWARZ):
    return bau(s, "vsource", a, b, size=size, farbe=farbe)


def kl(s, x, y, name="", dx=0.0, dy=0.3, farbe=SCHWARZ):
    """Klemme als kleiner Ring, Name daneben."""
    s.kreis(None, x, y, 0.07, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        s.text(None, name, (x + dx, y + dy), groesse=GR, ausrichtung="center", farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.06):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def spfeil(s, x, y0, y1, txt="", seite=1, farbe=BLAU, dx=0.1):
    """Senkrechter Spannungspfeil mit Text rechts (seite=1) oder links (seite=-1)."""
    s.pfeil((x, y0), (x, y1), "", farbe=farbe, spitze=0.17, dicke=2.5)
    if txt:
        t(s, txt, (x + seite * dx, 0.5 * (y0 + y1)), "left" if seite > 0 else "right", farbe)


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center"):
    """Kurzer Strompfeil auf einer Leitung."""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=3)
    if txt:
        t(s, txt, p, ausr, farbe)


def ladung(s, x, y, r=0.1):
    """Kleine positive Ladung (technische Stromrichtung)."""
    s.kreis(None, x, y, r, farbe=ROT, dicke=2, fuellung=HELLROT, deckung=1.0)
    s.linie(None, (x - 0.055, y), (x + 0.055, y), farbe=ROT, dicke=2)
    s.linie(None, (x, y - 0.055), (x, y + 0.055), farbe=ROT, dicke=2)


# ------------------------------------------------------------------------------------------ Stufe 1
def k7ladung():
    """Zweipol oben, Potenzialverlauf unten: Energie je Ladung mal Ladung je Zeit."""
    s = Szene("et1/k7ladung")
    yo = 1.0
    xl, xr = -0.95, 0.95
    xa = 3.1
    s.draht((-xa, yo), (xl, yo))
    s.draht((xr, yo), (xa, yo))
    wid(s, (xl, yo), (xr, yo), size=0.5)
    kl(s, -xa, yo)
    kl(s, xa, yo)
    t(s, "R_L", (0, yo + 0.36))
    ipfeil(s, (-2.3, yo), (-1.7, yo), "I = 0.5 A", (-2.0, yo + 0.32))
    s.pfeil((xl, yo - 0.42), (xr, yo - 0.42), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    t(s, "U = 8 V", (0, yo - 0.68), farbe=BLAU)
    # Potenzialverlauf
    yh, yn = 0.0, -1.05
    s.linie(None, (-xa, yh), (xl, yh), farbe=SCHWARZ, dicke=4)
    s.linie(None, (xl, yh), (xr, yn), farbe=SCHWARZ, dicke=4)
    s.linie(None, (xr, yn), (xa, yn), farbe=SCHWARZ, dicke=4)
    for x in (-2.8, -2.05, -1.3):
        ladung(s, x, yh + 0.14)
    for f in (0.2, 0.6):
        x = xl + f * (xr - xl)
        ladung(s, x + 0.1, yh + f * (yn - yh) + 0.17)
    for x in (1.3, 2.05, 2.8):
        ladung(s, x, yn + 0.14)
    t(s, "φ_1", (-xa - 0.14, yh), "right")
    t(s, "φ_2", (xa + 0.14, yn), "left")
    s.linie(None, (0.75, yh), (2.95, yh), farbe=GRAU, dicke=2, dash=DASH)
    s.pfeil((2.95, yh), (2.95, yn + 0.32), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    t(s, s.tr("jecoul", "jedes Coulomb gibt 8 J ab", "each coulomb gives off 8 J", "cada culombio cede 8 J", "每库仑释放 8 J"), (2.82, -0.42), "right", BLAU, 23)
    t(s, s.tr("jesek", "je Sekunde 0.5 C", "0.5 C per second", "0.5 C por segundo", "每秒 0.5 C"), (-1.1, -0.42), "right", ROT, 23)
    t(s, s.tr("produkt", "zusammen je Sekunde: 8 J/C · 0.5 C/s = 4 W", "per second: 8 J/C · 0.5 C/s = 4 W", "por segundo: 8 J/C · 0.5 C/s = 4 W", "每秒合计：8 J/C · 0.5 C/s = 4 W"), (0, -1.55), farbe=SCHWARZ)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k7stoss():
    """Stoßmodell: summierte Feldarbeit und Wärme im Gitter über der Zeit."""
    s = Szene("et1/k7stoss")
    s.welt()
    a = s.achsen((0, 5, 1), (0, 5, 1), breite=3.7, hoehe=2.0, mitte=(-1.25, 0), xl="t / T", yl="W / W_1", gitter=True)
    feld, gitter = [], []
    for k in range(5):
        feld += [(k + i / 24, k + (i / 24) ** 2) for i in range(25)]
        gitter += [(k, k), (k + 1, k), (k + 1, k + 1)]
    s.daten(a, feld, farbe=BLAU, dicke=5)
    s.daten(a, gitter, farbe=ROT, dicke=4)
    s.text(a, s.tr("feldarb", "Arbeit des Felds", "work done by the field", "trabajo del campo", "电场做的功"), (0.2, 4.45), groesse=23, farbe=BLAU)
    s.pfeil((1.6, 3.85), (3.72, 3.72), "", farbe=BLAU, spitze=0.15, dicke=2, on=a)
    s.text(a, s.tr("gitterw", "Wärme im Gitter", "heat in the lattice", "calor en la red", "晶格中的热量"), (2.75, 0.75), groesse=23, farbe=ROT)
    s.pfeil((3.3, 1.1), (2.55, 1.95), "", farbe=ROT, spitze=0.15, dicke=2, on=a)
    x = 0.95
    t(s, s.tr("flug", "Flug:", "flight:", "vuelo:", "飞行："), (x, 0.72), "left", BLAU, 24)
    t(s, s.tr("flug2", "Feld gibt Energie", "field gives energy", "el campo aporta", "电场供给能量"), (x, 0.4), "left", BLAU, 23)
    t(s, s.tr("flug3", "ans Elektron", "to the electron", "energía al electrón", "给电子"), (x, 0.1), "left", BLAU, 23)
    t(s, s.tr("stoss", "Stoß:", "collision:", "choque:", "碰撞："), (x, -0.32), "left", ROT, 24)
    t(s, s.tr("stoss2", "Elektron gibt W_1", "electron gives W_1", "el electrón cede W_1", "电子将 W_1"), (x, -0.64), "left", ROT, 23)
    t(s, s.tr("stoss3", "ans Gitter ab", "to the lattice", "a la red", "交给晶格"), (x, -0.94), "left", ROT, 23)
    s.speichern()


def k7grenze():
    """Belastungsgrenze eines 250-mW-Widerstands im I-U-Diagramm."""
    s = Szene("et1/k7grenze")
    a = s.achsen((0, 12, 2), (0, 120, 20), breite=4.3, hoehe=1.95, mitte=(-0.2, 0), xl=s.tr("u_v", "U in V", "U in V", "U en V", "U / V"),
                 yl=s.tr("i_ma", "I in mA", "I in mA", "I en mA", "I / mA"), yticks="0;20;40;60;80;100;120")
    s.flaeche(a, "min(120, 250/x)", 0.01, 12, f2="0", farbe=GRUEN, deckung=0.1)
    s.kurve(a, "250/x", x=(2.0833, 12), farbe=ORANGE, dicke=5)
    for un, im, fa in ((2.5, 100, ROT), (5, 50, BLAU), (10, 25, GRUEN)):
        s.linie(a, (0, 0), (un, im), farbe=fa, dicke=4)
        s.punkt(a, un, im, farbe=fa, r=0.08)
    s.text(a, "25 Ω", (1.95, 62), groesse=23, farbe=ROT)
    s.text(a, "100 Ω", (2.5, 17), groesse=23, farbe=BLAU)
    s.text(a, "400 Ω", (7.2, 9), groesse=23, farbe=GRUEN)
    s.text(a, "P = 250 mW", (4.1, 88), groesse=23, farbe=BRAUN)
    s.pfeil((4.0, 83), (3.25, 77.5), "", farbe=BRAUN, spitze=0.15, dicke=2, on=a)
    s.text(a, s.tr("zuheiss", "zu heiß", "too hot", "demasiado caliente", "过热"), (9.6, 106), groesse=23, farbe=SCHWARZ, ausrichtung="center")
    s.text(a, "(2.5 V; 100 mA)", (2.95, 104), groesse=22, farbe=ROT)
    s.text(a, "(5 V; 50 mA)", (5.3, 58), groesse=22, farbe=BLAU)
    s.text(a, "(10 V; 25 mA)", (8.0, 38), groesse=22, farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k7sinus():
    """Spannung, Strom und Leistung am Widerstand bei Sinusspannung."""
    s = Szene("et1/k7sinus")
    tl = s.tr("t_ms", "t in ms", "t in ms", "t en ms", "t / ms")
    a = s.achsen((0, 40, 10), (-10, 10, 5), breite=2.35, hoehe=1.75, mitte=(-2.05, 0), xl=tl,
                 yl=s.tr("ui", "u in V, i in A", "u in V, i in A", "u en V, i en A", "u / V，i / A"), yticks="-10;-5;0;5;10")
    s.linie(a, (0, 0), (40, 0), farbe=GRAU, dicke=2)
    s.kurve(a, "10*cos(2*pi*x/20)", farbe=BLAU, dicke=5)
    s.kurve(a, "2*cos(2*pi*x/20)", farbe=GRUEN, dicke=5)
    s.text(a, "u", (5.0, 8.3), groesse=25, farbe=BLAU, ausrichtung="center")
    s.text(a, "i", (22.0, 3.1), groesse=25, farbe=GRUEN, ausrichtung="center")
    b = s.achsen((0, 40, 10), (0, 20, 5), breite=2.35, hoehe=1.75, mitte=(1.25, 0), xl=tl,
                 yl=s.tr("p_w", "p in W", "p in W", "p en W", "p / W"), yticks="0;5;10;15;20")
    s.flaeche(b, "20*cos(2*pi*x/20)^2", 0, 40, f2="0", farbe=ROT, deckung=0.12)
    s.kurve(b, "20*cos(2*pi*x/20)^2", farbe=ROT, dicke=5)
    s.linie(b, (0, 10), (40, 10), farbe=SCHWARZ, dicke=3, dash=DASH)
    s.text(b, "p(t)", (15.0, 17.2), groesse=25, farbe=ROT, ausrichtung="center")
    s.text(b, "P = 10 W", (41.5, 10), groesse=23, farbe=SCHWARZ)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k7leitung():
    """Quelle, Leitung als Widerstand, Last; rechts die zwei Spannungsebenen."""
    s = Szene("et1/k7leitung")
    yo, yu = 0.8, -0.8
    x0, x1, x2, x3 = -3.35, -2.2, -0.75, 0.25
    uq(s, (x0, yo), (x0, yu))
    s.draht((x0, yo), (x1, yo))
    wid(s, (x1, yo), (x2, yo), size=0.45)
    s.draht((x2, yo), (x3, yo))
    wid(s, (x3, yo), (x3, yu), size=0.45, farbe=ORANGE)
    s.draht((x3, yu), (x0, yu))
    spfeil(s, x0 - 0.33, 0.5, -0.5, "U_q", seite=-1, farbe=SCHWARZ, dx=0.08)
    s.tr("kabel", "Kabel", "cable", "cable", "线路")
    t(s, "R_{@{kabel}}", (0.5 * (x1 + x2), yo + 0.3))
    s.pfeil((x1, yo - 0.34), (x2, yo - 0.34), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    t(s, "U_{@{kabel}}", (0.5 * (x1 + x2), yo - 0.6), farbe=BLAU)
    ipfeil(s, (x0 + 0.3, yo), (x0 + 0.8, yo), "I", (x0 + 0.55, yo + 0.3))
    spfeil(s, x3 + 0.34, 0.5, -0.5, "U_L", seite=1, dx=0.08)
    t(s, "R_L", (x3 - 0.2, 0), "right", BRAUN)
    x = 1.3
    t(s, s.tr("gl", "gleiche Last: 40 kW", "same load: 40 kW", "misma carga: 40 kW", "相同负载：40 kW"), (x, 1.0), "left", SCHWARZ, 24)
    t(s, "U_L = 400 V", (x, 0.54), "left", ROT, 24)
    t(s, "I = 100 A", (x, 0.22), "left", ROT, 24)
    t(s, "P_{@{kabel}} = 10 kW", (x, -0.1), "left", ROT, 24)
    t(s, "U_L = 20 kV", (x, -0.52), "left", GRUEN, 24)
    t(s, "I = 2 A", (x, -0.84), "left", GRUEN, 24)
    t(s, "P_{@{kabel}} = 4 W", (x, -1.16), "left", GRUEN, 24)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k7kreis():
    """Stromkreis mit Innenwiderstand; rechts der Potenzialverlauf einer Ladung auf dem Umlauf."""
    s = Szene("et1/k7kreis")
    s.welt()
    yo, yu = 0.85, -0.85
    x0, x1 = -3.4, -0.85
    xr0, xr1, xk = -2.9, -2.05, -1.6
    uq(s, (x0, yo), (x0, yu))
    s.draht((x0, yo), (xr0, yo))
    wid(s, (xr0, yo), (xr1, yo), size=0.42)
    s.draht((xr1, yo), (xk - 0.07, yo))
    kl(s, xk, yo, "A", dy=0.28)
    kl(s, xk, yu, "B", dy=-0.3)
    s.draht((xk + 0.07, yo), (x1, yo))
    wid(s, (x1, yo), (x1, yu), size=0.42, farbe=ORANGE)
    s.draht((x1, yu), (xk + 0.07, yu))
    s.draht((xk - 0.07, yu), (x0, yu))
    spfeil(s, x0 - 0.33, 0.5, -0.5, "U_q", seite=-1, farbe=SCHWARZ, dx=0.08)
    t(s, "R_i", (0.5 * (xr0 + xr1), yo + 0.3))
    s.pfeil((xr0, yo - 0.33), (xr1, yo - 0.33), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    t(s, "U_{Ri}", (0.5 * (xr0 + xr1), yo - 0.58), farbe=BLAU)
    ipfeil(s, (xk + 0.15, yo), (xk + 0.57, yo), "I", (xk + 0.36, yo + 0.3))
    spfeil(s, x1 + 0.33, 0.5, -0.5, "U_L", seite=1, dx=0.08)
    t(s, "R_L", (x1 - 0.2, 0), "right", BRAUN)
    # Potenzial auf dem Umlauf (R_L = 16 Ω)
    a = s.achsen((0, 4, 1), (0, 10, 2), breite=2.42, hoehe=1.9, mitte=(1.76, 0.08), yl=s.tr("phi", "φ in V", "φ in V", "φ en V", "φ / V"),
                 xzahlen=False, xmarks=False, yticks="0;2;4;6;8;10")
    pts = [(0, 0), (0.6, 0), (0.9, 9), (1.5, 9), (1.8, 8), (2.8, 8), (3.1, 0), (4, 0)]
    s.band(a, 0.6, 0.9, 0, 10, farbe=GRUEN, deckung=0.12)
    s.band(a, 1.5, 1.8, 0, 10, farbe=ROT, deckung=0.12)
    s.band(a, 2.8, 3.1, 0, 10, farbe=ORANGE, deckung=0.12)
    s.daten(a, pts, farbe=SCHWARZ, dicke=4)
    s.text(a, "+9 V", (0.98, 5.2), groesse=23, farbe=GRUEN)
    s.text(a, "−1 V", (1.95, 9.2), groesse=23, farbe=ROT)
    s.text(a, "−8 V", (3.15, 5.2), groesse=23, farbe=BRAUN)
    t(s, s.tr("uml_q", "Quelle", "source", "fuente", "电源"), (1.02, -1.2), g=22, farbe=GRUEN)
    t(s, "R_i", (1.87, -1.2), g=22, farbe=ROT)
    t(s, "R_L", (2.62, -1.2), g=22, farbe=BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k7rechteck():
    """Drei Arbeitspunkte auf der Quellengeraden: Rechteck unter der Geraden = P_L, darüber = P_v."""
    s = Szene("et1/k7rechteck")
    xl = s.tr("i_a", "I in A", "I in A", "I en A", "I / A")
    yl = s.tr("u_l", "U in V", "U in V", "U en V", "U / V")
    daten_ = ((-2.36, 3.6, 1.8, "R_L = 0.5 Ω"), (0.0, 2.25, 4.5, "R_L = 2 Ω"), (2.36, 0.9, 7.2, "R_L = 8 Ω"))
    for i, (cx, ia, ul, tit) in enumerate(daten_):
        a = s.achsen((0, 4.5, 1.5), (0, 9, 3), breite=1.8, hoehe=1.72, mitte=(cx, 0), xl=xl, yl=yl if i == 0 else "", xticks="0;1.5;3;4.5", yticks="0;3;6;9",
                     yzahlen=(i == 0))
        s.band(a, 0, ia, 0, ul, farbe=BLAU, deckung=0.4)
        s.band(a, 0, ia, ul, 9, farbe=ROT, deckung=0.22)
        s.kurve(a, "9-2*x", x=(0, 4.5), farbe=BLAU, dicke=4)
        s.linie(a, (0, ul), (ia, ul), farbe=BLAU, dicke=2.5)
        s.linie(a, (ia, 0), (ia, 9), farbe=GRAU, dicke=2, dash=DASH)
        s.punkt(a, ia, ul, farbe=ROT, r=0.08)
        s.text(a, tit, (2.6, 10.5), groesse=23, farbe=SCHWARZ, ausrichtung="center")
        if i == 0:
            s.text(a, "P_L = 6.48 W", (1.8, 0.9), groesse=22, farbe=BLAU, ausrichtung="center")
            s.text(a, "P_v = 25.92 W", (1.62, 2.85), groesse=22, farbe=ROT, ausrichtung="center")
        elif i == 1:
            s.text(a, "P_L", (1.12, 3.0), groesse=22, farbe=BLAU, ausrichtung="center")
            s.text(a, "10.125 W", (1.12, 1.6), groesse=22, farbe=BLAU, ausrichtung="center")
            s.text(a, "P_v = 10.125 W", (2.32, 8.2), groesse=22, farbe=ROT)
        else:
            s.text(a, "P_L = 6.48 W", (1.95, 6.6), groesse=22, farbe=BLAU)
            s.text(a, "P_v = 1.62 W", (1.05, 8.3), groesse=22, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k7kurven():
    """Leistung und Wirkungsgrad: links über R_L/R_i, rechts über I/I_KS."""
    s = Szene("et1/k7kurven")
    pl = "P_L / P_{L,max}"
    a = s.achsen((0, 8, 1), (0, 1, 0.25), breite=2.7, hoehe=1.85, mitte=(-1.85, 0), xl="R_L / R_i", gitter=True, yticks="0;0.25;0.5;0.75;1")
    s.kurve(a, "4*x/(1+x)^2", x=(0, 8), farbe=BLAU, dicke=5)
    s.kurve(a, "x/(1+x)", x=(0, 8), farbe=ROT, dicke=5)
    s.linie(a, (1, 0), (1, 1), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, 1, 1, farbe=BLAU, r=0.09)
    s.punkt(a, 1, 0.5, farbe=ROT, r=0.09)
    s.text(a, pl, (3.2, 0.42), groesse=24, farbe=BLAU)
    s.text(a, "η", (6.6, 0.95), groesse=27, farbe=ROT, ausrichtung="center")
    s.text(a, "(1; 0.5)", (1.35, 0.3), groesse=22, farbe=ROT)
    b = s.achsen((0, 1, 0.25), (0, 1, 0.25), breite=2.4, hoehe=1.85, mitte=(2.0, 0), xl=s.tr("iks", "I / I_{KS}", "I / I_{SC}", "I / I_{CC}", "I / I_{SC}"), gitter=True, yticks="0;0.25;0.5;0.75;1", xticks="0;0.25;0.5;0.75;1")
    s.kurve(b, "4*x*(1-x)", x=(0, 1), farbe=BLAU, dicke=5)
    s.kurve(b, "1-x", x=(0, 1), farbe=ROT, dicke=5)
    s.linie(b, (0.5, 0), (0.5, 1), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(b, 0.5, 1, farbe=BLAU, r=0.09)
    s.punkt(b, 0.5, 0.5, farbe=ROT, r=0.09)
    s.text(b, "η", (0.12, 0.97), groesse=27, farbe=ROT, ausrichtung="center")
    s.text(b, pl, (1.0, 1.1), groesse=22, farbe=BLAU, ausrichtung="right")
    s.speichern()


def k7netz():
    """Original mit Parallelwiderstand und seine Ersatzquelle bei Anpassung."""
    s = Szene("et1/k7netz")
    yo, yu = 0.8, -0.8
    # links: Original
    x0, xa, xb, xc, xl = -3.25, -2.8, -1.75, -1.25, -0.75
    uq(s, (x0, yo), (x0, yu))
    s.draht((x0, yo), (xa, yo))
    wid(s, (xa, yo), (xb, yo), size=0.42)
    s.draht((xb, yo), (xc - 0.07, yo))
    kn(s, xb, yo)
    wid(s, (xb, yo), (xb, yu), size=0.42)
    s.draht((xb, yu), (x0, yu))
    kn(s, xb, yu)
    s.draht((xb, yu), (xc - 0.07, yu))
    kl(s, xc, yo, "A", dy=0.28)
    kl(s, xc, yu, "B", dy=-0.3)
    s.draht((xc + 0.07, yo), (xl, yo))
    s.draht((xc + 0.07, yu), (xl, yu))
    wid(s, (xl, yo), (xl, yu), size=0.42, farbe=ORANGE)
    t(s, "18 V", (x0 - 0.36, 0), "right")
    t(s, "R_q = 6 Ω", (0.5 * (xa + xb), yo + 0.3))
    t(s, "37.5 W", (0.5 * (xa + xb), yo - 0.3), farbe=ROT, g=22)
    t(s, "R", (xb - 0.2, 0.17), "right")
    t(s, "3 Ω", (xb - 0.2, -0.17), "right")
    t(s, "3 W", (xb + 0.16, -0.48), "left", ROT, 22)
    t(s, "R_L", (xl + 0.17, 0.17), "left", BRAUN)
    t(s, "2 Ω", (xl + 0.17, -0.17), "left", BRAUN)
    t(s, "4.5 W", (xl - 0.15, 0.0), "right", BLAU, 22)
    t(s, "η = 4.5 W / 45 W = 10 %", (-2.0, -1.5), farbe=ROT)
    s.pfeil((-0.1, 0), (0.35, 0), "", farbe=GRAU, spitze=0.24, dicke=4.5)
    # rechts: Ersatzquelle
    x0, xa, xb, xc, xl = 0.85, 1.15, 1.95, 2.4, 2.85
    uq(s, (x0, yo), (x0, yu))
    s.draht((x0, yo), (xa, yo))
    wid(s, (xa, yo), (xb, yo), size=0.42)
    s.draht((xb, yo), (xc - 0.07, yo))
    s.draht((x0, yu), (xc - 0.07, yu))
    kl(s, xc, yo, "A", dy=0.28)
    kl(s, xc, yu, "B", dy=-0.3)
    s.draht((xc + 0.07, yo), (xl, yo))
    s.draht((xc + 0.07, yu), (xl, yu))
    wid(s, (xl, yo), (xl, yu), size=0.42, farbe=ORANGE)
    t(s, "6 V", (x0 + 0.34, 0), "left")
    t(s, "R_i = 2 Ω", (0.5 * (xa + xb), yo + 0.3))
    t(s, "R_L", (xl - 0.17, 0.17), "right", BRAUN)
    t(s, "2 Ω", (xl - 0.17, -0.17), "right", BRAUN)
    t(s, s.tr("nurkl", "stimmt nur an A und B", "valid only at A and B", "válido solo en A y B", "仅在 A、B 处成立"), (1.85, -1.5), farbe=GRAU)
    s.speichern()


ALLE = (k7ladung, k7stoss, k7grenze, k7sinus, k7leitung, k7kreis, k7rechteck, k7kurven, k7netz)

if __name__ == "__main__":
    for f in ALLE:
        f()
