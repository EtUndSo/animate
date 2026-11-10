---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3251400
summary: Transmisión sin distorsión, paso bajo ideal, envolvente compleja y retardo de grupo
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Sin distorsión significa que la señal solo se amplifica y se retrasa. Para ello hacen falta un módulo constante y una fase que decrece linealmente con la frecuencia.

</li>

<li>

Un paso bajo con límite abrupto (ideal) no es causal, presenta en los saltos una sobreoscilación de aproximadamente el 9 % y necesita un tiempo de subida de $1/(2f_\mathrm g)$. Unos flancos más suaves reducen la sobreoscilación a costa de la selectividad.

</li>

<li>

Una señal paso banda es una señal paso bajo (la envolvente compleja) sobre una portadora. Con la envolvente se calcula como con una señal paso bajo: sufre el retardo de grupo, y la portadora, el retardo de fase.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Sin distorsión: $h=h_0\delta(t-t_0)$, $H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: módulo constante, fase lineal.

</li>

<li>

$a=-20\lg|H|$ dB; $t_\mathrm p=-\frac{\varphi}{2\pi f}$; $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$.

</li>

<li>

Paso bajo ideal: $\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$, no causal; $f_\mathrm g t_m=\frac12$; sobreoscilación del 21,7 % (impulso) y del 8,95 % (escalón).

</li>

<li>

Respuesta al escalón $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$, $\operatorname{Si}(\infty)=\frac\pi2$, tiempo de subida $\frac{1}{2f_\mathrm g}$.

</li>

<li>

Truncar la respuesta al impulso $=$ convolución en el espectro; ventanas suaves: mayor rechazo, flanco más tendido.

</li>

<li>

Filtro conformador de pulsos: $T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$, poca sobreoscilación.

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$; $s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$; $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

</li>

<li>

$g_T=\frac12s_T*h_T$; la envolvente se retrasa $t_\mathrm g$, y la portadora, $t_\mathrm p$.

</li>

<li>

Muestreo paso banda: $2\Delta f$ valores por segundo; paso alto digital: $(-1)^nh_{\mathrm{TP}}(n)$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.**

| Resultado | De dónde viene |
|---|---|
| Sistema sin distorsión | cada oscilación amplificada por igual y retrasada el mismo tiempo (etapa [1](das-verzerrungsfreie-system.html#stufe-1)) |
| Retardo de fase y de grupo | retardo de la portadora y de la envolvente, respectivamente (etapas [1](das-verzerrungsfreie-system.html#stufe-1), [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)) |
| Duración de la señal $\cdot$ ancho de banda $=$ cte. | teorema de escalado o de semejanza (etapa [2](der-ideale-tiefpass.html#stufe-2)) |
| Sobreoscilación del 21,7 % y del 8,95 % | lóbulos secundarios de la función si, Gibbs (etapas [2](der-ideale-tiefpass.html#stufe-2), [3](sprungantwort-und-einschwingzeit.html#stufe-3)) |
| Aproximación causal, diseño con ventanas | truncar la respuesta al impulso = convolución en el espectro (etapas [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)) |
| Filtro conformador de pulsos | flanco suave en el espectro, respuesta al impulso que decae rápidamente (etapa [5](echomethode-und-pulsformfilter.html#stufe-5)) |
| Paso bajo equivalente, envolvente compleja | desplazar las frecuencias positivas hacia cero (etapas [7](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#stufe-7), [8](komplexe-hullkurve-und-quadraturkomponenten.html#stufe-8)) |
| Esquema en cuadratura, muestreo paso banda | calcular el paso banda en el dominio paso bajo (etapa [10](quadraturschaltung-und-bandpass-abtastung.html#stufe-10)) |
