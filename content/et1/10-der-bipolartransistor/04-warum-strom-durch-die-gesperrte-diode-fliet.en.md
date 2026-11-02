---
title: Stage 2: Why current flows through the blocking diode
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200400
summary: The CB diode blocks, and yet milliamperes flow through it.
tags: injection, diffusion length, transfer current, active region
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
The CB diode blocks, and yet milliamperes flow through it. This stage follows the path of the electrons and shows why only a small base current is needed.
:::

**The idea.** A blocking diode does not block because its boundary is impermeable. It blocks because almost no free electrons are available on the p side. The field of the space-charge region drives every electron that reaches the boundary from the p side across into the n region. For such electrons the boundary is a steep drop (Fig. [2](#abb-2), bottom). The transistor supplies exactly these missing electrons, in four steps:

<ol>

<li>

⁠**Injection.** $U_\mathrm{BE}$ lowers the barrier at the BE boundary. Electrons from the emitter enter the base. This introduction is called __injection__. The electron density at the emitter edge of the base grows with $\mathrm{e}^{U_\mathrm{BE}/U_T}$.

</li>

<li>

⁠**Crossing.** In the p-type base, electrons are a minority among many holes. They diffuse to the collector edge, where their density is almost zero. The base is much narrower than the __diffusion length__, the mean distance until recombination, several tens of µ m. That is why almost all of them get through.

</li>

<li>

⁠**Sweeping out.** At the collector edge, the field of the CB boundary catches every arriving electron and pulls it into the collector. How large $U_\mathrm{CB}$ is hardly matters; the field always collects them all. That is why $I_\mathrm{C}$ hardly depends on $U_\mathrm{CE}$.

</li>

<li>

⁠**Replenishing.** Two small losses remain: holes from the base pass into the emitter, and some electrons recombine in the base. Both use up holes. The base terminal must replace them. This replacement is the base current. It stays small because the emitter is much more heavily doped than the base and because the base is so narrow.

</li>

</ol>

The electrons run from the emitter to the collector. The conventional current $I_\mathrm{C}$ is counted the opposite way, from the collector to the emitter ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::abbildung et1/k10basis 2
Top: path of the electrons at the operating point. The emitter current of 2.01 mA divides into 2 mA to the collector and 10 µ A to the base. Bottom: energy of an electron over position, schematic. $U_\mathrm{BE}$ lowers the small step at the emitter, $U_\mathrm{CB}$ deepens the steep drop to the collector.
:::

:::satz Theorem 2.1 (Currents in normal operation)
<span class="anker" id="satz-2-1"></span>

If the BE diode conducts with $U_\mathrm{BE}\gg U_T$ and the collector lies above the base, then

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T},\qquad I_\mathrm{B}=\frac{I_\mathrm{C}}{B},\qquad I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}. \tag{2.1}$$
:::

⁠**How to read it:** $I_\mathrm{C}$ is also called the __transfer current__, because it is transferred through the base. $I_\mathrm{S}$ in A is tiny, here $1.9\cdot10^{-13}$ A, and depends on area and doping. $U_T=k_\mathrm{B}T/e$ is around 26 mV at 300 K. $B$ has no unit and lies between 10 and 1000. The value depends on doping and geometry and scatters: specimens of one type often differ by a factor of 2. **Validity:** the __active region__ (Stage [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)), at currents that are not too large.

:::herleitung Why $I_\mathrm{B}$ is proportional to $I_\mathrm{C}$
Electrons and holes cross the same barrier. The electron density at the emitter edge of the base and the hole density at the base edge of the emitter both grow with $\mathrm{e}^{U_\mathrm{BE}/U_T}$. The collector current is proportional to the first density, as is the recombination in the base, and the hole current is proportional to the second. All parts carry the same factor, so their ratio $B=I_\mathrm{C}/I_\mathrm{B}$ does not depend on $U_\mathrm{BE}$.
:::

**Who controls?** Physically, $U_\mathrm{BE}$ controls, because only the voltage lowers the barrier. The base current is the price for it. In circuits one nevertheless often calculates with $I_\mathrm{B}$: because of $I_\mathrm{C}=B\,I_\mathrm{B}$, the transistor behaves like a current-controlled current source (CCCS, [Part 6](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Both views describe the same proportionality. Control via $U_\mathrm{BE}$ explains the exponential law; the view via $I_\mathrm{B}$ is convenient when a resistor sets the base current.

**Example.** $U_\mathrm{BE}=0.6$ V gives $I_\mathrm{C}=1.9\cdot10^{-13}\,\mathrm{A}\cdot\mathrm{e}^{23.08}=2.00$ mA, $I_\mathrm{B}=10$ µ A, $I_\mathrm{E}=2.01$ mA. That is $1.25\cdot10^{16}$ electrons per second in the collector, and 99.5 % of the emitter current arrives there. The exponential function is sensitive: $+18$ mV doubles the current ($U_T\ln2$), $+60$ mV multiplies it by ten ($U_T\ln10$), $+1$ mV brings $+3.9$ %. **Limiting cases:** at $U_\mathrm{BE}=0.4$ V only 0.9 µ A flow, and the transistor is practically off. For $B\to\infty$, $I_\mathrm{B}$ vanishes and $I_\mathrm{E}=I_\mathrm{C}$.

:::analogie
A large water channel is closed by a flap. A thin jet from a side channel pushes the flap open. Without the control jet nothing flows, the stronger it is the more water passes, and at the bottom the two flows unite. The picture holds for three statements: small controls large, without control the transistor blocks, $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$. It does not hold for the mechanism: in the transistor nothing moves a flap, the voltage lowers a barrier, and the relationship is exponential.
:::

:::frage Where does the additional power at the output come from?
From the supply $U_\mathrm{CC}$. The collector current runs through the entire output circuit, and the source delivers $U_\mathrm{CC}I_\mathrm{C}$ in the process. The input signal pays only $U_\mathrm{BE}I_\mathrm{B}$ and thereby decides how much the source delivers.
:::

:::aufgabe Exercise 2 ★★ Counting electrons
<span class="anker" id="aufg-2"></span>

Calculate with transistor T. (a) How many electrons reach the collector per second at $I_\mathrm{C}=2$ mA? (b) Which $U_\mathrm{BE}$ belong to 5 mA and to 0.5 mA? How large is the difference, and why does it not depend on $I_\mathrm{S}$? (c) Another specimen has $B=50$. What fraction of the emitter current flows out through the base?

:::loesung
(a) $2\,\mathrm{mA}/e=1.25\cdot10^{16}$ per second. (b) $U_\mathrm{BE}=U_T\ln(I_\mathrm{C}/I_\mathrm{S})$ gives 0.624 V and 0.564 V. The difference is $U_T\ln10=59.9$ mV. In the difference of two logarithms, $I_\mathrm{S}$ cancels out. (c) $I_\mathrm{B}/I_\mathrm{E}=1/(1+B)=1/51=2.0$ %.
:::
:::
