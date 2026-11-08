---
title: El producto matriz-vector
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15210800
summary: La misma suma ponderada debe calcularse para todos los ejemplos de un conjunto de datos.
tags: producto matriz-vector, espacio columna
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
La misma suma ponderada debe calcularse para todos los ejemplos de un conjunto de datos. Esta sección introduce para ello el producto de una matriz por un vector y muestra las dos formas de leerlo: fila por fila o columna por columna.
:::

### Matriz por vector

<span class="anker" id="stufe-7-1"></span>

La agente inmobiliaria de la subsección [2.2](das-skalarprodukt.html#stufe-2-2) estima cada vivienda con la misma suma ponderada. Para cuatro viviendas calcula cuatro veces $\mathbf{w}^{\top}\mathbf{x}_i$. Si se escriben las viviendas como filas de una matriz, los cuatro cálculos pueden expresarse en un solo paso: cada fila de la matriz se multiplica por el mismo vector.

:::definition Definición 7.1 (Producto matriz-vector)
<span class="anker" id="satz-7-1"></span>

Para $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{x}\in\mathbb{R}^n$, el __producto matriz-vector__ $\mathbf{A}\mathbf{x}$ es el vector de $\mathbb{R}^m$ con las componentes

<span class="anker" id="gl-7-1"></span>
$$(\mathbf{A}\mathbf{x})_i=\sum_{j=1}^{n}a_{ij}\,x_j=a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n ,\qquad i=1,\dots,m . \tag{7.1}$$
:::

El producto solo existe si $\mathbf{x}$ tiene tantas componentes como columnas tiene $\mathbf{A}$. El resultado tiene tantas componentes como filas tiene $\mathbf{A}$. De las reglas de cálculo de las sumas se deduce: $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ y $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$.

⁠**Ejemplo numérico:** Para

$$\mathbf{A}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\quad\text{y}\quad \mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}\qquad\text{se tiene}\qquad \mathbf{A}\mathbf{x}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

Cada componente es una suma según [(7.1)](#gl-7-1) (fig. [28](#abb-28)). Una matriz $3\times2$ por un vector con $2$ componentes da un vector con $3$ componentes.

:::abbildung ml/k1rmv 28
El producto matriz-vector componente por componente: para cada fila $i$, las entradas $a_{ij}$ se multiplican por los $x_j$ correspondientes y se suman.
:::

⁠**En resumen:** $\mathbf{A}\mathbf{x}$ es el vector cuya componente $i$ es la suma $\sum_ja_{ij}x_j$; una matriz $m\times n$ convierte un vector de $\mathbb{R}^n$ en un vector de $\mathbb{R}^m$.

### La visión por filas: muchos productos escalares

<span class="anker" id="stufe-7-2"></span>

La fórmula [(7.1)](#gl-7-1) dice, para cada componente: la fila $i$ de la matriz, multiplicada entrada por entrada por $\mathbf{x}$ y sumada. Eso es el producto escalar de la fila $i$ con $\mathbf{x}$ (fig. [30](#abb-30), izquierda).

:::satz Teorema 7.2 (Visión por filas)
<span class="anker" id="satz-7-2"></span>

La componente $i$ de $\mathbf{A}\mathbf{x}$ es el producto escalar de la $i$-ésima fila de $\mathbf{A}$ con $\mathbf{x}$. Para una matriz de datos $\mathbf{X}$ con las filas $\mathbf{x}_i^{\top}$ y un vector de pesos $\mathbf{w}$, esto significa

<span class="anker" id="gl-7-2"></span>
$$\mathbf{X}\mathbf{w}=\begin{pmatrix}\mathbf{x}_1^{\top}\mathbf{w}\\\vdots\\\mathbf{x}_N^{\top}\mathbf{w}\end{pmatrix}. \tag{7.2}$$
:::

El producto matriz-vector aplica, por tanto, la suma ponderada con los pesos $\mathbf{w}$ a todos los ejemplos a la vez y da el vector de todas las predicciones. En la imagen de la comparación con un patrón: cada ejemplo se compara con el mismo patrón $\mathbf{w}$.

⁠**Ejemplo numérico:** Para el conjunto de datos de viviendas y $\mathbf{w}=(3,\,10,\,-4)^{\top}$ se tiene

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3\\10\\-4\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix},$$

las cuatro predicciones de la agente inmobiliaria en miles de euros. Cada componente es el producto escalar de una fila con $\mathbf{w}$ (fig. [29](#abb-29)).

:::abbildung ml/k1rzeilen 29
La visión por filas para la agente inmobiliaria: cada vivienda, es decir, cada fila de $\mathbf{X}$, por los pesos $\mathbf{w}$.
:::

⁠**En resumen:** En la visión por filas, $\mathbf{A}\mathbf{x}$ es una lista de productos escalares, uno por fila; $\mathbf{X}\mathbf{w}$ son las predicciones para todos los ejemplos.

:::hintergrund Cuánto trabajo de cálculo cuesta un producto matriz-vector
Cada una de las $m$ componentes necesita $n$ multiplicaciones y $n-1$ sumas. En total son $m(2n-1)$, es decir, unas $2mn$ operaciones aritméticas básicas. Para las cuatro viviendas con tres características son $4\cdot5=20$. Para un conjunto de datos con un millón de ejemplos y cien características son unas $2\cdot10^8$. Un procesador actual ejecuta varios miles de millones de operaciones de este tipo por segundo; un único producto matriz-vector de este tamaño se resuelve, por tanto, rápidamente. Pero tales recuentos solo indican el orden de magnitud del tiempo de cálculo, pues la velocidad real de un ordenador depende también de lo rápido que pueda traer los números de la memoria.
:::

### La visión por columnas: una combinación lineal de las columnas

<span class="anker" id="stufe-7-3"></span>

La misma suma también puede ordenarse de otro modo. En lugar de proceder fila por fila, se reúnen todas las contribuciones que corresponden a $x_1$, luego todas las que corresponden a $x_2$, y así sucesivamente. Las contribuciones de $x_j$ están todas en la columna $j$ de la matriz. Entonces el producto se convierte en una combinación lineal de las columnas (fig. [30](#abb-30), derecha).

:::abbildung ml/k1zeilenspalten 30
Dos formas de leer $\mathbf{A}\mathbf{x}$ para $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ y $\mathbf{x}=(2,\,1)^{\top}$. A la izquierda, la visión por filas: la componente $1$ del resultado es el producto escalar de la primera fila con $\mathbf{x}$. A la derecha, la visión por columnas: $\mathbf{A}\mathbf{x}$ es $2$ veces la primera columna $\mathbf{a}_1=(2,1)^{\top}$ más $1$ vez la segunda columna $\mathbf{a}_2=(1,1)^{\top}$.
:::

:::satz Teorema 7.3 (Visión por columnas)
<span class="anker" id="satz-7-3"></span>

Si $\mathbf{a}_1,\dots,\mathbf{a}_n$ son las columnas de $\mathbf{A}\in\mathbb{R}^{m\times n}$, entonces

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n=\sum_{j=1}^nx_j\,\mathbf{a}_j . \tag{7.3}$$

El producto matriz-vector es la combinación lineal de las columnas de $\mathbf{A}$ con las componentes de $\mathbf{x}$ como coeficientes.
:::

:::beweis Visión por columnas
La componente $i$ del lado derecho es $\sum_jx_j\,(\mathbf{a}_j)_i=\sum_jx_j\,a_{ij}$, pues la $i$-ésima componente de la columna $\mathbf{a}_j$ es la entrada $a_{ij}$. Eso es exactamente la componente $i$ de $\mathbf{A}\mathbf{x}$ según [(7.1)](#gl-7-1).
:::

⁠**Ejemplo numérico 1:** Para el producto $\mathbf{A}\mathbf{x}$ de la subsección [7.1](#stufe-7-1) se tiene

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=2\begin{pmatrix}1\\0\\3\end{pmatrix}+1\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

⁠**Ejemplo numérico 2:** Las predicciones de la agente inmobiliaria son $3$ veces la columna de las superficies más $10$ veces la columna de las habitaciones más $(-4)$ veces la columna de las distancias (fig. [31](#abb-31)). Las columnas de $\mathbf{X}$ se llaman aquí, como en la subsección [6.1](matrizen-und-die-datenmatrix.html#stufe-6-1), $\mathbf{a}_1$, $\mathbf{a}_2$, $\mathbf{a}_3$. En esta forma se ve qué parte de cada predicción procede de qué característica: el primer sumando contiene las contribuciones de la superficie; el segundo, las de las habitaciones; el tercero, las de la distancia.

:::abbildung ml/k1rspalten 31
La visión por columnas para la agente inmobiliaria: cada columna $\mathbf{a}_j$ de $\mathbf{X}$ se multiplica por su peso $w_j$ y después se suman los tres vectores.
:::

⁠**En resumen:** En la visión por columnas, $\mathbf{A}\mathbf{x}$ es una combinación lineal de las columnas de $\mathbf{A}$; las componentes de $\mathbf{x}$ dicen cuánto se toma de cada columna.

:::hintergrund Por qué hay dos visiones del mismo cálculo
Ambas visiones calculan los mismos $m\cdot n$ productos $a_{ij}x_j$ y los suman. La visión por filas los agrupa primero por filas; la visión por columnas, primero por columnas; con un número finito de sumandos, el orden es indiferente, como en la suma doble de la subsección [1.1](vektoren-daten-als-zahlenlisten.html#stufe-1-1). Pero cada visión responde a una pregunta distinta. La visión por filas pregunta: ¿qué sale en la componente $i$? La visión por columnas pregunta: ¿qué resultados puede dar la matriz en absoluto si $\mathbf{x}$ se elige libremente? La segunda pregunta lleva directamente al siguiente concepto.
:::

### El espacio columna

<span class="anker" id="stufe-7-4"></span>

Si $\mathbf{x}$ recorre todos los vectores de $\mathbb{R}^n$, $\mathbf{A}\mathbf{x}$ recorre, según la visión por columnas, todas las combinaciones lineales de las columnas. En general, no son todos los vectores de $\mathbb{R}^m$.

:::definition Definición 7.4 (Espacio columna)
<span class="anker" id="satz-7-4"></span>

El __espacio columna__ de una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ es el conjunto de todos los vectores $\mathbf{A}\mathbf{x}$ con $\mathbf{x}\in\mathbb{R}^n$, es decir, el conjunto de todas las combinaciones lineales de las columnas de $\mathbf{A}$.
:::

⁠**Ejemplo numérico 1:** La matriz $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ tiene las columnas $(1,\,2)^{\top}$ y $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. Toda combinación lineal es un múltiplo de $(1,\,2)^{\top}$. El espacio columna es, por tanto, solo la recta que pasa por el origen en la dirección $(1,\,2)^{\top}$, aunque los resultados tengan dos componentes. El vector $(3,\,6)^{\top}$ está en él; el vector $(1,\,1)^{\top}$, no.

⁠**Ejemplo numérico 2:** La matriz $\mathbf{H}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ da $\mathbf{H}\mathbf{x}=(x_1,\,x_2,\,x_1+x_2)^{\top}$. Su espacio columna consta de los vectores de $\mathbb{R}^3$ cuya tercera componente es la suma de las dos primeras; es un plano en el espacio. El vector $(1,\,2,\,3)^{\top}=\mathbf{H}\,(1,\,2)^{\top}$ está en él; $(1,\,1,\,1)^{\top}$, no, pues $1+1\ne1$.

Para una matriz de datos, esto significa: las predicciones $\mathbf{X}\mathbf{w}$ están siempre en el espacio columna de $\mathbf{X}$, sean cuales sean los pesos elegidos. Con estas características solo pueden generarse listas de predicciones muy concretas.

⁠**En resumen:** El espacio columna de una matriz es el conjunto de todos los vectores $\mathbf{A}\mathbf{x}$, es decir, todo lo que puede obtenerse como combinación lineal de sus columnas.

:::aufgabe Ejercicio 16 ★ Dos visiones de un producto
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

Calcula $\mathbf{B}\mathbf{x}$ para $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ y $\mathbf{x}=(1,\,3,\,-1)^{\top}$, una vez con la visión por filas y otra con la visión por columnas.

</li>

<li>

¿Está definido $\mathbf{B}\,(1,\,2)^{\top}$? ¿Y $\mathbf{B}\,(1,\,2,\,3)^{\top}$? Justifícalo con los tamaños e indica cuántas componentes tiene el resultado cuando está definido.

</li>

<li>

¿Está $(2,\,0,\,2)^{\top}$ en el espacio columna de la matriz $\mathbf{H}$ de la subsección [7.4](#stufe-7-4)? ¿Y $(2,\,1,\,2)^{\top}$?

</li>

</ol>

:::loesung
(a) Visión por filas: $(1\cdot1+0\cdot3+2\cdot(-1),\ 2\cdot1+1\cdot3+0\cdot(-1))^{\top}=(-1,\,5)^{\top}$. Visión por columnas: $1\,(1,\,2)^{\top}+3\,(0,\,1)^{\top}-1\,(2,\,0)^{\top}=(1+0-2,\ 2+3-0)^{\top}=(-1,\,5)^{\top}$.

(b) $\mathbf{B}$ tiene tres columnas. $\mathbf{B}\,(1,\,2)^{\top}$ no está definido, porque el vector solo tiene dos componentes. $\mathbf{B}\,(1,\,2,\,3)^{\top}$ está definido y tiene tantas componentes como filas tiene $\mathbf{B}$, es decir, dos: $(1+0+6,\ 2+2+0)^{\top}=(7,\,4)^{\top}$.

(c) El espacio columna de $\mathbf{H}$ consta de los vectores cuya tercera componente es la suma de las dos primeras. Para $(2,\,0,\,2)^{\top}$ se tiene $2+0=2$: sí, es $\mathbf{H}\,(2,\,0)^{\top}$. Para $(2,\,1,\,2)^{\top}$ se tiene $2+1=3\ne2$: no.
:::
:::

:::aufgabe Ejercicio 17 ★★ El alquiler mensual
<span class="anker" id="aufg-17"></span>

Un índice de alquileres estima el alquiler mensual de una vivienda con los pesos $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ en euros por metro cuadrado, por habitación y por kilómetro.

<ol class="al">

<li>

Calcula los alquileres estimados de las cuatro viviendas como $\mathbf{X}\mathbf{w}_{\mathrm M}$, una vez con la visión por filas y otra con la visión por columnas.

</li>

<li>

¿Cuántas multiplicaciones y sumas has necesitado? ¿Cuántas serían para $10\,000$ viviendas con $20$ características?

</li>

</ol>

:::loesung
(a) Visión por filas, para la vivienda 1: $12\cdot60+30\cdot2-8\cdot3=720+60-24=756$; del mismo modo, $502$, $1152$ y $914$ euros. Visión por columnas:

$$12\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+30\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-8\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}720\\480\\1080\\840\end{pmatrix}+\begin{pmatrix}60\\30\\120\\90\end{pmatrix}-\begin{pmatrix}24\\8\\48\\16\end{pmatrix}=\begin{pmatrix}756\\502\\1152\\914\end{pmatrix}.$$

(b) Cada una de las cuatro componentes necesita $3$ multiplicaciones y $2$ sumas; en total, $12+8=20$. Para $10\,000$ viviendas con $20$ características son $10\,000\cdot20=200\,000$ multiplicaciones y $10\,000\cdot19=190\,000$ sumas; en total, $390\,000\approx2mn$ con $m=10\,000$, $n=20$.
:::
:::
