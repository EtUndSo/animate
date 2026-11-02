---
title: Key points
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Orthogonal Expansion and Transmission Lines
order: 3280600
summary: Two supplementary topics: signals as vectors, waves on electrical transmission lines
tags: 
lang: en
---

:::merke The answer in three sentences
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
