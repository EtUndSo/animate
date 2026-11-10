---
title: Stage 4: Parallel-plate capacitor and dielectric
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Capacitor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Chapter 3: The Capacitor
order: 1130500
summary: Where does the value of C come from?
tags: polarization, bound charge, permittivity, relative permittivity, breakdown, displacement current
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Where does the value of $C$ come from? For two flat plates, it follows from the area, the separation and the material between them. This stage derives the formula and explains what the insulator does.
:::

**The idea.** At fixed voltage $U$ and fixed separation $d$, the field $E=U/d$ is fixed ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). The field says how dense the field lines are, and every line begins on a charge. So the charge per area is fixed. Twice the area therefore means twice the charge. Half the separation means twice the field and thus twice the charge per area.

The insulator increases the capacitance further. Its electrons stay with their atoms, but in every atom or molecule the field shifts the positive against the negative charge by a small amount. This shift is called __polarization__. In the interior, neighboring ends cancel; at the surfaces a __bound charge__ remains, negative opposite the plus plate (Fig. [4](#abb-4) right). Some of the field lines end on it, and the field between the plates would become weaker. But the battery holds $U$ and thus $E$ fixed, so it pushes in more charge until the field is right again. At the same voltage, more charge sits on the plates.

:::abbildung et1/k3platte 4
Same voltage, same separation, same field. Left, air: Every field line runs from plate to plate; $A$ is the area of one plate. Right, a dielectric with $\varepsilon_\mathrm{r}=2$: The molecules are aligned, inside the ends cancel, and bound charge remains at the edge. Half of the lines end there. That is why the plate carries twice the charge.
:::

:::satz Theorem 4.1 (Parallel-plate capacitor)
<span class="anker" id="satz-4-1"></span>

For two flat plates of area $A$ at separation $d$, with a dielectric filling the space,

<span class="anker" id="gl-4-1"></span>
$$C=\varepsilon\,\frac{A}{d},\qquad\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r},\qquad\varepsilon_0=8.854\cdot10^{-12}\,\frac{\mathrm{A\,s}}{\mathrm{V\,m}}. \tag{4.1}$$
:::

⁠**How to read it:** $C$ rises with larger area $A$ (in m$^2$; the italic $A$ is not the plate A from Stage [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)), smaller separation $d$ (in m) and larger $\varepsilon$. $\varepsilon_0$ is the electric constant from [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). $\varepsilon$ is called the __permittivity__; the pure number $\varepsilon_\mathrm{r}$ is called the __relative permittivity__ and indicates by what factor the material increases the capacitance compared with vacuum. Air counts with the value 1; the error is 0.06 %. **Validity:** $d$ must be small compared with the plate width. Otherwise the fringing field at the edge counts ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)); in the pair of plates with 3 mm separation and 10 cm width it increases $C$ by around 10 %. For rough estimates [(4.1)](#gl-4-1) is sufficient.

| Material | Air | Paper | Mica | Porcelain | Water | Capacitor ceramic |
|---|---|---|---|---|---|---|
| $\varepsilon_\mathrm{r}$ | 1 | $\approx2$ | $\approx5$ | $\approx6$ | $\approx81$ | 60 to 3000 |

:::herleitung From the field-line picture to the formula
A point charge produces the field $E=\frac{Q}{4\pi\varepsilon_0r^2}=\frac{Q}{\varepsilon_0\cdot4\pi r^2}$. The denominator contains the spherical surface through which all its field lines run. So, according to [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html): The field strength is the charge, divided by $\varepsilon_0$ and by the area that its lines pass through uniformly. In the pair of plates, all lines of the charge $Q$ run in parallel through the area $A$:

$$E=\frac{Q}{\varepsilon_0\,A},\qquad U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}\quad\Longrightarrow\quad C=\frac QU=\varepsilon_0\,\frac Ad.$$

With a dielectric, lines end on the bound charge $Q_\mathrm{g}$, and only the share $Q-Q_\mathrm{g}$ still runs through the space. In most insulators this share is a fixed fraction of $Q$. One writes $Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r}$, which gives $E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$ and thus [(4.1)](#gl-4-1).
:::

::::beispiel
The pair of plates has $C=8.854\cdot10^{-12}\,\mathrm{F/m}\cdot0.01\,\mathrm{m^2}/0.003\,\mathrm{m}=29.5$ pF. With ceramic of $\varepsilon_\mathrm{r}=1000$ it would be 29.5 nF. For 100 µF at 3 mm of air, you would need the area $A=C\,d/\varepsilon_0=33\,900\,\mathrm{m^2}$, which is 3.4 hectares. That is why real capacitors work with thin layers (Stage [5](bauformen-und-selbstentladung.html#stufe-5)).
::::

⁠**Check:** The unit is right: $\frac{\mathrm{A\,s}}{\mathrm{V\,m}}\cdot\frac{\mathrm{m^2}}{\mathrm{m}}=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$. **Limiting case:** For $d\to0$, $C$ would grow without limit. This is prevented by __breakdown__: at $E_\mathrm{max}$ the dielectric becomes conductive, in air at 3 MV/m ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Thin layers therefore need a solid material, and every capacitor has a maximum voltage $U_\mathrm{max}=E_\mathrm{max}\,d$.

:::zusatz Displacement current
With $u=E\,d$ and [(4.1)](#gl-4-1), [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) becomes $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$. No charge flows in the gap, but the field changes there, and this change has exactly the size of the current in the wires. Maxwell called it the __displacement current__. In the gap it produces the same magnetic field as the current in the wire (Ampère's law, [Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). For the magnetic field, then, the circuit is closed.
:::

:::frage Water has $\varepsilon_\mathrm{r}=81$. Why does nobody build water capacitors?
Because in practice water conducts: dissolved ions carry current between the plates, and the capacitor immediately discharges itself. A dielectric has to do two things: polarize and insulate. The high $\varepsilon_\mathrm{r}$ comes from the water molecules, which have separated centers of charge of their own accord and align in the field.
:::

:::aufgabe Exercise 4 ★★ Area and maximum voltage
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

How large must $A$ be for 100 µF if a 10 µm thick film with $\varepsilon_\mathrm{r}=3$ separates the plates instead of 3 mm of air?

</li>

<li>

How long would a 5 cm wide strip of this area be?

</li>

<li>

Up to what voltage does the pair of plates hold in air?

</li>

</ol>

:::loesung
(a) $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot10^{-5}\,\mathrm{m}}{3\cdot8.854\cdot10^{-12}\,\mathrm{F/m}}=37.6\,\mathrm{m^2}$.

(b) $37.6\,\mathrm{m^2}/0.05\,\mathrm{m}=753$ m. Real windings are shorter because they use thinner film and both sides of each electrode.

(c) $U_\mathrm{max}=E_\mathrm{max}\,d=3\,\mathrm{MV/m}\cdot3\,\mathrm{mm}=9$ kV.
:::
:::

:::aufgabe Exercise 5 ★★ Inserting a dielectric
<span class="anker" id="aufg-5"></span>

The pair of plates is connected to 9 V. Now the space is filled with a material with $\varepsilon_\mathrm{r}=4$. First predict what stays the same, and then calculate.

<ol class="al">

<li>

The battery stays connected. How large are $C$, $U$, $Q$ and $E$?

</li>

<li>

The battery was disconnected beforehand. How large are $C$, $U$, $Q$ and $E$ now?

</li>

<li>

Why do the two cases differ, even though $C$ is the same?

</li>

</ol>

:::loesung
In both cases $C=4\cdot29.5\,\mathrm{pF}=118$ pF.

(a) The battery holds $U=9$ V fixed. Then $E=U/d=3$ kV/m remains, and $Q=C\,U=1.06$ nC. The battery pushes in the additional charge.

(b) Without the battery no charge can flow in, so $Q=266$ pC remains. Then $U=Q/C=2.25$ V and $E=U/d=750$ V/m.

(c) A different quantity is held fixed in each case: the voltage with the battery, the charge without it. The dielectric changes $C$; the other quantity settles according to $Q=CU$.
:::
:::
