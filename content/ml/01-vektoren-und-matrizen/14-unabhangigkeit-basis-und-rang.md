---
title: Unabhängigkeit, Basis und Rang
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Kapitel 1: Vektoren und Matrizen
nachschlagen: ja
order: 15211400
summary: Manche Vektoren einer Liste bringen nichts Neues, weil sie sich aus den anderen zusammensetzen lassen.
tags: Spann, linear unabhängig, linear abhängig, Basis, Dimension, Standardbasis, Rang, vollen Rang
lang: de
---

<span class="anker" id="stufe-13"></span>

:::zweck
Manche Vektoren einer Liste bringen nichts Neues, weil sie sich aus den anderen zusammensetzen lassen. Dieser Abschnitt misst, wie viele wirklich verschiedene Richtungen in einer Matrix stecken, und zeigt, was es für Daten bedeutet, wenn Merkmale dieselbe Information doppelt tragen.
:::

### Der Spann

<span class="anker" id="stufe-13-1"></span>

Der Spaltenraum einer Matrix ist die Menge aller Linearkombinationen ihrer Spalten. Dieselbe Bildung ergibt für jede Liste von Vektoren eine Menge, und sie bekommt einen eigenen Namen (Abb. [39](#abb-39)).

:::abbildung ml/k1spann 39
Der Spann (blau) dreier Listen von Vektoren in der Ebene, im Maßstab $1:2$. (a) Ein Vektor spannt eine Gerade durch den Nullpunkt auf. (b) Ein zweiter Vektor auf derselben Geraden ändert nichts. (c) Zwei Vektoren in verschiedenen Richtungen spannen die ganze Ebene auf.
:::

:::definition Definition 13.1 (Spann)
<span class="anker" id="satz-13-1"></span>

Der __Spann__ der Vektoren $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ ist die Menge aller ihrer Linearkombinationen:

<span class="anker" id="gl-13-1"></span>
$$\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}=\Bigl\{\sum_{l=1}^kc_l\,\mathbf{v}_l\ :\ c_1,\dots,c_k\in\mathbb{R}\Bigr\}. \tag{13.1}$$
:::

Der Spaltenraum einer Matrix ist also der Spann ihrer Spalten. Mit zwei Vektoren liegt auch jede Linearkombination von ihnen im Spann; man verlässt ihn durch Addieren und Vervielfachen nie.

::::beispiel [Rechenbeispiel]
$\operatorname{span}\{(1,\,2)^{\top}\}$ ist die Gerade aller Vielfachen $c\,(1,\,2)^{\top}$. Der Spann von $(1,\,2)^{\top}$ und $(2,\,4)^{\top}$ ist dieselbe Gerade, denn $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. Der Spann von $(1,\,0)^{\top}$ und $(1,\,1)^{\top}$ ist die ganze Ebene: Jeder Vektor $(y_1,\,y_2)^{\top}$ ist $(y_1-y_2)\,(1,\,0)^{\top}+y_2\,(1,\,1)^{\top}$. Im $\mathbb{R}^3$ ist $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ die Ebene aller Vektoren mit $x_3=0$.
::::

⁠**Kurz gesagt:** Der Spann einer Liste von Vektoren ist alles, was man aus ihnen linear kombinieren kann.

### Lineare Unabhängigkeit

<span class="anker" id="stufe-13-2"></span>

In Abb. [39](#abb-39) (b) bringt der zweite Vektor nichts Neues: Er liegt schon im Spann des ersten. Ein Datensatz kann dieselbe Schwäche haben. Enthält er die Zahl der Schlafzimmer, die Zahl der Wohnzimmer und die Zahl aller Zimmer, so ist die dritte Spalte die Summe der ersten beiden und trägt keine eigene Information. Man braucht ein Wort dafür, dass in einer Liste von Vektoren nichts überflüssig ist.

:::definition Definition 13.2 (Lineare Unabhängigkeit)
<span class="anker" id="satz-13-2"></span>

Vektoren $\mathbf{v}_1,\dots,\mathbf{v}_k$ heißen __linear unabhängig__, wenn

<span class="anker" id="gl-13-2"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\mathbf{0} \tag{13.2}$$

nur für $c_1=c_2=\dots=c_k=0$ gilt. Andernfalls heißen sie __linear abhängig__.
:::

Linear abhängig heißt gleichwertig: Mindestens einer der Vektoren ist eine Linearkombination der anderen. Denn gilt [(13.2)](#gl-13-2) mit einem Koeffizienten $c_l\ne0$, so kann man nach $\mathbf{v}_l$ auflösen: $\mathbf{v}_l=-\sum_{l'\ne l}(c_{l'}/c_l)\,\mathbf{v}_{l'}$. Umgekehrt ergibt eine solche Darstellung sofort eine Kombination mit dem Koeffizienten $-1$ vor $\mathbf{v}_l$.

::::beispiel [Rechenbeispiel]
$(1,\,2)^{\top}$ und $(2,\,4)^{\top}$ sind linear abhängig: $2\,(1,\,2)^{\top}-(2,\,4)^{\top}=\mathbf{0}$. Die Vektoren $(1,\,0)^{\top}$ und $(1,\,1)^{\top}$ sind linear unabhängig: Aus $c_1(1,\,0)^{\top}+c_2(1,\,1)^{\top}=(c_1+c_2,\ c_2)^{\top}=\mathbf{0}$ folgt erst $c_2=0$ und dann $c_1=0$. Die drei Vektoren $(1,\,0,\,1)^{\top}$, $(0,\,1,\,1)^{\top}$ und $(1,\,1,\,2)^{\top}$ sind linear abhängig, denn der dritte ist die Summe der ersten beiden.
::::

⁠**Kurz gesagt:** Linear unabhängig heißt: Keiner der Vektoren lässt sich aus den anderen kombinieren, es gibt keine Redundanz.

### Basis und Dimension

<span class="anker" id="stufe-13-3"></span>

Will man einen Spann so knapp wie möglich beschreiben, nimmt man so wenige Vektoren wie nötig, aber genug, um alles zu erreichen. Eine solche Liste ist wie ein Koordinatensystem: Jeder Vektor des Spanns hat dann genau eine Darstellung durch sie.

:::definition Definition 13.3 (Basis, Dimension)
<span class="anker" id="satz-13-3"></span>

Eine Liste linear unabhängiger Vektoren, deren Spann eine Menge $\mathcal S$ ist, heißt eine __Basis__ von $\mathcal S$. Die Zahl der Vektoren einer Basis heißt die __Dimension__ von $\mathcal S$, geschrieben $\dim\mathcal S$.
:::

Eine Menge $\mathcal S$ hat viele verschiedene Basen, aber alle bestehen aus gleich vielen Vektoren; das ist ein Satz der linearen Algebra, auf dem die Definition der Dimension beruht. Die Einheitsvektoren $\mathbf{e}_1,\dots,\mathbf{e}_d$ bilden eine Basis des $\mathbb{R}^d$, die __Standardbasis__; deshalb ist $\dim\mathbb{R}^d=d$.

:::satz Satz 13.4 (Eindeutige Koordinaten)
<span class="anker" id="satz-13-4"></span>

Ist $\mathbf{v}_1,\dots,\mathbf{v}_k$ eine Basis von $\mathcal S$, so hat jeder Vektor $\mathbf{x}\in\mathcal S$ genau eine Darstellung $\mathbf{x}=\sum_lc_l\mathbf{v}_l$.
:::

:::beweis Eindeutige Koordinaten
Mindestens eine Darstellung gibt es, weil die Basis $\mathcal S$ aufspannt. Gäbe es zwei, $\sum_lc_l\mathbf{v}_l=\sum_lc_l'\mathbf{v}_l$, so wäre ihre Differenz $\sum_l(c_l-c_l')\mathbf{v}_l=\mathbf{0}$. Wegen der linearen Unabhängigkeit sind dann alle $c_l-c_l'=0$.
:::

::::beispiel [Rechenbeispiel]
$(1,\,0)^{\top}$ und $(1,\,1)^{\top}$ bilden eine Basis des $\mathbb{R}^2$: Sie sind linear unabhängig und spannen die Ebene auf. Der Vektor $(3,\,2)^{\top}$ hat in dieser Basis die Koordinaten $1$ und $2$, denn $(3,\,2)^{\top}=1\cdot(1,\,0)^{\top}+2\cdot(1,\,1)^{\top}$. Die Gerade $\operatorname{span}\{(0,\,1)^{\top}\}$ hat die Dimension $1$, obwohl ihre Vektoren zwei Komponenten haben.
::::

⁠**Kurz gesagt:** Eine Basis ist eine Liste unabhängiger Vektoren, die alles aufspannt; ihre Länge ist die Dimension.

### Der Rang einer Matrix

<span class="anker" id="stufe-13-4"></span>

Eine Matrix mit $n$ Spalten kann weniger als $n$ wirklich verschiedene Richtungen enthalten. Die Zahl der Richtungen, die übrig bleiben, wenn man alles Überflüssige weglässt, sagt, wie viel eine Matrix tatsächlich leistet.

:::definition Definition 13.5 (Rang)
<span class="anker" id="satz-13-5"></span>

Der __Rang__ $\operatorname{rang}\mathbf{A}$ einer Matrix $\mathbf{A}$ ist die größte Zahl linear unabhängiger Spalten von $\mathbf{A}$. Er ist gleich der Dimension ihres Spaltenraums.
:::

:::satz Satz 13.6 (Spaltenrang gleich Zeilenrang)
<span class="anker" id="satz-13-6"></span>

Die größte Zahl linear unabhängiger Spalten einer Matrix ist gleich der größten Zahl linear unabhängiger Zeilen. Insbesondere ist $\operatorname{rang}\mathbf{A}=\operatorname{rang}\mathbf{A}^{\top}\le\min(m,n)$ für $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

Ist $\operatorname{rang}\mathbf{A}=\min(m,n)$, so hat $\mathbf{A}$ __vollen Rang__. Praktisch bestimmt man den Rang mit dem Gauß-Verfahren: Zeilenumformungen ändern ihn nicht, und in der Zeilenstufenform ist er die Zahl der Zeilen, die nicht ganz aus Nullen bestehen.

::::beispiel [Rechenbeispiel]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ hat den Rang $1$: Die zweite Spalte ist das Doppelte der ersten, und ebenso die zweite Zeile das Doppelte der ersten. Für

$$\mathbf K=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$$

zieht man die erste und die zweite Zeile von der dritten ab und erhält die Zeilen $(1,0,1)$, $(0,1,1)$, $(0,0,0)$. Zwei Zeilen sind nicht null, also ist $\operatorname{rang}\mathbf K=2$; tatsächlich ist die dritte Spalte die Summe der ersten beiden. Die Datenmatrix der Wohnungen hat den vollen Rang $3$.
::::

⁠**Kurz gesagt:** Der Rang zählt, wie viele wirklich verschiedene Richtungen in den Spalten einer Matrix stecken, und es sind genauso viele wie in ihren Zeilen.

:::hintergrund Warum es genauso viele unabhängige Zeilen wie Spalten gibt
Das ist nicht selbstverständlich: Zeilen und Spalten einer $3\times5$-Matrix leben in ganz verschiedenen Räumen. Ein kurzes Argument geht so. Es seien $r$ Spalten von $\mathbf{A}$ linear unabhängig, und jede andere Spalte sei eine Linearkombination von ihnen. Diese $r$ Spalten bilden eine Matrix $\mathbf G\in\mathbb{R}^{m\times r}$. Jede Spalte $\mathbf{a}_j$ von $\mathbf{A}$ ist dann $\mathbf G$ mal einen Koeffizientenvektor mit $r$ Komponenten. Schreibt man diese Koeffizientenvektoren als Spalten einer Matrix $\mathbf F\in\mathbb{R}^{r\times n}$, so ist nach [(9.2)](das-matrixprodukt.html#gl-9-2) $\mathbf{A}=\mathbf G\mathbf F$. Jetzt liest man dasselbe Produkt zeilenweise: Zeile $i$ von $\mathbf{A}$ ist Zeile $i$ von $\mathbf G$ mal $\mathbf F$, also eine Linearkombination der $r$ Zeilen von $\mathbf F$. Alle Zeilen von $\mathbf{A}$ liegen also im Spann der $r$ Zeilen von $\mathbf F$, einer Menge der Dimension höchstens $r$, und mehr als $r$ von ihnen können deshalb nicht linear unabhängig sein. Die Zeilen haben also höchstens so viele unabhängige Richtungen wie die Spalten. Wendet man dasselbe Argument auf $\mathbf{A}^{\top}$ an, deren Spalten die Zeilen von $\mathbf{A}$ sind, folgt die umgekehrte Ungleichung. Beide Zahlen sind also gleich.
:::

### Der Kern und der Rangsatz

<span class="anker" id="stufe-13-5"></span>

Eine Matrix mit $n$ Spalten nimmt Vektoren aus $n$ Richtungen entgegen. Ein Teil dieser Richtungen kommt im Ergebnis an, der Rest wird auf den Nullvektor abgebildet und geht verloren. Die verlorenen Richtungen bilden eine eigene Menge.

:::definition Definition 13.7 (Kern)
<span class="anker" id="satz-13-7"></span>

Der __Kern__ einer Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist die Menge aller Vektoren, die $\mathbf{A}$ auf den Nullvektor abbildet:

<span class="anker" id="gl-13-3"></span>
$$\ker\mathbf{A}=\{\mathbf{x}\in\mathbb{R}^n:\ \mathbf{A}\mathbf{x}=\mathbf{0}\} . \tag{13.3}$$
:::

Der Kern ist die Lösungsmenge des homogenen Systems aus Unterabschnitt [12.4](lineare-gleichungssysteme.html#stufe-12-4). Er enthält immer den Nullvektor, und mit zwei Vektoren enthält er auch jede Linearkombination von ihnen; man kann also von seiner Dimension sprechen.

:::satz Satz 13.8 (Rangsatz)
<span class="anker" id="satz-13-8"></span>

Für jede Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ gilt

<span class="anker" id="gl-13-4"></span>
$$\dim\ker\mathbf{A}+\operatorname{rang}\mathbf{A}=n . \tag{13.4}$$
:::

Die $n$ Richtungen des Eingangs teilen sich auf: Was nicht im Ergebnis ankommt, landet im Kern. Am Gauß-Verfahren sieht man es so: In der Zeilenstufenform gibt es $\operatorname{rang}\mathbf{A}$ Stufen. Die übrigen $n-\operatorname{rang}\mathbf{A}$ Unbekannten haben keine eigene Stufe und sind im homogenen System frei wählbar. Jede von ihnen liefert eine Richtung des Kerns.

:::satz Satz 13.9 (Wann eine quadratische Matrix invertierbar ist)
<span class="anker" id="satz-13-9"></span>

Für $\mathbf{A}\in\mathbb{R}^{n\times n}$ sind gleichwertig: (i) $\mathbf{A}$ ist invertierbar; (ii) $\ker\mathbf{A}=\{\mathbf{0}\}$; (iii) $\operatorname{rang}\mathbf{A}=n$; (iv) die Spalten von $\mathbf{A}$ sind linear unabhängig.
:::

:::beweis Invertierbarkeit
Aus (i) folgt (ii) nach Unterabschnitt [11.5](einheitsmatrix-und-inverse.html#stufe-11-5). (ii), (iii) und (iv) sind nach dem Rangsatz und der Definition des Rangs gleichwertig. Es bleibt: Aus (iii) und (ii) folgt (i). Ist $\operatorname{rang}\mathbf{A}=n$, so ist der Spaltenraum ein Raum der Dimension $n$ im $\mathbb{R}^n$, also der ganze $\mathbb{R}^n$. Jedes System $\mathbf{A}\mathbf{c}_j=\mathbf{e}_j$ ist deshalb lösbar, und die Lösungen bilden die Spalten einer Matrix $\mathbf{C}$ mit $\mathbf{A}\mathbf{C}=\mathbf{I}$. Außerdem ist $\mathbf{A}(\mathbf{C}\mathbf{A}-\mathbf{I})=\mathbf{A}\mathbf{C}\mathbf{A}-\mathbf{A}=\mathbf 0$. Jede Spalte von $\mathbf{C}\mathbf{A}-\mathbf{I}$ liegt also im Kern, der nach (ii) nur den Nullvektor enthält. Also ist auch $\mathbf{C}\mathbf{A}=\mathbf{I}$, und $\mathbf{C}=\mathbf{A}^{-1}$.
:::

::::beispiel [Rechenbeispiel]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ hat den Kern $\operatorname{span}\{(2,\,-1)^{\top}\}$ der Dimension $1$ und den Rang $1$: $1+1=2$. Die Matrix $\mathbf K$ von oben hat den Kern $\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$, denn ihre dritte Spalte ist die Summe der ersten beiden; mit $\operatorname{rang}\mathbf K=2$ ist $1+2=3$.
::::

**Rang und Lösbarkeit.** Mit Rang und Kern lassen sich die Fragen aus Abschnitt [12](lineare-gleichungssysteme.html#stufe-12) an Zahlen ablesen, auch für Matrizen, die nicht quadratisch sind. Gibt es eine Lösung? Ist sie eindeutig? Gibt es für jede rechte Seite eine?

:::satz Satz 13.10 (Lösbarkeit und Rang)
<span class="anker" id="satz-13-10"></span>

Für $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{y}\in\mathbb{R}^m$ gilt:

<ol class="rm">

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ ist genau dann lösbar, wenn $\operatorname{rang}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rang}\mathbf{A}$ ist;

</li>

<li>

ist das System lösbar, so ist die Lösung genau dann eindeutig, wenn $\operatorname{rang}\mathbf{A}=n$ ist;

</li>

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ ist genau dann für jedes $\mathbf{y}\in\mathbb{R}^m$ lösbar, wenn $\operatorname{rang}\mathbf{A}=m$ ist.

</li>

</ol>
:::

:::beweis Lösbarkeit und Rang
(i) Nach Unterabschnitt [12.2](lineare-gleichungssysteme.html#stufe-12-2) ist das System genau dann lösbar, wenn $\mathbf{y}$ im Spaltenraum von $\mathbf{A}$ liegt. Liegt $\mathbf{y}$ darin, so bringt die zusätzliche Spalte keine neue Richtung: Die Spalten von $(\mathbf{A}\,|\,\mathbf{y})$ spannen denselben Raum auf wie die von $\mathbf{A}$, und beide Ränge sind dessen Dimension. Liegt $\mathbf{y}$ nicht darin, so nimmt man $r=\operatorname{rang}\mathbf{A}$ linear unabhängige Spalten $\mathbf g_1,\dots,\mathbf g_r$ von $\mathbf{A}$ und dazu $\mathbf{y}$. Aus $c_1\mathbf g_1+\dots+c_r\mathbf g_r+c\,\mathbf{y}=\mathbf{0}$ folgt $c=0$, denn sonst wäre $\mathbf{y}$ eine Linearkombination der $\mathbf g_l$ und läge im Spaltenraum; dann sind auch alle $c_l=0$. Also hat $(\mathbf{A}\,|\,\mathbf{y})$ mindestens $r+1$ linear unabhängige Spalten, und $\operatorname{rang}(\mathbf{A}\,|\,\mathbf{y})>\operatorname{rang}\mathbf{A}$.

(ii) Nach Unterabschnitt [12.4](lineare-gleichungssysteme.html#stufe-12-4) sind alle Lösungen eine Lösung plus die Vektoren des Kerns. Die Lösung ist also genau dann eindeutig, wenn $\ker\mathbf{A}=\{\mathbf{0}\}$ ist, und nach dem Rangsatz heißt das $\operatorname{rang}\mathbf{A}=n$.

(iii) Jedes $\mathbf{y}$ liegt genau dann im Spaltenraum, wenn der Spaltenraum der ganze $\mathbb{R}^m$ ist. Das ist genau dann der Fall, wenn er die Dimension $m$ hat, also $\operatorname{rang}\mathbf{A}=m$.
:::

Für eine quadratische Matrix mit $\operatorname{rang}\mathbf{A}=n=m$ treffen (ii) und (iii) zusammen: genau eine Lösung für jede rechte Seite, passend zum Satz über die Invertierbarkeit.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ist $\operatorname{rang}\mathbf{A}=1$. Mit $\mathbf{y}=(1,\,1)^{\top}$ hat die erweiterte Matrix die Zeilen $(1,\,2\,|\,1)$ und $(2,\,4\,|\,1)$; zieht man die erste zweimal von der zweiten ab, bleibt $(0,\,0\,|\,-1)$, keine Nullzeile. Also ist $\operatorname{rang}(\mathbf{A}\,|\,\mathbf{y})=2\ne1$, und das System ist unlösbar, wie in Unterabschnitt [12.2](lineare-gleichungssysteme.html#stufe-12-2). Mit $\mathbf{y}=(3,\,6)^{\top}$ bleibt dagegen $(0,\,0\,|\,0)$, die Ränge sind gleich, und das System ist lösbar. Wegen $\operatorname{rang}\mathbf{A}=1<2=n$ ist die Lösung nicht eindeutig: Alle Lösungen sind $(1,\,1)^{\top}+t\,(2,\,-1)^{\top}$. Und wegen $\operatorname{rang}\mathbf{A}=1<2=m$ gibt es rechte Seiten ohne Lösung. Im überbestimmten System aus Unterabschnitt [12.5](lineare-gleichungssysteme.html#stufe-12-5) ist $\operatorname{rang}\mathbf{A}=2=n$: Gäbe es eine Lösung, wäre sie eindeutig. Es gibt aber keine, also ist dort nach (i) $\operatorname{rang}(\mathbf{A}\,|\,\mathbf{y})=3$.
::::

⁠**Kurz gesagt:** Der Kern sammelt die Richtungen, die eine Matrix auf null abbildet; Kern und Rang teilen sich die $n$ Eingangsrichtungen. Ein System $\mathbf{A}\mathbf{x}=\mathbf{y}$ ist genau dann lösbar, wenn die rechte Seite den Rang nicht erhöht, und die Lösung ist genau dann eindeutig, wenn der Kern nur den Nullvektor enthält.

### Abhängige Merkmale

<span class="anker" id="stufe-13-6"></span>

In echten Datensätzen tragen Merkmale manchmal dieselbe Information doppelt. Ein Fragebogen erfasst das Körpergewicht in Kilogramm und, für eine andere Auswertung, noch einmal in Pfund. Eine Hausbeschreibung nennt die Fläche des Erdgeschosses, die des Obergeschosses und die Gesamtfläche. Für die Datenmatrix heißt das: Ihre Spalten sind linear abhängig, und ihr Rang ist kleiner als die Zahl der Merkmale.

::::beispiel [Rechenbeispiel] Erdgeschoss, Obergeschoss, Gesamtfläche
Vier Häuser:

$$\mathbf{X}=\begin{pmatrix}50&40&90\\60&0&60\\45&45&90\\70&30&100\end{pmatrix}\qquad(\text{Flächen in }\mathrm m^2).$$

Die dritte Spalte ist die Summe der ersten beiden. Also ist $\operatorname{rang}\mathbf{X}=2<3$, und der Kern enthält $\mathbf k=(1,\,1,\,-1)^{\top}$, denn $\mathbf{X}\mathbf k=\mathbf{0}$. Daraus folgen zwei Dinge.

<ul>

<li>

⁠**Die Gewichte sind nicht eindeutig.** Für jede Zahl $t$ liefern $\mathbf{w}$ und $\mathbf{w}+t\,\mathbf k$ dieselben Vorhersagen, denn $\mathbf{X}(\mathbf{w}+t\,\mathbf k)=\mathbf{X}\mathbf{w}+t\,\mathbf{X}\mathbf k=\mathbf{X}\mathbf{w}$. Die Gewichte $(3,\,3,\,0)^{\top}$, „$3$ pro Quadratmeter Erdgeschoss und Obergeschoss“, und $(0,\,0,\,3)^{\top}$, „$3$ pro Quadratmeter Gesamtfläche“, ergeben beide $(270,\,180,\,270,\,300)^{\top}$. Aus den Vorhersagen allein kann man nicht ablesen, welche Gewichte gemeint waren, und es ist sinnlos, ein einzelnes dieser Gewichte zu deuten.

</li>

<li>

⁠**Die Gram-Matrix der Merkmale ist singulär.** Aus $\mathbf{X}\mathbf k=\mathbf{0}$ folgt $\mathbf{X}^{\top}\mathbf{X}\mathbf k=\mathbf{X}^{\top}\mathbf{0}=\mathbf{0}$ mit $\mathbf k\ne\mathbf{0}$. Nach Unterabschnitt [11.5](einheitsmatrix-und-inverse.html#stufe-11-5) hat $\mathbf{X}^{\top}\mathbf{X}$ dann keine Inverse.

</li>

</ul>
::::

::::beispiel [Rechenbeispiel] Kilogramm und Pfund
Ein Pfund sind genau $0{,}45359237$ kg, also ist eine Masse in Pfund das $c=1/0{,}45359237\approx2{,}20462$-Fache derselben Masse in Kilogramm. Drei Personen mit Größe (cm), Masse (kg) und Masse (Pfund):

$$\mathbf{X}=\begin{pmatrix}170&70&70\,c\\182&85&85\,c\\165&60&60\,c\end{pmatrix}\approx\begin{pmatrix}170&70&154{,}3\\182&85&187{,}4\\165&60&132{,}3\end{pmatrix}.$$

Die dritte Spalte ist das $c$-Fache der zweiten, also ist $\operatorname{rang}\mathbf{X}=2$ und $(0,\,c,\,-1)^{\top}$ liegt im Kern. Die Pfundspalte bringt keine neue Information, sie verdoppelt nur eine vorhandene.
::::

⁠**Kurz gesagt:** Tragen Merkmale dieselbe Information doppelt, sind die Spalten der Datenmatrix linear abhängig; dann ist der Rang kleiner als $d$, verschiedene Gewichte liefern dieselben Vorhersagen, und $\mathbf{X}^{\top}\mathbf{X}$ ist nicht invertierbar.

:::aufgabe Aufgabe 31 ★★ Rang und Kern
<span class="anker" id="aufg-31"></span>

Bestimme Rang und Kern von

$$\mathbf{A}_1=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}\qquad\text{und}\qquad \mathbf{A}_2=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$$

und prüfe jeweils den Rangsatz. Welche der beiden Matrizen ist invertierbar?

:::loesung
$\mathbf{A}_1$: Die zweite Zeile ist das Doppelte der ersten. Zieht man sie ab und die erste Zeile auch von der dritten, bleiben die Zeilen $(1,2,3)$, $(0,0,0)$, $(0,-2,-2)$; nach dem Vertauschen der beiden unteren Zeilen ist das eine Stufenform mit zwei Stufen, also $\operatorname{rang}\mathbf{A}_1=2$. Den Kern liefern die Gleichungen $x_1+2x_2+3x_3=0$ und $-2x_2-2x_3=0$: Mit $x_3=t$ ist $x_2=-t$ und $x_1=-2(-t)-3t=-t$, also $\ker\mathbf{A}_1=\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$. Probe: Die Summe der ersten beiden Spalten ist $(3,\,6,\,1)^{\top}$, die dritte Spalte ist $(3,\,6,\,1)^{\top}$. Rangsatz: $1+2=3$. $\mathbf{A}_1$ ist nicht invertierbar.

$\mathbf{A}_2$: Zieht man die erste Zeile von der dritten ab, entsteht $(0,\,-1,\,1)$; addiert man die zweite Zeile, entsteht $(0,\,0,\,2)$. Drei Stufen, also $\operatorname{rang}\mathbf{A}_2=3$ und $\ker\mathbf{A}_2=\{\mathbf{0}\}$. Rangsatz: $0+3=3$. $\mathbf{A}_2$ ist invertierbar; ihre Determinante ist $1\cdot(1-0)-1\cdot(0-1)+0=2\ne0$.
:::
:::

:::aufgabe Aufgabe 32 ★★ Kilogramm und Pfund
<span class="anker" id="aufg-32"></span>

Benutze die Personen-Datenmatrix aus Unterabschnitt [13.6](#stufe-13-6).

<ol class="al">

<li>

Gib zwei verschiedene Gewichtsvektoren an, die für alle drei Personen dieselben Vorhersagen liefern, und zwar so, dass der eine nur die Kilogrammspalte und der andere nur die Pfundspalte benutzt.

</li>

<li>

Die Tabelle gibt die Pfundwerte auf eine Nachkommastelle gerundet an. Sind die Spalten der gerundeten Tabelle noch genau linear abhängig? Was sagt das über den Rang, den man aus gerundeten Daten berechnet?

</li>

</ol>

:::loesung
(a) Die Gewichte $(0,\,1,\,0)^{\top}$ sagen für jede Person ihre Masse in Kilogramm voraus, also $(70,\,85,\,60)^{\top}$. Dieselben Vorhersagen liefern die Gewichte $(0,\,0,\,1/c)^{\top}\approx(0;\ 0;\ 0{,}4536)^{\top}$, die nur die Pfundspalte benutzen, denn $\frac1c\cdot c\,x=x$. Die beiden Gewichtsvektoren unterscheiden sich um $\frac1c\,(0,\,c,\,-1)^{\top}$, einen Vektor des Kerns.

(b) Die Verhältnisse der gerundeten Pfund- zu den Kilogrammwerten sind $154{,}3/70\approx2{,}20429$, $187{,}4/85\approx2{,}20471$ und $132{,}3/60=2{,}205$, nicht genau gleich. Die gerundeten Spalten sind also nicht mehr exakt proportional, und die gerundete Tabelle hat rechnerisch den vollen Rang $3$. Inhaltlich hat sich nichts geändert: Die Pfundspalte trägt immer noch fast nur die Information der Kilogrammspalte. Der Rang springt durch winzige Rundungen von $2$ auf $3$. Bei gemessenen oder gerundeten Daten sagt der Rang allein deshalb nicht, ob zwei Merkmale praktisch dieselbe Information tragen.
:::
:::

:::aufgabe Aufgabe 33 ★★ Ein Stadtteil als Zahl
<span class="anker" id="aufg-33"></span>

Die Wohnungen liegen entweder im Norden oder im Süden. Man übersetzt das in zwei Merkmale: „Nord“ ist $1$ für Wohnungen im Norden und sonst $0$, „Süd“ ebenso für den Süden. Für einen Grundpreis hängt man außerdem eine Spalte aus Einsen an (Unterabschnitt [8.5](lineare-abbildungen.html#stufe-8-5)). Vier Wohnungen, abwechselnd Nord und Süd, ergeben

$$\mathbf{X}=\begin{pmatrix}1&1&0\\1&0&1\\1&1&0\\1&0&1\end{pmatrix}\qquad(\text{Spalten: Eins, Nord, Süd}).$$

<ol class="al">

<li>

Bestimme den Rang von $\mathbf{X}$ und einen Vektor $\mathbf k\ne\mathbf{0}$ im Kern. Welche Beziehung zwischen den Spalten steckt dahinter?

</li>

<li>

Zeige, dass die Gewichte $(100,\,20,\,0)^{\top}$ und $(80,\,40,\,20)^{\top}$ dieselben Vorhersagen liefern. Wie behebt man die Abhängigkeit, ohne Information zu verlieren?

</li>

</ol>

:::loesung
(a) Jede Wohnung liegt entweder im Norden oder im Süden, also ist Spalte „Nord“ plus Spalte „Süd“ in jeder Zeile gleich $1$, gleich der Einsenspalte. Die Spalten sind linear abhängig, und $\mathbf k=(1,\,-1,\,-1)^{\top}$ liegt im Kern: $\mathbf{X}\mathbf k=\mathbf{0}$. Die erste und die zweite Spalte sind unabhängig, also ist $\operatorname{rang}\mathbf{X}=2$.

(b) $\mathbf{X}\,(100,\,20,\,0)^{\top}=(120,\,100,\,120,\,100)^{\top}$ und $\mathbf{X}\,(80,\,40,\,20)^{\top}=(120,\,100,\,120,\,100)^{\top}$. Die beiden Gewichtsvektoren unterscheiden sich um $(20,\,-20,\,-20)^{\top}=20\,\mathbf k$. Man behebt die Abhängigkeit, indem man eine der beiden Spalten „Nord“ oder „Süd“ weglässt, zum Beispiel „Süd“. Dann ist der Grundpreis der Preis im Süden, und das Gewicht von „Nord“ ist der Aufschlag für den Norden. Information geht nicht verloren, denn „Süd“ ist immer $1-\text{Nord}$ und lässt sich jederzeit zurückrechnen.
:::
:::
