---
title: Stage 10: The R-2R converter
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1151200
summary: A processor knows only bits, a loudspeaker needs a voltage.
tags: digital-to-analog converter
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
A processor knows only bits, a loudspeaker needs a voltage. The R-2R converter translates between them. It is superposition and equivalent source in a single circuit.
:::

**The idea.** A __digital-to-analog converter__ turns a binary number with the bits $d_2d_1d_0$ into a voltage. In Fig. [12](#abb-12) each switch connects its 2$R$ resistor either to $U_\mathrm{ref}$ (bit 1) or to 0 V (bit 0). A switch at 0 V is a turned-off voltage source. So superposition is already built into the structure: every set bit is a source, all the others are wires. The ladder of $R$ and $2R$ is dimensioned so that each rung halves the effect.

:::abbildung et1/k5r2r 12
R-2R converter for three bits in the setting 101. Each changeover switch connects its resistor to $U_\mathrm{ref}$ or to ground. The output is taken at the top right.
:::

:::satz Theorem 10.1 (R-2R ladder)
<span class="anker" id="satz-10-1"></span>

For the converter in Fig. [12](#abb-12) with the output open,

<span class="anker" id="gl-10-1"></span>
$$U_\mathrm{out}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right),\qquad R_\mathrm{i}=R. \tag{10.1}$$
:::

⁠**How to read it:** $d_k$ is 0 or 1, $U_\mathrm{ref}$ the fixed reference voltage (a few volts), $R$ usually a few k$\Omega$. The most significant bit contributes half the reference voltage, each further one half of the previous one. $R_\mathrm{i}$ does not depend on the switch setting: on turning off, $U_\mathrm{ref}$ becomes 0 V, and then every branch leads to ground, however its switch is set. **Validity:** ideal switches without resistance of their own, output unloaded.

:::herleitung Equivalent source from left to right
At the left node, 2$R$ lies against ground and 2$R$ against $U_0=d_0U_\mathrm{ref}$. This is an equivalent source with $\frac12U_0$ and $2R\parallel2R=R$. With the series resistor it becomes $\frac12U_0$ and $2R$. At the next node this meets 2$R$ against $U_1=d_1U_\mathrm{ref}$: again two equal branches, hence the averaging from [(7.2)](quellen-zusammenschalten.html#gl-7-2), the equivalent source $\frac12\bigl(\frac12U_0+U_1\bigr)$ and again $R$. The last node repeats this:

$$U_\mathrm{out}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0.$$

Superposition gives the same number. Take source $U_1$ as an example: at the middle node it sees 2$R$ on the left and $R+2R=3R$ on the right, together $\frac65R$. The divider gives $\frac{6/5}{6/5+2}=\frac38U_1$ there. The way to the output divides once more by $\frac{2R}{R+2R}=\frac23$, so $\frac38\cdot\frac23=\frac14$.
:::

::::beispiel
With $U_\mathrm{ref}=8$ V and $R=1$ k$\Omega$, the bits weigh 4 V, 2 V and 1 V. The setting 101 gives 5 V. A load with $R_\mathrm{L}=R$ forms a divider with $R_\mathrm{i}$ and halves this to 2.5 V. That is why real converters are followed by an operational amplifier ([Chapter 11](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) with a very high input resistance: it draws practically no current, and the ladder stays in the open circuit.
::::

⁠**Limiting cases:** The setting 000 gives 0 V, the setting 111 gives 7 V, one step below $U_\mathrm{ref}$.

:::ltspice The converter counts
⁠**Draw:** Fig. [12](#abb-12) without switches: 2$R$ from node `n0` to ground, then 2$R$ each from `n0`, `n1`, `n2` to a source `voltage` against ground, and $R$ between the nodes, $R=1$ k$\Omega$. The sources count in binary: `PULSE(0 8 1m 1u 1u 1m 2m)`, `PULSE(0 8 2m 1u 1u 2m 4m)`, `PULSE(0 8 4m 1u 1u 4m 8m)`.

⁠**Directive:** `.tran 8m`

⁠**What you see:** `V(n2)` is a staircase with steps of 1 V, from 0 V to 7 V. With a load of 1 k$\Omega$ at `n2` it rises only to 3.5 V. With 3 k$\Omega$, your result from Exercise [12](#aufg-12)(c) appears on the top step.
:::

:::frage What is the single 2$R$ resistor at the far left for?
It makes the ladder uniform. With it, everything to the left of each node is an equivalent source with $2R$, just like the branch of the node's own switch. Only then do two equal branches and a pure mean value arise. Without it the left branch would be $3R$, and the weights would no longer be binary.
:::

:::aufgabe Exercise 12 ★★ Four bits
<span class="anker" id="aufg-12"></span>

(a) A converter with four bits runs on $U_\mathrm{ref}=16$ V. What are the step, the maximum value and the voltage at 1011? (b) How large is a step for eight bits at 5 V? (c) The three-bit converter from the example is set to 111 and feeds $R_\mathrm{L}=3R$. What voltage arises?

:::loesung
(a) Step $16\,\mathrm{V}/2^4=1$ V. Maximum value $15$ V. 1011: $8+0+2+1=11$ V. The formula continues with $d_3/2+d_2/4+d_1/8+d_0/16$.

(b) $5\,\mathrm{V}/256=19.5$ mV.

(c) Open circuit 7 V, internal resistance $R$. Divider: $7\,\mathrm{V}\cdot\frac{3R}{R+3R}=5.25$ V.
:::
:::
