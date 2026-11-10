# Abbildungen und Animationen — Paket ml_5 (Heft ml/05-statistik-und-information)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.
Deutsche Artikel 01–13. 22 Szenen `ml/k5…` im Heft eingebunden (12 Konzeptbilder aus Axes/FunctionGraph/Stem/TextBox/Zielscheibe und 11 „Rechenbilder“ k5r…). Von den 11 Rechenbildern ist nur **k5rcode** eine echte Editor-Operation (`DotProduct`); die übrigen **10** (k5rerwartung, k5rmse, k5rbessel, k5rprodukt, k5rloglik, k5rbayes, k5rentropie, k5rkreuz, k5rkl, k5rkreuzml) bestehen aus einem einzigen statischen `MathTex`. Sie sollen auf Σ / ∏ / Skalarprodukt / Arithmetik umgebaut werden (Summanden laufen nacheinander ein, Zwischensumme wächst).
Neue Szenen heißen `ml/k5<name>`; Szenen ohne Operation müssen nicht neu gezeichnet werden, sondern bekommen eine Zeitachse.

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-statistik-und-information | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-schatzen-aus-einer-stichprobe | 3 | 3 | 0 | 0 | 0 | 0 | 3 |
| 03-wie-gut-ist-ein-schatzer | 4 | 2 | 1 | 1 | 0 | 0 | 4 |
| 04-die-varianz-schatzen | 3 | 1 | 2 | 0 | 0 | 0 | 3 |
| 05-die-likelihood | 3 | 3 | 0 | 0 | 0 | 0 | 3 |
| 06-die-maximum-likelihood-schatzung | 4 | 0 | 3 | 1 | 0 | 0 | 4 |
| 07-prior-und-posterior | 5 | 3 | 2 | 0 | 0 | 0 | 5 |
| 08-die-maximum-a-posteriori-schatzung | 3 | 0 | 3 | 0 | 0 | 0 | 3 |
| 09-informationsgehalt-und-entropie | 4 | 4 | 1 | 0 | 0 | 0 | 5 |
| 10-kreuzentropie-und-kl-divergenz | 3 | 4 | 0 | 0 | 0 | 1 | 3 |
| 11-die-grote-entropie | 3 | 1 | 3 | 0 | 0 | 0 | 4 |
| 12-maximum-likelihood-und-kl-divergenz | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| 13-das-wichtigste-bis-hier | 2 | 0 | 1 | 1 | 0 | 0 | 2 |
| **Summe** | 41 | 22 | 18 | 4 | 0 | 1 | 43 |

Soll-Abweichungen (+1, zwei von 13 Artikeln): 09 (vier Unterabschnitte mit je eigenem Begriff: Informationsgehalt, Entropie, Code, binäre Entropie; „Informationsgehalt“ hat sonst keine Anschauung), 11 (drei verschiedene Sätze/Begriffe: Gleichverteilung maximal, differentielle Entropie, Normalverteilung maximal). 10 hat vorher 4 Szenen, davon werden k5rkl und k5kl zusammengelegt (−1). 07 ist mit 5 am Maximum.
Aus dem Soll-Plan weggelassen (nur Notiz): 02 Rechenbild ∏ der Münzfolge (0,7⁷·0,3³ ≈ 0,00222) — dieselbe Rechnung steht in Artikel 05 (ml/k5rprodukt); 07 „Prior-Gewicht w wandert mit N“ (Zahlenstrahl, B) — das gewichtete Mittel (4/14·0,5 + 10/14·0,7 = 9/14) ist dort nur Probe; 10 „KL ist kein Abstand“ (Stems p=(0,5;0,5) gegen r=(0,9;0,1), 0,511 gegen 0,368, B) — Maximum 3 erreicht; 09 Rechenbild Zweierblock (0,81·1+0,09·2+0,09·3+0,01·3 = 1,29, Skalarprodukt wie k5rcode) — Maximum 5 erreicht.

## Top 3

- V19 [A] 12-maximum-likelihood-und-kl-divergenz — Kreuzentropie über θ, waagerechte Linie H(p̂), Abstand = KL, Marker rutscht von 0,5 nach 0,7 und der Abstand schrumpft auf null — zeigt den Kernsatz des Kapitels („Maximum Likelihood = kleinste KL-Divergenz“), der sonst nur aus Gleichungen besteht
- V4 [A] 04-die-varianz-schatzen — Quadrate um den wahren Mittelwert gegen Quadrate um den eigenen Mittelwert, der Fehlbetrag N(x̄−μ)² — erklärt sichtbar, warum Teilen durch N zu klein ist; der Beweis steht nur als Herleitung
- V11 [A] 07-prior-und-posterior — Posterior Wurf für Wurf, Beta(2,2) → Beta(9,5), Kurve wandert und wird schmaler — das Verfahren „Posterior ist der Prior des nächsten Wurfs“ steht als Zahlenreihe ohne Bild

## Editor-Lücken

Für die 22 neuen Vorschläge (15 ohne neue Funktion machbar, 6 mit Notbehelf, 1 mit L-Wunsch):
- L3 (Parameter-Sweep): 4 (V2, V6, V7, V19; Notbehelf: Zustände nacheinander per FadeIn oder CurveFamily-Glieder, Marker per MoveTo)
- L1 (Verschwinden): 2 (V7, V11; Notbehelf: alte Kurve bleibt grau stehen)
- L6 (Stichproben ziehen): 1 (V3; Notbehelf: 20 vorberechnete Intervalle erscheinen nacheinander)
- L2 (Morph): 1 hilfreich, nicht nötig (V18; Rechteck wird zur Glocke)
- L-neu: Zahlenstrahl-/Balken-Zählen mit „Skalierung der Fläche auf 1“ (Normieren) kommt in V10, V11, V13 vor; machbar mit Scale in y-Richtung, falls Scale nur gleichmäßig skaliert, dann FadeIn des fertigen Zustands.
Für die vorhandenen Szenen: k5rerwartung, k5rmse, k5rbessel, k5rprodukt, k5rloglik, k5rbayes, k5rentropie, k5rkreuz, k5rkl, k5rkreuzml müssen von MathTex auf Σ/∏/Arithmetik umgebaut werden (Σ mit Gewichten p_k·x_k als Summanden; ob die Σ-Operation Produkte p·log(1/q) als Summand anzeigt, ist beim Umbau zu prüfen). L3 bei k5likelihood, k5beta, k5posterior, k5entropie (laufender Punkt). L10 (Abspielknopf im Artikel) betrifft alle.

## Vorschläge

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Zwei Richtungen: von der Verteilung zu den Daten und zurück
- **Artikel:** content/ml/05-statistik-und-information/01-statistik-und-information.md
- **Stelle:** Worum es geht — „In Grundlagen 4 war die Verteilung immer bekannt, und gefragt war, wie wahrscheinlich bestimmte Daten sind …“
- **Art:** vorhandene Szene wiederverwenden (ml/k5richtung, dort Abb. 1 in Artikel 02), als Animation
- **Was zu sehen ist:** Links ein Kasten „Verteilung: θ = 0,7“, rechts ein Kasten „Daten: 7× Kopf in 10 Würfen“. Zwei Pfeile zwischen ihnen. Über dem Hinpfeil „P = 0,267“, unter dem Rückpfeil rot ein „θ = ?“.
- **Ablauf:** 1. Linker Kasten erscheint (FadeIn). 2. Hinpfeil zeichnet sich (Create), „P(7 Köpfe) = 0,267“ erscheint. 3. Rechter Kasten, vorher grau, wird betont (Indicate). 4. Rückpfeil zeichnet sich von rechts nach links, „θ = ?“ in Rot. 5. Unter dem Bild: „Dieses Kapitel: der Weg zurück“. — Haltepunkte: Schritt 4.
- **Verständnisproblem:** Das Kapitel dreht die Fragerichtung der Wahrscheinlichkeitsrechnung um; ohne das Bild bleibt „Statistik“ ein Wort.
- **Szenenname:** ml/k5richtung (gemeinsam mit Artikel 02)
- **Editor-Lücke:** machbar

### Artikel 02 — Schätzen aus einer Stichprobe (Soll 3, vorh. 3)

Keine neuen Vorschläge, die drei vorhandenen Szenen werden animiert (siehe unten). Verworfen: Rechenbild ∏ der Münzfolge — dieselbe Rechnung steht in Artikel 05 (k5rprodukt).

### Artikel 03 — Wie gut ist ein Schätzer? (Soll 4, vorh. 2)

### V2 [A] Der Standardfehler schrumpft, der Schätzer wird konsistent
- **Artikel:** content/ml/05-statistik-und-information/03-wie-gut-ist-ein-schatzer.md
- **Stelle:** Konsistenz — „Mehr Daten sollten eine Schätzung besser machen. Beim Mittelwert ist das so …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen x (Anteil der Köpfe) von 0 bis 1, y (Dichte) von 0 bis 12. Senkrechte Linie bei θ = 0,7 und ein waagerechtes Band von 0,6 bis 0,8 (ε = 0,1). Drei Glockenkurven (Normalnäherung der Stichprobenverteilung von N₁/N um 0,7): N = 10 (SE ≈ 0,145, Höhe ≈ 2,75), N = 40 (SE ≈ 0,0725, Höhe ≈ 5,5), N = 160 (SE ≈ 0,0362, Höhe ≈ 11,0). Textfeld mit der Fläche außerhalb des Bandes.
- **Ablauf:** 1. Achsen, θ-Linie und Band erscheinen. 2. N = 10 zeichnet sich (Create), Text „SE = √(0,21/10) ≈ 0,145“, Fläche außerhalb des Bandes ≈ 0,49. 3. N = 40: schmalere Kurve, SE ≈ 0,0725, außerhalb ≈ 0,17. 4. N = 160: SE ≈ 0,036, außerhalb ≈ 0,006. 5. Beschriftung „Bei jedem ε wird die Fläche außerhalb beliebig klein: konsistent“. Hinweis im Bild: Näherung durch die Normalverteilung. — Haltepunkte: Schritt 3 und 4.
- **Verständnisproblem:** „Konsistent“ ist eine Aussage über eine Folge von Stichprobenverteilungen für wachsendes N; die Definition P(|θ̂_N − θ| ≥ ε) → 0 hat bisher keine Anschauung.
- **Szenenname:** ml/k5konsistenz
- **Editor-Lücke:** machbar mit Notbehelf (drei Kurven nacheinander); sauber braucht L3 (N als Sweep)

### V3 [B] Konfidenzintervall: 19 von 20 Wiederholungen überdecken θ (Ausnahme: im Hintergrund-Kasten)
- **Artikel:** content/ml/05-statistik-und-information/03-wie-gut-ist-ein-schatzer.md
- **Stelle:** Hintergrund „Den Standardfehler selbst schätzen“ — „Deshalb liegt das Intervall ‚Schätzwert ± 2 Standardfehler‘ in etwa 95 % der gedachten Wiederholungen so …“
- **Art:** neue Animation (Ausnahme zum Hintergrund-Kasten, weil die frequentistische Aussage sonst abstrakt bleibt)
- **Was zu sehen ist:** Waagerechte Achse θ von 0,5 bis 0,9, senkrechte Linie bei θ = 0,7. Zwanzig Zeilen übereinander, je ein Schätzwert (Punkt) mit Intervall ±2·SE̅ (SE̅ = √(θ̂(1−θ̂)/100), N = 100 je Wiederholung). Die Anteile stammen aus einer festen Simulation von Binomial(100; 0,7), Startwert so gewählt, dass 19 der 20 Intervalle die Linie überdecken (blau), eins nicht (rot). Zähler „19 von 20“.
- **Ablauf:** 1. Linie θ = 0,7 und Achse. 2. Intervall 1 erscheint (Punkt, dann Balken), dann Intervall 2 … 20, jedes kurz nach dem vorigen. 3. Das verfehlende Intervall wird rot und mit Indicate betont. 4. Text „etwa 95 % der Wiederholungen überdecken den wahren Wert; ein einzelnes Intervall tut es oder nicht“. — Haltepunkte: 3.
- **Verständnisproblem:** Das Intervall ist zufällig, der Parameter fest; die 95 % beziehen sich auf das Verfahren, nicht auf ein berechnetes Intervall.
- **Szenenname:** ml/k5konfidenz
- **Editor-Lücke:** machbar mit Notbehelf (vorberechnete Intervalle); sauber braucht L6 (Stichproben ziehen)

### Artikel 04 — Die Varianz schätzen (Soll 3, vorh. 1)

### V4 [A] Quadrate um den wahren und um den eigenen Mittelwert
- **Artikel:** content/ml/05-statistik-und-information/04-die-varianz-schatzen.md
- **Stelle:** Teilen durch N unterschätzt die Varianz — „Die Verzerrung ist 𝔼[σ̂²_N] − σ² = −σ²/N …“ (nach der Herleitung, im Haupttext)
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Zahlenstrahl von 0 bis 4. Roter Strich bei μ = 2 (wahrer Erwartungswert). Ein Beispiel-Datensatz aus dem Artikel: Stichprobe (1, 2) (Punkte bei 1 und 2). Quadrate über jeder Abweichung (Seitenlänge = Abstand).
- **Ablauf:** 1. Zahlenstrahl, μ = 2 und die Punkte 1 und 2. 2. Graue Quadrate um μ: Seiten 1 und 0, Summe 1. 3. Der Mittelwert x̄ = 1,5 erscheint (grün). 4. Grüne Quadrate um x̄: zweimal Seite 0,5, Summe 0,5; Differenz 0,5 = N(x̄ − μ)² = 2·0,25 wird als Rest markiert („fehlt“). 5. Zweite Stichprobe (1, 3): x̄ = 2, beide Summen 2, Fehlbetrag 0. 6. Dritte Stichprobe (3, 3): x̄ = 3; um μ: 2, um x̄: 0, Fehlbetrag 2. 7. Text „Im Mittel über alle neun Stichproben fehlt σ² = 2/3 (𝔼[N(x̄−μ)²]) “. — Haltepunkte: 4 und 6.
- **Verständnisproblem:** Warum die Abweichungen vom eigenen Mittelwert im Mittel zu klein sind (der Mittelwert wird aus denselben Daten berechnet und liegt mitten zwischen ihnen).
- **Szenenname:** ml/k5mittelnaeher
- **Editor-Lücke:** machbar (Quadrate als Square, Seiten per Scale)

### V5 [A] Rechenbild: Quadratsumme der Wohnungsflächen
- **Artikel:** content/ml/05-statistik-und-information/04-die-varianz-schatzen.md
- **Stelle:** Teilen durch N unterschätzt die Varianz — „Für die Flächen der vier Wohnungen, 60, 40, 90 und 70 m², ist die Quadratsumme 25+625+625+25=1300 …“
- **Art:** neue Animation (Rechenbild, Editor-Operation Σ plus Arithmetik)
- **Was zu sehen ist:** Σ über i = 1 bis 4 von (xᵢ − 65)²; Summanden 25, 625, 625, 25 mit den Abweichungen −5, −25, 25, 5. Danach ÷ 4 = 325 m⁴ und ÷ 3 ≈ 433,3 m⁴.
- **Ablauf:** 1. Zahlen 60, 40, 90, 70 und x̄ = 65. 2. Summand für Summand: Abweichung, Quadrat, Zwischensumme 25 → 650 → 1275 → 1300. 3. ÷ 4 = 325 (Nenner N), daneben ÷ 3 ≈ 433,3 (Nenner N−1). — Haltepunkte: Zwischensumme 650.
- **Verständnisproblem:** Der Unterschied der beiden Schätzer an Zahlen.
- **Szenenname:** ml/k5rwohnung
- **Editor-Lücke:** machbar

### Artikel 05 — Die Likelihood (Soll 3, vorh. 3)

Keine neuen Vorschläge. Die Likelihood-Kurve zeigt zusätzlich, was „Daten fest, θ variiert“ heißt; die Gegenlesart (θ fest, Daten variieren) ist bereits in k5stichprobe/Grundlagen 4 abgedeckt.

### Artikel 06 — Die Maximum-Likelihood-Schätzung (Soll 4, vorh. 0)

### V6 [A] Gipfelsuche: die Steigung der Log-Likelihood wechselt das Vorzeichen
- **Artikel:** content/ml/05-statistik-und-information/06-die-maximum-likelihood-schatzung.md
- **Stelle:** Der Maximum-Likelihood-Schätzer — „Die Likelihood bewertet jeden Parameterwert. Der beste nach dieser Bewertung ist der, unter dem die Daten am wahrscheinlichsten sind.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen θ von 0 bis 1, y von −12 bis −5. Kurve ℓ(θ) = 7 ln θ + 3 ln(1 − θ) (Wert am Gipfel −6,109 bei θ = 0,7). Eine Tangente mit Steigungsdreieck, die wandert, und ein Textfeld ℓ′(θ) = 7/θ − 3/(1−θ).
- **Ablauf:** 1. Achsen und Kurve zeichnen sich (Create). 2. Tangente bei θ = 0,4, Steigung ℓ′ = 17,5 − 5 = 12,5 („bergauf“). 3. Tangente wandert zu θ = 0,7, waagerecht, ℓ′ = 10 − 10 = 0, Gipfel rot markiert. 4. Tangente bei θ = 0,9, ℓ′ = 7,78 − 30 ≈ −22,2 („bergab“). 5. Text: „Vorzeichenwechsel + → − : höchster Punkt“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Warum „Ableitung null“ genau den Maximum-Likelihood-Schätzer liefert und warum der Vorzeichenwechsel (nicht nur die Nullstelle) zählt.
- **Szenenname:** ml/k5gipfelsuche
- **Editor-Lücke:** machbar mit Notbehelf (drei Tangenten nacheinander); sauber braucht L3

### V7 [A] Eine Glocke wandert und wird eng: Maximum Likelihood für μ und σ²
- **Artikel:** content/ml/05-statistik-und-information/06-die-maximum-likelihood-schatzung.md
- **Stelle:** Die Normalverteilung: der Mittelwert — „Vier Messungen derselben Spannung ergeben 4,9, 5,3, 5,1 und 4,7 V …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achse x (Spannung in V) von 4 bis 6, y (Dichte) von 0 bis 2. Die vier Messwerte als Punkte auf der Achse. Eine Normalverteilungsdichte mit σ = 0,2236 V (σ² = 0,05), Höhe 1,78. Senkrechte Linien von jedem Messwert bis zur Kurve (ihre Längen sind die Dichtewerte). Textfeld mit der Quadratsumme Σ(xᵢ − μ)².
- **Ablauf:** 1. Vier Punkte erscheinen. 2. Glocke bei μ = 4,6: kurze Linien, Quadratsumme 0,84. 3. Glocke gleitet nach μ = 5,0 (Shift): Linien am längsten, Quadratsumme 0,20 (Minimum). 4. Glocke gleitet weiter nach μ = 5,4: Quadratsumme wieder 0,84. 5. Jetzt bei μ = 5,0: breite Glocke σ² = 0,25 (flach), dann schmale σ² = 0,01 (die Linien außen werden sehr kurz), dann σ² = 0,05 (Q/N): „passt“. — Haltepunkte: Schritt 3 und 5.
- **Verständnisproblem:** Warum der Mittelwert herauskommt und nicht vom Rauschen σ² abhängt; warum die ML-Varianz Q/N ist (zu breit: Dichte klein überall, zu schmal: Dichte außen fast null).
- **Szenenname:** ml/k5glocke
- **Editor-Lücke:** machbar mit Notbehelf (die Glocken nacheinander, Shift für die μ-Bewegung); sauber braucht L3 und L1

### V8 [A] Rechenbild: Mittelwert und Quadratsumme der vier Spannungen
- **Artikel:** content/ml/05-statistik-und-information/06-die-maximum-likelihood-schatzung.md
- **Stelle:** Die Normalverteilung: der Mittelwert — „Für die vier Spannungen ist μ̂_ML = ¼(4,9+5,3+5,1+4,7) = 5,0 V.“ (und Rechenbeispiel zur Varianz im folgenden Unterabschnitt)
- **Art:** neue Animation (Rechenbild, Editor-Operation Σ plus Arithmetik)
- **Was zu sehen ist:** Σ xᵢ mit 4,9 + 5,3 + 5,1 + 4,7 = 20,0, ÷ 4 = 5,0 V. Dann Σ (xᵢ − 5,0)² mit −0,1; 0,3; 0,1; −0,3 → 0,01 + 0,09 + 0,01 + 0,09 = 0,2 V², ÷ 4 = 0,05 V², Wurzel ≈ 0,224 V.
- **Ablauf:** 1. Summanden einzeln einlaufen, Zwischensumme 4,9 → 10,2 → 15,3 → 20,0. 2. ÷ 4 = 5,0. 3. Abweichungen, Quadrate, Summe 0,2. 4. ÷ 4 = 0,05; Wurzel 0,224. — Haltepunkte: 2 und 4.
- **Verständnisproblem:** Rechenweg an den konkreten Zahlen.
- **Szenenname:** ml/k5rspannung
- **Editor-Lücke:** machbar

### V9 [B] Umrechnung des Parameters: der Gipfel wandert mit
- **Artikel:** content/ml/05-statistik-und-information/06-die-maximum-likelihood-schatzung.md
- **Stelle:** Umrechnen eines Maximum-Likelihood-Schätzers — „Oft interessiert nicht der Parameter selbst, sondern eine Größe, die aus ihm folgt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen θ von 0 bis 1, y von 0 bis 0,0025: Likelihood θ⁷(1−θ)³, Gipfel (0,7; 0,00222) rot. Darunter eine zweite Achse „Chance η = θ/(1−θ)“ mit Teilstrichen bei θ = 0,3 → 0,43; 0,5 → 1; 0,7 → 2,33; 0,9 → 9. Dieselbe Kurve als Parameterkurve (η(θ), L(θ)) auf der η-Achse.
- **Ablauf:** 1. Kurve und Gipfel in θ. 2. Senkrechte Linien vom Gipfel und von drei weiteren Punkten nach unten auf die η-Achse. 3. Die Kurve wird auf der η-Achse nachgezeichnet: gestreckt, aber gleich hoch, Gipfel bei η = 7/3. 4. Text „dieselben Funktionswerte, nur neu benannt“. — Haltepunkte: 3.
- **Verständnisproblem:** Warum die Likelihood das Umbenennen übersteht, die Dichte (Abschnitt 7) aber nicht.
- **Szenenname:** ml/k5umrechnung
- **Editor-Lücke:** machbar (ParametricCurve)

### Artikel 07 — Prior und Posterior (Soll 5, vorh. 3)

### V10 [A] Die Münzkiste: Prior × Likelihood ÷ Evidenz als Balken
- **Artikel:** content/ml/05-statistik-und-information/07-prior-und-posterior.md
- **Stelle:** Der Satz von Bayes für Parameter — „In einer Kiste liegen vier Münzen: eine, die mit der Wahrscheinlichkeit ¼ Kopf zeigt, zwei faire …“
- **Art:** neue Animation (ergänzt das Rechenbild k5rbayes für P(𝒟))
- **Was zu sehen ist:** Vier Stem-Felder (a) bis (d) nebeneinander, je mit Achse θ ∈ {¼, ½, ¾}. (a) Prior: 0,25; 0,5; 0,25. (b) Likelihood θ³(1−θ): 3/256 ≈ 0,0117; 16/256 = 0,0625; 27/256 ≈ 0,105. (c) Produkt: 0,00293; 0,03125; 0,02637, Summe 31/512 ≈ 0,0605. (d) Posterior (Produkt ÷ 31/512): 3/62 ≈ 0,048; 16/31 ≈ 0,516; 27/62 ≈ 0,435.
- **Ablauf:** 1. (a) Prior-Stäbe wachsen. 2. (b) Likelihood-Stäbe (anderer Maßstab) wachsen, mit Pfeil „×“. 3. (c) Produktstäbe, daneben Summe 31/512. 4. (d) Stäbe aus (c) strecken sich auf die Gesamthöhe 1 (÷ 31/512), die Mitte ist am höchsten. 5. Text: „Maximum Likelihood: ¾. Nach Bayes: ½ (doppelt so viele faire Münzen).“ — Haltepunkte: Schritt 2 und 4.
- **Verständnisproblem:** Wie der Satz von Bayes Parameterwerte neu gewichtet; warum die Münze mit der größten Likelihood nicht die wahrscheinlichste ist.
- **Szenenname:** ml/k5muenzkiste
- **Editor-Lücke:** machbar (Normieren per Scale in y-Richtung oder FadeIn des Endzustands)

### V11 [A] Der Posterior wandert Wurf für Wurf
- **Artikel:** content/ml/05-statistik-und-information/07-prior-und-posterior.md
- **Stelle:** Konjugierte Prior-Verteilungen — „Man kann den Posterior Wurf für Wurf aktualisieren: Der Posterior nach einem Wurf ist der Prior für den nächsten.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen θ von 0 bis 1, Dichte von 0 bis 3,5. Oben eine Reihe von zehn Kreisen für die Würfe 1, 0, 1, 1, 0, 1, 1, 0, 1, 1 (gefüllt = Kopf). Die Beta-Dichten Beta(2,2) (Höhe 1,5), Beta(3,2), Beta(3,3), Beta(4,3), Beta(5,3), Beta(5,4), Beta(6,4), Beta(7,4), Beta(7,5), Beta(8,5), Beta(9,5) (Höhe 3,10). Ein Punkt auf der Achse für den Erwartungswert (0,5 → 0,6 → 0,5 → 0,571 → 0,625 → 0,556 → 0,6 → 0,636 → 0,583 → 0,615 → 0,643). Textfeld „Beta(α₁, α₀)“.
- **Ablauf:** 1. Achsen und Prior Beta(2,2). 2. Erster Wurf (Kopf): Kreis gefüllt, neue Kurve Beta(3,2) verschiebt sich nach rechts, die alte bleibt grau; Textfeld wechselt. 3. Wurf für Wurf, nach jedem Wurf eine neue Kurve und ein neuer Erwartungswert-Punkt. 4. Nach dem zehnten Wurf Beta(9,5), rot, Gipfel 2/3. 5. Text „Alle zehn Würfe auf einmal gerechnet: dasselbe Beta(9,5)“. — Haltepunkte: nach Wurf 1, nach Wurf 3 (zurück bei 0,5) und am Ende.
- **Verständnisproblem:** Beta-Parameter als gezählte Einsen und Nullen; Reihenfolge der Würfe spielt keine Rolle; Posterior wird schmaler.
- **Szenenname:** ml/k5wurffuerwurf
- **Editor-Lücke:** machbar mit Notbehelf (alte Kurven bleiben grau stehen); sauber braucht L1 und L3

### Artikel 08 — Die Maximum-a-posteriori-Schätzung (Soll 3, vorh. 0)

### V12 [A] Der Strafterm hält den Gipfel vom Rand zurück
- **Artikel:** content/ml/05-statistik-und-information/08-die-maximum-a-posteriori-schatzung.md
- **Stelle:** Der Prior als Strafterm — „Die Form (7.1) zeigt, was der Prior beim MAP-Schätzer tut: Er addiert zur Log-Likelihood einen Term …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Felder. (a) Daten: dreimal Kopf in drei Würfen. Achsen θ von 0,02 bis 0,98, y von −10 bis 1,5. Blau ℓ(θ) = 3 ln θ (steigt bis θ = 1, Maximum am Rand), grün der Strafterm ln p(θ) = ln 6 + ln θ + ln(1−θ) (bei ½: 0,405; bei 0,9: −0,616; fällt zu beiden Rändern), rot die Summe ln 6 + 4 ln θ + ln(1−θ) mit Gipfel bei 0,8. (b) 30 Köpfe in 30 Würfen: ℓ = 30 ln θ, Strafterm unverändert, Summe ln 6 + 31 ln θ + ln(1−θ), Gipfel bei 31/32 ≈ 0,969.
- **Ablauf:** 1. (a) ℓ zeichnet sich, Marker am Rand θ = 1 („ML = 1“). 2. Strafterm erscheint. 3. Die Summe zeichnet sich, Marker rutscht von 1 auf 0,8 („MAP = 4/5“). 4. (b) dieselben drei Kurven mit 30 Würfen: die blaue Kurve ist viel steiler, der Strafterm kaum sichtbar, Marker bei 0,969. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** „Prior als Strafterm“ und warum der Strafterm bei vielen Daten an Gewicht verliert.
- **Szenenname:** ml/k5strafterm
- **Editor-Lücke:** machbar

### V13 [A] Gauß-Prior: Prior und Messung ziehen den Posterior zwischen sich
- **Artikel:** content/ml/05-statistik-und-information/08-die-maximum-a-posteriori-schatzung.md
- **Stelle:** Ein Gauß-Prior für einen Mittelwert — „Dieselbe Idee funktioniert bei stetigen Daten. Ein Sensor misst eine Spannung mit einem unbekannten Versatz μ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Felder (a) N = 4 und (b) N = 36, Achse μ in mV von −3 bis 4, y von 0 bis 1,4. Grün Prior 𝒩(0; 1²) (Höhe 0,399). (a) Orange Likelihood um x̄ = 1,5 mit Breite σ/√N = 2/√4 = 1 (Höhe 0,399); blau Posterior 𝒩(0,75; 0,5) (Höhe 0,564, Breite s ≈ 0,71). (b) Likelihood Breite 2/6 ≈ 0,333 (Höhe 1,197); Posterior bei 1,35 mit Breite s ≈ 0,316 (Höhe 1,262).
- **Ablauf:** 1. (a) Prior erscheint. 2. Likelihood erscheint rechts davon. 3. Posterior erscheint in der Mitte bei 0,75, schmaler als beide; Pfeil „Gewichte 1 : 1“. 4. (b) dasselbe mit N = 36: die Likelihood ist schmal, der Posterior liegt bei 1,35, nahe der Messung; Pfeil „Gewichte 9 : 1“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Gewichtetes Mittel mit den Kehrwerten der Varianzen; der Prior wirkt wie eine zusätzliche Messung.
- **Szenenname:** ml/k5gaussprior
- **Editor-Lücke:** machbar

### V14 [A] Rechenbild: gewichtetes Mittel von Messung und Prior
- **Artikel:** content/ml/05-statistik-und-information/08-die-maximum-a-posteriori-schatzung.md
- **Stelle:** Ein Gauß-Prior für einen Mittelwert — „Es sei σ = 2 mV, τ = 1 mV und μ₀ = 0. Aus N = 4 Messungen ergibt sich x̄ = 1,5 mV …“
- **Art:** neue Animation (Rechenbild, Editor-Operation Skalarprodukt plus Division)
- **Was zu sehen ist:** (a) (1; 1) · (1,5; 0) = 1·1,5 + 1·0 = 1,5, ÷ (1 + 1) = 0,75 mV. (b) (9; 1) · (1,5; 0) = 13,5, ÷ 10 = 1,35 mV. Beschriftung der Gewichte: N/σ² und 1/τ².
- **Ablauf:** 1. Gewichtsvektor und Wertevektor erscheinen. 2. Komponente für Komponente multiplizieren, Summe. 3. Division durch die Gewichtssumme. 4. Dasselbe für N = 36. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Wie das Gewicht der Daten mit N wächst.
- **Szenenname:** ml/k5rgauss
- **Editor-Lücke:** machbar

### Artikel 09 — Informationsgehalt und Entropie (Soll 4, vorh. 4)

### V15 [A] Informationsgehalt: die Überraschungskurve
- **Artikel:** content/ml/05-statistik-und-information/09-informationsgehalt-und-entropie.md
- **Stelle:** Der Informationsgehalt — „Die Nachricht ‚Die Münze zeigt Kopf‘ überrascht wenig, die Nachricht ‚Der Würfel zeigt viermal hintereinander eine Sechs‘ deutlich mehr …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen p von 0 bis 1, I in bit von 0 bis 7. Kurve I(p) = log₂(1/p) (für p ab 0,02). Marker bei p = 1 (0 bit), p = ½ (1 bit), p = 1/6 (2,585 bit), p = 1/32 (5 bit). Daneben zwei Münzen mit Pfeilen.
- **Ablauf:** 1. Achsen, Kurve zeichnet sich von rechts (p = 1, sicher: 0 bit) nach links (p klein: steil). 2. Marker p = ½ → 1 bit (Münze), p = 1/6 → 2,585 bit (Sechs), p = 1/32 → 5 bit (Karte). 3. Additivität: zwei unabhängige faire Münzen, beide Kopf, p = ¼; der Marker bei ¼ steht bei 2 bit = 1 + 1; Klammerpfeile „1 bit + 1 bit“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Warum der Logarithmus (Produkte der Wahrscheinlichkeiten werden zu Summen der Überraschungen) und was „bit“ misst.
- **Szenenname:** ml/k5informationsgehalt
- **Editor-Lücke:** machbar

### Artikel 10 — Kreuzentropie und KL-Divergenz (Soll 3, vorh. 4)

Zusammenlegen: **k5rkl entfällt**, seine Rechnung (Σ pₖ log₂(pₖ/qₖ) = 1 + 0,25 − 0,125 − 0,25 = 0,875 bit) wird als Σ-Operation in k5kl (Abb. 19) eingebaut: oben die Stems p und q, darunter die Beiträge, rechts die laufende Summe. Verworfen: „KL ist kein Abstand“ als Stem-Paar mit 0,511 gegen 0,368 (Maximum 3).

### Artikel 11 — Die größte Entropie (Soll 3, vorh. 1)

### V16 [A] Die Gleichverteilung hat die größte Entropie
- **Artikel:** content/ml/05-statistik-und-information/11-die-grote-entropie.md
- **Stelle:** Die Gleichverteilung hat die größte Entropie — „Eine faire Münze ist unvorhersagbarer als eine verbogene, ein fairer Würfel unvorhersagbarer als ein gezinkter.“
- **Art:** neue Animation
- **Was zu sehen ist:** Vier Balken über A, B, C, D, Achse p von 0 bis 0,6. Zustand 1: (½, ¼, ⅛, ⅛), H = 1,75 bit. Zustand 2: (0,4; 0,3; 0,2; 0,1), H ≈ 1,846 bit. Zustand 3: (¼, ¼, ¼, ¼), H = 2 bit = log₂ 4. Fortlaufendes Textfeld H und ein Balken „log₂ 4 − H = D_KL(p‖u)“ (0,25 bit im Zustand 1).
- **Ablauf:** 1. Zustand 1; Textfeld H = 1,75, Abstand zur Obergrenze 0,25. 2. Balken gleichen sich an (Zwischenzustand 2). 3. Zustand 3: alle gleich hoch, H = 2, Abstand 0. 4. Text „Jede Ungleichheit lässt sich zum Sparen nutzen (kürzere Codewörter)“. — Haltepunkte: 3.
- **Verständnisproblem:** Entropie als Maß der Unvorhersagbarkeit, größter Wert bei Gleichheit; KL zur Gleichverteilung als Abstand zur Obergrenze.
- **Szenenname:** ml/k5gleichverteilung
- **Editor-Lücke:** machbar mit Notbehelf (Balken per MoveTo/Scale); sauber braucht L3

### V17 [A] Differentielle Entropie kann negativ sein und hängt von der Einheit ab
- **Artikel:** content/ml/05-statistik-und-information/11-die-grote-entropie.md
- **Stelle:** Die Entropie einer Dichte — „Das kleine h soll daran erinnern, dass sie sich anders verhält als die Entropie H einer diskreten Verteilung.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen x von 0 bis 2,2, p(x) von 0 bis 8,5. Gleichverteilung auf [0, a] als Rechteck der Höhe 1/a, Fläche stets 1. Drei Zustände: a = ⅛ (Höhe 8, h = ln ⅛ ≈ −2,079 nat), a = 1 (Höhe 1, h = 0), a = 2 (Höhe ½, h = ln 2 ≈ 0,693). Zusätzlich ein Textfeld „in Millimetern statt Metern: h + ln 1000 ≈ h + 6,91“.
- **Ablauf:** 1. Das hohe schmale Rechteck a = ⅛ erscheint, h negativ (rot). 2. Es wird breiter (a = 1), h = 0. 3. Noch breiter (a = 2), h positiv. 4. Text „h misst die Ausbreitung der Dichte, nicht Bits“. 5. Einheit Millimeter: Achse neu beschriftet, derselbe Rechteckzustand, h um 6,91 größer. — Haltepunkte: 1 und 5.
- **Verständnisproblem:** Warum dasselbe Zeichen H/h einmal nie negativ ist (diskret, p ≤ 1) und einmal negativ sein kann (Dichtewerte größer 1).
- **Szenenname:** ml/k5diffentropie
- **Editor-Lücke:** machbar mit Notbehelf (drei Rechtecke nacheinander); sauber braucht L3

### V18 [A] Bei gleicher Varianz hat die Normalverteilung die größte Entropie
- **Artikel:** content/ml/05-statistik-und-information/11-die-grote-entropie.md
- **Stelle:** Die Normalverteilung hat bei fester Varianz die größte Entropie — „Weiß man von einem Rauschen nur, wie groß seine Leistung ist, also seine Varianz …“
- **Art:** neue Animation
- **Was zu sehen ist:** Achse x von −3 bis 3, p(x) von 0 bis 0,5. Beide Dichten haben die Varianz 1: Gleichverteilung auf [−√3; √3] ≈ [−1,732; 1,732] (Höhe 1/(2√3) ≈ 0,289, h = ln(2√3) ≈ 1,242 nat) und Normalverteilung 𝒩(0, 1) (Höhe 0,399, h ≈ 1,419 nat). Differenz 0,176 nat als Klammer.
- **Ablauf:** 1. Das Rechteck zeichnet sich, Text „Varianz 1, h = 1,242“. 2. Die Glocke zeichnet sich darüber, Text „Varianz 1, h = 1,419“. 3. Klammer „+0,176 nat = D_KL(Gleichverteilung‖Normalverteilung)“. 4. Text „Mehr Entropie heißt: weniger zusätzliche Struktur angenommen“. — Haltepunkte: 3.
- **Verständnisproblem:** Der zweite Grund für normalverteiltes Rauschen (größte Entropie bei fester Varianz); die Entropie-Zahlen des Artikels bekommen ein Bild.
- **Szenenname:** ml/k5normalmax
- **Editor-Lücke:** machbar (ein Morph Rechteck → Glocke wäre schöner, braucht L2, ist aber nicht nötig)

### Artikel 12 — Maximum Likelihood und KL-Divergenz (Soll 3, vorh. 1)

### V19 [A] Maximum Likelihood heißt kleinste KL-Divergenz: die Kreuzentropie über θ
- **Artikel:** content/ml/05-statistik-und-information/12-maximum-likelihood-und-kl-divergenz.md
- **Stelle:** Maximum Likelihood heißt kleinste KL-Divergenz — „Nach (9.2) ist die Kreuzentropie die Entropie plus die KL-Divergenz.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen θ von 0,05 bis 0,95, y in nat von 0 bis 1,8. Kurve H(p̂, q(θ)) = 0,7 ln(1/θ) + 0,3 ln(1/(1−θ)) = −ℓ(θ)/10 (bei 0,1: 1,643; bei 0,5: 0,693; bei 0,7: 0,611; bei 0,9: 0,765). Waagerechte gestrichelte Linie bei H(p̂) = 0,611 (untere Grenze, hängt nicht von θ ab). Ein Marker auf der Kurve und eine Maßlinie (Measure) zwischen Kurve und Linie, die den Abstand D_KL anzeigt.
- **Ablauf:** 1. Achsen, Kurve zeichnet sich. 2. Die Linie H(p̂) = 0,611 erscheint, Text „unabhängig von θ“. 3. Marker bei θ = 0,5: Kurvenwert 0,693, Abstand 0,082 = D_KL(p̂‖q(0,5)). 4. Marker bei θ = 0,9: Abstand 0,154. 5. Marker rutscht auf θ = 0,7: Abstand 0, Kurve berührt die Linie. 6. Text „Kleinste Kreuzentropie = größte Likelihood = kleinste KL-Divergenz“. — Haltepunkte: Schritt 3 und 5.
- **Verständnisproblem:** Wie aus der Zerlegung −ℓ/N = H(p̂) + D_KL ein Maximum der Likelihood als kleinster Abstand zur empirischen Verteilung folgt.
- **Szenenname:** ml/k5mlkl
- **Editor-Lücke:** machbar mit Notbehelf (drei Marker nacheinander per MoveTo); sauber braucht L3

### V20 [B] Aus der Summe über Würfe wird die Summe über Kategorien
- **Artikel:** content/ml/05-statistik-und-information/12-maximum-likelihood-und-kl-divergenz.md
- **Stelle:** Die Log-Likelihood als Kreuzentropie — „Die Log-Likelihood ist eine Summe über die Datenpunkte, ein Summand je Datenpunkt.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zehn Kärtchen in einer Reihe für die Würfe 1, 0, 1, 1, 0, 1, 1, 0, 1, 1 (Kopf = blau, Zahl = orange), unter jedem der Summand für das Modell θ = 0,7: ln(1/0,7) ≈ 0,357 für Kopf, ln(1/0,3) ≈ 1,204 für Zahl. Rechts zwei Säulen „Kopf“ und „Zahl“ mit den Höhen p̂ = 0,7 und 0,3.
- **Ablauf:** 1. Zehn Kärtchen erscheinen. 2. Die sieben blauen wandern (Shift) in die Säule „Kopf“, die drei orangen in „Zahl“; die Summe 7·0,357 + 3·1,204 = 6,109 steht darunter. 3. Die Säulenhöhen werden auf Anteile normiert: 0,7 und 0,3 (p̂). 4. Teilt man 6,109 durch 10, entsteht 0,7·0,357 + 0,3·1,204 = 0,611: die Kreuzentropie. — Haltepunkte: 2.
- **Verständnisproblem:** Warum Datenpunkte derselben Kategorie zusammengefasst werden dürfen und die Häufigkeiten N_k/N als Gewichte auftreten.
- **Szenenname:** ml/k5umsortieren
- **Editor-Lücke:** machbar

### Artikel 13 — Das Wichtigste bis hier (Soll 2, vorh. 0)

### V21 [A] Kapitelkarte: vom Schätzen zur Information
- **Artikel:** content/ml/05-statistik-und-information/13-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt aus zwei Werkzeugen: dem Erwartungswert über gedachte Wiederholungen der Daten und dem Logarithmus einer Wahrscheinlichkeit.“
- **Art:** neue Animation (Zusammenschau)
- **Was zu sehen ist:** Zwei Ketten aus Kästen. Obere Kette (Erwartungswert über gedachte Wiederholungen): Daten und Modell → Schätzer (Verzerrung, Varianz, MSE) → Likelihood → Maximum Likelihood → Prior und Posterior → MAP. Untere Kette (Logarithmus): Informationsgehalt → Entropie → Kreuzentropie und KL-Divergenz → größte Entropie. Roter Pfeil zwischen „Maximum Likelihood“ und „KL-Divergenz“ mit „Satz 11.2: ML = kleinste KL“. Ein Hinweis „Log-Likelihood = Summe“ an der Likelihood.
- **Ablauf:** 1. Obere Kette erscheint Kasten für Kasten (je ein FadeIn). 2. Untere Kette ebenso. 3. Der rote Pfeil zeichnet sich zuletzt. — Haltepunkte: 3.
- **Verständnisproblem:** Das Kapitel besteht aus zwei Ketten, die sich im Satz „Maximum Likelihood = kleinste KL-Divergenz“ treffen; das sieht man in der Tabelle nicht.
- **Szenenname:** ml/k5kapitelkarte
- **Editor-Lücke:** machbar (TextBox, LabeledArrow)

### V22 [B] Maximum Likelihood = kleinste KL-Divergenz (Wiederholung)
- **Artikel:** content/ml/05-statistik-und-information/13-das-wichtigste-bis-hier.md
- **Stelle:** Die Antwort in drei Sätzen — „… und Maximum Likelihood heißt genau, die Modellverteilung mit der kleinsten KL-Divergenz von der empirischen Verteilung der Daten zu wählen.“
- **Art:** vorhandene Szene wiederverwenden (ml/k5mlkl aus V19, Artikel 12), gerafft: nur der Gipfel (Marker rutscht von 0,5 auf 0,7, Abstand schrumpft auf 0)
- **Was zu sehen ist / Ablauf:** wie V19, Schritte 3 bis 5.
- **Verständnisproblem:** Wiederholung der Kernaussage am Kapitelende.
- **Szenenname:** ml/k5mlkl
- **Editor-Lücke:** machbar

## Vorhandene Abbildungen

- ml/k5richtung (02-schatzen-aus-einer-stichprobe, Abb. 1): animieren ja — Schritte: 1. Kasten „Verteilung“, 2. Hinpfeil mit „P = 0,267“, 3. Kasten „Daten“, 4. Rückpfeil mit „θ = ?“ | Lücke: machbar (siehe V1)
- ml/k5stichprobe (02, Abb. 2): animieren ja — Schritte: 1. (a) Gleichverteilung auf {1, 2, 3} (drei Stäbe ⅓), 2. neun Stichproben (1,1) … (3,3) erscheinen als Punkte mit ihrem Mittelwert, 3. sie fallen auf die fünf Mittelwerte und bilden die Stäbe 1/9, 2/9, 3/9, 2/9, 1/9 von (b), 4. Pfeil „gleicher Erwartungswert 2, halbe Varianz“ | Lücke: machbar mit Notbehelf (Stäbe nacheinander); L6/L7 für das echte Zählen
- ml/k5rerwartung (02, Abb. 3): animieren ja, aktuell nur MathTex — Schritte: 1. Σ x·P: 1·1/9 + 1,5·2/9 + 2·3/9 + 2,5·2/9 + 3·1/9 = 2, 2. Σ (x−2)²·P = 1/3 | Lücke: machbar (Σ-Operation)
- ml/k5zielscheibe (03, Abb. 4): animieren ja — Schritte: 1. Scheibe und rotes Kreuz, 2. in (a) erscheinen die acht Punkte nacheinander, Schwerpunkt-Marker in der Mitte, 3. (b) streuende Punkte, 4. (c)/(d): Schwerpunkt um (0,5; 0,35) verschoben, Pfeil „Verzerrung“ | Lücke: machbar
- ml/k5rmse (03, Abb. 5): animieren ja, aktuell nur MathTex — Schritte: 1. Σ P(x)(0,9x − 2)² über die fünf Werte (Summanden 0,134; 0,094; 0,013; 0,014; 0,054, Summe 0,31), 2. Zerlegung 0,04 + 0,27 | Lücke: machbar (Σ-Operation)
- ml/k5rbessel (04, Abb. 6): animieren ja, aktuell nur MathTex — Schritte: 1. Σ σ̂²_N·P = 0·3/9 + 0,25·4/9 + 1·2/9 = 1/3, 2. Σ σ̂²_{N−1}·P = 0·3/9 + 0,5·4/9 + 2·2/9 = 2/3 = σ² | Lücke: machbar
- ml/k5likelihood (05, Abb. 7): animieren ja — Schritte: 1. Achsen und Kurve (a) zeichnen sich, 2. Marker bei θ = 0,5 (0,000977), dann 0,6 (0,00179), 0,7 (Gipfel, 0,00222), 0,8 (0,00168), 3. Verhältnis 2,28 als Klammer, 4. (b) ln-Kurve mit Gipfel −6,109 | Lücke: machbar mit Notbehelf; sauber L3
- ml/k5rprodukt (05, Abb. 8): animieren ja, aktuell nur MathTex — Schritte: ∏ über zehn Faktoren 0,7; 0,3; 0,7; 0,7; 0,3; 0,7; 0,7; 0,3; 0,7; 0,7, Zwischenprodukte, Ergebnis 0,00222 | Lücke: machbar (∏-Operation)
- ml/k5rloglik (05, Abb. 9): animieren ja, aktuell nur MathTex — Schritte: Σ über zehn Summanden ln 0,7 ≈ −0,357 (sieben-mal) und ln 0,3 ≈ −1,204 (dreimal), Ergebnis −6,109 | Lücke: machbar (Σ-Operation)
- ml/k5rbayes (07, Abb. 10): animieren ja, aktuell nur MathTex — Schritte: Σ Likelihood × Anteil: 3/256·¼ + 16/256·½ + 27/256·¼ = 31/512 | Lücke: machbar; ergänzt durch V10
- ml/k5beta (07, Abb. 11): animieren ja — Schritte: 1. Beta(1,1) (Gerade), 2. Beta(2,2) mit Gipfel ½, 3. Beta(5,2) mit Gipfel 0,8, 4. Beta(9,5) mit Gipfel ⅔, Höhe 3,10, schmaler | Lücke: machbar mit Notbehelf; sauber L3 (α als Sweep)
- ml/k5posterior (07, Abb. 12): animieren ja — Schritte: 1. Prior Beta(2,2), 2. Likelihood ×1320, 3. Produkt, 4. Aufskalieren zum Posterior Beta(9,5), 5. gepunktete Linien 0,7 / ⅔ / 9/14 | Lücke: machbar
- ml/k5rentropie (09, Abb. 13): animieren ja, aktuell nur MathTex — Schritte: Σ pₖ log₂(1/pₖ) = ½·1 + ¼·2 + ⅛·3 + ⅛·3 = 1,75 | Lücke: machbar
- ml/k5code (09, Abb. 14): animieren ja — Schritte: 1. Wurzel, Kanten 0/1 zeichnen sich, 2. Blätter A (0), B (10), C (110), D (111) mit pₖ, 3. Marker läuft den Weg für die Folge 0110100: 0 → A, zurück zur Wurzel, 110 → C, 10 → B, 0 → A; Ausgabe „A C B A“ wächst | Lücke: machbar (Shift/MoveAlongPath)
- ml/k5rcode (09, Abb. 15): animieren ja, ist bereits echte Operation (DotProduct): p·l = ½·1 + ¼·2 + ⅛·3 + ⅛·3 = 1,75 | Lücke: machbar
- ml/k5entropie (09, Abb. 16): animieren ja — Schritte: 1. Achsen, Kurve H_b(θ) zeichnet sich, 2. Punkt läuft von θ = 0 über 0,5 (1 bit, Gipfel) nach 1, 3. Marker bei 0,7 (0,881) und 0,9 (0,469) | Lücke: machbar mit Notbehelf; sauber L3
- ml/k5rkreuz (10, Abb. 17): animieren ja, aktuell nur MathTex — Schritte: Σ pₖ·l′ₖ = ½·3 + ¼·3 + ⅛·2 + ⅛·1 = 2,625 | Lücke: machbar
- ml/k5rkl (10, Abb. 18): **entfällt, wird mit k5kl zusammengelegt** (Σ pₖ log₂(pₖ/qₖ) = 1 + 0,25 − 0,125 − 0,25 = 0,875) | Lücke: machbar
- ml/k5kl (10, Abb. 19): animieren ja — Schritte: 1. (a) p blau, q rot als Stäbe, 2. (b) die vier Beitragsbalken nacheinander (1; 0,25; −0,125; −0,25), 3. laufende Summe 1 → 1,25 → 1,125 → 0,875 | Lücke: machbar
- ml/k5lnx (10, Abb. 20): animieren ja — Schritte: 1. ln x zeichnet sich, 2. Punkt (1, 0), Tangente y = x − 1 wächst heraus, 3. senkrechte Abstände bei x = 0,5 (−0,693 gegen −0,5) und x = 2 (0,693 gegen 1) | Lücke: machbar
- ml/k5klflaeche (11, Abb. 21): animieren ja — Schritte: 1. (a) p = 𝒩(0, 1) und q = 𝒩(1, 4), 2. (b) der Integrand p ln(p/q) zeichnet sich, 3. blaue Fläche (−1,85 bis 1,18) wächst, 4. rote Fläche wächst, 5. Gesamtfläche 0,443 | Lücke: machbar
- ml/k5rkreuzml (12, Abb. 22): animieren ja, aktuell nur MathTex — Schritte: Σ p̂ₖ ln(1/qₖ) für θ = 0,5: 0,7 ln 2 + 0,3 ln 2 = 0,693; für θ = 0,7: 0,7·0,357 + 0,3·1,204 = 0,611 | Lücke: machbar
