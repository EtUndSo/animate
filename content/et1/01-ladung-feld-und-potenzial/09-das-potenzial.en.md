---
title: Stage 7: The potential
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Charge, Field and Potential
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Chapter 1: Charge, Field and Potential
order: 1110900
summary: If the work depends only on start and end, a single number per location is enough to calculate it.
tags: equipotential surfaces
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
If the work depends only on start and end, a single number per location is enough to calculate it. This number is the potential.
:::

**The idea.** Choose a reference point and write at each location the work per charge that the field gives up on the way from there to the reference point. Dividing by the charge makes the number a property of the location. The work between two locations is then a difference of two such numbers.

:::analogie
The potential is the height of a landscape, the field its slope, a positive charge a ball rolling downhill. The picture stops working for negative charges: they roll uphill in the same landscape.
:::

:::definition Definition 7.1 (Potential)
<span class="anker" id="satz-7-1"></span>

In an electrostatic field with the reference point $P_0$, the potential of a point $P$ is

<span class="anker" id="gl-7-1"></span>
$$\varphi(P)=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s=-\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s,\qquad[\varphi]=\frac{\mathrm J}{\mathrm C}=\mathrm V. \tag{7.1}$$

A charge $Q$ there has the potential energy $W_\mathrm{pot}=Q\,\varphi(P)$.
:::

:::satz Theorem 7.2 (Work as a potential difference, two profiles)
<span class="anker" id="satz-7-2"></span>

<span class="anker" id="gl-7-2"></span>
$$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr). \tag{7.2}$$

In the uniform field in the $x$-direction and in the field of a point charge $Q_0$ (reference point at infinity),

<span class="anker" id="gl-7-3"></span>
$$\varphi(x)=\varphi(0)-E\,x,\qquad\varphi(r)=k\,\frac{Q_0}{r}. \tag{7.3}$$
:::

:::herleitung Work as a potential difference
Because the work does not depend on the path, one may go from $P_1$ via $P_0$ to $P_2$:

$$\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\int_{P_1}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_2}\vec E\cdot\mathrm{d}\vec s=\varphi(P_1)-\varphi(P_2).$$

Without path independence, $\varphi$ would not even be unique. The profiles [(7.3)](#gl-7-3) follow from [(7.1)](#gl-7-1) with constant $E$ and from the derivation in Stage [6](arbeit-im-feld.html#stufe-6) with $r_2\to\infty$.
:::

⁠**How to read it:** $\varphi$ is a number per location, not a vector. In the direction of $\vec E$, $\varphi$ falls; the field strength is the slope of the potential: $E_x=-\mathrm{d}\varphi/\mathrm{d} x$. If $P_0$ is moved elsewhere, all potentials change by the same amount. **Validity:** The potential presupposes an electrostatic field.

**Equipotential surfaces.** Locations of equal potential form __equipotential surfaces__. A charge can be moved on them without work. It follows that field lines are perpendicular to them; otherwise there would be work along the surface. In the pair of plates, they are planes parallel to the plates; around a point charge, spheres. Because $\vec E=0$, a metal body at rest has the same potential everywhere.

:::abbildung et1/k1potenzial 8
Left: the pair of plates with the reference point on plate B. The dashed lines are equipotential surfaces in cross section, 3 V apart. Right: the potential falls along $x$ from 9 V to 0 V; its slope $-3$ V/mm is $-E$.
:::

::::beispiel
With $\varphi=0$ on B, A is at 9 V, and $\varphi(x)=9\,\mathrm{V}-3\,\mathrm{kV/m}\cdot x$: 6 V at 1 mm, 3 V at 2 mm. Sphere A ($+10$ nC) has the potential 3.0 kV at a distance of 3 cm and 1.5 kV at a distance of 6 cm. The difference times 1 nC gives the 1.5 µ J from Stage [6](arbeit-im-feld.html#stufe-6).
::::

⁠**In short:** the potential is the energy per charge at a location, measured from the reference point.

⁠**Limiting cases:** For $r\to\infty$, $\varphi\to0$; that is the chosen reference point. For $E=0$, $\varphi$ is constant, but it need not be zero.

:::frage If $\varphi=0$, there is no field there either, right?
No. The field depends on the slope, not on the value. Plate B has $\varphi=0$, and directly in front of it the full field 3 kV/m is present. Conversely, inside a charged metal sphere $E=0$, but its potential is not zero.
:::

:::aufgabe Exercise 7 ★★ Separating potential and field
<span class="anker" id="aufg-7"></span>

On the $x$-axis, $Q_1=+4$ nC is at $x=0$ and $Q_2=-1$ nC at $x=6$ cm; the reference point is at infinity.

<ol class="al">

<li>

Calculate the potential at $x=3$ cm. Why do you add here without directions?

</li>

<li>

Where between the charges is $\varphi=0$? How large is $E$ there?

</li>

</ol>

:::loesung
(a) Potentials are numbers; they add with their signs: $\varphi=k\,(4\,\mathrm{nC}-1\,\mathrm{nC})/3\,\mathrm{cm}=899$ V. (b) $4/x-1/(6-x)=0$ with $x$ in cm gives $x=4.8$ cm. There, both fields point to the right: $E=k\cdot4\,\mathrm{nC}/(4.8\,\mathrm{cm})^2+k\cdot1\,\mathrm{nC}/(1.2\,\mathrm{cm})^2=15.6\,\mathrm{kV/m}+62.4\,\mathrm{kV/m}=78.0$ kV/m. So $\varphi=0$ does not mean $E=0$.
:::
:::
