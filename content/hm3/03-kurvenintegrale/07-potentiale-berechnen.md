---
title: Stufe 6: Potentiale berechnen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130700
summary: Das Integral längs der Strecke wird schnell unbequem.
tags: Eichfreiheit, Coulomb-Eichung, Poisson-Gleichung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Das Integral längs der Strecke wird schnell unbequem. Diese Stufe gibt einen bequemeren Weg und klärt, wie weit ein Potential festliegt.
:::

**Die Idee.** Weil das Integral nicht vom Weg abhängt, nimmt man den bequemsten: Stücke parallel zu den Achsen (Abb. [6](#abb-6)). Auf jedem Stück ändert sich nur eine Koordinate, also zählt nur eine Komponente von $\boldsymbol{F}$.

:::abbildung hm3/k3achsen 6
Statt der Strecke (gestrichelt) läuft man erst in $x$-, dann in $y$-, dann in $z$-Richtung. Auf jedem Stück steht die zugehörige Komponente im Integral. Erledigte Koordinaten haben ihren Endwert, kommende noch ihren Startwert.
:::

:::satz Satz 6.1 (Potential längs der Achsen)
<span class="anker" id="satz-6-1"></span>

Sei $\boldsymbol{F}$ stetig differenzierbar in $B_R(\boldsymbol{x}_0)\subset\mathbb{R}^3$, $\boldsymbol{x}_0=(x_0,y_0,z_0)$, mit $\operatorname{rot}\boldsymbol{F}=0$. Dann ist

<span class="anker" id="gl-6-1"></span>
$$\varphi(x,y,z)=\int_{x_0}^xF_1(t,y_0,z_0)\,\mathrm{d} t+\int_{y_0}^yF_2(x,t,z_0)\,\mathrm{d} t+\int_{z_0}^zF_3(x,y,t)\,\mathrm{d} t \tag{6.1}$$

ein Skalarpotential von $\boldsymbol{F}$ in $B_R(\boldsymbol{x}_0)$.
:::

:::beweis Potential längs der Achsen
Der Weg bleibt in der Kugel, denn jeder Zwischenpunkt liegt höchstens so weit von $\boldsymbol{x}_0$ entfernt wie der Endpunkt. Ableiten: $\partial_z\varphi=F_3(x,y,z)$ nach dem Hauptsatz. Für $\partial_y$ zieht man die Ableitung unter das dritte Integral und benutzt $\partial_yF_3=\partial_zF_2$:

$$\partial_y\varphi=F_2(x,y,z_0)+\int_{z_0}^z\partial_tF_2(x,y,t)\,\mathrm{d} t=F_2(x,y,z).$$

Genauso gibt $\partial_x$ mit $\partial_xF_2=\partial_yF_1$ und $\partial_xF_3=\partial_zF_1$ die Summe $F_1(x,y_0,z_0)+\bigl[F_1(x,y,z_0)-F_1(x,y_0,z_0)\bigr]+\bigl[F_1(x,y,z)-F_1(x,y,z_0)\bigr]=F_1(x,y,z)$.
:::

**Beispiel.** $\boldsymbol{F}(x,y,z)=(2xy,\;x^2+\cos z,\;-y\sin z+3z^2)$ hat $\operatorname{rot}\boldsymbol{F}=0$ auf $\mathbb{R}^3$. Mit $\boldsymbol{x}_0=0$ fällt das erste Integral weg, $F_1(t,0,0)=0$. Es bleibt

$$\varphi=\int_0^y(x^2+1)\,\mathrm{d} t+\int_0^z(-y\sin t+3t^2)\,\mathrm{d} t=x^2y+y+y\cos z-y+z^3=x^2y+y\cos z+z^3.$$

⁠**Kontrolle:** Ableiten gibt $\nabla\varphi=\boldsymbol{F}$. Längs jeder Kurve von $0$ nach $(1,2,\pi)$ ist das Integral $\varphi(1,2,\pi)=\pi^3$, wie krumm sie auch läuft.

**Wie eindeutig sind Potentiale?** Auf einem Gebiet sind Skalarpotentiale bis auf eine Konstante bestimmt:

$$\nabla g=\nabla h\iff\nabla(g-h)=0\iff g-h=\text{konst}.$$

Das folgt aus [(4.1)](wann-nur-start-und-ziel-zahlen.html#gl-4-1), denn $g-h$ ändert sich längs keiner Kurve. Der Zusammenhang ist nötig: Auf zwei getrennten Kreisscheiben darf die Konstante auf jeder Scheibe anders sein.

Zu einem Vektorpotential darf man jedes stetig differenzierbare Gradientenfeld addieren, denn $\operatorname{rot}\nabla=0$:

<span class="anker" id="gl-6-2"></span>
$$\boldsymbol{F}=\nabla\times\boldsymbol{A}=\nabla\times(\boldsymbol{A}+\nabla\varphi). \tag{6.2}$$

In der Physik heißt das __Eichfreiheit__. Oft ist die __Coulomb-Eichung__ $\operatorname{div}\boldsymbol{A}=0$ günstig. Ist $\boldsymbol{A}'$ ein Vektorpotential von $\boldsymbol{F}$, erreicht man sie durch $\boldsymbol{A}=\boldsymbol{A}'+\nabla\varphi$ mit $\Delta\varphi=-\operatorname{div}\boldsymbol{A}'$. Voraussetzung ist, dass diese __Poisson-Gleichung__ für $\varphi$ lösbar ist. **Beispiel:** $\boldsymbol{A}'=(0,\,2x+y,\,0)$ hat $\operatorname{rot}\boldsymbol{A}'=(0,0,2)$ und $\operatorname{div}\boldsymbol{A}'=1$. Mit $\varphi=-y^2/2$ ist $\Delta\varphi=-1$, und $\boldsymbol{A}=(0,2x,0)$ hat dieselbe Rotation und $\operatorname{div}\boldsymbol{A}=0$.

:::frage Darf ich [(6.1)](#gl-6-1) benutzen, ohne $\operatorname{rot}\boldsymbol{F}$ zu prüfen?
Nein. Die Formel liefert immer eine Funktion, aber nur bei $\operatorname{rot}\boldsymbol{F}=0$ ein Potential. Also erst $\operatorname{rot}\boldsymbol{F}$ prüfen oder am Ende die Probe $\nabla\varphi=\boldsymbol{F}$ machen.
:::

:::aufgabe Aufgabe 6 ★★ Hässliche Kurve, kurze Rechnung
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Zeige $\operatorname{rot}\boldsymbol{F}=0$ für $\boldsymbol{F}(x,y,z)=(yz+2x,\;xz+\mathrm{e}^y,\;xy)$ und bestimme mit [(6.1)](#gl-6-1) ein Potential.

</li>

<li>

Berechne $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ für $\gamma(t)=(\cos(\pi t)+t,\;t^2,\;\sin(\pi t/2))$, $0\le t\le1$.

</li>

<li>

Ist das Kurvenintegral von $\boldsymbol K(x,y,z)=(-y,0,0)$ wegunabhängig? Berechne es über den Einheitskreis in der Ebene $z=0$.

</li>

</ol>

:::loesung
(a) $\operatorname{rot}\boldsymbol{F}=(x-x,\,y-y,\,z-z)=0$. Mit Startpunkt $0$: $\int_0^x2t\,\mathrm{d} t=x^2$, $\int_0^y\mathrm{e}^t\,\mathrm{d} t=\mathrm{e}^y-1$, $\int_0^zxy\,\mathrm{d} t=xyz$. Also $\varphi=x^2+\mathrm{e}^y-1+xyz$. (b) $\gamma(0)=(1,0,0)$, $\gamma(1)=(0,1,1)$. Das Integral ist $\varphi(0,1,1)-\varphi(1,0,0)=(\mathrm{e}-1)-1=\mathrm{e}-2$. (c) $\operatorname{rot}\boldsymbol K=(0,0,1)\neq0$, also nicht wegunabhängig. Mit $(\cos t,\sin t,0)$ ist der Integrand $\sin^2t$, das Integral ist $\pi$.
:::
:::

:::aufgabe Aufgabe 7 ★★★ Vektorpotential längs der Achsen
<span class="anker" id="aufg-7"></span>

Sei $\boldsymbol{F}$ stetig differenzierbar auf $\mathbb{R}^3$ mit $\operatorname{div}\boldsymbol{F}=0$ und $(x_0,y_0,z_0)$ ein Punkt.

<ol class="al">

<li>

Zeige $\operatorname{rot}\boldsymbol{A}=\boldsymbol{F}$ für $A_3=0$, $A_2=-\int_{z_0}^zF_1(x,y,t)\,\mathrm{d} t$ und $A_1=\int_{z_0}^zF_2(x,y,t)\,\mathrm{d} t-\int_{y_0}^yF_3(x,t,z_0)\,\mathrm{d} t$.

</li>

<li>

Berechne $\boldsymbol{A}$ für $\boldsymbol{F}=(z,x,y)$ mit dem Startpunkt $0$.

</li>

</ol>

:::loesung
(a) Erste Komponente: $-\partial_zA_2=F_1(x,y,z)$. Zweite: $\partial_zA_1=F_2(x,y,z)$, das zweite Integral hängt nicht von $z$ ab. Dritte: Mit $\operatorname{div}\boldsymbol{F}=0$ gilt

$$\partial_xA_2-\partial_yA_1=-\int_{z_0}^z(\partial_xF_1+\partial_yF_2)(x,y,t)\,\mathrm{d} t+F_3(x,y,z_0)=\int_{z_0}^z\partial_tF_3\,\mathrm{d} t+F_3(x,y,z_0)=F_3(x,y,z).$$

(b) $A_1=\int_0^zx\,\mathrm{d} t-\int_0^yt\,\mathrm{d} t=xz-\frac{y^2}{2}$, $A_2=-\int_0^zt\,\mathrm{d} t=-\frac{z^2}{2}$, $A_3=0$. Probe: $\operatorname{rot}\boldsymbol{A}=(z,x,y)$.
:::
:::
