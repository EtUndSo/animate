"""ET1 Teil 10 (kap10_stufen.tex): Der Bipolartransistor.

Aufruf: python tools/szenen/et1_teil10.py, danach python tools/szenen_ansehen.py out.png et1/k10aufbau ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap10.py.
"""
import sys
from math import atan2, degrees, exp, hypot, tanh
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

HELLROT, HELLBLAU, HELLORANGE = "#f6dede", "#dceafa", "#fbe6d3"
GR = 24           # Beschriftung in Schaltbildern
UT, IS, BB = 0.026, 1.9e-13, 200.0


def ic(ube, uce):
    """Modellfläche in A; Rückstrom und Early-Faktor wie Gl. k10flaeche."""
    return IS * exp(ube / UT) * (1 - exp(-uce / UT)) * (1 + (uce - 6) / 80)


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def wid(s, a, b, size=0.42, farbe=SCHWARZ):
    return bau(s, "resistor", a, b, size=size, farbe=farbe)


def kl(s, x, y, name="", dx=0.0, dy=0.25, farbe=SCHWARZ):
    s.kreis(None, x, y, 0.06, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        s.text(None, name, (x + dx, y + dy), groesse=GR, ausrichtung="center", farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.055):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def spfeil(s, a, b, txt="", p=None, farbe=BLAU, ausr="left"):
    s.pfeil(a, b, "", farbe=farbe, spitze=0.16, dicke=2.5)
    if txt:
        t(s, txt, p, ausr, farbe)


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center"):
    s.pfeil(a, b, "", farbe=farbe, spitze=0.16, dicke=3)
    if txt:
        t(s, txt, p, ausr, farbe)


def tr_npn(s, x, y, g=0.6, art="npn", flip=False):
    """Transistor um (x, y); liefert die Pins B, C, E (bei flip tauschen C und E den Platz)."""
    s.geraet(art, (x, y), groesse=g, flip=flip)
    oben, unten = (x + 0.5 * g, y + g), (x + 0.5 * g, y - g)
    return (x - g, y), (unten if flip else oben), (oben if flip else unten)


def masse(s, x, y, g=0.55):
    s.geraet("ground", (x, y), groesse=g)


def i_ma(s):
    return s.tr("ic_ma", "I_C in mA", "I_C in mA", "I_C en mA", "I_C / mA")


def v_achse(s, name, key):
    return s.tr(key, name + " in V", name + " in V", name + " en V", name + " / V")


def uein(s):
    return s.tr("uein", "U_{ein}", "U_{in}", "U_{ent}", "U_{in}")


def uaus(s):
    return s.tr("uaus", "U_{aus}", "U_{out}", "U_{sal}", "U_{out}")


def uein_v(s):
    return s.tr("uein_v", "U_{ein} in V", "U_{in} in V", "U_{ent} en V", "U_{in} / V")


def uaus_v(s):
    return s.tr("uaus_v", "U_{aus} in V", "U_{out} in V", "U_{sal} en V", "U_{out} / V")


# ------------------------------------------------------------------------------------------ Stufe 1
def stapel(s, x, namen, dot, farbe_rand, farbe_mitte):
    """Senkrechte Schichtfolge von oben nach unten, drei Rechtecke, Mitte als dünne Basis."""
    b = 1.0
    yo, ym1, ym2, yu = 1.0, 0.13, -0.13, -1.0
    for (y0, y1, nam, d, f) in ((yo, ym1, namen[0], dot[0], farbe_rand), (ym2, yu, namen[2], dot[2], farbe_rand)):
        s.box("", (x, 0.5 * (y0 + y1)), breite=b, hoehe=y0 - y1, fuellung=f, dicke=2)
        t(s, nam, (x, 0.5 * (y0 + y1) + 0.14), g=22)
        t(s, d, (x, 0.5 * (y0 + y1) - 0.17), g=22)
    s.box("", (x, 0), breite=b, hoehe=ym1 - ym2, fuellung=farbe_mitte, dicke=2)
    t(s, dot[1], (x, -0.015), g=22)
    t(s, namen[1], (x - 0.58, -0.015), "right", g=22)


def k10aufbau():
    """Schichtfolge und Schaltzeichen von npn und pnp."""
    s = Szene("et1/k10aufbau")
    kol = s.tr("kol", "Kollektor", "collector", "colector", "集电极")
    bas = s.tr("bas", "Basis", "base", "base", "基极")
    emi = s.tr("emi", "Emitter", "emitter", "emisor", "发射极")
    # npn
    x0 = -2.7
    t(s, "npn", (x0 + 0.65, 1.33), g=26)
    stapel(s, x0, (kol, bas, emi), ("n", "p", "n+"), HELLBLAU, HELLORANGE)
    xs = x0 + 1.85
    B, C, E = tr_npn(s, xs, 0, g=0.7)
    s.draht(C, (C[0], 1.15))
    s.draht(E, (E[0], -1.15))
    s.draht(B, (B[0] - 0.3, 0))
    kl(s, C[0], 1.15, "C", dx=-0.2, dy=0)
    kl(s, E[0], -1.15, "E", dx=-0.2, dy=0)
    kl(s, B[0] - 0.3, 0, "B", dy=-0.25)
    ipfeil(s, (C[0], 1.08), (C[0], 0.82), "I_C", (C[0] + 0.1, 0.97), ausr="left")
    ipfeil(s, (E[0], -0.8), (E[0], -1.06), "I_E", (E[0] + 0.1, -0.97), ausr="left")
    ipfeil(s, (B[0] - 0.22, 0), (B[0] + 0.1, 0), "I_B", (B[0] - 0.12, 0.2))
    spfeil(s, (C[0] + 0.3, 0.7), (C[0] + 0.3, -0.7), "U_{CE}", (C[0] + 0.36, 0.42))
    spfeil(s, (B[0] + 0.22, -0.3), (E[0] - 0.36, -0.88), "U_{BE}", (B[0] - 0.02, -0.72), ausr="center")
    spfeil(s, (E[0] - 0.36, 0.88), (B[0] + 0.22, 0.3), "U_{CB}", (B[0] - 0.02, 0.72), ausr="center")
    # pnp
    x1 = 1.05
    t(s, "pnp", (x1 + 0.65, 1.33), g=26)
    stapel(s, x1, (emi, bas, kol), ("p+", "n", "p"), HELLORANGE, HELLBLAU)
    xs = x1 + 1.62
    B, C, E = tr_npn(s, xs, 0, g=0.7, art="pnp", flip=True)
    s.draht(C, (C[0], -1.15))
    s.draht(E, (E[0], 1.15))
    s.draht(B, (B[0] - 0.3, 0))
    kl(s, E[0], 1.15, "E", dx=-0.2, dy=0)
    kl(s, C[0], -1.15, "C", dx=-0.2, dy=0)
    kl(s, B[0] - 0.3, 0, "B", dy=-0.25)
    ipfeil(s, (E[0], 1.08), (E[0], 0.82), "I_E", (E[0] + 0.1, 0.97), ausr="left")
    ipfeil(s, (C[0], -0.8), (C[0], -1.06), "I_C", (C[0] + 0.1, -0.97), ausr="left")
    ipfeil(s, (B[0] + 0.1, 0), (B[0] - 0.22, 0), "I_B", (B[0] - 0.05, 0.22))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k10basis():
    """Elektronenweg durch die drei Gebiete und Energie eines Elektrons über dem Ort."""
    s = Szene("et1/k10basis")
    w = s.welt()
    xe, xb0, xb1, xc = -2.7, -0.55, -0.15, 2.7
    yo, yu = 1.75, 0.75
    s.box("", (0.5 * (xe + xb0), 0.5 * (yo + yu)), breite=xb0 - xe, hoehe=yo - yu, fuellung=HELLBLAU, dicke=2)
    s.box("", (0.5 * (xb0 + xb1), 0.5 * (yo + yu)), breite=xb1 - xb0, hoehe=yo - yu, fuellung=HELLORANGE, dicke=2)
    s.box("", (0.5 * (xb1 + xc), 0.5 * (yo + yu)), breite=xc - xb1, hoehe=yo - yu, fuellung=HELLBLAU, dicke=2)
    t(s, s.tr("emi_n", "Emitter (n+)", "emitter (n+)", "emisor (n+)", "发射极 (n+)"), (-1.65, yo - 0.2), g=22)
    t(s, s.tr("bas", "Basis (p)", "base (p)", "base (p)", "基极 (p)"), (0.5 * (xb0 + xb1), yo + 0.18), g=22)
    t(s, s.tr("kol_n", "Kollektor (n)", "collector (n)", "colector (n)", "集电极 (n)"), (1.3, yo - 0.2), g=22)
    s.pfeil((-2.5, 1.25), (2.5, 1.25), "", farbe=BLAU, spitze=0.24, dicke=5)
    t(s, s.tr("elek", "Elektronen", "electrons", "electrones", "电子"), (-1.65, 1.02), farbe=BLAU, g=22)
    # Verlust und Nachliefern
    s.pfeil((0.5 * (xb0 + xb1), yu), (0.5 * (xb0 + xb1), 0.42), "", farbe=ROT, spitze=0.16, dicke=3)
    t(s, "I_B = 10 µA", (0.5 * (xb0 + xb1) + 0.12, 0.5), "left", ROT, g=22)
    # technische Ströme an den Enden
    s.pfeil((-2.7, 1.25), (-3.25, 1.25), "", farbe=ROT, spitze=0.16, dicke=3)
    t(s, "I_E", (-3.0, 1.46), "center", ROT, g=22)
    t(s, "2.01 mA", (-3.1, 1.02), "center", ROT, g=22)
    s.pfeil((3.25, 1.25), (2.7, 1.25), "", farbe=ROT, spitze=0.16, dicke=3)
    t(s, "I_C", (3.0, 1.46), "center", ROT, g=22)
    t(s, "2 mA", (3.05, 1.02), "center", ROT, g=22)
    # Energie
    pts = []
    n = 240
    for i in range(n + 1):
        x = xe + (xc - xe) * i / n
        y = -0.55 + 0.32 * 0.5 * (1 + tanh((x - xb0 + 0.08) / 0.05)) - 1.45 * 0.5 * (1 + tanh((x - xb1 - 0.12) / 0.09))
        pts.append((x, y))
    s.daten(w, duenn(pts, 2e-4), farbe=SCHWARZ, dicke=4)
    t(s, s.tr("energie", "Energie eines Elektrons", "energy of an electron", "energía de un electrón", "电子的能量"), (-2.7, 0.1), "left", g=22)
    s.kreis(None, -1.1, -0.45, 0.075, BLAU, dicke=0, fuellung=BLAU, deckung=1)
    s.kreis(None, -0.33, -0.13, 0.075, BLAU, dicke=0, fuellung=BLAU, deckung=1)
    s.kreis(None, 0.34, -1.05, 0.075, BLAU, dicke=0, fuellung=BLAU, deckung=1)
    s.pfeil((-0.98, -0.42), (-0.46, -0.16), "", farbe=BLAU, spitze=0.14, dicke=2.5)
    s.pfeil((-0.2, -0.16), (0.25, -0.9), "", farbe=BLAU, spitze=0.14, dicke=2.5)
    t(s, s.tr("stufe", "kleine Stufe, U_{BE} senkt sie", "small step, lowered by U_{BE}", "escalón pequeño, U_{BE} lo baja", "小台阶，U_{BE} 使其降低"),
      (-2.7, -0.82), "left", g=22)
    t(s, s.tr("hang", "Abhang, U_{CB} vertieft ihn", "steep drop, deepened by U_{CB}", "caída, U_{CB} la aumenta", "陡坡，U_{CB} 使其加深"),
      (0.55, -0.32), "left", g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k10flaeche():
    """Die Fläche I_C(U_BE, U_CE) mit den beiden Schnitten durch den Arbeitspunkt."""
    s = Szene("et1/k10flaeche", margin=10)
    x0, x1, y1, z1 = 0.52, 0.62, 8.0, 5.0
    a = s._add("Axes", {"x_range": [x0, x1, 0.02], "y_range": [0, y1, 2], "z_range": [0, z1, 1], "x_length": 3.2, "y_length": 3.6, "z_length": 2.0,
                        "origin": [0, 0, 0], "title": "", "x_label": "", "y_label": "", "number_size": 24, "label_size": 26, "axis_width": 3,
                        "show_axes": False, "x_numbers": False, "y_numbers": False})

    def lin(p, q, farbe=SCHWARZ, d=3):
        s._add("Line", {"start": list(p), "end": list(q), "color": farbe, "stroke_width": d, "dash": ""}, a)

    def txt(z, p, ausr="center", farbe=SCHWARZ, g=22):
        s._add("Text", {"text": z, "position": list(p), "font_size": g, "align": ausr, "color": farbe}, a)

    s._add("FunctionGraph", {"func": "1.9e-10*exp(x/0.026)*(1-exp(-y/0.026))*(1+(y-6)/80)", "color": BLAU, "fill_opacity": 0.72, "res_max": 44, "stroke_width": 1}, a)
    # eigene Achsen an den vorderen Kanten
    lin((x0, y1, 0), (x1, y1, 0))
    lin((x0, 0, 0), (x0, y1, 0))
    lin((x0, 0, 0), (x0, 0, z1))
    for u in (0.54, 0.56, 0.58, 0.6, 0.62):
        lin((u, y1, 0), (u, y1 + 0.2, 0))
        txt("%.2f" % u, (u, y1 + 0.75, 0))
    for u in (2, 4, 6, 8):
        lin((x0, u, 0), (x0 - 0.003, u, 0))
        txt("%d" % u, (x0 - 0.011, u, 0))
    for u in (1, 2, 3, 4, 5):
        lin((x0, 0, u), (x0 - 0.003, 0, u))
        txt("%d" % u, (x0 - 0.008, 0, u), "left")
    txt(v_achse(s, "U_{BE}", "ube_v"), (0.575, y1 + 1.7, 0), g=24)
    txt(v_achse(s, "U_{CE}", "uce_v"), (x0 - 0.024, 4.2, -0.5), g=24)
    txt(i_ma(s), (x0 - 0.006, 0, z1 + 0.55), g=24)

    def icm(u, v):
        return 1e3 * ic(u, v)

    n = 40
    for i in range(n):
        u0, u1 = x0 + (x1 - x0) * i / n, x0 + (x1 - x0) * (i + 1) / n
        lin((u0, 6, icm(u0, 6)), (u1, 6, icm(u1, 6)), ROT, 5)
    n = 60
    for i in range(n):
        v0, v1 = y1 * (i / n) ** 2.5, y1 * ((i + 1) / n) ** 2.5
        lin((0.6, v0, icm(0.6, v0)), (0.6, v1, icm(0.6, v1)), GRUEN, 5)
    s._add("Dot", {"center": [0.6, 6, 2.0], "radius": 0.08, "color": SCHWARZ, "fill_color": SCHWARZ, "fill_opacity": 1, "stroke_width": 0}, a)
    s.model_kamera = (2.35, 0.48)
    speichern3d(s)


def speichern3d(s):
    import json
    m = s.model()
    m["model"]["camera"] = {"mode": "3d", "theta": s.model_kamera[0], "phi": s.model_kamera[1], "zoom": 1.0}
    p = SZENEN / (s.name + ".json")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")


def k10schnitte():
    """Eingangs-/Steuerkennlinie, Ausgangskennlinien, Stromsteuerkennlinie."""
    s = Szene("et1/k10schnitte")
    b, h = 1.65, 2.0
    a = s.achsen((0.5, 0.65, 0.05), (0, 6, 2), breite=b, hoehe=h, mitte=(-2.6, 0), gitter=True, xl=v_achse(s, "U_{BE}", "ube_v"), yl=i_ma(s))
    s.kurve(a, "1.9e-10*exp(x/0.026)", x=(0.5, 0.6375), farbe=BLAU)
    s.punkt(a, 0.6, 2.0, r=0.06)
    for y in (2, 4, 6):
        s.linie(a, (0.65, y), (0.654, y), dicke=2)
        s.text(a, "%d" % (y * 5), (0.656, y - 0.25), groesse=22, farbe=ORANGE)
    s.text(a, s.tr("ib_ua", "I_B in µA", "I_B in µA", "I_B en µA", "I_B / µA"), (0.668, 6.6), groesse=22, ausrichtung="right", farbe=ORANGE)

    m = s.achsen((0, 12, 4), (0, 5, 1), breite=b + 0.2, hoehe=h, mitte=(-0.1, 0), gitter=True, xl=v_achse(s, "U_{CE}", "uce_v"), yl=i_ma(s))
    for k in (1, 2, 3, 4):
        s.kurve(m, "%d*(1-exp(-x/0.026))*(1+(x-6)/80)" % k, x=(0, 12), farbe=ROT if k == 2 else BLAU, dicke=4)
        s.text(m, "%d µA" % (k * 5), (7.0, k * (1 + 1 / 80) + 0.32), groesse=22, farbe=ROT if k == 2 else BLAU)
    s.linie(m, (0.6, 0), (0.6, 5), farbe=GRAU, dicke=2.5, dash=DASH)
    s.punkt(m, 6, 2, r=0.06)

    r = s.achsen((0, 20, 5), (0, 4, 1), breite=b - 0.35, hoehe=h, mitte=(2.3, 0), gitter=True,
                 xl=s.tr("ib_ua", "I_B in µA", "I_B in µA", "I_B en µA", "I_B / µA"), yl=i_ma(s))
    s.kurve(r, "0.2*x", x=(0, 20), farbe=BLAU)
    s.punkt(r, 10, 2, r=0.06)
    s.text(r, "B = 200", (10.5, 0.8), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def ersatz(s, x, art):
    """Ersatzschaltbild um x: B links oben, C rechts oben, E unten."""
    yo, yk, ye = 0.95, -0.85, -1.2
    xl, xr = x - 0.55, x + 0.55
    kl(s, xl - 0.3, yo, "B", dy=0.22)
    kl(s, xr + 0.3, yo, "C", dy=0.22)
    kl(s, x, ye, "E", dx=0.2, dy=0)
    if art == "sperr":
        s.draht((xl - 0.24, yo), (xl + 0.05, yo))
        s.draht((xr - 0.05, yo), (xr + 0.24, yo))
        s.draht((x, ye + 0.06), (x, ye + 0.45))
        return
    s.draht((xl - 0.24, yo), (xl, yo), (xl, 0.5))
    s.draht((xr + 0.24, yo), (xr, yo), (xr, 0.5))
    s.draht((xl, -0.5), (xl, yk), (xr, yk), (xr, -0.5))
    s.draht((x, yk), (x, ye + 0.06))
    kn(s, x, yk)
    bau(s, "vsource", (xl, 0.5), (xl, -0.5), size=0.55)
    t(s, "0.6 V", (xl + 0.33, 0.0), "left", BLAU, g=22)
    t(s, "+", (xl - 0.22, 0.42), farbe=ROT, g=22)
    if art == "aktiv":
        bau(s, "cccs", (xr, 0.5), (xr, -0.5), size=0.55)
        s.pfeil((xr, 0.68), (xr, 0.5), "", farbe=ROT, spitze=0.14, dicke=3)
        t(s, "B I_B", (xr + 0.32, 0.0), "left", ROT, g=22)
    else:
        bau(s, "vsource", (xr, 0.5), (xr, -0.5), size=0.55)
        t(s, "0.2 V", (xr + 0.33, 0.0), "left", BLAU, g=22)
        t(s, "+", (xr - 0.22, 0.42), farbe=ROT, g=22)
    ipfeil(s, (xl - 0.2, yo), (xl - 0.02, yo), "", None)
    t(s, "I_B", (xl - 0.02, yo + 0.2), g=22, farbe=ROT)
    ipfeil(s, (xr + 0.2, yo), (xr + 0.02, yo), "", None)
    t(s, "I_C", (xr + 0.02, yo + 0.2), g=22, farbe=ROT)


def k10esb():
    s = Szene("et1/k10esb")
    xs = (-2.4, -0.05, 2.3)
    ersatz(s, xs[0], "sperr")
    ersatz(s, xs[1], "aktiv")
    ersatz(s, xs[2], "sat")
    t(s, s.tr("t_sperr", "Sperrbereich", "cut-off", "corte", "截止区"), (xs[0], 1.5), g=24)
    t(s, s.tr("t_aktiv", "aktiver Bereich", "active region", "región activa", "放大区"), (xs[1], 1.5), g=24)
    t(s, s.tr("t_sat", "Sättigung", "saturation", "saturación", "饱和区"), (xs[2], 1.5), g=24)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def schaltung_rb(s, x, y0=0.0, rb="R_B"):
    """Emitter an Masse, Kollektorwiderstand, Basiswiderstand; x = Transistor."""
    B, C, E = tr_npn(s, x, y0 - 0.15, g=0.55)
    yt = y0 + 1.4
    wid(s, (C[0], yt), (C[0], C[1] + 0.05))
    s.draht((C[0], C[1] + 0.05), C)
    kl(s, C[0], yt, "U_{CC}", dx=0, dy=0.23)
    t(s, "R_C", (C[0] + 0.2, 0.5 * (yt + C[1])), "left", g=22)
    s.draht(E, (E[0], y0 - 1.05))
    masse(s, E[0], y0 - 1.05)
    wid(s, (B[0] - 0.8, B[1]), (B[0] - 0.1, B[1]))
    s.draht((B[0] - 0.1, B[1]), B)
    kl(s, B[0] - 0.8, B[1], uein(s), dx=-0.0, dy=0.25)
    t(s, rb, (B[0] - 0.45, B[1] + 0.22), g=22)
    return B, C, E


def k10arbeit():
    s = Szene("et1/k10arbeit")
    w = s.welt()
    B, C, E = schaltung_rb(s, -2.05)
    ipfeil(s, (C[0], C[1] + 0.34), (C[0], C[1] + 0.1), "I_C", (C[0] + 0.12, C[1] + 0.03), ausr="left")
    ipfeil(s, (B[0] - 0.04, B[1]), (B[0] + 0.22, B[1]), "I_B", (B[0] + 0.06, B[1] + 0.2))
    spfeil(s, (C[0] + 0.45, C[1] - 0.05), (C[0] + 0.45, E[1] + 0.05), "U_{CE}", (C[0] + 0.52, -0.15))
    a = s.achsen((0, 12.8, 2), (0, 5, 1), breite=3.2, hoehe=2.2, mitte=(1.8, 0), xl=v_achse(s, "U_{CE}", "uce_v"), yl=i_ma(s))
    for k, ub in ((1, "5"), (2, "10"), (3, "15"), (4, "20")):
        s.linie(a, (0.2, k), (12.8, k), farbe=BLAU if k != 2 else ROT, dicke=2.5)
        s.text(a, ub + " µA", (9.4, k + 0.22), groesse=22, farbe=BLAU if k != 2 else ROT)
    s.linie(a, (0.2, 0), (0.2, 5), farbe=BLAU, dicke=2.5)
    s.linie(a, (0.2, 0), (12.8, 0), farbe=ORANGE, dicke=3.5)
    s.linie(a, (0, 4), (12, 0), farbe=SCHWARZ, dicke=3.5)
    for x, y, n, dx, dy in ((6, 2, "A", 0.3, 0.22), (0.2, 3.933, "S", 0.5, -0.42), (12, 0, "Z", 0.35, 0.3)):
        s.punkt(a, x, y, farbe=SCHWARZ, r=0.075)
        s.text(a, n, (x + dx, y + dy), groesse=24)
    s.text(a, s.tr("sp_ib", "Sperrbereich", "cut-off", "corte", "截止区"), (6.6, 0.24), groesse=22, farbe=ORANGE)
    s.text(a, s.tr("t_aktiv", "aktiver Bereich", "active region", "región activa", "放大区"), (4.0, 4.5), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(a, s.tr("t_sat", "Sättigung", "saturation", "saturación", "饱和区"), (0.5, 4.5), groesse=22, ausrichtung="left", farbe=SCHWARZ)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k10schalter():
    s = Szene("et1/k10schalter")
    b, h = 1.5, 1.9
    a = s.achsen((0, 2, 0.5), (0, 12, 4), breite=b, hoehe=h, mitte=(-2.6, 0), gitter=True, xl=uein_v(s), yl=uaus_v(s))
    s.daten(a, [(0, 12), (0.6, 12), (0.9933, 0.2), (2, 0.2)], farbe=BLAU)
    s.linie(a, (0.6, 0), (0.6, 12), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (0.9933, 0), (0.9933, 12), farbe=GRAU, dicke=2, dash=DASH)

    m = s.achsen((0, 6, 1), (0, 12, 4), breite=b, hoehe=h, mitte=(-0.1, 0), xl="t", yl=v_achse(s, "U", "u_v"), xzahlen=False, xmarks=False, gitter=False)
    pe, pa = [], []
    for i in range(6):
        pe += [(i, 5 * (i % 2)), (i + 1, 5 * (i % 2))]
        pa += [(i, 0.2 if i % 2 else 12), (i + 1, 0.2 if i % 2 else 12)]
    s.daten(m, pe, farbe=GRAU, dicke=3)
    s.daten(m, pa, farbe=BLAU, dicke=4)

    r = s.achsen((0, 50, 20), (0, 120, 40), breite=b + 0.05, hoehe=h, mitte=(2.3, 0), xl=v_achse(s, "U_{CE}", "uce_v"), yl=i_ma(s))
    s.flaeche(r, "min(100,400/x)", 0.5, 40, farbe=BLAU, deckung=0.18)
    s.kurve(r, "min(100,400/x)", x=(0.5, 40), farbe=BLAU, dicke=4)
    s.linie(r, (40, 0), (40, 10), farbe=BLAU, dicke=4)
    s.punkt(r, 6, 2, r=0.06)
    s.text(r, "A", (6.5, 12), groesse=22)
    s.text(r, "I_{C,max}", (10, 106), groesse=22, ausrichtung="left", farbe=BLAU)
    s.text(r, "U_{CE,max}", (47, 26), groesse=22, ausrichtung="center", farbe=BLAU)
    s.text(r, "P_{max}", (16, 42), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k10gegenkopplung():
    s = Szene("et1/k10gegenkopplung")
    w = s.welt()
    yt, yg = 1.3, -1.3
    # Stromgegenkopplung
    xt = -2.6
    B, C, E = tr_npn(s, xt, 0, g=0.5)
    xr = B[0] - 0.05
    s.draht((xr, yt), (C[0], yt))
    wid(s, (C[0], yt), (C[0], C[1] + 0.02), size=0.36)
    s.draht((C[0], C[1] + 0.03), C)
    wid(s, (E[0], E[1] - 0.02), (E[0], yg), size=0.36)
    s.draht((E[0], E[1] - 0.03), E)
    wid(s, (xr, yt), (xr, B[1] + 0.02), size=0.36)
    wid(s, (xr, B[1] - 0.02), (xr, yg), size=0.36)
    s.draht((xr, B[1] + 0.02), (xr, B[1] - 0.02))
    s.draht((xr, B[1]), B)
    kn(s, xr, B[1])
    s.draht((xr, yg), (E[0], yg))
    masse(s, 0.5 * (xr + E[0]), yg)
    t(s, "U_{CC}", (0.5 * (xr + C[0]), yt + 0.2), g=22)
    kn(s, 0.5 * (xr + C[0]), yt)
    t(s, "R_1", (xr - 0.2, 0.65), "right", g=22)
    t(s, "R_2", (xr - 0.2, -0.65), "right", g=22)
    t(s, "R_C", (C[0] + 0.2, 0.9), "left", g=22)
    t(s, "R_E", (E[0] + 0.2, -0.9), "left", ROT, g=22)
    # Spannungsgegenkopplung
    xt = -0.3
    B, C, E = tr_npn(s, xt, -0.2, g=0.5)
    xc = C[0]
    xl = B[0] - 0.05
    wid(s, (xc, yt), (xc, 0.65), size=0.36)
    s.draht((xc, 0.65), C)
    kn(s, xc, 0.55)
    s.draht((xc, 0.55), (xl, 0.55), (xl, 0.2))
    wid(s, (xl, 0.2), (xl, B[1] - 0.0), size=0.3)
    s.draht((xl, B[1]), B)
    s.draht(E, (E[0], yg))
    masse(s, E[0], yg)
    kn(s, xc, yt)
    t(s, "U_{CC}", (xc, yt + 0.2), g=22)
    t(s, "R_C", (xc + 0.2, 0.95), "left", g=22)
    t(s, "R_B", (xl - 0.2, 0.05), "right", ROT, g=22)
    # I_C(B)
    a = s.achsen((0, 800, 200), (0, 5, 1), breite=2.2, hoehe=2.1, mitte=(2.15, 0.05), gitter=True, xl="B", yl=i_ma(s))
    s.kurve(a, "min(0.01*x,11.8/3)", x=(50, 800), farbe=GRAU, dicke=4)
    s.kurve(a, "11.4/(3*(1+1/x)+540/x)", x=(50, 800), farbe=ORANGE, dicke=4)
    s.kurve(a, "2.1/(1+1/x+6.975/x)", x=(50, 800), farbe=BLAU, dicke=4)
    s.text(a, s.tr("ohne", "ohne", "without", "sin", "无"), (610, 4.25), groesse=22, ausrichtung="left", farbe=GRAU)
    s.text(a, "R_B", (640, 2.45), groesse=22, ausrichtung="left", farbe=ORANGE)
    s.text(a, "R_E", (640, 1.5), groesse=22, ausrichtung="left", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k10spiegel():
    s = Szene("et1/k10spiegel")
    w = s.welt()
    yt, yg = 1.3, -1.1
    g = 0.5
    ym = -0.4
    x1, x2 = -2.85, -1.45
    # T1 gespiegelt: Drehung 180 mit flip tauscht links und rechts
    s._add("Device", {"kind": "npn", "center": [x1, ym, 0], "rotation": 180, "flip": True, "label": "", "pins": False, "size": g, "color": SCHWARZ, "stroke_width": 3})
    B1, C1, E1 = (x1 + g, ym), (x1 - 0.5 * g, ym + g), (x1 - 0.5 * g, ym - g)
    B2, C2, E2 = tr_npn(s, x2, ym, g=g)
    xm = 0.5 * (B1[0] + B2[0])
    s.draht(B1, B2)
    kn(s, xm, ym)
    yk = ym + 0.75
    s.draht((xm, ym), (xm, yk), (C1[0], yk))
    kn(s, C1[0], yk)
    wid(s, (C1[0], yt), (C1[0], yk), size=0.36)
    s.draht((C1[0], yk), C1)
    wid(s, (C2[0], yt), (C2[0], yk), size=0.36)
    s.draht((C2[0], yk), C2)
    s.draht(E1, (E1[0], yg))
    s.draht(E2, (E2[0], yg))
    masse(s, E1[0], yg)
    masse(s, E2[0], yg)
    kl(s, C1[0], yt, "U_{CC}", dy=0.2)
    kl(s, C2[0], yt, "U_{CC}", dy=0.2)
    t(s, "R_{ref}", (C1[0] + 0.2, 0.8), "left", g=22)
    t(s, "R_L", (C2[0] + 0.2, 0.8), "left", g=22)
    t(s, "T1", (x1 + 0.12, ym - 0.42), "left", g=22)
    t(s, "T2", (x2 - 0.12, ym - 0.42), "right", g=22)
    ipfeil(s, (C1[0], yt - 0.07), (C1[0], yt - 0.29), "", None)
    t(s, "I_{ref}", (C1[0] - 0.09, yt - 0.2), "right", ROT, g=22)
    ipfeil(s, (C1[0], yk - 0.02), (C1[0], yk - 0.22), "", None)
    t(s, "I_{C1}", (C1[0] - 0.08, yk - 0.3), "right", ROT, g=22)
    ipfeil(s, (C2[0], yk - 0.02), (C2[0], yk - 0.22), "", None)
    t(s, "I_{C2}", (C2[0] + 0.08, yk - 0.2), "left", ROT, g=22)
    # Regler
    xa, xr = -0.3, 1.65
    yo, yu = 0.85, -1.1
    kl(s, xa, yo)
    kl(s, xa, yu)
    s.draht((xa + 0.06, yu), (xr - 0.06, yu))
    kl(s, xr, yo)
    kl(s, xr, yu)
    xz = 0.2
    s.draht((xa + 0.06, yo), (xz, yo))
    kn(s, xz, yo)
    wid(s, (xz, yo), (xz, 0.0), size=0.33)
    kn(s, xz, -0.07)
    s.draht((xz, 0.0), (xz, -0.3))
    bau(s, "zener", (xz, yu), (xz, -0.3), size=0.5)
    kn(s, xz, yu)
    xt = 0.9
    s._add("Device", {"kind": "npn", "center": [xt, yo - 0.21, 0], "rotation": 90, "flip": False, "label": "", "pins": False, "size": 0.42, "color": SCHWARZ, "stroke_width": 3})
    s.draht((xz, yo), (xt - 0.42, yo))
    s.draht((xt + 0.42, yo), (xr - 0.06, yo))
    s.draht((xz, -0.07), (xt, -0.07), (xt, yo - 0.63))
    t(s, "R_1", (xz - 0.17, 0.42), "right", g=22)
    spfeil(s, (xa, yo - 0.15), (xa, yu + 0.15), "U_E", (xa + 0.06, -0.55))
    spfeil(s, (xr, yo - 0.15), (xr, yu + 0.15), "U_A", (xr - 0.06, -0.25), ausr="right")
    t(s, "U_Z", (xz + 0.25, -0.75), "left", BLAU, g=22)
    # Verlauf
    a = s.achsen((0, 4, 1), (0, 15, 5), breite=1.15, hoehe=1.9, mitte=(3.0, 0.0), xl="t", yl=v_achse(s, "U", "u_v"), xzahlen=False, xmarks=False)
    pts = []
    n = 240
    for i in range(n + 1):
        x = 4 * i / n
        f = (x % 1)
        y = 13.5 - 3.0 * f / 0.8 if f < 0.8 else 10.5 + 3.0 * (f - 0.8) / 0.2
        pts.append((x, y))
    s.daten(a, pts, farbe=GRAU, dicke=3)
    s.linie(a, (0, 5.6), (4, 5.6), farbe=BLAU, dicke=4)
    s.text(a, "U_E", (2.0, 8.6), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(a, "U_A", (2.0, 3.2), groesse=22, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k10tangente():
    s = Szene("et1/k10tangente")
    a = s.achsen((0.56, 0.64, 0.02), (0, 6, 2), breite=2.45, hoehe=2.2, mitte=(-2.0, 0), gitter=True, xl=v_achse(s, "U_{BE}", "ube_v"), yl=i_ma(s))
    s.kurve(a, "1.9e-10*exp(x/0.026)", x=(0.56, 0.6285), farbe=BLAU)
    s.kurve(a, "2+76.92*(x-0.6)", x=(0.574, 0.6264), farbe=ROT, dicke=3.5, dash=DASH)
    s.punkt(a, 0.6, 2.0, r=0.07)
    s.text(a, "A", (0.5965, 2.45), groesse=24)
    s.text(a, "S", (0.6185, 3.2), groesse=24, farbe=ROT, ausrichtung="left")
    r = s.achsen((-80, 16, 20), (0, 5, 1), breite=3.0, hoehe=2.2, mitte=(1.75, 0), gitter=True, xl=v_achse(s, "U_{CE}", "uce_v"), yl=i_ma(s))
    for k, f in ((2, BLAU), (4, BLAU)):
        s.kurve(r, "%d*(1-exp(-x/0.026))*(1+(x-6)/80)" % k, x=(0.001, 16), farbe=f, dicke=4)
        s.kurve(r, "%d*(1+(x-6)/80)" % k, x=(-74, 0.02), farbe=GRAU, dicke=2.5, dash=DASH)
    s.punkt(r, 6, 2, r=0.07)
    s.pfeil((6, 2.1), (6, 3.75), "", on=r, farbe=ROT, spitze=0.14, dicke=3)
    s.text(r, "18 mV", (-2, 3.0), groesse=22, ausrichtung="right", farbe=ROT)
    s.text(r, "−74 V", (-66, 0.85), groesse=22, ausrichtung="center", farbe=GRAU)
    s.text(r, "0.600 V", (15, 1.55), groesse=22, ausrichtung="right", farbe=BLAU)
    s.text(r, "0.618 V", (15, 4.55), groesse=22, ausrichtung="right", farbe=BLAU)
    s.speichern()


def k10kleinsignal():
    s = Szene("et1/k10kleinsignal")
    yo, yu = 0.8, -0.95
    # erweitert
    xb = -3.35
    xq = -2.55
    xi, xr = -1.7, -0.95
    kl(s, xb, yo, "B", dy=0.22)
    kl(s, xb, yu, "E", dy=-0.24)
    s.draht((xb + 0.06, yo), (xq, yo), (xq, 0.55))
    bau(s, "vsource", (xq, 0.55), (xq, -0.1), size=0.44)
    wid(s, (xq, -0.1), (xq, yu + 0.02), size=0.3)
    t(s, "U_0", (xq - 0.25, 0.22), "right", BLAU, g=22)
    t(s, "+", (xq + 0.22, 0.47), farbe=ROT, g=22)
    t(s, "r_{BE}", (xq - 0.22, -0.52), "right", g=22)
    s.draht((xb + 0.06, yu), (xr + 0.32, yu))
    kl(s, xr + 0.38, yu, "E", dy=-0.24)
    bau(s, "cccs", (xi, 0.35), (xi, -0.55), size=0.46)
    s.draht((xi, yo), (xi, 0.35))
    s.draht((xi, -0.55), (xi, yu))
    s.pfeil((xi, 0.6), (xi, 0.38), "", farbe=ROT, spitze=0.13, dicke=3)
    wid(s, (xr, yo), (xr, yu), size=0.3)
    s.draht((xi, yo), (xr + 0.32, yo))
    kl(s, xr + 0.38, yo, "C", dy=0.22)
    kn(s, xi, yu)
    kn(s, xr, yu)
    kn(s, xr, yo)
    kn(s, xq, yu)
    t(s, "I", (xi + 0.26, -0.1), "left", ROT, g=22)
    t(s, "r_{CE}", (xr + 0.17, -0.1), "left", g=22)
    s.pfeil((xb + 0.2, yo), (xb + 0.5, yo), "", farbe=ROT, spitze=0.13, dicke=3)
    t(s, "I_B", (xb + 0.42, yo + 0.2), g=22, farbe=ROT)
    # Pfeil
    s.pfeil((-0.35, -0.1), (0.0, -0.1), "", farbe=GRAU, spitze=0.22, dicke=4.5)
    # Kleinsignal
    xb = 0.25
    xq = 1.15
    xi, xr = 2.2, 2.9
    kl(s, xb, yo, "B", dy=0.22)
    kl(s, xb, yu, "E", dy=-0.24)
    s.draht((xb + 0.06, yo), (xq, yo))
    wid(s, (xq, yo), (xq, yu), size=0.3)
    s.draht((xb + 0.06, yu), (xr + 0.3, yu))
    kl(s, xr + 0.36, yu, "E", dy=-0.24)
    bau(s, "vccs", (xi, 0.35), (xi, -0.55), size=0.46)
    s.draht((xi, yo), (xi, 0.35))
    s.draht((xi, -0.55), (xi, yu))
    s.pfeil((xi, 0.6), (xi, 0.38), "", farbe=ROT, spitze=0.13, dicke=3)
    wid(s, (xr, yo), (xr, yu), size=0.3)
    s.draht((xi, yo), (xr + 0.3, yo))
    kl(s, xr + 0.36, yo, "C", dy=0.22)
    kn(s, xq, yu)
    kn(s, xi, yu)
    kn(s, xr, yu)
    kn(s, xr, yo)
    t(s, "r_{BE}", (xq + 0.18, 0.28), "left", g=22)
    t(s, "S u_{be}", (xi - 0.28, -0.25), "right", ROT, g=22)
    t(s, "r_{CE}", (xr + 0.17, -0.1), "left", g=22)
    spfeil(s, (xb + 0.16, yo - 0.12), (xb + 0.16, yu + 0.12), "u_{be}", (xb + 0.2, -0.05))
    s.pfeil((xb + 0.2, yo), (xb + 0.5, yo), "", farbe=ROT, spitze=0.13, dicke=3)
    t(s, "i_b", (xb + 0.42, yo + 0.2), g=22, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def loese(f, a, b, n=80):
    fa = f(a)
    for _ in range(n):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fa > 0) == (fm > 0):
            a, fa = m, fm
        else:
            b = m
    return 0.5 * (a + b)


def kurve_emitter(rc=3e3, ucc=12.0):
    pts = []
    for i in range(121):
        ue = 0.5 + 0.16 * i / 120
        pts.append((ue, loese(lambda u: ucc - rc * ic(ue, u) - u, 0.0, ucc + 1)))
    return pts


def kurve_folger(re=3e3, ucc=12.0):
    pts = []
    for i in range(121):
        ue = 12.0 * i / 120

        def f(u):
            ub = ue - u
            uc = ucc - u
            return (1 + 1 / BB) * re * IS * exp(ub / UT) * (1 + (uc - 6) / 80) - u
        pts.append((ue, loese(f, 0.0, max(ue, 1e-6))))
    return pts


def kurve_basis(rc=3e3, ucc=12.0):
    pts = []
    for i in range(121):
        ue = -0.66 + 0.16 * i / 120
        ub = -ue
        pts.append((ue, loese(lambda u: ucc - rc * ic(ub, u - ue) - u, ue, ucc + 1)))
    return pts


def k10grundschaltungen():
    s = Szene("et1/k10grundschaltungen")
    w = s.welt()
    y0 = 1.0
    xs = (-2.45, -0.05, 2.35)
    titel = (s.tr("t_em", "Emitterschaltung", "common emitter", "emisor común", "共发射极"),
             s.tr("t_ko", "Kollektorschaltung", "common collector", "colector común", "共集电极"),
             s.tr("t_ba", "Basisschaltung", "common base", "base común", "共基极"))
    for x, tt in zip(xs, titel):
        t(s, tt, (x + 0.1, y0 + 1.35), g=24)
    yt = y0 + 1.0
    # Emitterschaltung
    x = xs[0]
    B, C, E = tr_npn(s, x, y0 - 0.1, g=0.45)
    wid(s, (C[0], yt), (C[0], C[1] + 0.03), size=0.3)
    s.draht((C[0], C[1] + 0.03), C)
    kn(s, C[0], C[1] + 0.02)
    s.draht((C[0], C[1] + 0.02), (C[0] + 0.5, C[1] + 0.02))
    kl(s, C[0] + 0.56, C[1] + 0.02, uaus(s), dx=0.08, dy=0.2)
    s.draht(E, (E[0], y0 - 0.85))
    masse(s, E[0], y0 - 0.85, g=0.45)
    s.draht(B, (B[0] - 0.3, B[1]))
    kl(s, B[0] - 0.36, B[1], uein(s), dx=-0.02, dy=0.2)
    t(s, "U_{CC}", (C[0] + 0.15, yt + 0.1), "left", g=22)
    t(s, "R_C", (C[0] - 0.17, yt - 0.27), "right", g=22)
    # Kollektorschaltung
    x = xs[1]
    B, C, E = tr_npn(s, x, y0 + 0.05, g=0.45)
    s.draht(C, (C[0], yt))
    t(s, "U_{CC}", (C[0] + 0.15, yt + 0.1), "left", g=22)
    wid(s, (E[0], E[1] - 0.02), (E[0], y0 - 0.85), size=0.3)
    s.draht((E[0], E[1]), (E[0], E[1] - 0.02))
    kn(s, E[0], E[1] - 0.01)
    s.draht((E[0], E[1] - 0.01), (E[0] + 0.5, E[1] - 0.01))
    kl(s, E[0] + 0.56, E[1] - 0.01, uaus(s), dx=0.08, dy=0.2)
    masse(s, E[0], y0 - 0.85, g=0.45)
    s.draht(B, (B[0] - 0.3, B[1]))
    kl(s, B[0] - 0.36, B[1], uein(s), dx=-0.02, dy=0.2)
    t(s, "R_E", (E[0] - 0.17, y0 - 0.65), "right", g=22)
    # Basisschaltung
    x = xs[2]
    B, C, E = tr_npn(s, x, y0 - 0.1, g=0.45)
    wid(s, (C[0], yt), (C[0], C[1] + 0.03), size=0.3)
    s.draht((C[0], C[1] + 0.03), C)
    kn(s, C[0], C[1] + 0.02)
    s.draht((C[0], C[1] + 0.02), (C[0] + 0.5, C[1] + 0.02))
    kl(s, C[0] + 0.56, C[1] + 0.02, uaus(s), dx=0.08, dy=0.2)
    s.draht(B, (B[0] - 0.1, B[1]), (B[0] - 0.1, y0 - 0.75))
    masse(s, B[0] - 0.1, y0 - 0.75, g=0.45)
    s.draht(E, (E[0], y0 - 0.85))
    kl(s, E[0], y0 - 0.91, uein(s), dx=0.25, dy=0.0)
    t(s, "U_{CC}", (C[0] + 0.15, yt + 0.1), "left", g=22)
    t(s, "R_C", (C[0] - 0.17, yt - 0.27), "right", g=22)
    # Kennlinien
    b, h = 1.5, 1.2
    yk = -1.75
    ue, ua = uein_v(s), uaus_v(s)
    a = s.achsen((0.5, 0.66, 0.05), (0, 12, 4), breite=b, hoehe=h, mitte=(xs[0] + 0.15, yk), gitter=True, xl=ue, yl=ua)
    s.daten(a, duenn(kurve_emitter(), 2e-4), farbe=BLAU)
    s.punkt(a, 0.6, 6.0, r=0.06)
    m = s.achsen((0, 12, 4), (0, 12, 4), breite=b, hoehe=h, mitte=(xs[1] + 0.15, yk), gitter=True, xl=ue, yl=ua)
    s.kurve(m, "x", x=(0, 12), farbe=GRAU, dicke=2.5, dash=DASH)
    s.daten(m, duenn(kurve_folger(), 2e-4), farbe=BLAU)
    r = s.achsen((-0.66, -0.5, 0.05), (-2, 12), breite=b, hoehe=h, mitte=(xs[2] + 0.15, yk), gitter=True, xl=ue, yl=ua, yticks="0;4;8;12")
    s.daten(r, duenn(kurve_basis(), 2e-4), farbe=BLAU)
    s.punkt(r, -0.6, 6.0, r=0.06)
    s.speichern()


if __name__ == "__main__":
    for f in (k10aufbau, k10basis, k10flaeche, k10schnitte, k10esb, k10arbeit, k10schalter, k10gegenkopplung, k10spiegel, k10tangente, k10kleinsignal,
              k10grundschaltungen):
        f()
