---
title: La descomposición en valores singulares
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15221000
summary: Solo las matrices cuadradas tienen vectores propios, y solo en las simétricas son perpendiculares entre sí.
tags: valores singulares, vectores singulares derechos, vector singular izquierdo, norma espectral
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Solo las matrices cuadradas tienen vectores propios, y solo en las simétricas son perpendiculares entre sí. Esta sección muestra que toda matriz, incluso una rectangular, tiene un par de sistemas de ejes rectangulares: uno en el espacio de entrada y otro en el espacio de salida. La matriz transforma cada eje de uno en un múltiplo de un eje del otro. De ahí sale una descomposición de toda matriz en rotación, estiramiento y rotación.
:::

### Direcciones perpendiculares que siguen siendo perpendiculares

<span class="anker" id="stufe-9-1"></span>

La matriz $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ tiene, como matriz triangular, el valor propio doble $2$, pero solo una dirección propia: $(\mathbf{A}-2\mathbf{I})\mathbf{v}=\mathbf{0}$ significa $3v_2=0$, de modo que solo entran en consideración los múltiplos de $\mathbf{e}_1$ (ejercicio [19](eigenwerte-und-eigenvektoren.html#aufg-19)). Según la sección [7.2](diagonalisierung-und-spektralsatz.html#stufe-7-2), no es diagonalizable. Aun así, transforma la circunferencia unidad en una elipse (fig. [23](#abb-23)), y una elipse tiene dos ejes perpendiculares. ¿Qué flechas de la circunferencia van a parar a estos ejes?

Se busca menos que un vector propio: una flecha puede cambiar de dirección. Se buscan dos vectores unitarios perpendiculares $\mathbf{v}_1$, $\mathbf{v}_2$ cuyas imágenes $\mathbf{A}\mathbf{v}_1$ y $\mathbf{A}\mathbf{v}_2$ vuelvan a ser perpendiculares entre sí. Si dos imágenes son perpendiculares lo dice su producto escalar:

$$(\mathbf{A}\mathbf{v}_1)^{\top}(\mathbf{A}\mathbf{v}_2)=\mathbf{v}_1^{\top}\,\mathbf{A}^{\top}\mathbf{A}\,\mathbf{v}_2 .$$

Aquí aparece la matriz de Gram $\mathbf{A}^{\top}\mathbf{A}$. Es simétrica, aunque $\mathbf{A}$ no lo sea, y tiene, según el teorema espectral, una base ortonormal de vectores propios. Si $\mathbf{v}_2$ es un vector propio de $\mathbf{A}^{\top}\mathbf{A}$ asociado al valor propio $\lambda_2$ y $\mathbf{v}_1$ es perpendicular a $\mathbf{v}_2$, el producto escalar es $\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$. Los vectores propios de $\mathbf{A}^{\top}\mathbf{A}$ cumplen, por tanto, lo que se busca. El mismo cálculo con $\mathbf{v}_1=\mathbf{v}_2$ da las longitudes de las imágenes: $\lVert\mathbf{A}\mathbf{v}_i\rVert^2=\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_i=\lambda_i$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ es $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}4&6\\6&13\end{smallmatrix}\bigr)$, con la traza $17$ y el determinante $52-36=16$. El polinomio característico $\lambda^2-17\lambda+16=(\lambda-16)(\lambda-1)$ tiene las raíces $16$ y $1$. Son vectores propios normalizados $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$, asociado a $16$, y $\mathbf{v}_2=(-2,\,1)^{\top}/\sqrt5$, asociado a $1$. Sus imágenes

$$\mathbf{A}\mathbf{v}_1=\frac1{\sqrt5}\begin{pmatrix}8\\4\end{pmatrix},\qquad \mathbf{A}\mathbf{v}_2=\frac1{\sqrt5}\begin{pmatrix}-1\\2\end{pmatrix}$$

tienen el producto escalar $\tfrac15(-8+8)=0$ y las longitudes $\sqrt{80/5}=4=\sqrt{16}$ y $1=\sqrt1$ (fig. [22](#abb-22)).

:::abbildung ml/k2rsvdidee 22
Las imágenes $\mathbf{A}\mathbf{v}_1=(8,4)^{\top}/\sqrt5$ y $\mathbf{A}\mathbf{v}_2=(-1,2)^{\top}/\sqrt5$ son perpendiculares entre sí, y los cuadrados de sus longitudes son $16$ y $1$, los valores propios de $\mathbf{A}^{\top}\mathbf{A}$.
:::
::::

⁠**En resumen:** Los vectores propios de la matriz simétrica $\mathbf{A}^{\top}\mathbf{A}$ son direcciones perpendiculares cuyas imágenes por $\mathbf{A}$ vuelven a ser perpendiculares entre sí; las imágenes tienen las longitudes $\sqrt{\lambda_i}$.

### Valores singulares

<span class="anker" id="stufe-9-2"></span>

Las longitudes de las imágenes son las magnitudes características más importantes de una matriz: dicen cuánto estira la matriz en sus direcciones principales. Según la sección [8.4](positiv-definite-matrizen.html#stufe-8-4), $\mathbf{A}^{\top}\mathbf{A}$ es semidefinida positiva; sus valores propios no son, por tanto, negativos, y se puede extraer la raíz.

:::definition Definición 9.1 (Valores singulares)
<span class="anker" id="satz-9-1"></span>

Sea $\mathbf{A}\in\mathbb{R}^{m\times n}$, y sean $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n\ge0$ los valores propios de $\mathbf{A}^{\top}\mathbf{A}$, ordenados de forma decreciente y con los múltiples contados según su multiplicidad. Los números

<span class="anker" id="gl-9-1"></span>
$$d_j=\sqrt{\lambda_j},\qquad d_1\ge d_2\ge\dots\ge d_n\ge0 , \tag{9.1}$$

se llaman __valores singulares__ de $\mathbf{A}$.
:::

Muchos libros escriben $\sigma_j$ en lugar de $d_j$. Aquí, los valores singulares llevan siempre un índice; la $d$ sin índice de [Fundamentos 1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), el número de características, es otra cosa.

:::satz Teorema 9.2 (Valores singulares y rango)
<span class="anker" id="satz-9-2"></span>

El número de valores singulares distintos de cero es el rango de $\mathbf{A}$.
:::

:::beweis Valores singulares y rango
Sean $\mathbf{v}_1,\dots,\mathbf{v}_n$ vectores propios ortonormales de $\mathbf{A}^{\top}\mathbf{A}$ asociados a $\lambda_1,\dots,\lambda_n$. Todo vector es $\mathbf{x}=\sum_jc_j\mathbf{v}_j$; por tanto, $\mathbf{A}\mathbf{x}=\sum_jc_j\,\mathbf{A}\mathbf{v}_j$: el espacio columna está generado por las imágenes $\mathbf{A}\mathbf{v}_1,\dots,\mathbf{A}\mathbf{v}_n$. Según la subsección anterior, estas son perpendiculares dos a dos y tienen las longitudes $d_j$. Las imágenes con $d_j=0$ son el vector nulo y no aportan nada. Las restantes son perpendiculares entre sí y no nulas; divididas por sus longitudes, son ortonormales y, según el teorema de la sección [1.1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-1), linealmente independientes. Forman una base del espacio columna, y su número es el rango.
:::

En lo que sigue, el rango de una matriz se designa por $r$. Se tiene $d_1\ge\dots\ge d_r>0$ y $d_{r+1}=\dots=d_n=0$.

::::beispiel [Ejemplo numérico]
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ tiene los valores singulares $d_1=4$ y $d_2=1$ y el rango $2$. Los valores propios son $2$ y $2$: valores singulares y valores propios son, en general, números distintos. La matriz $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ tiene $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$, con los valores propios $25$ y $0$; tiene, por tanto, los valores singulares $5$ y $0$ y el rango $1$.
::::

⁠**En resumen:** Los valores singulares $d_j$ son las raíces de los valores propios de $\mathbf{A}^{\top}\mathbf{A}$; miden cuánto estira $\mathbf{A}$ en sus direcciones principales, y el número de los positivos es el rango.

### Vectores singulares

<span class="anker" id="stufe-9-3"></span>

A cada valor singular positivo le corresponden dos direcciones: una dirección de entrada $\mathbf{v}_j$ y la dirección de su imagen.

:::definition Definición 9.3 (Vectores singulares)
<span class="anker" id="satz-9-3"></span>

Los vectores propios ortonormales $\mathbf{v}_1,\dots,\mathbf{v}_n$ de $\mathbf{A}^{\top}\mathbf{A}$ asociados a los valores propios $d_1^2,\dots,d_n^2$ se llaman __vectores singulares derechos__ de $\mathbf{A}$. Para $d_j>0$,

<span class="anker" id="gl-9-2"></span>
$$\mathbf{u}_j=\frac{\mathbf{A}\mathbf{v}_j}{d_j},\qquad\text{es decir,}\qquad \mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j , \tag{9.2}$$

se llama __vector singular izquierdo__ correspondiente.
:::

Los nombres vienen del lugar que ocupan los vectores en la descomposición de la subsección siguiente. Los vectores singulares izquierdos vuelven a ser ortonormales, pues

$$\mathbf{u}_i^{\top}\mathbf{u}_j=\frac{\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_id_j}=\frac{d_j^2\,\mathbf{v}_i^{\top}\mathbf{v}_j}{d_id_j},$$

y esto es $1$ para $i=j$ y $0$ en otro caso. Son los vectores propios de $\mathbf{A}\mathbf{A}^{\top}$, y se cumple la ecuación en el sentido contrario:

$$\mathbf{A}^{\top}\mathbf{u}_j=\frac{\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_j}=d_j\mathbf{v}_j,\qquad \mathbf{A}\mathbf{A}^{\top}\mathbf{u}_j=d_j\,\mathbf{A}\mathbf{v}_j=d_j^2\,\mathbf{u}_j .$$

$\mathbf{A}$ transforma $\mathbf{v}_j$ en $d_j\mathbf{u}_j$, y $\mathbf{A}^{\top}$ transforma $\mathbf{u}_j$ en $d_j\mathbf{v}_j$.

:::warnung Los signos van juntos
Un vector propio solo está determinado salvo el signo. Si se calculan los $\mathbf{v}_j$ como vectores propios de $\mathbf{A}^{\top}\mathbf{A}$ y, por separado, los $\mathbf{u}_j$ como vectores propios de $\mathbf{A}\mathbf{A}^{\top}$, un $\mathbf{u}_j$ puede salir con el signo equivocado, y entonces $\mathbf{A}\mathbf{v}_j=-d_j\mathbf{u}_j$. El camino seguro es [(9.2)](#gl-9-2): primero elegir $\mathbf{v}_j$ y después calcular $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$. Si se cambia el signo de $\mathbf{v}_j$ y $\mathbf{u}_j$ a la vez, todo sigue siendo correcto.
:::

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ es $\mathbf{u}_1=\mathbf{A}\mathbf{v}_1/4=(2,\,1)^{\top}/\sqrt5$ y $\mathbf{u}_2=\mathbf{A}\mathbf{v}_2/1=(-1,\,2)^{\top}/\sqrt5$. Como control: $\mathbf{A}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}13&6\\6&4\end{smallmatrix}\bigr)$ transforma $(2,\,1)^{\top}$ en $(32,\,16)^{\top}=16\,(2,\,1)^{\top}$. El vector $(-2,\,-1)^{\top}/\sqrt5$ también sería un vector propio normalizado de $\mathbf{A}\mathbf{A}^{\top}$ asociado a $16$, pero con él se tendría $\mathbf{A}\mathbf{v}_1=-4\,\mathbf{u}_1$.
::::

⁠**En resumen:** Los vectores singulares derechos $\mathbf{v}_j$ son vectores propios de $\mathbf{A}^{\top}\mathbf{A}$; los izquierdos son $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$; ambas familias son ortonormales, y $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$.

### La descomposición

<span class="anker" id="stufe-9-4"></span>

Si se escriben las ecuaciones $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ para todos los $j$ una al lado de otra, se obtiene una descomposición de toda la matriz.

:::satz Teorema 9.4 (Descomposición en valores singulares)
<span class="anker" id="satz-9-4"></span>

Toda matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ de rango $r$ puede escribirse como

<span class="anker" id="gl-9-3"></span>
$$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top} \tag{9.3}$$

con matrices ortogonales $\mathbf{U}\in\mathbb{R}^{m\times m}$ y $\mathbf{V}\in\mathbb{R}^{n\times n}$ y una matriz $\mathbf{D}\in\mathbb{R}^{m\times n}$ que lleva en la diagonal los valores singulares $d_1\ge\dots\ge d_r>0$ y, en lo demás, solo ceros. Las columnas de $\mathbf{V}$ son vectores singulares derechos; las $r$ primeras columnas de $\mathbf{U}$, los izquierdos correspondientes. Es equivalente la forma compacta

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}=\sum_{j=1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} . \tag{9.4}$$
:::

:::beweis Descomposición en valores singulares
Para $j\le r$ es $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$. Para $j>r$ es $d_j=0$; por tanto, $\lVert\mathbf{A}\mathbf{v}_j\rVert=0$ y $\mathbf{A}\mathbf{v}_j=\mathbf{0}$. Si $r<m$, se completan $\mathbf{u}_1,\dots,\mathbf{u}_r$ hasta una base ortonormal de $\mathbb{R}^m$, por ejemplo con el proceso de Gram-Schmidt, como en la demostración del teorema espectral. Según [Fundamentos 1, sección 9.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-2), la columna $j$ de $\mathbf{A}\mathbf{V}$ es el vector $\mathbf{A}\mathbf{v}_j$, y la columna $j$ de $\mathbf{U}\mathbf{D}$ es $d_j\mathbf{u}_j$ para $j\le r$ y, en otro caso, el vector nulo. Por tanto, $\mathbf{A}\mathbf{V}=\mathbf{U}\mathbf{D}$. Como $\mathbf{V}$ es ortogonal, $\mathbf{V}\mathbf{V}^{\top}=\mathbf{I}$, y multiplicando por $\mathbf{V}^{\top}$ por la derecha se obtiene $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$. La forma compacta se deduce de [Fundamentos 1, sección 9.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5): columna $j$ de $\mathbf{U}\mathbf{D}$ por fila $j$ de $\mathbf{V}^{\top}$, sumado sobre $j$; solo los sumandos con $j\le r$ son distintos de cero.
:::

El tamaño de $\mathbf{D}$ se rige por el de $\mathbf{A}$. Para $m=3$ y $n=2$, por ejemplo, $\mathbf{D}=\Bigl(\begin{smallmatrix}d_1&0\\0&d_2\\0&0\end{smallmatrix}\Bigr)$. La abreviatura habitual es SVD, del nombre inglés *singular value decomposition*.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ es

$$\mathbf{A}=\underbrace{\frac1{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix}}_{\mathbf{U}}\underbrace{\begin{pmatrix}4&0\\0&1\end{pmatrix}}_{\mathbf{D}}\underbrace{\frac1{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}}_{\mathbf{V}^{\top}},$$

pues $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}8&-1\\4&2\end{smallmatrix}\bigr)$ y $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\tfrac15\bigl(\begin{smallmatrix}8+2&16-1\\4-4&8+2\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. En forma compacta:

$$4\cdot\frac15\begin{pmatrix}2&4\\1&2\end{pmatrix}+1\cdot\frac15\begin{pmatrix}2&-1\\-4&2\end{pmatrix}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix}+\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}=\begin{pmatrix}2&3\\0&2\end{pmatrix}.$$
::::

⁠**En resumen:** Toda matriz es $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, con dos matrices ortogonales y los valores singulares en la diagonal de $\mathbf{D}$, o, de forma equivalente, una suma $\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$.

:::hintergrund Por qué la descomposición existe para toda matriz
No toda matriz tiene vectores propios, y sus vectores propios no siempre son perpendiculares. La descomposición en valores singulares sortea ambos obstáculos con un truco: no usa los vectores propios de $\mathbf{A}$, sino los de $\mathbf{A}^{\top}\mathbf{A}$. Esta matriz es simétrica y semidefinida positiva para toda $\mathbf{A}$, y para ella el teorema espectral garantiza una base ortonormal de vectores propios con valores propios $\ge0$. El precio: se necesitan dos bases en lugar de una, una para el espacio de entrada y otra para el de salida.

Los vectores singulares también pueden describirse sin $\mathbf{A}^{\top}\mathbf{A}$. Según [(8.2)](positiv-definite-matrizen.html#gl-8-2), aplicado a $\mathbf{A}^{\top}\mathbf{A}$, para vectores unitarios es $\lVert\mathbf{A}\mathbf{v}\rVert^2=\mathbf{v}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}\le\lambda_1=d_1^2$, con igualdad en $\mathbf{v}_1$. Por tanto, $\mathbf{v}_1$ es la dirección que $\mathbf{A}$ más estira, y $d_1$ es ese estiramiento máximo. Entre todos los vectores unitarios perpendiculares a $\mathbf{v}_1$, el que más se estira es $\mathbf{v}_2$, y así sucesivamente; lo muestra el mismo cálculo de la media que en la demostración de [(8.2)](positiv-definite-matrizen.html#gl-8-2), con $c_1=0$. La descomposición enumera, por tanto, las direcciones por orden, del estiramiento más fuerte al más débil.

Lo que es único son los valores singulares. Si todos los $d_j$ son distintos y positivos, cada par $\mathbf{v}_j,\mathbf{u}_j$ queda determinado salvo un signo común. Con valores singulares iguales hay más libertad: una matriz ortogonal $\mathbf{Q}$ tiene todos sus valores singulares iguales a $1$, y para toda matriz ortogonal $\mathbf{V}$, $\mathbf{Q}=(\mathbf{Q}\mathbf{V})\,\mathbf{I}\,\mathbf{V}^{\top}$ es una descomposición en valores singulares.
:::

### Rotación, estiramiento, rotación

<span class="anker" id="stufe-9-5"></span>

Si se lee $\mathbf{A}\mathbf{x}=\mathbf{U}\bigl(\mathbf{D}(\mathbf{V}^{\top}\mathbf{x})\bigr)$ de derecha a izquierda, toda matriz actúa en tres pasos (fig. [23](#abb-23)):

<ol>

<li>

$\mathbf{V}^{\top}\mathbf{x}$ calcula, según [(1.2)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-2), las coordenadas $c_j=\mathbf{v}_j^{\top}\mathbf{x}$ de $\mathbf{x}$ en la base de los $\mathbf{v}_j$. Geométricamente es una rotación o una reflexión que lleva $\mathbf{v}_j$ a $\mathbf{e}_j$.

</li>

<li>

$\mathbf{D}$ multiplica cada coordenada $c_j$ por $d_j$. Si $m>n$, $\mathbf{D}$ añade ceros; si $m<n$, $\mathbf{D}$ suprime las últimas coordenadas. La circunferencia unidad se convierte en una elipse cuyos ejes están sobre los ejes de coordenadas.

</li>

<li>

$\mathbf{U}$ lleva $\mathbf{e}_j$ a $\mathbf{u}_j$; de nuevo, una rotación o una reflexión.

</li>

</ol>

Toda aplicación lineal es, por tanto, salvo reflexiones, una rotación, un estiramiento a lo largo de los ejes y otra rotación. Transforma la circunferencia unidad en una elipse y la esfera unidad en un elipsoide, con los semiejes $d_j\mathbf{u}_j$. Si $\det\mathbf{A}<0$, interviene al menos una reflexión, pues según [Fundamentos 1, sección 14.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), es $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$, y $\det\mathbf{D}\ge0$.

:::abbildung ml/k2svd 23
La matriz $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ como rotación, estiramiento y rotación. Arriba a la izquierda, la circunferencia unidad con $\mathbf{v}_1=(1,2)^{\top}/\sqrt5$ (rojo) y $\mathbf{v}_2=(-2,1)^{\top}/\sqrt5$ (verde). $\mathbf{V}^{\top}$ gira $-63{,}4^\circ$ y lleva $\mathbf{v}_1$ a $\mathbf{e}_1$ y $\mathbf{v}_2$ a $\mathbf{e}_2$ (abajo a la izquierda). $\mathbf{D}$ estira el primer eje por el factor $d_1=4$ y el segundo por el factor $d_2=1$ (abajo a la derecha). $\mathbf{U}$ gira $26{,}6^\circ$ y lleva los ejes a $\mathbf{u}_1=(2,1)^{\top}/\sqrt5$ y $\mathbf{u}_2=(-1,2)^{\top}/\sqrt5$ (arriba a la derecha). El punto negro $\mathbf{x}=\mathbf{e}_2$ llega por todos los caminos a $\mathbf{A}\mathbf{x}=(3,2)^{\top}$. El camino directo, arriba, es la propia $\mathbf{A}$: la circunferencia unidad se convierte en la elipse con los semiejes $4\,\mathbf{u}_1$ y $1\cdot\mathbf{u}_2$.
:::

::::beispiel [Ejemplo numérico]
Para $\mathbf{x}=\mathbf{e}_2$ y $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, las coordenadas son $\mathbf{V}^{\top}\mathbf{x}=(2,\,1)^{\top}/\sqrt5$. Estirado, esto da $\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=(8,\,1)^{\top}/\sqrt5$, y girado,

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=\frac15\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}8\\1\end{pmatrix}=\frac15\begin{pmatrix}15\\10\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}=\mathbf{A}\mathbf{e}_2 .$$

$\mathbf{V}$ tiene las columnas $(\cos\theta,\,\sin\theta)^{\top}$ y $(-\sin\theta,\,\cos\theta)^{\top}$ con $\cos\theta=1/\sqrt5$; es, por tanto, la rotación de ángulo $\theta\approx63{,}4^\circ$, y $\mathbf{V}^{\top}$ gira de vuelta $-63{,}4^\circ$. $\mathbf{U}$ es la rotación de $26{,}6^\circ$, pues $\cos26{,}6^\circ\approx2/\sqrt5$.
::::

⁠**En resumen:** Toda matriz gira, estira a lo largo de los ejes y vuelve a girar, salvo reflexiones; la circunferencia unidad se convierte en una elipse con los semiejes $d_j\mathbf{u}_j$.

### Bloques de rango 1 y los espacios de una matriz

<span class="anker" id="stufe-9-6"></span>

Cada sumando $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ de la forma compacta [(9.4)](#gl-9-4) tiene rango $1$, pues todas sus columnas son múltiplos de $\mathbf{u}_j$. Actúa sobre un vector así:

$$d_j\mathbf{u}_j\mathbf{v}_j^{\top}\mathbf{x}=d_j\,(\mathbf{v}_j^{\top}\mathbf{x})\,\mathbf{u}_j .$$

Lee la coordenada de $\mathbf{x}$ a lo largo de $\mathbf{v}_j$, la multiplica por $d_j$ y entrega el resultado en la dirección de $\mathbf{u}_j$. La matriz es la suma de $r$ bloques de este tipo, ordenados por su tamaño $d_j$. De paso, la descomposición proporciona bases ortonormales de los subespacios asociados a una matriz.

:::satz Teorema 9.5 (Lo que generan los vectores singulares)
<span class="anker" id="satz-9-5"></span>

Sea $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ de rango $r$. Entonces:

<ol class="rm">

<li>

$\mathbf{u}_1,\dots,\mathbf{u}_r$ es una base ortonormal del espacio columna de $\mathbf{A}$, y $\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ es una base ortonormal de su complemento ortogonal;

</li>

<li>

$\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ es una base ortonormal del núcleo de $\mathbf{A}$, y $\mathbf{v}_1,\dots,\mathbf{v}_r$ es una base ortonormal del espacio columna de $\mathbf{A}^{\top}$.

</li>

</ol>
:::

:::beweis Espacios
(i) Todo $\mathbf{A}\mathbf{x}=\sum_{j\le r}d_j(\mathbf{v}_j^{\top}\mathbf{x})\mathbf{u}_j$ está en el espacio generado por $\mathbf{u}_1,\dots,\mathbf{u}_r$ y, a la inversa, $\mathbf{u}_j=\mathbf{A}(\mathbf{v}_j/d_j)$ es una imagen. Las columnas restantes de $\mathbf{U}$ son perpendiculares a estas y generan, por tanto, según la sección [4.4](projektion-auf-einen-unterraum.html#stufe-4-4), el complemento ortogonal. (ii) Como los $\mathbf{u}_j$ son independientes y los $d_j$ positivos, $\mathbf{A}\mathbf{x}=\mathbf{0}$ si y solo si $\mathbf{v}_j^{\top}\mathbf{x}=0$ para todo $j\le r$, es decir, si $\mathbf{x}$ solo tiene coordenadas a lo largo de $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$. Por último, $\mathbf{A}^{\top}=\mathbf{V}\mathbf{D}^{\top}\mathbf{U}^{\top}$ es una descomposición en valores singulares de $\mathbf{A}^{\top}$ en la que $\mathbf{U}$ y $\mathbf{V}$ intercambian sus papeles; (i) para $\mathbf{A}^{\top}$ da el resto.
:::

Los números encajan con el teorema del rango de [Fundamentos 1, sección 13.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5): el núcleo tiene dimensión $n-r$.

::::beispiel [Ejemplo numérico]
La matriz $\mathbf{H}$ con las columnas $(1,\,0,\,1)^{\top}$ y $(0,\,1,\,1)^{\top}$ de la sección [3.2](die-beste-naherungslosung.html#stufe-3-2) tiene $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, con los valores propios $3$ y $1$; tiene, por tanto, los valores singulares $d_1=\sqrt3$ y $d_2=1$ y los vectores singulares derechos $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. Los izquierdos son

$$\mathbf{u}_1=\frac{\mathbf{H}\mathbf{v}_1}{\sqrt3}=\frac1{\sqrt6}\begin{pmatrix}1\\1\\2\end{pmatrix},\qquad \mathbf{u}_2=\frac{\mathbf{H}\mathbf{v}_2}{1}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.$$

Forman una base ortonormal del plano $x_3=x_1+x_2$, distinta de la de la sección [4.3](projektion-auf-einen-unterraum.html#stufe-4-3). Se completa con $\mathbf{u}_3=(1,\,1,\,-1)^{\top}/\sqrt3$, el vector normal normalizado de la sección [4.4](projektion-auf-einen-unterraum.html#stufe-4-4). En la descomposición completa es $\mathbf{D}=\Bigl(\begin{smallmatrix}\sqrt3&0\\0&1\\0&0\end{smallmatrix}\Bigr)$. El núcleo solo consta del vector nulo, pues $r=n=2$.
::::

⁠**En resumen:** Una matriz es la suma de $r$ bloques $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ de rango $1$; los $\mathbf{u}_j$ con $d_j>0$ generan el espacio columna, y los $\mathbf{v}_j$ con $d_j=0$, el núcleo.

### Matrices simétricas

<span class="anker" id="stufe-9-7"></span>

Para una matriz simétrica ya existe una descomposición con una base ortonormal, $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. ¿Qué relación tiene con la descomposición en valores singulares?

:::satz Teorema 9.6 (Valores singulares de las matrices simétricas)
<span class="anker" id="satz-9-6"></span>

Los valores singulares de una matriz simétrica son los valores absolutos $|\lambda_i|$ de sus valores propios. Si $\mathbf{q}_i$ es un vector propio normalizado asociado a $\lambda_i\ne0$, entonces $\mathbf{v}=\mathbf{q}_i$ es un vector singular derecho y $\mathbf{u}=\operatorname{sign}(\lambda_i)\,\mathbf{q}_i$, el vector singular izquierdo correspondiente.
:::

:::beweis Matrices simétricas
Se tiene $\mathbf{A}^{\top}\mathbf{A}=\mathbf{A}^2=\mathbf{Q}\boldsymbol{\Lambda}^2\mathbf{Q}^{\top}$; por tanto, $\mathbf{A}^{\top}\mathbf{A}$ tiene los vectores propios $\mathbf{q}_i$ con los valores propios $\lambda_i^2$, y los valores singulares son $\sqrt{\lambda_i^2}=|\lambda_i|$. Según [(9.2)](#gl-9-2), $\mathbf{u}=\mathbf{A}\mathbf{q}_i/|\lambda_i|=(\lambda_i/|\lambda_i|)\,\mathbf{q}_i$.
:::

Si $\mathbf{A}$ es semidefinida positiva, la descomposición espectral y la descomposición en valores singulares son la misma descomposición, con $\mathbf{U}=\mathbf{V}=\mathbf{Q}$. Con valores propios negativos, el signo pasa a $\mathbf{U}$. En las matrices no simétricas, los valores propios y los valores singulares no tienen, en general, nada que ver entre sí, como muestra $\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, con los valores propios $2,2$ y los valores singulares $4,1$. Pero siempre hay una relación: todo valor propio es, en módulo, como mucho $d_1$; esto se deduce de la subsección siguiente.

::::beispiel [Ejemplo numérico]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ tiene el valor propio $4$, con $\mathbf{q}_1=(1,\,1)^{\top}/\sqrt2$, y el valor propio $-2$, con $\mathbf{q}_2=(1,\,-1)^{\top}/\sqrt2$. Los valores singulares son $4$ y $2$. Con $\mathbf{v}_2=\mathbf{q}_2$ es $\mathbf{A}\mathbf{v}_2=(-2,\,2)^{\top}/\sqrt2=2\cdot(-1,\,1)^{\top}/\sqrt2$; por tanto, $\mathbf{u}_2=-\mathbf{q}_2$.
::::

⁠**En resumen:** En las matrices simétricas, los valores singulares son los valores absolutos de los valores propios, y en las semidefinidas positivas, la descomposición en valores singulares es la descomposición espectral.

### La norma espectral

<span class="anker" id="stufe-9-8"></span>

¿Cuánto puede alargar una matriz un vector como máximo? Para vectores, la norma mide el tamaño. Para una matriz, una medida natural de su tamaño es su mayor factor de alargamiento.

:::definition Definición 9.7 (Norma espectral)
<span class="anker" id="satz-9-7"></span>

La __norma espectral__ de una matriz $\mathbf{A}$ es

$$\lVert\mathbf{A}\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} .$$
:::

:::satz Teorema 9.8 (Estiramiento máximo y mínimo)
<span class="anker" id="satz-9-8"></span>

Para toda $\mathbf{A}\in\mathbb{R}^{m\times n}$ con los valores singulares $d_1\ge\dots\ge d_n$ y todo $\mathbf{x}\in\mathbb{R}^n$ se cumple

<span class="anker" id="gl-9-5"></span>
$$d_n\,\lVert\mathbf{x}\rVert\le\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\,\lVert\mathbf{x}\rVert . \tag{9.5}$$

Las cotas se alcanzan en $\mathbf{x}=\mathbf{v}_1$ y $\mathbf{x}=\mathbf{v}_n$. En particular, $\lVert\mathbf{A}\rVert_2=d_1$.
:::

:::beweis Estiramiento máximo y mínimo
Con $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ es $\lVert\mathbf{c}\rVert=\lVert\mathbf{x}\rVert$ y $\lVert\mathbf{A}\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\sum_jd_j^2c_j^2$. Esto está entre $d_n^2\sum_jc_j^2$ y $d_1^2\sum_jc_j^2$. Es el cociente de Rayleigh [(8.2)](positiv-definite-matrizen.html#gl-8-2) de $\mathbf{A}^{\top}\mathbf{A}$, multiplicado por $\lVert\mathbf{x}\rVert^2$.
:::

Dos consecuencias. Primera: $\lVert\mathbf{A}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert$ y, por ello, $\lVert\mathbf{A}\mathbf{B}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2\lVert\mathbf{x}\rVert$, es decir, $\lVert\mathbf{A}\mathbf{B}\rVert_2\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2$: al aplicar las matrices una tras otra, el factor de estiramiento máximo es, como mucho, el producto de los factores máximos. Segunda: para un vector propio es $\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$; por tanto, $|\lambda|\le d_1$ para todo valor propio de una matriz cuadrada. Para un vector propio complejo $\mathbf{v}=\mathbf{a}+\mathrm j\mathbf{b}$ con $\mathbf{a},\mathbf{b}$ reales vale lo mismo si se pone $\lVert\mathbf{v}\rVert^2=(\mathbf{v}^*)^{\top}\mathbf{v}=\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2$, pues $\lVert\mathbf{A}\mathbf{v}\rVert^2=\lVert\mathbf{A}\mathbf{a}\rVert^2+\lVert\mathbf{A}\mathbf{b}\rVert^2$ está, según [(9.5)](#gl-9-5), entre $d_n^2\lVert\mathbf{v}\rVert^2$ y $d_1^2\lVert\mathbf{v}\rVert^2$; para $\mathbf{A}$ cuadrada es, por tanto, también $|\lambda|\ge d_n$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ es $\lVert\mathbf{A}\rVert_2=4$. Los vectores unitarios de la base canónica se estiran menos: $\lVert\mathbf{A}\mathbf{e}_1\rVert=\lVert(2,\,0)^{\top}\rVert=2$ y $\lVert\mathbf{A}\mathbf{e}_2\rVert=\lVert(3,\,2)^{\top}\rVert=\sqrt{13}\approx3{,}61$. El factor $4$ solo se alcanza en $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$, y el factor mínimo $1$, en $\mathbf{v}_2$. El valor propio $2$ está entre $1$ y $4$.
::::

⁠**En resumen:** La norma espectral $\lVert\mathbf{A}\rVert_2=d_1$ es el mayor factor por el que $\mathbf{A}$ alarga un vector; el menor es $d_n$.

:::hintergrund Varias antenas: canales paralelos a partir de la descomposición en valores singulares
Un sistema de radio con varias antenas transmisoras y receptoras se llama sistema MIMO. Cada antena receptora recibe una mezcla de todas las señales transmitidas. En un modelo sencillo, el vector recibido es $\mathbf{y}=\mathbf{K}\mathbf{x}+\boldsymbol\nu$: $\mathbf{x}$ contiene las señales que transmiten las antenas, la matriz de canal $\mathbf{K}$ describe con qué intensidad llega cada antena transmisora a cada antena receptora, y $\boldsymbol\nu$ es el ruido.

Si el transmisor y el receptor conocen la descomposición $\mathbf{K}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, el transmisor envía $\mathbf{x}=\mathbf{V}\tilde{\mathbf{x}}$, y el receptor calcula $\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{y}$. Entonces

$$\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\tilde{\mathbf{x}}+\mathbf{U}^{\top}\boldsymbol\nu=\mathbf{D}\tilde{\mathbf{x}}+\tilde{\boldsymbol\nu} .$$

El canal mezclado se ha convertido en $r$ canales separados: $\tilde y_j=d_j\tilde x_j+\tilde\nu_j$. Cada uno transmite su propio flujo de datos, con el factor de amplificación $d_j$. El ruido solo se gira; su longitud no cambia, pues $\mathbf{U}^{\top}$ es ortogonal. El número de canales paralelos utilizables es el rango de la matriz de canal, y lo bueno que es cada canal lo dice su valor singular. Esto es rotación, estiramiento y rotación en la práctica: el transmisor gira de antemano, el canal estira y el receptor gira de vuelta.
:::

:::aufgabe Ejercicio 27 ★★ Una descomposición a mano
<span class="anker" id="aufg-27"></span>

Sea $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Calcula $\mathbf{A}^{\top}\mathbf{A}$, sus valores propios y los valores singulares de $\mathbf{A}$.

</li>

<li>

Determina $\mathbf{v}_1,\mathbf{v}_2$ y, a partir de ellos, $\mathbf{u}_1,\mathbf{u}_2$ con [(9.2)](#gl-9-2). Comprueba $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Compara los valores singulares con los valores propios de $\mathbf{A}$. ¿Qué coincide y qué no?

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}9+16&20\\20&25\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr)$, con traza $50$ y determinante $625-400=225$; por tanto, $\lambda^2-50\lambda+225=(\lambda-45)(\lambda-5)$. Los valores singulares son $d_1=\sqrt{45}=3\sqrt5\approx6{,}708$ y $d_2=\sqrt5\approx2{,}236$.

(b) Vectores propios de $\mathbf{A}^{\top}\mathbf{A}$: $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, asociado a $45$, y $\mathbf{v}_2=(-1,\,1)^{\top}/\sqrt2$, asociado a $5$. Entonces

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}{d_1}=\frac{(3,\,9)^{\top}}{\sqrt2\cdot3\sqrt5}=\frac{(1,\,3)^{\top}}{\sqrt{10}},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{d_2}=\frac{(-3,\,1)^{\top}}{\sqrt2\cdot\sqrt5}=\frac{(-3,\,1)^{\top}}{\sqrt{10}} .$$

Comprobación: $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt{10}}\bigl(\begin{smallmatrix}3\sqrt5&-3\sqrt5\\9\sqrt5&\sqrt5\end{smallmatrix}\bigr)=\tfrac1{\sqrt2}\bigl(\begin{smallmatrix}3&-3\\9&1\end{smallmatrix}\bigr)$ y

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\frac1{\sqrt2}\begin{pmatrix}3&-3\\9&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}6&0\\8&10\end{pmatrix}=\begin{pmatrix}3&0\\4&5\end{pmatrix}.$$

(c) Los valores propios de la matriz triangular son $3$ y $5$. El producto coincide: $3\cdot5=15=3\sqrt5\cdot\sqrt5=|\det\mathbf{A}|$. Las sumas no: $8$ frente a $4\sqrt5\approx8{,}94$. Los valores propios están, en valor absoluto, entre $d_2$ y $d_1$: $2{,}236\le3$ y $5\le6{,}708$.
:::
:::

:::aufgabe Ejercicio 28 ★★ Una matriz rectangular
<span class="anker" id="aufg-28"></span>

Sea $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Determina los valores singulares y los vectores singulares $\mathbf{v}_1,\mathbf{v}_2,\mathbf{u}_1,\mathbf{u}_2$.

</li>

<li>

Completa con $\mathbf{u}_3$ y escribe la descomposición completa $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Da bases ortonormales del espacio columna y de su complemento ortogonal.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ tiene los valores propios $4$, con $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, y $2$, con $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. Por tanto, $d_1=2$, $d_2=\sqrt2$, y

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}2=\frac{(2,\,2,\,0)^{\top}}{2\sqrt2}=\frac{(1,\,1,\,0)^{\top}}{\sqrt2},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{\sqrt2}=\frac{(0,\,0,\,2)^{\top}}{\sqrt2\cdot\sqrt2}=(0,\,0,\,1)^{\top} .$$

(b) $\mathbf{u}_3$ es perpendicular a ambos: $\mathbf{u}_3=(1,\,-1,\,0)^{\top}/\sqrt2$. La descomposición completa es

$$\mathbf{A}=\begin{pmatrix}1/\sqrt2&0&1/\sqrt2\\1/\sqrt2&0&-1/\sqrt2\\0&1&0\end{pmatrix}\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

(c) Según el teorema de la sección [9.6](#stufe-9-6), $\mathbf{u}_1,\mathbf{u}_2$ es una base ortonormal del espacio columna, y $\mathbf{u}_3$, una del complemento ortogonal. Como control: las columnas $(1,\,1,\,1)^{\top}=\sqrt2\,\mathbf{u}_1+\mathbf{u}_2$ y $(1,\,1,\,-1)^{\top}=\sqrt2\,\mathbf{u}_1-\mathbf{u}_2$ están en el espacio generado por $\mathbf{u}_1,\mathbf{u}_2$, y ambas son perpendiculares a $\mathbf{u}_3$.
:::
:::

:::aufgabe Ejercicio 29 ★★★ Propiedades de los valores singulares
<span class="anker" id="aufg-29"></span>

<ol class="al">

<li>

Demuestra: para una matriz cuadrada, $|\det\mathbf{A}|=d_1d_2\cdots d_n$.

</li>

<li>

Demuestra: $\mathbf{A}$ y $\mathbf{A}^{\top}$ tienen los mismos valores singulares positivos.

</li>

<li>

Demuestra: para $\mathbf{u}\ne\mathbf{0}$ y $\mathbf{v}\ne\mathbf{0}$, el producto exterior $\mathbf{u}\mathbf{v}^{\top}$ tiene exactamente un valor singular positivo, a saber, $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

</li>

<li>

Demuestra: si $\mathbf{Q}$ es ortogonal, $\mathbf{Q}\mathbf{A}$ y $\mathbf{A}$ tienen los mismos valores singulares.

</li>

</ol>

:::loesung
(a) Según [Fundamentos 1, sección 14.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$. Las dos matrices ortogonales tienen determinante $\pm1$, y $\mathbf{D}$ es una matriz diagonal con determinante $d_1\cdots d_n$. Por tanto, $|\det\mathbf{A}|=d_1\cdots d_n$.

(b) De $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ se deduce $\mathbf{A}^{\top}\mathbf{A}=\mathbf{V}\mathbf{D}^{\top}\mathbf{D}\mathbf{V}^{\top}$ y $\mathbf{A}\mathbf{A}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^{\top}\mathbf{U}^{\top}$. Las matrices diagonales $\mathbf{D}^{\top}\mathbf{D}$ y $\mathbf{D}\mathbf{D}^{\top}$ tienen en la diagonal las mismas entradas $d_j^2>0$; solo difieren en el número de ceros. Los valores singulares de $\mathbf{A}^{\top}$ son las raíces cuadradas de los valores propios de $(\mathbf{A}^{\top})^{\top}\mathbf{A}^{\top}=\mathbf{A}\mathbf{A}^{\top}$, es decir, de nuevo los $d_j$, completados con ceros.

(c) $(\mathbf{u}\mathbf{v}^{\top})^{\top}(\mathbf{u}\mathbf{v}^{\top})=\mathbf{v}\,\mathbf{u}^{\top}\mathbf{u}\,\mathbf{v}^{\top}=\lVert\mathbf{u}\rVert^2\,\mathbf{v}\mathbf{v}^{\top}$. Esta matriz transforma $\mathbf{v}$ en $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\,\mathbf{v}$, y cada vector perpendicular a $\mathbf{v}$, en cero. Sus valores propios son, por tanto, $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ y, por lo demás, $0$, y el único valor singular positivo es $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

(d) $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$. Ambas matrices tienen la misma matriz de Gram y, por tanto, los mismos valores singulares. Intuitivamente: una rotación o una reflexión después de $\mathbf{A}$ no cambia la forma de la elipse, solo su posición.
:::
:::
