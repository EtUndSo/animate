---
title: Näherung durch Matrizen von kleinem Rang
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Kapitel 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15221100
summary: Die Singulärwertzerlegung ordnet die Bausteine einer Matrix nach ihrer Größe.
tags: Frobeniusnorm, abgeschnittene Singulärwertzerlegung
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Die Singulärwertzerlegung ordnet die Bausteine einer Matrix nach ihrer Größe. Lässt man die kleinen weg, bleibt eine Matrix von kleinerem Rang, die man mit viel weniger Zahlen speichern kann. Dieser Abschnitt misst, wie weit diese Näherung von der ursprünglichen Matrix entfernt ist, und beweist, dass keine andere Matrix desselben Rangs näher liegt.
:::

### Die Frobeniusnorm

<span class="anker" id="stufe-10-1"></span>

Um zu sagen, wie nah zwei Matrizen beieinanderliegen, braucht man eine Größe für ihre Differenz. Die Spektralnorm ist eine solche Größe; sie misst die größte Verlängerung. Eine zweite liegt noch näher: Man liest die Matrix wie ein Bild in [Kapitel 1, Abschnitt 6.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1), Zeile für Zeile zu einem langen Vektor aus und nimmt dessen euklidische Norm.

:::definition Definition 10.1 (Frobeniusnorm)
<span class="anker" id="satz-10-1"></span>

Die __Frobeniusnorm__ von $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist

$$\lVert\mathbf{A}\rVert_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^na_{ij}^2} .$$
:::

:::satz Satz 10.2 (Frobeniusnorm und Singulärwerte)
<span class="anker" id="satz-10-2"></span>

Für jede Matrix $\mathbf{A}$ vom Rang $r$ gilt

<span class="anker" id="gl-10-1"></span>
$$\lVert\mathbf{A}\rVert_F^2=\operatorname{spur}(\mathbf{A}^{\top}\mathbf{A})=d_1^2+d_2^2+\dots+d_r^2 . \tag{10.1}$$
:::

:::beweis Frobeniusnorm
Der Diagonaleintrag $j$ von $\mathbf{A}^{\top}\mathbf{A}$ ist $\mathbf{a}_j^{\top}\mathbf{a}_j=\sum_ia_{ij}^2$, die quadrierte Länge der Spalte $j$. Die Spur, die Summe dieser Einträge, ist also die Summe aller quadrierten Einträge von $\mathbf{A}$. Nach [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5) ist die Spur auch die Summe der Eigenwerte von $\mathbf{A}^{\top}\mathbf{A}$, und das sind die $d_j^2$.
:::

Zwei Folgerungen. Wegen $d_1^2\le\sum_jd_j^2$ ist $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F$. Und eine orthogonale Matrix ändert die Frobeniusnorm nicht: $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$, also haben $\mathbf{Q}\mathbf{A}$ und $\mathbf{A}$ dieselben Singulärwerte.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist $\lVert\mathbf{A}\rVert_F^2=4+9+0+4=17=4^2+1^2$ (Abb. [24](#abb-24)), also $\lVert\mathbf{A}\rVert_F=\sqrt{17}\approx4{,}12$, etwas mehr als $\lVert\mathbf{A}\rVert_2=4$.

:::abbildung ml/k2rfrobenius 24
Die Frobeniusnorm von $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ im Quadrat: die Summe aller quadrierten Einträge, gleich der Summe der quadrierten Singulärwerte.
:::
::::

⁠**Kurz gesagt:** Die Frobeniusnorm ist die euklidische Norm aller Einträge; ihr Quadrat ist die Summe der quadrierten Singulärwerte.

### Die abgeschnittene Zerlegung

<span class="anker" id="stufe-10-2"></span>

Bricht man die Summe [(9.4)](die-singularwertzerlegung.html#gl-9-4) nach den $k$ größten Bausteinen ab, erhält man eine Näherung.

:::definition Definition 10.3 (Abgeschnittene Singulärwertzerlegung)
<span class="anker" id="satz-10-3"></span>

Für $k<r$ heißt

<span class="anker" id="gl-10-2"></span>
$$\mathbf{A}_k=\sum_{j=1}^kd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} \tag{10.2}$$

die __abgeschnittene Singulärwertzerlegung__ von $\mathbf{A}$ mit $k$ Bausteinen.
:::

$\mathbf{A}_k$ hat den Rang $k$, denn $\mathbf{A}_k\mathbf{v}_j=d_j\mathbf{u}_j$ für $j\le k$ und $\mathbf{A}_k\mathbf{v}_j=\mathbf{0}$ für $j>k$; die Bilder spannen also einen Raum der Dimension $k$ auf. Der Fehler ist der Rest der Summe:

$$\mathbf{A}-\mathbf{A}_k=\sum_{j=k+1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} .$$

Seine Gram-Matrix ist $\sum_{j>k}d_j^2\mathbf{v}_j\mathbf{v}_j^{\top}$, weil die gemischten Glieder wegen $\mathbf{u}_i^{\top}\mathbf{u}_j=0$ wegfallen. Sie hat die Eigenwerte $d_{k+1}^2,\dots,d_r^2$ und sonst null. Also hat der Fehler die Singulärwerte $d_{k+1},\dots,d_r$, und nach [(9.5)](die-singularwertzerlegung.html#gl-9-5) und [(10.1)](#gl-10-1) ist

<span class="anker" id="gl-10-3"></span>
$$\lVert\mathbf{A}-\mathbf{A}_k\rVert_2=d_{k+1},\qquad \lVert\mathbf{A}-\mathbf{A}_k\rVert_F=\sqrt{d_{k+1}^2+\dots+d_r^2} . \tag{10.3}$$

Zum Speichern braucht $\mathbf{A}_k$ nur die $k$ Vektoren $\mathbf{u}_j$ mit je $m$ Einträgen, die $k$ Vektoren $\mathbf{v}_j$ mit je $n$ Einträgen und die $k$ Zahlen $d_j$, zusammen $k(m+n+1)$ Zahlen statt $mn$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ und $k=1$ ist

$$\mathbf{A}_1=4\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\mathbf{u}_2\mathbf{v}_2^{\top}=\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}.$$

Die Frobeniusnorm des Fehlers ist $\sqrt{0{,}16+0{,}04+0{,}64+0{,}16}=1=d_2$ (Abb. [25](#abb-25)), ebenso seine Spektralnorm.

:::abbildung ml/k2rfehler 25
Der Fehler der besten Näherung vom Rang $1$ in der Frobeniusnorm, mit $0{,}4=\tfrac25$, $0{,}2=\tfrac15$ und $0{,}8=\tfrac45$: Sein Quadrat ist $d_2^2=1$.
:::
::::

⁠**Kurz gesagt:** $\mathbf{A}_k$ behält die $k$ größten Bausteine; der Fehler hat die restlichen Singulärwerte, seine Spektralnorm ist $d_{k+1}$.

### Die beste Näherung

<span class="anker" id="stufe-10-3"></span>

Es gibt viele Matrizen vom Rang $k$. Ist die abgeschnittene Zerlegung die beste unter ihnen? Ja, in beiden Normen.

:::satz Satz 10.4 (Satz von Eckart und Young)
<span class="anker" id="satz-10-4"></span>

Es sei $\mathbf{A}$ vom Rang $r$ und $k<r$. Für jede Matrix $\mathbf{B}$ derselben Form mit $\operatorname{rang}\mathbf{B}\le k$ gilt

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_2,\qquad \lVert\mathbf{A}-\mathbf{B}\rVert_F\ge\sqrt{d_{k+1}^2+\dots+d_r^2}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_F . \tag{10.4}$$

Unter allen Matrizen vom Rang höchstens $k$ liegt $\mathbf{A}_k$ also am nächsten an $\mathbf{A}$.
:::

:::beweis Spektralnorm
Nach dem Rangsatz hat der Kern von $\mathbf{B}$ die Dimension $n-\operatorname{rang}\mathbf{B}\ge n-k$. Man wählt $n-k$ linear unabhängige Vektoren $\mathbf{b}_1,\dots,\mathbf{b}_{n-k}$ im Kern und nimmt $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$ dazu. Das sind $n+1$ Vektoren im $\mathbb{R}^n$, und nach [Kapitel 1, Abschnitt 13.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4), sind sie linear abhängig, denn eine Matrix mit $n$ Zeilen hat höchstens den Rang $n$. Es gibt also Zahlen, nicht alle null, mit $\sum_l\alpha_l\mathbf{b}_l=\sum_j\beta_j\mathbf{v}_j$. Dieser Vektor $\mathbf{z}$ ist nicht null, denn sonst wären wegen der Unabhängigkeit beider Listen alle Zahlen null. Er liegt im Kern von $\mathbf{B}$ und im Spann von $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. Man normiert ihn auf die Länge $1$. Dann ist $(\mathbf{A}-\mathbf{B})\mathbf{z}=\mathbf{A}\mathbf{z}$, und mit $\mathbf{z}=\sum_{j\le k+1}c_j\mathbf{v}_j$, $\sum_jc_j^2=1$:

$$\lVert(\mathbf{A}-\mathbf{B})\mathbf{z}\rVert^2=\lVert\mathbf{A}\mathbf{z}\rVert^2=\sum_{j=1}^{k+1}d_j^2c_j^2\ge d_{k+1}^2\sum_{j=1}^{k+1}c_j^2=d_{k+1}^2 .$$

Also verlängert $\mathbf{A}-\mathbf{B}$ den Einheitsvektor $\mathbf{z}$ mindestens um den Faktor $d_{k+1}$, und $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}$.
:::

Der Beweis zeigt den Grund: Eine Matrix vom Rang $k$ muss eine ganze Menge von Richtungen auf null abbilden, nämlich ihren Kern. Dieser Kern trifft zwangsläufig den Raum der $k+1$ am stärksten gestreckten Richtungen von $\mathbf{A}$, und dort macht $\mathbf{B}$ einen Fehler von mindestens $d_{k+1}$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist $\mathbf{A}_1$ die beste Matrix vom Rang $1$, mit dem Fehler $1$ in beiden Normen. Eine andere Matrix vom Rang $1$, etwa $\mathbf{B}=\bigl(\begin{smallmatrix}2&3\\0&0\end{smallmatrix}\bigr)$, die einfach die zweite Zeile streicht, hat den Fehler $\mathbf{A}-\mathbf{B}=\bigl(\begin{smallmatrix}0&0\\0&2\end{smallmatrix}\bigr)$ mit der Norm $2$.
::::

⁠**Kurz gesagt:** Die abgeschnittene Zerlegung $\mathbf{A}_k$ ist die beste Näherung vom Rang $k$, in der Spektral- wie in der Frobeniusnorm.

:::hintergrund Warum die Aussage auch für die Frobeniusnorm stimmt
Der Beweis für die Frobeniusnorm sieht die Zeilen $\mathbf{a}^{(1)\top},\dots,\mathbf{a}^{(m)\top}$ von $\mathbf{A}$ als $m$ Punkte im $\mathbb{R}^n$, wie die Beispiele einer Datenmatrix. Hat $\mathbf{B}$ höchstens den Rang $k$, so liegen ihre Zeilen in einem Unterraum $\mathcal S$ der Dimension $k$, dem Spaltenraum von $\mathbf{B}^{\top}$, ergänzt auf die Dimension $k$. Für einen festen Unterraum $\mathcal S$ mit der Projektionsmatrix $\mathbf{P}$ ist nach Abschnitt [4](projektion-auf-einen-unterraum.html#stufe-4) die Projektion $\mathbf{P}\mathbf{a}^{(i)}$ jeder Zeile der nächste Punkt in $\mathcal S$. Mit einer Orthonormalbasis $\mathbf{w}_1,\dots,\mathbf{w}_k$ von $\mathcal S$ ist nach dem Satz des Pythagoras

$$\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge\sum_i\bigl\lVert\mathbf{a}^{(i)}-\mathbf{P}\mathbf{a}^{(i)}\bigr\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_i\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2 ,$$

denn $\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\sum_l(\mathbf{w}_l^{\top}\mathbf{a}^{(i)})^2$, und $\mathbf{w}_l^{\top}\mathbf{a}^{(i)}$ ist der Eintrag $i$ von $\mathbf{A}\mathbf{w}_l$. Es bleibt zu zeigen, dass $\sum_l\lVert\mathbf{A}\mathbf{w}_l\rVert^2\le d_1^2+\dots+d_k^2$ ist. In den Koordinaten der $\mathbf{v}_j$ ist

$$\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2=\sum_{l=1}^k\sum_jd_j^2(\mathbf{v}_j^{\top}\mathbf{w}_l)^2=\sum_jd_j^2\,g_j\qquad\text{mit}\qquad g_j=\sum_{l=1}^k(\mathbf{v}_j^{\top}\mathbf{w}_l)^2 .$$

Jedes $g_j$ ist die quadrierte Länge der Projektion von $\mathbf{v}_j$ auf $\mathcal S$, also $0\le g_j\le1$, und die Summe aller $g_j$ ist $\sum_l\lVert\mathbf{w}_l\rVert^2=k$. Eine Summe $\sum_jd_j^2g_j$ mit solchen Gewichten ist am größten, wenn die $k$ größten $d_j^2$ das volle Gewicht $1$ bekommen; das ist $d_1^2+\dots+d_k^2$. Zusammen mit [(10.1)](#gl-10-1) folgt $\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge d_{k+1}^2+\dots+d_r^2$. Die Rechnung zeigt nebenbei: Der Unterraum, in dem die Zeilen von $\mathbf{A}$ am nächsten liegen, ist der Spann von $\mathbf{v}_1,\dots,\mathbf{v}_k$.
:::

### Ein Bild mit wenigen Zahlen

<span class="anker" id="stufe-10-4"></span>

Ein Graustufenbild ist eine Matrix. Nach dem Satz von Eckart und Young ist $\mathbf{A}_k$ die beste Näherung mit $k$ Bausteinen, und [(10.3)](#gl-10-3) sagt, wie viel verloren geht. Der Anteil

$$\frac{d_1^2+\dots+d_k^2}{d_1^2+\dots+d_r^2}$$

gibt an, welcher Teil der Summe aller quadrierten Helligkeitswerte erhalten bleibt.

::::beispiel [Rechenbeispiel]
Das Kreuz aus [Kapitel 1, Abschnitt 6.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1), ist

$$\mathbf{C}=\begin{pmatrix}0&1&0\\1&1&1\\0&1&0\end{pmatrix}.$$

Es ist symmetrisch. Sein charakteristisches Polynom ist $-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda-2)(\lambda+1)$, die Eigenwerte sind $2$, $-1$ und $0$, mit den Eigenvektoren $(1,\,2,\,1)^{\top}$, $(1,\,-1,\,1)^{\top}$ und $(1,\,0,\,-1)^{\top}$. Nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) sind die Singulärwerte $2$, $1$ und $0$; der Rang ist $2$. Die beste Näherung vom Rang $1$ ist mit $\mathbf{q}_1=(1,\,2,\,1)^{\top}/\sqrt6$

$$\mathbf{C}_1=2\,\mathbf{q}_1\mathbf{q}_1^{\top}=\frac13\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix},\qquad \mathbf{C}-\mathbf{C}_1=\frac13\begin{pmatrix}-1&1&-1\\1&-1&1\\-1&1&-1\end{pmatrix}$$

(Abb. [26](#abb-26)). Der Fehler hat in beiden Normen die Größe $1$. $\mathbf{C}_1$ behält $4/5=80\,\%$ der Summe $\lVert\mathbf{C}\rVert_F^2=5$. Jede Zeile von $\mathbf{C}_1$ ist ein Vielfaches derselben Zeile $(1,\,2,\,1)$: Ein Bild vom Rang $1$ ist ein Helligkeitsprofil der Spalten mal ein Helligkeitsprofil der Zeilen, hier ein verwaschener Fleck mit dem hellsten Punkt in der Mitte. Gespeichert werden müssen $1\cdot(3+3+1)=7$ Zahlen statt $9$.

:::abbildung ml/k2bild 26
Das Kreuz $\mathbf{C}$ aus $3\times3$ Bildpunkten (links, $0$ schwarz, $1$ weiß), seine beste Näherung $\mathbf{C}_1$ vom Rang $1$ (Mitte; der Wert $\tfrac43$ ist heller als weiß und weiß dargestellt) und der Fehler $\mathbf{C}-\mathbf{C}_1$ (rechts, rot positiv, blau negativ). Der Fehler ist selbst eine Matrix vom Rang $1$, der Baustein zum Singulärwert $1$.
:::
::::

Bei einem Kreuz aus $3\times3$ Bildpunkten spart das wenig. Bei großen Bildern ist der Unterschied erheblich: Ein Bild aus $1000\times1000$ Bildpunkten hat $10^6$ Einträge; die Näherung mit $k=50$ Bausteinen braucht $50\cdot(1000+1000+1)=100\,050$ Zahlen, rund $10\,\%$. Ob die Näherung gut aussieht, hängt davon ab, wie schnell die Singulärwerte abfallen. Bei vielen Fotos ähneln sich benachbarte Zeilen stark; die Zeilen liegen dann nahe an einem Unterraum kleiner Dimension, und wenige große Singulärwerte tragen fast die ganze Summe $\sum_jd_j^2$.

⁠**Kurz gesagt:** Ein Bild vom Rang $k$ braucht $k(m+n+1)$ Zahlen; die abgeschnittene Zerlegung ist das beste solche Bild, und $\sum_{j\le k}d_j^2/\sum_jd_j^2$ sagt, wie viel erhalten bleibt.

:::aufgabe Aufgabe 30 ★ Normen einer Matrix
<span class="anker" id="aufg-30"></span>

<ol class="al">

<li>

Berechne $\lVert\mathbf{A}\rVert_F$ und $\lVert\mathbf{A}\rVert_2$ für $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$ aus Aufgabe [27](die-singularwertzerlegung.html#aufg-27) und prüfe [(10.1)](#gl-10-1).

</li>

<li>

Welche Frobeniusnorm hat eine orthogonale $n\times n$-Matrix?

</li>

<li>

Zeige $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F\le\sqrt r\,\lVert\mathbf{A}\rVert_2$. Wann gilt rechts Gleichheit?

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{A}\rVert_F^2=9+0+16+25=50=45+5=d_1^2+d_2^2$, also $\lVert\mathbf{A}\rVert_F=\sqrt{50}\approx7{,}07$, und $\lVert\mathbf{A}\rVert_2=d_1=3\sqrt5\approx6{,}71$.

(b) Alle Singulärwerte einer orthogonalen Matrix sind $1$, also ist $\lVert\mathbf{Q}\rVert_F^2=n$ und $\lVert\mathbf{Q}\rVert_F=\sqrt n$. Ebenso direkt: Jede der $n$ Spalten hat das Längenquadrat $1$.

(c) Es ist $\lVert\mathbf{A}\rVert_2^2=d_1^2\le d_1^2+\dots+d_r^2=\lVert\mathbf{A}\rVert_F^2$, und jeder der $r$ Summanden ist höchstens $d_1^2$, also $\lVert\mathbf{A}\rVert_F^2\le r\,d_1^2$. Wurzelziehen ergibt beide Ungleichungen. Rechts gilt Gleichheit genau dann, wenn alle positiven Singulärwerte gleich $d_1$ sind, wie bei einer orthogonalen Matrix.
:::
:::

:::aufgabe Aufgabe 31 ★★ Die beste Matrix vom Rang 1
<span class="anker" id="aufg-31"></span>

Es sei $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$ aus Aufgabe [28](die-singularwertzerlegung.html#aufg-28).

<ol class="al">

<li>

Berechne $\mathbf{A}_1$ und den Fehler $\mathbf{A}-\mathbf{A}_1$ in beiden Normen.

</li>

<li>

Die Matrix $\mathbf{B}$ aus lauter Einsen hat ebenfalls den Rang $1$. Berechne $\lVert\mathbf{A}-\mathbf{B}\rVert_F$ und $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ und vergleiche mit (a).

</li>

<li>

Welcher Anteil der Summe der quadrierten Einträge bleibt in $\mathbf{A}_1$ erhalten?

</li>

</ol>

:::loesung
(a) Aus Aufgabe [28](die-singularwertzerlegung.html#aufg-28): $d_1=2$, $\mathbf{u}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$. Also

$$\mathbf{A}_1=2\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1&1\\1&1\\0&0\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\begin{pmatrix}0&0\\0&0\\1&-1\end{pmatrix}.$$

Der Fehler hat die Frobeniusnorm $\sqrt{1+1}=\sqrt2=d_2$. Er ist das äußere Produkt $\mathbf{e}_3\,(1,\,-1)$, nach Aufgabe [29](die-singularwertzerlegung.html#aufg-29) mit dem einzigen Singulärwert $1\cdot\sqrt2$; auch seine Spektralnorm ist $\sqrt2$.

(b) $\mathbf{A}-\mathbf{B}=\Bigl(\begin{smallmatrix}0&0\\0&0\\0&-2\end{smallmatrix}\Bigr)$ hat in beiden Normen die Größe $2>\sqrt2$. Wie der Satz von Eckart und Young verlangt, liegt $\mathbf{B}$ weiter von $\mathbf{A}$ entfernt als $\mathbf{A}_1$.

(c) $\lVert\mathbf{A}\rVert_F^2=6=4+2$, und $\mathbf{A}_1$ behält $d_1^2/(d_1^2+d_2^2)=\tfrac46=\tfrac23\approx67\,\%$.
:::
:::

:::aufgabe Aufgabe 32 ★ Speicherbedarf
<span class="anker" id="aufg-32"></span>

Ein Graustufenbild hat $600\times800$ Bildpunkte.

<ol class="al">

<li>

Wie viele Zahlen braucht die Näherung mit $k=40$ Bausteinen? Welcher Anteil der ursprünglichen Zahl ist das?

</li>

<li>

Ab welchem $k$ spart die Näherung keinen Speicher mehr?

</li>

</ol>

:::loesung
(a) $40\cdot(600+800+1)=40\cdot1\,401=56\,040$ Zahlen statt $600\cdot800=480\,000$, also etwa $11{,}7\,\%$.

(b) Die Näherung spart Speicher, solange $k\cdot1\,401<480\,000$ ist, also für $k\le342$, denn $342\cdot1\,401=479\,142$ und $343\cdot1\,401=480\,543$. Ab $k=343$ braucht die Näherung mehr Zahlen als das Bild selbst. Der Rang ist höchstens $600$, mehr als $600$ Bausteine gibt es ohnehin nicht.
:::
:::
