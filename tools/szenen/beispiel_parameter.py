"""Beispiele für Parameter über die Zeit (L3, Anleitung: notizen/animationen.md §8).

Bauen:  python tools/szenen/beispiel_parameter.py
Export: python tools/export_szenen.py --animiert beispiel/anim_l3_welle beispiel/anim_l3_tangente \
            beispiel/anim_l3_zeitmarker beispiel/anim_l3_zeiger beispiel/anim_l3_grenzwert beispiel/anim_l3_flaeche

Ein Parameter (s.parameter) ist eine Zahl der Szene mit Namen; s.verstellen ändert ihn über die Zeit. Jedes Objekt,
dessen Ausdrücke ihn nennen (Kurve, Punkt, Strecke, Pfeil, Kreis, Fläche, Zahlenanzeige), wird in jedem Bild neu
berechnet. Das statische Bild und das PDF zeigen das Endbild (alle Parameter auf ihrem letzten Zielwert).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403


def welle():
    """Laufende Welle y = sin(k(x - c t)) mit c = 1: der Wellenberg wandert in 6 s um 6 Einheiten, der Punkt bei
    x = 2 schwingt nur auf und ab."""
    s = Szene("beispiel/anim_l3_welle", reihenfolge="anlegen")
    a = s.achsen((0, 12, 2), (-1.5, 1.5, 1), breite=6.4, hoehe=2.4, mitte=(0, -0.2), xl="x", yl="y")
    s.parameter("t", 0)
    f = "sin(pi/2*(x - t))"
    k = s.kurve(a, f, punkte=49)
    berg = s.punkt(a, "1 + t", 1, farbe=ROT, r=0.09)
    weg = s.linie(a, (1, 1.25), ("1 + t", 1.25), farbe=ROT, dicke=3)
    p = s.marke(a, 2, f=f, hilfslinien=False, farbe=GRUEN, r=0.09)
    z = s.zahl(a, "t", (8.6, 1.3), stellen=2, vor="t = ", nach=" s")
    s.einblenden(a, dauer=0.6)
    s.zeichnen(k, dauer=1.2)
    s.einblenden(berg, weg, p, z, dauer=0.5)             # weg hat bei t = 0 die Länge 0 und wächst mit t
    s.verstellen("t", 6, dauer=6, rate="linear")
    s.speichern()


def tangente():
    """Punkt läuft auf der Kurve, mit mitlaufender Tangente, Projektionen auf beide Achsen und Zahlenanzeige."""
    s = Szene("beispiel/anim_l3_tangente", reihenfolge="anlegen")
    s.welt()                                # on=None = Szeneneinheiten (Zahlen rechts neben dem Bild)
    a = s.achsen((-2, 2, 1), (-2, 2, 1), breite=4.4, hoehe=3.0, mitte=(-1.7, 0), kreuz=True, xl="x", yl="y")
    s.parameter("a", -1.6)
    f = "0.5*x^3 - 1.5*x"
    k = s.kurve(a, f)
    tg = s.tangente(a, f, "a", laenge=0.8, punkt=False, farbe=ORANGE, dicke=4)
    p = s.marke(a, "a", f=f, label="P", farbe=ROT, r=0.09)
    z1 = s.zahl(None, "a", (1.3, 1.3), stellen=2, vor="a = ")
    z2 = s.zahl(None, "1.5*a^2 - 1.5", (1.3, 0.7), stellen=2, vor="f′(a) = ", farbe=ORANGE)
    s.einblenden(a, dauer=0.6)
    s.zeichnen(k, dauer=1.0)
    s.einblenden(p, tg, z1, z2, dauer=0.5)
    s.verstellen("a", 1.6, dauer=5)
    s.pause(0.5)
    s.speichern()


def zeitmarker():
    """Ein Zeitmarker (senkrechte Linie bei t) liest Spannung und Strom gleichzeitig ab."""
    s = Szene("beispiel/anim_l3_zeitmarker", reihenfolge="anlegen")
    s.welt()                                # on=None = Szeneneinheiten (Zahlen rechts neben dem Bild)
    a = s.achsen((0, 2, 0.5), (-1.2, 1.2, 0.5), breite=5.0, hoehe=2.6, mitte=(-0.9, 0), xl="t in ms", gitter=True)
    s.parameter("T", 0.1)
    u = "sin(2*pi*x)"
    i = "0.6*sin(2*pi*x - pi/3)"
    ku = s.kurve(a, u, farbe=BLAU)
    ki = s.kurve(a, i, farbe=ROT)
    lin = s.linie(a, ("T", -1.2), ("T", 1.2), farbe=GRAU, dicke=3, dash=DASH)
    mu = s.marke(a, "T", f=u, hilfslinien=False, farbe=BLAU, r=0.08)
    mi = s.marke(a, "T", f=i, hilfslinien=False, farbe=ROT, r=0.08)
    zt = s.zahl(None, "T", (2.0, 0.9), stellen=2, vor="t = ", nach=" ms")
    zu = s.zahl(None, "sin(2*pi*T)", (2.0, 0.3), stellen=2, vor="u = ", nach=" V", farbe=BLAU)
    zi = s.zahl(None, "0.6*sin(2*pi*T - pi/3)", (2.0, -0.3), stellen=2, vor="i = ", nach=" A", farbe=ROT)
    s.einblenden(a, dauer=0.6)
    with s.gleichzeitig():
        s.zeichnen(ku, dauer=1.2)
        s.zeichnen(ki, dauer=1.2)
    s.einblenden(lin, mu, mi, zt, zu, zi, dauer=0.5)
    s.verstellen("T", 1.9, dauer=6, rate="linear")
    s.speichern()


def zeiger():
    """Zeiger z = r·e^{jφ}: dreht sich um 315° und wird dabei kürzer (zwei Parameter zugleich); die Spitze
    hinterlässt ihre Spur, die gestrichelte Linie zeigt den Realteil."""
    s = Szene("beispiel/anim_l3_zeiger", reihenfolge="anlegen")
    s.welt()                                # on=None = Szeneneinheiten (Zahlen rechts neben dem Bild)
    a = s.achsen((-2, 2, 1), (-2, 2, 1), breite=3.4, hoehe=3.4, mitte=(-1.6, 0), kreuz=True, xl="Re", yl="Im")
    s.parameter("r", 1.8)
    s.parameter("phi", 0)
    spur = s.weg(a, "(1.8 - 1.2*t/(2*pi))*cos(t)", "(1.8 - 1.2*t/(2*pi))*sin(t)", 0, "phi", farbe=HELLGRAU, dicke=3, n=121)
    re = s.linie(a, ("r*cos(phi)", "r*sin(phi)"), ("r*cos(phi)", 0), farbe=GRAU, dicke=2, dash=DASH)
    z = s.pfeil((0, 0), ("r*cos(phi)", "r*sin(phi)"), label="", farbe=BLAU, dicke=5, spitze=0.24, on=a)
    zr = s.zahl(None, "r", (1.4, 0.5), stellen=2, vor="|z| = ")
    zp = s.zahl(None, "phi*180/pi", (1.4, -0.1), stellen=0, vor="\\varphi = ", nach="°")
    s.einblenden(a, dauer=0.6)
    s.zeichnen(z, dauer=0.8)
    s.einblenden(re, zr, zp, dauer=0.5)
    with s.gleichzeitig():
        s.verstellen("phi", "7*pi/4", dauer=5, rate="linear")
        s.verstellen("r", 0.6, dauer=5, rate="linear")
    s.speichern()


def grenzwert():
    """Grenzprozess mit ganzzahligem n: (1 + x/n)^n nähert sich e^x, an der Stelle x = 1 der Zahl e."""
    s = Szene("beispiel/anim_l3_grenzwert", reihenfolge="anlegen")
    s.welt()                                # on=None = Szeneneinheiten (Zahlen rechts neben dem Bild)
    a = s.achsen((0, 2, 0.5), (0, 8, 2), breite=3.8, hoehe=3.0, mitte=(-1.7, 0), xl="x", yl="y")
    s.parameter("n", 1, ganzzahlig=True)
    ex = s.kurve(a, "exp(x)", farbe=GRAU, dicke=4, dash=DASH)
    fn = s.kurve(a, "(1 + x/n)^n", farbe=BLAU, punkte=41)
    m = s.marke(a, 1, f="(1 + x/n)^n", hilfslinien=True, farbe=ROT, r=0.08)
    ze = s.text(None, "e^x", (-0.5, 1.45), farbe=GRAU)
    zn = s.zahl(None, "n", (1.0, 0.9), stellen=0, vor="n = ")
    zw = s.zahl(None, "(1 + 1/n)^n", (1.0, 0.3), stellen=4, vor="(1 + 1/n)^n = ", farbe=ROT)
    zg = s.text(None, "e = 2.7183", (1.0, -0.3), farbe=GRAU)
    s.einblenden(a, dauer=0.6)
    with s.gleichzeitig():
        s.zeichnen(ex, dauer=1.0)
        s.einblenden(ze, zg, dauer=0.6)
    s.zeichnen(fn, dauer=0.8)
    s.einblenden(m, zn, zw, dauer=0.5)
    s.verstellen("n", 12, dauer=6, rate="linear")
    s.betonen(zw)
    s.speichern()


def flaeche():
    """Die Fläche unter f wächst mit der oberen Grenze b; die Zahl zeigt ihren Inhalt F(b)."""
    s = Szene("beispiel/anim_l3_flaeche", reihenfolge="anlegen")
    s.welt()                                # on=None = Szeneneinheiten (Zahlen rechts neben dem Bild)
    a = s.achsen((0, 4, 1), (0, 2, 0.5), breite=4.4, hoehe=2.6, mitte=(-1.3, 0), xl="x", yl="f(x)")
    s.parameter("b", 0)
    f = "1 + 0.5*sin(2*x)"
    fl = s.flaeche(a, f, 0, "b", farbe=BLAU, deckung=0.3, punkte=32)
    k = s.kurve(a, f)
    gr = s.linie(a, ("b", 0), ("b", "1 + 0.5*sin(2*b)"), farbe=ROT, dicke=3)
    zb = s.zahl(None, "b", (1.7, 0.6), stellen=2, vor="b = ")
    za = s.zahl(None, "b + 0.25*(1 - cos(2*b))", (1.7, 0.0), stellen=2, vor="A(b) = ", farbe=BLAU)
    s.einblenden(a, dauer=0.6)
    s.zeichnen(k, dauer=1.0)
    s.einblenden(fl, gr, zb, za, dauer=0.5)
    s.verstellen("b", 3.5, dauer=5)
    s.speichern()


if __name__ == "__main__":
    for f in (welle, tangente, zeitmarker, zeiger, grenzwert, flaeche):
        f()
    print("6 Szenen beispiel/anim_l3_* gebaut")
