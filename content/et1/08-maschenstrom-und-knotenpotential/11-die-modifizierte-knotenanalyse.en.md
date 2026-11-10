---
title: Stage 9: Modified nodal analysis
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1181100
summary: An ideal voltage source has no conductance and no current-source form (Chapter 5).
tags: current gain, transition frequency
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
An ideal voltage source has no conductance and no current-source form ([Chapter 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). This stage removes the last restriction. This is how SPICE calculates every circuit.
:::

**The idea.** A voltage source fixes the voltage between two nodes. Its current only establishes itself through the network, so it is unknown. You take it as an additional unknown. An additional unknown requires an additional equation, and the source itself supplies it: the potential difference is $U_\mathrm q$. So exactly one mesh equation returns per voltage source; everything else remains node analysis (Fig. [9](#abb-9)).

:::abbildung et1/k8mna 9
Modified nodal analysis. The source between $i$ and $k$ gets a new column for its current $I_V$ (green) and a new row for its voltage (red). $\mathbf Y$ stays as it is.
:::

:::satz Theorem 9.1 (Modified nodal analysis, MNA)
<span class="anker" id="satz-9-1"></span>

A network with $n$ nodes besides the reference node and one ideal voltage source between $i$ and $k$ satisfies

<span class="anker" id="gl-9-1"></span>
$$\begin{pmatrix}\mathbf Y&\mathbf C\\\mathbf B&0\end{pmatrix}\begin{pmatrix}\mathbf U\\I_V\end{pmatrix}=\begin{pmatrix}\mathbf I_\mathrm q\\U_\mathrm q\end{pmatrix}. \tag{9.1}$$

$\mathbf C$ is the new column with $+1$ in row $i$ and $-1$ in row $k$. $\mathbf B$ is the new row with $+1$ in column $i$ and $-1$ in column $k$. $I_V$ counts from $i$ through the source to $k$. The new row reads

<span class="anker" id="gl-9-2"></span>
$$U_i-U_k=U_\mathrm q. \tag{9.2}$$

For each further voltage source, one row and one column are added.
:::

⁠**How to read it:** $I_V$ flows away at $i$ and arrives at $k$, which is why it stands in row $i$ with $+1$ and in row $k$ with $-1$, like the outgoing currents of a conductance. If the source delivers power, its current flows through it from minus to plus, and $I_V$ is negative. That is exactly what SPICE shows as `I(V1)`. The ones have no unit; the new row calculates in volts, the new column in amperes. **Validity:** There is now a zero on the diagonal, but the system remains solvable as long as the network is unique. Two ideal sources in parallel are not. **In short:** Every network element has its own stamp, and all of them can be entered independently of one another.

::::beispiel the model network as SPICE sees it
SPICE converts nothing. The battery is an ideal source $U_\mathrm q$ between the new node 3 and ground; behind it lies $R_1$ from 3 to 1. The current source and $R_5$ stay as they are. The unknowns are $U_1$, $U_2$, $U_3$ and $I_V$:

$$\begin{pmatrix}1.75&-0.5&-1&0\\-0.5&0.8&0&0\\-1&0&1&1\\0&0&1&0\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\0\\9\end{pmatrix}.$$

The last row gives $U_3=9$ V, which turns the first two rows into the system from Stage [5](das-knotenpotentialverfahren.html#stufe-5): $U_1=8$ V, $U_2=10$ V. The third row gives $I_V=G_1\,(U_1-U_3)=-1$ mA. These are the results of both methods, without any conversion.
::::

⁠**Limiting case:** For $R_1\to0$, node 3 becomes node 1. Node voltage analysis fails there, the MNA does not (Exercise [11](#aufg-11)).

:::ltspice The model network as SPICE solves it
⁠**Draw:** `voltage` with `9` from `3` to ground, `R1 1k` from `3` to `1`, `R2 4k` from `1` to ground, `R3 2k` from `1` to `2`, `R4 10k` and `R5 5k` from `2` to ground, `current` with `4m` from ground to `2`.

⁠**Directives:** `.op`, `.meas op u1 FIND V(1)`, `.meas op u2 FIND V(2)`, `.meas op u3 FIND V(3)`, `.meas op iv FIND I(V1)`.

⁠**What you see:** $\mathtt{u1}=8$ V, $\mathtt{u2}=10$ V, $\mathtt{u3}=9$ V, $\mathtt{iv}=-1$ mA. These are exactly the four unknowns of the matrix above. `I(V1)` counts from the plus to the minus terminal through the source, like $I_V$. Then replace the battery as in Exercise [11](#aufg-11).
:::

**A source with 0 V is an ammeter.** An ideal voltage source with $U_\mathrm q=0$ acts like a wire, but the MNA delivers its current. This is used to measure the __current gain__. At the amplifier, $I_\mathrm{in}$ feeds node 1 with $G_\mathrm i$, and output 2 is connected to ground through the 0-V source. With $I_\mathrm{out}$ from node 2 through the source to ground,

<span class="anker" id="gl-9-3"></span>
$$\begin{pmatrix}G_\mathrm i&0&0\\g&G_\mathrm o&1\\0&1&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_\mathrm{out}\end{pmatrix}=\begin{pmatrix}I_\mathrm{in}\\0\\0\end{pmatrix},\qquad \frac{I_\mathrm{out}}{I_\mathrm{in}}=\frac{1}{I_\mathrm{in}}\cdot\frac{g\,I_\mathrm{in}}{-G_\mathrm i}=-\frac{g}{G_\mathrm i}. \tag{9.3}$$

In the model this is $-100$. Because $U_2=0$, nothing flows through $G_\mathrm o$, and the whole controlled current goes through the ammeter. At high frequencies this magnitude falls. The frequency at which it falls to 1 is called the __transition frequency__ and characterizes how fast a transistor is.

**The amplifier at an ideal source.** If the ideal voltage $U_\mathrm q$ is applied to the input, the calculation becomes shorter than in [(8.2)](gesteuerte-quellen-und-verstarker.html#gl-8-2). With $I_V$ from node 1 through the source to ground and $G=G_\mathrm o+G_\mathrm L$,

<span class="anker" id="gl-9-4"></span>
$$\begin{pmatrix}G_\mathrm i&0&1\\g&G&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_\mathrm i\\U_\mathrm o\\I_V\end{pmatrix}=\begin{pmatrix}0\\0\\U_\mathrm q\end{pmatrix},\qquad A_u=\frac{U_\mathrm o}{U_\mathrm q}=\frac{1}{U_\mathrm q}\cdot\frac{g\,U_\mathrm q}{-G}=-\frac gG=-g\,R, \tag{9.4}$$

with $R=1/G$. This is a basic structure that recurs in almost all amplifiers:

<span class="anker" id="gl-9-5"></span>
$$\text{voltage gain}=-\text{transconductance}\cdot\text{load resistance}. \tag{9.5}$$

The load resistance is the parallel connection of all resistances at the output node, in the model $20\,\mathrm{k\Omega}\parallel5\,\mathrm{k\Omega}=4\,\mathrm{k\Omega}$, so $A_u=-50\,\mathrm{mS}\cdot4\,\mathrm{k\Omega}=-200$. If several sources with the same control voltage feed the output, their transconductances add. The rule is suitable for estimating and for checking a calculation. **Limiting case:** Without a load and with $G_\mathrm o\to0$, $A_u$ grows without limit; in reality the supply voltage then sets the limit.

:::frage Why doesn't SPICE calculate with meshes if it needs voltage sources anyway?
Because the MNA only adds one row for each voltage source, whereas meshes would first have to be searched for. A network usually has few voltage sources and very many components. In addition, the extension hardly makes the matrix larger, and it stays sparse.
:::

:::aufgabe Exercise 11 ★★★ Replacing without change
<span class="anker" id="aufg-11"></span>

In the model network, replace the battery and $R_1$ by an ideal source with 8 V from node 1 to ground.

<ol class="al">

<li>

Set up the MNA system for $U_1$, $U_2$, $I_V$ and solve it with Cramer's rule.

</li>

<li>

Why does nothing change outside the replaced branch compared with the original network?

</li>

<li>

Now the ideal source delivers 9 V. How large are $U_2$ and $I_V$?

</li>

</ol>

:::loesung
(a) Unknowns $U_1$, $U_2$, $I_V$. What remains is $G_2$, $G_3$, $G_4$, $G_5$ and the current source:

$$\begin{pmatrix}0.75&-0.5&1\\-0.5&0.8&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\8\end{pmatrix}.$$

$D=-0.8$, $D_1=-6.4$, $D_2=-8$, $D_3=0.8$. So $U_1=8$ V, $U_2=10$ V, $I_V=-1$ mA.

(b) Node 1 was already at 8 V, and the branch carried 1 mA into the node. An ideal source with exactly this voltage forces the same state. The rest of the network feels only the voltage and current at this node.

(c) $U_1=9$ V. Row 2: $U_2=(4+0.5\cdot9)/0.8=10.6$ V. Row 1: $I_V=-0.75\cdot9+0.5\cdot10.625=-1.44$ mA.
:::
:::
