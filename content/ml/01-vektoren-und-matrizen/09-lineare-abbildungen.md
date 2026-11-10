---
title: Lineare Abbildungen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Kapitel 1: Vektoren und Matrizen
nachschlagen: ja
order: 15210900
summary: Eine Matrix ist nicht nur eine Tabelle, sondern auch eine Rechenvorschrift, die aus einem Vektor einen anderen macht.
tags: Abbildung, linear, Drehung, Streckung, Scherung, affin, Achsenabschnitt
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Eine Matrix ist nicht nur eine Tabelle, sondern auch eine Rechenvorschrift, die aus einem Vektor einen anderen macht. Dieser Abschnitt zeigt, welche Vorschriften sich so schreiben lassen, nämlich genau die linearen, und was eine Matrix geometrisch mit dem Raum macht.
:::

### Lineare Abbildungen

<span class="anker" id="stufe-8-1"></span>

Viele Rechnungen machen aus einer Liste von Zahlen eine andere Liste. Aus den Merkmalen einer Wohnung werden Kaufpreis und Miete geschätzt; aus den Ständen eines Wasserzählers wird der Verbrauch in jedem Monat. Eine solche Vorschrift heißt __Abbildung__ $f\colon\mathbb{R}^n\to\mathbb{R}^m$: Sie ordnet jedem Vektor $\mathbf{x}\in\mathbb{R}^n$ einen Vektor $f(\mathbf{x})\in\mathbb{R}^m$ zu.

Das Matrix-Vektor-Produkt hat zwei besondere Eigenschaften (Unterabschnitt [7.1](das-matrix-vektor-produkt.html#stufe-7-1)): $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ und $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$. Es ist gleichgültig, ob man zuerst addiert oder zuerst abbildet, und ebenso, ob man zuerst vervielfacht oder zuerst abbildet. In der Ebene sieht man diese Eigenschaften an einem Gitter: Eine solche Abbildung macht aus Geraden wieder Geraden oder einzelne Punkte, lässt den Nullpunkt an seinem Platz und macht aus parallelen, gleichabständigen Gitterlinien wieder parallele, gleichabständige Linien oder Punkte.

:::definition Definition 8.1 (Lineare Abbildung)
<span class="anker" id="satz-8-1"></span>

Eine Abbildung $f\colon\mathbb{R}^n\to\mathbb{R}^m$ heißt __linear__, wenn für alle $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ und alle Skalare $c$ gilt:

<span class="anker" id="gl-8-1"></span>
$$f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})\qquad\text{und}\qquad f(c\,\mathbf{u})=c\,f(\mathbf{u}) . \tag{8.1}$$
:::

Beide Bedingungen zusammen besagen: $f$ erhält Linearkombinationen, $f(c_1\mathbf{u}+c_2\mathbf{v})=c_1f(\mathbf{u})+c_2f(\mathbf{v})$. Jede lineare Abbildung bildet den Nullvektor auf den Nullvektor ab, denn $f(\mathbf{0})=f(0\cdot\mathbf{u})=0\cdot f(\mathbf{u})=\mathbf{0}$.

::::beispiel [Rechenbeispiel]
Die Abbildung $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ von $\mathbb{R}^2$ nach $\mathbb{R}^2$ ist linear. Beide Komponenten sind Summen von Vielfachen der $x_j$, und für solche Summen gelten die Bedingungen [(8.1)](#gl-8-1); zum Beispiel ist $f(\mathbf{u}+\mathbf{v})=(u_1+v_1+u_2+v_2,\ 2u_1+2v_1)^{\top}=f(\mathbf{u})+f(\mathbf{v})$. Nicht linear ist $g(\mathbf{x})=x_1x_2$, denn $g(2\mathbf{x})=4x_1x_2\ne2\,g(\mathbf{x})$, sobald $x_1x_2\ne0$. Auch $h(\mathbf{x})=\mathbf{x}+\mathbf 1$ ist nicht linear, denn $h(\mathbf{0})=\mathbf 1\ne\mathbf{0}$.
::::

⁠**Kurz gesagt:** Eine Abbildung ist linear, wenn sie Summen und Vielfache erhält; sie bildet dann Linearkombinationen auf Linearkombinationen ab.

:::hintergrund Linearität an der Supermarktkasse
Die Kasse eines Supermarkts rechnet linear. Sie macht aus der Liste der gekauften Mengen den Betrag, und legt man zwei Einkäufe zusammen aufs Band, kostet das die Summe der beiden Beträge; kauft man von allem das Doppelte, kostet es das Doppelte. Das sind genau die Bedingungen [(8.1)](#gl-8-1). Nicht linear wäre ein Tarif mit Mengenrabatt, bei dem das Doppelte weniger als den doppelten Preis kostet, oder einer mit fester Grundgebühr: Dort kostet der leere Einkauf schon etwas, und das verletzt $f(\mathbf{0})=\mathbf{0}$. Auch eine Tonaufnahme (Unterabschnitt [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)) wird oft linear bearbeitet: Wer zwei Aufnahmen erst mischt und dann leiser macht, erhält dasselbe, wie wenn er jede für sich leiser macht und dann mischt.
:::

### Jede lineare Abbildung ist eine Matrix

<span class="anker" id="stufe-8-2"></span>

Jede Matrix liefert eine lineare Abbildung $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$. Gilt auch die Umkehrung? Ja, und der Grund ist einfach: Jeder Vektor ist eine Linearkombination der Einheitsvektoren, und eine lineare Abbildung erhält Linearkombinationen. Wer weiß, wohin die $n$ Einheitsvektoren gehen, weiß deshalb, wohin jeder Vektor geht.

:::satz Satz 8.2 (Matrix einer linearen Abbildung)
<span class="anker" id="satz-8-2"></span>

Zu jeder linearen Abbildung $f\colon\mathbb{R}^n\to\mathbb{R}^m$ gibt es genau eine Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ mit $f(\mathbf{x})=\mathbf{A}\mathbf{x}$ für alle $\mathbf{x}\in\mathbb{R}^n$. Ihre Spalten sind die Bilder der Einheitsvektoren:

<span class="anker" id="gl-8-2"></span>
$$\mathbf{a}_j=f(\mathbf{e}_j),\qquad j=1,\dots,n . \tag{8.2}$$
:::

:::beweis Matrix einer linearen Abbildung
Nach [(1.6)](vektoren-daten-als-zahlenlisten.html#gl-1-6) ist $\mathbf{x}=\sum_jx_j\mathbf{e}_j$. Weil $f$ linear ist, folgt

$$f(\mathbf{x})=f\Bigl(\sum_{j=1}^nx_j\mathbf{e}_j\Bigr)=\sum_{j=1}^nx_j\,f(\mathbf{e}_j)=\sum_{j=1}^nx_j\,\mathbf{a}_j=\mathbf{A}\mathbf{x} ,$$

der letzte Schritt nach der Spaltensicht [(7.3)](das-matrix-vektor-produkt.html#gl-7-3). Gäbe es eine zweite Matrix $\mathbf{B}$ mit $\mathbf{B}\mathbf{x}=f(\mathbf{x})$ für alle $\mathbf{x}$, so wäre mit $\mathbf{x}=\mathbf{e}_j$ die Spalte $j$ von $\mathbf{B}$ gleich $f(\mathbf{e}_j)=\mathbf{a}_j$, für jedes $j$. Also ist $\mathbf{B}=\mathbf{A}$.
:::

::::beispiel [Rechenbeispiel]
Für $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ ist $f(\mathbf{e}_1)=(1,\,2)^{\top}$ und $f(\mathbf{e}_2)=(1,\,0)^{\top}$. Also ist

$$\mathbf{A}=\begin{pmatrix}1&1\\2&0\end{pmatrix},\qquad\text{und zur Probe}\qquad \mathbf{A}\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2\\6\end{pmatrix}=f\bigl((3,\,-1)^{\top}\bigr).$$
::::

⁠**Kurz gesagt:** Lineare Abbildungen und Matrizen sind dasselbe; die Spalte $j$ der Matrix ist das Bild des Einheitsvektors $\mathbf{e}_j$.

:::hintergrund Eine Nachwirkung als Matrix: Die Spalten sind verschobene Antworten
In einem Kaminofen gibt ein Holzscheit seine Wärme in der Stunde, in der es brennt, voll ab und in der Stunde danach durch die Glut noch zur Hälfte; das ist ein stark vereinfachtes Bild. Legt man in der Stunde $n$ genau $x[n]$ Scheite nach, so ist die Wärme in dieser Stunde, gemessen in Scheiten, $y[n]=x[n]+0{,}5\,x[n-1]$. Betrachtet werden drei Stunden, vor der ersten brannte nichts. Die Rechnung ist linear, also hat sie eine Matrix. Nach [(8.2)](#gl-8-2) ist ihre Spalte $j$ die Antwort auf den Einheitsvektor $\mathbf{e}_j$, also auf ein einzelnes Scheit in der Stunde $j$. Diese Antwort ist $(1;\,0{,}5)$, um $j-1$ Stunden verschoben:

$$\mathbf{A}=\begin{pmatrix}1&0&0\\0{,}5&1&0\\0&0{,}5&1\end{pmatrix}.$$

Die dritte Spalte enthält nur noch die $1$, weil die Betrachtung nach drei Stunden endet. Für $\mathbf{x}=(2,\,4,\,6)^{\top}$ liefert die Matrix $(2,\,5,\,8)^{\top}$, dasselbe wie die Formel. Jede solche Nachwirkung mit festen Gewichten, in der Mathematik eine Faltung genannt, ist auf diese Weise ein Matrix-Vektor-Produkt, und der Satz oben erklärt, warum: Kennt man die Antwort auf jedes einzelne Scheit, kennt man die Antwort auf jede Folge von Scheiten.
:::

:::hintergrund Daten oder Abbildung? Zwei Rollen derselben Tabelle
Eine Matrix kann eine Sammlung von Daten sein, wie die Datenmatrix $\mathbf{X}$, oder eine Abbildung, wie die Matrix des Kaminofens im Kasten davor. Formal ist beides dasselbe, und manchmal hat dieselbe Matrix beide Rollen zugleich: Die Datenmatrix ist auch die Abbildung $\mathbf{w}\mapsto\mathbf{X}\mathbf{w}$, die aus Gewichten Vorhersagen macht. Sie bildet den $\mathbb{R}^d$ der Gewichte in den $\mathbb{R}^N$ der Vorhersagelisten ab. Beim Lesen einer Formel lohnt deshalb die Frage, in welcher Rolle eine Matrix gerade auftritt.
:::

### Lineare Abbildungen der Ebene

<span class="anker" id="stufe-8-3"></span>

In der Ebene kann man sehen, was eine Matrix tut. Man zeichnet das Einheitsquadrat mit den Ecken $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_1+\mathbf{e}_2$ und $\mathbf{e}_2$ und sein Bild. Weil die Abbildung Linearkombinationen erhält, wird das Quadrat zu dem Parallelogramm mit den Ecken $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$ und $\mathbf{a}_2$. Seine beiden Kanten am Nullpunkt sind die Spalten der Matrix (Abb. [32](#abb-32)). Das ganze Gitter der Ebene wird ebenso verformt: Jedes Kästchen wird zu einer verschobenen Kopie dieses Parallelogramms.

:::abbildung ml/k1ebene 32
Vier lineare Abbildungen der Ebene. Grau gestrichelt das Einheitsquadrat, blau sein Bild. Der rote Pfeil ist das Bild $\mathbf{a}_1$ von $\mathbf{e}_1$, der grüne das Bild $\mathbf{a}_2$ von $\mathbf{e}_2$; das sind die beiden Spalten der Matrix. Beim Plattdrücken ist $\mathbf{a}_2=\mathbf{0}$, und das Quadrat wird zur Strecke von $\mathbf{0}$ bis $\mathbf{e}_1$.
:::

<ul>

<li>

Die __Drehung__ um $90^\circ$ gegen den Uhrzeigersinn schickt $\mathbf{e}_1$ nach $(0,\,1)^{\top}$ und $\mathbf{e}_2$ nach $(-1,\,0)^{\top}$; das sind ihre Spalten.

</li>

<li>

Die __Streckung__ $\operatorname{diag}(2;\,0{,}5)$ zieht die Ebene waagerecht auf das Doppelte und staucht sie senkrecht auf die Hälfte.

</li>

<li>

Die __Scherung__ $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ lässt $\mathbf{e}_1$ an seinem Platz und schiebt $\mathbf{e}_2$ nach rechts: Jeder Punkt wird um seine Höhe nach rechts verschoben.

</li>

<li>

Die Matrix $\operatorname{diag}(1;\,0)$ behält die erste Komponente und setzt die zweite auf null. Sie drückt die ganze Ebene auf die $x_1$-Achse platt.

</li>

</ul>

::::beispiel [Rechenbeispiel] die Drehung um einen beliebigen Winkel
Dreht man um den Winkel $\alpha$ gegen den Uhrzeigersinn, so landet $\mathbf{e}_1$ im Punkt $(\cos\alpha,\,\sin\alpha)^{\top}$ auf dem Einheitskreis und $\mathbf{e}_2$, das $90^\circ$ weiter liegt, im Punkt $(-\sin\alpha,\,\cos\alpha)^{\top}$. Nach [(8.2)](#gl-8-2) ist die Drehmatrix deshalb

<span class="anker" id="gl-8-3"></span>
$$\mathbf R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}. \tag{8.3}$$

Für $\alpha=90^\circ$ ergibt sich die Matrix aus Abb. [32](#abb-32). Den Punkt $(1,\,1)^{\top}$ dreht sie nach $(-1,\,1)^{\top}$, die Streckung bildet ihn auf $(2;\ 0{,}5)^{\top}$ ab, die Scherung auf $(2,\,1)^{\top}$ und das Plattdrücken auf $(1,\,0)^{\top}$.
::::

⁠**Kurz gesagt:** Eine $2\times2$-Matrix verformt das Gitter der Ebene; aus dem Einheitsquadrat wird das Parallelogramm, das ihre beiden Spalten aufspannen.

### Lineare Funktionen mit einem Ausgang

<span class="anker" id="stufe-8-4"></span>

Ein Modell, das aus den Merkmalen eines Beispiels eine einzige Zahl macht, ist eine Abbildung von $\mathbb{R}^d$ nach $\mathbb{R}$. Ist sie linear, so ist ihre Matrix nach dem Satz in Unterabschnitt [8.2](#stufe-8-2) eine einzige Zeile mit $d$ Einträgen.

:::satz Satz 8.3 (Lineare Funktionen sind gewichtete Summen)
<span class="anker" id="satz-8-3"></span>

Jede lineare Abbildung $f\colon\mathbb{R}^d\to\mathbb{R}$ hat die Form $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}$ mit den Gewichten $w_j=f(\mathbf{e}_j)$.
:::

Das ist der Satz aus Unterabschnitt [8.2](#stufe-8-2) für $m=1$: Die $1\times d$-Matrix ist die Zeile $\mathbf{w}^{\top}$, und ihr Produkt mit $\mathbf{x}$ ist das Skalarprodukt. Die gewichtete Summe aus Unterabschnitt [2.2](das-skalarprodukt.html#stufe-2-2) ist also nicht irgendein Beispiel, sondern die allgemeinste lineare Vorschrift mit einem Ausgang.

::::beispiel [Rechenbeispiel]
Die Vorschrift der Maklerin ist $f(\mathbf{x})=3x_1+10x_2-4x_3$. Es ist $f(\mathbf{e}_1)=3$, $f(\mathbf{e}_2)=10$, $f(\mathbf{e}_3)=-4$, also $\mathbf{w}=(3,\,10,\,-4)^{\top}$. Das Gewicht $w_j=f(\mathbf{e}_j)$ ist der Wert der Vorschrift für ein gedachtes Beispiel, das nur eine Einheit von Merkmal $j$ hat und sonst nichts: Es sagt, wie viel eine Einheit dieses Merkmals beiträgt.
::::

⁠**Kurz gesagt:** Jede lineare Abbildung mit einem Ausgang ist eine gewichtete Summe $\mathbf{w}^{\top}\mathbf{x}$, und das Gewicht $w_j$ ist ihr Wert bei $\mathbf{e}_j$.

### Affine Abbildungen

<span class="anker" id="stufe-8-5"></span>

Die Maklerin merkt, dass ihre Schätzungen durchweg zu niedrig sind. Sie rechnet deshalb zu jeder gewichteten Summe einen Grundbetrag von $20$ Tausend Euro hinzu. Diese neue Vorschrift ist nicht mehr linear: Einer gedachten Wohnung $\mathbf{x}=\mathbf{0}$ ordnet sie $20$ zu und nicht $0$. Sie ist eine lineare Abbildung, gefolgt von einer Verschiebung.

:::definition Definition 8.4 (Affine Abbildung)
<span class="anker" id="satz-8-4"></span>

Eine Abbildung $f\colon\mathbb{R}^n\to\mathbb{R}^m$ der Form

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b} \tag{8.4}$$

mit einer Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ und einem festen Vektor $\mathbf{b}\in\mathbb{R}^m$ heißt __affin__. Für einen Ausgang ($m=1$) schreibt man $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+b$ und nennt die Zahl $b$ den __Achsenabschnitt__.
:::

Für $\mathbf{b}\ne\mathbf{0}$ ist eine affine Abbildung nicht linear, denn $f(\mathbf{0})=\mathbf{b}\ne\mathbf{0}$. Im Bild des Gitters wird die Ebene erst verformt und dann als Ganzes um $\mathbf{b}$ verschoben; der Nullpunkt landet bei $\mathbf{b}$. Umgangssprachlich nennt man auch affine Vorschriften oft „linear“. In dieser Reihe heißt nur eine Abbildung mit $\mathbf{b}=\mathbf{0}$ linear.

Für alle Beispiele zugleich schreibt man die affine Vorhersage mit dem Einsvektor $\mathbf 1\in\mathbb{R}^N$:

<span class="anker" id="gl-8-5"></span>
$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+b\,\mathbf 1 . \tag{8.5}$$

Der Summand $b\,\mathbf 1$ addiert zu jeder Vorhersage denselben Betrag $b$.

::::beispiel [Rechenbeispiel]
Mit $\mathbf{w}=(3,\,10,\,-4)^{\top}$ und $b=20$ werden aus den Vorhersagen $(188,\,126,\,286,\,232)^{\top}$ die Vorhersagen

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+20\cdot\mathbf 1=(208,\,146,\,306,\,252)^{\top}\ \text{Tausend Euro}.$$
::::

⁠**Kurz gesagt:** Eine affine Abbildung ist eine lineare Abbildung plus eine feste Verschiebung, $\mathbf{A}\mathbf{x}+\mathbf{b}$; bei einem Ausgang heißt die Verschiebung Achsenabschnitt.

:::hintergrund Der Trick mit der angehängten Eins
Eine affine Funktion lässt sich als lineare Funktion schreiben, wenn man jedem Beispiel eine Komponente mit dem festen Wert $1$ anhängt:

$$\mathbf{w}^{\top}\mathbf{x}+b=\begin{pmatrix}w_1&\cdots&w_d&b\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_d\\1\end{pmatrix}.$$

Der Achsenabschnitt wird so zum Gewicht eines Merkmals, das immer den Wert $1$ hat. Für den ganzen Datensatz hängt man an die Datenmatrix eine Spalte aus Einsen an: $\begin{pmatrix}\mathbf{X}&\mathbf 1\end{pmatrix}\begin{pmatrix}\mathbf{w}\\b\end{pmatrix}=\mathbf{X}\mathbf{w}+b\,\mathbf 1$. Für die Wohnungen hat die erweiterte Datenmatrix die Zeilen $(60,2,3,1)$, $(40,1,1,1)$, $(90,4,6,1)$, $(70,3,2,1)$, und mit dem Vektor $(3,\,10,\,-4,\,20)^{\top}$ kommt wieder $(208,\,146,\,306,\,252)^{\top}$ heraus. Mit diesem Trick braucht man für affine Vorschriften keine eigene Theorie: Alles, was für lineare Abbildungen gilt, gilt im um eins größeren Raum auch für sie.
:::

:::aufgabe Aufgabe 18 ★ Linear oder nicht?
<span class="anker" id="aufg-18"></span>

Prüfe, welche der Abbildungen linear sind, und gib für die linearen die Matrix an:

$$\begin{gathered} f_1(\mathbf{x})=(2x_1,\ x_1-x_2)^{\top},\qquad f_2(\mathbf{x})=x_1^2,\qquad f_3(\mathbf{x})=(x_2,\ x_1)^{\top},\\ f_4(x)=2x+3,\qquad f_5(\mathbf{x})=(0,\ 0)^{\top} \end{gathered}$$

für $\mathbf{x}\in\mathbb{R}^2$ beziehungsweise $x\in\mathbb{R}$ bei $f_4$.

:::loesung
<ul>

<li>

$f_1$ ist linear; beide Komponenten sind Summen von Vielfachen der $x_j$. Die Spalten sind $f_1(\mathbf{e}_1)=(2,\,1)^{\top}$ und $f_1(\mathbf{e}_2)=(0,\,-1)^{\top}$, also $\bigl(\begin{smallmatrix}2&0\\1&-1\end{smallmatrix}\bigr)$.

</li>

<li>

$f_2$ ist nicht linear: $f_2(2\mathbf{x})=4x_1^2\ne2f_2(\mathbf{x})$, sobald $x_1\ne0$.

</li>

<li>

$f_3$ ist linear, mit der Matrix $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$; sie vertauscht die Komponenten.

</li>

<li>

$f_4$ ist nicht linear, denn $f_4(0)=3\ne0$. Sie ist affin, mit dem Achsenabschnitt $3$.

</li>

<li>

$f_5$ ist linear, mit der Nullmatrix; beide Bedingungen gelten wegen $\mathbf{0}+\mathbf{0}=\mathbf{0}$ und $c\,\mathbf{0}=\mathbf{0}$.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 19 ★★ Matrizen aus den Bildern der Einheitsvektoren
<span class="anker" id="aufg-19"></span>

<ol class="al">

<li>

Gib die Matrix der Drehung um $30^\circ$ an und berechne das Bild von $(2,\,0)^{\top}$.

</li>

<li>

Die Spiegelung an der Winkelhalbierenden $x_1=x_2$ vertauscht die beiden Komponenten. Gib ihre Matrix an und das Bild von $(3,\,1)^{\top}$.

</li>

<li>

Eine lineare Abbildung erfüllt $f\bigl((1,\,1)^{\top}\bigr)=(1,\,4)^{\top}$ und $f\bigl((2,\,-1)^{\top}\bigr)=(5,\,-1)^{\top}$. Bestimme ihre Matrix. Tipp: Schreibe beide Bedingungen mit den Spalten $\mathbf{a}_1,\mathbf{a}_2$ auf.

</li>

</ol>

:::loesung
(a) Nach [(8.3)](#gl-8-3) mit $\cos30^\circ=\sqrt3/2\approx0{,}866$ und $\sin30^\circ=\tfrac12$:

$$\mathbf R_{30^\circ}=\begin{pmatrix}0{,}866&-0{,}5\\0{,}5&0{,}866\end{pmatrix},\qquad \mathbf R_{30^\circ}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}\sqrt3\\1\end{pmatrix}\approx\begin{pmatrix}1{,}732\\1\end{pmatrix}.$$

Das Bild ist das Doppelte der ersten Spalte, ein Pfeil der Länge $2$ unter $30^\circ$.

(b) $\mathbf{e}_1$ geht nach $\mathbf{e}_2$ und $\mathbf{e}_2$ nach $\mathbf{e}_1$, also ist die Matrix $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, und $(3,\,1)^{\top}$ geht nach $(1,\,3)^{\top}$.

(c) Wegen der Linearität ist $f\bigl((1,1)^{\top}\bigr)=\mathbf{a}_1+\mathbf{a}_2=(1,\,4)^{\top}$ und $f\bigl((2,-1)^{\top}\bigr)=2\mathbf{a}_1-\mathbf{a}_2=(5,\,-1)^{\top}$. Addiert man beide Gleichungen, so ist $3\mathbf{a}_1=(6,\,3)^{\top}$, also $\mathbf{a}_1=(2,\,1)^{\top}$ und $\mathbf{a}_2=(1,4)^{\top}-(2,1)^{\top}=(-1,\,3)^{\top}$. Die Matrix ist $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)$. Probe: $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)(2,\,-1)^{\top}=(5,\,-1)^{\top}$.
:::
:::

:::aufgabe Aufgabe 20 ★★ Der Verbrauch aus Zählerständen als Matrix
<span class="anker" id="aufg-20"></span>

Ein neuer Wasserzähler zeigt am Ende von vier Monaten die Stände $x[1],\dots,x[4]$ in Kubikmetern; vor dem ersten Monat stand er auf $x[0]=0$. Der Verbrauch im Monat $n$ ist die Differenz $y[n]=x[n]-x[n-1]$, $n=1,\dots,4$.

<ol class="al">

<li>

Warum ist diese Rechnung linear? Stelle ihre $4\times4$-Matrix auf, indem du die Antworten auf die vier Einheitsvektoren berechnest.

</li>

<li>

Berechne den Verbrauch zu den Ständen $\mathbf{x}=(1,\,2,\,4,\,7)^{\top}$ mit der Matrix und mit der Formel.

</li>

</ol>

:::loesung
(a) Jede Komponente $y[n]=x[n]-x[n-1]$ des Ergebnisses ist eine feste Summe von Vielfachen der Komponenten von $\mathbf{x}$, also ist die Rechnung linear. Die Antwort auf die einzelne $1$ an der Stelle $1$, $\mathbf{x}=\mathbf{e}_1=(1,0,0,0)^{\top}$, ist $(1,\,-1,\,0,\,0)^{\top}$: Erst steigt der Stand auf $1$, dann fällt er wieder auf $0$. Ebenso antwortet die Rechnung auf $\mathbf{e}_2$ mit $(0,\,1,\,-1,\,0)^{\top}$, auf $\mathbf{e}_3$ mit $(0,\,0,\,1,\,-1)^{\top}$ und auf $\mathbf{e}_4$ mit $(0,\,0,\,0,\,1)^{\top}$; bei dieser letzten $1$ enden die vier Monate, bevor der Stand wieder abfällt. Diese Antworten sind die Spalten:

$$\mathbf{A}=\begin{pmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix}.$$

(b) Mit der Matrix: $\mathbf{A}\,(1,2,4,7)^{\top}=(1,\ -1+2,\ -2+4,\ -4+7)^{\top}=(1,\,1,\,2,\,3)^{\top}$. Mit der Formel: $y[1]=1-0=1$, $y[2]=2-1=1$, $y[3]=4-2=2$, $y[4]=7-4=3$. In den vier Monaten wurden also $1$, $1$, $2$ und $3$ Kubikmeter Wasser verbraucht.
:::
:::
