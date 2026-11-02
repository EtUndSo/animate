---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1201300
summary: How a small voltage controls a large current through a blocking diode
tags: emitter, base, collector, current gain, operating point, negative feedback, transconductance
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

The __emitter__ gives off electrons, the thin __base__ lets them through, the __collector__ collects them. The voltage $U_\mathrm{BE}$ decides how many electrons set off: $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$. The field of the blocking collector diode sweeps them out, and only a small remainder flows through the base, $I_\mathrm{B}=I_\mathrm{C}/B$. The factor $B$ is called the __current gain__.

</li>

<li>

Three terminals mean two independent voltages. That is why $I_\mathrm{C}$ is a surface over $U_\mathrm{BE}$ and $U_\mathrm{CE}$, and each characteristic curve is a slice of it. On this surface the external circuit selects the __operating point__, the DC state of the transistor. An emitter resistor holds it in place through __negative feedback__: the effect weakens its own cause.

</li>

<li>

For small signals, the tangent replaces the curve. Its slope, the __transconductance__ $S=I_\mathrm{C}/U_T$, turns the transistor into a controlled current source. The voltage gain of the common-emitter circuit, the standard circuit with the emitter at ground, is the DC voltage across the collector resistor divided by $U_T$.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$, $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$. Three terminals mean two free voltages, $I_\mathrm{C}$ is a surface, each characteristic curve a slice.

</li>

<li>

Mechanism: $U_\mathrm{BE}$ lowers the barrier, electrons cross the thin base, the field of the blocking CB diode sweeps them out: $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{C}/B$. The base current only replaces the few losses.

</li>

<li>

Regions: cut-off region (open), active ($I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\ge0.2$ V), saturation ($U_\mathrm{CE}=0.2$ V, $I_\mathrm{C}\le B\,I_\mathrm{B}$). Assume, calculate, check. Switch: ends of the load line. Amplifier: active, in the middle.

</li>

<li>

Negative feedback: $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/\bigl(R_\mathrm{E}(1+1/B)+R_\mathrm{i}/B\bigr)$. More current raises the emitter and takes $U_\mathrm{BE}$ back. Current mirror: $I_\mathrm{C2}=I_\mathrm{ref}/(1+2/B)$. Regulator: $U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}$.

</li>

<li>

Small signal: $S=I_\mathrm{C}/U_T$, $r_\mathrm{BE}=B/S$, $r_\mathrm{CE}\approx U_\mathrm{Early}/I_\mathrm{C}$. The tangent holds for $|u_\mathrm{be}|\ll U_T$.

</li>

<li>

Common emitter $A=-U_{R_\mathrm{C}}/U_T$, common collector $A\approx1$, common base $A=+S\,R_\mathrm{C}$. With $R_\mathrm{E}$, $A\approx-R_\mathrm{C}/R_\mathrm{E}$.

</li>

</ul>
:::

**One principle behind all the results.** The transistor has two boundaries with two tasks. Control happens at the base-emitter boundary: the voltage there sets exponentially how many electrons start. The collector-base boundary only collects: whatever arrives is swept out, and the voltage there hardly matters.

| Result | Where it comes from |
|---|---|
| $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$, two free voltages | Three terminals, node and mesh rules (Stage [1](drei-schichten-zwei-spannungen.html#stufe-1)) |
| $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{C}/B$ | Starting, crossing the thin base, being swept out (Stage [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2)) |
| Many characteristic curves | Slices through one surface: steep in $U_\mathrm{BE}$, flat in $U_\mathrm{CE}$ (Stage [3](eine-flache-viele-kennlinien.html#stufe-3)) |
| Three operating regions | Which of the two boundaries conducts (Stage [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)) |
| Operating point | Transistor equation and mesh must hold at once (Stage [5](der-arbeitspunkt.html#stufe-5)) |
| Switch, inverter | The two ends of the load line: little power in the transistor (Stage [6](der-transistor-als-schalter.html#stufe-6)) |
| Stable operating point | More current raises the emitter and takes $U_\mathrm{BE}$ back (Stage [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7)) |
| Current mirror, voltage regulator | Equal $U_\mathrm{BE}$ means equal current, and $U_\mathrm{BE}$ stays almost constant (Stage [8](zwei-schaltungen-die-nutzen.html#stufe-8)) |
| $S=I_\mathrm{C}/U_T$ | The slope of an exponential function is its value divided by the scale $U_T$ (Stage [9](tangente-statt-kurve.html#stufe-9)) |
| $\vert A\vert =U_{R_\mathrm{C}}/U_T$ | Current change $S\,u_\mathrm{in}$ times $R_\mathrm{C}$ (Stage [10](drei-grundschaltungen.html#stufe-10)) |
