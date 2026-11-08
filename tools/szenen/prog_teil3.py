"""Programmieren, Python 3 (C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\kap3_stufen.tex): Abbildungen.

Szenenname prog/k3<name> = \\label{fig:k3<name>} im Heft. Stil wie tools/szenen/prog_teil2.py (Kästen, Pfeile, Code mit s.formel).
Bauen:  python tools/szenen/prog_teil3.py
Export: python tools/export_szenen.py prog/k3<name> ...   (jedes Bild höchstens 548 px breit)
Rechenbilder prog/k3r<name>: Summe, Produkt oder Skalarprodukt Schritt für Schritt (s.summe, s.produkt, s.skalarprodukt, s.formel).
Die Zahlen prüft C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\rechnung_kap3.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24


SZENEN = ()

for f in SZENEN:
    f()
