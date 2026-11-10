---
title: Stage 3: Average power with a sinusoidal voltage
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Power, Matching and Efficiency
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Chapter 7: Power, Matching and Efficiency
order: 1170400
summary: With an AC voltage, the power changes constantly.
tags: amplitudes, period, angular frequency, RMS value
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
With an AC voltage, the power changes constantly. This stage finds the one number that determines the heating.
:::

**The idea.** At a resistor, $i$ is proportional to $u$. Both change sign at the same time, so their product is never negative. If the charge runs backward, the voltage is also reversed, and it gives off energy again. Both half-waves heat (Fig. [4](#abb-4)). The power pulsates between zero and the peak value, twice as fast as the voltage. Its mean value lies at half height.

:::abbildung et1/k7sinus 4
Left, voltage and current at the heating resistor. Right, the instantaneous power $p(t)$. It oscillates between 0 and 20 W around the mean value $P=10$ W and reaches its maximum twice as often as $u$.
:::

:::satz Theorem 3.1 (Average power at a resistor)
<span class="anker" id="satz-3-1"></span>

For $u(t)=\hat u\cos(\omega t)$ across $R$, the current $i(t)=\hat\imath\cos(\omega t)$ flows with $\hat\imath=\hat u/R$. The time average of the power is

<span class="anker" id="gl-3-1"></span>
$$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}=\frac12\,\hat\imath^2R. \tag{3.1}$$
:::

⁠**How to read it:** $\hat u$ and $\hat\imath$ are the __amplitudes__, the peak values. $T$ is the __period__, $\omega=2\pi/T$ the __angular frequency__. On the mains, $T=20$ ms and $\omega=314$ 1/s. **Validity:** The average runs over whole periods. The formula holds only if $i$ is proportional to $u$, that is, for resistors.

:::herleitung Where the factor $\frac12$ comes from
Substituting gives $p=u\,i=u^2/R=(\hat u^2/R)\cos^2(\omega t)$. With $\cos^2x=\frac12(1+\cos2x)$, this becomes

$$P=\frac{1}{T\,R}\int_0^T\hat u^2\cos^2(\omega t)\,\mathrm{d} t=\frac{1}{T\,R}\int_0^T\hat u^2\,\frac12\bigl(1+\cos(2\omega t)\bigr)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}.$$

The cosine part goes through two full oscillations in $T$; its integral is zero. With $\hat u=R\,\hat\imath$, the second form follows.
:::

::::beispiel
For $\hat u=10$ V and $R=5\,\Omega$, $\hat\imath=2$ A, the peak value of the power is 20 W and $P=10$ W. At 50 Hz, 0.2 J flow into the lattice per period.
::::

⁠**Limiting case:** For $\omega\to0$, $u$ becomes a DC voltage and $p$ stays at $\hat u^2/R$. The factor $\frac12$ disappears, because averaging over whole periods is then no longer possible.

:::zusatz RMS value
A DC voltage $U$ produces the same heat in $R$ if $U^2/R=\frac12\hat u^2/R$, that is, $U=\hat u/\sqrt2$. This value is called the __RMS value__. Here it is 7.07 V. The 230 V of the wall outlet are an RMS value; the amplitude is 325 V.
:::

:::ltspice Measuring average power
⁠**Draw:** `voltage` from `a` to ground with `SINE(0 10 50)`, `res` `R1` with 5 from `a` to ground.

⁠**Directives:** `.tran 0 40m 0 10u` and `.meas tran Pm AVG V(a)*I(R1) FROM=0 TO=40m`

⁠**What you see:** Plot `V(a)*I(R1)`: the curve stays between 0 and 20 W and oscillates at 100 Hz. The log gives `Pm` = 10 W. For Exercise [3](#aufg-3), enter the amplitude 325 and your resistance and read off 2 kW and 4 kW.
:::

:::frage With alternating current, the electrons only swing back and forth. How can that deliver energy?
Because the energy does not travel with the electrons. Even at 1 A/mm$^2$ and 50 Hz, they cover only about 0.5 µ m per half-period. The field in the resistor accelerates them in both directions, and every collision gives energy to the lattice. That requires no forward progress, only voltage and current.
:::

:::aufgabe Exercise 3 ★★ The fan heater
<span class="anker" id="aufg-3"></span>

A fan heater absorbs on average 2 kW from a sinusoidal voltage with $\hat u=325$ V and 50 Hz. (a) What are $R$, $\hat\imath$ and the peak value of the power? (b) How many times per second is $p=0$? (c) A component blocks every second half-wave. Predict the average power if $R$ stays the same.

:::loesung
(a) From [(3.1)](#gl-3-1): $R=\hat u^2/(2P)=26.4\,\Omega$, $\hat\imath=\hat u/R=12.3$ A, peak value $\hat u\,\hat\imath=2P=4$ kW. (b) Twice per period, so 100 times per second. (c) Every second half-wave is missing, and with it half of the energy: 1 kW.
:::
:::
