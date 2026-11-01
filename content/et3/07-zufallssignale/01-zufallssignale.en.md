---
title: Random Signals
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270100
summary: Mean values, distributions, power spectral density, noise in systems and the optimal receiver
tags: sample function, random process, random variable, expected value, autocorrelation function, stationary, ergodic, DC component
lang: en
---

## What this is about

The noise of a resistor, speech, a data stream: such signals cannot be predicted. Their exact waveform is unknown, but their *average properties* are known: how large they typically are, how fast they change, which frequencies they contain. This article shows how to describe such random signals, what an LTI system does to them and how to detect a known signal in noise most reliably.

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

A random signal is described by averages: mean value, power, variance, autocorrelation function and probability density function. For ergodic processes, they may be determined from a single, long signal.

</li>

<li>

The Fourier transform of the autocorrelation function is the power spectral density. An LTI system multiplies it by $|H(f)|^2$, exactly as for energy signals ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).

</li>

<li>

Against white noise, the matched filter $h(t)=s(T-t)$ is optimal. It achieves the signal-to-noise ratio $E_s/N_0$, regardless of the signal shape.

</li>

</ol>
:::

**One principle behind all the results.** You replace the unknown signal by its averages, and averages are linear:

| Result | Where it comes from |
|---|---|
| Mean value, power, variance | ensemble average and time average (Stages [1](#stufe-1)–[3](#stufe-3)) |
| ACF, covariance, CCF | average over products of values at two instants (Stage [4](#stufe-4)) |
| Probability density function | fraction of time or of the ensemble below a threshold (Stage [5](#stufe-5)) |
| Sum of independent variables | convolution of the densities, hence Gaussian (Stages [6](#stufe-6), [7](#stufe-7)) |
| Power spectral density, Wiener–Lee | linearity of the expected value in the convolution integral (Stage [8](#stufe-8)) |
| White noise | constant power spectral density, ACF $=N_0\delta$ (Stage [9](#stufe-9)) |
| Matched filter | Cauchy–Schwarz: the correlation is greatest with the signal itself (Stage [10](#stufe-10)) |
| Error probability | area under a Gaussian curve beyond the threshold (Stage [11](#stufe-11)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
<ul>

<li>

⁠**Uniformly distributed random numbers** between $-\frac12$ and $\frac12$ (variance $\frac{1}{12}$), also as discrete-time white noise.

</li>

<li>

⁠**Resistor** $R=1\,\mathrm{k\Omega}$ at 290 K, bandwidth 20 kHz (audio).

</li>

<li>

⁠**Recursive system** $g(n)=s(n)+0.6\,g(n-1)$ from [Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html).

</li>

</ul>

The script `rechnung_kap7.py` recomputes the numbers, in part checking them with simulated random numbers.
:::

## Stage 1: The random process

<span class="anker" id="stufe-1"></span>

:::zweck
How do you describe a signal whose waveform you do not know? You imagine many signals of the same kind and average over them.
:::

**The idea.** If you measure the noise of many identically built resistors at the same temperature, you get many different curves ${}^ks(t)$, $k=1,2,\dots$ (Fig. [1](#abb-1)). Each one is called a __sample function__ or realization. The imagined totality of all of them is called a __random process__ $s(t)$. The values of all sample functions at a fixed instant $t_1$ form a __random variable__ $s(t_1)$.

:::definition Definition 1.1 (Ensemble averages)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**How to read it:** $\mathrm E\{\cdot\}$ is called the __expected value__ or ensemble average: you average over all sample functions at the same instant, that is, vertically in Fig. [1](#abb-1). With $F[x]=x^2$ you obtain the mean square value. The __autocorrelation function__ averages the product of the values at two instants. It tells you how strongly the value at $t_2$ is related to the value at $t_1$.

:::abbildung et3/k7schar
Three sample functions of a random process (simulated, mean value 1). The ensemble average is formed vertically, over all sample functions at the same $t_1$ (red, dashed). The time average is formed horizontally, along one sample function.
:::

## Stage 2: Stationarity and ergodicity

<span class="anker" id="stufe-2"></span>

:::zweck
You never have an infinite ensemble, usually only a single signal. When is that enough?
:::

A process is called __stationary__ if none of its averages change when all observation times are shifted by the same time $t_0$:

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

Then the mean value $m_s=\mathrm E\{s(t)\}$ is a constant, and the ACF depends only on the difference $\tau=t_2-t_1$: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$. A stationary process is called __ergodic__ if, in addition, every time average of a sample function equals the corresponding ensemble average:

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{for every }k. \tag{2.2}$$

⁠**How to read it:** Stationary means that the statistics do not change with time. Ergodic means that a single sample function, observed for a long time, shows in the course of time everything that the whole ensemble shows. The noise of a resistor at constant temperature is ergodic. Only for this reason can noise be characterized with a single measuring instrument.

:::frage Is every stationary process also ergodic?
No. Example: each sample function is a constant whose value is drawn at random once, ${}^ks(t)=c_k$. The process is stationary, because nothing depends on $t$. But the time average of a sample function is $c_k$, which is different for every sample function and is not the ensemble average. A single sample function never “sees” the other values.
:::

## Stage 3: Mean value, power, variance

<span class="anker" id="stufe-3"></span>

:::zweck
The most important first-order averages and their intuitive meaning.
:::

The expected value is linear: $\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$, for arbitrary random variables. For stationary processes one defines:

<span class="anker" id="gl-3-1"></span>
$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2. \tag{3.1}$$

⁠**How to read it:** For an ergodic process, $m_s$ is the time average, that is, the __DC component__ of the signal, and $L_s$ is the time-averaged square, the __power__ ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). The __variance__ $\sigma_s^2$ is the power minus the power of the DC component, that is, the __AC power__. Its square root, the __standard deviation__ $\sigma_s$, is the RMS value of the AC component. A multimeter set to AC shows $\sigma_s$; set to DC, it shows $m_s$.

:::aufgabe Exercise 1 ★ Averages of a signal
<span class="anker" id="aufg-1"></span>

An ergodic signal has a DC component of 2 V and an RMS value (everything together, “true RMS”) of 2.5 V. What are the normalized power, the variance and the standard deviation?

:::loesung
$L_s=2.5^2=6.25$ V$^2$, $\sigma_s^2=L_s-m_s^2=6.25-4=2.25$ V$^2$, $\sigma_s=1.5$ V. An AC meter shows 1.5 V.
:::
:::

## Stage 4: Autocorrelation, covariance and cross-correlation

<span class="anker" id="stufe-4"></span>

:::zweck
How fast does a random signal change? The ACF tells you: how similar the signal still is to itself after the time $\tau$.
:::

:::satz Theorem 4.1 (Properties of the ACF of stationary processes)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

For ergodic processes, $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$, that is, the ACF of a power signal from [Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html).
:::

:::herleitung Maximum at $\tau=0$
$\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$, because the expected value of a square is never negative. Multiplying out and using linearity: $\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$, so $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$. Evenness: substitute $t\to t-\tau$ in the definition.
:::

**Covariance.** If you subtract the mean value first, you obtain the __autocovariance function__

<span class="anker" id="gl-4-2"></span>
$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2. \tag{4.2}$$

If the process contains no periodic components, values that lie far apart become independent: $\varphi_{ss}(\tau)\to m_s^2$ and $\mu_{ss}(\tau)\to0$ for $\tau\to\infty$.

**Cross-correlation and sums.** For two processes, $\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$ with $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$, and the cross-covariance is $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$. For the sum $s=u+v$, multiplying out gives

<span class="anker" id="gl-4-3"></span>
$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0). \tag{4.3}$$

⁠**In short:** Powers add only if the signals are uncorrelated. Otherwise the cross term is added. Two identical signals give four times the power, two opposite ones give zero power.

:::aufgabe Exercise 2 ★★ Two noise sources
<span class="anker" id="aufg-2"></span>

Two zero-mean noise voltages with the RMS values 3 mV and 4 mV are added. What is the RMS value of the sum if they are (a) uncorrelated, (b) identical in shape ($\varphi_{uv}(0)=\sigma_u\sigma_v$), (c) identical in shape but of opposite sign ($\varphi_{uv}(0)=-\sigma_u\sigma_v$)?

:::loesung
(a) $\sigma=\sqrt{9+16}=5$ mV. (b) $\sigma^2=9+16+2\cdot12=49$, so 7 mV: the amplitudes add. (c) $\sigma^2=9+16-24=1$, so 1 mV: the signals almost cancel each other.
:::
:::

## Stage 5: Distribution function and probability density

<span class="anker" id="stufe-5"></span>

:::zweck
Averages do not tell everything. How often does a signal take which values? This is described by the distribution.
:::

:::definition Definition 5.1 (Distribution)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**How to read it:** The __cumulative distribution function__ $P_s(x)$ is the fraction of the ensemble (for ergodic processes: the fraction of time) in which the signal lies below the threshold $x$. It rises monotonically from $P_s(-\infty)=0$ to $P_s(\infty)=1$. The __probability density function__ $p_s(x)$ is never negative, has the area 1, and $p_s(x)\,\mathrm{d} x$ is the probability that the signal lies between $x$ and $x+\mathrm{d} x$. All first-order averages follow from it:

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

**Example: uniform distribution.** All values in an interval of width $a$ around $m_s$ are equally likely: $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$. Then

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

The random numbers of the reference model ($a=1$, $m_s=0$) have the variance $\frac1{12}=0.0833$.

**Characteristic curves.** If a signal passes through a characteristic curve (transfer characteristic) $y=k(x)$ (amplifier with saturation, rectifier, quantizer), its distribution changes. For a monotonic characteristic, the probability of every interval is preserved:

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\text{ increasing}). \tag{5.3}$$

Where the characteristic is steep, the values are spread over a wide range, and the density decreases. With this rule, any distribution can be transformed into a desired one. Example: $k(x)=(2|x|-x^2)\operatorname{sgn}x$ turns a triangular distribution on $[-1,1]$ into a uniform distribution (Exercise [4](#aufg-4)).

**Quantization.** A __quantizer__ replaces every value by the nearest of $M$ levels. With uniform levels of width $\Delta$ and no overload, the error between $-\frac\Delta2$ and $\frac\Delta2$ is approximately uniformly distributed, hence has the variance $\frac{\Delta^2}{12}$. For a signal uniformly distributed over all $M$ levels (variance $\frac{(M\Delta)^2}{12}$), the signal-to-noise ratio is $M^2$, in decibels $20\lg M\approx6\,\text{dB per bit}$: 48 dB at 8 bits, 96 dB at 16 bits.

:::aufgabe Exercise 3 ★ Uniform distribution
<span class="anker" id="aufg-3"></span>

A signal is uniformly distributed between 1 V and 3 V. Compute $m_s$, $L_s$, $\sigma_s^2$ and the probability that it lies above 2.5 V.

:::loesung
$a=2$ V, $m_s=2$ V. $\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$, $L_s=\frac13+4=4.33$ V$^2$. A quarter of the interval lies above 2.5 V, so $\mathrm{Prob}=\frac{0.5}{2}=0.25$.
:::
:::

:::aufgabe Exercise 4 ★★ Transforming distributions
<span class="anker" id="aufg-4"></span>

A signal has the triangular density $p_s(x)=\Lambda(x)$ on $[-1,1]$.

<ol class="al">

<li>

Find $P_s(x)$ for $0\le x\le1$.

</li>

<li>

Use [(5.3)](#gl-5-3) to show that $k(x)=(2x-x^2)$ for $x\ge0$ (continued as an odd function) produces a uniform distribution on $[-1,1]$. Hint: for the uniform distribution, $P_g(y)=\frac12+\frac y2$.

</li>

</ol>

:::loesung
(a) $P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$ for $0\le x\le1$.

(b) According to [(5.3)](#gl-5-3), $P_g(k(x))=P_s(x)$ must hold, so $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$. This gives $k(x)=2x-x^2$. The characteristic is steep at $x=0$ (slope 2), where the triangular density is largest, and flat at the edge. In this way, the frequent values are pulled apart and the rare ones are pushed together. A simulation gives a flat histogram of height 0.5.
:::
:::

:::aufgabe Exercise 4a ★★★ (Going further) The optimal quantizer
<span class="anker" id="aufg-4a"></span>

A quantizer with the thresholds $u_i$ and the level values $v_i$ (level $i$ applies for $u_i<x\le u_{i+1}$) has the mean squared error $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$.

<ol class="al">

<li>

Show by differentiating with respect to $v_i$: at the optimum, $v_i$ lies at the centroid of the density on its interval.

</li>

<li>

Show by differentiating with respect to $u_i$: at the optimum, $u_i$ lies exactly halfway between $v_{i-1}$ and $v_i$.

</li>

<li>

Why is the uniform quantizer optimal for a uniformly distributed signal?

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$, so $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$, the centroid.

(b) $u_i$ appears as the upper limit of interval $i-1$ and as the lower limit of interval $i$: $\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$, so $u_i=\frac12(v_{i-1}+v_i)$. A value is assigned to the level whose level value is closer.

(c) For a constant density, the centroid of each interval is its midpoint. Intervals of equal width with their midpoints as level values satisfy both conditions, with the step size $\Delta=a/M$.
:::
:::

## Stage 6: Joint distribution, independence, uncorrelatedness

<span class="anker" id="stufe-6"></span>

:::zweck
Two random variables at once: when are they related, and what follows for their sum?
:::

The __joint distribution__ of two variables is $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{and}\ g\le y]$, its density is $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$. From it follow the individual distributions ($P_{sg}(x,\infty)=P_s(x)$) and the correlation $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$. For jointly stationary processes, everything depends only on the time shift $\tau$ between $s(t)$ and $g(t+\tau)$.

:::definition Definition 6.1 (Independent, uncorrelated)
<span class="anker" id="satz-6-1"></span>

$s$ and $g$ are called __statistically independent__ if $p_{sg}(x,y)=p_s(x)\,p_g(y)$. They are called __uncorrelated__ if $\mu_{sg}=\varphi_{sg}-m_sm_g=0$.
:::

Independence implies uncorrelatedness: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. The converse does not hold: uncorrelated only means that there is no *linear* relationship (Exercise [5](#aufg-5)).

**The sum of two independent variables.** The sum $s=f+g$ takes the value $x$ if $f=u$ and $g=x-u$, for any $u$:

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{independent}). \tag{6.1}$$

This is the convolution from [Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), where it appeared in the example of the dice. Two uniformly distributed variables give a triangular density, three give an almost bell-shaped one (Fig. [2](#abb-2)).

:::abbildung et3/k7summen
Probability density functions of sums of independent random variables, each uniformly distributed on $[-\frac12,\frac12]$. Even the sum of three lies close to the Gaussian curve with the same variance (at $x=0$: 0.75 versus 0.80).
:::

:::aufgabe Exercise 5 ★★ Uncorrelated, but dependent
<span class="anker" id="aufg-5"></span>

$s$ is uniformly distributed on $[-1,1]$ and $g=s^2$. Show that $s$ and $g$ are uncorrelated, although $g$ is completely determined by $s$.

:::loesung
$m_s=0$ and $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$, so $\mu_{sg}=0-0\cdot m_g=0$: uncorrelated. Nevertheless, $s$ determines the value of $g$. The relationship is quadratic, and a correlation captures only linear relationships: for positive $s$, $g$ increases with $s$; for negative $s$, it decreases; on average, the two tendencies cancel.
:::
:::

## Stage 7: The Gaussian distribution

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

## Stage 8: Random signals in LTI systems, power spectrum

<span class="anker" id="stufe-8"></span>

:::zweck
What does an LTI system do to a random signal? Each sample function is convolved. Simple rules therefore hold for the averages.
:::

**Mean value.** For each sample function, ${}^kg={}^ks*h$. The expected value is linear and may be moved into the convolution integral:

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

The mean value is transmitted like a DC component.

:::satz Theorem 8.1 (Wiener–Lee for stationary processes)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

with the impulse ACF (deterministic ACF) $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ of the impulse response and the __power spectral density__ $\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$. The power is

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung Wiener–Lee
Write out both convolution integrals, with different variables:

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

Move the expected value into the double integral. For a stationary process, $\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$. With $\vartheta=\beta-\alpha$:

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

In the frequency domain, $\varphi^E_{hh}$ becomes $|H|^2$ ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).
:::

⁠**How to read it:** $\Phi_{ss}(f)$ indicates how the power is distributed over the frequencies. It is real, never negative and, for real signals, even. An LTI system multiplies the power at each frequency by $|H(f)|^2$; its phase plays no role. This is the same rule as for energy signals in [Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html), now for processes. (Note: strictly speaking, $\Phi_{ss}$ is defined as the limit $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ over short-time spectra of segments of duration $T$. That this is the same as the transform of the ACF is the actual statement of the Wiener–Khinchin theorem.)

:::ltspice Noise with a mean value through low-pass and high-pass
⁠**Draw:** a behavioural source `bv` at net `s` with `V=1+white(1e3*time)`. `white(x)` returns random values between $-0.5$ and $0.5$, a new one at every integer $x$, joined smoothly, so here every millisecond. Connected to it in parallel, an RC low-pass (`res` with `1Meg` to `tp`, `cap` with `1u` to ground) and a CR high-pass (`cap` with `1u` to `hp`, `res` with `1Meg` to ground).

⁠**Directive:** `.tran 0 200 0 0.1m`.

⁠**Reading:** Zoom to 20 s to 200 s, i.e. to the time after the transient. A click on a trace name while holding the Ctrl key shows the mean (Average) and the RMS value over the visible range.

⁠**What you see:** The input has the mean 1 V. Compare the means of `V(tp)` and `V(hp)` with your result from Exercise [7](#aufg-7). The fluctuations are much smaller at the low-pass: plot `V(s)-1` and `V(tp)-1`, their RMS values are about 0.25 and 0.01. The low-pass passes only roughly the part of the broad power density below $1/(2\pi RC)=0.16$ Hz, and by [(8.3)](#gl-8-3) the power is the area under the power density.
:::

:::aufgabe Exercise 7 ★ Mean value through a filter
<span class="anker" id="aufg-7"></span>

Noise with the mean value 1 V passes through an RC low-pass filter and through a CR high-pass filter. What mean values do the outputs have, and why?

:::loesung
RC low-pass filter: $H(0)=1$, mean value 1 V. CR high-pass filter: $H(0)=0$, mean value 0. The capacitor does not pass direct current, so the DC component is blocked.
:::
:::

## Stage 9: White noise and thermal noise

<span class="anker" id="stufe-9"></span>

:::zweck
The most important model for disturbances: noise with the same power density at all frequencies.
:::

:::definition Definition 9.1 (White noise)
<span class="anker" id="satz-9-1"></span>

A zero-mean process with $\Phi_{ss}(f)=N_0$ for all $f$ is called __white noise__. Its ACF is $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
:::

⁠**How to read it:** Values at different times are uncorrelated, no matter how close together they are. The power $\int N_0\mathrm{d} f$ is infinite: white noise is a limiting model, like the Dirac impulse. What is actually measured is always filtered, “colored” noise:

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

Behind an ideal low-pass filter with the cutoff frequency $f_\mathrm g$: $L_g=2N_0f_\mathrm g$ and $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ (Fig. [3](#abb-3)). The ACF is zero at $\tau=k/(2f_\mathrm g)$, $k\neq0$: samples taken at the Nyquist rate are uncorrelated.

:::abbildung et3/k7tp
ACF of white noise behind an ideal low-pass filter: $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$. At $\tau=0$ it equals the power $2N_0f_\mathrm g$. At the red dots ($\tau=k/(2f_\mathrm g)$) it is zero.
:::

**Thermal noise.** The thermal motion of the electrons produces a noise voltage across every resistor $R$. In open circuit, measured in the frequency range $|f|\le f_\mathrm g$:

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

with the Boltzmann constant $k=1.38\cdot10^{-23}$ W s/K. At room temperature (290 K), $kT\approx4\cdot10^{-21}$ W/Hz, that is, 4 pW per GHz of bandwidth. $L_{\max}$ is the maximum power that can be extracted from the resistor, under power matching. In the reference model ($1\,\mathrm{k\Omega}$, 20 kHz), the RMS value is $\sqrt{\mathrm E\{u^2\}}=0.57$ µ V. This order of magnitude limits how sensitive a microphone amplifier can be. The spectrum is flat up to about $10^{12}$ Hz.

:::ltspice Measuring thermal noise
LTspice gives every resistor its thermal noise. The `.noise` analysis computes the noise density `V(onoise)` at a node in V$/\sqrt{\mathrm{Hz}}$. The measurement `.meas noise urms INTEG V(onoise)` integrates it in quadrature over the frequency range of the analysis, as in [(8.3)](#gl-8-3), and gives the RMS value. `.temp 16.85` sets 290 K.

⁠**Resistor:** `res` with `{Rx}` from net `a` to ground, in parallel a `current` source with the value 0 (name `I1`). It loads nothing; `.noise` only needs it as a reference source. Directives `.param Rx=1k` and `.noise V(a) I1 lin 20001 1 20k`. Result: 4.0 nV$/\sqrt{\mathrm{Hz}}$ and `urms` $=0.57$ µ V as above. Set `Rx=1Meg` and compare with your result from Exercise [8](#aufg-8).

⁠**$kT/C$:** a `voltage` source `V1` with the value 0 and `AC 1`, `res` with `{Rx}` to `out`, `cap` with `1p` to ground. Directives `.step param Rx list 1k 1Meg` and `.noise V(out) V1 dec 200 1 1T`, plus `.temp 16.85` and the measurement `urms` again. `urms` is the same for both resistors. Compare the value with your result from Exercise [9](#aufg-9)(b).
:::

:::aufgabe Exercise 8 ★ Noise of a resistor
<span class="anker" id="aufg-8"></span>

Compute the RMS noise voltage of a $1\,\mathrm{M\Omega}$ resistor at 290 K and 20 kHz bandwidth. By what factor is it larger than for the $1\,\mathrm{k\Omega}$ resistor, and why by exactly this factor?

:::loesung
The RMS value grows with $\sqrt R$: $\sqrt{1000}=31.6$ times larger, so $0.566\cdot31.6=17.9$ µ V.
:::
:::

:::aufgabe Exercise 9 ★★ $kT/C$ noise
<span class="anker" id="aufg-9"></span>

The thermal noise of the resistor ($N_0=2kTR$) passes through the RC circuit that the resistor forms with a capacitor $C$ ($h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$).

<ol class="al">

<li>

Use [(9.1)](#gl-9-1) to show that the noise power across the capacitor is $kT/C$, independent of $R$.

</li>

<li>

What is the RMS value for $C=1$ pF and 290 K? Why does a smaller resistor not help here?

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$. So $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$.

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V. A smaller resistor does produce less noise per hertz, but the RC circuit becomes more broadband ($1/RC$ larger). The two effects cancel exactly. Only a larger capacitor reduces the noise.
:::
:::

## Stage 10: The matched filter (correlation filter)

<span class="anker" id="stufe-10"></span>

:::zweck
A known pulse $s(t)$ arrives corrupted by noise. With which filter does it become most clearly visible at the sampling instant $T$?
:::

**The approach.** The receiver input carries $s(t)+n(t)$ with white noise $n$. A filter $h$ delivers $y=g+n_e$ with the signal component $g=s*h$ and the noise component $n_e=n*h$. Sampling takes place at $T$. The signal-to-noise ratio there is

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

The fraction on the right is the square of a correlation coefficient ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), between $h(\tau)$ and $s(T-\tau)$. It is at most 1, and it equals 1 exactly when both have the same shape.

:::satz Theorem 10.1 (Matched filter)
<span class="anker" id="satz-10-1"></span>

Against white noise, the best achievable signal-to-noise ratio is

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{achieved with}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**How to read it:** The best impulse response is the signal itself, time-reversed and shifted by $T$: the __matched filter__ (correlation filter). Its output without noise is $g(t)=a\,\varphi^E_{ss}(t-T)$, the shifted ACF of the signal, and it is sampled exactly at its maximum. Surprisingly, the result depends only on the *energy* of the signal, not on its shape. A short, high pulse is as good as a long, flat one with the same energy. For the filter to be causal, $T$ must be at least the duration of the signal. A __correlator__ is equivalent: it multiplies the received signal by $s(t)$ and integrates over the duration of the signal.

:::aufgabe Exercise 10 ★★ A rectangular pulse in noise
<span class="anker" id="aufg-10"></span>

A rectangular pulse of height 1 V and duration 1 ms is received together with white noise of power spectral density $N_0=10^{-6}$ V$^2$/Hz.

<ol class="al">

<li>

What does the matched filter look like, and what $S_a/N$ (in dB) does it achieve?

</li>

<li>

What does the output look like without noise, and when must it be sampled?

</li>

<li>

The pulse is shortened to 0.25 ms, with the same height. What changes?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: again a rectangle of 1 ms, causal for $T\ge1$ ms. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s, so $S_a/N=10^{-3}/10^{-6}=1000$, that is, 30 dB.

(b) The ACF of the rectangle, a triangle of width 2 ms, shifted by $T$: it rises from $t=T-1$ ms and reaches its maximum at $t=T$. For $T=1$ ms, you sample exactly at the end of the pulse; at that moment the filter has “seen” all of it.

(c) $E_s$ drops to a quarter, $S_a/N=250$, that is, 24 dB, 6 dB worse. Only the energy counts. At the same height, a shorter pulse means less energy.
:::
:::

## Stage 11: Error probability in binary reception

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

:::abbildung et3/k7pe
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

## Stage 12: Discrete-time random signals

<span class="anker" id="stufe-12"></span>

:::zweck
Everything also holds for sequences of random numbers, with sums instead of integrals.
:::

If a process band-limited to $f_\mathrm g$ is sampled with $T\le\frac{1}{2f_\mathrm g}$, the samples form a discrete-time process $s(n)$. Distributions, expected values and correlations are defined as before; the time averages are sums, for example $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. Through an LSI system with $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

with the periodic power spectral density $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ and $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. __Discrete-time white noise__ has $\Phi_{ss,\mathrm a}=N$ and $\varphi_{ss}(m)=N\delta(m)$: successive numbers are uncorrelated. Unlike in the continuous-time case, its power is finite, $L_s=N$.

**Example 1: averaging two values.** Uniformly distributed white noise ($\sigma_s^2=\frac1{12}$) passes through $h(n)=\frac12[\delta(n)+\delta(n-1)]$, that is, $g(n)=\frac12[s(n)+s(n-1)]$. With $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

The variance is halved to $\frac{1}{24}$, and neighboring output values are now correlated (they share an input value). The output values have a triangular distribution, because each is half the sum of two independent, uniformly distributed numbers. A simulation with 200,000 numbers gives the variance 0.0415 instead of $\frac1{24}=0.0417$.

**Example 2: recursive filter (AR(1) process).** White noise of variance $\sigma_s^2$ passes through $h(n)=b^n\varepsilon(n)$ ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). With $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

For $b=0.6$, the variance is $1.56$ times the input variance, and neighboring values have the correlation coefficient $0.6$. The closer $b$ is to 1, the stronger the low frequencies (Fig. [5](#abb-5)).

:::abbildung et3/k7ar
Power spectral densities of AR(1) processes, periodic with period 1. For $b=0.6$ the density ranges from 6.25 ($f=0$) to 0.39 ($f=\frac12$), for $b=0.9$ from 100 to 0.28.
:::

:::aufgabe Exercise 12 ★★ AR(1) process
<span class="anker" id="aufg-12"></span>

Uniformly distributed white noise ($\sigma_s^2=\frac1{12}$) passes through $g(n)=s(n)+0.6\,g(n-1)$.

<ol class="al">

<li>

Compute the output variance and $\varphi_{gg}(1)/\varphi_{gg}(0)$.

</li>

<li>

Derive $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ using the geometric series.

</li>

<li>

Is the output still uniformly distributed? What distribution do you roughly expect, and why?

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0.36}=0.130$, $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0.6$. The simulation gives 0.130 and 0.600.

(b) For $m\ge0$: $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$. The impulse ACF is even, so $b^{|m|}$ holds.

(c) No longer uniformly distributed: each output value is a weighted sum of many independent input values, $g(n)=\sum_kb^ks(n-k)$. By the central limit theorem, this is approximately Gaussian. For $b=0.6$, only a few terms contribute noticeably, so the approximation is rough, but the distribution is already clearly bell-shaped.
:::
:::

:::kern Key points
<ul>

<li>

Ensemble average $\mathrm E\{\cdot\}$; stationary: independent of shifts; ergodic: time average $=$ ensemble average.

</li>

<li>

$m_s$ (DC component), $L_s=\mathrm E\{s^2\}$ (power), $\sigma_s^2=L_s-m_s^2$ (AC power).

</li>

<li>

ACF: $\varphi_{ss}(0)=L_s$, even, maximum at 0; covariance $\mu=\varphi-m^2$; sum: $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$.

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$, $p_s=P_s'$; $m_s=\int xp_s$, $L_s=\int x^2p_s$; uniform distribution $\sigma^2=a^2/12$.

</li>

<li>

Characteristic curve: $p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$; quantization error $\Delta^2/12$, 6 dB per bit.

</li>

<li>

Independent $\Rightarrow$ uncorrelated; sum of independent variables: $p_s=p_f*p_g$; Gaussian: $\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$.

</li>

<li>

LTI: $m_g=m_sH(0)$, $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$, $\Phi_{gg}=\Phi_{ss}|H|^2$, $L=\int\Phi\,\mathrm{d} f$.

</li>

<li>

White: $\Phi=N_0$, $\varphi=N_0\delta$; thermal $\mathrm E\{u^2\}=4kTRf_\mathrm g$, $kT\approx4$ pW/GHz.

</li>

<li>

Matched filter: $h=a\,s(T-t)$, $(S_a/N)_{\max}=E_s/N_0$; $P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$.

</li>

</ul>
:::
