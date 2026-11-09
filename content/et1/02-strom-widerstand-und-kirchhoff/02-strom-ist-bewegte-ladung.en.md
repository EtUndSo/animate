---
title: Stage 1: Current is moving charge
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Current, Resistance and Kirchhoff's Laws
order: 1120200
summary: Part 1 considered charges at rest or flying individually.
tags: charge density, electric current, circuit, steady
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) considered charges at rest or flying individually. In a wire, countless charges move together. This stage gives this motion two measures.
:::

**The idea.** Stand at one spot of the conductor and measure how much charge passes per second. That depends on three things: how densely the charge sits, how fast it moves and how large the cross section is. In the time $\Delta t$, exactly the charge that was at most the distance $v\,\Delta t$ away beforehand passes through the area (Fig. [1](#abb-1)).

:::abbildung et1/k2strom 1
Charge carriers with the velocity $v$ in a conductor. All the charge in the shaded section passes through the area $A$ in the time $\Delta t$. The section has the volume $A\,v\,\Delta t$.
:::

:::definition Definition 1.1 (Current and current density)
<span class="anker" id="satz-1-1"></span>

The __charge density__ $q=\Delta Q/\Delta V$ is the charge per volume. The __electric current__ (current for short) is the charge that passes through an area per time. The current density is the current per area:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} i&=\lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t}=\frac{\mathrm{d} Q}{\mathrm{d} t},\qquad I=q\,v\,A,\qquad [I]=\mathrm{C/s}=\mathrm A,\\ j&=\frac IA=q\,v,\qquad\vec j=q\,\vec v. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**How to read it:** $i$ is the time-dependent current, $I$ the constant one, in amperes: 3 mA in the reference model, 20 mA in a light-emitting diode, 16 A in a household line. $q$ has the unit $\mathrm{C/m^3}$. For the free electrons in copper, $q=-n\,e=-1.36\cdot10^{10}\,\mathrm{C/m^3}$. $j$ has the unit $\mathrm{A/m^2}$; household lines carry around $10\,\mathrm{A/mm^2}$. The vector $\vec j$ points in the direction of $\vec v$ for $q>0$ and opposite to it for $q<0$. **Validity:** $I=q\,v\,A$ assumes that $q$ and $v$ are the same across $A$ and that $v$ is perpendicular to $A$.

:::herleitung Current from density and velocity
Let the area be $A=\Delta x\,\Delta y$. The shaded section has the volume $\Delta V=\Delta x\,\Delta y\,\Delta z$ with $\Delta z=v\,\Delta t$. It contains the charge $\Delta Q=q\,\Delta V=q\,A\,v\,\Delta t$, which passes through $A$ in the time $\Delta t$. So $\Delta Q/\Delta t=q\,v\,A$.
:::

**When does current flow continuously?** Two conditions must be met. First, the circuit needs a source, such as a battery or a power supply. It supplies energy, not charge: the charge carriers are already in the conductor; the source only drives them around the circuit. Second, the __circuit__ must be closed, that is, a path that returns to itself. Otherwise charge piles up at a gap, its field cancels the driving field, and the current ends. A current that is constant in time in a closed circuit is called __steady__.

::::beispiel
In the reference model, 3 mC per second pass through the wire, which is $3\,\mathrm{mC}/e=1.87\cdot10^{16}$ electrons. The current density is $j=3\,\mathrm{mA}/0.5\,\mathrm{mm^2}=6\,\mathrm{mA/mm^2}$. One meter of wire contains the free charge $n\,e\,A=6800$ C. So the entire charge that a rectangular battery moves in its lifetime (around 1800 C) already sits in 26 cm of this wire. **Check:** For $v=0$, $I=0$, no matter how much charge sits in the wire. Twice the area at the same $v$ gives twice the current, because that is two wires side by side.
::::

:::frage Are the electrons used up in the load?
No. Charge is conserved; as many electrons per second come out of a component as go in. What is used up is energy: each coulomb gives its energy per charge, the voltage, to the component and moves on at a lower potential.
:::

:::aufgabe Exercise 1 ★ Current, charge, current density
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

A light-emitting diode carries 20 mA for 5 min. How much charge passes through it, and how many electrons is that?

</li>

<li>

A cable with a cross section of $1.5\,\mathrm{mm^2}$ carries 16 A. How large is $j$ in $\mathrm{A/mm^2}$?

</li>

<li>

In which direction does $\vec j$ point in a wire in which electrons move to the right?

</li>

</ol>

:::loesung
(a) $Q=I\,t=20\,\mathrm{mA}\cdot300\,\mathrm{s}=6$ C, which is $6\,\mathrm{C}/e=3.7\cdot10^{19}$ electrons. (b) $j=16\,\mathrm{A}/1.5\,\mathrm{mm^2}=10.7\,\mathrm{A/mm^2}$. (c) To the left: for electrons, $q<0$, so $\vec j=q\,\vec v$ points against $\vec v$.
:::
:::
