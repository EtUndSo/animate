---
title: Positiv definite Matrizen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
knoten: Grundlagen 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15220900
summary: Eine quadratische Form ist eine Schüssel, wenn sie überall außer im Nullpunkt positiv ist.
tags: positiv definit, positiv semidefinit, indefinit, Rayleigh-Quotient
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Eine quadratische Form ist eine Schüssel, wenn sie überall außer im Nullpunkt positiv ist. Dieser Abschnitt gibt dieser Eigenschaft einen Namen und stellt Tests vor, mit denen man sie prüft: über die Eigenwerte, über die Pivots und über Determinanten. Dazu kommen zwei Folgerungen: der größte und kleinste Wert einer Form auf dem Einheitskreis und eine Zerlegung, die nur Schüsseln haben.
:::

### Positiv definit und positiv semidefinit

<span class="anker" id="stufe-8-1"></span>

Die Schüssel und die Rinne aus Abschnitt [5.3](quadratische-formen.html#stufe-5-3) unterscheiden sich in einem Punkt: Die Schüssel ist außerhalb des Nullpunkts überall positiv, die Rinne nur nicht negativ. Für diese beiden Eigenschaften gibt es feste Namen.

:::definition Definition 8.1 (Positiv definit, positiv semidefinit)
<span class="anker" id="satz-8-1"></span>

Eine symmetrische Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ heißt __positiv definit__, wenn

<span class="anker" id="gl-8-1"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}>0\qquad\text{für alle}\ \mathbf{x}\ne\mathbf{0} , \tag{8.1}$$

und __positiv semidefinit__, wenn $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}\ge0$ für alle $\mathbf{x}$.
:::

Die Symmetrie gehört zur Definition. Für die quadratische Form ist das keine Einschränkung, nach Abschnitt [5.2](quadratische-formen.html#stufe-5-2) zählt ohnehin nur der symmetrische Anteil. Sie ist aber nötig, damit die Tests im nächsten Unterabschnitt gelten. Jede positiv definite Matrix ist auch positiv semidefinit.

::::beispiel [Rechenbeispiel]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ ist positiv definit, denn nach Abschnitt [5.4](quadratische-formen.html#stufe-5-4) ist $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=5(x_1+0{,}4x_2)^2+1{,}2x_2^2$, und das ist nur null, wenn $x_2=0$ und dann auch $x_1=0$ ist. Die Matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ hat die Form $x_1^2+4x_1x_2+4x_2^2=(x_1+2x_2)^2\ge0$; sie ist positiv semidefinit, aber nicht positiv definit, denn für $\mathbf{x}=(2,\,-1)^{\top}$ ist die Form null. Ihr Graph ist eine Rinne mit dem Talboden in Richtung $(2,\,-1)^{\top}$.
::::

⁠**Kurz gesagt:** Positiv definit heißt: Die quadratische Form ist außerhalb des Nullpunkts positiv, eine Schüssel; positiv semidefinit heißt: nirgends negativ.

### Der Eigenwerttest

<span class="anker" id="stufe-8-2"></span>

Die Hauptachsenform [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) beantwortet die Frage sofort: Eine Summe $\sum_i\lambda_ic_i^2$ ist für jede Wahl der Koordinaten positiv, wenn alle $\lambda_i$ positiv sind, und sonst nicht.

:::satz Satz 8.2 (Eigenwerttest)
<span class="anker" id="satz-8-2"></span>

Eine symmetrische Matrix ist genau dann positiv definit, wenn alle ihre Eigenwerte positiv sind, und genau dann positiv semidefinit, wenn keiner negativ ist.
:::

:::beweis Eigenwerttest
Sind alle $\lambda_i>0$ und ist $\mathbf{x}\ne\mathbf{0}$, so ist auch $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}\ne\mathbf{0}$, denn $\mathbf{Q}$ ist invertierbar; nach [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) ist dann $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2>0$. Ist umgekehrt ein Eigenwert $\lambda_i\le0$, so ist für den Eigenvektor $\mathbf{x}=\mathbf{q}_i$ die Form $\mathbf{q}_i^{\top}\mathbf{A}\mathbf{q}_i=\lambda_i\le0$, und $\mathbf{A}$ ist nicht positiv definit. Für semidefinit geht man ebenso vor, mit $\ge$ statt $>$.
:::

Hat eine symmetrische Matrix positive und negative Eigenwerte, so ist ihre Form in manchen Richtungen positiv und in anderen negativ: ein Sattel. Eine solche Matrix heißt __indefinit__. Entsprechend heißt eine Matrix mit lauter negativen Eigenwerten negativ definit; ihre Form ist eine Kuppel.

::::beispiel [Rechenbeispiel]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ hat die Eigenwerte $6$ und $1$: positiv definit. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ hat die Eigenwerte $5$ und $0$: positiv semidefinit. $\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ hat lauter positive Einträge, aber die Eigenwerte $4$ und $-2$: indefinit, denn für $\mathbf{x}=(1,\,-1)^{\top}$ ist die Form $1-6+1=-4$. Positive Einträge sagen also nichts über die Definitheit.
::::

⁠**Kurz gesagt:** Eine symmetrische Matrix ist genau dann positiv definit, wenn alle Eigenwerte positiv sind; positive und negative Eigenwerte zusammen ergeben einen Sattel.

:::hintergrund Warum die Symmetrie zur Definition gehört
Manche Bücher definieren positiv definit über die quadratische Form, andere über die Eigenwerte. Für symmetrische Matrizen ist das nach dem Satz dasselbe, für nicht symmetrische nicht. Die Matrix $\bigl(\begin{smallmatrix}2&-5\\0&2\end{smallmatrix}\bigr)$ hat als Dreiecksmatrix die Eigenwerte $2$ und $2$, beide positiv. Ihre quadratische Form ist aber $2x_1^2-5x_1x_2+2x_2^2$, und für $\mathbf{x}=(1,\,1)^{\top}$ ist sie $2-5+2=-1$. Der Grund: Die Form sieht nur den symmetrischen Anteil $\bigl(\begin{smallmatrix}2&-2{,}5\\-2{,}5&2\end{smallmatrix}\bigr)$ mit den Eigenwerten $4{,}5$ und $-0{,}5$, die Eigenwerte gehören aber zur ganzen Matrix. Wer den Begriff ohne Symmetrie benutzt, muss deshalb immer sagen, welche Definition gemeint ist.
:::

### Tests ohne Eigenwerte

<span class="anker" id="stufe-8-3"></span>

Eigenwerte auszurechnen ist bei großen Matrizen aufwendig. Das quadratische Ergänzen aus Abschnitt [5.4](quadratische-formen.html#stufe-5-4) liefert einen Test ohne Eigenwerte, und aus ihm folgt ein zweiter mit Determinanten.

:::satz Satz 8.3 (Tests für positive Definitheit)
<span class="anker" id="satz-8-3"></span>

Für eine symmetrische Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ sind gleichwertig:

<ol class="rm">

<li>

$\mathbf{A}$ ist positiv definit;

</li>

<li>

das Gauß-Verfahren ohne Zeilenvertauschungen liefert $n$ positive Pivots;

</li>

<li>

alle führenden Hauptminoren sind positiv: Die Determinanten der linken oberen $k\times k$-Teilmatrizen sind für $k=1,\dots,n$ größer als null.

</li>

</ol>

Für $n=2$ und $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ heißt das: $a>0$ und $ac-b^2>0$.
:::

Für $n=2$ ist das [(5.3)](quadratische-formen.html#gl-5-3): Die Pivots sind $a$ und $c-b^2/a$, die Form ist genau dann eine Schüssel, wenn beide positiv sind, und $c-b^2/a>0$ ist bei $a>0$ gleichwertig mit $ac-b^2>0$. Für größere $n$ ergänzt jeder Eliminationsschritt eine Variable zu einem Quadrat, wie im Hintergrund in Abschnitt [5.4](quadratische-formen.html#stufe-5-4). Die Determinante der linken oberen $k\times k$-Teilmatrix ist das Produkt der ersten $k$ Pivots, deshalb sind die Pivots genau dann alle positiv, wenn es die führenden Hauptminoren sind. Der Determinantentest heißt auch Kriterium von Sylvester.

Zwei Warnungen. Erstens genügt $\det\mathbf{A}>0$ allein nicht: $\operatorname{diag}(-1;\,-3)$ hat die Determinante $3$, ist aber negativ definit. Zweitens überträgt sich der Test nicht einfach auf semidefinit: $\operatorname{diag}(0;\,-1)$ hat die führenden Hauptminoren $0$ und $0$, beide nicht negativ, und ist trotzdem nicht positiv semidefinit.

::::beispiel [Rechenbeispiel]
Für

$$\mathbf{A}=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$$

sind die führenden Hauptminoren $2$, $\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ und $\det\mathbf{A}=2\cdot3-1\cdot2=4$, alle positiv: $\mathbf{A}$ ist positiv definit. Die Pivots sind $2$, $\tfrac32$ und $\tfrac43$, die Quotienten aufeinanderfolgender Minoren. Zur Kontrolle: Die Eigenwerte sind $2-\sqrt2$, $2$ und $2+\sqrt2$, alle positiv, und ihr Produkt ist $(4-2)\cdot2=4$.
::::

⁠**Kurz gesagt:** Eine symmetrische Matrix ist genau dann positiv definit, wenn alle Pivots oder alle führenden Hauptminoren positiv sind; bei $2\times2$ heißt das $a>0$ und $ac-b^2>0$.

### Gram-Matrizen sind positiv semidefinit

<span class="anker" id="stufe-8-4"></span>

In [Grundlagen 1, Abschnitt 10](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10), tauchten die Gram-Matrizen $\mathbf{X}^{\top}\mathbf{X}$ und $\mathbf{X}\mathbf{X}^{\top}$ auf, und in diesem Kapitel $\mathbf{A}^{\top}\mathbf{A}$ in den Normalgleichungen. Sie sind immer positiv semidefinit, und der Grund ist einfach: Ihre quadratische Form ist ein Längenquadrat.

:::satz Satz 8.4 (Gram-Matrizen)
<span class="anker" id="satz-8-4"></span>

Für jede Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist $\mathbf{A}^{\top}\mathbf{A}$ positiv semidefinit. Sie ist genau dann positiv definit, wenn die Spalten von $\mathbf{A}$ linear unabhängig sind.
:::

:::beweis Gram-Matrizen
$\mathbf{A}^{\top}\mathbf{A}$ ist symmetrisch, und $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}\mathbf{x})^{\top}(\mathbf{A}\mathbf{x})=\lVert\mathbf{A}\mathbf{x}\rVert^2\ge0$. Gleich null ist das genau dann, wenn $\mathbf{A}\mathbf{x}=\mathbf{0}$ ist. Bei unabhängigen Spalten geschieht das nur für $\mathbf{x}=\mathbf{0}$.
:::

Dasselbe gilt für $\mathbf{A}\mathbf{A}^{\top}$ mit den Zeilen statt der Spalten. Der Satz erklärt nachträglich Abschnitt [3.5](die-beste-naherungslosung.html#stufe-3-5): Bei unabhängigen Spalten ist $\mathbf{A}^{\top}\mathbf{A}$ positiv definit, hat also lauter positive Eigenwerte und ist invertierbar.

::::beispiel [Rechenbeispiel]
$\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ hat die Eigenwerte $3$ und $1$: positiv definit, passend zu den unabhängigen Spalten von $\mathbf{H}$. Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ist $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$ mit der Determinante $0$ und den Eigenwerten $25$ und $0$: positiv semidefinit, nicht positiv definit.
::::

⁠**Kurz gesagt:** $\mathbf{A}^{\top}\mathbf{A}$ ist immer positiv semidefinit, weil $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf{A}\mathbf{x}\rVert^2$ ist; bei unabhängigen Spalten ist sie positiv definit.

### Größter und kleinster Wert auf dem Einheitskreis

<span class="anker" id="stufe-8-5"></span>

Eine quadratische Form wächst mit dem Quadrat der Länge von $\mathbf{x}$. Wie stark sie in verschiedenen Richtungen wächst, sieht man, wenn man nur Vektoren der Länge $1$ einsetzt. In welcher Richtung ist sie am größten?

:::satz Satz 8.5 (Extremwerte einer quadratischen Form)
<span class="anker" id="satz-8-5"></span>

Es sei $\mathbf{A}$ symmetrisch mit dem kleinsten Eigenwert $\lambda_{\min}$ und dem größten Eigenwert $\lambda_{\max}$. Für jeden Vektor $\mathbf{x}\ne\mathbf{0}$ gilt

<span class="anker" id="gl-8-2"></span>
$$\lambda_{\min}\le\frac{\mathbf{x}^{\top}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}}\le\lambda_{\max} . \tag{8.2}$$

Der größte Wert wird an einem Eigenvektor zu $\lambda_{\max}$ angenommen, der kleinste an einem Eigenvektor zu $\lambda_{\min}$.
:::

:::beweis Extremwerte
Mit $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ ist $\mathbf{x}^{\top}\mathbf{x}=\mathbf{c}^{\top}\mathbf{c}=\sum_ic_i^2$, weil $\mathbf{Q}$ Längen erhält, und $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2$. Der Quotient ist also

$$\frac{\sum_i\lambda_ic_i^2}{\sum_ic_i^2}=\sum_i\lambda_i\,g_i\qquad\text{mit}\qquad g_i=\frac{c_i^2}{\sum_lc_l^2}\ge0,\quad \sum_ig_i=1 .$$

Das ist ein gewichtetes Mittel der Eigenwerte, und ein Mittel liegt immer zwischen dem kleinsten und dem größten der gemittelten Werte. Für $\mathbf{x}=\mathbf{q}_i$ ist nur $g_i=1$, und der Quotient ist $\lambda_i$.
:::

Der Quotient in [(8.2)](#gl-8-2) heißt __Rayleigh-Quotient__. Für $\lVert\mathbf{x}\rVert=1$ ist er die quadratische Form selbst: Auf dem Einheitskreis liegt die Form zwischen dem kleinsten und dem größten Eigenwert.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ ist der Rayleigh-Quotient bei $\mathbf{e}_1$ gleich $5$, bei $\mathbf{e}_2$ gleich $2$, bei $(1,\,1)^{\top}/\sqrt2$ gleich $\tfrac{5+4+2}2=5{,}5$ und bei $(1,\,-1)^{\top}/\sqrt2$ gleich $\tfrac{5-4+2}2=1{,}5$. Alle Werte liegen zwischen $1$ und $6$. Den Wert $6$ erreicht er bei $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$: $\tfrac15(20+8+2)=6$. Der Quotient hängt nicht von der Länge von $\mathbf{x}$ ab; Abb. [21](#abb-21) rechnet ihn für $\mathbf{x}=(1,\,1)^{\top}$ ohne Wurzeln aus.

:::abbildung ml/k2rrayleigh 21
Der Rayleigh-Quotient von $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ an der Stelle $\mathbf{x}=(1,1)^{\top}$: Zähler und Nenner als Summen, der Quotient $\tfrac{11}2=5{,}5$ liegt zwischen den Eigenwerten $1$ und $6$.
:::
::::

⁠**Kurz gesagt:** Auf dem Einheitskreis liegt eine quadratische Form zwischen dem kleinsten und dem größten Eigenwert, und diese Extremwerte werden in den Eigenrichtungen angenommen.

### Die Cholesky-Zerlegung

<span class="anker" id="stufe-8-6"></span>

Quadratisches Ergänzen schreibt eine positiv definite Form als Summe von Quadraten. Fasst man die Ausdrücke in den Quadraten zu einem Vektor zusammen, so ist die Form das Längenquadrat dieses Vektors. Daraus wird eine Zerlegung der Matrix.

:::satz Satz 8.6 (Cholesky-Zerlegung)
<span class="anker" id="satz-8-6"></span>

Eine symmetrische Matrix $\mathbf{A}$ ist genau dann positiv definit, wenn es eine untere Dreiecksmatrix $\mathbf L$ mit positiven Diagonaleinträgen gibt mit

<span class="anker" id="gl-8-3"></span>
$$\mathbf{A}=\mathbf L\mathbf L^{\top} . \tag{8.3}$$

Diese Matrix $\mathbf L$ ist eindeutig und heißt Cholesky-Faktor von $\mathbf{A}$.
:::

Ist $\mathbf{A}=\mathbf L\mathbf L^{\top}$, so ist $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf L^{\top}\mathbf{x}\rVert^2$, eine Summe von Quadraten, und weil $\mathbf L$ invertierbar ist, ist sie nur für $\mathbf{x}=\mathbf{0}$ null. Das ist die eine Richtung. Die andere Richtung, dass jede positiv definite Matrix einen solchen Faktor hat, ist das quadratische Ergänzen: Für $n=2$ liest man ihn aus [(5.3)](quadratische-formen.html#gl-5-3) ab,

$$\mathbf L=\begin{pmatrix}\sqrt a&0\\b/\sqrt a&\sqrt{c-b^2/a}\end{pmatrix},$$

und für größere $n$ setzt man das Ergänzen Variable für Variable fort. Nach [Grundlagen 1, Abschnitt 14.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), ist $\det\mathbf{A}=\det\mathbf L\cdot\det\mathbf L^{\top}=(l_{11}\cdots l_{nn})^2$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$ ist $a=4$, $b=2$, $c=5$, also $l_{11}=2$, $l_{21}=1$ und $l_{22}=\sqrt{5-1}=2$:

$$\mathbf L=\begin{pmatrix}2&0\\1&2\end{pmatrix},\qquad \mathbf L\mathbf L^{\top}=\begin{pmatrix}4&2\\2&1+4\end{pmatrix}=\mathbf{A} .$$

Die Form ist $4x_1^2+4x_1x_2+5x_2^2=(2x_1+x_2)^2+(2x_2)^2$; die beiden Ausdrücke in den Quadraten sind die Komponenten von $\mathbf L^{\top}\mathbf{x}$. Die Determinante ist $20-4=16=(2\cdot2)^2$.
::::

⁠**Kurz gesagt:** Jede positiv definite Matrix ist $\mathbf L\mathbf L^{\top}$ mit einer unteren Dreiecksmatrix $\mathbf L$; die Zerlegung ist das quadratische Ergänzen in Matrixform.

:::aufgabe Aufgabe 24 ★ Definitheit prüfen
<span class="anker" id="aufg-24"></span>

Entscheide mit zwei verschiedenen Tests, ob die Matrizen positiv definit, positiv semidefinit, negativ definit oder indefinit sind:

$$\mathbf{A}_1=\begin{pmatrix}3&1\\1&2\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}2&6\\6&18\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&2\end{pmatrix},\qquad \mathbf{A}_4=\begin{pmatrix}-2&1\\1&-1\end{pmatrix}.$$

:::loesung
<ul>

<li>

$\mathbf{A}_1$: $a=3>0$ und $ac-b^2=6-1=5>0$: positiv definit. Eigenwerte: Spur $5$, Determinante $5$, $\lambda=\tfrac{5\pm\sqrt5}2\approx3{,}62$ und $1{,}38$, beide positiv.

</li>

<li>

$\mathbf{A}_2$: $a=2>0$, aber $ac-b^2=36-36=0$. Eigenwerte $20$ und $0$: positiv semidefinit, nicht definit. Ergänzt: $2(x_1+3x_2)^2$, eine Rinne.

</li>

<li>

$\mathbf{A}_3$: $ac-b^2=2-9=-7<0$; die Eigenwerte haben das Produkt $-7$, also verschiedene Vorzeichen: indefinit. Sie sind $\tfrac{3\pm\sqrt{37}}2\approx4{,}54$ und $-1{,}54$.

</li>

<li>

$\mathbf{A}_4$: $a=-2<0$, nicht positiv definit. Für $-\mathbf{A}_4=\bigl(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\bigr)$ ist $a=2>0$ und $ac-b^2=1>0$, also ist $-\mathbf{A}_4$ positiv definit und $\mathbf{A}_4$ negativ definit. Eigenwerte von $\mathbf{A}_4$: Spur $-3$, Determinante $1$, $\lambda=\tfrac{-3\pm\sqrt5}2\approx-0{,}38$ und $-2{,}62$, beide negativ: eine Kuppel.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 25 ★★ Eine Falle
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

Die Matrix $\bigl(\begin{smallmatrix}1&-4\\0&1\end{smallmatrix}\bigr)$ hat nur positive Eigenwerte. Ist ihre quadratische Form positiv? Finde einen Vektor, der das Gegenteil zeigt, und erkläre den Widerspruch.

</li>

<li>

Für welche Zahlen $t$ ist $\bigl(\begin{smallmatrix}1&t\\t&4\end{smallmatrix}\bigr)$ positiv definit? Für welche positiv semidefinit?

</li>

</ol>

:::loesung
(a) Die Eigenwerte sind $1$ und $1$, aber die Form $x_1^2-4x_1x_2+x_2^2$ ist bei $\mathbf{x}=(1,\,1)^{\top}$ gleich $1-4+1=-2<0$. Kein Widerspruch: Der Eigenwerttest gilt nur für symmetrische Matrizen. Die Form sieht nur den symmetrischen Anteil $\bigl(\begin{smallmatrix}1&-2\\-2&1\end{smallmatrix}\bigr)$, und der hat die Eigenwerte $3$ und $-1$; die Form ist indefinit.

(b) Mit dem $2\times2$-Test: $a=1>0$, und $ac-b^2=4-t^2>0$ genau für $|t|<2$. Für positiv semidefinit braucht man Eigenwerte $\ge0$. Ihre Summe ist die Spur $5>0$, ihr Produkt die Determinante $4-t^2$; beide sind genau dann $\ge0$, wenn $4-t^2\ge0$ ist, also für $|t|\le2$. Bei $t=\pm2$ ist die Matrix positiv semidefinit, aber nicht definit, mit den Eigenwerten $5$ und $0$; für $|t|>2$ ist sie indefinit.
:::
:::

:::aufgabe Aufgabe 26 ★★ Rayleigh-Quotient und Cholesky
<span class="anker" id="aufg-26"></span>

Es sei $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Berechne die Eigenwerte und den Rayleigh-Quotienten an den Stellen $\mathbf{e}_1$, $\mathbf{e}_2$ und $(1,\,1)^{\top}$. Prüfe [(8.2)](#gl-8-2).

</li>

<li>

Löse $\mathbf{A}\mathbf{x}=(2,\,9)^{\top}$ mit dem Cholesky-Faktor: zuerst $\mathbf L\mathbf{z}=(2,\,9)^{\top}$ von oben nach unten, dann $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ von unten nach oben.

</li>

</ol>

:::loesung
(a) Spur $9$, Determinante $16$: $\lambda=\tfrac{9\pm\sqrt{81-64}}2=\tfrac{9\pm\sqrt{17}}2\approx6{,}56$ und $2{,}44$. Der Rayleigh-Quotient ist bei $\mathbf{e}_1$ gleich $4$, bei $\mathbf{e}_2$ gleich $5$ und bei $(1,\,1)^{\top}$ gleich $\tfrac{4+2+2+5}2=\tfrac{13}2=6{,}5$. Alle drei liegen zwischen $2{,}44$ und $6{,}56$; der dritte liegt nahe am Maximum, denn $(1,\,1)^{\top}$ zeigt fast in die Richtung des Eigenvektors zum größeren Eigenwert.

(b) Aus Abschnitt [8.6](#stufe-8-6): $\mathbf L=\bigl(\begin{smallmatrix}2&0\\1&2\end{smallmatrix}\bigr)$. Von oben nach unten: $2z_1=2$, also $z_1=1$; $z_1+2z_2=9$, also $z_2=4$. Dann $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ von unten nach oben: $2x_2=4$, also $x_2=2$; $2x_1+x_2=1$, also $x_1=-\tfrac12$. Probe: $\mathbf{A}(-\tfrac12,\,2)^{\top}=(-2+4,\ -1+10)^{\top}=(2,\,9)^{\top}$. Zwei Dreieckssysteme ersetzen ein allgemeines Gleichungssystem.
:::
:::
