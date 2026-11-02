"""ET1 Teil 6 (kap6_stufen.tex): Zweitore.

Aufruf: python tools/szenen/et1_teil6.py, danach python tools/szenen_ansehen.py out.png et1/k6tor ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/ET1/Arbeitshefte/rechnung_kap6.py.
"""
import sys
from math import atan2, degrees, hypot
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

BRAUN = "#a84a22"
HELLBLAU = "#eef4fc"
GR = 24           # Beschriftung in Schaltbildern


def bau(s, art, a, b, size=0.5, farbe=SCHWARZ, dicke=3):
    """Zweipol zwischen den Punkten a und b."""
    m = (0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1]))
    return s.bauteil(art, m, drehung=degrees(atan2(b[1] - a[1], b[0] - a[0])), laenge=hypot(b[0] - a[0], b[1] - a[1]), label="",
                     size=size, farbe=farbe, dicke=dicke)


def wid(s, a, b, size=0.5, farbe=SCHWARZ):
    return bau(s, "resistor", a, b, size=size, farbe=farbe)


def kl(s, x, y, name="", dx=0.0, dy=0.3, farbe=SCHWARZ):
    """Klemme als kleiner Ring, Name daneben."""
    s.kreis(None, x, y, 0.07, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1.0)
    if name:
        s.text(None, name, (x + dx, y + dy), groesse=GR, ausrichtung="center", farbe=farbe)


def kn(s, x, y, farbe=SCHWARZ, r=0.06):
    s.punkt(None, x, y, r=r, farbe=farbe)


def t(s, txt, p, a="center", farbe=SCHWARZ, g=GR):
    s.text(None, txt, p, groesse=g, ausrichtung=a, farbe=farbe)


def spfeil(s, x, y0, y1, txt="", seite=1, farbe=BLAU, dx=0.1):
    """Senkrechter Spannungspfeil mit Text rechts (seite=1) oder links (seite=-1)."""
    s.pfeil((x, y0), (x, y1), "", farbe=farbe, spitze=0.17, dicke=2.5)
    if txt:
        t(s, txt, (x + seite * dx, 0.5 * (y0 + y1)), "left" if seite > 0 else "right", farbe)


def ipfeil(s, a, b, txt="", p=None, farbe=ROT, ausr="center"):
    """Kurzer Strompfeil auf einer Leitung."""
    s.pfeil(a, b, "", farbe=farbe, spitze=0.17, dicke=3)
    if txt:
        t(s, txt, p, ausr, farbe)


def block(s, txt, x0, x1, y0, y1, farbe=BLAU, fuellung=HELLBLAU, g=GR):
    s.box(txt, (0.5 * (x0 + x1), 0.5 * (y0 + y1)), breite=x1 - x0, hoehe=y1 - y0, farbe=farbe, fuellung=fuellung, dicke=2.5, groesse=g)


# ------------------------------------------------------------------------------------------ Stufe 1
def k6tor():
    """Quelle, Zweitor, Last; rechts ein äußerer Zweig, der die Torbedingung bricht."""
    s = Szene("et1/k6tor")
    yo, yu = 0.75, -0.75
    # --- links
    xq, xk1, xb0, xb1, xk2, xl = -3.42, -2.7, -2.17, -1.05, -0.52, -0.05
    bau(s, "vsource", (xq, yo), (xq, yu), size=0.6)
    s.draht((xq, yo), (xk1, yo))
    s.draht((xq, yu), (xk1, yu))
    t(s, s.tr("quelle", "Quelle", "source", "fuente", "电源"), (xq + 0.1, yo + 0.3), "center", GRAU, 23)
    s.draht((xk1, yo), (xb0, yo))
    s.draht((xk1, yu), (xb0, yu))
    s.draht((xb1, yo), (xk2, yo))
    s.draht((xb1, yu), (xk2, yu))
    block(s, s.tr("zweitor", "Zweitor", "two-port", "cuadripolo", "二端口"), xb0, xb1, yu - 0.12, yo + 0.12)
    s.draht((xk2, yo), (xl, yo))
    s.draht((xk2, yu), (xl, yu))
    wid(s, (xl, yo), (xl, yu), size=0.46)
    t(s, s.tr("last", "Last", "load", "carga", "负载"), (xl + 0.06, yo + 0.3), "center", GRAU, 23)
    kl(s, xk1, yo, "1", dx=-0.1, dy=0.27)
    kl(s, xk1, yu, "1′", dx=-0.1, dy=-0.27)
    kl(s, xk2, yo, "2", dx=0.1, dy=0.27)
    kl(s, xk2, yu, "2′", dx=0.1, dy=-0.27)
    ipfeil(s, (xk1 + 0.1, yo), (xb0 - 0.04, yo), "I_1", (0.5 * (xk1 + xb0) + 0.07, yo + 0.27))
    ipfeil(s, (xb0 - 0.04, yu), (xk1 + 0.1, yu), "I_1", (0.5 * (xk1 + xb0) + 0.07, yu - 0.27))
    ipfeil(s, (xk2 - 0.1, yo), (xb1 + 0.04, yo), "I_2", (0.5 * (xk2 + xb1) - 0.07, yo + 0.27))
    ipfeil(s, (xb1 + 0.04, yu), (xk2 - 0.1, yu), "I_2", (0.5 * (xk2 + xb1) - 0.07, yu - 0.27))
    spfeil(s, xk1, yo - 0.2, yu + 0.2, "U_1", seite=-1, dx=0.08)
    spfeil(s, xk2, yo - 0.2, yu + 0.2, "U_2", seite=-1, dx=0.08)
    s.pfeil((xb0 + 0.2, -0.32), (xb1 - 0.2, -0.32), "", farbe=ORANGE, spitze=0.2, dicke=4)
    # --- rechts
    xa, xb, xc, xd = 0.85, 1.72, 2.55, 3.1
    block(s, s.tr("vierpol", "Vierpol", "four-pole", "4 polos", "四端网络"), xb, xc, yu - 0.12, yo + 0.12, farbe=GRAU, fuellung="#f2f2f2", g=23)
    s.draht((0.55, yo), (xb, yo))
    s.draht((0.55, yu), (xb, yu))
    s.draht((xc, yo), (xd + 0.22, yo))
    s.draht((xc, yu), (xd + 0.22, yu))
    kl(s, xa, yo, "1", dx=-0.05, dy=-0.27)
    kl(s, xa, yu, "1′", dx=-0.05, dy=0.27)
    kl(s, xd, yo, "2", dx=0.05, dy=-0.27)
    kl(s, xd, yu, "2′", dx=0.05, dy=0.27)
    yz = yo + 0.7
    kn(s, xa, yo, farbe=ROT)
    kn(s, xd, yo, farbe=ROT)
    s.draht((xa, yo), (xa, yz), farbe=ROT)
    wid(s, (xa, yz), (xd, yz), size=0.42, farbe=ROT)
    s.draht((xd, yz), (xd, yo), farbe=ROT)
    ipfeil(s, (xa + 0.1, yz), (xa + 0.48, yz), "I_x", (xa + 0.3, yz + 0.27))
    ipfeil(s, (xa + 0.16, yo), (xb - 0.04, yo), "I_1", (xa + 0.45, yo + 0.25), farbe=BLAU)
    ipfeil(s, (xb - 0.04, yu), (xa + 0.16, yu), "I_1 + I_x", (xa + 0.42, yu - 0.27), farbe=ROT)
    s.speichern()


def k6masse():
    """Erdunsymmetrisch (T mit Masseleitung) und erdsymmetrisch (Brücke)."""
    s = Szene("et1/k6masse")
    yo, yu = 0.75, -0.75
    xl, xm, xr = -3.2, -1.85, -0.5
    wid(s, (xl + 0.07, yo), (xm, yo), size=0.46)
    wid(s, (xm, yo), (xr - 0.07, yo), size=0.46)
    wid(s, (xm, yo), (xm, yu), size=0.46)
    s.draht((xl + 0.07, yu), (xr - 0.07, yu), farbe=ROT, dicke=4)
    kn(s, xm, yo)
    kn(s, xm, yu, farbe=ROT)
    kl(s, xl, yo, "1", dx=-0.2, dy=0.0)
    kl(s, xl, yu, "1′", dx=-0.22, dy=0.0)
    kl(s, xr, yo, "2", dx=0.2, dy=0.0)
    kl(s, xr, yu, "2′", dx=0.22, dy=0.0)
    t(s, "R_a = 15 Ω", (-2.52, yo + 0.3))
    t(s, "R_c = 20 Ω", (-1.18, yo + 0.3))
    t(s, "R_b = 20 Ω", (xm + 0.2, 0.0), "left")
    t(s, s.tr("masse", "Masseleitung", "ground line", "línea de masa", "地线"), (xm, yu - 0.3), farbe=ROT)
    # Brücke: oben Klemme 1, unten Klemme 1', links Klemme 2, rechts Klemme 2'
    x0, xc, xd = 0.62, 1.35, 3.15
    ya, yb = 0.98, -0.98
    s.draht((x0 + 0.07, ya), (xd, ya))
    s.draht((x0 + 0.07, yb), (xd, yb))
    wid(s, (xc, ya), (xc, 0), size=0.42)
    wid(s, (xc, 0), (xc, yb), size=0.42)
    wid(s, (xd, ya), (xd, 0), size=0.42)
    wid(s, (xd, 0), (xd, yb), size=0.42)
    kn(s, xc, ya)
    kn(s, xc, yb)
    kn(s, xd, 0)
    kn(s, xc, 0)
    kl(s, x0, ya, "1", dx=0.0, dy=0.27)
    kl(s, x0, yb, "1′", dx=0.0, dy=-0.27)
    kl(s, 1.95, 0, "2", dx=0.0, dy=-0.28)
    kl(s, 2.55, 0, "2′", dx=0.0, dy=-0.28)
    s.draht((xc, 0), (1.88, 0))
    s.draht((2.62, 0), (xd, 0))
    s.pfeil((2.0, 0.26), (2.5, 0.26), "", farbe=BLAU, spitze=0.16, dicke=2.5)
    t(s, "U_2", (2.25, 0.5), farbe=BLAU)
    spfeil(s, x0, ya - 0.2, yb + 0.2, "U_1", seite=1, dx=0.08)
    t(s, "R_x", (xc + 0.14, 0.52), "left")
    t(s, "R_y", (xc + 0.14, -0.52), "left")
    t(s, "R_y", (xd - 0.14, 0.52), "right")
    t(s, "R_x", (xd - 0.14, -0.52), "right")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k6zaehlpfeile():
    """Symmetrisch, Kettenpfeil, gemischt."""
    s = Szene("et1/k6zaehlpfeile")
    yo, yu = 0.55, -0.55

    def panel(x0, titel, art):
        xb0, xb1, xk, xr = x0 + 0.38, x0 + 1.02, x0 + 1.42, x0 + 1.86
        block(s, "", xb0, xb1, yu - 0.1, yo + 0.1)
        s.draht((x0, yo), (xb0, yo))
        s.draht((x0, yu), (xb0, yu))
        s.draht((xb1, yo), (xr, yo))
        s.draht((xb1, yu), (xr, yu))
        wid(s, (xr, yo), (xr, yu), size=0.4)
        kl(s, x0, yo)
        kl(s, x0, yu)
        kl(s, xk, yo)
        kl(s, xk, yu)
        ipfeil(s, (x0 + 0.09, yo), (xb0 - 0.02, yo), "I_1", (x0 + 0.2, yo + 0.27))
        spfeil(s, x0, yo - 0.18, yu + 0.18, "U_1", seite=-1, dx=0.08)
        spfeil(s, xk, yo - 0.18, yu + 0.18, "U_2", seite=-1, dx=0.07)
        if art == "sym":
            ipfeil(s, (xk - 0.08, yo), (xb1 + 0.03, yo), "I_2", (0.5 * (xk + xb1), yo + 0.27))
        else:
            ipfeil(s, (xk + 0.08, yo), (xr - 0.02, yo), "I_2" if art == "kette" else "−I_2", (0.5 * (xk + xr) + 0.02, yo + 0.27))
        t(s, titel, (x0 + 0.9, yu - 0.42))

    panel(-3.0, s.tr("sym", "symmetrisch", "symmetric", "simétrico", "对称"), "sym")
    panel(-0.65, s.tr("kette", "Kettenpfeil", "chain arrows", "en cadena", "链式方向"), "kette")
    panel(1.7, s.tr("gemischt", "gemischt", "mixed", "mixto", "混合"), "gemischt")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k6zesb():
    """Ersatzschaltbild der Z-Form, daneben Leerlauf an Tor 2."""
    s = Szene("et1/k6zesb")
    yo, ym, yu = 0.9, 0.0, -0.9

    def esb(x0, offen):
        xa, xb, x1 = x0 + 0.55, x0 + 1.62, x0 + 2.62
        grau = HELLGRAU
        c2 = grau if offen else SCHWARZ
        if offen:
            xq = x0 - 0.45
            bau(s, "isource", (xq, yu), (xq, yo), size=0.55)
            s.draht((xq, yo), (x0, yo))
            s.draht((xq, yu), (x0, yu))
            s.pfeil((xq, 0.72), (xq, 0.86), "", farbe=ROT, spitze=0.15, dicke=3)
            t(s, "I_q", (xq - 0.03, yo + 0.26), "center", ROT)
        s.draht((x0, yo), (xa, yo))
        s.draht((x0, yu), (xa, yu))
        wid(s, (xa, yo), (xa, ym), size=0.46)
        bau(s, "ccvs", (xa, ym), (xa, yu), size=0.55, farbe=c2)
        s.draht((xb, yo), (x1, yo), farbe=c2)
        s.draht((xb, yu), (x1, yu))
        wid(s, (xb, yo), (xb, ym), size=0.46, farbe=c2)
        bau(s, "ccvs", (xb, ym), (xb, yu), size=0.55)
        kl(s, x0, yo)
        kl(s, x0, yu)
        kl(s, x1, yo)
        kl(s, x1, yu)
        ipfeil(s, (x0 + 0.09, yo), (x0 + 0.42, yo), "I_1", (x0 + 0.27, yo + 0.26))
        t(s, "Z_{11}", (xa + 0.14, 0.45), "left")
        spfeil(s, xa + 0.24, -0.12, -0.78, "", farbe=grau if offen else BRAUN)
        t(s, "Z_{12} I_2" if not offen else "0 V", (xa + 0.3, -0.45), "left", grau if offen else BRAUN, 23)
        t(s, "Z_{22}", (xb + 0.14, 0.45), "left", c2)
        spfeil(s, xb + 0.24, -0.12, -0.78, "", farbe=BRAUN)
        t(s, "Z_{21} I_1", (xb + 0.3, -0.45), "left", BRAUN, 23)
        spfeil(s, x0, yo - 0.2, yu + 0.2, "U_1", seite=1, dx=0.07)
        ipfeil(s, (x1 - 0.09, yo), (x1 - 0.4, yo), "I_2 = 0" if offen else "I_2", (x1 - 0.27, yo + 0.26))
        spfeil(s, x1, yo - 0.2, yu + 0.2, "U_2", seite=1, dx=0.07)

    esb(-3.5, False)
    esb(0.45, True)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k6betrieb():
    """Z-Ersatzschaltbild mit Quelle und Last, alle Zahlen des Betriebs."""
    s = Szene("et1/k6betrieb")
    yo, ym, yu = 0.9, 0.0, -0.9
    xq, xr, x0, xa, xb, x1, xl = -3.55, -2.75, -2.45, -1.2, 0.4, 1.6, 2.55
    bau(s, "vsource", (xq, yo), (xq, yu), size=0.6)
    wid(s, (xq, yo), (xr, yo), size=0.42)
    s.draht((xr, yo), (xa, yo))
    s.draht((xq, yu), (xa, yu))
    wid(s, (xa, yo), (xa, ym), size=0.46)
    bau(s, "ccvs", (xa, ym), (xa, yu), size=0.55)
    wid(s, (xb, yo), (xb, ym), size=0.46)
    bau(s, "ccvs", (xb, ym), (xb, yu), size=0.55)
    s.draht((xb, yo), (xl, yo))
    s.draht((xb, yu), (xl, yu))
    wid(s, (xl, yo), (xl, yu), size=0.46)
    kl(s, x0, yo)
    kl(s, x0, yu)
    kl(s, x1, yo)
    kl(s, x1, yu)
    t(s, "U_q", (xq + 0.3, 0.17), "left")
    t(s, "9 V", (xq + 0.3, -0.15), "left")
    t(s, "R_q = 5 Ω", (0.5 * (xq + xr), yo + 0.3))
    t(s, "U_1", (x0 + 0.13, 0.17), "left", BLAU)
    t(s, "7.75 V", (x0 + 0.13, -0.15), "left", BLAU)
    spfeil(s, x0, yo - 0.2, yu + 0.2, farbe=BLAU)
    ipfeil(s, (x0 + 0.1, yo), (x0 + 0.5, yo), "I_1 = 250 mA", (x0 + 0.62, yo + 0.3))
    t(s, "Z_{11}", (xa + 0.14, 0.62), "left")
    t(s, "35 Ω", (xa + 0.14, 0.28), "left")
    spfeil(s, xa + 0.24, -0.12, -0.78, "", farbe=BRAUN)
    t(s, "Z_{12} I_2", (xa + 0.36, -0.3), "left", BRAUN)
    t(s, "−1 V", (xa + 0.36, -0.62), "left", BRAUN)
    t(s, "Z_{22}", (xb + 0.14, 0.62), "left")
    t(s, "40 Ω", (xb + 0.14, 0.28), "left")
    spfeil(s, xb + 0.24, -0.12, -0.78, "", farbe=BRAUN)
    t(s, "Z_{21} I_1", (xb + 0.36, -0.3), "left", BRAUN)
    t(s, "5 V", (xb + 0.36, -0.62), "left", BRAUN)
    ipfeil(s, (x1 - 0.1, yo), (x1 - 0.5, yo), "I_2 = −50 mA", (x1 - 0.5, yo + 0.3))
    spfeil(s, x1, yo - 0.2, yu + 0.2, farbe=BLAU)
    t(s, "U_2", (x1 + 0.13, 0.17), "left", BLAU)
    t(s, "3 V", (x1 + 0.13, -0.15), "left", BLAU)
    t(s, "R_L", (xl + 0.16, 0.17), "left")
    t(s, "60 Ω", (xl + 0.16, -0.15), "left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k6yesb():
    """Ersatzschaltbild der Y-Form, daneben Kurzschluss an Tor 2."""
    s = Szene("et1/k6yesb")
    yo, yu = 0.85, -0.85

    def esb(x0, kurz):
        xa, xc, xd, xb, x1 = x0 + 0.42, x0 + 0.86, x0 + 1.76, x0 + 2.2, x0 + 2.58
        c1 = HELLGRAU if kurz else SCHWARZ
        if kurz:
            xq = x0 - 0.42
            bau(s, "vsource", (xq, yo), (xq, yu), size=0.55)
            s.draht((xq, yo), (x0, yo))
            s.draht((xq, yu), (x0, yu))
            t(s, "U_q", (xq, yo + 0.26), "center", ROT)
        s.draht((x0, yo), (xc, yo))
        s.draht((x0, yu), (xc, yu))
        s.draht((xd, yo), (x1, yo))
        s.draht((xd, yu), (x1, yu))
        wid(s, (xa, yo), (xa, yu), size=0.46)
        bau(s, "vccs", (xc, yo), (xc, yu), size=0.6, farbe=c1)
        bau(s, "vccs", (xd, yo), (xd, yu), size=0.6)
        wid(s, (xb, yo), (xb, yu), size=0.46, farbe=c1)
        kn(s, xa, yo)
        kn(s, xa, yu)
        kn(s, xb, yo)
        kn(s, xb, yu)
        kl(s, x0, yo)
        kl(s, x0, yu)
        kl(s, x1, yo)
        kl(s, x1, yu)
        ipfeil(s, (x0 + 0.09, yo), (x0 + 0.36, yo), "I_1", (x0 + 0.22, yo + 0.26))
        spfeil(s, x0, yo - 0.2, yu + 0.2, "U_1", seite=-1 if not kurz else 1, dx=0.07)
        t(s, "Y_{11}", (xa + 0.02, -0.62), "left", g=23)
        t(s, "Y_{12} U_2" if not kurz else "0", (xc + 0.2, 0.4), "left", c1 if kurz else BRAUN, 23)
        t(s, "Y_{21} U_1", (xd - 0.2, -0.4), "right", BRAUN, 23)
        t(s, "Y_{22}", (xb + 0.03, -0.62), "left", c1, 23)
        ipfeil(s, (x1 - 0.09, yo), (x1 - 0.33, yo), "I_2", (x1 - 0.2, yo + 0.26))
        if kurz:
            s.draht((x1, yo), (x1 + 0.3, yo), (x1 + 0.3, yu), (x1, yu), farbe=ROT, dicke=4)
            t(s, "U_2 = 0", (x1 - 0.05, yu - 0.27), "center", ROT)
        else:
            spfeil(s, x1, yo - 0.2, yu + 0.2, "U_2", seite=1, dx=0.07)

    esb(-3.25, False)
    esb(0.5, True)
    s.speichern()


def k6kennlinien():
    """Eingangs-, Übertragungs- und Ausgangskennlinie des T-Zweitors."""
    s = Szene("et1/k6kennlinien")
    s.welt()
    bx, hy = 1.25, 1.55
    ux = s.tr("u1v", "U_1 in V", "U_1 in V", "U_1 en V", "U_1 / V")
    uy = s.tr("u2v", "U_2 in V", "U_2 in V", "U_2 en V", "U_2 / V")
    i1 = s.tr("i1ma", "I_1 in mA", "I_1 in mA", "I_1 en mA", "I_1 / mA")
    i2 = s.tr("i2ma", "I_2 in mA", "I_2 in mA", "I_2 en mA", "I_2 / mA")
    g = 23

    def plot(mx, xl, yl, titel, f):
        a = s.achsen((0, 10, 5), (-200, 400, 200), breite=bx, hoehe=hy, mitte=(mx, 0), xl=xl, yl=yl, titel=titel, gitter=True, zahl=22, label=23)
        for w, c in ((0, BLAU), (5, GRUEN), (10, ROT)):
            s.kurve(a, f % w, x=(0, 10), farbe=c)
        return a

    def rechts(a, wert, y, farbe):
        s.text(a, wert, (10.5, y), groesse=g, farbe=farbe)

    a = plot(-2.42, ux, i1, s.tr("ein", "Eingang", "input", "entrada", "输入"), "40*x-20*%d")
    s.text(a, "U_2 = 0", (0.4, 330), groesse=g, farbe=BLAU)
    rechts(a, "5 V", 300, GRUEN)
    rechts(a, "10 V", 200, ROT)
    b = plot(-0.05, ux, i2, s.tr("ueb", "Übertragung", "transfer", "transferencia", "转移"), "-20*x+35*%d")
    s.text(b, "U_2 = 0", (0.4, -145), groesse=g, farbe=BLAU)
    rechts(b, "5 V", -25, GRUEN)
    rechts(b, "10 V", 150, ROT)
    c = plot(2.32, uy, i2, s.tr("aus", "Ausgang", "output", "salida", "输出"), "35*x-20*%d")
    s.text(c, "U_1 = 0", (0.4, 330), groesse=g, farbe=BLAU)
    rechts(c, "5 V", 250, GRUEN)
    rechts(c, "10 V", 150, ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k6tpi():
    """T-Schaltung und gleichwertige pi-Schaltung."""
    s = Szene("et1/k6tpi")
    yo, yu = 0.7, -0.7
    xl, xm, xr = -3.3, -2.0, -0.7
    wid(s, (xl + 0.07, yo), (xm, yo), size=0.46)
    wid(s, (xm, yo), (xr - 0.07, yo), size=0.46)
    wid(s, (xm, yo), (xm, yu), size=0.46)
    s.draht((xl + 0.07, yu), (xr - 0.07, yu))
    kn(s, xm, yo)
    kn(s, xm, yu)
    for x in (xl, xr):
        kl(s, x, yo)
        kl(s, x, yu)
    t(s, "15 Ω", (-2.65, yo + 0.3))
    t(s, "20 Ω", (-1.35, yo + 0.3))
    t(s, "20 Ω", (xm + 0.17, 0.0), "left")
    spfeil(s, xl, yo - 0.18, yu + 0.18, "U_1", seite=1, dx=0.08)
    spfeil(s, xr, yo - 0.18, yu + 0.18, "U_2", seite=-1, dx=0.08)
    t(s, "T", (xm, yu - 0.32))
    t(s, "=", (-0.1, 0.0), g=32)
    xl, xa, xb, xr = 0.5, 1.15, 2.6, 3.25
    s.draht((xl + 0.07, yo), (xa, yo))
    s.draht((xb, yo), (xr - 0.07, yo))
    s.draht((xl + 0.07, yu), (xr - 0.07, yu))
    wid(s, (xa, yo), (xb, yo), size=0.46)
    wid(s, (xa, yo), (xa, yu), size=0.46)
    wid(s, (xb, yo), (xb, yu), size=0.46)
    for x in (xa, xb):
        kn(s, x, yo)
        kn(s, x, yu)
    for x in (xl, xr):
        kl(s, x, yo)
        kl(s, x, yu)
    t(s, "50 Ω", (0.5 * (xa + xb), yo + 0.3))
    t(s, "50 Ω", (xa + 0.17, 0.0), "left")
    t(s, "66.7 Ω", (xb - 0.17, 0.0), "right")
    spfeil(s, xl, yo - 0.18, yu + 0.18, "U_1", seite=1, dx=0.08)
    spfeil(s, xr, yo - 0.18, yu + 0.18, "U_2", seite=-1, dx=0.08)
    t(s, "π", (0.5 * (xa + xb), yu - 0.32))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k6hesb():
    """Ersatzschaltbild der H-Form, daneben das Verstärkermodell."""
    s = Szene("et1/k6hesb")
    yo, ym, yu = 0.9, 0.0, -0.9
    # links
    x0, xa, xb, xc, x1 = -3.3, -2.8, -1.72, -1.22, -0.88
    s.draht((x0, yo), (xa, yo))
    s.draht((x0, yu), (xa, yu))
    wid(s, (xa, yo), (xa, ym), size=0.46)
    bau(s, "vcvs", (xa, ym), (xa, yu), size=0.55)
    bau(s, "cccs", (xb, yo), (xb, yu), size=0.6)
    wid(s, (xc, yo), (xc, yu), size=0.46)
    s.draht((xb, yo), (x1, yo))
    s.draht((xb, yu), (x1, yu))
    kn(s, xc, yo)
    kn(s, xc, yu)
    for x in (x0, x1):
        kl(s, x, yo)
        kl(s, x, yu)
    ipfeil(s, (x0 + 0.09, yo), (x0 + 0.42, yo), "I_1", (x0 + 0.26, yo + 0.26))
    ipfeil(s, (x1 - 0.09, yo), (x1 - 0.31, yo), "I_2", (x1 - 0.2, yo + 0.26))
    spfeil(s, x0, yo - 0.2, yu + 0.2, "U_1", seite=-1, dx=0.07)
    spfeil(s, x1, yo - 0.2, yu + 0.2, "U_2", seite=1, dx=0.07)
    t(s, "H_{11}", (xa - 0.14, 0.45), "right")
    spfeil(s, xa + 0.24, -0.12, -0.78, "", farbe=BRAUN)
    t(s, "H_{12} U_2", (xa + 0.3, -0.45), "left", BRAUN, 23)
    t(s, "H_{21} I_1", (xb - 0.2, 0.42), "right", BRAUN, 23)
    t(s, "H_{22}", (xc + 0.02, -0.64), "left", g=23)
    # rechts: Verstärker
    xq, xr1, xb, xr2, x1, xl = 0.5, 1.0, 1.58, 2.08, 2.72, 3.18
    s.draht((xq, yo), (xr1, yo))
    s.draht((xq, yu), (xr1, yu))
    wid(s, (xr1, yo), (xr1, yu), size=0.46)
    bau(s, "cccs", (xb, yo), (xb, yu), size=0.6)
    wid(s, (xr2, yo), (xr2, yu), size=0.46)
    wid(s, (xl, yo), (xl, yu), size=0.46)
    s.draht((xb, yo), (xl, yo))
    s.draht((xb, yu), (xl, yu))
    kn(s, xr2, yo)
    kn(s, xr2, yu)
    for x in (xq, x1):
        kl(s, x, yo)
        kl(s, x, yu)
    ipfeil(s, (xq + 0.09, yo), (xq + 0.42, yo), "10 µA", (xq + 0.2, yo + 0.26))
    t(s, "20 mV", (xq - 0.08, 0.0), "right", BLAU)
    spfeil(s, xq, yo - 0.2, yu + 0.2, "", seite=1)
    t(s, "2 kΩ", (xr1, yu - 0.26), "center")
    t(s, "100 I_1", (xb + 0.04, yo + 0.26), "center", BRAUN)
    t(s, "20 kΩ", (xr2 + 0.02, yu - 0.26), "center")
    ipfeil(s, (x1 + 0.42, yo), (x1 + 0.09, yo), "", None)
    t(s, "0.8 mA", (x1 + 0.1, yo + 0.26), "center", ROT)
    t(s, "5 kΩ", (xl + 0.04, yu - 0.26), "center")
    s.pfeil((x1, yo - 0.2), (x1, yu + 0.2), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    t(s, "−4 V", (x1 - 0.08, 0.0), "right", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k6kette():
    """Oben: zwei Zweitore in Kette. Unten: das T als Kette aus drei Bausteinen."""
    s = Szene("et1/k6kette")
    yo, yu = 1.4, 0.6
    xk0, b0, b1, xm, b2, b3, xk1 = -2.9, -2.3, -1.15, 0.0, 1.15, 2.3, 2.9
    block(s, "A′", b0, b1, yu - 0.1, yo + 0.1)
    block(s, "A″", b2, b3, yu - 0.1, yo + 0.1)
    for a, c in ((xk0, b0), (b1, b2), (b3, xk1)):
        s.draht((a, yo), (c, yo))
        s.draht((a, yu), (c, yu))
    for x in (xk0, xm, xk1):
        kl(s, x, yo)
        kl(s, x, yu)
    ipfeil(s, (xk0 + 0.1, yo), (b0 - 0.04, yo), "I_1", (xk0 + 0.3, yo + 0.27))
    spfeil(s, xk0, yo - 0.2, yu + 0.2, "U_1", seite=-1, dx=0.08)
    ipfeil(s, (xm - 0.5, yo), (xm + 0.5, yo), "−I_2′ = I_1″", (xm, yo + 0.3))
    s.pfeil((xm, yo - 0.18), (xm, yu + 0.18), "", farbe=BLAU, spitze=0.17, dicke=2.5)
    t(s, "U_2′", (xm - 0.09, 0.5 * (yo + yu)), "right", BLAU)
    t(s, "= U_1″", (xm + 0.09, 0.5 * (yo + yu)), "left", BLAU)
    ipfeil(s, (b3 + 0.04, yo), (xk1 - 0.1, yo), "−I_2″", (xk1 - 0.25, yo + 0.27))
    spfeil(s, xk1, yo - 0.2, yu + 0.2, "U_2″", seite=1, dx=0.08)
    # unten: Elementarzweitore
    yo, yu = -0.32, -0.98

    def rahmen(a, b, txt):
        s.box("", (0.5 * (a + b), 0.5 * (yo + yu)), breite=b - a, hoehe=yo - yu + 0.42, farbe=GRAU, fuellung="#ffffff", deckung=0.0, dicke=2, dash=DASH)
        t(s, txt, (0.5 * (a + b), yu - 0.45), "center", BLAU)

    rahmen(-2.6, -1.1, "A_R(15 Ω)")
    rahmen(-0.75, 0.75, "A_G(50 mS)")
    rahmen(1.1, 2.6, "A_R(20 Ω)")
    wid(s, (-2.3, yo), (-1.4, yo), size=0.42)
    s.draht((-2.95, yo), (-2.3, yo))
    s.draht((-1.4, yo), (1.4, yo))
    wid(s, (0.0, yo), (0.0, yu), size=0.38)
    wid(s, (1.4, yo), (2.3, yo), size=0.42)
    s.draht((2.3, yo), (2.95, yo))
    s.draht((-2.95, yu), (2.95, yu))
    kn(s, 0.0, yo)
    kn(s, 0.0, yu)
    for x in (-2.95, 2.95):
        kl(s, x, yo)
        kl(s, x, yu)
    t(s, "R_a", (-1.85, yo - 0.27), g=23)
    t(s, "G_b", (0.14, 0.5 * (yo + yu)), "left", g=23)
    t(s, "R_c", (1.85, yo - 0.27), g=23)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k6zusammen():
    """Reihe-Reihe, parallel-parallel, Reihe-parallel."""
    s = Szene("et1/k6zusammen")
    w, h = 0.8, 0.6
    yb1, yb2 = 0.6, -0.6
    d = 0.16                                         # halber Pinabstand

    def panel(cx, links, rechts, a, b, titel):
        x0, x1 = cx - w / 2, cx + w / 2
        block(s, a, x0, x1, yb1 - h / 2, yb1 + h / 2, g=23)
        block(s, b, x0, x1, yb2 - h / 2, yb2 + h / 2, g=23)

        def seite(xbox, sgn, art):
            xk = xbox + sgn * 0.6
            xa, xc = xbox + sgn * 0.2, xbox + sgn * 0.38
            yt, yu = yb1 + d, yb2 - d
            if art == "r":
                s.draht((xk, yt), (xbox, yt))
                s.draht((xbox, yb1 - d), (xa, yb1 - d), (xa, yb2 + d), (xbox, yb2 + d))
                s.draht((xbox, yu), (xk, yu))
            else:
                s.draht((xk, yt), (xbox, yt))
                s.draht((xc, yt), (xc, yb2 + d), (xbox, yb2 + d))
                kn(s, xc, yt)
                s.draht((xbox, yb1 - d), (xa, yb1 - d), (xa, yu))
                s.draht((xbox, yu), (xk, yu))
                kn(s, xa, yu)
            kl(s, xk, yt)
            kl(s, xk, yu)
            return xk, yt, yu

        xk, yt, yu = seite(x0, -1, links)
        spfeil(s, xk, yt - 0.18, yu + 0.18, "", farbe=BLAU)
        xk, yt, yu = seite(x1, 1, rechts)
        spfeil(s, xk, yt - 0.18, yu + 0.18, "", farbe=BLAU)
        t(s, titel, (cx, yb2 - h / 2 - 0.38), "center", SCHWARZ, 23)

    panel(-2.4, "r", "r", "Z′", "Z″", s.tr("rr", "Reihe, Reihe", "series, series", "serie, serie", "串联，串联"))
    panel(0.0, "p", "p", "Y′", "Y″", s.tr("pp", "parallel, parallel", "parallel, parallel", "paralelo, paralelo", "并联，并联"))
    panel(2.4, "r", "p", "H′", "H″", s.tr("rp", "Reihe, parallel", "series, parallel", "serie, paralelo", "串联，并联"))
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def k6umkehr():
    """Vorwärts und rückwärts: T-Zweitor und Verstärkermodell."""
    s = Szene("et1/k6umkehr")

    def zeile(cx, y, txt, links, rechts, vor):
        b0, b1 = cx - 0.5, cx + 0.5
        block(s, txt, b0, b1, y - 0.32, y + 0.32, g=23)
        for sgn, xb in ((-1, b0), (1, b1)):
            s.draht((xb, y + 0.18), (xb + sgn * 0.35, y + 0.18))
            s.draht((xb, y - 0.18), (xb + sgn * 0.35, y - 0.18))
            kl(s, xb + sgn * 0.38, y + 0.18)
            kl(s, xb + sgn * 0.38, y - 0.18)
        if vor:
            ipfeil(s, (b0 - 0.3, y + 0.18), (b0 - 0.03, y + 0.18))
            t(s, links, (b0 - 0.5, y), "right", ROT)
            s.pfeil((b1 + 0.38, y + 0.08), (b1 + 0.38, y - 0.08), "", farbe=BLAU, spitze=0.13, dicke=2)
            t(s, rechts, (b1 + 0.5, y), "left", BLAU)
        else:
            ipfeil(s, (b1 + 0.3, y + 0.18), (b1 + 0.03, y + 0.18))
            t(s, links, (b1 + 0.5, y), "left", ROT)
            s.pfeil((b0 - 0.38, y + 0.08), (b0 - 0.38, y - 0.08), "", farbe=BLAU, spitze=0.13, dicke=2)
            t(s, rechts, (b0 - 0.5, y), "right", BLAU)

    tz = s.tr("tz", "T-Zweitor", "T two-port", "cuadripolo T", "T 形网络")
    vs = s.tr("vs", "Verstärker", "amplifier", "amplificador", "放大器")
    t(s, tz, (-1.85, 1.0))
    t(s, vs, (1.85, 1.0))
    zeile(-1.85, 0.45, "T", "100 mA", "2 V", True)
    zeile(-1.85, -0.45, "T", "100 mA", "2 V", False)
    zeile(1.85, 0.45, "V", "1 µA", "−2 V", True)
    zeile(1.85, -0.45, "V", "1 µA", "0 V", False)
    s.speichern()


ALLE = (k6tor, k6masse, k6zaehlpfeile, k6zesb, k6betrieb, k6yesb, k6kennlinien, k6tpi, k6hesb, k6kette, k6zusammen, k6umkehr)

if __name__ == "__main__":
    for f in ALLE:
        f()
    print(len(ALLE), "Szenen")
