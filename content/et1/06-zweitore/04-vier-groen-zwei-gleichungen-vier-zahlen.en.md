---
title: Stage 2: Four quantities, two equations, four numbers
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160400
summary: Four port quantities are four unknowns.
tags: two-port functions, symmetric arrow system, chain-arrow system, mixed arrow system
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Four port quantities are four unknowns. This stage shows why the two-port contributes exactly two equations and why they contain only four numbers.
:::

**The idea.** Source and load each supply one equation between the voltage and the current of their port. Two are missing, and the two-port supplies them. If you specify two port quantities, say both currents, all the currents and voltages inside are fixed, and so are the other two port quantities. The specified quantities are the causes, the others the effects. If the two-port is linear and contains no independent sources, superposition from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) applies: Each effect is the sum of the part due to the first cause and the part due to the second cause, each part proportional to its cause. Two effects times two causes give four factors.

:::satz Theorem 2.1 (Two-port equations)
<span class="anker" id="satz-2-1"></span>

A time-invariant two-port is completely described by two __two-port functions__, for example

<span class="anker" id="gl-2-1"></span>
$$I_1=f_1(U_1,U_2),\quad I_2=g_1(U_1,U_2)\qquad\text{or}\qquad U_1=f_2(I_1,I_2),\quad U_2=g_2(I_1,I_2). \tag{2.1}$$

If it is linear and free of independent sources, then for effects $y_1,y_2$ and causes $x_1,x_2$

<span class="anker" id="gl-2-2"></span>
$$y_1=p_{11}x_1+p_{12}x_2,\qquad y_2=p_{21}x_1+p_{22}x_2. \tag{2.2}$$
:::

⁠**How to read it:** The first digit of a parameter names the effect, the second the cause. The parameters depend only on the two-port, not on source or load. Four quantities can be split into two causes and two effects in six ways. The four forms of this chapter are the usual ones. **Validity:** [(2.1)](#gl-2-1) also holds for nonlinear two-ports, then as curves. For the transistor, this describes either the behavior for DC quantities or the signal behavior for small AC quantities. A transformer with separate windings transmits only time-varying quantities. [(2.2)](#gl-2-2) requires linearity.

**Reference arrows.** To make the signs unique, a convention is needed (Fig. [3](#abb-3)). In the __symmetric arrow system__, also called the mathematical sign convention, the passive sign convention from [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) applies at both ports: The current arrows point into the two-port. In the __chain-arrow system__, also called the technical arrow system, it applies only at the input; at the output the active sign convention applies: The output current points out, toward the load. This chapter uses the __mixed arrow system__: $I_1$ and $I_2$ always point in. Where the chain form needs the current flowing out, it writes it explicitly as $-I_2$. A load therefore gives a negative $I_2$ in normal operation.

:::abbildung et1/k6zaehlpfeile 3
The three arrow systems. Left, symmetric: Both currents point into the two-port. Center, chain arrows: The output current points toward the load. Right, mixed, as in this chapter: $I_2$ stays defined as on the left, and the current to the load is called $-I_2$.
:::

**Example.** At the center point of the T two-port, $I_1$ and $I_2$ meet, and their sum flows through $R_\mathrm{b}$. The mesh rule gives

$$U_1=R_\mathrm{a}I_1+R_\mathrm{b}(I_1+I_2)=35\,\Omega\cdot I_1+20\,\Omega\cdot I_2,\qquad U_2=R_\mathrm{c}I_2+R_\mathrm{b}(I_1+I_2)=20\,\Omega\cdot I_1+40\,\Omega\cdot I_2.$$

The term $20\,\Omega\cdot I_2$ in $U_1$ is the mechanism: The current of port 2 runs through $R_\mathrm{b}$, raises the potential of the center point there, and port 1 sees this rise. With $I_1=250$ mA and $I_2=-50$ mA, this gives $U_1=8.75\,\mathrm{V}-1\,\mathrm{V}=7.75$ V and $U_2=5\,\mathrm{V}-2\,\mathrm{V}=3$ V. **Limiting case:** Without causes, $I_1=I_2=0$, both voltages are zero, as a two-port without sources of its own requires. With an independent source inside, a constant would be added to each equation.

⁠**In short:** Two quantities are free, and each of the other two is a sum with two fixed factors.

:::frage Who decides which two quantities are the causes, the network?
No, the calculation does. Physically, everything settles at the same time. The equations describe a relation between four quantities, and you may rearrange it around any two of them, provided these can really be chosen freely. “Cause” here means: It stands to the right of the equals sign.
:::

:::aufgabe Exercise 2 ★ Predicting a black box
<span class="anker" id="aufg-2"></span>

An unknown linear two-port without sources of its own gives two measurements. With $I_1=200$ mA, $I_2=0$, the result is $U_1=8$ V, $U_2=3$ V. With $I_1=0$, $I_2=100$ mA, the result is $U_1=1.5$ V, $U_2=3$ V.

<ol class="al">

<li>

Without any further measurement, predict $U_1$ and $U_2$ for $I_1=100$ mA, $I_2=200$ mA.

</li>

<li>

What results for $I_1=100$ mA, $I_2=-50$ mA? What stands out about $U_2$?

</li>

</ol>

:::loesung
The measurements give $Z_{11}=8\,\mathrm{V}/200\,\mathrm{mA}=40\,\Omega$, $Z_{21}=15\,\Omega$, $Z_{12}=1.5\,\mathrm{V}/100\,\mathrm{mA}=15\,\Omega$, $Z_{22}=30\,\Omega$. (a) $U_1=40\,\Omega\cdot0.1\,\mathrm{A}+15\,\Omega\cdot0.2\,\mathrm{A}=7$ V, $U_2=15\,\Omega\cdot0.1\,\mathrm{A}+30\,\Omega\cdot0.2\,\mathrm{A}=7.5$ V. (b) $U_1=4\,\mathrm{V}-0.75\,\mathrm{V}=3.25$ V, $U_2=1.5\,\mathrm{V}-1.5\,\mathrm{V}=0$. So this pair of currents belongs to a short-circuited port 2.
:::
:::
