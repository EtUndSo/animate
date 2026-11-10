---
title: Key points
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1181200
summary: Why a network gets by with few unknowns
tags: Mesh current analysis, mesh current, Node voltage analysis, node voltage, reference node, resistance matrix, conductance matrix, Modified nodal analysis
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

A network with $z$ branches and $k$ nodes has $m=z-k+1$ independent meshes and $k-1$ independent nodes. Of the $z$ currents only $m$ are free, of the $z$ voltages only $k-1$.

</li>

<li>

__Mesh current analysis__ calculates with the __mesh current__, an imagined circulating current for each mesh. It enters every node and leaves it again, so the node rule holds by itself. __Node voltage analysis__ calculates with the __node voltage__, the voltage of each node against a freely chosen __reference node__. Every branch voltage is a difference, so the mesh rule holds by itself.

</li>

<li>

The remaining equations can be read off the circuit as a matrix: in the __resistance matrix__, the diagonal holds the sum of the resistances of a mesh, and next to it stand the shared resistances of two meshes. In the __conductance matrix__, the diagonal holds the sum of the conductances at a node, and next to it stands the negative conductance between two nodes. __Modified nodal analysis__ also takes the current of each voltage source as an unknown, and that is how SPICE calculates.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Of $z$ currents, $m=z-k+1$ are free; of $z$ voltages, $k-1$. These are the sizes of the two methods. Node voltage analysis is smaller if $z>2k-2$.

</li>

<li>

Mesh currents run in circles; the node rule holds by itself. Branch current = sum of the mesh currents with signs. $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$: diagonal sum of the resistances of the mesh, next to it $\pm$ shared resistances, on the right driving voltages.

</li>

<li>

Node voltages are heights; the mesh rule holds by itself. Branch voltage = difference. $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$: diagonal sum of the conductances at the node, next to it the negative coupling conductance, on the right source currents flowing in.

</li>

<li>

Current sources disturb the meshes, voltage sources the nodes: real sources are converted beforehand. Internal quantities of the source are calculated in the original network.

</li>

<li>

Each component stamps independently: $G$ in four positions, current source only on the right, $g$ in the columns $p$, $q$. Delete the reference node. The matrix is sparse; controlled sources break the symmetry.

</li>

<li>

MNA: each voltage source brings along its current as an unknown and $U_i-U_k=U_\mathrm q$ as an equation. This is how SPICE calculates. A 0-V source measures current. The voltage gain is minus transconductance times load resistance.

</li>

</ul>
:::

**One principle behind all the results.** Kirchhoff demands two things: the node rule and the mesh rule. If you choose the unknowns so that one of the two rules holds for any numerical value, you only have to write down the other. The number of unknowns is then exactly the number of remaining equations.

| Result | Where it comes from |
|---|---|
| $m$ free currents, $k-1$ free voltages | A tree determines what can be specified and what follows from it (Stage [1](wie-viele-groen-sind-frei.html#stufe-1)) |
| Mesh currents | A circulating current brings nothing into a node (Stage [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2)) |
| Resistance matrix $\mathbf Z$ | A mesh's own current runs through all resistors of the mesh, another mesh's current only through the shared ones (Stage [3](das-maschenstromverfahren.html#stufe-3)) |
| Node voltages | A round trip returns to the starting potential (Stage [4](potenziale-erfullen-die-maschenregel.html#stufe-4)) |
| Conductance matrix $\mathbf Y$ | A node's own potential drives current through all conductances at the node, another node's potential only through the shared one (Stage [5](das-knotenpotentialverfahren.html#stufe-5)) |
| Choice of method | The smaller of the two numbers wins, so $z>2k-2$ or not (Stage [6](welches-verfahren-wann.html#stufe-6)) |
| Stamps and netlist | A component touches only its two nodes (Stage [7](stempel-und-netzliste.html#stufe-7)) |
| Asymmetric matrix | A controlled source depends on other nodes (Stage [8](gesteuerte-quellen-und-verstarker.html#stufe-8)) |
| Modified nodal analysis | An ideal voltage source has no conductance, its current becomes an unknown (Stage [9](die-modifizierte-knotenanalyse.html#stufe-9)) |
