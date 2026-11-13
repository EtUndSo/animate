"""Cybersecurity, Kapitel 4 „Netzwerke I: vom Signal zum Paket“ (Kap4_Netzwerke.tex, kap4_stufen.tex …): Abbildungen.

Gerüst; die Szenen baut der Abbildungs-Agent (Phase 2b) nach der Übergabe uebergabe_kap4.md.
Szenenname cyber/k4<name> = \\label{fig:k4<name>} im Heft (\\szenenabb{k4<name>}{…}{fig:k4<name>}).

    python tools/szenen/cyber_teil4.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

SZENEN = ()

if __name__ == "__main__":
    for f in SZENEN:
        f()
