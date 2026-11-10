---
title: Stage 3: The space-charge region
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Semiconductors and Diodes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Chapter 9: Semiconductors and Diodes
order: 1190500
summary: An n-piece and a p-piece are, on their own, just resistors.
tags: diffusion, space charge, drift, built-in voltage
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
An n-piece and a p-piece are, on their own, just resistors. This stage shows what forms at their boundary and why it is a barrier.
:::

**The idea.** In a crystal, a p-region borders an n-region. Four steps take place (Fig. [4](#abb-4)):

<ol>

<li>

⁠**Diffusion.** Charge carriers move randomly. More of them wander out of the region of high density than into it. This equalization by random motion is called __diffusion__. Electrons wander from the n-region into the p-region, holes the other way.

</li>

<li>

⁠**Recombination.** In the foreign region the wanderers meet the majority there and disappear. Near the boundary, hardly any free carriers remain afterward.

</li>

<li>

⁠**Fixed ions remain.** There the ions are no longer balanced: $\mathrm P^+$ on the n-side, $\mathrm B^-$ on the p-side. This stationary charge is called __space charge__, the layer the space-charge region.

</li>

<li>

⁠**The field stops the equalization.** The ions create a field from the n-side to the p-side. It drives electrons back into the n-region and holes back into the p-region (__drift__, [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). The region grows until the drift current exactly cancels the diffusion current.

</li>

</ol>

:::abbildung et1/k9rlz 4
pn junction without external voltage. Top: boxes are fixed ions, filled circles electrons, open circles holes. In the region the mobile carriers are missing, and the field $E$ points to the p-side. Bottom: the potential rises only in the region, by $U_\mathrm{D0}=0.71$ V in total. This potential step brakes electrons on their way to the p-side.
:::

:::satz Theorem 3.1 (Built-in voltage and width of the region)
<span class="anker" id="satz-3-1"></span>

For an abrupt junction, with the thermal voltage $U_T=k_\mathrm BT/e$,

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2},\qquad w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}},\qquad E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}. \tag{3.1}$$
:::

⁠**How to read it:** $U_\mathrm{D0}$ is the __built-in voltage__, the potential step between the two regions, around 0.7 to 0.9 V for silicon. On the way to the p-side, electrons see an energy barrier $W_\mathrm B=e\,U_\mathrm{D0}$. $w$ is the width of the region, $\varepsilon=\varepsilon_0\varepsilon_\mathrm r=1.04\cdot10^{-10}$ A s/(V m) the permittivity ([Chapter 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). The region reaches deeper into the more lightly doped side: $w_\mathrm n/w_\mathrm p=N_\mathrm A/N_\mathrm D$. **Validity:** equilibrium; insert the densities in [(3.1)](#gl-3-1) in 1/m$^3$.

:::herleitung Potential step and width
⁠**Potential step.** An electron on the p-side has climbed the barrier. By [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1), the densities satisfy $n_\mathrm p/n_\mathrm n=\mathrm{e}^{-U_\mathrm{D0}/U_T}$. With $n_\mathrm n=N_\mathrm D$ and $n_\mathrm p=n_\mathrm i^2/N_\mathrm A$ from [(2.1)](dotierung.html#gl-2-1), the first equation follows.

⁠**Width.** Both sides carry the same amount of charge, so $N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n$. The field grows linearly from the edges to the boundary and reaches there the value of a surface charge ([Chapter 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), $E_\mathrm{max}=e\,N_\mathrm Dw_\mathrm n/\varepsilon$. The voltage is the area under the field curve, a triangle: $U_\mathrm{D0}=\tfrac12E_\mathrm{max}w$. With $w=w_\mathrm n+w_\mathrm p$ this gives [(3.1)](#gl-3-1).
:::

::::beispiel
$U_\mathrm{D0}=25.85\,\mathrm{mV}\cdot\ln10^{12}=0.714$ V, which is $27.6\,U_T$. So the barrier lets the fraction $\mathrm{e}^{-27.6}=10^{-12}$ pass, exactly the ratio $10^{4}/10^{16}$ of the densities. Further, $w=0.43$ µ m, half of it in each region, and $E_\mathrm{max}=3.3$ MV/m, as much as the breakdown field strength of air ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)).
::::

⁠**Limiting cases:** If one side is much more heavily doped, the region lies almost entirely in the other. Ten times more doping on one side raises $U_\mathrm{D0}$ by only 60 mV.

:::frage There are 0.71 V inside the diode. Why do you measure 0 V across it, and why does it not drive a current?
The potential step is real, but it is not the only one in the circuit. Where metal contacts meet the semiconductor, further contact voltages arise. Around any closed circuit their sum is zero, because in equilibrium there is no energy source. The step only establishes the equilibrium between diffusion and drift.
:::

:::aufgabe Exercise 3 ★★ A one-sided junction
<span class="anker" id="aufg-3"></span>

A pn junction has $N_\mathrm A=10^{18}\,\mathrm{cm^{-3}}$ and $N_\mathrm D=10^{15}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Calculate $U_\mathrm{D0}$, $w$ and $E_\mathrm{max}$.

</li>

<li>

How wide is the region on each side? Why does it lie almost entirely in the lightly doped region?

</li>

</ol>

:::loesung
(a) $U_\mathrm{D0}=25.85\,\mathrm{mV}\cdot\ln(10^{33}/10^{20})=0.774$ V. Because $1/N_\mathrm A$ is negligible next to $1/N_\mathrm D$, $w=\sqrt{2\varepsilon U_\mathrm{D0}/(e\,N_\mathrm D)}=1.00$ µ m and $E_\mathrm{max}=2U_\mathrm{D0}/w=1.55$ MV/m. (b) $w_\mathrm n/w_\mathrm p=1000$, so $w_\mathrm n=1.00$ µ m and $w_\mathrm p=1.0$ nm. Both sides must provide the same ion charge. In the lightly doped region the ions sit a thousand times more thinly, so it takes a thousand times more depth.
:::
:::
