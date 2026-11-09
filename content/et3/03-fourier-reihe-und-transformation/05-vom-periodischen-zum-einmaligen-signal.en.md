---
title: Stage 4: From periodic to non-repeating signals
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230500
summary: A single pulse is not periodic.
tags: spectral density
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
A single pulse is not periodic. But it can be regarded as a periodic signal with an infinitely long period. In the process, the sum becomes an integral.
:::

**The idea.** Continue a pulse $s(t)$ of duration less than $T$ periodically. The coefficients of the series are then values of a fixed function:

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

If you double the period, the line spacing $F$ is halved, and the lines sample the same envelope $S(f)$ twice as densely (Fig. [4](#abb-4)). In the limit $T\to\infty$, the spacing $F$ becomes the differential $\mathrm{d} f$, and the sum $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ becomes the integral.

:::abbildung et3/k3grenz 4
A rectangular pulse $\operatorname{rect}(t)$, continued periodically with $T=2$ s and $T=4$ s. The Fourier coefficients multiplied by $T$ lie on the same envelope $S(f)=\operatorname{si}(\pi f)$, with the spacing $1/T$. As $T\to\infty$ they fill the curve without gaps.
:::

:::satz Theorem 4.1 (Fourier transform)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

Shorthand: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ or $S(f)=\mathcal{F}\{s(t)\}$.
:::

⁠**How to read it:** $S(f)$ is a __spectral density__: weight per frequency interval. If $s$ is a voltage in V, $S$ has the unit V/Hz. The inverse transform builds the signal from all oscillations, each with the weight $S(f)\,\mathrm{d} f$. A sufficient condition for existence is $\int|s(t)|\mathrm{d} t<\infty$. The Fourier transform is the Laplace transform on the imaginary axis, $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$, provided the axis lies in the region of convergence ([Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)).

⁠**Convolution becomes a product.** As in [Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html): $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$. From $s*\delta=s$ it follows that $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, so $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: the Dirac impulse contains all frequencies with equal weight.

::::beispiel the exponential pulse
The impulse response of the RC circuit, $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$:

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

This is the same frequency response as from AC analysis ([Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). So the impulse response contains all the information about the frequency behavior.
::::

:::frage What is the difference between $S_p(k)$ and $S(f)$, apart from the fact that one is discrete?
The unit. $S_p(k)$ is an amplitude (V): the $k$th harmonic really has this strength. $S(f)$ is a density (V/Hz): in a non-repeating signal no single frequency has a finite amplitude; only a frequency band $\Delta f$ carries approximately $S(f)\,\Delta f$. That is why $S_p(k)=F\cdot S(kF)$: each line represents a band of width $F$.
:::

:::aufgabe Exercise 4 ★ The two-sided exponential pulse
<span class="anker" id="aufg-4"></span>

Compute $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$ for $a>0$ by splitting the integral into $t<0$ and $t>0$. Show that the result is real and even, and explain this with the symmetry of the signal.

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

Real and even in $f$. This must be so: the signal is real and even, so its odd part is zero, and hence so is $\operatorname{Im} S$ (Stage [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)).
:::
:::
