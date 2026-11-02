---
title: Stage 6: Correlation of bandpass signals
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260700
summary: Correlation functions of bandpass signals, too, are computed with the complex envelopes (Part 5).
tags: 
lang: en
---

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
