---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Measuring Current and Voltage
order: 1140900
summary: Why every meter changes the circuit and how to measure accurately anyway
tags: ammeter, voltmeter, correct-current measurement, correct-voltage measurement, Wheatstone bridge, balance
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

An __ammeter__ (current meter) sits in series in the circuit and adds its internal resistance to it. A __voltmeter__ (voltage meter) sits in parallel and opens a second current path. Both show the value of the changed circuit.

</li>

<li>

The relative error is about $R_\mathrm i/R$ for the ammeter and about $R/R_\mathrm i$ for the voltmeter. If both measure at once, only one reading is right: __correct-current measurement__ (the current is right) or __correct-voltage measurement__ (the voltage is right).

</li>

<li>

The __Wheatstone bridge__ (two voltage dividers on one source with an instrument between them) compares resistances. At __balance__ (adjusted to a reading of zero), no current flows through the instrument. That is why its internal resistance, its scale and the source voltage drop out of the result $R_4=R_3R_2/R_1$.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

A meter is a resistor and shows the value of the changed circuit.

</li>

<li>

Ammeter: $I_R/I_R'=1+R_\mathrm i/R$. Voltmeter: $U_L/U_L'=1+R_L/R_\mathrm i$.

</li>

<li>

Extending the range: $R_\mathrm{Shunt}=R_\mathrm{old}I_\mathrm{old}/(I_\mathrm{new}-I_\mathrm{old})$ and $R_\mathrm V=R_\mathrm{old}(\alpha-1)$.

</li>

<li>

Correct current $U/I=R+R_\mathrm{iA}$ for large $R$, correct voltage $U/I=R\parallel R_\mathrm{iV}$ for small $R$.

</li>

<li>

Balance: $R_4=R_3R_2/R_1$, independent of internal resistance, scale and source voltage.

</li>

<li>

Unbalanced: $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$. Without the common voltage, a small range is enough.

</li>

</ul>
:::

**One principle behind all the results.** To the circuit, a meter is one more resistor. All the errors follow from the same rules as in [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): mesh rule, node rule, Ohm's law.

| Result | Where it comes from |
|---|---|
| Internal resistance | The instrument needs current, and its coil has resistance (Stage [1](das-messgerat-ist-ein-bauteil.html#stufe-1)) |
| Shunt and series resistor | Current divider and voltage divider protect the instrument (Stage [2](den-messbereich-erweitern.html#stufe-2)) |
| $I_R'=U/(R+R_\mathrm i)$ | One more resistor in the mesh (Stage [3](der-fehler-beim-strommessen.html#stufe-3)) |
| $U_L'=U_L/(1+R_L/R_\mathrm i)$ | One more branch at the node (Stage [4](der-fehler-beim-spannungsmessen.html#stufe-4)) |
| Correct current and correct voltage | Each instrument lies in the measuring circuit of the other (Stage [5](strom-und-spannung-zugleich.html#stufe-5)) |
| Balance $R_4=R_3R_2/R_1$ | Without current, the instrument takes nothing from the bridge (Stage [6](die-wheatstonesche-brucke.html#stufe-6)) |
| $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$ | The bridge subtracts the common voltage (Stage [7](die-verstimmte-brucke.html#stufe-7)) |
