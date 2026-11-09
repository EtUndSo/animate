---
title: Winkel und Ähnlichkeit
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
knoten: Grundlagen 1: Vektoren und Matrizen
nachschlagen: ja
order: 15210600
summary: Zwei Vektoren können in ähnliche Richtungen zeigen, auch wenn sie verschieden lang sind.
tags: Winkel, orthogonal, Kosinus-Ähnlichkeit
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Zwei Vektoren können in ähnliche Richtungen zeigen, auch wenn sie verschieden lang sind. Dieser Abschnitt misst den Winkel zwischen ihnen. Grundlage ist eine Ungleichung, die außerdem genau sagt, wann ein Mustervergleich am stärksten anschlägt.
:::

### Die Cauchy-Schwarz-Ungleichung

<span class="anker" id="stufe-5-1"></span>

Wie groß kann das Skalarprodukt zweier Vektoren werden, wenn ihre Längen feststehen? Ein Versuch: $\mathbf{u}=(1,\,2,\,2)^{\top}$ hat die Länge $3$, $\mathbf{v}=(2,\,0,\,1)^{\top}$ die Länge $\sqrt5\approx2{,}24$. Ihr Skalarprodukt ist $2+0+2=4$, deutlich weniger als das Produkt der Längen $3\cdot2{,}24\approx6{,}71$. Nimmt man stattdessen $\mathbf{v}=2\mathbf{u}$, einen Vektor in derselben Richtung mit der Länge $6$, so ist $\mathbf{u}^{\top}(2\mathbf{u})=2\cdot9=18=3\cdot6$: genau das Produkt der Längen. Mehr geht nicht.

:::satz Satz 5.1 (Cauchy-Schwarz-Ungleichung)
<span class="anker" id="satz-5-1"></span>

Für alle $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ gilt

<span class="anker" id="gl-5-1"></span>
$$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert . \tag{5.1}$$

Gleichheit gilt genau dann, wenn einer der beiden Vektoren ein Vielfaches des anderen ist.
:::

:::beweis Cauchy-Schwarz-Ungleichung
Ist $\mathbf{v}=\mathbf{0}$, sind beide Seiten null. Sonst betrachtet man für eine beliebige Zahl $t$ den Vektor $\mathbf{u}-t\,\mathbf{v}$. Das Quadrat seiner Länge ist nie negativ, und nach den Rechenregeln des Skalarprodukts ist

$$0\le\lVert\mathbf{u}-t\,\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2t\,\mathbf{u}^{\top}\mathbf{v}+t^2\lVert\mathbf{v}\rVert^2 .$$

Das gilt für jedes $t$, also auch für $t=\mathbf{u}^{\top}\mathbf{v}/\lVert\mathbf{v}\rVert^2$, die Stelle, an der die rechte Seite als Parabel in $t$ am kleinsten ist. Eingesetzt:

$$0\le\lVert\mathbf{u}\rVert^2-2\,\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}+\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}=\lVert\mathbf{u}\rVert^2-\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}.$$

Multipliziert mit $\lVert\mathbf{v}\rVert^2>0$ heißt das $(\mathbf{u}^{\top}\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$; die Wurzel daraus ist [(5.1)](#gl-5-1).

Gleichheit gilt genau dann, wenn $\lVert\mathbf{u}-t\,\mathbf{v}\rVert=0$ ist für dieses $t$, also $\mathbf{u}=t\,\mathbf{v}$. Umgekehrt ist für $\mathbf{u}=c\,\mathbf{v}$ tatsächlich $|\mathbf{u}^{\top}\mathbf{v}|=|c|\,\lVert\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{u}=(1,\,2,\,2)^{\top}$ und $\mathbf{v}=(2,\,0,\,1)^{\top}$ ist $|\mathbf{u}^{\top}\mathbf{v}|=4\le3\cdot\sqrt5\approx6{,}71$. Die Ungleichung ist streng, weil $\mathbf{v}$ kein Vielfaches von $\mathbf{u}$ ist.
::::

Mit der Ungleichung lässt sich nachholen, was in Unterabschnitt [3.4](normen-die-groe-eines-vektors.html#stufe-3-4) nur anschaulich begründet war: die Dreiecksungleichung der euklidischen Norm. Es ist

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2\le\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2=\bigl(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert\bigr)^2 ,$$

und die Wurzel daraus ist (N3).

⁠**Kurz gesagt:** Das Skalarprodukt ist dem Betrag nach höchstens das Produkt der Längen, und genau dann gleich, wenn die Vektoren auf einer Geraden durch den Nullpunkt liegen.

:::hintergrund Warum das Skalarprodukt Muster erkennt: die genaue Aussage
In Unterabschnitt [2.4](das-skalarprodukt.html#stufe-2-4) war der Mustervergleich eine Anschauung: Das Skalarprodukt $\mathbf{w}^{\top}\mathbf{x}$ ist groß, wenn das Signal dem Muster folgt. Die Cauchy-Schwarz-Ungleichung macht daraus eine genaue Aussage. Vergleicht man nur Signale mit derselben Länge $\lVert\mathbf{x}\rVert$, so liegt $\mathbf{w}^{\top}\mathbf{x}$ immer zwischen $-\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ und $+\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$. Den größten Wert erreicht genau das Signal, das ein positives Vielfaches des Musters ist, den kleinsten das negative Vielfache. Unter allen Signalen gleicher Energie schlägt der Vergleich also am stärksten beim Muster selbst an.

⁠**Rechenbeispiel:** Das Wechselmuster $\mathbf{w}=(1,-1,1,-1)^{\top}$ hat die Länge $2$. Unter allen Signalen der Länge $2$ liefert $\mathbf{x}=\mathbf{w}$ den größten Wert $4=2\cdot2$, das Signal $(2,0,0,0)^{\top}$ nur $2$ und $\mathbf{x}=-\mathbf{w}$ den kleinsten Wert $-4$.

In der Nachrichtentechnik ist das die Grundlage des Korrelationsempfängers und des signalangepassten Filters (*matched filter*). Ein solches Filter hat als Impulsantwort das zeitlich gespiegelte Sendesignal; zum Abtastzeitpunkt berechnet es dadurch genau das Skalarprodukt aus empfangenem Signal und Sendesignal. Dass dieses Filter das Verhältnis von Signal zu Rauschen größtmöglich macht, wird mit eben dieser Ungleichung bewiesen.
:::

### Der Winkel zwischen zwei Vektoren

<span class="anker" id="stufe-5-2"></span>

Zwei Pfeile, die vom Nullpunkt ausgehen, schließen einen Winkel ein. Er sagt, wie ähnlich ihre Richtungen sind, unabhängig davon, wie lang sie sind. In der Ebene kann man ihn mit dem Geodreieck messen. Für Vektoren mit vielen Komponenten braucht man eine Formel, und die liefert das Skalarprodukt.

:::herleitung Das Skalarprodukt in der Ebene
Die Pfeile $\mathbf{u}$ und $\mathbf{v}$ und ihr Verbindungspfeil $\mathbf{u}-\mathbf{v}$ bilden ein Dreieck. Ist $\varphi$ der Winkel zwischen $\mathbf{u}$ und $\mathbf{v}$, so sagt der Kosinussatz der Schulgeometrie

$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

Nach [(4.1)](abstande-und-einheiten.html#gl-4-1) ist dieselbe linke Seite gleich $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}$. Vergleicht man beide Zeilen, bleibt

$$\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

In der Ebene und im Raum ist das Skalarprodukt also das Produkt der Längen mal dem Kosinus des eingeschlossenen Winkels.
:::

In höheren Dimensionen gibt es kein Geodreieck. Man dreht die Herleitung deshalb um und benutzt die Formel als Definition.

:::definition Definition 5.2 (Winkel)
<span class="anker" id="satz-5-2"></span>

Für $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$, beide ungleich $\mathbf{0}$, ist der __Winkel__ $\varphi$ zwischen $\mathbf{u}$ und $\mathbf{v}$ die Zahl $\varphi\in[0^\circ,180^\circ]$ mit

<span class="anker" id="gl-5-2"></span>
$$\cos\varphi=\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert} . \tag{5.2}$$
:::

Diese Definition ist nur möglich, weil die rechte Seite nach der Cauchy-Schwarz-Ungleichung immer zwischen $-1$ und $1$ liegt. Zu jeder solchen Zahl gibt es genau einen Winkel zwischen $0^\circ$ und $180^\circ$. Am Vorzeichen des Skalarprodukts sieht man, ob der Winkel spitz ($\mathbf{u}^{\top}\mathbf{v}>0$), recht ($\mathbf{u}^{\top}\mathbf{v}=0$) oder stumpf ($\mathbf{u}^{\top}\mathbf{v}<0$) ist.

::::beispiel [Rechenbeispiel]
Für $(1,\,0)^{\top}$ und $(1,\,1)^{\top}$ ist $\cos\varphi=1/\sqrt2$, also $\varphi=45^\circ$. Für $(1,\,0,\,1)^{\top}$ und $(1,\,1,\,0)^{\top}$ ist $\cos\varphi=\tfrac12$, also $\varphi=60^\circ$ (Abb. [22](#abb-22)). Für $\mathbf{u}=(1,\,2,\,2)^{\top}$ und $\mathbf{v}=(2,\,0,\,1)^{\top}$ ist $\cos\varphi=4/(3\sqrt5)\approx0{,}596$, also $\varphi\approx53{,}4^\circ$.

:::abbildung ml/k1rwinkel 22
Der Winkel zwischen $(1,\,0,\,1)^{\top}$ und $(1,\,1,\,0)^{\top}$: im Zähler das Skalarprodukt, im Nenner die beiden Längen.
:::
::::

⁠**Kurz gesagt:** Der Kosinus des Winkels zwischen zwei Vektoren ist ihr Skalarprodukt geteilt durch das Produkt ihrer Längen.

### Orthogonale Vektoren

<span class="anker" id="stufe-5-3"></span>

Steht das Skalarprodukt zweier Vektoren auf null, so trägt keiner etwas in Richtung des anderen bei. In der Ebene stehen die Pfeile dann senkrecht aufeinander. Dieser Fall ist so wichtig, dass er einen eigenen Namen hat.

:::definition Definition 5.3 (Orthogonal)
<span class="anker" id="satz-5-3"></span>

Zwei Vektoren $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ heißen __orthogonal__, wenn $\mathbf{u}^{\top}\mathbf{v}=0$ ist.
:::

Sind beide Vektoren ungleich $\mathbf{0}$, so ist ihr Winkel nach [(5.2)](#gl-5-2) genau $90^\circ$. Der Nullvektor ist zu jedem Vektor orthogonal.

:::satz Satz 5.4 (Satz des Pythagoras)
<span class="anker" id="satz-5-4"></span>

Sind $\mathbf{u}$ und $\mathbf{v}$ orthogonal, so ist $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$.
:::

Das folgt sofort aus $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$, denn der mittlere Summand ist null.

::::beispiel [Rechenbeispiel 1]
$(1,\,2,\,2)^{\top}$ und $(2,\,0,\,-1)^{\top}$ sind orthogonal, denn $2+0-2=0$. Ihre Summe $(3,\,2,\,1)^{\top}$ hat das Längenquadrat $14=9+5$.
::::

::::beispiel [Rechenbeispiel 2] zwei Muster, die sich nicht stören
Das Gleichmuster $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ und das Wechselmuster $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ aus Unterabschnitt [2.4](das-skalarprodukt.html#stufe-2-4) sind orthogonal, $\mathbf 1^{\top}\mathbf{w}=0$. Ein Signal, das aus $2$-mal dem Gleichmuster und $1$-mal dem Wechselmuster besteht, ist $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}=(3,\,1,\,3,\,1)^{\top}$. Der Vergleich mit dem Gleichmuster ergibt $\mathbf 1^{\top}\mathbf{x}=8=2\cdot4$, der Vergleich mit dem Wechselmuster $\mathbf{w}^{\top}\mathbf{x}=4=1\cdot4$ (Abb. [23](#abb-23)). Jeder Vergleich findet genau seinen eigenen Anteil, mal $\lVert\mathbf 1\rVert^2=\lVert\mathbf{w}\rVert^2=4$; der andere Anteil stört ihn nicht.

:::abbildung ml/k1rortho 23
Die beiden Muster sind orthogonal (oben). Der Vergleich des Signals $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}$ mit jedem Muster liefert dessen Anteil mal $4$.
:::
::::

⁠**Kurz gesagt:** Orthogonal heißt Skalarprodukt null; orthogonale Pfeile stehen senkrecht aufeinander, und für sie gilt der Satz des Pythagoras.

:::hintergrund Warum orthogonale Muster sich nicht stören, und was das mit Fourier-Koeffizienten zu tun hat
Ist ein Signal eine Linearkombination $\mathbf{x}=\alpha\,\mathbf 1+\beta\,\mathbf{w}$ zweier orthogonaler Muster, so ist nach den Rechenregeln

$$\mathbf 1^{\top}\mathbf{x}=\alpha\,\mathbf 1^{\top}\mathbf 1+\beta\,\mathbf 1^{\top}\mathbf{w}=\alpha\,\lVert\mathbf 1\rVert^2+0 ,\qquad\text{also}\qquad \alpha=\frac{\mathbf 1^{\top}\mathbf{x}}{\lVert\mathbf 1\rVert^2} .$$

Der Vergleich mit einem Muster misst also nur dessen eigenen Anteil, weil der Beitrag des anderen Musters mit dem Faktor $\mathbf 1^{\top}\mathbf{w}=0$ verschwindet. Wären die Muster nicht orthogonal, würde jeder Vergleich auch ein Stück des anderen Anteils mitzählen.

Genau so sind die Koeffizienten einer Fourier-Reihe gebaut. Für ein Signal $s(t)$ mit der Periode $T$ und $\omega_0=2\pi/T$ ist

$$a_k=\frac{2}{T}\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t=\frac{\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t}{\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t}\qquad(k\ge1),$$

denn $\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t=T/2$. Das Integral über ein Produkt zweier Funktionen spielt die Rolle des Skalarprodukts, und die Kosinus- und Sinusfunktionen verschiedener Frequenzen sind in diesem Sinn orthogonal: Das Integral ihres Produkts über eine Periode ist null. Deshalb kann man jeden Fourier-Koeffizienten für sich ausrechnen, ohne die anderen zu kennen.
:::

### Die Kosinus-Ähnlichkeit

<span class="anker" id="stufe-5-4"></span>

Manchmal ist die Länge eines Vektors Nebensache. Ein Text lässt sich durch einen Vektor beschreiben, dessen Komponente $j$ zählt, wie oft das Wort $j$ einer festen Wortliste im Text vorkommt. Ein ausführlicher Bericht über ein Fußballspiel enthält die Wörter „Tor“ und „Ball“ öfter als eine kurze Meldung über dasselbe Spiel, aber im selben Verhältnis. Die beiden Vektoren sind verschieden lang, zeigen aber in dieselbe Richtung. Für den Inhalt zählt die Richtung.

:::definition Definition 5.5 (Kosinus-Ähnlichkeit)
<span class="anker" id="satz-5-5"></span>

Die __Kosinus-Ähnlichkeit__ zweier Vektoren $\mathbf{u},\mathbf{v}\ne\mathbf{0}$ ist die Zahl

<span class="anker" id="gl-5-3"></span>
$$\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}\in[-1,\,1] , \tag{5.3}$$

also der Kosinus ihres Winkels.
:::

Sie ist $1$, wenn die Vektoren in dieselbe Richtung zeigen, $0$, wenn sie orthogonal sind, und $-1$, wenn sie entgegengesetzt zeigen. Multipliziert man einen der Vektoren mit einer positiven Zahl, ändert sie sich nicht, denn die Zahl kürzt sich heraus.

::::beispiel [Rechenbeispiel]
Drei Texte und ihre Zählungen der Wörter „Tor“, „Ball“ und „Wahl“:

$$\mathbf{x}_1=(3,\,2,\,0)^{\top},\qquad \mathbf{x}_2=(6,\,4,\,0)^{\top},\qquad \mathbf{x}_3=(0,\,1,\,3)^{\top} .$$

Text 2 ist ein doppelt so langer Bericht über dasselbe Spiel, Text 3 handelt vor allem von einer Wahl. Die Kosinus-Ähnlichkeit von Text 1 und Text 2 ist $1$, die von Text 1 und Text 3 ist $2/\sqrt{130}\approx0{,}175$ (Abb. [24](#abb-24)). Ebenso ist die von Text 2 und Text 3 gleich $4/(\sqrt{52}\,\sqrt{10})=4/\sqrt{520}\approx0{,}175$.

:::abbildung ml/k1rkosinus 24
Zwei Kosinus-Ähnlichkeiten der Wortzählungen: jeweils ein Skalarprodukt im Zähler und zwei Längen im Nenner.
:::

Die Abstände dagegen sind $\lVert\mathbf{x}_1-\mathbf{x}_2\rVert=\sqrt{13}\approx3{,}61$, $\lVert\mathbf{x}_1-\mathbf{x}_3\rVert=\sqrt{19}\approx4{,}36$ und $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=\sqrt{54}\approx7{,}35$. Nach dem Abstand liegt Text 1 von Text 3 kaum weiter entfernt als von Text 2, obwohl Text 2 genau dasselbe Thema hat. Die Kosinus-Ähnlichkeit erkennt das sofort: Sie ist $1$, und der Winkel zu Text 3 ist mit etwa $79{,}9^\circ$ fast ein rechter.
::::

⁠**Kurz gesagt:** Die Kosinus-Ähnlichkeit vergleicht nur die Richtungen zweier Vektoren und übersieht ihre Längen.

:::hintergrund Kosinus-Ähnlichkeit ist nicht dasselbe wie Korrelation
Zentriert man zwei Vektoren gleicher Länge vorher (Unterabschnitt [4.3](abstande-und-einheiten.html#stufe-4-3)), so misst der Kosinus ihres Winkels, ob die Komponenten gemeinsam über und unter ihrem jeweiligen Mittelwert liegen. Diese Zahl heißt Korrelationskoeffizient. Ohne Zentrieren kommt oft etwas ganz anderes heraus. Beispiel: $\mathbf{a}=(1,2,3)^{\top}$, $\mathbf{b}=(3,4,5)^{\top}$ und $\mathbf{c}=(3,2,1)^{\top}$. Die Kosinus-Ähnlichkeit von $\mathbf{a}$ und $\mathbf{b}$ ist etwa $0{,}983$, die von $\mathbf{a}$ und $\mathbf{c}$ immerhin $0{,}714$, beide also klar positiv. Zentriert ist $\tilde{\mathbf{a}}=(-1,0,1)^{\top}$, $\tilde{\mathbf{b}}=(-1,0,1)^{\top}$ und $\tilde{\mathbf{c}}=(1,0,-1)^{\top}$: Der Korrelationskoeffizient von $\mathbf{a}$ und $\mathbf{b}$ ist $1$, der von $\mathbf{a}$ und $\mathbf{c}$ aber $-1$, denn $\mathbf{c}$ fällt genau dort, wo $\mathbf{a}$ steigt. Die unzentrierte Kosinus-Ähnlichkeit war nur deshalb positiv, weil alle Zahlen positiv sind und alle drei Vektoren deshalb ungefähr in dieselbe Richtung zeigen.
:::

### Das Skalarprodukt als Schattenlänge

<span class="anker" id="stufe-5-5"></span>

Das Skalarprodukt mit einem normierten Vektor hat eine einfache geometrische Bedeutung. Man stelle sich eine Gerade durch den Nullpunkt in Richtung des normierten Vektors $\mathbf{u}$ vor und lasse Licht senkrecht auf diese Gerade fallen. Der Pfeil $\mathbf{x}$ wirft dann einen Schatten auf die Gerade (Abb. [25](#abb-25)). Wie lang ist er?

:::abbildung ml/k1schatten 25
Der Schatten des Pfeils $\mathbf{x}=(3,1)^{\top}$ auf der Geraden in Richtung des normierten Vektors $\mathbf{u}=(0{,}6;\,0{,}8)^{\top}$. Das Licht fällt senkrecht auf die Gerade (gestrichelt). Der Schatten (hellblau) hat die Länge $\mathbf{u}^{\top}\mathbf{x}=\lVert\mathbf{x}\rVert\cos\varphi=2{,}6$ und endet im Punkt $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}=(1{,}56;\,2{,}08)^{\top}$.
:::

:::satz Satz 5.6 (Schattenlänge)
<span class="anker" id="satz-5-6"></span>

Es sei $\mathbf{u}\in\mathbb{R}^d$ normiert, also $\lVert\mathbf{u}\rVert=1$. Dann ist $\mathbf{u}^{\top}\mathbf{x}$ die vorzeichenbehaftete Länge des Schattens von $\mathbf{x}$ auf der Geraden in Richtung $\mathbf{u}$: Der Schatten endet im Punkt $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$, und der Verbindungspfeil $\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ ist orthogonal zu $\mathbf{u}$.
:::

:::beweis Schattenlänge
Mit $\mathbf{u}^{\top}\mathbf{u}=\lVert\mathbf{u}\rVert^2=1$ ist $\mathbf{u}^{\top}\bigl(\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}\bigr)=\mathbf{u}^{\top}\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}^{\top}\mathbf{u}=0$. Der Verbindungspfeil steht also senkrecht auf der Geraden; das ist genau die Richtung, aus der das Licht kommt. Der Schattenpunkt $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ ist $|\mathbf{u}^{\top}\mathbf{x}|$ vom Nullpunkt entfernt, weil $\mathbf{u}$ die Länge $1$ hat. Er liegt in Richtung $\mathbf{u}$, wenn $\mathbf{u}^{\top}\mathbf{x}>0$ ist, und entgegengesetzt, wenn $\mathbf{u}^{\top}\mathbf{x}<0$ ist. Im rechtwinkligen Dreieck aus $\mathbf{x}$, Schatten und Verbindungspfeil ist $\mathbf{x}$ die Hypotenuse; deshalb ist die Schattenlänge auch $\lVert\mathbf{x}\rVert\cos\varphi$.
:::

Ist $\mathbf{u}$ nicht normiert, so ist $\mathbf{u}^{\top}\mathbf{x}$ die Schattenlänge von $\mathbf{x}$ in Richtung $\mathbf{u}$, multipliziert mit $\lVert\mathbf{u}\rVert$.

::::beispiel [Rechenbeispiel]
$\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ ist normiert, denn $0{,}36+0{,}64=1$. Für $\mathbf{x}=(3,\,1)^{\top}$ ist die Schattenlänge $\mathbf{u}^{\top}\mathbf{x}=2{,}6$ (Abb. [26](#abb-26)), der Schattenpunkt $2{,}6\,\mathbf{u}=(1{,}56;\ 2{,}08)^{\top}$ und der Verbindungspfeil $\mathbf{x}-2{,}6\,\mathbf{u}=(1{,}44;\ -1{,}08)^{\top}$. Er ist orthogonal zu $\mathbf{u}$: $0{,}6\cdot1{,}44-0{,}8\cdot1{,}08=0$. Mit $\lVert\mathbf{x}\rVert=\sqrt{10}\approx3{,}162$ ist $\cos\varphi=2{,}6/3{,}162\approx0{,}822$, also $\varphi\approx34{,}7^\circ$.

:::abbildung ml/k1rschatten 26
Die Schattenlänge von $\mathbf{x}$ in Richtung des normierten Vektors $\mathbf{u}$ als Skalarprodukt.
:::
::::

Für eine gewichtete Summe heißt das: Sind die Gewichte normiert, so gibt $\mathbf{w}^{\top}\mathbf{x}$ an, wie weit das Beispiel $\mathbf{x}$ in Richtung von $\mathbf{w}$ reicht. Alle Punkte, die denselben Wert $\mathbf{w}^{\top}\mathbf{x}$ liefern, werfen denselben Schatten. In der Ebene liegen sie deshalb auf einer Geraden senkrecht zu $\mathbf{w}$, im Raum auf einer Ebene senkrecht zu $\mathbf{w}$.

⁠**Kurz gesagt:** Für einen normierten Vektor $\mathbf{u}$ ist $\mathbf{u}^{\top}\mathbf{x}$ die Länge des Schattens, den $\mathbf{x}$ auf die Gerade in Richtung $\mathbf{u}$ wirft.

:::aufgabe Aufgabe 12 ★ Winkel und Orthogonalität
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Berechne den Winkel zwischen $(2,\,1,\,2)^{\top}$ und $(1,\,0,\,1)^{\top}$ und prüfe die Cauchy-Schwarz-Ungleichung.

</li>

<li>

Sind $(1,\,1,\,0)^{\top}$ und $(1,\,-1,\,3)^{\top}$ orthogonal?

</li>

<li>

Finde einen Vektor $\mathbf{v}\ne\mathbf{0}$, der zu $\mathbf{u}=(1,\,2)^{\top}$ orthogonal ist, und prüfe den Satz des Pythagoras für $\mathbf{u}$ und $\mathbf{v}$.

</li>

</ol>

:::loesung
(a) Das Skalarprodukt ist $2+0+2=4$, die Längen sind $3$ und $\sqrt2$. Also ist $\cos\varphi=4/(3\sqrt2)\approx0{,}943$ und $\varphi\approx19{,}5^\circ$. Cauchy-Schwarz: $4\le3\sqrt2\approx4{,}243$.

(b) $1\cdot1+1\cdot(-1)+0\cdot3=0$: ja, sie sind orthogonal.

(c) Für $\mathbf{v}=(v_1,v_2)^{\top}$ verlangt die Bedingung $v_1+2v_2=0$. Eine Lösung ist $\mathbf{v}=(2,\,-1)^{\top}$, jedes von null verschiedene Vielfache davon ebenso. Probe des Pythagoras: $\mathbf{u}+\mathbf{v}=(3,\,1)^{\top}$ hat das Längenquadrat $10$, und $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2=5+5=10$.
:::
:::

:::aufgabe Aufgabe 13 ★★ Welcher Text ist ähnlich?
<span class="anker" id="aufg-13"></span>

Vier Texte, gezählt wurden wieder die Wörter „Tor“, „Ball“ und „Wahl“: $\mathbf{x}_a=(2,\,0,\,1)^{\top}$, $\mathbf{x}_b=(0,\,3,\,0)^{\top}$, $\mathbf{x}_c=(4,\,0,\,2)^{\top}$ und $\mathbf{x}_d=(1,\,1,\,1)^{\top}$.

<ol class="al">

<li>

Berechne die Kosinus-Ähnlichkeit und den euklidischen Abstand von Text $a$ zu den drei anderen Texten.

</li>

<li>

Welcher Text ist Text $a$ am ähnlichsten, nach dem Abstand und nach der Kosinus-Ähnlichkeit? Erkläre den Unterschied.

</li>

</ol>

:::loesung
(a) Mit $\lVert\mathbf{x}_a\rVert=\sqrt5$, $\lVert\mathbf{x}_b\rVert=3$, $\lVert\mathbf{x}_c\rVert=\sqrt{20}$ und $\lVert\mathbf{x}_d\rVert=\sqrt3$:

<ul>

<li>

zu Text $b$: $\mathbf{x}_a^{\top}\mathbf{x}_b=0$, Kosinus-Ähnlichkeit $0$; Abstand $\sqrt{4+9+1}=\sqrt{14}\approx3{,}74$;

</li>

<li>

zu Text $c$: $\mathbf{x}_a^{\top}\mathbf{x}_c=8+0+2=10$, Kosinus-Ähnlichkeit $10/(\sqrt5\sqrt{20})=1$; Abstand $\sqrt{4+0+1}=\sqrt5\approx2{,}24$;

</li>

<li>

zu Text $d$: $\mathbf{x}_a^{\top}\mathbf{x}_d=3$, Kosinus-Ähnlichkeit $3/(\sqrt5\sqrt3)\approx0{,}775$; Abstand $\sqrt{1+1+0}=\sqrt2\approx1{,}41$.

</li>

</ul>

(b) Nach dem Abstand ist Text $d$ am nächsten, nach der Kosinus-Ähnlichkeit Text $c$. Text $c$ ist $\mathbf{x}_c=2\mathbf{x}_a$: dieselbe Wortverteilung, nur doppelt so lang, also inhaltlich dasselbe Thema. Der Abstand bestraft die größere Länge, die Kosinus-Ähnlichkeit sieht nur die Richtung. Text $d$ ist kurz und liegt deshalb nah an jedem kurzen Text, auch ohne gemeinsames Thema. Für den Vergleich von Inhalten ist hier die Kosinus-Ähnlichkeit das passende Maß, und Text $b$ hat mit Text $a$ gar nichts gemeinsam.
:::
:::

:::aufgabe Aufgabe 14 ★★★ Abstand und Winkel normierter Vektoren
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Zeige: Für normierte Vektoren $\mathbf{u},\mathbf{v}$ mit dem Winkel $\varphi$ ist $\lVert\mathbf{u}-\mathbf{v}\rVert^2=2-2\cos\varphi$. Was folgt daraus für die Reihenfolge „ähnlich nach Abstand“ und „ähnlich nach Kosinus-Ähnlichkeit“, wenn man alle Beispiele vorher normiert?

</li>

<li>

Prüfe die Formel an den normierten Texten $\mathbf{x}_1$ und $\mathbf{x}_3$ aus Unterabschnitt [5.4](#stufe-5-4).

</li>

<li>

Zeige: $\lVert\mathbf{u}+\mathbf{v}\rVert=\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ gilt genau dann, wenn $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ ist. Wann ist das der Fall?

</li>

</ol>

:::loesung
(a) Nach [(4.1)](abstande-und-einheiten.html#gl-4-1) ist $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}=1+1-2\cos\varphi$, weil für normierte Vektoren $\mathbf{u}^{\top}\mathbf{v}=\cos\varphi$ ist. Der Abstand ist also eine fallende Funktion der Kosinus-Ähnlichkeit: Je größer der Kosinus, desto kleiner der Abstand. Normiert man alle Beispiele vorher, ordnen Abstand und Kosinus-Ähnlichkeit die Beispiele deshalb genau gleich.

(b) Die normierten Texte sind $\mathbf{x}_1/\sqrt{13}$ und $\mathbf{x}_3/\sqrt{10}$ mit dem Kosinus $0{,}1754$. Die Formel sagt $2-2\cdot0{,}1754\approx1{,}649$. Direkt: $\mathbf{x}_1/\sqrt{13}-\mathbf{x}_3/\sqrt{10}\approx(0{,}832;\ 0{,}238;\ -0{,}949)^{\top}$ mit dem Längenquadrat $0{,}692+0{,}057+0{,}900\approx1{,}649$.

(c) Beide Seiten sind nicht negativ, man darf also die Quadrate vergleichen. Es ist $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ und $(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2=\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2$. Beide sind genau dann gleich, wenn $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. Nach der Cauchy-Schwarz-Ungleichung und ihrem Gleichheitsfall ist das genau dann so, wenn einer der Vektoren ein Vielfaches des anderen ist, und zwar mit einem Faktor $\ge0$, denn sonst wäre das Skalarprodukt negativ. Anschaulich: Die Dreiecksungleichung wird nur dann zur Gleichung, wenn das Dreieck flach ist und beide Pfeile in dieselbe Richtung zeigen.
:::
:::
