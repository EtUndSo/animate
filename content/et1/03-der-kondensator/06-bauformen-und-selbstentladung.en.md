---
title: Stage 5: Types of construction and self-discharge
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1130600
summary: 100 µF as a pair of plates in air would be 3.4 hectares in size.
tags: electrolyte, polarized, Self-healing, leakage current, insulation resistance
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
100 µF as a pair of plates in air would be 3.4 hectares in size. Real capacitors solve this through $A$, $d$ and $\varepsilon$. Each type of construction pays its own price for it.
:::

**The idea.** Equation [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) has three adjusting knobs, and all types of construction turn them (Fig. [5](#abb-5)).

<ul>

<li>

⁠**Film capacitor:** Two long metal strips, separated by plastic film or paper, are rolled into a winding. A large area thus fits in a small space.

</li>

<li>

⁠**Ceramic capacitor:** A ceramic with large $\varepsilon_\mathrm{r}$, often in many thin layers stacked on top of each other and connected in parallel (Stage [7](parallel-und-reihenschaltung.html#stufe-7)). The price: $\varepsilon_\mathrm{r}$ depends on voltage and temperature.

</li>

<li>

⁠**Electrolytic capacitor:** The electrode is roughened aluminum foil. This increases $A$. The dielectric is an oxide layer only a few tens of nanometers thick; this makes $d$ small. The counter electrode is a conductive liquid, the __electrolyte__, because only a liquid follows every recess. The price: The electrolytic capacitor is __polarized__; the oxide holds in only one direction. Connected the wrong way round, it degrades, current flows, the component heats up and can burst.

</li>

<li>

⁠**Supercap (also Goldcap):** On a porous carbon electrode with a huge inner surface, ions of the electrolyte accumulate at a distance of around 1 nm. This gives capacitances up to 100 F and more. The price: only a few volts, above which the electrolyte decomposes, and comparatively high leakage current.

</li>

</ul>

:::abbildung et1/k3bauform 5
Four routes to large capacitance, schematic cross sections, not to scale. Red and blue are the two electrodes; in the electrolytic capacitor, orange is the oxide above the aluminum and light blue the electrolyte. In the supercap the ions sit close to the carbon.
:::

| Type | Capacitance | Voltage | Size | Polarized | Self-healing |
|---|---|---|---|---|---|
| Paper, metallized paper | 100 pF to 50 µF | 125 V to 1 kV | large | no | metallized only |
| Plastic film | 2 pF to 200 µF | 50 V to 5 kV | medium to very small | no | metallized only |
| Ceramic | 0.5 pF to 100 µF | 6 V to 1 kV | small | no | no |
| Electrolytic | 0.5 µF to 10 mF | 3 V to 650 V | very small | yes | yes |
| Supercap | 0.1 F to over 100 F | a few volts | very small | yes | no |

The table summarizes the usual ranges. __Self-healing__ means: in a breakdown, the thin metal layer around the defect vaporizes, the short circuit disappears, and only a tiny area is lost. In the electrolytic capacitor the oxide re-forms at the defect.

**Self-discharge.** No insulator is perfect. The dielectric contains a few mobile charges, so a tiny current flows from plate to plate, the __leakage current__. In the equivalent circuit, an __insulation resistance__ $R_\mathrm{I}$ lies in parallel with the ideal capacitor. Ideally $R_\mathrm{I}\to\infty$ and a disconnected capacitor keeps its charge forever. In reality it gives it up at the pace $R_\mathrm{I}\,C$ (Stage [10](entladen-und-zeitkonstante.html#stufe-10)). With the resistivity $\rho$ of the material ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), $R_\mathrm{I}=\rho\,d/A$, and together with [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) it follows that

<span class="anker" id="gl-5-1"></span>
$$R_\mathrm{I}\,C=\rho\,\varepsilon. \tag{5.1}$$

$A$ and $d$ cancel: the self-discharge depends only on the material, not on the size of the component.

**Example.** Plastic film with $\rho\approx10^{16}\,\Omega\,$m and $\varepsilon_\mathrm{r}=2.2$ gives around two days. For a 100 µF electrolytic capacitor at 9 V, data sheets state at most around 9 µA of leakage current, that is, $R_\mathrm{I}\approx1\,\mathrm{M\Omega}$. That is 100 times more than $R$ in the RC circuit; the leakage current is 1 % of 0.9 mA and is neglected in the following stages.

⁠**Limiting case:** For $\rho\to\infty$, $R_\mathrm{I}\,C$ grows without limit; this is the ideal capacitor without self-discharge.

:::frage Why not always use the type with the largest capacitance?
Because every type has its price. Electrolytic capacitors are polarized and have large tolerances, supercaps withstand only a few volts. Where the voltage changes sign or the capacitance has to be exact, you use film or ceramic.
:::

:::aufgabe Exercise 6 ★ An electrolytic capacitor recalculated
<span class="anker" id="aufg-6"></span>

An electrolytic capacitor with 100 µF and 16 V has an oxide layer with $\varepsilon_\mathrm{r}=9$ and a thickness of 1.4 nm per volt.

<ol class="al">

<li>

How thick is the oxide, and what area is needed?

</li>

<li>

A strip of 3 cm by 20 cm fits in the can. By what factor must the roughening increase the surface?

</li>

<li>

Why would a smooth metal counter electrode not give this gain?

</li>

</ol>

:::loesung
(a) $d=16\cdot1.4\,\mathrm{nm}=22.4$ nm. $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot22.4\cdot10^{-9}\,\mathrm{m}}{9\cdot8.854\cdot10^{-12}\,\mathrm{F/m}}=281\,\mathrm{cm^2}$.

(b) The strip has 60 cm$^2$, so a factor of $281/60=4.7$ is needed.

(c) A solid counter electrode would touch only the peaks of the rough surface. The recesses would contribute nothing, and the distance there would be much larger than the oxide is thick. Only a liquid follows the surface at the distance $d$.
:::
:::
