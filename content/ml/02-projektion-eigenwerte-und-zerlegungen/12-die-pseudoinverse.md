---
title: Die Pseudoinverse
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Kapitel 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15221200
summary: In Kapitel 1 hatte nur eine quadratische Matrix mit unabhängigen Spalten eine Inverse.
tags: Linksinverse, Rechtsinverse, Pseudoinverse
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
In [Kapitel 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) hatte nur eine quadratische Matrix mit unabhängigen Spalten eine Inverse. Dieser Abschnitt gibt jeder Matrix eine Art Inverse: eine, die von links umkehrt, wenn es mehr Gleichungen als Unbekannte gibt, eine, die von rechts umkehrt, wenn es weniger gibt, und eine für alle Fälle, die Pseudoinverse. Sie liefert immer die beste Näherungslösung und unter mehreren die kürzeste.
:::

### Linksinverse

<span class="anker" id="stufe-11-1"></span>

Eine hohe Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ mit $m>n$ hat keine Inverse; sie ist nicht einmal quadratisch. Eine Hälfte der Eigenschaft einer Inversen kann sie aber haben.

:::definition Definition 11.1 (Linksinverse)
<span class="anker" id="satz-11-1"></span>

Eine Matrix $\mathbf F\in\mathbb{R}^{n\times m}$ mit $\mathbf F\mathbf{A}=\mathbf{I}_n$ heißt __Linksinverse__ von $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Satz 11.2 (Linksinverse)
<span class="anker" id="satz-11-2"></span>

$\mathbf{A}$ hat genau dann eine Linksinverse, wenn ihre Spalten linear unabhängig sind. Dann ist

<span class="anker" id="gl-11-1"></span>
$$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{11.1}$$

eine Linksinverse, und $\mathbf F\mathbf{y}$ ist die beste Näherungslösung von $\mathbf{A}\mathbf{x}=\mathbf{y}$.
:::

:::beweis Linksinverse
Sind die Spalten unabhängig, so ist $\mathbf{A}^{\top}\mathbf{A}$ nach Abschnitt [3.5](die-beste-naherungslosung.html#stufe-3-5) invertierbar, und $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. Nach [(3.5)](die-beste-naherungslosung.html#gl-3-5) ist $\mathbf F\mathbf{y}=\hat{\mathbf{x}}$. Umgekehrt: Hat $\mathbf{A}$ eine Linksinverse und ist $\mathbf{A}\mathbf{x}=\mathbf{0}$, so ist $\mathbf{x}=\mathbf F\mathbf{A}\mathbf{x}=\mathbf F\mathbf{0}=\mathbf{0}$; der Kern ist also $\{\mathbf{0}\}$, und die Spalten sind unabhängig.
:::

Von rechts kehrt $\mathbf F$ nicht um. Das Produkt $\mathbf{A}\mathbf F=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ ist nach [(4.1)](projektion-auf-einen-unterraum.html#gl-4-1) die Projektion auf den Spaltenraum, und für $m>n$ ist das nicht $\mathbf{I}_m$. Eine hohe Matrix hat außerdem viele Linksinversen; [(11.1)](#gl-11-1) ist die, die zur orthogonalen Projektion gehört.

::::beispiel [Rechenbeispiel]
Für $\mathbf{H}$ mit den Spalten $(1,\,0,\,1)^{\top}$ und $(0,\,1,\,1)^{\top}$ ist $(\mathbf{H}^{\top}\mathbf{H})^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ und

$$\mathbf F=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\end{pmatrix}.$$

Es ist $\mathbf F\mathbf{H}=\tfrac13\bigl(\begin{smallmatrix}2+1&-1+1\\-1+1&2+1\end{smallmatrix}\bigr)=\mathbf{I}_2$, und $\mathbf F(1,\,1,\,1)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$ ist die beste Näherungslösung aus Abschnitt [3.3](die-beste-naherungslosung.html#stufe-3-3). $\mathbf{H}\mathbf F$ ist die Projektionsmatrix $\tfrac13\Bigl(\begin{smallmatrix}2&-1&1\\-1&2&1\\1&1&2\end{smallmatrix}\Bigr)$ aus Abschnitt [4.2](projektion-auf-einen-unterraum.html#stufe-4-2). Eine andere Linksinverse ist $\bigl(\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}\bigr)$, denn die ersten beiden Zeilen von $\mathbf{H}$ bilden die Einheitsmatrix; sie liefert aber für $(1,\,1,\,1)^{\top}$ nicht die beste Näherungslösung, sondern $(1,\,1)^{\top}$.
::::

⁠**Kurz gesagt:** Eine Matrix mit unabhängigen Spalten hat die Linksinverse $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$; sie bildet $\mathbf{y}$ auf die beste Näherungslösung ab.

### Rechtsinverse

<span class="anker" id="stufe-11-2"></span>

Bei einer breiten Matrix mit $m<n$ gibt es weniger Gleichungen als Unbekannte. Ist das System lösbar, so hat es unendlich viele Lösungen. Eine Rechtsinverse wählt eine davon aus, und zwar eine besondere.

:::definition Definition 11.3 (Rechtsinverse)
<span class="anker" id="satz-11-3"></span>

Eine Matrix $\mathbf G\in\mathbb{R}^{n\times m}$ mit $\mathbf{A}\mathbf G=\mathbf{I}_m$ heißt __Rechtsinverse__ von $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Satz 11.4 (Rechtsinverse und kürzeste Lösung)
<span class="anker" id="satz-11-4"></span>

Sind die Zeilen von $\mathbf{A}$ linear unabhängig, so ist

<span class="anker" id="gl-11-2"></span>
$$\mathbf G=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1} \tag{11.2}$$

eine Rechtsinverse. $\mathbf{x}=\mathbf G\mathbf{y}$ löst $\mathbf{A}\mathbf{x}=\mathbf{y}$ für jedes $\mathbf{y}$, und unter allen Lösungen hat es die kleinste Länge.
:::

:::beweis Rechtsinverse
Die Zeilen von $\mathbf{A}$ sind die Spalten von $\mathbf{A}^{\top}$; nach Abschnitt [3.5](die-beste-naherungslosung.html#stufe-3-5), angewandt auf $\mathbf{A}^{\top}$, ist $\mathbf{A}\mathbf{A}^{\top}$ invertierbar. Dann ist $\mathbf{A}\mathbf G=\mathbf{A}\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}=\mathbf{I}$ und $\mathbf{A}\mathbf G\mathbf{y}=\mathbf{y}$. Ist $\mathbf{x}$ irgendeine Lösung, so ist $\mathbf{A}(\mathbf{x}-\mathbf G\mathbf{y})=\mathbf{0}$, also liegt $\mathbf{z}=\mathbf{x}-\mathbf G\mathbf{y}$ im Kern. Der Vektor $\mathbf G\mathbf{y}=\mathbf{A}^{\top}\mathbf{w}$ mit $\mathbf{w}=(\mathbf{A}\mathbf{A}^{\top})^{-1}\mathbf{y}$ steht senkrecht auf jedem Vektor des Kerns, denn $(\mathbf{A}^{\top}\mathbf{w})^{\top}\mathbf{z}=\mathbf{w}^{\top}\mathbf{A}\mathbf{z}=0$. Nach dem Satz des Pythagoras ist

$$\lVert\mathbf{x}\rVert^2=\lVert\mathbf G\mathbf{y}+\mathbf{z}\rVert^2=\lVert\mathbf G\mathbf{y}\rVert^2+\lVert\mathbf{z}\rVert^2\ge\lVert\mathbf G\mathbf{y}\rVert^2 ,$$

mit Gleichheit nur für $\mathbf{z}=\mathbf{0}$.
:::

Geometrisch ist die Lösungsmenge eine Gerade oder Ebene, die nicht durch den Nullpunkt geht, und $\mathbf G\mathbf{y}$ ist ihr Punkt, der dem Nullpunkt am nächsten liegt: der Fußpunkt des Lots vom Nullpunkt.

::::beispiel [Rechenbeispiel]
Die eine Gleichung $x_1+2x_2=5$ hat $\mathbf{A}=(1\ \ 2)$ und $\mathbf{A}\mathbf{A}^{\top}=5$. Also ist $\mathbf G=\tfrac15(1,\,2)^{\top}$ und $\mathbf G\cdot5=(1,\,2)^{\top}$. Alle Lösungen sind $(1,\,2)^{\top}+t\,(2,\,-1)^{\top}$, mit der Länge im Quadrat $(1+2t)^2+(2-t)^2=5+5t^2$; am kürzesten ist die Lösung bei $t=0$. Der Vektor $(1,\,2)^{\top}$ steht senkrecht auf der Lösungsgeraden, deren Richtung $(2,\,-1)^{\top}$ ist.
::::

⁠**Kurz gesagt:** Eine Matrix mit unabhängigen Zeilen hat die Rechtsinverse $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$; sie liefert die kürzeste Lösung.

### Die Pseudoinverse

<span class="anker" id="stufe-11-3"></span>

Hat $\mathbf{A}$ weder unabhängige Spalten noch unabhängige Zeilen, versagen beide Formeln. Ein Beispiel ist $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ aus Abschnitt [3.5](die-beste-naherungslosung.html#stufe-3-5): Für $\mathbf{y}=(1,\,1)^{\top}$ sind alle Punkte der Geraden $x_1+2x_2=\tfrac35$ beste Näherungslösungen. Die Singulärwertzerlegung liefert eine Formel für jede Matrix.

:::definition Definition 11.5 (Pseudoinverse)
<span class="anker" id="satz-11-5"></span>

Es sei $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ mit dem Rang $r$. Die Matrix $\mathbf{D}^+\in\mathbb{R}^{n\times m}$ entsteht aus $\mathbf{D}^{\top}$, indem man jedes $d_j>0$ durch $1/d_j$ ersetzt; die Nullen bleiben. Die __Pseudoinverse__ von $\mathbf{A}$ ist

<span class="anker" id="gl-11-3"></span>
$$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\sum_{j=1}^r\frac1{d_j}\,\mathbf{v}_j\mathbf{u}_j^{\top} . \tag{11.3}$$
:::

Jeder Baustein kehrt einen Baustein von $\mathbf{A}$ um: $\mathbf{A}$ bildet $\mathbf{v}_j$ auf $d_j\mathbf{u}_j$ ab, $\mathbf{A}^+$ bildet $\mathbf{u}_j$ auf $\mathbf{v}_j/d_j$ ab. Die Richtungen $\mathbf{u}_j$ mit $j>r$, die $\mathbf{A}$ nicht erreicht, bildet $\mathbf{A}^+$ auf null ab, statt durch null zu teilen. Ist $\mathbf{A}$ invertierbar, so ist $\mathbf{A}^+=\mathbf{A}^{-1}$, denn dann ist $\mathbf{A}^{-1}=(\mathbf{V}^{\top})^{-1}\mathbf{D}^{-1}\mathbf{U}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$.

::::beispiel [Rechenbeispiel]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ist symmetrisch und positiv semidefinit mit dem Eigenwert $5$ zu $\mathbf{q}=(1,\,2)^{\top}/\sqrt5$ und dem Eigenwert $0$. Nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) ist $\mathbf{A}=5\,\mathbf{q}\mathbf{q}^{\top}$ ihre kompakte Zerlegung, mit $d_1=5$ und $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Also ist

$$\mathbf{A}^+=\frac15\,\mathbf{q}\mathbf{q}^{\top}=\frac1{25}\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$
::::

⁠**Kurz gesagt:** Die Pseudoinverse $\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ kehrt jeden Baustein $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ mit $d_j>0$ um und lässt die Richtungen zum Singulärwert $0$ auf null.

### Die kürzeste beste Näherungslösung

<span class="anker" id="stufe-11-4"></span>

Was leistet $\mathbf{A}^+\mathbf{y}$? Es vereint die beiden vorigen Unterabschnitte.

:::satz Satz 11.6 (Pseudoinverse und kleinste Quadrate)
<span class="anker" id="satz-11-6"></span>

Für jede Matrix $\mathbf{A}$ und jeden Vektor $\mathbf{y}$ ist $\mathbf{x}^+=\mathbf{A}^+\mathbf{y}$ eine beste Näherungslösung von $\mathbf{A}\mathbf{x}=\mathbf{y}$, und unter allen besten Näherungslösungen hat sie die kleinste Länge. Insbesondere ist

$$\begin{gathered} \mathbf{A}^+=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\quad\text{bei unabhängigen Spalten},\\ \mathbf{A}^+=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\quad\text{bei unabhängigen Zeilen}. \end{gathered}$$
:::

:::beweis Pseudoinverse
Man rechnet in den Koordinaten der Singulärvektoren: $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ und $\boldsymbol\beta=\mathbf{U}^{\top}\mathbf{y}$. Weil $\mathbf{U}^{\top}$ Längen erhält, ist

$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{U}^{\top}\mathbf{y}-\mathbf{D}\mathbf{V}^{\top}\mathbf{x}\rVert^2=\lVert\boldsymbol\beta-\mathbf{D}\mathbf{c}\rVert^2=\sum_{j=1}^r(\beta_j-d_jc_j)^2+\sum_{j=r+1}^m\beta_j^2 .$$

Die zweite Summe hängt nicht von $\mathbf{x}$ ab. Die erste ist genau dann null, also so klein wie möglich, wenn $c_j=\beta_j/d_j$ für alle $j\le r$ ist; die $c_j$ mit $j>r$ kommen gar nicht vor. Die besten Näherungslösungen sind also genau die $\mathbf{x}=\mathbf{V}\mathbf{c}$ mit $c_j=\beta_j/d_j$ für $j\le r$ und beliebigen $c_{r+1},\dots,c_n$. Ihre Länge ist $\lVert\mathbf{x}\rVert^2=\lVert\mathbf{c}\rVert^2=\sum_{j\le r}(\beta_j/d_j)^2+\sum_{j>r}c_j^2$, am kleinsten für $c_j=0$ bei $j>r$. Dieses $\mathbf{c}$ ist $\mathbf{D}^+\boldsymbol\beta$, also $\mathbf{x}=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}\mathbf{y}=\mathbf{A}^+\mathbf{y}$.

Bei unabhängigen Spalten gibt es nach Abschnitt [3.5](die-beste-naherungslosung.html#stufe-3-5) nur eine beste Näherungslösung, $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$; sie muss mit $\mathbf{A}^+\mathbf{y}$ übereinstimmen, und zwar für jedes $\mathbf{y}$. Bei unabhängigen Zeilen ist der Rang nach [Kapitel 1, Abschnitt 13.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4), gleich $m$, der Spaltenraum also der ganze $\mathbb{R}^m$, und das System ist für jedes $\mathbf{y}$ lösbar; die besten Näherungslösungen sind die Lösungen, und die kürzeste ist nach Abschnitt [11.2](#stufe-11-2) $\mathbf G\mathbf{y}$.
:::

::::beispiel [Rechenbeispiel 1]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ und $\mathbf{y}=(1,\,1)^{\top}$ ist $\mathbf{x}^+=\tfrac1{25}(1+2,\ 2+4)^{\top}=(0{,}12;\ 0{,}24)^{\top}$. Er liegt auf der Geraden der besten Näherungslösungen, denn $0{,}12+2\cdot0{,}24=0{,}6=\tfrac35$, und zeigt in Richtung $(1,\,2)^{\top}$, senkrecht zu ihr: Er ist ihr Punkt, der dem Nullpunkt am nächsten liegt.
::::

::::beispiel [Rechenbeispiel 2]
Dieselbe Größe wird dreimal gemessen, mit den Ergebnissen $4$, $5$ und $9$. Das System „$x=4$, $x=5$, $x=9$“ hat die Matrix $\mathbf{1}\in\mathbb{R}^{3\times1}$, eine Spalte aus Einsen. Sie hat eine unabhängige Spalte, also ist $\mathbf{1}^+=(\mathbf{1}^{\top}\mathbf{1})^{-1}\mathbf{1}^{\top}=\tfrac13(1,\,1,\,1)$ und

$$x^+=\tfrac13\,\mathbf{1}^{\top}\mathbf{y}=\tfrac13\,(4+5+9)=6 ,$$

der Mittelwert (Abb. [27](#abb-27)). Der Mittelwert mehrerer Messungen ist die beste Näherungslösung des Systems, das jede Messung für exakt hält.

:::abbildung ml/k2rmittel 27
Die Pseudoinverse der Einsenspalte angewandt auf die Messwerte $\mathbf{y}=(4,5,9)^{\top}$: Das Skalarprodukt mit $\mathbf{1}$ ist die Summe der Messwerte, geteilt durch $\mathbf{1}^{\top}\mathbf{1}=3$ ergibt den Mittelwert.
:::
::::

⁠**Kurz gesagt:** $\mathbf{A}^+\mathbf{y}$ ist für jede Matrix eine beste Näherungslösung, unter mehreren die kürzeste; bei unabhängigen Spalten oder Zeilen ist $\mathbf{A}^+$ die Links- oder Rechtsinverse.

:::hintergrund Warum die Pseudoinverse nicht durch null teilt
Die Pseudoinverse ersetzt $1/d_j$ durch $0$, wo $d_j=0$ ist. Das wirkt willkürlich, folgt aber aus einem Grenzübergang. Die Matrix $\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I}$ ist für jedes $\delta\ne0$ invertierbar, denn ihre Eigenwerte sind $d_j^2+\delta^2>0$. In den Koordinaten der Singulärvektoren multipliziert $(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ die $j$-te Koordinate mit

$$\frac{d_j}{d_j^2+\delta^2}\ \xrightarrow{\ \delta\to0\ }\ \begin{cases}1/d_j&\text{für }d_j>0,\\0&\text{für }d_j=0.\end{cases}$$

Also ist $\mathbf{A}^+=\lim_{\delta\to0}(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ für jede Matrix. Der Grenzübergang zeigt auch eine Gefahr: Die Pseudoinverse hängt nicht stetig von der Matrix ab. Für $\operatorname{diag}(1;\,\varepsilon)$ mit kleinem $\varepsilon>0$ ist die Pseudoinverse $\operatorname{diag}(1;\,1/\varepsilon)$, riesig; für $\varepsilon=0$ ist sie $\operatorname{diag}(1;\,0)$. Ein winziger Singulärwert, der nur durch Messfehler oder Rundung nicht null ist, wird durch $\mathbf{A}^+$ gewaltig verstärkt. Rechenprogramme behandeln deshalb Singulärwerte unterhalb einer kleinen Schwelle als null. Wie stark kleine Singulärwerte Fehler verstärken, misst der nächste Abschnitt.
:::

:::aufgabe Aufgabe 33 ★ Eine Linksinverse
<span class="anker" id="aufg-33"></span>

Die Ausgleichsgerade in Abschnitt [3.6](die-beste-naherungslosung.html#stufe-3-6) gehört zu $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Berechne die Linksinverse $\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ und prüfe $\mathbf F\mathbf{A}=\mathbf{I}$.

</li>

<li>

Wende $\mathbf F$ auf $\mathbf{y}=(1,\,2,\,4)^{\top}$ an und vergleiche mit Abschnitt [3.6](die-beste-naherungslosung.html#stufe-3-6).

</li>

<li>

Lies an den Zeilen von $\mathbf F$ ab, wie Achsenabschnitt und Steigung der Ausgleichsgeraden für beliebige Messwerte $y_1,y_2,y_3$ entstehen.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\bigr)$ mit der Inversen $\tfrac16\bigl(\begin{smallmatrix}5&-3\\-3&3\end{smallmatrix}\bigr)$, also

$$\mathbf F=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}=\frac16\begin{pmatrix}5&2&-1\\-3&0&3\end{pmatrix},\qquad \mathbf F\mathbf{A}=\frac16\begin{pmatrix}5+2-1&2-2\\-3+3&6\end{pmatrix}=\mathbf{I} .$$

(b) $\mathbf F(1,\,2,\,4)^{\top}=\tfrac16(5+4-4,\ -3+12)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$, die Ausgleichsgerade aus Abschnitt [3.6](die-beste-naherungslosung.html#stufe-3-6).

(c) Für beliebige Messwerte ist der Achsenabschnitt $\hat x_1=\tfrac16(5y_1+2y_2-y_3)$ und die Steigung $\hat x_2=\tfrac12(y_3-y_1)$. Die Gewichte des Achsenabschnitts summieren sich zu $1$: Sind alle Messwerte gleich, ist der Achsenabschnitt dieser Wert. Die Steigung hängt bei drei gleich weit auseinanderliegenden Messstellen nur von den beiden äußeren Punkten ab; der mittlere Punkt beeinflusst nur die Höhe der Geraden.
:::
:::

:::aufgabe Aufgabe 34 ★★ Kürzeste Lösungen
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Bestimme die Pseudoinverse von $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ und $\mathbf{x}^+$ für $\mathbf{y}=(1,\,3)^{\top}$. Prüfe, dass $\mathbf{x}^+$ eine beste Näherungslösung ist und dass keine kürzere existiert.

</li>

<li>

Bestimme die kürzeste Lösung von $x_1+2x_2+2x_3=9$. Vergleiche ihre Länge mit der Lösung $(9,\,0,\,0)^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}=2\,\mathbf{q}\mathbf{q}^{\top}$ mit $\mathbf{q}=(1,\,1)^{\top}/\sqrt2$, symmetrisch und positiv semidefinit, also die kompakte Zerlegung mit $d_1=2$ und $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Damit ist $\mathbf{A}^+=\tfrac12\mathbf{q}\mathbf{q}^{\top}=\tfrac14\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ und $\mathbf{x}^+=\tfrac14(4,\,4)^{\top}=(1,\,1)^{\top}$. Es ist $\mathbf{A}\mathbf{x}^+=(2,\,2)^{\top}$, die Projektion von $(1,\,3)^{\top}$ auf die Gerade in Richtung $(1,\,1)^{\top}$, denn $\tfrac{1+3}2(1,\,1)^{\top}=(2,\,2)^{\top}$. Die besten Näherungslösungen sind alle $\mathbf{x}$ mit $x_1+x_2=2$, also $(1+s,\ 1-s)^{\top}$ mit dem Längenquadrat $2+2s^2$. Am kürzesten ist die bei $s=0$, und das ist $\mathbf{x}^+$.

(b) $\mathbf{A}=(1\ \ 2\ \ 2)$ hat $\mathbf{A}\mathbf{A}^{\top}=9$, also ist $\mathbf G=\tfrac19(1,\,2,\,2)^{\top}$ und die kürzeste Lösung $\mathbf G\cdot9=(1,\,2,\,2)^{\top}$ mit der Länge $3$. Die Lösung $(9,\,0,\,0)^{\top}$ hat die Länge $9$. Die kürzeste Lösung zeigt in Richtung des Normalenvektors $(1,\,2,\,2)^{\top}$ der Lösungsebene.
:::
:::

:::aufgabe Aufgabe 35 ★★★ Was die Pseudoinverse projiziert
<span class="anker" id="aufg-35"></span>

Es sei $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ mit dem Rang $r$, und $\mathbf{U}_r$, $\mathbf{V}_r$ enthalten die ersten $r$ Spalten von $\mathbf{U}$ und $\mathbf{V}$.

<ol class="al">

<li>

Zeige $\mathbf{A}\mathbf{A}^+=\mathbf{U}_r\mathbf{U}_r^{\top}$ und $\mathbf{A}^+\mathbf{A}=\mathbf{V}_r\mathbf{V}_r^{\top}$. Auf welche Räume projizieren diese Matrizen?

</li>

<li>

Folgere $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$ und $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{A}^+=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^+\mathbf{U}^{\top}$. Die $m\times m$-Matrix $\mathbf{D}\mathbf{D}^+$ hat auf den ersten $r$ Diagonalplätzen $d_j\cdot\tfrac1{d_j}=1$ und sonst Nullen. Also ist $\mathbf{A}\mathbf{A}^+=\sum_{j\le r}\mathbf{u}_j\mathbf{u}_j^{\top}=\mathbf{U}_r\mathbf{U}_r^{\top}$, nach [(4.2)](projektion-auf-einen-unterraum.html#gl-4-2) die orthogonale Projektion auf den Spann von $\mathbf{u}_1,\dots,\mathbf{u}_r$, den Spaltenraum von $\mathbf{A}$. Ebenso ist $\mathbf{A}^+\mathbf{A}=\mathbf{V}\mathbf{D}^+\mathbf{D}\mathbf{V}^{\top}=\mathbf{V}_r\mathbf{V}_r^{\top}$, die Projektion auf den Spann von $\mathbf{v}_1,\dots,\mathbf{v}_r$, den Spaltenraum von $\mathbf{A}^{\top}$; das ist das orthogonale Komplement des Kerns.

(b) Jede Spalte von $\mathbf{A}$ liegt im Spaltenraum, und die Projektion darauf lässt sie fest: $\mathbf{A}\mathbf{A}^+\mathbf{A}=(\mathbf{U}_r\mathbf{U}_r^{\top})\mathbf{A}=\mathbf{A}$. Ebenso liegt jede Spalte von $\mathbf{A}^+=\sum_{j\le r}\tfrac1{d_j}\mathbf{v}_j\mathbf{u}_j^{\top}$ im Spann von $\mathbf{v}_1,\dots,\mathbf{v}_r$, also ist $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=(\mathbf{V}_r\mathbf{V}_r^{\top})\mathbf{A}^+=\mathbf{A}^+$.
:::
:::
