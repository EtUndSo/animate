---
title: Etapa 3: Respuesta al escalón y tiempo de subida
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3250400
summary: ¿Cómo reacciona el paso bajo ideal a un escalón?
tags: seno integral, tiempo de subida
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
¿Cómo reacciona el paso bajo ideal a un escalón? ¿Con qué rapidez sube y cuánto sobrepasa el valor final?
:::

La respuesta al escalón es la integral acumulada de la respuesta al impulso ([capítulo 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Con el __seno integral__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

se obtiene

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung Respuesta al escalón
La integral hasta $t$ se divide en 0. La parte de $-\infty$ a 0 es la mitad del área de $h$, es decir, $\frac12H(0)=\frac12$, porque $h$ es par. Para el resto se sustituye $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$: $\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$. El valor $\operatorname{Si}(\infty)=\frac\pi2$ se obtiene del teorema del área: $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$, por tanto $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$.
:::

⁠**Cómo leerlo:** en $t=0$, la respuesta vale exactamente $\frac12$; empieza ya antes (no es causal) y tiende a 1. El __tiempo de subida__ $t_e$ se define como el tiempo que tarda en subir una rampa con la pendiente máxima de la respuesta al escalón. La pendiente máxima es $h(0)=2f_\mathrm g$; por tanto,

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

La sobreoscilación de la respuesta al escalón es del $8{,}95\,\%$ (en $t=\frac{1}{2f_\mathrm g}$). Es el fenómeno de Gibbs del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): un $f_\mathrm g$ mayor acorta el tiempo de subida; la sobreoscilación se mantiene (fig. [1](#abb-1)).

:::abbildung et3/k5sprung 1
Respuesta al escalón del paso bajo ideal para $f_\mathrm g=1$ Hz y 2 Hz. En trazo discontinuo, la rampa con la pendiente máxima: su tiempo de subida es $t_e=1/(2f_\mathrm g)=0{,}5$ s. Las dos curvas tienen la misma sobreoscilación: llegan hasta 1,0895.
:::

:::frage Un paso bajo con más ancho de banda es «mejor», ¿no? Entonces, ¿por qué no disminuye la sobreoscilación?
Porque se debe a la *forma* de la respuesta en frecuencia, no a su anchura. La sobreoscilación surge en el flanco vertical en $f_\mathrm g$: todas las frecuencias hasta ahí llegan completas, y de las superiores no llega nada. Si se desplaza el flanco, sigue vertical, y la respuesta al escalón solo se comprime en el tiempo. La sobreoscilación solo disminuye si el flanco se vuelve suave (etapa [5](echomethode-und-pulsformfilter.html#stufe-5)).
:::

:::aufgabe Ejercicio 3 ★★ Seno integral
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Demuestra que $h_\varepsilon(0)=\frac12$ y $h_\varepsilon(\infty)=1$ con [(3.1)](#gl-3-1).

</li>

<li>

¿Dónde está el máximo de la respuesta al escalón? Pista: la derivada de la respuesta al escalón es la respuesta al impulso.

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$, $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$.

(b) La pendiente de la respuesta al escalón es $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$. Se anula por primera vez en $2\pi f_\mathrm gt=\pi$ y ahí pasa de positiva a negativa. Por tanto, el máximo está en $t=\frac{1}{2f_\mathrm g}$ y vale $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1{,}852}{\pi}=1{,}0895$.
:::
:::
