---
title: Stage 3: Impedance form and open-circuit test
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Two-Port Networks
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Chapter 6: Two-Port Networks
order: 1160500
summary: The first choice: The currents are the causes.
tags: Z parameters, open-circuit input resistance, open-circuit output resistance, open-circuit transfer resistance, two-terminal quantities, transfer quantities, impedance
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
The first choice: The currents are the causes. This stage shows why an open port isolates the four numbers one at a time.
:::

**The idea.** Each voltage is a sum of a part due to $I_1$ and a part due to $I_2$. To see one part alone, the other must vanish, so its current must be zero. A current is zero when its port is open. With port 2 open, only the parts due to $I_1$ remain in both equations. So one test gives two parameters, and the test with the ports swapped gives the other two.

:::definition Definition 3.1 (Impedance form, Z form)
<span class="anker" id="satz-3-1"></span>

The impedance form, also resistance form, takes the currents as causes:

<span class="anker" id="gl-3-1"></span>
$$U_1=Z_{11}I_1+Z_{12}I_2,\quad U_2=Z_{21}I_1+Z_{22}I_2,\qquad\text{in short}\quad\mathbf U=\mathbf Z\cdot\mathbf I,\quad\mathbf Z=\begin{pmatrix}Z_{11}&Z_{12}\\mathbb{Z}_{21}&Z_{22}\end{pmatrix}. \tag{3.1}$$

The __Z parameters__ follow from two open-circuit tests:

<span class="anker" id="gl-3-2"></span>
$$Z_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0},\quad Z_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0},\quad Z_{12}=\left.\frac{U_1}{I_2}\right|_{I_1=0},\quad Z_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}. \tag{3.2}$$
:::

⁠**How to read it:** $Z_{11}$ is the __open-circuit input resistance__, $Z_{22}$ the __open-circuit output resistance__, $Z_{21}$ the __open-circuit transfer resistance__ in the forward direction and $Z_{12}$ the one in the reverse direction. All have the unit $\Omega$, typically ohms to megohms. Parameters with equal indices are called __two-terminal quantities__: They are the resistance of a terminal pair with the other side fixed in its termination. Parameters with different indices are called __transfer quantities__: They link the two sides. The letter $Z$ stands for __impedance__. It generalizes resistance to capacitors and coils with AC quantities. Here all $Z$ are real resistances, for which $Z_{ii}=R_{ii}$. **Validity:** Both currents must be freely selectable (Stage [6](umrechnen-t-und.html#stufe-6)).

**Equivalent circuit.** The two equations can be drawn (Fig. [4](#abb-4) left). A sum of voltages is a series connection. $Z_{11}I_1$ depends on the port's own current, which makes it a resistor. $Z_{12}I_2$ depends on the other port's current, which makes it a controlled voltage source (CCVS). Port 2 is built in exactly the same way. This picture shows the mechanism of the open circuit: At $I_2=0$, the source $Z_{12}I_2$ supplies zero volts and $Z_{22}$ carries no current (Fig. [4](#abb-4) right). $U_1$ drops across $Z_{11}$ alone, and $U_2$ is the source voltage $Z_{21}I_1$.

:::abbildung et1/k6zesb 4
Left: equivalent circuit of the Z form, one resistor each in series with a current-controlled voltage source. Right: open-circuit test at port 2 with the impressed current $I_\mathrm{q}$. In gray, what drops out because of $I_2=0$. The test with port 1 open is the mirror image and gives $Z_{12}$ and $Z_{22}$.
:::

::::beispiel
On the T two-port, a current of 100 mA is impressed at port 1, and port 2 stays open. The current runs through $R_\mathrm{a}$ and $R_\mathrm{b}$, $U_1=3.5$ V. $R_\mathrm{c}$ carries no current, nothing drops across it, and $U_2$ is the voltage across $R_\mathrm{b}$: 2 V. So $Z_{11}=35\,\Omega$, $Z_{21}=20\,\Omega$. The same from port 2 gives $U_2=4$ V, $U_1=2$ V, so

$$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**The bridge.** The tests need no ground line. Because its branch resistances are equal, the bridge on the right of Fig. [2](vom-vierpol-zum-zweitor.html#abb-2) divides a current at port 1 in half; both branches have $R_\mathrm{x}+R_\mathrm{y}$. Port 2 is open, and the voltage between the branch midpoints is $\frac{I_1}{2}R_\mathrm{y}-\frac{I_1}{2}R_\mathrm{x}$. By symmetry, the same holds in reverse:

<span class="anker" id="gl-3-3"></span>
$$Z_{11}=Z_{22}=(R_\mathrm{x}+R_\mathrm{y})\parallel(R_\mathrm{x}+R_\mathrm{y})=\frac{R_\mathrm{x}+R_\mathrm{y}}{2},\qquad Z_{21}=Z_{12}=\frac{R_\mathrm{y}-R_\mathrm{x}}{2}. \tag{3.3}$$

⁠**Limiting cases:** For $R_\mathrm{b}\to0$, $Z_{12}=Z_{21}=0$: The shunt branch is a wire, and the ports are decoupled. For $R_\mathrm{x}=R_\mathrm{y}$, the bridge is balanced ([Chapter 4](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)), and again $Z_{21}=0$.

:::frage Why a current and not a voltage at the input? I'm more likely to have a voltage source at hand.
That works too. All that counts is that the other port is open. You then measure $U_1$ and $I_1$ and form the quotient. The impressed current merely fits the way of thinking of this form: It is the cause, the voltages are the effects.
:::

:::aufgabe Exercise 3 ★★ The bridge as a two-port
<span class="anker" id="aufg-3"></span>

In the bridge from Fig. [2](vom-vierpol-zum-zweitor.html#abb-2), let $R_\mathrm{x}=30\,\Omega$ and $R_\mathrm{y}=50\,\Omega$.

<ol class="al">

<li>

Determine $\mathbf Z$ and from it a T network with the same four parameters.

</li>

<li>

With 100 mA at port 1 and port 2 open: What are $U_1$ and $U_2$?

</li>

<li>

Swap the values, $R_\mathrm{x}=50\,\Omega$, $R_\mathrm{y}=30\,\Omega$. What changes in $\mathbf Z$ and in the T network? What does the result mean?

</li>

</ol>

:::loesung
(a) With [(3.3)](#gl-3-3): $Z_{11}=Z_{22}=40\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$. T network: $R_\mathrm{b}=Z_{12}=10\,\Omega$, $R_\mathrm{a}=R_\mathrm{c}=30\,\Omega$. (b) $U_1=40\,\Omega\cdot100\,\mathrm{mA}=4$ V, $U_2=10\,\Omega\cdot100\,\mathrm{mA}=1$ V. Directly: 50 mA through each branch, $U_2=50\,\mathrm{mA}\cdot(50-30)\,\Omega=1$ V. (c) $Z_{11}$ and $Z_{22}$ stay the same, $Z_{12}=Z_{21}=-10\,\Omega$. The T network would have $R_\mathrm{b}=-10\,\Omega$ and $R_\mathrm{a}=R_\mathrm{c}=50\,\Omega$. The negative element does not exist as a component; here the T is only a calculation aid. It says: For the same $I_1$, $U_2$ has the opposite sign.
:::
:::
