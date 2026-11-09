---
title: Stage 8: Two circuits that make use of $U_\mathrm{BE}$
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1201000
summary: So far, U BE was a nuisance.
tags: current mirror, reference current, ripple
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
So far, $U_\mathrm{BE}$ was a nuisance. This stage uses its two properties: equal $U_\mathrm{BE}$ means equal current, and when the current changes, $U_\mathrm{BE}$ stays almost the same.
:::

**The idea: current mirror.** According to [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1), $U_\mathrm{BE}$ sets the current. So two equal transistors with the same voltage $U_\mathrm{BE}$ carry the same current. In the __current mirror__ (Fig. [9](#abb-9), left), T1 is connected as a diode: base and collector are joined. The current $I_\mathrm{ref}$ through the resistor sets at T1 exactly the voltage $U_\mathrm{BE}$ that this current needs. T2 hangs on the same voltage and copies the current into another branch, independently of its load.

:::satz Theorem 8.1 (Current mirror)
<span class="anker" id="satz-8-1"></span>

With equal transistors and $I_\mathrm{B1}=I_\mathrm{B2}$,

<span class="anker" id="gl-8-1"></span>
$$I_\mathrm{ref}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{ref}}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2},\qquad I_\mathrm{C2}=B\,I_\mathrm{B2}=\frac{I_\mathrm{ref}}{1+\frac2B}\approx I_\mathrm{ref}. \tag{8.1}$$
:::

⁠**How to read it:** $I_\mathrm{ref}$ is the __reference current__. The two base currents branch off from it. Hence the small error $2/B$. **Validity:** T2 active, equal transistors and equal temperature, for instance on one chip. Because of the slope of the characteristic, T2 delivers somewhat more at large $U_\mathrm{CE2}$.

::::beispiel
With $R_\mathrm{ref}=5.7$ k$\Omega$, $I_\mathrm{ref}=2$ mA and $I_\mathrm{C2}=1.98$ mA, with $R_\mathrm{L}$ arbitrary up to $11.8\,\mathrm{V}/1.98\,\mathrm{mA}=5.96$ k$\Omega$. Beyond that T2 would be saturated. With [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1), the current in T2 would be 7 % larger at $U_\mathrm{CE2}=6$ V and $U_\mathrm{CE1}=0.6$ V.
::::

⁠**Limiting case:** for $B\to\infty$, $I_\mathrm{C2}=I_\mathrm{ref}$.

**The idea: voltage regulator.** A rectifier with smoothing ([Part 9](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) delivers a DC voltage with a residual fluctuation, the __ripple__. In the regulator (Fig. [9](#abb-9), right), a Zener diode holds the base at $U_\mathrm{Z}$. The emitter is the output and lies one diode voltage lower. If the output voltage falls because the load draws more current, $U_\mathrm{BE}$ grows and the transistor supplies more. The rest of the input voltage drops across $U_\mathrm{CE}$. The load current does not flow through $R_1$; the base needs only one $B$-th of it. So the Zener diode is hardly loaded.

:::satz Theorem 8.2 (Voltage regulator with Zener diode)
<span class="anker" id="satz-8-2"></span>

The mesh across Zener diode, BE path and load gives

<span class="anker" id="gl-8-2"></span>
$$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}. \tag{8.2}$$
:::

⁠**How to read it:** $U_\mathrm{E,min}$ is the minimum of the input voltage $U_\mathrm{E}$ in the ripple trough, $U_\mathrm{A}$ is the output voltage. **Validity:** $U_\mathrm{E}>U_\mathrm{A}+U_\mathrm{CE,sat}$ must always hold for T to stay active, and $R_1$ must supply enough current: $(U_\mathrm{E,min}-U_\mathrm{Z})/R_1>I_\mathrm{B}$. Otherwise the Zener diode drops out of breakdown and the ripple reaches the output.

:::abbildung et1/k10spiegel 9
Left, current mirror: T1 as a diode produces $U_\mathrm{BE}$, T2 copies the current. Center, voltage regulator with Zener diode, the emitter is the output. Right, the waveform: the input voltage fluctuates between 10.5 V and 13.5 V, the output stays at 5.6 V.
:::

::::beispiel
$U_\mathrm{Z}=6.2$ V gives $U_\mathrm{A}=5.6$ V. At a 50 mA load, the base needs 0.25 mA. With $R_1=1$ k$\Omega$ and $U_\mathrm{E}=12$ V$\,\pm1.5$ V, 4.05 mA to 7.05 mA flow through the Zener diode. A Zener diode with a small-signal resistance of 10 $\Omega$ turns 3 V of ripple into just 30 mV. In the transistor, up to $7.9\,\mathrm{V}\cdot50\,\mathrm{mA}=395$ mW arise, just under $P_\mathrm{max}$. The regulator converts the excess voltage into heat. With 0.68 V instead of 0.6 V, the more accurate $U_\mathrm{BE}$ at 50 mA, $U_\mathrm{A}$ would be 80 mV smaller.
::::

⁠**Limiting case:** without a load, $I_\mathrm{B}\approx0$, $U_\mathrm{A}$ rises slightly, $U_\mathrm{Z}$ stays.

:::frage Why not the Zener diode alone?
Then the series resistor would have to supply the entire 50 mA plus a remainder for the Zener diode at the lowest input voltage. At peak voltage the difference would flow through the Zener diode, and the series resistor would heat up with around 0.7 W. The transistor separates the two: the Zener diode sets the voltage, the supply delivers the current via the collector. Power transistors and components derived from them also switch large currents, for instance in converters for electric motors.
:::

:::aufgabe Exercise 10 ★★ Mirror and regulator
<span class="anker" id="aufg-10"></span>

(a) Which $R_\mathrm{ref}$ gives the reference current 1 mA at $U_\mathrm{CC}=12$ V? How large is $I_\mathrm{C2}$ for $B=200$ and for $B=50$? (b) Up to which $R_\mathrm{L}$ does the mirror work at $B=200$? (c) A regulator has $U_\mathrm{Z}=9.1$ V, $R_1=470\,\Omega$, a 30 mA load, $U_\mathrm{E}$ from 12 V to 15 V. Determine $U_\mathrm{A}$, the smallest Zener current, the largest transistor power and the voltage margin at the low end.

:::loesung
(a) $R_\mathrm{ref}=11.4\,\mathrm{V}/1\,\mathrm{mA}=11.4$ k$\Omega$. $I_\mathrm{C2}=1\,\mathrm{mA}/1.01=0.990$ mA, and for $B=50$ it is $1\,\mathrm{mA}/1.04=0.962$ mA.

(b) $R_\mathrm{L}\le11.8\,\mathrm{V}/0.990\,\mathrm{mA}=11.9$ k$\Omega$.

(c) $U_\mathrm{A}=8.5$ V, $I_\mathrm{B}=0.15$ mA. At 12 V, $2.9\,\mathrm{V}/470\,\Omega=6.17$ mA then flow through $R_1$, and 6.02 mA through the Zener diode. At 15 V, $P=6.5\,\mathrm{V}\cdot30\,\mathrm{mA}=195$ mW. Margin: $12\,\mathrm{V}-8.5\,\mathrm{V}-0.2\,\mathrm{V}=3.3$ V.
:::
:::
