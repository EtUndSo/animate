---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Current, Resistance and Kirchhoff's Laws
order: 1121200
summary: Why electrons crawl while the current is there at once, and why networks obey conservation laws
tags: drift velocity, current density, voltage divider
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

The field in the conductor accelerates the free electrons, and collisions take the gained velocity away again. What remains is a small __drift velocity__ (average velocity along the conductor) that is proportional to the field. That is why the __current density__, the current per cross-sectional area, is proportional to the field, and $U=R\,I$ follows for the component.

</li>

<li>

The node rule is charge conservation, the mesh rule is energy conservation.

</li>

<li>

Together, the three laws give every network exactly as many equations as it has unknowns. In series the voltage divides (__voltage divider__: two resistors whose ratio sets a partial voltage), in parallel the current divides.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Current: $i=\mathrm{d} Q/\mathrm{d} t$, $I=q\,v\,A$; current density $\vec j=q\,\vec v$.

</li>

<li>

Drift: $\vec v_\mathrm D=-\mu\,\vec E$, $v_\mathrm D=I/(n\,e\,A)$; current at once, because the field travels.

</li>

<li>

Material: $\vec j=\sigma\,\vec E$, $\sigma=n\,e\,\mu=1/\rho$.

</li>

<li>

Component: $U=R\,I$, $R=\rho\,L/A$, $G=1/R$; power $P=U\,I$.

</li>

<li>

E series: $w=(\sqrt[N]{10})^i$; temperature: $R(\vartheta)=R(\vartheta_0)(1+\alpha\,(\vartheta-\vartheta_0))$; PTC, NTC.

</li>

<li>

Two-terminal element: characteristic curve $I=f(U)$; PSC same direction, ASC opposite directions; electrons move against the conventional current.

</li>

<li>

Network: $k$ nodes, $z$ branches, $m=z-k+1$ independent meshes; tree of $k-1$ branches.

</li>

<li>

Node rule: $\sum I=0$, $k-1$ equations; mesh rule: $\sum U=0$, $z-k+1$ equations.

</li>

<li>

Series: $R_\mathrm{tot}=\sum R_i$, $U_\nu/U=R_\nu/\sum R_i$, only when unloaded.

</li>

<li>

Parallel: $G_\mathrm{tot}=\sum G_i$, $R_1\parallel R_2=R_1R_2/(R_1+R_2)$, $I_1=I_\mathrm{tot}\,R_2/(R_1+R_2)$.

</li>

<li>

Loaded: $U_2/U=(R_2\parallel R_\mathrm L)/(R_1+R_2\parallel R_\mathrm L)$, error $R_\mathrm i/(R_\mathrm i+R_\mathrm L)$.

</li>

</ul>
:::

**Looking ahead to [Part 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html).** A node stores almost no charge. The capacitor of two large plates does the opposite: it stores charge and energy.

**One principle behind all the results.** Two conservation laws and one equilibrium carry the chapter: charge is not lost, energy is not lost, and in the conductor the drive from the field and the braking from collisions balance each other.

| Result | Where it comes from |
|---|---|
| $I=\mathrm{d} Q/\mathrm{d} t$, $j=q\,v$ | Charge that passes through an area in a given time (Stage [1](strom-ist-bewegte-ladung.html#stufe-1)) |
| small, constant drift | Equilibrium of field and collisions, huge electron density (Stage [2](langsame-elektronen-sofortiger-strom.html#stufe-2)) |
| Current is there at once | The field travels, not the electrons; the wire is already full (Stage [2](langsame-elektronen-sofortiger-strom.html#stufe-2)) |
| $U=R\,I$, $R=\rho L/A$ | Drift proportional to field, field proportional to voltage (Stage [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3)) |
| Temperature dependence | Heat changes the flight time or the number of charge carriers (Stage [4](reale-widerstande-werte-und-temperatur.html#stufe-4)) |
| Reference arrows, $m=z-k+1$ | Agreement and counting before calculating (Stages [5](zweipole-und-zahlpfeile.html#stufe-5) and [6](knoten-zweige-maschen.html#stufe-6)) |
| Node rule | Charge conservation: a node stores nothing (Stage [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7)) |
| Mesh rule | Energy conservation: a round trip ends at the starting potential (Stage [8](die-maschenregel-ist-energieerhaltung.html#stufe-8)) |
| Voltage divider, current divider | Both rules applied to series and parallel (Stages [9](reihenschaltung-und-spannungsteiler.html#stufe-9) and [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10)) |
