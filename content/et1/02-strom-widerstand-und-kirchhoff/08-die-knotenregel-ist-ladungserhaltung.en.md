---
title: Stage 7: The node rule is charge conservation
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Current, Resistance and Kirchhoff's Laws
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Chapter 2: Current, Resistance and Kirchhoff's Laws
order: 1120800
summary: The first kind of equation: What does the conservation of charge demand at a node?
tags: 
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The first kind of equation: What does the conservation of charge demand at a node?
:::

**The idea.** A node is a piece of wire. If more flows in than out, charge collects on it and its potential rises. This lowers the voltage across the incoming resistors and raises it across the outgoing ones. The inflow falls and the outflow rises until both are equal. This self-regulation takes place in nanoseconds. It is the mechanism behind the rule: the node settles at exactly the potential at which nothing is left stuck.

:::satz Theorem 7.1 (Node rule, Kirchhoff's first law)
<span class="anker" id="satz-7-1"></span>

The sum of all currents flowing into a node is zero at every instant. Equivalently, the sum of the incoming currents equals the sum of the outgoing currents:

<span class="anker" id="gl-7-1"></span>
$$\sum_{\nu=1}^{N}I_\nu=0\quad\text{(all arrows toward the node)},\qquad\sum I_\mathrm{in}=\sum I_\mathrm{out}. \tag{7.1}$$

For a network with $k$ nodes, $k-1$ of these equations are independent.
:::

⁠**How to read it:** The arrows can be chosen freely. If all point toward the node, at least one of the currents must be negative, or all are zero. With mixed arrows, incoming ones count as positive and outgoing ones as negative. **Validity:** The node must not store any appreciable charge. That holds as long as the currents change slowly compared with the equalization time. The derivation gives a number for this.

:::abbildung et1/k2knoten 8
Left: node with two incoming and three outgoing currents, sum 7 mA each. Right: the rule also holds for a closed surface around part of the network, here around $K_2$, $K_3$ and $R_\mathrm e$. The current in $R_\mathrm e$ stays inside and does not count.
:::

:::herleitung Node rule from charge conservation
For the charge $Q_\mathrm K$ on the node, $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$, because charge neither arises nor disappears. An estimate with [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) shows how small $Q_\mathrm K$ stays: a metal sphere with a radius of 1 cm has the potential $\varphi=k_\mathrm C\,Q/r$ with the Coulomb constant $k_\mathrm C=8.99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$. For 9 V, $Q=10$ pC is enough. A surplus of 3 mA supplies that in 3.3 ns. That is why $\mathrm{d} Q_\mathrm K/\mathrm{d} t$ is negligible compared with the currents, and $\sum I_\nu=0$ remains.
:::

**Why one equation is superfluous.** Each branch connects two nodes. Its current therefore appears in exactly two node equations, once with $+$ (incoming) and once with $-$ (outgoing). If all $k$ equations are added, all the currents cancel. So one equation follows from the others, and any selection of $k-1$ equations is independent.

::::beispiel
All the current arrows in the network point in the direction of the actual current: from $K_1$ down through the resistors, $I_\mathrm e$ from $K_2$ to $K_3$, $I_0$ through the source from $K_4$ to $K_1$. The node equations are

$$\begin{aligned} K_1:&\quad +I_0-I_\mathrm a-I_\mathrm c=0, & K_2:&\quad +I_\mathrm a-I_\mathrm b-I_\mathrm e=0,\\ K_3:&\quad +I_\mathrm c-I_\mathrm d+I_\mathrm e=0, & K_4:&\quad -I_0+I_\mathrm b+I_\mathrm d=0. \end{aligned}$$

The sum of the first three is $I_0-I_\mathrm b-I_\mathrm d=0$, the fourth equation with the opposite sign. If only $K_2$ and $K_3$ are added, $I_\mathrm e$ drops out, and the closed surface from Fig. [8](#abb-8) remains: $I_\mathrm a+I_\mathrm c=I_\mathrm b+I_\mathrm d$. **Check:** At a point with only two branches, $I_1=I_2$ follows. The same current flows through components in series.
::::

:::frage Does the rule also hold if a capacitor is connected to a node?
Yes. The current to the plate is a branch current like any other; the charge collects not on the node, but on the plate. [Chapter 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html) deals with this.
:::

:::aufgabe Exercise 7 ★★ Applying the node rule
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Four current arrows point toward the node: $I_1=5$ mA, $I_2=-2$ mA, $I_3=-1$ mA. How large is $I_4$, and in which direction does it really flow?

</li>

<li>

Show from the node equations of the network that $I_0=I_\mathrm b+I_\mathrm d$. Which closed surface belongs to this?

</li>

<li>

Prediction: A surplus of only 1 µ A stays on the sphere from the derivation for 1 s. What potential would it have? Why does this not happen?

</li>

</ol>

:::loesung
(a) $5-2-1+I_4=0$, so $I_4=-2$ mA: 2 mA flow out of the node.

(b) Adding $K_1$, $K_2$, $K_3$ gives $I_0-I_\mathrm b-I_\mathrm d=0$. This is the closed surface around $K_1$, $K_2$, $K_3$ or, equivalently, the equation of $K_4$. With numbers: $4=1+3$.

(c) $Q=1\,\mu\text{C}$ gives $\varphi=k_\mathrm C\,Q/r=0.9$ MV. Long before this value would be reached, the rising potential drives the surplus away. That is the self-regulation.
:::
:::
