---
title: Overview: The Capacitor
kurz: Overview
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Capacitor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Chapter 3: The Capacitor
order: 1130100
summary: How current flows into an insulator and where the energy is afterward
tags: capacitor, electrode, dielectric, capacitance, parallel-plate capacitor, RC circuit
lang: en
---

## What this is about

Two metal plates with an insulator between them: this component is called a __capacitor__. If you connect it to a battery, current flows in the leads even though the plates do not touch. The current grows weaker and stops by itself. If you disconnect the battery, the voltage remains, and the component can drive current on its own. The question of this chapter is: *How can current flow into an insulator, why does it end by itself, and where is the energy afterward?*

Each plate is an __electrode__; the insulator between them is called the __dielectric__. The quantity that characterizes the component is the __capacitance__: it says how much charge sits on the plates per volt. The basic form is two flat plates, the __parallel-plate capacitor__.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Pair of plates from [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html):** square plates with 10 cm edge length (area $A=100$ cm$^2$), separation $d=3$ mm, air between them, 9 V voltage. The field is $E=3$ kV/m.

</li>

<li>

⁠**RC circuit:** An __RC circuit__ is the series connection of a resistor and a capacitor across a source. Here a 9 V battery ($U_0=9$ V) charges a capacitor $C=100\,\mu\text{F}$ through $R=10\,\mathrm{k\Omega}$. This gives $\tau=RC=1$ s. The internal resistance of the battery, around 2 $\Omega$, is neglected: it is 5000 times smaller than $R$.

</li>

<li>

⁠**Two capacitors:** $C_1=100\,\mu\text{F}$ (the same one as in the RC circuit) and $C_2=50\,\mu\text{F}$.

</li>

</ul>

The script `rechnung_kap3.py` recalculates all the numbers.
:::
