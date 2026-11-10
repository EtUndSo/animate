# Abbildungen und Animationen — Paket ml_1 (Heft ml/01-vektoren-und-matrizen)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.
Deutsche Artikel 01–17. 42 Szenen `ml/k1…` vorhanden (davon 4 mit echter Operation `DotProduct`: k1rskp, k1rmuster, k1rschatten, k1rstrom;
die übrigen „Rechenbilder“ k1r… bestehen aus einem einzigen statischen `MathTex`; die Konzeptbilder aus Axes/LabeledArrow/Text/TextBox).
Hinweis zu allen `k1r…`-MathTex-Rechenbildern: Als Animation werden sie zeilenweise/schrittweise aufgebaut (Write je Zeile, Summanden nacheinander) oder durch die
Editor-Operationen Σ / Skalarprodukt / Arithmetik ersetzt; „Umformen“ einer Zeile in die nächste braucht L2.

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-vektoren-und-matrizen | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-vektoren-daten-als-zahlenlisten | 5 | 5 | 1 | 0 | 0 | 1 | 5 |
| 03-das-skalarprodukt | 3 | 6 | 0 | 0 | 0 | 2 | 4 |
| 04-normen-die-groe-eines-vektors | 4 | 6 | 1 | 0 | 0 | 2 | 5 |
| 05-abstande-und-einheiten | 4 | 4 | 1 | 0 | 0 | 0 | 5 |
| 06-winkel-und-ahnlichkeit | 4 | 5 | 1 | 0 | 0 | 1 | 5 |
| 07-matrizen-und-die-datenmatrix | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 08-das-matrix-vektor-produkt | 2 | 4 | 1 | 0 | 0 | 2 | 3 |
| 09-lineare-abbildungen | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| 10-das-matrixprodukt | 3 | 4 | 0 | 0 | 0 | 0 | 4 |
| 11-transponierte-symmetrie-und-gram-matrix | 2 | 1 | 1 | 1 | 0 | 0 | 3 |
| 12-einheitsmatrix-und-inverse | 2 | 0 | 2 | 0 | 0 | 0 | 2 |
| 13-lineare-gleichungssysteme | 3 | 1 | 1 | 1 | 0 | 0 | 3 |
| 14-unabhangigkeit-basis-und-rang | 4 | 1 | 2 | 1 | 0 | 0 | 4 |
| 15-die-determinante | 3 | 2 | 1 | 1 | 0 | 0 | 4 |
| 16-elementweise-rechnen-und-tensoren | 2 | 1 | 2 | 0 | 0 | 0 | 3 |
| 17-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Summe** | 48 | 42 | 18 | 5 | 0 | 8 | 57 |

Soll-Abweichungen (+1) sind begründet: 03 (vier verschiedene Rechenbeispiele je ein Rechenbild), 04 (Anschauung der drei Normen plus Einheitskugel, Fehlervektor, Effektivwert), 05 und 06 (zwei Verfahren bzw. Winkel plus Rechenbilder), 10, 11, 15, 16 (je eine zusätzliche Aussage, die ohne Bild Text bleibt). Zusammengelegte Szenen („entfällt“) bleiben inhaltlich erhalten, sie werden Teil der behaltenen Szene.

## Top 3

- V14 [A] 13-lineare-gleichungssysteme — Gauß-Verfahren Zeile für Zeile an der erweiterten Matrix des Artikels — das einzige Rechenverfahren des Hefts ohne jedes Bild, reine Zahlenfolge
- V12 [A] 12-einheitsmatrix-und-inverse — Inverse macht eine Abbildung rückgängig (Punkt hin und zurück) — der Begriff „Inverse“ hat sonst keine Anschauung; zugleich die Brücke zu singulär (V13)
- V2 [A] 02-vektoren-daten-als-zahlenlisten — Linearkombination und Einheitsvektoren als Pfeile — Grundbegriff, auf dem Spaltensicht, lineare Abbildungen und Basis des ganzen Hefts aufbauen

Außerdem auffällig: Von 42 vorhandenen Szenen sind 27 „Rechenbilder“ (k1r…); nur 4 davon (k1rskp, k1rmuster, k1rschatten, k1rstrom) nutzen eine Editor-Operation, die übrigen 23 sind ein einziger statischer MathTex. Für die Pflicht „Rechenbilder als Prozess“ müssen sie erst auf Σ/Skalarprodukt/Arithmetik oder auf zeilenweises Aufbauen umgebaut werden.

## Editor-Lücken

Für die 23 neuen Vorschläge (15 sind ohne neue Editor-Funktion machbar):
- L9: 5 (V6, V10, V11, V14, V21; Table-Zellen/Zeilen einzeln betonen, heute nur mit übergelegten Rechtecken)
- L5: 3 (V9, V12, V20; Matrix auf Figur/Gitter anwenden; als zwei Zustände per FadeIn notbehelflich machbar). V19 ist als Pfeil-Bild machbar, ein Spiegelungs-Morph wäre L5
- L2: 2 (V10, V14; Zeile/Formel in nächste Zeile umformen)
- L7: 2 (V11, V21; Matrix·Matrix und elementweise Rechnung als Prozess)
- L4: 1 hilfreich, nicht nötig (V15; 3D-Kamera drehen)
- L-neu: 0

Für die vorhandenen Szenen: L5 bei k1ebene, k1reihenfolge, k1det, k1einheiten; L9 bei k1datenmatrix, k1raeusser, k1rlaplace, k1rdoppel; L7 bei k1rmv, k1rprodukt, k1rzeilen/k1rspalten, k1rmittelvektor; L3 bei k1einheitskugeln (stetiges p) und k1lgs (Schieberegler). L10 (Abspielknopf im Artikel) betrifft alle.

## Vorschläge

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Von der Wohnung zur Schätzung (Zusammenschau)
- **Artikel:** content/ml/01-vektoren-und-matrizen/01-vektoren-und-matrizen.md
- **Stelle:** Worum es geht — „Dieses Kapitel geht der Frage nach, wie man viele Messwerte vieler Dinge so aufschreibt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Blockbild aus TextBoxen, zwei Zeilen. Oben: „Wohnung 1“ → „Zahlenliste (60 | 2 | 3)“ → „eine Rechnung“ → „Schätzung 188“. Unten: „4 Wohnungen“ → „Tabelle 4 Zeilen × 3 Spalten“ → „dieselbe Rechnung für alle zugleich“ → „4 Schätzungen: 188, 126, 286, 232“. Ein kleiner Punkt (Datenpaket) läuft durch die Kästen. Nur Zahlen aus Kap. 1 (Tabelle 1, Maklerin), keine Formeln.
- **Ablauf:** 1. Wohnung-Kasten erscheint, daneben drei Etiketten „Fläche, Zimmer, Entfernung“ (FadeIn). 2. Zahlen 60, 2, 3 erscheinen, Kasten „Zahlenliste“ wächst darum. 3. Paket wandert durch „Rechnung“ und kommt als „188“ heraus. 4. Untere Zeile: vier Zeilen stapeln sich zur Tabelle. 5. Vier Pakete laufen gleichzeitig durch dieselbe Rechnung, vier Zahlen erscheinen. — Haltepunkte: nach 3 (eine Wohnung → eine Zahl), nach 5 (viele auf einmal).
- **Verständnisproblem:** Leser sieht den roten Faden des Kapitels nicht: Zahlenliste → eine Rechnung → dieselbe Rechnung für viele Dinge.
- **Szenenname:** ml/k1ueberblick
- **Editor-Lücke:** machbar (TextBox, Shift/MoveTo für das Paket)

### Artikel 02 — Vektoren: Daten als Zahlenlisten (Soll 5, vorh. 5; nachher 5)

### V2 [A] Linearkombination und Einheitsvektoren als Pfeile
- **Artikel:** content/ml/01-vektoren-und-matrizen/02-vektoren-daten-als-zahlenlisten.md
- **Stelle:** Linearkombinationen — „Im Bild der Pfeile: Man geht $c_1$-mal die Strecke $\mathbf{v}_1$, dann $c_2$-mal …“ (und „Die Einheitsvektoren“ — „Die einfachsten Vektoren haben eine einzige Komponente 1 …“)
- **Art:** neue Animation (zwei Teilbilder nebeneinander, eine Szene)
- **Was zu sehen ist:** Links Axes x∈[−1,3], y∈[−1,6]: $\mathbf v_1=(1,2)$, $\mathbf v_2=(0,1)$, Rechenbeispiel 1 des Artikels $(1,2)+3(0,1)=(1,5)$. Rechts Axes x∈[−1,4], y∈[−1,3]: $\mathbf e_1=(1,0)$ rot, $\mathbf e_2=(0,1)$ grün, $\mathbf x=(3,2)$ (Wohnung 4: Zimmer, km) aus Abb. 3. Beschriftungen $c_1\mathbf v_1$, $3\mathbf v_2$, $\mathbf x=3\mathbf e_1+2\mathbf e_2$.
- **Ablauf:** Links: 1. $\mathbf v_1$ wächst vom Nullpunkt (Create). 2. $\mathbf v_2$ erscheint am Nullpunkt, wird per Scale auf das Dreifache gestreckt. 3. $3\mathbf v_2$ wandert (Shift) an die Spitze von $\mathbf v_1$. 4. Ergebnispfeil $(1,5)$ vom Nullpunkt (Create). Rechts: 5. $\mathbf e_1$, $\mathbf e_2$ erscheinen. 6. $\mathbf e_1$ wird dreifach hintereinander gelegt (drei Kopien erscheinen nacheinander) bis $(3,0)$. 7. Zweimal $\mathbf e_2$ hängt sich an, Spitze bei $(3,2)$, Zielpfeil $\mathbf x$ erscheint; Etikett „Koeffizienten = Komponenten“. — Haltepunkte: 3 (Hintereinanderlegen), 7 (Treppe aus Einheitspfeilen).
- **Verständnisproblem:** Linearkombination und Einheitsvektor sind ohne Bild nur Formeln; dass die Komponenten die Koeffizienten sind, sieht man erst an der Treppe aus Einheitspfeilen.
- **Szenenname:** ml/k1lincomb
- **Editor-Lücke:** machbar (LabeledArrow, Scale, Shift, FadeIn)

### Artikel 03 — Das Skalarprodukt (Soll 3, vorh. 6; nachher 4)
Keine neuen Vorschläge: Skalarprodukt, gewichtete Summe, Summe/Mittelwert und Mustervergleich haben alle schon ein Bild. Es entfallen zwei Doppelungen (siehe „Vorhandene Abbildungen“): k1rmuster geht in k1muster auf, k1rstrom in k1rmittel. Vier statt drei (+1), weil vier verschiedene Rechenbeispiele je ein Rechenbild verlangen (rskp, rgewicht, rmittel+rstrom, muster+rmuster).

### Artikel 04 — Normen (Soll 4, vorh. 6; nachher 5)

### V3 [A] Drei Längen desselben Pfeils: Luftlinie, Taxi-Weg, größte Komponente
- **Artikel:** content/ml/01-vektoren-und-matrizen/04-normen-die-groe-eines-vektors.md
- **Stelle:** Die euklidische Norm — „Die naheliegende Größe eines Pfeils ist seine Länge. In der Ebene liefert sie der Satz des Pythagoras …“ (zugleich Betragssummennorm: „In einer Stadt mit rechtwinkligem Straßennetz …“ und Maximumnorm: „Bei einer Qualitätsprüfung …“)
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x∈[−5,5], y∈[−5,1], Gitter. Pfeil $\mathbf x=(3,-4)^{\top}$ vom Nullpunkt (Spitze markiert). Pythagoras-Dreieck: waagerechte Kathete 3 auf der x-Achse, senkrechte Kathete 4 abwärts, Hypotenuse = Pfeil, Etikett „5 = √(3²+4²)“. Taxi-Weg orange über die Katheten, Etikett „3 + 4 = 7“. Quadrat |x₁|,|x₂| ≤ 4 gestrichelt grün, Etikett „größte Komponente 4“.
- **Ablauf:** 1. Achsen, Pfeil wächst (Create). 2. Katheten erscheinen nacheinander, rechter Winkel markiert, Etikett 5. 3. Ein Taxi-Punkt fährt (MoveAlongPath) erst 3 nach rechts, dann 4 nach unten; die Wegstrecke färbt sich, Etikett 7. 4. Das Quadrat wächst aus dem Nullpunkt (Scale) bis die Spitze auf seinem Rand liegt, Etikett 4. 5. Alle drei Längen stehen als Zeile „5 ≤ 7, 4 ≤ 5“ darunter. — Haltepunkte: 2, 3, 5.
- **Verständnisproblem:** Drei Normen werden nur als Formeln eingeführt; das gemeinsame Objekt (derselbe Pfeil) und der Unterschied der drei Maße fehlt als Bild. Zugleich Vorbereitung der Einheitskugeln (Abb. 14).
- **Szenenname:** ml/k1normen3
- **Editor-Lücke:** machbar (LabeledArrow, MoveAlongPath, Scale)

### Artikel 05 — Abstände und Einheiten (Soll 4, vorh. 4; nachher 5)

### V4 [A] Standardisieren: Mittelwert abziehen, durch Standardabweichung teilen
- **Artikel:** content/ml/01-vektoren-und-matrizen/05-abstande-und-einheiten.md
- **Stelle:** Standardisieren — „Jetzt lässt sich jedes Merkmal in seiner eigenen typischen Schwankung messen …“ (Rechenbeispiel 1, Wohnungsdatensatz)
- **Art:** neue Animation
- **Was zu sehen ist:** Drei übereinanderliegende Zahlenstrahlen für die Flächenspalte $(60,40,90,70)$. Strahl 1 „Fläche in m²“, Bereich 30…100, vier Punkte W1…W4, Mittelwert-Marker bei 65. Strahl 2 „zentriert“, Bereich −30…30, Punkte −5, −25, 25, 5. Strahl 3 „standardisiert“, Bereich −2…2, Punkte −0,28; −1,39; 1,39; 0,28, Klammer „1 Standardabweichung = 18,03 m²“ als Einheitsmaß ±1.
- **Ablauf:** 1. Strahl 1 mit Punkten, Mittelwert-Marker 65 erscheint. 2. Abweichungs-Klammern von 65 zu jedem Punkt (−5, −25, +25, +5). 3. Punkte wandern per MoveTo auf Strahl 2; der Mittelwert liegt nun bei 0. 4. Das Maß „18,03“ wird als Strecke auf Strahl 2 abgetragen. 5. Punkte wandern auf Strahl 3 (Stauchung durch 18,03), Zahlen −0,28 … erscheinen. 6. Gegenprobe: dieselbe Spalte in Einheiten von 10 m² (6, 4, 9, 7) durchläuft dieselben Schritte und endet bei denselben Punkten (zweiter Satz Punkte deckt sich, Mark Haken). — Haltepunkte: 3, 5, 6.
- **Verständnisproblem:** Was „Zentrieren“ und „durch std teilen“ mit den Werten anschaulich macht (erst verschieben, dann stauchen) und warum die Einheit herausfällt (Satz 4.5), sieht man in den Formeln nicht.
- **Szenenname:** ml/k1standard
- **Editor-Lücke:** machbar (NumberLine, Dot, Brace, MoveTo)

### Artikel 06 — Winkel und Ähnlichkeit (Soll 4, vorh. 5; nachher 5)

### V5 [A] Winkel dreht sich: Vorzeichen des Skalarprodukts (spitz, recht, stumpf)
- **Artikel:** content/ml/01-vektoren-und-matrizen/06-winkel-und-ahnlichkeit.md
- **Stelle:** Der Winkel zwischen zwei Vektoren — „Zwei Pfeile, die vom Nullpunkt ausgehen, schließen einen Winkel ein …“ (und Orthogonale Vektoren — „Steht das Skalarprodukt zweier Vektoren auf null …“)
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x,y∈[−3,3]. Feststehender Pfeil $\mathbf u=(2,0)^{\top}$, drehender Pfeil $\mathbf v$ der Länge 2 um den Nullpunkt, Winkelbogen mit Etikett φ, daneben die Zeile „$\mathbf u^{\top}\mathbf v=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\varphi$“ mit Werten an den Haltepunkten: 0°: 4; 45°: 2,83; 90°: 0 (rechter Winkel markiert, Etikett „orthogonal“); 135°: −2,83; 180°: −4. Hintergrund färbt: spitz = grün, stumpf = orange.
- **Ablauf:** 1. $\mathbf u$ und $\mathbf v$ liegen aufeinander (φ=0°), Wert 4 = Produkt der Längen (Cauchy-Schwarz-Gleichheit). 2. $\mathbf v$ dreht (Rotate um den Nullpunkt) auf 45°, Wert erscheint. 3. Weiter auf 90°, Wert 0, Rechtwinkel-Zeichen. 4. Weiter auf 135°, Wert negativ. 5. Auf 180°, Wert −4, Gleichheit mit umgekehrtem Vorzeichen. — Haltepunkte: 0°, 90°, 180°.
- **Verständnisproblem:** Der Winkelbegriff steht nur als Formel (5.2) und im Beispiel (1,0,1)/(1,1,0) im Raum; nirgends sieht man, wie Winkel, Vorzeichen und Betrag des Skalarprodukts zusammenhängen und wo Cauchy-Schwarz scharf ist.
- **Szenenname:** ml/k1winkeldreh
- **Editor-Lücke:** machbar (Rotate um Ursprung, FadeIn der Werte; stufenlos mitlaufende Zahl bräuchte L3)

### Artikel 07 — Matrizen und die Datenmatrix (Soll 2, vorh. 1; nachher 2)

### V6 [A] Matrix als Zahlentabelle: Zeile, Spalte, Eintrag, Format; Bild als Matrix
- **Artikel:** content/ml/01-vektoren-und-matrizen/07-matrizen-und-die-datenmatrix.md
- **Stelle:** Matrizen — „Die Tabelle der Wohnungen ist mehr als vier einzelne Vektoren …“ / Rechenbeispiel „Die Matrix A = (1 2 3; 4 5 6) hat das Format 2×3 …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links Table 2×3 mit den Einträgen 1 2 3 / 4 5 6, Brace „2 Zeilen“, Brace „3 Spalten“, Etikett „Format 2×3“. Markierungen: $a_{12}=2$ (orange Rechteck), $a_{21}=4$ (blau), zweite Spalte $\mathbf a_2=(2,5)^{\top}$ (grün). Rechts 3×3-Raster aus Quadraten (Graustufenbild, helles Kreuz): Pixel hell/dunkel, daneben dieselbe Matrix (0 1 0 / 1 1 1 / 0 1 0).
- **Ablauf:** 1. Tabelle erscheint, Braces für Zeilen und Spalten, Format 2×3. 2. Der Eintrag $a_{12}$ leuchtet auf, Zeilenindex zuerst, dann Spaltenindex (Indicate); dann $a_{21}$. 3. Die zweite Spalte wird umrahmt und als Vektor $\mathbf a_2$ herausgezogen (Shift). 4. Rechts: 9 Pixel erscheinen grau, darunter kommen die Zahlen 0/1 und schalten das Raster hell/dunkel. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Index-Reihenfolge (zuerst Zeile, dann Spalte) und das Lesen von Format $m\times n$; dass eine Matrix auch ein Bild sein kann (Pixel = Einträge).
- **Szenenname:** ml/k1matrix
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Table-Zellen einzeln betonen); mit übergelegten Rechtecken machbar

### Artikel 08 — Das Matrix-Vektor-Produkt (Soll 2, vorh. 4; nachher 3)

### V7 [A] Spaltensicht und Spaltenraum (ersetzt k1zeilenspalten)
- **Artikel:** content/ml/01-vektoren-und-matrizen/08-das-matrix-vektor-produkt.md
- **Stelle:** Der Spaltenraum — „Lässt man $\mathbf{x}$ alle Vektoren des $\mathbb{R}^n$ durchlaufen, so durchläuft $\mathbf{A}\mathbf{x}$ …“ (zugleich Spaltensicht: „Man kann dieselbe Summe auch anders ordnen …“)
- **Art:** neue Animation, ersetzt die statische k1zeilenspalten (zusammengelegt)
- **Was zu sehen ist:** Zwei Axes nebeneinander. Links x∈[−1,6], y∈[−1,4]: $\mathbf A=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, Spalten $\mathbf a_1=(2,1)$ rot, $\mathbf a_2=(1,1)$ grün, $\mathbf x=(2,1)^{\top}$: $2\mathbf a_1=(4,2)$, daran $\mathbf a_2$, Ergebnis $\mathbf A\mathbf x=(5,3)$. Rechts x∈[−2,6], y∈[−2,7]: $\begin{pmatrix}1&2\\2&4\end{pmatrix}$, Spalten $(1,2)$ und $(2,4)$ auf einer Geraden; viele Punkte $c_1\mathbf a_1+c_2\mathbf a_2$ füllen nur die Gerade durch den Nullpunkt; Prüfpunkte $(3,6)$ (Haken, liegt darin) und $(1,1)$ (Kreuz, liegt nicht darin).
- **Ablauf:** Links: 1. $\mathbf a_1,\mathbf a_2$ erscheinen. 2. $\mathbf a_1$ wird auf das Doppelte gestreckt (Scale). 3. $\mathbf a_2$ hängt sich an die Spitze, Ergebnis (5,3). Rechts: 4. Beide Spalten liegen auf einer Linie. 5. Punkt für Punkt erscheinen Kombinationen (PointCloud) und füllen nur die Gerade. 6. $(3,6)$ erhält Haken, $(1,1)$ Kreuz. — Haltepunkte: 3, 5.
- **Verständnisproblem:** Zwei Sichten auf dasselbe Produkt, und dass die Spalten bestimmen, welche Ergebnisse überhaupt erreichbar sind (Spaltenraum), ist reiner Text.
- **Szenenname:** ml/k1spaltenraum
- **Editor-Lücke:** machbar (LabeledArrow, Scale, Shift, PointCloud, Mark)

### Artikel 09 — Lineare Abbildungen (Soll 3, vorh. 1; nachher 3)

### V8 [A] Linearität: Summe und Vielfaches bleiben erhalten
- **Artikel:** content/ml/01-vektoren-und-matrizen/09-lineare-abbildungen.md
- **Stelle:** Lineare Abbildungen — „Das Matrix-Vektor-Produkt hat zwei besondere Eigenschaften …“ / Definition 8.1
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Axes (Eingang links x∈[−1,4], y∈[−2,3]; Ausgang rechts x∈[−1,4], y∈[−1,7]), Pfeil dazwischen „f“. Beispiel des Artikels $f(\mathbf x)=(x_1+x_2,\ 2x_1)^{\top}$ mit $\mathbf u=(1,1)$, $\mathbf v=(2,-1)$: $\mathbf u+\mathbf v=(3,0)$; $f(\mathbf u)=(2,2)$, $f(\mathbf v)=(1,4)$, $f(\mathbf u)+f(\mathbf v)=(3,6)=f(\mathbf u+\mathbf v)$. Dazu $2\mathbf u=(2,2)$ und $f(2\mathbf u)=(4,4)=2f(\mathbf u)$.
- **Ablauf:** 1. Links $\mathbf u$ und $\mathbf v$, dann $\mathbf v$ an die Spitze von $\mathbf u$, Summe $(3,0)$. 2. Rechts $f(\mathbf u)$ und $f(\mathbf v)$ erscheinen, $f(\mathbf v)$ hängt sich an $f(\mathbf u)$. 3. Der Summenpfeil links wird in den Ausgang abgebildet: $f(\mathbf u+\mathbf v)$ landet in derselben Spitze (6/3), Haken „gleich“. 4. Zweite Runde: $2\mathbf u$ links, $f(2\mathbf u)$ rechts als Doppeltes von $f(\mathbf u)$. — Haltepunkte: 3, 4.
- **Verständnisproblem:** „Linear“ ist nur eine Formel (8.1); dass es egal ist, ob man vor oder nach dem Abbilden addiert, sieht man erst, wenn beide Wege auf denselben Punkt führen.
- **Szenenname:** ml/k1linear
- **Editor-Lücke:** machbar (Bildkoordinaten fest eingetragen, Shift/MoveTo/Create)

### V9 [B] Affine Abbildung: erst verformen, dann um $\mathbf b$ verschieben
- **Artikel:** content/ml/01-vektoren-und-matrizen/09-lineare-abbildungen.md
- **Stelle:** Affine Abbildungen — „Für $\mathbf{b}\ne\mathbf{0}$ ist eine affine Abbildung nicht linear …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x∈[−1,6], y∈[−1,5]. Einheitsquadrat, Scherung $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ (aus Abb. 32) liefert das Parallelogramm $(0,0),(1,0),(2,1),(1,1)$; dann Verschiebung um $\mathbf b=(2,1)^{\top}$; der Nullpunkt-Marker wandert von $(0,0)$ nach $(2,1)$, Etikett „$f(\mathbf 0)=\mathbf b$, also nicht linear“.
- **Ablauf:** 1. Quadrat mit Nullpunkt-Marker. 2. Zweite Kopie als Parallelogramm erscheint (Scherung). 3. Gesamtfigur und Marker wandern per Shift um $\mathbf b$, Verschiebungspfeil. — Haltepunkte: 3.
- **Verständnisproblem:** Warum der Achsenabschnitt $b$ eine Abbildung aus der Klasse „linear“ herauswirft (der Nullpunkt bleibt nicht liegen).
- **Szenenname:** ml/k1affin
- **Editor-Lücke:** braucht Editor-Funktion: L5 (Scherung als Gitter-Morph); als zwei Zustände (Quadrat und Parallelogramm, FadeIn) machbar

### Artikel 10 — Das Matrixprodukt (Soll 3, vorh. 4; nachher 4)
Keine neuen Abbildungen. k1rprodukt wird um eine zweite Phase erweitert (Wohnungsdatensatz $\mathbf X\mathbf W$, 4×3 mal 3×2, jeder Eintrag ein Skalarprodukt: 188/756, 126/502, 286/1152, 232/914), weil das Rechenbeispiel „Viele Vektoren auf einmal“ sonst ohne Rechenbild ist (siehe Liste unten). Vier statt drei (+1): vier verschiedene Aussagen (Hintereinanderausführung, Eintrag-Rechnung, Reihenfolge, äußeres Produkt).

### Artikel 11 — Transponierte, Symmetrie, Gram-Matrix (Soll 2, vorh. 1; nachher 3)

### V10 [A] Transponieren: Zeilen werden Spalten, Spiegelung an der Diagonale
- **Artikel:** content/ml/01-vektoren-und-matrizen/11-transponierte-symmetrie-und-gram-matrix.md
- **Stelle:** Die Transponierte — „Aus Unterabschnitt 1.3 ist das Zeichen ⊤ bekannt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Table $\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}$ links, rechts Platz für $\mathbf A^{\top}$ (3×2). Zeile 1 blau, Zeile 2 orange; gestrichelte Hauptdiagonale $a_{11},a_{22}$ durch die Tabelle. Zweites Teilbild darunter: $\mathbf C^{\top}\mathbf C=\begin{pmatrix}10&14\\14&20\end{pmatrix}$ mit den beiden 14 gleich gefärbt und der Diagonale als Spiegelachse (Symmetrie).
- **Ablauf:** 1. Tabelle erscheint, Zeilen eingefärbt. 2. Zeile 1 kippt (Rotate) und legt sich als Spalte 1 rechts ab, danach Zeile 2 als Spalte 2. 3. Eintrag $(1,3)=3$ leuchtet auf und landet in Position $(3,1)$; Format-Etikett $2\times3\to3\times2$. 4. Zweites Teilbild: die zwei 14 leuchten gleichzeitig auf, Spiegelachse erscheint. — Haltepunkte: 2, 4.
- **Verständnisproblem:** Was „Zeile ↔ Spalte vertauschen“ und „$a_{ij}=a_{ji}$“ (Symmetrie) bildlich heißt; Entfernungstabelle als Alltagsbild. Das Zeichen ⊤ wird sonst nur als Regel benutzt.
- **Szenenname:** ml/k1transponiert
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Zellen einzeln betonen) und L2 (Zeile in Spalte umformen); mit Rechtecken und Rotate/Shift machbar

### V11 [B] Gram-Matrix der Beispiele füllt sich Eintrag für Eintrag
- **Artikel:** content/ml/01-vektoren-und-matrizen/11-transponierte-symmetrie-und-gram-matrix.md
- **Stelle:** Die Gram-Matrix der Beispiele — „Wie ähnlich ist jedes Beispiel eines Datensatzes jedem anderen?“
- **Art:** neue Animation
- **Was zu sehen ist:** Links $\mathbf X=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix}$ (drei Texte), rechts ein leeres 3×3-Raster für $\mathbf X\mathbf X^{\top}$. Zeile $i$ und Zeile $k$ von $\mathbf X$ werden markiert, das Produkt $\mathbf x_i^{\top}\mathbf x_k$ erscheint im Eintrag $(i,k)$: Diagonale 13, 52, 10 (Längenquadrate); (1,2)=26, (1,3)=2, (2,3)=4, jeweils zugleich der gespiegelte Eintrag. Schluss: Eintrag (1,2): „26/√(13·52) = 1“.
- **Ablauf:** 1. Raster leer. 2. Diagonalwerte nacheinander. 3. Oberes Dreieck, Spiegelung füllt das untere. 4. Zwei Zeilen von $\mathbf X$ sind Vielfache, Eintrag (1,2) leuchtet: Kosinus 1. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Die Gram-Matrix steht nur als Formel $\mathbf X\mathbf X^{\top}$; dass sie die Tabelle aller paarweisen Skalarprodukte ist und symmetrisch, wird nicht gesehen.
- **Szenenname:** ml/k1grambsp
- **Editor-Lücke:** braucht Editor-Funktion: L7 (Matrix·Matrix als Prozess), L9 (Zellen betonen); mit Rechtecken und FadeIn der Zahlen machbar

### Artikel 12 — Einheitsmatrix und Inverse (Soll 2, vorh. 0; nachher 2)

### V12 [A] Die Inverse macht die Abbildung rückgängig
- **Artikel:** content/ml/01-vektoren-und-matrizen/12-einheitsmatrix-und-inverse.md
- **Stelle:** Die inverse Matrix — „Eine Drehung um 90° macht man rückgängig, indem man um 90° zurückdreht …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x∈[−1,6], y∈[−1,5]. Figur: Dreieck $(0,0),(1,0),(0,2)$ und der Punkt $\mathbf P=(1,2)$. $\mathbf A=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ (Rechenbeispiel des Artikels) bildet $\mathbf P$ auf $(4,3)$ ab, $\mathbf A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$ schickt $(4,3)$ zurück nach $(1,2)$. Zweite Hälfte: $\mathbf I$ lässt die Figur liegen.
- **Ablauf:** 1. Figur und $\mathbf P$. 2. Pfeil „$\mathbf A$“: das Bild aus Dreieck $(0,0),(2,1),(2,2)$ und $\mathbf P'=(4,3)$ erscheinen (zweiter Zustand per FadeIn), $\mathbf P$ wandert (MoveTo) nach $(4,3)$. 3. Pfeil „$\mathbf A^{-1}$“: $\mathbf P'$ wandert zurück nach $(1,2)$. 4. Beschriftung „$\mathbf A^{-1}\mathbf A=\mathbf I$: nichts hat sich geändert“. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Die Inverse und die Einheitsmatrix sind sonst reine Rechenregeln ($\mathbf A\mathbf A^{-1}=\mathbf I$); die Idee „zwei Abbildungen heben sich auf“ braucht das Bild.
- **Szenenname:** ml/k1inverse
- **Editor-Lücke:** braucht Editor-Funktion: L5 (ganze Figur durch Matrix verformen); Punkte und Pfeile per MoveTo/Create machbar

### V13 [A] Singulär: zwei Punkte landen im selben Ziel
- **Artikel:** content/ml/01-vektoren-und-matrizen/12-einheitsmatrix-und-inverse.md
- **Stelle:** Wann es keine Inverse gibt — „Die Matrix diag(1; 0) drückt die Ebene auf die $x_1$-Achse platt …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x∈[−1,3], y∈[−3,6]. Punkte $(1,5)$ und $(1,-2)$ (verschiedene Farben), senkrechte Lote auf die $x_1$-Achse, gemeinsames Ziel $(1,0)$. Das Rechenbeispiel $\begin{pmatrix}1&2\\2&4\end{pmatrix}$ mit $(1,1)$, $(3,0)\mapsto(3,6)$ wird nicht neu gezeichnet, sondern aus hm1/k10kern übernommen (siehe V17 und Hinweis unten).
- **Ablauf:** 1. Beide Punkte erscheinen. 2. Lote wachsen (Create). 3. Beide Punkte fahren per MoveTo auf $(1,0)$ und fallen zusammen; Frage „Welcher Punkt war es?“. — Haltepunkte: 3.
- **Verständnisproblem:** Warum fehlende Eindeutigkeit „keine Inverse“ heißt; ohne Bild bleibt Satz 11.5 eine Folgerung ohne Anschauung.
- **Szenenname:** ml/k1singulaer
- **Editor-Lücke:** machbar (Dot, Line, MoveTo)

Hinweis zu V13: hm1/k10kern (Heft hm1/10, Artikel 05) zeigt dieselbe Matrix $\begin{pmatrix}1&2\\2&4\end{pmatrix}$ mit $P(1,1)=P(3,0)=(3,6)$ und der Kerngeraden. Für das Beispiel dieses Artikels deshalb nur das erste Teilbild neu zeichnen; das zweite Teilbild entfällt zugunsten einer Wiederverwendung von hm1/k10kern (siehe V17).

### Artikel 13 — Lineare Gleichungssysteme (Soll 3, vorh. 1; nachher 3)

### V14 [A] Das Gauß-Verfahren Zeile für Zeile
- **Artikel:** content/ml/01-vektoren-und-matrizen/13-lineare-gleichungssysteme.md
- **Stelle:** Das Gauß-Verfahren — „Zieht man die erste Zeile zweimal von der zweiten und einmal von der dritten ab, so verschwindet $x_1$ aus beiden.“ (Rechenbeispiel zur erweiterten Koeffizientenmatrix)
- **Art:** neue Animation
- **Was zu sehen ist:** Erweiterte Koeffizientenmatrix $\left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right)$ als Table mit senkrechtem Strich, rechts daneben das System $x_1+2x_2+x_3=8,\dots$ Drei Zustände untereinander: nach $Z_2-2Z_1$, $Z_3-Z_1$ (Spalte 1 unter dem Pivot wird 0); nach Tausch $Z_2\leftrightarrow Z_3$; nach $Z_3-3Z_2$ (Stufenform mit $-1$, $-4$, $-12$). Pivots umrandet, die bereinigten Nullen farbig, Pfeil mit Etikett „$-2\cdot Z_1$“ usw. Unten Rückwärtseinsetzen: $x_3=3$, $x_2=2$, $x_1=1$.
- **Ablauf:** 1. Matrix mit Strich erscheint, Pivot $1$ in Zeile 1 umrandet. 2. Pfeile „$-2Z_1$“ und „$-Z_1$“; neue Zeilen 2 und 3 erscheinen darunter (Zahlen Write). 3. Tausch: die beiden Zeilen wechseln die Plätze (Shift). 4. Pfeil „$-3Z_2$“, dritte Zeile $(0,0,-4\,|\,-12)$. 5. Treppenlinie wird gezogen. 6. Rückwärts: $x_3$, $x_2$, $x_1$ erscheinen unten nacheinander und werden in die Gleichungen eingesetzt (Haken). — Haltepunkte: 2, 4, 6.
- **Verständnisproblem:** Das Verfahren ist reine Zahlenfolge; man sieht nicht, welche Zeile von welcher abgezogen wird und warum am Ende eine Treppe steht. hm1/k10gauss zeigt nur die Geometrie eines 2×2-Systems (Geraden drehen sich um den Lösungspunkt), nicht diese Zahlen und nicht das Rückwärtseinsetzen; kein Ersatz.
- **Szenenname:** ml/k1gauss
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Zeilen/Zellen einzeln betonen) und L2 (Zeile in neue Zeile umformen); mit Table-Zuständen untereinander und FadeIn/Write machbar

### V15 [B] Überbestimmt: die Preise liegen nicht im Spaltenraum (3D)
- **Artikel:** content/ml/01-vektoren-und-matrizen/13-lineare-gleichungssysteme.md
- **Stelle:** Mehr Gleichungen als Unbekannte — „Ein überbestimmtes System hat meist keine Lösung …“ / Rechenbeispiel „Für die Wohnungen 1 bis 3 mit den Preisen 200, 130 und 290 …“
- **Art:** neue Animation
- **Was zu sehen ist:** 3D-Achsen (Preis Wohnung 1, 2, 3; je 0…320). Spaltenraum als Ebene durch den Nullpunkt, aufgespannt von $\mathbf a_1=(60,40,90)$ und $\mathbf a_2=(2,1,4)$, als Fläche $z=3{,}5x-3y$ (liegt exakt auf beiden Spalten). Rechte Seite $\mathbf y=(200,130,290)$ als Pfeil, Spitze liegt $20$ unterhalb der Ebene (Ebene hat dort $z=310$). Kleiner Punkt auf der Ebene bei $(200,130,310)$ = Vorhersage mit $w_1=3$, $w_2=10$, gestrichelte Strecke $20$ zwischen beiden, Etikett „Vorhersage 310 statt 290“.
- **Ablauf:** 1. Achsen, $\mathbf a_1$, $\mathbf a_2$ erscheinen. 2. Ebene füllt sich (Create der Fläche). 3. $\mathbf y$ erscheint und liegt nicht auf der Ebene. 4. Der Punkt $3\mathbf a_1+10\mathbf a_2=(200,130,310)$ erscheint, die 20-Lücke wird markiert. — Haltepunkte: 3, 4.
- **Verständnisproblem:** „Keine Lösung“ im Spaltenbild bleibt abstrakt, solange man nicht sieht, dass die rechte Seite neben der aufgespannten Ebene liegt. Vorbereitung auf Ausgleichsrechnung.
- **Szenenname:** ml/k1ueberbest
- **Editor-Lücke:** machbar (FunctionGraph als Fläche in 3D, Vector 3D; Kamera-Drehung wäre hilfreich: L4)

### Artikel 14 — Unabhängigkeit, Basis und Rang (Soll 4, vorh. 1; nachher 4)

### V16 [A] Basis: ein schiefes Koordinatennetz mit eindeutiger Adresse
- **Artikel:** content/ml/01-vektoren-und-matrizen/14-unabhangigkeit-basis-und-rang.md
- **Stelle:** Basis und Dimension — „Will man einen Spann so knapp wie möglich beschreiben …“ / Rechenbeispiel „$(1,0)^{\top}$ und $(1,1)^{\top}$ bilden eine Basis des $\mathbb{R}^2$ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x∈[−1,5], y∈[−1,4]. Basisvektoren $\mathbf b_1=(1,0)$ (rot) und $\mathbf b_2=(1,1)$ (grün), schiefes Gitter aus Parallelen zu beiden, Punkt $\mathbf x=(3,2)$ (derselbe Vektor wie in Abb. 3). Weg: einmal $\mathbf b_1$, dann zweimal $\mathbf b_2$; Etikett „Koordinaten $(1,2)$“ und „$(3,2)=1\cdot\mathbf b_1+2\cdot\mathbf b_2$“. Zweites Teilbild: zwei abhängige Vektoren $(1,2)$, $(2,4)$ — viele Wege zum selben Punkt (nicht eindeutig) bzw. Punkt $(1,1)$ nicht erreichbar.
- **Ablauf:** 1. $\mathbf b_1,\mathbf b_2$ erscheinen, schiefes Gitter zeichnet sich (Create der Linien). 2. Punkt $(3,2)$ erscheint. 3. Weg: $\mathbf b_1$ (1×), dann $\mathbf b_2$ (2×) zum Punkt (MoveAlongPath/Shift). 4. Standardgitter zum Vergleich; dieselbe Stelle, andere Adresse. 5. Zweites Teilbild mit zwei Wegen zum selben Punkt bei abhängigen Vektoren. — Haltepunkte: 3, 5.
- **Verständnisproblem:** Basis als „Adresse, die jeder Punkt genau einmal hat“ (Satz 13.4); ohne Bild bleibt nur die Formel. Doppelung: hm1/k9basis zeigt dasselbe Prinzip mit anderen Vektoren ($(5,0)=2\vec a-\vec b$); wenn der Text des ml-Artikels nicht geändert werden soll, eigene Szene mit den Zahlen oben, sonst hm1/k9basis wiederverwenden.
- **Szenenname:** ml/k1basis
- **Editor-Lücke:** machbar (Line, LabeledArrow, MoveAlongPath)

### V17 [A] Kern und Rangsatz: eine Richtung geht verloren (Wiederverwendung)
- **Artikel:** content/ml/01-vektoren-und-matrizen/14-unabhangigkeit-basis-und-rang.md
- **Stelle:** Der Kern und der Rangsatz — „Eine Matrix mit $n$ Spalten nimmt Vektoren aus $n$ Richtungen entgegen …“ (Rechenbeispiel $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, Kern $\operatorname{span}\{(2,-1)\}$)
- **Art:** vorhandene Szene wiederverwenden: hm1/k10kern (Heft hm1/10, Artikel 05), dort als Animation aufbauen
- **Was zu sehen ist:** Links Ebene der Eingänge mit der Kerngeraden (rot) und zwei Parallelen dazu, rechts die Bildgerade $y=2x$; drei Punkte $(1,1)$, $(3,0)$, $(-1,2)$ fallen alle auf $(3,6)$. Beschriftung „Kern: 1 Richtung, Bild: 1 Richtung, $1+1=2$“.
- **Ablauf:** 1. Kerngerade und Parallelen zeichnen sich (Create). 2. Die drei Punkte wandern (MoveTo) nach rechts auf denselben Punkt. 3. Beschriftung mit Rangsatz. — Haltepunkte: 2.
- **Verständnisproblem:** Der Rangsatz $\dim\ker+\operatorname{rang}=n$ als Bilanz „was geht verloren, was bleibt“.
- **Szenenname:** hm1/k10kern (Verweis; falls die Beschriftung angepasst werden muss: ml/k1kern)
- **Editor-Lücke:** machbar

### V18 [B] Abhängige Merkmale: zwei Gewichte, dieselbe Vorhersage
- **Artikel:** content/ml/01-vektoren-und-matrizen/14-unabhangigkeit-basis-und-rang.md
- **Stelle:** Abhängige Merkmale — Rechenbeispiel „Erdgeschoss, Obergeschoss, Gesamtfläche“ („Die Gewichte sind nicht eindeutig.“)
- **Art:** neue Animation (Rechenbild, zwei Skalarprodukte)
- **Was zu sehen ist:** Haus 1: $\mathbf x_1=(50,40,90)$. Zwei Skalarprodukte nebeneinander: $\mathbf w=(3,3,0)$: $150+120+0=270$ und $\mathbf w'=(0,0,3)$: $0+0+270=270$. Darunter $\mathbf w-\mathbf w'=(3,3,-3)=3\mathbf k$ mit $\mathbf k=(1,1,-1)$ und $\mathbf x_1^{\top}\mathbf k=50+40-90=0$.
- **Ablauf:** 1. Haus-Zeile erscheint. 2. Linkes Skalarprodukt rechnet Summand für Summand, Ergebnis 270. 3. Rechtes rechnet, Ergebnis 270, beide Ergebnisse leuchten gleich. 4. Unterschied der Gewichte als Kernvektor, Kontrolle 0. — Haltepunkte: 3.
- **Verständnisproblem:** Warum man aus den Vorhersagen nicht auf die Gewichte zurückschließen kann.
- **Szenenname:** ml/k1abhmerkmal
- **Editor-Lücke:** machbar (Skalarprodukt-Operation, show_terms)

### Artikel 15 — Die Determinante (Soll 3, vorh. 2; nachher 4)

### V19 [A] Das Vorzeichen: spiegelt die Abbildung?
- **Artikel:** content/ml/01-vektoren-und-matrizen/15-die-determinante.md
- **Stelle:** Das Vorzeichen der Determinante — „Eine Fläche ist nie negativ, die Determinante kann es sein.“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Axes nebeneinander (x,y∈[−1,4]). Links $\begin{pmatrix}3&1\\1&2\end{pmatrix}$: $\mathbf a_1=(3,1)$, $\mathbf a_2=(1,2)$ liegt gegen den Uhrzeigersinn von $\mathbf a_1$, Drehpfeil von $\mathbf a_1$ nach $\mathbf a_2$, $\det=5>0$. Rechts Spalten vertauscht, $\begin{pmatrix}1&3\\2&1\end{pmatrix}$: $\mathbf a_1=(1,2)$, $\mathbf a_2=(3,1)$ liegt im Uhrzeigersinn, $\det=1-6=-5<0$, gleiche Fläche, Orientierung umgekehrt. Dazu Einheitsquadrat mit $\mathbf e_1,\mathbf e_2$ (gegen den Uhrzeigersinn) als Referenz.
- **Ablauf:** 1. Referenz $\mathbf e_1\to\mathbf e_2$ mit Drehpfeil. 2. Links Parallelogramm, Drehpfeil gleichsinnig, Wert +5. 3. Rechts dasselbe Parallelogramm aus vertauschten Spalten, Drehpfeil umgekehrt, Wert −5. 4. Spiegelung $\operatorname{diag}(1;-1)$: $\mathbf e_2$ klappt nach unten. — Haltepunkte: 3.
- **Verständnisproblem:** Was ein negativer Flächenfaktor bedeutet; sonst nur als Vorzeichenregel gelernt.
- **Szenenname:** ml/k1detvorz
- **Editor-Lücke:** machbar (LabeledArrow, Rotate-Pfeil als LoopArrow); Spiegelung als Gitter-Morph wäre L5

### V20 [B] Der Flächenfaktor gilt für jede Figur (Kreis wird Ellipse)
- **Artikel:** content/ml/01-vektoren-und-matrizen/15-die-determinante.md
- **Stelle:** Der Flächenfaktor gilt für jede Figur — „Bisher ging es um das Einheitsquadrat …“ / Rechenbeispiel „Der Kreis mit dem Radius 1 hat die Fläche $\pi$ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x,y∈[−4,4]. Einheitskreis (Fläche $\pi$) und Dreieck $(0,0),(1,0),(0,1)$ (Fläche ½). Streckung $\operatorname{diag}(3;2)$: Ellipse mit Halbachsen 3 und 2, Fläche $6\pi$; Dreieck unter $\begin{pmatrix}3&1\\1&2\end{pmatrix}$: Ecken $(0,0),(3,1),(1,2)$, Fläche $5/2$. Etikett „Faktor $|\det|=6$“ bzw. „$5$“.
- **Ablauf:** 1. Kreis erscheint, Fläche π. 2. Ellipse wächst aus dem Kreis (Scale in x mit 3, in y mit 2), Fläche 6π, Faktor 6. 3. Dreieck und sein Bild mit Faktor 5, Etikett ½ → 5/2. — Haltepunkte: 2.
- **Verständnisproblem:** Der Faktor gilt für beliebige Figuren, nicht nur fürs Quadrat.
- **Szenenname:** ml/k1detflaeche
- **Editor-Lücke:** braucht Editor-Funktion: L5 (Gitter-/Figur-Morph); Ellipse und Dreieck als zweiter Zustand (FadeIn) machbar

### Artikel 16 — Elementweise Rechnen und Tensoren (Soll 2, vorh. 1; nachher 3)

### V21 [A] Einen Vektor von jeder Zeile abziehen: die Datenmatrix zentrieren
- **Artikel:** content/ml/01-vektoren-und-matrizen/16-elementweise-rechnen-und-tensoren.md
- **Stelle:** Einen Vektor zu jeder Zeile addieren — „Um einen ganzen Datensatz zu zentrieren, zieht man von jeder Zeile der Datenmatrix denselben Vektor ab …“ (Rechenbeispiel $\tilde{\mathbf X}=\mathbf X-\mathbf 1\bar{\mathbf x}^{\top}$)
- **Art:** neue Animation
- **Was zu sehen ist:** Links $\mathbf X$ (4×3, Wohnungen), in der Mitte der Zeilenvektor $\bar{\mathbf x}^{\top}=(65;\ 2{,}5;\ 3)$, rechts das Ergebnis $\tilde{\mathbf X}$ mit den Zeilen $(-5,-0{,}5,0)$, $(-25,-1{,}5,-2)$, $(25,1{,}5,3)$, $(5,0{,}5,-1)$.
- **Ablauf:** 1. $\mathbf X$ und $\bar{\mathbf x}^{\top}$ erscheinen. 2. $\bar{\mathbf x}^{\top}$ kopiert sich viermal nach unten (die Matrix $\mathbf 1\bar{\mathbf x}^{\top}$ entsteht, Zeilen nacheinander per FadeIn/Shift). 3. Zeile für Zeile wird abgezogen, das Ergebnis erscheint. 4. Spaltensummen $=0$ als Kontrolle (Haken). — Haltepunkte: 2, 3.
- **Verständnisproblem:** Die Kurzschrift „$\mathbf X-\bar{\mathbf x}^{\top}$“ widerspricht den Formaten; das Bild zeigt, dass der Zeilenvektor zu jeder Zeile gedacht wird.
- **Szenenname:** ml/k1zentrierdaten
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Zeilen betonen) und L7 (elementweise Rechnung als Prozess); mit Table und FadeIn machbar

### V22 [A] Hadamard-Produkt und Skalarprodukt im selben Rechenweg
- **Artikel:** content/ml/01-vektoren-und-matrizen/16-elementweise-rechnen-und-tensoren.md
- **Stelle:** Das Hadamard-Produkt — Rechenbeispiel „$(1,2,3)^{\top}\odot(4,5,6)^{\top}=(4,10,18)^{\top}$, und $4+10+18=32$ ist das Skalarprodukt.“
- **Art:** neue Animation (Skalarprodukt-Rechenbild)
- **Was zu sehen ist:** Skalarprodukt-Operation mit $\mathbf u=(1,2,3)$, $\mathbf v=(4,5,6)$: erst die Produkte $4$, $10$, $18$ als Vektor (das Hadamard-Produkt), dann die Summe $32$. Daneben 2×2: $\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix}$ gegen das Matrixprodukt $\begin{pmatrix}2&1\\4&3\end{pmatrix}$.
- **Ablauf:** 1. Drei Produkte erscheinen nacheinander, bilden den Vektor $(4,10,18)$. 2. Summenzeichen fasst sie zu 32 zusammen. 3. Rechts 2×2: elementweise Produkte gleiche Stelle, danach Matrixprodukt (Zeile mal Spalte) zum Vergleich. — Haltepunkte: 1, 3.
- **Verständnisproblem:** Hadamard-Produkt (Einträge an gleicher Stelle) wird sonst leicht mit dem Matrixprodukt verwechselt; die Verbindung „Summe der Hadamard-Einträge = Skalarprodukt“.
- **Szenenname:** ml/k1hadamard
- **Editor-Lücke:** machbar (Skalarprodukt-Operation, Table)

### Artikel 17 — Das Wichtigste bis hier (Soll 1, vorh. 0; nachher 1)

### V23 [A] Landkarte des Kapitels: Wie die Begriffe auseinander hervorgehen
- **Artikel:** content/ml/01-vektoren-und-matrizen/17-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt aus zwei Rechenarten …“
- **Art:** neue Animation (Zusammenschau; vorhandene Szene V1 `ml/k1ueberblick` kann als erste Stufe wiederverwendet werden)
- **Was zu sehen ist:** Blockbild aus TextBoxen in zwei Zweigen, ausgehend von „Vektoren addieren und vervielfachen“. Zweig 1: „Skalarprodukt“ → „Länge, Abstand, Winkel“ (Pfeil „$\lVert\mathbf x\rVert^2=\mathbf x^{\top}\mathbf x$“). Zweig 2: „Linearkombination“ → „Matrix mal Vektor (Spaltensicht)“ → „lineare Abbildung = Matrix (Spalten = Bilder von $\mathbf e_j$)“ → „Matrixprodukt = Hintereinanderausführung“ → „Inverse, Rang, Kern, Determinante: geht Information verloren?“. Beide Zweige münden in „Datenmatrix $\mathbf X$, Vorhersagen $\mathbf X\mathbf w$“.
- **Ablauf:** 1. Wurzelkasten. 2. Zweig 1 baut sich auf (Kästen und Pfeile nacheinander). 3. Zweig 2 baut sich auf. 4. Beide Zweige laufen in der Datenmatrix zusammen, ein Paket (Wohnung 1, Zahl 188) wandert hindurch. — Haltepunkte: 2, 3.
- **Verständnisproblem:** Zusammenschau: Wie die Begriffe aus den zwei Rechenarten folgen; die Tabelle im Artikel ist Text.
- **Szenenname:** ml/k1landkarte
- **Editor-Lücke:** machbar (TextBox, LabeledArrow, FadeIn, Shift)

<!--VORSCHLAEGE_ENDE-->

## Vorhandene Abbildungen

Format: `- <szene> (<datei>): animieren ja/nein — Schritte | Lücke`. „MathTex-Rechenbild“ = die Szene besteht heute aus einem einzigen statischen MathTex; animiert wird sie mit der Σ-/Skalarprodukt-/Arithmetik-Operation des Editors oder zeilenweise.

**02-vektoren-daten-als-zahlenlisten.md (5 → 5)**
- k1rsumme (02): ja, MathTex-Rechenbild — Schritte: 1. Summe ausschreiben $a_1+a_2+a_3$ 2. Zahlen einsetzen 3. Ergebnis 8 (dann $\sum a_i^2=30$, $\sum j=6$) | machbar (Σ-Operation); Doppelsumme aus k1rdoppel kommt als zweite Hälfte dazu
- k1rdoppel (02): ja, zusammengelegt in k1rsumme — Schritte: 1. Tabelle 2×2 2. Zeilensummen 3, 7 → 10 3. Spaltensummen 4, 6 → 10, beide gleich | L9 (Zellen/Zeilen betonen); entfällt als eigene Szene
- k1punktpfeil (02): ja — 1. Achsen 2. Punkt $(3,2)$ erscheint, Lote auf die Achsen 3. Pfeil wächst vom Nullpunkt (Create), beide Bilder nebeneinander | machbar
- k1addition (02): ja — links 1. $\mathbf u$ 2. $\mathbf v$ am Nullpunkt 3. $\mathbf v$ wandert an die Spitze von $\mathbf u$ (Shift) 4. Summe $(4,3)$ 5. gestrichelter Gegenweg; zusätzlich 6. Differenz $\mathbf u-\mathbf v$ als Pfeil von Spitze zu Spitze; rechts 1. $\mathbf u$ 2. $2\mathbf u$ (Scale) 3. $-\mathbf u$ (Rotate 180°/Scale −1) | machbar
- k1rmittelvektor (02): ja, MathTex-Rechenbild — 1. vier Vektoren untereinander 2. Komponentensummen 260, 10, 12 3. Division durch 4 → $(65;2{,}5;3)$ | L7 (spaltenweise Σ als Prozess); mit Table-Zuständen machbar

**03-das-skalarprodukt.md (6 → 4)**
- k1rskp (03): ja, schon Operation (DotProduct, zwei Rechnungen) — 1. Zeile trifft Spalte 2. $1\cdot4$, $2\cdot(-1)$, $3\cdot2$ nacheinander 3. Summe 8; zweite Rechnung $\mathbf u^{\top}\mathbf u=14$ | machbar
- k1rgewicht (03): ja, MathTex-Rechenbild → durch DotProduct ersetzen — $\mathbf w=(3,10,-4)$, $\mathbf x_1=(60,2,3)$: Beiträge 180, 20, −12, Summe 188 | machbar
- k1rmittel (03): ja, zusammengelegt in k1rstrom (gleiches $\mathbf u=(200,250,300)$): $\mathbf 1^{\top}\mathbf u=750$, Mittel 250, $\mathbf e_2^{\top}\mathbf u=250$ als erste Rechnung der Szene | machbar; entfällt als eigene Szene
- k1rstrom (03): ja, schon Operation (DotProduct) — $\mathbf p=(0{,}32;0{,}34;0{,}28)$, Produkte 64, 85, 84, Summe 233 | machbar
- k1muster (03): ja — 1. Muster $\mathbf w$ (Stems) 2. Signal $\mathbf x$ 3. Produkte $w_jx_j$ erscheinen von links nach rechts 4. Summe 8; dasselbe für $\mathbf x'$ mit Summe 0 | machbar (Stem, Axes)
- k1rmuster (03): ja, zusammengelegt in k1muster, zweite Phase: Wechselmuster gegen Gleichmuster $\mathbf 1$ (8/0 und 2/10) | machbar; entfällt als eigene Szene

**04-normen-die-groe-eines-vektors.md (6 → 5)**
- k1rl2 (04): ja, MathTex-Rechenbild — 1. Quadrate 9, 16 2. Summe 25 3. Wurzel 5; zusätzlich $(1,2,2)\to3$ | machbar (Arithmetik); wird um k1rl1 und k1rlp erweitert (eine Szene „Normen von $(3,-4)$“: $p=1,2,3,10$ nacheinander)
- k1rl1 (04): ja, zusammengelegt in k1rl2 — $|3|+|-4|=7$, $1+2+2=5$ | machbar; entfällt als eigene Szene (Anschauung liefert V3)
- k1rlp (04): ja, zusammengelegt in k1rl2 — $p=3$: $27+64=91$, $91^{1/3}\approx4{,}498$; $p=10$: $1\,107\,625^{1/10}\approx4{,}022$ | machbar; entfällt als eigene Szene
- k1einheitskugeln (04): ja — 1. Raute ($p=1$) wächst 2. Kreis ($p=2$) 3. Quadrat ($p=\infty$); dazwischen $p=1{,}5$; $p=4$ als CurveFamily-Glieder | machbar (CurveFamily mit Grenzkurve); stetiges Wandern mit $p$ bräuchte L3
- k1rfehler (04): ja, MathTex-Rechenbild — Gutachter A: Quadrate $100\times4=400$, Wurzel 20; Gutachter B: $0,0,0,1600$, Wurzel 40 | machbar (Σ-Operation)
- k1rrms (04): ja, MathTex-Rechenbild — 1. Sinus mit vier Abtastpunkten 2. Quadrate $0,1,0,1$ 3. Summe 2, durch 4 → 0,5, Wurzel 0,707 | machbar

**05-abstande-und-einheiten.md (4 → 5)**
- k1rabstand (05): ja, MathTex-Rechenbild — 1. Differenz $(20,1,2)$ 2. Quadrate $400+1+4=405$ 3. Wurzel $\approx20{,}12$ | machbar
- k1einheiten (05): ja — 1. links: A, B, C und Kreis um A durch B, B näher 2. Achse wird auf $1/10$ gestaucht, Punkte wandern per MoveTo nach rechts 3. rechts: neuer Kreis um A durch C, jetzt C näher | machbar mit zwei Teilbildern; echte Achsenstauchung = L5/L3
- k1rzentriert (05): ja, MathTex-Rechenbild — Mittelwert 65, Abweichungen $-5,-25,25,5$, Summe 0 | machbar (Σ)
- k1rstd (05): ja, MathTex-Rechenbild — Quadrate 25, 625, 625, 25; Summe 1300; durch 4 → 325; Wurzel 18,03 | machbar

**06-winkel-und-ahnlichkeit.md (5 → 5)**
- k1rwinkel (06): ja, MathTex-Rechenbild — Zähler $1\cdot1+0\cdot1+1\cdot0=1$ (DotProduct), Nenner $\sqrt2\cdot\sqrt2=2$, $\cos\varphi=\tfrac12$, $60^\circ$ | machbar
- k1rortho (06): ja, MathTex-Rechenbild — $\mathbf 1^{\top}\mathbf w=0$; $\mathbf x=2\cdot\mathbf 1+\mathbf w=(3,1,3,1)$; $\mathbf 1^{\top}\mathbf x=8$, $\mathbf w^{\top}\mathbf x=4$ (zwei DotProducts) | machbar
- k1rkosinus (06): ja, MathTex-Rechenbild — $\mathbf x_1,\mathbf x_2$: Zähler 30, Längen $\sqrt{13}\sqrt{52}$ → 1; $\mathbf x_1,\mathbf x_3$: $2/\sqrt{130}\approx0{,}175$ | machbar
- k1schatten (06): ja — 1. Achsen, $\mathbf x=(3,1)$ und Gerade in Richtung $\mathbf u=(0{,}6;0{,}8)$ 2. Lichtstrahlen (gestrichelt, senkrecht zur Geraden) fallen auf die Gerade 3. Schattenpunkt $(1{,}56;2{,}08)$ erscheint, Schattenlänge 2,6 4. Rechnung $0{,}6\cdot3+0{,}8\cdot1=2{,}6$ aus k1rschatten als letzter Schritt | machbar (Line, MoveAlongPath)
- k1rschatten (06): ja, zusammengelegt in k1schatten (schon DotProduct mit denselben Zahlen) | machbar; entfällt als eigene Szene

**07-matrizen-und-die-datenmatrix.md (1 → 2)**
- k1datenmatrix (07): ja — 1. Tabelle 4×3 2. Zeilen werden zu Zeilenvektoren $\mathbf x_i^{\top}$ (Wohnung 2 blau) 3. Spalte der Flächen (orange) 4. Eintrag $x_{21}=40$ liegt in beiden | L9 (Zellen betonen); mit überlegten Rechtecken machbar

**08-das-matrix-vektor-produkt.md (4 → 3)**
- k1rmv (08): ja, MathTex-Rechenbild — Matrix $\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}$ mal $(2,1)$: Zeile 1: $2+2=4$, Zeile 2: $0-1=-1$, Zeile 3: $6+1=7$; danach Spaltensicht $2\mathbf a_1+\mathbf a_2$ | machbar (Σ/Skalarprodukt je Zeile); L7 für den Matrix-Vektor-Prozess als Ganzes
- k1rzeilen (08): ja, MathTex-Rechenbild — vier Zeilen von $\mathbf X$ mal $\mathbf w=(3,10,-4)$: 188, 126, 286, 232 (vier DotProducts nacheinander) | machbar
- k1rspalten (08): ja, zusammengelegt in k1rzeilen (zweite Phase: $3\cdot$Flächenspalte $+10\cdot$Zimmerspalte $-4\cdot$Entfernungsspalte = gleiche Vorhersagen) | L7; entfällt als eigene Szene
- k1zeilenspalten (08): ja, zusammengelegt in V7 (ml/k1spaltenraum), dessen linkes Teilbild genau diese Zahlen zeigt; dort Spaltensicht als Pfeile | machbar; entfällt als eigene Szene (Artikel 13 verweist auf „Abb. 30 rechts“: Verweis auf das Spaltenraum-Bild umstellen)

**09-lineare-abbildungen.md (1 → 3)**
- k1ebene (09): ja — vier Abbildungen nacheinander (Drehung 90°, Streckung $\operatorname{diag}(2;0{,}5)$, Scherung, Plattdrücken): 1. Einheitsquadrat und $\mathbf e_1$ (rot), $\mathbf e_2$ (grün) 2. die Pfeile wandern an die Spalten (MoveTo; Drehung per Rotate um den Nullpunkt) 3. das Quadrat wird zum Parallelogramm (zweiter Zustand per FadeIn) 4. beim Plattdrücken fällt $\mathbf a_2$ auf $\mathbf 0$; zusätzlich Drehung um beliebigen Winkel $\alpha$: $\mathbf e_1$ läuft auf dem Einheitskreis nach $(\cos\alpha,\sin\alpha)$ | braucht L5 (Gitter-Morph), Pfeile und zwei Zustände machbar. Ähnlich: hm1/k10quadrat (Matrix-Spalten als Bilder des Einheitsquadrats)

**10-das-matrixprodukt.md (4 → 4)**
- k1hinter (10): ja — 1. Kästen $\mathbf x\to\mathbf B\to\mathbf A\to\mathbf y$ 2. Paket (kleiner Pfeil) wandert hindurch 3. untere Zeile: $\mathbf x\to\mathbf A\mathbf B\to\mathbf y$, Paket kommt am selben Ziel an | machbar (TextBox, MoveAlongPath)
- k1rprodukt (10): ja, MathTex-Rechenbild — Eintrag $(1,1)$: Zeile 1 $(1,2)$ mal Spalte 1 $(0,1)$ = 2 usw. bis $\begin{pmatrix}2&1\\1&0\end{pmatrix}$; erweitert um $\mathbf X\mathbf W$ (4×3 mal 3×2: 188/756, 126/502, 286/1152, 232/914) | L7 (Matrix·Matrix als Prozess); mit vier DotProducts machbar
- k1reihenfolge (10): ja — 1. Quadrat mit $\mathbf e_1,\mathbf e_2$ 2. oben: erst Drehung, dann Streckung → senkrechtes Rechteck 3. unten: erst Streckung, dann Drehung → waagerechtes Rechteck | braucht L5; Rotate/Scale-Zustände machbar. Ähnlich: hm1/k10produkt
- k1raeusser (10): ja, MathTex-Rechenbild — Spalte 1 von $\mathbf A$ mal Zeile 1 von $\mathbf B$ = $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, Spalte 2 mal Zeile 2 = $\begin{pmatrix}2&0\\1&0\end{pmatrix}$, Summe $\begin{pmatrix}2&1\\1&0\end{pmatrix}$ | L9, L7

**11-transponierte-symmetrie-und-gram-matrix.md (1 → 3)**
- k1rgrammerk (11): ja, MathTex-Rechenbild — Spalte „Tor“ $(3,6,0)$ mal sich 45, mal „Ball“ $(2,4,1)$ 30, mal „Wahl“ $(0,0,3)$ 0 (DotProduct ×3) | machbar

**13-lineare-gleichungssysteme.md (1 → 3)**
- k1lgs (13): ja — drei Teilbilder (a) (b) (c): 1. Gerade $2x_1+x_2=5$ zeichnet sich (Create) 2. zweite Gerade $x_1+x_2=3$ 3. Schnittpunkt $(2,1)$ erscheint (a); parallele Geraden ohne Schnittpunkt (b); zweite Gleichung liegt auf der ersten (c) | machbar; stetig wanderndes „Schieberegler“-Beispiel (rechte Seite verschieben) wäre L3

**14-unabhangigkeit-basis-und-rang.md (1 → 4)**
- k1spann (14): ja — (a) 1. Vektor $\mathbf v=(1,2)$ 2. Gerade durch den Nullpunkt wächst in beide Richtungen (b) 3. zweiter Vektor liegt schon auf der Geraden, nichts Neues (c) 4. zwei Vektoren in verschiedenen Richtungen, das Band füllt die Ebene | machbar (Create, Band, FadeIn). Ähnlich: hm1/k8span

**15-die-determinante.md (2 → 4)**
- k1det (15): ja — 1. Einheitsquadrat, Fläche 1 2. $\mathbf a_1=(3,1)$ und $\mathbf a_2=(1,2)$ wachsen, Parallelogramm erscheint 3. umschließendes Rechteck $4\times3$ gestrichelt 4. Dreiecke und Rechtecke werden abgezogen: $12-3-2-2=5$ | L5 (Quadrat → Parallelogramm als Gitter-Morph); als zwei Zustände machbar
- k1rlaplace (15): ja, MathTex-Rechenbild — Eintrag 1 mal $\det\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)=1$, Eintrag 2 mal $\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ mit Minus, Eintrag 1 mal $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$; Summe $1-6+1=-4$; jeweils Zeile 1 und Spalte $j$ durchgestrichen | L9 (Zeile/Spalte streichen als Betonen)

**16-elementweise-rechnen-und-tensoren.md (1 → 3)**
- k1tensor (16): ja — 1. Skalar (eine Zahl) 2. Vektor (4 Kästchen reihen sich) 3. Matrix $4\times4$ (Zeilen stapeln sich) 4. Farbbild: drei Kanäle Rot, Grün, Blau liegen hintereinander 5. Stapel aus $N$ Bildern; mit jedem Schritt wächst die Zahl der Achsen um eins | machbar (TextBox, Shift, FadeIn)

Hinweis zu k1ebene, k1reihenfolge, k1det, k1einheiten: In allen vier Szenen ist die Idee „die ganze Ebene wird durch eine Matrix verformt“. Ein Editor-Werkzeug L5 (Gitter-Morph, Matrix wählbar) würde zugleich V9, V12, V19, V20 und diese vier vorhandenen Szenen tragen und ist die lohnendste Investition für dieses Heft.

<!--VORHANDEN_ENDE-->
