---
title: Overview: The Bipolar Transistor
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200100
summary: How a small voltage controls a large current through a blocking diode
tags: bipolar transistor
lang: en
---

## What this is about

A microphone delivers millivolts, a loudspeaker needs volts. A computer output delivers milliamperes, a motor needs amperes. Between them sits a component that controls a large current with a small signal. The classic representative is the __bipolar transistor__, a semiconductor component made of three layers with three terminals. The energy comes from the supply voltage; the signal only sets the amount. The other important type, the MOSFET, dominates digital electronics and is not the subject of this chapter. The question is: *How can a voltage of 0.6 V control a current that flows through a blocking diode?*



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Transistor T:** an npn small-signal transistor made of silicon with $B=200$, $I_\mathrm{S}=1.9\cdot10^{-13}$ A (saturation reverse current, [Part 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) and $U_T=26$ mV (thermal voltage at 300 K, rounded from 25.85 mV). For hand calculations, one approximates $U_\mathrm{BE}=0.6$ V when the transistor conducts and $U_\mathrm{CE,sat}=0.2$ V when it is fully switched on. Limiting values: $U_\mathrm{CE,max}=40$ V, $I_\mathrm{C,max}=100$ mA, $P_\mathrm{max}=400$ mW.

</li>

<li>

⁠**Circuit:** supply $U_\mathrm{CC}=12$ V, collector resistor $R_\mathrm{C}=3$ k$\Omega$, base resistor $R_\mathrm{B}=440$ k$\Omega$, input voltage $U_\mathrm{in}=5$ V. This gives the operating point $I_\mathrm{B}=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=6$ V.

</li>

<li>

⁠**Version with negative feedback:** base divider $R_1=31$ k$\Omega$, $R_2=9$ k$\Omega$, emitter resistor $R_\mathrm{E}=1$ k$\Omega$ (Stage [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7)).

</li>

</ul>

The script `rechnung_kap10.py` recalculates all the numbers.
:::
