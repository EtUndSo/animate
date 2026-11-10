---
title: Stage 7: Stamps and netlist
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1180900
summary: A program sees no meshes and rearranges nothing.
tags: stamp, netlist, sparse
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
A program sees no meshes and rearranges nothing. This stage shows how the matrix arises component by component, without any component having to know the others.
:::

**The idea.** A component touches only its two nodes. Its current therefore appears in exactly two node equations, in one with plus, in the other with minus. So each component has a fixed entry pattern, its __stamp__ (Fig. [7](#abb-7)). You begin with a matrix full of zeros and add the stamps component by component. The order does not matter.

:::abbildung et1/k8stempel 7
Entry patterns in the rows and columns of the nodes. Left: conductance $G$ between $i$ and $k$. Center: fixed current source that pushes $I_\mathrm q$ from $k$ to $i$; it enters only on the right-hand side. Right: voltage-controlled current source $g\,U_{pq}$ from $i$ to $k$. It stands in the rows $i$, $k$, but in the columns $p$, $q$ (Stage [8](gesteuerte-quellen-und-verstarker.html#stufe-8)).
:::

:::satz Theorem 7.1 (Stamps of conductance and current source)
<span class="anker" id="satz-7-1"></span>

Each row is the node rule “outgoing currents = impressed currents”.

<ul>

<li>

A conductance $G$ between $i$ and $k$ carries the current $I_Y=G\,(U_i-U_k)$ from $i$ to $k$. It adds $+G$ to the positions $(i,i)$ and $(k,k)$ and $-G$ to $(i,k)$ and $(k,i)$.

</li>

<li>

A fixed current source that pushes $I_\mathrm q$ through itself from $k$ to $i$ adds $+I_\mathrm q$ in row $i$ and $-I_\mathrm q$ in row $k$ of the right-hand side. It enters nothing in $\mathbf Y$, because its current depends on no voltage.

</li>

</ul>
:::

⁠**How to read it:** First, each of the $k$ nodes gets a row and a column, including the reference node. This full matrix has determinant zero, because all rows have the sum zero: if you raise all potentials together, no additional current flows anywhere. Physically, a network determines only differences. Only fixing $U_0=0$ makes the solution unique: you delete column 0 because its unknown is zero, and row 0 because it follows from the other node rules ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). What remains is $\mathbf Y$ from Stage [5](das-knotenpotentialverfahren.html#stufe-5). **Validity:** The stamps apply to linear components. Voltage sources follow in Stage [9](die-modifizierte-knotenanalyse.html#stufe-9).

**Netlist.** A circuit diagram is stored as a __netlist__: one line per component, consisting of name, nodes and value. In SPICE, `R3 1 2 2k` means: resistor between the nodes 1 and 2. `I2 0 2 4m` means: 4 mA through the source from node 0 to node 2. The program goes through the list line by line and stamps. If a new node name appears, the matrix grows by one row and one column. Nobody has to know its size beforehand. The rigid format dates from the 1970s, when SPICE was written in FORTRAN and each line occupied a punched card.

::::beispiel
The model network with the converted battery gives this list:

| Line | Value | Entry |
|---|---|---|
| `R1 1 0 1k` | $G_1=1$ | $+1$ at $(1,1)$, $(0,0)$; $-1$ at $(1,0)$, $(0,1)$ |
| `R2 1 0 4k` | $G_2=0.25$ | $+0.25$ at $(1,1)$, $(0,0)$; $-0.25$ at $(1,0)$, $(0,1)$ |
| `R3 1 2 2k` | $G_3=0.5$ | $+0.5$ at $(1,1)$, $(2,2)$; $-0.5$ at $(1,2)$, $(2,1)$ |
| `R4 2 0 10k` | $G_4=0.1$ | $+0.1$ at $(2,2)$, $(0,0)$; $-0.1$ at $(2,0)$, $(0,2)$ |
| `R5 2 0 5k` | $G_5=0.2$ | $+0.2$ at $(2,2)$, $(0,0)$; $-0.2$ at $(2,0)$, $(0,2)$ |
| `I1 0 1 9m` | $I=9$ | right $+9$ in row 1, $-9$ in row 0 |
| `I2 0 2 4m` | $I=4$ | right $+4$ in row 2, $-4$ in row 0 |

With the rows and columns in the order 0, 1, 2 this gives

$$\begin{pmatrix}1.55&-1.25&-0.3\\-1.25&1.75&-0.5\\-0.3&-0.5&0.8\end{pmatrix} \begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-13\\9\\4\end{pmatrix}.$$

Each row sums to zero. If you delete row and column 0, the system from Stage [5](das-knotenpotentialverfahren.html#stufe-5) remains. **Check:** In the reduced $\mathbf Y$, the row sum is the conductance to ground: $1.75-0.5=1.25=G_1+G_2$ and $0.8-0.5=0.3=G_4+G_5$.
::::

⁠**Limiting case:** A node without a branch to ground has the row sum zero.

**Large networks.** A node is usually connected to only two to five neighbors, so almost all positions of a large matrix are zero. It is called __sparse__. The simulator stores only the nonzero entries and solves the system by stepwise elimination. Cramer's rule would be useless for this: a determinant with 20 rows has around $2.4\cdot10^{18}$ products following the pattern of [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1).

:::zusatz Alternating current, capacitor, diode
With sinusoidal quantities you calculate with complex conductances, the admittances. That is where the letters $Y$ and $Z$ come from. A capacitor has the same stamp as a conductance. An impedance $Z$ can be entered only as $Y=1/Z$ as long as it is not zero; a coil at frequency zero breaks this. Stage [9](die-modifizierte-knotenanalyse.html#stufe-9) solves this problem. The simulator replaces nonlinear components such as diodes ([Chapter 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) by the tangent of their characteristic curve, stamps it and repeats this until nothing changes any more.
:::

:::frage Why may you delete precisely the row of the reference node?
Each of the $k$ node equations follows from the others ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). You could delete any of them. You delete the row of the reference node because, together with its column, a symmetric matrix results again and because the current into ground is rarely of interest.
:::

:::aufgabe Exercise 9 ★★ From the netlist to the solution
<span class="anker" id="aufg-9"></span>

The list `R1 1 0 1k`, `R2 1 2 2k`, `R3 2 0 2k`, `I1 0 1 7m`, `I2 2 1 1m` is given.

<ol class="al">

<li>

Stamp the full $3\times3$ matrix and the right-hand side. Check the row sums.

</li>

<li>

Delete the reference node and solve.

</li>

<li>

Check: Which current flows through the resistors into ground, and which comes out of it?

</li>

</ol>

:::loesung
(a) With the conductances 1, 0.5, 0.5 mS and rows 0, 1, 2:

$$\begin{pmatrix}1.5&-1&-0.5\\-1&1.5&-0.5\\-0.5&-0.5&1\end{pmatrix}\begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-7\\8\\-1\end{pmatrix}.$$

`I2 2 1 1m` pushes 1 mA from 2 to 1, so $+1$ in row 1 and $-1$ in row 2. All row sums are zero, and the sum on the right is zero too.

(b) $\begin{pmatrix}1.5&-0.5\\-0.5&1\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}8\\-1\end{pmatrix}$ with $D=1.25$, $D_1=7.5$, $D_2=2.5$. So $U_1=6$ V, $U_2=2$ V.

(c) Through `R1` flow 6 mA into ground, through `R3` 1 mA, together 7 mA. `I1` takes exactly 7 mA out of ground.
:::
:::
