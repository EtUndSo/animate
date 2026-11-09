---
title: Sistemas de ecuaciones lineales
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15211300
summary: Hasta ahora, la entrada x estaba dada y se buscaba la salida Ax .
tags: sistema de ecuaciones lineales, matriz de coeficientes, lado derecho, solución, matriz ampliada, eliminación gaussiana, forma escalonada, homogéneo
lang: es
---

<span class="anker" id="stufe-12"></span>

:::zweck
Hasta ahora, la entrada $\mathbf{x}$ estaba dada y se buscaba la salida $\mathbf{A}\mathbf{x}$. Esta sección plantea la pregunta inversa: ¿qué entrada da una salida prescrita? Eso es un sistema de ecuaciones lineales. La sección muestra cómo se resuelve y cuándo no tiene ninguna solución, tiene exactamente una o tiene infinitas.
:::

### Sistemas de ecuaciones en forma matricial

<span class="anker" id="stufe-12-1"></span>

Del colegio se conocen problemas como este: dos números $x_1$ y $x_2$ cumplen $2x_1+x_2=5$ y $x_1+x_2=3$; ¿cuáles son? Los lados izquierdos son las componentes de un producto matriz-vector. El problema pregunta, por tanto: ¿qué vector $\mathbf{x}$ lleva la matriz $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ a $(5,\,3)^{\top}$?

:::definition Definición 12.1 (Sistema de ecuaciones lineales)
<span class="anker" id="satz-12-1"></span>

Para una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ y un vector $\mathbf{y}\in\mathbb{R}^m$,

<span class="anker" id="gl-12-1"></span>
$$\mathbf{A}\mathbf{x}=\mathbf{y} \tag{12.1}$$

se llama un __sistema de ecuaciones lineales__ con $m$ ecuaciones y las $n$ incógnitas $x_1,\dots,x_n$. La matriz $\mathbf{A}$ se llama __matriz de coeficientes__; el vector $\mathbf{y}$, el __lado derecho__. Todo vector $\mathbf{x}\in\mathbb{R}^n$ que cumple [(12.1)](#gl-12-1) se llama una __solución__.
:::

Escrita en detalle, en la fila $i$ está la ecuación $a_{i1}x_1+\dots+a_{in}x_n=y_i$.

::::beispiel [Ejemplo numérico]
El sistema

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}$$

tiene la solución $\mathbf{x}=(2,\,1)^{\top}$: $2\cdot2+1=5$ y $2+1=3$. La matriz de coeficientes ya se conoce de la subsección [11.2](einheitsmatrix-und-inverse.html#stufe-11-2), con la inversa $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. Si se multiplica el sistema por ella por la izquierda, la solución aparece de inmediato: $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}=(5-3,\ -5+6)^{\top}=(2,\,1)^{\top}$.
::::

⁠**En resumen:** Un sistema de ecuaciones lineales $\mathbf{A}\mathbf{x}=\mathbf{y}$ pregunta qué entrada $\mathbf{x}$ da la salida $\mathbf{y}$.

### Imagen por filas e imagen por columnas

<span class="anker" id="stufe-12-2"></span>

Como en el producto matriz-vector, hay dos formas de leer un sistema de ecuaciones.

**Imagen por filas.** Cada ecuación por sí sola describe un conjunto de puntos. Con dos incógnitas, $2x_1+x_2=5$ es una recta en el plano, y lo mismo $x_1+x_2=3$. Una solución tiene que cumplir ambas ecuaciones, es decir, estar en ambas rectas: es su punto de intersección (fig. [38](#abb-38), izquierda). Con tres incógnitas, cada ecuación es un plano en el espacio.

**Imagen por columnas.** Según la visión por columnas [(7.3)](das-matrix-vektor-produkt.html#gl-7-3), $\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$. La ecuación pregunta, por tanto: ¿con qué coeficientes da la combinación lineal de las columnas el lado derecho? En el ejemplo: $x_1\,(2,\,1)^{\top}+x_2\,(1,\,1)^{\top}=(5,\,3)^{\top}$, que se resuelve con $x_1=2$ y $x_2=1$. Es exactamente lo que muestra la parte derecha de la fig. [30](das-matrix-vektor-produkt.html#abb-30).

:::abbildung ml/k1lgs 38
La imagen por filas de tres sistemas de ecuaciones con dos incógnitas. Cada ecuación es una recta; una solución está en todas las rectas. (a) Las rectas se cortan en un punto. (b) Las rectas son paralelas y no tienen ningún punto común. (c) Ambas ecuaciones describen la misma recta, y cada uno de sus puntos es una solución.
:::

La imagen por columnas responde de inmediato a la pregunta de cuándo hay alguna solución. Los vectores $\mathbf{A}\mathbf{x}$ forman el espacio columna (subsección [7.4](das-matrix-vektor-produkt.html#stufe-7-4)).

:::satz Teorema 12.2 (Existencia de solución)
<span class="anker" id="satz-12-2"></span>

El sistema $\mathbf{A}\mathbf{x}=\mathbf{y}$ tiene solución si y solo si $\mathbf{y}$ está en el espacio columna de $\mathbf{A}$.
:::

::::beispiel [Ejemplo numérico]
El sistema $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)\mathbf{x}=\mathbf{y}$ tiene solución para $\mathbf{y}=(3,\,6)^{\top}$, por ejemplo con $\mathbf{x}=(1,\,1)^{\top}$, pero para $\mathbf{y}=(1,\,1)^{\top}$ no: según la subsección [7.4](das-matrix-vektor-produkt.html#stufe-7-4), el espacio columna es solo la recta en la dirección $(1,\,2)^{\top}$.
::::

⁠**En resumen:** En la imagen por filas, una solución es un punto común de todas las ecuaciones; en la imagen por columnas, la elección de coeficientes con la que las columnas dan el lado derecho.

### La eliminación gaussiana

<span class="anker" id="stufe-12-3"></span>

Con dos incógnitas, la solución se encuentra a simple vista. Con tres o más hace falta un procedimiento que funcione siempre. La idea es la misma que en el colegio: se resta un múltiplo de una ecuación de otra, de modo que desaparezca una incógnita. Esto se repite hasta que la última ecuación solo contiene una incógnita.

Para ello se anotan solo los números: la matriz de coeficientes y, separado por una raya, el lado derecho. Esta tabla se llama __matriz ampliada__ $(\mathbf{A}\,|\,\mathbf{y})$.

:::definition Definición 12.3 (Eliminación gaussiana)
<span class="anker" id="satz-12-3"></span>

La __eliminación gaussiana__ transforma la matriz ampliada con tres operaciones de filas:

<ol>

<li>

sumar a una fila un múltiplo de otra fila;

</li>

<li>

intercambiar dos filas;

</li>

<li>

multiplicar una fila por un número distinto de cero.

</li>

</ol>

El objetivo es la __forma escalonada__: en cada fila, delante de la primera entrada distinta de cero hay al menos un cero más que en la fila de arriba. Después se determinan las incógnitas de abajo arriba (sustitución regresiva).
:::

:::satz Teorema 12.4 (Las operaciones de filas no cambian las soluciones)
<span class="anker" id="satz-12-4"></span>

Un sistema y el sistema obtenido de él mediante operaciones de filas tienen las mismas soluciones.
:::

:::beweis Operaciones de filas
Toda solución del sistema antiguo cumple también las ecuaciones nuevas, pues estas son sumas y múltiplos de las antiguas. Pero cada una de las tres operaciones también puede deshacerse: restar de nuevo el múltiplo, volver a intercambiar las filas, dividir por el número. Así que, a la inversa, toda solución del sistema nuevo cumple también el antiguo.
:::

::::beispiel [Ejemplo numérico]
El sistema

$$\begin{aligned} x_1+2x_2+x_3&=8\\ 2x_1+x_2+x_3&=7\\ x_1+x_2+2x_3&=9 \end{aligned} \qquad\text{tiene la matriz ampliada}\qquad \left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right).$$

Si se resta la primera fila dos veces de la segunda y una vez de la tercera, $x_1$ desaparece de ambas. Si después se intercambian la nueva segunda y la nueva tercera fila y se resta la nueva segunda tres veces de la tercera, desaparece también $x_2$ de la última fila:

$$\left(\begin{array}{ccc|c}1&2&1&8\\0&-3&-1&-9\\0&-1&1&1\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&-3&-1&-9\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&0&-4&-12\end{array}\right).$$

De abajo arriba: $-4x_3=-12$, así que $x_3=3$; luego $-x_2+3=1$, así que $x_2=2$; luego $x_1+4+3=8$, así que $x_1=1$. La solución es $\mathbf{x}=(1,\,2,\,3)^{\top}$, y sustituirla en las tres ecuaciones la confirma.
::::

⁠**En resumen:** La eliminación gaussiana elimina las incógnitas paso a paso mediante operaciones de filas que no cambian las soluciones y después sustituye de abajo arriba.

:::hintergrund Por qué para resolver no se calcula la inversa
Si $\mathbf{A}$ es invertible, la solución es $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}$. Esto es útil para razonar, pero desfavorable como método de cálculo. La eliminación gaussiana necesita, para un sistema con $n$ ecuaciones y $n$ incógnitas, unas $\tfrac23n^3$ operaciones aritméticas básicas; calcular la inversa cuesta unas $2n^3$, tres veces más, y después hay que añadir todavía el producto $\mathbf{A}^{-1}\mathbf{y}$. Además, un ordenador calcula con un número finito de cifras. La inversa solo puede representarse entonces redondeada, y la eliminación directa da por lo general resultados más exactos. Por eso, la inversa es sobre todo una herramienta para pensar y deducir, no para calcular.
:::

### Ninguna, una o infinitas soluciones

<span class="anker" id="stufe-12-4"></span>

Dos rectas en el plano se cortan en un punto, son paralelas o coinciden (fig. [38](#abb-38)). Nunca hay exactamente dos puntos de intersección. Lo mismo vale para todo sistema de ecuaciones lineales, sea cual sea su tamaño.

:::satz Teorema 12.5 (Número de soluciones)
<span class="anker" id="satz-12-5"></span>

Un sistema de ecuaciones lineales o bien no tiene ninguna solución, o bien tiene exactamente una, o bien tiene infinitas.
:::

:::beweis Número de soluciones
Basta demostrar: si el sistema tiene dos soluciones distintas $\mathbf{x}\ne\mathbf{x}'$, tiene infinitas. Para todo número $t$ se tiene

$$\mathbf{A}\bigl(\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})\bigr)=\mathbf{A}\mathbf{x}+t\,(\mathbf{A}\mathbf{x}'-\mathbf{A}\mathbf{x})=\mathbf{y}+t\,(\mathbf{y}-\mathbf{y})=\mathbf{y} ,$$

así que cada punto $\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})$ de la recta que pasa por $\mathbf{x}$ y $\mathbf{x}'$ es una solución, y valores distintos de $t$ dan puntos distintos.
:::

El sistema $\mathbf{A}\mathbf{x}=\mathbf{0}$, con lado derecho nulo, se llama __homogéneo__. Siempre tiene la solución $\mathbf{x}=\mathbf{0}$. Si se conoce una solución cualquiera $\mathbf{x}_{\mathrm s}$ del sistema $\mathbf{A}\mathbf{x}=\mathbf{y}$, se obtienen todas las demás sumándole las soluciones del sistema homogéneo: $\mathbf{A}\mathbf{x}=\mathbf{y}$ se cumple si y solo si $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm s})=\mathbf{y}-\mathbf{y}=\mathbf{0}$.

::::beispiel [Ejemplo numérico]
Los tres sistemas de la fig. [38](#abb-38):

<ol class="al">

<li>

$2x_1+x_2=5$, $x_1+x_2=3$: exactamente una solución, $(2,\,1)^{\top}$.

</li>

<li>

$x_1+x_2=3$, $x_1+x_2=1$: ninguna solución, pues la misma suma no puede valer a la vez $3$ y $1$.

</li>

<li>

$x_1+x_2=3$, $2x_1+2x_2=6$: la segunda ecuación es el doble de la primera. Una solución es $\mathbf{x}_{\mathrm s}=(3,\,0)^{\top}$, y el sistema homogéneo $x_1+x_2=0$ lo resuelven todos los múltiplos de $(-1,\,1)^{\top}$. Todas las soluciones son, por tanto, $\mathbf{x}=(3,\,0)^{\top}+t\,(-1,\,1)^{\top}$ con $t$ arbitrario.

</li>

</ol>
::::

⁠**En resumen:** Un sistema de ecuaciones lineales no tiene ninguna solución, tiene exactamente una o tiene infinitas; todas las soluciones son una solución más las soluciones del sistema homogéneo.

### Más ecuaciones que incógnitas

<span class="anker" id="stufe-12-5"></span>

Con datos, la situación suele estar desequilibrada. Supongamos que se buscan pesos $w_1$ para la superficie y $w_2$ para las habitaciones de modo que la suma ponderada acierte exactamente el precio real en tres viviendas. Son tres ecuaciones para dos incógnitas.

:::definition Definición 12.6 (Sobredeterminado, infradeterminado)
<span class="anker" id="satz-12-6"></span>

Un sistema de ecuaciones lineales con más ecuaciones que incógnitas ($m>n$) se llama __sobredeterminado__; uno con menos ecuaciones que incógnitas ($m<n$), __infradeterminado__.
:::

Un sistema sobredeterminado no suele tener solución: ya dos ecuaciones fijan dos incógnitas, y la tercera ecuación tendría que cumplirse también por casualidad. En la imagen por columnas: el espacio columna de $n$ columnas en $\mathbb{R}^m$ es, para $n<m$, solo una pequeña parte de $\mathbb{R}^m$, y el lado derecho casi nunca está en él. Un sistema infradeterminado, en cambio, si es que tiene solución, tiene infinitas: en la forma escalonada queda al menos una incógnita sin pivote propio, y puede elegirse libremente.

::::beispiel [Ejemplo numérico]
Para las viviendas 1 a 3, con los precios de $200$, $130$ y $290$ mil euros, el sistema es

$$60\,w_1+2\,w_2=200,\qquad 40\,w_1+w_2=130,\qquad 90\,w_1+4\,w_2=290 .$$

De las dos primeras ecuaciones se sigue $w_1=3$ y $w_2=10$: si se resta la segunda dos veces de la primera, queda $-20\,w_1=-60$. Pero, sustituido en la tercera, esto da $270+40=310\ne290$. El sistema no tiene solución. Ningún par de pesos acierta exactamente los tres precios. Qué se busca en su lugar en un caso así es una cuestión aparte.
::::

⁠**En resumen:** Un sistema sobredeterminado tiene más ecuaciones que incógnitas y no suele tener solución; uno infradeterminado tiene menos y, si tiene solución, tiene infinitas.

:::aufgabe Ejercicio 28 ★★ La eliminación gaussiana
<span class="anker" id="aufg-28"></span>

Resuelve con la eliminación gaussiana y haz la comprobación:

$$x_1+x_2+x_3=6,\qquad 2x_1+3x_2+x_3=11,\qquad x_1-x_2+2x_3=5 .$$

:::loesung
La matriz ampliada es $\Bigl(\begin{smallmatrix}1&1&1&|&6\\2&3&1&|&11\\1&-1&2&|&5\end{smallmatrix}\Bigr)$. Si se resta la primera fila dos veces de la segunda y una vez de la tercera, se obtienen las filas $(0,\,1,\,-1\,|\,-1)$ y $(0,\,-2,\,1\,|\,-1)$. Si después se suma dos veces la nueva segunda fila a la tercera, esta pasa a ser $(0,\,0,\,-1\,|\,-3)$. La forma escalonada es

$$x_1+x_2+x_3=6,\qquad x_2-x_3=-1,\qquad -x_3=-3 .$$

De abajo arriba: $x_3=3$, $x_2=-1+3=2$, $x_1=6-2-3=1$. Comprobación: $1+2+3=6$, $2+6+3=11$, $1-2+6=5$. La solución es $\mathbf{x}=(1,\,2,\,3)^{\top}$.
:::
:::

:::aufgabe Ejercicio 29 ★★ ¿Cuántas soluciones?
<span class="anker" id="aufg-29"></span>

Determina para cada sistema el conjunto de soluciones y dibuja la imagen por filas:

<ol class="al">

<li>

$x_1+2x_2=3$, $2x_1+4x_2=6$;

</li>

<li>

$x_1+2x_2=3$, $2x_1+4x_2=5$;

</li>

<li>

$x_1+2x_2=3$, $x_1-x_2=0$.

</li>

</ol>

:::loesung
(a) La segunda ecuación es el doble de la primera; ambas describen la misma recta. Infinitas soluciones: con $x_2=t$ se tiene $x_1=3-2t$, es decir, $\mathbf{x}=(3,\,0)^{\top}+t\,(-2,\,1)^{\top}$.

(b) Si se duplica la primera ecuación, se obtiene $2x_1+4x_2=6$, en contradicción con $2x_1+4x_2=5$. Las rectas son paralelas; no hay ninguna solución.

(c) De la segunda ecuación se obtiene $x_1=x_2$, y sustituyendo en la primera, $3x_2=3$. Exactamente una solución: $\mathbf{x}=(1,\,1)^{\top}$, el punto de intersección de dos rectas no paralelas.
:::
:::

:::aufgabe Ejercicio 30 ★★ Pesos que encajan
<span class="anker" id="aufg-30"></span>

Añade al sistema sobredeterminado de la subsección [12.5](#stufe-12-5) la vivienda 4, con el precio de $240$ mil euros.

<ol class="al">

<li>

¿Cuáles de las cuatro viviendas se aciertan exactamente con $w_1=3$, $w_2=10$?

</li>

<li>

Escribe el sistema con cuatro ecuaciones como $\mathbf{A}\mathbf{w}=\mathbf{y}$. ¿Qué tamaños tienen $\mathbf{A}$, $\mathbf{w}$ y $\mathbf{y}$? ¿Qué significa «ninguna solución» en la imagen por columnas?

</li>

</ol>

:::loesung
(a) Con $w_1=3$, $w_2=10$: vivienda 1: $180+20=200$ (acertada); vivienda 2: $120+10=130$ (acertada); vivienda 3: $270+40=310$ en lugar de $290$ (no acertada); vivienda 4: $210+30=240$ (acertada). Tres de los cuatro precios coinciden, pero no todos.

(b) $\mathbf{A}=\Biggl(\begin{smallmatrix}60&2\\40&1\\90&4\\70&3\end{smallmatrix}\Biggr)\in\mathbb{R}^{4\times2}$, $\mathbf{w}\in\mathbb{R}^2$, $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}\in\mathbb{R}^4$. El espacio columna de $\mathbf{A}$ consta de todas las combinaciones $w_1\mathbf{a}_1+w_2\mathbf{a}_2$ de la columna de la superficie y la columna de las habitaciones; es un plano que pasa por el origen en $\mathbb{R}^4$. «Ninguna solución» significa: el vector de precios $\mathbf{y}$ no está en este plano. Ninguna elección de los dos pesos produce exactamente estos cuatro precios.
:::
:::
