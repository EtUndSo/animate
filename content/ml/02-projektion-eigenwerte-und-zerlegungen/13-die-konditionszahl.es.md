---
title: El número de condición
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15221300
summary: Los datos medidos nunca son exactos, y un ordenador redondea en cada paso.
tags: número de condición
lang: es
---

<span class="anker" id="stufe-12"></span>

:::zweck
Los datos medidos nunca son exactos, y un ordenador redondea en cada paso. ¿Cuánto cambia la solución de un sistema de ecuaciones si el lado derecho es un poco erróneo? Esta sección muestra que un único número, obtenido de los valores singulares, da la respuesta, y qué significa para las ecuaciones normales.
:::

### Un sistema de ecuaciones sensible

<span class="anker" id="stufe-12-1"></span>

El sistema de ecuaciones

$$x_1+x_2=2,\qquad x_1+1{,}01\,x_2=2{,}01$$

tiene la solución $\mathbf{x}=(1,\,1)^{\top}$. Si se cambia el lado derecho de la segunda ecuación en $0{,}01$, a $2{,}02$, la diferencia de las ecuaciones da $0{,}01\,x_2=0{,}02$, es decir, $x_2=2$ y $x_1=0$. Un cambio de los datos en la tercera cifra desplaza la solución tanto como su propio tamaño.

Geométricamente, las dos ecuaciones son dos rectas que se cortan en el punto solución. Aquí son casi paralelas: se cortan con un ángulo de solo unos $0{,}29^\circ$. Si se desplaza un poco una de ellas, el punto de corte se mueve mucho a lo largo de la otra (fig. [28](#abb-28)). Si, en cambio, las rectas son perpendiculares, se mueve solo tanto como se desplaza la recta.

:::abbildung ml/k2kondition 28
Dos veces el mismo desplazamiento de la recta roja, en una distancia de $0{,}2$ (a trazos). A la izquierda corta perpendicularmente a la recta azul, y el punto de corte se mueve $0{,}2$. A la derecha, las rectas se cortan a $8^\circ$, y el punto de corte se mueve $0{,}2/\sin8^\circ\approx1{,}44$. Cuanto menor es el ángulo de corte, más sensible es la solución a los cambios de los datos.
:::

¿Qué magnitud tiene el efecto, medido en relación con las propias magnitudes? El lado derecho $\mathbf{y}=(2;\ 2{,}01)^{\top}$ tiene la longitud $\sqrt{4+4{,}0401}\approx2{,}8355$ (fig. [29](#abb-29)), y el cambio $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$, la longitud $0{,}01$. El lado derecho cambia, por tanto, en términos relativos, un $0{,}01/2{,}8355\approx0{,}35\,\%$. La solución cambia en $\Delta\mathbf{x}=(-1,\,1)^{\top}$, en términos relativos, un $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt2/\sqrt2=100\,\%$. El error relativo se amplifica unas $284$ veces.

:::abbildung ml/k2rnormy 29
El cuadrado de la longitud del lado derecho como producto escalar $\mathbf{y}^{\top}\mathbf{y}$; la longitud es $\sqrt{8{,}0401}\approx2{,}8355$.
:::

⁠**En resumen:** Si las rectas de un sistema de ecuaciones se cortan casi en paralelo, pequeños cambios de los datos desplazan mucho la solución.

### El número de condición

<span class="anker" id="stufe-12-2"></span>

¿De dónde viene el factor? Con la descomposición en valores singulares, la amplificación puede acotarse con precisión.

:::definition Definición 12.1 (Número de condición)
<span class="anker" id="satz-12-1"></span>

Sea $\mathbf{A}\in\mathbb{R}^{m\times n}$ con columnas linealmente independientes, es decir, $d_n>0$. El __número de condición__ de $\mathbf{A}$ es

<span class="anker" id="gl-12-1"></span>
$$\kappa(\mathbf{A})=\frac{d_1}{d_n}, \tag{12.1}$$

el cociente entre el estiramiento máximo y el mínimo.
:::

Siempre es $\kappa(\mathbf{A})\ge1$. Una matriz ortogonal tiene $\kappa=1$, pues todos sus valores singulares son $1$. Una matriz con un número de condición grande se llama mal condicionada.

:::satz Teorema 12.2 (Amplificación del error)
<span class="anker" id="satz-12-2"></span>

Sea $\mathbf{A}\in\mathbb{R}^{n\times n}$ invertible, $\mathbf{A}\mathbf{x}=\mathbf{y}$ con $\mathbf{y}\ne\mathbf{0}$ y $\mathbf{A}(\mathbf{x}+\Delta\mathbf{x})=\mathbf{y}+\Delta\mathbf{y}$. Entonces

<span class="anker" id="gl-12-2"></span>
$$\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(\mathbf{A})\,\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} . \tag{12.2}$$

La igualdad se da cuando $\mathbf{y}$ apunta en la dirección de $\mathbf{u}_1$ y $\Delta\mathbf{y}$ en la dirección de $\mathbf{u}_n$.
:::

:::beweis Amplificación del error
De ambas ecuaciones se sigue $\mathbf{A}\Delta\mathbf{x}=\Delta\mathbf{y}$. Según [(9.5)](die-singularwertzerlegung.html#gl-9-5), $\lVert\mathbf{y}\rVert=\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\lVert\mathbf{x}\rVert$, es decir, $1/\lVert\mathbf{x}\rVert\le d_1/\lVert\mathbf{y}\rVert$, y $\lVert\Delta\mathbf{y}\rVert=\lVert\mathbf{A}\Delta\mathbf{x}\rVert\ge d_n\lVert\Delta\mathbf{x}\rVert$, es decir, $\lVert\Delta\mathbf{x}\rVert\le\lVert\Delta\mathbf{y}\rVert/d_n$. Multiplicando ambas desigualdades se obtiene [(12.2)](#gl-12-2). Si $\mathbf{y}$ apunta en la dirección de $\mathbf{u}_1$, $\mathbf{x}$ es un múltiplo de $\mathbf{v}_1$ y la primera desigualdad es una igualdad; si $\Delta\mathbf{y}$ apunta en la dirección de $\mathbf{u}_n$, $\Delta\mathbf{x}$ es un múltiplo de $\mathbf{v}_n$ y la segunda es una igualdad.
:::

El peor caso es, por tanto, este: la solución está en la dirección que $\mathbf{A}$ más estira, de modo que $\mathbf{y}$ es grande comparado con $\mathbf{x}$, y el error está en la dirección que $\mathbf{A}$ menos estira, de modo que, al deshacer la transformación, se agranda por el factor $1/d_n$.

⁠**Ejemplo numérico:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$ es simétrica, con la traza $2{,}01$ y el determinante $0{,}01$. Sus valores propios son

$$\lambda_{1,2}=\frac{2{,}01\pm\sqrt{2{,}01^2-0{,}04}}2=\frac{2{,}01\pm\sqrt{4{,}0001}}2\approx\frac{2{,}01\pm2{,}000025}2,$$

es decir, $\lambda_1\approx2{,}005012$ y $\lambda_2\approx0{,}004988$, ambos positivos. Según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), son también los valores singulares, y $\kappa(\mathbf{A})\approx402$. La amplificación observada, $284$, queda por debajo. No alcanza del todo la cota porque $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ no apunta exactamente en la dirección de $\mathbf{u}_2\approx(1,\,-1)^{\top}/\sqrt2$. Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ es $\kappa=4/1=4$: los errores relativos se multiplican como mucho por cuatro.

⁠**En resumen:** El número de condición $\kappa(\mathbf{A})=d_1/d_n$ es el mayor factor por el que $\mathbf{A}^{-1}$ puede agrandar en la solución un error relativo de los datos.

### Número de condición y determinante

<span class="anker" id="stufe-12-3"></span>

En el recuadro de contexto de Fundamentos 1, sección 14.6, había una advertencia: un determinante pequeño no significa que una matriz sea casi singular. El número de condición mide lo que allí se quería decir.

:::satz Teorema 12.3 (Distancia a la matriz singular más cercana)
<span class="anker" id="satz-12-3"></span>

Para una matriz invertible $\mathbf{A}\in\mathbb{R}^{n\times n}$, la distancia mínima $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ a una matriz singular $\mathbf{B}$ es igual a $d_n$. En relación con la magnitud $\lVert\mathbf{A}\rVert_2=d_1$, es

<span class="anker" id="gl-12-3"></span>
$$\min_{\mathbf{B}\ \text{singular}}\frac{\lVert\mathbf{A}-\mathbf{B}\rVert_2}{\lVert\mathbf{A}\rVert_2}=\frac1{\kappa(\mathbf{A})} . \tag{12.3}$$
:::

:::beweis Distancia
Una matriz singular tiene como mucho rango $n-1$. Según el teorema de Eckart-Young con $k=n-1$, $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_n$, y la matriz singular $\mathbf{A}_{n-1}$ está exactamente a la distancia $d_n$.
:::

Un número de condición grande significa, por tanto, que un cambio relativamente pequeño hace singular la matriz. El determinante mide otra cosa. Según el ejercicio [29](die-singularwertzerlegung.html#aufg-29), $|\det\mathbf{A}|=d_1\cdots d_n$, el producto de todos los estiramientos; depende de la magnitud de la matriz. El número de condición es un cociente y no cambia si se multiplica $\mathbf{A}$ por un número: $\kappa(c\mathbf{A})=\kappa(\mathbf{A})$ para $c\ne0$. Solo mide lo achatada que es la elipse en la que $\mathbf{A}$ transforma la circunferencia unidad.

⁠**Ejemplo numérico:** Las dos matrices de Fundamentos 1, sección 14.6: $0{,}1\cdot\mathbf{I}_{10}$ tiene el determinante $10^{-10}$, pero todos sus valores singulares son $0{,}1$, y $\kappa=1$; está tan bien condicionada como es posible. $\operatorname{diag}(1000;\ 0{,}001)$ tiene el determinante $1$, pero $\kappa=1000/0{,}001=10^6$. Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$, la distancia a la matriz singular más cercana es $d_2\approx0{,}005$: si se cambian sus entradas en unas pocas milésimas, se vuelve singular. La matriz singular $\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ está a la distancia $\lVert\bigl(\begin{smallmatrix}0&0\\0&0{,}01\end{smallmatrix}\bigr)\rVert_2=0{,}01$, algo más que el mínimo.

⁠**En resumen:** $1/\kappa(\mathbf{A})$ es la distancia relativa a la matriz singular más cercana; el determinante no dice nada sobre ello, porque depende de la magnitud de la matriz.

### Las ecuaciones normales elevan al cuadrado el número de condición

<span class="anker" id="stufe-12-4"></span>

La mejor solución aproximada puede calcularse con las ecuaciones normales, $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$, o con la descomposición QR, $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$. Matemáticamente, ambas dan lo mismo. Con números redondeados, no, y la razón es el número de condición.

:::satz Teorema 12.4 (Número de condición de la matriz de Gram)
<span class="anker" id="satz-12-4"></span>

Si $\mathbf{A}$ tiene columnas linealmente independientes, entonces

<span class="anker" id="gl-12-4"></span>
$$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2 . \tag{12.4}$$

Para la descomposición QR $\mathbf{A}=\mathbf{Q}\mathbf{R}$, en cambio, $\kappa(\mathbf{R})=\kappa(\mathbf{A})$.
:::

:::beweis Matriz de Gram
$\mathbf{A}^{\top}\mathbf{A}$ es simétrica y definida positiva, con los valores propios $d_j^2$; según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), estos son también sus valores singulares, y su cociente es $d_1^2/d_n^2$. Como $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, es $\mathbf{R}^{\top}\mathbf{R}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{A}^{\top}\mathbf{A}$; $\mathbf{R}$ tiene, por tanto, los mismos valores singulares que $\mathbf{A}$.
:::

⁠**Ejemplo numérico:** La matriz de las viviendas de la sección [3.7](die-beste-naherungslosung.html#stufe-3-7), con la superficie y el número de habitaciones, tiene los valores singulares $d_1\approx135{,}02$ y $d_2\approx0{,}848$; es decir, $\kappa(\mathbf{A})\approx159{,}3$ y $\kappa(\mathbf{A}^{\top}\mathbf{A})\approx25\,367$. Dos causas hacen grande $\kappa(\mathbf{A})$. Primera, las unidades: las superficies son números en torno a $65$; los números de habitaciones, en torno a $2{,}5$. Si se mide la superficie en unidades de $10\,\mathrm m^2$, el número de condición baja a unos $18{,}5$. Segunda, las dos columnas apuntan casi en la misma dirección: forman un ángulo de solo unos $8{,}9^\circ$. Por eso, aunque se lleven ambas columnas a longitud $1$, queda $\kappa\approx12{,}8$. El cambio de unidades no altera los valores ajustados $\hat{\mathbf{y}}$: si se divide una columna por $10$, el peso correspondiente se hace $10$ veces mayor, y los productos no cambian.

⁠**En resumen:** Las ecuaciones normales trabajan con $\kappa(\mathbf{A})^2$; la descomposición QR, con $\kappa(\mathbf{A})$; unas unidades bien elegidas reducen el número de condición.

:::hintergrund Lo que hace el ordenador con el número de condición
Un ordenador guarda los números, habitualmente, con unas $16$ cifras decimales significativas y redondea tras cada operación aritmética. Un buen procedimiento da la solución exacta de un problema cuyos datos solo se han modificado en el orden de magnitud de este redondeo; tales procedimientos se llaman estables hacia atrás. Según [(12.2)](#gl-12-2), el resultado tiene entonces un error relativo de, como mucho, unos $\kappa\cdot10^{-16}$: se pierden aproximadamente $\log_{10}\kappa$ de las $16$ cifras.

El camino por la descomposición QR (y por la descomposición en valores singulares) es estable hacia atrás; con un residuo pequeño, su error crece aproximadamente como $\kappa(\mathbf{A})$. El camino por las ecuaciones normales no lo es: trabaja con la matriz $\mathbf{A}^{\top}\mathbf{A}$, y su error crece siempre como $\kappa(\mathbf{A})^2$, aunque el residuo sea pequeño. Con $\kappa(\mathbf{A})=10^6$, por este camino se pierden unas $12$ de las $16$ cifras; con QR, unas $6$. En las viviendas, con $\kappa(\mathbf{A})^2\approx2{,}5\cdot10^4$, esto aún es inofensivo; en grandes conjuntos de datos con características casi dependientes, no. Por eso, los buenos programas calculan la mejor solución aproximada mediante QR o mediante la descomposición en valores singulares, y no mediante las ecuaciones normales, aunque estas sean las que describen la teoría de la forma más breve.
:::

:::aufgabe Ejercicio 36 ★ Leer números de condición
<span class="anker" id="aufg-36"></span>

Determina el número de condición de

<ol class="al">

<li>

$\operatorname{diag}(2;\ 0{,}5)$ y $\operatorname{diag}(-3;\ 3)$;

</li>

<li>

la matriz de rotación de $30^\circ$;

</li>

<li>

$5\mathbf{A}$ para $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. Compara los determinantes de $\mathbf{A}$ y $5\mathbf{A}$.

</li>

</ol>

:::loesung
(a) $\operatorname{diag}(2;\,0{,}5)$ tiene los valores singulares $2$ y $0{,}5$; por tanto, $\kappa=4$. $\operatorname{diag}(-3;\,3)$ tiene, según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), los valores singulares $3$ y $3$; por tanto, $\kappa=1$, aunque los valores propios tengan signos distintos.

(b) Una matriz de rotación es ortogonal, y todos sus valores singulares son $1$: $\kappa=1$.

(c) $5\mathbf{A}$ tiene los valores singulares $20$ y $5$; por tanto, de nuevo $\kappa=4$. El determinante, en cambio, crece de $4$ a $\det(5\mathbf{A})=25\cdot4=100$.
:::
:::

:::aufgabe Ejercicio 37 ★★ Determinante 1 y, aun así, mal condicionada
<span class="anker" id="aufg-37"></span>

Sea $\mathbf{A}=\bigl(\begin{smallmatrix}10&7\\7&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Calcula $\det\mathbf{A}$ y $\mathbf{A}^{-1}$. Resuelve $\mathbf{A}\mathbf{x}=(17,\,12)^{\top}$ y $\mathbf{A}\mathbf{x}=(17;\ 12{,}1)^{\top}$.

</li>

<li>

Calcula los cambios relativos de $\mathbf{y}$ y de $\mathbf{x}$ y su cociente.

</li>

<li>

Calcula $\kappa(\mathbf{A})$ y comprueba [(12.2)](#gl-12-2). ¿A qué distancia está $\mathbf{A}$ de la matriz singular más cercana?

</li>

</ol>

:::loesung
(a) $\det\mathbf{A}=50-49=1$ y $\mathbf{A}^{-1}=\bigl(\begin{smallmatrix}5&-7\\-7&10\end{smallmatrix}\bigr)$. Así, $\mathbf{A}^{-1}(17,\,12)^{\top}=(85-84,\ -119+120)^{\top}=(1,\,1)^{\top}$ y $\mathbf{A}^{-1}(17;\ 12{,}1)^{\top}=(85-84{,}7;\ -119+121)^{\top}=(0{,}3;\ 2)^{\top}$.

(b) $\lVert\Delta\mathbf{y}\rVert/\lVert\mathbf{y}\rVert=0{,}1/\sqrt{433}\approx0{,}1/20{,}809\approx0{,}48\,\%$. $\Delta\mathbf{x}=(-0{,}7;\ 1)^{\top}$; por tanto, $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt{1{,}49}/\sqrt2\approx1{,}2207/1{,}4142\approx86{,}3\,\%$. El cociente es de alrededor de $180$.

(c) $\mathbf{A}$ es simétrica, con traza $15$ y determinante $1$; por tanto, $\lambda=\tfrac{15\pm\sqrt{221}}2\approx14{,}933$ y $0{,}0670$, ambos positivos. Según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), estos son los valores singulares, y $\kappa(\mathbf{A})\approx14{,}933/0{,}0670\approx223$. La cota [(12.2)](#gl-12-2) se cumple: $86{,}3\,\%\le223\cdot0{,}48\,\%\approx107\,\%$. La distancia a la matriz singular más cercana es $d_2\approx0{,}067$; en términos relativos, $1/223$. El determinante $1$ no revela nada de esto.
:::
:::

:::aufgabe Ejercicio 38 ★★★ Reglas de cálculo para el número de condición
<span class="anker" id="aufg-38"></span>

Sea $\mathbf{A}\in\mathbb{R}^{n\times n}$ invertible y $\mathbf{Q}$ ortogonal. Demuestra:

<ol class="al">

<li>

$\kappa(\mathbf{Q}\mathbf{A})=\kappa(\mathbf{A})$ y $\kappa(\mathbf{A}^{-1})=\kappa(\mathbf{A})$;

</li>

<li>

para todos los valores propios $\lambda$ y $\mu$ de $\mathbf{A}$ es $|\lambda|/|\mu|\le\kappa(\mathbf{A})$;

</li>

<li>

para $\mathbf{A}$ simétrica, $\kappa(\mathbf{A})=|\lambda|_{\max}/|\lambda|_{\min}$, el cociente entre el valor propio de mayor valor absoluto y el de menor valor absoluto.

</li>

</ol>

:::loesung
(a) Según el ejercicio [29](die-singularwertzerlegung.html#aufg-29), $\mathbf{Q}\mathbf{A}$ tiene los mismos valores singulares que $\mathbf{A}$ y, por tanto, el mismo número de condición. De $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ se deduce $\mathbf{A}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$, una descomposición en valores singulares con los valores singulares $1/d_j$. El mayor es $1/d_n$, y el menor, $1/d_1$; por tanto, $\kappa(\mathbf{A}^{-1})=\tfrac{1/d_n}{1/d_1}=\tfrac{d_1}{d_n}=\kappa(\mathbf{A})$.

(b) Para un vector propio $\mathbf{v}$ asociado a $\lambda$, según [(9.5)](die-singularwertzerlegung.html#gl-9-5), se cumple $d_n\lVert\mathbf{v}\rVert\le\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert\le d_1\lVert\mathbf{v}\rVert$; por tanto, $d_n\le|\lambda|\le d_1$. Para vectores propios complejos vale igualmente, como se mostró en la sección [9.8](die-singularwertzerlegung.html#stufe-9-8). Lo mismo vale para $\mu$. Por tanto, $|\lambda|/|\mu|\le d_1/d_n$.

(c) Para $\mathbf{A}$ simétrica, los valores singulares son, según la sección [9.7](die-singularwertzerlegung.html#stufe-9-7), los valores absolutos $|\lambda_i|$. Por tanto, el mayor valor singular es $|\lambda|_{\max}$, y el menor, $|\lambda|_{\min}$.
:::
:::
