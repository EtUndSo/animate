---
title: Richtungsableitung und steilster Anstieg
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
knoten: Grundlagen 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230500
summary: Die partiellen Ableitungen sagen, wie die Funktion reagiert, wenn man einen Eingang allein verändert.
tags: Richtungsableitung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die partiellen Ableitungen sagen, wie die Funktion reagiert, wenn man einen Eingang allein verändert. Verschiebt man alle Eingänge zugleich in eine Richtung, so misst die Richtungsableitung die Steigung. Mit ihr zeigt dieser Abschnitt, dass der Gradient in die Richtung des steilsten Anstiegs zeigt und senkrecht auf den Höhenlinien steht. Ein Beispiel zeigt, dass der steilste Weg bergab trotzdem nicht unbedingt auf den tiefsten Punkt zuläuft.
:::

### Die Richtungsableitung

<span class="anker" id="stufe-4-1"></span>

Im Gelände geht man selten genau nach Norden oder genau nach Osten. Wer an der Stelle $\mathbf{x}$ steht und in irgendeine Richtung losgeht, spürt eine Steigung, die von der Richtung abhängt. Eine Richtung beschreibt man durch einen Vektor $\mathbf{u}$ der Länge $1$. Die Länge muss festgelegt sein: Wer doppelt so große Schritte macht, steigt bei jedem Schritt doppelt so viel, ohne dass das Gelände steiler wäre.

:::definition Definition 4.1 (Richtungsableitung)
<span class="anker" id="satz-4-1"></span>

Für einen Vektor $\mathbf{u}$ mit $\lVert\mathbf{u}\rVert=1$ heißt

<span class="anker" id="gl-4-1"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\lim_{t\to0}\frac{f(\mathbf{x}+t\,\mathbf{u})-f(\mathbf{x})}{t} \tag{4.1}$$

die __Richtungsableitung__ von $f$ an der Stelle $\mathbf{x}$ in Richtung $\mathbf{u}$, sofern der Grenzwert existiert.
:::

Für $\mathbf{u}=\mathbf{e}_j$ ist das die partielle Ableitung nach $x_j$. Im Bild der Landschaft schneidet man das Gelände entlang der Geraden durch $\mathbf{x}$ in Richtung $\mathbf{u}$, und die Richtungsableitung ist die Steigung dieser Schnittkurve. Man muss sie aber nicht für jede Richtung neu ausrechnen.

:::satz Satz 4.2 (Richtungsableitung und Gradient)
<span class="anker" id="satz-4-2"></span>

Ist $f$ an der Stelle $\mathbf{x}$ differenzierbar, so gilt für jeden Vektor $\mathbf{u}$ der Länge $1$

<span class="anker" id="gl-4-2"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}\mathbf{u} . \tag{4.2}$$
:::

:::beweis Richtungsableitung und Gradient
Man setzt in [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5) speziell $\mathbf{h}=t\,\mathbf{u}$ mit $t\ne0$; dann ist $\lVert\mathbf{h}\rVert=|t|$. Der Quotient $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})-t\,\nabla f(\mathbf{x})^{\top}\mathbf{u}}{|t|}$ geht gegen $0$, also auch $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})}{t}-\nabla f(\mathbf{x})^{\top}\mathbf{u}$.
:::

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ mit $\nabla f=(4,\,5)^{\top}$ und der Richtung $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$, die die Länge $\sqrt{0{,}36+0{,}64}=1$ hat, ist

$$D_{\mathbf{u}}f(1,2)=4\cdot0{,}6+5\cdot0{,}8=2{,}4+4{,}0=6{,}4$$

(Abb. [8](#abb-8)). In die entgegengesetzte Richtung $-\mathbf{u}$ ist die Steigung $-6{,}4$, und in Richtung $(0{,}8;\ -0{,}6)^{\top}$, die auf $\mathbf{u}$ senkrecht steht, ist sie $3{,}2-3{,}0=0{,}2$.

:::abbildung ml/k3rrichtung 8
Die Richtungsableitung als Skalarprodukt von Gradient und Richtung, für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $\mathbf{x}=(1,\,2)^{\top}$.
:::

⁠**Kurz gesagt:** Die Steigung in Richtung eines Einheitsvektors $\mathbf{u}$ ist das Skalarprodukt $\nabla f(\mathbf{x})^{\top}\mathbf{u}$.

### Die Richtung des steilsten Anstiegs

<span class="anker" id="stufe-4-2"></span>

In welche Richtung muss man gehen, damit es am steilsten bergauf geht? Nach [(4.2)](#gl-4-2) sucht man den Einheitsvektor $\mathbf{u}$, für den das Skalarprodukt $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ am größten ist. [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) hat dafür das Werkzeug geliefert: die Cauchy-Schwarz-Ungleichung.

:::satz Satz 4.3 (Steilster Anstieg)
<span class="anker" id="satz-4-3"></span>

Es sei $f$ an der Stelle $\mathbf{x}$ differenzierbar und $\nabla f(\mathbf{x})\ne\mathbf{0}$. Dann gilt für jeden Vektor $\mathbf{u}$ der Länge $1$

<span class="anker" id="gl-4-3"></span>
$$-\lVert\nabla f(\mathbf{x})\rVert\le D_{\mathbf{u}}f(\mathbf{x})\le\lVert\nabla f(\mathbf{x})\rVert . \tag{4.3}$$

Die obere Schranke wird nur für $\mathbf{u}=\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$ erreicht, die untere nur für $\mathbf{u}=-\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. Der Gradient zeigt also in die Richtung des steilsten Anstiegs, und seine Länge ist die Steigung in dieser Richtung; der negative Gradient zeigt in die Richtung des steilsten Abstiegs.
:::

:::beweis Steilster Anstieg
Nach der Cauchy-Schwarz-Ungleichung aus [Grundlagen 1, Abschnitt 5.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1), ist $|\nabla f(\mathbf{x})^{\top}\mathbf{u}|\le\lVert\nabla f(\mathbf{x})\rVert\,\lVert\mathbf{u}\rVert=\lVert\nabla f(\mathbf{x})\rVert$, und Gleichheit gilt genau dann, wenn $\mathbf{u}$ ein Vielfaches von $\nabla f(\mathbf{x})$ ist. Die Vielfachen der Länge $1$ sind $\pm\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. Setzt man sie ein, erhält man $\pm\nabla f(\mathbf{x})^{\top}\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert=\pm\lVert\nabla f(\mathbf{x})\rVert$.
:::

Mit dem Winkel $\varphi$ zwischen $\nabla f(\mathbf{x})$ und $\mathbf{u}$ aus [Grundlagen 1, Abschnitt 5.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2), ist $D_{\mathbf{u}}f(\mathbf{x})=\lVert\nabla f(\mathbf{x})\rVert\cos\varphi$. Geht man in Richtung des Gradienten, ist $\varphi=0$ und $\cos\varphi=1$. Weicht man um $90^\circ$ ab, ist die Steigung null. Geht man entgegen, ist sie am stärksten negativ. Nach [Grundlagen 1, Abschnitt 5.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), ist $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ die Schattenlänge des Gradienten auf der Geraden in Richtung $\mathbf{u}$, und ein Schatten ist am längsten, wenn die Gerade in Richtung des Pfeils selbst zeigt.

Drei Voraussetzungen stecken im Satz. Erstens muss $\nabla f(\mathbf{x})\ne\mathbf{0}$ sein; ist der Gradient null, so ist die Steigung nach [(4.2)](#gl-4-2) in jede Richtung null, und keine Richtung ist steiler als eine andere. Zweitens muss $f$ differenzierbar sein, sonst gilt [(4.2)](#gl-4-2) nicht. Drittens vergleicht der Satz Richtungen gleicher euklidischer Länge; misst man Schritte anders, ändert sich die steilste Richtung (Hintergrund unten).

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ ist $\lVert\nabla f\rVert=\sqrt{16+25}=\sqrt{41}\approx6{,}403$, und die steilste Richtung ist $(4,\,5)^{\top}/\sqrt{41}\approx(0{,}625;\ 0{,}781)^{\top}$. Keine Richtung hat eine größere Steigung. Die Richtung $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ aus dem vorigen Unterabschnitt weicht nur um etwa $1{,}8^\circ$ davon ab; deshalb lag ihre Steigung $6{,}4$ schon fast am Höchstwert. In Richtung $(5,\,-4)^{\top}/\sqrt{41}$, senkrecht zum Gradienten, ist die Steigung $(20-20)/\sqrt{41}=0$.

⁠**Kurz gesagt:** Der Gradient zeigt in die Richtung des steilsten Anstiegs, seine Länge ist die Steigung dort; entgegen dem Gradienten geht es am steilsten bergab.

:::hintergrund Die steilste Richtung hängt davon ab, wie man Schritte misst
Der Satz vergleicht alle Richtungen $\mathbf{u}$ mit $\lVert\mathbf{u}\rVert=1$ in der euklidischen Norm. [Grundlagen 1, Abschnitt 3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3), kannte weitere Normen. Erlaubt man alle Schritte mit $\lVert\mathbf{u}\rVert_\infty\le1$, darf also jede Komponente zwischen $-1$ und $1$ liegen, so wird $\nabla f^{\top}\mathbf{u}=\sum_j\partial_jf\cdot u_j$ am größten, wenn jede Komponente $u_j$ den Wert $+1$ oder $-1$ mit dem Vorzeichen von $\partial_jf$ hat. Die steilste Richtung ist dann $\operatorname{sign}(\nabla f)$, komponentenweise, und die Steigung ist $\sum_j|\partial_jf|=\lVert\nabla f\rVert_1$. Erlaubt man dagegen alle Schritte mit $\lVert\mathbf{u}\rVert_1\le1$, so steckt man das ganze Budget in die Komponente mit dem größten $|\partial_jf|$: Die steilste Richtung ist eine Koordinatenachse, und die Steigung ist $\lVert\nabla f\rVert_\infty$. Für $\nabla f=(4,\,5)^{\top}$ ergibt das die Richtungen $(1,\,1)^{\top}$ mit Steigung $9$ und $(0,\,1)^{\top}$ mit Steigung $5$. „Der Gradient ist die steilste Richtung“ ist also eine Aussage über die euklidische Länge. Sie hängt auch an den Einheiten der Variablen: Misst man $x_1$ in anderen Einheiten, ändern sich die Längen der Schritte und mit ihnen die steilste Richtung, ganz wie die Abstände in [Grundlagen 1, Abschnitt 4.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2).
:::

### Der Gradient steht senkrecht auf den Höhenlinien

<span class="anker" id="stufe-4-3"></span>

Wer auf einer Höhenlinie entlanggeht, steigt weder auf noch ab. In Richtung der Höhenlinie ist die Steigung also null, und nach dem vorigen Unterabschnitt ist die Steigung genau in den Richtungen null, die senkrecht auf dem Gradienten stehen. Der Gradient steht deshalb senkrecht auf der Höhenlinie. Genauer heißt das:

:::satz Satz 4.4 (Gradient und Höhenlinie)
<span class="anker" id="satz-4-4"></span>

Es sei $f$ an der Stelle $\mathbf{x}$ differenzierbar, $\nabla f(\mathbf{x})\ne\mathbf{0}$ und $c=f(\mathbf{x})$. Die Niveaumenge der linearen Näherung durch $\mathbf{x}$, also die Menge der Punkte $\mathbf{x}+\mathbf{h}$ mit $\nabla f(\mathbf{x})^{\top}\mathbf{h}=0$, ist bei zwei Variablen die Gerade durch $\mathbf{x}$ senkrecht zum Gradienten. Sie ist die Tangente an die Höhenlinie von $f$ zum Wert $c$.
:::

Dass die Gerade die Höhenlinie berührt, folgt aus der Lupe: In der Nähe von $\mathbf{x}$ unterscheiden sich $f$ und ihre lineare Näherung nur um einen Fehler, der schneller als $\lVert\mathbf{h}\rVert$ verschwindet, und damit unterscheiden sich auch ihre Höhenlinien zum Wert $c$ nur so wenig, dass sie bei $\mathbf{x}$ dieselbe Richtung haben. Einen Beweis mit der Kettenregel liefert Aufgabe [22](die-kettenregel-fur-mehrere-variablen.html#aufg-22). Bei mehr als zwei Variablen gilt dasselbe für die Niveaumenge, die dann eine Fläche ist: Der Gradient steht senkrecht auf ihr.

⁠**Rechenbeispiel:** Für die Schüssel $f(\mathbf{x})=x_1^2+4x_2^2$ ist $\nabla f(\mathbf{x})=(2x_1,\,8x_2)^{\top}$ und an der Stelle $(1,\,1)$ gleich $(2,\,8)^{\top}$. Die Höhenlinie durch diesen Punkt ist die Ellipse $x_1^2+4x_2^2=5$. Die Richtung $\mathbf{t}=(4,\,-1)^{\top}$ steht senkrecht auf dem Gradienten, denn $2\cdot4+8\cdot(-1)=0$. Geht man von $(1,\,1)$ aus ein Stück $s$ in diese Richtung, so ist

$$f(1+4s,\ 1-s)=(1+4s)^2+4\,(1-s)^2=5+20s^2 .$$

Der Wert ändert sich nur um $20s^2$, also schneller verschwindend als $s$: Die Gerade berührt die Höhenlinie und ist ihre Tangente. Abb. [9](#abb-9) zeigt die Gradienten an vielen Punkten; jeder steht senkrecht auf der Höhenlinie durch seinen Fußpunkt.

:::abbildung ml/k3hoehen 9
Gradienten (rot, verkürzt gezeichnet) auf Höhenlinien (grau). (a) Bei der runden Schüssel zeigen alle Gradienten genau vom Mittelpunkt weg. (b) Bei der gestreckten Schüssel stehen sie ebenfalls senkrecht auf den Höhenlinien, zeigen aber nur auf den Achsen genau vom Mittelpunkt weg. Am Punkt $(1,\,1)$ (schwarz) ist die Richtung des steilsten Abstiegs blau eingezeichnet. In (a) zeigt sie auf den tiefsten Punkt, in (b) weicht sie um etwa $31^\circ$ von der Richtung zum tiefsten Punkt (gestrichelt) ab.
:::

⁠**Kurz gesagt:** Entlang einer Höhenlinie ändert sich $f$ nicht; deshalb steht der Gradient senkrecht auf ihr.

### Steilster Abstieg und der tiefste Punkt

<span class="anker" id="stufe-4-4"></span>

Bei einer runden Schüssel ist es selbstverständlich, dass der steilste Weg bergab zur Mitte führt. Bei einer gestreckten Schüssel ist es falsch, und dieser Unterschied ist wichtig, weil man vom Gradienten leicht mehr erwartet, als er weiß.

Für $f(\mathbf{x})=x_1^2+x_2^2$ ist $\nabla f(\mathbf{x})=2\mathbf{x}$. Der negative Gradient $-2\mathbf{x}$ zeigt also von jedem Punkt aus genau auf den Nullpunkt, den tiefsten Punkt der Schüssel. Für $f(\mathbf{x})=x_1^2+4x_2^2$ ist $-\nabla f(\mathbf{x})=(-2x_1,\,-8x_2)^{\top}$, und das ist nur dann ein Vielfaches von $-\mathbf{x}$, wenn $x_1=0$ oder $x_2=0$ ist, also auf den Achsen. Überall sonst zeigt der steilste Abstieg am tiefsten Punkt vorbei.

Der Grund liegt in der Form der Höhenlinien. Der Gradient weiß nur, wie das Gelände an seinem Fußpunkt geneigt ist; er steht senkrecht auf der Höhenlinie dort. Bei gestreckten Höhenlinien steht die Senkrechte schräg zur Richtung auf die Mitte. Im Beispiel wächst $f$ in Richtung $x_2$ viermal so schnell wie in Richtung $x_1$; die Wände der Schüssel sind in Richtung $x_2$ steiler, und der steilste Abstieg führt vor allem quer zu ihnen.

⁠**Rechenbeispiel:** An der Stelle $(1,\,1)$ ist $-\nabla f=(-2,\,-8)^{\top}$ mit der Länge $\sqrt{68}\approx8{,}246$, die Richtung des steilsten Abstiegs also $(-0{,}243;\ -0{,}970)^{\top}$. Die Richtung zum tiefsten Punkt ist $(-1,\,-1)^{\top}/\sqrt2\approx(-0{,}707;\ -0{,}707)^{\top}$. Der Winkel zwischen beiden hat den Kosinus

$$\frac{(-2)\cdot(-1)+(-8)\cdot(-1)}{\sqrt{68}\cdot\sqrt2}=\frac{10}{\sqrt{136}}\approx0{,}857,$$

er beträgt also etwa $31^\circ$. In Richtung des tiefsten Punkts ist die Steigung nach [(4.2)](#gl-4-2) nur $-10/\sqrt2\approx-7{,}07$, im steilsten Abstieg dagegen $-8{,}246$.

⁠**Kurz gesagt:** Der negative Gradient zeigt am steilsten bergab, aber nur bei runden Höhenlinien auf den tiefsten Punkt; bei gestreckten Höhenlinien zeigt er daran vorbei.

:::aufgabe Aufgabe 13 ★ Steigungen in vielen Richtungen
<span class="anker" id="aufg-13"></span>

Es sei $f(\mathbf{x})=x_1^2+4x_2^2$ und $\mathbf{x}=(1,\,1)^{\top}$.

<ol class="al">

<li>

Berechne die Richtungsableitungen in die Richtungen $\mathbf{e}_1$, $\mathbf{e}_2$, $(1,\,1)^{\top}/\sqrt2$ und $(-1,\,1)^{\top}/\sqrt2$.

</li>

<li>

Vergleiche mit $\lVert\nabla f(\mathbf{x})\rVert$. Welche der vier Richtungen ist der steilsten am nächsten?

</li>

</ol>

:::loesung
(a) Es ist $\nabla f(1,1)=(2,\,8)^{\top}$. Nach [(4.2)](#gl-4-2):

$$D_{\mathbf{e}_1}f=2,\qquad D_{\mathbf{e}_2}f=8,\qquad D_{(1,1)/\sqrt2}f=\frac{2+8}{\sqrt2}\approx7{,}071,\qquad D_{(-1,1)/\sqrt2}f=\frac{-2+8}{\sqrt2}\approx4{,}243 .$$

(b) $\lVert\nabla f\rVert=\sqrt{68}\approx8{,}246$; keine der Steigungen ist größer, wie [(4.3)](#gl-4-3) verlangt. Am nächsten an der steilsten Richtung liegt $\mathbf{e}_2$, mit $8$. Der Winkel zwischen $\mathbf{e}_2$ und $\nabla f$ hat den Kosinus $8/\sqrt{68}\approx0{,}970$, also etwa $14^\circ$; bei $(1,\,1)^{\top}/\sqrt2$ sind es etwa $31^\circ$.
:::
:::

:::aufgabe Aufgabe 14 ★★ Eine Hyperbel als Höhenlinie
<span class="anker" id="aufg-14"></span>

Es sei $f(\mathbf{x})=x_1x_2$ und $\mathbf{x}=(2,\,1)^{\top}$.

<ol class="al">

<li>

Berechne $\nabla f(\mathbf{x})$, die steilste Richtung und die Steigung in ihr.

</li>

<li>

Die Höhenlinie durch $\mathbf{x}$ ist $x_2=2/x_1$. Berechne die Steigung dieser Kurve an der Stelle $x_1=2$, schreibe ihre Tangentenrichtung als Vektor und prüfe, dass er senkrecht auf $\nabla f(\mathbf{x})$ steht.

</li>

</ol>

:::loesung
(a) $\nabla f(\mathbf{x})=(x_2,\,x_1)^{\top}$, an der Stelle $(2,\,1)$ also $(1,\,2)^{\top}$. Die steilste Richtung ist $(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$, die Steigung in ihr $\sqrt5\approx2{,}236$.

(b) Die Höhenlinie $x_2=2/x_1$ hat die Steigung $-2/x_1^2$, bei $x_1=2$ also $-\tfrac12$. Eine Tangentenrichtung ist $(1,\,-\tfrac12)^{\top}$ oder, mit $2$ multipliziert, $(2,\,-1)^{\top}$. Es ist $(1,\,2)(2,\,-1)^{\top}=2-2=0$: Der Gradient steht senkrecht auf der Höhenlinie.
:::
:::

:::aufgabe Aufgabe 15 ★★ Lineare Funktionen
<span class="anker" id="aufg-15"></span>

Es sei $f(\mathbf{x})=\mathbf{a}^{\top}\mathbf{x}+b$ mit festem $\mathbf{a}\in\mathbb{R}^d$, $\mathbf{a}\ne\mathbf{0}$, und einer Zahl $b$.

<ol class="al">

<li>

Zeige, dass $\nabla f(\mathbf{x})=\mathbf{a}$ an jeder Stelle gilt. Was sind die Höhenlinien für $d=2$?

</li>

<li>

Für die Wohnungen aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) ist $\hat y=\mathbf{w}^{\top}\mathbf{x}+b$ mit $\mathbf{w}=(3,\,10,\,-4)^{\top}$, wobei $x_1$ die Fläche in $\mathrm m^2$, $x_2$ die Zimmerzahl und $x_3$ die Entfernung zum Zentrum in km ist. Welche Änderung $\mathbf{u}$ der Merkmale mit $\lVert\mathbf{u}\rVert=1$ erhöht die Vorhersage am stärksten, und um wie viel?

</li>

<li>

Gibt man die Fläche in $10\,\mathrm m^2$ an, so wird aus $w_1=3$ das Gewicht $30$. Wie lautet jetzt die steilste Richtung? Was lernt man daraus über den Satz vom steilsten Anstieg?

</li>

</ol>

:::loesung
(a) $\partial_k(\mathbf{a}^{\top}\mathbf{x}+b)=a_k$, also $\nabla f=\mathbf{a}$ überall. Für $d=2$ sind die Höhenlinien die Geraden $a_1x_1+a_2x_2+b=c$; sie sind zueinander parallel und stehen senkrecht auf $\mathbf{a}$.

(b) Der Gradient nach $\mathbf{x}$ ist $\mathbf{w}=(3,\,10,\,-4)^{\top}$ mit $\lVert\mathbf{w}\rVert=\sqrt{9+100+16}=\sqrt{125}\approx11{,}18$. Die steilste Änderung der Länge $1$ ist $\mathbf{u}=\mathbf{w}/\sqrt{125}\approx(0{,}268;\ 0{,}894;\ -0{,}358)^{\top}$, und sie erhöht die Vorhersage um etwa $11{,}18$ Tausend Euro: etwas mehr Fläche, deutlich mehr Zimmer und etwas näher am Zentrum.

(c) In den neuen Einheiten ist $\mathbf{w}'=(30,\,10,\,-4)^{\top}$ mit $\lVert\mathbf{w}'\rVert=\sqrt{1016}\approx31{,}87$, und die steilste Richtung ist $\mathbf{w}'/\lVert\mathbf{w}'\rVert\approx(0{,}941;\ 0{,}314;\ -0{,}125)^{\top}$: Jetzt liegt sie fast ganz in der Fläche. Dieselbe Wohnung, dieselben Preise, aber eine andere steilste Richtung. Der Satz vom steilsten Anstieg vergleicht Schritte gleicher euklidischer Länge in den gewählten Koordinaten, und was „Länge $1$“ bedeutet, hängt von den Einheiten ab, genau wie die Abstände in [Grundlagen 1, Abschnitt 4.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2). Bei Merkmalen in verschiedenen Einheiten ist die steilste Richtung erst nach dem Standardisieren aus [Grundlagen 1, Abschnitt 4.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5), aussagekräftig.
:::
:::

:::aufgabe Aufgabe 16 ★★★ Wann zeigt der steilste Abstieg zur Mitte?
<span class="anker" id="aufg-16"></span>

Es sei $f(\mathbf{x})=a\,x_1^2+b\,x_2^2$ mit Zahlen $a,b>0$.

<ol class="al">

<li>

Zeige: $-\nabla f(\mathbf{x})$ ist genau dann ein positives Vielfaches von $-\mathbf{x}$, wenn $a=b$ ist oder $\mathbf{x}$ auf einer der Achsen liegt ($\mathbf{x}\ne\mathbf{0}$).

</li>

<li>

Berechne für $a=1$, $b=4$ an den Stellen $(1,\,1)$, $(2,\,1)$ und $(4,\,1)$ den Winkel zwischen $-\nabla f$ und $-\mathbf{x}$. Wie ändert er sich, wenn man auf der Geraden $x_2=1$ nach außen geht?

</li>

</ol>

:::loesung
(a) Es ist $-\nabla f(\mathbf{x})=(-2ax_1,\,-2bx_2)^{\top}$. Dieser Vektor ist genau dann gleich $c\,(-x_1,\,-x_2)^{\top}$ mit einem $c>0$, wenn $2ax_1=c\,x_1$ und $2bx_2=c\,x_2$ gilt. Sind beide Koordinaten von null verschieden, folgt $2a=c=2b$, also $a=b$. Ist $x_1=0$, genügt $c=2b$; ist $x_2=0$, genügt $c=2a$. Bei einer runden Schüssel zeigt der steilste Abstieg also überall zum Nullpunkt, bei einer gestreckten nur auf den Achsen.

(b) Für $a=1$, $b=4$ ist $-\nabla f=(-2x_1,\,-8x_2)^{\top}$:

$$\begin{aligned} (1,\,1)&:\ \cos\varphi=\frac{2+8}{\sqrt{68}\,\sqrt2}\approx0{,}857,\ \varphi\approx31{,}0^\circ;\\ (2,\,1)&:\ \cos\varphi=\frac{8+8}{\sqrt{80}\,\sqrt5}=0{,}8,\ \varphi\approx36{,}9^\circ;\\ (4,\,1)&:\ \cos\varphi=\frac{32+8}{\sqrt{128}\,\sqrt{17}}\approx0{,}857,\ \varphi\approx31{,}0^\circ . \end{aligned}$$

Auf der Geraden $x_2=1$ wächst der Winkel von $0^\circ$ bei $x_1=0$ zunächst an und nimmt dann wieder ab; weit draußen liegt der Punkt fast in Richtung der $x_1$-Achse, und dort zeigt der steilste Abstieg wieder fast zur Mitte.
:::
:::
