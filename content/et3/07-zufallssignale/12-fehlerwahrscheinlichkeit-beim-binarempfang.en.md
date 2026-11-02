---
title: Stage 11: Error probability in binary reception
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3271200
summary: The receiver has to decide: was the pulse sent or not?
tags: 
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
The receiver has to decide: was the pulse sent or not? How often is it wrong?
:::

**The idea.** The sample at the output of the matched filter is Gaussian with the variance $N$ (noise) and the mean value $\sqrt{S_a}$ if the pulse was sent, or 0 if not. The receiver compares it with a threshold $C$. An error occurs when the noise pushes the value across the threshold. The two error probabilities are the areas of the two Gaussian curves beyond the threshold:

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

If both cases are sent equally often, the average error probability is $\frac12(P_{e1}+P_{e0})$. It is smallest when the threshold lies exactly in the middle, $C=\sqrt{S_a}/2$. With the matched filter ($S_a/N=E_s/N_0$):

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**How to read it:** The error probability depends only on $E_s/N_0$ and falls extremely fast: at 10 dB $5.7\cdot10^{-2}$, at 16 dB $8\cdot10^{-4}$, at 20 dB $2.9\cdot10^{-7}$ (Fig. [4](#abb-4)). A few decibels more signal energy turn an unusable transmission into an almost error-free one.

:::abbildung et3/k7pe 4
Minimum error probability for on-off reception with a matched filter. Red dots: 10 dB, 16 dB, 20 dB.
:::

:::aufgabe Exercise 11 ★★ Error probability
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Compute $P_{e,\min}$ for $E_s/N_0=10$ dB. Hint: $\operatorname{erfc}(1.118)=0.114$.

</li>

<li>

Why does the optimal threshold lie in the middle between 0 and $\sqrt{S_a}$? What happens to $P_{e1}$ and $P_{e0}$ if you shift it upward?

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$: $\sqrt{10/8}=1.118$, $P_{e,\min}=\frac12\cdot0.114=0.057$.

(b) The two Gaussian curves have the same width. The sum of the two error areas is smallest where the curves intersect, and by symmetry that is the middle. If you shift the threshold upward, $P_{e0}$ becomes smaller, but $P_{e1}$ grows more, because the threshold moves into the dense part of the upper curve.
:::
:::
