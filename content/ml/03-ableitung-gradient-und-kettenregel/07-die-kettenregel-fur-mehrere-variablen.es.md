---
title: La regla de la cadena para varias variables
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230700
summary: Los cálculos con muchas variables son cadenas de funciones con muchas entradas y salidas.
tags: curva, vector velocidad
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Los cálculos con muchas variables son cadenas de funciones con muchas entradas y salidas. La regla de la cadena se traslada a ellas: las matrices jacobianas de las etapas se multiplican. Componente a componente, esto significa que se suma sobre todos los caminos por los que una variación llega de una entrada a la salida. Para el gradiente de un número aparece aquí la matriz jacobiana traspuesta.
:::

### La regla de la cadena como producto de matrices

<span class="anker" id="stufe-6-1"></span>

Sean dos etapas conectadas una tras otra: $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ convierte $\mathbf{x}$ en el vector intermedio $\mathbf{u}=\mathbf{g}(\mathbf{x})$, y $\mathbf f:\mathbb{R}^m\to\mathbb{R}^p$ convierte este en $\mathbf{y}=\mathbf f(\mathbf{u})$. Se sigue una pequeña variación $\Delta\mathbf{x}$ como en la sección [2.2](die-kettenregel.html#stufe-2-2). La primera etapa la transmite, según [(5.3)](die-jacobi-matrix.html#gl-5-3), como $\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$; la segunda, como $\Delta\mathbf{y}\approx\mathbf{J}_{\mathbf f}\,\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$. El producto de dos números se convierte en el producto de dos matrices. Esto encaja con el [capítulo 1, sección 9.4](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-4): dos etapas lineales una tras otra son una etapa lineal cuya matriz es el producto de las dos matrices.

:::satz Teorema 6.1 (Regla de la cadena para varias variables)
<span class="anker" id="satz-6-1"></span>

Si $\mathbf{g}$ es diferenciable en el punto $\mathbf{x}$ y $\mathbf f$ es diferenciable en el punto $\mathbf{g}(\mathbf{x})$, entonces $\mathbf f\circ\mathbf{g}$ es diferenciable en el punto $\mathbf{x}$, y

<span class="anker" id="gl-6-1"></span>
$$\mathbf{J}_{\mathbf f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_{\mathbf f}\bigl(\mathbf{g}(\mathbf{x})\bigr)\,\mathbf{J}_{\mathbf{g}}(\mathbf{x}). \tag{6.1}$$
:::

Las formas encajan: a la izquierda hay una matriz $p\times n$; a la derecha, una matriz $p\times m$ por una matriz $m\times n$. El número común $m$ es el número de variables intermedias. Como con una variable, cada matriz jacobiana se evalúa donde trabaja su etapa, es decir, $\mathbf{J}_{\mathbf f}$ en el valor intermedio $\mathbf{u}=\mathbf{g}(\mathbf{x})$. En cadenas más largas $\mathbf f_L\circ\dots\circ\mathbf f_1$, la matriz jacobiana es el producto $\mathbf{J}_{\mathbf f_L}\cdots\mathbf{J}_{\mathbf f_1}$, con la etapa aplicada en último lugar a la izquierda del todo. A diferencia de lo que ocurre con los números, los factores no pueden intercambiarse.

:::beweis Regla de la cadena para varias variables
La demostración es como en la sección [2.2](die-kettenregel.html#stufe-2-2), con longitudes en lugar de valores absolutos. Con $\mathbf{u}=\mathbf{g}(\mathbf{x})$ y $\mathbf{k}=\mathbf{g}(\mathbf{x}+\mathbf{h})-\mathbf{u}=\mathbf{J}_{\mathbf{g}}\mathbf{h}+\mathbf{r}_{\mathbf{g}}(\mathbf{h})$ se tiene

$$\mathbf f\bigl(\mathbf{g}(\mathbf{x}+\mathbf{h})\bigr)-\mathbf f(\mathbf{u})=\mathbf{J}_{\mathbf f}\,\mathbf{k}+\mathbf{r}_{\mathbf f}(\mathbf{k})=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}\,\mathbf{h}+\mathbf{J}_{\mathbf f}\,\mathbf{r}_{\mathbf{g}}(\mathbf{h})+\mathbf{r}_{\mathbf f}(\mathbf{k}).$$

El error central desaparece más rápido que $\lVert\mathbf{h}\rVert$, porque $\mathbf{r}_{\mathbf{g}}$ lo hace y la multiplicación por una matriz fija aumenta las longitudes a lo sumo en un factor fijo. El último desaparece más rápido que $\lVert\mathbf{k}\rVert$, y $\lVert\mathbf{k}\rVert$ es a lo sumo un múltiplo fijo de $\lVert\mathbf{h}\rVert$ en cuanto $\mathbf{h}$ es pequeño. Así pues, $\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$ es la matriz de la aproximación lineal de $\mathbf f\circ\mathbf{g}$.
:::

::::beispiel [Ejemplo numérico]
Sea $\mathbf{g}$ como en [(5.1)](die-jacobi-matrix.html#gl-5-1) y $f(\mathbf{u})=u_1^2+3u_2$, una función con una salida ($p=1$). Su composición es $F(\mathbf{x})=f(\mathbf{g}(\mathbf{x}))=x_1^2x_2^2+6x_1+3x_2^2$. En el punto $\mathbf{x}=(1,\,2)^{\top}$ se tiene $\mathbf{u}=\mathbf{g}(\mathbf{x})=(2,\,6)^{\top}$ y $\mathbf{J}_f(\mathbf{u})=(2u_1\ \ 3)=(4\ \ 3)$. Según [(6.1)](#gl-6-1),

$$\mathbf{J}_F(1,2)=\begin{pmatrix}4&3\end{pmatrix}\begin{pmatrix}2&1\\2&4\end{pmatrix}=\begin{pmatrix}4\cdot2+3\cdot2&\ 4\cdot1+3\cdot4\end{pmatrix}=\begin{pmatrix}14&16\end{pmatrix}.$$

Comprobación con la función escrita explícitamente: $\partial_1F=2x_1x_2^2+6=8+6=14$ y $\partial_2F=2x_1^2x_2+6x_2=4+12=16$.
::::

⁠**En resumen:** La matriz jacobiana de una composición es el producto de las matrices jacobianas de las etapas, con la etapa aplicada en último lugar a la izquierda: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}$.

### Suma sobre todos los caminos

<span class="anker" id="stufe-6-2"></span>

Si se escribe el producto de matrices [(6.1)](#gl-6-1) para una entrada de la matriz, aparece una suma sobre las variables intermedias. Para una función $F=f\circ\mathbf{g}$ con una salida se tiene

<span class="anker" id="gl-6-2"></span>
$$\frac{\partial F}{\partial x_j}(\mathbf{x})=\sum_{i=1}^m\frac{\partial f}{\partial u_i}(\mathbf{u})\,\frac{\partial u_i}{\partial x_j}(\mathbf{x}),\qquad \mathbf{u}=\mathbf{g}(\mathbf{x}). \tag{6.2}$$

Esta suma tiene un significado intuitivo. Una variación de $x_j$ no llega a $F$ directamente, sino a través de las variables intermedias $u_1,\dots,u_m$. Cada variable intermedia es un camino: en el camino a través de $u_i$, la variación se multiplica primero por $\partial u_i/\partial x_j$ y después por $\partial f/\partial u_i$. A la salida llegan las contribuciones de todos los caminos y se suman (fig. [11](#abb-11)). Por eso, la regla de la cadena se resume a menudo así: a lo largo de un camino, multiplicar; sobre todos los caminos, sumar.

:::abbildung ml/k3wege 11
La regla de la cadena como red de caminos para $F=f\circ\mathbf{g}$ en el punto $(1,\,2)$. En cada arista figura la derivada local del destino respecto del punto de partida de la arista. Desde $x_1$ llevan dos caminos a $F$: a través de $u_1$ (azul) y a través de $u_2$ (naranja). A lo largo de cada camino se multiplican los factores, y las dos contribuciones se suman. Puede imaginarse una red de tuberías en la que cada tubería multiplica por su factor la cantidad que la atraviesa y los caudales se reúnen en el destino.
:::

::::beispiel [Ejemplo numérico 1]
Para $F=f\circ\mathbf{g}$ de la subsección anterior, los factores de las aristas en el punto $(1,\,2)$ son

$$\frac{\partial u_1}{\partial x_1}=x_2=2,\quad \frac{\partial u_1}{\partial x_2}=x_1=1,\quad \frac{\partial u_2}{\partial x_1}=2,\quad \frac{\partial u_2}{\partial x_2}=2x_2=4,\quad \frac{\partial f}{\partial u_1}=2u_1=4,\quad \frac{\partial f}{\partial u_2}=3 .$$

Sumando sobre ambos caminos se obtienen las entradas $14$ y $16$, como en el producto de matrices (fig. [12](#abb-12)).

:::abbildung ml/k3rwege 12
Las derivadas parciales de $F=f\circ\mathbf{g}$ en el punto $(1,\,2)$ como sumas sobre los dos caminos a través de $u_1$ y $u_2$.
:::
::::

::::beispiel [Ejemplo numérico 2]
Una entrada, dos caminos. Sea $F(x)=g_1(x)\,g_2(x)$ con $g_1(x)=x^2$ y $g_2(x)=3x$, es decir, $f(\mathbf{u})=u_1u_2$. Los caminos a través de $u_1$ y $u_2$ dan

$$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial f}{\partial u_1}\,g_1'(x)+\frac{\partial f}{\partial u_2}\,g_2'(x)=u_2\cdot2x+u_1\cdot3=3x\cdot2x+x^2\cdot3=9x^2 .$$

Comprobación: $F(x)=3x^3$ tiene la derivada $9x^2$. Quien olvida un camino obtiene $6x^2$ o $3x^2$. De paso, esto es exactamente la regla del producto [(1.5)](die-ableitung.html#gl-1-5): es la regla de la cadena para dos caminos.
::::

⁠**En resumen:** Componente a componente, la regla de la cadena es una suma sobre todos los caminos de la entrada a la salida; a lo largo de cada camino se multiplican las derivadas locales.

:::hintergrund Por qué se suma sobre los caminos
La razón es la observación de la sección [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4): con variaciones pequeñas, los efectos se suman. Si se modifica $x_j$ en $\Delta x_j$, cambian todas las variables intermedias a la vez, cada una aproximadamente en $\frac{\partial u_i}{\partial x_j}\Delta x_j$. Cómo actúan estas variaciones simultáneas sobre $f$ lo dice la aproximación lineal de $f$ en las variables $u_1,\dots,u_m$: cada una aporta $\frac{\partial f}{\partial u_i}\Delta u_i$, y las contribuciones se suman como si cada variable intermedia hubiera cambiado sola. La suma sobre los caminos es, por tanto, la suma de estas contribuciones individuales. En cadenas más largas esto continúa: un camino pasa entonces por varias variables intermedias sucesivas; a lo largo del camino se multiplican todos los factores de las aristas y, al final, se suma sobre todos los caminos de la entrada a la salida. El número de caminos puede crecer muy deprisa; cómo agruparlos hábilmente lo muestra la sección [10](automatische-differentiation.html#stufe-10).
:::

### El gradiente de una composición

<span class="anker" id="stufe-6-3"></span>

Para una función $F=f\circ\mathbf{g}$ con una salida, la matriz jacobiana es el gradiente como fila. Si se quiere el gradiente como columna, tal como lo ha convenido este capítulo, hay que trasponer la regla de la cadena.

:::satz Teorema 6.2 (Gradiente de una composición)
<span class="anker" id="satz-6-2"></span>

Si $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ es diferenciable en el punto $\mathbf{x}$ y $f:\mathbb{R}^m\to\mathbb{R}$ es diferenciable en el punto $\mathbf{u}=\mathbf{g}(\mathbf{x})$, entonces

<span class="anker" id="gl-6-3"></span>
$$\nabla(f\circ\mathbf{g})(\mathbf{x})=\mathbf{J}_{\mathbf{g}}(\mathbf{x})^{\top}\,\nabla f(\mathbf{u}). \tag{6.3}$$
:::

:::beweis Gradiente de una composición
Según [(6.1)](#gl-6-1), $\nabla(f\circ\mathbf{g})(\mathbf{x})^{\top}=\mathbf{J}_{f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_f(\mathbf{u})\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\nabla f(\mathbf{u})^{\top}\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})$. Si se trasponen ambos lados con la regla $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ del [capítulo 1, sección 10.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1), se sigue la afirmación.
:::

La traspuesta es pura contabilidad: surge porque el gradiente se escribe como columna, mientras que las filas de la matriz jacobiana corresponden a las salidas. En cuanto al contenido, [(6.3)](#gl-6-3) dice lo mismo que [(6.2)](#gl-6-2): la componente $j$ de $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ es la columna $j$ de $\mathbf{J}_{\mathbf{g}}$ por $\nabla f$, es decir, la suma sobre los caminos que parten de $x_j$. Si la función interior es lineal, $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}$, según la sección [5.4](die-jacobi-matrix.html#stufe-5-4) se obtiene la regla $\nabla_{\mathbf{x}}f(\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\,\nabla f(\mathbf{A}\mathbf{x})$. El subíndice $\mathbf{x}$ en nabla indica respecto de qué variable se forma el gradiente.

::::beispiel [Ejemplo numérico]
Con $\mathbf{J}_{\mathbf{g}}(1,2)$ y $\nabla f(\mathbf{u})=(4,\,3)^{\top}$ del ejemplo de [(6.1)](#gl-6-1) se tiene

$$\nabla F(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}^{\top}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}2&2\\1&4\end{pmatrix}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}8+6\\4+12\end{pmatrix}=\begin{pmatrix}14\\16\end{pmatrix}.$$

Sin trasponer se obtendría $\mathbf{J}_{\mathbf{g}}\,\nabla f=(8+3;\ 8+12)^{\top}=(11,\,20)^{\top}$, y eso es incorrecto.
::::

:::warnung No olvides la traspuesta
Si la matriz jacobiana de la función interior es simétrica, olvidar la trasposición no se nota. Por eso, comprueba una fórmula de gradiente deducida por ti mismo con un ejemplo cuya matriz jacobiana no sea simétrica. Si $\mathbf{J}_{\mathbf{g}}$ no tiene el mismo número de filas que de columnas, un vistazo a las formas delata el error de inmediato: $\nabla f$ tiene $m$ entradas, $\mathbf{J}_{\mathbf{g}}^{\top}$ tiene $m$ columnas, y solo $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ da un vector con $n$ entradas.
:::

⁠**En resumen:** El gradiente de una composición es la matriz jacobiana traspuesta de la función interior por el gradiente de la exterior: $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

### Derivada a lo largo de una curva

<span class="anker" id="stufe-6-4"></span>

Un paseo por el mapa es una curva: en cada instante $t$ uno está en un lugar $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$. ¿Con qué rapidez cambia la altura $f(\boldsymbol{\gamma}(t))$ por el camino? Es un caso particular de la regla de la cadena con una única variable de entrada $t$.

:::definition Definición 6.3 (Curva y velocidad)
<span class="anker" id="satz-6-3"></span>

Una __curva__ es una función $\boldsymbol{\gamma}:\mathbb{R}\to\mathbb{R}^d$, $t\mapsto\boldsymbol{\gamma}(t)=(\gamma_1(t),\dots,\gamma_d(t))^{\top}$. Su derivada $\boldsymbol{\gamma}'(t)=(\gamma_1'(t),\dots,\gamma_d'(t))^{\top}$ se llama __vector velocidad__.
:::

El vector velocidad es la matriz jacobiana de $\boldsymbol{\gamma}$, una matriz $d\times1$. Apunta en la dirección en la que uno se mueve en ese momento, y su longitud es la rapidez. Según [(6.1)](#gl-6-1) con $n=1$, para $f$ diferenciable se cumple

<span class="anker" id="gl-6-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)=\nabla f\bigl(\boldsymbol{\gamma}(t)\bigr)^{\top}\boldsymbol{\gamma}'(t). \tag{6.4}$$

Para una recta $\boldsymbol{\gamma}(t)=\mathbf{x}+t\,\mathbf{h}$ se tiene $\boldsymbol{\gamma}'=\mathbf{h}$ y la tasa $\nabla f(\mathbf{x})^{\top}\mathbf{h}$; si $\mathbf{h}$ tiene longitud $1$, es la derivada direccional de la sección [4.1](richtungsableitung-und-steilster-anstieg.html#stufe-4-1). Si una curva discurre por completo dentro de una curva de nivel, $f(\boldsymbol{\gamma}(t))$ es constante, y el lado izquierdo es, por tanto, nulo: el gradiente es perpendicular a todo vector velocidad dentro de la curva de nivel. Este es el teorema de la sección [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3), ahora justificado con la regla de la cadena.

::::beispiel [Ejemplo numérico]
Sea $f(\mathbf{x})=x_1^2x_2+x_2^2$ y $\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$, una recta que pasa por $(1,\,2)$ con $\boldsymbol{\gamma}'(t)=(1,\,2)^{\top}$. En $t=0$ se tiene

$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)\Big|_{t=0}=\begin{pmatrix}4&5\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=4+10=14 .$$

Comprobación: $f(\boldsymbol{\gamma}(t))=(1+t)^2(2+2t)+(2+2t)^2=2\,(1+t)^3+4\,(1+t)^2$ tiene en $t=0$ la derivada $6+8=14$.
::::

⁠**En resumen:** A lo largo de una curva, $f$ cambia con la tasa $\nabla f^{\top}\boldsymbol{\gamma}'$; dentro de una curva de nivel, esta tasa es nula.

:::aufgabe Ejercicio 20 ★ Regla de la cadena con matrices jacobianas
<span class="anker" id="aufg-20"></span>

Sea $\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1x_2)^{\top}$ y $f(\mathbf{u})=u_1^2-u_2$.

<ol class="al">

<li>

Calcula en el punto $\mathbf{x}=(1,\,3)^{\top}$ el valor intermedio $\mathbf{u}$, la matriz jacobiana $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ y $\nabla f(\mathbf{u})$.

</li>

<li>

Calcula $\nabla(f\circ\mathbf{g})(\mathbf{x})$ con [(6.3)](#gl-6-3) y compruébalo con la función escrita explícitamente. ¿Qué saldría sin trasponer?

</li>

</ol>

:::loesung
(a) $\mathbf{u}=\mathbf{g}(1,3)=(4,\,3)^{\top}$. La matriz jacobiana es $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}1&1\\x_2&x_1\end{smallmatrix}\bigr)$; en el punto $(1,\,3)$, por tanto, $\bigl(\begin{smallmatrix}1&1\\3&1\end{smallmatrix}\bigr)$. El gradiente de la función exterior es $\nabla f(\mathbf{u})=(2u_1,\,-1)^{\top}=(8,\,-1)^{\top}$.

(b) Según [(6.3)](#gl-6-3):

$$\nabla(f\circ\mathbf{g})(1,3)=\begin{pmatrix}1&3\\1&1\end{pmatrix}\begin{pmatrix}8\\-1\end{pmatrix}=\begin{pmatrix}8-3\\8-1\end{pmatrix}=\begin{pmatrix}5\\7\end{pmatrix}.$$

Comprobación: $F(\mathbf{x})=(x_1+x_2)^2-x_1x_2=x_1^2+x_1x_2+x_2^2$ tiene las derivadas parciales $2x_1+x_2=5$ y $x_1+2x_2=7$. Sin trasponer se obtendría $\mathbf{J}_{\mathbf{g}}\nabla f=(8-1;\ 24-1)^{\top}=(7,\,23)^{\top}$, es decir, un resultado incorrecto.
:::
:::

:::aufgabe Ejercicio 21 ★★ Tres caminos
<span class="anker" id="aufg-21"></span>

Sea $F(x)=g_1(x)\,g_2(x)\,g_3(x)$ con $g_1(x)=x$, $g_2(x)=x^2$ y $g_3(x)=x^3$.

<ol class="al">

<li>

Dibuja la red de caminos de $x$ a través de $u_1,u_2,u_3$ hasta $F=u_1u_2u_3$ y escribe en cada arista su factor.

</li>

<li>

Calcula $F'(x)$ como suma sobre los tres caminos y compárala con la derivada de $x^6$.

</li>

</ol>

:::loesung
(a) De $x$ salen tres aristas hacia $u_1$, $u_2$, $u_3$, con los factores $1$, $2x$ y $3x^2$. De cada $u_i$ sale una arista hacia $F=u_1u_2u_3$; su factor es el producto de los otros dos: $u_2u_3=x^5$, $u_1u_3=x^4$ y $u_1u_2=x^3$.

(b) Sumando sobre los tres caminos:

$$F'(x)=x^5\cdot1+x^4\cdot2x+x^3\cdot3x^2=x^5+2x^5+3x^5=6x^5 .$$

Esta es la derivada de $F(x)=x^6$. El camino a través de $u_k$ aporta $k\,x^5$, porque $g_k=x^k$ tiene la derivada $k\,x^{k-1}$ y los otros dos factores dan juntos $x^{6-k}$. La regla del producto para tres factores es, por tanto, la suma sobre tres caminos.
:::
:::

:::aufgabe Ejercicio 22 ★★ Curva dentro de la curva de nivel
<span class="anker" id="aufg-22"></span>

Sea $f(\mathbf{x})=x_1^2+4x_2^2$ y $\boldsymbol{\gamma}(t)=\bigl(\sqrt5\cos t,\ \tfrac{\sqrt5}2\sin t\bigr)^{\top}$.

<ol class="al">

<li>

Demuestra que $\boldsymbol{\gamma}$ discurre por completo dentro de la curva de nivel $f=5$.

</li>

<li>

Determina $t$ con $\boldsymbol{\gamma}(t)=(1,\,1)^{\top}$, calcula allí $\boldsymbol{\gamma}'(t)$ y comprueba $\nabla f^{\top}\boldsymbol{\gamma}'=0$. Compara la dirección con el vector $\mathbf{t}$ de la sección [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

</li>

<li>

Justifica en general con [(6.4)](#gl-6-4): si una curva derivable discurre dentro de un conjunto de nivel de $f$, entonces $\nabla f$ es perpendicular a su vector velocidad.

</li>

</ol>

:::loesung
(a) $f(\boldsymbol{\gamma}(t))=5\cos^2t+4\cdot\tfrac54\sin^2t=5\,(\cos^2t+\sin^2t)=5$ para todo $t$.

(b) De $\sqrt5\cos t=1$ y $\tfrac{\sqrt5}2\sin t=1$ se sigue $\cos t=1/\sqrt5$ y $\sin t=2/\sqrt5$, es decir, $t\approx1{,}107$. Allí se tiene

$$\boldsymbol{\gamma}'(t)=\bigl(-\sqrt5\sin t,\ \tfrac{\sqrt5}2\cos t\bigr)^{\top}=\bigl(-2,\ \tfrac12\bigr)^{\top},\qquad \nabla f(1,1)^{\top}\boldsymbol{\gamma}'=2\cdot(-2)+8\cdot\tfrac12=0 .$$

El vector velocidad es $-\tfrac12\,(4,\,-1)^{\top}$; es, por tanto, paralelo al vector $\mathbf{t}$ de la sección [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

(c) Si $\boldsymbol{\gamma}$ discurre dentro del conjunto de nivel del valor $c$, entonces $f(\boldsymbol{\gamma}(t))=c$ para todo $t$, y la derivada respecto de $t$ es cero. Según [(6.4)](#gl-6-4), esta derivada es $\nabla f(\boldsymbol{\gamma}(t))^{\top}\boldsymbol{\gamma}'(t)$. Por tanto, el gradiente es perpendicular a todo vector velocidad de una curva dentro del conjunto de nivel.
:::
:::

:::aufgabe Ejercicio 23 ★★★ Una cadena de tres etapas
<span class="anker" id="aufg-23"></span>

Sea $F(\mathbf{x})=\sum_{i=1}^2(\mathbf{A}\mathbf{x})_i^2$ con $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$. El cálculo consta de tres etapas: $\mathbf{u}=\mathbf{A}\mathbf{x}$, después $v_i=u_i^2$ para cada componente, después $F=v_1+v_2$.

<ol class="al">

<li>

Da las tres matrices jacobianas en el punto $\mathbf{x}=(2,\,1)^{\top}$ y calcula $\mathbf{J}_F$ como su producto.

</li>

<li>

Demuestra en general que $\nabla F(\mathbf{x})=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$ y comprueba el resultado de (a).

</li>

<li>

Calcula el producto de (a) una vez empezando por la izquierda y otra empezando por la derecha. ¿Qué orden necesita menos multiplicaciones si $\mathbf{A}$ es una matriz $n\times n$?

</li>

</ol>

:::loesung
(a) En el punto $(2,\,1)$ se tiene $\mathbf{u}=\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, $\mathbf{v}=(16,\,1)^{\top}$ y $F=17$. Las matrices jacobianas son $\mathbf{J}_1=\mathbf{A}$, $\mathbf{J}_2=\operatorname{diag}(2u_1;\,2u_2)=\operatorname{diag}(8;\,2)$ y $\mathbf{J}_3=(1\ \ 1)$. Su producto es

$$\mathbf{J}_F=(1\ \ 1)\,\operatorname{diag}(8;\,2)\,\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 2)\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 18).$$

(b) Trasponiendo, $\nabla F=\mathbf{A}^{\top}\,\operatorname{diag}(2\mathbf{u})\,\mathbf{1}=\mathbf{A}^{\top}\,2\mathbf{u}=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$. Con $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$ se tiene $2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=2\,(4,\,9)^{\top}=(8,\,18)^{\top}$, como en (a). Comprobación: $F=(x_1+2x_2)^2+x_2^2$ tiene las derivadas parciales $2\cdot4=8$ y $4\cdot4+2=18$.

(c) Empezando por la izquierda: $(1\ \ 1)\,\operatorname{diag}(8;2)$ es una fila para la que se necesitan $n$ multiplicaciones, y la fila por $\mathbf{A}$ necesita $n^2$. Empezando por la derecha: $\operatorname{diag}(8;2)\,\mathbf{A}$ necesita $n^2$ multiplicaciones, y la fila por el resultado, otras $n^2$. Por la izquierda son, por tanto, unas $n^2$ multiplicaciones; por la derecha, unas $2n^2$. Si la matriz del medio no fuera diagonal, sino densa, el producto de matrices por la derecha costaría incluso unas $n^3$. Por la izquierda, empezando por el resultado, solo se generan filas.
:::
:::
