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
- Animation eines Parameters als Film (§8, §15): der Regler wirkt nur auf das Standbild.
- Hystereseschleife mit laufendem Punkt (§20), rotierender Zeiger (§8), bewegte Teilchen (§14).
- Ausschnittvergrößerung mit Verbindungslinien (§22), Rauschsignale mit festem Startwert (§21).
- Gekoppelte Hervorhebung zwischen Querschnitt und Ersatzschaltbild (§38), Matrixaufbau als Animation (§31).
- Echter LaTeX-Satz (Brüche, Wurzeln) in allen Beschriftungen (F28): dafür weiter `MathTex`.
