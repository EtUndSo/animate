"""ET1 Teil 11 (kap11_stufen.tex): Der Operationsverstärker.

Aufruf: python tools/szenen/et1_teil11.py, danach python tools/szenen_ansehen.py out.png et1/k11diff ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap11.py.
"""
import random
import sys
from math import atan2, degrees, exp, hypot, pi, sin
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLBLAU, HELLGRAU2 = "#dceafa", "#f2f2f2"
GR = 24           # Beschriftung in Schaltbildern


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def wid(s, a, b, size=0.42, farbe=SCHWARZ):
    return bau(s, "resistor", a, b, size=size, farbe=farbe)


def kl(s, x, y, name="", dx=0.0, dy=0.25, farbe=SCHWARZ, a="center"):
    s.kreis(None, x, y, 0.06, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        s.text(None, name, (x + dx, y + dy), groesse=GR, ausrichtung=a, farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.055):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center"):
    s.pfeil(a, b, "", farbe=farbe, spitze=0.16, dicke=3)
    if txt:
        t(s, txt, p, ausr, farbe)


def achse(s, sym, einheit):
    """Achsentitel "Größe in Einheit": Das Wort "in" gehört in die Sprachtabelle."""
    key = "ax_" + "".join(c for c in sym + einheit if c.isalnum())
    return s.tr(key, f"{sym} in {einheit}", f"{sym} in {einheit}", f"{sym} en {einheit}", f"{sym} / {einheit}")


def masse(s, x, y, g=0.5):
    s.geraet("ground", (x, y), groesse=g)


def opv(s, x, y, g=0.6, plus_oben=False):
    """OPV als Dreieck um (x, y); liefert die Pins (minus, plus, ausgang)."""
    s.geraet("opamp", (x, y), groesse=g, symbol_style="amerikanisch", flip=plus_oben)
    o, u = (x - 1.5 * g, y + 0.5 * g), (x - 1.5 * g, y - 0.5 * g)
    a = (x + 1.5 * g, y)
    return (u, o, a) if plus_oben else (o, u, a)


def t_rechts(s, x, y, g):
    """npn mit der Basis rechts: Pins B, C, E."""
    s.geraet("npn", (x, y), groesse=g, drehung=180, flip=True)
    return (x + g, y), (x - 0.5 * g, y + g), (x - 0.5 * g, y - g)


def t_links(s, x, y, g):
    """npn mit der Basis links: Pins B, C, E."""
    s.geraet("npn", (x, y), groesse=g)
    return (x - g, y), (x + 0.5 * g, y + g), (x + 0.5 * g, y - g)


# ------------------------------------------------------------------------------------------ Stufe 1
def k11rauschen():
    """Links Dichte mit 1/f-Anteil (doppellogarithmisch), rechts Sinus ohne und mit Rauschen (20 dB)."""
    s = Szene("et1/k11rauschen")
    x_f = s.tr("f_hz", "f in Hz", "f in Hz", "f en Hz", "f / Hz")
    a = s.achsen((1, 1e6), (1e-16, 1e-12), breite=2.6, hoehe=2.0, mitte=(-1.9, 0.1), xl=x_f, yl=achse(s, "|u_r|^2", "V^2/Hz"),
                 xlog=True, ylog=True, gitter=True, rahmen=True)
    d = 1.657e-16
    fs = [10 ** (i * 6 / 120) for i in range(121)]
    s.daten(a, [(f, d * (1 + 1000 / f)) for f in fs], farbe=BLAU, dicke=4)
    s.daten(a, [(1, d), (1e6, d)], farbe=GRAU, dicke=3, dash=DASH)
    s.text(a, s.tr("weiss", "weiß", "white", "blanco", "白噪声"), (3e4, 3.4e-16), farbe=GRAU, ausrichtung="center")
    s.text(a, "1/f", (18, 2.5e-14), farbe=BLAU)
    xt = s.tr("per", "t in Perioden", "t in periods", "t en periodos", "t / 周期")
    gem = dict(breite=2.6, hoehe=0.86, gitter=True, rahmen=True, yticks="-1.4;0;1.4", xticks="0;1;2")
    b = s.achsen((0, 2), (-2.2, 2.2), mitte=(1.85, 0.67), xl="", yl="u/u_{s,eff}", xzahlen=False, **gem)
    s.kurve(b, "sqrt(2)*sin(2*pi*x)", farbe=BLAU, dicke=4)
    c = s.achsen((0, 2), (-2.2, 2.2), mitte=(1.85, -0.47), xl=xt, **gem)
    rnd = random.Random(11)
    s.daten(c, [(i / 300, 2 ** 0.5 * sin(2 * pi * i / 300) + rnd.gauss(0, 0.1)) for i in range(601)], farbe=BLAU, dicke=2.5)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k11diff():
    """Links Schaltung mit T1, T2, T3; rechts Stromaufteilung."""
    s = Szene("et1/k11diff")
    s.welt()
    g = 0.5
    xl, xr, yt, yr = -2.9, -1.4, 1.1, 2.55    # Kollektorlinien, Transistorhöhe, Versorgung
    b1, c1, e1 = t_links(s, xl - 0.25, yt, g)
    b2, c2, e2 = t_rechts(s, xr + 0.25, yt, g)
    s.draht((xl, yr), (xr, yr))
    kn(s, -2.15, yr)
    s.draht((-2.15, yr), (-2.15, yr + 0.18))
    kl(s, -2.15, yr + 0.24, "U_{B+} = +12 V", dx=0.16, dy=0.02, a="left")
    wid(s, (xl, yr), (xl, 1.75))
    wid(s, (xr, yr), (xr, 1.75))
    t(s, "R_C", (xl - 0.32, 2.15), "right")
    t(s, "R_C", (xr + 0.32, 2.15), "left")
    s.draht((xl, 1.75), c1)
    s.draht((xr, 1.75), c2)
    kn(s, xl, 1.68)
    kn(s, xr, 1.68)
    s.pfeil((xl + 0.14, 1.68), (xr - 0.14, 1.68), "", farbe=BLAU, spitze=0.16, dicke=2.5)
    t(s, "U_A", (-2.15, 1.9), farbe=BLAU)
    t(s, "T1", (xl - 0.15, 0.62), "right", g=23)
    t(s, "T2", (xr + 0.15, 0.62), "left", g=23)
    kl(s, b1[0] - 0.14, b1[1], "φ_−", dx=-0.1, dy=0.0, a="right")
    s.draht((b1[0] - 0.1, b1[1]), b1)
    kl(s, b2[0] + 0.14, b2[1], "φ_+", dx=0.1, dy=0.0, a="left")
    s.draht(b2, (b2[0] + 0.1, b2[1]))
    ye = 0.2
    s.draht(e1, (xl, ye), (xr, ye), e2)
    kn(s, -2.15, ye)
    t(s, "E", (-2.3, ye + 0.22), "center", g=23)
    b3, c3, e3 = t_links(s, -2.4, -0.62, g)
    s.draht((-2.15, ye), c3)
    s.draht(e3, (-2.15, -1.3))
    kl(s, -2.15, -1.36, "U_{B−} = −12 V", dx=0.16, dy=-0.02, a="left")
    kl(s, b3[0] - 0.14, b3[1], "U_{bias}", dx=-0.1, dy=0.0, a="right")
    s.draht((b3[0] - 0.1, b3[1]), b3)
    t(s, "T3", (-1.6, -0.62), "left", g=23)
    ipfeil(s, (-2.0, 0.05), (-2.0, -0.17), "I_0 = 2 mA", (-1.86, 0.0), ausr="left")
    a = s.achsen((-150, 150), (0, 2.2), breite=2.3, hoehe=2.4, mitte=(1.75, 0.55), xl=achse(s, "U_D", "mV"), yl=achse(s, "I_C", "mA"), gitter=True, rahmen=True,
                 xticks="-100;0;100", yticks="0;1;2")
    s.kurve(a, "2/(1+exp(-x/26))", farbe=BLAU, dicke=4)
    s.kurve(a, "2/(1+exp(x/26))", farbe=ROT, dicke=4)
    s.text(a, "I_{C2}", (60, 1.45), farbe=BLAU)
    s.text(a, "I_{C1}", (55, 0.42), farbe=ROT)
    s.punkt(a, 100, 1.958, farbe=BLAU, r=0.065)
    s.punkt(a, 100, 0.0418, farbe=ROT, r=0.065)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k11opv():
    """Links Schaltzeichen, rechts Kennlinie."""
    s = Szene("et1/k11opv")
    s.welt()
    g = 0.65
    m, p, o = opv(s, -2.1, 0.1, g)
    s.draht((m[0] - 0.3, m[1]), m)
    s.draht((p[0] - 0.3, p[1]), p)
    s.draht(o, (o[0] + 0.3, o[1]))
    kl(s, m[0] - 0.36, m[1], "φ_−", dx=-0.1, dy=0.0, a="right")
    kl(s, p[0] - 0.36, p[1], "φ_+", dx=-0.1, dy=0.0, a="right")
    kl(s, o[0] + 0.36, o[1], "U_A", dx=0.0, dy=0.28)
    s.draht((-2.1, 0.1 + 0.5 * g), (-2.1, 1.0))
    s.draht((-2.1, 0.1 - 0.5 * g), (-2.1, -0.8))
    kl(s, -2.1, 1.06, "U_{B+} = +12 V", dx=0.0, dy=0.26)
    kl(s, -2.1, -0.86, "U_{B−} = −12 V", dx=0.0, dy=-0.26)
    t(s, "U_D = φ_+ − φ_−", (-2.15, -1.5), farbe=BLAU)
    a = s.achsen((-300, 300), (-14, 14), breite=2.7, hoehe=2.3, mitte=(1.85, 0.1), xl=achse(s, "U_D", "μV"),
                 yl=achse(s, "U_A", "V"), gitter=True, rahmen=True, xticks="-110;0;110", yticks="-11;0;11")
    s.kurve(a, "max(-11,min(11,0.1*x))", farbe=BLAU, dicke=4)
    s.punkt(a, 110, 11, farbe=ROT, r=0.065)
    s.punkt(a, -110, -11, farbe=ROT, r=0.065)
    s.text(a, s.tr("sat", "Sättigung", "saturation", "saturación", "饱和"), (205, 8.2), ausrichtung="center", farbe=GRAU, groesse=23)
    s.text(a, s.tr("sat2", "Sättigung", "saturation", "saturación", "饱和"), (-205, -8.2), ausrichtung="center", farbe=GRAU, groesse=23)
    s.text(a, "A", (28, 2.2), farbe=BLAU)
    s.speichern()


def k11flash():
    """2-Bit-Flash-Wandler mit Abgriffen 6, 4, 2 V."""
    s = Szene("et1/k11flash")
    xt, xb, xk, g = -2.0, -0.75, 1.1, 0.42
    ys = (1.6, 0.4, -0.8)                  # Höhe der Abgriffe
    kl(s, xt, 2.1, "U_{Ref} = 6 V", dx=-0.14, dy=0.0, a="right")
    s.draht((xt, 2.04), (xt, ys[0]))
    wid(s, (xt, ys[0]), (xt, ys[1]))
    wid(s, (xt, ys[1]), (xt, ys[2]))
    wid(s, (xt, ys[2]), (xt, -1.95))
    masse(s, xt, -1.95)
    kl(s, xb, 2.1, "U_E = 3.2 V", dx=0.14, dy=0.0, a="left", farbe=BLAU)
    s.draht((xb, 2.04), (xb, ys[2] - g), farbe=BLAU)
    for y0, name, u, wert, f in zip(ys, ("K1", "K2", "K3"), ("6 V", "4 V", "2 V"), ("−11 V", "−11 V", "+11 V"), (GRAU, GRAU, ROT)):
        m, p, o = opv(s, xk, y0 - 0.5 * g, g)
        kn(s, xt, y0)
        s.draht((xt, y0), m)
        s.draht((xb, p[1]), p, farbe=BLAU)
        kn(s, xb, p[1], farbe=BLAU)
        t(s, u, (xt - 0.14, y0 + 0.02), "right")
        t(s, name, (xk - 0.1, o[1]), g=23)
        s.draht(o, (o[0] + 0.45, o[1]))
        kl(s, o[0] + 0.51, o[1], wert, dx=0.14, dy=0.0, a="left", farbe=f)
    for ya, yb in ((ys[0], ys[1]), (ys[1], ys[2]), (ys[2], -1.95)):
        t(s, "R", (xt + 0.3, 0.5 * (ya + yb)), "left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k11schleife():
    """Links Blockbild der Schleife, rechts Sprungantwort."""
    s = Szene("et1/k11schleife")
    s.welt()
    y0, yb = 0.75, -0.75
    xs, xa0, xa1, xk = -2.75, -1.95, -1.0, -0.2
    s.kreis(None, xs, y0, 0.2, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    t(s, "+", (xs - 0.34, y0 + 0.2))
    t(s, "−", (xs + 0.26, y0 - 0.34))
    s.pfeil((-3.5, y0), (xs - 0.2, y0), "", spitze=0.18)
    t(s, "U_E", (-3.45, y0 + 0.28), "left")
    s.pfeil((xs + 0.2, y0), (xa0, y0), "", spitze=0.18)
    t(s, "U_D", (0.5 * (xs + xa0) + 0.06, y0 + 0.28), farbe=ROT)
    s.box("A", (0.5 * (xa0 + xa1), y0), breite=xa1 - xa0, hoehe=0.8, farbe=BLAU, fuellung=HELLBLAU, dicke=2.5)
    s.pfeil((xa1, y0), (xk + 0.2, y0), "", spitze=0.18)
    t(s, "U_A", (xk + 0.14, y0 + 0.28), "right")
    kn(s, xk - 0.25, y0)
    s.draht((xk - 0.25, y0), (xk - 0.25, yb))
    s.pfeil((xk - 0.25, yb), (xa1, yb), "", spitze=0.18)
    s.box("β", (0.5 * (xa0 + xa1), yb), breite=xa1 - xa0, hoehe=0.7, farbe=GRUEN, fuellung="#e3f3e9", dicke=2.5)
    s.draht((xa0, yb), (xs, yb))
    s.pfeil((xs, yb), (xs, y0 - 0.2), "", spitze=0.18)
    t(s, "β U_A", (xs - 0.1, 0.5 * (y0 + yb) - 0.1), "right", GRUEN)
    a = s.achsen((0, 5), (0, 6), breite=2.65, hoehe=2.5, mitte=(2.0, 0.15), xl=achse(s, "t", "μs"),
                 yl=achse(s, "U", "V"), gitter=True, rahmen=True, xticks="0;1;2;3;4;5", yticks="0;1;2;3;4;5;6")
    s.kurve(a, "4.99975*(1-exp(-x/0.7957))", farbe=BLAU, dicke=4)
    s.kurve(a, "1-0.2*4.99975*(1-exp(-x/0.7957))", farbe=ROT, dicke=4)
    s.kurve(a, "5", farbe=GRAU, dicke=2.5, dash=DASH)
    s.text(a, "U_A", (2.0, 3.65), farbe=BLAU)
    s.text(a, "U_D", (1.3, 0.75), farbe=ROT)
    s.punkt(a, 0.7957, 3.1605, farbe=BLAU, r=0.065)
    s.text(a, "τ_G", (0.92, 2.55), farbe=SCHWARZ, groesse=23)
    s.speichern()


def k11nichtinv():
    """Nicht-invertierender Verstärker mit Potenzialen, rechts Impedanzwandler."""
    s = Szene("et1/k11nichtinv")
    g = 0.6
    x0, y0 = -1.95, 1.2
    m, p, o = opv(s, x0, y0, g, plus_oben=True)
    kl(s, p[0] - 0.42, p[1], "U_E = 1 V", dx=-0.05, dy=0.28, a="left", farbe=BLAU)
    s.draht((p[0] - 0.36, p[1]), p)
    xr = o[0] + 0.25
    s.draht(o, (xr, o[1]))
    kn(s, xr, o[1])
    s.draht((xr, o[1]), (xr + 0.3, o[1]))
    kl(s, xr + 0.36, o[1], "U_A = 4.99975 V", dx=0.12, dy=0.6, a="right", farbe=BLAU)
    ym = -0.25
    s.draht(m, (m[0], ym))
    kn(s, m[0], ym)
    wid(s, (m[0], ym), (xr, ym))
    s.draht((xr, ym), (xr, o[1]))
    t(s, "R_2 = 40 kΩ", (0.5 * (m[0] + xr) + 0.05, ym + 0.33))
    wid(s, (m[0], ym), (m[0], -1.5))
    masse(s, m[0], -1.5)
    t(s, "R_1 = 10 kΩ", (m[0] + 0.3, -1.05), "left")
    t(s, "φ_− = 0.99995 V", (m[0] + 0.1, ym - 0.24), "left", ROT, 23)
    # rechts
    g2 = 0.6
    x2, y2 = 1.8, 1.2
    m2, p2, o2 = opv(s, x2, y2, g2, plus_oben=True)
    kl(s, p2[0] - 0.42, p2[1], "U_E", dx=0.0, dy=0.28, farbe=BLAU)
    s.draht((p2[0] - 0.36, p2[1]), p2)
    xr2 = o2[0] + 0.25
    s.draht(o2, (xr2, o2[1]))
    kn(s, xr2, o2[1])
    s.draht((xr2, o2[1]), (xr2 + 0.3, o2[1]))
    kl(s, xr2 + 0.36, o2[1], "U_A", dx=0.0, dy=0.28, farbe=BLAU)
    s.draht(m2, (m2[0], 0.15), (xr2, 0.15), (xr2, o2[1]))
    t(s, "β = 1", (0.5 * (m2[0] + xr2), -0.2), farbe=GRUEN)
    t(s, "G = 0.99999", (0.5 * (m2[0] + xr2), -0.6))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k11invert():
    """Oben Schaltung mit Strompfad, unten Übersteuerung."""
    s = Szene("et1/k11invert")
    s.welt()
    g = 0.65
    x0, y0 = -0.1, 2.0
    m, p, o = opv(s, x0, y0, g)
    xe, xw = -3.3, -2.6
    xk = m[0] - 0.25
    kl(s, xe, m[1], "U_E = 1 V", dx=0.1, dy=-0.27, farbe=BLAU)
    s.draht((xe + 0.06, m[1]), (xw, m[1]), farbe=ROT)
    wid(s, (xw, m[1]), (xk, m[1]), farbe=ROT)
    s.draht((xk, m[1]), m)
    kn(s, xk, m[1])
    t(s, "R_1 = 10 kΩ", (-1.82, m[1] - 0.33))
    yt = 3.25
    xr = o[0] + 0.3
    s.draht((xk, m[1]), (xk, yt), farbe=ROT)
    wid(s, (xk, yt), (xr, yt), farbe=ROT)
    s.draht((xr, yt), (xr, o[1]), farbe=ROT)
    s.draht(o, (xr, o[1]), farbe=ROT)
    kn(s, xr, o[1])
    s.draht((xr, o[1]), (xr + 0.35, o[1]))
    kl(s, xr + 0.41, o[1], "U_A = −4 V", dx=0.13, dy=0.0, a="left", farbe=BLAU)
    t(s, "R_2 = 40 kΩ", (0.5 * (xk + xr), yt + 0.33))
    s.draht(p, (p[0] - 0.25, p[1]), (p[0] - 0.25, 1.3))
    masse(s, p[0] - 0.25, 1.3, g=0.42)
    s.pfeil((-3.05, m[1]), (-2.72, m[1]), "", farbe=ROT, spitze=0.16)
    t(s, "100 μA", (-2.85, m[1] + 0.27), farbe=ROT)
    s.pfeil((xr, 3.0), (xr, 2.55), "", farbe=ROT, spitze=0.16)
    # Weg durch den Ausgangstransistor nach U_B-
    s.linie(None, (o[0] - 0.1, o[1]), (x0 + 0.02, y0 - 0.5 * g), farbe=ROT, dicke=3, dash=DASH)
    s.draht((x0, y0 - 0.5 * g), (x0, 1.15), farbe=ROT)
    s.pfeil((x0, 1.5), (x0, 1.27), "", farbe=ROT, spitze=0.16)
    kl(s, x0, 1.09, "U_{B−} = −12 V", dx=0.14, dy=-0.03, a="left", farbe=ROT)
    t(s, s.tr("vm", "virtuelle Masse: +40 μV", "virtual ground: +40 μV", "masa virtual: +40 μV", "虚地：+40 μV"), (xk - 0.12, 3.0), "right", ROT, 23)
    # unten
    xt = s.tr("per2", "t in Perioden", "t in periods", "t en periodos", "t / 周期")
    a = s.achsen((0, 2), (-16, 16), breite=3.6, hoehe=1.7, mitte=(-1.25, -0.9), xl=xt, yl=achse(s, "u", "V"), gitter=True, rahmen=True, xticks="0;1;2",
                 yticks="-11;0;11")
    s.kurve(a, "-14*sin(2*pi*x)", farbe=GRAU, dicke=2.5, dash=DASH)
    s.kurve(a, "3.5*sin(2*pi*x)", farbe=GRUEN, dicke=3)
    s.kurve(a, "max(-11,min(11,-14*sin(2*pi*x)))", farbe=BLAU, dicke=4)
    s.text(a, "u_A", (0.42, 8.0), farbe=BLAU, ausrichtung="center")
    s.text(a, "u_E", (1.27, 6.0), farbe=GRUEN, ausrichtung="center")
    b = s.achsen((0, 2), (-1, 1), breite=2.0, hoehe=1.7, mitte=(2.25, -0.9), xl=xt, yl=achse(s, "φ_−", "V"), gitter=True, rahmen=True, xticks="0;1;2", yticks="-0.6;0;0.6")
    s.kurve(b, "2.8*sin(2*pi*x)+0.2*max(-11,min(11,-14*sin(2*pi*x)))", farbe=ROT, dicke=4)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k11addsub():
    """Addierer und Subtrahierer."""
    s = Szene("et1/k11addsub")
    g = 0.55
    # Addierer
    x0, y0 = -1.85, 0.5
    m, p, o = opv(s, x0, y0, g)
    xk = m[0] - 0.2
    s.draht((xk, m[1]), m)
    ys = (m[1] + 0.7, m[1], m[1] - 0.7)
    s.draht((xk, ys[0]), (xk, ys[2]))
    kn(s, xk, m[1])
    for yi, nm, rn in zip(ys, ("U_{E1}", "U_{E2}", "U_{E3}"), ("R_{E1}", "R_{E2}", "R_{E3}")):
        kl(s, -3.42, yi, nm, dx=-0.1, dy=0.0, a="right")
        s.draht((-3.36, yi), (-3.25, yi))
        wid(s, (-3.25, yi), (xk, yi), size=0.36)
        t(s, rn, (-3.1, yi + 0.26), g=23)
    yt = ys[0] + 0.7
    xr = o[0] + 0.2
    s.draht((xk, ys[0]), (xk, yt))
    wid(s, (xk, yt), (xr, yt), size=0.36)
    s.draht((xr, yt), (xr, o[1]))
    s.draht(o, (xr + 0.25, o[1]))
    kn(s, xr, o[1])
    kl(s, xr + 0.31, o[1], "U_A", dx=-0.02, dy=0.27)
    t(s, "R_F", (0.5 * (xk + xr), yt + 0.27))
    s.draht(p, (p[0], p[1] - 0.45))
    masse(s, p[0], p[1] - 0.45, g=0.42)
    t(s, s.tr("add", "Addierer", "summing amplifier", "sumador", "加法器"), (-2.0, -1.5), g=25)
    # Subtrahierer
    x1, y1 = 1.78, 0.5
    m1, p1, o1 = opv(s, x1, y1, g)
    xk1 = m1[0] - 0.15
    s.draht((xk1, m1[1]), m1)
    s.draht((xk1, p1[1]), p1)
    kl(s, 0.12, m1[1], "U_{E1}", dx=0.02, dy=0.27, a="center")
    s.draht((0.18, m1[1]), (0.3, m1[1]))
    wid(s, (0.3, m1[1]), (xk1, m1[1]), size=0.36)
    t(s, "R_1", (0.6, m1[1] + 0.26), g=23)
    kl(s, 0.12, p1[1], "U_{E2}", dx=0.02, dy=-0.27, a="center")
    s.draht((0.18, p1[1]), (0.3, p1[1]))
    wid(s, (0.3, p1[1]), (xk1, p1[1]), size=0.36)
    t(s, "R_3", (0.6, p1[1] - 0.26), g=23)
    kn(s, xk1, m1[1])
    kn(s, xk1, p1[1])
    yt1 = m1[1] + 0.9
    xr1 = o1[0] + 0.2
    s.draht((xk1, m1[1]), (xk1, yt1))
    wid(s, (xk1, yt1), (xr1, yt1), size=0.36)
    s.draht((xr1, yt1), (xr1, o1[1]))
    s.draht(o1, (xr1 + 0.25, o1[1]))
    kn(s, xr1, o1[1])
    kl(s, xr1 + 0.31, o1[1], "U_A", dx=-0.02, dy=0.27)
    t(s, "R_2", (0.5 * (xk1 + xr1), yt1 + 0.27))
    wid(s, (xk1, p1[1]), (xk1, p1[1] - 0.95), size=0.36)
    masse(s, xk1, p1[1] - 0.95, g=0.42)
    t(s, "R_4", (xk1 + 0.27, p1[1] - 0.5), "left", g=23)
    t(s, "1.64 V", (x1 - 0.1, m1[1] + 0.56), "center", ROT, 23)
    t(s, s.tr("sub", "Subtrahierer", "difference amplifier", "restador", "减法器"), (1.65, -1.5), g=25)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def _feld(s, cx, cy, ein, rueck, titel):
    """Kleine Grundschaltung um (cx, cy): ein und rueck sind Bauteilarten."""
    g = 0.42
    x0, y0 = cx + 0.45, cy - 0.15
    m, p, o = opv(s, x0, y0, g)
    xk = m[0] - 0.12
    xq = xk - 1.05
    kl(s, xq - 0.06, m[1], "u_E", dx=-0.02, dy=0.26)
    s.draht((xq, m[1]), (xq + 0.05, m[1]))
    bau(s, ein, (xq + 0.05, m[1]), (xk, m[1]), size=0.38)
    s.draht((xk, m[1]), m)
    kn(s, xk, m[1])
    yt = m[1] + 0.68
    xr = o[0] + 0.14
    s.draht((xk, m[1]), (xk, yt))
    bau(s, rueck, (xk, yt), (xr, yt), size=0.38)
    s.draht((xr, yt), (xr, o[1]))
    s.draht(o, (xr + 0.2, o[1]))
    kn(s, xr, o[1])
    kl(s, xr + 0.26, o[1], "u_A", dx=0.0, dy=0.26)
    s.draht(p, (p[0], p[1] - 0.3))
    masse(s, p[0], p[1] - 0.3, g=0.34)
    t(s, titel, (cx + 0.05, cy - 1.0), g=24)


def k11bauteile():
    """Integrierer, Differenzierer, Logarithmierer, Exponentialschaltung."""
    s = Szene("et1/k11bauteile")
    _feld(s, -1.85, 1.15, "resistor", "capacitor", s.tr("int", "Integrierer", "integrator", "integrador", "积分器"))
    _feld(s, 1.85, 1.15, "capacitor", "resistor", s.tr("dif", "Differenzierer", "differentiator", "derivador", "微分器"))
    _feld(s, -1.85, -1.15, "resistor", "diode", s.tr("log", "Logarithmierer", "logarithmic amplifier", "amplificador logarítmico", "对数放大器"))
    _feld(s, 1.85, -1.15, "diode", "resistor", s.tr("exp", "Exponentialschaltung", "exponential amplifier", "amplificador exponencial", "指数放大器"))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k11nic():
    """Transimpedanzverstärker und NIC."""
    s = Szene("et1/k11nic")
    g = 0.5
    # links
    x0, y0 = -1.7, 0.4
    m, p, o = opv(s, x0, y0, g)
    xk = m[0] - 0.2
    s.draht((xk, m[1]), m)
    kn(s, xk, m[1])
    xq = -3.3
    s.draht((xq, m[1]), (xk, m[1]))
    bau(s, "isource", (xq, -0.75), (xq, m[1]), size=0.46)
    masse(s, xq, -0.75, g=0.42)
    ipfeil(s, (xq + 0.15, m[1]), (xq + 0.55, m[1]), "I_E", (xq + 0.35, m[1] + 0.27))
    t(s, "2 μA", (xq + 0.3, 0.1), "left", ROT, 23)
    yt = m[1] + 0.85
    xr = o[0] + 0.2
    s.draht((xk, m[1]), (xk, yt))
    wid(s, (xk, yt), (xr, yt), size=0.36)
    s.draht((xr, yt), (xr, o[1]))
    s.draht(o, (xr + 0.25, o[1]))
    kn(s, xr, o[1])
    kl(s, xr + 0.31, o[1], "U_A", dx=-0.02, dy=0.27)
    t(s, "R = 1 MΩ", (0.5 * (xk + xr), yt + 0.27))
    t(s, "−2 V", (xr + 0.25, o[1] - 0.3), "center", BLAU, 23)
    s.draht(p, (p[0], p[1] - 0.4))
    masse(s, p[0], p[1] - 0.4, g=0.42)
    # rechts
    x1, y1 = 2.1, 0.2
    m1, p1, o1 = opv(s, x1, y1, g, plus_oben=True)
    xk1 = p1[0] - 0.25
    xr1 = o1[0] + 0.3
    yt1 = p1[1] + 0.85
    yu1 = m1[1] - 0.85
    s.draht((xk1, p1[1]), p1)
    s.draht((xk1, m1[1]), m1)
    s.draht((xk1, p1[1]), (xk1, yt1))
    s.draht((xk1, m1[1]), (xk1, yu1))
    wid(s, (xk1, yt1), (xr1, yt1), size=0.36)
    wid(s, (xk1, yu1), (xr1, yu1), size=0.36)
    s.draht((xr1, yt1), (xr1, yu1))
    s.draht(o1, (xr1, o1[1]))
    kn(s, xr1, o1[1])
    kn(s, xk1, p1[1])
    kn(s, xk1, yu1)
    t(s, "R", (0.5 * (xk1 + xr1), yt1 + 0.27))
    t(s, "R", (0.5 * (xk1 + xr1), yu1 + 0.27))
    t(s, "3 V", (xr1 + 0.1, o1[1]), "left", BLAU, 23)
    kl(s, 0.25, p1[1], "1", dx=-0.16, dy=0.0)
    s.draht((0.31, p1[1]), (xk1, p1[1]))
    t(s, "U_1 = 1 V", (0.2, p1[1] - 0.3), "left", BLAU, 23)
    ipfeil(s, (0.95, p1[1]), (0.57, p1[1]), "0.2 mA", (0.67, p1[1] + 0.27))
    wid(s, (xk1, yu1), (xk1, yu1 - 0.95), size=0.36)
    masse(s, xk1, yu1 - 0.95, g=0.42)
    t(s, "R_2", (xk1 + 0.27, yu1 - 0.5), "left", g=23)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k11schmitt():
    """Schmitt-Trigger und Hystereseschleife."""
    s = Szene("et1/k11schmitt")
    s.welt()
    g = 0.6
    x0, y0 = -2.0, 0.85
    m, p, o = opv(s, x0, y0, g)
    kl(s, m[0] - 0.42, m[1], "U_E", dx=0.0, dy=0.28, farbe=BLAU)
    s.draht((m[0] - 0.36, m[1]), m)
    xr = o[0] + 0.25
    s.draht(o, (xr + 0.3, o[1]))
    kn(s, xr, o[1])
    kl(s, xr + 0.36, o[1], "U_A", dx=0.0, dy=0.28, farbe=BLAU)
    ym = -0.3
    s.draht(p, (p[0], ym))
    kn(s, p[0], ym)
    wid(s, (p[0], ym), (xr, ym))
    s.draht((xr, ym), (xr, o[1]))
    t(s, "R_2 = 40 kΩ", (0.5 * (p[0] + xr) + 0.05, ym + 0.33))
    wid(s, (p[0], ym), (p[0], -1.3))
    masse(s, p[0], -1.3)
    t(s, "R_1 = 10 kΩ", (p[0] + 0.3, -0.85), "left")
    a = s.achsen((-5, 5), (-14, 14), breite=2.75, hoehe=2.4, mitte=(2.05, 0.2), xl=achse(s, "U_E", "V"), yl=achse(s, "U_A", "V"), gitter=True, rahmen=True,
                 xticks="-5;-2.2;0;2.2;5", yticks="-11;0;11")
    s.daten(a, [(-5, 11), (2.2, 11), (2.2, -11), (5, -11)], farbe=BLAU, dicke=4)
    s.daten(a, [(5, -11), (-2.2, -11), (-2.2, 11), (-5, 11)], farbe=ROT, dicke=4)
    s.pfeil((-0.8, 12.6), (0.9, 12.6), "", farbe=BLAU, spitze=0.16, on=a)
    s.pfeil((2.2, 4.5), (2.2, -2.5), "", farbe=BLAU, spitze=0.18, on=a)
    s.pfeil((0.9, -12.6), (-0.8, -12.6), "", farbe=ROT, spitze=0.16, on=a)
    s.pfeil((-2.2, -4.5), (-2.2, 2.5), "", farbe=ROT, spitze=0.18, on=a)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def k11bode():
    """|A(f)| und |G(f)| doppellogarithmisch."""
    s = Szene("et1/k11bode")
    x_f = s.tr("f_hz2", "f in Hz", "f in Hz", "f en Hz", "f / Hz")
    a = s.achsen((1, 1e7), (0.1, 1e6), breite=5.6, hoehe=2.4, mitte=(0.45, 0), xl=x_f, yl=s.tr("betr", "Betrag", "magnitude", "módulo", "幅值"),
                 xlog=True, ylog=True, gitter=True, rahmen=True)
    fs = [10 ** (i * 7 / 140) for i in range(141)]
    s.daten(a, [(f, 1e5 / (1 + (f / 10) ** 2) ** 0.5) for f in fs], farbe=BLAU, dicke=4)
    s.daten(a, [(f, 5 / (1 + (f / 2e5) ** 2) ** 0.5) for f in fs], farbe=ROT, dicke=4)
    s.text(a, "|A(f)|", (120, 2.2e4), farbe=BLAU, groesse=25)
    s.text(a, "|G(f)|", (6, 1.5), farbe=ROT, groesse=25)
    s.punkt(a, 10, 1e5 / 2 ** 0.5, farbe=BLAU, r=0.065)
    s.text(a, "f_A = 10 Hz", (13, 2.3e5), farbe=BLAU, groesse=23)
    s.punkt(a, 2e5, 5 / 2 ** 0.5, farbe=ROT, r=0.065)
    s.text(a, "f_G = 200 kHz", (2.6e5, 7), farbe=ROT, groesse=23)
    s.punkt(a, 1e6, 1, farbe=BLAU, r=0.065)
    s.text(a, "f_T = 1 MHz", (1.4e4, 0.25), farbe=BLAU, groesse=23)
    s.pfeil((1e3, 5.3), (1e3, 950), "", farbe=GRAU, spitze=0.14, on=a, doppelt=True, dicke=2.5)
    s.text(a, "|A|β = 200", (1.3e3, 20), farbe=GRAU, groesse=23)
    s.speichern()


ALLE = (k11rauschen, k11diff, k11opv, k11flash, k11schleife, k11nichtinv, k11invert, k11addsub, k11bauteile, k11nic, k11schmitt, k11bode)

if __name__ == "__main__":
    for f in ALLE:
        f()
