---
title: Stage 9: Tangent instead of curve
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1201100
summary: An amplifier works around a fixed point in the active region.
tags: small-signal, partial derivative, input resistance, output resistance, Early voltage, extended equivalent circuit, small-signal equivalent circuit
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
An amplifier works around a fixed point in the active region. There, small changes see not an exponential function but a straight line. This stage reads off its slopes and draws them as an equivalent circuit.
:::

**The idea.** The linear model from Stage [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) has two flaws. It turns the BE path into a fixed voltage, so it has an input resistance of zero. And it makes the output characteristic horizontal, so it sets the conductance to zero. In truth, both slopes are finite. For small changes around the operating point, what was the tangent for the diode ([Part 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) is enough: the terrain from Stage [3](eine-flache-viele-kennlinien.html#stufe-3) becomes a flat inclined plane there, with one slope per direction.

The decomposition is written as follows: total quantity equals DC component plus change, $u_\mathrm{BE}(t)=U_\mathrm{BE}+u_\mathrm{be}(t)$, $i_\mathrm{C}(t)=I_\mathrm{C}+i_\mathrm{c}(t)$. The small letters with small indices are called __small-signal__ quantities. The symbol $\partial$ stands for the __partial derivative__: the derivative with respect to one variable while the others are held fixed, that is, the slope of a slice.

:::definition Definition 9.1 (Small-signal quantities at the operating point)
<span class="anker" id="satz-9-1"></span>

<span class="anker" id="gl-9-1"></span>
$$S=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{I_\mathrm{C}}{U_T},\qquad r_\mathrm{BE}=\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{B}}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S},\qquad G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}=\frac{I_\mathrm{C}}{U_\mathrm{Early}+U_\mathrm{CE}}. \tag{9.1}$$

For the changes this gives

<span class="anker" id="gl-9-2"></span>
$$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}},\qquad i_\mathrm{c}=S\,u_\mathrm{be}+\frac{u_\mathrm{ce}}{r_\mathrm{CE}}. \tag{9.2}$$
:::

⁠**How to read it:** The transconductance $S$ in A/V is the slope of the control characteristic, $r_\mathrm{BE}$ the __input resistance__, the slope of the input characteristic read inversely. $r_\mathrm{CE}$ is the __output resistance__. The straight lines of the output characteristics, extended to the left, meet at $-U_\mathrm{Early}$. The __Early voltage__ $U_\mathrm{Early}$ typically lies between 50 V and 200 V; for T it is 74 V. Mechanism: more $U_\mathrm{CB}$ widens the space-charge region into the base. The base becomes narrower, the density gradient steeper, the current larger. **Validity:** active region and $|u_\mathrm{be}|\ll U_T$.

:::herleitung The slopes
From $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$ follows $\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{1}{U_T}I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}=\frac{I_\mathrm{C}}{U_T}$. The derivative of an exponential function is the function itself divided by the scale in the exponent. Likewise, $\partial I_\mathrm{B}/\partial U_\mathrm{BE}=I_\mathrm{B}/U_T$. The reciprocal is $r_\mathrm{BE}$. With $I_\mathrm{B}=I_\mathrm{C}/B$ follows $r_\mathrm{BE}=B/S$. The third factor in [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1) gives $\partial I_\mathrm{C}/\partial U_\mathrm{CE}=I_\mathrm{C}/(74\,\mathrm{V}+U_\mathrm{CE})$. At point A that makes 80 V in the denominator. The sum in [(9.2)](#gl-9-2) is the tangent plane, which combines both directions.
:::

:::abbildung et1/k10tangente 10
Left, the control characteristic with the tangent at point A (2 mA), slope $S=76.9$ mS. Right, output characteristics for two values of $U_\mathrm{BE}$. The separation of the curves is the effect of $S$. The slope of each curve is $1/r_\mathrm{CE}$; extended to the left, they reach $-74$ V.
:::

::::beispiel
At point A, $S=2\,\mathrm{mA}/26\,\mathrm{mV}=76.9$ mS, so $1/S=13\,\Omega$, and in addition $r_\mathrm{BE}=200/S=2.6$ k$\Omega$ and $r_\mathrm{CE}=80\,\mathrm{V}/2\,\mathrm{mA}=40$ k$\Omega$. Mechanism of $S$: 1 mV more $U_\mathrm{BE}$ lowers the barrier, and according to the tangent the injection rises by 3.85 %, which is 77 µ A. To achieve the same via the output, one would need 3 V at $U_\mathrm{CE}$.
::::

⁠**In short:** the transconductance is the current divided by $U_T$, independent of $B$ and $I_\mathrm{S}$. **Limiting cases:** $I_\mathrm{C}\to0$ gives $S\to0$: without a quiescent current there is no control effect. $U_\mathrm{Early}\to\infty$ gives $r_\mathrm{CE}\to\infty$, the ideal current source.

**How small is small?** Exactly, $i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$; the tangent says $I_\mathrm{C}u_\mathrm{be}/U_T$. At $u_\mathrm{be}=+1$ mV the error is 2 %, at $+5$ mV it is 10 % ($+424$ µ A instead of $+385$ µ A), whereas at $-5$ mV only $-350$ µ A flow. The positive half-wave becomes larger than the negative one, and the signal is distorted. At 26 mV the tangent is useless.

**From the model to the equivalent circuit.** The tangents become components (Fig. [11](#abb-11)). The __extended equivalent circuit__ contains the DC components. In the input, a source $U_0$ and $r_\mathrm{BE}$ lie in series. Here $U_0=U_\mathrm{BE}-U_T=0.574$ V is the point at which the tangent to the input characteristic meets the axis. In the output, a controlled current source $I$ and $r_\mathrm{CE}$ lie in parallel. At point A it delivers $I=1.85$ mA, and the remaining 0.15 mA flow through $r_\mathrm{CE}$. Leaving out the DC components leaves the __small-signal equivalent circuit__. Constant sources disappear in the process: a constant voltage becomes a wire, and this also applies to $U_\mathrm{CC}$ (superposition, [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). The rule for the translation is: if a current depends on the voltage across its own terminal pair, it is a resistor. If it depends on another voltage, it is a controlled source, here a voltage-controlled current source (VCCS, [Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Expressed as a two-port, these are the Y parameters $Y_{11}=1/r_\mathrm{BE}$, $Y_{12}=0$, $Y_{21}=S$, $Y_{22}=G_\mathrm{CE}$.

:::abbildung et1/k10kleinsignal 11
Left, the extended equivalent circuit for DC quantities in conducting operation. Right, the small-signal equivalent circuit: the constants have disappeared, only the slopes remain. The source $S\,u_\mathrm{be}$ is the tangent in the direction of $U_\mathrm{BE}$, $r_\mathrm{CE}$ the one in the direction of $U_\mathrm{CE}$.
:::

:::frage Isn't the transconductance the slope in the family of output characteristics?
No. There $U_\mathrm{CE}$ is the horizontal axis, so the slope is $1/r_\mathrm{CE}$. The transconductance belongs to the direction of $U_\mathrm{BE}$ and appears in the output family as the vertical separation between two curves, divided by their difference in $U_\mathrm{BE}$.
:::

:::frage Why is $1/S=13\,\Omega$ but $r_\mathrm{BE}=2.6$ k$\Omega$? After all, both measure the same voltage.
Both divide the voltage change by a current, but by different ones. $1/S$ divides by the change in $I_\mathrm{C}$, $r_\mathrm{BE}$ by the $B$ times smaller change in $I_\mathrm{B}$. That is why the input resistance is $B$ times larger. The ratio here is 200.
:::

:::aufgabe Exercise 11 ★★ Small-signal quantities
<span class="anker" id="aufg-11"></span>

T operates at $I_\mathrm{C}=0.5$ mA and $U_\mathrm{CE}=6$ V. (a) Determine $S$, $1/S$, $r_\mathrm{BE}$ and $r_\mathrm{CE}$. (b) For $u_\mathrm{be}=\pm5$ mV, compare the exact current change with the tangent. (c) Predict: How do the four values from (a) change if the current becomes twice as large?

:::loesung
(a) $S=19.2$ mS, $1/S=52\,\Omega$, $r_\mathrm{BE}=200/S=10.4$ k$\Omega$, $r_\mathrm{CE}=80\,\mathrm{V}/0.5\,\mathrm{mA}=160$ k$\Omega$.

(b) Tangent $\pm96$ µ A. Exact: $+106$ µ A and $-87$ µ A.

(c) $S$ doubles; $1/S$, $r_\mathrm{BE}$ and $r_\mathrm{CE}$ halve. All four are proportional or inversely proportional to the current.
:::
:::
