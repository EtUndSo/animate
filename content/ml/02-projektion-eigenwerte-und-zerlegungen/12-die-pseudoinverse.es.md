---
title: La pseudoinversa
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15221200
summary: En Fundamentos 1, solo una matriz cuadrada con columnas independientes tenía inversa.
tags: inversa por la izquierda, inversa por la derecha, pseudoinversa
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
En Fundamentos 1, solo una matriz cuadrada con columnas independientes tenía inversa. Esta sección da a toda matriz una especie de inversa: una que invierte por la izquierda cuando hay más ecuaciones que incógnitas, otra que invierte por la derecha cuando hay menos, y una para todos los casos, la pseudoinversa. Esta da siempre la mejor solución aproximada y, si hay varias, la más corta.
:::

### Inversa por la izquierda

<span class="anker" id="stufe-11-1"></span>

Una matriz alta $\mathbf{A}\in\mathbb{R}^{m\times n}$ con $m>n$ no tiene inversa; ni siquiera es cuadrada. Pero puede tener la mitad de la propiedad de una inversa.

:::definition Definición 11.1 (Inversa por la izquierda)
<span class="anker" id="satz-11-1"></span>

Una matriz $\mathbf F\in\mathbb{R}^{n\times m}$ con $\mathbf F\mathbf{A}=\mathbf{I}_n$ se llama __inversa por la izquierda__ de $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Teorema 11.2 (Inversa por la izquierda)
<span class="anker" id="satz-11-2"></span>

$\mathbf{A}$ tiene una inversa por la izquierda si y solo si sus columnas son linealmente independientes. En ese caso,

<span class="anker" id="gl-11-1"></span>
$$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{11.1}$$

es una inversa por la izquierda, y $\mathbf F\mathbf{y}$ es la mejor solución aproximada de $\mathbf{A}\mathbf{x}=\mathbf{y}$.
:::

:::beweis Inversa por la izquierda
Si las columnas son independientes, $\mathbf{A}^{\top}\mathbf{A}$ es invertible según la sección [3.5](die-beste-naherungslosung.html#stufe-3-5), y $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. Según [(3.5)](die-beste-naherungslosung.html#gl-3-5), $\mathbf F\mathbf{y}=\hat{\mathbf{x}}$. A la inversa: si $\mathbf{A}$ tiene una inversa por la izquierda y $\mathbf{A}\mathbf{x}=\mathbf{0}$, entonces $\mathbf{x}=\mathbf F\mathbf{A}\mathbf{x}=\mathbf F\mathbf{0}=\mathbf{0}$; el núcleo es, por tanto, $\{\mathbf{0}\}$, y las columnas son independientes.
:::

Por la derecha, $\mathbf F$ no invierte. El producto $\mathbf{A}\mathbf F=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ es, según [(4.1)](projektion-auf-einen-unterraum.html#gl-4-1), la proyección sobre el espacio columna, y para $m>n$ no es $\mathbf{I}_m$. Además, una matriz alta tiene muchas inversas por la izquierda; [(11.1)](#gl-11-1) es la que corresponde a la proyección ortogonal.

⁠**Ejemplo numérico:** Para $\mathbf{H}$, con las columnas $(1,\,0,\,1)^{\top}$ y $(0,\,1,\,1)^{\top}$, es $(\mathbf{H}^{\top}\mathbf{H})^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ y

$$\mathbf F=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\end{pmatrix}.$$

Se tiene $\mathbf F\mathbf{H}=\tfrac13\bigl(\begin{smallmatrix}2+1&-1+1\\-1+1&2+1\end{smallmatrix}\bigr)=\mathbf{I}_2$, y $\mathbf F(1,\,1,\,1)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$ es la mejor solución aproximada de la sección [3.3](die-beste-naherungslosung.html#stufe-3-3). $\mathbf{H}\mathbf F$ es la matriz de proyección $\tfrac13\Bigl(\begin{smallmatrix}2&-1&1\\-1&2&1\\1&1&2\end{smallmatrix}\Bigr)$ de la sección [4.2](projektion-auf-einen-unterraum.html#stufe-4-2). Otra inversa por la izquierda es $\bigl(\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}\bigr)$, pues las dos primeras filas de $\mathbf{H}$ forman la matriz identidad; pero para $(1,\,1,\,1)^{\top}$ no da la mejor solución aproximada, sino $(1,\,1)^{\top}$.

⁠**En resumen:** Una matriz con columnas independientes tiene la inversa por la izquierda $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$; esta transforma $\mathbf{y}$ en la mejor solución aproximada.

### Inversa por la derecha

<span class="anker" id="stufe-11-2"></span>

En una matriz ancha, con $m<n$, hay menos ecuaciones que incógnitas. Si el sistema es resoluble, tiene infinitas soluciones. Una inversa por la derecha elige una de ellas, y precisamente una especial.

:::definition Definición 11.3 (Inversa por la derecha)
<span class="anker" id="satz-11-3"></span>

Una matriz $\mathbf G\in\mathbb{R}^{n\times m}$ con $\mathbf{A}\mathbf G=\mathbf{I}_m$ se llama __inversa por la derecha__ de $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Teorema 11.4 (Inversa por la derecha y solución más corta)
<span class="anker" id="satz-11-4"></span>

Si las filas de $\mathbf{A}$ son linealmente independientes,

<span class="anker" id="gl-11-2"></span>
$$\mathbf G=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1} \tag{11.2}$$

es una inversa por la derecha. $\mathbf{x}=\mathbf G\mathbf{y}$ resuelve $\mathbf{A}\mathbf{x}=\mathbf{y}$ para todo $\mathbf{y}$ y es, entre todas las soluciones, la de menor longitud.
:::

:::beweis Inversa por la derecha
Las filas de $\mathbf{A}$ son las columnas de $\mathbf{A}^{\top}$; según la sección [3.5](die-beste-naherungslosung.html#stufe-3-5), aplicada a $\mathbf{A}^{\top}$, $\mathbf{A}\mathbf{A}^{\top}$ es invertible. Entonces $\mathbf{A}\mathbf G=\mathbf{A}\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}=\mathbf{I}$ y $\mathbf{A}\mathbf G\mathbf{y}=\mathbf{y}$. Si $\mathbf{x}$ es una solución cualquiera, $\mathbf{A}(\mathbf{x}-\mathbf G\mathbf{y})=\mathbf{0}$; por tanto, $\mathbf{z}=\mathbf{x}-\mathbf G\mathbf{y}$ está en el núcleo. El vector $\mathbf G\mathbf{y}=\mathbf{A}^{\top}\mathbf{w}$, con $\mathbf{w}=(\mathbf{A}\mathbf{A}^{\top})^{-1}\mathbf{y}$, es perpendicular a todo vector del núcleo, pues $(\mathbf{A}^{\top}\mathbf{w})^{\top}\mathbf{z}=\mathbf{w}^{\top}\mathbf{A}\mathbf{z}=0$. Según el teorema de Pitágoras,

$$\lVert\mathbf{x}\rVert^2=\lVert\mathbf G\mathbf{y}+\mathbf{z}\rVert^2=\lVert\mathbf G\mathbf{y}\rVert^2+\lVert\mathbf{z}\rVert^2\ge\lVert\mathbf G\mathbf{y}\rVert^2 ,$$

con igualdad solo para $\mathbf{z}=\mathbf{0}$.
:::

Geométricamente, el conjunto de soluciones es una recta o un plano que no pasa por el origen, y $\mathbf G\mathbf{y}$ es su punto más cercano al origen: el pie de la perpendicular trazada desde el origen.

⁠**Ejemplo numérico:** La única ecuación $x_1+2x_2=5$ tiene $\mathbf{A}=(1\ \ 2)$ y $\mathbf{A}\mathbf{A}^{\top}=5$. Por tanto, $\mathbf G=\tfrac15(1,\,2)^{\top}$ y $\mathbf G\cdot5=(1,\,2)^{\top}$. Todas las soluciones son $(1,\,2)^{\top}+t\,(2,\,-1)^{\top}$, con el cuadrado de la longitud $(1+2t)^2+(2-t)^2=5+5t^2$; la solución más corta es la de $t=0$. El vector $(1,\,2)^{\top}$ es perpendicular a la recta de soluciones, cuya dirección es $(2,\,-1)^{\top}$.

⁠**En resumen:** Una matriz con filas independientes tiene la inversa por la derecha $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$; esta da la solución más corta.

### La pseudoinversa

<span class="anker" id="stufe-11-3"></span>

Si $\mathbf{A}$ no tiene ni columnas independientes ni filas independientes, ambas fórmulas fallan. Un ejemplo es $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ de la sección [3.5](die-beste-naherungslosung.html#stufe-3-5): para $\mathbf{y}=(1,\,1)^{\top}$, todos los puntos de la recta $x_1+2x_2=\tfrac35$ son mejores soluciones aproximadas. La descomposición en valores singulares da una fórmula para toda matriz.

:::definition Definición 11.5 (Pseudoinversa)
<span class="anker" id="satz-11-5"></span>

Sea $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ de rango $r$. La matriz $\mathbf{D}^+\in\mathbb{R}^{n\times m}$ se obtiene de $\mathbf{D}^{\top}$ sustituyendo cada $d_j>0$ por $1/d_j$; los ceros se mantienen. La __pseudoinversa__ de $\mathbf{A}$ es

<span class="anker" id="gl-11-3"></span>
$$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\sum_{j=1}^r\frac1{d_j}\,\mathbf{v}_j\mathbf{u}_j^{\top} . \tag{11.3}$$
:::

Cada bloque invierte un bloque de $\mathbf{A}$: $\mathbf{A}$ transforma $\mathbf{v}_j$ en $d_j\mathbf{u}_j$, y $\mathbf{A}^+$ transforma $\mathbf{u}_j$ en $\mathbf{v}_j/d_j$. Las direcciones $\mathbf{u}_j$ con $j>r$, a las que $\mathbf{A}$ no llega, $\mathbf{A}^+$ las transforma en cero, en lugar de dividir por cero. Si $\mathbf{A}$ es invertible, $\mathbf{A}^+=\mathbf{A}^{-1}$, pues entonces $\mathbf{A}^{-1}=(\mathbf{V}^{\top})^{-1}\mathbf{D}^{-1}\mathbf{U}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$.

⁠**Ejemplo numérico:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ es simétrica y semidefinida positiva, con el valor propio $5$, asociado a $\mathbf{q}=(1,\,2)^{\top}/\sqrt5$, y el valor propio $0$. Según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), $\mathbf{A}=5\,\mathbf{q}\mathbf{q}^{\top}$ es su descomposición compacta, con $d_1=5$ y $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Por tanto,

$$\mathbf{A}^+=\frac15\,\mathbf{q}\mathbf{q}^{\top}=\frac1{25}\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$

⁠**En resumen:** La pseudoinversa $\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ invierte cada bloque $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ con $d_j>0$ y deja en cero las direcciones asociadas al valor singular $0$.

### La mejor solución aproximada más corta

<span class="anker" id="stufe-11-4"></span>

¿Qué hace $\mathbf{A}^+\mathbf{y}$? Reúne las dos subsecciones anteriores.

:::satz Teorema 11.6 (Pseudoinversa y mínimos cuadrados)
<span class="anker" id="satz-11-6"></span>

Para toda matriz $\mathbf{A}$ y todo vector $\mathbf{y}$, $\mathbf{x}^+=\mathbf{A}^+\mathbf{y}$ es una mejor solución aproximada de $\mathbf{A}\mathbf{x}=\mathbf{y}$ y es, entre todas las mejores soluciones aproximadas, la de menor longitud. En particular,

$$\begin{gathered} \mathbf{A}^+=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\quad\text{con columnas independientes},\\ \mathbf{A}^+=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\quad\text{con filas independientes}. \end{gathered}$$
:::

:::beweis Pseudoinversa
Se calcula en las coordenadas de los vectores singulares: $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ y $\boldsymbol\beta=\mathbf{U}^{\top}\mathbf{y}$. Como $\mathbf{U}^{\top}$ conserva las longitudes,

$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{U}^{\top}\mathbf{y}-\mathbf{D}\mathbf{V}^{\top}\mathbf{x}\rVert^2=\lVert\boldsymbol\beta-\mathbf{D}\mathbf{c}\rVert^2=\sum_{j=1}^r(\beta_j-d_jc_j)^2+\sum_{j=r+1}^m\beta_j^2 .$$

La segunda suma no depende de $\mathbf{x}$. La primera es cero, y por tanto lo más pequeña posible, si y solo si $c_j=\beta_j/d_j$ para todo $j\le r$; los $c_j$ con $j>r$ ni siquiera aparecen. Las mejores soluciones aproximadas son, por tanto, exactamente los $\mathbf{x}=\mathbf{V}\mathbf{c}$ con $c_j=\beta_j/d_j$ para $j\le r$ y $c_{r+1},\dots,c_n$ cualesquiera. Su longitud es $\lVert\mathbf{x}\rVert^2=\lVert\mathbf{c}\rVert^2=\sum_{j\le r}(\beta_j/d_j)^2+\sum_{j>r}c_j^2$, mínima para $c_j=0$ cuando $j>r$. Este $\mathbf{c}$ es $\mathbf{D}^+\boldsymbol\beta$; por tanto, $\mathbf{x}=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}\mathbf{y}=\mathbf{A}^+\mathbf{y}$.

Con columnas independientes, según la sección [3.5](die-beste-naherungslosung.html#stufe-3-5), solo hay una mejor solución aproximada, $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$; tiene que coincidir con $\mathbf{A}^+\mathbf{y}$, y eso para todo $\mathbf{y}$. Con filas independientes, el rango es, según Fundamentos 1, sección 13.4, igual a $m$; el espacio columna es, por tanto, todo $\mathbb{R}^m$, y el sistema es resoluble para todo $\mathbf{y}$; las mejores soluciones aproximadas son las soluciones, y la más corta es, según la sección [11.2](#stufe-11-2), $\mathbf G\mathbf{y}$.
:::

⁠**Ejemplo numérico 1:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ y $\mathbf{y}=(1,\,1)^{\top}$ es $\mathbf{x}^+=\tfrac1{25}(1+2,\ 2+4)^{\top}=(0{,}12;\ 0{,}24)^{\top}$. Está sobre la recta de las mejores soluciones aproximadas, pues $0{,}12+2\cdot0{,}24=0{,}6=\tfrac35$, y apunta en la dirección de $(1,\,2)^{\top}$, perpendicular a ella: es su punto más cercano al origen.

⁠**Ejemplo numérico 2:** Una misma magnitud se mide tres veces, con los resultados $4$, $5$ y $9$. El sistema «$x=4$, $x=5$, $x=9$» tiene la matriz $\mathbf{1}\in\mathbb{R}^{3\times1}$, una columna de unos. Su única columna es independiente; por tanto, $\mathbf{1}^+=(\mathbf{1}^{\top}\mathbf{1})^{-1}\mathbf{1}^{\top}=\tfrac13(1,\,1,\,1)$ y

$$x^+=\tfrac13\,\mathbf{1}^{\top}\mathbf{y}=\tfrac13\,(4+5+9)=6 ,$$

la media (fig. [27](#abb-27)). La media de varias mediciones es la mejor solución aproximada del sistema que da cada medición por exacta.

:::abbildung ml/k2rmittel 27
La pseudoinversa de la columna de unos aplicada a los valores medidos $\mathbf{y}=(4,5,9)^{\top}$: el producto escalar con $\mathbf{1}$ es la suma de los valores medidos; dividida por $\mathbf{1}^{\top}\mathbf{1}=3$, da la media.
:::

⁠**En resumen:** $\mathbf{A}^+\mathbf{y}$ es, para toda matriz, una mejor solución aproximada y, si hay varias, la más corta; con columnas o filas independientes, $\mathbf{A}^+$ es la inversa por la izquierda o por la derecha.

:::hintergrund Por qué la pseudoinversa no divide por cero
La pseudoinversa sustituye $1/d_j$ por $0$ donde $d_j=0$. Parece arbitrario, pero se deduce de un paso al límite. La matriz $\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I}$ es invertible para todo $\delta\ne0$, pues sus valores propios son $d_j^2+\delta^2>0$. En las coordenadas de los vectores singulares, $(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ multiplica la coordenada $j$-ésima por

$$\frac{d_j}{d_j^2+\delta^2}\ \xrightarrow{\ \delta\to0\ }\ \begin{cases}1/d_j&\text{para }d_j>0,\\0&\text{para }d_j=0.\end{cases}$$

Por tanto, $\mathbf{A}^+=\lim_{\delta\to0}(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ para toda matriz. El paso al límite muestra también un peligro: la pseudoinversa no depende de forma continua de la matriz. Para $\operatorname{diag}(1;\,\varepsilon)$ con $\varepsilon>0$ pequeño, la pseudoinversa es $\operatorname{diag}(1;\,1/\varepsilon)$, enorme; para $\varepsilon=0$ es $\operatorname{diag}(1;\,0)$. Un valor singular diminuto, que solo por errores de medida o de redondeo no es cero, queda enormemente amplificado por $\mathbf{A}^+$. Por eso, los programas de cálculo numérico tratan como cero los valores singulares que están por debajo de un pequeño umbral. Cuánto amplifican los errores los valores singulares pequeños lo mide la sección siguiente.
:::

:::aufgabe Ejercicio 33 ★ Una inversa por la izquierda
<span class="anker" id="aufg-33"></span>

La recta de ajuste de la sección [3.6](die-beste-naherungslosung.html#stufe-3-6) corresponde a $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Calcula la inversa por la izquierda $\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ y comprueba $\mathbf F\mathbf{A}=\mathbf{I}$.

</li>

<li>

Aplica $\mathbf F$ a $\mathbf{y}=(1,\,2,\,4)^{\top}$ y compara con la sección [3.6](die-beste-naherungslosung.html#stufe-3-6).

</li>

<li>

Lee en las filas de $\mathbf F$ cómo se obtienen la ordenada en el origen y la pendiente de la recta de ajuste para valores medidos cualesquiera $y_1,y_2,y_3$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\bigr)$, con la inversa $\tfrac16\bigl(\begin{smallmatrix}5&-3\\-3&3\end{smallmatrix}\bigr)$; por tanto,

$$\mathbf F=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}=\frac16\begin{pmatrix}5&2&-1\\-3&0&3\end{pmatrix},\qquad \mathbf F\mathbf{A}=\frac16\begin{pmatrix}5+2-1&2-2\\-3+3&6\end{pmatrix}=\mathbf{I} .$$

(b) $\mathbf F(1,\,2,\,4)^{\top}=\tfrac16(5+4-4,\ -3+12)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$, la recta de ajuste de la sección [3.6](die-beste-naherungslosung.html#stufe-3-6).

(c) Para valores medidos cualesquiera, la ordenada en el origen es $\hat x_1=\tfrac16(5y_1+2y_2-y_3)$, y la pendiente, $\hat x_2=\tfrac12(y_3-y_1)$. Los pesos de la ordenada en el origen suman $1$: si todos los valores medidos son iguales, la ordenada en el origen es ese valor. Con tres puntos de medida equiespaciados, la pendiente depende solo de los dos puntos extremos; el punto central solo influye en la altura de la recta.
:::
:::

:::aufgabe Ejercicio 34 ★★ Soluciones más cortas
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Determina la pseudoinversa de $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ y $\mathbf{x}^+$ para $\mathbf{y}=(1,\,3)^{\top}$. Comprueba que $\mathbf{x}^+$ es una mejor solución aproximada y que no existe ninguna más corta.

</li>

<li>

Determina la solución más corta de $x_1+2x_2+2x_3=9$. Compara su longitud con la de la solución $(9,\,0,\,0)^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}=2\,\mathbf{q}\mathbf{q}^{\top}$ con $\mathbf{q}=(1,\,1)^{\top}/\sqrt2$, simétrica y semidefinida positiva; por tanto, esta es ya la descomposición compacta, con $d_1=2$ y $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Así, $\mathbf{A}^+=\tfrac12\mathbf{q}\mathbf{q}^{\top}=\tfrac14\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ y $\mathbf{x}^+=\tfrac14(4,\,4)^{\top}=(1,\,1)^{\top}$. Se tiene $\mathbf{A}\mathbf{x}^+=(2,\,2)^{\top}$, la proyección de $(1,\,3)^{\top}$ sobre la recta en la dirección de $(1,\,1)^{\top}$, pues $\tfrac{1+3}2(1,\,1)^{\top}=(2,\,2)^{\top}$. Las mejores soluciones aproximadas son todos los $\mathbf{x}$ con $x_1+x_2=2$, es decir, $(1+s,\ 1-s)^{\top}$, con el cuadrado de la longitud $2+2s^2$. La más corta es la de $s=0$, y esa es $\mathbf{x}^+$.

(b) $\mathbf{A}=(1\ \ 2\ \ 2)$ tiene $\mathbf{A}\mathbf{A}^{\top}=9$; por tanto, $\mathbf G=\tfrac19(1,\,2,\,2)^{\top}$, y la solución más corta es $\mathbf G\cdot9=(1,\,2,\,2)^{\top}$, de longitud $3$. La solución $(9,\,0,\,0)^{\top}$ tiene longitud $9$. La solución más corta apunta en la dirección del vector normal $(1,\,2,\,2)^{\top}$ del plano de soluciones.
:::
:::

:::aufgabe Ejercicio 35 ★★★ Lo que proyecta la pseudoinversa
<span class="anker" id="aufg-35"></span>

Sea $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ de rango $r$, y sean $\mathbf{U}_r$, $\mathbf{V}_r$ las matrices formadas por las $r$ primeras columnas de $\mathbf{U}$ y $\mathbf{V}$.

<ol class="al">

<li>

Demuestra $\mathbf{A}\mathbf{A}^+=\mathbf{U}_r\mathbf{U}_r^{\top}$ y $\mathbf{A}^+\mathbf{A}=\mathbf{V}_r\mathbf{V}_r^{\top}$. ¿Sobre qué espacios proyectan estas matrices?

</li>

<li>

Deduce $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$ y $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{A}^+=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^+\mathbf{U}^{\top}$. La matriz $\mathbf{D}\mathbf{D}^+$, de tamaño $m\times m$, tiene en los $r$ primeros lugares de la diagonal $d_j\cdot\tfrac1{d_j}=1$ y ceros en el resto. Por tanto, $\mathbf{A}\mathbf{A}^+=\sum_{j\le r}\mathbf{u}_j\mathbf{u}_j^{\top}=\mathbf{U}_r\mathbf{U}_r^{\top}$, que, según [(4.2)](projektion-auf-einen-unterraum.html#gl-4-2), es la proyección ortogonal sobre el espacio generado por $\mathbf{u}_1,\dots,\mathbf{u}_r$, el espacio columna de $\mathbf{A}$. Del mismo modo, $\mathbf{A}^+\mathbf{A}=\mathbf{V}\mathbf{D}^+\mathbf{D}\mathbf{V}^{\top}=\mathbf{V}_r\mathbf{V}_r^{\top}$, la proyección sobre el espacio generado por $\mathbf{v}_1,\dots,\mathbf{v}_r$, el espacio columna de $\mathbf{A}^{\top}$; este es el complemento ortogonal del núcleo.

(b) Cada columna de $\mathbf{A}$ está en el espacio columna, y la proyección sobre él la deja fija: $\mathbf{A}\mathbf{A}^+\mathbf{A}=(\mathbf{U}_r\mathbf{U}_r^{\top})\mathbf{A}=\mathbf{A}$. Del mismo modo, cada columna de $\mathbf{A}^+=\sum_{j\le r}\tfrac1{d_j}\mathbf{v}_j\mathbf{u}_j^{\top}$ está en el espacio generado por $\mathbf{v}_1,\dots,\mathbf{v}_r$; por tanto, $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=(\mathbf{V}_r\mathbf{V}_r^{\top})\mathbf{A}^+=\mathbf{A}^+$.
:::
:::
