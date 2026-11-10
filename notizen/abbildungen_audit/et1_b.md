# Abbildungen und Animationen: Paket et1_b

Hefte: `content/et1/05-quellen-und-ersatzquellen/` (13 Artikel), `06-zweitore/` (13), `07-leistung-und-anpassung/` (9), `08-maschenstrom-und-knotenpotential/` (12). Stand 09.11.2026.
Kürzel: L1 Verschwinden, L2 Umformen, L3 Parameter/Zeit, L7 weitere Operationen, L9 Zellen einzeln.
Hinweis: Keine der 42 vorhandenen Szenen dieses Pakets hat ein Rechenbild (`computations` überall leer) oder eine Zeitachse. Alle Schaltbilder bestehen aus Component/Line/Dot/Text, Kennlinienbilder aus Axes/FunctionGraph/Band.
Allgemeine Technik der Schaltungs-Animationen (nicht bei jedem Vorschlag wiederholt): Bauteile und Leitungen erscheinen per FadeIn/Create nacheinander; „Strom fließt“ = je ein kleiner Dot (Ladungspaket) per MoveAlongPath entlang der Leiterbahn (nur über das Szenen-JSON, nicht im Menü, aber machbar); Zahlen erscheinen per Write. „Verschwinden“ (L1) wird durch Überdecken mit einem Rechteck oder durch ein Geisterbild ersetzt.

Bilanz: 19 Vorschläge (A 19, B 0, C 0). Vorhandene Abbildungen: 42, alle 42 zum Animieren geeignet, keine entfällt. Artikel (47): vorher 11 mit 0 Abbildungen, 36 mit 1–5, keine mit mehr als 5; nachher alle 47 mit 1–5. Überschreitungen gegenüber dem Soll (+1, begründet): 05/09 Ausgleichsstrom, 06/04 und 06/10 und 08/05 (Rechenbilder), 06/07 und 07/03 (zwei vorhandene Bilder mit verschiedenen Begriffen); unter dem Soll (−1): 08/11 (nachher 1 statt 2).

## Kurzbilanz je Artikel (alle vier Hefte)

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 05/01-quellen-und-ersatzquellen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 05/02-von-grund-auf-klemmen-kennlinie-linearitat | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 05/03-widerstande-zusammenfassen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/04-symmetrie-nutzen | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 05/05-stern-und-dreieck | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/06-ideale-quellen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/07-reale-quellen-und-der-arbeitspunkt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/08-spannungsquelle-oder-stromquelle | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/09-quellen-zusammenschalten | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 05/10-uberlagerung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/11-thevenin-und-norton | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 05/12-der-r-2r-wandler | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/13-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 06/01-zweitore | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 06/02-von-grund-auf-gesteuerte-quellen-und-matrizen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 06/03-vom-vierpol-zum-zweitor | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 06/04-vier-groen-zwei-gleichungen-vier-zahlen | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06/05-impedanzform-und-leerlaufversuch | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/06-das-zweitor-im-betrieb | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/07-admittanzform-und-kurzschlussversuch | 1 | 2 | 0 | 0 | 0 | 0 | 2 |
| 06/08-umrechnen-t-und | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/09-hybridform | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/10-kettenform | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06/11-zusammenschaltung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/12-eigenschaften-und-alle-formen-im-uberblick | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06/13-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 07/01-leistung-und-anpassung | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 07/02-energie-je-ladung-mal-ladung-je-zeit | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/03-warum-der-widerstand-warm-wird | 1 | 2 | 0 | 0 | 0 | 0 | 2 |
| 07/04-mittlere-leistung-bei-sinusspannung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/05-leitungsverluste | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/06-wohin-die-leistung-einer-quelle-geht | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/07-leistungsanpassung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/08-warum-50-und-welches-ziel-gilt | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 07/09-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 08/01-maschenstrom-und-knotenpotential | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 08/02-von-grund-auf-drei-gleichungen-drei-unbekannte | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 08/03-wie-viele-groen-sind-frei | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/04-maschenstrome-erfullen-die-knotenregel | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/05-das-maschenstromverfahren | 2 | 1 | 2 | 0 | 0 | 0 | 3 |
| 08/06-potenziale-erfullen-die-maschenregel | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/07-das-knotenpotentialverfahren | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08/08-welches-verfahren-wann | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/09-stempel-und-netzliste | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08/10-gesteuerte-quellen-und-verstarker | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/11-die-modifizierte-knotenanalyse | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/12-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

(Die Tabellen je Heft weiter unten wiederholen diese Zeilen mit Begründungen der Abweichungen.)

## Top 3
- V15 [A] 08/05-das-maschenstromverfahren — Matrix Z Zelle für Zelle aus der Schaltung ablesen — das Hauptverfahren des Hefts lebt vom Ablesen (Diagonale = Widerstände der Masche, Nebendiagonale = gemeinsame, mit Vorzeichen), bisher nur als fertige Matrix.
- V18 [A] 08/09-stempel-und-netzliste — Netzliste stempelt die Matrix Zeile für Zeile — zeigt, wie ein Simulator rechnet, und macht die Singularität der vollen Matrix sichtbar.
- V3 [A] 05/09-quellen-zusammenschalten — Ausgleichsstrom zweier ungleicher Batterien — ein überraschendes Phänomen (Strom ohne Last), bisher nur als Formel.

## Editor-Lücken (nach Vorschlägen V1–V19)
- L1 (Verschwinden): 0 Vorschläge brauchen es zwingend; V1 und V10 behelfen sich mit Deckel/Umfärben, bei vorhandenen Szenen (k5zusammen, k5ueberlagerung, k5ersatz, k6zesb, k6yesb) mit Geisterbildern
- L2 (Umformen/Morph): 0 Vorschläge; 3 vorhandene Szenen (k5gruppe, k5bruecke, k6tpi) wären mit Morph am besten
- L3 (Parameter/Zeit): 2 Vorschläge (V6, V11); 9 vorhandene Szenen (k5ideal, k5arbeitsgerade, k6betrieb, k6kennlinien, k7grenze, k7sinus, k7rechteck, k7kurven, k8verstaerker) wünschen ein stetiges Durchfahren (Last, Arbeitspunkt, Ecke auf der Geraden), sind aber mit festen Zuständen machbar
- L7 (weitere Operationen): 1 Vorschlag optional (V8: Matrix mal Matrix); V16 wäre mit einer Determinanten-Operation bequemer
- L9 (Zellen einzeln betonen): 4 Vorschläge (V15, V17, V18, mit Behelf über Rechtecke) und 2 vorhandene Szenen (k8stempel, k8mna)
- L4, L5, L6, L8: 0
- L10 (Abspielen im Artikel): betrifft alle 19 Vorschläge und alle 42 vorhandenen Szenen
- L-neu: Tabellenzelle über die Zeit ändern (Zahl in einer Zelle wächst: 1 → 1,25 → 1,75): 1 (V18), bisher nur über Text ersetzen/überdecken
- machbar ohne neue Funktion: 17 von 19 (V6 und V18 sind unhandlich, aber möglich)

Allgemein: Die Rechenbilder (V7, V8, V16) nutzen die vorhandenen Operationen Skalarprodukt und Σ; V14 (Cramer als Flächenverhältnis) kommt ohne sie aus.

## Vorschläge Heft 05 (Quellen und Ersatzquellen)

### V1 [A] Netz als Kasten: zwei Zahlen genügen
- **Artikel:** content/et1/05-quellen-und-ersatzquellen/01-quellen-und-ersatzquellen.md
- **Stelle:** Worum es geht — „Ein Sensor hängt an zwei Drähten, dahinter liegt eine Schaltung aus Dutzenden Bauteilen. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Kasten (Rectangle, Beschriftung „Netzwerk N“) mit zehn verdrahteten Widerständen und zwei Quellen, zwei Klemmen A und B herausgeführt. Rechts Achsen: I_A waagerecht 0…5 A, U_AB senkrecht 0…10 V. Zahlen aus dem Heft: Netzwerk N mit U_LL = 9 V, I_KS = 4,5 A.
- **Ablauf:** 1. Der Kasten erscheint mit seinem Innenleben, Klemmen A, B. 2. Ein Voltmeter an A, B, Messpunkt (0 A | 9 V) erscheint (offene Klemmen). 3. Draht über A, B, Messpunkt (4,5 A | 0 V). 4. Lastpunkte (0,5 A | 8 V; 2,25 A | 4,5 V) erscheinen, danach zeichnet sich die Gerade durch alle Punkte. 5. Ein Deckel (Rectangle) legt sich über das Innenleben, übrig bleiben Klemmen und Gerade, Text „Zwei Zahlen: U_LL und I_KS“. — Haltepunkte: 4 (alle Punkte auf einer Geraden), 5.
- **Verständnisproblem:** Warum zwei Zahlen reichen, bevor die Begründung (Linearität) kommt; Vorstellung „Netz von außen“.
- **Szenenname:** et1/k5ueberblick
- **Editor-Lücke:** machbar (Deckel statt Verschwinden; L1 wäre schöner)

### V2 [A] Kennlinie eines Eintors: Leerlauf, Kurzschluss, linear
- **Artikel:** content/et1/05-quellen-und-ersatzquellen/02-von-grund-auf-klemmen-kennlinie-linearitat.md
- **Stelle:** „Die Kennlinie ist der Zusammenhang dieser beiden Größen. …“ und „Ein Bauteil ist linear, wenn …“
- **Art:** neue Animation
- **Was zu sehen ist:** Eintor-Kasten mit Klemmen A, B, Zählpfeile U_AB und I_A. Rechts Axes: I_A waagerecht 0…0,6 A, U_AB senkrecht 0…10 V. Kurve 1: Widerstand 16 Ω (Gerade durch den Ursprung). Kurve 2: Glühlampe (gekrümmte Kurve, schematisch, als solche gekennzeichnet).
- **Ablauf:** 1. Eintor und Zählpfeile erscheinen. 2. Offene Klemmen: Marker auf der Spannungsachse, Text „Leerlauf I_A = 0“. 3. Draht über die Klemmen: Marker auf der Stromachse, Text „Kurzschluss U_AB = 0“. 4. Ein Widerstand statt des Drahts, Messpunkte nacheinander (0,25 A | 4 V; 0,5 A | 8 V), Gerade durch den Ursprung wird gezeichnet; doppelter Strom ergibt doppelte Spannung (zwei Hilfslinien). 5. Die gekrümmte Kennlinie der Glühlampe (Create), Text „nicht linear: doppelter Strom, mehr als doppelte Spannung“. — Haltepunkte: 2, 3, 5.
- **Verständnisproblem:** Kennlinie als Zusammenhang zweier Klemmengrößen; Leerlauf/Kurzschluss als Punkte auf den Achsen; „linear“ anschaulich.
- **Szenenname:** et1/k5kennlinie
- **Editor-Lücke:** machbar

### V3 [A] Ausgleichsstrom zweier ungleicher Batterien
- **Artikel:** content/et1/05-quellen-und-ersatzquellen/09-quellen-zusammenschalten.md
- **Stelle:** Satz 7.1, „Gültigkeit: … Bei U_q1 ≠ U_q2 kreist schon ohne Last ein Ausgleichsstrom“
- **Art:** neue Animation (Überschreitung +1 gegenüber dem Soll, begründet: eigenes Phänomen mit eigener Gleichung 7.3, das k5zusammen nicht zeigt)
- **Was zu sehen ist:** Zwei Batterien parallel, ohne Last: 9 V mit 2 Ω und 8 V mit 2 Ω; Plus-Pole oben verbunden, Minus-Pole unten. Daneben die Rechnung 1 V / 4 Ω = 0,25 A.
- **Ablauf:** 1. Beide Batterien erscheinen einzeln, Leerlaufspannungen 9 V und 8 V. 2. Verbindungsdrähte werden gezogen (Create). 3. Ladungspakete laufen im Kreis (MoveAlongPath): aus dem Pluspol der 9-V-Batterie über die Verbindung in die 8-V-Batterie hinein, unten zurück; LabeledArrow 0,25 A. 4. Spannungsfall an den Innenwiderständen: je 0,5 V erscheint, beide Klemmen stehen auf 8,5 V. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Warum Strom fließt, obwohl keine Last da ist; dass die schwächere Quelle geladen wird; Mittelwert 8,5 V.
- **Szenenname:** et1/k5ausgleich
- **Editor-Lücke:** machbar

### V4 [A] Das Wichtigste: Überlagerung wird Gerade (Zusammenschau)
- **Artikel:** content/et1/05-quellen-und-ersatzquellen/13-das-wichtigste.md
- **Stelle:** Die Antwort in drei Sätzen — „In einem linearen Netzwerk addieren sich die Wirkungen der Quellen …“
- **Art:** vorhandene Szene wiederverwenden (et1/k5geraden, animiert wie unten beschrieben), ergänzt um einen Schlussschritt
- **Was zu sehen ist:** wie k5geraden: Axes I_A 0…5 A, U_AB 0…10 V, drei Geraden.
- **Ablauf:** 1. Gerade der Spannungsquelle allein (6 V, 3 A). 2. Gerade der Stromquelle allein (3 V, 1,5 A). 3. Beide wirken: Gerade nach oben verschoben, gleiche Neigung 2 Ω (9 V, 4,5 A). 4. Lastgerade 16 Ω, Arbeitspunkt (0,5 A | 8 V) leuchtet auf (Indicate). — Haltepunkte: 3, 4.
- **Verständnisproblem:** Das eine Prinzip hinter allen Stufen sehen: Netz = Gerade.
- **Szenenname:** et1/k5geraden (wiederverwendet)
- **Editor-Lücke:** machbar

### Kurzbilanz Heft 05

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 05/01-quellen-und-ersatzquellen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 05/02-von-grund-auf-klemmen-kennlinie-linearitat | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 05/03-widerstande-zusammenfassen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/04-symmetrie-nutzen | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 05/05-stern-und-dreieck | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/06-ideale-quellen | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/07-reale-quellen-und-der-arbeitspunkt | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/08-spannungsquelle-oder-stromquelle | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/09-quellen-zusammenschalten | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 05/10-uberlagerung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/11-thevenin-und-norton | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 05/12-der-r-2r-wandler | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 05/13-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Verworfen: 03 Σ der drei Leitwerte (50 + 33,3 + 16,7 mS) als eigenes Rechenbild: bleibt Schritt 2 der k5gruppe-Animation, eine Addition dreier Zahlen innerhalb eines Zusammenfassungsschritts ist kein eigenes Rechenbild. 07 „Selbstregelung“ (Ladungsansammlung an Klemme A, bis die Ströme gleich sind): über Soll, nicht aufgenommen. 11 „Drei Wege zu den zwei Zahlen“: steckt in der Animation von k5ersatz.

### Vorhandene Abbildungen Heft 05
- k5gruppe (03-widerstande-zusammenfassen.md): animieren ja — Schritte: 1. Netz aus sechs Widerständen (R_a 6 Ω, R_b 30 Ω, R_c 5 Ω, R_d 20 Ω, R_e 30 Ω, R_f 60 Ω) erscheint, Klemmen A, B. 2. Die drei gestapelten Widerstände d, e, f werden hervorgehoben (Indicate) und durch einen Widerstand 10 Ω ersetzt (Leitwerte 50 + 33,3 + 16,7 mS = 100 mS als Text). 3. R_c (5 Ω) und die 10 Ω fahren zusammen zu 15 Ω (Reihe). 4. 30 Ω ∥ 15 Ω = 10 Ω. 5. In Reihe zu R_a: R_AB = 16 Ω. 6. Rückrechnung: 8 V an A, B, Ströme 0,5 A, 166,7 mA, 333,3 mA als Ladungspakete. Haltepunkte 2, 4. | Lücke: L2 (echtes Zusammenschmelzen wäre Morph; heute Ersatz neben Geisterbild des Originals), sonst machbar
- k5symmetrie (04-symmetrie-nutzen.md): animieren ja — Schritte: 1. Netz aus sieben 14-Ω-Widerständen, A an 16 V, B auf 0. 2. Spiegelachse erscheint (gestrichelte Linie durch L und die Mitte des E-F-Widerstands), A und B tauschen per Pfeil die Plätze. 3. Potenziale auf der Achse erscheinen (8 V), die Achsenpunkte werden verbunden. 4. Der E-F-Widerstand zerfällt in zweimal 7 Ω. 5. Halbschaltung rechts baut sich auf: 14 Ω ∥ 7 Ω = 4,67 Ω, + 14 Ω = 18,67 Ω, ∥ 14 Ω = 8 Ω, R_AB = 16 Ω. Haltepunkt 3. | Lücke: machbar
- k5wuerfel (04-symmetrie-nutzen.md): animieren ja — Schritte: 1. Würfel aus zwölf 12-Ω-Kanten, Klemmen A, B an der Raumdiagonale. 2. Drei Nachbarn von A farbig markiert, Drehpfeil um die Diagonale zeigt: sie tauschen die Plätze. 3. Dasselbe für die Nachbarn von B. 4. Die Nachbarn werden mit einem Draht verbunden (Create), es entsteht die Kette 3 – 6 – 3 parallele Kanten. 5. Rechnung R/3 + R/6 + R/3 = 10 Ω, Ströme 167 mA, 83 mA, 167 mA als Pakete. Haltepunkt 4. | Lücke: machbar (L4, Kameradrehung, wäre eine Zugabe)
- k5bruecke (05-stern-und-dreieck.md): animieren ja — Schritte: 1. Brücke ohne Abgleich, Dreieck 1-2-3 blau (10, 20, 20 Ω). 2. Roter Stern erscheint im Dreieck, die drei Dreieckswiderstände werden zu Geisterbildern. 3. Werte 4, 4, 8 Ω erscheinen mit der Formel (10·20/50). 4. Reihen 4 Ω + 20 Ω und 8 Ω + 16 Ω (Klammern), Parallelschaltung 24 Ω ∥ 24 Ω = 12 Ω, + 4 Ω = 16 Ω. Haltepunkte 2, 3. | Lücke: L2 (echter Morph Dreieck zu Stern wäre ideal; sonst Geisterbild)
- k5ideal (06-ideale-quellen.md): animieren ja — Schritte: 1. Spannungsquelle 9 V, Kennlinie Waagerechte (Axes I 0…10 A, U 0…12 V), Last 16 Ω: Punkt (0,5625 A | 9 V). 2. Last 1 Ω: Punkt (9 A | 9 V); 1 mΩ: Pfeil aus dem Bild (9000 A). 3. Rechts Stromquelle 0,5 A, Senkrechte; Last 16 Ω: (0,5 A | 8 V), 1 kΩ: 500 V (Pfeil aus dem Bild). Haltepunkt 2. | Lücke: L3 (stufenloses Durchfahren der Last; als Folge von Punkten machbar)
- k5arbeitsgerade (07-reale-quellen-und-der-arbeitspunkt.md): animieren ja — Schritte: 1. Reale Quelle 9 V, 2 Ω mit Last; Kennlinie der Quelle (fallende Gerade von 9 V bei 0 A bis 4,5 A bei 0 V) zeichnet sich. 2. Leerlauf- und Kurzschlusspunkt markiert. 3. Lastgerade 16 Ω (Ursprungsgerade) erscheint; Schnittpunkt (0,5 A | 8 V), innen fällt 1 V (Messlinie). 4. Lastgerade schwenkt (Rotate um den Ursprung) zu 2 Ω: Arbeitspunkt (2,25 A | 4,5 V). 5. R_L → 0: Punkt läuft zum Kurzschlusspunkt; R_L → ∞: zum Leerlaufpunkt. Haltepunkte 3, 4. | Lücke: L3 (stetiges Mitlaufen des Arbeitspunkts)
- k5umwandlung (08-spannungsquelle-oder-stromquelle.md): animieren ja — Schritte: 1. Links Spannungsquelle 9 V mit 2 Ω an Last: 0,5 A durch alles, Klemmenspannung 8 V. 2. Rechts Stromquelle 4,5 A mit 0,5 S: der Quellenstrom teilt sich (Pakete) in 4 A durch den Leitwert und 0,5 A zur Last. 3. Daneben die Kennlinie: Achsenabschnitte 9 V und 4,5 A, beide Schaltungen liefern denselben Arbeitspunkt (8 V | 0,5 A). Haltepunkt 2. | Lücke: machbar
- k5zusammen (09-quellen-zusammenschalten.md): animieren ja — Schritte: 1. Einzelkennlinie 9 V / 4,5 A. 2. Zweite identische Batterie parallel: neue Kennlinie (Create): Leerlauf 9 V bleibt, Kurzschlussstrom 9 A (Steigung 1 Ω). 3. Reihenschaltung (Einzelkennlinie als Geisterbild): Leerlauf 18 V, Kurzschluss 4,5 A (Steigung 4 Ω). 4. Arbeitspunkte an 16 Ω: parallel (0,529 A | 8,47 V), Reihe (0,9 A | 14,4 V), einzeln (0,5 A | 8 V). Haltepunkte 2, 3. | Lücke: L1 (Geisterbild als Ersatz), machbar
- k5ueberlagerung (10-uberlagerung.md): animieren ja — Schritte: 1. Netz N: U_q1 = 18 V, R1 = 6 Ω, R2 = 3 Ω, I_q2 = 1,5 A, A, B offen. 2. Teilbild 1: Stromquelle wird zur Lücke, Spannungsteiler, U' = 6 V (Pakete in R1, R2). 3. Teilbild 2: Spannungsquelle wird zum Draht, Stromquelle speist R1 ∥ R2 = 2 Ω, U'' = 3 V. 4. Addition auf einer Spannungsachse: 6 V + 3 V = 9 V. 5. Zweigstrom in R1: 2 A − 0,5 A = 1,5 A. Haltepunkte 2, 3. | Lücke: L1 (Ersetzen per Überdeckung), machbar
- k5ersatz (11-thevenin-und-norton.md): animieren ja — Schritte: 1. Netz N. 2. Leerlauf: Voltmeter zeigt 9 V. 3. Kurzschluss: Draht zwischen A, B, 4,5 A als Pakete, R2 stromlos. 4. Quotient R_i = 9 V / 4,5 A = 2 Ω. 5. Alternativ Quellen abgeschaltet (Draht/Lücke): R1 ∥ R2 = 2 Ω. 6. Rechts erscheinen Thevenin- (9 V, 2 Ω) und Norton-Ersatz (4,5 A, 0,5 S), Lastpunkte decken sich. Haltepunkte 3, 5. | Lücke: L1, machbar
- k5geraden (11-thevenin-und-norton.md): animieren ja — Schritte: 1. Gerade der Spannungsquelle allein (6 V, 3 A). 2. Gerade der Stromquelle allein (3 V, 1,5 A). 3. Beide wirken: Gerade parallel nach oben (Shift), 9 V, 4,5 A, Neigung 2 Ω bleibt. Haltepunkt 3. | Lücke: machbar
- k5r2r (12-der-r-2r-wandler.md): animieren ja — Schritte: 1. Leiter aus R und 2R, Schalter d2 d1 d0 in Stellung 101. 2. Beiträge nacheinander: d2 allein auf U_ref = 8 V gibt 4 V, d1 (2 V, aus), d0 (1 V); Stem-Balken 4 V, 0 V, 1 V erscheinen, Summe 5 V. 3. Zählen 000…111: Treppe wächst Stufe für Stufe (Stem 0…7 V, je 1 V). 4. Last R_L = R: Ausgang halbiert, zweite Treppe 0…3,5 V in anderer Farbe. Haltepunkte 2, 4. | Lücke: L3 (Zählen als Folge von Stems machbar)

## Vorschläge Heft 06 (Zweitore)

### V5 [A] Das Zweitor als Kasten: von außen zählen nur Spannung und Strom
- **Artikel:** content/et1/06-zweitore/01-zweitore.md
- **Stelle:** Worum es geht — „Zwischen Quelle und Last sitzt oft ein weiteres Netzwerk: ein Kabel, ein Filter, ein Dämpfungsglied oder ein Verstärker. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Quelle (Quelle mit Innenwiderstand), mittig ein geschlossener Kasten „Zweitor“ mit zwei Klemmenpaaren, rechts Last. An jedem Klemmenpaar ein Voltmeter und ein Strommesser (vier Anzeigen: U_1, I_1, U_2, I_2). Zahlen aus dem Rechenmodell: Quelle 9 V / 5 Ω, Last 60 Ω.
- **Ablauf:** 1. Quelle, Kasten, Last erscheinen, Ladungspakete laufen von der Quelle durch den Kasten zur Last. 2. Die vier Messgeräte erscheinen mit den Werten 7,75 V / 250 mA am Eingang und 3 V / 50 mA am Ausgang. 3. Der Deckel öffnet sich nicht, stattdessen blendet nacheinander (FadeIn auf dem Deckel, Deckel bleibt) Text ein: „Kabel“, „Filter“, „Dämpfungsglied“, „Verstärker“, jeweils als kleines Schaltbild im Kasten daneben; die Messgeräte bleiben dieselben. 4. Text: „Von außen zählen nur diese vier Größen.“ — Haltepunkte: 2, 3.
- **Verständnisproblem:** Was ein Zweitor ist und dass nur die Torgrößen zählen, nicht der Inhalt; Bezug zum Eintor aus Teil 5.
- **Szenenname:** et1/k6kasten
- **Editor-Lücke:** machbar

### V6 [A] Gesteuerte Quelle: die Raute folgt einer fremden Größe
- **Artikel:** content/et1/06-zweitore/02-von-grund-auf-gesteuerte-quellen-und-matrizen.md
- **Stelle:** „Eine gesteuerte Quelle liefert einen Wert, der einer anderen Spannung oder einem anderen Strom an anderer Stelle der Schaltung proportional ist. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links ein Steuerkreis mit Messstelle U_s (Voltmeter), rechts eine VCVS-Raute mit U = μ·U_s, μ = 5 (Beispielwert), daran ein Last-Widerstand. Darunter Axes: U_s waagerecht 0…3 V, U senkrecht 0…15 V.
- **Ablauf:** 1. Steuerkreis, Raute und Lastkreis erscheinen; die Raute ist mit einer gestrichelten Linie zur Messstelle U_s verbunden (Steuerleitung). 2. U_s = 1 V: Anzeige 1 V, Raute-Ausgang 5 V, Punkt (1 V | 5 V) im Diagramm. 3. U_s = 2 V: Ausgang 10 V, Punkt (2 V | 10 V). 4. Die Gerade durch den Ursprung wird gezeichnet, Steigung μ = 5. 5. Last wechselt (zweiter Lastwiderstand): Ausgangsspannung bleibt 5 V bzw. 10 V, der Steuerkreis bleibt unberührt (Anzeige U_s ändert sich nicht). — Haltepunkte: 3, 5.
- **Verständnisproblem:** Wertgebung durch eine Größe an anderer Stelle (statt fester Wert); Vierpoleigenschaft: Steuergröße und Quelle sitzen an verschiedenen Orten, also ein Zweitor.
- **Szenenname:** et1/k6gesteuert
- **Editor-Lücke:** L3 (Steuerspannung als Parameter durchfahren; hier als zwei feste Zustände nacheinander gelöst, machbar)

### V7 [A] Rechenbild: die Z-Gleichungen mit den Zahlen des T-Zweitors
- **Artikel:** content/et1/06-zweitore/04-vier-groen-zwei-gleichungen-vier-zahlen.md
- **Stelle:** beispiel — „Am Mittelpunkt des T-Zweitors treffen sich I_1 und I_2, durch R_b fließt ihre Summe. Die Maschenregel ergibt …“
- **Art:** neue Animation (Rechenbild, Skalarprodukt; Überschreitung +1 gegenüber dem Soll, begründet durch die Rechenbild-Pflicht)
- **Was zu sehen ist:** Zwei Skalarprodukte, Zeile mal Spalte: (35 Ω, 20 Ω)·(0,25 A, −0,05 A) = 8,75 V − 1 V = 7,75 V und (20 Ω, 40 Ω)·(0,25 A, −0,05 A) = 5 V − 2 V = 3 V.
- **Ablauf:** 1. Matrix und Spaltenvektor (I_1, I_2) erscheinen, Zeilen 1 und 2 farbig. 2. Zeile 1 wird mit der Spalte multipliziert: Produkte 8,75 V und −1 V erscheinen einzeln, dann die Summe 7,75 V = U_1. 3. Dasselbe für Zeile 2: 5 V und −2 V, Summe 3 V = U_2. — Haltepunkte: 2 (Vorzeichen des zweiten Summanden), 3.
- **Verständnisproblem:** Woraus sich jede Wirkungsgröße zusammensetzt: eigener Anteil plus fremder Anteil, mit Vorzeichen von I_2.
- **Szenenname:** et1/k6zmatrix
- **Editor-Lücke:** machbar (Operation Skalarprodukt, zweimal)

### V8 [A] Rechenbild: Rückwärts durch die Kette von der Last aus
- **Artikel:** content/et1/06-zweitore/10-kettenform.md
- **Stelle:** beispiel — „Rückwärts von der Last, mit U_2 = 3 V und −I_2 = 50 mA: U_1 = 5,25 V + 2,5 V = 7,75 V und I_1 = 150 mA + 100 mA = 250 mA.“
- **Art:** neue Animation (Rechenbild, Skalarprodukt; +1 gegenüber dem Soll, begründet durch die Rechenbild-Pflicht)
- **Was zu sehen ist:** A = (1,75; 50 Ω / 50 mS; 2) mal (U_2, −I_2) = (3 V, 0,05 A). Zwei Skalarprodukte: (1,75 | 50 Ω)·(3 V | 0,05 A) = 5,25 V + 2,5 V = 7,75 V; (50 mS | 2)·(3 V | 0,05 A) = 0,15 A + 0,1 A = 0,25 A.
- **Ablauf:** 1. Matrix A und Spalte (U_2, −I_2) erscheinen. 2. Zeile 1: 5,25 V und 2,5 V einzeln, Summe 7,75 V = U_1. 3. Zeile 2: 0,15 A und 0,1 A, Summe 0,25 A = I_1. 4. Optional (L7: Matrix mal Matrix): das Produkt der drei Elementarmatrizen entsteht Spalte für Spalte; ohne diese Funktion nur als Text. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Dass die Kettenmatrix die Last-Größen in Eingangsgrößen übersetzt, ohne Gleichungssystem.
- **Szenenname:** et1/k6kettenrechnung
- **Editor-Lücke:** machbar (Schritte 1–3); Schritt 4 braucht L7 (Matrix·Matrix)

### V9 [A] Leistung im Zweitor: aktiv und passiv als Bilanz
- **Artikel:** content/et1/06-zweitore/12-eigenschaften-und-alle-formen-im-uberblick.md
- **Stelle:** Definition 10.1 und Beispiel — „Das T-Zweitor nimmt P_1 = 7,75 V · 250 mA = 1,9375 W auf und gibt P_2 = 3 V · 50 mA = 0,15 W ab. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Leistungsbilanzen als Balken (Rectangles, Höhe maßstäblich innerhalb jedes Bildteils). Links T-Zweitor: Balken P_1 = 1,9375 W, daraus wird P_2 = 0,15 W und die Wärme 1,7875 W (Aufteilung 0,9375 W + 0,8 W + 0,05 W in R_a, R_b, R_c). Rechts Verstärker: P_1 = 0,2 µW klein, P_2 = 3,2 mW groß, Differenz kommt aus der Versorgung (Pfeil von außen).
- **Ablauf:** 1. Das T-Zweitor als Kasten, Pfeil P_1 hinein, Balken wächst. 2. Pfeil P_2 heraus, kleiner Balken. 3. Rest als Wärme in den drei Widerständen (drei Teilbalken). 4. Verstärker: Eingangsbalken ist winzig, Ausgangsbalken ragt weit darüber; Pfeil „Versorgung“ von außen füllt die Differenz. Text „P < 0: aktiv“. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Was „aktiv“ bedeutet und woher die zusätzliche Leistung kommt (Hilfsquelle, nicht das Eingangssignal).
- **Szenenname:** et1/k6leistung
- **Editor-Lücke:** machbar (Balken als Rectangles, kein Wachstum über die Zeit: Scale)

### V10 [A] Das Wichtigste: eine Wahl der Ursachen, vier Formen
- **Artikel:** content/et1/06-zweitore/13-das-wichtigste.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Von vier Torgrößen wählt man zwei als Ursachen, die anderen zwei sind die Wirkungen. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zweitor-Kasten in der Mitte mit vier Größen U_1, I_1 (links), U_2, I_2 (rechts) als farbige Kästen. Unten eine Zeile mit der gewählten Form, dem Versuch und dem T-Zweitor-Wert.
- **Ablauf:** 1. Die vier Größen erscheinen. 2. Z-Form: I_1 und I_2 färben sich als Ursachen, U_1 und U_2 als Wirkungen; Text „Leerlauf: I = 0“, Wert Z_11 = 35 Ω. 3. Y-Form: U_1, U_2 Ursachen; Text „Kurzschluss: U = 0“, Y_11 = 40 mS. 4. H-Form: I_1 und U_2 Ursachen, Werte H_11 = 25 Ω. 5. A-Form: U_2 und −I_2 Ursachen, A_11 = 1,75. — Haltepunkte: 2, 3, 5.
- **Verständnisproblem:** Dass die vier Formen dasselbe Zweitor mit anderer Wahl der Ursachen beschreiben (großes Bild des Kapitels).
- **Szenenname:** et1/k6formen
- **Editor-Lücke:** L1 (Umfärben statt Verschwinden: jede Form als neue Kästenreihe; machbar)

### Kurzbilanz Heft 06

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 06/01-zweitore | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 06/02-von-grund-auf-gesteuerte-quellen-und-matrizen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 06/03-vom-vierpol-zum-zweitor | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 06/04-vier-groen-zwei-gleichungen-vier-zahlen | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06/05-impedanzform-und-leerlaufversuch | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/06-das-zweitor-im-betrieb | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/07-admittanzform-und-kurzschlussversuch | 1 | 2 | 0 | 0 | 0 | 0 | 2 |
| 06/08-umrechnen-t-und | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/09-hybridform | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/10-kettenform | 1 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06/11-zusammenschaltung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 06/12-eigenschaften-und-alle-formen-im-uberblick | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 06/13-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Begründung 07 (Soll 1, nachher 2): k6yesb zeigt den Kurzschlussversuch mit Ersatzschaltbild, k6kennlinien einen eigenen Begriff (Kennlinien und Kurvenschar); beide bleiben, die Animation beider ist kurz.
Verworfen: 02 Matrix mal Vektor/Matrix mal Matrix in der Einführung (nur allgemeine Buchstaben, keine Zahlen, daher kein Pflicht-Rechenbild; die Zahlen kommen in V7 und V8; Szenenbezug bei Bedarf hm1/k10produkt). 06 Kurve „Eingangswiderstand über der Last“ (35 Ω bei R_L → ∞ bis 25 Ω bei R_L = 0): über Soll, die Schritte 4 und 5 der Animation von k6betrieb zeigen zwei Punkte davon. 11 „Wann die Regel versagt“ (zwei übereinandergelegte T-Zweitore, Strom nimmt den Umweg durch R_c): über Soll, nur als Zusatzschritt in der Animation von k6zusammen vorgesehen.

### Vorhandene Abbildungen Heft 06
- k6tor (03-vom-vierpol-zum-zweitor.md): animieren ja — Schritte: 1. Links Quelle, Zweitor, Last. 2. Strompakete laufen in Klemme 1 hinein und aus 1' wieder heraus (Torbedingung), ebenso an Tor 2; Energiefluss-Pfeil von Tor 1 nach Tor 2. 3. Rechts derselbe Aufbau mit einem äußeren Zweig von Klemme 1 nach Klemme 2: ein Teil des Stroms (I_x) geht außen vorbei, in 1 fließt mehr hinein als aus 1' heraus: Klemmenpaare keine Tore mehr. Haltepunkt 3. | Lücke: machbar
- k6masse (03-vom-vierpol-zum-zweitor.md): animieren ja — Schritte: 1. T-Zweitor, Masseleitung von 1' nach 2' rot gezeichnet (Create). 2. Pakete in der Masseleitung: 50 mA fließen von 2' zum Fußpunkt von R_b. 3. Brückenschaltung rechts (R_x, R_y paarweise), keine durchgehende Leitung, Spiegelachse eingezeichnet. Haltepunkt 2. | Lücke: machbar
- k6zaehlpfeile (04-vier-groen-zwei-gleichungen-vier-zahlen.md): animieren ja — Schritte: 1. Symmetrisches Pfeilsystem: beide Strompfeile hinein. 2. Kettenpfeil: I_2 zeigt heraus, zur Last. 3. Gemischtes System: I_2 wie links, der Strom zur Last heißt −I_2. 4. Zahlenbeispiel: Last nimmt 50 mA auf, I_2 = −50 mA erscheint. Haltepunkt 3. | Lücke: machbar
- k6zesb (05-impedanzform-und-leerlaufversuch.md): animieren ja — Schritte: 1. Ersatzschaltbild der Z-Form: Z_11, Z_22 mit zwei stromgesteuerten Spannungsquellen. 2. Leerlaufversuch: Tor 2 wird geöffnet (Lücke), I_2 = 0: Z_22 und die Quelle Z_12·I_2 werden grau (Geisterbild). 3. Eingeprägter Strom 100 mA fließt durch Z_11, U_1 = 3,5 V; U_2 = Z_21·I_1 = 2 V. 4. Spiegelbild: Tor 1 offen, Strom an Tor 2, U_2 = 4 V, U_1 = 2 V. Haltepunkte 2, 3. | Lücke: L1 (Ausgrauen statt Verschwinden), machbar
- k6betrieb (06-das-zweitor-im-betrieb.md): animieren ja — Schritte: 1. T-Zweitor mit Quelle (9 V, 5 Ω) bei offenem Tor 2: I_1 = 225 mA, U_1 = 7,875 V, Z_1 = 35 Ω. 2. Last 60 Ω wird zugeschaltet: Pakete laufen zur Last, I_2 = −50 mA, I_1 steigt auf 250 mA. 3. Die Rückwirkung erscheint als LabeledArrow Z_12·I_2 = −1 V am Eingang (bei 250 mA wären es 8,75 V, es sind 7,75 V), Z_1 = 31 Ω. 4. Last auf 1 mΩ: Z_1 = 25 Ω; Last auf 1 GΩ: 35 Ω (zwei Grenzpunkte). Haltepunkt 3. | Lücke: L3 (stetiges Durchfahren der Last), als Folge von Zuständen machbar
- k6yesb (07-admittanzform-und-kurzschlussversuch.md): animieren ja — Schritte: 1. Ersatzschaltbild der Y-Form (Leitwerte plus spannungsgesteuerte Stromquellen). 2. Kurzschlussversuch: Draht über Tor 2, U_2 = 0: Quelle Y_12·U_2 und Y_22 grau. 3. 9 V an Tor 1, I_1 = 360 mA, Strom teilt sich hälftig, I_2 = −180 mA. 4. Spiegelbild: 9 V an Tor 2, I_2 = 315 mA, I_1 = −180 mA. Haltepunkte 2, 3. | Lücke: L1, machbar
- k6kennlinien (07-admittanzform-und-kurzschlussversuch.md): animieren ja — Schritte: 1. Eingangskennlinie I_1(U_1): Gerade Steigung 40 mS bei U_2 = 0 (Create). 2. U_2 = 1 V, 2 V: Geraden verschieben sich parallel um −20 mA je Volt (Kurvenschar entsteht, CurveFamily). 3. Übertragungskennlinie (−20 mS) und Ausgangskennlinie (35 mS) in derselben Weise. Haltepunkt 2. | Lücke: L3 (Parameter-Sweep; als drei Einzelgeraden machbar)
- k6tpi (08-umrechnen-t-und.md): animieren ja — Schritte: 1. T-Schaltung mit 15, 20, 20 Ω. 2. Matrix Z und det Z = 1000 Ω² erscheinen, daraus Y (40, −20, 35 mS). 3. π-Schaltung mit 50, 50, 66,7 Ω erscheint neben dem T (T wird Geisterbild). 4. Dasselbe Messpaar (Leerlauf an beiden: 100 mA gibt 2 V) zeigt gleiche Messwerte. Haltepunkt 3. | Lücke: L2 (Morph T zu π), sonst machbar
- k6hesb (09-hybridform.md): animieren ja — Schritte: 1. Ersatzschaltbild der H-Form (Reihenschaltung Eingang, Parallelschaltung Ausgang). 2. Verstärkermodell: U_1 = 20 mV, I_1 = 10 µA fließt durch H_11 = 2 kΩ. 3. Die Quelle H_21·I_1 = 1 mA erscheint, Strom verteilt sich: 0,8 mA durch die Last 5 kΩ, 0,2 mA durch H_22^-1 = 20 kΩ. 4. U_2 = −4 V erscheint; Spannungsverstärkung −200. Haltepunkte 3, 4. | Lücke: machbar
- k6kette (10-kettenform.md): animieren ja — Schritte: 1. Zwei Zweitore in Kette; gemeinsame Größen U_2' = U_1'' und −I_2' = I_1'' werden markiert (Pfeile, Pakete wandern über die Grenze). 2. T-Zweitor als Kette: R_a, G_b, R_c erscheinen nacheinander, jeweils mit ihrer Elementarmatrix. 3. Hinweis für die Zwei-T-Ketten: 5,56 statt 3,06 (zweite Stufe belastet die erste). Haltepunkt 2. | Lücke: L7 (Matrixprodukt als Operation), sonst machbar
- k6zusammen (11-zusammenschaltung.md): animieren ja — Schritte: 1. Reihe, Reihe: Strom I_1, I_2 gleich in beiden Teilen (Pakete laufen durch beide), die Spannungen addieren sich (zwei LabeledArrows werden zu einem). 2. parallel, parallel: Spannungen gleich, Ströme addieren sich. 3. Reihe, parallel (H). Dazu die Tabelle jeweils als Textzeile. Zusatz (verworfen oben): Fehlerfall der übereinandergelegten T-Zweitore. Haltepunkte 1, 2. | Lücke: machbar
- k6umkehr (12-eigenschaften-und-alle-formen-im-uberblick.md): animieren ja — Schritte: 1. T-Zweitor: 100 mA in Tor 1, Tor 2 offen, Voltmeter zeigt 2 V. 2. Dasselbe von Tor 2 aus: 100 mA, Tor 1 offen, ebenfalls 2 V (obwohl R_a ≠ R_c). 3. Verstärkermodell: 1 µA an Tor 1 gibt −2 V an Tor 2; 1 µA an Tor 2 gibt 0 V an Tor 1 (kein Rückweg). Haltepunkte 2, 3. | Lücke: machbar

## Vorschläge Heft 07 (Leistung und Anpassung)

### V11 [A] Wohin geht die Energie der Batterie, wenn die Last wechselt?
- **Artikel:** content/et1/07-leistung-und-anpassung/01-leistung-und-anpassung.md
- **Stelle:** Worum es geht — „Eine 9-V-Batterie hat 2 Ω Innenwiderstand, … Wie groß muss die Last sein, damit möglichst viel Leistung, also Energie je Zeit, bei ihr ankommt?“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Batterie (Quelle 9 V, innen sichtbar der Widerstand R_i = 2 Ω), rechts die Last R_L. Darunter zwei Balken: Wärme in der Last (blau) und Wärme in der Batterie (rot), Skala 0…30 W. Zahlen aus dem Rechenmodell: R_L = 16, 8, 2, 0,5 Ω.
- **Ablauf:** 1. Batterie, Last 16 Ω; Balken blau 4 W, rot 0,5 W. 2. Last 8 Ω: blau 6,48 W, rot 1,62 W. 3. Last 2 Ω: beide 10,125 W (Markierung „gleich“). 4. Last 0,5 Ω: blau 6,48 W, rot 25,92 W. 5. Der größte blaue Balken (Schritt 3) leuchtet auf (Indicate), Text: „Maximum bei R_L = R_i, dann gleich viel in der Batterie“. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Die Fragestellung des Kapitels sehen: „Mehr Last“ heißt nicht „mehr Leistung“; das Maximum bei gleichem Widerstand, die Hälfte bleibt innen.
- **Szenenname:** et1/k7ueberblick
- **Editor-Lücke:** L3 (Last stetig durchfahren; als vier feste Zustände machbar)

### V12 [A] Das Wichtigste: Leistung als Parabel, Wirkungsgrad als Gerade (Zusammenschau)
- **Artikel:** content/et1/07-leistung-und-anpassung/09-das-wichtigste.md
- **Stelle:** Die Antwort in drei Sätzen — „Eine Quelle mit Innenwiderstand R_i gibt die größte Leistung an die Last R_L = R_i ab. …“
- **Art:** vorhandene Szene wiederverwenden (et1/k7kurven, rechte Bildhälfte, animiert wie unten bei „Vorhandene Abbildungen“ beschrieben)
- **Was zu sehen ist:** Axes: Strom x = I/I_KS von 0…1, Ordinate 0…1 (normiert auf P_KS/4 beziehungsweise auf 1 für η). Wirkungsgrad η = 1 − x (Gerade), Leistung P_L/P_KS = x(1 − x) (Parabel, Scheitel bei 1/4).
- **Ablauf:** 1. Gerade η = 1 − x zeichnet sich. 2. Parabel P_L entsteht aus dem Produkt x·η (Punkte wandern von x = 0 nach 1). 3. Scheitel bei x = 1/2 markiert, dort η = 1/2 (Hilfslinien). — Haltepunkt: 3.
- **Verständnisproblem:** Das Prinzip „Produkt aus steigender und fallender Größe hat das Maximum in der Mitte“ als Schlussbild des Kapitels.
- **Szenenname:** et1/k7kurven (wiederverwendet)
- **Editor-Lücke:** L3 (Punkt auf der Kurve mit Projektion); ohne: Kurven nacheinander zeichnen, machbar

### Kurzbilanz Heft 07

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 07/01-leistung-und-anpassung | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 07/02-energie-je-ladung-mal-ladung-je-zeit | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/03-warum-der-widerstand-warm-wird | 1 | 2 | 0 | 0 | 0 | 0 | 2 |
| 07/04-mittlere-leistung-bei-sinusspannung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/05-leitungsverluste | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/06-wohin-die-leistung-einer-quelle-geht | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/07-leistungsanpassung | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 07/08-warum-50-und-welches-ziel-gilt | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 07/09-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Begründung 03 (Soll 1, nachher 2): k7stoss zeigt den Mechanismus (Stoß, Energie ans Gitter), k7grenze einen eigenen Begriff (Belastbarkeit und Hyperbel); beide Animationen sind kurz, eine Zusammenlegung würde eines der beiden Bilder überladen.
Verworfen: 02 Produkt 8 V mal 0,5 A als eigenes Rechenbild (zwei Faktoren, wird Schlussschritt der Animation von k7ladung). 04 Effektivwert (Zusatzkasten, zugeklappt). 05 Tabelle der Netzebenen (keine Anschauung durch Bewegung).

### Vorhandene Abbildungen Heft 07
- k7ladung (02-energie-je-ladung-mal-ladung-je-zeit.md): animieren ja — Schritte: 1. Last mit 8 V, 0,5 A, darunter Potenzialverlauf (Treppe von 8 V auf 0). 2. Positive Ladungspakete laufen in Stromrichtung durch die Last; beim Durchlaufen sinkt ihr Marker im Potenzialbild von 8 V auf 0, Text „je Coulomb 8 J“. 3. Zähler: 0,5 C je Sekunde laufen vorbei (Pakete pro Sekunde). 4. Schlusszeile: 8 J/C · 0,5 C/s = 4 W (Produkt als Rechteck der Kantenlängen 8 und 0,5, Fläche 4). Haltepunkt 2. | Lücke: machbar (MoveAlongPath)
- k7stoss (03-warum-der-widerstand-warm-wird.md): animieren ja — Schritte: 1. Achsen: Zeit waagerecht, Energie senkrecht. 2. Im Flug wächst die Arbeit des Felds (blaue Kurve, Create) und die Bewegungsenergie des Elektrons. 3. Beim Stoß springt die Gitterwärme (rote Stufe, W_1), die blaue Kurve fällt auf null zurück. 4. Wiederholung: nach jedem Stoß sind blau und rot gleich hoch; die rote Treppe wächst. Haltepunkte 3, 4. | Lücke: machbar (DataCurve), L1 für das Zurückfallen der blauen Kurve entfällt, da sie als Sägezahn gezeichnet wird
- k7grenze (03-warum-der-widerstand-warm-wird.md): animieren ja — Schritte: 1. Axes U waagerecht, I senkrecht, Grenze P_max = 250 mW als Hyperbel (Create), unzulässiger Bereich schraffiert. 2. Widerstandsgerade 25 Ω (Create): Schnittpunkt bei 100 mA. 3. Die Gerade dreht (Rotate um Ursprung) zu 100 Ω: Schnittpunkt wandert auf der Hyperbel zu 50 mA; dann 400 Ω: 25 mA. 4. Markierung für 100 Ω an 9 V: Punkt liegt über der Hyperbel (810 mW), Pfeil „zu viel“. Haltepunkte 3, 4. | Lücke: L3 (stetiges Drehen mit mitlaufendem Schnittpunkt), als drei Zustände machbar
- k7sinus (04-mittlere-leistung-bei-sinusspannung.md): animieren ja — Schritte: 1. Spannung u(t) (Create), Strom i(t) liegt darauf (Vorfaktor 2 A). 2. Momentanleistung p(t) = u·i entsteht punktweise (Punkt läuft mit, Fläche unter p wächst, Area). 3. Zeitlicher Mittelwert 10 W als waagerechte Linie, die Flächen oberhalb und unterhalb sind gleich groß. 4. p ist doppelt so oft maximal wie u (zwei Marker am Maximum). Haltepunkte 2, 3. | Lücke: L3 (mitlaufender Punkt auf Kurve; als aufbauende Kurve machbar)
- k7leitung (05-leitungsverluste.md): animieren ja — Schritte: 1. Quelle, Leitung (1 Ω) und Last (40 kW). 2. Fall 400 V: 100 A als dichter Strom von Paketen, 100 V fallen an der Leitung ab, Verlustbalken 10 kW. 3. Fall 20 kV: nur 2 Pakete je Zeitabschnitt, Verlustbalken 4 W (Skalenbruch kennzeichnen). 4. Text: Strom 50-mal kleiner, Verlust 2500-mal kleiner. Haltepunkt 3. | Lücke: machbar
- k7kreis (06-wohin-die-leistung-einer-quelle-geht.md): animieren ja — Schritte: 1. Quelle an Last 16 Ω; Potenzialbild des Umlaufs. 2. Eine Ladung (Dot) läuft den Umlauf: Sprung +9 V in der Quelle, −1 V in R_i, −8 V in der Last, zurück am Start. 3. Last wechselt auf 8, 2, 0,5 Ω: die Stufen verschieben sich (−1,8 / −7,2 V, −4,5 / −4,5 V, −7,2 / −1,8 V). Haltepunkt 3. | Lücke: machbar (MoveAlongPath)
- k7rechteck (07-leistungsanpassung.md): animieren ja — Schritte: 1. Quellengerade der Batterie (9 V bis 4,5 A). 2. Arbeitspunkt (0,5 A | 8 V): blaues Rechteck aus I und U_L (4 W), rotes aus I und U_Ri (0,5 W), zusammen P_q. 3. Arbeitspunkt wandert (2,25 A | 4,5 V): beide Rechtecke 10,125 W, blau am größten. 4. Weiter (3,6 A | 1,8 V): blau 6,48 W, rot 25,92 W. 5. Zurück zu 0,5 A und 8 V: 6,48 W bei 8 Ω. Haltepunkte 3, 4. | Lücke: L3 (Ecke läuft stetig mit; als vier Zustände machbar)
- k7kurven (08-warum-50-und-welches-ziel-gilt.md): animieren ja — Schritte (linke Hälfte): 1. P_L(R_L/R_i) steigt, erreicht Maximum bei 1, fällt wieder (Create, Punkt läuft mit). 2. Wirkungsgrad η(R_L/R_i) von 0 gegen 1; bei R_L/R_i = 1 liegt η = 0,5. (rechte Hälfte): 3. Dieselben Kurven über dem Strom: η wird eine fallende Gerade, die Leistung eine Parabel, Scheitel bei x = 1/2. Haltepunkte 1, 3. | Lücke: L3, sonst machbar
- k7netz (08-warum-50-und-welches-ziel-gilt.md): animieren ja — Schritte: 1. Netz mit U_q = 18 V, R_q = 6 Ω, R = 3 Ω, Last 2 Ω. 2. Ersatzquelle (6 V, 2 Ω) erscheint rechts; Last bekommt 4,5 W an beiden. 3. Wirkliche Leistungen im Netz: 37,5 W in R_q, 3 W in R, 4,5 W in der Last (Balken), Quelle 45 W, η = 10 %. 4. Die Ersatzquelle zeigt scheinbar 50 % (zwei gleiche Balken, rot durchgestrichen). Haltepunkt 3. | Lücke: machbar

## Vorschläge Heft 08 (Maschenstrom und Knotenpotential)

### V13 [A] Zwölf Unbekannte für sechs Zweige
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/01-maschenstrom-und-knotenpotential.md
- **Stelle:** Worum es geht — „Das Netz aus Teil 2 hat sechs Zweige. Jeder trägt einen Strom und eine Spannung, das sind zwölf Unbekannte, … Eine Schaltung mit Transistoren hat Hunderte Zweige.“
- **Art:** neue Animation
- **Was zu sehen ist:** Das Rechenmodell (drei Knoten 0, 1, 2; Batterie 9 V mit R_1 = 1 kΩ, R_2 = 4 kΩ, R_3 = 2 kΩ, R_4 = 10 kΩ, Stromquelle 4 mA mit R_5 = 5 kΩ). Daneben ein Zähler „Unbekannte: 0“.
- **Ablauf:** 1. Netz erscheint, Knoten rot. 2. Zweig für Zweig bekommt Strompfeil und Spannungspfeil (sechs Zweige: linker Zweig mit Batterie und R_1, R_2, R_3, R_4, rechter Zweig), der Zähler läuft 2, 4, …, 12. 3. Ein zweites, riesiges Netz (stilisiert, viele Zweige, Transistorsymbol) kommt klein dazu, Zähler „Hunderte“. 4. Text: „Wie wenige Unbekannte reichen?“ — Haltepunkt: 2 (Zähler bei 12).
- **Verständnisproblem:** Warum man überhaupt ein besseres Verfahren braucht (Anzahl der Unbekannten wächst mit dem Netz); Einstieg ohne Vorgriff auf Maschen oder Knotenpotenziale.
- **Szenenname:** et1/k8zaehlung
- **Editor-Lücke:** machbar

### V14 [A] Cramersche Regel als Flächenverhältnis
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/02-von-grund-auf-drei-gleichungen-drei-unbekannte.md
- **Stelle:** Satz 0.1 und Beispiel — „Beispiel: 2x + y = 5 und x + 3y = 5 haben D = 5, D_1 = 10, D_2 = 5, also x = 2, y = 1.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ebene, Axes x −1…6, y −1…6. Spaltenvektoren a_1 = (2|1), a_2 = (1|3) und Rechte Seite b = (5|5). Parallelogramm aus a_1 und a_2 (Fläche D = 2·3 − 1·1 = 5).
- **Ablauf:** 1. Die zwei Gleichungen als Text, daneben die Vektoren a_1, a_2, b (Create). 2. Parallelogramm aus a_1, a_2 füllt sich, Fläche 5 erscheint. 3. b wird in x·a_1 + y·a_2 zerlegt: der Weg 2·a_1, dann 1·a_2 führt nach b (zwei Pfeile aneinander). 4. Parallelogramm aus b und a_2 (Fläche 10): es entsteht durch Scherung aus dem Parallelogramm aus 2·a_1 und a_2 (Gleiten längs a_2, Fläche bleibt 10 = 2·5); daher x = D_1/D = 10/5 = 2. 5. Dasselbe für y: Parallelogramm aus a_1 und b (Fläche 5), y = 5/5 = 1. — Haltepunkte: 3, 4.
- **Verständnisproblem:** Warum der Quotient D_i/D die Lösung liefert (statt einer Regel, die man nur auswendig anwendet); Determinante als Fläche.
- **Szenenname:** et1/k8cramer
- **Editor-Lücke:** machbar (Polygon für die Parallelogramme, Vector, Shift für die Scherung); L7 (Determinante als Operation) entbehrlich

### V15 [A] Die Matrix Z aus der Schaltung ablesen
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/05-das-maschenstromverfahren.md
- **Stelle:** beispiel — „Rechts wird U_q5 = I_q·R_5 = 20 V mit R_5 in Reihe. Die drei Umläufe im Uhrzeigersinn lauten … Geordnet, in kΩ, mA und V, ist das genau, was man auch abliest: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links das Rechenmodell mit umgewandelter Stromquelle (R_1 = 1, R_2 = 4, R_3 = 2, R_4 = 10, R_5 = 5 kΩ, U_q = 9 V, U_q5 = 20 V), drei Fenster I, II, III mit Uhrzeigerpfeilen. Rechts eine 3×3-Tabelle (Table) für Z und die rechte Seite (9, 0, −20).
- **Ablauf:** 1. Netz, Fenster I, II, III mit Maschenströmen im Uhrzeigersinn. 2. Diagonale: Masche I leuchtet, R_1 und R_2 werden rot, Eintrag 5 erscheint in Zelle (1,1); dann II (R_2 + R_3 + R_4 = 16), III (R_4 + R_5 = 15). 3. Nebendiagonale: R_2 leuchtet (liegt in I und II), Eintrag −4 in (1,2) und (2,1); R_4 für (2,3) und (3,2) mit −10; Zelle (1,3) bleibt 0 (kein gemeinsamer Zweig). 4. Rechte Seite: U_q treibt Masche I an (+9), U_q5 wirkt gegen III (−20), II hat keine Quelle (0). 5. Matrix ist vollständig, Symmetrie als Kontrolle (Spiegelpfeil über der Diagonale). — Haltepunkte: 3 (Nebendiagonale negativ), 5.
- **Verständnisproblem:** Warum man die Matrix direkt ablesen darf (Diagonale = Widerstände der Masche, Nebendiagonale = gemeinsame Widerstände mit Vorzeichen); Zusammenhang Schaltung–Matrix.
- **Szenenname:** et1/k8zmatrix
- **Editor-Lücke:** L9 (Zellen einzeln betonen; heute mit Rechtecken über den Zellen gelöst, machbar)

### V16 [A] Rechenbild: Determinante D der Maschenstrommatrix
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/05-das-maschenstromverfahren.md
- **Stelle:** beispiel — „Mit (0.1) und (0.2) ist D = 5·140 + 4·(−60) = 460, D_1 = …“
- **Art:** neue Animation (Rechenbild Σ; Überschreitung +1 gegenüber dem Soll, begründet durch die Rechenbild-Pflicht und weil das Verfahren vier Schritte hat)
- **Was zu sehen ist:** Entwicklung nach der ersten Zeile der Matrix (5, −4, 0 / −4, 16, −10 / 0, −10, 15) als Summe von drei Termen mit wechselndem Vorzeichen: +5·140 + 4·(−60) + 0·(…) = 700 − 240 + 0 = 460. Danach die drei Quotienten I_I = 460/460 = 1 mA, I_II = −460/460 = −1 mA, I_III = −920/460 = −2 mA.
- **Ablauf:** 1. Matrix, erste Zeile hervorgehoben. 2. Für jeden Eintrag wird Zeile und Spalte durchgestrichen (Rechtecke), die 2×2-Restdeterminante erscheint: 16·15 − (−10)(−10) = 140; (−4)·15 − (−10)·0 = −60; dritte ist mit Faktor 0 egal. 3. Summe der drei Terme mit Vorzeichen +, −, +: 700, −240, 0, Ergebnis 460 (Operation Σ, Summanden einzeln). 4. D_1, D_2, D_3 mit denselben Schritten als Ergebnisliste (460, −460, −920); Quotienten 1, −1, −2 mA. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Wie die Entwicklung nach der ersten Zeile mit Vorzeichenwechsel konkret läuft; wo die Null (kein gemeinsamer Zweig) Arbeit spart.
- **Szenenname:** et1/k8det
- **Editor-Lücke:** machbar (Σ-Operation für die Summe, Restdeterminanten als Arithmetik); L7 (Determinante als Operation) wäre bequemer

### V17 [A] Das Knotenpotenzialverfahren: Matrix Y aus dem Leitwertnetz
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/07-das-knotenpotentialverfahren.md
- **Stelle:** beispiel — „Links wird I_q1 = U_q/R_1 = 9 mA mit G_1 = 1 mS parallel. … Die Knotenregeln lauten … Geordnet, in mS, V und mA: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links das Netz in Leitwerten (G_1 = 1, G_2 = 0,25, G_3 = 0,5, G_4 = 0,1, G_5 = 0,2 mS; Quellen 9 mA an Knoten 1, 4 mA an Knoten 2), Bezugsknoten 0 unten. Rechts 2×2-Tabelle für Y und die rechte Seite (9, 4).
- **Ablauf:** 1. Batterie wird zur Stromquelle 9 mA mit G_1 parallel (Ersatz erscheint, Geisterbild der Batterie). 2. Knoten 1 leuchtet: alle Leitwerte an Knoten 1 (G_1, G_2, G_3) werden rot und erscheinen summiert: 1,75 in Zelle (1,1). Knoten 2: G_3 + G_4 + G_5 = 0,8 in (2,2). 3. G_3 verbindet beide Knoten: −0,5 in (1,2) und (2,1). 4. Rechte Seite: 9 mA fließen in Knoten 1, 4 mA in Knoten 2. 5. Lösung: U_1 = 8 V, U_2 = 10 V erscheinen als Höhenmarker am Netz; Probe der Leistungen 49 mW. — Haltepunkte: 3, 5.
- **Verständnisproblem:** Warum die Matrix direkt ablesbar ist und warum fremde Potenziale ein Minus tragen; Parallele zur Maschenmatrix (V15).
- **Szenenname:** et1/k8ymatrix
- **Editor-Lücke:** L9 (Zellen einzeln), sonst machbar

### V18 [A] Stempeln: die Matrix entsteht Zeile für Zeile aus der Netzliste
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/09-stempel-und-netzliste.md
- **Stelle:** beispiel — „Das Rechenmodell mit umgewandelter Batterie ergibt diese Liste: R1 1 0 1k …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Netzliste mit sieben Zeilen (R1 1 0 1k, R2 1 0 4k, R3 1 2 2k, R4 2 0 10k, R5 2 0 5k, I1 0 1 9m, I2 0 2 4m) als Textzeilen. Rechts eine 3×3-Matrix (Zeilen, Spalten 0, 1, 2) mit allen Nullen und die rechte Seite (0, 0, 0). Darüber das Schaltbild klein.
- **Ablauf:** 1. Matrix voller Nullen. 2. R1: Zeile wird hervorgehoben, im Schaltbild leuchtet R1; die Stempelplätze (1,1), (0,0) bekommen +1, (1,0), (0,1) bekommen −1. 3. R2: +0,25 und −0,25 (Zellen wachsen: (1,1) = 1,25, (0,0) = 1,25, (1,0) = (0,1) = −1,25). 4. R3: Plätze (1,1), (2,2), (1,2), (2,1). 5. R4 und R5 nacheinander. 6. I1 und I2 tragen nur rechts ein: (+9 in Zeile 1, −9 in Zeile 0), (+4 in Zeile 2, −4 in Zeile 0), Summe −13 in Zeile 0. 7. Endzustand: alle Zeilensummen null (Kontrolle); Zeile und Spalte 0 werden durchgestrichen, übrig bleibt Y aus Stufe 5. — Haltepunkte: 2, 6, 7.
- **Verständnisproblem:** Wie ein Programm die Matrix aufbaut, ohne zu „denken“: jedes Bauteil addiert sein festes Muster; Reihenfolge egal; warum die volle Matrix singulär ist.
- **Szenenname:** et1/k8netzliste
- **Editor-Lücke:** L9 (Zellen einzeln, Zellwert erhöhen = Text ersetzen; ohne Verschwinden: L1/L2: alter Zellwert muss überschrieben werden; als Folge von Zuständen machbar, aber unhandlich)

### V19 [A] Das Wichtigste: dasselbe Netz, zwei Verfahren (Dualität)
- **Artikel:** content/et1/08-maschenstrom-und-knotenpotential/12-das-wichtigste.md
- **Stelle:** Das Wichtigste und Prinzip hinter allen Ergebnissen (die Dualitätstabelle in Stufe 6, hier als Schlussbild)
- **Art:** neue Animation
- **Was zu sehen ist:** Das Rechenmodell in der Mitte. Links die Maschenströme (I, II, III, Matrix 3×3 mit Z), rechts die Knotenpotenziale (U_1, U_2, Matrix 2×2 mit Y). Beide führen zu denselben Zweigströmen.
- **Ablauf:** 1. Das Netz in der Mitte. 2. Links: drei Fenster mit I_I = 1, I_II = −1, I_III = −2 mA, Z-Matrix (5, −4, 0 ...). 3. Rechts: zwei Höhen U_1 = 8 V, U_2 = 10 V, Y-Matrix (1,75, −0,5 …). 4. Die Zweigströme 1, 2, 1, 1, 2 mA erscheinen an den Zweigen, aus beiden Rechnungen gleich (zwei Farben decken sich). 5. Dualitäts-Pfeile zwischen den Seiten: Masche ↔ Knoten, Reihe ↔ parallel, R ↔ G, Strom ↔ Spannung. — Haltepunkte: 4, 5.
- **Verständnisproblem:** Das eine Prinzip hinter dem Kapitel: Kirchhoff in zwei Hälften; jedes Verfahren erfüllt eine Regel von selbst und stellt die andere auf.
- **Szenenname:** et1/k8dual
- **Editor-Lücke:** machbar

### Kurzbilanz Heft 08

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 08/01-maschenstrom-und-knotenpotential | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 08/02-von-grund-auf-drei-gleichungen-drei-unbekannte | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 08/03-wie-viele-groen-sind-frei | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/04-maschenstrome-erfullen-die-knotenregel | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/05-das-maschenstromverfahren | 2 | 1 | 2 | 0 | 0 | 0 | 3 |
| 08/06-potenziale-erfullen-die-maschenregel | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/07-das-knotenpotentialverfahren | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08/08-welches-verfahren-wann | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/09-stempel-und-netzliste | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08/10-gesteuerte-quellen-und-verstarker | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/11-die-modifizierte-knotenanalyse | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 08/12-das-wichtigste | 1 | 0 | 1 | 0 | 0 | 0 | 1 |

Begründung 05 (Soll 2, nachher 3): Das Verfahren hat vier Schritte und im Beispiel ein Kernstück mit Zahlen (Entwicklung der Determinante, Pflicht-Rechenbild); die Matrix-Aufstellung ist das Verfahren selbst.
Begründung 11 (Soll 2, nachher 1): k8mna zeigt bereits genau den Aufbau (neue Zeile, neue Spalte); ein zweites Bild für den 0-V-Strommesser wäre nur Text mit einer 3×3-Matrix.
Verworfen: 03 Baum und Verbindungszweige (Schritt in der Animation von k8netz, kein eigenes Bild). 08 Dualitätstabelle als eigenes Bild (V19 deckt sie ab). 10 Matrix (8.3) als Rechenbild (Matrixelemente sind Buchstaben, keine Zahlen). 11 Strommesser mit 0-V-Quelle (siehe oben). 07 Cramer-Determinanten 2×2 (D = 1,4 − 0,25 …): kein Σ/∏/Skalarprodukt, durch V14 anschaulich erklärt.

### Vorhandene Abbildungen Heft 08
- k8netz (03-wie-viele-groen-sind-frei.md): animieren ja — Schritte: 1. Netz mit drei Knoten (0, 1, 2) und sechs Zweigen (Batterie + R_1 gilt als ein Zweig). 2. Ein Baum (Knoten 0–1 über R_2, 1–2 über R_3, k − 1 = 2 Baumzweige) wird fett gezeichnet; die übrigen vier Zweige sind die Verbindungszweige. 3. Zählkasten: 12 → 6 → 4 → 2 (Zeilen der Tabelle aus dem Beispiel). 4. Ein Verbindungszweig wird zur Masche gezeichnet (Create). Haltepunkte 2, 3. | Lücke: machbar
- k8kreis (04-maschenstrome-erfullen-die-knotenregel.md): animieren ja — Schritte: 1. Knoten 1 mit zwei Maschen I, II. 2. Ein Kreisstrom (Ladungspakete, Maschenstrom I läuft durch den Knoten hindurch: hinein über einen Zweig, heraus über einen anderen). 3. Maschenstrom II läuft ebenso. 4. Rechts: Zweigströme I_I, I_I − I_II, I_II; die Pfeile zeigen, dass die Summe für jeden Wert null bleibt (Werte durchgespielt: I_I = 2, I_II = 1 mA, dann I_I = 1, I_II = 3 mA). Haltepunkte 2, 4. | Lücke: machbar (MoveAlongPath)
- k8maschen (05-das-maschenstromverfahren.md): animieren ja — Schritte: 1. Rechenmodell mit Stromquelle und R_5 parallel. 2. Umwandlung: Stromquelle wird zu Spannungsquelle 20 V mit R_5 in Reihe (Ersatz neben Geisterbild). 3. Fenster I, II, III mit Maschenströmen (ParametricCurve oder Kreispfeile, nacheinander). 4. R_2 und R_4 leuchten rot (gemeinsame Zweige). 5. Ergebnisse als Zweigströme (1, 2, 1, 1 mA) mit Pfeilen. Haltepunkte 2, 4. | Lücke: machbar (L1 für den Ersatz: Geisterbild)
- k8hoehen (06-potenziale-erfullen-die-maschenregel.md): animieren ja — Schritte: 1. Die Knoten 0, 1, 2 als Höhen (Balken, 0 V, 8 V, 10 V). 2. Ein Dot läuft den Umlauf 0 → 1 → 2 → 0: steigt um 8 V, steigt um 2 V, fällt um 10 V; Anzeige der Summe: null. 3. Dieselben Höhen werden gemeinsam um 3 V angehoben (alle Balken, Shift): der Umlauf bleibt null, die Spannungen der Zweige ändern sich nicht. Haltepunkt 3. | Lücke: machbar (Shift)
- k8yspalte (07-das-knotenpotentialverfahren.md): animieren ja — Schritte: 1. Rechenmodell mit Stromquellen. 2. Quellen entfernt; Knoten 1 wird auf 1 V gelegt, Knoten 2 auf 0 V (Spannungsquelle, die Batterie als Versuch). 3. Ströme über G_1, G_2, G_3 laufen ab: 1 + 0,25 + 0,5 = 1,75 mA, der Wert erscheint als Y_11. 4. 0,5 mA kommen an Knoten 2 an und müssen dort entnommen werden: Y_21 = −0,5 mS. Haltepunkte 3, 4. | Lücke: machbar
- k8zahl (08-welches-verfahren-wann.md): animieren ja — Schritte: 1. Axes: Knotenzahl k waagerecht 2…10, Zweigzahl z senkrecht 1…20. 2. Untere Grenze z = k − 1 (unzusammenhängend), schraffiert. 3. Rote Gerade z = 2k − 2 (Create). 4. Zwei Beispielnetze als Punkte: Rechenmodell (k = 3, z = 5) liegt darüber, Brücke (k = 4, z = 6) liegt auf der Geraden. 5. Bereichstexte: oberhalb Knotenpotentialverfahren, unterhalb Maschenstromverfahren. Haltepunkt 4. | Lücke: machbar
- k8stempel (09-stempel-und-netzliste.md): animieren ja — Schritte: 1. Leitwert G zwischen i und k: Matrix 2×2-Ausschnitt, Plätze (i,i), (k,k) +G, (i,k), (k,i) −G, einzeln. 2. Feste Stromquelle I_q von k nach i: +I_q rechts in Zeile i, −I_q in Zeile k. 3. Spannungsgesteuerte Stromquelle g·U_pq: Zeilen i, k, Spalten p, q (nicht symmetrisch). Haltepunkt 3. | Lücke: L9 (Zellen einzeln)
- k8verstaerker (10-gesteuerte-quellen-und-verstarker.md): animieren ja — Schritte: 1. Verstärker ohne Gegenkopplung: 20 µA in Knoten 1, U_1 = 20 mV, gesteuerte Quelle zieht Strom aus Knoten 2, U_2 = −4 V. 2. R_S = 1 kΩ erscheint zwischen Fußpunkt und Masse (Knoten 3). 3. Der Ausgangsstrom (roter Pfad, Pakete) fließt durch R_S, Knoten 3 hebt sich (Marker steigt), die Steuerspannung U_1 − U_3 sinkt (Pfeil schrumpft; Skala auf einen Wert, nicht stufenlos), U_2 = −188 mV, A_u = −4,81. 4. G_S → ∞ zurück auf Masse. Haltepunkt 3. | Lücke: L3 (Rückkopplung als Zeitverlauf), als zwei Zustände vorher/nachher machbar
- k8mna (11-die-modifizierte-knotenanalyse.md): animieren ja — Schritte: 1. Netz mit Spannungsquelle zwischen i und k, Matrix Y (unverändert, grau). 2. Neue Spalte für den Quellenstrom I_V (grün, +1 in Zeile i, −1 in Zeile k). 3. Neue Zeile für die Spannungsgleichung U_i − U_k = U_q (rot). 4. Rechenmodell 4×4: U_3 = 9 V aus der letzten Zeile, U_1 = 8 V, U_2 = 10 V, I_V = −1 mA. Haltepunkte 2, 3. | Lücke: L9 (Zeile/Spalte einzeln), sonst machbar

