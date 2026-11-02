---
title: Overview: Two-Port Networks
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Two-Port Networks
order: 1160100
summary: Why four numbers replace a whole network and every parameter form is just another choice
tags: two-port, port
lang: en
---

## What this is about

Between source and load there often sits another network: a cable, a filter, an attenuator or an amplifier. It has an input side and an output side, and from the outside all that counts is what it does to voltage and current. A network with two such terminal pairs is called a __two-port__, and each terminal pair is a __port__. [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) replaced a network at one terminal pair by two numbers, equivalent voltage and internal resistance. The question of this chapter is: *How many numbers do you need for two terminal pairs, and how do you measure them from the outside?*



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
<ul>

<li>

⁠**T two-port:** a T network ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) with the series resistor $R_\mathrm{a}=15\,\Omega$ at the input, the shunt resistor $R_\mathrm{b}=20\,\Omega$ to the continuous lower line and the series resistor $R_\mathrm{c}=20\,\Omega$ at the output.

</li>

<li>

⁠**Operation:** A real voltage source with $U_\mathrm{q}=9$ V and $R_\mathrm{q}=5\,\Omega$ is connected to port 1, and the load $R_\mathrm{L}=60\,\Omega$ to port 2.

</li>

<li>

⁠**Amplifier:** a model with 2 k$\Omega$ at the input, current gain 100, 20 k$\Omega$ at the output and a load of 5 k$\Omega$, shown in Stage [7](hybridform.html#stufe-7).

</li>

<li>

All quantities are DC quantities. The script `rechnung_kap6.py` recalculates all the numbers.

</li>

</ul>
:::
