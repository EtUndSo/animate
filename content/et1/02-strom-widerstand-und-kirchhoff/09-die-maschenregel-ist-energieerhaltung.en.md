---
title: Stage 8: The mesh rule is energy conservation
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Current, Resistance and Kirchhoff's Laws
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Chapter 2: Current, Resistance and Kirchhoff's Laws
order: 1120900
summary: The second kind of equation: What does the conservation of energy demand along a closed path?
tags: 
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
The second kind of equation: What does the conservation of energy demand along a closed path? With it, the network can be solved completely.
:::

**The idea.** Every point of a network has a potential ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Anyone who walks once around the loop arrives at the same point, and so at the same potential (Fig. [9](#abb-9)). For a charge, this means: the energy it gains in the source it gives up again in the resistors. In the battery, chemical forces lift the charge against the field to the higher potential.

:::analogie
A round hike ends at the starting point. All the ascents together are exactly as high as all the descents, whichever route was chosen. The analogy ends when a magnetic field changes: then a place no longer has a fixed “height” ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)).
:::

:::satz Theorem 8.1 (Mesh rule, Kirchhoff's second law)
<span class="anker" id="satz-8-1"></span>

The sum of all branch voltages along a mesh is zero in either direction of traversal and at every instant:

<span class="anker" id="gl-8-1"></span>
$$\sum_{\nu=1}^{N}U_\nu=0,\qquad U_\nu\text{ counted positive along the traversal, negative against it.} \tag{8.1}$$

For a network, $z-k+1$ of these equations are independent; all others are then satisfied.
:::

⁠**How to read it:** $U_\nu$ is the voltage of a branch, with its arrow. The direction of traversal is free; it changes only the overall sign. **Validity:** The magnetic flux through the mesh must not change, otherwise the field is not curl-free ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). In circuits, this flux sits almost entirely in coils. The rule also holds for paths across open terminals, because a path does not have to follow a wire.

:::herleitung Mesh rule from the potential
By [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$ is independent of the path, so $\oint\vec E\cdot\mathrm{d}\vec s=0$. For points $P_1,\dots,P_N$ along a mesh this gives

$$(\varphi_1-\varphi_2)+(\varphi_2-\varphi_3)+\dots+(\varphi_N-\varphi_1)=0.$$

Each potential appears once with $+$ and once with $-$. Multiplied by the charge $Q$, this is the energy balance of one traversal: the sum of all $Q\,U_\nu$ is zero.
:::

:::abbildung et1/k2masche 9
Potential in the solved network along two meshes. A positive voltage lowers the potential if you follow its arrow; against the arrow it raises it. Left: the source raises, $R_\mathrm a$ and $R_\mathrm b$ lower by $4+5=9$ V. On the right, the traversal runs without a source: the way back through $R_\mathrm b$ against the current raises the potential. Both traversals end at the starting value.
:::

::::beispiel solving the network
The voltage arrows at the resistors are in the PSC, that is, from top to bottom, and $U_\mathrm e$ from $K_2$ to $K_3$. $U_0=9$ V points from $K_1$ to $K_4$ (ASC). The three meshes from Fig. [7](knoten-zweige-maschen.html#abb-7) give

$$M_1:\ U_\mathrm a+U_\mathrm b-U_0=0,\qquad M_2:\ U_\mathrm c+U_\mathrm d-U_0=0,\qquad M_3:\ U_\mathrm e+U_\mathrm d-U_\mathrm b=0.$$

With Ohm's law and the node equations $I_\mathrm b=I_\mathrm a-I_\mathrm e$, $I_\mathrm d=I_\mathrm c+I_\mathrm e$, three unknowns remain (in mA, $\mathrm{k\Omega}$, V):

$$7\,I_\mathrm a-5\,I_\mathrm e=9,\qquad4\,I_\mathrm c+I_\mathrm e=9,\qquad-5\,I_\mathrm a+I_\mathrm c+8\,I_\mathrm e=0.$$

The first two give $I_\mathrm a=(9+5\,I_\mathrm e)/7$ and $I_\mathrm c=(9-I_\mathrm e)/4$. Substituted into the third and multiplied by 28, this gives $117\,I_\mathrm e=117$, so $I_\mathrm e=1$ mA. Thus

| Branch | 0 | a | b | c | d | e |
|---|---|---|---|---|---|---|
| $I$ in mA | 4 | 2 | 1 | 2 | 3 | 1 |
| $U$ in V | 9 | 4 | 5 | 6 | 3 | 2 |

The potentials relative to $K_4$ are 9, 5, 3 and 0 V. **Checks:** A fourth mesh through $K_1$, $K_2$, $K_3$ must work out by itself: $U_\mathrm a+U_\mathrm e-U_\mathrm c=4+2-6=0$. Energy: the source delivers $9\,\mathrm{V}\cdot4\,\mathrm{mA}=36$ mW, the resistors absorb $8+5+12+9+2=36$ mW. If two paths lie between the same points, such as $R_1$, $R_2$ in series next to $R_3$, then $U_1+U_2-U_3=0$ follows.
::::

:::ltspice Recalculating the network
⁠**Draw:** source `voltage` with `9` from `k1` to ground, so $K_4$ is the ground. `res`: `Ra 2k` from `k1` to `k2`, `Rb 5k` from `k2` to ground, `Rc 3k` from `k1` to `k3`, `Rd 1k` from `k3` to ground, `Re 2k` from `k2` to `k3`.

⁠**Directives:** `.op`, plus `.meas op p2 FIND V(k2)`, `.meas op ie FIND I(Re)` and likewise for the other quantities. The results appear in the SPICE Error Log.

⁠**What you see:** $\mathtt{V(k2)}=5$ V, $\mathtt{V(k3)}=3$ V, $\mathtt{I(Ra)}=\mathtt{I(Rc)}=2$ mA, $\mathtt{I(Rb)}=\mathtt{I(Re)}=1$ mA, $\mathtt{I(Rd)}=3$ mA. $\mathtt{I(V1)}=-4$ mA: SPICE counts the source current in the PSC, hence the negative sign. Then build Exercise [8](#aufg-8).
:::

:::frage How does the current ‘know’ how to divide?
It knows nothing. At switch-on, tiny charges collect at the nodes and shift their potentials until nothing is left stuck at any node. This happens in nanoseconds. The result is the only solution that satisfies both rules at once.
:::

:::aufgabe Exercise 8 ★★ Mesh and node together
<span class="anker" id="aufg-8"></span>

A 12 V source feeds $R_1=1.5\,\mathrm{k\Omega}$, followed by $R_2=3\,\mathrm{k\Omega}$ and an unknown resistor $R_3$ side by side. The measured value is $U_1=9$ V.

<ol class="al">

<li>

Use the mesh rule to determine $U_2$ and $U_3$.

</li>

<li>

Determine all the currents and $R_3$.

</li>

<li>

Check the energy balance.

</li>

<li>

Prediction: A moving bar magnet passes through the mesh of source, $R_1$ and $R_2$. What no longer holds now?

</li>

</ol>

:::loesung
(a) Mesh of source, $R_1$, $R_2$: $U_2=12\,\mathrm{V}-9\,\mathrm{V}=3$ V. Mesh of $R_2$, $R_3$: $U_3=U_2=3$ V.

(b) $I_1=9\,\mathrm{V}/1.5\,\mathrm{k\Omega}=6$ mA, $I_2=3\,\mathrm{V}/3\,\mathrm{k\Omega}=1$ mA. Node rule: $I_3=5$ mA, so $R_3=3\,\mathrm{V}/5\,\mathrm{mA}=600\,\Omega$. Check: $R_2\parallel R_3=500\,\Omega$, in total $2\,\mathrm{k\Omega}$, $12\,\mathrm{V}/2\,\mathrm{k\Omega}=6$ mA.

(c) The source delivers $12\,\mathrm{V}\cdot6\,\mathrm{mA}=72$ mW, the resistors absorb $54+3+15=72$ mW.

(d) The mesh rule. The changing flux produces a curl field along the mesh, $\oint\vec E\cdot\mathrm{d}\vec s$ is not zero, and the sum of the voltages becomes equal to the induced voltage. The node rule remains valid.
:::
:::
