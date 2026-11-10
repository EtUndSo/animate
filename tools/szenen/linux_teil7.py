"""Linux und Kommandozeile, Kapitel 7 „Benutzer, Gruppen und Rechte“ (Kap7_Rechte.tex, kap7_stufen.tex …): Abbildungen.

Gerüst; die Szenen baut der Abbildungs-Agent (Phase 2b) nach der Übergabe uebergabe_kap7.md.
Szenenname linux/k7<name> = \\label{fig:k7<name>} im Heft (\\szenenabb{k7<name>}{…}{fig:k7<name>}).

    python tools/szenen/linux_teil7.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

SZENEN = ()

if __name__ == "__main__":
    for f in SZENEN:
        f()
