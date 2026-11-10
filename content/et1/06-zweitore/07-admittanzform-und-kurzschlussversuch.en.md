---
title: Stage 5: Admittance form and short-circuit test
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Two-Port Networks
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Chapter 6: Two-Port Networks
order: 1160700
summary: The second choice: The voltages are the causes.
tags: Y parameters, admittance, short-circuit input conductance, short-circuit output conductance, short-circuit transfer conductance, transconductance, input characteristic, transfer characteristic
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
The second choice: The voltages are the causes. This stage carries everything over and shows why the short circuit now takes over the role of the open circuit.
:::

**The idea.** If the voltages are the causes, one voltage must vanish so that the other part remains alone. A voltage is zero when a wire bridges the port. The open circuit sets a current to zero, the short circuit a voltage. Which test is the right one follows from the choice of causes alone.

:::definition Definition 5.1 (Admittance form, Y form)
<span class="anker" id="satz-5-1"></span>

The admittance form, also conductance form, takes the voltages as causes:

<span class="anker" id="gl-5-1"></span>
$$I_1=Y_{11}U_1+Y_{12}U_2,\quad I_2=Y_{21}U_1+Y_{22}U_2,\qquad\text{in short}\quad\mathbf I=\mathbf Y\cdot\mathbf U,\quad\mathbf Y=\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{pmatrix}. \tag{5.1}$$

The __Y parameters__ follow from two short-circuit tests:

<span class="anker" id="gl-5-2"></span>
$$Y_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0},\quad Y_{21}=\left.\frac{I_2}{U_1}\right|_{U_2=0},\quad Y_{12}=\left.\frac{I_1}{U_2}\right|_{U_1=0},\quad Y_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}. \tag{5.2}$$

For a load with the conductance $Y_\mathrm{L}$ at port 2, $I_2=-Y_\mathrm{L}U_2$,

<span class="anker" id="gl-5-3"></span>
$$U_2=-\frac{Y_{21}}{Y_{22}+Y_\mathrm{L}}\,U_1,\qquad Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}, \tag{5.3}$$

with the limiting cases

<span class="anker" id="gl-5-4"></span>
$$Y_{1,\mathrm{SC}}=Y_{11},\qquad Y_{1,\mathrm{OC}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}. \tag{5.4}$$
:::

⁠**How to read it:** $Y$ stands for __admittance__, the reciprocal of impedance; here these are real conductances in siemens, typically micro- to millisiemens, $Y_{ii}=G_{ii}$. $Y_{11}$ is the __short-circuit input conductance__, $Y_{22}$ the __short-circuit output conductance__. $Y_{21}$ is the __short-circuit transfer conductance__ in the forward direction; for the transistor it is called __transconductance__, in general transadmittance: the influence of the input voltage on the output current. $Y_{12}$ is the same conductance in the reverse direction, the influence of the output voltage on the input current. The equivalent circuit (Fig. [6](#abb-6) left) is the counterpart of the Z form: A sum of currents is a parallel connection of a conductance and a voltage-controlled current source (VCCS). [(5.3)](#gl-5-3) arises as in Stage [4](das-zweitor-im-betrieb.html#stufe-4), only with the node rule at the right and left nodes instead of the mesh rule.

:::abbildung et1/k6yesb 6
Left: equivalent circuit of the Y form. Right: short-circuit test at port 2 with the impressed voltage $U_\mathrm{q}$. Because $U_2=0$, the source $Y_{12}U_2$ drops out and $Y_{22}$ carries no current. What remains is $Y_{11}$ at the input and the current source $Y_{21}U_1$, whose current flows through the wire.
:::

::::beispiel
On the T two-port, 9 V is applied to port 1, and port 2 is short-circuited. The wire puts $R_\mathrm{c}$ in parallel with $R_\mathrm{b}$, the total resistance is $15\,\Omega+10\,\Omega=25\,\Omega$, so $I_1=360$ mA. This current divides in half, $I_2=-180$ mA, negative because it flows out of port 2. With 9 V at port 2 and a short circuit at port 1, the total resistance is $20\,\Omega+15\,\Omega\parallel20\,\Omega$, $I_2=315$ mA and $I_1=-180$ mA. This gives

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}.$$

Check with the operation from Stage [4](das-zweitor-im-betrieb.html#stufe-4): $I_1=40\,\mathrm{mS}\cdot7.75\,\mathrm{V}-20\,\mathrm{mS}\cdot3\,\mathrm{V}=250$ mA. The load $Y_\mathrm{L}=16.67$ mS gives $Y_1=40\,\mathrm{mS}-400\,\mathrm{mS^2}/51.67\,\mathrm{mS}=32.26$ mS, which is $1/(31\,\Omega)$.
::::

⁠**Limiting cases:** $Y_{1,\mathrm{SC}}=40$ mS is $1/(25\,\Omega)$, $Y_{1,\mathrm{OC}}=28.57$ mS is $1/(35\,\Omega)$, as in Stage [4](das-zweitor-im-betrieb.html#stufe-4).

**Characteristic curves.** The Y equations can also be drawn. The __input characteristic__ is $I_1=f_1(U_1)$ at fixed $U_2$, the __transfer characteristic__ $I_2=f_2(U_1)$ at fixed $U_2$, the __output characteristic__ $I_2=f_3(U_2)$ at fixed $U_1$. For a linear two-port they are straight lines (Fig. [7](#abb-7)): Their slope is a Y parameter, and the fixed value shifts them in parallel. Each value of the fixed parameter gives one line; together they form a family of curves.

:::abbildung et1/k6kennlinien 7
Characteristic curves of the T two-port. Left, input characteristic: slope $Y_{11}=40$ mS, each volt at $U_2$ shifts it by $Y_{12}\cdot1\,\mathrm{V}=-20$ mA. Center, transfer characteristic: slope $Y_{21}=-20$ mS. Right, output characteristic: slope $Y_{22}=35$ mS. For the transistor, these curves are bent ([Chapter 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
:::

:::frage Why is $Y_{11}$ not $1/Z_{11}$? Both describe the input, after all.
Both describe the input, but with different terminations: $Z_{11}$ applies with the output open, $Y_{11}$ with it short-circuited. In the T two-port, these are 35 $\Omega$ and 25 $\Omega$. $1/Y_{11}=Z_{11}$ holds only if $Z_{12}$ or $Z_{21}$ is zero.
:::

:::aufgabe Exercise 5 ★★ A $\pi$ network
<span class="anker" id="aufg-5"></span>

A $\pi$ network has the shunt conductances $G_1=10$ mS at the input and $G_3=20$ mS at the output and the series conductance $G_2=40$ mS.

<ol class="al">

<li>

Determine $\mathbf Y$ from short-circuit tests. Which currents flow with 2 V at port 1?

</li>

<li>

Calculate $Y_{1,\mathrm{OC}}$ and check the result with a direct resistance calculation.

</li>

<li>

Predict: What is $I_1$ for $U_1=0$, $U_2=5$ V, and in which direction does it flow?

</li>

</ol>

:::loesung
(a) Port 2 shorted: $Y_{11}=G_1+G_2=50$ mS, $Y_{21}=-G_2=-40$ mS. Port 1 shorted: $Y_{22}=G_2+G_3=60$ mS, $Y_{12}=-40$ mS. At 2 V: $I_1=100$ mA, $I_2=-80$ mA. (b) $Y_{1,\mathrm{OC}}=50\,\mathrm{mS}-1600\,\mathrm{mS^2}/60\,\mathrm{mS}=23.33$ mS, which is 42.86 $\Omega$. Directly: $100\,\Omega\parallel(25\,\Omega+50\,\Omega)=42.86\,\Omega$. (c) $I_1=Y_{12}U_2=-200$ mA. Port 1 is short-circuited; the current runs from port 2 through $G_2$ and leaves the two-port at terminal 1.
:::
:::
