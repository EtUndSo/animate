---
title: Integration über Mengen und Berechnung von Volumina
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120500
summary: Die meisten Körper sind keine Quader.
tags: Fortsetzung durch null, wohldefiniert
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die meisten Körper sind keine Quader. Dieser Abschnitt erklärt, was das Integral über eine beliebige abgeschlossene und beschränkte Menge bedeutet, und berechnet Volumina aus den Flächen ihrer Querschnitte.
:::

### Das Integral über eine Menge

<span class="anker" id="stufe-4-1"></span>

Eine Ladung sitzt in einem Bauteil, dessen Form kein Quader ist. Wie integriert man die Ladungsdichte über das Bauteil?

Eine beschränkte Menge passt in einen Quader. Man setzt den Integranden außerhalb der Menge auf null und integriert über den Quader. Dann zählt nur, was in der Menge liegt (Abb. [11](#abb-11)).

:::abbildung hm3/k2fortsetzung 11
Links eine Menge $M$ in einem Quader $Q$ und eine Linie mit festem $y$. Rechts die fortgesetzte Funktion $\bar f$ längs dieser Linie: Innerhalb von $M$ hat sie die Werte von $f$, außerhalb ist sie null. Am Rand von $M$ springt sie.
:::

:::definition Definition 4.1 (Integral über eine Menge)
<span class="anker" id="satz-4-1"></span>

Sei $M\subset\mathbb{R}^n$ abgeschlossen und beschränkt, $f\colon M\to\mathbb{R}$ stetig und $Q\supset M$ ein Quader. Die Funktion

$$\bar f(\boldsymbol{x})=\begin{cases}f(\boldsymbol{x}),&\boldsymbol{x}\in M,\\0,&\boldsymbol{x}\in Q\setminus M,\end{cases}$$

heißt die __Fortsetzung durch null__ von $f$. Die Zahl

<span class="anker" id="gl-4-1"></span>
$$\int_Mf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}:=\int_Q\bar f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} \tag{4.1}$$

heißt das Integral von $f$ über $M$.
:::

⁠**So liest man das:** $Q\setminus M$ ist die Menge der Punkte von $Q$, die nicht in $M$ liegen. Das hat einen Haken: $\bar f$ ist im Allgemeinen nicht stetig, denn am Rand von $M$ springt sie von $f$ auf null. Die Sätze des letzten Abschnitts setzen stetige Integranden voraus und sagen deshalb über die rechte Seite nichts. Hier hilft das Lebesgue-Integral: Es garantiert, dass das Integral für abgeschlossene, beschränkte Mengen $M$ __wohldefiniert__ ist, also einen eindeutigen Wert hat, der nicht vom gewählten Quader abhängt. Man erhält ihn zum Beispiel, indem man $\bar f$ als Grenzwert geeigneter stetiger Funktionen auf $Q$ darstellt.

⁠**Beispiel:** $M=[0,1]\times[0,1]$, $f(x,y)=xy$ und der größere Quader $Q=[0,2]\times[0,1]$. Für festes $y>0$ ist $x\mapsto\bar f(x,y)$ gleich $xy$ für $x\le1$ und null für $x>1$; bei $x=1$ springt sie. Eine Funktion einer Variablen mit endlich vielen Sprüngen integriert man stückweise:

$$\int_0^2\bar f(x,y)\,\mathrm{d} x=\int_0^1xy\,\mathrm{d} x+\int_1^20\,\mathrm{d} x=\frac y2,\qquad\int_0^1\frac y2\,\mathrm{d} y=\frac14 .$$

Das ist dasselbe wie $\int_Mxy\,\mathrm{d} x\,\mathrm{d} y$ direkt über den Quader $M$ gerechnet, wie es sein muss.

:::hintergrund Warum der Sprung am Rand meist nicht stört
Man denkt an die Säulensummen aus dem Hintergrund zum Satz von Fubini. Ein kleines Rechteck, das ganz in $M$ oder ganz außerhalb liegt, merkt vom Sprung nichts. Nur die Rechtecke, die den Rand von $M$ treffen, können Ärger machen, denn dort hängt der Säulenwert davon ab, ob der gewählte Punkt innen oder außen liegt. Ihr Beitrag ist höchstens $\sup|f|$ mal ihre Gesamtfläche. Lässt sich der Rand mit Rechtecken beliebig kleiner Gesamtfläche überdecken, dann geht diese Gesamtfläche bei feiner werdender Einteilung gegen null, und die Säulensummen konvergieren trotz des Sprungs. Das trifft für alle Mengen dieses Kapitels zu. Ihr Rand besteht aus endlich vielen Stücken von Graphen stetiger Funktionen, und ein solcher Graph über $[a,b]$ lässt sich wegen der gleichmäßigen Stetigkeit mit $N$ Rechtecken der Breite $(b-a)/N$ und der Höhe $2\varepsilon$ überdecken, zusammen mit der Fläche $2\varepsilon\,(b-a)$. Es gibt aber abgeschlossene, beschränkte Mengen mit so zerfranstem Rand, dass er sich nicht so überdecken lässt. Für sie konvergieren die Säulensummen schon für $f=1$ nicht, und erst das Lebesgue-Integral gibt dem Integral einen Wert.
:::

⁠**Kurz gesagt:** Über eine Menge integriert man, indem man den Integranden außerhalb auf null setzt und über einen umgebenden Quader integriert.

### Volumen und Flächeninhalt

<span class="anker" id="stufe-4-2"></span>

Integriert man die Funktion $1$ über eine Menge, zählt jeder Punkt der Menge gleich. Das Ergebnis misst die Größe der Menge.

:::definition Definition 4.2 (Volumen und Flächeninhalt)
<span class="anker" id="satz-4-2"></span>

Für eine abgeschlossene, beschränkte Menge $M\subset\mathbb{R}^3$ heißt $\operatorname{vol}(M)=\int_M1\,\mathrm{d}\boldsymbol{x}$ das Volumen von $M$. Für eine abgeschlossene, beschränkte Menge $D\subset\mathbb{R}^2$ heißt $|D|=\int_D1\,\mathrm{d}\boldsymbol{x}$ ihr Flächeninhalt.
:::

Für einen Quader ergibt sich wieder $|Q|$, denn $\int_Q1\,\mathrm{d}\boldsymbol{x}$ ist das Produkt der Intervalllängen.

⁠**Beispiel:** Das Dreieck $D=\{(x,y):0\le y\le x\le1\}$ im Quadrat $[0,1]^2$. Für festes $y$ ist die fortgesetzte Funktion $\bar1$ gleich $1$ für $y\le x\le1$ und sonst null. Das innere Integral ist also die Länge $1-y$, und $|D|=\int_0^1(1-y)\,\mathrm{d} y=\frac12$, wie es für ein halbes Quadrat sein muss.

⁠**Kurz gesagt:** Volumen und Flächeninhalt sind die Integrale der Funktion $1$ über die Menge.

### Das Prinzip von Cavalieri

<span class="anker" id="stufe-4-3"></span>

Die Definition des Volumens taugt selten zum Rechnen. Oft kennt man aber die Querschnitte eines Körpers in jeder Höhe.

Ein Körper ist ein Stapel dünner Schichten. Jede Schicht hat fast das Volumen „Querschnittsfläche mal Dicke“. Verschiebt man die Schichten seitlich gegeneinander, ändert sich keine von ihnen und damit auch nicht das Volumen (Abb. [12](#abb-12)).

:::abbildung hm3/k2cavalieri 12
Links ein Kegel auf der Spitze mit dem Radius $R=2$ und der Höhe $H=3$. Der Schnitt in der Höhe $z$ ist ein Kreis mit dem Radius $2z/3$. Rechts sind dieselben Scheiben seitlich verschoben. In jeder Höhe bleibt die Schnittfläche gleich.
:::

:::satz Satz 4.3 (Prinzip von Cavalieri)
<span class="anker" id="satz-4-3"></span>

Gegeben sei ein Körper

$$M=\{(x,y,z)\in\mathbb{R}^3:\ (x,y)\in D(z),\ 0\le z\le H\}$$

mit Schnittflächen $D(z)\subset\mathbb{R}^2$, deren Flächeninhalt $\mathcal A(z)=|D(z)|$ stetig von $z$ abhängt. Dann gilt

<span class="anker" id="gl-4-2"></span>
$$\operatorname{vol}(M)=\int_0^H\mathcal A(z)\,\mathrm{d} z . \tag{4.2}$$
:::

:::herleitung Riemann-Summe über die Höhe
Man teilt die Höhe in $N$ Schichten der Dicke $\Delta z=H/N$. Die $k$-te Schicht liegt zwischen den Höhen $(k-1)\Delta z$ und $k\,\Delta z$. Ihr Volumen ist ungefähr $\mathcal A(z_k)\,\Delta z$ mit einer Höhe $z_k$ aus diesem Bereich. Aufaddieren ergibt

$$\operatorname{vol}(M)\approx\Delta z\sum_{k=1}^N\mathcal A(z_k).$$

Das ist eine Riemann-Summe von $\mathcal A$ auf $[0,H]$. Weil $\mathcal A$ stetig ist, existiert ihr Grenzwert für $\Delta z\searrow0$, unabhängig von der Wahl der $z_k$, und er ist [(4.2)](#gl-4-2).
:::

⁠**So liest man das:** $H$ ist die Höhe des Körpers, $D(z)$ sein ebener Querschnitt in der Höhe $z$ und $\mathcal A(z)$ dessen Flächeninhalt. Es zählt nur diese Fläche, nicht wo der Querschnitt liegt und welche Form er hat. Zwei Körper, die in jeder Höhe gleich große Schnittflächen haben, haben dasselbe Volumen.

:::hintergrund Warum die Herleitung genau stimmt
Das Zeichen $\approx$ in der Herleitung verbirgt die Frage, ob „Fläche mal Dicke“ für eine Schicht genau genug ist. Die genaue Begründung kommt aus dem Mehrfachintegral. Nach Unterabschnitt [4.2](#stufe-4-2) ist $\operatorname{vol}(M)=\int_Q\bar1\,\mathrm{d}\boldsymbol{x}$. Rechnet man dieses Integral iteriert, mit $z$ als äußerer Variable, dann ist das innere Doppelintegral über $x$ und $y$ in der Höhe $z$ genau $\int\!\!\int\bar1\,\mathrm{d} x\,\mathrm{d} y=|D(z)|=\mathcal A(z)$, und außen bleibt $\int_0^H\mathcal A(z)\,\mathrm{d} z$. Das Prinzip von Cavalieri ist also ein iteriertes Integral mit $z$ außen. Weil $\bar1$ am Rand von $M$ springt, braucht man dafür eine Fassung des Satzes von Fubini für unstetige Integranden; die liefert das Lebesgue-Integral.
:::

⁠**Beispiel: Kegel.** Ein Kegel mit einem Grundkreis vom Radius $R$ und der Höhe $H$ wird auf die Spitze gestellt. Der Radius des Querschnitts wächst linear von $0$ an der Spitze bis $R$ oben, ist also $zR/H$, und $\mathcal A(z)=\pi(zR/H)^2$. Damit ist

$$\operatorname{vol}=\int_0^H\pi\frac{R^2}{H^2}z^2\,\mathrm{d} z=\pi\frac{R^2}{H^2}\cdot\frac{H^3}3=\frac\pi3R^2H .$$

Bei $R=2$ und $H=3$ ist das $4\pi$. **Grenzfall:** Bei konstantem $\mathcal A$, etwa für einen Zylinder, bleibt Grundfläche mal Höhe.

⁠**Beispiel: Kuppel.** Die *Kuppel* $K$ ist der Körper zwischen der Ebene $z=0$ und dem Graphen der Kuppelfunktion: $K=\{(x,y,z):0\le z\le4-x^2-y^2\}$. In der Höhe $z$ ist der Querschnitt die Kreisscheibe $x^2+y^2\le4-z$ mit $\mathcal A(z)=\pi(4-z)$. Also ist

<span class="anker" id="gl-4-3"></span>
$$\operatorname{vol}(K)=\int_0^4\pi(4-z)\,\mathrm{d} z=8\pi . \tag{4.3}$$

:::hintergrund Ein Bild: der schief geschobene Münzstapel
Einen Stapel Münzen kann man schief schieben, ohne dass sich sein Volumen ändert, denn jede Münze bleibt dieselbe. Das ist das Prinzip von Cavalieri im Kleinen. Das Bild ist eine Analogie und hat eine Grenze: Eine echte Münze hat über ihre ganze Dicke denselben Querschnitt, eine Schicht eines Kegels nicht. Für dicke Schichten stimmt „Fläche mal Dicke“ deshalb nur ungefähr. Erst der Grenzwert $\Delta z\searrow0$ macht daraus eine genaue Aussage.
:::

⁠**Kurz gesagt:** Das Volumen eines Körpers ist das Integral seiner Querschnittsflächen über die Höhe.

### Aufgaben

<span class="anker" id="stufe-4-4"></span>

:::aufgabe Aufgabe 12 ★★ Scheiben zählen
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Ein Kugeltank mit dem Radius $2$ ist bis zur Höhe $H$ über seinem tiefsten Punkt gefüllt, $0\le H\le4$. Berechne das Volumen $V(H)$ der Füllung. Prüfe $V(4)$ und $V(2)$.

</li>

<li>

Berechne das Volumen des Körpers $\{|x|+|y|+|z|\le1\}$. Tipp: Die Querschnitte sind Quadrate.

</li>

</ol>

:::loesung
(a) Der tiefste Punkt liegt bei $z=0$, der Mittelpunkt bei $z=2$. In der Höhe $z$ ist der Querschnitt eine Kreisscheibe, deren Radius im Quadrat $4-(z-2)^2=4z-z^2$ ist. Also ist

$$V(H)=\int_0^H\pi(4z-z^2)\,\mathrm{d} z=\pi\Bigl(2H^2-\frac{H^3}3\Bigr).$$

$V(4)=\frac{32\pi}3=\frac43\pi\cdot2^3$ ist die volle Kugel, $V(2)=\frac{16\pi}3$ die Hälfte.

(b) In der Höhe $z$ mit $|z|\le1$ ist der Querschnitt $|x|+|y|\le1-|z|$, ein Quadrat mit Diagonalen der Länge $2(1-|z|)$, also mit der Fläche $\mathcal A(z)=\frac12\bigl(2(1-|z|)\bigr)^2=2(1-|z|)^2$. Damit ist $\operatorname{vol}=\int_{-1}^12(1-|z|)^2\,\mathrm{d} z=2\cdot2\int_0^1(1-z)^2\,\mathrm{d} z=\frac43$.
:::
:::

:::aufgabe Aufgabe 13 ★★ Schüssel und Kuppel
<span class="anker" id="aufg-13"></span>

Die Schüssel $W$ ist der Körper im Zylinder $x^2+y^2\le4$ zwischen der Ebene $z=0$ und dem Graphen $z=x^2+y^2$, also $W=\{(x,y,z):x^2+y^2\le4,\ 0\le z\le x^2+y^2\}$.

<ol class="al">

<li>

Beschreibe den Querschnitt von $W$ in der Höhe $z$, $0\le z\le4$, und berechne seinen Flächeninhalt.

</li>

<li>

Begründe ohne weitere Rechnung, dass $W$ dasselbe Volumen hat wie die Kuppel $K$, und gib es an.

</li>

<li>

Der Zylinder $x^2+y^2\le4$, $0\le z\le4$, hat das Volumen $16\pi$. Welches Volumen hat der Teil des Zylinders, der über der Schüssel liegt?

</li>

</ol>

:::loesung
(a) In der Höhe $z$ gehören die Punkte mit $x^2+y^2\le4$ und $x^2+y^2\ge z$ dazu, also der Kreisring zwischen den Radien $\sqrt z$ und $2$. Seine Fläche ist $\mathcal A_W(z)=\pi\cdot4-\pi z=\pi(4-z)$.

(b) Die Kuppel hat in derselben Höhe die Kreisscheibe $x^2+y^2\le4-z$ mit derselben Fläche $\pi(4-z)$. Nach dem Prinzip von Cavalieri haben beide Körper dasselbe Volumen, nach [(4.3)](#gl-4-3) also $\operatorname{vol}(W)=8\pi$. Die Querschnitte haben verschiedene Form, Ring und Scheibe, aber es zählt nur die Fläche.

(c) Über der Schüssel liegen die Punkte mit $x^2+y^2<z\le4$; in der Höhe $z$ ist das eine Kreisscheibe mit der Fläche $\pi z$, also ist das Volumen $\int_0^4\pi z\,\mathrm{d} z=8\pi$. Zur Kontrolle: $16\pi-8\pi=8\pi$.
:::
:::
