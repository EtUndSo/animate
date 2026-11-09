---
title: Stage 10: Properties and overview of all forms
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1161200
summary: The four numbers reveal more than the behavior at the ports.
tags: reciprocal, active, passive, small-signal operation
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
The four numbers reveal more than the behavior at the ports. This stage reads three properties from them: Does the two-port act equally in both directions? Does it act back at all? Can it gain power? At the end, all the forms stand side by side.
:::

**The idea.** A resistor knows no direction; its current depends only on the voltage difference of its two ends. That is why a network of resistors acts just as strongly from port 1 to port 2 as the other way around: If you swap the cause and the place of the effect, the quotient stays the same. A controlled source, by contrast, has a direction. It acts from the controlling quantity on its output, never back. Only it can break the symmetry. It alone can also bring in energy from outside.

:::definition Definition 10.1 (Reciprocal, unilateral, active)
<span class="anker" id="satz-10-1"></span>

A two-port is called __reciprocal__ (also reversible, transfer-symmetric) if the same cause shows the same effect in both directions. It is called unilateral if the input does not depend on the output:

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} \text{reciprocal:}\quad&Z_{12}=Z_{21},\quad Y_{12}=Y_{21},\quad H_{12}=-H_{21},\quad\det\mathbf A=1,\\ \text{unilateral:}\quad&Z_{12}=0,\quad Y_{12}=0,\quad H_{12}=0,\quad\det\mathbf A=0. \end{aligned} \tag{10.1|10.2}$$

With $P_1=U_1I_1$ and the delivered power $P_2=-U_2I_2$, the power absorbed by the two-port is

<span class="anker" id="gl-10-3"></span>
$$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2. \tag{10.3}$$

The two-port is __active__ if $P<0$ is possible in some operating state, and __passive__ if $P\ge0$ always holds.
:::

⁠**How to read it:** If 1 A into port 1 produces a voltage at open port 2, then in a reciprocal two-port 1 A into port 2 produces the same voltage at open port 1 (Fig. [12](#abb-12)). That is $Z_{21}=Z_{12}$. In the node equations ([Part 8](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren/maschenstrom-und-knotenpotential.html)), each resistor enters its conductance at two mirrored places, which is why the matrix stays symmetric. Reciprocal does not mean mirror-symmetric: The T two-port has $Z_{11}\neq Z_{22}$ and is reciprocal all the same. Because the fourth parameter is fixed, a reciprocal two-port has only three free parameters, matching the three elements of T and $\pi$. It can always be reproduced by a source-free T or $\pi$ network; the element values may be negative. In a unilateral two-port, three numbers are likewise free: input resistance, output resistance, control quantity. This is the basic form of the amplifier. The conditions for $\mathbf A$ and $\mathbf H$ follow from the conversions below. In [(10.3)](#gl-10-3) the minus is at $P_2$ because $I_2$ points in. The last form arises by substituting [(5.1)](admittanzform-und-kurzschlussversuch.html#gl-5-1).

:::abbildung et1/k6umkehr 12
Left: T two-port. 100 mA give 2 V at the other, open port in both directions, even though $R_\mathrm{a}\neq R_\mathrm{c}$. Right: amplifier model. 1 µ A at port 1 gives $-2$ V at port 2, 1 µ A at port 2 gives 0 V at port 1.
:::

::::beispiel
The T two-port absorbs $P_1=7.75\,\mathrm{V}\cdot250\,\mathrm{mA}=1.9375$ W and delivers $P_2=3\,\mathrm{V}\cdot50\,\mathrm{mA}=0.15$ W. The difference $P=1.7875$ W is exactly the heat in the resistors: $0.9375+0.8+0.05$ W. Each resistor absorbs $I^2R\geq0$, which is why a two-port of resistors is always passive. This also holds with capacitors and coils. Passive two-ports may even contain controlled sources; $P$ alone decides. The amplifier model absorbs $P_1=20\,\mathrm{mV}\cdot10\,\mu\text{A}=0.2$ µ W and delivers $P_2=4\,\mathrm{V}\cdot0.8\,\mathrm{mA}=3.2$ mW to the load, 16 000 times more. It is active. The energy does not come from the input signal but from an auxiliary source for the power supply, which does not appear in the two-port model. This model applies to small signals around a fixed DC state (__small-signal operation__, [Part 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
::::

⁠**Limiting cases:** For $U_1=U_2=0$, $P=0$. A two-port of ideal wires has $P=0$ in every state; it is passive, and nothing is lost.

:::ltspice Where the power comes from
⁠**Draw:** source `voltage` with `20m` from `1` to ground, `Rin` with `2k` from `1` to ground. The controlled current source `g` with `50m`: output from `2` to ground, control input from `1` to ground. `res` with `20k` and `res` with `5k` from `2` to ground. The value is $Y_{21}=H_{21}/H_{11}$.

⁠**Directives:** `.op`, `.meas op Uout FIND V(2)`, `.meas op Pin PARAM V(1)*I(Rin)`, `.meas op Pload PARAM V(2)*V(2)/5000`, `.meas op Pg PARAM V(2)*I(G1)`.

⁠**What you see:** $\mathtt{Uout}=-4$ V, `Pin` $=0.2$ µ W, `Pload` $=3.2$ mW, `Pg` $=-4$ mW. The controlled source delivers 4 mW, of which 3.2 mW go to the load; the rest heats the 20 k$\Omega$. For Exercise [10](#aufg-10)(b), set the values `10m`, `1k`, `50m`, `50k` and `10k`: $\mathtt{Uout}=-4.17$ V.
:::

**All forms at a glance.** The same four quantities, four choices of causes:

| Form | Causes | Effects | T two-port |
|---|---|---|---|
| Z (resistance matrix) | $I_1$, $I_2$ | $U_1$, $U_2$ | $Z_{11}=35\,\Omega$, $Z_{12}=Z_{21}=20\,\Omega$, $Z_{22}=40\,\Omega$ |
| Y (conductance matrix) | $U_1$, $U_2$ | $I_1$, $I_2$ | $Y_{11}=40$ mS, $Y_{12}=Y_{21}=-20$ mS, $Y_{22}=35$ mS |
| H (series-parallel matrix) | $I_1$, $U_2$ | $U_1$, $I_2$ | $H_{11}=25\,\Omega$, $H_{12}=0.5$, $H_{21}=-0.5$, $H_{22}=25$ mS |
| A (chain matrix) | $U_2$, $-I_2$ | $U_1$, $I_1$ | $A_{11}=1.75$, $A_{12}=50\,\Omega$, $A_{21}=50$ mS, $A_{22}=2$ |

Each conversion arises by solving the two equations for the new quantities. For reference, each wanted matrix from the three others:

$$\mathbf Z=\begin{pmatrix}\frac{Y_{22}}{\det\mathbf Y}&\frac{-Y_{12}}{\det\mathbf Y}\\[3pt]\frac{-Y_{21}}{\det\mathbf Y}&\frac{Y_{11}}{\det\mathbf Y}\end{pmatrix} =\begin{pmatrix}\frac{\det\mathbf H}{H_{22}}&\frac{H_{12}}{H_{22}}\\[3pt]\frac{-H_{21}}{H_{22}}&\frac{1}{H_{22}}\end{pmatrix} =\begin{pmatrix}\frac{A_{11}}{A_{21}}&\frac{\det\mathbf A}{A_{21}}\\[3pt]\frac{1}{A_{21}}&\frac{A_{22}}{A_{21}}\end{pmatrix},$$

$$\mathbf Y=\begin{pmatrix}\frac{Z_{22}}{\det\mathbf Z}&\frac{-Z_{12}}{\det\mathbf Z}\\[3pt]\frac{-Z_{21}}{\det\mathbf Z}&\frac{Z_{11}}{\det\mathbf Z}\end{pmatrix} =\begin{pmatrix}\frac{1}{H_{11}}&\frac{-H_{12}}{H_{11}}\\[3pt]\frac{H_{21}}{H_{11}}&\frac{\det\mathbf H}{H_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{22}}{A_{12}}&\frac{-\det\mathbf A}{A_{12}}\\[3pt]\frac{-1}{A_{12}}&\frac{A_{11}}{A_{12}}\end{pmatrix},$$

$$\mathbf H=\begin{pmatrix}\frac{\det\mathbf Z}{Z_{22}}&\frac{Z_{12}}{Z_{22}}\\[3pt]\frac{-Z_{21}}{Z_{22}}&\frac{1}{Z_{22}}\end{pmatrix} =\begin{pmatrix}\frac{1}{Y_{11}}&\frac{-Y_{12}}{Y_{11}}\\[3pt]\frac{Y_{21}}{Y_{11}}&\frac{\det\mathbf Y}{Y_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{12}}{A_{22}}&\frac{\det\mathbf A}{A_{22}}\\[3pt]\frac{-1}{A_{22}}&\frac{A_{21}}{A_{22}}\end{pmatrix},$$

$$\mathbf A=\begin{pmatrix}\frac{Z_{11}}{Z_{21}}&\frac{\det\mathbf Z}{Z_{21}}\\[3pt]\frac{1}{Z_{21}}&\frac{Z_{22}}{Z_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-Y_{22}}{Y_{21}}&\frac{-1}{Y_{21}}\\[3pt]\frac{-\det\mathbf Y}{Y_{21}}&\frac{-Y_{11}}{Y_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-\det\mathbf H}{H_{21}}&\frac{-H_{11}}{H_{21}}\\[3pt]\frac{-H_{22}}{H_{21}}&\frac{-1}{H_{21}}\end{pmatrix}.$$

From $\mathbf A$ follows the condition in [(10.1)](#gl-10-1) and [(10.2)](#gl-10-2): With the first line, $Z_{12}=\det\mathbf A/A_{21}$ and $Z_{21}=1/A_{21}$, so $\det\mathbf A=Z_{12}/Z_{21}$. This is 1 for reciprocity and 0 for a unilateral two-port. Likewise $Z_{12}=H_{12}/H_{22}$ and $Z_{21}=-H_{21}/H_{22}$, hence $H_{12}=-H_{21}$.

:::frage So non-reciprocal means active?
No. Reciprocity is a statement about symmetry, activity one about power. Both are tied to controlled sources, but they are not the same thing. Exercise [10](#aufg-10)(d) shows a two-port with $Z_{12}\neq Z_{21}$ that never gains power.
:::

:::aufgabe Exercise 10 ★★ Reading off properties
<span class="anker" id="aufg-10"></span>

Check for each two-port: Is it reciprocal? Unilateral? Active or passive?

<ol class="al">

<li>

$Y_{11}=2$ mS, $Y_{12}=Y_{21}=-1$ mS, $Y_{22}=3$ mS. Tip: Draw the $\pi$ network.

</li>

<li>

$H_{11}=1$ k$\Omega$, $H_{12}=0$, $H_{21}=50$, $H_{22}=20$ µ S, load 10 k$\Omega$, $U_1=10$ mV.

</li>

<li>

$A_{11}=2$, $A_{12}=30\,\Omega$, $A_{21}=0.1$ S, $A_{22}=2$.

</li>

<li>

$Z_{11}=Z_{22}=10\,\Omega$, $Z_{12}=5\,\Omega$, $Z_{21}=-5\,\Omega$. For this, calculate $P$ from $U_1I_1+U_2I_2$.

</li>

</ol>

:::loesung
(a) Reciprocal, $Y_{12}=Y_{21}$, not unilateral. $\pi$ network with $G_2=1$ mS, $G_1=1$ mS, $G_3=2$ mS, all positive: resistors, so passive.

(b) $H_{12}=0$: unilateral, not reciprocal ($H_{21}\neq-H_{12}$). $I_1=10$ µ A, and the output drives 0.5 mA into $50\,\text{k}\Omega\parallel10\,\text{k}\Omega=8.33$ k$\Omega$, $U_2=-4.17$ V. $P_1=0.1$ µ W, $P_2=U_2^2/R_\mathrm{L}=1.74$ mW. Active.

(c) $\det\mathbf A=4-3=1$: reciprocal, not unilateral. With $Z_{11}=Z_{22}=20\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, a T of positive resistors 10, 10, 10 $\Omega$: passive, and because $A_{11}=A_{22}$ even mirror-symmetric.

(d) $Z_{12}=5\,\Omega\neq Z_{21}=-5\,\Omega$: not reciprocal, not unilateral. $P=I_1(10I_1+5I_2)+I_2(-5I_1+10I_2)=10\,\Omega\,(I_1^2+I_2^2)\geq0$: passive. The mixed terms cancel. This is a non-reciprocal but passive two-port.
:::
:::
