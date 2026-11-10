---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Funciones de correlación
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Capítulo 6: Funciones de correlación
order: 3260900
summary: ¿Cuánto se parecen dos señales y cómo se reparte la energía en frecuencia?
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

La semejanza de dos señales se mide con la integral de su producto. La función de correlación lo hace para cada desplazamiento $\tau$; es una convolución con la señal reflejada.

</li>

<li>

La transformada de Fourier de la función de autocorrelación (FAC) es la densidad espectral de energía $|S(f)|^2$. En $\tau=0$ se obtiene la energía (Parseval).

</li>

<li>

Al pasar por un sistema LTI, las densidades espectrales de energía se multiplican por $|H(f)|^2$, y las funciones de autocorrelación se convolucionan con la función de autocorrelación de $h$.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$; $L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$.

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$, $|p|\le1$, $p=0$: ortogonales.

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$; $\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$.

</li>

<li>

FAC: par (señal real), máximo $\varphi^E_{ss}(0)=E_s$, duración doble.

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$, $\varphi^E_{sg}\leftrightarrow S^*G$; Parseval $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$.

</li>

<li>

Wiener-Lee: $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$, $|G|^2=|S|^2|H|^2$; $\varphi^E_{sg}=\varphi^E_{ss}*h$.

</li>

<li>

Paso banda: $\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$.

</li>

<li>

Discreto: $\varphi(m)=\sum s^*(n)g(n+m)$, $\leftrightarrow|S_\mathrm a|^2$; periódico: $S_d^*G_d$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** La correlación es una convolución con una señal reflejada. Por eso valen todas las herramientas de la convolución:

| Resultado | De dónde viene |
|---|---|
| Coeficiente de correlación | energía de la diferencia de dos señales normalizadas (etapa [2](ahnlichkeit-messen-der-korrelationskoeffizient.html#stufe-2)) |
| Producto de correlación | convolución con la señal reflejada y conjugada (etapa [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3)) |
| FAC par, máximo en 0 | reflejar, y a lo que más se parece una señal es a sí misma (etapa [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3)) |
| Densidad espectral de energía, Parseval | reflejar y conjugar da $S^*$, la convolución se convierte en producto (etapa [4](energiedichtespektrum.html#stufe-4)) |
| Wiener-Lee | ley asociativa de la convolución (etapa [5](korrelation-und-lti-systeme.html#stufe-5)) |
| Caso discreto, periódico, DFT | el mismo cálculo con sumas (etapa [7](zeitdiskrete-und-periodische-korrelation.html#stufe-7)) |
