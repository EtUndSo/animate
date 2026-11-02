---
title: Stage 1: Describing signals
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3210200
summary: Before studying systems, you need a language for signals: a few basic shapes and two operations on the time axis, shifting and stretching.
tags: signal, normalized, period, frequency
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before studying systems, you need a language for signals: a few basic shapes and two operations on the time axis, shifting and stretching.
:::

A __signal__ is the course of a physical quantity over time, written as a function $s(t)$. In system theory one usually works with __normalized__ quantities: times in multiples of 1 s, voltages in multiples of 1 V. Equations between physical quantities then become equations between pure numbers, and $\mathrm{e}^{-t}$ can be written down without any trouble with units.

**Elementary signals.** Some signals can be described by a simple expression and come up again and again (Fig. [1](#abb-1)):

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{(Gaussian)},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

The step $\varepsilon(t)$ and the rectangle $\operatorname{rect}(t)$ jump. Which value holds exactly at the jump is a matter of convention. A common choice there is $\tfrac12$: then rectangles placed side by side add up to exactly 1 everywhere.

:::abbildung et3/k1elementar 1
Elementary signals. Bottom right: a shifted and stretched rectangle with center at $t_0=2$, width $T=2$ and height $a=0.8$.
:::

**Shifting and stretching.** New signals arise from a given one when the time axis is transformed:

<ul>

<li>

⁠**Shifting:** $t\to t-t_0$. For $t_0>0$ the signal is *delayed* by $t_0$, that is, moved to the right.

</li>

<li>

⁠**Stretching:** $t\to t/T$. For $|T|>1$ the signal becomes wider, for $0<|T|<1$ narrower, and for $T<0$ it is also flipped.

</li>

</ul>

Combining both, plus an amplitude $a$, gives for example the rectangular pulse

<span class="anker" id="gl-1-1"></span>
$$s(t)=a\operatorname{rect}\Bigl(\frac{t-t_0}{T}\Bigr)=\begin{cases}a & |t-t_0|\le |T|/2\\ 0 & \text{otherwise}\end{cases} \tag{1.1}$$

with center $t_0$, duration $|T|$ and height $a$. To check this, substitute the argument $(t-t_0)/T$ into the definition of $\operatorname{rect}$. Likewise, $\sin(2\pi t/T)=\sin(2\pi Ft)$ is the stretched sine with __period__ $T$ and __frequency__ $F=1/T$.

:::frage Why does $t-t_0$ shift the signal to the right, even though something is subtracted?
At time $t$ the new signal shows the value that the old one had at time $t-t_0$, that is, *earlier*. Everything the old signal did, the new one does $t_0$ later. The easiest check is at a distinctive point: the edge of $\varepsilon(t-t_0)$ lies where the argument becomes zero, at $t=t_0$.
:::

**The complex exponential.** The most important signal for system theory is

$$\mathrm{e}^{\mathrm{j}2\pi Ft}=\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft).$$

By Euler's formula, a complex conjugate pair yields the real oscillations:

$$\cos(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2},\qquad \sin(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}-\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2\mathrm{j}}.$$

For an oscillation, a delay by $t_0$ appears as a phase shift:

<span class="anker" id="gl-1-2"></span>
$$\cos\bigl(2\pi F(t-t_0)\bigr)=\cos(2\pi Ft+\varphi)=\operatorname{Re}\bigl\{\mathrm{e}^{\mathrm{j}2\pi Ft}\,\mathrm{e}^{\mathrm{j}\varphi}\bigr\},\qquad\varphi=-2\pi Ft_0. \tag{1.2}$$

⁠**In short:** for an oscillation, delaying is the same as rotating the phase, and for $\mathrm{e}^{\mathrm{j}2\pi Ft}$ it is even the same as multiplying by the number $\mathrm{e}^{\mathrm{j}\varphi}$.

:::aufgabe Exercise 1 ★ Shifting, stretching, phase
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Where does $s(t)=2\operatorname{rect}\bigl(\frac{t-3}{4}\bigr)$ begin and end, and how high is the pulse?

</li>

<li>

Write down a rectangular pulse that has the height 0.5 V from $t=1$ s to $t=4$ s.

</li>

<li>

Sketch $s(-t)$ for $s(t)=\varepsilon(t-1)$. Where is the edge?

</li>

<li>

A cosine with $F=50$ Hz is delayed by $t_0=5$ ms. What is its phase $\varphi$ afterwards?

</li>

</ol>

:::loesung
(a) Center $t_0=3$, duration $T=4$: from $t=1$ to $t=5$, height 2.

(b) Center 2.5 s, duration 3 s: $s(t)=0.5\operatorname{rect}\bigl(\frac{t-2.5}{3}\bigr)$.

(c) $s(-t)=\varepsilon(-t-1)$. The edge lies where the argument becomes zero: $-t-1=0$, so $t=-1$. The value is 1 where the argument is $\ge0$, that is, for $t\le-1$. A flipped step: 1 to the left of $-1$, 0 to the right of it.

(d) $\varphi=-2\pi Ft_0=-2\pi\cdot50\,\mathrm{Hz}\cdot5\,\mathrm{ms}=-\pi/2=-90^\circ$. A delay of a quarter period is a quarter turn.
:::
:::
