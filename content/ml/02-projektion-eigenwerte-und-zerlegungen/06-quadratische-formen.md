---
title: Quadratische Formen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
knoten: Grundlagen 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15220600
summary: Nach den linearen Funktionen sind die quadratischen die einfachsten Funktionen mehrerer Variablen.
tags: quadratische Form
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Nach den linearen Funktionen sind die quadratischen die einfachsten Funktionen mehrerer Variablen. Sie beschreiben Energien, Fehlerquadrate und gekrümmte Flächen. Dieser Abschnitt schreibt sie mit einer Matrix, zeigt die drei Grundformen Schüssel, Rinne und Sattel und wie man an der Matrix erkennt, welche Form vorliegt, solange sie keine gemischten Glieder hat.
:::

### Quadratische Formen

<span class="anker" id="stufe-5-1"></span>

In [Grundlagen 1, Abschnitt 8.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-4), war jede lineare Funktion mit einem Ausgang eine gewichtete Summe $\mathbf{w}^{\top}\mathbf{x}$ der Komponenten. Die nächst einfachere Art von Funktion summiert Produkte von je zwei Komponenten: Quadrate wie $x_1^2$ und gemischte Glieder wie $x_1x_2$. Ein Beispiel aus der Elektrotechnik ist die magnetische Energie zweier gekoppelter Spulen mit den Induktivitäten $L_1$, $L_2$ und der Gegeninduktivität $M$, durch die die Ströme $i_1$ und $i_2$ fließen:

$$W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2 .$$

Solche Summen lassen sich mit einer Matrix in der Mitte schreiben.

:::definition Definition 5.1 (Quadratische Form)
<span class="anker" id="satz-5-1"></span>

Zu einer quadratischen Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ heißt die Funktion

<span class="anker" id="gl-5-1"></span>
$$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^na_{il}\,x_ix_l \tag{5.1}$$

die __quadratische Form__ von $\mathbf{A}$.
:::

Das Ergebnis ist eine Zahl: $\mathbf{A}\mathbf{x}$ ist ein Vektor, und $\mathbf{x}^{\top}(\mathbf{A}\mathbf{x})$ ist das Skalarprodukt von $\mathbf{x}$ mit ihm. Für $n=2$ ausgeschrieben ist

$$\mathbf{x}^{\top}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\mathbf{x}=a_{11}x_1^2+(a_{12}+a_{21})\,x_1x_2+a_{22}x_2^2 .$$

Verdoppelt man $\mathbf{x}$, so vervierfacht sich $f$: $f(c\,\mathbf{x})=c^2f(\mathbf{x})$. Daher der Name.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ ist $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$. An der Stelle $\mathbf{x}=(1,\,-1)^{\top}$ ist $f=5-4+2=3$; zur Kontrolle ist $\mathbf{A}\mathbf{x}=(3,\,0)^{\top}$ und $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=3$. Abb. [14](#abb-14) rechnet die Doppelsumme [(5.1)](#gl-5-1) an dieser Stelle Glied für Glied aus. An der Stelle $(1,\,1)^{\top}$ ist $f=11$, im Nullpunkt $f=0$. Die Energie der beiden Spulen ist $W=\tfrac12\,\mathbf i^{\top}\bigl(\begin{smallmatrix}L_1&M\\M&L_2\end{smallmatrix}\bigr)\,\mathbf i$ mit dem Stromvektor $\mathbf i=(i_1,\,i_2)^{\top}$; die Matrix heißt Induktivitätsmatrix.

:::abbildung ml/k2rqf 14
Die quadratische Form von $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ an der Stelle $\mathbf{x}=(1,-1)^{\top}$ als Doppelsumme: vier Glieder, eines für jeden Eintrag von $\mathbf{A}$.
:::
::::

⁠**Kurz gesagt:** Eine quadratische Form $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ist eine Summe aus Quadraten und gemischten Produkten der Komponenten, mit den Einträgen von $\mathbf{A}$ als Gewichten.

### Nur der symmetrische Anteil zählt

<span class="anker" id="stufe-5-2"></span>

Im Ausdruck für $n=2$ kommen $a_{12}$ und $a_{21}$ nur als Summe vor. Die Matrizen $\bigl(\begin{smallmatrix}5&4\\0&2\end{smallmatrix}\bigr)$ und $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ haben deshalb dieselbe quadratische Form. Man darf sich immer die symmetrische aussuchen.

:::satz Satz 5.2 (Der symmetrische Anteil)
<span class="anker" id="satz-5-2"></span>

Für jede quadratische Matrix $\mathbf{A}$ und jedes $\mathbf{x}$ ist

<span class="anker" id="gl-5-2"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\Bigl(\frac{\mathbf{A}+\mathbf{A}^{\top}}2\Bigr)\mathbf{x} . \tag{5.2}$$
:::

:::beweis Der symmetrische Anteil
Die Zahl $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ist gleich ihrer eigenen Transponierten, also $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})^{\top}=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{x}$. Der Mittelwert beider Ausdrücke ist $\mathbf{x}^{\top}\frac{\mathbf{A}+\mathbf{A}^{\top}}2\mathbf{x}$.
:::

Die Matrix $\frac12(\mathbf{A}+\mathbf{A}^{\top})$ ist symmetrisch. In diesem Kapitel hat eine quadratische Form deshalb immer eine symmetrische Matrix. Man liest sie so ab: Auf der Diagonale stehen die Faktoren vor den Quadraten, außerhalb jeweils die Hälfte des Faktors vor dem gemischten Glied.

::::beispiel [Rechenbeispiel]
Die Form $3x_1^2-6x_1x_2+x_2^2$ hat die symmetrische Matrix $\bigl(\begin{smallmatrix}3&-3\\-3&1\end{smallmatrix}\bigr)$. Die Form $x_1^2+2x_2^2+4x_3^2+2x_1x_3$ im $\mathbb{R}^3$ hat die Matrix $\Bigl(\begin{smallmatrix}1&0&1\\0&2&0\\1&0&4\end{smallmatrix}\Bigr)$; das gemischte Glied $2x_1x_3$ verteilt sich auf die Einträge $(1,3)$ und $(3,1)$.
::::

⁠**Kurz gesagt:** Eine quadratische Form sieht nur den symmetrischen Anteil ihrer Matrix; man schreibt sie deshalb immer mit einer symmetrischen Matrix.

### Schüssel, Rinne und Sattel

<span class="anker" id="stufe-5-3"></span>

Bei zwei Variablen kann man die quadratische Form als Fläche über der Ebene zeichnen, mit $f(\mathbf{x})$ als Höhe, und wie auf einer Landkarte ihre Höhenlinien, die Linien gleicher Höhe. Am einfachsten ist das, wenn die Matrix eine Diagonalmatrix ist. Dann gibt es keine gemischten Glieder, und $f(\mathbf{x})=a_{11}x_1^2+a_{22}x_2^2$. Je nach den Vorzeichen der beiden Einträge entstehen drei Grundformen (Abb. [15](#abb-15)).

:::abbildung ml/k2formen 15
Oben die Graphen der quadratischen Formen $x_1^2+2x_2^2$ (Schüssel), $x_1^2$ (Rinne) und $x_1^2-x_2^2$ (Sattel) über dem Quadrat $|x_1|,|x_2|\le1$, unten ihre Höhenlinien. Bei der Schüssel sind es Ellipsen ($f=\tfrac14,\tfrac12,1$), bei der Rinne Paare paralleler Geraden; gestrichelt die Gerade $x_1=0$, auf der die Rinne die Höhe null hat. Beim Sattel sind es Hyperbeln, kräftig für $f=\tfrac14,\tfrac12$, blass für $f=-\tfrac14,-\tfrac12$; gestrichelt die beiden Geraden mit $f=0$.
:::

<ul>

<li>

⁠**Schüssel:** Beide Diagonaleinträge sind positiv, etwa $f=x_1^2+2x_2^2$. Dann ist $f(\mathbf{x})>0$ für jedes $\mathbf{x}\ne\mathbf{0}$, und nur im Nullpunkt ist $f=0$. Die Höhenlinien sind Ellipsen um den Nullpunkt, mit den Halbachsen auf den Koordinatenachsen.

</li>

<li>

⁠**Rinne:** Ein Eintrag ist positiv, der andere null, etwa $f=x_1^2$. Dann ist $f\ge0$, aber auf der ganzen Geraden $x_1=0$ ist $f=0$: Die Fläche hat dort einen geraden Talboden. Die Höhenlinien sind Paare paralleler Geraden.

</li>

<li>

⁠**Sattel:** Die Einträge haben verschiedene Vorzeichen, etwa $f=x_1^2-x_2^2$. Längs der $x_1$-Achse steigt die Fläche nach beiden Seiten, längs der $x_2$-Achse fällt sie nach beiden Seiten. Die Höhenlinien sind Hyperbeln.

</li>

</ul>

Sind beide Einträge negativ, steht die Schüssel auf dem Kopf; das ist eine Kuppel. Ein negativer und ein verschwindender Eintrag geben eine umgedrehte Rinne, einen Kamm. Bei mehr als zwei Variablen gilt dasselbe: Die Vorzeichen der Diagonaleinträge entscheiden über die Form.

::::beispiel [Rechenbeispiel]
Für die Schüssel $f=x_1^2+2x_2^2$ ist die Höhenlinie $f=1$ die Ellipse mit den Halbachsen $1$ auf der $x_1$-Achse und $1/\sqrt2\approx0{,}707$ auf der $x_2$-Achse: Bei $(1,\,0)^{\top}$ und bei $(0,\,1/\sqrt2)^{\top}$ ist $f=1$. Beim Sattel $f=x_1^2-x_2^2$ ist $f(1,\,0)=1$, $f(0,\,1)=-1$ und $f(1,\,1)=0$.
::::

⁠**Kurz gesagt:** Ohne gemischte Glieder liest man die Form an den Vorzeichen der Diagonale ab: alle positiv eine Schüssel, positiv und null eine Rinne, gemischte Vorzeichen ein Sattel.

### Quadratisch ergänzen

<span class="anker" id="stufe-5-4"></span>

Mit gemischten Gliedern sieht man die Form nicht mehr sofort. Ist $5x_1^2+4x_1x_2+2x_2^2$ eine Schüssel? Das gemischte Glied kann negativ werden. Aus der Schule kennt man ein Werkzeug, das gemischte Glieder beseitigt: das quadratische Ergänzen. Es schreibt die Form als Summe von Quadraten, und an den Faktoren vor den Quadraten liest man die Form ab wie im vorigen Unterabschnitt.

:::herleitung Quadratisch ergänzen bei zwei Variablen
Es sei $a\ne0$. Man klammert $a$ aus den Gliedern mit $x_1$ aus und ergänzt zu einem Quadrat:

$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1^2+\frac{2b}ax_1x_2\Bigr)+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2-\frac{b^2}ax_2^2+cx_2^2 .$$

Also ist

<span class="anker" id="gl-5-3"></span>
$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2+\Bigl(c-\frac{b^2}a\Bigr)x_2^2 . \tag{5.3}$$
:::

Rechts steht eine Summe von zwei Quadraten. Die neuen Variablen $z_1=x_1+\frac bax_2$ und $z_2=x_2$ nehmen jedes Zahlenpaar an, wenn $\mathbf{x}$ die Ebene durchläuft. Die Form in den Variablen $z_1,z_2$ hat also keine gemischten Glieder mehr, und die Vorzeichen von $a$ und $c-b^2/a$ entscheiden über Schüssel, Rinne oder Sattel.

::::beispiel [Rechenbeispiel 1]
$5x_1^2+4x_1x_2+2x_2^2$ hat $a=5$, $b=2$, $c=2$:

$$5x_1^2+4x_1x_2+2x_2^2=5\,(x_1+0{,}4\,x_2)^2+1{,}2\,x_2^2 .$$

Beide Faktoren sind positiv: Die Form ist eine Schüssel. Probe bei $\mathbf{x}=(1,\,-1)^{\top}$: $5\cdot0{,}36+1{,}2=3$.
::::

::::beispiel [Rechenbeispiel 2]
$x_1^2+6x_1x_2+x_2^2=(x_1+3x_2)^2-8x_2^2$. Die Faktoren haben verschiedene Vorzeichen: ein Sattel. Tatsächlich ist $f(1,\,0)=1>0$ und $f(1,\,-1)=1-6+1=-4<0$.
::::

⁠**Kurz gesagt:** Quadratisches Ergänzen schreibt eine quadratische Form als Summe von Quadraten; die Vorzeichen der Faktoren vor den Quadraten zeigen, ob sie eine Schüssel, eine Rinne oder ein Sattel ist.

:::hintergrund Quadratisches Ergänzen ist das Gauß-Verfahren
Die Zahlen in [(5.3)](#gl-5-3) sind dieselben wie im Gauß-Verfahren aus [Grundlagen 1, Abschnitt 12.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3), angewandt auf die symmetrische Matrix $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$. Um unter der Diagonale eine Null zu erzeugen, zieht man das $\frac ba$-Fache der ersten Zeile von der zweiten ab und erhält $\bigl(\begin{smallmatrix}a&b\\0&c-b^2/a\end{smallmatrix}\bigr)$. Die Diagonaleinträge dieser Stufenform, die sogenannten Pivots, sind genau die Faktoren vor den Quadraten, und der Eliminationsfaktor $\frac ba$ steht in der ersten Klammer. Für die Matrix $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$: Faktor $0{,}4$, Pivots $5$ und $1{,}2$. Bei $n$ Variablen setzt man dasselbe fort: Jeder Eliminationsschritt ergänzt eine Variable zu einem Quadrat. Die Form ist genau dann eine Schüssel, wenn alle Pivots positiv sind. Das Produkt der Pivots ist nach den Rechenregeln aus [Grundlagen 1, Abschnitt 14.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), die Determinante, hier $5\cdot1{,}2=6=5\cdot2-2\cdot2$.
:::

:::aufgabe Aufgabe 14 ★ Formen und Matrizen
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Gib die symmetrische Matrix der Formen $2x_1^2-2x_1x_2+3x_2^2$ und $x_1x_2$ an.

</li>

<li>

Berechne die Form von $\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)$ und ihre symmetrische Matrix.

</li>

<li>

Bestimme ohne Rechnung, ob $3x_1^2+x_2^2$, $-x_1^2$ und $2x_1^2-x_2^2+x_3^2$ eine Schüssel, eine Rinne, ein Sattel oder etwas anderes sind.

</li>

</ol>

:::loesung
(a) Diagonale aus den Quadraten, außerhalb die Hälfte des gemischten Faktors: $2x_1^2-2x_1x_2+3x_2^2$ hat die Matrix $\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$, und $x_1x_2$ hat $\bigl(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\bigr)$.

(b) $\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)\mathbf{x}=x_1^2+(3-1)\,x_1x_2+2x_2^2=x_1^2+2x_1x_2+2x_2^2$. Die symmetrische Matrix ist $\tfrac12(\mathbf{A}+\mathbf{A}^{\top})=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)$.

(c) $3x_1^2+x_2^2$: beide Faktoren positiv, eine Schüssel. $-x_1^2$: ein negativer und ein verschwindender Faktor, also eine umgedrehte Rinne, ein Kamm längs der $x_2$-Achse. $2x_1^2-x_2^2+x_3^2$: gemischte Vorzeichen, ein Sattel; längs $x_1$ und $x_3$ steigt die Form, längs $x_2$ fällt sie.
:::
:::

:::aufgabe Aufgabe 15 ★★ Quadratisch ergänzen
<span class="anker" id="aufg-15"></span>

Ergänze quadratisch und entscheide über die Form:

$$f_1=2x_1^2+8x_1x_2+11x_2^2,\qquad f_2=x_1^2+4x_1x_2+4x_2^2,\qquad f_3=x_1^2+4x_1x_2+x_2^2 .$$

Gib bei der Rinne die Gerade an, auf der $f=0$ ist, und beim Sattel einen Punkt mit $f<0$.

:::loesung
Mit [(5.3)](#gl-5-3):

<ul>

<li>

$f_1$: $a=2$, $b=4$, $c=11$, also $f_1=2(x_1+2x_2)^2+(11-8)\,x_2^2=2(x_1+2x_2)^2+3x_2^2$. Beide Faktoren positiv: eine Schüssel.

</li>

<li>

$f_2=(x_1+2x_2)^2+0\cdot x_2^2$: eine Rinne. Sie ist null auf der Geraden $x_1+2x_2=0$, also in Richtung $(2,\,-1)^{\top}$.

</li>

<li>

$f_3=(x_1+2x_2)^2-3x_2^2$: verschiedene Vorzeichen, ein Sattel. Wählt man $x_2=1$ und $x_1=-2$, verschwindet das erste Quadrat: $f_3(-2,\,1)=4-8+1=-3<0$.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 16 ★★ Gekoppelte Spulen
<span class="anker" id="aufg-16"></span>

Zwei gekoppelte Spulen haben $L_1=4\,\mathrm{mH}$ und $L_2=1\,\mathrm{mH}$.

<ol class="al">

<li>

Ergänze die Energie $W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2$ quadratisch.

</li>

<li>

Für welche Werte von $M$ ist $W>0$ für alle Ströme $(i_1,\,i_2)\ne(0,\,0)$? Was folgt daraus für den Kopplungsfaktor $k=M/\sqrt{L_1L_2}$?

</li>

</ol>

:::loesung
(a) In [(5.3)](#gl-5-3) ist $a=\tfrac12L_1$, $2b=M$ und $c=\tfrac12L_2$, also $b/a=M/L_1$ und $b^2/a=M^2/(2L_1)$:

$$W=\tfrac12L_1\Bigl(i_1+\frac M{L_1}\,i_2\Bigr)^2+\tfrac12\Bigl(L_2-\frac{M^2}{L_1}\Bigr)i_2^2=2\,\mathrm{mH}\,\Bigl(i_1+\frac M{4\,\mathrm{mH}}\,i_2\Bigr)^2+\Bigl(\frac12\,\mathrm{mH}-\frac{M^2}{8\,\mathrm{mH}}\Bigr)i_2^2 .$$

(b) Der erste Faktor ist positiv. $W>0$ für alle Ströme $\ne(0,\,0)$ gilt genau dann, wenn auch der zweite positiv ist: $L_2-M^2/L_1>0$, also $M^2<L_1L_2=4\,(\mathrm{mH})^2$ und $|M|<2\,\mathrm{mH}$. Für den Kopplungsfaktor heißt das $|k|=|M|/\sqrt{L_1L_2}<1$. Bei $|k|=1$, der idealen festen Kopplung, wäre die Form nur eine Rinne: Für das passende Stromverhältnis $i_1=-\tfrac M{L_1}\,i_2$ wäre die gespeicherte Energie null. Dass die Energie eines Magnetfelds nie negativ ist, erzwingt also $|k|\le1$.
:::
:::
