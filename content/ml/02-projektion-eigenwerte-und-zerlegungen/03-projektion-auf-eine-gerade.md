---
title: Projektion auf eine Gerade
pfad: Informatik / Machine Learning / Projektion, Eigenwerte und Zerlegungen
order: 6220300
summary: Ein Punkt liegt neben einer Geraden.
tags: orthogonale Projektion, Projektionsmatrix, Projektion
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Punkt liegt neben einer Geraden. Welcher Punkt der Geraden liegt ihm am nächsten? Dieser Abschnitt beantwortet die Frage für Geraden durch den Nullpunkt, in jeder Dimension. Die Antwort ist der Fußpunkt des Lots, und der Grund dafür ist der Satz des Pythagoras.
:::

### Der Fußpunkt des Lots

<span class="anker" id="stufe-2-1"></span>

Eine Gerade durch den Nullpunkt besteht aus allen Vielfachen $t\,\mathbf{a}$ eines Richtungsvektors $\mathbf{a}\ne\mathbf{0}$. Gegeben ist ein Punkt $\mathbf{y}$, der nicht auf ihr liegen muss. Gesucht ist der Punkt der Geraden, der $\mathbf{y}$ am nächsten liegt.

In [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 5.5, warf ein Pfeil bei senkrechtem Lichteinfall einen Schatten auf eine Gerade. Der Endpunkt des Schattens ist der Punkt, an dem das Lot von $\mathbf{y}$ auf die Gerade trifft, der *Fußpunkt des Lots*. Die Verbindung von diesem Punkt zu $\mathbf{y}$ steht senkrecht auf der Geraden (Abb. [4](#abb-4)). Dass er der nächste Punkt ist, zeigt der nächste Unterabschnitt. Hier wird er zuerst ausgerechnet, und zwar auch dann, wenn $\mathbf{a}$ nicht normiert ist.

:::herleitung Der Fußpunkt des Lots
Der gesuchte Punkt liegt auf der Geraden, ist also $\hat x\,\mathbf{a}$ mit einer noch unbekannten Zahl $\hat x$. Die Verbindung $\mathbf{y}-\hat x\,\mathbf{a}$ soll senkrecht auf $\mathbf{a}$ stehen:

$$\mathbf{a}^{\top}(\mathbf{y}-\hat x\,\mathbf{a})=0\qquad\Longleftrightarrow\qquad \mathbf{a}^{\top}\mathbf{y}-\hat x\,\mathbf{a}^{\top}\mathbf{a}=0\qquad\Longleftrightarrow\qquad \hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} .$$

Wegen $\mathbf{a}\ne\mathbf{0}$ ist $\mathbf{a}^{\top}\mathbf{a}=\lVert\mathbf{a}\rVert^2>0$, die Division ist also erlaubt, und es gibt genau ein solches $\hat x$.
:::

:::definition Definition 2.1 (Projektion auf eine Gerade)
<span class="anker" id="satz-2-1"></span>

Es sei $\mathbf{a}\in\mathbb{R}^n$, $\mathbf{a}\ne\mathbf{0}$. Die __orthogonale Projektion__ von $\mathbf{y}\in\mathbb{R}^n$ auf die Gerade durch den Nullpunkt in Richtung $\mathbf{a}$ ist der Punkt

<span class="anker" id="gl-2-1"></span>
$$\hat{\mathbf{y}}=\hat x\,\mathbf{a}\qquad\text{mit}\qquad\hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} . \tag{2.1}$$
:::

Der Punkt $\hat{\mathbf{y}}$ ist ein Vektor im $\mathbb{R}^n$; die Zahl $\hat x$ ist seine Koordinate längs $\mathbf{a}$. Beides darf man nicht verwechseln. Ist $\mathbf{a}$ normiert, so ist $\mathbf{a}^{\top}\mathbf{a}=1$ und $\hat{\mathbf{y}}=(\mathbf{a}^{\top}\mathbf{y})\,\mathbf{a}$, genau der Schattenpunkt aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html).

:::abbildung ml/k2lot 4
Die Projektion von $\mathbf{y}=(4,3)^{\top}$ auf die Gerade in Richtung $\mathbf{a}=(1,2)^{\top}$. Der Fußpunkt des Lots ist $\hat{\mathbf{y}}=2\mathbf{a}=(2,4)^{\top}$, die Verbindung $\mathbf{r}=(2,-1)^{\top}$ (blau) steht senkrecht auf der Geraden. Ein anderer Punkt der Geraden, etwa $(1,2)^{\top}$, ist weiter von $\mathbf{y}$ entfernt (gestrichelt): Das Dreieck aus $\mathbf{y}$, $\hat{\mathbf{y}}$ und $(1,2)^{\top}$ hat bei $\hat{\mathbf{y}}$ einen rechten Winkel, und die gestrichelte Seite ist seine Hypotenuse.
:::

⁠**Rechenbeispiel 1:** Für $\mathbf{a}=(1,\,2)^{\top}$ und $\mathbf{y}=(4,\,3)^{\top}$ ist $\mathbf{a}^{\top}\mathbf{y}=4+6=10$ und $\mathbf{a}^{\top}\mathbf{a}=5$ (Abb. [5](#abb-5)), also $\hat x=2$ und $\hat{\mathbf{y}}=(2,\,4)^{\top}$. Die Verbindung $\mathbf{y}-\hat{\mathbf{y}}=(2,\,-1)^{\top}$ steht senkrecht auf $\mathbf{a}$: $2-2=0$.

:::abbildung ml/k2rproj 5
Die beiden Skalarprodukte der Projektion Schritt für Schritt: $\mathbf{a}^{\top}\mathbf{y}=10$ im Zähler und $\mathbf{a}^{\top}\mathbf{a}=5$ im Nenner von $\hat x$.
:::

⁠**Rechenbeispiel 2:** Für $\mathbf{a}=(3,\,4)^{\top}$ und $\mathbf{y}=(3,\,1)^{\top}$ ist $\hat x=(9+4)/25=0{,}52$ und $\hat{\mathbf{y}}=0{,}52\,(3,\,4)^{\top}=(1{,}56;\ 2{,}08)^{\top}$, derselbe Schattenpunkt wie in [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html) mit dem normierten Vektor $(0{,}6;\ 0{,}8)^{\top}=\mathbf{a}/5$. Die Länge des Richtungsvektors spielt keine Rolle: Ersetzt man $\mathbf{a}$ durch $c\,\mathbf{a}$ mit $c\ne0$, so wird $\hat x$ zu $\hat x/c$, und $\hat{\mathbf{y}}$ bleibt gleich. Verdoppelt man dagegen $\mathbf{y}$, so verdoppelt sich auch $\hat{\mathbf{y}}$.

⁠**Kurz gesagt:** Die Projektion von $\mathbf{y}$ auf die Gerade in Richtung $\mathbf{a}$ ist der Fußpunkt des Lots, $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$.

### Der Fußpunkt ist der nächste Punkt

<span class="anker" id="stufe-2-2"></span>

Bisher ist nur gezeigt, dass die Verbindung zum Fußpunkt senkrecht steht. Dass er auch der nächste Punkt ist, folgt aus dem Satz des Pythagoras: Wer auf der Geraden vom Fußpunkt weggeht, fügt zur senkrechten Verbindung ein Stück in Richtung der Geraden hinzu, und das kann den Abstand nur vergrößern.

:::satz Satz 2.2 (Der Fußpunkt ist der nächste Punkt)
<span class="anker" id="satz-2-2"></span>

Es sei $\hat{\mathbf{y}}=\hat x\,\mathbf{a}$ die Projektion von $\mathbf{y}$ auf die Gerade in Richtung $\mathbf{a}$. Für jede Zahl $t$ gilt

<span class="anker" id="gl-2-2"></span>
$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2=\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2+(t-\hat x)^2\,\lVert\mathbf{a}\rVert^2 . \tag{2.2}$$

Insbesondere ist $\hat{\mathbf{y}}$ der eindeutige Punkt der Geraden mit dem kleinsten Abstand zu $\mathbf{y}$.
:::

:::beweis Der nächste Punkt
Man schreibt die Verbindung von $t\,\mathbf{a}$ zu $\mathbf{y}$ als Summe zweier Pfeile:

$$\mathbf{y}-t\,\mathbf{a}=(\mathbf{y}-\hat{\mathbf{y}})+(\hat x-t)\,\mathbf{a} .$$

Der erste Summand steht nach der Herleitung senkrecht auf $\mathbf{a}$, also auch auf dem zweiten. Nach dem Satz des Pythagoras aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 5.3, ist das Längenquadrat der Summe die Summe der Längenquadrate, und das ist [(2.2)](#gl-2-2). Der zweite Summand auf der rechten Seite ist nie negativ und nur für $t=\hat x$ null. Also ist der Abstand genau für $t=\hat x$ am kleinsten.
:::

Für die Länge des Fußpunkts gilt $\lVert\hat{\mathbf{y}}\rVert=|\hat x|\,\lVert\mathbf{a}\rVert=|\mathbf{a}^{\top}\mathbf{y}|/\lVert\mathbf{a}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$, wobei $\varphi$ der Winkel zwischen $\mathbf{a}$ und $\mathbf{y}$ ist. Das ist die Ankathete im rechtwinkligen Dreieck mit der Hypotenuse $\mathbf{y}$.

⁠**Rechenbeispiel:** Im ersten Rechenbeispiel des vorigen Unterabschnitts ist $\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2=\lVert(2,\,-1)^{\top}\rVert^2=5$. Für den Punkt $t=1$, also $(1,\,2)^{\top}$, sagt [(2.2)](#gl-2-2) das Abstandsquadrat $5+1\cdot5=10$ voraus, und tatsächlich ist $\lVert(3,\,1)^{\top}\rVert^2=10$. Für $t=3$, also $(3,\,6)^{\top}$, ist es ebenfalls $5+1\cdot5=10=\lVert(1,\,-3)^{\top}\rVert^2$. Beide Punkte liegen gleich weit vom Fußpunkt entfernt, auf verschiedenen Seiten.

⁠**Kurz gesagt:** Der nächste Punkt einer Geraden ist der Fußpunkt des Lots, weil jeder Schritt längs der Geraden nach Pythagoras das Abstandsquadrat vergrößert.

:::hintergrund Warum es genau einen nächsten Punkt gibt und dass das an der euklidischen Norm liegt
Der Beweis benutzt den Satz des Pythagoras, und der gilt nur für Normen, die aus einem Skalarprodukt kommen. In [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 3.4, stellte sich heraus, dass die Betragssummennorm keine solche Norm ist. Mit ihr geht die Eindeutigkeit tatsächlich verloren. Beispiel: die Gerade in Richtung $\mathbf{a}=(1,\,1)^{\top}$ und der Punkt $\mathbf{y}=(1,\,0)^{\top}$. Für $0\le t\le1$ ist

$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert_1=|1-t|+|0-t|=(1-t)+t=1 ,$$

also gleich groß für alle Punkte zwischen $\mathbf{0}$ und $\mathbf{a}$; außerhalb dieser Strecke ist der Abstand größer. Es gibt in dieser Norm eine ganze Strecke nächster Punkte. In der euklidischen Norm ist es genau einer: $\hat x=\tfrac12$, der Punkt $(\tfrac12,\,\tfrac12)^{\top}$. Die eindeutige, mit einer einfachen Formel berechenbare Projektion ist einer der Gründe, warum so viele Verfahren den euklidischen Abstand benutzen.
:::

### Die Projektionsmatrix

<span class="anker" id="stufe-2-3"></span>

Die Vorschrift $\mathbf{y}\mapsto\hat{\mathbf{y}}$ ist linear: Die Summe zweier Punkte wird auf die Summe ihrer Projektionen abgebildet, ein Vielfaches auf das Vielfache. Nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 8.2, hat sie also eine Matrix. Man liest sie direkt ab, wenn man die Zahl $\mathbf{a}^{\top}\mathbf{y}$ an die andere Seite von $\mathbf{a}$ schreibt und das Matrixprodukt umklammert:

$$\hat{\mathbf{y}}=\mathbf{a}\,\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{y} .$$

Im Zähler steht das äußere Produkt aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 9.5.

:::definition Definition 2.3 (Projektionsmatrix einer Geraden)
<span class="anker" id="satz-2-3"></span>

Für $\mathbf{a}\ne\mathbf{0}$ heißt

<span class="anker" id="gl-2-3"></span>
$$\mathbf{P}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}} \tag{2.3}$$

die __Projektionsmatrix__ auf die Gerade in Richtung $\mathbf{a}$. Es ist $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$.
:::

:::satz Satz 2.4 (Eigenschaften der Projektionsmatrix einer Geraden)
<span class="anker" id="satz-2-4"></span>

Es gilt $\mathbf{P}^{\top}=\mathbf{P}$ und $\mathbf{P}^2=\mathbf{P}$. Punkte der Geraden bleiben, wo sie sind: $\mathbf{P}\mathbf{a}=\mathbf{a}$. Vektoren senkrecht zu $\mathbf{a}$ werden auf $\mathbf{0}$ abgebildet. Der Rang von $\mathbf{P}$ ist $1$.
:::

:::beweis Eigenschaften
$(\mathbf{a}\mathbf{a}^{\top})^{\top}=\mathbf{a}\mathbf{a}^{\top}$, also ist $\mathbf{P}$ symmetrisch. Weiter ist $\mathbf{P}^2=\mathbf{a}(\mathbf{a}^{\top}\mathbf{a})\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})^2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{P}$, weil $\mathbf{a}^{\top}\mathbf{a}$ eine Zahl ist. $\mathbf{P}\mathbf{a}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{a})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{a}$. Ist $\mathbf{a}^{\top}\mathbf{z}=0$, so ist $\mathbf{P}\mathbf{z}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{z})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{0}$. Jede Spalte von $\mathbf{P}$ ist ein Vielfaches von $\mathbf{a}$, also ist der Rang $1$.
:::

Die Gleichung $\mathbf{P}^2=\mathbf{P}$ hat eine einfache Bedeutung: Wer schon auf der Geraden steht, bleibt beim zweiten Projizieren stehen.

⁠**Rechenbeispiel:** Für $\mathbf{a}=(1,\,2)^{\top}$ ist

$$\mathbf{P}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad \mathbf{P}\begin{pmatrix}4\\3\end{pmatrix}=\frac15\begin{pmatrix}4+6\\8+12\end{pmatrix}=\begin{pmatrix}2\\4\end{pmatrix}.$$

Probe für $\mathbf{P}^2=\mathbf{P}$: $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)^2=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)=5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, also $\mathbf{P}^2=\frac1{25}\cdot5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=\mathbf{P}$. Die Matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ war in [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 11.5, das Beispiel einer Matrix ohne Inverse. Jetzt ist klar, was sie tut: Sie ist das Fünffache einer Projektion und drückt die Ebene auf die Gerade in Richtung $(1,\,2)^{\top}$ platt.

⁠**Kurz gesagt:** Die Projektion auf eine Gerade ist das Matrix-Vektor-Produkt mit $\mathbf{P}=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$; diese Matrix ist symmetrisch und erfüllt $\mathbf{P}^2=\mathbf{P}$.

### Projektionen im Allgemeinen

<span class="anker" id="stufe-2-4"></span>

Schatten gibt es auch bei schräg einfallendem Licht. Dann ist der Schatten eines Punkts auf einer Geraden nicht mehr der Fußpunkt des Lots, aber er liegt immer noch auf der Geraden, und ein Punkt, der schon auf der Geraden liegt, wirft sich selbst als Schatten. Die Eigenschaft $\mathbf{P}^2=\mathbf{P}$ bleibt also erhalten, die Symmetrie nicht.

:::definition Definition 2.5 (Projektion)
<span class="anker" id="satz-2-5"></span>

Eine quadratische Matrix $\mathbf{P}$ mit $\mathbf{P}^2=\mathbf{P}$ heißt __Projektion__. Sie heißt orthogonale Projektion, wenn außerdem für alle $\mathbf{y}$ die Verbindung $\mathbf{y}-\mathbf{P}\mathbf{y}$ senkrecht auf allen Bildern $\mathbf{P}\mathbf{z}$ steht.
:::

:::satz Satz 2.6 (Orthogonal heißt symmetrisch)
<span class="anker" id="satz-2-6"></span>

Eine Projektion $\mathbf{P}$ ist genau dann eine orthogonale Projektion, wenn $\mathbf{P}^{\top}=\mathbf{P}$ ist.
:::

:::beweis Orthogonal heißt symmetrisch
Für alle $\mathbf{y},\mathbf{z}$ ist $(\mathbf{y}-\mathbf{P}\mathbf{y})^{\top}\mathbf{P}\mathbf{z}=\mathbf{y}^{\top}(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}\mathbf{z}$. Ist $\mathbf{P}^{\top}=\mathbf{P}$, so ist $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}=\mathbf{P}-\mathbf{P}^2=\mathbf 0$, und der Ausdruck ist null. Ist umgekehrt der Ausdruck für alle $\mathbf{y},\mathbf{z}$ null, so ist die Matrix $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}$ die Nullmatrix; mit $\mathbf{y}=\mathbf{e}_i$ und $\mathbf{z}=\mathbf{e}_l$ wählt der Ausdruck nämlich ihren Eintrag $(i,l)$ aus. Dann ist $\mathbf{P}=\mathbf{P}^{\top}\mathbf{P}$, und $\mathbf{P}^{\top}\mathbf{P}$ ist nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 10.2, symmetrisch.
:::

⁠**Rechenbeispiel:** Die Matrix $\mathbf{P}=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ bildet $(x_1,\,x_2)^{\top}$ auf $(x_1+x_2,\,0)^{\top}$ ab. Es ist $\mathbf{P}^2=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$, also ist $\mathbf{P}$ eine Projektion auf die $x_1$-Achse. Sie ist nicht symmetrisch und damit nicht orthogonal: Der Punkt $(0,\,1)^{\top}$ wird auf $(1,\,0)^{\top}$ abgebildet, die Verbindung $(-1,\,1)^{\top}$ steht schräg zur Achse. Das Licht fällt hier in Richtung $(1,\,-1)^{\top}$ ein. Den nächsten Punkt der $x_1$-Achse, $(0,\,0)^{\top}$, liefert diese Projektion nicht.

⁠**Kurz gesagt:** Eine Projektion ist eine Matrix mit $\mathbf{P}^2=\mathbf{P}$; sie ist genau dann orthogonal, also ein Lot, wenn sie symmetrisch ist.

:::aufgabe Aufgabe 4 ★ Eine Projektion von Hand
<span class="anker" id="aufg-4"></span>

Projiziere $\mathbf{y}=(3,\,3,\,0)^{\top}$ auf die Gerade in Richtung $\mathbf{a}=(2,\,1,\,2)^{\top}$.

<ol class="al">

<li>

Berechne $\hat x$, $\hat{\mathbf{y}}$ und die Verbindung $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}$. Prüfe $\mathbf{a}^{\top}\mathbf{r}=0$. Wie weit ist $\mathbf{y}$ von der Geraden entfernt?

</li>

<li>

Stelle die Projektionsmatrix $\mathbf{P}$ auf und prüfe $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ und $\mathbf{P}\mathbf{a}=\mathbf{a}$.

</li>

</ol>

:::loesung
(a) Es ist $\mathbf{a}^{\top}\mathbf{y}=6+3+0=9$ und $\mathbf{a}^{\top}\mathbf{a}=4+1+4=9$, also $\hat x=1$ und $\hat{\mathbf{y}}=\mathbf{a}=(2,\,1,\,2)^{\top}$. Die Verbindung ist $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(1,\,2,\,-2)^{\top}$, und $\mathbf{a}^{\top}\mathbf{r}=2+2-4=0$: Sie steht senkrecht auf der Geraden. Der Abstand von $\mathbf{y}$ zur Geraden ist $\lVert\mathbf{r}\rVert=\sqrt{1+4+4}=3$; nach dem Satz in Abschnitt [2.2](#stufe-2-2) ist kein Punkt der Geraden näher.

(b)

$$\mathbf{P}=\frac{\mathbf{a}\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}=\frac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\qquad \mathbf{P}\mathbf{y}=\frac19\begin{pmatrix}12+6\\6+3\\12+6\end{pmatrix}=\begin{pmatrix}2\\1\\2\end{pmatrix},\qquad \mathbf{P}\mathbf{a}=\frac19\begin{pmatrix}8+2+8\\4+1+4\\8+2+8\end{pmatrix}=\mathbf{a} .$$
:::
:::

:::aufgabe Aufgabe 5 ★★ Pythagoras auf der Geraden
<span class="anker" id="aufg-5"></span>

Es seien $\mathbf{a}=(1,\,2)^{\top}$ und $\mathbf{y}=(4,\,3)^{\top}$ wie im Rechenbeispiel.

<ol class="al">

<li>

Berechne $\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2$ für $t=0$, $1$, $2$, $3$ und $4$ direkt und mit [(2.2)](#gl-2-2).

</li>

<li>

Berechne den Winkel $\varphi$ zwischen $\mathbf{a}$ und $\mathbf{y}$ und prüfe $\lVert\hat{\mathbf{y}}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$.

</li>

</ol>

:::loesung
(a) Direkt: $t=0$: $\lVert(4,\,3)^{\top}\rVert^2=25$; $t=1$: $\lVert(3,\,1)^{\top}\rVert^2=10$; $t=2$: $\lVert(2,\,-1)^{\top}\rVert^2=5$; $t=3$: $\lVert(1,\,-3)^{\top}\rVert^2=10$; $t=4$: $\lVert(0,\,-5)^{\top}\rVert^2=25$. Mit [(2.2)](#gl-2-2), $\hat x=2$, $\lVert\mathbf{r}\rVert^2=5$ und $\lVert\mathbf{a}\rVert^2=5$: $5+5(t-2)^2$ ergibt $25$, $10$, $5$, $10$, $25$. Die Werte liegen symmetrisch um den Fußpunkt $t=2$, denn das Abstandsquadrat wächst mit dem Quadrat des Abstands längs der Geraden.

(b) $\cos\varphi=\mathbf{a}^{\top}\mathbf{y}/(\lVert\mathbf{a}\rVert\,\lVert\mathbf{y}\rVert)=10/(\sqrt5\cdot5)=2/\sqrt5\approx0{,}894$, also $\varphi\approx26{,}57^\circ$. Es ist $\lVert\hat{\mathbf{y}}\rVert=\lVert(2,\,4)^{\top}\rVert=\sqrt{20}=2\sqrt5$ und $|\cos\varphi|\,\lVert\mathbf{y}\rVert=\tfrac2{\sqrt5}\cdot5=2\sqrt5$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Welche Matrizen sind Projektionen?
<span class="anker" id="aufg-6"></span>

Prüfe für jede Matrix, ob sie eine Projektion ist und ob sie eine orthogonale Projektion ist. Beschreibe bei den Projektionen, worauf projiziert wird.

$$\mathbf{P}_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad \mathbf{P}_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad \mathbf{P}_3=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad \mathbf{P}_4=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad \mathbf{P}_5=\mathbf{I},\quad \mathbf{P}_6=\mathbf 0 .$$

:::loesung
Für jede Matrix prüft man zuerst $\mathbf{P}^2=\mathbf{P}$ und dann $\mathbf{P}^{\top}=\mathbf{P}$.

<ul>

<li>

$\mathbf{P}_1$: $\mathbf{P}_1^2=\mathbf{P}_1$ und symmetrisch, also die orthogonale Projektion auf die $x_1$-Achse.

</li>

<li>

$\mathbf{P}_2$: $\mathbf{P}_2^2=\tfrac14\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)=\mathbf{P}_2$ und symmetrisch: die orthogonale Projektion auf die Gerade in Richtung $(1,\,1)^{\top}$; es ist $\mathbf{P}_2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ mit $\mathbf{a}=(1,\,1)^{\top}$.

</li>

<li>

$\mathbf{P}_3$: $\mathbf{P}_3^2=\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)=\mathbf{P}_3$, aber nicht symmetrisch. Eine schiefe Projektion: Sie bildet $(x_1,\,x_2)^{\top}$ auf $x_1\,(1,\,1)^{\top}$ ab, also auf die Gerade in Richtung $(1,\,1)^{\top}$, und den Vektor $(0,\,1)^{\top}$ auf null. Das Licht fällt in Richtung $(0,\,1)^{\top}$ ein, nicht senkrecht zur Geraden.

</li>

<li>

$\mathbf{P}_4$: $\mathbf{P}_4^2=\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)\ne\mathbf{P}_4$. Keine Projektion, sondern eine Scherung; zweimal angewandt schert sie doppelt so stark.

</li>

<li>

$\mathbf{P}_5=\mathbf{I}$: $\mathbf{I}^2=\mathbf{I}$, symmetrisch. Die orthogonale Projektion auf die ganze Ebene; sie lässt alles, wo es ist.

</li>

<li>

$\mathbf{P}_6=\mathbf 0$: $\mathbf 0^2=\mathbf 0$, symmetrisch. Die orthogonale Projektion auf den Nullpunkt.

</li>

</ul>
:::
:::
