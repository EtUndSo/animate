---
title: Stage 3: Mean value, power, variance
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270400
summary: The most important first-order averages and their intuitive meaning.
tags: DC component, power, variance, AC power, standard deviation
lang: en
---

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
