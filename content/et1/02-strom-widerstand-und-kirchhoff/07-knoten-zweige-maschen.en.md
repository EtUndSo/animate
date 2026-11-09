---
title: Stage 6: Nodes, branches, meshes
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Current, Resistance and Kirchhoff's Laws
order: 1120700
summary: A network has many unknowns.
tags: node, branch, graph, mesh, tree, link branches, linearly independent, complete
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
A network has many unknowns. Before calculating, you count: How many currents and voltages are there, and how many independent equations are available for them?
:::

**The idea.** For the number of equations, it does not matter which component sits in a branch. If every branch is replaced by a line, the skeleton of the network remains (Fig. [7](#abb-7)). This skeleton determines the calculation.

:::abbildung et1/k2netz 7
Left: the network of the reference model with four nodes and six branches. The branch of the source is called 0; the others bear the letter of their resistor. Right: its graph. The tree of the three black branches leaves three link branches. Each closes exactly one mesh via tree branches (the link branch in red).
:::

:::definition Definition 6.1 (Basic topological terms)
<span class="anker" id="satz-6-1"></span>

Five terms describe the structure of a network:

<ul>

<li>

A __node__ is a point at which the current branches. $k$ is their number.

</li>

<li>

A __branch__ connects two nodes via two-terminal elements, and a current flows in it. $z$ is their number.

</li>

<li>

The __graph__ is the representation made of nodes and branches. It is connected: from every node, a path leads to every other. Each branch gets the direction of its current arrow.

</li>

<li>

A __mesh__ is a closed path in which each node is connected to exactly two neighboring branches. No branch and no node is traversed more than once.

</li>

<li>

A __tree__ is a connected subgraph that contains all nodes and forms no mesh. The remaining branches are called __link branches__.

</li>

</ul>
:::

:::satz Theorem 6.2 (Number of independent meshes)
<span class="anker" id="satz-6-2"></span>

Meshes are called __linearly independent__ if they can be ordered so that each contains at least one branch missing from the previous ones. A graph with $k$ nodes and $z$ branches has exactly

<span class="anker" id="gl-6-1"></span>
$$m=z-k+1 \tag{6.1}$$

independent meshes. They form a __complete__ system: no further mesh adds anything new. Every tree defines such a system: each link branch closes exactly one mesh via the tree branches.
:::

⁠**How to read it:** $m$ counts the meshes whose equations carry new information. All other meshes are composed of them. **Validity:** The graph must be connected.

:::herleitung Why $z-k+1$
Build a tree: starting at one node, each new branch brings in exactly one new node; otherwise a mesh would arise. For $k$ nodes you need $k-1$ tree branches. That leaves $z-(k-1)$ link branches. In the tree, there is exactly one path between two nodes, so each link branch closes exactly one mesh. It contains no other link branch, which is why these meshes are independent.
:::

**Unknowns and equations.** Each branch carries a current and a voltage, which makes $2z$ unknowns. Against them stand $z$ component equations (one per branch), $k-1$ node equations (Stage [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7)) and $z-k+1$ mesh equations (Stage [8](die-maschenregel-ist-energieerhaltung.html#stufe-8)). The sum is exactly $2z$. **In short:** Every network has exactly as many equations as unknowns.

::::beispiel
The network has $k=4$, $z=6$, so $m=3$. Its graph has 16 trees with three branches each. Fig. [7](#abb-7) chooses the star around $K_4$ with the branches 0, b and d. The link branches a, c and e close the meshes $M_1$, $M_2$ and $M_3$. The system comprises 12 unknowns and 12 equations.
::::

⁠**Limiting cases:** A single loop has $z=k$, so $m=1$. A tree alone has $z=k-1$, so $m=0$: without a closed path, no steady current flows.

:::frage Is the connection of two components without a junction a node?
According to the definition it is not, because nothing branches there. If you count it anyway, $m$ does not change: an additional node splits one branch into two, and $k$ and $z$ both grow by 1.
:::

:::aufgabe Exercise 6 ★★ Counting
<span class="anker" id="aufg-6"></span>

Give $k$, $z$, $m$ and the number of tree branches in each case.

<ol class="al">

<li>

A source feeds three resistors in parallel.

</li>

<li>

$R_\mathrm e$ is removed from the network in Fig. [7](#abb-7).

</li>

<li>

A network has 6 nodes and 10 branches. How many equations of which kind are needed?

</li>

</ol>

:::loesung
(a) The two rails are the nodes: $k=2$, $z=4$, $m=3$, one tree branch. (b) $k=2$, $z=3$, $m=2$, one tree branch. Without $R_\mathrm e$ the current no longer branches at $K_2$ and $K_3$: $R_\mathrm a$ and $R_\mathrm b$ form one branch, $R_\mathrm c$ and $R_\mathrm d$ the other. (c) $m=10-6+1=5$. You need 5 node equations, 5 mesh equations and 10 component equations for 20 unknowns. A tree has 5 branches.
:::
:::
