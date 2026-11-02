"""ET1 Teil 9 (kap9_stufen.tex): Halbleiter und Dioden.

Aufruf: python tools/szenen/et1_teil9.py, danach python tools/szenen_ansehen.py out.png et1/k9einweg ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap9.py.
"""
import sys
from math import atan2, degrees, exp, hypot, log, tanh
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

BRAUN = "#a84a22"
HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#ddf0e4"
VB_F, LB_F = "#cfe0f5", "#f4f4f4"
GR = 24           # Beschriftung in Schaltbildern
UT, IS = 0.02585, 1e-14
UAP, IAP = 0.69249, 4.3075e-3


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b; bei der Diode ist a die Anode."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def kl(s, x, y, name="", dx=0.0, dy=0.3, farbe=SCHWARZ):
    s.kreis(None, x, y, 0.07, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        s.text(None, name, (x + dx, y + dy), groesse=GR, ausrichtung="center", farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.06):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def spfeil(s, a, b, txt="", p=None, farbe=BLAU, ausr="left"):
    """Spannungspfeil von a nach b mit Text an p."""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=2.5)
    if txt:
        t(s, txt, p, ausr, farbe)


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center"):
    """Kurzer Strompfeil auf einer Leitung."""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=3)
    if txt:
        t(s, txt, p, ausr, farbe)


def ms_achse(s):
    return s.tr("t_ms", "t in ms", "t in ms", "t en ms", "t / ms")


def v_achse(s, name="u", key="u_v"):
    return s.tr(key, name + " in V", name + " in V", name + " en V", name + " / V")


# ------------------------------------------------------------------------------------------ Von Grund auf
def k9einweg():
    """Einweggleichrichter: Schaltung, Spannung am Widerstand, Spannung an der Diode."""
    s = Szene("et1/k9einweg")
    s.welt()
    xq, xr, yo, yu = -2.85, -1.0, 0.85, -0.85
    bau(s, "ac_source", (xq, yu), (xq, yo), size=0.6)
    s.draht((xq, yo), (-2.4, yo))
    bau(s, "diode", (-2.4, yo), (-1.5, yo), size=0.55)
    s.draht((-1.5, yo), (xr, yo))
    bau(s, "resistor", (xr, yo), (xr, yu), size=0.55)
    s.draht((xq, yu), (xr, yu))
    t(s, "A", (-2.37, yo + 0.3))
    t(s, "K", (-1.53, yo + 0.3))
    spfeil(s, (-2.3, yo - 0.3), (-1.6, yo - 0.3), "u_D", (-1.95, yo - 0.55), farbe=ROT, ausr="center")
    spfeil(s, (xq - 0.42, 0.6), (xq - 0.42, -0.6), "u_e", (xq - 0.5, 0.0), ausr="right")
    spfeil(s, (xr + 0.38, 0.6), (xr + 0.38, -0.6), "u_a", (xr + 0.46, 0.0))
    ipfeil(s, (-2.8, yo), (-2.5, yo), "i", (-2.68, yo + 0.3))
    t(s, "R", (xr - 0.2, 0.0), "right")
    a = s.achsen((0, 40, 10), (-15, 15, 15), breite=2.9, hoehe=1.35, mitte=(1.95, 1.0), xl="", yl=v_achse(s), xzahlen=False)
    s.kurve(a, "12*sin(2*pi*x/20)", farbe=GRAU, dicke=3, dash=DASH)
    s.kurve(a, "max(12*sin(2*pi*x/20)-0.7,0)", farbe=BLAU, dicke=5)
    s.text(a, "u_e", (35, -4), groesse=GR, farbe=GRAU, ausrichtung="center")
    s.text(a, "u_a", (15, 8), groesse=GR, farbe=BLAU, ausrichtung="center")
    b = s.achsen((0, 40, 10), (-15, 15, 15), breite=2.9, hoehe=1.35, mitte=(1.95, -1.0), xl=ms_achse(s), yl=v_achse(s, key="u_v2"))
    s.kurve(b, "min(12*sin(2*pi*x/20),0.7)", farbe=ROT, dicke=5)
    s.text(b, "u_D", (5, 8), groesse=GR, farbe=ROT, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Bänder
def elektron(s, x, y, r=0.09):
    s.kreis(None, x, y, r, farbe=BLAU, dicke=2, fuellung=BLAU, deckung=1.0)


def loch(s, x, y, r=0.09):
    s.kreis(None, x, y, r, farbe=ROT, dicke=2.5, fuellung="#ffffff", deckung=1.0)


def bandkasten(s, x, y0, y1, b, gefuellt=True):
    s.box("", (x, 0.5 * (y0 + y1)), breite=b, hoehe=y1 - y0, farbe="#6a6a6a", fuellung=VB_F if gefuellt else LB_F, deckung=1.0, dicke=2)


def k9baender():
    """Metall, Halbleiter, Isolator im Bändermodell (nicht maßstäblich)."""
    s = Szene("et1/k9baender")
    b = 1.85
    xs = (-1.45, 0.65, 2.75)
    x0 = -2.8
    s.pfeil((x0, -1.45), (x0, 1.6), "", farbe=SCHWARZ, spitze=0.2)
    t(s, "W", (x0 - 0.15, 1.45), "right")
    lb = s.tr("lb", "Leitungsband", "conduction band", "banda de conducción", "导带")
    vb = s.tr("vb", "Valenzband", "valence band", "banda de valencia", "价带")
    # Metall: ein teilweise gefülltes Band
    x = xs[0]
    t(s, s.tr("metall", "Metall", "metal", "metal", "金属"), (x, 1.75))
    bandkasten(s, x, -1.2, 1.3, b, gefuellt=False)
    s.box("", (x, -0.45), breite=b, hoehe=1.5, farbe="#6a6a6a", fuellung=VB_F, deckung=1.0, dicke=2)
    s.linie(None, (x - b / 2, 0.3), (x + b / 2, 0.3), farbe=ROT, dicke=3, dash=DASH)
    t(s, "W_F", (x + 0.7, 0.52), farbe=ROT)
    t(s, s.tr("metall_t", "besetzt", "occupied", "ocupado", "已占据"), (x, -0.45), g=22)
    t(s, s.tr("frei", "frei", "empty", "libre", "空"), (x, 0.8), g=22)
    # Halbleiter
    x = xs[1]
    t(s, s.tr("hl", "Halbleiter", "semiconductor", "semiconductor", "半导体"), (x, 1.75))
    bandkasten(s, x, 0.7, 1.3, b, gefuellt=False)
    bandkasten(s, x, -1.2, -0.4, b)
    t(s, lb, (x, 1.12), g=22)
    t(s, vb, (x, -1.0), g=22)
    s.linie(None, (x - b / 2, 0.15), (x + b / 2, 0.15), farbe=ROT, dicke=3, dash=DASH)
    t(s, "W_F", (x + 0.7, 0.37), farbe=ROT)
    for dx in (-0.45, 0.45):
        elektron(s, x + dx, 0.84)
        loch(s, x + dx, -0.54)
    s.pfeil((x - 0.1, -0.4), (x - 0.1, 0.7), "", farbe=BRAUN, spitze=0.14, dicke=2.5, doppelt=True)
    t(s, "W_g", (x - 0.2, -0.1), "right", BRAUN)
    # Isolator
    x = xs[2]
    t(s, s.tr("iso", "Isolator", "insulator", "aislante", "绝缘体"), (x, 1.75))
    bandkasten(s, x, 1.1, 1.5, b, gefuellt=False)
    bandkasten(s, x, -1.2, -0.75, b)
    t(s, lb, (x, 1.3), g=22)
    t(s, vb, (x, -0.98), g=22)
    s.linie(None, (x - b / 2, 0.175), (x + b / 2, 0.175), farbe=ROT, dicke=3, dash=DASH)
    t(s, "W_F", (x + 0.7, 0.4), farbe=ROT)
    s.pfeil((x - 0.1, -0.75), (x - 0.1, 1.1), "", farbe=BRAUN, spitze=0.14, dicke=2.5, doppelt=True)
    t(s, "W_g", (x - 0.2, -0.25), "right", BRAUN)
    t(s, s.tr("verb", "verboten", "forbidden", "prohibida", "禁带"), (x + 0.5, -0.25), g=22)
    s.speichern()


def gitter(s, cx, cy, mitte, farbe, hell, p=0.62, r=0.2):
    """3x3-Ausschnitt des Kristalls; jede Bindung zwei Linien (zwei gemeinsame Elektronen)."""
    for i in range(3):
        for j in range(3):
            x, y = cx + (i - 1) * p, cy + (j - 1) * p
            if i < 2:
                for d in (-0.05, 0.05):
                    s.linie(None, (x, y + d), (x + p, y + d), farbe=HELLGRAU, dicke=2)
            if j < 2:
                for d in (-0.05, 0.05):
                    s.linie(None, (x + d, y), (x + d, y + p), farbe=HELLGRAU, dicke=2)
    for i in range(3):
        for j in range(3):
            x, y = cx + (i - 1) * p, cy + (j - 1) * p
            z = (i == 1 and j == 1)
            s.kreis(None, x, y, r, farbe=farbe if z else GRAU, dicke=2.5 if z else 2, fuellung=hell if z else "#f0f0f0", deckung=1.0)
            t(s, mitte if z else "Si", (x, y), g=22, farbe=farbe if z else SCHWARZ)


def k9dotierung():
    """Dotierung: Kristallausschnitt und Bänder für n- und p-Typ (Bänder nicht maßstäblich, Lage bei 300 K)."""
    s = Szene("et1/k9dotierung")
    xg, x, b = -1.85, 1.75, 1.8
    yn, yp = 1.08, -1.08
    t(s, s.tr("ntyp", "n-Typ", "n-type", "tipo n", "n 型"), (xg - 1.0, yn), "right", BLAU, g=26)
    t(s, s.tr("ptyp", "p-Typ", "p-type", "tipo p", "p 型"), (xg - 1.0, yp), "right", ROT, g=26)
    gitter(s, xg, yn, "P", ORANGE, "#fde8df")
    elektron(s, xg + 0.3, yn + 0.3, r=0.08)
    s.kreis(None, xg, yn, 0.42, farbe=BLAU, dicke=2, dash="5,5")
    t(s, s.tr("fuenft", "fünftes Elektron", "fifth electron", "quinto electrón", "第五个电子"), (xg + 0.95, yn + 0.8), "left", BLAU, g=22)
    s.pfeil((xg + 0.93, yn + 0.72), (xg + 0.38, yn + 0.36), "", farbe=BLAU, spitze=0.14, dicke=2)
    gitter(s, xg, yp, "B", GRUEN, HELLGRUEN)
    loch(s, xg + 0.31, yp, r=0.08)
    t(s, s.tr("fehl", "fehlendes Elektron", "missing electron", "electrón ausente", "缺一个电子"), (xg + 0.95, yp - 0.8), "left", ROT, g=22)
    s.pfeil((xg + 0.93, yp - 0.72), (xg + 0.37, yp - 0.09), "", farbe=ROT, spitze=0.14, dicke=2)
    # Bänder n: Das Donatorniveau liegt dicht unter dem LB, W_F bei 300 K etwas tiefer
    bandkasten(s, x, yn + 0.45, yn + 0.85, b, gefuellt=False)
    bandkasten(s, x, yn - 0.85, yn - 0.45, b)
    t(s, s.tr("lb", "LB", "CB", "BC", "导带"), (x + 0.68, yn + 0.65), g=22)
    t(s, s.tr("vb", "VB", "VB", "BV", "价带"), (x + 0.68, yn - 0.65), g=22)
    s.linie(None, (x - b / 2, yn + 0.3), (x + b / 2, yn + 0.3), farbe=ORANGE, dicke=3)
    t(s, "W_D", (x + b / 2 + 0.08, yn + 0.34), "left", ORANGE)
    s.linie(None, (x - b / 2, yn + 0.1), (x + b / 2, yn + 0.1), farbe=ROT, dicke=2.5, dash=DASH)
    t(s, "W_F", (x + b / 2 + 0.08, yn + 0.04), "left", ROT)
    for dx in (-0.7, -0.25, 0.2):
        s.pfeil((x + dx, yn + 0.3), (x + dx, yn + 0.54), "", farbe=BLAU, spitze=0.11, dicke=2)
        elektron(s, x + dx, yn + 0.6, r=0.07)
    # Bänder p
    bandkasten(s, x, yp + 0.45, yp + 0.85, b, gefuellt=False)
    bandkasten(s, x, yp - 0.85, yp - 0.45, b)
    t(s, "@lb", (x + 0.68, yp + 0.65), g=22)
    t(s, "@vb", (x + 0.68, yp - 0.65), g=22)
    s.linie(None, (x - b / 2, yp - 0.3), (x + b / 2, yp - 0.3), farbe=GRUEN, dicke=3)
    t(s, "W_A", (x + b / 2 + 0.08, yp - 0.34), "left", GRUEN)
    s.linie(None, (x - b / 2, yp - 0.1), (x + b / 2, yp - 0.1), farbe=ROT, dicke=2.5, dash=DASH)
    t(s, "W_F", (x + b / 2 + 0.08, yp - 0.04), "left", ROT)
    for dx in (-0.7, -0.25, 0.2):
        s.pfeil((x + dx, yp - 0.54), (x + dx, yp - 0.3), "", farbe=BLAU, spitze=0.11, dicke=2)
        loch(s, x + dx, yp - 0.6, r=0.07)
    s.speichern()


# ------------------------------------------------------------------------------------------ Raumladungszone
def ion(s, x, y, plus):
    f = BLAU if plus else ROT      # feste Donatoren +, feste Akzeptoren −: Farbe nach dem Gebiet, in dem sie sitzen
    s.box("+" if plus else "−", (x, y), breite=0.25, hoehe=0.25, form="rect", groesse=22, farbe=f, fuellung="#ffffff", deckung=1.0, dicke=2)


def k9rlz():
    """pn-Übergang im Gleichgewicht: Ladungsverteilung und Potenzial (Rechenmodell, w = 0,43 µm)."""
    s = Szene("et1/k9rlz")
    s.welt()
    m = 2.75 / 0.6            # Einheiten je µm (x = 0 ist die Grenzfläche)
    xl, xr = -2.75, 2.75
    y0, y1 = 0.6, 2.0
    wh = 0.215 * m
    s.box("", (0.5 * (xl - wh), 0.5 * (y0 + y1)), breite=-xl - wh, hoehe=y1 - y0, farbe="#6a6a6a", fuellung=HELLROT, deckung=1.0, dicke=2)
    s.box("", (0.5 * (xr + wh), 0.5 * (y0 + y1)), breite=xr - wh, hoehe=y1 - y0, farbe="#6a6a6a", fuellung=HELLBLAU, deckung=1.0, dicke=2)
    s.box("", (0, 0.5 * (y0 + y1)), breite=2 * wh, hoehe=y1 - y0, farbe="#6a6a6a", fuellung="#ffffff", deckung=1.0, dicke=2)
    s.linie(None, (0, y0), (0, y1), farbe=GRAU, dicke=2, dash=DASH)
    ys = (0.85, 1.3, 1.75)
    for k, y in enumerate(ys):
        for x in (-2.5, -1.9, -1.3):
            ion(s, x - 0.08, y, False)
            loch(s, x + 0.22, y + (0.09 if k != 1 else -0.09), r=0.09)
        ion(s, -0.68, y, False)
        ion(s, -0.28, y, False)
        ion(s, 0.28, y, True)
        ion(s, 0.68, y, True)
        for x in (1.3, 1.9, 2.5):
            ion(s, x + 0.08, y, True)
            elektron(s, x - 0.22, y + (0.09 if k != 1 else -0.09), r=0.09)
    t(s, "p", (xl - 0.15, 0.5 * (y0 + y1)), "right", ROT, g=26)
    t(s, "n", (xr + 0.15, 0.5 * (y0 + y1)), "left", BLAU, g=26)
    t(s, s.tr("neutral", "neutral", "neutral", "neutro", "中性"), (-1.9, 2.22), g=22, farbe=GRAU)
    t(s, s.tr("neutral", "neutral", "neutral", "neutro", "中性"), (1.9, 2.22), g=22, farbe=GRAU)
    t(s, s.tr("rlz", "Raumladungszone", "space-charge region", "zona de carga espacial", "空间电荷区"), (0, 2.56), g=22)
    s.pfeil((0.6, 2.25), (-0.6, 2.25), "", farbe=GRUEN, spitze=0.18, dicke=3.5)
    t(s, "E", (0.75, 2.25), "left", GRUEN)
    a = s.achsen((-0.6, 0.6, 0.2), (0, 0.8, 0.4), breite=5.5, hoehe=1.6, mitte=(0, -0.95),
                 xl=s.tr("x_um", "x in µm", "x in µm", "x en µm", "x / µm"), yl=s.tr("phi_v", "φ in V", "φ in V", "φ en V", "φ / V"), xl_mitte=False)
    U, wn = 0.71426, 0.215

    def phi(x):
        if x <= -wn:
            return 0.0
        if x >= wn:
            return U
        return 0.5 * U * ((x + wn) / wn) ** 2 if x < 0 else U - 0.5 * U * ((wn - x) / wn) ** 2
    pts = [(-0.6 + 1.2 * k / 240, phi(-0.6 + 1.2 * k / 240)) for k in range(241)]
    s.daten(a, pts, farbe=BLAU, dicke=5)
    s.linie(a, (-0.6, U), (0.6, U), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(None, (-wh, y0), (-wh, -1.75), farbe=GRAU, dicke=1.5, dash=DOT)
    s.linie(None, (wh, y0), (wh, -1.75), farbe=GRAU, dicke=1.5, dash=DOT)
    t(s, "U_{D0} = 0.71 V", (-1.75, -0.55), farbe=BLAU)
    s.pfeil((-wh, 0.32), (wh, 0.32), "", farbe=SCHWARZ, spitze=0.15, dicke=2, doppelt=True)
    t(s, "w = 0.43 µm", (wh + 0.1, 0.32), "left", g=22)
    s.speichern()


def k9barriere():
    """Elektronenenergie über dem Ort für U < 0, U = 0, U > 0: Wie viele Elektronen kommen über die Barriere?"""
    s = Szene("et1/k9barriere")
    s.welt()
    breite, y0 = 2.05, -1.25
    panels = ((-2.35, 2.0, s.tr("sperr", "Sperrrichtung, U < 0", "reverse, U < 0", "inversa, U < 0", "反向，U < 0"), 0.0),
              (0.0, 1.03, "U = 0", 0.45),
              (2.3, 0.55, s.tr("durch", "Durchlass, U > 0", "forward, U > 0", "directa, U > 0", "正向，U > 0"), 1.3))
    zeilen = (7, 5, 3, 2, 1, 1)     # Elektronen je Energiezeile: jede Zeile höher enthält weniger
    dy = 0.19
    for cx, h, titel, lrot in panels:
        pts = []
        for k in range(101):
            u = -1 + 2 * k / 100
            pts.append((cx + u * breite / 2, y0 + 0.5 * h * (1 - tanh(3.2 * u))))
        s.daten(None, pts, farbe=SCHWARZ, dicke=4)
        t(s, titel, (cx, 1.3), g=22)
        t(s, "p", (cx - 0.9, y0 - 0.25), farbe=ROT)
        t(s, "n", (cx + 0.9, y0 - 0.25), farbe=BLAU)
        ytop = y0 + h
        s.linie(None, (cx - 0.5, ytop), (cx + breite / 2 + 0.03, ytop), farbe=GRAU, dicke=2, dash=DASH)
        s.pfeil((cx + 1.1, y0 + 0.02), (cx + 1.1, ytop - 0.02), "", farbe=BRAUN, spitze=0.12, dicke=2.5, doppelt=True)
        t(s, "W_B", (cx + 1.08, max(ytop + 0.18, y0 + 1.28)), g=22, farbe=BRAUN)
        for j, n in enumerate(zeilen):
            y = y0 + 0.1 + j * dy
            for i in range(n):
                x = cx + 0.98 - i * 0.135
                s.kreis(None, x, y, 0.055, farbe=ROT if y > ytop else BLAU, dicke=2, fuellung=ROT if y > ytop else BLAU, deckung=1.0)
        # Minderheit auf der p-Seite läuft die Stufe hinab
        s.kreis(None, cx - 0.85, ytop + 0.1, 0.055, farbe=BLAU, dicke=2, fuellung=BLAU, deckung=1.0)
        s.pfeil((cx - 0.75, ytop + 0.1), (cx - 0.3, ytop + 0.1), "", farbe=BLAU, spitze=0.13, dicke=2.5)
        if lrot:
            s.pfeil((cx + 0.82, ytop + 0.24), (cx + 0.82 - lrot, ytop + 0.24), "", farbe=ROT, spitze=0.15, dicke=3.5)
    s.speichern()


# ------------------------------------------------------------------------------------------ Kennlinie
def k9kennlinie():
    """Aufbau und Schaltzeichen, Kennlinie linear und halblogarithmisch."""
    s = Szene("et1/k9kennlinie")
    s.welt()
    x = -3.3
    s.box("p", (x, 0.55), breite=0.72, hoehe=0.65, farbe="#6a6a6a", fuellung=HELLROT, groesse=26, dicke=2)
    s.box("n", (x, -0.1), breite=0.72, hoehe=0.65, farbe="#6a6a6a", fuellung=HELLBLAU, groesse=26, dicke=2)
    s.linie(None, (x, 0.875), (x, 1.2), dicke=3)
    s.linie(None, (x, -0.425), (x, -0.75), dicke=3)
    kl(s, x, 1.25, "A", dx=0.0, dy=0.28)
    kl(s, x, -0.8, "K", dx=0.0, dy=-0.28)
    xd = -2.5
    kl(s, xd, 1.25, "A", dx=0.0, dy=0.28)
    kl(s, xd, -0.8, "K", dx=0.0, dy=-0.28)
    bau(s, "diode", (xd, 1.18), (xd, -0.73), size=0.6)
    ipfeil(s, (xd, 1.12), (xd, 0.72), "I", (xd - 0.14, 0.92), ausr="right")
    spfeil(s, (xd + 0.3, 0.8), (xd + 0.3, -0.35), "U", (xd + 0.38, 0.2))
    a = s.achsen((-0.2, 0.8, 0.2), (-2, 10, 2), breite=1.9, hoehe=2.6, mitte=(-0.4, 0.15), xl=v_achse(s, "U", "uu_v"), yl=s.tr("i_ma", "I in mA", "I in mA", "I en mA", "I / mA"), xticks="0;0.2;0.4;0.6;0.8")
    pts = [(-0.2 + 0.94 * k / 300, 1e3 * IS * (exp((-0.2 + 0.94 * k / 300) / UT) - 1)) for k in range(301)]
    s.daten(a, pts, farbe=BLAU, dicke=5)
    s.linie(a, (-0.2, 0), (0.8, 0), farbe=GRAU, dicke=1.5)
    s.text(a, s.tr("scheinbar", "scheinbarer Knick", "apparent knee", "codo aparente", "表观拐点"), (0.55, 4.0), groesse=22, ausrichtung="right", farbe=GRAU)
    b = s.achsen((0, 0.8, 0.2), (1e-14, 1e-1), breite=1.9, hoehe=2.6, mitte=(2.25, 0.15), xl=v_achse(s, "U", "uu_v2"), yl=s.tr("i_a", "I in A", "I in A", "I en A", "I / A"), ylog=True, yticks="1e-14;1e-12;1e-10;1e-8;1e-6;1e-4;1e-2", xticks="0;0.2;0.4;0.6;0.8")
    pts = []
    for k in range(1, 321):
        u = 0.8 * k / 320
        i = IS * (exp(u / UT) - 1)
        if 1e-14 <= i <= 1e-1:
            pts.append((u, i))
    s.daten(b, pts, farbe=BLAU, dicke=5)
    for u, i in ((0.6547, 1e-3), (0.7142, 1e-2)):
        s.punkt(b, u, i, farbe=ROT, r=0.07)
    s.text(b, "1 mA", (0.6, 1e-3), groesse=22, ausrichtung="right", farbe=ROT)
    s.text(b, s.tr("dek", "Faktor 10", "factor of 10", "factor 10", "10 倍"), (0.79, 1e-9), groesse=22, ausrichtung="right", farbe=ROT)
    s.text(b, s.tr("dek2", "je 60 mV", "per 60 mV", "por 60 mV", "每 60 mV"), (0.79, 1.6e-11), groesse=22, ausrichtung="right", farbe=ROT)
    s.speichern()


def k9spezial():
    """Zener-Diode, Kapazitätsdiode, Photodiode und Solarzelle."""
    s = Szene("et1/k9spezial")
    s.welt()
    breite, hoehe, yo = 1.55, 1.8, 1.3
    xs = (-2.3, 0.1, 2.45)
    a = s.achsen((-7, 1, 1), (-40, 20, 20), breite=breite, hoehe=hoehe, mitte=(xs[0], yo), xl=v_achse(s, "U", "uu_v3"), yl=s.tr("i_ma3", "I in mA", "I in mA", "I en mA", "I / mA"),
                 xticks="-6;-4;-2;0", yticks="-40;-20;0;20")
    Uz, rz, d = 5.1, 10.0, 0.02

    def iz(u):
        i = IS * (exp(min(u, 0.85) / UT) - 1)
        x = (-u - Uz) / d
        return i * 1e3 - 1e3 * d / rz * log(1 + exp(x)) if x < 40 else i * 1e3 - 1e3 * (-u - Uz) / rz
    pts = [(-7 + 7.8 * k / 400, iz(-7 + 7.8 * k / 400)) for k in range(401)]
    s.daten(a, [p for p in pts if p[1] < 20], farbe=BLAU, dicke=5)
    s.linie(a, (-7, 0), (1, 0), farbe=GRAU, dicke=1.5)
    s.text(a, "−U_Z", (-5.1, 9), groesse=22, ausrichtung="center", farbe=ROT)
    s.linie(a, (-5.1, 0), (-5.1, -36), farbe=ROT, dicke=2, dash=DASH)
    b = s.achsen((0, 25, 5), (0, 250, 50), breite=breite, hoehe=hoehe, mitte=(xs[1], yo), xl=s.tr("ur", "U_R in V", "U_R in V", "U_R en V", "U_R / V"), yl=s.tr("c_pf", "C in pF", "C in pF", "C en pF", "C / pF"),
                 xticks="0;10;20", yticks="0;100;200")
    s.kurve(b, "241/sqrt(1+x/0.714)", farbe=BLAU, dicke=5)
    s.punkt(b, 0, 241, farbe=ROT, r=0.07)
    s.punkt(b, 25, 40.2, farbe=ROT, r=0.07)
    s.text(b, "241 pF", (2.5, 225), groesse=22, ausrichtung="left", farbe=ROT)
    s.text(b, "40 pF", (25, 75), groesse=22, ausrichtung="right", farbe=ROT)
    c = s.achsen((0, 0.6, 0.2), (-3.5, 0.5, 1), breite=breite, hoehe=hoehe, mitte=(xs[2], yo), xl=v_achse(s, "U", "uu_v4"), yl=s.tr("i_a4", "I in A", "I in A", "I en A", "I / A"), yticks="-3;-2;-1;0", xticks="0;0.2;0.4;0.6")
    for ip, f in ((0.3, HELLGRAU), (1.0, GRAU), (3.0, BLAU)):
        pts = []
        for k in range(241):
            u = 0.6 * k / 240
            i = 1e-9 * (exp(u / UT) - 1) - ip
            if i < 0.5:
                pts.append((u, i))
        s.daten(c, pts, farbe=f, dicke=4.5)
    s.linie(c, (0, 0), (0.6, 0), farbe=GRAU, dicke=1.5)
    s.text(c, "I_{Ph} = 3 A", (0.03, -2.6), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(c, "1 A", (0.03, -0.62), groesse=22, ausrichtung="left", farbe=GRAU)
    # Schaltzeichen unten
    yt, yu = -0.92, -1.55
    t(s, s.tr("zener", "Zener-Diode", "Zener diode", "diodo Zener", "齐纳二极管"), (xs[0], yt), g=22)
    t(s, s.tr("kap", "Kapazitätsdiode", "varactor diode", "diodo varicap", "变容二极管"), (xs[1], yt), g=22)
    t(s, s.tr("solar", "Photodiode, Solarzelle", "photodiode, solar cell", "fotodiodo, célula solar", "光电二极管、太阳能电池"), (xs[2] - 0.05, yt), g=22)
    bau(s, "zener", (xs[0] - 0.5, yu), (xs[0] + 0.5, yu), size=0.55)
    t(s, "A", (xs[0] - 0.62, yu), "right")
    t(s, "K", (xs[0] + 0.62, yu), "left")
    bau(s, "diode", (xs[1] - 0.8, yu), (xs[1] + 0.05, yu), size=0.5)
    bau(s, "capacitor", (xs[1] + 0.05, yu), (xs[1] + 0.7, yu), size=0.5)
    t(s, "A", (xs[1] - 0.92, yu), "right")
    t(s, "K", (xs[1] + 0.82, yu), "left")
    x0, x1 = xs[2] - 0.75, xs[2] + 0.1
    y1, y2 = yu + 0.42, yu - 0.5
    bau(s, "isource", (x0, y2), (x0, y1), size=0.38)
    bau(s, "diode", (x1, y1), (x1, y2), size=0.38)
    s.draht((x0, y1), (x1 + 0.45, y1))
    s.draht((x0, y2), (x1 + 0.45, y2))
    kn(s, x1, y1)
    kn(s, x1, y2)
    kl(s, x1 + 0.52, y1, "A", dx=0.26, dy=0.0)
    kl(s, x1 + 0.52, y2, "K", dx=0.26, dy=0.0)
    t(s, "I_{Ph}", (x0 - 0.27, yu - 0.04), "right", g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Arbeitspunkt
def k9arbeitsgerade():
    """Schaltung und grafische Bestimmung des Arbeitspunkts."""
    s = Szene("et1/k9arbeitsgerade")
    s.welt()
    xq, xd, yo, yu = -3.0, -1.25, 0.85, -1.05
    bau(s, "vsource", (xq, yu), (xq, yo), size=0.6)
    t(s, "+", (xq + 0.28, yo - 0.22), farbe=ROT)
    s.draht((xq, yo), (-2.7, yo))
    bau(s, "resistor", (-2.7, yo), (-1.8, yo), size=0.5)
    s.draht((-1.8, yo), (xd, yo))
    bau(s, "diode", (xd, yo), (xd, yu), size=0.6)
    s.draht((xq, yu), (xd, yu))
    t(s, "U_0", (xq - 0.4, 0.05), "right")
    t(s, "5 V", (xq - 0.4, -0.28), "right", g=22)
    t(s, "R = 1 kΩ", (-2.28, yo + 0.32), g=22)
    spfeil(s, (xd + 0.36, 0.45), (xd + 0.36, -0.65), "U_D", (xd + 0.44, -0.1), farbe=BLAU)
    ipfeil(s, (-1.72, yo), (-1.4, yo), "I", (-1.55, yo + 0.3))
    a = s.achsen((0, 5, 1), (0, 6, 1), breite=3.15, hoehe=2.6, mitte=(1.7, 0), gitter=True, xl=s.tr("ud", "U_D in V", "U_D in V", "U_D en V", "U_D / V"), yl=s.tr("id", "I in mA", "I in mA", "I en mA", "I / mA"))
    s.kurve(a, "5-x", x=(0, 5), farbe=ROT, dicke=4)
    s.kurve(a, "4*x", x=(0, 1.5), farbe=GRUEN, dicke=4)
    x1 = UT * log(6e-3 / IS + 1)
    s.kurve(a, "1e-11*(exp(x/0.02585)-1)", x=(0.0, x1), farbe=BLAU, dicke=5)
    s.punkt(a, UAP, IAP * 1e3, farbe=SCHWARZ, r=0.09)
    s.punkt(a, 1.0, 4.0, farbe=SCHWARZ, r=0.09)
    s.punkt(a, 0, 5, farbe=ROT, r=0.08)
    s.punkt(a, 5, 0, farbe=ROT, r=0.08)
    s.text(a, s.tr("ks", "Kurzschluss: 5 mA", "short circuit: 5 mA", "cortocircuito: 5 mA", "短路：5 mA"), (4.95, 5.5), groesse=22, farbe=ROT, ausrichtung="right")
    s.text(a, s.tr("ll", "Leerlauf: 5 V", "no load: 5 V", "sin carga: 5 V", "开路：5 V"), (4.95, 2.1), groesse=22, farbe=ROT, ausrichtung="right")
    s.text(a, s.tr("ag", "Arbeitsgerade", "load line", "recta de carga", "负载线"), (2.55, 3.2), groesse=22, farbe=ROT, ausrichtung="left")
    s.text(a, "(0.69 V | 4.31 mA)", (1.05, 1.55), groesse=22, farbe=BLAU, ausrichtung="left")
    s.text(a, "(1 V | 4 mA)", (1.35, 4.5), groesse=22, farbe=GRUEN, ausrichtung="left")
    s.speichern()


def k9ersatz():
    """Kennlinie und Modelle, Ersatzschaltungen, Beispiel mit zwei Dioden."""
    s = Szene("et1/k9ersatz")
    s.welt()
    a = s.achsen((-0.4, 1.0, 0.2), (-1, 6, 1), breite=2.5, hoehe=1.95, mitte=(-1.85, 1.3), xl=v_achse(s, "U_D", "ud_v5"), yl=s.tr("id5", "I_D in mA", "I_D in mA", "I_D en mA", "I_D / mA"), xticks="-0.4;0;0.4;0.7", yticks="0;2;4;6", xl_mitte=False)
    s.linie(a, (-0.4, 0), (1.0, 0), farbe=GRAU, dicke=1.5)
    s.kurve(a, "1e-11*(exp(x/0.02585)-1)", x=(-0.4, 0.7126), farbe=BLAU, dicke=5)
    s.linie(a, (0, 0), (0, 6), farbe=GRUEN, dicke=3.5, dash=DASH)
    s.linie(a, (0.7, 0), (0.7, 6), farbe=ROT, dicke=3.5, dash=DASH)
    s.linie(a, (-0.4, 0), (0.7, 0), farbe=ROT, dicke=3.5, dash=DASH)
    yt, yi, yf = 2.3, 1.72, 0.72
    x1, x2, x3, x4 = 1.45, 2.1, 2.55, 3.2
    t(s, s.tr("leitet", "leitet", "conducts", "conduce", "导通"), (0.5 * (x1 + x2), yt), g=22)
    t(s, s.tr("sperrt", "sperrt", "blocks", "bloquea", "截止"), (0.5 * (x3 + x4), yt), g=22)
    t(s, s.tr("ideal", "ideal", "ideal", "ideal", "理想"), (0.42, yi), "left", GRUEN, g=22)
    t(s, s.tr("mituf", "mit U_F", "with U_F", "con U_F", "含 U_F"), (0.42, yf), "left", ROT, g=22)
    for y in (yi, yf):
        kl(s, x1, y, "A", dx=0.0, dy=0.27)
        kl(s, x2, y, "K", dx=0.0, dy=0.27)
        kl(s, x3, y, "A", dx=0.0, dy=0.27)
        kl(s, x4, y, "K", dx=0.0, dy=0.27)
    s.draht((x1 + 0.07, yi), (x2 - 0.07, yi))
    s.draht((x1 + 0.07, yf), (x1 + 0.13, yf))
    s.draht((x2 - 0.13, yf), (x2 - 0.07, yf))
    bau(s, "vsource", (x2 - 0.13, yf), (x1 + 0.13, yf), size=0.36)
    t(s, "U_F", (0.5 * (x1 + x2), yf - 0.33), g=22)
    yo, yu, ym = -0.55, -1.65, -1.1
    ax = -3.1
    kl(s, ax, yo, "5 V", dx=-0.32, dy=0.0)
    kl(s, ax, yu, "2 V", dx=-0.32, dy=0.0)
    bau(s, "resistor", (ax + 0.07, yo), (-2.15, yo), size=0.42)
    bau(s, "resistor", (ax + 0.07, yu), (-2.15, yu), size=0.42)
    t(s, "R_1 = 1 kΩ", (-2.6, yo + 0.3), g=22)
    t(s, "R_2 = 1 kΩ", (-2.6, yu - 0.3), g=22)
    s.draht((-2.15, yo), (-1.75, yo))
    s.draht((-2.15, yu), (-1.75, yu))
    bau(s, "diode", (-1.75, yo), (-0.9, yo), size=0.5)
    bau(s, "diode", (-1.75, yu), (-0.9, yu), size=0.5)
    t(s, "D_1", (-1.3, yo + 0.32))
    t(s, "D_2", (-1.3, yu - 0.32))
    s.draht((-0.9, yo), (-0.5, yo), (-0.5, yu), (-0.9, yu))
    kn(s, -0.5, ym)
    t(s, "X", (-0.42, ym + 0.2), "left")
    s.draht((-0.5, ym), (0.0, ym))
    bau(s, "resistor", (0.0, ym), (0.85, ym), size=0.42)
    t(s, "R_3 = 2 kΩ", (0.42, ym + 0.32), g=22)
    s.draht((0.85, ym), (1.0, ym), (1.0, ym - 0.22))
    s.geraet("ground", (1.0, ym - 0.22), groesse=0.6)
    tx = 1.4
    t(s, s.tr("d1l", "D_1 leitet: 1.43 mA", "D_1 conducts: 1.43 mA", "D_1 conduce: 1.43 mA", "D_1 导通：1.43 mA"), (tx, -0.65), "left", ROT, g=22)
    t(s, s.tr("d2s", "D_2 sperrt: −0.87 V", "D_2 blocks: −0.87 V", "D_2 bloquea: −0.87 V", "D_2 截止：−0.87 V"), (tx, -1.05), "left", g=22)
    t(s, "φ_X = 2.87 V", (tx, -1.45), "left", BLAU, g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Kleinsignal
def k9kleinsignal():
    """Tangente im Arbeitspunkt und Kleinsignal-Ersatzschaltbild."""
    s = Szene("et1/k9kleinsignal")
    s.welt()
    a = s.achsen((0.66, 0.72, 0.02), (0, 10, 2), breite=2.85, hoehe=2.6, mitte=(-1.8, 0), gitter=True, xl=s.tr("ud6", "U_D in V", "U_D in V", "U_D en V", "U_D / V"), yl=s.tr("id6", "I in mA", "I in mA", "I en mA", "I / mA"))
    s.kurve(a, "1e-11*(exp(x/0.02585)-1)", x=(0.66, 0.7138), farbe=BLAU, dicke=5)
    r = UT / IAP
    s.kurve(a, f"{IAP * 1e3}+1000*(x-{UAP})/{r}", x=(0.6667, 0.72), farbe=ROT, dicke=3.5, dash=DASH)
    s.punkt(a, UAP, IAP * 1e3, farbe=SCHWARZ, r=0.09)
    s.text(a, s.tr("ap", "AP", "OP", "PT", "工作点"), (0.687, 5.0), groesse=24, ausrichtung="center")
    s.text(a, s.tr("tang", "Tangente", "tangent", "tangente", "切线"), (0.7195, 5.2), groesse=22, ausrichtung="right", farbe=ROT)
    s.text(a, "1/r", (0.7195, 4.2), groesse=22, ausrichtung="right", farbe=ROT)
    xq, xd, yo, yu = 0.9, 2.75, 0.85, -1.05
    t(s, s.tr("klein", "Kleinsignal", "small signal", "pequeña señal", "小信号"), (1.85, 1.45), g=24)
    bau(s, "ac_source", (xq, yu), (xq, yo), size=0.6)
    s.draht((xq, yo), (1.25, yo))
    bau(s, "resistor", (1.25, yo), (2.15, yo), size=0.5)
    s.draht((2.15, yo), (xd, yo))
    bau(s, "resistor", (xd, yo), (xd, yu), size=0.5)
    s.draht((xq, yu), (xd, yu))
    t(s, "u", (xq - 0.38, -0.05), "right")
    t(s, "R", (1.7, yo + 0.32), g=24)
    t(s, "r", (xd - 0.25, -0.05), "right", ROT)
    spfeil(s, (xd + 0.34, 0.5), (xd + 0.34, -0.7), "u_D", (xd + 0.44, -0.1), farbe=BLAU)
    ipfeil(s, (2.25, yo), (2.55, yo), "i", (2.42, yo + 0.3))
    s.speichern()


# ------------------------------------------------------------------------------------------ Gleichrichter
def bruecke(s, cx, cy, pos, d=1.0):
    """Graetz-Brücke mit Last in der Mitte; pos=True: positive Halbwelle, sonst negative. Die leitenden Dioden sind farbig."""
    f = ROT if pos else BLAU
    a, b, oben, unten = (cx - d, cy), (cx + d, cy), (cx, cy + d), (cx, cy - d)
    an = {"1": pos, "2": not pos, "3": pos, "4": not pos}
    grau = HELLGRAU
    bau(s, "diode", a, oben, size=0.42, farbe=f if an["1"] else grau)
    bau(s, "diode", b, oben, size=0.42, farbe=f if an["2"] else grau)
    bau(s, "diode", unten, b, size=0.42, farbe=f if an["3"] else grau)
    bau(s, "diode", unten, a, size=0.42, farbe=f if an["4"] else grau)
    bau(s, "resistor", oben, unten, size=0.42, farbe=f)
    t(s, "D_1", (cx - 0.72, cy + 0.72), g=22, farbe=f if an["1"] else GRAU)
    t(s, "D_2", (cx + 0.72, cy + 0.72), g=22, farbe=f if an["2"] else GRAU)
    t(s, "D_3", (cx + 0.72, cy - 0.72), g=22, farbe=f if an["3"] else GRAU)
    t(s, "D_4", (cx - 0.72, cy - 0.72), g=22, farbe=f if an["4"] else GRAU)
    # Quelle unten um die Brücke herum
    yq = cy - d - 0.32
    s.draht(a, (cx - d, yq), (cx - 0.3, yq))
    s.draht((cx + 0.3, yq), (cx + d, yq), b)
    bau(s, "ac_source", (cx - 0.3, yq), (cx + 0.3, yq), size=0.42)
    kn(s, a[0], a[1])
    kn(s, b[0], b[1])
    kn(s, oben[0], oben[1])
    kn(s, unten[0], unten[1])
    s.pfeil((cx + 0.27, cy + 0.42), (cx + 0.27, cy - 0.42), "", farbe=BLAU, spitze=0.14, dicke=2.5)
    t(s, "u_a", (cx + 0.33, cy - 0.02), "left", BLAU, g=22)
    t(s, "R", (cx - 0.2, cy), "right", g=22, farbe=f)
    t(s, "+", (cx - d - 0.16, cy - 0.45), g=24, farbe=ROT) if pos else t(s, "+", (cx + d + 0.16, cy - 0.45), g=24, farbe=ROT)


def k9graetz():
    """Brückengleichrichter in beiden Halbwellen und Verlauf der Ausgangsspannung."""
    s = Szene("et1/k9graetz")
    s.welt()
    xl, xr, y = -1.75, 1.75, 1.75
    bruecke(s, xl, y, True)
    bruecke(s, xr, y, False)
    t(s, "u_e > 1.4 V", (xl, 0.08), g=22, farbe=ROT)
    t(s, "u_e < −1.4 V", (xr, 0.08), g=22, farbe=BLAU)
    a = s.achsen((0, 40, 10), (-12, 12, 12), breite=5.6, hoehe=1.35, mitte=(-0.05, -1.3), xl=ms_achse(s), yl=v_achse(s, key="u_v7"), xl_mitte=False, gitter=False)
    s.linie(a, (0, 0), (40, 0), farbe=GRAU, dicke=1.5)
    s.kurve(a, "12*sin(2*pi*x/20)", farbe=GRAU, dicke=3, dash=DASH)
    s.kurve(a, "max(abs(12*sin(2*pi*x/20))-1.4,0)", farbe=BLAU, dicke=5)
    s.text(a, "u_a", (15.2, 8.5), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(a, "u_e", (34, -9.5), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "10.6 V", (41, 10.6), groesse=22, ausrichtung="left", farbe=BLAU)
    s.linie(a, (0, 10.6), (40, 10.6), farbe=BLAU, dicke=1.5, dash=DOT)
    s.speichern()


def pumpe(s, cx, cy, schritt):
    """Eine Ladungspumpe; schritt=1 lädt C1, schritt=2 pumpt. Der Schalter legt die untere Platte von C1 an Masse oder an U_e."""
    f = ROT if schritt == 1 else BLAU
    y, yu = cy + 0.8, cy - 1.0
    xe, xa, xm, xc = cx - 1.6, cx + 1.56, cx - 0.1, cx + 1.25
    xs = cx - 1.2                # Abzweig zum Schalter
    ys = cy - 0.3                # Höhe des Umschalters
    kl(s, xe, y, "U_e", dx=0.0, dy=0.3)
    kl(s, xe, yu)
    kl(s, xa, y, "U_a", dx=0.0, dy=0.3)
    kl(s, xa, yu)
    s.draht((xe + 0.07, yu), (xa - 0.07, yu))
    s.draht((xe + 0.07, y), (xs, y), farbe=f)
    s.draht((xs, y), (cx - 1.05, y), farbe=f if schritt == 1 else SCHWARZ)
    bau(s, "diode", (cx - 1.05, y), (cx - 0.45, y), size=0.38, farbe=f if schritt == 1 else GRAU)
    s.draht((cx - 0.45, y), (xm, y), farbe=f if schritt == 1 else SCHWARZ)
    kn(s, xm, y, farbe=f)
    s.draht((xm, y), (cx + 0.25, y), farbe=f if schritt == 2 else SCHWARZ)
    bau(s, "diode", (cx + 0.25, y), (cx + 0.85, y), size=0.38, farbe=f if schritt == 2 else GRAU)
    s.draht((cx + 0.85, y), (xa - 0.07, y), farbe=f if schritt == 2 else SCHWARZ)
    t(s, "D_1", (cx - 0.75, y + 0.28), g=22)
    t(s, "D_2", (cx + 0.55, y + 0.28), g=22)
    bau(s, "capacitor", (xm, y), (xm, ys), size=0.42, farbe=f)
    t(s, "C_1", (xm + 0.17, 0.5 * (y + ys) + 0.08), "left", g=22)
    # Umschalter: Mittelkontakt (xm, ys), oben links der Kontakt an U_e, unten der Kontakt an Masse
    kl(s, xm, ys)
    kl(s, xs + 0.35, ys - 0.35)
    kl(s, xm, yu + 0.28)
    s.draht((xm, yu + 0.21), (xm, yu), farbe=f if schritt == 1 else SCHWARZ)
    s.draht((xs, y), (xs, ys - 0.35), (xs + 0.28, ys - 0.35), farbe=f if schritt == 2 else SCHWARZ)
    kn(s, xs, y, farbe=f)
    if schritt == 1:
        s.linie(None, (xm, ys - 0.07), (xm, yu + 0.35), dicke=3.5, farbe=f)
    else:
        s.linie(None, (xm - 0.05, ys - 0.05), (xs + 0.4, ys - 0.3), dicke=3.5, farbe=f)
    bau(s, "capacitor", (xc, y), (xc, yu), size=0.42)
    kn(s, xc, y, farbe=f if schritt == 2 else SCHWARZ)
    kn(s, xc, yu)
    t(s, "C_2", (xc - 0.17, cy - 0.1), "right", g=22)


def k9pumpe():
    """Ladungspumpe: laden und pumpen."""
    s = Szene("et1/k9pumpe")
    xl, xr = -1.75, 1.75
    pumpe(s, xl, 0.0, 1)
    pumpe(s, xr, 0.0, 2)
    t(s, s.tr("s1", "Schritt 1: C_1 laden", "step 1: charge C_1", "paso 1: cargar C_1", "第 1 步：给 C_1 充电"), (xl, 1.62), g=24, farbe=ROT)
    t(s, s.tr("s2", "Schritt 2: pumpen", "step 2: pump", "paso 2: bombear", "第 2 步：泵送"), (xr, 1.62), g=24, farbe=BLAU)
    s.speichern()


if __name__ == "__main__":
    for f in (k9einweg, k9baender, k9dotierung, k9rlz, k9barriere, k9kennlinie, k9spezial, k9arbeitsgerade, k9ersatz, k9kleinsignal, k9graetz, k9pumpe):
        f()
