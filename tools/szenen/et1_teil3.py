"""ET1 Teil 3 (kap3_stufen.tex): Der Kondensator.

Aufruf: python tools/szenen/et1_teil3.py, danach python tools/szenen_ansehen.py out.png et1/k3aufbau ... [--lang de]
"""
import sys
from math import exp, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLROT, HELLBLAU, HELLGRUEN, HELLGRAU2, HELLORANGE = "#f6dede", "#dceafa", "#dff1e5", "#e6e6e6", "#fbe6da"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche


def ladung(s, x, y, plus=True, r=0.13, groesse=22, on=None):
    """Kreis mit Vorzeichen: positiv rot, negativ blau."""
    f = ROT if plus else BLAU
    s.kreis(on, x, y, r, farbe=f, dicke=2, fuellung=HELLROT if plus else HELLBLAU, deckung=1.0)
    s.text(on, "+" if plus else "−", (x, y), groesse=groesse, ausrichtung="center", farbe=f)


def platte(s, x, y0, y1, breite=0.12):
    """Metallplatte im Schnitt, senkrecht."""
    s.box("", (x, 0.5 * (y0 + y1)), breite=breite, hoehe=y1 - y0, farbe=SCHWARZ, fuellung="#8c8c8c", deckung=1.0, dicke=1.5)


def masse(s, x, y, groesse=0.7):
    return s._add("Device", {"kind": "ground", "center": [x, y, 0], "rotation": 0, "flip": False, "label": "", "pins": False, "size": groesse,
                             "font_size": 22, "color": SCHWARZ, "stroke_width": 3, "symbol_style": "europäisch"})


def klemme(s, x, y, r=0.06):
    """Kontakt eines Umschalters: kleiner offener Kreis."""
    s.kreis(None, x, y, r, farbe=SCHWARZ, dicke=2.5, fuellung="#ffffff", deckung=1.0)


def t_achse(s):
    return s.tr("t_in_s", "t in s", "t in s", "t en s", "t / s")


# ------------------------------------------------------------------------------------------ Stufe 1
def k3aufbau():
    """Plattenpaar an der Batterie: Elektronen in den Zuleitungen, nichts in der Lücke; rechts das Schaltzeichen."""
    s = Szene("et1/k3aufbau")
    xa, xb = -2.2, -1.0
    yo, yu = 1.15, -0.65
    xl, xr, yw = -3.2, 0.0, -1.55
    s.box("", (0.5 * (xa + xb), 0.5 * (yo + yu)), breite=xb - xa - 0.12, hoehe=yo - yu, farbe=HELLORANGE, fuellung=HELLORANGE, deckung=1.0, dicke=0)
    s.draht((xa - 0.06, 0.25), (xl, 0.25), (xl, yw), (-1.95, yw))
    s.draht((-1.25, yw), (xr, yw), (xr, 0.25), (xb + 0.06, 0.25))
    platte(s, xa, yu, yo)
    platte(s, xb, yu, yo)
    s.bauteil("vsource_dc", (-1.6, yw), drehung=0, laenge=0.7, label="")
    s.text(None, "+", (-1.82, yw + 0.33), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(None, "−", (-1.38, yw + 0.33), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(None, "U_0 = 9 V", (-1.6, yw - 0.42), groesse=24, ausrichtung="center")
    for k in range(5):
        y = yo - 0.2 - k * 0.35
        ladung(s, xa + 0.2, y, plus=True, r=0.12)
        ladung(s, xb - 0.2, y, plus=False, r=0.12)
    s.pfeil((xa + 0.36, 0.25), (xb - 0.36, 0.25), "", farbe=GRUEN, spitze=0.18, dicke=2.5)
    s.pfeil((xa + 0.36, 0.95), (xb - 0.36, 0.95), "", farbe=GRUEN, spitze=0.18, dicke=2.5)
    s.pfeil((xa + 0.36, -0.45), (xb - 0.36, -0.45), "", farbe=GRUEN, spitze=0.18, dicke=2.5)
    s.text(None, "E", (0.5 * (xa + xb), 0.6), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(None, "A", (xa, yo + 0.25), groesse=24, ausrichtung="center")
    s.text(None, "B", (xb, yo + 0.25), groesse=24, ausrichtung="center")
    s.text(None, s.tr("isolator", "Isolator", "insulator", "aislante", "绝缘体"), (0.5 * (xa + xb), yu - 0.27), groesse=23, ausrichtung="center", farbe=BRAUN)
    # Elektronen und Strom in den Zuleitungen
    for y in (-0.05, -0.55, -1.05):
        ladung(s, xl, y, plus=False, r=0.12)
        ladung(s, xr, y, plus=False, r=0.12)
    s.pfeil((xl + 0.27, -0.1), (xl + 0.27, -1.0), "", farbe=BLAU, spitze=0.18, dicke=2.5)
    s.pfeil((xr - 0.27, -1.0), (xr - 0.27, -0.1), "", farbe=BLAU, spitze=0.18, dicke=2.5)
    s.pfeil((xl - 0.27, -1.0), (xl - 0.27, -0.1), "", farbe=ROT, spitze=0.18, dicke=2.5)
    s.pfeil((xr + 0.27, -0.1), (xr + 0.27, -1.0), "", farbe=ROT, spitze=0.18, dicke=2.5)
    s.text(None, "i", (xl - 0.45, -0.55), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, "i", (xr + 0.45, -0.55), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, s.tr("elektronen", "Elektronen", "electrons", "electrones", "电子"), (xl - 0.2, 0.62), groesse=23, ausrichtung="center", farbe=BLAU)
    s.text(None, s.tr("elektronen", "Elektronen", "electrons", "electrones", "电子"), (xr + 0.2, 0.62), groesse=23, ausrichtung="center", farbe=BLAU)
    # Schaltzeichen
    x = 2.1
    s.bauteil("capacitor", (x, 0.0), drehung=270, laenge=2.0, label="C", voltage="u_C", current="i", font_size=26, size=0.9, label_flip=True)
    s.text(None, s.tr("schaltzeichen", "Schaltzeichen", "circuit symbol", "símbolo", "电路符号"), (x, -1.45), groesse=23, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def paar(s, cx, cy, n, breite=1.0, hoehe=1.3):
    """Plattenpaar mit n Ladungen je Platte und n Feldpfeilen."""
    xa, xb = cx - 0.5 * breite, cx + 0.5 * breite
    platte(s, xa, cy - 0.5 * hoehe, cy + 0.5 * hoehe, breite=0.1)
    platte(s, xb, cy - 0.5 * hoehe, cy + 0.5 * hoehe, breite=0.1)
    for k in range(n):
        y = cy + hoehe * ((k + 0.5) / n - 0.5)
        s.pfeil((xa + 0.08, y), (xb - 0.08, y), "", farbe=GRUEN, spitze=0.16, dicke=2)


def k3qu():
    """Doppelte Ladung, doppeltes Feld, doppelte Spannung; rechts die Gerade Q über U."""
    s = Szene("et1/k3qu")
    s.welt()
    paar(s, -2.5, 0.62, 3, hoehe=1.05)
    s.text(None, "Q", (-3.32, 0.62), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, "U", (-1.68, 0.62), groesse=26, ausrichtung="center", farbe=BLAU)
    paar(s, -2.5, -0.68, 6, hoehe=1.05)
    s.text(None, "2 Q", (-3.38, -0.68), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(None, "2 U", (-1.62, -0.68), groesse=26, ausrichtung="center", farbe=BLAU)
    a = s.achsen((0, 10, 3), (0, 1000, 500), breite=3.6, hoehe=2.0, mitte=(1.45, 0.0), xl=s.tr("u_in_v", "U in V", "U in V", "U en V", "U / V"),
                 yl=s.tr("q_in_uc", "Q in µC", "Q in µC", "Q en µC", "Q / µC"), gitter=True, xticks="0;3;6;9")
    s.kurve(a, "100*x", x=(0, 10), farbe=BLAU)
    s.kurve(a, "50*x", x=(0, 10), farbe=ORANGE)
    s.punkt(a, 9, 900, farbe=BLAU)
    s.punkt(a, 9, 450, farbe=ORANGE)
    s.text(a, "C_1 = 100 µF", (1.2, 760), groesse=24, farbe=BLAU)
    s.text(a, "C_2 = 50 µF", (5.8, 200), groesse=24, farbe=BRAUN)
    s.text(a, "900 µC", (7.7, 930), groesse=23, ausrichtung="right", farbe=BLAU)
    s.text(a, "450 µC", (8.7, 590), groesse=23, ausrichtung="right", farbe=BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k3rampe():
    """Stromquelle lädt über R: u_R springt und bleibt, u_C steigt gerade an."""
    s = Szene("et1/k3rampe")
    s.welt()
    xl, xr, yo, yu = -3.15, -1.1, 0.95, -0.95
    s.bauteil("isource", (xl, 0), drehung=90, laenge=1.9, label="", size=0.75)
    s.pfeil((xl, 0.55), (xl, 0.87), "", farbe=ROT, spitze=0.2, dicke=2.5)
    s.text(None, "I", (xl + 0.2, 0.7), groesse=26, ausrichtung="center", farbe=ROT)
    s.draht((xl, yo), (-2.55, yo))
    s.bauteil("switch", (-2.2, yo), drehung=0, laenge=0.7, label="", size=0.6)
    s.draht((-1.85, yo), (xr, yo))
    s.text(None, "S", (-2.2, yo + 0.4), groesse=24, ausrichtung="center")
    s.bauteil("resistor", (xr, 0.475), drehung=270, laenge=0.95, label="R", voltage="u_R", size=0.6, label_flip=True, font_size=24)
    s.bauteil("capacitor", (xr, -0.475), drehung=270, laenge=0.95, label="C", voltage="u_C", size=0.8, label_flip=True, font_size=24)
    s.draht((xl, yu), (xr, yu))
    a = s.achsen((0, 2, 0.5), (0, 18, 9), breite=3.4, hoehe=1.9, mitte=(1.75, 0.0), xl=t_achse(s), yl=s.tr("u_in_v2", "u in V", "u in V", "u en V", "u / V"), gitter=True)
    s.linie(a, (0, 9), (2, 9), farbe=ORANGE, dicke=4)
    s.kurve(a, "9*x", x=(0, 2), farbe=BLAU)
    s.punkt(a, 1, 9, farbe=ROT)
    s.text(a, "u_R = R I", (0.12, 10.4), groesse=24, farbe=BRAUN)
    s.text(a, "u_C = I t / C", (0.5, 14.0), groesse=24, farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k3platte():
    """Links Luft: E = U/d. Rechts Dielektrikum mit ε_r = 2: doppelte Plattenladung, die Hälfte der Linien endet auf gebundener Ladung."""
    s = Szene("et1/k3platte")
    h, b = 2.08, 1.9
    n = 8
    ys = [-0.91 + 0.26 * k for k in range(n)]
    # links
    cx = -2.0
    xa, xb = cx - 0.5 * b, cx + 0.5 * b
    platte(s, xa, -h / 2, h / 2)
    platte(s, xb, -h / 2, h / 2)
    for k, y in enumerate(ys):
        if k % 2 == 0:
            ladung(s, xa + 0.19, y, True, r=0.115)
            ladung(s, xb - 0.19, y, False, r=0.115)
            s.pfeil((xa + 0.33, y), (xb - 0.33, y), "", farbe=GRUEN, spitze=0.17, dicke=2.5)
    s.pfeil((xa, -1.3), (xb, -1.3), "", doppelt=True, spitze=0.18, dicke=2)
    s.text(None, "d", (cx, -1.55), groesse=26, ausrichtung="center")
    s.text(None, s.tr("luft", "Luft: ε_r = 1", "air: ε_r = 1", "aire: ε_r = 1", "空气：ε_r = 1"), (cx, 1.4), groesse=24, ausrichtung="center")
    s.text(None, "U", (xa - 0.3, 0), groesse=26, ausrichtung="center", farbe=BLAU)
    s.text(None, s.tr("flaeche_a", "Fläche A", "area A", "área A", "面积 A"), (xb + 0.1, 1.12), groesse=24, ausrichtung="center")
    # rechts
    cx = 1.75
    xa, xb = cx - 0.5 * b, cx + 0.5 * b
    s.box("", (cx, 0), breite=b - 0.12, hoehe=h, farbe=HELLORANGE, fuellung=HELLORANGE, deckung=1.0, dicke=0)
    platte(s, xa, -h / 2, h / 2)
    platte(s, xb, -h / 2, h / 2)
    for k, y in enumerate(ys):
        ladung(s, xa + 0.19, y, True, r=0.115)
        ladung(s, xb - 0.19, y, False, r=0.115)
        if k % 2 == 0:
            s.pfeil((xa + 0.33, y), (xb - 0.33, y), "", farbe=GRUEN, spitze=0.17, dicke=2.5)
        else:                                                  # Kette aus Dipolen: innen hebt sich alles auf
            for j in range(3):
                x0 = xa + 0.47 + j * 0.34
                s.box("", (x0 + 0.05, y), breite=0.3, hoehe=0.17, form="rect", farbe=GRAU, fuellung="#ffffff", deckung=0.9, dicke=1.5)
                s.text(None, "−", (x0 - 0.03, y), groesse=22, ausrichtung="center", farbe=BLAU)
                s.text(None, "+", (x0 + 0.13, y), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(None, s.tr("dielektrikum", "Dielektrikum: ε_r = 2", "dielectric: ε_r = 2", "dieléctrico: ε_r = 2", "电介质：ε_r = 2"), (cx, 1.4), groesse=24, ausrichtung="center")
    s.text(None, "U", (xa - 0.3, 0), groesse=26, ausrichtung="center", farbe=BLAU)
    s.text(None, s.tr("gebunden", "gebundene Ladung", "bound charge", "carga ligada", "束缚电荷"), (cx, -1.32), groesse=24, ausrichtung="center", farbe=BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k3bauform():
    """Vier Wege zu großer Kapazität: rollen, stapeln, dünne Oxidschicht, Doppelschicht."""
    s = Szene("et1/k3bauform")
    w = s.welt()
    cx = (-2.6, -0.87, 0.87, 2.6)
    # Folie: zwei ineinanderliegende Spiralen
    c = cx[0]
    s.weg(None, f"{c}+(0.08+0.043*t)*cos(t)", f"(0.08+0.043*t)*sin(t)", 0, 15.5, farbe=ROT, dicke=3, n=241)
    s.weg(None, f"{c}+(0.08+0.043*t)*cos(t+3.14159)", f"(0.08+0.043*t)*sin(t+3.14159)", 0, 15.5, farbe=BLAU, dicke=3, n=241)
    # Keramik: Kammstruktur
    c = cx[1]
    s.box("", (c, 0), breite=1.3, hoehe=1.3, farbe=GRAU, fuellung=HELLORANGE, deckung=1.0, dicke=2)
    s.box("", (c - 0.71, 0), breite=0.14, hoehe=1.3, farbe=SCHWARZ, fuellung="#8c8c8c", deckung=1.0, dicke=1.5)
    s.box("", (c + 0.71, 0), breite=0.14, hoehe=1.3, farbe=SCHWARZ, fuellung="#8c8c8c", deckung=1.0, dicke=1.5)
    for k in range(7):
        y = -0.48 + 0.16 * k
        if k % 2 == 0:
            s.linie(None, (c - 0.64, y), (c + 0.42, y), farbe=ROT, dicke=3)
        else:
            s.linie(None, (c + 0.64, y), (c - 0.42, y), farbe=BLAU, dicke=3)
    # Elko: aufgeraute Aluminiumfläche, dünnes Oxid, Elektrolyt
    c = cx[2]
    x0, x1 = c - 0.72, c + 0.72
    zack = f"(-0.2+1.6*abs(mod(x-({x0}),0.3)-0.15))"
    s.flaeche(w, zack, x0, x1, f2="-0.65", farbe="#8c8c8c", deckung=1.0)
    s.flaeche(w, f"({zack}+0.1)", x0, x1, f2=zack, farbe=ORANGE, deckung=1.0)
    s.flaeche(w, "0.65", x0, x1, f2=f"({zack}+0.1)", farbe=HELLBLAU, deckung=1.0)
    # Supercap: Kohle, Ionen in der Doppelschicht
    c = cx[3]
    s.box("", (c - 0.45, 0), breite=0.55, hoehe=1.3, farbe=SCHWARZ, fuellung="#8c8c8c", deckung=1.0, dicke=1.5)
    s.box("", (c + 0.3, 0), breite=0.95, hoehe=1.3, farbe=HELLBLAU, fuellung=HELLBLAU, deckung=1.0, dicke=0)
    for k in range(5):
        y = -0.5 + 0.25 * k
        s.text(None, "+", (c - 0.27, y), groesse=22, ausrichtung="center", farbe=ROT)
        ladung(s, c - 0.03, y, False, r=0.1, groesse=22)
    ladung(s, c + 0.42, 0.33, False, r=0.1, groesse=22)
    ladung(s, c + 0.56, -0.2, True, r=0.1, groesse=22)
    z = -1.05
    for x, a_, b_ in zip(cx, (("folie", "Folie", "film", "película", "薄膜"), ("keramik", "Keramik", "ceramic", "cerámica", "陶瓷"),
                              ("elko", "Elko", "electrolytic", "electrolítico", "电解"), ("super", "Supercap", "supercap", "supercap", "超级电容")),
                         (("f2", "A groß: gerollt", "large A: rolled", "A grande: enrollado", "A 大：卷绕"), ("k2", "ε groß, viele Lagen", "large ε, many layers", "ε grande, capas", "ε 大，多层"),
                          ("e2", "d klein: Oxid", "small d: oxide", "d pequeño: óxido", "d 小：氧化层"), ("s2", "d ≈ 1 nm", "d ≈ 1 nm", "d ≈ 1 nm", "d ≈ 1 nm"))):
        s.text(None, s.tr(*a_), (x, z), groesse=24, ausrichtung="center")
        s.text(None, s.tr(*b_), (x, z - 0.36), groesse=22, ausrichtung="center", farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k3energie():
    """Jede Portion Ladung läuft gegen die schon vorhandene Spannung: Fläche = Energie. Rechts: Die Energie sitzt im Feld."""
    s = Szene("et1/k3energie")
    s.welt()
    a = s.achsen((0, 900, 300), (0, 9, 3), breite=3.7, hoehe=2.0, mitte=(-1.35, 0.0), xl=s.tr("q_in_uc2", "q in µC", "q in µC", "q en µC", "q / µC"),
                 yl=s.tr("u_in_v3", "u in V", "u in V", "u en V", "u / V"), gitter=True)
    dq = 150.0
    for k in range(6):
        um = (k + 0.5) * dq / 100.0                   # Spannung in der Mitte der Portion
        s.band(a, k * dq, (k + 1) * dq, 0, um, farbe=ORANGE if k == 4 else BLAU, deckung=0.55 if k == 4 else 0.18)
    s.kurve(a, "x/100", x=(0, 900), farbe=BLAU)
    s.text(a, "u = q / C", (30, 6.2), groesse=24, farbe=BLAU)
    s.text(a, "W = ½ Q U = 4.05 mJ", (30, 7.4), groesse=24, farbe=BLAU)
    s.pfeil((560, 2.3), (660, 2.3), "", farbe=BRAUN, spitze=0.14, dicke=2, on=a, doppelt=True)
    s.text(a, "Δq", (610, 3.2), groesse=23, ausrichtung="center", farbe=BRAUN)
    s.text(a, "u Δq", (610, 1.2), groesse=23, ausrichtung="center", farbe=BRAUN)
    xa, xb = 1.75, 3.2
    yh = 0.8
    s.box("", (0.5 * (xa + xb), 0), breite=xb - xa, hoehe=2 * yh, farbe=HELLGRUEN, fuellung=HELLGRUEN, deckung=1.0, dicke=0)
    platte(s, xa, -yh, yh)
    platte(s, xb, -yh, yh)
    for y in (-0.6, -0.2, 0.2, 0.6):
        s.pfeil((xa + 0.1, y), (xb - 0.1, y), "", farbe=GRUEN, spitze=0.18, dicke=2.5)
    s.text(None, "w = ½ ε E²", (0.5 * (xa + xb), yh + 0.32), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(None, s.tr("metall0", "im Metall: E = 0", "in the metal: E = 0", "en el metal: E = 0", "金属内：E = 0"), (0.5 * (xa + xb), -yh - 0.3), groesse=23, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k3schaltungen():
    """Parallel: gleiche Spannung, Ladungen addieren sich. Reihe: gleiche Ladung, Spannungen addieren sich."""
    s = Szene("et1/k3schaltungen")
    yo, yu = 1.0, -1.0
    # parallel
    xq, x1, x2 = -3.3, -2.2, -0.95
    s.bauteil("vsource_dc", (xq, 0), drehung=270, laenge=2.0, label="")
    s.text(None, "9 V", (xq + 0.12, 0.55), groesse=24)
    s.bauteil("capacitor", (x1, 0), drehung=270, laenge=2.0, label="C_1", font_size=24, size=0.9)
    s.bauteil("capacitor", (x2, 0), drehung=270, laenge=2.0, label="C_2", font_size=24, size=0.9)
    s.draht((xq, yo), (x2, yo))
    s.draht((xq, yu), (x2, yu))
    s.punkt(None, x1, yo, r=0.06)
    s.punkt(None, x1, yu, r=0.06)
    s.text(None, "900 µC", (x1 + 0.1, -0.55), groesse=23, ausrichtung="left", farbe=ROT)
    s.text(None, "450 µC", (x2 + 0.1, -0.55), groesse=23, ausrichtung="left", farbe=ROT)
    s.text(None, s.tr("parallel", "parallel", "parallel", "en paralelo", "并联"), (-1.9, 1.35), groesse=24, ausrichtung="center")
    # Reihe
    xq, xc = 0.75, 2.0
    s.bauteil("vsource_dc", (xq, 0), drehung=270, laenge=2.0, label="")
    s.text(None, "9 V", (xq + 0.12, 0.55), groesse=24)
    s.bauteil("capacitor", (xc, 0.5), drehung=270, laenge=1.0, label="C_1", font_size=24, size=0.9, label_flip=True)
    s.bauteil("capacitor", (xc, -0.5), drehung=270, laenge=1.0, label="C_2", font_size=24, size=0.9, label_flip=True)
    s.draht((xq, yo), (xc, yo))
    s.draht((xq, yu), (xc, yu))
    s.box("", (xc, 0), breite=0.95, hoehe=0.72, farbe=ROT, fuellung="#ffffff", deckung=0.0, dicke=2, dash=DASH)
    x = xc + 0.62
    s.text(None, "3 V", (x, 0.82), groesse=24, farbe=BLAU)
    s.text(None, "300 µC", (x, 0.5), groesse=23, farbe=ROT)
    s.text(None, s.tr("insel", "Insel", "island", "isla", "孤岛"), (x, 0.0), groesse=23, farbe=ROT)
    s.text(None, "300 µC", (x, -0.5), groesse=23, farbe=ROT)
    s.text(None, "6 V", (x, -0.82), groesse=24, farbe=BLAU)
    s.text(None, s.tr("reihe", "Reihe", "series", "en serie", "串联"), (1.55, 1.35), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def umkreis(s, cx, stellung, t1, t2, insel=False):
    """Quelle, Umschalter, C_1 und C_2 an gemeinsamer Masse. stellung = 1 oder 2."""
    xq, xc, x2 = cx - 1.45, cx - 0.2, cx + 0.8
    yo, yu, yk = 1.05, -1.0, 0.68
    k = 0.3
    s.bauteil("vsource_dc", (xq, 0.025), drehung=270, laenge=2.05, label="")
    s.text(None, "9 V", (xq + 0.12, 0.5), groesse=24)
    s.draht((xq, yo), (xc - k, yo))
    s.draht((xc + k, yo), (x2, yo), (x2, 0.25))
    s.draht((xc, yk), (xc, 0.25))
    s.draht((xq, yu), (x2, yu), (x2, -0.25))
    s.draht((xc, -0.25), (xc, yu))
    s.bauteil("capacitor", (xc, 0), drehung=270, laenge=0.5, label="", size=0.8)
    s.bauteil("capacitor", (x2, 0), drehung=270, laenge=0.5, label="", size=0.8)
    s.text(None, "C_1", (xc + 0.12, -0.42), groesse=24)
    s.text(None, "C_2", (x2 - 0.12, -0.42), groesse=24, ausrichtung="right")
    s.linie(None, (xc, yk), (xc + (-k if stellung == 1 else k), yo), dicke=3)
    klemme(s, xc - k, yo)
    klemme(s, xc + k, yo)
    s.punkt(None, xc, yk, r=0.06)
    s.punkt(None, xc, yu, r=0.06)
    s.text(None, "1", (xc - k, yo + 0.25), groesse=22, ausrichtung="center")
    s.text(None, "2", (xc + k, yo + 0.25), groesse=22, ausrichtung="center")
    s.text(None, t1, (xc - 0.12, -0.5), groesse=23, ausrichtung="right", farbe=ROT)
    s.text(None, t2, (x2 + 0.12, -0.5), groesse=23, ausrichtung="left", farbe=ROT)
    masse(s, cx - 0.7, yu - 0.02, groesse=0.65)
    if insel:
        s.box("", (0.5 * (xc + x2), 0.5 * (yo + 0.13)), breite=x2 - xc + 0.42, hoehe=yo + 0.13, farbe=ROT, fuellung="#ffffff", deckung=0.0, dicke=2, dash=DASH)


def k3umladen():
    """Stellung 1: C_1 wird geladen. Stellung 2: Die Ladung verteilt sich, die Summe bleibt."""
    s = Szene("et1/k3umladen")
    umkreis(s, -1.85, 1, "900 µC", "0")
    umkreis(s, 1.75, 2, "600 µC", "300 µC", insel=True)
    s.text(None, s.tr("st1", "Stellung 1: 9 V und 0 V", "position 1: 9 V and 0 V", "posición 1: 9 V y 0 V", "位置 1：9 V 和 0 V"), (-1.95, 1.65), groesse=24, ausrichtung="center")
    s.text(None, s.tr("st2", "Stellung 2: beide 6 V", "position 2: both 6 V", "posición 2: ambos 6 V", "位置 2：均为 6 V"), (1.65, 1.65), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k3rckreis():
    """Links der RC-Kreis mit Umschalter, rechts die beiden Ersatzbilder für t = 0 und t gegen unendlich."""
    s = Szene("et1/k3rckreis")
    xq, xk, xp, xc = -3.3, -2.8, -2.3, -1.0
    yo, yu = 1.0, -1.0
    s.bauteil("vsource_dc", (xq, 0), drehung=270, laenge=2.0, label="")
    s.text(None, "U_0", (xq + 0.1, 0.52), groesse=24)
    s.draht((xq, yo), (xk, yo))
    klemme(s, xk, yo)
    klemme(s, xk, 0.45)
    s.punkt(None, xp, yo, r=0.06)
    s.linie(None, (xp, yo), (xk, yo), dicke=3)
    s.text(None, "1", (xk, yo + 0.26), groesse=22, ausrichtung="center")
    s.text(None, "2", (xk + 0.17, 0.3), groesse=22, ausrichtung="center")
    s.text(None, "S", (0.5 * (xk + xp), yo + 0.26), groesse=24, ausrichtung="center")
    s.draht((xk, 0.39), (xk, yu))
    s.bauteil("resistor", (-1.65, yo), drehung=0, laenge=1.3, label="R", voltage="u_R", current="i", size=0.6, font_size=24)
    s.bauteil("capacitor", (xc, 0), drehung=270, laenge=2.0, label="C", voltage="u_C", size=0.9, label_flip=True, font_size=24)
    s.draht((xq, yu), (xc, yu))

    def ersatz(cx, kurz, titel, z1, z2):
        x0, x1 = cx - 0.62, cx + 0.62
        s.bauteil("vsource_dc", (x0, 0), drehung=270, laenge=2.0, label="", size=0.7)
        s.bauteil("resistor", (cx, yo), drehung=0, laenge=x1 - x0, label="R", size=0.5, font_size=24)
        s.draht((x0, yu), (x1, yu))
        if kurz:
            s.draht((x1, yo), (x1, yu))
        else:
            s.draht((x1, yo), (x1, 0.2))
            s.draht((x1, -0.2), (x1, yu))
            klemme(s, x1, 0.2)
            klemme(s, x1, -0.2)
        s.text(None, titel, (cx, yo + 0.72), groesse=24, ausrichtung="center", farbe=ROT)
        s.text(None, z1, (cx, yu - 0.32), groesse=23, ausrichtung="center", farbe=BLAU)
        s.text(None, z2, (cx, yu - 0.68), groesse=23, ausrichtung="center", farbe=BLAU)

    ersatz(0.85, True, "t = 0", "u_C = 0", "i = U_0 / R")
    ersatz(2.55, False, "t → ∞", "u_C = U_0", "i = 0")
    s.text(None, s.tr("kreis", "Stellung 1: Laden", "position 1: charging", "posición 1: carga", "位置 1：充电"), (-2.2, yo + 0.72), groesse=24, ausrichtung="center")
    s.speichern()


def k3richtung():
    """Richtungsfeld der Gleichung: An jedem Punkt liegt die Steigung fest; der Startwert wählt die Kurve."""
    s = Szene("et1/k3richtung")
    br, ho = 5.2, 2.0
    a = s.achsen((0, 5, 1), (0, 12, 3), breite=br, hoehe=ho, mitte=(0, 0), xl=t_achse(s), yl=s.tr("uc_in_v", "u_C in V", "u_C in V", "u_C en V", "u_C / V"), gitter=False)
    sx, sy = br / 5, ho / 12
    L = 0.09
    for i in range(0, 11):
        t = i * 0.5
        for j in range(0, 9):
            u = 0.75 + j * 1.35
            m = 9.0 - u                                        # Steigung in V/s bei tau = 1 s
            n = sqrt(sx ** 2 + (m * sy) ** 2)
            dt = L / n
            s.linie(a, (t - dt, u - m * dt), (t + dt, u + m * dt), farbe="#9a9a9a", dicke=2.5)
    s.kurve(a, "9*(1-exp(-x))", x=(0, 5), farbe=BLAU)
    s.kurve(a, "9-6*exp(-x)", x=(0, 5), farbe=GRUEN)
    s.kurve(a, "9+3*exp(-x)", x=(0, 5), farbe=ORANGE)
    s.linie(a, (0, 9), (5, 9), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(a, 0, 0, farbe=BLAU)
    s.punkt(a, 0, 3, farbe=GRUEN)
    s.punkt(a, 0, 12, farbe=ORANGE)
    s.text(a, "U_0", (5.02, 9), groesse=24, farbe=ROT)
    s.speichern()


def k3laden():
    """Aufladen im Rechenmodell: Spannungen und Strom mit Tangente am Start."""
    s = Szene("et1/k3laden")
    a = s.achsen((0, 5, 1), (0, 9, 3), breite=3.0, hoehe=1.95, mitte=(-1.85, 0), xl=t_achse(s), yl=s.tr("u_in_v2", "u in V", "u in V", "u en V", "u / V"), gitter=True)
    s.kurve(a, "9*(1-exp(-x))", x=(0, 5), farbe=BLAU)
    s.kurve(a, "9*exp(-x)", x=(0, 5), farbe=ORANGE)
    s.linie(a, (0, 0), (1, 9), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(a, 1, 5.689, farbe=BLAU)
    s.punkt(a, 1, 3.311, farbe=ORANGE)
    s.text(a, "u_C", (3.0, 6.95), groesse=26, farbe=BLAU)
    s.text(a, "u_R", (2.0, 2.3), groesse=26, farbe=BRAUN)
    s.text(a, "5.69 V", (1.15, 4.95), groesse=23, farbe=BLAU)
    s.text(a, "3.31 V", (1.15, 3.85), groesse=23, farbe=BRAUN)
    s.text(a, s.tr("tangente", "Tangente", "tangent", "tangente", "切线"), (1.15, 8.3), groesse=23, farbe=ROT)
    b = s.achsen((0, 5, 1), (0, 0.9, 0.3), breite=2.6, hoehe=1.95, mitte=(1.95, 0), xl=t_achse(s), yl=s.tr("i_in_ma", "i in mA", "i in mA", "i en mA", "i / mA"), gitter=True)
    s.kurve(b, "0.9*exp(-x)", x=(0, 5), farbe=GRUEN)
    s.linie(b, (0, 0.9), (1, 0), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(b, 1, 0.3311, farbe=GRUEN)
    s.text(b, "0.331 mA", (1.2, 0.4), groesse=23, farbe=GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def k3entladen():
    """Fünf Sekunden laden, fünf Sekunden entladen: oben die Spannung, unten der Strom."""
    s = Szene("et1/k3entladen")
    br = 5.6
    a = s.achsen((0, 10, 1), (0, 9, 3), breite=br, hoehe=1.45, mitte=(0, 1.1), xl="", yl=s.tr("uc_in_v", "u_C in V", "u_C in V", "u_C en V", "u_C / V"), gitter=True, xzahlen=False)
    u5 = 9 * (1 - exp(-5))
    s.kurve(a, "9*(1-exp(-x))", x=(0, 5), farbe=BLAU)
    s.kurve(a, f"{u5:.5f}*exp(-(x-5))", x=(5, 10), farbe=BLAU)
    for n, txt in ((1, "63 %"), (2, "86 %"), (3, "95 %")):
        y = 9 * (1 - exp(-n))
        s.punkt(a, n, y, farbe=ROT, r=0.06)
        s.text(a, txt, (n + 0.05, y - 1.4), groesse=23, farbe=ROT)
    for n, txt in ((1, "37 %"), (2, "14 %"), (3, "5 %")):
        y = u5 * exp(-n)
        s.punkt(a, 5 + n, y, farbe=ROT, r=0.06)
        s.text(a, txt, (5 + n + 0.05, y + 1.1), groesse=23, farbe=ROT)
    b = s.achsen((0, 10, 1), (-0.9, 0.9, 0.9), breite=br, hoehe=1.45, mitte=(0, -1.0), xl=t_achse(s), yl=s.tr("i_in_ma", "i in mA", "i in mA", "i en mA", "i / mA"), gitter=True)
    s.linie(b, (0, 0), (10, 0), farbe=GRAU, dicke=2)
    s.kurve(b, "0.9*exp(-x)", x=(0, 5), farbe=GRUEN)
    s.kurve(b, f"-{u5 / 10:.5f}*exp(-(x-5))", x=(5, 10), farbe=GRUEN)
    s.linie(b, (5, 0.9 * exp(-5)), (5, -u5 / 10), farbe=GRUEN, dicke=3, dash=DASH)
    s.linie(b, (0, 0), (0, 0.9), farbe=GRUEN, dicke=3, dash=DASH)
    s.text(b, s.tr("laden_t", "Laden", "charging", "carga", "充电"), (2.4, 0.5), groesse=24, farbe=GRUEN)
    s.text(b, s.tr("entladen_t", "Entladen", "discharging", "descarga", "放电"), (7.0, -0.55), groesse=24, farbe=GRUEN)
    s.speichern()


if __name__ == "__main__":
    for f in (k3aufbau, k3qu, k3rampe, k3platte, k3bauform, k3energie, k3schaltungen, k3umladen, k3rckreis, k3richtung, k3laden, k3entladen):
        f()
