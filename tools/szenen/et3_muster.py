"""Muster-Szenen ET3: Mehrfeld, Dirac-Pfeile, Log-Achse mit Daten, Schaltung."""
import sys
from math import pi, sqrt, exp
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")


def k1elementar():
    """Sechs Elementarsignale, 3 x 2 Felder."""
    s = Szene("et3/k1elementar")
    feld = [("sin(t)", -7, 7, -1.3, 1.3, "sin(x)", "-7;7", "-1;1", None),
            ("exp(-pi t^2)", -2, 2, -0.3, 1.3, "exp(-pi*x^2)", "-1;1", "1", None),
            ("ε(t)", -2, 2, -0.3, 1.3, "epsilon(x)", "-1;1", "1", None),
            ("rect(t)", -2, 2, -0.3, 1.3, "rect(x)", "-1;1", "1", None),
            ("Λ(t)", -2, 2, -0.3, 1.3, "tri(x)", "-1;1", "1", None),
            ("0.8 rect((t-2)/2)", -1, 4, -0.3, 1.3, "0.8*rect((x-2)/2)", "1;2;3", "1", None)]
    for k, (titel, x0, x1, y0, y1, f, xt, yt, _) in enumerate(feld):
        spalte, zeile = k % 3, k // 3
        a = s.achsen((x0, x1), (y0, y1), breite=1.9, hoehe=1.2, mitte=(-2.55 + 2.55 * spalte, 1.0 - 2.3 * zeile), titel=titel, kreuz=True,
                     xticks=xt, yticks=yt, xl="t", label=24, zahl=22)
        s.kurve(a, f, farbe=BLAU, dicke=4)
    s.speichern()


def k3kamm():
    """Dirac-Kamm (T = 0.5 s) und Spektrum."""
    s = Szene("et3/k3kamm")
    a = s.achsen((-1.7, 1.7), (0, 1.5), breite=3.0, hoehe=1.8, mitte=(-2.0, 0), kreuz=True, titel="Σ_k δ(t - kT)", xl="t in s", xticks="-1;-0.5;0.5;1",
                 ymarks=False, yzahlen=False, label=24)
    s.stems(a, [k * 0.5 for k in range(-3, 4)], [1] * 7, pfeile=True, farbe=BLAU, dicke=4)
    b = s.achsen((-7, 7), (0, 1.5), breite=3.0, hoehe=1.8, mitte=(2.0, 0), kreuz=True, titel="1/T Σ_k δ(f - k/T)", xl="f in Hz", xticks="-4;-2;2;4",
                 ymarks=False, yzahlen=False, label=24)
    s.stems(b, [2 * k for k in range(-3, 4)], [1] * 7, pfeile=True, farbe=ROT, dicke=4)
    s.speichern()


def k7pe():
    """Fehlerwahrscheinlichkeit über E_s/N0, einfach logarithmisch."""
    s = Szene("et3/k7pe")
    pts = daten(DAT / "k7_pe.dat")
    a = s.achsen((0, 14), (1e-8, 1), breite=4.6, hoehe=3.2, mitte=(0, 0), xl=s.tr("x", "E_s/N_0 in dB", "E_s/N_0 in dB", "E_s/N_0 en dB", "E_s/N_0 (dB)"),
                 yl="P_{e,min}", ylog=True, gitter=True)
    s.daten(a, duenn(pts, 2e-3), farbe=BLAU, dicke=4)
    s.speichern()


def k8element():
    """Ersatzschaltbild eines Leitungsstücks."""
    s = Szene("et3/k8element")
    s.draht((-3.2, 1.2), (-2.6, 1.2))
    s.bauteil("resistor", (-1.9, 1.2), laenge=1.4, label="R'ds")
    s.bauteil("inductor", (-0.1, 1.2), laenge=1.4, label="L'ds", symbol_style="amerikanisch")
    s.draht((-1.2, 1.2), (-0.8, 1.2))
    s.draht((0.6, 1.2), (3.2, 1.2))
    s.draht((-3.2, -0.6), (3.2, -0.6))
    s.bauteil("resistor", (1.1, 0.3), drehung=270, laenge=1.8, label="G'ds", label_flip=True)
    s.bauteil("capacitor", (2.3, 0.3), drehung=270, laenge=1.8, label="C'ds")
    s.pfeil((-3.5, 1.0), (-3.5, -0.4), "", farbe=BLAU)
    s.text(None, "u(s,t)", (-3.65, 0.3), ausrichtung="right", farbe=BLAU)
    s.pfeil((3.5, 1.0), (3.5, -0.4), "", farbe=ROT)
    s.text(None, "u + ∂u/∂s · ds", (3.65, 0.3), farbe=ROT)
    s.pfeil((-3.1, 1.5), (-2.6, 1.5), "")
    s.text(None, "i(s,t)", (-3.3, 1.85), ausrichtung="left")
    s.speichern()


if __name__ == "__main__":  # nur Muster; die fertigen Szenen schreiben et3_teil<N>.py
    pass
