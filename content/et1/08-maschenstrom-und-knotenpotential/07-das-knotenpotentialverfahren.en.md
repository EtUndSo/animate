---
title: Stage 5: Node voltage analysis
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Mesh Current and Node Voltage Analysis
order: 1180700
summary: The mesh rule is taken care of; k-1 node rules with k-1 unknowns remain.
tags: coupling conductance
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
The mesh rule is taken care of; $k-1$ node rules with $k-1$ unknowns remain. This stage sets them up and solves the same network a second time.
:::

**The idea.** The current that flows away through a conductance $G$ from node $\mu$ to neighbor $\nu$ is $G\,(U_\mu-U_\nu)$. If you add all outgoing currents of a node and sort by potentials, the sum of all conductances at the node stands in front of the node's own potential. In front of another node's potential stands only the conductance leading to that node, with a minus: if you raise the neighbor, less flows away. Fig. [5](#abb-5) shows this as an experiment.

:::definition Definition 5.1 (Node voltage analysis)
<span class="anker" id="satz-5-1"></span>

The method has four steps:

<ol>

<li>

Convert real voltage sources into real current sources: $I_\mathrm q=U_\mathrm q/R$, the same resistor in parallel ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

</li>

<li>

Fix a reference node and enter the potentials of the other nodes as voltages against it. Write resistors as conductances.

</li>

<li>

Set up the node rule for the $k-1$ remaining nodes or read the matrix off directly.

</li>

<li>

Solve the system for the node voltages and calculate branch voltages and branch currents from them.

</li>

</ol>
:::

:::satz Theorem 5.2 (Matrix form of node voltage analysis)
<span class="anker" id="satz-5-2"></span>

With $n=k-1$, the node voltages satisfy $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$:

<span class="anker" id="gl-5-1"></span>
$$\begin{pmatrix}Y_{11}&Y_{12}&\dots&Y_{1n}\\Y_{21}&Y_{22}&\dots&Y_{2n}\\\vdots&\vdots&\ddots&\vdots\\Y_{n1}&Y_{n2}&\dots&Y_{nn}\end{pmatrix} \begin{pmatrix}U_1\\U_2\\\vdots\\U_n\end{pmatrix}= \begin{pmatrix}I_\mathrm{q1}\\I_\mathrm{q2}\\\vdots\\I_{\mathrm qn}\end{pmatrix}. \tag{5.1}$$

<ul>

<li>

$Y_{\mu\mu}$ is the sum of all conductances connected to node $\mu$.

</li>

<li>

$Y_{\mu\nu}=Y_{\nu\mu}$ is the negative __coupling conductance__, that is, minus the sum of the conductances lying directly between the nodes $\mu$ and $\nu$. Without a direct connection, the entry is zero.

</li>

<li>

$I_{\mathrm q\mu}$ is the sum of the source currents at the node, positive if they flow into the node.

</li>

</ul>
:::

:::herleitung From the node rule to the matrix
At node $\mu$, the current $G_a\,(U_\mu-U_\nu)$ flows away through each conductance $G_a$ to the neighbor $\nu$, and $G_a\,U_\mu$ to the reference node. The sum of these currents equals the injected $I_{\mathrm q\mu}$. Sorting gives the sum of all $G_a$ in front of $U_\mu$ and minus the sum of the conductances between $\mu$ and $\nu$ in front of $U_\nu$. Node $\nu$ receives the same entry, because a conductance has no direction. That is why $\mathbf Y$ is symmetric.
:::

⁠**How to read it:** Row $\mu$ is the node rule: on the left stand all currents flowing away through conductances, on the right what the sources push in. Column $\nu$ says: if you hold node $\nu$ at 1 V and all others at 0 V, you must inject the current $Y_{\nu\nu}$ at node $\nu$ and draw the current $-Y_{\mu\nu}$ at each neighbor $\mu$. That is exactly the short-circuit test from [Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). **Validity:** The network contains conductances and fixed current sources. An ideal voltage source does not fit in, because it has no finite conductance (Stage [9](die-modifizierte-knotenanalyse.html#stufe-9)).

:::abbildung et1/k8yspalte 5
Left: the model network for node voltage analysis; the battery is converted into a current source. Right: the sources are removed, node 1 is at 1 V, node 2 at 0 V. Through $G_1$, $G_2$, $G_3$, a total of $1+0.25+0.5=1.75$ mA flow away, which is $Y_{11}$. The 0.5 mA arrive at node 2 and must be drawn off there, which is $Y_{21}=-0.5$ mS.
:::

::::beispiel
On the left, $I_\mathrm{q1}=U_\mathrm q/R_1=9$ mA with $G_1=1$ mS in parallel. The conductances are $G_2=0.25$ mS, $G_3=0.5$ mS, $G_4=0.1$ mS and $G_5=0.2$ mS (Fig. [5](#abb-5)). The node rules read

$$\begin{aligned} \text{Node 1:}\quad&(G_1+G_2)\,U_1+G_3\,(U_1-U_2)-I_\mathrm{q1}=0,\\ \text{Node 2:}\quad&G_3\,(U_2-U_1)+(G_4+G_5)\,U_2-I_\mathrm q=0. \end{aligned}$$

Sorted, in mS, V and mA:

$$\begin{pmatrix}G_1+G_2+G_3&-G_3\\-G_3&G_3+G_4+G_5\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}= \begin{pmatrix}1.75&-0.5\\-0.5&0.8\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}9\\4\end{pmatrix}.$$

With $D=1.4-0.25=1.15$, $D_1=7.2+2=9.2$ and $D_2=7+4.5=11.5$, it follows that $U_1=8$ V and $U_2=10$ V. This is the same result as from the three meshes, with a $2\times2$ instead of a $3\times3$ calculation.

The currents come from the differences, and in the *original* network: $(U_\mathrm q-U_1)/R_1=1$ mA, $U_1/R_2=2$ mA, $(U_2-U_1)/R_3=1$ mA, $U_2/R_4=1$ mA, $U_2/R_5=2$ mA. **Checks:** At node 2, $4=1+1+2$ mA. The sources deliver $9\,\mathrm{V}\cdot1\,\mathrm{mA}+10\,\mathrm{V}\cdot4\,\mathrm{mA}=49$ mW, the resistors absorb $1+16+2+10+20=49$ mW.
::::

⁠**Limiting case:** For $G_3\to0$ the off-diagonal entries vanish, and the two sides calculate separately (Exercise [7](#aufg-7)).

:::frage In $\mathbf Z$ the sign depends on the arrows. Why is there always a minus in $\mathbf Y$?
Mesh currents have a direction that you choose, and so there are two possibilities in the shared branch. Node voltages have no direction; all count toward the same reference node. At the conductance between two nodes there is therefore always the difference, and the other node's potential always carries a minus.
:::

:::frage After the conversion, 2 mA flow upward through $R_5$ in the mesh picture, but 2 mA downward in the original network. Which is right?
The original network. Equivalent sources agree only at the terminals ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). At node 2 and at ground both forms deliver the same; inside the source the current means different things. That is why you calculate internal quantities in the original network from the terminal voltages.
:::

:::aufgabe Exercise 6 ★★ Three nodes and a reference
<span class="anker" id="aufg-6"></span>

A network has the nodes 0 (reference), 1, 2, 3. Resistors: 1 k$\Omega$ from 1 to 0, 1 k$\Omega$ from 1 to 2, 500 $\Omega$ from 2 to 0, 1 k$\Omega$ from 2 to 3, 1 k$\Omega$ from 3 to 0. Current sources push 6 mA into node 1 and 3 mA into node 2.

<ol class="al">

<li>

Read off $\mathbf Y$ and $\mathbf I_\mathrm q$. Why is $Y_{13}=0$?

</li>

<li>

Calculate the node voltages with Cramer's rule.

</li>

<li>

Calculate all resistor currents and do the check at node 2.

</li>

<li>

How many mesh currents do you need after converting the two sources? Which method would be shorter here?

</li>

</ol>

:::loesung
(a) With 1 mS, 1 mS, 2 mS, 1 mS, 1 mS:

$$\mathbf Y=\begin{pmatrix}2&-1&0\\-1&4&-1\\0&-1&2\end{pmatrix}\mathrm{mS},\qquad\mathbf I_\mathrm q=\begin{pmatrix}6\\3\\0\end{pmatrix}\mathrm{mA}.$$

$Y_{13}=0$, because there is no resistor between 1 and 3.

(b) $D=2\cdot7+1\cdot(-2)=12$, $D_1=48$, $D_2=24$, $D_3=12$. So $U_1=4$ V, $U_2=2$ V, $U_3=1$ V.

(c) $I_{10}=4$ mA, $I_{12}=2$ mA, $I_{20}=4$ mA, $I_{23}=1$ mA, $I_{30}=1$ mA. Node 2: $3+2=4+1$ mA.

(d) Each current source becomes one branch with its parallel resistor. Then $z=5$ and $k=4$, so $m=2$ against $k-1=3$. Mesh current analysis would be shorter with two equations. Node 3 is in truth not a node, but a series connection.
:::
:::

:::aufgabe Exercise 7 ★★ Limiting cases of the coupling conductance
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

$R_3$ in the model network is removed ($G_3=0$). What becomes of $\mathbf Y$? Calculate $U_1$ and $U_2$.

</li>

<li>

Prediction: $R_3$ is replaced by a wire. Why does this not work directly in $\mathbf Y$? Merge the nodes and determine the common voltage and the current in the wire.

</li>

</ol>

:::loesung
(a) The off-diagonal entries become zero and the equations decouple: $U_1=9\,\mathrm{mA}/1.25\,\mathrm{mS}=7.2$ V and $U_2=4\,\mathrm{mA}/0.3\,\mathrm{mS}=13.3$ V. These are two separate networks.

(b) $G_3\to\infty$ cannot be entered as a number. The wire turns both nodes into one: $U=(9+4)\,\mathrm{mA}/(1+0.25+0.1+0.2)\,\mathrm{mS}=8.39$ V. The current in the wire follows from node 2: $4\,\mathrm{mA}-0.3\,\mathrm{mS}\cdot8.39\,\mathrm{V}=1.48$ mA from 2 to 1. Stage [9](die-modifizierte-knotenanalyse.html#stufe-9) solves the same situation with a 0-V source.
:::
:::
