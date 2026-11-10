---
title: Derivar respecto de vectores y matrices
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230800
summary: Los gradientes de expresiones como a top x , x top Ax o lVerty-AxrVert 2 se necesitan una y otra vez.
tags: convención de disposición
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Los gradientes de expresiones como $\mathbf{a}^{\top}\mathbf{x}$, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ o $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ se necesitan una y otra vez. Esta sección fija primero qué forma tiene cada derivada y deduce después, componente a componente, las fórmulas más importantes. Al final aparecen las derivadas respecto de una matriz y la regla con la que se calcula una sensibilidad hacia atrás a través de un producto de matrices.
:::

### La convención de disposición

<span class="anker" id="stufe-7-1"></span>

En las funciones de una variable, la derivada es un número y no hay nada que ordenar. Con vectores y matrices hay que fijar en qué forma se escriben las muchas derivadas parciales: como columna o como fila, como matriz $m\times n$ o como matriz $n\times m$. Una fijación de este tipo se llama __convención de disposición__. Matemáticamente, cualquier elección es igual de buena; solo hay que mantenerla, porque si no, las fórmulas aparecen de repente traspuestas.

:::definition Definición 7.1 (Convención de disposición de este capítulo)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

Los vectores son columnas. El gradiente de una función $f:\mathbb{R}^n\to\mathbb{R}$ es una columna con la misma forma que $\mathbf{x}$.

</li>

<li>

La matriz jacobiana de una función $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ es una matriz $m\times n$: una fila por salida, una columna por entrada.

</li>

<li>

La derivada de una función $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ respecto de una matriz $\mathbf{A}$ es una matriz $\nabla_{\mathbf{A}}f$ de tamaño $m\times n$ con la entrada $\partial f/\partial a_{ij}$ en la posición $(i,j)$, es decir, con la misma forma que $\mathbf{A}$.

</li>

</ol>
:::

La tabla [2](#tab-2) lo resume. El capítulo ya ha utilizado dos consecuencias: para una función con una salida, la matriz jacobiana es el gradiente como fila, $\mathbf{J}_f=\nabla f^{\top}$. Y la regla de la cadena para gradientes necesita la traspuesta, $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$. La regla (iii) se necesita en la sección [7.5](#stufe-7-5): quien modifica una matriz en una matriz pequeña $\mathbf E$ quiere poder comparar $\nabla_{\mathbf{A}}f$ y $\mathbf E$ entrada por entrada.

<span class="anker" id="tab-2"></span>

**Tabla 2:** La forma de la derivada según el tipo de función, en la convención de este capítulo.

| Función | Derivada | Forma |
|---|---|---|
| $f:\mathbb{R}\to\mathbb{R}$ | $f'(x)$ | número |
| $f:\mathbb{R}^n\to\mathbb{R}$ | $\nabla f(\mathbf{x})$ | columna, $n\times1$ (como $\mathbf{x}$) |
| $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ | $m\times n$ (la fila $i$ es $\nabla g_i^{\top}$) |
| $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ | $\nabla_{\mathbf{A}}f(\mathbf{A})$ | $m\times n$ (como $\mathbf{A}$) |

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$, el gradiente es la columna $\nabla f=(4,\,5)^{\top}$, y la matriz jacobiana, la fila $\mathbf{J}_f=(4\ \ 5)$. Para $\mathbf{g}$ de [(5.1)](die-jacobi-matrix.html#gl-5-1), $\mathbf{J}_{\mathbf{g}}$ es una matriz $2\times2$ cuya primera fila $(2\ \ 1)$ es el gradiente de $g_1=x_1x_2$ como fila.
::::

⁠**En resumen:** En el capítulo, un gradiente tiene la forma de su variable, y una matriz jacobiana tiene una fila por salida; de ahí se siguen $\mathbf{J}_f=\nabla f^{\top}$ y la traspuesta en la regla de la cadena para gradientes.

:::hintergrund Otras convenciones en la bibliografía
Muchos libros escriben el gradiente como fila. Entonces es lo mismo que la matriz jacobiana de una función con una salida, y la regla de la cadena no necesita ninguna trasposición, pues $\nabla(f\circ\mathbf{g})=\nabla f\,\mathbf{J}_{\mathbf{g}}$ es entonces un producto de fila por matriz. El precio es que el gradiente ya no tiene la forma de $\mathbf{x}$; la recta $\mathbf{x}+t\,\nabla f$ en la dirección de máximo ascenso necesita entonces una trasposición. Se distinguen dos disposiciones: en la disposición de numerador, las filas corresponden a las componentes de la función, como en la matriz jacobiana de este capítulo. En la disposición de denominador corresponden a las componentes de la variable; entonces la derivada de una función vectorial es la traspuesta de la matriz jacobiana. Este capítulo usa una forma mixta muy extendida: gradiente como columna y matriz jacobiana en disposición de numerador. Por eso no deben combinarse sin comprobación fórmulas de fuentes distintas. Una prueba rápida es la forma: un gradiente respecto de $\mathbf{x}\in\mathbb{R}^n$ debe tener $n$ entradas en una columna. Una prueba más fiable es un pequeño ejemplo numérico.
:::

### Funciones lineales

<span class="anker" id="stufe-7-2"></span>

La función más sencilla de muchas variables es la suma ponderada. Su gradiente es tan sencillo que puede escribirse de inmediato; la deducción muestra el patrón según el cual surgen todas las demás fórmulas de esta sección.

:::satz Teorema 7.2 (Gradientes de funciones lineales)
<span class="anker" id="satz-7-2"></span>

Para vectores fijos $\mathbf{a},\mathbf{y}$ y una matriz fija $\mathbf{A}$ de forma adecuada se cumple

<span class="anker" id="gl-7-1"></span>
$$\nabla_{\mathbf{x}}(\mathbf{a}^{\top}\mathbf{x})=\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\qquad \nabla_{\mathbf{x}}(\mathbf{y}^{\top}\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\mathbf{y} . \tag{7.1}$$
:::

:::beweis Gradientes de funciones lineales
Se tiene $\mathbf{a}^{\top}\mathbf{x}=\sum_ja_jx_j$. Al derivar respecto de $x_k$ solo queda el sumando con $j=k$, es decir, $a_k$. Como $\mathbf{x}^{\top}\mathbf{a}=\mathbf{a}^{\top}\mathbf{x}$, lo mismo vale para $\mathbf{x}^{\top}\mathbf{a}$. Para la segunda parte se toma $\mathbf{a}=\mathbf{A}^{\top}\mathbf{y}$, pues $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}^{\top}\mathbf{y})^{\top}\mathbf{x}$.
:::

::::beispiel [Ejemplo numérico]
En el [capítulo 1, sección 2.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), la predicción para la vivienda 1, con $\mathbf{x}_1=(60,\,2,\,3)^{\top}$ y los pesos $\mathbf{w}=(3,\,10,\,-4)^{\top}$, era $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$. Como función de los pesos tiene el gradiente $\nabla_{\mathbf{w}}\hat y_1=\mathbf{x}_1=(60,\,2,\,3)^{\top}$. Si se aumenta $w_1$ en $0{,}1$, la predicción sube $60\cdot0{,}1=6$, hasta $194$; en efecto, $3{,}1\cdot60+10\cdot2-4\cdot3=194$. La razón es sencilla: cada peso se multiplica por su característica, y por eso la sensibilidad respecto de un peso es exactamente la característica correspondiente.
::::

⁠**En resumen:** El gradiente de $\mathbf{a}^{\top}\mathbf{x}$ respecto de $\mathbf{x}$ es $\mathbf{a}$; el de $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}$ es $\mathbf{A}^{\top}\mathbf{y}$.

### Formas cuadráticas

<span class="anker" id="stufe-7-3"></span>

Las formas cuadráticas $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ del [capítulo 2, sección 5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5), aparecen allí donde se suman cuadrados. Al derivar, $\mathbf{x}$ aparece en dos lugares, y ambos contribuyen, como los dos caminos de la sección [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2).

:::satz Teorema 7.3 (Gradiente de una forma cuadrática)
<span class="anker" id="satz-7-3"></span>

Para una matriz $\mathbf{A}\in\mathbb{R}^{n\times n}$ se cumple

<span class="anker" id="gl-7-2"></span>
$$\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\,\mathbf{x} . \tag{7.2}$$

Si $\mathbf{A}$ es simétrica, esto es $2\mathbf{A}\mathbf{x}$. En particular, $\nabla\lVert\mathbf{x}\rVert^2=\nabla(\mathbf{x}^{\top}\mathbf{x})=2\mathbf{x}$.
:::

:::beweis Gradiente de una forma cuadrática
Se tiene $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{j=1}^nx_i\,a_{ij}\,x_j$. Al derivar respecto de $x_k$ contribuyen dos grupos de sumandos: los de $i=k$, cuya derivada es $\sum_ja_{kj}x_j=(\mathbf{A}\mathbf{x})_k$, y los de $j=k$, cuya derivada es $\sum_ix_ia_{ik}=(\mathbf{A}^{\top}\mathbf{x})_k$. El sumando con $i=j=k$ es $a_{kk}x_k^2$ y tiene la derivada $2a_{kk}x_k$; está contenido en cada uno de los dos grupos una vez, con $a_{kk}x_k$. Así pues, la componente $k$ del gradiente es $(\mathbf{A}\mathbf{x})_k+(\mathbf{A}^{\top}\mathbf{x})_k$.
:::

Según el [capítulo 2, sección 5.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-2), la forma cuadrática solo depende de la parte simétrica $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$. La fórmula encaja con ello: $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$ se tiene $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$, es decir, $6$ en el punto $\mathbf{x}=(1,\,1)^{\top}$. Según [(7.2)](#gl-7-2),

$$\nabla f(1,1)=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=\begin{pmatrix}2&2\\2&6\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}2+2\\2+6\end{pmatrix}=\begin{pmatrix}4\\8\end{pmatrix}.$$

Comprobación con las derivadas parciales $2x_1+2x_2=4$ y $2x_1+6x_2=8$. La fórmula $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$, que solo vale para matrices simétricas, sería aquí incorrecta.
::::

⁠**En resumen:** El gradiente de $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ es $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, es decir, $2\mathbf{A}\mathbf{x}$ si $\mathbf{A}$ es simétrica, y el de $\lVert\mathbf{x}\rVert^2$ es $2\mathbf{x}$.

### La suma de cuadrados de un residuo

<span class="anker" id="stufe-7-4"></span>

En el [capítulo 2, sección 3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3), el residuo $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ era el vector de error de un sistema de ecuaciones $\mathbf{A}\mathbf{x}=\mathbf{y}$ que no tiene solución, y se buscaba el $\mathbf{x}$ con el residuo más corto. La suma de cuadrados $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ es una función de $\mathbf{x}$, y su gradiente dice cómo reacciona a una variación de $\mathbf{x}$.

:::satz Teorema 7.4 (Gradiente de la suma de cuadrados)
<span class="anker" id="satz-7-4"></span>

Para $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ con $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{y}\in\mathbb{R}^m$ se cumple

<span class="anker" id="gl-7-3"></span>
$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})=2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x}-\mathbf{y}). \tag{7.3}$$
:::

:::beweis Gradiente de la suma de cuadrados
La función es una composición: primero, la aplicación afín $\mathbf{r}(\mathbf{x})=\mathbf{y}-\mathbf{A}\mathbf{x}$ forma el residuo; después, $\mathbf{r}\mapsto\lVert\mathbf{r}\rVert^2$ forma su suma de cuadrados. Según la sección [5.4](die-jacobi-matrix.html#stufe-5-4), $\mathbf{J}_{\mathbf{r}}=-\mathbf{A}$; según [(7.2)](#gl-7-2), $\nabla_{\mathbf{r}}\lVert\mathbf{r}\rVert^2=2\mathbf{r}$. La regla de la cadena [(6.3)](die-kettenregel-fur-mehrere-variablen.html#gl-6-3) da $\nabla f=(-\mathbf{A})^{\top}\,2\mathbf{r}=-2\mathbf{A}^{\top}\mathbf{r}$.
:::

::::beispiel [Ejemplo numérico]
Sean $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$, $\mathbf{y}=(1,\,0)^{\top}$ y $\mathbf{x}=(2,\,1)^{\top}$. Entonces $\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, el residuo es $\mathbf{r}=(-3,\,-1)^{\top}$ y $f(\mathbf{x})=9+1=10$. Con $\mathbf{A}^{\top}\mathbf{r}=(-3,\,-7)^{\top}$ se tiene

$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}\mathbf{r}=-2\begin{pmatrix}-3\\-7\end{pmatrix}=\begin{pmatrix}6\\14\end{pmatrix}$$

(fig. [13](#abb-13)). Comprobación: escrita explícitamente, $f(\mathbf{x})=(1-x_1-2x_2)^2+x_2^2$, con las derivadas parciales $-2\,(1-x_1-2x_2)=6$ y $-4\,(1-x_1-2x_2)+2x_2=12+2=14$.

:::abbildung ml/k3rresiduum 13
El gradiente de la suma de cuadrados $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$: cada componente de $\mathbf{A}^{\top}\mathbf{r}$ es el producto escalar de una columna de $\mathbf{A}$ por el residuo.
:::
::::

La fórmula enlaza con el [capítulo 2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html). Allí, el residuo de la mejor solución aproximada $\hat{\mathbf{x}}$ era perpendicular a todas las columnas de $\mathbf{A}$, es decir, $\mathbf{A}^{\top}\hat{\mathbf{r}}=\mathbf{0}$, y de ello se seguían las ecuaciones normales $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$. Según [(7.3)](#gl-7-3), esto significa: en el punto $\hat{\mathbf{x}}$, el gradiente de la suma de cuadrados es nulo; allí la suma no sube ni baja en ninguna dirección, salvo por términos de segundo orden. Para el ejemplo del [capítulo 2, sección 3.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-3), con la matriz $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ y $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$, se tiene $\hat{\mathbf{r}}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ y $\mathbf{A}^{\top}\hat{\mathbf{r}}=(\tfrac13-\tfrac13,\ \tfrac13-\tfrac13)^{\top}=\mathbf{0}$.

⁠**En resumen:** El gradiente de $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ es $-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$; se anula exactamente donde el residuo es perpendicular a las columnas de $\mathbf{A}$.

### Derivar respecto de una matriz

<span class="anker" id="stufe-7-5"></span>

A veces la variable no es un vector, sino una matriz entera: ¿cómo cambia un número cuando se modifica una entrada de una matriz? Según la regla (iii) de la convención, las $m\cdot n$ derivadas parciales se ordenan con la forma de la matriz. Entonces la aproximación lineal vale como de costumbre, solo que el producto escalar recorre todas las entradas:

<span class="anker" id="gl-7-4"></span>
$$f(\mathbf{A}+\mathbf E)\approx f(\mathbf{A})+\sum_{i=1}^m\sum_{j=1}^n\bigl(\nabla_{\mathbf{A}}f\bigr)_{ij}\,e_{ij} \tag{7.4}$$

para una matriz pequeña $\mathbf E$ con las entradas $e_{ij}$. La suma doble es lo mismo que $\operatorname{tr}\bigl((\nabla_{\mathbf{A}}f)^{\top}\mathbf E\bigr)$, con la traza del [capítulo 2, sección 6.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5).

:::satz Teorema 7.5 (Dos derivadas respecto de una matriz)
<span class="anker" id="satz-7-5"></span>

Para vectores fijos $\mathbf{u}\in\mathbb{R}^m$, $\mathbf{v}\in\mathbb{R}^n$ y una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ se cumple

<span class="anker" id="gl-7-5"></span>
$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top},\qquad \nabla_{\mathbf{A}}\lVert\mathbf{A}\rVert_F^2=2\mathbf{A} . \tag{7.5}$$

Aquí, $\lVert\mathbf{A}\rVert_F$ es la norma de Frobenius del [capítulo 2, sección 10.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/naherung-durch-matrizen-von-kleinem-rang.html#stufe-10-1).
:::

:::beweis Dos derivadas respecto de una matriz
Se tiene $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\sum_i\sum_ju_i\,a_{ij}\,v_j$. La entrada $a_{ij}$ aparece exactamente en un sumando, con el factor $u_iv_j$. Así pues, $\partial(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})/\partial a_{ij}=u_iv_j$, y esta es la entrada $(i,j)$ del producto exterior $\mathbf{u}\mathbf{v}^{\top}$ del [capítulo 1, sección 9.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5). Del mismo modo, $\lVert\mathbf{A}\rVert_F^2=\sum_{i,j}a_{ij}^2$, y su derivada $\partial/\partial a_{ij}$ es $2a_{ij}$.
:::

::::beispiel [Ejemplo numérico]
Para $\mathbf{u}=(1,\,2)^{\top}$ y $\mathbf{v}=(3,\,-1)^{\top}$ se tiene

$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}=\begin{pmatrix}3&-1\\6&-2\end{pmatrix},$$

en cualquier punto $\mathbf{A}$, pues la función es lineal en $\mathbf{A}$. Para $\mathbf{A}=\mathbf{I}$, $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}=3-2=1$. Si se aumenta la entrada $a_{21}$ en $0{,}1$, el gradiente predice una variación de $6\cdot0{,}1=0{,}6$. En efecto, $a_{21}$ solo aparece en el sumando $u_2\,a_{21}\,v_1=2\cdot a_{21}\cdot3$, y este crece $0{,}6$.
::::

⁠**En resumen:** La derivada de un número respecto de una matriz tiene la forma de la matriz; para $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}$ es el producto exterior $\mathbf{u}\mathbf{v}^{\top}$, y para $\lVert\mathbf{A}\rVert_F^2$ es $2\mathbf{A}$.

### Hacia atrás a través de un producto de matrices

<span class="anker" id="stufe-7-6"></span>

A menudo, un producto matriz-vector $\mathbf{y}=\mathbf{A}\mathbf{x}$ es solo un paso intermedio de un cálculo más largo, al final del cual hay un número $f(\mathbf{y})$. Si ya se sabe cómo reacciona este número a $\mathbf{y}$, es decir, $\nabla f(\mathbf{y})$, se quiere deducir de ahí cómo reacciona a $\mathbf{A}$ y a $\mathbf{x}$. Este cálculo hacia atrás a través de un bloque es el patrón del modo inverso de la sección [10](automatische-differentiation.html#stufe-10).

:::satz Teorema 7.6 (Regla hacia atrás del producto de matrices)
<span class="anker" id="satz-7-6"></span>

Sean $f:\mathbb{R}^m\to\mathbb{R}$ diferenciable, $\mathbf{y}=\mathbf{A}\mathbf{x}$ con $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $F(\mathbf{A},\mathbf{x})=f(\mathbf{A}\mathbf{x})$. Entonces

<span class="anker" id="gl-7-6"></span>
$$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\,\nabla f(\mathbf{y}). \tag{7.6}$$

Más en general, para $\mathbf{C}=\mathbf{A}\mathbf{B}$ y $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ se cumple: $\nabla_{\mathbf{A}}F=(\nabla_{\mathbf{C}}f)\,\mathbf{B}^{\top}$ y $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\,(\nabla_{\mathbf{C}}f)$.
:::

:::beweis Regla hacia atrás del producto de matrices
Se tiene $y_i=\sum_ka_{ik}x_k$. La entrada $a_{ij}$ solo influye en $y_i$, y lo hace con el factor $\partial y_i/\partial a_{ij}=x_j$. Hay, pues, un solo camino de $a_{ij}$ a $f$, y $\partial F/\partial a_{ij}=\frac{\partial f}{\partial y_i}\,x_j$; esta es la entrada $(i,j)$ de $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$. La variable $x_j$, en cambio, influye en cada $y_i$, con el factor $a_{ij}$; sumando sobre todos los caminos, $\partial F/\partial x_j=\sum_i\frac{\partial f}{\partial y_i}\,a_{ij}$, la componente $j$ de $\mathbf{A}^{\top}\nabla f(\mathbf{y})$. La segunda afirmación se sigue del mismo modo, porque $\mathbf{C}=\mathbf{A}\mathbf{B}$ es, columna a columna, un producto matriz-vector.
:::

::::beispiel [Ejemplo numérico]
En el [capítulo 1, sección 7.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-1), se tenía $\mathbf{A}=\Bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\Bigr)$ y $\mathbf{x}=(2,\,1)^{\top}$, es decir, $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$. Sea $f(\mathbf{y})=y_1-y_3=-3$, es decir, $\nabla f(\mathbf{y})=(1,\,0,\,-1)^{\top}$. Según [(7.6)](#gl-7-6),

$$\nabla_{\mathbf{A}}F=\begin{pmatrix}1\\0\\-1\end{pmatrix}\begin{pmatrix}2&1\end{pmatrix}=\begin{pmatrix}2&1\\0&0\\-2&-1\end{pmatrix},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\begin{pmatrix}1\\0\\-1\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$$

(fig. [14](#abb-14)). Comprobación: escrita explícitamente, $F=(x_1+2x_2)-(3x_1+x_2)=-2x_1+x_2$, con el gradiente $(-2,\,1)^{\top}$. La segunda fila de $\nabla_{\mathbf{A}}F$ es nula porque $y_2$ no aparece en $f$; las entradas de la segunda fila de $\mathbf{A}$ solo actúan sobre $y_2$.

:::abbildung ml/k3rrueck 14
El gradiente respecto de la entrada de un producto matriz-vector: cada componente reúne, sobre las tres salidas $y_i$, cuánto reacciona $f$ a $y_i$, ponderado con el factor $a_{ij}$ con el que $x_j$ actúa sobre $y_i$.
:::
::::

:::warnung La comprobación de la forma es una regla mnemotécnica, no una demostración
Las formas casi fijan [(7.6)](#gl-7-6): $\nabla_{\mathbf{A}}F$ debe tener la forma $m\times n$, y a partir de la columna $\nabla f(\mathbf{y})$ con $m$ entradas y la columna $\mathbf{x}$ con $n$ entradas, solo $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ da esa forma. Así puede recordarse la regla. Pero la comprobación de la forma no detecta ni un signo incorrecto, ni un factor que falta, ni un orden intercambiado en matrices cuadradas. La regla solo queda justificada por el cálculo con las componentes.
:::

⁠**En resumen:** Hacia atrás a través de $\mathbf{y}=\mathbf{A}\mathbf{x}$: el gradiente respecto de $\mathbf{A}$ es $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$; el gradiente respecto de $\mathbf{x}$ es $\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

:::aufgabe Ejercicio 24 ★ Gradientes en notación matricial
<span class="anker" id="aufg-24"></span>

Calcula con las fórmulas de esta sección y haz en cada caso la comprobación con las derivadas parciales.

<ol class="al">

<li>

$f(\mathbf{x})=\mathbf{b}^{\top}\mathbf{x}+5$ con $\mathbf{b}=(2,\,-1,\,4)^{\top}$;

</li>

<li>

$f(\mathbf{x})=\lVert\mathbf{x}\rVert^2$ en el punto $(1,\,-1,\,2)$;

</li>

<li>

$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ con $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\3&4\end{smallmatrix}\bigr)$ en el punto $(1,\,-1)$.

</li>

</ol>

:::loesung
(a) Según [(7.1)](#gl-7-1), $\nabla f=\mathbf{b}=(2,\,-1,\,4)^{\top}$. Comprobación: $f=2x_1-x_2+4x_3+5$.

(b) Según [(7.2)](#gl-7-2) con $\mathbf{A}=\mathbf{I}$, $\nabla f=2\mathbf{x}=(2,\,-2,\,4)^{\top}$. Comprobación: $\partial_jf=2x_j$.

(c) $\mathbf{A}+\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&4\\4&8\end{smallmatrix}\bigr)$, así que $\nabla f(1,-1)=(4-4,\ 4-8)^{\top}=(0,\,-4)^{\top}$. Comprobación: $f=2x_1^2+4x_1x_2+4x_2^2$ tiene las derivadas parciales $4x_1+4x_2=0$ y $4x_1+8x_2=-4$.
:::
:::

:::aufgabe Ejercicio 25 ★★ La recta de ajuste del capítulo 2
<span class="anker" id="aufg-25"></span>

En el [capítulo 2, sección 3.6](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-6), se trazó una recta por los puntos $(0,\,1)$, $(1,\,2)$ y $(2,\,4)$, con $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ y $\mathbf{y}=(1,\,2,\,4)^{\top}$.

<ol class="al">

<li>

Calcula $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ y $\nabla f(\mathbf{x})$ en el punto $\mathbf{x}=(1,\,1)^{\top}$.

</li>

<li>

¿En qué dirección habría que desplazar $\mathbf{x}$ un pequeño trecho desde $(1,\,1)$ para que $f$ disminuya lo más rápido posible?

</li>

<li>

Demuestra que el gradiente en el punto $\hat{\mathbf{x}}=(\tfrac56,\,\tfrac32)^{\top}$ del [capítulo 2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) es nulo.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$, $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}=(0,\,0,\,1)^{\top}$ y $f=1$. Con $\mathbf{A}^{\top}\mathbf{r}=(0+0+1,\ 0+0+2)^{\top}=(1,\,2)^{\top}$ se tiene $\nabla f=-2\mathbf{A}^{\top}\mathbf{r}=(-2,\,-4)^{\top}$.

(b) $f$ disminuye lo más rápido en la dirección $-\nabla f/\lVert\nabla f\rVert=(2,\,4)^{\top}/\sqrt{20}=(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$: la ordenada en el origen debe crecer un poco, y la pendiente, el doble. Esto concuerda con que la recta $1+t$ queda a $1$ del tercer punto, $(2,\,4)$.

(c) $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\ \tfrac73,\ \tfrac{23}6)^{\top}$, así que $\hat{\mathbf{r}}=(\tfrac16,\ -\tfrac13,\ \tfrac16)^{\top}$ y

$$\mathbf{A}^{\top}\hat{\mathbf{r}}=\begin{pmatrix}\tfrac16-\tfrac13+\tfrac16\\0-\tfrac13+\tfrac26\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$

El gradiente es nulo: en la mejor solución aproximada, ningún pequeño desplazamiento cambia la suma de cuadrados en primer orden.
:::
:::

:::aufgabe Ejercicio 26 ★★ Derivadas respecto de una matriz
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Demuestra $\nabla_{\mathbf{A}}\operatorname{tr}\mathbf{A}=\mathbf{I}$ para $\mathbf{A}$ cuadrada.

</li>

<li>

Demuestra con [(7.6)](#gl-7-6) y $\nabla\lVert\mathbf{y}\rVert^2=2\mathbf{y}$ que $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$, y calcúlalo para $\mathbf{A}=\mathbf{I}\in\mathbb{R}^{2\times2}$ y $\mathbf{x}=(1,\,2)^{\top}$.

</li>

<li>

Comprueba (b) con la aproximación lineal [(7.4)](#gl-7-4): ¿en cuánto cambia aproximadamente $\lVert\mathbf{A}\mathbf{x}\rVert^2$ si se aumenta $a_{12}$ de $0$ a $0{,}01$? Verifícalo con el cálculo exacto.

</li>

</ol>

:::loesung
(a) $\operatorname{tr}\mathbf{A}=\sum_ia_{ii}$. La derivada respecto de $a_{ij}$ es $1$ para $i=j$ y $0$ en los demás casos; ordenado con la forma de $\mathbf{A}$, esto es $\mathbf{I}$.

(b) Se tiene $\lVert\mathbf{A}\mathbf{x}\rVert^2=f(\mathbf{y})$ con $\mathbf{y}=\mathbf{A}\mathbf{x}$ y $\nabla f(\mathbf{y})=2\mathbf{y}$. Según [(7.6)](#gl-7-6), $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\mathbf{y}\,\mathbf{x}^{\top}=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$. Para $\mathbf{A}=\mathbf{I}$ y $\mathbf{x}=(1,\,2)^{\top}$:

$$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}2&4\\4&8\end{pmatrix}.$$

(c) La entrada $(1,2)$ del gradiente es $4$, así que [(7.4)](#gl-7-4) predice una variación de unos $4\cdot0{,}01=0{,}04$. Cálculo exacto: con $a_{12}=0{,}01$ se tiene $\mathbf{A}\mathbf{x}=(1{,}02;\ 2)^{\top}$ y $\lVert\mathbf{A}\mathbf{x}\rVert^2=1{,}0404+4=5{,}0404$, es decir, una variación de $0{,}0404$ respecto de $5$.
:::
:::

:::aufgabe Ejercicio 27 ★★★ La regla hacia atrás para un producto de dos matrices
<span class="anker" id="aufg-27"></span>

Sean $\mathbf{C}=\mathbf{A}\mathbf{B}$ y $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ con $\mathbf G=\nabla_{\mathbf{C}}f$.

<ol class="al">

<li>

Demuestra componente a componente que $\nabla_{\mathbf{A}}F=\mathbf G\mathbf{B}^{\top}$ y $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\mathbf G$.

</li>

<li>

Comprueba ambas fórmulas para $\mathbf{A}=(1\ \ 2)$, $\mathbf{B}=\bigl(\begin{smallmatrix}3\\4\end{smallmatrix}\bigr)$ y $f(\mathbf{C})=c_{11}^2$ escribiendo $F$ explícitamente.

</li>

</ol>

:::loesung
(a) Se tiene $c_{ik}=\sum_ja_{ij}b_{jk}$. La entrada $a_{ij}$ actúa sobre todas las $c_{ik}$ de la fila $i$, con el factor $b_{jk}$; sumando sobre estos caminos, $\partial F/\partial a_{ij}=\sum_kg_{ik}b_{jk}=(\mathbf G\mathbf{B}^{\top})_{ij}$. La entrada $b_{jk}$ actúa sobre todas las $c_{ik}$ de la columna $k$, con el factor $a_{ij}$; por tanto, $\partial F/\partial b_{jk}=\sum_ia_{ij}g_{ik}=(\mathbf{A}^{\top}\mathbf G)_{jk}$.

(b) $\mathbf{C}=1\cdot3+2\cdot4=11$, $F=121$ y $\mathbf G=2c_{11}=22$. Las fórmulas dan $\nabla_{\mathbf{A}}F=22\,(3\ \ 4)=(66\ \ 88)$ y $\nabla_{\mathbf{B}}F=(1,\,2)^{\top}\cdot22=(22,\,44)^{\top}$. Escrita explícitamente, $F=(3a_{11}+4a_{12})^2$, con las derivadas $2\cdot11\cdot3=66$ y $2\cdot11\cdot4=88$, y $F=(b_{11}+2b_{21})^2$, con las derivadas $22$ y $44$.
:::
:::
