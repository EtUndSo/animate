---
title: Etapa 5: Señales en tiempo discreto y convolución discreta
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3240600
summary: A partir de ahora solo se calcula con las secuencias de números s(n) .
tags: convolución discreta, impulso unitario, invariante al desplazamiento, sistema LSI, respuesta al impulso, diferencia, acumulación, filtro FIR
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
A partir de ahora solo se calcula con las secuencias de números $s(n)$. Esta etapa traslada a las secuencias la convolución, las señales elementales y los sistemas LTI.
:::

**Convolución de las muestras.** Si la entrada $s$ y la respuesta al impulso $h$ de un sistema son señales paso bajo y se muestrea a la tasa de Nyquist, cada una puede escribirse como serie de funciones si [(3.3)](abtasttheorem-und-ruckgewinnung.html#gl-3-3). Como $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), las muestras de la salida se obtienen solo a partir de las muestras:

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

Normalizada a $T=1$, es la __convolución discreta__:

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**Secuencias elementales.**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

El __impulso unitario__ $\delta(n)$ es una secuencia ordinaria, no una distribución: en $n=0$ vale 1. Es el elemento neutro de la convolución discreta, $s(n)*\delta(n)=s(n)$. Un rectángulo de $2M+1$ unos centrado en $n=0$ es $\varepsilon(n+M)-\varepsilon(n-M-1)$.

**Lineal e invariante al desplazamiento.** Un sistema en tiempo discreto se llama lineal si cumple el principio de superposición, e __invariante al desplazamiento__ si $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ para todo entero $m$. Si cumple ambas cosas, se llama __sistema LSI__. Con la __respuesta al impulso__ $h(n)=\operatorname{Tr}\{\delta(n)\}$ se obtiene, como en la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html):

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

Aquí no hace falta ningún paso al límite: una secuencia *ya es* una suma de impulsos unitarios ponderados y desplazados.

**Diferencia y suma.** El equivalente de la derivada es la __diferencia__ $g(n)=s(n)-s(n-1)$, es decir, $h(n)=\delta(n)-\delta(n-1)$. El equivalente de la integral es la __acumulación__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. Una deshace a la otra: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$.

**Ecuaciones en diferencias, FIR e IIR.** En lugar de ecuaciones diferenciales, los sistemas en tiempo discreto se describen mediante ecuaciones en diferencias:

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{parte FIR}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{parte IIR}}. \tag{5.2}$$

La salida es una suma ponderada de valores pasados de la entrada y de la salida. Si solo depende de valores de la entrada ($b_p=0$), la respuesta al impulso termina al cabo de $Q+1$ valores: es un __filtro FIR__ (*finite impulse response*, respuesta al impulso finita). Con realimentación ($b_p\neq0$), la respuesta al impulso puede ser infinitamente larga: es un __filtro IIR__ (*infinite impulse response*, respuesta al impulso infinita). Ambos se construyen con elementos de retardo (memoria para un periodo de muestreo), multiplicadores y sumadores (fig. [4](#abb-4)).

:::abbildung et3/k4block 4
Sistema de primer orden $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. El bloque $T$ almacena un valor durante un periodo de muestreo. A la izquierda, la parte no recursiva; a la derecha, la realimentación de la salida.
:::

:::aufgabe Ejercicio 4 ★ Convolución discreta a mano
<span class="anker" id="aufg-4"></span>

Convoluciona $s=(1,1,1)$ con $h=(1,2)$, ambas empezando en $n=0$. ¿Qué longitud tiene el resultado y por qué?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Longitud $3+2-1=4$: el último valor no nulo aparece cuando el último valor de $h$ coincide con el último valor de $s$.
:::
:::
