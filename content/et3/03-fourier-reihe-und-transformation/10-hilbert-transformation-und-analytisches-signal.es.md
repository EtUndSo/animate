---
title: Etapa 9: Transformada de Hilbert y señal analítica
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3231000
summary: En una señal causal, las partes real e imaginaria del espectro están relacionadas: una determina la otra.
tags: transformada de Hilbert, componente analítica, paso todo
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
En una señal causal, las partes real e imaginaria del espectro están relacionadas: una determina la otra. El mismo cálculo proporciona una señal que solo contiene frecuencias positivas.
:::

**Señales causales.** Si $s(t)=0$ para $t<0$, las partes par e impar son iguales para $t>0$ ($\frac12s$) y opuestas para $t<0$. Por tanto, $s_u(t)=s_g(t)\operatorname{sgn}(t)$ y $s_g(t)=s_u(t)\operatorname{sgn}(t)$. En el dominio de la frecuencia, la multiplicación por $\operatorname{sgn}$ se convierte en la convolución con $\frac{1}{\mathrm{j}\pi f}$:

:::satz Teorema 9.1 (Relación de Hilbert de las señales causales)
<span class="anker" id="satz-9-1"></span>

Para una señal causal se cumple

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**Cómo leerlo:** la convolución con $\frac{1}{\pi f}$ se llama __transformada de Hilbert__. En un sistema causal basta con conocer la parte real de la respuesta en frecuencia; la parte imaginaria se deduce de ella. La causalidad es, por tanto, una restricción fuerte sobre el espectro.

**Componente analítica.** Con el escalón en el *dominio de la frecuencia* se eliminan las frecuencias negativas: $S_+(f)=S(f)\,\varepsilon(f)$. De la simetría se sigue $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, por tanto

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ se llama __componente analítica__, y $\hat s$, transformada de Hilbert de $s$. Para señales reales, $S_-(f)=S_+^*(-f)$, es decir, $s_-=s_+^*$ y $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. Las partes real e imaginaria de $s_+$ son, a su vez, transformadas de Hilbert la una de la otra.

**El transformador de Hilbert.** El sistema LTI con $h(t)=\frac{1}{\pi t}$ tiene $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: módulo 1 en todas las frecuencias (un __paso todo__), fase $-90^\circ$ para $f>0$ y $+90^\circ$ para $f<0$. A partir de $\cos(2\pi Ft)$ produce

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**En resumen:** el transformador de Hilbert desfasa cada oscilación $90^\circ$ sin cambiar su amplitud.

:::aufgabe Ejercicio 12 ★★ Transformador de Hilbert
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

¿Qué hace el transformador de Hilbert con $\sin(2\pi Ft)$? ¿Qué da aplicarlo dos veces?

</li>

<li>

Determina la componente analítica $s_+(t)$ de $\cos(2\pi Ft)$ y comprueba que $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

¿Por qué el transformador de Hilbert no es causal? Fíjate en $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplicación por $-\mathrm{j}\operatorname{sgn}(f)$: en $-F$ por $+\mathrm{j}$, en $+F$ por $-\mathrm{j}$. Resultado: $-\frac12\delta(f+F)-\frac12\delta(f-F)$, es decir, $-\cos(2\pi Ft)$. Aplicado dos veces: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$; la señal se invierte.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, por tanto $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. Esto concuerda con $\frac12(s+\mathrm{j}\hat s)$ con $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ es distinta de cero también para $t<0$. Por tanto, la salida en el instante $t$ depende de valores futuros de la entrada. En la práctica, el transformador de Hilbert se aproxima con una respuesta al impulso truncada, a cambio de aceptar un retardo.
:::
:::
