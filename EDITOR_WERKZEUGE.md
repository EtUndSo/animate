# Editor-Werkzeuge für die Artikel-Abbildungen

Stand 27.10.2026. Abgeleitet aus `ABBILDUNGEN_LISTE.md` (214 geplante Abbildungen in 23 Themen) und
`EDITOR_GRAFIK_FEATURES.md` (§1 bis §39). Die Zahl in Klammern gibt an, wie oft ein Abschnitt in der
Abbildungsliste als nötig genannt wird. Reihenfolge = Bauplan: erst das Fundament, das fast jede Abbildung
braucht, dann die Werkzeuge mit der größten Abdeckung. Jedes Werkzeug ist allgemein gehalten (Parameter,
Presets, freie Ausdrücke), nie auf eine Einzelszene zugeschnitten.

Status „fertig“ heißt: gebaut, Engine-Tests grün (`web/tests/test_figures.py`, `test_contract.py` und alle
übrigen), im echten Browser gerendert und angesehen (`tools/editor_shot.py`), Bedienung geprüft
(`tools/editor_ui_test.py`). Vom User noch nicht getestet.

## A. Fundament

| Nr. | Werkzeug | Was es kann | Für § | Status |
|---|---|---|---|---|
| A1 | Strichlinien | Eigenschaft `dash` an Linien, Graphen, Pfeilen, Formen, Kurven: Auswahl solid, dashed, short, dotted, dash-dot oder frei „an,aus“ in Pixeln; Pfeilspitzen und Punkte bleiben durchgezogen | §4, §16, §28, §32, §37 | fertig |
| A2 | Formel-Labels | Jede Beschriftung versteht `U_{GS}`, `I_D`, `10^{-16}`, verschachtelt `e^{U/U_T}`, griechische Buchstaben (`\alpha`, `\Omega`, `\mu`), Zeichen (`\cdot`, `\approx`, `\le`, `\minus`), Leerräume (`\,`), Zeilenumbruch `\\`; Ausrichtung links, mittig, rechts | §2, §7 und alle Beschriftungen | fertig |
| A3 | Teilbilder | Mehrere `Axes` in einer Szene: `origin` setzt das Teilbild auf die Leinwand, `title` beschriftet es („(a)“); jedes Objekt wählt in den Eigenschaften sein Achsensystem; ein neues Objekt landet im gerade gewählten Teilbild; `show_axes:false` macht ein Teilbild zum reinen Platzierungsrahmen (Schaltplan, Querschnitt, Blockbild) | §10 (137), §13 (26), §22 | fertig |
| A4 | Achsen erweitert | `x_log`, `y_log` mit Dekaden 10^k, Zwischenstrichen und Gitter; Pfeilspitzen (`arrows`); Zahlen je Achse abschaltbar (`x_numbers`, `y_numbers`); x-Achse unten statt bei y = 0 (`x_axis_at:bottom`), y-Achse links (`y_axis_at:left`); Linienstärke (`axis_width`) | §12 (23), §4, §13, §32, §37 | fertig |
| A5 | Parameter | Objekt `Parameter` (Name, Wert, min, max, Schritt) mit Schieberegler; der Name gilt in allen Ausdrücken der Szene wie eine Konstante; die Szenenliste zeigt „Name = Wert“ | §15 (52), §29, §36, §37 | fertig |
| A6 | SVG-Export | „Photo ▾ → SVG (Vektor)“ speichert die Szene als Vektorgrafik (Pfade, Text mit Hoch- und Tiefstellung, Strichlinien) für die Website | Einbindung in Artikel | fertig |
| A7 | Szene per Link | `editor.html?scene=szenen/<datei>.json` lädt eine gespeicherte Szene; Ablage `web/szenen/` (Beispiel `beispiel-emitterschaltung.json`) | §9 | fertig |

## B. Diagramme

| Nr. | Werkzeug | Was es kann | Für § | Status |
|---|---|---|---|---|
| B1 | Datenkurve | `DataCurve` aus eingefügter Wertetabelle (`x y` je Zeile oder `x,y;x,y`), wahlweise mit Punkten und geglättet; passt direkt zum Zahlenwerk | §11 (78), §32, §33 | fertig |
| B2 | Bereich | `Band`: Rechteck in Datenkoordinaten, wahlweise über die volle Höhe oder Breite, Beschriftung oben, mittig oder unten (Sperr-, Sättigungs-, Raumladungszonen, Frequenzbänder) | §4 (79), §13, §25 | fertig |
| B3 | Pfeile erweitert | `LabeledArrow`: Doppelspitze, Strichlinie, Knick (`elbow` hv oder vh), Mengenpfeil mit Breite proportional zum Wert (`thick`), Beschriftung neben dem längsten Stück; `LoopArrow` mit `head:false` als Bogen oder Winkelmarke | §2 (62), §18 (9), §19 | fertig |
| B4 | Stiele und Spektrallinien | `Stem`: Stiele aus Wertelisten mit Punkt und Beschriftung je Stiel; Grundlinie wählbar | §25, Abtastung | fertig |
| B5 | Teilchenwolke | `PointCloud`: n Punkte mit festem Zufallsstartwert, gleichverteilt oder exponentiell abfallend, gefüllt (Elektronen) oder hohl (Löcher) | §14 (8), §36 | fertig |
| B6 | Tangente und Steigungsdreieck | `TangentLine` mit `triangle_dx`: Dreieck mit beschriftetem Δx und Δy; auf logarithmischen Achsen ist die Tangente die im Bild gerade Linie (eine Dekade je 59,5 mV) | §37 (21), §4 | fertig |
| B7 | Freie Form mit Material | `Shape`: Polygon aus Punktliste, Füllung nach Material (n, p, n⁺, p⁺, Oxid, Poly, Metall, Raumladungszone, Substrat), Beschriftung in der Mitte | §27 (22), §36 (19), §6 | fertig |
| B8 | Ellipse und Bogen | `Ellipse` (Mitte, Breite, Höhe); Bogen über `LoopArrow` ohne Spitze | §7 | fertig |
| B9 | Berechnete Punkte | `Marker`: `x_expr` (mit Parametern), `func` (Punkt sitzt auf der Kurve), `func`+`func2` (Schnittpunkt, etwa Arbeitspunkt aus Kennlinie und Arbeitsgerade), `y_expr`; Hilfslinien gestrichelt zu den Achsen; Beschriftungsseite wählbar | §4, §8, §15, §37 | fertig |
| B10 | Kennlinienscharen | `CurveFamily`: feste Parameterwerte (`values` „2;2,5;3“) statt gleichmäßiger Schritte, Beschriftung am rechten Ende jeder Kurve (`labels`) | §4, §37 | fertig |

## C. Beschriftung, Kästen, Tabellen

| Nr. | Werkzeug | Was es kann | Für § | Status |
|---|---|---|---|---|
| C1 | Textkasten | `TextBox`: mehrzeiliger Formeltext in Rechteck, abgerundetem Rechteck, Raute oder Ellipse; Größe passt sich dem Text an | §19 (14), §7 (46) | fertig |
| C2 | Geschweifte Klammer | `Brace` zwischen zwei Punkten, Beschriftung außen, Seite umschaltbar | §7 | fertig |
| C3 | Haken, Kreuz, Durchstreichen | `Mark` mit `check`, `cross`, `strike` | §7, §34, §37 | fertig |
| C4 | Tabelle und Matrix | `Table`: Zellen „a,b;c,d“, Zeilen- und Spaltenköpfe, hervorgehobene Zellen, wahlweise Matrixklammern statt Gitter | §31 (13), §33, §35 | fertig |

## D. Schaltpläne

| Nr. | Werkzeug | Was es kann | Für § | Status |
|---|---|---|---|---|
| D1 | Zweipole | `Component` zwischen zwei Punkten, 25 Arten: Widerstand (auch nichtlinear, einstellbar), Kondensator (auch einstellbar), Spule, Diode, Z-Diode, LED, Spannungs-, Gleich-, Strom-, Wechselquelle, vier gesteuerte Quellen (Raute), Schalter, Lampe, Ampere- und Voltmeter, Sicherung, Nullator, Norator, Draht. Name und Wert auf einer Seite (umschaltbar), Strompfeil auf einer Zuleitung (Anfang oder Ende, umkehrbar), Spannungspfeil auf der anderen Seite (umkehrbar) | §1 (99), §28 (34), §31, §34 | fertig |
| D2 | Mehrpole und Blöcke | `Device`, 25 Arten: npn, pnp, NMOS und PMOS in vier Schreibweisen (Pfeil an der Source, DIN mit Bulk, selbstleitend, Digitaltechnik mit Kreis am Gate), n-JFET, Operationsverstärker, Verstärker, Zweitor, Masse, Klemme, Knoten, Triode, Mischer, Summierstelle, Oszillator, Tief-, Band-, Hochpass, AD-Umsetzer, Antenne. Drehbar, spiegelbar, Anschlüsse beschriftet; Anschlüsse liegen bei Größe 1 auf runden Koordinaten (Liste im Kopf von `web/engine/circuit.py`) | §1, §24 (14), §35 (9), §28 | fertig |
| D3 | Leitungen und Knoten | `Wire`: Linienzug, wahlweise rechtwinklig geführt, Lötpunkte an gewählten Punkten; `Node`: Knotenpunkt mit Namen | §1, §30 | fertig |

## E. Vorlagen und Prüfung

| Nr. | Werkzeug | Was es kann | Status |
|---|---|---|---|
| E1 | Vorlagen | Menü „Elektrotechnik · Vorlagen“: Kennlinienfeld mit Arbeitspunkt (Regler U_B), Diodenkennlinie halblogarithmisch, Bode-Diagramm Tiefpass (Regler f_g), Schaltplan Emitterschaltung, Kleinsignal-Ersatzschaltbild, Querschnitt NMOS, Wirkungskette Gegenkopplung. Quelle: `tools/editor_vorlagen.py` (fügt sie in `web/editor.js` ein) | fertig |
| E2 | Tests | `web/tests/test_figures.py` (alle neuen Objekte, jede Bauteilart, Log-Achsen, Teilbilder, Parameter, Schnittpunkt, Tangente auf Log-Achse, SVG); Vertragstest um eine Szene mit allen neuen Objekten und Animationen erweitert; `tools/editor_shot.py` (Szene im Browser fotografieren); `tools/editor_ui_test.py` (18 Bedienprüfungen) | fertig |

## F. Ergänzungen vom 10.11.2026 (Text, Ebenen, Rechenbilder)

Anleitung mit Beispielen: `notizen/animationen.md` §7. Tests: `web/tests/test_text_werkzeuge.py`, `test_texspec.mjs`.

| Nr. | Werkzeug | Was es kann | Status |
|---|---|---|---|
| F1 | Schreibmaschinenschrift | `Text.font` = mono: echte Zeichen in Zellen von 0,6 em, Spalten untereinander, mehrere Leerzeichen, gerade `'` und `` ` ``, kein Dezimalkomma; chinesische Zeichen zwei Zellen; gleich in Editor, `.svg`, `.anim.svg` und PDF (Consolas). `szenen_lib`: `s.text(..., schrift="tt")`, `tt_breite()` | fertig |
| F2 | Rohtext | `Text.raw`: der Text wörtlich, ohne Rich-Text (`_ ^ \ $ { }`), echter Zeilenumbruch bricht. `s.text(..., roh=True)` | fertig |
| F3 | Inhalt ändern | Transform Text → Text ändert Inhalt, Farbe, Größe, Lage, Schrift (aus-/einblenden), ohne Rest im Bild. `s.ersetzen(id, text, farbe)` | fertig |
| F4 | Ebenen | Szenen-Einstellung „Ebenen“: wie angelegt (`drawOrder: creation`, Standard für neue Szenen) / wie erschienen (bisher). `Szene(..., reihenfolge="anlegen")`; der Export warnt bei Text unter deckender Fläche | fertig |
| F5 | Richtungsmarke | `ParametricCurve.head_size` (Standard 0,22). `s.weg(..., spitze=…)` | fertig |
| F6 | Σ/∏ erweitert | `index` (anderer Laufindex), `exact` (exakte Brüche, beliebiger Nenner). `s.summe(..., index="k", exakt=True)` | fertig |
| F7 | Code in Formeln | `\mathtt{a.b}` ohne Abstand, gerade `'`/`` ` `` in `\texttt`, Code mit Klammern behält den Dezimalpunkt (`localizeTex`) | fertig |

## G. Parameter über die Zeit (L3, 10.11.2026)

Anleitung mit Beispielen: `notizen/animationen.md` §8. Vertrag: `web/ENGINE_CONTRACT.md` „Parameters over time“.
Tests: sechs L3-Fälle in `web/tests/test_contract.py`. Vorführszenen: `tools/szenen/beispiel_parameter.py`.

| Nr. | Werkzeug | Was es kann | Status |
|---|---|---|---|
| G1 | Parameter verstellen | Animation `ChangeValue` auf ein Objekt `Parameter` (Ziel `value`: Zahl oder Ausdruck wie `2*pi`; `rate`: smooth oder linear). Mehrere Parameter im selben Schritt laufen gleichzeitig. Im Editor: Parameter wählen, Animationen ▸ Parameter ▸ „+ Verstellen (ChangeValue)“, Felder „to value“ und „rate“. `szenen_lib`: `s.parameter("t", 0)`, `s.verstellen("t", "2*pi", dauer=4, rate="linear")` | fertig |
| G2 | Mitlaufende Objekte | Jedes Objekt, dessen Eigenschaften einen bewegten Parameter nennen, wird in jedem Bild neu gebaut: Funktionsgraph (auch Grenzen `x_range [0, "t"]`), Fläche (Grenzen), Marker (Punkt auf Kurve, gestrichelte Projektionen), Tangente (`x0`), Strecke, Pfeil/Zeiger, Kreis, Punkt, Wege (`t_max`) | fertig |
| G3 | Ausdrücke in Zahlenfeldern | Koordinaten und Zahlen dürfen Ausdrücke mit Parametern sein (`["r*cos(phi)", "r*sin(phi)", 0]`, `x_max: "b"`). Im Editor werden die Zahlenfelder zu Textfeldern, sobald die Szene einen Parameter hat; ein Ausdruck ohne Parameter (`2*pi`) wird dort sofort zur Zahl | fertig |
| G4 | Zahlenanzeige | Objekt „Zahlenanzeige“ (`DecimalNumber`): `value` = Ausdruck, `decimals`, `prefix`, `suffix`, `align`; Dezimalzeichen und Minus nach Sprache. `s.zahl(on, "t", pos, stellen=2, vor="t = ", nach=" s")` | fertig |
| G5 | Ganzzahliger Parameter | `Parameter.integer`: springt von Zahl zu Zahl, jede gleich lang (Grenzprozesse). `s.parameter("n", 1, ganzzahlig=True)` | fertig |
| G6 | Parameter t | Ein Parameter darf `t` heißen (Zeit): Er ersetzt dann in allen Ausdrücken der Szene die Variable t; Graphen in x schreiben (`sin(x - c*t)`). Parameter- und Polarkurven behalten ihr eigenes t | fertig |
| G7 | Export | Unter einem Parameter feste Abtastung (Graph 121 Punkte oder `samples`, Fläche `samples` mit glatter Oberkante): Zahlenspur „q“ (Toleranz 0,4 Szenenpixel), Zeichnen dazu als Teilstück „p“; Zahlenanzeigen mit kurzen Inhaltsbildern. Spieler unverändert | fertig |

## Nebenbei behobene Fehler

- Wissenschaftliche Schreibweise in Ausdrücken: `1e-15` wurde als `1·e − 15` gelesen. Jetzt eine Zahl.
- Funktionsnamen mit Ziffer am Ende (`log10`, `log2`) bekamen ein Malzeichen vor die Klammer und lieferten nichts.
- Kurvenschar, Polarkurve und Skalarfeld bekamen ihren Ausdruck bereits kompiliert und konnten ihn nie auswerten; sie erhalten jetzt den Ausdruckstext.
- Die Create-Animation entschied in jedem Bild neu, welche Teilpfade sie zeichnet; bei Objekten mit eigenem Pfad und Kindern (Datenkurve mit Punkten) war das Bild deshalb von der Abspielreihenfolge abhängig.
- Flächen, Stiele und Hilfslinien liefen auf logarithmischen Achsen zur nicht vorhandenen Null; sie enden jetzt an der Achse.
- Beschriftungen mit Wörtern in Großbuchstaben wie „UP“ wurden als interne Konstante gelesen.

## Bedienhinweise

- Teilbild anlegen: zweites `Axes` hinzufügen, `origin` setzen, verkleinern (`x_length`, `y_length`). Ein Objekt wechselt das Teilbild über das Feld `axes` in seinen Eigenschaften.
- Gestapelte Diagramme: gleiche `x_range` und `x_length`, oberes Teilbild mit `x_numbers:false`, unteres mit `x_axis_at:bottom`.
- Arbeitspunkt: `Marker` mit `func` = Kennlinie und `func2` = Arbeitsgerade; mit einem `Parameter` in der Arbeitsgeraden wandert er am Regler mit.
- Schaltplan: ein Teilbild mit `show_axes:false` und `x_range [-7,7]`, `x_length 14`, `y_range [-4,4]`, `y_length 8` macht Daten- gleich Leinwandeinheiten; Bauteile und Leitungen dann auf ganzen oder halben Koordinaten.

## Noch offen

Nicht in dieser Runde gebaut, weil selten gebraucht oder mit eigenem Unterbau:

- Achsenbruch und abschnittsweiser Maßstab (§17, 9 Nennungen): braucht eine stückweise Achsenabbildung.
- Hystereseschleife mit laufendem Punkt (§20) als fertige Vorlage (mit G1/G2 baubar), bewegte Teilchen (§14).
- Ausschnittvergrößerung mit Verbindungslinien (§22), Rauschsignale mit festem Startwert (§21).
- Gekoppelte Hervorhebung zwischen Querschnitt und Ersatzschaltbild (§38), Matrixaufbau als Animation (§31).
- Echter LaTeX-Satz (Brüche, Wurzeln) in allen Beschriftungen (F28): dafür weiter `MathTex`.
