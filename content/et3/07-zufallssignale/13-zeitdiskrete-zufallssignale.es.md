---
title: Etapa 12: Señales aleatorias en tiempo discreto
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3271300
summary: Todo vale también para secuencias de números aleatorios, con sumas en lugar de integrales.
tags: ruido blanco en tiempo discreto
lang: es
---

<span class="anker" id="stufe-12"></span>

:::zweck
Todo vale también para secuencias de números aleatorios, con sumas en lugar de integrales.
:::

Si se muestrea un proceso de banda limitada a $f_\mathrm g$ con $T\le\frac{1}{2f_\mathrm g}$, las muestras forman un proceso en tiempo discreto $s(n)$. Las distribuciones, los valores esperados y las correlaciones se definen como antes; las medias temporales son sumas, por ejemplo $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. A través de un sistema LSI con $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

con la densidad espectral de potencia periódica $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ y $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. El __ruido blanco en tiempo discreto__ tiene $\Phi_{ss,\mathrm a}=N$ y $\varphi_{ss}(m)=N\delta(m)$: los números consecutivos están incorrelados. A diferencia del caso continuo, su potencia es finita, $L_s=N$.

**Ejemplo 1: promedio de dos valores.** Ruido blanco con distribución uniforme ($\sigma_s^2=\frac1{12}$) a través de $h(n)=\frac12[\delta(n)+\delta(n-1)]$, es decir, $g(n)=\frac12[s(n)+s(n-1)]$. Con $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

La varianza se reduce a la mitad, a $\frac{1}{24}$, y los valores de salida vecinos están ahora correlados (comparten un valor de entrada). Los valores de salida tienen distribución triangular, porque cada uno es la semisuma de dos números independientes con distribución uniforme. Una simulación con 200 000 números da la varianza 0,0415 en lugar de $\frac1{24}=0{,}0417$.

**Ejemplo 2: filtro recursivo (proceso AR(1)).** Ruido blanco de varianza $\sigma_s^2$ a través de $h(n)=b^n\varepsilon(n)$ ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). Con $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

Para $b=0{,}6$, la varianza es $1{,}56$ veces la varianza de entrada, y los valores vecinos tienen el coeficiente de correlación $0{,}6$. Cuanto más se acerca $b$ a 1, más intensas son las frecuencias bajas (fig. [5](#abb-5)).

:::abbildung et3/k7ar 5
Densidades espectrales de potencia de procesos AR(1), periódicas con periodo 1. Para $b=0{,}6$ van de 6,25 ($f=0$) a 0,39 ($f=\frac12$); para $b=0{,}9$, de 100 a 0,28.
:::

:::aufgabe Ejercicio 12 ★★ Proceso AR(1)
<span class="anker" id="aufg-12"></span>

Ruido blanco con distribución uniforme ($\sigma_s^2=\frac1{12}$) pasa por $g(n)=s(n)+0{,}6\,g(n-1)$.

<ol class="al">

<li>

Calcula la varianza de salida y $\varphi_{gg}(1)/\varphi_{gg}(0)$.

</li>

<li>

Deduce $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ con la serie geométrica.

</li>

<li>

¿Sigue teniendo la salida distribución uniforme? ¿Qué distribución esperas aproximadamente y por qué?

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0{,}36}=0{,}130$, $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0{,}6$. La simulación da 0,130 y 0,600.

(b) Para $m\ge0$: $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$. La FAC de energía de la respuesta al impulso es par; por tanto, rige $b^{|m|}$.

(c) Ya no tiene distribución uniforme: cada valor de salida es una suma ponderada de muchos valores de entrada independientes, $g(n)=\sum_kb^ks(n-k)$. Según el teorema central del límite, tiene aproximadamente distribución gaussiana. Con $b=0{,}6$ solo contribuyen de forma apreciable unos pocos sumandos; por eso la aproximación es burda, pero la distribución ya tiene claramente forma de campana.
:::
:::
