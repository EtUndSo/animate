---
title: Etapa 4: Muestreo en el dominio de la frecuencia
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Muestreo y sistemas en tiempo discreto
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Capítulo 4: Muestreo y sistemas en tiempo discreto
order: 3240500
summary: El mismo principio vale con los papeles intercambiados: si se muestrea el espectro, la señal se vuelve periódica.
tags: 
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
El mismo principio vale con los papeles intercambiados: si se muestrea el espectro, la señal se vuelve periódica.
:::

Un espectro que solo se conoce en las frecuencias $kF$ es un peine de impulsos de Dirac ponderados. Con el factor $F$, los pesos son exactamente los coeficientes de Fourier del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

La señal correspondiente es el original repetido periódicamente con periodo $1/F$. Si la señal es más corta que $1/F$, las repeticiones no se solapan. Entonces se recupera con una ventana temporal, y el espectro, con funciones si:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**En resumen:** discreto en el tiempo significa periódico en el espectro; discreto en el espectro significa periódico en el tiempo. Lo segundo es la serie de Fourier del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): sus coeficientes son muestras del espectro de un pulso aislado, $S_p(k)=F\cdot S(kF)$.
