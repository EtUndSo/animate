"""Linux und Kommandozeile, Kapitel 9 „Software installieren: Paketverwaltung“ (Kap9_Pakete.tex, kap9_stufen.tex …): Abbildungen.

Gerüst; die Szenen baut der Abbildungs-Agent (Phase 2b) nach der Übergabe uebergabe_kap9.md.
Szenenname linux/k9<name> = \\label{fig:k9<name>} im Heft (\\szenenabb{k9<name>}{…}{fig:k9<name>}).

    python tools/szenen/linux_teil9.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

SZENEN = ()

if __name__ == "__main__":
    for f in SZENEN:
        f()
