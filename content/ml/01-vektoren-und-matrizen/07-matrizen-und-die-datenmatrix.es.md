---
title: Matrices y la matriz de datos
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Capítulo 1: Vectores y matrices
nachschlagen: ja
order: 15210700
summary: Un conjunto de datos consta de muchos vectores de la misma longitud.
tags: matriz, entrada, tamaño, cuadrada, diagonal, matriz diagonal, matriz nula, matriz de datos
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Un conjunto de datos consta de muchos vectores de la misma longitud. Esta sección los reúne en una única tabla de números, una matriz, y establece cómo se escribe y se calcula con matrices.
:::

### Matrices

<span class="anker" id="stufe-6-1"></span>

La tabla de las viviendas es más que cuatro vectores sueltos: es un objeto con el que se quiere calcular como un todo. También una imagen en escala de grises es una tabla, en concreto de luminosidades, dispuestas en filas y columnas. Un esquema rectangular de números así se llama matriz.

:::definition Definición 6.1 (Matriz)
<span class="anker" id="satz-6-1"></span>

Una __matriz__ $\mathbf{A}\in\mathbb{R}^{m\times n}$ es una disposición rectangular de $m\cdot n$ números reales en $m$ filas y $n$ columnas:

$$\mathbf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}.$$

El número $a_{ij}$ de la fila $i$ y la columna $j$ se llama __entrada__ de la matriz. El par $m\times n$ se llama el __tamaño__ de la matriz.
:::

Las matrices se escriben en negrita y en mayúscula; sus entradas, con la letra minúscula y dos índices: primero la fila, después la columna. La $j$-ésima columna de $\mathbf{A}$ es un vector con $m$ componentes; se llama $\mathbf{a}_j$. La matriz se escribe entonces también como sucesión de sus columnas, $\mathbf{A}=\begin{pmatrix}\mathbf{a}_1&\cdots&\mathbf{a}_n\end{pmatrix}$. Un vector con $d$ componentes es una matriz de tamaño $d\times1$; una fila con $d$ números, una matriz de tamaño $1\times d$.

Dos matrices son iguales si tienen el mismo tamaño y la misma entrada en cada posición. Las matrices del mismo tamaño se suman y se multiplican por un número entrada por entrada, exactamente como los vectores: $(\mathbf{A}+\mathbf{B})_{ij}=a_{ij}+b_{ij}$ y $(c\,\mathbf{A})_{ij}=c\,a_{ij}$.

::::beispiel [Ejemplo numérico]
La matriz

$$\mathbf{A}=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\in\mathbb{R}^{2\times3}$$

tiene el tamaño $2\times3$, las entradas $a_{12}=2$ y $a_{21}=4$ y la segunda columna $\mathbf{a}_2=(2,\,5)^{\top}$. Una imagen en escala de grises de $3\times3$ píxeles que muestra una cruz clara sobre fondo oscuro es la matriz con las filas $(0,1,0)$, $(1,1,1)$ y $(0,1,0)$. Además,

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad 2\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}2&4\\6&8\end{pmatrix}.$$
::::

⁠**En resumen:** Una matriz es una tabla rectangular de números con $m$ filas y $n$ columnas; la entrada $a_{ij}$ está en la fila $i$ y la columna $j$.

:::hintergrund Una imagen como matriz y como vector
Si se lee una imagen fila por fila y se colocan las filas una tras otra, la matriz se convierte en un vector largo: la cruz de $3\times3$ da el vector $(0,1,0,1,1,1,0,1,0)^{\top}\in\mathbb{R}^9$; una imagen de $28\times28$, un vector de $\mathbb{R}^{784}$. Los números siguen siendo los mismos, pero en la notación se pierde una información: qué píxeles son vecinos. El píxel situado justo debajo de otro está $28$ posiciones más atrás en el vector largo. Para los cálculos que ponderan cada característica por separado, esto no importa. Para los cálculos que quieren aprovechar las vecindades, la forma matricial es la más natural.
:::

### Matrices cuadradas y matrices diagonales

<span class="anker" id="stufe-6-2"></span>

Algunas matrices aparecen tan a menudo que tienen nombres propios. En las tres, la forma de la tabla es especialmente sencilla.

Una matriz con el mismo número de filas que de columnas se llama __cuadrada__. Las entradas $a_{11},a_{22},\dots,a_{nn}$ de una matriz cuadrada forman su __diagonal__, que va de la esquina superior izquierda a la inferior derecha.

:::definition Definición 6.2 (Matriz diagonal, matriz nula)
<span class="anker" id="satz-6-2"></span>

Una matriz cuadrada cuyas entradas fuera de la diagonal son todas cero se llama __matriz diagonal__. Para un vector $\mathbf{v}\in\mathbb{R}^n$, $\operatorname{diag}(\mathbf{v})$ es la matriz diagonal con las entradas diagonales $v_1,\dots,v_n$.

La matriz cuyas entradas son todas cero se llama __matriz nula__ y se escribe $\mathbf 0$.
:::

::::beispiel [Ejemplo numérico]
$$\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)=\begin{pmatrix}2&0\\0&0{,}5\end{pmatrix},\qquad \operatorname{diag}\bigl((1,\,0,\,3)^{\top}\bigr)=\begin{pmatrix}1&0&0\\0&0&0\\0&0&3\end{pmatrix}.$$

La segunda matriz tiene una entrada diagonal nula y, aun así, es una matriz diagonal; solo se exige que fuera de la diagonal haya ceros. En lugar de $\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)$ se escribe abreviadamente $\operatorname{diag}(2;\,0{,}5)$.
::::

⁠**En resumen:** Una matriz cuadrada tiene tantas filas como columnas; una matriz diagonal solo tiene entradas distintas de cero en la diagonal.

### La matriz de datos

<span class="anker" id="stufe-6-3"></span>

La tabla de las viviendas de la subsección [1.2](vektoren-daten-als-zahlenlisten.html#stufe-1-2) es una matriz: cuatro filas, una por vivienda, y tres columnas, una por característica. Esta disposición, un ejemplo por fila, es la forma estándar de un conjunto de datos (fig. [27](#abb-27)).

:::abbildung ml/k1datenmatrix 27
La matriz de datos $\mathbf{X}$ del conjunto de datos de viviendas. Cada fila es un ejemplo, el vector $\mathbf{x}_i^{\top}$ escrito como fila (azul: vivienda 2). Cada columna es la columna de una característica a lo largo de todos los ejemplos (naranja: las superficies). La entrada $x_{21}=40$ está en ambas.
:::

:::definition Definición 6.3 (Matriz de datos)
<span class="anker" id="satz-6-3"></span>

Para un conjunto de datos con los ejemplos $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^d$, la __matriz de datos__ es la matriz $\mathbf{X}\in\mathbb{R}^{N\times d}$ cuya fila $i$ es el ejemplo $\mathbf{x}_i$, escrito como fila:

<span class="anker" id="gl-6-1"></span>
$$\mathbf{X}=\begin{pmatrix}\mathbf{x}_1^{\top}\\\mathbf{x}_2^{\top}\\\vdots\\\mathbf{x}_N^{\top}\end{pmatrix}=\begin{pmatrix}x_{11}&\cdots&x_{1d}\\\vdots&&\vdots\\x_{N1}&\cdots&x_{Nd}\end{pmatrix}. \tag{6.1}$$
:::

La entrada $x_{ij}$ es el valor de la característica $j$ en el ejemplo $i$, exactamente como se acordó en la subsección [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3). La columna $j$ de $\mathbf{X}$ es la columna de la característica $j$ de la subsección [4.3](abstande-und-einheiten.html#stufe-4-3): todos los valores de esa característica a lo largo de todos los ejemplos. Las filas corresponden, por tanto, a los ejemplos; las columnas, a las características. La media de los ejemplos $\bar{\mathbf{x}}$ tiene como componente $j$ la media de la columna $j$.

::::beispiel [Ejemplo numérico]
Para el conjunto de datos de viviendas se tiene

$$\mathbf{X}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\in\mathbb{R}^{4\times3}.$$

La entrada $x_{32}=4$ es el número de habitaciones de la vivienda 3, la primera columna $(60,\,40,\,90,\,70)^{\top}$ contiene todas las superficies, y su media $65$ es la primera componente de $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$.
::::

⁠**En resumen:** La matriz de datos $\mathbf{X}\in\mathbb{R}^{N\times d}$ contiene un ejemplo por fila y una característica por columna.

:::hintergrund ¿Ejemplos como filas o como columnas?
Esta serie escribe los ejemplos como filas, como en una hoja de cálculo y en la mayoría de los libros de texto y bibliotecas de programación actuales. Algunos textos lo hacen al revés y colocan los ejemplos como columnas, una al lado de otra; su matriz de datos tiene entonces el tamaño $d\times N$. También las letras varían: a menudo el número de ejemplos se llama $m$ y el número de características $n$, y el ejemplo número $i$ se escribe $\mathbf{x}^{(i)}$, con el índice arriba entre paréntesis. En cuanto al contenido, no cambia nada. Por eso, quien lee un texto ajeno comprueba primero qué es allí fila y qué es columna.
:::

:::aufgabe Ejercicio 15 ★ Leer y construir matrices
<span class="anker" id="aufg-15"></span>

<ol class="al">

<li>

¿Qué tamaño tiene $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$? Indica $b_{13}$, $b_{21}$ y la tercera columna de $\mathbf{B}$.

</li>

<li>

Construye la matriz de datos de los tres textos de la subsección [5.4](winkel-und-ahnlichkeit.html#stufe-5-4). ¿Qué significan $N$, $d$ y la entrada $x_{23}$?

</li>

<li>

Una imagen en escala de grises de $4\times4$ píxeles muestra una «L» clara: la primera columna y la fila inferior son claras ($1$); todo lo demás, oscuro ($0$). Escribe la matriz y léela fila por fila para obtener un vector. ¿Cuántas componentes tiene?

</li>

</ol>

:::loesung
(a) $\mathbf{B}$ tiene el tamaño $2\times3$. Se tiene $b_{13}=2$ (fila 1, columna 3) y $b_{21}=2$ (fila 2, columna 1); la tercera columna es $(2,\,0)^{\top}$.

(b) $\mathbf{X}=\Bigl(\begin{smallmatrix}3&2&0\\6&4&0\\0&1&3\end{smallmatrix}\Bigr)$, con $N=3$ textos y $d=3$ palabras. La entrada $x_{23}=0$ dice: en el segundo texto no aparece la tercera palabra, «elección».

(c) La matriz tiene las filas $(1,0,0,0)$, $(1,0,0,0)$, $(1,0,0,0)$ y $(1,1,1,1)$. Leída fila por fila, da el vector

$$(1,0,0,0,\ 1,0,0,0,\ 1,0,0,0,\ 1,1,1,1)^{\top}\in\mathbb{R}^{16}$$

con $4\cdot4=16$ componentes.
:::
:::
