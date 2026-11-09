---
title: Etapa 8: La transformada discreta de Fourier (DFT)
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3240900
summary: S mathrm a(f) es una función continua, pero un ordenador necesita una cantidad finita de números.
tags: 
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ es una función continua, pero un ordenador necesita una cantidad finita de números. Para una secuencia de longitud finita basta con un número finito de muestras del espectro.
:::

**La idea.** Si $s(n)$ está limitada a $M$ valores, según la etapa [4](abtastung-im-frequenzbereich.html#stufe-4) bastan muestras del espectro con separación $F=1/M$. A ellas les corresponde la señal $s_d(n)$, repetida periódicamente con periodo $M$. Como el espectro también es periódico (tiempo discreto), bastan $M$ valores espectrales. Ahora ambos lados son discretos y periódicos.

:::satz Teorema 8.1 (Transformada discreta de Fourier)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**Cómo leerlo:** $S_d(k)$ es el valor del espectro $S_\mathrm a(f)$ en $f=k/M$. El índice $k$ numera las oscilaciones que caben exactamente $k$ veces en los $M$ valores. La transformada inversa es una serie de Fourier de $M$ términos. Los teoremas valen de forma análoga, por ejemplo el desplazamiento $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$ (circular: lo que sale por el final vuelve a entrar por el principio) y Parseval $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$.

::::beispiel
$s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Comprobación: $S_d(3)=S_d^*(1)$, porque la señal es real ($k=3$ corresponde a $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.
::::

:::aufgabe Ejercicio 8 ★★ DFT a mano
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Comprueba $S_d(1)$ para $s_d=(1,2,0,-1)$.

</li>

<li>

Determina con el teorema de desplazamiento la DFT de la secuencia desplazada circularmente $(-1,1,2,0)$ y comprueba $S_d(1)$ directamente.

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$, porque $(-\mathrm{j})^3=\mathrm{j}$.

(b) Desplazamiento en $m=1$: $S_d(k)\,(-\mathrm{j})^k$, es decir, $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$. Directamente: $S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$.
:::
:::
