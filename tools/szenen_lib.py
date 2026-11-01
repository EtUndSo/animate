"""Helfer, um Editor-Szenen (web/szenen/**.json) aus Python zu schreiben.

Die Szene ist danach eine gewöhnliche Editor-Szene: Sie lässt sich im Editor öffnen und ändern. Dieses Modul spart
nur Schreibarbeit, wenn viele Abbildungen dasselbe Aussehen haben sollen (Größen, Farben, Achsenstil).

    from szenen_lib import Szene, BLAU, ROT, GRAU, daten, duenn
    s = Szene("et3/k8beispiel")
    a = s.achsen(x=(0, 2, 0.5), y=(-1, 1, 0.5), breite=3, hoehe=2, mitte=(-2, 0), xl="t in s", yl="y(t)")
    s.kurve(a, "exp(-x)*sin(2*pi*x)", farbe=BLAU)
    s.text(a, s.tr("anf", de="Anfang", en="Start", es="Inicio", zh="起点"), (0.2, 0.8), farbe=ROT)
    s.speichern()

Regeln für Artikelbilder (engine/export.py):
- 1 Szeneneinheit = 135 Szenenpixel = 74 Pixel in der Artikelspalte. Die Spalte ist 548 px breit: Die Zeichnung
  darf mit allen Beschriftungen höchstens 7,4 Einheiten breit sein. Der sichtbare Rahmen geht von x = -7,11 bis 7,11
  und y = -4 bis 4, alles außerhalb wird abgeschnitten.
- Texte in Szenenpixeln: 24-28 ergibt 13-15 px im Artikel. Kleiner als 22 nicht.
- Dezimalzahlen in Labels immer mit Punkt schreiben (0.5): Die Sprache macht daraus 0,5 (de, es).
- Wörter stehen in der Tabelle der Szene (s.tr), je Sprache ein Text. Formelzeichen sind sprachfrei.
- Winkel im Bogenmaß: pgfplots rechnet sin(360*x) in Grad, hier heißt das sin(2*pi*x).
- on=None heißt Weltkoordinaten nur in Szenen ohne Achsen. Gibt es Achsen, landet das Objekt auf den ersten: Dann entweder
  s.welt() als erstes Objekt aufrufen oder Texte und Legenden mit on=<achsen> in Datenkoordinaten setzen.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SZENEN = ROOT / "web" / "szenen"

# Farben der Arbeitshefte
BLAU, ROT, GRUEN, ORANGE, GRAU, SCHWARZ = "#2a78d6", "#c82828", "#00823c", "#eb6834", "#7f7f7f", "#111111"
HELLGRAU = "#b5b5b5"
DASH, DOT = "10,7", "2,5"

TEXT = 26                  # normale Beschriftung
ZAHL = 24                  # Achsenzahlen
ACHSTITEL = 26             # Achsen- und Teilbildtitel


def daten(pfad, x=1, y=2):
    """Zwei Spalten (ab 1 gezählt) einer .dat-Datei als Liste [(x, y)]. Kopfzeilen werden übersprungen."""
    pts = []
    for line in Path(pfad).read_text(encoding="utf-8").splitlines():
        try:
            row = [float(v) for v in line.split()]
        except ValueError:
            continue
        if len(row) >= max(x, y):
            pts.append((row[x - 1], row[y - 1]))
    return pts


def duenn(pts, tol=1e-3):
    """Ramer-Douglas-Peucker: Punkte weglassen, die um weniger als tol (relativ zur Spanne) von der Linie abweichen.
    Misst linear: Kurven auf einer Log-Achse nicht ausdünnen, sonst entstehen dort sichtbare Knicke."""
    if len(pts) < 3:
        return list(pts)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    sx, sy = (max(xs) - min(xs)) or 1.0, (max(ys) - min(ys)) or 1.0
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay, bx, by = pts[a][0] / sx, pts[a][1] / sy, pts[b][0] / sx, pts[b][1] / sy
        dx, dy = bx - ax, by - ay
        n = (dx * dx + dy * dy) ** 0.5 or 1.0
        best, bi = 0.0, None
        for i in range(a + 1, b):
            d = abs((pts[i][0] / sx - ax) * dy - (pts[i][1] / sy - ay) * dx) / n
            if d > best:
                best, bi = d, i
        if bi is not None and best > tol:
            keep[bi] = True
            stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def _zahl(v):
    return ("%.6g" % v)


class Szene:
    def __init__(self, name, margin=24):
        self.name = name
        self.objects, self.strings = [], {}
        self.n = 0
        self.margin = margin

    # ---------------------------------------------------------------------------- intern
    def _add(self, typ, props, on=None):
        self.n += 1
        oid = "o%d" % self.n
        o = {"id": oid, "type": typ, "props": props}
        if on:
            o["on"] = on
        self.objects.append(o)
        return oid

    def tr(self, key, de, en, es, zh):
        """Text in vier Sprachen; das Ergebnis steht im Label. "@{key}" darf auch Teil eines längeren Labels sein."""
        self.strings[key] = {"de": de, "en": en, "es": es, "zh": zh}
        return "@" + key

    # ---------------------------------------------------------------------------- Achsen
    def achsen(self, x, y, breite=3.0, hoehe=2.2, mitte=(0, 0), xl="", yl="", titel="", kreuz=False, gitter=False, xticks="",
               yticks="", xmarks=True, ymarks=True, xzahlen=True, yzahlen=True, xlog=False, ylog=False, rahmen=False,
               xl_mitte=True, titel_mitte=False, zahl=ZAHL, label=ACHSTITEL, unsichtbar=False):
        """x, y = (von, bis) oder (von, bis, Schritt). kreuz=True: Achsenkreuz mit Pfeilen durch den Nullpunkt
        (Lehrbuchstil), sonst Achsen unten und links wie pgfplots."""
        p = {"x_range": list(x), "y_range": list(y), "x_length": breite, "y_length": hoehe, "origin": [mitte[0], mitte[1], 0],
             "title": titel, "x_label": xl, "y_label": yl, "number_size": zahl, "label_size": label, "axis_width": 3,
             "x_ticks": xticks, "y_ticks": yticks, "x_tick_marks": xmarks, "y_tick_marks": ymarks,
             "x_numbers": xzahlen, "y_numbers": yzahlen, "x_log": xlog, "y_log": ylog, "frame": rahmen,
             "title_at": "center" if titel_mitte else "left", "minor_ticks": True}
        if unsichtbar:
            p["show_axes"] = False
        if kreuz:
            p.update(arrows=True, x_label_at="end", arrow_size=0.16)
        else:
            p.update(x_axis_at="bottom", y_axis_at="left", x_label_at="center" if xl_mitte else "end")
        if gitter:
            p.update(grid_x=True, grid_y=True, grid_color="#d9d9d9", grid_width=1)
        return self._add("Axes", p)

    def welt(self):
        """Unsichtbares Achsenkreuz 1:1 als ERSTES Objekt einer Szene, die Achsen und freie Zeichnung mischt: Danach heißt
        on=None Szeneneinheiten. Reine Blockbilder und Schaltungen ohne Achsen brauchen es nicht."""
        return self.achsen((-7, 7), (-4, 4), breite=14, hoehe=8, mitte=(0, 0), unsichtbar=True)

    # ---------------------------------------------------------------------------- Kurven
    def kurve(self, on, f, x=None, farbe=BLAU, dicke=5, dash=""):
        """Graph y = f(x); Ausdruckssprache des Editors (sin, exp, rect, tri, epsilon, si, where, floor, ...)."""
        p = {"func": f, "color": farbe, "stroke_width": dicke, "dash": dash}
        if not x:                                      # ohne Angabe die ganze Achse (der Katalogwert wäre -10..10)
            ach = next((o for o in self.objects if o["id"] == on and o["type"] == "Axes"), None)
            x = ach["props"]["x_range"][:2] if ach else None
        if x:
            p["x_range"] = list(x)
        return self._add("FunctionGraph", p, on)

    def daten(self, on, pts, farbe=BLAU, dicke=4, dash="", treppe="", marker=False, marker_r=0.06):
        """Kurve aus Punkten [(x, y)]; am Teilbild abgeschnitten."""
        txt = "\n".join("%s %s" % (_zahl(a), _zahl(b)) for a, b in pts)
        return self._add("DataCurve", {"data": txt, "clip": True, "step": treppe, "markers": marker, "marker_radius": marker_r,
                                       "color": farbe, "stroke_width": dicke, "dash": dash}, on)

    def flaeche(self, on, f, x0, x1, f2="", farbe=BLAU, deckung=0.3):
        return self._add("Area", {"func": f, "func2": f2, "x_min": x0, "x_max": x1, "samples": 120, "color": farbe,
                                  "fill_color": farbe, "fill_opacity": deckung, "stroke_width": 0}, on)

    def stems(self, on, xs, ys=None, func="", farbe=BLAU, dicke=4, marker="circle", r=0.07, pfeile=False, breite=0, basis=0):
        """Stems mit Marker, Dirac-Pfeile (pfeile=True) oder Balken (breite in Dateneinheiten). func statt ys rechnet die Werte."""
        p = {"x": ";".join(_zahl(v) for v in xs), "func": func, "baseline": basis, "arrows": pfeile, "width": breite, "marker": marker,
             "markers": True, "marker_radius": r, "color": farbe, "stroke_width": dicke, "dash": ""}
        p["y"] = ";".join(_zahl(v) for v in ys) if ys is not None else ""
        return self._add("Stem", p, on)

    def punkt(self, on, x, y, farbe=SCHWARZ, r=0.08):
        return self._add("Dot", {"center": [x, y, 0], "radius": r, "color": farbe, "fill_color": farbe, "fill_opacity": 1, "stroke_width": 0}, on)

    def linie(self, on, a, b, farbe=SCHWARZ, dicke=3, dash=""):
        return self._add("Line", {"start": [a[0], a[1], 0], "end": [b[0], b[1], 0], "color": farbe, "stroke_width": dicke, "dash": dash}, on)

    def weg(self, on, fx, fy, t0, t1, farbe=BLAU, dicke=4, pfeile="", n=161, dash=""):
        """Parametrischer Weg; pfeile = "0.25;0.75": Richtungsmarken an diesen Stellen, "" = keine."""
        return self._add("ParametricCurve", {"fx": fx, "fy": fy, "t_min": t0, "t_max": t1, "samples": n, "show_arrow": bool(pfeile), "arrow_at": pfeile,
                                             "color": farbe, "stroke_width": dicke, "dash": dash}, on)

    def band(self, on, x0, x1, y0, y1, farbe=BLAU, deckung=0.15):
        return self._add("Band", {"x_min": x0, "x_max": x1, "y_min": y0, "y_max": y1, "full_height": False, "full_width": False, "label": "",
                                  "color": farbe, "fill_color": farbe, "fill_opacity": deckung, "stroke_width": 0, "dash": ""}, on)

    def kreis(self, on, x, y, r, farbe=SCHWARZ, dicke=3, fuellung=None, deckung=0.0, dash=""):
        return self._add("Circle", {"radius": r, "center": [x, y, 0], "color": farbe, "fill_color": fuellung or farbe, "fill_opacity": deckung,
                                    "stroke_width": dicke, "dash": dash}, on)

    def kreuzchen(self, on, x, y, farbe=ROT, groesse=0.26, dicke=4):
        return self._add("Mark", {"center": [x, y, 0], "kind": "cross", "size": groesse, "color": farbe, "stroke_width": dicke}, on)

    def legende(self, on, eintraege, pos, zeile=0.34, groesse=24):
        """eintraege = [(Text, Farbe, Stil)], Stil wie in matplotlib: "-", "--", ":", "o", "s", "-o"."""
        def schluessel(t):                             # mehrere Einträge in einem Text: @key geht nur als @{key}
            return "@{%s}" % t[1:] if t.startswith("@") and not t.startswith("@{") else t
        return self._add("Legend", {"labels": ";".join(schluessel(e[0]) for e in eintraege), "colors": ";".join(e[1].lstrip("#") for e in eintraege),
                                    "styles": ";".join(e[2] if len(e) > 2 else "-" for e in eintraege), "position": [pos[0], pos[1], 0],
                                    "font_size": groesse, "row_gap": zeile, "swatch_len": 0.4, "gap": 0.12, "color": SCHWARZ, "stroke_width": 4}, on)

    # ---------------------------------------------------------------------------- Text und Blöcke
    def text(self, on, s, pos, groesse=TEXT, ausrichtung="left", farbe=SCHWARZ):
        return self._add("Text", {"text": s, "position": [pos[0], pos[1], 0], "font_size": groesse, "align": ausrichtung, "color": farbe}, on)

    def box(self, s, mitte, breite=0, hoehe=0, form="rect", groesse=TEXT, farbe=SCHWARZ, fuellung="#ffffff", deckung=1.0, dicke=3, dash=""):
        return self._add("TextBox", {"text": s, "center": [mitte[0], mitte[1], 0], "width": breite, "height": hoehe, "shape": form, "padding": 0.2,
                                     "font_size": groesse, "color": farbe, "fill_color": fuellung, "fill_opacity": deckung, "stroke_width": dicke, "dash": dash})

    def pfeil(self, a, b, label="", knick="none", farbe=SCHWARZ, dicke=3, spitze=0.22, groesse=TEXT, on=None, label_seite="left", at="mid", dash="", doppelt=False):
        return self._add("LabeledArrow", {"start": [a[0], a[1], 0], "end": [b[0], b[1], 0], "label": label, "label_at": at, "double": doppelt, "elbow": knick,
                                          "thick": 0, "head_size": spitze, "font_size": groesse, "color": farbe, "stroke_width": dicke, "dash": dash,
                                          "label_side": label_seite}, on)

    def bauteil(self, art, mitte, drehung=0, laenge=2.0, label="", farbe=SCHWARZ, dicke=3, **kw):
        """Zweipol; art: resistor, capacitor, inductor, ... (Editor-Katalog Elektrotechnik · Schaltplan)."""
        p = {"kind": art, "center": [mitte[0], mitte[1], 0], "rotation": drehung, "length": laenge, "label": label, "color": farbe, "stroke_width": dicke}
        p.update(kw)
        return self._add("Component", p)

    def geraet(self, art, mitte, drehung=0, label="", groesse=1.0, farbe=SCHWARZ, dicke=3, **kw):
        """Mehrpol oder Schaltzeichen ohne Länge; art: ground, terminal, node, npn, pnp, opamp, ... (Device im Editor-Katalog)."""
        p = {"kind": art, "center": [mitte[0], mitte[1], 0], "rotation": drehung, "flip": False, "label": label, "pins": False,
             "size": groesse, "color": farbe, "stroke_width": dicke}
        p.update(kw)
        return self._add("Device", p)

    def draht(self, *pkte, farbe=SCHWARZ, dicke=3):
        """Leitung durch die Punkte (mehrere gerade Stücke)."""
        ids = []
        for a, b in zip(pkte, pkte[1:]):
            ids.append(self._add("Line", {"start": [a[0], a[1], 0], "end": [b[0], b[1], 0], "color": farbe, "stroke_width": dicke, "dash": ""}))
        return ids

    # ---------------------------------------------------------------------------- Ablegen
    def model(self):
        return {"v": 1, "counters": {"nextId": self.n + 1, "nextAnimId": 1, "nextCompId": 1},
                "model": {"objects": self.objects, "animations": [], "computations": [],
                          "background": {"color": "#ffffff", "transparent": False, "shadows": True, "axes_on_top": False},
                          "playMode": "sequential", "angleUnit": "rad", "domain": "real",
                          "camera": {"mode": "2d", "theta": 0.6, "phi": 1.0, "zoom": 1.0},
                          "export": {"mode": "content", "margin": self.margin, "scale": 0.55, "frame": None},
                          "lang": "de", "strings": self.strings}}

    def speichern(self):
        p = SZENEN / (self.name + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.model(), ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
        return p
