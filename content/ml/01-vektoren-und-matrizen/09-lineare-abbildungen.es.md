---
title: Aplicaciones lineales
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15210900
summary: Una matriz no es solo una tabla, sino también una regla de cálculo que convierte un vector en otro.
tags: aplicación, lineal, rotación, estiramiento, cizalladura, afín, ordenada en el origen
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Una matriz no es solo una tabla, sino también una regla de cálculo que convierte un vector en otro. Esta sección muestra qué reglas pueden escribirse así, a saber, exactamente las lineales, y qué hace una matriz geométricamente con el espacio.
:::

### Aplicaciones lineales

<span class="anker" id="stufe-8-1"></span>

Muchos cálculos convierten una lista de números en otra lista. A partir de las características de una vivienda se estiman el precio de compra y el alquiler; a partir de las muestras de una señal se obtiene una señal filtrada. Una regla así se llama __aplicación__ $f\colon\mathbb{R}^n\to\mathbb{R}^m$: asigna a cada vector $\mathbf{x}\in\mathbb{R}^n$ un vector $f(\mathbf{x})\in\mathbb{R}^m$.

El producto matriz-vector tiene dos propiedades especiales (subsección [7.1](das-matrix-vektor-produkt.html#stufe-7-1)): $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ y $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$. Da igual sumar primero y aplicar después la matriz o hacerlo al revés, y lo mismo ocurre con multiplicar por un número. En el plano, estas propiedades se ven en una cuadrícula: una aplicación así convierte rectas de nuevo en rectas o en puntos aislados, deja el origen en su sitio y convierte líneas de cuadrícula paralelas y equidistantes de nuevo en líneas paralelas y equidistantes o en puntos.

:::definition Definición 8.1 (Aplicación lineal)
<span class="anker" id="satz-8-1"></span>

Una aplicación $f\colon\mathbb{R}^n\to\mathbb{R}^m$ se llama __lineal__ si para todos los $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ y todos los escalares $c$ se cumple:

<span class="anker" id="gl-8-1"></span>
$$f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})\qquad\text{y}\qquad f(c\,\mathbf{u})=c\,f(\mathbf{u}) . \tag{8.1}$$
:::

Ambas condiciones juntas dicen: $f$ conserva las combinaciones lineales, $f(c_1\mathbf{u}+c_2\mathbf{v})=c_1f(\mathbf{u})+c_2f(\mathbf{v})$. Toda aplicación lineal lleva el vector nulo al vector nulo, pues $f(\mathbf{0})=f(0\cdot\mathbf{u})=0\cdot f(\mathbf{u})=\mathbf{0}$.

::::beispiel [Ejemplo numérico]
La aplicación $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ de $\mathbb{R}^2$ en $\mathbb{R}^2$ es lineal. Ambas componentes son sumas de múltiplos de las $x_j$, y para tales sumas se cumplen las condiciones [(8.1)](#gl-8-1); por ejemplo, $f(\mathbf{u}+\mathbf{v})=(u_1+v_1+u_2+v_2,\ 2u_1+2v_1)^{\top}=f(\mathbf{u})+f(\mathbf{v})$. No es lineal $g(\mathbf{x})=x_1x_2$, pues $g(2\mathbf{x})=4x_1x_2\ne2\,g(\mathbf{x})$ en cuanto $x_1x_2\ne0$. Tampoco $h(\mathbf{x})=\mathbf{x}+\mathbf 1$ es lineal, pues $h(\mathbf{0})=\mathbf 1\ne\mathbf{0}$.
::::

⁠**En resumen:** Una aplicación es lineal si conserva sumas y múltiplos; entonces lleva combinaciones lineales a combinaciones lineales.

:::hintergrund La misma linealidad que en los sistemas LTI
De la teoría de señales y sistemas se conoce el principio de superposición: un sistema lineal responde a la suma de dos señales de entrada con la suma de las dos respuestas, y a una señal amplificada con la respuesta amplificada en la misma proporción. Son exactamente las condiciones [(8.1)](#gl-8-1), solo que para señales en lugar de listas de números. Una señal muestreada de longitud finita es un vector (subsección [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)), y un sistema lineal que procesa tales señales es una aplicación lineal.
:::

### Toda aplicación lineal es una matriz

<span class="anker" id="stufe-8-2"></span>

Toda matriz da una aplicación lineal $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$. ¿Se cumple también lo recíproco? Sí, y la razón es sencilla: todo vector es una combinación lineal de los vectores unitarios, y una aplicación lineal conserva las combinaciones lineales. Quien sabe adónde van los $n$ vectores unitarios sabe, por tanto, adónde va cada vector.

:::satz Teorema 8.2 (Matriz de una aplicación lineal)
<span class="anker" id="satz-8-2"></span>

Para toda aplicación lineal $f\colon\mathbb{R}^n\to\mathbb{R}^m$ existe exactamente una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ con $f(\mathbf{x})=\mathbf{A}\mathbf{x}$ para todo $\mathbf{x}\in\mathbb{R}^n$. Sus columnas son las imágenes de los vectores unitarios:

<span class="anker" id="gl-8-2"></span>
$$\mathbf{a}_j=f(\mathbf{e}_j),\qquad j=1,\dots,n . \tag{8.2}$$
:::

:::beweis Matriz de una aplicación lineal
Según [(1.6)](vektoren-daten-als-zahlenlisten.html#gl-1-6), $\mathbf{x}=\sum_jx_j\mathbf{e}_j$. Como $f$ es lineal, se sigue

$$f(\mathbf{x})=f\Bigl(\sum_{j=1}^nx_j\mathbf{e}_j\Bigr)=\sum_{j=1}^nx_j\,f(\mathbf{e}_j)=\sum_{j=1}^nx_j\,\mathbf{a}_j=\mathbf{A}\mathbf{x} ,$$

el último paso, según la visión por columnas [(7.3)](das-matrix-vektor-produkt.html#gl-7-3). Si hubiera una segunda matriz $\mathbf{B}$ con $\mathbf{B}\mathbf{x}=f(\mathbf{x})$ para todo $\mathbf{x}$, tomando $\mathbf{x}=\mathbf{e}_j$, la columna $j$ de $\mathbf{B}$ sería igual a $f(\mathbf{e}_j)=\mathbf{a}_j$, para cada $j$. Por tanto, $\mathbf{B}=\mathbf{A}$.
:::

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ se tiene $f(\mathbf{e}_1)=(1,\,2)^{\top}$ y $f(\mathbf{e}_2)=(1,\,0)^{\top}$. Por tanto,

$$\mathbf{A}=\begin{pmatrix}1&1\\2&0\end{pmatrix},\qquad\text{y como comprobación}\qquad \mathbf{A}\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2\\6\end{pmatrix}=f\bigl((3,\,-1)^{\top}\bigr).$$
::::

⁠**En resumen:** Las aplicaciones lineales y las matrices son lo mismo; la columna $j$ de la matriz es la imagen del vector unitario $\mathbf{e}_j$.

:::hintergrund Un filtro como matriz: las columnas son las respuestas al impulso desplazadas
Sea un filtro de tiempo discreto que calcula $y[n]=x[n]+0{,}5\,x[n-1]$ y procesa señales de tres muestras, sin que haya nada antes de la primera muestra. El filtro es lineal, así que tiene una matriz. Según [(8.2)](#gl-8-2), su columna $j$ es la respuesta al vector unitario $\mathbf{e}_j$, es decir, a un único impulso unitario en la posición $j$. Esta respuesta es la respuesta al impulso $(1;\,0{,}5)$, desplazada $j-1$ pasos:

$$\mathbf{A}=\begin{pmatrix}1&0&0\\0{,}5&1&0\\0&0{,}5&1\end{pmatrix}.$$

La tercera columna ya solo contiene el $1$, porque la señal termina tras tres muestras. Para $\mathbf{x}=(2,\,4,\,6)^{\top}$, la matriz da $(2,\,5,\,8)^{\top}$, lo mismo que la fórmula del filtro. Toda convolución de una señal finita es de este modo un producto matriz-vector, y el teorema anterior explica por qué: si se conoce la respuesta a cada impulso individual, se conoce el sistema entero.
:::

:::hintergrund ¿Datos o aplicación? Dos papeles de la misma tabla
Una matriz puede ser una colección de datos, como la matriz de datos $\mathbf{X}$, o una aplicación, como la matriz de un filtro. Formalmente, ambas cosas son lo mismo, y a veces la misma matriz desempeña los dos papeles a la vez: la matriz de datos es también la aplicación $\mathbf{w}\mapsto\mathbf{X}\mathbf{w}$, que convierte pesos en predicciones. Lleva el $\mathbb{R}^d$ de los pesos al $\mathbb{R}^N$ de las listas de predicciones. Por eso, al leer una fórmula, conviene preguntarse en qué papel aparece una matriz en ese momento.
:::

### Aplicaciones lineales del plano

<span class="anker" id="stufe-8-3"></span>

En el plano se puede ver lo que hace una matriz. Se dibuja el cuadrado unidad, con los vértices $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_1+\mathbf{e}_2$ y $\mathbf{e}_2$, y su imagen. Como la aplicación conserva las combinaciones lineales, el cuadrado se convierte en el paralelogramo de vértices $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$ y $\mathbf{a}_2$. Sus dos lados en el origen son las columnas de la matriz (fig. [32](#abb-32)). Toda la cuadrícula del plano se deforma del mismo modo: cada casilla se convierte en una copia desplazada de este paralelogramo.

:::abbildung ml/k1ebene 32
Cuatro aplicaciones lineales del plano. En gris a trazos, el cuadrado unidad; en azul, su imagen. La flecha roja es la imagen $\mathbf{a}_1$ de $\mathbf{e}_1$; la verde, la imagen $\mathbf{a}_2$ de $\mathbf{e}_2$; son las dos columnas de la matriz. En el aplastamiento, $\mathbf{a}_2=\mathbf{0}$, y el cuadrado se convierte en el segmento de $\mathbf{0}$ a $\mathbf{e}_1$.
:::

<ul>

<li>

La __rotación__ de $90^\circ$ en sentido antihorario lleva $\mathbf{e}_1$ a $(0,\,1)^{\top}$ y $\mathbf{e}_2$ a $(-1,\,0)^{\top}$; esas son sus columnas.

</li>

<li>

El __estiramiento__ $\operatorname{diag}(2;\,0{,}5)$ estira el plano horizontalmente al doble y lo comprime verticalmente a la mitad.

</li>

<li>

La __cizalladura__ $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ deja $\mathbf{e}_1$ en su sitio y desplaza $\mathbf{e}_2$ hacia la derecha: cada punto se desplaza hacia la derecha tanto como su altura.

</li>

<li>

La matriz $\operatorname{diag}(1;\,0)$ conserva la primera componente y pone la segunda a cero. Aplasta todo el plano sobre el eje $x_1$.

</li>

</ul>

::::beispiel [Ejemplo numérico] la rotación de un ángulo cualquiera
Si se gira un ángulo $\alpha$ en sentido antihorario, $\mathbf{e}_1$ va a parar al punto $(\cos\alpha,\,\sin\alpha)^{\top}$ de la circunferencia unidad, y $\mathbf{e}_2$, que está $90^\circ$ más allá, al punto $(-\sin\alpha,\,\cos\alpha)^{\top}$. Según [(8.2)](#gl-8-2), la matriz de rotación es, por tanto,

<span class="anker" id="gl-8-3"></span>
$$\mathbf R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}. \tag{8.3}$$

Para $\alpha=90^\circ$ se obtiene la matriz de la fig. [32](#abb-32). Esta lleva el punto $(1,\,1)^{\top}$ a $(-1,\,1)^{\top}$; el estiramiento lo lleva a $(2;\ 0{,}5)^{\top}$; la cizalladura, a $(2,\,1)^{\top}$, y el aplastamiento, a $(1,\,0)^{\top}$.
::::

⁠**En resumen:** Una matriz $2\times2$ deforma la cuadrícula del plano; el cuadrado unidad se convierte en el paralelogramo que forman sus dos columnas.

### Funciones lineales con una salida

<span class="anker" id="stufe-8-4"></span>

Un modelo que convierte las características de un ejemplo en un único número es una aplicación de $\mathbb{R}^d$ en $\mathbb{R}$. Si es lineal, su matriz es, según el teorema de la subsección [8.2](#stufe-8-2), una única fila con $d$ entradas.

:::satz Teorema 8.3 (Las funciones lineales son sumas ponderadas)
<span class="anker" id="satz-8-3"></span>

Toda aplicación lineal $f\colon\mathbb{R}^d\to\mathbb{R}$ tiene la forma $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}$ con los pesos $w_j=f(\mathbf{e}_j)$.
:::

Es el teorema de la subsección [8.2](#stufe-8-2) para $m=1$: la matriz $1\times d$ es la fila $\mathbf{w}^{\top}$, y su producto por $\mathbf{x}$ es el producto escalar. La suma ponderada de la subsección [2.2](das-skalarprodukt.html#stufe-2-2) no es, por tanto, un ejemplo cualquiera, sino la regla lineal más general con una salida.

::::beispiel [Ejemplo numérico]
La regla de la agente inmobiliaria es $f(\mathbf{x})=3x_1+10x_2-4x_3$. Se tiene $f(\mathbf{e}_1)=3$, $f(\mathbf{e}_2)=10$, $f(\mathbf{e}_3)=-4$, es decir, $\mathbf{w}=(3,\,10,\,-4)^{\top}$. El peso $w_j=f(\mathbf{e}_j)$ es el valor de la regla para un ejemplo imaginario que solo tiene una unidad de la característica $j$ y nada más: dice cuánto aporta una unidad de esa característica.
::::

⁠**En resumen:** Toda aplicación lineal con una salida es una suma ponderada $\mathbf{w}^{\top}\mathbf{x}$, y el peso $w_j$ es su valor en $\mathbf{e}_j$.

### Aplicaciones afines

<span class="anker" id="stufe-8-5"></span>

La agente inmobiliaria se da cuenta de que sus estimaciones son sistemáticamente demasiado bajas. Por eso suma a cada suma ponderada un importe base de $20$ mil euros. Esta nueva regla ya no es lineal: a una vivienda imaginaria $\mathbf{x}=\mathbf{0}$ le asigna $20$ y no $0$. Es una aplicación lineal seguida de un desplazamiento.

:::definition Definición 8.4 (Aplicación afín)
<span class="anker" id="satz-8-4"></span>

Una aplicación $f\colon\mathbb{R}^n\to\mathbb{R}^m$ de la forma

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b} \tag{8.4}$$

con una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ y un vector fijo $\mathbf{b}\in\mathbb{R}^m$ se llama __afín__. Para una salida ($m=1$) se escribe $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+b$, y el número $b$ se llama __ordenada en el origen__.
:::

Para $\mathbf{b}\ne\mathbf{0}$, una aplicación afín no es lineal, pues $f(\mathbf{0})=\mathbf{b}\ne\mathbf{0}$. En la imagen de la cuadrícula, el plano primero se deforma y luego se traslada en bloque según $\mathbf{b}$; el origen va a parar a $\mathbf{b}$. En el lenguaje cotidiano, a las reglas afines también se las llama a menudo «lineales». En esta serie, solo se llama lineal a una aplicación con $\mathbf{b}=\mathbf{0}$.

Para todos los ejemplos a la vez, la predicción afín se escribe con el vector de unos $\mathbf 1\in\mathbb{R}^N$:

<span class="anker" id="gl-8-5"></span>
$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+b\,\mathbf 1 . \tag{8.5}$$

El sumando $b\,\mathbf 1$ suma a cada predicción el mismo importe $b$.

::::beispiel [Ejemplo numérico]
Con $\mathbf{w}=(3,\,10,\,-4)^{\top}$ y $b=20$, las predicciones $(188,\,126,\,286,\,232)^{\top}$ se convierten en las predicciones

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+20\cdot\mathbf 1=(208,\,146,\,306,\,252)^{\top}\ \text{miles de euros}.$$
::::

⁠**En resumen:** Una aplicación afín es una aplicación lineal más un desplazamiento fijo, $\mathbf{A}\mathbf{x}+\mathbf{b}$; con una salida, el desplazamiento se llama ordenada en el origen.

:::hintergrund El truco del uno añadido
Una función afín puede escribirse como función lineal si a cada ejemplo se le añade una componente con el valor fijo $1$:

$$\mathbf{w}^{\top}\mathbf{x}+b=\begin{pmatrix}w_1&\cdots&w_d&b\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_d\\1\end{pmatrix}.$$

La ordenada en el origen se convierte así en el peso de una característica que siempre vale $1$. Para todo el conjunto de datos, se añade a la matriz de datos una columna de unos: $\begin{pmatrix}\mathbf{X}&\mathbf 1\end{pmatrix}\begin{pmatrix}\mathbf{w}\\b\end{pmatrix}=\mathbf{X}\mathbf{w}+b\,\mathbf 1$. Para las viviendas, la matriz de datos ampliada tiene las filas $(60,2,3,1)$, $(40,1,1,1)$, $(90,4,6,1)$, $(70,3,2,1)$, y con el vector $(3,\,10,\,-4,\,20)^{\top}$ vuelve a salir $(208,\,146,\,306,\,252)^{\top}$. Con este truco, las reglas afines no necesitan una teoría propia: todo lo que vale para las aplicaciones lineales vale también para ellas en el espacio con una dimensión más.
:::

:::aufgabe Ejercicio 18 ★ ¿Lineal o no?
<span class="anker" id="aufg-18"></span>

Comprueba cuáles de las aplicaciones son lineales e indica la matriz de las que lo sean:

$$\begin{gathered} f_1(\mathbf{x})=(2x_1,\ x_1-x_2)^{\top},\qquad f_2(\mathbf{x})=x_1^2,\qquad f_3(\mathbf{x})=(x_2,\ x_1)^{\top},\\ f_4(x)=2x+3,\qquad f_5(\mathbf{x})=(0,\ 0)^{\top} \end{gathered}$$

para $\mathbf{x}\in\mathbb{R}^2$ o, en el caso de $f_4$, $x\in\mathbb{R}$.

:::loesung
<ul>

<li>

$f_1$ es lineal; ambas componentes son sumas de múltiplos de las $x_j$. Las columnas son $f_1(\mathbf{e}_1)=(2,\,1)^{\top}$ y $f_1(\mathbf{e}_2)=(0,\,-1)^{\top}$; la matriz es, por tanto, $\bigl(\begin{smallmatrix}2&0\\1&-1\end{smallmatrix}\bigr)$.

</li>

<li>

$f_2$ no es lineal: $f_2(2\mathbf{x})=4x_1^2\ne2f_2(\mathbf{x})$ en cuanto $x_1\ne0$.

</li>

<li>

$f_3$ es lineal, con la matriz $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$; intercambia las componentes.

</li>

<li>

$f_4$ no es lineal, pues $f_4(0)=3\ne0$. Es afín, con la ordenada en el origen $3$.

</li>

<li>

$f_5$ es lineal, con la matriz nula; ambas condiciones se cumplen porque $\mathbf{0}+\mathbf{0}=\mathbf{0}$ y $c\,\mathbf{0}=\mathbf{0}$.

</li>

</ul>
:::
:::

:::aufgabe Ejercicio 19 ★★ Matrices a partir de las imágenes de los vectores unitarios
<span class="anker" id="aufg-19"></span>

<ol class="al">

<li>

Indica la matriz de la rotación de $30^\circ$ y calcula la imagen de $(2,\,0)^{\top}$.

</li>

<li>

La reflexión respecto de la bisectriz $x_1=x_2$ intercambia las dos componentes. Indica su matriz y la imagen de $(3,\,1)^{\top}$.

</li>

<li>

Una aplicación lineal cumple $f\bigl((1,\,1)^{\top}\bigr)=(1,\,4)^{\top}$ y $f\bigl((2,\,-1)^{\top}\bigr)=(5,\,-1)^{\top}$. Determina su matriz. Pista: escribe ambas condiciones con las columnas $\mathbf{a}_1,\mathbf{a}_2$.

</li>

</ol>

:::loesung
(a) Según [(8.3)](#gl-8-3), con $\cos30^\circ=\sqrt3/2\approx0{,}866$ y $\sin30^\circ=\tfrac12$:

$$\mathbf R_{30^\circ}=\begin{pmatrix}0{,}866&-0{,}5\\0{,}5&0{,}866\end{pmatrix},\qquad \mathbf R_{30^\circ}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}\sqrt3\\1\end{pmatrix}\approx\begin{pmatrix}1{,}732\\1\end{pmatrix}.$$

La imagen es el doble de la primera columna, una flecha de longitud $2$ a $30^\circ$.

(b) $\mathbf{e}_1$ va a $\mathbf{e}_2$, y $\mathbf{e}_2$ va a $\mathbf{e}_1$; por tanto, la matriz es $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, y $(3,\,1)^{\top}$ va a $(1,\,3)^{\top}$.

(c) Por la linealidad, $f\bigl((1,1)^{\top}\bigr)=\mathbf{a}_1+\mathbf{a}_2=(1,\,4)^{\top}$ y $f\bigl((2,-1)^{\top}\bigr)=2\mathbf{a}_1-\mathbf{a}_2=(5,\,-1)^{\top}$. Si se suman ambas ecuaciones, se obtiene $3\mathbf{a}_1=(6,\,3)^{\top}$, es decir, $\mathbf{a}_1=(2,\,1)^{\top}$ y $\mathbf{a}_2=(1,4)^{\top}-(2,1)^{\top}=(-1,\,3)^{\top}$. La matriz es $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)$. Comprobación: $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)(2,\,-1)^{\top}=(5,\,-1)^{\top}$.
:::
:::

:::aufgabe Ejercicio 20 ★★ Un diferenciador como matriz
<span class="anker" id="aufg-20"></span>

Un filtro calcula, a partir de una señal de cuatro muestras, las diferencias $y[n]=x[n]-x[n-1]$, donde antes de la primera muestra se supone $x[0]=0$, $n=1,\dots,4$.

<ol class="al">

<li>

¿Por qué es lineal el filtro? Construye su matriz $4\times4$ calculando las respuestas a los cuatro impulsos unitarios.

</li>

<li>

Calcula la respuesta a $\mathbf{x}=(1,\,2,\,4,\,7)^{\top}$ con la matriz y con la fórmula.

</li>

</ol>

:::loesung
(a) Cada componente de salida $y[n]=x[n]-x[n-1]$ es una suma fija de múltiplos de las componentes de entrada; por tanto, el filtro es lineal. La respuesta al impulso en la posición $1$, $\mathbf{x}=\mathbf{e}_1=(1,0,0,0)^{\top}$, es $(1,\,-1,\,0,\,0)^{\top}$: primero la señal salta a $1$ y luego vuelve a $0$. Del mismo modo, el filtro responde a $\mathbf{e}_2$ con $(0,\,1,\,-1,\,0)^{\top}$, a $\mathbf{e}_3$ con $(0,\,0,\,1,\,-1)^{\top}$ y a $\mathbf{e}_4$ con $(0,\,0,\,0,\,1)^{\top}$; con este último impulso, la señal termina antes de que vuelva a bajar. Estas respuestas son las columnas:

$$\mathbf{A}=\begin{pmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix}.$$

(b) Con la matriz: $\mathbf{A}\,(1,2,4,7)^{\top}=(1,\ -1+2,\ -2+4,\ -4+7)^{\top}=(1,\,1,\,2,\,3)^{\top}$. Con la fórmula: $y[1]=1-0=1$, $y[2]=2-1=1$, $y[3]=4-2=2$, $y[4]=7-4=3$.
:::
:::
