"""Machine Learning Teil 1 (C:\\Bücher\\EtUndSo\\MachineLearning\\Arbeitshefte\\kap1_stufen.tex): Abbildungen.

Szenenname ml/k1<name> = \\label{fig:k1<name>} im Heft. Stil wie tools/szenen/et3_teil2.py (Achsen, Pfeile, Punkte).
Bauen:  python tools/szenen/ml_teil1.py
Export: python tools/export_szenen.py ml/k1<name> ...   (jedes Bild höchstens 548 px breit)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403


SZENEN = ()                # die Funktionen der Abbildungen, in der Reihenfolge des Hefts

for f in SZENEN:
    f()
