---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Semiconductors and Diodes
order: 1191200
summary: How silicon becomes a valve for current and how to calculate with it
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

At the pn junction, mobile charges move into the other region and leave fixed ions behind. The field of these ions builds up a barrier in the space-charge region that stops the equalization.

</li>

<li>

Heat lifts only the fraction $\mathrm{e}^{-W/(k_\mathrm BT)}$ of the charge carriers over a barrier of height $W$. Voltage in the forward direction lowers the barrier, so the current grows exponentially, by a factor of 10 per 60 mV: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$. In the reverse direction only the tiny current $-I_\mathrm S$ remains.

</li>

<li>

In a circuit, the operating point lies at the intersection of the characteristic curve and the load line (the straight line set by source and resistor). For hand calculations the diode becomes a switch with a fixed forward voltage, and for small changes around the operating point it becomes a resistor $r=U_T/I$.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Bands: $W_\mathrm g$ (silicon 1.12 eV), fraction $\mathrm{e}^{-W/(k_\mathrm BT)}$; the carriers are electrons in the CB and holes in the VB.

</li>

<li>

Doping: donors give $n\approx N_\mathrm D$, acceptors $p\approx N_\mathrm A$, everywhere $n\,p=n_\mathrm i^2$. The crystal stays neutral.

</li>

<li>

pn junction: diffusion, recombination, fixed ions, field. $U_\mathrm{D0}=U_T\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$.

</li>

<li>

Characteristic curve: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$, $U_T=k_\mathrm BT/e=25.85$ mV at 300 K, 60 mV per decade, no threshold.

</li>

<li>

Breakdown is reversible as long as the heat stays limited. Zener diode: $U_\mathrm Z$, $r_\mathrm Z$. Varactor diode: $C_\mathrm{j}=\varepsilon A/w$. Photodiode: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)-I_\mathrm{Ph}$, solar cell $U_\mathrm L=U_T\ln(I_\mathrm{Ph}/I_\mathrm S+1)$.

</li>

<li>

Operating point: intersection of the characteristic curve and the load line $I=(U_0-U_\mathrm D)/R$; iterate via $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$.

</li>

<li>

Models: conducting $U_\mathrm D=0$ or $U_\mathrm F$, blocking $I_\mathrm D=0$. Assume, calculate, check: $I_\mathrm D>0$ and $U_\mathrm D<U_\mathrm F$.

</li>

<li>

Small signal: $r=U_T/I$ for $|u_\mathrm D|\ll U_T$. Do not confuse with $U_\mathrm D/I$.

</li>

<li>

Bridge: peak $\hat u-2U_\mathrm F$, gap at $|u_\mathrm e|<2U_\mathrm F$. Charge pump: $U_\mathrm a\to2U_\mathrm e-2U_\mathrm F$.

</li>

</ul>
:::

**One principle behind all the results.** Heat distributes energy at random, and the fraction of particles above an energy falls exponentially with this energy. Almost everything in this chapter follows from that, once you ask which energy counts in each case.

| Result | Where it comes from |
|---|---|
| Pure silicon hardly conducts | The band gap (energy up to a free electron) is 43 times larger than the thermal energy (Stage [1](warum-silizium-kaum-leitet.html#stufe-1)) |
| Doping yields a charge carrier from almost every foreign atom | The electron is bound with only 1.7 times the thermal energy (Stage [2](dotierung.html#stufe-2)) |
| Built-in voltage $U_\mathrm{D0}$ | The barrier grows until the fraction above it equals the density ratio (Stage [3](die-raumladungszone.html#stufe-3)) |
| $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$ | The voltage shifts the barrier and thus the fraction (Stage [4](warum-der-strom-exponentiell-wachst.html#stufe-4)) |
| $U_\mathrm D$ stays almost constant, switch model | The current changes by a factor of 10 per 60 mV (Stages [6](der-arbeitspunkt.html#stufe-6) and [7](lineare-ersatzschaltungen.html#stufe-7)) |
| $r=U_T/I$ | The derivative of the exponential function is the function itself (Stage [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)) |
