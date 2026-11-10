---
title: Aproximación mediante matrices de rango bajo
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Capítulo 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15221100
summary: La descomposición en valores singulares ordena los bloques de una matriz por su tamaño.
tags: norma de Frobenius, descomposición en valores singulares truncada
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
La descomposición en valores singulares ordena los bloques de una matriz por su tamaño. Si se omiten los pequeños, queda una matriz de rango menor, que puede guardarse con muchos menos números. Esta sección mide lo lejos que está esta aproximación de la matriz original y demuestra que ninguna otra matriz del mismo rango está más cerca.
:::

### La norma de Frobenius

<span class="anker" id="stufe-10-1"></span>

Para decir lo cerca que están dos matrices, se necesita una medida del tamaño de su diferencia. La norma espectral es una medida así; mide el alargamiento máximo. Hay una segunda aún más inmediata: se lee la matriz fila por fila, como una imagen en el [capítulo 1, sección 6.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1), para formar un vector largo, y se toma su norma euclídea.

:::definition Definición 10.1 (Norma de Frobenius)
<span class="anker" id="satz-10-1"></span>

La __norma de Frobenius__ de $\mathbf{A}\in\mathbb{R}^{m\times n}$ es

$$\lVert\mathbf{A}\rVert_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^na_{ij}^2} .$$
:::

:::satz Teorema 10.2 (Norma de Frobenius y valores singulares)
<span class="anker" id="satz-10-2"></span>

Para toda matriz $\mathbf{A}$ de rango $r$ se cumple

<span class="anker" id="gl-10-1"></span>
$$\lVert\mathbf{A}\rVert_F^2=\operatorname{tr}(\mathbf{A}^{\top}\mathbf{A})=d_1^2+d_2^2+\dots+d_r^2 . \tag{10.1}$$
:::

:::beweis Norma de Frobenius
La entrada diagonal $j$ de $\mathbf{A}^{\top}\mathbf{A}$ es $\mathbf{a}_j^{\top}\mathbf{a}_j=\sum_ia_{ij}^2$, el cuadrado de la longitud de la columna $j$. La traza, la suma de estas entradas, es, por tanto, la suma de todas las entradas de $\mathbf{A}$ al cuadrado. Según [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5), la traza es también la suma de los valores propios de $\mathbf{A}^{\top}\mathbf{A}$, y estos son los $d_j^2$.
:::

Dos consecuencias. Como $d_1^2\le\sum_jd_j^2$, es $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F$. Y una matriz ortogonal no cambia la norma de Frobenius: $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$; por tanto, $\mathbf{Q}\mathbf{A}$ y $\mathbf{A}$ tienen los mismos valores singulares.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ es $\lVert\mathbf{A}\rVert_F^2=4+9+0+4=17=4^2+1^2$ (fig. [24](#abb-24)); por tanto, $\lVert\mathbf{A}\rVert_F=\sqrt{17}\approx4{,}12$, algo más que $\lVert\mathbf{A}\rVert_2=4$.

:::abbildung ml/k2rfrobenius 24
El cuadrado de la norma de Frobenius de $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$: la suma de todas las entradas al cuadrado, igual a la suma de los valores singulares al cuadrado.
:::
::::

⁠**En resumen:** La norma de Frobenius es la norma euclídea de todas las entradas; su cuadrado es la suma de los valores singulares al cuadrado.

### La descomposición truncada

<span class="anker" id="stufe-10-2"></span>

Si se corta la suma [(9.4)](die-singularwertzerlegung.html#gl-9-4) después de los $k$ bloques mayores, se obtiene una aproximación.

:::definition Definición 10.3 (Descomposición en valores singulares truncada)
<span class="anker" id="satz-10-3"></span>

Para $k<r$,

<span class="anker" id="gl-10-2"></span>
$$\mathbf{A}_k=\sum_{j=1}^kd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} \tag{10.2}$$

se llama __descomposición en valores singulares truncada__ de $\mathbf{A}$ con $k$ bloques.
:::

$\mathbf{A}_k$ tiene rango $k$, pues $\mathbf{A}_k\mathbf{v}_j=d_j\mathbf{u}_j$ para $j\le k$ y $\mathbf{A}_k\mathbf{v}_j=\mathbf{0}$ para $j>k$; las imágenes generan, por tanto, un espacio de dimensión $k$. El error es el resto de la suma:

$$\mathbf{A}-\mathbf{A}_k=\sum_{j=k+1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} .$$

Su matriz de Gram es $\sum_{j>k}d_j^2\mathbf{v}_j\mathbf{v}_j^{\top}$, porque los términos cruzados desaparecen debido a $\mathbf{u}_i^{\top}\mathbf{u}_j=0$. Tiene los valores propios $d_{k+1}^2,\dots,d_r^2$ y, por lo demás, cero. Por tanto, el error tiene los valores singulares $d_{k+1},\dots,d_r$, y según [(9.5)](die-singularwertzerlegung.html#gl-9-5) y [(10.1)](#gl-10-1) es

<span class="anker" id="gl-10-3"></span>
$$\lVert\mathbf{A}-\mathbf{A}_k\rVert_2=d_{k+1},\qquad \lVert\mathbf{A}-\mathbf{A}_k\rVert_F=\sqrt{d_{k+1}^2+\dots+d_r^2} . \tag{10.3}$$

Para guardarla, $\mathbf{A}_k$ solo necesita los $k$ vectores $\mathbf{u}_j$, de $m$ entradas cada uno, los $k$ vectores $\mathbf{v}_j$, de $n$ entradas cada uno, y los $k$ números $d_j$: en total, $k(m+n+1)$ números en lugar de $mn$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ y $k=1$ es

$$\mathbf{A}_1=4\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\mathbf{u}_2\mathbf{v}_2^{\top}=\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}.$$

La norma de Frobenius del error es $\sqrt{0{,}16+0{,}04+0{,}64+0{,}16}=1=d_2$ (fig. [25](#abb-25)), igual que su norma espectral.

:::abbildung ml/k2rfehler 25
El cuadrado del error de la mejor aproximación de rango $1$ en la norma de Frobenius, con $0{,}4=\tfrac25$, $0{,}2=\tfrac15$ y $0{,}8=\tfrac45$: es $d_2^2=1$.
:::
::::

⁠**En resumen:** $\mathbf{A}_k$ conserva los $k$ bloques mayores; el error tiene los valores singulares restantes, y su norma espectral es $d_{k+1}$.

### La mejor aproximación

<span class="anker" id="stufe-10-3"></span>

Hay muchas matrices de rango $k$. ¿Es la descomposición truncada la mejor de ellas? Sí, en ambas normas.

:::satz Teorema 10.4 (Teorema de Eckart-Young)
<span class="anker" id="satz-10-4"></span>

Sea $\mathbf{A}$ de rango $r$ y $k<r$. Para toda matriz $\mathbf{B}$ del mismo tamaño con $\operatorname{rango}\mathbf{B}\le k$ se cumple

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_2,\qquad \lVert\mathbf{A}-\mathbf{B}\rVert_F\ge\sqrt{d_{k+1}^2+\dots+d_r^2}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_F . \tag{10.4}$$

Entre todas las matrices de rango como mucho $k$, $\mathbf{A}_k$ es, por tanto, la más cercana a $\mathbf{A}$.
:::

:::beweis Norma espectral
Según el teorema del rango, el núcleo de $\mathbf{B}$ tiene dimensión $n-\operatorname{rango}\mathbf{B}\ge n-k$. Se eligen $n-k$ vectores linealmente independientes $\mathbf{b}_1,\dots,\mathbf{b}_{n-k}$ del núcleo y se les añaden $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. Son $n+1$ vectores de $\mathbb{R}^n$ y, según el [capítulo 1, sección 13.4](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4), son linealmente dependientes, pues una matriz con $n$ filas tiene como mucho rango $n$. Existen, por tanto, números, no todos nulos, con $\sum_l\alpha_l\mathbf{b}_l=\sum_j\beta_j\mathbf{v}_j$. Este vector $\mathbf{z}$ no es nulo, pues de lo contrario, por la independencia de ambas listas, todos los números serían cero. Está en el núcleo de $\mathbf{B}$ y en el espacio generado por $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. Se normaliza a longitud $1$. Entonces $(\mathbf{A}-\mathbf{B})\mathbf{z}=\mathbf{A}\mathbf{z}$, y con $\mathbf{z}=\sum_{j\le k+1}c_j\mathbf{v}_j$, $\sum_jc_j^2=1$:

$$\lVert(\mathbf{A}-\mathbf{B})\mathbf{z}\rVert^2=\lVert\mathbf{A}\mathbf{z}\rVert^2=\sum_{j=1}^{k+1}d_j^2c_j^2\ge d_{k+1}^2\sum_{j=1}^{k+1}c_j^2=d_{k+1}^2 .$$

Por tanto, $\mathbf{A}-\mathbf{B}$ alarga el vector unitario $\mathbf{z}$ al menos por el factor $d_{k+1}$, y $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}$.
:::

La demostración muestra la razón: una matriz de rango $k$ tiene que transformar en cero todo un conjunto de direcciones, a saber, su núcleo. Este núcleo corta forzosamente el espacio de las $k+1$ direcciones que $\mathbf{A}$ más estira, y allí $\mathbf{B}$ comete un error de al menos $d_{k+1}$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, $\mathbf{A}_1$ es la mejor matriz de rango $1$, con el error $1$ en ambas normas. Otra matriz de rango $1$, por ejemplo $\mathbf{B}=\bigl(\begin{smallmatrix}2&3\\0&0\end{smallmatrix}\bigr)$, que simplemente suprime la segunda fila, tiene el error $\mathbf{A}-\mathbf{B}=\bigl(\begin{smallmatrix}0&0\\0&2\end{smallmatrix}\bigr)$, de norma $2$.
::::

⁠**En resumen:** La descomposición truncada $\mathbf{A}_k$ es la mejor aproximación de rango $k$, tanto en la norma espectral como en la de Frobenius.

:::hintergrund Por qué el enunciado vale también para la norma de Frobenius
La demostración para la norma de Frobenius ve las filas $\mathbf{a}^{(1)\top},\dots,\mathbf{a}^{(m)\top}$ de $\mathbf{A}$ como $m$ puntos de $\mathbb{R}^n$, como los ejemplos de una matriz de datos. Si $\mathbf{B}$ tiene como mucho rango $k$, sus filas están en un subespacio $\mathcal S$ de dimensión $k$: el espacio columna de $\mathbf{B}^{\top}$, completado hasta la dimensión $k$. Para un subespacio fijo $\mathcal S$ con la matriz de proyección $\mathbf{P}$, según la sección [4](projektion-auf-einen-unterraum.html#stufe-4), la proyección $\mathbf{P}\mathbf{a}^{(i)}$ de cada fila es el punto más cercano de $\mathcal S$. Con una base ortonormal $\mathbf{w}_1,\dots,\mathbf{w}_k$ de $\mathcal S$, el teorema de Pitágoras da

$$\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge\sum_i\bigl\lVert\mathbf{a}^{(i)}-\mathbf{P}\mathbf{a}^{(i)}\bigr\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_i\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2 ,$$

pues $\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\sum_l(\mathbf{w}_l^{\top}\mathbf{a}^{(i)})^2$, y $\mathbf{w}_l^{\top}\mathbf{a}^{(i)}$ es la entrada $i$ de $\mathbf{A}\mathbf{w}_l$. Queda por demostrar que $\sum_l\lVert\mathbf{A}\mathbf{w}_l\rVert^2\le d_1^2+\dots+d_k^2$. En las coordenadas de los $\mathbf{v}_j$ es

$$\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2=\sum_{l=1}^k\sum_jd_j^2(\mathbf{v}_j^{\top}\mathbf{w}_l)^2=\sum_jd_j^2\,g_j\qquad\text{con}\qquad g_j=\sum_{l=1}^k(\mathbf{v}_j^{\top}\mathbf{w}_l)^2 .$$

Cada $g_j$ es el cuadrado de la longitud de la proyección de $\mathbf{v}_j$ sobre $\mathcal S$; por tanto, $0\le g_j\le1$, y la suma de todos los $g_j$ es $\sum_l\lVert\mathbf{w}_l\rVert^2=k$. Una suma $\sum_jd_j^2g_j$ con tales pesos es máxima cuando los $k$ mayores $d_j^2$ reciben el peso completo $1$; eso da $d_1^2+\dots+d_k^2$. Junto con [(10.1)](#gl-10-1) se sigue $\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge d_{k+1}^2+\dots+d_r^2$. El cálculo muestra, de paso, que el subespacio al que están más cerca las filas de $\mathbf{A}$ es el espacio generado por $\mathbf{v}_1,\dots,\mathbf{v}_k$.
:::

### Una imagen con pocos números

<span class="anker" id="stufe-10-4"></span>

Una imagen en escala de grises es una matriz. Según el teorema de Eckart-Young, $\mathbf{A}_k$ es la mejor aproximación con $k$ bloques, y [(10.3)](#gl-10-3) dice cuánto se pierde. La proporción

$$\frac{d_1^2+\dots+d_k^2}{d_1^2+\dots+d_r^2}$$

indica qué parte de la suma de todos los valores de brillo al cuadrado se conserva.

::::beispiel [Ejemplo numérico]
La cruz del [capítulo 1, sección 6.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1), es

$$\mathbf{C}=\begin{pmatrix}0&1&0\\1&1&1\\0&1&0\end{pmatrix}.$$

Es simétrica. Su polinomio característico es $-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda-2)(\lambda+1)$; los valores propios son $2$, $-1$ y $0$, con los vectores propios $(1,\,2,\,1)^{\top}$, $(1,\,-1,\,1)^{\top}$ y $(1,\,0,\,-1)^{\top}$. Según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), los valores singulares son $2$, $1$ y $0$; el rango es $2$. Con $\mathbf{q}_1=(1,\,2,\,1)^{\top}/\sqrt6$, la mejor aproximación de rango $1$ es

$$\mathbf{C}_1=2\,\mathbf{q}_1\mathbf{q}_1^{\top}=\frac13\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix},\qquad \mathbf{C}-\mathbf{C}_1=\frac13\begin{pmatrix}-1&1&-1\\1&-1&1\\-1&1&-1\end{pmatrix}$$

(fig. [26](#abb-26)). El error tiene tamaño $1$ en ambas normas. $\mathbf{C}_1$ conserva el $4/5=80\,\%$ de la suma $\lVert\mathbf{C}\rVert_F^2=5$. Cada fila de $\mathbf{C}_1$ es un múltiplo de la misma fila $(1,\,2,\,1)$: una imagen de rango $1$ es un perfil de brillo de las columnas por un perfil de brillo de las filas; aquí, una mancha difuminada con el punto más claro en el centro. Hay que guardar $1\cdot(3+3+1)=7$ números en lugar de $9$.

:::abbildung ml/k2bild 26
La cruz $\mathbf{C}$ de $3\times3$ píxeles (izquierda; $0$ negro, $1$ blanco), su mejor aproximación $\mathbf{C}_1$ de rango $1$ (centro; el valor $\tfrac43$ es más claro que el blanco y se representa en blanco) y el error $\mathbf{C}-\mathbf{C}_1$ (derecha; rojo positivo, azul negativo). El error es a su vez una matriz de rango $1$: el bloque asociado al valor singular $1$.
:::
::::

En una cruz de $3\times3$ píxeles, esto ahorra poco. En imágenes grandes, la diferencia es considerable: una imagen de $1000\times1000$ píxeles tiene $10^6$ entradas; la aproximación con $k=50$ bloques necesita $50\cdot(1000+1000+1)=100\,050$ números, alrededor del $10\,\%$. Que la aproximación se vea bien depende de lo rápido que decrezcan los valores singulares. En muchas fotos, las filas vecinas se parecen mucho; las filas están entonces cerca de un subespacio de dimensión pequeña, y unos pocos valores singulares grandes se llevan casi toda la suma $\sum_jd_j^2$.

⁠**En resumen:** Una imagen de rango $k$ necesita $k(m+n+1)$ números; la descomposición truncada es la mejor imagen de este tipo, y $\sum_{j\le k}d_j^2/\sum_jd_j^2$ dice cuánto se conserva.

:::aufgabe Ejercicio 30 ★ Normas de una matriz
<span class="anker" id="aufg-30"></span>

<ol class="al">

<li>

Calcula $\lVert\mathbf{A}\rVert_F$ y $\lVert\mathbf{A}\rVert_2$ para $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$ del ejercicio [27](die-singularwertzerlegung.html#aufg-27) y comprueba [(10.1)](#gl-10-1).

</li>

<li>

¿Qué norma de Frobenius tiene una matriz ortogonal $n\times n$?

</li>

<li>

Demuestra $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F\le\sqrt r\,\lVert\mathbf{A}\rVert_2$. ¿Cuándo se da la igualdad a la derecha?

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{A}\rVert_F^2=9+0+16+25=50=45+5=d_1^2+d_2^2$; por tanto, $\lVert\mathbf{A}\rVert_F=\sqrt{50}\approx7{,}07$, y $\lVert\mathbf{A}\rVert_2=d_1=3\sqrt5\approx6{,}71$.

(b) Todos los valores singulares de una matriz ortogonal son $1$; por tanto, $\lVert\mathbf{Q}\rVert_F^2=n$ y $\lVert\mathbf{Q}\rVert_F=\sqrt n$. Igual de directo: el cuadrado de la longitud de cada una de las $n$ columnas es $1$.

(c) Se tiene $\lVert\mathbf{A}\rVert_2^2=d_1^2\le d_1^2+\dots+d_r^2=\lVert\mathbf{A}\rVert_F^2$, y cada uno de los $r$ sumandos es como mucho $d_1^2$; por tanto, $\lVert\mathbf{A}\rVert_F^2\le r\,d_1^2$. Extrayendo la raíz se obtienen ambas desigualdades. A la derecha se da la igualdad si y solo si todos los valores singulares positivos son iguales a $d_1$, como en una matriz ortogonal.
:::
:::

:::aufgabe Ejercicio 31 ★★ La mejor matriz de rango 1
<span class="anker" id="aufg-31"></span>

Sea $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$ del ejercicio [28](die-singularwertzerlegung.html#aufg-28).

<ol class="al">

<li>

Calcula $\mathbf{A}_1$ y el error $\mathbf{A}-\mathbf{A}_1$ en ambas normas.

</li>

<li>

La matriz $\mathbf{B}$ formada solo por unos también tiene rango $1$. Calcula $\lVert\mathbf{A}-\mathbf{B}\rVert_F$ y $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ y compara con (a).

</li>

<li>

¿Qué proporción de la suma de las entradas al cuadrado se conserva en $\mathbf{A}_1$?

</li>

</ol>

:::loesung
(a) Del ejercicio [28](die-singularwertzerlegung.html#aufg-28): $d_1=2$, $\mathbf{u}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$. Por tanto,

$$\mathbf{A}_1=2\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1&1\\1&1\\0&0\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\begin{pmatrix}0&0\\0&0\\1&-1\end{pmatrix}.$$

El error tiene la norma de Frobenius $\sqrt{1+1}=\sqrt2=d_2$. Es el producto exterior $\mathbf{e}_3\,(1,\,-1)$, que, según el ejercicio [29](die-singularwertzerlegung.html#aufg-29), tiene el único valor singular $1\cdot\sqrt2$; también su norma espectral es $\sqrt2$.

(b) $\mathbf{A}-\mathbf{B}=\Bigl(\begin{smallmatrix}0&0\\0&0\\0&-2\end{smallmatrix}\Bigr)$ tiene en ambas normas el valor $2>\sqrt2$. Como exige el teorema de Eckart-Young, $\mathbf{B}$ está más lejos de $\mathbf{A}$ que $\mathbf{A}_1$.

(c) $\lVert\mathbf{A}\rVert_F^2=6=4+2$, y $\mathbf{A}_1$ conserva $d_1^2/(d_1^2+d_2^2)=\tfrac46=\tfrac23\approx67\,\%$.
:::
:::

:::aufgabe Ejercicio 32 ★ Memoria necesaria
<span class="anker" id="aufg-32"></span>

Una imagen en escala de grises tiene $600\times800$ píxeles.

<ol class="al">

<li>

¿Cuántos números necesita la aproximación con $k=40$ bloques? ¿Qué proporción del número original de valores es?

</li>

<li>

¿A partir de qué $k$ la aproximación deja de ahorrar memoria?

</li>

</ol>

:::loesung
(a) $40\cdot(600+800+1)=40\cdot1\,401=56\,040$ números en lugar de $600\cdot800=480\,000$, es decir, alrededor del $11{,}7\,\%$.

(b) La aproximación ahorra memoria mientras $k\cdot1\,401<480\,000$, es decir, para $k\le342$, pues $342\cdot1\,401=479\,142$ y $343\cdot1\,401=480\,543$. A partir de $k=343$, la aproximación necesita más números que la propia imagen. El rango es como mucho $600$; de todos modos, no hay más de $600$ bloques.
:::
:::
