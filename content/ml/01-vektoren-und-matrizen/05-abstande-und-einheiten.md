---
title: Abstände und Einheiten
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6210500
summary: Zwei Beispiele sind sich ähnlich, wenn ihre Vektoren nah beieinanderliegen.
tags: Abstand, Merkmalsspalte, zentrierte, Standardabweichung, standardisiert
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Zwei Beispiele sind sich ähnlich, wenn ihre Vektoren nah beieinanderliegen. Dieser Abschnitt misst Abstände, zeigt, dass das Ergebnis von den gewählten Einheiten abhängt, und stellt ein Verfahren vor, das die Merkmale vergleichbar macht.
:::

### Der Abstand zweier Datenpunkte

<span class="anker" id="stufe-4-1"></span>

Zwei Wohnungen sind sich ähnlich, wenn sie sich in allen Merkmalen nur wenig unterscheiden. Die Unterschiede stehen im Differenzvektor $\mathbf{u}-\mathbf{v}$, dem Pfeil von einem Punkt zum anderen. Wie groß dieser Pfeil ist, sagt eine Norm.

:::definition Definition 4.1 (Abstand)
<span class="anker" id="satz-4-1"></span>

Der __Abstand__ zweier Vektoren $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ bezüglich einer Norm ist die Norm ihrer Differenz, $\lVert\mathbf{u}-\mathbf{v}\rVert$. Ohne weitere Angabe ist der euklidische Abstand gemeint.
:::

Aus den Eigenschaften einer Norm folgen die Eigenschaften, die man von einem Abstand erwartet: Er ist nie negativ und nur für gleiche Punkte null; er ist von $\mathbf{u}$ nach $\mathbf{v}$ genauso groß wie von $\mathbf{v}$ nach $\mathbf{u}$, weil $\mathbf{v}-\mathbf{u}=-(\mathbf{u}-\mathbf{v})$ ist; und der Weg über einen dritten Punkt $\mathbf{q}$ ist nie kürzer, $\lVert\mathbf{u}-\mathbf{v}\rVert\le\lVert\mathbf{u}-\mathbf{q}\rVert+\lVert\mathbf{q}-\mathbf{v}\rVert$. Das ist die Dreiecksungleichung (N3), angewandt auf $\mathbf{u}-\mathbf{v}=(\mathbf{u}-\mathbf{q})+(\mathbf{q}-\mathbf{v})$.

**Abstand und Skalarprodukt.** Multipliziert man das Quadrat des euklidischen Abstands mit den Rechenregeln des Skalarprodukts aus, so erhält man

<span class="anker" id="gl-4-1"></span>
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=(\mathbf{u}-\mathbf{v})^{\top}(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v} . \tag{4.1}$$

Bei festen Längen gilt also: Je größer das Skalarprodukt, desto kleiner der Abstand. Beide messen Ähnlichkeit, nur in entgegengesetzter Richtung.

⁠**Rechenbeispiel:** Die Wohnungen 1 und 2 unterscheiden sich um $\mathbf{x}_1-\mathbf{x}_2=(20,\,1,\,2)^{\top}$. Ihr euklidischer Abstand ist $\sqrt{405}\approx20{,}12$ (Abb. [18](#abb-18)), in der Betragssummennorm $20+1+2=23$, in der Maximumnorm $20$.

:::abbildung ml/k1rabstand 18
Der euklidische Abstand der Wohnungen 1 und 2: zuerst die Differenz, dann ihre Länge.
:::

Zur Probe von [(4.1)](#gl-4-1) mit $\mathbf{u}=(1,\,2,\,2)^{\top}$ und $\mathbf{v}=(2,\,0,\,1)^{\top}$: links $\lVert(-1,\,2,\,1)^{\top}\rVert^2=6$, rechts $9+5-2\cdot4=6$.

⁠**Kurz gesagt:** Der Abstand zweier Datenpunkte ist die Norm ihrer Differenz; nah beieinander heißt ähnlich.

### Abstände hängen von den Einheiten ab

<span class="anker" id="stufe-4-2"></span>

Im Rechenbeispiel eben ist der Abstand $20{,}12$ fast genau der Flächenunterschied von $20\,\mathrm m^2$. Von $405$ im Quadrat des Abstands stammen $400$ aus der Fläche. Der Unterschied von einem Zimmer und zwei Kilometern spielt praktisch keine Rolle, und zwar nur deshalb, weil Flächen in Quadratmetern große Zahlen sind.

Drei andere Wohnungen zeigen, was daraus folgt. Gefragt ist, welche der Wohnungen B und C der Wohnung A am ähnlichsten ist:

$$\text{A}=(60,\,2)^{\top},\qquad \text{B}=(63,\,4)^{\top},\qquad \text{C}=(54,\,2)^{\top}\qquad(\text{Fläche in m}^2,\ \text{Zimmer}).$$

In Quadratmetern ist $\lVert\text{A}-\text{B}\rVert=\sqrt{9+4}\approx3{,}61$ und $\lVert\text{A}-\text{C}\rVert=\sqrt{36+0}=6$: B ist näher. Misst man die Fläche in Einheiten von $10\,\mathrm m^2$, so ist $\text{A}=(6,\,2)^{\top}$, $\text{B}=(6{,}3;\ 4)^{\top}$, $\text{C}=(5{,}4;\ 2)^{\top}$ und $\lVert\text{A}-\text{B}\rVert=\sqrt{0{,}09+4}\approx2{,}02$, $\lVert\text{A}-\text{C}\rVert=0{,}6$: Jetzt ist C näher. Abbildung [19](#abb-19) zeigt beide Bilder.

:::abbildung ml/k1einheiten 19
Dieselben drei Wohnungen, links mit der Fläche in $\mathrm m^2$, rechts in Einheiten von $10\,\mathrm m^2$. Beide Achsen eines Bildes sind gleich skaliert, sodass die Länge einer Strecke der euklidische Abstand ist. Links liegt B näher an A (gestrichelt der Kreis durch B um A), rechts C.
:::

Der Mechanismus ist einfach. Im Quadrat des Abstands steht für jedes Merkmal der quadrierte Unterschied. Misst man ein Merkmal in einer anderen Einheit, ändern sich seine Zahlen um einen Faktor $c$, und sein Beitrag zum Quadrat des Abstands ändert sich um $c^2$. Die Beiträge der anderen Merkmale bleiben gleich. Ein Merkmal mit großen Zahlen bestimmt den Abstand fast allein, ein Merkmal mit kleinen Zahlen geht fast unter.

⁠**Kurz gesagt:** Abstände zwischen Beispielen hängen von den Einheiten der Merkmale ab; welches Beispiel einem anderen am ähnlichsten ist, kann sich durch einen Einheitenwechsel ändern.

:::hintergrund Jede Wahl der Einheiten ist eine Gewichtung
Der euklidische Abstand addiert Quadrate von Quadratmetern, Zimmern und Kilometern. Rechnerisch geht das, weil der Rechner nur Zahlen sieht. Physikalisch ist es eine Summe aus Größen verschiedener Art, und die Einheiten entscheiden, wie viel jede zählt. Wer die Fläche in $\mathrm m^2$ angibt, hat damit, ohne es zu wollen, entschieden, dass $1\,\mathrm m^2$ Unterschied genauso viel zählt wie ein Zimmer Unterschied. Es gibt keine von der Natur vorgegebene richtige Wahl. Man muss sie bewusst treffen, und das nächste Verfahren ist eine solche bewusste Wahl.
:::

### Abweichungen vom Mittelwert

<span class="anker" id="stufe-4-3"></span>

Um Merkmale vergleichbar zu machen, betrachtet man jedes Merkmal für sich über alle Beispiele hinweg. In Tabelle [1](vektoren-daten-als-zahlenlisten.html#tab-1) sind das die Spalten: Die Flächen aller Wohnungen bilden den Vektor $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}\in\mathbb{R}^4$. Ein solcher Vektor gehört zu einem Merkmal und hat so viele Komponenten, wie es Beispiele gibt. Er heißt hier die __Merkmalsspalte__.

Für den Vergleich zählt nicht, wie groß die Flächen sind, sondern wie stark sie sich unterscheiden. Man misst deshalb jede Fläche als Abweichung vom Durchschnitt. In der Elektrotechnik heißt dieser Schritt: den Gleichanteil abziehen und nur den Wechselanteil behalten.

:::definition Definition 4.2 (Zentrierter Vektor)
<span class="anker" id="satz-4-2"></span>

Für $\mathbf{v}\in\mathbb{R}^N$ mit dem Mittelwert $\bar v$ heißt

<span class="anker" id="gl-4-2"></span>
$$\tilde{\mathbf{v}}=\mathbf{v}-\bar v\,\mathbf 1=(v_1-\bar v,\,\dots,\,v_N-\bar v)^{\top} \tag{4.2}$$

der __zentrierte__ Vektor. Seine Komponenten sind die Abweichungen vom Mittelwert.
:::

Die Abweichungen heben sich immer gegenseitig auf: $\mathbf 1^{\top}\tilde{\mathbf{v}}=\mathbf 1^{\top}\mathbf{v}-\bar v\,\mathbf 1^{\top}\mathbf 1=N\bar v-\bar v\,N=0$. Der zentrierte Vektor hat also den Mittelwert null.

⁠**Rechenbeispiel:** Die Flächen $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}$ haben den Mittelwert $\bar v=65$. Zentriert ist $\tilde{\mathbf{v}}=(-5,\,-25,\,25,\,5)^{\top}$, und die Abweichungen addieren sich tatsächlich zu null (Abb. [20](#abb-20)). Die Zimmerzahlen $(2,\,1,\,4,\,3)^{\top}$ haben den Mittelwert $2{,}5$ und zentriert $(-0{,}5;\ -1{,}5;\ 1{,}5;\ 0{,}5)^{\top}$, die Entfernungen $(3,\,1,\,6,\,2)^{\top}$ den Mittelwert $3$ und zentriert $(0,\,-2,\,3,\,-1)^{\top}$.

:::abbildung ml/k1rzentriert 20
Der Mittelwert der Flächen und die Summe der Abweichungen vom Mittelwert, in $\mathrm m^2$.
:::

⁠**Kurz gesagt:** Zentrieren zieht von jeder Komponente den Mittelwert ab; übrig bleiben die Abweichungen, die sich zu null addieren.

### Die Standardabweichung

<span class="anker" id="stufe-4-4"></span>

Wie stark ein Merkmal schwankt, sieht man an der Größe seiner Abweichungen. Ein typischer Betrag einer Komponente ist der Effektivwert aus Unterabschnitt [3.6](normen-die-groe-eines-vektors.html#stufe-3-6). Angewandt auf den zentrierten Vektor, ist er die typische Abweichung vom Mittelwert. In der Sprache der Elektrotechnik: der Effektivwert des Wechselanteils.

:::definition Definition 4.3 (Standardabweichung)
<span class="anker" id="satz-4-3"></span>

Die __Standardabweichung__ eines Vektors $\mathbf{v}\in\mathbb{R}^N$ ist der Effektivwert seines zentrierten Vektors:

<span class="anker" id="gl-4-3"></span>
$$\operatorname{std}(\mathbf{v})=\operatorname{rms}(\tilde{\mathbf{v}})=\frac{\lVert\mathbf{v}-\bar v\,\mathbf 1\rVert}{\sqrt N}=\sqrt{\frac1N\sum_{i=1}^N(v_i-\bar v)^2} . \tag{4.3}$$
:::

Die Standardabweichung hat dieselbe Einheit wie das Merkmal. Sie ist genau dann null, wenn alle Komponenten gleich sind. Viele Texte teilen in [(4.3)](#gl-4-3) durch $N-1$ statt durch $N$. Bei vielen Beispielen ist der Unterschied klein. Diese Reihe teilt durch $N$ und sagt es dazu, wenn es einmal anders sein soll.

⁠**Rechenbeispiel:** Die zentrierten Flächen $(-5,\,-25,\,25,\,5)^{\top}$ haben die Quadratsumme $1\,300$, also ist $\operatorname{std}(\mathbf{v})=\sqrt{325}\approx18{,}03\,\mathrm m^2$ (Abb. [21](#abb-21)). Ebenso erhält man für die Zimmer $\sqrt{5/4}\approx1{,}118$ und für die Entfernungen $\sqrt{14/4}\approx1{,}871$ km.

:::abbildung ml/k1rstd 21
Die Standardabweichung der Flächen: Abweichungen quadrieren, mitteln, Wurzel ziehen. Das Ergebnis $\sqrt{325}\approx18{,}03$ hat die Einheit $\mathrm m^2$.
:::

⁠**Kurz gesagt:** Die Standardabweichung ist der Effektivwert der Abweichungen vom Mittelwert, die typische Schwankung eines Merkmals.

:::hintergrund Gleichanteil und Wechselanteil teilen sich die Leistung
Ein Vektor ist die Summe aus seinem Gleichanteil $\bar v\,\mathbf 1$ und seinem Wechselanteil $\tilde{\mathbf{v}}$. Für das Quadrat der Länge gilt nach den Rechenregeln des Skalarprodukts

$$\lVert\bar v\,\mathbf 1+\tilde{\mathbf{v}}\rVert^2=\bar v^2\,\mathbf 1^{\top}\mathbf 1+2\,\bar v\,\mathbf 1^{\top}\tilde{\mathbf{v}}+\lVert\tilde{\mathbf{v}}\rVert^2=N\bar v^2+0+\lVert\tilde{\mathbf{v}}\rVert^2 ,$$

weil sich die Abweichungen zu null addieren. Teilt man durch $N$, wird daraus $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$. Das ist dieselbe Aufteilung wie bei einem Mischstrom, dessen Leistung an einem Widerstand sich aus der Leistung des Gleichanteils und der des Wechselanteils zusammensetzt. Für die Flächen: $\operatorname{rms}^2=(3600+1600+8100+4900)/4=4550=65^2+325$.
:::

### Standardisieren

<span class="anker" id="stufe-4-5"></span>

Jetzt lässt sich jedes Merkmal in seiner eigenen typischen Schwankung messen. Statt „$25\,\mathrm m^2$ über dem Durchschnitt“ sagt man „$1{,}39$ Standardabweichungen über dem Durchschnitt“. In dieser Sprache hat jedes Merkmal dieselbe Größenordnung, gleichgültig, in welcher Einheit es ursprünglich gemessen wurde.

:::definition Definition 4.4 (Standardisieren)
<span class="anker" id="satz-4-4"></span>

Ein Merkmal $j$ mit dem Mittelwert $\bar x_j$ und der Standardabweichung $s_j>0$ seiner Merkmalsspalte wird __standardisiert__, indem man jeden Wert durch

<span class="anker" id="gl-4-4"></span>
$$z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad i=1,\dots,N, \tag{4.4}$$

ersetzt. Die Zahlen $z_{ij}$ heißen die standardisierten Werte.
:::

Die standardisierte Merkmalsspalte hat den Mittelwert $0$ und die Standardabweichung $1$, denn Zentrieren macht den Mittelwert zu null und die Division durch $s_j$ macht die typische Abweichung zu eins. Die Werte haben keine Einheit mehr.

⁠**Rechenbeispiel 1: der Wohnungsdatensatz.** Mit den Mittelwerten $65$, $2{,}5$, $3$ und den Standardabweichungen $18{,}03$, $1{,}118$, $1{,}871$ werden die vier Wohnungen zu

$$\begin{aligned} \mathbf{z}_1&\approx(-0{,}28;\ -0{,}45;\ 0)^{\top}, & \mathbf{z}_2&\approx(-1{,}39;\ -1{,}34;\ -1{,}07)^{\top},\\ \mathbf{z}_3&\approx(1{,}39;\ 1{,}34;\ 1{,}60)^{\top}, & \mathbf{z}_4&\approx(0{,}28;\ 0{,}45;\ -0{,}53)^{\top}. \end{aligned}$$

Alle drei Merkmale bewegen sich jetzt im selben Zahlenbereich.

⁠**Rechenbeispiel 2: A, B und C.** Die drei Wohnungen aus Unterabschnitt [4.2](#stufe-4-2) haben die mittlere Fläche $59\,\mathrm m^2$ mit der Standardabweichung $\sqrt{14}\approx3{,}74\,\mathrm m^2$ und im Mittel $8/3$ Zimmer mit der Standardabweichung $\sqrt{8/9}\approx0{,}943$. Nach dem Standardisieren ist $\lVert\text A-\text B\rVert\approx2{,}27$ und $\lVert\text A-\text C\rVert\approx1{,}60$. Am ähnlichsten ist A also C, und dieses Urteil hängt nicht mehr von der Einheit der Fläche ab.

Dass die Einheit herausfällt, gilt allgemein:

:::satz Satz 4.5 (Standardisierte Werte hängen nicht von der Einheit ab)
<span class="anker" id="satz-4-5"></span>

Rechnet man ein Merkmal in eine andere Einheit um, $v_i'=\alpha\,v_i+\beta$ für alle $i$ mit Zahlen $\alpha>0$ und $\beta$, so bleiben seine standardisierten Werte gleich.
:::

:::beweis Unabhängigkeit von der Einheit
Der Mittelwert wird zu $\bar v'=\frac1N\sum_i(\alpha\,v_i+\beta)=\alpha\,\bar v+\beta$, die Abweichungen zu $v_i'-\bar v'=\alpha\,(v_i-\bar v)$. Nach [(4.3)](#gl-4-3) ist dann $\operatorname{std}(\mathbf{v}')=|\alpha|\operatorname{std}(\mathbf{v})=\alpha\operatorname{std}(\mathbf{v})$. Im Quotienten [(4.4)](#gl-4-4) kürzt sich $\alpha$, und $\beta$ ist schon beim Zentrieren verschwunden.
:::

Der Summand $\beta$ deckt auch Umrechnungen mit verschobenem Nullpunkt ab, etwa von Grad Celsius in Grad Fahrenheit.

⁠**Kurz gesagt:** Standardisieren misst jedes Merkmal als Abweichung vom Mittelwert in Vielfachen seiner Standardabweichung; danach hängen Abstände nicht mehr von den Einheiten ab.

:::hintergrund Warum gerade die Standardabweichung als Maßstab?
Man braucht für jedes Merkmal einen Maßstab, der sich bei einem Einheitenwechsel genauso ändert wie die Zahlen selbst. Dann kürzt er sich heraus. Jede Größe, die aus den Daten des Merkmals berechnet wird und die Einheit des Merkmals hat, leistet das: die Standardabweichung, aber auch die Spannweite vom kleinsten zum größten Wert. Die Standardabweichung ist die übliche Wahl, weil sie alle Werte berücksichtigt und nicht nur die beiden äußersten.

Was das Standardisieren mit einem Abstand macht, sieht man, wenn man zwei standardisierte Beispiele $\mathbf{z}_a$ und $\mathbf{z}_b$ voneinander abzieht. Der Mittelwert fällt heraus, $z_{aj}-z_{bj}=(x_{aj}-x_{bj})/s_j$, und es bleibt

$$\lVert\mathbf{z}_a-\mathbf{z}_b\rVert^2=\sum_{j=1}^d\frac{(x_{aj}-x_{bj})^2}{s_j^2} .$$

Der Abstand der standardisierten Werte ist also der gewöhnliche Abstand, in dem der quadrierte Unterschied in Merkmal $j$ mit dem Gewicht $1/s_j^2$ zählt. Für die Wohnungen A und B ist das $3^2/14+2^2/(8/9)=9/14+9/2\approx5{,}14$, die Wurzel daraus $2{,}27$ wie oben.

Das Standardisieren ist aber selbst eine Entscheidung. Es gibt jedem Merkmal dasselbe Gewicht im Abstand, auch einem Merkmal, das für die Frage gar keine Rolle spielt. Und ein Merkmal, das in allen Beispielen denselben Wert hat, hat die Standardabweichung null und lässt sich nicht standardisieren; es unterscheidet die Beispiele aber auch nicht und trägt zu keinem Abstand etwas bei.
:::

:::aufgabe Aufgabe 9 ★ Gleichanteil und Wechselanteil
<span class="anker" id="aufg-9"></span>

Ein Signal hat die Abtastwerte $\mathbf{x}=(1,\,3,\,1,\,-1)^{\top}$. Berechne den Mittelwert, den zentrierten Vektor, die Standardabweichung und den Effektivwert. Prüfe $\operatorname{rms}(\mathbf{x})^2=\bar x^2+\operatorname{std}(\mathbf{x})^2$.

:::loesung
Der Mittelwert ist $\bar x=(1+3+1-1)/4=1$, der zentrierte Vektor $\tilde{\mathbf{x}}=(0,\,2,\,0,\,-2)^{\top}$. Die Standardabweichung ist $\sqrt{(0+4+0+4)/4}=\sqrt2\approx1{,}414$, der Effektivwert $\sqrt{(1+9+1+1)/4}=\sqrt3\approx1{,}732$. Probe: $\operatorname{rms}^2=3=1^2+(\sqrt2)^2=\bar x^2+\operatorname{std}^2$. Gleichanteil und Wechselanteil teilen sich die „Leistung“ $3$ im Verhältnis $1:2$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Wer ist Wohnung 1 am ähnlichsten?
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Berechne die euklidischen Abstände von Wohnung 1 zu den Wohnungen 2, 3 und 4 mit den Werten aus Tabelle [1](vektoren-daten-als-zahlenlisten.html#tab-1). Welcher Anteil des Abstandsquadrats zu Wohnung 2 stammt aus der Fläche?

</li>

<li>

Berechne dieselben Abstände mit den standardisierten Werten aus Unterabschnitt [4.5](#stufe-4-5). Welcher Anteil des Abstandsquadrats zu Wohnung 2 stammt jetzt aus der Fläche?

</li>

<li>

Welche Wohnung ist Wohnung 1 jeweils am ähnlichsten? Was hat das Standardisieren hier geändert, wenn nicht die Antwort?

</li>

</ol>

:::loesung
(a) Mit den Werten der Tabelle:

$$\begin{aligned} \lVert\mathbf{x}_1-\mathbf{x}_2\rVert&=\sqrt{20^2+1^2+2^2}=\sqrt{405}\approx20{,}12,\\ \lVert\mathbf{x}_1-\mathbf{x}_3\rVert&=\sqrt{30^2+2^2+3^2}=\sqrt{913}\approx30{,}22,\\ \lVert\mathbf{x}_1-\mathbf{x}_4\rVert&=\sqrt{10^2+1^2+1^2}=\sqrt{102}\approx10{,}10 . \end{aligned}$$

Von $405$ im Abstandsquadrat zu Wohnung 2 stammen $400$ aus der Fläche, also $98{,}8$ %.

(b) Mit den standardisierten Vektoren aus Unterabschnitt [4.5](#stufe-4-5) ist $\mathbf{z}_1-\mathbf{z}_2\approx(1{,}109;\ 0{,}894;\ 1{,}069)^{\top}$, mit den Quadraten $1{,}231$, $0{,}800$ und $1{,}143$. Der Abstand ist $\sqrt{3{,}174}\approx1{,}78$. Ebenso erhält man $\lVert\mathbf{z}_1-\mathbf{z}_3\rVert\approx2{,}92$ und $\lVert\mathbf{z}_1-\mathbf{z}_4\rVert\approx1{,}18$. Der Anteil der Fläche am Abstandsquadrat zu Wohnung 2 ist jetzt $1{,}231/3{,}174\approx38{,}8$ %.

(c) In beiden Fällen ist Wohnung 4 am ähnlichsten, gefolgt von Wohnung 2 und Wohnung 3. Die Reihenfolge ändert sich hier nicht, weil in diesem kleinen Datensatz große Wohnungen auch mehr Zimmer haben und weiter draußen liegen; alle drei Merkmale erzählen ungefähr dieselbe Geschichte. Geändert hat sich, *warum* Wohnung 4 am ähnlichsten ist: Roh entscheidet fast allein die Fläche, standardisiert tragen alle drei Merkmale etwa gleich viel bei. Dass die Antwort trotzdem gleich bleibt, ist ein Zufall dieser Daten; bei den Wohnungen A, B und C in Unterabschnitt [4.2](#stufe-4-2) hat sie sich geändert.
:::
:::

:::aufgabe Aufgabe 11 ★★ Celsius oder Fahrenheit
<span class="anker" id="aufg-11"></span>

An vier Tagen wurden mittags $10$, $20$, $15$ und $25$ $^\circ$C gemessen.

<ol class="al">

<li>

Rechne in Grad Fahrenheit um ($F=1{,}8\,C+32$). Berechne in beiden Einheiten Mittelwert und Standardabweichung.

</li>

<li>

Berechne die standardisierten Werte in beiden Einheiten und vergleiche.

</li>

<li>

Was passiert mit den standardisierten Werten, wenn man ein Merkmal mit einem negativen Faktor umrechnet, etwa $v_i'=-v_i$?

</li>

</ol>

:::loesung
(a) In Fahrenheit sind die Werte $1{,}8\cdot10+32=50$, $68$, $59$ und $77$. In Celsius ist der Mittelwert $17{,}5$ und die Standardabweichung $\sqrt{(56{,}25+6{,}25+6{,}25+56{,}25)/4}=\sqrt{31{,}25}\approx5{,}590$; in Fahrenheit ist der Mittelwert $63{,}5=1{,}8\cdot17{,}5+32$ und die Standardabweichung $\approx10{,}062=1{,}8\cdot5{,}590$. Der Summand $32$ verschiebt nur den Mittelwert, der Faktor $1{,}8$ streckt auch die Standardabweichung.

(b) In beiden Einheiten sind die standardisierten Werte $\approx(-1{,}342;\ 0{,}447;\ -0{,}447;\ 1{,}342)$. So verlangt es der Satz in Unterabschnitt [4.5](#stufe-4-5): Der Summand fällt beim Zentrieren heraus, der Faktor kürzt sich mit der Standardabweichung.

(c) Mit $v_i'=-v_i$ werden alle Abweichungen vom Mittelwert mit $-1$ multipliziert, die Standardabweichung aber mit $|-1|=1$. Die standardisierten Werte wechseln also ihr Vorzeichen. Für Abstände zwischen Beispielen ist das gleichgültig, denn $\lVert-\mathbf{u}\rVert=\lVert\mathbf{u}\rVert$; der Datensatz wird nur gespiegelt.
:::
:::
