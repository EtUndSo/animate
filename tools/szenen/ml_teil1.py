"""Machine Learning Grundlagen 1 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap1_stufen.tex, kap1_stufen_b.tex): Abbildungen.

Szenenname ml/k1<name> = \\label{fig:k1<name>} im Heft. Stil wie tools/szenen/et3_teil2.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil1.py
Export: python tools/export_szenen.py ml/k1<name> ...   (jedes Bild höchstens 548 px breit)
Szenen mit mehreren Teilbildern rufen zuerst s.welt() auf: Danach sind Texte ohne on= in Szeneneinheiten.
"""
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


def parallelogramm(s, on, a, b, farbe=BLAU, dicke=3):
    zug(s, on, [(0, 0), a, (a[0] + b[0], a[1] + b[1]), b, (0, 0)], farbe=farbe, dicke=dicke)


# ------------------------------------------------------------------ Abschnitt 1
def k1punktpfeil():
    s = Szene("ml/k1punktpfeil")
    s.welt()
    for k, mx in enumerate((-1.75, 1.75)):
        a = s.achsen((0, 4.5), (0, 3), breite=2.7, hoehe=1.8, mitte=(mx, 0), xl="x₁", yl="x₂", xticks="1;2;3;4", yticks="1;2",
                     xl_mitte=False)
        if k == 0:
            s.linie(a, (3, 0), (3, 2), farbe=GRAU, dicke=2, dash=DASH)
            s.linie(a, (0, 2), (3, 2), farbe=GRAU, dicke=2, dash=DASH)
            s.punkt(a, 3, 2, farbe=BLAU, r=0.09)
            s.text(a, "x = (3, 2)^{⊤}", (3.1, 2.35), MITTEL)
        else:
            s.pfeil((0, 0), (3, 2), on=a, farbe=BLAU, dicke=4, spitze=0.2)
            s.text(a, "x", (3.1, 2.25), MITTEL)
    s.text(None, s.tr("punkt", "als Punkt", "as a point", "como punto", "看作点", fr="comme point", tr="nokta olarak"), (-1.75, -1.5),
           MITTEL, "center")
    s.text(None, s.tr("pfeil", "als Pfeil", "as an arrow", "como flecha", "看作箭头", fr="comme flèche", tr="ok olarak"), (1.75, -1.5),
           MITTEL, "center")
    s.speichern()


def k1addition():
    s = Szene("ml/k1addition")
    s.welt()
    a = s.achsen((0, 4.6), (0, 3.4), breite=2.5, hoehe=1.85, mitte=(-1.85, 0), xl="x₁", yl="x₂", xticks="1;2;3;4", yticks="1;2;3",
                 xl_mitte=False)
    s.pfeil((0, 0), (1, 2), on=a, farbe=ROT_HELL, dicke=3, spitze=0.16, dash=DASH)
    s.pfeil((1, 2), (4, 3), on=a, farbe=HELLBLAU, dicke=3, spitze=0.16, dash=DASH)
    s.pfeil((0, 0), (3, 1), on=a, farbe=BLAU, dicke=4, spitze=0.18)
    s.pfeil((3, 1), (4, 3), on=a, farbe=ROT, dicke=4, spitze=0.18)
    s.pfeil((0, 0), (4, 3), on=a, farbe=SCHWARZ, dicke=4, spitze=0.18)
    s.text(a, "u", (1.7, 0.25), MITTEL, "center", BLAU)
    s.text(a, "v", (3.75, 1.8), MITTEL, "left", ROT)
    s.text(a, "u + v", (1.6, 1.75), MITTEL, "right")
    b = s.achsen((-2.6, 4.6), (-1.4, 2.4), breite=2.3, hoehe=1.21, mitte=(1.6, 0.2), kreuz=True, xticks="", yticks="", xl="x₁", yl="x₂")
    s.pfeil((0, 0), (4, 2), on=b, farbe=HELLGRAU, dicke=8, spitze=0.22)
    s.pfeil((0, 0), (2, 1), on=b, farbe=BLAU, dicke=4, spitze=0.18)
    s.pfeil((0, 0), (-2, -1), on=b, farbe=ROT, dicke=4, spitze=0.18)
    s.text(b, "u", (1.3, 1.3), MITTEL, "center", BLAU)
    s.text(b, "2u", (3.6, 2.2), MITTEL, "center", GRAU)
    s.text(b, "−u", (-1.8, -1.35), MITTEL, "center", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k1muster():
    s = Szene("ml/k1muster")
    s.welt()
    werte = {"links": ((1, -1, 1, -1), (2, -1, 3, -2), (2, 1, 3, 2), "wᵀx = 2 + 1 + 3 + 2 = 8"),
             "rechts": ((1, -1, 1, -1), (2, 2, 3, 3), (2, -2, 3, -3), "wᵀx' = 2 − 2 + 3 − 3 = 0")}
    zeilen = (BLAU, ROT, GRUEN)
    for spalte, mx in (("links", -0.6), ("rechts", 2.6)):
        w, x, p, summe = werte[spalte]
        for k, (ys, farbe) in enumerate(zip((w, x, p), zeilen)):
            a = s.achsen((0.4, 4.6), (-3.2, 3.2), breite=2.6, hoehe=1.15, mitte=(mx, 1.75 - 1.4 * k), xticks="", yticks="",
                         xmarks=False, ymarks=False, xzahlen=False, yzahlen=False, unsichtbar=True)
            s.linie(a, (0.4, 0), (4.6, 0), farbe=GRAU, dicke=2)
            s.stems(a, (1, 2, 3, 4), ys, farbe=farbe, dicke=4, r=0.07)
        s.text(None, summe, (mx, -2.55), MITTEL, "center")
    s.text(None, s.tr("tl", "x wechselt im Takt", "x alternates", "x alterna", "x 交替变化", fr="x alterne en cadence",
                      tr="x işaret değiştirir"), (-0.6, 2.75), MITTEL, "center")
    s.text(None, s.tr("tr", "x' steigt gleichmäßig", "x' rises steadily", "x' sube de forma regular", "x' 平稳上升",
                      fr="x' croît régulièrement", tr="x' düzgün biçimde artar"), (2.6, 2.75), MITTEL, "center")
    s.text(None, s.tr("m", "Muster w", "pattern w", "patrón w", "模式 w", fr="motif w", tr="örüntü w"), (-2.05, 1.75), KLEIN, "right")
    s.text(None, s.tr("sig", "Verlauf", "time series", "serie temporal", "时间序列", fr="série", tr="zaman serisi"), (-2.05, 0.35), KLEIN, "right")
    s.text(None, s.tr("prod", "Produkte", "products", "productos", "乘积", fr="produits", tr="çarpımlar"), (-2.05, -1.05), KLEIN, "right")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3
def k1einheitskugeln():
    s = Szene("ml/k1einheitskugeln")
    s.welt()
    raute = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0)]
    quadrat = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    titel = (("L₁: |x₁| + |x₂| = 1", ORANGE), ("L₂: x₁² + x₂² = 1", BLAU), ("L∞: max(|x₁|, |x₂|) = 1", GRUEN))
    for k, mx in enumerate((-2.2, 0, 2.2)):
        a = s.achsen((-1.45, 1.45), (-1.45, 1.45), breite=1.75, hoehe=1.75, mitte=(mx, 0.2), kreuz=True, xticks="1", yticks="1", xl="x₁", yl="x₂")
        zug(s, a, raute, farbe=HELLGRAU, dicke=2)
        s.kreis(a, 0, 0, 1, farbe=HELLGRAU, dicke=2)
        zug(s, a, quadrat, farbe=HELLGRAU, dicke=2)
        if k == 0:
            zug(s, a, raute, farbe=ORANGE, dicke=5)
        elif k == 1:
            s.kreis(a, 0, 0, 1, farbe=BLAU, dicke=5)
        else:
            zug(s, a, quadrat, farbe=GRUEN, dicke=5)
        s.text(None, titel[k][0], (mx, -1.25), KLEIN, "center", titel[k][1])
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k1einheiten():
    s = Szene("ml/k1einheiten")
    s.welt()
    flaeche = s.tr("fl", "Fläche in m²", "area in m²", "superficie (m²)", "面积 m²", fr="surface (m²)", tr="alan (m²)")
    flaeche10 = s.tr("fl10", "Fläche in 10 m²", "area in 10 m²", "superficie\n(10 m²)", "面积 10 m²", fr="surface (10 m²)",
                     tr="alan (10 m²)")
    zimmer = s.tr("zi", "Zimmer", "rooms", "cuartos", "房间数", fr="pièces", tr="oda")   # es: „habitaciones“ ist zu breit
    a = s.achsen((51, 66.5), (0.5, 5.4), breite=4.0, hoehe=1.27, mitte=(-1.25, 0), xl=flaeche, yl=zimmer, xticks="52;56;60;64", yticks="2;4")
    s.kreis(a, 60, 2, 3.606, farbe=HELLBLAU, dicke=2, dash=DASH)
    s.linie(a, (60, 2), (63, 4), farbe=BLAU, dicke=4)
    s.linie(a, (60, 2), (54, 2), farbe=ROT, dicke=4)
    for n, x, y, f in (("A", 60, 2, SCHWARZ), ("B", 63, 4, BLAU), ("C", 54, 2, ROT)):
        s.punkt(a, x, y, farbe=f, r=0.07)
        s.text(a, n, (x + 0.4, y - 0.9), MITTEL, "center", f)
    s.text(a, "3.61", (63.3, 2.6), KLEIN, "left", BLAU)
    s.text(a, "6", (57, 2.7), KLEIN, "center", ROT)
    b = s.achsen((5.1, 6.75), (0.5, 5.4), breite=0.88, hoehe=2.6, mitte=(2.75, 0.4), xl=flaeche10, yl=zimmer, xticks="5.4;6;6.6", yticks="2;4")
    s.linie(b, (6, 2), (6.3, 4), farbe=BLAU, dicke=4)
    s.linie(b, (6, 2), (5.4, 2), farbe=ROT, dicke=4)
    for n, x, y, f in (("A", 6, 2, SCHWARZ), ("B", 6.3, 4, BLAU), ("C", 5.4, 2, ROT)):
        s.punkt(b, x, y, farbe=f, r=0.07)
        s.text(b, n, (x + 0.08, y - 0.5), MITTEL, "center", f)
    s.text(b, "2.02", (6.35, 3.0), KLEIN, "left", BLAU)
    s.text(b, "0.6", (5.7, 2.5), KLEIN, "center", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 5
def k1schatten():
    s = Szene("ml/k1schatten")
    s.welt()
    a = s.achsen((-0.6, 3.6), (-0.5, 2.9), breite=4.2, hoehe=3.4, mitte=(0, 0), kreuz=True, xticks="1;2;3", yticks="1;2", xl="x₁", yl="x₂")
    s.linie(a, (-0.3, -0.4), (2.0, 2.667), farbe=HELLGRAU, dicke=2)
    s.linie(a, (0, 0), (1.56, 2.08), farbe=HELLBLAU, dicke=9)
    s.pfeil((0, 0), (0.6, 0.8), on=a, farbe=GRUEN, dicke=5, spitze=0.16)
    s.pfeil((0, 0), (3, 1), on=a, farbe=ROT, dicke=4, spitze=0.18)
    s.linie(a, (3, 1), (1.56, 2.08), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, 1.56, 2.08, farbe=BLAU, r=0.07)
    s.text(a, "u", (0.2, 0.5), MITTEL, "right", GRUEN)
    s.text(a, "x", (3.1, 1.0), MITTEL, "left", ROT)
    s.text(a, "(uᵀx) u", (1.45, 2.4), MITTEL, "right", BLAU)
    s.text(a, "φ", (0.95, 0.55), MITTEL, "center")
    sch = s.tr("sch", "Schatten 2.6", "shadow 2.6", "sombra 2.6", "影长 2.6", fr="ombre 2.6", tr="gölge 2.6")
    s.text(a, sch, (0.55, 1.55), KLEIN, "right", BLAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k1datenmatrix():
    s = Szene("ml/k1datenmatrix")
    zeilen = ((60, 2, 3), (40, 1, 1), (90, 4, 6), (70, 3, 2))
    bx, by, h = 0.95, 0.5, -1.4
    for i, zeile in enumerate(zeilen):
        for j, wert in enumerate(zeile):
            if i == 1 and j == 0:
                f = "#a9c8ee"
            elif i == 1:
                f = BLAU_HELL
            elif j == 0:
                f = "#fbd9c8"
            else:
                f = "#ffffff"
            s.box(str(wert), (h + j * bx, 0.9 - i * by), breite=bx, hoehe=by, groesse=MITTEL, fuellung=f, dicke=2)
        n = i + 1
        s.text(None, s.tr("w%d" % n, "Wohnung %d" % n, "apartment %d" % n, "vivienda %d" % n, "公寓 %d" % n, fr="appartement %d" % n,
                          tr="daire %d" % n), (h - 0.6, 0.9 - i * by), MITTEL, "right")
    for j, (k, de, en, es, zh, fr, tr) in enumerate((("fl", "Fläche", "area", "superficie", "面积", "surface", "alan"),
                                                     ("zi", "Zimmer", "rooms", "habitaciones", "房间", "pièces", "oda"),
                                                     ("en", "Entfernung", "distance", "distancia", "距离", "distance", "uzaklık"))):
        s.text(None, s.tr(k, de, en, es, zh, fr=fr, tr=tr), (h + j * bx, 1.45), KLEIN, "center")
    s.text(None, s.tr("zeile", "Zeile 2: Beispiel x₂ᵀ", "row 2: example x₂ᵀ", "fila 2: ejemplo x₂ᵀ", "第 2 行：样本 x₂ᵀ",
                      fr="ligne 2 : exemple x₂ᵀ", tr="satır 2: örnek x₂ᵀ"), (h + 2.6 * bx, 0.4), MITTEL, "left", BLAU)
    s.text(None, s.tr("spalte", "Spalte 1: Merkmal Fläche", "column 1: feature area", "columna 1: característica superficie",
                      "第 1 列：特征 面积", fr="colonne 1 : caractéristique surface", tr="sütun 1: öznitelik alan"),
           (h - 0.3, -1.15), MITTEL, "left", ORANGE)
    s.text(None, "X ∈ ℝ^{4×3}", (h + 2.6 * bx, -0.6), MITTEL, "left")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 7
def k1zeilenspalten():
    s = Szene("ml/k1zeilenspalten")
    s.welt()
    z = 0.42
    zellen = (((-3.1, 0.5), "2", BLAU_HELL), ((-3.1 + z, 0.5), "1", BLAU_HELL), ((-3.1, 0.5 - z), "1", "#ffffff"), ((-3.1 + z, 0.5 - z), "1", "#ffffff"),
              ((-2.0, 0.5), "2", BLAU_HELL), ((-2.0, 0.5 - z), "1", BLAU_HELL), ((-1.0, 0.5), "5", BLAU_HELL), ((-1.0, 0.5 - z), "3", "#ffffff"))
    for (x, y), t, f in zellen:
        s.box(t, (x, y), breite=z, hoehe=z, groesse=MITTEL, fuellung=f, dicke=2)
    s.text(None, "·", (-2.45, 0.3), MITTEL, "center")
    s.text(None, "=", (-1.5, 0.3), MITTEL, "center")
    s.text(None, s.tr("zs", "Zeilensicht", "row view", "visión por filas", "行视角", fr="vue par lignes", tr="satır bakışı"), (-2.0, 1.3),
           MITTEL, "center")
    s.text(None, s.tr("z1", "Zeile 1 mal x:\n2·2 + 1·1 = 5", "row 1 times x:\n2·2 + 1·1 = 5", "fila 1 por x:\n2·2 + 1·1 = 5", "第 1 行乘 x：\n2·2 + 1·1 = 5",
                      fr="ligne 1 fois x\u00a0:\n2·2 + 1·1 = 5", tr="satır 1 çarpı x:\n2·2 + 1·1 = 5"),
           (-2.0, -0.7), KLEIN, "center")
    a = s.achsen((-0.3, 5.8), (-0.3, 3.7), breite=2.9, hoehe=2.0, mitte=(1.5, 0.0), kreuz=True, xticks="1;2;3;4;5", yticks="1;2;3", xl="y₁", yl="y₂")
    s.pfeil((0, 0), (2, 1), on=a, farbe=HELLBLAU, dicke=3, spitze=0.14)
    s.pfeil((0, 0), (1, 1), on=a, farbe=ROT_HELL, dicke=3, spitze=0.14)
    s.pfeil((0, 0), (4, 2), on=a, farbe=BLAU, dicke=4, spitze=0.18)
    s.pfeil((4, 2), (5, 3), on=a, farbe=ROT, dicke=4, spitze=0.18)
    s.punkt(a, 5, 3, r=0.06)
    s.text(a, "2a₁", (2.9, 1.05), KLEIN, "center", BLAU)
    s.text(a, "1a₂", (4.85, 2.2), KLEIN, "left", ROT)
    s.text(a, "Ax = (5, 3)^{⊤}", (4.6, 3.4), KLEIN, "right")
    s.text(None, s.tr("ss", "Spaltensicht", "column view", "visión por columnas", "列视角", fr="vue par colonnes", tr="sütun bakışı"),
           (1.65, 1.45), MITTEL, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 8
def k1ebene():
    s = Szene("ml/k1ebene")
    s.welt()
    bilder = (("dreh", ("Drehung", "rotation", "rotación", "旋转", "rotation", "dönme"), (0, 1), (-1, 0)),
              ("streck", ("Streckung", "stretch", "estiramiento", "拉伸", "étirement", "germe"), (2, 0), (0, 0.5)),
              ("scher", ("Scherung", "shear", "cizalladura", "剪切", "cisaillement", "kayma"), (1, 0), (1, 1)),
              ("platt", ("Plattdrücken", "flattening", "aplastamiento", "压扁", "aplatissement", "yassılaştırma"), (1, 0), (0, 0)))
    for k, (key, worte, a1, a2) in enumerate(bilder):
        mx = -2.5 + 1.67 * k
        a = s.achsen((-1.3, 2.3), (-0.6, 1.6), breite=1.55, hoehe=0.95, mitte=(mx, 0), kreuz=True, xticks="", yticks="",
                     xmarks=False, ymarks=False, xzahlen=False, yzahlen=False)   # wie im Heft: Achsen ohne Zahlen
        zug(s, a, [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], farbe=HELLGRAU, dicke=2, dash=DASH)
        parallelogramm(s, a, a1, a2, farbe=BLAU, dicke=3)
        if a1 != (0, 0):
            s.pfeil((0, 0), a1, on=a, farbe=ROT, dicke=4, spitze=0.13)
        if a2 != (0, 0):
            s.pfeil((0, 0), a2, on=a, farbe=GRUEN, dicke=4, spitze=0.13)
        s.text(None, s.tr(key, *worte[:4], fr=worte[4], tr=worte[5]), (mx, 0.95), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 9
def k1hinter():
    s = Szene("ml/k1hinter")
    kast = dict(form="rect", groesse=MITTEL, dicke=2.5)
    s.text(None, "x ∈ ℝᵏ", (-3.2, 0.6), MITTEL, "center")
    s.box("B", (-1.7, 0.6), breite=0.8, hoehe=0.5, **kast)
    s.text(None, "Bx ∈ ℝⁿ", (-0.1, 0.6), MITTEL, "center")
    s.box("A", (1.4, 0.6), breite=0.8, hoehe=0.5, **kast)
    s.text(None, "A(Bx) ∈ ℝᵐ", (2.9, 0.6), MITTEL, "center")
    for a, b in (((-2.75, 0.6), (-2.1, 0.6)), ((-1.3, 0.6), (-0.75, 0.6)), ((0.55, 0.6), (1.0, 0.6)), ((1.8, 0.6), (2.15, 0.6))):
        s.pfeil(a, b, dicke=3, spitze=0.14)
    s.text(None, "x ∈ ℝᵏ", (-3.2, -0.6), MITTEL, "center")
    s.box("AB", (-0.1, -0.6), breite=2.6, hoehe=0.5, **kast)
    s.text(None, "(AB)x ∈ ℝᵐ", (2.9, -0.6), MITTEL, "center")
    s.pfeil((-2.75, -0.6), (-1.4, -0.6), dicke=3, spitze=0.14)
    s.pfeil((1.2, -0.6), (2.1, -0.6), dicke=3, spitze=0.14)
    s.text(None, "=", (2.9, 0.0), MITTEL, "center", GRAU)
    s.speichern()


def k1reihenfolge():
    s = Szene("ml/k1reihenfolge")
    s.welt()
    teile = ((("vorher", "before", "antes", "变换前", "avant", "önce"), (1, 0), (0, 1), ""),
             (("erst drehen,\ndann strecken", "rotate first,\nthen stretch", "primero girar,\nluego estirar", "先旋转，\n再拉伸",
               "d’abord tourner,\npuis étirer", "önce döndür,\nsonra ger"), (0, 0.5), (-2, 0), "SR"),
             (("erst strecken,\ndann drehen", "stretch first,\nthen rotate", "primero estirar,\nluego girar", "先拉伸，\n再旋转",
               "d’abord étirer,\npuis tourner", "önce ger,\nsonra döndür"), (0, 2), (-0.5, 0), "RS"))
    for k, (worte, a1, a2, name) in enumerate(teile):
        mx = -2.3 + 2.3 * k
        a = s.achsen((-2.4, 1.5), (-0.5, 2.4), breite=1.95, hoehe=1.45, mitte=(mx, -0.4), kreuz=True, xticks="", yticks="",
                     xmarks=False, ymarks=False, xzahlen=False, yzahlen=False)   # wie im Heft: Achsen ohne Zahlen
        zug(s, a, [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], farbe=HELLGRAU, dicke=2, dash=DASH)
        parallelogramm(s, a, a1, a2, farbe=BLAU, dicke=3)
        s.pfeil((0, 0), a1, on=a, farbe=ROT, dicke=4, spitze=0.13)
        s.pfeil((0, 0), a2, on=a, farbe=GRUEN, dicke=4, spitze=0.13)
        titel = s.tr("t%d" % k, *worte[:4], fr=worte[4], tr=worte[5])
        s.text(None, titel if not name else "@{t%d}\n%s" % (k, name), (mx, 1.2), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 12
def k1lgs():
    s = Szene("ml/k1lgs")
    s.welt()
    titel = (("(a) genau eine Lösung", "(a) exactly one solution", "(a) exactamente una solución", "(a) 唯一解",
              "(a) exactement une solution", "(a) tek bir çözüm"),
             ("(b) keine Lösung", "(b) no solution", "(b) ninguna solución", "(b) 无解", "(b) aucune solution", "(b) çözüm yok"),
             ("(c) unendlich viele", "(c) infinitely many", "(c) infinitas", "(c) 无穷多解", "(c) une infinité", "(c) sonsuz sayıda"))
    for k in range(3):
        mx = -2.2 + 2.2 * k   # Abstand so, dass „x₁“ am Pfeilende nicht ins Nachbarbild ragt
        a = s.achsen((-0.4, 4.0), (-0.6, 4.0), breite=1.55, hoehe=1.88, mitte=(mx, -0.3), kreuz=True, xticks="1;2;3", yticks="1;2;3", xl="x₁", yl="x₂")
        if k == 0:
            s.linie(a, (1, 3), (2.5, 0), farbe=BLAU, dicke=4)
            s.linie(a, (0, 3), (3.5, -0.5), farbe=ROT, dicke=4)
            s.punkt(a, 2, 1, r=0.07)
            s.text(a, "2x₁ + x₂ = 5", (1.4, 3.5), KLEIN, "left", BLAU)
            s.text(a, "x₁ + x₂ = 3", (2.4, 1.3), KLEIN, "left", ROT)
        elif k == 1:
            s.linie(a, (0, 3), (3.5, -0.5), farbe=BLAU, dicke=4)
            s.linie(a, (0, 1), (1, 0), farbe=ROT, dicke=4)
            s.text(a, "x₁ + x₂ = 3", (1.0, 2.7), KLEIN, "left", BLAU)
            s.text(a, "x₁ + x₂ = 1", (0.1, 1.5), KLEIN, "left", ROT)
        else:
            s.linie(a, (0, 3), (3.5, -0.5), farbe=ROT_HELL, dicke=9)
            s.linie(a, (0, 3), (3.5, -0.5), farbe=BLAU, dicke=3)
            s.text(a, "x₁ + x₂ = 3\n2x₁ + 2x₂ = 6", (1.7, 2.3), KLEIN, "left")
        s.text(None, s.tr("t%d" % k, *titel[k][:4], fr=titel[k][4], tr=titel[k][5]), (mx, 1.6), KLEIN, "center")   # über „x₂“
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 13
def k1spann():
    s = Szene("ml/k1spann")
    s.welt()
    titel = ("(a) span{(1,2)^{⊤}}", "(b) span{(1,2)^{⊤}, (2,4)^{⊤}}", "(c) span{(1,0)^{⊤}, (1,1)^{⊤}}")
    for k in range(3):
        mx = -2.25 + 2.25 * k
        a = s.achsen((-1.6, 2.0), (-1.6, 2.6), breite=1.5, hoehe=1.98, mitte=(mx, -0.3), kreuz=True, xticks="", yticks="", xl="x₁", yl="x₂",
                     xmarks=False, ymarks=False, xzahlen=False, yzahlen=False)   # wie im Heft: ohne Zahlen (sie drängten sich)
        if k < 2:
            s.linie(a, (-0.8, -1.6), (1.3, 2.6), farbe=HELLBLAU, dicke=5)
            if k == 1:
                s.pfeil((0, 0), (1, 2), on=a, farbe=GRUEN, dicke=4, spitze=0.13)
                s.text(a, "(2,4)^{⊤}", (1.1, 2.1), KLEIN, "left", GRUEN)
            s.pfeil((0, 0), (0.5, 1), on=a, farbe=ROT, dicke=4, spitze=0.13)
            if k == 0:
                s.text(a, "(1,2)^{⊤}", (0.6, 1.0), KLEIN, "left", ROT)
        else:
            s.band(a, -1.6, 2.0, -1.6, 2.6, farbe=BLAU, deckung=0.13)
            s.pfeil((0, 0), (0.5, 0), on=a, farbe=ROT, dicke=4, spitze=0.13)
            s.pfeil((0, 0), (0.5, 0.5), on=a, farbe=GRUEN, dicke=4, spitze=0.13)
            s.text(a, "(1,0)^{⊤}", (0.5, -0.45), KLEIN, "left", ROT)
            s.text(a, "(1,1)^{⊤}", (0.6, 0.75), KLEIN, "left", GRUEN)
        s.text(None, titel[k], (mx, 1.6), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 14
def k1det():
    s = Szene("ml/k1det")
    s.welt()
    a = s.achsen((-0.4, 4.6), (-0.4, 3.6), breite=2.6, hoehe=2.08, mitte=(-1.75, 0), kreuz=True, xticks="1;2;3;4", yticks="1;2;3", xl="x₁", yl="x₂")
    s.band(a, 0, 1, 0, 1, farbe=GRAU, deckung=0.2)
    zug(s, a, [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], farbe=GRAU, dicke=2)
    s.pfeil((0, 0), (1, 0), on=a, farbe=ROT, dicke=4, spitze=0.13)
    s.pfeil((0, 0), (0, 1), on=a, farbe=GRUEN, dicke=4, spitze=0.13)
    s.text(a, "1", (0.5, 0.5), MITTEL, "center")
    s.text(None, s.tr("eq", "Einheitsquadrat", "unit square", "cuadrado unidad", "单位正方形", fr="carré unité", tr="birim kare"),
           (-1.75, -1.45), MITTEL, "center")
    b = s.achsen((-0.4, 4.6), (-0.4, 3.6), breite=2.6, hoehe=2.08, mitte=(1.75, 0), kreuz=True, xticks="1;2;3;4", yticks="1;2;3", xl="x₁", yl="x₂")
    zug(s, b, [(0, 0), (4, 0), (4, 3), (0, 3), (0, 0)], farbe=HELLGRAU, dicke=2, dash=DASH)
    parallelogramm(s, b, (3, 1), (1, 2), farbe=BLAU, dicke=3)
    s.pfeil((0, 0), (3, 1), on=b, farbe=ROT, dicke=4, spitze=0.14)
    s.pfeil((0, 0), (1, 2), on=b, farbe=GRUEN, dicke=4, spitze=0.14)
    s.text(b, "5", (2, 1.5), MITTEL, "center", BLAU)
    s.text(b, "a₁ = (3,1)^{⊤}", (3.1, 0.55), KLEIN, "left", ROT)
    s.text(b, "a₂ = (1,2)^{⊤}", (0.9, 2.4), KLEIN, "right", GRUEN)
    s.text(None, s.tr("bild", "Bild unter A", "image under A", "imagen bajo A", "A 作用后的像", fr="image par A", tr="A altındaki görüntü"),
           (1.75, -1.45), MITTEL, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 15
def k1tensor():
    s = Szene("ml/k1tensor")
    z = 0.17

    def gitter(x0, y0, sp, ze, fuellung="#ffffff"):
        for i in range(ze):
            for j in range(sp):
                s.box("", (x0 + j * z, y0 - i * z), breite=z, hoehe=z, fuellung=fuellung, dicke=1.5)

    gitter(-3.3, 0.2, 1, 1)
    gitter(-2.45, 0.5, 1, 4)
    gitter(-1.75, 0.5, 4, 4)
    for dx, f in ((0.24, ROT_HELL), (0.12, GRUEN_HELL), (0, BLAU_HELL)):
        gitter(-0.5 + dx, 0.5 + dx, 4, 4, f)
    for n in range(3):
        for dx, f in ((0.16, ROT_HELL), (0.08, GRUEN_HELL), (0, BLAU_HELL)):
            gitter(0.85 + 0.82 * n + dx, 0.5 + 0.12 * n + dx, 4, 4, f)
    texte = (("sk", ("Skalar\nForm: keine", "scalar\nshape: none", "escalar\nforma vacía", "标量\n形状：无",
                     "scalaire\nforme vide", "skaler\nşekil: yok"), -3.3),
             ("ve", ("Vektor\nForm 4", "vector\nshape 4", "vector\nforma 4", "向量\n形状 4", "vecteur\nforme 4", "vektör\nşekil 4"), -2.45),
             ("ma", ("Matrix\nForm 4×4", "matrix\nshape 4×4", "matriz\nforma 4×4", "矩阵\n形状 4×4", "matrice\nforme 4×4", "matris\nşekil 4×4"), -1.47),
             ("fb", ("Farbbild\nForm 3×4×4", "color image\nshape 3×4×4", "imagen en color\nforma 3×4×4", "彩色图像\n形状 3×4×4",
                     "image couleur\nforme 3×4×4", "renkli görüntü\nşekil 3×4×4"), -0.1),
             ("st", ("Bildstapel\nForm N×3×4×4", "image stack\nshape N×3×4×4", "pila de\nimágenes\nforma N×3×4×4", "图像堆叠\n形状 N×3×4×4",
                     "pile d’images\nforme N×3×4×4", "görüntü yığını\nşekil N×3×4×4"), 2.05))
    for key, worte, x in texte:
        s.text(None, s.tr(key, *worte[:4], fr=worte[4], tr=worte[5]), (x, -0.75), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Rechenbilder (Summen, Produkte, Skalarprodukte)
# Je Rechenbeispiel im Haupttext, in dem eine Summe oder ein Skalarprodukt mit Zahlen das Kernstück ist, ein Bild ml/k1r<name>
# (= \label{fig:k1r<name>} im Heft, dort dieselbe Rechnung als align*). skalarprodukt() nur für Vektoren ohne Index, sonst
# formel(); in formel() keine Dezimalzahlen, weil MathTex sie nicht je Sprache umschreibt (Brüche stattdessen).
# Alle Formeln bekommen dieselbe Schriftgröße: Die Höhe folgt aus den Maßen der gesetzten Formel (Glyphen-Cache des
# Exports), höchstens so groß, dass die Formel in die Spalte passt. Beim allerersten Bauen steht die Formel noch nicht
# im Cache; dann gilt der Schätzwert, und nach dem Export ergibt ein zweiter Lauf die richtige Höhe.
_CACHE = Path(__file__).resolve().parent.parent / "tex_glyphen_cache.json"
EM = 0.245          # Schriftgröße (em) in Szeneneinheiten, entspricht etwa FORMEL = 30 der Rechenoperationen
SPALTE = 6.9        # größte Breite in Szeneneinheiten (7.0 füllt die Artikelspalte)


def _hoehe(tex, schaetzung):
    try:
        import json as _json
        import re as _re
        glyphen = _json.loads(_CACHE.read_text(encoding="utf-8"))["glyphs"].get(tex)
    except (OSError, ValueError, KeyError):
        glyphen = None
    if not glyphen:
        return schaetzung
    xs, ys = [], []
    for g in glyphen:
        a, b, c, d, e, f = g["m"]
        zahlen = [float(z) for z in _re.findall(r"-?\d+(?:\.\d+)?", g["d"])]
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
    """Spaltenvektor als pmatrix."""
    return r"\begin{pmatrix}" + r"\\".join(str(z) for z in zahlen) + r"\end{pmatrix}"


X1, W = _sp(60, 2, 3), _sp(3, 10, -4)


def k1rsumme():                                          # 1.1
    _formel("k1rsumme", _al(r"\sum_{i=1}^3a_i&=a_1+a_2+a_3=2+5+1=8",
                            r"\sum_{i=1}^3a_i^2&=a_1^2+a_2^2+a_3^2=2^2+5^2+1^2=4+25+1=30",
                            r"\sum_{j=1}^3j&=1+2+3=6"), 1.45)


def k1rdoppel():                                         # 1.1
    _formel("k1rdoppel", _al(r"\sum_{i=1}^2\sum_{j=1}^2a_{ij}&=(a_{11}+a_{12})+(a_{21}+a_{22})",
                             r"&=(1+2)+(3+4)=3+7=10",
                             r"\sum_{j=1}^2\sum_{i=1}^2a_{ij}&=(a_{11}+a_{21})+(a_{12}+a_{22})",
                             r"&=(1+3)+(2+4)=4+6=10"), 2.2)


def k1rmittelvektor():                                   # 1.5
    _formel("k1rmittelvektor", _al(
        r"\bar{\mathbf x}=\tfrac14\sum_{i=1}^4\mathbf x_i&=\tfrac14\,(\mathbf x_1+\mathbf x_2+\mathbf x_3+\mathbf x_4)",
        r"&=\tfrac14\left[" + X1 + "+" + _sp(40, 1, 1) + "+" + _sp(90, 4, 6) + "+" + _sp(70, 3, 2) + r"\right]",
        r"&=\tfrac14" + _sp(260, 10, 12) + "=" + _sp(65, "5/2", 3)), 2.3)


def k1rskp():                                            # 2.1
    s = Szene("ml/k1rskp")
    s.skalarprodukt([1, 2, 3], [4, -1, 2], namen=("u", "v"), index="j", mitte=(0, 0.75))
    s.skalarprodukt([1, 2, 3], [1, 2, 3], namen=("u", "u"), index="j", mitte=(0, -1.25), vektoren=False)
    s.speichern()


def k1rgewicht():                                        # 2.2
    _formel("k1rgewicht", _al(r"&\mathbf w=" + W + r",\qquad \mathbf x_1=" + X1,
                              r"\hat y_1=\mathbf w^\top\mathbf x_1&=\sum_{j=1}^3w_j\,x_{1j}=w_1x_{11}+w_2x_{12}+w_3x_{13}",
                              r"&=3\cdot60+10\cdot2+(-4)\cdot3",
                              r"&=180+20-12=188"), 2.0)


def k1rmittel():                                         # 2.3
    _formel("k1rmittel", _al(r"\mathbf 1^\top\mathbf u=\sum_{i=1}^3u_i&=u_1+u_2+u_3=200+250+300=750",
                             r"\bar u=\tfrac13\,\mathbf 1^\top\mathbf u&=\tfrac{750}3=250"), 0.85)


def k1rstrom():                                          # 2.3
    s = Szene("ml/k1rstrom")
    s.skalarprodukt([0.32, 0.34, 0.28], [200, 250, 300], namen=("p", "u"), index="j")
    s.speichern()


def k1rmuster():                                         # 2.4
    s = Szene("ml/k1rmuster")                           # x' als Name kann skalarprodukt() nicht (Strich fällt weg): formel()
    s.skalarprodukt([1, -1, 1, -1], [2, -1, 3, -2], namen=("w", "x"), index="j", mitte=(0, 1.75))
    tex = _al(r"&\mathbf x'=" + _sp(2, 2, 3, 3),
              r"\mathbf w^\top\mathbf x'=\sum_{j=1}^4w_j\,x'_j&=w_1x'_1+w_2x'_2+w_3x'_3+w_4x'_4",
              r"&=1\cdot2+(-1)\cdot2+1\cdot3+(-1)\cdot3",
              r"&=2+(-2)+3+(-3)=0")
    h = _hoehe(tex, 2.4)
    s.formel(tex, mitte=(0, 0.25 - h / 2), hoehe=h)     # Oberkante knapp unter der Rechnung oben (deren Unterkante ≈ 0,65)
    s.speichern()


def k1rl2():                                             # 3.1
    _formel("k1rl2", _al(r"&\mathbf x=" + _sp(3, -4),
                         r"\lVert\mathbf x\rVert_2=\sqrt{\sum_{j=1}^2x_j^2}&=\sqrt{x_1^2+x_2^2}=\sqrt{3^2+(-4)^2}",
                         r"&=\sqrt{9+16}=\sqrt{25}=5"), 1.6)


def k1rl1():                                             # 3.2
    _formel("k1rl1", r"\lVert\mathbf x\rVert_1=\sum_{j=1}^2|x_j|=|x_1|+|x_2|=|3|+|{-4}|=3+4=7", 0.55)


def k1rlp():                                             # 3.4
    _formel("k1rlp", _al(r"\lVert\mathbf x\rVert_3=\Bigl(\sum_{j=1}^2|x_j|^3\Bigr)^{1/3}&=\bigl(|x_1|^3+|x_2|^3\bigr)^{1/3}"
                         r"=\bigl(3^3+4^3\bigr)^{1/3}",
                         r"&=(27+64)^{1/3}=91^{1/3}",
                         r"\lVert\mathbf x\rVert_{10}=\Bigl(\sum_{j=1}^2|x_j|^{10}\Bigr)^{1/10}&=\bigl(|x_1|^{10}+|x_2|^{10}\bigr)^{1/10}"
                         r"=\bigl(3^{10}+4^{10}\bigr)^{1/10}",
                         r"&=(59\,049+1\,048\,576)^{1/10}=1\,107\,625^{1/10}"), 2.3)


def k1rfehler():                                         # 3.5
    _formel("k1rfehler", _al(r"\lVert\hat{\mathbf y}_{\mathrm A}-\mathbf y\rVert_2&=\sqrt{10^2+(-10)^2+10^2+(-10)^2}",
                             r"&=\sqrt{100+100+100+100}=\sqrt{400}=20",
                             r"\lVert\hat{\mathbf y}_{\mathrm B}-\mathbf y\rVert_2&=\sqrt{0^2+0^2+0^2+40^2}",
                             r"&=\sqrt{0+0+0+1\,600}=\sqrt{1\,600}=40"), 1.6)


def k1rrms():                                            # 3.6
    _formel("k1rrms", _al(r"&\mathbf x=" + _sp(0, 1, 0, -1),
                          r"\operatorname{rms}(\mathbf x)=\sqrt{\frac14\sum_{i=1}^4x_i^2}&=\sqrt{\tfrac14\,\bigl(x_1^2+x_2^2+x_3^2+x_4^2\bigr)}",
                          r"&=\sqrt{\tfrac14\,\bigl(0^2+1^2+0^2+(-1)^2\bigr)}",
                          r"&=\sqrt{\tfrac14\,(0+1+0+1)}=\sqrt{\tfrac24}=\tfrac1{\sqrt2}"), 2.4)


def k1rabstand():                                        # 4.1
    _formel("k1rabstand", _al(r"&\mathbf x_1-\mathbf x_2=" + X1 + "-" + _sp(40, 1, 1) + "=" + _sp(20, 1, 2),
                              r"\lVert\mathbf x_1-\mathbf x_2\rVert=\sqrt{\sum_{j=1}^3(x_{1j}-x_{2j})^2}&=\sqrt{20^2+1^2+2^2}",
                              r"&=\sqrt{400+1+4}=\sqrt{405}"), 1.9)


def k1rzentriert():                                      # 4.3
    _formel("k1rzentriert", _al(r"\bar v=\tfrac14\sum_{i=1}^4v_i&=\tfrac14\,(v_1+v_2+v_3+v_4)",
                                r"&=\tfrac14\,(60+40+90+70)=\tfrac{260}4=65",
                                r"\mathbf 1^\top\tilde{\mathbf v}=\sum_{i=1}^4(v_i-\bar v)&=(-5)+(-25)+25+5=0"), 1.6)


def k1rstd():                                            # 4.4
    _formel("k1rstd", _al(r"\operatorname{std}(\mathbf v)&=\sqrt{\tfrac14\sum_{i=1}^4(v_i-\bar v)^2}",
                          r"&=\sqrt{\tfrac14\,\bigl((-5)^2+(-25)^2+25^2+5^2\bigr)}",
                          r"&=\sqrt{\tfrac14\,(25+625+625+25)}=\sqrt{\tfrac{1\,300}4}=\sqrt{325}"), 1.9)


def k1rwinkel():                                         # 5.2
    _formel("k1rwinkel", _al(r"\cos\varphi&=\frac{1\cdot1+0\cdot1+1\cdot0}{\sqrt{1^2+0^2+1^2}\,\sqrt{1^2+1^2+0^2}}",
                             r"&=\frac{1+0+0}{\sqrt2\,\sqrt2}=\frac12,\qquad \varphi=60^\circ"), 1.4)


def k1rortho():                                          # 5.3
    _formel("k1rortho", _al(r"&\mathbf 1=" + _sp(1, 1, 1, 1) + r",\quad \mathbf w=" + _sp(1, -1, 1, -1)
                            + r",\quad \mathbf x=" + _sp(3, 1, 3, 1),
                            r"\mathbf 1^\top\mathbf w&=1\cdot1+1\cdot(-1)+1\cdot1+1\cdot(-1)=1-1+1-1=0",
                            r"\mathbf 1^\top\mathbf x&=1\cdot3+1\cdot1+1\cdot3+1\cdot1=3+1+3+1=8",
                            r"\mathbf w^\top\mathbf x&=1\cdot3+(-1)\cdot1+1\cdot3+(-1)\cdot1=3-1+3-1=4"), 2.2)


def k1rkosinus():                                        # 5.4
    _formel("k1rkosinus", _al(r"\mathbf x_1^\top\mathbf x_2&=3\cdot6+2\cdot4+0\cdot0=18+8+0=26",
                              r"\lVert\mathbf x_1\rVert^2&=3^2+2^2+0^2=9+4+0=13",
                              r"\lVert\mathbf x_2\rVert^2&=6^2+4^2+0^2=36+16+0=52",
                              r"\frac{\mathbf x_1^\top\mathbf x_2}{\lVert\mathbf x_1\rVert\,\lVert\mathbf x_2\rVert}"
                              r"&=\frac{26}{\sqrt{13}\,\sqrt{52}}=\frac{26}{\sqrt{676}}=\frac{26}{26}=1",
                              r"\mathbf x_1^\top\mathbf x_3&=3\cdot0+2\cdot1+0\cdot3=0+2+0=2",
                              r"\lVert\mathbf x_3\rVert^2&=0^2+1^2+3^2=0+1+9=10",
                              r"\frac{\mathbf x_1^\top\mathbf x_3}{\lVert\mathbf x_1\rVert\,\lVert\mathbf x_3\rVert}"
                              r"&=\frac{2}{\sqrt{13}\,\sqrt{10}}=\frac2{\sqrt{130}}"), 3.0)


def k1rschatten():                                       # 5.5
    s = Szene("ml/k1rschatten")
    s.skalarprodukt([0.6, 0.8], [3, 1], namen=("u", "x"), index="j")
    s.speichern()


def k1rmv():                                             # 7.1
    _formel("k1rmv", _al(r"(\mathbf A\mathbf x)_i=\sum_{j=1}^2a_{ij}\,x_j&=a_{i1}x_1+a_{i2}x_2",
                         r"(\mathbf A\mathbf x)_1&=1\cdot2+2\cdot1=2+2=4",
                         r"(\mathbf A\mathbf x)_2&=0\cdot2+(-1)\cdot1=0-1=-1",
                         r"(\mathbf A\mathbf x)_3&=3\cdot2+1\cdot1=6+1=7"), 1.45)


def k1rzeilen():                                         # 7.2
    _formel("k1rzeilen", _al(r"\hat y_i=\mathbf x_i^\top\mathbf w&=\sum_{j=1}^3x_{ij}\,w_j=x_{i1}w_1+x_{i2}w_2+x_{i3}w_3",
                             r"\hat y_1&=60\cdot3+2\cdot10+3\cdot(-4)=180+20-12=188",
                             r"\hat y_2&=40\cdot3+1\cdot10+1\cdot(-4)=120+10-4=126",
                             r"\hat y_3&=90\cdot3+4\cdot10+6\cdot(-4)=270+40-24=286",
                             r"\hat y_4&=70\cdot3+3\cdot10+2\cdot(-4)=210+30-8=232"), 1.75)


def k1rspalten():                                        # 7.3
    a1, a2, a3 = _sp(60, 40, 90, 70), _sp(2, 1, 4, 3), _sp(3, 1, 6, 2)
    _formel("k1rspalten", _al(r"\mathbf X\mathbf w=\sum_{j=1}^3w_j\,\mathbf a_j&=w_1\mathbf a_1+w_2\mathbf a_2+w_3\mathbf a_3",
                              r"&=3" + a1 + "+10" + a2 + "+(-4)" + a3,
                              r"&=" + _sp(180, 120, 270, 210) + "+" + _sp(20, 10, 40, 30) + "+" + _sp(-12, -4, -24, -8)
                              + "=" + _sp(188, 126, 286, 232)), 3.0)


def k1rprodukt():                                        # 9.1
    _formel("k1rprodukt", _al(r"(\mathbf A\mathbf B)_{il}=\sum_{j=1}^2a_{ij}\,b_{jl}&=a_{i1}b_{1l}+a_{i2}b_{2l}",
                              r"(\mathbf A\mathbf B)_{11}&=1\cdot0+2\cdot1=0+2=2",
                              r"(\mathbf A\mathbf B)_{12}&=1\cdot1+2\cdot0=1+0=1",
                              r"(\mathbf A\mathbf B)_{21}&=0\cdot0+1\cdot1=0+1=1",
                              r"(\mathbf A\mathbf B)_{22}&=0\cdot1+1\cdot0=0+0=0"), 1.7)


def k1raeusser():                                        # 9.5
    _formel("k1raeusser", _al(r"\mathbf A\mathbf B&=\mathbf a_1\begin{pmatrix}0&1\end{pmatrix}+\mathbf a_2\begin{pmatrix}1&0\end{pmatrix}"
                              r"=" + _sp(1, 0) + r"\begin{pmatrix}0&1\end{pmatrix}+" + _sp(2, 1) + r"\begin{pmatrix}1&0\end{pmatrix}",
                              r"&=\begin{pmatrix}0&1\\0&0\end{pmatrix}+\begin{pmatrix}2&0\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\1&0\end{pmatrix}"), 1.25)


def k1rgrammerk():                                       # 10.4
    _formel("k1rgrammerk", _al(r"(\mathbf X^\top\mathbf X)_{jl}&=\sum_{i=1}^3x_{ij}\,x_{il}",
                               r"(\mathbf X^\top\mathbf X)_{11}&=3\cdot3+6\cdot6+0\cdot0=9+36+0=45",
                               r"(\mathbf X^\top\mathbf X)_{12}&=3\cdot2+6\cdot4+0\cdot1=6+24+0=30",
                               r"(\mathbf X^\top\mathbf X)_{13}&=3\cdot0+6\cdot0+0\cdot3=0+0+0=0"), 1.45)


def k1rlaplace():                                        # 14.4
    _formel("k1rlaplace", _al(r"\det\mathbf A&=\sum_{j=1}^3(-1)^{1+j}\,a_{1j}\det\mathbf A_{1j}",
                              r"&=a_{11}\det\mathbf A_{11}-a_{12}\det\mathbf A_{12}+a_{13}\det\mathbf A_{13}",
                              r"&=1\cdot\det\begin{pmatrix}1&1\\1&2\end{pmatrix}-2\cdot\det\begin{pmatrix}2&1\\1&2\end{pmatrix}"
                              r"+1\cdot\det\begin{pmatrix}2&1\\1&1\end{pmatrix}",
                              r"&=1\cdot1-2\cdot3+1\cdot1=1-6+1=-4"), 2.3)


RECHENBILDER = (k1rsumme, k1rdoppel, k1rmittelvektor, k1rskp, k1rgewicht, k1rmittel, k1rstrom, k1rmuster, k1rl2, k1rl1, k1rlp,
                k1rfehler, k1rrms, k1rabstand, k1rzentriert, k1rstd, k1rwinkel, k1rortho, k1rkosinus, k1rschatten, k1rmv,
                k1rzeilen, k1rspalten, k1rprodukt, k1raeusser, k1rgrammerk, k1rlaplace)

SZENEN = (k1punktpfeil, k1addition, k1muster, k1einheitskugeln, k1einheiten, k1schatten, k1datenmatrix, k1zeilenspalten,
          k1ebene, k1hinter, k1reihenfolge, k1lgs, k1spann, k1det, k1tensor) + RECHENBILDER

for f in SZENEN:
    f()
