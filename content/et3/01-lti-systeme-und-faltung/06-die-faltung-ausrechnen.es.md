---
title: Etapa 5: Calcular la convolución
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210600
summary: La integral (4.2) hay que evaluarla para señales concretas.
tags: 
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
La integral [(4.2)](das-faltungsintegral.html#gl-4-2) hay que evaluarla para señales concretas. La clave es dibujar ambos factores en función de la variable de integración $\tau$.
:::

**La receta.** Para un instante fijo $t$:

<ol>

<li>

Dibujar $s(\tau)$ en función de $\tau$.

</li>

<li>

Dibujar $h(-\tau)$: *reflejar* $h$ respecto al eje vertical.

</li>

<li>

$h(t-\tau)$: *desplazar* la $h$ reflejada una distancia $t$ hacia la derecha.

</li>

<li>

⁠*Multiplicar* ambas e *integrar* respecto a $\tau$: eso es $g(t)$.

</li>

</ol>

Si se deja crecer $t$, la $h$ reflejada se desliza de izquierda a derecha sobre $s$. Donde las dos no se solapan, $g(t)=0$.

¿Por qué reflejada? Como función de $\tau$, el argumento $t-\tau$ disminuye cuando $\tau$ crece. El comienzo de $h$ (edad cero) está en $\tau=t$; los impulsos más antiguos quedan más a la izquierda. En el circuito RC, $h$ es máxima al principio: el sistema «recuerda» con más fuerza el pasado más reciente.

::::beispiel circuito RC y pulso rectangular
La respuesta al impulso del circuito RC con la constante de tiempo $T=RC$ es un pulso exponencial decreciente de área 1. El impulso corto carga el condensador de golpe hasta $1/T$ y después se descarga a través de $R$:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Entrada: rectángulo de altura $a$ de $0$ a $T_0$. La figura [6](#abb-6) muestra la posición de los dos factores para dos instantes. Hay tres tramos:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$
::::

:::herleitung Respuesta al pulso rectangular
⁠**$t<0$:** La $h(t-\tau)$ desplazada solo es distinta de cero para $\tau\le t<0$; $s(\tau)$, solo para $\tau\ge0$. No hay solapamiento, $g=0$.

⁠**$0\le t\le T_0$:** Solapamiento para $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Solapamiento ya solo para $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

En el modelo de referencia ($a=1$, $T_0=T=1$ s): $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$, $g(3)=0{,}0855$. Es la misma curva que $g_0$ en la fig. [4](was-ein-lti-system-ist.html#abb-4).

:::abbildung et3/k1schieben 6
Convolución gráfica, $a=1$, $T_0=T=1$ s. Azul: $s(\tau)$. Rojo: $h(t-\tau)$, reflejada y desplazada una distancia $t$. El área naranja es $g(t)$: 0,3935 en $t=0{,}5$ s (solapamiento parcial), 0,2325 en $t=2$ s (todo el rectángulo cae en la parte ya amortiguada de $h$). A la derecha, la respuesta completa con ambos puntos.
:::

:::frage ¿Por qué se refleja $h$ y no $s$?
También se puede reflejar $s$ en lugar de $h$: la sustitución $\tau'=t-\tau$ convierte $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ en $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$. Se refleja la función con la que el desplazamiento resulta más claro, normalmente la de forma más sencilla.
:::

:::ltspice Respuesta al pulso rectangular
⁠**Esquema:** el circuito RC de la etapa [2](ein-erstes-system-das-rc-glied.html#stufe-2) con la fuente `PULSE(0 1 0 1u 1u 1)`: altura 1 V, duración 1 s.

⁠**Directivas:** `.tran 0 20 0 1m`; para cada instante, una medida como `.meas tran g2 FIND V(out) AT=2`, y además `.meas tran gmax MAX V(out)` y `.meas tran flaeche INTEG V(out)`.

⁠**Lo que ves:** $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$ y $g(3)=0{,}0855$, exactamente como predice [(5.2)](#gl-5-2). Compara `gmax` y `flaeche` con tu resultado del ejercicio [6](#aufg-6).
:::

:::aufgabe Ejercicio 5 ★★ Rectángulo con rectángulo
<span class="anker" id="aufg-5"></span>

Calcula $\operatorname{rect}(t)*\operatorname{rect}(t)$ con la receta. Distingue $|t|>1$, $-1\le t\le0$ y $0\le t\le1$. ¿Qué señal elemental resulta?

:::loesung
El rectángulo reflejado vuelve a ser $\operatorname{rect}$ (es simétrico); desplazado, ocupa $[t-\frac12,t+\frac12]$. La integral es la longitud del solapamiento con $[-\frac12,\frac12]$:

<ul>

<li>

$|t|>1$: sin solapamiento, 0.

</li>

<li>

$-1\le t\le0$: solapamiento de $-\frac12$ a $t+\frac12$, longitud $1+t$.

</li>

<li>

$0\le t\le1$: solapamiento de $t-\frac12$ a $\frac12$, longitud $1-t$.

</li>

</ul>

En conjunto, $1-|t|$ para $|t|\le1$: $\operatorname{rect}*\operatorname{rect}=\Lambda$. Numéricamente: 1,000; 0,500; 0,200 en $t=0$; 0,5; 0,8.
:::
:::

:::aufgabe Ejercicio 6 ★★ Comprobar la respuesta al rectángulo
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Demuestra que [(5.2)](#gl-5-2) es continua en $t=T_0$. ¿Por qué tiene que ser continua?

</li>

<li>

¿Dónde tiene $g(t)$ su máximo y cuánto vale en el modelo de referencia?

</li>

<li>

Demuestra que el área bajo $g(t)$ es igual a $aT_0$, y justifícalo sin calcular, a partir de $\int h\,\mathrm{d} t=1$.

</li>

</ol>

:::loesung
(a) En $t=T_0$: $a(1-\mathrm{e}^{-T_0/T})$ y $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$, iguales. Físicamente: la tensión del condensador no puede saltar; para ello haría falta una corriente infinita. Matemáticamente: la convolución de una señal acotada con una $h$ integrable es continua.

(b) Durante el pulso, $g$ crece; después, decrece. El máximo está en $t=T_0$: $g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0{,}632$.

(c) Cálculo:

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

Sin cálculo: el área de una convolución es el producto de las áreas, $\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Numéricamente: 1,000.
:::
:::
