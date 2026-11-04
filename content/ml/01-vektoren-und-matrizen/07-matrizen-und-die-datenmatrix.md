---
title: Matrizen und die Datenmatrix
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6210700
summary: Ein Datensatz besteht aus vielen Vektoren gleicher Länge.
tags: Matrix, Eintrag, Format, quadratisch, Diagonale, Diagonalmatrix, Nullmatrix, Datenmatrix
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Ein Datensatz besteht aus vielen Vektoren gleicher Länge. Dieser Abschnitt fasst sie zu einer einzigen Zahlentabelle zusammen, einer Matrix, und legt fest, wie man mit Matrizen schreibt und rechnet.
:::

### Matrizen

<span class="anker" id="stufe-6-1"></span>

Die Tabelle der Wohnungen ist mehr als vier einzelne Vektoren: Sie ist ein Gegenstand, mit dem man als Ganzes rechnen will. Auch ein Graustufenbild ist eine Tabelle, nämlich von Helligkeiten, angeordnet in Zeilen und Spalten. Ein solches rechteckiges Zahlenschema heißt Matrix.

:::definition Definition 6.1 (Matrix)
<span class="anker" id="satz-6-1"></span>

Eine __Matrix__ $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist eine rechteckige Anordnung von $m\cdot n$ reellen Zahlen in $m$ Zeilen und $n$ Spalten:

$$\mathbf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}.$$

Die Zahl $a_{ij}$ in Zeile $i$ und Spalte $j$ heißt __Eintrag__ der Matrix. Das Paar $m\times n$ heißt das __Format__ der Matrix.
:::

Matrizen werden fett und groß geschrieben, ihre Einträge mit dem kleinen Buchstaben und zwei Indizes: zuerst die Zeile, dann die Spalte. Die $j$-te Spalte von $\mathbf{A}$ ist ein Vektor mit $m$ Komponenten; er heißt $\mathbf{a}_j$. Man schreibt die Matrix dann auch als Reihe ihrer Spalten, $\mathbf{A}=\begin{pmatrix}\mathbf{a}_1&\cdots&\mathbf{a}_n\end{pmatrix}$. Ein Vektor mit $d$ Komponenten ist eine Matrix mit dem Format $d\times1$, eine Zeile mit $d$ Zahlen eine Matrix mit dem Format $1\times d$.

Zwei Matrizen sind gleich, wenn sie dasselbe Format und an jeder Stelle denselben Eintrag haben. Matrizen gleichen Formats addiert man und multipliziert sie mit einer Zahl Eintrag für Eintrag, genau wie Vektoren: $(\mathbf{A}+\mathbf{B})_{ij}=a_{ij}+b_{ij}$ und $(c\,\mathbf{A})_{ij}=c\,a_{ij}$.

⁠**Rechenbeispiel:** Die Matrix

$$\mathbf{A}=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\in\mathbb{R}^{2\times3}$$

hat das Format $2\times3$, die Einträge $a_{12}=2$ und $a_{21}=4$ und die zweite Spalte $\mathbf{a}_2=(2,\,5)^{\top}$. Ein Graustufenbild aus $3\times3$ Bildpunkten, das ein helles Kreuz auf dunklem Grund zeigt, ist die Matrix mit den Zeilen $(0,1,0)$, $(1,1,1)$ und $(0,1,0)$. Außerdem ist

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad 2\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}2&4\\6&8\end{pmatrix}.$$

⁠**Kurz gesagt:** Eine Matrix ist eine rechteckige Zahlentabelle mit $m$ Zeilen und $n$ Spalten; der Eintrag $a_{ij}$ steht in Zeile $i$ und Spalte $j$.

:::hintergrund Ein Bild als Matrix und als Vektor
Liest man ein Bild Zeile für Zeile aus und hängt die Zeilen hintereinander, wird aus der Matrix ein langer Vektor: aus dem $3\times3$-Kreuz der Vektor $(0,1,0,1,1,1,0,1,0)^{\top}\in\mathbb{R}^9$, aus einem $28\times28$-Bild ein Vektor im $\mathbb{R}^{784}$. Die Zahlen bleiben dieselben, aber eine Information geht in der Schreibweise verloren: welche Bildpunkte Nachbarn sind. Der Bildpunkt direkt unter einem anderen steht im langen Vektor $28$ Stellen weiter hinten. Für Rechnungen, die jedes Merkmal einzeln gewichten, spielt das keine Rolle. Für Rechnungen, die Nachbarschaften ausnutzen wollen, ist die Matrixform die natürlichere.
:::

### Quadratische Matrizen und Diagonalmatrizen

<span class="anker" id="stufe-6-2"></span>

Einige Matrizen kommen so oft vor, dass sie eigene Namen haben. Bei allen dreien ist die Form der Tabelle besonders einfach.

Eine Matrix mit gleich vielen Zeilen und Spalten heißt __quadratisch__. Die Einträge $a_{11},a_{22},\dots,a_{nn}$ einer quadratischen Matrix bilden ihre __Diagonale__, die von links oben nach rechts unten läuft.

:::definition Definition 6.2 (Diagonalmatrix, Nullmatrix)
<span class="anker" id="satz-6-2"></span>

Eine quadratische Matrix, deren Einträge außerhalb der Diagonale alle null sind, heißt __Diagonalmatrix__. Für einen Vektor $\mathbf{v}\in\mathbb{R}^n$ ist $\operatorname{diag}(\mathbf{v})$ die Diagonalmatrix mit den Diagonaleinträgen $v_1,\dots,v_n$.

Die Matrix, deren Einträge alle null sind, heißt __Nullmatrix__ und wird $\mathbf 0$ geschrieben.
:::

⁠**Rechenbeispiel:**

$$\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)=\begin{pmatrix}2&0\\0&0{,}5\end{pmatrix},\qquad \operatorname{diag}\bigl((1,\,0,\,3)^{\top}\bigr)=\begin{pmatrix}1&0&0\\0&0&0\\0&0&3\end{pmatrix}.$$

Die zweite Matrix hat einen Diagonaleintrag null und ist trotzdem eine Diagonalmatrix; verlangt wird nur, dass außerhalb der Diagonale Nullen stehen. Statt $\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)$ schreibt man kurz $\operatorname{diag}(2;\,0{,}5)$.

⁠**Kurz gesagt:** Eine quadratische Matrix hat gleich viele Zeilen wie Spalten; eine Diagonalmatrix hat nur auf der Diagonale Einträge ungleich null.

### Die Datenmatrix

<span class="anker" id="stufe-6-3"></span>

Die Wohnungstabelle aus Unterabschnitt [1.2](vektoren-daten-als-zahlenlisten.html#stufe-1-2) ist eine Matrix: vier Zeilen, eine je Wohnung, und drei Spalten, eine je Merkmal. Diese Anordnung, ein Beispiel pro Zeile, ist die Standardform eines Datensatzes (Abb. [27](#abb-27)).

:::abbildung ml/k1datenmatrix 27
Die Datenmatrix $\mathbf{X}$ des Wohnungsdatensatzes. Jede Zeile ist ein Beispiel, als Zeile geschriebener Vektor $\mathbf{x}_i^{\top}$ (blau: Wohnung 2). Jede Spalte ist die Merkmalsspalte eines Merkmals über alle Beispiele (orange: die Flächen). Der Eintrag $x_{21}=40$ steht in beiden.
:::

:::definition Definition 6.3 (Datenmatrix)
<span class="anker" id="satz-6-3"></span>

Zu einem Datensatz mit den Beispielen $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^d$ ist die __Datenmatrix__ die Matrix $\mathbf{X}\in\mathbb{R}^{N\times d}$, deren Zeile $i$ das Beispiel $\mathbf{x}_i$ ist, als Zeile geschrieben:

<span class="anker" id="gl-6-1"></span>
$$\mathbf{X}=\begin{pmatrix}\mathbf{x}_1^{\top}\\\mathbf{x}_2^{\top}\\\vdots\\\mathbf{x}_N^{\top}\end{pmatrix}=\begin{pmatrix}x_{11}&\cdots&x_{1d}\\\vdots&&\vdots\\x_{N1}&\cdots&x_{Nd}\end{pmatrix}. \tag{6.1}$$
:::

Der Eintrag $x_{ij}$ ist der Wert von Merkmal $j$ bei Beispiel $i$, genau wie in Unterabschnitt [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3) vereinbart. Die Spalte $j$ von $\mathbf{X}$ ist die Merkmalsspalte von Merkmal $j$ aus Unterabschnitt [4.3](abstande-und-einheiten.html#stufe-4-3): alle Werte dieses Merkmals über alle Beispiele. Die Zeilen gehören also zu den Beispielen, die Spalten zu den Merkmalen. Der Mittelwert der Beispiele $\bar{\mathbf{x}}$ hat als Komponente $j$ den Mittelwert der Spalte $j$.

⁠**Rechenbeispiel:** Für den Wohnungsdatensatz ist

$$\mathbf{X}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\in\mathbb{R}^{4\times3}.$$

Der Eintrag $x_{32}=4$ ist die Zimmerzahl von Wohnung 3, die erste Spalte $(60,\,40,\,90,\,70)^{\top}$ enthält alle Flächen, und ihr Mittelwert $65$ ist die erste Komponente von $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$.

⁠**Kurz gesagt:** Die Datenmatrix $\mathbf{X}\in\mathbb{R}^{N\times d}$ enthält ein Beispiel pro Zeile und ein Merkmal pro Spalte.

:::hintergrund Beispiele als Zeilen oder als Spalten?
Diese Reihe schreibt die Beispiele als Zeilen, so wie in einer Tabellenkalkulation und in den meisten heutigen Lehrbüchern und Programmbibliotheken. Manche Texte machen es umgekehrt und stellen die Beispiele als Spalten nebeneinander; ihre Datenmatrix hat dann das Format $d\times N$. Auch die Buchstaben schwanken: Oft heißt die Zahl der Beispiele $m$ und die Zahl der Merkmale $n$, und das Beispiel Nummer $i$ wird $\mathbf{x}^{(i)}$ geschrieben, mit dem Index oben in Klammern. Inhaltlich ändert sich nichts. Wer einen fremden Text liest, prüft deshalb zuerst, was dort Zeile und was Spalte ist.
:::

:::aufgabe Aufgabe 15 ★ Matrizen lesen und aufstellen
<span class="anker" id="aufg-15"></span>

<ol class="al">

<li>

Welches Format hat $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$? Gib $b_{13}$, $b_{21}$ und die dritte Spalte von $\mathbf{B}$ an.

</li>

<li>

Stelle die Datenmatrix der drei Texte aus Unterabschnitt [5.4](winkel-und-ahnlichkeit.html#stufe-5-4) auf. Was bedeuten $N$, $d$ und der Eintrag $x_{23}$?

</li>

<li>

Ein Graustufenbild aus $4\times4$ Bildpunkten zeigt ein helles „L“: Die erste Spalte und die unterste Zeile sind hell ($1$), alles andere dunkel ($0$). Schreibe die Matrix auf und lies sie Zeile für Zeile zu einem Vektor aus. Wie viele Komponenten hat er?

</li>

</ol>

:::loesung
(a) $\mathbf{B}$ hat das Format $2\times3$. Es ist $b_{13}=2$ (Zeile 1, Spalte 3) und $b_{21}=2$ (Zeile 2, Spalte 1); die dritte Spalte ist $(2,\,0)^{\top}$.

(b) $\mathbf{X}=\Bigl(\begin{smallmatrix}3&2&0\\6&4&0\\0&1&3\end{smallmatrix}\Bigr)$ mit $N=3$ Texten und $d=3$ Wörtern. Der Eintrag $x_{23}=0$ sagt: Im zweiten Text kommt das dritte Wort, „Wahl“, nicht vor.

(c) Die Matrix hat die Zeilen $(1,0,0,0)$, $(1,0,0,0)$, $(1,0,0,0)$ und $(1,1,1,1)$. Zeilenweise ausgelesen ergibt sie den Vektor

$$(1,0,0,0,\ 1,0,0,0,\ 1,0,0,0,\ 1,1,1,1)^{\top}\in\mathbb{R}^{16}$$

mit $4\cdot4=16$ Komponenten.
:::
:::
