---
title: Projektion auf einen Unterraum
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
knoten: Grundlagen 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15220500
summary: Der vorige Abschnitt hat den nächsten Punkt eines Spaltenraums gefunden.
tags: Unterraum, Projektionsmatrix, orthogonale Komplement, Gram-Schmidt-Verfahren, QR-Zerlegung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Der vorige Abschnitt hat den nächsten Punkt eines Spaltenraums gefunden. Dieser Abschnitt fasst das Ergebnis als Matrix, zeigt, dass alles besonders einfach wird, wenn die Spalten orthonormal sind, und stellt ein Verfahren vor, das aus beliebigen unabhängigen Spalten orthonormale macht. Damit lässt sich die beste Näherungslösung berechnen, ohne $\mathbf{A}^{\top}\mathbf{A}$ zu bilden.
:::

### Unterräume

<span class="anker" id="stufe-4-1"></span>

Geraden und Ebenen durch den Nullpunkt, Spaltenräume und Kerne haben eine gemeinsame Eigenschaft: Mit zwei Vektoren enthalten sie auch jede Linearkombination der beiden. Man verlässt sie durch Addieren und Vervielfachen nie. Für solche Mengen gibt es ein eigenes Wort.

:::definition Definition 4.1 (Unterraum)
<span class="anker" id="satz-4-1"></span>

Eine Menge $\mathcal U\subseteq\mathbb{R}^n$ heißt __Unterraum__ des $\mathbb{R}^n$, wenn sie der Spann von endlich vielen Vektoren ist.
:::

Gleichwertig: $\mathcal U$ enthält den Nullvektor, und mit zwei Vektoren $\mathbf{u},\mathbf{v}$ enthält $\mathcal U$ auch $\mathbf{u}+\mathbf{v}$ und jedes Vielfache $c\,\mathbf{u}$. Jeder Unterraum hat eine Basis und damit nach [Grundlagen 1, Abschnitt 13.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), eine Dimension.

⁠**Rechenbeispiel:** Im $\mathbb{R}^3$ sind Unterräume: der Nullpunkt allein, mit der Dimension $0$; jede Gerade durch den Nullpunkt, mit der Dimension $1$; jede Ebene durch den Nullpunkt, wie der Spaltenraum von $\mathbf{H}$ aus dem vorigen Abschnitt, mit der Dimension $2$; und der ganze $\mathbb{R}^3$. Der Kern einer Matrix ist ein Unterraum, der Spaltenraum ebenfalls. Eine Gerade, die nicht durch den Nullpunkt geht, ist kein Unterraum, denn sie enthält den Nullvektor nicht.

⁠**Kurz gesagt:** Ein Unterraum ist ein Spann von Vektoren; man verlässt ihn durch Addieren und Vervielfachen nicht.

### Die Projektionsmatrix eines Spaltenraums

<span class="anker" id="stufe-4-2"></span>

Bei linear unabhängigen Spalten liefert [(3.5)](die-beste-naherungslosung.html#gl-3-5) den nächsten Punkt $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$. Die Matrix vor $\mathbf{y}$ hängt nur von $\mathbf{A}$ ab. Sie leistet für den Spaltenraum, was $\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ für eine Gerade geleistet hat.

:::definition Definition 4.2 (Projektionsmatrix eines Spaltenraums)
<span class="anker" id="satz-4-2"></span>

Hat $\mathbf{A}$ linear unabhängige Spalten, so heißt

<span class="anker" id="gl-4-1"></span>
$$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{4.1}$$

die __Projektionsmatrix__ auf den Spaltenraum von $\mathbf{A}$.
:::

:::satz Satz 4.3 (Eigenschaften)
<span class="anker" id="satz-4-3"></span>

Es gilt $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$, $\mathbf{P}^{\top}=\mathbf{P}$, $\mathbf{P}^2=\mathbf{P}$ und $\mathbf{P}\mathbf{A}=\mathbf{A}$. Also ist $\mathbf{P}$ die orthogonale Projektion auf den Spaltenraum.
:::

:::beweis Eigenschaften
Die erste Gleichung ist die Herleitung oben. Mit den Rechenregeln aus [Grundlagen 1, Abschnitte 10.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1) und [11.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-4), ist $\mathbf{P}^{\top}=\mathbf{A}\bigl((\mathbf{A}^{\top}\mathbf{A})^{-1}\bigr)^{\top}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$, denn $\mathbf{A}^{\top}\mathbf{A}$ ist symmetrisch und damit auch ihre Inverse. Weiter ist $\mathbf{P}\mathbf{A}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}(\mathbf{A}^{\top}\mathbf{A})=\mathbf{A}$, und daraus $\mathbf{P}^2=\mathbf{P}\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$. Nach dem Satz in Abschnitt [2.4](projektion-auf-eine-gerade.html#stufe-2-4) ist eine symmetrische Projektion orthogonal.
:::

Die Gleichung $\mathbf{P}\mathbf{A}=\mathbf{A}$ sagt: Jede Spalte, und damit jeder Vektor des Spaltenraums, bleibt beim Projizieren, wo er ist.

⁠**Rechenbeispiel:** Für $\mathbf{H}$ ist

$$\mathbf{P}=\mathbf{H}\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf{H}^{\top}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

Probe: $\mathbf{P}(1,\,1,\,1)^{\top}=\tfrac13(2,\,2,\,4)^{\top}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}=\hat{\mathbf{y}}$, und $\mathbf{P}\mathbf{a}_1=\tfrac13(2+1,\ -1+1,\ 1+2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_1$.

⁠**Kurz gesagt:** Die Projektionsmatrix $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ bildet jeden Vektor auf den nächsten Punkt des Spaltenraums ab; sie ist symmetrisch und erfüllt $\mathbf{P}^2=\mathbf{P}$.

### Orthonormale Spalten

<span class="anker" id="stufe-4-3"></span>

Die Formel [(4.1)](#gl-4-1) enthält eine Inverse. Sie verschwindet, wenn die Spalten orthonormal sind, denn dann ist $\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. Für eine Matrix $\mathbf{Q}$ mit orthonormalen Spalten ist die beste Näherungslösung deshalb schlicht $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$: Ihre Komponenten sind die Schattenlängen $\mathbf{q}_i^{\top}\mathbf{y}$.

:::satz Satz 4.4 (Projektion bei orthonormalen Spalten)
<span class="anker" id="satz-4-4"></span>

Hat $\mathbf{Q}\in\mathbb{R}^{n\times k}$ orthonormale Spalten $\mathbf{q}_1,\dots,\mathbf{q}_k$, so ist die Projektionsmatrix auf ihren Spaltenraum

<span class="anker" id="gl-4-2"></span>
$$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}=\sum_{i=1}^k\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{4.2}$$
:::

Die Summenform folgt aus [Grundlagen 1, Abschnitt 9.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5): Ein Matrixprodukt ist die Summe der äußeren Produkte aus Spalten und Zeilen. Jeder Summand $\mathbf{q}_i\mathbf{q}_i^{\top}$ ist die Projektionsmatrix auf die Gerade in Richtung $\mathbf{q}_i$. Bei orthonormalen Spalten ist die Projektion auf den Spaltenraum also die Summe der Projektionen auf die einzelnen Achsen. Das erklärt nachträglich den letzten Unterabschnitt von Abschnitt [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1): $\mathbf{Q}\mathbf{Q}^{\top}$ ist nicht die Einheitsmatrix, sondern die Projektion auf den Spaltenraum von $\mathbf{Q}$. Was senkrecht dazu liegt, wirft sie weg.

⁠**Rechenbeispiel:** Die Vektoren $\mathbf{q}_1=\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}$ und $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ sind orthonormal: $\lVert\mathbf{q}_1\rVert^2=\tfrac22$, $\lVert\mathbf{q}_2\rVert^2=\tfrac66$, $\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac{-1+0+1}{\sqrt{12}}=0$. Bei beiden ist die dritte Komponente die Summe der ersten beiden; sie bilden eine Orthonormalbasis der Ebene von $\mathbf{H}$. Es ist

$$\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}=\frac12\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}+\frac16\begin{pmatrix}1&-2&-1\\-2&4&2\\-1&2&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix},$$

dieselbe Matrix wie im vorigen Unterabschnitt, diesmal ohne Inverse.

⁠**Kurz gesagt:** Bei orthonormalen Spalten ist $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ und $\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}$, die Summe der Projektionen auf die einzelnen Spalten.

### Das orthogonale Komplement

<span class="anker" id="stufe-4-4"></span>

Projiziert man $\mathbf{y}$ auf einen Unterraum, bleibt das Residuum $\mathbf{y}-\mathbf{P}\mathbf{y}$ übrig. Es steht senkrecht auf dem ganzen Unterraum. Alle Vektoren mit dieser Eigenschaft bilden selbst einen Unterraum, und $\mathbf{y}$ zerfällt in einen Teil in dem einen und einen Teil in dem anderen.

:::definition Definition 4.5 (Orthogonales Komplement)
<span class="anker" id="satz-4-5"></span>

Das __orthogonale Komplement__ eines Unterraums $\mathcal U\subseteq\mathbb{R}^n$ ist die Menge

<span class="anker" id="gl-4-3"></span>
$$\mathcal U^\perp=\{\mathbf{z}\in\mathbb{R}^n:\ \mathbf{z}^{\top}\mathbf{u}=0\ \text{für alle}\ \mathbf{u}\in\mathcal U\} . \tag{4.3}$$
:::

Gelesen wird $\mathcal U^\perp$ als „$\mathcal U$ senkrecht“. Ist $\mathcal U$ der Spaltenraum von $\mathbf{A}$, so steht $\mathbf{z}$ genau dann senkrecht auf $\mathcal U$, wenn $\mathbf{A}^{\top}\mathbf{z}=\mathbf{0}$ ist; das orthogonale Komplement ist also der Kern von $\mathbf{A}^{\top}$.

:::satz Satz 4.6 (Zerlegung in zwei senkrechte Teile)
<span class="anker" id="satz-4-6"></span>

Ist $\mathbf{P}$ die orthogonale Projektion auf einen Unterraum $\mathcal U$ des $\mathbb{R}^n$, so gilt:

<ol class="rm">

<li>

Jeder Vektor $\mathbf{y}$ ist auf genau eine Weise die Summe $\mathbf{y}=\mathbf{u}+\mathbf{z}$ mit $\mathbf{u}\in\mathcal U$ und $\mathbf{z}\in\mathcal U^\perp$, nämlich $\mathbf{u}=\mathbf{P}\mathbf{y}$ und $\mathbf{z}=(\mathbf{I}-\mathbf{P})\mathbf{y}$.

</li>

<li>

$\mathbf{I}-\mathbf{P}$ ist die orthogonale Projektion auf $\mathcal U^\perp$.

</li>

<li>

$\dim\mathcal U^\perp=n-\dim\mathcal U$.

</li>

</ol>
:::

:::beweis Zerlegung
(i) Dass $\mathbf{P}\mathbf{y}$ in $\mathcal U$ liegt und $\mathbf{y}-\mathbf{P}\mathbf{y}$ senkrecht auf $\mathcal U$ steht, ist die Definition der orthogonalen Projektion. Gäbe es eine zweite Zerlegung $\mathbf{y}=\mathbf{u}'+\mathbf{z}'$, so wäre $\mathbf{u}-\mathbf{u}'=\mathbf{z}'-\mathbf{z}$ ein Vektor, der in $\mathcal U$ liegt und zugleich senkrecht auf $\mathcal U$ steht, also senkrecht auf sich selbst. Sein Längenquadrat ist dann null, also ist er der Nullvektor. (ii) $\mathbf{I}-\mathbf{P}$ ist symmetrisch, und $(\mathbf{I}-\mathbf{P})^2=\mathbf{I}-2\mathbf{P}+\mathbf{P}^2=\mathbf{I}-\mathbf{P}$. Ihr Bild liegt nach (i) in $\mathcal U^\perp$. Jedes $\mathbf{z}\in\mathcal U^\perp$ bleibt fest: $\mathbf{P}\mathbf{z}$ liegt in $\mathcal U$ und ist zugleich die Differenz $\mathbf{z}-(\mathbf{z}-\mathbf{P}\mathbf{z})$ zweier Vektoren, die senkrecht auf $\mathcal U$ stehen; also steht $\mathbf{P}\mathbf{z}$ senkrecht auf sich selbst und ist $\mathbf{0}$. (iii) Wählt man für $\mathcal U$ eine Basis als Spalten einer Matrix $\mathbf{A}$, so ist $\mathcal U^\perp$ der Kern von $\mathbf{A}^{\top}$. Nach dem Rangsatz aus [Grundlagen 1, Abschnitt 13.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), hat er die Dimension $n-\operatorname{rang}\mathbf{A}^{\top}=n-\operatorname{rang}\mathbf{A}=n-\dim\mathcal U$.
:::

⁠**Rechenbeispiel:** Die Ebene von $\mathbf{H}$ hat die Dimension $2$, ihr orthogonales Komplement im $\mathbb{R}^3$ also die Dimension $1$: die Gerade in Richtung des Normalenvektors $\mathbf{k}=(1,\,1,\,-1)^{\top}$. Tatsächlich ist $\mathbf{H}^{\top}\mathbf{k}=(1-1,\ 1-1)^{\top}=\mathbf{0}$. Es ist

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&1&-1\\1&1&-1\\-1&-1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}},$$

die Projektion auf diese Gerade. Für $\mathbf{y}=(1,\,1,\,1)^{\top}$ ist $(\mathbf{I}-\mathbf{P})\mathbf{y}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$, das Residuum aus dem vorigen Abschnitt.

⁠**Kurz gesagt:** Das orthogonale Komplement $\mathcal U^\perp$ enthält alle Vektoren senkrecht zu $\mathcal U$; jeder Vektor zerfällt eindeutig in einen Teil in $\mathcal U$ und einen in $\mathcal U^\perp$, und die Dimensionen ergänzen sich zu $n$.

### Das Gram-Schmidt-Verfahren

<span class="anker" id="stufe-4-5"></span>

Orthonormale Spalten machen alles einfach, aber gegeben sind meist beliebige Spalten. Das Gram-Schmidt-Verfahren baut aus linear unabhängigen Vektoren $\mathbf{a}_1,\dots,\mathbf{a}_k$ orthonormale Vektoren $\mathbf{q}_1,\dots,\mathbf{q}_k$, die denselben Unterraum aufspannen.

Die Idee zeigt Abb. [11](#abb-11) für zwei Vektoren. Man normiert den ersten. Vom zweiten zieht man seinen Schatten auf den ersten ab, also seine Projektion. Was übrig bleibt, steht senkrecht auf dem ersten, und man normiert es. Beim dritten Vektor zieht man die Schatten auf die beiden schon gefundenen ab, und so weiter.

:::abbildung ml/k2gramschmidt 11
Das Gram-Schmidt-Verfahren für $\mathbf{a}_1=(2,1)^{\top}$ und $\mathbf{a}_2=(1,2)^{\top}$. Zuerst wird $\mathbf{a}_1$ normiert: $\mathbf{q}_1=\mathbf{a}_1/\sqrt5$. Vom zweiten Vektor zieht man seinen Schatten $(\mathbf{q}_1^{\top}\mathbf{a}_2)\,\mathbf{q}_1=(1{,}6;\,0{,}8)^{\top}$ ab (blau). Der Rest $\tilde{\mathbf{q}}_2=(-0{,}6;\,1{,}2)^{\top}$ (orange, parallel zur gestrichelten Lotlinie) steht senkrecht auf $\mathbf{q}_1$; normiert ergibt er $\mathbf{q}_2=(-1,2)^{\top}/\sqrt5$.
:::

:::definition Definition 4.7 (Gram-Schmidt-Verfahren)
<span class="anker" id="satz-4-7"></span>

Gegeben sind linear unabhängige Vektoren $\mathbf{a}_1,\dots,\mathbf{a}_k\in\mathbb{R}^n$. Das __Gram-Schmidt-Verfahren__ berechnet für $i=1,\dots,k$ nacheinander

<span class="anker" id="gl-4-4"></span>
$$\tilde{\mathbf{q}}_i=\mathbf{a}_i-\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l,\qquad \mathbf{q}_i=\frac{\tilde{\mathbf{q}}_i}{\lVert\tilde{\mathbf{q}}_i\rVert} . \tag{4.4}$$
:::

Für $i=1$ ist die Summe leer, also $\tilde{\mathbf{q}}_1=\mathbf{a}_1$. Die Summe ist die Projektion von $\mathbf{a}_i$ auf den Spann der schon gefundenen Vektoren, nach [(4.2)](#gl-4-2); $\tilde{\mathbf{q}}_i$ ist das Residuum dieser Projektion.

:::satz Satz 4.8 (Was Gram-Schmidt liefert)
<span class="anker" id="satz-4-8"></span>

Die Vektoren $\mathbf{q}_1,\dots,\mathbf{q}_k$ sind orthonormal, und für jedes $i$ spannen $\mathbf{q}_1,\dots,\mathbf{q}_i$ denselben Unterraum auf wie $\mathbf{a}_1,\dots,\mathbf{a}_i$.
:::

:::beweis Gram-Schmidt
Man geht Schritt für Schritt vor. Angenommen, $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ sind schon orthonormal und spannen denselben Unterraum auf wie $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$. Dann ist $\tilde{\mathbf{q}}_i$ das Residuum der Projektion von $\mathbf{a}_i$ auf diesen Unterraum und steht deshalb senkrecht auf $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$; direkt nachgerechnet ist $\mathbf{q}_l^{\top}\tilde{\mathbf{q}}_i=\mathbf{q}_l^{\top}\mathbf{a}_i-\mathbf{q}_l^{\top}\mathbf{a}_i=0$. Es ist $\tilde{\mathbf{q}}_i\ne\mathbf{0}$, denn sonst wäre $\mathbf{a}_i$ eine Linearkombination von $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ und damit von $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$, im Widerspruch zur Unabhängigkeit. Also darf man normieren. Schließlich ist $\mathbf{a}_i=\tilde{\mathbf{q}}_i+\sum_l(\mathbf{q}_l^{\top}\mathbf{a}_i)\mathbf{q}_l$ eine Linearkombination von $\mathbf{q}_1,\dots,\mathbf{q}_i$, und umgekehrt ist $\mathbf{q}_i$ eine Linearkombination von $\mathbf{a}_i$ und $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$. Beide Listen spannen also denselben Unterraum auf.
:::

Sind die gegebenen Vektoren doch abhängig, bemerkt das Verfahren es selbst: Irgendwann ist $\tilde{\mathbf{q}}_i=\mathbf{0}$, und man kann nicht normieren.

⁠**Rechenbeispiel:** Für die Spalten von $\mathbf{H}$, $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ und $\mathbf{a}_2=(0,\,1,\,1)^{\top}$, ist $\mathbf{q}_1=\mathbf{a}_1/\sqrt2$. Dann ist $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ und

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\frac1{\sqrt2}\,\mathbf{q}_1=(0,\,1,\,1)^{\top}-\tfrac12(1,\,0,\,1)^{\top}=\bigl(-\tfrac12,\,1,\,\tfrac12\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{\tfrac14+1+\tfrac14}=\sqrt{\tfrac32} .$$

Normiert ist $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$, genau die Orthonormalbasis aus dem Rechenbeispiel zu [(4.2)](#gl-4-2). Die beiden Summen dieses Rechenbeispiels zeigt Abb. [12](#abb-12).

:::abbildung ml/k2rgs 12
Gram-Schmidt für die Spalten von $\mathbf{H}$: das Skalarprodukt $\mathbf{q}_1^{\top}\mathbf{a}_2$ mit $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ und $\mathbf{a}_2=(0,1,1)^{\top}$, das die Länge des Schattens angibt, und das Längenquadrat des Rests $\tilde{\mathbf{q}}_2=(-\tfrac12,1,\tfrac12)^{\top}$.
:::

⁠**Kurz gesagt:** Gram-Schmidt zieht von jedem Vektor seine Projektion auf die schon gefundenen ab und normiert den Rest; so entsteht eine Orthonormalbasis desselben Unterraums.

:::hintergrund Aufwand und Rundungsfehler
Für $k$ Vektoren mit je $n$ Komponenten braucht das Verfahren etwa $2nk^2$ Grundrechenarten: Im Schritt $i$ sind $i-1$ Skalarprodukte und ebenso viele Vielfache abzuziehen, jedes kostet etwa $2n$, und die Summe über $i$ wächst wie $k^2$. Mit gerundeten Zahlen ist die Fassung [(4.4)](#gl-4-4) empfindlich: Sind zwei der gegebenen Vektoren fast parallel, ist $\tilde{\mathbf{q}}_i$ eine kleine Differenz großer Zahlen, und die berechneten $\mathbf{q}_i$ sind dann nicht mehr genau orthogonal. Eine leicht veränderte Reihenfolge der Rechenschritte, das modifizierte Gram-Schmidt-Verfahren, zieht die Schatten einzeln vom schon verkleinerten Rest ab statt alle vom ursprünglichen $\mathbf{a}_i$. Mit exakten Zahlen liefert sie dasselbe, mit gerundeten Zahlen ist sie deutlich genauer. Programmbibliotheken benutzen meist noch andere Verfahren, die mit Spiegelungen arbeiten, also mit orthogonalen Matrizen.
:::

### Die QR-Zerlegung

<span class="anker" id="stufe-4-6"></span>

Das Gram-Schmidt-Verfahren lässt sich als Zerlegung einer Matrix schreiben. Nach dem Beweis oben ist jeder Vektor $\mathbf{a}_i$ eine Linearkombination von $\mathbf{q}_1,\dots,\mathbf{q}_i$, und zwar

$$\mathbf{a}_i=\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l+\lVert\tilde{\mathbf{q}}_i\rVert\,\mathbf{q}_i .$$

In ihm kommen nur die ersten $i$ der Vektoren $\mathbf{q}_l$ vor, die späteren nicht. Schreibt man die Koeffizienten als Spalten einer Matrix, entsteht deshalb eine Dreiecksmatrix.

:::definition Definition 4.9 (QR-Zerlegung)
<span class="anker" id="satz-4-9"></span>

Hat $\mathbf{A}\in\mathbb{R}^{m\times n}$ linear unabhängige Spalten, so ist die __QR-Zerlegung__ die Darstellung

<span class="anker" id="gl-4-5"></span>
$$\mathbf{A}=\mathbf{Q}\mathbf{R} \tag{4.5}$$

mit einer Matrix $\mathbf{Q}\in\mathbb{R}^{m\times n}$ mit orthonormalen Spalten und einer oberen Dreiecksmatrix $\mathbf{R}\in\mathbb{R}^{n\times n}$ mit positiven Diagonaleinträgen. Dabei ist $r_{li}=\mathbf{q}_l^{\top}\mathbf{a}_i$ für $l<i$ und $r_{ii}=\lVert\tilde{\mathbf{q}}_i\rVert$.
:::

Eine obere Dreiecksmatrix hat unterhalb der Diagonale nur Nullen. Spalte $i$ von $\mathbf{Q}\mathbf{R}$ ist nach der Spaltensicht $\sum_lr_{li}\mathbf{q}_l$, also genau die Darstellung von $\mathbf{a}_i$ oben. Die Spalten von $\mathbf{Q}$ liefert das Gram-Schmidt-Verfahren, die Einträge von $\mathbf{R}$ fallen dabei nebenbei ab. Weil $\mathbf{Q}$ orthonormale Spalten hat, ist außerdem $\mathbf{R}=\mathbf{Q}^{\top}\mathbf{A}$.

⁠**Rechenbeispiel:** Für $\mathbf{H}$ ist

$$\mathbf{Q}=\begin{pmatrix}\tfrac1{\sqrt2}&-\tfrac1{\sqrt6}\\0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&\tfrac1{\sqrt2}\\0&\sqrt{\tfrac32}\end{pmatrix}\approx\begin{pmatrix}1{,}414&0{,}707\\0&1{,}225\end{pmatrix}.$$

Probe der zweiten Spalte: $\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}+\sqrt{\tfrac32}\cdot\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}=\tfrac12(1,\,0,\,1)^{\top}+\tfrac12(-1,\,2,\,1)^{\top}=(0,\,1,\,1)^{\top}=\mathbf{a}_2$.

⁠**Kurz gesagt:** Die QR-Zerlegung $\mathbf{A}=\mathbf{Q}\mathbf{R}$ schreibt das Gram-Schmidt-Verfahren als Matrixprodukt: $\mathbf{Q}$ hat orthonormale Spalten, $\mathbf{R}$ ist eine obere Dreiecksmatrix.

### Die beste Näherungslösung mit QR

<span class="anker" id="stufe-4-7"></span>

Mit der QR-Zerlegung lassen sich die Normalgleichungen lösen, ohne $\mathbf{A}^{\top}\mathbf{A}$ zu berechnen. Man setzt $\mathbf{A}=\mathbf{Q}\mathbf{R}$ ein und benutzt $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.

:::satz Satz 4.10 (Beste Näherungslösung mit QR)
<span class="anker" id="satz-4-10"></span>

Ist $\mathbf{A}=\mathbf{Q}\mathbf{R}$ die QR-Zerlegung, so ist die beste Näherungslösung von $\mathbf{A}\mathbf{x}=\mathbf{y}$ die Lösung von

<span class="anker" id="gl-4-6"></span>
$$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y} . \tag{4.6}$$
:::

:::beweis Lösen mit QR
Es ist $\mathbf{A}^{\top}\mathbf{A}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{R}^{\top}\mathbf{R}$ und $\mathbf{A}^{\top}\mathbf{y}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. Die Normalgleichungen lauten also $\mathbf{R}^{\top}\mathbf{R}\hat{\mathbf{x}}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. Die Dreiecksmatrix $\mathbf{R}$ hat positive Diagonaleinträge, also nach [Grundlagen 1, Abschnitt 14.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-4), eine Determinante ungleich null, und ist invertierbar; ebenso $\mathbf{R}^{\top}$. Multipliziert man von links mit $(\mathbf{R}^{\top})^{-1}$, bleibt [(4.6)](#gl-4-6).
:::

Das System [(4.6)](#gl-4-6) hat Dreiecksform und wird von unten nach oben gelöst, wie das Rückwärtseinsetzen am Ende des Gauß-Verfahrens in [Grundlagen 1, Abschnitt 12.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3). Für eine $m\times n$-Matrix kostet der ganze Weg etwa $2mn^2$ Grundrechenarten, fast alles davon für die QR-Zerlegung.

⁠**Rechenbeispiel:** Für $\mathbf{H}$ und $\mathbf{y}=(1,\,1,\,1)^{\top}$ ist $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac2{\sqrt2},\ \tfrac{-1+2+1}{\sqrt6}\bigr)^{\top}=\bigl(\sqrt2,\ \tfrac2{\sqrt6}\bigr)^{\top}$. Die untere Zeile von [(4.6)](#gl-4-6) lautet $\sqrt{\tfrac32}\,\hat x_2=\tfrac2{\sqrt6}$, also $\hat x_2=\tfrac2{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac23$. Die obere Zeile lautet $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac23=\sqrt2$, also $\hat x_1=1-\tfrac13=\tfrac23$. Das ist dieselbe Lösung wie mit den Normalgleichungen. Die Komponenten von $\mathbf{Q}^{\top}\mathbf{y}$ sind die Skalarprodukte in Abb. [13](#abb-13).

:::abbildung ml/k2rqr 13
Die rechte Seite $\mathbf{Q}^{\top}\mathbf{y}$ des Dreieckssystems für $\mathbf{y}=(1,1,1)^{\top}$, mit $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ und $\mathbf{q}_2=(-1,2,1)^{\top}/\sqrt6$.
:::

⁠**Kurz gesagt:** Mit $\mathbf{A}=\mathbf{Q}\mathbf{R}$ wird aus den Normalgleichungen das Dreieckssystem $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$; die Matrix $\mathbf{A}^{\top}\mathbf{A}$ wird dabei nie gebildet.

:::aufgabe Aufgabe 11 ★ Gram-Schmidt und Projektion
<span class="anker" id="aufg-11"></span>

Gegeben sind $\mathbf{a}_1=(1,\,1,\,0)^{\top}$ und $\mathbf{a}_2=(1,\,0,\,1)^{\top}$.

<ol class="al">

<li>

Wende das Gram-Schmidt-Verfahren an und prüfe, dass $\mathbf{q}_1,\mathbf{q}_2$ orthonormal sind.

</li>

<li>

Berechne die Projektionsmatrix $\mathbf{P}=\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}$ auf die Ebene, die $\mathbf{a}_1$ und $\mathbf{a}_2$ aufspannen, und projiziere $\mathbf{y}=(1,\,2,\,3)^{\top}$.

</li>

<li>

Bestimme einen Vektor, der das orthogonale Komplement der Ebene aufspannt, und prüfe $\mathbf{I}-\mathbf{P}=\mathbf{k}\mathbf{k}^{\top}/(\mathbf{k}^{\top}\mathbf{k})$.

</li>

</ol>

:::loesung
(a) $\mathbf{q}_1=\mathbf{a}_1/\sqrt2=(1,\,1,\,0)^{\top}/\sqrt2$. Dann ist $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ und

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\tfrac1{\sqrt2}\,\mathbf{q}_1=(1,\,0,\,1)^{\top}-\tfrac12(1,\,1,\,0)^{\top}=\bigl(\tfrac12,\,-\tfrac12,\,1\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert^2=\tfrac14+\tfrac14+1=\tfrac32 ,$$

also $\mathbf{q}_2=\tilde{\mathbf{q}}_2/\sqrt{3/2}=(1,\,-1,\,2)^{\top}/\sqrt6$. Probe: $\mathbf{q}_1^{\top}\mathbf{q}_2=(1-1+0)/\sqrt{12}=0$, $\lVert\mathbf{q}_2\rVert^2=\tfrac{1+1+4}6=1$.

(b)

$$\mathbf{P}=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}+\frac16\begin{pmatrix}1&-1&2\\-1&1&-2\\2&-2&4\end{pmatrix}=\frac13\begin{pmatrix}2&1&1\\1&2&-1\\1&-1&2\end{pmatrix},$$

$$\mathbf{P}\mathbf{y}=\frac13\begin{pmatrix}2+2+3\\1+4-3\\1-2+6\end{pmatrix}=\begin{pmatrix}7/3\\2/3\\5/3\end{pmatrix}.$$

(c) Gesucht ist $\mathbf{k}$ mit $\mathbf{a}_1^{\top}\mathbf{k}=k_1+k_2=0$ und $\mathbf{a}_2^{\top}\mathbf{k}=k_1+k_3=0$, also $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ oder ein Vielfaches. Es ist $\mathbf{k}^{\top}\mathbf{k}=3$ und

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&-1&-1\\-1&1&1\\-1&1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}} .$$

Das orthogonale Komplement der Ebene ist die Gerade in Richtung $\mathbf{k}$, mit der Dimension $3-2=1$. Zur Kontrolle: $\mathbf{y}-\mathbf{P}\mathbf{y}=(-\tfrac43,\,\tfrac43,\,\tfrac43)^{\top}=-\tfrac43\mathbf{k}$ liegt auf ihr.
:::
:::

:::aufgabe Aufgabe 12 ★★ Lösen mit QR
<span class="anker" id="aufg-12"></span>

Benutze die Matrix $\mathbf{A}$ mit den Spalten $\mathbf{a}_1$ und $\mathbf{a}_2$ aus Aufgabe [11](#aufg-11).

<ol class="al">

<li>

Gib die QR-Zerlegung an und prüfe $\mathbf{Q}\mathbf{R}=\mathbf{A}$.

</li>

<li>

Löse $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$ im Sinne der kleinsten Quadrate mit [(4.6)](#gl-4-6) und zur Kontrolle mit den Normalgleichungen.

</li>

</ol>

:::loesung
(a) Aus Aufgabe [11](#aufg-11): $\mathbf{q}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{q}_2=(1,\,-1,\,2)^{\top}/\sqrt6$, $r_{11}=\lVert\mathbf{a}_1\rVert=\sqrt2$, $r_{12}=\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$, $r_{22}=\lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{3/2}$:

$$\mathbf{Q}=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.$$

Probe: Spalte 1 von $\mathbf{Q}\mathbf{R}$ ist $\sqrt2\,\mathbf{q}_1=\mathbf{a}_1$; Spalte 2 ist $\tfrac1{\sqrt2}\mathbf{q}_1+\sqrt{\tfrac32}\,\mathbf{q}_2=\tfrac12(1,\,1,\,0)^{\top}+\tfrac12(1,\,-1,\,2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_2$, denn $\sqrt{3/2}/\sqrt6=\tfrac12$.

(b) $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac3{\sqrt2},\ \tfrac{1-2+6}{\sqrt6}\bigr)^{\top}=\bigl(\tfrac3{\sqrt2},\ \tfrac5{\sqrt6}\bigr)^{\top}$. Die untere Zeile von $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ ergibt $\hat x_2=\tfrac5{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac53$, die obere $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac53=\tfrac3{\sqrt2}$, mit $\sqrt2$ multipliziert $2\hat x_1+\tfrac53=3$, also $\hat x_1=\tfrac23$. Kontrolle mit den Normalgleichungen: $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}^{\top}\mathbf{y}=(3,\,4)^{\top}$, $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(3,\,4)^{\top}=(\tfrac23,\,\tfrac53)^{\top}$. Außerdem ist $\mathbf{A}\hat{\mathbf{x}}=(\tfrac73,\,\tfrac23,\,\tfrac53)^{\top}=\mathbf{P}\mathbf{y}$ aus Aufgabe [11](#aufg-11).
:::
:::

:::aufgabe Aufgabe 13 ★★ Komplemente
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

Welche Dimension hat das orthogonale Komplement einer Geraden durch den Nullpunkt im $\mathbb{R}^3$? Welche das einer Geraden im $\mathbb{R}^5$?

</li>

<li>

Zeige: $(\mathcal U^\perp)^\perp=\mathcal U$. Tipp: Zeige zuerst, dass jeder Vektor aus $\mathcal U$ in $(\mathcal U^\perp)^\perp$ liegt. Zerlege dann einen Vektor $\mathbf{y}\in(\mathcal U^\perp)^\perp$ wie im Satz in Abschnitt [4.4](#stufe-4-4) und bilde das Skalarprodukt mit seinem Teil in $\mathcal U^\perp$.

</li>

</ol>

:::loesung
(a) Nach dem Satz in Abschnitt [4.4](#stufe-4-4) ist $\dim\mathcal U^\perp=n-\dim\mathcal U$: im $\mathbb{R}^3$ also $3-1=2$, eine Ebene; im $\mathbb{R}^5$ ist es $5-1=4$.

(b) Erster Teil: Ist $\mathbf{u}\in\mathcal U$, so ist $\mathbf{u}^{\top}\mathbf{z}=0$ für jedes $\mathbf{z}\in\mathcal U^\perp$, nach der Definition von $\mathcal U^\perp$. Also steht $\mathbf{u}$ senkrecht auf ganz $\mathcal U^\perp$ und liegt in $(\mathcal U^\perp)^\perp$. Zweiter Teil: Es sei $\mathbf{y}\in(\mathcal U^\perp)^\perp$. Nach dem Satz zerlegt man $\mathbf{y}=\mathbf{u}+\mathbf{z}$ mit $\mathbf{u}\in\mathcal U$ und $\mathbf{z}\in\mathcal U^\perp$. Dann ist $\mathbf{z}^{\top}\mathbf{y}=0$, weil $\mathbf{y}$ senkrecht auf $\mathcal U^\perp$ steht, und $\mathbf{z}^{\top}\mathbf{u}=0$, weil $\mathbf{z}$ senkrecht auf $\mathcal U$ steht. Also ist $\mathbf{z}^{\top}\mathbf{z}=\mathbf{z}^{\top}\mathbf{y}-\mathbf{z}^{\top}\mathbf{u}=0$, und $\mathbf{z}=\mathbf{0}$. Damit ist $\mathbf{y}=\mathbf{u}\in\mathcal U$. Beide Mengen enthalten einander, sie sind gleich.
:::
:::
