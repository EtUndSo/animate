---
title: Stage 6: The operating point
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Semiconductors and Diodes
order: 1190800
summary: For a resistor, U=R\,I gives the result at once.
tags: load line, operating point, Operating point analysis, Operating point synthesis, no load, short circuit, hysteresis, iteration
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
For a resistor, $U=R\,I$ gives the result at once. The diode follows a different curve. This stage finds the voltage and current of the diode in a circuit.
:::

**The idea.** Two conditions must hold at the same time. The diode allows only points on its characteristic curve. The rest of the circuit, source and resistor, allows only points on the __load line__ ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). The circuit finds the intersection by itself: if $U_\mathrm D$ is too small, the resistor supplies more current than the diode lets through. Charge piles up at the node between the two and raises its potential until both currents are equal.

:::abbildung et1/k9arbeitsgerade 8
Circuit of the reference model and graphical solution. Red: the load line through no load and short circuit. Blue: the characteristic curve of the diode, intersection at 0.69 V and 4.31 mA. Green: the characteristic curve of a 250 $\Omega$ resistor in place of the diode, intersection at 1 V and 4 mA.
:::

:::definition Definition 6.1 (Operating point)
<span class="anker" id="satz-6-1"></span>

The __operating point__ (OP) is the point on the characteristic curve fixed by the current through the component and the voltage across it. __Operating point analysis__ means determining it from the given circuit. __Operating point synthesis__ means choosing the components so that a desired OP results.
:::

**The linear case.** If the diode is replaced by a resistor $R_1$, the component equation, the mesh rule and, from them, the load line hold:

<span class="anker" id="gl-6-1"></span>
$$I=\frac{U_{R1}}{R_1},\qquad U_0=U_R+U_{R1}=R\,I+U_{R1},\qquad I=\frac{U_0-U_{R1}}{R}. \tag{6.1}$$

Two linear equations can be solved; with $R_1=250\,\Omega$ it follows that $I=U_0/(R+R_1)=4$ mA and $U_{R1}=1$ V. Solving the system of equations means intersecting the two lines.

:::satz Theorem 6.2 (Operating point of the diode)
<span class="anker" id="satz-6-2"></span>

For the series circuit, both of these hold:

<span class="anker" id="gl-6-2"></span>
$$I=\frac{U_0-U_\mathrm D}{R}\qquad\text{and}\qquad I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr). \tag{6.2}$$

The characteristic curve rises everywhere, the line falls everywhere, so there is exactly one intersection.
:::

⁠**How to read it:** $U_\mathrm D$ is the voltage $U$ from [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1). You draw the load line through two points, ignoring the diode: __no load__ ($I=0$, $U_\mathrm D=U_0$) and __short circuit__ ($U_\mathrm D=0$, $I=U_0/R$). The characteristic curve comes from the equation or a datasheet. **Validity:** Components whose characteristic curve runs back or whose state depends on their history (__hysteresis__) can have several intersections. Several nonlinear components are solved numerically or with equivalent circuits (Stage [7](lineare-ersatzschaltungen.html#stufe-7)).

[(6.2)](#gl-6-2) cannot be solved for $U_\mathrm D$, because $U_\mathrm D$ appears both in the exponent and outside it. You solve graphically or by __iteration__, that is, by repeated substitution: estimate $U_\mathrm D$, calculate $I=(U_0-U_\mathrm D)/R$, then $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$, and repeat.

**Example.** Start with $U_\mathrm D=0.7$ V. Step 1: $I=4.300$ mA, $U_\mathrm D=0.69245$ V. Step 2: $I=4.3076$ mA, $U_\mathrm D=0.69249$ V. So the OP is (0.692 V | 4.31 mA), and 4.31 V is across the resistor. If $U_0$ is doubled to 10 V, the current almost doubles, to 9.29 mA, and $U_\mathrm D$ rises by only 20 mV to 0.712 V. **Limiting cases:** At $U_0=0.5$ V, $I=2.3$ µ A, and almost the whole source voltage stays across the diode. For negative $U_0$, $I=-I_\mathrm S$, and the source is entirely across the diode.

:::frage Why not calculate the other way around: estimate $U_\mathrm D$, get $I$ from the exponential function, then $U_\mathrm D=U_0-R\,I$?
Because this route diverges. An error of 1 mV changes the diode current by 3.9 %, that is, 0.17 mA, and this gives an error of 167 mV across the resistor. In the first method the error shrinks by that same factor each step, $r/R=0.006$ (Stage [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)). The flat logarithm damps, the steep exponential function amplifies.
:::

:::aufgabe Exercise 7 ★★ Finding and setting the operating point
<span class="anker" id="aufg-7"></span>

The diode of the reference model is in series with $R=470\,\Omega$ across $U_0=3$ V.

<ol class="al">

<li>

Determine no load and short circuit of the load line.

</li>

<li>

Iterate from 0.7 V until three digits no longer change.

</li>

<li>

Operating point synthesis: which $R$ gives the current 2 mA at $U_0=5$ V? What current flows with the standard value 2.2 k$\Omega$?

</li>

<li>

The diode is turned around. What do you measure across the diode and the resistor?

</li>

</ol>

:::loesung
(a) No load $U_\mathrm D=3$ V, short circuit $I=3\,\mathrm{V}/470\,\Omega=6.38$ mA. (b) $U_\mathrm D=0.7$ V gives $I=4.894$ mA, which gives $U_\mathrm D=0.6958$ V, then $I=4.903$ mA and again $U_\mathrm D=0.6958$ V. OP: (0.696 V | 4.90 mA). (c) At 2 mA, $U_\mathrm D=0.673$ V, so $R=(5\,\mathrm{V}-0.673\,\mathrm{V})/2\,\mathrm{mA}=2.16\,\mathrm{k\Omega}$. With 2.2 k$\Omega$, 1.97 mA flow. (d) The diode blocks: $I=-10^{-14}$ A, 4.7 pV across the resistor, $-3$ V across the diode.
:::
:::
