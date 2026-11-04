"""Beispiel: Summe, Produkt und Skalarprodukt als Abbildung (szenen_lib: summe, produkt, skalarprodukt; dazu formel).

Bauen:  python tools/szenen/beispiel_summen.py
Export: python tools/export_szenen.py beispiel/summe beispiel/produkt beispiel/skalarprodukt beispiel/skalarprodukt_lang beispiel/formel
Ansehen: python tools/szenen_ansehen.py blatt.png beispiel/summe beispiel/produkt beispiel/skalarprodukt beispiel/skalarprodukt_lang beispiel/formel

Im Artikel steht jede Rechnung vollständig da (Kopf = eingesetzt = Werte = Ergebnis, "=" unter "="); im Editor
(Szene öffnen, ▶) läuft dieselbe Rechnung Schritt für Schritt ab.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403


def summe():
    s = Szene("beispiel/summe")
    s.summe("1/i^2", von=1, bis=4)                       # Brüche exakt, die Summe zusätzlich als Dezimalzahl
    s.speichern()


def produkt():
    s = Szene("beispiel/produkt")
    s.produkt("1 + 1/i", von=1, bis=4)                   # 2 · 3/2 · 4/3 · 5/4 = 5 (Teleskopprodukt)
    s.speichern()


def skalarprodukt():
    s = Szene("beispiel/skalarprodukt")
    s.skalarprodukt([3, 10, -4], [120, 3, 25], namen=("w", "x"), index="j")
    s.speichern()


def skalarprodukt_lang():
    s = Szene("beispiel/skalarprodukt_lang")              # sieben Komponenten: ⋮ in den Vektoren, ⋯ in der Rechnung
    s.skalarprodukt([0.5, 1.25, -2, 3, 4, 5, 6], [0.4, 2, 3, 1, 1, 1, 2], namen=("theta", "x"), index="k", obere="d")
    s.speichern()


def formel():
    s = Szene("beispiel/formel")                          # MathTex: eine beliebige Formel, ebenfalls von MathJax gesetzt
    s.formel(r"\hat y = \sigma\!\left(\mathbf w^\top \mathbf x + b\right), \quad \sigma(z) = \frac{1}{1 + e^{-z}}", hoehe=0.42)
    s.speichern()


if __name__ == "__main__":
    for f in (summe, produkt, skalarprodukt, skalarprodukt_lang, formel):
        f()
        print("✓", f.__name__)
