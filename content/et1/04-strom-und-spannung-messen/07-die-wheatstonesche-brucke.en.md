---
title: Stage 6: The Wheatstone bridge
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Measuring Current and Voltage
order: 1140700
summary: R=U/I adds the errors of two readings.
tags: 
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
$R=U/I$ adds the errors of two readings. In the reference model these are $\pm1.1\,\%$ for the voltage and $\pm2\,\%$ for the current, together up to $\pm3.1\,\%$. The bridge needs only one statement from its instrument: zero or not zero.
:::

**The idea.** Two voltage dividers hang on the same source (Fig. [8](#abb-8)). A sensitive instrument connects their midpoints. If both divide in the same ratio, the midpoints are at the same potential, there is no voltage between them, and no current flows through the instrument. You adjust a resistor until the pointer is at zero: the balance. If no current flows, the instrument takes nothing from the circuit. Its internal resistance has no effect, and its scale is not needed.

:::abbildung et1/k4bruecke 8
Left, the principle. Right, the practical implementation: $R_1$ and $R_2$ are the parts of a resistance wire, and the sliding contact sets their ratio.
:::

:::satz Theorem 6.1 (Balance condition)
<span class="anker" id="satz-6-1"></span>

If no current flows through the instrument,

<span class="anker" id="gl-6-1"></span>
$$R_4=R_3\,\frac{R_2}{R_1}. \tag{6.1}$$
:::

⁠**How to read it:** $R_3$ is a precisely known reference resistor. Of $R_1$ and $R_2$, only the adjustable, known ratio counts; their values are irrelevant. $R_4$ is the unknown. The equation contains neither $U_\mathrm q$ nor the internal resistance of the instrument. If the source fluctuates, both midpoints shift equally. **Validity:** exact at balance. How precisely it is hit depends on what small deviation the instrument can still show.

:::herleitung Balance
Without a cross current, the node rule gives $I_1=I_2$ and $I_3=I_4$. Equal potentials of the midpoints give $U_{R2}=U_{R4}$ and $U_{R1}=U_{R3}$. So

$$\frac{U_{R4}}{U_{R3}}=\frac{U_{R2}}{U_{R1}} \quad\Rightarrow\quad \frac{I_4R_4}{I_3R_3}=\frac{I_2R_2}{I_1R_1} \quad\Rightarrow\quad \frac{R_4}{R_3}=\frac{R_2}{R_1}.$$
:::

::::beispiel
With $R_2/R_1=1.8$ and $R_3=1$ k$\Omega$, the pointer is at zero at $R_4=1800\,\Omega$, and both midpoints are at 5.786 V. If $R_3$ and the ratio are each accurate to 0.1 %, $R_4$ is accurate to $\pm0.2\,\%$, more than 15 times better than $U/I$. The accuracy now comes from resistors, and these can be made far more precisely than pointer scales.
::::

⁠**Limiting case:** As $R_4$ grows, the right midpoint runs from 0 to $U_\mathrm q$. The voltage across the instrument changes sign exactly once, so there is exactly one balance position.

:::frage But current does flow in the bridge. What exactly is zero?
Only the current in the cross branch. In the example, 3.214 mA flow through each of the two dividers; the source operates normally.
:::

**Slide wire and decades.** In the slide wire (a uniform resistance wire with a movable contact, length $l$, total resistance $R_0$), at contact position $x$ the lower part is $R_2=R_0\,x/l$ and the upper part $R_1=R_0\,(1-x/l)$. From this, $R_4=R_3\,x/(l-x)$, and $R_0$ drops out. For 1800 $\Omega$ at $l=1$ m, the contact is at $x=642.9$ mm. More precise bridges set $R_3$ in decades: step switches with $9\times100\,\Omega$, $9\times10\,\Omega$, $9\times1\,\Omega$ and $9\times0.1\,\Omega$ each supply one digit, and $R_2/R_1$ is a multiplier switchable in powers of ten. With the factor 10 and the switch setting 180.0 $\Omega$, this gives 1800 $\Omega$ in steps of 1 $\Omega$. A voltmeter also works as a null indicator, because at balance the voltages across $R_2$ and $R_4$ are equal.

:::ltspice The balance does not depend on the instrument
⁠**Draw:** source `voltage` with 9 V on net `o`. `R1` = 1k from `o` to `l`, `R2` = 1.8k from `l` to ground, `R3` = 1k from `o` to `r`, `R4` = `{RX}` from `r` to ground. The meter movement is `Rd` = 2k from `l` to `r`.

⁠**Directives:** `.step param RX 1700 1900 10` and `.op`

⁠**What you see:** Plot `I(Rd)` versus `RX`: the curve passes through zero at 1800; at 1700 it is $+36.4$ µ A, at 1900 $-33.6$ µ A. Set `Rd` to 1 or 1Meg: the curve changes its height, and the zero crossing stays at 1800. At 0.1 % deviation (1801.8 $\Omega$), only 0.63 µ A flow in the meter movement, which is 1.3 % of full-scale deflection. For Exercise [7](#aufg-7): with `R1` = 356.1 and `R2` = 643.9 (contact 1 mm off), the zero crossing moves to 1808 $\Omega$.
:::

:::aufgabe Exercise 7 ★★ Slide wire
<span class="anker" id="aufg-7"></span>

The wire is 1 m long, $R_3=1$ k$\Omega$. (a) Balance is reached at $x=642.9$ mm. How large is $R_4$? (b) The contact can be read to $\pm1$ mm. What error of $R_4$ follows from this? (c) Repeat (b) for $R_3=1.8$ k$\Omega$ and $R_3=100\,\Omega$. Why do you choose $R_3$ on the order of $R_4$?

:::loesung
(a) $R_4=1\,\mathrm{k\Omega}\cdot642.9/357.1=1800\,\Omega$. (b) A shift by $\Delta x$ changes $x/(l-x)$ in relative terms by $\Delta x\,(1/x+1/(l-x))$. That is $1\,\mathrm{mm}\cdot(1/642.9+1/357.1)/\mathrm{mm}=\pm0.44\,\%$.

(c) $R_3=1.8$ k$\Omega$: $x=500$ mm, $\pm0.40\,\%$. $R_3=100\,\Omega$: $x=947.4$ mm, $\pm2.0\,\%$. The error is smallest when the contact is in the middle, that is, at $R_3\approx R_4$. Near the end of the wire, the same millimeter weighs heavily in relative terms.
:::
:::
