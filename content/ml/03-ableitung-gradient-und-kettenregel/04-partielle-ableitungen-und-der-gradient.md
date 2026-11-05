---
title: Partielle Ableitungen und der Gradient
pfad: Informatik / Machine Learning / Ableitung, Gradient und Kettenregel
order: 6230400
summary: Hängt eine Zahl von vielen Eingängen ab, kann man jeden Eingang einzeln ein wenig verändern und die anderen festhalten.
tags: Funktion von d Variablen, Niveaumenge, Höhenlinie, Schnittkurve, partielle Ableitung, Gradient, Tangentialebene, differenzierbar
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Hängt eine Zahl von vielen Eingängen ab, kann man jeden Eingang einzeln ein wenig verändern und die anderen festhalten. Die Steigungen, die man dabei findet, heißen partielle Ableitungen. Zusammen bilden sie einen Vektor, den Gradienten, und mit ihm wird die lineare Näherung aus Abschnitt [1](die-ableitung.html#stufe-1) zu einer Näherung durch eine Ebene. Am Ende klärt der Abschnitt, wann diese Näherung wirklich gilt.
:::

### Funktionen mehrerer Variablen

<span class="anker" id="stufe-3-1"></span>

In [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 2.2, war die Vorhersage für eine Wohnung die gewichtete Summe $\hat y=\mathbf{w}^{\top}\mathbf{x}$ der Merkmale. Hält man die Merkmale fest und fragt, wie die Vorhersage von den Gewichten abhängt, so ist $\hat y$ eine Zahl, die von den $d$ Zahlen $w_1,\dots,w_d$ abhängt. Ebenso hängt die quadratische Form $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ aus [Teil 2](/wissen/informatik/machine-learning/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html), Abschnitt 5.1, von allen Komponenten von $\mathbf{x}$ ab. Für solche Zuordnungen braucht man einen eigenen Begriff.

:::definition Definition 3.1 (Funktion mehrerer Variablen, Höhenlinie)
<span class="anker" id="satz-3-1"></span>

Eine Funktion $f:\mathbb{R}^d\to\mathbb{R}$ ordnet jedem Vektor $\mathbf{x}\in\mathbb{R}^d$ eine Zahl $f(\mathbf{x})=f(x_1,\dots,x_d)$ zu; sie heißt __Funktion von $d$ Variablen__. Für eine Zahl $c$ heißt die Menge aller $\mathbf{x}$ mit $f(\mathbf{x})=c$ die __Niveaumenge__ von $f$ zum Wert $c$. Für $d=2$ ist sie meist eine Kurve und heißt dann __Höhenlinie__.
:::

Für zwei Variablen hilft das Bild einer Landschaft. Der Vektor $\mathbf{x}=(x_1,\,x_2)^{\top}$ ist ein Ort auf einer Landkarte, $f(\mathbf{x})$ die Höhe des Geländes über diesem Ort. Der Graph von $f$, die Menge der Punkte $(x_1,\,x_2,\,f(x_1,x_2))$ im Raum, ist die Oberfläche des Geländes. Die Höhenlinien verbinden wie auf einer Wanderkarte alle Orte gleicher Höhe. Wo sie dicht liegen, ist das Gelände steil; wo sie weit auseinanderliegen, ist es flach. Bei mehr als zwei Variablen fehlt das Bild, aber die Rechnungen bleiben dieselben.

⁠**Rechenbeispiel:** Durch die Abschnitte [3](#stufe-3) bis [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) begleitet uns die Funktion

<span class="anker" id="gl-3-1"></span>
$$f(\mathbf{x})=x_1^2\,x_2+x_2^2 . \tag{3.1}$$

An der Stelle $\mathbf{x}=(1,\,2)^{\top}$ ist $f(1,2)=1\cdot2+4=6$. Zur Höhenlinie $f=6$ gehören alle Punkte mit $x_1^2x_2+x_2^2=6$. Für $x_1=0$ ist das $x_2^2=6$, also liegt der Punkt $(0;\ \sqrt6)^{\top}\approx(0;\ 2{,}449)^{\top}$ darauf. Allgemein ist die Gleichung für jedes feste $x_1$ quadratisch in $x_2$, und ihre positive Lösung $x_2=\tfrac12\bigl(\sqrt{x_1^4+24}-x_1^2\bigr)$ beschreibt die ganze Höhenlinie oberhalb der $x_1$-Achse; für $x_1=1$ ergibt sie $\tfrac12(5-1)=2$. Abb. [6](#abb-6) zeigt einige Höhenlinien.

⁠**Kurz gesagt:** Eine Funktion von $d$ Variablen ordnet jedem Vektor eine Zahl zu; bei zwei Variablen stellt man sie sich als Landschaft vor, deren Höhenlinien die Orte gleicher Höhe verbinden.

### Partielle Ableitungen

<span class="anker" id="stufe-3-2"></span>

Wie stark reagiert $f$, wenn man nur einen Eingang verändert? Man hält alle anderen fest, und $f$ wird zu einer gewöhnlichen Funktion einer Variablen. Im Bild der Landschaft schneidet man das Gelände entlang einer Geraden parallel zu einer Achse. Die Schnittfläche zeigt als Rand eine Kurve, die __Schnittkurve__, und ihre Steigung ist die gesuchte Empfindlichkeit.

:::definition Definition 3.2 (Partielle Ableitung)
<span class="anker" id="satz-3-2"></span>

Die __partielle Ableitung__ von $f:\mathbb{R}^d\to\mathbb{R}$ nach $x_j$ an der Stelle $\mathbf{x}$ ist

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial x_j}(\mathbf{x})=\lim_{h\to0}\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x})}{h}, \tag{3.2}$$

sofern der Grenzwert existiert. Dabei ist $\mathbf{e}_j$ der $j$-te Einheitsvektor aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 1.6. Kurz schreibt man auch $\partial_jf(\mathbf{x})$.
:::

Der Vektor $\mathbf{x}+h\,\mathbf{e}_j$ unterscheidet sich von $\mathbf{x}$ nur in der $j$-ten Komponente, und zwar um $h$. Die Definition ist also die gewöhnliche Ableitung aus Abschnitt [1.2](die-ableitung.html#stufe-1-2), angewandt auf die Funktion, die man erhält, wenn man alle Variablen außer $x_j$ festhält. Daraus folgt die Rechenregel: Man leitet nach $x_j$ ab und behandelt alle anderen Variablen wie Konstanten. Das Zeichen $\partial$ ist ein gerundetes d und erinnert daran, dass nur ein Teil der Variablen sich bewegt.

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ behandelt man beim Ableiten nach $x_1$ die Variable $x_2$ als Konstante und umgekehrt:

$$\frac{\partial f}{\partial x_1}=2x_1\,x_2,\qquad \frac{\partial f}{\partial x_2}=x_1^2+2x_2 .$$

An der Stelle $(1,\,2)$ ergibt das $4$ und $5$. Mit den Schnittkurven sieht man dasselbe (Abb. [6](#abb-6)): Hält man $x_2=2$ fest, bleibt $f(x_1,2)=2x_1^2+4$ mit der Steigung $4x_1=4$ an der Stelle $x_1=1$. Hält man $x_1=1$ fest, bleibt $f(1,x_2)=x_2+x_2^2$ mit der Steigung $1+2x_2=5$ an der Stelle $x_2=2$.

:::abbildung ml/k3schnitt 6
Partielle Ableitungen als Steigungen von Schnittkurven, für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$. (a) Höhenlinien zu den Werten $2$, $4$, $6$ (schwarz), $8$ und $10$, dazu die beiden Schnittgeraden durch $(1,\,2)$. (b) Entlang der blauen Geraden $x_2=2$ verläuft das Gelände wie $2x_1^2+4$, mit der Steigung $4$ bei $x_1=1$. (c) Entlang der roten Geraden $x_1=1$ verläuft es wie $x_2+x_2^2$, mit der Steigung $5$ bei $x_2=2$.
:::

⁠**Kurz gesagt:** Die partielle Ableitung $\partial f/\partial x_j$ ist die Steigung in Richtung der $x_j$-Achse: Man leitet nach $x_j$ ab und hält alle anderen Variablen fest.

### Der Gradient

<span class="anker" id="stufe-3-3"></span>

Eine Funktion von $d$ Variablen hat an jeder Stelle $d$ partielle Ableitungen. Man fasst sie zu einem Vektor zusammen, damit man mit ihnen so rechnen kann wie mit $\mathbf{x}$ selbst.

:::definition Definition 3.3 (Gradient)
<span class="anker" id="satz-3-3"></span>

Existieren an der Stelle $\mathbf{x}$ alle partiellen Ableitungen von $f:\mathbb{R}^d\to\mathbb{R}$, so heißt der Spaltenvektor

<span class="anker" id="gl-3-3"></span>
$$\nabla f(\mathbf{x})=\begin{pmatrix}\partial_1f(\mathbf{x})\\ \vdots\\ \partial_df(\mathbf{x})\end{pmatrix}\in\mathbb{R}^d \tag{3.3}$$

der __Gradient__ von $f$ an der Stelle $\mathbf{x}$. Das Zeichen $\nabla$ liest man „Nabla“.
:::

Der Gradient hat dieselbe Form wie $\mathbf{x}$: einen Eintrag je Variable, als Spalte geschrieben. Diese Vereinbarung gilt im ganzen Kapitel; Abschnitt [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) kommt darauf zurück, weil nicht alle Bücher sie so treffen. Ordnet man jedem Punkt $\mathbf{x}$ seinen Gradienten zu, so entsteht ein Feld von Pfeilen, einer an jedem Ort der Landkarte. Wohin diese Pfeile zeigen, klärt Abschnitt [4](richtungsableitung-und-steilster-anstieg.html#stufe-4).

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ ist

$$\nabla f(\mathbf{x})=\begin{pmatrix}2x_1x_2\\ x_1^2+2x_2\end{pmatrix},\qquad \nabla f(1,2)=\begin{pmatrix}4\\5\end{pmatrix},\qquad \nabla f(0,1)=\begin{pmatrix}0\\2\end{pmatrix} .$$

Für die quadratische Summe $f(\mathbf{x})=x_1^2+x_2^2+x_3^2$ ist $\nabla f(\mathbf{x})=(2x_1,\,2x_2,\,2x_3)^{\top}=2\mathbf{x}$.

⁠**Kurz gesagt:** Der Gradient ist der Spaltenvektor aller partiellen Ableitungen, mit derselben Form wie $\mathbf{x}$.

### Die lineare Näherung im Raum

<span class="anker" id="stufe-3-4"></span>

Für eine Variable ersetzt die Tangente die Funktion in der Nähe einer Stelle. Bei zwei Variablen tritt an ihre Stelle eine Ebene. Unter der Lupe sieht ein glattes Gelände in der Nähe eines Punkts wie eine schräg gestellte Platte aus: Das ist die __Tangentialebene__. Eine Ebene durch den Punkt $(\mathbf{x},\,f(\mathbf{x}))$ hat die Form $f(\mathbf{x})+m_1h_1+m_2h_2$, wobei $\mathbf{h}=(h_1,\,h_2)^{\top}$ die Verschiebung auf der Landkarte ist und $m_1$, $m_2$ die Neigungen der Platte in Richtung der beiden Achsen sind. Soll sie sich dem Gelände anschmiegen, müssen ihre Neigungen entlang der Achsen mit den Steigungen der Schnittkurven übereinstimmen, also $m_j=\partial_jf(\mathbf{x})$.

Daraus ergibt sich die lineare Näherung für viele Variablen:

<span class="anker" id="gl-3-4"></span>
$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=f(\mathbf{x})+\sum_{j=1}^d\partial_jf(\mathbf{x})\,h_j . \tag{3.4}$$

Die Formel sagt etwas Bemerkenswertes: Verändert man mehrere Eingänge zugleich um kleine Beträge, so *addieren sich ihre Wirkungen*. Jede Variable trägt $\partial_jf\cdot h_j$ bei, als wäre sie allein verändert worden. Bei großen Änderungen stimmt das nicht mehr, denn dann beeinflussen die Variablen gegenseitig ihre Wirkung, wie bei $x_1^2x_2$. Bei kleinen Änderungen sind diese Wechselwirkungen Produkte kleiner Größen und verschwinden schneller als die Einzelwirkungen, genau wie das Eckstück in der Produktregel.

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $\mathbf{x}=(1,\,2)^{\top}$ und die Verschiebung $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$ ist

$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=6+4\cdot0{,}01+5\cdot0{,}02=6+0{,}14=6{,}14 .$$

Genau ist $f(1{,}01;\ 2{,}02)=1{,}0201\cdot2{,}02+2{,}02^2=2{,}060602+4{,}0804=6{,}141002$. Der Fehler $0{,}001002$ ist viel kleiner als die Änderung $0{,}14$ selbst. Abb. [7](#abb-7) zeigt das Skalarprodukt Schritt für Schritt.

:::abbildung ml/k3rlinear 7
Die Änderung der linearen Näherung als Skalarprodukt aus Gradient und Verschiebung: Jede Variable trägt ihre partielle Ableitung mal ihre eigene Änderung bei.
:::

⁠**Kurz gesagt:** Nahe bei $\mathbf{x}$ ist $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$: Bei kleinen Änderungen addieren sich die Wirkungen der einzelnen Variablen.

### Differenzierbarkeit

<span class="anker" id="stufe-3-5"></span>

Die Näherung [(3.4)](#gl-3-4) wurde bisher nur plausibel gemacht. Für eine Variable folgte sie aus der Existenz der Ableitung. Bei mehreren Variablen genügt die Existenz der partiellen Ableitungen dafür nicht, wie das Gegenbeispiel unten zeigt. Man fordert deshalb die Näherung selbst: Ihr Fehler soll schneller verschwinden als die Verschiebung, so wie in [(1.4)](die-ableitung.html#gl-1-4) der Fehler $r(h)$ schneller verschwand als $h$. Durch einen Vektor kann man nicht teilen; statt durch $h$ teilt man deshalb durch die Länge $\lVert\mathbf{h}\rVert$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 3.1.

:::definition Definition 3.4 (Differenzierbarkeit)
<span class="anker" id="satz-3-4"></span>

Eine Funktion $f:\mathbb{R}^d\to\mathbb{R}$ heißt an der Stelle $\mathbf{x}$ __differenzierbar__, wenn es einen Vektor $\mathbf{g}\in\mathbb{R}^d$ gibt mit

<span class="anker" id="gl-3-5"></span>
$$\lim_{\mathbf{h}\to\mathbf{0}}\frac{f(\mathbf{x}+\mathbf{h})-f(\mathbf{x})-\mathbf{g}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=0 . \tag{3.5}$$

Der Grenzwert $\mathbf{h}\to\mathbf{0}$ bedeutet: Der Quotient liegt beliebig nah bei $0$, sobald $\lVert\mathbf{h}\rVert$ klein genug und $\mathbf{h}\ne\mathbf{0}$ ist, gleichgültig, aus welcher Richtung $\mathbf{h}$ sich nähert.
:::

:::satz Satz 3.5 (Differenzierbar heißt: Gradient und lineare Näherung)
<span class="anker" id="satz-3-5"></span>

Ist $f$ an der Stelle $\mathbf{x}$ differenzierbar, so existieren dort alle partiellen Ableitungen, und der Vektor in [(3.5)](#gl-3-5) ist der Gradient: $\mathbf{g}=\nabla f(\mathbf{x})$. Umgekehrt ist $f$ an der Stelle $\mathbf{x}$ differenzierbar, wenn alle partiellen Ableitungen in der Nähe von $\mathbf{x}$ existieren und an der Stelle $\mathbf{x}$ stetig sind.
:::

:::beweis Der Vektor ist der Gradient
Man wählt in [(3.5)](#gl-3-5) speziell $\mathbf{h}=t\,\mathbf{e}_j$ mit einer Zahl $t\ne0$; dann ist $\lVert\mathbf{h}\rVert=|t|$ und $\mathbf{g}^{\top}\mathbf{h}=t\,g_j$. Der Quotient lautet $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})-t\,g_j}{|t|}$ und geht gegen $0$. Dann geht auch $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})}{t}-g_j$ gegen $0$, denn diese Zahl hat denselben Betrag. Also existiert die partielle Ableitung nach $x_j$, und sie ist $g_j$. Das gilt für jedes $j$.
:::

Für die Praxis ist die zweite Aussage wichtig. Polynome, die e-Funktion, die logistische Funktion und alles, was man durch Grundrechenarten und Verkettung daraus baut, haben überall dort stetige partielle Ableitungen, wo sie erklärt sind. Solche Funktionen sind also differenzierbar, und für sie gilt [(3.4)](#gl-3-4). Ausnahmen in diesem Kapitel sind Knicke, wie bei $|x|$ oder $\max(x,\,0)$.

:::warnung Partielle Ableitungen allein genügen nicht
Die Funktion $f(x_1,x_2)=\dfrac{x_1x_2}{x_1^2+x_2^2}$ mit $f(0,0)=0$ ist auf beiden Achsen null, denn dort ist $x_1x_2=0$. Ihre Schnittkurven durch den Nullpunkt entlang der Achsen sind also waagrecht: $\partial_1f(0,0)=\partial_2f(0,0)=0$, der Gradient im Nullpunkt ist $\mathbf{0}$. Die lineare Näherung sagt deshalb voraus, dass $f$ in der Nähe des Nullpunkts fast $0$ ist. Auf der Diagonalen $x_1=x_2=t$ mit $t\ne0$ ist aber $f(t,t)=t^2/(2t^2)=\tfrac12$, ganz gleich wie klein $t$ ist. Die Funktion springt im Nullpunkt, und keine Ebene schmiegt sich ihr an. Sie ist dort nicht differenzierbar, obwohl beide partiellen Ableitungen existieren. Wer aus der Existenz des Gradienten auf die lineare Näherung schließt, braucht deshalb die Differenzierbarkeit, zum Beispiel über stetige partielle Ableitungen.
:::

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ sind die partiellen Ableitungen $2x_1x_2$ und $x_1^2+2x_2$ Polynome, also überall stetig, und $f$ ist überall differenzierbar. Im Rechenbeispiel zu [(3.4)](#gl-3-4) war der Fehler $0{,}001002$ bei $\lVert\mathbf{h}\rVert=\sqrt{0{,}0001+0{,}0004}\approx0{,}0224$, der Quotient aus [(3.5)](#gl-3-5) also etwa $0{,}045$. Halbiert man $\mathbf{h}$ auf $(0{,}005;\ 0{,}01)^{\top}$, so ist der Fehler $f(1{,}005;\ 2{,}01)-6-0{,}07=0{,}000250\ldots$ und der Quotient etwa $0{,}022$: Er halbiert sich mit $\mathbf{h}$ und geht gegen $0$.

⁠**Kurz gesagt:** Differenzierbar heißt, dass die lineare Näherung mit dem Gradienten einen Fehler hat, der schneller als $\lVert\mathbf{h}\rVert$ verschwindet; stetige partielle Ableitungen garantieren das, ihre bloße Existenz nicht.

:::hintergrund Warum stetige partielle Ableitungen genügen
Man geht von $\mathbf{x}$ nach $\mathbf{x}+\mathbf{h}$ nicht schräg, sondern in zwei Etappen parallel zu den Achsen: zuerst um $h_1$ in Richtung $x_1$, dann um $h_2$ in Richtung $x_2$. Auf jeder Etappe ändert sich nur eine Variable, und nach dem Mittelwertsatz für eine Variable ist die Änderung genau $\partial_jf\cdot h_j$, ausgewertet an einer Zwischenstelle der Etappe. Sind die partiellen Ableitungen stetig, liegen ihre Werte an den Zwischenstellen nahe bei den Werten an der Stelle $\mathbf{x}$, und die Summe der beiden Etappen unterscheidet sich von $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ nur um einen Betrag, der schneller als $\lVert\mathbf{h}\rVert$ verschwindet. Beim Gegenbeispiel bricht genau dieser Schritt zusammen: Seine partiellen Ableitungen sind außerhalb des Nullpunkts zwar vorhanden, aber nicht stetig. Auf der Achse $x_1=0$ ist etwa $\partial_1f(0,x_2)=1/x_2$, und das wird beliebig groß, je näher man dem Nullpunkt kommt, wo der Wert $0$ ist.
:::

:::aufgabe Aufgabe 9 ★ Partielle Ableitungen und Gradienten
<span class="anker" id="aufg-9"></span>

Berechne die partiellen Ableitungen und den Gradienten an der angegebenen Stelle.

<ol class="al">

<li>

$f(\mathbf{x})=3x_1-2x_2+5$ an der Stelle $(4,\,-1)$;

</li>

<li>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ an den Stellen $(2,\,0)$ und $(1,\,1)$;

</li>

<li>

$f(\mathbf{x})=x_1x_2+x_2x_3+x_3x_1$ an der Stelle $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3$, $\partial_2f=-2$, also $\nabla f=(3,\,-2)^{\top}$ an jeder Stelle.

(b) $\partial_1f=\mathrm{e}^{x_2}$ und $\partial_2f=x_1\mathrm{e}^{x_2}$. An der Stelle $(2,\,0)$ ist $\nabla f=(1,\,2)^{\top}$, an der Stelle $(1,\,1)$ ist $\nabla f=(\mathrm{e},\,\mathrm{e})^{\top}\approx(2{,}718;\ 2{,}718)^{\top}$.

(c) $\partial_1f=x_2+x_3$, $\partial_2f=x_1+x_3$, $\partial_3f=x_1+x_2$; an der Stelle $(1,\,2,\,3)$ also $\nabla f=(5,\,4,\,3)^{\top}$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Lineare Näherung mit zwei Variablen
<span class="anker" id="aufg-10"></span>

Es sei $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$.

<ol class="al">

<li>

Berechne mit der linearen Näherung an der Stelle $(2,\,0)$ einen Näherungswert für $f(2{,}1;\ -0{,}05)$ und vergleiche mit dem genauen Wert.

</li>

<li>

Welche der beiden Änderungen trägt mehr zur Änderung von $f$ bei? Warum heben sie sich in der linearen Näherung genau auf, im genauen Wert aber nicht?

</li>

</ol>

:::loesung
(a) Es ist $f(2,0)=2$ und $\nabla f(2,0)=(1,\,2)^{\top}$ nach Aufgabe [9](#aufg-9). Mit $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$:

$$f(2{,}1;\ -0{,}05)\approx2+1\cdot0{,}1+2\cdot(-0{,}05)=2+0{,}1-0{,}1=2{,}0 .$$

Genau ist $2{,}1\,\mathrm{e}^{-0{,}05}\approx2{,}1\cdot0{,}951229\approx1{,}99758$. Der Fehler ist etwa $0{,}0024$.

(b) Beide Änderungen tragen gleich viel bei, $+0{,}1$ und $-0{,}1$, und heben sich in der linearen Näherung auf. Im genauen Wert beeinflussen sich die Variablen aber gegenseitig: Wird $x_1$ größer, so reagiert $f$ stärker auf $x_2$, denn $\partial_2f=x_1\mathrm{e}^{x_2}$ wächst mit $x_1$. Die Verkleinerung von $x_2$ wirkt deshalb etwas stärker, als die lineare Näherung annimmt. Solche Wechselwirkungen sind Produkte zweier Änderungen, hier etwa $0{,}1\cdot(-0{,}05)=-0{,}005$, und gehören zu den Gliedern zweiter Ordnung, die die lineare Näherung weglässt. Abschnitt [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) rechnet sie aus (Aufgabe [29](die-hesse-matrix-und-die-quadratische-naherung.html#aufg-29)).
:::
:::

:::aufgabe Aufgabe 11 ★★ Höhenlinien und Schnittkurven
<span class="anker" id="aufg-11"></span>

Es sei $f(\mathbf{x})=x_1^2x_2+x_2^2$ wie in [(3.1)](#gl-3-1).

<ol class="al">

<li>

Welchen Wert hat $f$ an der Stelle $(2,\,1)$? Gib einen weiteren Punkt derselben Höhenlinie mit $x_1=0$ an.

</li>

<li>

Berechne $\nabla f(2,1)$ und die Gleichungen der beiden Schnittkurven durch $(2,\,1)$. Prüfe ihre Steigungen.

</li>

</ol>

:::loesung
(a) $f(2,1)=4\cdot1+1=5$. Mit $x_1=0$ verlangt die Höhenlinie $x_2^2=5$, also liegt etwa $(0;\ \sqrt5)\approx(0;\ 2{,}236)$ darauf.

(b) $\nabla f(2,1)=(2\cdot2\cdot1,\ 4+2\cdot1)^{\top}=(4,\,6)^{\top}$. Die Schnittkurve entlang $x_2=1$ ist $f(x_1,1)=x_1^2+1$ mit der Steigung $2x_1=4$ bei $x_1=2$. Die Schnittkurve entlang $x_1=2$ ist $f(2,x_2)=4x_2+x_2^2$ mit der Steigung $4+2x_2=6$ bei $x_2=1$. Beide Steigungen stimmen mit den Komponenten des Gradienten überein.
:::
:::

:::aufgabe Aufgabe 12 ★★★ Stetig, aber nicht differenzierbar
<span class="anker" id="aufg-12"></span>

Es sei $f(x_1,x_2)=\sqrt{|x_1x_2|}$.

<ol class="al">

<li>

Zeige, dass beide partiellen Ableitungen im Nullpunkt existieren und $0$ sind.

</li>

<li>

Zeige mit $\mathbf{h}=(t,\,t)^{\top}$, dass der Quotient in [(3.5)](#gl-3-5) mit $\mathbf{g}=\mathbf{0}$ nicht gegen $0$ geht. Warum folgt daraus, dass $f$ im Nullpunkt nicht differenzierbar ist, obwohl $f$ dort stetig ist?

</li>

</ol>

:::loesung
(a) Auf beiden Achsen ist $x_1x_2=0$, also $f=0$. Damit ist $\frac{f(h,0)-f(0,0)}{h}=0$ für jedes $h\ne0$, und ebenso für die zweite Variable. Beide partiellen Ableitungen im Nullpunkt sind $0$.

(b) Wäre $f$ im Nullpunkt differenzierbar, so müsste der Vektor in [(3.5)](#gl-3-5) nach dem Satz in Abschnitt [3.5](#stufe-3-5) der Gradient $\mathbf{0}$ sein. Mit $\mathbf{h}=(t,\,t)^{\top}$ ist aber $f(\mathbf{h})=\sqrt{t^2}=|t|$ und $\lVert\mathbf{h}\rVert=\sqrt2\,|t|$, also

$$\frac{f(\mathbf{h})-f(\mathbf{0})-\mathbf{0}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=\frac{|t|}{\sqrt2\,|t|}=\frac1{\sqrt2}\approx0{,}707 ,$$

für jedes noch so kleine $t\ne0$. Der Quotient geht nicht gegen $0$, also ist $f$ nicht differenzierbar. Stetig ist $f$ trotzdem, denn $|f(\mathbf{x})|=\sqrt{|x_1|\,|x_2|}\le\max(|x_1|,|x_2|)\le\lVert\mathbf{x}\rVert$ geht gegen $0$, wenn $\mathbf{x}$ gegen $\mathbf{0}$ geht. Das Gelände hat im Nullpunkt keine Lücke, aber entlang der Diagonalen eine Falte, an die sich keine Ebene anschmiegt.
:::
:::
