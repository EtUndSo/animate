---
title: Etapa 2: El paso bajo ideal
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3250300
summary: El paso bajo ideal deja pasar sin alteración todas las frecuencias hasta f mathrm g y bloquea todas las superiores.
tags: duración de la señal
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
El paso bajo ideal deja pasar sin alteración todas las frecuencias hasta $f_\mathrm g$ y bloquea todas las superiores. Esta etapa muestra qué significa este corte abrupto en el dominio del tiempo.
:::

:::satz Teorema 2.1 (Paso bajo ideal)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**Cómo leerlo:** la respuesta al impulso se extiende hasta el infinito en ambas direcciones. Por tanto, el paso bajo ideal *no es causal*: tendría que responder a un impulso antes de que este llegue. Es un objeto matemático límite al que solo es posible aproximarse (etapas [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)).

**Duración y ancho de banda.** Como __duración de la señal__ $t_m$ de una respuesta al impulso se toma la anchura de un rectángulo con la misma altura $h_{\max}$ y la misma área:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

En el paso bajo ideal, $H(0)=1$ y $h_{\max}=2f_\mathrm g$; por tanto, $t_m=\frac{1}{2f_\mathrm g}$ y $f_\mathrm g\cdot t_m=\frac12$. En general, para los filtros paso bajo se cumple $f_\mathrm g\cdot t_m=\text{cte.}$: el doble de ancho de banda significa la mitad de duración de la respuesta. Es el teorema de escalado (semejanza) del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

**Sobreoscilación.** En la función si, la relación entre el máximo secundario de mayor valor absoluto, $a_1$, y el máximo principal $a_0$ es

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21{,}7\,\%,$$

independiente de $f_\mathrm g$ (el primer mínimo secundario de $\operatorname{si}(\pi u)$ está en $u=1{,}43$ y vale $-0{,}217$). Un cambio de $f_\mathrm g$ solo comprime la curva; no cambia su forma.

:::aufgabe Ejercicio 2 ★ Paso bajo ideal para voz
<span class="anker" id="aufg-2"></span>

Un paso bajo ideal con $f_\mathrm g=4$ kHz. ¿Cuánto valen la duración de la señal de la respuesta al impulso y la sobreoscilación? ¿Qué cambia con $f_\mathrm g=8$ kHz?

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s, sobreoscilación del 21,7 %. Con 8 kHz, la duración se reduce a la mitad, a 62,5 µ s. La sobreoscilación sigue siendo del 21,7 %, porque la respuesta al impulso solo se comprime.
:::
:::
