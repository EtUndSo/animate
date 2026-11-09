---
title: Stage 9: Series connection and voltage divider
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Current, Resistance and Kirchhoff's Laws
order: 1121000
summary: Many networks are composed of two basic patterns.
tags: series connection, total resistance, unloaded, digital-to-analog converter, bits, buffer, comparator, decoder
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Many networks are composed of two basic patterns. This stage combines resistors in series, shows how the voltage divides, and builds a converter from this.
:::

**The idea.** Nothing branches off between the resistors; the node rule forces the same current in all of them. The midpoint settles at the potential at which that holds. The same current needs more drive in a larger resistor: the field does more work per charge there, and more voltage drops across it.

:::satz Theorem 9.1 (Series connection and voltage divider)
<span class="anker" id="satz-9-1"></span>

For $N$ resistors in a __series connection__,

<span class="anker" id="gl-9-1"></span>
<span class="anker" id="gl-9-2"></span>
$$\begin{aligned} I&=I_1=I_2=\dots=I_N,\qquad U=U_1+U_2+\dots+U_N,\qquad U_i=R_i\,I,\\ R_\mathrm{tot}&=\sum_{i=1}^{N}R_i,\qquad\frac{U_\nu}{U}=\frac{R_\nu}{\sum_{i=1}^NR_i}, \end{aligned} \tag{9.1|9.2}$$

so for two resistors the voltage divider rule

<span class="anker" id="gl-9-3"></span>
$$\frac{U_2}{U}=\frac{R_2}{R_1+R_2},\qquad\frac{U_1}{U_2}=\frac{R_1}{R_2}. \tag{9.3}$$
:::

⁠**How to read it:** $R_\mathrm{tot}$ is the __total resistance__, the one resistor that replaces the chain. The voltages are in the same ratio as the resistances. **Validity:** The divider rule holds only when __unloaded__: no current may be drawn at the tap, otherwise $I_1\neq I_2$ (Stage [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10)).

:::herleitung Total resistance and divider rule
The mesh rule gives $U=\sum U_i$, Ohm's law gives $U_i=R_i\,I$ with the same $I$. So $U=(R_1+\dots+R_N)\,I$. In the quotient of $U_\nu=R_\nu\,I$ and $U$, $I$ cancels.
:::

::::beispiel
The chain has $R_\mathrm{tot}=3\,\mathrm{k\Omega}$, so $I=3$ mA, $U_1=6$ V and $U_2=3$ V (Fig. [10](#abb-10) left). From [(9.3)](#gl-9-3): $U_2=9\,\mathrm{V}\cdot1/3=3$ V.
::::

⁠**Limiting cases:** $R_2\to0$ gives $U_2\to0$: a short circuit carries no voltage. $R_2\to\infty$ gives $U_2\to U$: an open point carries the entire voltage. $R_1=R_2$ halves $U$.

:::abbildung et1/k2teiler 10
Left: the voltage divider of the reference model. Center: chain of a 3-bit converter at $U_\mathrm{ref}=3.2$ V. The end pieces $R/2$ shift all taps by half a step. Right: output versus the number $Z$. The staircase lies centered around the dashed ideal straight line; the error is at most half a step.
:::

**Application: digital-to-analog converter.** A __digital-to-analog converter__ (D/A converter) turns a number into a voltage. Three __bits__ (binary digits $b_0$, $b_1$, $b_2$) give the numbers $Z=0$ to 7. A chain of $R/2$, seven $R$ and $R/2$ has the total resistance $8R$ and divides $U_\mathrm{ref}$ into eight steps. The taps carry

<span class="anker" id="gl-9-4"></span>
$$U_Z=\Bigl(Z+\frac12\Bigr)\frac{U_\mathrm{ref}}{8}. \tag{9.4}$$

A tree of switches, one level per bit, lets exactly one tap through. A __buffer__, an amplifier with the factor 1, outputs the voltage without drawing current from the chain, so that the divider stays unloaded. With $U_\mathrm{ref}=3.2$ V the step is 0.4 V, and $Z=5$ gives 2.2 V.

**Application: flash analog-to-digital converter.** The same chain also works in reverse. A __comparator__, a device that reports which of two voltages is higher, compares the input voltage with every tap, all at the same time. A __decoder__, a logic circuit, turns the reports into the three-bit number. For the numbers 0 to 7, seven thresholds are enough, here 0.2 to 2.6 V. An eighth threshold can report an overflow. At 1.3 V, three thresholds lie below; the converter outputs $Z=3$, which is $3\cdot0.4\,\mathrm{V}=1.2$ V, the nearest multiple of the step.

:::frage Doesn't the first resistor slow the current down, so that less arrives at the second?
No, current is not used up (Stage [1](strom-ist-bewegte-ladung.html#stufe-1)). The electrons do not pile up in front of $R_2$: otherwise the midpoint would charge up until both currents are equal. $R_2$ acts back on the whole circuit, because the one common current is set by $R_1+R_2$.
:::

:::aufgabe Exercise 9 ★ Designing a divider
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

3.3 V are to be derived from 12 V, with $R_2=3.3\,\mathrm{k\Omega}$. Calculate $R_1$. Which E24 values (8.2 and 9.1 k$\Omega$) lie next to it, and what voltage do they give?

</li>

<li>

A chain of $1$, $2$, $3$ and $6\,\mathrm{k\Omega}$ is connected to 24 V. Give the current and the partial voltages.

</li>

<li>

A 3-bit converter has $U_\mathrm{ref}=5$ V. What voltage does it output at $Z=6$?

</li>

</ol>

:::loesung
(a) $R_1=R_2\,(12-3.3)/3.3=8.7\,\mathrm{k\Omega}$. With $8.2\,\mathrm{k\Omega}$ the result is 3.44 V ($+4.3\,\%$), with $9.1\,\mathrm{k\Omega}$ it is 3.19 V ($-3.2\,\%$). (b) $R_\mathrm{tot}=12\,\mathrm{k\Omega}$, $I=2$ mA, partial voltages 2, 4, 6 and 12 V. (c) $U_6=6.5\cdot5\,\mathrm{V}/8=4.06$ V.
:::
:::
