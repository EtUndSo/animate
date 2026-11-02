---
title: Stage 7: The Gaussian distribution
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270800
summary: Why is noise so often Gaussian, and how do you calculate with the Gaussian distribution?
tags: central limit theorem, error function
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
Why is noise so often Gaussian, and how do you calculate with the Gaussian distribution?
:::

If you convolve many densities with one another, the result approaches a Gaussian curve (__central limit theorem__, [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). Noise is usually the sum of very many small, independent contributions, such as the motions of many electrons. That is why it is Gaussian.

:::satz Theorem 7.1 (Gaussian distribution)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

with the __error function__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$ and $\operatorname{erfc}=1-\operatorname{erf}$.
:::

⁠**How to read it:** The mean value and the variance determine the Gaussian distribution completely. Within $\pm\sigma_s$ around the mean lie 68.3 % of the values, within $\pm2\sigma_s$ 95.4 %, within $\pm3\sigma_s$ 99.73 %. The integral of the Gaussian curve has no closed form, hence the function erf, which is tabulated or computed numerically. For large $x$, $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Calculation rules.** The sum of two independent Gaussian variables is Gaussian with $m_s=m_1+m_2$ and $\sigma_s^2=\sigma_1^2+\sigma_2^2$. A Gaussian process remains a Gaussian process after an LTI system, because the convolution integral is an (infinite) weighted sum. And for two jointly Gaussian variables, “uncorrelated” is the same as “independent”: if the normalized cross-covariance $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ is zero, the joint density factors into a product.

:::zusatz The two-dimensional Gaussian density
For zero-mean, jointly Gaussian $s,g$ with the correlation coefficient $\rho$,

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

It is obtained via the normalized sum and difference variables $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$: they are uncorrelated, have the variances $2(1\pm\rho)$ and, being Gaussian, are independent. Lines of equal density are ellipses; in the normalized coordinates $x/\sigma_s$, $y/\sigma_g$, their axes lie along these sums and differences. For $\rho=0$ they become circles (when $\sigma_s=\sigma_g$), and the density is the product of the individual densities.
:::

:::aufgabe Exercise 6 ★ Calculating with the Gaussian distribution
<span class="anker" id="aufg-6"></span>

A noise voltage is Gaussian with $m=0$ and $\sigma=1$ mV.

<ol class="al">

<li>

With what probability is it greater than 2 mV? (Hint: $\operatorname{erfc}(1.414)=0.0455$.)

</li>

<li>

Two such independent voltages are added. What distribution does the sum have?

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1.414)=0.023$, that is, 2.3 %.

(b) Gaussian with $m=0$ and $\sigma^2=2$ mV$^2$, $\sigma=1.41$ mV.
:::
:::
