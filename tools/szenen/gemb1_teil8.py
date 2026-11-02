"""GEMB 1 Teil 8 (kap8_stufen.tex): Vom Atom zum Band.

Aufruf: python tools/szenen/gemb1_teil8.py, danach python tools/szenen_ansehen.py out.png gemb1/k8bloch ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap8.py.
"""
import sys
from math import cos, exp, pi, sin, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GR = 24
HELLROT, HELLBLAU, HELLGRUEN = "#f6dede", "#dceafa", "#ddf0e4"
C0 = 0.038100                       # hbar^2/(2 m0) in eV nm^2
W, VB = 1.0, 1.0                    # Kammpotential: Topf 1 nm, Höhe 1 eV
Es, Vss, Ep, Vpp, Vsp, A0 = -5.0, 0.5, -1.0, 0.75, 0.6, 0.25


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def achse(s, name, einheit):
    return s.tr("a_" + name + einheit, name + " in " + einheit, name + " in " + einheit, name + " en " + einheit, name + " / " + einheit)


def f_kp(E, w, b, vb):
    q = sqrt(E / C0)
    if E < vb:
        ka = sqrt((vb - E) / C0)
        return cos(q * w) * np.cosh(ka * b) + (ka**2 - q**2) / (2 * q * ka) * sin(q * w) * np.sinh(ka * b)
    ka = sqrt(max(E - vb, 1e-12) / C0)
    return cos(q * w) * cos(ka * b) - (ka**2 + q**2) / (2 * q * ka) * sin(q * w) * sin(ka * b)


def baender(w, b, vb, emax=1.3, n=4001):
    es = np.linspace(1e-4, emax, n)
    fs = np.array([f_kp(x, w, b, vb) for x in es])
    ok = np.abs(fs) <= 1
    aus, i = [], 0
    while i < n:
        if ok[i]:
            j = i
            while j + 1 < n and ok[j + 1]:
                j += 1
            aus.append((es[i:j + 1], fs[i:j + 1]))
            i = j + 1
        else:
            i += 1
    return aus


def bloch(ka, b, M=280):
    """Tiefster Zustand zur Phase ka in einer Zelle aus Topf und Barriere (Gitter aus Teil 2 mit Bloch-Rand)."""
    a = W + b
    dx = a / M
    x = (np.arange(M) + 0.5) * dx
    V = np.where(x < W, 0.0, VB)
    tt = C0 / dx**2
    H = np.diag(2 * tt + V + 0j) + np.diag(-tt * np.ones(M - 1) + 0j, 1) + np.diag(-tt * np.ones(M - 1) + 0j, -1)
    H[M - 1, 0] += -tt * np.exp(1j * ka)
    H[0, M - 1] += -tt * np.exp(-1j * ka)
    E, U = np.linalg.eigh(H)
    return x, U[:, 0], E[0]


# ------------------------------------------------------------------------------------------ Stufe 1
def k8bloch():
    """Periodisches Potential, Bloch-Funktion und ihre Dichte für das Kammpotential b = 0,4 nm."""
    s = Szene("gemb1/k8bloch")
    b = 0.4
    a = W + b
    z = 8
    ka = 2 * pi / z
    x0, u0, E = bloch(ka, b)
    x, psi = [], []
    for l in range(z):
        x += list(x0 + l * a)
        psi += list(u0 * np.exp(1j * ka * l))
    x, psi = np.array(x), np.array(psi)
    # Phase so wählen, dass der Realteil bei x = W/2 groß ist
    i0 = np.argmin(np.abs(x - W / 2))
    psi = psi * np.exp(-1j * np.angle(psi[i0]))
    psi = psi / np.abs(psi).max()
    xm = z * a
    c = s.achsen((0, xm), (-0.1, 1.2), breite=6.0, hoehe=0.7, mitte=(0.1, 1.5), xl="", yl="V in eV", xzahlen=False, xticks=";".join("%.1f" % (l * a) for l in range(z + 1)),
                 yticks="0;1")
    pts = []
    for l in range(z):
        pts += [(l * a, 0), (l * a + W, 0), (l * a + W, 1), ((l + 1) * a, 1)]
    pts.append((xm, 0))
    s.daten(c, [p for i, p in enumerate(pts) if i < len(pts) - 1], farbe=SCHWARZ, dicke=3)
    s.linie(c, (0, E), (xm, E), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(c, "E", (xm + 0.35, E), groesse=GR, ausrichtung="center", farbe=ROT)
    s.pfeil((0.0, 1.13), (a, 1.13), "", farbe=SCHWARZ, spitze=0.11, doppelt=True, dicke=2, on=c)
    s.text(c, "a", (0.5 * a, 0.62), groesse=GR, ausrichtung="center")
    d = s.achsen((0, xm), (-1.15, 1.15), breite=6.0, hoehe=0.85, mitte=(0.1, 0.15), yl="Re \\psi", xzahlen=False, xticks=";".join("%.1f" % (l * a) for l in range(z + 1)), yzahlen=False, ymarks=False)
    s.kurve(d, "cos(%.5f*x)" % (2 * pi / xm), farbe=ORANGE, dicke=3, dash=DASH)
    s.kurve(d, "-cos(%.5f*x)" % (2 * pi / xm), farbe=ORANGE, dicke=3, dash=DASH)
    s.linie(d, (0, 0), (xm, 0), farbe=GRAU, dicke=1.5)
    st = 2
    s.daten(d, list(zip(x[::st], (psi.real)[::st])), farbe=BLAU, dicke=3.5)
    e = s.achsen((0, xm), (0, 1.15), breite=6.0, hoehe=0.6, mitte=(0.1, -1.05), xl=achse(s, "x", "nm"), yl="|\\psi|^2", xticks=";".join("%d" % v for v in range(0, 12, 2)), yzahlen=False, ymarks=False)
    s.daten(e, list(zip(x[::st], (np.abs(psi)**2)[::st])), farbe=ROT, dicke=3.5)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def kammband(s, mx, b, titel, links):
    a = W + b
    bd = baender(W, b, VB)
    em = 1.2
    d = s.achsen((0, 2), (0, em), breite=2.7, hoehe=2.1, mitte=(mx, 0), xl=s.tr("k_zone", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)"),
                 yl=achse(s, "E", "eV"), xticks="0;1;2", yticks="0;0.5;1", titel=titel, titel_mitte=True)
    for es, _ in bd[:2]:
        s.band(d, 0, 2, es[0], es[-1], farbe=BLAU, deckung=0.12)
    s.band(d, 0, 2, bd[0][0][-1], bd[1][0][0], farbe=GRAU, deckung=0.25)
    k = lambda f: float(np.arccos(np.clip(f, -1, 1)) / pi)
    p1 = [(k(fv), ev) for ev, fv in zip(*bd[0])]
    p2 = [(2 - k(fv), ev) for ev, fv in zip(*bd[1])]
    par = [(i / 100, C0 * (pi / a * i / 100) ** 2) for i in range(0, 201)]
    s.daten(d, [p for p in par if p[1] <= em], farbe=GRUEN, dicke=3, dash=DASH)
    s.daten(d, duenn(sorted(p1), 1e-3), farbe=BLAU, dicke=5)
    s.daten(d, duenn(sorted(p2), 1e-3), farbe=BLAU, dicke=5)
    s.linie(d, (1, 0), (1, em), farbe=GRAU, dicke=2, dash=DASH)
    mitte = 0.5 * (bd[0][0][-1] + bd[1][0][0])
    s.text(d, s.tr("luecke", "Lücke", "gap", "brecha", "带隙"), (0.42, mitte), groesse=GR, ausrichtung="center", farbe=SCHWARZ)


def k8baender():
    """Kammpotential mit dünner und dicker Barriere: E(k), gestrichelt das freie Elektron."""
    s = Szene("gemb1/k8baender")
    ti1 = s.tr("b02", "Barriere 0.2 nm", "barrier 0.2 nm", "barrera 0.2 nm", "势垒 0.2 nm")
    ti2 = s.tr("b04", "Barriere 0.4 nm", "barrier 0.4 nm", "barrera 0.4 nm", "势垒 0.4 nm")
    kammband(s, -1.75, 0.2, ti1, True)
    kammband(s, 1.75, 0.4, ti2, False)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def doppel(w, b, vb, rand=2.0, dx=0.01):
    L = 2 * w + b
    x = np.arange(-rand, L + rand + dx / 2, dx)
    V = np.full_like(x, vb)
    V[(x > 0) & (x < w)] = 0
    V[(x > w + b) & (x < L)] = 0
    tt = C0 / dx**2
    n = len(x)
    H = np.diag(2 * tt + V) + np.diag(-tt * np.ones(n - 1), 1) + np.diag(-tt * np.ones(n - 1), -1)
    E, U = np.linalg.eigh(H)
    return x, V, E, U


def k8doppel():
    """Zwei Töpfe: bindender und antibindender Zustand, darunter die Dichten, rechts das Niveauschema."""
    s = Szene("gemb1/k8doppel")
    s.welt()
    x, V, E, U = doppel(W, 0.4, VB)
    u0, u1 = U[:, 0], U[:, 1]
    u0 = u0 / np.abs(u0).max() * (1 if u0[np.argmin(np.abs(x - 0.5))] > 0 else -1)
    u1 = u1 / np.abs(u0).max()
    u1 = u1 / np.abs(u1).max() * (1 if u1[np.argmin(np.abs(x - 0.5))] > 0 else -1)
    xm = (-0.6, 3.0)
    st = 4
    for j, (u, farbe, tit) in enumerate(((u0, BLAU, s.tr("bd", "bindend", "bonding", "enlazante", "成键")), (u1, ROT, s.tr("ab", "antibindend", "antibonding", "antienlazante", "反键")))):
        mx = -2.72 + j * 2.05
        a = s.achsen(xm, (-1.2, 1.2), breite=1.85, hoehe=1.15, mitte=(mx, 0.85), xl="", yl="", xzahlen=False, xmarks=False, yzahlen=False, ymarks=False, titel=tit, titel_mitte=True)
        s.band(a, 1.0, 1.4, -1.2, 1.2, farbe=GRAU, deckung=0.25)
        s.band(a, xm[0], 0, -1.2, 1.2, farbe=GRAU, deckung=0.25)
        s.band(a, 2.4, xm[1], -1.2, 1.2, farbe=GRAU, deckung=0.25)
        s.linie(a, (xm[0], 0), (xm[1], 0), farbe=GRAU, dicke=1.5)
        s.daten(a, list(zip(x[::st], u[::st])), farbe=farbe, dicke=4)
        b = s.achsen(xm, (0, 1.2), breite=1.85, hoehe=1.0, mitte=(mx, -0.45), xl=achse(s, "x", "nm"), yl="", xticks="0;1;2", yzahlen=False, ymarks=False)
        s.band(b, 1.0, 1.4, 0, 1.2, farbe=GRAU, deckung=0.25)
        s.band(b, xm[0], 0, 0, 1.2, farbe=GRAU, deckung=0.25)
        s.band(b, 2.4, xm[1], 0, 1.2, farbe=GRAU, deckung=0.25)
        s.daten(b, list(zip(x[::st], (u**2)[::st])), farbe=farbe, dicke=4)
    t(s, "\\psi", (-3.9, 0.85), "center")
    t(s, "|\\psi|^2", (-3.92, -0.45), "center")
    # Niveauschema
    d = s.achsen((0, 3), (168, 212), breite=1.3, hoehe=2.45, mitte=(2.24, 0.1), yl=achse(s, "E", "meV"), xzahlen=False, xmarks=False, yticks="170;190;210")
    Em = 190.8
    Eb, Ea = E[0] * 1000, E[1] * 1000
    s.linie(d, (0.1, Em), (0.9, Em), farbe=SCHWARZ, dicke=4)
    s.linie(d, (2.1, Em), (2.9, Em), farbe=SCHWARZ, dicke=4)
    s.linie(d, (1.1, Eb), (1.9, Eb), farbe=BLAU, dicke=5)
    s.linie(d, (1.1, Ea), (1.9, Ea), farbe=ROT, dicke=5)
    for (p, q) in (((0.9, Em), (1.1, Eb)), ((0.9, Em), (1.1, Ea)), ((1.9, Eb), (2.1, Em)), ((1.9, Ea), (2.1, Em))):
        s.linie(d, p, q, farbe=GRAU, dicke=2, dash=DASH)
    s.text(d, "E_s", (0.5, Em + 3.2), groesse=GR, ausrichtung="center")
    s.text(d, "E_{\\sigma^*}", (1.5, Ea + 3.4), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(d, "E_\\sigma", (1.5, Eb - 3.6), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k8vier():
    """Vier Atome: Koeffizienten der vier Zustände mit Einhüllender, rechts die Energien auf dem Kosinus-Band."""
    s = Szene("gemb1/k8vier")
    s.welt()
    A = sqrt(2 / 5)
    pos = [(-2.75, 0.85), (-1.05, 0.85), (-2.75, -0.85), (-1.05, -0.85)]
    for n, mi in zip((1, 2, 3, 4), pos):
        a = s.achsen((0, 5), (-0.8, 0.8), breite=1.45, hoehe=1.0, mitte=mi, xl="\\ell" if n > 2 else "", yl="", xticks="1;2;3;4", yticks="-0.6;0;0.6", yzahlen=n in (1, 3),
                     titel="n = %d" % n, titel_mitte=True, xzahlen=n > 2)
        s.kurve(a, "%.5f*sin(%d*pi*x/5)" % (A, n), x=(0, 5), farbe=ORANGE, dicke=3, dash=DASH)
        s.linie(a, (0, 0), (5, 0), farbe=GRAU, dicke=1.5)
        s.stems(a, [1, 2, 3, 4], [A * sin(n * pi * l / 5) for l in (1, 2, 3, 4)], farbe=BLAU, r=0.07, dicke=3.5)
    t(s, "c_\\ell", (-3.45, 1.55), "center")
    t(s, "c_\\ell", (-3.45, -0.15), "center")
    b = s.achsen((0, 1), (-6.2, -3.8), breite=2.2, hoehe=2.55, mitte=(1.75, 0.0), xl=s.tr("ka_pi", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)"), yl=achse(s, "E", "eV"), xticks="0;0.5;1", yticks="-6;-5;-4")
    s.kurve(b, "-5-cos(pi*x)", x=(0, 1), farbe=BLAU, dicke=4)
    s.linie(b, (0, -5), (1, -5), farbe=GRAU, dicke=2, dash=DASH)
    s.text(b, "E_s", (0.1, -4.85), groesse=GR, ausrichtung="center", farbe=GRAU)
    for n in (1, 2, 3, 4):
        k = n / 5
        e = Es - 2 * Vss * cos(pi * k)
        s.linie(b, (0, e), (k, e), farbe=ROT, dicke=1.8, dash=DASH)
        s.punkt(b, k, e, farbe=ROT, r=0.08)
        s.text(b, "E_%d" % n, (k + 0.12, e - 0.12), groesse=GR, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k8leiter():
    """Niveaus für wachsendes N, E(k) für N = 20 und die Zustände am Bandboden, in der Mitte und oben."""
    s = Szene("gemb1/k8leiter")
    s.welt()
    a = s.achsen((0.1, 6.5), (-6.25, -3.75), breite=3.3, hoehe=1.5, mitte=(-1.55, 1.15), yl=achse(s, "E", "eV"), xzahlen=False, xmarks=False, yticks="-6;-5;-4", xl="")
    for i, N in enumerate((1, 2, 4, 8, 20)):
        for n in range(1, N + 1):
            e = Es - 2 * Vss * cos(n * pi / (N + 1))
            s.linie(a, (i + 0.72, e), (i + 1.28, e), farbe=BLAU, dicke=2.5 if N > 8 else 3.5)
        s.text(a, "%d" % N, (i + 1.0, -6.68), groesse=GR, ausrichtung="center")
    s.band(a, 5.72, 6.28, -6, -4, farbe=BLAU, deckung=0.7)
    s.text(a, "\\infty", (6.0, -6.68), groesse=GR, ausrichtung="center")
    s.text(a, "N:", (0.35, -6.68), groesse=GR, ausrichtung="center")
    b = s.achsen((-1, 1), (-6.25, -3.75), breite=2.2, hoehe=1.5, mitte=(2.15, 1.15), xl=s.tr("k_z2", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)"), yl="", xticks="-1;0;1", yticks="-6;-5;-4", yzahlen=False)
    s.kurve(b, "-5-cos(pi*x)", x=(-1, 1), farbe=BLAU, dicke=3.5)
    N = 20
    for n in range(1, N + 1):
        s.punkt(b, n / (N + 1), Es - 2 * Vss * cos(n * pi / (N + 1)), farbe=ROT, r=0.05)
    s.text(b, "N = 20", (-0.48, -4.2), groesse=GR, ausrichtung="center", farbe=ROT)
    # Wellen
    nz = 8
    xs = np.linspace(-0.6, nz - 0.4, 500)
    orb = lambda x, l: exp(-((x - l) / 0.3) ** 2)
    for j, (ka, ti) in enumerate(((0.0, "k = 0"), (pi / 2, "k = \\pi/(2a)"), (pi, "k = \\pi/a"))):
        c = s.achsen((-0.6, nz - 0.4), (-1.3, 1.3), breite=2.05, hoehe=0.95, mitte=(-2.33 + j * 2.33, -1.5), xl="", yl="", xzahlen=False, xmarks=False, yzahlen=False, ymarks=False, titel=ti, titel_mitte=True)
        s.linie(c, (-0.6, 0), (nz - 0.4, 0), farbe=GRAU, dicke=1.5)
        if ka > 0:
            s.kurve(c, "cos(%.5f*x)" % ka, x=(-0.6, nz - 0.4), farbe=ORANGE, dicke=2.5, dash=DASH)
        ys = [sum(orb(x, l) * cos(ka * l) for l in range(nz)) for x in xs]
        s.daten(c, list(zip(xs, ys)), farbe=BLAU, dicke=3.5)
        for l in range(nz):
            s.punkt(c, l, 0, farbe=SCHWARZ, r=0.04)
        tx = ("E_s - 2V_{ss}", "E_s", "E_s + 2V_{ss}")[j]
        s.text(c, tx, (3.5, -2.3), groesse=GR, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def poly(s, on, ecken, farbe, deckung=0.3):
    return s._add("Polygon", {"vertices": [[float(x), float(y), 0] for x, y in ecken], "color": farbe, "fill_color": farbe,
                              "fill_opacity": deckung, "stroke_width": 0}, on)


def k8abstand():
    """Aufspaltung der Niveaus mit dem Abstand; rechts die drei Fälle der Besetzung."""
    s = Szene("gemb1/k8abstand")
    s.welt()
    rr = np.linspace(0.15, 0.7, 120)
    a = s.achsen((0.15, 0.7), (-10, 2), breite=3.0, hoehe=2.55, mitte=(-2.0, 0.1), xl=s.tr("r_nm", "Abstand r in nm", "spacing r in nm", "distancia r en nm", "间距 r / nm"), yl=achse(s, "E", "eV"), xticks="0.2;0.4;0.6", yticks="-8;-4;0")
    kap = {"s": 11.46, "p": 5.12}
    for nam, e0, v0, kp, farbe in (("s", Es, Vss, kap["s"], BLAU), ("p", Ep, Vpp, kap["p"], GRUEN)):
        ob = [(r, e0 + 2 * v0 * exp(-kp * (r - A0))) for r in rr]
        un = [(r, e0 - 2 * v0 * exp(-kp * (r - A0))) for r in rr]
        poly(s, a, ob + un[::-1], farbe, 0.3)
        s.daten(a, ob, farbe=farbe, dicke=2.5)
        s.daten(a, un, farbe=farbe, dicke=2.5)
    ek = -8.5
    un = [(r, ek - 2 * 0.0027 * exp(-30 * (r - A0)) - 0.03) for r in rr]
    ob = [(r, ek + 2 * 0.0027 * exp(-30 * (r - A0)) + 0.03) for r in rr]
    s.linie(a, (0.15, ek), (0.7, ek), farbe=ORANGE, dicke=3.5)
    s.linie(a, (A0, -10), (A0, 2), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(a, "r_0", (A0 + 0.04, -9.4), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(a, "s", (0.64, -4.35), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(a, "p", (0.64, -0.2), groesse=GR, ausrichtung="center", farbe=GRUEN)
    s.text(a, s.tr("kern", "kernnah", "core", "interno", "内层"), (0.58, -7.85), groesse=GR, ausrichtung="center", farbe=ORANGE)
    # Besetzung
    def saeule(x, u1, o1, voll1, u2, o2, voll2, name):
        br = 0.82
        s.band(None, x - br / 2, x + br / 2, u1, u1 + (o1 - u1) * voll1, farbe=BLAU, deckung=0.75)
        s.band(None, x - br / 2, x + br / 2, u2, u2 + (o2 - u2) * voll2, farbe=BLAU, deckung=0.75)
        for (u, o) in ((u1, o1), (u2, o2)):
            s.linie(None, (x - br / 2, u), (x + br / 2, u), farbe=SCHWARZ, dicke=2.5)
            s.linie(None, (x - br / 2, o), (x + br / 2, o), farbe=SCHWARZ, dicke=2.5)
            s.linie(None, (x - br / 2, u), (x - br / 2, o), farbe=SCHWARZ, dicke=2.5)
            s.linie(None, (x + br / 2, u), (x + br / 2, o), farbe=SCHWARZ, dicke=2.5)
        t(s, name, (x, -1.5), "center", g=23)
    y0 = -1.15
    saeule(0.4, y0, y0 + 1.05, 0.5, y0 + 1.5, y0 + 2.55, 0.0, s.tr("metall", "Metall", "metal", "metal", "金属"))
    saeule(1.42, y0, y0 + 0.8, 1.0, y0 + 1.9, y0 + 2.7, 0.0, s.tr("isolator", "Isolator", "insulator", "aislante", "绝缘体"))
    saeule(2.5, y0, y0 + 1.1, 1.0, y0 + 1.45, y0 + 2.55, 0.0, s.tr("hl", "Halbleiter", "semicond.", "semicond.", "半导体"))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def s_orb(s, x, y, zeichen="+"):
    farbe = BLAU if zeichen == "+" else ROT
    s.kreis(None, x, y, 0.24, farbe=farbe, dicke=2, deckung=0.3)
    t(s, zeichen.replace("-", "−"), (x, y), "center", g=24)


def p_orb(s, x, y, links="+"):
    rechts = "-" if links == "+" else "+"
    for dx, z in ((-0.2, links), (0.2, rechts)):
        farbe = BLAU if z == "+" else ROT
        s.kreis(None, x + dx, y, 0.2, farbe=farbe, dicke=2, deckung=0.3)
        t(s, z.replace("-", "−"), (x + dx, y), "center", g=24)


def k8sp():
    """Vorzeichen der Kopplung für die Kette mit gleich ausgerichteten p-Orbitalen; rechts die zwei Bänder."""
    s = Szene("gemb1/k8sp")
    s.welt()
    x1, x2 = -3.25, -2.4
    ys = (1.05, 0.4, -0.25, -0.9)
    t(s, "\\ell", (x1, 1.55), "center", GRAU)
    t(s, "\\ell+1", (x2 + 0.08, 1.55), "center", GRAU)
    # s-s
    s_orb(s, x1, ys[0]); s_orb(s, x2 + 0.05, ys[0])
    t(s, "-V_{ss}", (-1.15, ys[0]), "center", BLAU)
    # s-p: s trifft die positive Keule
    s_orb(s, x1, ys[1]); p_orb(s, x2 + 0.22, ys[1], "+")
    t(s, "-V_{sp}", (-1.15, ys[1]), "center", BLAU)
    # p-s: negative Keule trifft s
    p_orb(s, x1 - 0.08, ys[2], "+"); s_orb(s, x2 + 0.05, ys[2])
    t(s, "+V_{sp}", (-1.15, ys[2]), "center", ROT)
    # p-p: negative Keule trifft positive Keule
    p_orb(s, x1 - 0.08, ys[3], "+"); p_orb(s, x2 + 0.22, ys[3], "+")
    t(s, "+V_{pp}", (-1.15, ys[3]), "center", ROT)
    b = s.achsen((0, 1), (-6.6, 1.0), breite=2.6, hoehe=2.25, mitte=(1.75, 0.15), xl=s.tr("k_sp", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)"), yl=achse(s, "E", "eV"), xticks="0;0.5;1", yticks="-6;-4;-2;0")
    s.band(b, 0, 1, -4.0, -2.5, farbe=GRAU, deckung=0.3)
    s.kurve(b, "-5-cos(pi*x)", x=(0, 1), farbe=GRAU, dicke=2.5, dash=DASH)
    s.kurve(b, "-1+1.5*cos(pi*x)", x=(0, 1), farbe=GRAU, dicke=2.5, dash=DASH)
    un, ob = [], []
    for i in range(201):
        ka = pi * i / 200
        A = Es - 2 * Vss * cos(ka)
        B = Ep + 2 * Vpp * cos(ka)
        w = sqrt(((A - B) / 2) ** 2 + 4 * Vsp**2 * sin(ka) ** 2)
        un.append((i / 200, (A + B) / 2 - w))
        ob.append((i / 200, (A + B) / 2 + w))
    s.daten(b, un, farbe=BLAU, dicke=5)
    s.daten(b, ob, farbe=ROT, dicke=5)
    s.text(b, "E_g", (0.22, -3.25), groesse=GR, ausrichtung="center")
    s.text(b, s.tr("s_band", "s-Band", "s band", "banda s", "s 带"), (0.3, -4.75), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.text(b, s.tr("p_band", "p-Band", "p band", "banda p", "p 带"), (0.72, 0.2), groesse=GR, ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k8rezept():
    """Kette mit zwei Atomen je Zelle und die beiden Bänder, gestrichelt das Kosinus-Band der einfachen Kette."""
    s = Szene("gemb1/k8rezept")
    s.welt()
    d = 0.56
    y0, dy = -0.05, 0.2
    # Zellen
    breite = 2 * d
    x0 = -3.55
    for i, (txt) in enumerate((s.tr("links", "links", "left", "izquierda", "左"), s.tr("mitte", "Mitte", "centre", "centro", "中"), s.tr("rechts", "rechts", "right", "derecha", "右"))):
        xl = x0 + i * breite
        if i == 1:
            s.band(None, xl, xl + breite, y0 - 0.55, y0 + 0.55, farbe=GRAU, deckung=0.2)
        t(s, txt, (xl + breite / 2, y0 + 0.74), "center")
        s.linie(None, (xl, y0 - 0.55), (xl, y0 + 0.55), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(None, (x0 + 3 * breite, y0 - 0.55), (x0 + 3 * breite, y0 + 0.55), farbe=GRAU, dicke=2, dash=DASH)
    pts = []
    for i in range(0, 6):
        x = x0 + (i + 0.5) * d
        y = y0 + (dy if i % 2 else -dy)
        pts.append((x, y, i))
    for (p, q) in zip(pts, pts[1:]):
        s.linie(None, p[:2], q[:2], farbe=SCHWARZ, dicke=3)
    for x, y, i in pts:
        s.punkt(None, x, y, farbe=BLAU if i % 2 == 0 else GRUEN, r=0.11)
    xa = x0 + 2.5 * d
    t(s, "A", (x0 + 2.5 * d, y0 - dy - 0.3), "center", BLAU)
    t(s, "B", (x0 + 3.5 * d, y0 + dy + 0.3), "center", GRUEN)
    s.pfeil((x0 + breite * 0, y0 - 0.74), (x0 + breite, y0 - 0.74), "", farbe=SCHWARZ, spitze=0.12, doppelt=True, dicke=2)
    t(s, "a", (x0 + breite / 2, y0 - 0.96), "center")
    b = s.achsen((-1, 1), (-5.6, 5.6), breite=2.3, hoehe=1.85, mitte=(2.1, 0), xl=s.tr("k_rz", "k in \\pi/a", "k in \\pi/a", "k en \\pi/a", "k / (\\pi/a)"), yl=s.tr("e_rel", "E - E_p in eV", "E - E_p in eV", "E - E_p en eV", "E - E_p / eV"), xticks="-1;0;1", yticks="-5;0;5")
    V = 2.5
    s.kurve(b, "%.3f*cos(pi*x/2)" % (2 * V), x=(-1, 1), farbe=ROT, dicke=4.5)
    s.kurve(b, "-%.3f*cos(pi*x/2)" % (2 * V), x=(-1, 1), farbe=BLAU, dicke=4.5)
    s.linie(b, (-1, 0), (1, 0), farbe=GRAU, dicke=1.5)
    s.text(b, s.tr("ab2", "antibindend", "antibonding", "antienlazante", "反键"), (0, 3.3), groesse=GR, ausrichtung="center", farbe=ROT)
    s.text(b, s.tr("bd2", "bindend", "bonding", "enlazante", "成键"), (0, -3.3), groesse=GR, ausrichtung="center", farbe=BLAU)
    s.speichern()


if __name__ == "__main__":
    k8bloch()
    k8baender()
    k8doppel()
    k8vier()
    k8leiter()
    k8abstand()
    k8sp()
    k8rezept()
