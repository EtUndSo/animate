---
title: Etapa 9: FFT y convolución rápida
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3241000
summary: La DFT necesita M 2 multiplicaciones.
tags: transformada rápida de Fourier, circular
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
La DFT necesita $M^2$ multiplicaciones. A la FFT le bastan aproximadamente $M\,\mathrm{lb}\,M$. Con ello, también la convolución a través del dominio de la frecuencia se vuelve rápida.
:::

**La idea de la FFT.** Con $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$ se tiene $S_d(k)=\sum_ns_d(n)W_M^{kn}$. Para $M$ par se separan los valores de índice par y los de índice impar:

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

porque $W_M^{2kn}=W_{M/2}^{kn}$. En lugar de una DFT de longitud $M$ se necesitan dos de longitud $M/2$ y $M$ multiplicaciones por $W_M^k$, es decir, $2(M/2)^2+M$ en lugar de $M^2$. Las dos DFT parciales son periódicas con periodo $M/2$; por eso dan también los valores para $k\ge M/2$. Si $M$ es una potencia de dos, la división se repite $\mathrm{lb}\,M$ veces. El coste baja a aproximadamente $M\,\mathrm{lb}\,M$. Para $M=1024$ son 10 240 multiplicaciones en lugar de 1 048 576, unas cien veces menos. Es la __transformada rápida de Fourier__ (FFT).

**Convolución circular.** Para secuencias periódicas de periodo $M$ vale la convolución __circular__ (periódica)

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

Es el resultado de la convolución ordinaria repetido periódicamente. Si $M$ es demasiado pequeño, las repeticiones se solapan. Para $s=(1,1,1)$ y $h=(1,2)$, la convolución ordinaria es $(1,3,3,2)$, con cuatro valores. Con $M=3$, el último valor cae sobre el primero: $(3,3,3)$. Con $M=4$ es correcto: $(1,3,3,2)$. En general debe cumplirse $M\ge M_1+M_2-1$ ($M_1$, $M_2$: longitudes de las dos secuencias); para ello se rellena con ceros.

**Convolución rápida.** En lugar de calcular directamente la suma de convolución, se transforman ambas secuencias con la FFT, se multiplican y se aplica la transformada inversa. Una señal de longitud arbitraria se divide en bloques, se convoluciona cada bloque por separado y se suman los resultados. Esto es lícito porque la convolución es distributiva:

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe Ejercicio 9 ★★ Circular o lineal
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Calcula a mano la convolución circular de $(1,1,1)$ y $(1,2,0)$ con $M=3$. ¿Qué valor de la convolución lineal se ha desplazado, y adónde?

</li>

<li>

Una señal de 1000 valores debe convolucionarse con un filtro de 25 valores mediante la DFT. ¿Qué longitud mínima debe tener la DFT?

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$, $g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$, $g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$. El cuarto valor de la convolución lineal (2 en $n=3$) se ha desplazado circularmente a $n=0$: $1+2=3$.

(b) Como mínimo $1000+25-1=1024$. Convenientemente, es una potencia de dos.
:::
:::
