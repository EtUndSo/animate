---
title: Diferenciación automática
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15231100
summary: Con el grafo computacional, las derivadas pueden calcularse mecánicamente, sin transformar fórmulas y con exactitud salvo por el redondeo de las operaciones elementales.
tags: diferenciación automática, modo directo, valor tangente, adjunto, modo inverso
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Con el grafo computacional, las derivadas pueden calcularse mecánicamente, sin transformar fórmulas y con exactitud salvo por el redondeo de las operaciones elementales. Esto se llama diferenciación automática. Hay dos formas de combinar las derivadas locales: hacia adelante, a la par que el cálculo, o hacia atrás, del resultado a las entradas. El modo inverso da la derivada de un número respecto de todas sus entradas en una sola pasada, y esta sección muestra por qué cuesta tan poco.
:::

### Qué es la diferenciación automática

<span class="anker" id="stufe-10-1"></span>

Hay tres maneras de obtener la derivada de un cálculo. Se puede transformar la fórmula con las reglas; esto se llama derivación simbólica y, según la sección [9.1](rechengraphen.html#stufe-9-1), las fórmulas crecen deprisa al hacerlo. Se puede evaluar la función en dos puntos cercanos y formar un cociente incremental; esto se llama derivación numérica, solo es aproximadamente correcta, y la sección [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) estudia su error. La tercera manera reúne las ventajas de las otras dos.

:::definition Definición 10.1 (Diferenciación automática)
<span class="anker" id="satz-10-1"></span>

La __diferenciación automática__ calcula derivadas de un cálculo aplicando la regla de la cadena a su grafo computacional: evalúa las derivadas locales con los números del cálculo y las combina según la suma sobre los caminos.
:::

La diferenciación automática calcula con números, no con fórmulas, y por eso las expresiones no se hinchan. No aproxima nada: el resultado es la derivada exacta, alterada solo por el redondeo de los distintos pasos de cálculo. Y funciona para cualquier programa formado por operaciones elementales, también con bucles y bifurcaciones, pues para las entradas dadas el programa da un grafo computacional. El cálculo paso a paso del ejemplo de la sección [9.1](rechengraphen.html#stufe-9-1) ya era diferenciación automática.

::::beispiel [Ejemplo numérico]
Para [(9.1)](rechengraphen.html#gl-9-1), la sección anterior compuso las derivadas $5$, $8$ y $3$ a partir de las derivadas locales, sin desarrollar ni derivar la fórmula de $f$. Eso era diferenciación automática, aunque todavía sin un procedimiento fijo para el orden del cálculo. Las dos subsecciones siguientes dan ese orden.
::::

⁠**En resumen:** La diferenciación automática aplica la regla de la cadena con números al grafo computacional; es exacta salvo por el redondeo y no necesita ninguna fórmula.

### El modo directo

<span class="anker" id="stufe-10-2"></span>

La primera posibilidad sigue al propio cálculo. Se fija en qué dirección se modifican las entradas y, en cada nodo, además de su valor, se lleva consigo lo rápido que cambia con esa modificación.

:::definition Definición 10.2 (Modo directo)
<span class="anker" id="satz-10-2"></span>

En el __modo directo__ se elige una dirección $\dot{\mathbf{x}}\in\mathbb{R}^n$ para las entradas y se calcula para cada nodo $b$, además de su valor, el número

<span class="anker" id="gl-10-1"></span>
$$\dot b=\sum_{a\text{ predecesor de }b}\frac{\partial b}{\partial a}\,\dot a , \tag{10.1}$$

en el mismo orden que los valores. Este número se llama el __valor tangente__ de $b$; los nodos de entrada reciben como valores tangentes las componentes de $\dot{\mathbf{x}}$.
:::

El nombre recuerda a la recta tangente de la sección [1.2](die-ableitung.html#stufe-1-2), pero es un número: el valor tangente $\dot b$ es la tasa de variación del nodo $b$ cuando las entradas se desplazan a lo largo de la recta $\mathbf{x}+t\,\dot{\mathbf{x}}$. La fórmula [(10.1)](#gl-10-1) es la regla de la cadena a lo largo de esta curva, [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), para un único nodo. Tras una pasada, en el resultado está $\dot f=\nabla f(\mathbf{x})^{\top}\dot{\mathbf{x}}$. Si el cálculo tiene varias salidas, allí está el producto $\mathbf{J}\,\dot{\mathbf{x}}$ de la matriz jacobiana por la dirección. Con $\dot{\mathbf{x}}=\mathbf{e}_j$, una pasada da la derivada parcial respecto de $x_j$; con varias salidas, la columna $j$ de la matriz jacobiana. Para el gradiente completo de una función de $n$ variables, el modo directo necesita, pues, $n$ pasadas.

::::beispiel [Ejemplo numérico]
Para [(9.1)](rechengraphen.html#gl-9-1) en el punto $(1,\,2,\,3)$ con la dirección $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)^{\top}$ resulta la tabla [5](#tab-5). En el resultado está $\dot f=8=\partial f/\partial x_2$. Para $\partial f/\partial x_1$ y $\partial f/\partial x_3$ hacen falta otras dos pasadas, con $\mathbf{e}_1$ y $\mathbf{e}_3$.

<span class="anker" id="tab-5"></span>

**Tabla 5:** El modo directo para $f=(x_1+x_2)\,(x_2+x_3)$ en el punto $(1,\,2,\,3)$ en la dirección $\dot{\mathbf{x}}=\mathbf{e}_2$.

| Nodo | Cálculo | Valor | Valor tangente |  |
|---|---|---|---|---|
| $x_1$ | entrada | $1$ | $\dot x_1$ | $0$ |
| $x_2$ | entrada | $2$ | $\dot x_2$ | $1$ |
| $x_3$ | entrada | $3$ | $\dot x_3$ | $0$ |
| $v_1$ | $x_1+x_2$ | $3$ | $\dot v_1=\dot x_1+\dot x_2$ | $1$ |
| $v_2$ | $x_2+x_3$ | $5$ | $\dot v_2=\dot x_2+\dot x_3$ | $1$ |
| $f$ | $v_1\cdot v_2$ | $15$ | $\dot f=v_2\,\dot v_1+v_1\,\dot v_2$ | $5+3=8$ |
::::

⁠**En resumen:** El modo directo lleva consigo, junto a cada valor, su valor tangente; una pasada da la derivada en una dirección, es decir, una columna de la matriz jacobiana.

:::hintergrund El modo directo con números duales
El modo directo puede entenderse como un cálculo con números ampliados. Se calcula con pares $a+\dot a\,\varepsilon$, donde $\varepsilon$ es un símbolo nuevo con la única regla $\varepsilon^2=0$; estos números se llaman números duales. La suma y la multiplicación funcionan como de costumbre: $(a+\dot a\varepsilon)+(b+\dot b\varepsilon)=(a+b)+(\dot a+\dot b)\varepsilon$ y $(a+\dot a\varepsilon)(b+\dot b\varepsilon)=ab+(a\dot b+\dot ab)\varepsilon$, porque el término $\dot a\dot b\varepsilon^2$ desaparece. El factor que acompaña a $\varepsilon$ sigue, pues, exactamente la regla de la suma y la del producto. Para [(9.1)](rechengraphen.html#gl-9-1) se toma $x_1=1$, $x_2=2+\varepsilon$, $x_3=3$ y se obtiene $(3+\varepsilon)(5+\varepsilon)=15+8\varepsilon+\varepsilon^2=15+8\varepsilon$: valor y derivada respecto de $x_2$ en un solo cálculo. Para una función $\varphi$ de una variable se define $\varphi(a+\dot a\varepsilon)=\varphi(a)+\varphi'(a)\,\dot a\,\varepsilon$, lo que corresponde a la aproximación lineal, en la que el cuadrado del término pequeño no desempeña ningún papel. Los números duales los introdujo William Kingdon Clifford en 1873, mucho antes de cualquier ordenador.
:::

### El modo inverso

<span class="anker" id="stufe-10-3"></span>

El modo directo pregunta, para una entrada, cuánto depende de ella cada nodo. El modo inverso plantea la pregunta contraria: ¿cuánto depende el resultado de cada nodo? Esta pregunta puede responderse hacia atrás desde el resultado, y al final se conoce la respuesta para todas las entradas a la vez.

:::definition Definición 10.3 (Modo inverso)
<span class="anker" id="satz-10-3"></span>

El __adjunto__ de un nodo $a$ es $\bar a=\partial f/\partial a$, la derivada del resultado respecto de este nodo cuando se lo considera una entrada del resto del cálculo. En el __modo inverso__ se hace primero la evaluación hacia adelante y se guardan todos los valores. Después se pone $\bar f=1$ y se calculan los nodos en orden inverso,

<span class="anker" id="gl-10-2"></span>
$$\bar a=\sum_{b\text{ sucesor de }a}\bar b\,\frac{\partial b}{\partial a}. \tag{10.2}$$

Los adjuntos de los nodos de entrada forman el gradiente $\nabla f(\mathbf{x})$.
:::

El orden inverso es necesario porque cada nodo necesita los adjuntos de sus sucesores, y estos vienen después de él en el cálculo. Cada adjunto tiene la misma forma que su nodo; si un nodo es un vector o una matriz, también el adjunto es un vector o una matriz, como en la regla hacia atrás del producto de matrices de la sección [7.6](ableiten-nach-vektoren-und-matrizen.html#stufe-7-6).

:::satz Teorema 10.4 (El modo inverso da el gradiente)
<span class="anker" id="satz-10-4"></span>

Para cada nodo $a$, el número $\bar a$ calculado según [(10.2)](#gl-10-2) es la suma sobre todos los caminos de $a$ al resultado, con el producto de las derivadas locales a lo largo de cada camino. Para los nodos de entrada es, según la sección [9.4](rechengraphen.html#stufe-9-4), la derivada parcial de $f$.
:::

:::beweis El modo inverso da el gradiente
Se ordenan todos los caminos de $a$ al resultado según su primera arista. Cada camino empieza con una arista hacia un sucesor $b$ y continúa después como camino de $b$ al resultado. Por eso, los caminos que pasan por $b$ aportan en conjunto $\frac{\partial b}{\partial a}$ por la suma sobre todos los caminos de $b$ al resultado. Si esta suma ya está bien calculada para todos los sucesores, es decir, es igual a $\bar b$, la suma para $a$ es exactamente [(10.2)](#gl-10-2). Para el propio resultado, el enunciado vale con $\bar f=1$, el camino vacío. Como se calcula hacia atrás, a los sucesores siempre les toca antes que a $a$, y el enunciado se transmite nodo a nodo hasta las entradas.
:::

::::beispiel [Ejemplo numérico]
Para [(9.1)](rechengraphen.html#gl-9-1) en el punto $(1,\,2,\,3)$ resultan la tabla [6](#tab-6) y la fig. [19](#abb-19). Una sola pasada hacia atrás da las tres derivadas parciales $(5,\,8,\,3)$, que el modo directo solo obtuvo con tres pasadas.

<span class="anker" id="tab-6"></span>

**Tabla 6:** El modo inverso para $f=(x_1+x_2)\,(x_2+x_3)$ en el punto $(1,\,2,\,3)$; los valores proceden de la tabla [3](rechengraphen.html#tab-3).

| Nodo | Cálculo según [(10.2)](#gl-10-2) | Adjunto |
|---|---|---|
| $f$ | inicio | $\bar f=1$ |
| $v_2$ | $\bar f\cdot\partial f/\partial v_2=1\cdot v_1$ | $\bar v_2=3$ |
| $v_1$ | $\bar f\cdot\partial f/\partial v_1=1\cdot v_2$ | $\bar v_1=5$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=3$ |
| $x_2$ | $\bar v_1\cdot1+\bar v_2\cdot1$ | $\bar x_2=5+3=8$ |
| $x_1$ | $\bar v_1\cdot1$ | $\bar x_1=5$ |

:::abbildung ml/k3rueckwaerts 19
Valores hacia adelante y hacia atrás en el grafo computacional de $f=(x_1+x_2)\,(x_2+x_3)$ en el punto $(1,\,2,\,3)$: en verde, los valores de la evaluación hacia adelante; en rojo, los adjuntos; en gris, junto a las aristas, las derivadas locales. Al calcular hacia atrás, cada adjunto recorre las aristas en sentido contrario a las flechas y se multiplica por la derivada local de la arista; donde salen dos aristas de un nodo, como en $x_2$, las contribuciones se suman.
:::
::::

⁠**En resumen:** El modo inverso calcula primero hacia adelante y guarda todos los valores; después calcula hacia atrás los adjuntos $\bar a=\sum\bar b\,\partial b/\partial a$; una pasada hacia atrás da el gradiente completo.

### Patrones en el flujo hacia atrás

<span class="anker" id="stufe-10-4"></span>

Según la tabla [4](rechengraphen.html#tab-4), las operaciones elementales se comportan al calcular hacia atrás de una manera sencilla y recurrente. Quien conoce estos patrones puede escribir los adjuntos casi sin cálculo y detectar rápidamente errores en las deducciones.

:::satz Teorema 10.5 (Patrones de las operaciones elementales)
<span class="anker" id="satz-10-5"></span>

<ol class="al">

<li>

Una *suma* transmite su adjunto sin cambios a cada entrada.

</li>

<li>

Una *multiplicación* transmite a cada entrada su adjunto por el valor de la *otra* entrada.

</li>

<li>

Un *máximo* transmite su adjunto entero a la entrada mayor; la menor recibe $0$.

</li>

<li>

Una función de una variable multiplica el adjunto por su derivada local; en la función logística, pues, por $b\,(1-b)$.

</li>

<li>

Si un nodo se usa varias veces, las contribuciones de todos sus sucesores se *suman*.

</li>

</ol>
:::

Cada enunciado es [(10.2)](#gl-10-2) con las derivadas locales de la tabla [4](rechengraphen.html#tab-4). De (b) se sigue una observación útil: si un factor es mil veces mayor que el otro, el adjunto del factor menor es mil veces mayor que el del mayor. Por eso, grandes diferencias en los órdenes de magnitud de las entradas llevan a diferencias igual de grandes en las derivadas parciales.

::::beispiel [Ejemplo numérico]
En la tabla [6](#tab-6), la multiplicación ha intercambiado: $v_1$ recibió $v_2=5$, y $v_2$ recibió $v_1=3$. Las sumas han transmitido estos valores sin cambios, y $x_2$, como nodo con dos sucesores, ha reunido $5+3=8$. Un ejemplo con máximo: para $f=\max(x_1,x_2)\cdot x_3$ en el punto $(1,\,2,\,3)$ se tiene $v=\max(1,2)=2$ y $f=6$. Hacia atrás, $\bar v=x_3=3$ y $\bar x_3=v=2$; el máximo transmite $\bar v$ a la entrada mayor, $x_2$, es decir, $\bar x_2=3$ y $\bar x_1=0$. En efecto, una pequeña variación de $x_1$ no cambia el resultado mientras se mantenga $x_1<x_2$.
::::

⁠**En resumen:** La suma reparte, la multiplicación intercambia, el máximo deja pasar, y en las ramificaciones se suma.

### El coste

<span class="anker" id="stufe-10-5"></span>

¿Por qué es tan importante el modo inverso? Porque da el gradiente de una función con muchísimas entradas casi tan barato como el propio valor de la función. La comparación de los procedimientos lo deja claro.

El modo directo necesita, para el gradiente de una función de $n$ variables, $n$ pasadas, una por cada dirección de entrada. Una pasada cuesta un pequeño múltiplo de una evaluación de $f$, pues a cada operación elemental se añade su valor tangente. Los cocientes incrementales necesitan incluso $n+1$ o $2n$ evaluaciones. El modo inverso, en cambio, necesita siempre exactamente una evaluación hacia adelante y una pasada hacia atrás, sea cual sea el tamaño de $n$. En la pasada hacia atrás, cada arista se usa exactamente una vez, con una multiplicación y una suma. Por tanto, también ella cuesta solo un pequeño múltiplo de la evaluación hacia adelante.

:::satz Teorema 10.6 (Coste del modo directo y del modo inverso)
<span class="anker" id="satz-10-6"></span>

Sea $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ dada por un grafo computacional de operaciones elementales, y sea $T$ el tiempo que cuesta una evaluación. Entonces la matriz jacobiana completa cuesta en el modo directo aproximadamente $c\cdot n\cdot T$, y en el modo inverso, aproximadamente $c\cdot m\cdot T$. El número $c$ no depende de $n$ ni de $m$. Si se cuenta cada operación aritmética básica como un paso, puede demostrarse que el valor de la función y el gradiente juntos necesitan a lo sumo cuatro veces más pasos que el valor de la función solo; si se cuentan también los accesos a memoria, $c$ queda por debajo de $6$, y en la práctica suele estar entre $2$ y $3$. Para un número ($m=1$), el gradiente completo en el modo inverso cuesta, pues, solo un pequeño múltiplo fijo de una evaluación.
:::

El teorema se demuestra contando, para cada operación elemental, cuántos pasos de cálculo necesita su paso hacia atrás en relación con ella misma. De ahí se sigue una regla práctica: muchas entradas y una salida, como en un número que depende de millones de perillas de ajuste, exigen el modo inverso. Pocas entradas y muchas salidas exigen el modo directo. Para la matriz jacobiana completa de una función con muchas entradas y muchas salidas no hay un truco así; ahí, cualquier procedimiento cuesta muchas pasadas.

El modo inverso tiene un precio: la memoria. La pasada hacia atrás necesita todos los valores de la evaluación hacia adelante, pues las derivadas locales se evalúan con ellos. Hay que conservar, pues, cada valor intermedio hasta que la pasada hacia atrás haya pasado por él. En cálculos largos, esta memoria suele ser el verdadero límite.

::::beispiel [Ejemplo numérico]
Supongamos que una función tiene $n=10^6$ entradas y que una evaluación dura un segundo. El modo directo necesita para el gradiente $10^6$ pasadas, es decir, al menos $10^6$ segundos, algo más de $11$ días. Los cocientes incrementales centrales necesitan $2\cdot10^6$ evaluaciones, algo más de $23$ días, y además solo son aproximadamente correctos. El modo inverso necesita una evaluación hacia adelante y una pasada hacia atrás; con $c\approx3$, pues, unos pocos segundos.
::::

⁠**En resumen:** El modo inverso da las $n$ derivadas parciales de un número por un pequeño múltiplo fijo de una evaluación, independientemente de $n$; lo paga con la memoria para todos los valores intermedios.

:::hintergrund Por qué el modo inverso es tan barato, y de dónde viene
La suma sobre todos los caminos puede tener muchísimos sumandos. Si se encadenan diez pasos de cálculo, cada uno de los cuales usa dos veces a su predecesor, por ejemplo $v_{k+1}=v_k\cdot v_k$, entre la entrada y el resultado hay $2^{10}=1024$ caminos, y con $50$ pasos, más de $10^{15}$. El modo inverso nunca cuenta estos caminos uno a uno. Reúne todos los caminos que pasan por un mismo nodo en el adjunto de este y reutiliza esta suma parcial para todos los predecesores. Es la misma idea que en la regla del producto paso a paso de la sección [9.1](rechengraphen.html#stufe-9-1): un resultado intermedio se calcula una vez y después se usa muchas veces. Así, cada arista cuesta una multiplicación y una suma, y el coste crece con el número de aristas, no con el número de caminos. La memoria necesaria puede reducirse guardando solo algunos valores intermedios y volviendo a calcular los demás durante la pasada hacia atrás; con un reparto hábil, la memoria y el factor en que el tiempo de cálculo supera al de una evaluación simple crecen entonces solo logarítmicamente con la longitud del cálculo.

El modo directo se describió en 1964 como programa de ordenador. El modo inverso lo desarrolló Seppo Linnainmaa en 1970 en su tesis de maestría en la Universidad de Helsinki, para estimar cómo repercuten en el resultado los errores de redondeo de todos los pasos de cálculo; la sensibilidad del resultado respecto de cada paso intermedio es exactamente su adjunto. En 1980 siguió un programa que generaba automáticamente el modo inverso para cálculos arbitrarios.
:::

### Asociación: vector por matriz jacobiana

<span class="anker" id="stufe-10-6"></span>

La diferencia entre los dos modos puede describirse también con matrices. Un cálculo que consta de las etapas $\mathbf{g}_1,\dots,\mathbf{g}_L$ y termina en un número tiene, según [(6.1)](die-kettenregel-fur-mehrere-variablen.html#gl-6-1), la matriz jacobiana

$$\mathbf{J}=\mathbf{J}_L\,\mathbf{J}_{L-1}\cdots\mathbf{J}_1 ,$$

donde $\mathbf{J}_L$ es una fila, porque la última etapa solo tiene una salida. El producto es el mismo se asocie como se asocie; pero, según el [capítulo 1, sección 9.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3), el coste es muy distinto. El modo inverso asocia por la izquierda: $\bigl((\mathbf{J}_L\mathbf{J}_{L-1})\,\mathbf{J}_{L-2}\bigr)\cdots$. Cada paso multiplica una fila por una matriz y da de nuevo una fila, el adjunto traspuesto de la etapa correspondiente. El modo directo asocia por la derecha: $\mathbf{J}_L\bigl(\cdots(\mathbf{J}_2\,(\mathbf{J}_1\dot{\mathbf{x}}))\bigr)$. Para un único vector $\dot{\mathbf{x}}$, también esto es barato; pero para el gradiente completo necesita $n$ vectores así, y eso es tan caro como si se multiplicaran por completo las matrices $\mathbf{J}_2\mathbf{J}_1$, $\mathbf{J}_3\mathbf{J}_2\mathbf{J}_1,\dots$.

A esto se añade un segundo punto: las matrices jacobianas nunca se forman. Cada paso hacia atrás calcula directamente el producto del adjunto por la matriz jacobiana, con las reglas de las operaciones elementales. Para un producto matriz-vector $\mathbf{y}=\mathbf{A}\mathbf{x}$ es, según [(7.6)](ableiten-nach-vektoren-und-matrizen.html#gl-7-6), $\bar{\mathbf{x}}=\mathbf{A}^{\top}\bar{\mathbf{y}}$, sin ninguna matriz adicional; para una función elemento a elemento es, según [(5.4)](die-jacobi-matrix.html#gl-5-4), el producto componente a componente por las derivadas, sin construir una matriz diagonal. Y es necesario: si una etapa tiene $10^5$ entradas y $10^5$ salidas, su matriz jacobiana tiene $10^{10}$ entradas de la matriz; con ocho bytes por número, son $80$ gigabytes.

::::beispiel [Ejemplo numérico]
Supongamos que un cálculo consta de tres etapas $\mathbb{R}^{1000}\to\mathbb{R}^{1000}$ y una última etapa $\mathbb{R}^{1000}\to\mathbb{R}$. Un producto de fila por matriz $1000\times1000$ cuesta, según el [capítulo 1, sección 9.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3), unas $2\cdot10^6$ operaciones aritméticas básicas; un producto de dos de estas matrices, unas $2\cdot10^9$. Asociando por la izquierda, son tres productos de fila por matriz, en total unas $6\cdot10^6$. Asociando por la derecha, son dos productos de matrices y un producto de fila por matriz, en total unas $4\cdot10^9$, unas $670$ veces más.
::::

⁠**En resumen:** El modo inverso multiplica la cadena de matrices jacobianas por la izquierda con una fila; el modo directo, por la derecha con una columna; las propias matrices jacobianas nunca se forman.

:::aufgabe Ejercicio 35 ★ Hacia atrás a través de un cuadrado
<span class="anker" id="aufg-35"></span>

Sea $f=(x_1x_2+x_3)^2$ como en el ejercicio [32](rechengraphen.html#aufg-32).

<ol class="al">

<li>

Calcula en el punto $(1,\,2,\,3)$ todos los adjuntos en el modo inverso y preséntalos en una tabla como la tabla [6](#tab-6).

</li>

<li>

¿Cuántas pasadas necesitaría el modo directo para el mismo gradiente? Realiza la pasada para $\dot{\mathbf{x}}=\mathbf{e}_1$.

</li>

</ol>

:::loesung
(a) Con los valores del ejercicio [32](rechengraphen.html#aufg-32):

| Nodo | Cálculo | Adjunto |
|---|---|---|
| $f$ | inicio | $\bar f=1$ |
| $v_2$ | $\bar f\cdot2v_2$ | $\bar v_2=10$ |
| $v_1$ | $\bar v_2\cdot1$ | $\bar v_1=10$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=10$ |
| $x_2$ | $\bar v_1\cdot x_1$ | $\bar x_2=10$ |
| $x_1$ | $\bar v_1\cdot x_2$ | $\bar x_1=20$ |

(b) Tres pasadas, una por cada entrada. Con $\dot{\mathbf{x}}=\mathbf{e}_1$: $\dot v_1=x_2\dot x_1+x_1\dot x_2=2$, $\dot v_2=\dot v_1+\dot x_3=2$, $\dot f=2v_2\,\dot v_2=10\cdot2=20=\partial f/\partial x_1$.
:::
:::

:::aufgabe Ejercicio 36 ★★ La función logística en el grafo
<span class="anker" id="aufg-36"></span>

Sea $f(x_1,x_2)=\sigma(2x_1-x_2)$, con la función logística $\sigma$.

<ol class="al">

<li>

Dibuja el grafo con $v_1=2x_1$, $v_2=v_1-x_2$, $f=\sigma(v_2)$ y calcula hacia adelante en el punto $(1,\,1)$.

</li>

<li>

Calcula todos los adjuntos. ¿Qué número guardado necesita el nodo $\sigma$ para su derivada local?

</li>

<li>

Verifica: $\nabla f(\mathbf{x})=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$.

</li>

</ol>

:::loesung
(a) El grafo tiene las aristas $x_1\to v_1$, $v_1\to v_2$, $x_2\to v_2$ y $v_2\to f$. Hacia adelante, en el punto $(1,\,1)$: $v_1=2$, $v_2=1$, $f=\sigma(1)\approx0{,}7311$.

(b) $\bar f=1$; $\bar v_2=\bar f\cdot f\,(1-f)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$; $\bar v_1=\bar v_2\cdot1\approx0{,}1966$; $\bar x_2=\bar v_2\cdot(-1)\approx-0{,}1966$; $\bar x_1=\bar v_1\cdot2\approx0{,}3932$. Para su derivada local, el nodo $\sigma$ solo necesita su propia salida guardada, $f$, según la tabla [4](rechengraphen.html#tab-4).

(c) Según la regla de la cadena, $\nabla f=\sigma'(2x_1-x_2)\,\nabla(2x_1-x_2)=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$; en el punto $(1,\,1)$, por tanto, $0{,}1966\cdot(2,\,-1)^{\top}=(0{,}3932;\ -0{,}1966)^{\top}$.
:::
:::

:::aufgabe Ejercicio 37 ★★ Números duales
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Calcula $p(x)=(x+1)(x+2)(x+3)(x+4)$ con el número dual $x=0+1\varepsilon$ y lee $p(0)$ y $p'(0)$.

</li>

<li>

Calcula del mismo modo $(x^2+1)^3$ en el punto $x=1+\varepsilon$ y compáralo con la regla de la cadena.

</li>

</ol>

:::loesung
(a) Con $x=\varepsilon$:

$$(1+\varepsilon)(2+\varepsilon)=2+3\varepsilon,\quad (2+3\varepsilon)(3+\varepsilon)=6+11\varepsilon,\quad (6+11\varepsilon)(4+\varepsilon)=24+50\varepsilon .$$

Por tanto, $p(0)=24$ y $p'(0)=50$; los factores que acompañan a $\varepsilon$ son exactamente los $p_k'$ del ejemplo numérico de la sección [9.1](rechengraphen.html#stufe-9-1).

(b) $(1+\varepsilon)^2=1+2\varepsilon$; sumando $1$ se obtiene $2+2\varepsilon$; $(2+2\varepsilon)^2=4+8\varepsilon$ y $(4+8\varepsilon)(2+2\varepsilon)=8+24\varepsilon$. La regla de la cadena da $3\,(x^2+1)^2\cdot2x=3\cdot4\cdot2=24$ en el punto $1$.
:::
:::

:::aufgabe Ejercicio 38 ★★★ ¿Qué modo?
<span class="anker" id="aufg-38"></span>

<ol class="al">

<li>

Un cálculo tiene $3$ entradas y $1000$ salidas; otro, $1000$ entradas y $3$ salidas. ¿Cuántas pasadas necesitan en cada caso el modo directo y el modo inverso para la matriz jacobiana completa?

</li>

<li>

Sea $f(\mathbf{x})=\mathbf{c}^{\top}\mathbf{B}\mathbf{x}$ con una matriz densa $\mathbf{B}\in\mathbb{R}^{n\times n}$, calculada en dos etapas, $\mathbf{y}=\mathbf{B}\mathbf{x}$ y $f=\mathbf{c}^{\top}\mathbf{y}$. Una pasada hacia adelante calcula $\mathbf{c}^{\top}(\mathbf{B}\dot{\mathbf{x}})$; una pasada hacia atrás, $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$. Cuenta, para ambos caminos, las operaciones aritméticas básicas que cuesta el gradiente completo, si un producto matriz-vector cuesta unas $2n^2$ y un producto escalar unas $2n$.

</li>

<li>

¿Por qué necesita el modo inverso más memoria que el modo directo? ¿Qué valores puede olvidar de inmediato el modo directo?

</li>

</ol>

:::loesung
(a) Con $3$ entradas y $1000$ salidas, el modo directo necesita $3$ pasadas, y el modo inverso, $1000$; se elige el modo directo. Con $1000$ entradas y $3$ salidas es al revés: $1000$ pasadas hacia adelante frente a $3$ pasadas hacia atrás.

(b) Hacia adelante, el gradiente necesita $n$ pasadas con $\dot{\mathbf{x}}=\mathbf{e}_1,\dots,\mathbf{e}_n$, cada una con un producto matriz-vector $\mathbf{B}\dot{\mathbf{x}}$ y un producto escalar: en total, unas $n\,(2n^2+2n)\approx2n^3$ operaciones aritméticas básicas. Hacia atrás, $\bar{\mathbf{y}}=\mathbf{c}$, y $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ cuesta un producto matriz-vector, unas $2n^2$; a ello se suma la evaluación hacia adelante, con unas $2n^2+2n$. El modo inverso es, por tanto, unas $n/2$ veces más rápido.

(c) La pasada hacia atrás necesita los valores de la evaluación hacia adelante para evaluar las derivadas locales, y solo empieza cuando la evaluación hacia adelante ha terminado. Por eso hay que guardar todos los valores intermedios hasta entonces. En el modo directo, el valor y el valor tangente avanzan juntos; ninguno de los dos se necesita ya en cuanto se han calculado todos los sucesores del nodo, y entonces pueden olvidarse.
:::
:::
