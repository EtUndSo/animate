---
title: Transponierte, Symmetrie und Gram-Matrix
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
knoten: Grundlagen 1: Vektoren und Matrizen
nachschlagen: ja
order: 15211100
summary: Vertauscht man in einer Matrix Zeilen und Spalten, entsteht ihre Transponierte.
tags: Transponierte, symmetrisch, Gram-Matrix
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Vertauscht man in einer Matrix Zeilen und Spalten, entsteht ihre Transponierte. Mit ihr lassen sich alle Skalarprodukte eines Datensatzes in einer einzigen Matrix sammeln: die Ähnlichkeiten aller Beispiele untereinander und die Zusammenhänge aller Merkmale untereinander.
:::

### Die Transponierte

<span class="anker" id="stufe-10-1"></span>

Aus Unterabschnitt [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3) ist das Zeichen $^{\top}$ bekannt: Es macht aus einer Spalte eine Zeile. Für Matrizen bedeutet es dasselbe, angewandt auf jede Spalte: Spalte $j$ wird zu Zeile $j$. Die Matrix wird dabei an ihrer Diagonale gespiegelt.

:::definition Definition 10.1 (Transponierte)
<span class="anker" id="satz-10-1"></span>

Die __Transponierte__ einer Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist die Matrix $\mathbf{A}^{\top}\in\mathbb{R}^{n\times m}$ mit

<span class="anker" id="gl-10-1"></span>
$$(\mathbf{A}^{\top})_{ij}=a_{ji} . \tag{10.1}$$
:::

Ein Vektor $\mathbf{x}\in\mathbb{R}^d$ ist eine $d\times1$-Matrix, seine Transponierte $\mathbf{x}^{\top}$ die $1\times d$-Matrix mit denselben Einträgen. Damit ist die Schreibweise $\mathbf{u}^{\top}\mathbf{v}$ aus Unterabschnitt [2.1](das-skalarprodukt.html#stufe-2-1) jetzt wörtlich ein Matrixprodukt: eine $1\times d$-Matrix mal eine $d\times1$-Matrix, das Ergebnis ist eine $1\times1$-Matrix, also eine Zahl.

:::satz Satz 10.2 (Rechenregeln der Transponierten)
<span class="anker" id="satz-10-2"></span>

Für Matrizen passender Formate und Skalare $c$ gilt

$$(\mathbf{A}^{\top})^{\top}=\mathbf{A},\qquad(\mathbf{A}+\mathbf{B})^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top},\qquad(c\,\mathbf{A})^{\top}=c\,\mathbf{A}^{\top},\qquad(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top} .$$
:::

:::herleitung Die Transponierte eines Produkts
Für $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{B}\in\mathbb{R}^{n\times k}$ ist nach [(10.1)](#gl-10-1) und [(9.1)](das-matrixprodukt.html#gl-9-1)

$$\bigl((\mathbf{A}\mathbf{B})^{\top}\bigr)_{li}=(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^na_{ij}\,b_{jl}=\sum_{j=1}^n(\mathbf{B}^{\top})_{lj}\,(\mathbf{A}^{\top})_{ji}=(\mathbf{B}^{\top}\mathbf{A}^{\top})_{li} .$$

Die ersten drei Regeln folgen direkt aus der Definition.
:::

⁠**Rechenbeispiel:**

$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^{\top}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$

Für $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ und $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ ist $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, also $(\mathbf{C}\mathbf{D})^{\top}=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$. Dasselbe liefert $\mathbf{D}^{\top}\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$, während $\mathbf{C}^{\top}\mathbf{D}^{\top}=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$ etwas anderes ist.

⁠**Kurz gesagt:** Transponieren vertauscht Zeilen und Spalten; beim Produkt kehrt sich die Reihenfolge um, $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$.

:::hintergrund Warum sich beim Transponieren eines Produkts die Reihenfolge umkehrt
Im Produkt $\mathbf{A}\mathbf{B}$ treffen die Zeilen von $\mathbf{A}$ auf die Spalten von $\mathbf{B}$. Nach dem Transponieren sind die Zeilen von $\mathbf{A}$ die Spalten von $\mathbf{A}^{\top}$, und die Spalten von $\mathbf{B}$ sind die Zeilen von $\mathbf{B}^{\top}$. Damit wieder Zeilen auf Spalten treffen, muss $\mathbf{B}^{\top}$ links stehen. Auch die Formate zeigen es: $(\mathbf{A}\mathbf{B})^{\top}$ hat das Format $k\times m$, und $\mathbf{B}^{\top}\mathbf{A}^{\top}$ ist $(k\times n)\cdot(n\times m)$, also passend. Der Ausdruck $\mathbf{A}^{\top}\mathbf{B}^{\top}$ wäre $(n\times m)\cdot(k\times n)$ und ist nur erklärt, wenn zufällig $m=k$ ist. Ein Sonderfall der Regel ist $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$: Eine Zahl ist ihre eigene Transponierte, also ist $\mathbf{u}^{\top}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{u}$.
:::

### Symmetrische Matrizen

<span class="anker" id="stufe-10-2"></span>

Manche Tabellen sind an ihrer Diagonale gespiegelt gleich. Eine Entfernungstabelle zwischen Städten ist so eine: Der Weg von München nach Köln ist so lang wie der von Köln nach München.

:::definition Definition 10.3 (Symmetrische Matrix)
<span class="anker" id="satz-10-3"></span>

Eine quadratische Matrix $\mathbf{A}$ heißt __symmetrisch__, wenn $\mathbf{A}^{\top}=\mathbf{A}$ ist, also $a_{ij}=a_{ji}$ für alle $i,j$.
:::

Jede Diagonalmatrix ist symmetrisch. Eine wichtige Quelle symmetrischer Matrizen sind Produkte einer Matrix mit ihrer eigenen Transponierten: Für jede Matrix $\mathbf{A}$ ist

<span class="anker" id="gl-10-2"></span>
$$(\mathbf{A}^{\top}\mathbf{A})^{\top}=\mathbf{A}^{\top}(\mathbf{A}^{\top})^{\top}=\mathbf{A}^{\top}\mathbf{A} , \tag{10.2}$$

also ist $\mathbf{A}^{\top}\mathbf{A}$ symmetrisch, und ebenso $\mathbf{A}\mathbf{A}^{\top}$.

⁠**Rechenbeispiel:** $\bigl(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr)$ ist symmetrisch, die Drehung $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ nicht. Für $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ ist

$$\mathbf{C}^{\top}\mathbf{C}=\begin{pmatrix}1&3\\2&4\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}10&14\\14&20\end{pmatrix},$$

symmetrisch, wie [(10.2)](#gl-10-2) verlangt.

⁠**Kurz gesagt:** Eine symmetrische Matrix ist gleich ihrer Transponierten; $\mathbf{A}^{\top}\mathbf{A}$ und $\mathbf{A}\mathbf{A}^{\top}$ sind immer symmetrisch.

:::hintergrund Skalarprodukte mit Gewichten
Im Skalarprodukt $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ zählt jede Stelle gleich viel. Will man die Stellen verschieden stark zählen, nimmt man positive Gewichte $d_1,\dots,d_n$ und bildet $\sum_jd_j\,u_jv_j$. Mit der Diagonalmatrix $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$ ist das $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$, denn $\mathbf{D}\mathbf{v}=(d_1v_1,\dots,d_nv_n)^{\top}$.

Diese Zahl hat dieselben Rechenregeln wie das gewöhnliche Skalarprodukt. Sie ist linear in jedem der beiden Vektoren, und $\mathbf{u}^{\top}\mathbf{D}\mathbf{u}=\sum_jd_ju_j^2$ ist positiv für jedes $\mathbf{u}\ne\mathbf{0}$. Symmetrisch ist sie, weil $\mathbf{D}$ symmetrisch ist: Eine Zahl ist ihre eigene Transponierte, und mit der Regel für die Transponierte eines Produkts, zweimal angewandt, ist $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{D}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{D}^{\top}\mathbf{u}=\mathbf{v}^{\top}\mathbf{D}\mathbf{u}$. Weil der Beweis der Cauchy-Schwarz-Ungleichung nur diese Regeln benutzt hat, kann man mit $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ ebenso Längen, Abstände und Winkel messen. Sie fallen nur anders aus. Zum Beispiel sind $(1,\,1)^{\top}$ und $(-1,\,1)^{\top}$ im gewöhnlichen Sinn orthogonal, mit $\mathbf{D}=\operatorname{diag}(2,\,1)$ aber nicht: $(1,\,1)\,\mathbf{D}\,(-1,\,1)^{\top}=2\cdot1\cdot(-1)+1\cdot1\cdot1=-1$.

Das Standardisieren aus Unterabschnitt [4.5](abstande-und-einheiten.html#stufe-4-5) ist genau eine solche Gewichtung. Der Abstand zweier standardisierter Beispiele ist $\sqrt{(\mathbf{x}_a-\mathbf{x}_b)^{\top}\mathbf{D}\,(\mathbf{x}_a-\mathbf{x}_b)}$ mit $\mathbf{D}=\operatorname{diag}(1/s_1^2,\dots,1/s_d^2)$. Umgekehrt wirkt jede solche Gewichtung wie ein Wechsel der Einheiten: Multipliziert man Merkmal $j$ mit $\sqrt{d_j}$, so ist das gewöhnliche Skalarprodukt der umgerechneten Vektoren $\sum_j(\sqrt{d_j}\,u_j)(\sqrt{d_j}\,v_j)=\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$. Die Wahl der Einheiten und die Wahl der Gewichte in $\mathbf{D}$ sind also dieselbe Entscheidung.
:::

### Die Gram-Matrix der Beispiele

<span class="anker" id="stufe-10-3"></span>

Wie ähnlich ist jedes Beispiel eines Datensatzes jedem anderen? Man kann alle paarweisen Skalarprodukte in eine Tabelle schreiben: Zeile $i$, Spalte $k$ enthält $\mathbf{x}_i^{\top}\mathbf{x}_k$. Diese Tabelle ist ein einziges Matrixprodukt.

:::definition Definition 10.4 (Gram-Matrix)
<span class="anker" id="satz-10-4"></span>

Die __Gram-Matrix__ einer Liste von Vektoren $\mathbf{v}_1,\dots,\mathbf{v}_k$ ist die $k\times k$-Matrix der paarweisen Skalarprodukte, mit dem Eintrag $\mathbf{v}_i^{\top}\mathbf{v}_l$ in Zeile $i$ und Spalte $l$.
:::

Für die Beispiele eines Datensatzes ist das die Matrix $\mathbf{X}\mathbf{X}^{\top}\in\mathbb{R}^{N\times N}$. Denn ihr Eintrag $(i,k)$ ist Zeile $i$ von $\mathbf{X}$ mal Spalte $k$ von $\mathbf{X}^{\top}$, also $\mathbf{x}_i^{\top}\mathbf{x}_k$:

<span class="anker" id="gl-10-3"></span>
$$(\mathbf{X}\mathbf{X}^{\top})_{ik}=\mathbf{x}_i^{\top}\mathbf{x}_k . \tag{10.3}$$

Sie ist symmetrisch, auf ihrer Diagonale stehen die Längenquadrate $\lVert\mathbf{x}_i\rVert^2$, und nach [(4.1)](abstande-und-einheiten.html#gl-4-1) lassen sich aus ihr alle Abstände ablesen:

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{x}_i-\mathbf{x}_k\rVert^2=(\mathbf{X}\mathbf{X}^{\top})_{ii}+(\mathbf{X}\mathbf{X}^{\top})_{kk}-2\,(\mathbf{X}\mathbf{X}^{\top})_{ik} . \tag{10.4}$$

Teilt man den Eintrag $(i,k)$ durch $\sqrt{(\mathbf{X}\mathbf{X}^{\top})_{ii}\,(\mathbf{X}\mathbf{X}^{\top})_{kk}}$, erhält man die Kosinus-Ähnlichkeit von $\mathbf{x}_i$ und $\mathbf{x}_k$.

⁠**Rechenbeispiel:** Für die drei Texte aus Unterabschnitt [5.4](winkel-und-ahnlichkeit.html#stufe-5-4) ist

$$\mathbf{X}=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix},\qquad \mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}13&26&2\\26&52&4\\2&4&10\end{pmatrix}.$$

Der Abstand von Text 1 und Text 3 ist nach [(10.4)](#gl-10-4) $\sqrt{13+10-2\cdot2}=\sqrt{19}$, wie früher berechnet. Die Kosinus-Ähnlichkeit von Text 1 und Text 2 ist $26/\sqrt{13\cdot52}=1$.

⁠**Kurz gesagt:** Die Gram-Matrix $\mathbf{X}\mathbf{X}^{\top}$ ist die Tabelle aller paarweisen Skalarprodukte der Beispiele; aus ihr folgen alle Längen, Abstände und Winkel.

:::hintergrund Die Gram-Matrix enthält die ganze Geometrie des Datensatzes
Längen, Abstände und Winkel zwischen den Beispielen hängen nur von den Skalarprodukten ab, nicht von den einzelnen Koordinaten. Dreht man den ganzen Datensatz zum Beispiel um den Nullpunkt, ändern sich alle Koordinaten, aber kein Skalarprodukt, und die Gram-Matrix bleibt dieselbe. Zwei Datensätze mit derselben Gram-Matrix sehen also geometrisch gleich aus. Wer nur wissen will, welche Beispiele einander ähnlich sind, braucht deshalb nicht die Datenmatrix selbst, sondern nur ihre Gram-Matrix.
:::

### Die Gram-Matrix der Merkmale

<span class="anker" id="stufe-10-4"></span>

Dreht man die Rollen um, so bekommt man eine Tabelle über die Merkmale: Wie sehr gehen zwei Merkmale über alle Beispiele hinweg gemeinsam? Ihre Merkmalsspalten sind Vektoren im $\mathbb{R}^N$, und ihr Skalarprodukt misst das. Diese Gram-Matrix der Spalten ist $\mathbf{X}^{\top}\mathbf{X}\in\mathbb{R}^{d\times d}$:

<span class="anker" id="gl-10-5"></span>
$$(\mathbf{X}^{\top}\mathbf{X})_{jl}=\sum_{i=1}^Nx_{ij}\,x_{il} . \tag{10.5}$$

Der Eintrag $(j,l)$ ist das Skalarprodukt der Merkmalsspalten $j$ und $l$, auf der Diagonale steht die Quadratsumme eines Merkmals.

:::satz Satz 10.5 (Die Gram-Matrix als Summe über die Beispiele)
<span class="anker" id="satz-10-5"></span>

<span class="anker" id="gl-10-6"></span>
$$\mathbf{X}^{\top}\mathbf{X}=\sum_{i=1}^N\mathbf{x}_i\,\mathbf{x}_i^{\top} . \tag{10.6}$$

Jedes Beispiel trägt sein eigenes äußeres Produkt bei.
:::

Der Eintrag $(j,l)$ der rechten Seite ist $\sum_ix_{ij}\,x_{il}$, derselbe wie in [(10.5)](#gl-10-5). Kommt ein neues Beispiel hinzu, ändert sich $\mathbf{X}^{\top}\mathbf{X}$ also nur um eine weitere Schicht $\mathbf{x}_{N+1}\mathbf{x}_{N+1}^{\top}$; man muss nicht alles neu ausrechnen.

⁠**Rechenbeispiel:** Für die Texte ist

$$\mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

Die Einträge der ersten Zeile sind die Skalarprodukte der Spalte „Tor“ mit den drei Merkmalsspalten (Abb. [37](#abb-37)).

:::abbildung ml/k1rgrammerk 37
Die erste Zeile der Gram-Matrix der Merkmale: Die Spalte „Tor“ $(3,\,6,\,0)^{\top}$ mal sich selbst, mal der Spalte „Ball“ $(2,\,4,\,1)^{\top}$ und mal der Spalte „Wahl“ $(0,\,0,\,3)^{\top}$.
:::

Die $0$ an der Stelle $(1,3)$ sagt: Die Wörter „Tor“ und „Wahl“ kommen in keinem Text gemeinsam vor. Als Summe der drei äußeren Produkte:

$$\begin{pmatrix}9&6&0\\6&4&0\\0&0&0\end{pmatrix}+\begin{pmatrix}36&24&0\\24&16&0\\0&0&0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&1&3\\0&3&9\end{pmatrix}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

⁠**Kurz gesagt:** $\mathbf{X}^{\top}\mathbf{X}$ ist die Gram-Matrix der Merkmalsspalten; sie ist die Summe der äußeren Produkte $\mathbf{x}_i\mathbf{x}_i^{\top}$ aller Beispiele.

:::aufgabe Aufgabe 24 ★ Transponieren
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Gib $\mathbf{B}^{\top}$ für $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ an und berechne $\mathbf{B}^{\top}\mathbf{B}$ und $\mathbf{B}\mathbf{B}^{\top}$. Welche Formate haben sie, und sind sie symmetrisch?

</li>

<li>

Zeige mit den Rechenregeln: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{B}^{\top}=\Bigl(\begin{smallmatrix}1&2\\0&1\\2&0\end{smallmatrix}\Bigr)$. Dann ist

$$\mathbf{B}^{\top}\mathbf{B}=\begin{pmatrix}5&2&2\\2&1&0\\2&0&4\end{pmatrix}\in\mathbb{R}^{3\times3},\qquad \mathbf{B}\mathbf{B}^{\top}=\begin{pmatrix}5&2\\2&5\end{pmatrix}\in\mathbb{R}^{2\times2}.$$

Beide sind symmetrisch, wie [(10.2)](#gl-10-2) verlangt. Der Eintrag $(1,1)$ von $\mathbf{B}^{\top}\mathbf{B}$ ist $1^2+2^2=5$, die Quadratsumme der ersten Spalte; der Eintrag $(1,2)$ von $\mathbf{B}\mathbf{B}^{\top}$ ist $1\cdot2+0\cdot1+2\cdot0=2$, das Skalarprodukt der beiden Zeilen.

(b) Zweimal die Produktregel: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\bigl((\mathbf{A}\mathbf{B})\mathbf{C}\bigr)^{\top}=\mathbf{C}^{\top}(\mathbf{A}\mathbf{B})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.
:::
:::

:::aufgabe Aufgabe 25 ★★ Gram-Matrizen eines kleinen Datensatzes
<span class="anker" id="aufg-25"></span>

Ein Datensatz hat drei Beispiele mit zwei Merkmalen: $\mathbf{x}_1=(1,\,0)^{\top}$, $\mathbf{x}_2=(2,\,1)^{\top}$, $\mathbf{x}_3=(0,\,3)^{\top}$.

<ol class="al">

<li>

Stelle $\mathbf{X}$ auf und berechne $\mathbf{X}\mathbf{X}^{\top}$ und $\mathbf{X}^{\top}\mathbf{X}$.

</li>

<li>

Lies aus $\mathbf{X}\mathbf{X}^{\top}$ den Abstand von $\mathbf{x}_2$ und $\mathbf{x}_3$ ab und prüfe ihn direkt.

</li>

<li>

Bestätige [(10.6)](#gl-10-6), indem du die drei äußeren Produkte $\mathbf{x}_i\mathbf{x}_i^{\top}$ addierst.

</li>

</ol>

:::loesung
(a) $\mathbf{X}=\Bigl(\begin{smallmatrix}1&0\\2&1\\0&3\end{smallmatrix}\Bigr)$,

$$\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}1&2&0\\2&5&3\\0&3&9\end{pmatrix},\qquad \mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}5&2\\2&10\end{pmatrix}.$$

(b) Nach [(10.4)](#gl-10-4) ist $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert^2=5+9-2\cdot3=8$, der Abstand also $\sqrt8\approx2{,}83$. Direkt: $\mathbf{x}_2-\mathbf{x}_3=(2,\,-2)^{\top}$ mit dem Längenquadrat $4+4=8$.

(c) $\mathbf{x}_1\mathbf{x}_1^{\top}=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$, $\mathbf{x}_2\mathbf{x}_2^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1\end{smallmatrix}\bigr)$, $\mathbf{x}_3\mathbf{x}_3^{\top}=\bigl(\begin{smallmatrix}0&0\\0&9\end{smallmatrix}\bigr)$; die Summe ist $\bigl(\begin{smallmatrix}5&2\\2&10\end{smallmatrix}\bigr)=\mathbf{X}^{\top}\mathbf{X}$.
:::
:::
