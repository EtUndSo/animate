"""GEMB 1 Teil 3 (kap3_stufen.tex): Stufe, Barriere und Tunneleffekt.

Aufruf: python tools/szenen/gemb1_teil3.py, danach python tools/szenen_ansehen.py out.png gemb1/k3stufe ... [--lang de]
Die Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap3.py: Energien in eV, Längen in nm.
"""
import cmath
import sys
from math import atan, cos, exp, pi, sin, sinh, sqrt
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

Z = 26.25                 # 2 m_e / hbar^2 in 1/(eV nm^2)
HBAR = 0.6582             # eV fs
WAND = "#c9c9c9"
GR = 24


def k(E):
    return sqrt(Z * E)


def T_stufe(q):
    """T über E/V0 > 1."""
    x = sqrt(1 - 1 / q)
    return 4 * x / (1 + x) ** 2


def T_barr(E, V0, L):
    if abs(E - V0) < 1e-9:
        return 1 / (1 + Z * V0 * L ** 2 / 4)
    if E < V0:
        return 1 / (1 + sinh(k(V0 - E) * L) ** 2 / (4 * E / V0 * (1 - E / V0)))
    return 1 / (1 + sin(k(E - V0) * L) ** 2 / (4 * E / V0 * (E / V0 - 1)))


def t(s, on, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(on, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def nm_achse(s):
    return s.tr("x_nm", "x in nm", "x in nm", "x en nm", "x / nm")


def ev_achse(s):
    return s.tr("E_ev", "E in eV", "E in eV", "E en eV", "E / eV")


def k_achse(s):
    return s.tr("k_nm", "k in 1/nm", "k in 1/nm", "k en 1/nm", "k / (1/nm)")


# ------------------------------------------------------------------------------------------ Stufe 1
def k3stufe():
    """Links und rechts die Parabel E(k) des jeweiligen Gebiets, in der Mitte der Potentialverlauf auf derselben Energieachse."""
    s = Szene("gemb1/k3stufe")
    Eo, Eu = 3.0, 0.5
    h = 2.75
    gI = s.tr("gI", "Gebiet I", "region I", "región I", "区域 I")
    gII = s.tr("gII", "Gebiet II", "region II", "región II", "区域 II")
    # Links: Parabel
    a = s.achsen((-10, 10, 5), (0, 4, 1), breite=1.7, hoehe=h, mitte=(-2.4, 0), xl=k_achse(s), yl=ev_achse(s))
    s.kurve(a, f"x^2/{Z}", x=(-9.1, 9.1), farbe=GRUEN, dicke=4)
    s.linie(a, (-10, Eo), (10, Eo), farbe=BLAU, dicke=3)
    s.linie(a, (-10, Eu), (10, Eu), farbe=ROT, dicke=3)
    for E, f in ((Eo, BLAU), (Eu, ROT)):
        for q in (-k(E), k(E)):
            s.punkt(a, q, E, farbe=f, r=0.075)
    t(s, a, gI, (0, 3.65), g=22)
    # Mitte: Potential
    b = s.achsen((-1, 1, 1), (0, 4, 1), breite=1.7, hoehe=h, mitte=(0.0, 0), xl=nm_achse(s), yl="V(x)", yzahlen=False)
    s.band(b, 0, 1, 0, 2, farbe=WAND, deckung=0.55)
    s.daten(b, [(-1, 0), (0, 0), (0, 2), (1, 2)], farbe=SCHWARZ, dicke=5)
    s.linie(b, (-1, Eo), (1, Eo), farbe=BLAU, dicke=3)
    s.linie(b, (-1, Eu), (1, Eu), farbe=ROT, dicke=3)
    t(s, b, "E > V_0", (-0.45, 3.3), farbe=BLAU, g=22)
    t(s, b, "E < V_0", (-0.45, 0.8), farbe=ROT, g=22)
    t(s, b, "V_0", (0.5, 2.3))
    # Rechts: Parabel, um V0 angehoben
    c = s.achsen((-10, 10, 5), (0, 4, 1), breite=1.7, hoehe=h, mitte=(2.4, 0), xl=k_achse(s), yl=ev_achse(s), yzahlen=False)
    s.kurve(c, f"2+x^2/{Z}", x=(-7.2, 7.2), farbe=GRUEN, dicke=4)
    s.linie(c, (-10, 2), (10, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(c, (-10, Eo), (10, Eo), farbe=BLAU, dicke=3)
    s.linie(c, (-10, Eu), (10, Eu), farbe=ROT, dicke=3)
    for q in (-k(1), k(1)):
        s.punkt(c, q, Eo, farbe=BLAU, r=0.075)
    t(s, c, gII, (0, 3.65), g=22)
    t(s, c, s.tr("kein_k", "kein reelles k", "no real k", "sin k real", "无实数 k"), (0, 0.95), farbe=ROT, g=22)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k3oben():
    """Links die Welle oberhalb der Stufe, rechts R und T über E/V0."""
    s = Szene("gemb1/k3oben")
    E, V0 = 3.0, 2.0
    kI, kII = k(E), k(E - V0)
    B = (kI - kII) / (kI + kII)
    C = 2 * kI / (kI + kII)
    a = s.achsen((-2, 2, 1), (-2.4, 2.4, 1), breite=2.9, hoehe=2.15, mitte=(-1.7, 0), xl=nm_achse(s), yl="Re ψ, |ψ|")
    s.band(a, 0, 2, -2.4, 2.4, farbe=WAND, deckung=0.45)
    xs = np.linspace(-2, 0, 260)
    s.daten(a, [(x, abs(cmath.exp(1j * kI * x) + B * cmath.exp(-1j * kI * x))) for x in xs] + [(2, C)], farbe=ORANGE, dicke=3, dash=DASH)
    s.daten(a, [(x, cos(kI * x) + B * cos(kI * x)) for x in xs], farbe=BLAU, dicke=4)
    xs = np.linspace(0, 2, 180)
    s.daten(a, [(x, C * cos(kII * x)) for x in xs], farbe=BLAU, dicke=4)
    s.linie(a, (-2, 0), (2, 0), farbe=GRAU, dicke=2)
    t(s, a, "λ_I", (-1.0, 1.85), farbe=BLAU)
    t(s, a, "λ_II", (1.0, 1.85), farbe=BLAU)
    t(s, a, "|ψ|", (0.32, 1.85), farbe=ORANGE)
    b = s.achsen((1, 5, 1), (0, 1, 0.5), breite=2.6, hoehe=2.15, mitte=(2.0, 0), xl="E / V_0", yl="R, T")
    s.kurve(b, "4*sqrt(1-1/x)/(1+sqrt(1-1/x))^2", x=(1.0005, 5), farbe=BLAU, dicke=5)
    s.kurve(b, "1-4*sqrt(1-1/x)/(1+sqrt(1-1/x))^2", x=(1.0005, 5), farbe=ROT, dicke=5)
    s.linie(b, (1, 1), (5, 1), farbe=GRAU, dicke=3, dash=DASH)
    t(s, b, "T", (3.6, 0.82), farbe=BLAU)
    t(s, b, "R", (2.1, 0.14), farbe=ROT)
    t(s, b, s.tr("klass", "klassisch", "classical", "clásico", "经典"), (3.3, 1.07), farbe=GRAU, g=22)
    s.punkt(b, 1.5, T_stufe(1.5), farbe=BLAU)
    s.punkt(b, 1.5, 1 - T_stufe(1.5), farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k3unten():
    """Stehende Welle links, abklingende Welle rechts, für zwei Energien."""
    s = Szene("gemb1/k3unten")
    V0 = 2.0

    def teil(E, mitte, key, farbe):
        kI, ka = k(E), k(V0 - E)
        ph = atan(ka / kI)
        a = s.achsen((-1.5, 1, 0.5), (-2.2, 2.2, 1), breite=2.75, hoehe=2.05, mitte=mitte, xl=nm_achse(s), yl="ψ")
        s.band(a, 0, 1, -2.2, 2.2, farbe=WAND, deckung=0.45)
        s.linie(a, (-1.5, 0), (1, 0), farbe=GRAU, dicke=2)
        xs = np.linspace(-1.5, 0, 150)
        s.daten(a, [(x, 2 * cos(kI * x + ph)) for x in xs], farbe=farbe, dicke=4)
        xs = np.linspace(0, 1, 120)
        s.daten(a, [(x, 2 * cos(ph) * exp(-ka * x)) for x in xs], farbe=farbe, dicke=4)
        d = 1 / ka
        y0 = 2 * cos(ph)
        s.linie(a, (d, 0), (d, y0 / 2.718), farbe=ROT, dicke=3, dash=DASH)
        s.punkt(a, d, y0 / 2.718, farbe=ROT, r=0.07)
        s.linie(a, (0, 0), (d, 0), farbe=ROT, dicke=5)
        t(s, a, "δ", (d / 2 + 0.03, -0.5), farbe=ROT)
        t(s, a, s.tr(key, "E = %g eV" % E, "E = %g eV" % E, "E = %g eV" % E, "E = %g eV" % E), (0.5, 1.75), g=22)

    teil(0.5, (-1.8, 0), "t05", BLAU)
    teil(1.5, (1.85, 0), "t15", ORANGE)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def paket():
    """Wellenpaket an der Barriere, Split-Operator. Gibt x, |psi|^2 zu Beginn und am Ende, Anteil rechts zurück."""
    L, V0, E0, sig = 0.4, 2.0, 1.5, 1.2
    N, dom = 4096, 80.0
    x = (np.arange(N) - N / 2) * dom / N
    dx = x[1] - x[0]
    q = 2 * np.pi * np.fft.fftfreq(N, dx)
    V = np.where((x > 0) & (x < L), V0, 0.0)
    k0 = k(E0)
    psi = np.exp(-(x + 7.0) ** 2 / (4 * sig ** 2) + 1j * k0 * x)
    psi = psi / np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
    p0 = np.abs(psi) ** 2
    dt = 0.002          # fs
    fak = 1 / Z / HBAR  # hbar/(2m) in nm^2/fs
    kin = np.exp(-1j * fak * q ** 2 * dt)
    pot = np.exp(-0.5j * V / HBAR * dt)
    n = int(17.0 / dt)
    for _ in range(n):
        psi = pot * psi
        psi = np.fft.ifft(kin * np.fft.fft(psi))
        psi = pot * psi
    p1 = np.abs(psi) ** 2
    rechts = float(np.sum(p1[x > L]) * dx)
    return x, p0, p1, rechts, n * dt


def k3barriere():
    """Oben stationäre Lösung an der Barriere, unten Wellenpaket vor und nach dem Treffen."""
    s = Szene("gemb1/k3barriere")
    E, V0, L = 0.5, 2.0, 0.4
    q, ka = k(E), k(V0 - E)
    M = np.array([[1, -1, -1, 0],
                  [-1j * q, ka, -ka, 0],
                  [0, exp(-ka * L), exp(ka * L), -cmath.exp(1j * q * L)],
                  [0, -ka * exp(-ka * L), ka * exp(ka * L), -1j * q * cmath.exp(1j * q * L)]], dtype=complex)
    B, C, D, F = np.linalg.solve(M, np.array([-1, -1j * q, 0, 0], dtype=complex))

    def psi(x):
        if x < 0:
            return cmath.exp(1j * q * x) + B * cmath.exp(-1j * q * x)
        if x < L:
            return C * exp(-ka * x) + D * exp(ka * x)
        return F * cmath.exp(1j * q * x)

    a = s.achsen((-3, 3, 1), (-2.4, 2.4, 1), breite=6.3, hoehe=1.55, mitte=(0.2, 1.3), xl=nm_achse(s), yl="Re ψ, |ψ|")
    s.band(a, 0, L, -2.4, 2.4, farbe=WAND, deckung=0.6)
    s.linie(a, (-3, 0), (3, 0), farbe=GRAU, dicke=2)
    xs = np.linspace(-3, 3, 900)
    s.daten(a, [(x, abs(psi(x))) for x in xs], farbe=ORANGE, dicke=3, dash=DASH)
    s.daten(a, [(x, psi(x).real) for x in xs], farbe=BLAU, dicke=4)
    t(s, a, "I", (-1.5, 2.0), g=26)
    t(s, a, "II", (0.2, 2.0), g=26)
    t(s, a, "III", (1.7, 2.0), g=26)
    t(s, a, "|ψ|", (2.6, 0.62), farbe=ORANGE)
    t(s, a, "Re ψ", (1.35, -0.75), farbe=BLAU)
    x, p0, p1, rechts, tf = paket()
    b = s.achsen((-12, 12, 4), (0, 0.45, 0.2), breite=6.3, hoehe=1.3, mitte=(0.2, -1.55), xl=nm_achse(s), yl="|ψ|^2")
    s.band(b, 0, 0.4, 0, 0.45, farbe="#8a8a8a", deckung=0.8)
    sel = (x > -12) & (x < 12)
    xp = x[sel][::2]
    s.daten(b, list(zip(xp.tolist(), p0[sel][::2].tolist())), farbe=GRAU, dicke=3, dash=DASH)
    s.daten(b, list(zip(xp.tolist(), p1[sel][::2].tolist())), farbe=BLAU, dicke=4)
    t(s, b, s.tr("vorher", "vorher", "before", "antes", "之前"), (-7, 0.39), farbe=GRAU)
    t(s, b, s.tr("nachher", "nachher", "after", "después", "之后"), (-2.2, 0.3), farbe=BLAU)
    s.speichern()
    print("Paket: Anteil rechts =", rechts, " T(E0) =", T_barr(1.5, 2, 0.4), " Zeit", tf)


# ------------------------------------------------------------------------------------------ Stufe 5
def k3tunnelT():
    """Links T(L) logarithmisch, rechts T(E) bei L = 1 nm, auch oberhalb der Barriere."""
    s = Szene("gemb1/k3tunnelT")
    V0 = 2.0
    a = s.achsen((0, 3, 1), (1e-18, 1), breite=2.55, hoehe=2.25, mitte=(-1.8, 0), xl=s.tr("L_nm", "L in nm", "L in nm", "L en nm", "L / nm"), yl="T",
                 ylog=True, yticks="1e-18;1e-12;1e-6;1")
    for E, f in ((0.5, BLAU), (1.0, GRUEN), (1.5, ORANGE)):
        pts = [(0.01 * i, T_barr(E, V0, 0.01 * i)) for i in range(1, 301)]
        s.daten(a, [(0, 1)] + pts[::3], farbe=f, dicke=4)
    t(s, a, "E = 1.5 eV", (1.25, 3e-3), a="left", farbe=ORANGE, g=22)
    t(s, a, "E = 1 eV", (0.55, 1e-12), a="left", farbe=GRUEN, g=22)
    t(s, a, "E = 0.5 eV", (0.32, 3e-16), a="left", farbe=BLAU, g=22)
    b = s.achsen((0, 7, 1), (0, 1, 0.5), breite=2.7, hoehe=2.25, mitte=(1.9, 0), xl=ev_achse(s), yl="T")
    s.band(b, 0, 2, 0, 1, farbe=WAND, deckung=0.35)
    pts = [(0.005 * i, T_barr(0.005 * i, V0, 1.0)) for i in range(1, 1401)]
    s.daten(b, pts, farbe=BLAU, dicke=4)
    t(s, b, "E < V_0", (0.98, 0.5), g=22)
    t(s, b, "L = 1 nm", (5.3, 0.55), g=22)
    for n in (1, 2, 3):
        s.punkt(b, 2 + n * n * pi * pi / (Z * 1.0), 1.0, farbe=ROT, r=0.07)
    s.speichern()


def k3prisma():
    """Totalreflexion im Prisma und verhinderte Totalreflexion mit zweitem Prisma."""
    s = Szene("gemb1/k3prisma")

    def flaeche(pa, pb, pc):
        s.daten(None, [pa, pb, pc, pa], farbe=SCHWARZ, dicke=3)

    # Linkes Teilbild: ein Prisma, rechter Winkel oben links, Hypotenuse von oben rechts nach unten links
    x0 = -2.85
    flaeche((x0, 0.85), (x0 + 1.6, 0.85), (x0, -0.75))
    hx, hy = x0 + 0.8, 0.05
    s.pfeil((x0 - 0.65, hy), (hx, hy), "", farbe=ROT, spitze=0.22, dicke=5)
    s.pfeil((hx, hy), (hx, 1.4), "", farbe=ROT, spitze=0.22, dicke=5)
    n = (sqrt(0.5), -sqrt(0.5))                 # Normale der Hypotenuse, zeigt aus dem Prisma
    tg = (sqrt(0.5), sqrt(0.5))
    pts = []
    for i in range(61):
        u = 0.0115 * i
        y = 0.17 * exp(-3.5 * u) * cos(15 * u)
        pts.append((hx + n[0] * u + tg[0] * y, hy + n[1] * u + tg[1] * y))
    s.daten(None, pts, farbe=BLAU, dicke=3)
    t(s, None, s.tr("t_tot", "Totalreflexion", "total reflection", "reflexión total", "全反射"), (x0 + 0.6, -1.05))
    t(s, None, s.tr("evan", "abklingende Welle", "decaying wave", "onda evanescente", "衰减波"), (x0 + 1.5, -0.55), a="left", farbe=BLAU, g=22)
    # Rechtes Teilbild: zweites Prisma im kleinen Abstand
    x1 = 0.7
    flaeche((x1, 0.85), (x1 + 1.6, 0.85), (x1, -0.75))
    gap = 0.2
    d = (gap * sqrt(0.5), -gap * sqrt(0.5))
    flaeche((x1 + 1.6 + d[0], 0.85 + d[1]), (x1 + d[0], -0.75 + d[1]), (x1 + 1.6 + d[0], -0.75 + d[1]))
    hx, hy = x1 + 0.8, 0.05
    s.pfeil((x1 - 0.65, hy), (hx, hy), "", farbe=ROT, spitze=0.22, dicke=5)
    s.pfeil((hx, hy), (hx, 1.4), "", farbe=ROT, spitze=0.22, dicke=4)
    s.pfeil((hx + d[0], hy), (x1 + 2.4, hy), "", farbe="#dd8888", spitze=0.2, dicke=3)
    t(s, None, s.tr("t_verh", "verhinderte Totalreflexion", "frustrated total reflection", "reflexión total frustrada", "受抑全反射"), (x1 + 0.95, -1.05))
    t(s, None, s.tr("spalt", "Spalt", "gap", "hueco", "间隙"), (x1 + 1.85, 1.18), g=22)
    s.linie(None, (x1 + 1.83, 1.02), (x1 + 1.67, 0.8), farbe=GRAU, dicke=2)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def topf(V0, L):
    """Gebundene Zustände (E, Parität) des endlichen Topfs, Bisektion."""
    def f(E, par):
        q, ka = k(E), k(V0 - E)
        c, s_ = cos(q * L / 2), sin(q * L / 2)
        return (q * s_ - ka * c) if par == 0 else (q * c + ka * s_)
    res = []
    N = 3000
    for i in range(N):
        a0, a1 = V0 * (i + 1e-6) / N, V0 * (i + 1 - 1e-6) / N
        for par in (0, 1):
            if f(a0, par) * f(a1, par) < 0:
                x, y = a0, a1
                for _ in range(70):
                    m = 0.5 * (x + y)
                    if f(x, par) * f(m, par) <= 0:
                        y = m
                    else:
                        x = m
                res.append((0.5 * (x + y), par))
    return sorted(res)


def k3box():
    """Unendlich hohe Wände links, endlich hohe Wände rechts, Niveaus und Wellenfunktionen auf derselben Energieachse."""
    s = Szene("gemb1/k3box")
    L, V0 = 1.0, 2.0
    amp = 0.36
    a = s.achsen((-1.2, 1.2, 0.5), (0, 4, 1), breite=2.6, hoehe=2.75, mitte=(-1.95, 0), xl=nm_achse(s), yl=ev_achse(s))
    s.band(a, -1.2, -0.5, 0, 4, farbe=WAND, deckung=0.55)
    s.band(a, 0.5, 1.2, 0, 4, farbe=WAND, deckung=0.55)
    s.daten(a, [(-0.5, 4), (-0.5, 0), (0.5, 0), (0.5, 4)], farbe=SCHWARZ, dicke=4)
    fb = (BLAU, ROT, GRUEN)
    for n in (1, 2, 3):
        En = n * n * pi * pi / (Z * L * L)
        s.linie(a, (-0.5, En), (0.5, En), farbe=fb[n - 1], dicke=2.5)
        xs = np.linspace(-0.5, 0.5, 100)
        s.daten(a, [(x, En + amp * sin(n * pi * (x + 0.5))) for x in xs], farbe=fb[n - 1], dicke=4)
        t(s, a, f"E_{n}", (0.85, En + 0.14), farbe=fb[n - 1])
    b = s.achsen((-1.2, 1.2, 0.5), (0, 4, 1), breite=2.6, hoehe=2.75, mitte=(1.75, 0), xl=nm_achse(s), yl=ev_achse(s))
    s.band(b, -1.2, -0.5, 0, 2, farbe=WAND, deckung=0.55)
    s.band(b, 0.5, 1.2, 0, 2, farbe=WAND, deckung=0.55)
    s.daten(b, [(-1.2, 2), (-0.5, 2), (-0.5, 0), (0.5, 0), (0.5, 2), (1.2, 2)], farbe=SCHWARZ, dicke=4)
    t(s, b, "V_0 = 2 eV", (0, 3.5), g=24)
    for i, (En, par) in enumerate(topf(V0, L)):
        q, ka = k(En), k(V0 - En)

        def psi(x):
            if abs(x) <= 0.5:
                return cos(q * x) if par == 0 else sin(q * x)
            r = cos(q / 2) if par == 0 else sin(q / 2)
            sg = 1 if (par == 0 or x > 0) else -1
            return sg * r * exp(-ka * (abs(x) - 0.5))
        norm = max(abs(psi(0.002 * j)) for j in range(0, 501))
        s.linie(b, (-1.2, En), (1.2, En), farbe=fb[i], dicke=1.5, dash=DASH)
        xs = np.linspace(-1.2, 1.2, 240)
        s.daten(b, [(x, En + amp * psi(x) / norm) for x in xs], farbe=fb[i], dicke=4)
        t(s, b, f"E_{i + 1}", (1.36, En), farbe=fb[i])
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k3rampe():
    """Links scharfe und sanfte Stufe, rechts der Reflexionskoeffizient über der Anstiegsbreite."""
    s = Szene("gemb1/k3rampe")
    V0, E = 2.0, 3.0
    a = s.achsen((-2, 2, 1), (0, 3.6, 1), breite=2.75, hoehe=2.25, mitte=(-1.85, 0), xl=nm_achse(s), yl=ev_achse(s))
    s.daten(a, [(-2, 0), (0, 0), (0, 2), (2, 2)], farbe=GRAU, dicke=4, dash=DASH)
    s.kurve(a, "2/(1+exp(-4*x))", x=(-2, 2), farbe=BLAU, dicke=5)
    s.linie(a, (-2, E), (2, E), farbe=ROT, dicke=3)
    t(s, a, "E", (-1.7, 3.28), farbe=ROT)
    t(s, a, "V_0", (1.45, 2.3))
    s.linie(a, (-0.5, 0.0), (-0.5, 2.7), farbe=BLAU, dicke=1.5, dash=DOT)
    s.linie(a, (0.5, 0.0), (0.5, 2.7), farbe=BLAU, dicke=1.5, dash=DOT)
    s.linie(a, (-0.5, 2.55), (0.5, 2.55), farbe=BLAU, dicke=3)
    t(s, a, "d", (0.75, 2.62), farbe=BLAU)
    b = s.achsen((0, 2, 0.5), (1e-12, 1), breite=2.6, hoehe=2.25, mitte=(1.95, 0), xl=s.tr("d_nm", "d in nm", "d in nm", "d en nm", "d / nm"), yl="R",
                 ylog=True, yticks="1e-12;1e-8;1e-4;1")
    k1, k2 = k(E), k(E - V0)

    def R(dd):
        if dd == 0:
            return ((k1 - k2) / (k1 + k2)) ** 2
        aa = dd / 4
        return (sinh(pi * aa * (k1 - k2)) / sinh(pi * aa * (k1 + k2))) ** 2
    pts = [(0.01 * i, R(0.01 * i)) for i in range(0, 171)]
    s.daten(b, pts, farbe=BLAU, dicke=4)
    s.punkt(b, 0, R(0), farbe=ROT)
    t(s, b, s.tr("scharf", "scharfe Stufe: R = 0.072", "sharp step: R = 0.072", "escalón abrupto: R = 0.072", "陡峭势阶：R = 0.072"), (0.18, 0.25), a="left", farbe=ROT, g=22)
    s.speichern()


if __name__ == "__main__":
    k3stufe()
    k3oben()
    k3unten()
    k3barriere()
    k3tunnelT()
    k3prisma()
    k3box()
    k3rampe()
