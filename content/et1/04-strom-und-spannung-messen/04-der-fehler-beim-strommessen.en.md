---
title: Stage 3: The error in measuring current
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Measuring Current and Voltage
order: 1140400
summary: The ammeter has to go into the circuit.
tags: relative error
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
The ammeter has to go into the circuit. This stage calculates exactly how much its internal resistance lowers the current it is supposed to measure.
:::

**The idea.** To measure, you open the circuit and insert the instrument (Fig. [4](#abb-4)). The mesh now contains $R$ and $R_\mathrm i$. The source holds $U$ fixed and drives less current through the larger total resistance. The reading is correct: it shows the current that flows now. The only mistake is to conclude that the same current also flows without the meter.

:::abbildung et1/k4strom 4
The reference model without and with an ammeter. Across the internal resistance 49.7 mV drop, which are missing across the resistor. The current falls by 0.55 %.
:::

:::satz Theorem 3.1 (Error of the ammeter)
<span class="anker" id="satz-3-1"></span>

Without a meter, $I_R$ flows; with a meter, $I_R'$:

<span class="anker" id="gl-3-1"></span>
$$I_R=\frac UR,\qquad I_R'=\frac{U}{R+R_\mathrm i}<I_R,\qquad \frac{I_R}{I_R'}=\frac{R+R_\mathrm i}{R}=1+\frac{R_\mathrm i}{R}. \tag{3.1}$$

The __relative error__ is $f=(I_R'-I_R)/I_R=-R_\mathrm i/(R+R_\mathrm i)$. For $R_\mathrm i\ll R$, $f\approx-R_\mathrm i/R$.
:::

⁠**How to read it:** $U$ is the source voltage in V, $R$ the resistance of the circuit, $R_\mathrm i$ that of the meter. The primed current is the current with the meter. In general, $f=(\text{reading}-\text{true value})/\text{true value}$; a negative $f$ means that the reading is too small. **Validity:** The circuit is an ideal source with one resistor. A small error requires $R_\mathrm i\ll R$, ideally $R_\mathrm i=0$.

:::herleitung Error of the ammeter
The mesh rule reads $U=I_R'R+I_R'R_\mathrm i$, so $I_R'=U/(R+R_\mathrm i)$. Hence $f=I_R'/I_R-1=R/(R+R_\mathrm i)-1=-R_\mathrm i/(R+R_\mathrm i)$.
:::

**Example.** $I_R=5$ mA, $I_R'=9\,\mathrm{V}/1810\,\Omega=4.972$ mA, so $f=-0.55\,\%$. With 1 $\Omega$ as in the digital multimeter, it would be 4.997 mA and $f=-0.056\,\%$: a negligible error. With a small resistor things look different: 0.9 V across 90 $\Omega$ gives 10 mA, with the instrument only 9 mA, so $f=-10\,\%$. It is not the meter alone that decides, but the ratio $R_\mathrm i/R$.

⁠**Limiting cases:** $R_\mathrm i\to0$ gives $f\to0$. $R\to0$ gives $I_R'\to U/R_\mathrm i$ and $f\to-100\,\%$: only the instrument limits the current now. That is Exercise [1](das-messgerat-ist-ein-bauteil.html#aufg-1)(a).

:::frage Is the current behind the ammeter smaller than in front of it?
No. No charge is lost in the instrument, only energy. The current is the same throughout the circuit and falls everywhere at once, because the total resistance has risen.
:::

:::aufgabe Exercise 3 ★★ Which range?
<span class="anker" id="aufg-3"></span>

(a) From what $R$ onward does the error of the 10 $\Omega$ ammeter stay below 1 %? (b) 90 k$\Omega$ are connected to 9 V. Compare the 10 mA range with the 250 µ A range: the error due to $R_\mathrm i$ and the reading error (1 % of the full-scale value). Which range measures better?

:::loesung
(a) $R_\mathrm i/(R+R_\mathrm i)\le0.01$ gives $R\ge99\,R_\mathrm i=990\,\Omega$.

(b) The true current is $9\,\mathrm{V}/90\,\mathrm{k\Omega}=100$ µ A. In the 10 mA range, $R_\mathrm i=10\,\Omega$, $f=-0.011\,\%$, but the reading error is $\pm100$ µ A, as much as the current itself. In the 250 µ A range, $R_\mathrm i=100\,\mathrm{mV}/250\,\mu\text{A}=400\,\Omega$, $f=-0.44\,\%$, and the reading error is $\pm2.5$ µ A, that is, 2.5 %. The small range interferes more but measures much better. The $-0.44\,\%$ can also be calculated out.
:::
:::
