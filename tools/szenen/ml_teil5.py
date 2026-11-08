"""Machine Learning Grundlagen 5 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap5_stufen.tex, kap5_stufen_b.tex): Abbildungen.

Szenenname ml/k5<name> = \\label{fig:k5<name>} im Heft. Stil wie tools/szenen/ml_teil3.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil5.py
Export: python tools/export_szenen.py ml/k5<name> ...   (jedes Bild höchstens 548 px breit)
Szenen mit mehreren Teilbildern rufen zuerst s.welt() auf: Danach sind Texte ohne on= in Szeneneinheiten.
Die Rechenbilder ml/k5r<name> zeigen eine Summe, ein Produkt oder ein Skalarprodukt Schritt für Schritt
(s.skalarprodukt, s.formel; Beispiele in tools/szenen/beispiel_summen.py).
Die Zahlen prüft C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\rechnung_kap5.py; die Koordinaten der Zielscheibe,
der Stichprobenverteilung, der markierten Punkte und der Hilfslinien liest diese Datei aus dem Heft (dieselben Daten wie im PDF).
"""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24
HEFT = Path(r"C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte")


def zug(s, on, pts, farbe=SCHWARZ, dicke=3, dash=""):
    """Linienzug in Datenkoordinaten."""
    return s.daten(on, pts, farbe=farbe, dicke=dicke, dash=dash)


def _abb(label):
    tex = (HEFT / "kap5_stufen.tex").read_text(encoding="utf-8") + (HEFT / "kap5_stufen_b.tex").read_text(encoding="utf-8")
    ende = tex.index(r"\label{%s}" % label)
    return tex[tex.rfind(r"\begin{abb}", 0, ende):ende]


def heft_punkte(label):
    """Koordinatenlisten (coordinates {...}) der Abbildung \\label{label} aus dem Heft."""
    return [[tuple(float(z) for z in t.split(",")) for t in re.findall(r"\(([^()]*)\)", block)]
            for block in re.findall(r"coordinates \{(.*?)\};", _abb(label), re.S)]


def heft_senkrechte(label):
    """Senkrechte Hilfslinien (axis cs:x,0) -- (axis cs:x,y) der Abbildung als [(x, y)]."""
    return [(float(a), float(b)) for a, b in re.findall(r"\(axis cs:([-\d.]+),0\) -- \(axis cs:\1,([-\d.]+)\)", _abb(label))]


# ------------------------------------------------------------------ Abschnitt 1
def k5richtung():
    s = Szene("ml/k5richtung")
    kast = dict(form="round", groesse=MITTEL, dicke=2.5)
    vert = s.tr("vert", "Verteilung\nP(X = x | θ)", "distribution\nP(X = x | θ)", "distribución\nP(X = x | θ)", "分布\nP(X = x | θ)")
    dat = s.tr("dat", "Daten\nx₁, …, x_{N}", "data\nx₁, …, x_{N}", "datos\nx₁, …, x_{N}", "数据\nx₁, …, x_{N}")
    s.box(vert, (-2.35, 0), breite=2.1, hoehe=1.0, **kast)
    s.box(dat, (2.35, 0), breite=2.1, hoehe=1.0, **kast)
    s.pfeil((-1.25, 0.2), (1.25, 0.2), farbe=BLAU, dicke=4, spitze=0.16)
    s.pfeil((1.25, -0.2), (-1.25, -0.2), farbe=ROT, dicke=4, spitze=0.16)
    s.text(None, s.tr("wr", "Wahrscheinlichkeitsrechnung:\nWie wahrscheinlich sind diese Daten?",
                      "probability theory:\nhow probable are these data?", "teoría de la probabilidad:\n¿qué probabilidad tienen estos datos?",
                      "概率论：\n这些数据出现的概率有多大？"), (0, 1.15), KLEIN, "center", BLAU)
    s.text(None, s.tr("st", "Statistik:\nWelches θ hat die Daten erzeugt?", "statistics:\nwhich θ produced the data?",
                      "estadística:\n¿qué θ generó los datos?", "统计学：\n哪个 θ 产生了这些数据？"), (0, -1.15), KLEIN, "center", ROT)
    s.speichern()


def k5stichprobe():
    s = Szene("ml/k5stichprobe")
    s.welt()
    pkte = heft_punkte("fig:k5stichprobe")
    for k, (mx, farbe, key, worte, xl) in enumerate(((-1.75, BLAU, "ta", ("(a) ein Wert X", "(a) one value X", "(a) un valor X", "(a) 单个值 X"), "x"),
                                                    (1.85, ROT, "tb", ("(b) Mittelwert X̄ aus N = 2", "(b) mean X̄ of N = 2",
                                                                       "(b) media X̄ de N = 2", "(b) N = 2 的均值 X̄"), "x̄"))):
        a = s.achsen((0.5, 3.5), (0, 0.42), breite=2.75, hoehe=1.9, mitte=(mx, -0.15), xl=xl, yl="P" if k == 0 else "",
                     xticks="1;1.5;2;2.5;3", yticks="0.1;0.2;0.3")
        xs, ys = zip(*pkte[k])
        s.stems(a, xs, ys, farbe=farbe, dicke=5, r=0.08)
        s.text(None, s.tr(key, *worte), (mx, 1.25), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k5zielscheibe():
    s = Szene("ml/k5zielscheibe")
    s.welt()
    pkte = heft_punkte("fig:k5zielscheibe")
    titel = (("ta", "(a) unverzerrt,\nkleine Streuung", "(a) unbiased,\nsmall spread", "(a) insesgado,\npoca dispersión", "(a) 无偏，\n离散小"),
             ("tb", "(b) unverzerrt,\ngroße Streuung", "(b) unbiased,\nlarge spread", "(b) insesgado,\nmucha dispersión", "(b) 无偏，\n离散大"),
             ("tc", "(c) verzerrt,\nkleine Streuung", "(c) biased,\nsmall spread", "(c) sesgado,\npoca dispersión", "(c) 有偏，\n离散小"),
             ("td", "(d) verzerrt,\ngroße Streuung", "(d) biased,\nlarge spread", "(d) sesgado,\nmucha dispersión", "(d) 有偏，\n离散大"))
    r0 = 0.72
    for k in range(4):
        cx, cy = -2.7 + 1.8 * k, -0.25
        for rr in (1, 2 / 3, 1 / 3):
            s.kreis(None, cx, cy, r0 * rr, farbe=HELLGRAU, dicke=2)
        s.kreuzchen(None, cx, cy, farbe=ROT, groesse=0.16, dicke=3)
        for x, y in pkte[2 * k + 1]:
            s.punkt(None, cx + r0 * x, cy + r0 * y, farbe=BLAU, r=0.05)
        s.text(None, s.tr(*titel[k]), (cx, 0.95), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k5likelihood():
    s = Szene("ml/k5likelihood")
    s.welt()
    pk = heft_punkte("fig:k5likelihood")
    a = s.achsen((0, 1), (0, 2.6), breite=2.75, hoehe=2.1, mitte=(-1.8, -0.2), xl="θ", xticks="0.2;0.4;0.6;0.8;1", yticks="0.5;1;1.5;2;2.5")
    s.kurve(a, "1000*x^7*(1-x)^3", farbe=BLAU, dicke=5)
    (x7, y7), = pk[0]
    (x5, y5), = pk[1]
    s.linie(a, (x7, 0), (x7, y7), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, x7, y7, farbe=ROT, r=0.07)
    s.punkt(a, x5, y5, farbe=GRAU, r=0.07)
    s.text(None, s.tr("ta", "(a) ℒ(θ) in Tausendsteln", "(a) ℒ(θ) in thousandths", "(a) ℒ(θ) en milésimas", "(a) ℒ(θ)，单位千分之一"),
           (-1.8, 1.25), KLEIN, "center")
    b = s.achsen((0, 1), (-16, -4), breite=2.75, hoehe=2.1, mitte=(1.85, -0.2), xl="θ", xticks="0.2;0.4;0.6;0.8;1", yticks="-16;-12;-8;-4")
    s.kurve(b, "7*ln(x)+3*ln(1-x)", x=(0.16, 0.97), farbe=BLAU, dicke=5)
    (x7, y7), = pk[2]
    (x5, y5), = pk[3]
    s.linie(b, (x7, -16), (x7, y7), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(b, x7, y7, farbe=ROT, r=0.07)
    s.punkt(b, x5, y5, farbe=GRAU, r=0.07)
    s.text(None, "(b) ℓ(θ) = ln ℒ(θ)", (1.85, 1.25), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k5beta():
    s = Szene("ml/k5beta")
    a = s.achsen((0, 1), (0, 3.4), breite=5.6, hoehe=3.0, mitte=(0.2, 0), xl="θ", yl="p(θ)", xticks="0.2;0.4;0.6;0.8;1", yticks="1;2;3")
    for f, farbe in (("1+0*x", GRAU), ("6*x*(1-x)", BLAU), ("30*x^4*(1-x)", GRUEN), ("6435*x^8*(1-x)^4", ROT)):
        s.kurve(a, f, farbe=farbe, dicke=5)
    s.legende(a, [("Beta(1, 1)", GRAU, "-"), ("Beta(2, 2)", BLAU, "-"), ("Beta(5, 2)", GRUEN, "-"), ("Beta(9, 5)", ROT, "-")], (0.03, 3.3))
    s.speichern()


def k5posterior():
    s = Szene("ml/k5posterior")
    a = s.achsen((0, 1), (0, 3.5), breite=5.6, hoehe=3.0, mitte=(0.2, 0), xl="θ", xticks="0.2;0.4;0.6;0.8;1", yticks="1;2;3")
    s.kurve(a, "6*x*(1-x)", farbe=GRAU, dicke=4, dash=DASH)
    s.kurve(a, "1320*x^7*(1-x)^3", farbe=BLAU, dicke=5)
    s.kurve(a, "6435*x^8*(1-x)^4", farbe=ROT, dicke=5)
    for (x, y), farbe in zip(heft_senkrechte("fig:k5posterior"), (ROT, BLAU, SCHWARZ)):
        s.linie(a, (x, 0), (x, y), farbe=farbe, dicke=2, dash=DOT)
    s.tr("pri", "Prior Beta(2, 2)", "prior Beta(2, 2)", "prior Beta(2, 2)", "先验 Beta(2, 2)")
    s.tr("lik", "Likelihood · 1320", "likelihood · 1320", "verosimilitud · 1320", "似然 · 1320")
    s.tr("post", "Posterior Beta(9, 5)", "posterior Beta(9, 5)", "posterior Beta(9, 5)", "后验 Beta(9, 5)")
    s.legende(a, [("@{pri}", GRAU, "--"), ("@{lik}", BLAU, "-"), ("@{post}", ROT, "-")], (0.03, 3.4))
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 8
def k5code():
    s = Szene("ml/k5code")
    P = {"w": (-0.6, 1.7), "n1": (0.5, 0.7), "n2": (1.5, -0.3)}
    B = {"A": (-1.7, 0.7, "A: 0", "1/2"), "B": (-0.5, -0.3, "B: 10", "1/4"), "C": (0.5, -1.4, "C: 110", "1/8"), "D": (2.5, -1.4, "D: 111", "1/8")}
    kanten = (("w", "A", "0"), ("w", "n1", "1"), ("n1", "B", "0"), ("n1", "n2", "1"), ("n2", "C", "0"), ("n2", "D", "1"))
    pos = lambda k: P[k] if k in P else B[k][:2]
    for a_, b_, t in kanten:
        (xa, ya), (xb, yb) = pos(a_), pos(b_)
        yb2 = yb + (0.32 if b_ in B else 0)
        s.linie(None, (xa, ya), (xb, yb2), farbe=SCHWARZ, dicke=3)
        xm, ym = (xa + xb) / 2, (ya + yb2) / 2
        s.text(None, t, (xm + (-0.18 if t == "0" else 0.18), ym + 0.05), KLEIN, "right" if t == "0" else "left", GRAU)
    for k, (x, y) in P.items():
        s.punkt(None, x, y, farbe=SCHWARZ, r=0.07)
    for k, (x, y, t, p) in B.items():
        s.box("%s\np = %s" % (t, p), (x, y), breite=1.2, hoehe=0.62, form="round", groesse=KLEIN, fuellung="#eaf1fb", dicke=2)
    s.speichern()


def k5entropie():
    s = Szene("ml/k5entropie")
    a = s.achsen((0, 1), (0, 1.12), breite=5.4, hoehe=2.9, mitte=(0.2, 0), xl="θ", yl="H_{b}(θ) in bit", xticks="0.1;0.3;0.5;0.7;0.9;1",
                 yticks="0.469;0.881;1")
    s.kurve(a, "-x*log2(x)-(1-x)*log2(1-x)", x=(0.0005, 0.9995), farbe=BLAU, dicke=5)
    pk = heft_punkte("fig:k5entropie")[0]
    for x, y in pk[1:]:
        zug(s, a, [(x, 0), (x, y), (0, y)], farbe=GRAU, dicke=2, dash=DASH)
    for x, y in pk:
        s.punkt(a, x, y, farbe=ROT, r=0.07)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 9
def k5kl():
    s = Szene("ml/k5kl")
    s.welt()
    pk = heft_punkte("fig:k5kl")
    a = s.achsen((0.4, 4.6), (0, 0.6), breite=2.6, hoehe=2.0, mitte=(-1.75, -0.2), xticks="", xzahlen=False, xmarks=False,
                 yticks="0.125;0.25;0.5")
    xs, ps = zip(*pk[0])
    _, qs = zip(*pk[1])
    s.stems(a, [x - 0.17 for x in xs], ps, farbe=BLAU, breite=0.3)
    s.stems(a, [x + 0.17 for x in xs], qs, farbe=ROT, breite=0.3)
    for x, n in zip(xs, "ABCD"):
        s.text(a, n, (x, -0.06), KLEIN, "center")
    s.legende(a, [("p_{k}", BLAU, "s"), ("q_{k}", ROT, "s")], (1.9, 0.58))
    s.text(None, s.tr("ta", "(a) Verteilungen", "(a) distributions", "(a) distribuciones", "(a) 分布"), (-1.75, 1.2), KLEIN, "center")
    b = s.achsen((0.4, 4.6), (-0.4, 1.15), breite=2.6, hoehe=2.0, mitte=(1.8, -0.2), xticks="", xzahlen=False, xmarks=False,
                 yticks="-0.25;0.25;0.5;1")
    xb, db = zip(*pk[2])
    s.stems(b, xb, db, farbe=GRUEN, breite=0.45)
    s.linie(b, (0.4, 0), (4.6, 0), farbe=GRAU, dicke=2)
    for x, n, y in zip(xb, "ABCD", db):
        s.text(b, n, (x, -0.33 if y >= 0 else 0.1), KLEIN, "center")
    s.text(None, s.tr("tb", "(b) Beiträge p_{k} log₂(p_{k}/q_{k})", "(b) contributions p_{k} log₂(p_{k}/q_{k})",
                      "(b) aportes p_{k} log₂(p_{k}/q_{k})", "(b) 各项贡献 p_{k} log₂(p_{k}/q_{k})"), (1.8, 1.2), KLEIN, "center")
    s.speichern()


def k5lnx():
    s = Szene("ml/k5lnx")
    a = s.achsen((0, 3), (-2.6, 2.2), breite=4.4, hoehe=3.4, kreuz=True, xl="x", xticks="1;2;3", yticks="-2;-1;1;2")
    s.kurve(a, "ln(x)", x=(0.07, 3), farbe=BLAU, dicke=5)
    s.kurve(a, "x-1", farbe=ROT, dicke=4)
    s.punkt(a, 1, 0, farbe=SCHWARZ, r=0.07)
    s.legende(a, [("ln x", BLAU, "-"), ("x − 1", ROT, "-")], (0.15, 2.05))
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 10
def k5klflaeche():
    s = Szene("ml/k5klflaeche")
    s.welt()
    a = s.achsen((-4, 5), (0, 0.45), breite=5.6, hoehe=1.45, mitte=(0.15, 1.35), xticks="-4;-2;0;2;4", yticks="0.2;0.4")
    s.kurve(a, "exp(-x^2/2)/sqrt(2*pi)", farbe=BLAU, dicke=5)
    s.kurve(a, "exp(-(x-1)^2/8)/(2*sqrt(2*pi))", farbe=ROT, dicke=5)
    s.legende(a, [("p(x) = 𝒩(0, 1)", BLAU, "-"), ("q(x) = 𝒩(1, 2²)", ROT, "-")], (1.6, 0.43))
    b = s.achsen((-4, 5), (-0.1, 0.37), breite=5.6, hoehe=1.7, mitte=(0.15, -1.3), xl="x", xticks="-4;-2;0;2;4", yticks="-0.1;0.1;0.2;0.3")
    f = "exp(-x^2/2)/sqrt(2*pi)*(ln(2)-x^2/2+(x-1)^2/8)"
    flaechen = re.findall(r"fill=(elblue|holered)!30,draw=none,domain=(-?[\d.]+):(-?[\d.]+),", _abb("fig:k5klflaeche"))
    assert len(flaechen) == 3
    for name, x0, x1 in flaechen:
        s.flaeche(b, f, float(x0), float(x1), farbe=BLAU if name == "elblue" else ROT, deckung=0.3)
    s.kurve(b, f, farbe=GRUEN, dicke=5)
    s.linie(b, (-4, 0), (5, 0), farbe=GRAU, dicke=2)
    s.text(None, s.tr("tb", "Fläche = D_{KL}(p ‖ q) ≈ 0.443", "area = D_{KL}(p ‖ q) ≈ 0.443", "área = D_{KL}(p ‖ q) ≈ 0.443",
                      "面积 = D_{KL}(p ‖ q) ≈ 0.443"), (0.15, -0.2), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Rechenbilder (Summen, Produkte, Skalarprodukte)
# Je Rechenbeispiel im Haupttext, in dem eine Summe, ein Produkt oder ein Skalarprodukt mit Zahlen das Kernstück ist, ein
# Bild ml/k5r<name> (= \label{fig:k5r<name>} im Heft, dort dieselbe Rechnung als align*). Dezimalzahlen mit Punkt:
# s.formel schreibt sie je Sprache um. Alle Formeln bekommen dieselbe Schriftgröße (wie in ml_teil3.py): Die Höhe folgt aus
# den Maßen der gesetzten Formel im Glyphen-Cache des Exports; beim allerersten Bauen gilt der Schätzwert, nach dem Export
# ergibt ein zweiter Lauf die richtige Höhe.
_CACHE = Path(__file__).resolve().parent.parent / "tex_glyphen_cache.json"
EM = 0.245
SPALTE = 6.9


def _hoehe(tex, schaetzung, spalte=SPALTE):
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
    em = min(EM, spalte * 1000 / breite)
    return round(em * hoehe / 1000, 3)


def _formel(name, tex, schaetzung=1.5, spalte=SPALTE):
    s = Szene("ml/" + name)
    s.formel(tex, hoehe=_hoehe(tex, schaetzung, spalte))
    s.speichern()


def _al(*zeilen):
    return r"\begin{aligned}" + r"\\".join(zeilen) + r"\end{aligned}"


def k5rerwartung():                                      # 1.4
    _formel("k5rerwartung", _al(
        r"\mathbb E[\bar X]=\sum_{\bar x}\bar x\,P(\bar X=\bar x)&=1\cdot\tfrac19+1.5\cdot\tfrac29+2\cdot\tfrac39+2.5\cdot\tfrac29+3\cdot\tfrac19",
        r"&=\tfrac{1+3+6+5+3}9=\tfrac{18}9=2",
        r"\operatorname{Var}(\bar X)=\sum_{\bar x}(\bar x-2)^2\,P(\bar X=\bar x)&=1\cdot\tfrac19+0.25\cdot\tfrac29+0\cdot\tfrac39+0.25\cdot\tfrac29"
        r"+1\cdot\tfrac19",
        r"&=\tfrac{1+0.5+0+0.5+1}9=\tfrac39=\tfrac13"), 1.9, 6.55)


def k5rmse():                                            # 2.3
    _formel("k5rmse", _al(
        r"\operatorname{MSE}(0.9\,\bar X)&=\sum_{\bar x}(0.9\,\bar x-2)^2\,P(\bar X=\bar x)",
        r"&=(-1.1)^2\cdot\tfrac19+(-0.65)^2\cdot\tfrac29+(-0.2)^2\cdot\tfrac39+0.25^2\cdot\tfrac29+0.7^2\cdot\tfrac19",
        r"&=\tfrac{1.21+0.845+0.12+0.125+0.49}9=\tfrac{2.79}9=0.31",
        r"&=\underbrace{(-0.2)^2}_{\operatorname{Bias}^2}+\underbrace{0.27}_{\operatorname{Var}}"), 2.4, 6.55)


def k5rbessel():                                         # 3.1
    _formel("k5rbessel", _al(
        r"\mathbb E[\hat\sigma^2_N]&=0\cdot\tfrac39+0.25\cdot\tfrac49+1\cdot\tfrac29=\tfrac{0+1+2}9=\tfrac13=\tfrac12\cdot\tfrac23=\tfrac{N-1}N\,\sigma^2",
        r"\mathbb E[\hat\sigma^2_{N-1}]&=0\cdot\tfrac39+0.5\cdot\tfrac49+2\cdot\tfrac29=\tfrac{0+2+4}9=\tfrac23=\sigma^2"), 1.0)


def k5rprodukt():                                        # 4.3
    _formel("k5rprodukt", _al(
        r"\mathcal L(0.7)=\prod_{i=1}^{10}P(X=x_i\mid0.7)&=0.7\cdot0.3\cdot0.7\cdot0.7\cdot0.3\cdot0.7\cdot0.7\cdot0.3\cdot0.7\cdot0.7",
        r"&=0.7^7\cdot0.3^3=0.0823543\cdot0.027\approx0.00222"), 1.0)


def k5rloglik():                                         # 4.4
    _formel("k5rloglik", _al(
        r"\ell(0.7)=\sum_{i=1}^{10}\ln P(X=x_i\mid0.7)&=\ln0.7+\ln0.3+\ln0.7+\ln0.7+\ln0.3",
        r"&\quad+\ln0.7+\ln0.7+\ln0.3+\ln0.7+\ln0.7",
        r"&=7\ln0.7+3\ln0.3\approx7\cdot(-0.3567)+3\cdot(-1.2040)",
        r"&\approx-2.4967-3.6119=-6.1086"), 2.0)


def k5rbayes():                                          # 6.1
    _formel("k5rbayes", _al(
        r"P(\mathcal D)=\sum_{k=1}^3P(\mathcal D\mid\theta_k)\,P(\theta=\theta_k)&=\tfrac3{256}\cdot\tfrac14+\tfrac{16}{256}\cdot\tfrac12+\tfrac{27}{256}\cdot\tfrac14",
        r"&=\tfrac3{1024}+\tfrac{32}{1024}+\tfrac{27}{1024}=\tfrac{62}{1024}=\tfrac{31}{512}"), 1.2)


def k5rentropie():                                       # 8.2
    _formel("k5rentropie", _al(
        r"H(\mathbf p)=\sum_{k=1}^4p_k\log_2\frac1{p_k}&=\tfrac12\log_22+\tfrac14\log_24+\tfrac18\log_28+\tfrac18\log_28",
        r"&=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3",
        r"&=\tfrac12+\tfrac12+\tfrac38+\tfrac38=\tfrac74=1.75\ \text{bit}"), 1.7)


def k5rcode():                                           # 8.3, bewusst die Darstellung „komponenten“: Wahrscheinlichkeit neben Länge
    s = Szene("ml/k5rcode")
    s.skalarprodukt([0.5, 0.25, 0.125, 0.125], [1, 2, 3, 3], namen=("p", "l"), index="k", darstellung="komponenten", summanden=4)
    s.speichern()


def k5rkreuz():                                          # 9.1
    _formel("k5rkreuz", _al(
        r"H(\mathbf p,\mathbf q)=\sum_{k=1}^4p_k\log_2\frac1{q_k}=\mathbf p^\top\mathbf l'&=0.5\cdot3+0.25\cdot3+0.125\cdot2+0.125\cdot1",
        r"&=1.5+0.75+0.25+0.125=2.625\ \text{bit}"), 1.0)


def k5rkl():                                             # 9.2
    _formel("k5rkl", _al(
        r"D_{\mathrm{KL}}(\mathbf p\,\|\,\mathbf q)=\sum_{k=1}^4p_k\log_2\frac{p_k}{q_k}&=\tfrac12\log_24+\tfrac14\log_22+\tfrac18\log_2\tfrac12"
        r"+\tfrac18\log_2\tfrac14",
        r"&=\tfrac12\cdot2+\tfrac14\cdot1+\tfrac18\cdot(-1)+\tfrac18\cdot(-2)",
        r"&=1+\tfrac14-\tfrac18-\tfrac14=\tfrac78=0.875\ \text{bit}"), 1.7)


def k5rkreuzml():                                        # 11.2
    _formel("k5rkreuzml", _al(
        r"H\bigl(\hat{\mathbf p},\mathbf q(0.5)\bigr)=\sum_{k=1}^2\hat p_k\ln\frac1{q_k(0.5)}&=0.7\ln\frac1{0.5}+0.3\ln\frac1{0.5}"
        r"\approx0.4852+0.2079=0.6931",
        r"H\bigl(\hat{\mathbf p},\mathbf q(0.7)\bigr)=\sum_{k=1}^2\hat p_k\ln\frac1{q_k(0.7)}&=0.7\ln\frac1{0.7}+0.3\ln\frac1{0.3}"
        r"\approx0.2497+0.3612=0.6109"), 1.2)


RECHENBILDER = (k5rerwartung, k5rmse, k5rbessel, k5rprodukt, k5rloglik, k5rbayes, k5rentropie, k5rcode, k5rkreuz, k5rkl, k5rkreuzml)

SZENEN = (k5richtung, k5stichprobe, k5zielscheibe, k5likelihood, k5beta, k5posterior, k5code, k5entropie, k5kl, k5lnx,
          k5klflaeche) + RECHENBILDER

for f in SZENEN:
    f()
