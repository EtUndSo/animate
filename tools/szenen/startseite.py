"""Startseite: Animation „Fourier-Reihe einer Rechteckschwingung“ (web/szenen/startseite/fourier.json).

Die Szene ist eine gewöhnliche Editor-Szene mit Schritt-für-Schritt-Choreografie (playMode sequential). Das Video auf
der Startseite (web/startseite/fourier.webm/.mp4) entsteht mit dem Video-Export des Editors (tools/startseite_video.py).

Fachlich: Rechteckschwingung x(t) = sgn(sin(2πt/T)) mit Amplitude 1. Ihre Fourier-Reihe enthält nur ungerade
Harmonische: x(t) = Σ_{n=1,3,5,…} b_n sin(2πn t/T) mit b_n = 4/(πn). Die Teilsumme S_N nimmt alle n ≤ N.
Am Sprung schwingt jede Teilsumme um ≈ 9 % der Sprunghöhe über (Gibbs-Phänomen, Grenzwert 1,179 bei Sprung 2).

Nahtlose Schleife: Die gezeichneten Kurven, Stems und die Gibbs-Beschriftung erscheinen nacheinander (Create/FadeIn).
Am Ende blendet je Teilbild ein weißer Vorhang (Rechteck ohne Rand, nur über dem Inneren des Teilbilds) ein.
Er erscheint als letztes Objekt und liegt damit über den Kurven, aber Achsen, Zahlen und Formeln bleiben frei:
Das letzte Bild gleicht dem ersten. Der Vorhang steht in der Szene außerhalb des Bildes und springt erst kurz vor
dem Einblenden an seinen Platz (MoveTo mit Laufzeit ≈ 0). So zeigt die ruhende Editor-Ansicht das fertige Bild.

    python tools/szenen/startseite.py
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import Szene, SZENEN, ORANGE  # noqa: E402

# Farbverlauf der Teilsummen (blau -> türkis -> grün -> oliv), die volle Summe orange
FARBEN = {1: "#2a78d6", 3: "#139a9a", 5: "#00823c", 7: "#6f9418"}
GRAU = "#8c8c8c"
DUNKEL = "#1d1f1e"
NZ, LZ, TZ = 40, 46, 44            # Achsenzahlen, Achsentitel, Text (Szenenpixel; das Video ist 1920 px breit)
N_MAX = 15


def b(n):
    return 4 / (np.pi * n)


def stuetzstellen(nmax):
    """t/T in [0, 2], 8 Stützstellen je Periode der höchsten Harmonischen (glatte Bézier-Kurve durch die Punkte).
    Bewusst Datenkurven statt Funktionsgraphen: Der adaptive Plotter setzt hier über 8000 Punkte je Kurve, und jedes
    Videobild zeichnet alle Kurven neu. So bleibt der Video-Export im Browser in Echtzeit."""
    return np.linspace(0.0, 2.0, max(65, 16 * nmax + 1))


def harmonische(n):
    t = stuetzstellen(n)
    return list(zip(t, b(n) * np.sin(2 * np.pi * n * t)))


def teilsumme(nmax):
    t = stuetzstellen(nmax)
    return list(zip(t, sum(b(n) * np.sin(2 * np.pi * n * t) for n in range(1, nmax + 1, 2))))


def glatte_kurve(s, on, pts, farbe, dicke):
    oid = s.daten(on, [(round(float(x), 5), round(float(y), 5)) for x, y in pts], farbe=farbe, dicke=dicke)
    s.objects[-1]["props"]["smooth"] = True
    # Ohne Abschneiden (alle Punkte liegen im Teilbild): clip_run vergleicht Endpunkte als Gleitkommazahlen auf
    # Gleichheit und zerlegt die Kurve sonst an Rundungsstellen in Stücke, die Create alle gleichzeitig zeichnet.
    s.objects[-1]["props"]["clip"] = False
    return oid


def achsen(s, x, y, breite, hoehe, mitte, **kw):
    """Achsen links/unten, ohne Hilfsstriche nach innen (der Vorhang soll sie nie berühren)."""
    a = s.achsen(x, y, breite=breite, hoehe=hoehe, mitte=mitte, zahl=NZ, label=LZ, **kw)
    o = s.objects[-1]["props"]
    o["minor_ticks"] = False
    o["axis_width"] = 4
    o["x_label_at"] = "end"
    return a


def welt_von(a_props):
    """Daten -> Weltkoordinaten eines Teilbilds (lineare Achsen, origin = Mitte)."""
    (x0, x1), (y0, y1) = a_props["x_range"][:2], a_props["y_range"][:2]
    cx, cy = a_props["origin"][:2]
    W, H = a_props["x_length"], a_props["y_length"]
    return (lambda d: cx + (d - (x0 + x1) / 2) / (x1 - x0) * W,
            lambda d: cy + (d - (y0 + y1) / 2) / (y1 - y0) * H)


def fourier():
    s = Szene("startseite/fourier")
    welt = s.welt()

    # ---------------------------------------------------------------- Teilbilder (statisch)
    p1 = achsen(s, (-0.1, 2.1), (-1.5, 2.0), 8.0, 3.3, (-2.35, 0.75), xmarks=False, xzahlen=False, yticks="-1;0;1")
    p2 = achsen(s, (-0.1, 2.1), (-1.6, 1.6), 8.0, 1.45, (-2.35, -2.55), xl="t/T", xmarks=False,
                xticks="0;0.5;1;1.5;2", ymarks=False, yzahlen=False)
    p3 = achsen(s, (-0.5, 16), (-0.1, 1.45), 3.8, 4.3, (4.8, -0.25), xl="n", xticks="1;3;5;7;9;11;13;15", yticks="0;0.5;1")
    props = {o["id"]: o["props"] for o in s.objects}
    w1x, w1y = welt_von(props[p1])
    w2x, w2y = welt_von(props[p2])
    w3x, w3y = welt_von(props[p3])

    s.formel(r"x(t)=\sum_{n=1,3,5,\dots} b_n\,\sin\!\left(2\pi n\,\frac{t}{T}\right)", mitte=(-2.35, 3.33), hoehe=0.9, farbe=DUNKEL)
    s.formel(r"b_n=\frac{4}{\pi n}", mitte=(4.8, 2.62), hoehe=0.78, farbe=DUNKEL)
    harm = s.tr("harm", de="Harmonische", en="Harmonics", es="Armónicos", zh="谐波", fr="Harmoniques", tr="Harmonikler")
    s.text(welt, harm, (w2x(-0.1), -1.36), groesse=TZ, farbe="#555a57")

    # ---------------------------------------------------------------- Akteure (erscheinen nacheinander)
    anim = []

    def zeige(oid, typ="Create", dauer=0.6):
        anim.append({"type": typ, "target": oid, "run_time": dauer})

    rechteck = [(0, 0), (0, 1), (0.5, 1), (0.5, -1), (1, -1), (1, 1), (1.5, 1), (1.5, -1), (2, -1), (2, 0)]
    zeige(s.daten(p1, rechteck, farbe=GRAU, dicke=5, dash="16,11"), dauer=0.9)

    for n, farbe in FARBEN.items():
        zeige(s.stems(p3, [n], [b(n)], farbe=farbe, dicke=8, r=0.09), dauer=0.4)
        zeige(glatte_kurve(s, p2, harmonische(n), farbe, 5), dauer=0.5)
        zeige(glatte_kurve(s, p1, teilsumme(n), farbe, 6), dauer=0.7)

    rest = list(range(9, N_MAX + 1, 2))
    zeige(s.stems(p3, rest, [b(n) for n in rest], farbe=ORANGE, dicke=8, r=0.09), dauer=0.6)
    zeige(glatte_kurve(s, p1, teilsumme(N_MAX), ORANGE, 7), dauer=1.0)

    # Gibbs: erstes Maximum der Teilsumme S_15 (bei t ≈ T/(2(N+1)))
    t = np.linspace(0.0, 0.1, 20001)
    sN = sum(b(n) * np.sin(2 * np.pi * n * t) for n in range(1, N_MAX + 1, 2))
    tp, yp = float(t[np.argmax(sN)]), float(sN.max())
    proz = round((yp - 1) / 2 * 100)                       # Überschwingen bezogen auf die Sprunghöhe 2
    gibbs = s.tr("gibbs", de="Gibbs-Phänomen: ≈ %d %% Überschwingen" % proz,
                 en="Gibbs phenomenon: ≈ %d %% overshoot" % proz, es="Fenómeno de Gibbs: ≈ %d %% de sobreoscilación" % proz,
                 zh="吉布斯现象：约 %d%% 过冲" % proz, fr="Phénomène de Gibbs : ≈ %d %% de dépassement" % proz,
                 tr="Gibbs olayı: ≈ %%%d aşma" % proz)
    txt = s.text(welt, gibbs, (w1x(0.17), w1y(1.74)), groesse=TZ, farbe=DUNKEL)
    zeige(txt, "FadeIn", 0.5)
    zeige(s.pfeil((w1x(0.16), w1y(1.62)), (w1x(tp + 0.004), w1y(yp + 0.06)), farbe=DUNKEL, dicke=4, spitze=0.2, on=welt), dauer=0.4)
    zeige(txt, "Indicate", 0.9)

    # ---------------------------------------------------------------- Vorhänge (zuletzt: liegen über allem Gezeichneten)
    def vorhang(x0, x1, y0, y1):
        mitte = [(x0 + x1) / 2, (y0 + y1) / 2, 0]
        oid = s._add("Rectangle", {"center": [mitte[0], -14.0, 0], "width": x1 - x0, "height": y1 - y0, "color": "#ffffff",
                                   "fill_color": "#ffffff", "fill_opacity": 1.0, "stroke_width": 0, "dash": "", "show_center": False}, welt)
        anim.append({"type": "MoveTo", "target": oid, "run_time": 0.001, "point": mitte})
        anim.append({"type": "FadeIn", "target": oid, "run_time": 0.45})
        return oid, mitte

    vorhang(w1x(-0.1) + 0.15, w1x(2.1), w1y(-1.5) + 0.06, w1y(2.0) - 0.02)          # Teilsummen
    vorhang(w2x(-0.1) + 0.15, w2x(2.1), w2y(-1.6) + 0.05, w2y(1.6) + 0.03)          # Harmonische
    letzt, mitte = vorhang(w3x(-0.5) + 0.16, w3x(16) - 0.05, w3y(-0.1) + 0.16, w3y(1.45) - 0.04)   # Spektrum
    anim.append({"type": "MoveTo", "target": letzt, "run_time": 0.4, "point": mitte})   # Pause: leeres Bild = erstes Bild

    m = s.model()
    m["model"]["animations"] = [dict(a, id="a%d" % (i + 1)) for i, a in enumerate(anim)]
    m["model"]["playMode"] = "sequential"
    m["counters"]["nextAnimId"] = len(anim) + 1
    pfad = SZENEN / (s.name + ".json")
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    dauer = sum(a["run_time"] for a in anim)
    print(pfad, "%d Objekte, %d Animationen, %.2f s, Gibbs-Spitze %.4f bei t/T = %.4f" % (s.n, len(anim), dauer, yp, tp))


if __name__ == "__main__":
    fourier()
