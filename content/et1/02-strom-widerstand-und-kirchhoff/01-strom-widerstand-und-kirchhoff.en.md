---
title: Overview: Current, Resistance and Kirchhoff's Laws
kurz: Overview
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Current, Resistance and Kirchhoff's Laws
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Chapter 2: Current, Resistance and Kirchhoff's Laws
order: 1120100
summary: Why electrons crawl while the current is there at once, and why networks obey conservation laws
tags: current, resistor, Ohm's law, node rule, mesh rule
lang: en
---

## What this is about

Close a circuit and the lamp lights up at that very moment. Yet the electrons in the wire crawl around 2000 times slower than a snail. A __current__ is moving charge, measured as charge per time. A __resistor__ is a component that slows this motion and converts its energy into heat. The question of this chapter is: *How does a voltage become a current, and how does that current divide in a network of many components?*

The answer consists of three laws. __Ohm's law__ links voltage and current at a component. The __node rule__ says that no current disappears at a junction. The __mesh rule__ says that the voltages along a closed path add up to zero.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Chain:** the 9 V battery from [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) across two resistors in series, $R_1=2\,\mathrm{k\Omega}$ and $R_2=1\,\mathrm{k\Omega}$. A current of 3 mA flows, 6 V are across $R_1$ and 3 V across $R_2$.

</li>

<li>

⁠**Wire:** copper, length $L=1$ m, cross section $A=0.5\,\mathrm{mm^2}$, resistivity (material constant, Stage [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3)) $\rho=1.7\cdot10^{-8}\,\mathrm{\Omega\,m}$, density of free electrons $n=8.5\cdot10^{28}\,\mathrm{m^{-3}}$ (one per atom). It carries the 3 mA of the chain.

</li>

<li>

⁠**Network:** a 9 V source and five resistors between four junctions, $R_\mathrm a=2$, $R_\mathrm b=5$, $R_\mathrm c=3$, $R_\mathrm d=1$, $R_\mathrm e=2$ (all in $\mathrm{k\Omega}$), Fig. [7](knoten-zweige-maschen.html#abb-7).

</li>

<li>

⁠**Constants:** $e=1.602\cdot10^{-19}$ C, $m_\mathrm e=9.109\cdot10^{-31}$ kg.

</li>

</ul>

The script `rechnung_kap2.py` recalculates all the numbers.
:::
