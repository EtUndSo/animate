# Abbildungen und Animationen — Paket prog_b (Heft prog/03-entscheidungen-und-schleifen)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.

Heft prog/03-entscheidungen-und-schleifen, 11 deutsche Artikel (01 bis 11). 11 Szenen `prog/k3…` vorhanden, alle statisch (`animations` leer); nur `k3rquadrate` hat eine echte Editor-Operation (`Summation`), `k3rmittel` ist ein einzelner statischer `MathTex`, die übrigen sind Flussdiagramme (TextBox/LabeledArrow), Zahlenstrahl- und Graphbilder. Kein Artikel hat mehr als 5 Abbildungen. Prog Heft 1 und 2 (prog_a) lagen zum Zeitpunkt nicht vor; keine Überschneidung bekannt. hm1 Heft 5 hat `hm1/k5zws` und `hm1/k5nullstelle` (Zwischenwertsatz, Nullstelle), dort Wiederverwendung vorgeschlagen (V20).

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-entscheidungen-und-schleifen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-bedingungen-vergleiche-und-logische-operatoren | 5 | 0 | 4 | 1 | 0 | 0 | 5 |
| 03-entscheidungen-if-elif-und-else | 5 | 3 | 1 | 2 | 0 | 1 | 5 |
| 04-wiederholen-mit-while | 4 | 1 | 2 | 1 | 0 | 0 | 4 |
| 05-zahlen-mit-for-und-range | 4 | 1 | 1 | 1 | 0 | 0 | 3 |
| 06-schleifen-steuern-verschachteln-und-ergebnisse-sammeln | 5 | 2 | 2 | 1 | 0 | 0 | 5 |
| 07-losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz | 3 | 0 | 2 | 0 | 0 | 0 | 2 |
| 08-die-bisektion | 4 | 1 | 2 | 1 | 0 | 0 | 4 |
| 09-das-newton-verfahren | 5 | 2 | 2 | 1 | 0 | 0 | 5 |
| 10-anwendung-der-arbeitspunkt-einer-diode | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| 11-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Summe** | 40 | 11 | 19 | 9 | 0 | 1 | 38 |

Abweichungen vom Soll: 05 und 07 liegen um 1 darunter (Rest wäre C: Zeitachse Aufaddieren/Zähler ist durch V10 abgedeckt, Kostenvergleich der Verfahren würde Bisektion vorwegnehmen). Kein Artikel über dem Soll. 03: `k3block` entfällt und geht in V7 auf.

## Top 3

- V7 [A] 03-entscheidungen-if-elif-und-else — Skript Zeile für Zeile mit Zeilenmarke, Speicher und übersprungenem Block (ersetzt `k3block`) — das Grundmuster „Programmablauf“, auf dem alle Schleifenbilder aufbauen; zeigt, was „Block überspringen“ heißt
- V21 [A] 08-die-bisektion — Bisektion am Graphen von x² − 2 mit lo, hi, Mitte und dem Vorzeichen von f(m) — verbindet Programm, Vorzeichen und Intervallwahl, was die vorhandene Schachtelung allein nicht erklärt
- V10 [A] 04-wiederholen-mit-while — die Gleitkomma-Falle: x springt in 0,1-Schritten, die Lupe zeigt 0,9999999999999999 neben der 1 — die Schleife, die „nie endet“, ist ohne Bild nicht zu glauben

## Editor-Lücken

Für die 28 neuen Vorschläge (22 ohne neue Editor-Funktion machbar):
- L8: 2 (V7, V13; Zeilenmarke und Speicherzustand, jeweils mit Behelf Text-Zeilen + wanderndes Rechteck); optional hilfreich bei V15
- L1: 2 (V4 Schalter und Lampe müssen wieder ausgehen, V14 alter Zeiger müsste verschwinden); als Behelf zusätzlich bei V21, V26 (Marken, die springen)
- L9: 1 (V23, einzelne Ziffern einfärben); optional hilfreich bei V3 und V16 (Zellen einzeln betonen)
- L4: 0 (nur hilfreich bei V10, dort als zweite Achse gelöst)
- L-neu: 0
Für die vorhandenen Szenen: keine nötig; `k3rmittel` muss auf eine Σ-Operation mit anschließender Division umgebaut werden. L10 (Abspielknopf im Artikel) betrifft alle.

## Vorschläge

Hinweis zu allen Programmablauf-Bildern (L8): Es gibt kein Code-Objekt. Behelf in jedem Vorschlag: Codezeilen als je ein `Text` (Monospace) untereinander, ein halbtransparentes `Rectangle` als Zeilenmarke, das per `Shift` von Zeile zu Zeile springt (gleicher Schritt = gleichzeitig), daneben ein `TextBox`-Kasten „Variablen“ mit `Text`-Werten. Da nichts verschwinden kann (L1), wird ein geänderter Wert als neuer Text neben dem alten eingeblendet und der alte durchgestrichen (`Line` per Create) oder in einer Spalte darunter fortgeschrieben (Wertverlauf-Tabelle, die nach unten wächst).

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Drei Wege durch ein Programm (Zusammenschau)
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/01-entscheidungen-und-schleifen.md
- **Stelle:** Worum es geht — „Die Skripte aus Python 1 und Python 2 laufen von oben nach unten, und jede Zeile läuft genau einmal. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei Spuren übereinander, jede ein kleines Flussbild aus `TextBox`-Kästen mit `LabeledArrow`: (1) „bisher“: vier Kästen in Reihe; (2) „Entscheidung“: Raute „U > 5,25 V?“, Ja-Kasten „Warnung“, Nein-Weg daran vorbei, beide münden wieder; (3) „Wiederholung“: Raute „Ergebnis genau genug?“ mit Pfeil zurück nach oben. Rechts je Spur eine Zeile Klartext („jede Zeile genau einmal“, „je nach Daten ein Weg“, „Schritt wiederholen, bis das Ziel erreicht ist“). Ein kleiner `Dot` (Marke „Programm“) läuft.
- **Ablauf:** 1. Spur 1 baut sich auf (Kästen nacheinander FadeIn), der Dot läuft per `MoveAlongPath` durch alle vier. 2. Spur 2 erscheint, der Dot läuft zweimal: erst Ja-Weg über den Warnungs-Kasten, dann Nein-Weg daran vorbei (die Kästen, die übersprungen werden, bekommen kurz `Indicate`). 3. Spur 3: der Dot kreist drei Runden um die Schleife und verlässt sie durch den Nein-Pfeil. — Haltepunkte: Ende Schritt 2 (zwei Wege), Schritt 3 während der Runden.
- **Verständnisproblem:** Der Leser kennt nur „oben nach unten“ und sieht nicht, was „je nach Daten verschiedene Wege“ und „Schritte wiederholen“ als Ablauf heißt; das Bild liefert den Gesamtüberblick, auf den die Abschnitte 1 bis 9 aufbauen.
- **Szenenname:** prog/k3ueberblick
- **Editor-Lücke:** machbar (der Dot springt am Ende der drei Läufe nicht zurück an den Start: ohne L1 drei getrennte Dots oder MoveAlongPath mit geschlossener Bahn)

### Artikel 02 — Bedingungen: Vergleiche und logische Operatoren (Soll 5, vorh. 0)

### V2 [A] Verketteter Vergleich auf dem Zahlenstrahl
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/02-bedingungen-vergleiche-und-logische-operatoren.md
- **Stelle:** Verkettete Vergleiche — „**Zwei Marken auf dem Zahlenstrahl.** Die Kette $4{,}75\le U\le5{,}25$ enthält zwei Vergleiche, …“
- **Art:** neue Animation
- **Was zu sehen ist:** `NumberLine` von 4,5 bis 5,5 V mit Marken bei 4,75 und 5,25 (`Marker`), der Bereich dazwischen als `Band` grün getönt. Darüber `TextBox` mit `4.75 <= u <= 5.25`, geteilt in zwei Teilvergleiche „4.75 <= u“ und „u <= 5.25“. Ein `Dot` für `u` mit Beschriftung. Unter jedem Teilvergleich Platz für `Mark` (Haken/Kreuz) und rechts das Gesamtergebnis `True`/`False`.
- **Ablauf:** 1. Zahlenstrahl, Marken, Band, Ausdruck erscheinen. 2. `u = 5.1`: Dot erscheint bei 5,1; Teilvergleich 1 bekommt Haken, Teilvergleich 2 Haken, Ergebnis `True`. 3. Dot läuft (`MoveTo`) zu 5,4 hinter die obere Marke; Teilvergleich 1 bleibt Haken, Teilvergleich 2 bekommt Kreuz, Ergebnis `False`. 4. Dot läuft zu 4,6 links der unteren Marke: Teilvergleich 1 Kreuz, Teilvergleich 2 grau mit „nicht mehr geprüft“ (Kurzschluss, zeigt die Aussage in Definition 1.1). — Haltepunkte: 2, 3.
- **Verständnisproblem:** Dass die Kette zwei Vergleiche sind, die beide stimmen müssen, und dass der Bereich genau das Intervall zwischen den Marken ist.
- **Szenenname:** prog/k3kette
- **Editor-Lücke:** machbar (Haken/Kreuz nach dem Verschieben des Dots stehen lassen und für den nächsten Fall neu setzen ginge nur mit L1; Behelf: drei Zeilen untereinander, je ein Fall)

### V3 [A] Zeichenketten Zeichen für Zeichen vergleichen
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/02-bedingungen-vergleiche-und-logische-operatoren.md
- **Stelle:** Zeichenketten vergleichen — „**Wie im Wörterbuch.** Im Wörterbuch steht „Ohm“ vor „Volt“, weil schon der erste Buchstabe entscheidet. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Zeilen aus Zeichenkästchen (`Table` mit einer Zeile je Kette, Zellen = Zeichen), darunter die Unicode-Nummer je Zeichen. Eine Prüfmarke (`Rectangle`-Rahmen) über der aktuellen Spalte. Rechts Ergebnis des Vergleichs. Drei Fälle nacheinander: `"Ohm" < "Volt"`, `"Volt" < "Voltmeter"`, `"10" < "9"`.
- **Ablauf:** 1. Fall 1: Rahmen über Spalte 1, `O` (U+004F) gegen `V` (U+0056): ungleich, Nummern erscheinen, 0x4F < 0x56, Ergebnis `True`; die Spalten 2 und 3 bleiben grau („wird nicht mehr betrachtet“). 2. Fall 2: Rahmen wandert über `V`, `o`, `l`, `t`: je gleich (grüner Haken); die erste Kette ist zu Ende, die zweite hat noch `m`: kürzere ist kleiner, `True`. 3. Fall 3: `1` (U+0031) gegen `9` (U+0039): ungleich, `True`; daneben Einblendung „es sind Texte, keine Zahlen: 10 < 9 als Zahlen wäre False“. — Haltepunkte: Ende jedes Falls.
- **Verständnisproblem:** Dass nur das erste verschiedene Zeichen zählt und dass Text „10“ vor „9“ steht.
- **Szenenname:** prog/k3zeichenvergleich
- **Editor-Lücke:** machbar (L9 hilfreich: Zellen einzeln betonen; Behelf Rechteck über Zelle per Shift)

### V4 [A] and und or als Schalter in Reihe und parallel
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/02-bedingungen-vergleiche-und-logische-operatoren.md
- **Stelle:** Der Operator `and` und Der Operator `or` — „**Zwei Schalter in Reihe.** Eine Lampe hinter zwei Schaltern in Reihe leuchtet nur, wenn beide Schalter geschlossen sind. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Schaltpläne nebeneinander mit `Component`: links Spannungsquelle, Schalter `a`, Schalter `b` in Reihe, Lampe (`and`); rechts dieselben Teile mit parallelen Schaltern (`or`). Unter jedem Plan die Wahrheitstafel aus dem Artikel als `Table` (vier Zeilen, Spalten a, b, Ergebnis). Eine Rahmenmarke zeigt die aktuelle Kombination. Strompfeil (`Component` Strompfeil) nur, wenn die Lampe leuchtet.
- **Ablauf:** 1. Beide Pläne erscheinen mit offenen Schaltern. 2. Kombination `False/False`: Rahmen auf Zeile 1, beide Lampen dunkel. 3. `False/True`: Schalter b zeigt „geschlossen“ (Stellung), links bleibt dunkel, rechts leuchtet (Strom über b). 4. `True/False` ebenso. 5. `True/True`: links leuchtet jetzt auch, rechts leuchtet. — Haltepunkte: 3 (Unterschied and/or zeigt sich erst hier), 5.
- **Verständnisproblem:** Wahrheitstafeln sind ohne Bild Auswendiglernstoff; die Schalter erklären, warum `and` genau eine Zeile wahr hat und `or` genau eine falsch (ferner Grundlage für De Morgan in Aufgabe 3).
- **Szenenname:** prog/k3andor
- **Editor-Lücke:** braucht Editor-Funktion: L1 (Schalter öffnen und Lampe wieder dunkel, sonst nur vier Standbild-Paare nebeneinander oder Zustände über mehrere Schritte als wachsende Spalten)

### V5 [A] Kurzschlussauswertung: wo die Auswertung stehen bleibt
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/02-bedingungen-vergleiche-und-logische-operatoren.md
- **Stelle:** Die Kurzschlussauswertung — „**Wer die Antwort kennt, liest nicht weiter.** Ist in „A und B“ schon A falsch, ist das Ganze falsch, was immer B ist. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Ausdruck als zwei `TextBox`-Hälften, links `n != 0`, Mitte `and`, rechts `10 / n > 1`; darunter ein Zeiger (`Dot` mit `LabeledArrow` „Auswertung“), der von links läuft; eine Variablenzeile `n = 0`. Rechts ein Ergebnisfeld. Vier Zeilen untereinander (Zeilenversion statt Wechsel): (1) `n != 0 and 10 / n > 1` mit n = 0; (2) `10 / n > 1 and n != 0` mit n = 0; (3) `True or 1 / 0`; (4) `True and 1 / 0`.
- **Ablauf:** 1. Zeile 1: Zeiger prüft die linke Hälfte: `False`; das Ergebnis `False` erscheint sofort, die rechte Hälfte wird ausgegraut mit Stempel „nie berechnet“. 2. Zeile 2: Zeiger steht links bei `10 / n`: rotes `Mark` mit `ZeroDivisionError`, die rechte Hälfte wird nie erreicht. 3. Zeile 3 (`or`): linke Hälfte `True`, Ergebnis `True`, rechte Hälfte grau. 4. Zeile 4 (`and`): linke Hälfte `True`, der Zeiger muss weiter, `1 / 0` rot, Fehler. — Haltepunkte: 1 und 2 (Reihenfolge schützt), 4.
- **Verständnisproblem:** „Wird die rechte Seite ausgewertet?“ und warum die schützende Bedingung links stehen muss.
- **Szenenname:** prog/k3kurzschluss
- **Editor-Lücke:** machbar

### V6 [B] Welche Werte gelten als wahr?
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/02-bedingungen-vergleiche-und-logische-operatoren.md
- **Stelle:** Der Wahrheitswert von Objekten — „**Ist da etwas?** Die Regel folgt einer einfachen Frage: Ist in dem Wert etwas enthalten? …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links eine Spalte Wertkärtchen (`TextBox`): `0`, `0.0`, `""`, `None`, `False`, `"0"`, `" "`, `"False"`, `-1`, `1e-300`, `0.1 + 0.2 - 0.3`. Rechts zwei Körbe (`TextBox` hoch): „False“ (rot getönt) und „True“ (grün getönt). In der Mitte ein Trichter „bool(x)“.
- **Ablauf:** 1. Kärtchen und Körbe erscheinen. 2. Die vier „leeren“ Werte (`0`, `0.0`, `""`, `None`, dazu `False` selbst) wandern per `Shift` in den False-Korb. 3. `"0"`, `" "`, `"False"` wandern in den True-Korb, dazu eingeblendet „mindestens ein Zeichen“. 4. `-1`, `1e-300` und `0.1 + 0.2 - 0.3` (≈ 5,55·10⁻¹⁷) wandern in True, dazu „nicht Null“. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Dass nicht die Bedeutung des Inhalts („0“, „False“), sondern „null/leer oder nicht“ entscheidet.
- **Szenenname:** prog/k3wahrheitswert
- **Editor-Lücke:** machbar

(verworfen: Rangfolge `not`/`and`/`or` als Klammerbaum, Ergebnis von `and`/`or` als Operand: beide reine Regel- bzw. Tabellenstoffe, C)

### Artikel 03 — Entscheidungen: if, elif und else (Soll 5, vorh. 3)

### V7 [A] Ein Skript Zeile für Zeile durchlaufen (if/else) — ersetzt `prog/k3block`
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/03-entscheidungen-if-elif-und-else.md
- **Stelle:** Der Block und die Einrückung — „**Wie eine Gliederung.** In einer Gliederung rücken Unterpunkte ein; was weiter links steht, gehört nicht mehr dazu. …“
- **Art:** neue Animation (ersetzt die vorhandene Abbildung `prog/k3block`)
- **Was zu sehen ist:** Der Code aus `usb_block.py` als vier Textzeilen: `u = float(input("Spannung in V: "))`, `if u > 5.25:`, `    zuviel = u - 5.25`, `    print(...)`, `print("Messung beendet")`. Der Block (Zeilen 3 und 4) ist blau hinterlegt wie in `k3block`. Links eine Zeilenmarke (Rechteck). Rechts ein Kasten „Speicher“ mit `u`, `zuviel`, und darunter ein Kasten „Ausgabe“.
- **Ablauf:** 1. Code und blauer Block erscheinen (wie die bisherige Abbildung, jetzt Zeile für Zeile per `Write`). 2. Lauf mit `u = 5,4`: Marke auf Zeile 1, `u = 5.4` im Speicher; Marke auf Zeile 2, Bedingung `5.4 > 5.25` mit `True`; Marke in den Block: `zuviel = 0.15`, Ausgabe „Achtung: Spannung um 0.15 V zu hoch“; Marke auf die letzte Zeile, „Messung beendet“. 3. Zweiter Lauf mit `u = 5,0` (Spalte daneben): `5.0 > 5.25` ergibt `False`, die Marke springt über den blauen Block direkt zur letzten Zeile, die Blockzeilen bleiben grau; nur „Messung beendet“. — Haltepunkte: Marke an der Kopfzeile (Wahrheitswert), Sprung über den Block.
- **Verständnisproblem:** Zusammenhang zwischen Einrückung, Block und tatsächlichem Ablauf: „Block überspringen“ ist ohne Zeitverlauf abstrakt; zugleich Programmablauf mit Variablenzustand (auch für `else` und `elif` verwendbar).
- **Szenenname:** prog/k3ablaufif
- **Editor-Lücke:** braucht Editor-Funktion: L8 (Code-Objekt mit Zeilenmarke und Speicherzustand; Behelf: Text-Zeilen + wanderndes Rechteck, siehe Hinweis oben)

### V8 [B] `elif`-Kette schneidet den Zahlenstrahl in Bereiche
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/03-entscheidungen-if-elif-und-else.md
- **Stelle:** Mehrere Fälle: `elif` — „Die zweite Bedingung prüft nur die obere Grenze. Das genügt, weil Python sie nur erreicht, wenn die erste falsch war, …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine `NumberLine` 0 bis 6 V, darüber der Code aus `usb_elif.py` als drei Bedingungszeilen `if u < 4.75`, `elif u <= 5.25`, `else`. Marken bei 4,75 und 5,25. Drei farbige Bänder (`Band`): „zu niedrig“, „in Ordnung“, „zu hoch“, die sich zeigen sollen. Ein Dot `u`.
- **Ablauf:** 1. Zahlenstrahl und Code. 2. Bedingung 1 `u < 4.75`: alles links von 4,75 färbt sich als „zu niedrig“; der Rest wird als „weiter“ markiert. 3. Bedingung 2 `u <= 5.25` darf nur auf dem Rest arbeiten: Der Bereich 4,75 bis 5,25 färbt sich grün, ohne dass `u >= 4.75` im Code steht; die untere Grenze wird als „schon ausgeschieden“ (grauer Pfeil zur linken Marke) gezeigt. 4. `else`: der Rest rechts färbt sich. 5. Dot wandert zu 4,5, 5,1, 5,4 und zeigt jeweils, welche Zeile greift. — Haltepunkte: 3 (warum nur obere Grenze genügt), 5.
- **Verständnisproblem:** Warum `elif` ohne untere Grenze auskommt und warum die Reihenfolge wichtig ist (Aufgabe 6 setzt das voraus).
- **Szenenname:** prog/k3elifbereiche
- **Editor-Lücke:** machbar

### V9 [B] Der 12-Bit-Wandler als Treppe mit Unter- und Überlauf
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/03-entscheidungen-if-elif-und-else.md
- **Stelle:** Anwendung: ein Messbereich mit Unter- und Überlauf — „Ein Analog-Digital-Umsetzer (ADU) wandelt eine Spannung in eine ganze Zahl. …“
- **Art:** neue Animation
- **Was zu sehen ist:** `Axes` mit U von −0,5 V bis 5,5 V (x) und Code von 0 bis 4095 (y, in der Zeichnung bei Stufenzahl 4096). Treppenkennlinie (`DataCurve`, Treppe) im Bereich 0 bis 5 V; links von 0 V flach bei Code 0 (rot „Unterlauf“), rechts von 5 V flach bei 4095 (rot „Überlauf“). Marker bei (2,5 V, 2048) mit Beschriftung „800 hex“ und (1 V, 819). Die drei Bereiche entsprechen den drei Zweigen des Skripts `adu.py`.
- **Ablauf:** 1. Achsen und Treppe zeichnen sich (Create) von 0 bis 5 V. 2. Der Dot für `u = 2,5` wandert von der x-Achse zur Treppe hoch, Marker (2048). 3. `u = 1,0`: Marker (819), Zusatz „819,2 Stufen, abgerundet“. 4. `u = 5,2`: Dot geht rechts neben die Treppe, Anzeige „Überlauf: Code 4095“, der `elif`-Zweig leuchtet in der Beschriftung. 5. `u = −0,1`: Unterlauf links. — Haltepunkte: 2 und 4.
- **Verständnisproblem:** Dass Code und Spannung eine Treppe bilden (abgerundet) und dass die drei Fälle des Skripts drei Bereiche der Kennlinie sind.
- **Szenenname:** prog/k3adu
- **Editor-Lücke:** machbar


### Artikel 04 — Wiederholen mit while (Soll 4, vorh. 1)

### V10 [A] Die Gleitkomma-Falle: die 1 wird übersprungen
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/04-wiederholen-mit-while.md
- **Stelle:** Die Gleitkomma-Falle — „**Die 1 wird übersprungen.** Damit die Falle nicht wirklich endlos läuft, bekommt das Skript eine Notbremse: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben `NumberLine` von 0 bis 1,2 mit Marke bei 1,0 (rot, „Ziel x == 1.0“). Ein Dot `x` springt in Schritten von 0,1. Darunter eine zweite, stark vergrößerte Zahlengerade (Ausschnitt 0,99999999999999 bis 1,00000000000001, beschriftet „Lupe“) mit der Marke 1.0 und dem Punkt `0.9999999999999999`. Rechts eine wachsende Tabelle `durchlauf | x | x != 1.0`, wie die Ausgabe von `gleitkomma.py`.
- **Ablauf:** 1. Zahlengerade, Ziel, Tabellenkopf. 2. Durchläufe 1 bis 9: der Dot springt Marke für Marke, jede Zeile erscheint (3: `0.30000000000000004`, 8: `0.7999999999999999` jeweils rot hervorgehoben, weil die Rundung zählt). 3. Durchlauf 10: der Dot landet nicht auf 1,0, sondern knapp darunter; die Lupe öffnet sich, der Abstand zur Marke wird sichtbar; `x != 1.0` bleibt `True`. 4. Durchlauf 11: der Dot liegt rechts der Marke (`1.0999999999999999`): die 1 wurde übersprungen. 5. Zum Vergleich unten ein zweiter Streifen, der mit `k / 10` rechnet und bei Durchlauf 10 genau auf 1,0 trifft (Haken). — Haltepunkte: 3 (Lupe), 5.
- **Verständnisproblem:** Warum „solange x != 1.0“ nie falsch wird, obwohl man zehnmal 0,1 addiert; der Mechanismus (Rundung bei jeder Addition) ist sonst reiner Text.
- **Szenenname:** prog/k3gleitkomma
- **Editor-Lücke:** machbar (zweite Achse als Lupe statt Kamera-Zoom; L4 nur für echten Zoom)

### V11 [A] RC-Entladung Schritt für Schritt bis 1 %
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/04-wiederholen-mit-while.md
- **Stelle:** Anwendung: Wie lange sich ein Kondensator entlädt — „Für eine Schleife zerlegt man die Zeit in kleine Schritte Δt. …“
- **Art:** neue Animation
- **Was zu sehen ist:** `Axes` t von 0 bis 6 ms, u von 0 bis 5 V. Die exakte Kurve `5·exp(−t/τ)` (`FunctionGraph`, hellgrau, mit τ = 1 ms) und waagrechte Linie bei 0,05 V („1 %“). Punkte (`Dot`) bei t = k·Δt mit Δt = 0,1 ms, die die Schleife berechnet; daneben Anzeige `schritte` und `u`. Marker bei Schritt 46 (u ≈ 0,0505 V, knapp darüber) und 47 (0,0455 V, darunter).
- **Ablauf:** 1. Achsen, graue Kurve, 1-%-Linie. 2. Punkt für Punkt erscheinen die Schleifenwerte (Schritte 0, 1, 2, …), jeweils mit Pfeil „× e^(−Δt/τ) ≈ 0,905“ zwischen zwei Punkten, zuerst langsam (Schritte 1 bis 3), dann zügig bis 45. 3. Bei Schritt 46: Anzeige `u > 0.05` ist noch wahr, die Schleife läuft weiter. 4. Schritt 47: Der Punkt liegt unter der Linie, `u > 0.05` ist falsch, `schritte = 47`, Ausgabe „4,7 ms“; daneben die exakte Zeit τ·ln 100 = 4,605 ms als senkrechte Linie, der Abstand von höchstens einem Schritt wird sichtbar. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Dass die Schleife ein Ziel statt einer Anzahl hat (Zahl der Durchläufe vorher unbekannt) und dass jeder Durchlauf mit demselben Faktor multipliziert; der Leser sieht zudem, warum das Ergebnis höchstens einen Schritt hinter dem exakten Wert liegt.
- **Szenenname:** prog/k3rcschleife
- **Editor-Lücke:** machbar (Muster „Iteration als Folge von Erscheinen“)

### V12 [B] Endlosschleife: der Zähler bewegt sich nicht
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/04-wiederholen-mit-while.md
- **Stelle:** Die Endlosschleife — „**Ein Programm, das hängt.** Ändert der Block nichts an der Bedingung, prüft Python immer wieder dieselbe wahre Bedingung. …“
- **Art:** neue Animation (Gegenstück zu `prog/k3while`)
- **Was zu sehen ist:** Dasselbe Flussdiagramm wie `k3while` (Raute `zaehler <= 3`, Kasten `summe = summe + zaehler`) ohne Kasten `zaehler = zaehler + 1`, daneben ein Kasten „Speicher“ mit `zaehler = 1` (bleibt) und `summe` wachsend: 1, 2, 3, 4, …; ein Zähler „Prüfungen“. Ein Dot läuft im Kreis. Am Ende ein Strg+C-Symbol und `KeyboardInterrupt`.
- **Ablauf:** 1. Flussdiagramm baut sich auf; auffällig fehlt der Kasten für `zaehler + 1` (gestrichelter, leerer Platz). 2. Der Dot läuft: Prüfung 1 `1 <= 3` wahr, `summe = 1`; Prüfung 2: `1 <= 3` wahr (`zaehler` unverändert!), `summe = 2`; Prüfung 3 und 4 ebenso, die Prüfzahl zählt hoch, ab da rasch (Dot beschleunigt, „…“). 3. Strg+C: Dot stoppt, `KeyboardInterrupt` erscheint. — Haltepunkte: 2 (`zaehler` bleibt 1).
- **Verständnisproblem:** „Der Block muss die Bedingung ändern“; der Leser sieht, dass `zaehler` immer 1 bleibt, wo bei `zaehlen.py` die Spalte 1, 2, 3, 4 lief.
- **Szenenname:** prog/k3endlos
- **Editor-Lücke:** machbar

### Artikel 05 — Zählen mit for und range (Soll 4, vorh. 1)

### V13 [A] Die Schleifenvariable wandert durch `range(5)`
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/05-zahlen-mit-for-und-range.md
- **Stelle:** Die `for`-Schleife — „**Ein Stufenschalter.** Man kann sich einen Stufenschalter vorstellen, der Stellung für Stellung weiterdreht: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben `range(5)` als fünf `TextBox`-Kästchen 0 1 2 3 4 (Stufenschalter). Darunter der Code von `zweierpotenzen.py` (`for k in range(5):`, `    print(k, 2 ** k)`, `print("fertig")`), links die Zeilenmarke. Rechts ein Kasten „k = …“ und eine wachsende Ausgabe (`0 1`, `1 2`, `2 4`, `3 8`, `4 16`, `fertig`).
- **Ablauf:** 1. Kästchen und Code. 2. Pro Durchlauf: Ein Zeiger (`LabeledArrow` „k“) zeigt auf das Kästchen, k erhält diesen Wert, die Zeilenmarke geht in den Block, die Ausgabezeile erscheint, dann springt die Marke zurück zur Kopfzeile, der Zeiger rückt eins weiter. 3. Nach Kästchen 4: Der Zeiger läuft hinter das letzte Kästchen; die Marke geht zur Zeile `print("fertig")`; Ausgabe „fertig“. Eingeblendet: „keine Bedingung, die Folge ist zu Ende“. — Haltepunkte: Durchlauf 1, Schluss.
- **Verständnisproblem:** Was die Schleifenvariable ist, wer sie setzt und wann die Schleife endet (ohne Zähler, Bedingung, Erhöhen).
- **Szenenname:** prog/k3forlauf
- **Editor-Lücke:** braucht Editor-Funktion: L8 (Behelf: Zeilenmarke per Shift, siehe Hinweis oben)

### V14 [B] Warum `i = 100` den nächsten Durchlauf nicht stört
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/05-zahlen-mit-for-und-range.md
- **Stelle:** `for` oder `while`? — „Ein Unterschied überrascht oft: Bindet man in einer `for`-Schleife die Schleifenvariable an einen anderen Wert, …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben die Folge `range(3)` als drei Kästchen 0, 1, 2 (der Vorrat der Schleife, ein Zeiger „nächstes Element“). Darunter ein Etikett „i“ als Zettel mit Pfeil (`LabeledArrow`) zu einem Wertkästchen. Rechts die Ausgabe von `schleifenvariable.py`.
- **Ablauf:** 1. Durchlauf 1: Der Vorrat gibt `0` heraus, der Pfeil von `i` zeigt auf 0, Ausgabe „Anfang des Durchlaufs: 0“. 2. Zeile `i = 100`: Ein neues Kästchen „100“ erscheint, der Pfeil von `i` wird auf 100 umgehängt (neuer Pfeil, alter durchgestrichen), Ausgabe „nach i = 100: 100“. Der Zeiger im Vorrat rückt unabhängig davon auf 1. 3. Durchlauf 2: `i` wird neu an die 1 gebunden (Pfeil springt auf 1), Ausgabe „Anfang des Durchlaufs: 1“; das Kästchen 100 bleibt zurück. 4. Dritter Durchlauf ebenso mit 2. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Dass ein Name nur ein Etikett ist, das die `for`-Schleife in jedem Durchlauf neu aus der Folge anheftet; eigene Zuweisungen ändern die Folge nicht.
- **Szenenname:** prog/k3schleifenvariable
- **Editor-Lücke:** braucht Editor-Funktion: L1 (alter Pfeil müsste verschwinden; Behelf: durchgestrichen)

(verworfen: Zeitachse mit Aufaddieren gegen Zähler: dieselbe Rundungsfalle ist in V10 als Bild, im Artikel dorthin verweisen, C)

### Artikel 06 — Schleifen steuern, verschachteln und Ergebnisse sammeln (Soll 5, vorh. 2)

### V15 [A] `break` und `continue` an einer Reihe von Durchläufen
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/06-schleifen-steuern-verschachteln-und-ergebnisse-sammeln.md
- **Stelle:** Abbrechen mit `break` — „**Wer den Schlüssel gefunden hat, sucht nicht weiter.** Wer Schubladen der Reihe nach nach einem Schlüssel durchsucht, …“ (und Überspringen mit `continue`)
- **Art:** neue Animation (zwei Spuren in einer Szene)
- **Was zu sehen ist:** Spur oben (`break`, aus `kleinster_teiler.py`, n = 91): Kästchen t = 2, 3, 4, 5, 6, 7, 8, 9 (bis √91 ≈ 9,5), darunter pro Kästchen `91 % t`: 1, 1, 3, 1, 1, **0**, 3, 1. Spur unten (`continue`, aus `kanaele.py`): Kästchen Kanal 0 bis 7, Ausgabezeile „messe Kanal …“. Ein Zeiger läuft.
- **Ablauf:** 1. Spur oben: Der Zeiger geht von t = 2 bis 7, bei jedem Kästchen erscheint `91 % t`; bei t = 7 wird die 0 rot, `teiler = 7`, `break` als gebogener roter Pfeil, der aus der Schleife hinaus nach rechts führt; t = 8 und 9 werden grau („werden nicht mehr geprüft“); Ausgabe `91 = 7 * 13`. 2. Spur unten: Der Zeiger läuft Kanal 0, 1, 2 (Ausgaben erscheinen); bei Kanal 3 ist `kanal == 3` wahr: `continue` als kurzer Bogen über das Kästchen hinweg zum Kanal 4, die Ausgabe für 3 bleibt aus; Kanal 4 bis 7 normal, danach „fertig“. — Haltepunkte: 1 bei t = 7, 2 bei Kanal 3.
- **Verständnisproblem:** Unterschied zwischen „Schleife verlassen“ (`break`) und „diesen Durchlauf auslassen“ (`continue`), im Ablauf sichtbar statt nur beschrieben.
- **Szenenname:** prog/k3steuern
- **Editor-Lücke:** machbar (Pfeilbögen mit `LabeledArrow`/`LoopArrow`; L8 bei der Codeanzeige hilfreich, aber nicht nötig)

### V16 [A] Verschachtelte Schleifen als Gitter
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/06-schleifen-steuern-verschachteln-und-ergebnisse-sammeln.md
- **Stelle:** Verschachtelte Schleifen — „**Wie bei einer Uhr.** Der Minutenzeiger läuft einmal ganz herum, dann rückt der Stundenzeiger eine Stunde weiter, …“
- **Art:** neue Animation (Gitter 3×4 aus dem Text als Prozess, ergänzt um das Dreieck aus `parallel_suche.py`)
- **Was zu sehen ist:** Links ein Gitter aus `Table` 3 Zeilen × 4 Spalten (Zeile 0 bis 2, Spalte 0 bis 3), zunächst leer; zwei Zeiger: „äußere Schleife“ am linken Rand (Zeile), „innere Schleife“ am oberen Rand (Spalte). Rechts ein zweites Gitter mit r1 = 100 bis 900 (Zeilen) und r2 = 100 bis 900 (Spalten), von dem nur das Dreieck r2 ≥ r1 gefüllt wird, mit den zwei Treffern (200/600) und (300/300) in Grün.
- **Ablauf:** 1. Das 3×4-Gitter: Zeiger Zeile 0; der innere Zeiger läuft Spalte 0 bis 3, in jeder Zelle erscheint die Zählung 1, 2, 3, 4. Dann springt der äußere Zeiger auf Zeile 1, der innere fängt wieder bei Spalte 0 an: 5 bis 8; Zeile 2: 9 bis 12. 2. Rechts: dasselbe Prinzip für r1 und r2; die Zeile r1 = 100 hat neun Zellen, r1 = 200 acht, … bis r1 = 900 eine; so entsteht ein Dreieck, die Zählung „45 Paare statt 81“ erscheint; die beiden Treffer leuchten. — Haltepunkte: Ende von Zeile 0 (innere Schleife läuft ganz durch), das fertige Dreieck.
- **Verständnisproblem:** „Die innere läuft bei jedem Durchlauf der äußeren ganz durch“ und m·n bzw. die Dreieckszahl 45; ohne Bild ist die Reihenfolge der Durchläufe (zeilenweise) eine reine Behauptung.
- **Szenenname:** prog/k3gitter
- **Editor-Lücke:** machbar (L9 hilfreich: Zellen einzeln betonen; Behelf Rechteck per Shift)

### V17 [B] Das Maximum sammeln: `beste_p` steigt nur bei einem größeren Wert
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/06-schleifen-steuern-verschachteln-und-ergebnisse-sammeln.md
- **Stelle:** Anwendung: Mittelwert und Maximum — „**Das Maximum.** Eine Quelle mit der Leerlaufspannung U0 und dem Innenwiderstand Ri treibt …“
- **Art:** neue Animation
- **Was zu sehen ist:** `Axes` R von 0 bis 200 Ω, P von 0 bis 0,6 W. Die 20 Rasterpunkte R = 10, 20, …, 200 mit `P = 100·R/(R+50)²` (R = 10: 0,278 W; R = 50: 0,500 W; R = 200: 0,320 W). Eine waagrechte Linie `beste_p` und ein Zeiger-Marker `beste_r`. Optional blasse exakte Kurve P(R) (`FunctionGraph`).
- **Ablauf:** 1. Achsen und Kurve (blass). 2. Die Punkte R = 10, 20, … erscheinen nacheinander (Dot); jedes Mal wird `p > beste_p` geprüft: Bei R = 10 bis 50 steigt die Linie `beste_p` (neues Maximum, Marker hüpft mit), ab R = 60 liegt `p` unter der Linie (graue Punkte, Linie bleibt). 3. Ende: Linie bei 0,500 W, `beste_r = 50`; senkrechte Hilfslinie bei R = Ri = 50 Ω. — Haltepunkte: R = 50 (Gipfel), 60 (erster kleinerer Wert).
- **Verständnisproblem:** Wie ein Akkumulator „Maximum“ funktioniert: nicht jeder Durchlauf ändert ihn, nur ein größerer Wert; und warum der Startwert `0.0` genügt.
- **Szenenname:** prog/k3maximum
- **Editor-Lücke:** machbar

### Artikel 07 — Lösungen durch Probieren: Raten und Prüfen, Näherung mit Toleranz (Soll 3, vorh. 0)

### V18 [A] Raten und Prüfen: g läuft, bis g·g die Zahl erreicht
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/07-losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.md
- **Stelle:** Raten und Prüfen — „**Ein Zahlenschloss.** Bei einem Zahlenschloss mit drei Ziffern kann man alle Kombinationen von 000 bis 999 der Reihe nach probieren. …“
- **Art:** neue Animation
- **Was zu sehen ist:** `Axes` g von 0 bis 9 (x), g·g von 0 bis 81 (y). Die Parabel g² als `FunctionGraph` (blass) und die Punkte (0,0), (1,1), (2,4), …, (8,64) als `Dot` bei ganzen g. Eine waagrechte Linie bei a (Beschriftung `a`). Ein Kasten „Schleife“ mit `g` und der Prüfung `g * g < a`. Zwei Läufe: a = 49 und a = 50.
- **Ablauf:** 1. Achsen, Parabel, Linie bei a = 49. 2. g = 0, 1, …, 6: jeder Punkt erscheint, die Prüfung `g * g < a` zeigt `True` (grüner Haken), g wächst um 1. 3. g = 7: der Punkt (7, 49) liegt auf der Linie, `g * g < a` ist `False`, die Schleife endet, `g * g == a`: „Wurzel: 7 nach 7 Schritten“. 4. Zweiter Lauf mit a = 50: Linie wandert auf 50, g = 7 → 49 < 50 wahr, g = 8 → 64 > 50, die Schleife endet, `g * g == a` falsch: „keine ganzzahlige Wurzel, geprüft bis 8“. — Haltepunkte: Ende von 3 und von 4. Am Ende ein Hinweis „Schritte ≈ √a“ mit 10¹² → 10⁶ Schritte.
- **Verständnisproblem:** Wie die Schleife endet (erstes g mit g² ≥ a), dass sie dann zwei Fälle unterscheiden muss, und warum die Zahl der Schritte mit √a wächst.
- **Szenenname:** prog/k3raten
- **Editor-Lücke:** machbar

### V19 [A] Der Graben: kleine und zu große Schritte der Schrittweite h
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/07-losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.md
- **Stelle:** Schrittweite und Toleranz — „**Ein schmaler Graben.** Die Werte von $g$, die die Toleranz einhalten, bilden einen schmalen Bereich um $\sqrt a$, …“ (mit der Näherung mit Toleranz davor)
- **Art:** neue Animation
- **Was zu sehen ist:** Vergrößerter Ausschnitt `Axes`: g von 4,990 bis 5,010 (x), g·g von 24,90 bis 25,10 (y). Die Parabel g² als nahezu gerader Anstieg, die waagrechte Linie bei a = 25, darum ein `Band` von 24,99 bis 25,01 (Toleranz ε = 0,01); darunter auf der x-Achse der Graben von 4,999 bis 5,001 grün markiert (`Brace`, „Breite ≈ ε/√a = 0,002“). Zwei Streifen untereinander (zwei Axes oder eine Axes mit zwei Punktfolgen in verschiedenen Farben): Schrittweite h = 0,0001 und h = 0,003.
- **Ablauf:** 1. Ausschnitt, Linie, Toleranzband, Graben. 2. Fall h = 0,0001: Punkte bei 4,9990 … laufen in 0,0001-Schritten Richtung Graben; die Bedingung `abs(g*g - a) >= eps` ist wahr, bis ein Punkt (4,9990) im Band landet: Haken, „Näherung 4.999 nach 49 990 Schritten“. 3. Fall h = 0,003: Punkte bei 4,998 (g² = 24,980 unter dem Band) und 5,001 (g² = 25,010 knapp über dem Band; der Grabenrand liegt bei 5,001): beide verfehlen das Band; die zweite Schleifenbedingung `g * g <= a` wird falsch, die Schleife endet mit „übersprungen“. Der Sprung über den Graben wird mit einem gebogenen `LabeledArrow` gezeigt. — Haltepunkte: Bild vom Graben, Sprung in Schritt 3.
- **Verständnisproblem:** Warum die Schrittweite kleiner als die Breite des Bereichs sein muss und wozu die zweite Bedingung dient; ohne Bild ist „über den Graben treten“ nur ein Gleichnis. Zugleich zeigt der Vergleich 49 990 Schritte, warum das Verfahren teuer ist.
- **Szenenname:** prog/k3graben
- **Editor-Lücke:** machbar (zweiter Streifen als zweite Axes; echter Zoom wäre L4, hier als Ausschnitt gelöst)

### Artikel 08 — Die Bisektion (Soll 4, vorh. 1)

### V20 [A] Zwischenwertsatz: wer von unten nach oben zeichnet, kreuzt die Achse
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/08-die-bisektion.md
- **Stelle:** Was du dafür brauchst: der Zwischenwertsatz — „Anschaulich: Wer ohne abzusetzen von unterhalb der $x$-Achse nach oberhalb zeichnet, muss sie irgendwo kreuzen. …“
- **Art:** vorhandene Szene wiederverwenden (hm1/k5nullstelle; vorher Inhalt der Szene prüfen, sonst neue Szene nach folgendem Plan)
- **Was zu sehen ist:** Im Plan der Neuzeichnung: `Axes` x von 0 bis 2, y von −2 bis 2.5; `FunctionGraph` f(x) = x² − 2; Punkte (0, −2) und (2, 2) mit Beschriftung `f(0) < 0`, `f(2) > 0`; Nullstelle bei √2 als roter Dot.
- **Ablauf:** 1. Achsen und die zwei Punkte. 2. Die Kurve zeichnet sich (`Create`) von links unten nach rechts oben „ohne abzusetzen“, ein Stift-Dot (`MoveAlongPath`) läuft mit. 3. Sobald er die x-Achse überquert, leuchtet der Schnittpunkt (`Indicate`), Beschriftung „x* mit f(x*) = 0“. 4. Zum Gegenbeispiel: eine unstetige Kurve mit Sprung über die Achse (zweiter Graph, Stück 1 endet unter der Achse, Stück 2 beginnt darüber), der Stift hebt ab, kein Schnittpunkt. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Der Satz klingt selbstverständlich; die Voraussetzung „stetig“ (kein Absetzen) wird erst am Gegenbeispiel greifbar.
- **Szenenname:** hm1/k5nullstelle (Wiederverwendung) oder prog/k3zws
- **Editor-Lücke:** machbar

### V21 [A] Die Bisektion am Graphen: lo, hi, Mitte und das Vorzeichen von f(m)
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/08-die-bisektion.md
- **Stelle:** Das Bisektionsverfahren — „**Zahlenraten mit „größer oder kleiner“.** Jemand denkt sich eine Zahl zwischen 1 und 100 …“
- **Art:** neue Animation (ergänzt die Intervallschachtelung `prog/k3bisektion`; hier der Funktionsgraph dazu)
- **Was zu sehen ist:** `Axes` x von 0 bis 2, y von −2 bis 2; Graph f(x) = x² − 2; grüne Marken `lo` und `hi` (`Marker` mit Hilfslinie) auf der x-Achse; senkrechte gestrichelte Linie für die Mitte `m`, ein Punkt `(m, f(m))` auf der Kurve; daneben Anzeige `lo`, `hi`, `m`, `m*m < a` und die Intervallbreite. Rechts eine Tabelle, die zeilenweise nach dem Artikel gefüllt wird (Schritt, lo, hi, m, m²).
- **Ablauf:** 1. Start lo = 0, hi = 2: f(lo) = −2 (rot, unter der Achse), f(hi) = 2 (grün). 2. Schritt 1: m = 1; der Punkt (1, −1) erscheint unter der Achse, `f(m) < 0` ⇒ `lo = 1` (Marke `lo` springt nach rechts, linke Intervallhälfte wird abgedunkelt). 3. Schritt 2: m = 1,5, f = 0,25 > 0 ⇒ `hi = 1,5`; Schritt 3: m = 1,25, f < 0 ⇒ `lo = 1,25`; Schritt 4: m = 1,375 ⇒ `lo`; Schritt 5: m = 1,4375, f > 0 ⇒ `hi`; Schritt 6: m = 1,40625 ⇒ `lo`. 4. Das Intervall schrumpft sichtbar um die Nullstelle (rot, √2), die Breite 0,03125 erscheint. — Haltepunkte: Schritt 1 (was bedeutet das Vorzeichen), Schritt 2 (Marke wechselt die Seite), Ende.
- **Verständnisproblem:** Die Verbindung zwischen dem Programm (`if mitte * mitte < a`), dem Vorzeichen von f an der Mitte und der Frage „links oder rechts von der Nullstelle?“; die Schachtelung allein zeigt nur Intervalle, nicht den Grund für die Wahl der Hälfte.
- **Szenenname:** prog/k3bisektiongraph
- **Editor-Lücke:** machbar (Marker auf Kurve vorhanden; die springenden Marken werden pro Schritt als neue Marken eingeblendet, die alten abgeblendet, weil Verschwinden fehlt: L1 als Behelf)

### V22 [B] Wie schnell sinkt die Schrittzahl mit der Genauigkeit?
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/08-die-bisektion.md
- **Stelle:** Die Schrittzahl der Bisektion — „41 und 12: Diese Zahlen lassen sich vor dem Start ausrechnen.“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine untereinander gestapelte Balkenfolge (`Rectangle`) der Intervallbreiten L, L/2, L/4, … mit L = 2, jeder Balken halb so lang wie der vorige; rechts die Zahl n und die Breite `2/2ⁿ`. Daneben ein kleines `Axes`-Diagramm: Genauigkeit ε (log) gegen Schritte n, Gerade n = log₂(L/ε) mit den zwei Punkten (ε = 10⁻¹², n = 41) und (für L = 25, ε = 0,01) n = 12.
- **Ablauf:** 1. Der Balken der Länge 2 erscheint. 2. Jeder Schritt erzeugt einen halb so langen Balken darunter, bis n = 6 (0,03125) im Takt, dann beschleunigt bis n = 41. 3. Die Gerade im Diagramm zeichnet sich, die zwei Beispielpunkte erscheinen; Beschriftung „Zehnmal genauer ≈ 3,3 Schritte mehr“. — Haltepunkte: n = 6 (Bezug zur Tabelle), Gerade.
- **Verständnisproblem:** Dass die Schrittzahl logarithmisch mit der Genauigkeit wächst; die Formel ⌈log₂(L/ε)⌉ ist im Text, ein Gefühl für „41 statt 2·10¹²“ fehlt.
- **Szenenname:** prog/k3schrittzahl
- **Editor-Lücke:** machbar

### Artikel 09 — Das Newton-Verfahren (Soll 5, vorh. 2)

### V23 [A] Quadratische Konvergenz: die richtigen Stellen verdoppeln sich
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/09-das-newton-verfahren.md
- **Stelle:** Die Wurzel durch Newton — „Fünf Schritte statt 41. Die richtigen Stellen wachsen sichtbar: eine nach Schritt 1 (`1.5`), drei nach Schritt 2 (`1.416`), …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Tabelle (`Table`) mit den Zeilen der Ausgabe von `wurzel_newton.py`: Schritt 1: `1.5`, Schritt 2: `1.4166666666666667`, Schritt 3: `1.4142156862745099`, Schritt 4: `1.4142135623746899`, Schritt 5: `1.4142135623730951`, darüber der Referenzwert `1.4142135623730951` (√2). Daneben eine Spalte „richtige Stellen“: 1, 3, 6, 12, alle.
- **Ablauf:** 1. Der Referenzwert steht oben. 2. Zeile für Zeile erscheint der Näherungswert; in jeder Zeile wird der mit dem Referenzwert übereinstimmende Anfang grün hinterlegt (Schritt 1: `1.`; Schritt 2: `1.41`…; es zählen die Stellen laut Text), der Rest rot. 3. Neben der Zeile wachsen Balken der Länge 1, 3, 6, 12 (verdoppelt, Pfeile „×2“). — Haltepunkte: Schritt 2 (drei Stellen), Schritt 4 (zwölf).
- **Verständnisproblem:** „Fehler quadriert sich“ klingt abstrakt; hier sieht man, dass die grüne Spanne jedes Mal ungefähr doppelt so lang wird. Zugleich Gegenüber zur Bisektion (ein Bit je Schritt).
- **Szenenname:** prog/k3stellen
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Zellen/Ziffern einzeln einfärben; Behelf: Rechtecke über Ziffern oder zwei `Text`-Teile je Zeile in zwei Farben)

### V24 [A] Wo Newton versagt: waagrechte Tangente und Kreislauf
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/09-das-newton-verfahren.md
- **Stelle:** Die Grenzen des Newton-Verfahrens — „**Die Steigung ist null.** Ist $f'(g)=0$, ist die Tangente waagerecht und schneidet die Achse nicht. …“
- **Art:** neue Animation (zwei Teilbilder)
- **Was zu sehen ist:** Links: `Axes`, Parabel x² − 2, Punkt (0, −2), waagrechte Tangente (`TangentLine`), kein Schnittpunkt mit der x-Achse, Beschriftung „f′(0) = 0: Division durch 0“. Rechts: `Axes` x von −2 bis 2, Graph f(x) = x³ − 2x + 2 (einzige reelle Nullstelle bei ≈ −1,77), Punkte (0, 2) und (1, 1).
- **Ablauf:** 1. Links: der Punkt auf der Parabel bei g = 0; die Tangente erscheint waagrecht (`Create`), die Strecke zur Achse fehlt; Fehlermeldung `ZeroDivisionError`. 2. Rechts: Start bei x = 0: die Tangente (Steigung −2, f = 2) schneidet die x-Achse bei x = 1; senkrechter Pfeil zum Punkt (1, 1) auf der Kurve. 3. Die Tangente bei x = 1 (Steigung 1, f = 1) schneidet die Achse bei x = 0; Pfeil zurück zum Start. 4. Ein Zähler „Schritt 1, 2, 3, 4, …“ wechselt zwischen 1,0 und 0,0; Beschriftung „kreist; die Nullstelle bei −1,77 wird nie erreicht“. — Haltepunkte: 2 und 3.
- **Verständnisproblem:** Warum Newton ohne Garantie ist; der Kreislauf (`Schritt 2: x = 0.0`) wirkt in der Ausgabe als Rätsel, die zwei Tangenten zeigen den Mechanismus.
- **Szenenname:** prog/k3newtongrenzen
- **Editor-Lücke:** machbar

### V25 [B] Weit weg vom Ziel: Halbieren statt Verdoppeln
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/09-das-newton-verfahren.md
- **Stelle:** Die Grenzen des Newton-Verfahrens — „**Weit weg ist es langsam.** Quadratische Konvergenz gilt erst nahe der Nullstelle. …“
- **Art:** neue Animation
- **Was zu sehen ist:** `NumberLine` von 0 bis 26 mit Marke bei 5 (√25). Die Schätzungen 25, 13, 7,46, 5,41, 5,015, 5,000023 als Dots mit Sprungpfeilen (`LabeledArrow`) von Schätzung zu Schätzung; über den ersten Pfeilen „ungefähr halbieren“, über den letzten „Stellen verdoppeln sich“. Darunter eine Zeile mit dem Fehler: 20, 8, 2,46, 0,41, 0,015, 0,000023.
- **Ablauf:** 1. Zahlenstrahl und Start 25. 2. Schritte 1 bis 3: lange Sprünge, die jedes Mal etwa auf die Hälfte der Schätzung führen. 3. Ab Schritt 4 verkürzen sich die Sprünge rapide (Lupe um die 5), der Fehler fällt auf 0,015 und dann auf 2·10⁻⁵. — Haltepunkte: Schritt 3, Schritt 5.
- **Verständnisproblem:** Warum die schnelle Konvergenz einen Startwert nahe der Lösung verlangt.
- **Szenenname:** prog/k3newtonweit
- **Editor-Lücke:** machbar

### Artikel 10 — Anwendung: der Arbeitspunkt einer Diode (Soll 3, vorh. 1)

### V26 [A] Die Bisektion halbiert das Intervall der Spannung
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/10-anwendung-der-arbeitspunkt-einer-diode.md
- **Stelle:** Der Arbeitspunkt durch Bisektion — „Die Bisektion braucht nur das Vorzeichen von $f$ und das Startintervall $[0,U_0]$. …“
- **Art:** neue Animation
- **Was zu sehen ist:** `Axes` U von 0 bis 5 V, Strom von −5 bis 5 mA; die Funktion `f(U) = (5 − U)/1000 − 10⁻¹²·(e^{U/0,02585} − 1)` als `FunctionGraph` (steil fallend ab 0,6 V, für den Plot unter −5 mA abgeschnitten, Beschriftung „weiter nach unten“). Marken `lo = 0`, `hi = 5`, die Mitte als gestrichelte Linie; die Zeile `f > 0 ?` mit Haken oder Kreuz.
- **Ablauf:** 1. Achsen, Kurve (Nullstelle bei 0,5741 V, rot markiert). 2. Schritt 1: m = 2,5 V: f(m) < 0 (Diodenstrom riesig) ⇒ `hi = 2,5`; Schritt 2: m = 1,25 ⇒ `hi`; Schritt 3: m = 0,625 ⇒ f(0,625) < 0 (Diodenstrom ≈ 32 mA gegen 4,4 mA im Widerstand) ⇒ `hi = 0,625`; Schritt 4: m = 0,3125 ⇒ f > 0 ⇒ `lo = 0,3125`. 3. Weitere Schritte schneller (Intervall wird kleiner als die Linienbreite; Lupe um 0,574 V). 4. Nach 43 Schritten: `U = 0,574147 V`, I = 4,4259 mA. Zusatz: der Eintrag „⌈log₂(5/10⁻¹²)⌉ = 43“. — Haltepunkte: 1 (Vorzeichenregel vertauscht gegenüber der Wurzel), 4.
- **Verständnisproblem:** Dass die Fälle im Code gegenüber der Wurzel vertauscht sind (f(lo) > 0) und was `f > 0` physikalisch heißt: Der Widerstand liefert mehr Strom, also liegt der Arbeitspunkt höher.
- **Szenenname:** prog/k3diodebisektion
- **Editor-Lücke:** machbar (Marker pro Schritt neu; L1 Behelf wie in V21)

### V27 [B] Newton von weit weg kriecht in Schritten von U_T
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/10-anwendung-der-arbeitspunkt-einer-diode.md
- **Stelle:** Der Arbeitspunkt durch Newton — „Mit einem Startwert in der Nähe, 0,7 V, braucht Newton 10 Schritte. Von $U_0=5$ V aus sind es 177, …“
- **Art:** neue Animation
- **Was zu sehen ist:** `Axes`: Schritt n von 0 bis 180 (x), Spannung U von 0 bis 5 V (y). Die Kurve der Newton-Iterierten für den Start 5 V (fällt ab 5 V annähernd linear, pro Schritt etwa 25,85 mV, bis nach ≈ 171 Schritten 0,57 V erreicht ist, dann ein Knick) und für den Start 0,7 V (springt in 10 Schritten auf 0,574 V). Horizontale Linie bei 0,574 V.
- **Ablauf:** 1. Achsen, Zielllinie. 2. Start 0,7 V: die kurze Kurve zeichnet sich (`Create`), 10 Schritte, Ziel erreicht. 3. Start 5 V: die lange Kurve zeichnet sich langsam entlang der fast geraden Strecke; eine Lupe (Beschriftung) zeigt, dass jeder Schritt nur U_T = 25,85 mV tiefer führt; am Knick bei ≈ 171 Schritten verdichten sich die Punkte, die letzten Schritte sind schnell: 177 gesamt. 4. Als Vergleich: Marke „Bisektion: 43 Schritte“ als senkrechte Linie. — Haltepunkte: Lupe, Knick.
- **Verständnisproblem:** Warum Newton von weit weg langsamer ist als die Bisektion, obwohl er nahe der Lösung viel schneller ist.
- **Szenenname:** prog/k3newtondiode
- **Editor-Lücke:** machbar (Verlaufskurven als DataCurve; die genauen Werte werden bei der Szenenerstellung aus dem Skript gerechnet)

### Artikel 11 — Das Wichtigste bis hier (Soll 1, vorh. 0)

### V28 [A] Zusammenschau: drei Verfahren, ein Bereich der Unsicherheit
- **Artikel:** content/prog/03-entscheidungen-und-schleifen/11-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt aus zwei Gedanken: … jedes Näherungsverfahren ist eine Schleife, die einen Bereich der Unsicherheit verkleinert, …“
- **Art:** vorhandene Szene wiederverwenden (prog/k3fehler aus Artikel 09 als Animation; ersatzweise die Intervallschachtelung `prog/k3bisektion`)
- **Was zu sehen ist:** Wie in V-zu-k3fehler: Fehler über Schritten, logarithmisch, drei Kurven (Schrittverfahren, Bisektion, Newton), Toleranzlinie.
- **Ablauf:** Die drei Kurven zeichnen sich nacheinander, Haltepunkt bei jeder: Schrittverfahren (kaum Abfall), Bisektion (Gerade), Newton (steiler werdend, bricht ab). Eine Zeile daneben ordnet je Kurve die Aussage der Tabelle darunter zu („ein Stück h“, „ein Bit je Schritt“, „Fehler wird quadriert“).
- **Verständnisproblem:** Der Zusammenhang „wie schnell, hängt davon ab, wie viel ein Schritt über die Lösung erfährt“, gebunden an ein einziges Bild.
- **Szenenname:** prog/k3fehler (Wiederverwendung)
- **Editor-Lücke:** machbar

## Vorhandene Abbildungen

- prog/k3if (03-entscheidungen-if-elif-und-else.md): animieren ja — Schritte: 1. Raute und beide Kästen erscheinen; 2. ein Dot läuft für `u = 5,4` über Ja-Weg durch den Warnungskasten; 3. zweiter Lauf `u = 5,0` über den Nein-Weg am Kasten vorbei (Kasten bleibt grau); beide Wege münden gemeinsam | Lücke: machbar (zwei Dots statt Rückkehr: L1).
- prog/k3block (03-entscheidungen-if-elif-und-else.md): entfällt, aufgegangen in V7 (Block-Hinterlegung wird dort Zeile für Zeile aufgebaut und läuft als Ablauf).
- prog/k3elif (03-entscheidungen-if-elif-und-else.md): animieren ja — Schritte: 1. Fragenkette baut sich auf; 2. ein Dot für `u = 4,5` hält an der ersten Raute, nimmt Ja, andere Kästen grau; 3. `u = 5,1`: Nein, Ja an der zweiten; 4. `u = 5,4`: Nein, Nein, `else` | Lücke: machbar.
- prog/k3while (04-wiederholen-mit-while.md): animieren ja — Schritte: 1. Diagramm; 2. Dot läuft vier Prüfungen (zaehler 1, 2, 3, 4) mit der Tabelle aus dem Artikel, die Zeilen erscheinen im Takt; 3. letzte Prüfung `4 <= 3` falsch, Dot verlässt die Schleife; Ausgabe „fertig, zaehler = 4“ | Lücke: machbar.
- prog/k3range (05-zahlen-mit-for-und-range.md): animieren ja — Schritte: 1. Zahlenstrahl mit Start 2; 2. Marken 5, 8 erscheinen nacheinander mit Schritt-Pfeilen (+3); 3. die nächste Marke 11 erscheint gestrichelt mit „Stopp, gehört nicht dazu“; zweiter Streifen `range(10, 0, -3)`: 10, 7, 4, 1 und die gestrichelte 0er-Marke | Lücke: machbar.
- prog/k3rquadrate (06-schleifen-steuern-verschachteln-und-ergebnisse-sammeln.md): ist bereits eine echte Σ-Operation (`Summation`): animieren ja, wie im Editor — Summand für Summand, Zwischenstände 1, 5, 14, 30, 55 | Lücke: machbar.
- prog/k3rmittel (06-schleifen-steuern-verschachteln-und-ergebnisse-sammeln.md): nur ein statischer `MathTex`, keine Operation. Umbau als Σ-Operation über die vier Messwerte 4,98, 5,02, 5,01, 4,99 (Summe 20,00) und anschließend die Division durch 4 (Arithmetik-Operation), Ergebnis 5,000 V | Lücke: machbar.
- prog/k3bisektion (08-die-bisektion.md): animieren ja — Schritte: 1. Startintervall [0, 2] mit roter gestrichelter √2; 2. jede Zeile der Schachtelung erscheint nacheinander mit der Mitte und dem Hervorheben der neuen Hälfte, Zeilen 1 bis 6 (Breite 2 bis 0,03125); 3. weitere Zeilen im Takt | Lücke: machbar (zusammen mit V21 in einer Szene möglich).
- prog/k3newton (09-das-newton-verfahren.md): animieren ja — Schritte: 1. Parabel x² − 2 und √2; 2. Punkt bei g0 = 2, Tangente (`TangentLine`) zeichnet sich bis zur Achse, g1 = 1,5; 3. senkrecht zum Punkt auf der Kurve, zweite Tangente bis g2 = 1,41667 | Lücke: machbar.
- prog/k3fehler (09-das-newton-verfahren.md): animieren ja — Schritte: 1. logarithmische Achsen; 2. Kurve Schrittverfahren; 3. Bisektion mit Gerade; 4. Newton, endet nach Schritt 4 | Lücke: machbar.
- prog/k3diode (10-anwendung-der-arbeitspunkt-einer-diode.md): animieren ja — Schritte: 1. Achsen; 2. Kennlinie zeichnet sich, steil ansteigend; 3. Arbeitsgerade; 4. Schnittpunkt als Dot mit `U = 0,574 V`, `I = 4,43 mA`; dazu optional Pfeil für den Überschuss f(U) bei U = 0,6 V (Widerstandsstrom 4,4 mA unter Diodenstrom 12 mA) | Lücke: machbar.

Übergeordnet: Alle elf vorhandenen Szenen sind statisch (`animations` leer). Mehr als fünf Abbildungen hat kein Artikel.
