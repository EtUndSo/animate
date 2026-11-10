---
title: Stage 6: Which method when?
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1180800
summary: Both methods deliver the same result.
tags: duality
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Both methods deliver the same result. This stage clarifies which one takes less work and what each one cannot do.
:::

**The idea.** The computational work lies in the size of the matrix. Mesh current analysis needs $z-k+1$ unknowns, node voltage analysis $k-1$. Many branches at few nodes mean many meshes but few nodes. Long chains mean the opposite.

:::satz Theorem 6.1 (Comparison of the number of equations)
<span class="anker" id="satz-6-1"></span>

Node voltage analysis needs fewer equations exactly when $k-1<z-k+1$, that is,

<span class="anker" id="gl-6-1"></span>
$$z>2k-2. \tag{6.1}$$
:::

⁠**How to read it:** On average, $2z/k$ branch ends meet at a node, because every branch has two ends. On the boundary that is $4-4/k$, so just under four. If on average more branches meet at the nodes, node voltage analysis wins (Fig. [6](#abb-6)). **Validity:** Each real source counts as one branch, because for the meshes it becomes a voltage source and a series resistor. The conversion does not change $k-1$.

:::abbildung et1/k8zahl 6
Each point is a network. Below $z=k-1$ it would not be connected. Above the red line $z=2k-2$, node voltage analysis needs fewer equations, below it mesh current analysis; on the line both are equal.
:::

|  | Mesh current analysis | Node voltage analysis |
|---|---|---|
| Unknowns | $z-k+1$ mesh currents | $k-1$ node voltages |
| satisfied by itself | node rule | mesh rule |
| set up | mesh rules | node rules |
| Matrix | $\mathbf Z$ in $\Omega$ | $\mathbf Y$ in S |
| Diagonal | sum of the resistances of the mesh | sum of the conductances at the node |
| Off-diagonal | $\pm$ shared resistance | $-$ coupling conductance |
| right-hand side | source voltages | source currents |
| disturbed by | current source | voltage source |
| smallest case | series connection, $m=1$ | parallel connection, $k-1=1$ |
| Use | hand calculation | hand calculation and simulator |

The table shows a __duality__, a mirroring: if you swap mesh and node, current and voltage, series and parallel, resistance and conductance, one method turns into the other. The reason lies in Kirchhoff: both rules say “the sum is zero”, only over different sets.

::::beispiel
After the conversion on the right, the model network has $k=3$ and $z=5$. With $5>4$ it lies above the line, and indeed there were three meshes against two nodes.
::::

⁠**Limiting case:** The bridge from [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) with $k=4$ and $z=6$ lies exactly on the line. Then the sources decide: an ideal voltage source speaks for meshes, because there it stands on the right-hand side.

Simulators use only node voltages. A program must first search for the meshes of a network, and windows exist only if the network can be drawn without crossings. Nodes, on the other hand, are already in the circuit description (Stage [7](stempel-und-netzliste.html#stufe-7)).

:::frage Isn't mesh current analysis superfluous if simulators don't use it?
For large networks, yes. By hand it is often shorter, and it keeps your eye on the current loops: you see which currents share which path. With few meshes and many nodes, for instance in long chains of series connections, it clearly wins.
:::

:::aufgabe Exercise 8 ★ Choosing the method
<span class="anker" id="aufg-8"></span>

Which method needs fewer equations? Give both numbers.

<ol class="al">

<li>

Three real voltage sources lie in parallel across a load, each as one branch.

</li>

<li>

A ring of six components.

</li>

<li>

Five nodes, all connected to each other.

</li>

<li>

Show: if in a network you combine two components in series together with the node between them, $k$ and $z$ decrease by 1 and $m$ stays the same.

</li>

</ol>

:::loesung
(a) $k=2$, $z=4$: $m=3$ against $k-1=1$, node voltages. Here $z=4>2$.

(b) $k=6$, $z=6$: $m=1$ against 5, mesh currents.

(c) $k=5$, $z=10$: $m=6$ against 4, node voltages.

(d) The node between them disappears and two branches become one, so $m'=(z-1)-(k-1)+1=z-k+1=m$. The count from [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) reaches the same conclusion.
:::
:::
