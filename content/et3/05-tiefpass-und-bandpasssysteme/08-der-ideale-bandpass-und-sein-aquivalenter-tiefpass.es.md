---
title: Etapa 7: El paso banda ideal y su paso bajo equivalente
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3250800
summary: Un paso banda deja pasar una banda en torno a la frecuencia central f 0 .
tags: paso bajo equivalente, simétrico
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Un paso banda deja pasar una banda en torno a la frecuencia central $f_0$. Esta etapa muestra que se puede describir por completo mediante un paso bajo y la frecuencia $f_0$.
:::

**Paso banda ideal.** Dos rectángulos de anchura $\Delta f$ en $\pm f_0$ ($f_0>\Delta f/2$):

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

La respuesta al impulso es una oscilación de frecuencia $f_0$ cuya envolvente es la respuesta al impulso de un paso bajo de ancho de banda $\Delta f/2$. La regla de modulación del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) lo explica: es un paso bajo cuyo espectro se desplaza a $\pm f_0$.

**Paso bajo equivalente.** Con una respuesta al impulso real, $H(-f)=H^*(f)$: la mitad negativa no contiene nada nuevo. Se conservan solo las frecuencias positivas, se duplican y se desplazan hacia la izquierda una frecuencia portadora $f_0$. El resultado es el __paso bajo equivalente__ $H_T(f)$:

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{para}\ f\le-f_0. \tag{7.2}$$

$H_T$ no tiene por qué ser simétrico respecto a $f=0$; por tanto, su respuesta al impulso $h_T(t)$ puede ser compleja. Si existe un $f_0$ para el que se cumple $H_T(-f)=H_T^*(f)$ (y, por tanto, $h_T$ es real), el paso banda se llama __simétrico__. En el paso banda ideal con $f_0$ en el centro, $H_T(f)=2\operatorname{rect}(f/\Delta f)$ y $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, real y par. Es un caso especial: también los filtros paso banda simétricos tienen, por lo general, una parte imaginaria en el espectro.

:::aufgabe Ejercicio 7 ★★ Paso bajo equivalente con otra referencia
<span class="anker" id="aufg-7"></span>

Paso banda ideal de 9 a 11 Hz.

<ol class="al">

<li>

Determina $H_T$ y $h_T$ para $f_0=10$ Hz.

</li>

<li>

Determina $H_T$ y $h_T$ para $f_0=9$ Hz. ¿Por qué ahora $h_T$ es compleja? ¿Describen ambos el mismo paso banda?

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz: tras el desplazamiento, la banda queda simétrica, de $-1$ a $1$ Hz. $H_T=2\operatorname{rect}(f/2)$, $h_T=4\operatorname{si}(2\pi t)$, real.

(b) $f_0=9$ Hz: la banda va de 0 a 2 Hz. $H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$, $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$. Es compleja porque $H_T$ no es simétrico respecto a $f=0$. Ambos describen el mismo paso banda: $\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$, lo mismo que en (a) y que [(7.1)](#gl-7-1).
:::
:::
