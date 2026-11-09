---
title: Stage 6: Work in the field
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Charge, Field and Potential
order: 1110800
summary: When a charge moves in a field, the field force does work.
tags: curl-free, electrostatic
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
When a charge moves in a field, the field force does work. This stage calculates it and shows the property on which everything else rests: the work does not depend on the path.
:::

**The idea.** A charge in a field behaves like the backpack from Stage [1](groen-kraft-und-arbeit.html#stufe-1); the force is now $Q\vec E$. If a positive charge moves in the direction of the field, the field gives energy to it. If it moves against the field, someone else must supply the work, and the energy goes into the field. Across the field, nothing happens.

:::satz Theorem 6.1 (Work in the electric field)
<span class="anker" id="satz-6-1"></span>

If a charge $Q$ goes from $P_1$ to $P_2$, the field does on it the work

<span class="anker" id="gl-6-1"></span>
$$W_{12}=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s,\qquad\text{in a uniform field}\quad W_{12}=Q\,E\,s\cos\alpha. \tag{6.1}$$

In the field of charges at rest, $W_{12}$ depends only on $P_1$ and $P_2$, not on the path. Equivalently, the integral over any closed path is zero; the field is __curl-free__:

<span class="anker" id="gl-6-2"></span>
$$\oint_L\vec E\cdot\mathrm{d}\vec s=0. \tag{6.2}$$
:::

⁠**How to read it:** $Q$ is the moving charge with its sign, $s$ the length of a straight path at the angle $\alpha$ to $\vec E$. The circle in the integral means that the path $L$ ends where it began. $W_{12}>0$ means that the field gives energy to the charge; the energy is *released*. $W_{12}<0$ means that $W_\text{ext}=-W_{12}$ must be supplied from outside, provided the charge does not speed up or slow down in the process. At 1 nC and a few volts, this is nanojoules. **Validity:** [(6.2)](#gl-6-2) requires charges at rest and no changing magnetic field (Stage [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10)). Such a field is called __electrostatic__.

:::herleitung Why the work does not depend on the path
⁠**One point charge.** Let $Q$ move in the field of $Q_0$ from $r_1$ to $r_2$. The path is split into pieces along the radius and across it. Across the radius, the field is perpendicular to the path, so only the change in distance counts:

$$W_{12}=Q\int_{r_1}^{r_2}k\,\frac{Q_0}{r^2}\,\mathrm{d} r=k\,Q\,Q_0\Bigl(\frac{1}{r_1}-\frac{1}{r_2}\Bigr).$$

⁠**Arbitrary charges at rest.** Every such field is a sum of point-charge fields, and the work is the sum of the individual works.

⁠**Closed path.** If path $a$ leads from $P_1$ to $P_2$ and path $b$ back, the return path read in the opposite direction changes sign: $\oint\vec E\cdot\mathrm{d}\vec s=\int_a\vec E\cdot\mathrm{d}\vec s-\int_{b,\,P_1\to P_2}\vec E\cdot\mathrm{d}\vec s=0$, because both paths give the same value.
:::

:::abbildung et1/k1feldarbeit 7
Detail of the pair of plates, to scale. A test charge $+1$ nC goes around the triangle. From 1 to 2 it gains 9 nJ. From 2 to 3 it moves across the field: no work. From 3 to 1 it loses 9 nJ. The round trip gives zero.
:::

::::beispiel
In Fig. [7](#abb-7), $F=Q\,E=3$ µ N in the $x$-direction and $W_{12}=10^{-9}\,\mathrm{C}\cdot3000\,\mathrm{V/m}\cdot3\,\mathrm{mm}=9$ nJ. Directly from 1 to 3 the path is 5 mm long, with $\cos\alpha=0.6$: again 9 nJ. In the field of sphere A ($Q_0=+10$ nC), $+1$ nC gains from 3 cm to 6 cm the energy $k\cdot1\,\mathrm{nC}\cdot10\,\mathrm{nC}\cdot(1/r_1-1/r_2)=1.5$ µ J.
::::

⁠**Limiting cases:** For $\alpha=90^\circ$ and for $P_2=P_1$, $W=0$. For a negative charge the sign reverses: an electron gains energy when it moves against $\vec E$. For $r_2\to\infty$, $W_{12}=kQQ_0/r_1$ remains finite.

:::frage There and back always gives zero anyway. Why is this a special statement?
On the same path there and back, that is true for every force field. [(6.2)](#gl-6-2) is stronger: it also holds when the return path is different. Otherwise a charge could be sent around in a circle, gaining energy on each round trip.
:::

:::aufgabe Exercise 6 ★★ Paths in the field
<span class="anker" id="aufg-6"></span>

In the uniform field $E=3$ kV/m in the $x$-direction, $Q=+2$ nC moves from $P_1=(0;\,0)$ to $P_2=(2\,\mathrm{mm};\,1.5\,\mathrm{mm})$.

<ol class="al">

<li>

Calculate $W_{12}$ on the straight path.

</li>

<li>

Calculate $W_{12}$ on the detour first in the $y$-direction, then in the $x$-direction.

</li>

<li>

What changes for $Q=-2$ nC?

</li>

</ol>

:::loesung
(a) Length $s=\sqrt{2^2+1.5^2}\,\mathrm{mm}=2.5$ mm, $\cos\alpha=0.8$: $W_{12}=2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2.5\,\mathrm{mm}\cdot0.8=12$ nJ. (b) In the $y$-direction the path is perpendicular to $\vec E$: 0. In the $x$-direction: $2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2\,\mathrm{mm}=12$ nJ. (c) $W_{12}=-12$ nJ; 12 nJ must be supplied from outside.
:::
:::
