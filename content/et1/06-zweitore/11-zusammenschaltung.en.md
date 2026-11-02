---
title: Stage 9: Interconnection
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1161100
summary: Stage 8 showed that the chain fits the A form.
tags: 
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Stage [8](kettenform.html#stufe-8) showed that the chain fits the A form. This stage answers the question in general: Which form fits which interconnection?
:::

**The idea.** If you connect two two-ports, at each port they share either the current (series) or the voltage (parallel). The shared quantity is equal for both parts, and the other one adds up. That says which form fits: The shared quantities belong to the causes, the summed ones to the effects. Then the right-hand side is the same for both parts, and the parameters add.

:::satz Theorem 9.1 (Interconnection of two two-ports)
<span class="anker" id="satz-9-1"></span>

If the port condition remains intact in both parts, the following holds:

| Connection (port 1, port 2) | equal for both | adds up | Rule |
|---|---|---|---|
| series, series | $I_1$, $I_2$ | $U_1$, $U_2$ | $\mathbf Z=\mathbf Z'+\mathbf Z''$ |
| parallel, parallel | $U_1$, $U_2$ | $I_1$, $I_2$ | $\mathbf Y=\mathbf Y'+\mathbf Y''$ |
| series, parallel | $I_1$, $U_2$ | $U_1$, $I_2$ | $\mathbf H=\mathbf H'+\mathbf H''$ |
| chain | $U_2'=U_1''$, $-I_2'=I_1''$ | nothing | $\mathbf A=\mathbf A'\mathbf A''$ |
:::

⁠**How to read it:** The circuit diagram says which quantities are equal, the table says which form adds (Fig. [11](#abb-11)). This is where the H matrix gets its second name, series-parallel matrix. The connection “parallel, series” is the missing case. It goes with the inverse hybrid form with $U_1$ and $I_2$ as causes, which you get from the inverse of $\mathbf H$.

:::herleitung Why the parameters add
In series, series, both parts carry the same currents: $\mathbf I'=\mathbf I''=\mathbf I$. So $\mathbf U=\mathbf U'+\mathbf U''=\mathbf Z'\mathbf I+\mathbf Z''\mathbf I=(\mathbf Z'+\mathbf Z'')\mathbf I$. In parallel, the same holds with the roles swapped. In series, parallel, the cause column $(I_1,\,U_2)$ is the same for both, and the effect column $(U_1,\,I_2)$ is the sum of the two effect columns.
:::

:::abbildung et1/k6zusammen 11
Three interconnections. Left, series, series: equal currents, Z adds. Center, parallel, parallel: equal voltages, Y adds. Right, series, parallel: equal $I_1$ and $U_2$, H adds.
:::

**Example.** ⁠**Series:** The T two-port itself is a series connection of two separate series resistors and one shunt resistor:

$$\mathbf Z=\begin{pmatrix}15&0\\0&20\end{pmatrix}\Omega+\begin{pmatrix}20&20\\20&20\end{pmatrix}\Omega=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$

⁠**Parallel:** If you place a resistor of 100 $\Omega$ from terminal 1 to terminal 2 across the T two-port, the series conductance is added to $\mathbf Y$:

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}+\begin{pmatrix}10&-10\\-10&10\end{pmatrix}\mathrm{mS}=\begin{pmatrix}50&-30\\-30&45\end{pmatrix}\mathrm{mS}.$$

Check: With port 2 short-circuited, $1/Y_{11}=20\,\Omega$, and directly it is $25\,\Omega\parallel100\,\Omega=20\,\Omega$.

**When the rule fails.** The rules assume that each part keeps the port condition on its own. In the chain this is safe, because for the front part, the rear part together with the load is a two-terminal element. Two three-poles with a common ground line may also be connected in parallel: For them, 1$'$ and 2$'$ coincide in one point, and only the sum of the return currents counts. Caution is needed in series. If you stack two T two-ports with their ground lines, the ground line of the upper one short-circuits the two upper terminals of the lower one. Part of the current of port 1 then runs through $R_\mathrm{c}$ in the lower T, and the port condition breaks. Instead of $Z_{11}=70\,\Omega$ you measure $35\,\Omega+15\,\Omega\parallel20\,\Omega+20\,\Omega=63.6\,\Omega$. The remedy: Mirror the lower T so that only the two ground lines are connected. Then both remain three-poles, and the rule gives the correct 70 $\Omega$.

⁠**Limiting case:** Two identical two-ports in parallel have half the matrix $\mathbf Z$; equal resistors in parallel give half the resistance. In series, $\mathbf Z$ doubles.

:::frage Why doesn't the chain matrix add in series too?
Because in series $I_1$ is equal for both, but $U_1$ is not. In the chain form, $U_1$ stands together with $I_1$ on the left-hand side, and the output quantities would stand on the right. The right column would differ for the two parts, and nothing could be combined.
:::

:::aufgabe Exercise 9 ★★ Which form fits?
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Two identical T two-ports are connected parallel, parallel. What is $\mathbf Z$ of the circuit? Why is the calculation permissible here?

</li>

<li>

Two identical T two-ports, the lower one mirrored, are in series, series. What is $\mathbf Z$?

</li>

<li>

The hybrid matrix of the T two-port is known. What is $\mathbf H$ for two identical two-ports in series, parallel (assuming the port condition)?

</li>

<li>

A shunt resistor of 10 $\Omega$ is added to the T two-port in series, series. Which $\mathbf Z$ results, and which T network goes with it?

</li>

</ol>

:::loesung
(a) $\mathbf Y$ doubles, so $\mathbf Z$ halves: $Z_{11}=17.5\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=20\,\Omega$. Both are three-poles with a common ground line, and the ports remain ports. (b) $\mathbf Z$ doubles: 70, 40, 40, 80 $\Omega$. (c) $\mathbf H$ doubles: $H_{11}=50\,\Omega$, $H_{12}=1$, $H_{21}=-1$, $H_{22}=50$ mS. (d) $Z_{11}=45\,\Omega$, $Z_{12}=Z_{21}=30\,\Omega$, $Z_{22}=50\,\Omega$. This is a T with $R_\mathrm{a}=15\,\Omega$, $R_\mathrm{b}=30\,\Omega$, $R_\mathrm{c}=20\,\Omega$: The shunt resistor is in series with $R_\mathrm{b}$, because it carries the same sum current.
:::
:::
