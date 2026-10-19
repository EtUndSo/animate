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
- [ ] **F3 Flächenfüllung** — Fläche **unter** einer Kurve bzw. **zwischen** zwei Kurven schraffieren/färben
  (Integral, Energie, Bereichsmarkierung), Intervallgrenzen als Parameter.
- [ ] **F4 Tangente/Sekante im Punkt** — an einen Graphen im Punkt $x_0$ (Steigung/Ableitung ablesbar),
  Sekante über zwei Punkte; allgemein für jede plottbare Funktion.

## BATCH 2 — Pfeile & Felder  (K2, K1, K3, K14 — grundlegend für ET & Vektoranalysis)
- [ ] **F5 Beschriftete Pfeile** — gerader Pfeil mit LaTeX-Label (Strom/Spannung/Kraft/Feld), Doppel-/Maßpfeil
  ($d$, $r$), gebogener Umlaufpfeil (Maschen/Rückkopplung). Freie Platzierung, Label-Anker.
- [ ] **F6 2D-Vektorfeld** — Pfeilraster aus freiem Ausdruck $\vec F(x,y)$ **oder** Presets
  (radial/Quelle/Senke/Wirbel/uniform), Pfeillänge/-farbe nach Betrag, optional Divergenz-Farbkodierung.
- [ ] **F7 Skalarfeld-Heatmap + Niveaulinien** — $f(x,y)$ als Farbkarte/Höhenfeld mit Konturlinien;
  andockbarer **Gradientpfeil ⟂ Niveaulinie**. Freier Ausdruck + Colormap.
- [ ] **F8 Parameter-Schar-Animator** — ein `ValueTracker`-getriebener Parameter ($N$, $T$, $r$, $\varepsilon$)
  erzeugt eine **Kurvenschar**, die gegen eine Grenzfunktion läuft (Fourier-Partialsummen/Gibbs, Kennlinienfeld,
  Kern-Familie). Allgemein: beliebige parametrisierte Kurve + Sweep.

## BATCH 3 — Kurven & Koordinaten  (K4, K7)
- [ ] **F9 Parametrische Kurve** $x(t),y(t)$ — mit Laufpunkt, Orientierungspfeil, Tangente/Normale;
  Durchlaufsinn/Umkehr (Vorzeichen). Freie Ausdrücke, $t$-Bereich.
- [ ] **F10 Polarkurve $r(\theta)$ + eigenständige NumberLine** — Polarplot aus Ausdruck; NumberLine als
  wiederverwendbares 1D-Achsenobjekt (Marken, Beschriftung, Einheiten).
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
