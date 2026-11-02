"""GEMB 1, Teil 4 (kap4_stufen.tex): Atome und Orbitale.

Aufruf: python tools/szenen/gemb1_teil4.py, danach python tools/szenen_ansehen.py out.png gemb1/k4coulomb ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/GEMB/Arbeitshefte/rechnung_kap4.py.
"""
import sys
from math import cos, pi, sin, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
C_EVNM = 1.44                                # e^2/(4 pi eps0) in eV nm
E_N = {1: -13.606, 2: -3.401, 3: -1.512}     # Energien des Wasserstoffatoms in eV
FARBE_L = {0: BLAU, 1: ROT, 2: GRUEN, 3: ORANGE}
HELL_L = {0: "#dceafa", 1: "#f6dede", 2: "#ddf0e4", 3: "#fbe6dc"}


def viel(s, on, ecken, farbe=BLAU, deckung=0.35, rand=2.5):
    return s._add("Polygon", {"vertices": [[x, y, 0] for x, y in ecken], "color": farbe, "fill_color": farbe, "fill_opacity": deckung,
                              "stroke_width": rand}, on)


# ------------------------------------------------------------------------------------------ Stufe 1
def k4coulomb():
    """Coulomb-Trichter im Schnitt durch den Kern mit den drei tiefsten Energien."""
    s = Szene("gemb1/k4coulomb")
    xl = s.tr("x_nm", "x in nm (Schnitt durch den Kern)", "x in nm (section through the nucleus)", "x en nm (corte por el núcleo)", "x / nm（过核截面）")
    yl = s.tr("e_ev", "Energie in eV", "energy in eV", "energía en eV", "能量 / eV")
    a = s.achsen((-1.2, 1.2, 0.4), (-16, 3, 4), breite=6.3, hoehe=3.4, mitte=(0.15, 0.0), xl=xl, yl=yl, yticks="-16;-12;-8;-4;0")
    s.band(a, -1.2, 1.2, 0, 3, farbe=GRAU, deckung=0.16)
    s.text(a, s.tr("frei", "E > 0: frei, jede Energie möglich", "E > 0: free, any energy possible", "E > 0: libre, cualquier energía", "E > 0：自由，任意能量"), (0, 1.5), ausrichtung="center", groesse=24)
    s.linie(a, (-1.2, 0), (1.2, 0), farbe=GRAU, dicke=2)
    s.kurve(a, "-1.44/abs(x)", x=(-1.2, -0.09), farbe=BLAU)
    s.kurve(a, "-1.44/abs(x)", x=(0.09, 1.2), farbe=BLAU)
    s.text(a, "V(x)", (-0.82, -3.9), farbe=BLAU, ausrichtung="center")
    for n, e in E_N.items():
        ru = C_EVNM / abs(e)
        s.linie(a, (-ru, e), (ru, e), farbe=ROT, dicke=4)
        s.punkt(a, ru, e, farbe=ROT, r=0.05)
        s.punkt(a, -ru, e, farbe=ROT, r=0.05)
    s.text(a, "E_1 = −13.6 eV", (0.16, -13.1), farbe=ROT, groesse=24)
    s.text(a, "E_2 = −3.4 eV", (0.47, -4.3), farbe=ROT, groesse=24)
    s.text(a, "E_3 = −1.5 eV", (-0.05, -0.75), farbe=ROT, groesse=24, ausrichtung="center")
    s.punkt(a, 0, -15.3, farbe=SCHWARZ, r=0.11)
    s.text(a, "+", (0, -15.32), farbe="#ffffff", ausrichtung="center", groesse=24)
    s.text(a, s.tr("kern", "Kern", "nucleus", "núcleo", "原子核"), (0.1, -15.3), groesse=24)
    s.text(a, s.tr("verb", "klassisch verboten", "classically forbidden", "clásicamente prohibido", "经典禁区"), (0.72, -8.3), ausrichtung="center", groesse=24, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k4radial():
    """Dichte am Ort und Dichte je Radius im Grundzustand."""
    s = Szene("gemb1/k4radial")
    s.welt()
    x = s.tr("r_r1", "r / r_1", "r / r_1", "r / r_1", "r / r_1")
    a = s.achsen((0, 5, 1), (0, 1, 0.5), breite=2.6, hoehe=2.0, mitte=(-1.72, 0.0), xl=x, yl="π r_1^3 |ψ_1|^2",
                 titel=s.tr("t1", "Dichte an einem Punkt", "density at one point", "densidad en un punto", "某点处的密度"))
    s.kurve(a, "exp(-2*x)", farbe=BLAU)
    b = s.achsen((0, 5, 1), (0, 0.6, 0.2), breite=2.6, hoehe=2.0, mitte=(2.0, 0.0), xl=x, yl="r_1 · 4π r^2 |ψ_1|^2",
                 titel=s.tr("t2", "Dichte je Radius", "density per radius", "densidad por radio", "按半径的密度"))
    s.flaeche(b, "4*x*x*exp(-2*x)", 0, 1, farbe=BLAU, deckung=0.2)
    s.kurve(b, "4*x*x*exp(-2*x)", farbe=BLAU)
    s.linie(b, (1, 0), (1, 0.5413), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(b, 1, 0.5413, farbe=ROT, r=0.07)
    s.text(b, s.tr("max", "Maximum bei r_1", "maximum at r_1", "máximo en r_1", "最大值在 r_1"), (1.3, 0.54), farbe=ROT, groesse=24)
    s.text(b, "32 %", (0.6, 0.085), ausrichtung="center", groesse=KLEIN, farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k4zaehlen():
    """Alle Orbitale bis n = 4 als Striche: gleiche Zeile, gleiche Energie."""
    s = Szene("gemb1/k4zaehlen")
    ys = {1: -1.3, 2: -0.3, 3: 0.42, 4: 1.0}
    xs = {0: -1.68, 1: -0.96, 2: 0.2, 3: 1.88}
    d = 0.24
    for l, name in enumerate("spdf"):
        s.text(None, "%s (ℓ = %d)" % (name, l), (xs[l], 1.62), ausrichtung="center", groesse=24, farbe=FARBE_L[l])
    wert = {1: "−13.6 eV", 2: "−3.40 eV", 3: "−1.51 eV", 4: "−0.85 eV"}
    s.text(None, s.tr("zeile", "n, Energie", "n, energy", "n, energía", "n，能量"), (-3.42, 1.62), groesse=24)
    s.text(None, "n^2", (3.28, 1.62), ausrichtung="center", groesse=24)
    for n in range(1, 5):
        s.text(None, "n = %d:  %s" % (n, wert[n]), (-3.42, ys[n]), groesse=24)
        s.linie(None, (-1.95, ys[n]), (3.0, ys[n]), farbe=HELLGRAU, dicke=1.5, dash=DOT)
        for l in range(n):
            k = 2 * l + 1
            for i in range(k):
                x = xs[l] + (i - (k - 1) / 2) * d
                s.linie(None, (x - 0.095, ys[n]), (x + 0.095, ys[n]), farbe=FARBE_L[l], dicke=6)
        s.text(None, str(n * n), (3.28, ys[n]), ausrichtung="center", groesse=24)
    s.pfeil((-3.52, -1.55), (-3.52, 1.3), "", spitze=0.17, dicke=2.5, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def keulen(f, n=240):
    """Polardiagramm von |f| in einer Ebene; zerlegt in Stücke gleichen Vorzeichens: [(vorzeichen, [(h, v)])]. t von der v-Achse aus."""
    werte = [(2 * pi * i / n, f(2 * pi * i / n)) for i in range(n)]
    start = next((i for i in range(n) if werte[i][1] * werte[i - 1][1] < 0), 0)
    werte = werte[start:] + werte[:start]
    out, cur, sg = [], [], None
    for t, w in werte:
        vz = 1 if w >= 0 else -1
        if sg is None or vz == sg:
            cur.append((t, w))
        else:
            out.append((sg, cur))
            cur = [(t, w)]
        sg = vz
    out.append((sg, cur))
    return out


def orbital(s, x0, y0, f, name, h, v, r=0.54):
    """Ein Teilbild: Achsenkreuz h (waagerecht), v (senkrecht), Keulen von f."""
    m = max(abs(f(2 * pi * i / 360)) for i in range(360))
    for sg, st in keulen(f):
        pk = [(x0 + r * abs(w) / m * sin(t), y0 + r * abs(w) / m * cos(t)) for t, w in st]
        pk = pk + [(x0, y0)] if len(st) < 240 else pk
        viel(s, None, pk, farbe=BLAU if sg > 0 else ROT, deckung=0.4, rand=2)
    q = r + 0.1
    s.pfeil((x0 - q, y0), (x0 + q, y0), "", spitze=0.1, dicke=1.5, farbe=GRAU)
    s.pfeil((x0, y0 - q), (x0, y0 + q), "", spitze=0.1, dicke=1.5, farbe=GRAU)
    s.text(None, h, (x0 + q - 0.03, y0 + 0.13), groesse=KLEIN, ausrichtung="center", farbe=GRAU)
    s.text(None, v, (x0 + 0.13, y0 + q - 0.05), groesse=KLEIN, ausrichtung="center", farbe=GRAU)
    s.text(None, name, (x0, y0 - q - 0.2), groesse=26, ausrichtung="center")


def k4formen():
    """Winkelanteile der s-, p- und d-Orbitale in einer Schnittebene."""
    s = Szene("gemb1/k4formen")
    y1, y2 = 1.15, -0.95
    # t ist der Winkel zur senkrechten Achse der Schnittebene
    orbital(s, -2.55, y1, lambda t: 1.0, "s", "x", "z")
    orbital(s, -0.85, y1, lambda t: cos(t), "p_z", "x", "z")
    orbital(s, 0.85, y1, lambda t: sin(t), "p_x", "x", "z")
    orbital(s, 2.55, y1, lambda t: sin(t), "p_y", "y", "z")
    dx = 1.4
    orbital(s, -2 * dx, y2, lambda t: 3 * cos(t)**2 - 1, "d_{z^2}", "x", "z")
    orbital(s, -dx, y2, lambda t: sin(t) * cos(t), "d_{xz}", "x", "z")
    orbital(s, 0, y2, lambda t: sin(t) * cos(t), "d_{yz}", "y", "z")
    orbital(s, dx, y2, lambda t: sin(t) * cos(t), "d_{xy}", "x", "y")
    orbital(s, 2 * dx, y2, lambda t: sin(t)**2 - cos(t)**2, "d_{x^2−y^2}", "x", "y")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k4austausch():
    """Zwei Elektronen in der Box aus Teil 2: Dichte für das zweite Elektron, wenn das erste bei 0,3 L sitzt."""
    s = Szene("gemb1/k4austausch")
    s.welt()
    x = s.tr("x2", "x_2 / L", "x_2 / L", "x_2 / L", "x_2 / L")
    a1, a2 = sin(pi * 0.3), sin(2 * pi * 0.3)
    fa = f"2*({a1:.6f}*sin(2*pi*x)-{a2:.6f}*sin(pi*x))*({a1:.6f}*sin(2*pi*x)-{a2:.6f}*sin(pi*x))"
    fs = f"2*({a1:.6f}*sin(2*pi*x)+{a2:.6f}*sin(pi*x))*({a1:.6f}*sin(2*pi*x)+{a2:.6f}*sin(pi*x))"
    a = s.achsen((0, 1, 0.2), (0, 6, 2), breite=2.6, hoehe=1.95, mitte=(-1.72, 0.0), xl=x, yl="L^2 |Φ|^2",
                 titel=s.tr("par", "Spins parallel", "parallel spins", "espines paralelos", "自旋平行"))
    s.kurve(a, fa, farbe=BLAU)
    s.linie(a, (0.3, 0), (0.3, 6), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(a, 0.3, 0, farbe=ROT, r=0.08)
    s.text(a, s.tr("null", "null bei x_2 = x_1", "zero at x_2 = x_1", "cero en x_2 = x_1", "在 x_2 = x_1 处为零"), (0.33, 5.45), farbe=ROT, groesse=24)
    b = s.achsen((0, 1, 0.2), (0, 6, 2), breite=2.6, hoehe=1.95, mitte=(2.0, 0.0), xl=x, yl="L^2 |Φ|^2",
                 titel=s.tr("anti", "Spins antiparallel", "antiparallel spins", "espines antiparalelos", "自旋反平行"))
    s.kurve(b, fs, farbe=GRUEN)
    s.linie(b, (0.3, 0), (0.3, 6), farbe=ROT, dicke=3, dash=DASH)
    s.punkt(b, 0.3, 4.736, farbe=ROT, r=0.07)
    s.text(b, s.tr("nn", "bei x_2 = x_1\\\\nicht null", "not zero\\\\at x_2 = x_1", "no es cero\\\\en x_2 = x_1", "在 x_2 = x_1\\\\处不为零"), (0.72, 5.0), ausrichtung="center", farbe=ROT, groesse=24)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def kaestchen(s, x, y, belegung, a=0.36, farbe=BLAU):
    """Ein Orbital als Kästchen; belegung z. B. "ud", "u", "" (u: Spin hoch, d: Spin runter)."""
    s.box("", (x, y), breite=a, hoehe=a, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0, dicke=2.5)
    if "u" in belegung:
        dx = -0.075 if len(belegung) == 2 else 0
        s.pfeil((x + dx, y - 0.14), (x + dx, y + 0.14), "", spitze=0.1, dicke=2.5, farbe=ROT)
    if "d" in belegung:
        s.pfeil((x + 0.075, y + 0.14), (x + 0.075, y - 0.14), "", spitze=0.1, dicke=2.5, farbe=BLAU)


def unterschale(s, x, y, name, belegungen, namen=None):
    d = 0.44
    s.text(None, name, (x - 0.33, y), groesse=24, ausrichtung="right")
    for i, b in enumerate(belegungen):
        kaestchen(s, x + i * d, y, b)
        if namen:
            s.text(None, namen[i], (x + i * d, y + 0.34), groesse=KLEIN, ausrichtung="center", farbe=GRAU)


def k4besetzung():
    """Besetzung von Kohlenstoff und Silizium, Energie wächst nach oben."""
    s = Szene("gemb1/k4besetzung")
    y = {"1s": -1.75, "2s": -1.1, "2p": -0.65, "3s": 0.2, "3p": 0.65}
    # Kohlenstoff
    x0 = -2.35
    s.text(None, s.tr("c", "Kohlenstoff, Z = 6", "carbon, Z = 6", "carbono, Z = 6", "碳，Z = 6"), (-1.75, 1.75), ausrichtung="center", groesse=26)
    s.text(None, "1s^2 2s^2 2p^2", (-1.75, 1.4), ausrichtung="center", groesse=26, farbe=BLAU)
    unterschale(s, x0, y["1s"], "1s", ["ud"])
    unterschale(s, x0, y["2s"], "2s", ["ud"])
    unterschale(s, x0 + 0.72, y["2p"], "2p", ["u", "u", ""], ["p_x", "p_y", "p_z"])
    # Silizium
    x1 = 1.2
    s.text(None, s.tr("si", "Silizium, Z = 14", "silicon, Z = 14", "silicio, Z = 14", "硅，Z = 14"), (1.95, 1.75), ausrichtung="center", groesse=26)
    s.text(None, "1s^2 2s^2 2p^6 3s^2 3p^2", (1.95, 1.4), ausrichtung="center", groesse=26, farbe=BLAU)
    unterschale(s, x1, y["1s"], "1s", ["ud"])
    unterschale(s, x1, y["2s"], "2s", ["ud"])
    unterschale(s, x1 + 0.72, y["2p"], "2p", ["ud", "ud", "ud"], ["p_x", "p_y", "p_z"])
    unterschale(s, x1, y["3s"], "3s", ["ud"])
    unterschale(s, x1 + 0.72, y["3p"], "3p", ["u", "u", ""], ["p_x", "p_y", "p_z"])
    s.pfeil((-3.45, -2.0), (-3.45, 1.15), "", spitze=0.17, dicke=2.5, farbe=GRAU)
    s.text(None, "E", (-3.27, 1.05), groesse=26, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
ZEILEN = ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He",
          "Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne",
          "Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar",
          "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
          "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
          "Cs", "Ba", "", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
          "Fr", "Ra", "", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
F_ZEILEN = (["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
            ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"])


def k4perioden():
    """Periodensystem, gefärbt nach dem Orbital, das sich gerade füllt."""
    s = Szene("gemb1/k4perioden")
    b, h = 0.378, 0.335
    x0, y0 = -3.3, 1.95
    for i, sym in enumerate(ZEILEN):
        if not sym:
            continue
        sp, ze = i % 18, i // 18
        blk = 0 if sp < 2 else (2 if sp < 12 else 1)
        if sym == "He":
            blk = 0
        rot = sym in ("C", "Si", "Ge")
        s.box(sym, (x0 + sp * b, y0 - ze * h), breite=b, hoehe=h, groesse=KLEIN, fuellung=HELL_L[blk], dicke=3.5 if rot else 1.2,
              farbe=ROT if rot else "#6a6a6a")
    for k, reihe in enumerate(F_ZEILEN):
        for i, sym in enumerate(reihe):
            s.box(sym, (x0 + (2.5 + i) * b, y0 - (7.45 + k) * h), breite=b, hoehe=h, groesse=KLEIN, fuellung=HELL_L[3], dicke=1.2, farbe="#6a6a6a")
    for ze in range(7):
        s.text(None, str(ze + 1), (x0 - 0.32, y0 - ze * h), groesse=24, ausrichtung="center", farbe=GRAU)
    for sp, nr in ((0, "I"), (1, "II"), (12, "III"), (13, "IV"), (14, "V"), (15, "VI"), (16, "VII"), (17, "VIII")):
        yy = y0 + 0.3 if sp in (0, 17) else (y0 - 0.03 if sp == 1 else y0 - 0.03)
        if sp == 1:
            yy = y0 - h + 0.3
        elif 12 <= sp <= 16:
            yy = y0 - h + 0.3
        s.text(None, nr, (x0 + sp * b, yy), groesse=KLEIN, ausrichtung="center", farbe=GRAU)
    # Legende in der Lücke
    xl, yl = x0 + 2.35 * b, y0 + 0.2
    zeilen = [(0, s.tr("bs", "s: Hauptgruppen I, II, dazu He", "s: main groups I, II, plus He", "s: grupos principales I, II y He", "s：主族 I、II，以及 He")),
              (1, s.tr("bp", "p: Hauptgruppen III bis VIII", "p: main groups III to VIII", "p: grupos principales III a VIII", "p：主族 III 至 VIII")),
              (2, s.tr("bd", "d: Nebengruppen", "d: transition groups", "d: grupos de transición", "d：副族")),
              (3, s.tr("bf", "f: innere Übergangsgruppen", "f: inner transition groups", "f: transición interna", "f：内过渡族"))]
    for k, (blk, txt) in enumerate(zeilen):
        yk = yl - k * 0.265
        s.box("", (xl, yk), breite=0.24, hoehe=0.2, fuellung=HELL_L[blk], dicke=1.2, farbe="#6a6a6a")
        s.text(None, txt, (xl + 0.2, yk), groesse=KLEIN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
IE = [("H", 13.598), ("He", 24.587), ("Li", 5.392), ("Be", 9.323), ("B", 8.298), ("C", 11.260), ("N", 14.534), ("O", 13.618), ("F", 17.423), ("Ne", 21.565),
      ("Na", 5.139), ("Mg", 7.646), ("Al", 5.986), ("Si", 8.152), ("P", 10.487), ("S", 10.360), ("Cl", 12.968), ("Ar", 15.760), ("K", 4.341), ("Ca", 6.113),
      ("Sc", 6.561), ("Ti", 6.828), ("V", 6.746), ("Cr", 6.767), ("Mn", 7.434), ("Fe", 7.902), ("Co", 7.881), ("Ni", 7.640), ("Cu", 7.726), ("Zn", 9.394),
      ("Ga", 5.999), ("Ge", 7.899), ("As", 9.789), ("Se", 9.752), ("Br", 11.814), ("Kr", 14.000)]


def k4ionisierung():
    """Erste Ionisierungsenergie über der Kernladungszahl."""
    s = Szene("gemb1/k4ionisierung")
    xl = s.tr("zz", "Kernladungszahl Z", "atomic number Z", "número atómico Z", "原子序数 Z")
    yl = s.tr("ie", "Ionisierungsenergie in eV", "ionization energy in eV", "energía de ionización en eV", "电离能 / eV")
    a = s.achsen((0, 37, 5), (0, 28, 5), breite=5.85, hoehe=2.6, mitte=(0.1, -0.1), xl=xl, titel=yl, yticks="0;5;10;15;20;25")
    for z in (2.5, 10.5, 18.5):
        s.linie(a, (z, 0), (z, 28), farbe=HELLGRAU, dicke=2, dash=DASH)
    pts = [(i + 1, w) for i, (_, w) in enumerate(IE)]
    s.daten(a, pts, farbe=GRAU, dicke=2.5)
    for i, (sym, w) in enumerate(IE):
        z = i + 1
        farbe = ROT if sym in ("He", "Ne", "Ar", "Kr") else (BLAU if sym in ("Li", "Na", "K") else SCHWARZ)
        s.punkt(a, z, w, farbe=farbe, r=0.075 if farbe != SCHWARZ else 0.05)
    for sym, z, w, dx, dy in (("He", 2, 24.59, 2.1, 0.8), ("Ne", 10, 21.57, 2.0, 1.2), ("Ar", 18, 15.76, 2.0, 1.2), ("Kr", 36, 14.0, 0.0, 2.1)):
        s.text(a, sym, (z + dx, w + dy), groesse=24, ausrichtung="center", farbe=ROT)
    for sym, z, w, dx, dy in (("Li", 3, 5.39, 0.0, -2.5), ("Na", 11, 5.14, 0.3, -2.5), ("K", 19, 4.34, 0.3, -2.5)):
        s.text(a, sym, (z + dx, w + dy), groesse=24, ausrichtung="center", farbe=BLAU)
    for sym, z, w, dx, dy in (("N", 7, 14.53, -1.2, 1.6), ("O", 8, 13.62, 1.3, -1.9), ("Si", 14, 8.15, 0.2, -2.5)):
        s.text(a, sym, (z + dx, w + dy), groesse=24, ausrichtung="center")
    for txt, z in (("1", 1.25), ("2", 6.5), ("3", 14.5), ("4", 27.5)):
        s.text(a, s.tr("per" + txt, "Periode " + txt, "period " + txt, "periodo " + txt, "第 " + txt + " 周期") if txt != "1" else txt, (z, 26.9), groesse=24, ausrichtung="center", farbe=GRAU)
    s.speichern()


ALLE = [k4coulomb, k4radial, k4zaehlen, k4formen, k4austausch, k4besetzung, k4perioden, k4ionisierung]

if __name__ == "__main__":
    for f in ALLE:
        f()
