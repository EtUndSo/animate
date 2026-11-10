---
title: Stage 2: Doping
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Semiconductors and Diodes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Chapter 9: Semiconductors and Diodes
order: 1190400
summary: Pure silicon has too few charge carriers, and their number depends strongly on temperature.
tags: valence electrons, covalent bond, donor, acceptor, n-region, p-region, majority carrier, minority carrier
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Pure silicon has too few charge carriers, and their number depends strongly on temperature. This stage fixes the type and number of carriers with foreign atoms.
:::

**The idea.** Silicon has four __valence electrons__ (electrons of the outermost shell). Each atom shares a pair of electrons with each of its four neighbors; this is the __covalent bond__. If an atom is replaced by phosphorus with five valence electrons, four bind and the fifth is left over (Fig. [3](#abb-3)). It is held to the phosphorus core by only 45 meV, which is 1.7 times $k_\mathrm BT$. Heat almost always frees it, it becomes a free electron in the CB, and a stationary $\mathrm P^+$ ion remains. Boron has only three valence electrons. One bond stays open, and a neighboring electron jumps in, likewise with 45 meV. The stationary $\mathrm B^-$ ion remains, and the hole wanders off.

:::abbildung et1/k9dotierung 3
Left: crystal in the plane; each double line is a bond. Right: bands at 300 K, not to scale. The level $W_\mathrm D$ of phosphorus lies 45 meV below the CB, the level $W_\mathrm A$ of boron 45 meV above the VB. Arrows: heat releases the electrons into the CB (top) and takes them out of the VB (bottom). The Fermi energy moves toward the band of the majority.
:::

:::definition Definition 2.1 (n-type and p-type doping)
<span class="anker" id="satz-2-1"></span>

A __donor__ (phosphorus) gives up an electron, an __acceptor__ (boron) takes one up. $N_\mathrm D$ donors per cm$^3$ create an __n-region__, $N_\mathrm A$ acceptors per cm$^3$ a __p-region__:

<span class="anker" id="gl-2-1"></span>
$$\text{n-region: }n\approx N_\mathrm D,\qquad\text{p-region: }p\approx N_\mathrm A,\qquad\text{everywhere: }n\,p=n_\mathrm i^2. \tag{2.1}$$
:::

⁠**How to read it:** $n$ and $p$ are the densities of electrons and holes in 1/cm$^3$. The more frequent kind is called the __majority carrier__, the rarer one the __minority carrier__. Typical values are $N=10^{15}$ to $10^{19}\,\mathrm{cm^{-3}}$. Doping does not charge the crystal: every free electron has a stationary $\mathrm P^+$ belonging to it. In the n-region the Fermi energy rises by $k_\mathrm BT\ln(n/n_\mathrm i)$ above the middle of the gap. **Validity:** room temperature (all foreign atoms ionized) and $N\gg n_\mathrm i$.

:::herleitung Why the product is constant
Heat generates pairs of electron and hole at a rate that depends only on $T$ and the material. Recombination requires the two to meet; its rate is $c\,n\,p$. In equilibrium both rates are equal, so $n\,p$ is constant. In pure silicon $n=p=n_\mathrm i$, so $n\,p=n_\mathrm i^2$. More electrons mean more recombination and fewer holes.
:::

::::beispiel
With $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ there is one foreign atom per $5\cdot10^{6}$ silicon atoms, and yet $n$ rises to a million times $n_\mathrm i$. The holes fall to $p=10^{20}/10^{16}=10^{4}\,\mathrm{cm^{-3}}$. Majority and minority are separated by the factor $10^{12}$. $W_\mathrm F$ rises by $25.85\,\mathrm{meV}\cdot\ln10^{6}=0.36$ eV.
::::

⁠**Limiting case:** For $N_\mathrm D\to0$, [(2.1)](#gl-2-1) again gives $n=p=n_\mathrm i$.

:::frage Is n-type silicon negatively charged and p-type silicon positively charged?
No, both are neutral. “n” and “p” name the sign of the mobile charges, not that of the piece. In the n-region, every free electron is matched by a stationary positive ion. Only at the pn junction do the two separate (Stage [3](die-raumladungszone.html#stufe-3)).
:::

:::aufgabe Exercise 2 ★★ Counting carriers
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Silicon receives $N_\mathrm D=5\cdot10^{15}\,\mathrm{cm^{-3}}$. How many silicon atoms are there per foreign atom? How large are $n$ and $p$?

</li>

<li>

How large are $n$ and $p$ at $N_\mathrm A=2\cdot10^{17}\,\mathrm{cm^{-3}}$?

</li>

<li>

Prediction: a piece receives equal numbers of donors and acceptors. What happens to the charge carriers?

</li>

</ol>

:::loesung
(a) $5\cdot10^{22}/5\cdot10^{15}=10^{7}$ atoms per foreign atom, $n=5\cdot10^{15}\,\mathrm{cm^{-3}}$, $p=10^{20}/5\cdot10^{15}=2\cdot10^{4}\,\mathrm{cm^{-3}}$. (b) $p=2\cdot10^{17}\,\mathrm{cm^{-3}}$, $n=500\,\mathrm{cm^{-3}}$. (c) Every donor electron falls onto an acceptor. No additional carriers arise, $n=p=n_\mathrm i$. The crystal behaves like pure silicon even though it is full of ions. This is called __compensation__.
:::
:::
