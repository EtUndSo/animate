---
title: Rechenregeln und Identitäten für Divergenz und Rotation
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
adresse: elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder
knoten: Kapitel 1: Differentialrechnung für Vektorfelder
order: 3110500
summary: Divergenz und Rotation schreibt man mit dem Nabla-Symbol wie ein Skalarprodukt und ein Kreuzprodukt.
tags: Kronecker-Symbol, Spatprodukt, Graßmann-Identität, äußere Produkt, divergenzfrei, Wirbelfeld, Vektorpotential, Eichfreiheit
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Divergenz und Rotation schreibt man mit dem Nabla-Symbol wie ein Skalarprodukt und ein Kreuzprodukt. Dieser Abschnitt zeigt, welche Rechenregeln für Vektoren sich übertragen lassen, wo Vorsicht nötig ist und was geschieht, wenn man zwei dieser Operatoren nacheinander anwendet. Zum Schluss geht es um Felder, die selbst eine Rotation sind.
:::

### Was du dafür brauchst: das Kronecker-Symbol

<span class="anker" id="stufe-4-1"></span>

In Rechnungen mit Indizes braucht man oft eine Zahl, die angibt, ob zwei Indizes gleich sind.

Das __Kronecker-Symbol__ ist

$$\delta_{il}=\begin{cases}1,&i=l,\\0,&i\neq l.\end{cases}$$

Als Matrix $(\delta_{il})_{il}$ geschrieben, stehen auf der Diagonale Einsen und sonst Nullen. Außerdem gilt $\delta_{il}=\hat{\boldsymbol{e}}_i\cdot\hat{\boldsymbol{e}}_l$. In einer Summe über einen Index wählt es einen Summanden aus: $\sum_{l}\delta_{il}\,a_l=a_i$.

::::beispiel
$\delta_{22}=1$, $\delta_{23}=0$. Für $\boldsymbol a=(4,5,6)$ ist $\sum_{l=1}^3\delta_{3l}\,a_l=a_3=6$.
::::

⁠**Kurz gesagt:** $\delta_{il}$ ist $1$ bei gleichen Indizes und sonst $0$; in einer Summe pickt es einen Summanden heraus.

### Was du dafür brauchst: das Spatprodukt

<span class="anker" id="stufe-4-2"></span>

Ein Skalarprodukt mit einem Kreuzprodukt kommt in den Produktregeln vor. Es hat eine einfache geometrische Bedeutung.

Für $\boldsymbol a,\boldsymbol b,\boldsymbol c\in\mathbb{R}^3$ heißt die Zahl

<span class="anker" id="gl-4-1"></span>
$$\boldsymbol a\cdot(\boldsymbol b\times\boldsymbol c)=\det(\boldsymbol a|\boldsymbol b|\boldsymbol c) \tag{4.1}$$

das __Spatprodukt__ von $\boldsymbol a,\boldsymbol b,\boldsymbol c$. Es ist der orientierte Rauminhalt des schiefen Quaders, den die drei Vektoren aufspannen. Zyklisches Vertauschen ändert es nicht:

$$\boldsymbol a\cdot(\boldsymbol b\times\boldsymbol c)=\boldsymbol b\cdot(\boldsymbol c\times\boldsymbol a)=\boldsymbol c\cdot(\boldsymbol a\times\boldsymbol b).$$

In Indizes ist es $\sum_{i,j,k}\varepsilon_{ijk}\,a_ib_jc_k$, nach [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6).

::::beispiel
Für $\boldsymbol a=(1,0,0)$, $\boldsymbol b=(0,1,0)$, $\boldsymbol c=(1,1,1)$ ist $\boldsymbol b\times\boldsymbol c=(1,0,-1)$ und $\boldsymbol a\cdot(\boldsymbol b\times\boldsymbol c)=1$. Ebenso ist $\det\bigl(\begin{smallmatrix}1&0&1\\0&1&1\\0&0&1\end{smallmatrix}\bigr)=1$.
::::

⁠**Kurz gesagt:** Das Spatprodukt $\boldsymbol a\cdot(\boldsymbol b\times\boldsymbol c)$ ist die Determinante der drei Vektoren und bleibt bei zyklischem Vertauschen gleich.

### Was du dafür brauchst: die Graßmann-Identität

<span class="anker" id="stufe-4-3"></span>

Für ein doppeltes Kreuzprodukt gibt es eine Formel, die ohne Kreuzprodukt auskommt. Sie ist der Schlüssel für die Rechenregeln mit zwei Rotationen.

Für $\boldsymbol a,\boldsymbol b,\boldsymbol c\in\mathbb{R}^3$ gilt die __Graßmann-Identität__

<span class="anker" id="gl-4-2"></span>
$$\boldsymbol a\times(\boldsymbol b\times\boldsymbol c)=(\boldsymbol a\cdot\boldsymbol c)\,\boldsymbol b-(\boldsymbol a\cdot\boldsymbol b)\,\boldsymbol c . \tag{4.2}$$

Beide Seiten sind in jedem der drei Vektoren linear. Deshalb genügt es, die Formel für alle Kombinationen von Einheitsvektoren $\hat{\boldsymbol{e}}_1,\hat{\boldsymbol{e}}_2,\hat{\boldsymbol{e}}_3$ nachzuprüfen. In Indizes lautet sie

<span class="anker" id="gl-4-3"></span>
$$\sum_{k=1}^3\varepsilon_{ijk}\,\varepsilon_{klm}=\delta_{il}\,\delta_{jm}-\delta_{im}\,\delta_{jl}. \tag{4.3}$$

::::beispiel
$\boldsymbol a=(1,2,0)$, $\boldsymbol b=(0,1,1)$, $\boldsymbol c=(1,0,1)$. Links: $\boldsymbol b\times\boldsymbol c=(1,1,-1)$ und $\boldsymbol a\times(1,1,-1)=(-2,1,-1)$. Rechts: $\boldsymbol a\cdot\boldsymbol c=1$ und $\boldsymbol a\cdot\boldsymbol b=2$, also $1\cdot(0,1,1)-2\cdot(1,0,1)=(-2,1,-1)$.
::::

:::hintergrund Warum die Indexform so aussieht
In der Summe $\sum_k\varepsilon_{ijk}\varepsilon_{klm}$ ist ein Summand nur dann nicht null, wenn $i,j,k$ verschieden sind und $k,l,m$ verschieden sind. Für $i=j$ ist also alles null, und rechts ebenso. Für $i\neq j$ ist $k$ der dritte Index, und dann müssen $l,m$ dieselben zwei Indizes sein wie $i,j$: entweder $l=i,m=j$ oder $l=j,m=i$. Im ersten Fall ist $\varepsilon_{ijk}\varepsilon_{kij}=\varepsilon_{ijk}^2=1$, denn $\varepsilon_{kij}=\varepsilon_{ijk}$ (zyklisch). Im zweiten Fall ist $\varepsilon_{ijk}\varepsilon_{kji}=-\varepsilon_{ijk}^2=-1$. Genau das zählt die rechte Seite: $\delta_{il}\delta_{jm}$ ist $1$ im ersten Fall, $\delta_{im}\delta_{jl}$ ist $1$ im zweiten. Geometrisch: $\boldsymbol b\times\boldsymbol c$ steht senkrecht auf der Ebene von $\boldsymbol b$ und $\boldsymbol c$, und ein zweites Kreuzprodukt damit führt in diese Ebene zurück. Deshalb ist das Ergebnis eine Kombination von $\boldsymbol b$ und $\boldsymbol c$.
:::

⁠**Kurz gesagt:** $\boldsymbol a\times(\boldsymbol b\times\boldsymbol c)=(\boldsymbol a\cdot\boldsymbol c)\boldsymbol b-(\boldsymbol a\cdot\boldsymbol b)\boldsymbol c$; in Indizes $\sum_k\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$.

### Rechnen mit dem Nabla-Symbol

<span class="anker" id="stufe-4-4"></span>

Der Gradient ist $\nabla\varphi$, die Divergenz $\nabla\cdot\boldsymbol{E}$, die Rotation $\nabla\times\boldsymbol{E}$. Das legt nahe, mit $\nabla$ wie mit einem Vektor zu rechnen. Das geht oft, aber nicht immer.

Der Grund: $\nabla$ ist kein Vektor aus Zahlen, sondern ein Ableitungsbefehl für alles, was rechts von ihm steht. Daraus folgen zwei Regeln.

<ol class="rm">

<li>

Die Reihenfolge zählt. $\nabla\cdot\boldsymbol{E}$ ist eine Funktion. Dagegen ist $\boldsymbol{E}\cdot\nabla=\sum_jE_j\,\partial/\partial x_j$ wieder ein Ableitungsbefehl, der auf eine Funktion rechts daneben wartet.

</li>

<li>

Steht rechts von $\nabla$ ein Produkt, wird jeder Faktor abgeleitet, wie bei der Produktregel einer Variablen.

</li>

</ol>

Jede Rechenregel dieses Abschnitts entsteht deshalb in zwei Schritten: zuerst die Produktregel, sodass jeder Faktor einmal abgeleitet wird, dann eine Rechenregel für Vektoren.

::::beispiel
Für $\varphi=x$ und $\boldsymbol{E}=(x,0,0)$ ist $\nabla\cdot(\varphi\boldsymbol{E})=\partial(x^2)/\partial x=2x$. Würde man $\varphi$ wie eine Zahl vor $\nabla$ ziehen, käme $x\,\nabla\cdot\boldsymbol{E}=x$ heraus, also nur die Hälfte: Der Beitrag, in dem $\varphi$ abgeleitet wird, fehlt.
::::

⁠**Kurz gesagt:** $\nabla$ leitet alles rechts von ihm ab. Mit ihm rechnet man wie mit einem Vektor, wenn man zusätzlich die Produktregel beachtet.

### Produktregeln mit einer skalaren Funktion

<span class="anker" id="stufe-4-5"></span>

Wie ändern sich Divergenz und Rotation, wenn man ein Feld mit einer skalaren Funktion multipliziert? Nach dem letzten Unterabschnitt wird einmal die Funktion abgeleitet und einmal das Feld.

:::satz Satz 4.1 (Produktregeln mit Skalar)
<span class="anker" id="satz-4-1"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen, $\varphi$ eine differenzierbare Funktion und $\boldsymbol{E}=(E_1,E_2,E_3)$ ein differenzierbares Vektorfeld auf $\mathcal U$. Dann gilt

<span class="anker" id="gl-4-4"></span>
$$\operatorname{div}(\varphi\boldsymbol{E})=\nabla\varphi\cdot\boldsymbol{E}+\varphi\,\operatorname{div}\boldsymbol{E},\qquad\operatorname{rot}(\varphi\boldsymbol{E})=\nabla\varphi\times\boldsymbol{E}+\varphi\,\operatorname{rot}\boldsymbol{E} . \tag{4.4}$$

Die erste Formel gilt in jeder Dimension (Satz [3.4](divergenz-rotation-und-laplace-operator.html#satz-3-4)).
:::

:::beweis Rotation eines Produkts
Mit [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6) und der Produktregel einer Variablen ist

$$\bigl(\operatorname{rot}(\varphi\boldsymbol{E})\bigr)_i=\sum_{j,k}\varepsilon_{ijk}\frac{\partial(\varphi E_k)}{\partial x_j}=\sum_{j,k}\varepsilon_{ijk}\frac{\partial\varphi}{\partial x_j}E_k+\varphi\sum_{j,k}\varepsilon_{ijk}\frac{\partial E_k}{\partial x_j}.$$

Die erste Summe ist nach [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6) die Komponente $i$ von $\nabla\varphi\times\boldsymbol{E}$, die zweite die von $\operatorname{rot}\boldsymbol{E}$.
:::

⁠**So liest man das:** Beide Formeln haben die Form „$\nabla$ trifft $\varphi$“ plus „$\nabla$ trifft $\boldsymbol{E}$“. Einmal dockt $\nabla$ als Skalarprodukt an, einmal als Kreuzprodukt.

::::beispiel
$\varphi=x$ und $\boldsymbol{E}=(0,0,y)$. Direkt: $\varphi\boldsymbol{E}=(0,0,xy)$ hat nach Unterabschnitt [3.12](divergenz-rotation-und-laplace-operator.html#stufe-3-12) die Rotation $(x,-y,0)$. Mit der Regel: $\nabla\varphi\times\boldsymbol{E}=(1,0,0)\times(0,0,y)=(0,-y,0)$ und $\varphi\,\operatorname{rot}\boldsymbol{E}=x\,(1,0,0)$, zusammen $(x,-y,0)$.
::::

⁠**Kurz gesagt:** Divergenz und Rotation von $\varphi\boldsymbol{E}$ zerfallen in einen Teil, in dem $\varphi$ abgeleitet wird, und einen, in dem $\boldsymbol{E}$ abgeleitet wird.

### Die Produktregel der Rotation in der Ebene

<span class="anker" id="stufe-4-6"></span>

Die zweite Formel aus [(4.4)](#gl-4-4) lässt sich auch in der Ebene benutzen. Dort ist die Rotation eine Zahl, und an die Stelle des Kreuzprodukts tritt eine Zahl aus zwei ebenen Vektoren.

Für $\boldsymbol a,\boldsymbol b\in\mathbb{R}^2$ heißt die Zahl $a_1b_2-a_2b_1$ das __äußere Produkt__ von $\boldsymbol a$ und $\boldsymbol b$. Sie ist die dritte Komponente von $(a_1,a_2,0)\times(b_1,b_2,0)$ und der orientierte Flächeninhalt des Parallelogramms aus $\boldsymbol a$ und $\boldsymbol b$. Damit gilt für ein Feld $\boldsymbol{E}=(E_1,E_2)$ in der Ebene

$$\operatorname{rot}(\varphi\boldsymbol{E})=\Bigl(\frac{\partial\varphi}{\partial x_1}E_2-\frac{\partial\varphi}{\partial x_2}E_1\Bigr)+\varphi\,\operatorname{rot}\boldsymbol{E} .$$

Man erhält die Formel, wenn man in [(4.4)](#gl-4-4) $\boldsymbol{E}=(E_1,E_2,0)$ einsetzt, mit $\varphi$ und $\boldsymbol{E}$ unabhängig von $x_3$, und die dritte Komponente nimmt.

::::beispiel
$\varphi=x$ und $\boldsymbol{E}=(y,x)$. Direkt: $\operatorname{rot}(xy,\;x^2)=2x-x=x$. Mit der Regel: $(1\cdot x-0\cdot y)+x\cdot(1-1)=x$.
::::

⁠**Kurz gesagt:** In der Ebene ersetzt das äußere Produkt $a_1b_2-a_2b_1$ das Kreuzprodukt in der Produktregel der Rotation.

### Die Ableitung eines Felds in Richtung eines anderen Felds

<span class="anker" id="stufe-4-7"></span>

In der Produktregel für die Rotation eines Kreuzprodukts tritt ein neuer Ausdruck auf: Ein Feld wird in der Richtung abgeleitet, in die ein anderes Feld zeigt.

Man stellt sich vor, man bewegt sich mit der Geschwindigkeit $\boldsymbol{E}(\boldsymbol{x})$ durch das Feld $\boldsymbol B$. Wie schnell ändert sich das Feld $\boldsymbol B$, das man dabei vorfindet? Nach [(1.10)](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#gl-1-10), für jede Komponente von $\boldsymbol B$ einzeln, ist das $\sum_jE_j\,\partial\boldsymbol B/\partial x_j$.

:::definition Definition 4.2 (Ableitung in Richtung eines Felds)
<span class="anker" id="satz-4-2"></span>

Für Vektorfelder $\boldsymbol{E}$ und $\boldsymbol B$ auf einer offenen Menge des $\mathbb{R}^3$ sei

<span class="anker" id="gl-4-5"></span>
$$(\boldsymbol{E}\cdot\nabla)\boldsymbol B=\sum_{j=1}^3E_j\,\frac{\partial\boldsymbol B}{\partial x_j},\qquad\text{wobei}\qquad\frac{\partial\boldsymbol B}{\partial x_j}=\Bigl(\frac{\partial B_1}{\partial x_j},\frac{\partial B_2}{\partial x_j},\frac{\partial B_3}{\partial x_j}\Bigr)^T . \tag{4.5}$$
:::

⁠**So liest man das:** $\boldsymbol{E}\cdot\nabla=\sum_jE_j\,\partial/\partial x_j$ ist ein Ableitungsbefehl, er wird auf jede Komponente von $\boldsymbol B$ angewendet. Das Ergebnis ist ein Vektorfeld. In Matrixform ist $(\boldsymbol{E}\cdot\nabla)\boldsymbol B=D\boldsymbol B\,\boldsymbol{E}$. Ist $\boldsymbol{E}$ an einem Punkt ein Einheitsvektor, ist das die Richtungsableitung von $\boldsymbol B$ in diese Richtung. Es ist etwas völlig anderes als $\boldsymbol{E}\,\operatorname{div}\boldsymbol B$, das Feld $\boldsymbol{E}$ mal die Zahl $\operatorname{div}\boldsymbol B$.

::::beispiel
$\boldsymbol{E}=(x,y,0)$ und $\boldsymbol B=(xy,0,0)$. Es ist $\partial\boldsymbol B/\partial x=(y,0,0)$, $\partial\boldsymbol B/\partial y=(x,0,0)$ und $\partial\boldsymbol B/\partial z=0$, also $(\boldsymbol{E}\cdot\nabla)\boldsymbol B=x(y,0,0)+y(x,0,0)=(2xy,0,0)$. Dagegen ist $\operatorname{div}\boldsymbol B=y$ und $\boldsymbol{E}\,\operatorname{div}\boldsymbol B=(xy,\,y^2,\,0)$.
::::

⁠**Kurz gesagt:** $(\boldsymbol{E}\cdot\nabla)\boldsymbol B$ ist die Änderung von $\boldsymbol B$, wenn man sich mit der Geschwindigkeit $\boldsymbol{E}$ bewegt.

### Produktregeln mit dem Kreuzprodukt

<span class="anker" id="stufe-4-8"></span>

Wie sehen Divergenz und Rotation des Kreuzprodukts zweier Felder aus? Auch hier wird jeder Faktor einmal abgeleitet, und danach sortiert eine Vektoridentität die Terme.

:::satz Satz 4.3 (Produktregeln mit Kreuzprodukt)
<span class="anker" id="satz-4-3"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen, und seien $\boldsymbol{E}=(E_1,E_2,E_3)$ und $\boldsymbol B=(B_1,B_2,B_3)$ differenzierbare Vektorfelder auf $\mathcal U$. Dann gilt

<span class="anker" id="gl-4-6"></span>
<span class="anker" id="gl-4-7"></span>
$$\begin{aligned} \operatorname{div}(\boldsymbol{E}\times\boldsymbol B)&=\boldsymbol B\cdot\operatorname{rot}\boldsymbol{E}-\boldsymbol{E}\cdot\operatorname{rot}\boldsymbol B,\\ \operatorname{rot}(\boldsymbol{E}\times\boldsymbol B)&=\boldsymbol{E}\,\operatorname{div}\boldsymbol B-\boldsymbol B\,\operatorname{div}\boldsymbol{E}+(\boldsymbol B\cdot\nabla)\boldsymbol{E}-(\boldsymbol{E}\cdot\nabla)\boldsymbol B . \end{aligned} \tag{4.6|4.7}$$
:::

⁠**So liest man das:** Beide Formeln folgen aus der Darstellung von Kreuzprodukt und Rotation mit Levi-Civita-Symbolen und der Produktregel. Für die zweite braucht man zusätzlich die Graßmann-Identität in Indizes [(4.3)](#gl-4-3). In [(4.6)](#gl-4-6) wird jeder Faktor einmal abgeleitet: Der Summand mit $\operatorname{rot}\boldsymbol{E}$ enthält die Ableitungen von $\boldsymbol{E}$, der mit $\operatorname{rot}\boldsymbol B$ die von $\boldsymbol B$. Das Minuszeichen kommt daher, dass das Kreuzprodukt beim Vertauschen der Faktoren sein Vorzeichen wechselt.

::::beispiel
$\boldsymbol{E}=(y,0,0)$ und $\boldsymbol B=(0,0,x)$. Es ist $\boldsymbol{E}\times\boldsymbol B=(0,\,-xy,\,0)$ und $\operatorname{div}(\boldsymbol{E}\times\boldsymbol B)=-x$. Rechts: $\operatorname{rot}\boldsymbol{E}=(0,0,-1)$ und $\operatorname{rot}\boldsymbol B=(0,-1,0)$, also $\boldsymbol B\cdot\operatorname{rot}\boldsymbol{E}-\boldsymbol{E}\cdot\operatorname{rot}\boldsymbol B=-x-0=-x$.
::::

:::hintergrund Warum man $\nabla$ nicht einfach in Vektorformeln einsetzen darf
Weil $\nabla$ alles rechts von ihm ableitet. Wendet man auf $\nabla\cdot(\boldsymbol{E}\times\boldsymbol B)$ das zyklische Vertauschen des Spatprodukts an, als wäre $\nabla$ ein Vektor, entsteht $\boldsymbol B\cdot(\nabla\times\boldsymbol{E})$. Dann fehlt der zweite Summand von [(4.6)](#gl-4-6), denn $\boldsymbol B$ steht nicht mehr rechts von $\nabla$ und würde gar nicht abgeleitet. Vektoridentitäten gelten für $\nabla$ nur, wenn man vorher mit der Produktregel dafür sorgt, dass jeder Faktor genau einmal abgeleitet wird, und wenn das abgeleitete Feld danach rechts von $\nabla$ steht.
:::

⁠**Kurz gesagt:** Divergenz und Rotation eines Kreuzprodukts entstehen aus Produktregel plus Vektoridentität; jeder Faktor wird einmal abgeleitet.

### Rotationsfelder sind divergenzfrei

<span class="anker" id="stufe-4-9"></span>

Nach Satz [3.11](divergenz-rotation-und-laplace-operator.html#satz-3-11) hat ein Gradient keine Rotation. Hat umgekehrt eine Rotation eine Divergenz? Auch hier treffen zwei Ableitungen aufeinander, und wieder ergibt sich null (Abb. [15](#abb-15)).

:::abbildung hm3/k1operatoren 15
Zwei Operatoren hintereinander. Oben: Ein Gradient hat keine Rotation. Unten: Eine Rotation hat keine Divergenz. Beide Nullen stammen aus der Vertauschbarkeit zweiter Ableitungen.
:::

Ein Feld mit $\operatorname{div}\boldsymbol{F}=0$ heißt __divergenzfrei__.

:::satz Satz 4.4 (Divergenz der Rotation)
<span class="anker" id="satz-4-4"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen und $\boldsymbol{E}$ ein zweimal stetig differenzierbares Vektorfeld auf $\mathcal U$. Dann gilt

<span class="anker" id="gl-4-8"></span>
$$\operatorname{div}\operatorname{rot}\boldsymbol{E}=0 . \tag{4.8}$$
:::

:::beweis Schiefsymmetrie trifft Symmetrie
Mit [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6) ist

$$\operatorname{div}\operatorname{rot}\boldsymbol{E}=\sum_{i=1}^3\frac{\partial}{\partial x_i}(\operatorname{rot}\boldsymbol{E})_i=\sum_{i,j,k}\varepsilon_{ijk}\frac{\partial^2E_k}{\partial x_i\,\partial x_j} =\sum_k\Bigl(\sum_{i<j}\varepsilon_{ijk}\frac{\partial^2E_k}{\partial x_i\,\partial x_j}+\sum_{i>j}\varepsilon_{ijk}\frac{\partial^2E_k}{\partial x_i\,\partial x_j}\Bigr).$$

Die Summanden mit $i=j$ fehlen, weil dort $\varepsilon_{ijk}=0$ ist. Benennt man in der zweiten inneren Summe $i$ und $j$ um, wird sie zu $\sum_{j<i}\dots=\sum_{i<j}\varepsilon_{jik}\frac{\partial^2E_k}{\partial x_j\,\partial x_i}$. Nach dem Lemma von Schwarz ist $\frac{\partial^2E_k}{\partial x_j\,\partial x_i}=\frac{\partial^2E_k}{\partial x_i\,\partial x_j}$, und es ist $\varepsilon_{jik}=-\varepsilon_{ijk}$. Also ist die zweite innere Summe das Negative der ersten, und beide heben sich weg.
:::

⁠**So liest man das:** Die Rotation eines zweimal stetig differenzierbaren Felds ist divergenzfrei. Der Mechanismus ist derselbe wie bei $\operatorname{rot}\nabla\varphi=0$: Das Levi-Civita-Symbol wechselt beim Vertauschen zweier Indizes das Vorzeichen, die zweite Ableitung nicht. Was schiefsymmetrisch gegen symmetrisch summiert wird, ergibt null.

::::beispiel
$\boldsymbol{E}=(0,0,x^2y)$ hat $\operatorname{rot}\boldsymbol{E}=(x^2,\,-2xy,\,0)$ und $\operatorname{div}\operatorname{rot}\boldsymbol{E}=2x-2x=0$.
::::

⁠**Kurz gesagt:** Die Divergenz einer Rotation ist null, weil die Levi-Civita-Symbole schiefsymmetrisch und die zweiten Ableitungen symmetrisch sind.

### Die doppelte Rotation

<span class="anker" id="stufe-4-10"></span>

Wendet man die Rotation zweimal an, entsteht kein neuer Operator. Das Ergebnis lässt sich aus Gradient, Divergenz und Laplace-Operator zusammensetzen.

:::satz Satz 4.5 (Rotation der Rotation)
<span class="anker" id="satz-4-5"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen und $\boldsymbol{E}$ ein zweimal stetig differenzierbares Vektorfeld auf $\mathcal U$. Dann gilt

<span class="anker" id="gl-4-9"></span>
$$\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E} . \tag{4.9}$$
:::

:::beweis Graßmann in Indizes
Mit [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6) zweimal und dem Lemma von Schwarz ist

$$(\operatorname{rot}\operatorname{rot}\boldsymbol{E})_i=\sum_{j,k}\varepsilon_{ijk}\frac{\partial}{\partial x_j}(\operatorname{rot}\boldsymbol{E})_k=\sum_{j,k,l,m}\varepsilon_{ijk}\,\varepsilon_{klm}\,\frac{\partial^2E_m}{\partial x_j\,\partial x_l}.$$

Nach [(4.3)](#gl-4-3) ist $\sum_k\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$. Die Kronecker-Symbole wählen Summanden aus:

$$(\operatorname{rot}\operatorname{rot}\boldsymbol{E})_i=\sum_j\frac{\partial^2E_j}{\partial x_j\,\partial x_i}-\sum_j\frac{\partial^2E_i}{\partial x_j^2}=\frac{\partial}{\partial x_i}\Bigl(\sum_j\frac{\partial E_j}{\partial x_j}\Bigr)-\Delta E_i=(\nabla\operatorname{div}\boldsymbol{E})_i-(\Delta\boldsymbol{E})_i .$$

Kompakt ist das die Graßmann-Identität mit $\boldsymbol a=\boldsymbol b=\nabla$ und $\boldsymbol c=\boldsymbol{E}$, achtsam angewendet:

$$\nabla\times(\nabla\times\boldsymbol{E})=\nabla(\nabla\cdot\boldsymbol{E})-(\nabla\cdot\nabla)\boldsymbol{E},\qquad\nabla\cdot\nabla=\Delta .$$

Das abgeleitete Feld steht dabei immer an letzter Stelle.
:::

⁠**So liest man das:** Der Laplace-Operator wirkt hier komponentenweise auf das Vektorfeld (Unterabschnitt [3.7](divergenz-rotation-und-laplace-operator.html#stufe-3-7)). Für ein divergenzfreies Feld bleibt $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=-\Delta\boldsymbol{E}$.

::::beispiel
$\boldsymbol{E}=(y^2,0,0)$. Es ist $\operatorname{rot}\boldsymbol{E}=(0,0,-2y)$ und $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=(-2,0,0)$. Rechts: $\operatorname{div}\boldsymbol{E}=0$ und $\Delta\boldsymbol{E}=(2,0,0)$, also $0-(2,0,0)=(-2,0,0)$.
::::

⁠**Kurz gesagt:** $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E}$: die Graßmann-Identität mit $\nabla$, das Feld immer an letzter Stelle.

### Wirbelfelder und Vektorpotentiale

<span class="anker" id="stufe-4-11"></span>

Ein Gradientenfeld ist durch eine einzige Funktion, sein Skalarpotential, festgelegt. Ähnlich kann ein Feld die Rotation eines anderen Felds sein. Das magnetische Feld ist das wichtigste Beispiel.

:::definition Definition 4.6 (Wirbelfeld und Vektorpotential)
<span class="anker" id="satz-4-6"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen. Ein Vektorfeld $\boldsymbol B\colon\mathcal U\to\mathbb{R}^3$ heißt __Wirbelfeld__ oder Rotationsfeld, wenn es ein differenzierbares Vektorfeld $\boldsymbol{A}$ auf $\mathcal U$ gibt mit

$$\boldsymbol B=\operatorname{rot}\boldsymbol{A} .$$

Jedes solche Feld $\boldsymbol{A}$ heißt ein __Vektorpotential__ von $\boldsymbol B$.
:::

Nach Satz [4.4](#satz-4-4) ist jedes Wirbelfeld $\boldsymbol B=\nabla\times\boldsymbol{A}$ mit zweimal stetig differenzierbarem Vektorpotential $\boldsymbol{A}$ divergenzfrei. Wie beim Gradienten fragt man nach der Umkehrung: Hat jedes divergenzfreie Feld ein Vektorpotential? Auch diese Frage ist im Allgemeinen mit nein zu beantworten, und wie beim Skalarpotential (Unterabschnitt [3.19](divergenz-rotation-und-laplace-operator.html#stufe-3-19)) hängt die Antwort von der Menge ab, auf der das Feld erklärt ist.

|  | Skalarpotential | Vektorpotential |
|---|---|---|
| Frage | $\boldsymbol{E}=\nabla\varphi$? | $\boldsymbol B=\operatorname{rot}\boldsymbol{A}$? |
| notwendige Bedingung | $\operatorname{rot}\boldsymbol{E}=0$ (Satz [3.11](divergenz-rotation-und-laplace-operator.html#satz-3-11)) | $\operatorname{div}\boldsymbol B=0$ (Satz [4.4](#satz-4-4)) |
| hinreichend? | nicht auf jeder Menge | nicht auf jeder Menge |

::::beispiel
$\boldsymbol B=(0,0,2)$ ist ein Wirbelfeld mit dem Vektorpotential $\boldsymbol{A}=(-y,x,0)$, denn $\operatorname{rot}(-y,x,0)=(0,0,2)$ (Unterabschnitt [3.14](divergenz-rotation-und-laplace-operator.html#stufe-3-14)). Es ist divergenzfrei, wie es sein muss.
::::

⁠**Kurz gesagt:** Ein Wirbelfeld ist die Rotation eines Vektorpotentials. Es ist dann divergenzfrei.

### Eichfreiheit

<span class="anker" id="stufe-4-12"></span>

Potentiale sind nicht eindeutig. Wie viel Freiheit bleibt, ist beim Vektorpotential viel größer als beim Skalarpotential.

Zu einem Skalarpotential $\varphi$ darf man jede Konstante addieren, denn ihr Gradient ist null. Zu einem Vektorpotential $\boldsymbol{A}$ darf man sogar jedes Gradientenfeld $\nabla\psi$ mit zweimal stetig differenzierbarem $\psi$ addieren:

$$\operatorname{rot}(\boldsymbol{A}+\nabla\psi)=\operatorname{rot}\boldsymbol{A}+\operatorname{rot}\nabla\psi=\operatorname{rot}\boldsymbol{A} ,$$

denn $\operatorname{rot}\nabla\psi=0$ nach Satz [3.11](divergenz-rotation-und-laplace-operator.html#satz-3-11). Diese Freiheit, ein Potential zu ändern, ohne das Feld zu ändern, heißt __Eichfreiheit__.

::::beispiel
Das Feld $\boldsymbol B=(0,0,2)$ hat die Vektorpotentiale $(-y,x,0)$ und $(0,2x,0)$; beide haben die Rotation $(0,0,2)$. Ihre Differenz ist $(-y,-x,0)=\nabla(-xy)$, ein Gradientenfeld.
::::

:::hintergrund Warum man die Freiheit begrüßt
Messen kann man nur das Feld, nicht sein Potential. Alle Potentiale, die dasselbe Feld liefern, beschreiben deshalb dieselbe Physik. Die Freiheit lässt sich ausnutzen: Man wählt unter allen Potentialen dasjenige, mit dem die Rechnung am einfachsten wird. Beim Skalarpotential legt man meist den Nullpunkt fest, etwa „$u=0$ im Unendlichen“. Beim Vektorpotential kann man eine ganze Funktion $\psi$ wählen und damit eine zusätzliche Bedingung an $\boldsymbol{A}$ erzwingen. Das heißt Eichen.
:::

⁠**Kurz gesagt:** Ein Skalarpotential ist bis auf eine Konstante bestimmt, ein Vektorpotential bis auf ein Gradientenfeld.

### Die Coulomb-Eichung

<span class="anker" id="stufe-4-13"></span>

Mit der Eichfreiheit kann man ein Vektorpotential so wählen, dass es selbst divergenzfrei ist. Diese Wahl vereinfacht die doppelte Rotation.

Eine Gleichung für eine unbekannte Funktion, in der partielle Ableitungen dieser Funktion vorkommen, heißt __partielle Differentialgleichung__. Ein Beispiel ist $\Delta\psi=h$ für eine gegebene Funktion $h$ und eine gesuchte Funktion $\psi$.

:::definition Definition 4.7 (Coulomb-Eichung)
<span class="anker" id="satz-4-7"></span>

Ein Vektorpotential $\boldsymbol{A}$ von $\boldsymbol B$ ist in __Coulomb-Eichung__, wenn

<span class="anker" id="gl-4-10"></span>
$$\boldsymbol B=\nabla\times\boldsymbol{A}\qquad\text{und}\qquad\operatorname{div}\boldsymbol{A}=0 . \tag{4.10}$$
:::

⁠**Wie man sie erreicht:** Ist $\boldsymbol{A}$ ein Vektorpotential von $\boldsymbol B$ mit $\operatorname{div}\boldsymbol{A}\neq0$ und $\psi$ eine Lösung der partiellen Differentialgleichung

$$\Delta\psi=\operatorname{div}\boldsymbol{A} ,$$

dann ist $\boldsymbol{A}'=\boldsymbol{A}-\nabla\psi$ ein Vektorpotential von $\boldsymbol B$ in Coulomb-Eichung. Denn nach der Eichfreiheit ist $\operatorname{rot}\boldsymbol{A}'=\operatorname{rot}\boldsymbol{A}=\boldsymbol B$, und $\operatorname{div}\boldsymbol{A}'=\operatorname{div}\boldsymbol{A}-\operatorname{div}\nabla\psi=\operatorname{div}\boldsymbol{A}-\Delta\psi=0$. In diesem Fall wird [(4.9)](#gl-4-9) einfach:

$$\operatorname{rot}\boldsymbol B=\operatorname{rot}\operatorname{rot}\boldsymbol{A}'=\nabla\underbrace{\operatorname{div}\boldsymbol{A}'}_{=0}-\Delta\boldsymbol{A}'=-\Delta\boldsymbol{A}' .$$

:::hintergrund Was die Coulomb-Eichung gewinnt
Ohne Eichung koppelt $\operatorname{rot}\operatorname{rot}\boldsymbol{A}$ die drei Komponenten von $\boldsymbol{A}$ miteinander: In $\nabla\operatorname{div}\boldsymbol{A}$ steckt in jeder Komponente die Divergenz, also alle drei Komponenten. In Coulomb-Eichung fällt dieser Teil weg, und $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}'$ zerfällt in drei getrennte Gleichungen $-\Delta A'_i=(\operatorname{rot}\boldsymbol B)_i$, je eine für jede Komponente. Jede davon hat dieselbe Form wie die Gleichung $-\Delta u=\operatorname{div}\boldsymbol{E}$, die nach Unterabschnitt [3.11](divergenz-rotation-und-laplace-operator.html#stufe-3-11) ein Potential $u$ mit der Quellendichte seines Felds $\boldsymbol{E}=-\nabla u$ verbindet. Statt eines gekoppelten Systems löst man dreimal dieselbe Art von Gleichung für eine einzige skalare Funktion.
:::

::::beispiel
$\boldsymbol{A}=(x,\,2x,\,0)$ hat $\operatorname{rot}\boldsymbol{A}=(0,0,2)$ und $\operatorname{div}\boldsymbol{A}=1$. Die Funktion $\psi=x^2/2$ löst $\Delta\psi=1$. Dann ist $\boldsymbol{A}'=\boldsymbol{A}-\nabla\psi=(x,2x,0)-(x,0,0)=(0,\,2x,\,0)$. Es ist $\operatorname{div}\boldsymbol{A}'=0$ und $\operatorname{rot}\boldsymbol{A}'=(0,0,2)$, wie verlangt.
::::

⁠**Kurz gesagt:** In Coulomb-Eichung ist $\operatorname{div}\boldsymbol{A}=0$; man erreicht sie mit einer Lösung von $\Delta\psi=\operatorname{div}\boldsymbol{A}$, und dann gilt $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}$.

### Aufgaben

<span class="anker" id="stufe-4-14"></span>

:::aufgabe Aufgabe 12 ★★★ Produktregeln beweisen
<span class="anker" id="aufg-12"></span>

Beweise [(4.6)](#gl-4-6) und [(4.7)](#gl-4-7). Tipp: Nach [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6) ist $(\boldsymbol{E}\times\boldsymbol B)_k=\sum_{l,m}\varepsilon_{klm}E_lB_m$. Für [(4.6)](#gl-4-6) ordne die Summe mit $\varepsilon_{klm}=\varepsilon_{mkl}=-\varepsilon_{lkm}$ um, für [(4.7)](#gl-4-7) benutze [(4.3)](#gl-4-3).

:::loesung
⁠*Erste Formel.* Mit $(\boldsymbol{E}\times\boldsymbol B)_k=\sum_{l,m}\varepsilon_{klm}E_lB_m$ und der Produktregel:

$$\operatorname{div}(\boldsymbol{E}\times\boldsymbol B)=\sum_{k,l,m}\varepsilon_{klm}\frac{\partial(E_lB_m)}{\partial x_k}=\sum_{k,l,m}\varepsilon_{klm}\frac{\partial E_l}{\partial x_k}B_m+\sum_{k,l,m}\varepsilon_{klm}E_l\frac{\partial B_m}{\partial x_k}.$$

Wegen $\varepsilon_{klm}=\varepsilon_{mkl}$ ist die erste Summe $\sum_mB_m\sum_{k,l}\varepsilon_{mkl}\frac{\partial E_l}{\partial x_k}=\sum_mB_m(\operatorname{rot}\boldsymbol{E})_m=\boldsymbol B\cdot\operatorname{rot}\boldsymbol{E}$. Wegen $\varepsilon_{klm}=-\varepsilon_{lkm}$ ist die zweite $-\sum_lE_l\sum_{k,m}\varepsilon_{lkm}\frac{\partial B_m}{\partial x_k}=-\boldsymbol{E}\cdot\operatorname{rot}\boldsymbol B$.

⁠*Zweite Formel.* Mit [(3.6)](divergenz-rotation-und-laplace-operator.html#gl-3-6) zweimal und [(4.3)](#gl-4-3):

$$\begin{aligned} \bigl(\operatorname{rot}(\boldsymbol{E}\times\boldsymbol B)\bigr)_i&=\sum_{j,k}\varepsilon_{ijk}\frac{\partial}{\partial x_j}\sum_{l,m}\varepsilon_{klm}E_lB_m=\sum_{j,l,m}(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})\frac{\partial(E_lB_m)}{\partial x_j}\\ &=\sum_j\frac{\partial(E_iB_j)}{\partial x_j}-\sum_j\frac{\partial(E_jB_i)}{\partial x_j}. \end{aligned}$$

Mit der Produktregel ist $\sum_j\partial_{x_j}(E_iB_j)=E_i\,\operatorname{div}\boldsymbol B+\sum_jB_j\,\partial_{x_j}E_i=E_i\,\operatorname{div}\boldsymbol B+\bigl((\boldsymbol B\cdot\nabla)\boldsymbol{E}\bigr)_i$ und ebenso $\sum_j\partial_{x_j}(E_jB_i)=B_i\,\operatorname{div}\boldsymbol{E}+\bigl((\boldsymbol{E}\cdot\nabla)\boldsymbol B\bigr)_i$. Die Differenz ist die Komponente $i$ von [(4.7)](#gl-4-7).
:::
:::

:::aufgabe Aufgabe 13 ★★ Identitäten anwenden
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

Zeige $\operatorname{rot}\bigl(f(r)\,\boldsymbol{x}\bigr)=0$ auf $\mathbb{R}^3\setminus\{0\}$ für eine stetig differenzierbare Funktion $f\colon(0,\infty)\to\mathbb{R}$.

</li>

<li>

Zeige $\operatorname{div}(\nabla f\times\nabla g)=0$ für zweimal stetig differenzierbare Funktionen $f,g$ auf $\mathbb{R}^3$.

</li>

<li>

Zeige $\Delta(\nabla f)=\nabla(\Delta f)$ für eine dreimal stetig differenzierbare Funktion $f$ auf $\mathbb{R}^3$.

</li>

</ol>

:::loesung
(a) Nach [(4.4)](#gl-4-4) und [(2.2)](radialsymmetrische-funktionen-und-felder.html#gl-2-2) ist $\operatorname{rot}\bigl(f(r)\boldsymbol{x}\bigr)=\nabla f(r)\times\boldsymbol{x}+f(r)\,\operatorname{rot}\boldsymbol{x}=f'(r)\,\hat{\boldsymbol{e}}_r\times\boldsymbol{x}+f(r)\,\operatorname{rot}\boldsymbol{x}$. Der erste Summand ist null, weil $\hat{\boldsymbol{e}}_r$ und $\boldsymbol{x}$ parallel sind. Der zweite ist null, weil $\boldsymbol{x}=\nabla(r^2/2)$ ein Gradientenfeld ist und Satz [3.11](divergenz-rotation-und-laplace-operator.html#satz-3-11) gilt.

(b) Nach [(4.6)](#gl-4-6) mit $\boldsymbol{E}=\nabla f$ und $\boldsymbol B=\nabla g$ ist $\operatorname{div}(\nabla f\times\nabla g)=\nabla g\cdot\operatorname{rot}\nabla f-\nabla f\cdot\operatorname{rot}\nabla g=0$, denn beide Rotationen sind nach Satz [3.11](divergenz-rotation-und-laplace-operator.html#satz-3-11) null.

(c) Komponente $k$: $\Delta\Bigl(\frac{\partial f}{\partial x_k}\Bigr)=\sum_j\frac{\partial^2}{\partial x_j^2}\frac{\partial f}{\partial x_k}=\frac{\partial}{\partial x_k}\sum_j\frac{\partial^2f}{\partial x_j^2}=\frac{\partial}{\partial x_k}\Delta f$. Die Vertauschung der Reihenfolge erlaubt das Lemma von Schwarz, weil $f\in C^3$ ist. Alternativ folgt es aus [(4.9)](#gl-4-9) mit $\boldsymbol{E}=\nabla f$: $0=\operatorname{rot}\operatorname{rot}\nabla f=\nabla\operatorname{div}\nabla f-\Delta\nabla f=\nabla\Delta f-\Delta\nabla f$.
:::
:::

:::aufgabe Aufgabe 14 ★★ Coulomb-Eichung
<span class="anker" id="aufg-14"></span>

Sei $\boldsymbol{A}=(x,\;x^3,\;0)$. Berechne $\boldsymbol B=\operatorname{rot}\boldsymbol{A}$ und $\operatorname{div}\boldsymbol{A}$. Finde eine Funktion $\psi$, die nur von $x$ abhängt, mit $\Delta\psi=\operatorname{div}\boldsymbol{A}$. Bilde $\boldsymbol{A}'=\boldsymbol{A}-\nabla\psi$ und prüfe $\operatorname{rot}\boldsymbol{A}'=\boldsymbol B$, $\operatorname{div}\boldsymbol{A}'=0$ und $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}'$.

:::loesung
$\boldsymbol B=\operatorname{rot}\boldsymbol{A}=\bigl(0-0,\;0-0,\;3x^2-0\bigr)=(0,\,0,\,3x^2)$ und $\operatorname{div}\boldsymbol{A}=1+0+0=1$. Gesucht ist $\psi(x)$ mit $\psi''(x)=1$, zum Beispiel $\psi=x^2/2$. Dann ist $\nabla\psi=(x,0,0)$ und $\boldsymbol{A}'=(x,x^3,0)-(x,0,0)=(0,\,x^3,\,0)$. Es ist $\operatorname{rot}\boldsymbol{A}'=(0,0,3x^2)=\boldsymbol B$ und $\operatorname{div}\boldsymbol{A}'=0$. Weiter ist $\operatorname{rot}\boldsymbol B=\bigl(0,\;-6x,\;0\bigr)$ und $\Delta\boldsymbol{A}'=(0,\,6x,\,0)$, also $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}'$.
:::
:::
