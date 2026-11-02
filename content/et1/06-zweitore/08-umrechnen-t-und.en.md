---
title: Stage 6: Conversion, T and $\pi$
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160800
summary: The Z form and the Y form describe the same two-port.
tags: 
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
The Z form and the Y form describe the same two-port. This stage shows how to get from one to the other, and when a form does not exist at all.
:::

**The idea.** The Y form and the Z form are the same two equations. One is solved for the voltages, the other for the currents. So the transition is the solving of a system of equations, and that is what the inverse matrix from the section “From the ground up” does.

:::satz Theorem 6.1 (Conversion between Z and Y)
<span class="anker" id="satz-6-1"></span>

The conductance matrix and the resistance matrix are inverses of each other, $\mathbf Y\cdot\mathbf Z=\mathbf 1$:

<span class="anker" id="gl-6-1"></span>
$$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix},\qquad \mathbf Z=\mathbf Y^{-1}=\frac{1}{\det\mathbf Y}\begin{pmatrix}Y_{22}&-Y_{12}\\-Y_{21}&Y_{11}\end{pmatrix} \tag{6.1}$$

with $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$ and $\det\mathbf Y=Y_{11}Y_{22}-Y_{12}Y_{21}$.
:::

⁠**How to read it:** The whole matrix is inverted, not each number on its own. Each element gets the whole denominator, which is why each Y parameter depends on all the Z parameters. **Validity:** The determinant must not be zero.

:::herleitung Two ways to the inverse
⁠**With matrices.** From $\mathbf I=\mathbf Y\mathbf U$ and $\mathbf U=\mathbf Z\mathbf I$ follows $\mathbf I=\mathbf Y\mathbf Z\,\mathbf I$ for every $\mathbf I$, so $\mathbf Y\mathbf Z=\mathbf 1$.

⁠**With short-circuit tests on the Z equivalent circuit.** At $U_2=0$, $Z_{21}I_1=-Z_{22}I_2$, so $I_2=-\frac{Z_{21}}{Z_{22}}I_1$ and $U_1=\bigl(Z_{11}-Z_{12}\frac{Z_{21}}{Z_{22}}\bigr)I_1$. This gives

$$Y_{11}=\frac{I_1}{U_1}=\frac{Z_{22}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{21}=\frac{I_2}{U_1}=-\frac{Z_{21}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$

At $U_1=0$, $-Z_{11}I_1=Z_{12}I_2$, so $I_1=-\frac{Z_{12}}{Z_{11}}I_2$ and $U_2=\bigl(Z_{22}-Z_{21}\frac{Z_{12}}{Z_{11}}\bigr)I_2$. This gives

$$Y_{12}=-\frac{Z_{12}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{22}=\frac{Z_{11}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$
:::

**T and $\pi$.** The Z matrix of the T network from Stage [3](impedanzform-und-leerlaufversuch.html#stufe-3) can be inverted with [(6.1)](#gl-6-1); the Y matrix of the $\pi$ network can be read directly from short-circuit tests. With $D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}=\det\mathbf Z$ and the conductances $G_1$, $G_3$ in shunt and $G_2$ in series,

<span class="anker" id="gl-6-2"></span>
$$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix},\qquad \mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}. \tag{6.2}$$

Setting the two equal gives $G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$ and $G_3=Y_{22}+Y_{21}$. For $G_3=0$, $\mathbf Y_\pi$ becomes the pair $I_1=(G_1+G_2)U_1-G_2U_2$, $I_2=-G_2U_1+G_2U_2$. This is the star-delta transformation from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): T is the star, $\pi$ the delta. Description by Z parameters leads naturally to the T network, description by Y parameters to the dual $\pi$ network. Conversely, every two-port with $Z_{12}=Z_{21}$ has a T and a $\pi$ equivalent circuit without sources (Stage [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)).

:::abbildung et1/k6tpi 8
Two circuits, the same two-port. Left, the T network with 15, 20 and 20 $\Omega$; right, the equivalent $\pi$ network with 50, 50 and 66.7 $\Omega$. Both have $\det\mathbf Z=1000\,\Omega^2$. At the ports, no measurement can tell them apart.
:::

**Example.** Here $\det\mathbf Z=35\cdot40\,\Omega^2-20\cdot20\,\Omega^2=1000\,\Omega^2$, so

$$\mathbf Y=\frac{1}{1000\,\Omega^2}\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\Omega=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS},$$

exactly the result of the short-circuit tests. The $\pi$ network has $G_2=20$ mS, $G_1=40\,\mathrm{mS}-20\,\mathrm{mS}=20$ mS, $G_3=15$ mS, that is, 50 $\Omega$, 50 $\Omega$ and 66.7 $\Omega$. With the same source and load, it again gives 7.75 V and 3 V.

⁠**Limiting cases: Not every form exists.** A series resistor $R$ and a shunt resistor $R$, each alone between the ports, have

$$\mathbf Y_\text{series}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad\mathbf Z_\text{shunt}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Both determinants are zero. The series resistor has no Z form: There $I_2=-I_1$ always holds, the currents cannot be chosen freely, so they are no good as causes. The shunt resistor has no Y form because $U_1=U_2$ always holds. The same applies to the ideal current-controlled current source: Its currents are rigidly coupled.

:::frage Why is $Y_{11}$ positive but $Y_{21}$ negative?
That comes from the reference arrows. At $U_2=0$, a positive voltage at port 1 drives a current in, $Y_{11}>0$. This current comes out at the other port, but it is counted going in. That is why the transfer conductances of passive circuits like T and $\pi$ are negative.
:::

:::aufgabe Exercise 6 ★ There and back
<span class="anker" id="aufg-6"></span>

A two-port has $Z_{11}=20\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=55\,\Omega$.

<ol class="al">

<li>

Calculate $\mathbf Y$.

</li>

<li>

Determine the resistors of the T and the $\pi$ network.

</li>

<li>

Write down $\mathbf Y$ of a series resistor of 100 $\Omega$. Why does $\mathbf Z=\mathbf Y^{-1}$ fail?

</li>

</ol>

:::loesung
(a) $\det\mathbf Z=20\cdot55\,\Omega^2-10\cdot10\,\Omega^2=1000\,\Omega^2$, so $Y_{11}=55$ mS, $Y_{12}=Y_{21}=-10$ mS, $Y_{22}=20$ mS. (b) T: $R_\mathrm{b}=10\,\Omega$, $R_\mathrm{a}=10\,\Omega$, $R_\mathrm{c}=45\,\Omega$. $\pi$: $G_2=10$ mS, $G_1=45$ mS, $G_3=10$ mS, that is, 100 $\Omega$ in series, 22.2 $\Omega$ and 100 $\Omega$ in shunt. (c) $Y_{11}=Y_{22}=10$ mS, $Y_{12}=Y_{21}=-10$ mS, $\det\mathbf Y=0$. There is no inverse, because $I_2=-I_1$ always holds and the currents cannot be chosen freely.
:::
:::
