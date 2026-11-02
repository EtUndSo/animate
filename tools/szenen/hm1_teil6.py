"""Höhere Mathematik 1, Teil 6 (kap6_stufen.tex): Unendliche Reihen.

Aufruf: python tools/szenen/hm1_teil6.py, danach python tools/szenen_ansehen.py out.png hm1/k6treppe ... [--lang de]
Alle Zahlen stehen im Heft und in rechnung_kap6.py. Teilsummen sind Punkte über dem Index; die Treppe zeigt, dass jedes Glied
eine Stufe ist. Rechenmodell: q = 1/2, H_N (harmonisch), L_N (alternierend), Q_N (Quadrate).
"""
import sys
from math import factorial, log
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 24                 # Beschriftung in den Bildern
HELLBLAU, HELLORANGE, HELLGRUEN, HELLROT = "#dceafa", "#fbe3d9", "#d6efe0", "#f8dcdc"
BRAUN = "#a84a22"          # dunkles Orange für Text auf heller Fläche
R = 0.055                  # Punktradius einer Folge


def G(N):
    return 2 - 0.5 ** N


def H(N):
    return sum(1 / n for n in range(1, N + 1))


def L(N):
    return sum((-1) ** (n + 1) / n for n in range(1, N + 1))


def T_liste(N):
    """Teilsummen von 1 + 1/3 - 1/2 + 1/5 + 1/7 - 1/4 + ..."""
    aus, s, pos, neg = [], 0.0, 1, 2
    while len(aus) < N:
        for _ in range(2):
            s += 1 / pos
            pos += 2
            aus.append(s)
        s -= 1 / neg
        neg += 2
        aus.append(s)
    return aus[:N]


def glieder(s, on, pts, farbe=BLAU, r=R):
    for x, y in pts:
        s.punkt(on, x, y, farbe=farbe, r=r)


# ------------------------------------------------------------------------------------------ Stufe 1
def k6treppe():
    """Teilsummen als Treppe: links mit Decke, rechts ohne."""
    s = Szene("hm1/k6treppe")
    t1 = s.tr("geo", "Geometrische Reihe, q = 1/2", "Geometric series, q = 1/2", "Serie geométrica, q = 1/2", "几何级数，q = 1/2")
    t2 = s.tr("harm", "Harmonische Reihe", "Harmonic series", "Serie armónica", "调和级数")
    links = s.achsen((-0.5, 11), (0.8, 2.25), breite=2.6, hoehe=1.9, mitte=(-1.75, 0), xticks="0;5;10", yticks="1;1.5;2", xl="N", xl_mitte=False, titel=t1)
    s.linie(links, (-0.5, 2), (11, 2), farbe=GRAU, dicke=2, dash=DASH)
    pts = [(n, G(n)) for n in range(0, 11)]
    s.daten(links, pts + [(11, G(10))], farbe=BLAU, dicke=3, treppe="post")
    glieder(s, links, pts)
    s.linie(links, (1, 1), (1, 1.5), farbe=ROT, dicke=4)
    s.text(links, "a_1 = 1/2", (1.4, 1.17), KLEIN, "left", ROT)
    s.text(links, s.tr("decke", "Decke S = 2", "ceiling S = 2", "techo S = 2", "上界 S = 2"), (4.0, 1.78), KLEIN, "left", GRAU)
    rechts = s.achsen((0, 21), (0, 4.2), breite=2.6, hoehe=1.9, mitte=(1.75, 0), xticks="1;5;10;15;20", yticks="1;2;3;4", xl="N", xl_mitte=False, titel=t2)
    pts = [(n, H(n)) for n in range(1, 21)]
    s.daten(rechts, pts + [(21, H(20))], farbe=GRUEN, dicke=3, treppe="post")
    glieder(s, rechts, pts, farbe=GRUEN)
    s.linie(rechts, (2, 1), (2, 1.5), farbe=ROT, dicke=4)
    s.text(rechts, "a_2 = 1/2", (3.2, 0.82), KLEIN, "left", ROT)
    s.text(rechts, s.tr("ohne", "keine Decke", "no ceiling", "sin techo", "没有上界"), (9.5, 2.0), KLEIN, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k6harmonisch():
    """Glieder 1/n als Balken, in Gruppen mit 1, 2, 4, 8 Gliedern, jede Gruppe mindestens 1/2."""
    s = Szene("hm1/k6harmonisch")
    b = s.achsen((0, 17), (0, 1.1), breite=5.9, hoehe=2.35, mitte=(0, 0), xticks="1;2;4;8;16", yticks="0;0.5;1", xl="n", xl_mitte=False)
    s.stems(b, [1], [1], farbe=GRAU, breite=0.7)
    gruppen = ((2, 2, 2, BLAU, "1 · 1/2", 1.7, 0.6), (3, 4, 4, GRUEN, "2 · 1/4", 3.0, 0.42), (5, 8, 8, BRAUN, "4 · 1/8", 5.2, 0.28), (9, 16, 16, ROT, "8 · 1/16", 10.8, 0.2))
    for n0, n1, h, farbe, t, xt, y in gruppen:
        xs = list(range(n0, n1 + 1))
        s.stems(b, xs, [1 / n for n in xs], farbe=farbe, breite=0.7)
        s.linie(b, (n0 - 0.5, 1 / h), (n1 + 0.5, 1 / h), farbe=SCHWARZ, dicke=2.5, dash=DASH)
        s.text(b, t, (xt, y), KLEIN, "left", farbe)
    t = s.tr("je", "Jede Gruppe ist mindestens 1/2:\ndoppelt so viele Glieder,\nhalb so hoch.", "Each group is at least 1/2:\ntwice as many terms,\nhalf as high.",
             "Cada grupo vale al menos 1/2:\nel doble de términos,\nla mitad de altura.", "每组至少为 1/2：\n项数加倍，\n高度减半。")
    s.text(b, t, (7.0, 0.88), KLEIN, "left")
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k6leibniz():
    """Teilsummen L_N: Die ungeraden fallen, die geraden steigen, S liegt dazwischen."""
    s = Szene("hm1/k6leibniz")
    b = s.achsen((0, 17), (0.4, 1.05), breite=5.0, hoehe=2.3, mitte=(-0.75, 0), xticks="1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16", yticks="0.5;0.6;0.7;0.8;0.9;1", xl="N", xl_mitte=False)
    s.linie(b, (0, log(2)), (17, log(2)), farbe=ROT, dicke=2.5, dash=DASH)
    pts = [(n, L(n)) for n in range(1, 17)]
    s.daten(b, pts, farbe=HELLGRAU, dicke=2.5)
    glieder(s, b, [p for p in pts if p[0] % 2 == 1], farbe=BLAU, r=0.065)
    glieder(s, b, [p for p in pts if p[0] % 2 == 0], farbe=GRUEN, r=0.065)
    s.text(b, "S = log 2 ≈ 0.693", (17.4, log(2)), KLEIN, "left", ROT)
    s.text(b, s.tr("fallen", "ungerade N: fallen", "odd N: falling", "N impar: bajan", "奇数 N：下降"), (5.2, 0.93), KLEIN, "left", BLAU)
    s.text(b, s.tr("steigen", "gerade N: steigen", "even N: rising", "N par: suben", "偶数 N：上升"), (5.2, 0.47), KLEIN, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k6klammern():
    """1 - 1 + 1 - ...: Jede Klammerung wählt eine andere Teilfolge der Teilsummen."""
    s = Szene("hm1/k6klammern")
    felder = (("(1 − 1) + (1 − 1) + …", -1.75, 0, "gerade", "S_2, S_4, S_6, … : 0", "S_2, S_4, S_6, … : 0"),
              ("1 + (−1 + 1) + (−1 + 1) + …", 1.75, 1, "ungerade", "S_1, S_3, S_5, … : 1", "S_1, S_3, S_5, … : 1"))
    for titel, mitte, wert, _, t, _t in felder:
        b = s.achsen((0, 11), (-0.45, 1.5), breite=2.6, hoehe=1.35, mitte=(mitte, 0), xticks="1;5;10", yticks="0;1", xl="N", xl_mitte=False, titel=titel)
        for n in range(1, 11):
            w = 1 if n % 2 else 0
            if w == wert:
                s.punkt(b, n, w, farbe=ROT, r=0.08)
            else:
                s.punkt(b, n, w, farbe=HELLGRAU, r=0.055)
        s.text(b, t, (0.6, 0.5), KLEIN, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k6bloecke():
    """Blocksummen B_k von 1/n und 1/n^2 unter der geometrischen Schranke."""
    s = Szene("hm1/k6bloecke")

    def B(k, al):
        return sum(1 / n ** al for n in range(2 ** k, 2 ** (k + 1)))
    t1 = s.tr("a1", "s = 1: Schranke 1, q = 1", "s = 1: bound 1, q = 1", "s = 1: cota 1, q = 1", "s = 1：上界 1，q = 1")
    t2 = s.tr("a2", "s = 2: Schranke (1/2)^k, q = 1/2", "s = 2: bound (1/2)^k, q = 1/2", "s = 2: cota (1/2)^k, q = 1/2", "s = 2：上界 (1/2)^k，q = 1/2")
    links = s.achsen((-0.5, 8), (0, 1.15), breite=2.6, hoehe=1.75, mitte=(-1.75, 0), xticks="0;2;4;6", yticks="0;0.5;1", xl="k", xl_mitte=False, titel=t1)
    s.linie(links, (-0.5, 1), (8, 1), farbe=ORANGE, dicke=2.5, dash=DASH)
    s.linie(links, (-0.5, 0.5), (8, 0.5), farbe=GRAU, dicke=2.5, dash=DASH)
    glieder(s, links, [(k, B(k, 1)) for k in range(8)], r=0.065)
    s.text(links, s.tr("bleibt", "Blöcke bleiben groß", "blocks stay large", "los bloques siguen grandes", "各块始终较大"), (0.3, 0.26), KLEIN, "left", BLAU)
    rechts = s.achsen((-0.5, 8), (0, 1.15), breite=2.6, hoehe=1.75, mitte=(1.75, 0), xticks="0;2;4;6", yticks="0;0.5;1", xl="k", xl_mitte=False, titel=t2)
    s.daten(rechts, [(k, 0.5 ** k) for k in range(8)], farbe=ORANGE, dicke=2.5, dash=DASH)
    glieder(s, rechts, [(k, B(k, 2)) for k in range(8)], r=0.065)
    s.text(rechts, s.tr("halb", "Blöcke halbieren sich", "blocks halve", "se reducen a la mitad", "各块逐次减半"), (2.2, 0.76), KLEIN, "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k6quotient():
    """3^n/n! auf logarithmischer Achse: Ab n = 5 liegt die Folge unter einer Geraden, also einer geometrischen Folge."""
    s = Szene("hm1/k6quotient")
    b = s.achsen((0, 17), (1e-6, 30), breite=5.3, hoehe=2.4, mitte=(-0.5, 0), xticks="0;5;10;15", yticks="1e-6;1e-4;1e-2;1", xl="n", xl_mitte=False, ylog=True, gitter=True)

    def a(n):
        return 3 ** n / factorial(n)
    s.linie(b, (5, 1e-6), (5, 30), farbe=ROT, dicke=2.5, dash=DASH)
    s.text(b, "n_0 = 5", (5.3, 12), KLEIN, "left", ROT)
    s.daten(b, [(n, a(5) * 0.5 ** (n - 5)) for n in (5, 17)], farbe=ORANGE, dicke=3.5, dash=DASH)
    glieder(s, b, [(n, a(n)) for n in range(0, 17)], r=0.065)
    s.text(b, "a_5 · (1/2)^{n−5}", (10.8, 0.5), KLEIN, "left", BRAUN)
    s.text(b, "|a_n| = 3^n / n!", (9.3, 3e-5), KLEIN, "right", BLAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 7
def k6verdichtung():
    """Balken a_n = 1/n, oben von Rechtecken überdeckt, unten Rechtecke, die in den Balken liegen."""
    s = Szene("hm1/k6verdichtung")
    t1 = s.tr("oben", "von oben: Block ≤ 2^k a(2^k)", "from above: block ≤ 2^k a(2^k)", "por arriba: bloque ≤ 2^k a(2^k)", "上方：块 ≤ 2^k a(2^k)")
    t2 = s.tr("unten", "von unten: Block ≥ 2^{k−1} a(2^k)", "from below: block ≥ 2^{k−1} a(2^k)", "por abajo: bloque ≥ 2^{k−1} a(2^k)", "下方：块 ≥ 2^{k−1} a(2^k)")
    xs = list(range(1, 17))
    links = s.achsen((0, 17), (0, 1.12), breite=2.6, hoehe=1.75, mitte=(-1.75, 0), xticks="1;2;4;8;16", yticks="0;0.5;1", xl="n", xl_mitte=False, titel=t1)
    for k, h in ((0, 1), (1, 0.5), (2, 0.25), (3, 0.125)):
        s.band(links, 2 ** k - 0.5, 2 ** (k + 1) - 0.5, 0, h, farbe=ROT, deckung=0.18)
    s.stems(links, xs[:15], [1 / n for n in xs[:15]], farbe=BLAU, breite=0.55)
    for k, h in ((0, 1), (1, 0.5), (2, 0.25), (3, 0.125)):
        s.linie(links, (2 ** k - 0.5, h), (2 ** (k + 1) - 0.5, h), farbe=ROT, dicke=3)
    rechts = s.achsen((0, 17), (0, 1.12), breite=2.6, hoehe=1.75, mitte=(1.75, 0), xticks="1;2;4;8;16", yticks="0;0.5;1", xl="n", xl_mitte=False, titel=t2)
    s.stems(rechts, xs, [1 / n for n in xs], farbe=HELLGRAU, breite=0.55)
    for k, h in ((1, 0.5), (2, 0.25), (3, 0.125), (4, 0.0625)):
        s.band(rechts, 2 ** (k - 1) + 0.5, 2 ** k + 0.5, 0, h, farbe=GRUEN, deckung=0.3)
        s.linie(rechts, (2 ** (k - 1) + 0.5, h), (2 ** k + 0.5, h), farbe=GRUEN, dicke=3)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 8
def k6umordnung():
    """Dieselben Glieder in zwei Reihenfolgen: L_N strebt zu ln 2, T_N zu 3/2 ln 2."""
    s = Szene("hm1/k6umordnung")
    b = s.achsen((0, 37), (0.4, 1.4), breite=4.8, hoehe=2.4, mitte=(-1.0, 0), xticks="1;6;12;18;24;30;36", yticks="0.5;0.75;1;1.25", xl="N", xl_mitte=False)
    s.linie(b, (0, log(2)), (37, log(2)), farbe=BLAU, dicke=2.5, dash=DASH)
    s.linie(b, (0, 1.5 * log(2)), (37, 1.5 * log(2)), farbe=BRAUN, dicke=2.5, dash=DASH)
    pl = [(n, L(n)) for n in range(1, 37)]
    pt = [(n + 1, t) for n, t in enumerate(T_liste(36))]
    s.daten(b, pl, farbe=HELLBLAU, dicke=2.5)
    s.daten(b, pt, farbe=HELLORANGE, dicke=2.5)
    glieder(s, b, pl, r=0.045)
    glieder(s, b, pt, farbe=ORANGE, r=0.045)
    s.text(b, "log 2 ≈ 0.693", (37.6, log(2)), KLEIN, "left", BLAU)
    s.text(b, "(3/2) log 2 ≈ 1.040", (37.6, 1.5 * log(2)), KLEIN, "left", BRAUN)
    t = s.tr("alt", "L_N: Reihenfolge 1, 2, 3, 4, …", "L_N: order 1, 2, 3, 4, …", "L_N: orden 1, 2, 3, 4, …", "L_N：顺序 1, 2, 3, 4, …")
    s.text(b, t, (9, 0.48), KLEIN, "left", BLAU)
    t = s.tr("neu", "T_N: je zwei positive, ein negatives Glied", "T_N: two positive terms, then one negative", "T_N: dos términos positivos, uno negativo", "T_N：每两个正项后接一个负项")
    s.text(b, t, (3, 1.33), KLEIN, "left", BRAUN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 9
def k6wegweiser():
    """Entscheidungsweg: Links die Fragen von oben nach unten, rechts der Ausgang bei Ja."""
    s = Szene("hm1/k6wegweiser")
    zeilen = (
        (s.tr("f1", "Strebt a_n nicht gegen 0?", "Does a_n not tend to 0?", "¿a_n no tiende a 0?", "a_n 不趋于 0？"),
         s.tr("e1", "divergent", "divergent", "divergente", "发散"), ROT, HELLROT),
        (s.tr("f2", "Teilsummen als Formel?\n(geometrisch, Teleskop)", "Partial sums in closed form?\n(geometric, telescoping)", "¿Sumas parciales con fórmula?\n(geométrica, telescópica)", "部分和有闭式？\n（几何、裂项）"),
         s.tr("e2", "Grenzwert ausrechnen", "compute the limit", "calcular el límite", "直接求极限"), BLAU, HELLBLAU),
        (s.tr("f3", "Wechselnde Vorzeichen,\n|a_n| fällt monoton gegen 0?", "Alternating signs,\n|a_n| decreases to 0?", "¿Signos alternos,\n|a_n| decrece a 0?", "符号交替，\n|a_n| 单调减到 0？"),
         s.tr("e3", "Leibniz: konvergent\nabsolut? weiter mit |a_n|", "Leibniz: convergent\nabsolutely? go on with |a_n|", "Leibniz: convergente\n¿absoluta? seguir con |a_n|", "莱布尼茨：收敛\n绝对收敛？对 |a_n| 继续"), GRUEN, HELLGRUEN),
        (s.tr("f4", "Fakultäten, q^n, Potenzen (…)^n?", "Factorials, q^n, powers (…)^n?", "¿Factoriales, q^n, potencias (…)^n?", "含阶乘、q^n、幂 (…)^n？"),
         s.tr("e4", "Quotient oder Wurzel\nα < 1 absolut konvergent\nα > 1 divergent\nα = 1 weiter nach unten", "ratio or root\nα < 1 absolutely convergent\nα > 1 divergent\nα = 1 go further down",
              "cociente o raíz\nα < 1 absolutamente conv.\nα > 1 divergente\nα = 1 seguir abajo", "比值或根值\nα < 1 绝对收敛\nα > 1 发散\nα = 1 继续向下"), BLAU, HELLBLAU),
        (s.tr("f5", "Nur Potenzen von n?\n(Brüche, Wurzeln)", "Only powers of n?\n(fractions, roots)", "¿Solo potencias de n?\n(fracciones, raíces)", "只含 n 的幂？\n（分式、根式）"),
         s.tr("e5", "Vergleich mit Σ 1/n^s", "comparison with Σ 1/n^s", "comparación con Σ 1/n^s", "与 Σ 1/n^s 比较"), BLAU, HELLBLAU),
        (s.tr("f6", "Monoton fallend, mit log n?", "Decreasing, with log n?", "¿Decreciente, con log n?", "单调递减，含 log n？"),
         s.tr("e6", "Verdichtung", "condensation", "condensación", "凝聚判别法"), BLAU, HELLBLAU),
    )
    ja, nein = s.tr("ja", "ja", "yes", "sí", "是"), s.tr("nein", "nein", "no", "no", "否")
    hoehen = (0.5, 0.7, 0.7, 1.12, 0.7, 0.5)
    xl, bl, xr, br = -1.8, 3.35, 1.95, 2.95
    y = 3.0
    for i, ((f, e, farbe, hell), h) in enumerate(zip(zeilen, hoehen)):
        s.box(f, (xl, y), breite=bl, hoehe=h, groesse=23, farbe=SCHWARZ, fuellung="#f4f4f4", dicke=2.5)
        s.box(e, (xr, y), breite=br, hoehe=h, groesse=23, farbe=farbe, fuellung=hell, dicke=2.5)
        s.pfeil((xl + bl / 2, y), (xr - br / 2, y), "", farbe=farbe, spitze=0.14, dicke=3)
        s.text(None, ja, (xl + bl / 2 + 0.05, y + 0.17), 22, "left", farbe)
        if i < len(zeilen) - 1:
            h2 = hoehen[i + 1]
            y2 = y - h / 2 - 0.27 - h2 / 2
            s.pfeil((xl, y - h / 2), (xl, y2 + h2 / 2), "", farbe=GRAU, spitze=0.14, dicke=3)
            s.text(None, nein, (xl + 0.1, y - h / 2 - 0.15), 22, "left", GRAU)
            y = y2
    s.speichern()


for f in (k6treppe, k6harmonisch, k6leibniz, k6klammern, k6bloecke, k6quotient, k6verdichtung, k6umordnung, k6wegweiser):
    f()
