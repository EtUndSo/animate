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


for f in (k2bausteine, k2linie, k2sprung, k2wege, k2residuen):
    f()
