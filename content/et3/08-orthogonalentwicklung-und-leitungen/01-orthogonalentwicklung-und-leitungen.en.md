---
title: Orthogonal Expansion and Transmission Lines
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Orthogonal Expansion and Transmission Lines
order: 3280100
summary: Two supplementary topics: signals as vectors, waves on electrical transmission lines
tags: orthogonal, orthonormal, generalized Parseval theorem, per-unit-length parameters, wave equation, propagation constant, characteristic impedance, attenuation constant
lang: en
---

## What this is about

This article adds two topics to Parts 1 to 7. The first generalizes the Fourier series: a signal is decomposed in terms of arbitrary orthogonal functions, just as a vector is decomposed into its components. The second shows what happens on a long line: voltage and current travel as waves, which can be reflected at the end. The optimal quantizer, which would be a candidate for a third supplementary topic, is already covered in [Part 7](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html) (Stage 5).

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

For orthonormal basis functions, the best coefficient of a function is its correlation with the basis function, and the energy is the sum of the squared coefficients.

</li>

<li>

On a line, every voltage is a superposition of a forward and a backward wave. The line is described by the propagation constant $\gamma$ and the characteristic impedance $Z$.

</li>

<li>

If the line is terminated with its characteristic impedance, the backward wave vanishes. On a lossless line all frequencies travel equally fast, and signals arrive undistorted.

</li>

</ol>
:::

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference models for this article
<ul>

<li>

⁠**Orthogonal expansion** of $f(t)=t^2$ on $[0,1]$ in terms of the orthonormal polynomials $s_0=1$, $s_1=\sqrt3(2t-1)$, $s_2=\sqrt5(6t^2-6t+1)$.

</li>

<li>

⁠**Coaxial cable** with $Z=50\,\Omega$ and $C'=100$ pF/m, lossless.

</li>

</ul>
:::

## Stage 1: Signals as vectors, the orthogonal expansion

<span class="anker" id="stufe-1"></span>

:::zweck
The Fourier series decomposes a signal into oscillations. The same works with any system of orthogonal functions. This stage shows how to find the coefficients and why they give the best approximation.
:::

**The idea.** A vector in space has the components $b_i=\vec f\cdot\vec e_i$ with respect to perpendicular unit vectors $\vec e_i$. For signals on an interval $[0,T]$, the integral $\int_0^Tf(t)g(t)\mathrm{d} t$ plays the role of the scalar product. Two signals are called __orthogonal__ if it is zero ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). A system of $M$ functions $s_i(t)$ is called __orthonormal__ if

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

An energy signal $f(t)$ is approximated by $\sum_{i=0}^{M-1}b_is_i(t)$, and a residual $r(t)=f(t)-\sum b_is_i(t)$ remains.

:::satz Theorem 1.1 (Orthogonal expansion)
<span class="anker" id="satz-1-1"></span>

The energy of the residual, $E_r=\int_0^Tr^2\mathrm{d} t$, is smallest for

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

Then $E_r=E_f-\sum_ib_i^2$. If $E_r\to0$ as $M$ grows (complete system), the __generalized Parseval theorem__ $E_f=\sum_ib_i^2$ holds.
:::

:::herleitung Coefficients and residual energy
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$. Differentiate with respect to $b_j$ and set to zero:

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

Orthonormality leaves only $i=j$ in the sum. If these $b_i$ are substituted and the square is multiplied out, the mixed terms drop out, again because of orthonormality: $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$.
:::

⁠**How to read it:** Each coefficient is determined on its own, independently of the others. If you add a basis function, the previous coefficients do not change. This is the advantage of orthogonal systems, just as with the Fourier series ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ is the cross-correlation $\varphi^E_{fs_i}(0)$. That is why the coefficients can be measured with a bank of correlation filters $h_i(t)=s_i(T-t)$ whose outputs are sampled at $t=T$ ([Part 7](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

**Example.** $f(t)=t^2$ on $[0,1]$, $E_f=\frac15$. With $s_0=1$ and $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0.289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

The approximation is $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, the best straight line in the sense of energy. The residual energy is $\frac15-\frac7{36}=\frac{1}{180}=0.0056$, that is, 2.8 % of $E_f$. With $s_2=\sqrt5(6t^2-6t+1)$, the coefficient $b_2=\frac{\sqrt5}{30}=0.075$ is added, and the residual becomes zero, because $t^2$ is itself a polynomial of degree two.

:::aufgabe Exercise 1 ★ Checking orthonormality
<span class="anker" id="aufg-1"></span>

Show that $s_0=1$ and $s_1=\sqrt3(2t-1)$ are orthonormal on $[0,1]$. Why does $s_1$ need the factor $\sqrt3$?

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$: orthogonal. $\int_0^11^2\mathrm{d} t=1$. $\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$. Without the factor, the energy of $2t-1$ would be only $\frac13$. The factor $\sqrt3$ normalizes it to 1; otherwise $b_1=\int fs_1\mathrm{d} t$ would not be the correct coefficient.
:::
:::

:::aufgabe Exercise 2 ★★ Best approximation
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Recompute $b_1$ for $f(t)=t^2$ and confirm the approximation $t-\frac16$.

</li>

<li>

Check $E_r=\frac{1}{180}$ by computing $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$ directly.

</li>

<li>

Find the coefficients of $f(t)=\sqrt2\cos(2\pi t)$ with respect to $s_0$ and $s_1$. What does the result mean?

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$, so $b_1=\frac{\sqrt3}{6}$. Approximation: $\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$.

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$.

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$ and $b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$ (the cosine is symmetric about $t=\frac12$, and $2t-1$ is antisymmetric). Both coefficients are zero: the function is orthogonal to both basis functions, the approximation is zero, and the entire signal content remains in the residual. A basis is suitable only for signals that resemble its functions.
:::
:::

## Stage 2: The transmission-line equations

<span class="anker" id="stufe-2"></span>

:::zweck
So far, lines were ideal connections. If a line is long compared with the wavelength, a signal needs a noticeable time to travel through it. This stage sets up the equations that describe this.
:::

**The idea.** The line is divided into short pieces of length $\mathrm{d} s$. Each piece has a series resistance and a series inductance (the outgoing and return conductors), plus a shunt capacitance and a shunt conductance (between the conductors). For a uniform line these quantities are proportional to the length: $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$, $G'\mathrm{d} s$, with the __per-unit-length parameters__ (line constants) $R'$, $L'$, $C'$, $G'$ (values per meter, Fig. [1](#abb-1)).

:::abbildung et3/k8element
Equivalent circuit of a short line segment of length $\mathrm{d} s$ with the per-unit-length parameters $R'$, $L'$, $G'$, $C'$.
:::

:::satz Theorem 2.1 (Transmission-line equations, telegrapher's equations)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung Transmission-line equations
Kirchhoff's voltage law around the piece: $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, so $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$. Kirchhoff's current law: part of the current $i$ flows away through $G'\mathrm{d} s$ and $C'\mathrm{d} s$, $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$. Divide by $\mathrm{d} s$. (Strictly speaking, the current law contains the voltage at the end of the piece; the difference is of second order in $\mathrm{d} s$.)
:::

⁠**How to read it:** The voltage drops along the line because current flows through the series elements. The current decreases because it leaks away through the shunt elements between the conductors. The two equations couple $u$ and $i$ in space and time.

## Stage 3: Waves under sinusoidal excitation

<span class="anker" id="stufe-3"></span>

:::zweck
With phasors, the partial differential equations become an ordinary differential equation in position. Its solution consists of two waves traveling in opposite directions.
:::

With $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$, and likewise for $i$, $\frac{\partial}{\partial t}$ becomes $\mathrm{j}2\pi f$:

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

Differentiating the first equation and substituting the second gives the __wave equation__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$.

:::satz Theorem 3.1 (Forward and backward wave)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

with the __propagation constant__ and the __characteristic impedance__

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**How to read it:** With $\gamma=\alpha+\mathrm{j}\beta$, the first term becomes $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$ in the time domain: a wave that travels in the direction of increasing $s$ and decays as it goes, with the __attenuation constant__ $\alpha$. A zero crossing moves at $v=2\pi f/\beta$, and the wavelength is $\lambda=2\pi/\beta$. The second term travels in the opposite direction. $Z$ is the ratio of voltage to current in a single wave. The constants $\underline U_1$, $\underline U_2$ are fixed by the boundary conditions, for example voltage and current at the beginning: $\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$.

**Reflection at the end.** If the line is terminated at its end ($s=l$) with a resistance $R_\mathrm E=\underline U_e/\underline I_e$, the voltage can be written as

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

The first term is the forward (incident) wave, the second the wave traveling back from the end (reflected wave). For $R_\mathrm E=Z$ the backward wave vanishes: a termination with the characteristic impedance absorbs the arriving wave completely, as if the line continued indefinitely. The ratio of the two waves at the end is the __reflection coefficient__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$ (Aside: short circuit $r=-1$, open circuit $r=+1$).

:::frage Why does a wrong termination not matter for short lines?
Because the reflected wave is then back almost immediately. If the propagation delay along the line is small compared with the duration of the signal changes (line short compared with the wavelength), the forward and backward waves superimpose practically simultaneously, and you notice only the terminating resistance. Only when the delay becomes comparable, for example with fast digital signals or at high frequencies, do reflections appear as echoes and distort the signal.
:::

## Stage 4: The lossless line

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

⁠**How to read it:** An arbitrary signal shape travels unchanged along the line at the velocity $v$. This is because all frequency components are equally fast and are attenuated equally little: the line is a distortion-free system in the sense of [Part 5](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), with the delay $l/v$. The wave equation for $u$ follows from [(2.1)](#gl-2-1) by differentiating the first equation with respect to $s$ and the second with respect to $t$ and eliminating $i$.

**Example: coaxial cable.** $Z=50\,\Omega$ and $C'=100$ pF/m give $L'=Z^2C'=250$ nH/m and $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s, two thirds of the speed of light (because of the dielectric in the cable). A signal needs 50 ns for 10 m of cable. If the cable is terminated with 75 $\Omega$ instead of 50 $\Omega$, then $r=\frac{75-50}{75+50}=0.2$: 20 % of the voltage amplitude travels back as an echo.

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

:::kern Key points
<ul>

<li>

Orthonormal: $\int s_is_j\mathrm{d} t=\delta_{ij}$; best coefficients $b_i=\int fs_i\mathrm{d} t$; $E_r=E_f-\sum b_i^2$; complete: $E_f=\sum b_i^2$.

</li>

<li>

Transmission-line equations: $\partial_su=-(R'+L'\partial_t)i$, $\partial_si=-(G'+C'\partial_t)u$.

</li>

<li>

Phasors (with $\omega=2\pi f$): $\underline U=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$; $\gamma=\sqrt{(R'+\mathrm{j}\omega L')(G'+\mathrm{j}\omega C')}=\alpha+\mathrm{j}\beta$; $Z=\sqrt{\frac{R'+\mathrm{j}\omega L'}{G'+\mathrm{j}\omega C'}}$.

</li>

<li>

Termination with $Z$: no reflection; $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$.

</li>

<li>

Lossless: $Z=\sqrt{L'/C'}$, $v=1/\sqrt{L'C'}$, $u=u_\mathrm{fw}(s-vt)+u_\mathrm{bw}(s+vt)$.

</li>

</ul>
:::
