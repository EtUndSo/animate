---
title: Elementweise Rechnen und Tensoren
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6211600
summary: Nicht jede Rechnung mit Vektoren und Matrizen ist ein Matrixprodukt.
tags: Hadamard-Produkt, elementweise, Tensor, Achse, Form
lang: de
---

<span class="anker" id="stufe-15"></span>

:::zweck
Nicht jede Rechnung mit Vektoren und Matrizen ist ein Matrixprodukt. Dieser Abschnitt stellt die Rechnungen vor, die Eintrag für Eintrag arbeiten, und erweitert Vektoren und Matrizen zu Zahlenfeldern mit mehr als zwei Indizes, wie sie für Bilder gebraucht werden.
:::

### Das Hadamard-Produkt

<span class="anker" id="stufe-15-1"></span>

Ein Händler hat die Liste der verkauften Mengen und die Liste der Stückpreise. Für jede Ware will er den Umsatz, also Menge mal Preis, aber noch nicht die Summe. Das ist ein Produkt Eintrag für Eintrag.

:::definition Definition 15.1 (Hadamard-Produkt)
<span class="anker" id="satz-15-1"></span>

Für zwei Vektoren oder zwei Matrizen gleichen Formats ist das __Hadamard-Produkt__ $\mathbf{A}\odot\mathbf{B}$ das Produkt Eintrag für Eintrag:

<span class="anker" id="gl-15-1"></span>
$$(\mathbf{A}\odot\mathbf{B})_{ij}=a_{ij}\,b_{ij} . \tag{15.1}$$
:::

Das Hadamard-Produkt ist *nicht* das Matrixprodukt. Das Matrixprodukt bildet Skalarprodukte aus Zeilen und Spalten; das Hadamard-Produkt multipliziert nur Einträge an derselben Stelle. Zwei Zusammenhänge mit Bekanntem: Summiert man das Hadamard-Produkt zweier Vektoren, erhält man ihr Skalarprodukt, $\mathbf 1^{\top}(\mathbf{u}\odot\mathbf{v})=\mathbf{u}^{\top}\mathbf{v}$. Und das Hadamard-Produkt mit einem festen Vektor ist eine Diagonalmatrix: $\mathbf{v}\odot\mathbf{x}=\operatorname{diag}(\mathbf{v})\,\mathbf{x}$.

⁠**Rechenbeispiel:** $(1,\,2,\,3)^{\top}\odot(4,\,5,\,6)^{\top}=(4,\,10,\,18)^{\top}$, und $4+10+18=32$ ist das Skalarprodukt. Für Matrizen ist

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix},\qquad\text{aber}\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

Mit einem Vektor aus Nullen und Einsen kann man Merkmale ausblenden: $(1,\,0,\,1)^{\top}\odot\mathbf{x}_1=(60,\,0,\,3)^{\top}$ lässt bei Wohnung 1 die Zimmerzahl weg.

⁠**Kurz gesagt:** Das Hadamard-Produkt $\odot$ multipliziert Eintrag für Eintrag; es ist nicht das Matrixprodukt.

### Elementweise Funktionen

<span class="anker" id="stufe-15-2"></span>

Oft wendet man dieselbe Funktion auf jeden Eintrag eines Vektors an: man quadriert alle Fehler, nimmt von allen den Betrag oder rundet alle Werte.

:::definition Definition 15.2 (Elementweise Funktion)
<span class="anker" id="satz-15-2"></span>

Für eine Funktion $f\colon\mathbb{R}\to\mathbb{R}$ und einen Vektor $\mathbf{x}\in\mathbb{R}^d$ ist $f$, __elementweise__ angewandt, der Vektor $\bigl(f(x_1),\dots,f(x_d)\bigr)^{\top}$. Für Matrizen gilt dasselbe Eintrag für Eintrag.
:::

Viele Normen lassen sich so schreiben: Die Betragssummennorm ist die Summe der elementweisen Beträge, $\lVert\mathbf{x}\rVert_1=\mathbf 1^{\top}|\mathbf{x}|$, und das Quadrat der euklidischen Norm die Summe der elementweisen Quadrate. Eine elementweise Funktion ist im Allgemeinen nicht linear: Elementweises Quadrieren macht aus $2\mathbf{x}$ den Vektor mit den Einträgen $4x_j^2$, nicht $2x_j^2$.

⁠**Rechenbeispiel:** Der Fehlervektor der Maklerin war $(-12,\,-4,\,-4,\,-8)^{\top}$. Elementweise Beträge ergeben $(12,\,4,\,4,\,8)^{\top}$ mit der Summe $28$, der Betragssummennorm. Für Gutachter A aus Unterabschnitt [3.5](normen-die-groe-eines-vektors.html#stufe-3-5) ergeben die elementweisen Quadrate $(100,\,100,\,100,\,100)^{\top}$ mit der Summe $400=20^2$.

⁠**Kurz gesagt:** Eine elementweise Funktion wirkt auf jeden Eintrag für sich; sie ist im Allgemeinen nicht linear.

### Einen Vektor zu jeder Zeile addieren

<span class="anker" id="stufe-15-3"></span>

Um einen ganzen Datensatz zu zentrieren, zieht man von jeder Zeile der Datenmatrix denselben Vektor ab, den Mittelwert der Beispiele. Genauso addiert die affine Vorhersage zu jeder Komponente denselben Achsenabschnitt. Für solche Rechnungen braucht man eine Schreibweise.

Den Mittelwert der Beispiele liefert ein Matrix-Vektor-Produkt: $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$, denn Komponente $j$ davon ist $\frac1N\sum_ix_{ij}$, der Mittelwert der Spalte $j$. Die Matrix, deren Zeilen alle gleich $\bar{\mathbf{x}}^{\top}$ sind, ist das äußere Produkt $\mathbf 1\,\bar{\mathbf{x}}^{\top}$. Damit ist die zentrierte Datenmatrix

<span class="anker" id="gl-15-2"></span>
$$\tilde{\mathbf{X}}=\mathbf{X}-\mathbf 1\,\bar{\mathbf{x}}^{\top} , \tag{15.2}$$

deren Zeile $i$ der Vektor $(\mathbf{x}_i-\bar{\mathbf{x}})^{\top}$ ist. Viele Texte schreiben dafür kurz $\mathbf{X}-\bar{\mathbf{x}}^{\top}$ und meinen damit: den Zeilenvektor von jeder Zeile abziehen. Streng genommen ist die Differenz einer $N\times d$-Matrix und einer $1\times d$-Matrix nicht erklärt; die Kurzschrift steht immer für [(15.2)](#gl-15-2).

⁠**Rechenbeispiel:** Für die Wohnungen ist $\bar{\mathbf{x}}=\tfrac14\mathbf{X}^{\top}\mathbf 1=(65;\ 2{,}5;\ 3)^{\top}$ und

$$\tilde{\mathbf{X}}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}-\begin{pmatrix}65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\end{pmatrix}=\begin{pmatrix}-5&-0{,}5&0\\-25&-1{,}5&-2\\25&1{,}5&3\\5&0{,}5&-1\end{pmatrix}.$$

Jede Spalte ist die zentrierte Merkmalsspalte aus Unterabschnitt [4.3](abstande-und-einheiten.html#stufe-4-3) und summiert sich zu null.

⁠**Kurz gesagt:** Einen Vektor $\mathbf{q}$ zu jeder Zeile einer Matrix $\mathbf{A}$ zu addieren heißt $\mathbf{A}+\mathbf 1\,\mathbf{q}^{\top}$; die verbreitete Kurzschrift $\mathbf{A}+\mathbf{q}^{\top}$ meint genau das.

### Tensoren

<span class="anker" id="stufe-15-4"></span>

Ein Skalar ist eine einzelne Zahl, ein Vektor eine Liste mit einem Index, eine Matrix eine Tabelle mit zwei Indizes. Ein Farbbild braucht drei: Zeile, Spalte und Farbkanal. Ein Stapel von Farbbildern braucht vier. Man fasst all diese Zahlenfelder unter einem Namen zusammen.

:::definition Definition 15.3 (Tensor, Form)
<span class="anker" id="satz-15-3"></span>

Ein __Tensor__ ist im maschinellen Lernen ein Zahlenfeld, dessen Einträge durch $k$ Indizes nummeriert werden. Jeder Index läuft entlang einer __Achse__. Die Liste der Achsenlängen heißt die __Form__ des Tensors.
:::

Ein Skalar ist ein Tensor mit $0$ Achsen, ein Vektor im $\mathbb{R}^d$ einer mit einer Achse der Länge $d$, eine Matrix im $\mathbb{R}^{m\times n}$ einer mit der Form $m\times n$. Ein Tensor der Form $n_1\times n_2\times\dots\times n_k$ hat $n_1\cdot n_2\cdots n_k$ Einträge. Abbildung [42](#abb-42) zeigt die ersten Stufen.

:::abbildung ml/k1tensor 42
Tensoren mit $0$ bis $4$ Achsen: ein Skalar, ein Vektor mit $4$ Einträgen, eine $4\times4$-Matrix (etwa ein Graustufenbild), ein Farbbild aus drei $4\times4$-Kanälen für Rot, Grün und Blau und ein Stapel aus $N$ solchen Farbbildern (angedeutet mit drei Bildern).
:::

⁠**Rechenbeispiel:** Ein Farbbild mit $4\times4$ Bildpunkten und drei Farbkanälen ist ein Tensor der Form $3\times4\times4$ mit $48$ Einträgen. Der Eintrag mit den Indizes $(1,2,3)$ ist die Helligkeit des ersten Kanals, also Rot, im Bildpunkt in Zeile $2$ und Spalte $3$.

⁠**Kurz gesagt:** Ein Tensor ist ein Zahlenfeld mit beliebig vielen Achsen; Skalar, Vektor und Matrix sind die Fälle mit $0$, $1$ und $2$ Achsen.

:::hintergrund Der Tensor der Physik ist etwas anderes
In der Physik und der Elektrotechnik ist ein Tensor mehr als ein Zahlenfeld, etwa der Spannungstensor eines Werkstoffs oder der Permittivitätstensor eines Kristalls. Dort gehört zum Tensor eine Vorschrift, wie sich seine Einträge ändern, wenn man das Koordinatensystem dreht; die Einträge allein machen ihn nicht aus. Im maschinellen Lernen fehlt diese Vorschrift: Ein Tensor ist dort nur ein mehrdimensionales Feld von Zahlen. Das Wort ist dasselbe, der Begriff ein anderer.
:::

### Bilder als Tensoren

<span class="anker" id="stufe-15-5"></span>

Bilddaten sind das wichtigste Beispiel für Tensoren mit mehr als zwei Achsen. Ihre Form zeigt sofort, wie viele Zahlen ein Datensatz enthält.

Ein Graustufenbild mit $28\times28$ Bildpunkten ist eine Matrix, also ein Tensor der Form $28\times28$ mit $784$ Einträgen. Ein Farbbild mit $32\times32$ Bildpunkten hat drei Kanäle und die Form $3\times32\times32$, also $3072$ Einträge. Ein Stapel von $100$ solchen Farbbildern hat die Form $100\times3\times32\times32$ und $307\,200$ Einträge. Die erste Achse zählt dabei die Beispiele, genau wie die Zeilen der Datenmatrix: Die Datenmatrix ist der Sonderfall eines Stapels von Vektoren, mit der Form $N\times d$.

Die Reihenfolge der Achsen ist eine Vereinbarung. Manche Programme legen den Farbkanal an den Anfang ($3\times32\times32$), andere an das Ende ($32\times32\times3$). Die Zahlen sind dieselben, nur ihre Anordnung unterscheidet sich, und vor jeder Rechnung muss klar sein, welche Achse was bedeutet.

⁠**Rechenbeispiel:** Ein Datensatz aus $60\,000$ Graustufenbildern mit $28\times28$ Bildpunkten ist ein Tensor der Form $60\,000\times28\times28$ mit $47\,040\,000$ Einträgen. Liest man jedes Bild zu einem Vektor im $\mathbb{R}^{784}$ aus, wird daraus eine Datenmatrix im $\mathbb{R}^{60\,000\times784}$, mit denselben Einträgen.

⁠**Kurz gesagt:** Ein Bild ist ein Tensor mit zwei oder drei Achsen, ein Stapel von Bildern einer mit einer Achse mehr; die erste Achse zählt die Beispiele.

:::aufgabe Aufgabe 36 ★ Elementweise oder nicht?
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

Berechne $\mathbf{u}\odot\mathbf{v}$ und $\mathbf{u}^{\top}\mathbf{v}$ für $\mathbf{u}=(2,\,-1,\,3)^{\top}$ und $\mathbf{v}=(1,\,4,\,2)^{\top}$.

</li>

<li>

Berechne $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\odot\bigl(\begin{smallmatrix}2&0\\1&3\end{smallmatrix}\bigr)$ und das Matrixprodukt derselben Matrizen.

</li>

<li>

Welche Form und wie viele Einträge hat ein Stapel aus $64$ Farbbildern mit $224\times224$ Bildpunkten, den Farbkanal vorn?

</li>

</ol>

:::loesung
(a) $\mathbf{u}\odot\mathbf{v}=(2,\,-4,\,6)^{\top}$ und $\mathbf{u}^{\top}\mathbf{v}=2-4+6=4$, die Summe der Einträge des Hadamard-Produkts.

(b) Hadamard: $\bigl(\begin{smallmatrix}1\cdot2&2\cdot0\\3\cdot1&4\cdot3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&0\\3&12\end{smallmatrix}\bigr)$. Matrixprodukt: $\bigl(\begin{smallmatrix}2+2&0+6\\6+4&0+12\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4&6\\10&12\end{smallmatrix}\bigr)$. Nur der Eintrag rechts unten stimmt zufällig überein.

(c) Die Form ist $64\times3\times224\times224$, mit $64\cdot3\cdot224\cdot224=9\,633\,792$ Einträgen.
:::
:::

:::aufgabe Aufgabe 37 ★★ Einen Datensatz zentrieren
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Zeige: Die Spalten der zentrierten Datenmatrix [(15.2)](#gl-15-2) summieren sich zu null, also $\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf{0}^{\top}$. Benutze $\mathbf 1^{\top}\mathbf 1=N$.

</li>

<li>

Zentriere die Datenmatrix der drei Texte aus Unterabschnitt [5.4](winkel-und-ahnlichkeit.html#stufe-5-4).

</li>

</ol>

:::loesung
(a) Es ist $\bar{\mathbf{x}}^{\top}=\frac1N\mathbf 1^{\top}\mathbf{X}$, die Transponierte von $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$. Damit ist

$$\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf 1^{\top}\mathbf{X}-(\mathbf 1^{\top}\mathbf 1)\,\bar{\mathbf{x}}^{\top}=\mathbf 1^{\top}\mathbf{X}-N\cdot\tfrac1N\,\mathbf 1^{\top}\mathbf{X}=\mathbf{0}^{\top} .$$

Jede Spalte ist ein zentrierter Vektor, und dessen Komponenten addieren sich zu null, wie in Unterabschnitt [4.3](abstande-und-einheiten.html#stufe-4-3).

(b) Der Mittelwert der Texte ist $\bar{\mathbf{x}}=\tfrac13\bigl((3,2,0)^{\top}+(6,4,0)^{\top}+(0,1,3)^{\top}\bigr)=(3,\,\tfrac73,\,1)^{\top}$. Zentriert:

$$\tilde{\mathbf{X}}=\begin{pmatrix}0&-\frac13&-1\\3&\frac53&-1\\-3&-\frac43&2\end{pmatrix}.$$

Jede Spalte summiert sich zu null: $0+3-3=0$, $-\tfrac13+\tfrac53-\tfrac43=0$, $-1-1+2=0$.
:::
:::
