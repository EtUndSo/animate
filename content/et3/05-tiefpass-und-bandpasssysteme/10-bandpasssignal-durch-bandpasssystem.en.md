---
title: Stage 9: Bandpass signal through a bandpass system
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3251000
summary: What the envelopes are good for: how a bandpass acts on a bandpass signal can be calculated entirely in the lowpass domain.
tags: 
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
What the envelopes are good for: how a bandpass acts on a bandpass signal can be calculated entirely in the lowpass domain.
:::

:::satz Theorem 9.1 (Transmission in the equivalent lowpass domain)
<span class="anker" id="satz-9-1"></span>

If $S_T$ and $H_T$ both satisfy [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) (nothing below $-f_0$), then the envelope of the output satisfies

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Transmission
Multiplying out $G=S\cdot H$ with both representations [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) gives four products. The mixed ones, such as $S_T(f-f_0)H_T^*(-f-f_0)$, are zero: the first factor lives at positive frequencies, the second at negative ones. What remains is $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. Comparing this with $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ gives $G_T=\frac12S_TH_T$.
:::

⁠**How to read it:** the factor $\frac12$ compensates for the fact that $S_T$ and $H_T$ were both doubled. Otherwise it is the familiar convolution theorem, just for the envelopes. The carrier need not be included in the calculation at all.

**Example: switched-on cosine through the ideal bandpass.** $s(t)=\varepsilon(t)\cos(2\pi f_0t)$ with $f_0=10$ Hz, bandpass with $\Delta f=2$ Hz around $f_0$. The envelope of the input is $s_T\approx\varepsilon(t)$. (Approximation: the spectrum of the step is not limited to $f>-f_0$, but in the passband $|f|\le\Delta f/2\ll f_0$ it is correct.) With $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

The envelope is the step response of an ideal lowpass with $f_\mathrm g=\Delta f/2$: rise time $1/\Delta f=0.5$ s, overshoot 8.95 % (Fig. [5](#abb-5)). A narrow bandpass takes a long time to “settle”.

:::abbildung et3/k5bandpass 5
Response of the ideal bandpass ($f_0=10$ Hz, $\Delta f=2$ Hz) to a cosine at the center frequency that is switched on at $t=0$. Blue: the output signal; red: the envelope $\pm g_T(t)$. It rises in about 0.5 s and overshoots to 1.09.
:::

:::ltspice Switched-on carrier through a resonant circuit
An ideal bandpass cannot be built, but a series resonant circuit can. **Draw:** a `voltage` source at net `in`, then in series `ind` with `{L}`, `cap` with `{1/((2*pi*f0)**2*L)}` and `res` with `{2*pi*df*L}` to ground. The output `out` is the voltage across the resistor. With `.param f0=10 df=2 L=1` the center frequency is 10 Hz and the bandwidth between the $-3$-dB points is 2 Hz.

⁠**Check:** source value `AC 1` and `.ac lin 2001 5 15` show the maximum 1 at 10 Hz and the $-3$-dB points at 9.05 Hz and 11.05 Hz.

⁠**Experiment:** source `SINE(0 1 10 0 0 90)`, which is $\varepsilon(t)\cos(2\pi f_0t)$, and `.tran 0 3 0 0.1m`. The envelope rises without overshoot: the carrier peaks reach 0.72 at 0.2 s, 0.96 at 0.5 s and practically 1 after 1 s, almost exactly like $1-\mathrm{e}^{-t/0.16\,\mathrm s}$. The ideal bandpass, by contrast, overshoots to 1.09 (Fig. [5](#abb-5)). The reason is the same as for the lowpass in Stage [3](sprungantwort-und-einschwingzeit.html#stufe-3): the edges of the resonant circuit are soft, those of the ideal bandpass are vertical.
:::
