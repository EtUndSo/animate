---
title: Stage 1: Why silicon hardly conducts
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Semiconductors and Diodes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Chapter 9: Semiconductors and Diodes
order: 1190300
summary: Metal conducts, glass does not, pure silicon hardly at all.
tags: energy levels, band, forbidden zone, valence band, conduction band, band gap, Fermi energy, metal
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Metal conducts, glass does not, pure silicon hardly at all. The difference lies in the number of mobile electrons. This stage explains it from the allowed energies in the crystal.
:::

**The idea.** In a single atom, electrons have only certain energies, the __energy levels__. In a crystal (regular lattice of atoms) the shells overlap, and the electrons belong to the whole crystal. No two electrons may occupy the same state. That is why each level splits into as many closely spaced levels as the crystal has atoms. This creates a __band__ of allowed energies. Between the bands lies the __forbidden zone__: there are no states there. A field can accelerate an electron only if a free state lies just above it. So a full band does not conduct, no matter how many electrons it contains.

:::abbildung et1/k9baender 2
Band model, not to scale; $W$ is the energy of an electron. In the metal, the top band is only partly filled. In the semiconductor, heat lifts a few electrons over the small gap and leaves holes behind. In the insulator, the gap is too large.
:::

:::definition Definition 1.1 (Bands)
<span class="anker" id="satz-1-1"></span>

The __valence band__ (VB) is the top band that is fully occupied at $T=0$. The __conduction band__ (CB) lies above it and is empty at $T=0$. The __band gap__ $W_\mathrm g$ is the smallest energy that lifts an electron from the VB into the CB. The __Fermi energy__ $W_\mathrm F$ separates occupied from empty states at $T=0$. At $T>0$ it is the energy at which a state would be occupied half of the time; it may lie in the gap even though there is no state there.
:::

⁠**How to read it:** Silicon has $W_\mathrm g=1.12$ eV, germanium 0.67 eV, diamond 5.5 eV. **Three cases:** In a __metal__, the top occupied band is only partly filled, free states lie directly above the electrons, and it conducts at every temperature. In an __insulator__, $W_\mathrm g$ is so large that no electron gets across. A semiconductor is an insulator with a small gap: at $T=0$ it insulates; when excited by heat, light or strong fields, electrons get into the CB.

An electron that moves into the CB leaves a free place in the VB. A neighboring electron moves in, and the place wanders. The __hole__ (defect electron) behaves like a mobile particle with the charge $+e$. Both count as charge carriers: electrons in the CB and holes in the VB. If an electron falls back into a hole, both disappear; this is called __recombination__.

:::satz Theorem 1.2 (Fraction of electrons in the conduction band)
<span class="anker" id="satz-1-2"></span>

In a pure semiconductor, $W_\mathrm F$ lies in the middle of the gap. For the states at the edge of the CB, this gives

<span class="anker" id="gl-1-1"></span>
$$\text{occupation}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}. \tag{1.1}$$
:::

:::herleitung Why half the gap counts
Every electron in the CB leaves a hole in the VB, so the numbers of both are equal. With similar numbers of states in both bands, this is possible only if $W_\mathrm F$ is the same distance $W_\mathrm g/2$ from both band edges. In [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1) the energy above $W_\mathrm F$ counts, so $W=W_\mathrm g/2$.
:::

::::beispiel
At 300 K, $W_\mathrm g/(k_\mathrm BT)=43.3$ and $\mathrm{e}^{-21.7}=3.9\cdot10^{-10}$. The measured density of free electrons is $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$. That is one per $5\cdot10^{12}$ atoms, because silicon has $5\cdot10^{22}$ atoms per cm$^3$. Copper has $8.5\cdot10^{12}$ times more free electrons ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).
::::

⁠**Limiting cases:** For $T\to0$, [(1.1)](#gl-1-1) goes to zero: silicon insulates. Every 10 K of warming doubles the fraction. That is why the resistance of a semiconductor falls with temperature ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::frage Why does a full band not conduct even though it is full of electrons?
Because current needs motion in a preferred direction. For that, an electron would have to move into a state with slightly more energy. In a full band, every such state is occupied. Two electrons could only swap places, and that changes nothing. The first hole makes the band conductive.
:::

:::aufgabe Exercise 1 ★ Comparing three materials
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Give $W_\mathrm g=1.12$ eV in joules. What multiple of $k_\mathrm BT$ is that at 300 K?

</li>

<li>

Calculate [(1.1)](#gl-1-1) for silicon, germanium and diamond. Which pure material conducts best?

</li>

<li>

Silicon warms from 300 K to 330 K. By what factor does the fraction grow?

</li>

</ol>

:::loesung
(a) $1.12\cdot1.602\cdot10^{-19}\,\mathrm{J}=1.79\cdot10^{-19}$ J, which is $1.12\,\mathrm{eV}/25.85\,\mathrm{meV}=43.3$ times $k_\mathrm BT$. (b) Silicon $3.9\cdot10^{-10}$, germanium $2.4\cdot10^{-6}$, diamond $6.3\cdot10^{-47}$. Germanium conducts best, with around 6000 times the occupation of silicon; diamond has practically no free electrons. (c) With $U_T=28.44$ mV at 330 K the fraction is $2.8\cdot10^{-9}$, 7.2 times as much.
:::
:::
