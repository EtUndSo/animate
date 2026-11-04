"""Machine Learning Teil 2 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap2_stufen.tex): Abbildungen.

Szenenname ml/k2<name> = \\label{fig:k2<name>} im Heft. Stil wie tools/szenen/ml_teil1.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil2.py
Export: python tools/export_szenen.py ml/k2<name> ...   (jedes Bild höchstens 548 px breit)
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


SZENEN = ()

for f in SZENEN:
    f()
