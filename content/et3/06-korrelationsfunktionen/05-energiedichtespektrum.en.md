---
title: Stage 4: Energy spectral density
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260500
summary: What is the Fourier transform of a correlation function?
tags: energy spectral density, cross energy spectral density
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
What is the Fourier transform of a correlation function? It shows how the energy is distributed over the frequencies.
:::

:::satz Theorem 4.1 (Wiener–Khinchin for energy signals)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**How to read it:** $|S(f)|^2$ is called the __energy spectral density__. It is real, never negative and, for real signals, even in $f$. The phase of the signal is lost: all signals with the same magnitude spectrum have the same ACF. $S^*G$ is called the __cross energy spectral density__. The derivation needs only the convolution theorem, time reversal and conjugation: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** At $\tau=0$ the ACF is the energy. With the area theorem:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Two orthogonal signals also have orthogonal spectra: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

::::beispiel the exponential pulse
$s(t)=\varepsilon(t)\mathrm{e}^{-t}$ has $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$, so $|S|^2=\frac{1}{1+(2\pi f)^2}$. This is also $\operatorname{Re}\{S\}$, and its inverse transform is the even part of the signal ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

The same value follows from $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ in the time domain and from $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ in the frequency domain. Figure [2](#abb-2) shows the signal, its ACF and both spectra.

:::abbildung et3/k6exp 2
Exponential pulse ($RC=1$ s). Left: the signal and its ACF $\frac12\mathrm{e}^{-|\tau|}$ (even, maximum $=E_s=\frac12$). Right: the magnitude spectrum and the energy spectral density, which decays faster: the energy is concentrated at low frequencies.
:::
::::

:::aufgabe Exercise 4 ★ Checking Parseval
<span class="anker" id="aufg-4"></span>

Compute the energy of $\operatorname{rect}(t)$ in the time domain, and from its spectrum with [(4.2)](#gl-4-2). Which well-known integral of the si function follows from this?

:::loesung
Time domain: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Frequency domain: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. Hence $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::
