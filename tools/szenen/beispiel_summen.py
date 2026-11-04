"""Beispiel: Summe, Produkt und Skalarprodukt als Abbildung (szenen_lib: summe, produkt, skalarprodukt; dazu formel).

Bauen:  python tools/szenen/beispiel_summen.py
Export: python tools/export_szenen.py beispiel/summe beispiel/produkt beispiel/skalarprodukt beispiel/skalarprodukt_lang \
            beispiel/skalarprodukt_komponenten beispiel/skalarprodukt_matrix beispiel/skalarprodukt_index beispiel/formel
Ansehen: python tools/szenen_ansehen.py blatt.png beispiel/skalarprodukt beispiel/skalarprodukt_komponenten …

Im Artikel steht jede Rechnung vollständig da (Kopf = eingesetzt = Werte = Ergebnis, "=" unter "="); im Editor
(Szene öffnen, ▶) läuft dieselbe Rechnung Schritt für Schritt ab. Das Skalarprodukt gibt es in drei Darstellungen:
"rechnung" (wie Σ), "komponenten" und "matrix"; das Bild zeigt jeweils den Endzustand.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

W, X = [3, 10, -4], [120, 3, 25]


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
    s.skalarprodukt(W, X, namen=("w", "x"), index="j")
    s.speichern()


def skalarprodukt_lang():
    s = Szene("beispiel/skalarprodukt_lang")              # sieben Komponenten: ⋮ in den Vektoren, ⋯ in der Rechnung
    s.skalarprodukt([0.5, 1.25, -2, 3, 4, 5, 6], [0.4, 2, 3, 1, 1, 1, 2], namen=("theta", "x"), index="k", obere="d")
    s.speichern()


def skalarprodukt_komponenten():
    s = Szene("beispiel/skalarprodukt_komponenten")       # je Zeile: Paar markiert, · dazwischen, = Produkt; dann die Summe
    s.skalarprodukt(W, X, namen=("w", "x"), darstellung="komponenten")
    s.speichern()


def skalarprodukt_matrix():
    s = Szene("beispiel/skalarprodukt_matrix")            # w dreht sich zum Zeilenvektor, x wird daraufgelegt
    s.skalarprodukt(W, X, namen=("w", "x"), darstellung="matrix")
    s.speichern()


def skalarprodukt_index():
    s = Szene("beispiel/skalarprodukt_index")             # indizierter Vektor: Kopf q₁ᵀx, Komponenten q_{1,j}
    s.skalarprodukt([0.2, -1.5, 3], [4, 2, 0.5], namen=("q_1", "x"), index="j")
    s.speichern()


def formel():
    s = Szene("beispiel/formel")                          # MathTex: eine beliebige Formel, Dezimalzahlen je Sprache
    s.formel(r"\hat y = \sigma\!\left(\mathbf w^\top \mathbf x + b\right), \quad \sigma(0.5) \approx 0.622", hoehe=0.3)
    s.speichern()


if __name__ == "__main__":
    for f in (summe, produkt, skalarprodukt, skalarprodukt_lang, skalarprodukt_komponenten, skalarprodukt_matrix,
              skalarprodukt_index, formel):
        f()
        print("✓", f.__name__)
