---
title: Stage 1: How many quantities are free?
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Mesh Current and Node Voltage Analysis
order: 1180300
summary: Part 2 showed that a network has 2z unknowns and 2z equations.
tags: 
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) showed that a network has $2z$ unknowns and $2z$ equations. This stage shows why two much smaller numbers are enough for the calculation.
:::

**The idea.** A tree ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) connects all nodes with $k-1$ branches; the remaining $m=z-k+1$ branches are link branches. If you know the voltages of the tree branches, you know all voltages: each link branch closes exactly one mesh with tree branches, and the mesh rule gives its voltage. If you know the currents of the link branches, you know all currents: at the end of the tree, a tree branch hangs alone among link branches, the node rule gives its current, and so it goes on branch by branch. So of $z$ currents you may specify only $m$, of $z$ voltages only $k-1$.

:::satz Theorem 1.1 (Free quantities of a network)
<span class="anker" id="satz-1-1"></span>

The $z$ branch currents of a connected network must satisfy $k-1$ independent node equations, the $z$ branch voltages $z-k+1$ independent mesh equations. Therefore

<span class="anker" id="gl-1-1"></span>
$$m=z-k+1\ \text{currents}\qquad\text{and}\qquad k-1\ \text{voltages} \tag{1.1}$$

can be chosen freely. All other currents and voltages follow from Kirchhoff.
:::

⁠**How to read it:** “Can be chosen freely” means: you can specify the values without violating a Kirchhoff rule. $z$ counts the branches as in [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html); in English books the number is often called $b$ (for *branch*). **Validity:** The count depends only on the graph, not on the components. It also holds for nonlinear components.

:::abbildung et1/k8netz 1
The model network. Three nodes (red), six branches. The branch on the left contains the battery and $R_1$ in series, because nothing branches off between them. Node 0 is the entire lower line.
:::

::::beispiel
The network in Fig. [1](#abb-1) has $k=3$ and $z=6$, so $m=4$:

| Approach | Unknowns | Equations |
|---|---|---|
| all currents and voltages | 12 | 6 components, 2 nodes, 4 meshes |
| Ohm's law substituted | 6 | 2 nodes, 4 meshes |
| mesh currents | 4 | 4 meshes; the current source fixes one value, 3 remain |
| node voltages | 2 | 2 nodes |
::::

⁠**Limiting cases:** A series connection as a ring has $z=k$ and $m=1$: a single current applies everywhere, which is the core of the series connection. A parallel connection has $k=2$ and $k-1=1$: a single voltage applies everywhere, which is the core of the parallel connection.

:::frage Can it be done with even fewer unknowns?
Not without changing the network, because $m$ and $k-1$ count exactly what can be specified. But you can simplify beforehand. If you combine series and parallel connections ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)), $z$ and $k$ shrink. The count then applies to the smaller network.
:::

:::aufgabe Exercise 1 ★ Counting
<span class="anker" id="aufg-1"></span>

Give $k$, $z$, $m$ and $k-1$.

<ol class="al">

<li>

The bridge from [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): source and five resistors between four nodes.

</li>

<li>

Five nodes, each connected to every other by a resistor.

</li>

<li>

The model network after the current source and $R_5$ have been combined into one branch.

</li>

<li>

A ring of six components.

</li>

</ol>

:::loesung
(a) $k=4$, $z=6$, $m=3$, $k-1=3$. (b) $k=5$, $z=10$ (each of the 10 pairs), $m=6$, $k-1=4$. (c) $k=3$, $z=5$, $m=3$, $k-1=2$. (d) $k=6$, $z=6$, $m=1$, $k-1=5$.
:::
:::
