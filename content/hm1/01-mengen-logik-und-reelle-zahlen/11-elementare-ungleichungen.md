---
title: Stufe 9: Elementare Ungleichungen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1211100
summary: Oft lässt sich ein Ausdruck nicht ausrechnen, nur abschätzen.
tags: Bernoulli, Young, Mittelwerte, geometrische Mittel, arithmetische Mittel, Cauchy-Schwarz, Minkowski, Vektor
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Oft lässt sich ein Ausdruck nicht ausrechnen, nur abschätzen. Diese Stufe liefert die fünf Standardabschätzungen.
:::

**Die Idee.** Fast alles folgt aus einer Tatsache: Ein Quadrat ist nicht negativ. Schreibt man $(a-b)^2\ge0$ aus, entsteht $2ab\le a^2+b^2$. Young, die Mittelwerte und Cauchy-Schwarz sind diese Zeile, geschickt umgeschrieben. Nur Bernoulli braucht die Induktion.

:::satz Satz 9.1 (Fünf Ungleichungen)
<span class="anker" id="satz-9-1"></span>

In $\mathbb{R}$ gilt:

<ol class="rm">

<li>

__Bernoulli__: Für $x>-1$, $x\ne0$ und $n\ge2$ gilt $(1+x)^n>1+nx$.

</li>

<li>

__Young__: Für $\varepsilon>0$ und $x,y\in\mathbb{R}$ gilt $|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$.

</li>

<li>

__Mittelwerte__: Für $x,y\ge0$ gilt $\sqrt{xy}\le\frac{x+y}2$. Links steht das __geometrische Mittel__, rechts das __arithmetische Mittel__.

</li>

<li>

__Cauchy-Schwarz__: Für $x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}$ gilt mit $\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i^2}\ge0$

<span class="anker" id="gl-9-1"></span>
$$\sum_{i=1}^n|x_iy_i|\le\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|. \tag{9.1}$$

</li>

<li>

__Minkowski__: Mit $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$ gilt

<span class="anker" id="gl-9-2"></span>
$$\sqrt{\sum_{i=1}^n(x_i+y_i)^2}\le\sqrt{\sum_{i=1}^nx_i^2}+\sqrt{\sum_{i=1}^ny_i^2},\quad\text{das heißt}\quad\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|. \tag{9.2}$$

</li>

</ol>
:::

⁠**So liest man das:** $\vec x=(x_1,\dots,x_n)$ ist ein __Vektor__, eine Liste von $n$ Zahlen, und $\|\vec x\|$ seine __Norm__. Für $n=2$ ist das nach Pythagoras die Länge des Pfeils vom Ursprung zum Punkt $(x_1,x_2)$. Dann ist [(9.2)](#gl-9-2) die Dreiecksungleichung für Pfeile, und in [Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) wird aus [(9.1)](#gl-9-1) das Skalarprodukt. Bei Young ist $\varepsilon$ ein Tauschkurs: Ein kleiner $x$-Term kostet einen großen $y$-Term. **Warum die Voraussetzungen:** Bernoulli: $x=-4$, $n=3$ gibt $-27>-11$, falsch, also braucht man $x>-1$. Für $x=0$ oder $n=1$ steht Gleichheit. Mittelwerte: $x=y=-1$ gibt $1\le-1$, falsch. Young: $\varepsilon=-1$ macht die rechte Seite negativ.

:::abbildung hm1/k1mittel 9
Links die Mittelwerte als Halbkreis: Der Radius ist das arithmetische Mittel, die Höhe über dem Teilpunkt das geometrische. Die Höhe ist nie größer als der Radius. Rechts Bernoulli für $n=3$: Die Gerade berührt die Kurve bei $x=0$ und liegt für $x>-1$ darunter.
:::

:::beweis Die fünf Ungleichungen
⁠*Bernoulli*, Induktion ab $n_0=2$. Anfang: $(1+x)^2=1+2x+x^2>1+2x$, denn $x^2>0$ nach Satz [4.2](anordnungsaxiome.html#satz-4-2) (d). Schritt: Wegen $1+x>0$ darf man die Voraussetzung nach (O4) mit $1+x$ multiplizieren: $(1+x)^{n+1}>(1+nx)(1+x)=1+(n+1)x+nx^2>1+(n+1)x$.

⁠*Young.* $\sqrt\varepsilon$ existiert nach Satz [7.2](intervallschachtelung-und-wurzeln.html#satz-7-2), und $\sqrt\varepsilon>0$. Quadrate sind nicht negativ:

$$0\le\Bigl(\sqrt\varepsilon\,x\pm\frac1{\sqrt\varepsilon}\,y\Bigr)^2=\varepsilon x^2\pm2xy+\frac1\varepsilon y^2.$$

Das gibt $\mp2xy\le\varepsilon x^2+\frac1\varepsilon y^2$. Weil $|xy|=\max\{xy,-xy\}$ ist, folgt die Behauptung nach Division durch 2.

⁠*Mittelwerte.* Young mit $\varepsilon=1$ für $\sqrt x$ und $\sqrt y$: $\sqrt x\sqrt y\le\frac12x+\frac12y$, und $\sqrt x\sqrt y=\sqrt{xy}$.

⁠*Cauchy-Schwarz.* Sind alle $x_i=0$ oder alle $y_i=0$, steht $0\le0$. Sonst ist $\|\vec x\|>0$ und $\|\vec y\|>0$, und man setzt $\xi_i:=x_i/\|\vec x\|$, $\eta_i:=y_i/\|\vec y\|$. Teilt man [(9.1)](#gl-9-1) durch $\|\vec x\|\|\vec y\|$, ist $\sum_{i=1}^n|\xi_i\eta_i|\le1$ zu zeigen. Es gilt $\sum_i\xi_i^2=\frac1{\|\vec x\|^2}\sum_ix_i^2=1$, ebenso $\sum_i\eta_i^2=1$. Nach den Mittelwerten für $\xi_i^2$, $\eta_i^2$ ist

$$\sum_{i=1}^n|\xi_i\eta_i|=\sum_{i=1}^n\sqrt{\xi_i^2\eta_i^2}\le\sum_{i=1}^n\frac{\xi_i^2+\eta_i^2}2=\frac12+\frac12=1.$$

⁠*Minkowski.* Sei $s_i:=x_i+y_i$, also $\vec s=\vec x+\vec y$. Mit (AM), dann $a\le|a|$, dann [(9.1)](#gl-9-1) für die Listen $x_i,s_i$ und $y_i,s_i$:

$$\|\vec s\|^2=\sum_ix_is_i+\sum_iy_is_i\le\sum_i|x_is_i|+\sum_i|y_is_i|\le\bigl(\|\vec x\|+\|\vec y\|\bigr)\|\vec s\|.$$

Für $\|\vec s\|=0$ steht in [(9.2)](#gl-9-2) links 0. Sonst teilt man durch $\|\vec s\|$.
:::

::::beispiel
Bernoulli: $1{,}01^{10}>1{,}1$, exakt $1{,}1046$. Für kleines $x$ ist $1+nx$ eine gute Näherung: 1 % mehr Spannung bedeutet an einem Widerstand rund 2 % mehr Leistung, exakt 2,01 %. Für großes $x$ ist sie grob: $2^{10}=1024$ gegen 11. Young mit $x=2$, $y=8$: Für $\varepsilon=1$ steht $16\le34$, für $\varepsilon=4$ steht $16\le16$. Cauchy-Schwarz mit $\vec x=(3,4)$, $\vec y=(1,2)$: $3+8=11\le5\sqrt5\approx11{,}18$. Minkowski: $\|(4,6)\|=\sqrt{52}\approx7{,}21\le5+\sqrt5\approx7{,}24$.
::::

⁠**Grenzfall:** Bei $x=y$ sind beide Mittel gleich, im Halbkreis steht die Höhe auf der Mitte.

:::frage Wann nehme ich welche Ungleichung?
Potenz einer Zahl nahe 1: Bernoulli. Produkt abschätzen: Young, Mittelwerte. Summe von Produkten: Cauchy-Schwarz. Wurzel aus einer Summe: Minkowski.
:::

:::aufgabe Aufgabe 10 ★★★ Abschätzen
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Zeige $2^{n-1}\ge n$ für alle $n\in\mathbb{N}$. (Diese Ungleichung braucht Stufe [7](intervallschachtelung-und-wurzeln.html#stufe-7).)

</li>

<li>

Schätze $0{,}995^{20}$ nach unten ab und vergleiche mit dem exakten Wert.

</li>

<li>

Ein Rechteck hat die Fläche 16. Zeige mit den Mittelwerten, dass der Umfang mindestens 16 ist. Für welche Seiten gilt Gleichheit?

</li>

<li>

Prüfe Cauchy-Schwarz und Minkowski für $\vec x=(1,2,2)$, $\vec y=(2,-1,2)$.

</li>

<li>

Zeige: Für $\vec y=t\,\vec x$ mit $t\in\mathbb{R}$ gilt in [(9.1)](#gl-9-1) Gleichheit.

</li>

</ol>

:::loesung
(a) Für $n=1,2$ steht $1\ge1$ und $2\ge2$. Für $n\ge3$ ist $2^{n-1}=(1+1)^{n-1}>1+(n-1)=n$ nach Bernoulli. (b) $x=-0{,}005$, $n=20$: $0{,}995^{20}>1-0{,}1=0{,}9$. Exakt $0{,}9046$, die Schranke liegt 0,5 % darunter. (c) Seiten $a,b>0$, $ab=16$: Umfang $2(a+b)\ge2\cdot2\sqrt{ab}=16$. Gleichheit für $a=b=4$, dem Quadrat. (d) $\|\vec x\|=\sqrt{1+4+4}=3$, $\|\vec y\|=\sqrt{4+1+4}=3$. Cauchy-Schwarz: $2+2+4=8\le9$. Minkowski: $\vec x+\vec y=(3,1,4)$, $\|\vec x+\vec y\|=\sqrt{26}\approx5{,}10\le6$. (e) $\sum_i|x_i\cdot tx_i|=|t|\sum_ix_i^2=|t|\,\|\vec x\|^2$. Rechts: $\|t\vec x\|=\sqrt{t^2\sum_ix_i^2}=|t|\,\|\vec x\|$, also $\|\vec x\|\,\|\vec y\|=|t|\,\|\vec x\|^2$.
:::
:::

::::formelsammlung
**Quadrate sind nicht negativ**

$$(a-b)^2\ge0\quad\Longrightarrow\quad2ab\le a^2+b^2$$

Young, die Mittelwerte und Cauchy-Schwarz sind diese Zeile, geschickt umgeschrieben; nur Bernoulli braucht die Induktion.

**Bernoulli**

$$(1+x)^n>1+nx$$

Für $x>-1$, $x\ne0$ und $n\ge2$; für $x=0$ oder $n=1$ steht Gleichheit. Für kleines $x$ ist $1+nx$ eine gute Näherung, für großes grob.

**Young**

$$|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$$

Für $\varepsilon>0$ und $x,y\in\mathbb{R}$. $\varepsilon$ ist ein Tauschkurs: Ein kleiner $x$-Term kostet einen großen $y$-Term.

**Mittelwerte**

$$\sqrt{xy}\le\frac{x+y}2$$

Für $x,y\ge0$: links das geometrische, rechts das arithmetische Mittel; bei $x=y$ sind beide gleich.

**Norm eines Vektors**

$$\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i^2}\ge0$$

Für den Vektor $\vec x=(x_1,\dots,x_n)$, eine Liste von $n$ Zahlen. Für $n=2$ ist das nach Pythagoras die Länge des Pfeils vom Ursprung zum Punkt $(x_1,x_2)$.

**Cauchy-Schwarz**

$$\sum_{i=1}^n|x_iy_i|\le\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|$$

Für $x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}$. Für $\vec y=t\,\vec x$ mit $t\in\mathbb{R}$ steht Gleichheit.

**Minkowski**

$$\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|,\qquad\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$$

Ausgeschrieben $\sqrt{\sum_{i=1}^n(x_i+y_i)^2}\le\sqrt{\sum_{i=1}^nx_i^2}+\sqrt{\sum_{i=1}^ny_i^2}$: die Dreiecksungleichung für Pfeile.
::::

::::lernkarten
:::karte zusammenhang Quadrate sind nicht negativ
Aus welcher einen Tatsache folgen die Ungleichungen von Young, der Mittelwerte und von Cauchy-Schwarz?
---
Daraus, dass ein Quadrat nicht negativ ist: $(a-b)^2\ge0$ ausgeschrieben gibt $2ab\le a^2+b^2$, und die drei Ungleichungen sind diese Zeile, geschickt umgeschrieben.
--- falsch
Aus der Dreiecksungleichung $|x+y|\le|x|+|y|$: Alle drei schätzen eine Summe nach oben ab und sind deshalb Sonderfälle von ihr, angewandt auf Produkte statt auf Summen.
--- falsch
Aus der vollständigen Induktion: Man beweist sie zuerst für zwei Zahlen und schließt dann von $n$ auf $n+1$; nur Bernoulli kommt ohne Induktion aus.
--- falsch
Aus der Regel $x<y\wedge z<0\Rightarrow xz>yz$: Alle drei entstehen, indem man eine bekannte Ungleichung mit einer negativen Zahl multipliziert und dadurch umdreht.
:::
:::karte formel Bernoulli
Wie lautet die Ungleichung von Bernoulli, und unter welchen Voraussetzungen gilt sie?
---
Für $x>-1$, $x\ne0$ und $n\ge2$ gilt $(1+x)^n>1+nx$. Für $x=0$ oder $n=1$ steht Gleichheit; ohne $x>-1$ scheitert sie, für $x=-4$, $n=3$ stünde dort $-27>-11$.
--- falsch
Für alle $x\in\mathbb{R}$ und $n\ge2$ gilt $(1+x)^n>1+nx$, weil eine Potenz schneller wächst als ein Vielfaches; Voraussetzungen an $x$ braucht man dafür nicht.
--- falsch
Für $x>-1$, $x\ne0$ und $n\ge2$ gilt $(1+x)^n<1+nx$: Die Gerade $1+nx$ liegt über der Kurve und schätzt die Potenz deshalb nach oben ab.
--- falsch
Für $x>0$ und $n\ge2$ gilt $(1+x)^n=1+nx$ exakt; für negative $x$ ist diese Gleichung nur eine Näherung, die mit wachsendem $n$ schlechter wird.
:::
:::karte formel Young
Wie lautet die Ungleichung von Young für $\varepsilon>0$, und welche Rolle spielt $\varepsilon$ darin?
---
$|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$ für $\varepsilon>0$ und $x,y\in\mathbb{R}$. $\varepsilon$ ist ein Tauschkurs: Ein kleiner $x$-Term kostet einen großen $y$-Term.
--- falsch
$|xy|\le\frac\varepsilon2x^2+\frac\varepsilon2y^2$ für $\varepsilon>0$ und $x,y\in\mathbb{R}$. $\varepsilon$ ist ein Fehlerterm, der beide Seiten der Ungleichung gleichmäßig vergrößert.
--- falsch
$|xy|\ge\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$ für $\varepsilon>0$ und $x,y\in\mathbb{R}$. $\varepsilon$ ist ein Tauschkurs: Ein kleiner $x$-Term kostet einen großen $y$-Term.
--- falsch
$|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$ für jedes $\varepsilon\ne0$, auch für negatives. $\varepsilon$ ist ein Tauschkurs zwischen dem $x$-Term und dem $y$-Term.
:::
:::karte begriff geometrisches Mittel und arithmetisches Mittel
Was sind das geometrische und das arithmetische Mittel zweier Zahlen $x,y\ge0$, und wie liegen sie zueinander?
---
Das geometrische Mittel ist $\sqrt{xy}$, das arithmetische $\frac{x+y}2$. Es gilt $\sqrt{xy}\le\frac{x+y}2$; bei $x=y$ sind beide gleich.
--- falsch
Das geometrische Mittel ist $\frac{x+y}2$, das arithmetische $\sqrt{xy}$. Es gilt $\frac{x+y}2\le\sqrt{xy}$; bei $x=y$ sind beide gleich.
--- falsch
Das geometrische Mittel ist $\sqrt{xy}$, das arithmetische $\frac{x+y}2$. Es gilt $\sqrt{xy}\ge\frac{x+y}2$, weil die Wurzel große Werte stärker betont.
--- falsch
Das geometrische Mittel ist $\sqrt{x^2+y^2}$, das arithmetische $\frac{x+y}2$. Beide sind stets gleich, wenn $x$ und $y$ nicht negativ sind.
:::
:::karte formel Mittelwerte
Was besagt die Ungleichung der Mittelwerte, und wie sieht man sie an einem Halbkreis?
---
Für $x,y\ge0$ gilt $\sqrt{xy}\le\frac{x+y}2$. Im Halbkreis mit dem Radius $\frac{x+y}2$ ist die Höhe über dem Teilpunkt das geometrische Mittel, und die Höhe ist nie größer als der Radius.
--- falsch
Für alle $x,y\in\mathbb{R}$ gilt $\sqrt{xy}\le\frac{x+y}2$. Im Halbkreis ist der Radius das geometrische Mittel und die Höhe über dem Teilpunkt das arithmetische; der Radius ist nie größer als die Höhe.
--- falsch
Für $x,y\ge0$ gilt $\frac{x+y}2\le\sqrt{xy}$. Im Halbkreis mit dem Radius $\sqrt{xy}$ ist die Höhe über dem Teilpunkt das arithmetische Mittel, und sie ist nie kleiner als der Radius.
--- falsch
Für $x,y\ge0$ gilt $\sqrt{xy}=\frac{x+y}2$. Im Halbkreis mit dem Radius $\frac{x+y}2$ sind der Radius und die Höhe über jedem Teilpunkt gleich lang.
:::
:::karte begriff Vektor und Norm
Was ist ein Vektor $\vec x=(x_1,\dots,x_n)$, und wie ist seine Norm $\|\vec x\|$ definiert?
---
Ein Vektor ist eine Liste von $n$ Zahlen. Seine Norm ist $\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i^2}\ge0$; für $n=2$ ist sie nach Pythagoras die Länge des Pfeils vom Ursprung zum Punkt $(x_1,x_2)$.
--- falsch
Ein Vektor ist eine Liste von $n$ Zahlen. Seine Norm ist $\|\vec x\|:=\sum_{i=1}^n|x_i|$; für $n=2$ ist sie nach Pythagoras die Länge des Pfeils vom Ursprung zum Punkt $(x_1,x_2)$.
--- falsch
Ein Vektor ist eine einzelne Zahl mit einer Richtung. Seine Norm ist der Betrag dieser Zahl; für $n=2$ ist sie die Fläche des Quadrats über dem Pfeil vom Ursprung zum Punkt $(x_1,x_2)$.
--- falsch
Ein Vektor ist eine Liste von $n$ Zahlen. Seine Norm ist $\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i}$, die Wurzel aus der Summe der Einträge, die es bei negativer Summe nicht gibt.
:::
:::karte formel Cauchy-Schwarz
Wie lautet die Ungleichung von Cauchy-Schwarz für $x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}$?
---
$\sum_{i=1}^n|x_iy_i|\le\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|$. Sie schätzt eine Summe von Produkten durch das Produkt der Normen ab.
--- falsch
$\sum_{i=1}^n|x_iy_i|\ge\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|$. Sie schätzt eine Summe von Produkten durch das Produkt der Normen nach unten ab.
--- falsch
$\sum_{i=1}^n|x_iy_i|\le\|\vec x\|+\|\vec y\|$. Sie schätzt eine Summe von Produkten durch die Summe der beiden Normen ab, wie die Dreiecksungleichung.
--- falsch
$\sum_{i=1}^n|x_iy_i|\le\|\vec x\|\cdot\|\vec y\|$ gilt nur für $n=2$, weil die Ungleichung auf dem Satz des Pythagoras in der Ebene beruht und für längere Listen nicht gilt.
:::
:::karte formel Minkowski
Wie lautet die Ungleichung von Minkowski, und was bedeutet sie für Pfeile in der Ebene?
---
$\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|$ mit $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$. Für $n=2$ ist sie die Dreiecksungleichung für Pfeile: Der Summenpfeil ist nie länger als beide zusammen.
--- falsch
$\|\vec x+\vec y\|=\|\vec x\|+\|\vec y\|$ mit $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$. Für $n=2$ heißt das: Die Länge des Summenpfeils ist stets genau die Summe der beiden Längen.
--- falsch
$\|\vec x+\vec y\|\ge\|\vec x\|+\|\vec y\|$ mit $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$. Für $n=2$ heißt das: Der Summenpfeil ist nie kürzer als die beiden Pfeile zusammengenommen.
--- falsch
$\|\vec x+\vec y\|\le\|\vec x\|\cdot\|\vec y\|$ mit $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$. Für $n=2$ ist sie der Satz des Pythagoras für zwei aneinandergesetzte Pfeile in der Ebene.
:::
:::karte herleitung Bernoulli durch Induktion
Wie beweist man die Ungleichung von Bernoulli $(1+x)^n>1+nx$ für $x>-1$, $x\ne0$ durch Induktion ab $n_0=2$?
---
Anfang: $(1+x)^2=1+2x+x^2>1+2x$, weil $x^2>0$ für $x\ne0$ gilt.
---
Schritt: Man setzt $(1+x)^n>1+nx$ voraus und multipliziert mit $1+x$; das ist erlaubt, weil $1+x>0$ ist und die Ungleichung dann nach (O4) erhalten bleibt.
---
Das gibt $(1+x)^{n+1}>(1+nx)(1+x)=1+(n+1)x+nx^2$, weil man das Produkt nach dem Distributivgesetz ausmultipliziert.
---
Das ist größer als $1+(n+1)x$, weil der weggelassene Summand $nx^2$ positiv ist; damit gilt die Aussage für $n+1$.
:::
:::karte herleitung Young aus einem Quadrat
Wie folgt die Ungleichung von Young $|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$ daraus, dass Quadrate nicht negativ sind?
---
Für $\varepsilon>0$ existiert $\sqrt\varepsilon>0$, weil jede nicht negative Zahl eine Wurzel hat.
---
Es gilt $0\le\Bigl(\sqrt\varepsilon\,x\pm\frac1{\sqrt\varepsilon}\,y\Bigr)^2=\varepsilon x^2\pm2xy+\frac1\varepsilon y^2$, weil ein Quadrat nicht negativ ist und man nach dem Distributivgesetz ausmultipliziert.
---
Umstellen gibt $\mp2xy\le\varepsilon x^2+\frac1\varepsilon y^2$, weil man den mittleren Summanden auf die andere Seite bringen darf.
---
Die Abschätzung gilt auch für $2|xy|$, weil $|xy|=\max\{xy,-xy\}$ ist; nach Division durch 2 folgt die Behauptung.
:::
:::karte herleitung Cauchy-Schwarz aus den Mittelwerten
Wie beweist man die Ungleichung von Cauchy-Schwarz mit der Ungleichung der Mittelwerte?
---
Sind alle $x_i=0$ oder alle $y_i=0$, steht $0\le0$; sonst ist $\|\vec x\|>0$ und $\|\vec y\|>0$, weil dann mindestens ein Quadrat in der Summe positiv ist.
---
Man setzt $\xi_i:=x_i/\|\vec x\|$ und $\eta_i:=y_i/\|\vec y\|$, weil nach Division durch $\|\vec x\|\|\vec y\|$ nur noch $\sum_{i=1}^n|\xi_i\eta_i|\le1$ zu zeigen ist.
---
Es gilt $\sum_i\xi_i^2=1$ und $\sum_i\eta_i^2=1$, weil $\sum_i\xi_i^2=\frac1{\|\vec x\|^2}\sum_ix_i^2$ ist und ebenso für die $\eta_i$.
---
Es folgt $\sum_{i=1}^n|\xi_i\eta_i|=\sum_{i=1}^n\sqrt{\xi_i^2\eta_i^2}\le\sum_{i=1}^n\frac{\xi_i^2+\eta_i^2}2=\frac12+\frac12=1$, weil das geometrische Mittel von $\xi_i^2$ und $\eta_i^2$ nie größer als ihr arithmetisches ist.
:::
:::karte zusammenhang Wahl der Ungleichung
Welche der fünf elementaren Ungleichungen nimmt man für welche Art von Ausdruck?
---
Potenz einer Zahl nahe 1: Bernoulli. Produkt abschätzen: Young oder die Mittelwerte. Summe von Produkten: Cauchy-Schwarz. Wurzel aus einer Summe: Minkowski.
--- falsch
Potenz einer Zahl nahe 1: Cauchy-Schwarz. Produkt abschätzen: Minkowski. Summe von Produkten: Bernoulli. Wurzel aus einer Summe: Young oder die Mittelwerte.
--- falsch
Potenz einer Zahl nahe 1: Bernoulli. Produkt abschätzen: Minkowski. Summe von Produkten: Young oder die Mittelwerte. Wurzel aus einer Summe: Cauchy-Schwarz.
--- falsch
Potenz einer Zahl nahe 1: Young. Produkt abschätzen: Bernoulli. Summe von Produkten: Cauchy-Schwarz. Wurzel aus einer Summe: die Mittelwerte oder Minkowski.
:::
:::karte zusammenhang Voraussetzungen der Ungleichungen
Warum braucht die Ungleichung von Bernoulli die Voraussetzung $x>-1$ und die der Mittelwerte die Voraussetzung $x,y\ge0$?
---
Weil die Ungleichungen sonst falsch werden: Bei Bernoulli gibt $x=-4$, $n=3$ die falsche Aussage $-27>-11$, bei den Mittelwerten gibt $x=y=-1$ die falsche Aussage $1\le-1$.
--- falsch
Weil die Ausdrücke sonst nicht erklärt sind: Für $x\le-1$ ist $(1+x)^n$ nicht definiert, und für negative $x$ und $y$ gibt es kein arithmetisches Mittel $\frac{x+y}2$.
--- falsch
Nur zur Vereinfachung der Beweise: Die Ungleichungen gelten auch für alle anderen Werte, man müsste dafür nur mehr Fälle unterscheiden und länger rechnen.
--- falsch
Weil sonst Gleichheit eintritt: Für $x\le-1$ ist $(1+x)^n=1+nx$ für alle $n$, und für negative $x$ und $y$ sind das geometrische und das arithmetische Mittel gleich.
:::
:::karte zusammenhang Bernoulli als Näherung
Wie gut nähert $1+nx$ die Potenz $(1+x)^n$ für kleine und für große $x$ an?
---
Für kleines $x$ gut: $1{,}01^{10}>1{,}1$, exakt $1{,}1046$; 1 % mehr Spannung gibt an einem Widerstand rund 2 % mehr Leistung, exakt 2,01 %. Für großes $x$ grob: $2^{10}=1024$ gegen 11.
--- falsch
Für kleines $x$ schlecht und für großes $x$ gut, weil sich bei großen Zahlen die Abweichungen der einzelnen Faktoren gegenseitig ausgleichen: $2^{10}$ liegt dicht bei 11.
--- falsch
Für alle $x$ gleich gut, weil die Abweichung immer genau $nx^2$ beträgt; bei $x=1$ und $n=10$ liegt die Potenz also genau um 10 über der Näherung $1+nx$.
--- falsch
Für kleines $x$ gut, weil $(1+x)^n$ dann sogar kleiner als $1+nx$ ist, $1{,}01^{10}$ etwa $1{,}0946$. Für großes $x$ wächst der Abstand, bleibt aber stets unter 1.
:::
:::karte zusammenhang Gleichheit bei Cauchy-Schwarz
Warum gilt in der Ungleichung von Cauchy-Schwarz Gleichheit, wenn $\vec y=t\,\vec x$ mit $t\in\mathbb{R}$ ist?
---
Weil dann beide Seiten $|t|\,\|\vec x\|^2$ ergeben: Links ist $\sum_i|x_i\cdot tx_i|=|t|\sum_ix_i^2$, rechts ist $\|t\vec x\|=|t|\,\|\vec x\|$, also $\|\vec x\|\,\|\vec y\|=|t|\,\|\vec x\|^2$.
--- falsch
Weil dann alle Produkte $x_iy_i$ null sind: Ein Vielfaches von $\vec x$ steht senkrecht auf $\vec x$, und deshalb sind beide Seiten der Ungleichung null.
--- falsch
Gleichheit gilt dort gar nicht: Für $\vec y=t\,\vec x$ ist die linke Seite $|t|\,\|\vec x\|$ und die rechte $|t|\,\|\vec x\|^2$, die rechte ist also meist echt größer.
--- falsch
Weil dann $\|\vec y\|=t\,\|\vec x\|$ für jedes $t\in\mathbb{R}$ gilt, auch für negatives $t$; beide Seiten ergeben dann denselben Wert $t\,\|\vec x\|^2$.
:::
:::karte zusammenhang Umfang eines Rechtecks
Warum hat ein Rechteck mit der Fläche 16 mindestens den Umfang 16, und wann gilt Gleichheit?
---
Für die Seiten $a,b>0$ mit $ab=16$ ist der Umfang nach den Mittelwerten $2(a+b)\ge2\cdot2\sqrt{ab}=16$. Gleichheit gilt für $a=b=4$, das Quadrat, weil die Mittel bei gleichen Zahlen übereinstimmen.
--- falsch
Weil der Umfang eines Rechtecks immer so groß ist wie seine Fläche: Für jedes Rechteck gilt $2(a+b)=ab$, deshalb ist der Umfang genau 16, gleich welche Seiten es hat.
--- falsch
Für die Seiten $a,b>0$ mit $ab=16$ ist der Umfang nach den Mittelwerten höchstens $2\cdot2\sqrt{ab}=16$. Gleichheit gilt für $a=16$, $b=1$, das längste Rechteck.
--- falsch
Weil der Umfang mit der längsten Seite wächst und die längste Seite bei Fläche 16 mindestens 8 ist. Gleichheit gilt deshalb für $a=8$, $b=2$.
:::
::::
