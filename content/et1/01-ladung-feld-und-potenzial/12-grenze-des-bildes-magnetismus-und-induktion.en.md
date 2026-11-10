---
title: Stage 10: Limit of the picture: magnetism and induction
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Charge, Field and Potential
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Chapter 1: Charge, Field and Potential
order: 1111200
summary: Everything so far held for charges at rest.
tags: magnetic field, coil, induction, electromagnetism, curl field, right-hand rule, conventional current direction, magnetic flux
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
Everything so far held for charges at rest. This stage shows what changes when charges move and magnetic fields change, and where path independence ends.
:::

**The idea.** For a long time, electricity and magnetism were regarded as separate fields. In 1820 Ørsted saw a compass needle deflect next to a current-carrying wire: moving charge produces a __magnetic field__ $H$. In 1831 Faraday reversed the idea: a magnet that he moved in a __coil__, a wire wound into turns, produced a voltage at its ends. This is called __induction__. In 1864 Maxwell combined everything into __electromagnetism__. The mechanism of induction is a new field: a changing magnetic field produces an electric field with closed lines, a __curl field__. On one round trip in it, a charge gains energy, and that ends the statement [(6.2)](arbeit-im-feld.html#gl-6-2).

:::abbildung et1/k1oersted 12
Left: cross section of a wire; the current $I$ flows into the page. The magnetic field $H$ runs in circles around the wire, and compass needles align their red tips with it. Right: a moving bar magnet changes the magnetic flux $\Phi$ through the coil. As long as it moves, the meter shows the voltage $u_\mathrm{ind}$.
:::

The direction of the magnetic field is given by the __right-hand rule__: the thumb points in the conventional current direction, the fingers in the direction of the field. The __conventional current direction__ runs from plus to minus; the electrons in the wire move the opposite way ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::satz Theorem 10.1 (Law of induction)
<span class="anker" id="satz-10-1"></span>

If the magnetic flux $\Phi$ through a coil with $N$ turns changes, the following voltage arises between its ends:

<span class="anker" id="gl-10-1"></span>
$$u_\mathrm{ind}(t)=-N\,\frac{\mathrm{d}\Phi}{\mathrm{d} t}. \tag{10.1}$$
:::

⁠**How to read it:** The __magnetic flux__ $\Phi$ measures how much magnetic field passes through the coil area, $[\Phi]=\mathrm{V\,s}=\mathrm{Wb}$ (weber). Small coils carry microwebers to milliwebers. Only the change counts, not the flux itself. The law is a measurement result: along one turn, the curl field supplies the voltage $|\mathrm{d}\Phi/\mathrm{d} t|$; the $N$ turns are in series and their voltages add. The lowercase letter $u$ stands for a time-dependent voltage. The minus sign says that a current driven by this voltage opposes the change in flux. **Validity:** All turns must enclose the same flux.

Faraday also showed induction without a magnet: he wound two coils onto a ring and connected a battery to one and a galvanometer (an early current meter) to the other. It deflected only when switching on and off, because only then does the flux change.

**Maxwell's equations in words.** The equations themselves need more mathematics, but their content fits into four sentences. The __flux density__ here is the measure of the density of the field lines. **Gauss's law for electric fields:** Charges are sources and sinks of the electric flux density. **Gauss's law for magnetism:** The magnetic flux density has no sources; its lines are closed. **Law of induction:** Changes of the magnetic flux in time lead to an electric curl field. **Ampère's law:** Currents and changes of the electric field in time lead to a magnetic curl field.

::::beispiel
The magnet in Fig. [12](#abb-12) changes the flux through the coil with $N=500$ uniformly by 0.2 mWb in 25 ms. The voltage is then constant: $|U_\mathrm{ind}|=500\cdot0.2\,\mathrm{mWb}/25\,\mathrm{ms}=4$ V. During this time, the loop integral of $\vec E$ around the flux is not zero, and the voltage between two points depends on which side of the flux the path runs.
::::

⁠**Limiting cases:** For constant flux, $u_\mathrm{ind}=0$; a magnet at rest produces no voltage. In most circuits, the changing fluxes sit almost entirely in coils. Between the components the field stays practically curl-free, which is why potentials and voltages remain the tool there.

:::frage Why can no potential be given in a curl field?
The potential of a location is the work per charge up to the reference point. In a curl field, that depends on the path. Two paths give two values, and the location would have no unique potential.
:::

:::aufgabe Exercise 11 ★ Induction
<span class="anker" id="aufg-11"></span>

A coil with 200 turns encloses a flux that increases uniformly by 0.5 mWb in 10 ms. (a) How large is the magnitude of the induced voltage? (b) The flux then stays constant. What voltage is present now?

:::loesung
(a) $|U_\mathrm{ind}|=200\cdot0.5\,\mathrm{mWb}/10\,\mathrm{ms}=10$ V. (b) Zero, because $\mathrm{d}\Phi/\mathrm{d} t=0$.
:::
:::
