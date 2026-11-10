---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3231300
summary: Toda señal como superposición de oscilaciones
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Una señal periódica es una suma de oscilaciones en múltiplos de la frecuencia fundamental (serie de Fourier); una señal no periódica, una integral sobre todas las frecuencias (integral de Fourier).

</li>

<li>

Cada oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ es una función propia: un sistema LTI la multiplica por $H(f)$, y por eso la convolución se convierte en el producto $G(f)=S(f)\,H(f)$.

</li>

<li>

Todas las reglas de cálculo (desplazamiento, dilatación, modulación, simetría) se deducen de lo que cada operación hace con una única oscilación.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$; $H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.

</li>

<li>

Serie: $s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$, $S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$; real: $S_p(-k)=S_p^*(k)$.

</li>

<li>

Parseval: $\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$; Gibbs: sobreoscilación de aproximadamente el 9 % en los saltos; LTI: $G_p(k)=S_p(k)H(kF)$.

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, $s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$; $s*h\leftrightarrow SH$, $s_1s_2\leftrightarrow S_1*S_2$.

</li>

<li>

Real: $S(-f)=S^*(f)$; par $\leftrightarrow\operatorname{Re} S$, impar $\leftrightarrow\mathrm{j}\operatorname{Im} S$.

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$; $s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$; $\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$; $\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$; $S(t)\leftrightarrow s(-f)$.

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$; $\Lambda\leftrightarrow\operatorname{si}^2$; $\delta\leftrightarrow1$; $1\leftrightarrow\delta(f)$; $\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$.

</li>

<li>

Peine $\leftrightarrow$ peine: $\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$; $\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

</li>

<li>

Hilbert: $h=\frac{1}{\pi t}$, $H=-\mathrm{j}\operatorname{sgn}(f)$; $s_+=\frac12(s+\mathrm{j}\hat s)$, $s=2\operatorname{Re} s_+$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.**

| Resultado | De dónde viene |
|---|---|
| Respuesta en frecuencia $H(f)$ | valor propio de la oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ (etapa [1](schwingungen-als-eigenfunktionen.html#stufe-1)) |
| Serie de Fourier, solo múltiplos de $F$ | solo estas oscilaciones tienen el periodo $T$ (etapa [2](periodische-signale-die-fourier-reihe.html#stufe-2)) |
| Fórmula de análisis de la serie | las oscilaciones de frecuencias distintas son ortogonales (etapa [2](periodische-signale-die-fourier-reihe.html#stufe-2)) |
| Parseval, Gibbs, LTI con entrada periódica | cada armónico por separado (etapa [3](leistung-konvergenz-und-lti-systeme.html#stufe-3)) |
| Integral de Fourier | periodo $\to\infty$, las líneas se acercan entre sí (etapa [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4)) |
| $S(-f)=S^*(f)$ en señales reales | las oscilaciones aparecen en pares conjugados (etapa [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)) |
| Desplazamiento, dilatación, derivación, modulación | lo que la operación hace con $\mathrm{e}^{\mathrm{j}2\pi ft}$ (etapa [6](die-rechenregeln-theoreme.html#stufe-6)) |
| Simetría (dualidad) | la transformada directa y la inversa solo se diferencian en el signo (etapa [6](die-rechenregeln-theoreme.html#stufe-6)) |
| Espectros de líneas, peine de Dirac, escalón | casos límite con impulsos de Dirac (etapa [8](singulare-signale-und-linienspektren.html#stufe-8)) |
| Transformada de Hilbert | una señal causal queda determinada por una mitad (etapa [9](hilbert-transformation-und-analytisches-signal.html#stufe-9)) |
| Fourier de tiempo corto | espectro de un fragmento (etapa [10](kurzzeit-fourier-transformation.html#stufe-10)) |
