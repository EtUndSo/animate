---
title: Key points
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Power, Matching and Efficiency
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Chapter 7: Power, Matching and Efficiency
order: 1170900
summary: Why half of the energy stays in the source at the power maximum
tags: Joule heat, power matching, efficiency, voltage matching, current matching
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

Voltage is energy per charge, current is charge per time. Their product is energy per time: $p=u\,i$.

</li>

<li>

In a resistor, the field accelerates the electrons, and every collision hands the energy gained to the atomic lattice. That is why all the power there turns into heat, the __Joule heat__, with $P=R\,I^2$.

</li>

<li>

A source with internal resistance $R_\mathrm{i}$ delivers the greatest power to the load $R_\mathrm{L}=R_\mathrm{i}$. This is called __power matching__. There, the energy of each charge divides equally between source and load, and the __efficiency__, the fraction of the power that is used, is 50 %. A fixed voltage is provided by __voltage matching__ (load large compared with the source), a fixed current by __current matching__ (load small compared with the source).

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Power is energy per coulomb times coulombs per second: $p=u\,i$. Energy is its time integral.

</li>

<li>

In a resistor, collisions give everything to the lattice: $P=R\,I^2=U^2/R$, limited by $P_\mathrm{max}$.

</li>

<li>

At a resistor with a sinusoidal voltage, $P=\frac12\hat u^2/R=\frac12\hat\imath^2R$.

</li>

<li>

The same power at $n$ times the voltage lowers the line loss to $1/n^2$.

</li>

<li>

Balance: $P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$. Efficiency: $\eta=U_\mathrm{L}/U_\mathrm{q}=R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$.

</li>

<li>

Greatest power at $R_\mathrm{L}=R_\mathrm{i}$: $P_\mathrm{L,max}=U_\mathrm{q}^2/(4R_\mathrm{i})$, with $\eta=\frac12$, because current and efficiency run linearly against each other.

</li>

<li>

Power engineering wants $R_\mathrm{L}\gg R_\mathrm{i}$, signal transmission $R_\mathrm{L}=R_\mathrm{i}$. Equivalent sources give the maximum correctly, but not the efficiency.

</li>

</ul>
:::

**One principle behind all the results.** Every power is the product of two answers: How much energy does one coulomb give off at this point, and how many coulombs pass per second?

| Result | Where it comes from |
|---|---|
| $p=u\,i$ | Energy per charge times charge per time (Stage [1](energie-je-ladung-mal-ladung-je-zeit.html#stufe-1)) |
| $P=R\,I^2=U^2/R$, power rating | Collisions give everything to the lattice; twice the current means twice as many coulombs, each giving off twice as much (Stage [2](warum-der-widerstand-warm-wird.html#stufe-2)) |
| $P=\frac12\hat u^2/R$ | $u$ and $i$ change sign together, $\cos^2$ has the mean value $\frac12$ (Stage [3](mittlere-leistung-bei-sinusspannung.html#stufe-3)) |
| High-voltage lines | The same power with fewer coulombs, each of which loses less (Stage [4](leitungsverluste.html#stufe-4)) |
| $\eta=U_\mathrm{L}/U_\mathrm{q}$ | Fraction of the energy per coulomb that reaches the load (Stage [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)) |
| $R_\mathrm{L}=R_\mathrm{i}$ | Current and load voltage run linearly against each other, their product is greatest in the middle (Stage [6](leistungsanpassung.html#stufe-6)) |
| $\eta=50\,\%$ at the maximum | The middle means: half of the energy per coulomb stays inside (Stage [7](warum-50-und-welches-ziel-gilt.html#stufe-7)) |
