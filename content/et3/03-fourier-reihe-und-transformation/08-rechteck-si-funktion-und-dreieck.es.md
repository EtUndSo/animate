---
title: Etapa 7: Rectángulo, función si y triángulo
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3230800
summary: Tres pares de transformadas aparecen constantemente.
tags: 
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Tres pares de transformadas aparecen constantemente. Con los teoremas se obtienen de un único cálculo.
:::

**Rectángulo.** Con $\operatorname{si}(x)=\sin(x)/x$:

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz Teorema 7.1 (Rectángulo, si y triángulo)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**Cómo leerlo:** un rectángulo de duración $T$ tiene un espectro de altura $T$ (su área) con ceros en todos los múltiplos no nulos de $1/T$. El doble de largo significa la mitad de ancho en el espectro (fig. [6](#abb-6)). [(7.2)](#gl-7-2) se deduce de la simetría; [(7.3)](#gl-7-3), del teorema de convolución; y [(7.4)](#gl-7-4) se cumple porque en el dominio de la frecuencia $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$: un paso bajo ideal no altera una señal que ya está limitada a su banda.

:::abbildung et3/k3rectsi 6
$\operatorname{rect}(t/T)$ y su espectro $|T|\operatorname{si}(\pi Tf)$ para $T=1$ s y $T=2$ s. Duración doble: altura doble ($=$ área), anchura mitad, primer cero en $1/T$.
:::

:::ltspice Espectro de un pulso rectangular
⁠**Esquema:** solo una fuente `voltage` con `PULSE(0 1 0 1u 1u {T0} 16)`: un rectángulo de duración $T_0$, repetido cada 16 s.

⁠**Directivas:** `.param T0=1`, `.step param T0 list 1 2`, `.tran 0 16 0 1m`, `.options plotwinsize=0`, `.four 0.0625 40 V(in)`.

⁠**Lo que ves:** la repetición cada 16 s convierte el espectro en líneas separadas $1/16$ Hz (etapa [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4)). `.four` da sus amplitudes $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$, es decir, muestras de la envolvente si. Con $T_0=1$ s son nulas las líneas en 1 Hz y 2 Hz; con $T_0=2$ s, ya las de 0,5 Hz, 1 Hz, 1,5 Hz y 2 Hz. La componente continua se duplica de 0,0625 a 0,125. Así pues, duración doble significa anchura mitad y altura doble, como en la fig. [6](#abb-6). En la vista FFT ves directamente la envolvente con sus ceros.
:::

:::aufgabe Ejercicio 8 ★ Áreas y energía de la función si
<span class="anker" id="aufg-8"></span>

Calcula sin integrar $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ y $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$. Usa el teorema del área y Parseval.

:::loesung
Teorema del área: $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$. Parseval: $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
:::
:::

:::aufgabe Ejercicio 9 ★★ Triángulo y convolución múltiple
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Determina el espectro de $\Lambda(t/2)$ (triángulo de semianchura 2 s). ¿Dónde están los ceros?

</li>

<li>

¿Qué espectro tiene $\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$? ¿Por qué los lóbulos secundarios decrecen tanto más rápido cuantas más veces se convoluciona?

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$ y escalado con $T=2$: $\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$. Ceros en $f=k/2$, $k\neq0$.

(b) $\operatorname{si}^3(\pi f)$. Cada convolución adicional multiplica el espectro por $\operatorname{si}(\pi f)$, que en los lóbulos secundarios decrece como $1/(\pi f)$. Con $M$ rectángulos convolucionados, los lóbulos secundarios decrecen como $1/f^M$. En el dominio del tiempo: el rectángulo tiene saltos (decrecimiento $1/f$), el triángulo tiene puntos angulosos ($1/f^2$) y la convolución triple tiene derivada continua ($1/f^3$). Cuanto más suave es una señal, más rápido decrece su espectro.
:::
:::
