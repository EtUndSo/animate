---
title: Stage 7: Hybrid form
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160900
summary: With an amplifier, it is easy to specify the current at the input and the voltage at the output.
tags: H parameters, short-circuit input resistance, short-circuit current ratio, open-circuit reverse voltage ratio, open-circuit output conductance
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
With an amplifier, it is easy to specify the current at the input and the voltage at the output. This stage mixes the causes.
:::

**The idea.** Nothing forces you to take the same kind of cause at both ports. If you take $I_1$ and $U_2$, then $U_1$ and $I_2$ are the effects. This suits components like the bipolar transistor: Its input is controlled by a current, and its output acts like a current source with a large internal resistance. The tests again follow from the choice: $U_2=0$ means a short circuit at the output, $I_1=0$ an open circuit at the input.

:::definition Definition 7.1 (Hybrid form, H form)
<span class="anker" id="satz-7-1"></span>

The hybrid form takes $I_1$ and $U_2$ as causes:

<span class="anker" id="gl-7-1"></span>
$$U_1=H_{11}I_1+H_{12}U_2,\quad I_2=H_{21}I_1+H_{22}U_2,\qquad\text{in short}\quad \begin{pmatrix}U_1\\I_2\end{pmatrix}=\mathbf H\begin{pmatrix}I_1\\U_2\end{pmatrix}. \tag{7.1}$$

The __H parameters__ are

<span class="anker" id="gl-7-2"></span>
$$H_{11}=\left.\frac{U_1}{I_1}\right|_{U_2=0},\quad H_{21}=\left.\frac{I_2}{I_1}\right|_{U_2=0},\quad H_{12}=\left.\frac{U_1}{U_2}\right|_{I_1=0},\quad H_{22}=\left.\frac{I_2}{U_2}\right|_{I_1=0}. \tag{7.2}$$
:::

⁠**How to read it:** $H_{11}$ is the __short-circuit input resistance__ in $\Omega$, typically a few k$\Omega$ for the transistor. $H_{21}$ is the forward __short-circuit current ratio__, the current gain, without a unit, about 100 to 500. $H_{12}$ is the __open-circuit reverse voltage ratio__, without a unit, around $10^{-4}$. $H_{22}$ is the __open-circuit output conductance__ in S, a few tens of µ S. The units are mixed, hence the name. The matrix is also called the series-parallel matrix (Stage [9](zusammenschaltung.html#stufe-9)). In the equivalent circuit (Fig. [9](#abb-9) left), voltages add at the input: a series connection of $H_{11}$ and a VCVS $H_{12}U_2$. Currents add at the output: a parallel connection of $H_{22}$ and a CCCS $H_{21}I_1$.

:::abbildung et1/k6hesb 9
Left: equivalent circuit of the H form, a series connection at the input, a parallel connection at the output. Right: The amplifier model with $H_{12}=0$ and the load 5 k$\Omega$. 10 µ A at the input control 1 mA, of which 0.8 mA flow through the load. The output is at $-4$ V.
:::

::::beispiel
The T two-port with 100 mA at the input and the output short-circuited: $U_1=2.5$ V, and the current divides in half, $I_2=-50$ mA, so $H_{11}=25\,\Omega$, $H_{21}=-0.5$. With the input open and $U_2=4$ V: $I_2=100$ mA, $U_1=2$ V, so $H_{22}=25$ mS, $H_{12}=0.5$. The amplifier model of the chapter has $H_{11}=2$ k$\Omega$, $H_{21}=100$, $H_{22}=50$ µ S, that is, an output resistance of 20 k$\Omega$, and $H_{12}=0$. This is an approximation that amounts to around 1 % (Exercise [7](#aufg-7)). At $U_1=20$ mV, $I_1=10$ µ A flows, and the source at the output drives 1 mA into $20\,\text{k}\Omega\parallel5\,\text{k}\Omega=4$ k$\Omega$. This gives $U_2=-4$ V, a voltage gain of $-200$. The minus comes from the fact that $H_{21}I_1$ runs into port 2, so the current flows through the load from below.
::::

⁠**Limiting cases:** For $H_{22}\to0$ the output becomes an ideal current source, for $H_{11}=0$ the input becomes a short circuit. The ideal current-amplifier model is exactly that: $U_1=0$, $I_2=H_{21}I_1$.

:::frage Why does $H_{21}$ have a minus in the T two-port but not in the amplifier?
The T two-port contains no source. A current into port 1 can only run out of port 2, $I_2$ is negative, and its magnitude is smaller than $I_1$. In the amplifier, $H_{21}$ is the law of a controlled source, which itself sets the direction and size of the current and is fed from an auxiliary source.
:::

:::aufgabe Exercise 7 ★★ How much does the reverse action matter?
<span class="anker" id="aufg-7"></span>

The amplifier model is given a small reverse action $H_{12}=5\cdot10^{-5}$, with the other values the same, load 5 k$\Omega$, $I_1=10$ µ A.

<ol class="al">

<li>

Do $U_2$ and $I_2$ change compared with the example? Justify with [(7.1)](#gl-7-1).

</li>

<li>

What is $U_1$ now? By what percentage does it change?

</li>

<li>

What are the voltage gain and the input resistance?

</li>

</ol>

:::loesung
(a) No. The second line of [(7.1)](#gl-7-1) does not contain $H_{12}$, and $I_1$ is fixed: $U_2=-4$ V, $I_2=0.8$ mA. (b) $U_1=20\,\mathrm{mV}+5\cdot10^{-5}\cdot(-4\,\mathrm{V})=19.8$ mV, 1 % less. (c) $U_2/U_1=-202$, $Z_1=19.8\,\mathrm{mV}/10\,\mu\text{A}=1.98$ k$\Omega$. The reverse action is small here, which is why it is often neglected.
:::
:::
