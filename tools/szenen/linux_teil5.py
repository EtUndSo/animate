"""Linux und Kommandozeile, Kapitel 5 „Expansion, Quoting, Variablen und Umgebung“ (Kap5_Expansion.tex, kap5_stufen.tex …): Abbildungen.

Gerüst; die Szenen baut der Abbildungs-Agent (Phase 2b) nach der Übergabe uebergabe_kap5.md.
Szenenname linux/k5<name> = \\label{fig:k5<name>} im Heft (\\szenenabb{k5<name>}{…}{fig:k5<name>}).

    python tools/szenen/linux_teil5.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

SZENEN = ()

if __name__ == "__main__":
    for f in SZENEN:
        f()
