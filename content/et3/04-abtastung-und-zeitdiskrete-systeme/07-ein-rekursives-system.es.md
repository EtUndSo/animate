---
title: Etapa 6: Un sistema recursivo
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3240700
summary: En el sistema IIR más sencillo se ve cómo la realimentación genera una respuesta al impulso infinitamente larga y cuándo es estable el sistema.
tags: causal, estable
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
En el sistema IIR más sencillo se ve cómo la realimentación genera una respuesta al impulso infinitamente larga y cuándo es estable el sistema.
:::

El sistema $g(n)=s(n)+b\,g(n-1)$ suma a la entrada la última salida ponderada con $b$. Para $s=\delta$ y reposo antes de $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

El impulso recorre una y otra vez el lazo de realimentación y en cada vuelta se multiplica por $b$. El sistema es __causal__ ($h(n)=0$ para $n<0$). Es __estable__ si $\sum_n|h(n)|<\infty$ (el equivalente discreto de la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), es decir, aquí exactamente para $|b|<1$, con $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Respuesta a una secuencia rectangular.** Entrada $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ unos). Con la suma de convolución y la fórmula de la suma geométrica $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

En el modelo de referencia ($b=0{,}6$, $M=4$): $g=1;\ 1{,}6;\ 1{,}96;\ 2{,}176$, luego $1{,}306;\ 0{,}783;\ 0{,}470;\dots$, cada valor 0,6 veces el anterior (fig. [5](#abb-5)). Es el equivalente discreto de la respuesta del circuito RC al pulso rectangular de la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek 5
El sistema recursivo con $b=0{,}6$. A la izquierda, la respuesta al impulso. A la derecha, la respuesta a cuatro unos: crece hasta 2,176 y después decae con el factor 0,6 por periodo de muestreo.
:::

:::aufgabe Ejercicio 5 ★★ Estudiar el sistema recursivo
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Comprueba directamente con la recursión los cinco primeros valores de $g(n)$ del modelo de referencia.

</li>

<li>

¿Hacia qué valor tiende la salida con una secuencia infinitamente larga de unos ($M\to\infty$)? Compáralo con $\sum_nh(n)$.

</li>

<li>

¿Cómo es $h(n)$ para $b=-0{,}6$ y para $b=1{,}1$? ¿Qué sistema es estable?

</li>

</ol>

:::loesung
(a) $g(0)=1$, $g(1)=1+0{,}6=1{,}6$, $g(2)=1+0{,}96=1{,}96$, $g(3)=1+1{,}176=2{,}176$, $g(4)=0+0{,}6\cdot2{,}176=1{,}306$.

(b) $\frac{1}{1-b}=2{,}5$. Es $\sum_nh(n)=\sum0{,}6^n=2{,}5$: con entrada constante 1, la convolución suma todos los valores de la respuesta al impulso. También $H_\mathrm a(0)=2{,}5$.

(c) $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\ -0{,}216;\dots$, signo alterno, decreciente, estable. $b=1{,}1$: $1;\ 1{,}1;\ 1{,}21;\dots$, creciente, inestable.
:::
:::

:::aufgabe Ejercicio 6 ★★ Sistema de primer orden
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0{,}5\,s(n-1)+0{,}6\,g(n-1)$ (fig. [4](zeitdiskrete-signale-und-die-diskrete-faltung.html#abb-4) con $a_0=1$, $a_1=0{,}5$, $b_1=0{,}6$).

<ol class="al">

<li>

Calcula de $h(0)$ a $h(3)$ con la recursión.

</li>

<li>

Demuestra que $h(n)=\frac{11}{6}\,0{,}6^n\varepsilon(n)-\frac56\delta(n)$.

</li>

</ol>

:::loesung
(a) $h(0)=1$, $h(1)=0{,}5+0{,}6\cdot1=1{,}1$, $h(2)=0{,}6\cdot1{,}1=0{,}66$, $h(3)=0{,}396$.

(b) La fórmula da $h(0)=\frac{11}{6}-\frac56=1$ y $h(1)=\frac{11}{6}\cdot0{,}6=1{,}1$. A partir de $n=2$ la entrada es nula, la recursión es $h(n)=0{,}6\,h(n-1)$, y la fórmula la cumple, porque $\frac{11}{6}0{,}6^n=0{,}6\cdot\frac{11}{6}0{,}6^{n-1}$. (Con la transformada z, la fórmula se obtiene de la descomposición $H(z)=-\frac56+\frac{11/6}{1-0{,}6z^{-1}}$.)
:::
:::
