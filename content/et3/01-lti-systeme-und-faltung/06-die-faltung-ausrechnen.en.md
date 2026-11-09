---
title: Stage 5: Evaluating the convolution
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3210600
summary: The integral (4.2) has to be evaluated for concrete signals.
tags: 
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
The integral [(4.2)](das-faltungsintegral.html#gl-4-2) has to be evaluated for concrete signals. The key is to draw both factors against the integration variable $\tau$.
:::

**The recipe.** For a fixed instant $t$:

<ol>

<li>

Draw $s(\tau)$ against $\tau$.

</li>

<li>

Draw $h(-\tau)$: *flip* $h$ about the vertical axis.

</li>

<li>

$h(t-\tau)$: *shift* the flipped $h$ to the right by $t$.

</li>

<li>

⁠*Multiply* the two and *integrate* over $\tau$: the result is $g(t)$.

</li>

</ol>

As $t$ increases, the flipped $h$ slides from left to right across $s$. Wherever the two do not overlap, $g(t)=0$.

Why flipped? As a function of $\tau$, the argument $t-\tau$ decreases as $\tau$ increases. The beginning of $h$ (age zero) lies at $\tau=t$, and older impulses lie further to the left. For the RC circuit, $h$ is largest at the beginning: the system “remembers” the most recent past most strongly.

::::beispiel RC circuit and rectangular pulse
The impulse response of the RC circuit with the time constant $T=RC$ is a decaying exponential pulse of area 1. The short impulse charges the capacitor abruptly to $1/T$, after which it discharges through $R$:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Input: a rectangle of height $a$ from $0$ to $T_0$. Figure [6](#abb-6) shows the position of the two factors at two instants. There are three regions:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$
::::

:::herleitung Response to the rectangular pulse
⁠**$t<0$:** The shifted $h(t-\tau)$ is nonzero only for $\tau\le t<0$, and $s(\tau)$ only for $\tau\ge0$. No overlap, $g=0$.

⁠**$0\le t\le T_0$:** Overlap for $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Overlap only for $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

In the reference model ($a=1$, $T_0=T=1$ s): $g(0.5)=0.3935$, $g(1)=0.6321$, $g(2)=0.2325$, $g(3)=0.0855$. This is the same curve as $g_0$ in Fig. [4](was-ein-lti-system-ist.html#abb-4).

:::abbildung et3/k1schieben 6
Graphical convolution, $a=1$, $T_0=T=1$ s. Blue: $s(\tau)$. Red: $h(t-\tau)$, flipped and shifted by $t$. The orange area is $g(t)$: 0.3935 at $t=0.5$ s (partial overlap), 0.2325 at $t=2$ s (the whole rectangle lies in the decayed part of $h$). Right: the complete response with both points.
:::

:::frage Why do we flip $h$ and not $s$?
You may also flip $s$ instead of $h$: the substitution $\tau'=t-\tau$ turns $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ into $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$. Flip whichever function makes the shifting easier to follow, usually the one with the simpler shape.
:::

:::ltspice Response to the rectangular pulse
⁠**Draw:** the RC circuit from Stage [2](ein-erstes-system-das-rc-glied.html#stufe-2) with the source `PULSE(0 1 0 1u 1u 1)`: height 1 V, duration 1 s.

⁠**Directives:** `.tran 0 20 0 1m`, one measurement per instant such as `.meas tran g2 FIND V(out) AT=2`, plus `.meas tran gmax MAX V(out)` and `.meas tran area INTEG V(out)`.

⁠**What you see:** $g(0.5)=0.3935$, $g(1)=0.6321$, $g(2)=0.2325$ and $g(3)=0.0855$, exactly as given by [(5.2)](#gl-5-2). Compare `gmax` and `area` with your result from Exercise [6](#aufg-6).
:::

:::aufgabe Exercise 5 ★★ Rectangle with rectangle
<span class="anker" id="aufg-5"></span>

Compute $\operatorname{rect}(t)*\operatorname{rect}(t)$ with the recipe. Distinguish $|t|>1$, $-1\le t\le0$ and $0\le t\le1$. Which elementary signal comes out?

:::loesung
The flipped rectangle is again $\operatorname{rect}$ (it is symmetric); after shifting, it occupies $[t-\frac12,t+\frac12]$. The integral is the length of the overlap with $[-\frac12,\frac12]$:

<ul>

<li>

$|t|>1$: no overlap, 0.

</li>

<li>

$-1\le t\le0$: overlap from $-\frac12$ to $t+\frac12$, length $1+t$.

</li>

<li>

$0\le t\le1$: overlap from $t-\frac12$ to $\frac12$, length $1-t$.

</li>

</ul>

Together, $1-|t|$ for $|t|\le1$: $\operatorname{rect}*\operatorname{rect}=\Lambda$. Numerically: 1.000, 0.500 and 0.200 at $t=0$, 0.5 and 0.8.
:::
:::

:::aufgabe Exercise 6 ★★ Checking the rectangle response
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Show that [(5.2)](#gl-5-2) is continuous at $t=T_0$. Why must it be continuous?

</li>

<li>

Where does $g(t)$ have its maximum, and how large is it in the reference model?

</li>

<li>

Show that the area under $g(t)$ equals $aT_0$, and justify this without calculation using $\int h\,\mathrm{d} t=1$.

</li>

</ol>

:::loesung
(a) At $t=T_0$: $a(1-\mathrm{e}^{-T_0/T})$ and $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$, which are equal. Physically: the capacitor voltage cannot jump, because that would require an infinite current. Mathematically: the convolution of a bounded signal with an integrable $h$ is continuous.

(b) During the pulse $g$ rises, and afterwards it falls. The maximum is at $t=T_0$: $g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0.632$.

(c) By calculation:

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

Without calculation: the area of a convolution is the product of the areas, $\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Numerically: 1.000.
:::
:::
