---
title: Etapa 7: Transformada de Fourier de tiempo discreto
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Muestreo y sistemas en tiempo discreto
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Capítulo 4: Muestreo y sistemas en tiempo discreto
order: 3240800
summary: ¿Qué espectro tiene una secuencia de números?
tags: convolución periódica
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
¿Qué espectro tiene una secuencia de números? Es el espectro de la señal muestreada idealmente, calculado directamente a partir de las muestras.
:::

Si se introduce $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ en la integral de Fourier, con la propiedad de muestreo queda una suma. Normalizada a $T=1$:

:::satz Teorema 7.1 (Transformada de Fourier de tiempo discreto)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**Cómo leerlo:** el espectro $S_\mathrm a(f)$ es periódico con periodo 1, que es la frecuencia de muestreo. Un periodo, $|f|\le\frac12$, lo contiene todo. Por eso la transformada inversa solo integra sobre un intervalo de longitud 1. La suma es una serie de Fourier en $f$, con las muestras como coeficientes.

::::beispiel
Para $s(n)=\varepsilon(n)\,b^n$ con $|b|<1$ (serie geométrica):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

Es a la vez la respuesta en frecuencia $H_\mathrm a(f)$ del sistema recursivo de la etapa [6](ein-rekursives-system.html#stufe-6). Para $b=0{,}6$: $|H_\mathrm a|=2{,}5$ en $f=0$, $1{,}60$ en $f=0{,}1$, $0{,}86$ en $f=0{,}25$ y $0{,}625$ en $f=0{,}5$ (fig. [6](#abb-6)). El sistema es un paso bajo, pero con respuesta en frecuencia periódica: en $f=1$ vuelve a amplificar tanto como en $f=0$.

:::abbildung et3/k4dtft 6
Módulo de la respuesta en frecuencia del sistema recursivo con $b=0{,}6$. Es periódico con la frecuencia de muestreo. Entre las líneas rojas está el único periodo que lo describe todo.
:::
::::

**Convolución y multiplicación.** Como con las funciones, se cumple $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. El producto de dos secuencias da la __convolución periódica__ de los espectros sobre un periodo:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Ejercicio 7 ★ Media móvil
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ promedia tres valores consecutivos.

<ol class="al">

<li>

Demuestra que $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

¿En qué frecuencia es $H_\mathrm a=0$? ¿Qué oscilación elimina, por tanto, el filtro por completo, y por qué (pista: suma de tres valores de una oscilación de periodo 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, es decir, $f=\frac13$ (con $f_\mathrm A=1$ kHz: 333 Hz). Una oscilación con tres valores por periodo consta de tres fasores separados $120^\circ$. Su suma es nula: el filtro ve en cada ventana exactamente un periodo completo.
:::
:::
