# Bestandsaufnahme Figuren-Editor, Teil B: 3D, Rendering, Export, Animation

Stand 28.10.2026. Repo `C:\Users\info\PycharmProjects\pythonanimation`; alle Pfade unten relativ dazu. Im Repo wurde nichts geändert.

**Methode.** Vollständig gelesen: `web/engine/threed.py`, `camera.py`, `renderer.py`, `renderScene.py`, `scene.py`, `animation.py`, `processes.py`, `value_tracker.py`, `video.py`, `svg_painter.py`, `axes.py`, `web/py/*.py`, `web/gl/surface3d.html`. Aus `scene_model.py` die Teile zu 3D, GL und Kamera sowie `_build_object`, `_build_animation` und `ModelScene`. Aus `web/editor.js` die Teile zu Rendering, GL-Schicht, Kamera, Eigenschaftenfeld, Timeline und Export. Außerdem `web/editor.html`, `tools/editor_shot.py` und `tools/editor_ui_test.py`.

**Ausgeführt** wurde CPython 3.13 im Ordner `web/`:
- `tests/test_3d.py`, `test_axes3d.py`, `test_contract.py`, `test_canvas.py` und `test_steps.py` laufen alle grün.
- Eigene Proben liegen im Scratchpad `C:\Users\info\AppData\Local\Temp\claude\C--B-cher\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\`:
  - `probe_r1.py`: R1-Szene, CPU- gegen GL-Aufbau, SVG-Export. Ergebnisse in `probe_gl0.svg` und `probe_gl1.svg`.
  - `probe_r2.py`: 3D-Positionen, GL-Clipping und `origin`, Create auf GL, ChangeValue.
  - `probe_cairo.py`: Headless-PNG und -MP4 mit der `.venv`, die pycairo enthält. Ergebnisse in `probe_cairo.png` und `probe_cairo.mp4`.

**Nicht im echten Browser ausgeführt.** Aussagen zur WebGL-Darstellung, zu MediaRecorder und zu Playwright sind aus dem Code abgeleitet und mit **(Code-Befund)** markiert.

Legende Status: ✅ voll · 🟡 teilweise · ❌ nicht.

---

## 1. Architektur Rendering-Pfad 2D/3D/GL

### 1.1 Datenfluss Editor → Bild
1. **Editor-Modell (JS).** Das Modell `model` steht in `editor.js:455`. `toPythonModel()` (`editor.js:482–519`) setzt es um:
   - props werden zu args, Hex-Farben zu RGB (466–471).
   - Hintergrund `null` bedeutet transparent (484).
   - Animations-Args werden **nur** für Shift, MoveTo, Rotate und Scale erzeugt (490–494).
   - `gl: gl3d.ok && !_glFailed` (518).
2. **Pyodide.** `render_model(json)` (`web/py/editor_backend.py:29–48`) läuft so:
   - Aufbau: `ModelScene.construct()` (`scene_model.py:1575–1674`), dann `show_static()` (1676–1687).
   - Zeichnen: `_paint()` (`editor_backend.py:89–96`) ruft `paint_scene()` (`renderer.py:119–142`) auf.
   - `CanvasPainter` (`web/py/canvas_painter.py`) zeichnet auf `<canvas id="view" width=1920 height=1080>` (`editor.html:161`).
3. **GL-Schicht.** Gibt `render_model` `"ok:gl"` zurück, lädt `syncGL()` (`editor.js:437–447`) die Meshes über `gl_meshes()` (`editor_backend.py:103–118`). Es zeichnet sie auf `#view3d` (`editor.html:160`), das **hinter** dem transparent gemalten 2D-Canvas liegt (CSS `editor.html:58–62`).

**Painter-Schnittstelle.** Sie besteht aus drei Methoden (`renderer.py:6–13`). Es gibt drei Painter:
- `CanvasPainter` für den Browser.
- `SvgPainter` (`engine/svg_painter.py`) für den SVG-Export.
- `CairoPainter` (`engine/renderScene.py`) nur für CPython. `renderScene.py` und `video.py` werden im Browser **nicht geladen**: Die Liste `ENGINE_FILES` in `editor.js:4–9` enthält sie nicht.

### 1.2 Kamera
- **Projektion.** `camera.py:5–93` ist **nur orthografisch**. 2D projiziert auf RIGHT/UP. 3D ist ein z-up-Orbit:
  - `theta` = Azimut, `phi` = Elevation, dazu `zoom` (`camera.py:26–55`, `project` 66–72).
  - Es gibt keine Perspektive (`camera.py:17`: „Perspective … can be added later").
- **Abbildung der Daten.** x→RIGHT, y→UP, z→TOWARDS. Welt-z zeigt auf dem Bildschirm nach oben (`threed.py:6–8`).
- **Kamera im JS.** Die GL-Matrix `camM()` wird aus dem **JS-Modell** `model.camera` gebaut (`editor.js:397–408`), nicht aus der Python-Kamera. Das ist wichtig für jede spätere Kamera-Animation.
- **Bedienung:**
  - Ziehen = Orbit (`editor.js:1967–1977`); die Elevation ist auf ±(π/2−0,03) begrenzt (1942, 1974).
  - Mausrad = Zoom zwischen 0,2 und 8 (1998–2007).
  - ViewCube (657–665, Kamerafahrt 643–656) und Rotations-Gizmo (750–780).
  - **Keine Zahleneingabe** für theta/phi. Exakte Winkel lassen sich nur über `camera.theta/phi` (rad) in der Szenen-JSON setzen; sie werden mitgespeichert (`sceneData` 1078–1082).
- **LOD.** Bei Kamerabewegung wird die Auflösung reduziert: `ORBIT_DETAIL_CAP=28` (`editor.js:526–568`), `begin_lod`/`end_lod` (`editor_backend.py:121–149`).

### 1.3 2D-Pfad
Objekte werden in Einfügereihenfolge gezeichnet. Mit `axes_on_top` kommen die Achsen zuletzt (`renderer.py:133–142`). Die z-Achse ist als `_only_3d` markiert und fällt in 2D weg (`renderer.py:53–54`, `axes.py:240–261`).

### 1.4 3D-CPU-Pfad (Maler-Algorithmus)
- **Zeichenablauf `_paint_3d`** (`renderer.py:73–116`):
  - Alle Blätter werden flach gesammelt (60–70) und in **einer** Matrixmultiplikation projiziert (88–93).
  - Tiefe pro Blatt = **Mittelwert seiner Kontrollpunkte** (97); sortiert wird von fern nach nah (106).
  - Es gibt keinen z-Buffer und kein Zerlegen sich schneidender Polygone.
- **Achsen.** Mit `axes_on_top=True` werden die Achsen samt Kindern zuletzt gezeichnet (101–104). Das Gitter `_is_grid` wird mitsortiert (63–66). Editor-Standard ist `axes_on_top=false` (`editor.js:455`, `editor_backend.py:42`).
- **Fläche z=f(x,y)** über `Axes.plot_surface` (`axes.py:343–500`):
  - adaptives oder uniformes Quad-Netz; T-Stellen werden vernäht (436–457);
  - **Clip an z_min/z_max** nach Sutherland–Hodgman (416–434, 463–464);
  - Lambert-Schattierung (398, 484) und Höhenfarbe (403–414);
  - **Netzlinien** = Quad-Konturen in `grid_color`/`grid_width` (491–494).
- **Körper** Sphere, Box, Cube, Pyramid und Vector bestehen aus flachen Polygonen (`threed.py`).

### 1.5 3D-GL-Hybrid
- **Wann aktiv.** Alle vier Bedingungen müssen erfüllt sein:
  - WebGL ist initialisiert (`editor.js:1938–1939` meldet das per `set_gl_enabled`);
  - die Kamera steht auf 3D;
  - die Szene enthält GL-Objekte (`_gl_on`, `editor_backend.py:83–86`);
  - das Modell hat `gl:true` (`scene_model.py:1584`).
- **Was auf der GPU läuft:**
  - **2-Variablen-FunctionGraph** über `_gl_surface_mesh` (`scene_model.py:64–109`). Die Netzgröße ist n = max(16, min(max(res,120),200)) (1208). Das Python-Objekt ist dann nur ein **Proxy mit den 8 Ecken der Bounding-Box** (1216–1226). Der 2D-Painter überspringt ihn über `skip_gl` (`renderer.py:129–130`).
  - **Sphere/Box/Cube/Pyramid** über `_gl_solid_mesh` (112–156, 1303–1314). Ihre 2D-Facetten bleiben zusätzlich im Objekt.
- **Alles andere malt der 2D-Canvas transparent darüber:** Achsen, Ticks, Labels, Kurven, Punkte, Text, Vector, MathTex. Folgen:
  - Zwischen GL-Fläche und 2D-Objekten gibt es keine Verdeckung.
  - Die Achsen liegen im GL-Modus immer vorne, der Schalter „axes on top" wirkt nicht (`EDITOR_FIXES.md` #2).
- **Shader** (`editor.js:363–369`):
  - Lambert-Licht (0,4+0,6·d), schaltbar über `background.shadows` (418);
  - Höhenfarbe `hc()` (366);
  - bei Opazität < 1: Blending und `depthMask(false)` (422), aber **keine Dreieckssortierung**;
  - **keine Netzlinien**.
- **`web/gl/surface3d.html`** ist ein **eigenständiger Prototyp** mit eigenem Shader und JS-`new Function`. Keine andere Datei verweist darauf (grep), er ist nicht Teil des Editors.

### 1.6 Timeline und Wiedergabe
- **Engine.** `Scene.play/wait/seek` (`scene.py:23–86`): Segmente laufen nacheinander, Animationen innerhalb eines Segments parallel. `seek` arbeitet in zwei Durchgängen und ruft danach die Updater (54–86). Vertrag: Der Zustand ist eine reine Funktion von t (`web/ENGINE_CONTRACT.md`).
- **Abspielreihenfolge.** Das Modell gruppiert über `_group_by_step` (`scene_model.py:1553–1563`). Der Editor setzt `step` aber **global**: entweder alles nacheinander oder alles gleichzeitig (`editor.js:489`, `editor.html:170–173`). Es fehlen:
  - gemischte Reihenfolgen;
  - Startversatz;
  - Wahl der Easing-Funktion: `rate_func` ist immer `smooth` (`animation.py:12`), `toPythonModel` sendet keine.
- **Abspielen:**
  - `prepare_play` und `play_frame(t)` (`editor_backend.py:262–285`).
  - Play rendert vorab in einen Bitmap-Cache (`editor.js:965–1024`): Budget 1 GB bzw. 300 MB, Bildrate 30→15, Skalierung 1→0,5. Danach Wiedergabe (1027–1038); passt es nicht ins Budget, wird live gerechnet (1039–1048).
  - Transportleiste: Reset, Play, Pause, End, Neu berechnen (`editor.html:181–185`). **Kein Scrubber, keine Zeitleiste.**

### 1.7 Übersicht: Merkmal × Pfad

| Merkmal | 2D-Canvas | 3D-CPU (ohne WebGL) | 3D-GL (Browser-Standard mit WebGL) | SVG-Export | Cairo (CPython) |
|---|---|---|---|---|---|
| Fläche z=f(x,y) | Draufsicht | Facetten, sortiert | glatt (GPU) | nur im CPU-Fall richtig, im GL-Fall kaputt (F1) | Facetten |
| Netzlinien | ja | ja | **nein** | ja (CPU-Fall) | ja |
| Clip am z-Bereich | ja | ja | **nein** (F3) | wie CPU | ja |
| Höhenfarbe | heller/dunkler um z=0 | dto., ohne Licht | heller/dunkler um die Mitte der Datenwerte, mit Licht (F5) | wie CPU | wie CPU |
| Transparenz | Alpha | Alpha + Maler-Sortierung | Blending, unsortiert | `fill-opacity` | Alpha |
| Hoch-/Tiefstellung in Labels | ja | ja | ja (2D-Overlay) | ja (`<tspan>`) | **nein** (`plain`) |
| Verdeckung Kurve ↔ Fläche | – | Maler-Sortierung je Blatt | keine (Overlay immer vorn) | wie CPU | wie CPU |

---

## 2. Anforderungen

### R1 — 3D-Fläche z=f(x,y) (Gesamtstatus 🟡 teilweise)

Geprüft mit der Szene x 0,6…0,68, y 0…3, z 0…3, x/y/z_length 8/6/4. Sie baut im CPU- und im GL-Pfad (`probe_r1.py`); `probe_cairo.png` zeigt das Ergebnis.

| Teilaspekt | Status | Beleg | Was genau fehlt |
|---|---|---|---|
| Fläche über beliebigem Datenbereich | ✅ | Ein Ausdruck mit x **und** y wird zur Fläche (`scene_model.py:38–41`, Zweig 1199–1229); der Bereich kommt aus den Achsen (`axes.py:351`, GL `scene_model.py:69–70`) | – |
| Ungleiche Achsenskalierung | ✅ mit Einschränkung | `x/y/z_length` sind unabhängig von den Ranges (`axes.py:71–72, 283–289`; Katalog `editor.js:70`); das GL-Mesh nutzt dieselbe Abbildung (`scene_model.py:86–92`) | z wird **nicht zentriert**: Daten-z=0 entspricht Welt-z=0 (`axes.py:288`). Ein z-Bereich ohne 0 lässt z-Achse und Fläche über dem Boden schweben. Die Szene sitzt vertikal versetzt, im Probe-PNG ist das z-Label oben abgeschnitten (F8). Der Ausweg `origin` scheitert im GL-Pfad, weil das GL-Mesh `origin` ignoriert (F3). |
| Achsenbeschriftung mit Einheit und Tiefstellung, alle 3 Achsen | 🟡 | Rich-Text wie `U_{BE} / V` in Canvas und SVG (`canvas_painter.py:78–103`, `svg_painter.py:68–93`); das Probe-SVG enthält `U<tspan …>BE</tspan> / V`. `x_label`/`y_label` stehen im Katalog (`editor.js:71`). | **`z_label` gibt es in der Engine** (`axes.py:77, 257–259`), **aber nicht im Katalog**. Im Editor lässt es sich nicht anlegen (das Eigenschaftenfeld zeigt nur vorhandene props, `editor.js:1460`), nur über eine JSON-Datei; sonst heißt die z-Achse immer „z". In Cairo geht die Tiefstellung verloren (`renderScene.py:46`; verifiziert: „UBE / V"). |
| Tick-Beschriftung, Dezimalkomma | 🟡 / Komma ❌ | Automatische „schöne" Schritte (`axes.py:15–27`; Probe: 0.6, 0.61 … 0.68 und 0 … 3 in Schritten von 0.5). Ein fester Schritt geht als 3. Range-Eintrag (118–120). | Das Format ist `f"{v:g}"` (`axes.py:10–12`): **Dezimalpunkt, kein Komma, keine Option** (grep nach comma/locale/decimal_sep leer). Der feste Schritt ist nur per JSON setzbar, weil die UI die Range als 2er-Vektor zeigt. Die z-Achse bekommt keine „0" (254). Im 3D-Bild überlappen Tick-Zahl und Achsenlabel (F10). Ausweg: `show_numbers:false` plus eigene `Text`-Labels mit Komma; für die z-Achse muss z dabei vorskaliert werden (F2). |
| Farbkarte nach Höhe | 🟡 | CPU: `height_color` hellt oberhalb z=0 bis 70 % Richtung Weiß auf und dunkelt darunter ab, ohne Licht (`axes.py:403–414, 486–488`). GL: `hc()` hellt bzw. dunkelt um die Mitte zwischen Daten-min und -max, mit Licht (`editor.js:366–369`, `zt` in `scene_model.py:107`). | Nur eine Helligkeitsrampe in einem Farbton. **Keine mehrfarbige Farbkarte** (viridis/jet o. ä.), **keine Farbleiste**. CPU und GL bilden unterschiedlich ab (F5). Eine mehrfarbige Karte (blau→gelb→rot) gibt es nur im 2D-`ScalarField` (`scene_model.py:586–598, 900–907`). |
| Transparenz | 🟡 | `fill_opacity` (Katalog `editor.js:75`). CPU: pro Facette, Maler-Sortierung. GL: Blending mit `depthMask(false)` (`editor.js:422`). | GL sortiert die Dreiecke nicht. Wo sich die Fläche selbst überdeckt, kann die Darstellung von der Zeichenreihenfolge abhängen (Code-Befund; `EDITOR_FIXES.md`, Status #3). |
| Netzlinien | 🟡 | CPU: `grid_color`/`grid_width` (`axes.py:491–494`, Standard weiß 0,2 px, `editor.js:75`). | **Im GL-Pfad gar nicht** (Shader ohne Linien; `EDITOR_FIXES.md` #4 offen). GL ist im Browser Standard, deshalb sieht man Netzlinien im Editor nur ohne WebGL. |
| Gewählter Blickwinkel | 🟡 | Orbit, ViewCube und Gizmo; gespeichert in `model.camera` (§1.2) | Keine numerische Eingabe in der UI, keine Perspektive. |

**Was für R1 fehlt:**
- `z_label` im Katalog;
- Option für Dezimalkomma in `_fmt` (wirkt dann auch auf `DecimalNumber`, `text.py:33–34`);
- echte Farbkarte mit Farbleiste;
- im GL-Mesh: Netzlinien, Clipping am z-Bereich, `origin`;
- z-Zentrierung bzw. Kamera-Ziel in der Box-Mitte;
- Zahlenfelder für theta/phi;
- besserer Abstand zwischen Tick-Zahlen und Achsenlabels in 3D.

### R2 — Kurven auf der Fläche, 3D-Kurven, Punkte und Text in 3D (Gesamtstatus ❌ nativ; 🟡 über einen JSON-Umweg)

| Teilaspekt | Status | Beleg | Was genau fehlt |
|---|---|---|---|
| Schnittkurven (x, y0, f(x,y0)) und (x0, y, f(x0,y)) | ❌ nativ | Ein 1-Variablen-FunctionGraph liegt immer in z=0: `axes.plot` ruft `coords_to_point(x,y)` mit z=0 auf (`axes.py:314–341`). `ParametricCurve` kennt nur `fx`/`fy`, z=0 ist fest (`scene_model.py:698–699, 716`; Probe: kein `fz`). `DataCurve` nimmt nur Paare (`figures.py:42–45, 76`). | Ein 3D-Kurvenobjekt. **Funktionierender Umweg (verifiziert):** Objekt `Polygon` von Hand in die Szenen-JSON schreiben (steht nicht im Katalog, aber in `OBJECT_TYPES` `scene_model.py:160`), mit `{"vertices":[[x,y,z·k],…],"closed":false}`. Dabei ist **k = z_length/(z_max−z_min) von Hand vorzumultiplizieren** (F2). Im Eigenschaftenfeld ist die Punktliste nicht editierbar: Verschachtelte Arrays landen in `numberInput` (`editor.js:1399–1402, 1336`), eine Änderung zerstört sie. |
| Eigene Farben, dickere Linien | ✅ | `color`/`stroke_width` gibt es bei jeder Kurve (`_STYLE_ATTRS` `scene_model.py:344`) | – |
| Verdeckung Kurve ↔ Fläche | 🟡 | CPU: Maler-Sortierung mit **einer** Tiefe je Blatt (`renderer.py:97`) → eine lange Kurve wird stellenweise von Facetten übermalt, die geometrisch dahinter liegen (Code-Befund). GL: Die Kurve liegt immer vorne, auch hinter Erhebungen. | Tiefenversatz bzw. Kurven in der GL-Schicht; im CPU-Pfad automatisch in Segmente zerlegen. |
| Allgemeine 3D-Parameterkurven | ❌ | Nur als Wunsch geführt: `web/FEATURES_ROADMAP.md:25, 69` (ParametricCurve3D, P7), `EDITOR_BUILD_QUEUE.md` F16 | Objekt `ParametricCurve3D` (fx, fy, fz, t-Bereich), über `coords_to_point(x,y,z)` abgebildet. |
| Punkte an 3D-Positionen | 🟡 | `Dot` mit `center [x,y,z]` wird korrekt über `coords_to_point` abgebildet (`scene_model.py:1249–1254`; Probe: z=2,667 ✓). `Marker` mit `point [x,y,z]` und Label ebenfalls (`scene_model.py:462–514`; Probe ✓). | `Dot` ist eine **flache Scheibe in der x-y-Ebene** (`simpleShape.py:12–22`; Probe: z-Ausdehnung 0) und wird bei flacher Elevation zur Linie (F9). Der Label-Versatz des Markers liegt in Welt-x/y. |
| Text an 3D-Positionen | 🟡 / Fehler | `Text` wird über `axes.place` → `data_to_world` gelegt, und das reicht z **unskaliert** durch (`axes.py:293–301`, Zeile 300). Probe: z=2,0 statt 2,667. Dasselbe gilt für `Line` und `Polygon`. | z-Skalierung in `data_to_world` angleichen (F2). Bis dahin z vorskalieren oder das Label des `Marker` nutzen. `Vector` und `MathTex` sind Welt-Typen (`scene_model.py:366–367`) und erwarten **Weltkoordinaten**, keine Daten (Probe: Vector endet bei Welt (0.62, 1, 2)). Texte bleiben bildschirmparallel und werden in 3D mitsortiert (`renderer.py:98–99`), das ist gut. |

### R3 — Statischer Export (Gesamtstatus 🟡)

**PNG** (Menü „Photo ▾", `editor.js:2056–2090`):
- **2D und 3D-CPU:** ✅ `#view.toBlob`, exakt der Canvas-Puffer 1920×1080 (`editor.html:161`).
- **3D-GL:** ✅ (Code-Befund) `_compositeSource` legt GL-Canvas und 2D-Canvas zu einem Bild zusammen (`editor.js:984–990`, ermöglicht durch `preserveDrawingBuffer:true` in 374). Die Fläche ist damit als Raster enthalten.
- **Weitere Formate:** JPEG, WebP, AVIF und BMP, sofern der Browser sie kann (2059–2062, 2072). Qualität 0,95.
- **Größe/Auflösung: ❌ keine Option.** Immer 1920×1080; es gibt kein 2× und keinen Zuschnitt auf den Inhalt.
- Nicht im PNG: ViewCube, Gizmos und das Σ-KaTeX-Overlay. Sie liegen auf eigenen Canvases bzw. im HTML; das ist richtig so.
- **Hintergrund ✅:** In den Einstellungen gibt es „color" und „transparent" (`editor.js:1422–1437`). Transparent wird über `clearRect` umgesetzt (`canvas_painter.py:33–34`), in GL über `clearColor(0,0,0,0)` (`editor.js:413`).
  - **Achtung:** Die Standardfarbe folgt dem Theme. Im Nachtmodus ist sie grau `#d4d7dc` (`editor.js:2163–2171`), ein Export ohne gesetzte Farbe wird dann grau (F13).

**SVG** (Menü „SVG (Vektor)", `editor.js:2077–2083` → `export_svg`, `editor_backend.py:10–18`):
- **2D: ✅**
  - Pfade als kubische Béziers, Strichmuster, Text mit Hoch- und Tiefstellung als `<tspan>` (`svg_painter.py:41–93`).
  - Hintergrund als `<rect>`, bei „transparent" keiner (29–32).
  - Die Schrift wird weder eingebettet noch in Pfade umgewandelt (`system-ui…`, Zeile 24); das Ergebnis hängt also von den Schriften beim Betrachter ab. Der Canvas nutzt `sans-serif` (`canvas_painter.py:83`), daher weichen PNG und SVG leicht voneinander ab.
- **3D ohne WebGL (CPU-Pfad): ✅**
  - Die Facetten stehen in Maler-Reihenfolge, über dasselbe `_paint_3d`. Tiefensortierung ja; eine echte Verdeckungsrechnung (Zerlegen sich schneidender Facetten) nein.
  - Dateigröße gemessen: uniform 64×64 = 4096 Facetten ≈ **1,2 MB**; adaptiv ≈ 82 KB. Editor-Standard ist `adaptive:false, res_max:64` (`editor.js:75`).
- **3D mit WebGL (im Browser der Normalfall): ❌ Fehler F1.**
  - Im aktiven Szenenobjekt ist die Fläche nur der 8-Ecken-Proxy. `export_svg` ruft `paint_scene` **ohne** `skip_gl` auf.
  - Statt der Fläche wird ein sinnloser Bézier-Klecks aus den Ecken der Bounding-Box gezeichnet, in Flächenfarbe und -opazität. Verifiziert: `probe_gl1.svg` enthält `<path d="M285.25 336.97C285.25 -4032.77 …" fill="#5999eb" fill-opacity="0.7" …/>`.
  - **Die GL-Fläche erscheint also nie im SVG.** Körper (Sphere/Box/…) sind nicht betroffen, ihre 2D-Facetten bleiben.
- Das SVG zeigt immer die **statische Bearbeitungsansicht** (`_active()`), nie das gerade abgespielte Bild.
- Größe: `width`/`height` 1920×1080 plus `viewBox` (`svg_painter.py:95–97`); keine Option für Größe oder Zuschnitt.

### R9 — Animation (Gesamtstatus 🟡: 2D-Animation und Videoexport ja; Parameter-, Kamera- und GL-Flächen-Animation nein)

**Animationstypen:**

| Animation | Engine (`animation.py`) | Modell (`ANIMATION_TYPES`, `scene_model.py:170–176`) | Editor-UI (`ANIM_GROUPS`, `editor.js:449–453`) | Args aus der UI (`editor.js:490–494`) |
|---|---|---|---|---|
| Create | 93–150 | ✅ | ✅ Erscheinen | – (CPU-Fläche: Wellenfront von der Mitte aus, 131–139) |
| Write | 338–340 | ✅ | ✅ | – |
| FadeIn | 65–75 | ✅ | ✅ | – |
| GrowFromCenter | 43–54 | ✅ | ✅ | – |
| Shift | 31–40 | ✅ | ✅ Bewegen | `vector` |
| MoveTo | 291–304 | ✅ | ✅ | `point` |
| Rotate | 256–270 | ✅ | ✅ | `angle` (Grad→rad); `around` fehlt |
| Scale | 273–288 | ✅ | ✅ | `factor`; `around` fehlt |
| Indicate | 331–335 | ✅ | ✅ Betonen | Farbe und Faktor fest |
| MoveAlongPath | 307–328 | ✅ | ❌ | `path` wird nie übergeben → **Szene baut nicht** (F7, verifiziert) |
| ChangeValue | 153–162 | ✅ | ❌ | `value` wird nie übergeben → **Szene baut nicht** (F7, verifiziert) |
| FadeOut, Transform, ReplacementTransform, TransformMatchingTex, Recolor, Pulse, PulseColor, AppearPulseColor, Refine | ✅ | ❌ | ❌ | nur intern, in Operationen (z. B. Σ-Choreografie `processes.py:207–316`) |

Animierte **Operationen** (Palette `COMPUTATIONS`, `editor.js:294–318`):
- Faltung: `processes.py:31–72` (ValueTracker + `always_redraw`).
- Σ/∏: 83–316.
- Arithmetik: `arithmetic.py`.

**Parameter-Animation (Schiebewert über die Zeit): ❌.**
- Ein `Parameter` ist eine Konstante in `_PARAMS`, die beim Aufbau gesetzt wird (`scene_model.py:234, 244–248, 1594–1604`). Der Regler löst einen kompletten Neuaufbau aus (`editor.js:1372–1381`).
- Es gibt keine Verbindung zu einem ValueTracker. Probe: `ChangeValue` auf einen ValueTracker namens `k` lässt den Graphen `k*x` unverändert („graph changed: False").
- Die Doku bestätigt das (`EDITOR_WERKZEUGE.md:85`).
- **Kürzester Weg:** eine Animation `ParameterSweep(name, from, to)`. `ModelScene` hängt dafür an jedes Objekt, dessen Ausdruck den Namen enthält, einen Updater. Der setzt `_PARAMS[name]` auf den Tracker-Wert und baut den Spec neu (`_build_object` + `become`).
  - Kosten pro Frame = Neuaufbau der betroffenen Objekte.
  - Bei GL-Flächen muss zusätzlich das Mesh pro Frame neu hochgeladen werden. Dafür braucht es einen Hook, der von `play_frame` zu `gl_meshes` der Play-Szene führt.

**Kamera-Animation in 3D: ❌.**
- `Camera` ist kein AnimObject und weder in der Timeline noch in `seek` (`scene.py:54–86`). `ModelScene` setzt die Kamera einmal (`scene_model.py:1585–1588`).
- Die UI-Kamerafahrt `_tweenCamera` (`editor.js:643–656`) ist reine Navigation und wird nicht aufgenommen; `exportVideo` ruft nur `playFrame` (2119–2127).
- **Weg:** Modellfeld `camera_keys:[{t,theta,phi,zoom}]`, in `seek` interpolieren. `play_frame` gibt die Kamera zurück, JS setzt `model.camera` für das Frame und ruft `gl3d.draw`. Weil die GL-Matrix aus `model.camera` kommt (`editor.js:397–408`), muss JS die Werte pro Frame spiegeln.

**Video/GIF/WebM/MP4/Frame-Folge:**
- **Im Browser: 🟡** `exportVideo` (`editor.js:2093–2135`):
  - Aufnahme über `captureStream(0)` + `requestFrame` bzw. `captureStream(30)` und MediaRecorder.
  - Formate je nach `isTypeSupported`: MP4 (H.264), WebM (VP9/VP8/AV1), MP4 (AV1) (2065–2073).
  - **30 fps fest** (2105), 12 Mbit/s (2109), 1920×1080. Im GL-Modus wird das zusammengesetzte Bild aufgenommen (2098–2102).
  - Das Frame-Tempo hängt an der Echtzeit (2131–2132). Rendert der Rechner langsamer als Echtzeit, tragen die Bilder Wanduhr-Zeitstempel: Das Video wird länger und ungleichmäßig (Code-Befund aus der MediaRecorder-Semantik; der Kommentar 2053–2055 verspricht Gleichmäßigkeit, F15).
  - **GIF ❌, PNG-Folge ❌,** keine Option für Bildrate oder Größe. Das Σ-KaTeX-Overlay fehlt im Video (HTML, `updateSumOverlay` 1807–1823).
- **GL und Animation (F4):**
  - Die GL-Schicht wird beim Abspielen und bei der Aufnahme **nicht neu gezeichnet**, nur einmal vor dem Start (`camDraw` 1058, 2119). `play_frame` malt nur 2D (`editor_backend.py:279–285`), und der Flächen-Proxy wird übersprungen.
  - Folge: Create, FadeIn, Shift und andere Animationen auf einer **GL-Fläche wirken nicht**. Eine Fläche, die per Create erscheinen soll, ist **ab t=0 voll sichtbar**: `gl_meshes` stammt aus der statischen Bearbeitungsszene (`editor_backend.py:106`), in der `show_static` die Erscheinungsziele voll zeigt (`scene_model.py:1684–1685`).
  - Verifiziert: Der Proxy während Create hat t=0,5 → 4 Punkte, aber `_gl=True`.
  - Ohne WebGL (CPU-Pfad) funktioniert Create als Wellenfront.
- **CPython (headless): 🟡**
  - `video.py` (`VideoWriter`: Cairo → ffmpeg aus `imageio_ffmpeg`) existiert, `-r` ist aber fest **60** (`video.py:14–22`, `constants.py:20`).
  - Es gibt **keine Schleife** von `ModelScene` zum Writer.
  - In der `.venv` lauffähig: Probe mit 31 Frames → MP4 in 0,8 s. Das System-Python hat kein pycairo.
- **Kürzeste Wege** stehen in §3.

---

## 3. Headless-Export-Weg

### 3.1 Was es schon gibt

**`tools/editor_shot.py`** (Playwright, `channel="chrome"`) injiziert die Szene über localStorage (22–24), wartet auf „Ready" plus 2,5 s (31–32) und macht einen **Element-Screenshot** von `#view` (36). Grenzen:
- Bildgröße = CSS-Größe des Elements (Viewport 1600×1000, `.view-wrap` `editor.html:57`), **nicht 1920×1080**.
- In 3D liegen ViewCube und Rotations-Gizmo absolut über der Zeichenfläche (`editor.html:64–65`) und **sind mit im Bild**; je nach Auswahl auch das Bearbeitungs-Gizmo (`#editgizmo`, 63).
- Das Warten ist zeitbasiert. Der Status „Ready ✓ — add…" wird schon **vor** dem Laden der Szene gesetzt (`editor.js:2009`), bei schweren Szenen droht ein Wettlauf.
- Nur PNG, kein SVG, kein Video. Die GL-Fläche ist dagegen richtig im Bild, weil es ein Seiten-Screenshot ist.

**`tools/editor_ui_test.py`** zeigt, dass beides funktioniert:
- ein Klick im Menü plus `expect_download` (SVG, 92–101);
- das Laden einer Szene per URL `?scene=` (104–111; `editor.js:2010–2015`).

**Wichtig:** `editor.js` wird als **ES-Modul** geladen (`editor.html:223`). `playFrame`, `preparePlay`, `svgFn` und `gl3d` sind modulintern und **nicht** über `page.evaluate` erreichbar. Frame-genaues Steuern von außen braucht deshalb einen kleinen Hook.

### 3.2 Wege

**A) Playwright + vorhandene Buttons** (keine Änderung am Editor nötig)
- Ablauf: `editor.html?scene=szenen/x.json` öffnen, warten, bis die Zeichenfläche fertig ist, dann über `#dl-png-caret` den Eintrag PNG oder SVG wählen bzw. `#dl-video` klicken und den Download abfangen.
- PNG ✅: 1920×1080, mit GL-Komposit.
- SVG ✅ **nur ohne GL**. Dazu Chromium mit `--disable-webgl` bzw. `--disable-3d-apis` starten. Dann schlägt `gl3d.init` fehl, und es folgen `set_gl_enabled(false)` und `gl:false` (`editor.js:518, 1938–1939`). Die Fläche läuft über den CPU-Pfad, und das SVG stimmt (Code-Befund).
- Video: MediaRecorder in Echtzeit. Headless-Chromium kann meist nur WebM; das Timing-Risiko aus F15 bleibt.

**B) Playwright + Hook** (empfohlen für Video, GIF und Frame-Folgen)
- In `editor.js` etwa 8 Zeilen ergänzen:
  `window.__anim = { ready:()=>!!renderModel, prepare:()=>(_prepare() ? playDuration : 0), frame:(t)=>{ playFrame(t); camDraw(); return _compositeSource($("view")).toDataURL("image/png"); }, svg:()=>String(svgFn()) }`.
- Python-Schleife: `for i in range(N): png = page.evaluate("t=>__anim.frame(t)", i/fps)` → Datei. Dann ffmpeg aus `imageio_ffmpeg` (vorhanden) → MP4/WebM; GIF über `palettegen`/`paletteuse`.
- Vorteile: deterministisch und unabhängig vom Rendertempo; Hoch-/Tiefstellung, MathTex und GL-Komposit funktionieren. GL-Flächen bleiben aber statisch (F4).
- Was fehlt: der Hook und ein Skript `tools/render_anim.py` (~50 Zeilen).

**C) Reines CPython** (ohne Browser)
- Schritt 1: ein Konverter vom Editor-JSON (props, Hex, `background{…}`) zum Python-Modell. Das ist ein Port von `toPythonModel` (`editor.js:466–519`): props→args, Hex→RGB, Hintergrund, Rotate Grad→rad, `step` aus `playMode`; ~40 Zeilen. Die gespeicherten Szenen (`web/szenen/*.json`) liegen im **Editor-Format**, das wurde geprüft.
- Schritt 2: `ModelScene(model, gl:false)`, dann:
  - **`SvgPainter`** → SVG, identisch zu `export_svg`; läuft mit System-Python (Probe).
  - `CairoPainter` → PNG.
  - Seek-Schleife mit `VideoWriter` → MP4.
- Grenzen:
  - **MathTex lässt den ganzen Aufbau scheitern** (`TypeError … unexpected keyword 'tex'`, verifiziert). Es muss herausgefiltert oder vorher im Browser in Glyphen aufgelöst werden; Σ-Operationen brauchen ebenfalls Glyphen.
  - Cairo verliert Hoch- und Tiefstellung. Ausweg: SVG-Frames erzeugen und mit Browser oder resvg rastern.
  - Bildrate in `video.py` fest 60.
  - `render_to_surface` nutzt `axes_on_top=True` (`renderScene.py:61`), der Editor-Standard ist False (`editor_backend.py:42`).
  - Flächen nur facettiert.
  - pycairo gibt es nur in der `.venv`.

### 3.3 Empfehlung
1. Vorher **F1** (SVG im GL-Modus) und **F2** (z-Skalierung) beheben, siehe §4.
2. **SVG-Standbilder** für Artikel: sofort Weg C mit `SvgPainter` (ohne Cairo, System-Python reicht) oder Weg A mit abgeschaltetem WebGL.
3. **PNG**: Weg A (1920×1080, mit GL-Glätte).
4. **Video/GIF**: Weg B (Hook + Frame-Schleife + ffmpeg). Den MediaRecorder-Button nur nutzen, wenn das Rendern sicher schneller als Echtzeit ist.

---

## 4. Fehler und Auffälligkeiten

| Nr. | Schwere | Befund | Beleg | geprüft |
|---|---|---|---|---|
| F1 | hoch | Der **SVG-Export im 3D-GL-Modus** zeichnet statt der Fläche einen Bézier-Klecks aus den 8 Ecken der Bounding-Box. Die Fläche fehlt, der Docstring behauptet das Gegenteil. **Fix:** in `export_svg` bei `_gl`-Objekten das letzte Modell mit `gl:false` neu bauen und malen (JSON in `render_model` merken); alternativ `skip_gl=True` und die GL-Fläche als `<image>` (DataURL) unterlegen. | `editor_backend.py:10–18`; Proxy `scene_model.py:1216–1226`; `renderer.py:129–130` | ja (CPython, `probe_gl1.svg`) |
| F2 | hoch (3D) | `data_to_world` reicht z **unskaliert** durch, `coords_to_point` skaliert z dagegen mit z_length/(z_max−z_min). Text, Line, Polygon und alle per `axes.place` gelegten Objekte landen in falscher Höhe; Dot und Marker liegen richtig. **Fix:** `out[:,2] = pts[:,2]*z_length/(z_max−z_min) + origin[2]`. | `axes.py:288` gegen `axes.py:300`; `scene_model.py:1299–1300` | ja (2,0 statt 2,667) |
| F3 | mittel | Das GL-Flächenmesh ignoriert `axes.origin`, Log-Achsen und das **Clipping am z-Bereich**. | `scene_model.py:69–92` (kein `origin`, kein `_fx`/`_fy`, kein Clip); Probe mit `origin [1,0.5,0]`: GL x −4…4, Achsen −3…5; Daten-z-max 12 → Welt 16 statt Clip bei 4 | ja |
| F4 | mittel | Die GL-Schicht ist beim Abspielen und Aufnehmen **statisch**. Animationen auf GL-Flächen sind unsichtbar, eine Create-Fläche ist ab t=0 voll da. Der Timeline-Vertrag gilt nicht für die GL-Schicht. | `editor_backend.py:106, 279–285`; `editor.js:1058, 2119–2127`; `scene_model.py:1684–1685` | Proxy-Zustand ja; Bild = Code-Befund |
| F5 | niedrig | Die Höhenfarbe unterscheidet sich zwischen CPU (Bezug z=0, ohne Licht) und GL (Bezug Mitte zwischen min und max, mit Licht). Editor-Bild und SVG/PNG-Fallback sehen verschieden aus. | `axes.py:403–414, 486–488` gegen `editor.js:366–369` | Code |
| F6 | niedrig | Bei GL-Transparenz werden die Dreiecke nicht sortiert. | `editor.js:422–426` | Code |
| F7 | mittel | `MoveAlongPath` und `ChangeValue` stehen im Modell, `toPythonModel` verwirft aber ihre Args. Steht ein solcher Typ in der Szenen-JSON, baut die **ganze Szene nicht** („error: … last frame kept"). | `editor.js:490–494`; `scene_model.py:1346–1348` | ja (`TypeError`) |
| F8 | mittel | Die z-Achse ist nicht zentriert, Daten-z=0 entspricht Welt-z=0. Ein z-Bereich ohne 0 schwebt; die Kamera dreht um den Welt-Ursprung, die Box sitzt vertikal versetzt, und das z-Label wird oben abgeschnitten. | `axes.py:244–261, 288`; `probe_cairo.png` | ja (PNG) |
| F9 | niedrig | Dot und Marker-Punkt sind in 3D flache Scheiben in der x-y-Ebene. | `simpleShape.py:12–22` | ja |
| F10 | niedrig | In 3D überlappen Tick-Zahl und Achsenlabel (im PNG steht „3" im Label „UCE / V"). Versätze immer in Welt-DOWN/LEFT. | `axes.py:215, 220, 229–233, 256` | ja (PNG) |
| F11 | mittel (headless) | MathTex scheitert in CPython am Argument `tex` → der Aufbau bricht ab. | `svg.py:191`; `editor.js:1897–1901` | ja |
| F12 | niedrig | Alter Cairo-/Video-Pfad: `plain()` flacht Rich-Text ab, Bildrate fest 60, `axes_on_top`-Standard weicht ab, kein Treiber für `ModelScene`. | `renderScene.py:46, 61`; `video.py:18` | ja |
| F13 | niedrig | Im Nachtmodus färbt sich der Export-Hintergrund grau (`#d4d7dc`), solange keine eigene Farbe gesetzt ist. | `editor.js:2163–2171` | Code |
| F14 | niedrig | `editor_shot.py`: Bild in CSS-Größe, mit 3D-Overlays, Warten mit Wettlauf. | §3.1 | Code |
| F15 | niedrig | MediaRecorder-Video mit Echtzeit-Zeitstempeln: Bei langsamem Rendern wird das Video länger und ungleichmäßig. | `editor.js:2105–2132` | abgeleitet |
| F16 | niedrig | Das SVG zeigt immer die Bearbeitungsansicht, das PNG den aktuellen Canvas (auch ein Zwischenbild beim Abspielen). | `editor_backend.py:54–55` | Code |
| F17 | niedrig | Das Σ-KaTeX-Overlay (Funktionsmodus bzw. Ladephase) fehlt in PNG, SVG und Video. | `editor.js:1807–1823` | Code |
| F18 | niedrig | Abspielreihenfolge nur global; `wait` aus dem Modell wird vom Editor nie gesendet. | `editor.js:489, 515–518`; `scene_model.py:1672–1673` | Code |
| F19 | niedrig | GL-Indizes sind 16-bit. Flächen sind sicher (höchstens 201² = 40 401 Vertices), Körper über 65 535 Vertices fallen still auf den CPU-Pfad zurück. | `scene_model.py:108, 150–151`; `editor.js:385, 426` | Code |

---

## 5. Abweichungen Doku ↔ Code

| Quelle | Aussage | Tatsächlich im Code | Bewertung |
|---|---|---|---|
| `web/py/editor_backend.py:11–12` (Docstring `export_svg`) | „3D surfaces are drawn by the flat CPU painter here" | Im GL-Modus wird der Proxy-Klecks gezeichnet | **falsch** (F1) |
| `EDITOR_WERKZEUGE.md:22` (A6) | SVG-Export „fertig" | 2D ✓; 3D mit WebGL ✗ | unvollständig |
| `web/FEATURES_ROADMAP.md:9` | „Schon vorhanden: … Surface" | Die Klasse `threed.Surface` (`threed.py:42`) steht nicht in `OBJECT_TYPES`; der Editor wandelt Surface in FunctionGraph um (`editor.js:331`) | veraltet |
| `web/FEATURES_ROADMAP.md:10` | Animationen „Create, FadeIn, GrowFromCenter, Shift" | UI kennt 9, Modell 11 (§2 R9) | veraltet |
| `web/FEATURES_ROADMAP.md:15` | „Painter (Canvas)" | Zusätzlich `SvgPainter` (Export) und GL-Hybrid | unvollständig |
| `web/FEATURES_ROADMAP.md:36, 57` | animierbares Kamera-Objekt ist ein Wunsch | nicht vorhanden | stimmt |
| `ROADMAP.md:76` (Batch 6 offen) | Foto/Video + Scrubber | Foto/Video vorhanden, Scrubber nicht | teils veraltet |
| `ROADMAP.md:77` (Batch 7 offen) | Perspektive + Orbit + 3D-Objekte | Orbit und Körper vorhanden, Perspektive fehlt | teils veraltet |
| `ROADMAP.md:84` | „More easing…, FadeOut, MoveAlongPath" offen | FadeOut und MoveAlongPath in der Engine (nicht in der UI); Easing nur smooth/linear | teils veraltet |
| `README.md:9` | Web = „HTML5 Canvas (Pyodide)" | dazu WebGL-Hybrid und SVG-Export | veraltet |
| `web/ENGINE_CONTRACT.md` | Bild zur Zeit t ist reine Funktion von t | gilt für die Python-Szene; die GL-Schicht liegt außerhalb und ist statisch | Lücke (F4) |
| `EDITOR_FIXES.md` #1/#3 „erledigt (Browsertest offen)" | Schatten-Schalter bzw. Opazität im GL | `uShade` (`editor.js:365–369, 418`), GL-Opazität (`scene_model.py:1223, 1309`; `editor.js:422`) | im Code vorhanden |
| `EDITOR_FIXES.md` #2/#4 offen | Achsen im GL bzw. Netzlinien im GL | fehlen beide | stimmt |
| `EDITOR_WERKZEUGE.md:85` | Parameter-Animation als Film offen | kein Mechanismus vorhanden | stimmt |
| `editor.js:73–74` (Kommentar) | Flächen-Props `height_color`, `grid_*` | `grid_*` wirkt im GL-Pfad nicht | unvollständig |
| `editor.js:195–196` (Kommentar) | Faltung „follow once ValueTracker/updaters land" | Faltung existiert (Vorlage 247–256) | veraltet |
| `editor.js:522–525` (Kommentar) | „Our renderer is a CPU painter (no GPU z-buffer)" | GL-Hybrid vorhanden | veraltet |
| `editor.js:2053–2055` (Kommentar) | Video „smooth no matter how long a frame takes" | keine verworfenen Frames, aber Zeitstempel nach Wanduhr | überzogen (F15) |
| `camera.py:17` | „Perspective/zoom can be added later" | Zoom vorhanden, Perspektive nicht | teils veraltet |
| `tools/editor_shot.py` (Docstring) | „fotografiert die Zeichenfläche" | Element-Screenshot in CSS-Größe, mit 3D-Overlays | ungenau |
| `EDITOR_BUILD_QUEUE.md:22–23` | 3D-Flächen über `_gl_surface_mesh` mit 2D-Fallback | stimmt; der Fallback greift nur ohne WebGL | stimmt |
