---
title: Vectores: datos como listas de números
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Capítulo 1: Vectores y matrices
nachschlagen: ja
order: 15210200
summary: Un ordenador solo sabe manejar números.
tags: índice, signo de sumatorio, índice de sumación, suma doble, característica, ejemplo, conjunto de datos, vector
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Un ordenador solo sabe manejar números. Esta sección aclara cómo se describe una cosa del mundo real mediante una lista de números y qué cálculos están permitidos con tales listas.
:::

:::::vorwissen Lo que necesitas: el signo de sumatorio y los índices

<span class="anker" id="stufe-1-1"></span>

En este capítulo se suman constantemente muchos números. Para no tener que escribir cada vez «$a_1+a_2+\dots$», existe una notación abreviada.

**Índices.** Si se tienen varios números del mismo tipo, se numeran correlativamente: $a_1,a_2,\dots,a_n$. El número escrito como subíndice se llama __índice__. Solo indica qué lugar ocupa el número en cuestión y no tiene nada que ver con su valor.

**El signo de sumatorio.** Para la suma de $a_1$ a $a_n$ se escribe

<span class="anker" id="gl-1-1"></span>
$$\sum_{i=1}^{n} a_i = a_1+a_2+\dots+a_n , \tag{1.1}$$

que se lee «suma de $a_i$ para $i$ desde $1$ hasta $n$». La gran sigma griega se llama __signo de sumatorio__. La letra $i$ que hay debajo es el __índice de sumación__: toma sucesivamente los valores $1,2,\dots,n$, y por cada valor se añade un sumando. El índice de sumación es un marcador de posición. Llamarlo $i$, $j$ o $k$ no cambia la suma: $\sum_{i=1}^n a_i=\sum_{j=1}^n a_j$.

**Dos reglas de cálculo.** Una suma con signo de sumatorio no es más que una suma ordinaria de un número finito de números, escrita de forma abreviada. Por eso valen para ella las reglas conocidas: se puede sacar factor común (propiedad distributiva) y reordenar y agrupar los sumandos a voluntad (propiedades conmutativa y asociativa). Escrito con el signo de sumatorio, esto significa que un factor común puede ponerse delante de la suma y que una suma de sumas puede separarse:

<span class="anker" id="gl-1-2"></span>
$$\sum_{i=1}^n c\,a_i=c\sum_{i=1}^n a_i ,\qquad \sum_{i=1}^n (a_i+b_i)=\sum_{i=1}^n a_i+\sum_{i=1}^n b_i . \tag{1.2}$$

**Sumas dobles.** Los números dispuestos en una tabla llevan dos índices: $a_{ij}$ es el número de la fila $i$ y la columna $j$. La suma de todas las entradas de una tabla con $m$ filas y $n$ columnas se escribe como __suma doble__

$$\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij} .$$

Se lee de dentro hacia fuera: para cada fila $i$, la suma interior suma los números de esa fila; la suma exterior suma las sumas de las filas. Como con un número finito de sumandos el orden no importa, se pueden intercambiar los dos signos de sumatorio y sumar primero por columnas.

::::beispiel [Ejemplo numérico 1]
Para $a_1=2$, $a_2=5$, $a_3=1$, cada suma se escribe primero desarrollada; después se sustituyen los números y se suma (fig. [1](#abb-1)). Así, $\sum_{i=1}^3 a_i=8$ y $\sum_{i=1}^3 a_i^2=30$. En la tercera suma, el propio índice de sumación es el sumando: $\sum_{j=1}^{3}j=6$.

:::abbildung ml/k1rsumme 1
Tres sumas paso a paso: desarrollar el signo de sumatorio, sustituir los números, sumar.
:::
::::

::::beispiel [Ejemplo numérico 2]
La tabla con las filas $(1,\,2)$ y $(3,\,4)$ tiene las entradas $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=4$. Sumando por filas, la suma doble da $(1+2)+(3+4)=10$; por columnas, $(1+3)+(2+4)=10$ (fig. [2](#abb-2)).

:::abbildung ml/k1rdoppel 2
La suma doble sobre la tabla con las filas $(1,\,2)$ y $(3,\,4)$: arriba, primero por filas; abajo, primero por columnas. Ambos órdenes dan la misma suma.
:::
::::

⁠**En resumen:** $\sum_{i=1}^n a_i$ es la suma de $a_1$ a $a_n$; el índice de sumación $i$ es solo un marcador de posición.

:::::

### Ejemplos y características

<span class="anker" id="stufe-1-2"></span>

Quien quiere aprender a partir de datos tiene primero ante sí una colección de cosas del mismo tipo: viviendas, pacientes, cartas, mediciones en una máquina. Cada cosa se describe mediante las mismas magnitudes medidas. Las viviendas, por ejemplo, mediante su superficie, el número de habitaciones y la distancia al centro de la ciudad. Si se anota esto para varias viviendas, se obtiene una tabla (tabla [1](#tab-1)), que acompaña a todo el capítulo.

<span class="anker" id="tab-1"></span>

**Tabla 1:** El conjunto de datos de viviendas de este capítulo: cuatro viviendas, cada una descrita por tres características. Los números son inventados.

|  | Superficie en $\mathrm{m}^2$ | Habitaciones | Distancia al centro en km |
|---|---|---|---|
| Vivienda 1 | 60 | 2 | 3 |
| Vivienda 2 | 40 | 1 | 1 |
| Vivienda 3 | 90 | 4 | 6 |
| Vivienda 4 | 70 | 3 | 2 |

Cada fila de la tabla corresponde a una cosa; cada columna, a una magnitud medida. Para ambas hay términos fijos.

:::definition Definición 1.1 (Característica, ejemplo, conjunto de datos)
<span class="anker" id="satz-1-1"></span>

Una __característica__ es una propiedad que puede expresarse mediante un número real.

Un __ejemplo__ es una cosa individual descrita por los valores de $d$ características.

Un __conjunto de datos__ es una colección de $N$ ejemplos, todos descritos por las mismas $d$ características.
:::

En toda la serie se cumple: $N$ es el número de ejemplos y $d$ el número de características. Los ejemplos se numeran con $i=1,\dots,N$; las características, con $j=1,\dots,d$.

Dos aclaraciones sobre los términos. En las bases de datos, una sola fila de una tabla se llama a menudo «registro»; aquí, el conjunto de datos es la colección entera. Y la palabra «ejemplo» designa en este capítulo siempre una cosa de un conjunto de datos; por eso, los cálculos resueltos paso a paso se llaman «ejemplo numérico».

::::beispiel [Ejemplo numérico]
El conjunto de datos de viviendas tiene $N=4$ ejemplos y $d=3$ características. La característica 2 es el número de habitaciones. En la vivienda 3 tiene el valor $4$.
::::

No toda propiedad es de por sí un número. El barrio de una vivienda es un nombre. Tales propiedades hay que traducirlas primero a números antes de poder calcular con ellas. En este capítulo, todas las características ya son números.

⁠**En resumen:** Un conjunto de datos consta de $N$ ejemplos, y cada ejemplo está descrito por las mismas $d$ características.

:::hintergrund Las mismas cosas con otros nombres
En los textos en inglés, un ejemplo se llama *example*, *sample*, *instance* o *data point*; una característica, *feature* o *attribute*; y el conjunto de datos, *dataset*. También en español son habituales «muestra», «instancia», «punto de datos» u «observación» para un ejemplo. Siempre se refieren a lo mismo: una fila de la tabla.
:::

### Vectores

<span class="anker" id="stufe-1-3"></span>

Para el ordenador, una vivienda no es otra cosa que sus tres números. Para poder calcular con estos tres números como con un único objeto, se reúnen en una lista. El orden es fijo: primero la superficie, después las habitaciones, después la distancia.

Una lista así también puede dibujarse si solo contiene dos números. Si de la vivienda 4 se toman solo el número de habitaciones $3$ y la distancia $2$, se obtiene el punto de coordenadas $(3,\,2)$ en un plano cuyo eje horizontal cuenta las habitaciones y cuyo eje vertical cuenta los kilómetros. La misma lista puede imaginarse también como una flecha que va del origen a ese punto (fig. [3](#abb-3)). Ambas imágenes describen los mismos dos números.

:::abbildung ml/k1punktpfeil 3
El vector $\mathbf{x}=(3,\,2)^{\top}$, a la izquierda como punto, a la derecha como flecha del origen a ese punto. Aquí $x_1$ representa el número de habitaciones y $x_2$ la distancia al centro en km de la vivienda 4.
:::

:::definition Definición 1.2 (Vector)
<span class="anker" id="satz-1-2"></span>

Un __vector__ $\mathbf{x}$ con $d$ componentes es una lista ordenada de $d$ números reales $x_1,\dots,x_d$, escritos uno debajo de otro:

$$\mathbf{x}=\begin{pmatrix}x_1\\\vdots\\x_d\end{pmatrix}.$$

El número $x_j$ se llama la $j$-ésima __componente__ de $\mathbf{x}$. El conjunto de todos los vectores con $d$ componentes se llama $\mathbb{R}^d$. Dos vectores son iguales si tienen el mismo número de componentes y todas las componentes coinciden en la misma posición.
:::

Los vectores se escriben en negrita y en minúscula; sus componentes, en tipo normal. Un único número real se llama, a diferencia de un vector, un __escalar__.

**Columna y fila.** En esta serie, un vector es siempre una columna. En el texto corrido, una columna ocupa mucho espacio. Por eso se escriben los números uno al lado de otro y se pone detrás un $\top$ en superíndice: $(x_1,\dots,x_d)^{\top}$ significa los mismos números como columna. El signo se lee __traspuesto__. Convierte una fila en una columna y una columna en una fila. A la inversa, $\mathbf{x}^{\top}=(x_1,\,\dots,\,x_d)$ es el vector $\mathbf{x}$ escrito como fila. Si un vector contiene números decimales, las componentes se separan con punto y coma, para no confundir la coma decimal con la coma separadora: $(0{,}2;\ 0{,}25;\ 0{,}3)^{\top}$ tiene tres componentes.

**Los ejemplos de un conjunto de datos.** El ejemplo número $i$ es el vector $\mathbf{x}_i\in\mathbb{R}^d$. El vector de un ejemplo se llama también su __vector de características__. Sus componentes llevan dos índices: $x_{ij}$ es el valor de la característica $j$ en el ejemplo $i$. Una letra en negrita con un índice es, por tanto, un vector entero de una lista de vectores; una letra normal con dos índices, un único número.

::::beispiel [Ejemplo numérico]
La vivienda 1 es el vector $\mathbf{x}_1=(60,\,2,\,3)^{\top}\in\mathbb{R}^3$. Su segunda componente es $x_{12}=2$. El vector $(2,\,60,\,3)^{\top}$ contiene los mismos números, pero es otro vector: en la primera posición está ahora el número $2$, y ese se leería como superficie.
::::

⁠**En resumen:** Un vector es una lista ordenada de números que puede dibujarse como punto o como flecha; un ejemplo con $d$ características es un vector de $\mathbb{R}^d$.

:::hintergrund Qué es en realidad un vector
Una lista de números es el vector con el que se calcula. En matemáticas, el concepto es más amplio: un vector es todo lo que puede sumarse y multiplicarse por un número sin salirse del tipo de objeto. Las flechas del plano entran en esta categoría, pero también las grabaciones de sonido. Una grabación de sonido registra, a intervalos iguales y muy cortos, cuánto se desvía en cada momento la presión del aire de su valor en reposo. Con $n$ de estos valores $x[0],\dots,x[n-1]$, es un vector de $\mathbb{R}^n$. Sumar dos grabaciones significa mezclarlas, y multiplicar una grabación por un número significa subirle o bajarle el volumen; ambas operaciones dan de nuevo una grabación de la misma longitud.

También una imagen es un vector. Una imagen en escala de grises de $28\times28$ píxeles consta de $784$ valores de luminosidad. Si se leen fila por fila, uno tras otro, la imagen es un punto de $\mathbb{R}^{784}$. Esta idea ya no puede dibujarse, pero se calcula con ella exactamente igual que con dos o tres componentes.
:::

### Suma y múltiplo

<span class="anker" id="stufe-1-4"></span>

Con listas de valores medidos se quiere calcular: sumar el consumo eléctrico de dos viviendas, convertir kilovatios hora en megavatios hora o ver en cuánto se diferencian dos viviendas. Todo ello se hace componente por componente.

En la imagen de las flechas, sumar significa colocar la segunda flecha en la punta de la primera. La flecha del origen a la nueva punta es la suma (fig. [4](#abb-4), izquierda). Multiplicar por un número significa alargar o acortar la flecha; un factor negativo, además, le da la vuelta (fig. [4](#abb-4), derecha).

:::abbildung ml/k1addition 4
Izquierda: $\mathbf{u}=(3,\,1)^{\top}$ más $\mathbf{v}=(1,\,2)^{\top}$. Si se coloca $\mathbf{v}$ en la punta de $\mathbf{u}$ (o $\mathbf{u}$ en la punta de $\mathbf{v}$, a trazos), se llega a $\mathbf{u}+\mathbf{v}=(4,\,3)^{\top}$. Derecha: $\mathbf{u}=(2,\,1)^{\top}$, el doble $2\mathbf{u}=(4,\,2)^{\top}$ (gris) y $-\mathbf{u}=(-2,\,-1)^{\top}$.
:::

:::definition Definición 1.3 (Suma y múltiplo)
<span class="anker" id="satz-1-3"></span>

Para dos vectores $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ y un escalar $c$, la __suma__ $\mathbf{u}+\mathbf{v}$ y el __múltiplo__ $c\,\mathbf{u}$ son los vectores con las componentes

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{u}+\mathbf{v})_j=u_j+v_j ,\qquad (c\,\mathbf{u})_j=c\,u_j ,\qquad j=1,\dots,d. \tag{1.3}$$

El __vector nulo__ $\mathbf{0}$ tiene solo ceros como componentes. Se escribe $-\mathbf{u}$ para $(-1)\,\mathbf{u}$ y $\mathbf{u}-\mathbf{v}$ para $\mathbf{u}+(-\mathbf{v})$.
:::

Solo se pueden sumar vectores con el mismo número de componentes. Además, solo tiene sentido si en la misma posición está la misma magnitud: kilovatios hora con kilovatios hora, no metros cuadrados con habitaciones.

Como cada componente es por sí sola un cálculo ordinario con números, valen las reglas conocidas: $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$, $(\mathbf{u}+\mathbf{v})+\mathbf{q}=\mathbf{u}+(\mathbf{v}+\mathbf{q})$, $c\,(\mathbf{u}+\mathbf{v})=c\,\mathbf{u}+c\,\mathbf{v}$, $(c+c')\,\mathbf{u}=c\,\mathbf{u}+c'\,\mathbf{u}$ y $\mathbf{u}+\mathbf{0}=\mathbf{u}$ para todos los vectores $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ y escalares $c,c'$.

La diferencia $\mathbf{u}-\mathbf{v}$ tiene una interpretación propia. Es la flecha que va de la punta de $\mathbf{v}$ a la punta de $\mathbf{u}$, pues $\mathbf{v}+(\mathbf{u}-\mathbf{v})=\mathbf{u}$. Para dos ejemplos, indica en cuánto se diferencian en cada característica.

::::beispiel [Ejemplo numérico]
La vivienda 1 ha consumido de enero a marzo $\mathbf{u}=(200,\,250,\,300)^{\top}$ kilovatios hora de electricidad; la vivienda 2, en el mismo edificio, $\mathbf{v}=(150,\,100,\,120)^{\top}$. Juntas consumen

$$\mathbf{u}+\mathbf{v}=(350,\,350,\,420)^{\top}\ \text{kWh}.$$

El consumo de la vivienda 1 en megavatios hora lo da el múltiplo $0{,}001\,\mathbf{u}=(0{,}2;\ 0{,}25;\ 0{,}3)^{\top}$. La diferencia $\mathbf{u}-\mathbf{v}=(50,\,150,\,180)^{\top}$ indica cuántos kilovatios hora más que la vivienda 2 consume la vivienda 1 en cada mes. En el conjunto de datos de viviendas, $\mathbf{x}_3-\mathbf{x}_1=(30,\,2,\,3)^{\top}$: la vivienda 3 es $30\,\mathrm m^2$ más grande, tiene dos habitaciones más y está $3$ km más lejos del centro que la vivienda 1.
::::

⁠**En resumen:** Los vectores se suman y se multiplican por un número componente por componente.

### Combinaciones lineales

<span class="anker" id="stufe-1-5"></span>

Casi todos los cálculos de este capítulo toman varios vectores, multiplican cada uno por un número propio y suman los resultados. Un promedio es un cálculo así; una mezcla, también.

En la imagen de las flechas: se recorre $c_1$ veces el trayecto $\mathbf{v}_1$, luego $c_2$ veces el trayecto $\mathbf{v}_2$, y así sucesivamente. El lugar al que se llega es el resultado.

:::definition Definición 1.4 (Combinación lineal)
<span class="anker" id="satz-1-4"></span>

Dados vectores $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ y escalares $c_1,\dots,c_k$, la suma

<span class="anker" id="gl-1-4"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\sum_{l=1}^{k}c_l\,\mathbf{v}_l \tag{1.4}$$

se llama una __combinación lineal__ de los vectores $\mathbf{v}_1,\dots,\mathbf{v}_k$. Los números $c_l$ se llaman sus __coeficientes__.
:::

Atención al leer: $\mathbf{v}_l$ está en negrita; es, por tanto, el $l$-ésimo vector de la lista, no la $l$-ésima componente de un vector.

::::beispiel [Ejemplo numérico 1]
$(1,\,2)^{\top}+3\,(0,\,1)^{\top}=(1,\,2)^{\top}+(0,\,3)^{\top}=(1,\,5)^{\top}$.
::::

::::beispiel [Ejemplo numérico 2] el punto medio
La combinación lineal $\tfrac12\mathbf{x}_1+\tfrac12\mathbf{x}_2$ de las viviendas 1 y 2 es

$$\tfrac12\,(60,\,2,\,3)^{\top}+\tfrac12\,(40,\,1,\,1)^{\top}=(50;\ 1{,}5;\ 2)^{\top}.$$

Es una vivienda imaginaria que, en cada característica, está exactamente a medio camino entre las dos. El punto está en el centro del segmento de unión.
::::

Hay una combinación lineal que se necesita con especial frecuencia en este capítulo. Si se toman todos los $N$ ejemplos con el coeficiente $1/N$, se obtiene la __media de los ejemplos__

<span class="anker" id="gl-1-5"></span>
$$\bar{\mathbf{x}}=\frac1N\sum_{i=1}^{N}\mathbf{x}_i . \tag{1.5}$$

Es un ejemplo imaginario que, en cada característica, tiene el promedio de todos los ejemplos: su componente $j$-ésima es la media de las $j$-ésimas características.

::::beispiel [Ejemplo numérico 3] la media de los ejemplos
Para el conjunto de datos de viviendas, $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$ (fig. [5](#abb-5)), la «vivienda media»: en promedio, $65\,\mathrm m^2$, $2{,}5$ habitaciones y $3$ km hasta el centro.

:::abbildung ml/k1rmittelvektor 5
La media de las cuatro viviendas: la suma de los vectores se forma componente por componente y después se divide por $4$; $5/2=2{,}5$.
:::
::::

⁠**En resumen:** Una combinación lineal multiplica cada vector por un número propio y lo suma todo.

:::hintergrund Dónde están las mezclas de dos puntos
Si para dos vectores $\mathbf{x}_1,\mathbf{x}_2$ se eligen los coeficientes de modo que su suma sea $1$, es decir, $(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2$ con un número $t$, el resultado está siempre en la recta que pasa por los dos puntos. En efecto, puede reescribirse como

$$(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2=\mathbf{x}_1+t\,(\mathbf{x}_2-\mathbf{x}_1) .$$

Es decir: partiendo del punto $\mathbf{x}_1$, avanzar $t$ veces la flecha de unión $\mathbf{x}_2-\mathbf{x}_1$. Para $t=0$ se está en $\mathbf{x}_1$; para $t=1$, en $\mathbf{x}_2$; para $t=\tfrac12$, en el centro. Todos los $t$ entre $0$ y $1$ dan los puntos del segmento de unión. Estas mezclas se necesitan siempre que se quieren obtener valores intermedios entre dos puntos de datos.
:::

### Los vectores unitarios

<span class="anker" id="stufe-1-6"></span>

Los vectores más sencillos tienen una única componente $1$ y, por lo demás, solo ceros. En un ejemplo significaría que solo una característica está «encendida», y además con el valor $1$. En el plano son las dos flechas de longitud $1$ a lo largo de los ejes.

:::definition Definición 1.5 (Vector unitario)
<span class="anker" id="satz-1-5"></span>

El $j$-ésimo __vector unitario__ $\mathbf{e}_j\in\mathbb{R}^d$ tiene un $1$ en la posición $j$ y un $0$ en todas las demás posiciones.
:::

En $\mathbb{R}^2$, $\mathbf{e}_1=(1,\,0)^{\top}$ y $\mathbf{e}_2=(0,\,1)^{\top}$. Todo vector es una combinación lineal de los vectores unitarios, y los coeficientes son exactamente sus componentes:

<span class="anker" id="gl-1-6"></span>
$$\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_d\mathbf{e}_d=\sum_{j=1}^d x_j\,\mathbf{e}_j . \tag{1.6}$$

Se ve calculando el lado derecho componente por componente: en la posición $j$ solo aporta algo el sumando $x_j\mathbf{e}_j$, y en concreto $x_j\cdot1$. Otros coeficientes no son posibles, pues darían en alguna posición un número distinto.

::::beispiel [Ejemplo numérico]
$\mathbf{x}_1=(60,\,2,\,3)^{\top}=60\,\mathbf{e}_1+2\,\mathbf{e}_2+3\,\mathbf{e}_3$, es decir, $60$ veces «un metro cuadrado» más $2$ veces «una habitación» más $3$ veces «un kilómetro».
::::

⁠**En resumen:** El vector unitario $\mathbf{e}_j$ tiene un uno en la posición $j$ y ceros en las demás; todo vector es la suma $\sum_jx_j\mathbf{e}_j$.

:::aufgabe Ejercicio 1 ★ Leer y escribir sumas
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Calcula $\sum_{i=1}^{5}(2i-1)$ y $\sum_{i=1}^{2}\sum_{j=1}^{3}i\,j$.

</li>

<li>

Escribe $3+6+9+12$ con un signo de sumatorio.

</li>

<li>

Sea $a_i$ la superficie de la vivienda $i$ de la tabla [1](#tab-1). ¿Qué significan $\sum_{i=1}^4a_i$ y $\frac14\sum_{i=1}^4a_i$, y qué números salen?

</li>

</ol>

:::loesung
(a) El índice de sumación $i$ toma los valores de $1$ a $5$, y los sumandos son los números impares $1,3,5,7,9$:

$$\sum_{i=1}^{5}(2i-1)=1+3+5+7+9=25 .$$

En la suma doble, para cada $i$ fijo, la suma interior es $\sum_{j=1}^3i\,j=i\,(1+2+3)=6i$; el factor $i$ no depende de $j$ y, según [(1.2)](#gl-1-2), puede ponerse delante de la suma interior. Después, $\sum_{i=1}^2 6i=6+12=18$.

(b) Los sumandos son los múltiplos de $3$: $3+6+9+12=\sum_{i=1}^43i$. Igual de correcto es $3\sum_{i=1}^4i$, según la regla de los factores comunes.

(c) $\sum_{i=1}^4a_i=60+40+90+70=260$ es la superficie total de las cuatro viviendas en $\mathrm m^2$, y $\frac14\sum_{i=1}^4a_i=65$ es la superficie media de una vivienda.
:::
:::

:::aufgabe Ejercicio 2 ★ Calcular con vectores
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Calcula $2\mathbf{u}-3\mathbf{v}$ para $\mathbf{u}=(1,\,-1,\,0)^{\top}$ y $\mathbf{v}=(0,\,1,\,2)^{\top}$.

</li>

<li>

Escribe $(4,\,-1,\,2)^{\top}$ como combinación lineal de los vectores unitarios de $\mathbb{R}^3$.

</li>

<li>

Encuentra números $c_1,c_2$ con $c_1(1,\,2)^{\top}+c_2(2,\,1)^{\top}=(3,\,3)^{\top}$. Dibuja la solución con flechas.

</li>

<li>

Calcula $\mathbf{x}_3-\mathbf{x}_2$ para el conjunto de datos de viviendas y describe con palabras lo que expresa el vector.

</li>

</ol>

:::loesung
(a) Componente a componente: $2\mathbf{u}=(2,\,-2,\,0)^{\top}$ y $3\mathbf{v}=(0,\,3,\,6)^{\top}$, así que $2\mathbf{u}-3\mathbf{v}=(2,\,-5,\,-6)^{\top}$.

(b) Según [(1.6)](#gl-1-6), los coeficientes son las componentes: $(4,\,-1,\,2)^{\top}=4\,\mathbf{e}_1-\mathbf{e}_2+2\,\mathbf{e}_3$.

(c) Componente a componente, la condición dice $c_1+2c_2=3$ y $2c_1+c_2=3$. Si se resta dos veces la primera ecuación de la segunda, queda $-3c_2=-3$, es decir, $c_2=1$ y, después, $c_1=1$. Comprobación: $(1,\,2)^{\top}+(2,\,1)^{\top}=(3,\,3)^{\top}$. En el dibujo se coloca la flecha $(2,\,1)^{\top}$ en la punta de $(1,\,2)^{\top}$ y se llega a $(3,\,3)^{\top}$.

(d) $\mathbf{x}_3-\mathbf{x}_2=(90-40,\ 4-1,\ 6-1)^{\top}=(50,\,3,\,5)^{\top}$: la vivienda 3 tiene $50\,\mathrm m^2$ más que la vivienda 2, tres habitaciones más y está $5$ km más lejos del centro. El vector es la flecha que va del punto $\mathbf{x}_2$ al punto $\mathbf{x}_3$.
:::
:::

:::aufgabe Ejercicio 3 ★ Un conjunto de datos propio
<span class="anker" id="aufg-3"></span>

Elige cuatro cosas de tu vida cotidiana, por ejemplo alimentos, bicicletas o canciones, y tres propiedades que puedas indicar como número para cada cosa. Mide o busca los valores.

<ol class="al">

<li>

Crea la tabla. ¿Cuánto valen $N$ y $d$? Escribe el segundo ejemplo como vector $\mathbf{x}_2$.

</li>

<li>

¿Qué propiedad que también te interesaría no es un número? ¿Cómo podría traducirse a números?

</li>

<li>

Calcula la media de los ejemplos $\bar{\mathbf{x}}$. ¿Hay alguna cosa que tenga exactamente ese aspecto?

</li>

</ol>

:::loesung
Una solución posible: cuatro manzanas con las características masa en g, diámetro en cm y precio en céntimos.

(a) Supongamos que la tabla tiene las filas $(180;\ 7{,}5;\ 45)$, $(150;\ 7{,}0;\ 40)$, $(210;\ 8{,}0;\ 55)$ y $(165;\ 7{,}2;\ 40)$. Entonces $N=4$ y $d=3$, y $\mathbf{x}_2=(150;\ 7{,}0;\ 40)^{\top}$. Lo único importante es que cada cosa se describa con las mismas tres características en el mismo orden.

(b) La variedad es un nombre, no un número. Puede traducirse introduciendo para cada variedad una característica propia que vale $1$ si la manzana es de esa variedad y $0$ en caso contrario. Numerar sin más las variedades, en cambio, no suele ser buena idea: los números simulan un orden y unas distancias que entre variedades no existen.

(c) La media de los ejemplos es, componente a componente, el promedio; aquí, $\bar{\mathbf{x}}=(176{,}25;\ 7{,}425;\ 45)^{\top}$. En la tabla no hay ninguna manzana con exactamente estos valores. La media es un ejemplo imaginario, no medido, y en una propiedad como el número de habitaciones puede ser incluso un valor que ninguna cosa real puede tomar, por ejemplo $2{,}5$ habitaciones.
:::
:::
