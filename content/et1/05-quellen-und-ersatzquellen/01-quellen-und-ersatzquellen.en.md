---
title: Overview: Sources and Equivalent Sources
kurz: Overview
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1150100
summary: Why two numbers replace an entire network
tags: 
lang: en
---

## What this is about

A sensor hangs on two wires, and behind them lies a circuit of dozens of components. It senses only the voltage and the current at its terminals. The question of this chapter is: *How many numbers does it take to describe an entire network at two terminals?* The answer is two, as long as the network is linear: it contains only resistors and fixed sources, and twice the cause gives twice the effect.

The way there has three parts. Stages [1](widerstande-zusammenfassen.html#stufe-1) to [3](stern-und-dreieck.html#stufe-3) reduce networks without a source. Stages [4](ideale-quellen.html#stufe-4) to [7](quellen-zusammenschalten.html#stufe-7) introduce sources and show that they too are straight lines. Stages [8](uberlagerung.html#stufe-8) and [9](thevenin-und-norton.html#stufe-9) prove that this holds for every linear network, and Stage [10](der-r-2r-wandler.html#stufe-10) uses it in a converter.

**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Battery:** the 9 V battery from [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). Its source voltage (the voltage supplied by the chemistry) is $U_\mathrm{q}=9$ V, its internal resistance $R_\mathrm{q}=2\,\Omega$.

</li>

<li>

⁠**Load:** the connected device, with the resistance $R_\mathrm{L}=16\,\Omega$. Stages [1](widerstande-zusammenfassen.html#stufe-1) to [3](stern-und-dreieck.html#stufe-3) build load networks from many resistors, all of which come to exactly 16 $\Omega$.

</li>

<li>

⁠**Network N:** two sources and two resistors (Fig. [9](uberlagerung.html#abb-9)): $U_\mathrm{q1}=18$ V, $R_1=6\,\Omega$, $R_2=3\,\Omega$, $I_\mathrm{q2}=1.5$ A. Stage [9](thevenin-und-norton.html#stufe-9) shows that from outside, N cannot be told apart from the battery.

</li>

</ul>

:::
