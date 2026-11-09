---
title: Stage 9: Positive feedback and the Schmitt trigger
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1211100
summary: If you swap the inputs of the non-inverting amplifier, the same equations give the same number.
tags: hysteresis, Schmitt trigger, unstable
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
If you swap the inputs of the non-inverting amplifier, the same equations give the same number. But the circuit does something completely different. This stage clarifies why the rule fails here and what happens instead.
:::

**The idea.** Now $U_\mathrm{E}$ is at the minus input, and the divider leads to the plus input (Fig. [11](#abb-11)). The calculation $U_\mathrm{D}=\beta\,U_\mathrm{A}-U_\mathrm{E}$ and $U_\mathrm{A}=A\,U_\mathrm{D}$ has, at $U_\mathrm{E}=1$ V, the solution $U_\mathrm{A}=5.00025$ V. This is an equilibrium, but an unstable one, like a ball on a hilltop. A disturbance of 1 µ V upward raises the plus input, so $U_\mathrm{D}$ grows, so the output rises further. The effect reinforces its cause. The output runs to its limit and stays there. There the rule does not hold: $U_\mathrm{D}\ne0$.

At the limit the circuit remembers its state. If the output is at $+11$ V, the plus input is at $+2.2$ V. As long as $U_\mathrm{E}$ stays below that, $U_\mathrm{D}>0$ and nothing changes. If $U_\mathrm{E}$ exceeds 2.2 V, the output flips, and the plus input jumps to $-2.2$ V. This reinforces the flipping. To flip back, $U_\mathrm{E}$ has to fall below $-2.2$ V. The output depends on the history; this is called __hysteresis__. The circuit is called an inverting __Schmitt trigger__.

:::satz Theorem 9.1 (Schmitt trigger)
<span class="anker" id="satz-9-1"></span>

With $\beta=R_1/(R_1+R_2)$ the output flips

<span class="anker" id="gl-9-1"></span>
$$\text{downward at }U_\mathrm{E}=\beta\,U_\mathrm{A,max},\qquad\text{upward at }U_\mathrm{E}=\beta\,U_\mathrm{A,min}. \tag{9.1}$$

The width of the hysteresis is $\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$. Between the thresholds both states are possible.
:::

⁠**How to read it:** The output changes as soon as $U_\mathrm{D}$ changes sign. **Validity:** $A\beta>1$; otherwise the positive feedback is not enough to flip.

:::herleitung The same equation, a different sign
With the sluggishness from Stage [4](gegenkopplung.html#stufe-4), now $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A(\beta\,U_\mathrm{A}-U_\mathrm{E})-U_\mathrm{A}=(A\beta-1)\,U_\mathrm{A}-A\,U_\mathrm{E}$. The factor in front of $U_\mathrm{A}$ is now positive. A deviation from equilibrium grows like $\mathrm{e}^{+t/\tau_\mathrm{M}}$ with $\tau_\mathrm{M}=\tau/(A\beta-1)=0.80$ µ s, the same size as in Stage [4](gegenkopplung.html#stufe-4). In this way a disturbance of 1 µ V becomes the 11 V in 13 µ s. An unlimited supply would give an unlimited rise; the circuit would be __unstable__. Only saturation stops it.
:::

:::abbildung et1/k11schmitt 11
Left, the inverting Schmitt trigger. Right, the hysteresis loop in the reference model, $\beta=0.2$: coming from the left, it flips at $+2.2$ V; coming from the right, at $-2.2$ V. The arrows give the direction of travel.
:::

::::beispiel
The thresholds are $\pm0.2\cdot11\,\mathrm{V}=\pm2.2$ V, and the hysteresis is 4.4 V wide. Shortly after flipping at $U_\mathrm{E}=2.2$ V, $U_\mathrm{D}=-2.2\,\mathrm{V}-2.2\,\mathrm{V}=-4.4$ V, far from the window. Benefit: a noisy signal passing slowly through a threshold switches a comparator back and forth many times. With the Schmitt trigger the threshold jumps away by 4.4 V after the first flip, and noise below this width triggers no second flip.
::::

⁠**Limiting cases:** $\beta\to0$ gives the comparator from Stage [3](der-opv-ohne-ruckfuhrung.html#stufe-3). $U_\mathrm{E}=0$ allows both states, depending on the history.

:::frage With swapped inputs, LTspice showed 5.00025 V in `.op`. Is the simulation wrong?
No, it answers a different question. `.op` solves the equilibrium equation, and this solution exists. Whether an equilibrium holds is decided only by the time behavior. In the component something is always making noise, which is why the output runs away. The LTspice box in Stage [10](wo-die-regeln-enden.html#stufe-10) shows this in `.tran`.
:::

:::aufgabe Exercise 10 ★★ Schmitt trigger
<span class="anker" id="aufg-10"></span>

(a) With $R_1=10$ k$\Omega$, $R_2=90$ k$\Omega$: Where are the thresholds, and how wide is the hysteresis? (b) Choose $R_2$ for the thresholds $\pm1$ V at $R_1=10$ k$\Omega$. (c) With (a), $U_\mathrm{E}$ runs from $-5$ V to $+5$ V and back. Sketch $U_\mathrm{A}(U_\mathrm{E})$. (d) A supply from 0 to 5 V gives an output from 0.5 V to 4.5 V, $\beta=0.2$. Where are the thresholds?

:::loesung
(a) $\beta=0.1$: thresholds $\pm1.1$ V, width 2.2 V. (b) $\beta=1/11$, so $R_2=100$ k$\Omega$. (c) At $-5$ V the output is at $+11$ V. It stays there until $U_\mathrm{E}=+1.1$ V, jumps to $-11$ V and stays there up to $5$ V. On the way back it jumps back only at $-1.1$ V. (d) $0.2\cdot4.5\,\mathrm{V}=0.9$ V and $0.2\cdot0.5\,\mathrm{V}=0.1$ V.
:::
:::
