"""Linux und Kommandozeile, Kapitel 10 „Shell-Skripte“ (Kap10_Skripte.tex, kap10_stufen.tex …): Abbildungen.

Gerüst; die Szenen baut der Abbildungs-Agent (Phase 2b) nach der Übergabe uebergabe_kap10.md.
Szenenname linux/k10<name> = \\label{fig:k10<name>} im Heft (\\szenenabb{k10<name>}{…}{fig:k10<name>}).

    python tools/szenen/linux_teil10.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

SZENEN = ()

if __name__ == "__main__":
    for f in SZENEN:
        f()
