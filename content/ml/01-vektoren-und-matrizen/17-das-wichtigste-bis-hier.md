---
title: Das Wichtigste bis hier
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6211700
summary: Daten als Zahlenlisten, Modelle als lineare Abbildungen
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ein Beispiel mit $d$ Merkmalen ist ein Spaltenvektor $\mathbf{x}\in\mathbb{R}^d$; ein Datensatz aus $N$ Beispielen ist die Datenmatrix $\mathbf{X}\in\mathbb{R}^{N\times d}$ mit einem Beispiel pro Zeile.

</li>

<li>

Das Skalarprodukt $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ ist eine gewichtete Summe und ein Mustervergleich; die gewichtete Summe $\mathbf{w}^{\top}\mathbf{x}$ ist die allgemeinste lineare Vorschrift mit einem Ausgang.

</li>

<li>

Normen messen Größe: $\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}$, $\lVert\mathbf{x}\rVert_1=\sum_j|x_j|$, $\lVert\mathbf{x}\rVert_\infty=\max_j|x_j|$; der Effektivwert ist $\lVert\mathbf{x}\rVert/\sqrt n$. Abstände $\lVert\mathbf{u}-\mathbf{v}\rVert$ hängen von den Einheiten ab, Standardisieren macht sie davon unabhängig.

</li>

<li>

$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$; der Winkel ist $\cos\varphi=\mathbf{u}^{\top}\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)$, orthogonal heißt $\mathbf{u}^{\top}\mathbf{v}=0$.

</li>

<li>

$\mathbf{A}\mathbf{x}$ ist eine Liste von Skalarprodukten (Zeilensicht) und eine Linearkombination der Spalten (Spaltensicht); $\mathbf{X}\mathbf{w}$ sind alle Vorhersagen zugleich.

</li>

<li>

Jede lineare Abbildung ist eine Matrix, ihre Spalten sind die Bilder der Einheitsvektoren; affin heißt $\mathbf{A}\mathbf{x}+\mathbf{b}$.

</li>

<li>

$\mathbf{A}\mathbf{B}$ ist „erst $\mathbf{B}$, dann $\mathbf{A}$“; assoziativ, nicht kommutativ; lineare Stufen hintereinander sind eine Matrix.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$; $\mathbf{X}\mathbf{X}^{\top}$ enthält alle Skalarprodukte der Beispiele, $\mathbf{X}^{\top}\mathbf{X}=\sum_i\mathbf{x}_i\mathbf{x}_i^{\top}$ die der Merkmale.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ hat keine, eine oder unendlich viele Lösungen und ist genau dann lösbar, wenn $\mathbf{y}$ im Spaltenraum liegt.

</li>

<li>

$\dim\ker\mathbf{A}+\operatorname{rang}\mathbf{A}=n$; abhängige Merkmale senken den Rang und machen die Gewichte mehrdeutig.

</li>

<li>

$\det\mathbf{A}$ ist der vorzeichenbehaftete Volumenfaktor, $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$, und $\mathbf{A}$ ist genau dann invertierbar, wenn $\det\mathbf{A}\ne0$.

</li>

<li>

$\odot$ multipliziert Eintrag für Eintrag; Tensoren sind Zahlenfelder mit beliebig vielen Achsen.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Datensatz ist eine Matrix, deren Zeilen die Beispiele als Vektoren enthalten, und Ähnlichkeit, Abstand und Größe sind Skalarprodukte und Normen dieser Vektoren, die von den gewählten Einheiten abhängen.

</li>

<li>

Eine lineare Vorschrift ist durch die Bilder der Einheitsvektoren festgelegt, also eine Matrix, und das Matrix-Vektor-Produkt wendet sie auf alle Beispiele zugleich an.

</li>

<li>

Hintereinanderausführen ist Multiplizieren der Matrizen, und ob sich eine Abbildung umkehren lässt, entscheiden Rang, Kern und Determinante: Sie zeigen, ob dabei Richtungen verloren gehen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Rechenarten: Vektoren werden addiert und mit Zahlen multipliziert, und lineare Abbildungen erhalten genau diese beiden Rechenarten.

| Ergebnis | Woher es kommt |
|---|---|
| Gewichtete Summe, Mustervergleich | Skalarprodukt: Produkte an gleicher Stelle, aufsummiert (Abschnitt [2](das-skalarprodukt.html#stufe-2)) |
| Länge, Abstand, Winkel | alle aus dem Skalarprodukt: $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$, [(4.1)](abstande-und-einheiten.html#gl-4-1), Cauchy-Schwarz (Abschnitte [3](normen-die-groe-eines-vektors.html#stufe-3) bis [5](winkel-und-ahnlichkeit.html#stufe-5)) |
| Abstände hängen von den Einheiten ab | jedes Merkmal geht mit seinem quadrierten Zahlenwert ein (Abschnitt [4](abstande-und-einheiten.html#stufe-4)) |
| Zeilen- und Spaltensicht | dieselbe Doppelsumme, verschieden geordnet (Abschnitt [7](das-matrix-vektor-produkt.html#stufe-7)) |
| Matrix einer linearen Abbildung | $\mathbf{x}=\sum_jx_j\mathbf{e}_j$, und die Abbildung erhält Linearkombinationen (Abschnitt [8](lineare-abbildungen.html#stufe-8)) |
| Matrixprodukt, nicht kommutativ | Matrix der Hintereinanderausführung (Abschnitt [9](das-matrixprodukt.html#stufe-9)) |
| Gram-Matrix | Tabelle der Skalarprodukte, $\mathbf{X}\mathbf{X}^{\top}$ und $\mathbf{X}^{\top}\mathbf{X}$ (Abschnitt [10](transponierte-symmetrie-und-gram-matrix.html#stufe-10)) |
| Keine Inverse bei $\mathbf{A}\mathbf{x}=\mathbf{0}$, $\mathbf{x}\ne\mathbf{0}$ | zwei Eingänge, ein Ausgang: Information verloren (Abschnitt [11](einheitsmatrix-und-inverse.html#stufe-11)) |
| Keine, eine, unendlich viele Lösungen | mit zwei Lösungen ist die ganze Gerade durch sie Lösung (Abschnitt [12](lineare-gleichungssysteme.html#stufe-12)) |
| Mehrdeutige Gewichte | Vektoren im Kern ändern $\mathbf{X}\mathbf{w}$ nicht (Abschnitt [13](unabhangigkeit-basis-und-rang.html#stufe-13)) |
| $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ | Volumenfaktoren multiplizieren sich beim Hintereinanderausführen (Abschnitt [14](die-determinante.html#stufe-14)) |
