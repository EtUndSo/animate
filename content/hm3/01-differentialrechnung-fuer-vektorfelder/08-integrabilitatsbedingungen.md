---
title: Stufe 7: Integrabilitätsbedingungen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110800
summary: Nicht jedes Feld ist ein Gradient.
tags: Integrabilitätsbedingungen, rotationsfrei, Gebieten, Sterngebiet
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Nicht jedes Feld ist ein Gradient. Diese Stufe liest aus der Jacobi-Matrix eine notwendige Bedingung ab, verbindet sie mit der Rotation und zeigt, dass sie allein nicht immer reicht.
:::

**Die Idee.** Ist $\boldsymbol{F}=\nabla\varphi$, dann sind die Einträge von $D\boldsymbol{F}$ zweite Ableitungen von $\varphi$. Zweite Ableitungen darf man vertauschen. Also muss $D\boldsymbol{F}$ symmetrisch sein. Das Drehfeld ist es nicht, das war der Grund in der Tabelle von Stufe [4](radiale-funktionen-und-felder.html#stufe-4).

:::satz Satz 7.1 (Integrabilitätsbedingungen)
<span class="anker" id="satz-7-1"></span>

Sei $\boldsymbol{F}=\nabla\varphi$ mit zweimal stetig differenzierbarem $\varphi$.

<ol class="rm">

<li>

Die Jacobi-Matrix ist symmetrisch, $D\boldsymbol{F}=(D\boldsymbol{F})^T$, das heißt, es gelten die __Integrabilitätsbedingungen__

<span class="anker" id="gl-7-1"></span>
$$\frac{\partial F_k}{\partial x_j}=\frac{\partial F_j}{\partial x_k}\qquad\text{für alle }1\le j,k\le n. \tag{7.1}$$

</li>

<li>

Für $n=2,3$ sind Gradientenfelder __rotationsfrei__: $\operatorname{rot}\nabla\varphi=0$.

</li>

</ol>
:::

:::beweis Integrabilitätsbedingungen
(i) Es ist $F_k=\partial\varphi/\partial x_k$, und nach dem Lemma von Schwarz gilt

$$\frac{\partial F_k}{\partial x_j}=\frac{\partial^2\varphi}{\partial x_j\,\partial x_k}=\frac{\partial^2\varphi}{\partial x_k\,\partial x_j}=\frac{\partial F_j}{\partial x_k}.$$

(ii) Jede Komponente von [(6.1)](rotation.html#gl-6-1) und [(6.4)](rotation.html#gl-6-4) ist eine Differenz $\partial F_k/\partial x_j-\partial F_j/\partial x_k$, also null nach (i).
:::

:::frage Woher kommt die Bedingung für Gradientenfelder in $n$ Dimensionen?
Aus der Vertauschbarkeit der zweiten Ableitungen, siehe den Beweis. Anschaulich: Lauf um ein kleines Rechteck mit den Seiten $a$ und $b$ in der $x_j$-$x_k$-Ebene (Abb. [7](#abb-7)). Längs einer Kante ändert sich das Potential ungefähr um Feldkomponente mal Kantenlänge. Die vier Änderungen ergeben zusammen etwa $ab\,(\partial F_k/\partial x_j-\partial F_j/\partial x_k)$. Das muss null sein, denn ein geschlossener Weg führt zum selben Potentialwert zurück. Jedes Paar von Richtungen spannt eine solche Ebene auf. Das ergibt $n(n-1)/2$ Bedingungen: keine für $n=1$, eine für $n=2$, drei für $n=3$, nämlich die Komponenten von $\operatorname{rot}\boldsymbol{F}$, sechs für $n=4$. Hinreichend sind sie nur auf geeigneten __Gebieten__, also offenen zusammenhängenden Mengen, etwa auf einem __Sterngebiet__: einem Gebiet mit einem Punkt, von dem aus die Strecke zu jedem anderen Punkt ganz im Gebiet liegt.
:::

:::abbildung hm3/k1rechteck 7
Rundweg um ein kleines Rechteck mit $Q=P+a\,\hat{\boldsymbol{e}}_j$ und $S=P+b\,\hat{\boldsymbol{e}}_k$. An den Kanten stehen die Änderungen des Potentials. Ihre Summe ist $b\,(F_k(Q)-F_k(P))-a\,(F_j(S)-F_j(P))$, also etwa $ab\,(\partial F_k/\partial x_j-\partial F_j/\partial x_k)$.
:::

**Eine einheitliche Darstellung.** In jeder Dimension sammelt man die Differenzen in der schiefsymmetrischen Matrix mit den Einträgen

<span class="anker" id="gl-7-2"></span>
$$\omega_{jk}=\frac12\Bigl(\frac{\partial F_k}{\partial x_j}-\frac{\partial F_j}{\partial x_k}\Bigr),\qquad1\le j,k\le n. \tag{7.2}$$

Jede quadratische Matrix ist die Summe eines symmetrischen und eines schiefsymmetrischen Anteils, und $(\omega_{jk})$ ist der schiefsymmetrische Anteil von $(D\boldsymbol{F})^T$. Die Bedingungen [(7.1)](#gl-7-1) heißen also $\omega_{jk}=0$ für alle $j,k$. Daraus erhält man die Rotation zurück:

<span class="anker" id="gl-7-3"></span>
$$(\operatorname{rot}\boldsymbol{F})_i=\sum_{j,k=1}^3\varepsilon_{ijk}\,\omega_{jk}\quad(n=3),\qquad\operatorname{rot}\boldsymbol{F}=\sum_{j,k=1}^2\varepsilon_{jk}\,\omega_{jk}\quad(n=2), \tag{7.3}$$

mit $\varepsilon_{12}=1$, $\varepsilon_{21}=-1$, $\varepsilon_{11}=\varepsilon_{22}=0$.

**Notwendig, nicht hinreichend.** Satz [7.1](#satz-7-1) sagt: $\operatorname{rot}\boldsymbol{F}=0$ ist notwendig dafür, dass ein stetig differenzierbares Feld ein Gradientenfeld ist. Die Kernfrage der Vektoranalysis ist die Umkehrung, und die lautet im Allgemeinen nein. Das Feld $\boldsymbol{H}=(-y,x)/(x^2+y^2)$ ist rotationsfrei (Aufgabe [8](rotation.html#aufg-8)). Wäre $\boldsymbol{H}=\nabla\varphi$ auf $\mathbb{R}^2\setminus\{0\}$, dann gäbe [(3.3)](die-kettenregel.html#gl-3-3) längs $\gamma(t)=(\cos t,\sin t)$

$$\frac{\mathrm{d}}{\mathrm{d} t}\,\varphi(\gamma(t))=\boldsymbol{H}(\gamma(t))\cdot\dot\gamma(t)=\sin^2t+\cos^2t=1.$$

Nach einem Umlauf wäre $\varphi$ um $2\pi$ gewachsen, obwohl man am selben Punkt steht. Das geht nicht. Dieses Gebiet hat ein Loch, um das der Weg herumläuft.

**Ein Potential finden.** Sind die Bedingungen erfüllt, integriert man Komponente für Komponente und prüft am Ende durch Ableiten. Beispiel $\boldsymbol{F}=(y+2xz,\;x+z^2,\;x^2+2yz)$ auf $\mathbb{R}^3$. Die drei Bedingungen stimmen: $1=1$, $2x=2x$, $2z=2z$. Aus $\partial\varphi/\partial x=y+2xz$ folgt $\varphi=xy+x^2z+c(y,z)$. Die Ableitung nach $y$ gibt $x+\partial c/\partial y=x+z^2$, also $c=yz^2+d(z)$. Die Ableitung nach $z$ gibt $x^2+2yz+d'(z)=x^2+2yz$, also ist $d$ konstant. Ergebnis: $\varphi=xy+x^2z+yz^2+\text{konst}$.

:::aufgabe Aufgabe 9 ★★ Potential suchen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Für welche $a\in\mathbb{R}$ hat $\boldsymbol{F}=(2xy+z^2,\;a\,x^2+z,\;2xz+y)$ auf $\mathbb{R}^3$ ein Skalarpotential? Gib es an.

</li>

<li>

Hat $\boldsymbol G=(yz,\;xz^2,\;xy)$ ein Skalarpotential?

</li>

<li>

Für welche $a\in\mathbb{R}$ hat $\boldsymbol{E}(x,y)=\dfrac{(a\,y,\;x)}{(x+y)^2}$ auf der Halbebene $x+y>0$ ein Skalarpotential? Gib es an.

</li>

</ol>

:::loesung
(a) $\partial_yF_1=2x$, $\partial_xF_2=2ax$ verlangt $a=1$. Die anderen Bedingungen stimmen: $2z=2z$, $1=1$. Aus $\partial_x\varphi=2xy+z^2$ folgt $\varphi=x^2y+xz^2+c(y,z)$. Dann $\partial_y$: $x^2+c_y=x^2+z$, also $c=yz+d(z)$, und $\partial_z$: $2xz+y+d'=2xz+y$. Ergebnis: $\varphi=x^2y+xz^2+yz+\text{konst}$. (b) Nein: $\partial_zG_2=2xz$, aber $\partial_yG_3=x$. Das ist nicht überall gleich, also ist [(7.1)](#gl-7-1) verletzt. (c) $\partial_yE_1=a\frac{x-y}{(x+y)^3}$ und $\partial_xE_2=\frac{y-x}{(x+y)^3}$. Also muss $a=-1$ sein. Dann gibt $\partial_x\varphi=-y/(x+y)^2$ die Funktion $\varphi=\frac{y}{x+y}+c(y)$, und $\partial_y\varphi=\frac{x}{(x+y)^2}+c'(y)$ verlangt $c'=0$. Ergebnis: $\varphi=\frac{y}{x+y}+\text{konst}$.
:::
:::
