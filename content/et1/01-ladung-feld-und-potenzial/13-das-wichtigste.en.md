---
title: Key points
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Charge, Field and Potential
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Chapter 1: Charge, Field and Potential
order: 1111300
summary: Why voltage is a difference and what it does to a charge
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

Charge is a property of electrons and protons, the charged building blocks of atoms. Like charges repel, opposite charges attract, and the sum of all charges is conserved.

</li>

<li>

Every charge produces a field around itself. The field $\vec E$ determines the force per charge at every location: $\vec F=Q\,\vec E$.

</li>

<li>

In a static field, the work done on a charge depends only on start and end, not on the path. That is why every point has a potential $\varphi$, and the voltage $U_{12}=\varphi_1-\varphi_2$ is the energy per charge that the field gives up on the way from point 1 to point 2.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Quantity = numerical value $\cdot$ unit. $1\,\mathrm{V}=1\,\mathrm{J/C}$, $1\,\mathrm{C}=1\,\mathrm{A\,s}$, $1\,\mathrm{N}=1\,\mathrm{kg\,m/s^2}$.

</li>

<li>

Work: $W=\int\vec F\cdot\mathrm{d}\vec s$, on a straight path $F\,s\cos\alpha$. Kinetic energy: $\frac12mv^2$.

</li>

<li>

Charge: $Q=(N_\mathrm{p}-N_\mathrm{e})\,e$; it is conserved.

</li>

<li>

Coulomb: $F=k\,|Q_\mathrm{A}Q_\mathrm{B}|/r^2$; like charges repel, opposite charges attract.

</li>

<li>

Field: $\vec F=Q\vec E$, direction as for the force on a positive charge; point charge $E=k|Q_0|/r^2$.

</li>

<li>

Field lines: from $+$ to $-$, never cross, perpendicular to conductors; in metal $\vec E=0$.

</li>

<li>

Work of the field: $W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$; curl-free: $\oint\vec E\cdot\mathrm{d}\vec s=0$.

</li>

<li>

Potential: $\varphi(P)=\int_P^{P_0}\vec E\cdot\mathrm{d}\vec s$; point charge $\varphi=kQ_0/r$; $\vec E$ points toward falling $\varphi$.

</li>

<li>

Voltage: $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=W_{12}/Q$, $U_{21}=-U_{12}$; uniform field $E=U/d$.

</li>

<li>

Ground: $\varphi:=0$; its location changes no voltage.

</li>

<li>

Charge in the field: $\frac12mv^2+Q\varphi$ constant; from rest $v=\sqrt{2|QU|/m}$.

</li>

<li>

Induction: $u_\mathrm{ind}=-N\,\mathrm{d}\Phi/\mathrm{d} t$; the field is then no longer curl-free.

</li>

</ul>
:::

**Looking ahead to [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html).** In a wire, the field drives very many charges at once: charge flows and a current arises. [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) shows why voltage and current are proportional and how they divide in a network.

**One principle behind all the results.** The force on a charge and its energy depend on the other charges around it and on the charge itself. Dividing by the charge itself leaves a property of the location: force becomes field strength, energy becomes potential.

| Result | Where it comes from |
|---|---|
| Field strength $\vec E=\vec F/Q$ | Force per charge: the test charge has been divided out (Stage [4](die-feldstarke.html#stufe-4)) |
| Field lines, shielding | Picture of $\vec E$; free electrons in metal arrange themselves so that no force remains (Stage [5](feldlinien-und-leiter.html#stufe-5)) |
| $W_{12}=Q\int\vec E\cdot\mathrm{d}\vec s$, independent of path | Work is force times distance; Coulomb forces point radially, only the distance counts (Stage [6](arbeit-im-feld.html#stufe-6)) |
| Potential $\varphi$ | Work per charge up to the reference point (Stage [7](das-potenzial.html#stufe-7)) |
| Voltage, ground | Work per charge between two points; the zero point can be chosen freely (Stage [8](spannung-und-masse.html#stufe-8)) |
| Speed of a charge | The energy $QU$ becomes kinetic energy (Stage [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9)) |
| Induction | Limit of the principle: if a magnetic field changes, the work depends on the path (Stage [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10)) |
