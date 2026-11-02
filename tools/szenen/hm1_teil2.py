"""HM1 Teil 2 (kap2_stufen.tex): Komplexe Zahlen. Rechenmodell z1 = 3 + i, z2 = 1 + 2i.

Aufruf: python tools/szenen/hm1_teil2.py, danach python tools/szenen_ansehen.py out.png hm1/k2parabel ... [--lang de]
Alle Zahlen kommen aus C:/Bücher/HöMa1/Arbeitshefte/rechnung_kap2.py.
Alle komplexen Ebenen haben in x und y denselben Maßstab, sonst stimmen Drehung und Spiegelung im Bild nicht.
"""
import sys
from math import atan2, pi, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KL = 24                    # Punktbeschriftung
Z1, Z2 = (3, 1), (1, 2)
M, BX = 0.55, (-0.3, 4.3)  # Maßstab und x-Bereich der Doppelbilder
BXL = (-0.3, 3.9)          # linkes Teilbild etwas kürzer: Abstand zum rechten


def ebene(s, x, y, m, mitte=(0, 0), xt="", yt="", **kw):
    """Achsenkreuz mit m Szeneneinheiten je Zahlschritt, in beiden Richtungen gleich."""
    return s.achsen(x, y, breite=(x[1] - x[0]) * m, hoehe=(y[1] - y[0]) * m, mitte=mitte, kreuz=True, xticks=xt, yticks=yt,
                    xl="Re", yl="Im", **kw)


def zeiger(s, on, a, b, farbe=BLAU, dicke=4, dash="", spitze=0.2):
    return s.pfeil(a, b, "", farbe=farbe, spitze=spitze, dicke=dicke, on=on, dash=dash)


# ------------------------------------------------------------------------------------------ Stufe 1
def k2parabel():
    """Parabel y = x² mit den Geraden y = 2 (zwei Schnittpunkte) und y = -1 (keiner)."""
    s = Szene("hm1/k2parabel")
    a = s.achsen((-2.4, 2.4), (-1.5, 4.2), breite=3.7, hoehe=2.6, kreuz=True, xticks="-2;-1;1;2", yticks="1;3;4", xl="x", yl="y")
    s.kurve(a, "x^2", x=(-2.0, 2.0), farbe=BLAU)
    s.text(a, "y = x²", (1.5, 3.8), ausrichtung="right", farbe=BLAU)
    r2 = sqrt(2)
    s.linie(a, (-2.3, 2), (2.3, 2), farbe=GRUEN, dicke=3)
    s.linie(a, (-2.3, -1), (2.3, -1), farbe=ROT, dicke=3)
    for x in (-r2, r2):
        s.linie(a, (x, 2), (x, 0), farbe=GRUEN, dicke=2, dash=DASH)
        s.punkt(a, x, 2, farbe=GRUEN)
        s.punkt(a, x, 0, farbe=GRUEN)
    s.text(a, "−√2", (-r2 - 0.1, 0.55), KL, "right", GRUEN)
    s.text(a, "√2", (r2 + 0.1, 0.55), KL, "left", GRUEN)
    zwei = s.tr("zwei", "y = 2: zwei Lösungen", "y = 2: two solutions", "y = 2: dos soluciones", "y = 2：两个解")
    kein = s.tr("kein", "y = −1: keine Lösung", "y = −1: no solution", "y = −1: sin solución", "y = −1：无解")
    s.text(a, zwei, (2.5, 2), KL, "left", GRUEN)
    s.text(a, kein, (2.5, -1), KL, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 2
def k2ebene():
    """Links z1, z2 und ihre Summe als Parallelogramm, rechts vier Drehungen von z1 um je 90 Grad."""
    s = Szene("hm1/k2ebene")
    a = ebene(s, (-0.4, 4.5), (-0.4, 3.5), 0.56, mitte=(-1.66, 0), xt="1;2;3;4", yt="1;2;3")
    S = (4, 3)
    s.linie(a, (-0.4, 0), (4.5, 0), farbe=ORANGE, dicke=4)
    s.linie(a, Z1, (3, 0), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.linie(a, Z1, (0, 1), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.linie(a, S, (4, 0), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.linie(a, S, (0, 3), farbe=HELLGRAU, dicke=2, dash=DASH)
    zeiger(s, a, Z1, S, GRAU, 3, DASH)
    zeiger(s, a, Z2, S, GRAU, 3, DASH)
    zeiger(s, a, (0, 0), S, ROT)
    zeiger(s, a, (0, 0), Z1, BLAU)
    zeiger(s, a, (0, 0), Z2, GRUEN)
    s.text(a, "z_1 = 3 + i", (1.45, 0.28), KL, "left", BLAU)
    s.text(a, "z_2 = 1 + 2i", (0.16, 2.6), KL, "left", GRUEN)
    s.text(a, "z_1 + z_2 = 4 + 3i", (3.2, 3.36), KL, "center", ROT)

    b = ebene(s, (-3.7, 3.7), (-3.6, 3.6), 0.38, mitte=(1.66, 0.12), xt="-3;-2;-1;1;2;3", yt="-3;-2;-1;1;2;3", xzahlen=False, yzahlen=False)
    ecken = [(3, 1), (-1, 3), (-3, -1), (1, -3)]
    r = sqrt(10)
    w0 = atan2(1, 3)
    for k in range(4):
        w1 = w0 + k * pi / 2 + 0.07
        w2 = w0 + (k + 1) * pi / 2 - 0.07
        s.weg(b, "%.4f*cos(t)" % r, "%.4f*sin(t)" % r, w1, w2, farbe=HELLGRAU, dicke=2.5, pfeile="0.55")
    for p, f in zip(ecken, (BLAU, GRUEN, ORANGE, ROT)):
        zeiger(s, b, (0, 0), p, f, 4)
    s.text(b, "z_1", (3.2, 1.3), KL, "left", BLAU)
    s.text(b, "i z_1", (-1.25, 3.5), KL, "right", GRUEN)
    s.text(b, "i² z_1", (-3.2, -1.45), KL, "right", ORANGE)
    s.text(b, "i³ z_1", (1.3, -3.4), KL, "left", ROT)
    for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        s.punkt(b, x, y, farbe=GRAU, r=0.055)
    s.text(b, "1", (1.05, -0.72), KL, "center", GRAU)
    s.text(b, "i", (0.42, 1.08), KL, "center", GRAU)
    s.text(b, "−1", (-1.15, 0.72), KL, "center", GRAU)
    s.text(b, "−i", (-0.6, -1.08), KL, "center", GRAU)
    s.text(b, "90°", (1.95, 3.45), KL, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 3
def k2konjugiert():
    """z1 und sein Spiegelbild, Summe auf der reellen, Differenz auf der imaginären Achse."""
    s = Szene("hm1/k2konjugiert")
    a = ebene(s, (-0.5, 6.9), (-1.7, 2.5), 0.6, xt="1;2;3;4;5;6", yt="-1;1;2", xzahlen=False)
    s.text(a, "6", (6.0, -0.5), KL, "center", ROT)
    Q = (3, -1)
    zeiger(s, a, Z1, (6, 0), GRAU, 3, DASH)
    zeiger(s, a, Q, (6, 0), GRAU, 3, DASH)
    zeiger(s, a, Q, Z1, GRUEN, 3)
    zeiger(s, a, (0, 0), (6, 0), ROT)
    zeiger(s, a, (0, 0), (0, 2), GRUEN)
    zeiger(s, a, (0, 0), Z1, BLAU)
    zeiger(s, a, (0, 0), Q, ORANGE)
    s.text(a, "z_1 = 3 + i", (3.1, 1.42), KL, "center", BLAU)
    s.text(a, "z̄_1 = 3 − i", (3.1, -1.42), KL, "center", ORANGE)
    s.text(a, "z_1 + z̄_1 = 6", (6.0, 0.5), KL, "center", ROT)
    s.text(a, "z_1 − z̄_1 = 2i", (0.25, 2.25), KL, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 4
def k2kehrwert():
    """Kehrwert von z2: spiegeln, dann durch 5 teilen. Der Pfeil des zweiten Schritts läuft neben dem Pfeil von z̄2."""
    s = Szene("hm1/k2kehrwert")
    a = ebene(s, (-0.7, 2.9), (-2.4, 2.4), 0.6, xt="2", yt="-2;-1;1;2")
    Q = (1, -2)
    K = (0.2, -0.4)
    n = (-0.894 * 0.2, -0.447 * 0.2)                       # Versatz senkrecht zum Pfeil von z̄2
    zeiger(s, a, (1.0, -1.9), (1.0, 1.9), GRAU, 2.5, DASH)
    zeiger(s, a, (Q[0] + n[0], Q[1] + n[1]), (0.34 + n[0], -0.68 + n[1]), GRAU, 2.5, DASH)
    zeiger(s, a, (0, 0), Z2, GRUEN)
    zeiger(s, a, (0, 0), Q, ORANGE)
    zeiger(s, a, (0, 0), K, ROT, 4.5, spitze=0.14)
    s.text(a, "z_2 = 1 + 2i", (1.2, 2.06), KL, "left", GRUEN)
    s.text(a, "z̄_2 = 1 − 2i", (1.2, -2.08), KL, "left", ORANGE)
    s.text(a, "1/z_2 = 0.2 − 0.4i", (-0.2, -0.42), KL, "right", ROT)
    eins = s.tr("s1", "1. spiegeln", "1. reflect", "1. reflejar", "1. 镜像")
    zwei = s.tr("s2", "2. durch 5 teilen", "2. divide by 5", "2. dividir por 5", "2. 除以 5")
    s.text(a, eins, (1.2, 0.7), KL, "left", GRAU)
    s.text(a, zwei, (-0.2, -1.5), KL, "right", GRAU)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 5
def k2betrag():
    """Links Betrag und Abstand mit Katheten, rechts die Dreiecksungleichung."""
    s = Szene("hm1/k2betrag")
    a = ebene(s, BXL, (-0.4, 3.5), M, mitte=(-1.8, 0), xt="1;2;3", yt="1;2;3")
    s.linie(a, (3, 0), Z1, farbe=BLAU, dicke=2, dash=DASH)
    s.linie(a, Z2, (1, 1), farbe=GRUEN, dicke=2, dash=DASH)
    s.linie(a, (1, 1), Z1, farbe=GRUEN, dicke=2, dash=DASH)
    s.linie(a, (0, 0), Z1, farbe=BLAU, dicke=4)
    s.linie(a, Z2, Z1, farbe=GRUEN, dicke=4)
    s.punkt(a, *Z1, farbe=SCHWARZ)
    s.punkt(a, *Z2, farbe=SCHWARZ)
    s.text(a, "z_1", (3.14, 1.3), KL, "left")
    s.text(a, "z_2", (0.86, 2.34), KL, "right")
    s.text(a, "|z_1| = √10", (3.14, 0.5), KL, "left", BLAU)
    s.text(a, "d(z_1, z_2) = √5", (1.55, 2.1), KL, "left", GRUEN)

    b = ebene(s, BX, (-0.4, 3.5), M, mitte=(1.68, 0), xt="1;2;3;4", yt="1;2;3")
    S = (4, 3)
    s.linie(b, (0, 0), S, farbe=ROT, dicke=4)
    s.linie(b, (0, 0), Z1, farbe=BLAU, dicke=4)
    s.linie(b, Z1, S, farbe=GRUEN, dicke=4)
    s.punkt(b, *Z1, farbe=SCHWARZ)
    s.punkt(b, *S, farbe=SCHWARZ)
    s.text(b, "|z_1 + z_2| = 5", (0.16, 2.34), KL, "left", ROT)
    s.text(b, "|z_1| = √10", (3.2, 0.62), KL, "left", BLAU)
    s.text(b, "|z_2| = √5", (3.72, 1.62), KL, "left", GRUEN)
    s.speichern()


# ------------------------------------------------------------------------------------------ Stufe 6
def k2loesungen():
    """Lösungen zweier quadratischer Gleichungen: symmetrisch zur Mitte -p/2."""
    s = Szene("hm1/k2loesungen")
    a = ebene(s, BXL, (-1.7, 1.9), M, mitte=(-1.8, -0.05), xt="1;2", yt="-1;1")
    s.linie(a, (3, 1), (3, -1), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, 3, 1, farbe=BLAU, r=0.09)
    s.punkt(a, 3, -1, farbe=BLAU, r=0.09)
    s.punkt(a, 3, 0, farbe=ROT, r=0.08)
    s.text(a, "3 + i", (3.18, 1.2), KL, "left", BLAU)
    s.text(a, "3 − i", (3.18, -1.2), KL, "left", BLAU)
    s.text(a, "−p/2 = 3", (2.85, 0.34), KL, "right", ROT)
    s.text(a, "z² − 6z + 10 = 0", (2.1, 2.3), KL, "center")

    b = ebene(s, BX, (-0.4, 3.2), M, mitte=(1.68, -0.05), xt="1;2;3;4", yt="1;2;3")
    C = (2, 1.5)
    zeiger(s, b, C, Z1, GRAU, 3)
    zeiger(s, b, C, Z2, GRAU, 3)
    s.punkt(b, *Z1, farbe=BLAU, r=0.09)
    s.punkt(b, *Z2, farbe=BLAU, r=0.09)
    s.punkt(b, *C, farbe=ROT, r=0.08)
    s.text(b, "z_1", (3.2, 1.14), KL, "left", BLAU)
    s.text(b, "z_2", (0.8, 2.14), KL, "right", BLAU)
    s.text(b, "−p/2", (2.14, 1.86), KL, "left", ROT)
    s.text(b, "+w", (2.7, 1.5), KL, "left", GRAU)
    s.text(b, "−w", (1.3, 1.48), KL, "right", GRAU)
    s.text(b, "z² − (4 + 3i)z + 1 + 7i = 0", (2.1, 3.6), KL, "center")
    s.speichern()


if __name__ == "__main__":
    for f in (k2parabel, k2ebene, k2konjugiert, k2kehrwert, k2betrag, k2loesungen):
        f()
