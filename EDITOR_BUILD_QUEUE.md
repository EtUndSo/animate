# Editor-Build-Queue — allgemeingültige Features für die Wissens-Grafiken

Konkrete, batchweise Umsetzungsliste für den EtUndSo-Editor (`web/editor.html` + `web/editor.js`,
Python-Engine via Pyodide, 2D-Canvas + WebGL-Hybrid). Ziel: die in den **427 `:::grafik`-Blöcken**
(102 Artikel) beschriebenen Szenen nachbilden — **jedes Feature allgemeingültig**, nicht auf eine
Einzelszene zugeschnitten, sondern über Parameter/Presets/freie Ausdrücke auf alle gleichartigen
Szenarien erweiterbar.

Ergänzt — **ersetzt nicht** — die bestehenden Planungsdokumente:
- `web/FEATURES_ROADMAP.md` (Phasen P0–P7, Engine-Sicht)
- `EDITOR_GRAFIK_FEATURES.md` (Grafik-Bedarf; **Schaltplan-Editor = eigener Worktree, hier NICHT dupliziert**)
- `EDITOR_FIXES.md` (offene WebGL-Bugs #2/#3/#4)

## So wird jedes Feature „allgemeingültig" eingebaut (Muster)
Der Editor hat eine zentrale Registry — neue Primitive hängen sich überall an **derselben** Stelle ein:
1. **Engine-Objekt**: Eintrag in `OBJECT_TYPES` (`web/engine/scene_model.py` ~Z.156) + Bau-Zweig in
   `_build_object` (~Z.323) — nimmt generische Parameter (Ausdruck, Bereich, Auflösung, Presets) entgegen.
2. **Palette/Defaults**: Eintrag in `CATALOG` (`web/editor.js` ~Z.51) → Properties-Panel leitet Felder
   automatisch aus den Defaults ab (Zahl/Vektor/Checkbox/Color/Select).
3. **Darstellung**: 2D über `web/py/canvas_painter.py`/`renderer.py`; 3D-Flächen über
   `_gl_surface_mesh`/`_gl_solid_mesh` (GL) mit 2D-Fallback.
4. **Serialisierung**: fällt automatisch aus `objToSpec`/`migrateModel` ab (nichts Extra nötig).
Jedes Feature endet **lauffähig** (statisch servierbar) und wird committet (kein Push).

Legende: `[ ]` offen · `[~]` in Arbeit · `[x]` fertig & vom User getestet.

---

## BATCH 1 — 2D-Plot-Fundament & Annotationen  (höchste Szenen-Abdeckung: K13)
- [~] **F1 Mehrkurven-Plot + Legende** — mehrere Graphen/Signale auf **gemeinsamem** Achsensystem,
  automatische Farbrotation, optionale Legende (Label je Kurve). Basis für Kennlinienscharen, Fermi-Dirac,
  Vergleich mehrerer $f$.
  **Umgesetzt (wartet auf Test):** Mehrere `FunctionGraph` teilen bereits automatisch die eine Szenen-`Axes`
  (jede Kurve folgt deren Bereich/Skalierung) — Mehrkurven-Plot funktioniert also ohne Änderung; die
  Farbrotation beim Anlegen existiert. NEU: allgemeines **`Legend`**-Primitiv (`web/engine/legend.py`,
  registriert in `scene_model.py`, Palette-Eintrag in `editor.js`): eine Zeile je Eintrag (Farb-Swatch + Label),
  `labels` als `;`-Liste, `colors` optional (`;`-Liste Hex ohne `#`, sonst Auto-Palette), frei platzierbar,
  skaliert mit der Achse. Test: Axes + 2–3 FunctionGraphs anlegen, dann „Legend" mit passenden Labels/Farben.
- [~] **F2 Marker & Vermaßung** — Punkt-Marker mit Koordinaten/LaTeX-Label; Hilfslinien zu den Achsen;
  Maß-Angaben (Amplitude, Periode $T$, Sprunghöhe, markierter Punkt $(x_0,y_0)$). Allgemein: an jedes
  Graph-/Kurvenobjekt andockbar.
  **Umgesetzt (wartet auf Test):** zwei neue Objekte (special-cased in `scene_model.py`, Welt-Koordinaten
  via `coords_to_point` → keine Dot-/Pfeil-Verzerrung): **`Marker`** {point, label, show_guides, radius,
  font_size, color} = Punkt + optionale dünne Hilfslinien zu x-/y-Achse + Label; **`Measure`** {start, end,
  label, offset, font_size, color, stroke_width} = Doppelpfeil (Heads an beiden Enden) mit mittigem Label,
  `offset` schiebt senkrecht zur Strecke. CATALOG-Gruppe „Allgemein · Annotation". Test: Axes + FunctionGraph,
  dann Marker auf einen Kurvenpunkt (show_guides an) und Measure zwischen zwei Punkten (z. B. Periode $T$).
- [~] **F3 Flächenfüllung** — Fläche **unter** einer Kurve bzw. **zwischen** zwei Kurven schraffieren/färben
  (Integral, Energie, Bereichsmarkierung), Intervallgrenzen als Parameter.
  **Umgesetzt (wartet auf Test):** neues `Area` (special-cased in `scene_model.py`, `_build_area`): gefülltes
  Polygon aus gesampelter Oberkante `func` und Unterkante `func2` (leer → Baseline y=0) über `[x_min,x_max]`,
  `samples` Stützstellen, Pol-/NaN-Clamping auf den y-Bereich. Props {func, func2, x_min, x_max, samples,
  color, fill_color, fill_opacity, stroke_width}, CATALOG-Gruppe „Funktionen & Achsen". Test: Axes +
  `Area` func `sin(x)` über [0, π] (Fläche unter Kurve); dann func2 setzen für Fläche zwischen zwei Kurven.
- [~] **F4 Tangente/Sekante im Punkt** — an einen Graphen im Punkt $x_0$ (Steigung/Ableitung ablesbar),
  Sekante über zwei Punkte; allgemein für jede plottbare Funktion.
  **Umgesetzt (wartet auf Test):** `TangentLine` (special-cased in `scene_model.py`, `_build_tangent`):
  Tangenten-Steigung via zentraler Differenz an `x0`, Sekante durch `x0`&`x1` (`secant:true`); Linie ±`half_len`
  in x, optional Berührpunkt-Dot(s) (`show_point`) und Steigungslabel „m = …" (`show_slope`). Props {func, x0,
  secant, x1, half_len, show_point, show_slope, font_size, color, stroke_width}, CATALOG „Funktionen & Achsen".
  Test: Axes + `TangentLine` func `sin(x)`, x0 variieren; `secant:true` + x1 für Sekante.

**BATCH 1 komplett umgesetzt (F1–F4) — warten auf User-Test.**

## BATCH 2 — Pfeile & Felder  (K2, K1, K3, K14 — grundlegend für ET & Vektoranalysis)
- [~] **F5 Beschriftete Pfeile** — gerader Pfeil mit LaTeX-Label (Strom/Spannung/Kraft/Feld), Doppel-/Maßpfeil
  ($d$, $r$), gebogener Umlaufpfeil (Maschen/Rückkopplung). Freie Platzierung, Label-Anker.
  **Umgesetzt (wartet auf Test):** `LabeledArrow` {start, end, label, label_at:"mid"/"end", font_size, color,
  stroke_width} = gerader Pfeil (Vector) + Label an Mitte/Spitze; `LoopArrow` {center, radius (Welt), start_angle,
  end_angle (Grad), label, …} = Bogen mit Pfeilspitze am Ende (Umlauf/Rückkopplung). Maß-/Doppelpfeil bereits
  durch `Measure` (F2) abgedeckt. CATALOG-Gruppe „Annotation". Test: `LabeledArrow` mit `\vec F`-Label; `LoopArrow`
  für einen Maschenumlauf.
- [~] **F6 2D-Vektorfeld** — Pfeilraster aus freiem Ausdruck $\vec F(x,y)$ **oder** Presets
  (radial/Quelle/Senke/Wirbel/uniform), Pfeillänge/-farbe nach Betrag, optional Divergenz-Farbkodierung.
  **Umgesetzt (wartet auf Test):** `VectorField` (special-cased, `_build_vector_field`): Pfeilraster `nx`×`ny`,
  Richtung aus `preset` (radial/source/sink/vortex/uniform) oder freien Komponenten `fx(x,y)`,`fy(x,y)`
  (`func2_from_expr`); Länge $\propto$ Betrag (gekappt bei `max_len`) oder `normalize` = alle gleich;
  `color_by_mag` = Blau→Rot-Rampe nach Betrag. Props {preset, fx, fy, x_min..y_max, nx, ny, scale, normalize,
  max_len, color_by_mag, color, stroke_width}, CATALOG-Gruppe „Mathematik · Felder". Test: `VectorField`
  preset `vortex`; dann `custom` mit `fx`=`x`, `fy`=`-y` (Sattel) und `color_by_mag` an.
- [~] **F7 Skalarfeld-Heatmap + Niveaulinien** — $f(x,y)$ als Farbkarte/Höhenfeld mit Konturlinien;
  andockbarer **Gradientpfeil ⟂ Niveaulinie**. Freier Ausdruck + Colormap.
  **Umgesetzt (wartet auf Test):** `ScalarField` (special-cased, `_build_scalar_field`): Heatmap (`nx`×`ny`
  farbige Zellen, Blau→Gelb→Rot-Colormap, `fill_opacity`), Niveaulinien via **Marching Squares** (`levels`
  Stufen zwischen min/max), optional **Gradientpfeil** (`gradient_at`="x,y", ∇f zentrale Differenz, ⟂ zur
  Niveaulinie). `show_heat`/`show_contours` schaltbar. Props {func, x_min..y_max, nx, ny, levels, show_heat,
  show_contours, gradient_at, grad_scale, color, fill_opacity}, CATALOG „Mathematik · Felder". Test: `ScalarField`
  func `x^2+y^2`, dann `gradient_at`=`1,1`. (Perf-Hinweis: viele Objekte bei hohem nx/ny·levels — ggf. senken.)
- [~] **F8 Parameter-Schar-Animator** — ein `ValueTracker`-getriebener Parameter ($N$, $T$, $r$, $\varepsilon$)
  erzeugt eine **Kurvenschar**, die gegen eine Grenzfunktion läuft (Fourier-Partialsummen/Gibbs, Kennlinienfeld,
  Kern-Familie). Allgemein: beliebige parametrisierte Kurve + Sweep.
  **Umgesetzt — STATISCHE Schar (wartet auf Test):** `CurveFamily` (special-cased, `_build_curve_family`):
  Ausdruck $f(x;p)$ mit frei benanntem Parameter `param`; `count` Kurven über `p_min..p_max`, Fade hell→Farbe
  (`fade`), optionale dicke Grenzkurve (`show_limit`+`limit_func`). Props {func, param, p_min, p_max, count,
  x_min, x_max, samples, fade, show_limit, limit_func, color, stroke_width}, CATALOG „Funktionen & Achsen".
  Test: `CurveFamily` func `sin(k*x)/k`, param `k`; oder Fermi-Dirac/Kern über Parameter. **Offen (Verfeinerung):**
  echte **Animation** des Parameters via ValueTracker/Timeline — bei Bedarf als F8b nachrüsten.

**BATCH 2 umgesetzt (F5–F8) — warten auf User-Test.**

## BATCH 3 — Kurven & Koordinaten  (K4, K7)
- [~] **F9 Parametrische Kurve** $x(t),y(t)$ — mit Laufpunkt, Orientierungspfeil, Tangente/Normale;
  Durchlaufsinn/Umkehr (Vorzeichen). Freie Ausdrücke, $t$-Bereich.
  **Umgesetzt (wartet auf Test):** `ParametricCurve` (special-cased, `_build_parametric_curve`): Polyline aus
  `fx(t)`,`fy(t)` + Orientierungs-Pfeilspitze (~55 % der Kurve), optional Laufpunkt (`point_at`="t") mit
  Tangenten-/Normalenvektor (`show_tangent`/`show_normal`). Props {fx, fy, t_min, t_max, samples, show_arrow,
  point_at, show_tangent, show_normal, color, stroke_width}, CATALOG „Funktionen & Achsen". Durchlaufumkehr =
  t_min/t_max tauschen. Test: Kreis `cos(t)`/`sin(t)`; Lissajous `sin(3t)`/`sin(2t)`; `point_at` setzen.
- [~] **F10 Polarkurve $r(\theta)$ + eigenständige NumberLine** — Polarplot aus Ausdruck; NumberLine als
  wiederverwendbares 1D-Achsenobjekt (Marken, Beschriftung, Einheiten).
  **Umgesetzt (wartet auf Test):** `PolarCurve` (`_build_polar_curve`): $r(\theta)$→$(r\cos\theta,r\sin\theta)$
  Polyline + Orientierungspfeil, Variable `theta` (alias `t`); Props {func, theta_min, theta_max, samples,
  show_arrow, color, stroke_width}. `NumberLine` (`_build_number_line`): eigenständige 1D-Achse (Welt-Länge
  `length` um `center`, Ticks je `step` von x_min..x_max, optionale Wert-Labels); Props {x_min, x_max, step,
  length, center, tick_labels, decimals, font_size, color, stroke_width}. CATALOG „Funktionen & Achsen". Test:
  `PolarCurve` func `1+cos(theta)` (Kardioide); `NumberLine` mit step 1.
- [ ] **F11 Krummliniges Koordinatengitter** — Polar/Zylinder/Kugel-Gitter (konzentrische Kreise, Strahlen,
  Höhenebenen) + hervorgehobenes Flächen-/Volumenelement ($r\,dr\,d\varphi$ usw.).

## BATCH 4 — Komplexe Ebene & Signale  (K14, K15, K18, K19)
- [ ] **F12 Rotierender Zeiger / Phasor** — Pfeil in komplexer Ebene, Projektion→Sinus (gekoppeltes Teilbild),
  Zeigeraddition, gegenläufige Zeiger, $\times j\omega$ (90°-Drehung+Streckung). Animierbar über Winkel/ω.
- [ ] **F13 Linien-/Balkenspektrum** — über Frequenz-/Index-Achse; ein-/zweiseitig; Amplituden- **und**
  Phasenspektrum; $|c_k|$-Balken. Eingabe als Koeffizientenliste oder aus einem Signal.
- [ ] **F14 Stem/Abtast-Plot** — diskrete Stiele auf ganzzahligem $n$ + durchlaufende Kurve(n);
  Aliasing-Überlagerung (mehrere Kurven durch dieselben Stiele).
- [ ] **F15 Kern-/Buckel-Plot + Faltungs-Animation** — Dirac-Schar/Gauß/Poisson/Dirichlet-Kern
  (konstante Fläche, Konzentration über Parameter); Faltung $\varphi_\varepsilon * f$ als Glättungs-Animation.

## BATCH 5 — 3D-Geometrie  (K6, K8, K9, K10, K11)
- [ ] **F16 Generische ParametricSurface $(u,v)$** — freie Vektorfunktion $x(u,v)$ + Presets
  Kugel/Graph $z=f(x,y)$/Rotationsfläche; erweitert die bestehende z=f(x,y)-Fläche. (Nutzt GL-Renderer.)
- [ ] **F17 Tangentialebene + Normalenvektor** — an einen Punkt einer 3D-Fläche; Abstand Fläche–Ebene
  visualisierbar. Allgemein für jede ParametricSurface.
- [ ] **F18 Gitter→Parallelogramm/Parallelepiped-Deformation** — Kästchen/Quader unter einer Abbildung verzerrt;
  Kreuzprodukt-Fläche $|\partial_u x\times\partial_v x|$, Volumenfaktor $|\det D\Phi|$. (Jacobi-Visual.)
- [ ] **F19 3D-Volumen mit Hülle + Flusspfeile / Normalbereich mit Scanstrich** — Raumbereich $V$ mit
  äußerer Normale und Flusspfeilen (Gauß); schraffierter Normalbereich mit laufendem Scanstrich (Fubini).

## BATCH 6 — Festkörper / Quantenmechanik  (K20–K23, gemb1)
- [ ] **F20 Energieniveau-Leiter** — horizontale Sprossen aus Energieliste/Formel, Besetzung $\uparrow\downarrow$,
  Entartung, skalierbare Achse. Allgemein für Atom-/Box-/Band-Diagramme.
- [ ] **F21 Banddispersion $E(k)$** — periodisch über Brillouin-Zone, Steigung/Geschwindigkeit, Bandbreiten-Maß.
- [ ] **F22 $|\psi|^2$-Dichtewolken** — Orbital-Presets (s/p/d), stehende Wellen in 1D/2D/3D-Box; Dichte-Rendering.
- [ ] **F23 Kristallgitter-Baukasten** — Punktgitter + Basis, Einheits-/Wigner-Seitz-Zelle, reziprokes Gitter,
  1. Brillouin-Zone (3D-Polyeder).

## BATCH 7 — Querschnitt, Konstruktionen & Infrastruktur
- [ ] **F24 Geometrische Elementar-Konstruktionen** — Winkel (Bogen+Label), Arc, Brace (geschweifte Klammer),
  Ellipse, Sektor, Projektion/Lot/Mittelsenkrechte. Kleine, überall gebrauchte Primitive.
- [ ] **F25 Multi-Panel-Layout** — mehrere synchronisierte Teilbilder ("links/rechts", "oben/unten") mit
  gekoppelten Markern/Animation. Querschnitts-Muster fast jeder Einstiegs-Animation.
- [ ] **F26 UI-Freischaltung vorhandener Engine-Animationen** — Transform/ReplacementTransform/MoveAlongPath/
  Flash/Circumscribe/Write in die Palette (`ANIM_GROUPS`) + neues **TracedPath** (Spur eines Laufpunkts).
  (Low-Hanging-Fruit: Engine kann es schon, nur UI fehlt.)
- [ ] **F27 WebGL-Bugfixes #2/#3/#4** — Achsen/Grid im GL-Layer (Axes-on-Top), Tiefensortierung mehrerer
  transparenter Flächen, Wireframe-/Grid-Overlay auf GL-Flächen. Stützt F16/F19.

---

## Reihenfolge-Logik
Batch 1–2 decken den Großteil der mmet-/get1-/Fourier-/Grundlagen-Szenen (2D-Plots, Felder, Pfeile) — breitester
Hebel, self-contained, schnell testbar. Batch 3–4 ergänzen Kurven/Koordinaten und die Signal-/Komplex-Szenen.
Batch 5 erschließt die hoema3-3D-Geometrie (baut auf dem vorhandenen GL-Flächenrenderer auf). Batch 6 die
gemb1-Festkörperphysik. Batch 7 bündelt Querschnitt (Multi-Panel), kleine Konstruktions-Primitive, billige
UI-Freischaltungen und die GL-Bugfixes.

Abgearbeitet wird **einzeln, ein Feature pro Loop-Tick** (wie die Artikel): bauen → lauffähig halten →
committen (kein Push) → der User testet. Nicht enthalten: Schaltplan-Editor (eigener Worktree).
