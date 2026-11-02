"""ET1 Teil 2 (kap2_stufen.tex): Strom, Widerstand und Kirchhoff.

Aufruf: python tools/szenen/et1_teil2.py, danach python tools/szenen_ansehen.py out.png et1/k2strom ... [--lang de]
Alle Zahlen stammen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap2.py.
"""
import sys
from math import cos, pi, sin
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#dff1e5"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche
LINIE = "#d0d0d0"


def ein(s, g, e):
    """Achsentitel „Größe in Einheit“ in vier Sprachen."""
    return s.tr("ein_" + g.replace("{", "").replace("}", "") + e, f"{g} in {e}", f"{g} in {e}", f"{g} en {e}", f"{g} / {e}")


def ladung(s, x, y, plus=True, r=0.13, groesse=22):
    """Kreis mit Vorzeichen: positiv rot, negativ blau."""
    f = ROT if plus else BLAU
    s.kreis(None, x, y, r, farbe=f, dicke=2, fuellung=HELLROT if plus else HELLBLAU, deckung=1.0)
    s.text(None, "+" if plus else "−", (x, y), groesse=groesse, ausrichtung="center", farbe=f)


def ellipse(s, cx, cy, a, b, farbe=SCHWARZ, dicke=3, dash="", t0=0.0, t1=2 * pi):
    s.weg(None, f"{cx}+{a}*cos(t)", f"{cy}+{b}*sin(t)", t0, t1, farbe=farbe, dicke=dicke, n=61, dash=dash)


def masse(s, x, y, groesse=0.7):
    return s._add("Device", {"kind": "ground", "center": [x, y, 0], "rotation": 0, "flip": False, "label": "", "pins": False, "size": groesse,
                             "font_size": 22, "color": SCHWARZ, "stroke_width": 3, "symbol_style": "europäisch"})


def r_v(s, x, y, laenge=1.0, groesse=0.55, farbe=SCHWARZ):
    """Senkrechter Widerstand ohne Beschriftung."""
    s.bauteil("resistor", (x, y), drehung=270, laenge=laenge, label="", size=groesse, farbe=farbe)


def r_h(s, x, y, laenge=1.0, groesse=0.55, farbe=SCHWARZ):
    """Waagerechter Widerstand ohne Beschriftung."""
    s.bauteil("resistor", (x, y), laenge=laenge, label="", size=groesse, farbe=farbe)


def quelle_v(s, x, y, laenge=2.0):
    """Gleichspannungsquelle, Pluspol oben."""
    s.bauteil("vsource_dc", (x, y), drehung=270, laenge=laenge, label="")


# ------------------------------------------------------------------------------------------ Stufe 1
def k2strom():
    """Ladung im Leiterstück der Länge v Δt läuft in der Zeit Δt durch die Fläche A."""
    s = Szene("et1/k2strom")
    y0, b = 0.0, 0.8
    xa, xp, xe = -3.1, 1.3, 3.1          # Anfang, Fläche A, Ende
    xs = xp - 2.4                        # Beginn des Stücks v Δt
    s.box("", (0.5 * (xs + xp), y0), breite=xp - xs, hoehe=2 * b, farbe="#ffffff", fuellung="#fbe9dd", deckung=1.0, dicke=0)
    s.linie(None, (xa, y0 + b), (xe, y0 + b), dicke=3)
    s.linie(None, (xa, y0 - b), (xe, y0 - b), dicke=3)
    ellipse(s, xa, y0, 0.26, b, dicke=3, t0=0.5 * pi, t1=1.5 * pi)
    ellipse(s, xa, y0, 0.26, b, dicke=2, dash=DASH, t0=-0.5 * pi, t1=0.5 * pi)
    ellipse(s, xe, y0, 0.26, b, dicke=3)
    ellipse(s, xp, y0, 0.26, b, farbe=GRUEN, dicke=4)
    for k, x in enumerate((-2.7, -2.1, -1.5, -0.8, -0.2, 0.4, 0.95, 1.85, 2.45)):
        ladung(s, x, y0 + (0.35 if k % 2 else -0.3), plus=True)
    for x in (-2.0, -0.55, 0.75, 2.15):
        s.pfeil((x - 0.2, y0 + 0.0), (x + 0.3, y0 + 0.0), "", farbe=ROT, spitze=0.16, dicke=2.5)
    s.text(None, "v", (0.1, y0 + 0.02), groesse=24, ausrichtung="center", farbe=ROT)
    s.pfeil((xs, y0 - 1.15), (xp, y0 - 1.15), "", doppelt=True, spitze=0.18, dicke=2.5, farbe=BRAUN)
    s.linie(None, (xs, y0 - b), (xs, y0 - 1.3), farbe=BRAUN, dicke=2, dash=DASH)
    s.linie(None, (xp, y0 - b), (xp, y0 - 1.3), farbe=BRAUN, dicke=2, dash=DASH)
    s.text(None, "v Δt", (0.5 * (xs + xp), y0 - 1.45), groesse=26, ausrichtung="center", farbe=BRAUN)
    s.text(None, s.tr("flaeche", "Fläche A", "area A", "área A", "面积 A"), (xp, y0 + 1.15), groesse=26, ausrichtung="center", farbe=GRUEN)
    s.text(None, s.tr("dichte", "Ladungsdichte q", "charge density q", "densidad de carga q", "电荷密度 q"), (xa + 0.1, y0 + 1.15), groesse=26, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k2drift():
    """Links: Bahn eines Elektrons durch das Gitter. Rechts: gerichteter Geschwindigkeitsanteil als Sägezahn."""
    s = Szene("et1/k2drift")
    s.welt()
    x0, y0, dx, dy = -3.5, -1.1, 0.56, 0.56
    for i in range(6):
        for j in range(5):
            s.kreis(None, x0 + i * dx, y0 + j * dy, 0.075, farbe=ROT, dicke=2, fuellung=HELLROT, deckung=1.0)
    bahn = [(-3.5, 0.0), (-3.05, 0.32), (-2.65, -0.55), (-2.25, 0.75), (-1.95, -0.28), (-1.4, 0.28), (-1.0, -0.2), (-0.7, 0.3)]
    for a, b in zip(bahn, bahn[1:]):
        s.pfeil(a, b, "", farbe=BLAU, spitze=0.15, dicke=2.5)
    ladung(s, -3.5, 0.0, plus=False, r=0.12)
    s.pfeil((-0.8, -1.62), (-3.3, -1.62), "", farbe=GRUEN, spitze=0.2, dicke=3)
    s.text(None, "E", (-2.1, -1.87), groesse=26, ausrichtung="center", farbe=GRUEN)
    s.pfeil((-3.3, 1.65), (-0.8, 1.65), "", farbe=BLAU, spitze=0.2, dicke=3)
    s.text(None, s.tr("driftr", "Drift der Elektronen", "electron drift", "deriva de los electrones", "电子漂移"), (-2.1, 1.92), groesse=24, ausrichtung="center", farbe=BLAU)
    a = s.achsen((0, 6, 1), (0, 1.2, 0.5), breite=2.7, hoehe=2.4, mitte=(1.45, 0.0), xl="t / T", yl="v / v_{max}", yticks="0;0.5;1")
    pts = []
    for k in range(6):
        pts += [(k, 0.0), (k + 1, 1.0)]
    pts.append((6, 0.0))
    s.daten(a, pts, farbe=BLAU, dicke=4)
    s.linie(a, (0, 0.5), (6, 0.5), farbe=ROT, dicke=3, dash=DASH)
    s.text(a, "v_D", (6.15, 0.5), groesse=25, ausrichtung="left", farbe=ROT)
    s.text(a, "v_{max}", (6.15, 1.0), groesse=25, ausrichtung="left", farbe=GRAU)
    s.linie(a, (0, 1), (6, 1), farbe=GRAU, dicke=2, dash=DASH)
    s.speichern()


def k2sofort():
    """Die Feldfront läuft in Nanosekunden durch den Draht, die Elektronen rücken kaum vor."""
    s = Szene("et1/k2sofort")
    x0, x1 = -2.2, 3.4
    zeilen = ((1.15, 0.0, "t = 0"), (0.0, 0.5, "t = 2.5 ns"), (-1.15, 1.0, "t = 5 ns"))
    for y, f, t in zeilen:
        xf = x0 + f * (x1 - x0)
        s.box("", (0.5 * (x0 + x1), y), breite=x1 - x0, hoehe=0.62, farbe=SCHWARZ, fuellung="#f4f4f4", deckung=1.0, dicke=2.5)
        if f > 0:
            s.box("", (0.5 * (x0 + xf), y), breite=xf - x0, hoehe=0.62, farbe=GRUEN, fuellung=HELLGRUEN, deckung=1.0, dicke=2.5)
        n = 18
        for k in range(n):
            x = x0 + (k + 0.5) * (x1 - x0) / n
            s.punkt(None, x, y - 0.17 if k % 2 else y + 0.17, farbe=BLAU, r=0.05)
        m = int(round(f * 4))
        for k in range(m):
            xa = x0 + 0.25 + k * (x1 - x0) / 4
            s.pfeil((xa, y), (xa + 0.75, y), "", farbe=GRUEN, spitze=0.17, dicke=3)
        s.text(None, t, (x0 - 0.2, y), groesse=25, ausrichtung="right")
        if 0 < f < 1:
            s.linie(None, (xf, y - 0.45), (xf, y + 0.45), farbe=ROT, dicke=3.5, dash=DASH)
            s.text(None, s.tr("front", "Feldfront", "field front", "frente de campo", "电场波前"), (xf + 0.1, y + 0.55), groesse=23, ausrichtung="center", farbe=ROT)
    yb = -1.85
    s.pfeil((x0, yb), (x1, yb), "", doppelt=True, spitze=0.18, dicke=2.5)
    s.text(None, "1 m", (0.5 * (x0 + x1), yb - 0.26), groesse=24, ausrichtung="center")
    s.text(None, "E", (x0 + 0.45, 0.5), groesse=25, ausrichtung="center", farbe=GRUEN)
    s.text(None, s.tr("draht", "Kupferdraht voller freier Elektronen", "copper wire full of free electrons", "hilo de cobre lleno de electrones libres", "充满自由电子的铜线"),
           (0.6, 1.7), groesse=24, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k2ohm():
    """Links: Leiter mit Länge L und Querschnitt A. Rechts: Kennlinien im Rechenmodell."""
    s = Szene("et1/k2ohm")
    s.welt()
    xa, xe, y0, b = -3.0, -0.6, 0.15, 0.55
    s.linie(None, (xa, y0 + b), (xe, y0 + b), dicke=3)
    s.linie(None, (xa, y0 - b), (xe, y0 - b), dicke=3)
    ellipse(s, xa, y0, 0.2, b, dicke=3)
    ellipse(s, xe, y0, 0.2, b, dicke=3, t0=-0.5 * pi, t1=0.5 * pi)
    ellipse(s, xe, y0, 0.2, b, dicke=2, dash=DASH, t0=0.5 * pi, t1=1.5 * pi)
    ellipse(s, -1.8, y0, 0.2, b, farbe=ROT, dicke=3, dash=DASH)
    s.text(None, "A", (-1.8, y0 + 0.82), groesse=26, ausrichtung="center", farbe=ROT)
    s.pfeil((-2.65, y0), (-2.05, y0), "", farbe=GRUEN, spitze=0.18, dicke=3)
    s.pfeil((-1.5, y0), (-0.9, y0), "", farbe=GRUEN, spitze=0.18, dicke=3)
    s.text(None, "E", (-2.4, y0 + 0.24), groesse=25, ausrichtung="center", farbe=GRUEN)
    s.text(None, "j", (-1.2, y0 + 0.24), groesse=25, ausrichtung="center", farbe=GRUEN)
    s.pfeil((-3.65, y0), (-3.2, y0), "", farbe=ROT, spitze=0.2, dicke=3.5)
    s.pfeil((-0.38, y0), (0.07, y0), "", farbe=ROT, spitze=0.2, dicke=3.5)
    s.text(None, "I", (-3.45, y0 + 0.28), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, "I", (-0.15, y0 + 0.28), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, "+", (xa, y0 + 0.82), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, "−", (xe, y0 + 0.82), groesse=26, ausrichtung="center", farbe=BLAU)
    s.pfeil((xa, y0 - 0.85), (xe, y0 - 0.85), "", doppelt=True, spitze=0.17, dicke=2.5)
    s.text(None, "L", (0.5 * (xa + xe), y0 - 0.62 - 0.45), groesse=26, ausrichtung="center")
    s.pfeil((xa, y0 - 1.42), (xe, y0 - 1.42), "", spitze=0.2, dicke=3, farbe=BLAU)
    s.text(None, "U = E L", (0.5 * (xa + xe), y0 - 1.67), groesse=25, ausrichtung="center", farbe=BLAU)
    a = s.achsen((0, 9, 3), (0, 9, 3), breite=2.4, hoehe=2.5, mitte=(2.0, 0.1), xl=ein(s, "U", "V"), yl=ein(s, "I", "mA"), gitter=True)
    for r, f in ((1, BLAU), (2, GRUEN), (3, ROT)):
        s.kurve(a, f"x/{r}", x=(0, 9), farbe=f)
    s.text(a, "R = 1 kΩ", (4.3, 7.9), groesse=23, ausrichtung="right", farbe=BLAU)
    s.text(a, "2 kΩ", (8.8, 5.25), groesse=23, ausrichtung="right", farbe=GRUEN)
    s.text(a, "3 kΩ", (8.8, 1.7), groesse=23, ausrichtung="right", farbe=ROT)
    s.punkt(a, 9, 3, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k2temperatur():
    """Links: Widerstand über der Temperatur. Rechts: Kennlinie einer 9-V-Glühlampe."""
    s = Szene("et1/k2temperatur")
    a = s.achsen((0, 100, 20), (0, 2.5, 0.5), breite=2.55, hoehe=2.5, mitte=(-1.9, 0.15), xl=s.tr("thetacel", "ϑ in °C", "ϑ in °C", "ϑ en °C", "ϑ / °C"), yl="R / R_{20}", gitter=True, yticks="0;0.5;1;1.5;2;2.5")
    s.kurve(a, "1+0.0039*(x-20)", x=(0, 100), farbe=BLAU)
    s.kurve(a, "1", x=(0, 100), farbe=GRUEN)
    s.kurve(a, "exp(3500*(1/(x+273.15)-1/293.15))", x=(0, 100), farbe=ROT)
    s.linie(a, (20, 0), (20, 2.5), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, s.tr("kupfer", "Kupfer: PTC", "copper: PTC", "cobre: PTC", "铜：PTC"), (98, 1.5), groesse=23, ausrichtung="right", farbe=BLAU)
    s.text(a, "Konstantan", (98, 0.84), groesse=23, ausrichtung="right", farbe=GRUEN)
    s.text(a, s.tr("halbl", "Halbleiter: NTC", "semiconductor: NTC", "semiconductor: NTC", "半导体：NTC"), (26, 2.3), groesse=23, ausrichtung="left", farbe=ROT)
    b = s.achsen((0, 10, 2), (0, 1, 0.2), breite=2.55, hoehe=2.5, mitte=(1.9, 0.15), xl=ein(s, "U", "V"), yl=ein(s, "I", "A"), gitter=True, yticks="0;0.2;0.4;0.6;0.8;1")
    s.kurve(b, "x/(1.5*(1+11*(x/9)^0.45))", x=(0, 10), farbe=BLAU)
    s.linie(b, (0, 0), (1.5, 1.0), farbe=ROT, dicke=3, dash=DASH)
    s.linie(b, (0, 0), (10, 0.5556), farbe=GRAU, dicke=2.5, dash=DASH)
    s.punkt(b, 9, 0.5, farbe=BLAU)
    s.text(b, s.tr("kalt", "kalt: 1.5 Ω", "cold: 1.5 Ω", "frío: 1.5 Ω", "冷态：1.5 Ω"), (1.85, 0.9), groesse=23, farbe=ROT)
    s.text(b, s.tr("heiss", "heiß: 18 Ω", "hot: 18 Ω", "caliente: 18 Ω", "热态：18 Ω"), (9.8, 0.28), groesse=23, ausrichtung="right", farbe=GRAU)
    s.text(b, s.tr("lampe", "Lampe", "lamp", "lámpara", "灯"), (3.6, 0.42), groesse=23, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k2zaehlpfeil():
    """Links: Quelle (Erzeugerpfeile) und Widerstand (Verbraucherpfeile). Rechts: ein gedrehter Spannungspfeil."""
    s = Szene("et1/k2zaehlpfeil")
    xq, xr, yo, yu = -2.6, -0.65, 1.0, -1.0
    quelle_v(s, xq, 0.0)
    r_v(s, xr, 0.0, laenge=2.0, groesse=0.75)
    s.draht((xq, yo), (xr, yo))
    s.draht((xq, yu), (xr, yu))
    s.pfeil((xq - 0.5, 0.75), (xq - 0.5, -0.75), "", farbe=BLAU, spitze=0.2, dicke=3)
    s.text(None, "U_q", (xq - 0.6, 0.0), groesse=25, ausrichtung="right", farbe=BLAU)
    s.text(None, "9 V", (xq - 0.6, -0.34), groesse=23, ausrichtung="right", farbe=BLAU)
    s.pfeil((xq + 0.52, -0.75), (xq + 0.52, 0.75), "", farbe=ROT, spitze=0.2, dicke=3)
    s.text(None, "I", (xq + 0.64, 0.0), groesse=25, farbe=ROT)
    s.pfeil((xr + 0.5, 0.75), (xr + 0.5, -0.75), "", farbe=BLAU, spitze=0.2, dicke=3)
    s.text(None, "U_R", (xr + 0.6, 0.0), groesse=25, farbe=BLAU)
    s.text(None, "9 V", (xr + 0.6, -0.34), groesse=23, farbe=BLAU)
    s.pfeil((xr - 0.3, 0.75), (xr - 0.3, -0.75), "", farbe=ROT, spitze=0.2, dicke=3)
    s.text(None, "I", (xr - 0.42, 0.0), groesse=25, ausrichtung="right", farbe=ROT)
    s.text(None, "3 mA", (xr - 0.42, -0.34), groesse=23, ausrichtung="right", farbe=ROT)
    s.text(None, "3 kΩ", (xr + 0.0, 1.27), groesse=23, ausrichtung="center")
    s.pfeil((-1.1, yu - 0.26), (-2.2, yu - 0.26), "", farbe=GRUEN, spitze=0.2, dicke=3)
    s.text(None, s.tr("elek", "Elektronen", "electrons", "electrones", "电子"), (-1.65, yu - 0.55), groesse=23, ausrichtung="center", farbe=GRUEN)
    s.text(None, s.tr("gzs", "Quelle: GZS", "generator convention", "convenio generador", "发电机惯例"), (xq, 1.72), groesse=24, ausrichtung="center")
    s.text(None, s.tr("vzs", "Verbraucher: VZS", "load convention", "convenio receptor", "负载惯例"), (xr + 0.2, 1.72), groesse=24, ausrichtung="center")
    x1, x2 = 1.4, 2.8
    for x, ups in ((x1, False), (x2, True)):
        r_v(s, x, 0.0, laenge=2.0, groesse=0.75)
        s.geraet("terminal", (x, 1.0), groesse=0.8)
        s.geraet("terminal", (x, -1.0), groesse=0.8)
        s.text(None, "9 V", (x, 1.32), groesse=23, ausrichtung="center", farbe=ROT)
        s.text(None, "0 V", (x, -1.32), groesse=23, ausrichtung="center", farbe=BLAU)
        s.pfeil((x - 0.3, 0.75), (x - 0.3, -0.75), "", farbe=ROT, spitze=0.2, dicke=3)
        s.text(None, "I", (x - 0.42, 0.0), groesse=25, ausrichtung="right", farbe=ROT)
        if ups:
            s.pfeil((x + 0.3, -0.75), (x + 0.3, 0.75), "", farbe=BLAU, spitze=0.2, dicke=3)
        else:
            s.pfeil((x + 0.3, 0.75), (x + 0.3, -0.75), "", farbe=BLAU, spitze=0.2, dicke=3)
        s.text(None, "U", (x + 0.42, 0.0), groesse=25, farbe=BLAU)
    s.text(None, "U = +9 V", (x1, -1.75), groesse=23, ausrichtung="center", farbe=BLAU)
    s.text(None, "U = −9 V", (x2, -1.75), groesse=23, ausrichtung="center", farbe=BLAU)
    s.text(None, "U = R I", (x1, 1.72), groesse=24, ausrichtung="center")
    s.text(None, "U = −R I", (x2, 1.72), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Brücke
def bruecke(s, cx, cy, w=1.7, h=1.6, xq=1.3, werte=True, r=0.5):
    """H-Schaltung: K1 oben, K4 unten, K2 links, K3 rechts, Quelle links. Gibt die Knotenlagen zurück."""
    xl, xr = cx - w / 2, cx + w / 2
    yo, yu = cy + h, cy - h
    k1, k2, k3, k4 = (cx, yo), (xl, cy), (xr, cy), (cx, yu)
    laenge = 0.9 * h
    s.draht((cx - w / 2 - xq, yo), (xr, yo), (xr, cy + 0.5 * h + laenge / 2))
    s.draht((cx - w / 2 - xq, yu), (xr, yu), (xr, cy - 0.5 * h - laenge / 2))
    s.draht((xl, yo), (xl, cy + 0.5 * h + laenge / 2))
    s.draht((xl, yu), (xl, cy - 0.5 * h - laenge / 2))
    s.draht((xl, cy), (xl, cy + 0.5 * h - laenge / 2))
    s.draht((xl, cy), (xl, cy - 0.5 * h + laenge / 2))
    s.draht((xr, cy), (xr, cy + 0.5 * h - laenge / 2))
    s.draht((xr, cy), (xr, cy - 0.5 * h + laenge / 2))
    r_v(s, xl, cy + 0.5 * h, laenge=laenge, groesse=r)
    r_v(s, xl, cy - 0.5 * h, laenge=laenge, groesse=r)
    r_v(s, xr, cy + 0.5 * h, laenge=laenge, groesse=r)
    r_v(s, xr, cy - 0.5 * h, laenge=laenge, groesse=r)
    r_h(s, cx, cy, laenge=w, groesse=r)
    xs = cx - w / 2 - xq
    s.draht((xs, yo), (xs, cy + 0.75))
    s.draht((xs, yu), (xs, cy - 0.75))
    s.bauteil("vsource_dc", (xs, cy), drehung=270, laenge=1.5, label="")
    for p in (k1, k2, k3, k4):
        s.punkt(None, p[0], p[1], farbe=ROT, r=0.075)
    return k1, k2, k3, k4, xs


def graph(s, cx, cy, w, h, fett=(), rot=(), hell=()):
    """Graph der Brücke im kleinen; fett = schwarz, rot = hervorgehoben, hell = sehr blass, sonst grau."""
    k1, k2, k3, k4 = (cx, cy + h / 2), (cx - w / 2, cy), (cx + w / 2, cy), (cx, cy - h / 2)
    xq = cx - w / 2 - 0.2
    zweige = {"a": [k1, k2], "b": [k2, k4], "c": [k1, k3], "d": [k3, k4], "e": [k2, k3], "0": [k1, (xq, k1[1]), (xq, k4[1]), k4]}
    for name, pts in zweige.items():
        f, d = (ROT, 5) if name in rot else (SCHWARZ, 5) if name in fett else (LINIE, 3)
        for a, b in zip(pts, pts[1:]):
            s.linie(None, a, b, farbe=f, dicke=d)
    for p in (k1, k2, k3, k4):
        s.punkt(None, p[0], p[1], farbe=SCHWARZ, r=0.055)


def k2netz():
    """Links das Netz des Rechenmodells, rechts Baum und die drei Maschen, die er festlegt."""
    s = Szene("et1/k2netz")
    k1, k2, k3, k4, xs = bruecke(s, -1.0, 0.0, xq=0.9)
    s.text(None, "K_1", (k1[0], k1[1] + 0.26), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(None, "K_4", (k4[0], k4[1] - 0.26), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(None, "K_2", (k2[0] + 0.12, k2[1] - 0.25), groesse=24, farbe=ROT)
    s.text(None, "K_3", (k3[0] - 0.12, k3[1] - 0.25), groesse=24, ausrichtung="right", farbe=ROT)
    s.text(None, "U_0", (xs - 0.46, 0.17), groesse=24, ausrichtung="right")
    s.text(None, "9 V", (xs - 0.46, -0.17), groesse=23, ausrichtung="right")
    xl, xr = k2[0], k3[0]
    for x, y, n, w, dx, al in ((xl, 0.8, "R_a", "2 kΩ", 0.24, "left"), (xl, -0.8, "R_b", "5 kΩ", 0.24, "left"),
                               (xr, 0.8, "R_c", "3 kΩ", -0.24, "right"), (xr, -0.8, "R_d", "1 kΩ", -0.24, "right")):
        s.text(None, n, (x + dx, y + 0.17), groesse=23, ausrichtung=al)
        s.text(None, w, (x + dx, y - 0.17), groesse=22, ausrichtung=al)
    s.text(None, "R_e = 2 kΩ", (-1.0, 0.33), groesse=22, ausrichtung="center")
    w, h = 1.05, 1.15
    x1, x2 = 1.45, 2.95
    y1, y2 = 0.9, -0.95
    graph(s, x1, y1, w, h, fett=("0", "b", "d"))
    s.text(None, s.tr("baum", "Baum", "tree", "árbol", "树"), (x1 - 0.1, y1 + 0.82), groesse=24, ausrichtung="center")
    graph(s, x2, y1, w, h, fett=("0", "b"), rot=("a",))
    s.text(None, "M_1", (x2 - 0.1, y1 + 0.82), groesse=24, ausrichtung="center", farbe=ROT)
    graph(s, x1, y2, w, h, fett=("0", "d"), rot=("c",))
    s.text(None, "M_2", (x1 - 0.1, y2 + 0.82), groesse=24, ausrichtung="center", farbe=ROT)
    graph(s, x2, y2, w, h, fett=("b", "d"), rot=("e",))
    s.text(None, "M_3", (x2 - 0.1, y2 + 0.82), groesse=24, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k2knoten():
    """Links: ein Knoten mit fünf Strömen. Rechts: Hülle um K2, K3 und R_e im Netz."""
    s = Szene("et1/k2knoten")
    cx, cy = -2.0, 0.1
    strahlen = ((160, True, "5 mA"), (235, True, "2 mA"), (305, False, "3 mA"), (20, False, "1 mA"), (90, False, "3 mA"))
    for w, hinein, t in strahlen:
        c, n = cos(w * pi / 180), sin(w * pi / 180)
        a, b = (cx + 1.3 * c, cy + 1.3 * n), (cx + 0.13 * c, cy + 0.13 * n)
        s.linie(None, a, b, dicke=3)
        m0, m1 = (cx + 0.45 * c, cy + 0.45 * n), (cx + 0.95 * c, cy + 0.95 * n)
        s.pfeil(m1 if hinein else m0, m0 if hinein else m1, "", farbe=ROT if hinein else BLAU, spitze=0.22, dicke=4)
        s.text(None, t, (cx + 1.62 * c, cy + 1.5 * n), groesse=24, ausrichtung="center", farbe=ROT if hinein else BLAU)
    s.punkt(None, cx, cy, farbe=SCHWARZ, r=0.12)
    s.text(None, s.tr("summe", "hinein: 7 mA, heraus: 7 mA", "in: 7 mA, out: 7 mA", "entran 7 mA, salen 7 mA", "流入 7 mA，流出 7 mA"), (cx, -1.85), groesse=24, ausrichtung="center")
    xl, xr, y0 = 1.05, 2.75, 0.1
    r_h(s, 0.5 * (xl + xr), y0, laenge=xr - xl, groesse=0.5)
    ellipse(s, 0.5 * (xl + xr), y0, 1.35, 0.5, farbe=GRUEN, dicke=3.5, dash=DASH)
    for x, t, f in ((xl, "I_a = 2 mA", ROT), (xr, "I_c = 2 mA", ROT)):
        s.linie(None, (x, y0 + 1.3), (x, y0), dicke=3)
        s.pfeil((x, y0 + 1.15), (x, y0 + 0.62), "", farbe=f, spitze=0.22, dicke=4)
        s.text(None, t, (x, y0 + 1.5), groesse=23, ausrichtung="center", farbe=f)
    for x, t, f in ((xl, "I_b = 1 mA", BLAU), (xr, "I_d = 3 mA", BLAU)):
        s.linie(None, (x, y0 - 1.3), (x, y0), dicke=3)
        s.pfeil((x, y0 - 0.62), (x, y0 - 1.15), "", farbe=f, spitze=0.22, dicke=4)
        s.text(None, t, (x, y0 - 1.5), groesse=23, ausrichtung="center", farbe=f)
    s.punkt(None, xl, y0, farbe=ROT, r=0.075)
    s.punkt(None, xr, y0, farbe=ROT, r=0.075)
    s.text(None, "K_2", (xl + 0.1, y0 - 0.25), groesse=23, farbe=ROT)
    s.text(None, "K_3", (xr - 0.1, y0 - 0.25), groesse=23, ausrichtung="right", farbe=ROT)
    s.text(None, "R_e", (0.5 * (xl + xr), y0 + 0.3), groesse=23, ausrichtung="center")
    s.text(None, s.tr("huelle", "Hülle: hinein 4 mA, heraus 4 mA", "surface: in 4 mA, out 4 mA", "superficie: entran y salen 4 mA", "闭合面：流入 4 mA，流出 4 mA"), (0.5 * (xl + xr), -1.85), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k2masche():
    """Potenzial längs zweier Maschen: Der Umlauf endet auf dem Startwert."""
    s = Szene("et1/k2masche")
    weg = s.tr("weg", "Weg im Umlauf", "path around the mesh", "recorrido de la malla", "沿网孔的路径")

    def achse(mitte, start, stufen, knoten, name, marken):
        a = s.achsen((0, 4.6), (0, 10), breite=2.85, hoehe=2.2, mitte=mitte, xl=weg, yl=ein(s, "φ", "V"), xmarks=False, xzahlen=False, yticks="0;3;5;9")
        pts = [(0, start), (0.4, start)]
        x = 0.4
        for ziel in stufen:
            pts += [(x + 1.0, ziel), (x + 1.4, ziel)]
            x += 1.4
        s.daten(a, pts, farbe=BLAU, dicke=5)
        s.linie(a, (0, start), (4.6, start), farbe=GRAU, dicke=2, dash=DASH)
        for (px, py), t in zip(knoten, name):
            s.text(a, t, (px, py), groesse=23, ausrichtung="center", farbe=ROT)
        for px, py, t, al, f in marken:
            s.text(a, t, (px, py), groesse=23, ausrichtung=al, farbe=f)
        return a
    achse((-1.8, 0.1), 9, (5, 0, 9), ((0.4, 9.85), (1.6, 6.0), (3.0, 0.95), (4.25, 9.85)), ("K_1", "K_2", "K_4", "K_1"),
          ((0.75, 6.0, "−U_a", "right", BLAU), (2.15, 1.6, "−U_b", "right", BLAU), (3.8, 3.9, "+U_0", "left", GRUEN), (2.3, 7.6, "M_1", "center", SCHWARZ)))
    achse((1.75, 0.1), 5, (3, 0, 5), ((0.4, 5.9), (1.6, 3.95), (3.0, 0.95), (4.25, 5.9)), ("K_2", "K_3", "K_4", "K_2"),
          ((0.75, 2.9, "−U_e", "right", BLAU), (2.1, 0.75, "−U_d", "center", BLAU), (3.8, 2.0, "+U_b", "left", GRUEN), (2.3, 7.6, "M_3", "center", SCHWARZ)))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k2teiler():
    """Links: Spannungsteiler des Rechenmodells. Mitte: Kette eines 3-Bit-Wandlers. Rechts: seine Treppe."""
    s = Szene("et1/k2teiler")
    s.welt()
    xq, xr, yo, yu = -3.3, -2.3, 1.2, -1.2
    s.draht((xq, yo), (xr, yo), (xr, 1.15))
    s.draht((xq, yu), (xr, yu), (xr, -1.15))
    s.draht((xq, yo), (xq, 0.75))
    s.draht((xq, yu), (xq, -0.75))
    s.bauteil("vsource_dc", (xq, 0), drehung=270, laenge=1.5, label="")
    r_v(s, xr, 0.6, laenge=1.15, groesse=0.6)
    r_v(s, xr, -0.6, laenge=1.15, groesse=0.6)
    s.draht((xr, 0.03), (xr, -0.03))
    s.text(None, "9 V", (xq + 0.26, -0.3), groesse=23)
    s.text(None, "R_1", (xr - 0.26, 0.6), groesse=23, ausrichtung="right")
    s.text(None, "R_2", (xr - 0.26, -0.6), groesse=23, ausrichtung="right")
    s.pfeil((xr + 0.3, 1.05), (xr + 0.3, 0.1), "", farbe=BLAU, spitze=0.18, dicke=2.5)
    s.pfeil((xr + 0.3, -0.1), (xr + 0.3, -1.05), "", farbe=BLAU, spitze=0.18, dicke=2.5)
    s.text(None, "6 V", (xr + 0.38, 0.6), groesse=23, farbe=BLAU)
    s.text(None, "3 V", (xr + 0.38, -0.6), groesse=23, farbe=BLAU)
    s.punkt(None, xr, 0.0, farbe=ROT, r=0.07)
    # Kette
    x, dy = -0.65, 0.42
    y0 = 1.9
    s.geraet("terminal", (x, y0 + 0.02), groesse=0.7)
    s.text(None, "U_{ref} = 3.2 V", (x + 0.0, y0 + 0.3), groesse=23, ausrichtung="center", farbe=ROT)
    namen = ["R/2"] + ["R"] * 7 + ["R/2"]
    for i, n in enumerate(namen):
        yc = y0 - (i + 0.5) * dy
        r_v(s, x, yc, laenge=dy, groesse=0.27)
        s.text(None, n, (x - 0.2, yc), groesse=22, ausrichtung="right")
        if i < 8:
            yt = yc - 0.5 * dy
            s.punkt(None, x, yt, farbe=BLAU, r=0.05)
            s.linie(None, (x, yt), (x + 0.2, yt), farbe=BLAU, dicke=2.5)
    masse(s, x, y0 - 9 * dy - 0.03, groesse=0.55)
    for i in range(8):
        yt = y0 - (i + 1) * dy
        s.text(None, f"{3.0 - 0.4 * i:.1f} V", (x + 0.27, yt), groesse=22, farbe=BLAU)
    a = s.achsen((-0.5, 7.5), (0, 3.2), breite=2.2, hoehe=2.75, mitte=(2.05, 0.05), xl=s.tr("code", "Zahl Z", "number Z", "número Z", "数字 Z"), yl=ein(s, "U", "V"),
                 xticks="0;1;2;3;4;5;6;7", yticks="0.2;1;1.8;2.6;3", gitter=False)
    pts = []
    for z in range(8):
        pts += [(z - 0.5, 0.2 + 0.4 * z), (z + 0.5, 0.2 + 0.4 * z)]
    s.daten(a, pts, farbe=ROT, dicke=4)
    s.linie(a, (-0.5, 0), (7.5, 3.2), farbe=GRUEN, dicke=2.5, dash=DASH)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def k2belastung():
    """Links: belasteter Teiler. Rechts: U2 über dem Lastwiderstand."""
    s = Szene("et1/k2belastung")
    s.welt()
    xq, xr, xl, yo, yu = -3.4, -2.25, -1.35, 1.35, -1.35
    ym = -0.15
    s.draht((xq, yo), (xr, yo), (xr, 1.05))
    s.draht((xq, yu), (xl, yu), (xl, -1.3))
    s.draht((xq, yo), (xq, 0.75))
    s.draht((xq, yu), (xq, -0.75))
    s.bauteil("vsource_dc", (xq, 0), drehung=270, laenge=1.5, label="")
    r_v(s, xr, 0.45, laenge=1.2, groesse=0.6)
    r_v(s, xr, -0.75, laenge=1.2, groesse=0.6)
    s.draht((xr, ym), (xl, ym))
    r_v(s, xl, -0.75, laenge=1.2, groesse=0.6, farbe=ROT)
    s.punkt(None, xr, ym, farbe=ROT, r=0.07)
    s.punkt(None, xr, yu, farbe=ROT, r=0.07)
    s.text(None, "9 V", (xq + 0.26, 0.0), groesse=23)
    s.text(None, "R_1", (xr - 0.26, 0.45), groesse=23, ausrichtung="right")
    s.text(None, "R_2", (xr - 0.26, -0.75), groesse=23, ausrichtung="right")
    s.text(None, "R_L", (xl - 0.25, -0.75), groesse=23, ausrichtung="right", farbe=ROT)
    s.pfeil((xl + 0.32, ym - 0.02), (xl + 0.32, yu + 0.02), "", farbe=BLAU, spitze=0.2, dicke=3)
    s.text(None, "U_2", (xl + 0.4, -0.75), groesse=23, farbe=BLAU)
    s.pfeil((-2.0, ym + 0.2), (-1.5, ym + 0.2), "", farbe=ROT, spitze=0.17, dicke=2.5)
    s.text(None, "I_L", (-1.75, ym + 0.43), groesse=23, ausrichtung="center", farbe=ROT)
    a = s.achsen((100, 1000000), (0, 3.5), breite=2.55, hoehe=2.5, mitte=(1.8, 0.05), xl=ein(s, "R_L", "Ω"), yl=ein(s, "U_2", "V"), xlog=True, gitter=True, yticks="0;1;2;3")
    pts = [(100 * 10 ** (i / 40), 9 * 1e3 * (100 * 10 ** (i / 40)) / (2e3 * (1e3 + 100 * 10 ** (i / 40)) + 1e3 * (100 * 10 ** (i / 40)))) for i in range(161)]
    s.daten(a, pts, farbe=BLAU, dicke=4)
    s.linie(a, (100, 3), (1000000, 3), farbe=GRAU, dicke=2.5, dash=DASH)
    s.text(a, s.tr("leer", "ohne Last: 3 V", "no load: 3 V", "sin carga: 3 V", "空载：3 V"), (150, 3.2), groesse=23, farbe=GRAU)
    for r_, u, t, dx in ((1e3, 1.8, "1.8 V", 1.8), (1e4, 2.8125, "2.81 V", 0.5)):
        s.punkt(a, r_, u, farbe=ROT)
    s.text(a, "1.8 V", (1400, 1.62), groesse=23, farbe=ROT)
    s.text(a, "2.81 V", (12000, 2.42), groesse=23, farbe=ROT)
    s.speichern()


def k2r2r():
    """R-2R-Leiter mit vier Knoten und Code 1010: Jeder Knoten halbiert den Strom."""
    s = Szene("et1/k2r2r")
    xs = [-2.3, -0.95, 0.4, 1.75]
    y1, y2, ya, ym = 1.0, -0.4, -1.03, -1.4
    x0, xe, xa = -3.2, 2.75, 3.5
    s.geraet("terminal", (x0, y1), groesse=0.8)
    s.text(None, "U_{ref}", (x0 - 0.02, y1 + 0.3), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(None, "8 V", (x0 - 0.02, y1 - 0.32), groesse=23, ausrichtung="center", farbe=ROT)
    s.draht((x0, y1), (xs[0], y1))
    pot = ("8 V", "4 V", "2 V", "1 V")
    strom = ("4 mA", "2 mA", "1 mA", "0.5 mA")
    code = (True, False, True, False)
    for i, x in enumerate(xs):
        r_v(s, x, 0.3, laenge=1.4, groesse=0.6)
        s.text(None, "2R", (x + 0.22, 0.45), groesse=23)
        s.punkt(None, x, y1, farbe=ROT, r=0.075)
        s.text(None, pot[i], (x - 0.05, y1 + 0.28), groesse=23, ausrichtung="center", farbe=ROT)
        s.text(None, strom[i], (x + 0.22, 0.1), groesse=23, farbe=BLAU)
        if i < 3:
            r_h(s, x + 0.675, y1, laenge=1.35, groesse=0.6)
            s.text(None, "R", (x + 0.675, y1 + 0.3), groesse=23, ausrichtung="center")
        s.draht((x, y2), (x, y2 - 0.12))
        kl, kr = (x - 0.26, ya), (x + 0.26, ym)
        s.linie(None, (x, y2 - 0.12), kl if code[i] else kr, farbe=ORANGE, dicke=3.5)
        s.punkt(None, kl[0], kl[1], r=0.05)
        s.punkt(None, kr[0], kr[1], r=0.05)
        s.text(None, "1" if code[i] else "0", (x + (-0.33 if code[i] else 0.33), y2 - 0.1), groesse=23, ausrichtung="center", farbe=ORANGE)
    s.draht((xs[3], y1), (xe, y1))
    r_v(s, xe, 0.3, laenge=1.4, groesse=0.6)
    s.draht((xe, y2), (xe, ym))
    s.text(None, "2R", (xe + 0.2, 0.45), groesse=23)
    s.text(None, "0.5 mA", (xe + 0.2, 0.1), groesse=23, farbe=BLAU)
    s.draht((xs[0] - 0.26, ya), (xa, ya))
    s.draht((xs[0] + 0.26, ym), (xe, ym))
    s.punkt(None, xe, ym, r=0.05)
    s.draht((xs[0] + 0.26, ym), (-3.0, ym), (-3.0, ym - 0.1))
    masse(s, -3.0, ym - 0.12, groesse=0.6)
    s.geraet("terminal", (xa, ya), groesse=0.8)
    s.text(None, s.tr("iaus", "I_{aus}", "I_{out}", "I_{sal}", "I_{out}"), (3.15, ya + 0.56), groesse=24, ausrichtung="center", farbe=ORANGE)
    s.text(None, "5 mA", (3.15, ya + 0.24), groesse=23, ausrichtung="center", farbe=ORANGE)
    s.speichern()


ALLE = (k2strom, k2drift, k2sofort, k2ohm, k2temperatur, k2zaehlpfeil, k2netz, k2knoten, k2masche, k2teiler, k2belastung, k2r2r)

if __name__ == "__main__":
    for f in ALLE:
        f()
