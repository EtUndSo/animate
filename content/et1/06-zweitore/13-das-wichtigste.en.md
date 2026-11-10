---
title: Key points
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Two-Port Networks
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Chapter 6: Two-Port Networks
order: 1161300
summary: Why four numbers replace a whole network and every parameter form is just another choice
tags: port condition, two-port parameters, impedance form, admittance form, hybrid form, chain form
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

At each port, the current that flows into one terminal flows back out of the other (__port condition__). That leaves two voltages and two currents visible from the outside.

</li>

<li>

In a linear two-port without sources of its own, two of these four quantities determine the other two. Each dependent quantity is a sum of two parts, so four numbers are enough, the __two-port parameters__.

</li>

<li>

The __impedance form__ (currents given), the __admittance form__ (voltages given), the __hybrid form__ (input current and output voltage given) and the __chain form__ (output quantities given) describe the same two-port. Open circuit and short circuit set a given quantity to zero and so isolate the parameters one at a time.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Two-port: four terminals, port condition $I_{1'}=-I_1$, $I_{2'}=-I_2$. Port quantities $U_1$, $I_1$, $U_2$, $I_2$; the current arrows point in.

</li>

<li>

Linear, without sources of its own: two quantities fix the others, four parameters.

</li>

<li>

Z: $\mathbf U=\mathbf Z\,\mathbf I$, open-circuit tests. Y: $\mathbf I=\mathbf Y\,\mathbf U$, short-circuit tests. $\mathbf Y=\mathbf Z^{-1}$.

</li>

<li>

H: $(U_1,I_2)$ from $(I_1,U_2)$. A: $(U_1,I_1)$ from $(U_2,-I_2)$.

</li>

<li>

A parameter is a quotient of effect and cause, with the other cause set to zero. $I=0$ means open circuit, $U=0$ means short circuit.

</li>

<li>

The port's own current gives a resistor; the other port's current or voltage gives a controlled source. Voltages add in series, currents in parallel.

</li>

<li>

Load: $Z_1=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$, $Y_1=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}$.

</li>

<li>

T: $\mathbf Z$ with $R_\mathrm{a}+R_\mathrm{b}$, $R_\mathrm{b}$, $R_\mathrm{b}+R_\mathrm{c}$. $\pi$: $\mathbf Y$ with $G_1+G_2$, $-G_2$, $G_2+G_3$. Conversion by star-delta.

</li>

<li>

Series, series: Z adds. Parallel, parallel: Y adds. Series, parallel: H adds. Chain: A multiplies. Condition: the port condition remains intact.

</li>

<li>

Reciprocal: $Z_{12}=Z_{21}$, $Y_{12}=Y_{21}$, $H_{12}=-H_{21}$, $\det\mathbf A=1$. Unilateral: $Z_{12}=Y_{12}=H_{12}=0$, $\det\mathbf A=0$.

</li>

<li>

Power: $P=U_1I_1+U_2I_2$, active if $P<0$ is possible.

</li>

</ul>
:::

**Looking ahead to [Chapter 7](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html).** The power $P$ from Stage [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10) leads to the next question: At which load does a source or a two-port deliver the greatest power, and what does that cost in efficiency?

**One principle behind all the results.** Of the four port quantities you choose two as causes; the other two are the effects. This choice changes nothing about the two-port, only the calculation, and every result follows from it.

| Result | Where it comes from |
|---|---|
| Four port quantities instead of six | A two-terminal element at each terminal pair takes back at one terminal the charge it gives off at the other (Stage [1](vom-vierpol-zum-zweitor.html#stufe-1)) |
| Four parameters | Superposition: two causes times two effects (Stage [2](vier-groen-zwei-gleichungen-vier-zahlen.html#stufe-2)) |
| Z parameters from open-circuit tests | The causes are currents, and an open port sets a current to zero (Stage [3](impedanzform-und-leerlaufversuch.html#stufe-3)) |
| Input resistance depends on the load | The second cause $I_2$ acts back on the input through $Z_{12}$ (Stage [4](das-zweitor-im-betrieb.html#stufe-4)) |
| Y parameters from short-circuit tests | The causes are voltages, and a wire sets a voltage to zero (Stage [5](admittanzform-und-kurzschlussversuch.html#stufe-5)) |
| $\mathbf Y=\mathbf Z^{-1}$, T and $\pi$ | The same two equations, solved for the other two quantities (Stage [6](umrechnen-t-und.html#stufe-6)) |
| Hybrid form | Mixed causes, suited to components with a current input and a current-source output (Stage [7](hybridform.html#stufe-7)) |
| Chain form, matrix product | The causes of one stage are the effects of the next (Stage [8](kettenform.html#stufe-8)) |
| Z, Y, H add | What both parts share belongs to the causes, what adds up belongs to the effects (Stage [9](zusammenschaltung.html#stufe-9)) |
| Reciprocal, unilateral, active | Relations between the four numbers and their signs (Stage [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)) |
