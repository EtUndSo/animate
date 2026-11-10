# Abbildungen und Animationen — Paket ml_2 (Heft ml/02-projektion-eigenwerte-und-zerlegungen)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.
Deutsche Artikel 01–14. 29 Szenen `ml/k2…` vorhanden: 11 Konzeptbilder (Axes/LabeledArrow/DataCurve/TextBox) und 18 „Rechenbilder“ k2r…. Von den 18 Rechenbildern haben nur 2 eine echte Editor-Operation (`DotProduct`: k2rproj, k2rnormy); die übrigen 16 sind ein einziger statischer `MathTex` und müssen für die Animation auf Σ / Skalarprodukt / Arithmetik umgebaut werden. Auch k2rorth (Bildunterschrift: „Schritt für Schritt“) ist nur MathTex.
Alle 11 Konzeptbilder eignen sich zum Animieren. Fehlende Pflicht-Rechenbilder (Σ/Skalarprodukt mit Zahlen im Kern eines Rechenbeispiels) habe ich im Heft nicht gefunden.

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-projektion-eigenwerte-und-zerlegungen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-orthonormalbasen-und-orthogonale-matrizen | 4 | 3 | 1 | 0 | 0 | 0 | 4 |
| 03-projektion-auf-eine-gerade | 3 | 2 | 0 | 1 | 0 | 0 | 3 |
| 04-die-beste-naherungslosung | 4 | 5 | 0 | 0 | 0 | 0 | 5 |
| 05-projektion-auf-einen-unterraum | 4 | 3 | 1 | 0 | 0 | 0 | 4 |
| 06-quadratische-formen | 3 | 2 | 0 | 1 | 0 | 0 | 3 |
| 07-eigenwerte-und-eigenvektoren | 5 | 3 | 1 | 1 | 0 | 0 | 5 |
| 08-diagonalisierung-und-spektralsatz | 4 | 2 | 2 | 0 | 0 | 0 | 4 |
| 09-positiv-definite-matrizen | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| 10-die-singularwertzerlegung | 5 | 2 | 2 | 1 | 0 | 0 | 5 |
| 11-naherung-durch-matrizen-von-kleinem-rang | 3 | 3 | 0 | 1 | 0 | 0 | 4 |
| 12-die-pseudoinverse | 3 | 1 | 2 | 0 | 0 | 0 | 3 |
| 13-die-konditionszahl | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 14-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Summe** | 46 | 29 | 13 | 6 | 0 | 0 | 48 |

Soll-Abweichungen: 04 (+1) ist Bestand: fünf vorhandene Bilder, alle begründet (Ebene, Ausgleichsgerade, drei Rechenbilder zu drei Rechenbeispielen); keine neue, nichts entfällt. 11 (+1): zwei Pflicht-Rechenbilder und die Bildmatrix sind vorhanden; die flachgedrückte Ellipse (V15) zeigt als einzige, was „Rang k“ geometrisch heißt. Alle anderen Artikel liegen auf dem Soll.

## Top 3

- V8 [A] 08-diagonalisierung-und-spektralsatz — Eigenbasis: derselbe Pfeil, die zwei Anteile werden nur mit 5 und 2 gestreckt, Summe = A·x — zeigt, was „Matrix wird diagonal“ und „entkoppeln“ bedeuten, bisher nur Formel S⁻¹AS
- V9 [A] 08-diagonalisierung-und-spektralsatz — Einwohnerfolge x_k wandert Jahr für Jahr zum Punkt (600, 400), der zweite Anteil halbiert sich — einziges Iterationsverfahren des Hefts ohne Bild
- V12 [A] 10-die-singularwertzerlegung — Einheitskreis wird zur Ellipse, v₁,v₂ landen auf den Achsen als 4u₁ und 1u₂ — Kernidee der SVD, steht bisher nur im Endbild und im Text von 9.1 als Vorgriff auf Abb. 23

## Editor-Lücken

- L5: 3 (V5, V12, V15; Kreis/Koordinatensystem/Ebene durch eine Matrix verformen; notbehelfsweise als zwei Zustände per FadeIn)
- L3: 3 (V10, V13, V16; laufender Punkt mit mitlaufender Länge/Funktionswert; notbehelfsweise MoveAlongPath + Spur oder feste Marker)
- L7: 1 (V14; Matrix aus Bausteinen u·vᵀ als Prozess)
- L9: 1 (V14; Table-Zellen nacheinander betonen)
- L-neu: komplexes Skalarprodukt mit Konjugation (k2rkomplex, kein Vorschlag, nur bei der Umbau-Zeile): 1
- Rest der 19 Vorschläge ist ohne neue Funktion machbar (Rotate um den Ursprung, MoveTo, Scale, MoveAlongPath, FadeIn, Create).
- Für vorhandene Szenen: L5 bei k2eigen, k2svd, k2bild nicht nötig, aber hilfreich (Kreis→Ellipse stetig); L3 bei k2lot (laufender Punkt mit Abstand), k2ausgleich (Gerade dreht sich), k2kondition (Gerade verschiebt sich), k2formen (stetiger Übergang Schüssel→Rinne→Sattel). L10 betrifft alle.

## Vorschläge

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Drei Fragen, drei Bilder
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/01-projektion-eigenwerte-und-zerlegungen.md
- **Stelle:** Worum es geht — „Dieses Kapitel geht dieser Frage nach und zwei weiteren, die sich als eng verwandt herausstellen …“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei nebeneinanderliegende kleine Koordinatensysteme (je x,y ∈ [−2, 5]), ohne Formeln, nur Stichworte als Beschriftung. Feld 1 „nächster Punkt“: Gerade durch 0 in Richtung (1, 2), Punkt y = (4, 3), Lot auf den Fußpunkt (2, 4). Feld 2 „Richtung bleibt“: Einheitskreis, Pfeil (1, 1)/√2 und sein Bild (5, 5)/√2 auf derselben Geraden, daneben e₁ und sein Bild (4, 2) in neuer Richtung. Feld 3 „Bausteine“: Ellipse mit den Halbachsen 4 und 1 (Matrix (2 3; 0 2), Achsen in Richtung (2, 1) und (−1, 2)).
- **Ablauf:** 1. Feld 1: Gerade (Create), y erscheint (FadeIn), Lot wächst (Create), Fußpunkt blinkt (Indicate). 2. Feld 2: Kreis (Create), zwei Pfeile (FadeIn), ihre Bilder wandern per MoveTo; der eine bleibt auf der Geraden, der andere dreht. 3. Feld 3: Kreis (Create), Ellipse erscheint (Create), die beiden Achsen mit „stark“ und „schwach“ (Write). — Haltepunkte: Ende von 1, 2 und 3.
- **Verständnisproblem:** Der Leser sieht vor dem ersten Abschnitt, dass drei scheinbar getrennte Fragen (Näherung, Eigenrichtung, Zerlegung) alle von rechten Winkeln leben.
- **Szenenname:** ml/k2ueberblick
- **Editor-Lücke:** machbar (Ellipse und Bildpfeile als fertig gezeichnete Objekte; stetiges Verformen des Kreises wäre L5)

### Artikel 02 — Orthonormalbasen und orthogonale Matrizen (Soll 4, vorh. 3)

### V2 [A] Orthonormalbasis als gedrehtes Achsenkreuz
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/02-orthonormalbasen-und-orthogonale-matrizen.md
- **Stelle:** Orthonormale Vektoren — „Man stelle sich die beiden Achsen e₁ und e₂ der Ebene vor, als Ganzes um einen Winkel gedreht …“ (Begriff orthogonale Matrix vorbereitend)
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen x₁, x₂ ∈ [−2, 2] mit Raster. e₁ = (1, 0), e₂ = (0, 1) in Grau. Der Pfeil x = (3, 1) und der Kreis mit Radius 1. Zielzustand q₁ = (0,6; 0,8) und q₂ = (−0,8; 0,6) in Grün, Winkel 53,13° als Bogen. Beschriftung „Länge 1“, „90°“, später Qx = (1, 3) mit |x|² = 10 = |Qx|².
- **Ablauf:** 1. e₁, e₂ und x erscheinen. 2. Alle drei drehen sich gemeinsam um den Ursprung um 53,13° (Rotate); Bogen und Winkel erscheinen; q₁, q₂ bleiben senkrecht und auf dem Einheitskreis. 3. x landet bei (1, 3); beide Längenquadrate 10 erscheinen. 4. Unter x ein Spiegelungspfeil: dieselben Achsen gespiegelt (q₂ → −q₂) mit der Beschriftung „det = −1“. — Haltepunkte: Schritt 2 (Winkel erhalten), Schritt 3 (Länge erhalten).
- **Verständnisproblem:** Was eine orthogonale Matrix tut, bevor die Definition QᵀQ = I kommt; dass Länge und Winkel starr bleiben.
- **Szenenname:** ml/k2drehung
- **Editor-Lücke:** machbar (Rotate um Punkt)

### Artikel 03 — Projektion auf eine Gerade (Soll 3, vorh. 2)

### V3 [B] Die Projektionsmatrix drückt die Ebene auf die Gerade
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/03-projektion-auf-eine-gerade.md
- **Stelle:** Die Projektionsmatrix und Projektionen im Allgemeinen — „Jetzt ist klar, was sie tut: Sie ist das Fünffache einer Projektion und drückt die Ebene auf die Gerade …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Felder, x ∈ [−1, 5], y ∈ [−2, 5]. Links die Gerade in Richtung (1, 2) und fünf Punkte (4, 3), (0, 4), (3, 0), (−1, 1), (2, 2) mit dem Lot (gestrichelt) auf die Gerade; Fußpunkte P·y mit P = ⅕(1 2; 2 4); (4, 3) → (2, 4). Rechts die x₁-Achse und dieselben Punkte mit schrägem Licht in Richtung (1, −1) (Matrix (1 1; 0 0)): (0, 1) → (1, 0). Überschrift links „Lot: symmetrisch“, rechts „schräg: nicht symmetrisch“.
- **Ablauf:** 1. Punkte und Gerade (FadeIn). 2. Lote erscheinen nacheinander (Create), jeder Punkt wandert in den Fußpunkt (MoveTo); rechtwinklige Markierung. 3. Wiederholung: Punkte auf der Geraden bleiben (Indicate), das Lot hat Länge 0 (P² = P). 4. Rechts dieselbe Abfolge, aber die Verbindungslinien sind schräg; (0, 1) wandert nach (1, 0), und der Abstand zur Achse ist nicht der kleinste. — Haltepunkte: Schritt 2, Schritt 4.
- **Verständnisproblem:** Was „P² = P“ und „symmetrisch = orthogonal“ geometrisch heißt; der Unterschied zwischen Lot und beliebigem Schatten.
- **Szenenname:** ml/k2platt
- **Editor-Lücke:** machbar

### Artikel 04 — Die beste Näherungslösung (Soll 4, vorh. 5; keine neue)

Kein neuer Vorschlag. Die Stelle „Beste Näherungslösung“ ist durch k2ebene gedeckt, die Normalgleichungen durch k2rnormal, die Ausgleichsgerade durch k2ausgleich/k2rausgleich, die Wohnungen durch k2rwohnungen. Verworfen: ein zusätzliches Bild zu (3.4) Pythagoras — wäre ein Beweisbild, steht aber schon als Rechtwinkel im Bild k2ebene.

### Artikel 05 — Projektion auf einen Unterraum (Soll 4, vorh. 3)

### V4 [A] Orthogonales Komplement: die Ebene und ihre Normale (Szene wiederverwenden)
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/05-projektion-auf-einen-unterraum.md
- **Stelle:** Das orthogonale Komplement — „Projiziert man y auf einen Unterraum, bleibt das Residuum y − Py übrig …“
- **Art:** vorhandene Szene wiederverwenden (ml/k2ebene aus Artikel 04, animiert, um die Normale k ergänzt)
- **Was zu sehen ist:** Die Szene k2ebene: Ebene x₃ = x₁ + x₂ (𝒰, blau), y = (1, 1, 1), Fußpunkt ŷ = (2/3, 2/3, 4/3). Zusätzlich die Gerade 𝒰^⊥ durch 0 in Richtung k = (1, 1, −1) und die Zerlegung y = ŷ + r mit r = (1/3, 1/3, −1/3) = k/3, also parallel zu k. Beschriftung „dim 𝒰 + dim 𝒰^⊥ = 2 + 1 = 3“.
- **Ablauf:** 1. Ebene (FadeIn), y erscheint. 2. ŷ in der Ebene (Create des Lots), r senkrecht. 3. Die Gerade durch k erscheint (Create) und fällt mit r zusammen (Indicate). 4. Die beiden Teilpfeile ŷ und r bilden mit y das rechtwinklige Dreieck; die Dimensionszahlen erscheinen (Write). — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Der Begriff „orthogonales Komplement“ und die eindeutige Zerlegung y = u + z haben bisher keine Anschauung; die Szene ist im Heft schon bekannt.
- **Szenenname:** ml/k2ebene (erweitert um die Gerade k, oder Kopie ml/k2komplement)
- **Editor-Lücke:** machbar (3D-Kamera drehen wäre L4, nicht nötig)

### Artikel 06 — Quadratische Formen (Soll 3, vorh. 2)

### V5 [B] Quadratisch ergänzen macht die schiefe Ellipse gerade
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/06-quadratische-formen.md
- **Stelle:** Quadratisch ergänzen — „Mit gemischten Gliedern sieht man die Form nicht mehr sofort. Ist 5x₁² + 4x₁x₂ + 2x₂² eine Schüssel?“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Höhenlinie f = 1 der Form 5x₁² + 4x₁x₂ + 2x₂² in den (x₁, x₂)-Achsen, x ∈ [−1,2; 1,2], y ∈ [−1,2; 1,2]: schiefe Ellipse (Achsen in Richtung (2, 1) und (1, −2), Halbachsen 1/√6 ≈ 0,41 und 1). Rechts dieselbe Kurve in den Koordinaten z₁ = x₁ + 0,4x₂, z₂ = x₂ als Ellipse 5z₁² + 1,2z₂² = 1 mit den Halbachsen 1/√5 ≈ 0,447 auf der z₁-Achse und 1/√1,2 ≈ 0,913 auf der z₂-Achse, achsenparallel. Zwischen den Feldern der Pfeil „z₁ = x₁ + 0,4x₂“. Beschriftung: „5(x₁+0,4x₂)² + 1,2x₂²: beide Faktoren positiv: Schüssel“; als Gegenprobe Beispiel 2 (x₁² + 6x₁x₂ + x₂² = (x₁+3x₂)² − 8x₂²) als zweite Zeile mit Hyperbelpaar.
- **Ablauf:** 1. Schiefe Ellipse links (Create). 2. Ein Punkt der Kurve, z. B. (1, −1) mit f = 3, wird markiert. 3. Rechts erscheint die Kurve in z-Koordinaten (Create), der Punkt wandert nach (z₁, z₂) = (0,6; −1). 4. Die zwei Faktoren 5 und 1,2 erscheinen (Write) und werden grün (positiv). 5. Gegenprobe Sattel: Faktoren 1 und −8, rotes Vorzeichen. — Haltepunkte: Schritt 3, 4.
- **Verständnisproblem:** Was quadratisches Ergänzen an der Fläche tut (ein Koordinatenwechsel, der die gemischten Glieder beseitigt) und warum die Vorzeichen der Faktoren die Form bestimmen.
- **Szenenname:** ml/k2ergaenzen
- **Editor-Lücke:** braucht Editor-Funktion: L5 (Scherung als stetiger Koordinatenwechsel; ersatzweise zwei Zustände)

### Artikel 07 — Eigenwerte und Eigenvektoren (Soll 5, vorh. 3)

### V6 [A] Die Drehung hat keinen Eigenvektor, aber komplexe Eigenwerte
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/07-eigenwerte-und-eigenvektoren.md
- **Stelle:** Komplexe Eigenwerte — „Eine Drehung um 90° lässt keinen Pfeil auf seiner Geraden: Jeder wird um einen rechten Winkel weitergedreht.“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Ebene (x ∈ [−2, 2]) mit Q = (0,6 −0,8; 0,8 0,6) (Drehung um 53,13°): drei Pfeile (1, 0), (1, 1), (0, 2) und ihre Bilder, nirgends dieselbe Gerade. Rechts die komplexe Ebene (Re, Im ∈ [−1,5; 1,5]) mit dem Einheitskreis und den beiden Eigenwerten 0,6 + 0,8j und 0,6 − 0,8j, gespiegelt an der reellen Achse, Winkel ±53,13°, Beschriftung „e^{±jα}, |λ| = 1“.
- **Ablauf:** 1. Drei Pfeile erscheinen. 2. Alle drehen sich um 53,13° (Rotate); keiner bleibt auf seiner Geraden (Gerade grau, Pfeil verlässt sie). 3. Rechts erscheinen Kreis und Punkt λ = 0,6 + 0,8j (Create), das Spiegelbild λ* (FadeIn), die Beschriftung. 4. Eine zweite Drehmatrix (Winkel 90°) setzt den Punkt auf j (MoveTo): „λ = ±j“. — Haltepunkte: Schritt 2 (kein Eigenvektor), Schritt 3.
- **Verständnisproblem:** Warum eine reelle Matrix komplexe Eigenwerte haben muss, wenn sie in einer Ebene dreht; dass Eigenwerte als Paare auftreten.
- **Szenenname:** ml/k2drehkomplex
- **Editor-Lücke:** machbar (Rotate um Ursprung)

### V7 [B] Eigenwerte als Nullstellen des charakteristischen Polynoms
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/07-eigenwerte-und-eigenvektoren.md
- **Stelle:** Das charakteristische Polynom — „Eine Zahl λ ist genau dann ein Eigenwert von A, wenn p(λ) = 0 ist.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen λ ∈ [−1, 7], p ∈ [−7, 12]. Die Parabel p(λ) = λ² − 7λ + 10 (Matrix (4 1; 2 3)) mit den Nullstellen 2 und 5, Spur 7 = 2 + 5 als Summe, Determinante 10 = p(0) = 2·5 bei λ = 0 markiert. Darunter eine zweite Parabel p(λ) = λ² + 1 (90°-Drehung) im selben Bild blass: sie schneidet die λ-Achse nie.
- **Ablauf:** 1. Achsen und Parabel (Create). 2. Ein Punkt gleitet auf der Parabel (MoveAlongPath), bleibt bei λ = 2 und λ = 5 stehen (Indicate); „p = 0: Eigenwert“. 3. Der Achsenabschnitt p(0) = 10 und die Summe der Nullstellen 7 werden markiert (Spur/Determinante). 4. Die Parabel λ² + 1 erscheint: keine reelle Nullstelle, Verweis „komplex“. — Haltepunkte: Schritt 2, Schritt 4.
- **Verständnisproblem:** Warum die Eigenwerte gerade die Nullstellen sind und wo Spur und Determinante in der Parabel stecken; warum es manchmal keine reellen Eigenwerte gibt.
- **Szenenname:** ml/k2charpoly
- **Editor-Lücke:** machbar (DataCurve, Marker, MoveAlongPath)

### Artikel 08 — Diagonalisierung und Spektralsatz (Soll 4, vorh. 2)

### V8 [A] In der Eigenbasis wird nur gestreckt
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/08-diagonalisierung-und-spektralsatz.md
- **Stelle:** Diagonalisierung — „Nimmt man als Basis die Eigenvektoren, so wird jeder Basisvektor nur mit seinem Eigenwert multipliziert.“
- **Art:** neue Animation
- **Was zu sehen ist:** Ebene x ∈ [−1, 5], y ∈ [−2, 4]. Matrix A = (4 1; 2 3), Eigenvektoren s₁ = (1, 1) (Eigenwert 5, rot) und s₂ = (1, −2) (Eigenwert 2, grün) als Achsen. Der Pfeil x = (1, 0) = (2/3) s₁ + (1/3) s₂ als Parallelogramm aus (2/3, 2/3) und (1/3, −2/3). Ziel: A·x = (4, 2) = (10/3) s₁ + (2/3) s₂ mit den Teilpfeilen (10/3, 10/3) und (2/3, −4/3).
- **Ablauf:** 1. Beide Achsen und x erscheinen; x zerlegt sich in zwei Teilpfeile (Create des Parallelogramms). 2. Der rote Teilpfeil wird auf das Fünffache gestreckt (Scale um den Ursprung, Faktor 5), der grüne auf das Doppelte (Scale, Faktor 2). 3. Die gestreckten Teile addieren sich (Shift zum Parallelogramm): Ergebnis (4, 2); gestrichelt der direkte Weg x → A·x, der dreht. 4. Daneben Koordinaten c = (2/3, 1/3) → (10/3, 2/3), Beschriftung „in dieser Basis: diag(5, 2)“. — Haltepunkte: Schritt 2, Schritt 3.
- **Verständnisproblem:** Was Λ = S⁻¹AS bedeutet: derselbe Pfeil, in schrägen Koordinaten betrachtet, wird nur komponentenweise gestreckt; „entkoppelt“ als Bild.
- **Szenenname:** ml/k2eigenbasis
- **Editor-Lücke:** machbar (Scale um Punkt, Shift); stetige Gitterverzerrung wäre L5

### V9 [A] Wanderung zweier Orte: die Folge x_k entkoppelt sich
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/08-diagonalisierung-und-spektralsatz.md
- **Stelle:** Entkoppeln: Potenzen und Folgen — „Zwei Orte A und B tauschen jedes Jahr Einwohner aus …“ (Rechenbeispiel x_k = (600 + 400·0,5^k, 400 − 400·0,5^k))
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen: Einwohner A (x ∈ [0, 1000]) gegen Einwohner B (y ∈ [0, 600]). Die Gerade x + y = 1000 (Gesamtzahl bleibt), der Fixpunkt (600, 400) und die Richtung s₂ = (1, −1). Punkte x₀ = (1000, 0), x₁ = (800, 200), x₂ = (700, 300), x₃ = (650, 350), x₄ = (625, 375). Rechts ein Balkenpaar der beiden Anteile 200·s₁ = (600, 400) (bleibt) und 400·0,5^k·s₂ (halbiert sich).
- **Ablauf:** 1. Gerade und Fixpunkt (Create). 2. x₀ erscheint, dann x₁, x₂, x₃, x₄ nacheinander (je FadeIn mit Verbindungspfeil, Beschriftung „Jahr k“); die Abstände zum Fixpunkt sind 400, 200, 100, 50, 25. 3. Gleichzeitig halbiert sich der Balken des zweiten Anteils (Scale), der erste bleibt (Indicate). 4. Schlussbeschriftung „auf lange Sicht (600, 400)“. — Haltepunkte: Schritt 2 (nach x₂), Schritt 3.
- **Verständnisproblem:** Warum der betragsgrößte Eigenwert auf lange Sicht überwiegt und die Anteile mit kleinerem Eigenwert verschwinden; die Folge als Iteration sehen.
- **Szenenname:** ml/k2wanderung
- **Editor-Lücke:** machbar (Iteration als Folge von Erscheinen); L1 (Verschwinden) hilfreich

### Artikel 09 — Positiv definite Matrizen (Soll 3, vorh. 1)

### V10 [A] Der Rayleigh-Quotient auf dem Einheitskreis
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/09-positiv-definite-matrizen.md
- **Stelle:** Größter und kleinster Wert auf dem Einheitskreis — „Eine quadratische Form wächst mit dem Quadrat der Länge von x. Wie stark sie in verschiedenen Richtungen wächst, sieht man, wenn man nur Vektoren der Länge 1 einsetzt.“
- **Art:** neue Animation
- **Was zu sehen ist:** Links der Einheitskreis (x ∈ [−1,5; 1,5]) mit einem umlaufenden Einheitsvektor x(φ) und den Eigenrichtungen q₁ = (2, 1)/√5 (φ = 26,57°) und q₂ = (1, −2)/√5 (φ = 116,57°). Rechts ein Graph des Rayleigh-Quotienten f(φ) = xᵀAx = 3,5 + 2,5·cos(2φ − 53,13°) über φ ∈ [0°, 180°], f ∈ [0, 7], mit den Linien f = 6 (λ_max) und f = 1 (λ_min). Matrix A = (5 2; 2 2). Marken bei φ = 0 (f = 5, e₁), 45° (f = 5,5), 135° (f = 1,5).
- **Ablauf:** 1. Kreis, q₁, q₂ und die beiden Grenzlinien. 2. x(φ) startet bei e₁ (f = 5) und läuft um den Kreis (MoveAlongPath), rechts wächst die Kurve mit (Create). 3. Bei φ = 26,57° stoppt der Punkt: f = 6, Marker „Maximum = größter Eigenwert“; bei 116,57° f = 1. 4. Die Kurve schließt sich; sie liegt immer zwischen 1 und 6. — Haltepunkte: Maximum und Minimum.
- **Verständnisproblem:** Dass die Form zwischen kleinstem und größtem Eigenwert liegt und die Extremwerte in den Eigenrichtungen angenommen werden; „gewichtetes Mittel der Eigenwerte“ als Bild.
- **Szenenname:** ml/k2rayleighkreis
- **Editor-Lücke:** braucht Editor-Funktion: L3 (Punkt auf Kreis mit mitlaufendem Funktionswert; ersatzweise MoveAlongPath und Spur per Create)

### V11 [B] Definit, semidefinit, indefinit an den Höhenlinien
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/09-positiv-definite-matrizen.md
- **Stelle:** Der Eigenwerttest — „Hat eine symmetrische Matrix positive und negative Eigenwerte, so ist ihre Form in manchen Richtungen positiv und in anderen negativ: ein Sattel.“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei Felder (x₁, x₂ ∈ [−1,5; 1,5]), je mit der Höhenlinie f = 1 und den Eigenrichtungen. (5 2; 2 2): Eigenwerte 6 und 1, Ellipse mit Halbachsen 0,41 und 1 („positiv definit“). (1 2; 2 4): Eigenwerte 5 und 0, zwei parallele Geraden in Richtung (2, −1) mit Abstand 1/√5 von 0 („semidefinit“, Rinne). (1 3; 3 1): Eigenwerte 4 und −2, Hyperbeln f = 1 (kräftig) und f = −1 (blass) mit den Asymptoten x₁ = ±x₂ („indefinit“).
- **Ablauf:** 1. Feld 1 erscheint, die Eigenwerte 6 und 1 daneben (Write). 2. Feld 2: Die Ellipse „reißt“ auf eine Streifenform auf (Zustandswechsel per FadeIn), Eigenwert 0. 3. Feld 3: Hyperbeln (Create), ein negativer Eigenwert, f(1, −1) = −4 als Marker. — Haltepunkte: Feld 2, Feld 3.
- **Verständnisproblem:** Warum der Eigenwerttest die Form erfasst und warum positive Einträge nichts über die Definitheit sagen.
- **Szenenname:** ml/k2definit
- **Editor-Lücke:** machbar (DataCurve; stetiger Übergang wäre L3)

### Artikel 10 — Die Singulärwertzerlegung (Soll 5, vorh. 2)

### V12 [A] Der Kreis wird zur Ellipse; v₁, v₂ landen auf den Achsen
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/10-die-singularwertzerlegung.md
- **Stelle:** Senkrechte Richtungen, die senkrecht bleiben — „Trotzdem macht sie aus dem Einheitskreis eine Ellipse (Abb. 23), und eine Ellipse hat zwei senkrechte Achsen. Welche Pfeile des Kreises landen auf diesen Achsen?“ (Verweis auf Abb. 23 ist hier ein Vorgriff: v, u, D sind noch nicht eingeführt)
- **Art:** neue Animation
- **Was zu sehen ist:** Eine Ebene x, y ∈ [−4, 4]. Matrix A = (2 3; 0 2). Der Einheitskreis, v₁ = (1, 2)/√5 (rot) und v₂ = (−2, 1)/√5 (grün). Die Bilder A·v₁ = (8, 4)/√5 (Länge 4) und A·v₂ = (−1, 2)/√5 (Länge 1) auf den Achsen der Ellipse; rechter Winkel zwischen den Bildern markiert, Skalarprodukt 0. Daneben als Kontrast e₁ → (2, 0) und e₂ → (3, 2) (gestrichelt, die nicht senkrecht bleiben).
- **Ablauf:** 1. Kreis, v₁, v₂ (grau, senkrecht). 2. Die Ellipse zeichnet sich (Create), die Bilder A·v₁ und A·v₂ erscheinen auf den Ellipsenachsen mit Länge 4 und 1; rechter Winkel markiert. 3. Kontrast: e₁, e₂ und ihre Bilder, deren Winkel kein rechter ist. — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Was gesucht wird: zwei senkrechte Richtungen, deren Bilder senkrecht bleiben; vorher nur Text und Formel mit AᵀA.
- **Szenenname:** ml/k2svdidee
- **Editor-Lücke:** braucht Editor-Funktion: L5 (Kreis stetig zur Ellipse; ersatzweise Endellipse per Create)

### V13 [A] Spektralnorm: der größte Streckfaktor
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/10-die-singularwertzerlegung.md
- **Stelle:** Die Spektralnorm — „Wie stark kann eine Matrix einen Vektor höchstens verlängern?“
- **Art:** neue Animation
- **Was zu sehen ist:** Links der Einheitskreis mit einem umlaufenden Einheitsvektor x(φ) und den Marken e₁, e₂, v₁ = (1, 2)/√5 (φ = 63,43°), v₂ (φ = 153,43°). Rechts die Ellipse A·x(φ) mit A = (2 3; 0 2) und der Länge ‖Ax‖ als Balken oder Graph über φ ∈ [0°, 180°], ‖Ax‖ ∈ [0, 4,5], mit den Linien d₁ = 4 und d₂ = 1. Marken: ‖Ae₁‖ = 2, ‖Ae₂‖ = √13 ≈ 3,61, ‖Av₁‖ = 4, ‖Av₂‖ = 1.
- **Ablauf:** 1. Kreis und Ellipse (Create). 2. Der Einheitsvektor läuft um den Kreis (MoveAlongPath), sein Bild läuft um die Ellipse, der Graph von ‖Ax‖ wächst mit. 3. Halt bei e₁ (2), e₂ (3,61), v₁ (4: Maximum), v₂ (1: Minimum). 4. Beschriftung „‖A‖₂ = d₁ = 4; kleinster Faktor d₂ = 1“. — Haltepunkte: e₁, e₂, v₁, v₂.
- **Verständnisproblem:** Spektralnorm als „größter Streckfaktor“ und dass Singulärwerte nicht mit Eigenwerten (2, 2) übereinstimmen; Vorbereitung für die Kondition.
- **Szenenname:** ml/k2spektralnorm
- **Editor-Lücke:** braucht Editor-Funktion: L3 (laufender Punkt mit mitlaufender Länge; ersatzweise vier feste Marker)

### V14 [B] Die Matrix als Summe von Bausteinen vom Rang 1
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/10-die-singularwertzerlegung.md
- **Stelle:** Die Zerlegung — „In kompakter Form: 4·⅕(2 4; 1 2) + 1·⅕(2 −1; −4 2) = (1,6 3,2; 0,8 1,6) + (0,4 −0,2; −0,8 0,4) = (2 3; 0 2)“
- **Art:** neue Animation
- **Was zu sehen ist:** Drei 2×2-Tabellen nebeneinander: Baustein 1 (1,6 3,2; 0,8 1,6), Pluszeichen, Baustein 2 (0,4 −0,2; −0,8 0,4), Gleichheitszeichen, Ergebnis (2 3; 0 2). Links darüber die Spalte u₁ = (2, 1)/√5 und die Zeile v₁ᵀ = (1, 2)/√5, Faktor d₁ = 4; die Zeilen/Spalten des Bausteins sind Vielfache von u₁ (Rang 1).
- **Ablauf:** 1. Baustein 1 entsteht aus u₁ · v₁ᵀ (Zelle für Zelle: 2·1 = 2, 2·2 = 4, … /5, mal 4). 2. Baustein 2 aus u₂, v₂, Faktor 1. 3. Zelle für Zelle addiert: 1,6 + 0,4 = 2; 3,2 − 0,2 = 3; 0,8 − 0,8 = 0; 1,6 + 0,4 = 2. — Haltepunkte: Schritt 1 und 3.
- **Verständnisproblem:** Dass jedes Produkt u·vᵀ eine Matrix vom Rang 1 ist und die Summe die ursprüngliche Matrix zurückliefert; Grundlage der Näherung in Artikel 11.
- **Szenenname:** ml/k2bausteine
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Zellen einzeln betonen) und L7 (äußeres Produkt/Matrixsumme als Prozess)

### Artikel 11 — Näherung durch Matrizen von kleinem Rang (Soll 3, vorh. 3)

### V15 [B] Rang 1: die Ellipse wird zur Strecke
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/11-naherung-durch-matrizen-von-kleinem-rang.md
- **Stelle:** Die abgeschnittene Zerlegung — „Bricht man die Summe (9.4) nach den k größten Bausteinen ab, erhält man eine Näherung.“ (oder bei Eckart-Young: „Der Beweis zeigt den Grund: Eine Matrix vom Rang k muss eine ganze Menge von Richtungen auf null abbilden …“)
- **Art:** neue Animation
- **Was zu sehen ist:** Ebene x, y ∈ [−4, 4]. Der Einheitskreis wird von A = (2 3; 0 2) zur Ellipse mit den Halbachsen 4u₁ und 1·u₂ (u₁ = (2, 1)/√5, u₂ = (−1, 2)/√5). Von A₁ = 4u₁v₁ᵀ wird derselbe Kreis auf die Strecke von −4u₁ bis +4u₁ gedrückt. Der Fehler ist der Abstand 1 in Richtung u₂ (rot), Beschriftung „‖A − A₁‖ = d₂ = 1“. Zum Vergleich B = (2 3; 0 0): Kreis → Strecke in x-Richtung, Fehler 2 (gestrichelt, länger).
- **Ablauf:** 1. Ellipse (Create) mit Achsen. 2. Die kurze Achse schrumpft auf null (Scale in Richtung u₂): Strecke; Pfeile am Rand zeigen den Verlust 1. 3. Zum Vergleich B: andere Strecke, Fehler 2. — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Was „Rang k“ als Bild heißt (gedrückte Ellipse) und warum die abgeschnittene Zerlegung näher liegt als jede andere Rang-1-Matrix.
- **Szenenname:** ml/k2rangellipse
- **Editor-Lücke:** braucht Editor-Funktion: L5 (Ellipse stetig zur Strecke; ersatzweise zwei Zustände)

### Artikel 12 — Die Pseudoinverse (Soll 3, vorh. 1)

### V16 [A] Rechtsinverse: die kürzeste Lösung ist der Fußpunkt vom Nullpunkt
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/12-die-pseudoinverse.md
- **Stelle:** Rechtsinverse — „Geometrisch ist die Lösungsmenge eine Gerade oder Ebene, die nicht durch den Nullpunkt geht, und G·y ist ihr Punkt, der dem Nullpunkt am nächsten liegt.“
- **Art:** neue Animation
- **Was zu sehen ist:** Achsen x₁, x₂ ∈ [−2, 5]. Die Lösungsgerade x₁ + 2x₂ = 5 (Punkt (1, 2), Richtung (2, −1)); Normalenpfeil (1, 2) vom Nullpunkt zum Fußpunkt. Weitere Lösungen bei t = −1: (−1, 3) und t = 1: (3, 1) mit gestrichelten Strecken zum Nullpunkt, Längenquadrate 5 + 5t²: 10, 5, 10.
- **Ablauf:** 1. Gerade (Create), 2. Lösungspunkte t = −1, 1, 2 erscheinen nacheinander (FadeIn) mit Strecken zum Nullpunkt und Längenquadrat. 3. Der Fußpunkt t = 0: Strecke ist die kürzeste (√5), rechter Winkel zur Geraden (Indicate). — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Warum die Rechtsinverse unter unendlich vielen Lösungen gerade die kürzeste liefert; Verbindung zur Projektion aus Abschnitt 2.
- **Szenenname:** ml/k2kuerzeste
- **Editor-Lücke:** braucht Editor-Funktion: L3 (laufender Punkt mit mitlaufender Länge; ersatzweise drei feste Marker)

### V17 [A] Pseudoinverse: das Urbild, der Fußpunkt und das Bild
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/12-die-pseudoinverse.md
- **Stelle:** Die kürzeste beste Näherungslösung — „Für A = (1 2; 2 4) und y = (1, 1) ist x⁺ = 1/25(1 + 2, 2 + 4) = (0,12; 0,24) …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Felder. Links der Eingangsraum (x₁, x₂ ∈ [−1, 2]): die Gerade der besten Näherungslösungen x₁ + 2x₂ = 3/5 (Punkte (0,6; 0), (0; 0,3), (1; −0,2)) und x⁺ = (0,12; 0,24) als Fußpunkt des Lots vom Nullpunkt. Rechts der Ausgangsraum (y₁, y₂ ∈ [−0,5; 2]): die Bildgerade (Vielfache von (1, 2)), y = (1, 1) abseits, die Projektion ŷ = (0,6; 1,2); alle Punkte der linken Geraden gehen unter A auf ŷ.
- **Ablauf:** 1. Rechts: y, die Bildgerade und ŷ = P·y (Lot). 2. Links: Die Lösungsgerade erscheint; drei Punkte werden mit ihren Pfeilen auf ŷ geführt (MoveTo-Pfeile). 3. x⁺ wird als der kürzeste Punkt markiert; Pfeil zurück: A⁺ bildet ŷ auf x⁺ ab. — Haltepunkte: Schritt 2, 3.
- **Verständnisproblem:** Warum die Pseudoinverse zwei Dinge in einem erledigt: erst auf das Bild projizieren (beste Näherung), dann den kürzesten Urbildpunkt wählen.
- **Szenenname:** ml/k2pseudo
- **Editor-Lücke:** machbar

### Artikel 13 — Die Konditionszahl (Soll 3, vorh. 2)

### V18 [A] Fehler in den Daten, Fehler in der Lösung: der schlimmste Fall
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/13-die-konditionszahl.md
- **Stelle:** Die Konditionszahl — „Der schlimmste Fall ist also: Die Lösung liegt in der Richtung, die A am stärksten streckt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Felder für A = (2 3; 0 2) (d₁ = 4, d₂ = 1, κ = 4). Links die Lösungsebene (x ∈ [−1,5; 1,5]): x = v₁ = (1, 2)/√5 (Länge 1) und ein Fehler Δx = 0,2·v₂ (Länge 0,2); rechts die Datenebene (y ∈ [−5, 5]): y = A·v₁ = 4u₁ (Länge 4) und Δy = 0,2·u₂ (Länge 0,2, kaum sichtbar). Relative Fehler: Δy/y = 0,2/4 = 5 %, Δx/x = 0,2/1 = 20 %; Verstärkung 20/5 = 4 = κ.
- **Ablauf:** 1. Rechts (Daten): langer Pfeil y und kleiner Fehlerpfeil Δy (ineinander gezeichnet, FadeIn). 2. Pfeil „A⁻¹: zurückrechnen“; links erscheint x und ein deutlich größerer Fehlerpfeil Δx. 3. Die Anteile 5 % und 20 % werden eingeblendet (Write), Verstärkung 4. 4. Gegenprobe mit y ∈ Richtung u₂ und Δy ∈ Richtung u₁: kleiner Verstärkungsfaktor (1/4); der Pfeil schrumpft. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Die Konditionszahl als Verhältnis der größten zur kleinsten Streckung: das Zurückrechnen vergrößert den Fehler in der schwach gestreckten Richtung am stärksten.
- **Szenenname:** ml/k2verstaerkung
- **Editor-Lücke:** machbar

### Artikel 14 — Das Wichtigste bis hier (Soll 1, vorh. 0)

### V19 [A] Ein Prinzip hinter allen Ergebnissen (Zusammenschau)
- **Artikel:** content/ml/02-projektion-eigenwerte-und-zerlegungen/14-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt aus einem Prinzip: In einem rechtwinkligen Achsenkreuz zerfällt ein Längenquadrat nach Pythagoras …“
- **Art:** vorhandene Szene wiederverwenden (ml/k2lot aus Artikel 03 in animierter Fassung; Ergänzung: Beschriftung „|y|² = |ŷ|² + |r|²“ mit 25 = 20 + 5)
- **Was zu sehen ist:** Wie k2lot: Gerade in Richtung (1, 2), y = (4, 3), ŷ = (2, 4), r = (2, −1); das rechtwinklige Dreieck 0, ŷ, y mit den Längenquadraten 20, 5 und 25, und ein anderer Punkt der Geraden (1, 2) als Hypotenuse zum Vergleich (Abstandsquadrat 10 = 5 + 5).
- **Ablauf:** 1. Gerade und y; Lot und Fußpunkt (Create). 2. Rechter Winkel markiert; die drei Längenquadrate werden eingeblendet (Write). 3. Vergleichspunkt (1, 2): längere Hypotenuse mit 10 = 5 + 5 (Indicate). — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Alle Ergebnisse des Kapitels in einem Bild: senkrecht heißt kürzeste Entfernung und gemischte Glieder fallen weg.
- **Szenenname:** ml/k2lot
- **Editor-Lücke:** machbar

## Vorhandene Abbildungen

- k2rorth (02-orthonormalbasen…): animieren ja — Schritte: 1. q₁ und q₂ als Spalten. 2. Komponente mal Komponente: 0,6·(−0,8) = −0,48, 0,8·0,6 = 0,48. 3. Summe 0. Umbau von MathTex auf DotProduct nötig, Bildunterschrift sagt bereits „Schritt für Schritt“ | Lücke: machbar
- k2onb (02): animieren ja — Schritte: 1. Achsen und q₁, q₂ (grün). 2. x = (3, 1) erscheint. 3. Lot auf q₁-Achse, Schatten 2,6. 4. Lot auf q₂-Achse, Schatten −1,8. 5. x = 2,6 q₁ − 1,8 q₂ | Lücke: machbar
- k2rkoord (02): animieren ja — Schritte: 1. c₁ = q₁ᵀx = (3/5)·3 + (4/5)·1 = 13/5. 2. c₂ = (−4/5)·3 + (3/5)·1 = −9/5. 3. Σ c² = 169/25 + 81/25 = 10. Umbau MathTex → 2× DotProduct + Σ | Lücke: machbar
- k2lot (03-projektion-auf-eine-gerade): animieren ja — Schritte: 1. Gerade und y. 2. Punkte t = 0, 1, 2, 3, 4 mit Abständen² 25, 10, 5, 10, 25 nacheinander (wie in Aufgabe 5). 3. Lot bei t = 2, rechter Winkel. Muster wie hm1/k8projektion | Lücke: L3 (laufender Punkt) | ersatzweise fünf Marker
- k2rproj (03): animieren ja (echtes DotProduct vorhanden, 2×) — Schritte: 1. aᵀy = 1·4 + 2·3 = 10. 2. aᵀa = 1 + 4 = 5. 3. x̂ = 10/5 = 2 | Lücke: machbar
- k2ebene (04-die-beste-naherungslosung): animieren ja — Schritte: 1. Ebene aus a₁ = (1, 0, 1), a₂ = (0, 1, 1). 2. y = (1, 1, 1) abseits. 3. ŷ = (2/3, 2/3, 4/3). 4. r senkrecht. Wird in V4 und evtl. V19 wiederverwendet | Lücke: machbar (Kamera drehen L4 hilfreich)
- k2rnormal (04): animieren ja — Schritte: 1. a₁ᵀa₂ = 1·0 + 0·1 + 1·1 = 1. 2. a₁ᵀy = 1 + 0 + 1 = 2. Umbau MathTex → 2× DotProduct | Lücke: machbar
- k2ausgleich (04): animieren ja — Schritte: 1. drei Messpunkte (0,1), (1,2), (2,4). 2. Ausgleichsgerade y = 5/6 + 3/2 t. 3. Residuen 1/6, −1/3, 1/6 (rot). 4. Quadratsumme 1/36 + 1/9 + 1/36 = 1/6. Vorher eine schlechtere Gerade zum Vergleich | Lücke: L3 (Gerade dreht sich, Summe sinkt) | ersatzweise zwei Zustände
- k2rausgleich (04): animieren ja — Schritte: 1. Σ tᵢ² = 0 + 1 + 4 = 5. 2. Σ tᵢyᵢ = 0·1 + 1·2 + 2·4 = 10. Umbau MathTex → 2× Σ | Lücke: machbar
- k2rwohnungen (04): animieren ja — Schritte: 1. a₁ᵀa₁ = 3600 + 1600 + 8100 + 4900 = 18 200. 2. a₁ᵀy = 12 000 + 5200 + 26 100 + 16 800 = 60 100. Umbau MathTex → 2× DotProduct | Lücke: machbar. Hinweis Artikel 04 hat 5: alle behalten, k2rnormal und k2rwohnungen sind die Rechenbilder zu zwei verschiedenen Beispielen
- k2gramschmidt (05-projektion-auf-einen-unterraum): animieren ja — Schritte: 1. a₁ = (2, 1), a₂ = (1, 2). 2. q₁ = a₁/√5. 3. Schatten (1,6; 0,8) von a₂ auf q₁. 4. Rest q̃₂ = (−0,6; 1,2). 5. Normiert q₂ = (−1, 2)/√5. Doppelung mit hm1 Heft 9 (Gram-Schmidt) nur im Prinzip; eigenes Bild behalten | Lücke: machbar
- k2rgs (05): animieren ja — Schritte: 1. q₁ᵀa₂ = (1·0 + 0·1 + 1·1)/√2 = 1/√2. 2. Rest (−½, 1, ½): ¼ + 1 + ¼ = 3/2. Umbau MathTex → DotProduct + Σ | Lücke: machbar
- k2rqr (05): animieren ja — Schritte: 1. q₁ᵀy = 2/√2 = √2. 2. q₂ᵀy = (−1 + 2 + 1)/√6 = 2/√6. Umbau MathTex → 2× DotProduct | Lücke: machbar
- k2rqf (06-quadratische-formen): animieren ja — Schritte: Doppelsumme an x = (1, −1): 5·1·1 + 2·1·(−1) + 2·(−1)·1 + 2·(−1)·(−1) = 5 − 2 − 2 + 2 = 3, ein Glied nach dem anderen. Umbau MathTex → Σ über vier Glieder | Lücke: machbar
- k2formen (06): animieren ja — Schritte: 1. Schüssel x₁² + 2x₂² (Fläche, Höhenlinien Ellipsen). 2. Rinne x₁². 3. Sattel x₁² − x₂². Die drei Zustände nacheinander (Create) | Lücke: L3 (stetiger Übergang Schüssel→Rinne→Sattel über den Koeffizienten von x₂²) | ersatzweise drei Zustände
- k2rkomplex (07-eigenwerte-und-eigenvektoren): animieren ja — Schritte: 1. v* = (1, j). 2. Glieder 1·1 = 1, j·(−j) = 1. 3. Summe 2. Umbau MathTex → Skalarprodukt mit komplexen Zahlen | Lücke: L-neu: komplexes Skalarprodukt mit Konjugation (ersatzweise Arithmetik mit j)
- k2eigen (07): animieren ja — Schritte: 1. Einheitskreis (grau). 2. Ellipse als Bild (Create). 3. v₁ = (1, 1)/√2 und Bild ×5 auf der Eigengeraden; v₂ = (1, −2)/√5 und Bild ×2. 4. e₁ → (4, 2), Richtung ändert sich | Lücke: L5 (stetiges Verformen des Kreises) | machbar mit fertigen Objekten
- k2rspur (07): animieren ja — Schritte: 1. Diagonale 4 und 3 markieren, 4 + 3 = 7. 2. Eigenwerte 5 und 2, 5 + 2 = 7. Umbau MathTex → Σ | Lücke: machbar
- k2rsenkrecht (08-diagonalisierung…): animieren ja — Schritte: (2, 1)·(1, −2) = 2·1 + 1·(−2) = 0. Umbau MathTex → DotProduct | Lücke: machbar
- k2ellipse (08): animieren ja — Schritte: 1. Achsen. 2. Ellipse f = 1 und f = ¼. 3. Eigenrichtungen q₁, q₂. 4. Halbachsen 1/√6 = 0,41 (rot) und 1 (grün) | Lücke: machbar
- k2rrayleigh (09-positiv-definite-matrizen): animieren ja — Schritte: 1. xᵀAx an (1, 1): 5 + 2 + 2 + 2 = 11. 2. xᵀx = 2. 3. Quotient 11/2 = 5,5 zwischen 1 und 6. Umbau MathTex → Σ/Σ/Arithmetik | Lücke: machbar
- k2rsvdidee (10-die-singularwertzerlegung): animieren ja — Schritte: 1. A v₁ · A v₂ = (8·(−1) + 4·2)/5 = 0. 2. Längenquadrate 80/5 = 16 und 5/5 = 1. Umbau MathTex → DotProduct (3×) | Lücke: machbar
- k2svd (10): animieren ja — Schritte: 1. Einheitskreis mit v₁, v₂. 2. Vᵀ dreht um −63,4°. 3. D streckt um 4 und 1. 4. U dreht um 26,6°. 5. Punkt e₂ landet bei (3, 2); direkter Weg A. Vier Teilbilder, die nacheinander erscheinen und durch Rotate/Scale verbunden werden | Lücke: L5 (Gitter-Morph) | ersatzweise Zustände
- k2rfrobenius (11-naherung-durch-matrizen-von-kleinem-rang): animieren ja — Schritte: 4 + 9 + 0 + 4 = 17 = 4² + 1². Umbau MathTex → Σ | Lücke: machbar
- k2rfehler (11): animieren ja — Schritte: 0,4² + (−0,2)² + (−0,8)² + 0,4² = 0,16 + 0,04 + 0,64 + 0,16 = 1. Umbau MathTex → Σ | Lücke: machbar
- k2bild (11): animieren ja — Schritte: 1. Kreuz C (3×3). 2. Pfeil, Rang-1-Näherung C₁ (4/3 in der Mitte). 3. Fehler C − C₁ (rot/blau) | Lücke: machbar (Table ist gefärbte TextBox; L9 für Zellen)
- k2rmittel (12-die-pseudoinverse): animieren ja — Schritte: 1ᵀy = 4 + 5 + 9 = 18, geteilt durch 3 ergibt 6. Umbau MathTex → DotProduct + Arithmetik | Lücke: machbar
- k2kondition (13-die-konditionszahl): animieren ja — Schritte: Links: senkrechte Geraden, Verschiebung 0,2 → Schnittpunkt wandert 0,2. Rechts: Schnittwinkel 8°, Schnittpunkt wandert 1,44 | Lücke: L3 (Gerade verschiebt sich stetig) | machbar mit Gestrichelt
- k2rnormy (13): animieren ja (echtes DotProduct vorhanden) — Schritte: yᵀy = 4 + 4,0401 = 8,0401, Wurzel 2,8355 | Lücke: machbar
