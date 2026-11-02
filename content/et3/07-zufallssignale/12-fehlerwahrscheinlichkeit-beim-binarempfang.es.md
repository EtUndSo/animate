---
title: Etapa 11: Probabilidad de error en la recepción binaria
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3271200
summary: El receptor debe decidir: ¿se envió el pulso o no?
tags: 
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
El receptor debe decidir: ¿se envió el pulso o no? ¿Con qué frecuencia se equivoca?
:::

**La idea.** La muestra a la salida del filtro adaptado tiene distribución gaussiana con la varianza $N$ (ruido) y el valor medio $\sqrt{S_a}$ si se envió el pulso, o 0 si no se envió. El receptor la compara con un umbral de decisión $C$. Se produce un error cuando el ruido empuja el valor al otro lado del umbral. Las dos probabilidades de error son las áreas de las dos curvas de Gauss más allá del umbral:

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

Si ambos casos se envían con la misma frecuencia, la probabilidad de error media es $\frac12(P_{e1}+P_{e0})$. Es mínima cuando el umbral está justo en el punto medio, $C=\sqrt{S_a}/2$. Con el filtro adaptado ($S_a/N=E_s/N_0$):

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**Cómo leerlo:** la probabilidad de error solo depende de $E_s/N_0$ y cae con muchísima rapidez: con 10 dB, $5{,}7\cdot10^{-2}$; con 16 dB, $8\cdot10^{-4}$; con 20 dB, $2{,}9\cdot10^{-7}$ (fig. [4](#abb-4)). Unos pocos decibelios más de energía de la señal convierten una transmisión inservible en una casi libre de errores.

:::abbildung et3/k7pe 4
Probabilidad de error mínima en la recepción todo-nada con filtro adaptado. Puntos rojos: 10 dB, 16 dB, 20 dB.
:::

:::aufgabe Ejercicio 11 ★★ Probabilidad de error
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Calcula $P_{e,\min}$ para $E_s/N_0=10$ dB. Pista: $\operatorname{erfc}(1{,}118)=0{,}114$.

</li>

<li>

¿Por qué el umbral óptimo está en el punto medio entre 0 y $\sqrt{S_a}$? ¿Qué les ocurre a $P_{e1}$ y $P_{e0}$ si se desplaza hacia arriba?

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$: $\sqrt{10/8}=1{,}118$, $P_{e,\min}=\frac12\cdot0{,}114=0{,}057$.

(b) Las dos curvas de Gauss tienen la misma anchura. La suma de las dos áreas de error es mínima donde se cortan las curvas, y por simetría ese punto es el punto medio. Si se desplaza el umbral hacia arriba, $P_{e0}$ disminuye, pero $P_{e1}$ crece más, porque el umbral se adentra en la parte densa de la curva superior.
:::
:::
