---
title: Stage 7: Discrete-time and periodic correlation
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260800
summary: For samples, the integral becomes a sum.
tags: fast correlation
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
For samples, the integral becomes a sum. With the DFT, correlations can be computed quickly.
:::

:::satz Theorem 7.1 (Discrete-time correlation)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{period }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

For sampled low-pass signals, $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ and $E_s=T\sum_n|s(nT)|^2$. A discrete-time energy signal is a square-summable sequence.

::::beispiel
$s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ for $m=-2,\dots,2$. Maximum $6=E_s$ at $m=0$, even, five values instead of three. Check with Wiener–Khinchin at $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.
::::

**Periodic correlation.** As with convolution ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)), the following holds for sequences with the period $M$:

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Computed with the FFT, this is called __fast correlation__. For the periodic correlation to reproduce the ordinary one, $M$ must be large enough. For $(1,2,1)$, $M=3$ gives the overlapped sequence $(6,5,5)$, whereas $M=5$ gives $(6,4,1,1,4)$, the ordinary ACF arranged cyclically.

**Power signals.** For signals of infinite energy, you average:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

If both signals are periodic with the same period, one period is sufficient, and the correlation function is periodic as well. Example: $A\cos(2\pi Ft+\varphi_0)$ has the ACF $\frac{A^2}{2}\cos(2\pi F\tau)$. The phase $\varphi_0$ has disappeared, and at $\tau=0$ the ACF equals the power $\frac{A^2}{2}$.

:::aufgabe Exercise 6 ★ Discrete ACF
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Verify the ACF of $(1,2,1)$ by hand.

</li>

<li>

Find the ACF of $(1,-1)$. What does $\varphi(\pm1)<0$ tell you about the signal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. A negative value at the shift 1 means that neighboring values tend to have opposite signs: the signal changes quickly. Consistent with this, $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ is zero at $f=0$ and maximal at $f=\frac12$: a high-pass signal.
:::
:::

:::aufgabe Exercise 7 ★★ ACF of a cosine
<span class="anker" id="aufg-7"></span>

Derive the ACF of $A\cos(2\pi Ft+\varphi_0)$ with [(7.4)](#gl-7-4) over one period. Why does $\varphi_0$ drop out, and what does this mean for measuring the phase with the ACF?

:::loesung
With $\omega=2\pi F$ and $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

The second integral runs over two full periods and is zero. The phase $\varphi_0$ only shifts the time origin, and averaging over all times knows no origin. The ACF of a single signal therefore cannot measure a phase. The phase difference of *two* signals, on the other hand, is revealed by the cross-correlation.
:::
:::
