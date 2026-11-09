---
title: Stage 4: The two-port in operation
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160600
summary: In operation, no port is open.
tags: reverse action, unilateral
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
In operation, no port is open. This stage shows how the load acts back on the input through the parameter $Z_{12}$ and what the two-port is for the load.
:::

**The idea.** The load draws a current from port 2, so $I_2\neq0$. Through the source $Z_{12}I_2$, this current appears as a voltage at the input. In the T two-port you can grasp this directly: Part of the current that would otherwise flow through $R_\mathrm{b}$ escapes through $R_\mathrm{c}$ to the load. Less drops across $R_\mathrm{b}$, $U_1$ falls, and the input looks lower in resistance. This effect of the output on the input is called __reverse action__.

:::satz Theorem 4.1 (Input resistance and output side)
<span class="anker" id="satz-4-1"></span>

With the load $Z_\mathrm{L}$ at port 2, $U_2=-Z_\mathrm{L}I_2$ and

<span class="anker" id="gl-4-1"></span>
$$I_2=-\frac{Z_{21}}{Z_{22}+Z_\mathrm{L}}\,I_1,\qquad Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}. \tag{4.1}$$

The limiting cases are the open-circuit and the short-circuit input resistance:

<span class="anker" id="gl-4-2"></span>
$$Z_{1,\mathrm{OC}}=Z_{11},\qquad Z_{1,\mathrm{SC}}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}. \tag{4.2}$$

If a source $U_\mathrm{q}$, $R_\mathrm{q}$ feeds port 1, port 2 acts as an equivalent voltage source ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) with

<span class="anker" id="gl-4-3"></span>
$$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q},\qquad R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}. \tag{4.3}$$
:::

⁠**How to read it:** $Z_\mathrm{L}$ is the load, here a resistor. The minus sign in $U_2=-Z_\mathrm{L}I_2$ is there because $I_2$ points into the two-port and so against the current through the load. The fraction in [(4.1)](#gl-4-1) is the amount by which the load changes the input resistance. If $Z_{12}=0$, it is zero: The input notices nothing of the load, and the two-port is called __unilateral__. **Validity:** The two-port must be linear; the formulas for the equivalent source assume a linear source.

:::herleitung Input resistance and output side
Right mesh: $U_2=Z_{21}I_1+Z_{22}I_2=-Z_\mathrm{L}I_2$; solving for $I_2$ gives the first part of [(4.1)](#gl-4-1). Substituting into the left mesh $U_1=Z_{11}I_1+Z_{12}I_2$ and dividing by $I_1$ gives $Z_1$. For $Z_\mathrm{L}\to\infty$ the fraction vanishes; for $Z_\mathrm{L}=0$, $Z_{1,\mathrm{SC}}$ follows with $I_2=-Z_{21}I_1/Z_{22}$.

For [(4.3)](#gl-4-3) you replace the load. The source imposes $U_1=U_\mathrm{q}-R_\mathrm{q}I_1$. At $I_2=0$, $I_1=U_\mathrm{q}/(Z_{11}+R_\mathrm{q})$ and $U_\mathrm{i}=Z_{21}I_1$. With $U_\mathrm{q}=0$, port 1 is terminated by $R_\mathrm{q}$, and $R_\mathrm{i}$ is $Z_1$ with swapped indices.
:::

:::abbildung et1/k6betrieb 5
Equivalent circuit of the T two-port with source and load. The currents are $I_1=250$ mA and $I_2=-50$ mA. The reverse action amounts to $Z_{12}I_2=-1$ V, and the forward source supplies $Z_{21}I_1=5$ V. The input shows 31 $\Omega$ instead of 35 $\Omega$.
:::

::::beispiel
For the T two-port, $Z_{1,\mathrm{OC}}=35\,\Omega$ and $Z_{1,\mathrm{SC}}=35\,\Omega-400\,\Omega^2/40\,\Omega=25\,\Omega$, which is $R_\mathrm{a}+R_\mathrm{b}\parallel R_\mathrm{c}$. With $R_\mathrm{L}=60\,\Omega$,

$$Z_1=35\,\Omega-\frac{400\,\Omega^2}{100\,\Omega}=31\,\Omega,\quad I_1=\frac{9\,\mathrm{V}}{5\,\Omega+31\,\Omega}=250\,\mathrm{mA},\quad I_2=-\frac{20}{100}\,I_1=-50\,\mathrm{mA}.$$

At the input, $U_1=9\,\mathrm{V}-5\,\Omega\cdot250\,\mathrm{mA}=7.75$ V, at the output $U_2=60\,\Omega\cdot50\,\mathrm{mA}=3$ V. In $R_\mathrm{b}$, $I_1+I_2=200$ mA flows instead of 250 mA, which lowers $U_1$ by exactly 1 V (Fig. [5](#abb-5)). Seen from the load: $U_\mathrm{i}=\frac{20}{40}\cdot9\,\mathrm{V}=4.5$ V, $R_\mathrm{i}=40\,\Omega-400\,\Omega^2/40\,\Omega=30\,\Omega$. Then $I=4.5\,\mathrm{V}/90\,\Omega=50$ mA, the same current. So the equivalent source from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) is contained in the four numbers.
::::

⁠**Limiting cases:** $R_\mathrm{L}\to\infty$ gives $Z_1\to35\,\Omega$, $R_\mathrm{L}\to0$ gives $25\,\Omega$. Every load lies in between.

:::frage The load is connected only to port 2. How does the input know about it?
Through the shared components. In the T two-port, both ports lead through $R_\mathrm{b}$, and its voltage drop depends on $I_1+I_2$. In general, $Z_{12}$ is the measure of this coupling. No signal transmission back is needed; the voltages in the network settle together.
:::

:::ltspice T two-port in operation
⁠**Draw:** source `voltage` with `9` from `q` to ground, `res` with `5` from `q` to `1`, `Ra` with `15` from `1` to `m`, `Rb` with `20` from `m` to ground, `Rc` with `20` from `m` to `2`, `RL` with `{RL}` from `2` to ground.

⁠**Directives:** `.param RL=60`, `.op`, `.meas op Uin FIND V(1)`, `.meas op Iin FIND I(Ra)`, `.meas op Zin PARAM Uin/Iin`, `.meas op Uout FIND V(2)`.

⁠**What you see:** $\mathtt{V(1)}=7.75$ V, $\mathtt{I(Ra)}=250$ mA, `Zin` $=31\,\Omega$, $\mathtt{V(2)}=3$ V. With `RL=1m`, `Zin` becomes 25.0 $\Omega$; with `RL=1G`, it becomes 35.0 $\Omega$ and $\mathtt{V(2)}=4.5$ V, the voltage $U_\mathrm{i}$. Set `RL=10` and check Exercise [4](#aufg-4)(a) and (c).
:::

:::aufgabe Exercise 4 ★★ The load on the T two-port
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

What is $Z_1$ for $R_\mathrm{L}=10\,\Omega$?

</li>

<li>

At which load does the input show $Z_1=30\,\Omega$?

</li>

<li>

For $R_\mathrm{L}=10\,\Omega$ with the source connected, calculate the currents $I_1$, $I_2$ and $U_2$. Check the load current with the equivalent source.

</li>

</ol>

:::loesung
(a) $Z_1=35\,\Omega-400\,\Omega^2/50\,\Omega=27\,\Omega$. (b) $400\,\Omega^2/(40\,\Omega+R_\mathrm{L})=5\,\Omega$, so $R_\mathrm{L}=40\,\Omega$. (c) $I_1=9\,\mathrm{V}/32\,\Omega=281.25$ mA, $I_2=-\frac{20}{50}I_1=-112.5$ mA, $U_2=1.125$ V. The equivalent source gives $4.5\,\mathrm{V}/(30\,\Omega+10\,\Omega)=112.5$ mA.
:::
:::
