---
title: Stage 7: The unbalanced bridge
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Measuring Current and Voltage
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Chapter 4: Measuring Current and Voltage
order: 1140800
summary: If a resistance changes only slightly or continuously, you do not readjust.
tags: strain gauge
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
If a resistance changes only slightly or continuously, you do not readjust. The deviation from zero is then the measuring signal. This stage shows why the smallest changes become visible this way.
:::

**The idea.** An instrument alone has to display the entire voltage, of which the change is a tiny part. The bridge subtracts the large common voltage. Only the change remains, and it fits in a small measuring range. Because the reading error is tied to the full-scale value, it falls with the range.

:::satz Theorem 7.1 (Bridge voltage)
<span class="anker" id="satz-7-1"></span>

Between the midpoints there is $U_\mathrm d=U_4-U_2$ with the voltages $U_2$ across $R_2$ and $U_4$ across $R_4$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm d=U_\mathrm q\left(\frac{R_4}{R_3+R_4}-\frac{R_2}{R_1+R_2}\right)=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}. \tag{7.1}$$

For $R_1=R_2=R_3=R$ and $R_4=R+\Delta R$,

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}\qquad\text{for }\Delta R\ll R. \tag{7.2}$$
:::

⁠**How to read it:** The numerator in [(7.1)](#gl-7-1) becomes zero at balance. $\Delta R/R$ is the relative change, without a unit. **Validity:** The voltmeter draws no appreciable current. **Limiting cases:** $\Delta R=0$ gives $U_\mathrm d=0$. $\Delta R\to\infty$ gives $U_\mathrm d\to U_\mathrm q/2$: the right midpoint is then at the plus terminal.

:::herleitung Small change
With $U_2=U_\mathrm q/2$ and $U_4=U_\mathrm q(R+\Delta R)/(2R+\Delta R)$,

$$U_\mathrm d=U_\mathrm q\,\frac{2(R+\Delta R)-(2R+\Delta R)}{2(2R+\Delta R)}=\frac{U_\mathrm q\,\Delta R}{4R+2\Delta R}=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}.$$
:::

:::abbildung et1/k4dms 9
Left, the bridge with the variable $R_4$. Right, the same change on two scales: red line the reading, light band the reading error. On the 10 V scale, a change of 9 mV is lost in the error. On the 100 mV scale, the deviation itself is the signal.
:::

::::beispiel strain gauge
A __strain gauge__ is a thin metal track that is glued onto a component. If the component stretches, the track becomes longer and thinner, and its resistance $R=\rho\,l/A$ rises. The relative change in resistance is about twice the strain. At 2 ‰ strain, $R_4$ grows by 0.4 % from 350 $\Omega$ to 351.4 $\Omega$. Then $U_2=4.500$ V and $U_4=9\,\mathrm{V}\cdot351.4/701.4=4.509$ V, so $U_\mathrm d=8.98$ mV. The approximation gives 9.00 mV, which deviates by 0.2 %. In the 10 M$\Omega$ voltmeter, 0.9 nA flow; compared with 12.9 mA in the branches, this is a share of $7\cdot10^{-8}$: negligible.
::::

**Why this is more accurate.** Measured directly, the instrument would have to distinguish 4.509 V from 4.500 V, that is, reliably display three decimal places in the 10 V range. But its reading error of $\pm100$ mV is eleven times the change being sought. On the bridge, the 100 mV range with $\pm1$ mV is enough, a hundredth of that (Fig. [9](#abb-9)). Two advantages are added. If the source fluctuates by 1 %, $U_4$ changes by 45 mV, five times the signal, whereas $U_\mathrm d$ changes by only 0.09 mV. And if all four resistors change by the same factor, for instance through heat, $U_\mathrm d$ stays the same.

:::frage Couldn't you measure $U_4$ and subtract 4.5 V in your head?
You can calculate that, but the $\pm100$ mV reading error remains in the result. The bridge subtracts before the instrument measures. That is why the instrument may have a small range.
:::

⁠**From here on:** Unless stated otherwise, meters count as ideal in all the following parts: ammeters with $R_\mathrm i\to0$, voltmeters with $R_\mathrm i\to\infty$.

:::aufgabe Exercise 8 ★★★ Two strain gauges
<span class="anker" id="aufg-8"></span>

The right branch now contains two strain gauges: $R_3=R-\Delta R$ is compressed, $R_4=R+\Delta R$ stretched, $R_1=R_2=R$. (a) Calculate $U_\mathrm d$ in general and for the example. (b) Why is the result exactly linear in $\Delta R$? (c) What changes if all four resistors change by 1 % through heat?

:::loesung
(a) $R_3+R_4=2R$, so $U_4=U_\mathrm q(R+\Delta R)/(2R)$. With $U_2=U_\mathrm q/2$ it follows that $U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R=4.5\,\mathrm{V}\cdot0.004=18.0$ mV, twice as much as with one gauge.

(b) The sum $R_3+R_4$ stays $2R$. The current in the right branch therefore stays 12.9 mA, and $U_4$ grows exactly with $R_4$. With one gauge, the sum grows as well, which produces the denominator in [(7.2)](#gl-7-2).

(c) Nothing: in [(7.1)](#gl-7-1), a common factor of all the resistors cancels.
:::
:::
