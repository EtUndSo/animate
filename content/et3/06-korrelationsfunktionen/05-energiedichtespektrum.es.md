---
title: Etapa 4: Densidad espectral de energía
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Funciones de correlación
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Capítulo 6: Funciones de correlación
order: 3260500
summary: ¿Cuál es la transformada de Fourier de una función de correlación?
tags: densidad espectral de energía, densidad espectral de energía cruzada
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
¿Cuál es la transformada de Fourier de una función de correlación? Muestra cómo se reparte la energía entre las frecuencias.
:::

:::satz Teorema 4.1 (Wiener-Khinchin para señales de energía)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**Cómo leerlo:** $|S(f)|^2$ se llama __densidad espectral de energía__. Es real, nunca negativa y, en las señales reales, par en $f$. La fase de la señal se pierde: todas las señales con el mismo espectro de amplitud tienen la misma FAC. $S^*G$ se llama __densidad espectral de energía cruzada__. La deducción solo necesita el teorema de convolución, la reflexión en el tiempo y la conjugación: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** En $\tau=0$, la FAC es la energía. Con el teorema del área:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Dos señales ortogonales tienen también espectros ortogonales: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

::::beispiel el pulso exponencial
$s(t)=\varepsilon(t)\mathrm{e}^{-t}$ tiene $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$; por tanto, $|S|^2=\frac{1}{1+(2\pi f)^2}$. Esto es a la vez $\operatorname{Re}\{S\}$, y su transformada inversa es la parte par de la señal ([capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

Lo mismo da $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ en el dominio del tiempo y $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ en el dominio de la frecuencia. La figura [2](#abb-2) muestra la señal, su FAC y los dos espectros.

:::abbildung et3/k6exp 2
Pulso exponencial ($RC=1$ s). A la izquierda, la señal y su FAC $\frac12\mathrm{e}^{-|\tau|}$ (par, máximo $=E_s=\frac12$). A la derecha, el espectro de amplitud y la densidad espectral de energía, que decae más deprisa: la energía se concentra en las frecuencias bajas.
:::
::::

:::aufgabe Ejercicio 4 ★ Comprobar Parseval
<span class="anker" id="aufg-4"></span>

Calcula la energía de $\operatorname{rect}(t)$ en el dominio del tiempo y, con [(4.2)](#gl-4-2), a partir de su espectro. ¿Qué integral conocida de la función si se deduce de ello?

:::loesung
Dominio del tiempo: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Dominio de la frecuencia: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. De ahí se deduce $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::
