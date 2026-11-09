---
title: Stage 3: The force between charges
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Charge, Field and Potential
order: 1110500
summary: Charged bodies exert forces on each other.
tags: electric constant, point charges, superposition
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Charged bodies exert forces on each other. This stage turns “they attract each other” into a law with numbers.
:::

**The idea.** Hang a charged sphere on a thread and place a second, oppositely charged sphere next to it (Fig. [4](#abb-4)). The attraction pulls the sphere out of the vertical, gravity pulls it back, and the deflection reveals the force: $\tan\alpha=F/(m\,g)$. Varying the charges and the distance shows that the force grows in proportion to each of the two charges and falls with the square of the distance. The law of gravitation [(1.2)](groen-kraft-und-arbeit.html#gl-1-2) has the same form, with charges instead of masses.

:::abbildung et1/k1pendel 4
Left: sphere A on a thread next to sphere B, forces to scale. Weight $m\,g=9.81$ mN, electric force $F=2.0$ mN and thread force $F_0=10.0$ mN cancel, $\alpha=11.5^\circ$. Right: Coulomb force in the reference model. Double the distance gives a quarter of the force.
:::

:::satz Theorem 3.1 (Coulomb's law)
<span class="anker" id="satz-3-1"></span>

Two point-like charges at rest at the distance $r$ exert forces of magnitude

<span class="anker" id="gl-3-1"></span>
$$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=8.99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}} \tag{3.1}$$

on each other. As a vector, the force on A, with $\vec r$ pointing from B to A, is

<span class="anker" id="gl-3-2"></span>
$$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}. \tag{3.2}$$
:::

⁠**How to read it:** $Q_\mathrm{A}$, $Q_\mathrm{B}$ are the charges in C, in [(3.2)](#gl-3-2) with their signs, and $r$ is the distance in m. The vector $\vec r/r$ has length 1 and gives only the direction. $\varepsilon_0=8.854\cdot10^{-12}$ A s/(V m) is called the __electric constant__. For like charges, $Q_\mathrm{A}Q_\mathrm{B}>0$ and $\vec F_\mathrm{A}$ points away from B: repulsion. For opposite charges, it points toward B: attraction. **Validity:** The bodies must be small compared with $r$ (__point charges__) and at rest. The law holds in vacuum; in air the force is only 0.06 % smaller. Several charges act independently, and their forces add as vectors (__superposition__).

:::herleitung From experiment to law
The law is a measurement result. Individually, the series of experiments give $F\sim Q_\mathrm{A}$, $F\sim Q_\mathrm{B}$, $F\sim1/r^2$ and $\vec F\parallel\vec r$, together $F\sim Q_\mathrm{A}Q_\mathrm{B}/r^2$, and the factor is $k$. If one assumes $F\sim1/r^{2\pm\delta}$, the limit on $\delta$ fell from 0.02 with Cavendish (18th century) via $5\cdot10^{-5}$ with Maxwell (19th century) to $10^{-13}$ (Bartlett and others, 1970) and $3\cdot10^{-16}$ (Williams and others, 1971).
:::

::::beispiel
In the reference model,

$$F=8.99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}\cdot\frac{10\cdot10^{-9}\,\mathrm{C}\cdot20\cdot10^{-9}\,\mathrm{C}}{(0.03\,\mathrm{m})^2}=2.0\,\mathrm{mN}.$$

The weight of sphere A is 9.81 mN, so $\tan\alpha=0.204$ and $\alpha=11.5^\circ$. This deflection is produced by the absence of one electron in $5\cdot10^{12}$. The gravitation between two 1 g spheres at the same distance is only $7.4\cdot10^{-14}$ N; it is smaller by a factor of $2.7\cdot10^{10}$ and can be dropped. Between two electrons, the electric force is even $4.2\cdot10^{42}$ times greater.
::::

⁠**Limiting cases:** For $r\to\infty$, $F\to0$. For $Q_\mathrm{A}=0$, $F=0$. Double the distance gives 0.5 mN, double the charge $Q_\mathrm{A}$ gives 4.0 mN.

:::frage Sphere B carries twice as much charge as sphere A. Does A therefore feel the larger force?
No, both feel the same 2.0 mN in opposite directions, because both charges enter [(3.1)](#gl-3-1) on an equal footing. What can differ is the effect: the lighter sphere is accelerated more strongly.
:::

:::aufgabe Exercise 3 ★★ Coulomb force
<span class="anker" id="aufg-3"></span>

Two small metal spheres carry $+2$ nC and $+5$ nC at a distance of 2 cm.

<ol class="al">

<li>

How large is the force, and where does it point on each sphere?

</li>

<li>

What results at three times the distance? Answer first without a calculator.

</li>

<li>

The equal-sized spheres briefly touch and are brought back to 2 cm. What force acts now? Why has it not stayed the same, even though the total charge has?

</li>

</ol>

:::loesung
(a) $F=k\cdot2\,\mathrm{nC}\cdot5\,\mathrm{nC}/(2\,\mathrm{cm})^2=225$ µ N. Like charges: each sphere is pushed away from the other. (b) Three times the distance gives one ninth: 25 µ N.

(c) Each sphere now carries $+3.5$ nC, so $F=k\,(3.5\,\mathrm{nC})^2/(2\,\mathrm{cm})^2=275$ µ N. The force depends on the product of the charges, not on their sum: $3.5\cdot3.5=12.25$ versus $2\cdot5=10$.
:::
:::
