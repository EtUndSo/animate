---
title: Stufe 9: Elementare Ungleichungen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
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

⁠**So liest man das:** $\vec x=(x_1,\dots,x_n)$ ist ein __Vektor__, eine Liste von $n$ Zahlen, und $\|\vec x\|$ seine __Norm__. Für $n=2$ ist das nach Pythagoras die Länge des Pfeils vom Ursprung zum Punkt $(x_1,x_2)$. Dann ist [(9.2)](#gl-9-2) die Dreiecksungleichung für Pfeile, und in [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) wird aus [(9.1)](#gl-9-1) das Skalarprodukt. Bei Young ist $\varepsilon$ ein Tauschkurs: Ein kleiner $x$-Term kostet einen großen $y$-Term. **Warum die Voraussetzungen:** Bernoulli: $x=-4$, $n=3$ gibt $-27>-11$, falsch, also braucht man $x>-1$. Für $x=0$ oder $n=1$ steht Gleichheit. Mittelwerte: $x=y=-1$ gibt $1\le-1$, falsch. Young: $\varepsilon=-1$ macht die rechte Seite negativ.

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

**Beispiel.** Bernoulli: $1{,}01^{10}>1{,}1$, exakt $1{,}1046$. Für kleines $x$ ist $1+nx$ eine gute Näherung: 1 % mehr Spannung bedeutet an einem Widerstand rund 2 % mehr Leistung, exakt 2,01 %. Für großes $x$ ist sie grob: $2^{10}=1024$ gegen 11. Young mit $x=2$, $y=8$: Für $\varepsilon=1$ steht $16\le34$, für $\varepsilon=4$ steht $16\le16$. Cauchy-Schwarz mit $\vec x=(3,4)$, $\vec y=(1,2)$: $3+8=11\le5\sqrt5\approx11{,}18$. Minkowski: $\|(4,6)\|=\sqrt{52}\approx7{,}21\le5+\sqrt5\approx7{,}24$. **Grenzfall:** Bei $x=y$ sind beide Mittel gleich, im Halbkreis steht die Höhe auf der Mitte.

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
