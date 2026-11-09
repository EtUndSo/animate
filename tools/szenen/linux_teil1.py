"""Linux und Kommandozeile, Linux 1 (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\kap1_stufen.tex): Abbildungen.

Szenenname linux/k1<name> = \\label{fig:k1<name>} im Heft. Stil wie tools/szenen/prog_teil2.py (Kästen, Pfeile, Code mit s.formel).
Bauen:  python tools/szenen/linux_teil1.py
Export: python tools/export_szenen.py linux/k1<name> ...   (jedes Bild höchstens 548 px breit)
Rechenbilder linux/k1r<name>: Summe, Produkt oder Skalarprodukt Schritt für Schritt (s.summe, s.produkt, s.skalarprodukt, s.formel).
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
