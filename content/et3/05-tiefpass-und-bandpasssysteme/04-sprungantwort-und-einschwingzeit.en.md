---
title: Stage 3: Step response and rise time
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3250400
summary: How does the ideal lowpass respond to a step?
tags: sine integral, rise time
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
How does the ideal lowpass respond to a step? How fast does it rise, and how far does it overshoot?
:::

The step response is the running integral of the impulse response ([Chapter 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). With the __sine integral__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

this gives

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung Step response
Split the integral up to $t$ at 0. The part from $-\infty$ to 0 is half the area of $h$, that is, $\frac12H(0)=\frac12$, because $h$ is even. For the rest, substitute $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$: $\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$. The value $\operatorname{Si}(\infty)=\frac\pi2$ follows from the area theorem: $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$, so $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$.
:::

⁠**How to read it:** at $t=0$ the response is exactly $\frac12$; it begins even earlier (not causal) and tends to 1. The __rise time__ $t_e$ is defined as the duration of the rise of a ramp with the maximum slope of the step response. The maximum slope is $h(0)=2f_\mathrm g$, so

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

The step response overshoots by $8.95\,\%$ (at $t=\frac{1}{2f_\mathrm g}$). This is the Gibbs phenomenon from [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): a larger $f_\mathrm g$ shortens the rise time, but the overshoot stays the same (Fig. [1](#abb-1)).

:::abbildung et3/k5sprung 1
Step response of the ideal lowpass for $f_\mathrm g=1$ Hz and 2 Hz. Dashed: the ramp with the maximum slope; its rise lasts $t_e=1/(2f_\mathrm g)=0.5$ s. Both curves overshoot equally far, to 1.0895.
:::

:::frage Surely a lowpass with more bandwidth is “better”. So why doesn't the overshoot shrink?
Because it comes from the *shape* of the frequency response, not its width. The overshoot arises at the vertical edge at $f_\mathrm g$: all frequencies up to there pass in full, all above not at all. If you move the edge, it stays vertical, and the step response is merely compressed in time. The overshoot only gets smaller once the edge becomes soft (Stage [5](echomethode-und-pulsformfilter.html#stufe-5)).
:::

:::aufgabe Exercise 3 ★★ Sine integral
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Show $h_\varepsilon(0)=\frac12$ and $h_\varepsilon(\infty)=1$ using [(3.1)](#gl-3-1).

</li>

<li>

Where is the maximum of the step response? Hint: the derivative of the step response is the impulse response.

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$, $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$.

(b) The slope of the step response is $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$. It becomes zero for the first time at $2\pi f_\mathrm gt=\pi$ and changes there from positive to negative. So the maximum lies at $t=\frac{1}{2f_\mathrm g}$ and equals $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1.852}{\pi}=1.0895$.
:::
:::
