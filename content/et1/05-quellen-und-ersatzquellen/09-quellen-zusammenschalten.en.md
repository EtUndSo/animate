---
title: Stage 7: Interconnecting sources
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1150900
summary: One source is often not enough.
tags: circulating current
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
One source is often not enough. A series connection raises the voltage, a parallel connection the current. This stage works out both and names the danger.
:::

**The idea.** In series, the same current flows through both sources, and their terminal voltages add at every current. In parallel, the same voltage lies across both, and their currents add at every voltage. That is why you calculate the series connection in the voltage-source form and the parallel connection in the current-source form. Two straight lines again give a straight line, and hence again a real source.

:::satz Theorem 7.1 (Interconnecting real sources)
<span class="anker" id="satz-7-1"></span>

Two sources in series or in parallel, respectively, act like one:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{eq}=U_\mathrm{q1}+U_\mathrm{q2},\quad R_\mathrm{eq}=R_\mathrm{q1}+R_\mathrm{q2} \qquad\text{or}\qquad I_\mathrm{eq}=I_\mathrm{q1}+I_\mathrm{q2},\quad G_\mathrm{eq}=G_\mathrm{q1}+G_\mathrm{q2}. \tag{7.1}$$

For the parallel connection, in voltage-source form this means

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{eq}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}},\qquad R_\mathrm{eq}=R_\mathrm{q1}\parallel R_\mathrm{q2}. \tag{7.2}$$
:::

⁠**How to read it:** The voltage in [(7.2)](#gl-7-2) is a weighted mean, and the source with the lower resistance counts more. Two identical sources give $U_\mathrm{q}$ and $R_\mathrm{q}/2$ in parallel, $2U_\mathrm{q}$ and $2R_\mathrm{q}$ in series. **Validity:** Series connections of voltage sources and parallel connections of current sources are technically uncritical. Parallel voltage sources need equal voltages or sufficient internal resistance: for $U_\mathrm{q1}\neq U_\mathrm{q2}$ a __circulating current__ flows even without a load,

<span class="anker" id="gl-7-3"></span>
$$I_\mathrm{circ}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}. \tag{7.3}$$

It runs out of the stronger source and into the weaker one. Two ideal voltage sources with different voltages must not be connected in parallel, nor two ideal current sources with different currents in series: the model then has no solution.

:::herleitung Parallel in the current-source form
Both sources have the voltage $U_\mathrm{AB}$, and the node rule adds their currents: $I_\mathrm{A}=(I_\mathrm{q1}-G_\mathrm{q1}U_\mathrm{AB})+(I_\mathrm{q2}-G_\mathrm{q2}U_\mathrm{AB})=(I_\mathrm{q1}+I_\mathrm{q2})-(G_\mathrm{q1}+G_\mathrm{q2})U_\mathrm{AB}$. This is again the form from [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1). With [(6.1)](spannungsquelle-oder-stromquelle.html#gl-6-1), [(7.2)](#gl-7-2) follows. In series, the mesh rule adds the voltages in the same way. The circulating current is the loop voltage $U_\mathrm{q1}-U_\mathrm{q2}$ divided by the resistance of the loop.
:::

:::abbildung et1/k5zusammen 8
Left, two identical batteries in parallel. Right, the characteristic curves: in parallel the open-circuit voltage stays and the short-circuit current doubles. In series the open-circuit voltage doubles and the short-circuit current stays. The dots show the operating points with 16 $\Omega$.
:::

::::beispiel
Two batteries from the reference model. In parallel: 9 V, 1 $\Omega$, $I_\mathrm{SC}=9$ A. Current form as a check: $4.5+4.5=9$ A and $0.5+0.5=1$ S. In series: 18 V, 4 $\Omega$, $I_\mathrm{SC}=4.5$ A. Into 16 $\Omega$ the parallel connection delivers 8.47 V and 0.529 A, the series connection 14.4 V and 0.9 A (Fig. [8](#abb-8)). The parallel connection brings little here, because 2 $\Omega$ is small compared with 16 $\Omega$.

If one of the batteries is discharged to 8 V, then by [(7.3)](#gl-7-3) a current of $1\,\mathrm{V}/4\,\Omega=0.25$ A circulates in the open circuit. Both terminals are at 8.5 V, also according to [(7.2)](#gl-7-2).
::::

⁠**Limiting case:** With only 10 m$\Omega$ of internal resistance each, it would be 50 A. That is why large battery cells are connected in parallel only at equal voltage. For $U_\mathrm{q1}=U_\mathrm{q2}$ the circulating current vanishes.

:::frage Do two parallel batteries give more voltage?
In the open circuit no, both supply 9 V. Under load a little, because the current divides between two internal resistances and only half as much drops internally. The real gain is a short-circuit current twice as large and twice the amount of charge.
:::

:::aufgabe Exercise 8 ★★ Old and new battery
<span class="anker" id="aufg-8"></span>

A new rechargeable battery (12.6 V, 0.1 $\Omega$) is connected in parallel with an old one (11.8 V, 0.3 $\Omega$). (a) How large is the circulating current? What equivalent source results? (b) A load draws 10 A. What voltage arises, and what does each battery deliver? (c) Above what load current does the old battery deliver any current at all? What happens below that?

:::loesung
(a) $I_\mathrm{circ}=\frac{0.8\,\mathrm{V}}{0.4\,\Omega}=2$ A. $U_\mathrm{eq}=\frac{10\,\mathrm{S}\cdot12.6\,\mathrm{V}+3.33\,\mathrm{S}\cdot11.8\,\mathrm{V}}{13.33\,\mathrm{S}}=12.4$ V, $R_\mathrm{eq}=0.1\,\Omega\parallel0.3\,\Omega=75$ m$\Omega$. Check: $12.6\,\mathrm{V}-0.1\,\Omega\cdot2\,\mathrm{A}=12.4$ V.

(b) $U=12.4\,\mathrm{V}-75\,\mathrm{m\Omega}\cdot10\,\mathrm{A}=11.65$ V. New: $\frac{12.6-11.65}{0.1}\,\mathrm{A}=9.5$ A. Old: $\frac{11.8-11.65}{0.3}\,\mathrm{A}=0.5$ A. Sum 10 A.

(c) The old battery delivers only once $U<11.8$ V, that is, for $I_\mathrm{L}>\frac{12.4-11.8}{0.075}\,\mathrm{A}=8$ A. Below that, current flows into it, and the new battery charges it.
:::
:::
