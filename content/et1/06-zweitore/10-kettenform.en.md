---
title: Stage 8: Chain form
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Two-Port Networks
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Chapter 6: Two-Port Networks
order: 1161000
summary: Two-ports are often connected one after the other.
tags: A parameters, chain
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Two-ports are often connected one after the other. The output of one feeds the input of the next. This stage chooses the output quantities as causes and turns the chain into a matrix product.
:::

**The idea.** If one two-port hangs behind another, the output quantities of the first are exactly the input quantities of the second. If a form describes the input quantities by the output quantities, you can string them together: You start at the load and calculate back to the source stage by stage. That is exactly what the chain form does. The minus in front of $I_2$ is the reason it fits: The current that leaves one two-port is the current that flows into the next.

:::definition Definition 8.1 (Chain form, A form)
<span class="anker" id="satz-8-1"></span>

The chain form takes $U_2$ and $-I_2$ as causes:

<span class="anker" id="gl-8-1"></span>
$$U_1=A_{11}U_2+A_{12}(-I_2),\quad I_1=A_{21}U_2+A_{22}(-I_2),\qquad\text{in short}\quad \begin{pmatrix}U_1\\I_1\end{pmatrix}=\mathbf A\begin{pmatrix}U_2\\-I_2\end{pmatrix}. \tag{8.1}$$

The __A parameters__ follow from tests at the output:

<span class="anker" id="gl-8-2"></span>
$$A_{11}=\left.\frac{U_1}{U_2}\right|_{I_2=0},\quad A_{21}=\left.\frac{I_1}{U_2}\right|_{I_2=0},\quad A_{12}=\left.-\frac{U_1}{I_2}\right|_{U_2=0},\quad A_{22}=\left.-\frac{I_1}{I_2}\right|_{U_2=0}. \tag{8.2}$$

For two two-ports in a __chain__, $\mathbf A=\mathbf A'\mathbf A''$.
:::

⁠**How to read it:** $A_{11}$ is the reciprocal forward open-circuit voltage ratio, $A_{21}$ the forward open-circuit transfer conductance, $A_{12}$ the forward short-circuit transfer resistance, $A_{22}$ the reciprocal forward short-circuit current ratio. Reciprocal means: It is input over output, so the inverse of the usual ratio. $A_{11}$ and $A_{22}$ have no unit, $A_{12}$ has $\Omega$, $A_{21}$ has S. An attenuator has $A_{11}>1$. **Validity:** The chain requires the order $\mathbf A'\mathbf A''$, with the source on the left.

:::herleitung Why the chain is a matrix product
One prime marks the first two-port, two primes the second. The connection forces $U_2'=U_1''$ and $-I_2'=I_1''$. Substituting:

$$\begin{pmatrix}U_1'\\I_1'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_2'\\-I_2'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_1''\\I_1''\end{pmatrix}=\mathbf A'\mathbf A''\begin{pmatrix}U_2''\\-I_2''\end{pmatrix}.$$
:::

:::abbildung et1/k6kette 10
Top: Two two-ports in a chain. The output of the first and the input of the second share voltage and current. Bottom: The T two-port as a chain of three elementary two-ports, series resistor, shunt conductance, series resistor.
:::

::::beispiel
The simplest building blocks are the series resistor and the shunt conductance. For the series resistor, $U_1=U_2+R(-I_2)$ and $I_1=-I_2$; for the shunt conductance, $U_1=U_2$ and $I_1=G\,U_2+(-I_2)$:

$$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix},\qquad \mathbf A_G=\begin{pmatrix}1&0\\G&1\end{pmatrix}.$$

The T two-port is a chain of $R_\mathrm{a}$, $G_\mathrm{b}=1/R_\mathrm{b}=50$ mS and $R_\mathrm{c}$ (Fig. [10](#abb-10) bottom):

$$\mathbf A=\begin{pmatrix}1&15\,\Omega\\0&1\end{pmatrix}\begin{pmatrix}1&0\\50\,\mathrm{mS}&1\end{pmatrix}\begin{pmatrix}1&20\,\Omega\\0&1\end{pmatrix}=\begin{pmatrix}1.75&50\,\Omega\\50\,\mathrm{mS}&2\end{pmatrix}.$$

Backward from the load, with $U_2=3$ V and $-I_2=50$ mA: $U_1=5.25\,\mathrm{V}+2.5\,\mathrm{V}=7.75$ V and $I_1=150\,\mathrm{mA}+100\,\mathrm{mA}=250$ mA. These are the values from Stage [4](das-zweitor-im-betrieb.html#stufe-4), without a system of equations.
::::

The equivalent $\pi$ network with the shunt conductances $G_1$, $G_3$ and the series conductance $G_2$ gives in general

<span class="anker" id="gl-8-3"></span>
$$A_{11}=1+\frac{G_3}{G_2},\qquad A_{21}=G_1+G_3+\frac{G_1G_3}{G_2},\qquad A_{12}=\frac{1}{G_2},\qquad A_{22}=1+\frac{G_1}{G_2}, \tag{8.3}$$

for example $A_{11}=1+15/20=1.75$. With the output open, $G_2$ and $G_3$ form a voltage divider, $U_2=U_1\,G_2/(G_2+G_3)$, hence $A_{11}$. The others follow in the same way from [(8.2)](#gl-8-2).

⁠**Limiting cases:** $R=0$ and $G=0$ give the identity matrix, a two-port that does nothing. Two identical T two-ports in a chain have $A_{11}=5.56$, not $1.75^2=3.06$. The second loads the first, and this pulls the intermediate voltage below the open-circuit value.

:::frage The signal runs forward. Why does the chain form calculate backward?
Because it is a calculation rule, not a sequence of events. At the output, the load fixes $-I_2$ together with $U_2$. From there, each stage supplies the quantities before it without a system of equations. Physically, everything settles together.
:::

:::ltspice The chain loads itself
⁠**Draw:** source `voltage` with `9` from `1` to ground. First T: `Ra1` with `15` from `1` to `m1`, `Rb1` with `20` from `m1` to ground, `Rc1` with `20` from `m1` to `k`. Second T in the same way from `k` through `m2` to `3`. `RL` with `1G` from `3` to ground, so almost an open circuit.

⁠**Directives:** `.op`, `.meas op Uk FIND V(k)`, `.meas op Uout FIND V(3)`, `.meas op Iin FIND I(Ra1)`.

⁠**What you see:** $\mathtt{V(3)}=1.618$ V, so $9\,\mathrm{V}/1.618\,\mathrm{V}=5.56$, like $A_{11}$ of $\mathbf A\mathbf A$. At point `k` the voltage is 2.83 V instead of the 5.14 V a single T would have in open circuit. Set `RL` to 60 and check Exercise [8](#aufg-8)(c): $\mathtt{V(3)}=1.036$ V.
:::

:::aufgabe Exercise 8 ★★★ The order counts
<span class="anker" id="aufg-8"></span>

A series resistor of 30 $\Omega$ and the T two-port are connected in a chain.

<ol class="al">

<li>

Calculate $\mathbf A$ for “T, then series resistor” and for “series resistor, then T”.

</li>

<li>

Explain the difference in $A_{11}$ with currents and voltage dividers, without matrices.

</li>

<li>

Two identical T two-ports in a chain are connected to an ideal 9 V source and feed the load 60 $\Omega$. What is $U_2$? Calculate with $\mathbf A\mathbf A$.

</li>

</ol>

:::loesung
(a) T, then series resistor: $A_{11}=1.75$, $A_{12}=102.5\,\Omega$, $A_{21}=50$ mS, $A_{22}=3.5$. Series resistor, then T: $A_{11}=3.25$, $A_{12}=110\,\Omega$, $A_{21}=50$ mS, $A_{22}=2$.

(b) $A_{11}$ applies with the output open. In the first case, the series resistor hangs open at the end, carries no current, and $A_{11}$ stays 1.75. In the second, it lies in front of the input of the T, which shows 35 $\Omega$. Together with it, it forms a voltage divider, $65/35=1.857$, and $1.857\cdot1.75=3.25$.

(c) $\mathbf A\mathbf A$ has $A_{11}=5.5625$, $A_{12}=187.5\,\Omega$, $A_{21}=187.5$ mS, $A_{22}=6.5$. With $-I_2=U_2/60\,\Omega$, $U_1=(5.5625+187.5/60)\,U_2=8.6875\,U_2$, so $U_2=1.036$ V.
:::
:::
