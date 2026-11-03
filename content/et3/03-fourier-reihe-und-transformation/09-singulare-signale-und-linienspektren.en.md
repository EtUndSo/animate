---
title: Stage 8: Singular signals and line spectra
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230900
summary: Constants, oscillations, the step and periodic signals are not absolutely integrable.
tags: line spectrum, Dirac comb
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Constants, oscillations, the step and periodic signals are not absolutely integrable. With Dirac impulses in the spectrum they can still be transformed. In this way the Fourier series and the Fourier integral become one.
:::

:::satz Theorem 8.1 (Singular pairs)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
<span class="anker" id="gl-8-6"></span>
<span class="anker" id="gl-8-7"></span>
$$\begin{aligned} \delta(t)&\;\circ\!\!-\!\!\bullet\;1, & c&\;\circ\!\!-\!\!\bullet\;c\,\delta(f),\\ \mathrm{e}^{\mathrm{j}2\pi Ft}&\;\circ\!\!-\!\!\bullet\;\delta(f-F), & \cos(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F),\\ & & \sin(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F),\\ \textstyle\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}&\;\circ\!\!-\!\!\bullet\;\textstyle\sum_kS_p(k)\,\delta(f-kF),\\ \textstyle\sum_n\delta(t-nT)&\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\textstyle\sum_k\delta\Bigl(f-\frac kT\Bigr),\\ \varepsilon(t)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}, & \operatorname{sgn}(t)&\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f},\\ \int_{-\infty}^ts(\tau)\mathrm{d}\tau&\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f). \end{aligned} \tag{8.1|8.2|8.3|8.4|8.5|8.6|8.7}$$
:::

⁠**How to read it:**

<ul>

<li>

A constant is an oscillation of frequency 0; its spectrum is a single line at $f=0$. An oscillation $\mathrm{e}^{\mathrm{j}2\pi Ft}$ is a line at $F$. A real cosine has two lines of half weight at $\pm F$.

</li>

<li>

A periodic signal has a __line spectrum__: Dirac impulses at the harmonics, with the Fourier coefficients as weights. So the Fourier series is a special case of the Fourier integral.

</li>

<li>

The __Dirac comb__ (impulses spaced $T$ apart) again has a Dirac comb as its spectrum, with the spacing $1/T$ and the weight $1/|T|$ (Fig. [7](#abb-7)).

</li>

<li>

The step has a DC component $\frac12$ (line $\frac12\delta(f)$) and an AC component $\frac12\operatorname{sgn}(t)$, whose spectrum decays like $1/f$.

</li>

</ul>

:::herleitung Singular pairs
⁠**Constant, oscillation:** Apply symmetry to $\delta(t)\circ\!\!-\!\!\bullet\,1$: $1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$. Modulation shifts the line: $\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$. Cosine and sine follow with Euler's formulas.

⁠**Line spectrum:** superposition over all harmonics.

⁠**Dirac comb:** It is periodic with $T$. Its Fourier coefficients are $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$ for all $k$. With the line spectrum, [(8.5)](#gl-8-5) follows.

⁠**Signum:** $\operatorname{sgn}(t)$ is the limiting case of $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ as $a\to0$:

$$\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}\;\xrightarrow{a\to0}\;\frac{1}{\mathrm{j}\pi f}.$$

⁠**Step:** $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$, so $\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

⁠**Integration:** $\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$, convolution theorem and sifting property $S(f)\delta(f)=S(0)\delta(f)$.
:::

:::abbildung et3/k3kamm 7
Dirac comb with $T=0.5$ s and its spectrum: again a comb, with the spacing $1/T=2$ Hz and the weight $1/T=2$. The denser the impulses in time, the farther apart the lines.
:::

:::frage But $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ implies $\mathrm{j}2\pi f\,S(f)=1$, so $S(f)=\frac{1}{\mathrm{j}2\pi f}$. Where does the $\frac12\delta(f)$ come from?
The equation $\mathrm{j}2\pi f\,S(f)=1$ determines $S$ only for $f\neq0$. At $f=0$ the left-hand side is $0\cdot S(0)$, and a term $c\,\delta(f)$ drops out because $f\delta(f)=0$. This is the counterpart of the fact that differentiation “forgets” a constant: $\varepsilon(t)$ and $\varepsilon(t)+b$ have the same derivative. Which constant is correct is decided by the even part: $\varepsilon$ has the mean value $\frac12$, so $c=\frac12$.
:::

**Example: the switched-on cosine.** $\varepsilon(t)\cos(2\pi Ft)$. Multiplication becomes convolution, and convolution with a Dirac impulse shifts:

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

Besides the halved lines at $\pm F$, a broad spectrum arises: the switch-on process itself contains frequencies near $\pm F$.

:::aufgabe Exercise 10 ★ Line spectra
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Give the spectrum of $s(t)=3+2\cos(2\pi\cdot50\,\mathrm{Hz}\cdot t)$ and sketch it.

</li>

<li>

Give the spectrum of the square wave of the reference model for $|f|\le0.5$ Hz.

</li>

</ol>

:::loesung
(a) $3\,\delta(f)+\delta(f-50\,\mathrm{Hz})+\delta(f+50\,\mathrm{Hz})$: one line of weight 3 at zero, two of weight 1 at $\pm50$ Hz.

(b) $F=0.159$ Hz. Up to 0.5 Hz lie $k=0,\pm1,\pm2,\pm3$, but $k=\pm2$ is missing:

$$0.5\,\delta(f)+0.318\bigl[\delta(f-0.159)+\delta(f+0.159)\bigr]-0.106\bigl[\delta(f-0.477)+\delta(f+0.477)\bigr].$$
:::
:::

:::aufgabe Exercise 11 ★★ Signum and integration
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Use [(5.2)](symmetrien-im-signal-und-im-spektrum.html#gl-5-2) to check that the spectrum of $\operatorname{sgn}(t)$ must be purely imaginary and odd.

</li>

<li>

Use [(8.7)](#gl-8-7) to compute the spectrum of $\int_{-\infty}^t\operatorname{rect}(\tau)\mathrm{d}\tau$. Which signal is this?

</li>

</ol>

:::loesung
(a) $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$: purely imaginary, and $-\frac{\mathrm{j}}{\pi(-f)}=+\frac{\mathrm{j}}{\pi f}$, so odd. This fits a real, odd signal.

(b) $\frac{\operatorname{si}(\pi f)}{\mathrm{j}2\pi f}+\frac12\delta(f)$. The signal is the running integral of the rectangle: 0 for $t\le-\frac12$, then a ramp up to 1 at $t=\frac12$, constant 1 after that. The mean value over all time is $\frac12$, hence $\frac12\delta(f)$.
:::
:::
