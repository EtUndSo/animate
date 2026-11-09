---
title: Etapa 9: Señal paso banda en un sistema paso banda
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3251000
summary: La utilidad de las envolventes: el efecto de un paso banda sobre una señal paso banda se calcula por completo en el dominio paso bajo.
tags: 
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
La utilidad de las envolventes: el efecto de un paso banda sobre una señal paso banda se calcula por completo en el dominio paso bajo.
:::

:::satz Teorema 9.1 (Transmisión en el dominio paso bajo equivalente)
<span class="anker" id="satz-9-1"></span>

Si $S_T$ y $H_T$ cumplen ambos [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) (nada por debajo de $-f_0$), para la envolvente de la salida se cumple

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Transmisión
Al desarrollar $G=S\cdot H$ con ambas representaciones [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) se obtienen cuatro productos. Los cruzados, por ejemplo $S_T(f-f_0)H_T^*(-f-f_0)$, son nulos: el primer factor vive en las frecuencias positivas, y el segundo, en las negativas. Queda $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. La comparación con $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ da $G_T=\frac12S_TH_T$.
:::

⁠**Cómo leerlo:** el factor $\frac12$ compensa que $S_T$ y $H_T$ se hayan duplicado ambos. Por lo demás, es el teorema de convolución habitual, solo que para las envolventes. Ni siquiera hace falta incluir la portadora en el cálculo.

::::beispiel coseno conectado que atraviesa el paso banda ideal
$s(t)=\varepsilon(t)\cos(2\pi f_0t)$ con $f_0=10$ Hz; paso banda con $\Delta f=2$ Hz en torno a $f_0$. La envolvente de la entrada es $s_T\approx\varepsilon(t)$. (Aproximación: el espectro del escalón no está limitado a $f>-f_0$, pero en la banda de paso, $|f|\le\Delta f/2\ll f_0$, es válida.) Con $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

La envolvente es la respuesta al escalón de un paso bajo ideal con $f_\mathrm g=\Delta f/2$: tiempo de subida $1/\Delta f=0{,}5$ s, sobreoscilación del 8,95 % (fig. [5](#abb-5)). Un paso banda estrecho tarda mucho en alcanzar el «régimen permanente».

:::abbildung et3/k5bandpass 5
Respuesta del paso banda ideal ($f_0=10$ Hz, $\Delta f=2$ Hz) a un coseno de la frecuencia central conectado en $t=0$. En azul, la señal de salida; en rojo, la envolvente $\pm g_T(t)$. Sube en aproximadamente 0,5 s y, con la sobreoscilación, llega hasta 1,09.
:::
::::

:::ltspice Portadora conectada a través de un circuito resonante
Un paso banda ideal no se puede construir; un circuito resonante serie, sí. **Esquema:** fuente `voltage` en el nodo `in` y luego, en serie, `ind` con `{L}`, `cap` con `{1/((2*pi*f0)**2*L)}` y `res` con `{2*pi*df*L}` a masa. La salida `out` es la tensión en la resistencia. Con `.param f0=10 df=2 L=1`, la frecuencia central es 10 Hz, y el ancho de banda entre los puntos de $-3$ dB, 2 Hz.

⁠**Comprobación:** el valor de fuente `AC 1` y `.ac lin 2001 5 15` muestran el máximo 1 en 10 Hz y los puntos de $-3$ dB en 9,05 Hz y 11,05 Hz.

⁠**Experimento:** fuente `SINE(0 1 10 0 0 90)`, que es $\varepsilon(t)\cos(2\pi f_0t)$, y `.tran 0 3 0 0.1m`. La envolvente sube sin sobreoscilación: los picos de la portadora alcanzan 0,72 a los 0,2 s, 0,96 a los 0,5 s y prácticamente 1 al cabo de 1 s, casi exactamente como $1-\mathrm{e}^{-t/0{,}16\,\mathrm s}$. El paso banda ideal, en cambio, sobreoscila hasta 1,09 (fig. [5](#abb-5)). La razón es la misma que en el paso bajo de la etapa [3](sprungantwort-und-einschwingzeit.html#stufe-3): los flancos del circuito resonante son suaves; los del paso banda ideal, verticales.
:::
