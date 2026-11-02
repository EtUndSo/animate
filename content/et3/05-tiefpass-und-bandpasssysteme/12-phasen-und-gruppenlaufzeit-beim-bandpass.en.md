---
title: Stage 11: Phase and group delay in a bandpass
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3251200
summary: Why are there two delays?
tags: delay distortion
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
Why are there two delays? Because the carrier and the envelope can be delayed differently.
:::

**The idea.** Let a bandpass have a constant magnitude and a slightly curved phase in the passband. Around $f_0$, approximate the phase by its tangent:

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

with $t_\mathrm p=t_\mathrm p(f_0)$ and $t_\mathrm g=t_\mathrm g(f_0)$ from [(1.4)](das-verzerrungsfreie-system.html#gl-1-4) and [(1.5)](das-verzerrungsfreie-system.html#gl-1-5). In the lowpass domain ($f-f_0\to f$) this is $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$: a constant phase and a delay.

:::satz Theorem 11.1 (Delays in a bandpass)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**How to read it:** the envelope, which carries the information, is delayed by the *group delay*. The carrier is delayed by the *phase delay*. The transmission is distortionless in the strict sense only if the two are equal. That is, the phase line passes through the origin (or through a multiple of $2\pi$ at $f=0$). For the information, a constant group delay is usually enough: if $t_\mathrm g$ is not constant, different frequency components of the envelope arrive at different times, and pulses spread out (__delay distortion__).

:::ltspice Envelope and carrier arrive at different times
⁠**Draw:** the resonant circuit from the LTspice hint in Stage [9](bandpasssignal-durch-bandpasssystem.html#stufe-9) ($f_0=10$ Hz, $\Delta f=2$ Hz). In the `.ac` analysis its phase at 10 Hz is $0^\circ$, so $t_\mathrm p(f_0)=0$. If you switch the phase axis to “Group Delay”, it shows $t_\mathrm g(f_0)=0.16$ s at 10 Hz.

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
