---
title: Stage 7: Linear equivalent circuits
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Semiconductors and Diodes
order: 1190900
summary: With several diodes, several exponential equations become coupled, and that can no longer be done by hand.
tags: Ideal diode, Diode with forward voltage, forward voltage
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
With several diodes, several exponential equations become coupled, and that can no longer be done by hand. This stage replaces the diode with linear parts and gives a method that always works.
:::

**The idea.** Over three decades of current, $U_\mathrm D$ changes by only 180 mV. So the characteristic curve is almost a right angle, and the component almost a switch. The price of the model: you must know the switching state of each diode. You assume it and check it afterward.

:::abbildung et1/k9ersatz 9
Top left: real characteristic curve (blue), ideal diode (green) and model with $U_\mathrm F=0.7$ V (red). Top right: the equivalent circuits of both models in the conducting and blocking states. Bottom: example with two diodes and its result.
:::

:::definition Definition 7.1 (Two diode models)
<span class="anker" id="satz-7-1"></span>

__Ideal diode__: a short circuit when conducting, an open circuit when blocking.

<span class="anker" id="gl-7-1"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=0,\qquad U_\mathrm D<0\ \Rightarrow\ I_\mathrm D=0. \tag{7.1}$$

__Diode with forward voltage__: a voltage source $U_\mathrm F$ when conducting, an open circuit when blocking.

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=U_\mathrm F,\qquad U_\mathrm D<U_\mathrm F\ \Rightarrow\ I_\mathrm D=0. \tag{7.2}$$
:::

⁠**How to read it:** $U_\mathrm F$ is called the __forward voltage__, also the forward drop. It is neither a material value like $U_\mathrm{D0}$ nor a threshold, but a model value: you choose the voltage at the expected current. Common values are 0.6 V or 0.7 V. The model diode has 0.6 V at 0.12 mA and 0.7 V at 5.8 mA. **Validity:** In the reference model, exactly $I=4.31$ mA. The ideal diode gives 5.00 mA (16 % too much), $U_\mathrm F=0.7$ V gives 4.30 mA ($-0.2$ %), $U_\mathrm F=0.6$ V gives 4.40 mA (2 % too much). The ideal diode is sufficient only when the voltages in the circuit are large compared with 0.7 V.

**The method.**

<ol>

<li>

Choose an equivalent circuit for the diodes.

</li>

<li>

Make a plausible assumption about which diode conducts and which blocks.

</li>

<li>

Replace the diodes and calculate all currents and voltages.

</li>

<li>

Check: conducting diodes need $I_\mathrm D>0$, blocking ones $U_\mathrm D<U_\mathrm F$. If there is a contradiction, make a new assumption.

</li>

</ol>

$n$ diodes have $2^n$ combinations, so a good first assumption pays off. A look at the potentials helps.

**Example.** Fig. [9](#abb-9) bottom: 5 V and 2 V feed node X through 1 k$\Omega$ and a diode each; from there $R_3=2\,\mathrm{k\Omega}$ leads to ground. $U_\mathrm F=0.7$ V.

⁠*Assumption 1: Both conduct.* The node rule ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) at X reads $(4.3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(1.3\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$. This gives $\varphi_\mathrm X=2.24$ V, $I_\mathrm{D1}=2.06$ mA and $I_\mathrm{D2}=-0.94$ mA. The negative current is a contradiction.

⁠*Assumption 2: D$_1$ conducts, D$_2$ blocks.* Then $I=(5\,\mathrm{V}-0.7\,\mathrm{V})/3\,\mathrm{k\Omega}=1.43$ mA and $\varphi_\mathrm X=2.87$ V. Across D$_2$ is $U_\mathrm{D2}=2\,\mathrm{V}-2.87\,\mathrm{V}=-0.87$ V. That is smaller than $U_\mathrm F$, no contradiction. The APs are D$_1$ (0.7 V | 1.43 mA) and D$_2$ ($-0.87$ V | 0). The full simulation gives 2.89 V and 1.45 mA.

⁠*View of the potentials:* D$_2$ conducts only if $\varphi_\mathrm X<2\,\mathrm{V}-0.7\,\mathrm{V}=1.3$ V. The 5-V source alone already raises X to 2.87 V, so the cathode of D$_2$ lies above the anode. The higher voltage prevails. Assumption 3 (only D$_2$ conducts) would give $U_\mathrm{D1}=4.13$ V, assumption 4 (both block) $U_\mathrm{D1}=5$ V, both larger than $U_\mathrm F$ and thus contradictions. **Limiting case:** At $U_2=5$ V both branches are equal, and each diode carries half.

:::frage Why is a negative current a contradiction? A voltage source can absorb current, after all.
The equivalent source can, the diode cannot: in the reverse direction only $I_\mathrm S$ flows. The model applies only for $I_\mathrm D>0$. A negative result shows that the calculation used the diode outside this range.
:::

:::aufgabe Exercise 8 ★★ Who wins?
<span class="anker" id="aufg-8"></span>

In the example, the 2-V source becomes the source $U_2$.

<ol class="al">

<li>

Let $U_2=4.5$ V. Which diodes conduct? Calculate $\varphi_\mathrm X$ and all diode currents.

</li>

<li>

From which $U_2$ on does D$_2$ begin to conduct?

</li>

</ol>

:::loesung
(a) Assumption: both conduct. $(4.3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(3.8\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$ gives $\varphi_\mathrm X=3.24$ V, $I_\mathrm{D1}=1.06$ mA, $I_\mathrm{D2}=0.56$ mA. Both positive, no contradiction. Check: $1.62\,\mathrm{mA}\cdot2\,\mathrm{k\Omega}=3.24$ V. (b) As long as D$_2$ blocks, $\varphi_\mathrm X=2.87$ V. D$_2$ begins to conduct when $U_2-0.7\,\mathrm{V}=2.87$ V, that is, at $U_2=3.57$ V.
:::
:::

:::aufgabe Exercise 9 ★★★ Protection diodes
<span class="anker" id="aufg-9"></span>

The input of a chip is node X. A voltage $U_\mathrm e$ feeds it through $R=1\,\mathrm{k\Omega}$. D$_1$ leads from X (anode) to the supply $+5$ V. D$_2$ leads from ground (anode) to X. $U_\mathrm F=0.7$ V.

<ol class="al">

<li>

For $U_\mathrm e=3$ V, $12$ V and $-3$ V, determine which diode conducts, as well as $\varphi_\mathrm X$ and the current through $R$.

</li>

<li>

Sketch $\varphi_\mathrm X$ versus $U_\mathrm e$.

</li>

<li>

Why can one of the four combinations be ruled out without calculation?

</li>

</ol>

:::loesung
(a) $U_\mathrm e=3$ V: no diode conducts, $I=0$, $\varphi_\mathrm X=3$ V. Check: $U_\mathrm{D1}=-2$ V, $U_\mathrm{D2}=-3$ V. $U_\mathrm e=12$ V: D$_1$ conducts, $\varphi_\mathrm X=5.7$ V, $I=6.3$ mA flows into the supply. $U_\mathrm e=-3$ V: D$_2$ conducts, $\varphi_\mathrm X=-0.7$ V, $I=-2.3$ mA, the current comes from ground. (b) A ramp $\varphi_\mathrm X=U_\mathrm e$ between $-0.7$ V and 5.7 V, horizontal outside: the input stays protected. (c) If both conducted, $\varphi_\mathrm X$ would have to be 5.7 V and $-0.7$ V at the same time.
:::
:::
