---
title: Orthonormalbasen und orthogonale Matrizen
pfad: Informatik / Machine Learning / Projektion, Eigenwerte und Zerlegungen
order: 6220200
summary: Manche Koordinatensysteme sind besonders bequem: Ihre Achsen stehen senkrecht aufeinander, und die Einheit ist auf jeder Achse gleich lang.
tags: orthonormal, Orthonormalbasis, orthogonale Matrix
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Manche Koordinatensysteme sind besonders bequem: Ihre Achsen stehen senkrecht aufeinander, und die Einheit ist auf jeder Achse gleich lang. In einem solchen System braucht man kein Gleichungssystem, um die Koordinaten eines Punkts zu finden, und Längen rechnet man mit dem Satz des Pythagoras. Dieser Abschnitt führt solche Koordinatensysteme ein und die Matrizen, die zu ihnen gehören.
:::

### Orthonormale Vektoren

<span class="anker" id="stufe-1-1"></span>

In [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 5.3, hießen zwei Vektoren orthogonal, wenn ihr Skalarprodukt null ist. Das Gleichmuster $(1,1,1,1)^{\top}$ und das Wechselmuster $(1,-1,1,-1)^{\top}$ waren ein Beispiel: Der Vergleich eines Signals mit dem einen Muster wurde vom anderen Muster nicht gestört. Er lieferte allerdings den Anteil mal $4$, weil beide Muster die Länge $2$ haben. Haben orthogonale Vektoren zusätzlich die Länge $1$, so fällt auch dieser Faktor weg.

Man stelle sich die beiden Achsen $\mathbf{e}_1$ und $\mathbf{e}_2$ der Ebene vor, als Ganzes um einen Winkel gedreht. Die beiden Pfeile haben weiterhin die Länge $1$ und stehen weiterhin senkrecht aufeinander, nur zeigen sie in andere Richtungen.

:::definition Definition 1.1 (Orthonormal)
<span class="anker" id="satz-1-1"></span>

Vektoren $\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathbb{R}^n$ heißen __orthonormal__, wenn jeder von ihnen die Länge $1$ hat und je zwei verschiedene von ihnen orthogonal sind:

<span class="anker" id="gl-1-1"></span>
$$\mathbf{q}_i^{\top}\mathbf{q}_l=\begin{cases}1, & i=l,\\ 0, & i\ne l.\end{cases} \tag{1.1}$$
:::

Das Wort setzt sich aus „orthogonal“ und „normiert“ zusammen. Die Einheitsvektoren $\mathbf{e}_1,\dots,\mathbf{e}_n$ sind das einfachste Beispiel.

:::satz Satz 1.2 (Orthonormale Vektoren sind linear unabhängig)
<span class="anker" id="satz-1-2"></span>

Sind $\mathbf{q}_1,\dots,\mathbf{q}_k$ orthonormal, so sind sie linear unabhängig.
:::

:::beweis Lineare Unabhängigkeit
Es sei $c_1\mathbf{q}_1+\dots+c_k\mathbf{q}_k=\mathbf{0}$. Man bildet das Skalarprodukt beider Seiten mit $\mathbf{q}_l$. Nach [(1.1)](#gl-1-1) bleibt links nur der Summand $c_l\,\mathbf{q}_l^{\top}\mathbf{q}_l=c_l$ übrig, rechts steht $\mathbf{q}_l^{\top}\mathbf{0}=0$. Also ist $c_l=0$, und zwar für jedes $l$. Nach der Definition in [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.2, sind die Vektoren damit linear unabhängig.
:::

⁠**Rechenbeispiel:** Für $\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ und $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ ist

$$\mathbf{q}_1^{\top}\mathbf{q}_1=0{,}36+0{,}64=1,\qquad \mathbf{q}_2^{\top}\mathbf{q}_2=0{,}64+0{,}36=1,\qquad \mathbf{q}_1^{\top}\mathbf{q}_2=-0{,}48+0{,}48=0 .$$

Die beiden Vektoren sind orthonormal; Abb. [1](#abb-1) zeigt das letzte Skalarprodukt Schritt für Schritt. Das Gleich- und das Wechselmuster werden orthonormal, wenn man sie durch ihre Länge $2$ teilt: $\tfrac12(1,1,1,1)^{\top}$ und $\tfrac12(1,-1,1,-1)^{\top}$.

:::abbildung ml/k2rorth 1
Das Skalarprodukt $\mathbf{q}_1^{\top}\mathbf{q}_2$ Schritt für Schritt, mit $0{,}6=\tfrac35$ und $0{,}8=\tfrac45$: Komponente mal Komponente, dann die Summe.
:::

⁠**Kurz gesagt:** Orthonormale Vektoren haben die Länge $1$ und stehen paarweise senkrecht aufeinander; sie sind immer linear unabhängig.

### Orthonormalbasen

<span class="anker" id="stufe-1-2"></span>

Eine Basis ist nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.3, ein Koordinatensystem: Jeder Vektor hat in ihr genau eine Darstellung. Am bequemsten sind Basen, deren Vektoren orthonormal sind. Sie sind wie das gewohnte Achsenkreuz, nur gedreht.

:::definition Definition 1.3 (Orthonormalbasis)
<span class="anker" id="satz-1-3"></span>

Eine Basis aus orthonormalen Vektoren heißt __Orthonormalbasis__.
:::

Für den ganzen $\mathbb{R}^n$ genügt es, $n$ orthonormale Vektoren zu finden. Sie sind nach dem Satz im vorigen Unterabschnitt linear unabhängig. Schreibt man sie als Spalten in eine $n\times n$-Matrix, so hat diese den Rang $n$, und ihr Spaltenraum ist nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.5, der ganze $\mathbb{R}^n$. Also spannen die $n$ Vektoren den $\mathbb{R}^n$ auf und bilden eine Basis. Ebenso kann man für einen Spann, etwa eine Ebene im $\mathbb{R}^3$, eine Orthonormalbasis suchen: orthonormale Vektoren, die genau diesen Spann aufspannen.

⁠**Rechenbeispiel:** Die Vektoren $\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ und $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ sind zwei orthonormale Vektoren im $\mathbb{R}^2$, also eine Orthonormalbasis des $\mathbb{R}^2$. Die Einheitsvektoren $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ bilden die Orthonormalbasis des $\mathbb{R}^3$, die man Standardbasis nennt. Die Ebene $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ im $\mathbb{R}^3$ hat die Orthonormalbasis $\mathbf{e}_1,\mathbf{e}_2$.

⁠**Kurz gesagt:** Eine Orthonormalbasis ist ein gedrehtes Achsenkreuz: $n$ orthonormale Vektoren im $\mathbb{R}^n$ bilden immer eine Basis.

### Koordinaten in einer Orthonormalbasis

<span class="anker" id="stufe-1-3"></span>

In einer gewöhnlichen Basis muss man ein Gleichungssystem lösen, um die Koordinaten eines Vektors zu finden. In [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.3, hatte $(3,\,2)^{\top}$ in der Basis $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ die Koordinaten $1$ und $2$. Die Skalarprodukte $(1,0)(3,2)^{\top}=3$ und $(1,1)(3,2)^{\top}=5$ sind etwas ganz anderes. In einer Orthonormalbasis dagegen sind die Koordinaten genau die Skalarprodukte.

Den Grund zeigt das Bild der Schattenlänge aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 5.5. Für einen normierten Vektor $\mathbf{q}$ ist $\mathbf{q}^{\top}\mathbf{x}$ die Länge des Schattens von $\mathbf{x}$ auf der Geraden in Richtung $\mathbf{q}$. In einer Orthonormalbasis ist jede Koordinate der Schatten auf der eigenen Achse (Abb. [2](#abb-2)).

:::abbildung ml/k2onb 2
Koordinaten in der Orthonormalbasis $\mathbf{q}_1=(0{,}6;\,0{,}8)^{\top}$, $\mathbf{q}_2=(-0{,}8;\,0{,}6)^{\top}$ (grün). Der Pfeil $\mathbf{x}=(3,1)^{\top}$ wirft auf jede der beiden gedrehten Achsen (grau) einen Schatten, das Licht fällt jeweils senkrecht (gestrichelt). Die Schattenlängen $\mathbf{q}_1^{\top}\mathbf{x}=2{,}6$ (blau) und $\mathbf{q}_2^{\top}\mathbf{x}=-1{,}8$ (orange) sind die Koordinaten: $\mathbf{x}=2{,}6\,\mathbf{q}_1-1{,}8\,\mathbf{q}_2$.
:::

:::satz Satz 1.4 (Koordinaten in einer Orthonormalbasis)
<span class="anker" id="satz-1-4"></span>

Ist $\mathbf{q}_1,\dots,\mathbf{q}_n$ eine Orthonormalbasis des $\mathbb{R}^n$, so gilt für jeden Vektor $\mathbf{x}\in\mathbb{R}^n$

<span class="anker" id="gl-1-2"></span>
$$\mathbf{x}=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})\,\mathbf{q}_i\qquad\text{und}\qquad \lVert\mathbf{x}\rVert^2=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})^2 . \tag{1.2}$$
:::

:::beweis Koordinaten in einer Orthonormalbasis
Weil die Vektoren eine Basis bilden, gibt es Zahlen $c_1,\dots,c_n$ mit $\mathbf{x}=\sum_ic_i\mathbf{q}_i$. Das Skalarprodukt mit $\mathbf{q}_l$ ergibt nach [(1.1)](#gl-1-1)

$$\mathbf{q}_l^{\top}\mathbf{x}=\sum_{i=1}^nc_i\,\mathbf{q}_l^{\top}\mathbf{q}_i=c_l ,$$

denn nur der Summand mit $i=l$ ist nicht null. Für die Länge multipliziert man aus:

$$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^nc_i\,c_l\,\mathbf{q}_i^{\top}\mathbf{q}_l=\sum_{i=1}^nc_i^2 ,$$

wieder, weil nur die Summanden mit $i=l$ übrig bleiben.
:::

Die zweite Formel ist der Satz des Pythagoras im $\mathbb{R}^n$: Die Länge eines Pfeils ergibt sich aus seinen Koordinaten in jedem rechtwinkligen Achsenkreuz gleich, solange die Einheit auf allen Achsen die Länge $1$ hat.

⁠**Rechenbeispiel:** Für $\mathbf{x}=(3,\,1)^{\top}$ und die Basis aus dem vorigen Unterabschnitt ist

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=1{,}8+0{,}8=2{,}6,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=-2{,}4+0{,}6=-1{,}8 .$$

Probe: $2{,}6\,(0{,}6;\ 0{,}8)^{\top}-1{,}8\,(-0{,}8;\ 0{,}6)^{\top}=(1{,}56+1{,}44;\ 2{,}08-1{,}08)^{\top}=(3,\,1)^{\top}$. Und $c_1^2+c_2^2=6{,}76+3{,}24=10=\lVert\mathbf{x}\rVert^2$. Abb. [3](#abb-3) zeigt die drei Summen mit Brüchen.

:::abbildung ml/k2rkoord 3
Die Koordinaten $c_1=\tfrac{13}5=2{,}6$ und $c_2=-\tfrac95=-1{,}8$ von $\mathbf{x}$ als Skalarprodukte und die Summe ihrer Quadrate, das Längenquadrat von $\mathbf{x}$.
:::

⁠**Kurz gesagt:** In einer Orthonormalbasis ist jede Koordinate ein Skalarprodukt, $c_i=\mathbf{q}_i^{\top}\mathbf{x}$, und die Summe der quadrierten Koordinaten ist das Längenquadrat.

:::hintergrund Abgetastete Schwingungen als Orthonormalbasis und der Satz von Parseval
Die vier Vektoren

$$\begin{gathered} \mathbf{q}_1=\tfrac12(1,\,1,\,1,\,1)^{\top},\qquad \mathbf{q}_2=\tfrac1{\sqrt2}(1,\,0,\,-1,\,0)^{\top},\\ \mathbf{q}_3=\tfrac1{\sqrt2}(0,\,1,\,0,\,-1)^{\top},\qquad \mathbf{q}_4=\tfrac12(1,\,-1,\,1,\,-1)^{\top} \end{gathered}$$

sind die Abtastwerte eines Gleichanteils, einer Kosinus- und einer Sinusschwingung mit einer Periode in vier Takten und einer Schwingung, die bei jedem Takt das Vorzeichen wechselt, jeweils normiert. Man prüft leicht nach, dass sie orthonormal sind. Sie bilden also eine Orthonormalbasis des $\mathbb{R}^4$. Jedes Signal mit vier Abtastwerten ist eine Summe dieser vier Schwingungen, und die Anteile sind nach [(1.2)](#gl-1-2) einfach Skalarprodukte. Für das Signal $\mathbf{x}=(4,\,2,\,0,\,2)^{\top}$ ist $\mathbf{q}_1^{\top}\mathbf{x}=4$, $\mathbf{q}_2^{\top}\mathbf{x}=4/\sqrt2=2\sqrt2$, $\mathbf{q}_3^{\top}\mathbf{x}=0$ und $\mathbf{q}_4^{\top}\mathbf{x}=0$: Das Signal besteht nur aus Gleichanteil und Kosinus.

Die zweite Formel in [(1.2)](#gl-1-2) sagt, dass die Energie $\lVert\mathbf{x}\rVert^2=24$ des Signals gleich der Summe der quadrierten Anteile ist, $16+8+0+0=24$. In der Signalverarbeitung heißt diese Aussage Satz von Parseval. Die diskrete Fourier-Transformation ist dieselbe Zerlegung mit komplexen Schwingungen. Ihre Matrix für $N$ Abtastwerte erhält Längen genau dann, wenn man sie mit $1/\sqrt N$ normiert; ohne diesen Faktor steht im Satz von Parseval zusätzlich der Faktor $N$.
:::

### Orthogonale Matrizen

<span class="anker" id="stufe-1-4"></span>

Schreibt man die Vektoren einer Orthonormalbasis als Spalten in eine Matrix $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$, so lassen sich beide Formeln [(1.2)](#gl-1-2) als Matrixprodukte schreiben. Alle Koordinaten zugleich sind nach der Zeilensicht aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 7.2, der Vektor $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, denn die Zeilen von $\mathbf{Q}^{\top}$ sind die Vektoren $\mathbf{q}_i^{\top}$. Umgekehrt ist $\mathbf{x}=\sum_ic_i\mathbf{q}_i=\mathbf{Q}\mathbf{c}$ nach der Spaltensicht. Die Matrix $\mathbf{Q}^{\top}$ macht also rückgängig, was $\mathbf{Q}$ tut.

:::definition Definition 1.5 (Orthogonale Matrix)
<span class="anker" id="satz-1-5"></span>

Eine quadratische Matrix $\mathbf{Q}\in\mathbb{R}^{n\times n}$, deren Spalten orthonormal sind, heißt __orthogonale Matrix__. Gleichwertig: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.
:::

Die beiden Formulierungen sind gleichwertig, weil der Eintrag $(i,l)$ von $\mathbf{Q}^{\top}\mathbf{Q}$ das Skalarprodukt $\mathbf{q}_i^{\top}\mathbf{q}_l$ der Spalten $i$ und $l$ ist. Die Bedingung $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ ist also genau [(1.1)](#gl-1-1).

:::satz Satz 1.6 (Die Inverse einer orthogonalen Matrix)
<span class="anker" id="satz-1-6"></span>

Ist $\mathbf{Q}$ orthogonal, so ist $\mathbf{Q}$ invertierbar mit $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$. Außerdem ist $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$; auch die Zeilen von $\mathbf{Q}$ sind also orthonormal, und $\mathbf{Q}^{\top}$ ist ebenfalls orthogonal.
:::

:::beweis Inverse einer orthogonalen Matrix
Die Spalten sind orthonormal, nach dem ersten Unterabschnitt also linear unabhängig. Nach dem Satz in [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.5, ist $\mathbf{Q}$ deshalb invertierbar. Multipliziert man $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ von rechts mit $\mathbf{Q}^{-1}$, so folgt $\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, und damit ist auch $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{Q}\mathbf{Q}^{-1}=\mathbf{I}$.
:::

Ein Wort zum Namen. Eine orthogonale Matrix hat orthonormale Spalten, nicht bloß orthogonale; der Name ist historisch gewachsen. Für Matrizen, deren Spalten nur orthogonal, aber nicht normiert sind, gibt es keinen eigenen Namen. Für sie ist $\mathbf{Q}^{\top}\mathbf{Q}$ eine Diagonalmatrix mit den Längenquadraten der Spalten auf der Diagonale, aber nicht $\mathbf{I}$.

⁠**Rechenbeispiel:** Mit den Vektoren aus dem ersten Unterabschnitt als Spalten ist

$$\mathbf{Q}=\begin{pmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{pmatrix},\qquad \mathbf{Q}^{\top}\mathbf{Q}=\begin{pmatrix}0{,}36+0{,}64&-0{,}48+0{,}48\\-0{,}48+0{,}48&0{,}64+0{,}36\end{pmatrix}=\mathbf{I} .$$

Die Einträge von $\mathbf{Q}^{\top}\mathbf{Q}$ sind die Skalarprodukte der Spalten aus dem ersten Unterabschnitt; den Eintrag außerhalb der Diagonale zeigt Abb. [1](#abb-1). Also ist $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, ohne Rechnung. Diese Matrix ist die Drehmatrix aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 8.3, mit $\cos\alpha=0{,}6$ und $\sin\alpha=0{,}8$, also eine Drehung um $\alpha\approx53{,}13^\circ$ gegen den Uhrzeigersinn. Die Inverse $\mathbf{Q}^{\top}$ dreht um denselben Winkel zurück.

⁠**Kurz gesagt:** Eine orthogonale Matrix ist quadratisch mit orthonormalen Spalten; ihre Inverse ist einfach ihre Transponierte.

### Längen und Winkel bleiben erhalten

<span class="anker" id="stufe-1-5"></span>

Eine Drehung ändert weder die Länge eines Pfeils noch den Winkel zwischen zwei Pfeilen. Diese Eigenschaft haben alle orthogonalen Matrizen, und sie ist der Grund, warum man so gern mit ihnen rechnet.

:::satz Satz 1.7 (Orthogonale Matrizen erhalten Skalarprodukte)
<span class="anker" id="satz-1-7"></span>

Ist $\mathbf{Q}$ orthogonal, so gilt für alle $\mathbf{x},\mathbf{y}\in\mathbb{R}^n$

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{y},\qquad \lVert\mathbf{Q}\mathbf{x}\rVert=\lVert\mathbf{x}\rVert , \tag{1.3}$$

und der Winkel zwischen $\mathbf{Q}\mathbf{x}$ und $\mathbf{Q}\mathbf{y}$ ist derselbe wie der zwischen $\mathbf{x}$ und $\mathbf{y}$. Die Determinante ist $\det\mathbf{Q}=1$ oder $\det\mathbf{Q}=-1$.
:::

:::beweis Erhaltung von Skalarprodukten
Nach der Regel $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 10.1, ist $(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{y}=\mathbf{x}^{\top}\mathbf{I}\mathbf{y}=\mathbf{x}^{\top}\mathbf{y}$. Mit $\mathbf{y}=\mathbf{x}$ folgt die Aussage über die Länge, und weil der Winkel nur aus Skalarprodukten und Längen berechnet wird, bleibt auch er gleich. Für die Determinante benutzt man die Rechenregeln aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 14.5: $1=\det\mathbf{I}=\det(\mathbf{Q}^{\top}\mathbf{Q})=\det\mathbf{Q}^{\top}\cdot\det\mathbf{Q}=(\det\mathbf{Q})^2$.
:::

Eine orthogonale Matrix bewegt den Raum also starr, ohne ihn zu verzerren. Ist $\det\mathbf{Q}=1$, ist sie eine Drehung. Ist $\det\mathbf{Q}=-1$, enthält sie eine Spiegelung, denn nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 14.2, kehrt eine negative Determinante die Orientierung um.

⁠**Rechenbeispiel:** Die Drehung aus dem vorigen Unterabschnitt bildet $\mathbf{x}=(3,\,1)^{\top}$ auf $\mathbf{Q}\mathbf{x}=(1{,}8-0{,}8;\ 2{,}4+0{,}6)^{\top}=(1,\,3)^{\top}$ ab. Beide Vektoren haben das Längenquadrat $10$. Die Determinante der Drehung ist $0{,}36+0{,}64=1$. Die Matrix $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ hat ebenfalls orthonormale Spalten, aber die Determinante $-0{,}36-0{,}64=-1$: Sie spiegelt an der Geraden in Richtung $(2,\,1)^{\top}$, denn sie bildet $(2,\,1)^{\top}$ auf sich selbst ab und $(-1,\,2)^{\top}$ auf $(1,\,-2)^{\top}$.

⁠**Kurz gesagt:** Orthogonale Matrizen erhalten Skalarprodukte, Längen und Winkel; sie drehen oder spiegeln, und ihre Determinante ist $\pm1$.

:::hintergrund Warum man in der Numerik gern mit orthogonalen Matrizen rechnet
Ein Rechner rechnet mit gerundeten Zahlen, jedes Zwischenergebnis trägt einen kleinen Fehler $\boldsymbol{\delta}$. Multipliziert man ein solches Zwischenergebnis mit einer Matrix, wird auch der Fehler mit ihr multipliziert. Eine beliebige Matrix kann ihn dabei vergrößern; eine orthogonale nicht, denn nach [(1.3)](#gl-1-3) ist $\lVert\mathbf{Q}\boldsymbol{\delta}\rVert=\lVert\boldsymbol{\delta}\rVert$. Rechenwege, die nur aus Multiplikationen mit orthogonalen Matrizen bestehen, lassen die Rundungsfehler deshalb nicht anwachsen. Aus demselben Grund ist die Inverse kein Problem: Man muss sie nicht ausrechnen, die Transponierte genügt, und sie ist exakt.
:::

### Matrizen mit orthonormalen Spalten

<span class="anker" id="stufe-1-6"></span>

Oft hat man weniger orthonormale Vektoren, als der Raum Dimensionen hat. Eine Ebene im $\mathbb{R}^3$ hat eine Orthonormalbasis aus zwei Vektoren. Schreibt man sie als Spalten in eine Matrix, ist diese nicht quadratisch, sondern hat drei Zeilen und zwei Spalten. Ein Teil der Rechenregeln überträgt sich, ein Teil nicht, und der Unterschied ist wichtig.

:::satz Satz 1.8 (Rechteckige Matrizen mit orthonormalen Spalten)
<span class="anker" id="satz-1-8"></span>

Hat $\mathbf{Q}\in\mathbb{R}^{n\times k}$ orthonormale Spalten und ist $k<n$, so gilt $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_k$ und $\lVert\mathbf{Q}\mathbf{c}\rVert=\lVert\mathbf{c}\rVert$ für jedes $\mathbf{c}\in\mathbb{R}^k$. Die Matrix $\mathbf{Q}\mathbf{Q}^{\top}\in\mathbb{R}^{n\times n}$ ist dagegen nicht die Einheitsmatrix.
:::

:::beweis Rechteckige Matrizen
Die ersten beiden Aussagen folgen genau wie bei quadratischen Matrizen aus [(1.1)](#gl-1-1). Für die dritte: Die Matrix $\mathbf{Q}^{\top}$ hat $k$ Zeilen und $n$ Spalten. Nach dem Rangsatz aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.5, hat ihr Kern die Dimension $n-\operatorname{rang}\mathbf{Q}^{\top}\ge n-k\ge1$. Es gibt also einen Vektor $\mathbf{z}\ne\mathbf{0}$ mit $\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}$, und für ihn ist $\mathbf{Q}\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}\ne\mathbf{z}$. Also ist $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.
:::

⁠**Rechenbeispiel 1:** Die Matrix mit der einen Spalte $\mathbf{q}=(0{,}6;\ 0{,}8)^{\top}$ erfüllt $\mathbf{q}^{\top}\mathbf{q}=1$, aber

$$\mathbf{q}\mathbf{q}^{\top}=\begin{pmatrix}0{,}36&0{,}48\\0{,}48&0{,}64\end{pmatrix}\ne\mathbf{I} .$$

Sie bildet $(-0{,}8;\ 0{,}6)^{\top}$ auf $\mathbf{0}$ ab. Den Vektor $\mathbf{x}=(3,\,1)^{\top}$ bildet sie auf $(1{,}08+0{,}48;\ 1{,}44+0{,}64)^{\top}=(1{,}56;\ 2{,}08)^{\top}$ ab. Das ist genau der Endpunkt des Schattens von $\mathbf{x}$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 5.5, denn $\mathbf{q}\mathbf{q}^{\top}\mathbf{x}=\mathbf{q}\,(\mathbf{q}^{\top}\mathbf{x})=2{,}6\,\mathbf{q}$.

⁠**Rechenbeispiel 2:** Die Spalten von $\mathbf{Q}=\Bigl(\begin{smallmatrix}1&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ sind $\mathbf{e}_1$ und $\mathbf{e}_2$ im $\mathbb{R}^3$. Es ist $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_2$, aber $\mathbf{Q}\mathbf{Q}^{\top}=\operatorname{diag}(1;\,1;\,0)$. Diese Matrix behält die ersten beiden Komponenten und setzt die dritte auf null.

⁠**Kurz gesagt:** Bei einer rechteckigen Matrix mit orthonormalen Spalten ist $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, aber $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$: Das Produkt in dieser Reihenfolge wirft einen Teil des Vektors weg.

:::aufgabe Aufgabe 1 ★ Orthonormal und Koordinaten
<span class="anker" id="aufg-1"></span>

Gegeben sind $\mathbf{q}_1=\tfrac13(1,\,2,\,2)^{\top}$, $\mathbf{q}_2=\tfrac13(2,\,1,\,-2)^{\top}$ und $\mathbf{q}_3=\tfrac13(2,\,-2,\,1)^{\top}$.

<ol class="al">

<li>

Prüfe, dass die drei Vektoren orthonormal sind.

</li>

<li>

Berechne die Koordinaten von $\mathbf{x}=(3,\,0,\,3)^{\top}$ in dieser Orthonormalbasis und mache die Probe. Prüfe die Formel für $\lVert\mathbf{x}\rVert^2$.

</li>

</ol>

:::loesung
(a) Man bildet alle sechs Skalarprodukte; der gemeinsame Faktor $\tfrac13\cdot\tfrac13=\tfrac19$ steht vorn:

$$\mathbf{q}_1^{\top}\mathbf{q}_1=\tfrac19(1+4+4)=1,\quad \mathbf{q}_2^{\top}\mathbf{q}_2=\tfrac19(4+1+4)=1,\quad \mathbf{q}_3^{\top}\mathbf{q}_3=\tfrac19(4+4+1)=1,$$

$$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac19(2+2-4)=0,\quad \mathbf{q}_1^{\top}\mathbf{q}_3=\tfrac19(2-4+2)=0,\quad \mathbf{q}_2^{\top}\mathbf{q}_3=\tfrac19(4-2-2)=0 .$$

Alle drei haben die Länge $1$ und stehen paarweise senkrecht: Sie sind orthonormal, nach Abschnitt [1.2](#stufe-1-2) also eine Orthonormalbasis des $\mathbb{R}^3$.

(b) Nach [(1.2)](#gl-1-2) sind die Koordinaten Skalarprodukte, ohne Gleichungssystem:

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=\tfrac13(3+0+6)=3,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=\tfrac13(6+0-6)=0,\qquad c_3=\mathbf{q}_3^{\top}\mathbf{x}=\tfrac13(6+0+3)=3 .$$

Probe: $3\mathbf{q}_1+0\cdot\mathbf{q}_2+3\mathbf{q}_3=(1,\,2,\,2)^{\top}+(2,\,-2,\,1)^{\top}=(3,\,0,\,3)^{\top}=\mathbf{x}$. Längenformel: $c_1^2+c_2^2+c_3^2=9+0+9=18$ und $\lVert\mathbf{x}\rVert^2=9+0+9=18$.
:::
:::

:::aufgabe Aufgabe 2 ★ Eine orthogonale Matrix
<span class="anker" id="aufg-2"></span>

Es sei $\mathbf{Q}$ die Matrix mit den Spalten $\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3$ aus Aufgabe [1](#aufg-1).

<ol class="al">

<li>

Gib $\mathbf{Q}^{-1}$ an, ohne zu rechnen. Prüfe $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ an einem Eintrag deiner Wahl außerhalb der Diagonale.

</li>

<li>

Berechne $\mathbf{Q}\,(1,\,1,\,1)^{\top}$ und vergleiche die Längen. Berechne $\det\mathbf{Q}$. Dreht oder spiegelt $\mathbf{Q}$?

</li>

</ol>

:::loesung
(a) Die Spalten sind orthonormal, also ist $\mathbf{Q}$ orthogonal und $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, ohne Rechnung. Hier ist

$$\mathbf{Q}=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}$$

sogar symmetrisch, also $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}=\mathbf{Q}$. Der Eintrag $(1,2)$ von $\mathbf{Q}\mathbf{Q}^{\top}$ ist das Skalarprodukt der ersten mit der zweiten Zeile: $\tfrac19(1\cdot2+2\cdot1+2\cdot(-2))=0$.

(b) $\mathbf{Q}\,(1,\,1,\,1)^{\top}=\tfrac13(5,\,1,\,1)^{\top}$ mit dem Längenquadrat $\tfrac19(25+1+1)=3$, genau das Längenquadrat von $(1,\,1,\,1)^{\top}$, wie [(1.3)](#gl-1-3) verlangt. Die Determinante ist

$$\det\mathbf{Q}=\tfrac1{27}\bigl(1\cdot(1-4)-2\cdot(2+4)+2\cdot(-4-2)\bigr)=\tfrac1{27}(-3-12-12)=-1 .$$

Also spiegelt $\mathbf{Q}$. Genauer: Wegen $\mathbf{Q}=\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$ ist $\mathbf{Q}^2=\mathbf{I}$, zweimal angewandt kommt alles zurück. Der Vektor $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ wird umgeklappt, $\mathbf{Q}\mathbf{k}=\tfrac13(1-2-2,\ 2-1+2,\ 2+2-1)^{\top}=(-1,\,1,\,1)^{\top}=-\mathbf{k}$, und die Vektoren senkrecht zu $\mathbf{k}$ bleiben fest. $\mathbf{Q}$ ist die Spiegelung an der Ebene $x_1-x_2-x_3=0$.
:::
:::

:::aufgabe Aufgabe 3 ★★ Rechnen mit orthogonalen Matrizen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Zeige: Sind $\mathbf{Q}_1$ und $\mathbf{Q}_2$ orthogonal, so ist auch $\mathbf{Q}_1\mathbf{Q}_2$ orthogonal.

</li>

<li>

Ist die Summe zweier orthogonaler Matrizen wieder orthogonal? Begründe oder gib ein Gegenbeispiel an.

</li>

<li>

Zeige, dass eine Diagonalmatrix genau dann orthogonal ist, wenn jeder Diagonaleintrag $1$ oder $-1$ ist. Was tut eine solche Matrix geometrisch?

</li>

</ol>

:::loesung
(a) Mit $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ ist $(\mathbf{Q}_1\mathbf{Q}_2)^{\top}(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^{\top}\mathbf{Q}_1^{\top}\mathbf{Q}_1\mathbf{Q}_2=\mathbf{Q}_2^{\top}\mathbf{I}\mathbf{Q}_2=\mathbf{I}$. Anschaulich: Zwei starre Bewegungen hintereinander sind wieder eine starre Bewegung.

(b) Nein. Gegenbeispiel: $\mathbf{I}+\mathbf{I}=2\mathbf{I}$, und $(2\mathbf{I})^{\top}(2\mathbf{I})=4\mathbf{I}\ne\mathbf{I}$; die Summe verdoppelt alle Längen. Ebenso ist $\mathbf{I}+(-\mathbf{I})$ die Nullmatrix.

(c) Für $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$ ist $\mathbf{D}^{\top}\mathbf{D}=\operatorname{diag}(d_1^2,\dots,d_n^2)$. Das ist genau dann $\mathbf{I}$, wenn jedes $d_i^2=1$ ist, also $d_i=1$ oder $d_i=-1$. Eine solche Matrix kehrt die Achsen mit $d_i=-1$ um und lässt die anderen stehen: Sie spiegelt an den Koordinatenebenen. Zum Beispiel spiegelt $\operatorname{diag}(1;\,-1)$ an der $x_1$-Achse, und $\operatorname{diag}(-1;\,-1)$ ist die Drehung um $180^\circ$.
:::
:::
