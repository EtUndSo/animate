---
title: Lowpass and Bandpass Systems
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3250100
summary: Distortionless transmission, ideal lowpass, complex envelope and group delay
tags: phase delay, group delay, signal duration, sine integral, rise time, echo, raised-cosine filter, equivalent lowpass
lang: en
---

## What this is about

Almost every transmission is meant to deliver a signal as unchanged as possible, but only within a certain frequency range: a lowpass passes the low frequencies, a bandpass passes a band around a carrier frequency. This article asks: *What exactly does “unchanged” mean, what does a sharply limited band cost, and how do you calculate with signals that ride on a high-frequency carrier?*

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

Undistorted means: only amplified and delayed. This requires a constant magnitude and a phase that falls linearly with frequency.

</li>

<li>

A sharply band-limited (ideal) lowpass is not causal, overshoots by about 9 % at steps and needs a rise time of $1/(2f_\mathrm g)$. Softer edges reduce the overshoot at the expense of sharpness.

</li>

<li>

A bandpass signal is a lowpass signal (the complex envelope) on a carrier. You calculate with the envelope as with a lowpass signal: it is delayed by the group delay, the carrier by the phase delay.

</li>

</ol>
:::

**One principle behind all the results.**

| Result | Where it comes from |
|---|---|
| Distortionless system | every oscillation amplified equally and delayed by the same time (Stage [1](#stufe-1)) |
| Phase and group delay | delay of the carrier and of the envelope, respectively (Stages [1](#stufe-1), [11](#stufe-11)) |
| Signal duration $\cdot$ bandwidth $=$ const. | similarity theorem (Stage [2](#stufe-2)) |
| Overshoot 21.7 % and 8.95 % | side lobes of the si function, Gibbs (Stages [2](#stufe-2), [3](#stufe-3)) |
| Causal approximation, window design | truncating the impulse response = convolution in the spectrum (Stages [4](#stufe-4), [6](#stufe-6)) |
| Pulse-shaping filter | soft edge in the spectrum, rapidly decaying impulse response (Stage [5](#stufe-5)) |
| Equivalent lowpass, complex envelope | shift the positive frequencies to zero (Stages [7](#stufe-7), [8](#stufe-8)) |
| Quadrature circuit, bandpass sampling | calculate the bandpass in the lowpass domain (Stage [10](#stufe-10)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
<ul>

<li>

⁠**RC lowpass** with $RC=1$ s as in Parts 1 to 3.

</li>

<li>

⁠**Ideal lowpass** with $f_\mathrm g=1$ Hz (also 2 Hz for comparison).

</li>

<li>

⁠**Ideal bandpass** with the center frequency $f_0=10$ Hz and the bandwidth $\Delta f=2$ Hz.

</li>

<li>

⁠**Discrete-time lowpass** with $f_\mathrm g=0.2$ (normalized to the sampling rate) and 21 coefficients.

</li>

</ul>

The script `rechnung_kap5.py` recomputes the numbers and curves. $\operatorname{si}(x)=\sin(x)/x$ as in [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::

## Stage 1: The distortionless system

<span class="anker" id="stufe-1"></span>

:::zweck
What exactly should a “good” transmission achieve? And with which characteristic quantities do you measure how far a system deviates from it?
:::

**The idea.** A signal has arrived undistorted if it is only louder or quieter and later, but its shape is the same:

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

In the spectrum this means: every oscillation is multiplied by the same factor $h_0$, and every one is shifted by the same time $t_0$. At the frequency $f$, a time shift $t_0$ is the angle $2\pi ft_0$. That is why the phase $\varphi(f)=-2\pi t_0f$ must be a straight line through the origin.

:::definition Definition 1.1 (Characteristic quantities of an LTI system)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{Attenuation:} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{or}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{Phase attenuation angle:} && b(f)=-\varphi(f),\\ &\text{Phase delay:} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{Group delay:} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**How to read it:** the __phase delay__ is the delay of a single oscillation of frequency $f$. The __group delay__ is the delay of a group of neighboring frequencies, that is, of an envelope (Stage [11](#stufe-11)). For the distortionless system, $a$, $t_\mathrm p$ and $t_\mathrm g$ are constant and $t_\mathrm p=t_\mathrm g=t_0$.

**Example: the RC circuit.** With $\varphi=-\arctan(2\pi f\,RC)$ and $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

For $f\to0$ both are $RC=1$ s. At $f=0.159$ Hz ($2\pi fRC=1$), $t_\mathrm p=0.785$ s, $t_\mathrm g=0.5$ s and $a=3.0$ dB. So the RC circuit is not distortionless: its attenuation depends on frequency, and different frequencies arrive at different times.

:::ltspice Reading attenuation and delays of the RC circuit
⁠**Draw:** the RC circuit (`res` with `1Meg`, `cap` with `1u`), source value `AC 1`, directive `.ac dec 100 0.01 10`.

⁠**Reading:** The left axis shows $20\lg|H|=-a$ in dB. Move the mouse onto the right axis (phase) until the pointer turns into a ruler, click and choose “Group Delay”: the axis then shows $t_\mathrm g(f)$ as in [(1.5)](#gl-1-5). You compute the phase delay from the phase, $t_\mathrm p=-\varphi/(2\pi f)$ with $\varphi$ in radians.

⁠**What you see:** Towards low frequencies $t_\mathrm g$ approaches 1 s. At 0.159 Hz you read $a=3.0$ dB, $\varphi=-45^\circ$ and $t_\mathrm g=0.5$ s, hence $t_\mathrm p=0.785$ s. Compare the values at $2\pi fRC=10$ with your result from Exercise [1](#aufg-1)(b).
:::

:::aufgabe Exercise 1 ★ Delays of the RC circuit
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Derive $t_\mathrm g$ of the RC circuit from [(1.5)](#gl-1-5).

</li>

<li>

Compute $t_\mathrm p$, $t_\mathrm g$ and $a$ at $2\pi fRC=10$. In which frequency range is the RC circuit approximately distortionless?

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$, $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$, so $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$.

(b) At $2\pi fRC=10$: $t_\mathrm p=\frac{\arctan10}{10}RC=0.147$ s, $t_\mathrm g=\frac{RC}{101}=0.0099$ s, $a=20.0$ dB. The RC circuit is approximately distortionless only for $2\pi fRC\ll1$, that is, far below 0.16 Hz: there $|H|\approx1$ and $t_\mathrm p\approx t_\mathrm g\approx RC$.
:::
:::

## Stage 2: The ideal lowpass

<span class="anker" id="stufe-2"></span>

:::zweck
The ideal lowpass passes all frequencies up to $f_\mathrm g$ unchanged and blocks all frequencies above. This stage shows what this sharp cutoff means in the time domain.
:::

:::satz Theorem 2.1 (Ideal lowpass)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**How to read it:** the impulse response extends to infinity in both directions. So the ideal lowpass is *not causal*: it would have to respond to an impulse before the impulse arrives. It is a mathematical limiting object that can only be approximated (Stages [4](#stufe-4), [6](#stufe-6)).

**Duration and bandwidth.** The __signal duration__ $t_m$ of an impulse response is taken to be the width of a rectangle with the same height $h_{\max}$ and the same area:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

For the ideal lowpass, $H(0)=1$ and $h_{\max}=2f_\mathrm g$, so $t_m=\frac{1}{2f_\mathrm g}$ and $f_\mathrm g\cdot t_m=\frac12$. In general, lowpass filters satisfy $f_\mathrm g\cdot t_m=\text{const.}$: double the bandwidth means half the response duration. This is the similarity theorem from [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

**Overshoot.** For the si function, the ratio of the side maximum with the largest magnitude, $a_1$, to the main maximum $a_0$ is

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21.7\,\%,$$

independent of $f_\mathrm g$ (the first side minimum of $\operatorname{si}(\pi u)$ lies at $u=1.43$ and is $-0.217$). Changing $f_\mathrm g$ only compresses the curve; it does not change its shape.

:::aufgabe Exercise 2 ★ Ideal lowpass for speech
<span class="anker" id="aufg-2"></span>

An ideal lowpass with $f_\mathrm g=4$ kHz. What are the signal duration of the impulse response and the overshoot? What changes for $f_\mathrm g=8$ kHz?

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s, overshoot 21.7 %. At 8 kHz the signal duration halves to 62.5 µ s. The overshoot remains 21.7 %, because the impulse response is only compressed.
:::
:::

## Stage 3: Step response and rise time

<span class="anker" id="stufe-3"></span>

:::zweck
How does the ideal lowpass respond to a step? How fast does it rise, and how far does it overshoot?
:::

The step response is the running integral of the impulse response ([Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). With the __sine integral__

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

The step response overshoots by $8.95\,\%$ (at $t=\frac{1}{2f_\mathrm g}$). This is the Gibbs phenomenon from [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): a larger $f_\mathrm g$ shortens the rise time, but the overshoot stays the same (Fig. [1](#abb-1)).

:::abbildung et3/k5sprung
Step response of the ideal lowpass for $f_\mathrm g=1$ Hz and 2 Hz. Dashed: the ramp with the maximum slope; its rise lasts $t_e=1/(2f_\mathrm g)=0.5$ s. Both curves overshoot equally far, to 1.0895.
:::

:::frage Surely a lowpass with more bandwidth is “better”. So why doesn't the overshoot shrink?
Because it comes from the *shape* of the frequency response, not its width. The overshoot arises at the vertical edge at $f_\mathrm g$: all frequencies up to there pass in full, all above not at all. If you move the edge, it stays vertical, and the step response is merely compressed in time. The overshoot only gets smaller once the edge becomes soft (Stage [5](#stufe-5)).
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

## Stage 4: Causal approximation

<span class="anker" id="stufe-4"></span>

:::zweck
How do you build something that comes as close as possible to the ideal lowpass? You delay the impulse response and cut off the rest.
:::

**The idea.** Shift $h(t)$ to the right by $t_0$ until the part at $t<0$ is negligible, and cut that part off. The envelope of the si function falls off like $1/(2\pi f_\mathrm g|t|)$. If it is to stay below 1 % of the maximum before $t=0$, you need $t_0\approx16/f_\mathrm g$. With a symmetric window of width $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**How to read it:** cutting off is a multiplication by a window, and so in the spectrum a convolution with the window's si spectrum. The sharp edge is smeared out and acquires ripples. The factor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ is the delay: the causal filter has a linear phase; it delays all frequencies equally (Fig. [2](#abb-2)). The larger $t_0$, the narrower the transition, but the later the response.

:::abbildung et3/k5kausal
Magnitude of the causally windowed lowpass with $f_\mathrm g=1$ Hz and $t_0=3$ s (blue); dashed: the ideal. At the edge a transition region forms with $|H_k(f_\mathrm g)|=0.49$, and before it there are ripples up to 1.10.
:::

:::aufgabe Exercise 4 ★★ How much delay does causality cost?
<span class="anker" id="aufg-4"></span>

A lowpass with $f_\mathrm g=1$ kHz is to be approximated causally. The shifted ideal lowpass response is to stay below 1 % of its maximum before $t=0$, that is, in the part that is cut off.

<ol class="al">

<li>

What is the minimum value of $t_0$?

</li>

<li>

What does this mean for a telephone call through a chain of ten such filters?

</li>

</ol>

:::loesung
(a) The envelope condition $\frac{1}{2\pi f_\mathrm g|t|}<0.01$ requires $|t|>\frac{100}{2\pi f_\mathrm g}=15.9$ ms. So $t_0\approx16$ ms.

(b) Ten filters delay by about 0.16 s. In a conversation this is noticeable as a delay. The causality of a steep filter costs time, and the narrower the band, the more time it costs.
:::
:::

## Stage 5: Echo method and pulse-shaping filters

<span class="anker" id="stufe-5"></span>

:::zweck
How do you design a lowpass with less overshoot? You assemble the impulse response from shifted si functions and choose their weights.
:::

**Echo method.** By the sampling theorem, every impulse response of a lowpass up to $f_\mathrm g=\frac{1}{2T}$ is an si series:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

Each sample $h(nT)$ is an __echo__: an si function shifted by $nT$. In the spectrum this becomes a Fourier series in $f$. If $h$ is real and even, $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$.

**Pulse-shaping filter.** Two echoes with the amplitude $a$ at a distance of $\pm T$ are added to the main component $\operatorname{si}(\pi t/T)$. For $a=\frac12$ the side oscillations largely cancel, and the spectrum gets a cosine-shaped, soft edge:

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

This is the __raised-cosine filter__ (cosine roll-off filter). Its overshoot is 2.7 % instead of 21.7 %; in exchange, the main lobe is twice as wide (first zero at $2T$ instead of $T$). Figure [3](#abb-3) shows both impulse responses normalized to the same area.

:::abbildung et3/k5pulsform
Impulse responses of the ideal lowpass and of the pulse-shaping filter (both with the area $T$). The pulse-shaping filter decays much faster: its largest side maximum is 2.7 % of the main maximum instead of 21.7 %.
:::

**Transversal filter (tapped delay line).** A sum of delayed, weighted copies is built with a chain of delay elements whose taps are weighted and added. So that no element has to reach into the future, everything is delayed together. This is the same structure as an FIR filter ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

:::aufgabe Exercise 5 ★★ The raised-cosine filter
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Derive $H(f)$ in [(5.3)](#gl-5-3) from [(5.1)](#gl-5-1).

</li>

<li>

What is the value of $H$ at $f=0$ and at $f=f_\mathrm g=\frac{1}{2T}$? Why is the edge smooth there?

</li>

</ol>

:::loesung
(a) At $t=mT$, $\operatorname{si}(\pi(t\pm T)/T)$ equals 1 only for $m=\mp1$ and is zero otherwise. So $h(0)=1$, $h(\pm T)=\frac12$, and all other $h(nT)=0$. By [(5.1)](#gl-5-1): $H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$.

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. The slope $-2\pi T^2\sin(2\pi Tf)$ is also zero at $f=\frac{1}{2T}$. The frequency response goes to zero without a jump and without a kink. The smoother the spectrum, the faster the impulse response decays ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::

## Stage 6: Discrete-time lowpass filters, window design

<span class="anker" id="stufe-6"></span>

:::zweck
How do you design a digital lowpass? Exactly like the causal analog one: take the ideal lowpass, delay it, truncate it with a window.
:::

The ideal discrete-time lowpass has the periodically repeated rectangular frequency response and the impulse response

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

so in the reference model ($f_\mathrm g=0.2$) $h(0)=0.4$, $h(\pm1)=0.303$, $h(\pm2)=0.094$, $h(\pm3)=-0.062$. It, too, is not causal. You multiply it by a window $w(n)$ of $2N+1$ values, shift it by $N$ and obtain an FIR filter with linear phase. The window determines the result (Fig. [4](#abb-4)):

<ul>

<li>

⁠**Rectangular window:** sharpest transition, but high side lobes. In the reference model ($N=10$), the stopband from $f=0.3$ on still reaches $-26.6$ dB, and the passband fluctuates by about $\pm0.5$ dB.

</li>

<li>

⁠**Hann window:** softer transition, but a much deeper stopband: from $f=0.3$ on at most $-45.9$ dB, passband flat to within $0.05$ dB.

</li>

</ul>

The reason is the same as for the short-time Fourier transform in [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): the spectrum of the window is convolved with the ideal, and the hard edges of the rectangle produce slowly decaying side lobes.

:::abbildung et3/k5fenster
Magnitude response of two FIR lowpass filters with $f_\mathrm g=0.2$ and 21 coefficients. Rectangular window: steep edge, from $f=0.3$ on attenuation only down to $-26.6$ dB. Hann window: shallower edge, from $f=0.3$ on at most $-45.9$ dB.
:::

:::aufgabe Exercise 6 ★ Half-band filter
<span class="anker" id="aufg-6"></span>

Compute the coefficients $h(0)$ to $h(3)$ of the ideal discrete-time lowpass with $f_\mathrm g=0.25$. What do you notice, and why does this save computation in an FIR filter?

:::loesung
$h(n)=0.5\operatorname{si}(\pi n/2)$: $h(0)=0.5$, $h(\pm1)=\frac1\pi=0.318$, $h(\pm2)=0$, $h(\pm3)=-\frac{1}{3\pi}=-0.106$. All even coefficients except $h(0)$ are zero, because $\sin(\pi n/2)=0$ for even $n$. In the FIR filter these multiplications are dropped, almost half of them.
:::
:::

## Stage 7: The ideal bandpass and its equivalent lowpass

<span class="anker" id="stufe-7"></span>

:::zweck
A bandpass passes a band around the center frequency $f_0$. This stage shows that it can be described completely by a lowpass and the frequency $f_0$.
:::

**Ideal bandpass.** Two rectangles of width $\Delta f$ at $\pm f_0$ ($f_0>\Delta f/2$):

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

The impulse response is an oscillation at $f_0$ whose envelope is the impulse response of a lowpass with the bandwidth $\Delta f/2$. The modulation rule from [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) explains this: it is a lowpass whose spectrum is shifted to $\pm f_0$.

**Equivalent lowpass.** For a real impulse response, $H(-f)=H^*(f)$; the negative half contains nothing new. Keep only the positive frequencies, double them and shift them to the left by a carrier frequency $f_0$. The result is the __equivalent lowpass__ $H_T(f)$:

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{for}\ f\le-f_0. \tag{7.2}$$

$H_T$ need not be symmetric about $f=0$, so its impulse response $h_T(t)$ can be complex. If there is an $f_0$ for which $H_T(-f)=H_T^*(f)$ holds (so that $h_T$ is real), the bandpass is called __symmetric__. For the ideal bandpass with $f_0$ at the center, $H_T(f)=2\operatorname{rect}(f/\Delta f)$ and $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, real and even. This is a special case: even symmetric bandpass filters generally have an imaginary part in the spectrum.

:::aufgabe Exercise 7 ★★ Equivalent lowpass with a different reference
<span class="anker" id="aufg-7"></span>

Ideal bandpass from 9 to 11 Hz.

<ol class="al">

<li>

Determine $H_T$ and $h_T$ for $f_0=10$ Hz.

</li>

<li>

Determine $H_T$ and $h_T$ for $f_0=9$ Hz. Why is $h_T$ complex now? Do both describe the same bandpass?

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz: after the shift, the band lies symmetrically from $-1$ to $1$ Hz. $H_T=2\operatorname{rect}(f/2)$, $h_T=4\operatorname{si}(2\pi t)$, real.

(b) $f_0=9$ Hz: the band lies from 0 to 2 Hz. $H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$, $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$. Complex, because $H_T$ is not symmetric about $f=0$. Both describe the same bandpass: $\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$, the same as in (a) and as [(7.1)](#gl-7-1).
:::
:::

## Stage 8: Complex envelope and quadrature components

<span class="anker" id="stufe-8"></span>

:::zweck
What holds for systems also holds for signals: a bandpass signal is a lowpass signal on a carrier. This stage shows the different ways of writing this down.
:::

Transforming [(7.2)](#gl-7-2) back with the modulation rule gives $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$, and so, because $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ is called the __complex envelope__, $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ the __complex carrier__. Half their product is the analytic component from [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, so $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Theorem 8.1 (Quadrature representation)
<span class="anker" id="satz-8-1"></span>

With $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ and the Hilbert transform $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**How to read it:** $s_{Tr}$ and $s_{Ti}$ are called __quadrature components__ (the in-phase and the quadrature component): one modulates the cosine of the carrier, the other its sine. $|s_T|$ is the __envelope__, which you see on an oscilloscope as the “outline” of the signal, and $\varphi_T$ is the phase deviation of the carrier. If the complex envelope is real (symmetric case), $s(t)=s_T(t)\cos(2\pi f_0t)$: an amplitude-modulated cosine.

:::herleitung Quadrature components
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. For [(8.3)](#gl-8-3): $2s_+=s+\mathrm{j}\hat s$ ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), so

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Exercise 8 ★★ Determining complex envelopes
<span class="anker" id="aufg-8"></span>

Determine $s_T$, $s_{Tr}$, $s_{Ti}$ and $|s_T|$ with respect to $f_0=10$ Hz for (a) $s(t)=\bigl[1+0.5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0.3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Check (c) with [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0.5\cos(2\pi t)$, real: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0.5\cos(2\pi t)$ between 0.5 and 1.5. An amplitude-modulated cosine.

(b) $s_T=\mathrm{e}^{\mathrm{j}0.3}$: $s_{Tr}=\cos0.3=0.955$, $s_{Ti}=\sin0.3=0.296$, $|s_T|=1$. The envelope is constant; only the phase is shifted by 0.3.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$, so $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Check: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::

## Stage 9: Bandpass signal through a bandpass system

<span class="anker" id="stufe-9"></span>

:::zweck
What the envelopes are good for: how a bandpass acts on a bandpass signal can be calculated entirely in the lowpass domain.
:::

:::satz Theorem 9.1 (Transmission in the equivalent lowpass domain)
<span class="anker" id="satz-9-1"></span>

If $S_T$ and $H_T$ both satisfy [(7.2)](#gl-7-2) (nothing below $-f_0$), then the envelope of the output satisfies

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Transmission
Multiplying out $G=S\cdot H$ with both representations [(7.2)](#gl-7-2) gives four products. The mixed ones, such as $S_T(f-f_0)H_T^*(-f-f_0)$, are zero: the first factor lives at positive frequencies, the second at negative ones. What remains is $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. Comparing this with $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ gives $G_T=\frac12S_TH_T$.
:::

⁠**How to read it:** the factor $\frac12$ compensates for the fact that $S_T$ and $H_T$ were both doubled. Otherwise it is the familiar convolution theorem, just for the envelopes. The carrier need not be included in the calculation at all.

**Example: switched-on cosine through the ideal bandpass.** $s(t)=\varepsilon(t)\cos(2\pi f_0t)$ with $f_0=10$ Hz, bandpass with $\Delta f=2$ Hz around $f_0$. The envelope of the input is $s_T\approx\varepsilon(t)$. (Approximation: the spectrum of the step is not limited to $f>-f_0$, but in the passband $|f|\le\Delta f/2\ll f_0$ it is correct.) With $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

The envelope is the step response of an ideal lowpass with $f_\mathrm g=\Delta f/2$: rise time $1/\Delta f=0.5$ s, overshoot 8.95 % (Fig. [5](#abb-5)). A narrow bandpass takes a long time to “settle”.

:::abbildung et3/k5bandpass
Response of the ideal bandpass ($f_0=10$ Hz, $\Delta f=2$ Hz) to a cosine at the center frequency that is switched on at $t=0$. Blue: the output signal; red: the envelope $\pm g_T(t)$. It rises in about 0.5 s and overshoots to 1.09.
:::

:::ltspice Switched-on carrier through a resonant circuit
An ideal bandpass cannot be built, but a series resonant circuit can. **Draw:** a `voltage` source at net `in`, then in series `ind` with `{L}`, `cap` with `{1/((2*pi*f0)**2*L)}` and `res` with `{2*pi*df*L}` to ground. The output `out` is the voltage across the resistor. With `.param f0=10 df=2 L=1` the center frequency is 10 Hz and the bandwidth between the $-3$-dB points is 2 Hz.

⁠**Check:** source value `AC 1` and `.ac lin 2001 5 15` show the maximum 1 at 10 Hz and the $-3$-dB points at 9.05 Hz and 11.05 Hz.

⁠**Experiment:** source `SINE(0 1 10 0 0 90)`, which is $\varepsilon(t)\cos(2\pi f_0t)$, and `.tran 0 3 0 0.1m`. The envelope rises without overshoot: the carrier peaks reach 0.72 at 0.2 s, 0.96 at 0.5 s and practically 1 after 1 s, almost exactly like $1-\mathrm{e}^{-t/0.16\,\mathrm s}$. The ideal bandpass, by contrast, overshoots to 1.09 (Fig. [5](#abb-5)). The reason is the same as for the lowpass in Stage [3](#stufe-3): the edges of the resonant circuit are soft, those of the ideal bandpass are vertical.
:::

## Stage 10: Quadrature circuit and bandpass sampling

<span class="anker" id="stufe-10"></span>

:::zweck
How are the quadrature components obtained in practice? And how many samples does a bandpass signal need?
:::

**Quadrature circuit.** If you multiply a bandpass signal by $\cos(2\pi f_0t)$ and filter it with a lowpass, $\frac12s_{Tr}$ remains. With $-\sin(2\pi f_0t)$, $\frac12s_{Ti}$ remains. The reason is trigonometric:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{at }2f_0,\text{ removed by the lowpass}},$$

and likewise $-s\sin=\frac12s_{Ti}+(\text{components at }2f_0)$. The prerequisite is that the band ends below $2f_0$. In the lowpass domain you then filter with four lowpass filters ($h_{Tr}$, $\pm h_{Ti}$) according to [(9.1)](#gl-9-1). At the output you modulate back onto the carrier according to [(8.2)](#gl-8-2), or you form the envelope $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (Fig. [6](#abb-6)).

:::abbildung et3/k5quadratur
Quadrature demodulator: it extracts the two quadrature components, that is, the complex envelope, from a bandpass signal.
:::

**Sampling theorem for bandpass signals.** With respect to the center frequency, a bandpass signal of bandwidth $\Delta f$ has quadrature components that are lowpass signals up to $\Delta f/2$. Each of them can be sampled at $1/T=\Delta f$:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

In total you need $2\Delta f$ values per second, as many as for a lowpass signal with the cutoff frequency $\Delta f$. So what matters is the bandwidth, not the highest frequency.

:::aufgabe Exercise 9 ★★ Sampling a radio signal
<span class="anker" id="aufg-9"></span>

A signal occupies the band from 10.0 to 10.2 MHz.

<ol class="al">

<li>

What sampling rate would the ordinary sampling theorem require?

</li>

<li>

With the quadrature circuit, how many samples per second suffice in total, and at what rate is each branch sampled?

</li>

</ol>

:::loesung
(a) At least $2\cdot10.2=20.4$ MHz.

(b) $\Delta f=0.2$ MHz. Each branch is sampled at 0.2 MHz ($T=5$ µ s), together 0.4 MHz, about fifty times less.
:::
:::

## Stage 11: Phase and group delay in a bandpass

<span class="anker" id="stufe-11"></span>

:::zweck
Why are there two delays? Because the carrier and the envelope can be delayed differently.
:::

**The idea.** Let a bandpass have a constant magnitude and a slightly curved phase in the passband. Around $f_0$, approximate the phase by its tangent:

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

with $t_\mathrm p=t_\mathrm p(f_0)$ and $t_\mathrm g=t_\mathrm g(f_0)$ from [(1.4)](#gl-1-4) and [(1.5)](#gl-1-5). In the lowpass domain ($f-f_0\to f$) this is $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$: a constant phase and a delay.

:::satz Theorem 11.1 (Delays in a bandpass)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**How to read it:** the envelope, which carries the information, is delayed by the *group delay*. The carrier is delayed by the *phase delay*. The transmission is distortionless in the strict sense only if the two are equal. That is, the phase line passes through the origin (or through a multiple of $2\pi$ at $f=0$). For the information, a constant group delay is usually enough: if $t_\mathrm g$ is not constant, different frequency components of the envelope arrive at different times, and pulses spread out (__delay distortion__).

:::ltspice Envelope and carrier arrive at different times
⁠**Draw:** the resonant circuit from the LTspice hint in Stage [9](#stufe-9) ($f_0=10$ Hz, $\Delta f=2$ Hz). In the `.ac` analysis its phase at 10 Hz is $0^\circ$, so $t_\mathrm p(f_0)=0$. If you switch the phase axis to “Group Delay”, it shows $t_\mathrm g(f_0)=0.16$ s at 10 Hz.

⁠**Experiment:** as the input a behavioural source `bv`, a carrier with a slowly varying envelope:

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

Directives `.tran 0 20 0 0.2m` and `.options plotwinsize=0`.

⁠**What you see:** Plot `V(in)` and `V(out)` on top of each other and zoom to 14.5 s to 15.5 s. The maximum of the envelope arrives at the output about 0.16 s later, but the zero crossings of the carrier lie at the same places as at the input. This is exactly what [(11.1)](#gl-11-1) says: the envelope is delayed by $t_\mathrm g$, the carrier by $t_\mathrm p$.
:::

:::aufgabe Exercise 10 ★★ Reading off delays
<span class="anker" id="aufg-10"></span>

At $f_0=1$ MHz, a bandpass has the phase $\varphi(f_0)=-\pi/2$ and the slope $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$.

<ol class="al">

<li>

Compute $t_\mathrm p$ and $t_\mathrm g$.

</li>

<li>

By how much is the envelope of a pulse delayed at the output? Is the carrier then still in the same position relative to the envelope?

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0.25$ µ s. $t_\mathrm g=2$ µ s.

(b) The envelope arrives 2 µ s later. The carrier is shifted by only 0.25 µ s. Relative to the envelope it is therefore rotated by $2\pi f_0(t_\mathrm g-t_\mathrm p)=3.5\pi$, which modulo $2\pi$ equals $1.5\pi$, that is $-\pi/2$: a quarter period. The information in the envelope remains undistorted as long as $t_\mathrm g$ is constant over the band.
:::
:::

## Stage 12: Discrete-time bandpass and highpass filters

<span class="anker" id="stufe-12"></span>

:::zweck
Digital bandpass and highpass filters are obtained from a lowpass by modulation.
:::

If the discrete-time lowpass has a real impulse response, multiplication by $2\cos(2\pi f_0n)$ shifts its passband to $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

valid as long as the shifted bands do not overlap: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Because of the periodicity, the band at $f_0$ must touch neither the band at $-f_0$ nor its copy at $1-f_0$. In general, also for complex lowpass impulse responses, $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$ holds as in [(8.1)](#gl-8-1). The factor 2 corresponds to the doubled equivalent lowpass $H_T=2H_{\mathrm{TP}}$.

A __highpass__ is a lowpass shifted to half the sampling rate, $f_0=\frac12$. There the band and its mirror image coincide, so it is shifted only once: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. With $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**In short:** a digital highpass is obtained from a lowpass by flipping every other sign.

:::aufgabe Exercise 11 ★ Highpass from the moving average
<span class="anker" id="aufg-11"></span>

The moving average $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) is a simple lowpass.

<ol class="al">

<li>

Form $h_{\mathrm{HP}}$ according to [(12.2)](#gl-12-2).

</li>

<li>

Compute $H_{\mathrm{TP}}$ and $H_{\mathrm{HP}}$ at $f=0$ and $f=\frac12$. Is this consistent with a highpass?

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$.

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$: $|H_{\mathrm{TP}}(0)|=1$, $|H_{\mathrm{TP}}(\frac12)|=\frac13$. The highpass is shifted by $\frac12$: $|H_{\mathrm{HP}}(0)|=\frac13$, $|H_{\mathrm{HP}}(\frac12)|=1$. It passes the fastest sequence $(+1,-1,+1,\dots)$ in full and attenuates the DC component to one third. A simple highpass, not a very steep one.
:::
:::

:::kern Key points
<ul>

<li>

Distortionless: $h=h_0\delta(t-t_0)$, $H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: constant magnitude, linear phase.

</li>

<li>

$a=-20\lg|H|$ dB; $t_\mathrm p=-\frac{\varphi}{2\pi f}$; $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$.

</li>

<li>

Ideal lowpass: $\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$, not causal; $f_\mathrm g t_m=\frac12$; overshoot 21.7 % (impulse), 8.95 % (step).

</li>

<li>

Step response $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$, $\operatorname{Si}(\infty)=\frac\pi2$, rise time $\frac{1}{2f_\mathrm g}$.

</li>

<li>

Truncating the impulse response $=$ convolution in the spectrum; smooth windows: deeper stopband, shallower edge.

</li>

<li>

Pulse-shaping filter: $T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$, little overshoot.

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$; $s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$; $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

</li>

<li>

$g_T=\frac12s_T*h_T$; envelope delayed by $t_\mathrm g$, carrier by $t_\mathrm p$.

</li>

<li>

Bandpass sampling: $2\Delta f$ values per second; digital highpass: $(-1)^nh_{\mathrm{TP}}(n)$.

</li>

</ul>
:::
