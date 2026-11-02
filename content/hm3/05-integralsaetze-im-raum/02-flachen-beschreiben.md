---
title: Stufe 1: Flächen beschreiben
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3150200
summary: Eine gekrümmte Fläche lässt sich nicht mit d x\,d y integrieren.
tags: Gebiet, reguläres Flächenstück, reguläre Parametrisierung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine gekrümmte Fläche lässt sich nicht mit $\mathrm{d} x\,\mathrm{d} y$ integrieren. Man beschreibt sie deshalb als Bild eines ebenen Bereichs. Diese Stufe sagt, welche Abbildungen dafür taugen.
:::

**Die Idee.** Eine Kurve ist das Bild eines Intervalls: Man läuft einen Parameter $t$ ab und erhält Punkte im Raum. Eine Fläche braucht zwei Parameter. Man legt ein ebenes Blatt $B$ mit Koordinaten $(u,v)$ hin und biegt es in den Raum, ohne dass es reißt oder sich selbst berührt (Abb. [1](#abb-1)). Die Gitterlinien des Blatts werden zu Linien auf der Fläche. Läuft man auf einer davon, ändert sich nur ein Parameter. Ihre Tangenten sind die Ableitungen $\boldsymbol{x}_u$ und $\boldsymbol{x}_v$.

:::abbildung hm3/k5flaeche 1
Die Parametrisierung biegt das ebene Blatt $B$ zur Kuppel $K$. Eine Gitterlinie $v=\text{konst}$ wird zu einer Kurve auf der Fläche, ihre Tangente ist $\boldsymbol{x}_u$. Dasselbe gilt für $u=\text{konst}$ und $\boldsymbol{x}_v$. Beide Tangenten spannen die Tangentialebene auf, $\boldsymbol{x}_u\times\boldsymbol{x}_v$ steht darauf senkrecht.
:::

:::definition Definition 1.1 (Reguläres Flächenstück)
<span class="anker" id="satz-1-1"></span>

Sei $\mathcal G\subset\mathbb{R}^2$ ein __Gebiet__ (offen und zusammenhängend) und $\Phi:\mathcal G\to\mathbb{R}^3$, $\Phi(u,v)=(x(u,v),y(u,v),z(u,v))$, stetig differenzierbar. Sei $B\subset\mathcal G$ ein regulärer Bereich, dessen Inneres einfach zusammenhängend ist, sein Rand $\partial B$ besteht also aus einer geschlossenen Kurve. Ist $\Phi$ auf $B$ injektiv und gilt

<span class="anker" id="gl-1-1"></span>
$$\frac{\partial\Phi}{\partial u}\times\frac{\partial\Phi}{\partial v}\neq(0,0,0)\quad\text{auf }B, \tag{1.1}$$

dann heißt $\mathcal F=\Phi(B)$ __reguläres Flächenstück__ und $\Phi$ eine __reguläre Parametrisierung__.
:::

⁠**So liest man das:** Die Injektivität verbietet, dass sich das Blatt selbst berührt. Die Bedingung [(1.1)](#gl-1-1) verbietet, dass es an einer Stelle zu einer Kurve oder einem Punkt zusammengedrückt wird: Das Kreuzprodukt ist genau dann null, wenn $\boldsymbol{x}_u$ und $\boldsymbol{x}_v$ parallel sind, und dann spannen sie keine Ebene auf. Schreibt man kurz $\boldsymbol{x}=\Phi(u,v)$, so ist $\boldsymbol{x}_u=\partial\Phi/\partial u$.

:::satz Satz 1.2 (Basis in jedem Flächenpunkt)
<span class="anker" id="satz-1-2"></span>

Für eine reguläre Parametrisierung bilden

<span class="anker" id="gl-1-2"></span>
$$\boldsymbol{t}_1=\frac{\boldsymbol{x}_u}{|\boldsymbol{x}_u|},\qquad\boldsymbol{t}_2=\frac{\boldsymbol{x}_v}{|\boldsymbol{x}_v|},\qquad\boldsymbol{n}=\frac{\boldsymbol{x}_u\times\boldsymbol{x}_v}{|\boldsymbol{x}_u\times\boldsymbol{x}_v|} \tag{1.2}$$

in jedem Punkt eine normierte Basis des $\mathbb{R}^3$.
:::

⁠**So liest man das:** $\boldsymbol{t}_1$ und $\boldsymbol{t}_2$ liegen in der Tangentialebene, $\boldsymbol{n}$ steht darauf senkrecht. Die drei Vektoren sind linear unabhängig, weil $\boldsymbol{x}_u\times\boldsymbol{x}_v\neq0$ gilt. Eine Orthonormalbasis ist das im Allgemeinen nicht: $\boldsymbol{t}_1$ und $\boldsymbol{t}_2$ müssen nicht senkrecht aufeinander stehen.

**Beispiel: die Kuppel.** In Polarkoordinaten lautet die Parametrisierung

<span class="anker" id="gl-1-3"></span>
$$\Phi(r,\varphi)=\begin{pmatrix}r\cos\varphi\\r\sin\varphi\\4-r^2\end{pmatrix},\qquad\Phi_r=\begin{pmatrix}\cos\varphi\\\sin\varphi\\-2r\end{pmatrix},\qquad\Phi_\varphi=\begin{pmatrix}-r\sin\varphi\\r\cos\varphi\\0\end{pmatrix}. \tag{1.3}$$

Das Kreuzprodukt ist $\Phi_r\times\Phi_\varphi=(2r^2\cos\varphi,\;2r^2\sin\varphi,\;r)$. Im Punkt $(1,0,3)$ ($r=1$, $\varphi=0$) ergibt das $(2,0,1)$, also $\boldsymbol{n}=(2,0,1)/\sqrt5$: schräg nach oben außen, wie man es auf einer Kuppel erwartet. Bei $r=0$ wird das Kreuzprodukt null, obwohl die Fläche dort völlig glatt ist. Das liegt an den Polarkoordinaten, nicht an der Fläche.

:::frage Heißt das, die Kuppel ist an der Spitze nicht regulär?
Doch, sie ist regulär, nur diese Parametrisierung nicht. Als Graph $(x,y)\mapsto(x,y,4-x^2-y^2)$ ist überall $\Phi_x\times\Phi_y=(2x,2y,1)\neq0$. Regularität ist eine Eigenschaft der Parametrisierung. Für Integrale spielt ein einzelner Ausnahmepunkt keine Rolle, er hat die Fläche null. Deshalb darf man Polar- und Kugelkoordinaten trotzdem benutzen.
:::

:::aufgabe Aufgabe 1 ★ Parametrisieren
<span class="anker" id="aufg-1"></span>

Parametrisiere den Zylindermantel $x^2+y^2=9$, $0\le z\le5$, durch $(\varphi,z)$. Berechne $\boldsymbol{x}_\varphi\times\boldsymbol{x}_z$ und entscheide, ob der Vektor nach außen zeigt.

:::loesung
$\boldsymbol{x}(\varphi,z)=(3\cos\varphi,\,3\sin\varphi,\,z)$ mit $0\le\varphi<2\pi$, $0\le z\le5$. Dann $\boldsymbol{x}_\varphi=(-3\sin\varphi,3\cos\varphi,0)$, $\boldsymbol{x}_z=(0,0,1)$ und $\boldsymbol{x}_\varphi\times\boldsymbol{x}_z=(3\cos\varphi,3\sin\varphi,0)$. Das ist der Ortsvektor in der $x$-$y$-Ebene, zeigt also nach außen. Sein Betrag ist 3, der Mantel hat die Fläche $3\cdot2\pi\cdot5=30\pi$.
:::
:::

:::aufgabe Aufgabe 2 ★ Regulär oder nicht?
<span class="anker" id="aufg-2"></span>

Prüfe [(1.1)](#gl-1-1). Was ist jeweils das Bild?

<ol class="al">

<li>

$\Phi(u,v)=(u,\,v,\,u^2+v^2)$ auf $\mathbb{R}^2$.

</li>

<li>

$\Phi(r,\varphi)=(r\cos\varphi,\,r\sin\varphi,\,r)$ für $0\le r\le1$, $0\le\varphi<2\pi$.

</li>

<li>

$\Phi(u,v)=(u+v,\,(u+v)^2,\,(u+v)^3)$ auf $\mathbb{R}^2$.

</li>

</ol>

:::loesung
(a) $\Phi_u\times\Phi_v=(-2u,-2v,1)\neq0$, injektiv. Regulär, das Bild ist ein Paraboloid. (b) $\Phi_r\times\Phi_\varphi=(-r\cos\varphi,-r\sin\varphi,r)$ ist bei $r=0$ null. Das Bild ist ein Kegel, und dort sitzt seine Spitze. Anders als bei der Kuppel liegt das nicht an den Koordinaten: Der Kegel hat in der Spitze keine Tangentialebene. (c) $\Phi_u=\Phi_v$, das Kreuzprodukt ist überall null. Das Bild ist eine Kurve, keine Fläche.
:::
:::
