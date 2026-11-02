---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Sources and Equivalent Sources
order: 1151300
summary: Why two numbers replace an entire network
tags: superposition, open-circuit voltage, internal resistance, equivalent source, short circuit
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

In a linear network the effects of the sources add up, because all the equations are linear. This is __superposition__, the overlaying of effects.

</li>

<li>

Therefore the voltage at two terminals A and B is a straight line in the terminal current: $U_\mathrm{AB}=U_\mathrm{OC}-R_\mathrm{i}\,I_\mathrm{A}$. The sources set the __open-circuit voltage__ $U_\mathrm{OC}$ (the voltage with the terminals open), the resistors set the __internal resistance__ $R_\mathrm{i}$ (the slope).

</li>

<li>

A straight line has two numbers. So the network behaves like an __equivalent source__, a source with an internal resistance. The open circuit and the __short circuit__ (terminals connected) supply the numbers: $R_\mathrm{i}=U_\mathrm{OC}/I_\mathrm{SC}$.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Series: add resistances, same current. Parallel: add conductances, same voltage. Combine from the inside out.

</li>

<li>

Nodes of equal potential may be connected, current-free branches may be cut. Symmetry shows where this is possible.

</li>

<li>

Star and delta are interchangeable at the terminals: $R_{10}=R_{12}R_{31}/(R_{12}+R_{23}+R_{31})$.

</li>

<li>

Ideal sources hold one quantity fixed. Real sources: $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}$. Converting: $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$, same resistance.

</li>

<li>

Superposition: voltage sources become wires, current sources become gaps, partial effects add. Powers do not add.

</li>

<li>

Every linear one-port is a straight line: $U_\mathrm{i}=U_\mathrm{OC}$, $I_\mathrm{i}=I_\mathrm{SC}$, $R_\mathrm{i}=U_\mathrm{OC}/I_\mathrm{SC}$. The operating point is the intersection with the line of the load.

</li>

</ul>
:::

**One principle behind all the results.** At two terminals a linear network behaves like a single straight line in the current-voltage diagram, which is why two numbers are enough. From outside, only this characteristic curve counts: two circuits with the same line are interchangeable, no matter what they look like inside. The table assigns the results to this idea.

| Result | Where it comes from |
|---|---|
| Total resistance | Without a source the characteristic curve passes through the origin, so one number is enough (Stage [1](widerstande-zusammenfassen.html#stufe-1)) |
| Symmetry, half circuit | Equal potentials may be connected, current-free branches may be cut (Stage [2](symmetrie-nutzen.html#stufe-2)) |
| Star and delta | Three terminals, three numbers, hence interchangeable (Stage [3](stern-und-dreieck.html#stufe-3)) |
| Ideal sources | Limiting cases of the line: horizontal and vertical (Stage [4](ideale-quellen.html#stufe-4)) |
| Operating point | Intersection of the source line with the load line (Stage [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5)) |
| Converting sources | The same line, read from the other axis (Stage [6](spannungsquelle-oder-stromquelle.html#stufe-6)) |
| Interconnecting sources | Lines add in voltage or in current (Stage [7](quellen-zusammenschalten.html#stufe-7)) |
| Superposition | Linear equations, each source acts on its own (Stage [8](uberlagerung.html#stufe-8)) |
| Thevenin and Norton | Superposition with the terminal current as one more cause (Stage [9](thevenin-und-norton.html#stufe-9)) |
| R-2R converter | Every switch is a source, every rung halves (Stage [10](der-r-2r-wandler.html#stufe-10)) |
