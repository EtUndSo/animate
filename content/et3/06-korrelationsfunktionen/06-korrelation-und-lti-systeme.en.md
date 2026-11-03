---
title: Stage 5: Correlation and LTI systems
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260600
summary: What does an LTI system do to the ACF and the energy spectral density?
tags: 
lang: en
---

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

⁠**How to read it:** The system multiplies the energy at each frequency by $|H|^2$. The phase of the system plays no role for the energy. Equation [(5.2)](#gl-5-2) is a measurement method: if the input has an ACF that is almost a weighted Dirac impulse $c\,\delta(\tau)$ (for example a very short pulse), then the cross-correlation between input and output is almost $c\,h(\tau)$, that is, the impulse response up to the factor $c$. Unlike $|H|^2$, it also contains the phase.

:::ltspice Energy before and after the RC circuit
⁠**Draw:** a behavioural source `bv` at net `s` with `V=exp(-time)*(time>0)`, the exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$. The factor `(time>0)` makes LTspice compute the initial state at $t=0$ with 0 V, so the capacitor starts empty. After it the RC circuit (`res` with `1Meg`, `cap` with `1u`) with its output at net `g`.

⁠**Directives:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` and `.meas tran Eg INTEG V(g)*V(g)`, the energies as in [(1.1)](energie-und-leistung.html#gl-1-1).

⁠**What you see:** `Es` $=0.500$, as $E_s=\varphi^E_{ss}(0)=\frac12$ in Stage [4](energiedichtespektrum.html#stufe-4). Compare `Eg` with your result from Exercise [5](#aufg-5). The output energy is smaller because the RC circuit multiplies the energy at each frequency by $|H|^2\le1$.
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
