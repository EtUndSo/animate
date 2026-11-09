---
title: Stage 8: Charge conservation when switching
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1130900
summary: If you switch charged capacitors, the new voltage can be found without any current calculation.
tags: 
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
If you switch charged capacitors, the new voltage can be found without any current calculation. It is enough to count charge.
:::

**The idea.** In a closed system the sum of the charges stays constant ([Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). In circuits, such a system arises when every path from a node to ground leads through a capacitor. This is the island from Stage [7](parallel-und-reihenschaltung.html#stufe-7): the dielectrics block all routes. Charge can redistribute within the island, but cannot leave it. If you compare before and after, you do not need to know how the equalization proceeded.

:::satz Theorem 8.1 (Charge conservation on an island)
<span class="anker" id="satz-8-1"></span>

If every path from a node to ground leads through a capacitance, the sum of the charges on the connected plates stays constant:

<span class="anker" id="gl-8-1"></span>
$$Q_\mathrm{tot}=\sum_iC_iU_i=\text{const}. \tag{8.1}$$
:::

⁠**How to read it:** $U_i$ is the voltage from the node to the opposite plate, so $C_iU_i$ is the charge of the plate at the node, with sign. The comparison holds between two states of rest; $Q=C\,U$ supplies the voltages. **Validity:** No resistor and no source to the outside may hang on the node, and the equalization must be fast compared with the self-discharge.

:::abbildung et1/k3umladen 8
Position 1: $C_1$ charges to 9 V, $C_2$ is empty. Position 2: The dashed island contains the upper plates of both capacitors. The 900 µC distribute themselves until both voltages are equal.
:::

::::beispiel
In Fig. [8](#abb-8), $C_1$ carries the charge $C_1U_0=900\,\mu\text{C}$ in position 1, and $C_2$ is empty. The switch moves to position 2. Both upper plates now hang on one wire, so after the equalization the same voltage $U$ applies. From [(8.1)](#gl-8-1) it follows that

<span class="anker" id="gl-8-2"></span>
$$C_1U+C_2U=C_1U_0\quad\Longrightarrow\quad U=U_0\,\frac{C_1}{C_1+C_2}=9\,\mathrm{V}\cdot\frac{100}{150}=6\,\mathrm{V}. \tag{8.2}$$

Afterward $C_1$ still carries 600 µC, and $C_2$ has received 300 µC.
::::

**The energy is not conserved.** Before, $\frac12C_1U_0^2=4.05$ mJ is stored, afterward $\frac12(C_1+C_2)U^2=2.70$ mJ. Missing are 1.35 mJ, one third. The equalizing current heats the wires and the switch. The loss does not depend on their resistance: a smaller resistance gives a larger current for a shorter time, and the two cancel exactly. In general, in the equalization of two voltages $U_1$ and $U_2$, the loss is:

<span class="anker" id="gl-8-3"></span>
$$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2. \tag{8.3}$$

:::herleitung Loss in the equalization
With $U=\frac{C_1U_1+C_2U_2}{C_1+C_2}$ from [(8.1)](#gl-8-1),

$$W_\mathrm{V}=\tfrac12C_1U_1^2+\tfrac12C_2U_2^2-\tfrac12\,\frac{(C_1U_1+C_2U_2)^2}{C_1+C_2}.$$

Over the common denominator $2(C_1+C_2)$, $C_1^2U_1^2$ and $C_2^2U_2^2$ cancel. The numerator leaves $C_1C_2(U_1^2-2U_1U_2+U_2^2)$, which is [(8.3)](#gl-8-3).
:::

⁠**Limiting cases:** For $C_2\to0$, $U=U_0$ remains and nothing is lost. For $C_2\gg C_1$, $U\to0$: the charge does not vanish, but it spreads over so large a capacitor that hardly any voltage remains.

:::frage The charge also changes during charging in position 1. Why does conservation not hold there?
Because there is no island there. The node hangs directly on ground through the battery, which is a path without capacitance. The charge flows in through it. Conservation always holds for the whole, but [(8.1)](#gl-8-1) needs a node that all routes leave through dielectrics.
:::

:::ltspice Charge sharing through a resistor
⁠**Draw:** `cap` with `100u` from `a` to ground, initial value `IC=9`. `cap` with `50u` from `b` to ground, initial value `IC=0`. `res` with `{Rv}` from `a` to `b`. This resistor stands for wires and switch.

⁠**Directives:** `.param Rv=10`, `.step param Rv list 1 10 100`, `.tran 0 100m 0 1u uic`, plus `.meas tran ua FIND V(a) AT=100m` and `.meas tran wr INTEG V(a,b)*I(R1)`. The result is in the SPICE Error Log.

⁠**What you see:** For all three resistors, `ua` $=6$ V and `wr` $=1.35$ mJ, as in [(8.2)](#gl-8-2) and [(8.3)](#gl-8-3). Only the time of the equalization changes. Set `IC=3` at $C_2$ and compare with Exercise [9](#aufg-9)(a).
:::

:::aufgabe Exercise 9 ★★ Charge sharing with precharge
<span class="anker" id="aufg-9"></span>

$C_1=100\,\mu\text{F}$ carries 9 V. Then $C_2=50\,\mu\text{F}$, which is already charged, is connected.

<ol class="al">

<li>

$C_2$ carries $+3$ V, in the same sense as $C_1$. How large is the final voltage? How much energy is lost?

</li>

<li>

$C_2$ carries $-3$ V, that is, reverse polarity. How large are the final voltage and the loss now?

</li>

<li>

Limiting case: What results for $U_2=9$ V, and why does no equalizing current flow?

</li>

</ol>

:::loesung
(a) $Q=100\,\mu\text{F}\cdot9\,\mathrm{V}+50\,\mu\text{F}\cdot3\,\mathrm{V}=1050\,\mu\text{C}$, $U=1050\,\mu\text{C}/150\,\mu\text{F}=7$ V. Loss from [(8.3)](#gl-8-3): $\frac12\cdot33.3\,\mu\text{F}\cdot(9\,\mathrm{V}-3\,\mathrm{V})^2=0.60$ mJ. Check: 4.275 mJ before, 3.675 mJ after.

(b) $Q=900\,\mu\text{C}-150\,\mu\text{C}=750\,\mu\text{C}$, $U=5$ V. Loss: $\frac12\cdot33.3\,\mu\text{F}\cdot(12\,\mathrm{V})^2=2.40$ mJ. The difference of the voltages is 12 V, not 6 V.

(c) $U=9$ V, $W_\mathrm{V}=0$. Both nodes are already at the same potential, so nothing drives a current.
:::
:::
