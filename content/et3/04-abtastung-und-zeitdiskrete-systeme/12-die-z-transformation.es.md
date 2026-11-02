---
title: Etapa 11: La transformada z
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3241200
summary: Igual que la transformada de Laplace amplía la transformada de Fourier (parte 2), la transformada z amplía la transformada de Fourier de tiempo discreto: primero se pondera exponencialmente y después se transforma.
tags: circunferencia unidad
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
Igual que la transformada de Laplace amplía la transformada de Fourier ([parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)), la transformada z amplía la transformada de Fourier de tiempo discreto: primero se pondera exponencialmente y después se transforma.
:::

**La idea.** Se multiplica la secuencia por $\rho^{-n}$ ($\rho>0$) y se transforma: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$. Con $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$, esto se convierte en una serie de potencias en $z^{-1}$. De forma equivalente: $z^n$ es una función propia de todo sistema LSI, porque $z^{n-k}=z^{-k}z^n$, y el valor propio es $H(z)$:

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz Teorema 11.1 (Transformada z)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

donde la integral de contorno recorre en sentido antihorario una circunferencia $|z|=\rho$ dentro de la región de convergencia.
:::

⁠**Cómo leerlo:** sobre la circunferencia $|z|=\rho$ se encuentra un periodo del espectro de la secuencia ponderada $s(n)\rho^{-n}$. Sobre la __circunferencia unidad__ $|z|=1$, $S(z)$ es el espectro ordinario $S_\mathrm a(f)$, siempre que esta esté dentro de la región de convergencia. Así, el plano de la transformada de Laplace se aplica sobre el plano $z$: el eje imaginario se convierte en la circunferencia unidad, y el semiplano izquierdo, en su interior.

**Pares básicos y región de convergencia.** Con la serie geométrica:

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

Como en Laplace, la misma expresión corresponde a dos señales; solo la región de convergencia decide. En las secuencias por la derecha está fuera de la circunferencia que pasa por el polo más exterior; en las secuencias por la izquierda, dentro de la circunferencia que pasa por el polo más interior; en las bilaterales es un anillo. Para $b^{|n|}$ con $0<b<1$, es el anillo $b<|z|<1/b$.

**Reglas de cálculo.** La convolución se convierte en producto: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. Un retardo de $n_0$ periodos de muestreo se convierte en una multiplicación por $z^{-n_0}$. Con ello, la ecuación en diferencias [(5.2)](zeitdiskrete-signale-und-die-diskrete-faltung.html#gl-5-2) da

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

Para el sistema del ejercicio [6](ein-rekursives-system.html#aufg-6), $H(z)=\frac{1+0{,}5z^{-1}}{1-0{,}6z^{-1}}$: cero en $z=-0{,}5$, polo en $z=0{,}6$.

:::satz Teorema 11.2 (Estabilidad)
<span class="anker" id="satz-11-2"></span>

Un sistema LSI causal es estable si y solo si todos los polos de $H(z)$ están en el interior de la circunferencia unidad.
:::

⁠**Por qué:** causal significa región de convergencia fuera del polo más exterior. Estable significa $\sum|h(n)|<\infty$; entonces $H(z)$ converge sobre la circunferencia unidad, que pertenece, por tanto, a la región de convergencia. Ambas cosas a la vez solo son posibles si el polo más exterior está dentro de la circunferencia unidad. Para el sistema recursivo con $H(z)=\frac{1}{1-bz^{-1}}$, esto vuelve a significar $|b|<1$.

**Ejemplo.** $s(n)=0{,}5^n\cos(\pi n/3)\,\varepsilon(n)$. Con $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$ y [(11.2)](#gl-11-2) para $b=0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$:

$$S(z)=\frac12\Bigl[\frac{1}{1-0{,}5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0{,}5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0{,}25z^{-1}}{1-0{,}5z^{-1}+0{,}25z^{-2}},\qquad|z|>0{,}5.$$

Polos en $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j}$, ceros en $z=0$ y $z=0{,}25$ (fig. [8](#abb-8)). El módulo de los polos da el decaimiento por periodo de muestreo (0,5), y su ángulo, la oscilación ($\pi/3$ por periodo de muestreo, es decir, seis periodos de muestreo por periodo de la oscilación).

:::abbildung et3/k4zebene 8
Plano $z$ del ejemplo: polos (cruces) en $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$, ceros (círculos) en 0 y 0,25. La región de convergencia (azul) está fuera de la circunferencia que pasa por los polos y contiene la circunferencia unidad. Leída como respuesta al impulso, la secuencia describe un sistema causal y estable.
:::

:::aufgabe Ejercicio 11 ★★ Aplicar la transformada z
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Comprueba el numerador y el denominador de $S(z)$ del ejemplo reduciendo las dos fracciones a común denominador.

</li>

<li>

¿Tiene la señal del ejemplo un espectro $S_\mathrm a(f)$? Razónalo con la región de convergencia.

</li>

</ol>

:::loesung
(a) Denominador común $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$ con $a=0{,}5\mathrm{e}^{\mathrm{j}\pi/3}$: $a+a^*=2\cdot0{,}25=0{,}5$, $|a|^2=0{,}25$. Numerador $\frac12[2-(a+a^*)z^{-1}]=1-0{,}25z^{-1}$.

(b) Sí. La región de convergencia $|z|>0{,}5$ contiene la circunferencia unidad.
:::
:::

:::aufgabe Ejercicio 12 ★★ Causal o estable
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$.

<ol class="al">

<li>

¿Qué respuesta al impulso tiene la región de convergencia $|z|>2$, y cuál $|z|<2$?

</li>

<li>

¿Cuál de las dos es estable y cuál causal? ¿Hay alguna que sea ambas cosas?

</li>

</ol>

:::loesung
(a) $|z|>2$: $h(n)=2^n\varepsilon(n)$. $|z|<2$: $h(n)=-2^n\varepsilon(-n-1)$, es decir, $-\frac12,-\frac14,\dots$ para $n=-1,-2,\dots$

(b) La primera es causal, pero inestable (crece). La segunda es estable ($\sum_{n\le-1}2^n=1$), pero anticausal. Ambas cosas a la vez no son posibles: el polo en $z=2$ está fuera de la circunferencia unidad, y entonces la región de convergencia no puede estar a la vez fuera del polo y contener la circunferencia unidad.
:::
:::
