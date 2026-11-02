---
title: Stage 7: Rectangle, si function and triangle
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230800
summary: Three transform pairs come up all the time.
tags: 
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
Three transform pairs come up all the time. With the theorems, they follow from a single calculation.
:::

**Rectangle.** With $\operatorname{si}(x)=\sin(x)/x$:

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz Theorem 7.1 (Rectangle, si and triangle)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**How to read it:** A rectangle of duration $T$ has a spectrum of height $T$ (its area) with zeros at all non-zero multiples of $1/T$. Twice as long means half as wide in the spectrum (Fig. [6](#abb-6)). [(7.2)](#gl-7-2) follows from symmetry, [(7.3)](#gl-7-3) from the convolution theorem, and [(7.4)](#gl-7-4) holds because $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$ in the frequency domain: an ideal low-pass filter does not change a signal that is already limited to its band.

:::abbildung et3/k3rectsi 6
$\operatorname{rect}(t/T)$ and its spectrum $|T|\operatorname{si}(\pi Tf)$ for $T=1$ s and $T=2$ s. Double the duration: double the height ($=$ area), half the width, first zero at $1/T$.
:::

:::ltspice Spectrum of a rectangular pulse
⁠**Draw:** just one `voltage` source with `PULSE(0 1 0 1u 1u {T0} 16)`: a rectangle of duration $T_0$, repeated every 16 s.

⁠**Directives:** `.param T0=1`, `.step param T0 list 1 2`, `.tran 0 16 0 1m`, `.options plotwinsize=0`, `.four 0.0625 40 V(in)`.

⁠**What you see:** The repetition every 16 s turns the spectrum into lines spaced $1/16$ Hz apart (Stage [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4)). `.four` reports their amplitudes $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$, i.e. samples of the si envelope. For $T_0=1$ s the lines at 1 Hz and 2 Hz are zero, for $T_0=2$ s already those at 0.5 Hz, 1 Hz, 1.5 Hz and 2 Hz. The DC component doubles from 0.0625 to 0.125. So double the duration means half the width and double the height, as in Fig. [6](#abb-6). In the FFT view you see the envelope and its zeros directly.
:::

:::aufgabe Exercise 8 ★ Areas and energy of the si function
<span class="anker" id="aufg-8"></span>

Compute $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ and $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$ without integration. Use the area theorem and Parseval.

:::loesung
Area theorem: $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$. Parseval: $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
:::
:::

:::aufgabe Exercise 9 ★★ Triangle and repeated convolution
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Find the spectrum of $\Lambda(t/2)$ (triangle with half-width 2 s). Where are the zeros?

</li>

<li>

What is the spectrum of $\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$? Why do the side lobes decay faster the more often you convolve?

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$ and similarity with $T=2$: $\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$. Zeros at $f=k/2$, $k\neq0$.

(b) $\operatorname{si}^3(\pi f)$. Each further convolution multiplies the spectrum by $\operatorname{si}(\pi f)$, which decays like $1/(\pi f)$ in the side lobes. For the $M$-fold convolution, the side lobes decay like $1/f^M$. In the time domain: the rectangle jumps (decay $1/f$), the triangle has kinks ($1/f^2$), the threefold convolution has a continuous derivative ($1/f^3$). The smoother a signal, the faster its spectrum decays.
:::
:::
