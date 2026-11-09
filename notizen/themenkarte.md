# Themenkarte: Wo ist welches Thema vollständig erklärt?

Regel des Users (06.11.2026): „Inhalte nicht mehrfach auf der Webseite vollständig erklären“. Jedes Thema hat genau einen
Ort, an dem es vollständig erklärt wird. Andere Hefte setzen es voraus, fassen es höchstens in ein bis drei Sätzen zusammen
und verweisen mit Link darauf.

## So benutzt du die Karte (Schreib-Agenten)
1. **Vor dem Schreiben nachsehen:** Für jeden Begriff deines Lernpfad-Eintrags mit Grep in dieser Datei suchen (Wortstamm,
   auch englisch), nicht die ganze Datei lesen. Jede Zeile beginnt mit der Verweis-Wendung des Abschnitts.
2. **Gefunden:** nicht neu erklären. Im Heft steht dann „Was du dafür brauchst“ mit einer kurzen, selbsttragenden
   Zusammenfassung (Definition, eine Formel, ein Mini-Beispiel) und dem Verweis in genau dieser Form; auf der Website wird er
   zum Link auf Artikel und Abschnitt:
   - ML-Grundlagen: „Grundlagen 1, Abschnitt 13.5“, ML-Pfad: „Teil 2, Abschnitt 3.1“ (Teil N = Lernpfad-Heft T(N+7));
   - Programmieren: „Programmieren, Python 2, Abschnitt 3.1“ (später „Programmieren, C 1, …“, „Programmieren, C++ 1, …“);
   - Linux und Kommandozeile: „Linux 2, Abschnitt 3.1“;
   - mehrere: „Grundlagen 1, Abschnitte 10.1 und 11.4“; das ganze Heft: „Grundlagen 1“.
   Übersetzungen: notizen/heft_uebersetzung.md, Abschnitt „Verweise auf andere Hefte“. Für die Uni-Module (Elektrotechnik,
   Höhere Mathematik) gibt es noch keine automatische Link-Wendung über Modulgrenzen; dort den Abschnitt im Bericht nennen.
3. **Nicht gefunden:** Du erklärst es vollständig, wenn es zu deinem Heft gehört (siehe „Zuständigkeiten“ unten). Gehört es in
   einen anderen Bereich, der noch kein Heft dazu hat, trägst du es unten unter „Geplant“ mit dem vorgesehenen Ort ein und
   fragst im Bericht nach.
4. **Nach dem Heft:** `python tools/themenkarte.py` im Repo ausführen. Das Skript erzeugt alles unterhalb von „Erklärt in“
   neu aus den Heften; nur der Teil zwischen den Markierungen „von Hand“ bleibt stehen.

<!-- von Hand: Anfang -->
## Zuständigkeiten und geplante Themen (von Hand)
- **Programmieren** (Informatik / Programmieren, Python 1 bis 3 fertig): Python als Sprache, Datenstrukturen, Funktionen, Module,
  venv, NumPy-Grundlagen; später C und C++. ML und Cybersecurity setzen das voraus.
  - Python 1 erklärt vollständig: Programm/Anweisung, Maschinenbefehl, Programmiersprache, Syntax, Semantik, Quelltext,
    Compiler, Interpreter, CPython, Bytecode, Python installieren (Windows install manager `py`, Linux `python3`),
    Versionsnummer, interaktiver Modus, Wert, Ausdruck, Grundrechenzeichen `+ - * / **` (nur als Taschenrechner),
    Zeichenkette (nur Literal), Funktion und Funktionsaufruf (nur `print`), Editor, Skript, Kommentar, Syntaxfehler,
    Laufzeitfehler, Ausnahme (Art + Beschreibung), Traceback, Logikfehler.
  - Python 2 erklärt vollständig: Objekt, Typ, Identität (`id`), Methode, Attribut, `int` (beliebig groß), Operatoren und
    Rangfolge, `/`, `//`, `%` (auch negativ), `**`; Stellenwertsystem, Bit, Byte, Binär- und Hexadezimalzahl, Binärbruch,
    Verdopplungsverfahren; Gleitkommazahl und IEEE 754 binary64 (Exponenten-/Mantissenfeld), Darstellungsfehler, kürzeste
    Darstellung, Rundungsfehler, Maschinengenauigkeit, Absorption, Auslöschung, `inf`, `nan`; Variable, Zuweisung, Namensregeln,
    erweiterte Zuweisung; `bool`, Vergleichsoperatoren, Toleranzvergleich (`math.isclose`), `is`, `None`; Modul/`import` (nur
    `import x`), `math`, `sys.float_info`; `complex`, `cmath`; Zeichenketten-Operatoren und `len`, f-String, `input`,
    Typumwandlung, `round`. Cyber T02 (Bit/Byte/Hex) und ML Grundlagen 3, Abschnitt 11.3 (Gleitkommazahlen) können darauf
    verweisen. Unicode-Nummern von Zeichen (U+201E): Python 9.
  - Python 3 erklärt vollständig: verkettete Vergleiche, Vergleich von Zeichenketten, `not`/`and`/`or`, Rangfolge,
    Kurzschlussauswertung, Wahrheitswert von Objekten (ohne Behälter), Ergebnis von `and`/`or`; `if`/`elif`/`else`, Block und
    Einrückung (Kopfzeile, IndentationError, TabError), `match` nur als Hintergrund; `while`, Endlosschleife, Strg+C/
    `KeyboardInterrupt`, Gleitkomma-Falle in Schleifen; `for`, `range`, Schleifenvariable; `break`, `continue`, `else` an Schleifen
    (Hintergrund), verschachtelte Schleifen, Akkumulator (Summe, Anzahl, Produkt, Mittelwert, Maximum); Raten und Prüfen,
    Näherung mit Toleranz, Zwischenwertsatz (Nullstellen-Fassung), Bisektion mit Schrittzahl, Tangente, Newton-Verfahren,
    quadratische Konvergenz, Heron = Newton, `math.sqrt`; Diodenarbeitspunkt numerisch. Numerik-Hefte und ML-Grundlagen
    (Gradientenabstieg, Optimierung) können für Bisektion/Newton darauf verweisen. Eigene Funktionen: Python 4; Listen: Python 5.
- **Linux und Kommandozeile** (Informatik / Linux und Kommandozeile, noch ohne Heft): Shell, Dateien, Rechte, Prozesse.
  Cybersecurity Teil 3 bis 5 werden nach der Recherche cyber-spezifisch oder entfallen.
  - Terminal, Eingabeaufforderung, Befehle eingeben, `cd`, `mkdir`: Kurzfassung in „Programmieren, Python 1, Abschnitt 3.1“
    (und 5.2), ausführlich geplant in Linux 2 (Python 1 verweist mit „Linux~2“, bisher Text ohne Link).
  - Paketverwaltung `apt` und `sudo`: in Python 1, Abschnitt 3.3 nur je ein Satz; ausführlich im Linux-Bereich
    (Heftnummer laut Linux-Lernpfad).
- **ML-Grundlagen gegen Höhere Mathematik:** Was ein HöMa-Heft vollständig erklärt (Beweise, Herleitungen), steht in den
  Grundlagen nur als Kurzfassung mit Verweis. Prüfen bei der nächsten Überarbeitung der Grundlagen.
- **Geplant (noch ohne Heft):** Grundlagen 6 Optimierung (Lernpfad T06, vor dem Gradientenabstieg); ML-Pfad ab Teil 1
  „Lernen aus Daten“ (T08).
<!-- von Hand: Ende -->

# Erklärt in (aus den Heften erzeugt, nicht von Hand ändern)

Je Zeile ein Abschnitt: Verweis-Wendung, Abschnittstitel, dann die Unterabschnitte mit Nummer.

## Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik

### Grundlagen der Elektrotechnik, Teil 1: Ladung, Feld und Potenzial (`Kap1_Feld`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 1 „Stufe 1: Größen, Kraft und Arbeit“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 2 „Stufe 2: Ladung“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 3 „Stufe 3: Die Kraft zwischen Ladungen“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 4 „Stufe 4: Die Feldstärke“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 5 „Stufe 5: Feldlinien und Leiter“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 6 „Stufe 6: Arbeit im Feld“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 7 „Stufe 7: Das Potenzial“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 8 „Stufe 8: Spannung und Masse“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 9 „Stufe 9: Was die Spannung mit einer Ladung macht“
- Grundlagen der Elektrotechnik, Teil 1, Abschnitt 10 „Stufe 10: Grenze des Bildes: Magnetismus und Induktion“

### Grundlagen der Elektrotechnik, Teil 2: Strom, Widerstand und Kirchhoff (`Kap2_Stromkreis`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 1 „Stufe 1: Strom ist bewegte Ladung“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 2 „Stufe 2: Langsame Elektronen, sofortiger Strom“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 3 „Stufe 3: Das ohmsche Gesetz aus Feld und Stößen“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 4 „Stufe 4: Reale Widerstände: Werte und Temperatur“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 5 „Stufe 5: Zweipole und Zählpfeile“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 6 „Stufe 6: Knoten, Zweige, Maschen“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 7 „Stufe 7: Die Knotenregel ist Ladungserhaltung“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 8 „Stufe 8: Die Maschenregel ist Energieerhaltung“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 9 „Stufe 9: Reihenschaltung und Spannungsteiler“
- Grundlagen der Elektrotechnik, Teil 2, Abschnitt 10 „Stufe 10: Parallelschaltung, Stromteiler und Belastung“

### Grundlagen der Elektrotechnik, Teil 3: Der Kondensator (`Kap3_Kondensator`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 1 „Stufe 1: Warum Strom in einen Isolator fließt“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 2 „Stufe 2: Die Kapazität“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 3 „Stufe 3: Strom und Spannung am Kondensator“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 4 „Stufe 4: Plattenkondensator und Dielektrikum“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 5 „Stufe 5: Bauformen und Selbstentladung“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 6 „Stufe 6: Die gespeicherte Energie“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 7 „Stufe 7: Parallel- und Reihenschaltung“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 8 „Stufe 8: Ladungserhaltung beim Umschalten“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 9 „Stufe 9: Aufladen über einen Widerstand“
- Grundlagen der Elektrotechnik, Teil 3, Abschnitt 10 „Stufe 10: Entladen und Zeitkonstante“

### Grundlagen der Elektrotechnik, Teil 4: Strom und Spannung messen (`Kap4_Messen`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 1 „Stufe 1: Das Messgerät ist ein Bauteil“
- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 2 „Stufe 2: Den Messbereich erweitern“
- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 3 „Stufe 3: Der Fehler beim Strommessen“
- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 4 „Stufe 4: Der Fehler beim Spannungsmessen“
- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 5 „Stufe 5: Strom und Spannung zugleich“
- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 6 „Stufe 6: Die Wheatstonesche Brücke“
- Grundlagen der Elektrotechnik, Teil 4, Abschnitt 7 „Stufe 7: Die verstimmte Brücke“

### Grundlagen der Elektrotechnik, Teil 5: Quellen und Ersatzquellen (`Kap5_Ersatzquellen`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 1 „Stufe 1: Widerstände zusammenfassen“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 2 „Stufe 2: Symmetrie nutzen“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 3 „Stufe 3: Stern und Dreieck“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 4 „Stufe 4: Ideale Quellen“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 5 „Stufe 5: Reale Quellen und der Arbeitspunkt“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 6 „Stufe 6: Spannungsquelle oder Stromquelle“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 7 „Stufe 7: Quellen zusammenschalten“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 8 „Stufe 8: Überlagerung“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 9 „Stufe 9: Thevenin und Norton“
- Grundlagen der Elektrotechnik, Teil 5, Abschnitt 10 „Stufe 10: Der R-2R-Wandler“

### Grundlagen der Elektrotechnik, Teil 6: Zweitore (`Kap6_Zweitore`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 1 „Stufe 1: Vom Vierpol zum Zweitor“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 2 „Stufe 2: Vier Größen, zwei Gleichungen, vier Zahlen“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 3 „Stufe 3: Impedanzform und Leerlaufversuch“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 4 „Stufe 4: Das Zweitor im Betrieb“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 5 „Stufe 5: Admittanzform und Kurzschlussversuch“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 6 „Stufe 6: Umrechnen, T und $\pi$“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 7 „Stufe 7: Hybridform“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 8 „Stufe 8: Kettenform“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 9 „Stufe 9: Zusammenschaltung“
- Grundlagen der Elektrotechnik, Teil 6, Abschnitt 10 „Stufe 10: Eigenschaften und alle Formen im Überblick“

### Grundlagen der Elektrotechnik, Teil 7: Leistung, Anpassung und Wirkungsgrad (`Kap7_Leistung`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 1 „Stufe 1: Energie je Ladung mal Ladung je Zeit“
- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 2 „Stufe 2: Warum der Widerstand warm wird“
- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 3 „Stufe 3: Mittlere Leistung bei Sinusspannung“
- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 4 „Stufe 4: Leitungsverluste“
- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 5 „Stufe 5: Wohin die Leistung einer Quelle geht“
- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 6 „Stufe 6: Leistungsanpassung“
- Grundlagen der Elektrotechnik, Teil 7, Abschnitt 7 „Stufe 7: Warum 50 %, und welches Ziel gilt“

### Grundlagen der Elektrotechnik, Teil 8: Maschenstrom- und Knotenpotentialverfahren (`Kap8_Netzwerkanalyse`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 1 „Stufe 1: Wie viele Größen sind frei?“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 2 „Stufe 2: Maschenströme erfüllen die Knotenregel“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 3 „Stufe 3: Das Maschenstromverfahren“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 4 „Stufe 4: Potenziale erfüllen die Maschenregel“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 5 „Stufe 5: Das Knotenpotentialverfahren“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 6 „Stufe 6: Welches Verfahren wann?“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 7 „Stufe 7: Stempel und Netzliste“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 8 „Stufe 8: Gesteuerte Quellen und Verstärker“
- Grundlagen der Elektrotechnik, Teil 8, Abschnitt 9 „Stufe 9: Die modifizierte Knotenanalyse“

### Grundlagen der Elektrotechnik, Teil 9: Halbleiter und Dioden (`Kap9_Dioden`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 1 „Stufe 1: Warum Silizium kaum leitet“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 2 „Stufe 2: Dotierung“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 3 „Stufe 3: Die Raumladungszone“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 4 „Stufe 4: Warum der Strom exponentiell wächst“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 5 „Stufe 5: Kennlinie, Durchbruch und Spezialdioden“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 6 „Stufe 6: Der Arbeitspunkt“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 7 „Stufe 7: Lineare Ersatzschaltungen“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 8 „Stufe 8: Kleine Änderungen um den Arbeitspunkt“
- Grundlagen der Elektrotechnik, Teil 9, Abschnitt 9 „Stufe 9: Gleichrichter und Ladungspumpe“

### Grundlagen der Elektrotechnik, Teil 10: Der Bipolartransistor (`Kap10_Bipolartransistor`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 1 „Stufe 1: Drei Schichten, zwei Spannungen“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 2 „Stufe 2: Warum Strom durch die gesperrte Diode fließt“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 3 „Stufe 3: Eine Fläche, viele Kennlinien“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 4 „Stufe 4: Drei Bereiche, drei Ersatzschaltbilder“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 5 „Stufe 5: Der Arbeitspunkt“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 6 „Stufe 6: Der Transistor als Schalter“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 7 „Stufe 7: Gegenkopplung hält den Arbeitspunkt fest“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 8 „Stufe 8: Zwei Schaltungen, die $U_\mathrm{BE}$ nutzen“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 9 „Stufe 9: Tangente statt Kurve“
- Grundlagen der Elektrotechnik, Teil 10, Abschnitt 10 „Stufe 10: Drei Grundschaltungen“

### Grundlagen der Elektrotechnik, Teil 11: Der Operationsverstärker (`Kap11_OPV`, Modul et1)

- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 1 „Stufe 1: Rauschen“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 2 „Stufe 2: Der Differenzverstärker“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 3 „Stufe 3: Der OPV ohne Rückführung“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 4 „Stufe 4: Gegenkopplung“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 5 „Stufe 5: Die Regel und die virtuelle Masse“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 6 „Stufe 6: Mehrere Eingänge, mehrere Stufen“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 7 „Stufe 7: Rechnen mit Kondensator und Diode“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 8 „Stufe 8: Strom als Signal“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 9 „Stufe 9: Mitkopplung und der Schmitt-Trigger“
- Grundlagen der Elektrotechnik, Teil 11, Abschnitt 10 „Stufe 10: Wo die Regeln enden“

## Elektrotechnik / 1. Semester / Höhere Mathematik 1

### Höhere Mathematik 1, Teil 1: Mengen, Logik und reelle Zahlen (`Kap1_Zahlen`, Modul hm1)

- Höhere Mathematik 1, Teil 1, Abschnitt 1 „Stufe 1: Mengen und Aussagen“
- Höhere Mathematik 1, Teil 1, Abschnitt 2 „Stufe 2: Quantoren und indirekter Beweis“
- Höhere Mathematik 1, Teil 1, Abschnitt 3 „Stufe 3: Körperaxiome“
- Höhere Mathematik 1, Teil 1, Abschnitt 4 „Stufe 4: Anordnungsaxiome“
- Höhere Mathematik 1, Teil 1, Abschnitt 5 „Stufe 5: Vollständige Induktion, Summe und Produkt“
- Höhere Mathematik 1, Teil 1, Abschnitt 6 „Stufe 6: Das Vollständigkeitsaxiom“
- Höhere Mathematik 1, Teil 1, Abschnitt 7 „Stufe 7: Intervallschachtelung und Wurzeln“
- Höhere Mathematik 1, Teil 1, Abschnitt 8 „Stufe 8: Abstand und Betrag“
- Höhere Mathematik 1, Teil 1, Abschnitt 9 „Stufe 9: Elementare Ungleichungen“

### Höhere Mathematik 1, Teil 2: Komplexe Zahlen (`Kap2_Komplex`, Modul hm1)

- Höhere Mathematik 1, Teil 2, Abschnitt 1 „Stufe 1: Paare statt einzelner Zahlen“
- Höhere Mathematik 1, Teil 2, Abschnitt 2 „Stufe 2: Die komplexe Ebene“
- Höhere Mathematik 1, Teil 2, Abschnitt 3 „Stufe 3: Spiegeln an der reellen Achse“
- Höhere Mathematik 1, Teil 2, Abschnitt 4 „Stufe 4: Dividieren, und was verloren geht“
- Höhere Mathematik 1, Teil 2, Abschnitt 5 „Stufe 5: Betrag und Abstand“
- Höhere Mathematik 1, Teil 2, Abschnitt 6 „Stufe 6: Quadratische Gleichungen“

### Höhere Mathematik 1, Teil 3: Funktionen und Polynome (`Kap3_Funktionen`, Modul hm1)

- Höhere Mathematik 1, Teil 3, Abschnitt 1 „Stufe 1: Was eine Funktion ist“
- Höhere Mathematik 1, Teil 3, Abschnitt 2 „Stufe 2: Gerade, monoton, beschränkt“
- Höhere Mathematik 1, Teil 3, Abschnitt 3 „Stufe 3: Rückwärts: injektiv, surjektiv, bijektiv“
- Höhere Mathematik 1, Teil 3, Abschnitt 4 „Stufe 4: Verknüpfen und Umkehren“
- Höhere Mathematik 1, Teil 3, Abschnitt 5 „Stufe 5: Polynome und Koeffizienten“
- Höhere Mathematik 1, Teil 3, Abschnitt 6 „Stufe 6: Division mit Rest“
- Höhere Mathematik 1, Teil 3, Abschnitt 7 „Stufe 7: Das Horner-Schema“
- Höhere Mathematik 1, Teil 3, Abschnitt 8 „Stufe 8: Jede Nullstelle spaltet einen Linearfaktor ab“
- Höhere Mathematik 1, Teil 3, Abschnitt 9 „Stufe 9: Rationale Funktionen und Pole“

### Höhere Mathematik 1, Teil 4: Folgen und Grenzwerte (`Kap4_Folgen`, Modul hm1)

- Höhere Mathematik 1, Teil 4, Abschnitt 1 „Stufe 1: Folgen und ihr Verlauf“
- Höhere Mathematik 1, Teil 4, Abschnitt 2 „Stufe 2: Das Epsilon-Spiel“
- Höhere Mathematik 1, Teil 4, Abschnitt 3 „Stufe 3: Nullfolgen vergleichen“
- Höhere Mathematik 1, Teil 4, Abschnitt 4 „Stufe 4: Der Grenzwert“
- Höhere Mathematik 1, Teil 4, Abschnitt 5 „Stufe 5: Rechenregeln“
- Höhere Mathematik 1, Teil 4, Abschnitt 6 „Stufe 6: Einklemmen und Divergenz“
- Höhere Mathematik 1, Teil 4, Abschnitt 7 „Stufe 7: Monotone Folgen und die Vollständigkeit“
- Höhere Mathematik 1, Teil 4, Abschnitt 8 „Stufe 8: Cauchy-Folgen und die Axiome“

### Höhere Mathematik 1, Teil 5: Exponentialfunktion und Stetigkeit (`Kap5_Stetigkeit`, Modul hm1)

- Höhere Mathematik 1, Teil 5, Abschnitt 1 „Stufe 1: Von der Zinsrechnung zur Exponentialfunktion“
- Höhere Mathematik 1, Teil 5, Abschnitt 2 „Stufe 2: Wachstum, Logarithmus, allgemeine Potenz“
- Höhere Mathematik 1, Teil 5, Abschnitt 3 „Stufe 3: Grenzwerte von Funktionen“
- Höhere Mathematik 1, Teil 5, Abschnitt 4 „Stufe 4: Stetigkeit und Epsilon-Delta“
- Höhere Mathematik 1, Teil 5, Abschnitt 5 „Stufe 5: Stetigkeit vererben“
- Höhere Mathematik 1, Teil 5, Abschnitt 6 „Stufe 6: Teilfolgen und Häufungspunkte“
- Höhere Mathematik 1, Teil 5, Abschnitt 7 „Stufe 7: Maximum, Minimum, gleichmäßige Stetigkeit“
- Höhere Mathematik 1, Teil 5, Abschnitt 8 „Stufe 8: Zwischenwerte, Nullstellen, Umkehrfunktion“

### Höhere Mathematik 1, Teil 6: Unendliche Reihen (`Kap6_Reihen`, Modul hm1)

- Höhere Mathematik 1, Teil 6, Abschnitt 1 „Stufe 1: Eine Reihe ist eine Folge“
- Höhere Mathematik 1, Teil 6, Abschnitt 2 „Stufe 2: Nullfolge nötig, aber nicht genug“
- Höhere Mathematik 1, Teil 6, Abschnitt 3 „Stufe 3: Wechselnde Vorzeichen“
- Höhere Mathematik 1, Teil 6, Abschnitt 4 „Stufe 4: Rechenregeln und Klammern“
- Höhere Mathematik 1, Teil 6, Abschnitt 5 „Stufe 5: Absolute Konvergenz und Vergleich“
- Höhere Mathematik 1, Teil 6, Abschnitt 6 „Stufe 6: Quotient und Wurzel“
- Höhere Mathematik 1, Teil 6, Abschnitt 7 „Stufe 7: Verdichten und der Entscheidungsweg“
- Höhere Mathematik 1, Teil 6, Abschnitt 8 „Stufe 8: Umordnen“

### Höhere Mathematik 1, Teil 7: Potenzreihen und Eulersche Formel (`Kap7_Potenzreihen`, Modul hm1)

- Höhere Mathematik 1, Teil 7, Abschnitt 1 „Stufe 1: Der Konvergenzkreis“
- Höhere Mathematik 1, Teil 7, Abschnitt 2 „Stufe 2: Den Radius ausrechnen“
- Höhere Mathematik 1, Teil 7, Abschnitt 3 „Stufe 3: Sinus und Cosinus als Reihen“
- Höhere Mathematik 1, Teil 7, Abschnitt 4 „Stufe 4: Reihen multiplizieren“
- Höhere Mathematik 1, Teil 7, Abschnitt 5 „Stufe 5: Die Exponentialreihe, reell und komplex“
- Höhere Mathematik 1, Teil 7, Abschnitt 6 „Stufe 6: Die Eulersche Formel“
- Höhere Mathematik 1, Teil 7, Abschnitt 7 „Stufe 7: Die Zahl $\pi$ und die Wertetabelle“
- Höhere Mathematik 1, Teil 7, Abschnitt 8 „Stufe 8: Polardarstellung, Drehen und Strecken“
- Höhere Mathematik 1, Teil 7, Abschnitt 9 „Stufe 9: Die $n$-ten Wurzeln“

### Höhere Mathematik 1, Teil 8: Vektoren und Skalarprodukt (`Kap8_Vektoren`, Modul hm1)

- Höhere Mathematik 1, Teil 8, Abschnitt 1 „Stufe 1: Pfeile addieren und strecken“
- Höhere Mathematik 1, Teil 8, Abschnitt 2 „Stufe 2: Der Vektorraum“
- Höhere Mathematik 1, Teil 8, Abschnitt 3 „Stufe 3: Unterraum und Linearkombination“
- Höhere Mathematik 1, Teil 8, Abschnitt 4 „Stufe 4: Lineare Unabhängigkeit“
- Höhere Mathematik 1, Teil 8, Abschnitt 5 „Stufe 5: Skalarprodukt, Norm, Abstand“
- Höhere Mathematik 1, Teil 8, Abschnitt 6 „Stufe 6: Projektion und Abstand zur Geraden“
- Höhere Mathematik 1, Teil 8, Abschnitt 7 „Stufe 7: Winkel, Cauchy-Schwarz, Parallelogramm“
- Höhere Mathematik 1, Teil 8, Abschnitt 8 „Stufe 8: Kugel, Hyperebene, drei geometrische Probleme“

### Höhere Mathematik 1, Teil 9: Vektorprodukt und Basen (`Kap9_Basen`, Modul hm1)

- Höhere Mathematik 1, Teil 9, Abschnitt 1 „Stufe 1: Das Vektorprodukt“
- Höhere Mathematik 1, Teil 9, Abschnitt 2 „Stufe 2: Rechenregeln und Geometrie im Raum“
- Höhere Mathematik 1, Teil 9, Abschnitt 3 „Stufe 3: Spatprodukt und Volumen“
- Höhere Mathematik 1, Teil 9, Abschnitt 4 „Stufe 4: Orthonormalsysteme und Projektion“
- Höhere Mathematik 1, Teil 9, Abschnitt 5 „Stufe 5: Die Basis“
- Höhere Mathematik 1, Teil 9, Abschnitt 6 „Stufe 6: Die Dimension“
- Höhere Mathematik 1, Teil 9, Abschnitt 7 „Stufe 7: Orthonormalbasis und Gram-Schmidt“
- Höhere Mathematik 1, Teil 9, Abschnitt 8 „Stufe 8: Skalarprodukträume“

### Höhere Mathematik 1, Teil 10: Matrizen und lineare Gleichungssysteme (`Kap10_Matrizen`, Modul hm1)

- Höhere Mathematik 1, Teil 10, Abschnitt 1 „Stufe 1: Lineare Abbildungen“
- Höhere Mathematik 1, Teil 10, Abschnitt 2 „Stufe 2: Die Spalten sind die Bilder“
- Höhere Mathematik 1, Teil 10, Abschnitt 3 „Stufe 3: Kern, Bild und die Bilanz der Dimensionen“
- Höhere Mathematik 1, Teil 10, Abschnitt 4 „Stufe 4: Koordinaten und Darstellungsmatrix“
- Höhere Mathematik 1, Teil 10, Abschnitt 5 „Stufe 5: Hintereinanderausführen ist Multiplizieren“
- Höhere Mathematik 1, Teil 10, Abschnitt 6 „Stufe 6: Gleichungssysteme fragen rückwärts“
- Höhere Mathematik 1, Teil 10, Abschnitt 7 „Stufe 7: Der Gauß-Algorithmus“
- Höhere Mathematik 1, Teil 10, Abschnitt 8 „Stufe 8: Rang und Inverse“

## Elektrotechnik / 3. Semester / Höhere Mathematik 3

### Höhere Mathematik 3, Teil 1: Differentialrechnung für Vektorfelder (`Kap1_Vektorfelder`, Modul hm3)

- Höhere Mathematik 3, Teil 1, Abschnitt 1 „Differenzierbarkeit und Kettenregel für Abbildungen“: 1.1 Was du dafür brauchst: Vektoren im $\mathbb{R}^n$ · 1.2 Was du dafür brauchst: das Skalarprodukt · 1.3 Was du dafür brauchst: Matrizen und Matrixprodukt · 1.4 Was du dafür brauchst: Transponieren und symmetrische Matrizen · 1.5 Was du dafür brauchst: Funktionen mehrerer Variablen · 1.6 Was du dafür brauchst: Grenzwert und Stetigkeit in mehreren Variablen · 1.7 Was du dafür brauchst: Partielle Ableitungen · 1.8 Was du dafür brauchst: Höhere partielle Ableitungen · 1.9 Was du dafür brauchst: Offene Mengen · 1.10 Abbildungen mit mehreren Ausgängen · 1.11 Vektorfelder · 1.12 Die Jacobi-Matrix · 1.13 Der Gradient · 1.14 Das Nabla-Symbol · 1.15 Gradient und Jacobi-Matrix: Spalte und Zeile · 1.16 Differentialoperatoren · 1.17 Totale Differenzierbarkeit · 1.18 Die Tangentialebene · 1.19 Partielle Ableitungen allein reichen nicht · 1.20 Stetig differenzierbar · 1.21 Mehrfach stetig differenzierbar · 1.22 Das Lemma von Schwarz · 1.23 Gradientenfelder und Skalarpotentiale · 1.24 Die Jacobi-Matrix eines Gradientenfelds ist symmetrisch · 1.25 Die Kettenregel · 1.26 Kurven · 1.27 Die Ableitung längs einer Kurve · 1.28 Die Richtungsableitung · 1.29 Wohin der Gradient zeigt · 1.30 Feldlinien · 1.31 Potentialfelder in der Physik · 1.32 Aufgaben
- Höhere Mathematik 3, Teil 1, Abschnitt 2 „Radialsymmetrische Funktionen und Felder“: 2.1 Was du dafür brauchst: Stammfunktionen · 2.2 Was du dafür brauchst: Kugelflächen · 2.3 Radialsymmetrische Funktionen · 2.4 Der radiale Einheitsvektor · 2.5 Der Gradient einer radialsymmetrischen Funktion · 2.6 Das Coulomb-Potential · 2.7 Zentralfelder · 2.8 Radialsymmetrische Vektorfelder · 2.9 Radialsymmetrische Vektorfelder sind Gradientenfelder · 2.10 Welche Zentralfelder Gradientenfelder sind · 2.11 Aufgaben
- Höhere Mathematik 3, Teil 1, Abschnitt 3 „Divergenz, Rotation und Laplace-Operator“: 3.1 Was du dafür brauchst: das Kreuzprodukt · 3.2 Was du dafür brauchst: Determinanten · 3.3 Was du dafür brauchst: die Spur einer Matrix · 3.4 Was du dafür brauchst: schiefsymmetrische Matrizen · 3.5 Die Divergenz · 3.6 Die Divergenz eines Gradientenfelds · 3.7 Der Laplace-Operator · 3.8 Harmonische Funktionen · 3.9 Die Produktregel der Divergenz · 3.10 Die Divergenz radialsymmetrischer Felder · 3.11 Das Coulomb-Potential ist harmonisch · 3.12 Die Rotation im Raum · 3.13 Levi-Civita-Symbole · 3.14 Die Rotation als Determinante · 3.15 Die Rotation in der Ebene · 3.16 Drehen um einen rechten Winkel vertauscht Divergenz und Rotation · 3.17 Eine Rotation für jede Dimension · 3.18 Die Integrabilitätsbedingungen · 3.19 Notwendig, aber nicht hinreichend · 3.20 Ein Skalarpotential ausrechnen · 3.21 Aufgaben
- Höhere Mathematik 3, Teil 1, Abschnitt 4 „Rechenregeln und Identitäten für Divergenz und Rotation“: 4.1 Was du dafür brauchst: das Kronecker-Symbol · 4.2 Was du dafür brauchst: das Spatprodukt · 4.3 Was du dafür brauchst: die Graßmann-Identität · 4.4 Rechnen mit dem Nabla-Symbol · 4.5 Produktregeln mit einer skalaren Funktion · 4.6 Die Produktregel der Rotation in der Ebene · 4.7 Die Ableitung eines Felds in Richtung eines anderen Felds · 4.8 Produktregeln mit dem Kreuzprodukt · 4.9 Rotationsfelder sind divergenzfrei · 4.10 Die doppelte Rotation · 4.11 Wirbelfelder und Vektorpotentiale · 4.12 Eichfreiheit · 4.13 Die Coulomb-Eichung · 4.14 Aufgaben

### Höhere Mathematik 3, Teil 2: Integralrechnung im Rⁿ (`Kap2_Integrale`, Modul hm3)

- Höhere Mathematik 3, Teil 2, Abschnitt 1 „Integrale mit Parameter über endlichen Intervallen“: 1.1 Was du dafür brauchst: das bestimmte Integral · 1.2 Was du dafür brauchst: der Hauptsatz · 1.3 Was du dafür brauchst: der Mittelwertsatz · 1.4 Was du dafür brauchst: abgeschlossene, beschränkte und kompakte Mengen · 1.5 Was du dafür brauchst: Stetigkeit mit $\varepsilon$ und $\delta$ · 1.6 Was du dafür brauchst: gleichmäßige Stetigkeit · 1.7 Das Parameterintegral · 1.8 Die Stetigkeit des Parameterintegrals · 1.9 Ableiten unter dem Integralzeichen · 1.10 Parameter aus einem abgeschlossenen Intervall · 1.11 Grenzen, die vom Parameter abhängen: die Leibnizregel · 1.12 Aufgaben
- Höhere Mathematik 3, Teil 2, Abschnitt 2 „Uneigentliche Parameterintegrale“: 2.1 Was du dafür brauchst: Supremum und Maximum · 2.2 Was du dafür brauchst: uneigentliche Integrale · 2.3 Was du dafür brauchst: absolute Konvergenz und Vergleich · 2.4 Was du dafür brauchst: die Substitutionsregel · 2.5 Was du dafür brauchst: Integrale komplexer Funktionen · 2.6 Das uneigentliche Parameterintegral · 2.7 Ein stetiger Integrand mit unstetigem Integral · 2.8 Gleichmäßige Konvergenz · 2.9 Majorante und Majorantenkriterium · 2.10 Die Fourier-Transformation · 2.11 Lokale Majoranten · 2.12 Die Gamma-Funktion · 2.13 Die Laplace-Transformation · 2.14 Aufgaben
- Höhere Mathematik 3, Teil 2, Abschnitt 3 „Mehrfachintegrale“: 3.1 Was du dafür brauchst: Quader · 3.2 Was du dafür brauchst: der Abschluss einer Menge · 3.3 Das iterierte Integral · 3.4 Der Satz von Fubini · 3.5 Das Mehrfachintegral · 3.6 Linearität und Monotonie · 3.7 Funktionen mit kompaktem Träger · 3.8 Über stetige Funktionen hinaus: das Lebesgue-Integral · 3.9 Aufgaben
- Höhere Mathematik 3, Teil 2, Abschnitt 4 „Integration über Mengen und Berechnung von Volumina“: 4.1 Das Integral über eine Menge · 4.2 Volumen und Flächeninhalt · 4.3 Das Prinzip von Cavalieri · 4.4 Aufgaben
- Höhere Mathematik 3, Teil 2, Abschnitt 5 „Integration über Normalbereiche“: 5.1 Normalbereiche · 5.2 Integration über Normalbereiche · 5.3 Zerlegung in reguläre Normalbereiche · 5.4 Räumliche Normalbereiche · 5.5 Aufgaben

### Höhere Mathematik 3, Teil 3: Kurvenintegrale (`Kap3_Kurvenintegrale`, Modul hm3)

- Höhere Mathematik 3, Teil 3, Abschnitt 1 „Integration längs regulärer Kurven“: 1.1 Was du dafür brauchst: Kurven und einseitige Ableitungen · 1.2 Was du dafür brauchst: streng monotone Funktionen und Umkehrfunktionen · 1.3 Was du dafür brauchst: die Cauchy-Schwarz-Ungleichung · 1.4 Stückweise stetig differenzierbare Kurven · 1.5 Reguläre Parametrisierung · 1.6 Geschlossene Kurven · 1.7 Einfache Kurven · 1.8 Das Kurvenintegral · 1.9 Linearität · 1.10 Umparametrisierung und Parameterinvarianz · 1.11 Entgegengesetzt durchlaufene Kurven · 1.12 Spur, reguläre Kurve und Orientierung · 1.13 Der Anfangspunkt einer geschlossenen Kurve · 1.14 Zusammengesetzte Kurven · 1.15 Linienelement und Einheitstangentenvektor · 1.16 Die Kurvenlänge · 1.17 Parametrisierung nach der Bogenlänge · 1.18 Die Standardabschätzung · 1.19 Aufgaben
- Höhere Mathematik 3, Teil 3, Abschnitt 2 „Erster Hauptsatz für Kurvenintegrale“: 2.1 Was du dafür brauchst: der Mittelwertsatz der Integralrechnung · 2.2 Gebiete · 2.3 Wegunabhängige Kurvenintegrale und konservative Felder · 2.4 Rundwege · 2.5 Der erste Hauptsatz · 2.6 Arbeit und Spannung in konservativen Feldern · 2.7 Konservative Felder sind rotationsfrei · 2.8 Ein rotationsfreies Feld, das nicht konservativ ist · 2.9 Aufgaben

### Höhere Mathematik 3, Teil 4: Koordinatentransformationen (`Kap4_Koordinaten`, Modul hm3)

- Höhere Mathematik 3, Teil 4, Abschnitt 1 „Stufe 1: Der Transformationssatz“
- Höhere Mathematik 3, Teil 4, Abschnitt 2 „Stufe 2: Der Beweis in der Ebene“
- Höhere Mathematik 3, Teil 4, Abschnitt 3 „Stufe 3: Polarkoordinaten“
- Höhere Mathematik 3, Teil 4, Abschnitt 4 „Stufe 4: Zylinder- und Kugelkoordinaten“
- Höhere Mathematik 3, Teil 4, Abschnitt 5 „Stufe 5: Integrale über eine Singularität“
- Höhere Mathematik 3, Teil 4, Abschnitt 6 „Stufe 6: Das Newtonpotential“
- Höhere Mathematik 3, Teil 4, Abschnitt 7 „Stufe 7: Krummlinige Koordinaten und der Gradient“
- Höhere Mathematik 3, Teil 4, Abschnitt 8 „Stufe 8: Divergenz und Laplace-Operator“

### Höhere Mathematik 3, Teil 5: Integralsätze im Raum (`Kap5_Integralsaetze`, Modul hm3)

- Höhere Mathematik 3, Teil 5, Abschnitt 1 „Stufe 1: Flächen beschreiben“
- Höhere Mathematik 3, Teil 5, Abschnitt 2 „Stufe 2: Das Oberflächenelement“
- Höhere Mathematik 3, Teil 5, Abschnitt 3 „Stufe 3: Drei Standardfälle“
- Höhere Mathematik 3, Teil 5, Abschnitt 4 „Stufe 4: Orientierung und Flussintegral“
- Höhere Mathematik 3, Teil 5, Abschnitt 5 „Stufe 5: Warum die Parametrisierung egal ist“
- Höhere Mathematik 3, Teil 5, Abschnitt 6 „Stufe 6: Der Satz von Stokes“
- Höhere Mathematik 3, Teil 5, Abschnitt 7 „Stufe 7: Wann ein Feld eine Rotation ist“
- Höhere Mathematik 3, Teil 5, Abschnitt 8 „Stufe 8: Der Satz von Gauß“
- Höhere Mathematik 3, Teil 5, Abschnitt 9 „Stufe 9: Poisson-Gleichung“
- Höhere Mathematik 3, Teil 5, Abschnitt 10 „Stufe 10: Der Hauptsatz der Vektoranalysis“

### Höhere Mathematik 3, Teil 6: Konvergenz von Funktionenfolgen (`Kap6_Funktionenfolgen`, Modul hm3)

- Höhere Mathematik 3, Teil 6, Abschnitt 1 „Stufe 1: Punktweise Konvergenz“
- Höhere Mathematik 3, Teil 6, Abschnitt 2 „Stufe 2: Gleichmäßige Konvergenz“
- Höhere Mathematik 3, Teil 6, Abschnitt 3 „Stufe 3: Stetigkeit und Integral bleiben erhalten“
- Höhere Mathematik 3, Teil 6, Abschnitt 4 „Stufe 4: Die Ableitung braucht mehr“
- Höhere Mathematik 3, Teil 6, Abschnitt 5 „Stufe 5: Funktionenreihen und der M-Test“
- Höhere Mathematik 3, Teil 6, Abschnitt 6 „Stufe 6: Potenzreihen“
- Höhere Mathematik 3, Teil 6, Abschnitt 7 „Stufe 7: Funktionen als Punkte eines Raums“
- Höhere Mathematik 3, Teil 6, Abschnitt 8 „Stufe 8: Konvergenz im quadratischen Mittel“

### Höhere Mathematik 3, Teil 7: Fourier-Reihen (`Kap7_Fourier`, Modul hm3)

- Höhere Mathematik 3, Teil 7, Abschnitt 1 „Stufe 1: Schwingungen als Bausteine“
- Höhere Mathematik 3, Teil 7, Abschnitt 2 „Stufe 2: Koeffizienten und Polynome“
- Höhere Mathematik 3, Teil 7, Abschnitt 3 „Stufe 3: Rechenregeln“
- Höhere Mathematik 3, Teil 7, Abschnitt 4 „Stufe 4: Der Sägezahn zu Fuß“
- Höhere Mathematik 3, Teil 7, Abschnitt 5 „Stufe 5: Die beste Näherung“
- Höhere Mathematik 3, Teil 7, Abschnitt 6 „Stufe 6: Konvergenz im quadratischen Mittel“
- Höhere Mathematik 3, Teil 7, Abschnitt 7 „Stufe 7: Mitteln mit Dirac-Scharen“
- Höhere Mathematik 3, Teil 7, Abschnitt 8 „Stufe 8: Punktweise Konvergenz“
- Höhere Mathematik 3, Teil 7, Abschnitt 9 „Stufe 9: Gleichmäßige Konvergenz und Glattheit“
- Höhere Mathematik 3, Teil 7, Abschnitt 10 „Stufe 10: Das Dirichlet-Problem“

### Höhere Mathematik 3, Teil 8: Wahrscheinlichkeitsrechnung (`Kap8_Wahrscheinlichkeit`, Modul hm3)

- Höhere Mathematik 3, Teil 8, Abschnitt 1 „Stufe 1: Ereignisse und Wahrscheinlichkeit“
- Höhere Mathematik 3, Teil 8, Abschnitt 2 „Stufe 2: Zählen“
- Höhere Mathematik 3, Teil 8, Abschnitt 3 „Stufe 3: Zusatzwissen, Unabhängigkeit und Bayes“
- Höhere Mathematik 3, Teil 8, Abschnitt 4 „Stufe 4: Zufallsvariablen und Verteilungsfunktion“
- Höhere Mathematik 3, Teil 8, Abschnitt 5 „Stufe 5: Drei diskrete Verteilungen“
- Höhere Mathematik 3, Teil 8, Abschnitt 6 „Stufe 6: Dichten“
- Höhere Mathematik 3, Teil 8, Abschnitt 7 „Stufe 7: Der Erwartungswert“
- Höhere Mathematik 3, Teil 8, Abschnitt 8 „Stufe 8: Varianz, Kovarianz und Tschebyschew“
- Höhere Mathematik 3, Teil 8, Abschnitt 9 „Stufe 9: Unabhängige Zufallsvariablen“
- Höhere Mathematik 3, Teil 8, Abschnitt 10 „Stufe 10: Zufallsvektoren mit Dichte“
- Höhere Mathematik 3, Teil 8, Abschnitt 11 „Stufe 11: Das Gesetz der großen Zahlen“
- Höhere Mathematik 3, Teil 8, Abschnitt 12 „Stufe 12: Der zentrale Grenzwertsatz“

## Elektrotechnik / 3. Semester / Signale und Systeme

### Signale und Systeme, Teil 1: LTI-Systeme und Faltung (`Kap1_Faltung`, Modul et3)

- Signale und Systeme, Teil 1, Abschnitt 1 „Stufe 1: Signale beschreiben“
- Signale und Systeme, Teil 1, Abschnitt 2 „Stufe 2: Ein erstes System, das RC-Glied“
- Signale und Systeme, Teil 1, Abschnitt 3 „Stufe 3: Was ein LTI-System ist“
- Signale und Systeme, Teil 1, Abschnitt 4 „Stufe 4: Das Faltungsintegral“
- Signale und Systeme, Teil 1, Abschnitt 5 „Stufe 5: Die Faltung ausrechnen“
- Signale und Systeme, Teil 1, Abschnitt 6 „Stufe 6: Rechenregeln der Faltung“
- Signale und Systeme, Teil 1, Abschnitt 7 „Stufe 7: Der Dirac-Impuls“
- Signale und Systeme, Teil 1, Abschnitt 8 „Stufe 8: Integrieren und Differenzieren“
- Signale und Systeme, Teil 1, Abschnitt 9 „Stufe 9: Kausal und stabil“
- Signale und Systeme, Teil 1, Abschnitt 10 „Stufe 10: Faltung ganz ohne System“

### Signale und Systeme, Teil 2: Laplace-Transformation (`Kap2_Laplace`, Modul et3)

- Signale und Systeme, Teil 2, Abschnitt 1 „Eigenfunktionen von LTI-Systemen“: 1.1 Was du dafür brauchst: die komplexe Exponentialfunktion · 1.2 Rückblick: die Antwort eines LTI-Systems · 1.3 Eigenfunktion und Eigenwert · 1.4 Die Exponentialfunktion $\mathrm{e}^{pt}$ als Eigenfunktion · 1.5 Die komplexe Frequenz und die $p$-Ebene · 1.6 Die Laplace-Übertragungsfunktion · 1.7 Zwei Systeme in Kette · 1.8 Die Laplace-Transformation eines Signals · 1.9 Die einseitige Laplace-Transformation
- Signale und Systeme, Teil 2, Abschnitt 2 „Beispiele zur Laplace-Transformation“: 2.1 Der rechtsseitige Exponentialimpuls · 2.2 Der Konvergenzbereich · 2.3 Der linksseitige Exponentialimpuls · 2.4 Summen von Signalen · 2.5 Der zweiseitige Exponentialimpuls · 2.6 Polstellen · 2.7 Eine Summe aus drei Exponentialimpulsen · 2.8 Die Grundpaare
- Signale und Systeme, Teil 2, Abschnitt 3 „Pole und Nullstellen in der $p$-Ebene“: 3.1 Nullstellen · 3.2 Die Produktform · 3.3 Das Pol-Nullstellen-Diagramm · 3.4 Wo der Konvergenzbereich liegt · 3.5 Faltung wird Multiplikation · 3.6 Ableiten im Zeitbereich · 3.7 Integrieren im Zeitbereich · 3.8 Der Dirac-Impuls
- Signale und Systeme, Teil 2, Abschnitt 4 „Lösung von Differentialgleichungen“: 4.1 Lineare Differentialgleichungen mit konstanten Koeffizienten · 4.2 Die Gleichung im Bildbereich · 4.3 Die Übertragungsfunktion als Polynombruch · 4.4 Beispiel: das RLC-System · 4.5 Partialbruchzerlegung · 4.6 Zurück in den Zeitbereich · 4.7 Die Impulsantwort des RLC-Systems · 4.8 Konjugiert komplexe Polpaare · 4.9 Mehrfache Pole
- Signale und Systeme, Teil 2, Abschnitt 5 „Stabilität“: 5.1 Rückblick: Stabilität im Zeitbereich · 5.2 Die Bedingung in der $p$-Ebene · 5.3 Beispiel: ein wachsender Exponentialimpuls · 5.4 Beispiel: ein System zweiter Ordnung
- Signale und Systeme, Teil 2, Abschnitt 6 „Systemanalyse und -synthese“: 6.1 Rückkopplung · 6.2 Grundbausteine · 6.3 Ein System erster Ordnung aus Grundbausteinen · 6.4 Drei Aufbauten eines Systems zweiter Ordnung · 6.5 Die direkte Form · 6.6 Bauelemente im Bildbereich · 6.7 Ein System aus Messungen bestimmen
- Signale und Systeme, Teil 2, Abschnitt 7 „Tabellen und Umkehrformel“: 7.1 Rechenregeln · 7.2 Transformationspaare · 7.3 Die Umkehrformel

### Signale und Systeme, Teil 3: Fourier-Reihe und -Transformation (`Kap3_Fourier`, Modul et3)

- Signale und Systeme, Teil 3, Abschnitt 1 „Stufe 1: Schwingungen als Eigenfunktionen“
- Signale und Systeme, Teil 3, Abschnitt 2 „Stufe 2: Periodische Signale, die Fourier-Reihe“
- Signale und Systeme, Teil 3, Abschnitt 3 „Stufe 3: Leistung, Konvergenz und LTI-Systeme“
- Signale und Systeme, Teil 3, Abschnitt 4 „Stufe 4: Vom periodischen zum einmaligen Signal“
- Signale und Systeme, Teil 3, Abschnitt 5 „Stufe 5: Symmetrien im Signal und im Spektrum“
- Signale und Systeme, Teil 3, Abschnitt 6 „Stufe 6: Die Rechenregeln (Theoreme)“
- Signale und Systeme, Teil 3, Abschnitt 7 „Stufe 7: Rechteck, si-Funktion und Dreieck“
- Signale und Systeme, Teil 3, Abschnitt 8 „Stufe 8: Singuläre Signale und Linienspektren“
- Signale und Systeme, Teil 3, Abschnitt 9 „Stufe 9: Hilbert-Transformation und analytisches Signal“
- Signale und Systeme, Teil 3, Abschnitt 10 „Stufe 10: Kurzzeit-Fourier-Transformation“
- Signale und Systeme, Teil 3, Abschnitt 11 „Stufe 11: Fourier und Laplace, Grenzen der Existenz“

### Signale und Systeme, Teil 4: Abtastung und zeitdiskrete Systeme (`Kap4_Diskret`, Modul et3)

- Signale und Systeme, Teil 4, Abschnitt 1 „Stufe 1: Signalklassen und ideale Abtastung“
- Signale und Systeme, Teil 4, Abschnitt 2 „Stufe 2: Das Spektrum des abgetasteten Signals“
- Signale und Systeme, Teil 4, Abschnitt 3 „Stufe 3: Abtasttheorem und Rückgewinnung“
- Signale und Systeme, Teil 4, Abschnitt 4 „Stufe 4: Abtastung im Frequenzbereich“
- Signale und Systeme, Teil 4, Abschnitt 5 „Stufe 5: Zeitdiskrete Signale und die diskrete Faltung“
- Signale und Systeme, Teil 4, Abschnitt 6 „Stufe 6: Ein rekursives System“
- Signale und Systeme, Teil 4, Abschnitt 7 „Stufe 7: Fourier-Transformation zeitdiskreter Signale“
- Signale und Systeme, Teil 4, Abschnitt 8 „Stufe 8: Die diskrete Fourier-Transformation (DFT)“
- Signale und Systeme, Teil 4, Abschnitt 9 „Stufe 9: FFT und schnelle Faltung“
- Signale und Systeme, Teil 4, Abschnitt 10 „Stufe 10: Abtastrate ändern, Dezimation und Interpolation“
- Signale und Systeme, Teil 4, Abschnitt 11 „Stufe 11: Die z-Transformation“

### Signale und Systeme, Teil 5: Tiefpass- und Bandpasssysteme (`Kap5_Tiefpass`, Modul et3)

- Signale und Systeme, Teil 5, Abschnitt 1 „Stufe 1: Das verzerrungsfreie System“
- Signale und Systeme, Teil 5, Abschnitt 2 „Stufe 2: Der ideale Tiefpass“
- Signale und Systeme, Teil 5, Abschnitt 3 „Stufe 3: Sprungantwort und Einschwingzeit“
- Signale und Systeme, Teil 5, Abschnitt 4 „Stufe 4: Kausale Näherung“
- Signale und Systeme, Teil 5, Abschnitt 5 „Stufe 5: Echomethode und Pulsformfilter“
- Signale und Systeme, Teil 5, Abschnitt 6 „Stufe 6: Zeitdiskrete Tiefpässe, Entwurf mit Fenstern“
- Signale und Systeme, Teil 5, Abschnitt 7 „Stufe 7: Der ideale Bandpass und sein äquivalenter Tiefpass“
- Signale und Systeme, Teil 5, Abschnitt 8 „Stufe 8: Komplexe Hüllkurve und Quadraturkomponenten“
- Signale und Systeme, Teil 5, Abschnitt 9 „Stufe 9: Bandpasssignal durch Bandpasssystem“
- Signale und Systeme, Teil 5, Abschnitt 10 „Stufe 10: Quadraturschaltung und Bandpass-Abtastung“
- Signale und Systeme, Teil 5, Abschnitt 11 „Stufe 11: Phasen- und Gruppenlaufzeit beim Bandpass“
- Signale und Systeme, Teil 5, Abschnitt 12 „Stufe 12: Zeitdiskrete Bandpässe und Hochpässe“

### Signale und Systeme, Teil 6: Korrelationsfunktionen (`Kap6_Korrelation`, Modul et3)

- Signale und Systeme, Teil 6, Abschnitt 1 „Stufe 1: Energie und Leistung“
- Signale und Systeme, Teil 6, Abschnitt 2 „Stufe 2: Ähnlichkeit messen, der Korrelationskoeffizient“
- Signale und Systeme, Teil 6, Abschnitt 3 „Stufe 3: Korrelationsfunktion und Korrelationsprodukt“
- Signale und Systeme, Teil 6, Abschnitt 4 „Stufe 4: Energiedichtespektrum“
- Signale und Systeme, Teil 6, Abschnitt 5 „Stufe 5: Korrelation und LTI-Systeme“
- Signale und Systeme, Teil 6, Abschnitt 6 „Stufe 6: Korrelation von Bandpasssignalen“
- Signale und Systeme, Teil 6, Abschnitt 7 „Stufe 7: Zeitdiskrete und periodische Korrelation“

### Signale und Systeme, Teil 7: Zufallssignale (`Kap7_Statistik`, Modul et3)

- Signale und Systeme, Teil 7, Abschnitt 1 „Stufe 1: Der Zufallsprozess“
- Signale und Systeme, Teil 7, Abschnitt 2 „Stufe 2: Stationarität und Ergodizität“
- Signale und Systeme, Teil 7, Abschnitt 3 „Stufe 3: Mittelwert, Leistung, Varianz“
- Signale und Systeme, Teil 7, Abschnitt 4 „Stufe 4: Autokorrelation, Kovarianz und Kreuzkorrelation“
- Signale und Systeme, Teil 7, Abschnitt 5 „Stufe 5: Verteilungsfunktion und Verteilungsdichte“
- Signale und Systeme, Teil 7, Abschnitt 6 „Stufe 6: Verbundverteilung, Unabhängigkeit, Unkorreliertheit“
- Signale und Systeme, Teil 7, Abschnitt 7 „Stufe 7: Die Gauß-Verteilung“
- Signale und Systeme, Teil 7, Abschnitt 8 „Stufe 8: Zufallssignale in LTI-Systemen, Leistungsdichte“
- Signale und Systeme, Teil 7, Abschnitt 9 „Stufe 9: Weißes Rauschen und thermisches Rauschen“
- Signale und Systeme, Teil 7, Abschnitt 10 „Stufe 10: Das Korrelationsfilter (Matched Filter)“
- Signale und Systeme, Teil 7, Abschnitt 11 „Stufe 11: Fehlerwahrscheinlichkeit beim Binärempfang“
- Signale und Systeme, Teil 7, Abschnitt 12 „Stufe 12: Zeitdiskrete Zufallssignale“

### Signale und Systeme, Teil 8: Orthogonalentwicklung und Leitungen (`Kap8_Zusatz`, Modul et3)

- Signale und Systeme, Teil 8, Abschnitt 1 „Stufe 1: Signale als Vektoren, die Orthogonalentwicklung“
- Signale und Systeme, Teil 8, Abschnitt 2 „Stufe 2: Die Leitungsgleichungen“
- Signale und Systeme, Teil 8, Abschnitt 3 „Stufe 3: Wellen bei sinusförmiger Anregung“
- Signale und Systeme, Teil 8, Abschnitt 4 „Stufe 4: Die verlustlose Leitung“

## Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1

### Elektronische Materialien und Bauelemente 1, Teil 1: Welle, Teilchen und Schrödinger-Gleichung (`Kap1_Schroedinger`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 1 „Stufe 1: Elektronen als Gas“
- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 2 „Stufe 2: Teilchen und Wellen“
- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 3 „Stufe 3: Die Wellenfunktion und ihre Deutung“
- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 4 „Stufe 4: Die Schrödinger-Gleichung“
- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 5 „Stufe 5: Freies Elektron, ebene Welle, Dispersion“
- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 6 „Stufe 6: Das Wellenpaket“
- Elektronische Materialien und Bauelemente 1, Teil 1, Abschnitt 7 „Stufe 7: Was die Parabel verrät“

### Elektronische Materialien und Bauelemente 1, Teil 2: Das Teilchen in der Box (`Kap2_Box`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 1 „Stufe 1: Die Schrödinger-Gleichung auf einem Gitter“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 2 „Stufe 2: Das Kosinus-Band“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 3 „Stufe 3: Das Elektron zwischen zwei Wänden“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 4 „Stufe 4: Die Box in der Ebene“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 5 „Stufe 5: Gleiche Energie, verschiedene Zustände“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 6 „Stufe 6: Die Box im Raum“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 7 „Stufe 7: Ergänzung: Quantenfilm, Draht und Punkt“
- Elektronische Materialien und Bauelemente 1, Teil 2, Abschnitt 8 „Stufe 8: Ergänzung: Zustandsdichten in Potentialkästen“

### Elektronische Materialien und Bauelemente 1, Teil 3: Stufe, Barriere und Tunneleffekt (`Kap3_Tunnel`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 1 „Stufe 1: Zwei Gebiete an einer Kante zusammensetzen“
- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 2 „Stufe 2: Reflexion trotz genügender Energie“
- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 3 „Stufe 3: Die Welle dringt in die Wand ein“
- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 4 „Stufe 4: Tunneln durch eine dünne Wand“
- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 5 „Stufe 5: Die dicke Barriere“
- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 6 „Stufe 6: Die Box mit endlich hohen Wänden“
- Elektronische Materialien und Bauelemente 1, Teil 3, Abschnitt 7 „Stufe 7: Ergänzung: Scharfe Stufen und Nachweise“

### Elektronische Materialien und Bauelemente 1, Teil 4: Atome und Orbitale (`Kap4_Atome`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 1 „Stufe 1: Der Kern als Kasten ohne Wände“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 2 „Stufe 2: Das Wasserstoffatom“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 3 „Stufe 3: Drei Quantenzahlen“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 4 „Stufe 4: Die Formen der Orbitale“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 5 „Stufe 5: Spin und Pauli-Prinzip“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 6 „Stufe 6: Besetzung der Orbitale und Hundsche Regel“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 7 „Stufe 7: Ergänzung: Das Periodensystem der Elemente“
- Elektronische Materialien und Bauelemente 1, Teil 4, Abschnitt 8 „Stufe 8: Ergänzung: Elektronegativität und Valenz“

### Elektronische Materialien und Bauelemente 1, Teil 5: Chemische Bindung (`Kap5_Bindung`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 1 „Stufe 1: Die Energiekurve der Bindung“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 2 „Stufe 2: Ionische Bindung“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 3 „Stufe 3: Zwei Atome teilen Elektronen“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 4 „Stufe 4: Richtung und Vorzeichen der Orbitale“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 5 „Stufe 5: Hybridisierung im Tetraeder“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 6 „Stufe 6: Mehrfachbindungen und bewegliche Elektronen“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 7 „Stufe 7: Metallische Bindung“
- Elektronische Materialien und Bauelemente 1, Teil 5, Abschnitt 8 „Stufe 8: Dipol-Bindungen und reale Materialien“

### Elektronische Materialien und Bauelemente 1, Teil 6: Kristallgitter (`Kap6_Kristall`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 1 „Stufe 1: Punktgitter und Basis“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 2 „Stufe 2: Bravais-Gitter in einer und zwei Dimensionen“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 3 „Stufe 3: Die Wigner-Seitz-Zelle“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 4 „Stufe 4: Drei Dimensionen“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 5 „Stufe 5: Koordinationszahl und Packungsdichte“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 6 „Stufe 6: Punkte, Ebenen und Richtungen“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 7 „Stufe 7: Beispiele für Kristallstrukturen“
- Elektronische Materialien und Bauelemente 1, Teil 6, Abschnitt 8 „Stufe 8: Ergänzung: Ionenkristalle und Modifikationen“

### Elektronische Materialien und Bauelemente 1, Teil 7: Kristallwachstum und reziprokes Gitter (`Kap7_Reziprok`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 1 „Stufe 1: Vom Quarz zum Rohsilizium“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 2 „Stufe 2: Reinigung über die Gasphase“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 3 „Stufe 3: Der Einkristall“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 4 „Stufe 4: Das reziproke Gitter in einer Dimension“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 5 „Stufe 5: Reziproke Gittervektoren in der Ebene und im Raum“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 6 „Stufe 6: Die Brillouin-Zone“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 7 „Stufe 7: Netzebenen und reziproke Vektoren“
- Elektronische Materialien und Bauelemente 1, Teil 7, Abschnitt 8 „Stufe 8: Der Kristall im Überblick“

### Elektronische Materialien und Bauelemente 1, Teil 8: Vom Atom zum Band (`Kap8_TightBinding`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 1 „Stufe 1: Was aus der Periodizität folgt“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 2 „Stufe 2: Bänder und Lücken“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 3 „Stufe 3: Zwei Atome“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 4 „Stufe 4: Vier Atome und die Matrix“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 5 „Stufe 5: Viele Atome“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 6 „Stufe 6: Bandbreite, Abstand und Besetzung“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 7 „Stufe 7: Zwei Orbitale je Atom“
- Elektronische Materialien und Bauelemente 1, Teil 8, Abschnitt 8 „Stufe 8: Das Rezept“

### Elektronische Materialien und Bauelemente 1, Teil 9: Bandstrukturen lesen (`Kap9_Bandstruktur`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 1 „Stufe 1: Das Band in der Ebene“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 2 „Stufe 2: Graphen“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 3 „Stufe 3: Silizium“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 4 „Stufe 4: GaAs, direkte und indirekte Lücke“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 5 „Stufe 5: Die effektive Masse im Kristall“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 6 „Stufe 6: Masse und Richtung“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 7 „Stufe 7: Das Loch“
- Elektronische Materialien und Bauelemente 1, Teil 9, Abschnitt 8 „Stufe 8: Was man an einer Bandstruktur abliest“

### Elektronische Materialien und Bauelemente 1, Teil 10: Zustandsdichte und Fermi-Verteilung (`Kap10_Fermi`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 1 „Stufe 1: Warum man Zustände zählt“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 2 „Stufe 2: Kreisring und Kugelschale“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 3 „Stufe 3: Leitungsband und Valenzband“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 4 „Stufe 4: Anordnungen zählen“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 5 „Stufe 5: Die Fermi-Verteilung“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 6 „Stufe 6: Temperatur und Boltzmann-Näherung“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 7 „Stufe 7: Elektronen und Löcher im Gleichgewicht“
- Elektronische Materialien und Bauelemente 1, Teil 10, Abschnitt 8 „Stufe 8: Ergänzung: Das Metall als Potentialtopf“

### Elektronische Materialien und Bauelemente 1, Teil 11: Eigenhalbleiter und Dotierung (`Kap11_Halbleiter`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 1 „Stufe 1: Welche Stoffe Halbleiter sind“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 2 „Stufe 2: Der reine Kristall“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 3 „Stufe 3: Fremdatome im Gitter“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 4 „Stufe 4: Warum die Bindung so schwach ist“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 5 „Stufe 5: Besetzung und Ladungsneutralität“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 6 „Stufe 6: Hohe und mittlere Temperaturen“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 7 „Stufe 7: Tiefe Temperaturen und die Lage von $E_\mathrm F$“
- Elektronische Materialien und Bauelemente 1, Teil 11, Abschnitt 8 „Stufe 8: Hohe Dotierstoffdichten“

### Elektronische Materialien und Bauelemente 1, Teil 12: Strom im Halbleiter (`Kap12_Transport`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 1 „Stufe 1: Strom aus besetzten Zuständen“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 2 „Stufe 2: Ohne Stöße kein Gleichstrom“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 3 „Stufe 3: Vom Wellenpaket zur Verteilungsfunktion“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 4 „Stufe 4: Was das Gleichgewicht verlangt“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 5 „Stufe 5: Der Streuterm und die Relaxationszeit“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 6 „Stufe 6: Der stationäre Strom“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 7 „Stufe 7: Beweglichkeit und Leitfähigkeit“
- Elektronische Materialien und Bauelemente 1, Teil 12, Abschnitt 8 „Stufe 8: Ergänzung: Der Hall-Effekt“

### Elektronische Materialien und Bauelemente 1, Teil 13: Diffusion, Rekombination und Grundgleichungen (`Kap13_Diffusion`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 1 „Stufe 1: Warum Teilchen ohne Kraft strömen“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 2 „Stufe 2: Die Kontinuitätsgleichung“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 3 „Stufe 3: Ergänzung: Diffusion aus unendlicher und endlicher Quelle“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 4 „Stufe 4: Diffusionsstrom und Einstein-Beziehung“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 5 „Stufe 5: Generation und Rekombination“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 6 „Stufe 6: Die Grundgleichungen der Halbleiter“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 7 „Stufe 7: Ergänzung: Raumladungen und Relaxation“
- Elektronische Materialien und Bauelemente 1, Teil 13, Abschnitt 8 „Stufe 8: Die Diffusionslänge“

### Elektronische Materialien und Bauelemente 1, Teil 14: Der p-n-Übergang (`Kap14_pn`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 1 „Stufe 1: Wie Ladung die Bänder verbiegt“
- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 2 „Stufe 2: Der Übergang im Gleichgewicht“
- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 3 „Stufe 3: Zwei Näherungen für die Ladung“
- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 4 „Stufe 4: Feld, Potential und Weite der Zone“
- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 5 „Stufe 5: Spannung anlegen“
- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 6 „Stufe 6: Injektion und Minoritätsträger“
- Elektronische Materialien und Bauelemente 1, Teil 14, Abschnitt 7 „Stufe 7: Die Diodenkennlinie“

### Elektronische Materialien und Bauelemente 1, Teil 15: Die MOS-Kapazität (`Kap15_MOS`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 1 „Stufe 1: Drei Stoffe auf einer Energieskala“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 2 „Stufe 2: Wie sich die Gatespannung aufteilt“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 3 „Stufe 3: Abschirmung und Akkumulation“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 4 „Stufe 4: Verarmung“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 5 „Stufe 5: Inversion“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 6 „Stufe 6: Die Schwellspannung“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 7 „Stufe 7: Die Inversionsschicht als Quantentopf“
- Elektronische Materialien und Bauelemente 1, Teil 15, Abschnitt 8 „Stufe 8: Die Kapazität in allen Bereichen“

### Elektronische Materialien und Bauelemente 1, Teil 16: Der reale MOS-Kondensator (`Kap16_MOSreal`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 1 „Stufe 1: Verschiedene Austrittsarbeiten“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 2 „Stufe 2: Feste Ladungen im Isolator“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 3 „Stufe 3: Die reale Bilanz und die verschobene Schwelle“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 4 „Stufe 4: Interfacezustände“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 5 „Stufe 5: Kennlinien bei niedriger und hoher Frequenz“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 6 „Stufe 6: Tiefenverarmung“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 7 „Stufe 7: Messen und Auswerten“
- Elektronische Materialien und Bauelemente 1, Teil 16, Abschnitt 8 „Stufe 8: Ergänzung: Charge-Coupled Devices“

### Elektronische Materialien und Bauelemente 1, Teil 17: Der MOSFET (`Kap17_MOSFET`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 1 „Stufe 1: Zwei Kontakte am MOS-Kondensator“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 2 „Stufe 2: Die Barriere im Kanal“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 3 „Stufe 3: Gradual Channel Approximation“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 4 „Stufe 4: Ausgangskennlinien“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 5 „Stufe 5: Transferkennlinie und Schwellspannung“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 6 „Stufe 6: Der Aus-Zustand“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 7 „Stufe 7: Vier Typen von MOSFETs“
- Elektronische Materialien und Bauelemente 1, Teil 17, Abschnitt 8 „Stufe 8: Ergänzung: Grundschaltungen“

### Elektronische Materialien und Bauelemente 1, Teil 19: Ergänzung: Licht und Laser (`Kap19_Licht`, Modul gemb1)

- Elektronische Materialien und Bauelemente 1, Teil 19, Abschnitt 1 „Stufe 1: Absorption und Emission“
- Elektronische Materialien und Bauelemente 1, Teil 19, Abschnitt 2 „Stufe 2: Fluoreszenz und Nanokristalle“
- Elektronische Materialien und Bauelemente 1, Teil 19, Abschnitt 3 „Stufe 3: Spontane und stimulierte Emission“
- Elektronische Materialien und Bauelemente 1, Teil 19, Abschnitt 4 „Stufe 4: Die Besetzungsumkehr“
- Elektronische Materialien und Bauelemente 1, Teil 19, Abschnitt 5 „Stufe 5: Der Laser“

## Informatik / Programmieren / Python

### Programmieren, Python 1: Programme und der Python-Interpreter (`Kap1_Programme`, Modul prog)

- Programmieren, Python 1, Abschnitt 1 „Programme und Programmiersprachen“: 1.1 Das Programm · 1.2 Was der Prozessor versteht: Maschinenbefehle · 1.3 Die Programmiersprache · 1.4 Die Syntax · 1.5 Die Semantik · 1.6 Der Quelltext
- Programmieren, Python 1, Abschnitt 2 „Vom Quelltext zur Ausführung: Compiler und Interpreter“: 2.1 Der Compiler · 2.2 Der Interpreter · 2.3 Python und CPython · 2.4 Der Bytecode
- Programmieren, Python 1, Abschnitt 3 „Python einrichten“: 3.1 Was du dafür brauchst: ein Terminal öffnen · 3.2 Python unter Windows: der Python install manager · 3.3 Python unter Linux · 3.4 Die Versionsnummer
- Programmieren, Python 1, Abschnitt 4 „Der interaktive Modus“: 4.1 Der interaktive Modus · 4.2 Der Wert · 4.3 Der Ausdruck · 4.4 Rechnen wie mit dem Taschenrechner · 4.5 Das Rezept im interaktiven Modus: erst von Hand, dann fertig · 4.6 Text als Wert: die Zeichenkette · 4.7 Die Funktion · 4.8 Der Funktionsaufruf: `print`
- Programmieren, Python 1, Abschnitt 5 „Skripte schreiben und ausführen“: 5.1 Der Editor · 5.2 Das Skript · 5.3 Der Kommentar
- Programmieren, Python 1, Abschnitt 6 „Fehler lesen und verstehen“: 6.1 Der Syntaxfehler · 6.2 Der Laufzeitfehler · 6.3 Die Ausnahme · 6.4 Der Traceback · 6.5 Der Logikfehler

### Programmieren, Python 2: Werte, Typen und Variablen (`Kap2_Werte`, Modul prog)

- Programmieren, Python 2, Abschnitt 1 „Objekte und Typen“: 1.1 Das Objekt · 1.2 Der Typ · 1.3 Die Identität · 1.4 Die Methode
- Programmieren, Python 2, Abschnitt 2 „Ganze Zahlen und Rechenoperatoren“: 2.1 Der Typ `int` · 2.2 Operator und Operand · 2.3 Die Division · 2.4 Ganzzahldivision und Rest · 2.5 Die Potenz · 2.6 Die Rangfolge
- Programmieren, Python 2, Abschnitt 3 „Zahlen im Binärsystem“: 3.1 Das Stellenwertsystem · 3.2 Die Binärzahl · 3.3 Das Byte · 3.4 Ins Binärsystem umrechnen: erst von Hand, dann fertig · 3.5 Die Hexadezimalzahl · 3.6 Binärbrüche · 3.7 Das Verdopplungsverfahren
- Programmieren, Python 2, Abschnitt 4 „Gleitkommazahlen: der Typ `float`“: 4.1 Die Gleitkommadarstellung · 4.2 Der Typ `float` · 4.3 Das Exponentenfeld · 4.4 Das Mantissenfeld · 4.5 Einen `float` in seine Felder zerlegen · 4.6 Der Darstellungsfehler · 4.7 Die kürzeste Darstellung
- Programmieren, Python 2, Abschnitt 5 „Rechnen mit Gleitkommazahlen“: 5.1 Der Rundungsfehler einer Rechnung · 5.2 Die Maschinengenauigkeit · 5.3 Die Absorption · 5.4 Die Auslöschung · 5.5 Der Überlauf: `inf` · 5.6 Das ungültige Ergebnis: `nan`
- Programmieren, Python 2, Abschnitt 6 „Variablen: Namen für Objekte“: 6.1 Die Zuweisung · 6.2 Die Variable · 6.3 Neu binden statt kopieren · 6.4 Die Namensregeln · 6.5 Die erweiterte Zuweisung · 6.6 Variablen im Skript
- Programmieren, Python 2, Abschnitt 7 „Wahrheitswerte und Vergleiche“: 7.1 Der Typ `bool` · 7.2 Die Vergleichsoperatoren · 7.3 Gleitkommazahlen nicht auf Gleichheit prüfen · 7.4 Der Vergleich mit Toleranz · 7.5 Der Identitätsvergleich · 7.6 Der Wert `None`
- Programmieren, Python 2, Abschnitt 8 „Module: `math` und `sys`“: 8.1 Das Modul und `import` · 8.2 Das Modul `math` · 8.3 Der Toleranzvergleich, fertig: `math.isclose` · 8.4 Die Grenzen des Typs `float`, fertig: `sys.float_info`
- Programmieren, Python 2, Abschnitt 9 „Komplexe Zahlen“: 9.1 Was du dafür brauchst: komplexe Zahlen · 9.2 Der Typ `complex` · 9.3 Das Attribut: Real- und Imaginärteil · 9.4 Das Modul `cmath` · 9.5 Betrag und Phase: erst von Hand, dann fertig · 9.6 Anwendung: die Impedanz eines RC-Glieds
- Programmieren, Python 2, Abschnitt 10 „Zeichenketten, Eingabe und Ausgabe“: 10.1 Zeichenketten verketten und vervielfachen · 10.2 Der f-String · 10.3 Die Eingabe mit `input` · 10.4 Die Typumwandlung · 10.5 Runden: erst von Hand, dann fertig · 10.6 Anwendung: ein Einheitenrechner

### Programmieren, Python 3: Entscheidungen und Schleifen (`Kap3_Kontrollfluss`, Modul prog)

- Programmieren, Python 3, Abschnitt 1 „Bedingungen: Vergleiche und logische Operatoren“: 1.1 Rückblick: Wahrheitswerte und Vergleiche · 1.2 Verkettete Vergleiche · 1.3 Zeichenketten vergleichen · 1.4 Der Operator `not` · 1.5 Der Operator `and` · 1.6 Der Operator `or` · 1.7 Die Rangfolge der logischen Operatoren · 1.8 Die Kurzschlussauswertung · 1.9 Der Wahrheitswert von Objekten · 1.10 Was `and` und `or` als Ergebnis liefern
- Programmieren, Python 3, Abschnitt 2 „Entscheidungen: if, elif und else“: 2.1 Die bedingte Anweisung `if` · 2.2 Der Block und die Einrückung · 2.3 Die Alternative `else` · 2.4 Mehrere Fälle: `elif` · 2.5 Typische Fehler in Bedingungen · 2.6 Anwendung: ein Messbereich mit Unter- und Überlauf
- Programmieren, Python 3, Abschnitt 3 „Wiederholen mit while“: 3.1 Die `while`-Schleife · 3.2 Die Endlosschleife · 3.3 Die Gleitkomma-Falle · 3.4 Anwendung: Wie lange sich ein Kondensator entlädt
- Programmieren, Python 3, Abschnitt 4 „Zählen mit for und range“: 4.1 Die `for`-Schleife · 4.2 Die Zahlenfolge `range` · 4.3 Gleitkomma-Schritte über einen ganzzahligen Zähler · 4.4 `for` oder `while`?
- Programmieren, Python 3, Abschnitt 5 „Schleifen steuern, verschachteln und Ergebnisse sammeln“: 5.1 Abbrechen mit `break` · 5.2 Überspringen mit `continue` · 5.3 Verschachtelte Schleifen · 5.4 Das Akkumulator-Muster · 5.5 Anwendung: Mittelwert und Maximum
- Programmieren, Python 3, Abschnitt 6 „Lösungen durch Probieren: Raten und Prüfen, Näherung mit Toleranz“: 6.1 Raten und Prüfen · 6.2 Die Näherung mit Toleranz · 6.3 Schrittweite und Toleranz
- Programmieren, Python 3, Abschnitt 7 „Die Bisektion“: 7.1 Was du dafür brauchst: der Zwischenwertsatz · 7.2 Das Bisektionsverfahren · 7.3 Die Wurzel durch Bisektion · 7.4 Die Schrittzahl der Bisektion
- Programmieren, Python 3, Abschnitt 8 „Das Newton-Verfahren“: 8.1 Was du dafür brauchst: Ableitung und Tangente · 8.2 Das Newton-Verfahren · 8.3 Die Wurzel durch Newton · 8.4 Die Konvergenzgeschwindigkeit · 8.5 Die Grenzen des Newton-Verfahrens · 8.6 Der fertige Weg: `math.sqrt`
- Programmieren, Python 3, Abschnitt 9 „Anwendung: der Arbeitspunkt einer Diode“: 9.1 Was du dafür brauchst: Diodenkennlinie und Vorwiderstand · 9.2 Der Arbeitspunkt als Nullstelle · 9.3 Der Arbeitspunkt durch Bisektion · 9.4 Der Arbeitspunkt durch Newton

## Informatik / Linux und Kommandozeile

(noch kein Heft; Modul `linux` in tools/heft_zu_artikel.py)

## Informatik / Cybersecurity

### Cybersecurity, Teil 1: Sicherheit, Schutzziele und Spielregeln (`Kap1_Sicherheit`, Modul cyber)

- Cybersecurity, Teil 1, Abschnitt 1 „Was geschützt wird: Schutzgut und Schutzziele“: 1.1 Das Schutzgut · 1.2 Berechtigte und Unbefugte · 1.3 Schutzziele · 1.4 Vertraulichkeit · 1.5 Integrität · 1.6 Verfügbarkeit · 1.7 Authentizität · 1.8 Verbindlichkeit · 1.9 Schutzbedarf
- Cybersecurity, Teil 1, Abschnitt 2 „Von der Schwachstelle zum Schaden“: 2.1 Schwachstelle · 2.2 Bedrohung · 2.3 Angreifer · 2.4 Angriff · 2.5 Exploit · 2.6 Der Schaden
- Cybersecurity, Teil 1, Abschnitt 3 „Risiko, Angreifermodell und Angriffsfläche“: 3.1 Was du dafür brauchst: Häufigkeit und Erwartungswert · 3.2 Was du dafür brauchst: unabhängige Ereignisse · 3.3 Risiko · 3.4 Das Gesamtrisiko · 3.5 Sicherheit ist Ökonomie · 3.6 Angreifermodell · 3.7 Angriffsfläche
- Cybersecurity, Teil 1, Abschnitt 4 „Richtlinie und Mechanismus“: 4.1 Sicherheitsrichtlinie · 4.2 Sicherheitsmechanismus · 4.3 Verhindern, erkennen, wiederherstellen · 4.4 Passiver und aktiver Angriff
- Cybersecurity, Teil 1, Abschnitt 5 „Sicherheitsprinzipien: Rechte vergeben und prüfen“: 5.1 Sicherheitsprinzipien · 5.2 Minimale Rechte · 5.3 Aufgabentrennung · 5.4 Sichere Voreinstellung · 5.5 Lückenlose Prüfung · 5.6 Prüfen und Handeln im selben Moment
- Cybersecurity, Teil 1, Abschnitt 6 „Sicherheitsprinzipien: Systeme robust entwerfen“: 6.1 Mehrere Verteidigungslinien · 6.2 Einfachheit · 6.3 Eine kleine vertrauenswürdige Basis · 6.4 Kein Verlass auf ein geheimes Verfahren · 6.5 Der Mensch als Teil des Systems · 6.6 Sicherheit von Anfang an
- Cybersecurity, Teil 1, Abschnitt 7 „Schwachstellen benennen und bewerten“: 7.1 CVE: der Name einer Schwachstelle · 7.2 CWE: die Art des Fehlers · 7.3 CVSS: die Schwere · 7.4 Wie aus dem Vektor die Zahl wird · 7.5 Der Lebenszyklus einer Schwachstelle · 7.6 Zero-Day
- Cybersecurity, Teil 1, Abschnitt 8 „Computerstrafrecht: was verboten ist“: 8.1 Was du dafür brauchst: wie ein Straftatbestand gebaut ist · 8.2 Ausspähen von Daten (§ 202a StGB) · 8.3 Abfangen von Daten (§ 202b StGB) · 8.4 Vorbereiten des Ausspähens und Abfangens (§ 202c StGB) · 8.5 Datenhehlerei (§ 202d StGB) · 8.6 Datenveränderung (§ 303a StGB) · 8.7 Computersabotage (§ 303b StGB) · 8.8 Computerbetrug (§ 263a StGB)
- Cybersecurity, Teil 1, Abschnitt 9 „Erlaubnis, Werkzeuge und gute Absicht“: 9.1 Die Erlaubnis des Berechtigten · 9.2 Antragsdelikt heißt nicht erlaubt · 9.3 Werkzeuge besitzen: der Beschluss von 2009 · 9.4 Gute Absicht schützt nicht
- Cybersecurity, Teil 1, Abschnitt 10 „Offenlegung und Ethik“: 10.1 Was du dafür brauchst: der Aufbau einer Webadresse · 10.2 Koordinierte Offenlegung · 10.3 Meldeprogramme und Bug-Bounty · 10.4 security.txt · 10.5 Was man bei einem Zufallsfund tut · 10.6 Hackerethik · 10.7 Die Spielregeln dieser Reihe

## Informatik / Machine Learning / Mathematische Grundlagen

### Grundlagen 1: Vektoren und Matrizen (`Kap1_Vektoren`, Modul ml)

- Grundlagen 1, Abschnitt 1 „Vektoren: Daten als Zahlenlisten“: 1.1 Was du dafür brauchst: Summenzeichen und Indizes · 1.2 Beispiele und Merkmale · 1.3 Vektoren · 1.4 Addition und Vielfaches · 1.5 Linearkombinationen · 1.6 Die Einheitsvektoren
- Grundlagen 1, Abschnitt 2 „Das Skalarprodukt“: 2.1 Das Skalarprodukt zweier Vektoren · 2.2 Gewichte und gewichtete Summen · 2.3 Summe und Mittelwert als Skalarprodukt · 2.4 Das Skalarprodukt als Mustervergleich
- Grundlagen 1, Abschnitt 3 „Normen: die Größe eines Vektors“: 3.1 Die euklidische Norm · 3.2 Die Betragssummennorm · 3.3 Die Maximumnorm · 3.4 Was eine Norm ausmacht · 3.5 Der Fehlervektor und seine Größe · 3.6 Der Effektivwert
- Grundlagen 1, Abschnitt 4 „Abstände und Einheiten“: 4.1 Der Abstand zweier Datenpunkte · 4.2 Abstände hängen von den Einheiten ab · 4.3 Abweichungen vom Mittelwert · 4.4 Die Standardabweichung · 4.5 Standardisieren
- Grundlagen 1, Abschnitt 5 „Winkel und Ähnlichkeit“: 5.1 Die Cauchy-Schwarz-Ungleichung · 5.2 Der Winkel zwischen zwei Vektoren · 5.3 Orthogonale Vektoren · 5.4 Die Kosinus-Ähnlichkeit · 5.5 Das Skalarprodukt als Schattenlänge
- Grundlagen 1, Abschnitt 6 „Matrizen und die Datenmatrix“: 6.1 Matrizen · 6.2 Quadratische Matrizen und Diagonalmatrizen · 6.3 Die Datenmatrix
- Grundlagen 1, Abschnitt 7 „Das Matrix-Vektor-Produkt“: 7.1 Matrix mal Vektor · 7.2 Die Zeilensicht: viele Skalarprodukte · 7.3 Die Spaltensicht: eine Linearkombination der Spalten · 7.4 Der Spaltenraum
- Grundlagen 1, Abschnitt 8 „Lineare Abbildungen“: 8.1 Lineare Abbildungen · 8.2 Jede lineare Abbildung ist eine Matrix · 8.3 Lineare Abbildungen der Ebene · 8.4 Lineare Funktionen mit einem Ausgang · 8.5 Affine Abbildungen
- Grundlagen 1, Abschnitt 9 „Das Matrixprodukt“: 9.1 Das Matrixprodukt · 9.2 Viele Vektoren auf einmal · 9.3 Rechenregeln: Die Reihenfolge zählt · 9.4 Zwei lineare Stufen sind eine · 9.5 Das äußere Produkt
- Grundlagen 1, Abschnitt 10 „Transponierte, Symmetrie und Gram-Matrix“: 10.1 Die Transponierte · 10.2 Symmetrische Matrizen · 10.3 Die Gram-Matrix der Beispiele · 10.4 Die Gram-Matrix der Merkmale
- Grundlagen 1, Abschnitt 11 „Einheitsmatrix und Inverse“: 11.1 Die Einheitsmatrix · 11.2 Die inverse Matrix · 11.3 Die Inverse einer $2\times2$-Matrix · 11.4 Rechenregeln für Inverse · 11.5 Wann es keine Inverse gibt
- Grundlagen 1, Abschnitt 12 „Lineare Gleichungssysteme“: 12.1 Gleichungssysteme in Matrixform · 12.2 Zeilenbild und Spaltenbild · 12.3 Das Gauß-Verfahren · 12.4 Keine, eine oder unendlich viele Lösungen · 12.5 Mehr Gleichungen als Unbekannte
- Grundlagen 1, Abschnitt 13 „Unabhängigkeit, Basis und Rang“: 13.1 Der Spann · 13.2 Lineare Unabhängigkeit · 13.3 Basis und Dimension · 13.4 Der Rang einer Matrix · 13.5 Der Kern und der Rangsatz · 13.6 Abhängige Merkmale
- Grundlagen 1, Abschnitt 14 „Die Determinante“: 14.1 Die Determinante einer $2\times2$-Matrix · 14.2 Das Vorzeichen der Determinante · 14.3 Der Flächenfaktor gilt für jede Figur · 14.4 Determinanten größerer Matrizen · 14.5 Rechenregeln für Determinanten · 14.6 Determinante und Invertierbarkeit
- Grundlagen 1, Abschnitt 15 „Elementweise Rechnen und Tensoren“: 15.1 Das Hadamard-Produkt · 15.2 Elementweise Funktionen · 15.3 Einen Vektor zu jeder Zeile addieren · 15.4 Tensoren · 15.5 Bilder als Tensoren

### Grundlagen 2: Projektion, Eigenwerte und Zerlegungen (`Kap2_Eigenwerte`, Modul ml)

- Grundlagen 2, Abschnitt 1 „Orthonormalbasen und orthogonale Matrizen“: 1.1 Orthonormale Vektoren · 1.2 Orthonormalbasen · 1.3 Koordinaten in einer Orthonormalbasis · 1.4 Orthogonale Matrizen · 1.5 Längen und Winkel bleiben erhalten · 1.6 Matrizen mit orthonormalen Spalten
- Grundlagen 2, Abschnitt 2 „Projektion auf eine Gerade“: 2.1 Der Fußpunkt des Lots · 2.2 Der Fußpunkt ist der nächste Punkt · 2.3 Die Projektionsmatrix · 2.4 Projektionen im Allgemeinen
- Grundlagen 2, Abschnitt 3 „Die beste Näherungslösung“: 3.1 Rückblick: Mehr Gleichungen als Unbekannte · 3.2 Die beste Näherungslösung · 3.3 Die Normalgleichungen · 3.4 Warum die Normalgleichungen die beste Lösung liefern · 3.5 Wann die beste Näherungslösung eindeutig ist · 3.6 Eine Gerade durch drei Punkte · 3.7 Die Wohnungen: was Grundlagen 1 offen ließ
- Grundlagen 2, Abschnitt 4 „Projektion auf einen Unterraum“: 4.1 Unterräume · 4.2 Die Projektionsmatrix eines Spaltenraums · 4.3 Orthonormale Spalten · 4.4 Das orthogonale Komplement · 4.5 Das Gram-Schmidt-Verfahren · 4.6 Die QR-Zerlegung · 4.7 Die beste Näherungslösung mit QR
- Grundlagen 2, Abschnitt 5 „Quadratische Formen“: 5.1 Quadratische Formen · 5.2 Nur der symmetrische Anteil zählt · 5.3 Schüssel, Rinne und Sattel · 5.4 Quadratisch ergänzen
- Grundlagen 2, Abschnitt 6 „Eigenwerte und Eigenvektoren“: 6.1 Was du dafür brauchst: komplexe Zahlen · 6.2 Eigenvektoren und Eigenwerte · 6.3 Das charakteristische Polynom · 6.4 Eigenvektoren berechnen · 6.5 Spur und Determinante · 6.6 Komplexe Eigenwerte · 6.7 Mehrfache Eigenwerte · 6.8 Wie viele Eigenvektoren es gibt · 6.9 Rechenregeln für Eigenwerte
- Grundlagen 2, Abschnitt 7 „Diagonalisierung und Spektralsatz“: 7.1 Basiswechsel · 7.2 Diagonalisierung · 7.3 Entkoppeln: Potenzen und Folgen · 7.4 Symmetrische Matrizen haben reelle Eigenwerte · 7.5 Eigenvektoren symmetrischer Matrizen stehen senkrecht · 7.6 Der Spektralsatz · 7.7 Hauptachsen
- Grundlagen 2, Abschnitt 8 „Positiv definite Matrizen“: 8.1 Positiv definit und positiv semidefinit · 8.2 Der Eigenwerttest · 8.3 Tests ohne Eigenwerte · 8.4 Gram-Matrizen sind positiv semidefinit · 8.5 Größter und kleinster Wert auf dem Einheitskreis · 8.6 Die Cholesky-Zerlegung
- Grundlagen 2, Abschnitt 9 „Die Singulärwertzerlegung“: 9.1 Senkrechte Richtungen, die senkrecht bleiben · 9.2 Singulärwerte · 9.3 Singulärvektoren · 9.4 Die Zerlegung · 9.5 Drehung, Streckung, Drehung · 9.6 Bausteine vom Rang 1 und die Räume einer Matrix · 9.7 Symmetrische Matrizen · 9.8 Die Spektralnorm
- Grundlagen 2, Abschnitt 10 „Näherung durch Matrizen von kleinem Rang“: 10.1 Die Frobeniusnorm · 10.2 Die abgeschnittene Zerlegung · 10.3 Die beste Näherung · 10.4 Ein Bild mit wenigen Zahlen
- Grundlagen 2, Abschnitt 11 „Die Pseudoinverse“: 11.1 Linksinverse · 11.2 Rechtsinverse · 11.3 Die Pseudoinverse · 11.4 Die kürzeste beste Näherungslösung
- Grundlagen 2, Abschnitt 12 „Die Konditionszahl“: 12.1 Ein empfindliches Gleichungssystem · 12.2 Die Konditionszahl · 12.3 Konditionszahl und Determinante · 12.4 Normalgleichungen quadrieren die Konditionszahl

### Grundlagen 3: Ableitung, Gradient und Kettenregel (`Kap3_Ableitung`, Modul ml)

- Grundlagen 3, Abschnitt 1 „Die Ableitung“: 1.1 Änderungsrate und Differenzenquotient · 1.2 Die Ableitung · 1.3 Die lineare Näherung · 1.4 Ableitungsregeln · 1.5 Die zweite Ableitung und die quadratische Näherung
- Grundlagen 3, Abschnitt 2 „Die Kettenregel“: 2.1 Verkettung · 2.2 Die Kettenregel · 2.3 Ketten aus vielen Gliedern · 2.4 Die logistische Funktion
- Grundlagen 3, Abschnitt 3 „Partielle Ableitungen und der Gradient“: 3.1 Funktionen mehrerer Variablen · 3.2 Partielle Ableitungen · 3.3 Der Gradient · 3.4 Die lineare Näherung im Raum · 3.5 Differenzierbarkeit
- Grundlagen 3, Abschnitt 4 „Richtungsableitung und steilster Anstieg“: 4.1 Die Richtungsableitung · 4.2 Die Richtung des steilsten Anstiegs · 4.3 Der Gradient steht senkrecht auf den Höhenlinien · 4.4 Steilster Abstieg und der tiefste Punkt
- Grundlagen 3, Abschnitt 5 „Die Jacobi-Matrix“: 5.1 Funktionen mit mehreren Ausgängen · 5.2 Die Jacobi-Matrix · 5.3 Die lineare Näherung mit der Jacobi-Matrix · 5.4 Zwei wichtige Jacobi-Matrizen
- Grundlagen 3, Abschnitt 6 „Die Kettenregel für mehrere Variablen“: 6.1 Die Kettenregel als Matrixprodukt · 6.2 Summe über alle Wege · 6.3 Der Gradient einer Verkettung · 6.4 Ableitung entlang einer Kurve
- Grundlagen 3, Abschnitt 7 „Ableiten nach Vektoren und Matrizen“: 7.1 Die Layout-Konvention · 7.2 Lineare Funktionen · 7.3 Quadratische Formen · 7.4 Die Quadratsumme eines Residuums · 7.5 Ableiten nach einer Matrix · 7.6 Rückwärts durch ein Matrixprodukt
- Grundlagen 3, Abschnitt 8 „Die Hesse-Matrix und die quadratische Näherung“: 8.1 Zweite partielle Ableitungen · 8.2 Die Hesse-Matrix · 8.3 Der Satz von Schwarz · 8.4 Die quadratische Näherung · 8.5 Die Krümmung in einer Richtung
- Grundlagen 3, Abschnitt 9 „Rechengraphen“: 9.1 Zwischenergebnisse · 9.2 Der Rechengraph · 9.3 Die Vorwärtsrechnung · 9.4 Lokale Ableitungen
- Grundlagen 3, Abschnitt 10 „Automatische Differentiation“: 10.1 Was automatische Differentiation ist · 10.2 Der Vorwärtsmodus · 10.3 Der Rückwärtsmodus · 10.4 Muster im Rückwärtsfluss · 10.5 Der Aufwand · 10.6 Klammerung: Vektor mal Jacobi-Matrix
- Grundlagen 3, Abschnitt 11 „Numerische Ableitung und Gradientenprüfung“: 11.1 Die Vorwärtsdifferenz · 11.2 Die zentrale Differenz · 11.3 Was du dafür brauchst: Gleitkommazahlen · 11.4 Die Fehlerkurve · 11.5 Die Gradientenprüfung · 11.6 Knicke und andere Fallstricke

### Grundlagen 4: Wahrscheinlichkeit (`Kap4_Wahrscheinlichkeit`, Modul ml)

- Grundlagen 4, Abschnitt 1 „Zufall und Ereignisse“: 1.1 Was du dafür brauchst: Mengen · 1.2 Zufallsexperiment und Ergebnisraum · 1.3 Ereignisse
- Grundlagen 4, Abschnitt 2 „Wahrscheinlichkeit“: 2.1 Die relative Häufigkeit · 2.2 Die Axiome der Wahrscheinlichkeit · 2.3 Rechenregeln · 2.4 Gleich wahrscheinliche Ergebnisse
- Grundlagen 4, Abschnitt 3 „Bedingte Wahrscheinlichkeit“: 3.1 Wahrscheinlichkeiten aus einer Zähltabelle · 3.2 Bedingte Wahrscheinlichkeit · 3.3 Die Produktregel · 3.4 Die totale Wahrscheinlichkeit
- Grundlagen 4, Abschnitt 4 „Der Satz von Bayes“: 4.1 Die Bedingung umdrehen · 4.2 Natürliche Häufigkeiten · 4.3 Die Basisrate
- Grundlagen 4, Abschnitt 5 „Unabhängigkeit“: 5.1 Unabhängige Ereignisse · 5.2 Unabhängig ist nicht unvereinbar · 5.3 Mehrere unabhängige Ereignisse · 5.4 Bedingte Unabhängigkeit
- Grundlagen 4, Abschnitt 6 „Zufallsvariablen und Verteilungen“: 6.1 Zufallsvariablen · 6.2 Diskrete Verteilungen · 6.3 Was du dafür brauchst: Integrale · 6.4 Dichten · 6.5 Die Verteilungsfunktion
- Grundlagen 4, Abschnitt 7 „Erwartungswert und Varianz“: 7.1 Der Erwartungswert · 7.2 Der Erwartungswert einer Funktion · 7.3 Die Linearität des Erwartungswerts · 7.4 Varianz und Standardabweichung · 7.5 Die Verschiebungsformel · 7.6 Umrechnen und Standardisieren · 7.7 Mittelwert der Daten und Erwartungswert
- Grundlagen 4, Abschnitt 8 „Wichtige Verteilungen“: 8.1 Die Bernoulli-Verteilung · 8.2 Die kategorische Verteilung · 8.3 Die Binomialverteilung · 8.4 Die Gleichverteilung · 8.5 Die Normalverteilung · 8.6 Standardisieren und die Verteilungsfunktion $\Phi$ · 8.7 Rauschen als Zufallsvariable
- Grundlagen 4, Abschnitt 9 „Mehrere Zufallsvariablen“: 9.1 Was du dafür brauchst: Doppelintegrale · 9.2 Die gemeinsame Verteilung · 9.3 Randverteilungen · 9.4 Bedingte Verteilungen · 9.5 Unabhängige Zufallsvariablen · 9.6 Unabhängig und identisch verteilt
- Grundlagen 4, Abschnitt 10 „Kovarianz und Korrelation“: 10.1 Die Kovarianz · 10.2 Die Varianz einer Summe · 10.3 Der Korrelationskoeffizient · 10.4 Die Kovarianz als Skalarprodukt · 10.5 Unkorreliert heißt nicht unabhängig · 10.6 Kovarianz und Korrelation eines Datensatzes
- Grundlagen 4, Abschnitt 11 „Zufallsvektoren und die Kovarianzmatrix“: 11.1 Zufallsvektoren · 11.2 Die Kovarianzmatrix · 11.3 Die Kovarianzmatrix eines Datensatzes · 11.4 Lineare Abbildungen von Zufallsvektoren · 11.5 Die Streuung in einer Richtung · 11.6 Kovarianzmatrizen sind positiv semidefinit
- Grundlagen 4, Abschnitt 12 „Die mehrdimensionale Normalverteilung“: 12.1 Die Dichte · 12.2 Höhenlinien und der Mahalanobis-Abstand · 12.3 Im Eigensystem zerfällt die Verteilung · 12.4 Lineare Abbildungen und das Erzeugen normalverteilter Vektoren · 12.5 Bedingte Verteilungen · 12.6 Unkorreliert und unabhängig
- Grundlagen 4, Abschnitt 13 „Mittelwerte vieler Zufallsvariablen“: 13.1 Der Mittelwert unabhängiger Zufallsvariablen · 13.2 Die Tschebyschow-Ungleichung · 13.3 Das Gesetz der großen Zahlen · 13.4 Der zentrale Grenzwertsatz

### Grundlagen 5: Statistik und Information (`Kap5_Statistik`, Modul ml)

- Grundlagen 5, Abschnitt 1 „Schätzen aus einer Stichprobe“: 1.1 Wahrscheinlichkeitsrechnung und Statistik · 1.2 Rückblick: Die Stichprobe · 1.3 Schätzer · 1.4 Die Stichprobenverteilung
- Grundlagen 5, Abschnitt 2 „Wie gut ist ein Schätzer?“: 2.1 Verzerrung und Erwartungstreue · 2.2 Varianz und Standardfehler eines Schätzers · 2.3 Der mittlere quadratische Fehler · 2.4 Konsistenz
- Grundlagen 5, Abschnitt 3 „Die Varianz schätzen“: 3.1 Teilen durch $N$ unterschätzt die Varianz · 3.2 Die Bessel-Korrektur · 3.3 Erwartungstreu heißt nicht genauer
- Grundlagen 5, Abschnitt 4 „Die Likelihood“: 4.1 Was du dafür brauchst: Logarithmen · 4.2 Die Likelihood · 4.3 Die Likelihood einer Stichprobe · 4.4 Die Log-Likelihood
- Grundlagen 5, Abschnitt 5 „Die Maximum-Likelihood-Schätzung“: 5.1 Was du dafür brauchst: Der höchste Punkt einer Kurve · 5.2 Der Maximum-Likelihood-Schätzer · 5.3 Die Normalverteilung: der Mittelwert · 5.4 Die Normalverteilung: die Varianz · 5.5 Umrechnen eines Maximum-Likelihood-Schätzers
- Grundlagen 5, Abschnitt 6 „Prior und Posterior“: 6.1 Der Satz von Bayes für Parameter · 6.2 Die Prior-Verteilung · 6.3 Was du dafür brauchst: Ein Integral über Potenzen · 6.4 Die Beta-Verteilung · 6.5 Die Posterior-Verteilung · 6.6 Konjugierte Prior-Verteilungen · 6.7 Der Posterior-Mittelwert und die Laplace-Regel
- Grundlagen 5, Abschnitt 7 „Die Maximum-a-posteriori-Schätzung“: 7.1 Der MAP-Schätzer · 7.2 Der Prior als Strafterm · 7.3 Ein Gauß-Prior für einen Mittelwert · 7.4 Drei Schätzer im Vergleich
- Grundlagen 5, Abschnitt 8 „Informationsgehalt und Entropie“: 8.1 Der Informationsgehalt · 8.2 Die Entropie · 8.3 Entropie und Codelänge · 8.4 Die binäre Entropie
- Grundlagen 5, Abschnitt 9 „Kreuzentropie und KL-Divergenz“: 9.1 Die Kreuzentropie · 9.2 Die KL-Divergenz · 9.3 Was du dafür brauchst: Die Ungleichung $\ln x\le x-1$ · 9.4 Die Gibbs-Ungleichung · 9.5 Die KL-Divergenz ist kein Abstand
- Grundlagen 5, Abschnitt 10 „Die größte Entropie“: 10.1 Die Gleichverteilung hat die größte Entropie · 10.2 Die Entropie einer Dichte · 10.3 Die KL-Divergenz für Dichten · 10.4 Die Normalverteilung hat bei fester Varianz die größte Entropie
- Grundlagen 5, Abschnitt 11 „Maximum Likelihood und KL-Divergenz“: 11.1 Rückblick: Die empirische Verteilung · 11.2 Die Log-Likelihood als Kreuzentropie · 11.3 Maximum Likelihood heißt kleinste KL-Divergenz · 11.4 Die kategorische Verteilung · 11.5 Stetige Daten: Normalverteilung und Quadratsumme
