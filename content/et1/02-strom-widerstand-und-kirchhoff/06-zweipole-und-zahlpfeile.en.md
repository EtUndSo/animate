---
title: Stage 5: Two-terminal elements and reference arrows
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Current, Resistance and Kirchhoff's Laws
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Chapter 2: Current, Resistance and Kirchhoff's Laws
order: 1120600
summary: From now on, what counts is no longer what happens inside the component, but what can be measured at its terminals.
tags: two-terminal element, characteristic curve, black box, network, linear two-terminal element, nonlinear two-terminal element, passive sign convention, active sign convention
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
From now on, what counts is no longer what happens inside the component, but what can be measured at its terminals. That requires a term for the component and an agreement about signs.
:::

**The idea.** For calculating, it is enough to know how a component responds to voltage with current. The inside may be unknown. Signs are fixed beforehand with arrows, because the true directions are often not known before the calculation. The result then says whether reality follows the arrow.

:::definition Definition 5.1 (Two-terminal element, black box, network)
<span class="anker" id="satz-5-1"></span>

A __two-terminal element__ is a component that can be fully described by the current and voltage between its two terminals. In the steady state (time-independent), that is its __characteristic curve__ $I=f(U)$. A __black box__ is a system whose outward behavior is known but whose construction is unknown or unimportant. A __network__ is an interconnection of two-terminal elements. If the characteristic curve is a straight line through the origin,

<span class="anker" id="gl-5-1"></span>
$$G=\frac IU=\text{const}\quad\text{or}\quad R=\frac UI=\text{const}. \tag{5.1}$$
:::

⁠**How to read it:** Such a __linear two-terminal element__ is the ohmic resistor (Fig. [4](das-ohmsche-gesetz-aus-feld-und-stoen.html#abb-4) right, each straight line one value). Batteries and voltage sources also belong to the building blocks of linear networks, but their characteristic curve does not pass through the origin ([Chapter 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). For a __nonlinear two-terminal element__ such as the incandescent lamp (Fig. [5](reale-widerstande-werte-und-temperatur.html#abb-5) right), $U/I$ depends on the operating point, and [(5.1)](#gl-5-1) does not hold there.

:::definition Definition 5.2 (Sign conventions)
<span class="anker" id="satz-5-2"></span>

The voltage arrow points from 1 to 2 and means $U_{12}=\varphi_1-\varphi_2$ ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). The current arrow counts positive charge in the direction of the arrow. In the __passive sign convention__ (PSC, load convention), the voltage and current arrows at a two-terminal element point in the same direction; in the __active sign convention__ (ASC, generator convention), they point in opposite directions. For a resistor,

<span class="anker" id="gl-5-2"></span>
$$U=R\,I\quad\text{(PSC)},\qquad U=-R\,I\quad\text{(ASC)}. \tag{5.2}$$
:::

⁠**How to read it:** Both conventions are only agreements. The direction of both arrows can be chosen freely; that changes signs, never the physics. The usual choice is the PSC at a load and the ASC at a source, because then all numbers are positive in normal operation (Fig. [6](#abb-6) left). **Why this fits:** In a load, positive charge runs from high to low potential and gives up energy; current and voltage have the same direction. In a source, it is lifted from low to high potential; current and voltage have opposite directions. In the PSC, $U\,I>0$ therefore means that energy is absorbed; in the ASC, it means that energy is delivered.

The __conventional current direction__ is the direction in which positive charge would move: outside the source from plus to minus. It corresponds to the current arrow at a load in the PSC. The electrons move the opposite way.

:::abbildung et1/k2zaehlpfeil 6
Left: chain of source and $3\,\mathrm{k\Omega}$ with the usual arrows. At the source opposite directions (ASC), at the resistor the same direction (PSC), all values positive. The electrons move against the current arrow. Right: the same resistor, once with the voltage arrow reversed. Only the sign changes.
:::

::::beispiel
9 V across $3\,\mathrm{k\Omega}$ give $I=3$ mA. If the voltage arrow points from bottom to top, $U=\varphi_\text{bottom}-\varphi_\text{top}=-9$ V, and [(5.2)](#gl-5-2) reads $-9\,\mathrm{V}=-3\,\mathrm{k\Omega}\cdot3\,\mathrm{mA}$. **Check:** Reversing both arrows turns $U=R\,I$ into $-U=R\,(-I)$, which is the same equation again.
::::

:::frage Electrons move from minus to plus. Why is it calculated the other way round?
The direction was fixed before electrons were known, and it does no harm: in $\vec j=q\,\vec v$, both factors change sign for electrons. Electrons moving left give the same current density as positive charge moving right. Voltage drop, heat and magnetic field depend only on $\vec j$.
:::

:::aufgabe Exercise 5 ★ Interpreting signs
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

A black box in the PSC shows $U=5$ V and $I=-2$ mA. Does it absorb or deliver energy, and how much per second?

</li>

<li>

A car battery in the ASC shows $U=14$ V and $I=-10$ A. What is happening to it?

</li>

<li>

In a wire, electrons move to the right; the magnitude of the current is 2 mA. The current arrow points to the right. How large is $I$?

</li>

</ol>

:::loesung
(a) $U\,I=-10$ mW in the PSC: the box delivers 10 mW; it works as a source. (b) $U\,I=-140$ W in the ASC: it does not deliver, but absorbs 140 W. It is being charged. (c) The current in the sense of positive charge runs to the left, so $I=-2$ mA.
:::
:::
