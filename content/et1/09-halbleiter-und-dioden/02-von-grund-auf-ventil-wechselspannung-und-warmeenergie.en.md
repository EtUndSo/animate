---
title: From the ground up: Valve, AC voltage and thermal energy
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Semiconductors and Diodes
order: 1190200
summary: How silicon becomes a valve for current and how to calculate with it
tags: AC voltage, peak value, frequency, half-wave rectifier, electronvolt, Thermal energy, Boltzmann constant, Boltzmann distribution
lang: en
---

An __AC voltage__ changes its sign periodically. Here it is sinusoidal, $u_\mathrm e(t)=\hat u\sin(2\pi ft)$, with the __peak value__ $\hat u$ (largest magnitude) and the __frequency__ $f$ (oscillations per second, unit Hz). One oscillation lasts $T=1/f$, so 20 ms at 50 Hz. Lowercase letters stand for time-dependent quantities.

:::abbildung et1/k9einweg 1
Left: diode with the terminals anode (A) and cathode (K) in series with a resistor on an AC voltage. Top right: only the positive half-wave appears across the resistor, reduced by 0.7 V. Bottom right: the diode holds 0.7 V while conducting and takes over the whole negative voltage while blocking. $\hat u=12$ V, 50 Hz.
:::

Fig. [1](#abb-1) shows the effect of a diode. The mesh gives $u_\mathrm e=u_\mathrm D+u_\mathrm a$. If $u_\mathrm e$ is positive, the diode conducts, around 0.7 V remains across it, and the rest is across the resistor. If $u_\mathrm e$ is negative, no current flows. Then $u_\mathrm a=0$, and the diode bears the whole voltage. The AC voltage becomes a voltage with only one sign. This circuit is called a __half-wave rectifier__. Its peak is $12\,\mathrm{V}-0.7\,\mathrm{V}=11.3$ V.

For the why, the chapter needs two energy quantities. The __electronvolt__ (eV) is the energy an electron gains by passing through 1 V ([Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1.602\cdot10^{-19}$ J. __Thermal energy__ arises because atoms and electrons move randomly at every temperature. Its measure is $k_\mathrm BT$ with the absolute temperature $T$ in K and the __Boltzmann constant__ $k_\mathrm B$. At 300 K, $k_\mathrm BT=4.14\cdot10^{-21}\,\mathrm{J}=25.85$ meV. Collisions distribute this energy unevenly: few particles have a lot, many have little. In equilibrium the __Boltzmann distribution__ holds:

<span class="anker" id="gl-0-1"></span>
$$\text{fraction of particles with at least the energy }W=\mathrm{e}^{-W/(k_\mathrm BT)}. \tag{0.1}$$

For every additional $k_\mathrm BT$ of energy the fraction drops by a factor of 2.718; at $10\,k_\mathrm BT$ it is $4.5\cdot10^{-5}$. The same law describes how air gets thinner with altitude.
