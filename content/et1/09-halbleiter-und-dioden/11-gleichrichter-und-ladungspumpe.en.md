---
title: Stage 9: Rectifiers and charge pump
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Semiconductors and Diodes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Chapter 9: Semiconductors and Diodes
order: 1191100
summary: The half-wave rectifier wastes every second half-wave.
tags: bridge rectifier, smoothing
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
The half-wave rectifier wastes every second half-wave. This stage uses both, and it shows how to raise a voltage above the source voltage with diodes and capacitors.
:::

**The idea.** The __bridge rectifier__ (Graetz circuit) consists of four diodes in a diamond (Fig. [11](#abb-11)). They switch the load in each half-wave so that the current always passes through it from top to bottom. With positive voltage on the left, it runs through D$_1$, the load and D$_3$. Meanwhile D$_2$ has its cathode at the top on the high potential and its anode at the low input, so it blocks, and likewise D$_4$. In the other half-wave the pairs swap.

:::abbildung et1/k9graetz 11
Top: bridge in both half-waves, conducting diodes in color, blocked ones gray; the plus sign marks the higher input. The current through the load $R$ always has the same direction. Bottom: input $u_\mathrm e$ (gray) and output $u_\mathrm a$ (blue) for $\hat u=12$ V, $U_\mathrm F=0.7$ V.
:::

:::satz Theorem 9.1 (Bridge rectifier)
<span class="anker" id="satz-9-1"></span>

In the model with forward voltage, since the current always passes through two diodes in series,

<span class="anker" id="gl-9-1"></span>
$$u_\mathrm a=\begin{cases}|u_\mathrm e|-2U_\mathrm F&|u_\mathrm e|>2U_\mathrm F\\0&\text{otherwise.}\end{cases} \tag{9.1}$$

A blocked diode bears at most $\hat u-U_\mathrm F$.
:::

⁠**How to read it:** For $|u_\mathrm e|<2U_\mathrm F$ neither pair conducts, and $u_\mathrm a$ stays zero. At the lowered peak you can read off twice the forward voltage. **Validity:** resistive load. Input and output have no common reference point.

::::beispiel
The peak is $12\,\mathrm{V}-1.4\,\mathrm{V}=10.6$ V; for the half-wave rectifier it is 11.3 V. The gap lasts 0.74 ms per half-wave, which is 7.4 % of the time. The mean value is 6.29 V; for the half-wave rectifier it is only 3.48 V.
::::

⁠**Limiting cases:** For $U_\mathrm F\to0$, $u_\mathrm a=|u_\mathrm e|$. For $\hat u<1.4$ V the output stays zero.

:::ltspice Bridge rectifier
⁠**Draw:** source with `SINE(0 12 50)` between `a` and `b`. Diodes DM from `a` to `p`, from `b` to `p`, from ground to `a` and from ground to `b`. `res` 1k from `p` to ground.

⁠**Directive:** `.tran 40m`

⁠**What you see:** `V(p)` as in Fig. [11](#abb-11), peak 10.57 V, mean value 6.29 V. The voltage $V(p,a)$ across the blocked diode reaches 11.28 V. The calculation gives 10.6 V, 6.29 V and 11.3 V. For Exercise [11](#aufg-11), use 24 instead of 12.
:::

:::frage This still pulses strongly. Is this already DC voltage?
Not yet. A capacitor in parallel with the load (__smoothing__) charges to the peak and feeds the load during the gap. In 10 ms it loses $\Delta U=I\,\Delta t/C$ ([Chapter 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). With $I=10.6$ mA and $C=470$ µ F that is 0.23 V. The diodes then conduct only briefly at the peak.
:::

**Charge pump.** It produces a higher voltage from a DC voltage $U_\mathrm e$, without a coil. The diodes are treated as ideal here (Fig. [12](#abb-12)). *Step 1:* The changeover switch connects the bottom plate of $C_1$ to ground. $C_1$ charges through D$_1$ to $U_\mathrm e$. *Step 2:* The changeover switch connects the bottom plate to $U_\mathrm e$. The voltage across $C_1$ cannot jump ([Chapter 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), so the top plate jumps to $2U_\mathrm e$. D$_1$ blocks because its cathode is now higher, D$_2$ conducts, and $C_1$ gives charge to the output capacitor $C_2$. After a few cycles, $U_\mathrm a\approx2U_\mathrm e$. In practice, small resistors limit the current peaks. With further pump stages on the same scheme, the voltage rises further.

:::abbildung et1/k9pumpe 12
Charge pump; the current paths of the two steps are in color. Left: $U_\mathrm e$ charges the capacitor $C_1$. Right: $U_\mathrm e$ and the voltage across $C_1$ are in series and feed $C_2$.
:::

:::herleitung Voltage after $k$ cycles for $C_1=C_2$
In the first step, $C_2$ also charges to $U_\mathrm e$ through both diodes. In the pump step, $C_1$ with $2U_\mathrm e$ and $C_2$ with $U_\mathrm a$ are connected. Charge is conserved, and equal capacitors end at the mean value: $U_\mathrm a'=(2U_\mathrm e+U_\mathrm a)/2$. The distance to the final value $2U_\mathrm e$ halves per cycle: $U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$.
:::

With $U_\mathrm e=5$ V this gives 7.5 V, 8.75 V, 9.38 V, and so on up to 10 V. With real diodes you lose $U_\mathrm F$ twice: the final value is $2U_\mathrm e-2U_\mathrm F=8.6$ V. **Limiting case:** If current flows at the output, charge is missing per cycle, and $U_\mathrm a$ stays below the final value.

:::aufgabe Exercise 11 ★★ Power supply
<span class="anker" id="aufg-11"></span>

A bridge is connected to $\hat u=24$ V, $U_\mathrm F=0.7$ V.

<ol class="al">

<li>

How large is the peak of $u_\mathrm a$? What reverse voltage must each diode withstand?

</li>

<li>

For what fraction of the time is $u_\mathrm a=0$?

</li>

<li>

The load draws 100 mA. Which $C$ limits the fluctuation to 1 V? How large would it have to be for the half-wave rectifier, and why?

</li>

</ol>

:::loesung
(a) $24\,\mathrm{V}-1.4\,\mathrm{V}=22.6$ V, reverse voltage $24\,\mathrm{V}-0.7\,\mathrm{V}=23.3$ V. (b) $u_\mathrm a=0$ for $|\sin|<1.4/24$, that is, 3.34° around each zero crossing, which is $2\cdot3.34^\circ/180^\circ=3.7$ % of the time. (c) $C=I\,\Delta t/\Delta U=100\,\mathrm{mA}\cdot10\,\mathrm{ms}/1\,\mathrm{V}=1000$ µ F. With the half-wave rectifier, replenishment comes only every 20 ms, so 2000 µ F.
:::
:::

:::aufgabe Exercise 12 ★★ Counting pumps
<span class="anker" id="aufg-12"></span>

$U_\mathrm e=3$ V, $C_1=C_2$, ideal diodes.

<ol class="al">

<li>

How large is $U_\mathrm a$ after 1, 2 and 3 cycles?

</li>

<li>

After how many cycles is 99 % of the final value reached?

</li>

<li>

What final value do real diodes with 0.7 V give? What remains at $U_\mathrm e=1.5$ V, and what follows from this for low-voltage circuits?

</li>

</ol>

:::loesung
(a) $U_\mathrm a(k)=6\,\mathrm{V}-3\,\mathrm{V}\cdot2^{-k}$: 4.5 V, 5.25 V, 5.63 V. (b) $3\,\mathrm{V}\cdot2^{-k}\le0.06\,\mathrm{V}$ requires $2^k\ge50$, so $k=6$. (c) $6\,\mathrm{V}-1.4\,\mathrm{V}=4.6$ V. At 1.5 V, $3\,\mathrm{V}-1.4\,\mathrm{V}=1.6$ V remain, hardly more than the input. At low voltages the diodes are therefore replaced by switches.
:::
:::
