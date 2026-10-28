# Bestandsaufnahme Abbildungs-Editor, Teil A: 2D-Objekte, Beschriftung, Schaltpläne

Geprüft am 28.10.2026 im Repo `C:\Users\info\PycharmProjects\pythonanimation` (letzter Commit `75aeed1`). Im Repo wurde nichts geändert.

**Methode.** Ich habe vollständig gelesen: `web/engine/scene_model.py` (2D-Teile), `axes.py`, `plotting.py`, `figures.py`, `circuit.py`, `richtext.py`, `text.py`, `legend.py`, `geometry.py`, `simpleShape.py`, `svg.py`, `renderer.py`, `svg_painter.py`, `AnimObject.py`, `web/py/canvas_painter.py`, `web/py/editor_backend.py` sowie die relevanten Teile von `web/editor.js` (Katalog, Modell→Python, Eigenschaftsfeld, MathJax-Pfad, Export).
- Ausgeführt habe ich `tests/test_figures.py`, `tests/test_axes.py` und `tests/test_contract.py`; alle sind grün.
- Dazu kamen zwei eigene Sondierungsskripte, die die Engine in CPython ansprechen: `probe.py` und `probe2.py` im Scratchpad-Ordner.

Jede Aussage zu „geht“ oder „geht nicht“ ist durch Code (Datei:Zeile) oder einen Sondierungslauf belegt. Pfade ohne Präfix beziehen sich auf `web/`.

Status-Legende: **voll** = die Anforderung lässt sich mit Editor-Mitteln erfüllen; **teilweise** = es geht nur mit Lücken, Umwegen oder einem Fehler; **nein** = es geht nicht. Ein Sternchen (voll\*) heißt: Die Funktion ist da, hat aber einen bekannten Fehler (siehe §3).

---

## 0. Wie der Editor intern arbeitet

1. **Vom Editor zur Grafik.** Das Editor-Modell (JS) wird von `toPythonModel` in JSON übersetzt. `ModelScene.construct` baut daraus die Szene, `_build_object` die einzelnen Objekte. Gezeichnet wird im Browser von `CanvasPainter`, beim Export von `SvgPainter` (`editor.js:482-519`, `scene_model.py:1575-1674`, `editor_backend.py:10-18, 29-48`).
2. **Farben.** Jede Zeichenkette, die mit `#` beginnt, wird in RGB umgerechnet (`editor.js:466-471`).
3. **Teilbilder.** Zuerst werden alle `Axes` gebaut. Jedes andere Objekt wählt mit `on` sein Teilbild; ohne `on` landet es im ersten Axes (`scene_model.py:1605-1626`).
4. **Koordinaten.** Die Builder rechnen Datenkoordinaten mit `c2p` selbst um. Die klassenbasierten Typen (Line, Circle, Text, …) werden nach dem Bau mit `axes.place` auf die Achsen abgebildet (`scene_model.py:1297-1300`).
   - Ausnahme sind die `_WORLD_TYPES`: Axes, ThreeDAxes, Box, Cube, Sphere, Pyramid, **Vector, MathTex** und SVGMobject. Sie bleiben in **Weltkoordinaten** (`scene_model.py:366-367`).
5. **Stil-Props.** Die Stil-Props (`color, fill_color, fill_opacity, stroke_width, stroke_opacity, show_center, dash`, `scene_model.py:344`) werden vor dem Bau herausgelöst. Jeder Builder liest sie selbst.
   - Danach werden sie per `setattr` gesetzt, aber **nur am obersten Objekt** (`scene_model.py:1315-1317`). `dash` dagegen wird rekursiv weitergegeben.
   - Der Painter zeichnet jedes Blatt mit dessen eigenen Attributen (`renderer.py:29-41`).
6. **Defaults.** Beim Laden einer Szene füllt der Editor fehlende Props aus seinem Katalog auf (`editor.js:330-338, 1093`). Im Editor gelten also die **Katalog-Defaults**. Die Engine-Defaults greifen nur, wenn ein JSON direkt in Python gerendert wird, etwa in Tests. Wo beide abweichen, ist das unten vermerkt.
7. **Unbekannte Props.** Builder-Typen ignorieren sie still. Klassen-Typen (Text, Circle, Line, Legend, Rectangle, …) werfen einen `TypeError`; dann rendert **die ganze Szene** nicht und der Editor behält das letzte Bild (`scene_model.py:1296`, `editor_backend.py:39-40`). Sondierung: `Text` mit `rotation` ergibt TypeError, ebenso `Circle` mit `label`.
8. **Leinwand und Export.** Die Leinwand ist 16:9 und 8 Welteinheiten (WE) hoch, also etwa 14,22 WE breit (`constants.py:18-19, 31`). Der Export als SVG oder PNG hat **immer 1920×1080** und wird nicht zugeschnitten (`editor_backend.py:16`, `editor.js:2075-2090`).
9. **Zeichenreihenfolge.** Es wird in Einfügereihenfolge gezeichnet. Die Objektliste lässt sich in der Oberfläche **nicht umsortieren**; ziehbar sind nur die Animationen (`editor.js:1255-1331`).
   - `axes_on_top` steht im Editor standardmäßig auf aus (`editor.js:455`, `editor_backend.py:42`).

---

## 1. Objekttypen mit allen Props

**Gemeinsam für alle Objekte:**
- `color`, `fill_color`, `fill_opacity`, `stroke_width`, `stroke_opacity`, `show_center`, `dash`.
- `dash` versteht: `""` bzw. „solid“; „dashed“ = [10,7]; „dotted“ = [2,5]; oder eine freie Folge „an,aus,…“ in Pixeln (`scene_model.py:347-363`). Pfeilspitzen und Punkte bleiben durchgezogen, weil sie `_no_dash` tragen.
- Objektebene: `on` (Teilbild), `visible`, `children` (Ergebnisobjekte).

In den Tabellen steht „E:“ für einen abweichenden Engine-Default.

### 1.1 Achsen und Funktionen

**Axes** (`axes.py:71-81`, Katalog `editor.js:70-72`)

| Prop | Bedeutung | Default |
|---|---|---|
| `x_range`, `y_range` (`z_range`) | Datenbereich [min, max(, Schritt)]; ein dritter Eintrag setzt einen festen Tick-Schritt (nur bei linearer Achse, `axes.py:118-120`); die Oberfläche kann keinen dritten Eintrag anlegen (`editor.js:1399-1402`) | [-10,10] |
| `x_length`, `y_length` (`z_length`) | Bildgröße in WE | 7 |
| `origin` | Mitte des Teilbilds in WE | [0,0,0] |
| `title` | Teilbildtitel, oben links über dem y-Label, Größe `label_size` (`axes.py:234-238`) | "" |
| `x_label`, `y_label` | Achsentitel als Rich-Text; x am rechten Achsenende, y über der Achse (`axes.py:227-233`) | "x", "y" |
| `x_log`, `y_log` | logarithmische Achse | false |
| `arrows` | Pfeilspitzen an den positiven Enden | false |
| `x_axis_at` | „auto“ (bei y=0, in den Bereich geklemmt) oder „bottom“ | auto |
| `y_axis_at` | „auto“ oder „left“ | auto |
| `show_axes` | false = leerer Platzierungsrahmen | true |
| `show_ticks`, `show_numbers`, `x_numbers`, `y_numbers`, `show_labels`, `minor_ticks` | Schalter | true |
| `number_size`, `label_size` | Schriftgröße in px | 24, 34 |
| `axis_width` | Strichstärke von Achsen und Ticks | 4 |
| `x_color`, `y_color`, `z_color` | Achsenfarben | #000000 |
| `grid_x`, `grid_y`, `grid_z`, `grid_color`, `grid_width` | Gitter (durchgezogen, nicht strichelbar) | false, #000000, 1 |
| `tick_size` | Ticklänge, nur per JSON | 0.1 |

Einschränkungen der Achsen:
- **Tick-Zahlen** werden als `f"{v:g}"` gesetzt: mit Dezimalpunkt und für kleine Werte als „2e-06“ (`axes.py:10-12`, Sondierung).
- **Log-Achsen** beschriften nur Dekaden: „1“, „10“, „100“, danach „10^{k}“ (`axes.py:30-45`). Ein Tick-Schritt wird dort ignoriert (Sondierung).
- **Nicht vorhanden** sind: eigene Tick-Positionen oder -Texte, eine Rahmenbox, Achsen oben oder rechts, eine Achse bei frei wählbarem Wert und ein frei positionierbarer Achsentitel.
- Bei Kamera-Zoom gibt es einen Tick-Fehler (F9).

**FunctionGraph, eindimensional** (`scene_model.py:1199-1245`, `axes.py:314-341`, Katalog `editor.js:75`)

| Prop | Bedeutung | Default |
|---|---|---|
| `func` | Ausdruck in x (t und y sind Aliase); kommen x **und** y vor, wird daraus eine 3D-Fläche | "sin(x)" |
| `x_range` | Definitionsbereich; wird auf die Achse geklemmt, ein ungültiger Bereich fällt still auf die ganze Achse zurück (`axes.py:321-326`) | [-10,10] |
| `color`, `stroke_width`, `stroke_opacity`, `dash` | Linienstil | #59a0eb, 4, 1.0, "" |
| (`adaptive`, `res_*`, `fill_opacity`, `height_color`, `grid_*`) | nur für Flächen | – |

**Ausdruckssprache** (`scene_model.py:181-240, 264-298`):
- Funktionen: `sin cos tan exp log ln log10 log2 sqrt abs sinh cosh tanh arcsin arccos arctan sign`.
- Signale: `epsilon/step/u heaviside rect tri ramp si sinc`.
- Hilfsfunktionen: `max min clip floor ceil mod where`.
- Konstanten: `pi e j`.
- Schreibweise: `^` wird zu `**`; implizite Multiplikation wird ergänzt; `1e-15` gilt als eine Zahl.
- Szenen-Parameter sind als Namen verfügbar.

Verhalten am Rand: Die y-Werte werden auf den y-Bereich der Achse **beschnitten**, die Kurve endet dort (`scene_model.py:1233-1234`, `axes.py:328-334`). Auf einer log-y-Achse wird ein Wert ≤ 0 zur Lücke. Ohne Axes zeichnet der Graph in Weltkoordinaten (`simpleShape.py:91-104`). Fehler: F1.

**Area** (`scene_model.py:545-583`, Katalog `editor.js:77`)
- `func`; `func2` (leer = Basislinie y=0, auf einer log-Achse y_min).
- `x_min` 0, `x_max` 3.14159, `samples` 64.
- Stil: `color`, `fill_color`, `fill_opacity` 0.4, `stroke_width` 0, `dash`.
- Werte werden in den y-Bereich geklemmt.
- Nur Ausdrücke sind möglich; man kann nicht auf ein vorhandenes Graph-Objekt verweisen.

**TangentLine** (`scene_model.py:1102-1183`, Katalog `editor.js:81`)
- `func`, `x0` 1, `secant` false, `x1` 2.
- `half_len` 2, gemessen in Plot-Einheiten; auf einer log-x-Achse also in **Dekaden** (`:1111-1149`).
- `show_point` true, `show_slope` false (Text „m = %.3g“ mit Punkt, `:1165`).
- `triangle_dx` 0, `dx_label` „\Delta x“, `dy_label` „\Delta y“, `font_size` 26, `color` #111111, `stroke_width` 3, `dash`.
- Die Linie wird nicht an der Achse abgeschnitten.

**CurveFamily** (`scene_model.py:775-854`, Katalog `editor.js:85`)
- `func` „sin(k*x)/k“, `param` „k“, `p_min` 1, `p_max` 5, `count` 5.
- `values` "": eine Zahlenliste per Regex, die den Bereich p_min…p_max ersetzt (`:810`).
- `labels` "": durch „;“ getrennt, Rich-Text.
- `x_min` -6, `x_max` 6 (E: Achsenbereich), `samples` 120.
- `fade` true: aufhellen bei kleinem p.
- `show_limit` false, `limit_func` "": Grenzkurve, immer fast schwarz mit stroke_width+2 (`:845-847`).
- `font_size` 24, `color` (**eine** Grundfarbe für alle Kurven), `stroke_width` 3, `dash`.
- Beschriftungen nur am **rechten Ende**, +0,15 WE versetzt (`:851-853`).
- Die Kurven werden in den y-Bereich **geklemmt** statt geschnitten (F2).

**ParametricCurve** (`:693-772`, Katalog `:88`): `fx` „cos(t)“, `fy` „sin(t)“, `t_min` 0, `t_max` 2π, `samples` 160, `show_arrow` true, `point_at` "", `show_tangent`, `show_normal` (Normale immer orange), `color`, `stroke_width` 4, `dash`.

**PolarCurve** (`:600-651`, Katalog `:90`): `func` „1+cos(theta)“, `theta_min` 0, `theta_max` 2π, `samples` 200, `show_arrow` true, Stil.

**DataCurve** (`figures.py:72-116`, Katalog `editor.js:93`)
- `data`: Paare „x y“ je Zeile oder „x,y;x,y“. Das Komma ist Trennzeichen, ein **Dezimalkomma ist deshalb unmöglich**: „0,7 1,2“ wird zu (0,7),(1,2) (Sondierung).
- `markers` false, `marker_radius` 0.06 (Welt), `smooth` false (Bézier durch die Punkte).
- Stil: `color`, `stroke_width` 4, `dash`.
- Auf einer log-Achse wird ein Wert ≤ 0 zur Lücke. Kein Abschneiden am Teilbild.

**Band** (`figures.py:119-152`, Katalog `:96`)
- `x_min` 1, `x_max` 2, `y_min` 0, `y_max` 1.
- `full_height` true (E: false), `full_width` false.
- `label` "", `label_at` top|center|bottom, `font_size` 26.
- Stil: `color`, `fill_color`, `fill_opacity` 0.18, `stroke_width` 0, `dash`.
- Nur achsparallele Rechtecke, nur in einem Teilbild.

**Stem** (`figures.py:155-182`, Katalog `:98`): `x` „1;2;3;4“, `y` „1;0.5;0.25;0.125“, `labels` "", `baseline` 0 (auf log-Achse y_min), `markers` true, `marker_radius` 0.07, `font_size` 24, Stil.

**PointCloud** (`figures.py:185-223`, Katalog `:102`)
- `n` 60 (E: 50); `x_min` -2, `x_max` 2, `y_min` 0, `y_max` 2 (E: -1…1).
- `seed` 1, `distribution` uniform|exp_y|exp_x, `decay` 0.5.
- `radius` 0.05 (Welt), `hollow` false, `color`, `stroke_width` 2.
- Punkte werden nur zufällig gesetzt; ein regelmäßiges Raster gibt es nicht.

**NumberLine** (`scene_model.py:654-690`, Katalog `:104`): `x_min` -5, `x_max` 5, `step` 1, `length` 10 (Welt), `center`, `tick_labels` true, `decimals` 0 (Punkt, `:689`), `font_size` 24, Stil. **Nur waagerecht**; eine unbekannte `rotation` wird still ignoriert.

**Legend** (`legend.py:47-65`, Katalog `editor.js:107`)
- `labels` „f(x);g(x)“.
- `colors` "": Hex-Werte **ohne #**, durch „;“ getrennt; leer = automatische Palette.
- `position` [-5,4,0]; `row_gap` 0.8, `swatch_len` 0.9, `gap` 0.35 — **alle in Dateneinheiten**.
- `font_size` 26, `color` (Textfarbe) #111111, `stroke_width` 6.
- Je Eintrag nur ein durchgezogener Linienstrich: keine Strichelung, keine Marker, kein Rahmen, keine Kopplung an die Kurvenfarben (F4).

**Riemann** (`scene_model.py:1246-1248`, `axes.py:502-517`): `func`, `count` 8, `color`, `fill_opacity`. Nur über eine Vorlage oder JSON, nicht in der Palette; die Rechtecke beginnen immer bei y=0.

**VectorField / ScalarField** (`:955-1001`, `:857-944`): 2D-Pfeilgitter (Presets, `fx`/`fy`, `nx`, `ny`, `scale`, `normalize`, `max_len`, `color_by_mag`) bzw. Heatmap mit Höhenlinien (`levels`, `show_heat`, `show_contours`, `gradient_at`). Für R4–R8 nicht zentral und in `web/tests` nicht getestet.

### 1.2 Geometrie

| Typ | Props (Default) | Koordinaten / Hinweis |
|---|---|---|
| Dot (`scene_model.py:1249-1254`, `editor.js:55`) | `center`, `radius` 0.08 | Mitte in Daten, Radius in Welt, bleibt also rund |
| Line (`simpleShape.py:25-28`, `:56`) | `start`, `end`, `dash` | Daten; auf log-Achsen **krumm** (F8) |
| Circle (`:12-15`, `:54`) | `center`, `radius` 1 | Daten; auf ungleich skalierten Achsen eine Ellipse |
| Rectangle / Square (`:74-88`, `:57-58`) | `center`, `width` 2, `height` 1 / `side` | Daten, nicht drehbar |
| Ellipse (`:58-64`, `:60`) | `center`, `width` 2, `height` 1 | Daten, nur achsparallel |
| Polygon / Triangle (`:31-38, 67-71`) | `vertices` [[x,y,z],…], `closed` | nur per JSON, nicht in der Palette |
| Vector (`threed.py:129-156`, `:61`) | `end` [2,1,0], `start`, `color`, `stroke_width` | **Weltkoordinaten**, ignoriert das Teilbild (Sondierung) |
| Shape (`figures.py:342-367`, `:162`) | `points` „x,y;…“, `closed` true, `label` (im Schwerpunkt), `material` custom\|n\|p\|n+\|p+\|oxide\|poly\|metal\|depletion\|substrate, `font_size` 24, `fill_opacity` 0.5, `stroke_width` 2, `dash` | Daten; bei Materialien wird die Deckkraft auf ≥ 0,9 gesetzt (`:358-359`); keine Schraffur |
| Mark (`figures.py:309-332`, `:159`) | `center`, `kind` check\|cross\|strike, `size` 0.5, `width`/`height` 1, `color` #2ca02c, `stroke_width` 5 | – |

### 1.3 Beschriftung und Annotation

**Text** (`text.py:6-17`, Katalog `editor.js:134`)
- `text` (Rich-Text, §2 R5), `position` (Datenkoordinaten), `font_size` 40 (E: 28), `align` center|left|right, `color`.
- **Nicht vorhanden**: Drehung, vertikale Ausrichtung (immer mittig, `canvas_painter.py:81`), Hintergrund. Die Schrift ist fest: `sans-serif` auf der Leinwand, aber `system-ui,…` im SVG (`canvas_painter.py:83/97`, `svg_painter.py:24`).

**DecimalNumber** (`text.py:20-39`): `value`, `position`, `font_size` 40, `decimals` 2, `prefix`, `suffix`. Dezimalpunkt; in der Oberfläche nur als Ergebnis-Kind.

**MathTex** (`svg.py:183-220`, Katalog `editor.js:135`)
- `tex` „\frac{a}{b}“: wird im Browser per MathJax zu Glyphen.
- `height` 1.2: Die **ganze Formel** wird auf diese Höhe normiert.
- `position` [0,0,0] in **WE**, `color`.
- Nur in der Engine (per JSON): `fill_opacity` und `scale` (gleichmäßige Größe).

**TextBox** (`figures.py:240-270`, Katalog `:138`)
- `text`, `center`.
- `width`/`height` 0 = an den Text angepasst; die Breite wird nur geschätzt (0,56·font_size je Zeichen, `figures.py:51-54`).
- `shape` rect|round|diamond|ellipse, `padding` 0.25, `font_size` 28.
- `color` gilt für Rand **und** Text; `fill_color` #fff, `fill_opacity` 1, `stroke_width` 3, `dash`.

**Marker** (`scene_model.py:456-515`, Katalog `:144`)
- `point` [1,1,0], `label` „P“, `label_pos` ne|nw|se|sw|n|s|e|w.
- `show_guides` true (E: false), `guide_dash` „5,5“. Die Hilfslinien sind fest grau (0,55) und 1,5 px stark (`:497-500`).
- Berechnete Lage: `x_expr`, `func`, `func2`, `y_expr`.
- `radius` 0.08, `font_size` 28, `color`.

**Measure** (`:518-542`, Katalog `:147`)
- `start`, `end`, `label` „d“, `offset` 0 (Verschiebung senkrecht, in WE), `font_size` 28, `color`, `stroke_width` 4, `dash`.
- Die Spitzen sind 3D-Kegel aus `Vector`; ihre Größe (≤ 0,28 WE) ist nicht einstellbar.

**LabeledArrow** (`:1004-1064`, Katalog `:151`)
- `start`, `end`, `label` „F“, `label_at` mid|end, `double` false, `elbow` none|hv|vh.
- `thick` 0: > 0 ergibt einen gefüllten Mengenpfeil; die Breite ist eine **absolute** Zahl in WE.
- `head_size` 0.3, `font_size` 28, `color`, `stroke_width` 4, `dash`.
- Das Label steht immer links in Pfeilrichtung (Sondierung).

**LoopArrow** (`:1074-1099`, Katalog `:155`): `center`, `radius` 0.8 (Welt), `start_angle` 30, `end_angle` 320 (Grad), `head` true, `label` "" (immer im Mittelpunkt), `font_size` 28, Stil.

**Brace** (`figures.py:273-306`, Katalog `:157`): `start`, `end`, `label`, `flip` false, `size` 0.3, `font_size` 26, `color`, `stroke_width` 3. Das Label steht **zentriert** jenseits der Klammerspitze (F6).

**Table** (`figures.py:370-430`, Katalog `:165`)
- `cells` „1,2;3,4“: Zeilen durch „;“, Zellen durch **„,“** getrennt.
- `row_labels`, `col_labels` (durch „;“).
- `highlight` „r,c;…“ (0-basiert), `brackets` false.
- `cell_w` 1.2, `cell_h` 0.6 (WE, für alle Zellen gleich).
- `position` = linke obere Ecke in Daten, `font_size` 24, `color`.
- `fill_color` #f5c542 und `fill_opacity` 0.35 gelten für die Hervorhebung; `stroke_width` 1.5.

### 1.4 Schaltplan

**Component** (`circuit.py:75-207`, Katalog `editor.js:179`)
- `kind`, 25 Arten (`circuit.py:68-72`):
  - Widerstände: resistor, resistor_nl, resistor_var.
  - Kapazitäten und Spule: capacitor, capacitor_var, inductor.
  - Dioden: diode, zener, led.
  - Quellen: vsource, vsource_dc, isource, ac_source.
  - Gesteuerte Quellen: vcvs, vccs, cccs, ccvs.
  - Sonstiges: switch, lamp, ammeter, voltmeter, fuse, nullator, norator, wire.
- `start`, `end` (Daten), `label` „R_1“, `value` "" (unter dem Namen gestapelt), `label_flip`.
- `current` "", `current_at` start|end, `current_reverse`.
- `voltage` "", `voltage_reverse`.
- `size` 1.0, `font_size` 26, `color`, `stroke_width` 3.
- `dash` wirkt, kommt aber **nur per JSON** hinein, weil das Feld im Katalog fehlt.

**Device** (`circuit.py:218-368`, Katalog `:184`)
- `kind`, 25 Arten (`:213-215`).
- `center`, `rotation` 0 (Grad, beliebig), `flip` false (Spiegelung an der lokalen x-Achse).
- `label` „T_1“: Die Position ist je Art fest (`label_at`, `:252` ff.).
- `pins` true: Die Anschlussnamen sind fest, z. B. B/C/E, G/D/S, 1/1'/2/2', A/G/K (`:247-249`).
- `size` 1.0, `font_size` 24 (Anschlussnamen 0,85×), `color`, `stroke_width` 3.
- Innenflächen von opamp, Filter und Mischer sind fest weiß.

**Wire** (`circuit.py:372-401`, Katalog `:187`): `points` „x,y;…“, `route` direct|hv|vh, `dots` "" | „all“ | „0;2“ (Indizes der **angegebenen** Punkte), `dot_radius` 0.07, `color`, `stroke_width` 3, `dash`.

**Node** (`circuit.py:404-418`, Katalog `:189`): `center`, `label` „K_1“, `offset` [0.25,0.25,0] (Welt), `dot` true, `radius` 0.08, `font_size` 26, `color`.

### 1.5 Parameter und Sonstiges

- **Parameter** (`editor.js:170`, `scene_model.py:1595-1604`): `name` „p“, `value` 1, `min` 0, `max` 5, `step` 0.1 (Schieberegler).
  - Der Name gilt in allen **Ausdrücken** (`func`, `func2`, `x_expr`, `fx`, …), nicht in Zahlenfeldern wie Positionen oder Bereichen.
  - Reservierte Namen werden still ignoriert (F11).
- **ValueTracker(value)** gibt es nur per JSON.
- **SVGMobject** (`svg.py:147-158`) gibt es nur per JSON, in Weltkoordinaten. Er liest nur `<path d>`; Bögen (A) werden übersprungen (`svg.py:123-124`), `transform`-Attribute und Dateifarben ignoriert.
- 3D-Typen (ThreeDAxes, Box, Cube, Sphere, Pyramid) sind nicht Teil dieser Prüfung.

---

## 2. Anforderungen R4–R8

### R4 — 2D-Diagramme

| Bedarf | Status | Beleg | Was fehlt / Hinweis |
|---|---|---|---|
| Mehrere Teilbilder nebeneinander, Titel „(a)“ | **voll** | `axes.py:97-98` (origin), `:234-238` (title); `scene_model.py:1605-1626` (on); `editor.js:855-861, 1443-1449`; Test „panel binding“ grün | Platzierung von Hand über `origin`/`length` im gemeinsamen 16:9-Rahmen; keine automatische Anordnung, keine automatischen Buchstaben, keine gekoppelten Achsen, keine Bildunterschrift; Export immer 1920×1080 ohne Zuschnitt (`editor_backend.py:16`) |
| Funktionsgraphen mit exp() und benannten Parametern | **voll** | `exp` in `_SAFE_NAMES` (`scene_model.py:181-183`); Parameter `:1595-1604, 244-248`; Sondierung `U_T`, `IS` und `Ut` funktionieren | Benannt werden kann nur über `Parameter`-Objekte (global, mit Regler). Namen wie `e`, `j`, `u`, `step`, `rect`, `max`, `ln` werden still ignoriert und liefern eine falsche oder leere Kurve (F11). `xexp(x)` wird nicht zerlegt, also `x*exp(x)` schreiben |
| Kurvenschar mit festen Parameterwerten und Labels am Kurvenende | **teilweise** | `CurveFamily` `values`/`labels` (`scene_model.py:810-813, 833-834, 851-853`) | (1) **Klemmt** Werte außerhalb des y-Bereichs auf den Rand: Es entstehen waagerechte Linien am oberen bzw. unteren Rand, und die Labels liegen übereinander (F2). (2) Nur eine Grundfarbe, standardmäßig mit `fade` aufgehellt. (3) Labels nur am rechten Ende, ohne Versatz. (4) `values` mit Dezimalkomma wird falsch gelesen (F3). Umweg: je Kurve ein `FunctionGraph` (schneidet korrekt ab) plus `Text` |
| Logarithmische Achsen | **voll** | `axes.py:87-93, 124-135, 271-281, 335-338`; Tests „log x …“ grün | Beschriftung nur 1/10/100 und dann „10^{k}“ (`axes.py:40-45`); keine Werte wie 1-2-5 oder „100 k“; ein Tick-Schritt wird auf der log-Achse ignoriert; Unterteilungen fallen weg, wenn eine Dekade kürzer als 0,6 WE ist |
| Achsentitel mit Einheit „U_CE in V“ | **voll** | `x_label`/`y_label` als Rich-Text (`axes.py:227-233`); Sondierung: „U_{CE} in V“ steht am x-Achsenende | Lage fest: x rechts vom Achsenende, y zentriert über der Achse. Kein Titel mittig unter der Achse, keine Drehung |
| Tick-Labels mit Dezimalkomma | **nein** | `axes.py:10-12` (`f"{v:g}"`); ebenso `NumberLine` `:689`, `DecimalNumber` `text.py:34`, TangentLine `:1165` | Kein Schalter für das Format. Umweg: `x_numbers`/`y_numbers:false` und je Tick ein eigenes `Text`. Zusätzlich schreibt der Editor kleine Werte als „2e-06“ |
| Punkt im Schnittpunkt zweier Kurven | **voll** | `Marker` mit `func`+`func2` sucht den Vorzeichenwechsel nahe `point.x` (`scene_model.py:405-449, 473-477`); Tests grün, auch auf log-y (Sondierung) | Nur für zwei **Ausdrücke** in x, also nicht mit `DataCurve` oder `CurveFamily`. Eine Berührung ohne Vorzeichenwechsel wird nicht gefunden. Ausdrücke müssen doppelt gepflegt werden, weil kein Verweis auf das Graph-Objekt möglich ist |
| Strichlinien | **voll\*** | `dash` an allen Objekten (`scene_model.py:347-363, 1315-1319`; `AnimObject.py:123-130`); Tests „dash …“ grün | Das Oberflächenfeld fehlt bei Component, Device, Brace, Node, Table, Legend und Mark (nur per JSON). Das Achsengitter lässt sich nicht stricheln. Ein gestrichelter **Measure** wird fehlerhaft gezeichnet (F7) |
| Gefüllte Bänder und Bereiche | **voll** | `Band` (`figures.py:119-152`), `Area` unter oder zwischen Kurven (`scene_model.py:545-583`), `Shape` (Polygon) | Keine Schraffur. Ein Band wirkt nur in einem Teilbild; ein Streifen über alle Teilbilder hinweg ist nicht möglich |
| Freie Textannotation in Datenkoordinaten | **voll** | `Text`, abgebildet über `axes.place` (`scene_model.py:1297-1300`); Sondierung: Text im Teilbild p2 landet korrekt | **MathTex** und **Vector** ignorieren das Teilbild (F12). Keine Drehung, keine vertikale Ausrichtung |
| Gerade Pfeile und Doppelpfeile zwischen zwei Punkten mit Label | **voll** | `LabeledArrow` (`double`, `label_at`) `:1004-1064`; `Measure` (Maßpfeil mit `offset`) `:518-542` | Die Label-Seite ist durch die Pfeilrichtung festgelegt (links der Richtung), es gibt kein `label_flip`. Beim Doppelpfeil hilft Start/Ende-Tausch, beim einfachen Pfeil nicht. Ein Pfeil auf Basis von `Vector` steht in Weltkoordinaten |
| Legenden | **teilweise** | `legend.py:47-65`; Sondierung: auf log-y liegen die Zeilen bei y = -146 WE, auf y∈[0;0,01] bei -398 WE | Zeilenabstand und Strichlänge sind in Dateneinheiten (F4). Nur durchgezogene Linienstriche; Farben werden von Hand eingetragen (Hex ohne #); kein Rahmen. Umweg: die Legende auf ein eigenes, 1:1 skaliertes Teilbild mit `show_axes:false` legen |
| Farben und Linienstärken pro Objekt | **voll\*** | `color`/`stroke_width` an allen Typen; Achsen: `axis_width`, `x_color` | Ein **FunctionGraph, der in mehrere Stücke zerfällt** (Polstelle, Verlassen und Wiedereintritt in den y-Bereich), verliert Farbe, Stärke und Deckkraft und wird in Standardblau mit 4 px gezeichnet (F1, Sondierung tan(x) und 4·sin(x)). Bei einer `CurveFamily` geht nur eine Farbe |
| Kurve auf einen Teilbereich beschränken | **voll** | `FunctionGraph.x_range` (`axes.py:321-326`); `CurveFamily`/`Area` `x_min`/`x_max` | Ein ungültiger Bereich (min ≥ max) fällt still auf die ganze Achse zurück |
| Gerade durch zwei Datenpunkte bzw. Verlängerung (Extrapolation) | **teilweise** | `Line` (Daten), `DataCurve` mit 2 Punkten, `TangentLine secant:true` (`:1137-1145`) | Es gibt kein Objekt „Gerade durch P1, P2, verlängert um Δ“. Eine Verlängerung geht nur über eine von Hand ausgerechnete Geradengleichung in einem `FunctionGraph` mit `x_range`, oder über eine Sekante, wenn beide Punkte auf einer Funktion liegen. Eine `Line` wird auf log-Achsen krumm (F8); dort `DataCurve` nehmen. Nichts wird am Teilbild abgeschnitten, eine Verlängerung ragt also heraus |

### R5 — Beschriftungen

Zwei getrennte Systeme:

**(a) Leichtgewichtige Formel-Labels** (`richtext.py`)
- Sie gelten in **jedem** Text-Label: Text, Achsentitel, Tick-Zahlen, Teilbildtitel sowie Labels von Bauteilen, Pfeilen, Markern, Klammern, Tabellenzellen, Legende und TextBox.
- Zerlegt wird erst beim Zeichnen (`canvas_painter.py:78-104`, `svg_painter.py:68-93`). Hochgestellte Teile werden auf 0,7× verkleinert und um 0,3 bzw. 0,4 versetzt (`richtext.py:42-53`).
- Beim SVG-Export entstehen `<text>`/`<tspan>`-Elemente, das Ergebnis hängt also von der Schrift des Betrachters ab.

**(b) MathTex**
- Echter LaTeX-Satz: MathJax `tex-svg` 3.2.2 aus dem CDN (`editor.html:9-11`) erzeugt Glyphenpfade (`editor.js:1838-1902`). Daraus baut `MathTex` in Python Bézier-Flächen (`svg.py:183-220`), die als gefüllte Pfade gezeichnet und exportiert werden, unabhängig von der Schrift.
- Ohne geladenes MathJax (offline, CPython-Tests) gibt es keine Glyphen.
- **Platzierung nur in Weltkoordinaten** (`scene_model.py:366-367`).
  - Die Oberfläche bietet trotzdem das Teilbild-Feld an (`editor.js:1444, 1480`), das aber nichts bewirkt (Sondierung: MathTex auf p2 bleibt bei Welt (0,5; 0,5)).
  - Im üblichen Schaltplan-Teilbild (x_range [-7,7], x_length 14, y [-4,4], y_length 8, origin 0) sind Daten- und Weltkoordinaten gleich. Dort ist MathTex frei platzierbar.
  - In Diagrammen muss man die Weltposition selbst ausrechnen: origin + (x−x_min)/(x_max−x_min)·x_length − x_length/2.
- **Nicht als Label verwendbar**: weder in Component, Device, Achsen, Pfeilen noch in Tabellen.
- Die Größe über `height` normiert jede Formel einzeln. Zwei MathTex mit gleicher `height` haben deshalb verschieden große Glyphen, sobald eine einen Bruch enthält. Der Parameter `scale` (gleichmäßig, `svg.py:192, 215-216`) fehlt im Katalog (`editor.js:135`) und geht nur per JSON.
- `\color{}` wird beim Glyphen-Auslesen nicht übernommen; nach einem Fehler wird ohne Farbe erneut gerendert (`editor.js:1881-1883`). Es gibt nur eine Farbe pro Formel.

| Bedarf | Status (leicht / MathTex) | Beleg | Hinweis |
|---|---|---|---|
| Tiefstellung | voll / voll | `richtext.py:96-117`; Test `U_{GS}` grün | Ein Zeichen oder eine `{…}`-Gruppe, verschachtelbar |
| Hochstellung | voll / voll | dto.; Test `e^{U/U_T}` grün | – |
| Griechische Buchstaben | voll / voll | `richtext.py:20-27` | Fehlend: `\varrho`, `\varsigma`, `\Upsilon` (erscheinen als Name). `\mu` wird zum Mikrozeichen U+00B5 |
| Brüche | **nein** / voll | Sondierung: `\frac{a}{b}` wird zu „fracab“ (`richtext.py:135-141, 144-146`) | Leicht nur als „a/b“. Ebenso wirkungslos: `\sqrt{…}` (nur „√“ ohne Balken), `\underline` (komplexe Größen!), `\hat`, `\vec`, `\overline`, `\left`/`\right` erscheinen als Name im Text |
| `\mathrm` | voll (wirkungslos) / voll | `richtext.py:40, 129-134` | Leicht ist **alles** aufrecht und serifenlos. Kursive Formelzeichen nach DIN gibt es nicht, auch kein Fett (`\mathbf` wird ignoriert) |
| Text und Formel gemischt | voll / voll | `$` wird entfernt (`richtext.py:144`) | „Arbeitsgerade $U_{CE}$“ funktioniert |
| Dezimalkomma | **teilweise** / voll | in freiem Text ja | Nicht in Tabellenzellen (F5), nicht in Tick-Zahlen, nicht in Zahlenlisten (`values`, `data`, `x`/`y` von Stem, `highlight`) |
| Schriftgröße | voll / über `height` | `font_size` je Objekt; Achsen `number_size`/`label_size` | Bei zusammengesetzten Objekten gilt eine Größe für alle Labels (Pins 0,85×) |
| Farbe | voll / voll | `color` | Bei Component, Device, Pfeil und TextBox ist die Label-Farbe gleich der Symbolfarbe und nicht getrennt einstellbar |
| Ausrichtung | **teilweise** / – | `Text.align` (`text.py:16`, `editor.js:1343`); bei mehrzeiligem Text wird jede Zeile ausgerichtet (Sondierung) | Vertikal immer mittig; keine Drehung (TypeError); die Labels anderer Objekte werden automatisch ausgerichtet |
| Zeilenumbruch | voll / – | `\\` (`richtext.py:155`) | Achtung: Ein unbekannter Befehl, der mit `n` beginnt (`\not`, `\neg`), wird zum Zeilenumbruch (F10) |

### R6 — Schaltpläne

| Bedarf | Status | Beleg | Was fehlt / Hinweis |
|---|---|---|---|
| npn-Symbol mit Anschlussnamen | **voll** | `circuit.py:253-262`; Anschlüsse B(-1,0), C(0.5,1), E(0.5,-1)·size (`:6-9`) | Die Namen sind fest „B/C/E“ (`pins` nur an/aus); umbenennen geht nur über `pins:false` plus `Text`. Kein Kreis um das Symbol |
| Widerstand, Diode, Kondensator, Spannungsquelle | **voll** | `circuit.py:100-153` (Rechteck; gefülltes Dreieck mit Strich; zwei Platten; Kreis mit Linie längs nach DIN) | Die Polarität einer Quelle (+/−) ist im Symbol nicht darstellbar, nur über Zählpfeile |
| Spannungsgesteuerte Stromquelle (Raute) mit beliebigem Label | **voll** | `vccs` `circuit.py:154-160`; Labels werden nicht zerlegt (Sondierung „I_C(U_{BE},U_{CE})“, „S\cdot u_{be}“ korrekt) | Der Pfeil in der Raute zeigt von start nach end; zum Umdrehen start und end tauschen |
| Spannungs- und Strompfeile mit Labels | **voll** | `Component.voltage` (Pfeil parallel auf der Gegenseite des Namens, `:195-206`); `current` (Spitze auf der Zuleitung, `:185-194`); frei: `LabeledArrow`; Strompfeil auf einer Leitung: `Component kind:"wire"` + `current` (Sondierung) | Abstand und Länge des Spannungspfeils sind fest (76 % der Spanne); keine gebogenen Zählpfeile (außer LoopArrow); die Lage des Strompfeils ist nur start oder end |
| Offene Klemmenkreise | **voll** | `Device kind:"terminal"`, weiß gefüllt (`:350-352`) | Das Label steht fest darüber |
| Knotenpunkte | **voll** | `Wire.dots`, `Node`, `Device kind:"node"` | – |
| Leitungen mit Ecken | **voll** | `Wire` mit Eckpunkten bzw. `route` hv/vh (`:372-401`) | Kein Einrasten an Gitter oder Winkel, kein Brückenbogen bei Kreuzungen |
| Einzelne Elemente grau | **voll** | `color` je Objekt (Sondierung: #999999 im SVG) | Grau färbt auch das Label. Strichelung bei Component/Device nur per JSON. `stroke_opacity` wirkt bei Bauteilen **nicht** (F13) |
| Drehen und Spiegeln | **voll** | `Device`: `rotation` (beliebig), `flip` (`:223-237`); `Component` über die Lage von start und end | Spiegeln nur an der lokalen x-Achse; links-rechts = `flip` + 180°. Labels bleiben waagerecht |
| Größen und Label-Platzierung | **teilweise** | `size`, `font_size`, `label_flip` (Component), `offset` (nur Node) | Kein Versatz für Device-Labels (eine Prop `label_offset` wird still ignoriert, Sondierung) und keiner für Spannungspfeile |

Weitere Symbole: npn, pnp, NMOS in 4 Varianten, **PMOS in 3 Varianten** (es gibt kein `pmos_dep`), JFET, OPV, Zweitor, Röhre, Funkblöcke. Es fehlen gekoppelte Spulen, Schottky- und Fotodiode, Lautsprecher und ein Phasenschieber.

### R7 — Schemazeichnungen

| Bedarf | Status | Beleg | Was fehlt / Hinweis |
|---|---|---|---|
| Rechtecke und Polygone für Halbleitergebiete mit Füllung (n, p, Raumladungszone) | **voll** | `Shape.material` (`figures.py:335-367`), `Rectangle`, `Band` | Die Materialfarben sind fest, bei Materialien ist die Deckkraft ≥ 0,9. Keine Schraffur, kein Verlauf |
| Teilchen (Elektronen, Löcher) | **voll** | `PointCloud` (gefüllt/hohl, Seed, `figures.py:185-223`); einzeln: `Dot`, `Circle` mit fill_opacity 0 | Regelmäßige Anordnungen (Ionengitter) gehen nur Punkt für Punkt; „⊕/⊖“ als Unicode-`Text` |
| Pfeile | **voll** | `LabeledArrow` (auch geknickt oder breit), `LoopArrow` | – |
| Textkästen | **voll** | `TextBox` | Die Breite wird nur geschätzt |
| Bänderdiagramm aus stückweisen Kurven | **voll** | `FunctionGraph` mit `where`/`clip`/`min`/`max` (`scene_model.py:236-240`), `DataCurve`, `Line`, `Area` zwischen zwei Kurven | Die Stückgrenzen müssen von Hand formuliert werden; Niveaustriche als einzelne `Line`; Beschriftungen als `Text` |
| Konzentrationsprofil als Gerade zwischen zwei Endwerten, mit schattierten Bereichen | **voll** | `DataCurve` „x0 c0\nx1 c1“; Schattierung über `Band` oder `Shape` (Eckpunkte über `c2p` abgebildet) | Auf einer log-Achse `DataCurve` statt `Line` nehmen (F8); `Area` braucht einen Ausdruck |
| Senkrechte „Potentialleiter“ (drei Punkte auf einer senkrechten Achse, Abstandspfeile oder Klammern mit Label) | **teilweise** | zusammensetzbar aus `Line` + `Dot`/`Marker` + `Measure`/`Brace` + `Text` | Kein eigenes Objekt; `NumberLine` nur waagerecht. Das Label einer **senkrechten** `Brace` ist zentriert und überdeckt bei längerem Text die Klammer (F6, Sondierung). Die Label-Seite von `Measure` hängt von der Richtung ab |

### R8 — Tabellen in Abbildungen

| Bedarf | Status | Beleg | Was fehlt |
|---|---|---|---|
| Tabelle in der Abbildung | **teilweise** | `Table` (`figures.py:370-430`) | (1) Das Komma trennt die Zellen: **Dezimalkomma und `\,` zerlegen die Zelle** (Sondierung: „0,7 V“ wird zu „0“ | „7 V“, „1\,k\Omega“ zu „1\“ | „k\Omega“). (2) Alle Zellen gleich breit und hoch (`cell_w`/`cell_h`), keine Breite je Spalte, keine automatische Breite. (3) Alles zentriert, keine Ausrichtung je Spalte. (4) Kopfzeile und Kopfspalte haben **keine Gitterlinien** (nur der Datenblock, `:412-418`). (5) Keine verbundenen Zellen, keine Farbe je Zelle, nur eine Hervorhebungsfarbe. (6) Textfarbe = Linienfarbe. Umweg: ein Raster aus `TextBox`-Objekten |

---

## 3. Gefundene Fehler und Auffälligkeiten (alle nachgeprüft)

| Nr. | Befund | Beleg | Wirkung |
|---|---|---|---|
| F1 | Ein mehrteiliger FunctionGraph ignoriert Farbe, Stärke und Deckkraft | `axes.plot` ohne Farbe (`scene_model.py:1243`); die Stücke erhalten die Standardfarbe (`plotting.py:116-123`); Stil nur am Elternobjekt (`:1315-1317`); Painter je Blatt (`renderer.py:29-41`) | tan(x): 5 Stücke in Blau mit 4 px statt Rot mit 9 px; 4·sin(x) auf y∈[−3,3]: ebenso (Sondierung) |
| F2 | CurveFamily klemmt statt zu schneiden | `scene_model.py:816-819, 824` | Waagerechte Linien am Rand (82 bzw. 193 Kontrollpunkte auf der Oberkante); Labels übereinander; auf log-y Linie entlang der x-Achse |
| F3 | `values` liest Dezimalkomma falsch | Regex `scene_model.py:810` | „2;2,5;3“ ergibt 2, 2, 5, 3 (vier Kurven) |
| F4 | Legende in Dateneinheiten | `legend.py:56-63` + `axes.place` | Auf log-Achsen und bei nicht 1:1 skalierten Achsen unbrauchbar (Zeilen bei −146 bzw. −398 WE) |
| F5 | Tabellenzellen werden am Komma getrennt | `figures.py:375` | Dezimalkomma und `\,` zerlegen die Zelle und verschieben die Spalten |
| F6 | Label einer senkrechten Brace überlappt | `figures.py:301-305` (zentriert) | „U_{BE} = 0,7 V“ reicht von x −1,37 bis −0,18, die Klammer von −0,60 bis 0,00 |
| F7 | Gestrichelter Measure | zwei gegenläufige Schäfte (`scene_model.py:533-534`) | Zwei gestrichelte Pfade übereinander, deren Muster an entgegengesetzten Enden beginnen; die Lücken verschwinden dadurch teilweise |
| F8 | `Line` auf log-Achsen krumm | Bézier-Stützpunkte werden einzeln abgebildet (`axes.py:303-312`) | Stützpunkte (−4,−2,5), (−1,33; 2,1), (1,33; 2,35), (4; 2,5): weder gerade noch eine richtige Exponentialkurve |
| F9 | Ticks bei Kamera-Zoom > 1 abgeschnitten | Fenster um den Datenursprung 0 (`axes.py:111-116`) | Achse 0…10 zeigt bei Zoom 1,2 nur die Ticks 0…5, Achse 2…12 nur 2…7. Trifft auch den Export, der die aktuelle Kamera nutzt |
| F10 | Unbekannte Makros erscheinen als Text; `\n…` wird Zeilenumbruch | `richtext.py:135-141` | `\frac{a}{b}` wird „fracab“; `\not=` wird Umbruch + „ot=“; ebenso `\neg` |
| F11 | Parameter-Namen werden still verworfen | `scene_model.py:241, 247` | `u`, `step`, `rect`, `max`, `ln`, … liefern eine leere Kurve; `e`, `j`, `pi`, `x`, `t`, `i`, `theta` den eingebauten Wert (`e` → 2,718); keine Warnung |
| F12 | MathTex und Vector ignorieren `on`, obwohl die Oberfläche es anbietet | `scene_model.py:366-367` vs. `editor.js:1480, 1444` | Stehen in Weltkoordinaten (Sondierung) |
| F13 | Stil-Attribute nur am obersten Objekt | `scene_model.py:1316-1317` | `stroke_opacity` wirkt bei Component, Device, Gruppen und mehrteiligen Graphen nicht (Sondierung: Blätter bleiben bei 1,0) |
| F14 | Unbekannte Prop bei Klassen-Typen bricht die ganze Szene | `scene_model.py:1296` | z. B. `Text.rotation`; Status „error …, last frame kept“ |
| F15 | Tick-Format mit Punkt und Exponent | `axes.py:10-12` | „0.5“, „2e-06“, „1e+06“ |
| F16 | Zeichenketten mit führendem `#` werden zu Farben | `editor.js:469, 1406` | Ein Label „#1 …“ wird zum Farbwert und zum Farbwähler |
| F17 | Schrift auf der Leinwand ≠ Schrift im SVG | `canvas_painter.py:83/97` vs. `svg_painter.py:24` | Laufweiten und Umbrüche weichen ab |
| F18 | Export fest 1920×1080 | `editor_backend.py:16` | Kein Zuschnitt auf den Inhalt, kein anderes Seitenverhältnis |
| F19 | Kein Abschneiden am Teilbild | nur FunctionGraph (`axes.py:328-334`) sowie CurveFamily/Area (Klemmen) | Tangente, DataCurve, Line und Pfeile ragen über die Achsen hinaus |
| F20 | Objekte nicht umsortierbar | `editor.js:1255-1331` (nur Animationen) | Zeichenreihenfolge nur per JSON änderbar |
| F21 | Editor- und Engine-Defaults weichen ab | z. B. Marker `show_guides` (`editor.js:144` true vs. `scene_model.py:493` false), Text `font_size` 40 vs. 28, Band `full_height` | Gleiches JSON sieht im Editor anders aus als in Python |
| F22 | TangentLine `half_len` auf log-x in Dekaden | `scene_model.py:1111-1149` | Katalog-Kommentar: „line half-length in x“ (`editor.js:79`) |
| F23 | Testlücken | `grep` in `web/tests` | Kein Test für Legend, Measure, Area, NumberLine, ParametricCurve, PolarCurve, VectorField, ScalarField, Polygon |

---

## 4. Abweichungen zwischen Doku und Code

| Dokument (Stelle) | Behauptung | Code-Befund |
|---|---|---|
| `EDITOR_WERKZEUGE.md:38` (B10) | `values` „2;2,5;3“ | Wird als 2, 2, 5, 3 gelesen (F3); die Vorlage nutzt richtigerweise „2;2.5;…“ (`editor.js:268`) |
| `EDITOR_WERKZEUGE.md:54` (D2) | „NMOS und PMOS in vier Schreibweisen“ | NMOS 4 (`nmos`, `nmos4`, `nmos_dep`, `nmos_dig`), PMOS nur 3 (kein selbstleitender PMOS, `circuit.py:213`) |
| `EDITOR_WERKZEUGE.md:18` (A2) | „Jede Beschriftung versteht … `\,`“ | In Tabellenzellen zerlegt `\,` die Zelle (F5); Brüche, Unterstreichung usw. gehen nicht (F10) |
| `EDITOR_WERKZEUGE.md:19` (A3) | „jedes Objekt wählt … sein Achsensystem“ | MathTex und Vector ignorieren das (F12) |
| `EDITOR_WERKZEUGE.md:22` (A6) | SVG-Export für die Website | Richtig, aber immer 1920×1080 ohne Zuschnitt; Text als `<text>` und damit von der Schrift abhängig (F17, F18) |
| `EDITOR_WERKZEUGE.md:31` (B3) | „Mengenpfeil mit Breite proportional zum Wert“ | `thick` ist eine absolute Breite in WE; die Proportionalität muss man selbst ausrechnen |
| `EDITOR_WERKZEUGE.md:47` (C4) | Tabelle mit Zellen „a,b;c,d“, „Formelkurzschrift in Zellen“ | Kein Dezimalkomma, kein `\,`, kein Kopfgitter, keine Breite je Spalte (R8) |
| `EDITOR_WERKZEUGE.md:62` (E2) | Tests decken „alle neuen Objekte“ ab | Gilt für die Typen aus `figures.py` und `circuit.py`; Legend, Measure, Area, NumberLine und andere sind ungetestet (F23) |
| `EDITOR_GRAFIK_FEATURES.md:26` (§1) | „Beschriftung je Bauteil über das vorhandene MathTex“ | Bauteil-Labels sind Rich-Text-`Text`, nicht MathTex (`circuit.py:183`) |
| `EDITOR_GRAFIK_FEATURES.md:30-35` (§1) | Winkelraster 0/45/90° „Standard AN“, Gitter mit Einrasten | Nicht gebaut; die Doku sagt das in Zeile 39 selbst |
| `EDITOR_GRAFIK_FEATURES.md:9-12` (Kopf) | §10 Teilbilder, §13, §14, §31 als „gebaut“ | §10: keine automatischen Buchstaben, keine gekoppelten Achsen, keine Bildunterschrift. §13: kein Streifen über alle Teilbilder. §14: keine Hervorhebung nach Bedingung, nicht animierbar. §31: nur statische Tabelle, keine Kopplung oder Animation |
| `EDITOR_GRAFIK_FEATURES.md:57-59` (§4) | „Mehrere Kurven … + Legende“, „Achsen frei beschriften mit Einheiten“ | Legende nur auf 1:1-Achsen brauchbar (F4); Achsentitel ja, Tick-Format nicht anpassbar |
| `EDITOR_GRAFIK_FEATURES.md:77` (§7) | „Textlabels mit LaTeX … an beliebiger Stelle (MathTex)“; Callouts/Sprechblasen | MathTex nur in Weltkoordinaten; Callouts gibt es nicht (TextBox ohne Zeiger) |
| `EDITOR_GRAFIK_FEATURES.md:133-136` (§11) | Datenkurven aus CSV/JSON-Datei vom Zahlenwerk | Nur eingefügter Text im Feld `data`; kein Datei-Import, keine Verknüpfung |
| `EDITOR_GRAFIK_FEATURES.md:142` (§12) | log-x „50 kΩ bis 2 MΩ“ | Nur Dekaden-Beschriftung „10^{k}“ (`axes.py:40-45`) |
| `web/FEATURES_ROADMAP.md:8-11` | „Schon vorhanden: … Surface …; Animationen: Create, FadeIn, GrowFromCenter, Shift“ | Veraltet: Surface ist in FunctionGraph aufgegangen (`editor.js:331`); die Oberfläche hat zusätzlich Write, Rotate, Scale, MoveTo und Indicate (`editor.js:449-453`) |
| `web/FEATURES_ROADMAP.md:19-28` (Brainstorm) | Ellipse, Brace, NumberLine, Tangente, Parameter- und Polarkurve, Matrix/Tabelle, Log-Achsen, Stem, Schaltungselemente, Richtungsfeld, Contour/Heatmap seien offen | Alles schon vorhanden (`figures.py`, `circuit.py`, `scene_model.py`); die Roadmap ist veraltet |
| `editor.js:79` (Katalog-Kommentar) | `half_len` = „line half-length in x“ | Auf log-x in Dekaden (F22) |

---

## 5. Kurzfassung der wichtigsten Umwege

- **Dezimalkomma an den Achsen:** `x_numbers`/`y_numbers:false` und je Tick ein eigenes `Text`.
- **Kennlinienschar mit sauberen Rändern und eigenen Farben:** je Kurve ein `FunctionGraph` (schneidet richtig ab) plus ein `Text` am Ende statt `CurveFamily`.
- **Legende auf skalierten oder log-Achsen:** ein zweites `Axes` mit `show_axes:false`, x_range [-7,7], x_length 14, y [-4,4], y_length 8, origin 0 (Daten = Welt), und die Legende dort per `on` anhängen.
- **Gerade auf log-Achsen:** `DataCurve` mit zwei Punkten statt `Line`.
- **Verlängerung einer Geraden:** Geradengleichung in einen `FunctionGraph` mit `x_range` schreiben und die Endpunkte so wählen, dass die Linie im Teilbild bleibt.
- **Tabelle mit Dezimalkomma:** ein Raster aus `TextBox`-Objekten oder `Text` plus `Line`.
- **MathTex in Diagrammen:** die Weltposition ausrechnen; für einheitliche Größe `scale` per JSON setzen.
- **Graues oder gestricheltes Bauteil:** `color` in der Oberfläche; `dash` per JSON nachtragen. `stroke_opacity` wirkt nicht.
