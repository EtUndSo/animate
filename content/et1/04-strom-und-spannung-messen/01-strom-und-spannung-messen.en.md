---
title: Overview: Measuring Current and Voltage
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Measuring Current and Voltage
order: 1140100
summary: Why every meter changes the circuit and how to measure accurately anyway
tags: internal resistance, meter movement, measuring range
lang: en
---

## What this is about

A voltage divider is supposed to have 3 V across it, and the meter shows 2.73 V. The divider is fine and the reading is correct: it shows the voltage that has been present since the meter was connected. That is because a meter is a component with an __internal resistance__, the resistance between its terminals. The question is: *Why does every meter change the circuit it measures, how large is the error, and why does a bridge measure more accurately than an instrument alone?*



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Instrument:** a __meter movement__ (the part of the device that converts current into a pointer deflection) with full-scale deflection at $I_\mathrm M=50$ µ A and its own resistance $R_\mathrm M=2$ k$\Omega$. As an ammeter in the __measuring range__ (the range of values it can display) up to 10 mA it has $R_\mathrm{iA}=10\,\Omega$; as a voltmeter in the range up to 10 V it has $R_\mathrm{iV}=200$ k$\Omega$ (Stage [2](den-messbereich-erweitern.html#stufe-2)). Its reading deviates by at most 1 % of the full-scale value.

</li>

<li>

⁠**Object under test:** $R=1.8$ k$\Omega$ on an ideal voltage source $U=9$ V (it holds 9 V at any current). Without a meter, 5 mA flow.

</li>

<li>

⁠**Divider:** $R_1=60$ k$\Omega$ and $R_2=30$ k$\Omega$ in series across 9 V; there are 3 V across $R_2$.

</li>

<li>

⁠**Bridge:** $R_1=1$ k$\Omega$, $R_2=1.8$ k$\Omega$, $R_3=1$ k$\Omega$ at 9 V; $R_4$ is wanted. For small changes, four resistors of 350 $\Omega$ each at 9 V.

</li>

</ul>

The script `rechnung_kap4.py` recalculates all the numbers.
:::
