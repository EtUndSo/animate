"""Helfer, um Editor-Szenen (web/szenen/**.json) aus Python zu schreiben.

Die Szene ist danach eine gewöhnliche Editor-Szene: Sie lässt sich im Editor öffnen und ändern. Dieses Modul spart
nur Schreibarbeit, wenn viele Abbildungen dasselbe Aussehen haben sollen (Größen, Farben, Achsenstil).

    from szenen_lib import Szene, BLAU, ROT, GRAU, daten, duenn
    s = Szene("et3/k8beispiel")
    a = s.achsen(x=(0, 2, 0.5), y=(-1, 1, 0.5), breite=3, hoehe=2, mitte=(-2, 0), xl="t in s", yl="y(t)")
    s.kurve(a, "exp(-x)*sin(2*pi*x)", farbe=BLAU)
    s.text(a, s.tr("anf", de="Anfang", en="Start", es="Inicio", zh="起点", fr="Début", tr="Başlangıç"), (0.2, 0.8), farbe=ROT)
    s.speichern()

Regeln für Artikelbilder (engine/export.py):
- 1 Szeneneinheit = 135 Szenenpixel = 74 Pixel in der Artikelspalte. Die Spalte ist 548 px breit: Die Zeichnung
  darf mit allen Beschriftungen höchstens 7,4 Einheiten breit sein. Der sichtbare Rahmen geht von x = -7,11 bis 7,11
  und y = -4 bis 4, alles außerhalb wird abgeschnitten.
- Texte in Szenenpixeln: 24-28 ergibt 13-15 px im Artikel. Kleiner als 22 nicht.
- Dezimalzahlen in Labels immer mit Punkt schreiben (0.5): Die Sprache macht daraus 0,5 (de, es, fr, tr).
- Wörter stehen in der Tabelle der Szene (s.tr), je Sprache ein Text. Formelzeichen sind sprachfrei. fr und tr
  dürfen fehlen (dann englischer Text im Bild).
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
FORMEL = 30                # Formeln von summe(), produkt(), skalarprodukt() (LaTeX wirkt bei gleicher Größe kleiner)
PX = 135.0                 # Szenenpixel je Szeneneinheit
TT_ZELLE = 0.6             # Schreibmaschinenschrift (s.text(..., schrift="tt")): Breite einer Zeichenzelle in em


def tt_breite(groesse=TEXT, zeichen=1):
    """Breite von `zeichen` Zellen der Schreibmaschinenschrift in Szeneneinheiten (groesse = Schriftgröße in
    Szenenpixeln wie bei s.text). Ein chinesisches Zeichen belegt zwei Zellen. Spalte i einer links ausgerichteten
    Zeile, die bei x0 beginnt, fängt bei x0 + tt_breite(groesse, i) an."""
    return TT_ZELLE * groesse * zeichen / PX


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


def det_ausdruck(matrix, p="s"):
    """Ausdruck für die Determinante der Zwischenmatrix (1 - p) I + p A von s.abbilden(..., weg="gerade") beim
    Fortschritt p (Parametername): die Fläche des Bilds des Einheitsquadrats (mit Vorzeichen). Für s.zahl, z. B.
    s.zahl(a, "abs(" + det_ausdruck(A, "s") + ")", (2, 2), vor="Fläche = ")."""
    (a, b), (c, d) = matrix
    f = lambda v: "(%s)" % v if isinstance(v, str) else _zahl(float(v))
    return "(1 - {p} + {p}*{a})*(1 - {p} + {p}*{d}) - {p}^2*{b}*{c}".format(p=p, a=f(a), b=f(b), c=f(c), d=f(d))


class Szene:
    def __init__(self, name, margin=24, reihenfolge=None):
        """reihenfolge = was oben liegt: "anlegen" = Reihenfolge des Anlegens (was später angelegt wird, liegt oben,
        auch wenn es per Animation erscheint; Empfehlung für neue Szenen), "erscheinen" = ein Objekt mit
        Erscheinen-Animation legt sich über alles, was schon sichtbar ist. None (Standard) = "erscheinen", wie alle
        Szenen vor dem 10.11.2026; die Szenendatei bleibt dann ohne Eintrag (notizen/animationen.md §6)."""
        self.name = name
        self.objects, self.strings = [], {}
        self.n = 0
        self.margin = margin
        if reihenfolge not in (None, "anlegen", "erscheinen"):
            raise ValueError('reihenfolge ist "anlegen", "erscheinen" oder None')
        self.reihenfolge = reihenfolge

    # ---------------------------------------------------------------------------- intern
    def _add(self, typ, props, on=None):
        self.n += 1
        oid = "o%d" % self.n
        o = {"id": oid, "type": typ, "props": props}
        if on:
            o["on"] = on
        self.objects.append(o)
        return oid

    def tr(self, key, de, en, es, zh, fr=None, tr=None):
        """Text je Sprache; das Ergebnis steht im Label. "@{key}" darf auch Teil eines längeren Labels sein.
        fr und tr sind freiwillig: Fehlen sie, zeigt das Bild in diesen Sprachen den englischen Text
        (engine/scene_model._lookup), bis die Szene übersetzt ist. Ohne fr/tr bleibt die Szenendatei wie bisher."""
        self.strings[key] = {"de": de, "en": en, "es": es, "zh": zh}
        if fr is not None:
            self.strings[key]["fr"] = fr
        if tr is not None:
            self.strings[key]["tr"] = tr
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
    def kurve(self, on, f, x=None, farbe=BLAU, dicke=5, dash="", punkte=None):
        """Graph y = f(x); Ausdruckssprache des Editors (sin, exp, rect, tri, epsilon, si, where, floor, ...).
        Unter einem Parameter, der sich über die Zeit ändert (s.verstellen), wird die Kurve in jedem Bild an punkte
        gleichmäßig verteilten Stellen berechnet (Standard 121; etwa 10 je Schwingung genügen). x darf den Parameter
        nennen: x=(0, "t") lässt die Kurve mit t wachsen."""
        p = {"func": f, "color": farbe, "stroke_width": dicke, "dash": dash}
        if not x:                                      # ohne Angabe die ganze Achse (der Katalogwert wäre -10..10)
            ach = next((o for o in self.objects if o["id"] == on and o["type"] == "Axes"), None)
            x = ach["props"]["x_range"][:2] if ach else None
        if x:
            p["x_range"] = list(x)
        if punkte is not None:
            p["samples"] = int(punkte)
        return self._add("FunctionGraph", p, on)

    def daten(self, on, pts, farbe=BLAU, dicke=4, dash="", treppe="", marker=False, marker_r=0.06):
        """Kurve aus Punkten [(x, y)]; am Teilbild abgeschnitten."""
        txt = "\n".join("%s %s" % (_zahl(a), _zahl(b)) for a, b in pts)
        return self._add("DataCurve", {"data": txt, "clip": True, "step": treppe, "markers": marker, "marker_radius": marker_r,
                                       "color": farbe, "stroke_width": dicke, "dash": dash}, on)

    def flaeche(self, on, f, x0, x1, f2="", farbe=BLAU, deckung=0.3, punkte=120):
        """Fläche unter f (oder zwischen f und f2) von x0 bis x1; Grenzen dürfen einen Parameter nennen (x1="t": die
        Fläche wächst mit). punkte = Stützstellen; unter einem Parameter genügen etwa 32 (die Oberkante ist dann glatt
        durch die Stützstellen gelegt), das hält die animierte Datei klein."""
        return self._add("Area", {"func": f, "func2": f2, "x_min": x0, "x_max": x1, "samples": punkte, "color": farbe,
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
        """Strecke von a nach b; in 3D-Szenen dürfen a und b drei Koordinaten haben (x, y, z)."""
        return self._add("Line", {"start": [a[0], a[1], a[2] if len(a) > 2 else 0], "end": [b[0], b[1], b[2] if len(b) > 2 else 0],
                                  "color": farbe, "stroke_width": dicke, "dash": dash}, on)

    def weg(self, on, fx, fy, t0, t1, farbe=BLAU, dicke=4, pfeile="", n=161, dash="", spitze=None):
        """Parametrischer Weg; pfeile = "0.25;0.75": Richtungsmarken an diesen Stellen, "" = keine.
        spitze = Länge jeder Richtungsmarke in Szeneneinheiten (Standard 0.22; für kurze Wege kleiner, z. B. 0.11)."""
        p = {"fx": fx, "fy": fy, "t_min": t0, "t_max": t1, "samples": n, "show_arrow": bool(pfeile), "arrow_at": pfeile,
             "color": farbe, "stroke_width": dicke, "dash": dash}
        if spitze is not None:
            p["head_size"] = float(spitze)
        return self._add("ParametricCurve", p, on)

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
    def text(self, on, s, pos, groesse=TEXT, ausrichtung="left", farbe=SCHWARZ, schrift=None, roh=None):
        """Beschriftung. Ohne Zusatz Rich-Text: _x tief, ^x hoch, \\alpha, \\\\ Zeilenumbruch; $ { } verschwinden;
        Dezimalpunkte werden in de/es/fr/tr zum Komma.
        schrift="tt": Schreibmaschinenschrift (Terminalzeilen, Code, Werkzeugausgaben). Jedes Zeichen steht in einer
          Zelle fester Breite (tt_breite), mehrere Leerzeichen bleiben, Spalten stehen untereinander, ein chinesisches
          Zeichen belegt zwei Zellen; ' und ` bleiben gerade; Dezimalpunkte bleiben Punkte. Kostet nur die Zeichen
          selbst (keine Formel-Glyphen). Ohne roh=False ist tt immer roh.
        roh=True: der Text wörtlich (_ ^ \\ $ { } sind gewöhnliche Zeichen, Dateinamen wie einkauf_alt.txt oder C:\\
          ohne Maskierung; ein echter Zeilenumbruch "\\n" bricht die Zeile). @schluessel aus s.tr gilt weiter."""
        p = {"text": s, "position": [pos[0], pos[1], pos[2] if len(pos) > 2 else 0], "font_size": groesse, "align": ausrichtung,
             "color": farbe}
        if schrift not in (None, "sans", "tt", "mono"):
            raise ValueError('schrift ist None, "tt" oder "sans"')
        mono = schrift in ("tt", "mono")
        if mono:
            p["font"] = "mono"
        if roh or (roh is None and mono):
            p["raw"] = True
        return self._add("Text", p, on)

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

    def tabelle(self, zeilen, links_oben, zelle_b=1.2, zelle_h=0.6, zeilenkoepfe=(), spaltenkoepfe=(), klammern=False,
                groesse=ZAHL, farbe=SCHWARZ, markiert=(), on=None):
        """Tabelle oder Matrix (klammern=True): zeilen = [[a, b], [c, d]] (Text oder Zahl), links_oben = linke obere Ecke.
        markiert = [(z, s), ...] fest hinterlegte Zellen; einzelne Zellen kurz betonen: s.betonen(id, zelle=(z, s))."""
        zellen = ";".join(",".join(str(x) for x in z) for z in zeilen)
        return self._add("Table", {"cells": zellen, "row_labels": ",".join(zeilenkoepfe), "col_labels": ",".join(spaltenkoepfe),
                                   "highlight": ";".join("%d,%d" % rc for rc in markiert), "brackets": bool(klammern),
                                   "cell_w": zelle_b, "cell_h": zelle_h, "position": [links_oben[0], links_oben[1], 0],
                                   "font_size": groesse, "color": farbe, "fill_color": "#f5c542", "fill_opacity": 0.35,
                                   "stroke_width": 1.5}, on)

    def draht(self, *pkte, farbe=SCHWARZ, dicke=3):
        """Leitung durch die Punkte (mehrere gerade Stücke)."""
        ids = []
        for a, b in zip(pkte, pkte[1:]):
            ids.append(self._add("Line", {"start": [a[0], a[1], 0], "end": [b[0], b[1], 0], "color": farbe, "stroke_width": dicke, "dash": ""}))
        return ids

    # ---------------------------------------------------------------------------- Rechnungen: Σ, ∏, Skalarprodukt
    # Operationen des Editors. Im Artikelbild vollständig ausgerechnet, jeder Schritt eine Zeile, "=" unter "="
    # (Kopf = eingesetzt = Werte = Ergebnis); im Editor lassen sie sich Schritt für Schritt abspielen. Die Formeln
    # setzt MathJax beim Export (export_szenen.py). mitte = Mitte der Rechnung in Szeneneinheiten, auch in Szenen
    # mit Achsen (eine Rechnung sitzt nie auf Achsen). groesse = Schriftgröße der Formel in Szenenpixeln wie bei
    # Texten (FORMEL = 30 passt zu 24er bis 28er Beschriftung). breite = höchste Breite in Szeneneinheiten:
    # 7.0 füllt die Artikelspalte (548 px), längere Zeilen brechen vor einem "+" oder "=" um.
    # Zahlen mit Punkt schreiben (0.5): Die Sprache macht daraus 0,5 (de, es, fr, tr).
    def _operation(self, typ, props):
        """Eine Operation (computations) anlegen. model() bleibt unverändert: Mit der ersten Operation bekommt diese
        Szene ein eigenes model(), das die Operationen einträgt. Ergebnis: die id ("k1", "k2", …)."""
        ops = self.__dict__.setdefault("_ops", [])
        if not ops:
            basis = self.model                                 # die Methode der Klasse

            def model_mit_operationen():
                m = basis()
                m["model"]["computations"] = json.loads(json.dumps(self._ops))
                m["counters"]["nextCompId"] = len(self._ops) + 1
                return m
            self.model = model_mit_operationen
        cid = "k%d" % (len(ops) + 1)
        ops.append({"id": cid, "type": typ, "props": props})
        return cid

    @staticmethod
    def _rechnung(mitte, groesse, breite, summanden, alle_schritte, farbe, laufzeit, props):
        p = {"show_terms": summanden, "all_steps": alle_schritte, "max_width": breite, "font_size": groesse, "run_time": laufzeit,
             "size": 1.4, "position": [mitte[0], mitte[1], 0], "color": farbe, "var_color": ORANGE, "value_color": GRUEN,
             "end_color": BLAU, "pulse_color": "#66b3ff", "bound_color": ROT}
        p.update(props)
        return p

    @staticmethod
    def _index_exakt(p, index, exakt):
        """Laufindex und exakte Brüche nur eintragen, wenn sie vom Standard abweichen (alte Szenendateien bleiben gleich)."""
        if index != "i":
            if not (isinstance(index, str) and len(index) == 1 and index.isalpha() and index.isascii() and index != "e"):
                raise ValueError('index ist ein lateinischer Buchstabe außer e, z. B. "k"')
            p["index"] = index
        if exakt:
            p["exact"] = True
        return p

    def summe(self, term, von=1, bis="n", mitte=(0, 0), groesse=None, breite=7.0, summanden=3, alle_schritte=True,
              farbe=SCHWARZ, laufzeit=5, index="i", exakt=False, **props):
        """Σ_{i=von}^{bis} term. term in der Ausdruckssprache des Editors mit dem Laufindex i ("1/i^2", "(-1)^i/i",
        "2^(-i)"); bis = Zahl oder Buchstabe ("n": symbolisch, dann bleiben die Summanden Ausdrücke, ohne Summe).
        summanden: so viele Summanden vorn, dann ⋯ und die letzten zwei (sind es höchstens summanden + 2, alle).
        Brüche bleiben exakt (1/4), eine Summe mit Bruch bekommt zusätzlich ihren Dezimalwert.
        index = anderer Laufindex (ein Buchstabe, z. B. "k"); term schreibt dann k statt i.
        exakt=True: exakt mit ganzen Zahlen rechnen, Brüche mit beliebig großem Nenner (3/131072, Summe 13107/131072);
          ohne exakt werden Brüche mit Nenner über 10000 als Dezimalzahl gezeigt.
        **props: weitere Props der Editor-Operation (z. B. value_color="#…")."""
        p = self._index_exakt({"sum_mode": "number", "term": term, "from": von, "to": str(bis)}, index, exakt)
        p.update(self._rechnung(mitte, FORMEL if groesse is None else groesse, breite, summanden, alle_schritte, farbe, laufzeit, props))
        return self._operation("Summation", p)

    def produkt(self, term, von=1, bis="n", mitte=(0, 0), groesse=None, breite=7.0, summanden=3, alle_schritte=True,
                farbe=SCHWARZ, laufzeit=5, index="i", exakt=False, **props):
        """∏_{i=von}^{bis} term, sonst wie summe() (Faktoren statt Summanden, verbunden mit ·; index, exakt ebenso)."""
        p = self._index_exakt({"sum_mode": "number", "term": term, "from": von, "to": str(bis)}, index, exakt)
        p.update(self._rechnung(mitte, FORMEL if groesse is None else groesse, breite, summanden, alle_schritte, farbe, laufzeit, props))
        return self._operation("BigProduct", p)

    def skalarprodukt(self, u, v, namen=("w", "x"), index="j", obere="", mitte=(0, 0), groesse=None, breite=7.0, summanden=3,
                      vektoren=True, alle_schritte=True, farbe=SCHWARZ, laufzeit=6, darstellung="rechnung", **props):
        """uᵀv = Σ_j u_j v_j zweier Zahlenlisten gleicher Länge, z. B. u=[3, 10, -4], v=[120, 3, 25].
        namen = (Name von u, Name von v), fett gesetzt ("w", "x"; griechisch als "theta"; mit Index "q_1" oder
        r"\\mathbf q_1": Kopf q₁ᵀx, Komponenten q_{1,j}); index = Laufindex; obere = obere Grenze am Σ ("" = die Länge,
        oder z. B. "d"). Dezimalzahlen bleiben exakt (0.5·0.4 = 0.2), negative Zahlen stehen in Klammern.
        darstellung (das Bild ist der Endzustand, im Editor läuft es Schritt für Schritt ab):
          "rechnung"    wᵀx = Σ w_j x_j = w_1 x_1 + … = 3·120 + … = 360 + … = Summe; vektoren=True zeigt beide
                        Vektoren als Spalten darüber (bei langen Vektoren ⋮ an der Stelle des ⋯)
          "komponenten" beide Vektoren als Spalten nebeneinander, je Zeile · dazwischen und = Produkt dahinter,
                        darunter wᵀx = 360 + … = Summe
          "matrix"      Zeilenvektor wᵀ, x daruntergelegt (x_j unter w_j, · dazwischen), dahinter = 360 + … = Summe"""
        if len(u) != len(v) or not len(u):
            raise ValueError("skalarprodukt: u und v brauchen gleich viele Zahlen (mindestens eine)")
        if darstellung not in ("rechnung", "komponenten", "matrix"):
            raise ValueError('skalarprodukt: darstellung ist "rechnung", "komponenten" oder "matrix"')

        def liste(xs):
            def z(x):
                if isinstance(x, str):
                    return x.strip()
                s = "%.12g" % x
                return format(x, "f").rstrip("0").rstrip(".") if "e" in s else s
            return ", ".join(z(x) for x in xs)
        p = {"display": darstellung, "u": liste(u), "v": liste(v), "u_name": namen[0], "v_name": namen[1], "index": index,
             "upper": str(obere), "show_vectors": bool(vektoren)}
        p.update(self._rechnung(mitte, FORMEL if groesse is None else groesse, breite, summanden, alle_schritte, farbe, laufzeit, props))
        return self._operation("DotProduct", p)

    def formel(self, tex, mitte=(0, 0), hoehe=0.25, farbe=SCHWARZ, zeilenweise=False, dauer=None):
        """Eine LaTeX-Formel als Bild (MathTex, gesetzt von MathJax), z. B. s.formel(r"\\hat y = \\sigma(\\mathbf w^\\top \\mathbf x)").
        hoehe = Höhe der GANZEN Formel in Szeneneinheiten (eine Zeile ohne Bruch: 0.25 passt zu FORMEL = 30, mit
        Bruch oder Σ entsprechend mehr). mitte in Szeneneinheiten, auch in Szenen mit Achsen.
        Dezimalzahlen mit Punkt schreiben (0.5): Die Sprache macht daraus 0,5 (de, es, fr, tr); Längen wie 0.5em bleiben.
        zeilenweise=True: Auf der Website erscheint die Formel Zeile für Zeile (Rechnung in aligned: ein Rechenschritt
        je Zeile, Sprungmarke je Zeile); dauer = Gesamtdauer (Standard 1,2 s je Zeile). Das Bild bleibt dasselbe."""
        oid = self._add("MathTex", {"tex": tex, "height": hoehe, "position": [mitte[0], mitte[1], 0], "color": farbe})
        if zeilenweise:
            zeilen = tex.count("\\\\") + 1 - sum(tex.count("\\begin{%s}" % u) for u in ("pmatrix", "bmatrix", "vmatrix", "matrix", "cases", "array"))
            self.animation("FadeIn", oid, dauer if dauer is not None else 1.2 * max(1, zeilen), lines=True)
        return oid

    # ---------------------------------------------------------------------------- Zeitachse (Animationen)
    # Jede Abbildung darf eine Zeitachse haben: Auf der Website läuft sie mit Start/Stopp-Knopf ab
    # (export_szenen.py --animiert), das statische Bild und das PDF zeigen ihr Endbild. Jeder Aufruf hängt einen neuen
    # Schritt an; Aufrufe in "with s.gleichzeitig():" teilen sich einen Schritt. Ziele sind die ids der Objekte
    # (Rückgabewerte von s.kurve, s.box, ...). Objekte mit einer Erscheinen-Animation sind vorher unsichtbar.
    # Anleitung: notizen/animationen.md.
    def animation(self, art, ziel, dauer=1.0, **werte):
        """Eine Animation des Editors (art = Create, Write, FadeIn, GrowFromCenter, FadeOut, Shift, MoveTo, Rotate,
        Scale, Indicate, Transform, ReplacementTransform, TransformMatchingTex, MoveAlongPath, ChangeValue, ApplyMatrix,
        ApplyFunction, MoveCamera) mit ihren Werten (vector, point, angle in Grad, factor, around, to, row, col, cell;
        ChangeValue: value, rate; ApplyMatrix: matrix, objects, path, rate; ApplyFunction: func, objects, rate;
        MoveCamera (ziel None): theta, phi, turn in Grad, zoom, center, rate).
        Ergebnis: die id der Animation."""
        anims = self.__dict__.setdefault("_anims", [])
        if not anims:
            basis = self.model                                 # wie _operation: model() trägt die Zeitachse ein

            def model_mit_zeitachse():
                m = basis()
                m["model"]["animations"] = json.loads(json.dumps(self._anims))
                m["counters"]["nextAnimId"] = len(self._anims) + 1
                return m
            self.model = model_mit_zeitachse
        gruppe = self.__dict__.get("_gruppe")
        if gruppe is not None:                                 # in gleichzeitig(): ein gemeinsamer Schritt
            if gruppe[0] is None:
                gruppe[0] = self._schritt_neu()
            schritt = gruppe[0]
        else:
            schritt = self._schritt_neu()
        a = {"id": "a%d" % (len(anims) + 1), "type": art, "target": ziel, "run_time": float(dauer), "step": schritt}
        a.update({k: v for k, v in werte.items() if v is not None})
        anims.append(a)
        return a["id"]

    def _schritt_neu(self):
        anims = self.__dict__.get("_anims") or []
        return (max(a["step"] for a in anims) + 1) if anims else 0

    class _Gleichzeitig:
        """Ein gemeinsamer Schritt. Verschachtelt (einblenden/ausblenden mit mehreren Zielen in gleichzeitig()) bleibt
        es beim äußeren Schritt; bis 10.11.2026 begann das innere einen neuen Schritt und beendete den äußeren."""
        def __init__(self, s):
            self.s = s
            self.innen = False

        def __enter__(self):
            if self.s.__dict__.get("_gruppe") is not None:
                self.innen = True
            else:
                self.s._gruppe = [None]
            return self.s

        def __exit__(self, *exc):
            if not self.innen:
                self.s._gruppe = None
            return False

    def gleichzeitig(self):
        """with s.gleichzeitig(): s.zeichnen(k); s.einblenden(t)  -> beide Animationen laufen zusammen."""
        return Szene._Gleichzeitig(self)

    # Erscheinen
    def zeichnen(self, ziel, dauer=1.5):
        """Linie, Kurve, Pfeil, Umriss zeichnet sich (Create)."""
        return self.animation("Create", ziel, dauer)

    def schreiben(self, ziel, dauer=1.0):
        """Text oder Formel erscheint Strich für Strich (Write)."""
        return self.animation("Write", ziel, dauer)

    def einblenden(self, *ziele, dauer=0.6, nacheinander=False):
        """Ein oder mehrere Objekte blenden ein (FadeIn); mehrere zusammen, mit nacheinander=True eines nach dem anderen."""
        if nacheinander or len(ziele) == 1:
            return [self.animation("FadeIn", z, dauer) for z in ziele][-1]
        with self.gleichzeitig():
            for z in ziele:
                self.animation("FadeIn", z, dauer)

    def wachsen(self, ziel, dauer=0.8):
        """Wächst aus seiner Mitte (GrowFromCenter), z. B. ein Punkt oder Kasten."""
        return self.animation("GrowFromCenter", ziel, dauer)

    # Verschwinden (L1)
    def ausblenden(self, *ziele, dauer=0.6):
        """Objekte blenden aus (FadeOut); sie fehlen dann im Endbild und im PDF."""
        with self.gleichzeitig():
            for z in ziele:
                self.animation("FadeOut", z, dauer)

    # Bewegen
    def verschieben(self, ziel, dx, dy, dauer=1.0):
        """Um (dx, dy) Szeneneinheiten verschieben (Shift); im Endbild steht das Objekt am Ziel."""
        return self.animation("Shift", ziel, dauer, vector=[dx, dy, 0])

    def bewegen_zu(self, ziel, x, y, dauer=1.0):
        """Mitte des Objekts nach (x, y) (MoveTo, Szeneneinheiten)."""
        return self.animation("MoveTo", ziel, dauer, point=[x, y, 0])

    def drehen(self, ziel, grad, um=None, dauer=1.0):
        """Um grad Grad drehen (gegen den Uhrzeiger), um die eigene Mitte oder um den Punkt um=(x, y) (Zeiger)."""
        return self.animation("Rotate", ziel, dauer, angle=grad, around=[um[0], um[1], 0] if um else None)

    def skalieren(self, ziel, faktor, um=None, dauer=1.0):
        return self.animation("Scale", ziel, dauer, factor=faktor, around=[um[0], um[1], 0] if um else None)

    def entlang(self, ziel, weg, dauer=2.0):
        """Objekt läuft auf dem Weg (id einer Kurve) entlang (MoveAlongPath)."""
        return self.animation("MoveAlongPath", ziel, dauer, path=weg)

    # Betonen
    def betonen(self, ziel, dauer=0.9, zeile=None, spalte=None, zelle=None):
        """Kurz hervorheben (Indicate). Bei einer Tabelle (s.tabelle) nur eine Zeile, Spalte oder Zelle (zeile, spalte)
        ab 0 gezählt, ohne Kopfzeile/-spalte (L9)."""
        return self.animation("Indicate", ziel, dauer, row=zeile, col=spalte, cell=list(zelle) if zelle else None)

    def pause(self, dauer=0.8):
        """Haltepunkt: nichts bewegt sich (Schritt „Wait“), z. B. zwischen zwei Rechenschritten."""
        return self.animation("Wait", None, dauer)

    # Umformen (L2)
    def umformen(self, ziel, zu, dauer=1.2, passend=False):
        """ziel nimmt die Form von zu an (Transform). zu ist nur Vorlage und wird nie selbst gezeichnet; im Endbild
        steht ziel in der Form von zu. passend=True bei zwei Formeln: gleiche Zeichen wandern an ihren neuen Platz,
        die übrigen blenden aus bzw. ein (TransformMatchingTex).
        Zwei Texte (s.text): Inhalt, Farbe, Größe, Lage und Schrift gehen auf die Vorlage über; der alte Text blendet in
        der ersten Hälfte aus, der neue in der zweiten ein. Im Endbild steht nur der neue Text (bequemer: ersetzen)."""
        return self.animation("TransformMatchingTex" if passend else "Transform", ziel, dauer, to=zu)

    def ersetzen(self, ziel, text, farbe=None, dauer=0.8, groesse=None):
        """Inhalt eines s.text ändern (z. B. ein Zähler, eine Datei bekommt einen neuen Namen): legt die Vorlage selbst an
        (gleiche Lage, Ausrichtung, Schrift; neuer Text, wahlweise neue Farbe/Größe) und formt um. Im Endbild, in .svg
        und PDF steht nur der neue Text, kein unsichtbarer Rest. Ergebnis: die id der Animation."""
        o = next((x for x in self.objects if x["id"] == ziel), None)
        if o is None or o["type"] != "Text":
            raise ValueError("ersetzen: %s ist kein s.text" % ziel)
        p = json.loads(json.dumps(o["props"]))
        p["text"] = text
        if farbe is not None:
            p["color"] = farbe
        if groesse is not None:
            p["font_size"] = groesse
        vorlage = self._add("Text", p, o.get("on"))
        return self.umformen(ziel, vorlage, dauer)

    # ---------------------------------------------------------------------------- Parameter über die Zeit (L3)
    # Ein Parameter ist eine Zahl der Szene mit Namen. Jeder Ausdruck darf ihn nennen: Funktionen
    # (s.kurve(a, "sin(x - c*t)")), Grenzen und Koordinaten (s.flaeche(a, f, 0, "t"), s.punkt(a, "t", "sin(t)"),
    # s.linie(a, ("t", -1), ("t", 1))), Zahlenanzeigen (s.zahl). s.verstellen ändert ihn über die Zeit, und alles, was
    # ihn nennt, läuft in jedem Bild mit. Anleitung: notizen/animationen.md §8.
    def parameter(self, name, wert, von=None, bis=None, schritt=None, ganzzahlig=False):
        """Parameter name mit Startwert wert (im Editor: Objekt „Parameter“ mit Regler von..bis).
        name: Buchstaben, Ziffern, _ (nicht x, y, e, pi, i, j, theta). "t" ist erlaubt und ersetzt dann in allen
          Ausdrücken der Szene die Variable t: Kurven in x schreiben (sin(x - c*t)); Wege (s.weg) behalten ihr eigenes t.
        ganzzahlig=True: nur ganze Werte (n = 1, 2, 3 …); s.verstellen springt dann von Zahl zu Zahl, jede gleich lang.
        von, bis: Bereich des Reglers (Standard: so, dass Startwert und alle Ziele aus s.verstellen hineinpassen).
        Ergebnis: die id (s.verstellen nimmt id oder Namen)."""
        if not (isinstance(name, str) and name.isidentifier() and name.isascii() and name[0].isalpha()):
            raise ValueError("parameter: name aus Buchstaben, Ziffern und _, beginnend mit einem Buchstaben")
        if name in ("x", "y", "e", "pi", "i", "j", "theta"):
            raise ValueError('parameter: "%s" ist schon vergeben (Variable oder Konstante)' % name)
        ids = self.__dict__.setdefault("_params", {})
        if name in ids:
            raise ValueError("parameter: %s gibt es schon" % name)
        w = float(round(wert)) if ganzzahlig else float(wert)
        p = {"name": name, "value": w, "min": float(von) if von is not None else min(0.0, w),
             "max": float(bis) if bis is not None else max(1.0, w),
             "step": float(schritt) if schritt is not None else (1.0 if ganzzahlig else 0.01)}
        if ganzzahlig:
            p["integer"] = True
        oid = self._add("Parameter", p)
        ids[name] = (oid, von is None, bis is None)
        return oid

    def verstellen(self, parameter, ziel, dauer=2.0, rate="glatt"):
        """Parameter (Name oder id) in dauer Sekunden vom jetzigen Wert auf ziel (Zahl oder Ausdruck wie "2*pi")
        bringen (Animation ChangeValue). rate: "glatt" (langsam an und aus, Standard) oder "linear" (gleichmäßig:
        laufende Welle, Uhrzeiger, Zeitmarker). Mehrere Parameter zugleich: in "with s.gleichzeitig():". Das Endbild
        (statisches Bild, PDF) zeigt alles beim letzten Zielwert. Ergebnis: die id der Animation."""
        ids = self.__dict__.get("_params") or {}
        if parameter in ids:
            oid, frei_von, frei_bis = ids[parameter]
        else:
            hit = [v for v in ids.values() if v[0] == parameter]
            if not hit:
                raise ValueError("verstellen: %s ist kein Parameter dieser Szene (s.parameter)" % parameter)
            oid, frei_von, frei_bis = hit[0]
        if rate not in ("glatt", "linear"):
            raise ValueError('verstellen: rate ist "glatt" oder "linear"')
        o = next(x for x in self.objects if x["id"] == oid)
        if isinstance(ziel, (int, float)):             # den Regler im Editor so weit machen, dass das Ziel hineinpasst
            z = float(round(ziel)) if o["props"].get("integer") else float(ziel)
            if frei_von and z < o["props"]["min"]:
                o["props"]["min"] = z
            if frei_bis and z > o["props"]["max"]:
                o["props"]["max"] = z
            ziel = z
        else:
            ziel = str(ziel)
        werte = {"value": ziel}
        if rate == "linear":
            werte["rate"] = "linear"
        return self.animation("ChangeValue", oid, dauer, **werte)

    def zahl(self, on, ausdruck, pos, stellen=2, vor="", nach="", groesse=TEXT, ausrichtung="left", farbe=SCHWARZ):
        """Zahlenanzeige (DecimalNumber): der Wert von ausdruck (ein Parameter oder etwas daraus: "t", "A*exp(-t/tau)")
        mit stellen Nachkommastellen; vor/nach stehen davor/dahinter ("t = ", " s"; Rich-Text und @schluessel wie bei
        s.text). Dezimalzeichen und Minus folgen der Sprache (1,25 in de/es/fr/tr, 1.25 in en/zh). ausrichtung="left"
        hält den Anfang fest, während die Zahl breiter oder schmaler wird."""
        return self._add("DecimalNumber", {"value": str(ausdruck), "decimals": int(stellen), "prefix": vor, "suffix": nach,
                                           "position": [pos[0], pos[1], 0], "font_size": groesse, "align": ausrichtung,
                                           "color": farbe}, on)

    def marke(self, on, x, f="", f2="", y=None, label="", hilfslinien=True, farbe=SCHWARZ, r=0.08, groesse=TEXT,
              label_pos="ne"):
        """Punkt mit gestrichelten Hilfslinien zu beiden Achsen (Marker). x: Zahl oder Ausdruck ("t"). Mit f sitzt der
        Punkt auf der Kurve y = f(x), mit f und f2 im Schnittpunkt nahe x (Arbeitspunkt); ohne f gilt y (Zahl oder
        Ausdruck). label_pos: ne, nw, se, sw, n, s, e, w."""
        return self._add("Marker", {"point": [0, 0, 0], "x_expr": str(x), "func": f, "func2": f2,
                                    "y_expr": "" if y is None else str(y), "label": label, "label_pos": label_pos,
                                    "show_guides": bool(hilfslinien), "guide_dash": "5,5", "radius": r, "font_size": groesse,
                                    "color": farbe}, on)

    def tangente(self, on, f, x0, laenge=1.0, punkt=True, farbe=SCHWARZ, dicke=3, dash=""):
        """Tangente an y = f(x) im Punkt x0 (Zahl oder Ausdruck: "t" läuft mit); laenge = halbe Länge in x-Einheiten."""
        return self._add("TangentLine", {"func": f, "x0": x0, "secant": False, "half_len": laenge, "show_point": bool(punkt),
                                         "show_slope": False, "triangle_dx": 0, "color": farbe, "stroke_width": dicke,
                                         "dash": dash}, on)

    # ---------------------------------------------------------------------------- Ebene abbilden (L5)
    # Eine 2x2-Matrix verformt die Ebene über die Zeit: das Koordinatengitter (s.gitter) und alles, was mitgenommen
    # wird (Punkte, Pfeile, Vielecke, Kreise, Kurven, Texte). Jeder Punkt p läuft nach A p, im Endbild steht das Bild.
    # Mehrere Abbildungen hintereinander starten jeweils vom verformten Zustand. Anleitung: notizen/animationen.md §9.
    def gitter(self, on, schritt=1.0, schritt_y=None, farbe="#8fa6c8", dicke=2, deckung=1.0, rand=1.0, punkte=2,
               achsen_dicke=0, zuschneiden=True, x=None, y=None, dash=""):
        """Koordinatengitter (Grid) im Fenster der Achsen on (oder x=(von, bis), y=(von, bis)): Linien x = k*schritt
        und y = k*schritt_y. rand: wie viele Fensterbreiten die Linien über das Fenster hinausreichen (damit eine
        Scherung Linien von außen hereinholt); zuschneiden=False zeigt die verformten Linien ganz. punkte > 2 für
        gekrümmte Bilder (s.abbilden_funktion, etwa 40). achsen_dicke > 0: die Linien x = 0 und y = 0 so dick.
        Ein zweites Gitter, das nicht in s.abbilden steht, bleibt als „Geistergitter“ stehen (blass: deckung=0.35)."""
        p = {"x_step": schritt, "y_step": schritt if schritt_y is None else schritt_y, "extend": rand, "samples": int(punkte),
             "clip": bool(zuschneiden), "axis_width": achsen_dicke, "color": farbe, "stroke_width": dicke,
             "stroke_opacity": deckung, "dash": dash}
        if x is not None:
            p["x_range"] = list(x)
        if y is not None:
            p["y_range"] = list(y)
        return self._add("Grid", p, on)

    def vektor(self, on, ende, start=(0, 0), label="", farbe=SCHWARZ, dicke=4, spitze=0.22, groesse=TEXT,
               label_seite="left", label_am_ende=True):
        """Pfeil von start nach ende in Datenkoordinaten (Basisvektor e_1, Bildvektor A e_1, ...); die Beschriftung
        steht an der Spitze (label_am_ende=False: an der Mitte). In s.abbilden behält er seine Spitze und die
        Beschriftung bleibt aufrecht."""
        return self.pfeil(start, ende, label=label, farbe=farbe, dicke=dicke, spitze=spitze, groesse=groesse, on=on,
                          label_seite=label_seite, at="end" if label_am_ende else "mid")

    def vieleck(self, on, punkte, farbe=BLAU, deckung=0.25, dicke=3, randfarbe=None, dash=""):
        """Gefülltes Vieleck durch die Ecken punkte [(x, y), ...] in Datenkoordinaten, z. B. das Einheitsquadrat. In
        3D-Szenen (x, y, z); Koordinaten dürfen Ausdrücke mit Parametern sein ("a + 0.3")."""
        z = lambda v: v if isinstance(v, str) else float(v)
        return self._add("Polygon", {"vertices": [[z(p[0]), z(p[1]), z(p[2]) if len(p) > 2 else 0.0] for p in punkte],
                                     "color": randfarbe or farbe, "fill_color": farbe, "fill_opacity": deckung,
                                     "stroke_width": dicke, "dash": dash}, on)

    def _abbildung(self, art, werte, objekte, dauer, rate, parameter):
        ids = [o for o in objekte]
        if not ids:
            raise ValueError("abbilden: objekte nennt kein Objekt")
        bekannt = {o["id"] for o in self.objects}
        fremd = [o for o in ids if o not in bekannt]
        if fremd:
            raise ValueError("abbilden: unbekannte Objekte %s" % ", ".join(fremd))
        if rate not in ("glatt", "linear"):
            raise ValueError('abbilden: rate ist "glatt" oder "linear"')
        werte = dict(werte, objects=ids[1:])
        if rate == "linear":
            werte["rate"] = "linear"
        if parameter is None:
            return self.animation(art, ids[0], dauer, **werte)
        if parameter not in (self.__dict__.get("_params") or {}):
            self.parameter(parameter, 0, von=0, bis=1)
        if self.__dict__.get("_gruppe") is not None:            # schon in gleichzeitig(): derselbe Schritt
            aid = self.animation(art, ids[0], dauer, **werte)
            self.verstellen(parameter, 1, dauer=dauer, rate=rate)
            return aid
        with self.gleichzeitig():
            aid = self.animation(art, ids[0], dauer, **werte)
            self.verstellen(parameter, 1, dauer=dauer, rate=rate)
        return aid

    def abbilden(self, matrix, objekte, dauer=2.0, weg="gerade", rate="glatt", parameter=None):
        """Die Matrix [[a, b], [c, d]] (Zahlen oder Ausdrücke wie "cos(pi/6)") auf die Ebene anwenden (ApplyMatrix):
        objekte = ids (Gitter, Vektoren, Vielecke, Punkte, Kreise, Kurven, Texte) in den Datenkoordinaten ihrer Achsen.
        weg="gerade": jeder Punkt läuft geradlinig nach A p (wie Manim); weg="drehung": Drehanteil als Drehung, der
          Rest geradlinig (A = R·P, nur für det A > 0; eine Drehmatrix dreht dann, statt zwischendurch zu schrumpfen).
        parameter="s": dazu ein Parameter s, der im selben Schritt gleich schnell von 0 auf 1 läuft; s.zahl kann dann
          einen Wert der Zwischenmatrix zeigen, z. B. s.zahl(a, det_ausdruck(A, "s"), ...). Je Abbildung ein eigener Name.
        Ergebnis: die id der Animation."""
        try:
            a, b = matrix[0][0], matrix[0][1]
            c, d = matrix[1][0], matrix[1][1]
        except (TypeError, IndexError):
            raise ValueError("abbilden: matrix hat die Form [[a, b], [c, d]]")
        if weg not in ("gerade", "drehung"):
            raise ValueError('abbilden: weg ist "gerade" oder "drehung"')
        if weg == "drehung":
            try:
                det = float(a) * float(d) - float(b) * float(c)
            except (TypeError, ValueError):
                det = None
            if det is not None and det <= 0:
                raise ValueError("abbilden: weg=\"drehung\" braucht det A > 0 (Spiegelung oder plattdrücken: weg=\"gerade\")")
        m = [[a, b], [c, d]]
        werte = {"matrix": m}
        if weg == "drehung":
            werte["path"] = "rotate"
        return self._abbildung("ApplyMatrix", werte, objekte, dauer, rate, parameter)

    def abbilden_funktion(self, fx, fy, objekte, dauer=2.0, rate="glatt", parameter=None):
        """Nichtlineare Abbildung (ApplyFunction): jeder Punkt (x, y) läuft geradlinig nach (fx(x, y), fy(x, y)),
        z. B. Polarkoordinaten fx="x*cos(y)", fy="x*sin(y)" (Gitter wird zu Kreisen und Strahlen). Das Gitter dafür
        mit punkte=40 anlegen, damit seine Linien sich biegen können. Sonst wie abbilden."""
        return self._abbildung("ApplyFunction", {"func": [str(fx), str(fy)]}, objekte, dauer, rate, parameter)

    # ---------------------------------------------------------------------------- Kamera (L4)
    # Die Kamera einer 3D-Szene steht in theta (Drehung um die senkrechte z-Achse), phi (Höhe über der Grundebene),
    # beide in Grad, zoom (> 1 größer) und blickpunkt (der Weltpunkt in der Bildmitte). s.kamera fährt sie über die
    # Zeit, gleichzeitig mit anderen Animationen in "with s.gleichzeitig():". Anleitung: notizen/animationen.md §10.
    def achsen3d(self, x=(-2, 2), y=(-2, 2), z=(0, 2), xl="x", yl="y", zl="z", zahlen=False, pfeile=True, mitte=(0, 0, 0)):
        """Räumliche Achsen (x, y waagrecht, z nach oben), Länge = Spanne: Datenkoordinaten = Weltkoordinaten (bei
        mitte = Ursprung; z zählt ab 0). Für Flächen (s.flaeche3d), Kugeln (s.kugel), Strecken und Texte mit z."""
        return self._add("Axes", {"x_range": list(x), "y_range": list(y), "z_range": list(z), "x_length": x[1] - x[0],
                                  "y_length": y[1] - y[0], "z_length": z[1] - z[0], "origin": list(mitte), "x_label": xl,
                                  "y_label": yl, "z_label": zl, "number_size": ZAHL, "label_size": ACHSTITEL, "axis_width": 3,
                                  "x_numbers": bool(zahlen), "y_numbers": bool(zahlen), "show_ticks": bool(zahlen),
                                  "show_numbers": bool(zahlen), "arrows": bool(pfeile), "arrow_size": 0.16,
                                  "minor_ticks": False, "title": ""})

    def zuoberst(self, *ziele, stufe=1):
        """3D: diese Objekte nach allen Objekten einer niedrigeren Stufe zeichnen, unabhängig von der Tiefe (prop layer).
        Für etwas, das vor einer Fläche liegt, deren Facetten es sonst stückweise verdecken (Tangentialebene über einer
        gewölbten Fläche, Punkt und Beschriftung darauf). Nur, wenn es aus jeder gezeigten Richtung davor liegt."""
        for z in ziele:
            o = next((x for x in self.objects if x["id"] == z), None)
            if o is None:
                raise ValueError("zuoberst: %s gibt es nicht" % z)
            o["props"]["layer"] = int(stufe)

    def flaeche3d(self, on, f, farbe=BLAU, deckung=0.85, aufloesung=20, gitter=1):
        """Fläche z = f(x, y) über dem Bereich der Achsen on (ein Ausdruck in x und y); aufloesung = Zellen je Achse
        (klein halten: jede Zelle ist ein Element der animierten Datei)."""
        return self._add("FunctionGraph", {"func": f, "color": farbe, "fill_opacity": deckung, "res_max": int(aufloesung),
                                           "stroke_width": gitter}, on)

    def kugel(self, on, punkt, r=0.2, farbe=BLAU, glanz=True, rand=1.5):
        """Kugel als Scheibe, die immer zur Kamera zeigt, mit Lichtfleck (Ball): Atom, Punkt im Raum. punkt (x, y, z)
        in Datenkoordinaten (Ausdrücke mit Parametern erlaubt), r in Szeneneinheiten. Ein Pfad statt eines Netzes."""
        return self._add("Ball", {"center": [punkt[0], punkt[1], punkt[2] if len(punkt) > 2 else 0], "radius": r,
                                  "color": farbe, "fill_opacity": 1.0, "stroke_width": rand, "highlight": bool(glanz)}, on)

    def kamera_start(self, theta=35.0, phi=20.0, zoom=1.0, blickpunkt=None, raum=True):
        """Ansicht am Anfang (Grad). raum=True: 3D-Szene (z zeigt nach oben); raum=False: 2D mit zoom/blickpunkt."""
        import math
        k = {"mode": "3d" if raum else "2d", "theta": round(math.radians(theta), 6), "phi": round(math.radians(phi), 6),
             "zoom": float(zoom)}
        if blickpunkt is not None:
            k["center"] = [float(v) for v in (list(blickpunkt) + [0, 0, 0])[:3]]
        self._kamera = k
        return k

    def kamera(self, theta=None, phi=None, zoom=None, blickpunkt=None, drehen=None, dauer=2.0, rate="glatt"):
        """Kamerafahrt (MoveCamera) in dauer Sekunden: auf theta/phi (Grad), zoom und blickpunkt (x, y, z), was
        fehlt, bleibt. drehen = Grad, die zu theta hinzukommen (360 = einmal um die Szene). rate "glatt" oder
        "linear". Statisches Bild und PDF zeigen die Endstellung. Ergebnis: die id der Animation."""
        if rate not in ("glatt", "linear"):
            raise ValueError('kamera: rate ist "glatt" oder "linear"')
        werte = {}
        for k, v in (("theta", theta), ("phi", phi), ("turn", drehen)):
            if v is not None:
                werte[k] = v if isinstance(v, str) else float(v)
        if zoom is not None:
            werte["zoom"] = float(zoom)
        if blickpunkt is not None:
            werte["center"] = [float(v) for v in (list(blickpunkt) + [0, 0, 0])[:3]]
        if not werte:
            raise ValueError("kamera: nichts zu bewegen (theta, phi, zoom, blickpunkt oder drehen angeben)")
        if rate == "linear":
            werte["rate"] = "linear"
        return self.animation("MoveCamera", None, dauer, **werte)

    def kamera_kreisen(self, grad=360.0, dauer=6.0):
        """Gleichmäßige Drehung um die senkrechte Achse (wie Manims ambient rotation) über dauer Sekunden."""
        return self.kamera(drehen=grad, dauer=dauer, rate="linear")

    # ---------------------------------------------------------------------------- Ablegen
    def model(self):
        m = {"v": 1, "counters": {"nextId": self.n + 1, "nextAnimId": 1, "nextCompId": 1},
             "model": {"objects": self.objects, "animations": [], "computations": [],
                       "background": {"color": "#ffffff", "transparent": False, "shadows": True, "axes_on_top": False},
                       "playMode": "sequential", "angleUnit": "rad", "domain": "real",
                       "camera": dict(self.__dict__.get("_kamera") or {"mode": "2d", "theta": 0.6, "phi": 1.0, "zoom": 1.0}),
                       "export": {"mode": "content", "margin": self.margin, "scale": 0.55, "frame": None},
                       "lang": "de", "strings": self.strings}}
        if getattr(self, "reihenfolge", None):                 # nur wenn gewählt: ältere Szenendateien bleiben gleich
            m["model"]["drawOrder"] = "creation" if self.reihenfolge == "anlegen" else "appearance"
        return m

    def speichern(self):
        p = SZENEN / (self.name + ".json")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.model(), ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
        return p
