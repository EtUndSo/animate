---
title: El determinante
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15211500
summary: Una aplicación lineal deforma la cuadrícula del plano, y al hacerlo las áreas se hacen mayores o menores.
tags: determinante, orientación, desarrollo de Laplace
lang: es
---

<span class="anker" id="stufe-14"></span>

:::zweck
Una aplicación lineal deforma la cuadrícula del plano, y al hacerlo las áreas se hacen mayores o menores. Esta sección determina el factor en que cambian. Este factor es un único número, el determinante, y en él se reconoce también si una matriz es invertible.
:::

### El determinante de una matriz $2\times2$

<span class="anker" id="stufe-14-1"></span>

El cuadrado unidad tiene área $1$. Una matriz $\mathbf{A}$ lo lleva al paralelogramo que forman sus dos columnas (subsección [8.3](lineare-abbildungen.html#stufe-8-3)). ¿Qué área tiene este? La figura [40](#abb-40) lo muestra para $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$.

:::abbildung ml/k1det 40
A la izquierda, el cuadrado unidad, de área $1$; a la derecha, su imagen bajo $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$: el paralelogramo formado por las columnas $\mathbf{a}_1$ y $\mathbf{a}_2$. Tiene área $5=3\cdot2-1\cdot1$. A trazos, el rectángulo que lo encierra y a partir del cual puede calcularse el área.
:::

:::herleitung El área del paralelogramo
Sean las columnas $\mathbf{a}_1=(a,\,c)^{\top}$ y $\mathbf{a}_2=(b,\,d)^{\top}$, con todas las entradas positivas, y supongamos que $\mathbf{a}_2$ está a la izquierda y por encima de $\mathbf{a}_1$, como en la fig. [40](#abb-40). El paralelogramo de vértices $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$, $\mathbf{a}_2$ cabe en el rectángulo de lados $a+b$ y $c+d$. Para que solo quede el paralelogramo, se recortan del rectángulo dos triángulos de catetos $a$ y $c$, dos triángulos de catetos $b$ y $d$ y dos rectángulos de lados $b$ y $c$:

$$(a+b)(c+d)-2\cdot\tfrac12ac-2\cdot\tfrac12bd-2\,bc=ac+ad+bc+bd-ac-bd-2bc=ad-bc .$$

Para $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$: $4\cdot3-3-2-2=5$.
:::

:::definition Definición 14.1 (Determinante de una matriz $2\times2$)
<span class="anker" id="satz-14-1"></span>

El __determinante__ de la matriz $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ es el número

<span class="anker" id="gl-14-1"></span>
$$\det\mathbf{A}=ad-bc . \tag{14.1}$$
:::

Su valor absoluto es el área del paralelogramo que forman las columnas, es decir, el factor en que $\mathbf{A}$ cambia el área del cuadrado unidad. Es el mismo número que aparece en el denominador de la inversa [(11.2)](einheitsmatrix-und-inverse.html#gl-11-2).

⁠**Ejemplo numérico:** $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=6-1=5$, $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=2-1=1$, $\det\operatorname{diag}(2;\,0{,}5)=1$ y $\det\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=0$. El estiramiento cambia la forma del cuadrado, pero no su área: lo que estira a lo ancho lo quita en altura.

⁠**En resumen:** El determinante $ad-bc$ de una matriz $2\times2$ es, en valor absoluto, el factor en que la aplicación cambia el área del cuadrado unidad.

### El signo del determinante

<span class="anker" id="stufe-14-2"></span>

Un área nunca es negativa; el determinante puede serlo. El signo lleva una información adicional: si la aplicación refleja el plano.

En el cuadrado unidad, $\mathbf{e}_2$ está, visto desde $\mathbf{e}_1$, en sentido antihorario. Si en las imágenes sigue siendo así, es decir, si $\mathbf{a}_2$ está, visto desde $\mathbf{a}_1$, también en sentido antihorario, entonces $\det\mathbf{A}>0$. Si $\mathbf{a}_2$ está en sentido horario respecto de $\mathbf{a}_1$, el plano se ha reflejado, y $\det\mathbf{A}<0$. Esta propiedad se llama __orientación__: un determinante positivo conserva la orientación; uno negativo la invierte.

⁠**Ejemplo numérico:** La reflexión respecto del eje $x_1$, $\operatorname{diag}(1;\,-1)$, tiene el determinante $-1$: el área sigue siendo la misma, la orientación se invierte. Si se intercambian las columnas de una matriz, el determinante cambia de signo: $\det\bigl(\begin{smallmatrix}1&3\\2&1\end{smallmatrix}\bigr)=1-6=-5$. La rotación de $90^\circ$ tiene $\det=0\cdot0-(-1)\cdot1=1$; la cizalladura, $\det=1\cdot1-1\cdot0=1$; el aplastamiento $\operatorname{diag}(1;\,0)$, el determinante $0$.

⁠**En resumen:** El valor absoluto del determinante es el factor de área; su signo dice si la aplicación refleja.

### El factor de área vale para cualquier figura

<span class="anker" id="stufe-14-3"></span>

Hasta ahora se trataba del cuadrado unidad. Pero una aplicación lineal trata igual cada lugar del plano, y por eso cambia el área de cualquier figura en el mismo factor.

:::satz Teorema 14.2 (Factor de área)
<span class="anker" id="satz-14-2"></span>

Si $\mathbf{A}\in\mathbb{R}^{2\times2}$ transforma una figura de área $F$, la imagen tiene el área $|\det\mathbf{A}|\cdot F$.
:::

:::herleitung Factor de área
Se coloca sobre la figura una cuadrícula fina de pequeños cuadrados de lado $h$. Un cuadrado con el vértice $\mathbf{q}$ tiene los vértices $\mathbf{q}$, $\mathbf{q}+h\mathbf{e}_1$, $\mathbf{q}+h\mathbf{e}_1+h\mathbf{e}_2$ y $\mathbf{q}+h\mathbf{e}_2$. Su imagen tiene los vértices $\mathbf{A}\mathbf{q}$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1+h\mathbf{a}_2$ y $\mathbf{A}\mathbf{q}+h\mathbf{a}_2$: es el paralelogramo formado por $h\mathbf{a}_1$ y $h\mathbf{a}_2$, desplazado a $\mathbf{A}\mathbf{q}$. Su área es $h^2\,|\det\mathbf{A}|$, independientemente de dónde estuviera el cuadrado. Cada cuadrado pequeño se hace, por tanto, mayor o menor en el mismo factor $|\det\mathbf{A}|$. La figura consta aproximadamente de tales cuadrados, y cuanto más fina es la cuadrícula, más exacta es la aproximación. Por eso, el factor vale para toda la figura.
:::

⁠**Ejemplo numérico:** El círculo de radio $1$ tiene el área $\pi$. El estiramiento $\operatorname{diag}(3;\,2)$ lo convierte en una elipse de semiejes $3$ y $2$. Su área es $\pi\cdot3\cdot2=6\pi$, es decir, exactamente $|\det\mathbf{A}|=6$ veces el área del círculo. El triángulo de vértices $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ tiene el área $\tfrac12$; bajo $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ se convierte en el triángulo de vértices $\mathbf{0}$, $(3,1)^{\top}$, $(1,2)^{\top}$, de área $\tfrac52$.

⁠**En resumen:** Una aplicación lineal cambia el área de cualquier figura en el mismo factor $|\det\mathbf{A}|$, porque trata igual cada casilla pequeña de la cuadrícula.

### Determinantes de matrices mayores

<span class="anker" id="stufe-14-4"></span>

En el espacio, el cubo unidad se convierte en el paralelepípedo que forman las tres columnas de la matriz, un ortoedro deformado oblicuamente. Su volumen es el factor en que la aplicación cambia los volúmenes. También para matrices mayores existe un número así. Se calcula reduciéndolo a determinantes de matrices más pequeñas.

:::definition Definición 14.3 (Determinante)
<span class="anker" id="satz-14-3"></span>

Para $\mathbf{A}\in\mathbb{R}^{1\times1}$, $\det\mathbf{A}=a_{11}$. Para $\mathbf{A}\in\mathbb{R}^{n\times n}$ con $n\ge2$,

<span class="anker" id="gl-14-2"></span>
$$\det\mathbf{A}=\sum_{j=1}^n(-1)^{1+j}\,a_{1j}\,\det\mathbf{A}_{1j} , \tag{14.2}$$

donde $\mathbf{A}_{1j}$ es la matriz $(n-1)\times(n-1)$ que resulta de $\mathbf{A}$ al suprimir la primera fila y la columna $j$. Esta regla de cálculo se llama __desarrollo de Laplace__ por la primera fila.
:::

Para $n=2$, [(14.2)](#gl-14-2) vuelve a dar $a_{11}a_{22}-a_{12}a_{21}$. Igualmente se puede desarrollar por cualquier otra fila o columna, con el signo $(-1)^{i+j}$ para la entrada $a_{ij}$; el resultado es siempre el mismo. Para $n=3$, $|\det\mathbf{A}|$ es el volumen del paralelepípedo formado por las tres columnas, y el signo dice si las columnas están dispuestas en el mismo sentido de giro que $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ (regla de la mano derecha) o reflejadas.

⁠**Ejemplo numérico:** Para la matriz de coeficientes de la subsección [12.3](lineare-gleichungssysteme.html#stufe-12-3),

$$\mathbf{A}=\begin{pmatrix}1&2&1\\2&1&1\\1&1&2\end{pmatrix},$$

el desarrollo de Laplace por la primera fila da $\det\mathbf{A}=-4$ (fig. [41](#abb-41)).

:::abbildung ml/k1rlaplace 41
El desarrollo de Laplace por la primera fila: cada entrada de la primera fila por el determinante de la matriz restante sin su fila ni su columna, con signos alternos.
:::

Para una matriz triangular superior, bajo cuya diagonal solo hay ceros, se desarrolla una y otra vez por la primera columna y se obtiene el producto de las entradas diagonales, por ejemplo $\det\Bigl(\begin{smallmatrix}2&1&3\\0&3&1\\0&0&4\end{smallmatrix}\Bigr)=2\cdot3\cdot4=24$.

⁠**En resumen:** El determinante de una matriz $n\times n$ se reduce mediante el desarrollo de Laplace a determinantes más pequeños; su valor absoluto es el factor en que la aplicación cambia los volúmenes.

### Reglas de cálculo para determinantes

<span class="anker" id="stufe-14-5"></span>

La regla más importante se deduce directamente de la intuición. Si se encadenan dos aplicaciones, la primera cambia el volumen en su factor y la segunda cambia el resultado otra vez en el suyo. Los factores se multiplican.

:::satz Teorema 14.4 (Reglas de cálculo del determinante)
<span class="anker" id="satz-14-4"></span>

Para $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ y un número $c$ se cumple:

<ol class="rm">

<li>

$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\cdot\det\mathbf{B}$;

</li>

<li>

$\det\mathbf{A}^{\top}=\det\mathbf{A}$;

</li>

<li>

$\det\mathbf{A}^{-1}=1/\det\mathbf{A}$, si $\mathbf{A}$ es invertible;

</li>

<li>

$\det(c\,\mathbf{A})=c^n\det\mathbf{A}$;

</li>

<li>

si se suma a una fila un múltiplo de otra, el determinante no cambia; si se intercambian dos filas, cambia de signo; si se multiplica una fila por $c$, queda multiplicado por $c$.

</li>

</ol>
:::

La regla (iii) se sigue de (i) con $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$ y $\det\mathbf{I}=1$. La regla (iv) dice: si se estiran las $n$ aristas del cubo unidad en un factor $c$, su volumen crece en el factor $c^n$. La regla (v) hace de la eliminación gaussiana el camino práctico para calcular determinantes: se lleva la matriz a forma escalonada, se anota el número de intercambios y se multiplican las entradas diagonales.

⁠**Ejemplo numérico 1:** Con $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$ y $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=5$, el producto $\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ tiene que tener el determinante $5$: $21-16=5$.

⁠**Ejemplo numérico 2:** En la eliminación gaussiana de la subsección [12.3](lineare-gleichungssysteme.html#stufe-12-3), la matriz de coeficientes se llevó, con sumas de múltiplos y un intercambio, a la forma escalonada con la diagonal $1$, $-1$, $-4$. Así que su determinante es $(-1)\cdot\bigl(1\cdot(-1)\cdot(-4)\bigr)=-4$, como con el desarrollo de Laplace.

⁠**En resumen:** El determinante de un producto es el producto de los determinantes, porque los factores de volumen se multiplican al encadenar aplicaciones; en la práctica se calcula con la eliminación gaussiana.

:::hintergrund Por qué las operaciones de filas cambian el determinante precisamente así
Según la regla (ii), en lugar de las filas pueden transformarse igualmente las columnas, y las columnas forman el paralelogramo o el paralelepípedo. Si a una columna se le suma un múltiplo de otra, por ejemplo $\mathbf{a}_2\to\mathbf{a}_2+t\,\mathbf{a}_1$, el lado opuesto a $\mathbf{a}_1$ se desliza paralelamente a $\mathbf{a}_1$. El paralelogramo sufre una cizalladura, como una baraja de cartas que se empuja de lado. La base y la altura siguen siendo las mismas, y por tanto también el área. En el espacio ocurre lo mismo con el paralelepípedo: cada sección paralela a la base solo se desplaza, no se modifica, y los cuerpos con secciones de igual área a cada altura tienen el mismo volumen (principio de Cavalieri). Si se intercambian dos columnas, el área sigue siendo la misma, pero el sentido de giro de la primera a la segunda columna se invierte, y con él el signo. Si se multiplica una columna por $c$, una arista se hace $c$ veces más larga y el volumen $c$ veces mayor. Para matrices $2\times2$, la fórmula $ad-bc$ lo confirma directamente, por ejemplo para la cizalladura: $a\,(d+t\,c)-(b+t\,a)\,c=ad-bc$.

A la inversa, ya tres propiedades fijan por completo el determinante: $\det\mathbf{I}=1$; si se intercambian dos filas, cambia el signo; y si se mantienen fijas todas las filas menos una, el determinante es lineal en esa fila. Toda función de la matriz con estas tres propiedades es el determinante. La razón es la eliminación gaussiana: lleva toda matriz cuadrada, mediante operaciones de filas, a $\mathbf{I}$ o a una matriz con una fila nula, y el efecto de cada operación está fijado por las tres propiedades. Por eso, muchos libros de texto definen el determinante mediante estas propiedades y deducen de ellas el desarrollo de Laplace.
:::

:::hintergrund Por qué los determinantes no se calculan con el desarrollo de Laplace
El desarrollo de Laplace de una matriz $n\times n$ recurre a $n$ determinantes de tamaño $n-1$; cada uno de ellos, a $n-1$ de tamaño $n-2$, y así sucesivamente. Desarrollado por completo, salen $n!$ productos. Para $n=20$, son más de $2\cdot10^{18}$, un coste inasumible para un ordenador. La eliminación gaussiana, en cambio, solo necesita unas $\tfrac23n^3$ operaciones aritméticas básicas, es decir, para $n=20$, unos pocos miles. Por eso, el desarrollo de Laplace es una definición y una herramienta para matrices pequeñas y para deducciones, no un método de cálculo.
:::

### Determinante e invertibilidad

<span class="anker" id="stufe-14-6"></span>

Si el determinante es cero, el cuadrado unidad se convierte en una figura sin área, es decir, en un segmento o un punto. La aplicación aplasta el plano, y lo que se ha aplastado no puede recuperarse.

:::satz Teorema 14.5 (Determinante e invertibilidad)
<span class="anker" id="satz-14-5"></span>

Una matriz cuadrada $\mathbf{A}$ es invertible si y solo si $\det\mathbf{A}\ne0$.
:::

:::beweis Determinante e invertibilidad
Si $\mathbf{A}$ es invertible, según la regla (i), $\det\mathbf{A}\cdot\det\mathbf{A}^{-1}=\det\mathbf{I}=1$, así que $\det\mathbf{A}\ne0$. Si, a la inversa, $\det\mathbf{A}\ne0$, se lleva $\mathbf{A}$ a forma escalonada con la eliminación gaussiana. Según la regla (v), en este proceso el determinante a lo sumo se multiplica por factores distintos de cero, así que el determinante de la forma escalonada tampoco es cero. Es el producto de sus entradas diagonales, así que ninguna de ellas es cero, y hay $n$ pivotes. Con ello, $\operatorname{rango}\mathbf{A}=n$, y según el teorema de la subsección [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5), $\mathbf{A}$ es invertible.
:::

Junto con el teorema de la subsección [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5), para una matriz cuadrada son, por tanto, equivalentes: $\det\mathbf{A}\ne0$, $\mathbf{A}$ invertible, $\operatorname{rango}\mathbf{A}=n$, $\ker\mathbf{A}=\{\mathbf{0}\}$, columnas linealmente independientes.

⁠**Ejemplo numérico:** La matriz $\mathbf K$ de la subsección [13.4](unabhangigkeit-basis-und-rang.html#stufe-13-4) tiene $\det\mathbf K=1\cdot(2-1)-0+1\cdot(0-1)=0$, de acuerdo con $\operatorname{rango}\mathbf K=2$. La matriz de coeficientes del ejemplo de la eliminación gaussiana tiene $\det=-4\ne0$ y es invertible; por eso el sistema tenía exactamente una solución.

⁠**En resumen:** Una matriz cuadrada es invertible si y solo si su determinante no es cero, es decir, si no aplasta el espacio.

:::hintergrund Un determinante pequeño no significa «casi no invertible»
Se podría pensar que una matriz con un determinante muy pequeño es casi singular. No es así. La matriz $0{,}1\,\mathbf{I}_{10}$ tiene el determinante $0{,}1^{10}=10^{-10}$, pero es perfectamente invertible: su inversa es $10\,\mathbf{I}_{10}$, y lo único que hace es acortar todas las longitudes a una décima parte. El diminuto determinante se debe solo a que el factor $0{,}1$ se multiplica en diez direcciones. A la inversa, $\operatorname{diag}(1000;\,0{,}001)$ tiene el determinante $1$, aunque aplasta casi por completo el plano en una dirección. El determinante mide el volumen, y el volumen depende de la escala. Si una matriz «casi» destruye información no se ve en él de forma fiable.
:::

:::aufgabe Ejercicio 34 ★ Calcular determinantes
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Calcula los determinantes de $\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)$ y $\Bigl(\begin{smallmatrix}1&2&0\\3&1&2\\0&1&1\end{smallmatrix}\Bigr)$. ¿Cuál de las dos matrices es invertible?

</li>

<li>

¿Qué área tiene el triángulo de vértices $(0,\,0)$, $(3,\,1)$ y $(1,\,2)$?

</li>

<li>

¿Qué volumen tiene el paralelepípedo formado por los vectores $(1,\,0,\,0)^{\top}$, $(1,\,2,\,0)^{\top}$ y $(0,\,1,\,3)^{\top}$?

</li>

</ol>

:::loesung
(a) $\det\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)=4-4=0$: no es invertible; la segunda columna es el doble de la primera. Para la matriz $3\times3$, desarrollando por la primera fila:

$$1\cdot\det\begin{pmatrix}1&2\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}3&2\\0&1\end{pmatrix}+0=1\cdot(1-2)-2\cdot3=-7 .$$

Es invertible.

(b) El triángulo es la mitad del paralelogramo formado por $(3,1)^{\top}$ y $(1,2)^{\top}$, cuya área es $|\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)|=5$; tiene, por tanto, el área $2{,}5$. Lo mismo se sigue del factor de área: el triángulo de vértices $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$, de área $\tfrac12$, se transforma en este triángulo.

(c) Los vectores como columnas dan $\Bigl(\begin{smallmatrix}1&1&0\\0&2&1\\0&0&3\end{smallmatrix}\Bigr)$, una matriz triangular superior con el determinante $1\cdot2\cdot3=6$. El volumen es $6$.
:::
:::

:::aufgabe Ejercicio 35 ★★ Comprobar las reglas de cálculo
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

Comprueba $\det(\mathbf{C}\mathbf{D})=\det\mathbf{C}\cdot\det\mathbf{D}$ para $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ y $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ y calcula $\det(3\,\mathbf{C})$.

</li>

<li>

Demuestra que toda matriz de rotación $\mathbf R_\alpha$ tiene el determinante $1$. ¿Qué significa esto geométricamente?

</li>

<li>

Justifica sin hacer cálculos por qué una matriz con dos columnas iguales tiene el determinante $0$.

</li>

</ol>

:::loesung
(a) $\det\mathbf{C}=4-6=-2$, $\det\mathbf{D}=0-1=-1$ y $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, con $\det=14-12=2=(-2)\cdot(-1)$. Además, $3\mathbf{C}=\bigl(\begin{smallmatrix}3&6\\9&12\end{smallmatrix}\bigr)$, con $\det=36-54=-18=3^2\cdot(-2)$, como dice la regla (iv) con $n=2$.

(b) $\det\mathbf R_\alpha=\cos\alpha\cdot\cos\alpha-(-\sin\alpha)\cdot\sin\alpha=\cos^2\alpha+\sin^2\alpha=1$. Una rotación no cambia las áreas ni refleja.

(c) Dos columnas iguales son linealmente dependientes. El paralelogramo o el paralelepípedo que forman las columnas está aplastado, y su área o su volumen es cero. Lo mismo se sigue de la regla (v), trasladada a las columnas con $\det\mathbf{A}^{\top}=\det\mathbf{A}$: si se intercambian las dos columnas iguales, la matriz sigue siendo la misma, pero el determinante tendría que cambiar de signo. Por tanto, $\det\mathbf{A}=-\det\mathbf{A}$ y, con ello, $\det\mathbf{A}=0$.
:::
:::
