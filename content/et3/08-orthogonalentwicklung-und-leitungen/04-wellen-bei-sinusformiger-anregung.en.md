---
title: Stage 3: Waves under sinusoidal excitation
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Orthogonal Expansion and Transmission Lines
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Chapter 8: Orthogonal Expansion and Transmission Lines
order: 3280400
summary: With phasors, the partial differential equations become an ordinary differential equation in position.
tags: wave equation, propagation constant, characteristic impedance, attenuation constant, reflection coefficient
lang: en
---

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
