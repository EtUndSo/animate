---
title: Stage 4: Causal approximation
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3250500
summary: How do you build something that comes as close as possible to the ideal lowpass?
tags: 
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
How do you build something that comes as close as possible to the ideal lowpass? You delay the impulse response and cut off the rest.
:::

**The idea.** Shift $h(t)$ to the right by $t_0$ until the part at $t<0$ is negligible, and cut that part off. The envelope of the si function falls off like $1/(2\pi f_\mathrm g|t|)$. If it is to stay below 1 % of the maximum before $t=0$, you need $t_0\approx16/f_\mathrm g$. With a symmetric window of width $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**How to read it:** cutting off is a multiplication by a window, and so in the spectrum a convolution with the window's si spectrum. The sharp edge is smeared out and acquires ripples. The factor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ is the delay: the causal filter has a linear phase; it delays all frequencies equally (Fig. [2](#abb-2)). The larger $t_0$, the narrower the transition, but the later the response.

:::abbildung et3/k5kausal 2
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
