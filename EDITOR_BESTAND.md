# Editor: Bestand und Ausbauplan (Stand 28.10.2026)

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
- **Export:** PNG immer, SVG in 2D, MP4/WebM als Echtzeit-Aufnahme.
- **Tests:** `editor_ui_test.py` 18/18, `test_figures`, `test_contract`, `test_3d`, `test_axes`, `test_axes3d`, `test_canvas`, `test_steps` grün.

## 2. Sicherheitsbefund (zuerst beheben)

`editor.html?scene=<url>` lädt eine beliebige Adresse (`editor.js:2011`). Σ/∏-Terme aus der Szene werden mit `new Function` ausgeführt (`editor.js:1699–1703`). Ein präparierter Link kann deshalb beliebiges JavaScript auf der Website starten. Außerdem überschreibt jeder Link die automatisch gesicherte Szene.
Abhilfe: `?scene=` nur für relative Pfade unter `szenen/`. `evalExprJS` durch einen kleinen Ausdrucksparser ohne `new Function` ersetzen. Vor dem Überschreiben der Sicherung fragen oder sie getrennt halten.

## 3. Lücken und Fehler, die unsere Abbildungen betreffen

**Grundlagen (für fast alle Abbildungen):**
- G1 Dezimalkomma fehlt an Achsenzahlen (`axes.py:10`, „0.5“, „2e-06“), in Wertelisten (`values` „2;2,5;3“ → vier Kurven, `scene_model.py:810`) und in Tabellen (Komma trennt Zellen, `figures.py:375`).
- G2 Export fest 1920×1080, kein Zuschnitt auf den Inhalt (`editor_backend.py:16`).
- G3 Kein Abschneiden am Teilbild außer bei FunctionGraph (F19). CurveFamily und Area klemmen am Rand und erzeugen waagerechte Linien (F2).
- G4 Mehrteilige Graphen verlieren Farbe und Stärke (F1). Stil-Attribute wirken nur am obersten Objekt (F13).
- G5 Unbekannte Prop bricht die ganze Szene ab (F14). Parameternamen wie `u`, `e`, `max` werden still verworfen (F11).
- G6 Oberfläche: Automatikfarben überschreiben Katalogfarben, neue Schaltplan-Bauteile werden farbig, TextBox-Text unsichtbar (C §1). MathTex und Vector: Oberfläche und Engine behandeln Koordinaten verschieden, Objekte springen beim Ziehen (F12).
- G7 Schrift im Editor ≠ Schrift im SVG (F17).

**Beschriftung:**
- B1 Formel-Labels ohne Brüche, Akzente, Kursiv, Drehung (F10). MathTex kann Brüche, ist aber nur in Weltkoordinaten setzbar und als Bauteil- oder Achsenlabel nicht nutzbar.

**3D (Fläche I_C(U_BE, U_CE) mit Schnitten):**
- D1 Kein 3D-Kurvenobjekt. Schnittkurven nur per Hand als Polygon in der JSON.
- D2 `data_to_world` skaliert z nicht, `coords_to_point` schon (`axes.py:288` gegen `:300`). Text, Line, Polygon landen in falscher Höhe.
- D3 SVG-Export mit WebGL liefert statt der Fläche einen sinnlosen Pfad. PNG ist richtig.
- D4 WebGL-Fläche ohne Netzlinien, ohne Schnitt am z-Bereich, `origin` ignoriert. Höhenfarbe nur als Helligkeitsrampe. Szene in z nicht zentriert (z-Label abgeschnitten). `z_label` fehlt in der Oberfläche.
- D5 Die WebGL-Fläche reagiert nicht auf Animationen (Create wirkt nicht).

**Diagramm-Bausteine:**
- K1 Gerade durch zwei Punkte mit Verlängerung (Early-Konstruktion) fehlt. `Line` wird auf Log-Achsen krumm (F8).
- K2 CurveFamily: eine Farbe für alle Kurven, Labels überlappen.
- K3 Legende auf Log- oder ungleich skalierten Achsen unbrauchbar (F4). Wir beschriften ohnehin direkt an den Kurven.
- K4 Senkrechte Klammer: Label überdeckt die Klammer (F6), wichtig für die Potentialleiter.
- K5 Tabellen: gleich breite Spalten, keine Ausrichtung je Spalte.

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
2. **Abbildungen auf die Website:** Hook `window.__anim` in `editor.js`. Ein Skript rendert alle Szenen unter `web/szenen/` headless (Playwright) als zugeschnittenes SVG/PNG und Bild für Bild als MP4/WebM (ffmpeg). Block `:::abbildung` in `build_wissen.py` mit Bild oder Film und dem Link „In der Vorlage öffnen“. Dazu G2, G7 und D3.
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

Jedes Paket hält `web/ENGINE_CONTRACT.md` ein. Es kommt mit Tests in `web/tests`, wird im Browser fotografiert (`tools/editor_shot.py`) und mit `tools/editor_ui_test.py` geprüft. Abgeschlossene Punkte werden hier abgehakt.
