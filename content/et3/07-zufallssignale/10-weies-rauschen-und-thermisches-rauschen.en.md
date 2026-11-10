---
title: Stage 9: White noise and thermal noise
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Random Signals
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Chapter 7: Random Signals
order: 3271000
summary: The most important model for disturbances: noise with the same power density at all frequencies.
tags: white noise
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
The most important model for disturbances: noise with the same power density at all frequencies.
:::

:::definition Definition 9.1 (White noise)
<span class="anker" id="satz-9-1"></span>

A zero-mean process with $\Phi_{ss}(f)=N_0$ for all $f$ is called __white noise__. Its ACF is $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
:::

⁠**How to read it:** Values at different times are uncorrelated, no matter how close together they are. The power $\int N_0\mathrm{d} f$ is infinite: white noise is a limiting model, like the Dirac impulse. What is actually measured is always filtered, “colored” noise:

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

Behind an ideal low-pass filter with the cutoff frequency $f_\mathrm g$: $L_g=2N_0f_\mathrm g$ and $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ (Fig. [3](#abb-3)). The ACF is zero at $\tau=k/(2f_\mathrm g)$, $k\neq0$: samples taken at the Nyquist rate are uncorrelated.

:::abbildung et3/k7tp 3
ACF of white noise behind an ideal low-pass filter: $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$. At $\tau=0$ it equals the power $2N_0f_\mathrm g$. At the red dots ($\tau=k/(2f_\mathrm g)$) it is zero.
:::

**Thermal noise.** The thermal motion of the electrons produces a noise voltage across every resistor $R$. In open circuit, measured in the frequency range $|f|\le f_\mathrm g$:

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

with the Boltzmann constant $k=1.38\cdot10^{-23}$ W s/K. At room temperature (290 K), $kT\approx4\cdot10^{-21}$ W/Hz, that is, 4 pW per GHz of bandwidth. $L_{\max}$ is the maximum power that can be extracted from the resistor, under power matching. In the reference model ($1\,\mathrm{k\Omega}$, 20 kHz), the RMS value is $\sqrt{\mathrm E\{u^2\}}=0.57$ µ V. This order of magnitude limits how sensitive a microphone amplifier can be. The spectrum is flat up to about $10^{12}$ Hz.

:::ltspice Measuring thermal noise
LTspice gives every resistor its thermal noise. The `.noise` analysis computes the noise density `V(onoise)` at a node in V$/\sqrt{\mathrm{Hz}}$. The measurement `.meas noise urms INTEG V(onoise)` integrates it in quadrature over the frequency range of the analysis, as in [(8.3)](zufallssignale-in-lti-systemen-leistungsdichte.html#gl-8-3), and gives the RMS value. `.temp 16.85` sets 290 K.

⁠**Resistor:** `res` with `{Rx}` from net `a` to ground, in parallel a `current` source with the value 0 (name `I1`). It loads nothing; `.noise` only needs it as a reference source. Directives `.param Rx=1k` and `.noise V(a) I1 lin 20001 1 20k`. Result: 4.0 nV$/\sqrt{\mathrm{Hz}}$ and `urms` $=0.57$ µ V as above. Set `Rx=1Meg` and compare with your result from Exercise [8](#aufg-8).

⁠**$kT/C$:** a `voltage` source `V1` with the value 0 and `AC 1`, `res` with `{Rx}` to `out`, `cap` with `1p` to ground. Directives `.step param Rx list 1k 1Meg` and `.noise V(out) V1 dec 200 1 1T`, plus `.temp 16.85` and the measurement `urms` again. `urms` is the same for both resistors. Compare the value with your result from Exercise [9](#aufg-9)(b).
:::

:::aufgabe Exercise 8 ★ Noise of a resistor
<span class="anker" id="aufg-8"></span>

Compute the RMS noise voltage of a $1\,\mathrm{M\Omega}$ resistor at 290 K and 20 kHz bandwidth. By what factor is it larger than for the $1\,\mathrm{k\Omega}$ resistor, and why by exactly this factor?

:::loesung
The RMS value grows with $\sqrt R$: $\sqrt{1000}=31.6$ times larger, so $0.566\cdot31.6=17.9$ µ V.
:::
:::

:::aufgabe Exercise 9 ★★ $kT/C$ noise
<span class="anker" id="aufg-9"></span>

The thermal noise of the resistor ($N_0=2kTR$) passes through the RC circuit that the resistor forms with a capacitor $C$ ($h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$).

<ol class="al">

<li>

Use [(9.1)](#gl-9-1) to show that the noise power across the capacitor is $kT/C$, independent of $R$.

</li>

<li>

What is the RMS value for $C=1$ pF and 290 K? Why does a smaller resistor not help here?

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$. So $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$.

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V. A smaller resistor does produce less noise per hertz, but the RC circuit becomes more broadband ($1/RC$ larger). The two effects cancel exactly. Only a larger capacitor reduces the noise.
:::
:::
