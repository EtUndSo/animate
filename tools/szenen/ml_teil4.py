"""Machine Learning Teil 4 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap4_stufen.tex): Abbildungen.

Szenenname ml/k4<name> = \\label{fig:k4<name>} im Heft. Stil wie tools/szenen/ml_teil3.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil4.py
Export: python tools/export_szenen.py ml/k4<name> ...   (jedes Bild höchstens 548 px breit)
Szenen mit mehreren Teilbildern rufen zuerst s.welt() auf: Danach sind Texte ohne on= in Szeneneinheiten.
Die Rechenbilder ml/k4r<name> zeigen eine Summe, ein Produkt oder ein Skalarprodukt Schritt für Schritt
(s.summe, s.produkt, s.skalarprodukt, s.formel; Beispiele in tools/szenen/beispiel_summen.py).
Die Zahlen prüft C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\rechnung_kap4.py; die Punktwolken, Würfelfolgen und
Würfelverteilungen sind dieselben wie im Heft (dort mit festen Startwerten erzeugt und von rechnung_kap4.py verglichen).
"""
import json
import math
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24
HELLBLAU = "#9ec3ec"
ROT_HELL = "#f4c7c7"
GRUEN_HELL = "#c4e3cf"
BLAU_HELL = "#cfe0f5"
HEFT = Path(r"C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte")


def zug(s, on, pts, farbe=SCHWARZ, dicke=3, dash=""):
    """Linienzug in Datenkoordinaten."""
    return s.daten(on, pts, farbe=farbe, dicke=dicke, dash=dash)


def heft_punkte(label, muster=r"coordinates \{(.*?)\};"):
    """Koordinatenlisten der Abbildung \\label{label} aus dem Heft (dieselben Daten wie im PDF)."""
    tex = (HEFT / "kap4_stufen.tex").read_text(encoding="utf-8") + (HEFT / "kap4_stufen_b.tex").read_text(encoding="utf-8")
    ende = tex.index(r"\label{%s}" % label)
    abb = tex[tex.rfind(r"\begin{abb}", 0, ende):ende]
    return [[tuple(float(z) for z in t.split(",")) for t in re.findall(r"\(([^()]*)\)", block)]
            for block in re.findall(muster, abb, re.S)]


# ------------------------------------------------------------------ Abschnitt 4
def k4baum():
    s = Szene("ml/k4baum")
    teile = s.tr("teile", "10 000 Teile", "10,000 parts", "10 000 piezas", "10 000 个零件")
    defekt = s.tr("defekt", "defekt", "faulty", "defectuosas", "有缺陷")
    intakt = s.tr("intakt", "intakt", "intact", "intactas", "完好")
    alarm = s.tr("alarm", "Alarm", "alarm", "alarma", "报警")
    kein = s.tr("kein", "kein Alarm", "no alarm", "sin alarma", "无报警")
    kast = dict(form="round", groesse=MITTEL, dicke=2.5)
    rot = dict(form="round", groesse=MITTEL, dicke=2.5, farbe=ROT, fuellung="#fbe0e0")
    knoten = {"w": ((0, 1.75), "@{teile}", kast, 2.2), "d": ((-1.75, 0.45), "100 @{defekt}", kast, 1.75),
              "i": ((1.75, 0.45), "9 900 @{intakt}", kast, 2.0),
              "da": ((-2.6, -0.85), "99 @{alarm}", rot, 1.45), "dk": ((-0.92, -0.85), "1 @{kein}", kast, 1.7),
              "ia": ((0.92, -0.85), "495 @{alarm}", rot, 1.6), "ik": ((2.6, -0.85), "9 405\n@{kein}", kast, 1.5)}
    for (x, y), t, stil, b in knoten.values():
        s.box(t, (x, y), breite=b, hoehe=0.55 if "\n" not in t else 0.85, **stil)
    kanten = (("w", "d", "1 %", "right"), ("w", "i", "99 %", "left"), ("d", "da", "99 %", "right"), ("d", "dk", "1 %", "left"),
              ("i", "ia", "5 %", "right"), ("i", "ik", "95 %", "left"))
    for a_, b_, t, seite in kanten:
        (xa, ya), (xb, yb) = knoten[a_][0], knoten[b_][0]
        hb = 0.43 if b_ == "ik" else 0.28
        s.pfeil((xa, ya - 0.28), (xb, yb + hb), label=t, dicke=2.5, spitze=0.15, groesse=KLEIN, label_seite=seite)
    s.text(None, s.tr("fazit", "594 Alarme, davon 99 an defekten Teilen:", "594 alarms, 99 of them on faulty parts:",
                      "594 alarmas, 99 de ellas en piezas defectuosas:", "共 594 次报警，其中 99 次来自有缺陷的零件："),
           (0, -1.75), MITTEL, "center")
    s.text(None, "P(@{defekt} | @{alarm}) = 99/594 = 1/6 ≈ 16.7 %", (0, -2.2), MITTEL, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k4dichte():
    s = Szene("ml/k4dichte")
    s.welt()
    t1 = s.tr("pmf", "(a) Wahrscheinlichkeitsfunktion", "(a) probability mass function", "(a) función de probabilidad", "(a) 概率质量函数")
    t2 = s.tr("dichte", "(b) Dichte", "(b) density", "(b) densidad", "(b) 概率密度")
    a = s.achsen((-0.6, 3.6), (0, 0.45), breite=2.2, hoehe=2.0, mitte=(-1.65, -0.1), xl="x", yl="P(X = x)", xticks="0;1;2;3",
                 yticks="0.125;0.25;0.375")
    s.stems(a, (0, 1, 2, 3), (0.125, 0.375, 0.375, 0.125), farbe=BLAU, dicke=5, r=0.08)
    s.text(None, t1, (-1.65, 1.65), KLEIN, "center")
    ts = s.tr("ts", "t in s", "t in s", "t en s", "t / s")
    b = s.achsen((-0.15, 0.65), (0, 2.5), breite=2.2, hoehe=2.0, mitte=(1.95, -0.1), xl="@{ts}", yl="p(t) in 1/s", xticks="0;0.1;0.3;0.5",
                 yticks="1;2")
    s.band(b, 0.1, 0.3, 0, 2, farbe=BLAU, deckung=0.25)
    zug(s, b, [(-0.15, 0), (0, 0), (0, 2), (0.5, 2), (0.5, 0), (0.65, 0)], farbe=BLAU, dicke=5)
    s.text(b, s.tr("flaeche", "Fläche\n0.4", "area\n0.4", "área\n0.4", "面积\n0.4"), (0.2, 1.0), KLEIN, "center")
    s.text(None, t2, (1.95, 1.65), KLEIN, "center")
    s.speichern()


def k4vertfkt():
    s = Szene("ml/k4vertfkt")
    s.welt()
    t1 = s.tr("koepfe", "(a) Anzahl der Köpfe", "(a) number of heads", "(a) número de caras", "(a) 正面朝上的次数")
    t2 = s.tr("eintreff", "(b) Eintreffzeitpunkt", "(b) arrival time", "(b) instante de llegada", "(b) 到达时刻")
    a = s.achsen((-1, 4), (0, 1.1), breite=2.2, hoehe=2.0, mitte=(-1.65, -0.1), xl="x", yl="F(x)", xticks="0;1;2;3",
                 yticks="0.125;0.5;0.875;1")
    stufen = ((-1, 0, 0), (0, 1, 0.125), (1, 2, 0.5), (2, 3, 0.875), (3, 4, 1))
    for x0, x1, y in stufen:
        s.linie(a, (x0, y), (x1, y), farbe=BLAU, dicke=5)
    for x, y0, y1 in ((0, 0, 0.125), (1, 0.125, 0.5), (2, 0.5, 0.875), (3, 0.875, 1)):
        s.punkt(a, x, y0, farbe=BLAU, r=0.065)             # offener Kreis: blauer Punkt mit weißem Kern
        s.punkt(a, x, y0, farbe="#ffffff", r=0.038)
        s.punkt(a, x, y1, farbe=BLAU, r=0.065)
    s.text(None, t1, (-1.65, 1.65), KLEIN, "center")
    ts = s.tr("ts", "t in s", "t in s", "t en s", "t / s")
    b = s.achsen((-0.15, 0.65), (0, 1.1), breite=2.2, hoehe=2.0, mitte=(1.95, -0.1), xl="@{ts}", yl="F(t)", xticks="0;0.1;0.3;0.5",
                 yticks="0.2;0.6;1")
    zug(s, b, [(-0.15, 0), (0, 0), (0.5, 1), (0.65, 1)], farbe=BLAU, dicke=5)
    zug(s, b, [(0.1, 0), (0.1, 0.2), (-0.15, 0.2)], farbe=GRAU, dicke=2, dash=DASH)
    zug(s, b, [(0.3, 0), (0.3, 0.6), (-0.15, 0.6)], farbe=GRAU, dicke=2, dash=DASH)
    s.text(None, t2, (1.95, 1.65), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 8
def k4normal():
    s = Szene("ml/k4normal")
    a = s.achsen((-4, 4), (0, 0.46), breite=6.2, hoehe=2.8, mitte=(0, 0.1), xticks="-3;-2;-1;0;1;2;3", xzahlen=False, yticks="",
                 yzahlen=False, ymarks=False, yl="p(x)")
    f = "exp(-x^2/2)/sqrt(2*pi)"
    s.flaeche(a, f, -3, 3, farbe=BLAU, deckung=0.12)
    s.flaeche(a, f, -2, 2, farbe=BLAU, deckung=0.18)
    s.flaeche(a, f, -1, 1, farbe=BLAU, deckung=0.25)
    s.kurve(a, f, farbe=BLAU, dicke=5)
    for x, t in ((-3, "μ−3σ"), (-2, "μ−2σ"), (-1, "μ−σ"), (0, "μ"), (1, "μ+σ"), (2, "μ+2σ"), (3, "μ+3σ")):
        s.text(a, t, (x, -0.035), KLEIN, "center")
    for k, y, t in ((1, 0.30, "68.3 %"), (2, 0.11, "95.4 %"), (3, 0.03, "99.7 %")):
        s.pfeil((-k, y), (k, y), on=a, dicke=2.5, spitze=0.12, doppelt=True)
        s.text(a, t, (0, y + 0.03), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 10
def k4streu():
    s = Szene("ml/k4streu")
    s.welt()
    wolken = heft_punkte("fig:k4streu")
    titel = ("(a) ρ = −0.9", "(b) ρ = 0", "(c) ρ = 0.5", "(d) ρ = 0.9", "(e) Y = X², ρ = 0", "(f) Y = ±X, ρ = 0")
    bereiche = [((-3, 3), (-3, 3))] * 4 + [((-1.2, 1.2), (-0.15, 1.15)), ((-2.4, 2.4), (-2.4, 2.4))]
    for k, (pts, t, (xr, yr)) in enumerate(zip(wolken, titel, bereiche)):
        mx, my = -2.35 + 2.35 * (k % 3), 0.95 - 2.55 * (k // 3)
        a = s.achsen(xr, yr, breite=1.9, hoehe=1.9, mitte=(mx, my), xticks="", yticks="", xzahlen=False, yzahlen=False,
                     xmarks=False, ymarks=False, rahmen=True)
        farbe = BLAU if k < 4 else ROT
        for x, y in pts:
            s.punkt(a, x, y, farbe=farbe, r=0.035)
        s.text(None, t, (mx, my + 1.2), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 12
def _ellipse_fx(c):
    return ("1+%g*(sqrt(3)*cos(t)+sin(t))/sqrt(2)" % c, "2+%g*(sqrt(3)*cos(t)-sin(t))/sqrt(2)" % c)


def k4ellipsen():
    s = Szene("ml/k4ellipsen")
    s.welt()
    t1 = s.tr("hoehen", "(a) Höhenlinien und Hauptachsen", "(a) contours and principal axes", "(a) curvas de nivel y ejes principales",
              "(a) 等高线与主轴")
    t2 = s.tr("bed", "(b) Bedingen auf x₂ = 4", "(b) conditioning on x₂ = 4", "(b) condicionar a x₂ = 4", "(b) 以 x₂ = 4 为条件")
    pts = heft_punkte("fig:k4ellipsen", r"mark size=0.9pt\] coordinates \{(.*?)\};")[0]
    for k, mx in enumerate((-1.8, 1.8)):
        a = s.achsen((-3, 5), (-2, 6), breite=2.5, hoehe=2.5, mitte=(mx, -0.2), xl="x₁", yl="x₂", xticks="-2;0;2;4", yticks="-2;0;2;4;6",
                     xl_mitte=False)
        if k == 0:
            for x, y in pts:
                s.punkt(a, x, y, farbe=GRAU, r=0.03)
        fx, fy = _ellipse_fx(1)
        s.weg(a, fx, fy, 0, 2 * math.pi, farbe=BLAU, dicke=4)
        fx, fy = _ellipse_fx(2)
        s.weg(a, fx, fy, 0, 2 * math.pi, farbe=BLAU, dicke=3, dash=DASH)
        if k == 0:
            s.pfeil((1, 2), (2.2247, 3.2247), on=a, farbe=ROT, dicke=4, spitze=0.13)
            s.pfeil((1, 2), (1.7071, 1.2929), on=a, farbe=GRUEN, dicke=4, spitze=0.13)
            s.text(a, "√3 q₁", (4.9, 4.6), KLEIN, "right", ROT)
            s.linie(a, (2.3, 3.3), (3.4, 4.3), farbe=ROT, dicke=1.5)
            s.text(a, "q₂", (3.0, 0.2), KLEIN, "left", GRUEN)
            s.linie(a, (1.8, 1.2), (2.95, 0.4), farbe=GRUEN, dicke=1.5)
        else:
            s.linie(a, (-0.5, -1), (4, 8), farbe=GRAU, dicke=3)
            s.linie(a, (-3, 4), (5, 4), farbe=SCHWARZ, dicke=3)
            s.linie(a, (0.7753, 4), (3.2247, 4), farbe=ORANGE, dicke=8)
            s.punkt(a, 2, 4, r=0.06)
            s.punkt(a, 1, 2, r=0.06)
            s.text(a, "μ₁|₂ = 2", (3.4, 3.35), KLEIN, "left")
            s.text(a, "E[x₁ | x₂]", (2.9, 5.6), KLEIN, "left", GRAU)
        s.text(None, t1 if k == 0 else t2, (mx, 1.55), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 13
def k4lln():
    s = Szene("ml/k4lln")
    xl = s.tr("anzahl", "Anzahl n der Würfe", "number n of rolls", "número n de tiradas", "投掷次数 n")
    yl = s.tr("lauf", "laufender Mittelwert", "running mean", "media acumulada", "累计平均值")
    a = s.achsen((1, 10000), (1, 6), breite=6.0, hoehe=3.0, mitte=(0.25, 0.1), xl=xl, yl=yl, xlog=True, xticks="1;10;100;1000;10000",
                 yticks="1;2;3;3.5;4;5;6")
    s.kurve(a, "3.5+3.4157/sqrt(x)", farbe=GRAU, dicke=2, dash=DASH)
    s.kurve(a, "3.5-3.4157/sqrt(x)", farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (1, 3.5), (10000, 3.5), farbe=SCHWARZ, dicke=2)
    for pts, farbe in zip(heft_punkte("fig:k4lln", r"thick\] coordinates \{(.*?)\};"), (BLAU, ROT, GRUEN)):
        zug(s, a, pts, farbe=farbe, dicke=3)
    s.speichern()


def k4zgws():
    s = Szene("ml/k4zgws")
    s.welt()
    balken = heft_punkte("fig:k4zgws", r"draw=elblue\] coordinates \{(.*?)\};")
    for k, (pts, n) in enumerate(zip(balken, (1, 2, 3, 10))):
        mx, my = -1.85 + 3.7 * (k % 2), 0.95 - 2.3 * (k // 2)
        a = s.achsen((0.6, 6.4), (0, 0.8), breite=2.75, hoehe=1.45, mitte=(mx, my), xticks="1;2;3;4;5;6", yticks="0.4;0.8")
        s.stems(a, [p[0] for p in pts], [p[1] for p in pts], farbe=BLAU, dicke=2, marker="none", breite=0.8 / n)
        s.kurve(a, "exp(-(x-3.5)^2/(2*35/(12*%d)))/sqrt(2*pi*35/(12*%d))" % (n, n), farbe=ROT, dicke=3)
        s.text(None, "n = %d" % n, (mx, my + 0.95), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Rechenbilder (Summen, Produkte, Skalarprodukte)
# Je Rechenbeispiel im Haupttext, in dem eine Summe, ein Produkt oder ein Skalarprodukt mit Zahlen das Kernstück ist, ein
# Bild ml/k4r<name> (= \label{fig:k4r<name>} im Heft, dort dieselbe Rechnung als align*). Dezimalzahlen mit Punkt: s.formel
# schreibt sie je Sprache um. Alle Formeln bekommen dieselbe Schriftgröße (wie in ml_teil3.py): Die Höhe folgt aus den Maßen
# der gesetzten Formel im Glyphen-Cache des Exports; beim allerersten Bauen gilt der Schätzwert, nach dem Export ergibt ein
# zweiter Lauf die richtige Höhe.
_CACHE = Path(__file__).resolve().parent.parent / "tex_glyphen_cache.json"
EM = 0.245
SPALTE = 6.9


def _hoehe(tex, schaetzung):
    try:                                         # Formeln mit Dezimalzahlen stehen im Cache mit dem Komma der Sprache (de)
        cache = json.loads(_CACHE.read_text(encoding="utf-8"))["glyphs"]
        glyphen = cache.get(tex) or cache.get(re.sub(r"(\d)\.(\d+)(?!\d)", r"\1{,}\2", tex))
    except (OSError, ValueError, KeyError):
        glyphen = None
    if not glyphen:
        return schaetzung
    xs, ys = [], []
    for g in glyphen:
        a, b, c, d, e, f = g["m"]
        zahlen = [float(z) for z in re.findall(r"-?\d+(?:\.\d+)?", g["d"])]
        for x, y in zip(zahlen[0::2], zahlen[1::2]):
            xs.append(a * x + c * y + e)
            ys.append(b * x + d * y + f)
    breite, hoehe = max(xs) - min(xs), max(ys) - min(ys)
    em = min(EM, SPALTE * 1000 / breite)
    return round(em * hoehe / 1000, 3)


def _formel(name, tex, schaetzung=1.5):
    s = Szene("ml/" + name)
    s.formel(tex, hoehe=_hoehe(tex, schaetzung))
    s.speichern()


def _al(*zeilen):
    return r"\begin{aligned}" + r"\\".join(zeilen) + r"\end{aligned}"


def _sp(*zahlen):
    return r"\begin{pmatrix}" + r"\\".join(str(z) for z in zahlen) + r"\end{pmatrix}"


def k4rverkettung():                                     # 3.3
    _formel("k4rverkettung", _al(r"P(A_1\cap A_2\cap A_3)&=P(A_1)\,P(A_2\mid A_1)\,P(A_3\mid A_1\cap A_2)",
                                 r"&=\frac{8}{10}\cdot\frac{7}{9}\cdot\frac{6}{8}=\frac{8\cdot7\cdot6}{10\cdot9\cdot8}"
                                 r"=\frac{336}{720}=\frac{7}{15}"), 1.1)


def k4rtotal():                                          # 3.4
    _formel("k4rtotal", _al(r"P(A)=\sum_{i=1}^2P(A\mid B_i)\,P(B_i)&=P(A\mid B_1)\,P(B_1)+P(A\mid B_2)\,P(B_2)",
                            r"&=0.01\cdot0.6+0.03\cdot0.4", r"&=0.006+0.012", r"&=0.018"), 1.6)


def k4rbayes():                                          # 4.2
    _formel("k4rbayes", _al(r"P(W)=P(W\mid D)\,P(D)+P(W\mid D^{\mathrm c})\,P(D^{\mathrm c})&=0.99\cdot0.01+0.05\cdot0.99",
                            r"&=0.0099+0.0495=0.0594",
                            r"P(D\mid W)=\frac{P(W\mid D)\,P(D)}{P(W)}&=\frac{0.0099}{0.0594}=\frac{1}{6}\approx0.167"), 1.4)


def k4rmuenzen():                                        # 7.1: Skalarprodukt Wertevektor mal Wahrscheinlichkeitsvektor
    s = Szene("ml/k4rmuenzen")                           # Darstellung "rechnung": wie das align* im Heft (Vektoren, dann Summe)
    s.skalarprodukt([0, 1, 2, 3], [0.125, 0.375, 0.375, 0.125], namen=("v", "p"), index="k", summanden=4)
    s.speichern()


def k4rwuerfel():                                        # 7.1
    _formel("k4rwuerfel", _al(r"\mathbb E[X]=\sum_{k=1}^6k\,P(X=k)&=1\cdot\tfrac16+2\cdot\tfrac16+3\cdot\tfrac16+4\cdot\tfrac16"
                              r"+5\cdot\tfrac16+6\cdot\tfrac16",
                              r"&=\tfrac{1+2+3+4+5+6}{6}=\tfrac{21}{6}=3.5"), 1.0)


def k4rquadrat():                                        # 7.2
    _formel("k4rquadrat", _al(r"\mathbb E[X^2]=\sum_{k=1}^6k^2\,P(X=k)&=1^2\cdot\tfrac16+2^2\cdot\tfrac16+3^2\cdot\tfrac16"
                              r"+4^2\cdot\tfrac16+5^2\cdot\tfrac16+6^2\cdot\tfrac16",
                              r"&=\tfrac{1+4+9+16+25+36}{6}=\tfrac{91}{6}\approx15.17"), 1.0)


def k4rvarianz():                                        # 7.4
    _formel("k4rvarianz", _al(r"\operatorname{Var}(X)=\sum_{k=1}^6(k-\mu)^2\,P(X=k)&=(1-3.5)^2\cdot\tfrac16+(2-3.5)^2\cdot\tfrac16"
                              r"+\dots+(6-3.5)^2\cdot\tfrac16",
                              r"&=\tfrac16\,\bigl(6.25+2.25+0.25+0.25+2.25+6.25\bigr)",
                              r"&=\tfrac{17.5}{6}=\tfrac{35}{12}\approx2.917"), 1.4)


def k4rkovarianz():                                      # 10.1
    _formel("k4rkovarianz", _al(r"\mathbb E[SR]=\sum_{s=0}^1\sum_{r=0}^1s\,r\,P(S=s,R=r)&=0\cdot0\cdot0.5+0\cdot1\cdot0.1"
                                r"+1\cdot0\cdot0.1+1\cdot1\cdot0.3",
                                r"&=0+0+0+0.3=0.3",
                                r"\operatorname{Cov}(S,R)=\mathbb E[SR]-\mathbb E[S]\,\mathbb E[R]&=0.3-0.4\cdot0.4=0.3-0.16=0.14"), 1.5)


AT = r"\tilde{\mathbf a}"
BT = r"\tilde{\mathbf b}"


def k4rdaten():                                          # 10.6
    _formel("k4rdaten", _al(r"&" + AT + "=" + _sp(-1, 0, 1) + r",\qquad " + BT + "=" + _sp(0, -1, 1),
                            r"\operatorname{cov}(\mathbf a,\mathbf b)=\frac13\sum_{i=1}^3(a_i-\bar a)(b_i-\bar b)"
                            r"&=\tfrac13\,\bigl((-1)\cdot0+0\cdot(-1)+1\cdot1\bigr)=\tfrac13\,(0+0+1)=\tfrac13",
                            r"\operatorname{std}(\mathbf a)^2=\frac13\sum_{i=1}^3(a_i-\bar a)^2"
                            r"&=\tfrac13\,\bigl((-1)^2+0^2+1^2\bigr)=\tfrac13\,(1+0+1)=\tfrac23"), 2.0)


def k4rkovmatrix():                                      # 11.3
    _formel("k4rkovmatrix", _al(r"&\tilde{\mathbf X}=\begin{pmatrix}-1&0\\0&-1\\1&1\end{pmatrix}",
                                r"S_{jl}=\frac13\bigl(\tilde{\mathbf X}^\top\tilde{\mathbf X}\bigr)_{jl}&=\frac13\sum_{i=1}^3"
                                r"\tilde x_{ij}\,\tilde x_{il}",
                                r"S_{11}&=\tfrac13\,\bigl((-1)\cdot(-1)+0\cdot0+1\cdot1\bigr)=\tfrac13\,(1+0+1)=\tfrac23",
                                r"S_{12}&=\tfrac13\,\bigl((-1)\cdot0+0\cdot(-1)+1\cdot1\bigr)=\tfrac13\,(0+0+1)=\tfrac13",
                                r"S_{22}&=\tfrac13\,\bigl(0\cdot0+(-1)\cdot(-1)+1\cdot1\bigr)=\tfrac13\,(0+1+1)=\tfrac23"), 3.0)


def k4rrichtung():                                       # 11.5
    _formel("k4rrichtung", _al(r"&\mathbf S=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf u=\frac1{\sqrt2}"
                               + _sp(1, 1),
                               r"\mathbf u^\top\mathbf S\mathbf u=\sum_{j=1}^2\sum_{l=1}^2u_j\,S_{jl}\,u_l&=u_1S_{11}u_1+u_1S_{12}u_2"
                               r"+u_2S_{21}u_1+u_2S_{22}u_2",
                               r"&=\tfrac12\cdot\tfrac13\,(1\cdot2\cdot1+1\cdot1\cdot1+1\cdot1\cdot1+1\cdot2\cdot1)",
                               r"&=\tfrac16\,(2+1+1+2)=\tfrac66=1"), 2.6)


def k4rmahalanobis():                                    # 12.2
    _formel("k4rmahalanobis", _al(r"\Delta^2=\sum_{i=1}^2\frac{y_i^2}{\lambda_i}&=\frac{y_1^2}{\lambda_1}+\frac{y_2^2}{\lambda_2}",
                                  r"\Delta(\mathbf x_a)^2&=\frac{(1.5\sqrt2)^2}{3}+\frac{0^2}{1}=\frac{4.5}{3}+0=1.5",
                                  r"\Delta(\mathbf x_b)^2&=\frac{0^2}{3}+\frac{(\sqrt2)^2}{1}=0+\frac{2}{1}=2"), 2.0)


RECHENBILDER = (k4rverkettung, k4rtotal, k4rbayes, k4rmuenzen, k4rwuerfel, k4rquadrat, k4rvarianz, k4rkovarianz, k4rdaten,
                k4rkovmatrix, k4rrichtung, k4rmahalanobis)

SZENEN = (k4baum, k4dichte, k4vertfkt, k4normal, k4streu, k4ellipsen, k4lln, k4zgws) + RECHENBILDER

for f in SZENEN:
    f()
