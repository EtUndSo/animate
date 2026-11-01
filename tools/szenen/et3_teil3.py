"""ET3 Teil 3 (kap3_stufen_a.tex, kap3_stufen_b.tex): acht Abbildungen zur Fourier-Transformation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")
BLAU60 = "#7faee6"         # elblue!60 im Heft
BEREICH = 24               # Beschriftung an den Kurven
PERIODE = "mod(x+pi/2,2*pi)"                                  # Phase der Rechteckschwingung (T = 2π s, Impuls um t = 0)
G0 = "1/(1+exp(pi))"                                          # 0,0414: unterer Umkehrpunkt des RC-Ausgangs


def wort_t(s):
    return s.tr("t", "t in s", "t in s", "t en s", "t / s")


def wort_f(s):
    return s.tr("f", "f in Hz", "f in Hz", "f en Hz", "f / Hz")


def k3koeff():
    """Fourier-Koeffizienten für T1 = T/2 und T/4 mit si-Hüllkurve."""
    s = Szene("et3/k3koeff")
    feld = (("T_1 = T/2", "k3_koeff_2.dat", "0.5*si(pi*x/2)", BLAU, -1.78),
            ("T_1 = T/4", "k3_koeff_4.dat", "0.25*si(pi*x/4)", ROT, 1.72))
    for titel, datei, huelle, farbe, mitte in feld:
        a = s.achsen((-12.5, 12.5), (-0.15, 0.55), breite=2.85, hoehe=1.95, mitte=(mitte, 0), titel=titel, titel_mitte=True, xl="k",
                     xticks="-10;-5;0;5;10", yticks="0;0.2;0.4", gitter=True)
        pts = daten(DAT / datei)
        s.stems(a, [p[0] for p in pts], [p[1] for p in pts], farbe=farbe, dicke=3, r=0.055)
        s.kurve(a, huelle, x=(-12.5, 12.5), farbe=GRAU, dicke=2, dash=DASH)
        if mitte < 0:
            s.text(a, "S_p(k)", (-12.5, 0.645), TEXT, "center")
    s.speichern()


def k3gibbs():
    """Teilsummen N = 3, 9, 27. Die Beschriftung steht im freien Feld des unteren Plateaus."""
    s = Szene("et3/k3gibbs")
    a = s.achsen((-6.3, 12.6), (-0.2, 1.2), breite=6.1, hoehe=2.5, mitte=(0.1, 0), xl=wort_t(s), xticks="-6;-4;-2;0;2;4;6;8;10;12", yticks="0;0.5;1", gitter=True)
    for n, farbe in ((3, ORANGE), (9, GRUEN), (27, BLAU)):
        s.daten(a, duenn(daten(DAT / f"k3_teilsumme_{n}.dat"), 5e-4), farbe=farbe, dicke=3)
    for y, name, farbe in ((0.74, "N = 3", ORANGE), (0.5, "N = 9", GRUEN), (0.26, "N = 27", BLAU)):
        s.text(a, name, (9.42, y), BEREICH, "center", farbe)
    s.speichern()


def k3rc():
    """Rechteckschwingung durch den RC-Tiefpass (RC = 1 s), beide Kurven in geschlossener Form."""
    s = Szene("et3/k3rc")
    a = s.achsen((-6.3, 12.6), (-0.1, 1.15), breite=6.1, hoehe=2.3, mitte=(0.1, 0), xl=wort_t(s), xticks="-6;-4;-2;0;2;4;6;8;10;12", yticks="0;0.5;1", gitter=True)
    s.kurve(a, f"where({PERIODE}<pi,1,0)", x=(-6.3, 12.6), farbe=GRAU, dicke=3)
    s.kurve(a, f"where({PERIODE}<pi,1-(1-{G0})*exp(-{PERIODE}),(1-{G0})*exp(pi-{PERIODE}))", x=(-6.3, 12.6), farbe=ROT, dicke=4)
    ein = s.tr("ein", "Eingang", "Input", "Entrada", "输入")
    aus = s.tr("aus", "Ausgang", "Output", "Salida", "输出")
    s.text(a, ein, (0, 1.08), BEREICH, "center", GRAU)
    s.text(a, aus, (8.25, 0.92), BEREICH, "left", ROT)
    s.speichern()


def k3grenz():
    """T·S_p(k) für T = 2 s und 4 s auf der Hüllkurve si(πf)."""
    s = Szene("et3/k3grenz")
    s.tr("oder", "bzw.", "or", "o", "或")
    a = s.achsen((-4.2, 4.2), (-0.3, 1.1), breite=6.0, hoehe=2.5, mitte=(0.1, 0), xl=wort_f(s), xticks="-4;-3;-2;-1;0;1;2;3;4", yticks="0;0.5;1", gitter=True,
                 titel="T·S_p(k) @{oder} S(f)")
    s.kurve(a, "si(pi*x)", farbe=GRAU, dicke=3, dash=DASH)
    s.stems(a, [-4 + 0.5 * k for k in range(17)], func="si(pi*x)", farbe=ROT, dicke=3, r=0.075)
    s.stems(a, [-4 + 0.25 * k for k in range(33)], func="si(pi*x)", farbe=BLAU, dicke=3, r=0.05)
    s.legende(a, [("S(f) = si(πf)", GRAU, "--"), ("T = 2 s", ROT, "o"), ("T = 4 s", BLAU, "o")], (2.0, 1.0))
    s.speichern()


def k3gerade():
    """Exponentialimpuls: gerader und ungerader Anteil, Re{H} und Im{H}."""
    s = Szene("et3/k3gerade")
    zeit = s.tr("zeit", "Zeitbereich", "Time domain", "Dominio del tiempo", "时域")
    freq = s.tr("freq", "Frequenzbereich", "Frequency domain", "Dominio de la frecuencia", "频域")
    gerade = s.tr("gerade", "gerade", "even", "par", "偶部")
    ungerade = s.tr("ungerade", "ungerade", "odd", "impar", "奇部")
    a = s.achsen((-3, 3), (-0.6, 1.1), breite=2.8, hoehe=2.1, mitte=(-1.76, 0), titel=zeit, titel_mitte=True, xl=wort_t(s), xticks="-2;0;2",
                 yticks="-0.5;0;0.5;1", gitter=True)
    s.kurve(a, "exp(-x)", x=(0, 3), farbe=GRAU, dicke=3)
    s.linie(a, (-3, 0), (0, 0), farbe=GRAU, dicke=3)
    s.kurve(a, "0.5*exp(-abs(x))", farbe=BLAU, dicke=3)
    s.kurve(a, "-0.5*exp(-abs(x))", x=(-3, -0.001), farbe=ROT, dicke=3)
    s.kurve(a, "0.5*exp(-abs(x))", x=(0.001, 3), farbe=ROT, dicke=3)
    s.text(a, "ε(t)e^{−t}", (0.32, 0.92), BEREICH, "left", GRAU)
    s.text(a, gerade, (-1.62, 0.34), BEREICH, "center", BLAU)
    s.text(a, ungerade, (-1.62, -0.38), BEREICH, "center", ROT)

    b = s.achsen((-1.5, 1.5), (-0.6, 1.1), breite=2.8, hoehe=2.1, mitte=(1.7, 0), titel=freq, titel_mitte=True, xl=wort_f(s), xticks="-1;0;1",
                 yticks="-0.5;0;0.5;1", gitter=True)
    s.kurve(b, "1/(1+(2*pi*x)^2)", farbe=BLAU, dicke=3)
    s.kurve(b, "-2*pi*x/(1+(2*pi*x)^2)", farbe=ROT, dicke=3)
    s.text(b, "Re\\{H\\}", (0.2, 0.85), BEREICH, "left", BLAU)
    s.text(b, "Im\\{H\\}", (-1.32, 0.44), BEREICH, "left", ROT)
    s.speichern()


def k3rectsi():
    """rect(t/T) für T = 1 s und 2 s und das si-Spektrum dazu."""
    s = Szene("et3/k3rectsi")
    zeit = s.tr("zeit", "Zeitbereich", "Time domain", "Dominio del tiempo", "时域")
    freq = s.tr("freq", "Frequenzbereich", "Frequency domain", "Dominio de la frecuencia", "频域")
    a = s.achsen((-1.6, 1.6), (-0.1, 1.3), breite=2.85, hoehe=2.1, mitte=(-1.78, 0), titel=zeit, titel_mitte=True, xl=wort_t(s), xticks="-1;0;1", yticks="0;0.5;1",
                 gitter=True)
    s.daten(a, [(-1.6, 0), (-0.5, 0), (-0.5, 1), (0.5, 1), (0.5, 0), (1.6, 0)], farbe=BLAU, dicke=3)
    s.daten(a, [(-1.6, 0), (-1, 0), (-1, 1), (1, 1), (1, 0), (1.6, 0)], farbe=ROT, dicke=3, dash=DASH)
    s.text(a, "T = 1 s", (0, 0.5), BEREICH, "center", BLAU)
    s.text(a, "T = 2 s", (0, 1.17), BEREICH, "center", ROT)

    b = s.achsen((-3, 3), (-0.5, 2.2), breite=2.85, hoehe=2.1, mitte=(1.72, 0), titel=freq, titel_mitte=True, xl=wort_f(s), xticks="-2;0;2", yticks="0;1;2",
                 gitter=True)
    s.kurve(b, "si(pi*x)", farbe=BLAU, dicke=3)
    s.kurve(b, "2*si(2*pi*x)", farbe=ROT, dicke=3, dash=DASH)
    s.text(b, "T = 1 s", (0.95, 0.75), BEREICH, "left", BLAU)
    s.text(b, "T = 2 s", (0.45, 1.8), BEREICH, "left", ROT)
    s.speichern()


def k3kamm():
    """Dirac-Kamm (T = 0,5 s) und sein Spektrum, gleiche y-Achse wie im Heft (Gewicht 1 und 2)."""
    s = Szene("et3/k3kamm")
    titel = s.tr("kamm", "Σ_n δ(t − nT), T = 0.5 s", "Σ_n δ(t − nT), T = 0.5 s", "Σ_n δ(t − nT), T = 0.5 s", "Σ_n δ(t − nT)，T = 0.5 s")
    a = s.achsen((-1.7, 1.9), (0, 2.6), breite=2.6, hoehe=1.75, mitte=(-1.95, 0), kreuz=True, titel=titel, titel_mitte=True, xl="t", xticks="-1;1", yticks="1;2", yzahlen=False)
    s.stems(a, [-1.5 + 0.5 * k for k in range(7)], [1] * 7, pfeile=True, farbe=BLAU, dicke=3)
    for y in (1, 2):                      # rechts der Achse: links stünde die Zahl im Pfeil bei -0,5
        s.text(a, str(y), (0.16, y), ZAHL)
    b = s.achsen((-7, 7.6), (0, 2.6), breite=2.85, hoehe=1.75, mitte=(1.55, 0), kreuz=True, titel="1/T Σ_k δ(f − k/T)", titel_mitte=True, xl="f",
                 xticks="-6;-4;-2;2;4;6", yticks="1;2", yzahlen=False)
    s.stems(b, [-6 + 2 * k for k in range(7)], [2] * 7, pfeile=True, farbe=ROT, dicke=3)
    for y in (1, 2):
        s.text(b, str(y), (0.58, y), ZAHL)
    s.speichern()


def k3hann():
    """Sieben Hann-Fenster (Breite 2 s, Versatz 1 s), ihre Summe ist 1."""
    s = Szene("et3/k3hann")
    tau = s.tr("tau", "τ in s", "τ in s", "τ en s", "τ / s")
    a = s.achsen((-1.5, 3.5), (0, 1.25), breite=6.1, hoehe=1.9, mitte=(0.1, 0), xl=tau, xticks=";".join("%g" % (-1.5 + 0.5 * k) for k in range(11)), yticks="0;0.5;1",
                 gitter=True)
    for n in range(-2, 5):
        s.kurve(a, f"cos(pi*(x-({n}))/2)^2", x=(n - 1, n + 1), farbe=BLAU60, dicke=3)
    s.linie(a, (-1.5, 1), (3.5, 1), farbe=ROT, dicke=5)
    summe = s.tr("summe", "Summe = 1", "Sum = 1", "Suma = 1", "总和 = 1")
    s.text(a, summe, (1, 1.12), BEREICH, "center", ROT)
    s.speichern()


for f in (k3koeff, k3gibbs, k3rc, k3grenz, k3gerade, k3rectsi, k3kamm, k3hann):
    f()
