---
title: Stage 4: Line losses
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Power, Matching and Efficiency
order: 1170500
summary: The line lies between source and load, and it too is a resistor.
tags: voltage drop, power loss, useful power, nominal voltage
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The line lies between source and load, and it too is a resistor. This stage shows why large powers travel over high voltages.
:::

**The idea.** The line is in series with the load; the entire current must pass through it (Fig. [5](#abb-5)). Each coulomb loses $R_\mathrm{cable}I$ joules in it before reaching the load. A fixed power can be transmitted in two ways: with high voltage and low current, or the other way around. At high voltage, each coulomb brings a lot of energy, so few are enough. The low current helps twice: each coulomb loses less, and there are fewer of them.

:::abbildung et1/k7leitung 5
Source, line and load. $R_\mathrm{cable}$ combines the outgoing and return conductors. Right, the two cases of the example.
:::

:::satz Theorem 4.1 (Line losses)
<span class="anker" id="satz-4-1"></span>

If the current $I$ flows to the load over a line with $R_\mathrm{cable}$, then

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{cable}=R_\mathrm{cable}\,I,\qquad P_\mathrm{cable}=U_\mathrm{cable}\,I=R_\mathrm{cable}\,I^2,\qquad P_\mathrm{useful}=(U_\mathrm{q}-U_\mathrm{cable})\,I \tag{4.1}$$

and therefore

<span class="anker" id="gl-4-2"></span>
$$\frac{P_\mathrm{useful}}{P_\mathrm{q}}=\frac{(U_\mathrm{q}-U_\mathrm{cable})\,I}{U_\mathrm{q}\,I}=1-\frac{U_\mathrm{cable}}{U_\mathrm{q}}. \tag{4.2}$$

For two voltages with the same load power $P_\mathrm{L}=U_\mathrm{L1}I_1=U_\mathrm{L2}I_2$,

<span class="anker" id="gl-4-3"></span>
$$\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}},\qquad\frac{P_\mathrm{cable,1}}{P_\mathrm{cable,2}}=\left(\frac{U_\mathrm{L2}}{U_\mathrm{L1}}\right)^{\!2}. \tag{4.3}$$
:::

⁠**How to read it:** $U_\mathrm{cable}$ is the __voltage drop__ along the line. $P_\mathrm{cable}$ is the __power loss__, $P_\mathrm{useful}=P_\mathrm{L}$ the __useful power__ of the load, $P_\mathrm{q}=U_\mathrm{q}I$ the power of the source. $U_\mathrm{L}$ is the voltage across the load. **Validity:** The formulas hold for DC quantities and for the resistance of the line. For an AC voltage and an ohmic load, they hold with RMS values.

**Example.** The load needs 40 kW, $R_\mathrm{cable}=1\,\Omega$. At $U_\mathrm{L}=400$ V, $I=100$ A, $U_\mathrm{cable}=100$ V and $P_\mathrm{cable}=10$ kW. The source must supply 500 V, and by [(4.2)](#gl-4-2), $1-100/500=80$ % arrive. At 20 kV, $I=2$ A, $U_\mathrm{cable}=2$ V and $P_\mathrm{cable}=4$ W, and 99.99 % arrive. The current falls by a factor of 50, the loss by $50^2=2500$. **Limiting case:** For $R_\mathrm{cable}\to0$, $U_\mathrm{cable}=0$ and [(4.2)](#gl-4-2) gives 1. Over longer distances, energy can be transmitted only at high voltage, which is why the grid is built in levels. The __nominal voltage__ is the voltage for which a grid is designed:

| Level | Nominal voltage | Range | Task |
|---|---|---|---|
| Low voltage | 230/400 V | a few 100 m | Households and businesses in town |
| Medium voltage | 10 kV | up to around 10 km | Distribution in large cities |
| Medium voltage | 20 kV | up to around 25 km | Distribution in rural areas and medium-sized towns |
| High voltage | 110 kV | up to around 100 km | Supply of the medium-voltage grids |
| Extra-high voltage | 220 kV, 380 kV | a few 100 to over 1000 km | Interconnection within the country and across Europe |

High voltage cannot be brought all the way into the home: air breaks down at around 3 kV/mm ([Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), so overhead lines need clearances of several meters. Transformers step the AC voltage up for transport and back down again ahead of the consumers.

:::frage According to $P=U^2/R$, power grows with voltage. Shouldn't higher voltages bring more loss?
The formula is correct, but it needs the voltage across the same resistor. In the example, the cable does not have 20 kV across it but $U_\mathrm{cable}=2$ V, and $(2\,\mathrm{V})^2/1\,\Omega$ gives the 4 W. The high voltage is across the load. $U_\mathrm{cable}$ falls because the current falls.
:::

:::aufgabe Exercise 4 ★★ The cabin at the edge of the forest
<span class="anker" id="aufg-4"></span>

A cabin absorbs 480 W at 48 V DC, and the supply line has $R_\mathrm{cable}=0.2\,\Omega$. (a) Calculate $I$, $U_\mathrm{cable}$, $P_\mathrm{cable}$, $U_\mathrm{q}$ and the fraction that arrives. (b) The same for 480 W at 12 V. (c) Which voltage $U_\mathrm{L}$ limits the loss to 1 % of the load power?

:::loesung
(a) $I=480\,\mathrm{W}/48\,\mathrm{V}=10$ A, $U_\mathrm{cable}=2$ V, $P_\mathrm{cable}=20$ W, $U_\mathrm{q}=50$ V. A fraction of $1-2/50=96$ % arrives. (b) $I=40$ A, $U_\mathrm{cable}=8$ V, $P_\mathrm{cable}=320$ W, $U_\mathrm{q}=20$ V. Only 60 % arrives. Four times the current gives sixteen times the loss. (c) $R_\mathrm{cable}\,P_\mathrm{L}^2/U_\mathrm{L}^2\le0.01\,P_\mathrm{L}$ gives $U_\mathrm{L}\ge\sqrt{R_\mathrm{cable}\,P_\mathrm{L}/0.01}=98$ V.
:::
:::
