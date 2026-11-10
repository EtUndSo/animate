"""Beispiele für Kamerafahrten in 3D (L4, Anleitung: notizen/animationen.md §10).

Bauen:  python tools/szenen/beispiel_kamera.py
Export: python tools/export_szenen.py --animiert beispiel/anim_l4_flaeche beispiel/anim_l4_kristall beispiel/anim_l4_ebene

s.kamera_start(theta, phi) macht die Szene dreidimensional (Winkel in Grad, z zeigt nach oben); s.kamera(...) fährt die
Kamera über die Zeit (drehen, neigen, zoomen, Blickpunkt), auch gleichzeitig mit anderen Animationen. Im Artikel
projiziert der Spieler selbst (die Datei trägt Weltpunkte und die Kamera-Spur) und zeichnet von hinten nach vorn. Das
statische Bild und das PDF zeigen die Endstellung der Kamera.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403


def flaeche():
    """Die Kamera fährt um die Fläche z = 1 + sin(x)·cos(y)/1,3: erst ein gutes Stück herum, dann von höher oben."""
    s = Szene("beispiel/anim_l4_flaeche", reihenfolge="anlegen")
    s.kamera_start(theta=-70, phi=22)
    a = s.achsen3d(z=(0, 2))
    f = s.flaeche3d(a, "1 + sin(x)*cos(y)/1.3", aufloesung=20)
    t = s.text(a, "z = f(x, y)", (1.7, -1.7, 2.3), groesse=TEXT, ausrichtung="center")
    s.zuoberst(t)                         # die Beschriftung bleibt vor der Fläche
    s.einblenden(a, dauer=0.5)
    s.zeichnen(f, dauer=1.2)
    s.einblenden(t, dauer=0.4)
    s.kamera(drehen=150, dauer=4.0)
    s.kamera(phi=50, dauer=2.0)
    s.pause(0.4)
    s.speichern()


def kristall():
    """Kubisch raumzentrierte Zelle (bcc): Die Kamera dreht halb um die senkrechte Achse, zoomt auf das Zentrum und
    fährt dann zurück in eine Ansicht quer zur Raumdiagonale, auf der Ecke, Zentrum und Gegenecke liegen."""
    s = Szene("beispiel/anim_l4_kristall", reihenfolge="anlegen")
    s.kamera_start(theta=25, phi=18)
    h = 1.1
    ecken = [(x, y, z) for x in (-h, h) for y in (-h, h) for z in (-h, h)]
    kanten = [s.linie(None, p, q, farbe=GRAU, dicke=3) for i, p in enumerate(ecken) for q in ecken[i + 1:]
              if sum(abs(u - v) > 1e-9 for u, v in zip(p, q)) == 1]
    atome = [s.kugel(None, p, r=0.26, farbe=BLAU) for p in ecken]
    mitte = s.kugel(None, (0, 0, 0), r=0.3, farbe=ORANGE)
    diag = s.linie(None, (-h, -h, -h), (h, h, h), farbe=ROT, dicke=3, dash=DASH)
    s.einblenden(*kanten, dauer=0.6)
    s.einblenden(*atome, dauer=0.6)
    s.einblenden(mitte, dauer=0.5)
    s.kamera_kreisen(180, dauer=4.0)
    s.kamera(zoom=1.8, dauer=1.2)
    with s.gleichzeitig():
        s.kamera(phi=12, theta=315, zoom=1.0, dauer=2.0)
        s.zeichnen(diag, dauer=2.0)
    s.pause(0.5)
    s.speichern()


def ebene():
    """Tangentialebene an z = 2 - (x² + y²)/4 im Punkt P = (a, 0,5): Die Kamera dreht, während Ebene und P erscheinen,
    P wandert (Parameter a), dann zoomt die Kamera auf P: nah an P schmiegt sich die Ebene an die Fläche. Zum Schluss
    wieder die ganze Fläche (Endbild für Heft und PDF)."""
    s = Szene("beispiel/anim_l4_ebene", reihenfolge="anlegen")
    s.kamera_start(theta=-60, phi=24)
    ax = s.achsen3d(z=(0, 2.2))
    s.parameter("a", -1.0)
    flaeche = s.flaeche3d(ax, "2 - (x^2 + y^2)/4", deckung=0.8, aufloesung=18)
    y0 = 0.5
    z0 = "(2 - (a^2 + %s)/4)" % (y0 * y0)
    dx, dy = "(-a/2)", "(%s)" % (-y0 / 2)
    k = [-0.9, -0.3, 0.3, 0.9]

    def ecke(u, v):                       # Punkt der Tangentialebene über (a + u, y0 + v), knapp über der Fläche
        return ("a + %s" % u, y0 + v, "%s + %s*%s + %s*%s + 0.02" % (z0, dx, u, dy, v))
    teile = [s.vieleck(ax, [ecke(k[i], k[j]), ecke(k[i + 1], k[j]), ecke(k[i + 1], k[j + 1]), ecke(k[i], k[j + 1])],
                       farbe=ORANGE, deckung=0.55, dicke=1)
             for i in range(3) for j in range(3)]
    p = s.kugel(ax, ("a", y0, z0 + " + 0.03"), r=0.08, farbe=ROT)
    lp = s.text(ax, "P", ("a + 0.15", y0, z0 + " + 0.3"), groesse=TEXT, farbe=ROT)
    s.zuoberst(*teile)                    # die Ebene liegt über der Kuppel: vor allen Facetten der Fläche
    s.zuoberst(p, lp, stufe=2)
    s.einblenden(ax, dauer=0.5)
    s.zeichnen(flaeche, dauer=1.0)
    with s.gleichzeitig():
        s.kamera(drehen=60, dauer=2.5)
        s.einblenden(*teile, p, lp, dauer=1.2)
    with s.gleichzeitig():
        s.verstellen("a", 0.6, dauer=2.5)
        s.kamera(drehen=30, phi=32, dauer=2.5)
    s.kamera(blickpunkt=(0.6, y0, 2 - (0.36 + y0 * y0) / 4), zoom=3.0, dauer=1.8)
    s.pause(0.6)
    s.kamera(blickpunkt=(0, 0, 0), zoom=1.0, dauer=1.5)
    s.speichern()


for f in (flaeche, kristall, ebene):
    f()
