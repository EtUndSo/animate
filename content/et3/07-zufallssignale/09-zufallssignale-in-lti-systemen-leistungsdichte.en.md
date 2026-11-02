---
title: Stage 8: Random signals in LTI systems, power spectrum
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270900
summary: What does an LTI system do to a random signal?
tags: power spectral density
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
What does an LTI system do to a random signal? Each sample function is convolved. Simple rules therefore hold for the averages.
:::

**Mean value.** For each sample function, ${}^kg={}^ks*h$. The expected value is linear and may be moved into the convolution integral:

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

The mean value is transmitted like a DC component.

:::satz Theorem 8.1 (Wiener–Lee for stationary processes)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

with the impulse ACF (deterministic ACF) $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ of the impulse response and the __power spectral density__ $\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$. The power is

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung Wiener–Lee
Write out both convolution integrals, with different variables:

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

Move the expected value into the double integral. For a stationary process, $\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$. With $\vartheta=\beta-\alpha$:

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

In the frequency domain, $\varphi^E_{hh}$ becomes $|H|^2$ ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).
:::

⁠**How to read it:** $\Phi_{ss}(f)$ indicates how the power is distributed over the frequencies. It is real, never negative and, for real signals, even. An LTI system multiplies the power at each frequency by $|H(f)|^2$; its phase plays no role. This is the same rule as for energy signals in [Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html), now for processes. (Note: strictly speaking, $\Phi_{ss}$ is defined as the limit $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ over short-time spectra of segments of duration $T$. That this is the same as the transform of the ACF is the actual statement of the Wiener–Khinchin theorem.)

:::ltspice Noise with a mean value through low-pass and high-pass
⁠**Draw:** a behavioural source `bv` at net `s` with `V=1+white(1e3*time)`. `white(x)` returns random values between $-0.5$ and $0.5$, a new one at every integer $x$, joined smoothly, so here every millisecond. Connected to it in parallel, an RC low-pass (`res` with `1Meg` to `tp`, `cap` with `1u` to ground) and a CR high-pass (`cap` with `1u` to `hp`, `res` with `1Meg` to ground).

⁠**Directive:** `.tran 0 200 0 0.1m`.

⁠**Reading:** Zoom to 20 s to 200 s, i.e. to the time after the transient. A click on a trace name while holding the Ctrl key shows the mean (Average) and the RMS value over the visible range.

⁠**What you see:** The input has the mean 1 V. Compare the means of `V(tp)` and `V(hp)` with your result from Exercise [7](#aufg-7). The fluctuations are much smaller at the low-pass: plot `V(s)-1` and `V(tp)-1`, their RMS values are about 0.25 and 0.01. The low-pass passes only roughly the part of the broad power density below $1/(2\pi RC)=0.16$ Hz, and by [(8.3)](#gl-8-3) the power is the area under the power density.
:::

:::aufgabe Exercise 7 ★ Mean value through a filter
<span class="anker" id="aufg-7"></span>

Noise with the mean value 1 V passes through an RC low-pass filter and through a CR high-pass filter. What mean values do the outputs have, and why?

:::loesung
RC low-pass filter: $H(0)=1$, mean value 1 V. CR high-pass filter: $H(0)=0$, mean value 0. The capacitor does not pass direct current, so the DC component is blocked.
:::
:::
