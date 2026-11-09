---
title: Stage 7: Negative feedback holds the operating point in place
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200900
summary: The operating point from Stage 5 depends on B and on U BE , and both are unreliable.
tags: current feedback, voltage feedback
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The operating point from Stage [5](der-arbeitspunkt.html#stufe-5) depends on $B$ and on $U_\mathrm{BE}$, and both are unreliable. This stage shows how the circuit holds the current in place by itself.
:::

**The idea.** In the reference model, $I_\mathrm{C}=B\cdot10$ µ A. A specimen with $B=100$ carries 1 mA ($U_\mathrm{CE}=9$ V), one with $B=400$ reaches saturation. A fixed voltage $U_\mathrm{BE}$ would be worse: at fixed current, $U_\mathrm{BE}$ falls by around 2 mV per kelvin, and 18 mV double the current, so as little as 9 K of warming already doubles $I_\mathrm{C}$.

The remedy is a resistor in the emitter. A divider holds the base potential almost fixed. The current now runs in a loop against itself:

$I_\mathrm{C}$ rises $\to$ voltage across $R_\mathrm{E}$ rises $\to$ $\varphi_\mathrm{E}$ rises $\to$ $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$ falls $\to$ less injection $\to$ $I_\mathrm{C}$ falls.

The effect weakens its cause: this is negative feedback, here __current feedback__, because the current through $R_\mathrm{E}$ produces the opposing voltage. In the end $U_\mathrm{BE}$ changes only by millivolts, and the current follows from Ohm's law at $R_\mathrm{E}$ instead of from the exponential function. The second form connects $R_\mathrm{B}$ to the collector (Fig. [8](#abb-8), center). If $I_\mathrm{C}$ rises, $U_\mathrm{CE}$ falls, and with it $I_\mathrm{B}=(U_\mathrm{CE}-U_\mathrm{BE})/R_\mathrm{B}$ falls. This is __voltage feedback__.

:::abbildung et1/k10gegenkopplung 8
Left, current feedback with a base divider; center, voltage feedback. Right, $I_\mathrm{C}$ over $B$ in the reference model. Without feedback, the current grows in proportion to $B$ up to saturation (gray). The current feedback (blue) stays almost flat, the voltage feedback (orange) lies in between.
:::

:::satz Theorem 7.1 (Operating point with negative feedback)
<span class="anker" id="satz-7-1"></span>

Current feedback with the divider $R_1$, $R_2$ and $R_\mathrm{i}=R_1\parallel R_2$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2},\quad I_\mathrm{B}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{(1+B)R_\mathrm{E}+R_\mathrm{i}},\quad I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{E}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{i}}{B}}. \tag{7.1}$$

For $R_\mathrm{E}\gg R_\mathrm{i}/B$ and $B\gg1$, $I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$; if in addition $U_\mathrm{q}\gg U_\mathrm{BE}$, $I_\mathrm{C}\approx U_\mathrm{CC}R_2/\bigl(R_\mathrm{E}(R_1+R_2)\bigr)$.

Voltage feedback with $R_\mathrm{B}$ from the collector to the base:

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}+\frac{R_\mathrm{B}}{B}},\qquad\text{for } R_\mathrm{C}\gg\frac{R_\mathrm{B}}{B}:\ I_\mathrm{C}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}}. \tag{7.2}$$
:::

⁠**How to read it:** $U_\mathrm{q}$ and $R_\mathrm{i}$ describe the divider as an equivalent voltage source ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)): $U_\mathrm{q}$ is its open-circuit voltage, $R_\mathrm{i}$ its internal resistance. In the denominator, $R_\mathrm{E}$ acts almost fully, $R_\mathrm{i}$ only divided by $B$. **Validity:** active region. This must be checked at the end. $U_\mathrm{BE}$ is a fixed value here; the last approximation in [(7.1)](#gl-7-1) needs a large $U_\mathrm{q}$.

:::herleitung The formulas from the meshes
The divider becomes the source $U_\mathrm{q}$ with $R_\mathrm{i}$ in series. With $I_\mathrm{E}=(1+B)I_\mathrm{B}$, the mesh through base and emitter reads

$$U_\mathrm{q}=I_\mathrm{B}R_\mathrm{i}+U_\mathrm{BE}+I_\mathrm{B}(1+B)R_\mathrm{E}.$$

Solving for $I_\mathrm{B}$ and multiplying by $B$ gives [(7.1)](#gl-7-1). With voltage feedback, the current $I_\mathrm{C}+I_\mathrm{B}$ flows through $R_\mathrm{C}$, and only $I_\mathrm{B}$ through $R_\mathrm{B}$. With $I_\mathrm{B}=I_\mathrm{C}/B$, the mesh reads

$$U_\mathrm{CC}-U_\mathrm{BE}=\Bigl(\frac{I_\mathrm{C}}{B}+I_\mathrm{C}\Bigr)R_\mathrm{C}+\frac{I_\mathrm{C}}{B}R_\mathrm{B}.$$

Solving for $I_\mathrm{C}$ gives [(7.2)](#gl-7-2).
:::

::::beispiel
Reference model: $U_\mathrm{q}=2.7$ V, $R_\mathrm{i}=6.98$ k$\Omega$, $R_\mathrm{i}/B=35\,\Omega\ll1$ k$\Omega$. This gives $I_\mathrm{C}=2.1\,\mathrm{V}/1040\,\Omega=2.02$ mA and $U_\mathrm{CE}=12\,\mathrm{V}-6.06\,\mathrm{V}-2.03\,\mathrm{V}=3.91$ V, so active. The base potential is 2.63 V, and the divider carries 300 µ A, 30 times $I_\mathrm{B}$.

| $I_\mathrm{C}$ at | $B=100$ | $B=200$ | $B=400$ |
|---|---|---|---|
| without feedback ($I_\mathrm{B}=10$ µ A) | 1 mA | 2 mA | 3.93 mA (saturation) |
| voltage feedback ($R_\mathrm{B}=540$ k$\Omega$) | 1.35 mA | 1.99 mA | 2.62 mA |
| current feedback | 1.94 mA | 2.02 mA | 2.06 mA |

Temperature, too, has hardly any effect now: 50 K of warming lowers $U_\mathrm{BE}$ by 0.1 V, and with [(7.1)](#gl-7-1) $I_\mathrm{C}$ rises by only 4.8 %. At a fixed voltage $U_\mathrm{BE}$ it would be 47 times the value. Voltage feedback achieves less, because here $R_\mathrm{B}/B=2.7$ k$\Omega$ is not small compared with 3 k$\Omega$. With $R_\mathrm{B}=100$ k$\Omega$, $I_\mathrm{C}$ varies only between 2.83 mA and 3.50 mA, but then only $U_\mathrm{CE}=2.2$ V remains.
::::

⁠**Limiting cases:** $R_\mathrm{E}\to0$ gives $I_\mathrm{C}=B(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{i}$, the formula with base resistor from Stage [5](der-arbeitspunkt.html#stufe-5). $B\to\infty$ gives $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$.

:::frage What does the emitter resistor cost?
Two things. The voltage across $R_\mathrm{E}$, here 2 V, is missing at the collector for the signal swing. And the negative feedback also acts on the signal: the voltage gain falls sharply (Stage [10](drei-grundschaltungen.html#stufe-10)). A capacitor in parallel with $R_\mathrm{E}$ acts like a wire for AC signals and removes the second drawback.
:::

:::ltspice $I_\mathrm{C}$ is almost independent of $B$
⁠**Draw:** `voltage` `VCC` with 12 at net `cc`. Divider `res` 31k from `cc` to `b`, 9k from `b` to ground. `npn` with model `T`, `res` 3k from `cc` to the collector, `res` 1k from the emitter to ground.

⁠**Directives:** `.model T NPN(IS=1.55e-13 BF={BF} VAF=74)`, `.param BF=186`, `.step param BF list 93 186 372`, `.dc VCC 0 12 0.1`, `.meas dc ic FIND Ic(Q1) AT=12`. The three values correspond to $B=100$, 200, 400 at 6 V.

⁠**What you see:** Three almost coincident curves. At 12 V, LTspice gives 1.94 mA; 2.02 mA; 2.06 mA, exactly as in the calculation. Enter the values from Exercise [8](#aufg-8) and check your spread.
:::

:::aufgabe Exercise 8 ★★★ Designing the operating point
<span class="anker" id="aufg-8"></span>

Using T, design a current feedback circuit for $U_\mathrm{CC}=15$ V, $I_\mathrm{C}=1$ mA, 2 V across $R_\mathrm{E}$ and $U_\mathrm{CE}=6$ V. (a) Determine $R_\mathrm{E}$ and $R_\mathrm{C}$ as round values. (b) $10\,I_\mathrm{B}$ are to flow through $R_2$. Determine $R_2$ and $R_1$ (round to 52 k$\Omega$ and 225 k$\Omega$). (c) Calculate $I_\mathrm{C}$ for $B=100$, 200, 400 and compare with the circuit from the table. Why is the spread larger? Predict the result before you calculate.

:::loesung
(a) $R_\mathrm{E}=2\,\mathrm{V}/1\,\mathrm{mA}=2$ k$\Omega$, $R_\mathrm{C}=(15-6-2)\,\mathrm{V}/1\,\mathrm{mA}=7$ k$\Omega$.

(b) $I_\mathrm{B}=5$ µ A, base potential 2.6 V. $R_2=2.6\,\mathrm{V}/50\,\mu\text{A}=52$ k$\Omega$. Through $R_1$ flow 55 µ A: $R_1=12.4\,\mathrm{V}/55\,\mu\text{A}=225$ k$\Omega$.

(c) $U_\mathrm{q}=2.82$ V, $R_\mathrm{i}=42.2$ k$\Omega$. With [(7.1)](#gl-7-1), $I_\mathrm{C}=0.91$ mA; 1.00 mA; 1.05 mA. Prediction: the spread is larger because $R_\mathrm{i}/B=211\,\Omega$ is no longer small compared with $R_\mathrm{E}$. Here the divider carries only ten times $I_\mathrm{B}$ instead of thirty times. LTspice: 0.92 mA; 1.01 mA; 1.06 mA.
:::
:::

:::aufgabe Exercise 9 ★★ Voltage feedback
<span class="anker" id="aufg-9"></span>

Take the voltage feedback from the example. (a) Check $I_\mathrm{C}$ and $U_\mathrm{CE}$ for $B=200$. (b) Limiting case $R_\mathrm{B}\to0$: What values do $U_\mathrm{CE}$ and $I_\mathrm{C}$ have? Is the transistor then active? Answer with [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) and the meaning of $U_\mathrm{CB}$.

:::loesung
(a) $I_\mathrm{C}=11.4\,\mathrm{V}/(3015\,\Omega+2700\,\Omega)=1.99$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-3\,\text{k}\Omega\cdot2.005\,\mathrm{mA}=5.99$ V.

(b) Base and collector are connected: $U_\mathrm{CE}=U_\mathrm{BE}=0.6$ V and $I_\mathrm{C}=11.4\,\mathrm{V}/3015\,\Omega=3.78$ mA. Because $U_\mathrm{CE}>0.2$ V the transistor is active, exactly on the line $U_\mathrm{CB}=0$. This is T1 in the current mirror.
:::
:::
