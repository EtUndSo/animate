---
title: Stage 8: The discrete Fourier transform (DFT)
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Sampling and Discrete-Time Systems
order: 3240900
summary: S mathrm a(f) is a continuous function, but a computer needs finitely many numbers.
tags: 
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ is a continuous function, but a computer needs finitely many numbers. For a sequence of finite length, finitely many samples of the spectrum are enough.
:::

**The idea.** If $s(n)$ is limited to $M$ values, then by Stage [4](abtastung-im-frequenzbereich.html#stufe-4) samples of the spectrum spaced $F=1/M$ apart are enough. They correspond to the signal $s_d(n)$, repeated periodically with period $M$. Because the spectrum is also periodic (time discrete), $M$ spectral values suffice. Both sides are now discrete and periodic.

:::satz Theorem 8.1 (Discrete Fourier transform)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**How to read it:** $S_d(k)$ is the value of the spectrum $S_\mathrm a(f)$ at $f=k/M$. The index $k$ counts oscillations that fit exactly $k$ times into the $M$ values. The inverse transform is a Fourier series with $M$ terms. The theorems hold analogously, for example the shift $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$ (circular: what is shifted out at the end comes back in at the start) and Parseval $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$.

::::beispiel
$s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Check: $S_d(3)=S_d^*(1)$, because the signal is real ($k=3$ corresponds to $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.
::::

:::aufgabe Exercise 8 ★★ DFT by hand
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Recompute $S_d(1)$ for $s_d=(1,2,0,-1)$.

</li>

<li>

Use the shift theorem to determine the DFT of the circularly shifted sequence $(-1,1,2,0)$, and check $S_d(1)$ directly.

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$, because $(-\mathrm{j})^3=\mathrm{j}$.

(b) Shift by $m=1$: $S_d(k)\,(-\mathrm{j})^k$, so $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$. Directly: $S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$.
:::
:::
