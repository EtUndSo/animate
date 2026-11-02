---
title: Stage 4: Three regions, three equivalent circuits
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200600
summary: With exponential functions, circuits can hardly be solved by hand.
tags: cut-off region, saturation region, threshold voltage, saturation voltage, equivalent circuit
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
With exponential functions, circuits can hardly be solved by hand. This stage replaces the surface with three linear pieces.
:::

**The idea.** Each of the two diodes can conduct or block. This gives the operating states. If the BE diode blocks, no electron starts and nothing flows. This is the __cut-off region__. If it conducts and the CB diode blocks, the collector collects all the electrons, and $I_\mathrm{C}=B\,I_\mathrm{B}$ holds. This is the active region. If $U_\mathrm{CE}$ falls so far that the CB diode conducts noticeably as well, the collector sends electrons back. Then it can no longer collect them all, the base fills up with electrons, and $I_\mathrm{C}$ stays below $B\,I_\mathrm{B}$. This is the __saturation region__. As with the diode ([Part 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)), the curves are replaced by straight lines: the input characteristic gets a knee at 0.6 V, the current control characteristic becomes a straight line with slope $B$ that bends to horizontal in saturation, and the output characteristics become horizontal to the right of 0.2 V (Fig. [6](der-arbeitspunkt.html#abb-6)).

:::definition Definition 4.1 (Operating regions of the npn transistor)
<span class="anker" id="satz-4-1"></span>

With the __threshold voltage__ $U_\mathrm{BE,on}=0.6$ V and the __saturation voltage__ $U_\mathrm{CE,sat}=0.2$ V:

<span class="anker" id="gl-4-1"></span>
<span class="anker" id="gl-4-2"></span>
<span class="anker" id="gl-4-3"></span>
$$\begin{aligned} \text{Cut-off region:}\quad & U_\mathrm{BE}<U_\mathrm{BE,on}\;\Rightarrow\; I_\mathrm{B}=I_\mathrm{C}=0,\\ \text{active region:}\quad & U_\mathrm{BE}=U_\mathrm{BE,on},\ I_\mathrm{B}>0,\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}\ge U_\mathrm{CE,sat},\\ \text{saturation region:}\quad & U_\mathrm{BE}=U_\mathrm{BE,on},\ I_\mathrm{B}>0,\quad U_\mathrm{CE}=U_\mathrm{CE,sat},\quad I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.1|4.2|4.3}$$
:::

⁠**How to read it:** Each region has a linear __equivalent circuit__ of ideal elements that holds between B, C and E (Fig. [5](#abb-5)). In the cut-off region, all terminals are open. In the two conducting regions, a voltage source of 0.6 V lies between B and E; between C and E there is a controlled current source in the active region and a voltage source of 0.2 V in saturation. At the common node, $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$ always holds. **Validity:** a rough but proven approximation. The threshold is not a true switch (Stage [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2)); the 0.6 V fit T at 2 mA, at 20 mA it would be 0.66 V. The value 0.2 V depends on the type.

:::abbildung et1/k10esb 5
The three equivalent circuits of the npn transistor. Left, open in the cut-off region; center, with a controlled current source in the active region; right, with two voltage sources in saturation. At the node above E, $I_\mathrm{B}$ and $I_\mathrm{C}$ unite.
:::

**Example.** For T ($B=200$): $I_\mathrm{B}=10$ µ A with $U_\mathrm{CE}=6$ V is active, so $I_\mathrm{C}=2$ mA. $I_\mathrm{B}=30$ µ A with $I_\mathrm{C}=3.9$ mA is saturation, because $B\,I_\mathrm{B}=6$ mA is larger than the current the circuit allows. $U_\mathrm{BE}=0.3$ V is the cut-off region. **Limiting case:** for $B\,I_\mathrm{B}=I_\mathrm{C}$ and $U_\mathrm{CE}=U_\mathrm{CE,sat}$, the transistor lies exactly on the boundary between active and saturation. Both equivalent circuits give the same result there.

:::frage Why is it called saturation when the current just stops following?
What is saturated is not the current but the base: it is overfilled with electrons. That is why, for the bipolar transistor, the word means the steep part at the left of the output characteristic. For the MOSFET, the flat part is called saturation. The two words mean different things.
:::

**The pnp transistor.** In the pnp transistor, n and p are swapped (Fig. [1](drei-schichten-zwei-spannungen.html#abb-1)). The mechanisms stay the same, but holes take over the role of the electrons. The emitter lies at the highest potential, and all signs reverse. With the npn designations, $U_\mathrm{BE,on}=-0.6$ V and $U_\mathrm{CE,sat}=-0.2$ V are now negative. If $I_\mathrm{B}$ and $I_\mathrm{C}$ are counted out of the component, both are positive, and:

<span class="anker" id="gl-4-4"></span>
$$\begin{aligned} &\text{cut-off region: } U_\mathrm{BE}>-0.6\,\mathrm{V};\qquad \text{active: } I_\mathrm{C}=B\,I_\mathrm{B},\ U_\mathrm{CE}\le-0.2\,\mathrm{V};\\ &\text{saturation: } U_\mathrm{CE}=-0.2\,\mathrm{V},\ I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.4}$$

In practice the npn transistor is more common, because electrons in silicon are around three times more mobile than holes. The pnp form serves mainly where the emitter is to sit at the positive supply.

:::aufgabe Exercise 4 ★ Recognizing the region
<span class="anker" id="aufg-4"></span>

Determine the region of T and the missing current or the missing voltage. (a) $I_\mathrm{B}=20$ µ A, $U_\mathrm{CE}=5$ V. (b) $I_\mathrm{B}=40$ µ A, $I_\mathrm{C}=3$ mA. (c) $U_\mathrm{BE}=-1$ V, $U_\mathrm{CE}=12$ V. (d) A pnp transistor with $B=200$: $U_\mathrm{CE}=-5$ V and $I_\mathrm{B}=10$ µ A.

:::loesung
(a) $I_\mathrm{B}>0$ and $U_\mathrm{CE}>0.2$ V: active, $I_\mathrm{C}=4$ mA. (b) $B\,I_\mathrm{B}=8$ mA $>3$ mA: saturation, $U_\mathrm{CE}=0.2$ V. (c) $U_\mathrm{BE}<0.6$ V: cut-off region, $I_\mathrm{B}=I_\mathrm{C}=0$. (d) $U_\mathrm{CE}\le-0.2$ V and $I_\mathrm{B}>0$: active, $I_\mathrm{C}=2$ mA, $U_\mathrm{BE}=-0.6$ V.
:::
:::
