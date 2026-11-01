"""ET3 Teil 6 (Korrelation): die zwei Abbildungen aus kap6_stufen.tex."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

B, M = 2.75, 1.82           # Breite der Teilbilder, Abstand ihrer Mitten von der Bildmitte


def k6korr():
    """AKF des Rechtecks; KKF mit einem Echo."""
    s = Szene("et3/k6korr")
    xl = s.tr("x", "t bzw. τ", "t or τ", "t o τ", "t 或 τ")
    a = s.achsen((-1.6, 1.6), (-0.05, 1.2), breite=B, hoehe=2.2, mitte=(-M, 0), xl=xl, xticks="-1;0;1", yticks="0;0.5;1", gitter=True, rahmen=True, titel_mitte=True,
                 titel=s.tr("t1", "AKF des Rechtecks", "ACF of the rectangle", "FAC del rectángulo", "矩形的自相关函数"))
    s.kurve(a, "rect(x)", farbe=GRAU, dicke=4)
    s.kurve(a, "tri(x)", farbe=BLAU, dicke=4)
    s.text(a, "rect(t)", (-0.6, 1.08), farbe=GRAU, ausrichtung="right", groesse=24)
    s.text(a, r"\varphi^E_{ss}(\tau)\\= \Lambda(\tau)", (0.6, 0.76), farbe=BLAU, groesse=24)
    b = s.achsen((-1.5, 4.5), (-0.05, 1.2), breite=B, hoehe=2.2, mitte=(M, 0), xl=xl, xticks="0;2;4", yticks="0;0.5;1", gitter=True, rahmen=True, titel_mitte=True,
                 titel=s.tr("t2", "KKF mit einem Echo", "CCF with an echo", "FCC con un eco", "与回波的互相关函数"))
    s.kurve(b, "rect(x)", farbe=GRAU, dicke=4)
    s.kurve(b, "0.5*rect(x-3)", farbe=ORANGE, dicke=4)
    s.kurve(b, "0.5*tri(x-3)", farbe=ROT, dicke=4)
    s.text(b, s.tr("ge", "gesendet", "sent", "emitido", "发送"), (0.65, 0.85), farbe=GRAU, groesse=24)
    s.text(b, s.tr("ec", "Echo", "echo", "eco", "回波"), (3.0, 0.68), farbe=ORANGE, ausrichtung="center", groesse=24)
    s.text(b, r"\varphi^E_{sg}(\tau)", (2.15, 0.28), farbe=ROT, ausrichtung="right", groesse=24)
    s.speichern()


def k6exp():
    """Exponentialimpuls und seine AKF; |S| und |S|^2."""
    s = Szene("et3/k6exp")
    a = s.achsen((-3, 3), (0, 1.1), breite=B, hoehe=2.2, mitte=(-M, 0), xticks="-2;0;2", yticks="0;0.5;1", gitter=True, rahmen=True, titel_mitte=True,
                 xl=s.tr("x1", "t bzw. τ in s", "t or τ in s", "t o τ en s", "t 或 τ / s"),
                 titel=s.tr("t1", "Zeitbereich", "Time domain", "Dominio del tiempo", "时域"))
    s.kurve(a, "exp(-x)", x=(0, 3), farbe=GRAU, dicke=4)
    s.kurve(a, "0", x=(-3, 0), farbe=GRAU, dicke=4)
    s.kurve(a, "0.5*exp(-abs(x))", farbe=BLAU, dicke=4)
    s.text(a, "s(t)", (0.75, 0.72), farbe=GRAU, groesse=24)
    s.text(a, r"\varphi^E_{ss}(\tau)", (-0.35, 0.5), farbe=BLAU, ausrichtung="right", groesse=24)
    b = s.achsen((-1, 1), (0, 1.1), breite=B, hoehe=2.2, mitte=(M, 0), xticks="-1;-0.5;0;0.5;1", yticks="0;0.5;1", gitter=True, rahmen=True, titel_mitte=True,
                 xl=s.tr("x2", "f in Hz", "f in Hz", "f en Hz", "f / Hz"),
                 titel=s.tr("t2", "Frequenzbereich", "Frequency domain", "Dominio de la frecuencia", "频域"))
    s.kurve(b, "1/sqrt(1+(2*pi*x)^2)", farbe=GRAU, dicke=4)
    s.kurve(b, "1/(1+(2*pi*x)^2)", farbe=ROT, dicke=4)
    s.legende(b, [("|S(f)|", GRAU, "-"), ("|S(f)|^2", ROT, "-")], (0.2, 0.97))
    s.speichern()


for f in (k6korr, k6exp):
    f()
