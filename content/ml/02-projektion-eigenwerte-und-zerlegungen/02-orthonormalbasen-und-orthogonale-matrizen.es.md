---
title: Bases ortonormales y matrices ortogonales
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15220200
summary: Algunos sistemas de coordenadas son especialmente cómodos: sus ejes son perpendiculares entre sí y la unidad tiene la misma longitud en cada eje.
tags: ortonormales, base ortonormal, matriz ortogonal
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Algunos sistemas de coordenadas son especialmente cómodos: sus ejes son perpendiculares entre sí y la unidad tiene la misma longitud en cada eje. En un sistema así no hace falta resolver un sistema de ecuaciones para hallar las coordenadas de un punto, y las longitudes se calculan con el teorema de Pitágoras. Esta sección introduce tales sistemas de coordenadas y las matrices que les corresponden.
:::

### Vectores ortonormales

<span class="anker" id="stufe-1-1"></span>

En [Fundamentos 1, sección 5.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-3), dos vectores se llamaban ortogonales si su producto escalar es cero. El patrón constante $(1,1,1,1)^{\top}$ y el patrón alternante $(1,-1,1,-1)^{\top}$ eran un ejemplo: al comparar una señal con uno de los patrones, el otro patrón no interfería. Eso sí, la comparación daba la contribución del patrón multiplicada por $4$, porque ambos patrones tienen longitud $2$. Si los vectores ortogonales tienen además longitud $1$, también desaparece este factor.

Imagina los dos ejes $\mathbf{e}_1$ y $\mathbf{e}_2$ del plano girados en bloque un cierto ángulo. Las dos flechas siguen teniendo longitud $1$ y siguen siendo perpendiculares entre sí; solo apuntan en otras direcciones.

:::definition Definición 1.1 (Ortonormales)
<span class="anker" id="satz-1-1"></span>

Los vectores $\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathbb{R}^n$ se llaman __ortonormales__ si cada uno de ellos tiene longitud $1$ y dos cualesquiera distintos de ellos son ortogonales:

<span class="anker" id="gl-1-1"></span>
$$\mathbf{q}_i^{\top}\mathbf{q}_l=\begin{cases}1, & i=l,\\ 0, & i\ne l.\end{cases} \tag{1.1}$$
:::

La palabra se compone de «ortogonal» y «normalizado». Los vectores unitarios $\mathbf{e}_1,\dots,\mathbf{e}_n$ son el ejemplo más sencillo.

:::satz Teorema 1.2 (Los vectores ortonormales son linealmente independientes)
<span class="anker" id="satz-1-2"></span>

Si $\mathbf{q}_1,\dots,\mathbf{q}_k$ son ortonormales, son linealmente independientes.
:::

:::beweis Independencia lineal
Sea $c_1\mathbf{q}_1+\dots+c_k\mathbf{q}_k=\mathbf{0}$. Se calcula el producto escalar de ambos lados con $\mathbf{q}_l$. Según [(1.1)](#gl-1-1), a la izquierda solo queda el sumando $c_l\,\mathbf{q}_l^{\top}\mathbf{q}_l=c_l$, y a la derecha está $\mathbf{q}_l^{\top}\mathbf{0}=0$. Por tanto, $c_l=0$, y eso para cada $l$. Según la definición de [Fundamentos 1, sección 13.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-2), los vectores son entonces linealmente independientes.
:::

::::beispiel [Ejemplo numérico]
Para $\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ y $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ se tiene

$$\mathbf{q}_1^{\top}\mathbf{q}_1=0{,}36+0{,}64=1,\qquad \mathbf{q}_2^{\top}\mathbf{q}_2=0{,}64+0{,}36=1,\qquad \mathbf{q}_1^{\top}\mathbf{q}_2=-0{,}48+0{,}48=0 .$$

Los dos vectores son ortonormales; la fig. [1](#abb-1) muestra el último producto escalar paso a paso. El patrón constante y el alternante se vuelven ortonormales si se dividen por su longitud $2$: $\tfrac12(1,1,1,1)^{\top}$ y $\tfrac12(1,-1,1,-1)^{\top}$.

:::abbildung ml/k2rorth 1
El producto escalar $\mathbf{q}_1^{\top}\mathbf{q}_2$ paso a paso, con $0{,}6=\tfrac35$ y $0{,}8=\tfrac45$: componente por componente y después la suma.
:::
::::

⁠**En resumen:** Los vectores ortonormales tienen longitud $1$ y son perpendiculares dos a dos; siempre son linealmente independientes.

### Bases ortonormales

<span class="anker" id="stufe-1-2"></span>

Según [Fundamentos 1, sección 13.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), una base es un sistema de coordenadas: cada vector tiene en ella exactamente una representación. Las más cómodas son las bases cuyos vectores son ortonormales. Son como el sistema de ejes habitual, solo que girado.

:::definition Definición 1.3 (Base ortonormal)
<span class="anker" id="satz-1-3"></span>

Una base formada por vectores ortonormales se llama __base ortonormal__.
:::

Para una base ortonormal de todo $\mathbb{R}^n$ basta con encontrar $n$ vectores ortonormales. Según el teorema de la subsección anterior, son linealmente independientes. Si se escriben como columnas de una matriz $n\times n$, esta tiene rango $n$, y su espacio columna es, según [Fundamentos 1, sección 13.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), todo $\mathbb{R}^n$. Por tanto, los $n$ vectores generan $\mathbb{R}^n$ y forman una base. Del mismo modo puede buscarse una base ortonormal de un espacio generado, por ejemplo de un plano en $\mathbb{R}^3$: vectores ortonormales que generen exactamente ese espacio.

::::beispiel [Ejemplo numérico]
Los vectores $\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ y $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ son dos vectores ortonormales de $\mathbb{R}^2$ y, por tanto, una base ortonormal de $\mathbb{R}^2$. Los vectores unitarios $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ forman la base ortonormal de $\mathbb{R}^3$ que se llama base canónica. El plano $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ de $\mathbb{R}^3$ tiene la base ortonormal $\mathbf{e}_1,\mathbf{e}_2$.
::::

⁠**En resumen:** Una base ortonormal es un sistema de ejes girado: $n$ vectores ortonormales de $\mathbb{R}^n$ forman siempre una base.

### Coordenadas en una base ortonormal

<span class="anker" id="stufe-1-3"></span>

En una base cualquiera hay que resolver un sistema de ecuaciones para hallar las coordenadas de un vector. En [Fundamentos 1, sección 13.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), $(3,\,2)^{\top}$ tenía en la base $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ las coordenadas $1$ y $2$. Los productos escalares $(1,0)(3,2)^{\top}=3$ y $(1,1)(3,2)^{\top}=5$ son algo completamente distinto. En una base ortonormal, en cambio, las coordenadas son exactamente los productos escalares.

La razón la muestra la imagen de la longitud de la sombra de [Fundamentos 1, sección 5.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5). Para un vector normalizado $\mathbf{q}$, $\mathbf{q}^{\top}\mathbf{x}$ es la longitud de la sombra de $\mathbf{x}$ sobre la recta en la dirección de $\mathbf{q}$. En una base ortonormal, cada coordenada es la sombra sobre su propio eje (fig. [2](#abb-2)).

:::abbildung ml/k2onb 2
Coordenadas en la base ortonormal $\mathbf{q}_1=(0{,}6;\,0{,}8)^{\top}$, $\mathbf{q}_2=(-0{,}8;\,0{,}6)^{\top}$ (verde). La flecha $\mathbf{x}=(3,1)^{\top}$ proyecta una sombra sobre cada uno de los dos ejes girados (gris); la luz incide en cada caso perpendicularmente (a trazos). Las longitudes de las sombras, $\mathbf{q}_1^{\top}\mathbf{x}=2{,}6$ (azul) y $\mathbf{q}_2^{\top}\mathbf{x}=-1{,}8$ (naranja), son las coordenadas: $\mathbf{x}=2{,}6\,\mathbf{q}_1-1{,}8\,\mathbf{q}_2$.
:::

:::satz Teorema 1.4 (Coordenadas en una base ortonormal)
<span class="anker" id="satz-1-4"></span>

Si $\mathbf{q}_1,\dots,\mathbf{q}_n$ es una base ortonormal de $\mathbb{R}^n$, para todo vector $\mathbf{x}\in\mathbb{R}^n$ se cumple

<span class="anker" id="gl-1-2"></span>
$$\mathbf{x}=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})\,\mathbf{q}_i\qquad\text{y}\qquad \lVert\mathbf{x}\rVert^2=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})^2 . \tag{1.2}$$
:::

:::beweis Coordenadas en una base ortonormal
Como los vectores forman una base, existen números $c_1,\dots,c_n$ con $\mathbf{x}=\sum_ic_i\mathbf{q}_i$. El producto escalar con $\mathbf{q}_l$ da, según [(1.1)](#gl-1-1),

$$\mathbf{q}_l^{\top}\mathbf{x}=\sum_{i=1}^nc_i\,\mathbf{q}_l^{\top}\mathbf{q}_i=c_l ,$$

pues solo el sumando con $i=l$ no es cero. Para la longitud se desarrolla el producto:

$$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^nc_i\,c_l\,\mathbf{q}_i^{\top}\mathbf{q}_l=\sum_{i=1}^nc_i^2 ,$$

de nuevo porque solo quedan los sumandos con $i=l$.
:::

La segunda fórmula es el teorema de Pitágoras en $\mathbb{R}^n$: la longitud de una flecha se obtiene igual a partir de sus coordenadas en cualquier sistema de ejes rectangular, siempre que la unidad tenga longitud $1$ en todos los ejes.

::::beispiel [Ejemplo numérico]
Para $\mathbf{x}=(3,\,1)^{\top}$ y la base de la subsección anterior se tiene

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=1{,}8+0{,}8=2{,}6,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=-2{,}4+0{,}6=-1{,}8 .$$

Comprobación: $2{,}6\,(0{,}6;\ 0{,}8)^{\top}-1{,}8\,(-0{,}8;\ 0{,}6)^{\top}=(1{,}56+1{,}44;\ 2{,}08-1{,}08)^{\top}=(3,\,1)^{\top}$. Y $c_1^2+c_2^2=6{,}76+3{,}24=10=\lVert\mathbf{x}\rVert^2$. La fig. [3](#abb-3) muestra las tres sumas con fracciones.

:::abbildung ml/k2rkoord 3
Las coordenadas $c_1=\tfrac{13}5=2{,}6$ y $c_2=-\tfrac95=-1{,}8$ de $\mathbf{x}$ como productos escalares, y la suma de sus cuadrados, el cuadrado de la longitud de $\mathbf{x}$.
:::
::::

⁠**En resumen:** En una base ortonormal, cada coordenada es un producto escalar, $c_i=\mathbf{q}_i^{\top}\mathbf{x}$, y la suma de los cuadrados de las coordenadas es el cuadrado de la longitud.

:::hintergrund Oscilaciones muestreadas como base ortonormal y el teorema de Parseval
Los cuatro vectores

$$\begin{gathered} \mathbf{q}_1=\tfrac12(1,\,1,\,1,\,1)^{\top},\qquad \mathbf{q}_2=\tfrac1{\sqrt2}(1,\,0,\,-1,\,0)^{\top},\\ \mathbf{q}_3=\tfrac1{\sqrt2}(0,\,1,\,0,\,-1)^{\top},\qquad \mathbf{q}_4=\tfrac12(1,\,-1,\,1,\,-1)^{\top} \end{gathered}$$

son las muestras de una componente continua, de una oscilación coseno y una oscilación seno con un periodo de cuatro muestras, y de una oscilación que cambia de signo en cada muestra, cada una normalizada. Es fácil comprobar que son ortonormales. Forman, por tanto, una base ortonormal de $\mathbb{R}^4$. Toda señal de cuatro muestras es una suma de estas cuatro oscilaciones, y las contribuciones son, según [(1.2)](#gl-1-2), simplemente productos escalares. Para la señal $\mathbf{x}=(4,\,2,\,0,\,2)^{\top}$ se tiene $\mathbf{q}_1^{\top}\mathbf{x}=4$, $\mathbf{q}_2^{\top}\mathbf{x}=4/\sqrt2=2\sqrt2$, $\mathbf{q}_3^{\top}\mathbf{x}=0$ y $\mathbf{q}_4^{\top}\mathbf{x}=0$: la señal consta solo de componente continua y coseno.

La segunda fórmula de [(1.2)](#gl-1-2) dice que la energía $\lVert\mathbf{x}\rVert^2=24$ de la señal es igual a la suma de los cuadrados de las contribuciones, $16+8+0+0=24$. En procesamiento de señales, este enunciado se llama teorema de Parseval. La transformada discreta de Fourier es la misma descomposición con oscilaciones complejas. Su matriz para $N$ muestras conserva las longitudes exactamente cuando se normaliza con $1/\sqrt N$; sin ese factor, en el teorema de Parseval aparece además el factor $N$.
:::

### Matrices ortogonales

<span class="anker" id="stufe-1-4"></span>

Si se escriben los vectores de una base ortonormal como columnas de una matriz $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$, las dos fórmulas [(1.2)](#gl-1-2) pueden escribirse como productos de matrices. Todas las coordenadas a la vez forman, según la visión por filas de [Fundamentos 1, sección 7.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2), el vector $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, pues las filas de $\mathbf{Q}^{\top}$ son los vectores $\mathbf{q}_i^{\top}$. A la inversa, $\mathbf{x}=\sum_ic_i\mathbf{q}_i=\mathbf{Q}\mathbf{c}$ según la visión por columnas. La matriz $\mathbf{Q}^{\top}$ deshace, por tanto, lo que hace $\mathbf{Q}$.

:::definition Definición 1.5 (Matriz ortogonal)
<span class="anker" id="satz-1-5"></span>

Una matriz cuadrada $\mathbf{Q}\in\mathbb{R}^{n\times n}$ cuyas columnas son ortonormales se llama __matriz ortogonal__. De forma equivalente: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.
:::

Las dos formulaciones son equivalentes porque la entrada $(i,l)$ de $\mathbf{Q}^{\top}\mathbf{Q}$ es el producto escalar $\mathbf{q}_i^{\top}\mathbf{q}_l$ de las columnas $i$ y $l$. La condición $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ es, por tanto, exactamente [(1.1)](#gl-1-1).

:::satz Teorema 1.6 (La inversa de una matriz ortogonal)
<span class="anker" id="satz-1-6"></span>

Si $\mathbf{Q}$ es ortogonal, $\mathbf{Q}$ es invertible con $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$. Además, $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$; también las filas de $\mathbf{Q}$ son, por tanto, ortonormales, y $\mathbf{Q}^{\top}$ también es ortogonal.
:::

:::beweis Inversa de una matriz ortogonal
Las columnas son ortonormales y, según la primera subsección, linealmente independientes. Por el teorema de [Fundamentos 1, sección 13.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), $\mathbf{Q}$ es, por ello, invertible. Si se multiplica $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ por la derecha por $\mathbf{Q}^{-1}$, se obtiene $\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, y con ello también $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{Q}\mathbf{Q}^{-1}=\mathbf{I}$.
:::

Una observación sobre el nombre. Una matriz ortogonal tiene columnas ortonormales, no meramente ortogonales; el nombre es fruto de la historia. Las matrices cuyas columnas solo son ortogonales, pero no están normalizadas, no tienen un nombre propio. Para ellas, $\mathbf{Q}^{\top}\mathbf{Q}$ es una matriz diagonal con los cuadrados de las longitudes de las columnas en la diagonal, pero no $\mathbf{I}$.

::::beispiel [Ejemplo numérico]
Con los vectores de la primera subsección como columnas se tiene

$$\mathbf{Q}=\begin{pmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{pmatrix},\qquad \mathbf{Q}^{\top}\mathbf{Q}=\begin{pmatrix}0{,}36+0{,}64&-0{,}48+0{,}48\\-0{,}48+0{,}48&0{,}64+0{,}36\end{pmatrix}=\mathbf{I} .$$

Las entradas de $\mathbf{Q}^{\top}\mathbf{Q}$ son los productos escalares de las columnas de la primera subsección; la entrada fuera de la diagonal la muestra la fig. [1](#abb-1). Por tanto, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, sin cálculo alguno. Esta matriz es la matriz de rotación de [Fundamentos 1, sección 8.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3), con $\cos\alpha=0{,}6$ y $\sin\alpha=0{,}8$, es decir, una rotación de $\alpha\approx53{,}13^\circ$ en sentido antihorario. La inversa $\mathbf{Q}^{\top}$ gira el mismo ángulo en sentido contrario.
::::

⁠**En resumen:** Una matriz ortogonal es cuadrada y tiene columnas ortonormales; su inversa es simplemente su traspuesta.

### Se conservan las longitudes y los ángulos

<span class="anker" id="stufe-1-5"></span>

Una rotación no cambia ni la longitud de una flecha ni el ángulo entre dos flechas. Todas las matrices ortogonales tienen esta propiedad, y es la razón por la que se trabaja tan a gusto con ellas.

:::satz Teorema 1.7 (Las matrices ortogonales conservan los productos escalares)
<span class="anker" id="satz-1-7"></span>

Si $\mathbf{Q}$ es ortogonal, para todos los $\mathbf{x},\mathbf{y}\in\mathbb{R}^n$ se cumple

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{y},\qquad \lVert\mathbf{Q}\mathbf{x}\rVert=\lVert\mathbf{x}\rVert , \tag{1.3}$$

y el ángulo entre $\mathbf{Q}\mathbf{x}$ y $\mathbf{Q}\mathbf{y}$ es el mismo que entre $\mathbf{x}$ y $\mathbf{y}$. El determinante es $\det\mathbf{Q}=1$ o $\det\mathbf{Q}=-1$.
:::

:::beweis Conservación de los productos escalares
Según la regla $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ de [Fundamentos 1, sección 10.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1), se tiene $(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{y}=\mathbf{x}^{\top}\mathbf{I}\mathbf{y}=\mathbf{x}^{\top}\mathbf{y}$. Con $\mathbf{y}=\mathbf{x}$ se obtiene la afirmación sobre la longitud, y como el ángulo se calcula solo a partir de productos escalares y longitudes, tampoco cambia. Para el determinante se usan las reglas de cálculo de [Fundamentos 1, sección 14.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5): $1=\det\mathbf{I}=\det(\mathbf{Q}^{\top}\mathbf{Q})=\det\mathbf{Q}^{\top}\cdot\det\mathbf{Q}=(\det\mathbf{Q})^2$.
:::

Una matriz ortogonal mueve, por tanto, el espacio de forma rígida, sin deformarlo. Si $\det\mathbf{Q}=1$, es una rotación. Si $\det\mathbf{Q}=-1$, contiene una reflexión, pues según [Fundamentos 1, sección 14.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-2), un determinante negativo invierte la orientación.

::::beispiel [Ejemplo numérico]
La rotación de la subsección anterior transforma $\mathbf{x}=(3,\,1)^{\top}$ en $\mathbf{Q}\mathbf{x}=(1{,}8-0{,}8;\ 2{,}4+0{,}6)^{\top}=(1,\,3)^{\top}$. El cuadrado de la longitud de ambos vectores es $10$. El determinante de la rotación es $0{,}36+0{,}64=1$. La matriz $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ también tiene columnas ortonormales, pero su determinante es $-0{,}36-0{,}64=-1$: refleja respecto a la recta en la dirección de $(2,\,1)^{\top}$, pues transforma $(2,\,1)^{\top}$ en sí mismo y $(-1,\,2)^{\top}$ en $(1,\,-2)^{\top}$.
::::

⁠**En resumen:** Las matrices ortogonales conservan productos escalares, longitudes y ángulos; giran o reflejan, y su determinante es $\pm1$.

:::hintergrund Por qué en cálculo numérico se prefiere trabajar con matrices ortogonales
Un ordenador calcula con números redondeados: cada resultado intermedio lleva un pequeño error $\boldsymbol{\delta}$. Si se multiplica un resultado intermedio así por una matriz, el error también queda multiplicado por ella. Una matriz cualquiera puede aumentarlo al hacerlo; una ortogonal no, pues según [(1.3)](#gl-1-3) es $\lVert\mathbf{Q}\boldsymbol{\delta}\rVert=\lVert\boldsymbol{\delta}\rVert$. Por eso, los procedimientos de cálculo que solo constan de multiplicaciones por matrices ortogonales no dejan que crezcan los errores de redondeo. Por la misma razón, la inversa no supone ningún problema: no hace falta calcularla, basta con la traspuesta, y esta es exacta.
:::

### Matrices con columnas ortonormales

<span class="anker" id="stufe-1-6"></span>

A menudo se tienen menos vectores ortonormales que dimensiones tiene el espacio. Un plano de $\mathbb{R}^3$ tiene una base ortonormal de dos vectores. Si se escriben como columnas de una matriz, esta no es cuadrada, sino que tiene tres filas y dos columnas. Una parte de las reglas de cálculo sigue valiendo, otra no, y la diferencia es importante.

:::satz Teorema 1.8 (Matrices rectangulares con columnas ortonormales)
<span class="anker" id="satz-1-8"></span>

Si $\mathbf{Q}\in\mathbb{R}^{n\times k}$ tiene columnas ortonormales y $k<n$, se cumple $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_k$ y $\lVert\mathbf{Q}\mathbf{c}\rVert=\lVert\mathbf{c}\rVert$ para todo $\mathbf{c}\in\mathbb{R}^k$. La matriz $\mathbf{Q}\mathbf{Q}^{\top}\in\mathbb{R}^{n\times n}$, en cambio, no es la matriz identidad.
:::

:::beweis Matrices rectangulares
Las dos primeras afirmaciones se deducen de [(1.1)](#gl-1-1) exactamente igual que en las matrices cuadradas. Para la tercera: la matriz $\mathbf{Q}^{\top}$ tiene $k$ filas y $n$ columnas. Según el teorema del rango de [Fundamentos 1, sección 13.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), su núcleo tiene dimensión $n-\operatorname{rango}\mathbf{Q}^{\top}\ge n-k\ge1$. Existe, por tanto, un vector $\mathbf{z}\ne\mathbf{0}$ con $\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}$, y para él $\mathbf{Q}\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}\ne\mathbf{z}$. Así pues, $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.
:::

::::beispiel [Ejemplo numérico 1]
La matriz con la única columna $\mathbf{q}=(0{,}6;\ 0{,}8)^{\top}$ cumple $\mathbf{q}^{\top}\mathbf{q}=1$, pero

$$\mathbf{q}\mathbf{q}^{\top}=\begin{pmatrix}0{,}36&0{,}48\\0{,}48&0{,}64\end{pmatrix}\ne\mathbf{I} .$$

Transforma $(-0{,}8;\ 0{,}6)^{\top}$ en $\mathbf{0}$. El vector $\mathbf{x}=(3,\,1)^{\top}$ lo transforma en $(1{,}08+0{,}48;\ 1{,}44+0{,}64)^{\top}=(1{,}56;\ 2{,}08)^{\top}$. Es exactamente el extremo de la sombra de $\mathbf{x}$ de [Fundamentos 1, sección 5.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), pues $\mathbf{q}\mathbf{q}^{\top}\mathbf{x}=\mathbf{q}\,(\mathbf{q}^{\top}\mathbf{x})=2{,}6\,\mathbf{q}$.
::::

::::beispiel [Ejemplo numérico 2]
Las columnas de $\mathbf{Q}=\Bigl(\begin{smallmatrix}1&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ son $\mathbf{e}_1$ y $\mathbf{e}_2$ en $\mathbb{R}^3$. Se tiene $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_2$, pero $\mathbf{Q}\mathbf{Q}^{\top}=\operatorname{diag}(1;\,1;\,0)$. Esta matriz conserva las dos primeras componentes y pone la tercera a cero.
::::

⁠**En resumen:** En una matriz rectangular con columnas ortonormales, $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, pero $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$: el producto en este orden desecha una parte del vector.

:::aufgabe Ejercicio 1 ★ Ortonormalidad y coordenadas
<span class="anker" id="aufg-1"></span>

Se dan $\mathbf{q}_1=\tfrac13(1,\,2,\,2)^{\top}$, $\mathbf{q}_2=\tfrac13(2,\,1,\,-2)^{\top}$ y $\mathbf{q}_3=\tfrac13(2,\,-2,\,1)^{\top}$.

<ol class="al">

<li>

Comprueba que los tres vectores son ortonormales.

</li>

<li>

Calcula las coordenadas de $\mathbf{x}=(3,\,0,\,3)^{\top}$ en esta base ortonormal y haz la comprobación. Comprueba la fórmula para $\lVert\mathbf{x}\rVert^2$.

</li>

</ol>

:::loesung
(a) Se calculan los seis productos escalares; el factor común $\tfrac13\cdot\tfrac13=\tfrac19$ va delante:

$$\mathbf{q}_1^{\top}\mathbf{q}_1=\tfrac19(1+4+4)=1,\quad \mathbf{q}_2^{\top}\mathbf{q}_2=\tfrac19(4+1+4)=1,\quad \mathbf{q}_3^{\top}\mathbf{q}_3=\tfrac19(4+4+1)=1,$$

$$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac19(2+2-4)=0,\quad \mathbf{q}_1^{\top}\mathbf{q}_3=\tfrac19(2-4+2)=0,\quad \mathbf{q}_2^{\top}\mathbf{q}_3=\tfrac19(4-2-2)=0 .$$

Los tres tienen longitud $1$ y son perpendiculares dos a dos: son ortonormales y, según la sección [1.2](#stufe-1-2), forman por tanto una base ortonormal de $\mathbb{R}^3$.

(b) Según [(1.2)](#gl-1-2), las coordenadas son productos escalares, sin sistema de ecuaciones:

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=\tfrac13(3+0+6)=3,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=\tfrac13(6+0-6)=0,\qquad c_3=\mathbf{q}_3^{\top}\mathbf{x}=\tfrac13(6+0+3)=3 .$$

Comprobación: $3\mathbf{q}_1+0\cdot\mathbf{q}_2+3\mathbf{q}_3=(1,\,2,\,2)^{\top}+(2,\,-2,\,1)^{\top}=(3,\,0,\,3)^{\top}=\mathbf{x}$. Fórmula de la longitud: $c_1^2+c_2^2+c_3^2=9+0+9=18$ y $\lVert\mathbf{x}\rVert^2=9+0+9=18$.
:::
:::

:::aufgabe Ejercicio 2 ★ Una matriz ortogonal
<span class="anker" id="aufg-2"></span>

Sea $\mathbf{Q}$ la matriz con las columnas $\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3$ del ejercicio [1](#aufg-1).

<ol class="al">

<li>

Da $\mathbf{Q}^{-1}$ sin hacer cálculos. Comprueba $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ en una entrada de tu elección fuera de la diagonal.

</li>

<li>

Calcula $\mathbf{Q}\,(1,\,1,\,1)^{\top}$ y compara las longitudes. Calcula $\det\mathbf{Q}$. ¿Gira o refleja $\mathbf{Q}$?

</li>

</ol>

:::loesung
(a) Las columnas son ortonormales; por tanto, $\mathbf{Q}$ es ortogonal y $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, sin hacer cálculos. Aquí

$$\mathbf{Q}=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}$$

es incluso simétrica; por tanto, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}=\mathbf{Q}$. La entrada $(1,2)$ de $\mathbf{Q}\mathbf{Q}^{\top}$ es el producto escalar de la primera fila por la segunda: $\tfrac19(1\cdot2+2\cdot1+2\cdot(-2))=0$.

(b) $\mathbf{Q}\,(1,\,1,\,1)^{\top}=\tfrac13(5,\,1,\,1)^{\top}$, con el cuadrado de la longitud $\tfrac19(25+1+1)=3$, exactamente el cuadrado de la longitud de $(1,\,1,\,1)^{\top}$, como exige [(1.3)](#gl-1-3). El determinante es

$$\det\mathbf{Q}=\tfrac1{27}\bigl(1\cdot(1-4)-2\cdot(2+4)+2\cdot(-4-2)\bigr)=\tfrac1{27}(-3-12-12)=-1 .$$

Así pues, $\mathbf{Q}$ refleja. Más exactamente: como $\mathbf{Q}=\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, se tiene $\mathbf{Q}^2=\mathbf{I}$; aplicada dos veces, todo vuelve a su sitio. El vector $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ se invierte, $\mathbf{Q}\mathbf{k}=\tfrac13(1-2-2,\ 2-1+2,\ 2+2-1)^{\top}=(-1,\,1,\,1)^{\top}=-\mathbf{k}$, y los vectores perpendiculares a $\mathbf{k}$ quedan fijos. $\mathbf{Q}$ es la reflexión respecto al plano $x_1-x_2-x_3=0$.
:::
:::

:::aufgabe Ejercicio 3 ★★ Cálculo con matrices ortogonales
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Demuestra: si $\mathbf{Q}_1$ y $\mathbf{Q}_2$ son ortogonales, también $\mathbf{Q}_1\mathbf{Q}_2$ es ortogonal.

</li>

<li>

¿Es la suma de dos matrices ortogonales de nuevo ortogonal? Justifícalo o da un contraejemplo.

</li>

<li>

Demuestra que una matriz diagonal es ortogonal si y solo si cada entrada diagonal es $1$ o $-1$. ¿Qué hace geométricamente una matriz así?

</li>

</ol>

:::loesung
(a) Con $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ se tiene $(\mathbf{Q}_1\mathbf{Q}_2)^{\top}(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^{\top}\mathbf{Q}_1^{\top}\mathbf{Q}_1\mathbf{Q}_2=\mathbf{Q}_2^{\top}\mathbf{I}\mathbf{Q}_2=\mathbf{I}$. Intuitivamente: dos movimientos rígidos seguidos son de nuevo un movimiento rígido.

(b) No. Contraejemplo: $\mathbf{I}+\mathbf{I}=2\mathbf{I}$, y $(2\mathbf{I})^{\top}(2\mathbf{I})=4\mathbf{I}\ne\mathbf{I}$; la suma duplica todas las longitudes. Del mismo modo, $\mathbf{I}+(-\mathbf{I})$ es la matriz nula.

(c) Para $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$ es $\mathbf{D}^{\top}\mathbf{D}=\operatorname{diag}(d_1^2,\dots,d_n^2)$. Esto es $\mathbf{I}$ si y solo si cada $d_i^2=1$, es decir, $d_i=1$ o $d_i=-1$. Una matriz así invierte los ejes con $d_i=-1$ y deja los demás como están: refleja respecto a los planos coordenados. Por ejemplo, $\operatorname{diag}(1;\,-1)$ refleja respecto al eje $x_1$, y $\operatorname{diag}(-1;\,-1)$ es la rotación de $180^\circ$.
:::
:::
