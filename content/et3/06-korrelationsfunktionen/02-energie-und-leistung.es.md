---
title: Etapa 1: Energía y potencia
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Funciones de correlación
order: 3260200
summary: Antes de comparar señales hace falta una medida de su «tamaño».
tags: energía de la señal, señal de energía, potencia, señal de potencia
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Antes de comparar señales hace falta una medida de su «tamaño». En teoría de sistemas, esa medida es la energía y, en las señales de duración infinita, la potencia.
:::

En una resistencia $R$, durante el intervalo de $t_1$ a $t_2$ se convierte en calor la energía $\frac1R\int u^2\mathrm{d} t$. Sin el factor $1/R$, la expresión se llama __energía de la señal__:

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

Si es finita, $s$ se llama __señal de energía__ (por ejemplo, cualquier pulso). Si una señal dura indefinidamente sin decaer (un coseno, un escalón), su energía es infinita. Entonces se mide la __potencia__ media:

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

Si es finita, $s$ se llama __señal de potencia__. En las señales periódicas basta con promediar sobre un periodo. Para los impulsos de Dirac no están definidas ni la energía ni la potencia ($\delta^2$ no existe).

:::aufgabe Ejercicio 1 ★ ¿Energía o potencia?
<span class="anker" id="aufg-1"></span>

Determina la energía o la potencia de (a) $a\operatorname{rect}(t/T)$, (b) $\varepsilon(t)\mathrm{e}^{-t}$, (c) $A\cos(2\pi Ft)$, (d) $\varepsilon(t)$.

:::loesung
(a) $E=a^2|T|$. (b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$. (c) Energía infinita, potencia $\frac{A^2}{2}$ (el valor medio de $\cos^2$ es $\frac12$). (d) Energía infinita, potencia $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$: la señal vale 1 durante la mitad del tiempo.
:::
:::
