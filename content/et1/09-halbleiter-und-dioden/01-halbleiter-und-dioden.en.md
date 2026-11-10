---
title: Overview: Semiconductors and Diodes
kurz: Overview
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Semiconductors and Diodes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Chapter 9: Semiconductors and Diodes
order: 1190100
summary: How silicon becomes a valve for current and how to calculate with it
tags: diode, semiconductor, Doping, charge carriers, pn junction, space-charge region, characteristic curve, operating point
lang: en
---

## What this is about

A charger turns the AC voltage of the wall outlet into the DC voltage for the rechargeable battery. The component that does this is called a __diode__: it lets current through in one direction (forward direction) and blocks it in the other (reverse direction). It consists of a __semiconductor__, a material whose conductivity lies between that of a metal and that of an insulator and can be set deliberately. The question of this chapter is: *How does a piece of silicon become a valve for current, and how do you calculate with a component that does not obey Ohm's law?*

The answer runs through six terms. __Doping__ means building in a few foreign atoms, which fixes how many __charge carriers__ (mobile charges) the crystal has. At the boundary between two differently doped regions, the __pn junction__, the __space-charge region__ forms by itself, a thin layer without mobile charges that acts as an energy barrier. The __characteristic curve__ is the graph of current versus voltage, the __operating point__ the pair of voltage and current that settles in a circuit.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Diode:** silicon, reverse saturation current $I_\mathrm S=10^{-14}$ A (the small current in the reverse direction), thermal voltage $U_T=25.85$ mV (thermal energy per charge) at $T=300$ K (27 °C). The switch model uses the forward voltage $U_\mathrm F=0.7$ V (voltage across the conducting diode).

</li>

<li>

⁠**pn junction:** $10^{16}$ foreign atoms per cm$^3$ on each side, $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ free electrons in pure silicon, relative permittivity $\varepsilon_\mathrm r=11.7$.

</li>

<li>

⁠**Circuit:** source $U_0=5$ V, resistor $R=1\,\mathrm{k\Omega}$, diode in series.

</li>

<li>

⁠**Rectifier:** sinusoidal voltage with a peak value of 12 V and 50 Hz, load 1 k$\Omega$.

</li>

<li>

⁠**Constants:** $e=1.602\cdot10^{-19}$ C, $k_\mathrm B=1.3806\cdot10^{-23}$ J/K. The script `rechnung_kap9.py` recalculates all the numbers.

</li>

</ul>
:::
