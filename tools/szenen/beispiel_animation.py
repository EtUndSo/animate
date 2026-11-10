"""Beispiele für Abbildungen mit Zeitachse (animierte Artikelbilder, Anleitung: notizen/animationen.md).

Bauen:  python tools/szenen/beispiel_animation.py
Export: python tools/export_szenen.py --animiert beispiel/anim_bootkette beispiel/anim_sprung beispiel/anim_esb \
            beispiel/anim_norm beispiel/anim_umformen startseite/fourier prog/k3rquadrate
        (schreibt je Szene und Sprache <szene>.svg = Endbild und <szene>.anim.svg = Animation)

Die ersten vier sind Kopien vorhandener Szenen (Zeichnung unverändert), denen nur eine Zeitachse angehängt wird: So
zeigt das statische Bild dasselbe wie das Original, und die Animation baut es Schritt für Schritt auf. anim_umformen
zeigt die Animationen Verschwinden (L1), Umformen (L2) und Zellen betonen (L9) an einer eigenen kleinen Szene.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import SZENEN  # noqa: E402


def mit_zeitachse(quelle, ziel, plan):
    """Kopie der Szene quelle mit der Zeitachse aus plan(s) als Szene ziel (die Objekte bleiben, wie sie sind)."""
    d = json.loads((SZENEN / (quelle + ".json")).read_text(encoding="utf-8"))
    s = Szene(ziel)
    plan(s)
    d["model"]["animations"] = s._anims
    d["counters"]["nextAnimId"] = len(s._anims) + 1
    p = SZENEN / (ziel + ".json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    return p


def bootkette(s):
    """Blockbild: die Startkette baut sich Glied für Glied auf, jeder Pfeil zeichnet sich zum nächsten Kasten."""
    kaesten = [("o1", "o2"), ("o3", "o4"), ("o5", "o6"), ("o7", "o8")]
    pfeile = [("o9", "o10", "o11"), ("o12", "o13", "o14"), ("o15", "o16", "o17")]
    for i, (k, t) in enumerate(kaesten):
        with s.gleichzeitig():
            s.wachsen(k, dauer=0.5)
            s.einblenden(t, dauer=0.5)
        if i < len(pfeile):
            p, oben, unten = pfeile[i]
            s.zeichnen(p, dauer=0.6)
            s.einblenden(oben, unten, dauer=0.5)
    s.einblenden("o18", dauer=0.6)
    s.betonen("o18")


def sprung(s):
    """Funktionsgraph: Achsen, dann die vier Kurven nacheinander, zuletzt die Legende."""
    s.einblenden("o1", dauer=0.6)
    for k in ("o2", "o3", "o4", "o5"):
        s.zeichnen(k, dauer=1.2)
    s.einblenden("o6", dauer=0.6)


def esb(s):
    """Schaltung (ET1, Ersatzschaltbilder des Transistors): die drei Betriebsfälle nacheinander, im aktiven Fall
    erscheinen die Quellen und die Ströme einzeln."""
    def gruppe(*ids, dauer=0.6):
        with s.gleichzeitig():
            for i in ids:
                s.einblenden(i, dauer=dauer)
    gruppe("o60", *("o%d" % i for i in range(1, 10)))
    gruppe("o61", *("o%d" % i for i in range(10, 25)))
    with s.gleichzeitig():
        s.wachsen("o25"); s.einblenden("o26", "o27")
    with s.gleichzeitig():
        s.wachsen("o28"); s.einblenden("o30")
    with s.gleichzeitig():
        for p, t in (("o29", None), ("o31", "o32"), ("o33", "o34")):
            s.zeichnen(p, dauer=0.8)
            if t:
                s.einblenden(t, dauer=0.8)
    gruppe("o62", *("o%d" % i for i in range(35, 50)))
    with s.gleichzeitig():
        for q, t, plus in (("o50", "o51", "o52"), ("o53", "o54", "o55")):
            s.wachsen(q); s.einblenden(t, plus)
    with s.gleichzeitig():
        for p, t in (("o56", "o57"), ("o58", "o59")):
            s.zeichnen(p, dauer=0.8); s.einblenden(t, dauer=0.8)


def norm(s):
    """3D (feste Kamera): Achsen, Quader-Kanten, dann die Diagonalen und die Beschriftung."""
    s.einblenden("o1", dauer=0.5)
    with s.gleichzeitig():
        for i in list(range(2, 13)) + [14]:
            s.zeichnen("o%d" % i, dauer=1.2)
    s.einblenden("o20", "o21", "o22", "o24")
    with s.gleichzeitig():
        s.zeichnen("o13", dauer=0.8); s.einblenden("o23", dauer=0.8)
    with s.gleichzeitig():
        s.zeichnen("o15", dauer=1.2); s.einblenden("o16", "o17", "o18", "o19", dauer=1.2)
    with s.gleichzeitig():
        s.einblenden(*("o%d" % i for i in range(25, 30)), dauer=0.6)


def formel_zeilen(s):
    """Rechenbild aus s.formel (aligned): Zeile für Zeile, wie s.formel(..., zeilenweise=True)."""
    s.animation("FadeIn", "o1", 4.8, lines=True)


def umformen():
    """L1/L2/L9 an einer kleinen Szene: Quadrat wird Kreis, Formel stellt sich um, Tabellenzellen leuchten nacheinander
    auf, ein Hilfspfeil verschwindet wieder."""
    s = Szene("beispiel/anim_umformen")
    q = s._add("Square", {"side": 1.4, "center": [-2.6, 0.9, 0], "color": BLAU, "fill_color": BLAU, "fill_opacity": 0.25,
                          "stroke_width": 4})
    k = s._add("Circle", {"radius": 0.8, "center": [-2.6, 0.9, 0], "color": ORANGE, "fill_color": ORANGE, "fill_opacity": 0.25,
                          "stroke_width": 4})
    f1 = s.formel(r"a\cdot(b+c)", mitte=(1.6, 1.4), hoehe=0.32)
    f2 = s.formel(r"a\cdot b+a\cdot c", mitte=(1.6, 1.4), hoehe=0.32)
    t = s.tabelle([[2, 1, 5], [4, 3, 11]], links_oben=(0.0, 0.5), zelle_b=0.9, zelle_h=0.55, klammern=True)
    hilfe = s.pfeil((-1.6, -0.8), (-0.3, -0.25), farbe=GRUEN)
    s.zeichnen(q, dauer=1.0)
    s.umformen(q, k, dauer=1.2)                       # L2: Quadrat -> Kreis (k selbst wird nie gezeichnet)
    s.schreiben(f1, dauer=1.0)
    s.umformen(f1, f2, dauer=1.4, passend=True)       # L2: gleiche Zeichen wandern
    s.einblenden(t, dauer=0.5)
    s.zeichnen(hilfe, dauer=0.6)
    s.betonen(t, zelle=(1, 0))                        # L9: eine Zelle
    s.betonen(t, zeile=0)                             # L9: eine Zeile
    s.ausblenden(hilfe, dauer=0.5)                    # L1: Hilfspfeil verschwindet
    s.speichern()


if __name__ == "__main__":
    mit_zeitachse("linux/k1bootkette", "beispiel/anim_bootkette", bootkette)
    mit_zeitachse("et3/k2sprung", "beispiel/anim_sprung", sprung)
    mit_zeitachse("et1/k10esb", "beispiel/anim_esb", esb)
    mit_zeitachse("hm1/k8norm", "beispiel/anim_norm", norm)
    mit_zeitachse("prog/k3rmittel", "beispiel/anim_formel", formel_zeilen)
    umformen()
    print("Beispiele mit Zeitachse geschrieben")
