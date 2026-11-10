---
title: Eigenwerte und Eigenvektoren
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Kapitel 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15220700
summary: Eine Matrix dreht und streckt die meisten Vektoren zugleich.
tags: konjugiert komplexe, Eigenvektor, Eigenwert, charakteristische Polynom, Eigenraum, Spur, algebraische Vielfachheit, geometrische Vielfachheit
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine Matrix dreht und streckt die meisten Vektoren zugleich. Manche Richtungen aber dreht sie nicht: Ein Pfeil in dieser Richtung wird nur länger, kürzer oder umgeklappt. Dieser Abschnitt findet diese Richtungen und die Streckfaktoren, die zu ihnen gehören. Sie sind die natürlichen Achsen einer Matrix.
:::

:::::vorwissen Was du dafür brauchst: komplexe Zahlen

<span class="anker" id="stufe-6-1"></span>

Bei der Suche nach Streckfaktoren entstehen Polynomgleichungen, und nicht jede hat reelle Lösungen. Dieser Unterabschnitt stellt zusammen, was dieses Kapitel über komplexe Zahlen benutzt.

**Komplexe Zahlen.** Eine komplexe Zahl $z=x+\mathrm j\,y$ besteht aus dem Realteil $x$ und dem Imaginärteil $y$, zwei reellen Zahlen. Für die imaginäre Einheit gilt $\mathrm j^2=-1$. Viele Mathematikbücher nennen sie $\mathrm i$; dieses Kapitel schreibt wie Python ein aufrechtes $\mathrm j$, denn Python schreibt die Zahl $3+4\,\mathrm j$ als `3+4j`, und $i$ bleibt als Index frei.

**Konjugieren und Betrag.** Die zu $z$ __konjugiert komplexe__ Zahl ist $z^*=x-\mathrm j\,y$. Es ist $z\,z^*=x^2+y^2=|z|^2$, das Quadrat des Betrags, eine reelle Zahl, die nur für $z=0$ null ist. Eine Zahl ist genau dann reell, wenn $z=z^*$ ist. Konjugieren verträgt sich mit Summe und Produkt: $(z+w)^*=z^*+w^*$ und $(zw)^*=z^*w^*$. Für einen Vektor $\mathbf{v}$ mit komplexen Komponenten bezeichnet $\mathbf{v}^*$ in diesem Kapitel den Vektor der konjugierten Komponenten, nicht transponiert. Dann ist

$$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0\qquad\text{für }\mathbf{v}\ne\mathbf{0} .$$

**Die Eulersche Formel.** Für jede reelle Zahl $\alpha$ ist $\mathrm e^{\mathrm j\alpha}=\cos\alpha+\mathrm j\sin\alpha$, ein Punkt auf dem Einheitskreis der komplexen Ebene mit dem Betrag $1$.

**Nullstellen von Polynomen.** Jedes Polynom vom Grad $n\ge1$ mit reellen oder komplexen Koeffizienten hat genau $n$ komplexe Nullstellen, wenn man mehrfache Nullstellen mehrfach zählt, und zerfällt in $n$ Linearfaktoren. Hat das Polynom reelle Koeffizienten, so ist mit $z$ auch $z^*$ eine Nullstelle: Nicht reelle Nullstellen kommen in Paaren.

::::beispiel [Rechenbeispiel]
$\lambda^2-1{,}2\lambda+1=0$ hat nach der Lösungsformel die Nullstellen $\lambda=0{,}6\pm\sqrt{0{,}36-1}=0{,}6\pm\mathrm j\,0{,}8$, ein konjugiertes Paar mit dem Betrag $\sqrt{0{,}36+0{,}64}=1$. Für $\mathbf{v}=(1,\,-\mathrm j)^{\top}$ ist $\mathbf{v}^*=(1,\,\mathrm j)^{\top}$ und $(\mathbf{v}^*)^{\top}\mathbf{v}=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2$ (Abb. [16](#abb-16)).

:::abbildung ml/k2rkomplex 16
Das Skalarprodukt $(\mathbf{v}^*)^{\top}\mathbf{v}$ für $\mathbf{v}=(1,-\mathrm j)^{\top}$: Jedes Glied ist $v_i^*v_i=|v_i|^2$, denn $\mathrm j\cdot(-\mathrm j)=-\mathrm j^2=1$.
:::
::::

⁠**Kurz gesagt:** Komplexe Zahlen $x+\mathrm jy$ mit $\mathrm j^2=-1$ lösen jede Polynomgleichung; Konjugieren wechselt das Vorzeichen des Imaginärteils, und $zz^*=|z|^2$ ist reell.

:::::

### Eigenvektoren und Eigenwerte

<span class="anker" id="stufe-6-2"></span>

In [Kapitel 1, Abschnitt 8.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3), wurde das Gitter der Ebene von Matrizen gedreht, gestreckt und geschert. Dabei ändern die meisten Pfeile ihre Richtung. Bei manchen Matrizen gibt es aber Richtungen, in denen ein Pfeil auf seiner Geraden durch den Nullpunkt bleibt: Er wird nur gestreckt, gestaucht oder umgeklappt (Abb. [17](#abb-17)).

:::abbildung ml/k2eigen 17
Die Matrix $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ bildet den Einheitskreis (grau) auf eine Ellipse ab (blau). Der Pfeil $\mathbf{v}_1=(1,1)^{\top}/\sqrt2$ (rot) bleibt auf seiner Geraden und wird auf das Fünffache gestreckt, der Pfeil $\mathbf{v}_2=(1,-2)^{\top}/\sqrt5$ (grün) auf das Doppelte; ihre Bilder sind hell gezeichnet. Die grauen Geraden sind die beiden Eigenrichtungen. Der Einheitsvektor $\mathbf{e}_1$ dagegen wird auf $(4,2)^{\top}$ abgebildet (gestrichelt) und ändert seine Richtung.
:::

:::definition Definition 6.1 (Eigenvektor, Eigenwert)
<span class="anker" id="satz-6-1"></span>

Es sei $\mathbf{A}\in\mathbb{R}^{n\times n}$. Ein Vektor $\mathbf{v}\ne\mathbf{0}$ heißt __Eigenvektor__ von $\mathbf{A}$, wenn es eine Zahl $\lambda$ gibt mit

<span class="anker" id="gl-6-1"></span>
$$\mathbf{A}\mathbf{v}=\lambda\,\mathbf{v} . \tag{6.1}$$

Die Zahl $\lambda$ heißt der zugehörige __Eigenwert__.
:::

Der Nullvektor ist ausgeschlossen, weil $\mathbf{A}\mathbf{0}=\lambda\mathbf{0}$ für jede Zahl $\lambda$ gilt und nichts verrät. Der Eigenwert darf dagegen null sein: Dann wird der Eigenvektor auf $\mathbf{0}$ abgebildet. Ein negativer Eigenwert klappt den Pfeil um. Eigenwerte heißen in diesem Kapitel $\lambda$ oder $\lambda_i$. Das Wort stammt aus dem Deutschen und wird auch im Englischen benutzt: *eigenvalue*, *eigenvector*.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ ist

$$\mathbf{A}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.$$

Also ist $(1,\,1)^{\top}$ ein Eigenvektor zum Eigenwert $5$ und $(1,\,-2)^{\top}$ einer zum Eigenwert $2$. Der Vektor $(1,\,0)^{\top}$ ist keiner, denn $(4,\,2)^{\top}$ ist kein Vielfaches von ihm.
::::

⁠**Kurz gesagt:** Ein Eigenvektor wird von der Matrix nicht gedreht, nur mit einer Zahl multipliziert; diese Zahl ist der Eigenwert.

:::hintergrund Dieselbe Idee für unendlich lange Folgen: der Zinseszins
Ein Guthaben von $100$ Euro wächst mit $5$ % Zinsen im Jahr auf $100$, $105$, $110{,}25$, … Euro, allgemein auf $a_n=100\cdot1{,}05^n$ nach $n$ Jahren. Die Vorschrift „jeden Wert durch den des folgenden Jahres ersetzen“ macht aus einer Folge $(a_0,a_1,a_2,\dots)$ die Folge $(a_1,a_2,a_3,\dots)$. Sie ist linear: Verschiebt man die Summe zweier Folgen, erhält man die Summe der verschobenen Folgen, und ebenso bei Vielfachen. Für das Guthaben liefert sie

$$(105;\ 110{,}25;\ \dots)=1{,}05\cdot(100;\ 105;\ \dots) .$$

Die Form der Folge bleibt erhalten, nur eine Zahl kommt hinzu: Die Folge $a_n=100\cdot1{,}05^n$ ist ein Eigenvektor des Verschiebens, und der Eigenwert ist der Zinsfaktor $1{,}05$. Gleichung [(6.1)](#gl-6-1) sagt für eine Matrix dasselbe. Es gibt auch keine anderen Eigenvektoren des Verschiebens als solche Folgen: Aus $a_{n+1}=\lambda\,a_n$ für alle $n$ folgt $a_n=a_0\,\lambda^n$. In beiden Fällen, bei Folgen wie bei Vektoren, gibt es Dinge, die die lineare Vorschrift nur mit einer Zahl multipliziert.
:::

### Das charakteristische Polynom

<span class="anker" id="stufe-6-3"></span>

Wie findet man Eigenwerte, ohne zu raten? Man schreibt [(6.1)](#gl-6-1) so um, dass alles auf einer Seite steht: $\mathbf{A}\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}$, also $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. Gesucht ist ein $\lambda$, für das dieses homogene System eine Lösung $\mathbf{v}\ne\mathbf{0}$ hat. Nach [Kapitel 1, Abschnitt 11.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-5), heißt das: Die Matrix $\mathbf{A}-\lambda\mathbf{I}$ ist nicht invertierbar. Nach [Kapitel 1, Abschnitt 14.6](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-6), ist das genau dann der Fall, wenn ihre Determinante null ist.

:::definition Definition 6.2 (Charakteristisches Polynom)
<span class="anker" id="satz-6-2"></span>

Für $\mathbf{A}\in\mathbb{R}^{n\times n}$ heißt

<span class="anker" id="gl-6-2"></span>
$$p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I}) \tag{6.2}$$

das __charakteristische Polynom__ von $\mathbf{A}$.
:::

:::satz Satz 6.3 (Eigenwerte sind Nullstellen)
<span class="anker" id="satz-6-3"></span>

Eine Zahl $\lambda$ ist genau dann ein Eigenwert von $\mathbf{A}$, wenn $p(\lambda)=0$ ist.
:::

Das charakteristische Polynom hat den Grad $n$. Für eine $2\times2$-Matrix ist es

<span class="anker" id="gl-6-3"></span>
$$\det\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}=(a-\lambda)(d-\lambda)-bc=\lambda^2-(a+d)\,\lambda+(ad-bc) . \tag{6.3}$$

Nach dem Unterabschnitt über komplexe Zahlen hat es, mit Vielfachheit gezählt, genau $n$ komplexe Nullstellen. Eine $n\times n$-Matrix hat also $n$ Eigenwerte, wenn man komplexe zulässt und mehrfache mehrfach zählt.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ ist $p(\lambda)=\lambda^2-7\lambda+(12-2)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. Die Eigenwerte sind $5$ und $2$, wie im vorigen Unterabschnitt. Für die Diagonalmatrix $\operatorname{diag}(3;\,-1)$ ist $p(\lambda)=(3-\lambda)(-1-\lambda)$ mit den Nullstellen $3$ und $-1$: Die Eigenwerte einer Diagonalmatrix stehen auf ihrer Diagonale, die Eigenvektoren sind die Einheitsvektoren.
::::

⁠**Kurz gesagt:** Die Eigenwerte sind die Nullstellen des charakteristischen Polynoms $\det(\mathbf{A}-\lambda\mathbf{I})$; eine $n\times n$-Matrix hat, mit Vielfachheit und komplex gezählt, $n$ Eigenwerte.

### Eigenvektoren berechnen

<span class="anker" id="stufe-6-4"></span>

Ist ein Eigenwert $\lambda$ bekannt, sind die zugehörigen Eigenvektoren die Lösungen $\mathbf{v}\ne\mathbf{0}$ des homogenen Systems $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. Man findet sie mit dem Gauß-Verfahren. Mit $\mathbf{v}$ ist auch jedes Vielfache $c\,\mathbf{v}$ mit $c\ne0$ ein Eigenvektor, denn $\mathbf{A}(c\mathbf{v})=c\lambda\mathbf{v}=\lambda(c\mathbf{v})$. Ein Eigenvektor ist also nie eindeutig, nur seine Richtung ist es, und manchmal nicht einmal die.

:::definition Definition 6.4 (Eigenraum)
<span class="anker" id="satz-6-4"></span>

Der Kern von $\mathbf{A}-\lambda\mathbf{I}$ heißt der __Eigenraum__ von $\mathbf{A}$ zum Eigenwert $\lambda$.
:::

Er enthält alle Eigenvektoren zu $\lambda$ und den Nullvektor. Als Kern ist er ein Unterraum im Sinn von Abschnitt [4.1](projektion-auf-einen-unterraum.html#stufe-4-1).

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ und $\lambda=5$ ist

$$\mathbf{A}-5\mathbf{I}=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}.$$

Beide Zeilen verlangen dasselbe: $-v_1+v_2=0$. Der Eigenraum ist die Gerade aller Vielfachen von $(1,\,1)^{\top}$. Für $\lambda=2$ ist $\mathbf{A}-2\mathbf{I}=\bigl(\begin{smallmatrix}2&1\\2&1\end{smallmatrix}\bigr)$ mit der Bedingung $2v_1+v_2=0$, der Eigenraum ist die Gerade in Richtung $(1,\,-2)^{\top}$. Normiert sind die Eigenvektoren $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ und $\mathbf{v}_2=(1,\,-2)^{\top}/\sqrt5$, wie in Abb. [17](#abb-17). Sie stehen nicht senkrecht aufeinander: $(1,\,1)(1,\,-2)^{\top}=-1\ne0$.
::::

⁠**Kurz gesagt:** Die Eigenvektoren zu $\lambda$ sind die Lösungen $\mathbf{v}\ne\mathbf{0}$ von $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$; zusammen mit dem Nullvektor bilden sie den Eigenraum.

### Spur und Determinante

<span class="anker" id="stufe-6-5"></span>

In [(6.3)](#gl-6-3) stehen zwei Zahlen, die man der Matrix direkt ansieht: $ad-bc$ ist die Determinante, und $a+d$ ist die Summe der Diagonaleinträge. Diese Summe hat einen eigenen Namen. Beide Zahlen hängen auf einfache Weise mit den Eigenwerten zusammen und taugen deshalb als Probe.

:::definition Definition 6.5 (Spur)
<span class="anker" id="satz-6-5"></span>

Die __Spur__ einer quadratischen Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ ist die Summe ihrer Diagonaleinträge:

<span class="anker" id="gl-6-4"></span>
$$\operatorname{spur}\mathbf{A}=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^na_{ii} . \tag{6.4}$$
:::

:::satz Satz 6.6 (Spur und Determinante aus den Eigenwerten)
<span class="anker" id="satz-6-6"></span>

Sind $\lambda_1,\dots,\lambda_n$ die Eigenwerte von $\mathbf{A}$, mit Vielfachheit und komplex gezählt, so ist

<span class="anker" id="gl-6-5"></span>
$$\operatorname{spur}\mathbf{A}=\lambda_1+\lambda_2+\dots+\lambda_n,\qquad \det\mathbf{A}=\lambda_1\cdot\lambda_2\cdots\lambda_n . \tag{6.5}$$

Außerdem ist $\operatorname{spur}(\mathbf{A}\mathbf{B})=\operatorname{spur}(\mathbf{B}\mathbf{A})$ für $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{B}\in\mathbb{R}^{n\times m}$.
:::

:::herleitung Spur und Determinante
Für $n=2$: Das Polynom $\lambda^2-(a+d)\lambda+(ad-bc)$ zerfällt in $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$. Vergleicht man die Koeffizienten, folgt $a+d=\lambda_1+\lambda_2$ und $ad-bc=\lambda_1\lambda_2$.

Für beliebiges $n$ zerfällt $p(\lambda)$ ebenso in $(\lambda_1-\lambda)(\lambda_2-\lambda)\cdots(\lambda_n-\lambda)$; das Vorzeichen stimmt, weil in $\det(\mathbf{A}-\lambda\mathbf{I})$ der Summand $(-\lambda)^n$ vorkommt. Setzt man $\lambda=0$, steht links $\det\mathbf{A}$ und rechts $\lambda_1\cdots\lambda_n$. Für die Spur vergleicht man die Koeffizienten von $\lambda^{n-1}$. Rechts sind sie $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$. Links liefert in der Laplace-Entwicklung nur das Produkt der Diagonaleinträge $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$ eine so hohe Potenz von $\lambda$, mit dem Koeffizienten $(-1)^{n-1}(a_{11}+\dots+a_{nn})$.

Für die letzte Aussage: $\operatorname{spur}(\mathbf{A}\mathbf{B})=\sum_i(\mathbf{A}\mathbf{B})_{ii}=\sum_i\sum_la_{il}b_{li}$ und $\operatorname{spur}(\mathbf{B}\mathbf{A})=\sum_l\sum_ib_{li}a_{il}$. Das ist dieselbe Doppelsumme, nur anders geordnet.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ ist $\operatorname{spur}\mathbf{A}=7=5+2$ (Abb. [18](#abb-18)) und $\det\mathbf{A}=10=5\cdot2$. Für $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ ist $\operatorname{spur}=7$ und $\det=6$; die Eigenwerte sind also die Lösungen von $\lambda^2-7\lambda+6=0$, nämlich $6$ und $1$. Für $\mathbf{A}\in\mathbb{R}^{2\times3}$ mit den Zeilen $(1,0,2)$, $(0,1,1)$ und $\mathbf{B}=\mathbf{A}^{\top}$ ist $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ mit der Spur $7$ und $\mathbf{B}\mathbf{A}$ eine $3\times3$-Matrix mit den Diagonaleinträgen $1$, $1$ und $5$, ebenfalls mit der Spur $7$.

:::abbildung ml/k2rspur 18
Die Spur von $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ als Summe der Diagonaleinträge; sie ist gleich der Summe der Eigenwerte $5$ und $2$.
:::
::::

⁠**Kurz gesagt:** Die Spur ist die Summe der Diagonaleinträge und die Summe der Eigenwerte, die Determinante das Produkt der Eigenwerte.

### Komplexe Eigenwerte

<span class="anker" id="stufe-6-6"></span>

Eine Drehung um $90^\circ$ lässt keinen Pfeil auf seiner Geraden: Jeder wird um einen rechten Winkel weitergedreht. Sie kann also keinen reellen Eigenvektor haben. Das charakteristische Polynom zeigt, was stattdessen geschieht.

::::beispiel [Rechenbeispiel 1]
Für die Drehung $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ ist $p(\lambda)=\lambda^2+1$ mit den Nullstellen $\lambda=\mathrm j$ und $\lambda=-\mathrm j$. Die Eigenwerte sind rein imaginär. Zu $\lambda=\mathrm j$ gehört der komplexe Eigenvektor $(1,\,-\mathrm j)^{\top}$, denn $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)(1,\,-\mathrm j)^{\top}=(\mathrm j,\,1)^{\top}=\mathrm j\,(1,\,-\mathrm j)^{\top}$.
::::

::::beispiel [Rechenbeispiel 2]
Die Drehung $\mathbf{Q}=\bigl(\begin{smallmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{smallmatrix}\bigr)$ aus Abschnitt [1.4](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-4) hat $p(\lambda)=\lambda^2-1{,}2\lambda+1$ und nach dem Rechenbeispiel zu den komplexen Zahlen die Eigenwerte $0{,}6\pm\mathrm j\,0{,}8=\cos\alpha\pm\mathrm j\sin\alpha=\mathrm e^{\pm\mathrm j\alpha}$ mit $\alpha\approx53{,}13^\circ$. Allgemein hat die Drehung um den Winkel $\alpha$ die Eigenwerte $\mathrm e^{\pm\mathrm j\alpha}$.
::::

Eine reelle Matrix kann also komplexe Eigenwerte haben. Weil ihr charakteristisches Polynom reelle Koeffizienten hat, treten sie in konjugierten Paaren auf. Ein reeller Eigenvektor gehört nur zu einem reellen Eigenwert: Wäre $\mathbf{v}$ reell und $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, so wäre $\lambda\mathbf{v}$ als Bild eines reellen Vektors reell, also auch $\lambda$. Komplexe Eigenwerte zeigen an, dass die Matrix in einer Ebene dreht.

⁠**Kurz gesagt:** Eine reelle Matrix kann komplexe Eigenwerte haben, immer in konjugierten Paaren; eine Drehung um $\alpha$ hat die Eigenwerte $\mathrm e^{\pm\mathrm j\alpha}$.

:::hintergrund Drehen heißt mit $\mathrm e^{\mathrm j\alpha}$ multiplizieren
Mit komplexen Zahlen sieht man das Ergebnis direkt. Man identifiziert den Pfeil $(x_1,\,x_2)^{\top}$ mit der komplexen Zahl $z=x_1+\mathrm jx_2$, also mit einem Punkt der Zahlenebene. Eine Drehung um $\alpha$ ist dann die Multiplikation mit $\mathrm e^{\mathrm j\alpha}$: $\mathrm e^{\mathrm j\alpha}z=(x_1\cos\alpha-x_2\sin\alpha)+\mathrm j\,(x_1\sin\alpha+x_2\cos\alpha)$, und das sind genau die beiden Komponenten von $\mathbf{Q}\mathbf{x}$ für die Drehmatrix aus [Kapitel 1, Abschnitt 8.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3). In der komplexen Schreibweise ist die Drehung also eine Multiplikation mit einer Zahl, und diese Zahl ist ein Eigenwert. Der zweite Eigenwert $\mathrm e^{-\mathrm j\alpha}$ gehört zur konjugierten Schreibweise $z^*$, die sich in die Gegenrichtung dreht.
:::

### Mehrfache Eigenwerte

<span class="anker" id="stufe-6-7"></span>

Das charakteristische Polynom kann eine doppelte Nullstelle haben. Dann fallen zwei der $n$ Eigenwerte zusammen. Wie oft ein Eigenwert vorkommt, ist eine eigene Zahl.

:::definition Definition 6.7 (Algebraische Vielfachheit)
<span class="anker" id="satz-6-7"></span>

Die __algebraische Vielfachheit__ eines Eigenwerts $\lambda$ ist die Vielfachheit von $\lambda$ als Nullstelle des charakteristischen Polynoms.
:::

::::beispiel [Rechenbeispiel]
Die Matrix $2\mathbf{I}=\operatorname{diag}(2;\,2)$ hat $p(\lambda)=(2-\lambda)^2$: Der Eigenwert $2$ hat die algebraische Vielfachheit $2$. Die Scherung $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ aus [Kapitel 1, Abschnitt 8.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3), hat $p(\lambda)=(1-\lambda)^2$: Der Eigenwert $1$ hat ebenfalls die algebraische Vielfachheit $2$. Die Matrix $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ hat zwei verschiedene Eigenwerte, jeder mit der algebraischen Vielfachheit $1$.
::::

⁠**Kurz gesagt:** Die algebraische Vielfachheit zählt, wie oft ein Eigenwert als Nullstelle des charakteristischen Polynoms vorkommt.

### Wie viele Eigenvektoren es gibt

<span class="anker" id="stufe-6-8"></span>

Die beiden Beispiele mit einem doppelten Eigenwert verhalten sich ganz verschieden. Die Matrix $2\mathbf{I}$ streckt jeden Pfeil auf das Doppelte; jeder Vektor $\ne\mathbf{0}$ ist ein Eigenvektor, der Eigenraum ist die ganze Ebene. Die Scherung schiebt jeden Punkt um seine Höhe nach rechts; nur Pfeile auf der $x_1$-Achse bleiben auf ihrer Geraden. Ihr Eigenraum ist $\ker\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, die Gerade in Richtung $(1,\,0)^{\top}$. Der Unterschied ist die Dimension des Eigenraums.

:::definition Definition 6.8 (Geometrische Vielfachheit)
<span class="anker" id="satz-6-8"></span>

Die __geometrische Vielfachheit__ eines Eigenwerts ist die Dimension seines Eigenraums.
:::

Sie ist mindestens $1$, denn zu jedem Eigenwert gibt es einen Eigenvektor, und höchstens so groß wie die algebraische Vielfachheit; diesen zweiten Teil beweist das Kapitel nicht. Bei $2\mathbf{I}$ sind beide Vielfachheiten $2$, bei der Scherung ist die algebraische $2$ und die geometrische $1$: Ihr fehlt ein Eigenvektor.

:::satz Satz 6.9 (Verschiedene Eigenwerte, unabhängige Eigenvektoren)
<span class="anker" id="satz-6-9"></span>

Eigenvektoren $\mathbf{v}_1,\dots,\mathbf{v}_k$ zu paarweise verschiedenen Eigenwerten $\lambda_1,\dots,\lambda_k$ sind linear unabhängig. Hat eine $n\times n$-Matrix $n$ verschiedene Eigenwerte, so bilden ihre Eigenvektoren eine Basis.
:::

:::beweis Unabhängige Eigenvektoren
Für zwei Eigenvektoren: Es sei $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$. Wendet man $\mathbf{A}$ an, folgt $c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2=\mathbf{0}$. Zieht man davon das $\lambda_2$-Fache der ersten Gleichung ab, bleibt $c_1(\lambda_1-\lambda_2)\mathbf{v}_1=\mathbf{0}$. Wegen $\lambda_1\ne\lambda_2$ und $\mathbf{v}_1\ne\mathbf{0}$ ist $c_1=0$, und dann auch $c_2=0$. Für mehr Eigenvektoren geht man ebenso vor: Gäbe es eine Abhängigkeit, so nehme man eine mit möglichst wenigen Koeffizienten ungleich null. Anwenden von $\mathbf{A}$ und Abziehen des $\lambda$-Fachen eines dieser Eigenwerte ergäbe eine Abhängigkeit mit noch weniger Koeffizienten ungleich null, ein Widerspruch.
:::

::::beispiel [Rechenbeispiel]
Die Eigenvektoren $(1,\,1)^{\top}$ und $(1,\,-2)^{\top}$ von $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ gehören zu den verschiedenen Eigenwerten $5$ und $2$; sie sind linear unabhängig, denn $\det\bigl(\begin{smallmatrix}1&1\\1&-2\end{smallmatrix}\bigr)=-3\ne0$. Die Scherung hat dagegen nur die Eigenrichtung $(1,\,0)^{\top}$; zwei unabhängige Eigenvektoren gibt es nicht.
::::

⁠**Kurz gesagt:** Die geometrische Vielfachheit zählt die unabhängigen Eigenvektoren zu einem Eigenwert; sie kann kleiner sein als die algebraische, aber verschiedene Eigenwerte haben immer unabhängige Eigenvektoren.

### Rechenregeln für Eigenwerte

<span class="anker" id="stufe-6-9"></span>

Wer die Eigenvektoren einer Matrix kennt, kennt sie auch für viele daraus gebaute Matrizen. Die Regeln folgen alle direkt aus [(6.1)](#gl-6-1).

:::satz Satz 6.10 (Rechenregeln)
<span class="anker" id="satz-6-10"></span>

Es sei $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ mit $\mathbf{v}\ne\mathbf{0}$. Dann gilt:

<ol class="rm">

<li>

$\mathbf{A}^k\mathbf{v}=\lambda^k\mathbf{v}$ für jede natürliche Zahl $k$;

</li>

<li>

$(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=(\lambda+\beta)\mathbf{v}$ für jede Zahl $\beta$;

</li>

<li>

$\mathbf{A}$ ist genau dann invertierbar, wenn kein Eigenwert null ist, und dann ist $\mathbf{A}^{-1}\mathbf{v}=\frac1\lambda\mathbf{v}$;

</li>

<li>

$\mathbf{A}^{\top}$ hat dieselben Eigenwerte wie $\mathbf{A}$, im Allgemeinen aber andere Eigenvektoren.

</li>

</ol>
:::

:::beweis Rechenregeln
(i) $\mathbf{A}^2\mathbf{v}=\mathbf{A}(\lambda\mathbf{v})=\lambda\mathbf{A}\mathbf{v}=\lambda^2\mathbf{v}$, und so weiter. (ii) $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=\lambda\mathbf{v}+\beta\mathbf{v}$. (iii) Nach [(6.5)](#gl-6-5) ist $\det\mathbf{A}$ das Produkt der Eigenwerte, also genau dann ungleich null, wenn kein Eigenwert null ist. Multipliziert man $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ mit $\mathbf{A}^{-1}$, folgt $\mathbf{v}=\lambda\mathbf{A}^{-1}\mathbf{v}$. (iv) Nach [Kapitel 1, Abschnitt 14.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), ist $\det(\mathbf{A}^{\top}-\lambda\mathbf{I})=\det\bigl((\mathbf{A}-\lambda\mathbf{I})^{\top}\bigr)=\det(\mathbf{A}-\lambda\mathbf{I})$; beide haben dasselbe charakteristische Polynom.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ hat $\mathbf{A}^2=\bigl(\begin{smallmatrix}18&7\\14&11\end{smallmatrix}\bigr)$ die Eigenwerte $25$ und $4$: $\mathbf{A}^2(1,\,1)^{\top}=(25,\,25)^{\top}$. Die Matrix $\mathbf{A}-5\mathbf{I}$ hat die Eigenwerte $0$ und $-3$ und ist nicht invertierbar. Die Inverse $\mathbf{A}^{-1}=\tfrac1{10}\bigl(\begin{smallmatrix}3&-1\\-2&4\end{smallmatrix}\bigr)$ hat die Eigenwerte $\tfrac15$ und $\tfrac12$: $\mathbf{A}^{-1}(1,\,-2)^{\top}=\tfrac1{10}(5,\,-10)^{\top}=\tfrac12(1,\,-2)^{\top}$. Die Transponierte $\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&2\\1&3\end{smallmatrix}\bigr)$ hat ebenfalls die Eigenwerte $5$ und $2$, aber $\mathbf{A}^{\top}(1,\,1)^{\top}=(6,\,4)^{\top}$: Ihre Eigenvektoren sind $(2,\,1)^{\top}$ und $(1,\,-1)^{\top}$.
::::

⁠**Kurz gesagt:** Potenzen, Verschiebungen um $\beta\mathbf{I}$ und die Inverse behalten die Eigenvektoren und verändern die Eigenwerte auf dieselbe Weise; die Transponierte behält nur die Eigenwerte.

:::aufgabe Aufgabe 17 ★ Eigenwerte und Eigenvektoren
<span class="anker" id="aufg-17"></span>

Bestimme Eigenwerte und Eigenräume von

$$\mathbf{A}_1=\begin{pmatrix}2&2\\1&3\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&1\end{pmatrix}.$$

Prüfe jeweils Spur und Determinante. Bei welcher Matrix stehen die Eigenvektoren senkrecht aufeinander?

:::loesung
$\mathbf{A}_1$: Spur $5$, Determinante $6-2=4$, also $\lambda^2-5\lambda+4=(\lambda-4)(\lambda-1)$. Zu $\lambda=4$: $\mathbf{A}_1-4\mathbf{I}=\bigl(\begin{smallmatrix}-2&2\\1&-1\end{smallmatrix}\bigr)$, Eigenraum in Richtung $(1,\,1)^{\top}$. Zu $\lambda=1$: $\mathbf{A}_1-\mathbf{I}=\bigl(\begin{smallmatrix}1&2\\1&2\end{smallmatrix}\bigr)$, Eigenraum in Richtung $(2,\,-1)^{\top}$. Probe: $4+1=5$, $4\cdot1=4$. Die Eigenvektoren stehen nicht senkrecht: $(1,\,1)(2,\,-1)^{\top}=1$.

$\mathbf{A}_2=3\mathbf{I}$: $p(\lambda)=(3-\lambda)^2$, der Eigenwert $3$ doppelt; der Eigenraum ist die ganze Ebene. Probe: $3+3=6$, $3\cdot3=9$. Man kann zwei senkrechte Eigenvektoren wählen, etwa $\mathbf{e}_1$ und $\mathbf{e}_2$, aber auch zwei schräge.

$\mathbf{A}_3$: Spur $2$, Determinante $1-9=-8$, also $\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$. Eigenvektoren $(1,\,1)^{\top}$ zu $4$ und $(1,\,-1)^{\top}$ zu $-2$. Probe: $4-2=2$, $4\cdot(-2)=-8$. Sie stehen senkrecht aufeinander; $\mathbf{A}_3$ ist symmetrisch, und Abschnitt [7.5](diagonalisierung-und-spektralsatz.html#stufe-7-5) zeigt, dass das kein Zufall ist.
:::
:::

:::aufgabe Aufgabe 18 ★ Dreiecksmatrizen
<span class="anker" id="aufg-18"></span>

Zeige: Die Eigenwerte einer oberen Dreiecksmatrix sind ihre Diagonaleinträge. Bestimme Eigenwerte und Eigenvektoren von $\Bigl(\begin{smallmatrix}2&1&0\\0&3&1\\0&0&5\end{smallmatrix}\Bigr)$.

:::loesung
Für eine obere Dreiecksmatrix ist $\mathbf{A}-\lambda\mathbf{I}$ wieder eine obere Dreiecksmatrix mit den Diagonaleinträgen $a_{ii}-\lambda$. Nach [Kapitel 1, Abschnitt 14.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-4), ist ihre Determinante das Produkt der Diagonaleinträge: $p(\lambda)=(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$. Die Nullstellen sind die Diagonaleinträge.

Für die gegebene Matrix sind die Eigenwerte also $2$, $3$ und $5$. Zu $2$: $\mathbf{A}-2\mathbf{I}=\Bigl(\begin{smallmatrix}0&1&0\\0&1&1\\0&0&3\end{smallmatrix}\Bigr)$ verlangt $v_3=0$ und $v_2=0$, Eigenvektor $(1,\,0,\,0)^{\top}$. Zu $3$: $\Bigl(\begin{smallmatrix}-1&1&0\\0&0&1\\0&0&2\end{smallmatrix}\Bigr)$ verlangt $v_3=0$ und $v_2=v_1$, Eigenvektor $(1,\,1,\,0)^{\top}$. Zu $5$: $\Bigl(\begin{smallmatrix}-3&1&0\\0&-2&1\\0&0&0\end{smallmatrix}\Bigr)$ verlangt $v_2=3v_1$ und $v_3=2v_2$, Eigenvektor $(1,\,3,\,6)^{\top}$. Probe: $\mathbf{A}(1,\,3,\,6)^{\top}=(2+3,\ 9+6,\ 30)^{\top}=5\,(1,\,3,\,6)^{\top}$.
:::
:::

:::aufgabe Aufgabe 19 ★★ Vielfachheiten
<span class="anker" id="aufg-19"></span>

Bestimme für $\mathbf{B}_1=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$, $\mathbf{B}_2=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ und $\mathbf{B}_3=\Bigl(\begin{smallmatrix}1&0&0\\0&1&1\\0&0&1\end{smallmatrix}\Bigr)$ alle Eigenwerte mit ihrer algebraischen und geometrischen Vielfachheit.

:::loesung
$\mathbf{B}_1=2\mathbf{I}$: Eigenwert $2$, algebraische Vielfachheit $2$, Eigenraum die ganze Ebene, geometrische Vielfachheit $2$.

$\mathbf{B}_2$: Dreiecksmatrix, Eigenwert $2$ mit algebraischer Vielfachheit $2$. $\mathbf{B}_2-2\mathbf{I}=\bigl(\begin{smallmatrix}0&3\\0&0\end{smallmatrix}\bigr)$ verlangt $v_2=0$; der Eigenraum ist die $x_1$-Achse, geometrische Vielfachheit $1$. Wie der Scherung fehlt $\mathbf{B}_2$ ein Eigenvektor.

$\mathbf{B}_3$: Dreiecksmatrix, Eigenwert $1$ mit algebraischer Vielfachheit $3$. $\mathbf{B}_3-\mathbf{I}=\Bigl(\begin{smallmatrix}0&0&0\\0&0&1\\0&0&0\end{smallmatrix}\Bigr)$ verlangt nur $v_3=0$; der Eigenraum ist $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$, geometrische Vielfachheit $2$. Hier liegt die geometrische Vielfachheit zwischen $1$ und der algebraischen.
:::
:::

:::aufgabe Aufgabe 20 ★★ Eine Drehung und eine Spiegelung
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

Berechne die Eigenwerte der Drehung um $30^\circ$ und schreibe sie in der Form $\mathrm e^{\pm\mathrm j\alpha}$.

</li>

<li>

Die Spiegelung $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ aus Abschnitt [1.5](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-5) ist ebenfalls orthogonal. Bestimme ihre Eigenwerte und Eigenvektoren und deute sie geometrisch.

</li>

<li>

Zeige: Jeder reelle Eigenwert einer orthogonalen Matrix ist $1$ oder $-1$.

</li>

</ol>

:::loesung
(a) Die Drehung um $30^\circ$ ist $\bigl(\begin{smallmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{smallmatrix}\bigr)$ mit Spur $\sqrt3$ und Determinante $1$. Also $p(\lambda)=\lambda^2-\sqrt3\,\lambda+1$ und

$$\lambda=\frac{\sqrt3\pm\sqrt{3-4}}2=\frac{\sqrt3}2\pm\mathrm j\,\frac12=\cos30^\circ\pm\mathrm j\sin30^\circ=\mathrm e^{\pm\mathrm j\,30^\circ} .$$

(b) Spur $0$, Determinante $-0{,}36-0{,}64=-1$, also $p(\lambda)=\lambda^2-1$ mit den Eigenwerten $1$ und $-1$. Zu $1$: $\bigl(\begin{smallmatrix}-0{,}4&0{,}8\\0{,}8&-1{,}6\end{smallmatrix}\bigr)$, Eigenvektor $(2,\,1)^{\top}$. Zu $-1$: $\bigl(\begin{smallmatrix}1{,}6&0{,}8\\0{,}8&0{,}4\end{smallmatrix}\bigr)$, Eigenvektor $(1,\,-2)^{\top}$. Geometrisch: Die Punkte der Spiegelachse in Richtung $(2,\,1)^{\top}$ bleiben fest, der Eigenwert ist $1$; die Richtung senkrecht dazu wird umgeklappt, der Eigenwert ist $-1$. Die beiden Eigenvektoren stehen senkrecht, denn die Matrix ist symmetrisch.

(c) Es sei $\mathbf{Q}\mathbf{v}=\lambda\mathbf{v}$ mit reellem $\lambda$ und reellem $\mathbf{v}\ne\mathbf{0}$. Nach [(1.3)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-3) ist $\lVert\mathbf{v}\rVert=\lVert\mathbf{Q}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$, also $|\lambda|=1$ und $\lambda=\pm1$. Eine starre Bewegung kann einen Pfeil auf seiner Geraden nur stehen lassen oder umklappen, nicht strecken.
:::
:::
