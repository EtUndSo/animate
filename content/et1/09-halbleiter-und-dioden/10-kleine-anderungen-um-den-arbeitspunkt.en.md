---
title: Stage 8: Small changes around the operating point
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Semiconductors and Diodes
order: 1191000
summary: Often a small signal rides on a DC voltage, and only the change counts.
tags: differential resistance, small signal
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Often a small signal rides on a DC voltage, and only the change counts. This stage shows that for small changes the diode acts like a resistor whose value is set by the direct current.
:::

**The idea.** Close to the OP, every smooth curve coincides with its tangent (Fig. [10](#abb-10)). The mechanism: 1 mV more lowers the barrier by 1 meV. This raises the fraction above the barrier by $1/25.85=3.9$ %, and always by the same percentage of the present current. So a large current means a large absolute change and thus a small resistance.

:::abbildung et1/k9kleinsignal 10
Left: section of the characteristic curve around the OP (0.692 V | 4.31 mA). The tangent has the slope $1/r=0.167$ S and meets the axis at $U_\mathrm D-U_T=0.667$ V. Right: for the small signal the DC voltage source is gone, and the diode is the resistor $r$.
:::

:::satz Theorem 8.1 (Differential resistance)
<span class="anker" id="satz-8-1"></span>

At the OP with the direct current $I$, for small changes $u_\mathrm D$ and $i$,

<span class="anker" id="gl-8-1"></span>
$$r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}=\frac{U_T}{I+I_\mathrm S}\approx\frac{U_T}{I},\qquad u_\mathrm D=r\,i. \tag{8.1}$$
:::

⁠**How to read it:** $r$ is called the __differential resistance__; at 1 mA it is 25.85 $\Omega$. Lowercase letters are the deviations from the OP, the __small signal__. **Validity:** $|u_\mathrm D|\ll U_T$. At 1 mV the error is 2 %, at 5 mV 10 %, at 25.85 mV already 72 %.

:::herleitung Slope of the characteristic curve
Differentiating [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1): $\mathrm{d} I/\mathrm{d} U_\mathrm D=(I_\mathrm S/U_T)\,\mathrm{e}^{U_\mathrm D/U_T}=(I+I_\mathrm S)/U_T$. The reciprocal is $r$. The exponential function reproduces itself under differentiation, which is why only $I$ appears in the result, and $I_\mathrm S$ drops out in the forward direction. Two diodes with different $I_\mathrm S$ have the same $r$ at the same current.
:::

::::beispiel
In the reference model, $r=25.85\,\mathrm{mV}/4.31\,\mathrm{mA}=6.0\,\Omega$. A sine with a peak value of 100 mV is added to the source. For the changes, $R$ and $r$ form a voltage divider:

$$\hat u_\mathrm D=100\,\mathrm{mV}\cdot\frac{6.0\,\Omega}{1000\,\mathrm{\Omega}+6.0\,\Omega}=0.60\,\mathrm{mV},\qquad\hat\imath=\frac{100\,\mathrm{mV}}{1006\,\mathrm{\Omega}}=99.4\,\mu\text{A}.$$

The exact calculation for $U_0=5.1$ V gives $+0.59$ mV and $+99.4$ µ A. Almost all of the signal appears across the resistor; 0.6 % remains at the diode.
::::

⁠**Limiting cases:** For $I\to0$, $r=U_T/I_\mathrm S=2.6\,\mathrm{T\Omega}$, and the diode isolates. For large $I$, $r$ tends to zero; in reality the bulk resistance remains.

:::ltspice Operating point and signal
⁠**Draw:** source `voltage` from `in` to ground, value `5`, under `Advanced` enter `1` for AC Amplitude. `res` 1k from `in` to `d`, `diode` DM from `d` to ground, model as above.

⁠**Directives:** first `.op`, then `.ac dec 1 1k 10k`

⁠**What you see:** With `.op`, $V(d)=0.693$ V and $I(D1)=4.31$ mA. With `.ac`, $V(d)$ shows $-44.5$ dB, that is, the ratio 0.00597. That is $r/(R+r)$ from the example. For Exercise [10](#aufg-10), change the values and read off your $r$.
:::

:::frage Why is the resistance of the diode not $U_\mathrm D/I$?
That would be the reciprocal of the slope of the line from the origin to the OP: $0.692\,\mathrm{V}/4.31\,\mathrm{mA}=161\,\Omega$. It describes which resistor would carry the same current at the OP, but it is not a property of the characteristic curve at this point. How strongly the current responds to a change is told only by the tangent, and that is 27 times steeper. For an ohmic resistor the two coincide.
:::

:::aufgabe Exercise 10 ★★ Slope and tangent
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Calculate $r$ at 2 mA and at 20 mA.

</li>

<li>

At 2 mA the voltage rises by 10 mV. What current does the tangent predict, and what does the characteristic curve give? Why does the tangent lie below?

</li>

<li>

Three identical diodes in series carry 2 mA from 12 V through a resistor. Calculate the voltage across the three diodes and the resistor. By how much does the voltage across the diodes change when the source rises by 1 V?

</li>

</ol>

:::loesung
(a) 12.9 $\Omega$ and 1.29 $\Omega$. (b) Tangent: $2\,\mathrm{mA}+10\,\mathrm{mV}/12.9\,\Omega=2.77$ mA. Characteristic curve: $2\,\mathrm{mA}\cdot\mathrm{e}^{0.387}=2.94$ mA. An exponential curve bends upward and always lies above its tangent. (c) Voltage $3\cdot0.673\,\mathrm{V}=2.02$ V, $R=(12\,\mathrm{V}-2.02\,\mathrm{V})/2\,\mathrm{mA}=5.0\,\mathrm{k\Omega}$. The three diodes together have $r=38.8\,\Omega$. So 1 V becomes $1\,\mathrm{V}\cdot38.8/5039=7.7$ mV.
:::
:::
