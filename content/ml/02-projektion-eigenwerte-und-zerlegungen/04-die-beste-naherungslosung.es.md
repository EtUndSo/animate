---
title: La mejor solución aproximada
pfad: Informática / Aprendizaje automático / Proyección, valores propios y descomposiciones
order: 6220400
summary: Un sistema de ecuaciones con más ecuaciones que incógnitas no suele tener solución.
tags: residuo, mejor solución aproximada, ecuaciones normales, recta de ajuste
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Un sistema de ecuaciones con más ecuaciones que incógnitas no suele tener solución. En su lugar, esta sección busca las incógnitas que cumplen el sistema lo mejor posible. Se obtienen de un sistema de ecuaciones más pequeño y siempre resoluble, y la razón vuelve a ser un ángulo recto.
:::

### Repaso: más ecuaciones que incógnitas

<span class="anker" id="stufe-3-1"></span>

En la parte 1, sección 12.5, dos pesos, $w_1$ para la superficie y $w_2$ para el número de habitaciones, debían acertar exactamente los precios de unas viviendas. Con las cuatro viviendas, esto es el sistema $\mathbf{A}\mathbf{w}=\mathbf{y}$ con

$$\mathbf{A}=\begin{pmatrix}60&2\\40&1\\90&4\\70&3\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}200\\130\\290\\240\end{pmatrix}\ \text{miles de euros}.$$

No tiene solución. En la imagen por columnas, esto significa que las columnas de $\mathbf{A}$ generan en $\mathbb{R}^4$ un plano, el espacio columna, y que el vector de precios $\mathbf{y}$ no está en él. Se elija lo que se elija para $\mathbf{w}$, siempre queda un resto.

:::definition Definición 3.1 (Residuo)
<span class="anker" id="satz-3-1"></span>

Para un sistema de ecuaciones $\mathbf{A}\mathbf{x}=\mathbf{y}$ y un vector cualquiera $\mathbf{x}$,

<span class="anker" id="gl-3-1"></span>
$$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x} \tag{3.1}$$

se llama __residuo__ de $\mathbf{x}$.
:::

La palabra viene del término latino que significa «resto». El residuo es cero si y solo si $\mathbf{x}$ resuelve el sistema. Es el vector de error de la parte 1, sección 3.5, con el signo cambiado; su longitud es la misma.

⁠**Ejemplo numérico:** Con los pesos $\mathbf{w}=(3,\,10)^{\top}$ de la parte 1 se obtiene el producto $\mathbf{A}\mathbf{w}=(200,\,130,\,310,\,240)^{\top}$, y el residuo es $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{w}=(0,\,0,\,-20,\,0)^{\top}$, de longitud $20$. Tres precios se aciertan exactamente, y uno se falla por $20$ mil euros.

⁠**En resumen:** El residuo $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ es el resto que deja un vector $\mathbf{x}$ al resolver $\mathbf{A}\mathbf{x}=\mathbf{y}$.

### La mejor solución aproximada

<span class="anker" id="stufe-3-2"></span>

Si el residuo no puede llegar a ser cero, que al menos sea lo más pequeño posible. La medida para ello es su longitud euclídea.

El problema puede imaginarse geométricamente. Si $\mathbf{x}$ recorre todos los vectores, $\mathbf{A}\mathbf{x}$ recorre, según la parte 1, sección 7.4, el espacio columna de $\mathbf{A}$. La distancia $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert$ es la distancia del punto $\mathbf{y}$ al punto $\mathbf{A}\mathbf{x}$ del espacio columna. Se busca, por tanto, el punto del espacio columna más cercano a $\mathbf{y}$ (fig. [6](#abb-6)). En la sección anterior, el espacio columna era una recta; ahora puede ser un plano o un espacio generado de dimensión mayor.

:::definition Definición 3.2 (Mejor solución aproximada)
<span class="anker" id="satz-3-2"></span>

Un vector $\hat{\mathbf{x}}$ se llama __mejor solución aproximada__ del sistema $\mathbf{A}\mathbf{x}=\mathbf{y}$ si

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert\le\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\qquad\text{para todo }\mathbf{x} . \tag{3.2}$$
:::

La longitud es mínima donde lo es su cuadrado, y el cuadrado es la suma de los cuadrados de las componentes del residuo. Por eso se habla también de la solución por el *método de mínimos cuadrados*. Si el sistema tiene una solución exacta, esta es también la mejor solución aproximada, pues su residuo tiene longitud cero.

:::abbildung ml/k2ebene 6
Proyección sobre un plano de $\mathbb{R}^3$. Las columnas $\mathbf{a}_1=(1,0,1)^{\top}$ y $\mathbf{a}_2=(0,1,1)^{\top}$ generan el plano $x_3=x_1+x_2$ (azul). El punto $\mathbf{y}=(1,1,1)^{\top}$ no está en él. El punto más cercano del plano es $\hat{\mathbf{y}}=(\tfrac23,\tfrac23,\tfrac43)^{\top}$; el residuo $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(\tfrac13,\tfrac13,-\tfrac13)^{\top}$ es perpendicular al plano.
:::

⁠**Ejemplo numérico:** La matriz $\mathbf{H}$ de la parte 1, sección 7.4, tiene las columnas $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ y $\mathbf{a}_2=(0,\,1,\,1)^{\top}$. Su espacio columna es el plano de todos los vectores cuya tercera componente es la suma de las dos primeras. El vector $\mathbf{y}=(1,\,1,\,1)^{\top}$ no está en él; el sistema $\mathbf{H}\mathbf{x}=\mathbf{y}$ no tiene, por tanto, solución. Con $\mathbf{x}=(1,\,0)^{\top}$, el residuo es $(0,\,1,\,0)^{\top}$, de longitud $1$; con $\mathbf{x}=(1,\,1)^{\top}$ es $(0,\,0,\,-1)^{\top}$, también de longitud $1$. Si se puede hacer mejor lo responde la subsección siguiente.

⁠**En resumen:** La mejor solución aproximada hace el residuo lo más corto posible; geométricamente, busca el punto del espacio columna más cercano a $\mathbf{y}$.

### Las ecuaciones normales

<span class="anker" id="stufe-3-3"></span>

En la recta, el punto más cercano era el pie de la perpendicular: el residuo era perpendicular a la recta. Para un espacio columna, la misma condición se impone de forma natural: el residuo debe ser perpendicular a todo vector del espacio columna. Esto puede escribirse como un sistema de ecuaciones.

:::herleitung Las ecuaciones normales
Todo vector del espacio columna es una combinación lineal $\sum_jz_j\mathbf{a}_j$ de las columnas. Si $\mathbf{r}$ es perpendicular a cada columna, también lo es a cada una de estas combinaciones lineales, pues $\bigl(\sum_jz_j\mathbf{a}_j\bigr)^{\top}\mathbf{r}=\sum_jz_j\,\mathbf{a}_j^{\top}\mathbf{r}$. Basta, por tanto, con exigir para cada columna:

$$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=0\qquad\text{para }j=1,\dots,n .$$

Los números $\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ son las componentes de $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$, pues las filas de $\mathbf{A}^{\top}$ son las columnas de $\mathbf{A}$. Las $n$ condiciones juntas se escriben, por tanto, como $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=\mathbf{0}$; desarrollando el producto, $\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$.
:::

:::definition Definición 3.3 (Ecuaciones normales)
<span class="anker" id="satz-3-3"></span>

Al sistema $\mathbf{A}\mathbf{x}=\mathbf{y}$ con $\mathbf{A}\in\mathbb{R}^{m\times n}$ le corresponden las __ecuaciones normales__

<span class="anker" id="gl-3-3"></span>
$$\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y} . \tag{3.3}$$
:::

La palabra «normal» significa aquí «perpendicular», como en el vector normal de un plano: las ecuaciones exigen que el residuo sea perpendicular al espacio columna. La matriz $\mathbf{A}^{\top}\mathbf{A}$ es la matriz de Gram de las columnas de la parte 1, sección 10.4; es cuadrada, con tantas filas como incógnitas hay. Un sistema grande e irresoluble de $m$ ecuaciones se convierte en uno pequeño de $n$ ecuaciones. Para una sola columna $\mathbf{a}$ queda $\mathbf{a}^{\top}\mathbf{a}\,\hat x=\mathbf{a}^{\top}\mathbf{y}$, la fórmula de la sección anterior.

⁠**Ejemplo numérico:** Para $\mathbf{H}$ y $\mathbf{y}=(1,\,1,\,1)^{\top}$ se tiene

$$\mathbf{H}^{\top}\mathbf{H}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf{H}^{\top}\mathbf{y}=\begin{pmatrix}2\\2\end{pmatrix}.$$

Cada entrada es un producto escalar de dos columnas o de una columna con $\mathbf{y}$ (fig. [7](#abb-7)).

:::abbildung ml/k2rnormal 7
Dos entradas de las ecuaciones normales como productos escalares: la entrada $(1,2)$ de $\mathbf{H}^{\top}\mathbf{H}$ es $\mathbf{a}_1^{\top}\mathbf{a}_2$, y la primera componente de $\mathbf{H}^{\top}\mathbf{y}$ es $\mathbf{a}_1^{\top}\mathbf{y}$.
:::

Las ecuaciones normales $2\hat x_1+\hat x_2=2$ y $\hat x_1+2\hat x_2=2$ tienen la solución $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$. Con ella, $\hat{\mathbf{y}}=\mathbf{H}\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}$ y el residuo es $\mathbf{r}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$. Comprobación: $\mathbf{a}_1^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$ y $\mathbf{a}_2^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$. La longitud del residuo es $\sqrt{3/9}\approx0{,}577$, más corta que en los dos intentos de la subsección anterior.

⁠**En resumen:** Las ecuaciones normales $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ exigen que el residuo sea perpendicular a todas las columnas.

### Por qué las ecuaciones normales dan la mejor solución

<span class="anker" id="stufe-3-4"></span>

Que un residuo perpendicular corresponda al punto más cercano era, en la recta, el teorema de Pitágoras. El mismo argumento sirve aquí: descompone el error en una parte en la que se puede influir eligiendo $\mathbf{x}$ y otra en la que no se puede influir.

:::satz Teorema 3.4 (Las ecuaciones normales dan la mejor solución aproximada)
<span class="anker" id="satz-3-4"></span>

Si $\hat{\mathbf{x}}$ resuelve las ecuaciones normales, para todo vector $\mathbf{x}$ se cumple

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert^2+\lVert\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})\rVert^2 . \tag{3.4}$$

Por tanto, $\hat{\mathbf{x}}$ es una mejor solución aproximada. A la inversa, toda mejor solución aproximada resuelve las ecuaciones normales, y todas las mejores soluciones aproximadas dan el mismo punto $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}$.
:::

:::beweis Mejor solución aproximada
Se descompone $\mathbf{y}-\mathbf{A}\mathbf{x}=(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})+\mathbf{A}(\hat{\mathbf{x}}-\mathbf{x})$. El primer sumando es el residuo $\mathbf{r}$ de $\hat{\mathbf{x}}$; el segundo está en el espacio columna. Según las ecuaciones normales, $\mathbf{r}$ es perpendicular al espacio columna, y el teorema de Pitágoras da [(3.4)](#gl-3-4). El segundo sumando de la derecha nunca es negativo; por tanto, $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\ge\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert$ para todo $\mathbf{x}$.

Si $\mathbf{x}$ es también una mejor solución aproximada, ambas longitudes son iguales, y [(3.4)](#gl-3-4) obliga a que $\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})=\mathbf{0}$. Entonces $\mathbf{A}\mathbf{x}=\mathbf{A}\hat{\mathbf{x}}$; ambas dan, por tanto, el mismo punto y el mismo residuo, y $\mathbf{x}$ también cumple las ecuaciones normales.
:::

⁠**Ejemplo numérico:** Para $\mathbf{H}$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ y $\mathbf{x}=(1,\,0)^{\top}$ es $\lVert\mathbf{y}-\mathbf{H}\mathbf{x}\rVert^2=1$. El lado derecho de [(3.4)](#gl-3-4) es $\lVert\mathbf{r}\rVert^2=\tfrac13$ más $\lVert\mathbf{H}(\tfrac13,\,-\tfrac23)^{\top}\rVert^2=\lVert(\tfrac13,\,-\tfrac23,\,-\tfrac13)^{\top}\rVert^2=\tfrac69$, en total $\tfrac13+\tfrac23=1$.

⁠**En resumen:** Pitágoras descompone el error cuadrático en el residuo perpendicular, que ninguna elección de $\mathbf{x}$ puede reducir, y una parte en el espacio columna, que se anula en $\hat{\mathbf{x}}$.

:::hintergrund En qué se puede influir y en qué no
La fórmula [(3.4)](#gl-3-4) explica por qué precisamente la perpendicularidad es la condición correcta. Todo candidato $\mathbf{A}\mathbf{x}$ está en el espacio columna. La distancia a $\mathbf{y}$ se compone de dos tramos perpendiculares entre sí: un tramo en el espacio columna, de $\mathbf{A}\mathbf{x}$ a $\hat{\mathbf{y}}$, y el tramo $\mathbf{r}$ perpendicular a él, de $\hat{\mathbf{y}}$ a $\mathbf{y}$. El primer tramo puede modificarse a voluntad eligiendo $\mathbf{x}$ y, en particular, reducirse a cero. El segundo no depende en absoluto de $\mathbf{x}$: es la parte de $\mathbf{y}$ que las columnas no alcanzan con ninguna combinación lineal. La mejor solución aproximada es justo la que anula el tramo modificable. Que los dos tramos se sumen según Pitágoras y no puedan compensarse mutuamente se debe a su ángulo recto.
:::

### Cuándo es única la mejor solución aproximada

<span class="anker" id="stufe-3-5"></span>

Las ecuaciones normales son un sistema cuadrado. Que tenga exactamente una solución depende de si $\mathbf{A}^{\top}\mathbf{A}$ es invertible. Y eso, a su vez, lo deciden las columnas de $\mathbf{A}$.

:::satz Teorema 3.5 (Invertibilidad de $\mathbf{A}^{\top}\mathbf{A}$)
<span class="anker" id="satz-3-5"></span>

La matriz $\mathbf{A}^{\top}\mathbf{A}$ es invertible si y solo si las columnas de $\mathbf{A}$ son linealmente independientes. En ese caso, la mejor solución aproximada es única:

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y} . \tag{3.5}$$
:::

:::beweis Invertibilidad
Según la parte 1, sección 13.5, la matriz cuadrada $\mathbf{A}^{\top}\mathbf{A}$ es invertible si y solo si su núcleo solo contiene el vector nulo. Sea $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Entonces también $\mathbf{z}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=0$, es decir, $\lVert\mathbf{A}\mathbf{z}\rVert^2=0$ y $\mathbf{A}\mathbf{z}=\mathbf{0}$. A la inversa, de $\mathbf{A}\mathbf{z}=\mathbf{0}$ se sigue inmediatamente $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Los dos núcleos son, por tanto, iguales. El núcleo de $\mathbf{A}$ solo contiene el vector nulo si y solo si las columnas de $\mathbf{A}$ son linealmente independientes.
:::

Si las columnas son linealmente dependientes, hay infinitas mejores soluciones aproximadas. A una de ellas se le puede sumar cualquier vector del núcleo de $\mathbf{A}$ sin cambiar $\mathbf{A}\hat{\mathbf{x}}$. El punto más cercano $\hat{\mathbf{y}}$ es, aun así, único, como muestra el teorema de la subsección anterior. Esto encaja con la parte 1, sección 13.6: las características dependientes hacen ambiguos los pesos, pero no las predicciones.

⁠**Ejemplo numérico 1:** Las columnas de $\mathbf{H}$ son linealmente independientes, y $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ tiene la inversa $\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$. Con [(3.5)](#gl-3-5) es $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(2,\,2)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$, como antes.

⁠**Ejemplo numérico 2:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ y $\mathbf{y}=(1,\,1)^{\top}$, las columnas son dependientes. Las ecuaciones normales son $\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)\hat{\mathbf{x}}=(3,\,6)^{\top}$, es decir, dos veces la misma ecuación $\hat x_1+2\hat x_2=\tfrac35$. Cada punto de esta recta es una mejor solución aproximada, por ejemplo $(\tfrac35,\,0)^{\top}$ o $(0,\,\tfrac3{10})^{\top}$. Todas dan el mismo punto $\hat{\mathbf{y}}=(\tfrac35,\,\tfrac65)^{\top}$, la proyección de $\mathbf{y}$ sobre la recta en la dirección de $(1,\,2)^{\top}$.

⁠**En resumen:** Con columnas linealmente independientes, $\mathbf{A}^{\top}\mathbf{A}$ es invertible y la mejor solución aproximada $\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ es única; si no, hay infinitas, y todas dan el mismo punto más cercano.

### Una recta por tres puntos

<span class="anker" id="stufe-3-6"></span>

Ahora la teoría está completa y puede aplicarse a un problema cotidiano. Tres puntos de medida $(t,\,y)=(0,\,1)$, $(1,\,2)$ y $(2,\,4)$ deben describirse mediante una recta $y=x_1+x_2\,t$. Los tres puntos no están sobre una misma recta. Se buscan la ordenada en el origen $x_1$ y la pendiente $x_2$ que mejor se ajusten.

Cada punto de medida da una ecuación $x_1+x_2\,t_i=y_i$. Con la columna de unos para la ordenada en el origen, como en la parte 1, sección 8.5, esto es el sistema

$$\mathbf{A}\mathbf{x}=\mathbf{y}\qquad\text{con}\qquad \mathbf{A}=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}1\\2\\4\end{pmatrix}.$$

Las componentes del residuo son las distancias verticales de los puntos de medida a la recta, medidas en la dirección $y$ (fig. [8](#abb-8)). La mejor solución aproximada hace la suma de sus cuadrados lo más pequeña posible. Una recta así se llama __recta de ajuste__.

:::abbildung ml/k2ausgleich 8
La recta de ajuste por los puntos de medida $(0,1)$, $(1,2)$ y $(2,4)$. Los segmentos rojos son las componentes del residuo, las distancias verticales de los puntos a la recta en la dirección $y$. La recta hace la suma de sus cuadrados lo más pequeña posible, aquí $\tfrac1{36}+\tfrac19+\tfrac1{36}=\tfrac16$.
:::

⁠**Ejemplo numérico:** Se tiene

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&3\\3&5\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}7\\10\end{pmatrix},\qquad (\mathbf{A}^{\top}\mathbf{A})^{-1}=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix},$$

por tanto, $\hat{\mathbf{x}}=\tfrac16(35-30,\ -21+30)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$. Las entradas de $\mathbf{A}^{\top}\mathbf{A}$ y $\mathbf{A}^{\top}\mathbf{y}$ son sumas sobre los puntos de medida; dos de ellas las muestra la fig. [9](#abb-9). La recta de ajuste es $y=\tfrac56+\tfrac32\,t$. Sus valores en los puntos de medida son $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\,\tfrac73,\,\tfrac{23}6)^{\top}$, y el residuo es $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$, con la suma de cuadrados $\tfrac16$. Comprobación: $\mathbf{A}^{\top}\mathbf{r}=(\tfrac16-\tfrac13+\tfrac16,\ 0-\tfrac13+\tfrac13)^{\top}=(0,\,0)^{\top}$.

La primera componente de la comprobación tiene un significado propio. La primera columna de $\mathbf{A}$ es la columna de unos, y $\mathbf{1}^{\top}\mathbf{r}=0$ significa que los residuos suman cero. La recta no queda, en promedio, ni demasiado alta ni demasiado baja. De forma equivalente, pasa por el centroide de los puntos de medida, aquí $(\bar t,\,\bar y)=(1,\,\tfrac73)$: se tiene $\tfrac56+\tfrac32\cdot1=\tfrac73$.

:::abbildung ml/k2rausgleich 9
Dos entradas de las ecuaciones normales de la recta de ajuste como sumas sobre los tres puntos de medida $(t_i,\,y_i)=(0,1)$, $(1,2)$, $(2,4)$.
:::

⁠**En resumen:** Una recta de ajuste es la mejor solución aproximada del sistema que exige que todos los puntos de medida estén sobre la recta; con una columna de unos, sus residuos suman cero.

:::hintergrund Un filtro que reproduce una señal lo mejor posible
El mismo cálculo sirve para diseñar filtros digitales. Un filtro con los coeficientes $h_0,\dots,h_{K-1}$ debe reproducir lo mejor posible, a partir de una señal de entrada $x[n]$, una señal deseada $d[n]$, con la salida $\sum_kh_k\,x[n-k]$. Para cada instante $n$ esto es una ecuación para las $K$ incógnitas $h_k$; para muchos instantes, por tanto, un sistema sobredeterminado $\mathbf{X}\mathbf h=\mathbf d$. La fila $n$ de $\mathbf{X}$ contiene $x[n],x[n-1],\dots,x[n-K+1]$. En las ecuaciones normales $\mathbf{X}^{\top}\mathbf{X}\mathbf h=\mathbf{X}^{\top}\mathbf d$, la entrada $(k,l)$ de $\mathbf{X}^{\top}\mathbf{X}$ es la suma $\sum_nx[n-k]\,x[n-l]$, es decir, salvo efectos de borde al principio y al final de la señal, la autocorrelación de $x$ para el desplazamiento $l-k$. En $\mathbf{X}^{\top}\mathbf d$ está la correlación cruzada de $d$ y $x$. Son exactamente los productos escalares de señales desplazadas de la parte 1, sección 2.4. El residuo $d[n]-\sum_kh_k\,x[n-k]$ del mejor filtro es, según [(3.3)](#gl-3-3), perpendicular a cada señal de entrada desplazada: lo que el filtro no puede reproducir no tiene nada en común con ninguna de las señales a partir de las cuales compone la salida.
:::

### Las viviendas: lo que la parte 1 dejó abierto

<span class="anker" id="stufe-3-7"></span>

Ahora puede responderse la pregunta del comienzo de la sección. Se buscan los pesos para la superficie y el número de habitaciones que acierten los cuatro precios lo mejor posible.

⁠**Ejemplo numérico:** Para el sistema $\mathbf{A}\mathbf{w}=\mathbf{y}$ de la primera subsección se tiene

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}18\,200&730\\730&30\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}60\,100\\2\,410\end{pmatrix}.$$

La fig. [10](#abb-10) calcula dos de las entradas.

:::abbildung ml/k2rwohnungen 10
Dos entradas de las ecuaciones normales de las viviendas como productos escalares: $\mathbf{a}_1=(60,40,90,70)^{\top}$ es la columna de superficies, $\mathbf{a}_2=(2,1,4,3)^{\top}$ la de habitaciones y $\mathbf{y}=(200,130,290,240)^{\top}$ el vector de precios.
:::

Las dos columnas son linealmente independientes; el determinante es $18\,200\cdot30-730^2=13\,100$. Con la inversa de la parte 1, sección 11.3, se tiene

$$\hat{\mathbf{w}}=\frac1{13\,100}\begin{pmatrix}30&-730\\-730&18\,200\end{pmatrix}\begin{pmatrix}60\,100\\2\,410\end{pmatrix}=\frac1{13\,100}\begin{pmatrix}43\,700\\-11\,000\end{pmatrix}=\begin{pmatrix}437/131\\-110/131\end{pmatrix}\approx\begin{pmatrix}3{,}336\\-0{,}840\end{pmatrix}.$$

Los precios estimados son $\mathbf{A}\hat{\mathbf{w}}\approx(198{,}47;\ 132{,}60;\ 296{,}87;\ 230{,}99)^{\top}$, y el residuo es

$$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{w}}=\frac{20}{131}\,(10,\,-17,\,-45,\,59)^{\top}\approx(1{,}53;\ -2{,}60;\ -6{,}87;\ 9{,}01)^{\top}$$

con la longitud $\lVert\mathbf{r}\rVert\approx11{,}72$. Los pesos $(3,\,10)^{\top}$ de la parte 1 acertaban tres precios exactamente, pero dejaban un residuo de longitud $20$. La mejor solución aproximada no acierta ningún precio exactamente, pero en conjunto se desvía claramente menos. Comprobación: $\mathbf{A}^{\top}\mathbf{r}=\frac{20}{131}(600-680-4050+4130,\ 20-17-180+177)^{\top}=\mathbf{0}$.

⁠**En resumen:** La mejor solución aproximada para las viviendas son los pesos $\hat{\mathbf{w}}\approx(3{,}336;\ -0{,}840)^{\top}$; su residuo, de longitud $11{,}72$, es claramente más corto que cualquier residuo que acierte tres precios exactamente.

:::hintergrund Por qué el peso de las habitaciones es negativo
Un peso negativo para el número de habitaciones parece a primera vista erróneo: más habitaciones no deberían bajar el precio. Aun así, el cálculo es correcto, y la razón está en los datos. En estas cuatro viviendas, la superficie y el número de habitaciones crecen juntos: cuanto más grande es la vivienda, más habitaciones tiene. Por eso, las dos columnas de $\mathbf{A}$ apuntan casi en la misma dirección; según la parte 1, sección 5.2, el coseno de su ángulo es $730/\sqrt{18\,200\cdot30}\approx0{,}988$, es decir, el ángulo es de solo unos $8{,}9^\circ$. La mejor combinación toma mucho de la columna de superficies y vuelve a restar un poco de la columna de habitaciones, para compensar las desviaciones de las viviendas respecto a la proporción común. A igual superficie, más habitaciones significan aquí habitaciones más pequeñas, y eso puede efectivamente bajar un precio; pero cuatro viviendas no bastan para mostrar si es así. Como en la parte 1, sección 13.6: cuando las características llevan casi la misma información, los pesos individuales dicen poco, y las predicciones, en cambio, mucho.
:::

:::aufgabe Ejercicio 7 ★ Ecuaciones normales a mano
<span class="anker" id="aufg-7"></span>

El sistema $x_1=1$, $x_2=2$, $x_1+x_2=6$ no tiene solución.

<ol class="al">

<li>

Escríbelo como $\mathbf{A}\mathbf{x}=\mathbf{y}$, plantea las ecuaciones normales y resuélvelas.

</li>

<li>

Calcula el residuo y comprueba que es perpendicular a ambas columnas. ¿Por cuánto falla la mejor solución aproximada cada una de las tres ecuaciones?

</li>

</ol>

:::loesung
(a) Con $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ y $\mathbf{y}=(1,\,2,\,6)^{\top}$ se tiene $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ y $\mathbf{A}^{\top}\mathbf{y}=(1+6,\ 2+6)^{\top}=(7,\,8)^{\top}$. Las ecuaciones normales $2\hat x_1+\hat x_2=7$, $\hat x_1+2\hat x_2=8$ tienen la solución

$$\hat{\mathbf{x}}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix}=\frac13\begin{pmatrix}6\\9\end{pmatrix}=\begin{pmatrix}2\\3\end{pmatrix}.$$

(b) $\mathbf{A}\hat{\mathbf{x}}=(2,\,3,\,5)^{\top}$ y $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}=(-1,\,-1,\,1)^{\top}$. Comprobación: $\mathbf{a}_1^{\top}\mathbf{r}=-1+0+1=0$ y $\mathbf{a}_2^{\top}\mathbf{r}=0-1+1=0$. La mejor solución aproximada falla cada una de las tres ecuaciones exactamente por $1$: $\hat x_1=2$ en lugar de $1$, $\hat x_2=3$ en lugar de $2$, $\hat x_1+\hat x_2=5$ en lugar de $6$. Reparte la contradicción por igual; $\lVert\mathbf{r}\rVert^2=3$.
:::
:::

:::aufgabe Ejercicio 8 ★★ Una recta de ajuste
<span class="anker" id="aufg-8"></span>

Determina la recta de ajuste $y=x_1+x_2\,t$ por los puntos $(1,\,2)$, $(2,\,3)$ y $(3,\,5)$. Calcula el residuo, comprueba $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ y demuestra que la recta pasa por el centroide de los tres puntos.

:::loesung
Con $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&2\\1&3\end{smallmatrix}\Bigr)$ y $\mathbf{y}=(2,\,3,\,5)^{\top}$ se tiene

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&6\\6&14\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}10\\23\end{pmatrix},\qquad \hat{\mathbf{x}}=\frac16\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}10\\23\end{pmatrix}=\frac16\begin{pmatrix}2\\9\end{pmatrix}=\begin{pmatrix}1/3\\3/2\end{pmatrix}.$$

La recta de ajuste es $y=\tfrac13+\tfrac32\,t$, con los valores $\tfrac{11}6$, $\tfrac{10}3$, $\tfrac{29}6$ en los puntos de medida. El residuo es $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$, y $\mathbf{A}^{\top}\mathbf{r}=\bigl(\tfrac16-\tfrac13+\tfrac16,\ \tfrac16-\tfrac23+\tfrac12\bigr)^{\top}=(0,\,0)^{\top}$. El centroide es $(\bar t,\,\bar y)=(2,\,\tfrac{10}3)$, y $\tfrac13+\tfrac32\cdot2=\tfrac{10}3$: la recta pasa por él. Esto se deduce de la primera componente de $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$: los residuos suman cero; por tanto, $\bar y=\hat x_1+\hat x_2\,\bar t$.
:::
:::

:::aufgabe Ejercicio 9 ★★ Precio base y precio por metro cuadrado
<span class="anker" id="aufg-9"></span>

Los precios de las cuatro viviendas deben estimarse solo a partir de su superficie, con un precio base: $y\approx x_1+x_2\cdot\text{superficie}$.

<ol class="al">

<li>

Escribe $\mathbf{A}$ con la columna de unos y resuelve las ecuaciones normales.

</li>

<li>

Calcula el residuo y su longitud. Compara con el resultado de la última subsección.

</li>

</ol>

:::loesung
(a) La matriz tiene la columna de unos y la columna de las superficies:

$$\mathbf{A}=\begin{pmatrix}1&60\\1&40\\1&90\\1&70\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}4&260\\260&18\,200\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}860\\60\,100\end{pmatrix}.$$

El determinante es $4\cdot18\,200-260^2=72\,800-67\,600=5\,200$, y

$$\hat{\mathbf{x}}=\frac1{5\,200}\begin{pmatrix}18\,200&-260\\-260&4\end{pmatrix}\begin{pmatrix}860\\60\,100\end{pmatrix}=\frac1{5\,200}\begin{pmatrix}26\,000\\16\,800\end{pmatrix}=\begin{pmatrix}5\\42/13\end{pmatrix}\approx\begin{pmatrix}5\\3{,}231\end{pmatrix}.$$

El precio base es de $5$ mil euros, y a él se suman unos $3{,}23$ mil euros por metro cuadrado.

(b) Los precios estimados son $5+\tfrac{42}{13}\cdot\text{superficie}$, y el residuo es

$$\mathbf{r}=\tfrac1{13}\,(15,\,-55,\,-75,\,115)^{\top}\approx(1{,}15;\ -4{,}23;\ -5{,}77;\ 8{,}85)^{\top},\qquad \lVert\mathbf{r}\rVert=\tfrac1{13}\sqrt{22\,100}\approx11{,}44 .$$

Los residuos suman cero, como exige la columna de unos. Con la superficie y el número de habitaciones se obtenía $\lVert\mathbf{r}\rVert\approx11{,}72$; así pues, el precio base y la superficie, también con dos incógnitas, se ajustan algo mejor. La elección de las dos columnas cambia el espacio columna y, con él, el punto más cercano.
:::
:::

:::aufgabe Ejercicio 10 ★★★ Residuos sin columna de unos
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Demuestra: si el espacio columna de $\mathbf{A}$ contiene el vector de unos $\mathbf{1}$, las componentes del residuo de la mejor solución aproximada suman cero.

</li>

<li>

Comprueba con el residuo de las viviendas de la última subsección que, sin columna de unos, la suma de los residuos en general no es cero.

</li>

</ol>

:::loesung
(a) Si $\mathbf{1}$ está en el espacio columna, el residuo de la mejor solución aproximada es, según las ecuaciones normales, perpendicular a $\mathbf{1}$, porque es perpendicular a todo el espacio columna. Por tanto, $\mathbf{1}^{\top}\mathbf{r}=\sum_ir_i=0$.

(b) El residuo de las viviendas es $\tfrac{20}{131}(10,\,-17,\,-45,\,59)^{\top}$, con la suma $\tfrac{20}{131}(10-17-45+59)=\tfrac{140}{131}\approx1{,}07\ne0$. Sin columna de unos, $\mathbf{1}$ no está aquí en el espacio columna, y los residuos no tienen por qué compensarse.
:::
:::
