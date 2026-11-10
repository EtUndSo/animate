---
title: Stufe 5: Skalarprodukt, Norm, Abstand
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektoren und Skalarprodukt
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt
knoten: Kapitel 8: Vektoren und Skalarprodukt
order: 1280700
summary: Bisher kann man addieren und strecken, aber nichts messen.
tags: Skalarprodukt, orthogonale, senkrecht, euklidische Norm, Länge, Abstand, Linearität, Symmetrie
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher kann man addieren und strecken, aber nichts messen. Diese Stufe führt in $\mathbb{R}^n$ ($\mathbb K=\mathbb{R}$) eine neue Rechenart ein, aus der Länge und „senkrecht“ folgen.
:::

**Die Idee.** In der Ebene gibt Pythagoras die Länge: $\|\vec x\|^2=x_1^2+x_2^2$. Im Raum wendet man ihn zweimal an, erst in der Grundfläche, dann mit der Höhe (Abb. [6](#abb-6)). Wie lang ist nun eine Summe? Ausmultiplizieren ergibt

$$\sum_{i=1}^n(x_i+y_i)^2=\sum_{i=1}^nx_i^2+\sum_{i=1}^ny_i^2+2\sum_{i=1}^nx_iy_i.$$

Die ersten beiden Summen wären Pythagoras, der letzte Term ist die Korrektur. Stehen die Pfeile senkrecht, muss sie verschwinden. Also misst $\sum_ix_iy_i$, wie weit zwei Pfeile von „senkrecht“ entfernt sind.

:::abbildung hm1/k8norm 6
Länge von $\vec x=(2,1,2)$ im Raum. In der Grundfläche gibt Pythagoras die Diagonale $\sqrt{2^2+1^2}=\sqrt5$. Sie steht senkrecht auf der Höhe 2, also ist $\|\vec x\|=\sqrt{5+2^2}=3$.
:::

:::definition Definition 5.1 (Skalarprodukt, orthogonal, Norm, Abstand)
<span class="anker" id="satz-5-1"></span>

<ol class="al">

<li>

Für $\vec x,\vec y\in\mathbb{R}^n$ heißt

<span class="anker" id="gl-5-1"></span>
$$\langle\vec x,\vec y\rangle:=x_1y_1+\dots+x_ny_n=\sum_{i=1}^nx_iy_i\in\mathbb{R} \tag{5.1}$$

das __Skalarprodukt__ von $\vec x$ und $\vec y$.

</li>

<li>

$\vec x$ und $\vec y$ heißen zueinander __orthogonale__ Vektoren, falls $\langle\vec x,\vec y\rangle=0$. Man schreibt $\vec x\perp\vec y$ und sagt auch, sie stehen __senkrecht__.

</li>

<li>

Die Abbildung $\|\cdot\|:\mathbb{R}^n\to\mathbb{R}_0^+$, $\vec x\mapsto\|\vec x\|:=\sqrt{\langle\vec x,\vec x\rangle}=\sqrt{x_1^2+\dots+x_n^2}$, heißt __euklidische Norm__ auf $\mathbb{R}^n$. Die Zahl $\|\vec x\|$ heißt Norm oder __Länge__ von $\vec x$.

</li>

<li>

Die Zahl $d(\vec x,\vec y):=\|\vec x-\vec y\|=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}$ heißt __Abstand__ zwischen $\vec x$ und $\vec y$.

</li>

</ol>
:::

⁠**So liest man das:** Das Ergebnis von [(5.1)](#gl-5-1) ist eine Zahl, kein Vektor. Im Modell ist $\langle\vec a,\vec b\rangle=3+2=5$, $\|\vec a\|=\sqrt{10}=3{,}162$, $\|\vec b\|=\sqrt5=2{,}236$ und $d(\vec a,\vec b)=\|(2,-1)\|=\sqrt5$. Die Korrektur der Idee zeigt sich so: $\|\vec a+\vec b\|^2=25$, aber $\|\vec a\|^2+\|\vec b\|^2=15$, der Unterschied ist $2\cdot5$. Für Einheitsvektoren in $\mathbb{R}^n$ gilt $\|\vec e_j\|=1$ und $\langle\vec e_i,\vec e_j\rangle=0$ für $i\ne j$.

:::satz Satz 5.2 (Eigenschaften von Skalarprodukt und Norm)
<span class="anker" id="satz-5-2"></span>

Für alle $\alpha,\beta\in\mathbb{R}$ und alle $\vec x,\vec y,\vec z\in\mathbb{R}^n$ gilt:

<ul>

<li>

⁠**(S)** $\langle\alpha\vec x+\beta\vec y,\vec z\rangle=\alpha\langle\vec x,\vec z\rangle+\beta\langle\vec y,\vec z\rangle$ (__Linearität__), $\langle\vec x,\vec y\rangle=\langle\vec y,\vec x\rangle$ (__Symmetrie__), $\langle\vec x,\vec x\rangle=0\iff\vec x=\vec0$ (__Definitheit__), $\langle\vec x,\vec x\rangle>0$ für $\vec x\ne\vec0$ (__Positivität__).

</li>

<li>

⁠**(N)** $\|\vec x\|=0\iff\vec x=\vec0$ (Definitheit), $\|\alpha\vec x\|=|\alpha|\cdot\|\vec x\|$ (__Homogenität__), $\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|$ (__Dreiecksungleichung__ in $\mathbb{R}^n$).

</li>

</ul>

Außerdem gilt für den Abstand $d(\vec x,\vec y)\le d(\vec x,\vec z)+d(\vec z,\vec y)$.
:::

⁠**So liest man das:** Wegen der Symmetrie ist $\langle\cdot,\cdot\rangle$ auch im zweiten Eingang linear, man sagt __bilinear__. Die Dreiecksungleichung sagt: Ein Umweg ist nie kürzer.

:::beweis Aus der Formel
(S): Nach [(5.1)](#gl-5-1) ist $\sum_i(\alpha x_i+\beta y_i)z_i=\alpha\sum_ix_iz_i+\beta\sum_iy_iz_i$ und $\sum_ix_iy_i=\sum_iy_ix_i$. Weiter ist $\langle\vec x,\vec x\rangle=\sum_ix_i^2$ eine Summe von Quadraten. Sie ist positiv, sobald ein $x_i\ne0$ ist, und null genau für $x_1=\dots=x_n=0$.

(N): Die Definitheit folgt aus (S). Homogenität: $\sqrt{\sum_i\alpha^2x_i^2}=\sqrt{\alpha^2}\sqrt{\sum_ix_i^2}$ und $\sqrt{\alpha^2}=|\alpha|$. Die Dreiecksungleichung ist die Minkowski-Ungleichung aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html), in Stufe [7](winkel-cauchy-schwarz-parallelogramm.html#stufe-7) folgt ein kurzer Beweis.

Abstand: $\|\vec x-\vec y\|=\|(\vec x-\vec z)+(\vec z-\vec y)\|\le\|\vec x-\vec z\|+\|\vec z-\vec y\|$.
:::

**Bilinear rechnen.** Wie bei $(a\pm b)^2=a^2\pm2ab+b^2$ multipliziert man mit (S) aus:

<span class="anker" id="gl-5-2"></span>
$$\|\vec x\pm\vec z\|^2=\langle\vec x\pm\vec z,\vec x\pm\vec z\rangle=\|\vec x\|^2\pm2\langle\vec x,\vec z\rangle+\|\vec z\|^2. \tag{5.2}$$

Für $\vec x\perp\vec z$ fällt die Mitte weg: $\|\vec x+\vec z\|^2=\|\vec x\|^2+\|\vec z\|^2$. Das ist Pythagoras in $\mathbb{R}^n$, die wichtigste Folgerung für die nächsten Stufen. Beispiel: $\vec h=(-1,3)$ steht senkrecht auf $\vec a$, und $\|\vec a+\vec h\|^2=\|(2,4)\|^2=20=10+10$. **Grenzfall:** Für $\vec z=\vec x$ gibt [(5.2)](#gl-5-2) $\|2\vec x\|^2=4\|\vec x\|^2$, passend zur Homogenität.

:::frage Ist das Skalarprodukt dasselbe wie die skalare Multiplikation?
Nein, trotz der ähnlichen Namen. Die skalare Multiplikation nimmt eine Zahl und einen Vektor und gibt einen Vektor. Das Skalarprodukt nimmt zwei Vektoren und gibt eine Zahl.
:::

:::aufgabe Aufgabe 6 ★ Messen
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Berechne $\langle\vec c,\vec f\rangle$, $\|\vec f\|$ und $d(\vec c,\vec f)$.

</li>

<li>

Für welches $t$ steht $(t,2,1)$ senkrecht auf $(2,1,2)$?

</li>

<li>

Normiere $(2,1,2)$, also finde den Vektor gleicher Richtung mit Länge 1.

</li>

</ol>

:::loesung
(a) $\langle\vec c,\vec f\rangle=8+1+0=9$, $\|\vec f\|=\sqrt{21}$, $d(\vec c,\vec f)=\|(-2,0,2)\|=\sqrt8$. (b) $2t+2+2=0$, also $t=-2$. (c) $\frac13(2,1,2)=(\frac23,\frac13,\frac23)$.
:::
:::
