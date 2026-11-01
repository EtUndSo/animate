"""ET3 Teil 7 (Statistik): die fünf Abbildungen aus kap7_stufen_a.tex und kap7_stufen_b.tex als Editor-Szenen.

Aufruf vom Repo-Root: python tools/szenen/et3_teil7.py  (schreibt web/szenen/et3/k7*.json)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")


def k7schar():
    """Drei Musterfunktionen eines Zufallsprozesses (Werte aus der Datei), Schnitt bei t = 2."""
    s = Szene("et3/k7schar")
    h, abstand = 1.0, 1.12
    for k in range(3):
        unten = k == 2
        a = s.achsen((0, 6, 1), (-0.2, 2.2), breite=5.6, hoehe=h, mitte=(0.1, abstand * (1 - k)), yticks="0;1;2", xzahlen=unten, xl="t" if unten else "",
                     gitter=True)
        s.daten(a, duenn(daten(DAT / "k7_schar.dat", 1, k + 2), 3e-4), farbe=BLAU, dicke=3)
        s.linie(a, (2, -0.2), (2, 2.2), farbe=ROT, dash=DASH)
        s.text(a, "^%ds(t)" % (k + 1), (6.12, 1.0))
    s.speichern()


def k7summen():
    """Dichten von Summen gleichverteilter Größen, dazu die Gaußkurve gleicher Varianz."""
    s = Szene("et3/k7summen")
    a = s.achsen((-1.6, 1.6, 0.5), (0, 1.15), breite=6.0, hoehe=2.6, mitte=(0.35, 0), gitter=True, yticks="0;0.5;1", xl="x",
                 yl=s.tr("dichte", "Dichte", "Density", "densidad", "概率密度"))
    s.daten(a, duenn(daten(DAT / "k7_summen.dat", 1, 2), 1e-6), farbe=BLAU, treppe="post")
    s.kurve(a, "tri(x)", farbe=ROT, dicke=4)
    s.kurve(a, "where(abs(x)<=0.5,0.75-x^2,where(abs(x)<=1.5,0.5*(1.5-abs(x))^2,0))", farbe=GRUEN, dicke=4)
    s.kurve(a, "exp(-2*x^2)/sqrt(pi/2)", farbe=SCHWARZ, dicke=3, dash=DASH)
    s.tr("eine", "eine Größe", "one variable", "una variable", "一个变量")
    s.tr("zwei", "Summe von zwei", "sum of two", "suma de dos", "两个变量之和")
    s.tr("drei", "Summe von drei", "sum of three", "suma de tres", "三个变量之和")
    s.tr("gauss", "Gauß, σ^2 = 3/12", "Gaussian, σ^2 = 3/12", "Gauss, σ^2 = 3/12", "高斯分布，σ^2 = 3/12")
    s.legende(a, [("@{eine}", BLAU, "-"), ("@{zwei}", ROT, "-"), ("@{drei}", GRUEN, "-"), ("@{gauss}", SCHWARZ, "--")], (0.62, 1.05))
    s.speichern()


def k7tp():
    """AKF von tiefpassgefiltertem Rauschen, rote Punkte = Nullstellen bei k/2."""
    s = Szene("et3/k7tp")
    a = s.achsen((-3, 3, 1), (-0.6, 2.2), breite=6.0, hoehe=2.4, mitte=(0.35, 0), gitter=True, xl="τ·f_g", yl="φ_{gg}/(N_0 f_g)", yticks="0;1;2")
    s.kurve(a, "2*si(2*pi*x)", farbe=BLAU, dicke=4)
    for x in (-2.5, -2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2, 2.5):
        s.punkt(a, x, 0, farbe=ROT, r=0.07)
    s.speichern()


def k7pe():
    """Minimale Fehlerwahrscheinlichkeit über E_s/N_0 (einfach logarithmisch), rote Punkte bei 10, 16 und 20 dB."""
    s = Szene("et3/k7pe")
    a = s.achsen((0, 20, 2), (1e-8, 1), breite=6.0, hoehe=3.0, mitte=(0.35, 0), ylog=True, gitter=True, yl="P_{e,min}",
                 xl=s.tr("x", "10 lg(E_s/N_0) in dB", "10 lg(E_s/N_0) in dB", "10 lg(E_s/N_0) en dB", "10 lg(E_s/N_0) / dB"))
    s.daten(a, daten(DAT / "k7_pe.dat"), farbe=BLAU)    # nicht ausdünnen: duenn misst linear, die Achse ist logarithmisch
    for x, y in ((10, 5.69e-2), (16, 8.03e-4), (20, 2.87e-7)):
        s.punkt(a, x, y, farbe=ROT, r=0.07)
    s.speichern()


def k7ar():
    """Leistungsdichte von AR(1)-Prozessen für b = 0,6 und 0,9 (einfach logarithmisch), als Formeln."""
    s = Szene("et3/k7ar")
    a = s.achsen((-1, 1, 0.2), (0.1, 200), breite=6.0, hoehe=2.6, mitte=(0.35, 0), ylog=True, gitter=True, yl="Φ_{gg,a}(f)/σ_s^2",
                 xl=s.tr("f", "f (bezogen auf die Abtastrate)", "f (relative to the sampling rate)",
                         "f (normalizada a la frecuencia de muestreo)", "f（对采样率归一化）"))
    s.kurve(a, "1/(1-2*0.6*cos(2*pi*x)+0.36)", farbe=BLAU, dicke=4)
    s.kurve(a, "1/(1-2*0.9*cos(2*pi*x)+0.81)", farbe=ROT, dicke=4)
    s.text(a, "b = 0.9", (0.13, 40), farbe=ROT)
    s.text(a, "b = 0.6", (-0.5, 1.05), ausrichtung="center", farbe=BLAU)
    s.speichern()


for f in (k7schar, k7summen, k7tp, k7pe, k7ar):
    f()
