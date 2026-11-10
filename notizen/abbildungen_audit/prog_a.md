# Abbildungen und Animationen — Paket prog_a (Hefte prog/01 und prog/02)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln, Szenen oder Werkzeugen geändert.
Hefte: `content/prog/01-programme-und-der-python-interpreter/` (Artikel 01–08) und `content/prog/02-werte-typen-und-variablen/` (Artikel 01–12); alle deutschen Artikel ganz gelesen.
Bestand: 16 Abbildungen (`prog/k1…`, `prog/k2…`). Zusammensetzung: 12 Zeichnungen aus Text/TextBox/Line/Dot/LabeledArrow; 1 echte Rechenoperation (prog/k2rbyte, Summation); 3 „Rechenbilder“, die nur ein einziger statischer MathTex sind (prog/k2rbinaer, k2rnull, k2rfloat, ohne Operation). Keine Szene hat eine Animation (`animations` leer).
Hinweis zu den Programmabläufen: Ein Code-Objekt mit Zeilen-Hervorhebung fehlt (L8). Alle Vorschläge zu Programmläufen geben deshalb einen Behelf an: Programmzeilen als Textzeilen, ein Rechteck als Zeilenmarke, das per Shift wandert, daneben Namen-/Wert-Tabelle (Table) oder Zustandsdiagramm und ein Terminal-Kasten.

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| prog/01/01-programme-und-der-python-interpreter | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| prog/01/02-programme-und-programmiersprachen | 4 | 1 | 2 | 1 | 0 | 0 | 4 |
| prog/01/03-vom-quelltext-zur-ausfuhrung-compiler-und-interpreter | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| prog/01/04-python-einrichten | 4 | 0 | 2 | 1 | 1 | 0 | 4 |
| prog/01/05-der-interaktive-modus | 5 | 0 | 3 | 2 | 0 | 0 | 5 |
| prog/01/06-skripte-schreiben-und-ausfuhren | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| prog/01/07-fehler-lesen-und-verstehen | 5 | 2 | 1 | 1 | 1 | 0 | 5 |
| prog/01/08-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| prog/02/01-werte-typen-und-variablen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| prog/02/02-objekte-und-typen | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| prog/02/03-ganze-zahlen-und-rechenoperatoren | 5 | 1 | 2 | 1 | 0 | 0 | 4 |
| prog/02/04-zahlen-im-binarsystem | 5 | 3 | 3 | 0 | 0 | 1 | 5 |
| prog/02/05-gleitkommazahlen-der-typ-float | 5 | 3 | 2 | 0 | 0 | 0 | 5 |
| prog/02/06-rechnen-mit-gleitkommazahlen | 4 | 0 | 3 | 1 | 0 | 0 | 4 |
| prog/02/07-variablen-namen-fur-objekte | 4 | 1 | 1 | 2 | 0 | 0 | 4 |
| prog/02/08-wahrheitswerte-und-vergleiche | 4 | 0 | 2 | 2 | 0 | 0 | 4 |
| prog/02/09-module-math-und-sys | 3 | 0 | 1 | 1 | 1 | 0 | 3 |
| prog/02/10-komplexe-zahlen | 5 | 2 | 1 | 1 | 1 | 0 | 5 |
| prog/02/11-zeichenketten-eingabe-und-ausgabe | 4 | 0 | 3 | 1 | 0 | 0 | 4 |
| prog/02/12-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Summe** | 70 | 16 | 33 | 17 | 4 | 1 | 69 |

Bemerkungen zur Bilanz: Kein Artikel liegt über 5 oder unter 1; kein Soll wurde überschritten. Bei prog/02/03 bleibt es bei 4 von 5 (verworfen: Blockbild 125 // 60 mit 2 Stunden und 5 Minuten, k2rest deckt Quotient und Rest ab). Verworfen außerdem: Hexadezimal-Vierergruppen (prog/02/04, über Soll), erweiterte Zuweisung `zaehler += 1` (prog/02/07, gleiches Muster wie k2etikett), `None` als Wert eines Aufrufs (prog/02/08, bei V13 mit abgedeckt), Zehnmal-0,1-Aufsummieren (prog/02/06, über Soll). Eulersche Formel (prog/02/10): HM-Szene hm1/k7euler existiert; Verweis statt neuer Abbildung.

## Top 3

- V37 [A] prog/02/07 — die Zuweisungszeilen des Ohm-Beispiels Zeile für Zeile: Name zeigt auf Objekt, Kasten entsteht, Pfeil wird gesetzt — Grundbild für alles Folgende (`y = x` kopiert nichts, Schleifen, Funktionen), bisher nur Satz und ein statisches Bild.
- V33 [A] prog/02/06 — `0.1 + 0.2`: exakt rechnen, auf den Gleichstand zweier `float` stoßen, zur geraden Mantisse runden — die berühmteste Überraschung des Heftes, bisher eine Tabelle voller 55-stelliger Zahlen.
- V5 [A] prog/01/03 — die Interpreterschleife arbeitet Bytecode-Karten ab (Marke wandert, Dreischritt holen–erkennen–ausführen) — Kernbild des ganzen Heftes (zwei Phasen), bisher nur ein statisches Kästchenbild und ein zugeklappter Hintergrundkasten.

## Editor-Lücken

Gezählt über die Vorschläge V1–V54 (neue Abbildungen); die meisten sind ohne neue Funktion machbar (Kästen, FadeIn, Shift, Create, Write, Table, LabeledArrow, Brace).
- L8: 5 (V2, V5, V37, V39, V52; Code-Objekt mit Zeilen-Hervorhebung und Variablenzustand; Behelf angegeben, funktioniert, ist aber aufwendig)
- L3: 3 (V15, V30, V42; Parameter über die Zeit, z. B. laufender Zähler oder Wert, der gegen 0 wandert; Behelf: mehrere Zustände nacheinander)
- L1: 2 (V10, V17; Verschwinden; Behelf: Kreuz bzw. Abdunkeln)
- L2: 1 (V6; Formel Schritt für Schritt umformen, Behelf: Zeilen untereinander) und bei der vorhandenen Szene k2rfloat
- L9: 1 (V29; Tabellenzeilen einzeln betonen)
- L-neu: Pfeilende animieren, 1 Vorschlag (V38) und die vorhandene Szene prog/k2etikett: Ein Pfeil Name → Objekt soll bei einer Zuweisung auf ein anderes Objekt umspringen („Zuweisung biegt den Pfeil um“). Behelf Rotate um den Etikett-Anker ist nur bei gleichem Abstand der Kästen exakt. Dieses Verhalten ist der Kern von Python-Variablen; eine eigene Animationsart „Pfeilende bewegen“ lohnt sich.
- L4, L5, L6, L7: 0. L10 (Abspielknopf im Artikel) betrifft alle Abbildungen.

## Auffälligkeiten

- Die vorhandenen 16 Abbildungen sind durchweg Endzustände; Verfahren (Heron, Interpreterschleife, Division durch 2, Verdopplungsverfahren, Zuweisung) haben keine Bewegung. Die Heron-Szene k1heron und die Zuweisungs-Szene k2etikett sind die besten Kandidaten zum Animieren.
- Rechenbilder: k2rbyte ist eine echte Σ-Operation. k2rbinaer und k2rnull sind statische MathTex-Formeln, obwohl es Σ-Rechnungen mit Zahlen im Kern eines Beispiels sind (RICHTLINIEN: Rechenbild-Pflicht): Vorschlag V28 und V30. k2rfloat ist eine mehrzeilige Formelkette ohne Σ/∏/Skalarprodukt und daher nicht pflichtig.
- Ausgewogen verteilt: Programmläufe (V1, V11, V13, V16, V37, V39, V52), Bitmuster (V28 bis V32), Rundung (V31 bis V36).
- Doppelungen vermieden: Rangfolge in prog/01 (V12) und prog/02 (V27) sind abgegrenzt; Raster-Szene prog/k2raster dient V34, V41 (Bausteine) und V46 (Wiederverwendung); Zeigermultiplikation verweist auf hm1/k7dreh (V48).
- Die Erwähnung von `NameError` in prog/01 (V19) bereitet das Namens-Bild von prog/02 (V37, V44) vor; kein Vorgriff, die Namen werden in prog/01 nur als „Wort ohne Anführungszeichen“ gezeigt.

## Vorschläge (V1 bis V54, nach Artikel geordnet)

### Heft prog/01 — Programme und der Python-Interpreter

#### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Taschenrechner gegen Programm (Zusammenschau)
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/01-programme-und-der-python-interpreter.md
- **Stelle:** Worum es geht — „Ein Taschenrechner rechnet genau das, was man gerade eintippt. Will man dieselbe Rechnung für zwanzig Preise …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Taschenrechner-Kasten (TextBox „Taschenrechner“) mit Tippfeld und darunter eine Liste von Preiskarten (TextBox je Zahl, Beispielpreise 4,50 / 12,00 / 7,90 …, „…“ bis Nr. 20). Rechts ein Kasten „Programm“ mit einer einzigen Zeile Anweisung (z. B. „Preis mal 1,19“, Beispielwert) und ein Ausgabestapel. Überschriften „einmal pro Preis tippen“ und „einmal aufschreiben“.
- **Ablauf:** 1. Links: Hand-Symbol tippt Preis 1, Ergebnis erscheint; dasselbe für Preis 2, 3 (Karten erscheinen nacheinander mit Write). 2. Bei Preis 7 erscheint ein rotes Kreuz („Tippfehler“), die Ergebniskarte ist falsch. 3. Rechts: die Anweisungszeile wird einmal geschrieben (Write). 4. Alle 20 Preiskarten (hier 6 stellvertretend + „…“) fahren gleichzeitig per Shift durch den Programm-Kasten und kommen rechts als Ergebnisse heraus; kein Kreuz. 5. Unterzeile: „so oft man will, ohne neue Tippfehler“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Der Leser sieht nicht, warum eine aufgeschriebene Anweisungsliste mehr ist als ein Taschenrechner (Wiederholbarkeit, Fehlerfreiheit nach einmal Prüfen).
- **Szenenname:** prog/k1programm
- **Editor-Lücke:** machbar (FadeIn, Write, Shift; Paketdurchlauf mit Shift auf mehrere Karten gleichzeitig)

#### Artikel 02 — Programme und Programmiersprachen (Soll 4, vorh. 1)

### V2 [A] Der Prozessor führt Maschinenbefehle aus (Heron, ein Durchgang)
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/02-programme-und-programmiersprachen.md
- **Stelle:** Was der Prozessor versteht: Maschinenbefehle — Beispiel „Schritt 2 des Heron-Rezepts zerfällt in Maschinenbefehle etwa so …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Speicher als Tabelle (Table, Spalten Adresse/Inhalt): Zelle 12 enthält $g=1$; darüber die fünf Befehle des Beispiels als Liste mit erfundenen Beispielzahlen daneben (Vermerk „Zahlen nur zur Illustration; jede Prozessorfamilie hat eigene“): 1 „hole Zahl aus Platz 12“, 2 „teile 2 durch diese Zahl“, 3 „addiere g“, 4 „teile durch 2“, 5 „lege ab in Platz 12“. Rechts der Kasten „Prozessor“ mit Unterkasten „Rechenwerk“ und einem Anzeigefeld für die aktuelle Zahl.
- **Ablauf:** 1. Befehlsmarke (Rechteck) steht auf Befehl 1; Pfeil von Platz 12 zum Rechenwerk, Anzeige 1. 2. Marke per Shift auf Befehl 2: Anzeige $2/1=2$. 3. Befehl 3: $2+1=3$ (g wird wieder aus dem Speicher geholt, Pfeil). 4. Befehl 4: $3/2=1{,}5$. 5. Befehl 5: Pfeil vom Rechenwerk zu Platz 12, Inhalt wechselt von 1 auf 1,5 (altes g wird überschrieben). 6. Kurz: „nächster Durchgang beginnt wieder bei Befehl 1“. — Haltepunkte: 3, 5.
- **Verständnisproblem:** „Maschinenbefehl“ und „Prozessor führt aus“ bleiben abstrakt; der Leser sieht nicht, dass ein Rechenschritt aus Speicherzugriffen und winzigen Rechnungen besteht und das Ergebnis im Speicher überschrieben wird.
- **Szenenname:** prog/k1maschine
- **Editor-Lücke:** machbar (Table, Shift der Marke, LabeledArrow); L8 (Code mit Zeilen-Hervorhebung) wäre hilfreich, Behelf: Textzeilen + wanderndes Rechteck

### V3 [A] Syntax prüft die Form, Semantik legt die Wirkung fest
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/02-programme-und-programmiersprachen.md
- **Stelle:** Die Syntax — „Bei einer Programmiersprache muss man zwei Fragen trennen: Ist ein Text überhaupt erlaubt? Und was bewirkt er?“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Stationen von links nach rechts: Station 1 „Form erlaubt? (Syntax)“, Station 2 „Was bewirkt der Text? (Semantik)“. Links vier Textkarten (Monospace): `(1 + 2 / 1) / 2`, `(1 + 2 / 1 / 2`, `1 + / 2`, `7 / 2`. Rechts hinter Station 2 zwei Ergebnisfelder „Python: 3,5“ und „C: 3“.
- **Ablauf:** 1. Karte `(1 + 2 / 1) / 2` fährt in Station 1, grüner Haken (Mark), fährt weiter zu Station 2, dort erscheint „teile 2 durch 1, addiere 1, teile durch 2 = 1,5“. 2. Karte `(1 + 2 / 1 / 2`: die öffnende Klammer wird mit LabeledArrow markiert („nie geschlossen“), rotes Kreuz, Karte bleibt vor Station 1 liegen. 3. Karte `1 + / 2`: Lücke zwischen `+` und `/` markiert („hier fehlt eine Zahl“), Kreuz. 4. Karte `7 / 2`: Haken in Station 1, in Station 2 teilt sich der Weg: oben „Python: teile 7 durch 2 = 3,5“, unten „C (ganze Zahlen): Rest weglassen = 3“. Schlussbeschriftung: „gleiche Form, verschiedene Bedeutung“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Syntax und Semantik werden als Wörter gelernt, aber nicht als zwei getrennte Prüfungen erlebt.
- **Szenenname:** prog/k1syntaxsemantik
- **Editor-Lücke:** machbar (TextBox, Mark, LabeledArrow, Shift)

### V4 [B] Alltagssprache mehrdeutig, Programmiersprache eindeutig
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/02-programme-und-programmiersprachen.md
- **Stelle:** Die Programmiersprache — „Maschinencode ist eine lange Folge von Zahlen. Menschen können ihn kaum lesen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei Zeilen untereinander wie Stufen: „Alltagssprache“ mit dem Satz „Ich sah den Mann mit dem Fernglas.“, „Programmiersprache“ mit `(1 + 2 / 1) / 2`, „Maschinencode“ mit einer Reihe erfundener Zahlen (Vermerk „nur zur Illustration“). Rechts je eine Spalte „Bedeutungen“.
- **Ablauf:** 1. Satz erscheint, von zwei LabeledArrows nacheinander gedeutet: Pfeil 1 vom „Fernglas“ zum Mann („der Mann hat es“), dann Pfeil 2 zum „Ich“ („ich habe es“); Beschriftung „2 Bedeutungen — Rechner kann nicht raten“. 2. Die Python-Zeile erscheint, nur ein Pfeil zur Bedeutung „teile 2 durch 1, addiere 1, teile durch 2“; Beschriftung „genau 1 Bedeutung“. 3. Maschinencode erscheint als Zahlenfolge mit Vermerk „nur eine Prozessorfamilie, für Menschen kaum lesbar“. — Haltepunkt: 1.
- **Verständnisproblem:** Warum man überhaupt eine künstliche Sprache braucht, statt Alltagssprache oder direkt Zahlen.
- **Szenenname:** prog/k1sprache
- **Editor-Lücke:** machbar

#### Artikel 03 — Vom Quelltext zur Ausführung (Soll 3, vorh. 1)

### V5 [A] Die Interpreterschleife arbeitet den Bytecode ab
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/03-vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.md
- **Stelle:** Der Bytecode — „Den Bytecode arbeitet anschließend ein Teil von CPython Befehl für Befehl ab: die Interpreterschleife.“ (nach Abbildung 2)
- **Art:** neue Animation
- **Was zu sehen ist:** Quelltext `print("Hallo")` links; Mitte eine Stapelliste „Bytecode“ mit drei vereinfachten Befehlskarten (Vermerk „vereinfacht; echte Namen hängen von der Version ab“): „lege `print` bereit“, „lege `"Hallo"` bereit“, „rufe auf“; rechts ein Kasten „Interpreterschleife“ mit Unterfeldern „nächsten Befehl holen“, „welcher Befehl?“, „passendes Stück Maschinencode ausführen“ und einem Rückpfeil (LoopArrow); darunter ein Terminal-Kasten.
- **Ablauf:** 1. Phase „Übersetzen“: Quelltext fährt in den Übersetzer, die drei Befehlskarten erscheinen nacheinander; Beschriftung „noch nichts ausgeführt“. 2. Phase „Ausführen“: Marke (Rechteck) auf Karte 1, durchläuft die drei Felder der Schleife, Schleifenpfeil zurück. 3. Dasselbe für Karte 2. 4. Karte 3: Terminal zeigt `Hallo`. 5. Schleife endet (keine Karte mehr). — Haltepunkte: 2, 4.
- **Verständnisproblem:** „Interpreterschleife“ und „Bytecode Befehl für Befehl“ sind Wörter; der Leser sieht nicht, dass die Schleife immer denselben Dreischritt wiederholt und jeder Bytecode-Befehl auf ein Stück Maschinencode von CPython abgebildet wird.
- **Szenenname:** prog/k1schleife
- **Editor-Lücke:** machbar; L8 hilfreich (Behelf: Karten als TextBoxen, Marke per Shift)

### V6 [B] Der Übersetzer rechnet feste Ausdrücke vorab aus
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/03-vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.md
- **Stelle:** Der Bytecode — Beispiel „Aus der Zeile `(1 + 2 / 1) / 2` entstehen Bytecode-Befehle der Art ‚lege die Zahl 1 bereit‘ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Spalten „Phase 1: Übersetzen“ und „Phase 2: Ausführen“. In Phase 1 der Ausdruck `(1 + 2 / 1) / 2` in Zeile 1; darunter Zeilen für die Zwischenschritte; rechts der erzeugte Bytecode „lege 1,5 bereit“.
- **Ablauf:** 1. Ausdruck erscheint, Brace unter `2 / 1`. 2. Zeile 2 (Write): `(1 + 2.0) / 2`. 3. Zeile 3: `3.0 / 2`. 4. Zeile 4: `1.5`. 5. Bytecode-Karte „lege 1,5 bereit“ erscheint; in Phase 2 steht daneben nur „nichts mehr zu rechnen“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Dass der Übersetzer schon rechnet und im Bytecode eine fertige Zahl steht; später (Skript ohne Anzeige, Aufgabe zum Bytecode) wird das vorausgesetzt.
- **Szenenname:** prog/k1vorabrechnen
- **Editor-Lücke:** machbar (zeilenweiser Aufbau); L2 (Formel-Umformen) wäre die saubere Fassung

#### Artikel 04 — Python einrichten (Soll 4, vorh. 0)

### V7 [A] Terminal: Eingabeaufforderung, Befehl, Antwort
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/04-python-einrichten.md
- **Stelle:** Was du dafür brauchst: ein Terminal öffnen — „Python startet man meist mit einem Befehl, den man in ein Terminal tippt.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Terminalfenster (Rectangle, dunkel, Titelleiste „Terminal“). Letzte Zeile `PS C:\Users\student>` mit Cursor. Drei LabeledArrows beschriften später den Aufbau: Eingabeaufforderung, Befehl, Antwort. Daneben die Linux-Variante `student@labor:~$` mit Beschriftung „Benutzername @ Rechnername : Ordner“ und das Kürzel `PS>`/`$` aus dem Kapitel.
- **Ablauf:** 1. Fenster erscheint leer mit Eingabeaufforderung, Cursor blinkt. 2. `echo Hallo` wird getippt (Write). 3. Enter: Zeile bleibt stehen, darunter erscheint `Hallo` (Antwort), darunter neue Eingabeaufforderung. 4. Pfeile benennen: „Eingabeaufforderung (wartet auf Befehl)“, „Befehl“, „Antwort“. 5. Linux-Fenster: Brace zerlegt `student@labor:~$` in Benutzername, Rechnername, `~` = persönlicher Ordner. 6. Zusammenfassung zur Kurzform: `PS>` und `$`. — Haltepunkte: 3, 5.
- **Verständnisproblem:** „Terminal“ und „Eingabeaufforderung“ sind für Anfänger neu; ohne Bild bleibt unklar, was Eingabe und was Antwort ist (alle späteren Kästen im Kapitel setzen das voraus).
- **Szenenname:** prog/k1terminal
- **Editor-Lücke:** machbar (Rectangle, Text, Write, FadeIn)

### V8 [A] Versionsnummern teilweise vergleichen
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/04-python-einrichten.md
- **Stelle:** Die Versionsnummer — „Versionsnummern vergleicht man Teil für Teil von links, nicht als Dezimalzahl …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben `3.14.4` in drei Kästen (TextBox) mit Brace-Beschriftungen „Hauptversion 3“, „Unterversion 14 (neue Sprachmittel, jeden Oktober)“, „Fehlerbehebung 4“. Darunter drei Versionspaare in Zeilen, jeweils mit drei Spalten: `3.9.18` gegen `3.14.4`, `3.14.4` gegen `3.14.10`, `3.13.9` gegen `3.12.0`.
- **Ablauf:** 1. `3.14.4` zerfällt in die drei Kästen. 2. Paar 1: Spalte 1 gleich (grün), Spalte 2: 9 < 14 → „älter“, Rest wird grau („entschieden“). 3. Paar 2: Spalte 1, 2 gleich, Spalte 3: 4 < 10. 4. Paar 3: Spalte 2: 13 > 12. 5. Falle: Dezimal gelesen „3,9 > 3,14?“ erscheint rot durchgestrichen mit Kreuz. — Haltepunkte: 2, 5.
- **Verständnisproblem:** Wer Versionsnummern wie Dezimalzahlen liest, hält 3.9 für neuer als 3.14.
- **Szenenname:** prog/k1version
- **Editor-Lücke:** machbar

### V9 [B] `py` wählt unter den installierten Versionen
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/04-python-einrichten.md
- **Stelle:** Python unter Windows: der Python install manager — „Danach startet `py` die Standardversion; das ist die neueste installierte …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links drei Befehlskarten (`py`, `python`, `py -V:3.13`), in der Mitte ein Kasten „Python install manager“, rechts drei Versionskästen 3.12, 3.13, 3.14 (der Rahmen von 3.14 hervorgehoben als „Standard = neueste installierte“). Darunter `py install 3.14` und `py list`.
- **Ablauf:** 1. Anfangs nur 3.12 und 3.13 installiert, Standard 3.13. 2. `py install 3.14`: Kasten 3.14 wächst (GrowFromCenter), der Standardrahmen wandert auf 3.14. 3. `py` und `python` zeigen mit Pfeilen auf 3.14. 4. `py -V:3.13` zeigt auf 3.13. 5. `py list` bündelt alle Kästen mit der Markierung „Standard“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Die Rolle des install managers (ein Starter für mehrere Versionen) und was „Standardversion“ bedeutet.
- **Szenenname:** prog/k1installmanager
- **Editor-Lücke:** machbar

### V10 [C] Linux: `python` fehlt, `python3` ist das System-Python
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/04-python-einrichten.md
- **Stelle:** Python unter Linux — Warnung „Das Python des Systems nicht entfernen oder ersetzen“
- **Art:** neue Animation
- **Was zu sehen ist:** Links zwei Befehle `python3` (grüner Pfeil zu „Python 3.14.4“) und `python` (roter Pfeil ins Leere, Meldung „Command 'python' not found“). Rechts oben Kasten „python3“ mit mehreren darauf zeigenden Systemteilen (Kästen „Befehlshilfe“, „weitere Pakete …“).
- **Ablauf:** 1. `python3` findet Python. 2. `python` findet nichts, Hinweis „did you mean python3“. 3. Paket `python-is-python3` kommt hinzu: gestrichelter Pfeil `python` → `python3`. 4. Warnung: `python3` wird entfernt, die davon abhängigen Kästen erhalten rote Kreuze nacheinander („über hundert weitere Pakete würden mit entfernt“). — Haltepunkt: 4.
- **Verständnisproblem:** Warum man das System-Python nicht anrühren soll (das System hängt daran).
- **Szenenname:** prog/k1linuxpython
- **Editor-Lücke:** machbar (ohne Verschwinden L1; Kreuze statt Entfernen)

#### Artikel 05 — Der interaktive Modus (Soll 5, vorh. 0)

### V11 [A] Der Kreislauf Lesen – Auswerten – Anzeigen
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/05-der-interaktive-modus.md
- **Stelle:** Der interaktive Modus — „Am Taschenrechner tippt man eine Rechnung, drückt ‚=‘ und liest das Ergebnis ab …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Terminal-Kasten mit `>>>`; rechts drei Kästen im Kreis: „Lesen (read)“, „Auswerten (eval)“, „Anzeigen (print)“ mit Pfeilen (LoopArrow schließt den Kreis).
- **Ablauf:** 1. `2 + 3` wird hinter `>>>` getippt. 2. Der Text wandert in „Lesen“, dann „Auswerten“ (Wert 5 entsteht), dann „Anzeigen“; im Terminal erscheint `5` und eine neue `>>>`-Zeile. 3. Zweite Runde mit `7 * 6` → `42`. 4. Dritte Runde: `(2 + 3` wird getippt, Auswerten bleibt aus, Terminal zeigt `...`, der Kreis bleibt in „Lesen“ stehen („Python wartet auf den Rest“). — Haltepunkte: 2, 4.
- **Verständnisproblem:** Dass „interaktiv“ ein Kreislauf ist und dass `...` heißt „Eingabe noch unvollständig“, nicht „Fehler“.
- **Szenenname:** prog/k1repl
- **Editor-Lücke:** machbar

### V12 [A] Auswertungsreihenfolge Schritt für Schritt
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/05-der-interaktive-modus.md
- **Stelle:** Rechnen wie mit dem Taschenrechner — „Python rechnet wie in der Mathematik: Potenzen vor Punktrechnung, Punktrechnung vor Strichrechnung.“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Legende „Rang: 1 Klammern, 2 `**`, 3 `* /`, 4 `+ -`“ und drei Rechenzeilen: `100 + 220 * 2`, `(100 + 220) * 2`, `1000 * 1.02 ** 10`.
- **Ablauf:** 1. Zeile 1: Brace unter `220 * 2`, darunter 440 (FadeIn), Brace über das Ganze, 540. 2. Zeile 2: Klammer wird farbig, 100 + 220 = 320 wächst heraus, dann · 2 = 640. 3. Zeile 3: Brace unter `1.02 ** 10` = 1,2189944…, dann mal 1000 = 1218,99…; Beschriftung „Potenz zuerst“. 4. Zusatz: Klammern sind nur die runden; `[ ]` und `{ }` ausgegraut mit „andere Bedeutung“. — Haltepunkte: 1, 2.
- **Verständnisproblem:** Der Leser weiß nicht, in welcher Reihenfolge Python einen Ausdruck zerlegt; die Folgen (Klammerfehler, Logikfehler in Abschnitt 6) hängen daran.
- **Szenenname:** prog/k1reihenfolge
- **Editor-Lücke:** machbar (Brace, FadeIn); L7/Arithmetik-Operation nicht nötig

### V13 [A] Der Funktionsaufruf `print`: erst auswerten, dann ausgeben
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/05-der-interaktive-modus.md
- **Stelle:** Der Funktionsaufruf: `print` — „Die Funktion `print` schreibt die Werte in ihren Klammern in eine Zeile, getrennt durch je ein Leerzeichen.“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Zeile `print("Preis pro kg in Euro:", 4.49 / 0.45)`; mit Braces markiert: Funktionsname `print`, runde Klammern, zwei Werte (durch Komma getrennt). Rechts ein Kasten „Funktion print (fertiges Teilprogramm)“, darunter ein Terminal-Kasten.
- **Ablauf:** 1. Die Zeile erscheint, Braces benennen Name, Klammern, die zwei Werte. 2. Der zweite Wert `4.49 / 0.45` wird zu `9.977777777777778` ausgewertet (Wert ersetzt den Ausdruck). 3. Beide Werte fahren in den `print`-Kasten. 4. Das Terminal schreibt `Preis pro kg in Euro: 9.977777777777778`, das Trenn-Leerzeichen wird hervorgehoben, die Anführungszeichen sind weg. 5. Kontrast darunter: `"Hallo"` im interaktiven Modus zeigt den Wert `'Hallo'`, `print("Hallo")` schreibt `Hallo` und liefert nichts zum Anzeigen. — Haltepunkte: 2, 5.
- **Verständnisproblem:** „Funktion“ und „Aufruf“ sind neu; unklar bleibt die Reihenfolge (Argument zuerst ausrechnen) und der Unterschied zwischen Anzeigen eines Wertes und Ausgeben durch `print`.
- **Szenenname:** prog/k1print
- **Editor-Lücke:** machbar

### V14 [B] Zeichenkette gegen Ausdruck: `7 * 6` und `"7 * 6"`
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/05-der-interaktive-modus.md
- **Stelle:** Text als Wert: die Zeichenkette — „Der interaktive Modus zeigt eine Zeichenkette mit Apostrophen an …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Auswertungsmaschine (TextBox „Auswerten“) in der Mitte. Oben ein Eingabeband mit der Eingabe `7 * 6`, darunter dieselbe Eingabe mit Anführungszeichen, `"7 * 6"`, zerlegt in fünf Zeichenkästchen (`7`, Leerzeichen, `*`, Leerzeichen, `6`).
- **Ablauf:** 1. `7 * 6` läuft durch die Maschine, Ergebnis `42` (ohne Apostrophe). 2. `"7 * 6"`: die Anführungszeichen schließen sich um die fünf Kästchen wie eine Schale; die Maschine lässt die Schale unverändert durch (Pfeil geht daran vorbei). 3. Anzeige `'7 * 6'` mit Apostrophen. 4. Letzte Zeile: `42` (Zahl) und `'42'` (zwei Zeichen `4`, `2`) nebeneinander. — Haltepunkt: 2.
- **Verständnisproblem:** Zahl und Text sehen auf dem Bildschirm ähnlich aus; was in Anführungszeichen steht, wird nicht gerechnet.
- **Szenenname:** prog/k1zeichenkette
- **Editor-Lücke:** machbar

### V15 [B] Das Heron-Rezept mit `_`, Durchgang für Durchgang
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/05-der-interaktive-modus.md
- **Stelle:** Das Rezept im interaktiven Modus: erst von Hand, dann fertig — „Von Hand. Der erste Durchgang mit $g=1$ ist `(1 + 2/1) / 2` …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Terminal-Kasten mit den Zeilen aus dem Artikel; rechts ein Fach (Rectangle) mit der Beschriftung `_` (zuletzt angezeigter Wert). Unten ein Vergleichsbalken: Heron-Ergebnis gegen `2 ** 0.5`.
- **Ablauf:** 1. `(1 + 2/1) / 2` → `1.5`, das Fach `_` füllt sich mit 1.5. 2. Die Zeile `(_ + 2/_) / 2` erscheint, zwei Pfeile aus beiden `_` ins Fach, Ergebnis `1.4166666666666665` überschreibt das Fach. 3. Dasselbe für `1.4142156862745097`, `1.4142135623746899`, `1.414213562373095`. 4. Der sechste Durchgang liefert wieder `1.414213562373095`: Fach unverändert, „Ziel erreicht“. 5. Daneben `2 ** 0.5` = `1.4142135623730951`; die letzte Ziffer farbig markiert (… 095 gegen … 0951). — Haltepunkte: 2, 4.
- **Verständnisproblem:** Wie `_` ein Ergebnis an die nächste Zeile weiterreicht (Vorbereitung auf Variablen) und warum die Folge irgendwann stehen bleibt.
- **Szenenname:** prog/k1heronrepl
- **Editor-Lücke:** machbar; ein Zähler/Parameter über die Zeit wäre L3

#### Artikel 06 — Skripte schreiben und ausführen (Soll 3, vorh. 1)

### V16 [A] Vom Editor über die Datei zur Ausgabe
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/06-skripte-schreiben-und-ausfuhren.md
- **Stelle:** Das Skript — „Mit einem Editor kann man den Quelltext eines Programms in eine Datei schreiben und so oft ausführen, wie man will.“
- **Art:** neue Animation
- **Was zu sehen ist:** Von links nach rechts vier Kästen: „Editor“ (Fenster mit den drei Zeilen von `hallo.py`), „Ordner `python-kurs`“ (mit Dateisymbol), „Terminal“ (`cd python-kurs`, `py hallo.py`), „Python“ (Übersetzen, Ausführen). Unter dem Terminal die Ausgabe.
- **Ablauf:** 1. Die drei Zeilen werden im Editor geschrieben (Write). 2. „Speichern“: die Datei `hallo.py` fliegt in den Ordner. 3. Im Terminal `cd python-kurs` (Prompt wechselt in den Ordner), dann `py hallo.py`. 4. Die Datei wandert in „Python“: erst Phase „übersetzen“, dann „Zeile 1, 2, 3 nacheinander“. 5. Terminal füllt sich: `Hallo, Welt!`, `5`, `2 + 3`. 6. Zum Schluss steht wieder die Eingabeaufforderung da. 7. Hinweis auf die Falle: Dateiname `hallo.py.txt` mit Kreuz, wenn der Explorer Endungen ausblendet. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Der Ablauf Datei schreiben → speichern → starten → Ausgabe ist für Anfänger ein ungeübter Mehrschritt-Prozess.
- **Szenenname:** prog/k1skriptablauf
- **Editor-Lücke:** machbar

### V17 [B] Ein Kommentar fällt beim Zerlegen weg
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/06-skripte-schreiben-und-ausfuhren.md
- **Stelle:** Der Kommentar — „Ein Kommentar beginnt mit dem Zeichen `#` und reicht bis zum Ende der Zeile. Python überliest ihn vollständig.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Zeilen aus `rezept.py` in Monospace: `# Pizzateig fuer 6 statt fuer 4 Personen` und `print("Mehl in g:", 500 / 4 * 6)   # Menge pro Person mal 6`. Rechts ein Kasten „was Python ausführt“.
- **Ablauf:** 1. Ein Leserahmen (Rechteck) fährt über Zeile 2 von links; bei `#` färbt sich der Rest der Zeile grau. 2. Der graue Teil fällt weg (abgeblendet, kein Verschwinden nötig), der Code-Teil fährt in den Kasten rechts. 3. Zeile 1 komplett grau, rechts bleibt nichts. 4. Zusatz: `print("Nr. # 5")` — das `#` liegt in einer Zeichenkette (Anführungszeichen markiert), Leserahmen färbt nichts grau, Ausgabe `Nr. # 5`. — Haltepunkt: 1.
- **Verständnisproblem:** Wo genau ein Kommentar beginnt und dass `#` in einer Zeichenkette keiner ist.
- **Szenenname:** prog/k1kommentar
- **Editor-Lücke:** machbar (L1 für echtes Verschwinden, Behelf Abdunkeln)

#### Artikel 07 — Fehler lesen und verstehen (Soll 5, vorh. 2)

### V18 [A] Logikfehler: Plausibilitätsprüfung am Zahlenstrahl
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/07-fehler-lesen-und-verstehen.md
- **Stelle:** Der Logikfehler — Beispiel „Wer eine Strecke hin mit 60 km/h und zurück mit 40 km/h fährt, ist im Schnitt nicht 50 km/h schnell …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben ein Hin-/Rückweg (zwei LabeledArrows mit 60 km/h und 40 km/h, je 120 km). Mitte zwei Rechenzeilen: `2 * 60 * 40 / 60 + 40` und `2 * 60 * 40 / (60 + 40)`. Unten ein Zahlenstrahl von 0 bis 130 km/h mit hervorgehobenem Band 40 bis 60 („möglicher Durchschnitt“).
- **Ablauf:** 1. Pfeile für Hin- und Rückweg. 2. Zeile 1: Braces zeigen Pythons Reihenfolge ($2\cdot60\cdot40=4800$, geteilt durch 60 = 80, plus 40 = 120). 3. Der Wert 120 erscheint auf dem Zahlenstrahl weit rechts außerhalb des Bandes, rotes Kreuz („kann nicht stimmen“). 4. Zeile 2 mit Klammern: $4800/100=48$, Marke 48 liegt im Band, Haken. 5. Zusatzprobe: 50 hin, 50 zurück: falsche Formel 150, richtige 50. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Python meldet den Logikfehler nicht; der Leser sieht an der Zahlengeraden, wie man ihn selbst bemerkt.
- **Szenenname:** prog/k1logikfehler
- **Editor-Lücke:** machbar

### V19 [B] NameError: Ohne Anführungszeichen sucht Python einen Namen
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/07-fehler-lesen-und-verstehen.md
- **Stelle:** Die Ausnahme — Beispiel `NameError`: „Ohne Anführungszeichen hält Python ein Wort für einen Namen, wie es `print` einer ist …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links zwei Zeilen `print("Hallo")` und `print(Hallo)`. Rechts ein Regal „Namen, die Python kennt“ mit Fächern `print`, `exit`, … und einem Suchzeiger.
- **Ablauf:** 1. `print("Hallo")`: das Wort liegt in Anführungszeichen, wird zur Zeichenkette (Schale), geht an `print`. 2. `print(Hallo)`: das Wort ohne Anführungszeichen wird zum Suchbegriff, der Zeiger geht die Fächer durch (Shift). 3. Kein Fach passt: Blitz, Meldung `NameError: name 'Hallo' is not defined`; Programm bricht ab. — Haltepunkt: 3.
- **Verständnisproblem:** Warum fehlende Anführungszeichen keinen Syntaxfehler, sondern einen Laufzeitfehler auslösen.
- **Szenenname:** prog/k1namefehler
- **Editor-Lücke:** machbar

### V20 [C] Die Syntaxfehler-Meldung in ihren vier Zeilen
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/07-fehler-lesen-und-verstehen.md
- **Stelle:** Der Syntaxfehler — „Die Meldung besteht aus vier Zeilen: Datei und Zeilennummer, die betroffene Zeile …“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Meldung von `syntaxfehler.py` (Linux-Fassung) als Textblock; vier LabeledArrows.
- **Ablauf:** 1. Der Block erscheint. 2. Pfeil 1 auf die `File …, line 3`-Zeile: „Datei und Zeilennummer“. 3. Pfeil 2 auf `print("Zeile 3"`: „betroffene Zeile“. 4. Pfeil 3 auf `^`: „hier macht Python den Fehler fest“. 5. Pfeil 4 auf `SyntaxError: '(' was never closed`: „Art und Beschreibung“. Darunter das Ergebnis des Terminals: kein „Zeile 1“. Vorschlag: Szene im Stil von prog/k1traceback bauen (gleiche Pfeile), dann weglassbar, wenn k1traceback zu zwei Tabs zusammengelegt wird.
- **Verständnisproblem:** Wie man die Meldung liest, bevor der Traceback eingeführt ist.
- **Szenenname:** prog/k1syntaxmeldung
- **Editor-Lücke:** machbar

#### Artikel 08 — Das Wichtigste bis hier (Soll 1, vorh. 0)

### V21 [A] Zwei Phasen erklären das ganze Kapitel (Zusammenschau)
- **Artikel:** content/prog/01-programme-und-der-python-interpreter/08-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt daraus, dass CPython in zwei Phasen arbeitet …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Zeitpfeil mit zwei Abschnitten „Phase 1: ganze Datei übersetzen“ und „Phase 2: Bytecode ausführen“. Darunter acht kleine Karten aus der Tabelle (kurz): Konstanten vorab ausgerechnet; Kommentar fällt weg; Skript ohne „Wert anzeigen“; Syntaxfehler; `5 / 0` bleibt stehen; Laufzeitfehler; Wert gezeigt/verworfen; Logikfehler.
- **Ablauf:** 1. Zeitpfeil mit den beiden Abschnitten wächst (Create). 2. Karten fliegen nacheinander an ihre Stelle: vier in Phase 1, zwei in Phase 2. 3. Letzte Karte „Logikfehler“ landet hinter dem Zeitpfeil mit Beschriftung „nie: die Absicht des Verfassers wird nicht geprüft“. 4. Unterzeile: „Form vor dem Start, Ausführbarkeit beim Ausführen, Absicht nie“. — Haltepunkt: 2.
- **Verständnisproblem:** Der Kern-Artikel ist eine reine Textliste; die integrierende Einsicht (alles folgt aus zwei Phasen) ist nicht anschaulich.
- **Szenenname:** prog/k1phasen
- **Editor-Lücke:** machbar

### Heft prog/02 — Werte, Typen und Variablen

#### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V22 [A] Zwei Beobachtungen aus Python 1 und die drei Fragen des Kapitels
- **Artikel:** content/prog/02-werte-typen-und-variablen/01-werte-typen-und-variablen.md
- **Stelle:** Worum es geht — „Python 1 hat gezeigt, wie man Python rechnen lässt. Dabei blieben Beobachtungen unerklärt: `12 / 4` ergibt `3.0` und nicht `3` …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Terminal-Kasten mit `>>> 12 / 4` und `3.0` sowie `>>> 2 ** 0.5` / Heron-Ergebnis `1.414213562373095` gegen `1.4142135623730951`. Rechts drei Kästen als Fahrplan: „Welche Arten von Werten?“, „Wie speichert der Rechner sie?“, „Warum rechnet Python so?“.
- **Ablauf:** 1. Terminal: `12 / 4` wird getippt, `3.0` erscheint, rotes Fragezeichen an der Null. 2. Zwei Heron-Ergebnisse untereinander, die letzten Ziffern farbig, zweites Fragezeichen. 3. Die drei Fahrplan-Kästen erscheinen nacheinander; je ein Pfeil von den Fragezeichen: Frage 1 zu `3.0`, Fragen 2 und 3 zur letzten Ziffer. — Haltepunkt: 2.
- **Verständnisproblem:** Der Überblick benennt die Fragen nur in Worten; mit den zwei konkreten Beobachtungen sieht der Leser, worauf das Kapitel Antworten gibt.
- **Szenenname:** prog/k2fragen
- **Editor-Lücke:** machbar

#### Artikel 02 — Objekte und Typen (Soll 3, vorh. 1)

### V23 [A] Der Typ entscheidet, was `+` bedeutet
- **Artikel:** content/prog/02-werte-typen-und-variablen/02-objekte-und-typen.md
- **Stelle:** Der Typ — Beispiel „Was der Typ bewirkt, zeigt das Pluszeichen. Für zwei Objekte vom Typ `int` addiert es …“
- **Art:** neue Animation
- **Was zu sehen ist:** In der Mitte ein Kasten `+` mit zwei Eingängen und einem Ausgang; links drei Operandenpaare als beschriftete Kästen (Aufschrift `int`/`str`): (2, 3), („2“, „3“), („2“, 3); rechts darüber ein kleines Regelbuch mit Zeilen „int + int: addieren“, „str + str: verketten“ und einer leeren Zeile „str + int: —“.
- **Ablauf:** 1. Paar 1 fährt hinein, der Operator liest die zwei Aufschriften (Pfeile auf die Typen), die Regelzeile „int + int“ leuchtet auf (Indicate), aus dem Ausgang kommt ein `int`-Kasten mit 5. 2. Paar 2: Regelzeile „str + str“, Ausgang: `str`-Kasten `'23'` (die zwei Kästen schieben sich zusammen). 3. Paar 3: keine Zeile passt, Blitz, Meldung `TypeError: can only concatenate str (not "int") to str`. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Dass dasselbe Zeichen je nach Typ der Operanden etwas anderes tut und dass Python bei fehlender Regel nicht rät.
- **Szenenname:** prog/k2plus
- **Editor-Lücke:** machbar

### V24 [B] Eine Methode hängt am Typ
- **Artikel:** content/prog/02-werte-typen-und-variablen/02-objekte-und-typen.md
- **Stelle:** Die Methode — „Manche Funktionen hängen an einem Typ wie Knöpfe an einem Gerät …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Objektkästen: `str` mit „Ohm“, `float` mit 2.5; am `str`-Kasten ein Knopf `upper()`, am `float`-Kasten ein Knopf `as_integer_ratio()`.
- **Ablauf:** 1. Beide Kästen mit ihren Knöpfen erscheinen. 2. `"Ohm".upper()`: Pfeil vom Knopf auf den Kasten, Ergebnis `'OHM'` als neuer Kasten (der alte bleibt „Ohm“). 3. `(2.5).as_integer_ratio()`: Ergebnis `(5, 2)`, daneben $2{,}5=5/2$. 4. `(2.5).upper()`: Pfeil zum `float`-Kasten, dort gibt es keinen Knopf `upper`, Blitz, `AttributeError: 'float' object has no attribute 'upper'`. — Haltepunkt: 4.
- **Verständnisproblem:** „Methode“ als Funktion eines Typs und warum die Schreibweise `objekt.name()` nur zu Objekten des passenden Typs passt.
- **Szenenname:** prog/k2methode
- **Editor-Lücke:** machbar

#### Artikel 03 — Ganze Zahlen und Rechenoperatoren (Soll 5, vorh. 1)

### V25 [B] Ein `int` wächst mit der Zahl
- **Artikel:** content/prog/02-werte-typen-und-variablen/03-ganze-zahlen-und-rechenoperatoren.md
- **Stelle:** Der Typ `int` — „Auf Papier schreibt man eine ganze Zahl mit so vielen Ziffern, wie sie braucht.“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Zeile, in der ein Objektkasten (Aufschrift `int`) mit Ziffernkästchen gefüllt wird; darüber der jeweilige Ausdruck.
- **Ablauf:** 1. `2 ** 10` = 1024: Kasten mit 4 Ziffern. 2. `2 ** 100`: der Kasten dehnt sich (Scale), 31 Ziffern (1267650600228229401496703205376). 3. `10 ** 20 + 1 - 10 ** 20`: Der Kasten mit 21 Ziffern (1 und 20 Nullen) nimmt die +1 auf (letzte Ziffer 1), wird dann um 10^20 verkleinert; Ergebnis `1`. Beschriftung „nichts gerundet, nichts verloren“. — Haltepunkt: 3.
- **Verständnisproblem:** Dass ein `int` keine feste Größe hat und exakt bleibt (Gegenstück zum `float`, das später kommt).
- **Szenenname:** prog/k2intwaechst
- **Editor-Lücke:** machbar

### V26 [A] Operator, Operanden und Typ des Ergebnisses
- **Artikel:** content/prog/02-werte-typen-und-variablen/03-ganze-zahlen-und-rechenoperatoren.md
- **Stelle:** Operator und Operand — „Ein Rechenzeichen nimmt Werte entgegen und gibt einen neuen Wert heraus, wie eine kleine Maschine mit Eingängen und einem Ausgang.“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Maschine (TextBox) mit dem Operator, zwei Eingängen, einem Ausgang; Objektkästen mit Typaufschrift. Zeile darunter: einstelliges Minus.
- **Ablauf:** 1. `7 - 2`: zwei `int`-Kästen fahren in die Maschine, `5` (`int`) kommt heraus; Braces benennen Operator und Operanden. 2. `7 + 0.5`: der `int`-Kasten 7 wird auf dem Weg zu einem `float`-Kasten 7.0 (neuer Kasten, der alte bleibt), Ergebnis 7.5 (`float`). 3. `2 * 3.0` → 6.0. 4. `7 / 2` → 3.5 und `12 / 4` → 3.0: beide Operanden `int`, der Ausgang trägt trotzdem `float`. 5. `-7`: nur ein Eingang, aus 7 wird −7. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Die Regel für den Ergebnistyp (int/int → int, `/` → float, ein float im Spiel → float) und der Begriff Operand.
- **Szenenname:** prog/k2operator
- **Editor-Lücke:** machbar

### V27 [A] Rangfolge Schritt für Schritt, auch von rechts nach links
- **Artikel:** content/prog/02-werte-typen-und-variablen/03-ganze-zahlen-und-rechenoperatoren.md
- **Stelle:** Die Rangfolge — Beispiel „`2 + 3 * 4 ** 2 // 5` wertet Python so aus: zuerst die Potenz …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Rangtabelle (1 `**`, 2 einstelliges `+ -`, 3 `* / // %`, 4 zweistelliges `+ -`). Rechts der Ausdruck `2 + 3 * 4 ** 2 // 5` in Monospace mit Platz für Braces; darunter `2 ** 3 ** 2` und `-3 ** 2`.
- **Ablauf:** 1. Ausdruck: Brace ① unter `4 ** 2`, darüber 16. 2. Brace ② unter `3 * 16` → 48. 3. Brace ③ `48 // 5` → 9. 4. Brace ④ `2 + 9` → 11. 5. `12 / 3 / 2`: gleicher Rang, Pfeil von links nach rechts, (12/3)/2 = 2.0. 6. `2 ** 3 ** 2`: Pfeil von rechts nach links, zuerst 3 ** 2 = 9, dann 2 ** 9 = 512; die falsche Lesart (2 ** 3) ** 2 = 64 erscheint durchgestrichen. 7. `-3 ** 2`: Brace um `3 ** 2`, dann Minus: −9. — Haltepunkte: 1, 6.
- **Verständnisproblem:** Welcher Operator zuerst dran ist, und dass gleicher Rang nicht überall von links nach rechts läuft.
- **Szenenname:** prog/k2rangfolge
- **Editor-Lücke:** machbar (Doppelung mit prog/k1reihenfolge (V12) vermeiden: dort Grundrechenarten und `**` ohne Vorzeichen und Gleichrang, hier die vollständige Rangtabelle; im Editor können beide dieselben Bausteine nutzen)

#### Artikel 04 — Zahlen im Binärsystem (Soll 5, vorh. 3)

### V28 [A] Schalterreihe: Dezimalstellen und Binärstellen, Wert von $10011_2$ (ersetzt prog/k2rbinaer)
- **Artikel:** content/prog/02-werte-typen-und-variablen/04-zahlen-im-binarsystem.md
- **Stelle:** Die Binärzahl — „Man stelle sich eine Reihe von Schaltern vor. Der rechte zählt 1, der nächste 2, dann 4, 8, 16 …“
- **Art:** neue Animation (ersetzt die bestehende statische Formel-Abbildung prog/k2rbinaer, die ein einziger MathTex ist)
- **Was zu sehen ist:** Oben die Dezimalzahl 4705 mit vier Spalten (Stellenwerte 1000, 100, 10, 1). Darunter eine Reihe von fünf Schaltern (Kästen mit Wert 16, 8, 4, 2, 1 und Stellung 1 0 0 1 1), darunter das Rechenbild als Operation Σ (Summation, Term $b_i\,2^i$, $i=0$ bis 4) mit den Werten aus dem Artikel.
- **Ablauf:** 1. 4705: Ziffer mal Stellenwert, 4000 + 700 + 0 + 5. 2. Die Binärstellen erscheinen von rechts, jeder Stellenwert doppelt so groß wie sein rechter Nachbar (Pfeile ×2). 3. Die Schalter springen in die Stellung 1 0 0 1 1; die eingeschalteten Werte 16, 2, 1 heben sich ab. 4. Summationsoperation: $1\cdot16+0\cdot8+0\cdot4+1\cdot2+1\cdot1=19$, Term für Term. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Der Begriff Stellenwertsystem und warum jedes Bit „zählt $2^i$“; bisher steht nur die Formel (Rechenbild als Pflicht, siehe RICHTLINIEN: Σ mit Zahlen im Rechenbeispiel).
- **Szenenname:** prog/k2schalter
- **Editor-Lücke:** machbar (Summation ist Editor-Operation)

### V29 [A] Fortgesetzte Division durch 2: Der Rest ist das herausgeschobene Bit
- **Artikel:** content/prog/02-werte-typen-und-variablen/04-zahlen-im-binarsystem.md
- **Stelle:** Ins Binärsystem umrechnen: erst von Hand — „Teilt man eine ganze Zahl $n\ge0$ durch 2, ist der Rest das letzte Bit $b_0$ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Schalterreihe von 19 (1 0 0 1 1) und daneben die Tabelle $n$, $n\,/\!/\,2$, $n\,\%\,2$, Bit.
- **Ablauf:** 1. n = 19 als Reihe 10011. 2. Die ganze Reihe rückt um eine Stelle nach rechts (Shift), das herausfallende Bit (1) wandert in die Spalte „Rest“, die übrigen Bits sind der Quotient 9 (= 1001). 3. Dasselbe mit 9 → 4 Rest 1; 4 → 2 Rest 0; 2 → 1 Rest 0; 1 → 0 Rest 1. 4. Die Restspalte wird mit einem Pfeil von unten nach oben gelesen: 10011. Der letzte Schritt endet bei Quotient 0. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Warum die Reste die Bits sind und warum man von unten liest.
- **Szenenname:** prog/k2halbieren
- **Editor-Lücke:** L9 hilfreich (Tabellenzeilen einzeln betonen); Behelf: Rechtecke über den Zeilen

### V30 [A] Das Verdopplungsverfahren für 0,1 und seine Schleife (inklusive Rechenbild prog/k2rnull)
- **Artikel:** content/prog/02-werte-typen-und-variablen/04-zahlen-im-binarsystem.md
- **Stelle:** Das Verdopplungsverfahren — Beispiel 2 „Damit sich keine Rundung einschleicht, rechnet man mit dem Bruch $\frac z{10}$ …“
- **Art:** neue Animation (Verfahren), plus bestehendes Rechenbild als echte Operation
- **Was zu sehen ist:** Links ein Zähler-Kasten „z/10“ (Start 1/10), in der Mitte eine Verdopplungsmaschine („mal 2; ab 10: Stelle 1 und 10 abziehen“), rechts eine wachsende Bitreihe „0,“ für die Binärstellen. Unten ein kleiner Zustandsring mit den Zählern 2, 4, 8, 6.
- **Ablauf:** 1. 1/10 → 2/10, Stelle 0. 2. 2/10 → 4/10, Stelle 0. 3. 4/10 → 8/10, Stelle 0. 4. 8/10 → 16/10: Stelle 1, Rest 6/10. 5. 6/10 → 12/10: Stelle 1, Rest 2/10. 6. Der Zähler 2/10 hat denselben Wert wie nach Schritt 1: ein Rückpfeil schließt den Ring 2 → 4 → 8 → 6 → 2, die Bitreihe zeigt 0,0 0011 0011 … (Gruppe 0011 mit Klammer wiederholt). 7. Zum Schluss die Summe der ersten vier Einserpaare als Operation Σ (Term $3/2^{4k+1}$, $k=1$ bis 4): $\frac3{32}+\frac3{512}+\frac3{8192}+\frac3{131072}=\frac{13107}{131072}\approx0{,}0999985$ (das bisher statische prog/k2rnull wird so zur echten Operation). — Haltepunkte: 4, 6.
- **Verständnisproblem:** Wie die Stellen entstehen und warum sie sich wiederholen müssen; die zehn Zustände bzw. der Ring sind aus der Tabelle schwer zu sehen.
- **Szenenname:** prog/k2verdoppeln (Rechenbild bleibt prog/k2rnull, nur als Summation)
- **Editor-Lücke:** machbar; Zähler über die Zeit wäre L3 (Behelf: Zeilen nacheinander per Write)

#### Artikel 05 — Gleitkommazahlen: der Typ float (Soll 5, vorh. 3)

### V31 [A] 0,1 wird auf den nächsten `float` gerundet
- **Artikel:** content/prog/02-werte-typen-und-variablen/05-gleitkommazahlen-der-typ-float.md
- **Stelle:** Der Darstellungsfehler — „Von Hand: die Felder von $0{,}1$ vorhersagen. Aus dem Verdopplungsverfahren ist $0{,}1=0{,}0001\,1001\,1001\ldots{}_2$ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben die unendliche Binärfolge $1{,}1001\,1001\,1001\ldots{}_2\cdot2^{-4}$ mit einer Trennlinie hinter der 52. Stelle. Darunter ein Zahlenstrahl-Ausschnitt mit zwei benachbarten `float` (linker Nachbar …`9`, rechter …`a`) und der Marke für $0{,}1$ dazwischen. Daneben die Hexadezimalziffern `9999999999999` / `999999999999a`.
- **Ablauf:** 1. Die Binärfolge schreibt sich von links (Write). 2. Die Trennlinie hinter Stelle 52 erscheint; der abgeschnittene Rest beginnt mit 1 1 …. 3. Auf dem Zahlenstrahl liegt $0{,}1$ näher am rechten Nachbarn (Abstand zum rechten Nachbarn kleiner als der halbe Abstand der beiden Nachbarn); Pfeil zum rechten Nachbarn; die letzte Hexziffer wechselt von `9` auf `a`. 4. Beschriftung „gespeichert: $\frac{3602879701896397}{2^{55}}$, um $5{,}55\cdot10^{-18}$ zu groß“. — Haltepunkt: 3.
- **Verständnisproblem:** Wie aus einer unendlichen Folge ein gespeichertes Feld wird, und warum aufgerundet wird.
- **Szenenname:** prog/k2runden
- **Editor-Lücke:** machbar

### V32 [A] Die kürzeste Darstellung als Etikett für einen `float`
- **Artikel:** content/prog/02-werte-typen-und-variablen/05-gleitkommazahlen-der-typ-float.md
- **Stelle:** Die kürzeste Darstellung — „Zwischen zwei benachbarten `float` liegen unendlich viele Dezimalzahlen. Alle, die näher am gespeicherten Wert liegen als an seinen Nachbarn …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zahlenstrahl-Ausschnitt mit drei benachbarten `float`: L (`0x1.3333333333333p-2`, gespeichert für `0.3`), R (`0x1.3333333333334p-2`, das Ergebnis von `0.1 + 0.2`) und dem Nachbarn links von L. Um jeden `float` ein farbiges Band (Einzugsgebiet bis zur Mitte zum Nachbarn). Darunter Etiketten.
- **Ablauf:** 1. Die drei `float` als Punkte, dann ihre Bänder (Create). 2. Dezimalzahl `0.3` wird eingetippt (Marke wandert aufs Band von L): „landet bei L“ → Etikett `0.3` für L. 3. Für R: `0.3` liegt nicht in R's Band; Kandidaten mit mehr Stellen erscheinen nacheinander (`0.30000000000000004` liegt im Band) → Etikett für R. 4. Fazit: „Angezeigt ist das kürzeste Etikett, nicht der gespeicherte Wert“. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Warum `0.1` angezeigt wird, obwohl etwas anderes gespeichert ist, und warum `0.1 + 0.2` plötzlich 17 Stellen zeigt.
- **Szenenname:** prog/k2etikettfloat
- **Editor-Lücke:** machbar

#### Artikel 06 — Rechnen mit Gleitkommazahlen (Soll 4, vorh. 0)

### V33 [A] `0.1 + 0.2`: exakt gerechnet, dann gerundet, Gleichstand zur geraden Mantisse
- **Artikel:** content/prog/02-werte-typen-und-variablen/06-rechnen-mit-gleitkommazahlen.md
- **Stelle:** Der Rundungsfehler einer Rechnung — Beispiel „Die gespeicherten Werte sind etwas größer als $0{,}1$ und $0{,}2$. Ihre exakte Summe ist …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zahlenstrahl-Ausschnitt mit drei Marken: linker Nachbar (`float` für `0.3`, Mantissenfeld endet auf `3` = Bit 1), exakte Summe in der Mitte, rechter Nachbar (angezeigt als `0.30000000000000004`, Mantissenfeld endet auf `4` = Bit 0). Maßpfeile zwischen den Marken, beide $2{,}78\cdot10^{-17}$.
- **Ablauf:** 1. Die gespeicherten `0.1` und `0.2` (kleine Marken, etwas rechts von 0,1 und 0,2), Pfeil „addiere exakt“ → die exakte Summe landet auf dem Zahlenstrahl. 2. Die zwei Nachbarn erscheinen, beide Maßpfeile gleich lang. 3. „Gleichstand“: die Mantissen-Endbits (…3 → 1, …4 → 0) werden eingeblendet, der Pfeil von der Summe zeigt auf den rechten Nachbarn (gerades Bit). 4. Ergebnis: nicht der `float` von `0.3`. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Warum die Summe zweier „ungenauer“ Zahlen auf einem bestimmten Nachbarn landet; die Rundung zur geraden Mantisse ist reine Textregel.
- **Szenenname:** prog/k2gleichstand
- **Editor-Lücke:** machbar

### V34 [A] Das Raster der `float` bei 1 und bei $10^{16}$: Maschinengenauigkeit und Absorption
- **Artikel:** content/prog/02-werte-typen-und-variablen/06-rechnen-mit-gleitkommazahlen.md
- **Stelle:** Die Maschinengenauigkeit — „Addiert man zu 1 den Wert $2^{-52}$, entsteht der Nachbar von 1. Addiert man nur die Hälfte, $2^{-53}$ …“; ebenso Die Absorption
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Zahlenstrahl-Ausschnitte untereinander: Raster um 1 (Teilstriche im Abstand $\varepsilon_{\mathrm M}=2^{-52}$) und Raster um $10^{16}$ (Teilstriche im Abstand 2). Ein Summand-Pfeil (Länge des zu addierenden Werts).
- **Ablauf:** 1. Raster um 1: `1.0 + 2 ** -52`, der Pfeil reicht genau bis zum nächsten Strich, Ergebnis 1.0000000000000002. 2. `1.0 + 2 ** -53`: der Pfeil endet genau in der Mitte zwischen 1 und dem Nachbarn, Gleichstand, der Ergebnispfeil springt zurück auf 1.0. 3. Zweiter Ausschnitt $10^{16}$, Abstand 2: `1e16 + 1` endet in der Mitte, springt zurück auf `1e16`. 4. `1e16 + 2` trifft den Nachbarn. 5. Reihenfolge: `1e16 + 1 - 1e16 = 0.0`, `1e16 - 1e16 + 1 = 1.0` als zwei kurze Zeilen. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Maschinengenauigkeit und Absorption beruhen auf einem Raster, das mit der Größe der Zahl gröber wird; nur Textregeln.
- **Szenenname:** prog/k2raster
- **Editor-Lücke:** machbar

### V35 [A] Auslöschung: 4,5 Rasterschritte werden zu 5
- **Artikel:** content/prog/02-werte-typen-und-variablen/06-rechnen-mit-gleitkommazahlen.md
- **Stelle:** Die Auslöschung — Beispiel „$1+10^{-15}$ wird beim Speichern auf ein Vielfaches von $2^{-52}$ gerundet. Zieht man 1 wieder ab, sieht man genau diese Rundung …“
- **Art:** neue Animation
- **Was zu sehen ist:** Raster um 1 mit nummerierten Rasterschritten 0, 1, 2, …, 6 (Abstand $2^{-52}\approx2{,}22\cdot10^{-16}$); die Marke $1+10^{-15}$ liegt bei etwa 4,5 Schritten (genauer 4,50…). Rechts ein Balkenpaar „Ergebnis“ und „soll“.
- **Ablauf:** 1. Marke $1+10^{-15}$ erscheint bei 4,5…. 2. Pfeil zum nächsten Rasterpunkt, Schritt 5 (≈ $1{,}11\cdot10^{-15}$ über 1). 3. „minus 1“: der Abstand von 1 bis zum Rasterpunkt wird als Balken herausgezogen: `1.1102230246251565e-15` neben dem Soll-Balken $10^{-15}$. 4. Unterschrift „+11 %: von 16 Stellen bleibt eine“. — Haltepunkt: 3.
- **Verständnisproblem:** Warum ein winziger Eingangsfehler relativ zum kleinen Ergebnis groß wird.
- **Szenenname:** prog/k2ausloeschung
- **Editor-Lücke:** machbar

### V36 [B] Überlauf, `inf` und `nan` im Bitfeld
- **Artikel:** content/prog/02-werte-typen-und-variablen/06-rechnen-mit-gleitkommazahlen.md
- **Stelle:** Der Überlauf: `inf` — „IEEE 754 hat dafür einen eigenen Wert reserviert: unendlich.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Zahlenstrahl nach rechts (Beschriftungen $10^{300}$, $1{,}797\cdot10^{308}$ als senkrechte Wand) und darunter der 64-Bit-Streifen aus prog/k2bitfelder (Vorzeichen | Exponentenfeld | Mantissenfeld).
- **Ablauf:** 1. Ein Punkt „1e308“ wird mit `* 10` nach rechts geschoben und stößt an die Wand; Ergebnis `inf`, der Streifen zeigt $c=2047$ (alle elf Bits 1), Mantisse 0. 2. `1e309 - 1e309`: zwei `inf`-Pfeile heben sich auf, Ergebnis `nan`; im Streifen $c=2047$, Mantisse ungleich 0. 3. `nan + 1` bleibt `nan`. — Haltepunkt: 2.
- **Verständnisproblem:** Dass `inf` und `nan` bestimmte Bitmuster sind und dass `nan` ansteckend ist.
- **Szenenname:** prog/k2infnan
- **Editor-Lücke:** machbar (Streifen aus k2bitfelder wiederverwenden)

#### Artikel 07 — Variablen: Namen für Objekte (Soll 4, vorh. 1)

### V37 [A] Zuweisungen Zeile für Zeile: Namen zeigen auf Objekte
- **Artikel:** content/prog/02-werte-typen-und-variablen/07-variablen-namen-fur-objekte.md
- **Stelle:** Die Zuweisung — Beispiel „Spannung, Widerstand und Strom aus dem ohmschen Gesetz“ (und Die Variable)
- **Art:** neue Animation
- **Was zu sehen ist:** Links die vier Programmzeilen `spannung = 5`, `widerstand = 470`, `strom = spannung / widerstand`, `leistung = spannung * strom` (Monospace, ein Rechteck als Zeilenmarke). In der Mitte eine Spalte „Namen“ (Etiketten, zunächst leer), rechts Objektkästen mit Typaufschrift. Ganz rechts ein Terminal.
- **Ablauf:** 1. Marke auf Zeile 1: Kasten `int` 5 entsteht (GrowFromCenter), Etikett `spannung` erscheint, Pfeil Name → Kasten. 2. Zeile 2: Kasten 470, Etikett `widerstand`. 3. Zeile 3: `spannung / widerstand` wird ausgewertet (beide Pfeile laufen in eine Rechenbox), neuer Kasten `float` 0.010638297872340425, Etikett `strom`. 4. Zeile 4: Kasten `float` 0.05319148936170213, Etikett `leistung`; zuvor kurz: `leistung` allein → NameError (Etikett fehlt). 5. Terminal: Die Zuweisungszeilen zeigen nichts an, `leistung` allein zeigt den Wert. Nach jeder Zeile verschiebt sich die Marke. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Python-Semantik: Zuweisung wertet rechts aus und bindet links einen Namen an das entstandene Objekt; ein Name existiert erst nach der Zuweisung. Das ist der Kern von Abschnitt 6, bisher nur als Satz.
- **Szenenname:** prog/k2zuweisung
- **Editor-Lücke:** machbar; L8 (Code-Objekt mit Zeilen-Hervorhebung, Variablenzustand) wäre hilfreich, Behelf: Textzeilen + per Shift wanderndes Rechteck

### V38 [B] `print = 5`: der Name wird umgehängt
- **Artikel:** content/prog/02-werte-typen-und-variablen/07-variablen-namen-fur-objekte.md
- **Stelle:** Die Namensregeln — „Eine Falle: eingebaute Namen überschreiben. `print`, `type`, `id` und die anderen eingebauten Funktionen sind ebenfalls Namen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links drei Etiketten `print`, `type`, `id` mit Pfeilen auf je ein Funktions-Objekt (Kästen „Funktion print“ usw.); rechts ein `int`-Kasten 5.
- **Ablauf:** 1. `print("Hallo")`: Pfeil von `print` zum Funktionskasten, Ausgabe `Hallo`. 2. `print = 5`: das Etikett `print` wird auf den `int`-Kasten umgehängt (Rotate des Pfeils um den Etikett-Anker; beide Kästen liegen auf demselben Kreis um den Anker, daher genau). Der Funktionskasten hat kein Etikett mehr (gestrichelter Rand). 3. `print("Hallo")`: der Pfeil führt zum `int`-Kasten, Blitz, `TypeError: 'int' object is not callable`. — Haltepunkt: 2.
- **Verständnisproblem:** Dass eine Zuweisung auch einen schon vergebenen Namen umhängt und die Funktion dadurch nicht mehr erreichbar ist.
- **Szenenname:** prog/k2printfalle
- **Editor-Lücke:** L-neu: Pfeilende animieren (ein Pfeil Name → Objekt soll auf ein anderes Objekt „umgebogen“ werden); Behelf: Rotate um den Etikett-Anker, nur exakt, wenn beide Kästen gleich weit vom Anker liegen, sonst neuer Pfeil und alter gestrichelt

### V39 [B] Das LED-Skript Zeile für Zeile
- **Artikel:** content/prog/02-werte-typen-und-variablen/07-variablen-namen-fur-objekte.md
- **Stelle:** Variablen im Skript — „Mit Namen sieht dasselbe Skript so aus: …“ (`led_variablen.py`)
- **Art:** neue Animation
- **Was zu sehen ist:** Links die neun Zeilen von `led_variablen.py` (Kommentare ausgeblendet), rechts eine Tabelle „Name | Wert“, darunter ein Terminal. Zeilenmarke (Rechteck).
- **Ablauf:** 1. `u_batterie = 9`, `u_led = 2.0`, `strom = 0.020`: drei Tabellenzeilen füllen sich. 2. `u_widerstand = u_batterie - u_led`: die zwei Werte laufen in eine Rechenbox, neue Zeile 7.0. 3. `widerstand = u_widerstand / strom`: 7.0 / 0.020 = 350.0. 4. `leistung = u_widerstand * strom`: 0.14. 5. Zwei `print`-Zeilen: Terminal `Vorwiderstand in Ohm: 350.0`, `Leistung im Widerstand in W: 0.14`. — Haltepunkte: 3, 5.
- **Verständnisproblem:** Wie ein Skript Wert für Wert aufgebaut wird und warum man nur die Annahmen oben ändern muss.
- **Szenenname:** prog/k2ledskript
- **Editor-Lücke:** L8 hilfreich (Behelf: Textzeilen, Marke per Shift, Table für Namen/Werte)

#### Artikel 08 — Wahrheitswerte und Vergleiche (Soll 4, vorh. 0)

### V40 [A] Ein Vergleich liefert einen Wahrheitswert
- **Artikel:** content/prog/02-werte-typen-und-variablen/08-wahrheitswerte-und-vergleiche.md
- **Stelle:** Die Vergleichsoperatoren — „Woher kommen Wahrheitswerte? Meist aus einem Vergleich zweier Werte.“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Vergleichsmaschine (Kasten mit dem Operator), links zwei Eingänge, rechts eine zweifarbige Lampe `True`/`False`.
- **Ablauf:** 1. `7 > 5`: zwei `int`-Kästen hinein, Lampe `True`. 2. `2 + 3 == 5`: erst werden beide Seiten ausgerechnet (links 5, rechts 5, kleine Rechenboxen), dann Vergleich: `True` (Beschriftung: Rang niedriger als die Arithmetik). 3. `1 == 1.0`: `True` (Wert zählt, nicht der Typ); `"2" == 2`: `False`. 4. Daneben `x = 5` (Etikett wird gehängt, nichts vergleichen) gegen `x == 5` (Lampe), mit der Beschriftung „bindet“ / „vergleicht“. — Haltepunkt: 2.
- **Verständnisproblem:** Wahrheitswerte als Ergebnis einer Rechnung, die Reihenfolge (erst rechnen, dann vergleichen) und `=` gegen `==`.
- **Szenenname:** prog/k2vergleich
- **Editor-Lücke:** machbar

### V41 [A] `==` fragt „bit-gleich?“, die Toleranz fragt „nah genug?“
- **Artikel:** content/prog/02-werte-typen-und-variablen/08-wahrheitswerte-und-vergleiche.md
- **Stelle:** Der Vergleich mit Toleranz — „Wie bei Bauteiltoleranzen. Ein Widerstand mit $4{,}7\,\mathrm{k\Omega}$ und 5 % Toleranz …“
- **Art:** neue Animation (baut auf den Bausteinen von prog/k2gleichstand (V33) auf)
- **Was zu sehen ist:** Zahlenstrahl-Ausschnitt mit zwei benachbarten `float`, a = `0.1 + 0.2` und b = `0.3`. Zwei Lampen: `a == b` und `isclose`. Ein Toleranzband um b, Breite $r\cdot\max(|a|,|b|)$ (nicht maßstäblich gestaucht, mit Hinweis „r = $10^{-9}$ ist hier viel größer als der Abstand der beiden“).
- **Ablauf:** 1. a und b als zwei Punkte, der Abstand ist ein Rasterschritt. 2. `a == b`: Lampe `False` (nur gleich, wenn derselbe `float`). 3. `0.1 * 10 == 1.0`: beide Punkte fallen zusammen, `True` (Zufall der Rundung). 4. Das Toleranzband um b erscheint (Create), a liegt darin: `abs(a - b) <= 1e-9 * max(abs(a), abs(b))` → `True`. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Warum `==` für Ergebnisse von Rechnungen kein brauchbarer Test ist und was die Toleranz stattdessen tut.
- **Szenenname:** prog/k2toleranz
- **Editor-Lücke:** machbar

### V42 [B] Nahe null versagt der relative Vergleich
- **Artikel:** content/prog/02-werte-typen-und-variablen/08-wahrheitswerte-und-vergleiche.md
- **Stelle:** Der Vergleich mit Toleranz — „Die Grenze des relativen Vergleichs. Ist eine der beiden Zahlen 0, versagt der relative Vergleich …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zahlenstrahl mit dem Punkt a und der 0; um a ein Band der Breite $r\cdot|a|$ ($r=10^{-9}$), darunter ein schmaler fester Streifen ±$t_{\mathrm{abs}}$ um die 0.
- **Ablauf:** 1. a = 1000 mit breitem Band. 2. a wandert nach links (MoveTo/Scale), das Band schrumpft proportional mit; a = $10^{-3}$, $10^{-10}$, $3\cdot10^{-19}$. 3. Bei $3\cdot10^{-19}$ ist der Abstand zu 0 größer als das Band (gerade beim Abstand $|a-0|$ und Band $r|a|$): Kreuz, `False`. 4. Der absolute Streifen ($10^{-12}$) umfasst a: `True`. — Haltepunkt: 3.
- **Verständnisproblem:** Warum ein relativer Vergleich mit 0 nie `True` ergibt und die absolute Toleranz die Lücke schließt.
- **Szenenname:** prog/k2nullvergleich
- **Editor-Lücke:** L3 hilfreich (a als laufender Parameter); Behelf: vier Zustände nacheinander

### V43 [B] `is` fragt nach dem Objekt, `==` nach dem Wert
- **Artikel:** content/prog/02-werte-typen-und-variablen/08-wahrheitswerte-und-vergleiche.md
- **Stelle:** Der Identitätsvergleich — „Die Vergleichsoperatoren fragen nach dem Wert. Manchmal will man aber wissen, ob zwei Namen am selben Objekt hängen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zustandsdiagramm wie in prog/k2etikett: Etiketten `x`, `y`, `z`, zwei `float`-Kästen 1000.5 an verschiedenen Plätzen. Zwei Lampen `==` und `is`.
- **Ablauf:** 1. `x = 1000.5`, `y = 1000.5`: zwei Kästen mit je einem Etikett. 2. `x == y`: Lampe `True` (Wert gleich); `x is y`: `False` (verschiedene Plätze, Platznummern eingeblendet). 3. `z = x`: neues Etikett `z` am Kasten von `x`. 4. `z is x`: `True`. — Haltepunkt: 2.
- **Verständnisproblem:** Der Unterschied zwischen gleichem Wert und gleichem Objekt.
- **Szenenname:** prog/k2identitaet
- **Editor-Lücke:** machbar (Bausteine aus prog/k2etikett)

#### Artikel 09 — Module: math und sys (Soll 3, vorh. 0)

### V44 [A] Ein Modul ist ein Werkzeugkasten, den man holt
- **Artikel:** content/prog/02-werte-typen-und-variablen/09-module-math-und-sys.md
- **Stelle:** Das Modul und `import` — „Die Funktionen liegen deshalb in beschrifteten Werkzeugkästen. Man holt einen Kasten, wenn man ihn braucht …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Regal „bekannte Namen“ (Etiketten `print`, `type`, …), rechts ein Lager mit einem Werkzeugkasten „math“ (Objektkasten mit Typaufschrift `module`, Inhalt `sqrt`, `pi`, `exp`, `sin`, …).
- **Ablauf:** 1. `math.sqrt(2)`: Name `math` fehlt im Regal, Blitz `NameError: name 'math' is not defined`. 2. `import math`: der Kasten fliegt herein, ein Etikett `math` wird angeheftet. 3. `math.sqrt(2)`: der Punkt greift in den Kasten, `sqrt` wird herausgezogen, Ergebnis 1.4142135623730951. 4. `sqrt(2)` allein: das Regal hat kein Etikett `sqrt`, `NameError`. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Warum erst `import` nötig ist und warum nur `math` ein Name wird, nicht die Namen darin.
- **Szenenname:** prog/k2import
- **Editor-Lücke:** machbar

### V45 [B] Warum `math.sin(math.pi)` nicht 0 ist
- **Artikel:** content/prog/02-werte-typen-und-variablen/09-module-math-und-sys.md
- **Stelle:** Das Modul `math` — Beispiel „Die letzten beiden Zeilen zeigen wieder Rundungsfehler: $\sin30^\circ$ ist $0{,}5$, und $\sin\pi$ ist 0.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Ausschnitt der Sinuskurve um $\pi$ (stark vergrößert, Hinweis „nicht maßstäblich“), darunter der Zahlenstrahl mit dem exakten $\pi$ und `math.pi` um $\delta\approx1{,}2246\cdot10^{-16}$ links davon.
- **Ablauf:** 1. Sinuskurve und Nullstelle bei $\pi$. 2. Auf der Achse erscheint `math.pi` links von $\pi$ (kleiner Maßpfeil δ). 3. Ein Lot von `math.pi` auf die Kurve: Höhe $\approx\delta$, beschriftet `1.2246467991473532e-16`. 4. Satz: „Der Fehler steckt in der Eingabe, nicht in der Funktion.“ — Haltepunkt: 3.
- **Verständnisproblem:** Warum ein korrekt arbeitendes `sin` ein Ergebnis ungleich 0 liefert.
- **Szenenname:** prog/k2sinpi
- **Editor-Lücke:** machbar (Axes, FunctionGraph, Marker)

### V46 [C] Raster der `float` bei `math.ulp` wiederverwenden
- **Artikel:** content/prog/02-werte-typen-und-variablen/09-module-math-und-sys.md
- **Stelle:** Die Grenzen des Typs `float`, fertig — „`math.ulp(x)` ist der Abstand von $x$ zum nächsten `float` mit größerem Betrag …“
- **Art:** vorhandene Szene wiederverwenden: prog/k2raster (V34), dort die Beschriftungen `math.ulp(1.0)` und `math.ulp(1e16)` ergänzen
- **Was zu sehen ist:** wie V34; die Abstandspfeile tragen die Python-Aufrufe.
- **Ablauf:** 1. Abstand bei 1: `math.ulp(1.0)` = 2.220446049250313e-16 = `sys.float_info.epsilon`. 2. Abstand bei $10^{16}$: `math.ulp(1e16)` = 2.0. — Haltepunkt: 2.
- **Verständnisproblem:** Der Abstand benachbarter `float` ist der Wert hinter `math.ulp` und `epsilon`.
- **Szenenname:** prog/k2raster (Wiederverwendung)
- **Editor-Lücke:** machbar

#### Artikel 10 — Komplexe Zahlen (Soll 5, vorh. 2)

### V47 [A] Die Quadrantenfalle: `atan` gegen `atan2`
- **Artikel:** content/prog/02-werte-typen-und-variablen/10-komplexe-zahlen.md
- **Stelle:** Betrag und Phase: erst von Hand, dann fertig — „`math.atan(y / x)` sieht nur den Quotienten und liefert für $-3-4\mathrm j$ denselben Winkel wie für $3+4\mathrm j$ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Komplexe Ebene mit zwei Zeigern: $z=3+4\mathrm j$ (rechts oben) und $w=-3-4\mathrm j$ (links unten), beide auf derselben Geraden durch den Ursprung (Steigung 4/3). Zwei Winkelbögen mit Beschriftung.
- **Ablauf:** 1. Beide Zeiger und die gemeinsame Gerade. 2. `math.atan(w.imag / w.real)`: der Quotient $4/3$ ist derselbe; der Bogen von der positiven reellen Achse zum Strahl durch $z$: 0.9272952180016122 (53,13°), also zum falschen Strahl. 3. `math.atan2(w.imag, w.real)`: der Bogen läuft im Uhrzeigersinn bis zu $w$: −2.214297435588181 (−126,87°). 4. Kurzfassung: `cmath.phase(w)` gleich. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Warum der Quotient allein den Quadranten verliert (Python-Funktion mit zwei Argumenten ist nötig).
- **Szenenname:** prog/k2quadrant
- **Editor-Lücke:** machbar (ParametricCurve für die Bögen)

### V48 [C] Multiplikation komplexer Zahlen = Drehen und Strecken (vorhandene Szene)
- **Artikel:** content/prog/02-werte-typen-und-variablen/10-komplexe-zahlen.md
- **Stelle:** Was du dafür brauchst: komplexe Zahlen — „Beim Multiplizieren multiplizieren sich die Beträge, und die Phasen addieren sich …“
- **Art:** vorhandene Szene wiederverwenden: hm1/k7dreh (Drehen und Strecken, dort mit $i$); für diesen Artikel mit $\mathrm j$ beschriften oder Verweis auf die HM-Szene setzen. Der Artikel verweist schon auf Höhere Mathematik 1
- **Was zu sehen ist:** zwei Zeiger $z_1$, $z_2$, Produkt $z_1z_2$ mit Winkeln $\varphi_1$, $\varphi_2$; geeignet ist auch das Beispiel $(1+2\mathrm j)(3-4\mathrm j)=11+2\mathrm j$ aus dem Python-Beispiel: Beträge $\sqrt5\cdot5=\sqrt{125}$, Phasen $63{,}43^\circ+(-53{,}13^\circ)=10{,}30^\circ$.
- **Ablauf:** 1. $z_1$, $z_2$. 2. $z_1$ dreht sich um $\varphi_2$ (Rotate) und streckt sich um $|z_2|$ (Scale): Produkt. — Haltepunkt: 2.
- **Verständnisproblem:** Beim Rechnen mit `*` in Python (Beispiel `(1 + 2j) * (3 - 4j)`) steht das Ergebnis `(11+2j)` ohne Anschauung.
- **Szenenname:** hm1/k7dreh (Wiederverwendung) oder neu prog/k2dreh, falls j-Beschriftung nötig
- **Editor-Lücke:** machbar

### V49 [B] `complex` ist ein Paar von `float`
- **Artikel:** content/prog/02-werte-typen-und-variablen/10-komplexe-zahlen.md
- **Stelle:** Das Attribut: Real- und Imaginärteil — „Aus einer komplexen Zahl will man oft den Real- oder den Imaginärteil allein haben … Beide Teile stehen fertig im Objekt.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Objektkasten mit Typaufschrift `complex`, darin zwei Fächer (`float` 3.0 und `float` 4.0), angezeigt als `(3+4j)`. Am Kasten die Etiketten `.real` und `.imag`, ein Knopf `.conjugate()`.
- **Ablauf:** 1. `z = 3 + 4j`: Kasten entsteht mit zwei Fächern, Etikett `z` hängt daran. 2. `z.real`: Pfeil aus dem linken Fach, Wert 3.0; `z.imag`: 4.0. 3. `z.conjugate()`: ein neuer Kasten (3−4j), der alte bleibt. 4. `z.real = 5`: roter Blitz `AttributeError: readonly attribute`. — Haltepunkt: 3.
- **Verständnisproblem:** Wie Python komplexe Zahlen speichert und was ein Attribut ist (Wert am Objekt, ohne Klammern).
- **Szenenname:** prog/k2complexobjekt
- **Editor-Lücke:** machbar

#### Artikel 11 — Zeichenketten, Eingabe und Ausgabe (Soll 4, vorh. 0)

### V50 [A] Zeichenketten sind Folgen von Zeichen: verketten, wiederholen, zählen
- **Artikel:** content/prog/02-werte-typen-und-variablen/11-zeichenketten-eingabe-und-ausgabe.md
- **Stelle:** Zeichenketten verketten und vervielfachen — „Auch mit Text kann man einiges rechnen: Teile zusammensetzen, Linien aus Strichen bauen, die Länge bestimmen.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zeichen als einzelne Kästchen in einer Reihe mit Typaufschrift `str` (Index bewusst nicht gezeigt, kommt später).
- **Ablauf:** 1. „Ohm“ (3 Kästchen) und „meter“ (5): `+` schiebt die zweite Reihe an die erste, „Ohmmeter“ (8). 2. `"Ohm" * 3`: die Reihe wird dreimal kopiert, „OhmOhmOhm“. 3. `len("Größe")`: Zähler läuft über die 5 Kästchen, 5 (ö und ß zählen je als ein Zeichen). 4. `"4" + "2"` ergibt `'42'` (zwei Zeichen), `4 + 2` ergibt 6: Zeichen-Reihe gegen Zahl. — Haltepunkt: 4.
- **Verständnisproblem:** Dass `+` bei Text keine Zahlen verknüpft, und dass Text eine Folge einzelner Zeichen ist.
- **Szenenname:** prog/k2zeichen
- **Editor-Lücke:** machbar

### V51 [A] Der f-String als Formular mit Lücken
- **Artikel:** content/prog/02-werte-typen-und-variablen/11-zeichenketten-eingabe-und-ausgabe.md
- **Stelle:** Der f-String — „Ein Formular mit Lücken. Man schreibt den Text einmal hin und lässt Lücken; in jede Lücke kommt ein ausgerechneter Wert …“
- **Art:** neue Animation
- **Was zu sehen ist:** Der f-String `f"R = {U / I:.1f} Ohm, P = {U * I:.3e} W"` mit den zwei Lücken als Rahmen; darunter `U = 3.3`, `I = 0.0125`; am Ende der Ergebnistext.
- **Ablauf:** 1. Lücke 1: `U / I` wird mit den Werten ausgewertet (264.0), die Formatangabe `.1f` formt zu `'264.0'`, der Text fliegt in die Lücke. 2. Lücke 2: `U * I` = 0.04125, `.3e` formt zu `4.125e-02`, fliegt in die Lücke. 3. Ergebnis `'R = 264.0 Ohm, P = 4.125e-02 W'`. 4. Zusatz: `f"{0.1:.20f}"` zeigt `0.10000000000000000555`; das Objekt `0.1` bleibt unverändert (Formatangabe rundet nur die Anzeige). — Haltepunkte: 1, 4.
- **Verständnisproblem:** Das Zusammenspiel Ausdruck, Auswerten, Formatieren, Einsetzen; die Formatangaben sind Textregeln.
- **Szenenname:** prog/k2fstring
- **Editor-Lücke:** machbar

### V52 [A] Der Einheitenrechner: `input` liefert Text, `float` macht eine Zahl daraus
- **Artikel:** content/prog/02-werte-typen-und-variablen/11-zeichenketten-eingabe-und-ausgabe.md
- **Stelle:** Die Eingabe mit `input` und Die Typumwandlung (Beispiel `spannung * 2` ergibt `'55'`; Anwendung `einheiten.py`)
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Tastatur-Box (Eingabe „5“), ein Kasten `input(...)` mit dem Prompt „Spannung in V:“, Objektkästen mit Typaufschrift, rechts ein Terminal. Dann die Zeilen von `einheiten.py`.
- **Ablauf:** 1. `spannung = input(...)`: Skript hält an, das Terminal zeigt die Frage; „5“ + Enter → `str`-Kasten `'5'`, Etikett `spannung`. 2. `spannung * 2` → `'55'` (Text wiederholt). 3. `float('5')` erzeugt einen neuen Kasten `float` 5.0; der `str`-Kasten bleibt; Etikett `spannung` wird auf den neuen Kasten umgehängt. 4. Dasselbe für `widerstand_k` = 2.2. 5. `strom_ma = spannung / widerstand_k` (≈ 2,27…) und `leistung_mw = spannung * strom_ma` (≈ 11,36…), die f-Strings schreiben `Strom: 2.27 mA`, `Leistung: 11.36 mW`. 6. Falls `2,2` getippt: `float('2,2')` → `ValueError`. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Warum man mit einer Eingabe nicht rechnen kann und dass die Umwandlung ein neues Objekt erzeugt.
- **Szenenname:** prog/k2einheiten
- **Editor-Lücke:** L8 hilfreich (Programmablauf mit Variablenzustand); Behelf: Textzeilen, Marke per Shift

### V53 [B] Runden: `round` gegen `int(x + 0.5)` am Zahlenstrahl
- **Artikel:** content/prog/02-werte-typen-und-variablen/11-zeichenketten-eingabe-und-ausgabe.md
- **Stelle:** Runden: erst von Hand, dann fertig — „`int` schneidet ab. Addiert man vorher $0{,}5$, wird aus dem Abschneiden ein Runden …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zahlenstrahl von −3 bis 4 mit Ganzzahlmarken; fünf Punkte x = 2.7, 2.5, 3.5, −2.5, −2.7. Zwei Pfeilfarben: `round` (blau), `int(x + 0.5)` (orange).
- **Ablauf:** 1. x = 2.7: beide Pfeile zur 3. 2. x = 2.5: `round` zur 2 (gerade), `int(x+0.5)` zur 3. 3. x = 3.5: beide zur 4. 4. x = −2.5: beide zur −2. 5. x = −2.7: `round` zur −3, `int(x+0.5)` zur −2 (roter Rahmen „falsch“, weil `int` Richtung null abschneidet). — Haltepunkte: 2, 5.
- **Verständnisproblem:** Wo der Weg von Hand versagt (Hälften, negative Zahlen) und die Regel zur geraden Zahl.
- **Szenenname:** prog/k2runden-round
- **Editor-Lücke:** machbar

#### Artikel 12 — Das Wichtigste bis hier (Soll 1, vorh. 0)

### V54 [A] Der Typ legt die Darstellung fest (Zusammenschau)
- **Artikel:** content/prog/02-werte-typen-und-variablen/12-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt daraus, dass der Typ eines Objekts festlegt, wie sein Wert im Speicher steht …“
- **Art:** neue Animation
- **Was zu sehen ist:** Vier Objektkästen: `int` (Ziffernreihe, wächst), `float` (64-Bit-Streifen aus prog/k2bitfelder), `complex` (zwei `float`-Fächer), `str` (Zeichenreihe). Darunter acht Karten aus der Ergebnistabelle (`"2" + 3` ist ein Fehler, `int` läuft nie über, $0{,}1$ ist nicht exakt, `0.1 + 0.2 != 0.3`, `y = x` kopiert nicht, …).
- **Ablauf:** 1. Die vier Kästen erscheinen nacheinander mit ihren Speicherformen. 2. Jede Karte fliegt zu dem Kasten, aus dessen Darstellung sie folgt (Pfeil). 3. `y = x kopiert nicht` bekommt als Sonderfall ein Etikett-Symbol (Namen sind keine Kästen). — Haltepunkt: 2.
- **Verständnisproblem:** Der Kern-Artikel ist eine reine Textliste; die integrierende Einsicht (Darstellung bestimmt die Rechenregeln) ist nicht sichtbar.
- **Szenenname:** prog/k2darstellung
- **Editor-Lücke:** machbar (Bausteine aus k2bitfelder, k2objekt wiederverwenden)

## Vorhandene Abbildungen

### prog/02
- prog/k2objekt (02-objekte-und-typen.md): animieren ja — Schritte: 1. Speicher als Reihe von Fächern. 2. Kasten 1 (`int` 42) erscheint mit Platznummer, Aufschrift `int`. 3. Kasten 2 (`float` 4.0), Kasten 3 (`str` "42"). 4. Pfeile für `type(...)` auf die Aufschrift und `id(...)` auf die Platznummer. | Lücke: machbar
- prog/k2rest (03-ganze-zahlen-und-rechenoperatoren.md): animieren ja — Schritte: 1. Zahlenstrahl mit allen Vielfachen von 2. 2. $a=7$: Marke, das nächste Vielfache links ($6=3\cdot2$) wird markiert, der Restpfeil wächst (Rest 1). 3. $a=-7$: Marke, nächstes Vielfaches links $-8=(-4)\cdot2$ (nicht $-6$), Rest 1. | Lücke: machbar
- prog/k2rbinaer (04-zahlen-im-binarsystem.md): statisches Rechenbild (einziger MathTex, keine Operation); entfällt als eigene Abbildung und geht in die Schalterreihen-Animation V28 mit echter Σ-Operation auf. | Lücke: machbar
- prog/k2rbyte (04-zahlen-im-binarsystem.md): animieren ja, ist bereits eine echte Summation ($\sum_{i=0}^{7}2^i=255$, `show_terms: 8`, `all_steps`) — Schritte: Term für Term 1, 2, 4, …, 128, laufende Summe 255, dann „=$2^8-1$“. | Lücke: machbar
- prog/k2rnull (04-zahlen-im-binarsystem.md): statisches Rechenbild (MathTex); ersetzen durch Operation Σ ($3/2^{4k+1}$, $k=1\ldots4$), Schritt für Schritt Summand für Summand, im Zusammenhang mit V30. | Lücke: machbar
- prog/k2zahlenstrahl (05-gleitkommazahlen-der-typ-float.md): animieren ja — Schritte: 1. Achse 0 bis 8. 2. Zeile $E=-1$: vier Punkte (0,5; 0,625; 0,75; 0,875). 3. $E=0$: vier Punkte mit Abstand 0,25. 4. $E=1$, $E=2$ nacheinander, die Abstände verdoppeln sich. 5. Marke für 6,5: fällt zwischen 6 und 7, Pfeil „runden“. | Lücke: machbar
- prog/k2bitfelder (05-gleitkommazahlen-der-typ-float.md): animieren ja — Schritte: 1. Der Streifen mit 64 Bit, die drei Felder werden nacheinander farbig (Vorzeichen, 11 Bit Exponent, 52 Bit Mantisse). 2. Zeile 6,5: $s=0$, $c=10000000001_2=1025$, Mantisse beginnt mit 101. 3. Zeile 0.1: $c=01111111011_2=1019$, Mantisse 999999999999a. | Lücke: machbar
- prog/k2rfloat (05-gleitkommazahlen-der-typ-float.md): statisches Rechenbild (einziger MathTex, mehrzeilig, keine Operation; kein Σ/∏/Skalarprodukt, daher nicht Pflicht); animieren ja als zeilenweiser Aufbau (Write je Zeile: Formel, Zahlen eingesetzt, Bruch, Dezimalwert). | Lücke: L2 für das Umformen von Zeile zu Zeile, sonst machbar
- prog/k2etikett (07-variablen-namen-fur-objekte.md): animieren ja — Schritte: 1. `x = 5`: Etikett `x` an Kasten 5. 2. `y = x`: zweites Etikett `y` am selben Kasten. 3. `x = x + 1`: neuer Kasten 6 entsteht, das Etikett `x` wird umgehängt (Rotate des Pfeils um den Etikett-Anker, Kästen im gleichen Abstand, oder neuer Pfeil und alter gestrichelt). Das Objekt 5 bleibt, `y` hängt weiter daran. | Lücke: machbar (L1 würde den alten Pfeil verschwinden lassen)
- prog/k2zeiger (10-komplexe-zahlen.md): animieren ja — Schritte: 1. Achsen der komplexen Ebene. 2. Realteil 3 (Pfeil nach rechts), Imaginärteil 4 (Pfeil nach oben). 3. Zeiger vom Nullpunkt (Create), Länge 5. 4. Winkelbogen $\varphi=53{,}13^\circ$ (Create der ParametricCurve). 5. $z^*$ gestrichelt (Spiegelung). 6. Rechts die Python-Ausdrücke Zeile für Zeile. | Lücke: machbar
- prog/k2rc (10-komplexe-zahlen.md): animieren ja — Schritte: 1. Realteil $R=1000$ (Pfeil nach rechts). 2. $-1591{,}5\,\mathrm j$ (Pfeil nach unten). 3. Summenzeiger $Z$ (Create). 4. Winkelbogen $-57{,}86^\circ$, Betrag 1879,6. | Lücke: machbar


### prog/01
- prog/k1heron (02-programme-und-programmiersprachen.md): animieren ja — Schritte: 1. Zahlenstrahl mit Marke $\sqrt2$ (Create/Write). 2. Durchgang 1: Punkte $g=1$ und $2/g=2$ erscheinen (FadeIn), Mittelwert-Strich bei 1,5 (Create). 3. Der Strich wird zum neuen $g$; $2/g=1{,}333$ erscheint auf der anderen Seite. 4. Durchgang 2 und 3 analog, Abstand schrumpft von 1 über 0,17 auf 0,005. | Lücke: machbar (L3 wäre die saubere Fassung, ein Parameter-Sweep)
- prog/k1wege (03-vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.md): animieren ja — Schritte: 1. Links `hallo.py` → `python` übersetzt die Datei in Bytecode, danach arbeitet die Interpreterschleife (Marke wandert) → Ausgabe. 2. Rechts `hallo.c` → `gcc` einmalig → `hallo.exe` → Prozessor. 3. Zweiter Start: links wieder Übersetzen, rechts Compiler entfällt. | Lücke: machbar
- prog/k1modi (06-skripte-schreiben-und-ausfuhren.md): animieren ja — Schritte: 1. Links: Eingabe → Auswerten → Anzeigen, Kreislauf wiederholt. 2. Rechts: ganze Datei `ausdruck.py` übersetzen, dann Zeilen nacheinander, `2 + 3` wird gerechnet, der Wert wandert in einen „verworfen“-Kasten, nur die zwei `print`-Zeilen erscheinen im Terminal. | Lücke: machbar
- prog/k1fehlerarten (07-fehler-lesen-und-verstehen.md): animieren ja — Schritte: 1. Beide Dateien erscheinen. 2. Links: Prüfung läuft über die Datei, bleibt bei Zeile 3 stehen, alle drei Zeilen werden grau, keine Ausgabe. 3. Rechts: Prüfung grün, Zeile 1 läuft (Ausgabe „Zeile 1“), Zeile 2 bricht ab (Blitz), Zeile 3 bleibt grau. Optional dritte Spalte „Logikfehler“: alle Zeilen laufen, falsches Ergebnis, niemand meldet es. | Lücke: machbar
- prog/k1traceback (07-fehler-lesen-und-verstehen.md): animieren ja — Schritte: 1. Der Traceback erscheint komplett. 2. Von unten nach oben werden die Teile nummeriert eingeblendet: 5 Ausnahme (Art und Beschreibung), dann 4, 3, 2 (Stelle). 3. Zum Schluss Pfeil „so liest man“. | Lücke: machbar
