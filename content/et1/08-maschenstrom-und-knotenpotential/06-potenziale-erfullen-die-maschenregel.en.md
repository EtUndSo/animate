---
title: Stage 4: Potentials satisfy the mesh rule
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1180600
summary: Of z voltages only k-1 are free.
tags: 
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Of $z$ voltages only $k-1$ are free. This stage shows why the potentials of the nodes take on this role and why the mesh rule then holds by itself.
:::

**The idea.** Each node has a potential ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), just as each point of a landscape has a height. The voltage of a branch is the height difference between its ends. Anyone who walks in a circle arrives back at the starting height, whatever heights have been assigned to the nodes (Fig. [4](#abb-4)). So the mesh rule cannot be violated at all. Since only differences count, you may fix one height freely. That saves one unknown, and $k-1$ remain.

:::abbildung et1/k8hoehen 4
The nodes of the model network as heights. The round trip from 0 via 1 and 2 back to 0 rises by 8 V and 2 V and falls by 10 V. The sum is zero, and it would stay zero if the heights 1 and 2 were shifted arbitrarily.
:::

:::definition Definition 4.1 (Reference node and node voltage)
<span class="anker" id="satz-4-1"></span>

A freely chosen node 0 is the *reference node*; its potential is $\varphi_0=0$. The *node voltage* of another node $\mu$ is its voltage against the reference node:

<span class="anker" id="gl-4-1"></span>
$$U_\mu=\varphi_\mu-\varphi_0. \tag{4.1}$$

The voltage of a branch between the nodes $\mu$ and $\nu$ is $U_{\mu\nu}=U_\mu-U_\nu$; toward the reference node it is $U_{\mu0}=U_\mu$.
:::

:::satz Theorem 4.2 (Node voltages)
<span class="anker" id="satz-4-2"></span>

For any values of the $k-1$ node voltages, every mesh rule is satisfied. Conversely, every voltage distribution that satisfies the mesh rule has exactly one set of node voltages.
:::

:::herleitung Why this always works
⁠*Mesh rule.* Along a mesh through the nodes $1,2,\dots,N$, $(U_1-U_2)+(U_2-U_3)+\dots+(U_N-U_1)=0$. Each potential appears once with $+$ and once with $-$.

⁠*Completeness.* Choose a tree. In it there is exactly one path between the reference node and each node. The sum of the branch voltages along this path defines the node voltage uniquely. With this, all differences are correct for the tree branches. For each link branch the difference is correct because it closes a mesh with tree branches, whose rule holds by assumption.
:::

⁠**How to read it:** $U_\mu$ is a voltage with an arrow from node $\mu$ to the reference node, unit volt. In a circuit diagram, the ground symbol marks the reference node; in SPICE it is always called 0. You choose the reference node where most branches meet, which makes the equations shortest. **Validity:** The field must be curl-free. A changing magnetic field through a mesh destroys the potentials ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)); in circuits it sits in coils.

::::beispiel
In the model network, $U_1=8$ V and $U_2=10$ V, as Stage [3](das-maschenstromverfahren.html#stufe-3) showed. The voltage across $R_3$ is $U_{12}=U_1-U_2=-2$ V, so node 2 lies higher, and the current runs from 2 to 1. With $R_3=2\,\mathrm{k\Omega}$ that is the 1 mA from Stage [3](das-maschenstromverfahren.html#stufe-3). The round trip gives $(U_1-U_2)+U_2-U_1=0$ for any other pair of numbers too.
::::

⁠**Limiting case:** A network with $k=2$ has a single node voltage. That is the common voltage of a parallel connection.

:::frage So is the node voltage a potential or a voltage?
Both. A potential by itself has a value only relative to a zero point ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). The node voltage is the voltage against the chosen zero point, which is why it carries the symbol $U$. Changing the reference node changes all node voltages, but not a single branch voltage.
:::

:::aufgabe Exercise 5 ★ Changing the reference
<span class="anker" id="aufg-5"></span>

In the model network, choose node 2 as the reference node. (a) What node voltages do the lower line and node 1 have? (b) From these, calculate the voltage between node 1 and the lower line. (c) Why does no current change?

:::loesung
(a) All potentials drop by 10 V: lower line $-10$ V, node 1 $-2$ V, node 2 0 V.

(b) $-2\,\mathrm{V}-(-10\,\mathrm{V})=8$ V, as before.

(c) Currents depend only on differences, and those stay the same.
:::
:::
