---
title: Matrices definidas positivas
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15220900
summary: Una forma cuadrática es un cuenco si es positiva en todas partes salvo en el origen.
tags: definida positiva, semidefinida positiva, indefinida, cociente de Rayleigh
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Una forma cuadrática es un cuenco si es positiva en todas partes salvo en el origen. Esta sección da un nombre a esta propiedad y presenta criterios con los que se comprueba: mediante los valores propios, mediante los pivotes y mediante determinantes. A ello se suman dos consecuencias: el valor máximo y el mínimo de una forma sobre la circunferencia unidad, y una descomposición que solo tienen los cuencos.
:::

### Definida positiva y semidefinida positiva

<span class="anker" id="stufe-8-1"></span>

El cuenco y el canal de la sección [5.3](quadratische-formen.html#stufe-5-3) se diferencian en un punto: el cuenco es positivo en todas partes fuera del origen; el canal, solo no negativo. Para estas dos propiedades hay nombres fijos.

:::definition Definición 8.1 (Definida positiva, semidefinida positiva)
<span class="anker" id="satz-8-1"></span>

Una matriz simétrica $\mathbf{A}\in\mathbb{R}^{n\times n}$ se llama __definida positiva__ si

<span class="anker" id="gl-8-1"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}>0\qquad\text{para todo}\ \mathbf{x}\ne\mathbf{0} , \tag{8.1}$$

y __semidefinida positiva__ si $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}\ge0$ para todo $\mathbf{x}$.
:::

La simetría forma parte de la definición. Para la forma cuadrática no supone ninguna restricción: según la sección [5.2](quadratische-formen.html#stufe-5-2), de todos modos solo cuenta la parte simétrica. Pero es necesaria para que valgan los criterios de la subsección siguiente. Toda matriz definida positiva es también semidefinida positiva.

::::beispiel [Ejemplo numérico]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ es definida positiva, pues según la sección [5.4](quadratische-formen.html#stufe-5-4) es $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=5(x_1+0{,}4x_2)^2+1{,}2x_2^2$, y esto solo es cero si $x_2=0$ y entonces también $x_1=0$. La matriz $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ tiene la forma $x_1^2+4x_1x_2+4x_2^2=(x_1+2x_2)^2\ge0$; es semidefinida positiva, pero no definida positiva, pues para $\mathbf{x}=(2,\,-1)^{\top}$ la forma es cero. Su gráfica es un canal con el fondo del valle en la dirección de $(2,\,-1)^{\top}$.
::::

⁠**En resumen:** Definida positiva significa que la forma cuadrática es positiva fuera del origen: un cuenco; semidefinida positiva significa que no es negativa en ningún punto.

### El criterio de los valores propios

<span class="anker" id="stufe-8-2"></span>

La forma de ejes principales [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) responde a la pregunta de inmediato: una suma $\sum_i\lambda_ic_i^2$ es positiva para toda elección de las coordenadas si todos los $\lambda_i$ son positivos, y si no, no.

:::satz Teorema 8.2 (Criterio de los valores propios)
<span class="anker" id="satz-8-2"></span>

Una matriz simétrica es definida positiva si y solo si todos sus valores propios son positivos, y semidefinida positiva si y solo si ninguno es negativo.
:::

:::beweis Criterio de los valores propios
Si todos los $\lambda_i>0$ y $\mathbf{x}\ne\mathbf{0}$, también $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}\ne\mathbf{0}$, pues $\mathbf{Q}$ es invertible; según [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4), entonces $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2>0$. Si, a la inversa, un valor propio es $\lambda_i\le0$, para el vector propio $\mathbf{x}=\mathbf{q}_i$ la forma vale $\mathbf{q}_i^{\top}\mathbf{A}\mathbf{q}_i=\lambda_i\le0$, y $\mathbf{A}$ no es definida positiva. Para semidefinida se procede igual, con $\ge$ en lugar de $>$.
:::

Si una matriz simétrica tiene valores propios positivos y negativos, su forma es positiva en unas direcciones y negativa en otras: una silla. Una matriz así se llama __indefinida__. Análogamente, una matriz cuyos valores propios son todos negativos se llama definida negativa; su forma es una cúpula.

::::beispiel [Ejemplo numérico]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ tiene los valores propios $6$ y $1$: definida positiva. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ tiene los valores propios $5$ y $0$: semidefinida positiva. $\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ tiene todas sus entradas positivas, pero los valores propios $4$ y $-2$: indefinida, pues para $\mathbf{x}=(1,\,-1)^{\top}$ la forma vale $1-6+1=-4$. Las entradas positivas no dicen, por tanto, nada sobre el carácter definido.
::::

⁠**En resumen:** Una matriz simétrica es definida positiva si y solo si todos sus valores propios son positivos; valores propios positivos y negativos a la vez dan una silla.

:::hintergrund Por qué la simetría forma parte de la definición
Algunos libros definen «definida positiva» mediante la forma cuadrática; otros, mediante los valores propios. Para matrices simétricas es lo mismo, según el teorema; para las no simétricas, no. La matriz $\bigl(\begin{smallmatrix}2&-5\\0&2\end{smallmatrix}\bigr)$ tiene, como matriz triangular, los valores propios $2$ y $2$, ambos positivos. Pero su forma cuadrática es $2x_1^2-5x_1x_2+2x_2^2$, y para $\mathbf{x}=(1,\,1)^{\top}$ vale $2-5+2=-1$. La razón: la forma solo ve la parte simétrica $\bigl(\begin{smallmatrix}2&-2{,}5\\-2{,}5&2\end{smallmatrix}\bigr)$, con los valores propios $4{,}5$ y $-0{,}5$, mientras que los valores propios pertenecen a la matriz completa. Quien usa el término sin simetría debe indicar, por tanto, siempre a qué definición se refiere.
:::

### Criterios sin valores propios

<span class="anker" id="stufe-8-3"></span>

En matrices grandes, calcular valores propios es costoso. Completar cuadrados, como en la sección [5.4](quadratische-formen.html#stufe-5-4), da un criterio sin valores propios, y de él se deduce un segundo con determinantes.

:::satz Teorema 8.3 (Criterios para ser definida positiva)
<span class="anker" id="satz-8-3"></span>

Para una matriz simétrica $\mathbf{A}\in\mathbb{R}^{n\times n}$ son equivalentes:

<ol class="rm">

<li>

$\mathbf{A}$ es definida positiva;

</li>

<li>

la eliminación gaussiana sin intercambios de filas da $n$ pivotes positivos;

</li>

<li>

todos los menores principales dominantes son positivos: los determinantes de las submatrices $k\times k$ superiores izquierdas son mayores que cero para $k=1,\dots,n$.

</li>

</ol>

Para $n=2$ y $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$, esto significa: $a>0$ y $ac-b^2>0$.
:::

Para $n=2$, esto es [(5.3)](quadratische-formen.html#gl-5-3): los pivotes son $a$ y $c-b^2/a$; la forma es un cuenco si y solo si ambos son positivos, y, si $a>0$, $c-b^2/a>0$ equivale a $ac-b^2>0$. Para $n$ mayor, cada paso de eliminación completa el cuadrado de una variable, como en el recuadro de contexto de la sección [5.4](quadratische-formen.html#stufe-5-4). El determinante de la submatriz $k\times k$ superior izquierda es el producto de los $k$ primeros pivotes; por eso, los pivotes son todos positivos si y solo si lo son los menores principales dominantes. El criterio de los determinantes se llama también criterio de Sylvester.

Dos advertencias. Primera: $\det\mathbf{A}>0$ por sí solo no basta: $\operatorname{diag}(-1;\,-3)$ tiene el determinante $3$, pero es definida negativa. Segunda: el criterio no se traslada sin más al caso semidefinido: $\operatorname{diag}(0;\,-1)$ tiene los menores principales dominantes $0$ y $0$, ambos no negativos, y aun así no es semidefinida positiva.

::::beispiel [Ejemplo numérico]
Para

$$\mathbf{A}=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$$

los menores principales dominantes son $2$, $\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ y $\det\mathbf{A}=2\cdot3-1\cdot2=4$, todos positivos: $\mathbf{A}$ es definida positiva. Los pivotes son $2$, $\tfrac32$ y $\tfrac43$, los cocientes de menores consecutivos. Como control: los valores propios son $2-\sqrt2$, $2$ y $2+\sqrt2$, todos positivos, y su producto es $(4-2)\cdot2=4$.
::::

⁠**En resumen:** Una matriz simétrica es definida positiva si y solo si todos los pivotes o todos los menores principales dominantes son positivos; en el caso $2\times2$, esto significa $a>0$ y $ac-b^2>0$.

### Las matrices de Gram son semidefinidas positivas

<span class="anker" id="stufe-8-4"></span>

En [Fundamentos 1, sección 10](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10), aparecieron las matrices de Gram $\mathbf{X}^{\top}\mathbf{X}$ y $\mathbf{X}\mathbf{X}^{\top}$, y en este capítulo, $\mathbf{A}^{\top}\mathbf{A}$ en las ecuaciones normales. Siempre son semidefinidas positivas, y la razón es sencilla: su forma cuadrática es el cuadrado de una longitud.

:::satz Teorema 8.4 (Matrices de Gram)
<span class="anker" id="satz-8-4"></span>

Para toda matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$, $\mathbf{A}^{\top}\mathbf{A}$ es semidefinida positiva. Es definida positiva si y solo si las columnas de $\mathbf{A}$ son linealmente independientes.
:::

:::beweis Matrices de Gram
$\mathbf{A}^{\top}\mathbf{A}$ es simétrica, y $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}\mathbf{x})^{\top}(\mathbf{A}\mathbf{x})=\lVert\mathbf{A}\mathbf{x}\rVert^2\ge0$. Esto es igual a cero si y solo si $\mathbf{A}\mathbf{x}=\mathbf{0}$. Con columnas independientes, esto solo ocurre para $\mathbf{x}=\mathbf{0}$.
:::

Lo mismo vale para $\mathbf{A}\mathbf{A}^{\top}$, con las filas en lugar de las columnas. El teorema explica a posteriori la sección [3.5](die-beste-naherungslosung.html#stufe-3-5): con columnas independientes, $\mathbf{A}^{\top}\mathbf{A}$ es definida positiva; tiene, por tanto, todos sus valores propios positivos y es invertible.

::::beispiel [Ejemplo numérico]
$\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ tiene los valores propios $3$ y $1$: definida positiva, en consonancia con las columnas independientes de $\mathbf{H}$. Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ es $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$, con el determinante $0$ y los valores propios $25$ y $0$: semidefinida positiva, no definida positiva.
::::

⁠**En resumen:** $\mathbf{A}^{\top}\mathbf{A}$ es siempre semidefinida positiva, porque $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf{A}\mathbf{x}\rVert^2$; con columnas independientes, es definida positiva.

### Valor máximo y mínimo sobre la circunferencia unidad

<span class="anker" id="stufe-8-5"></span>

Una forma cuadrática crece con el cuadrado de la longitud de $\mathbf{x}$. Cuánto crece en las distintas direcciones se ve si solo se introducen vectores de longitud $1$. ¿En qué dirección es máxima?

:::satz Teorema 8.5 (Valores extremos de una forma cuadrática)
<span class="anker" id="satz-8-5"></span>

Sea $\mathbf{A}$ simétrica, con el valor propio mínimo $\lambda_{\min}$ y el valor propio máximo $\lambda_{\max}$. Para todo vector $\mathbf{x}\ne\mathbf{0}$ se cumple

<span class="anker" id="gl-8-2"></span>
$$\lambda_{\min}\le\frac{\mathbf{x}^{\top}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}}\le\lambda_{\max} . \tag{8.2}$$

El valor máximo se alcanza en un vector propio asociado a $\lambda_{\max}$, y el mínimo, en un vector propio asociado a $\lambda_{\min}$.
:::

:::beweis Valores extremos
Con $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ es $\mathbf{x}^{\top}\mathbf{x}=\mathbf{c}^{\top}\mathbf{c}=\sum_ic_i^2$, porque $\mathbf{Q}$ conserva las longitudes, y $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2$. El cociente es, por tanto,

$$\frac{\sum_i\lambda_ic_i^2}{\sum_ic_i^2}=\sum_i\lambda_i\,g_i\qquad\text{con}\qquad g_i=\frac{c_i^2}{\sum_lc_l^2}\ge0,\quad \sum_ig_i=1 .$$

Es una media ponderada de los valores propios, y una media está siempre entre el menor y el mayor de los valores promediados. Para $\mathbf{x}=\mathbf{q}_i$, todos los pesos son nulos salvo $g_i=1$, y el cociente es $\lambda_i$.
:::

El cociente de [(8.2)](#gl-8-2) se llama __cociente de Rayleigh__. Para $\lVert\mathbf{x}\rVert=1$, es la propia forma cuadrática: sobre la circunferencia unidad, la forma está entre el valor propio mínimo y el máximo.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, el cociente de Rayleigh vale $5$ en $\mathbf{e}_1$; $2$ en $\mathbf{e}_2$; $\tfrac{5+4+2}2=5{,}5$ en $(1,\,1)^{\top}/\sqrt2$, y $\tfrac{5-4+2}2=1{,}5$ en $(1,\,-1)^{\top}/\sqrt2$. Todos los valores están entre $1$ y $6$. El valor $6$ lo alcanza en $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$: $\tfrac15(20+8+2)=6$. El cociente no depende de la longitud de $\mathbf{x}$; la fig. [21](#abb-21) lo calcula para $\mathbf{x}=(1,\,1)^{\top}$ sin raíces.

:::abbildung ml/k2rrayleigh 21
El cociente de Rayleigh de $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ en el punto $\mathbf{x}=(1,1)^{\top}$: numerador y denominador como sumas; el cociente $\tfrac{11}2=5{,}5$ está entre los valores propios $1$ y $6$.
:::
::::

⁠**En resumen:** Sobre la circunferencia unidad, una forma cuadrática está entre el valor propio mínimo y el máximo, y estos valores extremos se alcanzan en las direcciones propias.

### La descomposición de Cholesky

<span class="anker" id="stufe-8-6"></span>

Completar cuadrados escribe una forma definida positiva como suma de cuadrados. Si se reúnen las expresiones de dentro de los cuadrados en un vector, la forma es el cuadrado de la longitud de ese vector. De ahí sale una descomposición de la matriz.

:::satz Teorema 8.6 (Descomposición de Cholesky)
<span class="anker" id="satz-8-6"></span>

Una matriz simétrica $\mathbf{A}$ es definida positiva si y solo si existe una matriz triangular inferior $\mathbf L$ con entradas diagonales positivas tal que

<span class="anker" id="gl-8-3"></span>
$$\mathbf{A}=\mathbf L\mathbf L^{\top} . \tag{8.3}$$

Esta matriz $\mathbf L$ es única y se llama factor de Cholesky de $\mathbf{A}$.
:::

Si $\mathbf{A}=\mathbf L\mathbf L^{\top}$, entonces $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf L^{\top}\mathbf{x}\rVert^2$, una suma de cuadrados, y como $\mathbf L$ es invertible, solo es cero para $\mathbf{x}=\mathbf{0}$. Esa es una de las implicaciones. La otra, que toda matriz definida positiva tiene un factor así, es completar cuadrados: para $n=2$ se lee en [(5.3)](quadratische-formen.html#gl-5-3),

$$\mathbf L=\begin{pmatrix}\sqrt a&0\\b/\sqrt a&\sqrt{c-b^2/a}\end{pmatrix},$$

y para $n$ mayor se sigue completando cuadrados variable por variable. Según [Fundamentos 1, sección 14.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), es $\det\mathbf{A}=\det\mathbf L\cdot\det\mathbf L^{\top}=(l_{11}\cdots l_{nn})^2$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$ es $a=4$, $b=2$, $c=5$; por tanto, $l_{11}=2$, $l_{21}=1$ y $l_{22}=\sqrt{5-1}=2$:

$$\mathbf L=\begin{pmatrix}2&0\\1&2\end{pmatrix},\qquad \mathbf L\mathbf L^{\top}=\begin{pmatrix}4&2\\2&1+4\end{pmatrix}=\mathbf{A} .$$

La forma es $4x_1^2+4x_1x_2+5x_2^2=(2x_1+x_2)^2+(2x_2)^2$; las dos expresiones de dentro de los cuadrados son las componentes de $\mathbf L^{\top}\mathbf{x}$. El determinante es $20-4=16=(2\cdot2)^2$.
::::

⁠**En resumen:** Toda matriz definida positiva es $\mathbf L\mathbf L^{\top}$ con una matriz triangular inferior $\mathbf L$; la descomposición es completar cuadrados en forma matricial.

:::aufgabe Ejercicio 24 ★ Comprobar el carácter definido
<span class="anker" id="aufg-24"></span>

Decide con dos criterios distintos si las matrices son definidas positivas, semidefinidas positivas, definidas negativas o indefinidas:

$$\mathbf{A}_1=\begin{pmatrix}3&1\\1&2\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}2&6\\6&18\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&2\end{pmatrix},\qquad \mathbf{A}_4=\begin{pmatrix}-2&1\\1&-1\end{pmatrix}.$$

:::loesung
<ul>

<li>

$\mathbf{A}_1$: $a=3>0$ y $ac-b^2=6-1=5>0$: definida positiva. Valores propios: traza $5$, determinante $5$, $\lambda=\tfrac{5\pm\sqrt5}2\approx3{,}62$ y $1{,}38$, ambos positivos.

</li>

<li>

$\mathbf{A}_2$: $a=2>0$, pero $ac-b^2=36-36=0$. Valores propios $20$ y $0$: semidefinida positiva, no definida. Completando cuadrados: $2(x_1+3x_2)^2$, un canal.

</li>

<li>

$\mathbf{A}_3$: $ac-b^2=2-9=-7<0$; los valores propios tienen el producto $-7$ y, por tanto, signos distintos: indefinida. Son $\tfrac{3\pm\sqrt{37}}2\approx4{,}54$ y $-1{,}54$.

</li>

<li>

$\mathbf{A}_4$: $a=-2<0$, no es definida positiva. Para $-\mathbf{A}_4=\bigl(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\bigr)$ es $a=2>0$ y $ac-b^2=1>0$; por tanto, $-\mathbf{A}_4$ es definida positiva y $\mathbf{A}_4$, definida negativa. Valores propios de $\mathbf{A}_4$: traza $-3$, determinante $1$, $\lambda=\tfrac{-3\pm\sqrt5}2\approx-0{,}38$ y $-2{,}62$, ambos negativos: una cúpula.

</li>

</ul>
:::
:::

:::aufgabe Ejercicio 25 ★★ Una trampa
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

La matriz $\bigl(\begin{smallmatrix}1&-4\\0&1\end{smallmatrix}\bigr)$ solo tiene valores propios positivos. ¿Es positiva su forma cuadrática? Encuentra un vector que muestre lo contrario y explica la contradicción.

</li>

<li>

¿Para qué números $t$ es $\bigl(\begin{smallmatrix}1&t\\t&4\end{smallmatrix}\bigr)$ definida positiva? ¿Para cuáles es semidefinida positiva?

</li>

</ol>

:::loesung
(a) Los valores propios son $1$ y $1$, pero la forma $x_1^2-4x_1x_2+x_2^2$ toma en $\mathbf{x}=(1,\,1)^{\top}$ el valor $1-4+1=-2<0$. No hay contradicción: el criterio de los valores propios solo vale para matrices simétricas. La forma solo ve la parte simétrica $\bigl(\begin{smallmatrix}1&-2\\-2&1\end{smallmatrix}\bigr)$, y esta tiene los valores propios $3$ y $-1$; la forma es indefinida.

(b) Con el criterio $2\times2$: $a=1>0$, y $ac-b^2=4-t^2>0$ exactamente para $|t|<2$. Para que sea semidefinida positiva hacen falta valores propios $\ge0$. Su suma es la traza $5>0$, y su producto, el determinante $4-t^2$; ambos valores propios son $\ge0$ si y solo si $4-t^2\ge0$, es decir, para $|t|\le2$. Para $t=\pm2$, la matriz es semidefinida positiva, pero no definida, con los valores propios $5$ y $0$; para $|t|>2$ es indefinida.
:::
:::

:::aufgabe Ejercicio 26 ★★ Cociente de Rayleigh y Cholesky
<span class="anker" id="aufg-26"></span>

Sea $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Calcula los valores propios y el cociente de Rayleigh en los puntos $\mathbf{e}_1$, $\mathbf{e}_2$ y $(1,\,1)^{\top}$. Comprueba [(8.2)](#gl-8-2).

</li>

<li>

Resuelve $\mathbf{A}\mathbf{x}=(2,\,9)^{\top}$ con el factor de Cholesky: primero $\mathbf L\mathbf{z}=(2,\,9)^{\top}$ de arriba abajo, después $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ de abajo arriba.

</li>

</ol>

:::loesung
(a) Traza $9$, determinante $16$: $\lambda=\tfrac{9\pm\sqrt{81-64}}2=\tfrac{9\pm\sqrt{17}}2\approx6{,}56$ y $2{,}44$. El cociente de Rayleigh vale $4$ en $\mathbf{e}_1$, $5$ en $\mathbf{e}_2$ y $\tfrac{4+2+2+5}2=\tfrac{13}2=6{,}5$ en $(1,\,1)^{\top}$. Los tres están entre $2{,}44$ y $6{,}56$; el tercero está cerca del máximo, porque $(1,\,1)^{\top}$ apunta casi en la dirección del vector propio asociado al valor propio mayor.

(b) De la sección [8.6](#stufe-8-6): $\mathbf L=\bigl(\begin{smallmatrix}2&0\\1&2\end{smallmatrix}\bigr)$. De arriba abajo: $2z_1=2$, luego $z_1=1$; $z_1+2z_2=9$, luego $z_2=4$. Después, $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ de abajo arriba: $2x_2=4$, luego $x_2=2$; $2x_1+x_2=1$, luego $x_1=-\tfrac12$. Comprobación: $\mathbf{A}(-\tfrac12,\,2)^{\top}=(-2+4,\ -1+10)^{\top}=(2,\,9)^{\top}$. Dos sistemas triangulares sustituyen a un sistema de ecuaciones general.
:::
:::
