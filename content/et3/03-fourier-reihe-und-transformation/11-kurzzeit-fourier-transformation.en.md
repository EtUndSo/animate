---
title: Stage 10: Short-time Fourier transform
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3231100
summary: The spectrum S(f) describes a signal over all time.
tags: Hann window, spectrogram
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
The spectrum $S(f)$ describes a signal over all time. Speech or music, however, change their frequencies continually. The short-time Fourier transform (STFT) asks: which frequencies does the signal contain *around the instant $t$*?
:::

**The idea.** Cut out a segment around $t$ and transform only that segment. With a rectangular window of width $T_0$:

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

The spectrum of the segment is the true spectrum, smeared by the si spectrum of the window. A short window localizes well in time but smears strongly in frequency (similarity theorem). The hard edges of the rectangle also produce slowly decaying side lobes. Smooth windows are therefore better, for example the __Hann window__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz Theorem 10.1 (Short-time Fourier transform)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

If the windows shifted by $T$ add up to a constant, $\sum_nw(\tau-nT)=c$, then

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**How to read it:** $S_T(f,t)$ is a spectrum that depends on time. Plotting $|S_T|$ over $t$ and $f$ gives a __spectrogram__. For the Hann window with the offset $T=T_0/2$, $c=1$, because $\cos^2x+\sin^2x=1$ (Fig. [8](#abb-8)): the segments fit together seamlessly into the whole signal, and the sum of their spectra is the whole spectrum.

:::abbildung et3/k3hann 8
Hann windows of width $T_0=2$ s, each offset by $T=1$ s (blue). Their sum is exactly 1 everywhere (red).
:::

:::aufgabe Exercise 13 ★ Hann window
<span class="anker" id="aufg-13"></span>

Show that $\sum_nw(\tau-nT)=1$ for $T=T_0/2$. Hint: at every point exactly two windows overlap. Write the second one using $\cos^2(x-\frac\pi2)$.

:::loesung
For $\tau$ between $nT$ and $(n+1)T$ with $T=T_0/2$, exactly the windows $n$ and $n+1$ are nonzero. With $x=\pi(\tau-nT)/T_0$:

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::
