---
title: Stage 4: The field strength
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Charge, Field and Potential
order: 1110600
summary: Coulomb's law gives the force but does not say how it gets across empty space.
tags: test charge, electric field strength
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Coulomb's law gives the force but does not say how it gets across empty space. The concept of the field answers this and separates cause from effect.
:::

**The idea.** Instead of “B pulls A across 3 cm”, the process is split in two. First: charge B changes the space around it; it produces a field. Second: charge A feels the field at its own location and experiences a force there. Why charges produce fields cannot be traced back to anything simpler; it is a fundamental law. But the picture solves three problems. **Cause and effect are separated:** The field depends only on the charges producing it and holds for any charge brought into it. **Many charges become manageable:** Their fields are added once, and after that you calculate with one vector per location. **The effect takes time:** If B is moved, the force on A changes only when the change in the field arrives there at the speed of light. Over 3 cm this takes 100 ps, from the Sun to the Earth 8.3 minutes. In the meantime, the change resides in the field, so the field is more than a computational aid.

:::analogie
The Earth is surrounded by a gravitational field: at every location, the force $\vec F=m\,\vec g$ acts on every mass. The field $\vec g$ is force per mass; the electric field is force per charge. The picture stops working in two places: masses always attract, and a gravitational field cannot be shielded.
:::

:::definition Definition 4.1 (Electric field strength)
<span class="anker" id="satz-4-1"></span>

If a small __test charge__ $Q$ is brought to a location and the force $\vec F$ on it is measured, the __electric field strength__ there is

<span class="anker" id="gl-4-1"></span>
$$\vec E:=\lim_{Q\to0}\frac{\vec F}{Q},\qquad\text{hence}\quad\vec F=Q\cdot\vec E. \tag{4.1}$$

The direction of $\vec E$ is the direction of the force on a positive test charge. The electric field assigns such a vector to every location.
:::

⁠**How to read it:** The unit is $[E]=\mathrm{N/C}=\mathrm{m\,kg\,A^{-1}\,s^{-3}}=\mathrm{V/m}$, because $\mathrm V=\mathrm{J/C}=\mathrm{N\,m/C}$. On a negative charge, the force acts opposite to $\vec E$. Typical values: in a current-carrying conductor 0.1 V/m, in the atmosphere in clear weather 100 to 200 V/m, at the surface of a broadcast antenna 1 to 1000 V/m, at a high-voltage line $10^6$ V/m, in a capacitor (a component made of two plates, [Part 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) $10^6$ to $10^8$ V/m. At $3\cdot10^6$ V/m air breaks down and a spark forms. **Validity:** The limit $Q\to0$ is needed because a large test charge displaces the charges producing the field, such as the free electrons of a metal plate. But what is to be measured is the field without the test charge.

:::satz Theorem 4.2 (Field of point charges)
<span class="anker" id="satz-4-2"></span>

A point charge $Q_0$ produces at the distance $r$ the field

<span class="anker" id="gl-4-2"></span>
$$\vec E=k\,\frac{Q_0}{r^2}\cdot\frac{\vec r}{r},\qquad E=k\,\frac{|Q_0|}{r^2}, \tag{4.2}$$

where $\vec r$ points from the charge to the location. Several charges together produce the sum of their fields: $\vec E=\sum_i\vec E_i$.
:::

:::herleitung Field of a point charge
By [(3.2)](die-kraft-zwischen-ladungen.html#gl-3-2), a test charge $Q$ experiences the force $\vec F=k\,Q\,Q_0/r^2\cdot\vec r/r$. Dividing by $Q$ removes $Q$; the result depends only on $Q_0$ and the location. The sum rule follows from the superposition of forces.
:::

:::abbildung et1/k1feldpfeile 5
Field vectors around a positive and a negative point charge. The field points away from the positive charge and toward the negative one. The arrow length is proportional to $1/r^2$.
:::

::::beispiel
Sphere B ($-20$ nC) produces at the location of sphere A the field $E=k\cdot20\,\mathrm{nC}/(3\,\mathrm{cm})^2=2.0\cdot10^5$ V/m, which points toward B. The force on A is $F=10\,\mathrm{nC}\cdot2.0\cdot10^5\,\mathrm{V/m}=2.0$ mN as in Stage [3](die-kraft-zwischen-ladungen.html#stufe-3). Conversely, A produces only $1.0\cdot10^5$ V/m at the location of B, but meets twice the charge there: again 2.0 mN.
::::

⁠**In short:** the force on a charge is its charge times the field at its location.

⁠**Limiting cases:** For $r\to\infty$, $E\to0$. For $r\to0$, $E$ would grow without bound; this shows the limit of the point-charge model.

:::frage Does a charge also feel its own field?
$\vec F=Q\vec E$ contains only the field of the *other* charges. A charge at rest exerts no force on itself.
:::

:::aufgabe Exercise 4 ★★ Two charges, one field-free point
<span class="anker" id="aufg-4"></span>

On the $x$-axis, $Q_1=+4$ nC is at $x=0$ and $Q_2=+1$ nC at $x=6$ cm.

<ol class="al">

<li>

Calculate the magnitude and direction of the field at $x=3$ cm. What force does an electron experience there?

</li>

<li>

Where between the charges is $E=0$?

</li>

<li>

Limiting case: Where does this point move for $Q_2\to0$? Does this fit the field of a single charge?

</li>

</ol>

:::loesung
(a) $E_1=k\cdot4\,\mathrm{nC}/(3\,\mathrm{cm})^2=40.0$ kV/m to the right, $E_2=k\cdot1\,\mathrm{nC}/(3\,\mathrm{cm})^2=9.99$ kV/m to the left, together $E=30.0$ kV/m to the right. Electron: $F=e\,E=4.8\cdot10^{-15}$ N to the left.

(b) $E=0$ requires $Q_1/x^2=Q_2/(a-x)^2$ with $a=6$ cm. From this $2/x=1/(a-x)$, so $x=\frac23a=4$ cm. (c) In general, $x=a/(1+\sqrt{Q_2/Q_1})$. For $Q_2\to0$, $x\to a$: the point moves to the location of $Q_2$ and vanishes: a single charge has no field-free point.
:::
:::
