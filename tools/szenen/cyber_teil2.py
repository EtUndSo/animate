"""Cybersecurity, Kapitel 2 „Schutzgrenzen in Hardware und Betriebssystem“ (Kap2_Schutzgrenzen.tex, kap2_stufen.tex …): Abbildungen.

Gerüst; die Szenen baut der Abbildungs-Agent (Phase 2b) nach der Übergabe uebergabe_kap2.md.
Szenenname cyber/k2<name> = \\label{fig:k2<name>} im Heft (\\szenenabb{k2<name>}{…}{fig:k2<name>}).

    python tools/szenen/cyber_teil2.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

SZENEN = ()

if __name__ == "__main__":
    for f in SZENEN:
        f()
