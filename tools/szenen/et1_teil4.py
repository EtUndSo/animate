"""ET1 Teil 4 (kap4_stufen.tex): Strom und Spannung messen.

Aufruf: python tools/szenen/et1_teil4.py, danach python tools/szenen_ansehen.py out.png et1/k4messwerk ... [--lang de]
Zahlen: C:/Bücher/ET1/Arbeitshefte/rechnung_kap4.py.
"""
import sys
from math import cos, radians, sin
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#dcefe3"
KLEIN = 23


def stelle(s, *pkte):
    """Knotenpunkte"""
    for p in pkte:
        s.punkt(None, p[0], p[1], r=0.07)


def anschluss(s, *pkte):
    for p in pkte:
        s.kreis(None, p[0], p[1], 0.09, dicke=2.5, fuellung="#ffffff", deckung=1.0)


def res(s, mitte, senkrecht=False, laenge=1.0, groesse=0.6, farbe=SCHWARZ):
    """Widerstand; laenge = Abstand der Anschlüsse, groesse skaliert das Symbol."""
    return s.bauteil("resistor", mitte, drehung=270 if senkrecht else 0, laenge=laenge, label="", size=groesse, farbe=farbe)


def inst(s, art, mitte, senkrecht=False, laenge=0.8, groesse=0.75, farbe=SCHWARZ):
    return s.bauteil(art, mitte, drehung=270 if senkrecht else 0, laenge=laenge, label="", size=groesse, farbe=farbe, font_size=24)


def quelle(s, mitte, laenge=2.0, art="vsource", groesse=0.8):
    return s.bauteil(art, mitte, drehung=270, laenge=laenge, label="", size=groesse)


def spannung(s, x, y0, y1, text, seite="right", farbe=BLAU, groesse=KLEIN):
    """Senkrechter Spannungspfeil von y0 nach y1 bei x, Text daneben."""
    s.pfeil((x, y0), (x, y1), "", farbe=farbe, spitze=0.17, dicke=2.5)
    ym = 0.5 * (y0 + y1)
    if seite == "right":
        s.text(None, text, (x + 0.1, ym), groesse=groesse, farbe=farbe)
    else:
        s.text(None, text, (x - 0.1, ym), groesse=groesse, farbe=farbe, ausrichtung="right")


def strom(s, a, b, farbe=ROT):
    """Kurzer Strompfeil auf einer Leitung"""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=2.5)


# ------------------------------------------------------------------------------------------ Stufe 1
def k4messwerk():
    """Links das Messwerk, rechts die beiden realen Instrumente als ideales Gerät plus Innenwiderstand."""
    s = Szene("et1/k4messwerk")
    s.welt()
    cx, cy = -2.15, -0.45
    s.box("N", (cx - 0.95, cy), breite=0.5, hoehe=0.8, fuellung=HELLROT, groesse=24)
    s.box("S", (cx + 0.95, cy), breite=0.5, hoehe=0.8, fuellung=HELLBLAU, groesse=24)
    s.kreis(None, cx, cy, 0.48, dicke=2, dash=DASH, farbe=GRAU)
    s.box("", (cx, cy), breite=0.92, hoehe=0.34, fuellung="#ead9c4", dicke=2.5)
    for dx in (-0.3, -0.15, 0.0, 0.15, 0.3):
        s.linie(None, (cx + dx, cy - 0.17), (cx + dx, cy + 0.17), dicke=1.5, farbe="#7a5a33")
    Rz, Ra, wink = 1.3, 1.42, 16
    s.linie(None, (cx, cy), (cx + Rz * sin(radians(wink)), cy + Rz * cos(radians(wink))), farbe=ROT, dicke=3.5)
    s.punkt(None, cx, cy, r=0.07, farbe=ROT)
    s.weg(None, f"{cx}+{Ra}*sin(t)", f"{cy}+{Ra}*cos(t)", radians(-38), radians(38), farbe=SCHWARZ, dicke=3, n=41)
    for k in range(6):
        w = radians(-38 + k * 76 / 5)
        s.linie(None, (cx + Ra * sin(w), cy + Ra * cos(w)), (cx + (Ra + 0.11) * sin(w), cy + (Ra + 0.11) * cos(w)), dicke=2.5)
    s.text(None, "0", (cx - 1.0, cy + 1.27), groesse=KLEIN, ausrichtung="center")
    s.text(None, "50 µA", (cx + 1.2, cy + 1.3), groesse=KLEIN, ausrichtung="center")
    s.text(None, s.tr("magnet", "Dauermagnet", "permanent magnet", "imán permanente", "永磁体"), (cx, cy - 0.66), groesse=KLEIN, ausrichtung="center")
    s.text(None, s.tr("spule", "Spule, R_M = 2 kΩ", "coil, R_M = 2 kΩ", "bobina, R_M = 2 kΩ", "线圈，R_M = 2 kΩ"), (cx, cy - 0.96), groesse=KLEIN, ausrichtung="center")
    s.text(None, s.tr("zeiger", "Zeiger", "pointer", "aguja", "指针"), (cx - 0.5, cy + 0.82), groesse=KLEIN, ausrichtung="center", farbe=ROT)
    # Amperemeter
    xl, xr, y = 0.25, 3.4, 0.72
    xm = 0.5 * (xl + xr)
    s.text(None, s.tr("realA", "reales Amperemeter", "real ammeter", "amperímetro real", "实际电流表"), (xm, y + 0.7), groesse=KLEIN, ausrichtung="center")
    s.box("", (xm, y + 0.05), breite=2.4, hoehe=0.96, deckung=0.0, dash=DASH, farbe=GRAU, dicke=2)
    anschluss(s, (xl, y), (xr, y))
    s.draht((xl, y), (0.95, y))
    inst(s, "ammeter", (1.3, y), laenge=0.7, groesse=0.6)
    s.draht((1.65, y), (1.95, y))
    res(s, (2.35, y), laenge=0.8)
    s.draht((2.75, y), (xr, y))
    s.text(None, "R_{iA}", (2.35, y + 0.3), groesse=KLEIN, ausrichtung="center")
    s.text(None, s.tr("ideal1", "ideal", "ideal", "ideal", "理想"), (1.3, y + 0.37), groesse=22, ausrichtung="center", farbe=GRAU)
    # Voltmeter
    ym = -0.72
    s.text(None, s.tr("realV", "reales Voltmeter", "real voltmeter", "voltímetro real", "实际电压表"), (xm, ym + 0.82), groesse=KLEIN, ausrichtung="center")
    s.box("", (xm, ym), breite=2.4, hoehe=1.28, deckung=0.0, dash=DASH, farbe=GRAU, dicke=2)
    anschluss(s, (xl, ym), (xr, ym))
    a, b = 1.05, 2.6
    s.draht((xl, ym), (a, ym))
    s.draht((b, ym), (xr, ym))
    s.draht((a, ym + 0.33), (a, ym - 0.33))
    s.draht((b, ym + 0.33), (b, ym - 0.33))
    s.draht((a, ym + 0.33), (1.5, ym + 0.33))
    s.draht((2.15, ym + 0.33), (b, ym + 0.33))
    inst(s, "voltmeter", (0.5 * (a + b), ym + 0.33), laenge=0.65, groesse=0.52)
    res(s, (0.5 * (a + b), ym - 0.33), laenge=1.55)
    stelle(s, (a, ym), (b, ym))
    s.text(None, "R_{iV}", (0.5 * (a + b), ym - 0.04), groesse=KLEIN, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k4bereich():
    """Shunt und Vorwiderstand am selben Messwerk."""
    s = Szene("et1/k4bereich")
    x0, x1, x2, x3 = -3.4, -2.85, -0.85, -0.3
    yo, yu = 0.55, -0.25
    s.text(None, s.tr("tA", "Amperemeter, Bereich 10 mA", "ammeter, range 10 mA", "amperímetro, rango 10 mA", "电流表，量程 10 mA"), (0.5 * (x0 + x3), 1.22), groesse=KLEIN, ausrichtung="center")
    xm = 0.5 * (x1 + x2)
    anschluss(s, (x0, yu), (x3, yu))
    s.draht((x0, yu), (x1, yu), (x1, yo))
    s.draht((x3, yu), (x2, yu), (x2, yo))
    s.draht((x1, yu), (xm - 0.35, yu))
    s.draht((x2, yu), (xm + 0.35, yu))
    inst(s, "ammeter", (xm, yu), laenge=0.7, groesse=0.65)
    stelle(s, (x1, yu), (x2, yu))
    s.draht((x1, yo), (xm - 0.5, yo))
    s.draht((x2, yo), (xm + 0.5, yo))
    res(s, (xm, yo), laenge=1.0)
    s.text(None, "R_{Shunt} = 10.05 Ω", (xm, yo + 0.3), groesse=KLEIN, ausrichtung="center")
    s.text(None, "9.95 mA", (x1 + 0.05, yo - 0.28), groesse=KLEIN, farbe=ROT)
    strom(s, (x1 + 0.1, yo), (x1 + 0.45, yo))
    s.text(None, "R_M = 2 kΩ", (xm, yu - 0.6), groesse=KLEIN, ausrichtung="center")
    s.text(None, "50 µA", (x1 + 0.08, yu - 0.28), groesse=KLEIN, farbe=ROT)
    strom(s, (x1 + 0.08, yu), (x1 + 0.42, yu))
    s.text(None, "10 mA", (x0 - 0.05, yu + 0.28), groesse=KLEIN, farbe=ROT)
    strom(s, (x0 + 0.1, yu), (x0 + 0.46, yu))
    x0, x1 = 0.2, 3.38
    y = 0.3
    s.text(None, s.tr("tV", "Voltmeter, Bereich 10 V", "voltmeter, range 10 V", "voltímetro, rango 10 V", "电压表，量程 10 V"), (0.5 * (x0 + x1), 1.22), groesse=KLEIN, ausrichtung="center")
    anschluss(s, (x0, y), (x1, y))
    s.draht((x0, y), (0.5, y))
    res(s, (1.05, y), laenge=1.1)
    s.draht((1.6, y), (2.25, y))
    inst(s, "voltmeter", (2.6, y), laenge=0.7, groesse=0.65)
    s.draht((2.95, y), (x1, y))
    s.text(None, "R_V = 198 kΩ", (1.05, y + 0.32), groesse=KLEIN, ausrichtung="center")
    s.text(None, "R_M = 2 kΩ", (2.6, y + 0.5), groesse=KLEIN, ausrichtung="center")
    yp = y - 0.5
    s.pfeil((0.5, yp), (1.6, yp), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    s.text(None, "9.9 V", (1.05, yp - 0.26), groesse=KLEIN, farbe=BLAU, ausrichtung="center")
    s.pfeil((2.2, yp), (3.0, yp), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    s.text(None, "100 mV", (2.6, yp - 0.26), groesse=KLEIN, farbe=BLAU, ausrichtung="center")
    yq = yp - 0.52
    s.pfeil((x0, yq), (x1, yq), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    s.text(None, "10 V", (0.5 * (x0 + x1), yq - 0.26), groesse=KLEIN, farbe=BLAU, ausrichtung="center")
    s.speichern()


def k4stufen():
    """Mehrere Bereiche: Shunts werden zugeschaltet, Vorwiderstände werden überbrückt."""
    s = Szene("et1/k4stufen")
    yo, yu = 0.75, -0.6
    ym = 0.5 * (yo + yu)
    xl, dx = -2.86, 0.82
    x = [xl + k * dx for k in range(4)]
    s.text(None, s.tr("sA", "Schalter schließen", "close the switches", "cerrar interruptores", "闭合开关"), (x[0] + 1.2, yo + 0.62), groesse=KLEIN, ausrichtung="center")
    anschluss(s, (x[0] - 0.5, yo), (x[0] - 0.5, yu))
    s.draht((x[0] - 0.5, yo), (x[0], yo))
    s.draht((x[0] - 0.5, yu), (x[3], yu))
    inst(s, "ammeter", (x[0], ym), senkrecht=True, laenge=1.35, groesse=0.6)
    stelle(s, (x[0], yo), (x[0], yu))
    for k in range(1, 4):
        s.bauteil("switch", (x[k] - dx / 2, yo), laenge=dx, label="", size=0.5)
        s.text(None, f"S_{k}", (x[k] - dx / 2, yo + 0.3), groesse=KLEIN, ausrichtung="center")
        res(s, (x[k], ym), senkrecht=True, laenge=1.35, groesse=0.5)
        s.text(None, f"R_{k}", (x[k] - 0.16, ym), groesse=KLEIN, ausrichtung="right")
        if k < 3:
            stelle(s, (x[k], yo), (x[k], yu))
    x0, d = 0.6, 0.68
    y, yb = 0.05, 0.75
    s.text(None, s.tr("sV", "Schalter öffnen", "open the switches", "abrir interruptores", "断开开关"), (2.0, yo + 0.62), groesse=KLEIN, ausrichtung="center")
    anschluss(s, (x0 - 0.4, y), (x0 - 0.4, yu))
    s.draht((x0 - 0.4, y), (x0, y))
    xs = [x0 + k * d for k in range(4)]
    for k in range(3):
        xc = 0.5 * (xs[k] + xs[k + 1])
        res(s, (xc, y), laenge=d, groesse=0.42)
        s.bauteil("switch", (xc, yb), laenge=d, label="", size=0.42)
        s.text(None, f"S_{3 - k}", (xc, yb + 0.3), groesse=KLEIN, ausrichtung="center")
        s.text(None, f"R_{3 - k}", (xc, y - 0.3), groesse=KLEIN, ausrichtung="center")
    for xk in xs:
        s.draht((xk, y), (xk, yb))
        stelle(s, (xk, y), (xk, yb))
    s.draht((xs[3], y), (xs[3] + 0.15, y))
    inst(s, "voltmeter", (xs[3] + 0.45, y), laenge=0.6, groesse=0.56)
    s.draht((xs[3] + 0.75, y), (xs[3] + 0.9, y), (xs[3] + 0.9, yu), (x0 - 0.4, yu))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k4strom():
    """Stromkreis ohne und mit Amperemeter."""
    s = Szene("et1/k4strom")
    yo, yu = 0.75, -0.75
    yt = yo + 0.85
    xl, xr = -3.25, -1.65
    s.text(None, s.tr("ohne", "ohne Messgerät", "without meter", "sin instrumento", "未接仪表"), (0.5 * (xl + xr) + 0.2, yt), groesse=KLEIN, ausrichtung="center")
    quelle(s, (xl, 0), laenge=1.5, groesse=0.7)
    res(s, (xr, 0), senkrecht=True, laenge=1.5, groesse=0.55)
    s.draht((xl, yo), (xr, yo))
    s.draht((xl, yu), (xr, yu))
    s.text(None, "9 V", (xl + 0.36, 0), groesse=KLEIN)
    s.text(None, "1.8 kΩ", (xr + 0.22, 0), groesse=KLEIN)
    s.text(None, "5 mA", (0.5 * (xl + xr), yo - 0.28), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    strom(s, (0.5 * (xl + xr) - 0.2, yo), (0.5 * (xl + xr) + 0.2, yo))
    xl, xr = 0.0, 2.45
    s.text(None, s.tr("mit", "mit Amperemeter", "with ammeter", "con amperímetro", "接入电流表"), (0.5 * (xl + xr) + 0.2, yt), groesse=KLEIN, ausrichtung="center")
    quelle(s, (xl, 0), laenge=1.5, groesse=0.7)
    res(s, (xr, 0), senkrecht=True, laenge=1.5, groesse=0.55)
    s.draht((xl, yu), (xr, yu))
    s.draht((xl, yo), (0.3, yo))
    inst(s, "ammeter", (0.62, yo), laenge=0.64, groesse=0.6)
    s.draht((0.94, yo), (1.15, yo))
    res(s, (1.55, yo), laenge=0.8)
    s.draht((1.95, yo), (xr, yo))
    s.box("", (1.14, yo), breite=1.8, hoehe=0.68, deckung=0.0, dash=DASH, farbe=GRAU, dicke=2)
    s.text(None, "R_{iA} = 10 Ω", (1.55, yo + 0.5), groesse=KLEIN, ausrichtung="center")
    s.text(None, "9 V", (xl + 0.36, 0), groesse=KLEIN)
    s.text(None, "1.8 kΩ", (xr - 0.22, -0.25), groesse=KLEIN, ausrichtung="right")
    s.text(None, "4.972 mA", (1.2, yu + 0.28), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    strom(s, (1.4, yu), (1.0, yu))
    spannung(s, xr + 0.3, 0.65, -0.65, "8.950 V")
    s.pfeil((1.15, yo - 0.46), (1.95, yo - 0.46), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    s.text(None, "49.7 mV", (1.55, yo - 0.7), groesse=KLEIN, farbe=BLAU, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k4spannung():
    """Voltmeter an Stromquelle mit Last und am Spannungsteiler."""
    s = Szene("et1/k4spannung")
    yo, yu = 0.75, -0.75
    yt = yo + 0.58
    yz = yu - 0.27
    x1, x2, x3, x4 = -3.25, -2.15, -1.0, -0.2
    s.text(None, s.tr("anI", "an einer Stromquelle", "on a current source", "en una fuente de corriente", "接在电流源上"), (-1.75, yt), groesse=KLEIN, ausrichtung="center")
    quelle(s, (x1, 0), art="isource", laenge=1.5, groesse=0.7)
    res(s, (x2, 0), senkrecht=True, laenge=1.5, groesse=0.5)
    res(s, (x3, 0), senkrecht=True, laenge=1.5, groesse=0.5)
    inst(s, "voltmeter", (x4, 0), senkrecht=True, laenge=1.5, groesse=0.62)
    s.draht((x1, yo), (x4, yo))
    s.draht((x1, yu), (x4, yu))
    stelle(s, (x2, yo), (x3, yo), (x2, yu), (x3, yu))
    s.box("", (0.5 * (x3 + x4) + 0.03, 0.0), breite=1.62, hoehe=1.2, deckung=0.0, dash=DASH, farbe=GRAU, dicke=2)
    s.text(None, "20 kΩ", (x2 + 0.2, 0), groesse=KLEIN)
    s.text(None, "200", (x3 + 0.2, 0.14), groesse=KLEIN)
    s.text(None, "kΩ", (x3 + 0.2, -0.14), groesse=KLEIN)
    for x, t in ((x1, "150 µA"), (x2, "136.4 µA"), (x3, "13.6 µA")):
        s.text(None, t, (x, yz), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    for x in (x2, x3):
        strom(s, (x, 0.75), (x, 0.47))
    strom(s, (x1 + 0.1, yo), (x1 + 0.5, yo))
    s.text(None, s.tr("anz", "Anzeige 2.727 V statt 3 V", "reading 2.727 V instead of 3 V", "lectura 2.727 V en vez de 3 V", "读数 2.727 V，而非 3 V"), (-1.75, yz - 0.34), groesse=KLEIN, farbe=BLAU, ausrichtung="center")
    xq, xr, xv = 0.85, 2.15, 3.1
    s.text(None, s.tr("anT", "am Spannungsteiler", "on a voltage divider", "en un divisor de tensión", "接在分压器上"), (2.1, yt), groesse=KLEIN, ausrichtung="center")
    quelle(s, (xq, 0), laenge=1.5, groesse=0.7)
    res(s, (xr, 0.375), senkrecht=True, laenge=0.75, groesse=0.42)
    res(s, (xr, -0.375), senkrecht=True, laenge=0.75, groesse=0.42)
    inst(s, "voltmeter", (xv, -0.375), senkrecht=True, laenge=0.75, groesse=0.56)
    s.draht((xq, yo), (xr, yo))
    s.draht((xq, yu), (xv, yu))
    s.draht((xr, 0), (xv, 0))
    stelle(s, (xr, 0), (xr, yu))
    s.text(None, "9 V", (xq + 0.32, 0), groesse=KLEIN)
    s.text(None, "60 kΩ", (xr - 0.16, 0.375), groesse=KLEIN, ausrichtung="right")
    s.text(None, "30 kΩ", (xr - 0.16, -0.375), groesse=KLEIN, ausrichtung="right")
    s.text(None, "104.5 µA", (1.65, yo + 0.26), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    strom(s, (1.45, yo), (1.85, yo))
    strom(s, (xr + 0.25, 0), (xr + 0.62, 0))
    for x, t in ((xr, "90.9 µA"), (xv, "13.6 µA")):
        s.text(None, t, (x, yz), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    s.text(None, s.tr("anz", "Anzeige 2.727 V statt 3 V", "reading 2.727 V instead of 3 V", "lectura 2.727 V en vez de 3 V", "读数 2.727 V，而非 3 V"), (2.1, yz - 0.34), groesse=KLEIN, farbe=BLAU, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k4richtig():
    """Stromrichtige und spannungsrichtige Schaltung."""
    s = Szene("et1/k4richtig")
    yo, yu = 0.65, -0.65
    yt = yo + 0.5

    def kreis(xq, xa, xv, xr):
        quelle(s, (xq, 0), laenge=1.3, groesse=0.62)
        s.text(None, "9 V", (xq + 0.3, 0), groesse=KLEIN)
        res(s, (xr, 0), senkrecht=True, laenge=1.3, groesse=0.5)
        s.text(None, "R", (xr + 0.2, 0), groesse=KLEIN)
        inst(s, "voltmeter", (xv, 0), senkrecht=True, laenge=1.3, groesse=0.56)
        s.draht((xq, yu), (xr, yu))
        s.draht((xq, yo), (xa - 0.3, yo))
        s.draht((xa + 0.3, yo), (xr, yo))
        inst(s, "ammeter", (xa, yo), laenge=0.6, groesse=0.56)
        stelle(s, (xv, yo), (xv, yu))

    kreis(-3.3, -1.5, -2.3, -0.7)
    kreis(0.5, 1.3, 2.1, 2.95)
    s.text(None, s.tr("sr", "stromrichtig", "correct current", "corriente correcta", "电流正确"), (-2.0, yt + 0.42), groesse=KLEIN, ausrichtung="center")
    s.text(None, s.tr("ur", "spannungsrichtig", "correct voltage", "tensión correcta", "电压正确"), (1.75, yt + 0.42), groesse=KLEIN, ausrichtung="center")
    y = yt
    s.text(None, "I = I_R", (-1.5, y), groesse=KLEIN, farbe=GRUEN, ausrichtung="center")
    s.text(None, "I = I_R + I_{iV}", (1.3, y), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    y = yu - 0.32
    s.text(None, "U = U_R + U_{iA}", (-2.3, y), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    s.text(None, "U = U_R", (2.1, y), groesse=KLEIN, farbe=GRUEN, ausrichtung="center")
    s.speichern()


def k4fehler():
    """Relativer Fehler von R = U/I über R, doppelt logarithmisch."""
    s = Szene("et1/k4fehler")
    xl = s.tr("Rin", "R in Ω", "R in Ω", "R en Ω", "R / Ω")
    yl = s.tr("fin", "|f| in %", "|f| in %", "|f| en %", "|f| / %")
    a = s.achsen((10, 1e6), (0.001, 100), breite=5.8, hoehe=1.7, mitte=(0.2, 0), xl=xl, yl=yl, xlog=True, ylog=True, gitter=True, rahmen=True)
    pts = [10 ** (1 + 5 * k / 200) for k in range(201)]
    s.daten(a, [(r, 1000 / r) for r in pts], farbe=BLAU, dicke=4)
    s.daten(a, [(r, 100 * r / (r + 2e5)) for r in pts], farbe=ROT, dicke=4)
    s.punkt(a, 1800, 1000 / 1800, farbe=BLAU, r=0.08)
    s.punkt(a, 1800, 100 * 1800 / 201800, farbe=ROT, r=0.08)
    s.linie(a, (1800, 0.001), (1800, 100), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "1.8 kΩ", (2200, 0.002), groesse=KLEIN, farbe=GRAU)
    s.text(a, s.tr("kS", "stromrichtig", "correct current", "corriente correcta", "电流正确"), (13, 0.4), groesse=KLEIN, farbe=BLAU)
    s.text(a, "R_{iA}/R", (13, 0.06), groesse=KLEIN, farbe=BLAU)
    s.text(a, s.tr("kU", "spannungsrichtig", "correct voltage", "tensión correcta", "电压正确"), (1.8e5, 2), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    s.text(a, "R/(R + R_{iV})", (1.8e5, 0.35), groesse=KLEIN, farbe=ROT, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def bruecke(s, xq, xl, xr, yo, yu, art="ammeter", r4="resistor"):
    """H-Form: Quelle bei xq, linker Teiler bei xl, rechter bei xr."""
    h = 0.5 * (yo - yu)
    ym = 0.5 * (yo + yu)
    quelle(s, (xq, ym), laenge=yo - yu, groesse=0.68)
    s.draht((xq, yo), (xr, yo))
    s.draht((xq, yu), (xr, yu))
    res(s, (xl, ym + h / 2), senkrecht=True, laenge=h, groesse=0.5)
    res(s, (xl, ym - h / 2), senkrecht=True, laenge=h, groesse=0.5)
    res(s, (xr, ym + h / 2), senkrecht=True, laenge=h, groesse=0.5)
    s.bauteil(r4, (xr, ym - h / 2), drehung=270, laenge=h, label="", size=0.5, farbe=ROT if r4 != "resistor" else SCHWARZ)
    xm = 0.5 * (xl + xr)
    s.draht((xl, ym), (xm - 0.3, ym))
    s.draht((xm + 0.3, ym), (xr, ym))
    inst(s, art, (xm, ym), laenge=0.6, groesse=0.56)
    stelle(s, (xl, yo), (xl, yu), (xl, ym), (xr, ym))


def k4bruecke():
    """Prinzip und Schleifdraht."""
    s = Szene("et1/k4bruecke")
    yo, yu = 1.15, -1.15
    xq, xl, xr = -3.3, -2.2, -0.7
    s.text(None, s.tr("prinzip", "Prinzip", "principle", "principio", "原理"), (-2.0, yo + 0.3), groesse=KLEIN, ausrichtung="center")
    bruecke(s, xq, xl, xr, yo, yu)
    s.text(None, "U_q", (xq + 0.36, 0), groesse=KLEIN)
    for y, n in ((0.58, 1), (-0.58, 2)):
        s.text(None, f"R_{n}", (xl - 0.16, y), groesse=KLEIN, ausrichtung="right")
    for y, n in ((0.58, 3), (-0.58, 4)):
        s.text(None, f"R_{n}", (xr + 0.16, y), groesse=KLEIN)
    for x, y0, y1, t, sgn in ((xl, 1.13, 0.9, "I_1", 1), (xl, -0.9, -1.13, "I_2", 1), (xr, 1.13, 0.9, "I_3", -1), (xr, -0.9, -1.13, "I_4", -1)):
        strom(s, (x, y0), (x, y1))
        s.text(None, t, (x + 0.12 * sgn, 0.5 * (y0 + y1)), groesse=KLEIN, farbe=ROT, ausrichtung="left" if sgn > 0 else "right")
    # Schleifdraht
    xw, xr, xq = 0.95, 2.45, 3.1
    y0, y1 = -0.98, 0.98
    ys = y0 + (y1 - y0) * 0.643
    s.text(None, s.tr("draht", "Schleifdraht", "slide wire", "hilo deslizante", "滑线"), (1.9, yo + 0.3), groesse=KLEIN, ausrichtung="center")
    quelle(s, (xq, 0), laenge=yo - yu, groesse=0.68)
    s.draht((xw, yo), (xq, yo))
    s.draht((xw, yu), (xq, yu))
    s.draht((xw, yo), (xw, y1))
    s.draht((xw, yu), (xw, y0))
    s.box("", (xw, 0), breite=0.14, hoehe=y1 - y0, fuellung="#9a9a9a", dicke=2.5)
    res(s, (xr, 0.575), senkrecht=True, laenge=1.15, groesse=0.5)
    res(s, (xr, -0.575), senkrecht=True, laenge=1.15, groesse=0.5)
    s.pfeil((1.35, ys), (xw + 0.08, ys), "", spitze=0.18, dicke=3)
    s.draht((1.35, ys), (1.35, 0), (1.45, 0))
    inst(s, "ammeter", (1.75, 0), laenge=0.6, groesse=0.56)
    s.draht((2.05, 0), (xr, 0))
    stelle(s, (xr, 0))
    s.pfeil((0.67, y0), (0.67, ys), "", doppelt=True, spitze=0.15, dicke=2.5, farbe=BLAU)
    s.pfeil((0.67, ys), (0.67, y1), "", doppelt=True, spitze=0.15, dicke=2.5, farbe=BLAU)
    s.text(None, "x", (0.55, 0.5 * (y0 + ys)), groesse=KLEIN, farbe=BLAU, ausrichtung="right")
    s.text(None, "l − x", (0.55, 0.5 * (ys + y1)), groesse=KLEIN, farbe=BLAU, ausrichtung="right")
    s.text(None, "R_1", (xw + 0.14, 0.72), groesse=KLEIN)
    s.text(None, "R_2", (xw + 0.14, -0.5), groesse=KLEIN)
    s.text(None, "R_3", (xr - 0.16, 0.58), groesse=KLEIN, ausrichtung="right")
    s.text(None, "R_4", (xr - 0.16, -0.58), groesse=KLEIN, ausrichtung="right")
    s.text(None, "U_q", (xq + 0.08, 0.66), groesse=KLEIN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k4dms():
    """Verstimmte Brücke und Vergleich der Messbereiche."""
    s = Szene("et1/k4dms")
    yo, yu = 1.1, -1.1
    xq, xl, xr = -3.35, -2.3, -1.0
    bruecke(s, xq, xl, xr, yo, yu, art="voltmeter", r4="resistor_var")
    s.text(None, "9 V", (xq + 0.36, 0), groesse=KLEIN)
    for y in (0.55, -0.55):
        s.text(None, "350 Ω", (xl - 0.16, y), groesse=KLEIN, ausrichtung="right")
    s.text(None, "350 Ω", (xr + 0.16, 0.55), groesse=KLEIN)
    s.text(None, "351.4 Ω", (xr + 0.24, -0.55), groesse=KLEIN, farbe=ROT)
    s.text(None, "U_d", (0.5 * (xl + xr), 0.42), groesse=KLEIN, ausrichtung="center", farbe=BLAU)
    x0, br = 0.55, 2.5
    xm = x0 + br / 2

    def skala(y, skw, marke, fehler, ende, titel):
        """Skala von 0 bis skw, Marke mit Fehlerband, Titel darüber."""
        h = 0.42
        k = br / skw
        s.linie(None, (x0, y), (x0 + br, y), dicke=3)
        for v in (0, skw / 2, skw):
            s.linie(None, (x0 + k * v, y - 0.05), (x0 + k * v, y + 0.1), dicke=3)
        s.box("", (x0 + k * marke, y + h / 2), breite=2 * k * fehler, hoehe=h, fuellung=ROT, farbe=ROT, deckung=0.4, dicke=0)
        s.linie(None, (x0 + k * marke, y), (x0 + k * marke, y + h), farbe=ROT, dicke=1.5)
        s.text(None, "0", (x0, y - 0.28), groesse=KLEIN, ausrichtung="center")
        s.text(None, "%g" % (skw / 2), (x0 + br / 2, y - 0.28), groesse=KLEIN, ausrichtung="center")
        s.text(None, ende, (x0 + br, y - 0.28), groesse=KLEIN, ausrichtung="center")
        s.text(None, titel, (xm, y + h + 0.2), groesse=KLEIN, ausrichtung="center")

    skala(0.4, 10, 4.509, 0.1, "10 V", s.tr("sk1", "direkt: U_4 = 4.509 V ± 100 mV", "direct: U_4 = 4.509 V ± 100 mV", "directo: U_4 = 4.509 V ± 100 mV", "直接：U_4 = 4.509 V ± 100 mV"))
    skala(-0.85, 100, 8.98, 1, "100 mV", s.tr("sk2", "Brücke: U_d = 8.98 mV ± 1 mV", "bridge: U_d = 8.98 mV ± 1 mV", "puente: U_d = 8.98 mV ± 1 mV", "电桥：U_d = 8.98 mV ± 1 mV"))
    s.speichern()


if __name__ == "__main__":
    for f in (k4messwerk, k4bereich, k4stufen, k4strom, k4spannung, k4richtig, k4fehler, k4bruecke, k4dms):
        f()
