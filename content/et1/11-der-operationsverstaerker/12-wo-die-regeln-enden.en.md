---
title: Stage 10: Where the rules end
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1211200
summary: Up to here the op amp was ideal except for A and the limits.
tags: Offset voltage, Input bias current, common-mode rejection, transition frequency, slew rate, overdriven
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
Up to here the op amp was ideal except for $A$ and the limits. This stage orders the real deviations by size and summarizes the procedure.
:::

**The idea.** Real deviations act in two ways. Some shift the point the loop regulates to: the transistors T1 and T2 are never exactly equal, so the rest point is not $U_\mathrm{D}=0$ but $U_\mathrm{D}=U_\mathrm{off}$. The others reduce the reserve $A\beta$. Above all the frequency: so that the loop does not oscillate, an internal capacitance limits the bandwidth. The voltage across it cannot follow fast signals, and $A$ falls.

| Quantity | Cause | Effect in the reference model |
|---|---|---|
| $A$ finite, $10^5$ to $10^6$ | Limited stage gain | Deviation $1/(A\beta)=0.005$ % |
| __Offset voltage__ $U_\mathrm{off}$ | Unequal input transistors; changes with temperature, supply, age | At the output $U_\mathrm{off}/\beta=5$ mV, even at $U_\mathrm{E}=0$ |
| __Input bias current__ $I_\mathrm{B}$ | Base currents of T1 and T2 | Through $R_2$: $I_\mathrm{B}R_2=2$ mV |
| Common mode | Real current source T3, unequal branches | see below |
| $A(f)$ | Internal capacitance | $\vert A(f)\vert \approx f_\mathrm{T}/f$, see below |
| Output | Transistors of the output stage | $\pm11$ V, 20 mA, $r_\mathrm{a}/(1+A\beta)=3.75$ m$\Omega$ |
| Noise | Own transistors | 10 nV/$\sqrt{\text{Hz}}$: 1.41 µ V in 20 kHz |

The offset is the input voltage at which the output becomes zero. In the loop, $\varphi_+-\varphi_-=U_\mathrm{off}$ establishes itself, and the divider enlarges this by $1/\beta$. The op amp's own noise adds in quadrature to the sensor from Stage [1](rauschen.html#stufe-1): 2.31 µ V instead of 1.82 µ V, and the SNR falls by 2.1 dB to 52.7 dB.

:::definition Definition 10.1 (Common-mode rejection)
<span class="anker" id="satz-10-1"></span>

The __common-mode rejection__ CMRR (common mode rejection ratio) compares the gain of the difference with that of the common mode:

<span class="anker" id="gl-10-1"></span>
$$\mathrm{CMRR}=\frac{A}{A_\mathrm{cm}},\qquad \mathrm{CMRR}_\mathrm{dB}=20\lg\frac{A}{A_\mathrm{cm}}. \tag{10.1}$$

Ideally $\mathrm{CMRR}\to\infty$; usual values are 60 dB ($A_\mathrm{cm}/A=10^{-3}$) to 120 dB ($10^{-6}$).
:::

⁠**How to read it:** Mechanism: a real T3 has a finite $r_\mathrm{CE}$. If the common mode rises, E rises, and the total current grows by $U_\mathrm{cm}/r_\mathrm{CE}$. In the differential stage from Stage [2](der-differenzverstarker.html#stufe-2) with $r_\mathrm{CE}=40$ k$\Omega$, each collector changes with the factor $R_\mathrm{C}/(2r_\mathrm{CE})=0.0375$ against 57.7 for the difference: 63.7 dB. In the reference model it is 90 dB, so $A_\mathrm{cm}=3.16$. On the difference amplifier from Stage [6](mehrere-eingange-mehrere-stufen.html#stufe-6), 2 V of common mode acts like $2\,\mathrm{V}/31600=63$ µ V of difference, which is 0.32 mV at the output, 0.16 % of the measured 0.2 V.

**The frequency.** Above $f_A=f_\mathrm{T}/A=10$ Hz, $A$ falls by a factor of 10 per decade, $|A(f)|\approx f_\mathrm{T}/f$. At the __transition frequency__ $f_\mathrm{T}$, $|A|=1$. The loop works as long as $|A(f)|\,\beta\gg1$. The reserve is used up at $f_G=\beta\,f_\mathrm{T}$:

<span class="anker" id="gl-10-2"></span>
$$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}},\qquad f_G=\beta\,f_\mathrm{T},\qquad G\,f_G=f_\mathrm{T}. \tag{10.2}$$

⁠**How to read it:** With $G=5$ the bandwidth reaches 200 kHz. The product of gain and bandwidth is fixed: with $G=1$ it would be 1 MHz, with $G=100$ only 10 kHz. The time constant $\tau_G=0.80$ µ s from Stage [4](gegenkopplung.html#stufe-4) is the same value: $1/(2\pi\cdot200\,\mathrm{kHz})$. **Limiting case:** For $f\gg f_G$, $|G|\to|A|$; the feedback no longer acts.

:::abbildung et1/k11bode 12
Open-loop gain and gain of the circuit versus frequency, both axes logarithmic. The distance between the curves is the reserve $|A|\beta$. It is still 200 at 1 kHz and used up at 200 kHz.
:::

:::ltspice Bandwidth and latching
⁠**Draw:** Symbol `UniversalOpAmp2` (folder OpAmps) with `Avol=100k GBW=1Meg Slew=0.5Meg`, `Ilimit=20m Rail=1`, supply `voltage` $\pm12$. Circuit as in the box in Stage [4](gegenkopplung.html#stufe-4), `VE` with `AC 1`.

⁠**Directives:** `.ac dec 50 1 10Meg`, `.meas ac g0 FIND mag(V(a)) AT=10`, `.meas ac fg WHEN mag(V(a))=g0/sqrt(2)`.

⁠**What you see:** `fg` = 199 kHz against 200 kHz in the calculation. Then swap the inputs, give `VE` the value `PULSE(-3 3 1m 1u 1u 1m 2m)` and run `.tran 4m`: `V(a)` jumps between $\pm10.98$ V. With $\pm1$ V instead of $\pm3$ V the output stays put; this is the hysteresis from Stage [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9). For Exercise [11](#aufg-11) set `R1` to 1k and `R2` to 100k.
:::

:::zusatz Slew rate
The internal charging current is limited. That is why the output has a maximum speed, the __slew rate__, typically 0.5 V/µ s. The step from Fig. [5](gegenkopplung.html#abb-5) thus really takes about 10 µ s instead of a few µ s. A sine wave with 11 V amplitude stays undistorted only up to about 7.2 kHz, even though the bandwidth is much larger.
:::

:::merke The calculation scheme
<ol>

<li>

⁠**No feedback** (comparator): $U_\mathrm{A}=U_\mathrm{A,max}$ or $U_\mathrm{A,min}$, $U_\mathrm{D}\ne0$.

</li>

<li>

⁠**Check the sign:** Raise the output in your mind. If $U_\mathrm{D}$ falls, it is negative feedback; if it rises, positive feedback.

</li>

<li>

⁠**Negative feedback:** Assume $U_\mathrm{D}=0$ and calculate $U_\mathrm{A}$ with the node rule and Ohm's law. If it lies within the limits, the calculation is valid. Otherwise the op amp is __overdriven__: $U_\mathrm{A}$ is at its limit, $U_\mathrm{D}\ne0$, and you calculate the network with this fixed $U_\mathrm{A}$.

</li>

<li>

⁠**Positive feedback:** As a rule, $U_\mathrm{A}$ at the limit, $U_\mathrm{D}\ne0$. The thresholds follow from the sign change of $U_\mathrm{D}$.

</li>

<li>

⁠**Accuracy:** $1/(A\beta)$ at the signal frequency, $U_\mathrm{off}/\beta$ and $I_\mathrm{B}R_2$ at the output.

</li>

</ol>
:::

:::aufgabe Exercise 11 ★★★ Measuring amplifier
<span class="anker" id="aufg-11"></span>

A sensor with 10 mV is to be amplified to about 1 V using V: $R_1=1$ k$\Omega$, $R_2=100$ k$\Omega$, non-inverting. (a) How large are $\beta$, $G$ and the deviation due to $A$? (b) Up to what frequency does the circuit reach? How large is $|G|$ at 5 kHz? (c) How large is the offset at the output, and what share of the signal is it? How much does $I_\mathrm{B}$ add? (d) Up to what input does the output reach? (e) An integrator with $R\,C=10$ ms has the same offset. How fast does its output run at $U_\mathrm{E}=0$, and when does it hit its limit?

:::loesung
(a) $\beta=1/101$, $G\approx101$, deviation $101/A=0.10$ %. (b) $f_G=1\,\mathrm{MHz}/101=9.9$ kHz. $|G(5\,\mathrm{kHz})|=101/\sqrt{1+(5/9.9)^2}=90.2$. Such a circuit already loses a tenth at 5 kHz. (c) $101\cdot1\,\mathrm{mV}=101$ mV, that is, 10 % of the signal of 1.01 V. In addition $I_\mathrm{B}R_2=5$ mV. (d) $11\,\mathrm{V}/101=109$ mV. (e) $1\,\mathrm{mV}/10\,\mathrm{ms}=0.1$ V/s, at the limit after 110 s. A real integrator therefore needs a reset switch or a large resistor in parallel with $C$.
:::
:::
