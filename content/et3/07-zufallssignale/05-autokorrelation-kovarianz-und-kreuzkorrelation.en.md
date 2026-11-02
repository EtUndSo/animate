---
title: Stage 4: Autocorrelation, covariance and cross-correlation
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270500
summary: How fast does a random signal change?
tags: autocovariance function
lang: en
---

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
