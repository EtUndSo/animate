---
title: Stage 8: Integrating and differentiating
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / LTI Systems and Convolution
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Chapter 1: LTI Systems and Convolution
order: 3210900
summary: The integrator and the differentiator are LTI systems.
tags: integrator, differentiator, doublet
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
The integrator and the differentiator are LTI systems. They link the step response to the impulse response, and they let you obtain the impulse response of the RC circuit from its step response.
:::

**The integrator.** If $\delta$ in [(7.6)](der-dirac-impuls.html#gl-7-6) is replaced by an arbitrary $s$, the same calculation gives

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

A system with the impulse response $\varepsilon(t)$ forms the running integral of its input; it is called an __integrator__. Read with the roles swapped ($\varepsilon*s$), [(8.1)](#gl-8-1) says: **the step response of a system is the running integral of its impulse response.** Check with the RC circuit: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, exactly [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5). Two independent routes, the differential equation and convolution, give the same result.

**The differentiator.** An integrator followed by a __differentiator__ leaves every signal unchanged; the cascade is ideally distortion-free. The impulse response of the differentiator is therefore the distribution $\delta'(t)$ (the __doublet__), defined by

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

Approximately, $\delta'$ is a narrow double rectangular pulse: first a rectangle of height $+1/T_0^2$, then one of height $-1/T_0^2$, each $T_0$ wide. It is drawn as a pair of arrows, one pointing up and one pointing down.

**Impulse response = derivative of the step response.** Because $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ and the system is linear and time-invariant, $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{step response})$. For the RC circuit, with the product rule:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

The second term vanishes by [(7.2)](der-dirac-impuls.html#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. The mechanism behind this: the step response of the RC circuit does not jump, because the capacitor needs time to charge. Only a step response that jumps produces a Dirac impulse in $h$ (Exercise [9](#aufg-9)).

:::aufgabe Exercise 9 ★★ High-pass: a Dirac impulse in the impulse response
<span class="anker" id="aufg-9"></span>

If $R$ and $C$ are swapped, the output voltage is taken across $R$ (CR high-pass, $RC=1$ s). Its step response is $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Explain the step response through the mechanism: what is across $R$ at the first instant, and what after a long time?

</li>

<li>

Find the impulse response by differentiation. What does the Dirac component mean physically?

</li>

<li>

Check: integrating the impulse response must give back the step response.

</li>

</ol>

:::loesung
(a) At the first instant the capacitor is empty, so there is no voltage across it. The full 1 V is across $R$. The current then charges the capacitor; its voltage rises as $1-\mathrm{e}^{-t}$, and $\mathrm{e}^{-t}$ remains across $R$. After a long time the capacitor is full, no current flows, and no voltage is left across $R$.

(b) Product rule:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Here the step response jumps from 0 to 1 at $t=0$, so the Dirac component remains. Physically: an infinitely short impulse passes straight through, because the capacitor cannot build up a voltage in zero time. The charge that the impulse has put on the capacitor then flows off again through $R$, in the opposite direction: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::
