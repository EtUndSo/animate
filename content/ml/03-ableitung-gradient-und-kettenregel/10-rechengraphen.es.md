---
title: Grafos computacionales
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15231000
summary: Las fórmulas largas las evalúa un ordenador paso a paso, y cada paso es una operación sencilla con derivada conocida.
tags: grafo computacional, evaluación hacia adelante, derivada local
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Las fórmulas largas las evalúa un ordenador paso a paso, y cada paso es una operación sencilla con derivada conocida. Un grafo computacional hace visibles estos pasos y sus dependencias. Esta sección dibuja un grafo así, lo evalúa hacia adelante en forma de tabla y escribe en cada arista su derivada local. Con ello queda todo preparado para calcular mecánicamente las derivadas del resultado respecto de todas las entradas.
:::

### Resultados intermedios

<span class="anker" id="stufe-9-1"></span>

Con las reglas de la sección [1.4](die-ableitung.html#stufe-1-4) puede derivarse cualquier fórmula formada por operaciones aritméticas básicas y funciones conocidas. Pero si se escribe el resultado como fórmula, a menudo resulta mucho más largo que la propia función. Según la regla del producto, un producto de $n$ factores tiene una derivada formada por $n$ sumandos de $n$ factores cada uno; la fórmula crece, pues, con $n^2$, mientras que la función solo tiene $n$ factores. Con resultados intermedios, en cambio, el cálculo sigue siendo pequeño. Tras cada paso se guardan el valor y la derivada obtenidos hasta ese momento, y se sigue calculando con números, no con fórmulas.

::::beispiel [Ejemplo numérico]
Sea $p(x)=(x+1)(x+2)(x+3)(x+4)$; se busca $p'(0)$. La regla del producto escrita explícitamente da cuatro sumandos, en cada uno de los cuales un factor se ha sustituido por su derivada $1$:

$$p'(0)=2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3=24+12+8+6=50$$

(fig. [17](#abb-17)). Paso a paso, con los productos parciales $p_1=x+1$, $p_k=p_{k-1}\cdot(x+k)$ y la regla del producto $p_k'=p_{k-1}'\cdot(x+k)+p_{k-1}\cdot1$, se procede así:

$$\begin{gathered} p_1=1,\quad p_1'=1;\qquad p_2=1\cdot2=2,\quad p_2'=1\cdot2+1\cdot1=3;\\ p_3=2\cdot3=6,\quad p_3'=3\cdot3+2\cdot1=11;\qquad p_4=6\cdot4=24,\quad p_4'=11\cdot4+6\cdot1=50 . \end{gathered}$$

Cada paso cuesta dos multiplicaciones y una suma, sin importar cuántos factores se hayan procesado ya.

:::abbildung ml/k3rvierfaktoren 17
La regla del producto escrita explícitamente para $p(x)=(x+1)(x+2)(x+3)(x+4)$ en el punto $0$: en el sumando $k$, el factor $x+k$ se ha sustituido por su derivada $1$.
:::
::::

⁠**En resumen:** Las fórmulas de derivadas escritas explícitamente se vuelven enseguida mucho más largas que la función; con resultados intermedios guardados como números, el coste por paso sigue siendo pequeño.

### El grafo computacional

<span class="anker" id="stufe-9-2"></span>

Qué resultados intermedios tiene un cálculo y de qué depende cada uno lo muestra con mayor claridad una imagen de nodos y flechas. Una flecha de un nodo $a$ a un nodo $b$ significa: $a$ se necesita para calcular $b$.

:::definition Definición 9.1 (Grafo computacional)
<span class="anker" id="satz-9-1"></span>

Un __grafo computacional__ consta de nodos y aristas dirigidas, es decir, flechas entre nodos. Cada nodo representa un número o, en cálculos mayores, un vector entero o una matriz. Los nodos de entrada son las entradas del cálculo; cualquier otro nodo $v$ surge mediante una operación elemental a partir de los nodos de los que parte una arista hacia $v$. Estos se llaman predecesores de $v$, y $v$ se llama su sucesor. Si se siguen las aristas, nunca se vuelve a un nodo por el que ya se ha pasado; un grafo así se llama acíclico. Un nodo distinguido es el resultado.
:::

Las operaciones elementales son las operaciones aritméticas básicas y las funciones de una variable, como el cuadrado, la función exponencial o la función logística. Como el grafo es acíclico, los nodos siempre pueden ordenarse de modo que cada nodo venga después de sus predecesores; en ese orden se calcula. Un programa de cálculo con bucles y bifurcaciones da también, para valores de entrada concretos, un grafo así: un bucle que se recorre tres veces aporta tres veces seguidas los mismos nodos.

::::beispiel [Ejemplo numérico]
El ejemplo de esta sección y de la siguiente es

<span class="anker" id="gl-9-1"></span>
$$f(x_1,x_2,x_3)=(x_1+x_2)\,(x_2+x_3) \tag{9.1}$$

con los resultados intermedios $v_1=x_1+x_2$ y $v_2=x_2+x_3$ y el resultado $f=v_1\cdot v_2$. El grafo tiene tres nodos de entrada, dos nodos de suma y un nodo de producto, unidos por seis aristas (fig. [18](#abb-18)). La entrada $x_2$ tiene dos sucesores; el grafo se ramifica ahí.

:::abbildung ml/k3graph 18
El grafo computacional de $f=(x_1+x_2)\,(x_2+x_3)$. Las flechas apuntan en el sentido del cálculo, y los círculos contienen la operación elemental. En verde, los valores de la evaluación hacia adelante en el punto $(1,\,2,\,3)$.
:::
::::

⁠**En resumen:** Un grafo computacional descompone un cálculo en operaciones elementales; sus aristas muestran qué valor entra en qué otro, y como es acíclico, siempre hay un orden en el que puede calcularse.

### La evaluación hacia adelante

<span class="anker" id="stufe-9-3"></span>

Evaluar un grafo computacional significa calcular los nodos en un orden en el que cada nodo venga después de sus predecesores. Si se escriben los pasos uno debajo de otro, surge una tabla que también se necesita para las derivadas: se guardan todos los valores, no solo el resultado.

:::definition Definición 9.2 (Evaluación hacia adelante)
<span class="anker" id="satz-9-2"></span>

La __evaluación hacia adelante__ de un grafo computacional calcula todos los nodos en un orden en el que cada nodo viene después de sus predecesores, y guarda cada valor.
:::

::::beispiel [Ejemplo numérico]
Para [(9.1)](#gl-9-1) en el punto $(1,\,2,\,3)$ resulta la tabla [3](#tab-3).

<span class="anker" id="tab-3"></span>

**Tabla 3:** La evaluación hacia adelante para $f=(x_1+x_2)\,(x_2+x_3)$ en el punto $(1,\,2,\,3)$.

| Nodo | Cálculo | Valor |
|---|---|---|
| $x_1$ | entrada | $1$ |
| $x_2$ | entrada | $2$ |
| $x_3$ | entrada | $3$ |
| $v_1$ | $x_1+x_2$ | $3$ |
| $v_2$ | $x_2+x_3$ | $5$ |
| $f$ | $v_1\cdot v_2$ | $15$ |
::::

⁠**En resumen:** La evaluación hacia adelante evalúa el grafo nodo a nodo y guarda cada valor intermedio.

### Derivadas locales

<span class="anker" id="stufe-9-4"></span>

Cada arista une un nodo con un sucesor que surge de él mediante una operación elemental. Cuánto reacciona el sucesor a una pequeña variación de este único predecesor es una derivada parcial ordinaria de la operación elemental.

:::definition Definición 9.3 (Derivada local)
<span class="anker" id="satz-9-3"></span>

Para una arista de $a$ a $b$, la derivada parcial $\partial b/\partial a$ de la operación elemental que calcula $b$, respecto de su entrada $a$, se llama la __derivada local__ de la arista. Se evalúa con los valores guardados de la evaluación hacia adelante.
:::

Para las operaciones elementales, las derivadas locales son sencillas (tabla [4](#tab-4)). Llama la atención lo poco que necesitan: en la función exponencial y en la función logística basta el valor guardado del propio sucesor. El nodo de máximo tiene un punto anguloso cuando las dos entradas son iguales; allí se usa uno de los dos valores laterales.

<span class="anker" id="tab-4"></span>

**Tabla 4:** Derivadas locales de las operaciones elementales, expresadas mediante valores guardados.

| Operación | derivadas locales | valores necesarios |
|---|---|---|
| $b=a_1+a_2$ | $\partial b/\partial a_1=1$, $\ \partial b/\partial a_2=1$ | ninguno |
| $b=a_1\cdot a_2$ | $\partial b/\partial a_1=a_2$, $\ \partial b/\partial a_2=a_1$ | las entradas |
| $b=a^2$ | $\partial b/\partial a=2a$ | la entrada |
| $b=\mathrm{e}^a$ | $\partial b/\partial a=\mathrm{e}^a=b$ | la salida |
| $b=\sigma(a)$ | $\partial b/\partial a=b\,(1-b)$ | la salida |
| $b=\max(a_1,a_2)$ | $1$ para la entrada mayor, $0$ para la otra | cuál es mayor |

Con las derivadas locales, la regla de la cadena de la sección [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2) es una pura tarea de recuento: la derivada del resultado respecto de una entrada es la suma sobre todos los caminos de la entrada al resultado, y a lo largo de cada camino se multiplican las derivadas locales de sus aristas.

::::beispiel [Ejemplo numérico]
En el grafo de la fig. [18](#abb-18), las cuatro aristas que van de las entradas a los nodos de suma tienen la derivada local $1$. La arista de $v_1$ al resultado tiene $\partial f/\partial v_1=v_2=5$; la de $v_2$, $\partial f/\partial v_2=v_1=3$. De $x_1$ lleva un camino al resultado, de $x_3$ también, y de $x_2$, dos. Así pues,

$$\frac{\partial f}{\partial x_1}=1\cdot5=5,\qquad \frac{\partial f}{\partial x_2}=1\cdot5+1\cdot3=8,\qquad \frac{\partial f}{\partial x_3}=1\cdot3=3 .$$

Comprobación: desarrollada, $f=x_1x_2+x_1x_3+x_2^2+x_2x_3$, con las derivadas parciales $x_2+x_3=5$, $x_1+2x_2+x_3=8$ y $x_1+x_2=3$.
::::

⁠**En resumen:** Cada arista lleva la derivada local de su operación elemental, evaluada con los valores guardados; la derivada del resultado es la suma, sobre todos los caminos, de los productos de estos números.

:::aufgabe Ejercicio 32 ★ Un grafo con un cuadrado
<span class="anker" id="aufg-32"></span>

Sea $f(x_1,x_2,x_3)=(x_1x_2+x_3)^2$.

<ol class="al">

<li>

Dibuja el grafo computacional con los resultados intermedios $v_1=x_1x_2$, $v_2=v_1+x_3$ y $f=v_2^2$.

</li>

<li>

Construye la tabla de la evaluación hacia adelante en el punto $(1,\,2,\,3)$ y escribe en cada arista su derivada local.

</li>

<li>

Calcula las tres derivadas parciales como sumas sobre los caminos y haz la comprobación.

</li>

</ol>

:::loesung
(a) Entradas $x_1,x_2,x_3$; un nodo de producto $v_1$ con aristas desde $x_1$ y $x_2$; un nodo de suma $v_2$ con aristas desde $v_1$ y $x_3$; un nodo de cuadrado $f$ con una arista desde $v_2$.

(b) Hacia adelante: $x_1=1$, $x_2=2$, $x_3=3$, $v_1=2$, $v_2=5$, $f=25$. Derivadas locales: $\partial v_1/\partial x_1=x_2=2$, $\partial v_1/\partial x_2=x_1=1$, $\partial v_2/\partial v_1=1$, $\partial v_2/\partial x_3=1$, $\partial f/\partial v_2=2v_2=10$.

(c) De cada entrada sale exactamente un camino hasta el resultado:

$$\frac{\partial f}{\partial x_1}=2\cdot1\cdot10=20,\qquad \frac{\partial f}{\partial x_2}=1\cdot1\cdot10=10,\qquad \frac{\partial f}{\partial x_3}=1\cdot10=10 .$$

Comprobación: $\partial_1f=2\,(x_1x_2+x_3)\,x_2=20$, $\partial_2f=2\,(x_1x_2+x_3)\,x_1=10$, $\partial_3f=2\,(x_1x_2+x_3)=10$.
:::
:::

:::aufgabe Ejercicio 33 ★★ Cinco factores
<span class="anker" id="aufg-33"></span>

Sea $p(x)=(x+1)(x+2)(x+3)(x+4)(x+5)$.

<ol class="al">

<li>

Calcula $p'(1)$ paso a paso con productos parciales, como en el ejemplo numérico de la sección [9.1](#stufe-9-1).

</li>

<li>

¿Cuántas multiplicaciones necesita la regla del producto escrita explícitamente, y cuántas el cálculo paso a paso? ¿Cómo crecen ambas cifras con el número $n$ de factores?

</li>

</ol>

:::loesung
(a) En el punto $1$, los factores son $2,3,4,5,6$. Paso a paso:

$$\begin{aligned} p_1&=2, & p_1'&=1,\\ p_2&=2\cdot3=6, & p_2'&=1\cdot3+2\cdot1=5,\\ p_3&=6\cdot4=24, & p_3'&=5\cdot4+6\cdot1=26,\\ p_4&=24\cdot5=120, & p_4'&=26\cdot5+24\cdot1=154,\\ p_5&=120\cdot6=720, & p_5'&=154\cdot6+120\cdot1=1044 . \end{aligned}$$

Por tanto, $p'(1)=1044$. Comprobación: $p'(1)=p(1)\bigl(\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\bigr)=720\cdot\tfrac{87}{60}=1044$.

(b) Escrita explícitamente, la regla del producto tiene $n$ sumandos con $n-1$ factores cada uno, es decir, $n\,(n-2)$ multiplicaciones; para $n=5$ son $15$. Paso a paso, cada uno de los $n-1$ pasos necesita dos multiplicaciones; para $n=5$, por tanto, $8$. La fórmula escrita explícitamente crece con $n^2$; el cálculo paso a paso, con $n$.
:::
:::

:::aufgabe Ejercicio 34 ★★ Un bucle como grafo
<span class="anker" id="aufg-34"></span>

Un programa hace $y=x$ y después eleva $y$ al cuadrado tres veces seguidas.

<ol class="al">

<li>

Dibuja el grafo computacional y da la función $y(x)$.

</li>

<li>

Calcula en el punto $x=2$ todos los valores intermedios y las derivadas locales y, a partir de ellos, $y'(2)$. Compáralo con la derivada de la fórmula de (a).

</li>

</ol>

:::loesung
(a) El grafo es una cadena $x\to y_1\to y_2\to y_3$ de tres nodos de cuadrado, $y_k=y_{k-1}^2$. Se tiene $y=((x^2)^2)^2=x^8$.

(b) En el punto $2$: $y_1=4$, $y_2=16$, $y_3=256$. Las derivadas locales son $2\cdot2=4$, $2\cdot4=8$ y $2\cdot16=32$, y su producto, $4\cdot8\cdot32=1024$. La fórmula da $8x^7=8\cdot128=1024$.
:::
:::
