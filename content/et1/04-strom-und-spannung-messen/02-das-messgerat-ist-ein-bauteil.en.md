---
title: Stage 1: The meter is a component
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Measuring Current and Voltage
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Chapter 4: Measuring Current and Voltage
order: 1140200
summary: Before an error can be calculated, it must be clear what a meter is electrically: a component with two terminals and a resistance between them.
tags: full-scale value
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before an error can be calculated, it must be clear what a meter is electrically: a component with two terminals and a resistance between them.
:::

**The idea.** In a pointer instrument, a rotatable coil of thin wire sits between the poles of a permanent magnet (Fig. [1](#abb-1)). When current flows, the magnetic field exerts a force on the moving electrons in the wire, and the coil turns against a spiral spring. The torque grows with the current, the counterforce of the spring with the angle. That is why the deflection is proportional to the current. Two things cannot be avoided: without current there is no deflection, and with current a voltage drops across the wire. A digital multimeter (a device with a numeric display) converts the voltage across an internal resistor into a number. There, too, current flows through a resistor.

:::abbildung et1/k4messwerk 1
Left, the meter movement: the coil turns in the magnetic field against a spring (not drawn). Right, the equivalent circuits: ideal instrument plus internal resistance, in series or in parallel.
:::

:::definition Definition 1.1 (Measuring range and internal resistance)
<span class="anker" id="satz-1-1"></span>

The measuring range extends up to the __full-scale value__, the largest value that can be displayed (for a pointer, full-scale deflection). The internal resistance $R_\mathrm i$ is the resistance between the terminals.

<ul>

<li>

An ammeter is connected in series. Ideally $R_\mathrm i=0$, in practice about $R_\mathrm i\approx1\,\Omega$.

</li>

<li>

A voltmeter is connected in parallel. Ideally $R_\mathrm i\to\infty$, in practice about $R_\mathrm i\approx10\,\mathrm{M\Omega}$.

</li>

</ul>
:::

⁠**How to read it:** Current is charge passing through a cross section. That is why you open the circuit and send the entire current through the ammeter. No voltage should drop across it, so $R_\mathrm i$ should be small. Voltage is the difference between two points. That is why you connect the voltmeter to both points without opening the circuit. No current should flow through it, so $R_\mathrm i$ should be large. The numerical values are typical of digital multimeters. **Validity:** $R_\mathrm i$ applies to one measuring range and changes when the range is switched (Stage [2](den-messbereich-erweitern.html#stufe-2)).

::::beispiel
The meter movement of the reference model is already both. At full-scale deflection, 50 µ A flow through 2 k$\Omega$, so $U_\mathrm M=R_\mathrm MI_\mathrm M=100$ mV are across it. The scale could be labeled with 50 µ A or with 100 mV: two names for the same deflection.
::::

⁠**Limiting case:** For $R_\mathrm i=0$ the ammeter acts like a piece of wire, for $R_\mathrm i\to\infty$ the voltmeter like an open gap. To the circuit, ideal instruments are not there.

:::frage If no current flows through an ideal voltmeter, how can it display anything?
A pointer could not, because without current there is no deflection. The ideal case is a limit, not a device. A large internal resistance makes the current small, not zero. Digital devices get by with very little current because the energy for the display comes from their own battery, not from the circuit being measured.
:::

:::aufgabe Exercise 1 ★ Connected wrongly
<span class="anker" id="aufg-1"></span>

First predict which device is in danger. (a) The ammeter of the reference model is accidentally connected directly across the 9 V source. What current flows? (b) The voltmeter is accidentally connected in series with $R$ on the source. What does it show, and what current flows?

:::loesung
(a) The ammeter is in danger, because its small resistance hardly limits the current: $I=9\,\mathrm{V}/10\,\Omega=0.9$ A, ninety times the range. Through the meter movement flow 4.5 mA instead of 50 µ A, and 8.06 W are released in the shunt.

(b) $I=9\,\mathrm{V}/201.8\,\mathrm{k\Omega}=44.6$ µ A. The voltmeter shows $44.6\,\mu\text{A}\cdot200\,\mathrm{k\Omega}=8.92$ V; 80 mV remain across $R$. Nothing breaks, but the circuit no longer works.
:::
:::
