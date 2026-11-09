---
title: Overview: Power, Matching and Efficiency
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Power, Matching and Efficiency
order: 1170100
summary: Why half of the energy stays in the source at the power maximum
tags: internal resistance, load, power
lang: en
---

## What this is about

A 9 V battery has 2 $\Omega$ of __internal resistance__, the resistance that the current must overcome inside the source itself. It feeds a __load__, the connected device. How large must the load be so that as much __power__, that is, energy per time, as possible arrives at it? The answer is 2 $\Omega$, and it comes at a price: half of the energy then stays in the battery as heat. The question of this chapter is: *Where does the power come from, where does it go, and why does the maximum lie at exactly 50 % utilization?*



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Battery:** the 9 V battery from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) with the source voltage $U_\mathrm{q}=9$ V (the voltage supplied by the chemistry) and the internal resistance $R_\mathrm{i}=2\,\Omega$. [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) calls it $R_\mathrm{q}$ for a single source. The short-circuit current is $I_\mathrm{SC}=4.5$ A.

</li>

<li>

⁠**Load:** a resistor $R_\mathrm{L}$ of 16, 8, 2 or 0.5 $\Omega$.

</li>

<li>

⁠**Others:** $R=5\,\Omega$ on a sinusoidal voltage with a peak value of 10 V (Stage [3](mittlere-leistung-bei-sinusspannung.html#stufe-3)), a line with $R_\mathrm{cable}=1\,\Omega$ ahead of a 40 kW load (Stage [4](leitungsverluste.html#stufe-4)).

</li>

</ul>

The script `rechnung_kap7.py` recalculates all the numbers.
:::
