---
title: Stage 5: Real sources and the operating point
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1150700
summary: A battery does not hold its voltage under load.
tags: equivalent circuit, real voltage source, real current source, load line, operating point
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
A battery does not hold its voltage under load. This stage shows why, and finds the point on the characteristic curve that a load sets.
:::

**The idea.** In a battery, chemistry drives charge and supplies a fixed energy per coulomb for this, the source voltage. But the current has to pass through the battery itself: ions migrate through the electrolyte solution, electrons through electrodes and connections. In the process energy is lost as heat, just as in a resistor. Only the remainder is left at the terminals. The greater the current, the greater the internal drop. This drop is proportional to the current, so the characteristic curve is a falling straight line.

:::abbildung et1/k5arbeitsgerade 6
Left, the real voltage source with a load. Right, the characteristic curve of the source (blue) from open circuit to short circuit and the load line of each load. The intersection is the operating point: with 16 $\Omega$ at 0.5 A and 8 V, with 2 $\Omega$ at 2.25 A and 4.5 V.
:::

:::definition Definition 5.1 (Real sources)
<span class="anker" id="satz-5-1"></span>

An __equivalent circuit__ is a circuit of ideal elements that behaves like the real component at the terminals. The __real voltage source__ is an ideal voltage source in series with $R_\mathrm{q}$, the __real current source__ an ideal current source in parallel with $G_\mathrm{q}$:

<span class="anker" id="gl-5-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}, \qquad\qquad I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}. \tag{5.1}$$
:::

⁠**How to read it:** $U_\mathrm{q}$ is the open-circuit voltage. $R_\mathrm{q}$ is the internal or source resistance in $\Omega$: around 2 $\Omega$ for a 9 V battery, 10 m$\Omega$ for a car battery. $I_\mathrm{q}$ is the short-circuit current, $G_\mathrm{q}$ the source conductance in S. The first equation is the mesh rule in the equivalent circuit, the second the node rule: $G_\mathrm{q}U_\mathrm{AB}$ branches off from $I_\mathrm{q}$, and the rest goes outside. **Validity:** The straight line holds as long as $R_\mathrm{q}$ does not depend on the current. Real batteries deviate at large currents and with age.

**The load line.** A load imposes a second equation, $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$. This straight line through the origin is called the __load line__. Both equations must hold at once. That is possible only at the intersection, the __operating point__. Equating $U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}=R_\mathrm{L}I_\mathrm{A}$ gives:

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}},\qquad U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}. \tag{5.2}$$

The mechanism behind it: if the source delivered more current than the load takes, charge would accumulate at terminal A and its potential would rise. Then the current of the source would fall and the current of the load would rise. This continues until the two currents are equal.

::::beispiel
With 16 $\Omega$, $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0.5$ A and $U_\mathrm{AB}=8$ V, and 1 V drops internally. With 2 $\Omega$ it is 2.25 A and 4.5 V. Both points lie on the line: $9\,\mathrm{V}-2\,\Omega\cdot2.25\,\mathrm{A}=4.5$ V. Their separation shows the internal resistance as a slope: $\Delta U_\mathrm{AB}/\Delta I_\mathrm{A}=3.5\,\mathrm{V}/(-1.75\,\mathrm{A})=-2\,\Omega$.
::::

⁠**Limiting cases:** For $R_\mathrm{L}\to\infty$, [(5.2)](#gl-5-2) gives the open circuit $U_\mathrm{AB}=U_\mathrm{q}$, for $R_\mathrm{L}\to0$ the short-circuit current $I_\mathrm{SC}=U_\mathrm{q}/R_\mathrm{q}=4.5$ A. For $R_\mathrm{q}\to0$ the ideal voltage source remains. A nonlinear load can be treated the same way: its characteristic is then a curve, and the intersection is still the solution ([Chapter 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::ltspice The characteristic curve of the battery
⁠**Draw:** `voltage` with 9 from `q` to ground, `res` with 2 from `q` to `a`. As a load, a current source `current` named `I1` from `a` to ground.

⁠**Directive:** `.dc I1 0 4.5 0.05`

⁠**What you see:** `V(a)` falls as a straight line from 9 V at 0 A to 0 V at 4.5 A. At 0.5 A it reads 8 V, at 2.25 A it reads 4.5 V, the points from Fig. [6](#abb-6). For Exercise [6](#aufg-6), set the values 12.6 and 0.01 and run up to 200 A (`.dc I1 0 200 1`). At 150 A and at 20 A you read off your terminal voltages.
:::

:::frage Why does the meter show 9 V on a battery even though it has 2 $\Omega$ inside?
Because it draws hardly any current ([Chapter 4](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). With an input resistance of 10 M$\Omega$, 0.9 µ A flows, and 1.8 µ V drops internally. You are practically measuring the open circuit. The internal resistance shows up only under load.
:::

:::aufgabe Exercise 6 ★ The lights during starting
<span class="anker" id="aufg-6"></span>

A car battery has 12.6 V and 10 m$\Omega$. The starter motor acts like 74 m$\Omega$. (a) Calculate the current and terminal voltage during starting. (b) What would the short-circuit current be? (c) The lights alone draw 20 A. What is the terminal voltage then, and hence what is their resistance? (d) What is the terminal voltage when lights and starter motor run at the same time? Why do the lights get dimmer?

:::loesung
(a) $I_\mathrm{A}=12.6\,\mathrm{V}/84\,\mathrm{m\Omega}=150$ A, $U_\mathrm{AB}=12.6\,\mathrm{V}-10\,\mathrm{m\Omega}\cdot150\,\mathrm{A}=11.1$ V.

(b) $I_\mathrm{SC}=12.6\,\mathrm{V}/10\,\mathrm{m\Omega}=1260$ A.

(c) $U_\mathrm{AB}=12.6\,\mathrm{V}-0.2\,\mathrm{V}=12.4$ V, so $R=12.4\,\mathrm{V}/20\,\mathrm{A}=0.62\,\Omega$.

(d) Lights and starter motor in parallel: $0.62\,\Omega\parallel74\,\mathrm{m\Omega}=66.1\,\mathrm{m\Omega}$. Voltage divider with 10 m$\Omega$: $U_\mathrm{AB}=10.94$ V. The battery delivers 165.6 A, and the lights receive 17.65 A instead of 20 A. The large current of the starter motor produces an internal drop of 1.66 V, which the lights feel as well. Their power falls from 248 W to 193 W.
:::
:::
