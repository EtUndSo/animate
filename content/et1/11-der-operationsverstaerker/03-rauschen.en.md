---
title: Stage 1: Noise
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1210300
summary: A sensor delivers millivolts, and every conductor produces a random interference voltage.
tags: noise voltage density, signal-to-noise ratio, decibels, Boltzmann constant, Thermal noise, Shot noise, 1/f noise, white noise
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A sensor delivers millivolts, and every conductor produces a random interference voltage. This stage clarifies where it comes from, how it is measured, and what an amplifier can do about it.
:::

**The idea.** Noise is a disturbance made up of many oscillations of different frequency and amplitude. Its waveform is random and can only be described statistically: the mean is zero, and the rms value measures its strength. Because independent disturbances sometimes reinforce and sometimes cancel each other, it is not their rms values that add but the squares of these values. That is why noise is described by the __noise voltage density__ $|u_\mathrm{r}(f)|^2$: the contribution of each frequency strip 1 Hz wide to the square of the rms value.

:::definition Definition 1.1 (Noise)
<span class="anker" id="satz-1-1"></span>

The rms value of the noise voltage and the density of the thermal noise of a resistor are

<span class="anker" id="gl-1-1"></span>
$$u_\mathrm{r,eff}=\sqrt{\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f},\qquad |u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R. \tag{1.1}$$

The __signal-to-noise ratio__ is the ratio of the powers, written in __decibels__ (dB):

<span class="anker" id="gl-1-2"></span>
$$\mathrm{SNR}=\frac{P_\mathrm{s}}{P_\mathrm{r}}=\Bigl(\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}\Bigr)^2,\qquad \mathrm{SNR}_\mathrm{dB}=10\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=20\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}. \tag{1.2}$$
:::

⁠**How to read it:** $[|u_\mathrm{r}|^2]=\mathrm{V^2/Hz}$. $k_\mathrm{B}=1.381\cdot10^{-23}$ J/K is the __Boltzmann constant__: it converts temperature into mean thermal energy per particle. $T$ is the absolute temperature in K, $R$ the resistance. $\lg$ is the base-10 logarithm. 20 dB mean a factor of 10 in voltage and 100 in power. **Validity:** The right-hand part of [(1.1)](#gl-1-1) holds up to far beyond the frequencies of electronics.

| Type | Mechanism | Density |
|---|---|---|
| __Thermal noise__ | Thermal motion of the charge carriers in every conductor. Random accumulations at the ends produce a voltage, even without current flow. | constant, $\sim T\,R$ |
| __Shot noise__ | Current consists of individual charges that cross a potential barrier at random times, for example in the pn junction. | constant |
| __1/f noise__ | Recharging of surface states, fluctuating number of free charge carriers in the semiconductor. | $\sim1/f$, interferes up to about 10 kHz |

Constant density is called __white noise__, after white light made of all colors. This is a shape of the spectrum, not a cause. Integrated over all frequencies it would give infinite power. That is a limit of the model: real densities fall off at very high frequencies, and every circuit has a finite __bandwidth__ $\Delta f$, the frequency range it passes. For white noise the integral becomes $u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2\,\Delta f}$.

:::abbildung et1/k11rauschen 1
Left, the density of a 10-k$\Omega$ resistor with a 1/f component below 1 kHz: flat above (white), rising below. Right, the same useful signal without noise and with noise at 20 dB, that is, at a tenth of its rms value.
:::

:::herleitung Why squares add
For two independent disturbances, $(u_1+u_2)^2=u_1^2+2u_1u_2+u_2^2$. Averaged over time, the product $u_1u_2$ is positive as often as it is negative, so its mean vanishes. What remains is $u_\mathrm{tot,eff}^2=u_\mathrm{1,eff}^2+u_\mathrm{2,eff}^2$. The integral in [(1.1)](#gl-1-1) is this sum over all frequency strips.
:::

::::beispiel
The sensor resistor has $|u_\mathrm{r,R}|^2=4\cdot1.381\cdot10^{-23}\cdot300\cdot10^4=1.66\cdot10^{-16}\,\mathrm{V^2/Hz}$, so in 20 kHz, $u_\mathrm{r,eff}=1.82$ µ V. The useful signal of 1 mV is 549 times larger: $\mathrm{SNR}=54.8$ dB. Half the bandwidth lowers the noise by $\sqrt2$, which is 3 dB.
::::

⁠**Limiting cases:** For $R\to0$ or $T\to0$ the thermal noise vanishes.

**What an amplifier changes.** It raises the signal and the noise present at its input by the same factor, so the SNR stays the same or gets worse through the amplifier's own noise. It helps only against disturbances that join in *behind* it and have a fixed size. If the line to the next device adds 100 µ V, then 20.0 dB remain without an amplifier. With a gain of 100 at the sensor it is $0.1\,\mathrm{V}/\sqrt{(182\,\mathrm{\mu\text{} V})^2+(100\,\mathrm{\mu\text{} V})^2}$, that is, 53.7 dB. The second remedy is the difference: a disturbance that hits two lines equally vanishes if only their difference is evaluated. Stage [2](der-differenzverstarker.html#stufe-2) achieves this.

:::aufgabe Exercise 1 ★★ Thermal noise
<span class="anker" id="aufg-1"></span>

(a) How large is the noise of 47 k$\Omega$ in 10 kHz at 300 K, and how large at 77 K? (b) Behind the 47 k$\Omega$ there are 53 k$\Omega$ in series. Add the two noise voltages correctly and compare with a single resistor of 100 k$\Omega$. (c) A signal of 200 µ V with the noise from (a) runs over a line that adds 50 µ V. How large is the SNR without and with a gain of 1000 ahead of the line?

:::loesung
(a) $u_\mathrm{r,eff}=\sqrt{4k_\mathrm{B}\cdot300\,\mathrm{K}\cdot47\,\mathrm{k\Omega}\cdot10\,\mathrm{kHz}}=2.79$ µ V, at 77 K smaller by $\sqrt{77/300}$: 1.41 µ V. (b) 53 k$\Omega$ gives 2.96 µ V. Independent disturbances add in quadrature: $\sqrt{2.79^2+2.96^2}\,\mu\text{V}=4.07$ µ V, exactly the value of 100 k$\Omega$. The linear sum 5.75 µ V would be wrong. (c) Without an amplifier: $200/\sqrt{2.79^2+50^2}=4.0$, that is, 12.0 dB. With a gain of 1000: $200\,\mathrm{mV}/\sqrt{(2.79\,\mathrm{mV})^2+(0.05\,\mathrm{mV})^2}=71.7$, that is, 37.1 dB. This is almost the SNR at the input; the line no longer plays a role.
:::
:::
