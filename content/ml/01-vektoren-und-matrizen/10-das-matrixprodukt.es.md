---
title: El producto de matrices
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15211000
summary: Dos aplicaciones lineales una tras otra dan de nuevo una aplicación lineal, es decir, una matriz.
tags: producto de matrices, producto exterior
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Dos aplicaciones lineales una tras otra dan de nuevo una aplicación lineal, es decir, una matriz. Esta sección la determina. El resultado es el producto de matrices, y su definición se deduce forzosamente de este planteamiento.
:::

### El producto de matrices

<span class="anker" id="stufe-9-1"></span>

Primero se aplica a un vector $\mathbf{x}\in\mathbb{R}^k$ una matriz $\mathbf{B}\in\mathbb{R}^{n\times k}$, y después, al resultado $\mathbf{B}\mathbf{x}\in\mathbb{R}^n$, una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ (fig. [33](#abb-33)). La composición $\mathbf{x}\mapsto\mathbf{A}(\mathbf{B}\mathbf{x})$ es lineal, pues cada una de las dos etapas conserva sumas y múltiplos. Según el teorema de la subsección [8.2](lineare-abbildungen.html#stufe-8-2), tiene, por tanto, una matriz. Su columna $l$ es la imagen de $\mathbf{e}_l$: la primera etapa lo convierte en la columna $\mathbf{B}\mathbf{e}_l$ de $\mathbf{B}$; la segunda etapa multiplica esta columna por $\mathbf{A}$.

:::abbildung ml/k1hinter 33
Arriba, dos aplicaciones lineales una tras otra: primero $\mathbf{B}$, después $\mathbf{A}$. Abajo, la misma aplicación en un solo paso, con la única matriz $\mathbf{A}\mathbf{B}$. El producto de matrices está definido exactamente de modo que ambos caminos den el mismo resultado.
:::

:::definition Definición 9.1 (Producto de matrices)
<span class="anker" id="satz-9-1"></span>

Para $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{B}\in\mathbb{R}^{n\times k}$, el __producto de matrices__ $\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times k}$ es la matriz con las entradas

<span class="anker" id="gl-9-1"></span>
$$(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^{n}a_{ij}\,b_{jl},\qquad i=1,\dots,m,\quad l=1,\dots,k . \tag{9.1}$$
:::

La entrada $(i,l)$ es el producto escalar de la fila $i$ de $\mathbf{A}$ por la columna $l$ de $\mathbf{B}$. El producto solo está definido si $\mathbf{A}$ tiene tantas columnas como filas tiene $\mathbf{B}$: los tamaños «interiores» deben coincidir, $(m\times n)\cdot(n\times k)$, y el resultado tiene los tamaños «exteriores», $m\times k$.

:::satz Teorema 9.2 (El producto es la composición)
<span class="anker" id="satz-9-2"></span>

Para todo $\mathbf{x}\in\mathbb{R}^k$ se cumple $(\mathbf{A}\mathbf{B})\,\mathbf{x}=\mathbf{A}\,(\mathbf{B}\mathbf{x})$.
:::

:::herleitung Composición
La componente $i$ del lado izquierdo es, según [(7.1)](das-matrix-vektor-produkt.html#gl-7-1) y [(9.1)](#gl-9-1),

$$\sum_{l=1}^k(\mathbf{A}\mathbf{B})_{il}\,x_l=\sum_{l=1}^k\sum_{j=1}^na_{ij}\,b_{jl}\,x_l=\sum_{j=1}^na_{ij}\Bigl(\sum_{l=1}^kb_{jl}\,x_l\Bigr)=\sum_{j=1}^na_{ij}\,(\mathbf{B}\mathbf{x})_j ,$$

y esa es la componente $i$ de $\mathbf{A}(\mathbf{B}\mathbf{x})$. En el paso intermedio se han intercambiado las dos sumas y se ha sacado $a_{ij}$ delante de la suma interior.
:::

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ y $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ se tiene

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$

Cada una de las cuatro entradas es una suma según [(9.1)](#gl-9-1) (fig. [34](#abb-34)).

:::abbildung ml/k1rprodukt 34
El producto de matrices entrada por entrada: la entrada $(i,l)$ es la fila $i$ de $\mathbf{A}$ por la columna $l$ de $\mathbf{B}$.
:::

Comprobación con $\mathbf{x}=(1,\,2)^{\top}$: $\mathbf{B}\mathbf{x}=(2,\,1)^{\top}$, luego $\mathbf{A}(\mathbf{B}\mathbf{x})=(4,\,1)^{\top}$; y directamente, $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+2,\ 1+0)^{\top}=(4,\,1)^{\top}$.

⁠**En resumen:** El producto de matrices $\mathbf{A}\mathbf{B}$ es la matriz de la aplicación «primero $\mathbf{B}$, después $\mathbf{A}$»; su entrada $(i,l)$ es la fila $i$ de $\mathbf{A}$ por la columna $l$ de $\mathbf{B}$.

:::hintergrund Por qué el producto de matrices se define precisamente así
La fórmula [(9.1)](#gl-9-1) parece arbitraria a primera vista. Más natural sería multiplicar las matrices entrada por entrada. Pero el producto de matrices no es una invención libre, sino que está fijado por una exigencia: debe ser la matriz de la composición. Esta matriz es única según el teorema de la subsección [8.2](lineare-abbildungen.html#stufe-8-2), y su columna $l$ tiene que ser la imagen de $\mathbf{e}_l$ bajo ambas aplicaciones, es decir, $\mathbf{A}$ por la columna $l$ de $\mathbf{B}$. Si se escribe esto componente por componente, sale exactamente [(9.1)](#gl-9-1). Un producto entrada por entrada no tendría un significado así: no describe la composición de dos aplicaciones.
:::

### Muchos vectores a la vez

<span class="anker" id="stufe-9-2"></span>

Según la deducción del producto, la columna $l$ de $\mathbf{A}\mathbf{B}$ es el producto de $\mathbf{A}$ por la columna $l$ de $\mathbf{B}$. Un producto de matrices puede leerse, por tanto, como varios productos matriz-vector uno al lado de otro:

<span class="anker" id="gl-9-2"></span>
$$\mathbf{A}\begin{pmatrix}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{B}\mathbf{e}_k\end{pmatrix}=\begin{pmatrix}\mathbf{A}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{A}\mathbf{B}\mathbf{e}_k\end{pmatrix}. \tag{9.2}$$

Del mismo modo, la fila $i$ de $\mathbf{A}\mathbf{B}$ es la fila $i$ de $\mathbf{A}$ multiplicada por $\mathbf{B}$.

Para los datos, esto significa: si se quieren aplicar varias sumas ponderadas a todos los ejemplos, se escriben los vectores de pesos uno al lado de otro como columnas de una matriz $\mathbf{W}$. El producto $\mathbf{X}\mathbf{W}$ contiene entonces en la columna $l$ las predicciones con el $l$-ésimo vector de pesos.

⁠**Ejemplo numérico:** Además del precio de compra con $\mathbf{w}=(3,\,10,\,-4)^{\top}$ (miles de euros), se quiere estimar el alquiler mensual con los pesos $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ (euros). Con $\mathbf{W}=\begin{pmatrix}\mathbf{w}&\mathbf{w}_{\mathrm M}\end{pmatrix}\in\mathbb{R}^{3\times2}$ se tiene

$$\mathbf{X}\mathbf{W}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3&12\\10&30\\-4&-8\end{pmatrix}=\begin{pmatrix}188&756\\126&502\\286&1152\\232&914\end{pmatrix}.$$

La fila $i$ contiene ambas estimaciones para la vivienda $i$; la columna $1$, todos los precios de compra; la columna $2$, todos los alquileres.

⁠**En resumen:** Las columnas de $\mathbf{A}\mathbf{B}$ son $\mathbf{A}$ por las columnas de $\mathbf{B}$; $\mathbf{X}\mathbf{W}$ aplica varias sumas ponderadas a todos los ejemplos a la vez.

### Reglas de cálculo: el orden importa

<span class="anker" id="stufe-9-3"></span>

Para los números, $2\cdot3=3\cdot2$. Para las matrices no es así, y la razón es intuitiva: primero girar y luego estirar es algo distinto de primero estirar y luego girar (fig. [35](#abb-35)).

:::abbildung ml/k1reihenfolge 35
El cuadrado unidad con $\mathbf{e}_1$ (rojo) y $\mathbf{e}_2$ (verde) y, a su lado, sus imágenes bajo $\mathbf{S}\mathbf R$ y $\mathbf R\mathbf{S}$. Aquí $\mathbf R$ es la rotación de $90^\circ$ y $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ el estiramiento. El orden decide si el rectángulo se alarga en horizontal o en vertical.
:::

:::satz Teorema 9.3 (Reglas de cálculo del producto de matrices)
<span class="anker" id="satz-9-3"></span>

Para matrices de tamaños adecuados y escalares $c$ se cumple:

<ol class="rm">

<li>

$(\mathbf{A}\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\mathbf{C})$ (asociativo);

</li>

<li>

$\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}$ y $(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}$ (distributivo);

</li>

<li>

$c\,(\mathbf{A}\mathbf{B})=(c\,\mathbf{A})\mathbf{B}=\mathbf{A}(c\,\mathbf{B})$.

</li>

</ol>

En general, sin embargo, $\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}$: el producto de matrices *no* es conmutativo.
:::

La regla (i) se deduce del significado: ambos lados son la matriz de la aplicación «primero $\mathbf{C}$, después $\mathbf{B}$, después $\mathbf{A}$», pues $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{x})=\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{x}))=\mathbf{A}((\mathbf{B}\mathbf{C})\mathbf{x})$ para todo $\mathbf{x}$. Las reglas (ii) y (iii) se comprueban entrada por entrada con [(9.1)](#gl-9-1) y las reglas de las sumas.

⁠**Ejemplo numérico 1:** Con la rotación $\mathbf R=\mathbf R_{90^\circ}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ y el estiramiento $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ se tiene

$$\mathbf{S}\mathbf R=\begin{pmatrix}0&-2\\0{,}5&0\end{pmatrix},\qquad \mathbf R\mathbf{S}=\begin{pmatrix}0&-0{,}5\\2&0\end{pmatrix}.$$

Primero girar y luego estirar lleva $\mathbf{e}_1$ a $(0;\,0{,}5)^{\top}$; primero estirar y luego girar, a $(0,\,2)^{\top}$.

⁠**Ejemplo numérico 2:** De la subsección [9.1](#stufe-9-1) se tiene $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$, pero $\mathbf{B}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$. Con tamaños distintos es aún más claro: para $\mathbf{A}\in\mathbb{R}^{2\times3}$ y $\mathbf{B}\in\mathbb{R}^{3\times2}$, $\mathbf{A}\mathbf{B}$ es una matriz $2\times2$ y $\mathbf{B}\mathbf{A}$ una matriz $3\times3$.

⁠**En resumen:** En el producto de matrices se pueden mover los paréntesis y desarrollar los productos, pero no intercambiar el orden.

:::hintergrund Por qué la colocación de los paréntesis ahorra tiempo de cálculo
Según la regla (i), $(\mathbf{A}\mathbf{B})\mathbf{x}=\mathbf{A}(\mathbf{B}\mathbf{x})$. El resultado es el mismo; el trabajo, no. Para dos matrices $n\times n$, el producto $\mathbf{A}\mathbf{B}$ necesita, para cada una de las $n^2$ entradas, $n$ multiplicaciones y $n-1$ sumas, en total unas $2n^3$ operaciones aritméticas básicas; después, $(\mathbf{A}\mathbf{B})\mathbf{x}$ cuesta todavía unas $2n^2$. El camino $\mathbf{A}(\mathbf{B}\mathbf{x})$ consta de dos productos matriz-vector de unas $2n^2$ cada uno. Para $n=1000$, son unos $2\cdot10^9$ frente a $4\cdot10^6$ operaciones aritméticas básicas, una diferencia de un factor $500$. Por eso, quien aplica una larga cadena de matrices a un vector calcula de derecha a izquierda y nunca forma la matriz producto.
:::

### Dos etapas lineales son una sola

<span class="anker" id="stufe-9-4"></span>

Si se conectan varias etapas de cálculo lineales una tras otra, no surge ningún tipo nuevo de aplicación. Según la subsección [9.1](#stufe-9-1), esto es evidente, pero merece un teorema propio, porque marca los límites de las reglas lineales.

:::satz Teorema 9.4 (Aplicaciones lineales en serie)
<span class="anker" id="satz-9-4"></span>

Si $f(\mathbf{x})=\mathbf{B}\mathbf{x}$ y $g(\mathbf{u})=\mathbf{A}\mathbf{u}$ son lineales, la composición $\mathbf{x}\mapsto g(f(\mathbf{x}))$ vuelve a ser lineal, y además con la única matriz $\mathbf{A}\mathbf{B}$. Lo mismo vale para toda cadena finita de etapas lineales.
:::

Por muchas etapas lineales que se conecten en serie, el resultado siempre puede calcularse con una única matriz en un solo paso. Todo lo que puede hacer una cadena de etapas lineales lo puede hacer ya, por tanto, una sola matriz. De la teoría de señales y sistemas se conoce lo mismo: dos sistemas lineales en cadena forman juntos de nuevo un sistema lineal.

⁠**Ejemplo numérico:** Una primera etapa convierte tres números en dos, $\mathbf{B}=\bigl(\begin{smallmatrix}1&2&0\\0&1&-1\end{smallmatrix}\bigr)$; una segunda convierte dos números de nuevo en tres, $\mathbf{A}=\Bigl(\begin{smallmatrix}2&1\\1&-1\\0&3\end{smallmatrix}\Bigr)$. Juntas son la única matriz

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&5&-1\\1&1&1\\0&3&-3\end{pmatrix}.$$

Comprobación con $\mathbf{x}=(1,\,1,\,1)^{\top}$: $\mathbf{B}\mathbf{x}=(3,\,0)^{\top}$ y $\mathbf{A}(3,\,0)^{\top}=(6,\,3,\,0)^{\top}$; igualmente, $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+5-1,\ 1+1+1,\ 0+3-3)^{\top}=(6,\,3,\,0)^{\top}$.

⁠**En resumen:** Varias etapas lineales en serie son juntas una única aplicación lineal; su matriz es el producto de las matrices individuales.

### El producto exterior

<span class="anker" id="stufe-9-5"></span>

El producto escalar $\mathbf{u}^{\top}\mathbf{v}$ es «fila por columna» y da un número. Si se invierte el orden, «columna por fila», según [(9.1)](#gl-9-1) sale una matriz entera: la tabla de todos los productos de una componente de un vector por una componente del otro, como una tabla de multiplicar.

:::definition Definición 9.5 (Producto exterior)
<span class="anker" id="satz-9-5"></span>

Para $\mathbf{u}\in\mathbb{R}^m$ y $\mathbf{v}\in\mathbb{R}^n$, el __producto exterior__ $\mathbf{u}\mathbf{v}^{\top}\in\mathbb{R}^{m\times n}$ es la matriz con las entradas

<span class="anker" id="gl-9-3"></span>
$$(\mathbf{u}\mathbf{v}^{\top})_{ij}=u_i\,v_j . \tag{9.3}$$
:::

Es el producto de matrices de una matriz $m\times1$ por una matriz $1\times n$. Cada columna es un múltiplo de $\mathbf{u}$, en concreto $v_j\,\mathbf{u}$, y cada fila, un múltiplo de $\mathbf{v}^{\top}$.

⁠**Ejemplo numérico:**

$$\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}4&5\end{pmatrix}=\begin{pmatrix}4&5\\8&10\\12&15\end{pmatrix}.$$

Con el producto exterior, todo producto de matrices puede escribirse como suma: «columna $j$ de $\mathbf{A}$ por fila $j$ de $\mathbf{B}$», sumado sobre $j$,

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}\mathbf{B}=\sum_{j=1}^n\mathbf{a}_j\,\bigl(\text{fila $j$ de }\mathbf{B}\bigr) . \tag{9.4}$$

La entrada $(i,l)$ del lado derecho es $\sum_ja_{ij}\,b_{jl}$, exactamente como en [(9.1)](#gl-9-1). Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ y $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ de la subsección [9.1](#stufe-9-1), la suma de dos productos exteriores vuelve a dar $\mathbf{A}\mathbf{B}$ (fig. [36](#abb-36)).

:::abbildung ml/k1raeusser 36
El producto de matrices como suma de productos exteriores: columna $j$ de $\mathbf{A}$ por fila $j$ de $\mathbf{B}$, sumado sobre $j=1,2$.
:::

⁠**En resumen:** El producto exterior $\mathbf{u}\mathbf{v}^{\top}$ es la tabla de todos los productos $u_iv_j$; todo producto de matrices es una suma de tales tablas.

:::aufgabe Ejercicio 21 ★ Productos y tamaños
<span class="anker" id="aufg-21"></span>

<ol class="al">

<li>

Calcula $\mathbf{C}\mathbf{D}$ y $\mathbf{D}\mathbf{C}$ para $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ y $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$.

</li>

<li>

Sean $\mathbf{A}\in\mathbb{R}^{2\times3}$, $\mathbf{B}\in\mathbb{R}^{3\times4}$ y $\mathbf{x}\in\mathbb{R}^4$. ¿Cuáles de las expresiones $\mathbf{A}\mathbf{B}$, $\mathbf{B}\mathbf{A}$, $\mathbf{A}\mathbf{B}\mathbf{x}$, $\mathbf{B}\mathbf{x}\mathbf{A}$ están definidas y qué tamaño tiene el resultado?

</li>

<li>

Calcula el producto exterior $(1,\,-1)^{\top}(2,\,0,\,3)$ y comprueba que cada fila es un múltiplo de $(2,\,0,\,3)$.

</li>

</ol>

:::loesung
(a) $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot1\\3\cdot0+4\cdot1&3\cdot1+4\cdot1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ y $\mathbf{D}\mathbf{C}=\bigl(\begin{smallmatrix}0+3&0+4\\1+3&2+4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$. Los dos productos son distintos.

(b) $\mathbf{A}\mathbf{B}$: $(2\times3)\cdot(3\times4)$ encaja, tamaño $2\times4$. $\mathbf{B}\mathbf{A}$: $(3\times4)\cdot(2\times3)$, los tamaños interiores no coinciden, $4\ne2$; no está definido. $\mathbf{A}\mathbf{B}\mathbf{x}$: $(2\times4)\cdot(4\times1)$ encaja, un vector de $\mathbb{R}^2$. $\mathbf{B}\mathbf{x}\mathbf{A}$: $\mathbf{B}\mathbf{x}$ tiene el tamaño $3\times1$, y $(3\times1)\cdot(2\times3)$ no encaja, los interiores no coinciden, $1\ne2$; no está definido.

(c) $(1,\,-1)^{\top}(2,\,0,\,3)=\bigl(\begin{smallmatrix}2&0&3\\-2&0&-3\end{smallmatrix}\bigr)$. La primera fila es $1\cdot(2,0,3)$; la segunda, $-1\cdot(2,0,3)$.
:::
:::

:::aufgabe Ejercicio 22 ★★ Dos rotaciones
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

Calcula $\mathbf R_\alpha\mathbf R_\beta$ con [(8.3)](lineare-abbildungen.html#gl-8-3). ¿Qué rotación es? ¿Qué dos fórmulas de trigonometría obtienes de paso?

</li>

<li>

Calcula $\mathbf R_{90^\circ}^2=\mathbf R_{90^\circ}\mathbf R_{90^\circ}$ y $\mathbf R_{90^\circ}^4$ e interpreta los resultados geométricamente.

</li>

<li>

¿Es $\mathbf R_\alpha\mathbf R_\beta=\mathbf R_\beta\mathbf R_\alpha$? ¿Por qué no contradice esto la regla de que las matrices no conmutan?

</li>

</ol>

:::loesung
(a) Al multiplicar se obtiene

$$\mathbf R_\alpha\mathbf R_\beta=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}.$$

Geométricamente, esto es «primero girar $\beta$, luego $\alpha$», es decir, la rotación de $\alpha+\beta$, cuya matriz es, según [(8.3)](lineare-abbildungen.html#gl-8-3), $\mathbf R_{\alpha+\beta}$. Si se comparan las entradas, se obtienen las fórmulas de adición $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ y $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$. El producto de matrices las proporciona sin necesidad de sabérselas de memoria.

(b) $\mathbf R_{90^\circ}^2=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-1&0\\0&-1\end{smallmatrix}\bigr)=-\mathbf{I}$: dos giros de $90^\circ$ son media vuelta, y cada punto pasa a su simétrico respecto del origen. $\mathbf R_{90^\circ}^4=(-\mathbf{I})(-\mathbf{I})=\mathbf{I}$: cuatro cuartos de vuelta son una vuelta completa.

(c) Sí: ambos productos son $\mathbf R_{\alpha+\beta}=\mathbf R_{\beta+\alpha}$, pues las rotaciones del plano alrededor del mismo punto pueden realizarse en cualquier orden. «No conmutativo» solo significa que $\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}$ *no siempre* se cumple. Para ciertos pares, por ejemplo dos rotaciones del plano o dos matrices diagonales, puede cumplirse de todos modos.
:::
:::

:::aufgabe Ejercicio 23 ★★ El paréntesis correcto
<span class="anker" id="aufg-23"></span>

Sean $\mathbf{A}\in\mathbb{R}^{100\times1000}$, $\mathbf{B}\in\mathbb{R}^{1000\times1000}$ y $\mathbf{x}\in\mathbb{R}^{1000}$. Estima el número de operaciones aritméticas básicas para $(\mathbf{A}\mathbf{B})\mathbf{x}$ y para $\mathbf{A}(\mathbf{B}\mathbf{x})$. Cuenta para ello unas $2mnk$ operaciones por cada producto de una matriz $m\times n$ por una matriz $n\times k$.

:::loesung
$(\mathbf{A}\mathbf{B})\mathbf{x}$: el producto $\mathbf{A}\mathbf{B}$ de una matriz $100\times1000$ por una matriz $1000\times1000$ cuesta unas $2\cdot100\cdot1000\cdot1000=2\cdot10^8$ operaciones, y después $(\mathbf{A}\mathbf{B})\mathbf{x}$, unas $2\cdot100\cdot1000=2\cdot10^5$ más; en total, unos $200{,}2$ millones. $\mathbf{A}(\mathbf{B}\mathbf{x})$: $\mathbf{B}\mathbf{x}$ cuesta unas $2\cdot1000\cdot1000=2\cdot10^6$, y después $\mathbf{A}(\mathbf{B}\mathbf{x})$, unas $2\cdot10^5$; en total, unos $2{,}2$ millones. El segundo camino es unas $91$ veces más rápido, con el mismo resultado.
:::
:::
