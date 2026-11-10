# Abbildungen und Animationen — Paket ml_4 (Heft ml/04-wahrscheinlichkeit)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.
Deutsche Artikel 01–15. 20 Szenen `ml/k4…` vorhanden. Davon 12 „Rechenbilder“ (k4r…): nur k4rmuenzen ist eine echte Editor-Operation (`DotProduct`), die übrigen 11 sind ein einziger statischer `MathTex`. Konzeptbilder: k4baum, k4dichte, k4vertfkt, k4normal, k4streu, k4ellipsen, k4lln, k4zgws (Axes/DataCurve/Stem/Dot/TextBox). Keine Szene hat eine Zeitachse.

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-wahrscheinlichkeit | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-zufall-und-ereignisse | 2 | 0 | 2 | 0 | 0 | 0 | 2 |
| 03-wahrscheinlichkeit-2 | 3 | 0 | 3 | 0 | 0 | 0 | 3 |
| 04-bedingte-wahrscheinlichkeit | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 05-der-satz-von-bayes | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 06-unabhangigkeit | 2 | 0 | 2 | 0 | 0 | 0 | 2 |
| 07-zufallsvariablen-und-verteilungen | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 08-erwartungswert-und-varianz | 5 | 4 | 1 | 0 | 0 | 0 | 5 |
| 09-wichtige-verteilungen | 5 | 1 | 3 | 1 | 0 | 0 | 5 |
| 10-mehrere-zufallsvariablen | 4 | 0 | 3 | 1 | 0 | 0 | 4 |
| 11-kovarianz-und-korrelation | 4 | 3 | 1 | 1 | 0 | 0 | 5 |
| 12-zufallsvektoren-und-die-kovarianzmatrix | 4 | 2 | 2 | 0 | 0 | 0 | 4 |
| 13-die-mehrdimensionale-normalverteilung | 4 | 2 | 1 | 1 | 0 | 0 | 4 |
| 14-mittelwerte-vieler-zufallsvariablen | 4 | 2 | 2 | 0 | 0 | 0 | 4 |
| 15-das-wichtigste-bis-hier | 2 | 0 | 1 | 1 | 0 | 0 | 2 |
| **Summe** | 49 | 20 | 25 | 5 | 0 | 0 | 50 |

Eine einzige Überschreitung (Artikel 11, +1, V22 begründet). Alle anderen Artikel liegen genau auf dem Soll. Nicht in die Liste aufgenommen (verworfen, siehe Hinweise bei den Artikeln): Riemann-Summen (07), Streuung/Standardisieren in 08, Bernoulli-Varianz, kategorische Verteilung, Rauschen (09), Bayes als Umgewichten (05), Paritätsbits (06), Bedingen als wandernder Schnitt und Ellipsenanteil (13).

## Top 3

- V8 [A] 05-der-satz-von-bayes — Basisrate: dasselbe Prüfgerät bei 0,1 / 1 / 10 / 50 % Defekten, Flächenbild der Alarme — der Basisratenfehler ist der wichtigste Denkfehler des Kapitels und steht nur in einer Tabelle
- V17 [A] 10-mehrere-zufallsvariablen — gemeinsame Dichte x + y, Streifen für Streifen zur Randverteilung (und zugleich das Doppelintegral) — Marginalisieren hat ohne Bild keine Anschauung; Abschnitt 10 ist ohne jede Abbildung
- V23 [A] 12-zufallsvektoren-und-die-kovarianzmatrix — Schatten der Punkte auf eine drehende Gerade, Varianz als Kurve mit Maximum und Minimum bei den Eigenvektoren — zeigt, warum die Kovarianzmatrix die Streuung in jeder Richtung kennt und was die Hauptachsen sind

Auffällig: Die Artikel 01, 02, 03, 06, 10 und 15 haben bisher keine einzige Abbildung; in Artikel 03 (Axiome, Additionssatz, Laplace) und 06 (Unabhängigkeit) fehlt jede Anschauung.

## Editor-Lücken

Für die 30 neuen Vorschläge (12 ganz ohne neue Editor-Funktion machbar: V1, V3, V5, V6, V9, V10, V11, V12, V20, V21, V28, V30):
- L1: 4 (V2, V7, V8, V29; überall mit Notbehelf Überdeckung/Übermalen lösbar)
- L2: 3 (V15, V18, V25; Kurve wird Kurve; Notbehelf: Zustände nacheinander)
- L3: 5 (V15, V16, V17, V18, V23; Parameter oder Schnittlinie als Zeit) + 1 hilfreich (V22)
- L4: 1 (V26; Kamera drehen)
- L5: 2 (V24, V25; Matrix auf Punktwolke)
- L6: 3 (V8, V19, V27; Stichproben/viele bewegte Punkte) + 3 hilfreich (V4, V13, V14)
- L7: 1 (V14; Histogramm wächst als Prozess)
- L9: 1 (V7; Tabellenzellen betonen)
- L-neu: 0

Für die vorhandenen Szenen: L7 bei k4rkovmatrix, k4rrichtung (Matrix · Matrix, quadratische Form); L3 bei k4normal, k4ellipsen; L2 bei k4zgws; L6 bei k4streu; L1 bei k4rverkettung. L10 (Abspielknopf im Artikel) betrifft alle.

Rechenbilder: Von den 12 Rechenbildern k4r… ist nur k4rmuenzen eine echte Editor-Operation (DotProduct). Die anderen 11 (k4rverkettung, k4rtotal, k4rbayes, k4rwuerfel, k4rquadrat, k4rvarianz, k4rkovarianz, k4rdaten, k4rkovmatrix, k4rrichtung, k4rmahalanobis) sind ein einziger statischer MathTex und sollten auf Σ / ∏ / DotProduct / Arithmetik umgebaut werden. Fehlende Pflicht-Rechenbilder (neu vorgeschlagen): V10 (∏ 0,95^10). Bei den Rechenbeispielen in Artikel 02, 03 (nur Mengen und Brüche), 05 Tabelle 2 und 09 (Binomial 0,95^10, 10·0,05·0,95^9) gibt es keine eigenen Σ/∏-Operationen; die Binomialzahlen sind in V13 enthalten.

Doppelungen mit anderen Modulen: V7 ↔ hm3 (V17 in hm3_c, `hm3/k8wuerfel`), V9/V20 ↔ `hm3/k8mosaik`, V12 ↔ `hm3/k8schwerpunkt`, V13 ↔ `hm3/k8poisson`, V14 ↔ `hm3/k8dichte`, V28 ↔ `hm3/k8tscheb`, k4lln/k4zgws ↔ `hm3/k8mittel`, `hm3/k8zgs`. Die ml-Fassung bleibt eigenständig, soweit die Beispiele des Hefts (Sonne/Rad, Prüfgerät, Würfel) andere Zahlen haben; wo die Szene gleich wäre, ist Wiederverwendung angegeben.

## Vorschläge

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Vom Rauschen zur Glocke (Zusammenschau des Kapitels)
- **Artikel:** content/ml/04-wahrscheinlichkeit/01-wahrscheinlichkeit.md
- **Stelle:** Worum es geht — „Daten sind nie ganz sicher. Misst man dieselbe Spannung zweimal …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zahlenstrahl (NumberLine) „Messwert in V“ von 4,90 bis 5,10, darüber eine Axes für Häufigkeit (0 bis 8). Zwölf Messpunkte (Dots) für dieselbe Spannung, z. B. 4,97 / 5,02 / 5,00 / 4,99 / 5,04 / 4,96 / 5,01 / 5,00 / 4,98 / 5,03 / 5,00 / 5,01. Drei Textmarken, die jeweils eine Kapitelfrage tragen: „typischer Wert“, „Streuung“, „Form der Schwankung“.
- **Ablauf:** 1. Zahlenstrahl erscheint, ein Messpunkt bei 5,02 (Text „Messung 1“). 2. Zweiter Punkt bei 4,97: „Messung 2: anderer Wert“. 3. Die übrigen zehn Punkte erscheinen nacheinander und stapeln sich zu Säulen (Rectangles erscheinen je Messwertklasse). 4. Eine senkrechte Linie bei 5,00 (Marker, „typischer Wert“) und ein Brace über die Breite („Streuung“). 5. Eine glatte Glockenkurve (FunctionGraph, Mitte 5,00, Breite ≈ 0,03) wird über die Säulen gezeichnet („Form der Schwankung“). — Haltepunkte: 3 (Säulen stehen), 5.
- **Verständnisproblem:** Der Leser hat noch kein Bild, wozu das Kapitel dient; die fünf Eingangsfragen (typischer Wert, Streuung, gemeinsames Schwanken, immer gleiche Form) bleiben abstrakt. Hinweis: Das Bild nimmt Begriffe nur als Wörter vorweg, rechnet nichts.
- **Szenenname:** ml/k4ueberblick
- **Editor-Lücke:** machbar (schrittweises Erscheinen; „Histogramm wächst“ als Erscheinen von Rechtecken, besser mit L7)

### Artikel 02 — Zufall und Ereignisse (Soll 2, vorh. 0)

### V2 [A] Würfel-Ergebnisraum und Mengenoperationen
- **Artikel:** content/ml/04-wahrscheinlichkeit/02-zufall-und-ereignisse.md
- **Stelle:** Was du dafür brauchst: Mengen — „Eine Menge ist eine Zusammenfassung von Dingen …“ (Rechenbeispiel A={2,4,6}, B={5,6})
- **Art:** neue Animation
- **Was zu sehen ist:** Großes Rechteck Ω mit sechs Punkten 1 bis 6 (Beschriftung), darin eine Ellipse A um 2, 4, 6 (blau) und eine Ellipse B um 5, 6 (orange), die sich bei der 6 überlappen. Rechts eine Textzeile, die sich mit jedem Schritt ändert.
- **Ablauf:** 1. Ω und die sechs Punkte erscheinen. 2. Ellipse A (blau) wird gezeichnet, Text „A = {2, 4, 6}“. 3. Ellipse B (orange), Text „B = {5, 6}“. 4. Schnitt: die 6 wird betont (Indicate), Text „A ∩ B = {6} (und)“. 5. Vereinigung: 2, 4, 5, 6 werden grün hinterlegt, „A ∪ B = {2, 4, 5, 6} (oder)“. 6. Komplement: 1, 3, 5 werden rot hinterlegt, „A^c = {1, 3, 5} (nicht)“. 7. Erste De-Morgan-Regel: Punkte 1, 3 als „weder A noch B“ markiert, „(A ∪ B)^c = A^c ∩ B^c = {1, 3}“. — Haltepunkte: 4, 5, 7.
- **Verständnisproblem:** Vereinigung, Schnitt, Komplement bleiben Symbole; der Leser muss „oder/und/nicht“ erst auf Punktmengen übertragen. Alle späteren Ereignisse (Abschnitt 3 bis 6) sind solche Mengen.
- **Szenenname:** ml/k4mengen
- **Editor-Lücke:** braucht Editor-Funktion: L1 (Verschwinden; die Hervorhebungen der Schritte 4 bis 7 müssten sonst übereinander gelegt werden, machbar mit getrennten Farbüberlagerungen, die nacheinander erscheinen)

### V3 [A] Die 36 Ergebnisse zweier Würfel
- **Artikel:** content/ml/04-wahrscheinlichkeit/02-zufall-und-ereignisse.md
- **Stelle:** Zufallsexperiment und Ergebnisraum — „Beim Wurf zweier unterscheidbarer Würfel, eines roten und eines blauen, ist ein Ergebnis ein Paar (a, b) …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes (Gitter) mit Achse „rot a“ 1..6 und „blau b“ 1..6; 36 Punkte (Dots) in einem 6×6-Raster. Text „#Ω = 6·6 = 36“.
- **Ablauf:** 1. Erste Zeile (a = 1, sechs Punkte) erscheint, dann Zeile 2, …, Zeile 6, nacheinander (Zähler „6, 12, …, 36“). 2. Die Punkte (1,2) und (2,1) werden betont und beschriftet: „rot 1, blau 2“ bzw. „rot 2, blau 1“, Text „verschiedene Ergebnisse“. 3. Ereignis „Augensumme 7“: die Nebendiagonale (6 Punkte) wird farbig, Text „A“. 4. Ereignis „roter Würfel zeigt 6“: die Zeile a = 6 wird farbig, Text „B“; der Schnittpunkt (6,1) wird betont. — Haltepunkte: 1 (36), 2, 4.
- **Verständnisproblem:** Warum der Ergebnisraum 36 und nicht 21 oder 11 Elemente hat und dass ein Ereignis eine Teilmenge dieses Gitters ist. Dieselbe Szene wird in Aufgabe 1 und in Abschnitt 3 (V6) weiterverwendet.
- **Szenenname:** ml/k4ergebnisraum
- **Editor-Lücke:** machbar

### Artikel 03 — Wahrscheinlichkeit (Soll 3, vorh. 0)

### V4 [A] Relative Häufigkeit pendelt sich ein
- **Artikel:** content/ml/04-wahrscheinlichkeit/03-wahrscheinlichkeit-2.md
- **Stelle:** Die relative Häufigkeit — „Wie wahrscheinlich ein Ereignis ist, zeigt sich, wenn man das Experiment oft wiederholt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben ein Streifen „Würfe 1, 2, 3, …“ mit den Augenzahlen, unten Axes: x = Anzahl Würfe n (0 bis 60), y = h_n(„gerade“) (0 bis 1), gestrichelte Linie bei 0,5. Die Kurve h_n ist fest vorberechnet (festgelegte Folge, z. B. g,u,g,g,u,u,g,u,g,g, … so gewählt, dass h_10 = 0,7, h_20 = 0,45, h_60 ≈ 0,52). Zähler „n_A / n = 9/20 = 0,45“ ändert sich.
- **Ablauf:** 1. Die ersten 10 Würfe erscheinen im Streifen, die Kurve wird bis n = 10 gezeichnet (Create), springt stark. 2. Weiter bis n = 20: Text „9 von 20 gerade: h = 0,45“ (das Beispiel des Artikels), Punkt auf der Kurve betont. 3. Weiter bis n = 60: Kurve glättet sich, Ausschläge werden kleiner. 4. Zweite Kurve (anderes Experiment, andere Wurffolge, andere Farbe) wird gezeichnet: anders in den ersten Würfen, ähnlich am Ende. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Der Satz „sie schwankt, aber immer weniger“ und die Idee, dass eine Wahrscheinlichkeit das ist, worauf sich h_n einpendelt, hat ohne Bewegung keine Anschauung. Das Bild zeigt nur das Einpendeln, nicht die Rate (die kommt in Abschnitt 13, dort ml/k4lln).
- **Szenenname:** ml/k4haeufigkeit
- **Editor-Lücke:** braucht Editor-Funktion: L6 hilfreich (viele gezogene Werte), machbar mit DataCurve (Create) und einem Punkt per MoveAlongPath

### V5 [A] Additionssatz: die Überlappung nicht doppelt zählen
- **Artikel:** content/ml/04-wahrscheinlichkeit/03-wahrscheinlichkeit-2.md
- **Stelle:** Rechenregeln — „Aus den drei Axiomen folgen die Regeln, mit denen man tatsächlich rechnet. Sie entsprechen der Anschauung, dass Wahrscheinlichkeit sich wie ein Flächeninhalt verhält …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Streifen der Länge 1 (Ω), in sechs gleiche Felder zu je 1/6 geteilt (Würfelaugen 1 bis 6). Darunter zwei weitere Streifen: A = {2,4,6} (blau) und B = {5,6} (orange). Eine Skala 0 bis 1 mit Beschriftung P.
- **Ablauf:** 1. Streifen Ω (Länge 1, „P(Ω) = 1“) erscheint, Felder werden eingezeichnet. 2. A erscheint als Felder 2, 4, 6, Klammer „P(A) = 3/6“. 3. B erscheint als Felder 5, 6, „P(B) = 2/6“. 4. Beide Streifen werden hintereinander gelegt (Shift): Gesamtlänge 5/6, Feld 6 ist doppelt belegt (rot hervorgehoben): „3/6 + 2/6 = 5/6 zählt die 6 zweimal“. 5. Das doppelt belegte Feld 6 wird einmal abgezogen: Klammer „− P(A ∩ B) = −1/6“, Ergebnis „P(A ∪ B) = 4/6“; die vier Felder 2, 4, 5, 6 auf dem Ω-Streifen werden markiert. 6. Gegenereignis: Felder 1, 3 rot, „P(A ∪ B)^c = 1 − 4/6 = 2/6“. — Haltepunkte: 4, 5.
- **Verständnisproblem:** Warum der Schnitt abgezogen wird; „Wahrscheinlichkeit verhält sich wie Flächeninhalt“ ist im Text nur ein Satz. Hinweis: Das Bild ist eine Rechnung mit Brüchen (Arithmetik), keine Σ/∏-Rechnung im Kern; Rechenbild-Pflicht greift deshalb nicht.
- **Szenenname:** ml/k4addition
- **Editor-Lücke:** machbar

### V6 [A] Die Augensumme: nicht alle Ausgänge gleich wahrscheinlich
- **Artikel:** content/ml/04-wahrscheinlichkeit/03-wahrscheinlichkeit-2.md
- **Stelle:** Gleich wahrscheinlich Ergebnisse (Warnung) — „Beim Wurf zweier Würfel ist die Augensumme eine der Zahlen 2, …, 12 …“
- **Art:** vorhandene Szene wiederverwenden (ml/k4ergebnisraum aus V3, ergänzt um Summenbalken)
- **Was zu sehen ist:** Das 6×6-Raster aus V3 (a rot, b blau) links, rechts eine Axes: x = Augensumme 2 bis 12, y = Anzahl der Paare 0 bis 6 (bzw. Wahrscheinlichkeit in 36stel). Die Diagonalen a + b = const sind farbig.
- **Ablauf:** 1. Das Raster steht. 2. Diagonale a + b = 2 (ein Punkt) wird farbig, Balken bei 2 wächst auf 1 („1/36“). 3. Diagonale a + b = 3 (zwei Punkte), Balken 2. 4. So weiter bis Summe 7 (sechs Punkte, Balken 6, „6/36 = 1/6“, betont). 5. Diagonalen 8 bis 12 bauen die Balken 5, 4, 3, 2, 1 ab (nur wieder auf), Dreieck-Form sichtbar; Text „elf Ausgänge, nicht gleich wahrscheinlich; die 36 Paare schon“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Der häufigste Laplace-Fehler: elf Summen als gleich wahrscheinlich anzusehen. Das Bild zeigt, wie sich 36 gleiche Paare ungleich auf elf Summen verteilen. Die Verteilung wird in Abschnitt 7 (Zufallsvariablen) weiterverwendet, kein Vorgriff.
- **Szenenname:** ml/k4summen
- **Editor-Lücke:** machbar (Stem/Balken, die erscheinen); „Histogramm wächst“ eleganter mit L7

### Artikel 04 — Bedingte Wahrscheinlichkeit (Soll 3, vorh. 2)

### V7 [A] Bedingen heißt: den Ergebnisraum auf eine Zeile verkleinern
- **Artikel:** content/ml/04-wahrscheinlichkeit/04-bedingte-wahrscheinlichkeit.md
- **Stelle:** Bedingte Wahrscheinlichkeit — „Angenommen, man weiß schon, dass heute die Sonne scheint …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Quadrat (Fläche 1 = 200 Tage), aufgeteilt wie Tabelle 1 als Mosaik: oben Sonne (Höhe 0,4), darin links Fahrrad (Breite 0,75 von der Zeile, Fläche 0,3, „60“) und rechts kein Fahrrad (0,1, „20“); unten Regen (Höhe 0,6), darin Fahrrad 0,1 („20“), kein Fahrrad 0,5 („100“). Daneben die Tabelle selbst mit Zahlen.
- **Ablauf:** 1. Mosaik erscheint Feld für Feld (Tabellenzellen leuchten gleichzeitig mit dem Feld auf), Zahlen 60, 20, 20, 100. 2. „Wir erfahren: Sonne.“ Die Regenzeile wird ausgeblendet bzw. grau überdeckt (Rechteck erscheint darüber). 3. Die Sonnenzeile wird auf volle Höhe gestreckt (Scale), Text „neuer Ergebnisraum = 80 Tage“. 4. Anteil Fahrrad in dieser Zeile: Klammer „60 von 80 = 0,75“; Formel P(A|B) = P(A∩B)/P(B) = 0,3/0,4 erscheint. 5. Dasselbe für „Regen“: die Sonnenzeile wird überdeckt, die Regenzeile gestreckt, „20 von 120 = 1/6“. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Warum man durch P(B) teilt und was „der Ergebnisraum schrumpft“ bedeutet; ohne Bild bleibt die Definition ein Bruch.
- **Szenenname:** ml/k4einschraenken
- **Editor-Lücke:** braucht Editor-Funktion: L1 (Verschwinden der Regenzeile; Notbehelf: graue Überdeckung), L9 (Tabellenzellen einzeln betonen; Notbehelf: Rechtecke darüber)

### Artikel 05 — Der Satz von Bayes (Soll 3, vorh. 2)

### V8 [A] Basisrate: dasselbe Gerät, vier Populationen
- **Artikel:** content/ml/04-wahrscheinlichkeit/05-der-satz-von-bayes.md
- **Stelle:** Die Basisrate — „Das Prüfgerät erkennt 99 % der Defekte und irrt sich bei intakten Teilen nur in 5 % der Fälle, und trotzdem …“ (Tabelle 2)
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Quadratraster aus 100 × 100 Punkten (10 000 Teile). Links eine Skala „Basisrate P(D)“. Rechts ein Feld „Alarme“ (leer), darin später rote Punkte (echte Alarme) und graue Punkte (Fehlalarme). Unter dem Feld der Anteil „P(D|W) = rot / (rot + grau)“.
- **Ablauf:** 1. Basisrate 0,1 %: 10 Teile sind defekt (rot), 9 990 intakt; ins Alarmfeld wandern 9,9 → 10 rote und 499,5 → ≈ 500 graue Punkte (gerundet; bei Dezimalstellen „≈“): Anteil Rot „1,9 %“. 2. Basisrate 1 %: 100 rote, rote Alarme 99, graue 495, „16,7 % = jeder sechste“ (Wert des Artikels). 3. 10 %: rote 990, graue 450, „68,8 %“. 4. 50 %: rote 4 950, graue 250, „95,2 %“. Der Rot-Anteil im Alarmfeld wird jeweils als Balken (0 bis 100 %) eingeblendet. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Warum ein gutes Gerät bei seltenen Defekten fast nur Fehlalarme liefert (Basisratenfehler). Die Tabelle gibt Zahlen, das Bild die Flächen: selten mal viele ergibt viele. Ergänzt den Baum k4baum, der nur den Fall 1 % zeigt.
- **Szenenname:** ml/k4basisrate
- **Editor-Lücke:** braucht Editor-Funktion: L6 (viele bewegte Punkte; Notbehelf: Gruppen als Rechtecke mit Zahlenbeschriftung, Bereichsgröße = Anzahl). Verschwinden (L1) für den Wechsel zwischen den vier Zuständen; Notbehelf: vier Teilbilder nacheinander erscheinen.

verworfen (05): „Bayes als Umgewichten“ (Balken Ausgangswahrscheinlichkeit 60/40 → mal Wahrscheinlichkeit der Beobachtung 0,01/0,03 → normiert 1/3, 2/3) [B]; über dem Soll, der Fabrik-Fall steht bereits im Rechenbeispiel.

### Artikel 06 — Unabhängigkeit (Soll 2, vorh. 0)

### V9 [A] Unabhängig = Fläche ist Länge mal Breite
- **Artikel:** content/ml/04-wahrscheinlichkeit/06-unabhangigkeit.md
- **Stelle:** Unabhängige Ereignisse — „Ein Ereignis B sagt nichts über A, wenn die Information „B ist eingetreten“ die Wahrscheinlichkeit von A nicht ändert …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Einheitsquadrate nebeneinander. Links (Würfel, A = {2,4,6}, B = {1,2}): waagerechte Teilung bei 1/2 (A oben), senkrechte bei 1/3 (B links); Schnittrechteck 1/2 · 1/3 = 1/6. Rechts (Tabelle 1 des Kapitels, Sonne/Fahrrad): Sonne-Höhe 0,4, Fahrrad-Breite 0,4; das Produkt wäre 0,16, die echte Fläche ist 0,3.
- **Ablauf:** 1. Linkes Quadrat: Streifen A (Höhe 1/2) erscheint. 2. Streifen B (Breite 1/3) erscheint. 3. Der Schnitt wird farbig, Text „P(A) · P(B) = 1/2 · 1/3 = 1/6 = P(A ∩ B)“; die Zeile „P(B|A) = 1/3 = P(B)“ mit Hinweis, dass der Anteil von B in der Zeile A derselbe wie im ganzen Quadrat ist (die Teilung geht gerade durch). 4. Rechtes Quadrat: dieselben Streifen Sonne (0,4) und Fahrrad (0,4), erwartete Produktfläche 0,16 gestrichelt; die tatsächliche Fläche 0,3 (grün) ragt darüber hinaus, Text „0,3 ≠ 0,16: abhängig“. 5. Unvereinbar: ein drittes kleines Quadrat, in dem A und B keinen gemeinsamen Teil haben: „P(A∩B) = 0, Produkt > 0: nicht unabhängig“. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Das Produktkriterium ist eine Formel ohne Anschauung; dass unabhängig ≠ unvereinbar ist, ergibt sich aus dem Bild (Ausschluss = keine Schnittfläche) sofort.
- **Szenenname:** ml/k4unabh
- **Editor-Lücke:** machbar

### V10 [A] Rechenbild: kein Ausfall bei zehn unabhängigen Bauteilen
- **Artikel:** content/ml/04-wahrscheinlichkeit/06-unabhangigkeit.md
- **Stelle:** Mehrere unabhängige Ereignisse (Rechenbeispiel 1) — „Zehn Bauteile fallen unabhängig voneinander mit je 5 % Wahrscheinlichkeit aus …“
- **Art:** neue Animation (Editor-Operation ∏, danach „1 − …“)
- **Was zu sehen ist:** Produkt-Rechenbild (Operation ∏, zehn Faktoren 0,95), Zwischenprodukte 0,95 → 0,9025 → 0,857 → … → 0,599; danach eine Zeile „1 − 0,599 = 0,401“. Daneben zehn Kreise (Bauteile), grün, bei „ausgefallen“ rot.
- **Ablauf:** 1. Zehn Bauteile (Kreise) erscheinen, alle „funktioniert“ mit 0,95. 2. Das Produkt wächst Faktor für Faktor, der Zwischenwert sinkt sichtbar. 3. Ergebnis „0,95^10 ≈ 0,599“. 4. „mindestens eines fällt aus“: 1 − 0,599 = 0,401. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Dass viele einzeln harmlose Risiken zusammen groß werden (6 % Ausfall je Teil, 40 % für das System) ist eine Zahl, die man sehen muss.
- **Szenenname:** ml/k4rausfall
- **Editor-Lücke:** machbar (Operation ∏ vorhanden)

verworfen (06): Paritätsbits als Würfel der vier Fälle (paarweise, aber nicht gegenseitig unabhängig) [B]; über dem Soll.

### Artikel 07 — Zufallsvariablen und Verteilungen (Soll 3, vorh. 2)

### V11 [A] Eine Zufallsvariable ordnet Ergebnissen Zahlen zu
- **Artikel:** content/ml/04-wahrscheinlichkeit/07-zufallsvariablen-und-verteilungen.md
- **Stelle:** Zufallsvariablen — „Wirft man eine Münze dreimal, ist ein Ergebnis eine Folge wie (K, Z, K) aus Kopf und Zahl …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links eine Spalte mit den acht Ergebnissen KKK, KKZ, KZK, ZKK, KZZ, ZKZ, ZZK, ZZZ (je 1/8). Rechts ein Zahlenstrahl 0, 1, 2, 3 „Wert von X (Anzahl Köpfe)“. Darunter Axes für „P(X = x)“ von 0 bis 0,4.
- **Ablauf:** 1. Die acht Ergebnisse erscheinen nacheinander. 2. Von jedem Ergebnis läuft ein Pfeil zur Zahl auf dem Strahl (KKK → 3, die drei Ergebnisse mit zwei Köpfen → 2, …); die Pfeile sind farbig nach Zielzahl. 3. Die Pfeile, die bei 2 ankommen, werden betont, Text „{X = 2} = {KKZ, KZK, ZKK}“. 4. Über jeder Zahl wächst ein Stab, so hoch wie die Anzahl der Pfeile mal 1/8: 1/8, 3/8, 3/8, 1/8; Text „P(X = x) = Summe der 1/8“. — Haltepunkte: 2, 3.
- **Verständnisproblem:** „weder zufällig noch eine Variable, sondern eine feste Funktion“: Ohne Bild bleibt X eine Formel. Das Bild zeigt außerdem, wie die Wahrscheinlichkeitsfunktion (Stabdiagramm in Abb. 5) überhaupt entsteht, bevor sie dort als fertiges Bild erscheint.
- **Szenenname:** ml/k4zufallsvariable
- **Editor-Lücke:** machbar

verworfen (07): „Integral als Grenzwert von Rechtecksummen“ (Riemann, f(x)=2x, n = 2, 4, 16) [B]; steht als Hilfsabschnitt im Artikel, ist in einem früheren Heft Standardstoff und über dem Soll.

### Artikel 08 — Erwartungswert und Varianz (Soll 5, vorh. 4)

### V12 [A] Erwartungswert als Schwerpunkt (Wippe)
- **Artikel:** content/ml/04-wahrscheinlichkeit/08-erwartungswert-und-varianz.md
- **Stelle:** Der Erwartungswert — „Anschaulich ist der Erwartungswert der Schwerpunkt der Verteilung: Legt man auf einen Stab an jede Stelle x_k ein Gewicht P(X = x_k) …“
- **Art:** neue Animation (Doppelung prüfen: `hm3/k8schwerpunkt` zeigt dasselbe Auflager-Bild für eine Dichte und für Stäbe mit E(S) = 5; sie kann wiederverwendet werden, wenn ihre Zahlen zum Heft passen. Für ml wird eine eigene Szene mit den Gewichten des Würfels vorgeschlagen, weil das Heft den Würfel und die Köpfe-Verteilung als Leitbeispiele nutzt; der Aufbau ist derselbe.)
- **Was zu sehen ist:** Ein waagerechter Stab (Line) auf dem Zahlenstrahl von 0 bis 7 mit den Gewichten des fairen Würfels (sechs gleiche Klötze bei 1 bis 6), darunter ein Dreieck als Unterstützungspunkt (Keil), der verschoben werden kann. Text „E[X] = 3,5“.
- **Ablauf:** 1. Stab und die sechs Gewichte erscheinen. 2. Keil bei x = 2: der Stab neigt sich nach rechts (Rotate um den Keil), Text „kippt nach rechts“. 3. Keil bei x = 5: kippt nach links. 4. Keil wandert (Shift) auf 3,5: Stab waagerecht, Text „Gleichgewicht: E[X] = 3,5 = Σ x·P(x)“. 5. Zweiter Stab unten: ungleiche Gewichte (Anzahl der Köpfe: 1/8, 3/8, 3/8, 1/8 bei 0 bis 3), Keil bei 1,5, Gleichgewicht. — Haltepunkte: 2, 4.
- **Verständnisproblem:** „Schwerpunkt“ steht nur als Satz im Text; der Leser sieht nicht, warum die Gewichte der Verteilung den Mittelwert bestimmen und warum 3,5 keine Augenzahl sein muss.
- **Szenenname:** ml/k4schwerpunkt
- **Editor-Lücke:** machbar (Rotate des Stabes um den Keil; die Neigung ist ein fest vorberechneter Winkel)

Verworfen (08, über dem Soll 5): „Streuung: zwei Verteilungen mit gleichem E[X] und verschiedenem σ“ und „Standardisieren Z = (X − μ)/σ (verschieben, dann strecken)“ [je B]. Das Standardisieren wird in Artikel 09 (V15) für die Normalverteilung gezeigt, dort mit demselben Bild.

### Artikel 09 — Wichtige Verteilungen (Soll 5, vorh. 1)

### V13 [A] Binomialverteilung: Folgen zählen, Stäbe wachsen
- **Artikel:** content/ml/04-wahrscheinlichkeit/09-wichtige-verteilungen.md
- **Stelle:** Die Binomialverteilung — „Aus einer laufenden Fertigung mit 5 % Ausschuss prüft man 10 Teile. Wie viele defekte sind dabei? …“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben eine Reihe von vier Plätzen (n = 4), jeder Platz „intakt“ oder „defekt“. Darunter Axes: x = m (Anzahl defekter Teile) 0 bis 4, y = Anzahl der Folgen 0 bis 6. Dann zweite Axes für Bin(10; 0,05) mit m = 0 bis 5 und y = P(X = m) von 0 bis 0,65.
- **Ablauf:** 1. Für n = 4 erscheinen die 16 Folgen (Punktmuster 0/1) nacheinander und wandern jeweils zu der Spalte ihres m: Stäbe 1, 4, 6, 4, 1; Text „C(4, m) = 4·3 / 2 = 6 für m = 2“. 2. Jede Folge bekommt ihr Gewicht θ^m (1−θ)^(n−m): „jede bestimmte Folge hat dieselbe Wahrscheinlichkeit“ (nur für m = 2 gezeigt, 6 gleiche Stücke bilden einen Stab). 3. Wechsel zum Beispiel des Artikels: n = 10, θ = 0,05; Stäbe 0,599 / 0,315 / 0,075 / 0,010 / … erscheinen; Marker bei E[X] = nθ = 0,5. 4. Dazu zum Vergleich n = 20, θ = 0,5 (Glockenform, E = 10), in blau. — Haltepunkte: 1, 3.
- **Verständnisproblem:** Woher der Binomialkoeffizient kommt (Folgen mit m Erfolgen zählen) und was „Anzahl der Erfolge“ als Verteilung aussieht. Bei hm3 Teil 8 ist die Binomialverteilung bereits erklärt (Szene `hm3/k8poisson` zeigt Binomialstäbe); hier eigene Szene, weil die Zusammensetzung aus Einzelfolgen und der Bezug zu Bernoulli und Indikatoren zum Heft gehört, nicht der Poisson-Grenzwert.
- **Szenenname:** ml/k4binomial
- **Editor-Lücke:** machbar (L6 für „Folgen wandern“ hilfreich; Notbehelf MoveTo je Folge)

### V14 [A] Histogramm: Messwerte stapeln sich zur Glocke
- **Artikel:** content/ml/04-wahrscheinlichkeit/09-wichtige-verteilungen.md
- **Stelle:** Die Normalverteilung — „Misst man dieselbe Größe oft, so häufen sich die Messwerte um einen mittleren Wert …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes: x = Widerstand in Ω von 96 bis 104, y = Anzahl der Messwerte. Intervalle der Breite 0,5 (16 Balken). Eine gestrichelte Kurve (Normaldichte, μ = 100, σ = 1, skaliert auf die Balkenfläche) liegt zunächst verborgen.
- **Ablauf:** 1. Zehn Messpunkte fallen als Quadrate in ihre Intervalle (ein Quadrat je Messwert), es entsteht ein Klotzdiagramm, noch unregelmäßig. 2. Weitere 40 Werte (50 gesamt): Das Bild wird rund. 3. 300 Werte als Balken (nicht mehr einzelne Quadrate). 4. Die Dichtekurve N(100; 1) wird darübergezeichnet (Create); Text „Fläche der Balken → 1: Histogramm → Dichte“. 5. Marker für μ ± σ. — Haltepunkte: 1, 3, 4.
- **Verständnisproblem:** Der Begriff Histogramm und die Behauptung „sieht aus wie eine Glocke“ stehen als Text; die Brücke vom Zählen zur Dichte (Fläche 1, Balkenhöhe pro Breite) fehlt. Die Szene dient auch als Ausgangsbild für die Mittelwerte in Abschnitt 14 (k4lln, k4zgws).
- **Szenenname:** ml/k4histogramm
- **Editor-Lücke:** braucht Editor-Funktion: L7 (Histogramm wächst als Prozess) bzw. L6 (viele Punkte ziehen); Notbehelf: drei vorberechnete Balkenfolgen, die nacheinander erscheinen

### V15 [A] Standardisieren: verschieben, strecken, in die Tabelle lesen
- **Artikel:** content/ml/04-wahrscheinlichkeit/09-wichtige-verteilungen.md
- **Stelle:** Standardisieren und die Verteilungsfunktion Φ — „Für jede Wahrscheinlichkeit einer normalverteilten Größe braucht man ein Integral über (8.5) …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei übereinanderliegende Achsen. Oben X-Achse in Ω von 96 bis 104 mit der Dichte N(100; 1) und der markierten Fläche links von 102 Ω; unten Z-Achse von −4 bis 4 mit Standardnormaldichte und Fläche links von z = 2. Der Wert Φ(2) = 0,9772 wird angezeigt.
- **Ablauf:** 1. Dichte N(100; 1) mit der Schwelle 102 Ω; die Fläche rechts davon ist schraffiert („P(X > 102) = ?“). 2. Die Kurve wird um 100 nach links verschoben (Shift), Text „− μ“; die Schwelle wird zu 2. 3. Streckung um 1/σ (Scale) – bei σ = 1 gleich 1, deshalb zweites Beispiel σ = 2: Dichte N(100; 4) (flacher, Schwelle 104) wird um den Faktor 1/2 gestaucht, Schwelle wird 2. 4. Die Fläche rechts von z = 2 ist dieselbe wie vorher (0,0228), Text „1 − Φ(2) = 0,0228“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Warum eine einzige Tabelle für alle Normalverteilungen genügt; im Text steht dies als Beweis mit Substitution, ohne dass man sieht, dass Verschieben und Strecken die Fläche links der Schwelle erhalten.
- **Szenenname:** ml/k4standardisieren
- **Editor-Lücke:** braucht Editor-Funktion: L2 (Kurve wird Kurve) und L3 (Parameter μ, σ als Zeit); Notbehelf: drei Kurven nacheinander einblenden (gestrichelt die Ausgangskurve), Schwelle jeweils als MoveTo

### V16 [B] Quantisierungsrauschen ist gleichverteilt
- **Artikel:** content/ml/04-wahrscheinlichkeit/09-wichtige-verteilungen.md
- **Stelle:** Die Gleichverteilung (Rechenbeispiel Quantisierungsrauschen) — „Ein Analog-Digital-Umsetzer rundet jede Spannung auf das nächste Vielfache einer Stufe Δ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes: x = Eingangsspannung 0 bis 5 Δ, y links = Ausgangsstufen (Treppe), darunter y = Fehler e = Ausgang − Eingang zwischen −Δ/2 und Δ/2 (Sägezahn). Rechts Histogramm der Fehler.
- **Ablauf:** 1. Die Rundungstreppe wird gezeichnet. 2. Der Fehler (Sägezahn) wird gezeichnet. 3. Ein Punkt läuft über die Eingangsachse (MoveAlongPath), der Fehler wird als Messwert rechts im Histogramm abgelegt. 4. Das Histogramm ist ein Rechteck von −Δ/2 bis Δ/2 mit Höhe 1/Δ; Text „Gleichverteilung, Varianz Δ²/12“. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Warum der Fehler gleichverteilt ist, hängt an der Sägezahnform; im Text bleibt es eine Behauptung.
- **Szenenname:** ml/k4quantisierung
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Punkt mit mitlaufender Projektion); Notbehelf: MoveAlongPath und festes Rechteck

Verworfen (09, über dem Soll 5): „Bernoulli: Varianz θ(1−θ) als Parabel in θ“ [C], „Rauschen als wahrer Wert plus Zufallsstörung“ [B], „kategorische Verteilung und One-Hot“ [C].

### Artikel 10 — Mehrere Zufallsvariablen (Soll 4, vorh. 0)

### V17 [A] Gemeinsame Dichte und Randverteilung (marginalisieren)
- **Artikel:** content/ml/04-wahrscheinlichkeit/10-mehrere-zufallsvariablen.md
- **Stelle:** Die gemeinsame Verteilung / Randverteilungen — „Aus der gemeinsamen Verteilung erhält man die Verteilung jeder einzelnen Größe, wie in der Zähltabelle die Randsummen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Tabelle des Kapitels (S = Sonne, R = Rad; Zellen 0,3 / 0,1 / 0,1 / 0,5, Randsummen 0,4 / 0,6). Rechts die Dichte p(x, y) = x + y auf dem Einheitsquadrat als Heatmap (ScalarField) mit Achsen x, y von 0 bis 1, darunter eine Achse für p_X(x) (0,5 bis 1,5).
- **Ablauf:** 1. Tabelle: die Zeile S = 1 wird summiert (0,3 + 0,1 = 0,4), Randzahl erscheint; dasselbe für die anderen Zeilen/Spalten. 2. Heatmap der Dichte erscheint (hell oben rechts). 3. Ein senkrechter Streifen bei x = 0,2 (Breite 0,05) wird farbig; der Schnitt (y von 0 bis 1) wird zur Kurve „p(0,2; y)“ aufgetragen. 4. Die Fläche dieses Schnitts (= x + ½ = 0,7) wird als Punkt in die Achse p_X eingetragen. 5. Dasselbe für x = 0,5, x = 0,8: Punkte (0,2; 0,7), (0,5; 1,0), (0,8; 1,3) liegen auf der Geraden p_X(x) = x + ½, die gezeichnet wird. — Haltepunkte: 1, 4, 5.
- **Verständnisproblem:** „Marginalisieren“ und das Doppelintegral (Volumen) sind abstrakt; der Leser sieht nicht, dass die Randdichte die Summe aller Schnittflächen ist und wie die Tabellen-Randsumme dazu passt. Das Bild klärt auch das Doppelintegral als zwei Integrale nacheinander (innen Schnittfläche, außen Aufsummieren).
- **Szenenname:** ml/k4rand
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Streifen, der über x läuft); Notbehelf: drei feste Streifen nacheinander. Heatmap: ScalarField vorhanden.

### V18 [A] Bedingte Verteilung: Schnitt, skaliert auf Fläche 1
- **Artikel:** content/ml/04-wahrscheinlichkeit/10-mehrere-zufallsvariablen.md
- **Stelle:** Bedingte Verteilungen — „Kennt man den Wert einer Größe, so ändert sich, was man über die andere weiß …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Heatmap von p(x, y) = x + y (wie V17), rechts zwei kleine Achsen für y von 0 bis 1: oben der Schnitt p(x₀, y) = x₀ + y, unten die bedingte Dichte p(y | x₀) = (x₀ + y)/(x₀ + ½).
- **Ablauf:** 1. Die Heatmap erscheint, eine senkrechte Linie bei x₀ = 0 wird gezogen („wir erfahren X = 0“). 2. Oben rechts erscheint der Schnitt: die Gerade y (von 0 bis 1), Fläche ½. 3. Die Fläche ist nicht 1; Text „nicht normiert“. Die Kurve wird mit dem Faktor 1/(x₀ + ½) = 2 gestreckt (Scale in y): 2y, Fläche 1. 4. Linie wandert zu x₀ = 1: Schnitt 1 + y (Fläche 1,5), skaliert 1/1,5: (1 + y)/1,5. Die Form ist fast flach, kleine y sind jetzt nicht mehr selten. 5. Vergleich mit der Tabelle: Zeile S = 1: 0,3 / 0,4 = 0,75, 0,1 / 0,4 = 0,25. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Dass die bedingte Verteilung eine ganz neue Verteilung für jeden x-Wert ist und dass man teilen muss, damit sie wieder 1 ergibt. Hinweis: dieselbe Idee wie V7 (Einschränken auf die Sonnenzeile) für Dichten.
- **Szenenname:** ml/k4bedingtdichte
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Schnittlinie wandert) und L2 (Kurve wird skaliert); Notbehelf: Scale auf FunctionGraph (nicht uniform nötig, y-Streckung) oder zwei getrennte Kurven

### V19 [A] i.i.d.: Ein Datensatz sind unabhängige Ziehungen aus einer Verteilung
- **Artikel:** content/ml/04-wahrscheinlichkeit/10-mehrere-zufallsvariablen.md
- **Stelle:** Unabhängig und identisch verteilt — „Ein Datensatz entsteht oft so: Man wählt zufällig Wohnungen aus, misst wiederholt mit demselben Gerät …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links eine Verteilung über der Ebene (Fläche in m², Miete in €: Punktwolke als Höhenlinien einer zweidimensionalen Glocke, die Datenpunkte werden aus ihr gezogen). Rechts eine Datenmatrix (Table) mit den Zeilen x₁, x₂, … (Fläche | Miete).
- **Ablauf:** 1. Die Verteilung liegt als Höhenlinien (Ellipsen, positiv geneigt) im Hintergrund. 2. Ein Punkt erscheint, seine Koordinaten laufen als Zeile 1 in die Tabelle („x₁“). 3. Zweiter, dritter Punkt: jeder neue Punkt unabhängig vom vorigen. 4. Nach 30 Punkten (schnell): die Wolke gleicht der Verteilung. 5. „Zweiter Datensatz“: eine andere Menge von 30 Punkten in anderer Farbe über derselben Verteilung; Text „andere Stichprobe, dieselbe Verteilung“. — Haltepunkte: 3, 5.
- **Verständnisproblem:** „Ein Datensatz ist eine Stichprobe aus einer unbekannten Verteilung“ ist der Kernsatz des Heftes für die Statistik; sein Sinn (andere Auswahl, andere Zahlen) ist ohne Bewegung kaum zu sehen. Die Szene ml/k4streu (Artikel 11) zeigt schon eine Punktwolke; hier der Erzeugungsprozess.
- **Szenenname:** ml/k4iid
- **Editor-Lücke:** braucht Editor-Funktion: L6 (Stichproben ziehen); Notbehelf: PointCloud mit festen Punkten, in Gruppen erscheinend

### V20 [B] Unabhängige Zufallsvariablen: gemeinsame Verteilung = Produkt der Ränder
- **Artikel:** content/ml/04-wahrscheinlichkeit/10-mehrere-zufallsvariablen.md
- **Stelle:** Unabhängige Zufallsvariablen — „Zwei Zufallsvariablen sind unabhängig, wenn jede Aussage über die eine unabhängig von jeder Aussage über die andere ist …“
- **Art:** vorhandene Szene wiederverwenden (ml/k4unabh aus V9, Flächenbild mit dem Mosaik der Zähltabelle; im Zweig „unabhängig“ zweimal Würfel mit 1/36 = 1/6·1/6)
- **Was zu sehen ist:** Wie V9; ergänzt um das 6×6-Raster der zwei Würfel: Jede Zelle hat die Fläche 1/36 = 1/6 · 1/6, gestrichelt das Produkt der Ränder, im Gegensatz zu S und R (0,3 statt 0,16).
- **Ablauf:** 1. Raster der 36 Zellen mit 1/36. 2. Die Randstreifen (1/6 breit, 1/6 hoch) werden aufgetragen, ihr Produkt füllt jede Zelle. 3. Das Mosaik von S und R: das Produkt der Ränder 0,16 passt nicht zu 0,3. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Dass „Produkt der Randverteilungen“ ein Flächenbild ist; V9 hat es für Ereignisse gezeigt, hier für Zufallsvariablen (Verteilungen) und die Folge E[XY] = E[X]·E[Y].
- **Szenenname:** ml/k4unabh (wie V9, oder Erweiterung ml/k4unabhrv)
- **Editor-Lücke:** machbar

### Artikel 11 — Kovarianz und Korrelation (Soll 4, vorh. 3, +1 begründet)

### V21 [A] Kovarianz: Rechtecke aus den Abweichungen, grün und rot
- **Artikel:** content/ml/04-wahrscheinlichkeit/11-kovarianz-und-korrelation.md
- **Stelle:** Die Kovarianz — „Liegt X über seinem Erwartungswert, wenn auch Y über seinem liegt, so ist das Produkt der beiden Abweichungen positiv …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes: x = Fläche in m² (30 bis 100), y = Zimmerzahl (0 bis 5). Die vier Wohnungen aus Heft-1-Beispiel als Punkte (60; 2), (40; 1), (90; 4), (70; 3). Ein Fadenkreuz im Schwerpunkt (65; 2,5). Rechts eine Zeile für das Mittel der Rechteckflächen.
- **Ablauf:** 1. Punkte und Fadenkreuz erscheinen; die vier Quadranten werden mit „+“ (rechts oben, links unten) und „−“ (links oben, rechts unten) beschriftet. 2. Zu jedem Punkt wird das Rechteck zwischen Punkt und Schwerpunkt gezeichnet (Abweichung a_i × Abweichung b_i): Flächen 2,5 (Punkt (60; 2)), 37,5 (40; 1), 37,5 (90; 4), 2,5 (70; 3), alle grün, weil alle vier Punkte links unten oder rechts oben liegen. 3. Die Rechteckflächen werden addiert und durch 4 geteilt: „cov = (2,5 + 37,5 + 37,5 + 2,5)/4 = 20“. 4. Zweiter Datensatz daneben (gleicher Mittelpunkt, Punkte (60; 3), (40; 4), (90; 1), (70; 2) mit negativem Zusammenhang): Rechtecke rot, Summe negativ. 5. Dritter Datensatz ohne Zusammenhang: grüne und rote Rechtecke heben sich auf, cov ≈ 0. — Haltepunkte: 2, 3, 5.
- **Verständnisproblem:** Die Definition E[(X−μ_X)(Y−μ_Y)] ist ein Erwartungswert eines Produkts; erst als Rechteckfläche mit Vorzeichen wird klar, warum das Vorzeichen den gemeinsamen Anstieg zählt und warum die Kovarianz eine Einheit „m²·Zimmer“ hat. Ergänzt k4streu, das die Wolken nach Korrelation zeigt, aber nicht den Mechanismus.
- **Szenenname:** ml/k4kovquadrant
- **Editor-Lücke:** machbar (Rectangles aus Punkt zum Fadenkreuz)

### V22 [B] Varianz einer Summe als Pythagoras (Winkel zwischen Rauschquellen)
- **Artikel:** content/ml/04-wahrscheinlichkeit/11-kovarianz-und-korrelation.md
- **Stelle:** Die Kovarianz als Skalarprodukt — „Die Rechenregeln der Kovarianz sind die eines Skalarprodukts …“ (Rechenbeispiel Rauschquellen 3 und 4 mV)
- **Art:** neue Animation
- **Was zu sehen ist:** Ebene mit zwei Pfeilen a (Länge 3, „σ_X = 3 mV“) und b (Länge 4, „σ_Y = 4 mV“) aus dem Nullpunkt und der Summenpfeil a + b. Anzeige „ρ = cos(Winkel)“ und „σ_{X+Y}“.
- **Ablauf:** 1. a nach rechts, b senkrecht nach oben (ρ = 0): a + b hat Länge 5 (Hypotenuse), Text „σ² = 9 + 16 = 25“. 2. b dreht um den Nullpunkt auf 60° (ρ = 0,5): Länge √37 ≈ 6,08, „9 + 16 + 2·0,5·3·4 = 37“. 3. b dreht weiter auf 0° (ρ = 1): Länge 7 = 3 + 4, „Standardabweichungen addieren sich nur bei ρ = 1“. 4. b dreht auf 120° (ρ = −0,5): Länge √13 ≈ 3,61, „9 + 16 − 12 = 13“. — Haltepunkte: 1, 2, 4.
- **Verständnisproblem:** „Varianzen addieren sich, Standardabweichungen nicht“ und die Rolle des Korrelationskoeffizienten als Kosinus; dies ist im Text eine Tabelle von Entsprechungen, im Bild wird die Aussage sichtbar. Knüpft an ml/01 an (Winkel, Skalarprodukt; `ml/k1…`-Szenen), kein Vorgriff.
- **Szenenname:** ml/k4pythagoras
- **Editor-Lücke:** braucht Editor-Funktion: L3 hilfreich (Winkel als Parameter); machbar mit Rotate des Pfeils b um den Nullpunkt und festen Zwischenhalten
- **Soll-Hinweis:** +1 über Soll (4), weil die Geometrie von Kovarianz und Korrelation im Text als reine Tabelle steht und drei vorhandene Szenen (Σ, Streuplot, Skalarprodukt) den Pythagoras-Gedanken nicht abdecken.

### Artikel 12 — Zufallsvektoren und die Kovarianzmatrix (Soll 4, vorh. 2)

### V23 [A] Streuung in einer Richtung: der Schatten dreht sich
- **Artikel:** content/ml/04-wahrscheinlichkeit/12-zufallsvektoren-und-die-kovarianzmatrix.md
- **Stelle:** Die Streuung in einer Richtung — „Wie stark streuen Datenpunkte, wenn man nur in eine Richtung blickt? …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die drei zentrierten Punkte (−1; 0), (0; −1), (1; 1) und eine Gerade durch den Nullpunkt in Richtung u (Einheitsvektor, Pfeil). Die Punkte werfen senkrechte Schatten auf die Gerade (Fußpunkte). Rechts Axes: x = Winkel von u (0° bis 180°), y = Varianz u^T S u (0 bis 1,2). Eintragungen der Eigenwerte 1 und 1/3.
- **Ablauf:** 1. Die Punkte und u bei 0° (Achsenrichtung): Schatten auf der x-Achse bei −1, 0, 1; Varianz 2/3, Punkt erscheint in der rechten Kurve. 2. u dreht sich auf 45° (Richtung (1,1)/√2): Schattenlängen −1/√2, −1/√2, 2/√2; Varianz 1 (Maximum), Kurvenpunkt. 3. u dreht auf 135° ((1,−1)/√2): Varianz 1/3 (Minimum). 4. Die ganze Kurve wird gezeichnet (u = (cos θ, sin θ): u^T S u = 2/3 + (1/3) sin 2θ), Marker bei Maximum 1 und Minimum 1/3, Text „Eigenwerte, Eigenvektoren = Richtungen extremer Streuung“. — Haltepunkte: 2, 3, 4.
- **Verständnisproblem:** Dass die Kovarianzmatrix die Streuung in jeder Richtung enthält, und warum die Eigenwerte Maximum und Minimum sind; im Text stehen Formel, Abbildung der quadratischen Form und ein Satz mit dem Spektralsatz.
- **Szenenname:** ml/k4richtungsvarianz
- **Editor-Lücke:** braucht Editor-Funktion: L3 (u als Winkel-Sweep mit mitlaufender Projektion und Kurvenpunkt); Notbehelf: vier feste Winkel (0°, 45°, 90° und 135°) mit Fußpunkten als einzelne Frames, Rotate der Gerade, Kurve per Create
- Hinweis: Die Rechnung „Schatten“ benutzt das Skalarprodukt aus ml/01 (`ml/k1rschatten`, DotProduct).

### V24 [A] Lineare Abbildung einer Punktwolke: aus (a, b) wird (a + b, a − b)
- **Artikel:** content/ml/04-wahrscheinlichkeit/12-zufallsvektoren-und-die-kovarianzmatrix.md
- **Stelle:** Lineare Abbildungen von Zufallsvektoren — „Aus Merkmalen bildet man oft neue: Summen, Differenzen, gewichtete Summen, gedrehte Koordinaten …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Koordinatensysteme nebeneinander. Links (a, b)-Ebene mit den drei Punkten (1; 2), (2; 1), (3; 3), Mittelpunkt (2; 2). Rechts (a + b, a − b)-Ebene mit den Bildpunkten (3; −1), (3; 1), (6; 0). Unter beiden Texte: Kovarianzmatrix S = (1/3)((2, 1), (1, 2)) und A S A^T = (1/3)((6, 0), (0, 2)).
- **Ablauf:** 1. Linke Wolke, Mittelpunkt, Matrix S; Text „korreliert“. 2. Pfeile von jedem Punkt nach rechts (A = ((1,1),(1,−1))) laufen zu den Bildpunkten. 3. Rechts erscheint die Wolke; Mittelpunkt (4; 0). 4. Die Streuung in der neuen Achsenrichtung wird gezeigt: Varianz der Summe 2, der Differenz 2/3; die Wolke liegt jetzt achsenparallel (unkorreliert). — Haltepunkte: 2, 4.
- **Verständnisproblem:** Was A Σ A^T bedeutet; als reine Formel mit Beweis; im Bild sieht man, dass die Verschiebung herausfällt und die Wolke gedreht und gestreckt wird. Die Szene dient auch als Brücke zu den Hauptachsen (Abschnitt 13).
- **Szenenname:** ml/k4lineareabb
- **Editor-Lücke:** braucht Editor-Funktion: L5 (Matrix auf die Wolke anwenden); Notbehelf: zwei Zustände mit verbindenden Pfeilen (wie `ml/k1…` für Abbildungen)

### Artikel 13 — Die mehrdimensionale Normalverteilung (Soll 4, vorh. 2)

### V25 [A] Erzeugen und Zerlegen: Kreiswolke → strecken → drehen → verschieben
- **Artikel:** content/ml/04-wahrscheinlichkeit/13-die-mehrdimensionale-normalverteilung.md
- **Stelle:** Im Eigensystem zerfällt die Verteilung — „Anschaulich ist eine mehrdimensionale Normalverteilung also eine Wolke aus unabhängigen Glocken entlang senkrechter Achsen, die gedreht und verschoben wurde …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes (x₁ von −4 bis 5, x₂ von −3 bis 6), eine Wolke von 60 Punkten aus N(0, I) mit Höhenlinie Δ = 1 (Kreis mit Radius 1). Dann dieselben Punkte nach jedem Schritt. Beschriftung: „z“, „y = Λ^{1/2} z“, „Q y“, „μ + Q y“.
- **Ablauf:** 1. Die Standardwolke z (runde Wolke, Kreis Δ = 1). 2. Strecken: Achse 1 mit √3 ≈ 1,73, Achse 2 mit 1 (Skalierung der Wolke): Ellipse mit Halbachsen √3 und 1, noch achsenparallel (unabhängig). 3. Drehen um 45°: Achsen in Richtung (1,1)/√2 und (1,−1)/√2; die Komponenten x₁, x₂ sind nun korreliert (ρ = 0,5). 4. Verschieben um μ = (1; 2). Text: „x = μ + Q Λ^{1/2} z ∼ N(μ, Σ)“, Σ = ((2,1),(1,2)). 5. Rückwärts: Die Pfeile zeigen, dass man aus x die unabhängigen Koordinaten y = Q^T(x − μ) zurückgewinnt. — Haltepunkte: 2, 3, 4.
- **Verständnisproblem:** „im Eigensystem zerfällt die Verteilung“ und wie Rechner Normalverteilungen erzeugen. Der Text sagt es in Sätzen; das Bild zeigt, was die Drehung koppelt.
- **Szenenname:** ml/k4erzeugen
- **Editor-Lücke:** braucht Editor-Funktion: L5 (lineare Abbildung der Wolke) oder L2; Notbehelf: vier Wolken-Zustände (PointCloud) mit Höhenlinien, nacheinander FadeIn

### V26 [B] Die Dichte als Berg: Höhenlinien sind Schnitte in gleicher Höhe
- **Artikel:** content/ml/04-wahrscheinlichkeit/13-die-mehrdimensionale-normalverteilung.md
- **Stelle:** Die Dichte — „In einer Dimension steht im Exponenten der Normalverteilung die quadrierte Abweichung, geteilt durch die Varianz …“
- **Art:** neue Animation
- **Was zu sehen ist:** 3D-Fläche z = p(x) für die Verteilung des Artikels (μ = (1; 2), Σ = ((2,1),(1,2)), Höchstwert 0,0919), darunter in der Grundebene die Höhenlinien Δ = 1, 2, 3 (ScalarField mit Höhenlinien).
- **Ablauf:** 1. Die Fläche wächst aus der Grundebene (Berg). 2. Eine waagerechte Ebene in Höhe 0,0919·e^{−1/2} = 0,0557 schneidet den Berg; die Schnittkurve wird auf die Grundebene projiziert und ist die Ellipse Δ = 1. 3. Höhe 0,0919·e^{−2} = 0,0124: Ellipse Δ = 2. 4. Kamera dreht sich über den Berg und endet in Draufsicht auf die Höhenlinien. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Was „Höhenlinie der Dichte“ und „konstanter Mahalanobis-Abstand“ bedeuten, bevor Abb. 17 die Ellipsen zeigt.
- **Szenenname:** ml/k4dichteberg
- **Editor-Lücke:** braucht Editor-Funktion: L4 (Kamera drehen), sonst machbar (FunctionGraph 3D und ScalarField vorhanden)

Verworfen (13, über dem Soll): „Bedingen als wandernder Schnitt (Gerade der bedingten Erwartungswerte)“ [B] gehört in die Animation der vorhandenen Szene k4ellipsen (b), siehe Liste; „Wahrscheinlichkeit in der Ellipse 39,3 % / 86,5 %“ [C].

### Artikel 14 — Mittelwerte vieler Zufallsvariablen (Soll 4, vorh. 2)

### V27 [A] Standardfehler: der Mittelwert streut mit σ/√n
- **Artikel:** content/ml/04-wahrscheinlichkeit/14-mittelwerte-vieler-zufallsvariablen.md
- **Stelle:** Der Mittelwert unabhängiger Zufallsvariablen — „Ein verrauschter Messwert schwankt mit der Standardabweichung σ. Misst man n-mal und mittelt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Achse „Messwert in mV“ von −15 bis 15 (wahrer Wert 0, σ = 5 mV). Drei Zeilen übereinander: n = 1, n = 16, n = 100. In jeder Zeile 30 Punkte (30 Wiederholungen des Versuchs: 1 Messwert, Mittelwert aus 16, Mittelwert aus 100) und die zugehörige Glockenkurve.
- **Ablauf:** 1. Zeile n = 1: 30 Punkte, breite Wolke, σ = 5 mV als Klammer. 2. Zeile n = 16: die Punkte sind enger, Klammer 5/4 = 1,25 mV. 3. Zeile n = 100: noch enger, 5/10 = 0,5 mV. 4. Text: „4-fache Messungen → halbe Streuung“ (Pfeil von n = 16 auf n = 64 in der Skizze) und „100-fach → ein Zehntel“. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Warum man die Streuung des Mittelwerts mit 1/√n beschreibt und nicht mit 1/n; der Text gibt die Rechnung (Varianz σ²/n). Das Bild zeigt den langsamen Gewinn. Ergänzt k4lln (eine Folge) um die Verteilung bei festem n.
- **Szenenname:** ml/k4standardfehler
- **Editor-Lücke:** braucht Editor-Funktion: L6 (Stichproben ziehen); Notbehelf: PointCloud mit festen Punkten je Zeile

### V28 [A] Tschebyschow-Ungleichung: die grobe Schranke gilt für jede Verteilung
- **Artikel:** content/ml/04-wahrscheinlichkeit/14-mittelwerte-vieler-zufallsvariablen.md
- **Stelle:** Die Tschebyschow-Ungleichung — „Die Varianz sagt, wie weit eine Zufallsvariable typischerweise streut. Wie wahrscheinlich ist eine große Abweichung? …“
- **Art:** vorhandene Szene wiederverwenden (`hm3/k8tscheb` aus dem Heft Wahrscheinlichkeitsrechnung, Achsen k von 0 bis 4, Schranke 1/k², wahre Werte der Normalverteilung); mit einem zusätzlichen Marker für den Würfel des Artikels, falls die Szene angepasst wird
- **Was zu sehen ist:** Achsen k = Abstand in Standardabweichungen, y = Wahrscheinlichkeit; Schranke 1/k² (grob), Normalverteilung (4,6 % bei k = 2, 0,3 % bei k = 3) und der Würfelmarker (k = 2,5/1,708 ≈ 1,46: tatsächlich 1/3, Schranke 0,467).
- **Ablauf:** 1. Achsen. 2. Die Schranke 1/k² zeichnet sich. 3. Die Normalverteilung darunter. 4. Marker k = 2: 25 % gegen 4,6 %. 5. Würfelpunkt bei k = 1,46: 1/3 gegen 0,467. — Haltepunkte: 4, 5.
- **Verständnisproblem:** Was die Ungleichung sagt (obere Schranke für jede Verteilung) und wie weit sie vom wahren Wert liegt; der Beweis ist nur ein Absatz.
- **Szenenname:** hm3/k8tscheb (oder ml/k4tscheb als Kopie mit dem Würfelmarker)
- **Editor-Lücke:** machbar

### Artikel 15 — Das Wichtigste bis hier (Soll 2, vorh. 0)

### V29 [A] Wahrscheinlichkeit als Masse vom Gewicht 1 (Zusammenschau)
- **Artikel:** content/ml/04-wahrscheinlichkeit/15-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt aus einem Prinzip: Wahrscheinlichkeit verhält sich wie eine Masse vom Gesamtgewicht 1 …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Stab (Zahlenstrahl 0 bis 7) mit den sechs Würfelgewichten 1/6 auf 1 bis 6 (sechs Klötze). Rechts ein Ablesefeld „P“, „E[X]“, „Var“.
- **Ablauf:** 1. Sechs Klötze der Masse 1/6, Gesamtmasse 1. 2. Ereignis A = {2, 4, 6} wird gelb markiert: Masse 1/2 (Additivität). 3. Bedingen auf A: die Klötze 1, 3, 5 werden grau (ausgeblendet), die drei übrigen Klötze wachsen von 1/6 auf 1/3 (neu auf 1 gewogen). 4. Der Keil (Schwerpunkt) gleitet auf E[X | A] = 4. 5. Pfeile von 4 zu den Klötzen zeigen die Abstände 2, 0, 2; Text „Var = (4 + 0 + 4)/3 = 8/3“. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Der integrierende Gedanke des Kapitels (Wahrscheinlichkeit = Masse; Bedingen = Ausschneiden und neu wiegen; Erwartungswert = Schwerpunkt; Varianz = Trägheit) steht als Satz und als Tabelle; das Bild verbindet vier Bausteine in einem Beispiel.
- **Szenenname:** ml/k4masse
- **Editor-Lücke:** braucht Editor-Funktion: L1 (Verschwinden der Klötze; Notbehelf: graue Überdeckung)

### V30 [B] Vom Rauschen zur Glocke: Abschluss mit dem zentralen Grenzwertsatz
- **Artikel:** content/ml/04-wahrscheinlichkeit/15-das-wichtigste-bis-hier.md
- **Stelle:** Die Antwort in drei Sätzen (Punkt 3) — „Weil sich die Varianzen unabhängiger Größen addieren, wird ein Mittelwert aus n Messungen mit σ/√n genauer …“
- **Art:** vorhandene Szene wiederverwenden (`ml/k4zgws` aus Artikel 14: Verteilung des Mittelwerts von n = 1, 2, 3, 10 Würfeln mit der roten Normalkurve)
- **Was zu sehen ist / Ablauf:** wie die animierte Fassung von k4zgws (siehe Liste).
- **Verständnisproblem:** Die dritte Zusammenfassung bündelt Mittelwert, Standardfehler und Glocke; das Bild liefert die Anschauung dazu, ohne neue Szene.
- **Szenenname:** ml/k4zgws
- **Editor-Lücke:** machbar

## Vorhandene Abbildungen

- ml/k4rverkettung (04-bedingte-wahrscheinlichkeit): animieren ja, echtes ∏-Rechenbild nötig (heute ein statischer MathTex) — Schritte: 1. Kiste mit 10 Teilen (2 defekt), 2. erste Entnahme: 8/10 (Teil verschwindet aus der Kiste, 7 intakte bleiben), 3. zweite: 7/9, 4. dritte: 6/8, 5. Produkt 8/10 · 7/9 · 6/8 = 7/15 ≈ 0,467 wächst Faktor für Faktor, „mehr als 50 % mindestens ein defektes“ | Lücke: machbar (Operation ∏, Rechenbild); L1 für das Entfernen des gezogenen Teils
- ml/k4rtotal (04): animieren ja, echtes Σ-Rechenbild nötig (heute ein statischer MathTex) — Schritte: 1. zwei Balken „Fabrik 1: 60 % Lieferanteil, 1 % Ausschuss“ und „Fabrik 2: 40 %, 3 %“, 2. Produkte 0,6 · 0,01 = 0,006 und 0,4 · 0,03 = 0,012 als Flächen, 3. Summe 0,018 = 1,8 %, 4. Marker zwischen 1 % und 3 % | Lücke: machbar (Operation Σ)
- ml/k4baum (05-der-satz-von-bayes): animieren ja — Schritte: 1. 10 000 Teile, 2. Verzweigung in 100 defekt / 9 900 intakt, 3. weiter in 99 / 1 Alarm bzw. 495 / 9 405, 4. die roten Alarme (99 + 495 = 594) werden hervorgehoben, Anteil 99/594 = 1/6, 5. Zweig „ohne Alarm“: 1 von 9 406 | Lücke: machbar (TextBox, LabeledArrow; Wandern der Teile wäre L6)
- ml/k4rbayes (05): animieren ja, Rechenbild — Schritte: 1. Zähler 0,99 · 0,01 = 0,0099, 2. Nenner 0,0099 + 0,05 · 0,99 = 0,0594, 3. Quotient 1/6 | Lücke: machbar (Arithmetik-Operation; heute MathTex)
- ml/k4dichte (07-zufallsvariablen-und-verteilungen): animieren ja — Schritte: 1. (a) Stäbe 1/8, 3/8, 3/8, 1/8 wachsen nacheinander (siehe V11), 2. (b) Rechteck der Dichte 2 auf [0; 0,5] s, 3. Fläche 0,1 bis 0,3 füllt sich, 0,2·2 = 0,4, 4. Marker „Höhe ist keine Wahrscheinlichkeit“, Fläche Gesamt 1 | Lücke: machbar
- ml/k4vertfkt (07): animieren ja — Schritte: 1. Treppe: Stufen 1/8, 3/8, 3/8, 1/8 springen nacheinander (gefüllter Punkt), 2. Rampe der Steigung 2/s entsteht, 3. gestrichelte Linien bei 0,1 und 0,3 s, Abstand F(0,3) − F(0,1) = 0,4 | Lücke: machbar
- ml/k4rmuenzen (08-erwartungswert-und-varianz): animieren ja, ist bereits echte Operation DotProduct (v^T p = 1,5) — Schritte: Zeile für Zeile Wert × Wahrscheinlichkeit, Summe | Lücke: machbar (Operation vorhanden)
- ml/k4rwuerfel (08): animieren ja, heute MathTex — Schritte: sechs Summanden k · 1/6, Summe 3,5 (Operation Σ oder DotProduct) | Lücke: machbar
- ml/k4rquadrat (08): animieren ja, heute MathTex — Schritte: quadrieren 1, 4, …, 36, je mit 1/6 gewichten, Summe 91/6 ≈ 15,17 | Lücke: machbar (Σ)
- ml/k4rvarianz (08): animieren ja, heute MathTex — Schritte: Abweichungen −2,5, −1,5, −0,5, 0,5, 1,5, 2,5, quadrieren 6,25, 2,25, 0,25, …, mit 1/6 gewichten, Summe 35/12 ≈ 2,917 | Lücke: machbar (Σ)
- ml/k4normal (09-wichtige-verteilungen): animieren ja — Schritte: 1. Achsen und Glocke (Create), 2. Fläche ±1σ (0,683), 3. ±2σ (0,954), 4. ±3σ (0,997), 5. Wendepunkte bei μ ± σ markiert | Lücke: machbar; L3 (μ, σ verändern) hilfreich
- ml/k4rkovarianz (11-kovarianz-und-korrelation): animieren ja, Rechenbild — Schritte: Zellen (s, r) = (1, 1), (1, 0), (0, 1), (0, 0) mit s·r·P: nur die erste trägt 0,3 bei, Summe 0,3, minus E[S]E[R] = 0,16 → 0,14 | Lücke: machbar (Σ; heute MathTex)
- ml/k4streu (11): animieren ja — Schritte: 1. Achsen (a), Wolke ρ = −0,90 erscheint, 2. (b) ρ = 0, 3. (c) 0,5, 4. (d) 0,9 — die Punkte werden stufenweise ergänzt; 5. (e) Parabel und (f) Kreuz mit Hinweis „ρ = 0 trotz Abhängigkeit“ | Lücke: machbar (240 Punkte; L6 hilfreich)
- ml/k4rdaten (11): animieren ja, Rechenbild — Schritte: DotProduct der zentrierten Vektoren (−1, 0, 1)·(0, −1, 1) = 1, geteilt durch 3 = 1/3; zwei weitere für die Varianzen 2/3; Quotient 0,5 | Lücke: machbar (Operation DotProduct, heute MathTex)
- ml/k4rkovmatrix (12-zufallsvektoren-und-die-kovarianzmatrix): animieren ja, Rechenbild — Schritte: vier Einträge S_jl als Skalarprodukte der zentrierten Spalten durch 3, symmetrisch | Lücke: L7 (Matrix · Matrix als Prozess); Notbehelf: vier DotProduct-Operationen
- ml/k4rrichtung (12): animieren ja, Rechenbild — Schritte: Komponenten von u, Einträge von S mit u_j u_l gewichtet, Summe 1 | Lücke: L7; Notbehelf: Σ über vier Summanden
- ml/k4ellipsen (13-die-mehrdimensionale-normalverteilung): animieren ja — Schritte: (a) 1. Wolke von 80 Punkten, 2. Eigenvektoren q₁, q₂, 3. Ellipse Δ = 1 mit Halbachsen √3 und 1, 4. Δ = 2, Zähler 31 und 69 innerhalb; (b) 5. Schnittlinie x₂ = 4 erscheint, 6. bedingte Normalverteilung Mittel 2, Standardabweichung 1,22, 7. die Gerade der bedingten Erwartungswerte wird gezeichnet | Lücke: machbar; L3 (Linie wandert über x₂) hilfreich
- ml/k4rmahalanobis (13): animieren ja, Rechenbild — Schritte: Eigenkoordinaten y₁ = 1,5√2, y₂ = 0; Σ y²/λ = 4,5/3 = 1,5, Wurzel 1,22; ebenso x_b: 2/1 = 2, Wurzel 1,41 | Lücke: machbar (Σ; heute MathTex)
- ml/k4lln (14-mittelwerte-vieler-zufallsvariablen): animieren ja — Schritte: 1. Achsen (log n von 1 bis 10 000), 2. erste Folge zeichnet sich, 3. zweite und dritte, 4. die Hüllkurven 3,5 ± 2σ/√n erscheinen | Lücke: machbar (Create der DataCurve; die Parallelszene `hm3/k8mittel` zeigt dasselbe)
- ml/k4zgws (14): animieren ja — Schritte: 1. n = 1 (Rechteckbalken, Gleichverteilung), 2. n = 2 (Dreieck), 3. n = 3, 4. n = 10 (fast Glocke); die rote Normalkurve liegt über jedem Schritt | Lücke: braucht L2 (Balken verwandeln sich); Notbehelf: vier Zustände nacheinander (Stem-Gruppen erscheinen). Parallelszene `hm3/k8zgs`.

Überzählige vorhandene Szenen: keine (kein Artikel hat mehr als 5; Artikel 08 hat exakt 4 vorhandene plus V12 = 5).
