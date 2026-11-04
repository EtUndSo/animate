"""ET3 Teil 2 (kap2_stufen.tex): fünf Abbildungen zur Laplace-Transformation.

Die p-Ebenen rechnen in echten Größen: x = Re p in 1/s; k2bausteine y = Im p in 1/s, k2linie y = f in Hz.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")
KLEIN = 22                 # zweite Zeilen und Markenschrift (Untergrenze)
BEREICH = 24               # Beschriftung in den p-Ebenen


def k2bausteine():
    """Links p-Ebene mit den Punkten a-d, rechts die vier Verläufe untereinander."""
    s = Szene("et3/k2bausteine")
    a = s.achsen((-1.1, 0.7), (-0.6, 3.9), breite=2.35, hoehe=3.3, mitte=(-2.2, 0), kreuz=True, xticks="-1;-0.5;0.5", yticks="3.14159",
                 yzahlen=False, yl="Im p = 2πf")
    s.band(a, -1.1, 0, -0.6, 3.9, farbe=ORANGE, deckung=0.09)
    s.band(a, 0, 0.7, -0.6, 3.9, farbe=ROT, deckung=0.08)
    s.linie(a, (-1.1, 3.14159), (0.7, 3.14159), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.text(a, "π", (-0.06, 2.84), BEREICH, "right")
    punkte = (("a", -0.5, 0, GRUEN, "center", 0), ("b", -0.3, 3.14159, ORANGE, "center", 0), ("c", 0, 3.14159, BLAU, "left", 0.05),
              ("d", 0.2, 3.14159, ROT, "left", 0.05))
    for name, x, y, farbe, ausr, dx in punkte:
        s.punkt(a, x, y, farbe=farbe, r=0.085)
        s.text(a, name, (x + dx, y + 0.36), ausrichtung=ausr, farbe=farbe)
    ab = s.tr("ab", "klingt ab\nσ < 0", "decays\nσ < 0", "decae\nσ < 0", "衰减\nσ < 0")
    auf = s.tr("auf", "wächst\nσ > 0", "grows\nσ > 0", "crece\nσ > 0", "增长\nσ > 0")
    s.text(a, ab, (-0.6, 1.6), BEREICH, "center", ORANGE)
    s.text(a, auf, (0.36, 1.6), BEREICH, "center", ROT)
    achse = s.tr("achse", "σ = Re p in 1/s", "σ = Re p in 1/s", "σ = Re p en 1/s", "σ = Re p，单位 1/s")
    s.text(a, achse, (-0.2, -0.98), BEREICH, "center")

    t = s.tr("t", "t in s", "t in s", "t en s", "t / s")
    feld = (("a: p = −0.5", (-0.1, 1.15), "exp(-0.5*x)", GRUEN, None),
            ("b: p = −0.3 + jπ", (-1.15, 1.15), "exp(-0.3*x)*cos(pi*x)", ORANGE, "exp(-0.3*x)"),
            ("c: p = jπ", (-1.15, 1.15), "cos(pi*x)", BLAU, None),
            ("d: p = 0.2 + jπ", (-5.2, 5.2), "exp(0.2*x)*cos(pi*x)", ROT, "exp(0.2*x)"))
    for k, (name, y, f, farbe, huelle) in enumerate(feld):
        unten = k == 3
        b = s.achsen((0, 8), y, breite=2.15, hoehe=0.72, mitte=(0.85, 1.29 - 0.86 * k), xticks="0;2;4;6;8", ymarks=False, yzahlen=False,
                     xzahlen=unten, xl=t if unten else "")
        if huelle:
            s.kurve(b, huelle, farbe=GRAU, dicke=2, dash=DASH)
            s.kurve(b, "-" + huelle, farbe=GRAU, dicke=2, dash=DASH)
        s.kurve(b, f, farbe=farbe, dicke=4)
        s.text(b, name, (8.2, 0.5 * (y[0] + y[1])), BEREICH)
    s.speichern()


def k2linie():
    """p-Ebene des Sprungs: Konvergenzbereich, Pol, Integrationslinie mit Bausteinpunkten."""
    s = Szene("et3/k2linie")
    a = s.achsen((-1.6, 1.8), (-2.9167, 3.0), breite=4.5, hoehe=4.7, mitte=(0, 0), kreuz=True, xticks="0.5", yticks="", xzahlen=False, yzahlen=False,
                 ymarks=False, yl="Im p")
    s.band(a, 0, 1.7, -2.75, 2.75, farbe=BLAU, deckung=0.1)
    s.weg(a, "0.5", "t", -2.75, 2.75, farbe=BLAU, dicke=4, pfeile="0.25;0.8")
    s.kreuzchen(a, 0, 0, farbe=SCHWARZ, groesse=0.24)
    pol = s.tr("pol", "Pol p = 0", "Pole p = 0", "Polo p = 0", "极点 p = 0")
    s.text(a, pol, (-0.13, -0.24), BEREICH, "right")
    s.text(a, "0.5", (0.54, -0.2), KLEIN)
    for f, name in ((1, "f = 1 Hz"), (2, "f = 2 Hz"), (-1, "f = −1 Hz")):
        s.punkt(a, 0.5, f, farbe=BLAU, r=0.065)
        s.text(a, name, (0.57, f), KLEIN)
    re = s.tr("re", "Re p in 1/s", "Re p in 1/s", "Re p en 1/s", "Re p（1/s）")
    s.text(a, re, (1.72, -0.2), BEREICH, "right")
    weg = s.tr("weg", "Integrationsweg", "Path of\nintegration", "Camino de\nintegración", "积分路径")
    s.text(a, "@{weg}\nRe p = σ = 0.5", (0.72, -1.95), BEREICH, "left", BLAU)
    kb = s.tr("kb", "Konvergenz-\nbereich Re p > 0", "Region of\nconvergence\nRe p > 0", "Región de\nconvergencia\nRe p > 0", "收敛域\nRe p > 0")
    s.text(a, kb, (1.21, 1.5), KLEIN, "center", BLAU)
    s.speichern()


def k2sprung():
    """Sprung aus Bausteinen mit |f| <= F."""
    s = Szene("et3/k2sprung")
    t = s.tr("t", "t in s", "t in s", "t en s", "t / s")
    a = s.achsen((-2, 5), (-0.3, 1.35), breite=5.9, hoehe=3.0, mitte=(0.2, 0), xl=t, yl="s_F(t)", xticks="-2;-1;0;1;2;3;4;5", yticks="0;0.5;1", gitter=True)
    s.daten(a, [(-2, 0), (0, 0), (0, 1), (5, 1)], farbe=GRAU, dicke=3, dash=DASH)
    s.daten(a, duenn(daten(DAT / "sprung_F0.25.dat")), farbe=ORANGE, dicke=3)
    s.daten(a, duenn(daten(DAT / "sprung_F1.dat")), farbe=GRUEN, dicke=3)
    s.daten(a, duenn(daten(DAT / "sprung_F4.dat")), farbe=BLAU, dicke=3)
    s.tr("sprung", "Sprung", "Step", "Escalón", "阶跃")
    s.legende(a, [("@{sprung} ε(t)", GRAU, "--"), ("F = 0.25 Hz", ORANGE, "-"), ("F = 1 Hz", GRUEN, "-"), ("F = 4 Hz", BLAU, "-")], (2.75, 0.46))
    s.speichern()


def k2wege():
    """Zwei Wege vom Eingang zum Ausgang. Die Pfeiltexte stehen innen (spart Breite), der Verweis auf eine Gleichung entfällt."""
    s = Szene("et3/k2wege")
    links, mitte, rechts, oben, unten = -2.0, 0.0, 2.0, 0.95, -0.95
    hell = dict(fuellung=BLAU, deckung=0.08)

    def kasten(x, y, breite, haupt, klein=None, **stil):
        h = 1.1 if klein else 0.62
        if klein and "\n" not in klein:
            h = 0.86
        s.box("", (x, y), breite=breite, hoehe=h, form="round", dicke=2.5, **stil)
        if klein:
            dy = 0.41 if "\n" in klein else 0.2
            s.text(None, haupt, (x, y + dy - 0.03), ausrichtung="center")
            s.text(None, klein, (x, y - (0.2 if "\n" in klein else 0.2)), KLEIN, "center")
        else:
            s.text(None, haupt, (x, y), ausrichtung="center")

    s.tr("falt", "Faltung", "Convolution", "Convolución", "卷积")
    muehsam = s.tr("muehsam", "mühsam:\nein Integral je t", "laborious:\none integral per t", "laborioso:\nuna integral por cada t", "繁琐：\n每个 t 一个积分")
    einfach = s.tr("einfach", "einfach:\neine Zahl je p", "simple:\none number per p", "sencillo:\nun número por cada p", "简单：\n每个 p 一个数")
    gew = s.tr("gew", "Gewichte", "weights", "pesos", "权重")
    kasten(links, oben, 1.25, "s(t)")
    kasten(mitte, oben, 2.0, "@{falt} ∗ h(t)", muehsam)
    kasten(rechts, oben, 1.25, "g(t)")
    kasten(links, unten, 1.25, "S(p)", gew, **hell)
    kasten(mitte, unten, 2.0, "× H(p)", einfach, **hell)
    kasten(rechts, unten, 1.25, "G(p)", gew, **hell)

    s.pfeil((links + 0.625, oben), (mitte - 1.0, oben))
    s.pfeil((mitte + 1.0, oben), (rechts - 0.625, oben))
    s.pfeil((links + 0.625, unten), (mitte - 1.0, unten))
    s.pfeil((mitte + 1.0, unten), (rechts - 0.625, unten))
    s.pfeil((links, oben - 0.31), (links, unten + 0.43))
    s.pfeil((rechts, unten + 0.43), (rechts, oben - 0.31))
    zerl = s.tr("zerl", "zerlegen\nℒ", "decompose\nℒ", "descomponer\nℒ", "分解\nℒ")
    zus = s.tr("zus", "zusammensetzen\nℒ^{−1}", "reassemble\nℒ^{−1}", "recomponer\nℒ^{−1}", "重新合成\nℒ^{−1}")
    s.text(None, zerl, (links + 0.1, -0.02), BEREICH)
    s.text(None, zus, (rechts - 0.1, -0.02), BEREICH, "right")
    zeit = s.tr("zeit", "Zeitbereich", "time domain", "dominio\ndel tiempo", "时域")
    bild = s.tr("bild", "Bildbereich", "transform\ndomain", "dominio\ntransformado", "变换域")
    s.text(None, zeit, (2.72, oben), BEREICH, "left", GRAU)
    s.text(None, bild, (2.72, unten), BEREICH, "left", GRAU)
    s.speichern()


def k2residuen():
    """Zwei p-Ebenen: Linie sigma = -1,5 im Streifen -2 < Re p < -1, nach links und rechts geschlossen."""
    s = Szene("et3/k2residuen")
    texte = (s.tr("links", "t > 0: links schließen,\nPol −2 zählt", "t > 0: close to the left,\npole −2 counts", "t > 0: cerrar por la izquierda,\ncuenta el polo −2",
                  "t > 0：向左闭合，\n极点 −2 计入"),
             s.tr("rechts", "t < 0: rechts schließen,\nPol −1 zählt (mit Minus)", "t < 0: close to the right,\npole −1 counts (with a minus sign)",
                  "t < 0: cerrar por la derecha,\ncuenta el polo −1 (con signo menos)", "t < 0：向右闭合，\n极点 −1 计入（带负号）"))
    for k, (mitte, text) in enumerate(zip((-1.75, 1.75), texte)):
        # gleicher Maßstab in x und y (0,58 Einheiten je 1/s), damit der Halbkreis rund bleibt
        a = s.achsen((-3.7, 1.2), (-2.5, 2.6), breite=2.842, hoehe=2.958, mitte=(mitte, 0), kreuz=True, xticks="", yticks="", xzahlen=False, yzahlen=False,
                     xmarks=False, ymarks=False, yl="Im p")
        s.band(a, -2, -1, -2.4, 2.4, farbe=BLAU, deckung=0.1)
        s.weg(a, "-1.5", "t", -2.2, 2.2, farbe=BLAU, dicke=4, pfeile="0.25;0.75")
        s.weg(a, "-1.5-2.2*sin(t)" if k == 0 else "-1.5+2.2*sin(t)", "2.2*cos(t)", 0, 3.14159265, farbe=ROT, dicke=4, pfeile="0.25;0.75", n=181)
        for x in (-1, -2):
            s.kreuzchen(a, x, 0, farbe=SCHWARZ, groesse=0.2)
            s.text(a, "−%d" % -x, (x, -0.4), KLEIN, "center")
        s.text(a, "Re p", (1.42, -0.42), KLEIN, "right")
        s.text(a, text, (-1.25, -3.3), BEREICH, "center")
    s.speichern()


# ------------------------------------------------------------------ Neufassung 03.11.2026 (Gliederung wie das Skript)
def _ebene(s, mitte, x, y, breite, hoehe):
    """Kleine p-Ebene ohne Zahlen; Beschriftung „Re p“ rechts unten an der Achse."""
    a = s.achsen(x, y, breite=breite, hoehe=hoehe, mitte=mitte, kreuz=True, xticks="", yticks="", xzahlen=False, yzahlen=False,
                 xmarks=False, ymarks=False, yl="Im p")
    s.text(a, "Re p", (x[1] - 0.1, -0.08 * (y[1] - y[0])), KLEIN, "right")
    return a


def _kbtext(s):
    return s.tr("kb", "Konvergenz-\nbereich", "region of\nconvergence", "región de\nconvergencia", "收敛域")


def k2kbhalb():
    """Konvergenzbereiche des rechtsseitigen und des linksseitigen Exponentialimpulses (Re b = 1)."""
    s = Szene("et3/k2kbhalb")
    kb = _kbtext(s)
    for k, (mitte, x0, x1, tx, titel) in enumerate((((-1.95, 0), -1, 2.2, 0.75, "e^{−bt} ε(t):  Re p > −Re b"),
                                                     ((1.95, 0), -2.6, -1, -1.8, "e^{−bt} ε(−t):  Re p < −Re b"))):
        a = _ebene(s, mitte, (-2.8, 2.4), (-2.1, 2.3), 2.6, 2.2)
        s.band(a, x0, x1, -2.0, 2.0, farbe=BLAU, deckung=0.12)
        s.linie(a, (-1, -2.0), (-1, 2.0), farbe=BLAU, dicke=3, dash=DASH)
        s.text(a, "−Re b", (-1.08 if k == 0 else -0.92, -0.35), KLEIN, "right" if k == 0 else "left")
        s.text(a, kb, (tx, 1.35), KLEIN, "center", BLAU)
        s.text(a, titel, (-0.2, -2.75), BEREICH, "center")
    s.speichern()


def k2zweiseitig():
    """Links e^{-b|t|} für b = 0,8 und b = -0,8, rechts der Streifen -b < Re p < b mit den Polen ±b."""
    s = Szene("et3/k2zweiseitig")
    t = s.tr("t", "t in s", "t in s", "t en s", "t / s")
    o = s.achsen((-3, 3), (0, 1.25), breite=2.5, hoehe=1.05, mitte=(-1.9, 0.8), kreuz=True, xticks="-2;2", yticks="", yzahlen=False,
                 ymarks=False)
    s.kurve(o, "exp(-0.8*abs(x))", farbe=BLAU, dicke=4)
    s.text(o, "b = 0.8/s", (2.9, 1.15), KLEIN, "right")
    u = s.achsen((-3, 3), (0, 11), breite=2.5, hoehe=1.05, mitte=(-1.9, -0.95), kreuz=True, xticks="-2;2", yticks="", yzahlen=False,
                 ymarks=False, xl=t)
    s.kurve(u, "exp(0.8*abs(x))", farbe=ROT, dicke=4)
    s.text(u, "b = −0.8/s", (2.9, 10.5), KLEIN, "right")
    a = _ebene(s, (2.1, 0), (-2.6, 2.6), (-2.1, 2.3), 2.3, 2.0)
    s.band(a, -1, 1, -2.0, 2.0, farbe=BLAU, deckung=0.12)
    for x in (-1, 1):
        s.linie(a, (x, -2.0), (x, 2.0), farbe=BLAU, dicke=3, dash=DASH)
        s.kreuzchen(a, x, 0, farbe=SCHWARZ, groesse=0.2)
    s.text(a, "−b", (-1.08, -0.4), KLEIN, "right")
    s.text(a, "b", (1.08, -0.4), KLEIN, "left")
    s.text(a, _kbtext(s), (1.25, 1.55), KLEIN, "left", BLAU)
    s.speichern()


def k2pn():
    """Pol-Nullstellen-Diagramm von (2p²+5p+12)/((p²+2p+10)(p+2)), Konvergenzbereich Re p > -1."""
    s = Szene("et3/k2pn")
    a = s.achsen((-3, 2.3), (-3.9, 4.1), breite=3.2, hoehe=4.8, mitte=(0, 0), kreuz=True, xticks="", yticks="", xzahlen=False, yzahlen=False,
                 xmarks=False, ymarks=False, yl="Im p")
    s.band(a, -1, 2.1, -3.8, 3.8, farbe=BLAU, deckung=0.12)
    s.linie(a, (-1, -3.8), (-1, 3.8), farbe=BLAU, dicke=3, dash=DASH)
    for x, y in ((-2, 0), (-1, 3), (-1, -3)):
        s.kreuzchen(a, x, y, farbe=SCHWARZ, groesse=0.22)
    for y in (2.107, -2.107):
        s.kreis(a, -1.25, y, 0.09, farbe=SCHWARZ, dicke=3)
    for y, l in ((3, "3"), (-3, "−3"), (2.107, "2.11"), (-2.107, "−2.11")):
        s.linie(a, (-0.07, y), (0.07, y), farbe=GRAU, dicke=2)
        s.text(a, l, (0.12, y), KLEIN)
    s.text(a, "−2", (-2, -0.45), KLEIN, "center")
    s.text(a, "−1", (-0.92, -0.45), KLEIN, "left")
    s.text(a, "−1.25", (-1.45, 2.65), KLEIN, "right")
    s.text(a, "Re p", (2.2, -0.45), KLEIN, "right")
    s.text(a, _kbtext(s), (1.1, -1.6), KLEIN, "center", BLAU)
    s.speichern()


def k2dreikb():
    """Ein Ausdruck, drei Signale: Pole von 1/((p+1)(p+2)) und die drei möglichen Konvergenzbereiche (2 x 2)."""
    s = Szene("et3/k2dreikb")
    teile = ((s.tr("pole", "(a) Pole", "(a) poles", "(a) polos", "(a) 极点"), None, ()),
             ("(b) Re p > −1", (-1, 1.3), (-1,)),
             ("(c) Re p < −2", (-3.5, -2), (-2,)),
             ("(d) −2 < Re p < −1", (-2, -1), (-1, -2)))
    for k, (t, band, linien) in enumerate(teile):
        mitte = (-1.95 + 3.9 * (k % 2), 1.55 - 3.45 * (k // 2))
        a = _ebene(s, mitte, (-3.6, 1.4), (-2.1, 2.3), 2.4, 2.1)
        if band:
            s.band(a, band[0], band[1], -2.0, 2.0, farbe=BLAU, deckung=0.12)
        for x in linien:
            s.linie(a, (x, -2.0), (x, 2.0), farbe=BLAU, dicke=3, dash=DASH)
        for x in (-1, -2):
            s.kreuzchen(a, x, 0, farbe=SCHWARZ, groesse=0.2)
            s.text(a, "−%d" % -x, (x, -0.45), KLEIN, "center")
        s.text(a, t, (-1.1, -2.75), BEREICH, "center")
    s.speichern()


def k2rlc():
    """RLC-System: Quelle, R und L in Reihe, Ausgang am Kondensator (Maße wie im Heft, Ursprung in der Mitte)."""
    s = Szene("et3/k2rlc")
    k = 0.92

    def p(x, y):
        return ((x - 2.5) * k, (y - 1.0) * k)

    s.kreis(None, *p(0, 1), 0.35 * k, farbe=SCHWARZ, dicke=3)
    s.text(None, "~", p(0, 1.02), 34, "center")
    s.draht(p(0, 1.35), p(0, 2), p(0.8, 2))
    s.bauteil("resistor", p(1.3, 2), laenge=1.0 * k, label="")
    s.text(None, "R", p(1.3, 2.45), ausrichtung="center")
    s.draht(p(1.8, 2), p(2.3, 2))
    s.bauteil("inductor", p(2.8, 2), laenge=1.0 * k, label="")
    s.text(None, "L", p(2.8, 2.45), ausrichtung="center")
    s.draht(p(3.3, 2), p(5.2, 2))
    s.pfeil(p(3.55, 2), p(3.95, 2), spitze=0.18)
    s.text(None, "i(t)", p(3.75, 2.4), ausrichtung="center")
    s.bauteil("capacitor", p(4.5, 1), drehung=270, laenge=2 * k, label="")
    s.text(None, "C", p(4.15, 1), ausrichtung="right")
    s.draht(p(0, 0.65), p(0, 0), p(5.2, 0))
    for x, y in ((4.5, 2), (4.5, 0)):
        s.punkt(None, *p(x, y), r=0.06)
    for x, y in ((5.2, 2), (5.2, 0)):
        s.kreis(None, *p(x, y), 0.07, farbe=SCHWARZ, dicke=2, fuellung="#ffffff", deckung=1)
    s.pfeil(p(5.65, 1.8), p(5.65, 0.2), "u_2(t)", farbe=ROT, spitze=0.2)
    s.pfeil(p(-0.75, 1.6), p(-0.75, 0.4), "u_1(t)", farbe=BLAU, label_seite="right", spitze=0.2)
    s.speichern()


def k2rlcpole():
    """Pole des RLC-Systems: (a) xi = 0,5 auf dem Kreis mit Radius omega_0 = 2, (b) xi = 1,25, omega_0 = 1,6."""
    s = Szene("et3/k2rlcpole")
    # (a) gleicher Maßstab in x und y (0,55 Einheiten je Einheit), damit der Kreis rund bleibt
    a = s.achsen((-3.6, 1.6), (-2.7, 2.9), breite=2.42, hoehe=2.61, mitte=(-1.9, 0.2), kreuz=True, xticks="", yticks="", xzahlen=False,
                 yzahlen=False, xmarks=False, ymarks=False, yl="Im p")
    s.band(a, -1, 1.5, -2.6, 2.6, farbe=BLAU, deckung=0.12)
    s.linie(a, (-1, -2.6), (-1, 2.6), farbe=BLAU, dicke=3, dash=DASH)
    s.weg(a, "2*cos(t)", "2*sin(t)", 1.5708, 4.7124, farbe=HELLGRAU, dicke=2, dash=DASH)
    s.linie(a, (0, 0), (-1, 1.732), farbe=GRAU, dicke=2)
    s.weg(a, "0.55*cos(t)", "0.55*sin(t)", 2.0944, 3.1416, farbe=GRAU, dicke=2)
    s.text(a, "θ", (-0.75, 0.33), KLEIN, "center")
    s.text(a, "ω₀", (-0.42, 1.0), KLEIN, "left")
    for y in (1.732, -1.732):
        s.kreuzchen(a, -1, y, farbe=SCHWARZ, groesse=0.22)
    s.linie(a, (-1, 1.732), (-2.55, 1.732), farbe=HELLGRAU, dicke=2)
    s.pfeil((-2.45, 0.05), (-2.45, 1.68), "", doppelt=True, spitze=0.14, dicke=2, on=a)
    s.text(a, "ω₀√(1−ξ²)", (-2.6, 0.87), KLEIN, "right")
    s.text(a, "−ξω₀", (-1.08, -0.4), KLEIN, "right")
    s.text(a, "Re p", (1.5, -0.4), KLEIN, "right")
    s.text(a, "(a)  ξ < 1", (-1.0, -3.25), BEREICH, "center")
    # (b)
    b = s.achsen((-3.8, 1.6), (-2.7, 2.9), breite=2.52, hoehe=2.61, mitte=(1.92, 0.2), kreuz=True, xticks="", yticks="", xzahlen=False,
                 yzahlen=False, xmarks=False, ymarks=False, yl="Im p")
    s.band(b, -0.8, 1.5, -2.6, 2.6, farbe=BLAU, deckung=0.12)
    s.linie(b, (-0.8, -2.6), (-0.8, 2.6), farbe=BLAU, dicke=3, dash=DASH)
    for x in (-0.8, -3.2):
        s.kreuzchen(b, x, 0, farbe=SCHWARZ, groesse=0.22)
    s.linie(b, (-2, 0.08), (-2, -0.08), farbe=GRAU, dicke=2)
    s.text(b, "−ξω₀", (-2, -0.45), KLEIN, "center")
    s.pfeil((-3.15, 0.6), (-0.85, 0.6), "", doppelt=True, spitze=0.14, dicke=2, on=b)
    s.text(b, "2ω₀√(ξ²−1)", (-2, 1.0), KLEIN, "center")
    s.text(b, "Re p", (1.5, -0.4), KLEIN, "right")
    s.text(b, "(b)  ξ > 1", (-1.1, -3.25), BEREICH, "center")
    s.speichern()


def k2rlch():
    """Impulsantwort des RLC-Systems mit R = 4 Ohm, L = 1 H: Kriechfall, Grenzfall, Schwingfall."""
    s = Szene("et3/k2rlch")
    t = s.tr("t", "t in s", "t in s", "t en s", "t / s")
    a = s.achsen((0, 4), (-1.2, 2.8), breite=5.9, hoehe=3.0, mitte=(0, 0), xl=t, yl="h(t) in 1/s", xticks="0;1;2;3;4", yticks="-1;0;1;2",
                 gitter=True)
    s.kurve(a, "1.5*(exp(-x)-exp(-3*x))", x=(0, 4), farbe=ORANGE, dicke=4)
    s.kurve(a, "4*x*exp(-2*x)", x=(0, 4), farbe=GRUEN, dicke=4)
    s.kurve(a, "5*exp(-2*x)*sin(4*x)", x=(0, 4), farbe=BLAU, dicke=4)
    s.tr("kriech", "a) Kriechfall, C = 1/3 F", "a) overdamped, C = 1/3 F", "a) sobreamortiguado, C = 1/3 F", "a) 过阻尼，C = 1/3 F")
    s.tr("grenz", "b) Grenzfall, C = 1/4 F", "b) critically damped, C = 1/4 F", "b) amortiguamiento crítico, C = 1/4 F", "b) 临界阻尼，C = 1/4 F")
    s.tr("schwing", "c) Schwingfall, C = 1/20 F", "c) underdamped, C = 1/20 F", "c) subamortiguado, C = 1/20 F", "c) 欠阻尼，C = 1/20 F")
    s.legende(a, [("@{kriech}", ORANGE, "-"), ("@{grenz}", GRUEN, "-"), ("@{schwing}", BLAU, "-")], (1.75, 2.55))
    s.speichern()


# ---- Blockschaltbilder: Heft-Koordinaten (cm) mal K
K = 0.8


class Block:
    """Kleine Hilfe für Blockschaltbilder in Heft-Koordinaten (cm); (x0, y0) wird der Ursprung der Szene."""

    def __init__(self, s, x0=0.0, y0=0.0, k=K):
        self.s, self.x0, self.y0, self.k = s, x0, y0, k

    def p(self, x, y):
        return ((x - self.x0) * self.k, (y - self.y0) * self.k)

    def kasten(self, text, x, y, breite=1.0):
        self.s.box(text, self.p(x, y), breite=breite * self.k, hoehe=0.7 * self.k, form="rect", groesse=24, dicke=2.5)

    def glied(self, text, x, y, d=0.75, groesse=22):
        """Proportionalglied: Kreis mit Durchmesser d (cm) und der Zahl darin."""
        self.s.kreis(None, *self.p(x, y), d / 2 * self.k, farbe=SCHWARZ, dicke=2.5, fuellung="#ffffff", deckung=1)
        self.s.text(None, text, self.p(x, y), groesse, "center")

    def summe(self, x, y):
        """Summierstelle: Kreis mit Radius 0,25 cm."""
        self.s.kreis(None, *self.p(x, y), 0.25 * self.k, farbe=SCHWARZ, dicke=2.5, fuellung="#ffffff", deckung=1)

    def knoten(self, x, y):
        self.s.punkt(None, *self.p(x, y), r=0.05)

    def pfeil(self, a, b, knick="none"):
        self.s.pfeil(self.p(*a), self.p(*b), knick=knick, spitze=0.15, dicke=2.5)

    def draht(self, *pkte):
        self.s.draht(*[self.p(*q) for q in pkte], dicke=2.5)

    def text(self, t, x, y, ausr="center", groesse=24, farbe=SCHWARZ):
        self.s.text(None, t, self.p(x, y), groesse, ausr, farbe)


def _rueckkopplung(b, x, y, vor, zur, vor_kreis=False, zur_kreis=False):
    """Eingang, Summierstelle, Vorwärtsglied, Knoten, Ausgang und Rückführung wie im Heft; Bildursprung bei (x, y)."""
    hv = 0.375 if vor_kreis else 0.5
    hz = 0.375 if zur_kreis else 0.5
    b.text("S(p)", x, y)
    b.summe(x + 1.3, y)
    (b.glied if vor_kreis else b.kasten)(vor, x + 2.7, y)
    b.knoten(x + 3.9, y)
    b.text("G(p)", x + 4.9, y)
    (b.glied if zur_kreis else b.kasten)(zur, x + 2.7, y - 1.2)
    b.pfeil((x + 0.45, y), (x + 1.05, y))
    b.pfeil((x + 1.55, y), (x + 2.7 - hv, y))
    b.pfeil((x + 2.7 + hv, y), (x + 4.45, y))
    b.pfeil((x + 3.9, y), (x + 2.7 + hz, y - 1.2), "vh")
    b.pfeil((x + 2.7 - hz, y - 1.2), (x + 1.3, y - 0.25), "hv")
    b.text("+", x + 0.98, y + 0.25, groesse=22)
    b.text("−", x + 1.1, y - 0.45, groesse=22)


def k2rueck():
    """Rückgekoppelte Verbindung zweier LTI-Systeme."""
    s = Szene("et3/k2rueck")
    b = Block(s, 3.2, -0.6)
    b.text("S(p)", 0, 0)
    b.summe(1.6, 0)
    b.kasten("H₁(p)", 3.4, 0, 1.3)
    b.knoten(5.0, 0)
    b.text("G(p)", 6.4, 0)
    b.kasten("H₂(p)", 3.4, -1.3, 1.3)
    b.pfeil((0.45, 0), (1.35, 0))
    b.pfeil((1.85, 0), (2.75, 0))
    b.pfeil((4.05, 0), (5.95, 0))
    b.pfeil((5.0, 0), (4.05, -1.3), "vh")
    b.pfeil((2.75, -1.3), (1.6, -0.25), "hv")
    b.text("+", 1.25, 0.25, groesse=22)
    b.text("−", 1.38, -0.45, groesse=22)
    s.box("", b.p(3.25, -0.62), breite=4.3 * K, hoehe=2.55 * K, form="rect", farbe=GRAU, deckung=0, dicke=2, dash=DASH)
    b.text("H(p)", 5.1, -1.7, groesse=22, farbe=GRAU)
    s.speichern()


def k2erster():
    """Zwei Aufbauten von 1/(p+b): (a) Integrierer vorwärts, b zurück; (b) 1/b vorwärts, Differenzierer zurück."""
    s = Szene("et3/k2erster")
    b = Block(s, 2.5, -1.9)
    _rueckkopplung(b, 0, 0, "1/p", "b", zur_kreis=True)
    b.text("(a)", 0.2, -1.2)
    _rueckkopplung(b, 0, -2.6, "1/b", "p", vor_kreis=True)
    b.text("(b)", 0.2, -3.8)
    s.speichern()


def k2formen():
    """Drei Aufbauten von 1/((p+c1)(p+c2)): (a) direkt, (b) Kaskade, (c) parallel (übereinander)."""
    s = Szene("et3/k2formen")
    b = Block(s, 3.8, -4.4)
    # (a) direkte Darstellung
    b.text("S(p)", 0, 0)
    b.summe(1.2, 0)
    b.kasten("1/p", 2.5, 0)
    b.knoten(3.6, 0)
    b.kasten("1/p", 4.7, 0)
    b.knoten(5.8, 0)
    b.text("G(p)", 6.9, 0)
    b.glied("c₁+c₂", 3.6, -1.15, d=0.95, groesse=20)
    b.glied("c₁c₂", 5.8, -1.15, groesse=20)
    b.summe(3.6, -2.2)
    b.pfeil((0.45, 0), (0.95, 0))
    b.pfeil((1.45, 0), (2.0, 0))
    b.pfeil((3.0, 0), (4.2, 0))
    b.pfeil((5.2, 0), (6.45, 0))
    b.pfeil((3.6, 0), (3.6, -1.15 + 0.475))
    b.pfeil((5.8, 0), (5.8, -1.15 + 0.375))
    b.pfeil((3.6, -1.15 - 0.475), (3.6, -2.2 + 0.25))
    b.pfeil((5.8, -1.15 - 0.375), (3.85, -2.2), "vh")
    b.pfeil((3.35, -2.2), (1.2, -0.25), "hv")
    b.text("+", 0.88, 0.25, groesse=22)
    b.text("−", 1.0, -0.45, groesse=22)
    b.text("(a)", 0.1, -1.2)
    # (b) Kaskade
    y = -3.6
    b.text("S(p)", 0, y)
    for xs, xi, xn, c in ((1.2, 2.4, 3.4, "c₁"), (4.3, 5.5, 6.5, "c₂")):
        b.summe(xs, y)
        b.kasten("1/p", xi, y)
        b.knoten(xn, y)
        b.glied(c, xi, y - 1.1)
        b.pfeil((xs + 0.25, y), (xi - 0.5, y))
        b.draht((xi + 0.5, y), (xn, y))
        b.pfeil((xn, y), (xi + 0.375, y - 1.1), "vh")
        b.pfeil((xi - 0.375, y - 1.1), (xs, y - 0.25), "hv")
        b.text("+", xs - 0.32, y + 0.25, groesse=22)
        b.text("−", xs - 0.2, y - 0.45, groesse=22)
    b.pfeil((0.45, y), (0.95, y))
    b.pfeil((3.4, y), (4.05, y))
    b.pfeil((6.5, y), (7.05, y))
    b.text("G(p)", 7.5, y)
    b.text("(b)", 0.1, y - 1.2)
    # (c) parallel
    y = -6.6
    b.text("S(p)", 0, y - 0.9)
    b.draht((0.45, y - 0.9), (0.8, y - 0.9))
    b.knoten(0.8, y - 0.9)
    for dy, c in ((0, "c₁"), (-1.8, "c₂")):
        yy = y + dy
        b.summe(1.6, yy)
        b.kasten("1/p", 2.8, yy)
        b.knoten(3.9, yy)
        b.glied(c, 2.8, yy - 0.85)
        b.pfeil((0.8, y - 0.9), (1.35, yy), "vh")
        b.pfeil((1.85, yy), (2.3, yy))
        b.draht((3.3, yy), (3.9, yy))
        b.pfeil((3.9, yy), (3.175, yy - 0.85), "vh")
        b.pfeil((2.425, yy - 0.85), (1.6, yy - 0.25), "hv")
        b.text("+", 1.28, yy + 0.25, groesse=22)
        b.text("−", 1.42, yy - 0.45, groesse=22)
    b.summe(4.8, y - 0.9)
    b.pfeil((3.9, y), (4.8, y - 0.65), "hv")
    b.pfeil((3.9, y - 1.8), (4.8, y - 1.15), "hv")
    b.text("+", 4.55, y - 0.4, groesse=22)
    b.text("−", 4.55, y - 1.42, groesse=22)
    b.glied("1/(c₂−c₁)", 6.05, y - 0.9, d=1.3, groesse=16)
    b.pfeil((5.05, y - 0.9), (5.4, y - 0.9))
    b.pfeil((6.7, y - 0.9), (7.0, y - 0.9))
    b.text("G(p)", 7.45, y - 0.9)
    b.text("(c)", 0.1, y - 3.25)
    s.speichern()


def k2direkt():
    """(a) 1/H2 vor H1, (b) direkte Form von (β2 p² + β1 p + β0)/(p² + α1 p + α0) ohne Differenzierer."""
    s = Szene("et3/k2direkt")
    b = Block(s, 4.6, -2.3, k=0.7)
    # (a)
    b.text("S(p)", 0, 0)
    b.kasten("1/H₂(p)", 2.2, 0, 2.0)
    b.kasten("H₁(p)", 6.0, 0, 2.0)
    b.text("G(p)", 8.0, 0)
    b.pfeil((0.45, 0), (1.2, 0))
    b.pfeil((3.2, 0), (5.0, 0))
    b.pfeil((7.0, 0), (7.55, 0))
    b.text("G₁(p)", 4.1, 0.35, groesse=22)
    b.text("(a)", 0, -0.9)
    # (b)
    y = -4.3
    b.text("S(p)", 0, y)
    b.summe(1.2, y)
    b.knoten(2.1, y)
    b.kasten("1/p", 3.1, y)
    b.knoten(4.3, y)
    b.kasten("1/p", 5.4, y)
    b.knoten(6.6, y)
    for x, t in ((2.1, "β₂"), (4.3, "β₁"), (6.6, "β₀")):
        b.glied(t, x, y + 1.2)
        b.pfeil((x, y), (x, y + 0.825))
    s.box("Σ", b.p(8.0, y + 1.95), breite=0.7 * b.k, hoehe=2.4 * b.k, form="rect", groesse=26, dicke=2.5)
    b.text("G(p)", 9.3, y + 1.95)
    b.pfeil((2.1, y + 1.575), (7.65, y + 2.65), "vh")
    b.pfeil((4.3, y + 1.575), (7.65, y + 1.95), "vh")
    b.pfeil((6.975, y + 1.2), (7.65, y + 1.2))
    b.pfeil((8.35, y + 1.95), (8.85, y + 1.95))
    b.glied("α₁", 4.3, y - 1.2)
    b.glied("α₀", 6.6, y - 1.2)
    b.summe(4.3, y - 2.1)
    b.pfeil((0.45, y), (0.95, y))
    b.draht((1.45, y), (2.6, y))
    b.pfeil((2.1, y), (2.6, y))
    b.draht((3.6, y), (4.9, y))
    b.pfeil((4.3, y), (4.9, y))
    b.draht((5.9, y), (6.6, y))
    b.pfeil((4.3, y), (4.3, y - 0.825))
    b.pfeil((6.6, y), (6.6, y - 0.825))
    b.pfeil((4.3, y - 1.575), (4.3, y - 1.85))
    b.pfeil((6.6, y - 1.575), (4.55, y - 2.1), "vh")
    b.pfeil((4.05, y - 2.1), (1.2, y - 0.25), "hv")
    b.text("+", 0.88, y + 0.25, groesse=22)
    b.text("−", 1.0, y - 0.45, groesse=22)
    for x, t in ((2.1, "d²g₁/dt²"), (4.3, "dg₁/dt"), (6.6, "g₁")):
        b.text(t, x + 0.12, y - 0.5, "left", 16)
    b.text("(b)", 0, y - 1.6)
    s.speichern()


for f in (k2bausteine, k2linie, k2sprung, k2wege, k2residuen, k2kbhalb, k2zweiseitig, k2pn, k2dreikb, k2rlc, k2rlcpole, k2rlch, k2rueck,
          k2erster, k2formen, k2direkt):
    f()
