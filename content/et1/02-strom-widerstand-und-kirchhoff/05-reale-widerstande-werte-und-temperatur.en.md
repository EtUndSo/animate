---
title: Stage 4: Real resistors: values and temperature
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Current, Resistance and Kirchhoff's Laws
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Chapter 2: Current, Resistance and Kirchhoff's Laws
order: 1120500
summary: So far, R was a number from material and shape.
tags: Metal-film or carbon-film resistors, Wire-wound resistors, SMD, E series, temperature coefficient, PTC, cold conductor, NTC
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
So far, $R$ was a number from material and shape. A purchased component has a standardized value and a tolerance, and its resistance changes with temperature.
:::

**The idea.** Manufacturing scatters by a percentage. That is why the values on offer are graded so that successive values have the same *percentage* spacing. For temperature, $\sigma=n\,e\,\mu$ decides: heat changes either the mobility $\mu$ or the charge carrier density $n$.

**Types of construction.** __Metal-film or carbon-film resistors__ carry a thin layer on a ceramic body. This is the usual design for 0.1 to 2 W, and the value is printed on them as a color code. __Wire-wound resistors__ withstand high power and temperature and are suited to small values. __SMD__ resistors (Surface Mounted Device) are soldered directly onto the circuit board. They are very small, allow a high packing density, tolerate little power and, because they have no connecting wires, are suited to high frequencies.

:::definition Definition 4.1 (E series)
<span class="anker" id="satz-4-1"></span>

An __E series__ E$N$ contains $N$ values per decade; according to DIN IEC 60063 there are E3, E6, E12, E24, E48, E96 and E192:

<span class="anker" id="gl-4-1"></span>
$$w=\bigl(\sqrt[N]{10}\,\bigr)^{i}=\sqrt[N]{10^{i}},\qquad i=0,1,\dots,N-1. \tag{4.1}$$
:::

⁠**How to read it:** $w$ is the prefactor; the decade (power of ten) is chosen freely. The step is a fixed factor; for E12, $\sqrt[12]{10}=1.21$. The standard values are rounded: 1.0; 1.2; 1.5; 1.8; 2.2; 2.7; 3.3; 3.9; 4.7; 5.6; 6.8; 8.2. Some deviate slightly from [(4.1)](#gl-4-1) for historical reasons, such as 2.7 instead of 2.61. Why this factor? E12 belongs to the tolerance $\pm10\,\%$: the ranges of neighboring values then adjoin without gaps, and every manufactured piece belongs to a standard value. Likewise, E6 belongs to $\pm20\,\%$ and E24 to $\pm5\,\%$.

**Color code.** Leaded resistors usually carry four rings: two digits, the multiplier $10^x$, the tolerance. The digits are black 0, brown 1, red 2, orange 3, yellow 4, green 5, blue 6, violet 7, gray 8, white 9. As multipliers there are also gold $10^{-1}$ and silver $10^{-2}$. The tolerance is brown 1 %, red 2 %, green 0.5 %, blue 0.25 %, violet 0.1 %, gold 5 %, silver 10 %. Yellow, violet, red, gold means $47\cdot10^2\,\Omega=4.7\,\mathrm{k\Omega}$ with $\pm5\,\%$, that is 4.47 to 4.94 k$\Omega$. $R_1$ of the chain carries red, black, red, gold.

:::satz Theorem 4.2 (Temperature dependence)
<span class="anker" id="satz-4-2"></span>

Near a reference temperature $\vartheta_0$,

<span class="anker" id="gl-4-2"></span>
$$R(\vartheta)=R(\vartheta_0)\,\bigl(1+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)\bigr). \tag{4.2}$$
:::

⁠**How to read it:** $\vartheta$ is the temperature in °C, in data sheets usually $\vartheta_0=20$ °C. The __temperature coefficient__ $\alpha$ has the unit 1/K: copper $3.9\cdot10^{-3}$, tungsten $4.5\cdot10^{-3}$, carbon $-0.5\cdot10^{-3}$, constantan around $10^{-5}$. For $\alpha>0$, the material is called __PTC__ (positive temperature coefficient) or __cold conductor__: it conducts better when cold. For $\alpha<0$, it is called __NTC__ (negative temperature coefficient) or __hot conductor__. **Validity:** [(4.2)](#gl-4-2) is the tangent to the true curve. For metals it reaches far, for semiconductors only a few kelvins (Fig. [5](#abb-5) left).

:::abbildung et1/k2temperatur 5
Left: $R/R_{20}$ versus temperature for copper ($\alpha=3.9\cdot10^{-3}$ /K), the compensated alloy constantan and a semiconductor hot conductor (around $-4\,\%$/K at 20 °C). Right: model characteristic of a 9 V incandescent lamp. Cold, it has $1.5\,\Omega$; in operation at 0.5 A it has $18\,\Omega$. The curve changes between the two dashed straight lines.
:::

**Mechanism.** Metals (copper, silver, platinum, tungsten): $n$ is fixed, a warmer lattice vibrates more strongly, the flight time $T$ falls, $\mu$ falls, $R$ rises. Semiconductors (silicon, germanium): at room temperature only a few electrons are free. Heat frees more ([Chapter 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)), $n$ grows much faster than $\mu$ falls, $R$ falls. __Compensated alloys__ such as constantan: the collisions with the irregularly embedded impurity atoms predominate and hardly depend on temperature. Alternatively, a PTC and an NTC are placed in series so that the increase of one offsets the decrease of the other ($R_1\alpha_1+R_2\alpha_2=0$).

::::beispiel
The wire warms up from 20 °C to 70 °C. From [(4.2)](#gl-4-2) follows the factor $1+3.9\cdot10^{-3}\cdot50=1.195$, so 40.6 m$\Omega$ instead of 34 m$\Omega$. An extreme case is the tungsten filament of the lamp: the factor 12 from $1.5\,\Omega$ to $18\,\Omega$ corresponds by [(4.2)](#gl-4-2) to around 2460 °C, as a rough approximation over this large span.
::::

⁠**Limiting cases:** $\vartheta=\vartheta_0$ gives $R(\vartheta_0)$, $\alpha=0$ gives a constant value.

:::frage Why do incandescent lamps usually burn out at switch-on?
Cold, the filament has only $1.5\,\Omega$; at 9 V, 6 A flow in the first moment instead of 0.5 A. This surge heats the filament in fractions of a second. Its resistance rises, which lowers the current, until $18\,\Omega$ are reached. At thin spots the heating is greatest, and that is where the filament breaks.
:::

:::aufgabe Exercise 4 ★★ Standard values and temperature
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

A resistor carries blue, gray, red, gold. What are its value and range?

</li>

<li>

Calculate the step factor of E24. Which tolerance makes neighboring ranges just touch?

</li>

<li>

A copper coil has exactly $10\,\Omega$ at 20 °C and $12\,\Omega$ when warm. How warm is it?

</li>

<li>

A copper resistor of $100\,\Omega$ is to be made temperature-independent with carbon in series. What value does the carbon need?

</li>

</ol>

:::loesung
(a) Blue 6, gray 8, red $10^2$, gold $\pm5\,\%$: $6.8\,\mathrm{k\Omega}$, range 6.46 to 7.14 k$\Omega$.

(b) $\sqrt[24]{10}=1.10$. From $(1+t)/(1-t)=1.10$ follows $t=4.8\,\%$, rounded $\pm5\,\%$.

(c) $\vartheta=20\text{\,°C}+(12/10-1)/(3.9\cdot10^{-3}\,\mathrm{K^{-1}})=71$ °C.

(d) $R_\mathrm{Cu}\,\alpha_\mathrm{Cu}+R_\mathrm C\,\alpha_\mathrm C=0$: $R_\mathrm C=100\,\Omega\cdot3.9/0.5=780\,\Omega$.
:::
:::
