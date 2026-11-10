---
title: Stufe 3: Drei Standardfälle
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralsätze im Raum
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum
knoten: Kapitel 5: Integralsätze im Raum
order: 3150400
summary: Fast alle Rechnungen führen auf einen von drei Fällen: Graph, Kugel, Rotationsfläche.
tags: 
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Fast alle Rechnungen führen auf einen von drei Fällen: Graph, Kugel, Rotationsfläche. Diese Stufe liefert die fertigen Formeln mit ihrer Herleitung.
:::

:::satz Satz 3.1 (Graph, Kugel, Rotationsfläche)
<span class="anker" id="satz-3-1"></span>

<ol class="rm">

<li>

⁠**Graph** $z=H(x,y)$ über $B$: $E=1+H_x^2$, $F=H_xH_y$, $G=1+H_y^2$ und

<span class="anker" id="gl-3-1"></span>
$$\mathrm{d}\sigma=\sqrt{1+|\nabla H|^2}\;\mathrm{d} x\,\mathrm{d} y. \tag{3.1}$$

</li>

<li>

⁠**Kugel** $\partial B_R(0)$ mit $\boldsymbol{x}(\theta,\varphi)=R(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)$:

<span class="anker" id="gl-3-2"></span>
$$\int_{\partial B_R(0)}f\,\mathrm{d}\sigma=R^2\int_0^{2\pi}\!\!\int_0^\pi f(\boldsymbol{x}(\theta,\varphi))\sin\theta\;\mathrm{d}\theta\,\mathrm{d}\varphi. \tag{3.2}$$

</li>

<li>

⁠**Rotationsfläche** aus der Kurve $\gamma(t)=(x(t),z(t))$, $t\in[a,b]$, durch Drehen um die $z$-Achse:

<span class="anker" id="gl-3-3"></span>
$$\mathcal A(\mathcal F)=2\pi\int_a^b\sqrt{\dot x(t)^2+\dot z(t)^2}\;|x(t)|\;\mathrm{d} t. \tag{3.3}$$

</li>

</ol>
:::

:::herleitung Die drei Fälle
(i) $\Phi(x,y)=(x,y,H)$ gibt $\Phi_x=(1,0,H_x)$, $\Phi_y=(0,1,H_y)$. Daraus folgen $E$, $F$, $G$, und $EG-F^2=(1+H_x^2)(1+H_y^2)-H_x^2H_y^2=1+H_x^2+H_y^2$.

(ii) $\boldsymbol{x}_\theta=R(\cos\theta\cos\varphi,\cos\theta\sin\varphi,-\sin\theta)$, $\boldsymbol{x}_\varphi=R(-\sin\theta\sin\varphi,\sin\theta\cos\varphi,0)$. Das gibt $E=R^2$, $F=0$, $G=R^2\sin^2\theta$ und $\sqrt{EG-F^2}=R^2\sin\theta$. Diese Parametrisierung ist an den Polen nicht regulär und nicht global injektiv, aber die Ausnahmemenge hat die Fläche null, die Formel gilt trotzdem.

(iii) $\boldsymbol{x}(t,\varphi)=(x\cos\varphi,x\sin\varphi,z)$ gibt $\boldsymbol{x}_t=(\dot x\cos\varphi,\dot x\sin\varphi,\dot z)$, $\boldsymbol{x}_\varphi=(-x\sin\varphi,x\cos\varphi,0)$. Also $E=\dot x^2+\dot z^2$, $F=0$, $G=x^2$ und $\sqrt{EG-F^2}=|x|\sqrt{\dot x^2+\dot z^2}$. Die Integration über $\varphi$ liefert $2\pi$.
:::

⁠**So liest man das:** In (iii) ist $\sqrt{\dot x^2+\dot z^2}\,\mathrm{d} t$ das Längenstück der Kurve und $2\pi|x|$ der Umfang des Kreises, den dieses Stück beim Drehen beschreibt. Die Fläche ist also ein Stapel dünner Ringe. **Kontrolle:** Für die Kugel mit $f=1$ gibt [(3.2)](#gl-3-2) den Inhalt $R^2\cdot2\pi\cdot2=4\pi R^2$, bei $R=2$ also $16\pi$. Für einen ebenen Graphen $H=\text{konst}$ ist der Faktor in [(3.1)](#gl-3-1) gleich 1.

:::aufgabe Aufgabe 3 ★★ Torus
<span class="anker" id="aufg-3"></span>

Ein Kreis mit Radius 1 um den Punkt $(2,0)$ in der $x$-$z$-Ebene dreht sich um die $z$-Achse. Berechne die Oberfläche des entstehenden Torus.

:::loesung
$\gamma(t)=(2+\cos t,\,\sin t)$ mit $t\in[0,2\pi]$ hat $\dot x^2+\dot z^2=1$. Aus [(3.3)](#gl-3-3) folgt $\mathcal A=2\pi\int_0^{2\pi}(2+\cos t)\,\mathrm{d} t=2\pi\cdot4\pi=8\pi^2\approx79{,}0$. Der $\cos t$-Anteil fällt weg: Außen ist der Ring länger, innen kürzer, im Mittel zählt der Radius 2.
:::
:::

:::aufgabe Aufgabe 4 ★★ Integral über ein Paraboloid
<span class="anker" id="aufg-4"></span>

Sei $P$ der Graph $z=x^2+y^2$ über $x^2+y^2\le2$. Berechne $\int_Pz\,\mathrm{d}\sigma$. Tipp: Polarkoordinaten, dann $w=1+4r^2$.

:::loesung
Mit [(3.1)](#gl-3-1) ist $\mathrm{d}\sigma=\sqrt{1+4r^2}\,r\,\mathrm{d} r\,\mathrm{d}\varphi$ und $z=r^2$. Mit $w=1+4r^2$ ist $r\,\mathrm{d} r=\mathrm{d} w/8$ und $r^2=(w-1)/4$:

$$\int_Pz\,\mathrm{d}\sigma=2\pi\int_1^9\frac{w-1}{4}\sqrt w\,\frac{\mathrm{d} w}{8}=\frac\pi{16}\Bigl[\tfrac25w^{5/2}-\tfrac23w^{3/2}\Bigr]_1^9=\frac\pi{16}\cdot\frac{1192}{15}=\frac{149\pi}{30}\approx15{,}6.$$
:::
:::

:::aufgabe Aufgabe 5 ★★ Rechnen mit Symmetrie
<span class="anker" id="aufg-5"></span>

Berechne $\int_{\partial B_2(0)}x^2\,\mathrm{d}\sigma$, ohne ein Integral auszuwerten. Tipp: Was ergibt $\int(x^2+y^2+z^2)\,\mathrm{d}\sigma$, und warum sind die drei Summanden gleich groß?

:::loesung
Auf der Kugel ist $x^2+y^2+z^2=4$, also $\int(x^2+y^2+z^2)\,\mathrm{d}\sigma=4\cdot16\pi=64\pi$. Vertauschen der Koordinaten bildet die Kugel auf sich ab, die drei Integrale sind also gleich. Damit ist $\int x^2\,\mathrm{d}\sigma=\frac{64\pi}{3}$.
:::
:::
