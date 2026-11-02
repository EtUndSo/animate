"""ET1 Teil 1 (kap1_stufen.tex): Ladung, Feld und Potenzial.

Aufruf: python tools/szenen/et1_teil1.py, danach python tools/szenen_ansehen.py out.png et1/k1atom ... [--lang de]
Feldlinien: C:/Bücher/ET1/Arbeitshefte/daten/k1_*.dat aus rechnung_kap1.py.
"""
import sys
from math import cos, radians, sin
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET1\Arbeitshefte\daten")
HELLROT, HELLBLAU = "#f6dede", "#dceafa"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche


def linien(name):
    """Mehrere Feldlinien aus einer .dat-Datei; Linien sind durch '# neu' getrennt."""
    out, cur = [], []
    for z in (DAT / name).read_text(encoding="utf-8").splitlines():
        if z.startswith("#"):
            if cur:
                out.append(cur)
            cur = []
        else:
            x, y = z.split()
            cur.append((float(x), float(y)))
    if cur:
        out.append(cur)
    return out


def ladung(s, on, x, y, plus=True, r=0.17, groesse=26):
    """Kreis mit Vorzeichen: positiv rot, negativ blau."""
    f = ROT if plus else BLAU
    s.kreis(on, x, y, r, farbe=f, dicke=2.5, fuellung=HELLROT if plus else HELLBLAU, deckung=1.0)
    s.text(on, "+" if plus else "−", (x, y), groesse=groesse, ausrichtung="center", farbe=f)


def pfeil_auf_linie(s, on, ln, frac=0.5, farbe=BLAU, spitze=0.16, dicke=2, grenze=(2.8, 2.0)):
    """Kurzer Pfeil an der Stelle frac des sichtbaren Anfangsstücks der Linie, zeigt in Laufrichtung."""
    n = 0
    while n < len(ln) and abs(ln[n][0]) < grenze[0] and abs(ln[n][1]) < grenze[1]:
        n += 1
    ln = ln[:max(n, 3)]
    i = max(1, min(len(ln) - 2, int(frac * (len(ln) - 1))))
    a, b = ln[i - 1], ln[i + 1]
    s.pfeil(a, b, "", farbe=farbe, spitze=spitze, dicke=dicke, on=on)


def platte(s, x, y0, y1, breite=0.14):
    """Metallplatte im Schnitt, senkrecht."""
    s.box("", (x, 0.5 * (y0 + y1)), breite=breite, hoehe=y1 - y0, farbe=SCHWARZ, fuellung="#8c8c8c", deckung=1.0, dicke=1.5)


# ------------------------------------------------------------------------------------------ Von Grund auf
def k1atom():
    """Schema eines Atoms mit drei Protonen: neutral und mit einem Elektron weniger."""
    s = Szene("et1/k1atom")
    prot = s.tr("proton", "Proton", "proton", "protón", "质子")
    neut = s.tr("neutron", "Neutron", "neutron", "neutrón", "中子")
    elek = s.tr("elektron", "Elektron", "electron", "electrón", "电子")
    R = 0.95

    def atom(cx, cy, winkel):
        s.kreis(None, cx, cy, R, farbe=GRAU, dicke=2, dash=DASH)
        kern = [(-0.17, 0.12, True), (0.17, 0.12, False), (0.0, 0.3, True), (-0.17, -0.17, False), (0.17, -0.17, True), (0.0, -0.02, False)]
        for dx, dy, p in kern:
            if p:
                s.kreis(None, cx + dx, cy + dy, 0.13, farbe=ROT, dicke=2, fuellung=HELLROT, deckung=1.0)
                s.text(None, "+", (cx + dx, cy + dy), groesse=22, ausrichtung="center", farbe=ROT)
            else:
                s.kreis(None, cx + dx, cy + dy, 0.13, farbe=GRAU, dicke=2, fuellung="#e6e6e6", deckung=1.0)
        for w in winkel:
            ladung(s, None, cx + R * cos(radians(w)), cy + R * sin(radians(w)), plus=False, r=0.15, groesse=22)

    xl, xr, y = -1.6, 1.55, 0.0
    atom(xl, y, (90, 210, 330))
    atom(xr, y, (90, 210))
    ladung(s, None, 3.05, 1.0, plus=False, r=0.15, groesse=22)            # abgetrenntes Elektron
    s.pfeil((2.3, 0.42), (2.9, 0.88), "", farbe=BLAU, spitze=0.18)
    s.text(None, elek, (-3.5, 1.15), groesse=24, farbe=BLAU)
    s.pfeil((-2.72, 1.12), (-1.8, 0.98), "", farbe=BLAU, spitze=0.16, dicke=2)
    s.text(None, prot, (-3.5, -1.1), groesse=24, farbe=ROT)
    s.pfeil((-2.9, -1.0), (-1.53, -0.2), "", farbe=ROT, spitze=0.16, dicke=2)
    s.text(None, neut, (-0.8, 1.02), groesse=24, farbe=GRAU)
    s.pfeil((-0.5, 0.85), (-1.3, 0.17), "", farbe=GRAU, spitze=0.16, dicke=2)
    s.text(None, s.tr("neutral", "neutrales Atom", "neutral atom", "átomo neutro", "中性原子"), (xl, -1.42), ausrichtung="center")
    s.text(None, "Q = (3 − 3) e = 0", (xl, -1.8), ausrichtung="center")
    s.text(None, s.tr("ion", "positives Ion", "positive ion", "ion positivo", "正离子"), (xr, -1.42), ausrichtung="center")
    s.text(None, "Q = (3 − 2) e = +e", (xr, -1.8), ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 1
def k1wegarbeit():
    """Zwei Wege von A nach B im Schwerefeld: Treppe und Rampe (3-4-5-Dreieck)."""
    s = Szene("et1/k1wegarbeit")
    m = 0.36                                    # Einheiten je Meter
    x0, y0 = -2.6, -1.25

    def p(x, y):
        return (x0 + m * x, y0 + m * y)
    for k in range(0, 10):
        s.linie(None, p(k, 0), p(k, 7), farbe="#e4e4e4", dicke=1.5)
    for k in range(0, 8):
        s.linie(None, p(0, k), p(9, k), farbe="#e4e4e4", dicke=1.5)
    treppe = [(0, 0), (3, 0), (3, 2), (6, 2), (6, 5), (8, 5), (8, 6)]
    for a, b in zip(treppe, treppe[1:]):
        s.linie(None, p(*a), p(*b), farbe=ROT if a[0] == b[0] else GRUEN, dicke=5)
    s.linie(None, p(0, 0), p(8, 6), farbe=BLAU, dicke=4)
    s.punkt(None, *p(0, 0), r=0.09)
    s.punkt(None, *p(8, 6), r=0.09)
    s.text(None, "A", (p(0, 0)[0] - 0.14, p(0, 0)[1] - 0.26), ausrichtung="center")
    s.text(None, "B", (p(8, 6)[0] + 0.02, p(8, 6)[1] + 0.3), ausrichtung="center")
    s.text(None, "s = 10 m", p(2.9, 4.35), groesse=24, ausrichtung="center", farbe=BLAU)
    # Winkel zwischen Hubkraft (senkrecht) und Weg
    s.pfeil(p(0, 0), p(0, 3.4), "", farbe=SCHWARZ, spitze=0.2, dicke=3)
    s.text(None, "F", (p(0, 3.4)[0] - 0.22, p(0, 3.4)[1] - 0.05), ausrichtung="center")
    w0, w1 = radians(90), radians(36.87)
    rb = 0.7
    s.weg(None, f"{p(0, 0)[0]}+{rb}*cos(t)", f"{p(0, 0)[1]}+{rb}*sin(t)", w1, w0, farbe=SCHWARZ, dicke=2.5, n=31)
    s.text(None, "α", (p(0, 0)[0] + 0.28, p(0, 0)[1] + 0.9), groesse=24, ausrichtung="center")
    # rechts: Erklärung
    xr = 1.1
    s.linie(None, (xr, 1.15), (xr + 0.5, 1.15), farbe=ROT, dicke=5)
    s.text(None, s.tr("hoch", "hinauf: 6 m", "upward: 6 m", "hacia arriba: 6 m", "向上：6 m"), (xr + 0.62, 1.15), groesse=24, farbe=ROT)
    s.text(None, "W = 117.7 J", (xr + 0.62, 0.8), groesse=24, farbe=ROT)
    s.linie(None, (xr, 0.3), (xr + 0.5, 0.3), farbe=GRUEN, dicke=5)
    s.text(None, s.tr("waag", "waagerecht: 8 m", "horizontal: 8 m", "horizontal: 8 m", "水平：8 m"), (xr + 0.62, 0.3), groesse=24, farbe=GRUEN)
    s.text(None, "W = 0", (xr + 0.62, -0.05), groesse=24, farbe=GRUEN)
    s.linie(None, (xr, -0.55), (xr + 0.5, -0.55), farbe=BLAU, dicke=4)
    s.text(None, s.tr("rampe", "Rampe: F s cos α", "ramp: F s cos α", "rampa: F s cos α", "斜坡：F s cos α"), (xr + 0.62, -0.55), groesse=24, farbe=BLAU)
    s.text(None, "W = 117.7 J", (xr + 0.62, -0.9), groesse=24, farbe=BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k1reibung():
    """Reiben trennt Ladung, dann Kräfte zwischen den Stäben."""
    s = Szene("et1/k1reibung")

    def stab(cx, cy, plus, n=5, w=2.4):
        s.box("", (cx, cy), breite=w, hoehe=0.42, form="round", farbe=ROT if plus else BLAU, fuellung="#fdf1f1" if plus else "#eef4fc", dicke=2.5)
        for k in range(n):
            s.text(None, "+" if plus else "−", (cx + (k - (n - 1) / 2) * w / n, cy), groesse=24, ausrichtung="center", farbe=ROT if plus else BLAU)

    def tuch(cx, cy, plus, n=5, w=2.4):
        s.box("", (cx, cy), breite=w, hoehe=0.42, form="rect", farbe=GRAU, fuellung="#f0f0f0", dicke=2)
        for k in range(n):
            s.text(None, "+" if plus else "−", (cx + (k - (n - 1) / 2) * w / n, cy), groesse=24, ausrichtung="center", farbe=ROT if plus else BLAU)

    xl, xr = -1.85, 1.85
    s.text(None, s.tr("glas", "Glasstab", "glass rod", "varilla de vidrio", "玻璃棒"), (xl, 1.75), ausrichtung="center")
    stab(xl, 1.32, True)
    tuch(xl, 0.32, False)
    s.pfeil((xl, 1.08), (xl, 0.56), "", farbe=BLAU, spitze=0.2)
    s.text(None, "e^−", (xl + 0.15, 0.82), groesse=24, farbe=BLAU)
    s.text(None, s.tr("seide", "Seidentuch", "silk cloth", "paño de seda", "丝绸"), (xl, -0.1), ausrichtung="center", farbe=GRAU)
    s.text(None, s.tr("gummi", "Hartgummistab", "hard-rubber rod", "varilla de ebonita", "硬橡胶棒"), (xr, 1.75), ausrichtung="center")
    stab(xr, 1.32, False)
    tuch(xr, 0.32, True)
    s.pfeil((xr, 0.56), (xr, 1.08), "", farbe=BLAU, spitze=0.2)
    s.text(None, "e^−", (xr + 0.15, 0.82), groesse=24, farbe=BLAU)
    s.text(None, s.tr("fell", "Fell", "fur", "piel", "毛皮"), (xr, -0.1), ausrichtung="center", farbe=GRAU)
    # Kräfte, nebeneinander
    y, w = -0.75, 1.05
    stab(xl - 0.82, y, True, n=3, w=w)
    stab(xl + 0.82, y, False, n=3, w=w)
    s.pfeil((xl - 0.27, y), (xl - 0.05, y), "", farbe=ROT, spitze=0.18, dicke=3.5)
    s.pfeil((xl + 0.27, y), (xl + 0.05, y), "", farbe=ROT, spitze=0.18, dicke=3.5)
    s.text(None, s.tr("anziehen", "ziehen sich an", "attract", "se atraen", "相互吸引"), (xl, y - 0.42), ausrichtung="center", farbe=ROT)
    stab(xr - 0.62, y, False, n=3, w=w)
    stab(xr + 0.62, y, False, n=3, w=w)
    s.pfeil((xr - 1.17, y), (xr - 1.55, y), "", farbe=ROT, spitze=0.18, dicke=3.5)
    s.pfeil((xr + 1.17, y), (xr + 1.55, y), "", farbe=ROT, spitze=0.18, dicke=3.5)
    s.text(None, s.tr("abstossen", "stoßen sich ab", "repel", "se repelen", "相互排斥"), (xr, y - 0.42), ausrichtung="center", farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k1pendel():
    """Links die Kräfte an der Kugel am Faden (Kräfte maßstäblich), rechts F(r)."""
    s = Szene("et1/k1pendel")
    s.welt()
    wink = radians(11.5)
    xa0, ytop = -3.0, 1.3
    l = 1.6
    xa, ya = xa0 + l * sin(wink), ytop - l * cos(wink)
    s.linie(None, (xa0 - 0.6, ytop), (xa0 + 0.6, ytop), dicke=4)
    for k in range(7):
        s.linie(None, (xa0 - 0.6 + 0.2 * k, ytop), (xa0 - 0.45 + 0.2 * k, ytop + 0.15), dicke=2)
    s.linie(None, (xa0, ytop), (xa0, ytop - 1.95), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(None, (xa0, ytop), (xa, ya), dicke=2.5)
    kraft = 1.3 / 9.81                          # Einheiten je mN
    s.pfeil((xa, ya), (xa, ya - 9.81 * kraft), "", farbe=GRAU, spitze=0.2)
    s.text(None, "m g", (xa - 0.12, ya - 0.85), groesse=24, ausrichtung="right", farbe=GRAU)
    f0 = 10.01 * kraft
    s.pfeil((xa, ya), (xa - f0 * sin(wink), ya + f0 * cos(wink)), "", farbe=ORANGE, spitze=0.2, dicke=3)
    s.text(None, "F_0", (xa + 0.02, ya + 0.85), groesse=24, farbe=BRAUN)
    s.pfeil((xa, ya), (xa + 2.0 * kraft, ya), "", farbe=ROT, spitze=0.17, dicke=4)
    s.text(None, "F", (xa + 0.28, ya + 0.27), groesse=24, ausrichtung="center", farbe=ROT)
    xb = xa + 1.4
    ladung(s, None, xa, ya, plus=True, r=0.12, groesse=22)
    ladung(s, None, xb, ya, plus=False, r=0.12, groesse=22)
    s.linie(None, (xb, ya - 0.14), (xb, ya - 1.0), dicke=2.5)
    s.text(None, "Q_A", (xa - 0.2, ya + 0.14), groesse=24, ausrichtung="right")
    s.text(None, "Q_B", (xb + 0.18, ya + 0.14), groesse=24)
    s.pfeil((xa, ya - 1.5), (xb, ya - 1.5), "r", doppelt=True, spitze=0.16, dicke=2, groesse=24, label_seite="left")
    wb = 0.9
    s.weg(None, f"{xa0}+{wb}*sin(t)", f"{ytop}-{wb}*cos(t)", 0, wink, dicke=2.5, n=21)
    s.text(None, "α", (xa0 + 0.1, ytop - 1.16), groesse=24, ausrichtung="center")
    a = s.achsen((0, 10, 2), (0, 10, 2), breite=2.9, hoehe=2.0, mitte=(1.75, 0.1), xl=s.tr("r_in_cm", "r in cm", "r in cm", "r en cm", "r / cm"),
                 yl=s.tr("f_in_mn", "F in mN", "F in mN", "F en mN", "F / mN"), gitter=True)
    s.kurve(a, "17.975/x^2", x=(1.35, 10), farbe=BLAU)
    for r_, f in ((3, 1.997), (6, 0.499)):
        s.punkt(a, r_, f, farbe=ROT)
    s.text(a, "3 cm: 2.0 mN", (3.4, 2.9), groesse=23, farbe=ROT)
    s.text(a, "6 cm: 0.5 mN", (5.0, 1.35), groesse=23, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k1feldpfeile():
    """Feldvektoren um eine positive und eine negative Ladung, Länge proportional 1/r²."""
    s = Szene("et1/k1feldpfeile")
    for cx, plus in ((-1.75, True), (1.75, False)):
        for r0, wo in ((0.46, 0), (0.76, 22.5), (1.08, 0)):
            lg = 0.52 * (0.46 / r0) ** 2
            for k in range(8):
                w = radians(wo + 45 * k)
                x, y = cx + r0 * cos(w), r0 * sin(w)
                dx, dy = lg * cos(w), lg * sin(w)
                a, b = (x, y), (x + dx, y + dy)
                if plus:
                    s.pfeil(a, b, "", farbe=GRUEN, spitze=min(0.15, 0.7 * lg), dicke=2.5)
                else:
                    s.pfeil(b, a, "", farbe=GRUEN, spitze=min(0.15, 0.7 * lg), dicke=2.5)
        ladung(s, None, cx, 0, plus=plus, r=0.2, groesse=28)
    s.text(None, s.tr("pos", "positive Ladung", "positive charge", "carga positiva", "正电荷"), (-1.75, -1.47), groesse=24, ausrichtung="center")
    s.text(None, s.tr("neg", "negative Ladung", "negative charge", "carga negativa", "负电荷"), (1.75, -1.47), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k1feldlinien():
    """Vier Feldbilder aus rechnung_kap1.py: ungleichnamig, gleichnamig, Plattenpaar, Metallrohr zwischen Platten."""
    s = Szene("et1/k1feldlinien")
    B, H = 2.9, 2.13
    y1, y2 = 1.3, -1.32
    x1, x2 = -1.65, 1.65
    titel = (s.tr("t2", "ungleichnamige Ladungen", "opposite charges", "cargas opuestas", "异号电荷"),
             s.tr("t3", "gleichnamige Ladungen", "like charges", "cargas iguales", "同号电荷"),
             s.tr("t4", "Plattenpaar", "pair of plates", "par de placas", "平行极板"),
             s.tr("t5", "Metallrohr zwischen Platten", "metal tube between plates", "tubo metálico entre placas", "极板间的金属管"))
    ax = []
    for m_, t_ in zip(((x1, y1), (x2, y1), (x1, y2)), titel):
        a = s.achsen((-3, 3), (-2.2, 2.2), breite=B, hoehe=H, mitte=m_, unsichtbar=True)
        s.text(a, t_, (0, 2.58), groesse=24, ausrichtung="center")
        ax.append(a)
    a = ax[0]
    for ln in linien("k1_dipol.dat"):
        s.daten(a, duenn(ln, 1e-3), farbe=BLAU, dicke=2)
        pfeil_auf_linie(s, a, ln, 0.45, spitze=0.12)
    ladung(s, a, -1, 0, plus=True, r=0.11, groesse=22)
    ladung(s, a, 1, 0, plus=False, r=0.11, groesse=22)
    a = ax[1]
    for ln in linien("k1_gleich.dat"):
        s.daten(a, duenn(ln, 2e-3), farbe=BLAU, dicke=2)
        pfeil_auf_linie(s, a, ln, 0.35, spitze=0.12)
    ladung(s, a, -1, 0, plus=True, r=0.11, groesse=22)
    ladung(s, a, 1, 0, plus=True, r=0.11, groesse=22)
    a = ax[2]
    for ln in linien("k1_platten.dat"):
        s.daten(a, duenn(ln, 1e-3), farbe=BLAU, dicke=2)
        pfeil_auf_linie(s, a, ln, 0.5, spitze=0.12)
    for x, plus in ((-0.75, True), (0.75, False)):
        s.band(a, x - 0.06, x + 0.06, -1.5, 1.5, farbe="#6e6e6e", deckung=1.0)
        ladung(s, a, x, 0.0, plus=plus, r=0.12, groesse=22)
    # Metallrohr: Daten bis x = ±2,1
    a = s.achsen((-2.5, 2.5), (-2.1, 2.1), breite=2.9, hoehe=2.436, mitte=(x2, y2 - 0.12), unsichtbar=True)
    s.text(a, titel[3], (0, 2.36), groesse=24, ausrichtung="center")
    for ln in linien("k1_ring.dat"):
        s.daten(a, duenn(ln, 1e-3), farbe=BLAU, dicke=2)
        pfeil_auf_linie(s, a, ln, 0.5, spitze=0.12, grenze=(9, 9))
    s.kreis(a, 0, 0, 0.8, farbe=SCHWARZ, dicke=5)
    for w in (145, 180, 215):
        ladung(s, a, 0.64 * cos(radians(w)), 0.64 * sin(radians(w)), plus=False, r=0.125, groesse=22)
    for w in (35, 0, -35):
        ladung(s, a, 0.64 * cos(radians(w)), 0.64 * sin(radians(w)), plus=True, r=0.125, groesse=22)
    s.text(a, "E = 0", (0, 0), groesse=22, ausrichtung="center", farbe=ROT)
    for x, plus in ((-2.1, True), (2.1, False)):
        s.band(a, x - 0.09, x + 0.09, -2.05, 2.05, farbe="#6e6e6e", deckung=1.0)
        for y in (-1.3, 0, 1.3):
            s.text(a, "+" if plus else "−", (x + (-0.32 if plus else 0.32), y), groesse=24, ausrichtung="center", farbe=ROT if plus else BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k1feldarbeit():
    """Dreieck im Plattenfeld, maßstäblich. Probeladung +1 nC: 9 nJ, 0, -9 nJ."""
    s = Szene("et1/k1feldarbeit")
    mm = 0.6
    xa, xb = -2.1, -2.1 + 3 * mm
    yu, yo = -1.2, -1.2 + 4 * mm
    platte(s, xa - 0.08, yu - 0.3, yo + 0.25)
    platte(s, xb + 0.08, yu - 0.3, yo + 0.25)
    s.text(None, "A (+)", (xa - 0.08, yo + 0.5), ausrichtung="center", farbe=ROT)
    s.text(None, "B (−)", (xb + 0.08, yo + 0.5), ausrichtung="center", farbe=BLAU)
    for y in (-0.45, 0.75):
        s.pfeil((xa + 0.15, y), (xb - 0.15, y), "", farbe="#a9d3bb", spitze=0.2, dicke=2.5)
    s.text(None, "E", (xa + 0.2, 0.98), farbe=GRUEN)
    p1, p2, p3 = (xa, yu), (xb, yu), (xb, yo)
    s.pfeil(p1, p2, "", farbe=BLAU, spitze=0.22, dicke=4)
    s.pfeil(p2, p3, "", farbe=GRUEN, spitze=0.22, dicke=4)
    s.pfeil(p3, p1, "", farbe=ROT, spitze=0.22, dicke=4)
    for p_, n, dx, dy in ((p1, "1", -0.32, -0.22), (p2, "2", 0.34, -0.22), (p3, "3", 0.34, 0.1)):
        s.punkt(None, *p_, r=0.08)
        s.text(None, n, (p_[0] + dx, p_[1] + dy), ausrichtung="center")
    s.text(None, "3 mm", (0.5 * (xa + xb), yu - 0.28), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(None, "5 mm", (-1.4, 0.3), groesse=24, ausrichtung="right", farbe=ROT)
    s.text(None, "4 mm", (xb - 0.1, -0.05), groesse=24, ausrichtung="right", farbe=GRUEN)
    x = 0.55
    s.text(None, "Q = +1 nC", (x, 0.95), groesse=24)
    s.text(None, "W_{12} = 9 nJ", (x, 0.45), groesse=26, farbe=BLAU)
    s.text(None, "W_{23} = 0", (x, 0.02), groesse=26, farbe=GRUEN)
    s.text(None, "W_{31} = −9 nJ", (x, -0.41), groesse=26, farbe=ROT)
    s.linie(None, (x, -0.67), (x + 1.75, -0.67), dicke=2)
    s.text(None, s.tr("umlauf", "Umlauf: 0", "round trip: 0", "vuelta completa: 0", "闭合路径：0"), (x, -0.97), groesse=26)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k1potenzial():
    """Links die Platten mit Äquipotenziallinien, rechts phi(x)."""
    s = Szene("et1/k1potenzial")
    s.welt()
    mm = 0.95
    x0 = -3.2
    yu, yo = -0.9, 0.9
    platte(s, x0 - 0.07, yu, yo)
    platte(s, x0 + 3 * mm + 0.07, yu, yo)
    for k, u in enumerate(("9 V", "6 V", "3 V", "0 V")):
        x = x0 + k * mm
        if 0 < k < 3:
            s.linie(None, (x, yu), (x, yo), farbe=ROT, dicke=2.5, dash=DASH)
        s.text(None, u, (x, yo + 0.3), groesse=24, ausrichtung="center", farbe=ROT)
    for y in (-0.5, 0.5):
        s.pfeil((x0 + 0.22, y), (x0 + 3 * mm - 0.22, y), "", farbe=GRUEN, spitze=0.2, dicke=2.5)
    s.text(None, "E", (x0 + 1.5 * mm, 0), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(None, "A", (x0 - 0.07, yu - 0.3), ausrichtung="center")
    s.text(None, "B", (x0 + 3 * mm + 0.07, yu - 0.3), ausrichtung="center")
    a = s.achsen((0, 3, 1), (0, 9, 3), breite=2.7, hoehe=1.8, mitte=(1.75, 0.0), xl=s.tr("x_in_mm", "x in mm", "x in mm", "x en mm", "x / mm"),
                 yl=s.tr("phi_in_v", "φ in V", "φ in V", "φ en V", "φ / V"), gitter=True)
    s.kurve(a, "9-3*x", x=(0, 3), farbe=ROT)
    for x, y in ((0, 9), (1, 6), (2, 3), (3, 0)):
        s.punkt(a, x, y, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k1symbole():
    """Schaltzeichen der Spannungsquellen und der Zählpfeil."""
    s = Szene("et1/k1symbole")
    x1, x2 = -2.75, -0.15
    y = 0.25
    s.bauteil("vsource_dc", (x1, y), drehung=270, laenge=1.6, label="")
    s.text(None, "+", (x1 - 0.32, y + 0.36), farbe=ROT, ausrichtung="center")
    s.text(None, "−", (x1 - 0.32, y - 0.36), farbe=BLAU, ausrichtung="center")
    s.pfeil((x1 + 0.45, y + 0.6), (x1 + 0.45, y - 0.6), "", spitze=0.2, farbe=SCHWARZ)
    s.text(None, "U", (x1 + 0.62, y), ausrichtung="left")
    s.text(None, s.tr("batterie", "Batterie", "battery", "batería", "电池"), (x1 + 0.1, y - 1.1), groesse=24, ausrichtung="center")
    s.bauteil("vsource", (x2, y), drehung=270, laenge=1.6, label="")
    s.pfeil((x2 + 0.65, y + 0.6), (x2 + 0.65, y - 0.6), "", spitze=0.2, farbe=SCHWARZ)
    s.text(None, "U", (x2 + 0.82, y), ausrichtung="left")
    s.text(None, s.tr("quelle", "Gleichspannungsquelle", "DC voltage source", "fuente de tensión continua", "直流电压源"), (x2 + 0.1, y - 1.1), groesse=24, ausrichtung="center")
    x3 = 2.75
    yo, yu = y + 0.7, y - 0.7
    s.linie(None, (x3, yo), (x3, yu), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(None, x3, yo, r=0.1, farbe=ROT)
    s.punkt(None, x3, yu, r=0.1, farbe=ROT)
    s.text(None, "φ_1 = 9 V", (x3, yo + 0.32), groesse=24, ausrichtung="center")
    s.text(None, "φ_2 = 0 V", (x3, yu - 0.32), groesse=24, ausrichtung="center")
    s.pfeil((x3 - 0.25, yo - 0.12), (x3 - 0.25, yu + 0.12), "", spitze=0.2, farbe=BLAU, dicke=3)
    s.text(None, "U_{12} = 9 V", (x3 - 0.35, y + 0.2), groesse=24, ausrichtung="right", farbe=BLAU)
    s.pfeil((x3 + 0.25, yu + 0.12), (x3 + 0.25, yo - 0.12), "", spitze=0.2, farbe=ROT, dicke=3)
    s.text(None, "U_{21} = −9 V", (x3 - 0.35, y - 0.2), groesse=24, ausrichtung="right", farbe=ROT)
    s.speichern()


def schaltung(s, cx, cy, pot, gnd):
    """Rechenmodell-Kreis: Batterie links, zwei Widerstände rechts. pot = Potenziale oben, Mitte, unten; gnd = 0, 1 oder 2."""
    xl, xr = cx - 0.85, cx + 0.4
    yo, ym, yu = cy + 0.9, cy, cy - 0.9
    s.bauteil("vsource_dc", (xl, cy), drehung=270, laenge=1.8, label="", size=0.85)
    s.bauteil("resistor", (xr, cy + 0.45), drehung=270, laenge=0.9, label="", size=0.5)
    s.bauteil("resistor", (xr, cy - 0.45), drehung=270, laenge=0.9, label="", size=0.5)
    s.draht((xl, yo), (xr, yo))
    s.draht((xl, yu), (xr, yu))
    s.text(None, "9 V", (xl + 0.22, cy), groesse=24)
    ys = (yo, ym, yu)
    for k, y in enumerate(ys):
        s.punkt(None, xr, y, r=0.07, farbe=ROT)
        s.text(None, pot[k], (xr - 0.16, y + (-0.24 if k == 0 else 0.24 if k == 2 else 0)), groesse=24, ausrichtung="right", farbe=ROT)
    y = ys[gnd]
    s.draht((xr, y), (xr + 0.45, y))
    s.geraet("ground", (xr + 0.45, y), groesse=0.6)


def k1masse():
    """Derselbe Kreis mit Masse an drei Stellen."""
    s = Szene("et1/k1masse")
    x1, x2, x3 = -2.33, 0.0, 2.33
    y = -0.1
    schaltung(s, x1, y, ("9 V", "3 V", "0 V"), 2)
    s.text(None, s.tr("unten", "Masse am Minuspol", "ground at minus", "masa en el negativo", "接地点在负极"), (x1, y + 1.28), groesse=24, ausrichtung="center")
    schaltung(s, x2, y, ("6 V", "0 V", "−3 V"), 1)
    s.text(None, s.tr("mitte", "Masse in der Mitte", "ground in the middle", "masa en el centro", "接地点在中间"), (x2, y + 1.28), groesse=24, ausrichtung="center")
    schaltung(s, x3, y, ("0 V", "−6 V", "−9 V"), 0)
    s.text(None, s.tr("oben", "Masse am Pluspol", "ground at plus", "masa en el positivo", "接地点在正极"), (x3, y + 1.28), groesse=24, ausrichtung="center")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k1elektron():
    """Elektron zwischen den Platten, rechts die Energiebilanz über x."""
    s = Szene("et1/k1elektron")
    s.welt()
    mm = 0.95
    x0 = -3.2
    yu, yo = -0.9, 0.9
    platte(s, x0 - 0.07, yu, yo)
    platte(s, x0 + 3 * mm + 0.07, yu, yo)
    s.text(None, "A (+)", (x0 - 0.07, yu - 0.3), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(None, "B (−)", (x0 + 3 * mm + 0.07, yu - 0.3), groesse=24, ausrichtung="center", farbe=BLAU)
    s.pfeil((x0 + 0.3, 0.6), (x0 + 3 * mm - 0.3, 0.6), "", farbe=GRUEN, spitze=0.2, dicke=2.5)
    s.text(None, "E", (x0 + 1.5 * mm, 0.8), groesse=24, ausrichtung="center", farbe=GRUEN)
    ladung(s, None, x0 + 3 * mm - 0.2, -0.2, plus=False, r=0.15, groesse=22)
    s.pfeil((x0 + 3 * mm - 0.38, -0.2), (x0 + 0.3, -0.2), "", farbe=BLAU, spitze=0.2, dicke=3)
    s.text(None, s.tr("flug", "Flugrichtung", "direction of flight", "dirección de vuelo", "飞行方向"), (x0 + 1.5 * mm, -0.52), groesse=23, ausrichtung="center", farbe=BLAU)
    s.text(None, "F = −e E", (x0 + 1.5 * mm, 0.1), groesse=23, ausrichtung="center", farbe=BLAU)
    a = s.achsen((0, 3, 1), (-1.6, 1.6, 0.8), breite=2.7, hoehe=1.8, mitte=(1.75, 0.0), xl=s.tr("x_in_mm", "x in mm", "x in mm", "x en mm", "x / mm"),
                 yl=s.tr("w_18", "W in 10^{−18} J", "W in 10^{−18} J", "W en 10^{−18} J", "W / (10^{−18} J)"), gitter=True)
    s.linie(a, (0, 0), (3, 0), farbe=GRAU, dicke=2)
    s.kurve(a, "1.442*(3-x)/3", x=(0, 3), farbe=ORANGE)
    s.kurve(a, "-1.442*(3-x)/3", x=(0, 3), farbe=BLAU)
    s.punkt(a, 0, 1.442, farbe=ORANGE)
    s.punkt(a, 0, -1.442, farbe=BLAU)
    s.text(a, s.tr("kin", "Bewegungsenergie", "kinetic energy", "energía cinética", "动能"), (0.85, 1.36), groesse=23, farbe=BRAUN)
    s.text(a, s.tr("pot", "potenzielle Energie", "potential energy", "energía potencial", "势能"), (0.85, -1.36), groesse=23, farbe=BLAU)
    s.text(a, s.tr("summe", "Summe = 0", "sum = 0", "suma = 0", "总和 = 0"), (0.08, 0.24), groesse=23, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 10
def k1oersted():
    """Links: Magnetfeld um einen Draht mit Kompassnadeln, rechts: Induktion mit Spule und Magnet."""
    s = Szene("et1/k1oersted")
    cx = -2.05
    for r_ in (0.6, 1.0, 1.4):
        s.kreis(None, cx, 0, r_, farbe=GRUEN, dicke=2.5)
    for w in (70, 160, 250, 340):                    # Feldrichtung: im Uhrzeigersinn
        x, y = cx + 1.0 * cos(radians(w)), 1.0 * sin(radians(w))
        tx, ty = sin(radians(w)), -cos(radians(w))
        s.pfeil((x - 0.05 * tx, y - 0.05 * ty), (x + 0.05 * tx, y + 0.05 * ty), "", farbe=GRUEN, spitze=0.22, dicke=2.5)
    s.kreis(None, cx, 0, 0.2, farbe=SCHWARZ, dicke=3, fuellung="#ffd9b8", deckung=1.0)
    s.linie(None, (cx - 0.13, -0.13), (cx + 0.13, 0.13), dicke=3)
    s.linie(None, (cx - 0.13, 0.13), (cx + 0.13, -0.13), dicke=3)
    s.text(None, "I", (cx + 0.3, -0.28), groesse=26, ausrichtung="center")
    s.text(None, "H", (cx + 1.12, 1.14), groesse=26, ausrichtung="center", farbe=GRUEN)
    # Kompassnadeln: rote Spitze zeigt in Feldrichtung
    for w in (25, 115, 205, 295):
        x, y = cx + 0.8 * cos(radians(w)), 0.8 * sin(radians(w))
        tx, ty = sin(radians(w)), -cos(radians(w))
        s.linie(None, (x - 0.17 * tx, y - 0.17 * ty), (x, y), farbe=GRAU, dicke=5)
        s.linie(None, (x, y), (x + 0.17 * tx, y + 0.17 * ty), farbe=ROT, dicke=5)
    s.text(None, s.tr("oersted", "Strom in die Zeichenebene", "current into the page", "corriente hacia el plano", "电流垂直穿入纸面"), (cx, -1.75), groesse=24, ausrichtung="center")
    # Stabmagnet vor einer Spule
    y = 0.55
    s.box("", (0.15, y), breite=0.5, hoehe=0.42, farbe=GRAU, fuellung="#e8e8e8", dicke=2.5)
    s.box("", (0.65, y), breite=0.5, hoehe=0.42, farbe=ROT, fuellung="#fbe4e4", dicke=2.5)
    s.text(None, "S", (0.15, y), groesse=24, ausrichtung="center", farbe=GRAU)
    s.text(None, "N", (0.65, y), groesse=24, ausrichtung="center", farbe=ROT)
    s.pfeil((-0.05, y + 0.42), (0.85, y + 0.42), "", doppelt=True, spitze=0.18, dicke=3)
    s.text(None, s.tr("faraday", "bewegter Magnet", "moving magnet", "imán en movimiento", "运动的磁铁"), (0.4, y + 0.75), groesse=24, ausrichtung="center")
    x0, n, dx = 1.3, 7, 0.27
    s.pfeil((1.0, y), (3.35, y), "", farbe=GRUEN, spitze=0.2, dicke=2.5)
    s.text(None, "Φ", (3.25, y + 0.28), groesse=26, ausrichtung="center", farbe=GRUEN)
    for k in range(n):
        x = x0 + k * dx
        s.linie(None, (x - 0.07, y - 0.5), (x + 0.07, y + 0.5), farbe=BRAUN, dicke=4)
    xe = x0 + (n - 1) * dx
    xm = 0.5 * (x0 + xe)
    s.draht((x0 - 0.07, y - 0.5), (x0 - 0.07, -0.95), (xm - 0.45, -0.95))
    s.draht((xe - 0.07, y - 0.5), (xe - 0.07, -0.95), (xm + 0.45, -0.95))
    s.bauteil("voltmeter", (xm, -0.95), laenge=0.9, label="", size=0.8)
    s.text(None, "N = 500", (xm, y + 0.75), groesse=24, ausrichtung="center", farbe=BRAUN)
    s.text(None, "u_{ind}", (xm, -1.6), groesse=24, ausrichtung="center")
    s.speichern()


if __name__ == "__main__":
    for f in (k1atom, k1wegarbeit, k1reibung, k1pendel, k1feldpfeile, k1feldlinien, k1feldarbeit, k1potenzial, k1symbole, k1masse, k1elektron,
              k1oersted):
        f()
