# animate / EtUndSo — Feature-Roadmap (Brainstorm → Bedarf → Phasen)

Ziel: eine browserbasierte Weiterentwicklung von Manim für Erklärungen in **Elektrotechnik** (Kern),
**Mathematik** (Unterbau) und angrenzenden natur-/ingenieurwiss. Fächern. Unten: was wir bauen sollten,
was die Engine dafür braucht, und eine dependency-bewusste Reihenfolge.

## Schon vorhanden
- **Objekte:** Circle, Dot, Line, Rectangle, Square, Vector, Axes(+Grid), FunctionGraph (2D + Fläche),
  Surface, Sphere, Box, Cube, Pyramid, Text, MathTex, Signale (ε/rect/tri/si/sinc/ramp), Riemann, DecimalNumber.
- **Animationen:** Create, FadeIn, GrowFromCenter, Shift (Engine zusätzlich: FadeOut, Transform,
  ReplacementTransform, TransformMatchingTex, Recolor, Pulse/PulseColor/AppearPulseColor, ChangeValue).
- **Operationen:** Convolution, Produkt/Summe/Differenz (Funktionen), Intersection (Geometrie),
  Arithmetik (Zahlen), Σ/∏ (Reihen).
- **Infra:** ValueTracker, Updater/always_redraw, Kamera 2D/3D (Orbit/Zoom/ViewCube/Gizmo/LOD),
  Timeline/seek (wasserdicht), Painter (Canvas), MathJax→VMobject, adaptives Plotten.

## Brainstorm — was noch rein sollte

### Objekte
**Geometrie/Mathe:** Angle (Bogen+Label), Arc, Ellipse, RegularPolygon/Polygon(n), Sector, Brace
(geschweifte Klammer + Label), NumberLine (eigenständig), Tangente/Sekante, Parametrische Kurve
(x(t),y(t)), Polarplot r(θ), implizite Kurve f(x,y)=0, Ungleichungs-/Flächenfüllung, Matrix/Tabelle,
komplexe Ebene.
**Analysis:** Fläche unter Kurve (exakt), Ableitungs-/Tangenten-Visual, Taylor-Approximation, Richtungsfeld.
**3D:** ParametricSurface, ParametricCurve3D, Vektor3D, Ebene, Rotationskörper, Contour/Heatmap, 3D-Vektorfeld.
**ET/Physik:** Schaltungselemente (R/L/C/Quelle/Draht/Knoten), Zeigerdiagramm (Phasor),
Bode-Diagramm, Nyquist, Pol-/Nullstellen (s-Ebene), Spektrum/FFT-Balken, Stem-Plot (diskret),
E-/B-Feldlinien, Äquipotential, Ladung, Feder/Pendel/Masse, Kraftpfeile/Freikörperbild, Welle (lauf./stehend).

### Animationen (nach Bewegungsart)
**Erscheinen:** Write (Strich-für-Strich Text/Formel), DrawBorderThenFill, SpinIn, Uncreate, GrowFromPoint/Edge.
**Bewegen:** MoveTo, MoveAlongPath, Rotate, Scale, Flip, TracedPath (Spur eines Punktes).
**Transform:** Transform/ReplacementTransform (da), TransformMatchingShapes, Morph zwischen Objekten.
**Betonen:** Indicate, Flash, Wiggle, Circumscribe, FocusOn (Pulse da).
**Werte:** CountUp/ChangeDecimal (ChangeValue da).
**Kamera:** Orbit-360°/Zoom/MoveTo (Kamera-Objekt, s. Batch A).

### Operationen
**Funktionen:** Komposition f∘g, Ableitung f′, Integral ∫f, Fourier-Reihe/-Transformation, Laplace,
Skalieren/Verschieben f(ax+b), Abtasten/Quantisieren, Korrelation (Convolution da).
**Geometrie:** boolesche Vereinigung/Schnitt/Differenz, Transform (Matrix anwenden), Spiegeln/Drehen,
Schnittpunkte, Tangente an Kurve.
**Vektor/LinAlg:** Skalar-/Kreuzprodukt, Matrix·Vektor, Matrix·Matrix, Determinante (Fläche/Volumen),
lineare Transformation des Raums (Gitter-Morph), Eigenvektoren.
**Daten/Statistik:** Mittel/Varianz, Regression/Fit, Histogramm.
**Reihen:** geschlossene Form bekannter Reihen (Batch H).

## Was wir dafür brauchen (Engine-Primitive)
1. **Ergebnis-als-Element** (bestätigt): Operationsergebnisse benannt + verkettbar — Grundlage für Pipelines.
2. **Parametrik:** generische Parameterkurve/-fläche (t bzw. u,v) → Polar, parametrisch, Rotationskörper, 3D-Kurven.
3. **Transform-/Pfad-Infrastruktur:** MoveAlongPath (Pfad-Parametrisierung), Rotate/Scale-um-Punkt als Animationen.
4. **Betonungs-Animationen** (Indicate/Flash/Circumscribe) auf Pulse-Basis.
5. **Brace/Angle/Arc-Primitive** (häufig gebraucht, klein).
6. **Log-Achsen** (Bode) + **komplexe Funktionsauswertung** (Pol-/Nullstellen, Nyquist).
7. **Matrix-Objekt** + lineare-Transformation-Animation (Gitter unter Matrix).
8. **Schaltungs-Sublanguage** (größtes Teilprojekt): Element-Bibliothek + einfache Platzierung/Verdrahtung.
9. **Kamera-Objekt** animierbar (Batch A) — für dynamische 3D-Renders.

## Vorgeschlagene Phasen (klein→groß, abhängigkeitsbewusst)
- **P0 Fundament:** Ergebnis-als-Element (bestätigt) · Betonungs-Animationen (Indicate/Flash/Circumscribe) ·
  Rotate/Scale/MoveTo/MoveAlongPath · Write. *(breiter Nutzen, kleine Bausteine)*
- **P1 Geometrie-Primitive:** Angle, Arc, Ellipse, RegularPolygon, Brace, NumberLine, Parameter-/Polarkurve.
- **P2 Analysis:** Tangente/Ableitung, exakte Integralfläche, Taylor, Richtungsfeld; Ops Ableitung/Integral/Komposition.
- **P3 Lineare Algebra:** Matrix-Objekt, lineare Transformation (Gitter-Morph), Skalar-/Kreuzprodukt, Eigenvektoren.
- **P4 Signale & Systeme (ET-Kern):** Log-Achsen, Bode, Pol-/Nullstellen, Spektrum/FFT, Stem, Zeigerdiagramm,
  Fourier-Reihe/-Transformation.
- **P5 Schaltungen:** R/L/C/Quelle/Draht/Knoten-Bibliothek + Platzierung/Verdrahtung.
- **P6 Physik/Felder/Mechanik:** E-/B-Feldlinien, Feder/Pendel/Projektil, Wellen (lauf./stehend/Interferenz).
- **P7 3D-Tiefe:** ParametricSurface/Curve3D, 3D-Vektorfeld, Ebenen, Contour/Heatmap; Kamera-Objekt (Batch A).
- **Querschnitt:** Daten/Statistik (Histogramm, Regression), geschlossene Reihenformen (Batch H).

Reihenfolge-Logik: P0 schaltet Verkettung + die häufigsten Animationen frei (Hebel für alles Weitere),
P1–P3 sind der Mathe-Unterbau, P4/P5 der ET-Kern (Herzstück EtUndSo), P6/P7 Vertiefung.
