---
title: Die beste Näherungslösung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
knoten: Grundlagen 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15220400
summary: Ein Gleichungssystem mit mehr Gleichungen als Unbekannten hat meist keine Lösung.
tags: Residuum, beste Näherungslösung, Normalgleichungen, Ausgleichsgerade
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Ein Gleichungssystem mit mehr Gleichungen als Unbekannten hat meist keine Lösung. Dieser Abschnitt sucht stattdessen die Unbekannten, die das System so gut wie möglich erfüllen. Sie folgen aus einem kleineren, immer lösbaren Gleichungssystem, und der Grund dafür ist wieder ein rechter Winkel.
:::

### Rückblick: Mehr Gleichungen als Unbekannte

<span class="anker" id="stufe-3-1"></span>

In [Grundlagen 1, Abschnitt 12.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-5), sollten zwei Gewichte $w_1$ für die Fläche und $w_2$ für die Zimmerzahl die Preise von Wohnungen genau treffen. Mit allen vier Wohnungen ist das das System $\mathbf{A}\mathbf{w}=\mathbf{y}$ mit

$$\mathbf{A}=\begin{pmatrix}60&2\\40&1\\90&4\\70&3\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}200\\130\\290\\240\end{pmatrix}\ \text{Tausend Euro}.$$

Es hat keine Lösung. Im Spaltenbild heißt das: Die Spalten von $\mathbf{A}$ spannen im $\mathbb{R}^4$ eine Ebene auf, den Spaltenraum, und der Preisvektor $\mathbf{y}$ liegt nicht in ihr. Was immer man für $\mathbf{w}$ wählt, ein Rest bleibt übrig.

:::definition Definition 3.1 (Residuum)
<span class="anker" id="satz-3-1"></span>

Für ein Gleichungssystem $\mathbf{A}\mathbf{x}=\mathbf{y}$ und einen beliebigen Vektor $\mathbf{x}$ heißt

<span class="anker" id="gl-3-1"></span>
$$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x} \tag{3.1}$$

das __Residuum__ zu $\mathbf{x}$.
:::

Das Wort kommt vom lateinischen Wort für „Rest“. Das Residuum ist genau dann null, wenn $\mathbf{x}$ das System löst. Es ist der Fehlervektor aus [Grundlagen 1, Abschnitt 3.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-5), mit umgekehrtem Vorzeichen; seine Länge ist dieselbe.

⁠**Rechenbeispiel:** Mit den Gewichten $\mathbf{w}=(3,\,10)^{\top}$ aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) ist das Produkt $\mathbf{A}\mathbf{w}=(200,\,130,\,310,\,240)^{\top}$ und das Residuum $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{w}=(0,\,0,\,-20,\,0)^{\top}$ mit der Länge $20$. Drei Preise werden genau getroffen, einer um $20$ Tausend Euro verfehlt.

⁠**Kurz gesagt:** Das Residuum $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ ist der Rest, den ein Vektor $\mathbf{x}$ beim Lösen von $\mathbf{A}\mathbf{x}=\mathbf{y}$ übrig lässt.

### Die beste Näherungslösung

<span class="anker" id="stufe-3-2"></span>

Wenn das Residuum nicht null werden kann, soll es wenigstens so klein wie möglich sein. Das Maß dafür ist seine euklidische Länge.

Man kann sich die Aufgabe geometrisch vorstellen. Lässt man $\mathbf{x}$ alle Vektoren durchlaufen, so durchläuft $\mathbf{A}\mathbf{x}$ nach [Grundlagen 1, Abschnitt 7.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-4), den Spaltenraum von $\mathbf{A}$. Der Abstand $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert$ ist der Abstand des Punkts $\mathbf{y}$ vom Punkt $\mathbf{A}\mathbf{x}$ im Spaltenraum. Gesucht ist also der Punkt des Spaltenraums, der $\mathbf{y}$ am nächsten liegt (Abb. [6](#abb-6)). Im vorigen Abschnitt war der Spaltenraum eine Gerade, jetzt kann er eine Ebene oder ein Spann höherer Dimension sein.

:::definition Definition 3.2 (Beste Näherungslösung)
<span class="anker" id="satz-3-2"></span>

Ein Vektor $\hat{\mathbf{x}}$ heißt __beste Näherungslösung__ des Systems $\mathbf{A}\mathbf{x}=\mathbf{y}$, wenn

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert\le\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\qquad\text{für alle }\mathbf{x} . \tag{3.2}$$
:::

Die Länge ist am kleinsten, wo ihr Quadrat am kleinsten ist, und das Quadrat ist die Summe der quadrierten Komponenten des Residuums. Deshalb spricht man auch von der Lösung nach der *Methode der kleinsten Quadrate*. Hat das System eine exakte Lösung, so ist sie auch die beste Näherungslösung, denn ihr Residuum hat die Länge null.

:::abbildung ml/k2ebene 6
Projektion auf eine Ebene im $\mathbb{R}^3$. Die Spalten $\mathbf{a}_1=(1,0,1)^{\top}$ und $\mathbf{a}_2=(0,1,1)^{\top}$ spannen die Ebene $x_3=x_1+x_2$ auf (blau). Der Punkt $\mathbf{y}=(1,1,1)^{\top}$ liegt nicht in ihr. Der nächste Punkt der Ebene ist $\hat{\mathbf{y}}=(\tfrac23,\tfrac23,\tfrac43)^{\top}$; das Residuum $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(\tfrac13,\tfrac13,-\tfrac13)^{\top}$ steht senkrecht auf der Ebene.
:::

⁠**Rechenbeispiel:** Die Matrix $\mathbf{H}$ aus [Grundlagen 1, Abschnitt 7.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-4), hat die Spalten $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ und $\mathbf{a}_2=(0,\,1,\,1)^{\top}$. Ihr Spaltenraum ist die Ebene aller Vektoren, deren dritte Komponente die Summe der ersten beiden ist. Der Vektor $\mathbf{y}=(1,\,1,\,1)^{\top}$ liegt nicht darin, das System $\mathbf{H}\mathbf{x}=\mathbf{y}$ hat also keine Lösung. Mit $\mathbf{x}=(1,\,0)^{\top}$ ist das Residuum $(0,\,1,\,0)^{\top}$ mit der Länge $1$, mit $\mathbf{x}=(1,\,1)^{\top}$ ist es $(0,\,0,\,-1)^{\top}$, ebenfalls mit der Länge $1$. Ob es besser geht, beantwortet der nächste Unterabschnitt.

⁠**Kurz gesagt:** Die beste Näherungslösung macht das Residuum so kurz wie möglich; geometrisch sucht sie den Punkt des Spaltenraums, der $\mathbf{y}$ am nächsten liegt.

### Die Normalgleichungen

<span class="anker" id="stufe-3-3"></span>

Bei der Geraden war der nächste Punkt der Fußpunkt des Lots: Das Residuum stand senkrecht auf der Geraden. Für einen Spaltenraum liegt dieselbe Bedingung nahe: Das Residuum soll senkrecht auf jedem Vektor des Spaltenraums stehen. Das lässt sich als Gleichungssystem schreiben.

:::herleitung Die Normalgleichungen
Jeder Vektor des Spaltenraums ist eine Linearkombination $\sum_jz_j\mathbf{a}_j$ der Spalten. Steht $\mathbf{r}$ senkrecht auf jeder Spalte, so auch auf jeder solchen Linearkombination, denn $\bigl(\sum_jz_j\mathbf{a}_j\bigr)^{\top}\mathbf{r}=\sum_jz_j\,\mathbf{a}_j^{\top}\mathbf{r}$. Es genügt also, für jede Spalte zu verlangen:

$$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=0\qquad\text{für }j=1,\dots,n .$$

Die Zahlen $\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ sind die Komponenten von $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$, denn die Zeilen von $\mathbf{A}^{\top}$ sind die Spalten von $\mathbf{A}$. Die $n$ Bedingungen lauten also zusammen $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=\mathbf{0}$, ausmultipliziert $\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$.
:::

:::definition Definition 3.3 (Normalgleichungen)
<span class="anker" id="satz-3-3"></span>

Zum System $\mathbf{A}\mathbf{x}=\mathbf{y}$ mit $\mathbf{A}\in\mathbb{R}^{m\times n}$ gehören die __Normalgleichungen__

<span class="anker" id="gl-3-3"></span>
$$\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y} . \tag{3.3}$$
:::

Das Wort „normal“ bedeutet hier „senkrecht“, wie beim Normalenvektor einer Ebene: Die Gleichungen verlangen, dass das Residuum senkrecht auf dem Spaltenraum steht. Die Matrix $\mathbf{A}^{\top}\mathbf{A}$ ist die Gram-Matrix der Spalten aus [Grundlagen 1, Abschnitt 10.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-4); sie ist quadratisch, mit so vielen Zeilen, wie es Unbekannte gibt. Aus einem großen, unlösbaren System mit $m$ Gleichungen wird ein kleines mit $n$ Gleichungen. Für eine einzige Spalte $\mathbf{a}$ steht dort $\mathbf{a}^{\top}\mathbf{a}\,\hat x=\mathbf{a}^{\top}\mathbf{y}$, die Formel aus dem vorigen Abschnitt.

⁠**Rechenbeispiel:** Für $\mathbf{H}$ und $\mathbf{y}=(1,\,1,\,1)^{\top}$ ist

$$\mathbf{H}^{\top}\mathbf{H}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf{H}^{\top}\mathbf{y}=\begin{pmatrix}2\\2\end{pmatrix}.$$

Jeder Eintrag ist ein Skalarprodukt zweier Spalten oder einer Spalte mit $\mathbf{y}$ (Abb. [7](#abb-7)).

:::abbildung ml/k2rnormal 7
Zwei Einträge der Normalgleichungen als Skalarprodukte: Eintrag $(1,2)$ von $\mathbf{H}^{\top}\mathbf{H}$ ist $\mathbf{a}_1^{\top}\mathbf{a}_2$, die erste Komponente von $\mathbf{H}^{\top}\mathbf{y}$ ist $\mathbf{a}_1^{\top}\mathbf{y}$.
:::

Die Normalgleichungen $2\hat x_1+\hat x_2=2$ und $\hat x_1+2\hat x_2=2$ haben die Lösung $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$. Damit ist $\hat{\mathbf{y}}=\mathbf{H}\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}$ und das Residuum $\mathbf{r}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$. Probe: $\mathbf{a}_1^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$ und $\mathbf{a}_2^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$. Die Länge des Residuums ist $\sqrt{3/9}\approx0{,}577$, kürzer als die beiden Versuche im vorigen Unterabschnitt.

⁠**Kurz gesagt:** Die Normalgleichungen $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ verlangen, dass das Residuum senkrecht auf allen Spalten steht.

### Warum die Normalgleichungen die beste Lösung liefern

<span class="anker" id="stufe-3-4"></span>

Dass ein senkrechtes Residuum zum nächsten Punkt gehört, war bei der Geraden der Satz des Pythagoras. Dasselbe Argument trägt hier: Es zerlegt den Fehler in einen Teil, den man durch die Wahl von $\mathbf{x}$ beeinflussen kann, und einen Teil, den man nicht beeinflussen kann.

:::satz Satz 3.4 (Die Normalgleichungen liefern die beste Näherungslösung)
<span class="anker" id="satz-3-4"></span>

Löst $\hat{\mathbf{x}}$ die Normalgleichungen, so gilt für jeden Vektor $\mathbf{x}$

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert^2+\lVert\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})\rVert^2 . \tag{3.4}$$

Also ist $\hat{\mathbf{x}}$ eine beste Näherungslösung. Umgekehrt löst jede beste Näherungslösung die Normalgleichungen, und alle besten Näherungslösungen liefern denselben Punkt $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}$.
:::

:::beweis Beste Näherungslösung
Man zerlegt $\mathbf{y}-\mathbf{A}\mathbf{x}=(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})+\mathbf{A}(\hat{\mathbf{x}}-\mathbf{x})$. Der erste Summand ist das Residuum $\mathbf{r}$ zu $\hat{\mathbf{x}}$, der zweite liegt im Spaltenraum. Nach den Normalgleichungen steht $\mathbf{r}$ senkrecht auf dem Spaltenraum, und der Satz des Pythagoras liefert [(3.4)](#gl-3-4). Der zweite Summand rechts ist nie negativ, also ist $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\ge\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert$ für jedes $\mathbf{x}$.

Ist $\mathbf{x}$ ebenfalls eine beste Näherungslösung, so sind beide Längen gleich, und [(3.4)](#gl-3-4) erzwingt $\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})=\mathbf{0}$. Dann ist $\mathbf{A}\mathbf{x}=\mathbf{A}\hat{\mathbf{x}}$, beide liefern also denselben Punkt und dasselbe Residuum, und $\mathbf{x}$ erfüllt die Normalgleichungen ebenfalls.
:::

⁠**Rechenbeispiel:** Für $\mathbf{H}$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ und $\mathbf{x}=(1,\,0)^{\top}$ ist $\lVert\mathbf{y}-\mathbf{H}\mathbf{x}\rVert^2=1$. Die rechte Seite von [(3.4)](#gl-3-4) ist $\lVert\mathbf{r}\rVert^2=\tfrac13$ plus $\lVert\mathbf{H}(\tfrac13,\,-\tfrac23)^{\top}\rVert^2=\lVert(\tfrac13,\,-\tfrac23,\,-\tfrac13)^{\top}\rVert^2=\tfrac69$, zusammen $\tfrac13+\tfrac23=1$.

⁠**Kurz gesagt:** Pythagoras zerlegt das Fehlerquadrat in das senkrechte Residuum, das keine Wahl von $\mathbf{x}$ verkleinern kann, und einen Teil im Spaltenraum, der bei $\hat{\mathbf{x}}$ verschwindet.

:::hintergrund Was man beeinflussen kann und was nicht
Die Formel [(3.4)](#gl-3-4) erklärt, warum gerade die senkrechte Lage die richtige Bedingung ist. Jeder Kandidat $\mathbf{A}\mathbf{x}$ liegt im Spaltenraum. Der Abstand zu $\mathbf{y}$ setzt sich aus zwei rechtwinklig zueinander liegenden Stücken zusammen: einem Stück im Spaltenraum, von $\mathbf{A}\mathbf{x}$ bis $\hat{\mathbf{y}}$, und dem Stück $\mathbf{r}$ senkrecht dazu, von $\hat{\mathbf{y}}$ bis $\mathbf{y}$. Das erste Stück kann man durch die Wahl von $\mathbf{x}$ beliebig verändern und insbesondere auf null bringen. Das zweite hängt von $\mathbf{x}$ gar nicht ab: Es ist der Teil von $\mathbf{y}$, den die Spalten mit keiner Linearkombination erreichen. Die beste Näherungslösung ist genau die, die das beeinflussbare Stück null macht. Dass die beiden Stücke sich nach Pythagoras addieren und nicht gegenseitig ausgleichen können, liegt an ihrem rechten Winkel.
:::

### Wann die beste Näherungslösung eindeutig ist

<span class="anker" id="stufe-3-5"></span>

Die Normalgleichungen sind ein quadratisches System. Ob es genau eine Lösung hat, hängt davon ab, ob $\mathbf{A}^{\top}\mathbf{A}$ invertierbar ist. Das wiederum entscheiden die Spalten von $\mathbf{A}$.

:::satz Satz 3.5 (Invertierbarkeit von $\mathbf{A}^{\top}\mathbf{A}$)
<span class="anker" id="satz-3-5"></span>

Die Matrix $\mathbf{A}^{\top}\mathbf{A}$ ist genau dann invertierbar, wenn die Spalten von $\mathbf{A}$ linear unabhängig sind. Dann ist die beste Näherungslösung eindeutig:

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y} . \tag{3.5}$$
:::

:::beweis Invertierbarkeit
Nach [Grundlagen 1, Abschnitt 13.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), ist die quadratische Matrix $\mathbf{A}^{\top}\mathbf{A}$ genau dann invertierbar, wenn ihr Kern nur den Nullvektor enthält. Es sei $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Dann ist auch $\mathbf{z}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=0$, also $\lVert\mathbf{A}\mathbf{z}\rVert^2=0$ und $\mathbf{A}\mathbf{z}=\mathbf{0}$. Umgekehrt folgt aus $\mathbf{A}\mathbf{z}=\mathbf{0}$ sofort $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Die beiden Kerne sind also gleich. Der Kern von $\mathbf{A}$ enthält genau dann nur den Nullvektor, wenn die Spalten von $\mathbf{A}$ linear unabhängig sind.
:::

Sind die Spalten linear abhängig, so gibt es unendlich viele beste Näherungslösungen. Zu einer von ihnen darf man jeden Vektor aus dem Kern von $\mathbf{A}$ addieren, ohne $\mathbf{A}\hat{\mathbf{x}}$ zu ändern. Der nächste Punkt $\hat{\mathbf{y}}$ ist trotzdem eindeutig, wie der Satz im vorigen Unterabschnitt zeigt. Das passt zu [Grundlagen 1, Abschnitt 13.6](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6): Abhängige Merkmale machen die Gewichte mehrdeutig, nicht aber die Vorhersagen.

⁠**Rechenbeispiel 1:** Die Spalten von $\mathbf{H}$ sind linear unabhängig, und $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ hat die Inverse $\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$. Mit [(3.5)](#gl-3-5) ist $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(2,\,2)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$, wie oben.

⁠**Rechenbeispiel 2:** Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ und $\mathbf{y}=(1,\,1)^{\top}$ sind die Spalten abhängig. Die Normalgleichungen lauten $\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)\hat{\mathbf{x}}=(3,\,6)^{\top}$, also zweimal dieselbe Gleichung $\hat x_1+2\hat x_2=\tfrac35$. Jeder Punkt dieser Geraden ist eine beste Näherungslösung, etwa $(\tfrac35,\,0)^{\top}$ oder $(0,\,\tfrac3{10})^{\top}$. Alle liefern denselben Punkt $\hat{\mathbf{y}}=(\tfrac35,\,\tfrac65)^{\top}$, die Projektion von $\mathbf{y}$ auf die Gerade in Richtung $(1,\,2)^{\top}$.

⁠**Kurz gesagt:** Bei linear unabhängigen Spalten ist $\mathbf{A}^{\top}\mathbf{A}$ invertierbar und die beste Näherungslösung $\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ eindeutig; sonst gibt es unendlich viele, die alle denselben nächsten Punkt liefern.

### Eine Gerade durch drei Punkte

<span class="anker" id="stufe-3-6"></span>

Jetzt ist die Theorie vollständig, und sie lässt sich auf eine alltägliche Aufgabe anwenden. Drei Messpunkte $(t,\,y)=(0,\,1)$, $(1,\,2)$ und $(2,\,4)$ sollen durch eine Gerade $y=x_1+x_2\,t$ beschrieben werden. Die drei Punkte liegen nicht auf einer gemeinsamen Geraden. Gesucht sind der Achsenabschnitt $x_1$ und die Steigung $x_2$, die am besten passen.

Jeder Messpunkt liefert eine Gleichung $x_1+x_2\,t_i=y_i$. Mit der Einsenspalte für den Achsenabschnitt, wie in [Grundlagen 1, Abschnitt 8.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-5), ist das das System

$$\mathbf{A}\mathbf{x}=\mathbf{y}\qquad\text{mit}\qquad \mathbf{A}=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}1\\2\\4\end{pmatrix}.$$

Die Komponenten des Residuums sind die senkrechten Abstände der Messpunkte von der Geraden, gemessen in $y$-Richtung (Abb. [8](#abb-8)). Die beste Näherungslösung macht die Summe ihrer Quadrate so klein wie möglich. Eine solche Gerade heißt __Ausgleichsgerade__.

:::abbildung ml/k2ausgleich 8
Die Ausgleichsgerade durch die Messpunkte $(0,1)$, $(1,2)$ und $(2,4)$. Die roten Strecken sind die Komponenten des Residuums, die senkrechten Abstände der Punkte von der Geraden in $y$-Richtung. Die Gerade macht die Summe ihrer Quadrate so klein wie möglich, hier $\tfrac1{36}+\tfrac19+\tfrac1{36}=\tfrac16$.
:::

⁠**Rechenbeispiel:** Es ist

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&3\\3&5\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}7\\10\end{pmatrix},\qquad (\mathbf{A}^{\top}\mathbf{A})^{-1}=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix},$$

also $\hat{\mathbf{x}}=\tfrac16(35-30,\ -21+30)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$. Die Einträge von $\mathbf{A}^{\top}\mathbf{A}$ und $\mathbf{A}^{\top}\mathbf{y}$ sind Summen über die Messpunkte; zwei davon zeigt Abb. [9](#abb-9). Die Ausgleichsgerade ist $y=\tfrac56+\tfrac32\,t$. Ihre Werte an den Messstellen sind $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\,\tfrac73,\,\tfrac{23}6)^{\top}$, das Residuum ist $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$ mit der Quadratsumme $\tfrac16$. Probe: $\mathbf{A}^{\top}\mathbf{r}=(\tfrac16-\tfrac13+\tfrac16,\ 0-\tfrac13+\tfrac13)^{\top}=(0,\,0)^{\top}$.

Die erste Komponente der Probe hat eine eigene Bedeutung. Die erste Spalte von $\mathbf{A}$ ist die Einsenspalte, und $\mathbf{1}^{\top}\mathbf{r}=0$ heißt: Die Residuen addieren sich zu null. Die Gerade liegt im Mittel weder zu hoch noch zu tief. Gleichwertig geht sie durch den Schwerpunkt der Messpunkte, hier $(\bar t,\,\bar y)=(1,\,\tfrac73)$: Es ist $\tfrac56+\tfrac32\cdot1=\tfrac73$.

:::abbildung ml/k2rausgleich 9
Zwei Einträge der Normalgleichungen der Ausgleichsgeraden als Summen über die drei Messpunkte $(t_i,\,y_i)=(0,1)$, $(1,2)$, $(2,4)$.
:::

⁠**Kurz gesagt:** Eine Ausgleichsgerade ist die beste Näherungslösung des Systems, das verlangt, dass alle Messpunkte auf der Geraden liegen; mit einer Einsenspalte addieren sich ihre Residuen zu null.

:::hintergrund Ein Filter, das ein Signal möglichst gut nachbildet
Dieselbe Rechnung entwirft digitale Filter. Ein Filter mit den Koeffizienten $h_0,\dots,h_{K-1}$ soll aus einem Eingangssignal $x[n]$ ein gewünschtes Signal $d[n]$ möglichst gut nachbilden, mit dem Ausgang $\sum_kh_k\,x[n-k]$. Für jeden Takt $n$ ist das eine Gleichung für die $K$ Unbekannten $h_k$, für viele Takte also ein überbestimmtes System $\mathbf{X}\mathbf h=\mathbf d$. Die Zeile $n$ von $\mathbf{X}$ enthält $x[n],x[n-1],\dots,x[n-K+1]$. In den Normalgleichungen $\mathbf{X}^{\top}\mathbf{X}\mathbf h=\mathbf{X}^{\top}\mathbf d$ steht im Eintrag $(k,l)$ von $\mathbf{X}^{\top}\mathbf{X}$ die Summe $\sum_nx[n-k]\,x[n-l]$, bis auf Randeffekte am Anfang und Ende des Signals also die Autokorrelation von $x$ bei der Verschiebung $l-k$. In $\mathbf{X}^{\top}\mathbf d$ steht die Kreuzkorrelation von $d$ und $x$. Das sind genau die Skalarprodukte verschobener Signale aus [Grundlagen 1, Abschnitt 2.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-4). Das Residuum $d[n]-\sum_kh_k\,x[n-k]$ des besten Filters steht nach [(3.3)](#gl-3-3) senkrecht auf jedem verschobenen Eingangssignal: Was das Filter nicht nachbilden kann, hat mit keinem der Signale, aus denen es den Ausgang zusammensetzt, etwas gemeinsam.
:::

### Die Wohnungen: was Grundlagen 1 offen ließ

<span class="anker" id="stufe-3-7"></span>

Jetzt lässt sich die Frage vom Anfang des Abschnitts beantworten. Gesucht sind die Gewichte für Fläche und Zimmerzahl, die die vier Preise so gut wie möglich treffen.

⁠**Rechenbeispiel:** Für das System $\mathbf{A}\mathbf{w}=\mathbf{y}$ aus dem ersten Unterabschnitt ist

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}18\,200&730\\730&30\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}60\,100\\2\,410\end{pmatrix}.$$

Abb. [10](#abb-10) rechnet zwei der Einträge vor.

:::abbildung ml/k2rwohnungen 10
Zwei Einträge der Normalgleichungen der Wohnungen als Skalarprodukte: $\mathbf{a}_1=(60,40,90,70)^{\top}$ ist die Flächenspalte, $\mathbf{a}_2=(2,1,4,3)^{\top}$ die Zimmerspalte, $\mathbf{y}=(200,130,290,240)^{\top}$ der Preisvektor.
:::

Die beiden Spalten sind linear unabhängig, die Determinante ist $18\,200\cdot30-730^2=13\,100$. Mit der Inversen aus [Grundlagen 1, Abschnitt 11.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-3), ist

$$\hat{\mathbf{w}}=\frac1{13\,100}\begin{pmatrix}30&-730\\-730&18\,200\end{pmatrix}\begin{pmatrix}60\,100\\2\,410\end{pmatrix}=\frac1{13\,100}\begin{pmatrix}43\,700\\-11\,000\end{pmatrix}=\begin{pmatrix}437/131\\-110/131\end{pmatrix}\approx\begin{pmatrix}3{,}336\\-0{,}840\end{pmatrix}.$$

Die geschätzten Preise sind $\mathbf{A}\hat{\mathbf{w}}\approx(198{,}47;\ 132{,}60;\ 296{,}87;\ 230{,}99)^{\top}$, das Residuum ist

$$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{w}}=\frac{20}{131}\,(10,\,-17,\,-45,\,59)^{\top}\approx(1{,}53;\ -2{,}60;\ -6{,}87;\ 9{,}01)^{\top}$$

mit der Länge $\lVert\mathbf{r}\rVert\approx11{,}72$. Die Gewichte $(3,\,10)^{\top}$ aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) trafen drei Preise genau, ließen aber ein Residuum der Länge $20$. Die beste Näherungslösung trifft keinen Preis genau, liegt aber insgesamt deutlich weniger daneben. Probe: $\mathbf{A}^{\top}\mathbf{r}=\frac{20}{131}(600-680-4050+4130,\ 20-17-180+177)^{\top}=\mathbf{0}$.

⁠**Kurz gesagt:** Die beste Näherungslösung für die Wohnungen sind die Gewichte $\hat{\mathbf{w}}\approx(3{,}336;\ -0{,}840)^{\top}$; ihr Residuum ist mit $11{,}72$ deutlich kürzer als jedes Residuum, das drei Preise genau trifft.

:::hintergrund Warum das Gewicht der Zimmer negativ ist
Ein negatives Gewicht für die Zimmerzahl sieht zunächst falsch aus: Mehr Zimmer sollten den Preis nicht senken. Die Rechnung ist trotzdem richtig, und der Grund liegt in den Daten. In diesen vier Wohnungen wachsen Fläche und Zimmerzahl gemeinsam: Je größer die Wohnung, desto mehr Zimmer hat sie. Die beiden Spalten von $\mathbf{A}$ zeigen deshalb fast in dieselbe Richtung; nach [Grundlagen 1, Abschnitt 5.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2), ist der Kosinus ihres Winkels $730/\sqrt{18\,200\cdot30}\approx0{,}988$, der Winkel also nur etwa $8{,}9^\circ$. Die beste Kombination nimmt viel von der Flächenspalte und zieht ein wenig von der Zimmerspalte wieder ab, um die Abweichungen der Wohnungen vom gemeinsamen Verhältnis auszugleichen. Bei gleicher Fläche bedeuten mehr Zimmer hier kleinere Zimmer, und das kann einen Preis tatsächlich senken; ob das stimmt, können vier Wohnungen aber nicht zeigen. Wie in [Grundlagen 1, Abschnitt 13.6](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6), gilt: Wenn Merkmale fast dieselbe Information tragen, sagen die einzelnen Gewichte wenig, die Vorhersagen dagegen viel.
:::

:::aufgabe Aufgabe 7 ★ Normalgleichungen von Hand
<span class="anker" id="aufg-7"></span>

Das System $x_1=1$, $x_2=2$, $x_1+x_2=6$ hat keine Lösung.

<ol class="al">

<li>

Schreibe es als $\mathbf{A}\mathbf{x}=\mathbf{y}$, stelle die Normalgleichungen auf und löse sie.

</li>

<li>

Berechne das Residuum und prüfe, dass es senkrecht auf beiden Spalten steht. Um wie viel verfehlt die beste Näherungslösung jede der drei Gleichungen?

</li>

</ol>

:::loesung
(a) Mit $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ und $\mathbf{y}=(1,\,2,\,6)^{\top}$ ist $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ und $\mathbf{A}^{\top}\mathbf{y}=(1+6,\ 2+6)^{\top}=(7,\,8)^{\top}$. Die Normalgleichungen $2\hat x_1+\hat x_2=7$, $\hat x_1+2\hat x_2=8$ haben die Lösung

$$\hat{\mathbf{x}}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix}=\frac13\begin{pmatrix}6\\9\end{pmatrix}=\begin{pmatrix}2\\3\end{pmatrix}.$$

(b) $\mathbf{A}\hat{\mathbf{x}}=(2,\,3,\,5)^{\top}$ und $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}=(-1,\,-1,\,1)^{\top}$. Probe: $\mathbf{a}_1^{\top}\mathbf{r}=-1+0+1=0$ und $\mathbf{a}_2^{\top}\mathbf{r}=0-1+1=0$. Jede der drei Gleichungen wird um genau $1$ verfehlt: $\hat x_1=2$ statt $1$, $\hat x_2=3$ statt $2$, $\hat x_1+\hat x_2=5$ statt $6$. Die beste Näherungslösung verteilt den Widerspruch gleichmäßig; $\lVert\mathbf{r}\rVert^2=3$.
:::
:::

:::aufgabe Aufgabe 8 ★★ Eine Ausgleichsgerade
<span class="anker" id="aufg-8"></span>

Bestimme die Ausgleichsgerade $y=x_1+x_2\,t$ durch die Punkte $(1,\,2)$, $(2,\,3)$ und $(3,\,5)$. Berechne das Residuum, prüfe $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ und zeige, dass die Gerade durch den Schwerpunkt der drei Punkte geht.

:::loesung
Mit $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&2\\1&3\end{smallmatrix}\Bigr)$ und $\mathbf{y}=(2,\,3,\,5)^{\top}$ ist

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&6\\6&14\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}10\\23\end{pmatrix},\qquad \hat{\mathbf{x}}=\frac16\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}10\\23\end{pmatrix}=\frac16\begin{pmatrix}2\\9\end{pmatrix}=\begin{pmatrix}1/3\\3/2\end{pmatrix}.$$

Die Ausgleichsgerade ist $y=\tfrac13+\tfrac32\,t$, mit den Werten $\tfrac{11}6$, $\tfrac{10}3$, $\tfrac{29}6$ an den Messstellen. Das Residuum ist $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$, und $\mathbf{A}^{\top}\mathbf{r}=\bigl(\tfrac16-\tfrac13+\tfrac16,\ \tfrac16-\tfrac23+\tfrac12\bigr)^{\top}=(0,\,0)^{\top}$. Der Schwerpunkt ist $(\bar t,\,\bar y)=(2,\,\tfrac{10}3)$, und $\tfrac13+\tfrac32\cdot2=\tfrac{10}3$: Die Gerade geht durch ihn. Das folgt aus der ersten Komponente von $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$: Die Residuen summieren sich zu null, also ist $\bar y=\hat x_1+\hat x_2\,\bar t$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Grundpreis und Preis pro Quadratmeter
<span class="anker" id="aufg-9"></span>

Die vier Wohnungen sollen nur über ihre Fläche geschätzt werden, mit einem Grundpreis: $y\approx x_1+x_2\cdot\text{Fläche}$.

<ol class="al">

<li>

Stelle $\mathbf{A}$ mit der Einsenspalte auf und löse die Normalgleichungen.

</li>

<li>

Berechne das Residuum und seine Länge. Vergleiche mit dem Ergebnis im letzten Unterabschnitt.

</li>

</ol>

:::loesung
(a) Die Matrix hat die Einsenspalte und die Flächenspalte:

$$\mathbf{A}=\begin{pmatrix}1&60\\1&40\\1&90\\1&70\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}4&260\\260&18\,200\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}860\\60\,100\end{pmatrix}.$$

Die Determinante ist $4\cdot18\,200-260^2=72\,800-67\,600=5\,200$, und

$$\hat{\mathbf{x}}=\frac1{5\,200}\begin{pmatrix}18\,200&-260\\-260&4\end{pmatrix}\begin{pmatrix}860\\60\,100\end{pmatrix}=\frac1{5\,200}\begin{pmatrix}26\,000\\16\,800\end{pmatrix}=\begin{pmatrix}5\\42/13\end{pmatrix}\approx\begin{pmatrix}5\\3{,}231\end{pmatrix}.$$

Der Grundpreis ist $5$ Tausend Euro, dazu kommen etwa $3{,}23$ Tausend Euro pro Quadratmeter.

(b) Die geschätzten Preise sind $5+\tfrac{42}{13}\cdot\text{Fläche}$, und das Residuum ist

$$\mathbf{r}=\tfrac1{13}\,(15,\,-55,\,-75,\,115)^{\top}\approx(1{,}15;\ -4{,}23;\ -5{,}77;\ 8{,}85)^{\top},\qquad \lVert\mathbf{r}\rVert=\tfrac1{13}\sqrt{22\,100}\approx11{,}44 .$$

Die Residuen summieren sich zu null, wie es die Einsenspalte verlangt. Mit Fläche und Zimmerzahl war $\lVert\mathbf{r}\rVert\approx11{,}72$; Grundpreis und Fläche passen also bei ebenfalls zwei Unbekannten etwas besser. Welche zwei Spalten man wählt, verändert den Spaltenraum und damit den nächsten Punkt.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Residuen ohne Einsenspalte
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Zeige: Enthält der Spaltenraum von $\mathbf{A}$ den Einsvektor $\mathbf{1}$, so addieren sich die Komponenten des Residuums der besten Näherungslösung zu null.

</li>

<li>

Prüfe am Residuum der Wohnungen aus dem letzten Unterabschnitt, dass ohne Einsenspalte die Summe der Residuen im Allgemeinen nicht null ist.

</li>

</ol>

:::loesung
(a) Liegt $\mathbf{1}$ im Spaltenraum, so steht das Residuum der besten Näherungslösung nach den Normalgleichungen senkrecht auf $\mathbf{1}$, denn es steht senkrecht auf dem ganzen Spaltenraum. Also ist $\mathbf{1}^{\top}\mathbf{r}=\sum_ir_i=0$.

(b) Das Residuum der Wohnungen ist $\tfrac{20}{131}(10,\,-17,\,-45,\,59)^{\top}$ mit der Summe $\tfrac{20}{131}(10-17-45+59)=\tfrac{140}{131}\approx1{,}07\ne0$. Ohne Einsenspalte liegt $\mathbf{1}$ hier nicht im Spaltenraum, und die Residuen müssen sich nicht ausgleichen.
:::
:::
