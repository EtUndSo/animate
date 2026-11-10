---
title: Stage 3: Ohm's law from field and collisions
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Current, Resistance and Kirchhoff's Laws
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Chapter 2: Current, Resistance and Kirchhoff's Laws
order: 1120400
summary: Stage 2 has shown that the drift is proportional to the field.
tags: conductivity, resistivity, conductance, linear, homogeneous, power
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Stage [2](langsame-elektronen-sofortiger-strom.html#stufe-2) has shown that the drift is proportional to the field. In a few steps, this stage turns that into the most important law of circuit engineering.
:::

**The idea.** More voltage means a stronger field in the conductor, a stronger field means faster drift, faster drift means more current. Each step is a proportionality, and so is the whole way from $U$ to $I$. The factor contains the material and the shape (Fig. [4](#abb-4)).

:::abbildung et1/k2ohm 4
Left: conductor with length $L$ and cross section $A$. The field $E$ and the current density $j$ are the same everywhere. Right: characteristic curves in the reference model. $I$ versus $U$ is a straight line through the origin; its slope is the conductance $G=\Delta I/\Delta U$, the reciprocal of $R=\Delta U/\Delta I$. The point belongs to 9 V across $R_1+R_2=3\,\mathrm{k\Omega}$.
:::

:::satz Theorem 3.1 (Ohm's law)
<span class="anker" id="satz-3-1"></span>

For a conductor with the electron density $n$,

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} \vec j&=\sigma\,\vec E,\qquad\sigma=n\,e\,\mu,\qquad\rho=\frac1\sigma,\\ U&=R\,I,\qquad R=\frac{L}{\sigma\,A}=\rho\,\frac LA,\qquad G=\frac1R=\frac IU. \end{aligned} \tag{3.1|3.2}$$
:::

⁠**How to read it:** $\sigma$ is the __conductivity__ in S/m, $\rho$ the __resistivity__ in $\Omega\,\mathrm m$. It is often given in $\Omega\,\mathrm{mm^2/m}$; copper then has 0.017. $R$ is the resistance in $\Omega$ (ohms), $1\,\Omega=1$ V/A: m$\Omega$ in a wire, k$\Omega$ in circuits. Its circuit symbol is a rectangle (Fig. [6](zweipole-und-zahlpfeile.html#abb-6)). $G$ is the __conductance__ in S (siemens), $1\,\mathrm{S}=1\,\Omega^{-1}$. The units bear the names of Georg Simon Ohm and Werner von Siemens. **Validity:** The conductor must be __linear__ ($\vec j$ proportional to $\vec E$) and __homogeneous__ (the same material everywhere). The temperature must be constant (Stage [4](reale-widerstande-werte-und-temperatur.html#stufe-4)), and $L\gg\sqrt A$ must hold so that the field at the ends plays no role. Linearity holds very precisely in metals: the flight time $T$ does not depend on $E$, because the drift is more than $10^{9}$ times smaller than the random motion.

:::herleitung From field to component
Current density of the electrons, Stage [1](strom-ist-bewegte-ladung.html#stufe-1), with $q=-n\,e$ and [(2.1)](langsame-elektronen-sofortiger-strom.html#gl-2-1):

$$\vec j=q\,\vec v_\mathrm D=(-n\,e)(-\mu\,\vec E)=n\,e\,\mu\,\vec E=\sigma\,\vec E.$$

The field is uniform, so $U=E\,L$ ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Thus

$$I=j\,A=\sigma\,E\,A=\frac{\sigma\,A}{L}\,U\quad\Longrightarrow\quad U=\frac{L}{\sigma\,A}\,I=R\,I.$$
:::

| Conductor | $\rho$ in $10^{-8}\,\Omega\,\mathrm m$ | $\sigma$ in $10^{6}$ S/m | Conductor | $\rho$ in $10^{-8}\,\Omega\,\mathrm m$ | $\sigma$ in $10^{6}$ S/m |
|---|---|---|---|---|---|
| Silver | 1.6 | 62 | Brass | 7 to 9 | 14 to 11 |
| Copper | 1.7 | 59 | Iron | 10 to 15 | 10 to 7 |
| Gold | 2.3 | 43 | Platinum | 11 | 9 |
| Aluminum | 2.8 | 36 | Constantan | 50 | 2 |
| Tungsten | 5.5 | 18 | Carbon | 5000 to 10000 | 0.02 to 0.01 |

::::beispiel
The wire has $R=\rho\,L/A=34\,\mathrm{m\Omega}$. At 3 mA, 0.10 mV drops across it, which is $1.1\cdot10^{-5}$ of the 9 V. This justifies why circuit diagrams draw wires as ideal, without voltage along the wire. The same calculation shows why resistors are not made of copper: $2\,\mathrm{k\Omega}$ would need 1.2 km of copper at a cross section of $0.01\,\mathrm{mm^2}$, but only 40 m of constantan.
::::

⁠**Limiting cases:** Twice the length at the same voltage halves the field and thus the current. Twice the cross section acts like two wires side by side; the current doubles. $U=0$ gives $I=0$.

**Where the energy goes.** At each collision, the electron gives the kinetic energy gained in the field to the lattice. The lattice vibrates more strongly, and that is heat. Each coulomb gives up the energy $U$ in joules, and $I$ coulombs pass per second. The __power__, the energy per time, is therefore $P=U\,I=R\,I^2$. The chain converts $9\,\mathrm{V}\cdot3\,\mathrm{mA}=27$ mW. [Chapter 7](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html) treats power in more detail.

:::frage You can always calculate $R=U/I$. So what does Ohm's law still say?
The quotient $U/I$ exists for every component. The law says more: it is *constant*, independent of $U$. That is a statement about the material and follows from the fixed flight time. It does not hold for an incandescent lamp (Stage [4](reale-widerstande-werte-und-temperatur.html#stufe-4)).
:::

:::aufgabe Exercise 3 ★★ Resistance from geometry
<span class="anker" id="aufg-3"></span>

A supply line consists of an outgoing and a return conductor, each 20 m of copper with a cross section of $1.5\,\mathrm{mm^2}$.

<ol class="al">

<li>

Calculate its resistance and the voltage that drops across it at 16 A.

</li>

<li>

What cross section would aluminum need for the same resistance?

</li>

<li>

Prediction: A wire is drawn to twice its length while its volume stays the same. By what factor does $R$ change?

</li>

</ol>

:::loesung
(a) $R=\rho\cdot40\,\mathrm{m}/1.5\,\mathrm{mm^2}=0.453\,\Omega$. The drop is $0.453\,\Omega\cdot16\,\mathrm{A}=7.3$ V, 3.2 % of 230 V. (b) The same $R$ means the same $\rho/A$: $A_\mathrm{Al}=1.5\,\mathrm{mm^2}\cdot2.8/1.7=2.5\,\mathrm{mm^2}$. (c) Volume $L\,A$ constant: $L\to2L$ forces $A\to A/2$. So $R\to4R$.
:::
:::
