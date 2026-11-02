---
title: Stage 3: Correlation function and correlation product
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260400
summary: An echo is similar to the transmitted pulse, but shifted.
tags: autocorrelation function, cross-correlation function, correlation product
lang: en
---

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

:::abbildung et3/k6korr 1
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
