---
title: Das Matrixprodukt
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
knoten: Grundlagen 1: Vektoren und Matrizen
nachschlagen: ja
order: 15211000
summary: Zwei lineare Abbildungen hintereinander ergeben wieder eine lineare Abbildung, also eine Matrix.
tags: Matrixprodukt, äußere Produkt
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Zwei lineare Abbildungen hintereinander ergeben wieder eine lineare Abbildung, also eine Matrix. Dieser Abschnitt bestimmt sie. Das Ergebnis ist das Matrixprodukt, und seine Definition folgt zwingend aus dieser Aufgabe.
:::

### Das Matrixprodukt

<span class="anker" id="stufe-9-1"></span>

Zuerst wird ein Vektor $\mathbf{x}\in\mathbb{R}^k$ mit einer Matrix $\mathbf{B}\in\mathbb{R}^{n\times k}$ abgebildet, das Ergebnis $\mathbf{B}\mathbf{x}\in\mathbb{R}^n$ dann mit einer Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ (Abb. [33](#abb-33)). Die Hintereinanderausführung $\mathbf{x}\mapsto\mathbf{A}(\mathbf{B}\mathbf{x})$ ist linear, denn jede der beiden Stufen erhält Summen und Vielfache. Nach dem Satz in Unterabschnitt [8.2](lineare-abbildungen.html#stufe-8-2) hat sie also eine Matrix. Ihre Spalte $l$ ist das Bild von $\mathbf{e}_l$: Die erste Stufe macht daraus die Spalte $\mathbf{B}\mathbf{e}_l$ von $\mathbf{B}$, die zweite Stufe multipliziert diese mit $\mathbf{A}$.

:::abbildung ml/k1hinter 33
Oben zwei lineare Abbildungen hintereinander: erst $\mathbf{B}$, dann $\mathbf{A}$. Unten dieselbe Abbildung in einem Schritt, mit der einen Matrix $\mathbf{A}\mathbf{B}$. Das Matrixprodukt ist genau so definiert, dass beide Wege dasselbe Ergebnis liefern.
:::

:::definition Definition 9.1 (Matrixprodukt)
<span class="anker" id="satz-9-1"></span>

Für $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{B}\in\mathbb{R}^{n\times k}$ ist das __Matrixprodukt__ $\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times k}$ die Matrix mit den Einträgen

<span class="anker" id="gl-9-1"></span>
$$(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^{n}a_{ij}\,b_{jl},\qquad i=1,\dots,m,\quad l=1,\dots,k . \tag{9.1}$$
:::

Der Eintrag $(i,l)$ ist das Skalarprodukt der Zeile $i$ von $\mathbf{A}$ mit der Spalte $l$ von $\mathbf{B}$. Das Produkt ist nur erklärt, wenn $\mathbf{A}$ so viele Spalten hat wie $\mathbf{B}$ Zeilen: Die „inneren“ Formate müssen übereinstimmen, $(m\times n)\cdot(n\times k)$, und das Ergebnis hat die „äußeren“ Formate $m\times k$.

:::satz Satz 9.2 (Das Produkt ist die Hintereinanderausführung)
<span class="anker" id="satz-9-2"></span>

Für alle $\mathbf{x}\in\mathbb{R}^k$ gilt $(\mathbf{A}\mathbf{B})\,\mathbf{x}=\mathbf{A}\,(\mathbf{B}\mathbf{x})$.
:::

:::herleitung Hintereinanderausführung
Komponente $i$ der linken Seite ist nach [(7.1)](das-matrix-vektor-produkt.html#gl-7-1) und [(9.1)](#gl-9-1)

$$\sum_{l=1}^k(\mathbf{A}\mathbf{B})_{il}\,x_l=\sum_{l=1}^k\sum_{j=1}^na_{ij}\,b_{jl}\,x_l=\sum_{j=1}^na_{ij}\Bigl(\sum_{l=1}^kb_{jl}\,x_l\Bigr)=\sum_{j=1}^na_{ij}\,(\mathbf{B}\mathbf{x})_j ,$$

und das ist Komponente $i$ von $\mathbf{A}(\mathbf{B}\mathbf{x})$. Im mittleren Schritt wurden die beiden Summen vertauscht und $a_{ij}$ vor die innere Summe gezogen.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ und $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ ist

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$

Jeder der vier Einträge ist eine Summe nach [(9.1)](#gl-9-1) (Abb. [34](#abb-34)).

:::abbildung ml/k1rprodukt 34
Das Matrixprodukt Eintrag für Eintrag: Eintrag $(i,l)$ ist Zeile $i$ von $\mathbf{A}$ mal Spalte $l$ von $\mathbf{B}$.
:::

Probe mit $\mathbf{x}=(1,\,2)^{\top}$: $\mathbf{B}\mathbf{x}=(2,\,1)^{\top}$, dann $\mathbf{A}(\mathbf{B}\mathbf{x})=(4,\,1)^{\top}$; und direkt $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+2,\ 1+0)^{\top}=(4,\,1)^{\top}$.
::::

⁠**Kurz gesagt:** Das Matrixprodukt $\mathbf{A}\mathbf{B}$ ist die Matrix der Abbildung „erst $\mathbf{B}$, dann $\mathbf{A}$“; sein Eintrag $(i,l)$ ist Zeile $i$ von $\mathbf{A}$ mal Spalte $l$ von $\mathbf{B}$.

:::hintergrund Warum das Matrixprodukt gerade so definiert ist
Die Formel [(9.1)](#gl-9-1) sieht auf den ersten Blick willkürlich aus. Näher läge es, Matrizen Eintrag für Eintrag zu multiplizieren. Das Matrixprodukt ist aber keine freie Erfindung, sondern durch eine Forderung festgelegt: Es soll die Matrix der Hintereinanderausführung sein. Diese Matrix ist nach dem Satz in Unterabschnitt [8.2](lineare-abbildungen.html#stufe-8-2) eindeutig, und ihre Spalte $l$ muss das Bild von $\mathbf{e}_l$ unter beiden Abbildungen sein, also $\mathbf{A}$ mal Spalte $l$ von $\mathbf{B}$. Schreibt man das Komponente für Komponente aus, entsteht genau [(9.1)](#gl-9-1). Ein eintragsweises Produkt hätte keine solche Bedeutung: Es beschreibt keine Hintereinanderausführung zweier Abbildungen.
:::

### Viele Vektoren auf einmal

<span class="anker" id="stufe-9-2"></span>

Nach der Herleitung des Produkts ist die Spalte $l$ von $\mathbf{A}\mathbf{B}$ das Produkt von $\mathbf{A}$ mit der Spalte $l$ von $\mathbf{B}$. Man kann ein Matrixprodukt also als mehrere Matrix-Vektor-Produkte nebeneinander lesen:

<span class="anker" id="gl-9-2"></span>
$$\mathbf{A}\begin{pmatrix}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{B}\mathbf{e}_k\end{pmatrix}=\begin{pmatrix}\mathbf{A}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{A}\mathbf{B}\mathbf{e}_k\end{pmatrix}. \tag{9.2}$$

Ebenso ist die Zeile $i$ von $\mathbf{A}\mathbf{B}$ die Zeile $i$ von $\mathbf{A}$, multipliziert mit $\mathbf{B}$.

Für Daten heißt das: Will man mehrere gewichtete Summen auf alle Beispiele anwenden, schreibt man die Gewichtsvektoren als Spalten einer Matrix $\mathbf{W}$ nebeneinander. Das Produkt $\mathbf{X}\mathbf{W}$ enthält dann in Spalte $l$ die Vorhersagen mit dem $l$-ten Gewichtsvektor.

::::beispiel [Rechenbeispiel]
Neben dem Kaufpreis mit $\mathbf{w}=(3,\,10,\,-4)^{\top}$ (Tausend Euro) soll die Monatsmiete mit den Gewichten $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ (Euro) geschätzt werden. Mit $\mathbf{W}=\begin{pmatrix}\mathbf{w}&\mathbf{w}_{\mathrm M}\end{pmatrix}\in\mathbb{R}^{3\times2}$ ist

$$\mathbf{X}\mathbf{W}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3&12\\10&30\\-4&-8\end{pmatrix}=\begin{pmatrix}188&756\\126&502\\286&1152\\232&914\end{pmatrix}.$$

Zeile $i$ enthält beide Schätzungen für Wohnung $i$, Spalte $1$ alle Kaufpreise, Spalte $2$ alle Mieten.
::::

⁠**Kurz gesagt:** Die Spalten von $\mathbf{A}\mathbf{B}$ sind $\mathbf{A}$ mal die Spalten von $\mathbf{B}$; $\mathbf{X}\mathbf{W}$ wendet mehrere gewichtete Summen auf alle Beispiele zugleich an.

### Rechenregeln: Die Reihenfolge zählt

<span class="anker" id="stufe-9-3"></span>

Für Zahlen ist $2\cdot3=3\cdot2$. Für Matrizen gilt das nicht, und der Grund ist anschaulich: Erst drehen und dann strecken ist etwas anderes als erst strecken und dann drehen (Abb. [35](#abb-35)).

:::abbildung ml/k1reihenfolge 35
Das Einheitsquadrat mit $\mathbf{e}_1$ (rot) und $\mathbf{e}_2$ (grün), daneben seine Bilder unter $\mathbf{S}\mathbf R$ und $\mathbf R\mathbf{S}$. Dabei ist $\mathbf R$ die Drehung um $90^\circ$ und $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ die Streckung. Die Reihenfolge entscheidet, ob das Rechteck waagerecht oder senkrecht lang wird.
:::

:::satz Satz 9.3 (Rechenregeln des Matrixprodukts)
<span class="anker" id="satz-9-3"></span>

Für Matrizen passender Formate und Skalare $c$ gilt:

<ol class="rm">

<li>

$(\mathbf{A}\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\mathbf{C})$ (assoziativ);

</li>

<li>

$\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}$ und $(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}$ (distributiv);

</li>

<li>

$c\,(\mathbf{A}\mathbf{B})=(c\,\mathbf{A})\mathbf{B}=\mathbf{A}(c\,\mathbf{B})$.

</li>

</ol>

Im Allgemeinen ist aber $\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}$: Das Matrixprodukt ist *nicht* kommutativ.
:::

Regel (i) folgt aus der Bedeutung: Beide Seiten sind die Matrix der Abbildung „erst $\mathbf{C}$, dann $\mathbf{B}$, dann $\mathbf{A}$“, denn $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{x})=\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{x}))=\mathbf{A}((\mathbf{B}\mathbf{C})\mathbf{x})$ für jedes $\mathbf{x}$. Die Regeln (ii) und (iii) rechnet man mit [(9.1)](#gl-9-1) und den Summenregeln Eintrag für Eintrag nach.

::::beispiel [Rechenbeispiel 1]
Mit der Drehung $\mathbf R=\mathbf R_{90^\circ}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ und der Streckung $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ ist

$$\mathbf{S}\mathbf R=\begin{pmatrix}0&-2\\0{,}5&0\end{pmatrix},\qquad \mathbf R\mathbf{S}=\begin{pmatrix}0&-0{,}5\\2&0\end{pmatrix}.$$

Erst drehen, dann strecken schickt $\mathbf{e}_1$ nach $(0;\,0{,}5)^{\top}$, erst strecken, dann drehen nach $(0,\,2)^{\top}$.
::::

::::beispiel [Rechenbeispiel 2]
Aus Unterabschnitt [9.1](#stufe-9-1) ist $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$, aber $\mathbf{B}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$. Bei verschiedenen Formaten ist es noch deutlicher: Für $\mathbf{A}\in\mathbb{R}^{2\times3}$ und $\mathbf{B}\in\mathbb{R}^{3\times2}$ ist $\mathbf{A}\mathbf{B}$ eine $2\times2$-Matrix und $\mathbf{B}\mathbf{A}$ eine $3\times3$-Matrix.
::::

⁠**Kurz gesagt:** Beim Matrixprodukt darf man Klammern versetzen und ausmultiplizieren, aber nicht die Reihenfolge vertauschen.

:::hintergrund Warum die Klammerung Rechenzeit spart
Nach der Regel (i) ist $(\mathbf{A}\mathbf{B})\mathbf{x}=\mathbf{A}(\mathbf{B}\mathbf{x})$. Das Ergebnis ist gleich, der Aufwand nicht. Für zwei $n\times n$-Matrizen braucht das Produkt $\mathbf{A}\mathbf{B}$ für jeden der $n^2$ Einträge $n$ Multiplikationen und $n-1$ Additionen, zusammen etwa $2n^3$ Grundrechenarten; danach kostet $(\mathbf{A}\mathbf{B})\mathbf{x}$ noch etwa $2n^2$. Der Weg $\mathbf{A}(\mathbf{B}\mathbf{x})$ besteht aus zwei Matrix-Vektor-Produkten zu je etwa $2n^2$. Für $n=1000$ sind das rund $2\cdot10^9$ gegen $4\cdot10^6$ Grundrechenarten, ein Unterschied um den Faktor $500$. Wer eine lange Kette von Matrizen auf einen Vektor anwendet, rechnet deshalb von rechts nach links und bildet nie die Produktmatrix.
:::

### Zwei lineare Stufen sind eine

<span class="anker" id="stufe-9-4"></span>

Schaltet man mehrere lineare Rechenstufen hintereinander, so entsteht keine neue Art von Abbildung. Das ist nach Unterabschnitt [9.1](#stufe-9-1) klar, verdient aber einen eigenen Satz, weil es die Grenzen linearer Vorschriften markiert.

:::satz Satz 9.4 (Hintereinandergeschaltete lineare Abbildungen)
<span class="anker" id="satz-9-4"></span>

Sind $f(\mathbf{x})=\mathbf{B}\mathbf{x}$ und $g(\mathbf{u})=\mathbf{A}\mathbf{u}$ linear, so ist die Hintereinanderausführung $\mathbf{x}\mapsto g(f(\mathbf{x}))$ wieder linear, und zwar mit der einen Matrix $\mathbf{A}\mathbf{B}$. Dasselbe gilt für jede endliche Kette von linearen Stufen.
:::

Wie viele lineare Stufen man auch hintereinanderschaltet, das Ergebnis lässt sich immer mit einer einzigen Matrix in einem Schritt ausrechnen. Was eine Kette linearer Stufen kann, kann also schon eine einzelne Matrix. Aus Signale und Systeme kennt man dasselbe: Zwei lineare Systeme in Kette bilden zusammen wieder ein lineares System.

::::beispiel [Rechenbeispiel]
Eine erste Stufe macht aus drei Zahlen zwei, $\mathbf{B}=\bigl(\begin{smallmatrix}1&2&0\\0&1&-1\end{smallmatrix}\bigr)$, eine zweite aus zwei Zahlen wieder drei, $\mathbf{A}=\Bigl(\begin{smallmatrix}2&1\\1&-1\\0&3\end{smallmatrix}\Bigr)$. Zusammen ist das die eine Matrix

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&5&-1\\1&1&1\\0&3&-3\end{pmatrix}.$$

Probe mit $\mathbf{x}=(1,\,1,\,1)^{\top}$: $\mathbf{B}\mathbf{x}=(3,\,0)^{\top}$ und $\mathbf{A}(3,\,0)^{\top}=(6,\,3,\,0)^{\top}$; ebenso $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+5-1,\ 1+1+1,\ 0+3-3)^{\top}=(6,\,3,\,0)^{\top}$.
::::

⁠**Kurz gesagt:** Lineare Stufen hintereinander sind zusammen eine einzige lineare Abbildung, ihre Matrix ist das Produkt der einzelnen Matrizen.

### Das äußere Produkt

<span class="anker" id="stufe-9-5"></span>

Das Skalarprodukt $\mathbf{u}^{\top}\mathbf{v}$ ist „Zeile mal Spalte“ und ergibt eine Zahl. Dreht man die Reihenfolge um, „Spalte mal Zeile“, entsteht nach [(9.1)](#gl-9-1) eine ganze Matrix: die Tabelle aller Produkte je einer Komponente des einen mit einer Komponente des anderen Vektors, wie ein Einmaleins.

:::definition Definition 9.5 (Äußeres Produkt)
<span class="anker" id="satz-9-5"></span>

Für $\mathbf{u}\in\mathbb{R}^m$ und $\mathbf{v}\in\mathbb{R}^n$ ist das __äußere Produkt__ $\mathbf{u}\mathbf{v}^{\top}\in\mathbb{R}^{m\times n}$ die Matrix mit den Einträgen

<span class="anker" id="gl-9-3"></span>
$$(\mathbf{u}\mathbf{v}^{\top})_{ij}=u_i\,v_j . \tag{9.3}$$
:::

Es ist das Matrixprodukt einer $m\times1$-Matrix mit einer $1\times n$-Matrix. Jede Spalte ist ein Vielfaches von $\mathbf{u}$, nämlich $v_j\,\mathbf{u}$, und jede Zeile ein Vielfaches von $\mathbf{v}^{\top}$.

::::beispiel [Rechenbeispiel]
$$\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}4&5\end{pmatrix}=\begin{pmatrix}4&5\\8&10\\12&15\end{pmatrix}.$$
::::

Mit dem äußeren Produkt lässt sich jedes Matrixprodukt als Summe schreiben: „Spalte $j$ von $\mathbf{A}$ mal Zeile $j$ von $\mathbf{B}$“, summiert über $j$,

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}\mathbf{B}=\sum_{j=1}^n\mathbf{a}_j\,\bigl(\text{Zeile $j$ von }\mathbf{B}\bigr) . \tag{9.4}$$

Eintrag $(i,l)$ der rechten Seite ist $\sum_ja_{ij}\,b_{jl}$, genau wie in [(9.1)](#gl-9-1). Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ und $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ aus Unterabschnitt [9.1](#stufe-9-1) ergibt die Summe zweier äußerer Produkte wieder $\mathbf{A}\mathbf{B}$ (Abb. [36](#abb-36)).

:::abbildung ml/k1raeusser 36
Das Matrixprodukt als Summe äußerer Produkte: Spalte $j$ von $\mathbf{A}$ mal Zeile $j$ von $\mathbf{B}$, summiert über $j=1,2$.
:::

⁠**Kurz gesagt:** Das äußere Produkt $\mathbf{u}\mathbf{v}^{\top}$ ist die Tabelle aller Produkte $u_iv_j$; jedes Matrixprodukt ist eine Summe solcher Tabellen.

:::aufgabe Aufgabe 21 ★ Produkte und Formate
<span class="anker" id="aufg-21"></span>

<ol class="al">

<li>

Berechne $\mathbf{C}\mathbf{D}$ und $\mathbf{D}\mathbf{C}$ für $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ und $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$.

</li>

<li>

Es seien $\mathbf{A}\in\mathbb{R}^{2\times3}$, $\mathbf{B}\in\mathbb{R}^{3\times4}$ und $\mathbf{x}\in\mathbb{R}^4$. Welche der Ausdrücke $\mathbf{A}\mathbf{B}$, $\mathbf{B}\mathbf{A}$, $\mathbf{A}\mathbf{B}\mathbf{x}$, $\mathbf{B}\mathbf{x}\mathbf{A}$ sind erklärt, und welches Format hat das Ergebnis?

</li>

<li>

Berechne das äußere Produkt $(1,\,-1)^{\top}(2,\,0,\,3)$ und prüfe, dass jede Zeile ein Vielfaches von $(2,\,0,\,3)$ ist.

</li>

</ol>

:::loesung
(a) $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot1\\3\cdot0+4\cdot1&3\cdot1+4\cdot1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ und $\mathbf{D}\mathbf{C}=\bigl(\begin{smallmatrix}0+3&0+4\\1+3&2+4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$. Die beiden sind verschieden.

(b) $\mathbf{A}\mathbf{B}$: $(2\times3)\cdot(3\times4)$ passt, Format $2\times4$. $\mathbf{B}\mathbf{A}$: $(3\times4)\cdot(2\times3)$, innen $4\ne2$, nicht erklärt. $\mathbf{A}\mathbf{B}\mathbf{x}$: $(2\times4)\cdot(4\times1)$ passt, ein Vektor im $\mathbb{R}^2$. $\mathbf{B}\mathbf{x}\mathbf{A}$: $\mathbf{B}\mathbf{x}$ hat das Format $3\times1$, und $(3\times1)\cdot(2\times3)$ passt nicht, innen $1\ne2$; nicht erklärt.

(c) $(1,\,-1)^{\top}(2,\,0,\,3)=\bigl(\begin{smallmatrix}2&0&3\\-2&0&-3\end{smallmatrix}\bigr)$. Die erste Zeile ist $1\cdot(2,0,3)$, die zweite $-1\cdot(2,0,3)$.
:::
:::

:::aufgabe Aufgabe 22 ★★ Zwei Drehungen
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

Berechne $\mathbf R_\alpha\mathbf R_\beta$ mit [(8.3)](lineare-abbildungen.html#gl-8-3). Welche Drehung ist das? Welche zwei Formeln der Trigonometrie erhältst du nebenbei?

</li>

<li>

Berechne $\mathbf R_{90^\circ}^2=\mathbf R_{90^\circ}\mathbf R_{90^\circ}$ und $\mathbf R_{90^\circ}^4$ und deute die Ergebnisse geometrisch.

</li>

<li>

Ist $\mathbf R_\alpha\mathbf R_\beta=\mathbf R_\beta\mathbf R_\alpha$? Warum widerspricht das nicht der Regel, dass Matrizen nicht kommutieren?

</li>

</ol>

:::loesung
(a) Ausmultipliziert ist

$$\mathbf R_\alpha\mathbf R_\beta=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}.$$

Geometrisch ist das „erst um $\beta$ drehen, dann um $\alpha$“, also die Drehung um $\alpha+\beta$, deren Matrix nach [(8.3)](lineare-abbildungen.html#gl-8-3) $\mathbf R_{\alpha+\beta}$ ist. Vergleicht man die Einträge, erhält man die Additionstheoreme $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ und $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$. Das Matrixprodukt liefert sie, ohne dass man sie auswendig wissen muss.

(b) $\mathbf R_{90^\circ}^2=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-1&0\\0&-1\end{smallmatrix}\bigr)=-\mathbf{I}$: zweimal $90^\circ$ ist eine halbe Drehung, jeder Punkt geht in sein Spiegelbild am Nullpunkt über. $\mathbf R_{90^\circ}^4=(-\mathbf{I})(-\mathbf{I})=\mathbf{I}$: vier Vierteldrehungen sind eine volle Drehung.

(c) Ja: Beide Produkte sind $\mathbf R_{\alpha+\beta}=\mathbf R_{\beta+\alpha}$, denn Drehungen in der Ebene um denselben Punkt kann man in beliebiger Reihenfolge ausführen. „Nicht kommutativ“ heißt nur, dass $\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}$ *nicht immer* gilt. Für bestimmte Paare, etwa zwei Drehungen der Ebene oder zwei Diagonalmatrizen, kann es trotzdem gelten.
:::
:::

:::aufgabe Aufgabe 23 ★★ Die richtige Klammer
<span class="anker" id="aufg-23"></span>

Es seien $\mathbf{A}\in\mathbb{R}^{100\times1000}$, $\mathbf{B}\in\mathbb{R}^{1000\times1000}$ und $\mathbf{x}\in\mathbb{R}^{1000}$. Schätze die Zahl der Grundrechenarten für $(\mathbf{A}\mathbf{B})\mathbf{x}$ und für $\mathbf{A}(\mathbf{B}\mathbf{x})$ ab. Rechne dabei für ein Produkt einer $m\times n$-Matrix mit einer $n\times k$-Matrix etwa $2mnk$.

:::loesung
$(\mathbf{A}\mathbf{B})\mathbf{x}$: Das Produkt $\mathbf{A}\mathbf{B}$ einer $100\times1000$- mit einer $1000\times1000$-Matrix kostet etwa $2\cdot100\cdot1000\cdot1000=2\cdot10^8$, danach $(\mathbf{A}\mathbf{B})\mathbf{x}$ noch etwa $2\cdot100\cdot1000=2\cdot10^5$; zusammen rund $200{,}2$ Millionen. $\mathbf{A}(\mathbf{B}\mathbf{x})$: $\mathbf{B}\mathbf{x}$ kostet etwa $2\cdot1000\cdot1000=2\cdot10^6$, danach $\mathbf{A}(\mathbf{B}\mathbf{x})$ etwa $2\cdot10^5$; zusammen rund $2{,}2$ Millionen. Der zweite Weg ist etwa $91$-mal schneller, mit demselben Ergebnis.
:::
:::
