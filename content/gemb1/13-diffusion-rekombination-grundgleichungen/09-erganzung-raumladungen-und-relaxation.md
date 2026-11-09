---
title: Stufe 7: Ergänzung: Raumladungen und Relaxation
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4230900
summary: Licht erzeugt Paare und lässt den Kristall neutral.
tags: dielektrische Relaxationszeit, ambipolaren Diffusionskonstanten
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Licht erzeugt Paare und lässt den Kristall neutral. Bringt man nur Elektronen ein, entsteht eine Raumladung. Diese Stufe zeigt, wie schnell sie verschwindet und wie die Neutralität die Diffusion von Paaren steuert.
:::

**Die Idee.** Ein Elektronenstrahl trifft einen Punkt eines n-Halbleiters. Die zusätzliche Ladung erzeugt ein Feld, das Feld treibt in der gut leitenden Umgebung einen Driftstrom, und dieser trägt die Ladung ab. So entlädt sich ein Kondensator mit leitfähigem Dielektrikum (Abb. [7](#abb-7), links).

:::abbildung gemb1/k13relax 7
Links: Ein Stück Halbleiter wirkt wie $C$ parallel zu $R$. Rechts: Paket aus Paaren kurz nach dem Start. Die Elektronen sind vorausgelaufen, in der Mitte bleibt positive Ladung, außen negative.
:::

:::satz Satz 7.1 (Dielektrische Relaxation)
<span class="anker" id="satz-7-1"></span>

Eine Raumladung baut sich durch Drift exponentiell ab:

<span class="anker" id="gl-7-1"></span>
$$\rho(t)=\rho(0)\,\mathrm{e}^{-t/\tau_\varepsilon},\qquad\tau_\varepsilon=\frac{\varepsilon_0\varepsilon_\mathrm r}\sigma. \tag{7.1}$$
:::

⁠**So liest man das:** $\tau_\varepsilon$ ist die __dielektrische Relaxationszeit__, $\nu_\varepsilon=1/(2\pi\tau_\varepsilon)$ die Relaxationsfrequenz. Sie ist die RC-Zeit des Stücks: In $RC=(d/(\sigma A))\,(\varepsilon_0\varepsilon_\mathrm rA/d)$ kürzen sich Fläche und Dicke. **Gültigkeit:** $\Delta n\ll n$, kein Diffusionsstrom, und $\tau_\varepsilon\gg\tau_\text{scat}$, sonst folgen die Träger dem Feld nicht schnell genug.

:::herleitung Aus Poisson und Ladungsbilanz
Der Überschuss hat die Raumladung $\rho_\mathrm n=-e\,\Delta n$. Sie erzeugt ein Feld, $\operatorname{div}\boldsymbol{\mathcal E}=\rho_\mathrm n/(\varepsilon_0\varepsilon_\mathrm r)$. Die Ladung ist erhalten, $\operatorname{div}\boldsymbol j=-\partial\rho_\mathrm n/\partial t$, mit $\boldsymbol j=\sigma\boldsymbol{\mathcal E}$. Zusammen ist $\partial\rho_\mathrm n/\partial t=-\sigma\operatorname{div}\boldsymbol{\mathcal E}=-\sigma\rho_\mathrm n/(\varepsilon_0\varepsilon_\mathrm r)$.
:::

**Mehrheit und Minderheit.** Eine Wolke aus Mehrheitsträgern zerfließt mit $\tau_\varepsilon$. Trifft der Strahl dagegen ein p-Gebiet, bleiben die Elektronen als Minderheit, und aus der Umgebung fließen in der Zeit $\tau_\varepsilon$ Löcher zu, bis die Ladung neutralisiert ist. Es bleiben überschüssige Paare mit $n\,p>n_\mathrm i^2$. Erst sie baut die Rekombination langsam mit $\tau_\text{rec}$ ab.

::::beispiel
Die Probe hat $\sigma=1{,}92$ S/cm, also $\tau_\varepsilon=0{,}54$ ps und $\nu_\varepsilon=0{,}3$ THz, $1{,}9\cdot10^{6}$-mal schneller als $\tau_\text{rec}$. Das ist nur eine Größenordnung, denn $\tau_\varepsilon$ ist nur dreimal so groß wie $\tau_\text{scat}$.
::::

⁠**Grenzfall:** In einem Isolator geht $\sigma\to0$, und die Ladung bleibt liegen.

**Ambipolare Diffusion.** Eine einzelne Sorte geladener Teilchen kann nie rein diffundieren, weil sofort ein Gegenfeld entsteht. Diffusion läuft nur als Tausch gleich geladener Teilchen in Gegenrichtung oder gemeinsam mit ungleich geladenen in gleicher Richtung. Bei einem Paket aus Paaren eilen die beweglicheren Elektronen voraus, das Feld zwischen den Fronten bremst sie und zieht die Löcher mit (Abb. [7](#abb-7)). Beide laufen dann gleich schnell, mit der __ambipolaren Diffusionskonstanten__

<span class="anker" id="gl-7-2"></span>
$$D_\mathrm a=\frac{D_1D_2\,(z_1^2N_1+z_2^2N_2)}{z_1^2D_1N_1+z_2^2D_2N_2},\qquad\text{für Elektronen und Löcher}\quad D_\mathrm a=\frac{D_\mathrm nD_\mathrm p\,(n+p)}{n\,D_\mathrm n+p\,D_\mathrm p}. \tag{7.2}$$

⁠**Starke Injektion** ($n\approx p$): $D_\mathrm a=2D_\mathrm nD_\mathrm p/(D_\mathrm n+D_\mathrm p)$, in der Probe 16 cm$^2$/s. **Schwache Injektion** im n-Gebiet ($p\ll n$): $D_\mathrm a\approx D_\mathrm p$. Die vielen Mehrheitsträger bauen das Feld ab, und die Minderheit bestimmt das Tempo.

:::herleitung Woher $D_\mathrm a$ kommt
Das Paket bleibt neutral, $\partial n/\partial x=\partial p/\partial x$, und $j_\mathrm n+j_\mathrm p=0$. Das ergibt $(n\mu_\mathrm n+p\mu_\mathrm p)\mathcal E=-(D_\mathrm n-D_\mathrm p)\,\partial p/\partial x$. Einsetzen in $\mathcal J_\mathrm p=p\mu_\mathrm p\mathcal E-D_\mathrm p\,\partial p/\partial x$ mit $\mu_\mathrm p/\mu_\mathrm n=D_\mathrm p/D_\mathrm n$ gibt $\mathcal J_\mathrm p=-D_\mathrm a\,\partial p/\partial x$.
:::

:::frage Verschwindet die Ladung bei der Relaxation? Sie ist doch erhalten.
Sie verschwindet nur am Ort der Störung und erscheint an den Rändern der Probe. Die Elektronen selbst bewegen sich dabei kaum: Das Feld verschiebt alle ein winziges Stück.
:::

:::aufgabe Aufgabe 8 ★★ Zwei Zeitskalen
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Berechne $\sigma$, $\tau_\varepsilon$ und $\nu_\varepsilon$ für p-Silizium mit $p=10^{15}\,\mathrm{cm^{-3}}$, $\mu_\mathrm p=450\,\mathrm{cm^2/(V\,s)}$. Was geschieht nacheinander, wenn ein Elektronenblitz diese Probe trifft?

</li>

<li>

Wie groß ist $\tau_\varepsilon$ für reines Silizium ($\mu_\mathrm n=1400$, $\mu_\mathrm p=450\,\mathrm{cm^2/(V\,s)}$)? Was folgt beim Vergleich mit $\tau_\text{rec}=1$ µ s?

</li>

<li>

Mit $D_\mathrm n=35$, $D_\mathrm p=12\,\mathrm{cm^2/s}$: Wie groß ist $D_\mathrm a$ bei $n=10^{15}\,\mathrm{cm^{-3}}+\Delta$, $p=\Delta$ für $\Delta=10^{13}$, $10^{15}$, $10^{17}\,\mathrm{cm^{-3}}$? Welche Grenzwerte erwartest du?

</li>

</ol>

:::loesung
(a) $\sigma=0{,}072$ S/cm, $\tau_\varepsilon=14$ ps, $\nu_\varepsilon=11$ GHz. In rund 14 ps fließen Löcher zu und neutralisieren die Ladung. Die Paare diffundieren dann mit $D_\mathrm a\approx D_\mathrm n$, der Konstanten der Minderheit, und rekombinieren mit $\tau_\text{rec}$. (b) $\sigma=2{,}6\cdot10^{-6}$ S/cm, $\tau_\varepsilon=0{,}39$ µ s, nahe bei $\tau_\text{rec}$: In reinem Silizium trennt sich die Neutralisierung nicht mehr von der Rekombination. (c) 12,1, 15,4 und 17,8 cm$^2$/s. Grenzwerte: schwach $D_\mathrm p=12$, stark $2D_\mathrm nD_\mathrm p/(D_\mathrm n+D_\mathrm p)=17{,}9\,\mathrm{cm^2/s}$.
:::
:::
