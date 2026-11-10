---
title: Overview: The Operational Amplifier
kurz: Overview
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Operational Amplifier
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Chapter 11: The Operational Amplifier
order: 1210100
summary: How a huge, imprecise factor turns into a component whose behavior is determined by the resistors alone
tags: operational amplifier, open-loop gain, negative feedback
lang: en
---

## What this is about

An __operational amplifier__, op amp for short, is an integrated amplifier made of a few dozen transistors. It amplifies the voltage between its two inputs by a factor of about 100000. This factor is called the __open-loop gain__. It varies by a factor of four from one specimen to the next and changes with temperature. Nevertheless, this component is used to build amplifiers that feel only 0.01 % of this variation, as well as summing amplifiers and integrators. The question is: *How does a huge, imprecise factor turn into a component whose behavior is determined by the resistors alone?* The answer is __negative feedback__: part of the output voltage is fed back to the input in such a way that it counteracts its own cause.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Op amp V:** Open-loop gain $A=100000$ (specimens 50000 to 200000), input resistance $r_\mathrm{e}=1$ M$\Omega$, output resistance $r_\mathrm{a}=75\,\Omega$. Supply $\pm12$ V; the output reaches $\pm11$ V and at most 20 mA. For Stage [10](wo-die-regeln-enden.html#stufe-10): transition frequency $f_\mathrm{T}=1$ MHz (there $A$ has fallen to 1), offset $U_\mathrm{off}=1$ mV (residual difference of the inputs), input bias current $I_\mathrm{B}=50$ nA (base current of the input transistors), common-mode rejection 90 dB (attenuation of common disturbances).

</li>

<li>

⁠**External circuit:** $R_1=10$ k$\Omega$, $R_2=40$ k$\Omega$, $U_\mathrm{E}=1$ V.

</li>

<li>

⁠**Differential stage:** transistors T from [Chapter 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html) ($B=200$, $U_T=26$ mV), $I_0=2$ mA, $R_\mathrm{C}=3$ k$\Omega$.

</li>

<li>

⁠**Sensor:** 1 mV rms, internal resistance 10 k$\Omega$, bandwidth (the frequency range passed) 20 kHz, temperature 300 K.

</li>

</ul>

The script `rechnung_kap11.py` recalculates all the numbers.
:::
