---
title: La matriz jacobiana
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230600
summary: Muchos pasos de cálculo no dan un número, sino varios: un producto matriz-vector convierte un vector en otro.
tags: vectorial, matriz jacobiana
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Muchos pasos de cálculo no dan un número, sino varios: un producto matriz-vector convierte un vector en otro. Para tales funciones, la matriz jacobiana reúne las derivadas parciales de todas las salidas respecto de todas las entradas. Es la matriz de la aproximación lineal, y para los dos bloques más frecuentes, las aplicaciones lineales y las funciones elemento a elemento, tiene una forma especialmente sencilla.
:::

### Funciones con varias salidas

<span class="anker" id="stufe-5-1"></span>

En el [capítulo 1, sección 8](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8), una aplicación lineal $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ llevaba vectores de $\mathbb{R}^n$ a vectores de $\mathbb{R}^m$, y en el [capítulo 1, sección 15.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/elementweise-rechnen-und-tensoren.html#stufe-15-2), se aplicaba una función a cada componente de un vector por separado. En ambos casos, de un vector salen varios números. Cada uno de ellos es, por sí solo, una función de varias variables.

:::definition Definición 5.1 (Función vectorial)
<span class="anker" id="satz-5-1"></span>

Una función $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ que asigna a cada $\mathbf{x}\in\mathbb{R}^n$ un vector

$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}g_1(\mathbf{x})\\ \vdots\\ g_m(\mathbf{x})\end{pmatrix}\in\mathbb{R}^m$$

se llama __vectorial__. Las funciones $g_1,\dots,g_m:\mathbb{R}^n\to\mathbb{R}$ se llaman sus componentes.
:::

Este capítulo escribe las funciones vectoriales en negrita, como los vectores; las funciones cuyo valor es un número, en letra normal.

::::beispiel [Ejemplo numérico]
A lo largo de las secciones [5](#stufe-5) y [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6) nos acompaña la función $\mathbf{g}:\mathbb{R}^2\to\mathbb{R}^2$ con

<span class="anker" id="gl-5-1"></span>
$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}x_1x_2\\ 2x_1+x_2^2\end{pmatrix},\qquad \mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix}. \tag{5.1}$$

Sus componentes son $g_1(\mathbf{x})=x_1x_2$ y $g_2(\mathbf{x})=2x_1+x_2^2$.
::::

⁠**En resumen:** Una función vectorial $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ consta de $m$ funciones de $n$ variables, una por cada salida.

### La matriz jacobiana

<span class="anker" id="stufe-5-2"></span>

Cada componente $g_i$ tiene $n$ derivadas parciales, una respecto de cada entrada. En total son $m\cdot n$ números. Se disponen en una tabla con una fila por salida y una columna por entrada.

:::definition Definición 5.2 (Matriz jacobiana)
<span class="anker" id="satz-5-2"></span>

Si en el punto $\mathbf{x}$ existen todas las derivadas parciales de las componentes de $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$, la matriz $m\times n$

<span class="anker" id="gl-5-2"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{pmatrix},\qquad \bigl(\mathbf{J}_{\mathbf{g}}(\mathbf{x})\bigr)_{ij}=\frac{\partial g_i}{\partial x_j}(\mathbf{x}), \tag{5.2}$$

se llama __matriz jacobiana__ de $\mathbf{g}$ en el punto $\mathbf{x}$.
:::

La fila $i$ corresponde a la salida $g_i$; es su gradiente, escrito como fila: $\nabla g_i(\mathbf{x})^{\top}$. La columna $j$ corresponde a la entrada $x_j$; dice cómo reaccionan todas las salidas a la vez cuando solo se modifica $x_j$. Para una función $f:\mathbb{R}^n\to\mathbb{R}$ con una única salida, la matriz jacobiana es una matriz $1\times n$, a saber, el gradiente como fila: $\mathbf{J}_f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}$. La matriz lleva el nombre del matemático Carl Gustav Jacob Jacobi.

::::beispiel [Ejemplo numérico]
Para $\mathbf{g}$ de [(5.1)](#gl-5-1) se tiene

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}x_2&x_1\\2&2x_2\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}.$$

La primera columna $(2,\,2)^{\top}$ dice: si $x_1$ crece en un $h$ pequeño, ambas salidas crecen aproximadamente $2h$. La segunda columna $(1,\,4)^{\top}$ dice: si crece $x_2$, la segunda salida reacciona con una intensidad cuatro veces mayor que la primera.
::::

⁠**En resumen:** La matriz jacobiana tiene una fila por salida y una columna por entrada; su entrada $(i,j)$ es $\partial g_i/\partial x_j$.

### La aproximación lineal con la matriz jacobiana

<span class="anker" id="stufe-5-3"></span>

Cada componente tiene su aproximación lineal [(3.4)](partielle-ableitungen-und-der-gradient.html#gl-3-4). Si se escriben las $m$ aproximaciones una debajo de otra, a la izquierda están las componentes de $\mathbf{g}(\mathbf{x}+\mathbf{h})$, y a la derecha, las filas de la matriz jacobiana por $\mathbf{h}$. Según la visión por filas del [capítulo 1, sección 7.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2), eso es un producto matriz-vector.

:::satz Teorema 5.3 (Aproximación lineal de una función vectorial)
<span class="anker" id="satz-5-3"></span>

Si cada componente de $\mathbf{g}$ es diferenciable en el punto $\mathbf{x}$, se cumple

<span class="anker" id="gl-5-3"></span>
$$\mathbf{g}(\mathbf{x}+\mathbf{h})=\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}+\mathbf{r}(\mathbf{h})\qquad\text{con}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{\lVert\mathbf{r}(\mathbf{h})\rVert}{\lVert\mathbf{h}\rVert}=0 . \tag{5.3}$$
:::

:::beweis Aproximación lineal de una función vectorial
La componente $i$ de $\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ es $\nabla g_i(\mathbf{x})^{\top}\mathbf{h}$. Según la definición de diferenciabilidad [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5), para cada $i$ el cociente $r_i(\mathbf{h})/\lVert\mathbf{h}\rVert$ tiende a $0$. Como $\lVert\mathbf{r}\rVert\le|r_1|+\dots+|r_m|$, también $\lVert\mathbf{r}(\mathbf{h})\rVert/\lVert\mathbf{h}\rVert$ tiende a $0$.
:::

Cerca de $\mathbf{x}$, $\mathbf{g}$ actúa, pues, como la aplicación lineal $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$, y según el [capítulo 1, sección 8.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2), a cada aplicación lineal le corresponde exactamente una matriz. La matriz jacobiana es esa matriz. Bajo la lupa, $\mathbf{g}$ deforma una pequeña cuadrícula alrededor de $\mathbf{x}$ del mismo modo que la matriz $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ deforma la cuadrícula unidad: se gira, se estira o se cizalla, pero las líneas rectas siguen siendo casi rectas.

::::beispiel [Ejemplo numérico]
Para $\mathbf{g}$ de [(5.1)](#gl-5-1) en el punto $(1,\,2)$ y $\mathbf{h}=(0{,}1;\ -0{,}1)^{\top}$ se tiene

$$\mathbf{J}_{\mathbf{g}}(1,2)\,\mathbf{h}=\begin{pmatrix}2\cdot0{,}1+1\cdot(-0{,}1)\\2\cdot0{,}1+4\cdot(-0{,}1)\end{pmatrix}=\begin{pmatrix}0{,}1\\-0{,}2\end{pmatrix}, \qquad \mathbf{g}(1{,}1;\ 1{,}9)\approx\begin{pmatrix}2{,}1\\5{,}8\end{pmatrix}.$$

El valor exacto es $\mathbf{g}(1{,}1;\ 1{,}9)=(2{,}09;\ 5{,}81)^{\top}$. La fig. [10](#abb-10) muestra el producto fila por fila.

:::abbildung ml/k3rjacobi 10
La variación de la aproximación lineal de $\mathbf{g}$ en el punto $\mathbf{x}=(1,\,2)^{\top}$ como producto matriz-vector: cada fila es el producto escalar del gradiente de una salida y el desplazamiento.
:::
::::

⁠**En resumen:** Cerca de $\mathbf{x}$, $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$; la matriz jacobiana es la matriz de la aplicación lineal a la que $\mathbf{g}$ equivale a pequeña escala.

### Dos matrices jacobianas importantes

<span class="anker" id="stufe-5-4"></span>

Dos bloques aparecen constantemente en los cálculos con datos: el producto matriz-vector y las funciones que se aplican a cada componente por separado. Sus matrices jacobianas se necesitan una y otra vez, y ambas pueden darse sin cálculo.

:::satz Teorema 5.4 (Matrices jacobianas de los bloques)
<span class="anker" id="satz-5-4"></span>

<ol class="al">

<li>

Para $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ con $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{b}\in\mathbb{R}^m$, se tiene $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\mathbf{A}$ en todos los puntos.

</li>

<li>

Si $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^n$ aplica una función derivable $\varphi$ de una variable a cada componente, $g_i(\mathbf{x})=\varphi(x_i)$, entonces

<span class="anker" id="gl-5-4"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\operatorname{diag}\bigl(\varphi'(x_1),\,\dots,\,\varphi'(x_n)\bigr). \tag{5.4}$$

</li>

</ol>
:::

:::beweis Matrices jacobianas de los bloques
(a) La componente $i$ es $g_i(\mathbf{x})=\sum_ka_{ik}x_k+b_i$. Al derivar respecto de $x_j$ solo queda el sumando con $k=j$, es decir, $\partial g_i/\partial x_j=a_{ij}$. (b) La componente $g_i=\varphi(x_i)$ solo depende de $x_i$. Por eso, su derivada respecto de $x_j$ es $0$ para $j\ne i$ y $\varphi'(x_i)$ para $j=i$.
:::

Ambos resultados tienen una razón sencilla. Una aplicación afín ya es lineal salvo por el desplazamiento $\mathbf{b}$; su mejor aproximación lineal es ella misma sin $\mathbf{b}$. En una función elemento a elemento, cada entrada actúa solo sobre su propia salida; todas las entradas de la matriz fuera de la diagonal son nulas, porque no hay conexiones entre componentes distintas.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\bigr)$, la matriz jacobiana de $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ es en todas partes la propia $\mathbf{A}$. Si se eleva al cuadrado cada componente, $\varphi(t)=t^2$, en el punto $\mathbf{x}=(1,\,-2,\,3)^{\top}$ la matriz jacobiana es $\operatorname{diag}(2;\,-4;\,6)$. Si se aplica la función logística a cada componente de $\mathbf{x}=(0,\,2)^{\top}$, según [(2.4)](die-kettenregel.html#gl-2-4) es $\operatorname{diag}\bigl(\sigma'(0);\,\sigma'(2)\bigr)\approx\operatorname{diag}(0{,}25;\ 0{,}105)$.
::::

⁠**En resumen:** La matriz jacobiana de $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}+\mathbf{b}$ es $\mathbf{A}$; la de una función elemento a elemento es la matriz diagonal de las derivadas individuales.

:::hintergrund El determinante de la matriz jacobiana como factor de área
Según el [capítulo 1, sección 14.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-3), una aplicación lineal multiplica el área de toda figura por el mismo factor $|\det\mathbf{A}|$. Como $\mathbf{g}$ actúa a pequeña escala como $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$, esto vale aproximadamente también para $\mathbf{g}$: un cuadrado pequeño alrededor de $\mathbf{x}$ con área $F$ se transforma en una figura que es casi un paralelogramo de área $|\det\mathbf{J}_{\mathbf{g}}(\mathbf{x})|\cdot F$. Para $\mathbf{g}$ de [(5.1)](#gl-5-1), $\det\mathbf{J}_{\mathbf{g}}(1,2)=2\cdot4-1\cdot2=6$: cerca de $(1,\,2)$, $\mathbf{g}$ multiplica las áreas aproximadamente por seis. Un ejemplo conocido son las coordenadas polares, $\mathbf{g}(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)^{\top}$. Su matriz jacobiana tiene las columnas $(\cos\varphi,\,\sin\varphi)^{\top}$ y $(-r\sin\varphi,\,r\cos\varphi)^{\top}$ y el determinante $r\cos^2\varphi+r\sin^2\varphi=r$. Un rectángulo pequeño de lados $\Delta r$ y $\Delta\varphi$ se convierte en un trozo de corona circular con un área de aproximadamente $r\,\Delta r\,\Delta\varphi$, porque el arco correspondiente al ángulo $\Delta\varphi$ a la distancia $r$ tiene la longitud $r\,\Delta\varphi$.
:::

:::aufgabe Ejercicio 17 ★ Calcular matrices jacobianas
<span class="anker" id="aufg-17"></span>

Calcula la matriz jacobiana en el punto indicado.

<ol class="al">

<li>

$\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1-x_2,\ x_1x_2)^{\top}$ en el punto $(3,\,1)$;

</li>

<li>

$\mathbf{g}(\mathbf{x})=(\mathrm{e}^{x_1},\,\mathrm{e}^{x_2},\,\mathrm{e}^{x_3})^{\top}$ en el punto $(0,\,1,\,-1)$;

</li>

<li>

$f(\mathbf{x})=x_1^2x_2+x_2^2$ de [(3.1)](partielle-ableitungen-und-der-gradient.html#gl-3-1) en el punto $(1,\,2)$. ¿Qué forma tiene la matriz y qué es?

</li>

</ol>

:::loesung
(a) La matriz jacobiana tiene tres filas y dos columnas:

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}1&1\\1&-1\\x_2&x_1\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(3,1)=\begin{pmatrix}1&1\\1&-1\\1&3\end{pmatrix}.$$

(b) La función actúa elemento a elemento; por [(5.4)](#gl-5-4), $\mathbf{J}=\operatorname{diag}(\mathrm{e}^0;\,\mathrm{e}^1;\,\mathrm{e}^{-1})\approx\operatorname{diag}(1;\ 2{,}718;\ 0{,}368)$.

(c) Una función con una salida tiene una matriz jacobiana $1\times2$, el gradiente como fila: $\mathbf{J}_f(1,2)=(4\ \ 5)=\nabla f(1,2)^{\top}$.
:::
:::

:::aufgabe Ejercicio 18 ★★ Aproximación lineal de una aplicación del plano
<span class="anker" id="aufg-18"></span>

Sea $\mathbf{g}(\mathbf{x})=(x_1^2-x_2,\ x_1x_2)^{\top}$.

<ol class="al">

<li>

Calcula $\mathbf{J}_{\mathbf{g}}(2,1)$ y, con ella, un valor aproximado de $\mathbf{g}(2{,}05;\ 0{,}9)$. Compáralo con el valor exacto.

</li>

<li>

¿Cómo hay que desplazar las entradas para que cambie la primera salida, pero la segunda, en aproximación lineal, no cambie en absoluto? Da un desplazamiento $\mathbf{h}$ así.

</li>

</ol>

:::loesung
(a) $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}2x_1&-1\\x_2&x_1\end{smallmatrix}\bigr)$, así que $\mathbf{J}_{\mathbf{g}}(2,1)=\bigl(\begin{smallmatrix}4&-1\\1&2\end{smallmatrix}\bigr)$, y $\mathbf{g}(2,1)=(3,\,2)^{\top}$. Con $\mathbf{h}=(0{,}05;\ -0{,}1)^{\top}$ se tiene

$$\mathbf{J}_{\mathbf{g}}\mathbf{h}=\begin{pmatrix}0{,}2+0{,}1\\0{,}05-0{,}2\end{pmatrix}=\begin{pmatrix}0{,}3\\-0{,}15\end{pmatrix},\qquad \mathbf{g}(2{,}05;\ 0{,}9)\approx\begin{pmatrix}3{,}3\\1{,}85\end{pmatrix}.$$

El valor exacto es $\mathbf{g}(2{,}05;\ 0{,}9)=(4{,}2025-0{,}9;\ 1{,}845)^{\top}=(3{,}3025;\ 1{,}845)^{\top}$.

(b) La segunda salida cambia, en aproximación lineal, en $h_1+2h_2$; esto es cero para $\mathbf{h}$ en la dirección $(2,\,-1)^{\top}$. Si el paso es exactamente este vector, la primera salida cambia entonces en $4\cdot2-1\cdot(-1)=9$. Por tanto, tienen que cambiar ambas entradas: $x_1$ crece y $x_2$ disminuye en la mitad de esa cantidad, por ejemplo $\mathbf{h}=(0{,}02;\ -0{,}01)^{\top}$, con el efecto $(0{,}09;\ 0)^{\top}$.
:::
:::

:::aufgabe Ejercicio 19 ★★★ Cuánto aumenta $\mathbf{g}$ las áreas
<span class="anker" id="aufg-19"></span>

Sea $\mathbf{g}$ como en [(5.1)](#gl-5-1).

<ol class="al">

<li>

Calcula las imágenes de los cuatro vértices del cuadrado con vértices $(1,\,2)$, $(1{,}1;\ 2)$, $(1{,}1;\ 2{,}1)$ y $(1;\ 2{,}1)$.

</li>

<li>

Las imágenes forman casi un paralelogramo. Estima su área con las imágenes de los dos lados que parten de $\mathbf{g}(1,2)$ y compárala con $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01$.

</li>

</ol>

:::loesung
(a) Con $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$:

$$\mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2)=\begin{pmatrix}2{,}2\\6{,}2\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2{,}1)=\begin{pmatrix}2{,}31\\6{,}61\end{pmatrix},\quad \mathbf{g}(1;\,2{,}1)=\begin{pmatrix}2{,}1\\6{,}41\end{pmatrix}.$$

(b) Las imágenes de los dos lados que parten de $\mathbf{g}(1,2)$ son $(0{,}2;\ 0{,}2)^{\top}$ y $(0{,}1;\ 0{,}41)^{\top}$. Según el [capítulo 1, sección 14.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-1), el paralelogramo que generan tiene el área $|0{,}2\cdot0{,}41-0{,}1\cdot0{,}2|=0{,}062$. La matriz jacobiana predice $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01=6\cdot0{,}01=0{,}06$. La diferencia se debe a que el cuadrado no es arbitrariamente pequeño; el cuarto vértice, en $(2{,}31;\ 6{,}61)$, tampoco está exactamente donde lo tendría un paralelogramo verdadero, en $(2{,}3;\ 6{,}61)$, sino solo cerca.
:::
:::
