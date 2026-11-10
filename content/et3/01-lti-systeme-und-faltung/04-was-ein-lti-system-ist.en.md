---
title: Stage 3: What an LTI system is
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / LTI Systems and Convolution
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Chapter 1: LTI Systems and Convolution
order: 3210400
summary: The RC circuit has two properties on which everything else rests: it is linear and time-invariant.
tags: system, transformation, linear, time-invariant, LTI system
lang: en
---

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

In the RC circuit, linearity comes from the fact that the differential equation [(2.1)](ein-erstes-system-das-rc-glied.html#gl-2-1) contains neither products nor squares of $u_1$ and $u_2$. Time invariance comes from the fact that $R$ and $C$ do not change with time. Every network of $R$, $L$ and $C$ is described by linear differential equations with constant coefficients. This does not hold for every LTI system, though: an ideal delay element, for example, which merely delays its input by a fixed time, has no such equation.

**What the two properties allow.** If you know the response $g_0$ to a rectangular pulse $s_0$, you know, without further calculation, the response to any sum of shifted and scaled rectangular pulses. Figure [4](#abb-4) shows this for $s(t)=s_0(t)+0.5\,s_0(t-2)$: the output is $g_0(t)+0.5\,g_0(t-2)$.

:::abbildung et3/k1doppel 4
Left: rectangle $s_0$ (height 1 V, duration 1 s) and the response $g_0$ of the RC circuit. Right: a pair of pulses. The response (red) is the sum of $g_0(t)$ and the shifted, halved copy $0.5\,g_0(t-2)$ (dashed).
:::

:::frage Is $g(t)=2s(t)+1$ linear? Its characteristic is a straight line, after all.
No. For a linear system, zero input must give zero output: setting all $a_i=0$ in [(3.1)](#gl-3-1) gives $\operatorname{Tr}\{0\}=0$. Here $\operatorname{Tr}\{0\}=1$. The superposition principle fails as well: two inputs applied separately give $2s_1+2s_2+2$ in total, but applied together they give $2s_1+2s_2+1$. A straight line that does not pass through the origin is called *affine*, not linear.
:::

:::ltspice Checking superposition: two rectangles
⁠**Draw:** the RC circuit from Stage [2](ein-erstes-system-das-rc-glied.html#stufe-2), but with two `voltage` sources in series: `V1` with its negative terminal at ground and its positive terminal at net `a`, value `PULSE(0 {a1} 0 1u 1u 1)`, on top of it `V2` from `a` to `in`, value `PULSE(0 {a2} 2 1u 1u 1)`. In series the voltages add, so the RC circuit sees $a_1s_0(t)+a_2s_0(t-2)$.

⁠**Directives:** `.param a1=1 a2=0.5`, `.step param a1 list 0 1`, `.step param a2 list 0 0.5`, `.tran 0 6 0 1m`. LTspice runs all four combinations and plots them on top of each other.

⁠**What you see:** the curves $0$, $g_0(t)$, $0.5\,g_0(t-2)$ and their sum, as in Fig. [4](#abb-4). At $t=2.5$ s: $0.141+0.197=0.338$. The sum of the inputs gives the sum of the responses (linearity), and the source shifted by 2 s gives the curve shifted by 2 s (time invariance).
:::

:::aufgabe Exercise 3 ★ LTI or not?
<span class="anker" id="aufg-3"></span>

Check each system for linearity and time invariance: (a) $g(t)=3\,s(t-2)$, (b) $g(t)=s(t)^2$, (c) $g(t)=s(t)+1$, (d) $g(t)=t\,s(t)$, (e) $g(t)=s(2t)$, (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$.

:::loesung
(a) Linear and time-invariant (gain 3, delay 2): LTI. (b) Not linear: $\operatorname{Tr}\{2s\}=4s^2\neq2s^2$. Time-invariant. (c) Not linear (affine, $\operatorname{Tr}\{0\}=1$). Time-invariant. (d) Linear. Not time-invariant: $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, but $g(t-t_0)=(t-t_0)\,s(t-t_0)$. The factor $t$ is a component that changes with time. (e) Linear. Not time-invariant: $\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$, but $g(t-t_0)=s(2t-2t_0)$. Compressing time also compresses every shift. (f) LTI. Linear, because the integral is linear. Time-invariant: $\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$. Its impulse response is $\varepsilon(t)$ (Stage [8](integrieren-und-differenzieren.html#stufe-8)).
:::
:::
