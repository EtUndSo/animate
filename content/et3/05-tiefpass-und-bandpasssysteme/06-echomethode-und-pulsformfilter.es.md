---
title: Etapa 5: Método de ecos y filtros conformadores de pulsos
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3250600
summary: ¿Cómo se diseña un paso bajo con menos sobreoscilación?
tags: eco, filtro de coseno alzado
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
¿Cómo se diseña un paso bajo con menos sobreoscilación? Se compone la respuesta al impulso a partir de funciones si desplazadas y se eligen sus pesos.
:::

**Método de ecos.** Según el teorema de muestreo, toda respuesta al impulso de un paso bajo hasta $f_\mathrm g=\frac{1}{2T}$ es una serie de funciones si:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

Cada muestra $h(nT)$ es un __eco__: una función si desplazada en $nT$. En el espectro, esto se convierte en una serie de Fourier en $f$. Si $h$ es real y par, $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$.

**Filtro conformador de pulsos.** A la componente principal $\operatorname{si}(\pi t/T)$ se añaden dos ecos de amplitud $a$ a una distancia de $\pm T$. Con $a=\frac12$, las oscilaciones secundarias se cancelan en gran parte, y el espectro adquiere un flanco suave de forma cosenoidal:

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

Este es el __filtro de coseno alzado__. Su sobreoscilación es del 2,7 % en lugar del 21,7 %; a cambio, el lóbulo principal es el doble de ancho (primer cero en $2T$ en lugar de $T$). La figura [3](#abb-3) muestra ambas respuestas al impulso normalizadas a la misma área.

:::abbildung et3/k5pulsform 3
Respuestas al impulso del paso bajo ideal y del filtro conformador de pulsos (ambas con área $T$). El filtro conformador de pulsos decae mucho más rápido: su mayor máximo secundario es el 2,7 % del máximo principal, en lugar del 21,7 %.
:::

**Filtro transversal.** Una suma de copias retardadas y ponderadas se construye con una cadena de elementos de retardo cuyas tomas se ponderan y se suman. Para que ningún elemento deba acceder al futuro, se retrasa todo en bloque. Es la misma estructura que un filtro FIR ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

:::aufgabe Ejercicio 5 ★★ El filtro de coseno alzado
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Deduce $H(f)$ en [(5.3)](#gl-5-3) a partir de [(5.1)](#gl-5-1).

</li>

<li>

¿Qué valor tiene $H$ en $f=0$ y en $f=f_\mathrm g=\frac{1}{2T}$? ¿Por qué el flanco es suave ahí?

</li>

</ol>

:::loesung
(a) En $t=mT$, $\operatorname{si}(\pi(t\pm T)/T)$ solo vale 1 para $m=\mp1$; en los demás casos es nula. Por tanto, $h(0)=1$, $h(\pm T)=\frac12$ y todos los demás $h(nT)=0$. Según [(5.1)](#gl-5-1): $H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$.

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. También la pendiente $-2\pi T^2\sin(2\pi Tf)$ es nula en $f=\frac{1}{2T}$. La respuesta en frecuencia llega a cero sin salto y sin punto anguloso. Cuanto más suave es el espectro, más rápido decae la respuesta al impulso ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::
