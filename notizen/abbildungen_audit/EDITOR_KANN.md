# Was der Editor animieren kann (Stand 09.11.2026)

Quellen: `web/editor.js` (CATALOG, COMPUTATIONS, ANIM_GROUPS), `web/engine/scene_model.py` (OBJECT_TYPES, ANIMATION_TYPES),
`web/engine/animation.py`, `tools/szenen_lib.py`, `web/ENGINE_CONTRACT.md`.

## Bestand
- 703 Szenen-Dateien unter `web/szenen/`. **Keine einzige hat eine Zeitachse** (`animations` überall leer).
- Nur 10 Szenen haben eine Operation (Rechenbild): ml 8, prog 2 (15× Skalarprodukt, 3× Σ, 1× ∏).
- Artikel zeigen jede Szene als **statisches SVG** (Endzustand). Abspielen geht nur im Editor („Szene im Editor öffnen“).

## Objekte (alle statisch zeichenbar, alle als Ziel einer Animation nutzbar)
- **Geometrie:** Circle, Dot, Line, Rectangle, Square, Ellipse, Polygon/Triangle, Shape (freies Polygon), Vector (2D/3D).
- **Achsen & Kurven:** Axes (linear/log, Gitter, Achsenkreuz), FunctionGraph (auch Fläche z = f(x,y) in 3D), Area (unter/zwischen
  Kurven), TangentLine (Tangente oder Sekante mit Steigungsdreieck), CurveFamily (Kurvenschar, verblassend, mit Grenzkurve),
  ParametricCurve (Richtungspfeile, Punkt, Tangente/Normale), PolarCurve, DataCurve (Messpunkte, Treppe), Band, Stem (diskrete
  Werte, Dirac-Pfeile, Balken), PointCloud (Zufallspunkte, Verteilungen), NumberLine, Legend, Riemann (Mittelpunkt-Rechtecke).
- **Signale:** ε(t), rect, tri, si, sinc, ramp als Funktionen in jeder Formel.
- **Felder:** VectorField (Presets oder fx, fy; Farbe nach Betrag), ScalarField (Heatmap, Höhenlinien, Gradientenpfeile).
- **3D:** Sphere, Box, Cube, Pyramid; Kamera 2D/3D (Winkel, Zoom) als feste Einstellung.
- **Text:** Text, MathTex (LaTeX über MathJax), TextBox (Kästen für Blockbilder, Ablauf- und Datenflussbilder).
- **Annotation:** Marker (Punkt mit Hilfslinien, auch auf einer Kurve), Measure (Bemaßung), LabeledArrow (mit Knick,
  Doppelpfeil), LoopArrow, Brace, Mark (Haken/Kreuz), Table (Zellen, Hervorhebung, Klammern → auch Matrix).
- **Schaltplan:** Component (R, C, L, Diode, Z-Diode, LED, Spannungs-/Stromquellen DC/AC, gesteuerte Quellen, Schalter, Lampe,
  Mess­geräte, Sicherung; Strompfeil), Device (npn/pnp, MOSFETs, JFET, OpAmp, Verstärker, Zweitor, Masse, Klemme, Knoten,
  Mischer, Summierer, Oszillator, Filter, ADC, Antenne), Wire, Node.
- **Parameter:** Schieberegler; wirkt als Konstante beim Aufbau der Szene (nicht über die Zeit).

## Animationen (Zeitachse)
- Jede Animation hat Ziel, Dauer und Schritt: gleicher Schritt = gleichzeitig, aufsteigende Schritte = nacheinander.
- **Im Editor-Menü:** Erscheinen: Create (Linie zeichnet sich), FadeIn, Write (Text/Formel Strich für Strich),
  GrowFromCenter · Bewegen: Shift, MoveTo, Rotate (auch um einen Punkt: Zeiger), Scale · Betonen: Indicate.
- **Nur über das Szenen-JSON:** MoveAlongPath (Objekt läuft auf einer Kurve; zusammen mit Create der Kurve = Spur),
  ChangeValue (ValueTracker; im Modell liest aber kein Objekt den Tracker → praktisch unbrauchbar).
- **Operationen, die selbst als Prozess ablaufen:** Σ, ∏, Skalarprodukt (Rechenbild, 3 Darstellungen), Arithmetik
  (+ − × ÷ mit Quadraten/Zahlenstrahl), **Faltung f∗g** (gespiegelte Funktion gleitet, Produktfläche und Ergebnis wachsen).
  Statisch: Summe/Produkt/Differenz zweier Funktionen, Schnitt zweier Formen.

## Was damit schon geht (Muster)
- Schrittweiser Aufbau: Achsen → Kurve zeichnen (Create) → Markierung erscheint → Pfeil/Beschriftung (FadeIn/Write).
- Blockbild/Datenfluss: Kästen erscheinen nacheinander, ein kleines Objekt (Paket, Token) wandert per Shift/MoveAlongPath.
- Zeiger dreht sich (Rotate um Ursprung); Punkt wandert auf Kurve (MoveAlongPath); Vergleich: zweite Kurve erscheint.
- Iteration als Folge von Erscheinen: Glied 1, 2, 3 … nacheinander (je ein Objekt); Grenzprozess als CurveFamily-Glieder.

## Grenzen: Editor-Lücken (Kürzel für die Vorschläge)
- **L1 Verschwinden:** FadeOut/Uncreate sind in der Engine, aber nicht im Modell → nichts kann wieder weggehen.
- **L2 Umformen/Morph:** Transform, ReplacementTransform, TransformMatchingTex (Engine) fehlen im Modell → keine
  Kurve-wird-Kurve, keine Formelumformung Schritt für Schritt.
- **L3 Parameter/Zeit animieren:** kein Parameter-Sweep (Frequenz, Grenzwert n → ∞, laufende Welle f(x − ct), Punkt auf Kurve
  mit mitlaufender Tangente/Projektion, Schieberegler als Animation).
- **L4 Kamera-Animation:** 3D-Szene drehen/zoomen über die Zeit.
- **L5 Gitter-Morph:** lineare Abbildung/Matrix auf die Ebene anwenden, Koordinatentransformation.
- **L6 Teilchen:** viele bewegte Punkte (Ladungsträger-Drift, Diffusion, Zufallsbewegung, Stichproben ziehen).
- **L7 Weitere Operationen:** Ableitung/Integral als Prozess, Fourier-Teilsummen, Abtasten, Matrix·Vektor, Histogramm
  wächst, Korrelation.
- **L8 Code/Speicher:** Code-Objekt mit Zeilen-Hervorhebung und Variablen-/Speicherzustand (Programmablauf).
- **L9 Zellen einzeln betonen:** Table-Zellen nacheinander hervorheben (heute nur über Rechtecke darübergelegt).
- **L10 Abspielen im Artikel:** Start/Stopp-Knopf im Artikel fehlt ganz (baut ein anderer Agent).
