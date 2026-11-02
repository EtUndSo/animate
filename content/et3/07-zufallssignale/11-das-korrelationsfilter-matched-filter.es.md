---
title: Etapa 10: El filtro adaptado (matched filter)
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3271100
summary: Un pulso conocido s(t) llega con ruido.
tags: filtro adaptado, correlador
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Un pulso conocido $s(t)$ llega con ruido. ¿Con qué filtro se hace más visible en el instante de muestreo $T$?
:::

**El planteamiento.** A la entrada del receptor llega $s(t)+n(t)$, con ruido blanco $n$. Un filtro $h$ entrega $y=g+n_e$, con la componente útil $g=s*h$ y la componente de ruido $n_e=n*h$. Se muestrea en $T$. La relación señal-ruido en ese instante es

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

La fracción de la derecha es el cuadrado de un coeficiente de correlación ([parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), entre $h(\tau)$ y $s(T-\tau)$. Vale como máximo 1, y lo alcanza exactamente cuando ambas tienen la misma forma.

:::satz Teorema 10.1 (Filtro adaptado)
<span class="anker" id="satz-10-1"></span>

Frente al ruido blanco, la mejor relación señal-ruido alcanzable es

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{alcanzada con}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**Cómo leerlo:** la mejor respuesta al impulso es la propia señal reflejada en el tiempo y desplazada $T$: el __filtro adaptado__ (también filtro de correlación, en inglés *matched filter*). Su salida sin ruido es $g(t)=a\,\varphi^E_{ss}(t-T)$, la FAC desplazada de la señal, y se muestrea justo en su máximo. Lo sorprendente es que el resultado solo depende de la *energía* de la señal, no de su forma. Un pulso corto y alto es tan bueno como uno largo y plano con la misma energía. Para que el filtro sea causal, $T$ tiene que ser como mínimo la duración de la señal. Equivalente es un __correlador__ (receptor de correlación): multiplica la señal recibida por $s(t)$ e integra sobre la duración de la señal.

:::aufgabe Ejercicio 10 ★★ Un pulso rectangular en el ruido
<span class="anker" id="aufg-10"></span>

Un pulso rectangular de altura 1 V y duración 1 ms se recibe con ruido blanco de densidad espectral de potencia $N_0=10^{-6}$ V$^2$/Hz.

<ol class="al">

<li>

¿Cómo es el filtro adaptado y qué $S_a/N$ (en dB) alcanza?

</li>

<li>

¿Cómo es la salida sin ruido y cuándo hay que muestrear?

</li>

<li>

El pulso se acorta a 0,25 ms, con la misma altura. ¿Qué cambia?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: de nuevo un rectángulo de 1 ms, causal con $T\ge1$ ms. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s; por tanto, $S_a/N=10^{-3}/10^{-6}=1000$, es decir, 30 dB.

(b) La FAC del rectángulo, un triángulo de anchura 2 ms, desplazado $T$: empieza a subir en $t=T-1\,\mathrm{ms}$ y alcanza su máximo en $t=T$. Con $T=1$ ms se muestrea justo al final del pulso; entonces el filtro lo ha «visto» entero.

(c) $E_s$ baja a la cuarta parte, $S_a/N=250$, es decir, 24 dB, 6 dB peor. Solo cuenta la energía. Con la misma altura, un pulso más corto significa menos energía.
:::
:::
