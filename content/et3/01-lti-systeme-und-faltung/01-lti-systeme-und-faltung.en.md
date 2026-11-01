---
title: Signals, LTI Systems and Convolution
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3210100
summary: Why the response to a single impulse describes the whole system
tags: signal, normalized, period, frequency, system, transformation, linear, time-invariant
lang: en
---

## What this is about

A system takes in one signal and puts out another: an RC circuit smooths a voltage, a loudspeaker cabinet colors a sound, a measuring amplifier delays and amplifies. The question of this article is: *What do you need to know about a system to compute its output for any input signal?*

For the large class of linear, time-invariant systems (LTI systems), the answer is surprisingly short: the response to a single, infinitely short impulse. The tool that turns this one response into every other one is convolution.

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

Every signal is a superposition of infinitely many short impulses: at each instant $\tau$, one impulse with the weight $s(\tau)\,\mathrm{d}\tau$.

</li>

<li>

An LTI system responds to a shifted impulse with the shifted impulse response $h(t-\tau)$ (time invariance), and to a sum of impulses with the sum of the responses (linearity).

</li>

<li>

Therefore the output is the convolution $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$, and $h(t)$ describes the system completely.

</li>

</ol>
:::

**One principle behind all the results.** The table links each result of this article to the principle “decompose, send one building block through, reassemble”.

| Result | Where it comes from |
|---|---|
| Convolution integral | superpose impulses, superpose shifted impulse responses (Stage [4](#stufe-4)) |
| Flipping during evaluation | $h(t-\tau)$ is the response to an impulse that arrived $t-\tau$ seconds ago (Stage [5](#stufe-5)) |
| $\delta$ is the identity element | a signal made of impulses, sent through a system that leaves every impulse unchanged (Stage [6](#stufe-6)) |
| Commutative, associative, distributive laws | swap roles, systems in cascade, systems in parallel (Stage [6](#stufe-6)) |
| Sifting property, scaling of the Dirac impulse | $\delta$ is defined only through its area (Stage [7](#stufe-7)) |
| Step response = integral of the impulse response | a step is the sum of all impulses up to $t$ (Stage [8](#stufe-8)) |
| Causality, stability | conditions on $h(t)$: zero before the impulse, finite area of $\vert h\vert $ (Stage [9](#stufe-9)) |
| Convolution without a system | the same superposition, for example for the sum of two dice (Stage [10](#stufe-10)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
<ul>

<li>

⁠**RC low-pass** with $T=RC=1$ s (for example $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Times in s, voltages in V, so all calculations are dimensionless.

</li>

<li>

⁠**Rectangular pulse** of height $a=1$ V and duration $T_0=1$ s, starting at $t=0$.

</li>

</ul>

The script `rechnung_kap1.py` recomputes the numbers and curves.
:::

## Stage 1: Describing signals

<span class="anker" id="stufe-1"></span>

:::zweck
Before studying systems, you need a language for signals: a few basic shapes and two operations on the time axis, shifting and stretching.
:::

A __signal__ is the course of a physical quantity over time, written as a function $s(t)$. In system theory one usually works with __normalized__ quantities: times in multiples of 1 s, voltages in multiples of 1 V. Equations between physical quantities then become equations between pure numbers, and $\mathrm{e}^{-t}$ can be written down without any trouble with units.

**Elementary signals.** Some signals can be described by a simple expression and come up again and again (Fig. [1](#abb-1)):

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{(Gaussian)},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

The step $\varepsilon(t)$ and the rectangle $\operatorname{rect}(t)$ jump. Which value holds exactly at the jump is a matter of convention. A common choice there is $\tfrac12$: then rectangles placed side by side add up to exactly 1 everywhere.

:::abbildung et3/k1elementar
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

⁠**In short:** for an oscillation, delaying is the same as rotating the phase, and for $\mathrm{e}^{\mathrm{j}2\pi Ft}$ it is even the same as multiplying by the number $\mathrm{e}^{\mathrm{j}\varphi}$. In [Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) this property carries the entire Laplace transform.

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

## Stage 2: A first system, the RC circuit

<span class="anker" id="stufe-2"></span>

:::zweck
The RC low-pass (Fig. [2](#abb-2)) already shows all the ideas of this article on a small scale: a complex exponential comes out merely multiplied by a number, and the circuit responds to a step with an exponential curve.
:::

**The differential equation.** The current through $R$ is $(u_1-u_2)/R$. All of it flows into the capacitor and charges it, $C\,\dot u_2=(u_1-u_2)/R$. Rearranged:

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung
RC low-pass: input $u_1$, output $u_2$ across the capacitor. In the reference model $RC=1$ s.
:::

**Input $\mathrm{e}^{\mathrm{j}2\pi Ft}$: the output is a number times the input.** If $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$ is applied, the output in the steady state has the same form, only with a different amplitude and phase: $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. The reason is that differentiation does not change the form, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Substituting into [(2.1)](#gl-2-1):

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

AC analysis with phasors gives the same result: the capacitor has the impedance $1/(\mathrm{j}2\pi FC)$, and the circuit is a voltage divider,

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

The real voltage belonging to a phasor is $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$ (RMS phasor).

:::satz Theorem 2.1 (Transfer function of the RC low-pass)
<span class="anker" id="satz-2-1"></span>

With $x=2\pi FRC$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**How to read it:** $|H|$ tells you by what factor the amplitude shrinks, and $\varphi$ by what angle the oscillation lags. At $x=1$, that is, $F=1/(2\pi RC)=0.16$ Hz in the reference model, $|H|=0.707$ and $\varphi=-45^\circ$. At $x=10$, $|H|=0.0995$ and $\varphi=-84.3^\circ$ (Fig. [3](#abb-3)). **Limiting cases:** $F\to0$ gives $H\to1$ (the capacitor has time to charge fully); $F\to\infty$ gives $H\to0$ with $\varphi\to-90^\circ$ (the capacitor acts like a short circuit).

:::abbildung et3/k1bode
Magnitude and phase of the transfer function of the RC low-pass versus $x=2\pi FRC$ (logarithmic scale). Slow oscillations pass almost unchanged; fast ones are attenuated and lag by up to $90^\circ$.
:::

**The phase in general.** For an arbitrary complex number $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$,

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{integer}, \tag{2.4}$$

where $\arctan$ returns the principal value in $[-\pi/2,\pi/2]$.

:::frage Why does the phase formula need the extra term $\lambda\pi$?
$\arctan$ sees only the ratio $\operatorname{Im}/\operatorname{Re}$. The numbers $1+\mathrm{j}$ and $-1-\mathrm{j}$ have the same ratio 1, but lie in opposite quadrants. $\arctan1=45^\circ$ is correct for $1+\mathrm{j}$. For $-1-\mathrm{j}$ the true angle is $45^\circ+180^\circ=225^\circ$, equivalently $-135^\circ$ (with $l=-1$). Whenever the real part is negative, you have to add $\pi$.
:::

**Step input: the exponential curve.** At $t=0$ the voltage $u_1=1$ V is applied; the capacitor is empty. For $t\ge0$, Kirchhoff's voltage law with the current $i$ gives

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

Differentiating gives $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$, hence $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, and integrating gives

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

because at the first instant the whole voltage is across $R$. Kirchhoff's voltage law, $u_2=1-R\,i$, then gives

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

The mechanism: the fuller the capacitor, the less voltage is left for $R$, the smaller the charging current, and the more slowly the capacitor continues to fill. This feedback makes the curve exponential.

:::ltspice RC low-pass: step response and frequency response
⁠**Draw:** a `voltage` source at net `in`, `res` with `1Meg` from `in` to `out`, `cap` with `1u` from `out` to ground, so $RC=1$ s. Careful: SPICE reads `1M` as 1 milli; mega is written `Meg`.

⁠**Step:** source `PULSE(0 1 0 1u 1u 100)`, directive `.tran 5`. A measurement such as `.meas tran g1 FIND V(out) AT=1` gives exact values; the result appears in the SPICE Error Log (View, SPICE Error Log). Expected: 0.393 at 0.5 s, 0.632 at 1 s and 0.950 at 3 s, i.e. $1-\mathrm{e}^{-t}$ as in [(2.5)](#gl-2-5).

⁠**Frequency response:** source value `AC 1`, and instead of `.tran` the directive `.ac dec 100 0.01 100`. LTspice plots the magnitude in dB (solid) and the phase (dashed). At 0.159 Hz ($x=1$) they show $-3.0$ dB, i.e. $|H|=0.707$, and $-45^\circ$. Compare the values at $x=10$ with your result from Exercise [2](#aufg-2)(a).
:::

:::aufgabe Exercise 2 ★★ Frequency response and phase
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Compute $|H|$ and $\varphi$ of the RC low-pass for $x=0$, $1$ and $10$. Which frequency in Hz corresponds to $x=10$ in the reference model?

</li>

<li>

A signal $u_1(t)=\cos(2\pi Ft)$ with $x=1$ is applied. Write down $u_2(t)$. By how many seconds does $u_2$ lag if $RC=1$ s?

</li>

<li>

Use [(2.4)](#gl-2-4) to determine the phases of $-1-\mathrm{j}$, $-\mathrm{j}$ and $-2$.

</li>

</ol>

:::loesung
(a) $x=0$: $|H|=1$, $\varphi=0$. $x=1$: $|H|=0.707$, $\varphi=-45^\circ$. $x=10$: $|H|=0.0995$, $\varphi=-84.3^\circ$. $x=10$ means $F=10/(2\pi RC)=1.59$ Hz.

(b) $u_2(t)=0.707\cos(2\pi Ft-45^\circ)$ with $2\pi F=1/\mathrm s$, so $F=0.159$ Hz. It lags by $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0.785$ s.

(c) $-1-\mathrm{j}$: $\arctan1=45^\circ$, real part negative, so add $180^\circ$: $225^\circ$, equivalently $-135^\circ$. $-\mathrm{j}$: real part zero, imaginary part negative; $\arctan(\operatorname{Im}/\operatorname{Re})$ tends to $-90^\circ$, so the phase is $-90^\circ$. $-2$: $\arctan0=0$, real part negative, so $180^\circ$.
:::
:::

## Stage 3: What an LTI system is

<span class="anker" id="stufe-3"></span>

:::zweck
The RC circuit has two properties on which everything else rests: it is linear and time-invariant. This stage defines both and shows what they make possible.
:::

A __system__ assigns an output signal to an input signal:

$$g(t)=\operatorname{Tr}\{s(t)\}.$$

Such a mapping from functions to functions is called a __transformation__. It does not map one numerical value to another: the output at time $t$ may depend on the entire past course of the input. In the RC circuit, $u_2(t)$ depends on how much charge has accumulated up to $t$.

:::definition Definition 3.1 (LTI system)
<span class="anker" id="satz-3-1"></span>

A system is called

<ul>

<li>

__linear__ if the superposition principle holds for arbitrary constants $a_i$:

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t); \tag{3.1}$$

</li>

<li>

__time-invariant__ if for every shift $t_0$:

<span class="anker" id="gl-3-2"></span>
$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0). \tag{3.2}$$

</li>

</ul>

A linear, time-invariant system is called an __LTI system__ for short (LTI stands for linear time-invariant).
:::

In the RC circuit, linearity comes from the fact that the differential equation [(2.1)](#gl-2-1) contains neither products nor squares of $u_1$ and $u_2$. Time invariance comes from the fact that $R$ and $C$ do not change with time. Every network of $R$, $L$ and $C$ is described by linear differential equations with constant coefficients. This does not hold for every LTI system, though: the ideal delay element of Stage [7](#stufe-7), for example, has no such equation.

**What the two properties allow.** If you know the response $g_0$ to a rectangular pulse $s_0$, you know, without further calculation, the response to any sum of shifted and scaled rectangular pulses. Figure [4](#abb-4) shows this for $s(t)=s_0(t)+0.5\,s_0(t-2)$: the output is $g_0(t)+0.5\,g_0(t-2)$.

:::abbildung et3/k1doppel
Left: rectangle $s_0$ (height 1 V, duration 1 s) and the response $g_0$ of the RC circuit. Right: a pair of pulses. The response (red) is the sum of $g_0(t)$ and the shifted, halved copy $0.5\,g_0(t-2)$ (dashed).
:::

:::frage Is $g(t)=2s(t)+1$ linear? Its characteristic is a straight line, after all.
No. For a linear system, zero input must give zero output: setting all $a_i=0$ in [(3.1)](#gl-3-1) gives $\operatorname{Tr}\{0\}=0$. Here $\operatorname{Tr}\{0\}=1$. The superposition principle fails as well: two inputs applied separately give $2s_1+2s_2+2$ in total, but applied together they give $2s_1+2s_2+1$. A straight line that does not pass through the origin is called *affine*, not linear.
:::

:::ltspice Checking superposition: two rectangles
⁠**Draw:** the RC circuit from Stage [2](#stufe-2), but with two `voltage` sources in series: `V1` with its negative terminal at ground and its positive terminal at net `a`, value `PULSE(0 {a1} 0 1u 1u 1)`, on top of it `V2` from `a` to `in`, value `PULSE(0 {a2} 2 1u 1u 1)`. In series the voltages add, so the RC circuit sees $a_1s_0(t)+a_2s_0(t-2)$.

⁠**Directives:** `.param a1=1 a2=0.5`, `.step param a1 list 0 1`, `.step param a2 list 0 0.5`, `.tran 0 6 0 1m`. LTspice runs all four combinations and plots them on top of each other.

⁠**What you see:** the curves $0$, $g_0(t)$, $0.5\,g_0(t-2)$ and their sum, as in Fig. [4](#abb-4). At $t=2.5$ s: $0.141+0.197=0.338$. The sum of the inputs gives the sum of the responses (linearity), and the source shifted by 2 s gives the curve shifted by 2 s (time invariance).
:::

:::aufgabe Exercise 3 ★ LTI or not?
<span class="anker" id="aufg-3"></span>

Check each system for linearity and time invariance: (a) $g(t)=3\,s(t-2)$, (b) $g(t)=s(t)^2$, (c) $g(t)=s(t)+1$, (d) $g(t)=t\,s(t)$, (e) $g(t)=s(2t)$, (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$.

:::loesung
(a) Linear and time-invariant (gain 3, delay 2): LTI. (b) Not linear: $\operatorname{Tr}\{2s\}=4s^2\neq2s^2$. Time-invariant. (c) Not linear (affine, $\operatorname{Tr}\{0\}=1$). Time-invariant. (d) Linear. Not time-invariant: $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, but $g(t-t_0)=(t-t_0)\,s(t-t_0)$. The factor $t$ is a component that changes with time. (e) Linear. Not time-invariant: $\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$, but $g(t-t_0)=s(2t-2t_0)$. Compressing time also compresses every shift. (f) LTI. Linear, because the integral is linear. Time-invariant: $\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$. Its impulse response is $\varepsilon(t)$ (Stage [8](#stufe-8)).
:::
:::

## Stage 4: The convolution integral

<span class="anker" id="stufe-4"></span>

:::zweck
With linearity and time invariance, the response to *any* signal can be computed from the response to a single short pulse. The result is the convolution integral.
:::

**The idea in four steps.**

<ol>

<li>

⁠**Decompose.** Approximate the input signal by a staircase of narrow rectangles of width $T_0$. The building block is a rectangle $s_0(t)$ of duration $T_0$ and height $1/T_0$, that is, of area 1. The stair step at $nT_0$ is this building block, shifted by $nT_0$ and weighted with $s(nT_0)\,T_0$, the area of the strip:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Send one building block through the system.** The system responds to $s_0$ with $g_0(t)$. This has to be known once.

</li>

<li>

⁠**Reassemble.** Time invariance: the shifted building block produces the shifted response. Linearity: weights and sum carry through. Hence

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Limit $T_0\to0$.** The staircase becomes the signal. The rectangle of area 1 becomes the __Dirac impulse__ $\delta(t)$, an infinitely short impulse of area 1 (Stage [7](#stufe-7)). Its response is called the __impulse response__ $h(t)$. $nT_0$ becomes the continuous variable $\tau$, $T_0$ becomes the differential $\mathrm{d}\tau$, and the sums become integrals.

</li>

</ol>

:::abbildung et3/k1treppe
Top: a triangular pulse $s(t)=\Lambda(t-1)$ and its staircase approximation with $T_0=0.5$ s. Bottom: the exact response of the RC circuit and the sum of the shifted rectangle responses. The largest deviation falls from 0.17 ($T_0=0.5$ s) to 0.08 ($0.25$ s) and 0.03 ($0.1$ s).
:::

:::satz Theorem 4.1 (Convolution integral)
<span class="anker" id="satz-4-1"></span>

Every signal $s(t)$ satisfies

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

and an LTI system with the impulse response $h(t)$ responds to it with

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**How to read it:** $\tau$ is the instant of an input impulse, and $s(\tau)\,\mathrm{d}\tau$ is its weight (the area of the strip). $h(t-\tau)$ is the response of the system at time $t$ to an impulse that arrived at time $\tau$, that is, $t-\tau$ seconds ago. The output collects all impulses of the past, each weighted by how strongly the system still “remembers” it after that time. The equation is exact and holds for every LTI system.

⁠**In short:** the output of an LTI system is the superposition of its impulse responses, shifted to every instant of the input and weighted by the input there.

:::frage Why must the rectangular building blocks have area 1?
So that the response to the building block keeps a fixed shape in the limit. A rectangle of fixed height 1 would have zero area as $T_0\to0$, and its response would vanish. With the height $1/T_0$ the area stays 1, and the response tends to $h(t)$. For the RC circuit, the peak of the response is $(1-\mathrm{e}^{-T_0})/T_0$: 0.632 for $T_0=1$ s, 0.787 for 0.5 s, 0.952 for 0.1 s, and as $T_0\to0$ it becomes $1=h(0^+)$. Throughout, the area of the response stays 1.
:::

:::frage Does the impulse $\delta(t)$ exist in reality? Then how do you measure $h(t)$?
An infinitely short impulse does not exist. But any pulse that is much shorter than the time constants of the system will do. The system then sees only its area, and the response is practically $(\text{area})\cdot h(t)$. For the RC circuit with $RC=1$ s, the peak of the response to a 1-ms pulse deviates from $h(0^+)$ by only 0.05 %. This is also how impulse responses are measured: you clap your hands in a room and record the reverberation.
:::

:::ltspice Approximating the impulse response with a short rectangle
⁠**Draw:** the RC circuit from Stage [2](#stufe-2) with the source `PULSE(0 {1/T0} 0 1n 1n {T0})`: a rectangle of width $T_0$ and height $1/T_0$, hence area 1.

⁠**Directives:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran peak MAX V(out)`, `.meas tran area INTEG V(out)`.

⁠**What you see:** The peaks are 0.632, 0.787, 0.952 and 0.9995, as given by $(1-\mathrm{e}^{-T_0})/T_0$. For the 1-ms pulse the response is practically $h(t)=\mathrm{e}^{-t}$ already. The area is 1.000 in all four runs: a pulse much shorter than $RC$ acts only through its area.
:::

:::aufgabe Exercise 4 ★★ A closer look at the staircase
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Compute the response $g_0(t)$ of the RC circuit ($RC=1$ s) to the rectangle of height $1/T_0$ from $0$ to $T_0$. To do this, use [(2.5)](#gl-2-5) and write the rectangle as the difference of two steps.

</li>

<li>

Show that $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ and that it tends to 1 as $T_0\to0$.

</li>

<li>

Why does the approximation $g_a$ in Fig. [5](#abb-5) come too late? (Hint: where does the stair step lie relative to the triangle on the rising edge, and where on the falling edge?)

</li>

</ol>

:::loesung
(a) The rectangle is $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linearity and time invariance together with the step response [(2.5)](#gl-2-5) give

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) At $t=T_0$ the second term is zero: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. With $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ for small $T_0$, this is $\approx1-T_0/2\to1=h(0^+)$. Numbers: 0.632, 0.787 and 0.952 for $T_0=1$, 0.5 and 0.1 s.

(c) Each stair step holds the value $s(nT_0)$ from the *beginning* of its interval to the end. On the rising edge the staircase therefore lies below the triangle, and on the falling edge above it: on average it is delayed by $T_0/2$. The output inherits this delay; on the falling side, $g_a$ lies above $g$ ($g_a(2)=0.508$ instead of $0.400$ for $T_0=0.5$ s). As $T_0$ gets smaller, the delay shrinks, and with it the error.
:::
:::

## Stage 5: Evaluating the convolution

<span class="anker" id="stufe-5"></span>

:::zweck
The integral [(4.2)](#gl-4-2) has to be evaluated for concrete signals. The key is to draw both factors against the integration variable $\tau$.
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

**Example: RC circuit and rectangular pulse.** The impulse response of the RC circuit with the time constant $T=RC$ is a decaying exponential pulse of area 1 (Stage [8](#stufe-8) derives it):

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Input: a rectangle of height $a$ from $0$ to $T_0$. Figure [6](#abb-6) shows the position of the two factors at two instants. There are three regions:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$

:::herleitung Response to the rectangular pulse
⁠**$t<0$:** The shifted $h(t-\tau)$ is nonzero only for $\tau\le t<0$, and $s(\tau)$ only for $\tau\ge0$. No overlap, $g=0$.

⁠**$0\le t\le T_0$:** Overlap for $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Overlap only for $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

In the reference model ($a=1$, $T_0=T=1$ s): $g(0.5)=0.3935$, $g(1)=0.6321$, $g(2)=0.2325$, $g(3)=0.0855$. This is the same curve as $g_0$ in Fig. [4](#abb-4).

:::abbildung et3/k1schieben
Graphical convolution, $a=1$, $T_0=T=1$ s. Blue: $s(\tau)$. Red: $h(t-\tau)$, flipped and shifted by $t$. The orange area is $g(t)$: 0.3935 at $t=0.5$ s (partial overlap), 0.2325 at $t=2$ s (the whole rectangle lies in the decayed part of $h$). Right: the complete response with both points.
:::

:::frage Why do we flip $h$ and not $s$?
You may also flip $s$, because convolution is commutative (Stage [6](#stufe-6)). Flip whichever function makes the shifting easier to follow, usually the one with the simpler shape.
:::

:::ltspice Response to the rectangular pulse
⁠**Draw:** the RC circuit from Stage [2](#stufe-2) with the source `PULSE(0 1 0 1u 1u 1)`: height 1 V, duration 1 s.

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

## Stage 6: Rules of convolution

<span class="anker" id="stufe-6"></span>

:::zweck
In many respects convolution behaves like multiplication. Each rule has a meaning for systems.
:::

The convolution integral is written in short as the __convolution product__ $g(t)=s(t)*h(t)$. Equation [(4.1)](#gl-4-1) then reads $s(t)=s(t)*\delta(t)$.

<ol class="al">

<li>

⁠**Identity element.** $s*\delta=s$: the Dirac impulse plays the role of the number one. A system with $h(t)=\delta(t)$ passes every signal on unchanged; it is called __ideally distortion-free__.

</li>

<li>

⁠**Commutative law.** $s*h=h*s$. Meaning: input and impulse response may swap roles. The system with the impulse response $s$ responds to the input $h$ exactly as the system $h$ responds to the input $s$.

</li>

<li>

⁠**Associative law.** $(f*s)*h=f*(s*h)$. Meaning: two systems in cascade act like one system whose impulse response is the convolution of the two impulse responses.

</li>

<li>

⁠**Distributive law.** $f*(s+h)=f*s+f*h$. Meaning: two systems connected in parallel, whose outputs are added, act like one system with the sum of the impulse responses.

</li>

<li>

⁠**Complex signals.** Because convolution is linear, it splits into real and imaginary parts:

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung Commutative law
Substitute $\tau'=t-\tau$, so $\tau=t-\tau'$ and $\mathrm{d}\tau=-\mathrm{d}\tau'$. The limits $\tau=\mp\infty$ become $\tau'=\pm\infty$; swapping them cancels the minus sign:

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke
Top: cascade connection, impulse response $h_1*h_2$ (associative law). Bottom: parallel connection with addition, impulse response $h_1+h_2$ (distributive law).
:::

:::aufgabe Exercise 7 ★★ Two RC circuits in cascade
<span class="anker" id="aufg-7"></span>

Two RC circuits with $RC=1$ s are connected in cascade. Assume that the second does not load the first (for example, with a voltage follower in between).

<ol class="al">

<li>

Compute the impulse response of the cascade, $h*h$ with $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

</li>

<li>

When is it at its maximum, and what is its area?

</li>

<li>

Why is the condition “does not load” needed?

</li>

</ol>

:::loesung
(a) For $t\ge0$:

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

So $h_{\text{cascade}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$.

(b) Derivative: $(1-t)\mathrm{e}^{-t}=0$ at $t=1$ s, maximum $\mathrm{e}^{-1}=0.368$. Area: $\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$ (product of the areas).

(c) Without decoupling, the second RC circuit draws current from the first capacitor. The voltage across the first capacitor is then no longer that of an unloaded RC circuit, and the cascade does not have $h*h$ as its impulse response. It remains an LTI system, but with a different impulse response. Convolving the individual responses assumes that no system acts back on its input.
:::
:::

## Stage 7: The Dirac impulse

<span class="anker" id="stufe-7"></span>

:::zweck
The Dirac impulse is the limiting object from Stage [4](#stufe-4). It is not an ordinary function. All of its properties follow from the fact that it acts only through its area.
:::

**What $\delta$ is and what it is not.** As $T_0\to0$, the rectangles $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ become ever narrower and taller, while their area stays 1 (Fig. [8](#abb-8)). There is no limit in the sense of ordinary functions: a function that is zero everywhere except at one point has zero area, whatever its value at that point. $\delta(t)$ is therefore a __distribution__: an object that is defined only by its effect under an integral, namely by [(4.1)](#gl-4-1). It is drawn as an arrow whose height gives the weight (the area).

:::abbildung et3/k1dirac
Left: rectangles of area 1, ever narrower and taller. Right: the symbol for the limiting object. The height of the arrow is the weight, not the function value.
:::

:::satz Theorem 7.1 (Properties of the Dirac impulse)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Weight:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Sifting:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Area:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Scaling:} && \delta(bt)=\frac{1}{|b|}\,\delta(t),\qquad \delta(-t)=\delta(t),\\ &\text{Shifting:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**How to read it:** the product $s(t)\,\delta(t-T)$ can have an effect only at the point $T$, so only $s(T)$ counts. A compressed impulse $\delta(bt)$ is just as “infinitely high”, but its area is only $1/|b|$. A system with $h(t)=\delta(t-t_0)$ delays every signal by $t_0$; it is called an __ideal delay element__. And because the step is the running integral of the impulse, functions with jumps may be differentiated: a jump of height $A$ becomes $A\,\delta$. This is called __generalized differentiation__. Caution: many operations, such as squaring ($\delta^2$), are not defined for Dirac impulses.

:::herleitung Scaling and the sifting product
⁠**Scaling.** For $b>0$, with $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

For $b<0$ the substitution reverses the direction of integration, and the result is $-\frac1b=\frac{1}{|b|}$. So $\delta(bt)$ acts like $\frac1{|b|}\delta(t)$. With $b=-1$ the symmetry $\delta(-t)=\delta(t)$ follows.

⁠**Sifting product.** If $s(t)\delta(t)$ is convolved with an arbitrary $g(t)$, the sifting property gives

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Both act identically on every $g$, so $s(t)\delta(t)=s(0)\delta(t)$. Shifting then gives $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, and $\varepsilon(t-\tau)=1$ exactly for $\tau\le t$.
:::

:::frage But $\delta(0)$ is infinite. So $\delta(2t)$ is the same as $\delta(t)$, isn't it?
No. “Infinitely high” does not describe $\delta$, because all function values except at $0$ are the same, and the value at $0$ is not a number. What characterizes $\delta$ is its area. If you compress the rectangle of area 1 to half its width and keep its height, the area halves. That is why $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Exercise 8 ★ Calculating with $\delta$
<span class="anker" id="aufg-8"></span>

Compute: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0.135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::

## Stage 8: Integrating and differentiating

<span class="anker" id="stufe-8"></span>

:::zweck
The integrator and the differentiator are LTI systems. They link the step response to the impulse response, and they let you obtain the impulse response of the RC circuit from its step response.
:::

**The integrator.** If $\delta$ in [(7.6)](#gl-7-6) is replaced by an arbitrary $s$, the same calculation gives

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

A system with the impulse response $\varepsilon(t)$ forms the running integral of its input; it is called an __integrator__. Read with the roles swapped ($\varepsilon*s$), [(8.1)](#gl-8-1) says: **the step response of a system is the running integral of its impulse response.** Check with the RC circuit: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, exactly [(2.5)](#gl-2-5). Two independent routes, the differential equation and convolution, give the same result.

**The differentiator.** An integrator followed by a __differentiator__ leaves every signal unchanged; the cascade is ideally distortion-free. The impulse response of the differentiator is therefore the distribution $\delta'(t)$ (the __doublet__), defined by

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

Approximately, $\delta'$ is a narrow double rectangular pulse: first a rectangle of height $+1/T_0^2$, then one of height $-1/T_0^2$, each $T_0$ wide. It is drawn as a pair of arrows, one pointing up and one pointing down.

**Impulse response = derivative of the step response.** Because $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ and the system is linear and time-invariant, $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{step response})$. For the RC circuit, with the product rule:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

The second term vanishes by [(7.2)](#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. The mechanism behind this: the step response of the RC circuit does not jump, because the capacitor needs time to charge. Only a step response that jumps produces a Dirac impulse in $h$ (Exercise [9](#aufg-9)).

:::aufgabe Exercise 9 ★★ High-pass: a Dirac impulse in the impulse response
<span class="anker" id="aufg-9"></span>

If $R$ and $C$ are swapped, the output voltage is taken across $R$ (CR high-pass, $RC=1$ s). Its step response is $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Explain the step response through the mechanism: what is across $R$ at the first instant, and what after a long time?

</li>

<li>

Find the impulse response by differentiation. What does the Dirac component mean physically?

</li>

<li>

Check: integrating the impulse response must give back the step response.

</li>

</ol>

:::loesung
(a) At the first instant the capacitor is empty, so there is no voltage across it. The full 1 V is across $R$. The current then charges the capacitor; its voltage rises as $1-\mathrm{e}^{-t}$, and $\mathrm{e}^{-t}$ remains across $R$. After a long time the capacitor is full, no current flows, and no voltage is left across $R$.

(b) Product rule:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Here the step response jumps from 0 to 1 at $t=0$, so the Dirac component remains. Physically: an infinitely short impulse passes straight through, because the capacitor cannot build up a voltage in zero time. The charge that the impulse has put on the capacitor then flows off again through $R$, in the opposite direction: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::

## Stage 9: Causal and stable

<span class="anker" id="stufe-9"></span>

:::zweck
Two properties that every real system should have can be read directly from $h(t)$.
:::

:::definition Definition 9.1 (Causal, stable)
<span class="anker" id="satz-9-1"></span>

A system is called __causal__ if the output does not begin before the input. For an LTI system this means

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{for }t<0. \tag{9.1}$$

A system is called __stable__ (more precisely, BIBO stable, *bounded input, bounded output*) if it responds to every bounded input $|s(t)|\le A<\infty$ with a bounded output.
:::

Causal: an impulse at time 0 cannot have any effect before that time. In the convolution, only impulses from the past then contribute, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.

:::satz Theorem 9.2 (Stability condition)
<span class="anker" id="satz-9-2"></span>

An LTI system is stable if and only if its impulse response is absolutely integrable:

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung Stability condition
⁠**Sufficient.** With the triangle inequality for integrals and $|s|\le A$:

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

If the integral is finite, $g$ is bounded.

⁠**Necessary.** If $\int|h|=\infty$, choose the least favorable bounded input: $s(t_1-\tau)=\operatorname{sign}h(\tau)$, that is, always $\pm1$ with the sign of $h$. Then $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, although $|s|\le1$.
:::

Examples: the RC circuit has $\int|h|=1$ and is stable. The ideal delay element ($\int|\delta(t-t_0)|\mathrm{d} t=1$) is stable. The integrator has $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ and is unstable: it responds to the bounded step with the unbounded ramp $t\,\varepsilon(t)$.

:::aufgabe Exercise 10 ★★ Causal? Stable?
<span class="anker" id="aufg-10"></span>

Examine (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$, (b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$, (c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$, (d) $h(t)=\mathrm{e}^{-|t|}$, (e) $h(t)=\delta(t+1)$. For each unstable system, give a bounded input that produces an unbounded output.

:::loesung
(a) Causal, $\int|h|=\tfrac12$: stable.

(b) Causal, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$: unstable. The step $\varepsilon(t)$ produces $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$, which is unbounded.

(c) Causal, $\int|h|=1$: stable. The system forms the integral of the input over the last second (sliding window).

(d) Not causal, because $h(t)\neq0$ for $t<0$. $\int\mathrm{e}^{-|t|}\mathrm{d} t=2$: stable.

(e) $\delta(t+1)$ acts at $t=-1<0$: $g(t)=s(t+1)$; the system “sees” the input one second in advance. Not causal, but stable ($\int|h|=1$).
:::
:::

## Stage 10: Convolution without any system

<span class="anker" id="stufe-10"></span>

:::frage Convolution makes sense to me when a signal really passes through a system. What does it mean when no system is involved?
Convolution is a mathematical operation with a general meaning of its own: *for every way of splitting a result into two parts, multiply the weights of the two parts, and sum over all splittings.* The system is one interpretation of this (part 1: when did the impulse arrive; part 2: how old is it), not the only one.

⁠**An example with neither a system nor time: two dice.** What is the probability that the sum of the dice is $k$? Every splitting $k=i+(k-i)$ contributes, with the probability $P_1(i)\,P_2(k-i)$:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

This is a convolution, with exactly the same structure as $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ corresponds to the number on the first die, $t$ to the sum, and $t-\tau$ to the number on the second die. Two uniformly distributed dice (“rectangles”) give a triangular distribution, just like $\operatorname{rect}*\operatorname{rect}=\Lambda$ in Exercise [5](#aufg-5). The sum 7 is the most frequent because it has the most splittings (Fig. [9](#abb-9)).

More examples: a moving average over measured values is a convolution with a rectangle. A blurred photo is the sharp image convolved with the spot of light that the optics make from a single point. And multiplying two polynomials convolves their coefficients (Exercise [11](#aufg-11)).
:::

:::abbildung et3/k1wuerfel
Probabilities of the sum of the dice. Each distribution is the convolution of the previous one with that of a single die. The rectangle becomes a triangle ($P(7)=6/36$), and the triangle becomes a bell-shaped curve ($P(10)=P(11)=27/216$).
:::

:::zusatz Why convolutions occur so often
If you convolve more and more identical distributions, the result approaches a Gaussian curve, almost regardless of the initial shape (central limit theorem). That is why noise, the sum of many small independent influences, is so often Gaussian. And the fact that a convolution of coefficients corresponds to a product of polynomials is the core of all transforms that turn convolutions into products: [Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) does the same with the building blocks $\mathrm{e}^{pt}$ instead of the powers $x^n$.
:::

:::aufgabe Exercise 11 ★ Convolution with dice and polynomials
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Compute $P(7)$ and $P(4)$ for two dice from the convolution sum. Which splittings contribute in each case?

</li>

<li>

Compute $P(10)$ for three dice by convolving the distribution for two dice with the distribution for one die.

</li>

<li>

Multiply out $(1+2x)(3+x)$. Show that the coefficient sequence of the result is the convolution of the sequences $(1,2)$ and $(3,1)$.

</li>

</ol>

:::loesung
(a) $P(7)$: splittings $1+6,\,2+5,\dots,6+1$, six in all, each with $\frac16\cdot\frac16$: $P(7)=\frac{6}{36}=\frac16$. $P(4)$: $1+3,\,2+2,\,3+1$: $\frac{3}{36}=\frac{1}{12}$.

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$.

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$. The coefficient of $x^k$ collects all pairs of powers with $i+j=k$: $c_0=1\cdot3=3$, $c_1=1\cdot1+2\cdot3=7$, $c_2=2\cdot1=2$. This is the convolution sum $c_k=\sum_ia_ib_{k-i}$, the same structure as with the dice.
:::
:::

:::kern Key points
<ul>

<li>

Shifting $t\to t-t_0$ delays, stretching $t\to t/T$ widens; $a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$: center $t_0$, duration $|T|$, height $a$.

</li>

<li>

RC low-pass: $H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$, $|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$, $\varphi=-\arctan(2\pi FRC)$; step response $1-\mathrm{e}^{-t/RC}$.

</li>

<li>

LTI: superposition principle and $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$.

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$ and $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$.

</li>

<li>

Evaluating: flip, shift, multiply, integrate.

</li>

<li>

$s*\delta=s$; commutative, associative (cascade: $h_1*h_2$), distributive (parallel: $h_1+h_2$).

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$; $\delta(bt)=\delta(t)/|b|$; $\delta(t-t_0)*s=s(t-t_0)$; $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$.

</li>

<li>

Step response $=\int h$, impulse response $=\frac{\mathrm{d}}{\mathrm{d} t}$ step response.

</li>

<li>

Causal: $h(t)=0$ for $t<0$. Stable: $\int|h|\mathrm{d} t<\infty$.

</li>

</ul>
:::

**Looking ahead to [Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html).** This article decomposes signals into impulses $\delta(t-\tau)$. The system responds to each of them with a shifted copy of $h$, and all the copies have to be added up: that is convolution. [Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) decomposes signals into building blocks $\mathrm{e}^{pt}$. The system responds to each of these with just a number $H(p)$, and convolution turns into multiplication.
