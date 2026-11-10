"""Beispiele für Ebene abbilden (L5, Anleitung: notizen/animationen.md §9).

Bauen:  python tools/szenen/beispiel_gitter.py
Export: python tools/export_szenen.py --animiert beispiel/anim_l5_scherung beispiel/anim_l5_determinante \
            beispiel/anim_l5_eigen beispiel/anim_l5_svd beispiel/anim_l5_nacheinander beispiel/anim_l5_polar

s.gitter legt ein Koordinatengitter an, s.abbilden(A, [Objekte]) verformt die Ebene mit der Matrix A über die Zeit:
Jeder Punkt p läuft nach A p, das Gitter wird am Fenster der Achsen abgeschnitten. Punkte bleiben rund, Pfeile behalten
ihre Spitze, ein Kreis wird zur Ellipse. Das statische Bild und das PDF zeigen das Endbild.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

GITTER = "#8fa6c8"
GEIST = "#d5dbe5"


def ebene(s, x, y, breite, hoehe, mitte=(0, 0), schritt=1.0, geist=True, rand=1.0, punkte=2):
    """Achsenkreuz, blasses Geistergitter (bleibt stehen) und das Gitter, das sich verformt."""
    a = s.achsen(x, y, breite=breite, hoehe=hoehe, mitte=mitte, kreuz=True, xzahlen=False, yzahlen=False,
                 xmarks=False, ymarks=False)
    g0 = s.gitter(a, schritt, farbe=GEIST, dicke=2, rand=0) if geist else None
    g = s.gitter(a, schritt, farbe=GITTER, dicke=2, rand=rand, punkte=punkte, achsen_dicke=3)
    return a, g0, g


def scherung():
    """Scherung A = (1 1; 0 1): e1 bleibt, e2 kippt nach (1, 1); waagrechte Gitterlinien bleiben waagrecht."""
    s = Szene("beispiel/anim_l5_scherung", reihenfolge="anlegen")
    s.welt()
    a, g0, g = ebene(s, (-3, 3), (-2, 2), 4.8, 3.2, mitte=(-1.2, 0))
    e1 = s.vektor(a, (1, 0), label="e_1", farbe=ROT, label_seite="right")
    e2 = s.vektor(a, (0, 1), label="e_2", farbe=GRUEN)
    m = s.formel(r"A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}", mitte=(2.55, 0.9), hoehe=0.62)
    s.einblenden(a, g0, g, dauer=0.6)
    s.einblenden(e1, e2, dauer=0.6)
    s.einblenden(m, dauer=0.5)
    s.pause(0.4)
    s.abbilden([[1, 1], [0, 1]], [g, e1, e2], dauer=2.5)
    s.pause(0.6)
    s.speichern()


def determinante():
    """Das Einheitsquadrat wird zum Parallelogramm aus a1 = (3, 1) und a2 = (1, 2); die Fläche läuft als Zahl mit
    (|det| der Zwischenmatrix) und endet bei det A = 5."""
    s = Szene("beispiel/anim_l5_determinante", reihenfolge="anlegen")
    s.welt()
    a, g0, g = ebene(s, (-1, 4.5), (-1, 3.5), 4.0, 3.3, mitte=(-1.65, 0))
    A = [[3, 1], [1, 2]]
    q = s.vieleck(a, [(0, 0), (1, 0), (1, 1), (0, 1)], farbe=ORANGE, deckung=0.35, dicke=3)
    e1 = s.vektor(a, (1, 0), label="e_1", farbe=ROT, label_seite="right")
    e2 = s.vektor(a, (0, 1), label="e_2", farbe=GRUEN)
    z = s.zahl(None, "abs(" + det_ausdruck(A, "s") + ")", (0.8, 1.0), stellen=2,
               vor=s.tr("fl", de="Fläche = ", en="area = ", es="área = ", zh="面积 = ", fr="aire = ", tr="alan = "))
    m = s.formel(r"A = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}", mitte=(1.6, -0.05), hoehe=0.62)
    d = s.formel(r"\det A = 3\cdot 2 - 1\cdot 1 = 5", mitte=(-1.65, -2.05), hoehe=0.19)
    s.einblenden(a, g0, g, dauer=0.6)
    s.einblenden(q, e1, e2, z, m, dauer=0.6)
    s.pause(0.4)
    s.abbilden(A, [g, q, e1, e2], dauer=3.0, parameter="s")
    s.einblenden(d, dauer=0.6)
    s.pause(0.6)
    s.speichern()


def eigen():
    """A = (4 1; 2 3): v1 auf der Geraden y = x wird nur 5-mal so lang, v2 auf y = -2x nur 2-mal so lang; w kippt."""
    s = Szene("beispiel/anim_l5_eigen", reihenfolge="anlegen")
    s.welt()
    a, g0, g = ebene(s, (-3, 3), (-3, 3), 4.4, 4.4, mitte=(-1.5, 0), geist=False, rand=2.0)
    h1 = s.linie(a, (-3, -3), (3, 3), farbe=BLAU, dicke=2, dash=DASH)
    h2 = s.linie(a, (-1.5, 3), (1.5, -3), farbe=ORANGE, dicke=2, dash=DASH)
    v1 = s.vektor(a, (0.5, 0.5), label="v_1", farbe=BLAU)
    v2 = s.vektor(a, (-0.3, 0.6), label="v_2", farbe=ORANGE)
    w = s.vektor(a, (0.6, 0), label="w", farbe=ROT, label_seite="right")
    m = s.formel(r"A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}", mitte=(2.2, 1.3), hoehe=0.62)
    t1 = s.formel(r"A\mathbf v_1 = 5\,\mathbf v_1", mitte=(2.2, 0.35), hoehe=0.21, farbe=BLAU)
    t2 = s.formel(r"A\mathbf v_2 = 2\,\mathbf v_2", mitte=(2.2, -0.25), hoehe=0.21, farbe=ORANGE)
    t3 = s.text(None, s.tr("kippt", de="A w kippt", en="A w tilts", es="A w se inclina", zh="A w 转向",
                           fr="A w bascule", tr="A w döner"), (2.2, -0.85), groesse=TEXT, farbe=ROT, ausrichtung="center")
    s.einblenden(a, g, h1, h2, m, dauer=0.6)
    s.einblenden(v1, v2, w, dauer=0.6)
    s.pause(0.4)
    s.abbilden([[4, 1], [2, 3]], [g, v1, v2, w], dauer=3.0)
    s.einblenden(t1, t2, t3, nacheinander=True, dauer=0.5)
    s.pause(0.5)
    s.speichern()


def svd():
    """A = U Σ Vᵀ = (2 3; 0 2) in drei Schritten: Vᵀ dreht v1, v2 auf die Achsen, Σ streckt um 4 und 1, U dreht auf
    u1, u2. Der Einheitskreis wird zur Ellipse mit den Halbachsen 4 u1 und 1 u2."""
    s = Szene("beispiel/anim_l5_svd", reihenfolge="anlegen")
    s.welt()
    a, g0, g = ebene(s, (-4, 4), (-2.5, 2.5), 6.4, 4.0, geist=True, rand=1.5)
    r5 = 5 ** 0.5
    k = s.kreis(a, 0, 0, 1, farbe=SCHWARZ, dicke=3)
    v1 = s.vektor(a, (1 / r5, 2 / r5), farbe=BLAU)
    v2 = s.vektor(a, (-2 / r5, 1 / r5), farbe=ORANGE)
    l1 = s.text(a, "v_1", (0.62, 1.12), groesse=TEXT, farbe=BLAU, ausrichtung="center")
    l2 = s.text(a, "v_2", (-1.18, 0.62), groesse=TEXT, farbe=ORANGE, ausrichtung="center")
    m1 = s.text(a, "σ_1 u_1 = 4 u_1", (2.1, 2.2), groesse=TEXT, farbe=BLAU, ausrichtung="center")
    m2 = s.text(a, "σ_2 u_2 = u_2", (-1.25, 1.3), groesse=TEXT, farbe=ORANGE, ausrichtung="center")
    s.tr("dreh", de="drehen", en="rotate", es="girar", zh="旋转", fr="tourner", tr="döndür")
    s.tr("streck", de="strecken (4 und 1)", en="stretch (4 and 1)", es="estirar (4 y 1)", zh="拉伸 (4 和 1)",
         fr="étirer (4 et 1)", tr="ger (4 ve 1)")
    schritte = [s.text(None, x, (0, -2.4), groesse=TEXT, ausrichtung="center", farbe=GRAU) for x in
                ("1. V^T: @{dreh}", "2. Σ: @{streck}", "3. U: @{dreh}")]
    alle = [g, k, v1, v2, l1, l2]
    c, d = 1 / r5, 2 / r5
    Vt = [[c, d], [-d, c]]                       # dreht v1 auf e1 (−63,4°)
    U = [[d, -c], [c, d]]                        # dreht e1 auf u1 (+26,6°)
    s.einblenden(a, g0, g, dauer=0.6)
    s.zeichnen(k, dauer=0.8)
    s.einblenden(v1, v2, l1, l2, dauer=0.6)
    for nr, (M, weg) in enumerate(((Vt, "drehung"), ([[4, 0], [0, 1]], "gerade"), (U, "drehung"))):
        s.einblenden(schritte[nr], dauer=0.4)
        s.abbilden(M, alle, dauer=1.6, weg=weg)
        s.ausblenden(schritte[nr], dauer=0.3)
    with s.gleichzeitig():
        s.ausblenden(l1, l2, dauer=0.4)
        s.einblenden(m1, m2, dauer=0.6)
    s.pause(0.6)
    s.speichern()


def nacheinander():
    """Erst D (Drehung um 90°), dann S (Scherung): das Bild ist S·D; das Einheitsquadrat zeigt jeden Schritt."""
    s = Szene("beispiel/anim_l5_nacheinander", reihenfolge="anlegen")
    s.welt()
    a, g0, g = ebene(s, (-3, 3), (-2, 2.5), 4.8, 3.6, mitte=(-1.3, 0))
    q = s.vieleck(a, [(0, 0), (1, 0), (1, 1), (0, 1)], farbe=ORANGE, deckung=0.35)
    e1 = s.vektor(a, (1, 0), label="e_1", farbe=ROT, label_seite="right")
    e2 = s.vektor(a, (0, 1), label="e_2", farbe=GRUEN)
    s.tr("d90", de="Drehung um 90°", en="rotation by 90°", es="giro de 90°", zh="旋转 90°", fr="rotation de 90°",
         tr="90° döndürme")
    s.tr("sch", de="Scherung", en="shear", es="cizalla", zh="剪切", fr="cisaillement", tr="kayma")
    t1 = s.text(None, "1. D: @{d90}", (1.35, 1.5), groesse=TEXT)
    t2 = s.text(None, "2. S: @{sch}", (1.35, 0.95), groesse=TEXT)
    t3 = s.formel(r"SD = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}", mitte=(2.38, -0.6), hoehe=0.62)
    s.einblenden(a, g0, g, dauer=0.6)
    s.einblenden(q, e1, e2, dauer=0.5)
    s.einblenden(t1, dauer=0.4)
    s.abbilden([[0, -1], [1, 0]], [g, q, e1, e2], dauer=2.0, weg="drehung")
    s.einblenden(t2, dauer=0.4)
    s.abbilden([[1, 1], [0, 1]], [g, q, e1, e2], dauer=2.0)
    s.einblenden(t3, dauer=0.5)
    s.pause(0.6)
    s.speichern()


def polar():
    """Nichtlineare Abbildung: das Rechteck r ∈ [0, 2], u ∈ [0, 4] wird mit (r cos(πu/2), r sin(πu/2)) zur Kreisscheibe;
    Linien r = konst. werden Kreise, Linien u = konst. Strahlen."""
    s = Szene("beispiel/anim_l5_polar", reihenfolge="anlegen")
    a = s.achsen((-2.3, 2.3), (-2.3, 4.3), breite=3.45, hoehe=4.95, kreuz=True, xzahlen=False, yzahlen=False,
                 xmarks=False, ymarks=False)
    g = s.gitter(a, 0.5, farbe=GITTER, dicke=2, rand=0, punkte=25, zuschneiden=False, x=(0, 2), y=(0, 4))
    s.einblenden(a, g, dauer=0.6)
    s.pause(0.4)
    s.abbilden_funktion("x*cos(pi*y/2)", "x*sin(pi*y/2)", [g], dauer=3.0)
    s.pause(0.6)
    s.speichern()


for f in (scherung, determinante, eigen, svd, nacheinander, polar):
    f()
