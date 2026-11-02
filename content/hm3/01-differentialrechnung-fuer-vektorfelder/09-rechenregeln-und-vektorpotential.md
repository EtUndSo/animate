---
title: Stufe 8: Rechenregeln und Vektorpotential
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110900
summary: Mit nabla rechnet man fast wie mit einem Vektor.
tags: Spatprodukt, Graßmann-Identität, Rotationsfeld, Wirbelfeld, Vektorpotential, divergenzfrei, Eichfreiheit, Coulomb-Eichung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Mit $\nabla$ rechnet man fast wie mit einem Vektor. Diese Stufe sagt, wo die Grenze liegt, gibt die Produktregeln, die Formeln für zwei Operatoren hintereinander, und stellt die Frage nach Rotationsfeldern.
:::

**Die Idee.** $\nabla$ ist kein Vektor, sondern ein Ableitungsbefehl für alles, was rechts von ihm steht. Deshalb ist $\nabla\cdot\boldsymbol{F}$ eine Funktion, $\boldsymbol{F}\cdot\nabla$ aber ein Operator, der auf etwas wartet. Jede Regel entsteht in zwei Schritten: erst die Produktregel, sodass jeder Faktor einmal abgeleitet wird, dann eine Vektoridentität.

:::satz Satz 8.1 (Produktregeln mit Skalar)
<span class="anker" id="satz-8-1"></span>

Für eine differenzierbare Funktion $\varphi$ und ein differenzierbares Feld $\boldsymbol{E}$ auf $\mathcal U\subset\mathbb{R}^3$ gilt

<span class="anker" id="gl-8-1"></span>
$$\operatorname{div}(\varphi\boldsymbol{E})=\nabla\varphi\cdot\boldsymbol{E}+\varphi\,\operatorname{div}\boldsymbol{E},\qquad\operatorname{rot}(\varphi\boldsymbol{E})=\nabla\varphi\times\boldsymbol{E}+\varphi\,\operatorname{rot}\boldsymbol{E}. \tag{8.1}$$

Die erste Formel gilt in jeder Dimension. In 2D ersetzt man das Kreuzprodukt durch das äußere Produkt $a_1b_2-a_2b_1$: $\operatorname{rot}(\varphi\boldsymbol{E})=\bigl(\frac{\partial\varphi}{\partial x_1}E_2-\frac{\partial\varphi}{\partial x_2}E_1\bigr)+\varphi\,\operatorname{rot}\boldsymbol{E}$.
:::

:::beweis Rotation eines Produkts
Mit [(6.3)](rotation.html#gl-6-3): $(\operatorname{rot}(\varphi\boldsymbol{E}))_i=\sum_{j,k}\varepsilon_{ijk}\,\partial_{x_j}(\varphi E_k)=\sum_{j,k}\varepsilon_{ijk}(\partial_{x_j}\varphi)E_k+\varphi\sum_{j,k}\varepsilon_{ijk}\,\partial_{x_j}E_k$. Die erste Summe ist $(\nabla\varphi\times\boldsymbol{E})_i$, die zweite $(\operatorname{rot}\boldsymbol{E})_i$.
:::

**Zwei Vektoridentitäten.** Das __Spatprodukt__ und die __Graßmann-Identität__ lauten für $\boldsymbol a,\boldsymbol b,\boldsymbol c\in\mathbb{R}^3$:

<span class="anker" id="gl-8-2"></span>
$$\boldsymbol a\cdot(\boldsymbol b\times\boldsymbol c)=\det(\boldsymbol a|\boldsymbol b|\boldsymbol c),\qquad\boldsymbol a\times(\boldsymbol b\times\boldsymbol c)=(\boldsymbol a\cdot\boldsymbol c)\,\boldsymbol b-(\boldsymbol a\cdot\boldsymbol b)\,\boldsymbol c. \tag{8.2}$$

Das Spatprodukt bleibt beim zyklischen Vertauschen gleich. Die Graßmann-Identität ist linear in $\boldsymbol a,\boldsymbol b,\boldsymbol c$, es genügt also, sie für Einheitsvektoren der Achsen zu prüfen. In Indizes lautet sie, mit $\delta_{il}=1$ für $i=l$ und sonst 0,

<span class="anker" id="gl-8-3"></span>
$$\sum_{k=1}^3\varepsilon_{ijk}\,\varepsilon_{klm}=\delta_{il}\,\delta_{jm}-\delta_{im}\,\delta_{jl}. \tag{8.3}$$

:::satz Satz 8.2 (Produktregeln mit Kreuzprodukt)
<span class="anker" id="satz-8-2"></span>

Für differenzierbare Felder $\boldsymbol{E}$, $\boldsymbol B$ auf $\mathcal U\subset\mathbb{R}^3$ gilt

<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
$$\begin{aligned} \operatorname{div}(\boldsymbol{E}\times\boldsymbol B)&=\boldsymbol B\cdot\operatorname{rot}\boldsymbol{E}-\boldsymbol{E}\cdot\operatorname{rot}\boldsymbol B,\\ \operatorname{rot}(\boldsymbol{E}\times\boldsymbol B)&=\boldsymbol{E}\,\operatorname{div}\boldsymbol B-\boldsymbol B\,\operatorname{div}\boldsymbol{E}+(\boldsymbol B\cdot\nabla)\boldsymbol{E}-(\boldsymbol{E}\cdot\nabla)\boldsymbol B, \end{aligned} \tag{8.4|8.5}$$

dabei ist $(\boldsymbol{E}\cdot\nabla)\boldsymbol B=\sum_{j=1}^3E_j\,\dfrac{\partial\boldsymbol B}{\partial x_j}$ mit $\dfrac{\partial\boldsymbol B}{\partial x_j}=\Bigl(\dfrac{\partial B_1}{\partial x_j},\dfrac{\partial B_2}{\partial x_j},\dfrac{\partial B_3}{\partial x_j}\Bigr)^T$.
:::

⁠**So liest man das:** $(\boldsymbol{E}\cdot\nabla)\boldsymbol B$ ist die Ableitung von $\boldsymbol B$ in Richtung $\boldsymbol{E}$, komponentenweise. Das ist etwas anderes als $\boldsymbol{E}\,\operatorname{div}\boldsymbol B$, das Feld $\boldsymbol{E}$ mal die Zahl $\operatorname{div}\boldsymbol B$. Beide Formeln folgen aus den Darstellungen mit $\varepsilon_{ijk}$ und der Produktregel, die zweite braucht zusätzlich [(8.3)](#gl-8-3) (Aufgabe [10](#aufg-10)).

:::satz Satz 8.3 (Zwei Operatoren hintereinander)
<span class="anker" id="satz-8-3"></span>

Für ein zweimal stetig differenzierbares Feld $\boldsymbol{E}$ auf $\mathcal U\subset\mathbb{R}^3$ gilt

<span class="anker" id="gl-8-6"></span>
$$\operatorname{div}\operatorname{rot}\boldsymbol{E}=0,\qquad\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E}. \tag{8.6}$$
:::

:::beweis Antisymmetrie trifft Symmetrie
Mit [(6.3)](rotation.html#gl-6-3) ist $\operatorname{div}\operatorname{rot}\boldsymbol{E}=\sum_{i,j,k}\varepsilon_{ijk}\,\dfrac{\partial^2E_k}{\partial x_i\,\partial x_j}$. Für festes $k$ ist $\varepsilon_{ijk}$ schief in $i,j$, die zweite Ableitung nach Schwarz symmetrisch. In der Summe hebt sich der Summand mit $(i,j)$ gegen den mit $(j,i)$ weg.

Für die zweite Formel ist nach [(6.3)](rotation.html#gl-6-3) und [(8.3)](#gl-8-3)

$$(\operatorname{rot}\operatorname{rot}\boldsymbol{E})_i=\sum_{j,k,l,m}\varepsilon_{ijk}\,\varepsilon_{klm}\,\partial_{x_j}\partial_{x_l}E_m=\sum_j\partial_{x_j}\partial_{x_i}E_j-\sum_j\partial_{x_j}\partial_{x_j}E_i=\partial_{x_i}\operatorname{div}\boldsymbol{E}-\Delta E_i.$$

Kompakt ist das Graßmann mit $\boldsymbol a=\boldsymbol b=\nabla$, $\boldsymbol c=\boldsymbol{E}$, aber achtsam angewendet: $\nabla\times(\nabla\times\boldsymbol{E})=\nabla(\nabla\cdot\boldsymbol{E})-(\nabla\cdot\nabla)\boldsymbol{E}$. Das abgeleitete Feld steht immer an letzter Stelle.
:::

:::frage Warum darf ich in Vektorformeln nicht $\boldsymbol a=\nabla$ einsetzen?
Weil $\nabla$ alles rechts von ihm ableitet. Zyklisches Tauschen im Spatprodukt gäbe $\nabla\cdot(\boldsymbol{E}\times\boldsymbol B)=\boldsymbol B\cdot(\nabla\times\boldsymbol{E})$. Dann fehlte der zweite Summand von [(8.4)](#gl-8-4), denn $\boldsymbol B$ würde gar nicht mehr abgeleitet. Vektoridentitäten gelten für $\nabla$ nur, wenn die Produktregel jeden Faktor erreicht und das abgeleitete Feld hinten steht.
:::

:::abbildung hm3/k1operatoren 8
Zwei Operatoren hintereinander. Oben: Ein Gradient hat keine Rotation. Unten: Eine Rotation hat keine Divergenz. Beide Nullen stammen aus der Vertauschbarkeit zweiter Ableitungen.
:::

:::definition Definition 8.4 (Rotationsfeld und Vektorpotential)
<span class="anker" id="satz-8-4"></span>

Ein Vektorfeld $\boldsymbol B$ auf $\mathcal U\subset\mathbb{R}^3$ heißt __Rotationsfeld__ oder __Wirbelfeld__, wenn $\boldsymbol B=\operatorname{rot}\boldsymbol{A}$ für ein differenzierbares Feld $\boldsymbol{A}$ gilt. $\boldsymbol{A}$ heißt dann __Vektorpotential__ von $\boldsymbol B$.
:::

Nach [(8.6)](#gl-8-6) sind Rotationsfelder mit zweimal stetig differenzierbarem $\boldsymbol{A}$ __divergenzfrei__ (Abb. [8](#abb-8)). Wie beim Gradienten fragt man nach der Umkehrung: Reicht $\operatorname{div}\boldsymbol B=0$ für ein Vektorpotential? Im Allgemeinen nein, auch hier kommt es auf das Gebiet an.

**Eichfreiheit.** Potentiale sind nicht eindeutig. Zu einem Skalarpotential darf man eine Konstante addieren, zu einem Vektorpotential ein beliebiges Gradientenfeld, denn $\operatorname{rot}\nabla\psi=0$ ändert $\operatorname{rot}\boldsymbol{A}$ nicht. Diese __Eichfreiheit__ nutzt man, um $\boldsymbol{A}$ bequem zu wählen, etwa in der __Coulomb-Eichung__

<span class="anker" id="gl-8-7"></span>
$$\boldsymbol B=\nabla\times\boldsymbol{A}\quad\text{mit}\quad\operatorname{div}\boldsymbol{A}=0. \tag{8.7}$$

Ist $\operatorname{div}\boldsymbol{A}\neq0$ und $\psi$ eine Lösung der partiellen Differentialgleichung $\Delta\psi=\operatorname{div}\boldsymbol{A}$, dann ist $\boldsymbol{A}'=\boldsymbol{A}-\nabla\psi$ ein Vektorpotential von $\boldsymbol B$ in Coulomb-Eichung, denn $\operatorname{div}\boldsymbol{A}'=\operatorname{div}\boldsymbol{A}-\Delta\psi=0$. Damit vereinfacht sich [(8.6)](#gl-8-6) zu $\operatorname{rot}\boldsymbol B=\operatorname{rot}\operatorname{rot}\boldsymbol{A}'=-\Delta\boldsymbol{A}'$. **Beispiel:** $\boldsymbol B=(0,0,2)$ hat die Vektorpotentiale $(-y,x,0)$ und $(0,2x,0)$. Sie unterscheiden sich um $\nabla(-xy)$, und beide sind divergenzfrei.

:::aufgabe Aufgabe 10 ★★★ Produktregeln beweisen
<span class="anker" id="aufg-10"></span>

Beweise [(8.4)](#gl-8-4) und [(8.5)](#gl-8-5). Tipp: $(\boldsymbol{E}\times\boldsymbol B)_k=\sum_{l,m}\varepsilon_{klm}E_lB_m$. Für [(8.4)](#gl-8-4) ordne die Summe mit $\varepsilon_{ijk}=\varepsilon_{jki}$ um, für [(8.5)](#gl-8-5) benutze [(8.3)](#gl-8-3).

:::loesung
Erste Formel, mit Produktregel:

$$\operatorname{div}(\boldsymbol{E}\times\boldsymbol B)=\sum_{k,l,m}\varepsilon_{klm}\,\partial_{x_k}(E_lB_m)=\sum_{k,l,m}\varepsilon_{klm}(\partial_{x_k}E_l)B_m+\sum_{k,l,m}\varepsilon_{klm}E_l\,\partial_{x_k}B_m.$$

Wegen $\varepsilon_{klm}=\varepsilon_{mkl}$ ist die erste Summe $\sum_mB_m(\operatorname{rot}\boldsymbol{E})_m$. Wegen $\varepsilon_{klm}=-\varepsilon_{lkm}$ ist die zweite $-\sum_lE_l(\operatorname{rot}\boldsymbol B)_l$. Zweite Formel: $(\operatorname{rot}(\boldsymbol{E}\times\boldsymbol B))_i=\sum\varepsilon_{ijk}\varepsilon_{klm}\,\partial_{x_j}(E_lB_m)$. Mit [(8.3)](#gl-8-3) wird daraus

$$\sum_j\partial_{x_j}(E_iB_j)-\sum_j\partial_{x_j}(E_jB_i)=E_i\operatorname{div}\boldsymbol B+(\boldsymbol B\cdot\nabla)E_i-B_i\operatorname{div}\boldsymbol{E}-(\boldsymbol{E}\cdot\nabla)B_i.$$
:::
:::

:::aufgabe Aufgabe 11 ★★ Identitäten anwenden
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Zeige $\operatorname{rot}(f(r)\,\boldsymbol{x})=0$ auf $\mathbb{R}^3\setminus\{0\}$ für stetig differenzierbares $f$.

</li>

<li>

Zeige $\operatorname{div}(\nabla f\times\nabla g)=0$ für zweimal stetig differenzierbare $f,g$ auf $\mathbb{R}^3$.

</li>

<li>

Zeige $\Delta(\nabla f)=\nabla(\Delta f)$ für dreimal stetig differenzierbares $f$.

</li>

</ol>

:::loesung
(a) Nach [(8.1)](#gl-8-1) und [(4.3)](radiale-funktionen-und-felder.html#gl-4-3) ist $\operatorname{rot}(f(r)\boldsymbol{x})=f'(r)\,\hat{\boldsymbol{e}}_r\times\boldsymbol{x}+f(r)\,\operatorname{rot}\boldsymbol{x}=0$, denn $\hat{\boldsymbol{e}}_r$ und $\boldsymbol{x}$ sind parallel und $\operatorname{rot}\boldsymbol{x}=0$. (b) Nach [(8.4)](#gl-8-4) mit $\boldsymbol{E}=\nabla f$, $\boldsymbol B=\nabla g$ ist $\operatorname{div}(\nabla f\times\nabla g)=\nabla g\cdot\operatorname{rot}\nabla f-\nabla f\cdot\operatorname{rot}\nabla g=0$. (c) Komponente $k$: $\Delta\,\partial_{x_k}f=\sum_j\partial_{x_j}^2\partial_{x_k}f=\partial_{x_k}\sum_j\partial_{x_j}^2f=\partial_{x_k}\Delta f$ nach Schwarz. Alternativ aus [(8.6)](#gl-8-6) mit $\boldsymbol{E}=\nabla f$, denn $\operatorname{rot}\nabla f=0$.
:::
:::

:::aufgabe Aufgabe 12 ★★ Coulomb-Eichung
<span class="anker" id="aufg-12"></span>

Sei $\boldsymbol{A}=(x,\;x^3,\;0)$. Berechne $\boldsymbol B=\operatorname{rot}\boldsymbol{A}$ und $\operatorname{div}\boldsymbol{A}$. Finde ein $\psi$, das nur von $x$ abhängt, mit $\Delta\psi=\operatorname{div}\boldsymbol{A}$, bilde $\boldsymbol{A}'=\boldsymbol{A}-\nabla\psi$ und prüfe $\operatorname{rot}\boldsymbol{A}'=\boldsymbol B$, $\operatorname{div}\boldsymbol{A}'=0$ und $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}'$.

:::loesung
$\boldsymbol B=\operatorname{rot}\boldsymbol{A}=(0,\;0,\;3x^2)$ und $\operatorname{div}\boldsymbol{A}=1$. Aus $\psi''(x)=1$ folgt zum Beispiel $\psi=x^2/2$. Dann ist $\boldsymbol{A}'=(x,x^3,0)-(x,0,0)=(0,x^3,0)$. Es ist $\operatorname{rot}\boldsymbol{A}'=(0,0,3x^2)=\boldsymbol B$ und $\operatorname{div}\boldsymbol{A}'=0$. Weiter ist $\operatorname{rot}\boldsymbol B=(0,\;-6x,\;0)$ und $\Delta\boldsymbol{A}'=(0,6x,0)$, also $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}'$.
:::
:::
