---
title: Stage 1: The distortionless system
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3250200
summary: What exactly should a “good” transmission achieve?
tags: phase delay, group delay
lang: en
---

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

⁠**How to read it:** the __phase delay__ is the delay of a single oscillation of frequency $f$. The __group delay__ is the delay of a group of neighboring frequencies, that is, of an envelope (Stage [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)). For the distortionless system, $a$, $t_\mathrm p$ and $t_\mathrm g$ are constant and $t_\mathrm p=t_\mathrm g=t_0$.

::::beispiel the RC circuit
With $\varphi=-\arctan(2\pi f\,RC)$ and $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

For $f\to0$ both are $RC=1$ s. At $f=0.159$ Hz ($2\pi fRC=1$), $t_\mathrm p=0.785$ s, $t_\mathrm g=0.5$ s and $a=3.0$ dB. So the RC circuit is not distortionless: its attenuation depends on frequency, and different frequencies arrive at different times.
::::

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
