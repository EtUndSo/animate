---
title: Die Jacobi-Matrix
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Kapitel 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230600
summary: Viele Rechenschritte liefern nicht eine Zahl, sondern mehrere: Ein Matrix-Vektor-Produkt macht aus einem Vektor einen anderen.
tags: vektorwertig, Jacobi-Matrix
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Viele Rechenschritte liefern nicht eine Zahl, sondern mehrere: Ein Matrix-Vektor-Produkt macht aus einem Vektor einen anderen. Für solche Funktionen sammelt die Jacobi-Matrix die partiellen Ableitungen aller Ausgänge nach allen Eingängen. Sie ist die Matrix der linearen Näherung, und für die beiden häufigsten Bausteine, lineare Abbildungen und elementweise Funktionen, hat sie eine besonders einfache Form.
:::

### Funktionen mit mehreren Ausgängen

<span class="anker" id="stufe-5-1"></span>

In [Kapitel 1, Abschnitt 8](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8), bildete eine lineare Abbildung $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ Vektoren des $\mathbb{R}^n$ auf Vektoren des $\mathbb{R}^m$ ab, und in [Kapitel 1, Abschnitt 15.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/elementweise-rechnen-und-tensoren.html#stufe-15-2), wurde eine Funktion auf jede Komponente eines Vektors einzeln angewandt. In beiden Fällen kommen aus einem Vektor mehrere Zahlen heraus. Jede von ihnen ist für sich eine Funktion mehrerer Variablen.

:::definition Definition 5.1 (Vektorwertige Funktion)
<span class="anker" id="satz-5-1"></span>

Eine Funktion $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ ordnet jedem $\mathbf{x}\in\mathbb{R}^n$ einen Vektor

$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}g_1(\mathbf{x})\\ \vdots\\ g_m(\mathbf{x})\end{pmatrix}\in\mathbb{R}^m$$

zu; sie heißt __vektorwertig__. Die Funktionen $g_1,\dots,g_m:\mathbb{R}^n\to\mathbb{R}$ heißen ihre Komponenten.
:::

Vektorwertige Funktionen schreibt dieses Kapitel fett, wie Vektoren; Funktionen mit einer Zahl als Wert schreibt es mager.

::::beispiel [Rechenbeispiel]
Durch die Abschnitte [5](#stufe-5) und [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6) begleitet uns die Funktion $\mathbf{g}:\mathbb{R}^2\to\mathbb{R}^2$ mit

<span class="anker" id="gl-5-1"></span>
$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}x_1x_2\\ 2x_1+x_2^2\end{pmatrix},\qquad \mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix}. \tag{5.1}$$

Ihre Komponenten sind $g_1(\mathbf{x})=x_1x_2$ und $g_2(\mathbf{x})=2x_1+x_2^2$.
::::

⁠**Kurz gesagt:** Eine vektorwertige Funktion $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ besteht aus $m$ Funktionen von $n$ Variablen, einer für jeden Ausgang.

### Die Jacobi-Matrix

<span class="anker" id="stufe-5-2"></span>

Jede Komponente $g_i$ hat $n$ partielle Ableitungen, eine nach jedem Eingang. Zusammen sind das $m\cdot n$ Zahlen. Man ordnet sie in einer Tabelle mit einer Zeile je Ausgang und einer Spalte je Eingang an.

:::definition Definition 5.2 (Jacobi-Matrix)
<span class="anker" id="satz-5-2"></span>

Existieren alle partiellen Ableitungen der Komponenten von $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ an der Stelle $\mathbf{x}$, so heißt die $m\times n$-Matrix

<span class="anker" id="gl-5-2"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{pmatrix},\qquad \bigl(\mathbf{J}_{\mathbf{g}}(\mathbf{x})\bigr)_{ij}=\frac{\partial g_i}{\partial x_j}(\mathbf{x}), \tag{5.2}$$

die __Jacobi-Matrix__ von $\mathbf{g}$ an der Stelle $\mathbf{x}$.
:::

Die Zeile $i$ gehört zum Ausgang $g_i$; sie ist sein Gradient, als Zeile geschrieben: $\nabla g_i(\mathbf{x})^{\top}$. Die Spalte $j$ gehört zum Eingang $x_j$; sie sagt, wie alle Ausgänge zugleich reagieren, wenn man nur $x_j$ verändert. Für eine Funktion $f:\mathbb{R}^n\to\mathbb{R}$ mit einem einzigen Ausgang ist die Jacobi-Matrix eine $1\times n$-Matrix, nämlich der Gradient als Zeile: $\mathbf{J}_f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}$. Die Matrix ist nach dem Mathematiker Carl Gustav Jacob Jacobi benannt.

::::beispiel [Rechenbeispiel]
Für $\mathbf{g}$ aus [(5.1)](#gl-5-1) ist

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}x_2&x_1\\2&2x_2\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}.$$

Die erste Spalte $(2,\,2)^{\top}$ sagt: Wächst $x_1$ um ein kleines $h$, wachsen beide Ausgänge um etwa $2h$. Die zweite Spalte $(1,\,4)^{\top}$ sagt: Wächst $x_2$, reagiert der zweite Ausgang viermal so stark wie der erste.
::::

⁠**Kurz gesagt:** Die Jacobi-Matrix hat eine Zeile je Ausgang und eine Spalte je Eingang; ihr Eintrag $(i,j)$ ist $\partial g_i/\partial x_j$.

### Die lineare Näherung mit der Jacobi-Matrix

<span class="anker" id="stufe-5-3"></span>

Jede Komponente hat ihre lineare Näherung [(3.4)](partielle-ableitungen-und-der-gradient.html#gl-3-4). Schreibt man alle $m$ Näherungen untereinander, so stehen links die Komponenten von $\mathbf{g}(\mathbf{x}+\mathbf{h})$ und rechts die Zeilen der Jacobi-Matrix mal $\mathbf{h}$. Das ist nach der Zeilensicht aus [Kapitel 1, Abschnitt 7.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2), ein Matrix-Vektor-Produkt.

:::satz Satz 5.3 (Lineare Näherung einer vektorwertigen Funktion)
<span class="anker" id="satz-5-3"></span>

Ist jede Komponente von $\mathbf{g}$ an der Stelle $\mathbf{x}$ differenzierbar, so gilt

<span class="anker" id="gl-5-3"></span>
$$\mathbf{g}(\mathbf{x}+\mathbf{h})=\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}+\mathbf{r}(\mathbf{h})\qquad\text{mit}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{\lVert\mathbf{r}(\mathbf{h})\rVert}{\lVert\mathbf{h}\rVert}=0 . \tag{5.3}$$
:::

:::beweis Lineare Näherung einer vektorwertigen Funktion
Die Komponente $i$ von $\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ ist $\nabla g_i(\mathbf{x})^{\top}\mathbf{h}$. Nach der Definition der Differenzierbarkeit [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5) geht für jedes $i$ der Quotient $r_i(\mathbf{h})/\lVert\mathbf{h}\rVert$ gegen $0$. Weil $\lVert\mathbf{r}\rVert\le|r_1|+\dots+|r_m|$ ist, geht auch $\lVert\mathbf{r}(\mathbf{h})\rVert/\lVert\mathbf{h}\rVert$ gegen $0$.
:::

In der Nähe von $\mathbf{x}$ wirkt $\mathbf{g}$ also wie die lineare Abbildung $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$, und nach [Kapitel 1, Abschnitt 8.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2), gehört zu jeder linearen Abbildung genau eine Matrix. Die Jacobi-Matrix ist diese Matrix. Unter der Lupe verformt $\mathbf{g}$ ein kleines Gitter um $\mathbf{x}$ so, wie die Matrix $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ das Einheitsgitter verformt: Es wird gedreht, gestreckt oder geschert, aber gerade Linien bleiben fast gerade.

::::beispiel [Rechenbeispiel]
Für $\mathbf{g}$ aus [(5.1)](#gl-5-1) an der Stelle $(1,\,2)$ und $\mathbf{h}=(0{,}1;\ -0{,}1)^{\top}$ ist

$$\mathbf{J}_{\mathbf{g}}(1,2)\,\mathbf{h}=\begin{pmatrix}2\cdot0{,}1+1\cdot(-0{,}1)\\2\cdot0{,}1+4\cdot(-0{,}1)\end{pmatrix}=\begin{pmatrix}0{,}1\\-0{,}2\end{pmatrix}, \qquad \mathbf{g}(1{,}1;\ 1{,}9)\approx\begin{pmatrix}2{,}1\\5{,}8\end{pmatrix}.$$

Genau ist $\mathbf{g}(1{,}1;\ 1{,}9)=(2{,}09;\ 5{,}81)^{\top}$. Abb. [10](#abb-10) zeigt das Produkt Zeile für Zeile.

:::abbildung ml/k3rjacobi 10
Die Änderung der linearen Näherung von $\mathbf{g}$ an der Stelle $\mathbf{x}=(1,\,2)^{\top}$ als Matrix-Vektor-Produkt: Jede Zeile ist das Skalarprodukt aus dem Gradienten eines Ausgangs und der Verschiebung.
:::
::::

⁠**Kurz gesagt:** Nahe bei $\mathbf{x}$ ist $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$; die Jacobi-Matrix ist die Matrix der linearen Abbildung, als die $\mathbf{g}$ im Kleinen wirkt.

### Zwei wichtige Jacobi-Matrizen

<span class="anker" id="stufe-5-4"></span>

Zwei Bausteine kommen in Rechnungen mit Daten ständig vor: das Matrix-Vektor-Produkt und Funktionen, die man auf jede Komponente einzeln anwendet. Ihre Jacobi-Matrizen braucht man immer wieder, und beide lassen sich ohne Rechnung angeben.

:::satz Satz 5.4 (Jacobi-Matrizen der Bausteine)
<span class="anker" id="satz-5-4"></span>

<ol class="al">

<li>

Für $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ mit $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{b}\in\mathbb{R}^m$ ist $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\mathbf{A}$ an jeder Stelle.

</li>

<li>

Wendet $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^n$ eine differenzierbare Funktion $\varphi$ einer Variablen auf jede Komponente an, $g_i(\mathbf{x})=\varphi(x_i)$, so ist

<span class="anker" id="gl-5-4"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\operatorname{diag}\bigl(\varphi'(x_1),\,\dots,\,\varphi'(x_n)\bigr). \tag{5.4}$$

</li>

</ol>
:::

:::beweis Jacobi-Matrizen der Bausteine
(a) Die Komponente $i$ ist $g_i(\mathbf{x})=\sum_ka_{ik}x_k+b_i$. Nach $x_j$ abgeleitet bleibt nur der Summand mit $k=j$, also $\partial g_i/\partial x_j=a_{ij}$. (b) Die Komponente $g_i=\varphi(x_i)$ hängt nur von $x_i$ ab. Ihre Ableitung nach $x_j$ ist deshalb $0$ für $j\ne i$ und $\varphi'(x_i)$ für $j=i$.
:::

Beide Ergebnisse haben einen einfachen Grund. Eine affine Abbildung ist schon linear bis auf die Verschiebung $\mathbf{b}$; ihre beste lineare Näherung ist sie selbst ohne $\mathbf{b}$. Bei einer elementweisen Funktion wirkt jeder Eingang nur auf seinen eigenen Ausgang; alle Einträge außerhalb der Diagonale sind null, weil es keine Verbindungen zwischen verschiedenen Komponenten gibt.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\bigr)$ ist die Jacobi-Matrix von $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ überall $\mathbf{A}$ selbst. Quadriert man jede Komponente, $\varphi(t)=t^2$, so ist an der Stelle $\mathbf{x}=(1,\,-2,\,3)^{\top}$ die Jacobi-Matrix $\operatorname{diag}(2;\,-4;\,6)$. Wendet man die logistische Funktion auf jede Komponente von $\mathbf{x}=(0,\,2)^{\top}$ an, so ist sie nach [(2.4)](die-kettenregel.html#gl-2-4) $\operatorname{diag}\bigl(\sigma'(0);\,\sigma'(2)\bigr)\approx\operatorname{diag}(0{,}25;\ 0{,}105)$.
::::

⁠**Kurz gesagt:** Die Jacobi-Matrix von $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}+\mathbf{b}$ ist $\mathbf{A}$; die einer elementweisen Funktion ist die Diagonalmatrix der einzelnen Ableitungen.

:::hintergrund Die Determinante der Jacobi-Matrix als Flächenfaktor
Nach [Kapitel 1, Abschnitt 14.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-3), vervielfacht eine lineare Abbildung den Flächeninhalt jeder Figur um denselben Faktor $|\det\mathbf{A}|$. Weil $\mathbf{g}$ im Kleinen wie $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ wirkt, gilt das ungefähr auch für $\mathbf{g}$: Ein kleines Quadrat um $\mathbf{x}$ mit dem Flächeninhalt $F$ geht in eine Figur über, die fast ein Parallelogramm mit dem Flächeninhalt $|\det\mathbf{J}_{\mathbf{g}}(\mathbf{x})|\cdot F$ ist. Für $\mathbf{g}$ aus [(5.1)](#gl-5-1) ist $\det\mathbf{J}_{\mathbf{g}}(1,2)=2\cdot4-1\cdot2=6$: In der Nähe von $(1,\,2)$ vergrößert $\mathbf{g}$ Flächen etwa auf das Sechsfache. Ein bekanntes Beispiel sind Polarkoordinaten, $\mathbf{g}(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)^{\top}$. Ihre Jacobi-Matrix hat die Spalten $(\cos\varphi,\,\sin\varphi)^{\top}$ und $(-r\sin\varphi,\,r\cos\varphi)^{\top}$ und die Determinante $r\cos^2\varphi+r\sin^2\varphi=r$. Ein kleines Rechteck der Seiten $\Delta r$ und $\Delta\varphi$ wird zu einem Stück eines Kreisrings mit dem Flächeninhalt etwa $r\,\Delta r\,\Delta\varphi$, weil der Bogen zum Winkel $\Delta\varphi$ im Abstand $r$ die Länge $r\,\Delta\varphi$ hat.
:::

:::aufgabe Aufgabe 17 ★ Jacobi-Matrizen berechnen
<span class="anker" id="aufg-17"></span>

Berechne die Jacobi-Matrix an der angegebenen Stelle.

<ol class="al">

<li>

$\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1-x_2,\ x_1x_2)^{\top}$ an der Stelle $(3,\,1)$;

</li>

<li>

$\mathbf{g}(\mathbf{x})=(\mathrm{e}^{x_1},\,\mathrm{e}^{x_2},\,\mathrm{e}^{x_3})^{\top}$ an der Stelle $(0,\,1,\,-1)$;

</li>

<li>

$f(\mathbf{x})=x_1^2x_2+x_2^2$ aus [(3.1)](partielle-ableitungen-und-der-gradient.html#gl-3-1) an der Stelle $(1,\,2)$. Welche Form hat die Matrix, und was ist sie?

</li>

</ol>

:::loesung
(a) Die Jacobi-Matrix hat drei Zeilen und zwei Spalten:

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}1&1\\1&-1\\x_2&x_1\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(3,1)=\begin{pmatrix}1&1\\1&-1\\1&3\end{pmatrix}.$$

(b) Die Funktion ist elementweise; nach [(5.4)](#gl-5-4) ist $\mathbf{J}=\operatorname{diag}(\mathrm{e}^0;\,\mathrm{e}^1;\,\mathrm{e}^{-1})\approx\operatorname{diag}(1;\ 2{,}718;\ 0{,}368)$.

(c) Eine Funktion mit einem Ausgang hat eine $1\times2$-Jacobi-Matrix, den Gradienten als Zeile: $\mathbf{J}_f(1,2)=(4\ \ 5)=\nabla f(1,2)^{\top}$.
:::
:::

:::aufgabe Aufgabe 18 ★★ Lineare Näherung einer Abbildung der Ebene
<span class="anker" id="aufg-18"></span>

Es sei $\mathbf{g}(\mathbf{x})=(x_1^2-x_2,\ x_1x_2)^{\top}$.

<ol class="al">

<li>

Berechne $\mathbf{J}_{\mathbf{g}}(2,1)$ und damit einen Näherungswert für $\mathbf{g}(2{,}05;\ 0{,}9)$. Vergleiche mit dem genauen Wert.

</li>

<li>

Wie muss man die Eingänge verschieben, damit sich der erste Ausgang ändert, der zweite in linearer Näherung aber gar nicht? Gib eine solche Verschiebung $\mathbf{h}$ an.

</li>

</ol>

:::loesung
(a) $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}2x_1&-1\\x_2&x_1\end{smallmatrix}\bigr)$, also $\mathbf{J}_{\mathbf{g}}(2,1)=\bigl(\begin{smallmatrix}4&-1\\1&2\end{smallmatrix}\bigr)$, und $\mathbf{g}(2,1)=(3,\,2)^{\top}$. Mit $\mathbf{h}=(0{,}05;\ -0{,}1)^{\top}$ ist

$$\mathbf{J}_{\mathbf{g}}\mathbf{h}=\begin{pmatrix}0{,}2+0{,}1\\0{,}05-0{,}2\end{pmatrix}=\begin{pmatrix}0{,}3\\-0{,}15\end{pmatrix},\qquad \mathbf{g}(2{,}05;\ 0{,}9)\approx\begin{pmatrix}3{,}3\\1{,}85\end{pmatrix}.$$

Genau ist $\mathbf{g}(2{,}05;\ 0{,}9)=(4{,}2025-0{,}9;\ 1{,}845)^{\top}=(3{,}3025;\ 1{,}845)^{\top}$.

(b) Der zweite Ausgang ändert sich in linearer Näherung um $h_1+2h_2$; das ist null für $\mathbf{h}$ in Richtung $(2,\,-1)^{\top}$. Bei einem Schritt um genau diesen Vektor ändert sich dann der erste Ausgang um $4\cdot2-1\cdot(-1)=9$. Es müssen sich also beide Eingänge ändern: $x_1$ wächst, $x_2$ fällt halb so viel, etwa $\mathbf{h}=(0{,}02;\ -0{,}01)^{\top}$ mit der Wirkung $(0{,}09;\ 0)^{\top}$.
:::
:::

:::aufgabe Aufgabe 19 ★★★ Wie stark $\mathbf{g}$ Flächen vergrößert
<span class="anker" id="aufg-19"></span>

Es sei $\mathbf{g}$ wie in [(5.1)](#gl-5-1).

<ol class="al">

<li>

Berechne die Bilder der vier Ecken des Quadrats mit den Ecken $(1,\,2)$, $(1{,}1;\ 2)$, $(1{,}1;\ 2{,}1)$ und $(1;\ 2{,}1)$.

</li>

<li>

Die Bilder bilden fast ein Parallelogramm. Schätze seinen Flächeninhalt mit den Bildern der beiden Kanten, die von $\mathbf{g}(1,2)$ ausgehen, und vergleiche mit $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01$.

</li>

</ol>

:::loesung
(a) Mit $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$:

$$\mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2)=\begin{pmatrix}2{,}2\\6{,}2\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2{,}1)=\begin{pmatrix}2{,}31\\6{,}61\end{pmatrix},\quad \mathbf{g}(1;\,2{,}1)=\begin{pmatrix}2{,}1\\6{,}41\end{pmatrix}.$$

(b) Die Bilder der beiden Kanten, die von $\mathbf{g}(1,2)$ ausgehen, sind $(0{,}2;\ 0{,}2)^{\top}$ und $(0{,}1;\ 0{,}41)^{\top}$. Das von ihnen aufgespannte Parallelogramm hat nach [Kapitel 1, Abschnitt 14.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-1), den Flächeninhalt $|0{,}2\cdot0{,}41-0{,}1\cdot0{,}2|=0{,}062$. Die Jacobi-Matrix sagt $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01=6\cdot0{,}01=0{,}06$ voraus. Die Abweichung kommt daher, dass das Quadrat nicht beliebig klein ist; die vierte Ecke liegt mit $(2{,}31;\ 6{,}61)$ auch nur fast dort, wo ein echtes Parallelogramm sie hätte, bei $(2{,}3;\ 6{,}61)$.
:::
:::
