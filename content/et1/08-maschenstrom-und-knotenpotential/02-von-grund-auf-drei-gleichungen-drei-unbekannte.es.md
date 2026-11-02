---
title: Desde cero: Tres ecuaciones, tres incógnitas
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1180200
summary: Por qué a una red le bastan pocas incógnitas
tags: simétrica, conductancia
lang: es
---

Ambos métodos terminan en un sistema de ecuaciones lineales $\mathbf M\,\mathbf x=\mathbf b$, es decir, una matriz por un vector columna ([Parte 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). $\mathbf x$ contiene las incógnitas, $\mathbf b$ el lado derecho conocido. Cada fila de la matriz es una ecuación, cada columna pertenece a una incógnita. Para dos incógnitas ya se conoce el determinante $\det\mathbf M=a\,d-b\,c$. Para tres incógnitas se recorre la primera fila. Cada número se multiplica por el determinante que queda al tachar su fila y su columna, y los signos se alternan ($+,-,+$):

<span class="anker" id="gl-0-1"></span>
$$\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p). \tag{0.1}$$

:::satz Teorema 0.1 (Regla de Cramer)
<span class="anker" id="satz-0-1"></span>

Si $D=\det\mathbf M\neq0$, entonces $\mathbf M\,\mathbf x=\mathbf b$ tiene exactamente una solución. Su componente $i$-ésima es

<span class="anker" id="gl-0-2"></span>
$$x_i=\frac{D_i}{D}. \tag{0.2}$$

$D_i$ es el determinante de la matriz en la que la columna $i$ se ha sustituido por $\mathbf b$.
:::

:::herleitung Cramer con dos incógnitas
De $a\,x+b\,y=e$ y $c\,x+d\,y=f$ se obtiene una ecuación sin $y$: $d$ por la primera menos $b$ por la segunda da $(a\,d-b\,c)\,x=e\,d-b\,f$. A la izquierda está $D\,x$, a la derecha el determinante con $(e,f)$ en la columna 1. Con más incógnitas funciona igual.
:::

Ejemplo: $2x+y=5$ y $x+3y=5$ tienen $D=5$, $D_1=10$, $D_2=5$, es decir, $x=2$, $y=1$. La regla sirve para el cálculo a mano hasta unas cuatro incógnitas, sobre todo si la matriz contiene muchos ceros. Una matriz se llama __simétrica__ si no cambia al reflejarla en la diagonal principal (de arriba a la izquierda a abajo a la derecha). La __conductancia__ $G=1/R$ ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) tiene como unidad el siemens: $1\,\mathrm{mS}=1/\mathrm{k\Omega}$.
