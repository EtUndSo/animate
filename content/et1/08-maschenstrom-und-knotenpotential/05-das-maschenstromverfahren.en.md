---
title: Stage 3: Mesh current analysis
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Mesh Current and Node Voltage Analysis
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Chapter 8: Mesh Current and Node Voltage Analysis
order: 1180500
summary: The node rule is taken care of; m mesh rules with m unknowns remain.
tags: coupling resistance
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
The node rule is taken care of; $m$ mesh rules with $m$ unknowns remain. This stage sets them up and shows why the matrix can be read off.
:::

**The idea.** Go around a mesh in the direction of its current. At each resistor, $R$ times the branch current drops, and the branch current is the mesh's own current plus or minus those of its neighbors. If you sort by mesh currents, the sum of all resistances of the mesh stands in front of the mesh's own current. In front of another mesh's current stands only what both meshes traverse together. Nothing more can stand there. That is why the matrix is a list of the circuit.

:::definition Definition 3.1 (Mesh current analysis)
<span class="anker" id="satz-3-1"></span>

The method has four steps:

<ol>

<li>

Convert real current sources into real voltage sources: $U_\mathrm q=I_\mathrm q\,R$, the same resistor in series ([Chapter 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

</li>

<li>

Choose $m$ independent meshes and enter one mesh current each with any direction. The direction of traversal of the mesh is this direction.

</li>

<li>

Set up the mesh rule for each mesh or read the matrix off directly.

</li>

<li>

Solve the system for the mesh currents and calculate branch currents and branch voltages from them.

</li>

</ol>
:::

:::satz Theorem 3.2 (Matrix form of mesh current analysis)
<span class="anker" id="satz-3-2"></span>

The mesh currents satisfy $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$:

<span class="anker" id="gl-3-1"></span>
$$\begin{pmatrix}Z_{11}&Z_{12}&\dots&Z_{1m}\\mathbb{Z}_{21}&Z_{22}&\dots&Z_{2m}\\\vdots&\vdots&\ddots&\vdots\\mathbb{Z}_{m1}&Z_{m2}&\dots&Z_{mm}\end{pmatrix} \begin{pmatrix}I_1\\I_2\\\vdots\\I_m\end{pmatrix}= \begin{pmatrix}U_\mathrm{q1}\\U_\mathrm{q2}\\\vdots\\U_{\mathrm qm}\end{pmatrix}. \tag{3.1}$$

<ul>

<li>

$Z_{\mu\mu}$ is the sum of all resistances of mesh $\mu$.

</li>

<li>

$Z_{\mu\nu}$ is the __coupling resistance__, the sum of the resistances traversed by both meshes: positive if both currents flow there in the same direction, negative for opposite currents, zero without a shared branch. $Z_{\mu\nu}=Z_{\nu\mu}$ holds.

</li>

<li>

$U_{\mathrm q\mu}$ is the sum of the source voltages in the mesh, positive for each source that drives the mesh current. With voltage arrows from the plus to the minus pole (ASC, [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) this means: an arrow against the traversal counts as positive, an arrow along the traversal as negative.

</li>

</ul>
:::

:::herleitung From the mesh rule to the matrix
For mesh $\mu$, the sum of all $R_a\,I_a$ equals the driving voltage $U_{\mathrm q\mu}$, because the sources move to the right-hand side. Here $I_a$ is the current in $R_a$, counted in the direction of traversal of $\mu$. According to [(2.1)](maschenstrome-erfullen-die-knotenregel.html#gl-2-1), $I_a=I_\mu+\sum_{\nu\neq\mu}\sigma_{a\nu}\,I_\nu$. Rearranging gives the sum of all $R_a$ in front of $I_\mu$ and the sum $\sum_a\sigma_{a\nu}R_a$ over the shared resistances in front of $I_\nu$. Mesh $\nu$ receives the same resistance with the same sign, because “same direction” is a relation between two meshes. That is why $\mathbf Z$ is symmetric.
:::

⁠**How to read it:** Row $\mu$ is the mesh rule of mesh $\mu$. Column $\nu$ tells which voltage one ampere of mesh current $\nu$ produces in each mesh. Hence the unit ohm; kiloohms are typical here. The letter $Z$ comes from impedance ([Chapter 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)); here these are pure resistances. **Validity:** The network contains linear resistors and fixed voltage sources. The symmetry is also a check: a mistake in setting up usually destroys it.

:::abbildung et1/k8maschen 3
The model network for mesh current analysis. On the right, the current source is converted into a voltage source. In red are the shared resistors $R_2$ and $R_4$: they stand outside the diagonal of $\mathbf Z$. I and III have no shared branch, which is why $Z_{13}=0$.
:::

::::beispiel
On the right, $U_\mathrm{q5}=I_\mathrm q\,R_5=20$ V with $R_5$ in series (Fig. [3](#abb-3)). The three clockwise traversals read

$$\begin{aligned} \text{I:}\quad&R_1I_\mathrm I+R_2(I_\mathrm I-I_\mathrm{II})-U_\mathrm q=0,\\ \text{II:}\quad&R_2(I_\mathrm{II}-I_\mathrm I)+R_3I_\mathrm{II}+R_4(I_\mathrm{II}-I_\mathrm{III})=0,\\ \text{III:}\quad&R_4(I_\mathrm{III}-I_\mathrm{II})+R_5I_\mathrm{III}+U_\mathrm{q5}=0. \end{aligned}$$

Sorted, in k$\Omega$, mA and V, this is exactly what you also read off:

$$\begin{pmatrix}R_1+R_2&-R_2&0\\-R_2&R_2+R_3+R_4&-R_4\\0&-R_4&R_4+R_5\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}5&-4&0\\-4&16&-10\\0&-10&15\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}9\\0\\-20\end{pmatrix}.$$

All off-diagonal entries are negative because neighboring circles with the same sense of rotation run against each other in the shared branch. $U_\mathrm q$ drives mesh I, $U_\mathrm{q5}$ acts against mesh III. With [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) and [(0.2)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-2),

$$D=5\cdot140+4\cdot(-60)=460,\qquad D_1=9\cdot140+4\cdot(-200)=460,$$

$$D_2=5\cdot(-200)-9\cdot(-60)=-460,\qquad D_3=-1600+320+360=-920.$$

So $I_\mathrm I=1$ mA, $I_\mathrm{II}=-1$ mA and $I_\mathrm{III}=-2$ mA. The minus says: meshes II and III actually run counterclockwise. The branch currents from Stage [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2) are 1 mA in $R_1$, 2 mA downward in $R_2$, 1 mA in $R_3$ from node 2 to node 1 and 1 mA downward in $R_4$. **Check:** $U_1=R_2\cdot2\,\mathrm{mA}=8$ V and $U_2=R_4\cdot1\,\mathrm{mA}=10$ V. Mesh I: $1+8-9=0$.
::::

⁠**Limiting case:** For $R_2\to0$, $Z_{12}=0$ and mesh I is decoupled: a wire in the middle separates both sides, because its voltage is zero whatever flows through it.

:::frage Do all mesh currents have to run the same way around?
No. The same sense of rotation is only convenient, because then all off-diagonal entries are negative. If you reverse a mesh current, its row and its column change sign, the diagonal stays, and the value of the current also changes sign. The branch current does not change.
:::

:::zusatz Ideal current source
For $R_5\to\infty$, $U_\mathrm{q5}$ grows without limit and the conversion fails ([Chapter 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). You then lay out the meshes so that only one runs through the current source. Its mesh current is known. You omit the mesh equation of this mesh, because it contains the unknown voltage of the source. One unknown fewer, one equation fewer.
:::

:::aufgabe Exercise 3 ★★ The network from Chapter 2
<span class="anker" id="aufg-3"></span>

The network from [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) has an ideal source with 9 V between $K_1$ and $K_4$ and $R_\mathrm a=2\,\mathrm{k\Omega}$ ($K_1K_2$), $R_\mathrm b=5\,\mathrm{k\Omega}$ ($K_2K_4$), $R_\mathrm c=3\,\mathrm{k\Omega}$ ($K_1K_3$), $R_\mathrm d=1\,\mathrm{k\Omega}$ ($K_3K_4$), $R_\mathrm e=2\,\mathrm{k\Omega}$ ($K_2K_3$). The meshes run as follows: $I_\mathrm A$ through the source from $K_4$ to $K_1$, then $K_2$, back to $K_4$. $I_\mathrm B$ from $K_1$ to $K_3$, $K_2$, back to $K_1$. $I_\mathrm C$ from $K_2$ to $K_3$, $K_4$, back to $K_2$.

<ol class="al">

<li>

Read off $\mathbf Z$ and the right-hand side. Check the symmetry.

</li>

<li>

Calculate the mesh currents with Cramer's rule.

</li>

<li>

Determine the five resistor currents and compare with [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html).

</li>

</ol>

:::loesung
(a) Mesh A contains $R_\mathrm a$, $R_\mathrm b$, mesh B $R_\mathrm a$, $R_\mathrm c$, $R_\mathrm e$, mesh C $R_\mathrm b$, $R_\mathrm d$, $R_\mathrm e$. All run in opposite directions in the shared branches:

$$\mathbf Z=\begin{pmatrix}7&-2&-5\\-2&7&-2\\-5&-2&8\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\0\end{pmatrix}\mathrm V.$$

The matrix is symmetric.

(b) $D=7(56-4)+2(-16-10)-5(4+35)=364-52-195=117$. $D_1=9\cdot52=468$, $D_2=234$, $D_3=351$. So $I_\mathrm A=4$ mA, $I_\mathrm B=2$ mA, $I_\mathrm C=3$ mA.

(c) $I_\mathrm a=I_\mathrm A-I_\mathrm B=2$ mA, $I_\mathrm b=I_\mathrm A-I_\mathrm C=1$ mA, $I_\mathrm c=I_\mathrm B=2$ mA, $I_\mathrm d=I_\mathrm C=3$ mA, $I_\mathrm e=I_\mathrm C-I_\mathrm B=1$ mA from $K_2$ to $K_3$. That is the table from [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), with three equations instead of twelve.
:::
:::

:::aufgabe Exercise 4 ★★ Reversing and short-circuiting
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

In the model network, reverse only mesh current II. What are $\mathbf Z$, the right-hand side and $I_\mathrm{II}$?

</li>

<li>

Prediction: $R_4$ is replaced by a wire. Which entries of $\mathbf Z$ become zero? Determine $I_\mathrm{III}$ without a system of equations.

</li>

</ol>

:::loesung
(a) Row and column II change sign, the diagonal stays:

$$\mathbf Z=\begin{pmatrix}5&4&0\\4&16&10\\0&10&15\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\-20\end{pmatrix}\mathrm V,\qquad I_\mathrm{II}=+1\,\mathrm{mA}.$$

In both shared branches the circles now run in the same direction. The right-hand side stays because there is no source in mesh II.

(b) $Z_{23}=Z_{32}=0$, because $R_4$ was the only shared resistor. Mesh III now contains only $R_5$ and $U_\mathrm{q5}$: $I_\mathrm{III}=-20\,\mathrm{V}/5\,\mathrm{k\Omega}=-4$ mA. That is the converted current source in a short circuit, the short-circuit current of 4 mA. Meshes I and II remain coupled.
:::
:::
