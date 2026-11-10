---
title: Etapa 4: La integral de convolución
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210500
summary: Con la linealidad y la invariancia en el tiempo, la respuesta a cualquier señal puede calcularse a partir de la respuesta a un único pulso corto.
tags: impulso de Dirac, respuesta al impulso
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Con la linealidad y la invariancia en el tiempo, la respuesta a *cualquier* señal puede calcularse a partir de la respuesta a un único pulso corto. El resultado es la integral de convolución.
:::

**La idea en cuatro pasos.**

<ol>

<li>

⁠**Descomponer.** Se aproxima la señal de entrada por una escalera de rectángulos estrechos de anchura $T_0$. Como bloque elemental sirve un rectángulo $s_0(t)$ de duración $T_0$ y altura $1/T_0$, es decir, de área 1. El peldaño en $nT_0$ es este bloque, desplazado $nT_0$ y ponderado con $s(nT_0)\,T_0$, el área de la franja:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Un bloque a través del sistema.** A $s_0$ el sistema responde con $g_0(t)$. Esto hay que conocerlo una vez.

</li>

<li>

⁠**Recomponer.** Invariancia en el tiempo: el bloque desplazado produce la respuesta desplazada. Linealidad: los pesos y la suma pasan a través del sistema. Por tanto,

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Paso al límite $T_0\to0$.** La escalera se convierte en la señal. El rectángulo de área 1 se convierte en el __impulso de Dirac__ (delta de Dirac) $\delta(t)$, un impulso infinitamente corto de área 1. Su respuesta se llama __respuesta al impulso__ $h(t)$. De $nT_0$ resulta la variable continua $\tau$; de $T_0$, el diferencial $\mathrm{d}\tau$; de las sumas, integrales.

</li>

</ol>

:::abbildung et3/k1treppe 5
Arriba: un pulso triangular $s(t)=\Lambda(t-1)$ y su aproximación escalonada con $T_0=0{,}5$ s. Abajo: la respuesta exacta del circuito RC y la suma de las respuestas a los rectángulos desplazados. La desviación máxima baja de 0,17 ($T_0=0{,}5$ s) a 0,08 ($0{,}25$ s) y a 0,03 ($0{,}1$ s).
:::

:::satz Teorema 4.1 (Integral de convolución)
<span class="anker" id="satz-4-1"></span>

Para toda señal $s(t)$ se cumple

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

y un sistema LTI con respuesta al impulso $h(t)$ responde a ella con

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**Cómo leerlo:** $\tau$ es el instante de un impulso de entrada, y $s(\tau)\,\mathrm{d}\tau$, su peso (el área de la franja). $h(t-\tau)$ es la respuesta del sistema en el instante $t$ a un impulso que llegó en el instante $\tau$, es decir, hace $t-\tau$ segundos. La salida reúne todos los impulsos del pasado, cada uno ponderado según cuánto lo «recuerda» todavía el sistema al cabo de ese tiempo. La ecuación es exacta y vale para todo sistema LTI.

⁠**En resumen:** la salida de un sistema LTI es la superposición de sus respuestas al impulso, desplazadas a cada instante de la entrada y ponderadas con el valor de la entrada en ese instante.

:::frage ¿Por qué los bloques rectangulares tienen que tener área 1?
Para que la respuesta al bloque conserve una forma fija en el paso al límite. Un rectángulo de altura fija 1 tendría área cero para $T_0\to0$, y su respuesta desaparecería. Con la altura $1/T_0$, el área sigue siendo 1, y la respuesta tiende a $h(t)$. En el circuito RC, el pico de la respuesta es $(1-\mathrm{e}^{-T_0})/T_0$: 0,632 para $T_0=1$ s, 0,787 para 0,5 s, 0,952 para 0,1 s, y para $T_0\to0$ pasa a ser $1=h(0^+)$. El área de la respuesta sigue siendo siempre 1.
:::

:::frage ¿Existe en la realidad el impulso $\delta(t)$? ¿Cómo se mide entonces $h(t)$?
Un impulso infinitamente corto no existe. Pero basta cualquier pulso mucho más corto que las constantes de tiempo del sistema. Entonces el sistema solo ve su área, y la respuesta es prácticamente $(\text{área})\cdot h(t)$. En el circuito RC con $RC=1$ s, el pico de la respuesta a un pulso de 1 ms se desvía solo un 0,05 % de $h(0^+)$. Así se miden también las respuestas al impulso: se da una palmada en una sala y se graba la reverberación.
:::

:::ltspice Aproximar la respuesta al impulso con un rectángulo corto
⁠**Esquema:** el circuito RC de la etapa [2](ein-erstes-system-das-rc-glied.html#stufe-2) con la fuente `PULSE(0 {1/T0} 0 1n 1n {T0})`: un rectángulo de anchura $T_0$ y altura $1/T_0$, es decir, de área 1.

⁠**Directivas:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran spitze MAX V(out)`, `.meas tran flaeche INTEG V(out)`.

⁠**Lo que ves:** los picos valen 0,632; 0,787; 0,952 y 0,9995, como $(1-\mathrm{e}^{-T_0})/T_0$. Con el pulso de 1 ms, la respuesta ya es prácticamente $h(t)=\mathrm{e}^{-t}$. El área vale 1,000 en las cuatro simulaciones: un pulso mucho más corto que $RC$ solo actúa a través de su área.
:::

:::aufgabe Ejercicio 4 ★★ La escalera, más de cerca
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Calcula la respuesta $g_0(t)$ del circuito RC ($RC=1$ s) al rectángulo de altura $1/T_0$ de $0$ a $T_0$. Usa para ello [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5) y escribe el rectángulo como diferencia de dos escalones.

</li>

<li>

Demuestra que $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ y que tiende a 1 para $T_0\to0$.

</li>

<li>

¿Por qué la aproximación $g_a$ de la fig. [5](#abb-5) va retrasada? (Pista: ¿dónde está el peldaño respecto al triángulo en el flanco ascendente y en el descendente?)

</li>

</ol>

:::loesung
(a) El rectángulo es $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linealidad e invariancia en el tiempo con la respuesta al escalón [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5):

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) En $t=T_0$ el segundo sumando es nulo: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. Con $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ para $T_0$ pequeño, esto es $\approx1-T_0/2\to1=h(0^+)$. Valores numéricos: 0,632; 0,787; 0,952 para $T_0=1$; 0,5; 0,1 s.

(c) Cada peldaño mantiene el valor $s(nT_0)$ desde el *comienzo* del intervalo hasta su final. Por eso, en el flanco ascendente la escalera queda por debajo del triángulo, y en el descendente, por encima: en promedio está retrasada $T_0/2$. La salida hereda este retraso; en el lado descendente, $g_a$ queda por encima de $g$ ($g_a(2)=0{,}508$ en lugar de $0{,}400$ para $T_0=0{,}5$ s). Con un $T_0$ menor se reduce el retraso y, con él, el error.
:::
:::
