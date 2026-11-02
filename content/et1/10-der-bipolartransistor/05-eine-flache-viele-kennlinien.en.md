---
title: Stage 3: One surface, many characteristic curves
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200500
summary: Data sheets show several characteristic curves with different axes.
tags: characteristic curve, slice, family of curves, Input characteristic, Control characteristic, Current control characteristic, Output characteristic, transfer characteristic
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Data sheets show several characteristic curves with different axes. This stage traces them back to one object.
:::

**The idea.** $I_\mathrm{C}$ depends on two voltages. A function of two variables is a surface, like a terrain over a map: the map has the directions $U_\mathrm{BE}$ and $U_\mathrm{CE}$, the height of the terrain is $I_\mathrm{C}$ (Fig. [3](#abb-3)). A __characteristic curve__ (relationship between two quantities, [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) arises when one voltage is held fixed: a __slice__ through the terrain. Several parallel slices give a __family of curves__. So there are not many dependencies, but one terrain with several views. In the direction of $U_\mathrm{BE}$ it is a steep slope (red), in the direction of $U_\mathrm{CE}$ an edge and then an almost horizontal plane (green).

:::abbildung et1/k10flaeche 3
The surface $I_\mathrm{C}(U_\mathrm{BE},U_\mathrm{CE})$ of the reference model. Red: slice at $U_\mathrm{CE}=6$ V, exponential. Green: slice at $U_\mathrm{BE}=0.6$ V, first steep, then almost horizontal. The two meet at the operating point.
:::

:::satz Theorem 3.1 (The model surface)
<span class="anker" id="satz-3-1"></span>

For $U_\mathrm{BE}\gg U_T$ and $U_\mathrm{CE}\ge0$, the reference model has

<span class="anker" id="gl-3-1"></span>
$$I_\mathrm{C}=\underbrace{I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}}_{\text{injection}}\cdot\underbrace{\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)}_{\text{collection}}\cdot\underbrace{\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)}_{\text{small slope}},\qquad I_\mathrm{B}=\frac{I_\mathrm{S}}{B}\,\mathrm{e}^{U_\mathrm{BE}/U_T}. \tag{3.1}$$
:::

⁠**How to read it:** The first factor is [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1). The second tends to 1 as soon as the collector lies a few $U_T$ above the emitter: it counts how many electrons the collector sends back, which is 15 % at $U_\mathrm{CE}=0.05$ V, still 2 % at 0.1 V and only 0.05 % at 0.2 V. The third factor describes the slight increase with $U_\mathrm{CE}$ (Stage [9](tangente-statt-kurve.html#stufe-9)). $I_\mathrm{S}$ and $B$ apply at $U_\mathrm{CE}=6$ V. **Validity:** a model for small and medium currents.

:::herleitung The factor $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$
The electron current through the base is proportional to the density gradient between its two edges. Each edge follows the voltage at its boundary: $\mathrm{e}^{U_\mathrm{BE}/U_T}$ at the emitter, $\mathrm{e}^{U_\mathrm{BC}/U_T}$ at the collector, with $U_\mathrm{BC}=-U_\mathrm{CB}=U_\mathrm{BE}-U_\mathrm{CE}$ from [(1.1)](drei-schichten-zwei-spannungen.html#gl-1-1). So $I_\mathrm{C}\sim\mathrm{e}^{U_\mathrm{BE}/U_T}-\mathrm{e}^{(U_\mathrm{BE}-U_\mathrm{CE})/U_T}=\mathrm{e}^{U_\mathrm{BE}/U_T}(1-\mathrm{e}^{-U_\mathrm{CE}/U_T})$. The exponential function in $U_\mathrm{BE}$ and the edge in $U_\mathrm{CE}$ are two sides of one difference.
:::

:::abbildung et1/k10schnitte 4
Four slices from equation [(3.1)](#gl-3-1). Left, input and control characteristics at $U_\mathrm{CE}=6$ V: the same shape, the $I_\mathrm{B}$ axis is scaled differently by a factor of 200. Center, output characteristics for $I_\mathrm{B}=5$ to 20 µ A, dashed the boundary $U_\mathrm{CE}=U_\mathrm{BE}$. Right, current control characteristic with slope $B$.
:::

| Characteristic | held fixed | axes | shape and reason |
|---|---|---|---|
| __Input characteristic__ | $U_\mathrm{CE}$ | $I_\mathrm{B}$ over $U_\mathrm{BE}$ | Diode, knee around 0.6 V: the BE boundary is a diode |
| __Control characteristic__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ over $U_\mathrm{BE}$ | Same shape, $B$ times higher: injection |
| __Current control characteristic__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ over $I_\mathrm{B}$ | Straight line with slope $B$: the exponential function cancels out |
| __Output characteristic__ | $U_\mathrm{BE}$ or $I_\mathrm{B}$ | $I_\mathrm{C}$ over $U_\mathrm{CE}$ | Steep, then almost flat like a current source: collection |

The current control characteristic is also called the __transfer characteristic__. At very large currents it flattens and $B$ falls: the base is then so full of electrons that the simple calculation no longer holds. The boundary $U_\mathrm{CE}=U_\mathrm{BE}$ in Fig. [4](#abb-4) is the locus $U_\mathrm{CB}=0$. To the left of it the CB diode already conducts weakly, but the curve only bends down below around 0.2 V.

**Example.** Slice at $U_\mathrm{CE}=6$ V: 0.582 V, 0.600 V and 0.618 V give 1.0 mA, 2.0 mA and 4.0 mA. Slice at $U_\mathrm{BE}=0.6$ V: $U_\mathrm{CE}=0.05$ V; 0.2 V; 6 V; 14 V give 1.58 mA; 1.85 mA; 2.00 mA; 2.20 mA. **Limiting case:** for $U_\mathrm{CE}=0$, $I_\mathrm{C}=0$: both edges of the base lie at the same height, and there is no gradient.

:::frage So does the current depend on $U_\mathrm{CE}$ or not?
Yes, but to very different degrees. Strongly up to 0.2 V, after that by around 1 % per volt. For comparison: 1 mV at $U_\mathrm{BE}$ has an effect of 3.9 %. “Depends” does not mean “depends equally strongly”. The terrain has a slope in both directions; they are just very different.
:::

:::ltspice The family of output characteristics
⁠**Draw:** `npn` with the model name `T`, emitter at ground, at the collector `voltage` named `VCE`, at the base `current` with `{IB0}` from ground to the base.

⁠**Directives:** `.model T NPN(IS=1.55e-13 BF=186 VAF=74)`, `.param IB0=10u`, `.step param IB0 list 5u 10u 15u 20u`, `.dc VCE 0 12 0.02`. At 6 V and 27 °C these parameters give the values of T, because LTspice counts $B$ and $I_\mathrm{S}$ at $U_\mathrm{CB}=0$.

⁠**What you see:** Four curves in `Ic(Q1)`, steep up to 0.2 V, then rising slightly. At $I_\mathrm{B}=10$ µ A, LTspice shows 1.996 mA at 6 V and 2.147 mA at 12 V; the calculation gives 2.00 mA and 2.15 mA. Compare with Exercise [3](#aufg-3).
:::

:::aufgabe Exercise 3 ★ Reading slices
<span class="anker" id="aufg-3"></span>

(a) From [(3.1)](#gl-3-1), determine $I_\mathrm{C}$ at $U_\mathrm{BE}=0.6$ V for $U_\mathrm{CE}=0.1$ V and 12 V. Which characteristic are you calculating? (b) Determine $I_\mathrm{C}$ at $U_\mathrm{CE}=6$ V for $U_\mathrm{BE}=0.56$ V and 0.62 V. Which characteristic is this? (c) Predict: What does the curve $I_\mathrm{C}(I_\mathrm{B})$ look like at $U_\mathrm{CE}=0.05$ V, compared with the one at 6 V?

:::loesung
(a) $1.81$ mA and $2.15$ mA, a slice at fixed $U_\mathrm{BE}$: output characteristic. (b) 0.43 mA and 4.32 mA, a slice at fixed $U_\mathrm{CE}$: control characteristic. 60 mV make the factor of 10. (c) Again a straight line through the origin, only flatter. $I_\mathrm{B}$ in [(3.1)](#gl-3-1) does not depend on $U_\mathrm{CE}$, and the other two factors are constants at fixed $U_\mathrm{CE}$: $0.854\cdot0.926=0.79$, so the slope is 158 instead of 200.
:::
:::
