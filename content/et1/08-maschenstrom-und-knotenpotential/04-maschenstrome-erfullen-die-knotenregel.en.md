---
title: Stage 2: Mesh currents satisfy the node rule
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1180400
summary: We are looking for m quantities from which all branch currents follow.
tags: windows
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
We are looking for $m$ quantities from which all branch currents follow. This stage shows why circulating currents achieve this and why the node rule then holds by itself.
:::

**The idea.** Imagine a separate current in each independent mesh, running in a circle (Fig. [2](#abb-2)). The mechanism lies in the word circle: if the current enters a node through one branch, it leaves the node through another branch of the same mesh. It brings nothing into the node. This applies to every circulating current, at every node and for every numerical value. In a branch that belongs to two meshes, both circulating currents are superimposed. Only this sum is measured.

:::analogie
Two circular bus lines share a street. On the shared street run the buses of both lines, and every line that drives into an intersection also drives out of it again. The analogy ends with the individual: an electron belongs to no mesh. Mesh currents are calculation quantities; only the branch current really flows.
:::

:::abbildung et1/k8kreis 2
Node 1 with the mesh currents I and II. Left: each circulating current runs through the node. Right: the same situation as branch currents. $I_\mathrm I$ flows toward the node, $I_\mathrm I-I_\mathrm{II}$ and $I_\mathrm{II}$ flow away. The sum is zero for all values.
:::

:::satz Theorem 2.1 (Mesh currents)
<span class="anker" id="satz-2-1"></span>

If you place a *mesh current* $I_\mu$ with a freely chosen direction in each of $m$ independent meshes, the current of a branch is

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{branch}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu,\qquad\sigma_\mu=\begin{cases}+1&\text{mesh }\mu\text{ runs in the arrow direction of the branch,}\\-1&\text{mesh }\mu\text{ runs against the arrow,}\\0&\text{mesh }\mu\text{ does not contain the branch.}\end{cases} \tag{2.1}$$

The node rule is then satisfied for all values of the $I_\mu$. Conversely, every current distribution that satisfies the node rule can be represented in this way.
:::

:::herleitung Why this always works
⁠*Node rule.* In a mesh, every node is connected to exactly two branches ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Its current counts once flowing in and once flowing out at the node, and the contributions cancel.

⁠*Completeness.* Choose a tree. Each link branch closes exactly one mesh; let its mesh current be the current of this link branch. If you subtract all these circulating currents from the given distribution, the remainder still satisfies the node rule and is zero in all link branches. It can flow only in the tree. But the tree has an end, a node with only one tree branch. There the node rule forces the current to zero. Delete this branch and repeat. The remainder is zero everywhere.
:::

⁠**How to read it:** $\mu$ numbers the meshes, in the examples with Roman numerals. The direction is free; a negative value means that the circulating current runs the other way around. **Validity:** The meshes must be independent. If the network can be drawn without crossings, you choose the __windows__, the areas between the branches. When building up from the tree, each new link branch divides exactly one area in two, so there are exactly $m$ windows.

::::beispiel
If you combine the current source and $R_5$ in the model network into a branch with a voltage source (Stage [3](das-maschenstromverfahren.html#stufe-3)), three windows I, II, III remain, with clockwise mesh currents. All five branch currents follow from them:

| Branch | left, $R_1$ | $R_2$ | $R_3$ | $R_4$ | right, $R_5$ |
|---|---|---|---|---|---|
| Current | $I_\mathrm I$ | $I_\mathrm I-I_\mathrm{II}$ | $I_\mathrm{II}$ | $I_\mathrm{II}-I_\mathrm{III}$ | $I_\mathrm{III}$ |

At node 1 this gives $I_\mathrm I-(I_\mathrm I-I_\mathrm{II})-I_\mathrm{II}=0$, no matter what values the currents have.
::::

⁠**Limiting cases:** For $m=1$, the mesh current is the current of the series connection. For $I_\mathrm{II}=0$, the current in $R_3$ vanishes; the left and right halves exchange nothing.

:::frage What does an ammeter in the branch of $R_2$ measure, $I_\mathrm I$ or $I_\mathrm{II}$?
Neither of them, but the branch current $I_\mathrm I-I_\mathrm{II}$. A mesh current can be measured directly only where it flows alone, here for example $I_\mathrm I$ in $R_1$. That is the tree idea: the mesh current is the current of a branch that belongs only to this mesh.
:::

:::aufgabe Exercise 2 ★ From mesh current to branch current
<span class="anker" id="aufg-2"></span>

Two meshes share the vertical resistor $R_\mathrm g=3\,\mathrm{k\Omega}$; mesh a lies to its left, mesh b to its right. Otherwise a contains only a source and $R_\mathrm a=2\,\mathrm{k\Omega}$, b only a source and $R_\mathrm b=1\,\mathrm{k\Omega}$. Both mesh currents run clockwise, $I_\mathrm a=3$ mA, $I_\mathrm b=-1$ mA.

<ol class="al">

<li>

How large is the current in $R_\mathrm g$ in the direction of $I_\mathrm a$?

</li>

<li>

Check the node rule at the upper end of $R_\mathrm g$.

</li>

<li>

What voltage must the source in each mesh drive in the direction of traversal?

</li>

</ol>

:::loesung
(a) In the shared branch, the two clockwise circles run against each other: $I_\mathrm a-I_\mathrm b=3-(-1)=4$ mA in the direction of $I_\mathrm a$.

(b) If $R_\mathrm g$ stands vertically between the meshes, $I_\mathrm a$ runs toward the node at the top and $I_\mathrm b$ away from it. Flowing away are $I_\mathrm a-I_\mathrm b$ downward and $I_\mathrm b$ to the right: $3-4-(-1)=0$.

(c) Mesh a: $R_\mathrm a\,I_\mathrm a+R_\mathrm g\,(I_\mathrm a-I_\mathrm b)=6+12=18$ V. Mesh b: $R_\mathrm b\,I_\mathrm b+R_\mathrm g\,(I_\mathrm b-I_\mathrm a)=-1-12=-13$ V. So the source in b drives with 13 V counterclockwise.
:::
:::
