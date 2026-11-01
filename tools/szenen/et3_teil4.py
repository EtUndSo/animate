"""ET3 Teil 4 (Abtastung, zeitdiskrete Signale): die acht Abbildungen aus kap4_stufen_a/b.tex."""
import sys
from math import cos, pi
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

DAT = Path(r"C:\Bücher\ET3\Arbeitshefte\daten")
T_GRAU = "#a6a6a6"          # black!35 der Hefte, dünne Nebenkurven


def achsen_pfeile(s):
    """Wie axis lines=left im Heft: Pfeilspitzen an den Achsen des zuletzt angelegten Teilbilds."""
    s.objects[-1]["props"].update(arrows=True, arrow_size=0.16)


def summe(ks, b):
    """Summe von Dreiecken der Halbbreite b an den Stellen ks (Heft: tri(x-k) bzw. tr(x-k, b))."""
    return "+".join("tri((x-(%g))/%g)" % (k, b) for k in ks)


def k4spektrum():
    """Abgetastetes Spektrum: f_A = 1 kHz (Kopien getrennt), f_A = 0,5 kHz (Aliasing)."""
    s = Szene("et3/k4spektrum")
    xl = s.tr("f", "f in kHz", "f in kHz", "f en kHz", "f / kHz")
    ticks = "-2;-1.5;-1;-0.5;0;0.5;1;1.5;2"
    a = s.achsen((-2.2, 2.2), (0, 1.35), breite=6.4, hoehe=1.5, mitte=(0, 1.75), xl=xl, xticks=ticks, ymarks=False, yzahlen=False, titel_mitte=True,
                 titel=s.tr("t1", "f_{A} = 1 kHz: Kopien getrennt", "f_{A} = 1 kHz: copies separate", "f_{A} = 1 kHz: copias separadas", "f_{A} = 1 kHz：副本相互分开"))
    achsen_pfeile(s)
    s.flaeche(a, "tri(x/0.3)", -0.3, 0.3, farbe=BLAU, deckung=0.15)
    s.kurve(a, "tri(x/0.3)", x=(-0.3, 0.3), farbe=BLAU, dicke=4)
    s.kurve(a, summe((2, 1, -1, -2), 0.3), farbe=GRAU, dicke=4)
    for x in (-0.5, 0.5):
        s.linie(a, (x, 0), (x, 1.3), farbe=ROT, dicke=2, dash=DASH)
    s.text(a, "f_{A}/2", (0.56, 1.17), farbe=ROT, groesse=24)
    b = s.achsen((-2.2, 2.2), (0, 1.35), breite=6.4, hoehe=1.5, mitte=(0, -1.55), xl=xl, xticks=ticks, ymarks=False, yzahlen=False, titel_mitte=True,
                 titel=s.tr("t2", "f_{A} = 0.5 kHz: Kopien überlappen (Aliasing)", "f_{A} = 0.5 kHz: copies overlap (aliasing)",
                            "f_{A} = 0.5 kHz: las copias se solapan (aliasing)", "f_{A} = 0.5 kHz：副本相互重叠（混叠）"))
    achsen_pfeile(s)
    s.kurve(b, summe((2, 1.5, 1, 0.5, -0.5, -1, -1.5, -2), 0.3), farbe=HELLGRAU, dicke=2)
    s.kurve(b, "tri(x/0.3)", x=(-0.3, 0.3), farbe=BLAU, dicke=4)
    s.kurve(b, summe((2, 1.5, 1, 0.5, 0, -0.5, -1, -1.5, -2), 0.3), farbe=ROT, dicke=4)
    s.speichern()


def k4siinterp():
    """si-Interpolation: gewichtete si-Funktionen, ihre Summe, Abtastwerte."""
    s = Szene("et3/k4siinterp")
    werte = [0, 1, 0.6, -0.4, 0.8, 0]
    a = s.achsen((-1.5, 6.5, 1), (-0.6, 1.25), breite=6.3, hoehe=3.0, mitte=(0.2, 0), xl="t/T", yticks="-0.5;0;0.5;1", gitter=True, rahmen=True)
    for n in (1, 2, 3, 4):
        s.kurve(a, "%g*si(pi*(x-%d))" % (werte[n], n), farbe=T_GRAU, dicke=2)
    s.kurve(a, "+".join("(%g)*si(pi*(x-%d))" % (w, n) for n, w in enumerate(werte) if w), farbe=BLAU, dicke=5)
    for n, w in enumerate(werte):
        s.punkt(a, n, w, farbe=ROT, r=0.07)
    s.speichern()


def k4alias():
    """700 Hz und 300 Hz mit denselben Abtastwerten bei f_A = 1 kHz."""
    s = Szene("et3/k4alias")
    a = s.achsen((0, 7, 1), (-1.2, 1.2), breite=6.35, hoehe=2.3, mitte=(0.15, 0), yticks="-1;0;1", gitter=True, rahmen=True,
                 xl=s.tr("t", "t in ms", "t in ms", "t en ms", "t / ms"))
    s.kurve(a, "cos(2*pi*0.7*x)", farbe=BLAU, dicke=4)
    s.kurve(a, "cos(2*pi*0.3*x)", farbe=ROT, dicke=4, dash=DASH)
    for n in range(8):
        s.punkt(a, n, cos(2 * pi * 0.3 * n), farbe=SCHWARZ, r=0.07)
    s.legende(a, [("700 Hz", BLAU, "-")], (1.95, 1.5))
    s.legende(a, [("300 Hz", ROT, "--")], (3.75, 1.5))
    s.speichern()


def k4block():
    """System erster Ordnung: Verzögerer T, zwei Summierstellen, a0, a1, b1."""
    s = Szene("et3/k4block")
    xw = lambda cm: (cm - 4.1) * 0.8        # Heftkoordinaten (cm) auf Szeneneinheiten
    y_t = -0.85                             # Höhe der T-Kästen
    b_t, h_t, r = 0.6, 0.5, 0.21            # Kastenmaße, Radius der Summierstelle
    xa, xd1, xp1, xp2, xb = xw(1), xw(2.2), xw(3.6), xw(5.4), xw(6.6)
    xs, xg = xw(0), xw(8.2)
    s.text(None, "s(n)", (xs + 0.28, 0), ausrichtung="right")
    s.text(None, "g(n)", (xg - 0.28, 0))
    s.box("T", (xd1, y_t), breite=b_t, hoehe=h_t)
    s.box("T", (xb, y_t), breite=b_t, hoehe=h_t)
    s.box("+", (xp1, 0), breite=2 * r / 1.3, hoehe=2 * r / 1.4, form="ellipse")
    s.box("+", (xp2, 0), breite=2 * r / 1.3, hoehe=2 * r / 1.4, form="ellipse")
    s.draht((xs + 0.36, 0), (xa, 0))
    s.pfeil((xa, 0), (xp1 - r, 0), "a_0", spitze=0.18)
    s.draht((xa, 0), (xa, y_t), (xd1 - b_t / 2, y_t))
    s.pfeil((xd1 + b_t / 2, y_t), (xp1, -r), "a_1", knick="hv", label_seite="right", spitze=0.18)
    s.pfeil((xp1 + r, 0), (xp2 - r, 0), spitze=0.18)
    s.draht((xp2 + r, 0), (xb, 0))
    s.pfeil((xb, 0), (xg - 0.36, 0), spitze=0.18)
    s.pfeil((xb, 0), (xb, y_t + h_t / 2), spitze=0.18)
    s.pfeil((xb - b_t / 2, y_t), (xp2, -r), "b_1", knick="hv", spitze=0.18)
    s.punkt(None, xa, 0, r=0.05)
    s.punkt(None, xb, 0, r=0.05)
    s.text(None, s.tr("fir", "FIR-Teil", "FIR part", "parte FIR", "FIR 部分"), (xw(2.3), 0.62), farbe=GRAU, ausrichtung="center", groesse=24)
    s.text(None, s.tr("iir", "IIR-Teil", "IIR part", "parte IIR", "IIR 部分"), (xw(6.0), 0.62), farbe=GRAU, ausrichtung="center", groesse=24)
    s.speichern()


def k4rek():
    """Rekursives System b = 0,6: Impulsantwort; Rechteck M = 4 (grau) und Antwort."""
    s = Szene("et3/k4rek")
    n = [p[0] for p in daten(DAT / "k4_rekursion.dat", 1, 2)]
    sf = [p[1] for p in daten(DAT / "k4_rekursion.dat", 1, 2)]
    h = [p[1] for p in daten(DAT / "k4_rekursion.dat", 1, 3)]
    g = [p[1] for p in daten(DAT / "k4_rekursion.dat", 1, 4)]
    a = s.achsen((-2.5, 13.5), (0, 1.15), breite=2.75, hoehe=2.2, mitte=(-1.82, 0), xl="n", xticks="0;5;10", yticks="0;0.5;1", gitter=True, rahmen=True, titel_mitte=True,
                 titel=s.tr("t1", "Impulsantwort\\\\h(n) = 0.6^n ε(n)", "Impulse response\\\\h(n) = 0.6^n ε(n)", "Respuesta al impulso\\\\h(n) = 0.6^n ε(n)", "单位脉冲响应\\\\h(n) = 0.6^n ε(n)"))
    s.stems(a, n, h, farbe=BLAU, dicke=3, r=0.05)
    b = s.achsen((-2.5, 13.5), (0, 2.4), breite=2.75, hoehe=2.2, mitte=(1.82, 0), xl="n", xticks="0;5;10", yticks="0;1;2", gitter=True, rahmen=True, titel_mitte=True,
                 titel=s.tr("t2", "Rechteck mit M = 4 (grau)\\\\und Antwort", "Rectangle with M = 4 (gray)\\\\and response", "Rectángulo con M = 4 (gris)\\\\y respuesta", "M = 4 的矩形（灰色）\\\\及其响应"))
    s.stems(b, n, sf, farbe=HELLGRAU, dicke=3, marker="square", r=0.06)
    s.stems(b, n, g, farbe=ROT, dicke=3, r=0.05)
    s.speichern()


def k4dtft():
    """|H_a(f)| des rekursiven Systems, periodisch; Grenzen bei ±f_A/2."""
    s = Szene("et3/k4dtft")
    a = s.achsen((-1.1, 1.1), (0, 2.8), breite=6.4, hoehe=2.5, mitte=(0.2, 0), xticks="-1;-0.5;0;0.5;1", yticks="0;1;2", yl="|H_{a}(f)|", gitter=True, rahmen=True,
                 xl=s.tr("f", "f (bezogen auf die Abtastrate)", "f (normalized to the sampling rate)", "f (normalizada a la frecuencia de muestreo)", "f（对采样率归一化）"))
    s.kurve(a, "1/sqrt(1+0.36-1.2*cos(2*pi*x))", farbe=BLAU, dicke=4)
    for x in (-0.5, 0.5):
        s.linie(a, (x, 0), (x, 2.8), farbe=ROT, dicke=2, dash=DASH)
    s.text(a, "f_{A}/2", (0.53, 2.45), farbe=ROT, groesse=24)
    s.speichern()


def k4rate():
    """Spektren beim Ändern der Abtastrate: Original, herabgetastet, hochgetastet."""
    s = Szene("et3/k4rate")
    ticks = "-1;-0.5;0;0.5;1"
    feld = [(s.tr("t1", "Original, f_{g} = 0.2", "Original, f_{g} = 0.2", "Original, f_{g} = 0.2", "原序列，f_{g} = 0.2"),
             "+".join("tri((x-(%d))/0.2)" % k for k in (0, 1, -1)), BLAU),
            (s.tr("t2", "herabgetastet mit c = 2: Band bis 0.4, keine Überlappung (Höhe halbiert)",
                  "downsampled with c = 2: band up to 0.4, no overlap (height halved)",
                  "submuestreado con c = 2: banda hasta 0.4,\\\\sin solapamiento (altura reducida a la mitad)",
                  "以 c = 2 降采样：频带延伸到 0.4，无重叠（高度减半）"),
             "0.5*(%s)" % "+".join("tri((x-(%d))/0.4)" % k for k in (0, 1, -1)), ROT),
            (s.tr("t3", "hochgetastet mit c = 2: Band bis 0.1, Spiegelspektrum bei ±0.5",
                  "upsampled with c = 2: band up to 0.1, spectral image at ±0.5",
                  "sobremuestreado con c = 2: banda hasta 0.1, réplica espectral en ±0.5",
                  "以 c = 2 升采样：频带延伸到 0.1，±0.5 处出现频谱镜像"),
             "+".join("tri((x-(%g))/0.1)" % k for k in (0, 0.5, -0.5, 1, -1)), GRUEN)]
    for k, (titel, f, farbe) in enumerate(feld):
        a = s.achsen((-1.2, 1.2), (0, 1.3), breite=6.4, hoehe=1.05, mitte=(0, 2.45 - 2.45 * k), xticks=ticks, ymarks=False, yzahlen=False, titel=titel, titel_mitte=True, label=24)
        achsen_pfeile(s)
        s.kurve(a, f, farbe=farbe, dicke=4)
    s.speichern()


def k4zebene():
    """z-Ebene: Pole, Nullstellen, Einheitskreis, Konvergenzbereich |z| > 0,5."""
    s = Szene("et3/k4zebene")
    k = 1.6                                 # Maßstab Szeneneinheiten je Dateneinheit (beide Achsen gleich, sonst keine Kreise)
    a = s.achsen((-1.5, 1.55), (-1.3, 1.35), breite=3.05 * k, hoehe=2.65 * k, unsichtbar=True, xzahlen=False, yzahlen=False, xmarks=False, ymarks=False)
    s.band(a, -1.45, 1.45, -1.25, 1.25, farbe=BLAU, deckung=0.12)
    s.kreis(a, 0, 0, 0.5, farbe=GRAU, dicke=2, fuellung="#ffffff", deckung=1)
    s.pfeil((-1.5, 0), (1.55, 0), farbe=GRAU, dicke=2, spitze=0.18, on=a)
    s.pfeil((0, -1.3), (0, 1.35), farbe=GRAU, dicke=2, spitze=0.18, on=a)
    s.text(a, "Re z", (1.53, -0.1), farbe=GRAU, ausrichtung="right", groesse=24)
    s.text(a, "Im z", (-0.05, 1.3), farbe=GRAU, ausrichtung="right", groesse=24)
    s.kreis(a, 0, 0, 1, farbe=SCHWARZ, dicke=4)
    s.text(a, s.tr("ek", "Einheitskreis", "Unit circle", "circunferencia\\\\unidad", "单位圆"), (0.71, 0.9), groesse=24)
    s.linie(a, (0, 0), (0.25, 0.433), farbe=GRAU, dicke=2, dash=DASH)
    for y in (0.433, -0.433):
        s.kreuzchen(a, 0.25, y, farbe=ROT, groesse=0.22, dicke=4)
    s.kreis(a, 0, 0, 0.045, farbe=BLAU, dicke=3)
    s.kreis(a, 0.25, 0, 0.045, farbe=BLAU, dicke=3)
    s.text(a, "0.5 e^{jπ/3}", (0.22, 0.58), groesse=24)
    s.text(a, s.tr("kb", "Konvergenz-\\\\bereich\\\\|z| > 0.5", "Region\\\\of convergence\\\\|z| > 0.5", "Región de\\\\convergencia\\\\|z| > 0.5", "收敛域\\\\|z| > 0.5"),
           (-1.05, -1.0), farbe=BLAU, ausrichtung="center", groesse=24)
    s.speichern()


for f in (k4spektrum, k4siinterp, k4alias, k4block, k4rek, k4dtft, k4rate, k4zebene):
    f()
