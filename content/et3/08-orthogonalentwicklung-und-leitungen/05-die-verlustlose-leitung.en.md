---
title: Stage 4: The lossless line
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Orthogonal Expansion and Transmission Lines
order: 3280500
summary: Without losses ( R'=G'=0 ), the characteristic impedance and the velocity become independent of frequency.
tags: 
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Without losses ($R'=G'=0$), the characteristic impedance and the velocity become independent of frequency. The wave solution then holds for arbitrary signals, not only for sinusoids.
:::

With $R'=G'=0$, $\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$: no attenuation ($\alpha=0$), and $\beta$ is proportional to $f$. From this:

<span class="anker" id="gl-4-1"></span>
$$Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}},\qquad\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}. \tag{4.1}$$

:::satz Theorem 4.1 (d'Alembert solution)
<span class="anker" id="satz-4-1"></span>

Every solution of the wave equation [(4.1)](#gl-4-1) has the form

<span class="anker" id="gl-4-2"></span>
$$u(s,t)=u_\mathrm{fw}(s-vt)+u_\mathrm{bw}(s+vt) \tag{4.2}$$

with arbitrary (twice differentiable) functions $u_\mathrm{fw}$ (forward) and $u_\mathrm{bw}$ (backward).
:::

⁠**How to read it:** An arbitrary signal shape travels unchanged along the line at the velocity $v$. This is because all frequency components are equally fast and are attenuated equally little: the line is a distortion-free system in the sense of [Part 5](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), with the delay $l/v$. The wave equation for $u$ follows from [(2.1)](die-leitungsgleichungen.html#gl-2-1) by differentiating the first equation with respect to $s$ and the second with respect to $t$ and eliminating $i$.

::::beispiel coaxial cable
$Z=50\,\Omega$ and $C'=100$ pF/m give $L'=Z^2C'=250$ nH/m and $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s, two thirds of the speed of light (because of the dielectric in the cable). A signal needs 50 ns for 10 m of cable. If the cable is terminated with 75 $\Omega$ instead of 50 $\Omega$, then $r=\frac{75-50}{75+50}=0.2$: 20 % of the voltage amplitude travels back as an echo.
::::

:::ltspice Reflections on a transmission line
⁠**Draw:** a `voltage` source with `PULSE(0 2 0 1n 1n 10n 1)` and an internal resistance `res` with `50` to net `in`. From `in` a lossless line `tline` with `Td=50n Z0=50` (the 10-m coaxial cable from the example) to net `end`, and there `res` with `{RE}` to ground. Because the internal resistance equals $Z$, a wave of 1 V sets off, and the echo is fully absorbed at the source.

⁠**Directives:** `.param RE=75`, `.step param RE list 1m 50 75 1G` (almost short circuit, matched, 75 $\Omega$, almost open circuit), `.tran 0 200n 0 0.1n`.

⁠**What you see:** At `in`, first the pulse of 1 V. After $2\cdot50\,\mathrm{ns}=100$ ns the echo returns with the height $r\cdot1$ V: $-1$, $0$, $0.2$ and $+1$, exactly $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$. At `end`, after 50 ns, there is the sum of forward and backward wave, $(1+r)\cdot1$ V. Set `Td` and `Z0` to your values from Exercise [4](#aufg-4)(a), set `RE` to 100 and compare the echo height with your result from Exercise [4](#aufg-4)(b).
:::

:::aufgabe Exercise 3 ★★ Checking d'Alembert
<span class="anker" id="aufg-3"></span>

Show by substitution that $u(s,t)=u_\mathrm{fw}(s-vt)$ solves the wave equation [(4.1)](#gl-4-1) with $v=1/\sqrt{L'C'}$. How is the associated current related to the voltage? Hint: first transmission-line equation with $R'=0$.

:::loesung
With $x=s-vt$: $\frac{\partial^2u}{\partial s^2}=u_\mathrm{fw}''(x)$ and $\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{fw}''(x)$. The wave equation requires $u''=L'C'v^2u''$, so $v^2=\frac{1}{L'C'}$. Current: with $R'=0$, $\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$, so $u_\mathrm{fw}'(x)=-L'\frac{\partial i}{\partial t}$. The ansatz $i=u_\mathrm{fw}(x)/Z$ gives $\frac{\partial i}{\partial t}=-\frac vZu'_\mathrm{fw}$, and this is consistent because $L'v/Z=L'\cdot\frac{1}{\sqrt{L'C'}}\cdot\sqrt{\frac{C'}{L'}}=1$. In the forward wave, voltage and current are everywhere in the ratio $Z$.
:::
:::

:::aufgabe Exercise 4 ★★ Cable and termination
<span class="anker" id="aufg-4"></span>

A lossless cable has $L'=300$ nH/m and $C'=120$ pF/m.

<ol class="al">

<li>

Compute $Z$, $v$ and the propagation delay for 5 m.

</li>

<li>

With what resistance must it be terminated so that nothing is reflected? What reflection coefficient results with 100 $\Omega$?

</li>

<li>

Up to what frequency can the 5 m still be treated as “short” if the line is to be at most one tenth of the wavelength long?

</li>

</ol>

:::loesung
(a) $Z=\sqrt{300/120}\cdot\sqrt{\frac{\text{nH}}{\text{pF}}}=\sqrt{2.5\cdot10^3}\,\Omega=50\,\Omega$. $v=\frac{1}{\sqrt{300\cdot10^{-9}\cdot120\cdot10^{-12}}}\,\mathrm{m/s}=\frac{1}{\sqrt{3.6\cdot10^{-17}}}\,\mathrm{m/s}=1.67\cdot10^8$ m/s. Propagation delay for 5 m: 30 ns.

(b) With $Z=50\,\Omega$. With 100 $\Omega$: $r=\frac{100-50}{150}=\frac13$.

(c) $\lambda=v/f\ge50$ m, so $f\le\frac{1.67\cdot10^8}{50}\,\mathrm{Hz}=3.3$ MHz.
:::
:::
