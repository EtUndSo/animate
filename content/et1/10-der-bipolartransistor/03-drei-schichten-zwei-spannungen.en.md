---
title: Stage 1: Three layers, two voltages
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200300
summary: A diode has two terminals and one characteristic curve.
tags: npn transistor, BE diode, CB diode, pnp transistor, circuit symbol, collector current, base current, emitter current
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A diode has two terminals and one characteristic curve. The transistor has three terminals. This stage explains its structure and counts how many quantities are free.
:::

**The idea.** An __npn transistor__ consists of three regions of the same semiconductor: n-doped emitter, p-doped base, n-doped collector (Fig. [1](#abb-1)). The emitter is the most heavily doped, so that it can give off many electrons. The collector is the most lightly doped, so that its space-charge region becomes wide and withstands high voltages. The base lies between them and is very narrow, around 1 µ m. This creates two pn junctions that share the base: the __BE diode__ and the __CB diode__. In normal operation, the BE diode conducts and the CB diode blocks. Swapping n and p gives the __pnp transistor__ (Stage [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)). In the __circuit symbol__, the symbol in the schematic, the emitter is the terminal with the arrow. The arrow shows the direction of the conventional current.

:::abbildung et1/k10aufbau 1
Left: npn transistor as a layer sequence and as a circuit symbol with all reference arrows. Right: pnp transistor with the reversed layer sequence. There the emitter arrow points into the component, and all currents and voltages reverse.
:::

:::definition Definition 1.1 (Currents and voltages at the npn transistor)
<span class="anker" id="satz-1-1"></span>

$I_\mathrm{B}$ and $I_\mathrm{C}$ are counted into the component, $I_\mathrm{E}$ out of it. Voltages are potential differences, and the first index is the plus pole: $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, $U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E}$, $U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$. It always holds that

<span class="anker" id="gl-1-1"></span>
$$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C},\qquad U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}. \tag{1.1}$$
:::

⁠**How to read it:** $I_\mathrm{C}$ is the __collector current__, from microamperes to amperes depending on the type. $I_\mathrm{B}$ is the much smaller __base current__, $I_\mathrm{E}$ the __emitter current__. $U_\mathrm{BE}$ is across the BE diode, around 0.6 V. $U_\mathrm{CE}$ ranges from around 0.2 V up to several tens of volts. $U_\mathrm{CB}$ is the reverse voltage of the CB diode. **Validity:** the node and mesh rules hold in every operating state.

:::herleitung How many quantities are free
A component with $n$ terminals has $n$ currents. It stores no charge, so the node rule ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) removes one current. It has $n$ potentials, but only differences count, so $n-1$ voltages remain. The diode ($n=2$) has one voltage, one current and one curve. The transistor ($n=3$) has two voltages and two currents. Its interior links them through two equations,

$$I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE}),\qquad I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE}).$$

So it is a two-port ([Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) whose two ports share the emitter.
:::

**Example.** In the reference model, $\varphi_\mathrm{E}=0$, $\varphi_\mathrm{B}=0.6$ V, $\varphi_\mathrm{C}=6$ V. This gives $U_\mathrm{BE}=0.6$ V, $U_\mathrm{CE}=6$ V and $U_\mathrm{CB}=5.4$ V. The BE diode conducts because its p side is higher. The CB diode blocks because its n side is 5.4 V higher. From $I_\mathrm{C}=2$ mA and $I_\mathrm{B}=10$ µ A follows $I_\mathrm{E}=2.01$ mA. **Limiting case:** for $U_\mathrm{CB}=0$, $U_\mathrm{CE}=U_\mathrm{BE}$. This is where normal operation ends.

:::frage Can I solder a transistor together from two diodes?
No. The equivalent picture of two diodes only shows the polarity of the boundaries. In two separate diodes, every electron recombines long before it reaches the second depletion layer, and the blocking diode stays blocked. The transistor effect arises only because the two boundaries lie closer together than the distance an electron survives in the p region.
:::

:::aufgabe Exercise 1 ★ From potential to voltage
<span class="anker" id="aufg-1"></span>

Measured against ground are $\varphi_\mathrm{E}=1.2$ V, $\varphi_\mathrm{B}=1.85$ V and $\varphi_\mathrm{C}=7$ V, as well as $I_\mathrm{B}=15$ µ A and $I_\mathrm{C}=3$ mA. (a) Determine $U_\mathrm{BE}$, $U_\mathrm{CE}$, $U_\mathrm{CB}$ and check [(1.1)](#gl-1-1). (b) How large is $I_\mathrm{E}$? (c) To what value must $\varphi_\mathrm{C}$ fall so that $U_\mathrm{CB}=0$?

:::loesung
(a) $U_\mathrm{BE}=0.65$ V, $U_\mathrm{CE}=5.8$ V, $U_\mathrm{CB}=5.15$ V. Check: $5.15\,\mathrm{V}+0.65\,\mathrm{V}=5.8$ V. (b) $I_\mathrm{E}=3.015$ mA. (c) $U_\mathrm{CB}=0$ means $\varphi_\mathrm{C}=\varphi_\mathrm{B}=1.85$ V.
:::
:::
