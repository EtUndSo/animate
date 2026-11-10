---
title: Stage 1: Combining resistors
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1150300
summary: A network of resistors without a source has, at two terminals, a characteristic curve through the origin, so one number is enough.
tags: series-parallel circuit, total resistance, conductance
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A network of resistors without a source has, at two terminals, a characteristic curve through the origin, so one number is enough. This stage finds it by combining step by step.
:::

**The idea.** A __series-parallel circuit__ consists of series and parallel groups nested inside one another. Two resistors are in series if nothing else is connected to their common node. Then the same current flows through both, because the charge has nowhere to turn off. They are in parallel if they hang on the same two nodes. Then the same voltage lies across both. Each such group is itself a small one-port with a resistance as its characteristic curve. You replace it by this resistance, and the rest of the circuit notices nothing. You repeat this from the inside out.

:::abbildung et1/k5gruppe 1
Left, a load network of six resistors. The three stacked ones are in parallel and give 10 $\Omega$, and together with $R_\mathrm{c}$ in series 15 $\Omega$. Right, the network after these two steps.
:::

:::definition Definition 1.1 (Total resistance)
<span class="anker" id="satz-1-1"></span>

The __total resistance__ $R_\mathrm{AB}$ is the ratio $U_\mathrm{AB}/I_\mathrm{A}$ of a one-port without a source. For the network in Fig. [1](#abb-1),

<span class="anker" id="gl-1-1"></span>
$$R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{b}\parallel\bigl(R_\mathrm{c}+R_\mathrm{d}\parallel R_\mathrm{e}\parallel R_\mathrm{f}\bigr) =R_\mathrm{a}+\left[G_\mathrm{b}+\frac{1}{R_\mathrm{c}+\dfrac{1}{G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}}}\right]^{-1}. \tag{1.1}$$
:::

⁠**How to read it:** $R$ is a resistance in $\Omega$, $G=1/R$ its __conductance__ in siemens (S). In series you add resistances, in parallel you add conductances. That is why each parallel group appears as a sum of conductances in the second form. The square bracket with the exponent $-1$ inverts the result again. **Validity:** The method needs genuine groups. If a third branch hangs on an intermediate node, the two neighbors are no longer in series (Stages [2](symmetrie-nutzen.html#stufe-2) and [3](stern-und-dreieck.html#stufe-3)).

::::beispiel
With the values from Fig. [1](#abb-1): $G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}=50+33.3+16.7$ mS $=100$ mS, which is 10 $\Omega$. Adding $R_\mathrm{c}$ in series: 15 $\Omega$. In parallel with $R_\mathrm{b}$: $30\,\Omega\parallel15\,\Omega=10\,\Omega$. Adding $R_\mathrm{a}$ in series: $R_\mathrm{AB}=16\,\Omega$. Working backward gives the currents: with 8 V across A and B, 0.5 A flows. Across $R_\mathrm{a}$ the voltage drops by 3 V, leaving 5 V for the rest. Through $R_\mathrm{b}$ flows $5\,\mathrm{V}/30\,\Omega=166.7$ mA, through $R_\mathrm{c}$ flows $5\,\mathrm{V}/15\,\Omega=333.3$ mA. The sum is 500 mA.
::::

⁠**Limiting case:** For $R_\mathrm{b}\to0$, [(1.1)](#gl-1-1) becomes $R_\mathrm{AB}=R_\mathrm{a}=6\,\Omega$. The short circuit bypasses everything behind it; the charge takes the wire.

:::frage May I do the steps in any order?
No. A group often comes into being only once the inner group has been combined: in the initial diagram $R_\mathrm{c}$ and $R_\mathrm{b}$ are not in parallel, because the three stacked resistors hang between them. That is why you work from the group farthest from the terminals toward the terminals.
:::

:::aufgabe Exercise 1 ★ Changing the load network
<span class="anker" id="aufg-1"></span>

Start from the network in Fig. [1](#abb-1). What $R_\mathrm{AB}$ results if (a) $R_\mathrm{b}$ drops out through a broken wire, (b) $R_\mathrm{c}$ is short-circuited, (c) $R_\mathrm{d}$ is short-circuited, (d) $R_\mathrm{f}$ drops out? Before calculating, predict which of the four changes has the least effect.

:::loesung
Prediction: (d) has the least effect, because $R_\mathrm{f}$ is the largest resistor in its parallel group and carries the smallest current.

(a) $R_\mathrm{AB}=6\,\Omega+15\,\Omega=21\,\Omega$. (b) $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel10\,\Omega=13.5\,\Omega$. (c) The entire parallel group is bypassed: $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel5\,\Omega=10.29\,\Omega$. (d) $20\,\Omega\parallel30\,\Omega=12\,\Omega$, so $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel17\,\Omega=16.85\,\Omega$.
:::
:::
