"""ET3 Teil 8 (kap8_stufen.tex): Ersatzschaltbild eines Leitungsstücks.

Aufruf: python tools/szenen/et3_teil8.py, danach python tools/szenen_ansehen.py out.png et3/k8element [--lang de]
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403


def k8element():
    """Gleiche Reihenfolge wie im Heft (R, L, G, C), die Maße zusammengeschoben: Die Spalte erlaubt nur 7 Einheiten.
    Der Bruch ∂u/∂s ist aus zwei Texten und einem Strich gesetzt, einzeilig wäre die Beschriftung zu breit."""
    s = Szene("et3/k8element")
    yo, yu = 1.0, -1.0
    xa, xr, xl, xg, xc, xe = -2.62, -1.85, -0.8, 0.12, 0.98, 1.98
    s.draht((xa, yo), (xr - 0.48, yo))
    s.bauteil("resistor", (xr, yo), laenge=0.96, label="", size=0.8)
    s.text(None, "R′ds", (xr, yo), groesse=24, ausrichtung="center")
    s.draht((xr + 0.48, yo), (xl - 0.42, yo))
    s.bauteil("inductor", (xl, yo), laenge=0.84, label="L′ds", size=0.7, symbol_style="amerikanisch", font_size=24)
    s.draht((xl + 0.42, yo), (xe, yo))
    s.draht((xa, yu), (xe, yu))
    s.bauteil("resistor", (xg, 0), drehung=270, laenge=2.0, label="G′ds", label_flip=True, size=0.6, font_size=24)
    s.bauteil("capacitor", (xc, 0), drehung=270, laenge=2.0, label="C′ds", size=0.85, font_size=24)
    for x in (xg, xc):
        s.punkt(None, x, yo, r=0.055)
        s.punkt(None, x, yu, r=0.055)
    s.pfeil((xa - 0.2, 0.8), (xa - 0.2, -0.8), "u(s,t)", farbe=BLAU, label_seite="right", groesse=24, spitze=0.2)
    s.pfeil((xe + 0.2, 0.8), (xe + 0.2, -0.8), "", farbe=ROT, spitze=0.2)
    x = xe + 0.36
    s.text(None, "u +", (x, 0), groesse=24, farbe=ROT)
    xb = x + 0.5
    s.text(None, "∂u", (xb, 0.19), groesse=22, farbe=ROT, ausrichtung="center")
    s.linie(None, (xb - 0.18, 0), (xb + 0.18, 0), farbe=ROT, dicke=2.5)
    s.text(None, "∂s", (xb, -0.21), groesse=22, farbe=ROT, ausrichtung="center")
    s.text(None, "ds", (xb + 0.25, 0), groesse=24, farbe=ROT)
    s.pfeil((xa, yo + 0.28), (xa + 0.45, yo + 0.28), "", spitze=0.2)
    s.text(None, "i(s,t)", (xa + 0.2, yo + 0.6), groesse=24, ausrichtung="center")
    s.speichern()


k8element()
