---
title: Das Matrix-Vektor-Produkt
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6210800
summary: Dieselbe gewichtete Summe soll für alle Beispiele eines Datensatzes berechnet werden.
tags: Matrix-Vektor-Produkt, Spaltenraum
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Dieselbe gewichtete Summe soll für alle Beispiele eines Datensatzes berechnet werden. Dieser Abschnitt führt dafür das Produkt aus Matrix und Vektor ein und zeigt die zwei Arten, es zu lesen: Zeile für Zeile oder Spalte für Spalte.
:::

### Matrix mal Vektor

<span class="anker" id="stufe-7-1"></span>

Die Maklerin aus Unterabschnitt [2.2](das-skalarprodukt.html#stufe-2-2) schätzt jede Wohnung mit derselben gewichteten Summe. Für vier Wohnungen rechnet sie viermal $\mathbf{w}^{\top}\mathbf{x}_i$. Schreibt man die Wohnungen als Zeilen einer Matrix, kann man alle vier Rechnungen in einem Schritt ausdrücken: Jede Zeile der Matrix wird mit demselben Vektor multipliziert.

:::definition Definition 7.1 (Matrix-Vektor-Produkt)
<span class="anker" id="satz-7-1"></span>

Für $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{x}\in\mathbb{R}^n$ ist das __Matrix-Vektor-Produkt__ $\mathbf{A}\mathbf{x}$ der Vektor im $\mathbb{R}^m$ mit den Komponenten

<span class="anker" id="gl-7-1"></span>
$$(\mathbf{A}\mathbf{x})_i=\sum_{j=1}^{n}a_{ij}\,x_j=a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n ,\qquad i=1,\dots,m . \tag{7.1}$$
:::

Das Produkt gibt es nur, wenn $\mathbf{x}$ so viele Komponenten hat, wie $\mathbf{A}$ Spalten hat. Das Ergebnis hat so viele Komponenten, wie $\mathbf{A}$ Zeilen hat. Aus den Rechenregeln für Summen folgt: $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ und $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$.

⁠**Rechenbeispiel:**

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=\begin{pmatrix}1\cdot2+2\cdot1\\0\cdot2+(-1)\cdot1\\3\cdot2+1\cdot1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

Eine $3\times2$-Matrix mal ein Vektor mit $2$ Komponenten ergibt einen Vektor mit $3$ Komponenten.

⁠**Kurz gesagt:** $\mathbf{A}\mathbf{x}$ ist der Vektor, dessen Komponente $i$ die Summe $\sum_ja_{ij}x_j$ ist; eine $m\times n$-Matrix macht aus einem Vektor im $\mathbb{R}^n$ einen Vektor im $\mathbb{R}^m$.

### Die Zeilensicht: viele Skalarprodukte

<span class="anker" id="stufe-7-2"></span>

Die Formel [(7.1)](#gl-7-1) sagt für jede Komponente: Zeile $i$ der Matrix, Eintrag für Eintrag mit $\mathbf{x}$ multipliziert und aufsummiert. Das ist das Skalarprodukt der Zeile $i$ mit $\mathbf{x}$ (Abb. [8](#abb-8), links).

:::satz Satz 7.2 (Zeilensicht)
<span class="anker" id="satz-7-2"></span>

Komponente $i$ von $\mathbf{A}\mathbf{x}$ ist das Skalarprodukt der $i$-ten Zeile von $\mathbf{A}$ mit $\mathbf{x}$. Für eine Datenmatrix $\mathbf{X}$ mit den Zeilen $\mathbf{x}_i^{\top}$ und einen Gewichtsvektor $\mathbf{w}$ heißt das

<span class="anker" id="gl-7-2"></span>
$$\mathbf{X}\mathbf{w}=\begin{pmatrix}\mathbf{x}_1^{\top}\mathbf{w}\\\vdots\\\mathbf{x}_N^{\top}\mathbf{w}\end{pmatrix}. \tag{7.2}$$
:::

Das Matrix-Vektor-Produkt wendet also die gewichtete Summe mit den Gewichten $\mathbf{w}$ auf alle Beispiele zugleich an und liefert den Vektor aller Vorhersagen. Im Bild des Mustervergleichs: Jedes Beispiel wird mit demselben Muster $\mathbf{w}$ verglichen.

⁠**Rechenbeispiel:** Für den Wohnungsdatensatz und $\mathbf{w}=(3,\,10,\,-4)^{\top}$ ist

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3\\10\\-4\end{pmatrix}=\begin{pmatrix}180+20-12\\120+10-4\\270+40-24\\210+30-8\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix},$$

die vier Vorhersagen der Maklerin in Tausend Euro.

⁠**Kurz gesagt:** In der Zeilensicht ist $\mathbf{A}\mathbf{x}$ eine Liste von Skalarprodukten, eines je Zeile; $\mathbf{X}\mathbf{w}$ sind die Vorhersagen für alle Beispiele.

:::hintergrund Wie viel Rechenarbeit ein Matrix-Vektor-Produkt kostet
Jede der $m$ Komponenten braucht $n$ Multiplikationen und $n-1$ Additionen. Zusammen sind das $m(2n-1)$, also ungefähr $2mn$ Grundrechenarten. Für die vier Wohnungen mit drei Merkmalen sind es $4\cdot5=20$. Für einen Datensatz mit einer Million Beispielen und hundert Merkmalen sind es etwa $2\cdot10^8$. Ein heutiger Prozessor führt pro Sekunde mehrere Milliarden solcher Operationen aus; ein einzelnes Matrix-Vektor-Produkt dieser Größe ist also schnell erledigt. Solche Zählungen geben aber nur die Größenordnung der Rechenzeit an, denn wie schnell ein Rechner tatsächlich ist, hängt auch davon ab, wie schnell er die Zahlen aus dem Speicher holen kann.
:::

### Die Spaltensicht: eine Linearkombination der Spalten

<span class="anker" id="stufe-7-3"></span>

Man kann dieselbe Summe auch anders ordnen. Statt Zeile für Zeile vorzugehen, sammelt man alle Beiträge, die zu $x_1$ gehören, dann alle, die zu $x_2$ gehören, und so weiter. Die Beiträge zu $x_j$ stehen alle in Spalte $j$ der Matrix. Dann wird aus dem Produkt eine Linearkombination der Spalten (Abb. [8](#abb-8), rechts).

:::abbildung ml/k1zeilenspalten 8
Zwei Arten, $\mathbf{A}\mathbf{x}$ für $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ und $\mathbf{x}=(2,\,1)^{\top}$ zu lesen. Links die Zeilensicht: Komponente $1$ des Ergebnisses ist das Skalarprodukt der ersten Zeile mit $\mathbf{x}$. Rechts die Spaltensicht: $\mathbf{A}\mathbf{x}$ ist $2$-mal die erste Spalte $\mathbf{a}_1=(2,1)^{\top}$ plus $1$-mal die zweite Spalte $\mathbf{a}_2=(1,1)^{\top}$.
:::

:::satz Satz 7.3 (Spaltensicht)
<span class="anker" id="satz-7-3"></span>

Sind $\mathbf{a}_1,\dots,\mathbf{a}_n$ die Spalten von $\mathbf{A}\in\mathbb{R}^{m\times n}$, so ist

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n=\sum_{j=1}^nx_j\,\mathbf{a}_j . \tag{7.3}$$

Das Matrix-Vektor-Produkt ist die Linearkombination der Spalten von $\mathbf{A}$ mit den Komponenten von $\mathbf{x}$ als Koeffizienten.
:::

:::beweis Spaltensicht
Komponente $i$ der rechten Seite ist $\sum_jx_j\,(\mathbf{a}_j)_i=\sum_jx_j\,a_{ij}$, denn die $i$-te Komponente der Spalte $\mathbf{a}_j$ ist der Eintrag $a_{ij}$. Das ist genau Komponente $i$ von $\mathbf{A}\mathbf{x}$ nach [(7.1)](#gl-7-1).
:::

⁠**Rechenbeispiel 1:** Für das Produkt aus dem vorigen Unterabschnitt ist

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=2\begin{pmatrix}1\\0\\3\end{pmatrix}+1\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

⁠**Rechenbeispiel 2:** Die Vorhersagen der Maklerin sind $3$-mal die Spalte der Flächen plus $10$-mal die Spalte der Zimmer minus $4$-mal die Spalte der Entfernungen:

$$\mathbf{X}\mathbf{w}=3\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+10\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-4\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}180\\120\\270\\210\end{pmatrix}+\begin{pmatrix}20\\10\\40\\30\end{pmatrix}-\begin{pmatrix}12\\4\\24\\8\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix}.$$

In dieser Form sieht man, welcher Teil jeder Vorhersage von welchem Merkmal stammt.

⁠**Kurz gesagt:** In der Spaltensicht ist $\mathbf{A}\mathbf{x}$ eine Linearkombination der Spalten von $\mathbf{A}$; die Komponenten von $\mathbf{x}$ sagen, wie viel von jeder Spalte genommen wird.

:::hintergrund Warum es zwei Sichten auf dieselbe Rechnung gibt
Beide Sichten berechnen dieselben $m\cdot n$ Produkte $a_{ij}x_j$ und addieren sie. Die Zeilensicht fasst sie zuerst zeilenweise zusammen, die Spaltensicht zuerst spaltenweise; bei endlich vielen Summanden ist die Reihenfolge gleichgültig, wie bei der Doppelsumme in Unterabschnitt [1.1](vektoren-daten-als-zahlenlisten.html#stufe-1-1). Jede Sicht beantwortet aber eine andere Frage. Die Zeilensicht fragt: Was kommt in Komponente $i$ heraus? Die Spaltensicht fragt: Welche Ergebnisse kann die Matrix überhaupt liefern, wenn man $\mathbf{x}$ frei wählt? Die zweite Frage führt direkt zum nächsten Begriff.
:::

### Der Spaltenraum

<span class="anker" id="stufe-7-4"></span>

Lässt man $\mathbf{x}$ alle Vektoren des $\mathbb{R}^n$ durchlaufen, so durchläuft $\mathbf{A}\mathbf{x}$ nach der Spaltensicht alle Linearkombinationen der Spalten. Das sind im Allgemeinen nicht alle Vektoren des $\mathbb{R}^m$.

:::definition Definition 7.4 (Spaltenraum)
<span class="anker" id="satz-7-4"></span>

Der __Spaltenraum__ einer Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist die Menge aller Vektoren $\mathbf{A}\mathbf{x}$ mit $\mathbf{x}\in\mathbb{R}^n$, also die Menge aller Linearkombinationen der Spalten von $\mathbf{A}$.
:::

⁠**Rechenbeispiel 1:** Die Matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ hat die Spalten $(1,\,2)^{\top}$ und $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. Jede Linearkombination ist ein Vielfaches von $(1,\,2)^{\top}$. Der Spaltenraum ist also nur die Gerade durch den Nullpunkt in Richtung $(1,\,2)^{\top}$, obwohl die Ergebnisse zwei Komponenten haben. Der Vektor $(3,\,6)^{\top}$ liegt darin, der Vektor $(1,\,1)^{\top}$ nicht.

⁠**Rechenbeispiel 2:** Die Matrix $\mathbf{H}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ liefert $\mathbf{H}\mathbf{x}=(x_1,\,x_2,\,x_1+x_2)^{\top}$. Ihr Spaltenraum besteht aus den Vektoren des $\mathbb{R}^3$, deren dritte Komponente die Summe der ersten beiden ist; das ist eine Ebene im Raum. Der Vektor $(1,\,2,\,3)^{\top}=\mathbf{H}\,(1,\,2)^{\top}$ liegt darin, $(1,\,1,\,1)^{\top}$ nicht, denn $1+1\ne1$.

Für eine Datenmatrix heißt das: Die Vorhersagen $\mathbf{X}\mathbf{w}$ liegen immer im Spaltenraum von $\mathbf{X}$, gleichgültig, welche Gewichte man wählt. Mit diesen Merkmalen lassen sich nur ganz bestimmte Listen von Vorhersagen überhaupt erzeugen.

⁠**Kurz gesagt:** Der Spaltenraum einer Matrix ist die Menge aller Vektoren $\mathbf{A}\mathbf{x}$, also alles, was sich aus ihren Spalten linear kombinieren lässt.

:::aufgabe Aufgabe 16 ★ Zwei Sichten auf ein Produkt
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

Berechne $\mathbf{B}\mathbf{x}$ für $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ und $\mathbf{x}=(1,\,3,\,-1)^{\top}$, einmal in der Zeilensicht und einmal in der Spaltensicht.

</li>

<li>

Ist $\mathbf{B}\,(1,\,2)^{\top}$ erklärt? Und $\mathbf{B}\,(1,\,2,\,3)^{\top}$? Begründe mit den Formaten und gib an, wie viele Komponenten das Ergebnis hat, wenn es erklärt ist.

</li>

<li>

Liegt $(2,\,0,\,2)^{\top}$ im Spaltenraum der Matrix $\mathbf{H}$ aus Unterabschnitt [7.4](#stufe-7-4)? Und $(2,\,1,\,2)^{\top}$?

</li>

</ol>

:::loesung
(a) Zeilensicht: $(1\cdot1+0\cdot3+2\cdot(-1),\ 2\cdot1+1\cdot3+0\cdot(-1))^{\top}=(-1,\,5)^{\top}$. Spaltensicht: $1\,(1,\,2)^{\top}+3\,(0,\,1)^{\top}-1\,(2,\,0)^{\top}=(1+0-2,\ 2+3-0)^{\top}=(-1,\,5)^{\top}$.

(b) $\mathbf{B}$ hat drei Spalten. $\mathbf{B}\,(1,\,2)^{\top}$ ist nicht erklärt, weil der Vektor nur zwei Komponenten hat. $\mathbf{B}\,(1,\,2,\,3)^{\top}$ ist erklärt und hat so viele Komponenten, wie $\mathbf{B}$ Zeilen hat, nämlich zwei: $(1+0+6,\ 2+2+0)^{\top}=(7,\,4)^{\top}$.

(c) Der Spaltenraum von $\mathbf{H}$ besteht aus den Vektoren, deren dritte Komponente die Summe der ersten beiden ist. Für $(2,\,0,\,2)^{\top}$ ist $2+0=2$: ja, es ist $\mathbf{H}\,(2,\,0)^{\top}$. Für $(2,\,1,\,2)^{\top}$ ist $2+1=3\ne2$: nein.
:::
:::

:::aufgabe Aufgabe 17 ★★ Die Monatsmiete
<span class="anker" id="aufg-17"></span>

Ein Mietspiegel schätzt die Monatsmiete einer Wohnung mit den Gewichten $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ in Euro pro Quadratmeter, pro Zimmer und pro Kilometer.

<ol class="al">

<li>

Berechne die geschätzten Mieten aller vier Wohnungen als $\mathbf{X}\mathbf{w}_{\mathrm M}$, einmal in der Zeilensicht und einmal in der Spaltensicht.

</li>

<li>

Wie viele Multiplikationen und Additionen hast du gebraucht? Wie viele wären es für $10\,000$ Wohnungen mit $20$ Merkmalen?

</li>

</ol>

:::loesung
(a) Zeilensicht, für Wohnung 1: $12\cdot60+30\cdot2-8\cdot3=720+60-24=756$, ebenso $502$, $1152$ und $914$ Euro. Spaltensicht:

$$12\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+30\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-8\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}720\\480\\1080\\840\end{pmatrix}+\begin{pmatrix}60\\30\\120\\90\end{pmatrix}-\begin{pmatrix}24\\8\\48\\16\end{pmatrix}=\begin{pmatrix}756\\502\\1152\\914\end{pmatrix}.$$

(b) Jede der vier Komponenten braucht $3$ Multiplikationen und $2$ Additionen, zusammen $12+8=20$. Für $10\,000$ Wohnungen mit $20$ Merkmalen sind es $10\,000\cdot20=200\,000$ Multiplikationen und $10\,000\cdot19=190\,000$ Additionen, zusammen $390\,000\approx2mn$ mit $m=10\,000$, $n=20$.
:::
:::
