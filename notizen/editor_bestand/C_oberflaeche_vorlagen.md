# Bestandsaufnahme Editor-Oberfläche (Teil C: UI und Arbeitsablauf)

Stand: 2026-10-28, Repo `C:\Users\info\PycharmProjects\pythonanimation`, letzter Commit `75aeed1` (Arbeitsbaum sauber, durch dieses Audit nichts verändert).
Grundlage: `web/editor.html` (228 Z.) und `web/editor.js` (2198 Z.) vollständig gelesen, dazu `web/py/editor_backend.py`, `web/py/app.py`, `tools/editor_vorlagen.py`, `tools/editor_shot.py`, `tools/editor_ui_test.py`, aus der Engine `scene_model.py` (Registries, `_build_object`, `construct`), `svg_painter.py`, `animation.py`, `text.py`, `svg.py` (MathTex), `circuit.py` (Kopf).
Zusätzlich im echten Browser geprüft (Chrome 156 über Playwright, `python -m http.server 8000 --directory web`, Server danach beendet): `editor_ui_test.py`, `editor_shot.py` und drei eigene Prüfskripte (im Scratchpad: `probe_ui.py`, `probe_gizmo3.py`, `mk_tex_scene.py`; Ergebnisse in `probe_out/probe.json`, Bilder in `probe_out/`, `gizmo_out/`, `shot_out/`).

Kennzeichnung: **[Browser]** = im laufenden Editor nachgeprüft, **[Code]** = nur aus dem Quelltext abgeleitet.

---

## 1. Oberfläche und Objektpalette

### 1.1 Aufbau der Seite (`web/editor.html`)
- Kopfleiste (Z. 142–156): „Save scene“ (grün), „Load scene“ (Dateiauswahl `.json`), „Photo ▾“ und „Animation ▾“ (Export, je mit Formatmenü), Tag/Nacht-Schalter, Reiter „Editor | Code | Both“. **„Code“ und „Both“ sind deaktiviert** (`disabled`, Titel „coming in Batch 5“, Z. 153–154). Die Engine hätte einen Codegenerator (`scene_model.py:1705 model_to_code`), die UI ruft ihn nicht auf.
- Vorschau (Z. 158–198): Zeichenfläche `#view` 1920×1080 (fest 16:9), darunter WebGL-Ebene `#view3d`, Overlay `#editgizmo` (Auswahlrahmen + Verschiebepfeile), ViewCube und Kamera-Gizmo (nur im 3D-Modus), KaTeX-Overlay `#sum-overlay` (nur Σ-Fallback), Vorberechnungs-Overlay (Zahnrad + %).
- Globale Schalter unter der Vorschau (Z. 168–197): „Animations: sequential | simultaneous“, „View: 2D | 3D“, Transport ⏮ ▶ ⏸ ⏭, „⟳ Neu berechnen“, Statuszeile, „Numbers: real | complex (Re/Im)“, „Angle: rad | deg“.
- Drei große Kästen (Z. 199–219):
  - **Add Elements**: Vorlagen-Dropdown `#templates`, Objektpalette `#palette`, Operationspalette `#comp-palette`.
  - **Scene**: Objektliste (mit Zeile „Settings“ für Hintergrund), Animationsliste, Operationsliste.
  - **Properties**: Eigenschaften des gewählten Objekts bzw. der gewählten Operation.
- Externe Abhängigkeiten (alle per CDN, ohne Internet startet nichts): Pyodide 0.27.2 (Z. 221), MathJax 3.2.2 tex-svg (Z. 10–11), KaTeX 0.16.11 (Z. 7–8). Der Aufruf `/api/count` (Z. 226) liefert lokal 404 (harmlos) **[Browser]**.

### 1.2 Objektpalette (`CATALOG`, `editor.js:52–191`, aufgebaut in `buildPalette`, Z. 1115–1128)
Klick auf einen Eintrag = `addObject(type, defaults)` (Z. 846–865). 9 Gruppen, 48 Einträge, 42 verschiedene Typen. **[Browser]**: Alle 48 Einträge einzeln in eine Szene mit einem Axes eingefügt, jeder rendert ohne Fehler („Ready ✓“, `probe_out/probe.json`).

| Gruppe | Einträge |
|---|---|
| Mathematik · Geometrie | Circle, Dot, Line, Rectangle, Square, Ellipse, Vector |
| Mathematik · Funktionen & Achsen | Axes, FunctionGraph, Area, TangentLine, CurveFamily, ParametricCurve, PolarCurve, DataCurve, Band, Stem, PointCloud, NumberLine, Legend |
| Mathematik · Felder | VectorField, ScalarField |
| Mathematik · 3D-Körper | Sphere, Box, Cube, Pyramid |
| Elektrotechnik · Signale | 6 Voreinstellungen eines FunctionGraph: ε(t), rect(t), tri(t), si(t), sinc(t), ramp(t) (`_type:"FunctionGraph"`) |
| Allgemein · Text & LaTeX | Text, MathTex, TextBox |
| Allgemein · Annotation | Marker, Measure, LabeledArrow, LoopArrow, Brace, Mark, Shape, Table |
| Allgemein · Parameter | Parameter |
| Elektrotechnik · Schaltplan | Component, Device, Wire, Node |

Verhalten beim Hinzufügen (`addObject`, Z. 846–865) **[Code+Browser]**:
- Jedes neue Objekt mit `color` (außer Text und MathTex) bekommt eine **Automatikfarbe** aus `AUTO_COLORS` (blau, orange, grün, rot, …), die Katalogvorgabe (oft Schwarz `#111111`) wird überschrieben; `fill_color` wird gleich mitgesetzt (Z. 849–853). Folgen, im Browser gesehen: ein neuer Widerstand ist blau (`probe_out/pal_Component.png`); bei **TextBox ist der Text unsichtbar**, weil Füllung (Deckkraft 1) und Schrift dieselbe Farbe bekommen (`probe_out/pal_TextBox.png`).
- Ein neues Objekt landet im gerade gewählten Teilbild (gewähltes Axes oder Axes des gewählten Objekts), außer Axes und `WORLD_TYPES` (Z. 857–861).
- Position immer die Katalogvorgabe (meist Ursprung), kein „hier klicken, um zu platzieren“.
- Die Signal-Voreinstellungen werden **ohne Ergänzung der Standard-Eigenschaften** angelegt (`ensureDefaults` läuft nur beim Laden, Z. 330–339): ihr Eigenschaftenfeld zeigt nur `func`, `x_range`, `color`, `stroke_width` (kein `dash`, kein `stroke_opacity`), erst nach einem Neuladen der Seite kommen die übrigen Felder dazu **[Browser]**.

### 1.3 Operationspalette (`COMPUTATIONS`, Z. 294–318)
11 Einträge in 4 Gruppen: Summation (Σ), Product (∏) · Addition, Subtraction, Multiplication, Division (Zahlen, Darstellung Quadrate oder Zahlenstrahl) · Convolution, Product f·g, Sum, Difference (Operanden: FunctionGraph) · Intersection (Operanden: Circle, Rectangle, Square, Triangle, Polygon). **[Browser]**: alle 11 lassen sich anlegen; die mit Operanden stehen bis zur Auswahl als „⚠ incomplete“ in der Liste.

### 1.4 Typen, die es nur in der Engine bzw. im JSON gibt
Registry `scene_model.py:159–176` plus Sonderzweige in `_build_object` (Z. 1191–1343):
- **Objekte ohne Paletteneintrag**: `Polygon`, `Triangle` (beide sogar als Intersection-Operanden zugelassen, `editor.js:291`, aber in der UI nicht erzeugbar), `ValueTracker`, `ThreeDAxes`, `SVGMobject`, `Riemann` (nur über die Vorlage „Riemann approximation“), `plot` (Graph auf benanntem Axes, `scene_model.py:1197`), `DecimalNumber` (nur als Ergebnis-Kind, s. 2.3).
- **Animationen**: Die UI bietet 9 (`ANIM_GROUPS`, Z. 449–453: Create, FadeIn, Write, GrowFromCenter, Shift, MoveTo, Rotate, Scale, Indicate). Registriert, aber nicht in der UI: `MoveAlongPath`, `ChangeValue` (`scene_model.py:170–176`). In `animation.py` vorhanden, aber **gar nicht registriert** (also auch per JSON nicht nutzbar): FadeOut, Pulse, PulseColor, AppearPulseColor, Recolor, Refine, Transform, ReplacementTransform, TransformMatchingTex.
- JSON-only-Objekte lassen sich nach dem Laden im Eigenschaftenfeld nur eingeschränkt bearbeiten: verschachtelte Listen (z. B. `vertices` eines Polygon) werden als Zahlenfelder mit Listeninhalt dargestellt und sind praktisch nicht editierbar **[Code, `propInput` Z. 1399–1403]**.

---

## 2. Eigenschaften je Typ (UI gegenüber Engine)

### 2.1 Wie das Eigenschaftenfeld gebaut wird (`propInput`, Z. 1364–1408)
Das Steuerelement wird aus dem **Typ des Vorgabewerts** abgeleitet, nicht aus einer Beschreibung:
| Regel (in dieser Reihenfolge) | Steuerelement |
|---|---|
| Schlüssel steht in `ENUMS` (Z. 1339–1360) | Auswahlliste |
| `Parameter.value` | Schieberegler + Zahlenfeld (einziger Regler im Editor) |
| Schlüssel `dash` | Auswahl solid/dashed/short/dotted/dash-dot + Freitext „an,aus px“ |
| Text in `MULTILINE_KEYS` = `data`, `cells`, `points`, `text` | mehrzeiliges Textfeld (Monospace) |
| Liste | je Komponente ein Zahlenfeld (2 oder 3) |
| true/false | Kontrollkästchen |
| Zahl | Zahlenfeld (`step 0.1`, Pfeile per CSS ausgeblendet, übernimmt bei Enter/Verlassen) |
| Text, der mit `#` beginnt | nativer Farbwähler (nur Hex, keine Deckkraft, keine Palette) |
| sonstiger Text | einzeiliges Textfeld |

Darüber hinaus: bei mehreren Axes ein Feld „axes“ (Teilbild-Wahl, Z. 1444–1449), bei Circle/Rectangle/Square/Line/FunctionGraph/Riemann der Block „Results“ (Kontrollkästchen, Z. 1590–1616), immer der Block „Animations“ (Z. 1620–1657). Für FunctionGraph werden `adaptive`, `res_max`, `res_min` bewusst ausgeblendet (Z. 1452–1459, vgl. EDITOR_FIXES #5).

### 2.2 Felder je Typ (aus dem Browser ausgelesen, `probe_out/probe.json`) und was nur die Engine kennt
Abkürzungen: Z = Zahlenfeld, V = Vektor (Zahlenfelder), T = Text, TA = mehrzeiliges Textfeld, F = Farbe, H = Haken, A = Auswahl, S = Strich-Widget.
Abgleich mit der Engine: für alle Builder-Typen (figures.py, circuit.py, Sonderbuilder in scene_model.py) habe ich per AST die Schlüssel ausgelesen, die der Builder liest (`propdiff.py`): **UI-Felder und Engine-Schlüssel stimmen überein**, Ausnahmen in der rechten Spalte. Für Klassen-Typen wurden die Konstruktor-Parameter verglichen.

| Typ | Felder in der UI | nur Engine/JSON (nicht in der UI) |
|---|---|---|
| Circle | center V, radius Z, color F, fill_color F, fill_opacity Z, stroke_width Z, dash S, show_center H; Results: Radius, Area, Circumference | stroke_opacity |
| Dot | center V, radius Z, color F, stroke_width Z, show_center H | – |
| Line | start V, end V, color F, stroke_width Z, dash S, show_center H; Results: Length, Slope | stroke_opacity |
| Rectangle / Square | center V, width+height Z bzw. side Z, color/fill_color F, fill_opacity Z, stroke_width Z, dash S, show_center H; Results (Rechteck 5, Quadrat 4) | stroke_opacity |
| Ellipse | center V, width Z, height Z, color/fill_color F, fill_opacity Z, stroke_width Z, dash S, show_center H | – |
| Vector | end V, start V, color F, stroke_width Z, dash S | – |
| Axes | x/y/z_range V(2), x/y/z_length Z, origin V, title T, x_label/y_label T, x_log/y_log/arrows H, x_axis_at A (auto, bottom), y_axis_at A (auto, left), show_axes/show_ticks/show_numbers/x_numbers/y_numbers/show_labels/minor_ticks H, number_size/label_size/axis_width Z, x/y/z_color F, grid_x/y/z H, grid_color F, grid_width Z | `z_label`, `tick_size`, **Teilstrich-Schritt als 3. Eintrag von x_range/y_range** (Engine `axes.py:118`; die UI zeigt nur 2 Felder) |
| FunctionGraph | func T, x_range V, color F, grid_color F, grid_width Z, stroke_width Z, stroke_opacity Z, fill_opacity Z, height_color H, dash S; Result: Integral | adaptive, res_max, res_min (bewusst verborgen) |
| Area | func, func2 T, x_min, x_max, samples Z, color/fill_color F, fill_opacity, stroke_width Z, dash S | – |
| TangentLine | func T, x0 Z, secant H, x1, half_len Z, show_point, show_slope H, triangle_dx Z, dx_label, dy_label T, font_size Z, color F, stroke_width Z, dash S | – |
| CurveFamily | func, param T, p_min, p_max, count Z, values, labels T, x_min, x_max, samples Z, fade, show_limit H, limit_func T, font_size Z, color F, stroke_width Z, dash S | – |
| ParametricCurve | fx, fy T, t_min, t_max, samples Z, show_arrow H, point_at T, show_tangent, show_normal H, color F, stroke_width Z, dash S | – |
| PolarCurve | func T, theta_min, theta_max, samples Z, show_arrow H, color F, stroke_width Z, dash S | – |
| DataCurve | data TA, markers H, marker_radius Z, smooth H, color F, stroke_width Z, dash S | – |
| Band | x_min, x_max, y_min, y_max Z, full_height, full_width H, label T, label_at A, font_size Z, color/fill_color F, fill_opacity, stroke_width Z, dash S | – |
| Stem | x, y, labels T (Listen „1;2;3“ als Text), baseline Z, markers H, marker_radius, font_size Z, color F, stroke_width Z, dash S | – |
| PointCloud | n, x_min…y_max, seed Z, distribution A, decay, radius Z, hollow H, color F, stroke_width Z | – |
| NumberLine | x_min, x_max, step, length Z, center V, tick_labels H, decimals, font_size Z, color F, stroke_width Z | – |
| Legend | labels, colors T (Hex ohne `#`, als Freitext), position V, font_size, row_gap, swatch_len, gap Z, color F, stroke_width Z | – |
| VectorField | preset A, fx, fy T, x_min…y_max, nx, ny, scale Z, normalize H, max_len Z, color_by_mag H, color F, stroke_width Z | – |
| ScalarField | func T, x_min…y_max, nx, ny, levels Z, show_heat, show_contours H, gradient_at T, grad_scale, font_size Z, color F, fill_opacity Z | `stroke_width` (Engine liest es, Katalog hat es nicht); `font_size` steht in der UI, wird aber vom Builder nicht gelesen |
| Sphere / Box / Cube / Pyramid | Maße Z, center V, (Sphere: resolution Z), color F, fill_opacity Z | – |
| Text | text TA, position V, font_size Z, align A (center, left, right), color F | – |
| MathTex | tex T (einzeilig), height Z, position V, color F | `scale`, `fill_opacity`; **position/height in Welt-Einheiten, nicht in Achsen-Daten** (`scene_model.py:366–367`) |
| TextBox | text TA, center V, width, height Z, shape A, padding, font_size Z, color/fill_color F, fill_opacity, stroke_width Z, dash S | – |
| Marker | point V, label T, label_pos A (8), show_guides H, guide_dash T (Freitext, nicht das Strich-Widget), x_expr, func, func2, y_expr T, radius, font_size Z, color F | – |
| Measure | start, end V, label T, offset, font_size Z, color F, stroke_width Z, dash S | – |
| LabeledArrow | start, end V, label T, label_at A, double H, elbow A (none, hv, vh), thick, head_size, font_size Z, color F, stroke_width Z, dash S | – |
| LoopArrow | center V, radius, start_angle, end_angle Z, head H, label T, font_size Z, color F, stroke_width Z, dash S | – |
| Brace | start, end V, label T, flip H, size, font_size Z, color F, stroke_width Z | – (kein dash) |
| Mark | center V, kind A (check, cross, strike), size, width, height Z, color F, stroke_width Z | – |
| Shape | points TA, closed H, label T, material A (10), font_size Z, color/fill_color F, fill_opacity, stroke_width Z, dash S | – |
| Table | cells TA, row_labels, col_labels, highlight T, brackets H, cell_w, cell_h Z, position V, font_size Z, color/fill_color F, fill_opacity, stroke_width Z | – |
| Parameter | name T, value Regler+Z, min, max, step Z | – |
| Component | kind A (25), start, end V, label, value T, label_flip H, current T, current_at A, current_reverse H, voltage T, voltage_reverse H, size, font_size Z, color F, stroke_width Z | – |
| Device | kind A (25), center V, rotation Z (Grad), flip H, label T, pins H, size, font_size Z, color F, stroke_width Z | – |
| Wire | points TA, route A (direct, hv, vh), dots T, dot_radius Z, color F, stroke_width Z, dash S | – |
| Node | center V, label T, offset V, dot H, radius, font_size Z, color F | – |

Alle Werte der Auswahllisten (`ENUMS`) kommen im Engine-Quelltext als Zeichenkette vor (geprüft, z. B. alle 25 Component- und 25 Device-Arten).

### 2.3 Ergebnisse (Results) und Kinder
- Results erzeugen ein Kind `DecimalNumber` mit `position, font_size, color, decimals, prefix` (Z. 1604–1611); das Kind erscheint eingerückt in der Objektliste und ist wie ein Objekt einstellbar. `suffix` (Engine) fehlt.
- **Ergebnis-Kinder von Operationen** (z. B. „Intersection area = …“) sind weder in der Liste noch per Klick erreichbar (`renderComputations` zeigt keine Kinder; `findNode` sucht nur in `model.objects`), also in der UI nicht einstellbar **[Code]**.

### 2.4 Operationen (Properties › Operation)
Σ: Mode (Zahlenreihe | Funktions-Teilsumme/Fourier), term T, from Z, to T (Zahl oder „n“), show_terms, run_time, size Z, position V, sechs Farben. ∏ ebenso ohne Mode. Arithmetik: Darstellung A, bis 10 Zahlen (+ number), run_time. Funktionsoperationen: Operanden-Auswahl (nur passende Typen), run_time/tau_range (Faltung), color, stroke_width. Intersection: Operanden A/B, Farben **[Browser]**.

---

## 3. Szenenformat, Speichern/Laden/Link, Vorlagen

### 3.1 Editor-Modell und Speicherformat
Speicherformat (`sceneData`, Z. 1078–1082):
```
{ v:1, counters:{nextId, nextAnimId, nextCompId},
  model:{ objects:[…], animations:[…], computations:[…], background:{color, transparent, shadows, axes_on_top},
          playMode:"sequential"|"parallel", angleUnit:"rad"|"deg", domain:"real"|"complex",
          camera:{mode:"2d"|"3d", theta, phi, zoom} } }
```
- Objekt: `{id:"o<N>", type, props:{…}, visible?, expanded?, on?:<Axes-id>, children?:[…], result?:{key}, a?, b?}`. Farben als Hex-Text.
- Animation: `{id:"a<N>", type, target:<Objekt-id>, run_time, visible?, vector? | point? | angle? (Grad) | factor?}`.
- Operation: `{id:"k<N>", type, props, visible?, numbers? | inputs:{rolle:<id>}, children?}`.
- **Parameter sind gewöhnliche Objekte** vom Typ `Parameter` (kein eigener Abschnitt).
- Für die Engine wird das Modell übersetzt (`toPythonModel`, Z. 482–519): Hex → RGB-Tripel, Animationen bekommen `step` (sequenziell = Listenindex, simultan = 0), Rotate Grad → Bogenmaß, MathTex-`tex` → Glyphendaten aus MathJax, ausgeblendete Animationen entfallen.
- Lesen (`applyScene`, Z. 1083–1101) akzeptiert das Speicherformat oder ein nacktes Modell; fehlende Eigenschaften werden aus dem Katalog ergänzt (`migrateModel`).

### 3.2 Speichern und Laden
- **Save scene**: lädt `szene.animate.json` herunter (Z. 1102–1106). **Load scene**: Dateiauswahl, `FileReader` (Z. 1107–1111, 2029).
- **Automatisches Speichern** in `localStorage["animate.scene.v1"]` nach jedem Rendern, jeder Kamerabewegung, jedem Hintergrundwechsel (Z. 797, 567, 1112). Theme separat in `animate-theme`.
- Startreihenfolge (Z. 2010–2017): `?scene=` → automatisch gespeicherte Szene (wenn sie Objekte hat) → Startbeispiel (3D-Fläche sin x + cos y, `START_EXAMPLE` Z. 281–287).

### 3.3 Laden per Link `editor.html?scene=…`
- `fetch(sceneUrl, {cache:"no-cache"})`, dann `applyScene` (Z. 2012–2015). **[Browser]**: `?scene=szenen/beispiel-emitterschaltung.json` lädt (17 Objekte).
- Die Meldung „Szene geladen ✓“ wird sofort vom nächsten Rendern durch „Ready ✓“ überschrieben.
- In `web/szenen/` liegt nur `beispiel-emitterschaltung.json` (ohne `counters`, IDs wie `pa`, `t`). Kein Artikel und keine Seite verlinkt bisher `editor.html?scene=` (Suche im Repo).
- **Risiken [Code]**: (1) Wer einen Link öffnet, verliert seine automatisch gespeicherte Szene (sie wird beim ersten Rendern überschrieben, ohne Rückfrage). (2) Die URL ist nicht eingeschränkt (jede per CORS erreichbare Adresse). Szenendateien sind ausführbarer Inhalt: Der Σ/∏-Term wird im Browser mit `new Function("i","with(Math){return (…)}")` ausgewertet (`evalExprJS`, Z. 1699–1703, aufgerufen bei jedem Rendern über `updateSumOverlay` → `sumStages`). Eine präparierte Szene führt damit beliebiges JavaScript im Editor aus. Ausdrücke in Python laufen mit `eval(…, {"__builtins__": {}})` (`scene_model.py:291–321`), was keine echte Sandbox ist. Empfehlung: `?scene=` auf relative Pfade unter `szenen/` begrenzen und `evalExprJS` durch einen Parser ersetzen.

### 3.4 Vorlagen
- Definition: Konstante `TEMPLATES` in `editor.js` (Z. 197–276). 9 handgeschriebene (Empty axes, Sine (drawn), Parabola + point, Riemann approximation, Unit circle, Function f(x) (2D), 3D solids, Convolution f∗g, Intersection of two circles) und 7 generierte ET-Vorlagen zwischen `// >>> ET-Vorlagen (generiert)` und `// <<< ET-Vorlagen` (Z. 267–275).
- Format einer Vorlage: `{objects:[{key, type, props, on?:<key>, children?, visible?, result?}], animations?:[{type, targetKey, run_time, vector?}], computations?:[{type, inputs:{rolle:<key>}, props, numbers?, children?}], camera?, background?, playMode?}`. Nur abweichende Eigenschaften nötig, der Rest kommt aus dem Katalog (`migrateModel`, Z. 945).
- Auflistung: Dropdown mit Gruppen aus `TEMPLATE_GROUPS` (Z. 1130–1137: Mathematik · Analysis 6, Geometrie 2, 3D 1, Elektrotechnik · Vorlagen 7); nicht eingetragene Vorlagen landen unter „Weitere“ (Z. 1148–1149).
- **Einfügen heißt Ersetzen**: `loadTemplate` (Z. 922–951) leert Objekte, Animationen und Operationen und baut die Vorlage neu auf. Es gibt kein „in die aktuelle Szene einfügen“, keine Rückfrage, kein Rückgängig; die automatische Sicherung wird überschrieben.
- Einschränkung in `loadTemplate`: von Animationsparametern wird nur `vector` (Shift) übernommen (Z. 928–929). `point` (MoveTo), `angle` (Rotate), `factor` (Scale) einer Vorlage gehen verloren; ein MoveTo ohne `point` würde in der Engine scheitern (Pflichtargument, `animation.py:294`). Derzeit nutzt keine Vorlage diese Typen.
- **Neue Vorlage anlegen**: (a) für ET-Vorlagen in `tools/editor_vorlagen.py` im Dict `T` einen Eintrag mit `o(key, typ, on, **props)` bzw. `bare()` für ein 1:1-Schaltplan-Teilbild ergänzen und `python tools/editor_vorlagen.py` ausführen; das Skript schreibt **direkt in `web/editor.js`** (beide markierten Blöcke, wiederholbar; mit `--json <ordner>` zusätzlich Szenen für `editor_shot.py`). Die Gruppe „Elektrotechnik · Vorlagen“ wird dabei aus allen Schlüsseln von `T` neu erzeugt. (b) Sonst `TEMPLATES` und `TEMPLATE_GROUPS` in `editor.js` von Hand ergänzen. Eigene Vorlagen aus der UI heraus speichern geht nicht.

---

## 4. Parameter, Zeitleiste, Animation, Export in der UI

### 4.1 Parameter
- Objekt `Parameter` (name, value, min, max, step). Im Eigenschaftenfeld Regler + Zahl; der Regler baut die Szene bei jeder Bewegung neu auf (`oninput` → `renderPreview`, 70 ms entprellt, Z. 1372–1381). Die Objektliste zeigt „Name = Wert“ (Z. 1273). **[Browser]**: UB im Kennlinienfeld von 5 auf 3,5 → Arbeitspunkt wandert.
- Die Engine setzt die Namen vor dem Kompilieren aller Ausdrücke (`scene_model.py:1594–1604`); reservierte Namen (x, y, t, i, e, pi, j, theta) und Funktionsnamen werden still ignoriert (`_safe_names`, Z. 244–258).
- Grenzen: Ändern von min/max/step wirkt auf den Regler erst nach erneutem Anwählen; ein Parameter lässt sich **nicht animieren** (kein Parameter-Film; `ChangeValue` ist nur für ValueTracker und nicht in der UI).

### 4.2 Animationen und „Zeitleiste“
- Es gibt **keine Zeitleiste** im Sinne einer Spur mit Startzeiten oder eines Zeitschiebers. Animationen werden am gewählten Objekt mit „+ Create“ usw. angelegt (Z. 953–962, 1651–1655). Je Animation einstellbar: `run_time` (Sekunden) und bei Shift `vector`, MoveTo `point`, Rotate `angle°`, Scale `factor` (Z. 1625–1650). Nicht einstellbar: Verzögerung, Startzeitpunkt, Easing (`rate_func` gibt es in der Engine, `animation.py:12`, aber weder UI noch JSON-Weg), Drehpunkt (`around`), Farbe/Faktor von Indicate.
- Reihenfolge: Liste „Animations“ im Kasten Scene, per Ziehen umsortierbar, Auge = beim Abspielen überspringen (Z. 1295–1332).
- Ablauf global: „sequential“ (jede Animation ein Schritt) oder „simultaneous“ (alle gleichzeitig) (Z. 487–495). Gruppen („diese zwei gleichzeitig, dann die nächste“) kann die Engine (`step`, `scene_model.py:1553–1563`), die UI nicht.
- Operationen bringen ihre Animation über `run_time` mit (Faltung, Σ, Arithmetik).
- Ruhebild: Transform-Ziele werden im Bearbeitungsmodus im Anfangszustand, Erscheinen-Ziele voll sichtbar gezeigt (`show_static`, `scene_model.py:1676–1687`).

### 4.3 Wiedergabe
- ▶ rendert zuerst **alle Bilder vorab** in einen Speicher (Zahnrad + Prozent), dann flüssige Wiedergabe; Bildrate/Auflösung werden an ein Speicherbudget (1 GB bzw. 300 MB) angepasst; notfalls Live-Wiedergabe (Z. 965–1064). ⏸ Pause, ⏮ zurück zum Bearbeitungsbild, ⏭ Endbild, „⟳ Neu berechnen“ verwirft den Speicher (Z. 2021–2027). Jede Änderung oder Kamerabewegung verwirft ihn ebenfalls. **[Browser]**: „Sine (drawn)“ spielt bis „Ended ✓“.

### 4.4 Export
- **Photo** (Z. 2056–2090): PNG, JPEG, WebP (AVIF, BMP nur, wenn der Browser sie kodieren kann; in Chrome 156 nicht angeboten) über `canvas.toBlob` des aktuellen Zeichenflächen-Inhalts, immer 1920×1080, im 3D/WebGL-Modus zusammengesetzt aus beiden Ebenen. Transparenter Hintergrund möglich (Settings → transparent). **[Browser]**: PNG-Download `scene.png` (90 KB).
- **SVG (Vektor)**: ruft `export_svg()` (`editor_backend.py:10–18`) auf; `SvgPainter` (`engine/svg_painter.py`) schreibt Pfade (mit `stroke-dasharray`) und Beschriftungen als `<text>`/`<tspan>` (Hoch-/Tiefstellung), Schrift „system-ui“ (nicht eingebettet, nicht in Pfade umgewandelt). MathTex-Formeln werden als Pfade exportiert. Immer der volle Rahmen 1920×1080 (viewBox), kein Zuschnitt auf den Inhalt; exportiert wird das Bearbeitungsbild (nicht das aktuelle Animationsbild); 3D-Flächen nur flach (CPU-Maler). **[Browser]**: UI-Test liefert ein 69 648 Zeichen langes SVG mit `<path>` und `<text>`.
- **Animation** (Z. 2092–2135): Aufnahme der Zeichenfläche mit `captureStream(0)` + `requestFrame` und `MediaRecorder`, 30 fps, 12 Mbit/s, in Echtzeit getaktet; Formate MP4 (H.264), WebM (VP9, VP8, AV1), MP4 (AV1), je nach Browser. **[Browser]**: `animation.mp4` (52 KB) für die Sinus-Vorlage. Kein GIF, keine Einzelbildfolge, keine Wahl von Auflösung oder Bildrate.
- Der Kamera-Zoom (Mausrad) wirkt auf alle Exporte und wird mitgespeichert.

### 4.5 MathJax/MathTex
- Konfiguration `svg:{fontCache:'none'}`, Paket `color`, kein automatisches Setzen (`editor.html:10`).
- Ablauf: `tex` → `MathJax.tex2svg` → alle `path`/`rect`/`use` im SVG mit ihrer Transformationsmatrix und dem Zeichen (`_tex2glyphs`, Z. 1838–1876) → Cache `_texCache` → beim nächsten Rendern als Glyphendaten an die Engine (`injectTexGlyphs`, Z. 1897–1902) → Python-Klasse `MathTex` baut daraus Bézier-Pfade (`engine/svg.py:183ff.`). Beim ersten Rendern ist die Formel leer, sie erscheint nach dem asynchronen Satz. Schlägt der Satz ganz fehl, wird ohne `\color` wiederholt (Z. 1881–1883).
- **[Browser]**: `U_{GS} = \frac{1}{\sqrt{2}}\,\hat u` wird sauber gesetzt (`shot_out/tex.png`). **Fehlerhafte Eingabe** `\frac{a` erscheint als **schwarzer Balken** (das Fehler-Rechteck von MathJax wird als gefüllter Glyph übernommen), ohne Fehlermeldung in der Statuszeile.
- Gewöhnliche Beschriftungen (Text, label-Felder) nutzen dagegen `richtext` (Hoch-/Tiefstellung, griechische Buchstaben, Symbole, Zeilenumbruch), kein echtes LaTeX: `\frac{1}{2}` wird als „frac12“ ausgegeben **[Browser]**.
- KaTeX wird nur als Übergangsanzeige für die Σ/∏-Operation verwendet, solange MathJax die Glyphen noch nicht geliefert hat (Z. 1807–1823); diese Überlagerung ist im PNG-Export nicht enthalten.
- MathTex hat kein `align`, Position und Höhe in Welt-Einheiten (anders als Text, der in Achsen-Daten liegt).

---

## 5. Bedien-Grenzen (was präzises Zeichnen behindert)

| Grenze | Beleg |
|---|---|
| **Kein Rückgängig/Wiederholen** (kein Verlauf); Strg+Z ohne Wirkung | nur Strg+C/V im Tastatur-Handler, Z. 2044–2050; **[Browser]** Zeilenzahl vor/nach Strg+Z gleich |
| Vorlage laden und Szene laden ersetzen alles ohne Rückfrage; die automatische Sicherung wird überschrieben | Z. 922–951, 797 |
| Kopieren: Strg+C/Strg+V und Knopf ⧉ (Duplizieren). Die Kopie liegt **exakt auf dem Original** (kein Versatz) und **bekommt eine andere Farbe** (`recolorFresh`); Einfügen immer auf oberster Ebene | Z. 839–845, 902–909, 2048–2049; **[Browser]** +1 Zeile |
| **Automatikfarben** beim Hinzufügen überschreiben die Katalogfarbe; Schaltpläne und Beschriftungen müssen einzeln auf Schwarz zurückgestellt werden; neue TextBox hat unsichtbaren Text | Z. 849–853; **[Browser]** `pal_Component.png`, `pal_TextBox.png` |
| **Keine Mehrfachauswahl, keine Gruppen, kein Ausrichten/Verteilen, kein Sperren** | `model.selectedId` ist ein einzelner Wert (Z. 455); Kinder nur für Ergebnis-Zahlen |
| **Keine Ebenenreihenfolge** in der UI: Zeichenreihenfolge = Objektliste, Objektzeilen sind nicht ziehbar (nur Animationen) | Z. 1255–1290; `renderer.py:119–140` |
| **Keine Umbenennung**: Zeilen heißen „Typ · o17“ (nur Parameter-Name und Axes-Titel erscheinen) | Z. 1273–1275 |
| Numerische Positionierung ja (alle Koordinaten als Zahlenfelder), aber **kein Fang/Raster/Winkelraster** | keine Snap-Logik im Code; EDITOR_GRAFIK_FEATURES §1 nennt es „steht noch aus“ |
| Maus-Verschieben nur über Achsenpfeile am Auswahlrahmen (x/y, in 3D auch z); kein Ziehen am Objekt, keine Griffe für Endpunkte, Größe, Drehung; die Werte sind **ungerundete Fließkommazahlen** (z. B. −0,773066508156659) | Z. 1474–1586; **[Browser]** `probe_gizmo3.py` |
| Mit Pfeilen verschiebbar sind nur Objekte mit `center`, `position` oder `start`+`end`; **nicht** Wire, Shape, DataCurve, Stem, Band, Area, PointCloud, FunctionGraph, Axes (auch nicht dessen `origin`) | `movablePosKeys`, Z. 1489–1495 |
| **Fehler beim Verschieben von MathTex und Vector**: die UI hält sie für Daten-Objekte (`WORLD_TYPES` der UI enthält nur Sphere/Box/Cube/Pyramid, Z. 1480), die Engine für Welt-Objekte (`scene_model.py:366–367`). Beim Ziehen folgt die Formel der Maus, nach dem Loslassen springt sie um den Faktor (Welt pro Dateneinheit)⁻¹ weiter | **[Browser]**: 150 px Ziehen = 1,479 Welt-Einheiten; Kreis bewegt sich korrekt um 4,227 Daten = 1,479 Welt; MathTex springt um 4,227 **Welt**-Einheiten (`gizmo_out/giz2_mt_during.png` vs. `…_after.png`). Ebenso zeigt die UI für MathTex/Vector das Feld „axes“, das in der Engine wirkungslos ist |
| Punktlisten (Wire, Shape, DataCurve, Table) nur als Text „x,y;x,y“, kein Zeichnen mit der Maus | `MULTILINE_KEYS`, Z. 1363 |
| Schaltplan-Symbole haben feste Welt-Größe; auf einem gewöhnlichen Axes (Daten ≠ Welt) wirken Abstände verzerrt, man braucht ein 1:1-Teilbild (`show_axes:false`, x_range [−7,7], x_length 14 …), das es nur in Vorlagen gibt | `probe_out/pal_Component.png`; EDITOR_WERKZEUGE „Bedienhinweise“ |
| Zoom nur per Mausrad um die Bildmitte (0,2–8), **kein Verschieben (Pan) im 2D**; keine Anzeige der Mauskoordinaten | Z. 1997–2007 |
| Klick-Auswahl nimmt das Objekt mit dem kleinsten umgebenden Rechteck; Achsen nur über die Liste | `editor_backend.py:170–191` |
| Kein Löschen per Entf-Taste (nur ✕) | Tastatur-Handler Z. 2044–2050 |
| Bildformat fest 1920×1080 (16:9); kein Zuschnitt, keine eigene Bildgröße, keine DPI-Wahl | `editor.html:160–162`, Export Z. 2075–2090 |
| Eingaben übernehmen erst bei Enter/Verlassen; Fehler in Ausdrücken zeigen „⚠ error … (last frame kept)“ in der Statuszeile, aber nicht am Feld | Z. 1333–1336, 791 |
| Ergebnis-Beschriftungen von Operationen nicht einstellbar | s. 2.3 |
| Ohne Internet startet der Editor nicht (Pyodide, MathJax, KaTeX per CDN) | `editor.html:7–11, 221` |
| Code-Ansicht fehlt (Reiter deaktiviert) | `editor.html:153–154` |

---

## 6. Testlage

### 6.1 `tools/editor_ui_test.py` (Lauf am 2026-10-28, Chrome 156, Ausgabe im Scratchpad `ui_out/`)
**Ergebnis: 18/18 OK, „ALLE UI-TESTS OK“.** Die Prüfungen:
1. ET-Vorlagen im Menü (genau 7) · 2.–8. jede ET-Vorlage lädt ohne Fehlermeldung in der Statuszeile (je 2,5 s Wartezeit) · 9. die 7 Bilder sind paarweise verschieden (MD5 des Zeichenflächen-Screenshots)
10. Parameter „UB = 5“ in der Objektliste · 11. ein Schieberegler im Eigenschaftenfeld · 12. Regler auf 3,5 ändert das Bild · 13. Liste zeigt „UB = 3.5“
14. Bode-Vorlage: FunctionGraph hat das Feld „axes“ · 15. Panelwechsel ändert das Bild
16. Photo ▾ → SVG lädt ein Dokument mit `<svg`, `<path`, `<text` herunter
17. `?scene=szenen/beispiel-emitterschaltung.json` lädt (besteht über die Ersatzbedingung „mehr als 5 Zeilen“, weil die Statusmeldung „Szene geladen“ sofort überschrieben wird)
18. keine `pageerror`-Ereignisse.

Nicht geprüft: Hinzufügen aus der Palette, Eigenschaften ändern (außer Regler/Panel), Animationen und Wiedergabe, PNG- und Video-Export, Speichern/Laden per Datei, Verschiebepfeile, MathTex, inhaltliche Richtigkeit der Bilder (nur „verschieden“ und „kein Fehler“). Voraussetzungen: Server auf Port 8000, Internet, Chrome-Kanal.

### 6.2 `tools/editor_shot.py`
Legt eine Szene in `localStorage`, wartet bis „Ready“, fotografiert `#view`, gibt Konsolenfehler aus. Endet auch bei Zeitüberschreitung mit „ok“ (keine Fehlerrückgabe). **[Browser]** mit der Beispielszene und einer MathTex-Testszene erfolgreich.

### 6.3 Engine-Tests (nur die in E2 genannten)
`python tests/test_figures.py` → „ALL OK“; `python tests/test_contract.py` → „CONTRACT TESTS PASSED“ (inkl. „article figures (panels, log, circuit, figures)“). Ohne Bytecode ausgeführt, Repo unverändert.

### 6.4 Eigene Zusatzprüfungen
- Alle 48 Palettenobjekte und alle 11 Operationen einzeln angelegt: kein Render-Fehler.
- Strg+Z: keine Wirkung. Strg+C/V: Kopie entsteht.
- ▶ bis „Ended ✓“; PNG- und MP4-Download funktionieren.
- Fehler gefunden: Verschieben von MathTex (und laut Code Vector) springt; TextBox aus der Palette mit unsichtbarem Text; fehlerhaftes TeX als schwarzer Balken; Signal-Voreinstellungen ohne `dash`-Feld bis zum Neuladen.
- Konsole: nur 404 für `/api/count` und `favicon.ico`.

---

## 7. Abgleich der Behauptungen A1–E2 (`EDITOR_WERKZEUGE.md`)

Hinweis: Die Spalte bewertet, ob das Werkzeug in UI und Modell so vorhanden und bedienbar ist. Ob jede Zeichnung inhaltlich exakt stimmt (z. B. 59,5 mV pro Dekade), prüfen hier nur die Engine-Tests und die Vorlagenbilder.

| Nr. | Behauptung | Befund | Belege / Einschränkungen |
|---|---|---|---|
| A1 | Strichlinien | **bestätigt** | Strich-Widget (Auswahl + Freitext) in 21 Typen (Z. 1382–1392), Engine `_parse_dash`. Fehlt bei Brace, Component, Device, Node, Mark, Table, Legend, Dot, PointCloud, NumberLine und bei den Achsen; Marker hat nur Freitext `guide_dash`; Signal-Voreinstellungen erst nach Neuladen |
| A2 | Formel-Labels | **bestätigt** | `richtext.py` in Canvas- und SVG-Maler; [Browser] U_{GS}, α, 10^{-16} korrekt. Ausrichtung links/mittig/rechts gibt es nur beim Objekt Text. Kein echtes LaTeX in Labels (dafür MathTex) |
| A3 | Teilbilder | **bestätigt** | `origin`, `title`, `show_axes` in der UI; Feld „axes“ ab zwei Axes (Z. 1444–1449); neues Objekt landet im gewählten Teilbild (Z. 857–861); UI-Test 14–15. Bei MathTex/Vector ist das Feld wirkungslos; `origin` nicht mit der Maus verschiebbar |
| A4 | Achsen erweitert | **bestätigt** | alle genannten Felder in der UI ([Browser]-Liste), Bode-Vorlage zeigt Dekaden. Nicht in der UI: `z_label`, `tick_size`, Teilstrich-Schritt |
| A5 | Parameter | **bestätigt** | Regler, „Name = Wert“, Namen in allen Ausdrücken; UI-Test 10–13. Kein Parameter-Film; min/max wirken erst nach erneutem Anwählen |
| A6 | SVG-Export | **bestätigt** | `export_svg` + `SvgPainter`; UI-Test 16, `test_figures` „SVG export is well-formed XML“. Immer voller 1920×1080-Rahmen, Text als `<text>` mit Systemschrift, nur Ruhebild |
| A7 | Szene per Link | **bestätigt** | Z. 2010–2015, UI-Test 17. Überschreibt die automatische Sicherung; keine Pfadbeschränkung (Sicherheitsrisiko, s. 3.3); nur eine Beispielszene, noch von keinem Artikel genutzt |
| B1 | DataCurve | **bestätigt** | Felder data (mehrzeilig), markers, smooth; Engine liest dieselben Schlüssel |
| B2 | Band | **bestätigt** | full_height/full_width, label_at top/center/bottom |
| B3 | Pfeile erweitert | **bestätigt** | LabeledArrow: double, dash, elbow none/hv/vh, thick; LoopArrow head:false |
| B4 | Stem | **bestätigt** | x/y/labels als Text-Listen, baseline |
| B5 | PointCloud | **bestätigt** | n, seed, distribution uniform/exp_y/exp_x, hollow |
| B6 | Tangente + Steigungsdreieck | **bestätigt** | triangle_dx, dx_label, dy_label; `test_figures` „semi-log tangent“ OK; Vorlage Diodenkennlinie |
| B7 | Shape mit Material | **bestätigt** | 10 Materialien in der Auswahl (inkl. custom), Vorlage Querschnitt NMOS |
| B8 | Ellipse und Bogen | **bestätigt** | Ellipse center/width/height; Bogen = LoopArrow ohne Spitze |
| B9 | Berechnete Punkte | **bestätigt** | Marker x_expr/func/func2/y_expr, Hilfslinien, label_pos (8); `test_figures` Schnittpunkt OK; Kennlinienfeld-Vorlage |
| B10 | Kennlinienscharen | **bestätigt** | values, labels; `test_figures` „CurveFamily … explicit values“ OK |
| C1 | TextBox | **teilweise** | Funktion vorhanden (shape rect/round/diamond/ellipse, Größe passt sich an), aber aus der Palette eingefügt ist der **Text unsichtbar** (Automatikfarbe = Füllfarbe) [Browser] |
| C2 | Brace | **bestätigt** | start/end/label/flip/size; keine Strichlinie |
| C3 | Mark | **bestätigt** | kind check/cross/strike |
| C4 | Table | **bestätigt** | cells, Zeilen-/Spaltenköpfe, highlight, brackets |
| D1 | Zweipole | **bestätigt** | 25 Arten in der Auswahl und im Engine-Quelltext; label/value/label_flip, current/current_at/current_reverse, voltage/voltage_reverse. Neue Bauteile farbig statt schwarz; auf normalem Axes verzerrt |
| D2 | Mehrpole und Blöcke | **bestätigt** | 25 Arten, rotation (Grad), flip, pins; Pin-Liste steht im Kopf von `circuit.py` (Z. 6–15) |
| D3 | Leitungen und Knoten | **bestätigt** | Wire route direct/hv/vh, dots; Node mit offset/dot. Nur per Texteingabe, kein Zeichnen mit der Maus, kein Fang (laut Doku selbst noch offen) |
| E1 | Vorlagen | **bestätigt** | 7 ET-Vorlagen in der Gruppe „Elektrotechnik · Vorlagen“, erzeugt von `tools/editor_vorlagen.py`; alle laden (UI-Test 1–9). „Einfügen“ ersetzt die ganze Szene |
| E2 | Tests | **bestätigt** | Dateien vorhanden; `editor_ui_test.py` hat genau 18 `check`-Aufrufe, heute 18/18 OK; `test_figures.py` und `test_contract.py` grün. Der UI-Test deckt Palette, Animation, PNG/Video, Dateispeichern und Verschieben nicht ab |

Nebenbefund zu `web/py/app.py`: gehört nicht zum Editor (der Editor lädt nur `canvas_painter.py` und `editor_backend.py`, `editor.js:43`); `app.py` ist eine fest programmierte Sinus-Demo für `main.js`.
