---
title: Zufallsvektoren und die Kovarianzmatrix
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15241200
summary: Ein Datenpunkt hat meist viele Merkmale.
tags: Zufallsvektor, Erwartungswertvektor, Kovarianzmatrix, empirische Kovarianzmatrix
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Ein Datenpunkt hat meist viele Merkmale. Dieser Abschnitt fasst sie zu einem Zufallsvektor zusammen und ordnet alle Varianzen und Kovarianzen in einer Matrix an. Mit der Matrixrechnung aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) und [Grundlagen 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) wird dann vieles einfach: wie sich die Kovarianzmatrix unter linearen Abbildungen ändert, wie stark die Daten in einer beliebigen Richtung streuen und warum jede Kovarianzmatrix positiv semidefinit ist. Ihre Eigenvektoren zeigen die Richtungen größter und kleinster Streuung.
:::

### Zufallsvektoren

<span class="anker" id="stufe-11-1"></span>

Mehrere Zufallsvariablen, die zum selben Experiment gehören, schreibt man als Vektor. So kann man mit ihnen rechnen wie mit den Datenpunkten aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html).

:::definition Definition 11.1 (Zufallsvektor, Erwartungswertvektor)
<span class="anker" id="satz-11-1"></span>

Ein __Zufallsvektor__ $\mathbf{x}=(x_1,\dots,x_d)^{\top}$ besteht aus $d$ Zufallsvariablen $x_1,\dots,x_d$ auf demselben Ergebnisraum. Sein __Erwartungswertvektor__ ist $\boldsymbol{\mu}=\mathbb{E}[\mathbf{x}]=(\mathbb{E}[x_1],\dots,\mathbb{E}[x_d])^{\top}$.
:::

Bei Vektoren schreibt dieses Kapitel wie im maschinellen Lernen üblich auch den Zufallsvektor und seine Komponenten klein; der große fette Buchstabe $\mathbf{X}$ bleibt die Datenmatrix aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html). Ob $\mathbf{x}$ der Zufallsvektor oder ein fester Wert ist, sagt der Zusammenhang: In $\mathbb{E}[\mathbf{x}]$ ist er zufällig, in einer Dichte $p(\mathbf{x})$ ist $\mathbf{x}$ die Stelle, an der man sie auswertet. Ein Datenpunkt $\mathbf{x}_i$ ist ein Wert. Erwartungswerte von Matrizen aus Zufallsvariablen bildet man ebenso komponentenweise. Aus der Linearität folgt für eine feste Matrix $\mathbf{A}$ und einen festen Vektor $\mathbf{b}$

<span class="anker" id="gl-11-1"></span>
$$\mathbb{E}[\mathbf{A}\mathbf{x}+\mathbf{b}]=\mathbf{A}\boldsymbol{\mu}+\mathbf{b} , \tag{11.1}$$

denn jede Komponente von $\mathbf{A}\mathbf{x}+\mathbf{b}$ ist eine Linearkombination der $x_j$ plus eine Zahl.

::::beispiel [Rechenbeispiel]
Fasst man Sonne und Rad aus Abschnitt [9](mehrere-zufallsvariablen.html#stufe-9) zu $\mathbf{x}=(S,R)^{\top}$ zusammen, so ist $\boldsymbol{\mu}=(0{,}4;\ 0{,}4)^{\top}$. Die Summe $S+R$, die Anzahl der „guten Dinge“ eines Tages, ist $\mathbf{1}^{\top}\mathbf{x}$ mit dem Einsvektor und hat den Erwartungswert $\mathbf{1}^{\top}\boldsymbol{\mu}=0{,}8$.
::::

⁠**Kurz gesagt:** Ein Zufallsvektor fasst mehrere Zufallsvariablen zusammen; sein Erwartungswert wird komponentenweise gebildet und vertauscht mit $\mathbf{A}\mathbf{x}+\mathbf{b}$.

### Die Kovarianzmatrix

<span class="anker" id="stufe-11-2"></span>

Bei $d$ Komponenten gibt es $d$ Varianzen und für jedes Paar eine Kovarianz. Man ordnet sie in einer $d\times d$-Matrix an: Der Eintrag in Zeile $j$ und Spalte $l$ ist die Kovarianz der Komponenten $j$ und $l$.

:::definition Definition 11.2 (Kovarianzmatrix)
<span class="anker" id="satz-11-2"></span>

Die __Kovarianzmatrix__ eines Zufallsvektors $\mathbf{x}$ mit dem Erwartungswertvektor $\boldsymbol{\mu}$ ist

<span class="anker" id="gl-11-2"></span>
$$\boldsymbol{\Sigma}=\mathbb{E}\bigl[(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}\bigr],\qquad \Sigma_{jl}=\operatorname{Cov}(x_j,x_l). \tag{11.2}$$
:::

$(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}$ ist das äußere Produkt aus [Grundlagen 1, Abschnitt 9.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5): eine Matrix mit den Einträgen $(x_j-\mu_j)(x_l-\mu_l)$. Ihr Erwartungswert, komponentenweise gebildet, hat nach [(10.1)](kovarianz-und-korrelation.html#gl-10-1) die Einträge $\operatorname{Cov}(x_j,x_l)$. Auf der Diagonalen stehen die Varianzen $\Sigma_{jj}=\operatorname{Var}(x_j)$. Weil die Kovarianz symmetrisch ist, ist $\boldsymbol{\Sigma}$ symmetrisch. Wie bei einer Zahl gibt es die Verschiebungsformel $\boldsymbol{\Sigma}=\mathbb{E}[\mathbf{x}\mathbf{x}^{\top}]-\boldsymbol{\mu}\boldsymbol{\mu}^{\top}$. Sind die Komponenten paarweise unkorreliert, so ist $\boldsymbol{\Sigma}$ eine Diagonalmatrix.

::::beispiel [Rechenbeispiel]
Für $\mathbf{x}=(S,R)^{\top}$ ist $\operatorname{Var}(S)=\operatorname{Var}(R)=0{,}24$ und $\operatorname{Cov}(S,R)=0{,}14$, also

$$\boldsymbol{\Sigma}=\begin{pmatrix}0{,}24&0{,}14\\0{,}14&0{,}24\end{pmatrix}.$$
::::

⁠**Kurz gesagt:** Die Kovarianzmatrix enthält auf der Diagonalen die Varianzen und daneben die Kovarianzen aller Paare; sie ist der Erwartungswert des äußeren Produkts der Abweichung mit sich selbst und symmetrisch.

### Die Kovarianzmatrix eines Datensatzes

<span class="anker" id="stufe-11-3"></span>

Für einen Datensatz mit der Datenmatrix $\mathbf{X}\in\mathbb{R}^{N\times d}$ aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) nimmt man wieder die empirische Verteilung. Ihre Kovarianzmatrix enthält alle empirischen Kovarianzen der Merkmale und lässt sich mit einem einzigen Matrixprodukt ausrechnen.

:::definition Definition 11.3 (Empirische Kovarianzmatrix)
<span class="anker" id="satz-11-3"></span>

Für die Datenmatrix $\mathbf{X}$ mit dem Mittelwertvektor $\bar{\mathbf{x}}=\tfrac1N\mathbf{X}^{\top}\mathbf{1}$ und der zentrierten Datenmatrix $\tilde{\mathbf{X}}=\mathbf{X}-\mathbf{1}\bar{\mathbf{x}}^{\top}$ heißt

<span class="anker" id="gl-11-3"></span>
$$\mathbf{S}=\frac1N\,\tilde{\mathbf{X}}^{\top}\tilde{\mathbf{X}}=\frac1N\sum_{i=1}^N(\mathbf{x}_i-\bar{\mathbf{x}})(\mathbf{x}_i-\bar{\mathbf{x}})^{\top} \tag{11.3}$$

die __empirische Kovarianzmatrix__.
:::

Der Eintrag $(j,l)$ von $\tilde{\mathbf{X}}^{\top}\tilde{\mathbf{X}}$ ist das Skalarprodukt der zentrierten Merkmalsspalten $j$ und $l$; das ist die Gram-Matrix der Merkmale aus [Grundlagen 1, Abschnitt 10.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-4), für die zentrierten Daten. Geteilt durch $N$ ergibt das die empirischen Kovarianzen [(10.7)](kovarianz-und-korrelation.html#gl-10-7). Auf der Diagonalen stehen die Quadrate $s_j^2$ der Standardabweichungen der Merkmale. Die Summenform schreibt dasselbe Produkt als Summe äußerer Produkte, einer je Datenpunkt.

::::beispiel [Rechenbeispiel]
Die drei Punkte $(1,2)$, $(2,1)$, $(3,3)$ aus Unterabschnitt [10.6](kovarianz-und-korrelation.html#stufe-10-6) bilden die Zeilen von $\mathbf{X}$. Mit $\bar{\mathbf{x}}=(2,\,2)^{\top}$ ist $\tilde{\mathbf{X}}$ die Matrix mit den Zeilen $(-1,\,0)$, $(0,\,-1)$ und $(1,\,1)$, und

$$\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}=\begin{pmatrix}\tfrac23&\tfrac13\\\tfrac13&\tfrac23\end{pmatrix}$$

(Abb. [15](#abb-15)), in Übereinstimmung mit Unterabschnitt [10.6](kovarianz-und-korrelation.html#stufe-10-6).

:::abbildung ml/k4rkovmatrix 15
Die empirische Kovarianzmatrix der drei Punkte: Jeder Eintrag ist ein Skalarprodukt zweier zentrierter Merkmalsspalten, geteilt durch $N=3$. Wegen der Symmetrie ist $S_{21}=S_{12}$.
:::
::::

⁠**Kurz gesagt:** Die empirische Kovarianzmatrix ist $\tfrac1N\tilde{\mathbf{X}}^{\top}\tilde{\mathbf{X}}$, die Gram-Matrix der zentrierten Merkmale geteilt durch $N$.

### Lineare Abbildungen von Zufallsvektoren

<span class="anker" id="stufe-11-4"></span>

Aus Merkmalen bildet man oft neue: Summen, Differenzen, gewichtete Summen, gedrehte Koordinaten. Ist $\mathbf{y}=\mathbf{A}\mathbf{x}+\mathbf{b}$, so folgt der Erwartungswert aus [(11.1)](#gl-11-1). Auch die Kovarianzmatrix von $\mathbf{y}$ lässt sich direkt aus $\boldsymbol{\Sigma}$ ausrechnen, ohne die Verteilung von $\mathbf{x}$ im Einzelnen zu kennen.

:::satz Satz 11.4 (Kovarianzmatrix unter affinen Abbildungen)
<span class="anker" id="satz-11-4"></span>

Ist $\mathbf{x}$ ein Zufallsvektor mit der Kovarianzmatrix $\boldsymbol{\Sigma}$ und $\mathbf{y}=\mathbf{A}\mathbf{x}+\mathbf{b}$ mit einer festen Matrix $\mathbf{A}\in\mathbb{R}^{m\times d}$ und einem festen Vektor $\mathbf{b}\in\mathbb{R}^m$, so ist

<span class="anker" id="gl-11-4"></span>
$$\operatorname{Cov}(\mathbf{y})=\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top} . \tag{11.4}$$
:::

:::beweis Kovarianz unter affinen Abbildungen
Die Abweichung von $\mathbf{y}$ von seinem Erwartungswert ist $\mathbf{y}-(\mathbf{A}\boldsymbol{\mu}+\mathbf{b})=\mathbf{A}(\mathbf{x}-\boldsymbol{\mu})$; die Verschiebung $\mathbf{b}$ fällt heraus. Also ist

$$\operatorname{Cov}(\mathbf{y})=\mathbb{E}\bigl[\mathbf{A}(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}\mathbf{A}^{\top}\bigr]=\mathbf{A}\,\mathbb{E}\bigl[(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}\bigr]\,\mathbf{A}^{\top}=\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top} ,$$

wobei man $\mathbf{A}$ und $\mathbf{A}^{\top}$ aus dem Erwartungswert herausziehen darf, weil jeder Eintrag des Produkts eine Linearkombination der Einträge der mittleren Matrix mit festen Faktoren ist.
:::

Für $m=1$ ist $\mathbf{A}$ eine Zeile $\mathbf{u}^{\top}$, und $\mathbf{u}^{\top}\mathbf{x}$ ist eine einzige Zufallsvariable mit der Varianz $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$. Für $\mathbf{u}=\mathbf{1}$ ist das die Summe aller Komponenten, und $\mathbf{1}^{\top}\boldsymbol{\Sigma}\mathbf{1}$ ist die Summe aller Einträge von $\boldsymbol{\Sigma}$: alle Varianzen und jede Kovarianz zweimal, wie in [(10.3)](kovarianz-und-korrelation.html#gl-10-3).

::::beispiel [Rechenbeispiel]
Für die drei Punkte mit $\mathbf{S}=\tfrac13\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ bilde man Summe und Differenz der Merkmale, $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$. Dann ist

$$\mathbf{A}\mathbf{S}\mathbf{A}^{\top}=\frac13\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\frac13\begin{pmatrix}3&3\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\frac13\begin{pmatrix}6&0\\0&2\end{pmatrix}.$$

Die Summe hat die Varianz $2$, die Differenz $\tfrac23$, und die beiden sind unkorreliert, obwohl die ursprünglichen Merkmale es nicht waren. Zur Probe: Die Summen der drei Punkte sind $3,3,6$ mit dem Mittelwert $4$ und der Varianz $\tfrac13(1+1+4)=2$.
::::

⁠**Kurz gesagt:** Unter $\mathbf{y}=\mathbf{A}\mathbf{x}+\mathbf{b}$ wird die Kovarianzmatrix zu $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}$; eine einzelne Linearkombination $\mathbf{u}^{\top}\mathbf{x}$ hat die Varianz $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$.

### Die Streuung in einer Richtung

<span class="anker" id="stufe-11-5"></span>

Wie stark streuen Datenpunkte, wenn man nur in eine Richtung blickt? Nach [Grundlagen 1, Abschnitt 5.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), ist das Skalarprodukt $\mathbf{u}^{\top}\mathbf{x}$ mit einem Einheitsvektor $\mathbf{u}$ die Länge des Schattens von $\mathbf{x}$ auf die Gerade in Richtung $\mathbf{u}$. Die Streuung der Daten in Richtung $\mathbf{u}$ ist die Varianz dieser Schattenlängen.

:::satz Satz 11.5 (Varianz in einer Richtung)
<span class="anker" id="satz-11-5"></span>

Für einen Einheitsvektor $\mathbf{u}$ hat die Projektion $\mathbf{u}^{\top}\mathbf{x}$ eines Zufallsvektors mit der Kovarianzmatrix $\boldsymbol{\Sigma}$ die Varianz

<span class="anker" id="gl-11-5"></span>
$$\operatorname{Var}(\mathbf{u}^{\top}\mathbf{x})=\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u} . \tag{11.5}$$

Für einen Datensatz gilt dasselbe mit $\mathbf{S}$: Die Schattenlängen $\mathbf{u}^{\top}\mathbf{x}_i$ der Datenpunkte haben die empirische Varianz $\mathbf{u}^{\top}\mathbf{S}\mathbf{u}$.
:::

Das ist der Fall $m=1$ von [(11.4)](#gl-11-4). $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$ ist eine quadratische Form aus [Grundlagen 2, Abschnitt 5.1](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1). Für $\mathbf{u}=\mathbf{e}_j$ ergibt sie das Diagonalelement $\Sigma_{jj}$, die Varianz der $j$-ten Komponente. Die Kovarianzmatrix enthält also nicht nur die Streuung in den Richtungen der Koordinatenachsen, sondern in jeder Richtung.

::::beispiel [Rechenbeispiel]
Für die drei Punkte mit $\mathbf{S}=\tfrac13\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ und $\mathbf{u}=\tfrac1{\sqrt2}(1,\,1)^{\top}$ ist $\mathbf{u}^{\top}\mathbf{S}\mathbf{u}=1$ (Abb. [16](#abb-16)). Direkt: Die zentrierten Punkte $(-1,0)$, $(0,-1)$, $(1,1)$ haben die Schattenlängen $-\tfrac1{\sqrt2}$, $-\tfrac1{\sqrt2}$, $\tfrac2{\sqrt2}$ mit den Quadraten $\tfrac12$, $\tfrac12$, $2$ und dem Mittelwert $1$. In Richtung $\tfrac1{\sqrt2}(1,\,-1)^{\top}$ ist die Varianz nur $\tfrac13\cdot\tfrac12\,(2-1-1+2)=\tfrac13$, in Richtung der Achsen $\tfrac23$.

:::abbildung ml/k4rrichtung 16
Die Varianz der drei Punkte in Richtung $\mathbf{u}=(1,1)^{\top}/\sqrt2$ als quadratische Form: Jeder Eintrag von $\mathbf{S}$ wird mit den beiden zugehörigen Komponenten von $\mathbf{u}$ gewichtet.
:::
::::

⁠**Kurz gesagt:** Die Varianz der Projektion auf eine Richtung $\mathbf{u}$ ist die quadratische Form $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$; die Kovarianzmatrix kennt die Streuung in jeder Richtung.

### Kovarianzmatrizen sind positiv semidefinit

<span class="anker" id="stufe-11-6"></span>

Eine Varianz ist nie negativ. Weil $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$ für jeden Vektor $\mathbf{u}$ eine Varianz ist, erfüllt $\boldsymbol{\Sigma}$ die Bedingung aus [Grundlagen 2, Abschnitt 8.1](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-1), mit der positiv semidefinite Matrizen definiert sind. Daraus folgt alles, was [Grundlagen 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) über solche Matrizen weiß.

:::satz Satz 11.6 (Eigenschaften der Kovarianzmatrix)
<span class="anker" id="satz-11-6"></span>

Jede Kovarianzmatrix $\boldsymbol{\Sigma}$ und jede empirische Kovarianzmatrix $\mathbf{S}$ ist symmetrisch und positiv semidefinit. Ihre Eigenwerte $\lambda_1\ge\dots\ge\lambda_d$ sind nichtnegativ. Der Eigenwert $\lambda_i$ ist die Varianz in Richtung des zugehörigen normierten Eigenvektors $\mathbf{q}_i$, und die größte Varianz in irgendeiner Richtung ist $\lambda_1$, angenommen in Richtung $\mathbf{q}_1$; die kleinste ist $\lambda_d$. $\boldsymbol{\Sigma}$ ist genau dann singulär, wenn eine Linearkombination $\mathbf{u}^{\top}\mathbf{x}$ mit $\mathbf{u}\ne\mathbf{0}$ die Varianz $0$ hat, also mit Wahrscheinlichkeit $1$ konstant ist.
:::

:::beweis Eigenschaften der Kovarianzmatrix
Für jedes $\mathbf{u}$ ist $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}=\operatorname{Var}(\mathbf{u}^{\top}\mathbf{x})\ge0$, auch für Vektoren, die keine Einheitsvektoren sind, denn [(11.4)](#gl-11-4) gilt für jede Zeile. Das ist die Definition von positiv semidefinit; nach dem Eigenwerttest in [Grundlagen 2, Abschnitt 8.2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-2), sind die Eigenwerte nichtnegativ. Für einen normierten Eigenvektor ist $\mathbf{q}_i^{\top}\boldsymbol{\Sigma}\mathbf{q}_i=\lambda_i\mathbf{q}_i^{\top}\mathbf{q}_i=\lambda_i$. Die größte und die kleinste Varianz in einer Richtung sind nach [Grundlagen 2, Abschnitt 8.5](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5), der größte und der kleinste Eigenwert. Ist schließlich $\boldsymbol{\Sigma}\mathbf{u}=\mathbf{0}$ für ein $\mathbf{u}\ne\mathbf{0}$, so ist $\operatorname{Var}(\mathbf{u}^{\top}\mathbf{x})=\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}=0$; ist umgekehrt $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}=0$, so ist $\mathbf{u}$ nach dem Spektralsatz eine Kombination von Eigenvektoren zum Eigenwert $0$ und $\boldsymbol{\Sigma}\mathbf{u}=\mathbf{0}$.
:::

Für Daten heißt der letzte Teil: $\mathbf{S}$ ist singulär, wenn die Datenpunkte alle in einer Ebene oder auf einer Geraden liegen, die nicht den ganzen Raum ausfüllt. Dann gibt es eine Richtung, in der sie gar nicht streuen, wie bei den abhängigen Merkmalen aus [Grundlagen 1, Abschnitt 13.6](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6).

::::beispiel [Rechenbeispiel]
$\mathbf{S}=\tfrac13\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ hat die Eigenwerte $1$ und $\tfrac13$ mit den Eigenvektoren $\tfrac1{\sqrt2}(1,\,1)^{\top}$ und $\tfrac1{\sqrt2}(1,\,-1)^{\top}$. Das sind genau die Richtungen und Varianzen aus Unterabschnitt [11.5](#stufe-11-5): In keiner Richtung streuen die drei Punkte stärker als in Richtung $(1,1)^{\top}$, in keiner schwächer als in Richtung $(1,-1)^{\top}$. Die Punkte $(1,2)$, $(2,4)$, $(3,6)$ liegen dagegen auf einer Geraden durch den Nullpunkt. Für sie ist $\mathbf{S}=\tfrac13\bigl(\begin{smallmatrix}2&4\\4&8\end{smallmatrix}\bigr)$ mit der Determinante $0$, und in Richtung $\tfrac1{\sqrt5}(2,\,-1)^{\top}$ ist die Varianz $0$, weil $2x_1-x_2=0$ für jeden Punkt gilt.
::::

⁠**Kurz gesagt:** Jede Kovarianzmatrix ist positiv semidefinit, weil $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$ eine Varianz ist; ihre Eigenvektoren sind die Richtungen extremer Streuung, ihre Eigenwerte die Varianzen in diesen Richtungen.

:::hintergrund Jede positiv semidefinite Matrix ist eine Kovarianzmatrix
Der Satz hat eine Umkehrung. Ist $\boldsymbol{\Sigma}$ symmetrisch und positiv definit, so gibt es nach [Grundlagen 2, Abschnitt 8.6](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-6), die Cholesky-Zerlegung $\boldsymbol{\Sigma}=\mathbf{L}\mathbf{L}^{\top}$. Nimmt man einen Zufallsvektor $\mathbf{z}$ mit unkorrelierten Komponenten der Varianz $1$, also $\operatorname{Cov}(\mathbf{z})=\mathbf{I}$, so hat $\mathbf{x}=\mathbf{L}\mathbf{z}$ nach [(11.4)](#gl-11-4) die Kovarianzmatrix $\mathbf{L}\mathbf{I}\mathbf{L}^{\top}=\boldsymbol{\Sigma}$. Für positiv semidefinite Matrizen nimmt man statt $\mathbf{L}$ etwa $\mathbf{Q}\boldsymbol{\Lambda}^{1/2}$ aus dem Spektralsatz, mit den Wurzeln der Eigenwerte auf der Diagonalen. Eine symmetrische Matrix ist also genau dann eine mögliche Kovarianzmatrix, wenn sie positiv semidefinit ist. Eine Matrix wie $\bigl(\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\bigr)$ mit dem Eigenwert $-1$ kann keine sein: In Richtung des Eigenvektors $(1,-1)^{\top}/\sqrt2$ hätte sie die Varianz $-1$. Das ist auch ein Prüfstein für eigene Rechnungen: Hat eine von Hand angenommene oder aus Teilen zusammengesetzte Kovarianzmatrix einen negativen Eigenwert, steckt ein Fehler darin.
:::

:::aufgabe Aufgabe 33 ★ Vier Punkte
<span class="anker" id="aufg-33"></span>

Gegeben sind die Datenpunkte $(0,0)$, $(1,2)$, $(2,1)$ und $(3,3)$.

<ol class="al">

<li>

Berechne den Mittelwertvektor, die zentrierte Datenmatrix und die empirische Kovarianzmatrix $\mathbf{S}$.

</li>

<li>

Berechne den empirischen Korrelationskoeffizienten der beiden Merkmale.

</li>

<li>

Bestimme die Eigenwerte und Eigenvektoren von $\mathbf{S}$. In welcher Richtung streuen die Punkte am stärksten?

</li>

</ol>

:::loesung
(a) $\bar{\mathbf{x}}=(1{,}5;\ 1{,}5)^{\top}$; $\tilde{\mathbf{X}}$ hat die Zeilen $(-1{,}5;\ -1{,}5)$, $(-0{,}5;\ 0{,}5)$, $(0{,}5;\ -0{,}5)$, $(1{,}5;\ 1{,}5)$. Damit ist $S_{11}=S_{22}=\tfrac14\,(2{,}25+0{,}25+0{,}25+2{,}25)=1{,}25$ und $S_{12}=\tfrac14\,(2{,}25-0{,}25-0{,}25+2{,}25)=1$, also $\mathbf{S}=\bigl(\begin{smallmatrix}1{,}25&1\\1&1{,}25\end{smallmatrix}\bigr)$.

(b) $\operatorname{corr}=1/\sqrt{1{,}25\cdot1{,}25}=0{,}8$.

(c) Spur $2{,}5$, Determinante $1{,}5625-1=0{,}5625$, also $\lambda^2-2{,}5\lambda+0{,}5625=0$ mit $\lambda_1=2{,}25$ und $\lambda_2=0{,}25$. Die Eigenvektoren sind $\tfrac1{\sqrt2}(1,\,1)^{\top}$ und $\tfrac1{\sqrt2}(1,\,-1)^{\top}$. Am stärksten streuen die Punkte entlang der Diagonalen, mit der Varianz $2{,}25$.
:::
:::

:::aufgabe Aufgabe 34 ★★ Varianzen von Kombinationen
<span class="anker" id="aufg-34"></span>

Ein Zufallsvektor habe die Kovarianzmatrix $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}4&2\\2&3\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Berechne die Varianzen von $x_1+x_2$, $x_1-x_2$ und $\tfrac1{\sqrt2}(x_1+x_2)$.

</li>

<li>

Berechne die Eigenwerte von $\boldsymbol{\Sigma}$. Zeige, dass die Varianz aus (a) in Richtung $\tfrac1{\sqrt2}(1,\,1)^{\top}$ zwischen ihnen liegt.

</li>

<li>

Berechne die Kovarianzmatrix von $(x_1+x_2,\ x_1-x_2)^{\top}$. Sind die beiden unkorreliert?

</li>

</ol>

:::loesung
(a) $\operatorname{Var}(x_1+x_2)=\mathbf{1}^{\top}\boldsymbol{\Sigma}\mathbf{1}=4+2+2+3=11$, $\operatorname{Var}(x_1-x_2)=4-2-2+3=3$ und $\operatorname{Var}\bigl(\tfrac1{\sqrt2}(x_1+x_2)\bigr)=\tfrac{11}2=5{,}5$.

(b) Spur $7$, Determinante $8$: $\lambda=\tfrac{7\pm\sqrt{17}}2\approx5{,}562$ und $1{,}438$. Die Varianz $5{,}5$ in Richtung $\tfrac1{\sqrt2}(1,1)^{\top}$ liegt dazwischen, knapp unter dem größten Eigenwert, weil diese Richtung fast die erste Hauptachse ist.

(c) Mit $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$ ist $\mathbf{A}\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}6&5\\2&-1\end{smallmatrix}\bigr)$ und $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}11&1\\1&3\end{smallmatrix}\bigr)$. Die Kovarianz ist $1=\operatorname{Var}(x_1)-\operatorname{Var}(x_2)$: Summe und Differenz sind hier korreliert, weil die beiden Komponenten verschiedene Varianzen haben.
:::
:::

:::aufgabe Aufgabe 35 ★★ Welche Matrix kann eine Kovarianzmatrix sein?
<span class="anker" id="aufg-35"></span>

Entscheide für jede Matrix, ob sie die Kovarianzmatrix eines Zufallsvektors sein kann, und begründe.

$$\mathbf{A}_1=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad \mathbf{A}_2=\begin{pmatrix}1&2\\2&1\end{pmatrix},\quad \mathbf{A}_3=\begin{pmatrix}1&1\\1&1\end{pmatrix},$$

$$\mathbf{A}_4=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad \mathbf{A}_5=\begin{pmatrix}1&2\\0&1\end{pmatrix}.$$

Was lässt sich bei der singulären unter ihnen über die beiden Komponenten sagen?

:::loesung
$\mathbf{A}_1$: symmetrisch mit den Eigenwerten $3$ und $1$, positiv definit: ja. $\mathbf{A}_2$: Eigenwerte $3$ und $-1$: nein, in Richtung $(1,-1)^{\top}$ ergäbe sich eine negative Varianz. $\mathbf{A}_3$: Eigenwerte $2$ und $0$, positiv semidefinit: ja, aber singulär. $\mathbf{A}_4$: Ein Diagonaleintrag ist eine Varianz und kann nicht $-1$ sein: nein. $\mathbf{A}_5$: nein, denn eine Kovarianzmatrix muss wegen $\operatorname{Cov}(x_1,x_2)=\operatorname{Cov}(x_2,x_1)$ symmetrisch sein. Bei $\mathbf{A}_3$ ist $\operatorname{Var}(x_1-x_2)=1-1-1+1=0$: Die Differenz ist mit Wahrscheinlichkeit $1$ konstant, $x_2=x_1+c$. Die beiden Komponenten tragen dieselbe Information.
:::
:::

:::aufgabe Aufgabe 36 ★★★ Komponentenweise nachgerechnet
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

Beweise $\operatorname{Cov}(\mathbf{y})=\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}$ für $\mathbf{y}=\mathbf{A}\mathbf{x}$ komponentenweise: Schreibe $y_i=\sum_ja_{ij}x_j$ und rechne $\operatorname{Cov}(y_i,y_k)$ mit der Linearität der Kovarianz aus.

</li>

<li>

Zeige, dass für die empirische Kovarianzmatrix die Spur $\operatorname{spur}\mathbf{S}$ gleich dem mittleren quadrierten Abstand der Datenpunkte von ihrem Mittelwert ist.

</li>

</ol>

:::loesung
(a) Mit $y_i=\sum_ja_{ij}x_j$ und der Linearität der Kovarianz in beiden Argumenten ist

$$\operatorname{Cov}(y_i,y_k)=\operatorname{Cov}\Bigl(\sum_ja_{ij}x_j,\ \sum_la_{kl}x_l\Bigr)=\sum_j\sum_la_{ij}\,\Sigma_{jl}\,a_{kl}=(\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top})_{ik} .$$

(b) $\operatorname{spur}\mathbf{S}=\sum_jS_{jj}=\sum_j\tfrac1N\sum_i(x_{ij}-\bar x_j)^2=\tfrac1N\sum_i\sum_j(x_{ij}-\bar x_j)^2=\tfrac1N\sum_i\lVert\mathbf{x}_i-\bar{\mathbf{x}}\rVert^2$, der mittlere quadrierte Abstand vom Mittelwert. Weil die Spur die Summe der Eigenwerte ist ([Grundlagen 2, Abschnitt 6.5](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5)), verteilt sich diese Gesamtstreuung auf die Hauptachsen.
:::
:::
