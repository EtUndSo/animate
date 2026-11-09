---
title: Stage 8: Superposition
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Sources and Equivalent Sources
order: 1151000
summary: When there are several sources at different places in the network, groups alone do not help.
tags: superposition method, independent, sensitivity
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
When there are several sources at different places in the network, groups alone do not help. The __superposition method__ splits the problem into one calculation per source.
:::

**The idea.** A network is determined by three kinds of equations: node rule, mesh rule, Ohm's law. None of them contains a product or a square of currents and voltages, as long as $R$ is fixed. Such equations are linear. If such a system has the solution $x'$ for one source and the solution $x''$ for another, then $x'+x''$ is the solution when both sources act at the same time. Substitution shows this: every equation adds term by term. So each source drives its own current through the network as if the other were not there, and the currents add in every branch.

:::satz Theorem 8.1 (Superposition)
<span class="anker" id="satz-8-1"></span>

In a linear network with $n$ independent voltage sources and $m$ independent current sources, every branch voltage and every branch current satisfies

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
$$\begin{aligned} U_\mathrm{AB}&=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m},\\ I_\mathrm{CD}&=Y_1U_\mathrm{q1}+\dots+Y_nU_{\mathrm{q}n}+b_1I_\mathrm{q1}+\dots+b_mI_{\mathrm{q}m}. \end{aligned} \tag{8.1|8.2}$$

The coefficients depend only on the resistors, not on the sources.
:::

⁠**How to read it:** A source is __independent__ if its value depends on no quantity in the network. $a_k$ is the voltage gain from source $k$ to the voltage $U_\mathrm{AB}$, without a unit: this is how many volts $U_\mathrm{AB}$ changes per volt of the source. It is also called the __sensitivity__. $Z_k$ in $\Omega$ is the transfer resistance (the transimpedance) from a current source to this voltage. Correspondingly, $Y_k$ in S and the current gain $b_k$ describe the current between two nodes C and D. $U_\mathrm{AB}$ and $I_\mathrm{CD}$ stand for any voltage and any current in the network. **Validity:** only for linear networks and only for voltages and currents.

**The procedure.**

<ol>

<li>

Turn off all sources except one. An ideal voltage source with the value zero forces equal potentials at its terminals, which is what a wire does: it becomes a **short circuit**. An ideal current source with the value zero forces the current zero, which is what a gap does: it becomes **open terminals**. Internal resistances of real sources stay in the network.

</li>

<li>

Calculate the partial effect of this one source. Usually only a voltage or current divider remains.

</li>

<li>

Repeat for every source and add all the partial effects with the correct signs.

</li>

</ol>

:::abbildung et1/k5ueberlagerung 9
Network N and its two partial circuits. Center: the current source is open, leaving a voltage divider. Right: the voltage source is a wire, and the current source feeds $R_1$ and $R_2$ in parallel. Terminals A and B are open.
:::

::::beispiel
We want $U_\mathrm{AB}$ in N with the terminals open (Fig. [9](#abb-9)). Partial circuit 1: voltage divider, $U'=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}=\frac13\cdot18\,\mathrm{V}=6$ V. Partial circuit 2: $U''=(R_1\parallel R_2)\,I_\mathrm{q2}=2\,\Omega\cdot1.5\,\mathrm{A}=3$ V. Sum: $U_\mathrm{AB}=9$ V. The coefficients are therefore $a=\frac13$ for $U_\mathrm{q1}$ and $Z=2\,\Omega$ for $I_\mathrm{q2}$. **Check** with the node rule at A: through $R_1$ come $(18-9)\,\mathrm{V}/6\,\Omega=1.5$ A, plus 1.5 A from the current source, and through $R_2$ go off $9\,\mathrm{V}/3\,\Omega=3$ A. The branch currents superpose too: in $R_1$ flow $2$ A from partial circuit 1 and $-0.5$ A from partial circuit 2.
::::

⁠**Limiting case:** If you double both sources, $U_\mathrm{AB}$ doubles to 18 V, because the coefficients stay the same.

:::herleitung The coefficients of N
With the terminals open, the node rule at A reads $(U_\mathrm{q1}-U_\mathrm{AB})/R_1+I_\mathrm{q2}=U_\mathrm{AB}/R_2$. Solved for the voltage we want:

$$U_\mathrm{AB}=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}+\frac{R_1R_2}{R_1+R_2}\,I_\mathrm{q2}.$$

This is the form [(8.1)](#gl-8-1): each term belongs to one source, and the coefficients contain only resistors.
:::

**The limit: power.** The power in a resistor is quadratic in the voltage, $P=UI=U^2/R$ ([Part 7](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). In $R_2$, adding would give $(6\,\mathrm{V})^2/3\,\Omega+(3\,\mathrm{V})^2/3\,\Omega=15$ W. The truth is $(9\,\mathrm{V})^2/3\,\Omega=27$ W. The cross term $2U'U''/R_2=12$ W is missing. Powers must not be superposed; voltages and currents may. An exception comes later: for alternating quantities of different frequencies, the cross term vanishes in the time average. Nor does superposition hold once a diode sits in the network ([Part 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::frage Why must I not take a turned-off voltage source out of the network?
Because zero volts does not turn into “nothing”. The source remains part of the line; it just no longer holds a voltage. If you take it out, you interrupt the current path through it. That would be the case of the current source, not of the voltage source.
:::

:::aufgabe Exercise 9 ★★ Two sources, one load
<span class="anker" id="aufg-9"></span>

From node C, three branches lead to the common ground: $R_3=4\,\Omega$ directly, $R_\mathrm{s}=2\,\Omega$ in series with $U_\mathrm{s}=12$ V, and $R_\mathrm{t}=4\,\Omega$ in series with $U_\mathrm{t}=6$ V (both plus terminals point toward C). (a) Calculate the voltage $U_3$ across $R_3$ by superposition and generally as a formula. Check with the node rule. (b) Compare the true power in $R_3$ with the sum of the partial powers. (c) What is the sensitivity of $U_3$ to $U_\mathrm{t}$? What does this give for $U_\mathrm{t}=8$ V, without recalculating everything?

:::loesung
(a) $U_\mathrm{t}$ turned off: $R_\mathrm{t}\parallel R_3=2\,\Omega$, divider $U_3'=\frac{2}{2+2}\cdot12\,\mathrm{V}=6$ V. $U_\mathrm{s}$ turned off: $R_\mathrm{s}\parallel R_3=\frac43\,\Omega$, divider $U_3''=\frac{4/3}{4+4/3}\cdot6\,\mathrm{V}=1.5$ V. So $U_3=7.5$ V. In general:

$$U_3=\frac{R_\mathrm{t}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{s}+\frac{R_\mathrm{s}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{t}.$$

Node rule: $\frac{12-7.5}{2}\,\mathrm{A}+\frac{6-7.5}{4}\,\mathrm{A}=2.25\,\mathrm{A}-0.375\,\mathrm{A}=1.875$ A, and $7.5\,\mathrm{V}/4\,\Omega=1.875$ A. The 6 V source absorbs current.

(b) Partial powers: 9 W and 0.5625 W, sum 9.56 W. True: $(7.5\,\mathrm{V})^2/4\,\Omega=14.06$ W.

(c) $a_\mathrm{t}=\frac{1.5\,\mathrm{V}}{6\,\mathrm{V}}=\frac14$. For 8 V: $U_3=6\,\mathrm{V}+\frac14\cdot8\,\mathrm{V}=8$ V.
:::
:::
