---
title: Stage 4: Why the current grows exponentially
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Semiconductors and Diodes
order: 1190600
summary: The barrier is in place.
tags: reverse saturation current, thermal voltage, decade, bulk resistance
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The barrier is in place. This stage applies an external voltage and shows why the current grows exponentially in one direction and stays almost zero in the other.
:::

**The idea.** An external voltage $U$ between the p-side (anode) and the n-side (cathode) drops almost entirely across the region, because only there are charge carriers missing. The neutral regions conduct well. So the barrier changes to $W_\mathrm B=e(U_\mathrm{D0}-U)$ (Fig. [5](#abb-5)). Two electron currents run across the region:

<ul>

<li>

⁠**Uphill:** majority electrons of the n-region. Only the fraction $\mathrm{e}^{-W_\mathrm B/(k_\mathrm BT)}$ gets over the barrier. Every $k_\mathrm BT$ less barrier increases it by a factor of 2.718.

</li>

<li>

⁠**Downhill:** minority electrons of the p-region that reach the edge of the region. For them the potential step is a slope, and they always get through. Their number does not depend on the barrier.

</li>

</ul>

The same applies to holes in the opposite direction. Without voltage both currents are equally large, so nothing flows.

:::abbildung et1/k9barriere 5
Energy of an electron versus position; dots: electrons, each higher row contains fewer (schematic distribution, the real ratios are far more extreme). Red: electrons above the barrier $W_\mathrm B$, which wander to the left. The blue arrow at top left is the minority current downhill, always the same size. At $U=0$ the two currents cancel.
:::

:::satz Theorem 4.1 (Shockley equation)
<span class="anker" id="satz-4-1"></span>

For the ideal diode with $U$ from anode to cathode and $I$ from anode to cathode,

<span class="anker" id="gl-4-1"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr),\qquad U_T=\frac{k_\mathrm BT}{e}. \tag{4.1}$$
:::

⁠**How to read it:** $I_\mathrm S$ is the __reverse saturation current__ (reverse current for short), $10^{-15}$ to $10^{-9}$ A depending on area and doping. The __thermal voltage__ $U_T$ is the thermal energy $k_\mathrm BT$ in volts, divided by $e$, so 25.85 mV at 300 K. Important: $k_\mathrm BT$ alone is an energy; only $k_\mathrm BT/e$ is a voltage. The factor of 10 (one __decade__) costs $U_T\ln10=59.5$ mV, so about 60 mV. **Validity:** [(4.1)](#gl-4-1) holds for $U<U_\mathrm{D0}$ and without breakdown (Stage [5](kennlinie-durchbruch-und-spezialdioden.html#stufe-5)). In the forward direction, $I\approx I_\mathrm S\mathrm{e}^{U/U_T}$ is enough.

:::herleitung From the barrier to the characteristic curve
<ol>

<li>

Uphill: the current is proportional to the fraction above the barrier, $I_\text{up}=c\,\mathrm{e}^{-(U_\mathrm{D0}-U)/U_T}=I_0\,\mathrm{e}^{U/U_T}$. Here $I_0=c\,\mathrm{e}^{-U_\mathrm{D0}/U_T}$ collects everything that does not depend on $U$.

</li>

<li>

Downhill: $I_\text{down}$ does not depend on $U$.

</li>

<li>

At $U=0$ no current flows, so $I_\text{down}=I_0$. The net current is $I=I_\text{up}-I_\text{down}=I_0(\mathrm{e}^{U/U_T}-1)$.

</li>

<li>

Electrons and holes have the same barrier, and their currents add with the same factor: $I_0$ becomes $I_\mathrm S$.

</li>

</ol>

Simplification: in reality the size of $I_\mathrm S$ is determined by the diffusion of the minority in the neutral regions behind the space-charge region. The factor $\mathrm{e}^{U/U_T}$ remains, because it sets the carrier density at the edge of the region.
:::

**Example.** With [(4.1)](#gl-4-1), the reference model gives:

| $I$ | 1 µ A | 10 µ A | 100 µ A | 1 mA | 10 mA |
|---|---|---|---|---|---|
| $U$ | 0.476 V | 0.536 V | 0.595 V | 0.655 V | 0.714 V |

At 0.655 V the barrier has shrunk to $2.3\,U_T$, and the fraction has risen from $10^{-12}$ to 0.1. **Limiting cases:** At $U=0$, $I=0$. For $U\ll-U_T$, $I=-I_\mathrm S$ remains: already at $-5\,U_T$ it is 99.3 % of that. From $U=119$ mV on, the term $-1$ is smaller than 1 % of the first term.

**Reverse direction.** At $U<0$ the barrier grows and the region becomes wider. The uphill current dies out, and only the minority current remains. It does not depend on how high the barrier is, only on how many carriers reach its edge. That is why it saturates at $I_\mathrm S$. Real diodes block with pA to nA, because additional pairs are generated in the region.

:::ltspice The characteristic curve of the reference-model diode
⁠**Draw:** `voltage` named `V1` from `a` to ground, `diode` from `a` to ground, value `DM`.

⁠**Directives:** `.model DM D(Is=1e-14)` and `.dc V1 0 0.8 1m`

⁠**What you see:** `I(D1)` seems to start at 0.6 V. Set the current axis to logarithmic: it becomes a straight line. At 0.6547 V you read 0.98 mA, at 0.7142 V 9.8 mA, at 0.7737 V 98 mA. LTspice calculates at 27 °C, hence the 2 % deviation from 1, 10 and 100 mA. Use this to check Exercise [4](#aufg-4)(a).
:::

:::frage What happens when $U$ becomes larger than $U_\mathrm{D0}$? Is the barrier gone then?
The formula no longer applies there. At such a high current, the carriers that have crossed the barrier are as dense in the foreign region as the doping, and the neutral regions have a noticeable resistance (__bulk resistance__, a few $\Omega$). The rest of the external voltage drops there, and the characteristic curve becomes flatter and almost straight. The barrier never becomes negative.
:::

:::zusatz Temperature
$I_\mathrm S$ contains $n_\mathrm i^2$ and grows by a factor of about 4 per 10 K. This outweighs the growth of $U_T$: at a fixed current the voltage falls by about 2 mV/K. Real diodes often follow $\mathrm{e}^{U/(mU_T)}$ with $1\le m\le2$.
:::

:::aufgabe Exercise 4 ★ Decades
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

The diode of the reference model shows 0.655 V at 1 mA. Without a calculator, estimate $U$ at 100 mA and at 10 µ A.

</li>

<li>

By how many mV does $U$ rise when the current doubles? When it triples?

</li>

<li>

What current flows at $U=-1$ V and at $U=-0.2$ V?

</li>

</ol>

:::loesung
(a) 100 mA is two decades more: $0.655\,\mathrm{V}+2\cdot0.060\,\mathrm{V}=0.775$ V (exactly 0.774 V). 10 µ A is two decades less: 0.535 V (exactly 0.536 V). (b) Doubling: $U_T\ln2=17.9$ mV. Tripling: $U_T\ln3=28.4$ mV. (c) At $-1$ V, $\mathrm{e}^{U/U_T}\approx0$, so $I=-10^{-14}$ A. At $-0.2$ V, $\mathrm{e}^{-7.7}=4.4\cdot10^{-4}$, so likewise $I=-10^{-14}$ A to within 0.05 %.
:::
:::
