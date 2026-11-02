---
title: Stufe 8: Körper zwischen zwei Flächen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3121000
summary: Derselbe Gedanke eine Dimension höher: Ein Körper zwischen Boden und Deckel wird zu einem Integral über seinen Schatten.
tags: Oktant
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Derselbe Gedanke eine Dimension höher: Ein Körper zwischen Boden und Deckel wird zu einem Integral über seinen Schatten.
:::

**Die Idee.** Über jedem Punkt $(x,y)$ des Schattens $D$ steht ein senkrechter Stab vom Boden bis zum Deckel. Man integriert zuerst längs des Stabs, also über $z$, und danach über den Schatten (Abb. [8](#abb-8)). Der Begriff Normalbereich lässt sich so von Dimension zu Dimension fortsetzen. Hier genügt der Raum.

:::satz Satz 8.1 (Räumliche Normalbereiche)
<span class="anker" id="satz-8-1"></span>

Sei $D\subset\mathbb{R}^2$ eine endliche Vereinigung regulärer Normalbereiche wie in [(7.3)](bereiche-zwischen-zwei-kurven.html#gl-7-3), $\mu,\nu:D\to\mathbb{R}$ stetig mit $\mu\le\nu$ und

$$M=\{(x,y,z)\in\mathbb{R}^3:\mu(x,y)\le z\le\nu(x,y),\ (x,y)\in D\}.$$

Für stetiges $f:M\to\mathbb{R}$ gilt

<span class="anker" id="gl-8-1"></span>
$$\int_Mf(x,y,z)\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_D\Bigl(\int_{\mu(x,y)}^{\nu(x,y)}f(x,y,z)\,\mathrm{d} z\Bigr)\mathrm{d} x\,\mathrm{d} y. \tag{8.1}$$
:::

⁠**So liest man das:** $\mu(x,y)$ ist die Höhe des Bodens, $\nu(x,y)$ die des Deckels über dem Punkt $(x,y)$, und $D$ der Schatten in der $x$-$y$-Ebene. Das innere Integral hängt noch von $x$ und $y$ ab, das äußere ist ein Integral aus Stufe [7](bereiche-zwischen-zwei-kurven.html#stufe-7). Für $f\equiv1$ ist $\operatorname{vol}(M)=\int_D(\nu-\mu)\,\mathrm{d} x\,\mathrm{d} y$. Ist der Boden eben und $\nu-\mu=H$ konstant, bleibt $H\,|D|$: Grundfläche mal Höhe.

:::abbildung hm3/k2raum 8
Der Körper $M$ aus zwei Zylindern mit Radius 2 im ersten Oktanden. Der Schatten $D$ ist ein Viertelkreis in der $x$-$y$-Ebene. Über dem Punkt $(x,y)$ reicht der Stab von $z=0$ bis zum Deckel $z=\sqrt{4-x^2}$.
:::

**Beispiel: noch einmal die Kuppel.** Mit Boden $\mu=0$, Deckel $\nu=4-x^2-y^2$ und Kreisscheibe $D$ ist

$$\operatorname{vol}(K)=\int_{-2}^2\Bigl(\int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}}(4-y^2-x^2)\,\mathrm{d} x\Bigr)\mathrm{d} y=\frac43\int_{-2}^2(4-y^2)^{3/2}\,\mathrm{d} y=8\pi.$$

Innen gilt $\int_{-w}^w(w^2-x^2)\,\mathrm{d} x=\frac43w^3$ mit $w=\sqrt{4-y^2}$. Außen gibt die Substitution $y=2\sin s$ den Wert $16\int_{-\pi/2}^{\pi/2}\cos^4s\,\mathrm{d} s=6\pi$. Das stimmt mit [(6.3)](mengen-und-scheiben.html#gl-6-3) überein, und die Scheiben waren viel bequemer.

**Beispiel: zwei Zylinder.** Sei $M=Z_1\cap Z_2\cap O$ mit den Zylindern $Z_1=\{x^2+y^2\le4\}$, $Z_2=\{x^2+z^2\le4\}$ und $O=\{x\ge0,\ y\ge0,\ z\ge0\}$. Dieses Achtel des Raums heißt __Oktant__. $Z_2$ begrenzt $z$, $Z_1$ begrenzt $y$, beide über $x$:

$$M=\{0\le z\le\sqrt{4-x^2},\ (x,y)\in D\},\qquad D=\{0\le y\le\sqrt{4-x^2},\ 0\le x\le2\}.$$

$D$ ist ein ebener Normalbereich vom Typ 2. Also ist

$$\int_Mf\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_0^2\Bigl(\int_0^{\sqrt{4-x^2}}\Bigl(\int_0^{\sqrt{4-x^2}}f(x,y,z)\,\mathrm{d} z\Bigr)\mathrm{d} y\Bigr)\mathrm{d} x.$$

Für $f\equiv1$ gibt das $\operatorname{vol}(M)=\int_0^2(4-x^2)\,\mathrm{d} x=\frac{16}3$. Für $f=x^2+y^2+z^2$ ist das innere Doppelintegral $x^2w^2+\frac23w^4$ mit $w^2=4-x^2$, und es folgt $\frac{704}{45}\approx15{,}6$.

:::merke Vorgehen bei jedem Mehrfachintegral
Den Bereich skizzieren und als Normalbereich schreiben, nötigenfalls zerlegen. Von innen nach außen integrieren: Innen stehen Funktionen der äußeren Variablen, ganz außen Zahlen. Die Reihenfolge so wählen, dass die Rechnung kurz wird.
:::

:::frage Wie erkenne ich, welche Variable innen stehen muss?
Die Variable, deren Grenzen sich am leichtesten als Funktionen der anderen schreiben lassen. Bei den zwei Zylindern hängen die Grenzen von $y$ und $z$ nur von $x$ ab, also steht $x$ außen. Mit $x$ innen müsste man den Bereich zerlegen, denn dann gilt $x\le\sqrt{4-\max(y,z)^2}$.
:::

:::aufgabe Aufgabe 12 ★★ Körper als Normalbereich
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Sei $T=\{x,y,z\ge0,\ x+\frac y2+\frac z3\le1\}$. Schreibe $T$ als räumlichen Normalbereich und berechne $\operatorname{vol}(T)$ und $\int_Tx\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z$.

</li>

<li>

Berechne das Volumen des Körpers über der Einheitskreisscheibe zwischen den Ebenen $z=-1-x$ und $z=2+y$. Tipp: Symmetrie.

</li>

</ol>

:::loesung
(a) $0\le z\le3(1-x-\frac y2)$ über $D=\{0\le y\le2(1-x),\ 0\le x\le1\}$. Mit $L=2(1-x)$ ist $\int_0^L3(\frac L2-\frac y2)\,\mathrm{d} y=\frac34L^2=3(1-x)^2$. Also ist $\operatorname{vol}(T)=\int_0^13(1-x)^2\,\mathrm{d} x=1$ und $\int_Tx\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_0^13x(1-x)^2\,\mathrm{d} x=\frac14$. (b) Die Höhe ist $(2+y)-(-1-x)=3+x+y>0$ auf $D$. Die Kreisscheibe ist symmetrisch zu beiden Achsen, $x$ und $y$ sind ungerade, das innere Integral verschwindet also jeweils. Es bleibt $\operatorname{vol}=3\,|D|=3\pi$.
:::
:::
