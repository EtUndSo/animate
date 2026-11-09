---
title: Proyección sobre un subespacio
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15220500
summary: La sección anterior encontró el punto más cercano de un espacio columna.
tags: subespacio, matriz de proyección, complemento ortogonal, proceso de Gram-Schmidt, descomposición QR
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
La sección anterior encontró el punto más cercano de un espacio columna. Esta sección expresa el resultado como una matriz, muestra que todo se vuelve especialmente sencillo cuando las columnas son ortonormales y presenta un procedimiento que convierte columnas independientes cualesquiera en columnas ortonormales. Con él puede calcularse la mejor solución aproximada sin formar $\mathbf{A}^{\top}\mathbf{A}$.
:::

### Subespacios

<span class="anker" id="stufe-4-1"></span>

Las rectas y los planos que pasan por el origen, los espacios columna y los núcleos tienen una propiedad común: si contienen dos vectores, contienen también toda combinación lineal de ambos. Sumando y multiplicando por números nunca se sale de ellos. Para tales conjuntos hay una palabra propia.

:::definition Definición 4.1 (Subespacio)
<span class="anker" id="satz-4-1"></span>

Un conjunto $\mathcal U\subseteq\mathbb{R}^n$ se llama __subespacio__ de $\mathbb{R}^n$ si es el espacio generado por un número finito de vectores.
:::

De forma equivalente: $\mathcal U$ contiene el vector nulo, y si dos vectores $\mathbf{u},\mathbf{v}$ están en $\mathcal U$, también lo están $\mathbf{u}+\mathbf{v}$ y todo múltiplo $c\,\mathbf{u}$. Todo subespacio tiene una base y, por tanto, según [Fundamentos 1, sección 13.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), una dimensión.

::::beispiel [Ejemplo numérico]
En $\mathbb{R}^3$ son subespacios: el origen solo, de dimensión $0$; toda recta que pasa por el origen, de dimensión $1$; todo plano que pasa por el origen, como el espacio columna de $\mathbf{H}$ de la sección anterior, de dimensión $2$; y todo $\mathbb{R}^3$. El núcleo de una matriz es un subespacio, y el espacio columna también. Una recta que no pasa por el origen no es un subespacio, pues no contiene el vector nulo.
::::

⁠**En resumen:** Un subespacio es un espacio generado por vectores; sumando y multiplicando por números no se sale de él.

### La matriz de proyección de un espacio columna

<span class="anker" id="stufe-4-2"></span>

Con columnas linealmente independientes, [(3.5)](die-beste-naherungslosung.html#gl-3-5) da el punto más cercano $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$. La matriz delante de $\mathbf{y}$ solo depende de $\mathbf{A}$. Hace para el espacio columna lo que $\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ hacía para una recta.

:::definition Definición 4.2 (Matriz de proyección de un espacio columna)
<span class="anker" id="satz-4-2"></span>

Si $\mathbf{A}$ tiene columnas linealmente independientes,

<span class="anker" id="gl-4-1"></span>
$$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{4.1}$$

se llama __matriz de proyección__ sobre el espacio columna de $\mathbf{A}$.
:::

:::satz Teorema 4.3 (Propiedades)
<span class="anker" id="satz-4-3"></span>

Se cumple $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$, $\mathbf{P}^{\top}=\mathbf{P}$, $\mathbf{P}^2=\mathbf{P}$ y $\mathbf{P}\mathbf{A}=\mathbf{A}$. Por tanto, $\mathbf{P}$ es la proyección ortogonal sobre el espacio columna.
:::

:::beweis Propiedades
La primera ecuación es la deducción de arriba. Con las reglas de cálculo de [Fundamentos 1, secciones 10.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1) y [11.4](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-4), se tiene $\mathbf{P}^{\top}=\mathbf{A}\bigl((\mathbf{A}^{\top}\mathbf{A})^{-1}\bigr)^{\top}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$, pues $\mathbf{A}^{\top}\mathbf{A}$ es simétrica y, con ella, también su inversa. Además, $\mathbf{P}\mathbf{A}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}(\mathbf{A}^{\top}\mathbf{A})=\mathbf{A}$, y de ahí $\mathbf{P}^2=\mathbf{P}\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$. Según el teorema de la sección [2.4](projektion-auf-eine-gerade.html#stufe-2-4), una proyección simétrica es ortogonal.
:::

La ecuación $\mathbf{P}\mathbf{A}=\mathbf{A}$ dice que cada columna y, con ello, cada vector del espacio columna se queda donde está al proyectar.

::::beispiel [Ejemplo numérico]
Para $\mathbf{H}$ se tiene

$$\mathbf{P}=\mathbf{H}\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf{H}^{\top}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

Comprobación: $\mathbf{P}(1,\,1,\,1)^{\top}=\tfrac13(2,\,2,\,4)^{\top}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}=\hat{\mathbf{y}}$, y $\mathbf{P}\mathbf{a}_1=\tfrac13(2+1,\ -1+1,\ 1+2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_1$.
::::

⁠**En resumen:** La matriz de proyección $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ transforma cada vector en el punto más cercano del espacio columna; es simétrica y cumple $\mathbf{P}^2=\mathbf{P}$.

### Columnas ortonormales

<span class="anker" id="stufe-4-3"></span>

La fórmula [(4.1)](#gl-4-1) contiene una inversa. Esta desaparece cuando las columnas son ortonormales, pues entonces $\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. Para una matriz $\mathbf{Q}$ con columnas ortonormales, la mejor solución aproximada es, por ello, simplemente $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$: sus componentes son las longitudes de las sombras $\mathbf{q}_i^{\top}\mathbf{y}$.

:::satz Teorema 4.4 (Proyección con columnas ortonormales)
<span class="anker" id="satz-4-4"></span>

Si $\mathbf{Q}\in\mathbb{R}^{n\times k}$ tiene columnas ortonormales $\mathbf{q}_1,\dots,\mathbf{q}_k$, la matriz de proyección sobre su espacio columna es

<span class="anker" id="gl-4-2"></span>
$$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}=\sum_{i=1}^k\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{4.2}$$
:::

La forma de suma se deduce de [Fundamentos 1, sección 9.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5): un producto de matrices es la suma de los productos exteriores de columnas y filas. Cada sumando $\mathbf{q}_i\mathbf{q}_i^{\top}$ es la matriz de proyección sobre la recta en la dirección de $\mathbf{q}_i$. Con columnas ortonormales, la proyección sobre el espacio columna es, por tanto, la suma de las proyecciones sobre los ejes individuales. Esto explica a posteriori la última subsección de la sección [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1): $\mathbf{Q}\mathbf{Q}^{\top}$ no es la matriz identidad, sino la proyección sobre el espacio columna de $\mathbf{Q}$. Lo que es perpendicular a él lo desecha.

::::beispiel [Ejemplo numérico]
Los vectores $\mathbf{q}_1=\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}$ y $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ son ortonormales: $\lVert\mathbf{q}_1\rVert^2=\tfrac22$, $\lVert\mathbf{q}_2\rVert^2=\tfrac66$, $\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac{-1+0+1}{\sqrt{12}}=0$. En ambos, la tercera componente es la suma de las dos primeras; forman una base ortonormal del plano de $\mathbf{H}$. Se tiene

$$\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}=\frac12\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}+\frac16\begin{pmatrix}1&-2&-1\\-2&4&2\\-1&2&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix},$$

la misma matriz que en la subsección anterior, esta vez sin inversa.
::::

⁠**En resumen:** Con columnas ortonormales, $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ y $\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}$, la suma de las proyecciones sobre las columnas individuales.

### El complemento ortogonal

<span class="anker" id="stufe-4-4"></span>

Si se proyecta $\mathbf{y}$ sobre un subespacio, queda el residuo $\mathbf{y}-\mathbf{P}\mathbf{y}$. Es perpendicular a todo el subespacio. Todos los vectores con esta propiedad forman a su vez un subespacio, y $\mathbf{y}$ se descompone en una parte en uno de ellos y otra en el otro.

:::definition Definición 4.5 (Complemento ortogonal)
<span class="anker" id="satz-4-5"></span>

El __complemento ortogonal__ de un subespacio $\mathcal U\subseteq\mathbb{R}^n$ es el conjunto

<span class="anker" id="gl-4-3"></span>
$$\mathcal U^\perp=\{\mathbf{z}\in\mathbb{R}^n:\ \mathbf{z}^{\top}\mathbf{u}=0\ \text{para todo}\ \mathbf{u}\in\mathcal U\} . \tag{4.3}$$
:::

El símbolo $\mathcal U^\perp$ se lee «$\mathcal U$ perpendicular». Si $\mathcal U$ es el espacio columna de $\mathbf{A}$, $\mathbf{z}$ es perpendicular a $\mathcal U$ si y solo si $\mathbf{A}^{\top}\mathbf{z}=\mathbf{0}$; el complemento ortogonal es, por tanto, el núcleo de $\mathbf{A}^{\top}$.

:::satz Teorema 4.6 (Descomposición en dos partes perpendiculares)
<span class="anker" id="satz-4-6"></span>

Si $\mathbf{P}$ es la proyección ortogonal sobre un subespacio $\mathcal U$ de $\mathbb{R}^n$, se cumple:

<ol class="rm">

<li>

Todo vector $\mathbf{y}$ es, de manera única, la suma $\mathbf{y}=\mathbf{u}+\mathbf{z}$ con $\mathbf{u}\in\mathcal U$ y $\mathbf{z}\in\mathcal U^\perp$, a saber, $\mathbf{u}=\mathbf{P}\mathbf{y}$ y $\mathbf{z}=(\mathbf{I}-\mathbf{P})\mathbf{y}$.

</li>

<li>

$\mathbf{I}-\mathbf{P}$ es la proyección ortogonal sobre $\mathcal U^\perp$.

</li>

<li>

$\dim\mathcal U^\perp=n-\dim\mathcal U$.

</li>

</ol>
:::

:::beweis Descomposición
(i) Que $\mathbf{P}\mathbf{y}$ está en $\mathcal U$ y que $\mathbf{y}-\mathbf{P}\mathbf{y}$ es perpendicular a $\mathcal U$ es la definición de la proyección ortogonal. Si hubiera una segunda descomposición $\mathbf{y}=\mathbf{u}'+\mathbf{z}'$, $\mathbf{u}-\mathbf{u}'=\mathbf{z}'-\mathbf{z}$ sería un vector que está en $\mathcal U$ y a la vez es perpendicular a $\mathcal U$, es decir, perpendicular a sí mismo. Entonces el cuadrado de su longitud es cero y, por tanto, es el vector nulo. (ii) $\mathbf{I}-\mathbf{P}$ es simétrica, y $(\mathbf{I}-\mathbf{P})^2=\mathbf{I}-2\mathbf{P}+\mathbf{P}^2=\mathbf{I}-\mathbf{P}$. Su imagen está, según (i), en $\mathcal U^\perp$. Todo $\mathbf{z}\in\mathcal U^\perp$ queda fijo: $\mathbf{P}\mathbf{z}$ está en $\mathcal U$ y es a la vez la diferencia $\mathbf{z}-(\mathbf{z}-\mathbf{P}\mathbf{z})$ de dos vectores perpendiculares a $\mathcal U$; por tanto, $\mathbf{P}\mathbf{z}$ es perpendicular a sí mismo y es $\mathbf{0}$. (iii) Si se elige una base de $\mathcal U$ como columnas de una matriz $\mathbf{A}$, $\mathcal U^\perp$ es el núcleo de $\mathbf{A}^{\top}$. Según el teorema del rango de [Fundamentos 1, sección 13.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), tiene dimensión $n-\operatorname{rango}\mathbf{A}^{\top}=n-\operatorname{rango}\mathbf{A}=n-\dim\mathcal U$.
:::

::::beispiel [Ejemplo numérico]
El plano de $\mathbf{H}$ tiene dimensión $2$; su complemento ortogonal en $\mathbb{R}^3$ tiene, por tanto, dimensión $1$: la recta en la dirección del vector normal $\mathbf{k}=(1,\,1,\,-1)^{\top}$. En efecto, $\mathbf{H}^{\top}\mathbf{k}=(1-1,\ 1-1)^{\top}=\mathbf{0}$. Se tiene

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&1&-1\\1&1&-1\\-1&-1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}},$$

la proyección sobre esta recta. Para $\mathbf{y}=(1,\,1,\,1)^{\top}$ es $(\mathbf{I}-\mathbf{P})\mathbf{y}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$, el residuo de la sección anterior.
::::

⁠**En resumen:** El complemento ortogonal $\mathcal U^\perp$ contiene todos los vectores perpendiculares a $\mathcal U$; cada vector se descompone de manera única en una parte en $\mathcal U$ y otra en $\mathcal U^\perp$, y las dimensiones suman $n$.

### El proceso de Gram-Schmidt

<span class="anker" id="stufe-4-5"></span>

Las columnas ortonormales lo simplifican todo, pero lo que suele darse son columnas cualesquiera. El proceso de Gram-Schmidt construye, a partir de vectores linealmente independientes $\mathbf{a}_1,\dots,\mathbf{a}_k$, vectores ortonormales $\mathbf{q}_1,\dots,\mathbf{q}_k$ que generan el mismo subespacio.

La idea la muestra la fig. [11](#abb-11) para dos vectores. Se normaliza el primero. Al segundo se le resta su sombra sobre el primero, es decir, su proyección. Lo que queda es perpendicular al primero, y se normaliza. Al tercer vector se le restan las sombras sobre los dos ya hallados, y así sucesivamente.

:::abbildung ml/k2gramschmidt 11
El proceso de Gram-Schmidt para $\mathbf{a}_1=(2,1)^{\top}$ y $\mathbf{a}_2=(1,2)^{\top}$. Primero se normaliza $\mathbf{a}_1$: $\mathbf{q}_1=\mathbf{a}_1/\sqrt5$. Al segundo vector se le resta su sombra $(\mathbf{q}_1^{\top}\mathbf{a}_2)\,\mathbf{q}_1=(1{,}6;\,0{,}8)^{\top}$ (azul). El resto $\tilde{\mathbf{q}}_2=(-0{,}6;\,1{,}2)^{\top}$ (naranja, paralelo a la perpendicular a trazos) es perpendicular a $\mathbf{q}_1$; normalizado da $\mathbf{q}_2=(-1,2)^{\top}/\sqrt5$.
:::

:::definition Definición 4.7 (Proceso de Gram-Schmidt)
<span class="anker" id="satz-4-7"></span>

Se dan vectores linealmente independientes $\mathbf{a}_1,\dots,\mathbf{a}_k\in\mathbb{R}^n$. El __proceso de Gram-Schmidt__ calcula sucesivamente, para $i=1,\dots,k$,

<span class="anker" id="gl-4-4"></span>
$$\tilde{\mathbf{q}}_i=\mathbf{a}_i-\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l,\qquad \mathbf{q}_i=\frac{\tilde{\mathbf{q}}_i}{\lVert\tilde{\mathbf{q}}_i\rVert} . \tag{4.4}$$
:::

Para $i=1$ la suma es vacía, es decir, $\tilde{\mathbf{q}}_1=\mathbf{a}_1$. La suma es la proyección de $\mathbf{a}_i$ sobre el espacio generado por los vectores ya hallados, según [(4.2)](#gl-4-2); $\tilde{\mathbf{q}}_i$ es el residuo de esta proyección.

:::satz Teorema 4.8 (Lo que da Gram-Schmidt)
<span class="anker" id="satz-4-8"></span>

Los vectores $\mathbf{q}_1,\dots,\mathbf{q}_k$ son ortonormales, y para cada $i$ los vectores $\mathbf{q}_1,\dots,\mathbf{q}_i$ generan el mismo subespacio que $\mathbf{a}_1,\dots,\mathbf{a}_i$.
:::

:::beweis Gram-Schmidt
Se procede paso a paso. Supongamos que $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ ya son ortonormales y generan el mismo subespacio que $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$. Entonces $\tilde{\mathbf{q}}_i$ es el residuo de la proyección de $\mathbf{a}_i$ sobre este subespacio y es, por ello, perpendicular a $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$; calculado directamente, $\mathbf{q}_l^{\top}\tilde{\mathbf{q}}_i=\mathbf{q}_l^{\top}\mathbf{a}_i-\mathbf{q}_l^{\top}\mathbf{a}_i=0$. Además, $\tilde{\mathbf{q}}_i\ne\mathbf{0}$, pues de lo contrario $\mathbf{a}_i$ sería una combinación lineal de $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ y, con ello, de $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$, en contradicción con la independencia. Por tanto, se puede normalizar. Finalmente, $\mathbf{a}_i=\tilde{\mathbf{q}}_i+\sum_l(\mathbf{q}_l^{\top}\mathbf{a}_i)\mathbf{q}_l$ es una combinación lineal de $\mathbf{q}_1,\dots,\mathbf{q}_i$ y, a la inversa, $\mathbf{q}_i$ es una combinación lineal de $\mathbf{a}_i$ y $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$. Ambas listas generan, por tanto, el mismo subespacio.
:::

Si los vectores dados son, a pesar de todo, dependientes, el proceso lo detecta por sí mismo: en algún momento es $\tilde{\mathbf{q}}_i=\mathbf{0}$, y no se puede normalizar.

::::beispiel [Ejemplo numérico]
Para las columnas de $\mathbf{H}$, $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ y $\mathbf{a}_2=(0,\,1,\,1)^{\top}$, es $\mathbf{q}_1=\mathbf{a}_1/\sqrt2$. Entonces $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ y

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\frac1{\sqrt2}\,\mathbf{q}_1=(0,\,1,\,1)^{\top}-\tfrac12(1,\,0,\,1)^{\top}=\bigl(-\tfrac12,\,1,\,\tfrac12\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{\tfrac14+1+\tfrac14}=\sqrt{\tfrac32} .$$

Normalizado es $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$, exactamente la base ortonormal del ejemplo numérico de [(4.2)](#gl-4-2). Las dos sumas de este ejemplo numérico las muestra la fig. [12](#abb-12).

:::abbildung ml/k2rgs 12
Gram-Schmidt para las columnas de $\mathbf{H}$: el producto escalar $\mathbf{q}_1^{\top}\mathbf{a}_2$ con $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ y $\mathbf{a}_2=(0,1,1)^{\top}$, que da la longitud de la sombra, y el cuadrado de la longitud del resto $\tilde{\mathbf{q}}_2=(-\tfrac12,1,\tfrac12)^{\top}$.
:::
::::

⁠**En resumen:** Gram-Schmidt resta a cada vector su proyección sobre los ya hallados y normaliza el resto; así se obtiene una base ortonormal del mismo subespacio.

:::hintergrund Coste y errores de redondeo
Para $k$ vectores de $n$ componentes cada uno, el proceso necesita unas $2nk^2$ operaciones aritméticas elementales: en el paso $i$ hay que calcular $i-1$ productos escalares y restar otros tantos múltiplos; cada uno cuesta unas $2n$ operaciones, y la suma sobre $i$ crece como $k^2$. Con números redondeados, la versión [(4.4)](#gl-4-4) es delicada: si dos de los vectores dados son casi paralelos, $\tilde{\mathbf{q}}_i$ es una pequeña diferencia de números grandes, y los $\mathbf{q}_i$ calculados dejan de ser exactamente ortogonales. Un orden ligeramente distinto de los pasos de cálculo, el proceso de Gram-Schmidt modificado, resta las sombras una a una del resto ya reducido, en lugar de restarlas todas del $\mathbf{a}_i$ original. Con números exactos da lo mismo; con números redondeados es claramente más preciso. Las bibliotecas de programas suelen usar todavía otros procedimientos, que trabajan con reflexiones, es decir, con matrices ortogonales.
:::

### La descomposición QR

<span class="anker" id="stufe-4-6"></span>

El proceso de Gram-Schmidt puede escribirse como una descomposición de una matriz. Según la demostración de arriba, cada vector $\mathbf{a}_i$ es una combinación lineal de $\mathbf{q}_1,\dots,\mathbf{q}_i$, en concreto

$$\mathbf{a}_i=\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l+\lVert\tilde{\mathbf{q}}_i\rVert\,\mathbf{q}_i .$$

En esta expresión solo aparecen los $i$ primeros vectores $\mathbf{q}_l$, no los posteriores. Por eso, si se escriben los coeficientes como columnas de una matriz, se obtiene una matriz triangular.

:::definition Definición 4.9 (Descomposición QR)
<span class="anker" id="satz-4-9"></span>

Si $\mathbf{A}\in\mathbb{R}^{m\times n}$ tiene columnas linealmente independientes, la __descomposición QR__ es la representación

<span class="anker" id="gl-4-5"></span>
$$\mathbf{A}=\mathbf{Q}\mathbf{R} \tag{4.5}$$

con una matriz $\mathbf{Q}\in\mathbb{R}^{m\times n}$ de columnas ortonormales y una matriz triangular superior $\mathbf{R}\in\mathbb{R}^{n\times n}$ con entradas diagonales positivas. Aquí, $r_{li}=\mathbf{q}_l^{\top}\mathbf{a}_i$ para $l<i$ y $r_{ii}=\lVert\tilde{\mathbf{q}}_i\rVert$.
:::

Una matriz triangular superior solo tiene ceros por debajo de la diagonal. La columna $i$ de $\mathbf{Q}\mathbf{R}$ es, según la visión por columnas, $\sum_lr_{li}\mathbf{q}_l$, es decir, exactamente la representación de $\mathbf{a}_i$ de arriba. Las columnas de $\mathbf{Q}$ las da el proceso de Gram-Schmidt, y las entradas de $\mathbf{R}$ se obtienen de paso. Como $\mathbf{Q}$ tiene columnas ortonormales, además $\mathbf{R}=\mathbf{Q}^{\top}\mathbf{A}$.

::::beispiel [Ejemplo numérico]
Para $\mathbf{H}$ se tiene

$$\mathbf{Q}=\begin{pmatrix}\tfrac1{\sqrt2}&-\tfrac1{\sqrt6}\\0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&\tfrac1{\sqrt2}\\0&\sqrt{\tfrac32}\end{pmatrix}\approx\begin{pmatrix}1{,}414&0{,}707\\0&1{,}225\end{pmatrix}.$$

Comprobación de la segunda columna: $\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}+\sqrt{\tfrac32}\cdot\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}=\tfrac12(1,\,0,\,1)^{\top}+\tfrac12(-1,\,2,\,1)^{\top}=(0,\,1,\,1)^{\top}=\mathbf{a}_2$.
::::

⁠**En resumen:** La descomposición QR $\mathbf{A}=\mathbf{Q}\mathbf{R}$ escribe el proceso de Gram-Schmidt como un producto de matrices: $\mathbf{Q}$ tiene columnas ortonormales y $\mathbf{R}$ es una matriz triangular superior.

### La mejor solución aproximada con QR

<span class="anker" id="stufe-4-7"></span>

Con la descomposición QR, las ecuaciones normales pueden resolverse sin calcular $\mathbf{A}^{\top}\mathbf{A}$. Se sustituye $\mathbf{A}=\mathbf{Q}\mathbf{R}$ y se usa $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.

:::satz Teorema 4.10 (Mejor solución aproximada con QR)
<span class="anker" id="satz-4-10"></span>

Si $\mathbf{A}=\mathbf{Q}\mathbf{R}$ es la descomposición QR, la mejor solución aproximada de $\mathbf{A}\mathbf{x}=\mathbf{y}$ es la solución de

<span class="anker" id="gl-4-6"></span>
$$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y} . \tag{4.6}$$
:::

:::beweis Resolver con QR
Se tiene $\mathbf{A}^{\top}\mathbf{A}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{R}^{\top}\mathbf{R}$ y $\mathbf{A}^{\top}\mathbf{y}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. Las ecuaciones normales son, por tanto, $\mathbf{R}^{\top}\mathbf{R}\hat{\mathbf{x}}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. La matriz triangular $\mathbf{R}$ tiene entradas diagonales positivas y, por tanto, según [Fundamentos 1, sección 14.4](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-4), un determinante distinto de cero, de modo que es invertible; lo mismo vale para $\mathbf{R}^{\top}$. Si se multiplica por la izquierda por $(\mathbf{R}^{\top})^{-1}$, queda [(4.6)](#gl-4-6).
:::

El sistema [(4.6)](#gl-4-6) tiene forma triangular y se resuelve de abajo arriba, como en la sustitución regresiva al final de la eliminación gaussiana de [Fundamentos 1, sección 12.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3). Para una matriz $m\times n$, el camino completo cuesta unas $2mn^2$ operaciones aritméticas elementales, casi todas para la descomposición QR.

::::beispiel [Ejemplo numérico]
Para $\mathbf{H}$ y $\mathbf{y}=(1,\,1,\,1)^{\top}$ es $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac2{\sqrt2},\ \tfrac{-1+2+1}{\sqrt6}\bigr)^{\top}=\bigl(\sqrt2,\ \tfrac2{\sqrt6}\bigr)^{\top}$. La fila inferior de [(4.6)](#gl-4-6) dice $\sqrt{\tfrac32}\,\hat x_2=\tfrac2{\sqrt6}$, es decir, $\hat x_2=\tfrac2{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac23$. La fila superior dice $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac23=\sqrt2$, es decir, $\hat x_1=1-\tfrac13=\tfrac23$. Es la misma solución que con las ecuaciones normales. Las componentes de $\mathbf{Q}^{\top}\mathbf{y}$ son los productos escalares de la fig. [13](#abb-13).

:::abbildung ml/k2rqr 13
El lado derecho $\mathbf{Q}^{\top}\mathbf{y}$ del sistema triangular para $\mathbf{y}=(1,1,1)^{\top}$, con $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ y $\mathbf{q}_2=(-1,2,1)^{\top}/\sqrt6$.
:::
::::

⁠**En resumen:** Con $\mathbf{A}=\mathbf{Q}\mathbf{R}$, las ecuaciones normales se convierten en el sistema triangular $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$; la matriz $\mathbf{A}^{\top}\mathbf{A}$ no se forma nunca.

:::aufgabe Ejercicio 11 ★ Gram-Schmidt y proyección
<span class="anker" id="aufg-11"></span>

Se dan $\mathbf{a}_1=(1,\,1,\,0)^{\top}$ y $\mathbf{a}_2=(1,\,0,\,1)^{\top}$.

<ol class="al">

<li>

Aplica el proceso de Gram-Schmidt y comprueba que $\mathbf{q}_1,\mathbf{q}_2$ son ortonormales.

</li>

<li>

Calcula la matriz de proyección $\mathbf{P}=\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}$ sobre el plano generado por $\mathbf{a}_1$ y $\mathbf{a}_2$, y proyecta $\mathbf{y}=(1,\,2,\,3)^{\top}$.

</li>

<li>

Determina un vector que genere el complemento ortogonal del plano y comprueba $\mathbf{I}-\mathbf{P}=\mathbf{k}\mathbf{k}^{\top}/(\mathbf{k}^{\top}\mathbf{k})$.

</li>

</ol>

:::loesung
(a) $\mathbf{q}_1=\mathbf{a}_1/\sqrt2=(1,\,1,\,0)^{\top}/\sqrt2$. Entonces $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ y

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\tfrac1{\sqrt2}\,\mathbf{q}_1=(1,\,0,\,1)^{\top}-\tfrac12(1,\,1,\,0)^{\top}=\bigl(\tfrac12,\,-\tfrac12,\,1\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert^2=\tfrac14+\tfrac14+1=\tfrac32 ,$$

luego $\mathbf{q}_2=\tilde{\mathbf{q}}_2/\sqrt{3/2}=(1,\,-1,\,2)^{\top}/\sqrt6$. Comprobación: $\mathbf{q}_1^{\top}\mathbf{q}_2=(1-1+0)/\sqrt{12}=0$, $\lVert\mathbf{q}_2\rVert^2=\tfrac{1+1+4}6=1$.

(b)

$$\mathbf{P}=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}+\frac16\begin{pmatrix}1&-1&2\\-1&1&-2\\2&-2&4\end{pmatrix}=\frac13\begin{pmatrix}2&1&1\\1&2&-1\\1&-1&2\end{pmatrix},$$

$$\mathbf{P}\mathbf{y}=\frac13\begin{pmatrix}2+2+3\\1+4-3\\1-2+6\end{pmatrix}=\begin{pmatrix}7/3\\2/3\\5/3\end{pmatrix}.$$

(c) Se busca $\mathbf{k}$ con $\mathbf{a}_1^{\top}\mathbf{k}=k_1+k_2=0$ y $\mathbf{a}_2^{\top}\mathbf{k}=k_1+k_3=0$; por tanto, $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ o un múltiplo. Se tiene $\mathbf{k}^{\top}\mathbf{k}=3$ y

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&-1&-1\\-1&1&1\\-1&1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}} .$$

El complemento ortogonal del plano es la recta en la dirección de $\mathbf{k}$, de dimensión $3-2=1$. Como control: $\mathbf{y}-\mathbf{P}\mathbf{y}=(-\tfrac43,\,\tfrac43,\,\tfrac43)^{\top}=-\tfrac43\mathbf{k}$ está sobre ella.
:::
:::

:::aufgabe Ejercicio 12 ★★ Resolver con QR
<span class="anker" id="aufg-12"></span>

Usa la matriz $\mathbf{A}$ con las columnas $\mathbf{a}_1$ y $\mathbf{a}_2$ del ejercicio [11](#aufg-11).

<ol class="al">

<li>

Da la descomposición QR y comprueba $\mathbf{Q}\mathbf{R}=\mathbf{A}$.

</li>

<li>

Resuelve $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$ en el sentido de mínimos cuadrados con [(4.6)](#gl-4-6) y, como control, con las ecuaciones normales.

</li>

</ol>

:::loesung
(a) Del ejercicio [11](#aufg-11): $\mathbf{q}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{q}_2=(1,\,-1,\,2)^{\top}/\sqrt6$, $r_{11}=\lVert\mathbf{a}_1\rVert=\sqrt2$, $r_{12}=\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$, $r_{22}=\lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{3/2}$:

$$\mathbf{Q}=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.$$

Comprobación: la columna 1 de $\mathbf{Q}\mathbf{R}$ es $\sqrt2\,\mathbf{q}_1=\mathbf{a}_1$; la columna 2 es $\tfrac1{\sqrt2}\mathbf{q}_1+\sqrt{\tfrac32}\,\mathbf{q}_2=\tfrac12(1,\,1,\,0)^{\top}+\tfrac12(1,\,-1,\,2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_2$, pues $\sqrt{3/2}/\sqrt6=\tfrac12$.

(b) $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac3{\sqrt2},\ \tfrac{1-2+6}{\sqrt6}\bigr)^{\top}=\bigl(\tfrac3{\sqrt2},\ \tfrac5{\sqrt6}\bigr)^{\top}$. La fila inferior de $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ da $\hat x_2=\tfrac5{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac53$; la superior, $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac53=\tfrac3{\sqrt2}$, que, multiplicada por $\sqrt2$, da $2\hat x_1+\tfrac53=3$; luego $\hat x_1=\tfrac23$. Control con las ecuaciones normales: $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}^{\top}\mathbf{y}=(3,\,4)^{\top}$, $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(3,\,4)^{\top}=(\tfrac23,\,\tfrac53)^{\top}$. Además, $\mathbf{A}\hat{\mathbf{x}}=(\tfrac73,\,\tfrac23,\,\tfrac53)^{\top}=\mathbf{P}\mathbf{y}$ del ejercicio [11](#aufg-11).
:::
:::

:::aufgabe Ejercicio 13 ★★ Complementos
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

¿Qué dimensión tiene el complemento ortogonal de una recta que pasa por el origen en $\mathbb{R}^3$? ¿Y el de una recta en $\mathbb{R}^5$?

</li>

<li>

Demuestra: $(\mathcal U^\perp)^\perp=\mathcal U$. Pista: demuestra primero que todo vector de $\mathcal U$ está en $(\mathcal U^\perp)^\perp$. Después descompón un vector $\mathbf{y}\in(\mathcal U^\perp)^\perp$ como en el teorema de la sección [4.4](#stufe-4-4) y calcula el producto escalar con su parte en $\mathcal U^\perp$.

</li>

</ol>

:::loesung
(a) Según el teorema de la sección [4.4](#stufe-4-4), $\dim\mathcal U^\perp=n-\dim\mathcal U$: en $\mathbb{R}^3$, por tanto, $3-1=2$, un plano; en $\mathbb{R}^5$ es $5-1=4$.

(b) Primera parte: si $\mathbf{u}\in\mathcal U$, entonces $\mathbf{u}^{\top}\mathbf{z}=0$ para todo $\mathbf{z}\in\mathcal U^\perp$, por la definición de $\mathcal U^\perp$. Por tanto, $\mathbf{u}$ es perpendicular a todo $\mathcal U^\perp$ y está en $(\mathcal U^\perp)^\perp$. Segunda parte: sea $\mathbf{y}\in(\mathcal U^\perp)^\perp$. Según el teorema, se descompone $\mathbf{y}=\mathbf{u}+\mathbf{z}$ con $\mathbf{u}\in\mathcal U$ y $\mathbf{z}\in\mathcal U^\perp$. Entonces $\mathbf{z}^{\top}\mathbf{y}=0$, porque $\mathbf{y}$ es perpendicular a $\mathcal U^\perp$, y $\mathbf{z}^{\top}\mathbf{u}=0$, porque $\mathbf{z}$ es perpendicular a $\mathcal U$. Por tanto, $\mathbf{z}^{\top}\mathbf{z}=\mathbf{z}^{\top}\mathbf{y}-\mathbf{z}^{\top}\mathbf{u}=0$, y $\mathbf{z}=\mathbf{0}$. Así, $\mathbf{y}=\mathbf{u}\in\mathcal U$. Cada uno de los dos conjuntos contiene al otro: son iguales.
:::
:::
