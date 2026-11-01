---
title: Correlation Functions
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260100
summary: How similar are two signals, and how is the energy distributed over frequency?
tags: signal energy, energy signal, power, power signal, correlation coefficient, orthogonal, autocorrelation function, cross-correlation function
lang: en
---

## What this is about

A radar sends out a pulse and searches the received signal for its echo. A mobile phone searches the noise for a known synchronization sequence. Both ask the same question: *How similar is one signal to another, and at which shift is it most similar?* The answer is given by the correlation function. Its Fourier transform also tells you how the energy of a signal is distributed over the frequencies.

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

The similarity of two signals is measured by the integral of their product. The correlation function does this for every shift $\tau$; it is a convolution with the flipped signal.

</li>

<li>

The Fourier transform of the autocorrelation function is the energy spectral density $|S(f)|^2$. At $\tau=0$ it equals the energy (Parseval).

</li>

<li>

An LTI system multiplies energy spectral densities by $|H(f)|^2$ and convolves autocorrelation functions with the autocorrelation function of $h$.

</li>

</ol>
:::

**One principle behind all the results.** Correlation is convolution with a flipped signal. That is why all the tools of convolution apply:

| Result | Where it comes from |
|---|---|
| Correlation coefficient | energy of the difference of two normalized signals (Stage [2](#stufe-2)) |
| Correlation product | convolution with the flipped, conjugated signal (Stage [3](#stufe-3)) |
| ACF even, maximum at 0 | flipping, and a signal is most similar to itself (Stage [3](#stufe-3)) |
| Energy spectral density, Parseval | flipping and conjugating become $S^*$, convolution becomes a product (Stage [4](#stufe-4)) |
| Wiener–Lee | associative law of convolution (Stage [5](#stufe-5)) |
| Discrete-time, periodic, DFT | the same calculation with sums (Stage [7](#stufe-7)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
Rectangular pulse $\operatorname{rect}(t)$, triangle $\Lambda(t)$, exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$ (the impulse response of the RC circuit with $RC=1$ s) and the sequence $(1,2,1)$. The script `rechnung_kap6.py` recomputes the numbers.
:::

## Stage 1: Energy and power

<span class="anker" id="stufe-1"></span>

:::zweck
Before comparing signals, you need a measure of their “size”. In system theory this is the energy, or, for infinitely long signals, the power.
:::

In a resistor $R$, the energy $\frac1R\int u^2\mathrm{d} t$ is converted into heat during the time from $t_1$ to $t_2$. Without the factor $1/R$, the expression is called the __signal energy__:

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

If it is finite, $s$ is called an __energy signal__ (for example, any pulse). If a signal lasts infinitely long without decaying (a cosine, a step), its energy is infinite. Then you measure the average __power__:

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

If it is finite, $s$ is called a __power signal__. For periodic signals, averaging over one period is sufficient. For Dirac impulses, energy and power are not defined ($\delta^2$ does not exist).

:::aufgabe Exercise 1 ★ Energy or power?
<span class="anker" id="aufg-1"></span>

Find the energy or the power of (a) $a\operatorname{rect}(t/T)$, (b) $\varepsilon(t)\mathrm{e}^{-t}$, (c) $A\cos(2\pi Ft)$, (d) $\varepsilon(t)$.

:::loesung
(a) $E=a^2|T|$. (b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$. (c) Infinite energy, power $\frac{A^2}{2}$ (the mean value of $\cos^2$ is $\frac12$). (d) Infinite energy, power $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$: the signal is 1 for half of the time.
:::
:::

## Stage 2: Measuring similarity, the correlation coefficient

<span class="anker" id="stufe-2"></span>

:::zweck
How do you measure with a single number how similar two signals are? You measure how large their difference is.
:::

**The idea.** The energy of the difference $\Delta(t)=s(t)-g(t)$ is small when the signals are similar. Multiplied out:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

So the difference lies solely in the integral of the product. To keep the size of the signals from counting, you normalize both to the energy 1. Then $E_\Delta=2-2\operatorname{Re}\,p_{sg}$ with the __correlation coefficient__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**How to read it:** $|p_{sg}|\le1$ (Cauchy–Schwarz inequality). $p=1$ means $s=a\,g$ with $a>0$: the same shape. $p=-1$ means $s=-a\,g$: the same shape, opposite sign. $p=0$ means $\int s^*g\,\mathrm{d} t=0$; the signals are __orthogonal__, like the harmonics of a Fourier series in [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Example: $\operatorname{rect}(t)$ and $\Lambda(t)$ have $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0.75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$, so $p=0.919$.

:::aufgabe Exercise 2 ★★ Correlation coefficients
<span class="anker" id="aufg-2"></span>

Compute $p$ for (a) $\operatorname{rect}(t)$ and $\operatorname{rect}(t-0.5)$, (b) $\operatorname{rect}(t)$ and $\Lambda(t)$ (result above), (c) $\operatorname{rect}(t)$ and $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) The rectangles overlap over a length of 0.5, so $\int=0.5$, and both energies are 1: $p=0.5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0.75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0.75}{\sqrt{2/3}}=0.919$. Very similar shapes. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$; the signals are orthogonal, although they are equal on the right half.
:::
:::

## Stage 3: Correlation function and correlation product

<span class="anker" id="stufe-3"></span>

:::zweck
An echo is similar to the transmitted pulse, but shifted. You therefore compare for every shift $\tau$.
:::

:::definition Definition 3.1 (Correlation function for energy signals)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau). \tag{3.1}$$

For $g=s$ it is called the __autocorrelation function__ (ACF) $\varphi^E_{ss}(\tau)$, otherwise the __cross-correlation function__ (CCF). Divided by $\sqrt{E_sE_g}$, it is called normalized.
:::

⁠**How to read it:** You shift $g$ to the left by $\tau$ and form the integral of the product. The second equals sign is the heart of the matter: correlation is convolution with the flipped, conjugated signal. That is why it is also called the __correlation product__. Unlike convolution, nothing is flipped here; both signals run in the same direction.

:::herleitung Correlation as convolution
Set $t=-\vartheta$ in [(3.1)](#gl-3-1): $\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$. This is the convolution integral of $s^*(-\tau)$ with $g(\tau)$.
:::

:::satz Theorem 3.2 (Properties of correlation functions)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-2"></span>
<span class="anker" id="gl-3-3"></span>
$$\begin{aligned} &\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)\ \ (\text{even for real }s),\\ &|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s. \end{aligned} \tag{3.2|3.3}$$

A time-limited signal has an ACF of twice the duration.
:::

⁠**How to read it:** A signal is most similar to itself without a shift, and there the ACF is its energy. The ACF of a rectangle is the triangle: $\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$, twice as wide as the rectangle (Fig. [1](#abb-1), left).

**Example: finding an echo.** The transmitted signal is $s=\operatorname{rect}(t)$; the received signal is the attenuated, delayed echo $g=0.5\operatorname{rect}(t-3)$. The CCF is $\varphi^E_{sg}(\tau)=0.5\,\Lambda(\tau-3)$: its maximum lies at $\tau=3$, the delay, and its height $0.5=0.5\cdot E_s$ indicates the attenuation (Fig. [1](#abb-1), right). This is how a radar measures distance.

:::abbildung et3/k6korr
Left: the ACF of the rectangle is the triangle, maximum $=E_s=1$ at $\tau=0$, twice the width. Right: the CCF between the transmitted pulse and the echo $0.5\operatorname{rect}(t-3)$ has its maximum at the delay $\tau=3$.
:::

:::frage Convolution and correlation look almost the same. What is the difference?
In convolution, $\int s(\tau)h(t-\tau)\mathrm{d}\tau$, the second signal runs backward ($-\tau$): the system “remembers” the past. In correlation, $\int s^*(t)g(t+\tau)\mathrm{d} t$, both run forward: you place one shape exactly over the other and measure how well they match. Mathematically, the difference is precisely the flipping; that is why correlation is convolution with the flipped signal.
:::

:::ltspice Finding an echo with a moving integrator
A filter that at every moment integrates over the last second forms $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$. With $s=\operatorname{rect}(t)$ this is exactly the CCF [(3.1)](#gl-3-1), delayed by 0.5 s: $y(t)=\varphi^E_{sg}(t-0.5)$. The filter computes it for all $\tau$ while the signal is coming in.

⁠**Draw:** a `voltage` source at net `g` with `PULSE(0 0.5 2.5 1u 1u 1)`, the echo $0.5\operatorname{rect}(t-3)$. Two behavioural sources `bv`: at net `int` with `V=idt(V(g))` (running integral) and at net `y` with `V=V(int)-delay(V(int),1)` (integral over the last second).

⁠**Directives:** `.tran 0 6 0 1m`, `.meas tran ymax MAX V(y)`.

⁠**What you see:** `V(y)` is the triangle $0.5\,\Lambda(t-3.5)$ with its maximum 0.5 at $t=3.5$ s: the delay of 3 s plus 0.5 s, because the filter has finished integrating only at the end of the echo. The height 0.5 is the attenuation of the echo.

⁠**For Exercise [3](#aufg-3):** input `PULSE(0 1 0 1u 1u 1 2 2)`, the double rectangle, each 0.5 s later than in the text. For `y` use

`V=V(int)-delay(V(int),1)+delay(V(int),2)-delay(V(int),3)`.

This filter integrates over two windows that match the double rectangle, and `V(y)` is its ACF, shifted by 3 s. Compare with your result from Exercise [3](#aufg-3)(a).
:::

:::aufgabe Exercise 3 ★★ Echo and repetition
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

A signal consists of two rectangles: $s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$. Find its ACF. How can you see the repetition in it?

</li>

<li>

Check [(3.3)](#gl-3-3) for this signal.

</li>

</ol>

:::loesung
(a) With $\operatorname{rect}(-\tau)=\operatorname{rect}(\tau)$ and $\operatorname{rect}*\operatorname{rect}=\Lambda$, the four partial products give

$$\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2).$$

The side peaks at $\tau=\pm2$ show the spacing of the repetition. There, in each case, one of the two rectangles lies over the other. At $\tau=0$ both lie on top of each other, which gives twice the height.

(b) $\varphi^E_{ss}(0)=2=E_s=1+1$, and the side peaks have only the value 1.
:::
:::

## Stage 4: Energy spectral density

<span class="anker" id="stufe-4"></span>

:::zweck
What is the Fourier transform of a correlation function? It shows how the energy is distributed over the frequencies.
:::

:::satz Theorem 4.1 (Wiener–Khinchin for energy signals)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**How to read it:** $|S(f)|^2$ is called the __energy spectral density__. It is real, never negative and, for real signals, even in $f$. The phase of the signal is lost: all signals with the same magnitude spectrum have the same ACF. $S^*G$ is called the __cross energy spectral density__. The derivation needs only the convolution theorem, time reversal and conjugation: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** At $\tau=0$ the ACF is the energy. With the area theorem:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Two orthogonal signals also have orthogonal spectra: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

**Example: the exponential pulse.** $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ has $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$, so $|S|^2=\frac{1}{1+(2\pi f)^2}$. This is also $\operatorname{Re}\{S\}$, and its inverse transform is the even part of the signal ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

The same value follows from $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ in the time domain and from $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ in the frequency domain. Figure [2](#abb-2) shows the signal, its ACF and both spectra.

:::abbildung et3/k6exp
Exponential pulse ($RC=1$ s). Left: the signal and its ACF $\frac12\mathrm{e}^{-|\tau|}$ (even, maximum $=E_s=\frac12$). Right: the magnitude spectrum and the energy spectral density, which decays faster: the energy is concentrated at low frequencies.
:::

:::aufgabe Exercise 4 ★ Checking Parseval
<span class="anker" id="aufg-4"></span>

Compute the energy of $\operatorname{rect}(t)$ in the time domain, and from its spectrum with [(4.2)](#gl-4-2). Which well-known integral of the si function follows from this?

:::loesung
Time domain: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Frequency domain: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. Hence $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::

## Stage 5: Correlation and LTI systems

<span class="anker" id="stufe-5"></span>

:::zweck
What does an LTI system do to the ACF and the energy spectral density? And how do you measure a system with cross-correlation?
:::

:::satz Theorem 5.1 (Wiener–Lee)
<span class="anker" id="satz-5-1"></span>

For $g=s*h$:

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung Wiener–Lee
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$. Rearrange using the commutative and associative laws: $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$. Likewise, $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$.
:::

⁠**How to read it:** The system multiplies the energy at each frequency by $|H|^2$. The phase of the system plays no role for the energy. Equation [(5.2)](#gl-5-2) is a measurement method: if the input has an ACF that is almost a weighted Dirac impulse $c\,\delta(\tau)$ (a very short pulse or broadband noise, [Part 7](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)), then the cross-correlation between input and output is almost $c\,h(\tau)$, that is, the impulse response up to the factor $c$. Unlike $|H|^2$, it also contains the phase.

:::ltspice Energy before and after the RC circuit
⁠**Draw:** a behavioural source `bv` at net `s` with `V=exp(-time)*(time>0)`, the exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$. The factor `(time>0)` makes LTspice compute the initial state at $t=0$ with 0 V, so the capacitor starts empty. After it the RC circuit (`res` with `1Meg`, `cap` with `1u`) with its output at net `g`.

⁠**Directives:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` and `.meas tran Eg INTEG V(g)*V(g)`, the energies as in [(1.1)](#gl-1-1).

⁠**What you see:** `Es` $=0.500$, as $E_s=\varphi^E_{ss}(0)=\frac12$ in Stage [4](#stufe-4). Compare `Eg` with your result from Exercise [5](#aufg-5). The output energy is smaller because the RC circuit multiplies the energy at each frequency by $|H|^2\le1$.
:::

:::aufgabe Exercise 5 ★★ Energy at the output
<span class="anker" id="aufg-5"></span>

The exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$ passes through an RC circuit with $RC=1$ s.

<ol class="al">

<li>

Find $|G(f)|^2$ and from it the output energy. Hint: $\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$.

</li>

<li>

Check in the time domain with $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ ([Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), two RC circuits in cascade).

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$. With $x=2\pi f$: $E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$.

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$. Both ways agree. The energy drops from $\frac12$ to $\frac14$ because the second RC circuit attenuates the higher frequencies further.
:::
:::

## Stage 6: Correlation of bandpass signals

<span class="anker" id="stufe-6"></span>

:::zweck
Correlation functions of bandpass signals, too, are computed with the complex envelopes ([Part 5](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)).
:::

The CCF of two real bandpass signals is again a bandpass signal:

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

The flipped signal has the envelope $s_T^*(-t)$, because

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

With the transmission rule $g_T=\frac12s_T*h_T$ from [Part 5](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html):

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**How to read it:** The correlation of two bandpass signals is half the correlation of their envelopes, modulated onto the carrier. The energy of a bandpass signal is half the energy of its complex envelope: a cosine of amplitude $|s_T|$ has, on average, only half the power.

## Stage 7: Discrete-time and periodic correlation

<span class="anker" id="stufe-7"></span>

:::zweck
For samples, the integral becomes a sum. With the DFT, correlations can be computed quickly.
:::

:::satz Theorem 7.1 (Discrete-time correlation)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{period }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

For sampled low-pass signals, $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ and $E_s=T\sum_n|s(nT)|^2$. A discrete-time energy signal is a square-summable sequence.

**Example.** $s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ for $m=-2,\dots,2$. Maximum $6=E_s$ at $m=0$, even, five values instead of three. Check with Wiener–Khinchin at $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.

**Periodic correlation.** As with convolution ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)), the following holds for sequences with the period $M$:

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Computed with the FFT, this is called __fast correlation__. For the periodic correlation to reproduce the ordinary one, $M$ must be large enough. For $(1,2,1)$, $M=3$ gives the overlapped sequence $(6,5,5)$, whereas $M=5$ gives $(6,4,1,1,4)$, the ordinary ACF arranged cyclically.

**Power signals.** For signals of infinite energy, you average:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

If both signals are periodic with the same period, one period is sufficient, and the correlation function is periodic as well. Example: $A\cos(2\pi Ft+\varphi_0)$ has the ACF $\frac{A^2}{2}\cos(2\pi F\tau)$. The phase $\varphi_0$ has disappeared, and at $\tau=0$ the ACF equals the power $\frac{A^2}{2}$.

:::aufgabe Exercise 6 ★ Discrete ACF
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Verify the ACF of $(1,2,1)$ by hand.

</li>

<li>

Find the ACF of $(1,-1)$. What does $\varphi(\pm1)<0$ tell you about the signal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. A negative value at the shift 1 means that neighboring values tend to have opposite signs: the signal changes quickly. Consistent with this, $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ is zero at $f=0$ and maximal at $f=\frac12$: a high-pass signal.
:::
:::

:::aufgabe Exercise 7 ★★ ACF of a cosine
<span class="anker" id="aufg-7"></span>

Derive the ACF of $A\cos(2\pi Ft+\varphi_0)$ with [(7.4)](#gl-7-4) over one period. Why does $\varphi_0$ drop out, and what does this mean for measuring the phase with the ACF?

:::loesung
With $\omega=2\pi F$ and $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

The second integral runs over two full periods and is zero. The phase $\varphi_0$ only shifts the time origin, and averaging over all times knows no origin. The ACF of a single signal therefore cannot measure a phase. The phase difference of *two* signals, on the other hand, is revealed by the cross-correlation.
:::
:::

:::kern Key points
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$; $L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$.

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$, $|p|\le1$, $p=0$: orthogonal.

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$; $\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$.

</li>

<li>

ACF: even (for real signals), maximum $\varphi^E_{ss}(0)=E_s$, twice the duration.

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$, $\varphi^E_{sg}\leftrightarrow S^*G$; Parseval $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$.

</li>

<li>

Wiener–Lee: $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$, $|G|^2=|S|^2|H|^2$; $\varphi^E_{sg}=\varphi^E_{ss}*h$.

</li>

<li>

Bandpass: $\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$.

</li>

<li>

Discrete: $\varphi(m)=\sum s^*(n)g(n+m)$, $\leftrightarrow|S_\mathrm a|^2$; periodic: $S_d^*G_d$.

</li>

</ul>
:::
