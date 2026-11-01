"""ET3 Teil 5 (Tiefpass): die sechs Abbildungen aus kap5_stufen_a.tex und kap5_stufen_b.tex als Editor-Szenen.

Aufruf vom Repo-Root: python tools/szenen/et3_teil5.py  (schreibt web/szenen/et3/k5*.json)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")
HELLBLAU = "#6aa1e2"       # elblue!70 des Hefts


def k5sprung():
    """Sprungantwort des idealen Tiefpasses für f_g = 1 Hz und 2 Hz, Rampe, Überschwingen auf 1,0895."""
    s = Szene("et3/k5sprung")
    a = s.achsen((-1.5, 2, 0.5), (-0.15, 1.3), breite=6.0, hoehe=2.6, mitte=(0.35, 0), gitter=True, yticks="0;0.5;1",
                 xl=s.tr("t", "t in s", "t in s", "t en s", "t / s"), yl="h_ε(t)")
    s.daten(a, duenn(daten(DAT / "k5_sprung.dat", 1, 2), 1e-4), farbe=BLAU)
    s.daten(a, duenn(daten(DAT / "k5_sprung.dat", 1, 3), 1e-4), farbe=ROT)
    s.linie(a, (-0.25, 0), (0.25, 1), farbe=BLAU, dash=DASH)
    s.linie(a, (-1.5, 1.0895), (2, 1.0895), farbe=GRAU, dash=DASH)
    s.text(a, "1.0895", (0.6, 1.18))
    s.text(a, "f_g = 1 Hz", (-0.28, 0.42), ausrichtung="right", farbe=BLAU)
    s.text(a, "f_g = 2 Hz", (0.2, 0.28), farbe=ROT)
    s.speichern()


def k5kausal():
    """Betrag des kausal gefensterten Tiefpasses, gestrichelt das Ideal."""
    s = Szene("et3/k5kausal")
    a = s.achsen((0, 2.5, 0.2), (0, 1.2), breite=6.0, hoehe=2.4, mitte=(0.35, 0), gitter=True, yticks="0;0.5;1",
                 xl=s.tr("f", "f in Hz", "f in Hz", "f en Hz", "f / Hz"), yl="|H_k(f)|")
    s.daten(a, [(0, 1), (1, 1), (1, 0), (2.5, 0)], farbe=GRAU, dash=DASH)
    s.daten(a, duenn(daten(DAT / "k5_kausal.dat"), 1e-4), farbe=BLAU)
    s.speichern()


def k5pulsform():
    """Impulsantworten: idealer Tiefpass und Cosine-Rolloff (gleiche Fläche T), als Formeln."""
    s = Szene("et3/k5pulsform")
    a = s.achsen((-5, 5, 1), (-0.3, 1.1), breite=6.0, hoehe=2.4, mitte=(0.35, 0), gitter=True, yticks="0;0.5;1", xl="t/T")
    s.kurve(a, "si(pi*x)", farbe=GRAU, dicke=4)
    s.kurve(a, "(si(pi*x)+0.5*si(pi*(x+1))+0.5*si(pi*(x-1)))/2", farbe=ROT, dicke=4)
    s.text(a, s.tr("ideal", "idealer Tiefpass", "ideal lowpass", "paso bajo ideal", "理想低通"), (0.75, 0.78), farbe=GRAU)
    s.text(a, s.tr("rolloff", "Cosine-Rolloff, a = ½", "raised cosine, a = ½", "coseno alzado, a = ½", "升余弦，a = ½"), (1.35, 0.32), farbe=ROT)
    s.speichern()


def k5fenster():
    """FIR-Betragsgang in dB: Rechteck- und Hann-Fenster, Grenzfrequenz 0,2."""
    s = Szene("et3/k5fenster")
    a = s.achsen((0, 0.5, 0.1), (-80, 5, 20), breite=6.0, hoehe=2.7, mitte=(0.35, 0), gitter=True,
                 xl=s.tr("f", "f (bezogen auf die Abtastrate)", "f (normalized to the sampling rate)",
                         "f (normalizada a la frecuencia de muestreo)", "f（对采样率归一化）"),
                 yl=s.tr("db", "20 lg|H| in dB", "20 lg|H| in dB", "20 lg|H| en dB", "20 lg|H| / dB"))
    s.daten(a, duenn(daten(DAT / "k5_fenster.dat", 1, 2), 1e-4), farbe=BLAU)
    s.daten(a, duenn(daten(DAT / "k5_fenster.dat", 1, 3), 1e-4), farbe=ROT)
    s.linie(a, (0.2, -80), (0.2, 5), farbe=GRAU, dash=DASH)
    s.tr("rect", "Rechteckfenster", "rectangular window", "ventana rectangular", "矩形窗")
    s.tr("hann", "Hann-Fenster", "Hann window", "ventana de Hann", "汉宁窗")
    s.legende(a, [("@{rect}", BLAU, "-"), ("@{hann}", ROT, "-")], (0.3, -1))
    s.speichern()


def k5bandpass():
    """Antwort des idealen Bandpasses mit Einhüllender +-g_T(t); die untere Einhüllende ist umgerechnet."""
    s = Szene("et3/k5bandpass")
    a = s.achsen((-1.5, 3, 0.5), (-1.2, 1.2), breite=6.0, hoehe=2.5, mitte=(0.35, 0), gitter=True, yticks="-1;0;1",
                 xl=s.tr("t", "t in s", "t in s", "t en s", "t / s"))
    s.daten(a, duenn(daten(DAT / "k5_bandpass.dat", 1, 2), 1e-4), farbe=HELLBLAU, dicke=2)
    env = duenn(daten(DAT / "k5_bandpass.dat", 1, 3), 1e-4)
    s.daten(a, env, farbe=ROT, dicke=4)
    s.daten(a, [(t, -e) for t, e in env], farbe=ROT, dicke=4)
    s.speichern()


def k5quadratur():
    """Quadraturdemodulator: Verzweigung, zwei Multiplizierer, zwei Tiefpässe."""
    s = Szene("et3/k5quadratur")
    tp = s.tr("tp", "Tiefpass", "lowpass", "paso bajo", "低通")
    xs, xv, xm, xt, xa = -3.0, -2.15, -0.95, 0.85, 2.0   # Eingang, Verzweigung, Multiplizierer, Tiefpass, Ausgang
    r, spitze = 0.24, 0.17
    s.text(None, "s(t)", (xs, 0), ausrichtung="center")
    s.draht((xs + 0.38, 0), (xv, 0))
    s.punkt(None, xv, 0, r=0.06)
    for y, sig, res, v in ((0.85, "cos(2π f_0 t)", "½ s_{Tr}(t)", 1), (-0.85, "−sin(2π f_0 t)", "½ s_{Ti}(t)", -1)):
        s.pfeil((xv, 0), (xm - r, y), knick="vh", spitze=spitze)
        s.kreis(None, xm, y, r, fuellung="#ffffff", deckung=1)
        s.text(None, "×", (xm, y), groesse=34, ausrichtung="center")
        s.pfeil((xm + r, y), (xt - 0.7, y), spitze=spitze)
        s.box(tp, (xt, y), breite=1.4, hoehe=0.6)
        s.pfeil((xt + 0.7, y), (xa, y), spitze=spitze)
        s.text(None, res, (xa + 0.12, y), ausrichtung="left")
        s.text(None, sig, (xm, y + v * 1.0), ausrichtung="center")
        s.pfeil((xm, y + v * 0.8), (xm, y + v * r), spitze=spitze)
    s.speichern()


for f in (k5sprung, k5kausal, k5pulsform, k5fenster, k5bandpass, k5quadratur):
    f()
