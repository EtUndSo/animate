---
title: Stage 5: Characteristic curve, breakdown and special diodes
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Semiconductors and Diodes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Chapter 9: Semiconductors and Diodes
order: 1190700
summary: The equation is in place.
tags: anode, cathode, avalanche effect, Zener effect, breakdown, junction capacitance, photons, internal photoelectric effect
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
The equation is in place. This stage reads it as a curve, adds breakdown, and shows what else can be built from the properties of the junction.
:::

**The idea.** The p-side is called the __anode__, the n-side the __cathode__; both carry metal contacts. The triangle of the circuit symbol points in the forward direction. In a linear plot there seems to be a knee at 0.6 V (Fig. [6](#abb-6)). It is due to the scale, because an exponential function has no threshold. On an axis up to 10 mA the curve reaches 1 % of the final value at 0.595 V, on an axis up to 10 µ A already at 0.417 V. On a logarithmic plot it is a straight line.

:::abbildung et1/k9kennlinie 6
Structure, circuit symbol with reference arrows, and characteristic curve of the reference model. Middle: linear; the reverse current $10^{-14}$ A is invisible. Right: logarithmic, a straight line that bends away only near $U=0$ because of the term $-1$.
:::

**Breakdown.** At a large reverse voltage, the field in the region becomes so strong that carriers release new pairs through collisions (__avalanche effect__) or electrons pass directly from the VB into the CB (__Zener effect__). The reverse current rises steeply; this is __breakdown__. It does no harm in itself. A diode is destroyed only by the heat $P=U\,I$ if nothing limits the current.

**Zener diode.** It is built for operation in breakdown and has a precisely defined voltage $U_\mathrm Z$ (Fig. [7](#abb-7) left). In the forward direction it behaves like a pn diode. Beyond $U_\mathrm Z$ the characteristic curve is almost vertical, and its small resistance is $r_\mathrm Z=\Delta U/\Delta I$. A series resistor absorbs fluctuations of the source: the voltage across the component barely changes, the current changes. With $r_\mathrm Z=10\,\Omega$, a current change of 18 mA causes only 0.18 V.

**Varactor diode.** The carrier-free region is an insulating layer between two conducting regions, so it is a capacitor ([Chapter 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) with the area $A$ and the spacing $w$. The __junction capacitance__ falls with the reverse voltage $U_\mathrm R=-U$ because the region grows:

<span class="anker" id="gl-5-1"></span>
$$C_\mathrm{j}=\frac{\varepsilon A}{w}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}. \tag{5.1}$$

With $A=1\,\mathrm{mm^2}$, $C_0=241$ pF; at 25 V it is 40 pF and $w=2.6$ µ m. **Validity:** abrupt junction, operation in the reverse direction. Diodes with a particularly strong effect are called varactor diodes. They are used to tune the frequency of resonant circuits by voltage, for example in radio receivers. A resonant circuit of coil and capacitor oscillates at a frequency that depends on $C$.

:::abbildung et1/k9spezial 7
Left: Zener diode with $U_\mathrm Z=5.1$ V and $r_\mathrm Z=10\,\Omega$. Middle: capacitance according to [(5.1)](#gl-5-1). Right: solar cell with $I_\mathrm S=1$ nA for three illumination levels. The current follows the light, the open-circuit voltage hardly does. Bottom: circuit symbols and equivalent circuit of the photodiode.
:::

**Photodiode.** Light consists of energy packets, the __photons__, with $W=h\,c/\lambda$ ($h$: Planck constant, $c$: speed of light, $\lambda$: wavelength). If $W\ge W_\mathrm g$, a photon lifts an electron into the CB (__internal photoelectric effect__). For silicon this requires $\lambda\le1107$ nm. The field of the region separates the pair: the electron runs to the n-side, the hole to the p-side. This is a current from cathode to anode through the diode, that is, in the reverse direction, and it is proportional to the light power.

:::satz Theorem 5.1 (Illuminated diode)
<span class="anker" id="satz-5-1"></span>

The characteristic curve shifts downward by the __photocurrent__ $I_\mathrm{Ph}$. The equivalent circuit is a current source in parallel with the diode:

<span class="anker" id="gl-5-2"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph},\qquad\text{open circuit }(I=0):\ U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm{Ph}}{I_\mathrm S}+1\Bigr). \tag{5.2}$$
:::

⁠**How to read it:** As a light sensor, the photodiode is operated in the reverse direction; then $I\approx-I_\mathrm{Ph}$. A __solar cell__ is a large-area photodiode that operates at $U>0$ and $I<0$: the product $U\,I$ is negative, so it delivers power. Ten times the light raises $I_\mathrm{Ph}$ tenfold, but $U_\mathrm L$ by only 60 mV. The reason is the logarithm in [(5.2)](#gl-5-2). The voltage depends mainly on the material, around 0.5 V in operation for silicon. In the model with $I_\mathrm S=1$ nA, $U_\mathrm L=0.505$ V, 0.536 V and 0.564 V at 0.3 A, 1 A and 3 A. **Limiting case:** $I_\mathrm{Ph}=0$ gives [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1) and $U_\mathrm L=0$.

:::frage But the diode only conducts from 0.6 V on. Isn't that a threshold?
In a circuit with currents around 1 mA it looks that way: at 0.4 V only 52 nA flow, barely measurable. But the current grows steadily from 0 V on, by a factor of 10 per 60 mV. There is no voltage at which something switches. Only the magnitude becomes important for the circuit at some point.
:::

:::aufgabe Exercise 5 ★★ Holding a voltage
<span class="anker" id="aufg-5"></span>

A Zener diode with $U_\mathrm Z=5.1$ V and $r_\mathrm Z=10\,\Omega$ is connected through $R=220\,\Omega$ to a source that fluctuates between 10 V and 14 V.

<ol class="al">

<li>

How large is the current at both ends if the diode holds exactly 5.1 V?

</li>

<li>

By how much does the diode voltage really change? By what factor has the fluctuation become smaller?

</li>

<li>

What power does the diode convert at 14 V?

</li>

</ol>

:::loesung
(a) $I=(10\,\mathrm{V}-5.1\,\mathrm{V})/220\,\Omega=22.3$ mA and $(14\,\mathrm{V}-5.1\,\mathrm{V})/220\,\Omega=40.5$ mA. (b) $\Delta U=r_\mathrm Z\Delta I=10\,\Omega\cdot18.2\,\mathrm{mA}=0.18$ V. More precisely, $R$ divides with $r_\mathrm Z$: $4\,\mathrm{V}\cdot10/230=0.17$ V. The fluctuation is 23 times smaller. (c) $P=5.1\,\mathrm{V}\cdot40.5\,\mathrm{mA}=0.21$ W.
:::
:::

:::aufgabe Exercise 6 ★★ Solar cell
<span class="anker" id="aufg-6"></span>

A cell has $I_\mathrm S=1$ nA and, in full sun, $I_\mathrm{Ph}=3$ A.

<ol class="al">

<li>

Calculate $U_\mathrm L$. How does $U_\mathrm L$ change when the light falls to one third?

</li>

<li>

Calculate $I$ and the delivered power at $U=0.5$ V.

</li>

<li>

How many cells in series are needed to charge a 14 V battery at 0.5 V each?

</li>

</ol>

:::loesung
(a) $U_\mathrm L=25.85\,\mathrm{mV}\cdot\ln(3\cdot10^{9}+1)=0.564$ V. At 1 A, $U_\mathrm L=0.536$ V, only 28 mV less. (b) $I=10^{-9}\,\mathrm{A}\cdot(\mathrm{e}^{19.34}-1)-3\,\mathrm{A}=0.25\,\mathrm{A}-3\,\mathrm{A}=-2.75$ A. The delivered power is $0.5\,\mathrm{V}\cdot2.75\,\mathrm{A}=1.37$ W. (c) $14\,\mathrm{V}/0.5\,\mathrm{V}=28$ cells.
:::
:::
