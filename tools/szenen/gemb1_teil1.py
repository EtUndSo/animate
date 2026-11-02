"""GEMB 1 Teil 1 (kap1_stufen.tex): Welle, Teilchen und Schrödinger-Gleichung.

Aufruf: python tools/szenen/gemb1_teil1.py, danach python tools/szenen_ansehen.py out.png gemb1/k1drude ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap1.py.
"""
import random
import sys
from math import cos, exp, pi, sin, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLBLAU = "#8fb4e3"
ALPHA = 0.0381      # hbar^2/(2 m0) in eV nm^2
K0 = 5.123          # 1/nm bei E_kin = 1 eV
HBAR_M = 0.11577    # hbar/m0 in nm^2/fs


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


# ------------------------------------------------------------------------------------------ Stufe 1
def pfad(mx, breite, hoch, drift):
    """Zufallsweg mit 11 Stößen, der im Rahmen bleibt; mit Drift läuft er nach links, ohne Drift bleibt er nahe am Start."""
    for seed in range(1, 200000):
        rnd = random.Random(seed)
        x, y = (mx + 1.2, 0.05) if drift else (mx + 0.1, 0.05)
        pts = [(x, y)]
        for _ in range(11):
            a, l = rnd.uniform(0, 2 * pi), rnd.uniform(0.5, 0.85)
            x, y = x + l * cos(a) + drift, y + l * sin(a)
            if abs(x - mx) > breite / 2 - 0.12 or abs(y) > hoch / 2 - 0.12:
                break
            pts.append((x, y))
        else:
            netto = pts[-1][0] - pts[0][0]
            if (drift and -2.6 < netto < -2.0) or (not drift and abs(netto) < 0.5 and abs(pts[-1][1] - pts[0][1]) > 0.3):
                return pts
    raise ValueError("kein Weg gefunden")


def k1drude():
    """Zickzackweg eines Elektrons zwischen den Atomrümpfen, ohne und mit Feld."""
    s = Szene("gemb1/k1drude")
    s.welt()
    breite, hoch = 3.3, 2.25
    for mx, titel, drift in ((-1.8, s.tr("ohne", "ohne Feld", "without field", "sin campo", "无电场"), 0.0),
                             (1.8, s.tr("mit", "mit Feld", "with field", "con campo", "有电场"), -0.22)):
        x0, y0 = mx - breite / 2, -hoch / 2
        s.box("", (mx, 0), breite=breite, hoehe=hoch, farbe="#6a6a6a", fuellung="#ffffff", deckung=0.0, dicke=2)
        for i in range(6):
            for j in range(4):
                s.kreis(None, x0 + 0.3 + i * 0.54, y0 + 0.3 + j * 0.55, 0.075, farbe="#9a9a9a", dicke=1.5, fuellung="#c4c4c4", deckung=1.0)
        t(s, titel, (mx, hoch / 2 + 0.28))
        pts = pfad(mx, breite, hoch, drift)
        start = pts[0]
        for a, b in zip(pts[:-1], pts[1:-1]):
            s.linie(None, a, b, farbe=BLAU, dicke=2.5)
        s.punkt(None, start[0], start[1], farbe=BLAU, r=0.085)
        s.pfeil(pts[-2], pts[-1], "", farbe=BLAU, spitze=0.17, dicke=2.5)
        if drift:
            s.pfeil((start[0], -hoch / 2 - 0.3), (pts[-1][0], -hoch / 2 - 0.3), "", farbe=ROT, spitze=0.2, dicke=4)
            t(s, "v_d", (pts[-1][0] - 0.3, -hoch / 2 - 0.33), farbe=ROT)
    s.pfeil((-2.4, -1.43), (-1.2, -1.43), "", farbe=SCHWARZ, spitze=0.2, dicke=3)
    t(s, "ℰ", (-1.0, -1.45), g=32)
    t(s, s.tr("mit2", "Feld", "field", "campo", "电场"), (-2.8, -1.43), g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def verteilung(y):
    """Trefferdichte hinter dem Doppelspalt: Streifen mal Einhüllende."""
    return cos(pi * y / 0.62) ** 2 * exp(-(y / 1.05) ** 2)


def kugeln(y):
    return exp(-((y - 0.62) / 0.34) ** 2) + exp(-((y + 0.62) / 0.34) ** 2)


def k1doppelspalt():
    """Oben der Aufbau für Kugeln und für Elektronen, unten das Trefferbild für wachsende Elektronenzahl."""
    s = Szene("gemb1/k1doppelspalt")
    s.welt()
    ywand, yschirm = -0.55, 0.75
    hb = 1.6
    for mx, titel in ((-1.78, s.tr("kug", "Kugeln", "small balls", "bolitas", "小球")), (1.78, s.tr("ele", "Elektronen", "electrons", "electrones", "电子"))):
        t(s, titel, (mx, 2.12))
        for a, b in (((mx - hb, ywand), (mx - 0.44, ywand)), ((mx - 0.28, ywand), (mx + 0.28, ywand)), ((mx + 0.44, ywand), (mx + hb, ywand))):
            s.linie(None, a, b, farbe=SCHWARZ, dicke=7)
        s.linie(None, (mx - hb, yschirm), (mx + hb, yschirm), farbe=SCHWARZ, dicke=4)
        s.pfeil((mx, ywand - 0.6), (mx, ywand - 0.15), "", farbe=GRAU, spitze=0.18, dicke=3)
        t(s, s.tr("schirm", "Schirm", "screen", "pantalla", "屏"), (mx + hb - 0.4, yschirm - 0.22), g=22)
    t(s, s.tr("wand", "Wand mit zwei Spalten", "wall with two slits", "pared con dos rendijas", "双缝挡板"), (0, -0.85), g=22)
    mx = -1.78
    for sp in (-0.36, 0.36):
        for ds in (-0.25, 0.25):
            s.linie(None, (mx + sp, ywand), (mx + sp + (sp + ds) * 0.75, yschirm), farbe=HELLBLAU, dicke=2, dash=DASH)
    pts = [(mx + y, yschirm + 1.05 * kugeln(y)) for y in np.linspace(-hb, hb, 121)]
    s.daten(None, pts, farbe=ROT, dicke=4)
    mx = 1.78
    for sp in (-0.36, 0.36):
        for r in (0.25, 0.5, 0.75, 1.0, 1.25):
            pk = []
            for a in np.linspace(0.02, pi - 0.02, 61):
                x, y = mx + sp + r * cos(a), ywand + r * sin(a)
                if abs(x - mx) <= hb and y <= yschirm - 0.04:
                    pk.append((float(x), float(y)))
            if len(pk) > 2:
                s.daten(None, pk, farbe=HELLBLAU, dicke=2)
    pts = [(mx + y, yschirm + 1.05 * verteilung(y)) for y in np.linspace(-hb, hb, 241)]
    s.daten(None, pts, farbe=ROT, dicke=4)
    rnd = random.Random(7)
    breite, hoehe, y0 = 2.2, 0.62, -1.85
    zeilen = (("n30", 30, "30 Elektronen", "30 electrons", "30 electrones", "30 个电子"),
              ("n300", 300, "300 Elektronen", "300 electrons", "300 electrones", "300 个电子"),
              ("n3000", 3000, "3000 Elektronen", "3000 electrons", "3000 electrones", "3000 个电子"))
    for i, (key, n, de, en, es, zh) in enumerate(zeilen):
        mx = -2.38 + i * 2.38
        s.box("", (mx, y0), breite=breite, hoehe=hoehe, farbe="#6a6a6a", fuellung="#ffffff", deckung=0.0, dicke=2)
        pk = []
        while len(pk) < n:
            y, u = rnd.uniform(-1.08, 1.08), rnd.random()
            if u < verteilung(y):
                pk.append((mx + y, y0 + rnd.uniform(-0.29, 0.29)))
        r = 0.022 if n < 1000 else 0.012
        s.daten(None, pk, farbe=BLAU, dicke=0, marker=True, marker_r=r)
        t(s, s.tr(key, de, en, es, zh), (mx, y0 - 0.53), g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k1zeiger():
    """Die Zeiger aus beiden Spalten addieren sich; erst die Summe wird quadriert."""
    s = Szene("gemb1/k1zeiger")
    s.welt()
    a = s.achsen((-1, 1, 0.5), (0, 4, 2), breite=6.0, hoehe=1.55, mitte=(0.25, 1.0),
                 xl="y/y_S", yl="|Ψ|²/|Ψ₁|²", xticks="", zahl=ZAHL, xl_mitte=False)
    s.kurve(a, "4*cos(pi*x)^2", farbe=ROT, dicke=5)
    s.kurve(a, "2", farbe=GRAU, dicke=3, dash=DASH)
    s.text(a, "|Ψ₁+Ψ₂|²", (0.45, 3.5), groesse=GR, farbe=ROT, ausrichtung="center")
    s.text(a, "|Ψ₁|²+|Ψ₂|²", (0.5, 2.4), groesse=GR, farbe=GRAU, ausrichtung="center")
    for x_, y_, n, dx, dy in ((0, 4, "A", 0.15, -0.1), (0.25, 2, "B", -0.07, -0.3), (0.5, 0, "C", 0.07, 0.42)):
        s.punkt(a, x_, y_, farbe=ROT, r=0.09)
        s.text(a, n, (x_ + dx, y_ + dy), groesse=GR, ausrichtung="center")
    L, y = 0.5, -0.85
    for x, phi, name, txt in ((-2.75, 0.0, "A", "δ = 0"), (-0.05, pi / 2, "B", "δ = π/2"), (2.2, pi, "C", "δ = π")):
        m = (x, y)
        p1 = (m[0] + L * cos(phi / 2), m[1] + L * sin(phi / 2))
        p2 = (p1[0] + L * cos(-phi / 2), p1[1] + L * sin(-phi / 2))
        if phi == 0:
            s.pfeil((m[0], y - 0.13), (p2[0], y - 0.13), "", farbe=ROT, spitze=0.17, dicke=4)
            s.pfeil(m, p1, "", farbe=BLAU, spitze=0.16, dicke=3)
            s.pfeil(p1, p2, "", farbe=GRUEN, spitze=0.16, dicke=3)
        elif phi == pi:
            s.pfeil((m[0] - 0.06, y), (m[0] - 0.06, y + L), "", farbe=BLAU, spitze=0.16, dicke=3)
            s.pfeil((m[0] + 0.06, y + L), (m[0] + 0.06, y), "", farbe=GRUEN, spitze=0.16, dicke=3)
            s.punkt(None, m[0], y - 0.12, farbe=ROT, r=0.07)
        else:
            s.pfeil(m, p2, "", farbe=ROT, spitze=0.17, dicke=4)
            s.pfeil(m, p1, "", farbe=BLAU, spitze=0.16, dicke=3)
            s.pfeil(p1, p2, "", farbe=GRUEN, spitze=0.16, dicke=3)
        t(s, name, (x - 0.32, y + 0.42))
        t(s, txt, (x + 0.55, y - 0.4))
    y2 = -1.72
    t(s, "Ψ₁", (-0.75, y2), farbe=BLAU)
    t(s, "Ψ₂", (-0.05, y2), farbe=GRUEN)
    t(s, s.tr("sum", "Summe", "sum", "suma", "和"), (0.95, y2), farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k1stationaer():
    """Der Zeiger dreht sich, der Realteil schwingt, das Betragsquadrat steht."""
    s = Szene("gemb1/k1stationaer")
    s.welt()
    c = (-2.35, -0.1)
    R = 0.8
    s.kreis(None, c[0], c[1], R, farbe=GRAU, dicke=2, dash=DASH)
    s.pfeil((c[0] - 1.0, c[1]), (c[0] + 1.1, c[1]), "", farbe=SCHWARZ, spitze=0.15, dicke=2)
    s.pfeil((c[0], c[1] - 1.0), (c[0], c[1] + 1.05), "", farbe=SCHWARZ, spitze=0.15, dicke=2)
    t(s, "Re", (c[0] + 1.0, c[1] - 0.25), g=22)
    t(s, "Im", (c[0] + 0.28, c[1] + 1.0), g=22)
    farben = ((0.0, BLAU), (pi / 3, GRUEN), (2 * pi / 3, ORANGE))
    for wt, f in farben:
        s.pfeil(c, (c[0] + R * cos(wt), c[1] - R * sin(wt)), "", farbe=f, spitze=0.17, dicke=3.5)
    t(s, s.tr("ort", "an festem Ort", "at a fixed position", "en un punto fijo", "固定位置处"), (c[0], c[1] + 1.4), g=22)
    a = s.achsen((0, 2, 0.5), (-1, 1, 1), breite=3.4, hoehe=1.05, mitte=(1.45, 0.72), xl="", yl="Re Ψ", xzahlen=False)
    for wt, f in farben:
        s.kurve(a, "sin(2*pi*x)*cos(%.6f)" % wt, farbe=f, dicke=4)
    b = s.achsen((0, 2, 0.5), (0, 1, 1), breite=3.4, hoehe=0.8, mitte=(1.45, -0.8), xl="x/λ", yl="|Ψ|²")
    s.kurve(b, "sin(2*pi*x)^2", farbe=ROT, dicke=5)
    t(s, "ωt = 0", (0.75, 1.5), farbe=BLAU, g=22)
    t(s, "π/3", (1.75, 1.5), farbe=GRUEN, g=22)
    t(s, "2π/3", (2.55, 1.5), farbe=ORANGE, g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k_achse(s):
    return s.tr("k_achse", "k in 1/nm", "k in 1/nm", "k en 1/nm", "k / nm⁻¹")


def e_achse(s):
    return s.tr("e_achse", "E in eV", "E in eV", "E en eV", "E / eV")


def k1parabel():
    """Dispersionsrelation mit den Wellen zu vier Punkten, reale Zahlen: V0 = 1 eV, Masse m0."""
    s = Szene("gemb1/k1parabel")
    s.welt()
    V0, ymax = 1.0, 3.5
    xk0, bk, ho, ym = -1.85, 3.05, 2.65, 0.0
    a = s.achsen((-8, 8, 4), (0, ymax, 1), breite=bk, hoehe=ho, mitte=(xk0, ym), xl=k_achse(s), yl=e_achse(s))
    s.kurve(a, "%g*x^2+%g" % (ALPHA, V0), x=(-7.7, 7.7), farbe=GRUEN, dicke=5)
    s.linie(a, (-8, V0), (8, V0), farbe=GRAU, dicke=2, dash=DASH)
    s.text(a, "V₀", (-6.6, 1.2), groesse=GR, ausrichtung="center", farbe=GRAU)

    def wx(k):
        return xk0 + k / 16 * bk

    def wy(e):
        return ym + (e / ymax - 0.5) * ho
    xw0, xw1 = 0.9, 3.22
    b = s.achsen((0, 6, 2), (0, ymax, 1), breite=xw1 - xw0, hoehe=ho, mitte=(0.5 * (xw0 + xw1), ym),
                 xl=s.tr("x_achse", "x in nm", "x in nm", "x en nm", "x / nm"), yl="", yzahlen=False)
    for k_, f in ((1.5, ROT), (3.0, ORANGE), (5.123, GRUEN), (7.0, BLAU)):
        e_ = ALPHA * k_ ** 2 + V0
        s.punkt(a, k_, e_, farbe=f, r=0.08)
        s.linie(None, (wx(k_), wy(e_)), (xw0, wy(e_)), farbe=f, dicke=2, dash=DASH)
        s.kurve(b, "%g+0.14*cos(%g*x)" % (e_, k_), farbe=f, dicke=3)
    k_ = 5.123
    e_ = ALPHA * k_ ** 2 + V0
    s.linie(a, (k_, 0), (k_, V0), farbe=ROT, dicke=4)
    s.linie(a, (k_, V0), (k_, e_), farbe=ORANGE, dicke=4)
    s.text(a, "E_{pot}", (6.2, 0.45), groesse=GR, farbe=ROT, ausrichtung="center")
    s.text(a, "E_{kin}", (6.4, 1.5), groesse=GR, farbe=ORANGE, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def paket(x, tt, w=2.0, k0=K0):
    """Exaktes Gauß-Paket (V0 = 0, Masse m0): komplexer Wert bei Zeit tt in fs; x in nm, Betrag 1 bei t = 0."""
    q = HBAR_M * tt / 2                     # hbar t / (2 m) in nm^2
    a2 = w ** 2 / 4 + 1j * q
    return (w / (2 * np.sqrt(a2))) * np.exp(1j * (k0 * x - HBAR_M * k0 ** 2 * tt / 2)) * np.exp(-(x - HBAR_M * k0 * tt) ** 2 / (4 * a2))


def k1paket():
    s = Szene("gemb1/k1paket")
    s.welt()
    breite, hoehe = 3.4, 0.72
    xl, xr = -1.65, 2.1
    y1, y2, y3 = 2.2, 0.8, -1.3
    x_nm = s.tr("x_achse", "x in nm", "x in nm", "x en nm", "x / nm")
    for y0, w, zeigen in ((y1, 2.0, False), (y2, 0.8, True)):
        a = s.achsen((-6, 6, 3), (-1, 1, 1), breite=breite, hoehe=hoehe, mitte=(xl, y0), xl=x_nm if zeigen else "", yl="Re ψ", xzahlen=zeigen, yzahlen=False)
        s.kurve(a, "exp(-(x/%g)^2)*cos(%g*x)" % (w, K0), farbe=BLAU, dicke=2.5)
        s.kurve(a, "exp(-(x/%g)^2)" % w, farbe=ROT, dicke=3)
        s.kurve(a, "-exp(-(x/%g)^2)" % w, farbe=ROT, dicke=3)
        s.text(a, "w = %s nm" % ("2" if w == 2 else "0.8"), (4.1, 0.65), groesse=22, ausrichtung="center")
        b = s.achsen((0, 10, 5), (0, 1, 1), breite=2.4, hoehe=hoehe, mitte=(xr, y0), xl=k_achse(s) if zeigen else "", yl="c(k)", xzahlen=zeigen, yzahlen=False)
        s.kurve(b, "exp(-(x-%g)^2*%g/4)" % (K0, w ** 2), farbe=GRUEN, dicke=4)
        s.linie(b, (K0, 0), (K0, 1), farbe=GRAU, dicke=2, dash=DASH)
    tt = 6.0
    v_g = HBAR_M * K0
    v_ph = v_g / 2
    xs = np.linspace(-5, 9.5, 1500)
    c = s.achsen((-5, 9.5, 5), (-1, 1.7, 1), breite=6.3, hoehe=1.55, mitte=(0.05, y3), xl=x_nm, yl="Re ψ", yzahlen=False, xticks="")
    z0, z1 = paket(xs, 0.0), paket(xs, tt)
    s.daten(c, [(float(a_), float(b_)) for a_, b_ in zip(xs, z0.real)], farbe=BLAU, dicke=2.5)
    s.daten(c, [(float(a_), float(b_)) for a_, b_ in zip(xs, z1.real)], farbe=GRUEN, dicke=2.5)
    i = int(np.argmin(np.abs(xs - v_ph * tt)))
    j = i - 40 + int(np.argmax(z1.real[i - 40:i + 40]))
    xc, yc = float(xs[j]), float(z1.real[j])
    s.punkt(c, 0.0, 1.0, farbe=ROT, r=0.07)
    s.punkt(c, xc, yc, farbe=ROT, r=0.07)
    xpk = v_g * tt
    s.linie(c, (0, 1.0), (0, 1.5), farbe=GRAU, dicke=1.5, dash=DASH)
    s.linie(c, (xc, yc), (xc, 1.18), farbe=GRAU, dicke=1.5, dash=DASH)
    s.linie(c, (xpk, 0.9), (xpk, 1.5), farbe=GRAU, dicke=1.5, dash=DASH)
    wx = lambda x_: 0.05 + (x_ - 2.25) / 14.5 * 6.3
    wy = lambda y_: y3 + (y_ - 0.35) / 2.7 * 1.55
    s.pfeil((wx(0), wy(1.18)), (wx(xc), wy(1.18)), "", farbe=ROT, spitze=0.14, dicke=3)
    s.pfeil((wx(0), wy(1.5)), (wx(xpk), wy(1.5)), "", farbe=SCHWARZ, spitze=0.14, dicke=3)
    s.text(c, "v_{ph}", (xc + 0.7, 1.13), groesse=22, farbe=ROT, ausrichtung="center")
    s.text(c, "v_g", (xpk + 0.6, 1.45), groesse=22, ausrichtung="center")
    s.text(c, "t = 0", (-3.4, 0.72), groesse=22, farbe=BLAU, ausrichtung="center")
    s.text(c, "t = 6 fs", (7.9, 0.72), groesse=22, farbe=GRUEN, ausrichtung="center")
    s.speichern()
    return v_g * tt, xc


# ------------------------------------------------------------------------------------------ Stufe 7
def k1kruemmung():
    s = Szene("gemb1/k1kruemmung")
    s.welt()
    a = s.achsen((-6, 6, 3), (0, 3, 1), breite=3.15, hoehe=2.0, mitte=(-1.75, 0), xl=k_achse(s), yl=e_achse(s))
    s.kurve(a, "%g*x^2" % ALPHA, x=(-6, 6), farbe=BLAU, dicke=5)
    s.kurve(a, "%g*x^2" % (ALPHA / 0.2), x=(-3.97, 3.97), farbe=ROT, dicke=5)
    k_ = 4.5
    e_ = ALPHA * k_ ** 2
    st = 2 * ALPHA * k_
    s.linie(a, (k_ - 1.4, e_ - 1.4 * st), (k_ + 1.4, e_ + 1.4 * st), farbe=GRAU, dicke=3, dash=DASH)
    s.punkt(a, k_, e_, farbe=BLAU, r=0.08)
    s.text(a, "m₀", (-5.1, 1.7), groesse=GR, farbe=BLAU, ausrichtung="center")
    s.text(a, "0.2 m₀", (-1.0, 2.75), groesse=GR, farbe=ROT, ausrichtung="center")
    b = s.achsen((-6, 6, 3), (-2, 2, 1), breite=2.8, hoehe=2.0, mitte=(1.85, 0), xl=k_achse(s),
                 yl=s.tr("v_achse", "v in 10⁶ m/s", "v in 10⁶ m/s", "v en 10⁶ m/s", "v / (10⁶ m/s)"))
    s.kurve(b, "0.11577*x", x=(-6, 6), farbe=BLAU, dicke=5)
    s.kurve(b, "0.11577*x/0.2", x=(-3.4, 3.4), farbe=ROT, dicke=5)
    s.punkt(b, k_, 0.11577 * k_, farbe=BLAU, r=0.08)
    s.text(b, "m₀", (4.8, 0.2), groesse=GR, farbe=BLAU, ausrichtung="center")
    s.text(b, "0.2 m₀", (-3.1, 1.5), groesse=GR, farbe=ROT, ausrichtung="center")
    s.speichern()


def k1feld():
    """Energie über dem Ort zwischen zwei Platten: Scheitel folgt V(x), die Gesamtenergie bleibt."""
    s = Szene("gemb1/k1feld")
    s.welt()
    x0, x1, y0, y1 = -3.0, 3.0, -1.3, 0.1
    for x, name in ((x0 - 0.08, "0 V"), (x1 + 0.08, "+1 V")):
        s.box("", (x, -0.05), breite=0.16, hoehe=3.1, farbe="#555555", fuellung="#9a9a9a", deckung=1.0, dicke=2)
        t(s, name, (x, 1.75))
    s.linie(None, (x0, y1), (x1, y0), farbe=BLAU, dicke=5)
    t(s, "V(x)", (-1.1, -0.85), farbe=BLAU)
    s.pfeil((x0 + 0.05, y1), (x1 - 0.05, y1), "", farbe=ROT, spitze=0.2, dicke=3.5)
    t(s, "E", (2.72, y1 + 0.24), farbe=ROT, g=26)
    c = 1.4 / 0.85 ** 2
    for xp in (-2.1, 0.0, 2.1):
        vs = y1 + (y0 - y1) * (xp - x0) / (x1 - x0)
        hoehe = y1 - vs
        qmax = 0.82
        pts = [(xp + q, vs + c * q * q) for q in np.linspace(-qmax, qmax, 61)]
        s.daten(None, pts, farbe=GRUEN, dicke=4)
        s.linie(None, (xp, vs - 0.15), (xp, vs + 1.25), farbe=GRAU, dicke=1.5)
        t(s, "k", (xp + qmax - 0.1, vs - 0.2), farbe=GRAU, g=22)
        s.linie(None, (xp - qmax, vs), (xp + qmax, vs), farbe=GRAU, dicke=1.5)
        qe = sqrt(hoehe / c)
        s.linie(None, (xp + qe, vs), (xp + qe, y1), farbe=ORANGE, dicke=3)
        s.punkt(None, xp + qe, y1, farbe=ROT, r=0.09)
        if xp > -2:
            t(s, "E_{kin}", (xp + qe + 0.42, 0.5 * (vs + y1)), farbe=ORANGE, g=22)
    s.punkt(None, x0 + 0.03, y1, farbe=ROT, r=0.09)
    t(s, "x = 0", (x0 + 0.15, -1.9), g=22)
    t(s, "x = d", (x1 - 0.15, -1.9), g=22)
    s.pfeil((0.7, -1.9), (-0.7, -1.9), "", farbe=SCHWARZ, spitze=0.2, dicke=3)
    t(s, "ℰ", (0.95, -1.92), g=32)
    s.speichern()


def alle():
    k1drude()
    k1doppelspalt()
    k1zeiger()
    k1stationaer()
    k1parabel()
    print("Paket:", k1paket())
    k1kruemmung()
    k1feld()


if __name__ == "__main__":
    alle()
