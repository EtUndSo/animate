---
title: Stage 3: Star and delta
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Sources and Equivalent Sources
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Chapter 5: Sources and Equivalent Sources
order: 1150500
summary: An unbalanced bridge has neither groups nor symmetry.
tags: delta, star, adjacent elements, two-ports, \pi network, T network, attenuators
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
An unbalanced bridge has neither groups nor symmetry. The star-delta transformation exchanges a piece of the network so that groups arise.
:::

**The idea.** A __delta__ is three resistors between three terminals. A __star__ is three resistors from three terminals to a common inner node, the star point. Both have three terminals and three numbers. With suitable values they cannot be told apart from outside. The exchange helps because the star point is a new node at which each star resistor lies in series with the neighbor behind it.

:::satz Theorem 3.1 (Star-delta transformation)
<span class="anker" id="satz-3-1"></span>

Terminals 1, 2, 3, star point 0. From delta to star:

<span class="anker" id="gl-3-1"></span>
$$R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}},\qquad R_{20}=\frac{R_{12}R_{23}}{R_{12}+R_{23}+R_{31}},\qquad R_{30}=\frac{R_{23}R_{31}}{R_{12}+R_{23}+R_{31}}. \tag{3.1}$$

From star to delta, with the conductances $G_{ij}=1/R_{ij}$:

<span class="anker" id="gl-3-2"></span>
$$G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}},\qquad G_{23}=\frac{G_{20}G_{30}}{G_{10}+G_{20}+G_{30}},\qquad G_{31}=\frac{G_{30}G_{10}}{G_{10}+G_{20}+G_{30}}. \tag{3.2}$$
:::

⁠**How to read it:** $R_{10}$ leads from terminal 1 to the star point, $R_{12}$ from terminal 1 to terminal 2. The __adjacent elements__ are the two elements that adjoin: for $R_{10}$ the delta sides at terminal 1, for $G_{12}$ the star branches at terminals 1 and 2. As a rule to remember: star resistance = product of the adjacent resistances divided by the perimeter resistance of the delta. Delta conductance = product of the adjacent conductances divided by the sum of the star conductances. Equivalent to [(3.2)](#gl-3-2) is $R_{12}=R_{10}+R_{20}+R_{10}R_{20}/R_{30}$ with cyclically permuted indices. **Validity:** The equality holds for any external circuit, but only at the three terminals. The star point is not a node in the original, and the currents in the resistors themselves differ.

:::herleitung Star to delta, then invert
In the star, the node rule at the star point reads $G_{10}(\varphi_1-\varphi_0)+G_{20}(\varphi_2-\varphi_0)+G_{30}(\varphi_3-\varphi_0)=0$. With $S=G_{10}+G_{20}+G_{30}$ it follows that $\varphi_0=(G_{10}\varphi_1+G_{20}\varphi_2+G_{30}\varphi_3)/S$. The current into terminal 1 is thus

$$I_1=G_{10}(\varphi_1-\varphi_0)=\frac{G_{10}G_{20}}{S}(\varphi_1-\varphi_2)+\frac{G_{10}G_{30}}{S}(\varphi_1-\varphi_3).$$

In the delta, $I_1=G_{12}(\varphi_1-\varphi_2)+G_{31}(\varphi_1-\varphi_3)$. Comparing the two gives [(3.2)](#gl-3-2), for arbitrary potentials. Terminal 2 gives $G_{23}$ in the same way.

For the inversion, let $H=R_{10}R_{20}+R_{20}R_{30}+R_{30}R_{10}$. Then $S=H/(R_{10}R_{20}R_{30})$, and [(3.2)](#gl-3-2) becomes $R_{12}=H/R_{30}$, $R_{23}=H/R_{10}$, $R_{31}=H/R_{20}$. From these follow $R_{12}R_{31}=H^2/(R_{20}R_{30})$ and $R_{12}+R_{23}+R_{31}=H^2/(R_{10}R_{20}R_{30})$. The quotient is $R_{10}$, which is [(3.1)](#gl-3-1).
:::

:::abbildung et1/k5bruecke 4
Left, an unbalanced bridge with the delta 1-2-3 (blue). Right, the delta has been replaced by a star (red). Now 4 $\Omega$ and 20 $\Omega$ are in series, as are 8 $\Omega$ and 16 $\Omega$.
:::

::::beispiel
In Fig. [4](#abb-4), $R_{12}=10\,\Omega$, $R_{23}=R_{31}=20\,\Omega$, and the perimeter is 50 $\Omega$. From [(3.1)](#gl-3-1) follow $R_{10}=4\,\Omega$, $R_{20}=4\,\Omega$, $R_{30}=8\,\Omega$. The bridge breaks down into groups:

$$R_\mathrm{AB}=4\,\Omega+(4\,\Omega+20\,\Omega)\parallel(8\,\Omega+16\,\Omega)=4\,\Omega+12\,\Omega=16\,\Omega.$$
::::

⁠**Check** at terminals 1, 2 with terminal 3 open: the star has $4+4=8\,\Omega$, the delta $10\,\Omega\parallel40\,\Omega=8\,\Omega$. **Limiting cases:** Three equal delta resistors give a star with one third of the value. For $R_{12}\to0$, $R_{10}$ and $R_{20}$ go to zero, and $R_{30}$ becomes $R_{23}\parallel R_{31}$, which is exactly what the short-circuited delta is.

**$\pi$ and T.** For __two-ports__ ([Chapter 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)), delta and star are drawn with an input on the left and an output on the right. The delta is then called a __$\pi$ network__, the star a __T network__. The formulas and rules stay the same. In communications engineering this is how __attenuators__ are built, which weaken a signal by a fixed factor and present the same input resistance at both terminal pairs (power matching, [Chapter 7](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). Filters made of coils and capacitors can also be built in either form.

:::frage Which delta should I convert?
Any one whose conversion creates groups. In a bridge the lower delta works too, or even a star converted into a delta. The result is always the same.
:::

:::aufgabe Exercise 4 ★★ There and back
<span class="anker" id="aufg-4"></span>

(a) Three resistors of 12 $\Omega$ each form a delta. How large are the star resistors? (b) In a bridge, let the three upper resistors (delta A, C, D) be 6 $\Omega$ each; from C, 1 $\Omega$ and from D, 4 $\Omega$ lead to B. Calculate $R_\mathrm{AB}$. (c) Convert the star $R_{10}=5\,\Omega$, $R_{20}=R_{30}=10\,\Omega$ into a delta, once with [(3.2)](#gl-3-2) and once with the resistance form.

:::loesung
(a) Perimeter 36 $\Omega$, $R_\mathrm{star}=\frac{12\cdot12}{36}\,\Omega=4\,\Omega$, one third of the delta value.

(b) The delta becomes three star resistors of 2 $\Omega$ each. Then $R_\mathrm{AB}=2\,\Omega+(2\,\Omega+1\,\Omega)\parallel(2\,\Omega+4\,\Omega)=2\,\Omega+3\,\Omega\parallel6\,\Omega=4\,\Omega$.

(c) Conductances 0.2 S, 0.1 S, 0.1 S, sum 0.4 S. $G_{12}=\frac{0.2\cdot0.1}{0.4}$ S $=0.05$ S, $G_{23}=0.025$ S, $G_{31}=0.05$ S. These are $R_{12}=20\,\Omega$, $R_{23}=40\,\Omega$, $R_{31}=20\,\Omega$. Resistance form: $R_{12}=5+10+\frac{5\cdot10}{10}=20\,\Omega$, $R_{23}=10+10+\frac{10\cdot10}{5}=40\,\Omega$, $R_{31}=10+5+\frac{10\cdot5}{10}=20\,\Omega$.
:::
:::
