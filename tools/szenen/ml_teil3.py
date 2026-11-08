"""Machine Learning Grundlagen 3 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap3_stufen.tex, kap3_stufen_b.tex): Abbildungen.

Szenenname ml/k3<name> = \\label{fig:k3<name>} im Heft. Stil wie tools/szenen/ml_teil2.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil3.py
Export: python tools/export_szenen.py ml/k3<name> ...   (jedes Bild höchstens 548 px breit)
Szenen mit mehreren Teilbildern rufen zuerst s.welt() auf: Danach sind Texte ohne on= in Szeneneinheiten.
Die Rechenbilder ml/k3r<name> zeigen eine Summe, ein Produkt oder ein Skalarprodukt Schritt für Schritt
(s.summe, s.produkt, s.skalarprodukt, s.formel; Beispiele in tools/szenen/beispiel_summen.py).
Die Zahlen prüft C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\rechnung_kap3.py.
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


def zug(s, on, pts, farbe=SCHWARZ, dicke=3, dash=""):
    """Linienzug in Datenkoordinaten."""
    return s.daten(on, pts, farbe=farbe, dicke=dicke, dash=dash)


# ------------------------------------------------------------------ Abschnitt 1
def k3sekante():
    s = Szene("ml/k3sekante")
    a = s.achsen((1, 3.2), (-2, 30), breite=5.6, hoehe=3.7, mitte=(0.2, 0), xl="x", yl="f(x)", xticks="1;1.5;2;2.5;3",
                 yticks="0;8;15.625;27")
    s.kurve(a, "x^3", x=(1, 3.15), farbe=BLAU, dicke=5)
    s.linie(a, (1.5, -1.5), (3.15, 29.85), farbe=ROT, dicke=3)
    s.linie(a, (1.5, 0.375), (3.15, 25.5375), farbe=ORANGE, dicke=3)
    s.linie(a, (1.5, 2), (3.15, 21.8), farbe=SCHWARZ, dicke=3, dash=DASH)
    s.punkt(a, 2, 8, farbe=SCHWARZ, r=0.07)
    s.punkt(a, 3, 27, farbe=ROT, r=0.07)
    s.punkt(a, 2.5, 15.625, farbe=ORANGE, r=0.07)
    s.tr("s1", "Sekante h = 1: Steigung 19", "secant h = 1: slope 19", "secante h = 1: pendiente 19", "割线 h = 1：斜率 19")
    s.tr("s2", "Sekante h = 0.5: Steigung 15.25", "secant h = 0.5: slope 15.25", "secante h = 0.5: pendiente 15.25",
         "割线 h = 0.5：斜率 15.25")
    s.tr("tg", "Tangente: Steigung 12", "tangent: slope 12", "tangente: pendiente 12", "切线：斜率 12")
    s.legende(a, [("f(x) = x³", BLAU, "-"), ("@{s1}", ROT, "-"), ("@{s2}", ORANGE, "-"), ("@{tg}", SCHWARZ, "--")], (1.1, 27.5))
    s.speichern()


def k3lupe():
    s = Szene("ml/k3lupe")
    s.welt()
    fenster = (((1, 3), (-5, 28), "1;2;3", ("x von 1 bis 3", "x from 1 to 3", "x de 1 a 3", "x 从 1 到 3")),
               ((1.9, 2.1), (6.7, 9.4), "1.9;2;2.1", ("x von 1.9 bis 2.1", "x from 1.9 to 2.1", "x de 1.9 a 2.1", "x 从 1.9 到 2.1")),
               ((1.99, 2.01), (7.87, 8.13), "1.99;2;2.01",
                ("x von 1.99 bis 2.01", "x from 1.99 to 2.01", "x de 1.99 a 2.01", "x 从 1.99 到 2.01")))
    for k, (xr, yr, ticks, worte) in enumerate(fenster):
        mx = -2.4 + 2.4 * k
        a = s.achsen(xr, yr, breite=1.85, hoehe=1.9, mitte=(mx, -0.1), xticks=ticks, yticks="", yzahlen=False, ymarks=False)
        s.kurve(a, "x^3", farbe=BLAU, dicke=5)
        s.kurve(a, "8+12*(x-2)", farbe=ROT, dicke=3, dash=DASH)
        s.punkt(a, 2, 8, farbe=SCHWARZ, r=0.06)
        s.text(None, s.tr("t%d" % k, *worte), (mx, 1.3), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k3getriebe():
    s = Szene("ml/k3getriebe")
    m = 12.0                                     # Szeneneinheiten je Zahleneinheit, auf allen drei Strahlen gleich
    x0 = -1.2
    zeilen = ((1.2, "x", 0.01, "1", "1.01", BLAU), (0.0, "u = 3x + 1", 0.03, "4", "4.03", ORANGE),
              (-1.2, "y = u²", 0.2409, "16", "16.2409", ROT))
    for y, name, d, a_, b_, farbe in zeilen:
        s.linie(None, (-1.9, y), (3.4, y), farbe=HELLGRAU, dicke=2)
        s.text(None, name, (-2.05, y), MITTEL, "right")
        s.linie(None, (x0, y), (x0 + m * d, y), farbe=farbe, dicke=8)
        s.text(None, a_, (x0 - 0.08, y + 0.3), KLEIN, "right")
        s.text(None, b_, (x0 + m * d + 0.08, y + 0.3), KLEIN, "left")
    s.linie(None, (x0, 1.2), (x0, -1.2), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(None, (x0 + m * 0.01, 1.2), (x0 + m * 0.03, 0.0), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(None, (x0 + m * 0.03, 0.0), (x0 + m * 0.2409, -1.2), farbe=GRAU, dicke=2, dash=DASH)
    s.text(None, s.tr("st1", "Stufe 1: Faktor 3", "stage 1: factor 3", "etapa 1: factor 3", "第 1 级：因子 3"), (0.75, 0.62), KLEIN, "left")
    s.text(None, s.tr("st2", "Stufe 2: Faktor 8", "stage 2: factor 8", "etapa 2: factor 8", "第 2 级：因子 8"), (1.75, -0.58), KLEIN, "left")
    s.text(None, s.tr("zus", "zusammen: Δy ≈ 8 · 3 · Δx = 24 · 0.01 = 0.24", "together: Δy ≈ 8 · 3 · Δx = 24 · 0.01 = 0.24",
                      "en total: Δy ≈ 8 · 3 · Δx = 24 · 0.01 = 0.24", "合计：Δy ≈ 8 · 3 · Δx = 24 · 0.01 = 0.24"), (0.6, -1.95), KLEIN, "center")
    s.speichern()


def k3logistisch():
    s = Szene("ml/k3logistisch")
    a = s.achsen((-6, 6), (0, 1.05), breite=6.0, hoehe=3.0, mitte=(0, 0), xl="x", xticks="-6;-4;-2;0;2;4;6", yticks="0;0.25;0.5;0.75;1")
    s.kurve(a, "1/(1+exp(-x))", farbe=BLAU, dicke=5)
    s.kurve(a, "exp(-x)/(1+exp(-x))^2", farbe=ROT, dicke=5)
    s.linie(a, (0, 0), (0, 0.5), farbe=GRAU, dicke=2, dash=DASH)
    for x, y, f in ((0, 0.5, BLAU), (0, 0.25, ROT), (2, 0.8808, BLAU), (2, 0.105, ROT)):
        s.punkt(a, x, y, farbe=f, r=0.07)
    s.legende(a, [("σ(x)", BLAU, "-"), ("σ'(x) = σ(x) (1 − σ(x))", ROT, "-")], (-5.7, 0.95))
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3
def k3schnitt():
    s = Szene("ml/k3schnitt")
    s.welt()
    t1 = s.tr("ta", "(a) Höhenlinien", "(a) contour lines", "(a) curvas de nivel", "(a) 等高线")
    t2 = s.tr("tb", "(b) Schnitt x₂ = 2", "(b) section x₂ = 2", "(b) corte x₂ = 2", "(b) 截线 x₂ = 2")
    t3 = s.tr("tc", "(c) Schnitt x₁ = 1", "(c) section x₁ = 1", "(c) corte x₁ = 1", "(c) 截线 x₁ = 1")
    st = s.tr("st", "Steigung", "slope", "pendiente", "斜率")
    a = s.achsen((-2, 2), (0, 3.5), breite=1.55, hoehe=1.75, mitte=(-2.35, -0.05), xl="x₁", yl="x₂", xticks="-2;0;2", yticks="1;2;3")
    for c in (2, 4, 8, 10):
        s.kurve(a, "(sqrt(x^4+4*%d)-x^2)/2" % c, farbe=HELLGRAU, dicke=3)
    s.kurve(a, "(sqrt(x^4+24)-x^2)/2", farbe=SCHWARZ, dicke=3)
    s.linie(a, (-2, 2), (2, 2), farbe=BLAU, dicke=4)
    s.linie(a, (1, 0), (1, 3.5), farbe=ROT, dicke=4)
    s.punkt(a, 1, 2, farbe=SCHWARZ, r=0.06)
    s.text(a, "f = 6", (-1.9, 2.75), KLEIN, "left")
    s.text(None, t1, (-2.35, 1.4), KLEIN, "center")
    b = s.achsen((-0.5, 2), (2, 13), breite=1.55, hoehe=1.75, mitte=(0.1, -0.05), xl="x₁", xticks="0;1;2", yticks="4;8;12")
    s.kurve(b, "2*x^2+4", farbe=BLAU, dicke=4)
    s.kurve(b, "6+4*(x-1)", x=(0, 2), farbe=SCHWARZ, dicke=3, dash=DASH)
    s.punkt(b, 1, 6, farbe=SCHWARZ, r=0.06)
    s.text(b, "@{st} 4", (1.1, 4.4), KLEIN, "left")
    s.text(None, t2, (0.1, 1.4), KLEIN, "center")
    c_ = s.achsen((0.5, 3), (0, 13), breite=1.55, hoehe=1.75, mitte=(2.5, -0.05), xl="x₂", xticks="1;2;3", yticks="6;12")
    s.kurve(c_, "x+x^2", farbe=ROT, dicke=4)
    s.kurve(c_, "6+5*(x-2)", x=(1, 3), farbe=SCHWARZ, dicke=3, dash=DASH)
    s.punkt(c_, 2, 6, farbe=SCHWARZ, r=0.06)
    s.text(c_, "@{st} 5", (2.1, 3.6), KLEIN, "left")
    s.text(None, t3, (2.5, 1.4), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k3hoehen():
    s = Szene("ml/k3hoehen")
    s.welt()
    a = s.achsen((-2.05, 2.05), (-2.3, 2.3), breite=2.17, hoehe=2.44, mitte=(-2.1, 0.15), kreuz=True, xticks="", yticks="",
                 xzahlen=False, yzahlen=False, xl="x₁", yl="x₂")
    for r_ in (0.7071, 1.0, 1.4142, 1.7321):
        s.kreis(a, 0, 0, r_, farbe=HELLGRAU, dicke=2)
    for k in range(8):
        t = k * math.pi / 4
        p = (1.4142 * math.cos(t), 1.4142 * math.sin(t))
        s.pfeil(p, (1.3 * p[0], 1.3 * p[1]), on=a, farbe=ROT, dicke=3, spitze=0.12)
    s.punkt(a, 1, 1, farbe=SCHWARZ, r=0.06)
    s.pfeil((1, 1), (0.32, 0.32), on=a, farbe=BLAU, dicke=4, spitze=0.14)
    s.text(None, "(a) f(x) = x₁² + x₂²", (-2.1, -1.55), KLEIN, "center")
    b = s.achsen((-2.9, 2.9), (-2.1, 2.1), breite=3.07, hoehe=2.23, mitte=(1.55, 0.15), kreuz=True, xticks="", yticks="",
                 xzahlen=False, yzahlen=False, xl="x₁", yl="x₂")
    for c in (1, 2, 5, 8):
        s.weg(b, "%g*cos(t)" % math.sqrt(c), "%g*sin(t)" % (math.sqrt(c) / 2), 0, 2 * math.pi, farbe=HELLGRAU, dicke=2)
    for k in range(12):
        t = k * math.pi / 6
        p = (math.sqrt(5) * math.cos(t), math.sqrt(5) / 2 * math.sin(t))
        s.pfeil(p, (p[0] + 0.15 * p[0], p[1] + 0.6 * p[1]), on=b, farbe=ROT, dicke=3, spitze=0.12)
    s.punkt(b, 1, 1, farbe=SCHWARZ, r=0.06)
    s.linie(b, (1, 1), (0, 0), farbe=GRAU, dicke=2, dash=DASH)
    s.pfeil((1, 1), (0.835, 0.34), on=b, farbe=BLAU, dicke=4, spitze=0.14)
    s.text(None, "(b) f(x) = x₁² + 4x₂²", (1.55, -1.55), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Graphen (Abschnitte 6, 9, 10)
def _knoten(s, x, y, text, r=0.3, eckig=False, farbe=SCHWARZ):
    if eckig:
        s.box(text, (x, y), breite=2 * r, hoehe=2 * r * 0.85, form="round", groesse=MITTEL, farbe=farbe, dicke=2.5)
    else:
        s.kreis(None, x, y, r, farbe=farbe, dicke=2.5, fuellung="#ffffff", deckung=1)
        s.text(None, text, (x, y), MITTEL, "center")


def _kante(s, p, q, r1, r2, farbe=SCHWARZ, dicke=3):
    """Pfeil von Knoten p zu Knoten q, gekürzt um die Radien r1 und r2."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    a = (p[0] + dx * r1 / n, p[1] + dy * r1 / n)
    b = (q[0] - dx * r2 / n, q[1] - dy * r2 / n)
    s.pfeil(a, b, farbe=farbe, dicke=dicke, spitze=0.16)


def _etikett(s, p, q, t, anteil=0.5, farbe=SCHWARZ, groesse=KLEIN):
    m = (p[0] + anteil * (q[0] - p[0]), p[1] + anteil * (q[1] - p[1]))
    s.box(t, m, form="rect", groesse=groesse, farbe=farbe, dicke=0)


def k3wege():
    s = Szene("ml/k3wege")
    P = {"x1": (-2.9, 1.1), "x2": (-2.9, -1.1), "u1": (0.0, 1.1), "u2": (0.0, -1.1), "F": (2.9, 0.0)}
    for k in ("x1", "x2", "u1", "u2", "F"):
        _knoten(s, *P[k], {"x1": "x₁", "x2": "x₂", "u1": "u₁", "u2": "u₂", "F": "F"}[k])
    kanten = (("x1", "u1", "2", BLAU, 4, 0.5), ("x1", "u2", "2", ORANGE, 4, 0.27), ("x2", "u1", "1", GRAU, 2.5, 0.27),
              ("x2", "u2", "4", GRAU, 2.5, 0.5), ("u1", "F", "4", BLAU, 4, 0.5), ("u2", "F", "3", ORANGE, 4, 0.5))
    for a_, b_, t, farbe, d, anteil in kanten:
        _kante(s, P[a_], P[b_], 0.3, 0.3, farbe=farbe, dicke=d)
        _etikett(s, P[a_], P[b_], t, anteil)
    s.text(None, "u₁ = x₁x₂ = 2", (0.0, 1.65), KLEIN, "center")
    s.text(None, "u₂ = 2x₁ + x₂² = 6", (0.0, -1.65), KLEIN, "center")
    s.text(None, "F = u₁² + 3u₂", (2.9, 0.55), KLEIN, "center")
    s.text(None, "∂F/∂x₁ = 2 · 4 + 2 · 3 = 8 + 6 = 14", (0.0, -2.35), MITTEL, "center")
    s.speichern()


_GP = {"x1": (-2.2, 1.5), "x2": (-2.2, 0.0), "x3": (-2.2, -1.5), "v1": (0.3, 0.75), "v2": (0.3, -0.75), "f": (2.6, 0.0)}
_GK = (("x1", "v1"), ("x2", "v1"), ("x2", "v2"), ("x3", "v2"), ("v1", "f"), ("v2", "f"))


def _graph(s):
    for k in ("x1", "x2", "x3"):
        _knoten(s, *_GP[k], {"x1": "x₁", "x2": "x₂", "x3": "x₃"}[k], r=0.32, eckig=True)
    for k, op in (("v1", "+"), ("v2", "+"), ("f", "×")):
        _knoten(s, *_GP[k], op)
    for a_, b_ in _GK:
        _kante(s, _GP[a_], _GP[b_], 0.33, 0.3)


def k3graph():
    s = Szene("ml/k3graph")
    _graph(s)
    gw = "#00823c"
    for k, t in (("x1", "1"), ("x2", "2"), ("x3", "3")):
        s.text(None, t, (_GP[k][0] - 0.5, _GP[k][1]), MITTEL, "right", gw)
    s.text(None, "v₁", (0.3, 1.25), MITTEL, "center")
    s.text(None, "v₂", (0.3, -1.25), MITTEL, "center")
    s.text(None, "f", (2.6, 0.5), MITTEL, "center")
    s.text(None, "3", (0.7, 0.75), MITTEL, "left", gw)
    s.text(None, "5", (0.7, -0.75), MITTEL, "left", gw)
    s.text(None, "15", (3.0, 0.0), MITTEL, "left", gw)
    s.speichern()


def k3rueckwaerts():
    s = Szene("ml/k3rueckwaerts")
    _graph(s)
    gw = "#00823c"
    lok = (("x1", "v1", "1"), ("x2", "v1", "1"), ("x2", "v2", "1"), ("x3", "v2", "1"), ("v1", "f", "v₂ = 5"), ("v2", "f", "v₁ = 3"))
    for a_, b_, t in lok:
        _etikett(s, _GP[a_], _GP[b_], t, 0.45, farbe=GRAU, groesse=KLEIN)
    for k, w, adj in (("x1", "1", "x̄₁ = 5"), ("x2", "2", "x̄₂ = 8"), ("x3", "3", "x̄₃ = 3")):
        s.text(None, w, (_GP[k][0] - 0.5, _GP[k][1] + 0.17), MITTEL, "right", gw)
        s.text(None, adj, (_GP[k][0] - 0.5, _GP[k][1] - 0.2), MITTEL, "right", ROT)
    s.text(None, "3", (0.3, 1.25), MITTEL, "center", gw)
    s.text(None, "v̄₁ = 5", (0.3, 0.25), MITTEL, "center", ROT)
    s.text(None, "5", (0.3, -0.25), MITTEL, "center", gw)
    s.text(None, "v̄₂ = 3", (0.3, -1.25), MITTEL, "center", ROT)
    s.text(None, "15", (3.0, 0.25), MITTEL, "left", gw)
    s.text(None, "f̄ = 1", (3.0, -0.22), MITTEL, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 11
VOR = [(1.000e-01, 6.100e-01), (3.162e-02, 1.907e-01), (1.000e-02, 6.010e-02), (3.162e-03, 1.898e-02), (1.000e-03, 6.001e-03),
       (3.162e-04, 1.897e-03), (1.000e-04, 6.000e-04), (3.162e-05, 1.897e-04), (1.000e-05, 6.000e-05), (3.162e-06, 1.897e-05),
       (1.000e-06, 6.002e-06), (3.162e-07, 1.905e-06), (1.000e-07, 5.843e-07), (3.162e-08, 9.102e-08), (1.000e-08, 7.293e-08),
       (3.162e-09, 4.145e-07), (1.000e-09, 9.929e-07), (3.162e-10, 6.326e-06), (1.000e-10, 9.929e-07), (3.162e-11, 2.738e-05),
       (1.000e-11, 9.929e-07), (3.162e-12, 3.097e-04), (1.000e-12, 1.067e-03), (3.162e-13, 1.376e-03), (1.000e-13, 9.591e-03),
       (3.162e-14, 3.508e-02), (1.000e-14, 2.569e-01), (3.162e-15, 2.036e-01), (1.000e-15, 1.342e+00)]
ZEN = [(1.000e-01, 1.000e-02), (3.162e-02, 1.000e-03), (1.000e-02, 1.000e-04), (3.162e-03, 1.000e-05), (1.000e-03, 1.000e-06),
       (3.162e-04, 1.000e-07), (1.000e-04, 1.001e-08), (3.162e-05, 1.031e-09), (1.000e-05, 2.118e-10), (3.162e-06, 1.992e-11),
       (1.000e-06, 7.892e-10), (3.162e-07, 2.548e-09), (1.000e-07, 6.316e-09), (3.162e-08, 4.941e-08), (1.000e-08, 1.173e-07),
       (3.162e-09, 4.145e-07), (1.000e-09, 9.929e-07), (3.162e-10, 2.113e-06), (1.000e-10, 9.929e-07), (3.162e-11, 2.738e-05),
       (1.000e-11, 9.929e-07), (3.162e-12, 3.097e-04), (1.000e-12, 1.067e-03), (3.162e-13, 1.376e-03), (1.000e-13, 9.591e-03),
       (3.162e-14, 3.508e-02), (1.000e-14, 1.236e-01), (3.162e-15, 2.036e-01), (1.000e-15, 9.591e-03)]


def k3vkurve():
    s = Szene("ml/k3vkurve")
    hl = s.tr("hl", "Schrittweite h", "step size h", "paso h", "步长 h")
    fl = s.tr("fl", "Fehler", "error", "error", "误差")
    a = s.achsen((1e-15, 0.1), (1e-12, 10), breite=5.6, hoehe=3.6, mitte=(0.3, 0.1), xl=hl, yl=fl, xlog=True, ylog=True,
                 xticks="1e-15;1e-12;1e-9;1e-6;1e-3", yticks="1e-12;1e-9;1e-6;1e-3;1")
    s.kurve(a, "6*x+1.776/(10^15*x)", farbe=ROT, dicke=3, dash=DASH)
    s.kurve(a, "x^2+0.8882/(10^15*x)", farbe=BLAU, dicke=3, dash=DASH)
    for h, e in VOR:
        s.punkt(a, h, e, farbe=ROT, r=0.05)
    for h, e in ZEN:
        s.punkt(a, h, max(e, 1e-12), farbe=BLAU, r=0.05)
    s.tr("vg", "Vorwärtsdifferenz", "forward difference", "diferencia progresiva", "前向差分")
    s.tr("zg", "zentrale Differenz", "central difference", "diferencia central", "中心差分")
    s.tr("ab", "Abschätzungen", "estimates", "estimaciones", "估计")
    s.legende(a, [("@{vg}", ROT, "o"), ("@{zg}", BLAU, "o"), ("@{ab}", GRAU, "--")], (2e-15, 2e-8))
    s.speichern()


# ------------------------------------------------------------------ Rechenbilder (Summen, Skalarprodukte)
# Je Rechenbeispiel im Haupttext, in dem eine Summe oder ein Skalarprodukt mit Zahlen das Kernstück ist, ein Bild ml/k3r<name>
# (= \label{fig:k3r<name>} im Heft, dort dieselbe Rechnung als align*). Dezimalzahlen mit Punkt: s.formel schreibt sie je
# Sprache um. Alle Formeln bekommen dieselbe Schriftgröße (wie in ml_teil1.py): Die Höhe folgt aus den Maßen der gesetzten
# Formel im Glyphen-Cache des Exports; beim allerersten Bauen gilt der Schätzwert, nach dem Export ergibt ein zweiter Lauf
# die richtige Höhe.
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


NF = r"\nabla f(\mathbf x)"


def k3rtaylor1():                                        # 1.5
    _formel("k3rtaylor1", _al(r"f(2+h)&\approx f(2)+f'(2)\,h+\tfrac12f''(2)\,h^2",
                              r"&=8+12\cdot0.01+\tfrac12\cdot12\cdot0.01^2",
                              r"&=8+0.12+0.0006",
                              r"&=8.1206"), 1.6)


def k3rlinear():                                         # 3.4
    _formel("k3rlinear", _al(r"&" + NF + "=" + _sp(4, 5) + r",\qquad \mathbf h=" + _sp(0.01, 0.02),
                             NF + r"^\top\mathbf h&=\sum_{j=1}^2\partial_jf(\mathbf x)\,h_j=\partial_1f(\mathbf x)\,h_1+\partial_2f(\mathbf x)\,h_2",
                             r"&=4\cdot0.01+5\cdot0.02",
                             r"&=0.04+0.10",
                             r"&=0.14"), 2.4)


def k3rrichtung():                                       # 4.1
    _formel("k3rrichtung", _al(r"&" + NF + "=" + _sp(4, 5) + r",\qquad \mathbf u=" + _sp(0.6, 0.8),
                               r"D_{\mathbf u}f(\mathbf x)=" + NF + r"^\top\mathbf u&=\sum_{j=1}^2\partial_jf(\mathbf x)\,u_j"
                               r"=\partial_1f(\mathbf x)\,u_1+\partial_2f(\mathbf x)\,u_2",
                               r"&=4\cdot0.6+5\cdot0.8",
                               r"&=2.4+4.0",
                               r"&=6.4"), 2.4)


JG = r"\mathbf J_{\mathbf g}(\mathbf x)"


def k3rjacobi():                                         # 5.3
    _formel("k3rjacobi", _al(r"&" + JG + r"=\begin{pmatrix}2&1\\2&4\end{pmatrix},\qquad \mathbf h=" + _sp(0.1, -0.1),
                             r"\bigl(" + JG + r"\,\mathbf h\bigr)_i&=\sum_{j=1}^2\frac{\partial g_i}{\partial x_j}(\mathbf x)\,h_j",
                             r"\bigl(" + JG + r"\,\mathbf h\bigr)_1&=2\cdot0.1+1\cdot(-0.1)=0.2-0.1=0.1",
                             r"\bigl(" + JG + r"\,\mathbf h\bigr)_2&=2\cdot0.1+4\cdot(-0.1)=0.2-0.4=-0.2"), 2.3)


def k3rwege():                                           # 6.2
    t = lambda j: (r"\frac{\partial F}{\partial x_%d}&=\sum_{i=1}^2\frac{\partial f}{\partial u_i}\,\frac{\partial u_i}{\partial x_%d}"
                   r"=\frac{\partial f}{\partial u_1}\,\frac{\partial u_1}{\partial x_%d}+\frac{\partial f}{\partial u_2}\,"
                   r"\frac{\partial u_2}{\partial x_%d}") % (j, j, j, j)
    _formel("k3rwege", _al(t(1), r"&=4\cdot2+3\cdot2=8+6=14", t(2), r"&=4\cdot1+3\cdot4=4+12=16"), 2.6)


def k3rresiduum():                                       # 7.4
    _formel("k3rresiduum", _al(r"&\mathbf A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad \mathbf r=\mathbf y-\mathbf A\mathbf x=" + _sp(-3, -1),
                               r"(\mathbf A^\top\mathbf r)_j&=\sum_{i=1}^2a_{ij}\,r_i",
                               r"(\mathbf A^\top\mathbf r)_1&=1\cdot(-3)+0\cdot(-1)=-3+0=-3",
                               r"(\mathbf A^\top\mathbf r)_2&=2\cdot(-3)+1\cdot(-1)=-6-1=-7",
                               r"\nabla f(\mathbf x)&=-2\,\mathbf A^\top\mathbf r=" + _sp(6, 14)), 3.0)


def k3rrueck():                                          # 7.6
    NY = r"\nabla f(\mathbf y)"
    _formel("k3rrueck", _al(r"&\mathbf A=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix},\qquad " + NY + "=" + _sp(1, 0, -1),
                            r"\bigl(\mathbf A^\top" + NY + r"\bigr)_j&=\sum_{i=1}^3a_{ij}\,\frac{\partial f}{\partial y_i}",
                            r"\bigl(\mathbf A^\top" + NY + r"\bigr)_1&=1\cdot1+0\cdot0+3\cdot(-1)=1+0-3=-2",
                            r"\bigl(\mathbf A^\top" + NY + r"\bigr)_2&=2\cdot1+(-1)\cdot0+1\cdot(-1)=2+0-1=1"), 2.6)


HF = r"\mathbf H_f(\mathbf x)"


def k3rtaylor2():                                        # 8.4
    _formel("k3rtaylor2", _al(r"&" + HF + r"=\begin{pmatrix}4&2\\2&2\end{pmatrix},\qquad \mathbf h=" + _sp(0.01, 0.02),
                              r"\tfrac12\,\mathbf h^\top" + HF + r"\,\mathbf h&=\tfrac12\sum_{i=1}^2\sum_{j=1}^2h_i\,"
                              r"\frac{\partial^2f}{\partial x_i\,\partial x_j}\,h_j",
                              r"&=\tfrac12\bigl(4\cdot0.01^2+2\cdot2\cdot0.01\cdot0.02+2\cdot0.02^2\bigr)",
                              r"&=\tfrac12\,(0.0004+0.0008+0.0008)",
                              r"&=0.001"), 3.0)


def k3rkruemmung():                                      # 8.5
    _formel("k3rkruemmung", _al(r"&" + HF + r"=\begin{pmatrix}4&2\\2&2\end{pmatrix},\qquad \mathbf u=\frac1{\sqrt2}" + _sp(1, 1),
                                r"\mathbf u^\top" + HF + r"\,\mathbf u&=\sum_{i=1}^2\sum_{j=1}^2u_i\,"
                                r"\frac{\partial^2f}{\partial x_i\,\partial x_j}\,u_j",
                                r"&=\tfrac12\,(1\cdot4\cdot1+1\cdot2\cdot1+1\cdot2\cdot1+1\cdot2\cdot1)",
                                r"&=\tfrac12\,(4+2+2+2)",
                                r"&=5"), 3.0)


def k3rvierfaktoren():                                   # 9.1
    _formel("k3rvierfaktoren", _al(r"p'(0)&=\sum_{k=1}^4\ \prod_{l\ne k}(0+l)=2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3",
                                   r"&=24+12+8+6",
                                   r"&=50"), 1.3)


RECHENBILDER = (k3rtaylor1, k3rlinear, k3rrichtung, k3rjacobi, k3rwege, k3rresiduum, k3rrueck, k3rtaylor2, k3rkruemmung,
                k3rvierfaktoren)

SZENEN = (k3sekante, k3lupe, k3getriebe, k3logistisch, k3schnitt, k3hoehen, k3wege, k3graph, k3rueckwaerts, k3vkurve) + RECHENBILDER

for f in SZENEN:
    f()
