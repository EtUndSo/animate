---
title: Stage 9: Hilbert transform and analytic signal
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Fourier Series and Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Chapter 3: Fourier Series and Transform
order: 3231000
summary: For a causal signal, the real and imaginary parts of the spectrum are linked: one determines the other.
tags: Hilbert transform, principal value, analytic component, all-pass
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
For a causal signal, the real and imaginary parts of the spectrum are linked: one determines the other. The same calculation yields a signal that contains only positive frequencies.
:::

**Causal signals.** If $s(t)=0$ for $t<0$, then the even and odd parts are equal for $t>0$ ($\frac12s$) and opposite for $t<0$. So $s_u(t)=s_g(t)\operatorname{sgn}(t)$ and $s_g(t)=s_u(t)\operatorname{sgn}(t)$. In the frequency domain, multiplication by $\operatorname{sgn}$ becomes convolution with $\frac{1}{\mathrm{j}\pi f}$:

:::satz Theorem 9.1 (Hilbert relation for causal signals)
<span class="anker" id="satz-9-1"></span>

For a causal signal,

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**How to read it:** Convolution with $\frac{1}{\pi f}$ is called the __Hilbert transform__. Its integral exists only as a __principal value__: around the point where the kernel becomes infinite, a symmetric piece is cut out and then shrunk to zero. For a causal system it is enough to know the real part of the frequency response; the imaginary part follows from it. Causality is therefore a strong constraint on the spectrum.

**Analytic component.** With the step in the *frequency domain* you cut off the negative frequencies: $S_+(f)=S(f)\,\varepsilon(f)$. Symmetry gives $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, so

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ is called the __analytic component__, $\hat s$ the Hilbert transform of $s$; the convolution with $\frac{1}{\pi t}$ is also meant as a principal value. Likewise, $S_-(f)=S(f)\,\varepsilon(-f)$, with the time function $s_-(t)$, contains only the negative frequencies. For real signals, $S_-(f)=S_+^*(-f)$, so $s_-=s_+^*$ and $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. The real and imaginary parts of $s_+$ are again Hilbert transforms of each other.

**The Hilbert transformer.** The LTI system with $h(t)=\frac{1}{\pi t}$ has $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: magnitude 1 at all frequencies (an __all-pass__), phase $-90^\circ$ for $f>0$ and $+90^\circ$ for $f<0$. It turns $\cos(2\pi Ft)$ into

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**In short:** The Hilbert transformer shifts the phase of every oscillation by $90^\circ$ without changing its amplitude.

:::aufgabe Exercise 12 ★★ Hilbert transformer
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

What does the Hilbert transformer make of $\sin(2\pi Ft)$? What does applying it twice give?

</li>

<li>

Find the analytic component $s_+(t)$ of $\cos(2\pi Ft)$ and check $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

Why is the Hilbert transformer not causal? Look at $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplication by $-\mathrm{j}\operatorname{sgn}(f)$: at $-F$ by $+\mathrm{j}$, at $+F$ by $-\mathrm{j}$. Result: $-\frac12\delta(f+F)-\frac12\delta(f-F)$, that is, $-\cos(2\pi Ft)$. Applied twice: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, so the signal is inverted.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, so $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. This agrees with $\frac12(s+\mathrm{j}\hat s)$ with $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ is nonzero for $t<0$ as well. So the output at time $t$ depends on future input values. In practice, the Hilbert transformer is approximated with a truncated impulse response, at the cost of a delay.
:::
:::
