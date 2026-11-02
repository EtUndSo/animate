---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1131200
summary: How current flows into an insulator and where the energy is afterward
tags: field energy, time constant
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

A capacitor does not let charge through, it displaces it: electrons leave one plate and arrive on the other, and the same current flows at both terminals at the same moment.

</li>

<li>

The separated charge $Q$ produces the field between the plates. This field determines the voltage $U=Q/C$, and it holds the __field energy__ $\frac12CU^2$, stored in the space between the plates.

</li>

<li>

Charge needs current and time, so the voltage does not jump. At the first moment an empty capacitor acts like a short circuit (current at 0 V), a full one like an open circuit (voltage without current). In between runs an exponential curve with the __time constant__ $\tau=RC$, the time that sets the pace of charging.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

The capacitor separates charge: $+Q$ and $-Q$, total charge zero. The same current flows at both terminals, no charge through the gap.

</li>

<li>

Capacitance: $C=Q/U$; $i=C\,\mathrm{d} u/\mathrm{d} t$; $u(t)=u(t_0)+\frac1C\int_{t_0}^ti\,\mathrm{d} t'$. $u$ does not jump, direct current is blocked.

</li>

<li>

Parallel-plate capacitor: $C=\varepsilon A/d$ with $\varepsilon=\varepsilon_0\varepsilon_\mathrm{r}$, $\varepsilon_0=8.854\cdot10^{-12}$ A s/(V m).

</li>

<li>

Energy: $W=\frac12CU^2=\frac12QU=Q^2/(2C)$, in the field with the density $w=\frac12\varepsilon E^2$.

</li>

<li>

Parallel: $C_\mathrm{G}=\sum C_i$. Series: $1/C_\mathrm{G}=\sum1/C_i$.

</li>

<li>

Island: $Q_\mathrm{tot}=\sum C_iU_i=$ const. The energy is not conserved in the process.

</li>

<li>

Charging: $u_C=U_0(1-\mathrm{e}^{-t/\tau})$, $i=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Discharging: $u_C=U_0\,\mathrm{e}^{-t/\tau}$, $i=-\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Time constant $\tau=RC$.

</li>

<li>

General: $u_C(t)=u_\infty+(u_C(0)-u_\infty)\,\mathrm{e}^{-t/\tau}$. Empty, it acts at the first moment like a short circuit; full, like an open circuit.

</li>

</ul>
:::

**One principle behind all the results.** The voltage shows how much charge is separated, and charge changes only through current. From these two facts, $u=q/C$ and $i=\mathrm{d} q/\mathrm{d} t$, all the results of this chapter follow.

| Result | Where it comes from |
|---|---|
| Current despite the gap | Charge is displaced, not passed through (Stage [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)) |
| $Q=CU$ | Twice the charge, twice the field, twice the voltage (Stage [2](die-kapazitat.html#stufe-2)) |
| $i=C\,\mathrm{d} u/\mathrm{d} t$, $u$ does not jump | Current is charge per time (Stage [3](strom-und-spannung-am-kondensator.html#stufe-3)) |
| $C=\varepsilon A/d$ | Field per charge depends on area, separation and material (Stage [4](plattenkondensator-und-dielektrikum.html#stufe-4)) |
| Types of construction | Large $A$, small $d$, large $\varepsilon$ (Stage [5](bauformen-und-selbstentladung.html#stufe-5)) |
| $W=\frac12CU^2$ | Every further charge runs against the voltage already present (Stage [6](die-gespeicherte-energie.html#stufe-6)) |
| Parallel and series connection | Same voltage or same charge (Stage [7](parallel-und-reihenschaltung.html#stufe-7)) |
| Charge sharing | Charge cannot leave an island (Stage [8](ladungserhaltung-beim-umschalten.html#stufe-8)) |
| Short circuit, open circuit, exponential curve | The current depends on the voltage it builds up itself (Stage [9](aufladen-uber-einen-widerstand.html#stufe-9)) |
| Discharging, $\tau=RC$ | The same feedback with a different starting value (Stage [10](entladen-und-zeitkonstante.html#stufe-10)) |
