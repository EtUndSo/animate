# Editor: Bestand und Ausbauplan (Stand 30.10.2026)

Ziel: Alle Abbildungen der Website entstehen im EtUndSo-Editor. Im Artikel steht ein festes Bild oder eine vorher gerenderte Animation, jeweils mit einem Link zur Vorlage im Editor. Keine Engine läuft live auf der Artikelseite (Entscheidung des Users am 28.10.2026).

Diese Datei fasst eine vollständige Code-Prüfung zusammen. Drei Prüfungen haben den Code gelesen, Proben in CPython und im echten Browser ausgeführt und jede Aussage mit Datei:Zeile belegt. Die Detailberichte liegen in `notizen/editor_bestand/`:
- `A_2d_beschriftung_schaltplaene.md`: Objekttypen mit allen Props, 2D-Diagramme, Beschriftung, Schaltpläne, Schemazeichnungen, Fehler F1–F23.
- `B_3d_export_animation.md`: Rendering-Pfad 2D/3D/WebGL, 3D-Flächen, Export, Animation, Headless-Wege.
- `C_oberflaeche_vorlagen.md`: Palette, Eigenschaftenfeld, Szenenformat, Vorlagen, Bedienung, Testlage, Abgleich mit `EDITOR_WERKZEUGE.md`.

Die älteren Dokumente (`EDITOR_WERKZEUGE.md`, `EDITOR_GRAFIK_FEATURES.md`, `web/FEATURES_ROADMAP.md`, `ROADMAP.md`) behaupten in mehreren Punkten mehr, als der Code kann. Bei Widersprüchen gilt diese Datei.

## 1. Was sicher funktioniert

- **Diagramme:** Teilbilder mit Titel, Funktionsgraphen mit `exp()` und Parametern, Log-Achsen, Achsentitel mit Tiefstellung, Schnittpunkt zweier Kurven (`Marker` mit `func` + `func2`), Strichlinien, Bänder und Flächen, Text in Datenkoordinaten, Pfeile und Doppelpfeile mit Label, Kurven auf Teilbereichen.
- **Schaltpläne:** npn und weitere Mehrpole, Zweipole einschließlich gesteuerter Quellen (Raute) mit beliebigem Label, Spannungs- und Strompfeile, offene Klemmen, Knoten, Leitungen mit Ecken, graue Bauteile, Drehen und Spiegeln.
- **Schemazeichnungen:** Gebiete mit Materialfüllung, Teilchenwolken, Bänderdiagramme mit `where()`, Profile als `DataCurve` plus `Band`.
- **3D:** Fläche z = f(x,y) mit beliebigen Datenbereichen und ungleicher Skalierung, Transparenz, Blickwinkel.
- **Oberfläche:** 42 Typen in der Palette, Eigenschaftenfeld deckt fast alle Engine-Props ab. Speichern als JSON, automatische Sicherung, Szene per `?scene=`, Vorlagen über `tools/editor_vorlagen.py`.
- **Export:** PNG immer (fest 1920×1080), SVG in 2D als zugeschnittenes Artikelbild, MP4/WebM als Echtzeit-Aufnahme. Stapel-Export der SVGs ohne Browser mit `tools/export_szenen.py`.
- **Artikel:** Block `:::abbildung <szene>` in `build_wissen.py` (§6, 30.10.).
- **Tests:** `editor_ui_test.py`, `editor_schematic_test.py` und alle Tests in `web/tests` grün. `test_children` und `test_process` brauchen auf der Windows-Konsole `PYTHONIOENCODING=utf-8`, sonst brechen sie beim Ausgeben von „≈“ ab.

## 2. Sicherheitsbefund (behoben am 28.10., siehe §6)

So war es: `editor.html?scene=<url>` lud eine beliebige Adresse, und Σ/∏-Terme aus der Szene wurden mit `new Function` ausgeführt. Ein präparierter Link konnte deshalb beliebiges JavaScript auf der Website starten. Außerdem überschrieb jeder Link die automatisch gesicherte Szene.

Heute:
- `?scene=` nimmt nur relative Pfade `szenen/…/name.json` (`SCENE_LINK_RE`, `editor.js:14`, Prüfung `:2397–2398`). Alles andere wird abgelehnt und nicht geladen.
- Der `new Function`-Pfad ist entfernt, `evalExprJS` ist ein eigener Parser (`editor.js:2029`).
- Eine per Link geöffnete Szene sichert unter einem eigenen Schlüssel.

## 3. Lücken und Fehler, die unsere Abbildungen betreffen

**Grundlagen (für fast alle Abbildungen):**
- G1 Dezimalkomma fehlt an Achsenzahlen (`axes.py:10`, „0.5“, „2e-06“), in Wertelisten (`values` „2;2,5;3“ → vier Kurven, `scene_model.py:851`) und in Tabellen (Komma trennt Zellen, `figures.py:375`).
- G2 **Erledigt am 30.10.** (§6). Früher war der Export fest 1920×1080 ohne Zuschnitt; in der Artikelspalte wurden Tick-Zahlen dadurch nur etwa 8 px groß.
- G3 Kein Abschneiden am Teilbild außer bei FunctionGraph (F19). CurveFamily und Area klemmen am Rand und erzeugen waagerechte Linien (F2).
- G4 Mehrteilige Graphen verlieren Farbe und Stärke (F1): **erledigt am 30.10.** (§6). Offen: Stil-Attribute wirken bei anderen zusammengesetzten Objekten nur am obersten Objekt (F13).
- G5 **Erledigt am 28.10.** (§6). Unbekannte Props werden übersprungen und gemeldet (`scene_model.py:1342`), belegte Parameternamen ergeben eine klare Fehlermeldung (`:1662`).
- G6 **Erledigt am 28.10.** (§6). Katalogfarben bleiben erhalten. `WORLD_TYPES` der Oberfläche (`editor.js:1604`) ist gleich `_WORLD_TYPES` der Engine, und die Teilbildwahl wird für diese Typen nicht mehr angeboten (`editor.js:1504`).
- G7 Schrift im Editor ≠ Schrift im SVG (F17): teilweise behoben. Das SVG nutzt fest Arial und metrisch gleiche Schriften (`svg_painter.SVG_FONT`). Der Editor zeichnet `sans-serif`; das ist in Chrome unter Windows Arial (gemessen), auf anderen Systemen nicht zwingend.
- G8 Keine Mehrsprachigkeit. Szenen speichern Texte wörtlich, die Website ist fest deutsch, auch das Zahlformat hängt an der Sprache. Weg und Aufwand: `C:\Bücher\ET3\Arbeitshefte\ABBILDUNGEN_INVENTAR.md` Abschnitt 3 (Paket P2). Vorbereitet sind Ausgabepfad und `--lang` im Stapel-Export.

**Beschriftung:**
- B1 Formel-Labels ohne Brüche, Akzente, Kursiv, Drehung (F10). MathTex kann Brüche, ist aber nur in Weltkoordinaten setzbar und als Bauteil- oder Achsenlabel nicht nutzbar.
- B2 `f_\mathrm{A}` wurde zu „fmathrmA“: **erledigt am 30.10.** (§6).

**3D (Fläche I_C(U_BE, U_CE) mit Schnitten):**
- D1 Kein 3D-Kurvenobjekt. Schnittkurven nur per Hand als Polygon in der JSON.
- D2 `data_to_world` skaliert z nicht, `coords_to_point` schon (`axes.py:288` gegen `:300`). Text, Line, Polygon landen in falscher Höhe.
- D3 SVG-Export mit WebGL liefert statt der Fläche einen sinnlosen Pfad. PNG ist richtig.
- D4 WebGL-Fläche ohne Netzlinien, ohne Schnitt am z-Bereich, `origin` ignoriert. Höhenfarbe nur als Helligkeitsrampe. Szene in z nicht zentriert (z-Label abgeschnitten). `z_label` fehlt in der Oberfläche.
- D5 Die WebGL-Fläche reagiert nicht auf Animationen (Create wirkt nicht).

**Diagramm-Bausteine:**
- K1 Gerade durch zwei Punkte mit Verlängerung (Early-Konstruktion) fehlt. `Line` wird auf Log-Achsen krumm (F8).
- K2 CurveFamily: eine Farbe für alle Kurven, Labels überlappen.
- K3 Legende auf Log- oder ungleich skalierten Achsen unbrauchbar (F4): **erledigt am 30.10.** (§6). Offen: nur durchgezogene Einträge, keine gestrichelten oder Marker-Einträge.
- K4 Senkrechte Klammer: Label überdeckt die Klammer (F6), wichtig für die Potentialleiter.
- K5 Tabellen: gleich breite Spalten, keine Ausrichtung je Spalte.
- K6 Keine Tick-Listen im Konstruktor, `show_ticks` gilt für beide Achsen gemeinsam (`axes.py:73`, `:193`). Stand bisher nur in der Detailnotiz A.
- K7 Summation und Convolution zeichnen nur auf dem ersten Teilbild: Sie bekommen immer den ersten `Axes` (`scene_model.py:1679`, `:1718`).

**Animation und gerenderte Filme:**
- A1 Parameter über die Zeit animieren geht nicht (Parameter hängt an keinem ValueTracker). `ChangeValue` und `MoveAlongPath` sind registriert, brechen aber die Szene, weil die Argumente nicht durchgereicht werden.
- A2 Keine Kamerafahrt (für eine drehende 3D-Fläche).
- A3 Video nur in Echtzeit (MediaRecorder, 30 fps). Auf einem langsamen Rechner wird es länger und ungleichmäßig. Kein Bild-für-Bild-Rendern, kein GIF.
- A4 Keine Zeitleiste, nur „alles nacheinander“ oder „alles gleichzeitig“.

**Bedienung (später):**
- Kein Rückgängig, keine Mehrfachauswahl, kein Fang oder Raster, Ziehen nur über Achsenpfeile. Vorlage laden ersetzt die Szene ohne Rückfrage.

## 4. Abbildungen für ST1 Kapitel 4 und was sie brauchen

| Abbildung (Quelle BJT-Material) | braucht |
|---|---|
| Fläche I_C(U_BE, U_CE) mit zwei Schnitten | D1, D2, D3, D4, G1, G2; als Film zusätzlich A2, A3 |
| Zwei Dioden gegen Transistor (Schnittbild, Pfeile, Teilchen) | vorhanden, prüfen; G2 |
| Landkarte der Betriebsbereiche (Quadranten) | G1, G2, G3 |
| Kennlinienfelder (Eingang/Steuer, Ausgang mit I_B bzw. U_BE, Scharen) | G1, G3, G4, K2 |
| Kollektorstrom über U_CB und über U_CE (zwei Teilbilder) | G1, G3, K2 |
| Gummel-Plot und B(I_C) (log) | G1, G3, K1 (Geraden auf log) |
| Early-Konstruktion | K1, G1, G3 |
| Basisprofile (Einfluss von U_CE und U_BE) | G1, G3; Profile mit `DataCurve`/`FunctionGraph` |
| Maßstab ändert den Eindruck (drei Teilbilder) | G1 |
| Potentialleiter | K4, B1 |
| Bänderschema npn | vorhanden über `where()`, prüfen; G1 |
| Schaltzeichen npn/pnp mit Strömen | vorhanden; G6 (Farben) |
| Großsignal → Kleinsignal → MOSFET, T-Form, dynamisches ESB | vorhanden; G6, B1 (α·i_e, r_e ≈ 1/S) |
| Arbeitspunkt-Wahl (Kennlinie und Arbeitsgeraden) | G1 |
| MOSFET-Kennlinien zum Vergleich | G1, G3 |

## 5. Ausbaupakete in dieser Reihenfolge

1. **Sicherheit und Fundament:** §2; D2; G5; G6; G4.
2. **Abbildungen auf die Website:** Für feste 2D-Bilder erledigt (§6, 30.10.): Der Stapel-Export läuft in CPython, Playwright ist dafür nicht nötig. Offen bleiben nur die Fälle, die den Browser brauchen: MathTex und Σ/∏ im Zahlenmodus (MathJax) und Filme (Hook `window.__anim`, Bild für Bild als MP4/WebM mit ffmpeg). Dazu D3.
3. **Deutsche Zahlen:** G1 als Szeneneinstellung (Standard: Dezimalkomma).
4. **3D-Fläche mit Schnitten:** D1 (Kurve auf Fläche bzw. 3D-Parameterkurve, Punkte und Text in 3D), D4, D5; A2 (Kamerafahrt) für den Film.
5. **Kennlinien-Werkzeuge:** G3 (Abschneiden statt Klemmen), K2 (Farbe je Kurve, Labelabstand), K1 (verlängerte Gerade, gerade auch auf Log-Achsen).
6. **Beschriftung:** B1 (Brüche und Akzente in Formel-Labels oder MathTex in Datenkoordinaten), K4, K5.
7. **Animation:** A1 (Parameter animieren), A4 (Zeitleiste mit Startzeiten) nach Bedarf.

## 6. Erledigt

- **28.10. Sicherheit (§2):** Die Lücke war größer als gemeldet. Auch die Python-Engine ließ sich verlassen: `eval` ohne Builtins ist kein Schutz, `heaviside.__globals__['__builtins__']` erreichte `len` (Probe ergab 3), unter Pyodide also auch `import js`. Behoben:
  - `scene_model._safe_compile` prüft jeden Ausdruck gegen eine Positivliste der AST-Knoten. Erlaubt sind Zahlen, Namen, Operatoren und einfache Aufrufe, verboten sind Attribute, Indizes, `_`-Namen, Schlüsselwortargumente und Zeichenketten. Alle 9 Übersetzungsstellen nutzen sie.
  - `evalExprJS` ist ein eigener Parser ohne `new Function`.
  - `?scene=` nimmt nur `szenen/…/name.json`. Eine per Link geöffnete Vorlage sichert unter `animate.scene.v1:link` und überschreibt die eigene Szene nicht. Annahme und Ablehnung stehen in der Statuszeile.
  - Tests: `web/tests/test_security.py`, `web/tests/test_exprjs.mjs` (Node), Browser-Probe (Link-Regeln), `editor_ui_test.py` 18/18, alle Engine-Tests grün.

- **28.10. Paket 1, weitere Punkte:**
  - `data_to_world` skaliert z (D2).
  - Unbekannte Props werden übersprungen, belegte Parameternamen gemeldet (G5).
  - Katalogfarben bleiben erhalten, und die Welt-Typen von Oberfläche und Engine stimmen überein (G6).
- **28.10. Schaltplan-Bearbeitung wie in KiCad und LTspice (Wunsch des Users):**
  - **Platzierungsmodell:**
    - `Component` hat jetzt `center`, `rotation` (0/90/180/270) und `length` (Pin-Abstand, Standard 2 = 4 Rasterschritte). Liegt die Mitte auf dem Raster 0,5, liegen beide Pins darauf.
    - Alte `start`/`end`-Szenen funktionieren weiter. Der Editor rechnet sie beim Laden um, die Engine liest beide Formen.
    - Die Symbolgrößen sind fest. Der Widerstand ist ein IEC-Kasten 3:1, unabhängig vom Pin-Abstand.
  - **Darstellung je Element** (`symbol_style` europäisch/amerikanisch):
    - Widerstand: Kasten oder Zickzack mit 3 Perioden, auch bei einstellbarem und nichtlinearem Widerstand.
    - Induktivität: gefüllter Balken oder Windungen.
    - Spannungsquelle: Strich in Leitungsrichtung oder ±.
    - Stromquelle: Querstrich oder Pfeil.
    - Gesteuerte Spannungsquelle: Strich oder ±.
    - Sicherung: Kasten mit Strich oder S-Kurve.
    - Operationsverstärker und Verstärker: IEC-Kasten mit ▷ (und ∞) oder Dreieck.
  - **Schaltplanfeld:** Das erste Schaltplan-Element legt ein 1:1-Feld (`schematic:true`) an und schaltet auf 2D.
  - **Bearbeitungshilfen** auf dem Overlay, nie exportiert:
    - Punktraster 0,5, ein- und ausschaltbar (Taste G, Häkchen „Raster“),
    - offene Pins als rote Ringe,
    - Auswahlrahmen.
  - **Bedienung:**
    - Ein neues Bauteil hängt am Cursor und wird per Klick eingerastet abgesetzt.
    - R dreht, M spiegelt, Esc bricht ab, Entf löscht.
    - Bauteile werden am Körper gezogen und rasten ein. Leitungsenden an ihren Pins folgen.
  - **Verdrahten:**
    - Ziehen von einem Pin oder Leitungsende erzeugt ein `Wire`-Element. Es endet am Pin unter dem Cursor oder rastet sonst auf das Raster.
    - Die Führung ist rechtwinklig, hv oder vh je nach erster Zugrichtung.
    - Umschalt-Ziehen beginnt überall, etwa mitten auf einer Leitung.
    - An T-Verbindungen und bei 3 oder mehr Anschlüssen setzt der Editor automatisch einen Lötpunkt.
  - **Weiteres:**
    - Neue Bauteile werden fortlaufend benannt (R_1, R_2, …).
    - Schaltplan-Elemente sind standardmäßig schwarz (#000000).
  - **Engine und Backend:** `circuit.component_ends`, `device_pin_offsets`, `pins_world`, Backend `circuit_pins()` und `panel_affine()`.
  - **Tests:**
    - `web/tests/test_circuit_place.py` (Pins, Drehung, alte Szenen, alle 25 Arten in beiden Normen, 3:1, Device-Pins),
    - `tools/editor_schematic_test.py` (Browser: Platzieren, Drehen, Verdrahten, Mitziehen, T-Verbindung mit Lötpunkt, Spiegeln, Stilwechsel),
    - `editor_ui_test.py` 18/18.

- **30.10. Von der Szene zum Artikelbild (Paket P1 aus `ABBILDUNGEN_INVENTAR.md`):**
  - **Ausschnitt** (`engine/export.py`, Einstellung `export` in der Szene): wie `bbox_inches="tight"` in matplotlib, „Zeichnung exportieren“ in Inkscape und der Exportbereich in GeoGebra.
    - `content` (Standard): alles Gezeichnete mit halber Strichbreite und geschätzter Textbreite plus Rand 24 px, begrenzt auf die 1920×1080-Fläche.
    - `frame`: fester Rahmen `[x0, y0, x1, y1]` in Welt-Einheiten der 2D-Ansicht.
    - `canvas`: die ganze Fläche wie bisher.
  - **Größe:** Das SVG behält die Szenen-Pixel im `viewBox` und wird mit Maßstab 0,55 angezeigt. Beschriftungen mit 24/26/28 px erscheinen dadurch mit 13,2/14,3/15,4 px.
  - **Spaltenbreite (gemessen in Chrome):** Der Artikel ist 616 px breit, eine Abschnittskarte innen 570 px, das Bild im Abbildungskasten höchstens 548 px (`export.COLUMN_PX`). Die 680 px im CSS von `figure.fig` werden nie erreicht. Ein breiteres Bild verkleinert der Browser samt Text; Editor und Stapel-Export melden das mit der entstehenden Textgröße. Abhilfe ist eine schmalere Zeichnung, denn Textgrößen sind fest. Auf dem Handy (308 px) schrumpft jedes breite Bild.
  - **Textbreite:** Sie kommt aus den Laufweiten von Helvetica/Arial. Das SVG nutzt dazu fest Arial und metrisch gleiche Schriften. Chrome misst an der Demo-Szene Ränder von 24,0–24,6 px bei 24 px Soll.
  - **Hintergrund:** Das Nachtmodus-Grau #d4d7dc wird weiß. Transparenz und eigene Farben bleiben.
  - **Oberfläche:** Settings zeigt den Abschnitt „Artikelbild (SVG-Export)“ mit Ausschnitt, Rand, Maßstab, Rahmen und dem Knopf „Rahmen = jetziger Zuschnitt“. Solange Settings gewählt ist, steht der Ausschnitt als orangefarbener Rahmen mit Größe und Textgröße auf dem Overlay (zu breit: rot). Er wird nie exportiert.
  - **Stapel-Export ohne Browser:** `python tools/export_szenen.py [namen…] [--out DIR] [--lang de] [--check]` schreibt `web/abbildungen/<sprache>/<szene>.svg`. Ohne Namen nimmt es alle Szenen unter `web/szenen/`. Es setzt die Szene um wie der Editor beim Laden (`ensureDefaults`, `toPythonModel`, Katalog über node). Das Ergebnis ist byteweise gleich dem SVG-Export im Browser (geprüft an `beispiel-zwei-felder`). MathTex und Σ/∏ im Zahlenmodus fehlen im Bild und werden gemeldet.
  - **Artikel-Block:**
    ```
    :::abbildung et3/k1-bode
    Bildunterschrift, auch mit $f_\mathrm{A}$ und **Markdown**, über mehrere Zeilen.
    :::
    ```
    - Name = Pfad unter `web/szenen/` ohne `.json`.
    - Ergebnis: `<figure class="abb">` mit dem SVG in natürlicher Größe (höchstens spaltenbreit), Alternativtext aus der Bildunterschrift, „Abbildung N“ je Artikel fortlaufend und Link „In Editor öffnen“.
    - Fehlt das SVG oder ist der Name ungültig, erscheint ein Platzhalter wie bei `:::grafik`, die Nummer bleibt reserviert, und der Build meldet es. `:::grafik` funktioniert unverändert.
    - Nach einer Änderung an CSS oder Abbildungen `python build_wissen.py` laufen lassen.
  - **Sicherheit des Links:** Der Link nutzt den vorhandenen Pfad `editor.html?scene=szenen/<szene>.json`. Der war bereits sicher (§2), ein zweiter Ladepfad wäre nur mehr Angriffsfläche. Die Regel steht jetzt als `SCENE_LINK_RE` an einer Stelle; `test_abbildung` prüft, dass sie genau die Namen annimmt, die der Build erzeugt. In der Browser-Probe wurden fremde Hosts, `..`, Query und `javascript:` abgelehnt, ohne dass etwas geladen wurde.
- **30.10. Darstellungsfehler (Paket P3, teilweise):**
  - **F1:** Teilstücke eines Graphen übernehmen Farbe, Stärke, Deckkraft und Strichelung (`plotting.sync_pieces`), auch bei Operationen, Faltung und den Animationen in `processes.py`.
  - **Rich-Text:** `f_\mathrm{A}`, `f_\mathrm A`, `x^\text{max}` und `\mathrm A` werden richtig gesetzt (`richtext._macro_arg`).
  - **Legende:** Nur `position` ist eine Datenkoordinate. `row_gap`, `swatch_len` und `gap` sind Szenen-Einheiten, Labels sind linksbündig (`scene_model._ANCHORED_TYPES`). Neue Standardwerte 0,35/0,4/0,15 entsprechen bei 26 px ungefähr matplotlib. Gespeicherte Szenen behalten ihre Werte und sehen auf 1:1-Achsen aus wie bisher, aber die Labels stehen jetzt linksbündig; auf anderen Achsen ändern sich die Abstände wie gewollt.
  - **Noch offen aus P3:** `label_side` für LabeledArrow, gestrichelte und Marker-Einträge in der Legende.
  - **Tests:** `web/tests/test_render_fixes.py`, `test_export.py`, `test_abbildung.py`, neuer Fall in `test_contract.py`, Ergänzungen in `tools/editor_ui_test.py`.

Jedes Paket hält `web/ENGINE_CONTRACT.md` ein. Es kommt mit Tests in `web/tests`, wird im Browser fotografiert (`tools/editor_shot.py`) und mit `tools/editor_ui_test.py` geprüft. Abgeschlossene Punkte werden hier abgehakt.
