---
title: Stage 2: A first system, the RC circuit
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / LTI Systems and Convolution
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Chapter 1: LTI Systems and Convolution
order: 3210300
summary: With the RC low-pass (Fig.
tags: frequency response
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
With the RC low-pass (Fig. [2](#abb-2)) we can work out how a system responds to two typical inputs: a complex exponential and a step.
:::

**The differential equation.** The current through $R$ is $(u_1-u_2)/R$. All of it flows into the capacitor and charges it, $C\,\dot u_2=(u_1-u_2)/R$. Rearranged:

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung 2
RC low-pass: input $u_1$, output $u_2$ across the capacitor. In the reference model $RC=1$ s.
:::

**Input $\mathrm{e}^{\mathrm{j}2\pi Ft}$: the output is a number times the input.** If $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$ is applied, the output in the steady state has the same form, only with a different amplitude and phase: $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. The number $H(F)$ depends on the frequency and is therefore called the __frequency response__. The reason is that differentiation does not change the form, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Substituting into [(2.1)](#gl-2-1):

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

AC analysis with phasors gives the same result: the capacitor has the impedance $1/(\mathrm{j}2\pi FC)$, and the circuit is a voltage divider,

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

The real voltage belonging to a phasor is $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$ (RMS phasor).

:::satz Theorem 2.1 (Transfer function of the RC low-pass)
<span class="anker" id="satz-2-1"></span>

With $x=2\pi FRC$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**How to read it:** $|H|$ tells you by what factor the amplitude shrinks, and $\varphi$ by what angle the oscillation lags. At $x=1$, that is, $F=1/(2\pi RC)=0.16$ Hz in the reference model, $|H|=0.707$ and $\varphi=-45^\circ$. At $x=10$, $|H|=0.0995$ and $\varphi=-84.3^\circ$ (Fig. [3](#abb-3)). **Limiting cases:** $F\to0$ gives $H\to1$ (the capacitor has time to charge fully); $F\to\infty$ gives $H\to0$ with $\varphi\to-90^\circ$ (the capacitor acts like a short circuit).

:::abbildung et3/k1bode 3
Magnitude and phase of the transfer function of the RC low-pass versus $x=2\pi FRC$ (logarithmic scale). Slow oscillations pass almost unchanged; fast ones are attenuated and lag by up to $90^\circ$.
:::

**The phase in general.** For an arbitrary complex number $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$,

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{integer}, \tag{2.4}$$

where $\arctan$ returns the principal value in $[-\pi/2,\pi/2]$.

:::frage Why does the phase formula need the extra term $\lambda\pi$?
$\arctan$ sees only the ratio $\operatorname{Im}/\operatorname{Re}$. The numbers $1+\mathrm{j}$ and $-1-\mathrm{j}$ have the same ratio 1, but lie in opposite quadrants. $\arctan1=45^\circ$ is correct for $1+\mathrm{j}$. For $-1-\mathrm{j}$ the true angle is $45^\circ+180^\circ=225^\circ$, equivalently $-135^\circ$ (with $l=-1$). Whenever the real part is negative, you have to add $\pi$.
:::

**Step input: the exponential curve.** At $t=0$ the voltage $u_1=1$ V is applied; the capacitor is empty. For $t\ge0$, Kirchhoff's voltage law with the current $i$ gives

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

Differentiating gives $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$, hence $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, and integrating gives

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

because at the first instant the whole voltage is across $R$. Kirchhoff's voltage law, $u_2=1-R\,i$, then gives

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

The mechanism: the fuller the capacitor, the less voltage is left for $R$, the smaller the charging current, and the more slowly the capacitor continues to fill. This feedback makes the curve exponential.

:::ltspice RC low-pass: step response and frequency response
⁠**Draw:** a `voltage` source at net `in`, `res` with `1Meg` from `in` to `out`, `cap` with `1u` from `out` to ground, so $RC=1$ s. Careful: SPICE reads `1M` as 1 milli; mega is written `Meg`.

⁠**Step:** source `PULSE(0 1 0 1u 1u 100)`, directive `.tran 5`. A measurement such as `.meas tran g1 FIND V(out) AT=1` gives exact values; the result appears in the SPICE Error Log (View, SPICE Error Log). Expected: 0.393 at 0.5 s, 0.632 at 1 s and 0.950 at 3 s, i.e. $1-\mathrm{e}^{-t}$ as in [(2.5)](#gl-2-5).

⁠**Frequency response:** source value `AC 1`, and instead of `.tran` the directive `.ac dec 100 0.01 100`. LTspice plots the magnitude in dB (solid) and the phase (dashed). At 0.159 Hz ($x=1$) they show $-3.0$ dB, i.e. $|H|=0.707$, and $-45^\circ$. Compare the values at $x=10$ with your result from Exercise [2](#aufg-2)(a).
:::

:::aufgabe Exercise 2 ★★ Frequency response and phase
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Compute $|H|$ and $\varphi$ of the RC low-pass for $x=0$, $1$ and $10$. Which frequency in Hz corresponds to $x=10$ in the reference model?

</li>

<li>

A signal $u_1(t)=\cos(2\pi Ft)$ with $x=1$ is applied. Write down $u_2(t)$. By how many seconds does $u_2$ lag if $RC=1$ s?

</li>

<li>

Use [(2.4)](#gl-2-4) to determine the phases of $-1-\mathrm{j}$, $-\mathrm{j}$ and $-2$.

</li>

</ol>

:::loesung
(a) $x=0$: $|H|=1$, $\varphi=0$. $x=1$: $|H|=0.707$, $\varphi=-45^\circ$. $x=10$: $|H|=0.0995$, $\varphi=-84.3^\circ$. $x=10$ means $F=10/(2\pi RC)=1.59$ Hz.

(b) $u_2(t)=0.707\cos(2\pi Ft-45^\circ)$ with $2\pi F=1/\mathrm s$, so $F=0.159$ Hz. It lags by $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0.785$ s.

(c) $-1-\mathrm{j}$: $\arctan1=45^\circ$, real part negative, so add $180^\circ$: $225^\circ$, equivalently $-135^\circ$. $-\mathrm{j}$: real part zero, imaginary part negative; $\arctan(\operatorname{Im}/\operatorname{Re})$ tends to $-90^\circ$, so the phase is $-90^\circ$. $-2$: $\arctan0=0$, real part negative, so $180^\circ$.
:::
:::
