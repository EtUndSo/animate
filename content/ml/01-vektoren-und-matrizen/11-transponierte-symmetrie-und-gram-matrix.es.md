---
title: Traspuesta, simetría y matriz de Gram
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Capítulo 1: Vectores y matrices
nachschlagen: ja
order: 15211100
summary: Si en una matriz se intercambian filas y columnas, se obtiene su traspuesta.
tags: traspuesta, simétrica, matriz de Gram
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Si en una matriz se intercambian filas y columnas, se obtiene su traspuesta. Con ella pueden reunirse en una única matriz todos los productos escalares de un conjunto de datos: las similitudes de todos los ejemplos entre sí y las relaciones de todas las características entre sí.
:::

### La traspuesta

<span class="anker" id="stufe-10-1"></span>

El signo $^{\top}$ ya se conoce de la subsección [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3): convierte una columna en una fila. Para las matrices significa lo mismo, aplicado a cada columna: la columna $j$ pasa a ser la fila $j$. La matriz se refleja así respecto de su diagonal.

:::definition Definición 10.1 (Traspuesta)
<span class="anker" id="satz-10-1"></span>

La __traspuesta__ de una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ es la matriz $\mathbf{A}^{\top}\in\mathbb{R}^{n\times m}$ con

<span class="anker" id="gl-10-1"></span>
$$(\mathbf{A}^{\top})_{ij}=a_{ji} . \tag{10.1}$$
:::

Un vector $\mathbf{x}\in\mathbb{R}^d$ es una matriz $d\times1$; su traspuesta $\mathbf{x}^{\top}$, la matriz $1\times d$ con las mismas entradas. Con ello, la notación $\mathbf{u}^{\top}\mathbf{v}$ de la subsección [2.1](das-skalarprodukt.html#stufe-2-1) es ahora literalmente un producto de matrices: una matriz $1\times d$ por una matriz $d\times1$; el resultado es una matriz $1\times1$, es decir, un número.

:::satz Teorema 10.2 (Reglas de cálculo de la traspuesta)
<span class="anker" id="satz-10-2"></span>

Para matrices de tamaños adecuados y escalares $c$ se cumple

$$(\mathbf{A}^{\top})^{\top}=\mathbf{A},\qquad(\mathbf{A}+\mathbf{B})^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top},\qquad(c\,\mathbf{A})^{\top}=c\,\mathbf{A}^{\top},\qquad(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top} .$$
:::

:::herleitung La traspuesta de un producto
Para $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{B}\in\mathbb{R}^{n\times k}$, según [(10.1)](#gl-10-1) y [(9.1)](das-matrixprodukt.html#gl-9-1), se tiene

$$\bigl((\mathbf{A}\mathbf{B})^{\top}\bigr)_{li}=(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^na_{ij}\,b_{jl}=\sum_{j=1}^n(\mathbf{B}^{\top})_{lj}\,(\mathbf{A}^{\top})_{ji}=(\mathbf{B}^{\top}\mathbf{A}^{\top})_{li} .$$

Las tres primeras reglas se siguen directamente de la definición.
:::

::::beispiel [Ejemplo numérico]
$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^{\top}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$

Para $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ y $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ se tiene $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, así que $(\mathbf{C}\mathbf{D})^{\top}=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$. Lo mismo da $\mathbf{D}^{\top}\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$, mientras que $\mathbf{C}^{\top}\mathbf{D}^{\top}=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$ es otra cosa.
::::

⁠**En resumen:** Trasponer intercambia filas y columnas; en el producto, el orden se invierte: $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$.

:::hintergrund Por qué el orden se invierte al trasponer un producto
En el producto $\mathbf{A}\mathbf{B}$, las filas de $\mathbf{A}$ se encuentran con las columnas de $\mathbf{B}$. Tras trasponer, las filas de $\mathbf{A}$ son las columnas de $\mathbf{A}^{\top}$, y las columnas de $\mathbf{B}$ son las filas de $\mathbf{B}^{\top}$. Para que de nuevo las filas se encuentren con las columnas, $\mathbf{B}^{\top}$ tiene que estar a la izquierda. También los tamaños lo muestran: $(\mathbf{A}\mathbf{B})^{\top}$ tiene el tamaño $k\times m$, y $\mathbf{B}^{\top}\mathbf{A}^{\top}$ es $(k\times n)\cdot(n\times m)$, es decir, encaja. La expresión $\mathbf{A}^{\top}\mathbf{B}^{\top}$ sería $(n\times m)\cdot(k\times n)$ y solo está definida si casualmente $m=k$. Un caso particular de la regla es $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$: un número es su propia traspuesta, así que $\mathbf{u}^{\top}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{u}$.
:::

### Matrices simétricas

<span class="anker" id="stufe-10-2"></span>

Algunas tablas son iguales a su reflejo respecto de la diagonal. Una tabla de distancias entre ciudades es una de ellas: el camino de Múnich a Colonia es tan largo como el de Colonia a Múnich.

:::definition Definición 10.3 (Matriz simétrica)
<span class="anker" id="satz-10-3"></span>

Una matriz cuadrada $\mathbf{A}$ se llama __simétrica__ si $\mathbf{A}^{\top}=\mathbf{A}$, es decir, $a_{ij}=a_{ji}$ para todos los $i,j$.
:::

Toda matriz diagonal es simétrica. Una fuente importante de matrices simétricas son los productos de una matriz por su propia traspuesta: para toda matriz $\mathbf{A}$ se tiene

<span class="anker" id="gl-10-2"></span>
$$(\mathbf{A}^{\top}\mathbf{A})^{\top}=\mathbf{A}^{\top}(\mathbf{A}^{\top})^{\top}=\mathbf{A}^{\top}\mathbf{A} , \tag{10.2}$$

así que $\mathbf{A}^{\top}\mathbf{A}$ es simétrica, y también $\mathbf{A}\mathbf{A}^{\top}$.

::::beispiel [Ejemplo numérico]
$\bigl(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr)$ es simétrica; la rotación $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, no. Para $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ se tiene

$$\mathbf{C}^{\top}\mathbf{C}=\begin{pmatrix}1&3\\2&4\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}10&14\\14&20\end{pmatrix},$$

que es simétrica, como exige [(10.2)](#gl-10-2).
::::

⁠**En resumen:** Una matriz simétrica es igual a su traspuesta; $\mathbf{A}^{\top}\mathbf{A}$ y $\mathbf{A}\mathbf{A}^{\top}$ son siempre simétricas.

:::hintergrund Productos escalares con pesos
En el producto escalar $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$, cada posición cuenta lo mismo. Si se quiere que las posiciones cuenten de forma distinta, se toman pesos positivos $d_1,\dots,d_n$ y se forma $\sum_jd_j\,u_jv_j$. Con la matriz diagonal $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$, esto es $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$, pues $\mathbf{D}\mathbf{v}=(d_1v_1,\dots,d_nv_n)^{\top}$.

Este número tiene las mismas reglas de cálculo que el producto escalar ordinario. Es lineal en cada uno de los dos vectores, y $\mathbf{u}^{\top}\mathbf{D}\mathbf{u}=\sum_jd_ju_j^2$ es positivo para todo $\mathbf{u}\ne\mathbf{0}$. Es simétrico porque $\mathbf{D}$ es simétrica: un número es su propia traspuesta y, con la regla de la traspuesta de un producto aplicada dos veces, $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{D}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{D}^{\top}\mathbf{u}=\mathbf{v}^{\top}\mathbf{D}\mathbf{u}$. Como la demostración de la desigualdad de Cauchy-Schwarz solo ha usado estas reglas, con $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ pueden medirse igualmente longitudes, distancias y ángulos. Solo que salen distintos. Por ejemplo, $(1,\,1)^{\top}$ y $(-1,\,1)^{\top}$ son ortogonales en el sentido ordinario, pero con $\mathbf{D}=\operatorname{diag}(2,\,1)$ no lo son: $(1,\,1)\,\mathbf{D}\,(-1,\,1)^{\top}=2\cdot1\cdot(-1)+1\cdot1\cdot1=-1$.

La estandarización de la subsección [4.5](abstande-und-einheiten.html#stufe-4-5) es exactamente una ponderación de este tipo. La distancia entre dos ejemplos estandarizados es $\sqrt{(\mathbf{x}_a-\mathbf{x}_b)^{\top}\mathbf{D}\,(\mathbf{x}_a-\mathbf{x}_b)}$ con $\mathbf{D}=\operatorname{diag}(1/s_1^2,\dots,1/s_d^2)$. A la inversa, toda ponderación así actúa como un cambio de unidades: si se multiplica la característica $j$ por $\sqrt{d_j}$, el producto escalar ordinario de los vectores convertidos es $\sum_j(\sqrt{d_j}\,u_j)(\sqrt{d_j}\,v_j)=\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$. La elección de las unidades y la elección de los pesos en $\mathbf{D}$ son, por tanto, la misma decisión.
:::

### La matriz de Gram de los ejemplos

<span class="anker" id="stufe-10-3"></span>

¿Cuánto se parece cada ejemplo de un conjunto de datos a cada uno de los demás? Se pueden escribir todos los productos escalares por parejas en una tabla: la fila $i$, columna $k$, contiene $\mathbf{x}_i^{\top}\mathbf{x}_k$. Esta tabla es un único producto de matrices.

:::definition Definición 10.4 (Matriz de Gram)
<span class="anker" id="satz-10-4"></span>

La __matriz de Gram__ de una lista de vectores $\mathbf{v}_1,\dots,\mathbf{v}_k$ es la matriz $k\times k$ de los productos escalares por parejas, con la entrada $\mathbf{v}_i^{\top}\mathbf{v}_l$ en la fila $i$ y la columna $l$.
:::

Para los ejemplos de un conjunto de datos, es la matriz $\mathbf{X}\mathbf{X}^{\top}\in\mathbb{R}^{N\times N}$. En efecto, su entrada $(i,k)$ es la fila $i$ de $\mathbf{X}$ por la columna $k$ de $\mathbf{X}^{\top}$, es decir, $\mathbf{x}_i^{\top}\mathbf{x}_k$:

<span class="anker" id="gl-10-3"></span>
$$(\mathbf{X}\mathbf{X}^{\top})_{ik}=\mathbf{x}_i^{\top}\mathbf{x}_k . \tag{10.3}$$

Es simétrica, en su diagonal están los cuadrados de las longitudes $\lVert\mathbf{x}_i\rVert^2$, y según [(4.1)](abstande-und-einheiten.html#gl-4-1) pueden leerse en ella todas las distancias:

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{x}_i-\mathbf{x}_k\rVert^2=(\mathbf{X}\mathbf{X}^{\top})_{ii}+(\mathbf{X}\mathbf{X}^{\top})_{kk}-2\,(\mathbf{X}\mathbf{X}^{\top})_{ik} . \tag{10.4}$$

Si se divide la entrada $(i,k)$ por $\sqrt{(\mathbf{X}\mathbf{X}^{\top})_{ii}\,(\mathbf{X}\mathbf{X}^{\top})_{kk}}$, se obtiene la similitud coseno de $\mathbf{x}_i$ y $\mathbf{x}_k$.

::::beispiel [Ejemplo numérico]
Para los tres textos de la subsección [5.4](winkel-und-ahnlichkeit.html#stufe-5-4) se tiene

$$\mathbf{X}=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix},\qquad \mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}13&26&2\\26&52&4\\2&4&10\end{pmatrix}.$$

La distancia entre el texto 1 y el texto 3 es, según [(10.4)](#gl-10-4), $\sqrt{13+10-2\cdot2}=\sqrt{19}$, como se calculó antes. La similitud coseno de los textos 1 y 2 es $26/\sqrt{13\cdot52}=1$.
::::

⁠**En resumen:** La matriz de Gram $\mathbf{X}\mathbf{X}^{\top}$ es la tabla de todos los productos escalares por parejas de los ejemplos; de ella se deducen todas las longitudes, distancias y ángulos.

:::hintergrund La matriz de Gram contiene toda la geometría del conjunto de datos
Las longitudes, distancias y ángulos entre los ejemplos solo dependen de los productos escalares, no de las coordenadas individuales. Si, por ejemplo, se gira todo el conjunto de datos alrededor del origen, cambian todas las coordenadas, pero ningún producto escalar, y la matriz de Gram sigue siendo la misma. Dos conjuntos de datos con la misma matriz de Gram tienen, por tanto, el mismo aspecto geométrico. Quien solo quiere saber qué ejemplos se parecen entre sí no necesita, por eso, la matriz de datos misma, sino solo su matriz de Gram.
:::

### La matriz de Gram de las características

<span class="anker" id="stufe-10-4"></span>

Si se invierten los papeles, se obtiene una tabla sobre las características: ¿en qué medida van de la mano dos características a lo largo de todos los ejemplos? Las columnas de dos características son vectores de $\mathbb{R}^N$, y su producto escalar lo mide. Esta matriz de Gram de las columnas es $\mathbf{X}^{\top}\mathbf{X}\in\mathbb{R}^{d\times d}$:

<span class="anker" id="gl-10-5"></span>
$$(\mathbf{X}^{\top}\mathbf{X})_{jl}=\sum_{i=1}^Nx_{ij}\,x_{il} . \tag{10.5}$$

La entrada $(j,l)$ es el producto escalar de las columnas de las características $j$ y $l$; en la diagonal está la suma de cuadrados de una característica.

:::satz Teorema 10.5 (La matriz de Gram como suma sobre los ejemplos)
<span class="anker" id="satz-10-5"></span>

<span class="anker" id="gl-10-6"></span>
$$\mathbf{X}^{\top}\mathbf{X}=\sum_{i=1}^N\mathbf{x}_i\,\mathbf{x}_i^{\top} . \tag{10.6}$$

Cada ejemplo aporta su propio producto exterior.
:::

La entrada $(j,l)$ del lado derecho es $\sum_ix_{ij}\,x_{il}$, la misma que en [(10.5)](#gl-10-5). Si se añade un ejemplo nuevo, $\mathbf{X}^{\top}\mathbf{X}$ solo cambia, por tanto, en una capa más, $\mathbf{x}_{N+1}\mathbf{x}_{N+1}^{\top}$; no hay que recalcularlo todo.

::::beispiel [Ejemplo numérico]
Para los textos se tiene

$$\mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

Las entradas de la primera fila son los productos escalares de la columna «gol» con las tres columnas de las características (fig. [37](#abb-37)).

:::abbildung ml/k1rgrammerk 37
La primera fila de la matriz de Gram de las características: la columna «gol» $(3,\,6,\,0)^{\top}$ por sí misma, por la columna «balón» $(2,\,4,\,1)^{\top}$ y por la columna «elección» $(0,\,0,\,3)^{\top}$.
:::

El $0$ en la posición $(1,3)$ dice: las palabras «gol» y «elección» no aparecen juntas en ningún texto. Como suma de los tres productos exteriores:

$$\begin{pmatrix}9&6&0\\6&4&0\\0&0&0\end{pmatrix}+\begin{pmatrix}36&24&0\\24&16&0\\0&0&0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&1&3\\0&3&9\end{pmatrix}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$
::::

⁠**En resumen:** $\mathbf{X}^{\top}\mathbf{X}$ es la matriz de Gram de las columnas de las características; es la suma de los productos exteriores $\mathbf{x}_i\mathbf{x}_i^{\top}$ de todos los ejemplos.

:::aufgabe Ejercicio 24 ★ Trasponer
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Indica $\mathbf{B}^{\top}$ para $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ y calcula $\mathbf{B}^{\top}\mathbf{B}$ y $\mathbf{B}\mathbf{B}^{\top}$. ¿Qué tamaños tienen y son simétricas?

</li>

<li>

Demuestra con las reglas de cálculo: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{B}^{\top}=\Bigl(\begin{smallmatrix}1&2\\0&1\\2&0\end{smallmatrix}\Bigr)$. Entonces

$$\mathbf{B}^{\top}\mathbf{B}=\begin{pmatrix}5&2&2\\2&1&0\\2&0&4\end{pmatrix}\in\mathbb{R}^{3\times3},\qquad \mathbf{B}\mathbf{B}^{\top}=\begin{pmatrix}5&2\\2&5\end{pmatrix}\in\mathbb{R}^{2\times2}.$$

Ambas son simétricas, como exige [(10.2)](#gl-10-2). La entrada $(1,1)$ de $\mathbf{B}^{\top}\mathbf{B}$ es $1^2+2^2=5$, la suma de cuadrados de la primera columna; la entrada $(1,2)$ de $\mathbf{B}\mathbf{B}^{\top}$ es $1\cdot2+0\cdot1+2\cdot0=2$, el producto escalar de las dos filas.

(b) Dos veces la regla del producto: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\bigl((\mathbf{A}\mathbf{B})\mathbf{C}\bigr)^{\top}=\mathbf{C}^{\top}(\mathbf{A}\mathbf{B})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.
:::
:::

:::aufgabe Ejercicio 25 ★★ Matrices de Gram de un pequeño conjunto de datos
<span class="anker" id="aufg-25"></span>

Un conjunto de datos tiene tres ejemplos con dos características: $\mathbf{x}_1=(1,\,0)^{\top}$, $\mathbf{x}_2=(2,\,1)^{\top}$, $\mathbf{x}_3=(0,\,3)^{\top}$.

<ol class="al">

<li>

Construye $\mathbf{X}$ y calcula $\mathbf{X}\mathbf{X}^{\top}$ y $\mathbf{X}^{\top}\mathbf{X}$.

</li>

<li>

Lee en $\mathbf{X}\mathbf{X}^{\top}$ la distancia entre $\mathbf{x}_2$ y $\mathbf{x}_3$ y compruébala directamente.

</li>

<li>

Confirma [(10.6)](#gl-10-6) sumando los tres productos exteriores $\mathbf{x}_i\mathbf{x}_i^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{X}=\Bigl(\begin{smallmatrix}1&0\\2&1\\0&3\end{smallmatrix}\Bigr)$,

$$\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}1&2&0\\2&5&3\\0&3&9\end{pmatrix},\qquad \mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}5&2\\2&10\end{pmatrix}.$$

(b) Según [(10.4)](#gl-10-4), $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert^2=5+9-2\cdot3=8$; la distancia es, por tanto, $\sqrt8\approx2{,}83$. Directamente: $\mathbf{x}_2-\mathbf{x}_3=(2,\,-2)^{\top}$, con el cuadrado de la longitud $4+4=8$.

(c) $\mathbf{x}_1\mathbf{x}_1^{\top}=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$, $\mathbf{x}_2\mathbf{x}_2^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1\end{smallmatrix}\bigr)$, $\mathbf{x}_3\mathbf{x}_3^{\top}=\bigl(\begin{smallmatrix}0&0\\0&9\end{smallmatrix}\bigr)$; la suma es $\bigl(\begin{smallmatrix}5&2\\2&10\end{smallmatrix}\bigr)=\mathbf{X}^{\top}\mathbf{X}$.
:::
:::
