---
title: Stage 2: Capacitance
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1130300
summary: How much charge does a given voltage hold on the plates?
tags: 
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
How much charge does a given voltage hold on the plates? The answer is a single number for each component.
:::

**The idea.** If you double the charge on both plates, each charge contributes its field twice. By the superposition from [Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), the field doubles at every location, and its shape stays the same (Fig. [2](#abb-2) left). The voltage is the integral of the field from plate to plate, so it doubles too. $Q$ and $U$ are therefore proportional. Their ratio does not depend on how much charge happens to be there, but only on shape, separation and material.

:::definition Definition 2.1 (Capacitance)
<span class="anker" id="satz-2-1"></span>

The capacitance of a capacitor is the ratio of charge to voltage:

<span class="anker" id="gl-2-1"></span>
$$C=\frac{Q}{U},\qquad Q=C\,U,\qquad[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F\ \text{(farad)}. \tag{2.1}$$
:::

⁠**How to read it:** $Q$ is the charge of the positive plate in C (coulombs), $U$ the voltage between the plates in V, $C$ the capacitance in F. At 1 F, one volt holds one coulomb. That is a great deal. Usual values are in the fF, pF, nF and µF ranges; electrolytic capacitors reach into the mF range. Do not confuse the symbols: italic $C$ is the capacitance, upright C is the coulomb. **Validity:** [(2.1)](#gl-2-1) assumes that the material between the plates does not change with the field. Ceramics with very large $\varepsilon_\mathrm{r}$ (Stage [4](plattenkondensator-und-dielektrikum.html#stufe-4)) noticeably lose capacitance at high voltage.

:::abbildung et1/k3qu 2
Left: Twice the charge gives field lines twice as dense and thus twice the voltage. Right: The charge grows in proportion to the voltage; the slope of the line is the capacitance. The dots belong to 9 V.
:::

**Example.** The pair of plates has $C=29.5$ pF (Stage [4](plattenkondensator-und-dielektrikum.html#stufe-4)). At 9 V it carries $Q=29.5\,\mathrm{pF}\cdot9\,\mathrm{V}=266$ pC, which is $1.66\cdot10^{9}$ electrons. A 1 mm thick copper plate of this area contains $8.5\cdot10^{23}$ free electrons. So only one in $5\cdot10^{14}$ moves, and these sit on the inner side of the plate. The metal stays practically unchanged. The capacitor of the RC circuit carries $Q=900\,\mu\text{C}$ at 9 V, 3.4 million times more.

⁠**Limiting case:** For $U=0$, $Q=0$: without voltage nothing is separated. For the same charge, the smaller capacitor shows the larger voltage.

:::frage Capacitance sounds like holding capacity. Does a capacitor ever get full?
Not in the sense of a bucket. More voltage always brings more charge, and $C$ stays the same. The limit is set by the dielectric: above a certain field strength it breaks down. In this chapter, full only means: the voltage has reached that of the source.
:::

:::aufgabe Exercise 2 ★ Charge and voltage
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

A 470 nF capacitor is connected to 12 V. How large is its charge?

</li>

<li>

At what voltage does it carry 1 µC?

</li>

<li>

The voltage is halved. What happens to $Q$ and to $C$?

</li>

<li>

Two capacitors of 10 µF and 1 µF each carry 50 µC. What voltages are across them?

</li>

</ol>

:::loesung
(a) $Q=470\,\mathrm{nF}\cdot12\,\mathrm{V}=5.64\,\mu\text{C}$.

(b) $U=Q/C=1\,\mu\text{C}/470\,\mathrm{nF}=2.13$ V.

(c) $Q$ halves to 2.82 µC. $C$ stays the same, because it depends only on the component.

(d) $U=Q/C$: 5 V across the 10 µF capacitor, 50 V across the 1 µF capacitor. The same charge produces the larger voltage on the smaller one.
:::
:::
