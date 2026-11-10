---
title: Stage 2: Extending the measuring range
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Measuring Current and Voltage
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Chapter 4: Measuring Current and Voltage
order: 1140300
summary: The meter movement ends at 50 µ A and 100 mV.
tags: shunt, series resistor
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
The meter movement ends at 50 µ A and 100 mV. This stage turns it into an ammeter up to 10 mA and a voltmeter up to 10 V and shows where $R_\mathrm{iA}$ and $R_\mathrm{iV}$ come from.
:::

**The idea.** The meter movement tolerates only 50 µ A. If it is to show 10 mA, the rest must flow past it: a __shunt__ (parallel resistor) lies in parallel and takes over 9.95 mA. If it is to show 10 V, only 100 mV may be across it: a __series resistor__ takes over 9.9 V (Fig. [2](#abb-2)). At full-scale deflection, the movement sees the same as before; only the labeling of the scale changes.

:::abbildung et1/k4bereich 2
The same meter movement twice. On the left, the shunt divides the current in the ratio 199 to 1; on the right, the series resistor divides the voltage in the ratio 99 to 1.
:::

:::satz Theorem 2.1 (Shunt and series resistor)
<span class="anker" id="satz-2-1"></span>

Let an instrument have the internal resistance $R_\mathrm{old}$ and the full-scale value $I_\mathrm{old}$ or $U_\mathrm{old}$, respectively. For the new full-scale value $I_\mathrm{new}$ or $U_\mathrm{new}=\alpha\,U_\mathrm{old}$, it needs

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{Shunt}=R_\mathrm{old}\,\frac{I_\mathrm{old}}{I_\mathrm{new}-I_\mathrm{old}},\qquad R_\mathrm V=R_\mathrm{old}\,(\alpha-1). \tag{2.1}$$

The new internal resistance is $R_\mathrm{old}\parallel R_\mathrm{Shunt}$ or $R_\mathrm{old}+R_\mathrm V$, respectively.
:::

⁠**How to read it:** $\alpha>1$ is the factor of the extension, without a unit. $\parallel$ means parallel: $R_a\parallel R_b=R_aR_b/(R_a+R_b)$. The shunt is small compared with $R_\mathrm{old}$, the series resistor large. **Validity:** The deflection must be proportional to the current, and the resistors must be accurate, because their error enters the reading.

:::herleitung Current divider and voltage divider
Shunt and instrument are in parallel; $G=1/R$ is the conductance. At full-scale deflection, the current divider gives

$$\frac{I_\mathrm{old}}{I_\mathrm{new}}=\frac{R_\mathrm{Shunt}}{R_\mathrm{Shunt}+R_\mathrm{old}}=\frac{G_\mathrm{old}}{G_\mathrm{Shunt}+G_\mathrm{old}} \quad\Rightarrow\quad R_\mathrm{Shunt}=\frac{I_\mathrm{old}}{I_\mathrm{new}}\,(R_\mathrm{Shunt}+R_\mathrm{old}).$$

Solving for $R_\mathrm{Shunt}$ gives [(2.1)](#gl-2-1). The series resistor and the instrument are in series. The voltage divider gives

$$U_\mathrm{old}=U_\mathrm{new}\,\frac{R_\mathrm{old}}{R_\mathrm{old}+R_\mathrm V} \quad\Rightarrow\quad \alpha=\frac{R_\mathrm{old}+R_\mathrm V}{R_\mathrm{old}}\quad\Rightarrow\quad R_\mathrm V=R_\mathrm{old}\,(\alpha-1).$$
:::

::::beispiel
For 10 mA: $R_\mathrm{Shunt}=2\,\mathrm{k\Omega}\cdot\frac{50\,\mu\text{A}}{9.95\,\mathrm{mA}}=10.05\,\Omega$, in parallel with 2 k$\Omega$ this gives $R_\mathrm{iA}=10\,\Omega$. For 10 V: $\alpha=100$, $R_\mathrm V=2\,\mathrm{k\Omega}\cdot99=198$ k$\Omega$, so $R_\mathrm{iV}=200$ k$\Omega$.
::::

⁠**In short:** at full-scale deflection, 100 mV drop across the ammeter in every range, and 50 µ A flow through the voltmeter in every range. The internal resistances follow directly: $R_\mathrm{iA}=100\,\mathrm{mV}/10\,\mathrm{mA}=10\,\Omega$ and $R_\mathrm{iV}=10\,\mathrm{V}/50\,\mu\text{A}=200$ k$\Omega$. So a sensitive current range has a large internal resistance, and so does a high voltage range. The reciprocal of 50 µ A, 20 k$\Omega$/V, is printed on pointer instruments as a characteristic value.

⁠**Limiting case:** For $I_\mathrm{new}\to I_\mathrm{old}$, $R_\mathrm{Shunt}\to\infty$; for $\alpha=1$, $R_\mathrm V=0$. Without an extension, no component is needed.

**Several ranges.** A multirange meter (a device with several ranges) switches between them (Fig. [3](#abb-3)). In the ammeter, each further switch places a shunt in parallel; in the voltmeter, each further open switch brings in a series resistor. Equation [(2.1)](#gl-2-1) holds step by step: the arrangement so far is the instrument, and its internal resistance is called $R_\mathrm{old}$.

:::abbildung et1/k4stufen 3
Stepwise extension. On the left, each closed switch adds a shunt; on the right, each opened switch adds a series resistor.
:::

:::frage Does the shunt make the instrument more sensitive?
No, less sensitive. The meter movement still needs 50 µ A for full-scale deflection, and the shunt ensures that it takes 10 mA to get there.
:::

:::aufgabe Exercise 2 ★★ Range switch
<span class="anker" id="aufg-2"></span>

The meter movement gets the circuits from Fig. [3](#abb-3). (a) Calculate $R_1$, $R_2$, $R_3$ for the current ranges 250 µ A, 1 mA, 10 mA and the internal resistance in each case. (b) Calculate $R_1$, $R_2$, $R_3$ for the voltage ranges 1 V, 10 V, 100 V. (c) Check both parts with the statement from “In short”.

:::loesung
(a) With [(2.1)](#gl-2-1) step by step:

$$\begin{aligned} R_1&=2\,\mathrm{k\Omega}\cdot\tfrac{50}{250-50}=500\,\Omega, & R^*&=2\,\mathrm{k\Omega}\parallel500\,\Omega=400\,\Omega,\\ R_2&=400\,\Omega\cdot\tfrac{250}{1000-250}=133.3\,\Omega, & R^{**}&=400\,\Omega\parallel133.3\,\Omega=100\,\Omega,\\ R_3&=100\,\Omega\cdot\tfrac{1}{10-1}=11.11\,\Omega, & R^{***}&=100\,\Omega\parallel11.11\,\Omega=10\,\Omega. \end{aligned}$$

In parallel, the three shunts give 10.05 $\Omega$, like the single shunt in the example.

(b) Each step has $\alpha=10$: $R_1=2\,\mathrm{k\Omega}\cdot9=18$ k$\Omega$ with $R^*=20$ k$\Omega$, $R_2=20\,\mathrm{k\Omega}\cdot9=180$ k$\Omega$ with $R^{**}=200$ k$\Omega$, $R_3=200\,\mathrm{k\Omega}\cdot9=1.8$ M$\Omega$ with $R^{***}=2$ M$\Omega$.

(c) $250\,\mu\text{A}\cdot400\,\Omega=1\,\mathrm{mA}\cdot100\,\Omega=10\,\mathrm{mA}\cdot10\,\Omega=100$ mV. For the voltmeter, $1\,\mathrm{V}/20\,\mathrm{k\Omega}=10\,\mathrm{V}/200\,\mathrm{k\Omega}=100\,\mathrm{V}/2\,\mathrm{M\Omega}=50$ µ A.
:::
:::
