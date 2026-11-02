---
title: Etapa 7: Correlación en tiempo discreto y periódica
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Funciones de correlación
order: 3260800
summary: Con muestras, la integral se convierte en una suma.
tags: correlación rápida
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Con muestras, la integral se convierte en una suma. Con la DFT, las correlaciones se calculan rápidamente.
:::

:::satz Teorema 7.1 (Correlación en tiempo discreto)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{periodo }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

Para señales paso bajo muestreadas se cumple $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ y $E_s=T\sum_n|s(nT)|^2$. Una señal de energía en tiempo discreto es una secuencia de cuadrado sumable.

**Ejemplo.** $s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ para $m=-2,\dots,2$. Máximo $6=E_s$ en $m=0$, par, cinco valores en lugar de tres. Comprobación con Wiener-Khinchin en $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.

**Correlación periódica.** Como en la convolución ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)), para secuencias de periodo $M$ se cumple

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Calculada con la FFT, se llama __correlación rápida__. Para que la correlación periódica reproduzca la ordinaria, $M$ tiene que ser suficientemente grande. Para $(1,2,1)$, $M=3$ da la secuencia solapada $(6,5,5)$; $M=5$, en cambio, da $(6,4,1,1,4)$, la FAC ordinaria dispuesta de forma cíclica.

**Señales de potencia.** Para señales de energía infinita se promedia:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

Si ambas señales son periódicas con el mismo periodo, basta con un periodo, y la función de correlación también es periódica. Ejemplo: $A\cos(2\pi Ft+\varphi_0)$ tiene la FAC $\frac{A^2}{2}\cos(2\pi F\tau)$. La fase $\varphi_0$ ha desaparecido; en $\tau=0$ se obtiene la potencia $\frac{A^2}{2}$.

:::aufgabe Ejercicio 6 ★ FAC discreta
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Comprueba a mano la FAC de $(1,2,1)$.

</li>

<li>

Determina la FAC de $(1,-1)$. ¿Qué indica $\varphi(\pm1)<0$ sobre la señal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. Un valor negativo con el desplazamiento 1 significa que los valores vecinos tienden a tener signos opuestos: la señal cambia rápidamente. En consonancia con ello, $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ es nula en $f=0$ y máxima en $f=\frac12$: una señal paso alto.
:::
:::

:::aufgabe Ejercicio 7 ★★ FAC de un coseno
<span class="anker" id="aufg-7"></span>

Deduce la FAC de $A\cos(2\pi Ft+\varphi_0)$ con [(7.4)](#gl-7-4) sobre un periodo. ¿Por qué desaparece $\varphi_0$ y qué significa eso para la medida de la fase con la FAC?

:::loesung
Con $\omega=2\pi F$ y $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

La segunda integral abarca dos periodos completos y es nula. La fase $\varphi_0$ solo desplaza el origen de tiempos, y el promedio sobre todos los instantes no conoce ningún origen. Por eso, con la FAC de una sola señal no se puede medir ninguna fase. En cambio, la diferencia de fase de *dos* señales sí la muestra la correlación cruzada.
:::
:::
