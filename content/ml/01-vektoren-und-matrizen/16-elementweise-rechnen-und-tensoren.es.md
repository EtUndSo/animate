---
title: Cálculo elemento a elemento y tensores
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Capítulo 1: Vectores y matrices
nachschlagen: ja
order: 15211600
summary: No todo cálculo con vectores y matrices es un producto de matrices.
tags: producto de Hadamard, elemento a elemento, tensor, eje, forma
lang: es
---

<span class="anker" id="stufe-15"></span>

:::zweck
No todo cálculo con vectores y matrices es un producto de matrices. Esta sección presenta los cálculos que operan entrada por entrada y amplía los vectores y las matrices a disposiciones de números con más de dos índices, como las que se necesitan para las imágenes.
:::

### El producto de Hadamard

<span class="anker" id="stufe-15-1"></span>

Un comerciante tiene la lista de las cantidades vendidas y la lista de los precios unitarios. Para cada artículo quiere la facturación, es decir, cantidad por precio, pero todavía no la suma. Es un producto entrada por entrada.

:::definition Definición 15.1 (Producto de Hadamard)
<span class="anker" id="satz-15-1"></span>

Para dos vectores o dos matrices del mismo tamaño, el __producto de Hadamard__ $\mathbf{A}\odot\mathbf{B}$ es el producto entrada por entrada:

<span class="anker" id="gl-15-1"></span>
$$(\mathbf{A}\odot\mathbf{B})_{ij}=a_{ij}\,b_{ij} . \tag{15.1}$$
:::

El producto de Hadamard *no* es el producto de matrices. El producto de matrices forma productos escalares de filas y columnas; el producto de Hadamard solo multiplica entradas en la misma posición. Dos relaciones con lo ya conocido: si se suma el producto de Hadamard de dos vectores, se obtiene su producto escalar, $\mathbf 1^{\top}(\mathbf{u}\odot\mathbf{v})=\mathbf{u}^{\top}\mathbf{v}$. Y el producto de Hadamard por un vector fijo es la multiplicación por una matriz diagonal: $\mathbf{v}\odot\mathbf{x}=\operatorname{diag}(\mathbf{v})\,\mathbf{x}$.

::::beispiel [Ejemplo numérico]
$(1,\,2,\,3)^{\top}\odot(4,\,5,\,6)^{\top}=(4,\,10,\,18)^{\top}$, y $4+10+18=32$ es el producto escalar. Para matrices se tiene

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix},\qquad\text{pero}\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

Con un vector de ceros y unos se pueden ocultar características: $(1,\,0,\,1)^{\top}\odot\mathbf{x}_1=(60,\,0,\,3)^{\top}$ suprime en la vivienda 1 el número de habitaciones.
::::

⁠**En resumen:** El producto de Hadamard $\odot$ multiplica entrada por entrada; no es el producto de matrices.

### Funciones elemento a elemento

<span class="anker" id="stufe-15-2"></span>

A menudo se aplica la misma función a cada entrada de un vector: se elevan al cuadrado todos los errores, se toma el valor absoluto de todos o se redondean todos los valores.

:::definition Definición 15.2 (Función elemento a elemento)
<span class="anker" id="satz-15-2"></span>

Para una función $f\colon\mathbb{R}\to\mathbb{R}$ y un vector $\mathbf{x}\in\mathbb{R}^d$, $f$ aplicada __elemento a elemento__ es el vector $\bigl(f(x_1),\dots,f(x_d)\bigr)^{\top}$. Para las matrices vale lo mismo, entrada por entrada.
:::

Muchas normas pueden escribirse así: la norma 1 es la suma de los valores absolutos elemento a elemento, $\lVert\mathbf{x}\rVert_1=\mathbf 1^{\top}|\mathbf{x}|$, y el cuadrado de la norma euclídea, la suma de los cuadrados elemento a elemento. Una función elemento a elemento no es lineal en general: elevar al cuadrado elemento a elemento convierte $2\mathbf{x}$ en el vector con las entradas $4x_j^2$, no $2x_j^2$.

::::beispiel [Ejemplo numérico]
El vector de error de la agente inmobiliaria era $(-12,\,-4,\,-4,\,-8)^{\top}$. Los valores absolutos elemento a elemento dan $(12,\,4,\,4,\,8)^{\top}$, con la suma $28$, la norma 1. Para el tasador A de la subsección [3.5](normen-die-groe-eines-vektors.html#stufe-3-5), los cuadrados elemento a elemento dan $(100,\,100,\,100,\,100)^{\top}$, con la suma $400=20^2$.
::::

⁠**En resumen:** Una función elemento a elemento actúa sobre cada entrada por separado; en general no es lineal.

### Sumar un vector a cada fila

<span class="anker" id="stufe-15-3"></span>

Para centrar un conjunto de datos entero, se resta de cada fila de la matriz de datos el mismo vector, la media de los ejemplos. Del mismo modo, la predicción afín suma a cada componente la misma ordenada en el origen. Para tales cálculos hace falta una notación.

La media de los ejemplos la da un producto matriz-vector: $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$, pues su componente $j$ es $\frac1N\sum_ix_{ij}$, la media de la columna $j$. La matriz cuyas filas son todas iguales a $\bar{\mathbf{x}}^{\top}$ es el producto exterior $\mathbf 1\,\bar{\mathbf{x}}^{\top}$. Con ello, la matriz de datos centrada es

<span class="anker" id="gl-15-2"></span>
$$\tilde{\mathbf{X}}=\mathbf{X}-\mathbf 1\,\bar{\mathbf{x}}^{\top} , \tag{15.2}$$

cuya fila $i$ es el vector $(\mathbf{x}_i-\bar{\mathbf{x}})^{\top}$. Muchos textos escriben abreviadamente $\mathbf{X}-\bar{\mathbf{x}}^{\top}$ y quieren decir con ello: restar el vector fila de cada fila. En sentido estricto, la diferencia de una matriz $N\times d$ y una matriz $1\times d$ no está definida; la abreviatura significa siempre [(15.2)](#gl-15-2).

::::beispiel [Ejemplo numérico]
Para las viviendas, $\bar{\mathbf{x}}=\tfrac14\mathbf{X}^{\top}\mathbf 1=(65;\ 2{,}5;\ 3)^{\top}$ y

$$\tilde{\mathbf{X}}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}-\begin{pmatrix}65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\end{pmatrix}=\begin{pmatrix}-5&-0{,}5&0\\-25&-1{,}5&-2\\25&1{,}5&3\\5&0{,}5&-1\end{pmatrix}.$$

Cada columna es la columna de la característica centrada de la subsección [4.3](abstande-und-einheiten.html#stufe-4-3) y suma cero.
::::

⁠**En resumen:** Sumar un vector $\mathbf{q}$ a cada fila de una matriz $\mathbf{A}$ significa $\mathbf{A}+\mathbf 1\,\mathbf{q}^{\top}$; la abreviatura habitual $\mathbf{A}+\mathbf{q}^{\top}$ quiere decir exactamente eso.

### Tensores

<span class="anker" id="stufe-15-4"></span>

Un escalar es un único número; un vector, una lista con un índice; una matriz, una tabla con dos índices. Una imagen en color necesita tres: fila, columna y canal de color. Una pila de imágenes en color necesita cuatro. Todas estas disposiciones de números se reúnen bajo un solo nombre.

:::definition Definición 15.3 (Tensor, forma)
<span class="anker" id="satz-15-3"></span>

Un __tensor__ es, en el aprendizaje automático, una disposición de números cuyas entradas se numeran mediante $k$ índices. Cada índice recorre un __eje__. La lista de las longitudes de los ejes se llama la __forma__ del tensor.
:::

Un escalar es un tensor con $0$ ejes; un vector de $\mathbb{R}^d$, uno con un eje de longitud $d$; una matriz de $\mathbb{R}^{m\times n}$, uno con la forma $m\times n$. Un tensor de forma $n_1\times n_2\times\dots\times n_k$ tiene $n_1\cdot n_2\cdots n_k$ entradas. La figura [42](#abb-42) muestra los primeros casos.

:::abbildung ml/k1tensor 42
Tensores de $0$ a $4$ ejes: un escalar, un vector de $4$ entradas, una matriz $4\times4$ (por ejemplo, una imagen en escala de grises), una imagen en color formada por tres canales $4\times4$ para rojo, verde y azul, y una pila de $N$ de estas imágenes en color (representada con tres imágenes).
:::

::::beispiel [Ejemplo numérico]
Una imagen en color de $4\times4$ píxeles y tres canales de color es un tensor de forma $3\times4\times4$ con $48$ entradas. La entrada con los índices $(1,2,3)$ es la luminosidad del primer canal, es decir, el rojo, en el píxel de la fila $2$ y la columna $3$.
::::

⁠**En resumen:** Un tensor es una disposición de números con un número cualquiera de ejes; el escalar, el vector y la matriz son los casos con $0$, $1$ y $2$ ejes.

:::hintergrund El tensor de la física es otra cosa
En física, un tensor es más que una disposición de números, por ejemplo el tensor de inercia, que indica lo difícil que es hacer girar un cuerpo en torno a cada eje, o el tensor que describe con qué intensidad se estira o se comprime una viga cargada en cada dirección. Allí, al tensor le corresponde una regla que dice cómo cambian sus entradas cuando se gira el sistema de coordenadas; las entradas solas no lo constituyen. En el aprendizaje automático falta esta regla: en ese ámbito, un tensor es solo una disposición multidimensional de números. La palabra es la misma; el concepto, otro.
:::

### Imágenes como tensores

<span class="anker" id="stufe-15-5"></span>

Los datos de imagen son el ejemplo más importante de tensores con más de dos ejes. Su forma muestra de inmediato cuántos números contiene un conjunto de datos.

Una imagen en escala de grises de $28\times28$ píxeles es una matriz, es decir, un tensor de forma $28\times28$ con $784$ entradas. Una imagen en color de $32\times32$ píxeles tiene tres canales y la forma $3\times32\times32$, es decir, $3072$ entradas. Una pila de $100$ de estas imágenes en color tiene la forma $100\times3\times32\times32$ y $307\,200$ entradas. El primer eje cuenta aquí los ejemplos, igual que las filas de la matriz de datos: la matriz de datos es el caso particular de una pila de vectores, con la forma $N\times d$.

El orden de los ejes es una convención. Algunos programas ponen el canal de color al principio ($3\times32\times32$); otros, al final ($32\times32\times3$). Los números son los mismos, solo cambia su disposición, y antes de cada cálculo tiene que estar claro qué significa cada eje.

::::beispiel [Ejemplo numérico]
Un conjunto de datos de $60\,000$ imágenes en escala de grises de $28\times28$ píxeles es un tensor de forma $60\,000\times28\times28$ con $47\,040\,000$ entradas. Si cada imagen se lee como un vector de $\mathbb{R}^{784}$, se obtiene una matriz de datos de $\mathbb{R}^{60\,000\times784}$, con las mismas entradas.
::::

⁠**En resumen:** Una imagen es un tensor con dos o tres ejes; una pila de imágenes, uno con un eje más; el primer eje cuenta los ejemplos.

:::aufgabe Ejercicio 36 ★ ¿Elemento a elemento o no?
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

Calcula $\mathbf{u}\odot\mathbf{v}$ y $\mathbf{u}^{\top}\mathbf{v}$ para $\mathbf{u}=(2,\,-1,\,3)^{\top}$ y $\mathbf{v}=(1,\,4,\,2)^{\top}$.

</li>

<li>

Calcula $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\odot\bigl(\begin{smallmatrix}2&0\\1&3\end{smallmatrix}\bigr)$ y el producto de matrices de las mismas matrices.

</li>

<li>

¿Qué forma y cuántas entradas tiene una pila de $64$ imágenes en color de $224\times224$ píxeles, con el canal de color delante?

</li>

</ol>

:::loesung
(a) $\mathbf{u}\odot\mathbf{v}=(2,\,-4,\,6)^{\top}$ y $\mathbf{u}^{\top}\mathbf{v}=2-4+6=4$, la suma de las entradas del producto de Hadamard.

(b) Hadamard: $\bigl(\begin{smallmatrix}1\cdot2&2\cdot0\\3\cdot1&4\cdot3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&0\\3&12\end{smallmatrix}\bigr)$. Producto de matrices: $\bigl(\begin{smallmatrix}2+2&0+6\\6+4&0+12\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4&6\\10&12\end{smallmatrix}\bigr)$. Solo la entrada de abajo a la derecha coincide, por casualidad.

(c) La forma es $64\times3\times224\times224$, con $64\cdot3\cdot224\cdot224=9\,633\,792$ entradas.
:::
:::

:::aufgabe Ejercicio 37 ★★ Centrar un conjunto de datos
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Demuestra: las columnas de la matriz de datos centrada [(15.2)](#gl-15-2) suman cero, es decir, $\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf{0}^{\top}$. Usa $\mathbf 1^{\top}\mathbf 1=N$.

</li>

<li>

Centra la matriz de datos de los tres textos de la subsección [5.4](winkel-und-ahnlichkeit.html#stufe-5-4).

</li>

</ol>

:::loesung
(a) Se tiene $\bar{\mathbf{x}}^{\top}=\frac1N\mathbf 1^{\top}\mathbf{X}$, la traspuesta de $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$. Con ello,

$$\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf 1^{\top}\mathbf{X}-(\mathbf 1^{\top}\mathbf 1)\,\bar{\mathbf{x}}^{\top}=\mathbf 1^{\top}\mathbf{X}-N\cdot\tfrac1N\,\mathbf 1^{\top}\mathbf{X}=\mathbf{0}^{\top} .$$

Cada columna es un vector centrado, y sus componentes suman cero, como en la subsección [4.3](abstande-und-einheiten.html#stufe-4-3).

(b) La media de los textos es $\bar{\mathbf{x}}=\tfrac13\bigl((3,2,0)^{\top}+(6,4,0)^{\top}+(0,1,3)^{\top}\bigr)=(3,\,\tfrac73,\,1)^{\top}$. Centrada:

$$\tilde{\mathbf{X}}=\begin{pmatrix}0&-\frac13&-1\\3&\frac53&-1\\-3&-\frac43&2\end{pmatrix}.$$

Cada columna suma cero: $0+3-3=0$, $-\tfrac13+\tfrac53-\tfrac43=0$, $-1-1+2=0$.
:::
:::
