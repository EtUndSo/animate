---
title: Valores propios y vectores propios
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15220700
summary: Una matriz gira y estira a la vez la mayoría de los vectores.
tags: conjugado complejo, vector propio, valor propio, polinomio característico, espacio propio, traza, multiplicidad algebraica, multiplicidad geométrica
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Una matriz gira y estira a la vez la mayoría de los vectores. Pero hay direcciones que no gira: una flecha en esa dirección solo se alarga, se acorta o se invierte. Esta sección encuentra esas direcciones y los factores de estiramiento que les corresponden. Son los ejes naturales de una matriz.
:::

### Lo que necesitas: números complejos

<span class="anker" id="stufe-6-1"></span>

Al buscar factores de estiramiento aparecen ecuaciones polinómicas, y no todas tienen soluciones reales. Esta subsección reúne lo que este capítulo usa de los números complejos.

**Números complejos.** Un número complejo $z=x+\mathrm j\,y$ consta de la parte real $x$ y la parte imaginaria $y$, dos números reales. Para la unidad imaginaria se cumple $\mathrm j^2=-1$. La electrotecnia escribe $\mathrm j$ en lugar de $i$, porque $i$ está reservada para la corriente.

**Conjugación y módulo.** El número __conjugado complejo__ de $z$ es $z^*=x-\mathrm j\,y$. Se tiene $z\,z^*=x^2+y^2=|z|^2$, el cuadrado del módulo, un número real que solo es cero para $z=0$. Un número es real si y solo si $z=z^*$. La conjugación es compatible con la suma y el producto: $(z+w)^*=z^*+w^*$ y $(zw)^*=z^*w^*$. Para un vector $\mathbf{v}$ con componentes complejas, $\mathbf{v}^*$ designa en este capítulo el vector de las componentes conjugadas, sin trasponer. Entonces

$$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0\qquad\text{para }\mathbf{v}\ne\mathbf{0} .$$

**La fórmula de Euler.** Para todo número real $\alpha$ es $\mathrm e^{\mathrm j\alpha}=\cos\alpha+\mathrm j\sin\alpha$, un punto de la circunferencia unidad del plano complejo, de módulo $1$.

**Raíces de polinomios.** Todo polinomio de grado $n\ge1$ con coeficientes reales o complejos tiene exactamente $n$ raíces complejas si las raíces múltiples se cuentan con su multiplicidad, y se descompone en $n$ factores lineales. Si el polinomio tiene coeficientes reales, con $z$ también $z^*$ es una raíz: las raíces no reales vienen por pares.

⁠**Ejemplo numérico:** $\lambda^2-1{,}2\lambda+1=0$ tiene, según la fórmula de resolución, las raíces $\lambda=0{,}6\pm\sqrt{0{,}36-1}=0{,}6\pm\mathrm j\,0{,}8$, un par conjugado de módulo $\sqrt{0{,}36+0{,}64}=1$. Para $\mathbf{v}=(1,\,-\mathrm j)^{\top}$ es $\mathbf{v}^*=(1,\,\mathrm j)^{\top}$ y $(\mathbf{v}^*)^{\top}\mathbf{v}=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2$ (fig. [16](#abb-16)).

:::abbildung ml/k2rkomplex 16
El producto escalar $(\mathbf{v}^*)^{\top}\mathbf{v}$ para $\mathbf{v}=(1,-\mathrm j)^{\top}$: cada término es $v_i^*v_i=|v_i|^2$, pues $\mathrm j\cdot(-\mathrm j)=-\mathrm j^2=1$.
:::

⁠**En resumen:** Los números complejos $x+\mathrm jy$ con $\mathrm j^2=-1$ resuelven toda ecuación polinómica; conjugar cambia el signo de la parte imaginaria, y $zz^*=|z|^2$ es real.

### Vectores propios y valores propios

<span class="anker" id="stufe-6-2"></span>

En Fundamentos 1, sección 8.3, unas matrices giraban, estiraban y cizallaban la cuadrícula del plano. Al hacerlo, la mayoría de las flechas cambian de dirección. Pero en algunas matrices hay direcciones en las que una flecha se queda sobre su recta que pasa por el origen: solo se estira, se comprime o se invierte (fig. [17](#abb-17)).

:::abbildung ml/k2eigen 17
La matriz $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ transforma la circunferencia unidad (gris) en una elipse (azul). La flecha $\mathbf{v}_1=(1,1)^{\top}/\sqrt2$ (roja) se queda sobre su recta y se estira al quíntuplo; la flecha $\mathbf{v}_2=(1,-2)^{\top}/\sqrt5$ (verde), al doble; sus imágenes están dibujadas en tono claro. Las rectas grises son las dos direcciones propias. El vector unitario $\mathbf{e}_1$, en cambio, se transforma en $(4,2)^{\top}$ (a trazos) y cambia de dirección.
:::

:::definition Definición 6.1 (Vector propio, valor propio)
<span class="anker" id="satz-6-1"></span>

Sea $\mathbf{A}\in\mathbb{R}^{n\times n}$. Un vector $\mathbf{v}\ne\mathbf{0}$ se llama __vector propio__ de $\mathbf{A}$ si existe un número $\lambda$ con

<span class="anker" id="gl-6-1"></span>
$$\mathbf{A}\mathbf{v}=\lambda\,\mathbf{v} . \tag{6.1}$$

El número $\lambda$ se llama __valor propio__ correspondiente.
:::

El vector nulo queda excluido porque $\mathbf{A}\mathbf{0}=\lambda\mathbf{0}$ se cumple para todo número $\lambda$ y no revela nada. El valor propio, en cambio, sí puede ser cero: entonces el vector propio se transforma en $\mathbf{0}$. Un valor propio negativo invierte la flecha. En este capítulo, los valores propios se llaman $\lambda$ o $\lambda_i$. La palabra alemana *eigen* significa «propio»; el inglés la ha adoptado tal cual: *eigenvalue*, *eigenvector*.

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ se tiene

$$\mathbf{A}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.$$

Por tanto, $(1,\,1)^{\top}$ es un vector propio asociado al valor propio $5$, y $(1,\,-2)^{\top}$, uno asociado al valor propio $2$. El vector $(1,\,0)^{\top}$ no lo es, pues $(4,\,2)^{\top}$ no es un múltiplo de él.

⁠**En resumen:** La matriz no gira un vector propio; solo lo multiplica por un número, y ese número es el valor propio.

:::hintergrund Las funciones propias ya las conoces
De la teoría de señales y sistemas conoces la misma idea para funciones en lugar de vectores. Un sistema LTI con la respuesta al impulso $h(t)$ responde a la función exponencial $\mathrm e^{pt}$ con la frecuencia compleja $p$, que muchos libros escriben $s$, con

$$\int_{-\infty}^{\infty}h(\tau)\,\mathrm e^{p(t-\tau)}\,\mathrm{d}\tau=H(p)\,\mathrm e^{pt},\qquad H(p)=\int_{-\infty}^{\infty}h(\tau)\,\mathrm e^{-p\tau}\,\mathrm{d}\tau ,$$

para todos los $p$ para los que existe la integral. La forma de la entrada se conserva; solo se añade un factor numérico: $\mathrm e^{pt}$ es una función propia del sistema, y el valor propio es el valor $H(p)$ de la función de transferencia. La ecuación [(6.1)](#gl-6-1) dice lo mismo para una matriz. Un sistema LTI es una aplicación lineal de señales en señales; una matriz, una aplicación lineal de vectores en vectores; en ambos casos hay entradas que solo se multiplican por un número.
:::

### El polinomio característico

<span class="anker" id="stufe-6-3"></span>

¿Cómo se encuentran los valores propios sin adivinar? Se reescribe [(6.1)](#gl-6-1) de modo que todo quede a un lado: $\mathbf{A}\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}$, es decir, $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. Se busca un $\lambda$ para el que este sistema homogéneo tenga una solución $\mathbf{v}\ne\mathbf{0}$. Según Fundamentos 1, sección 11.5, eso significa que la matriz $\mathbf{A}-\lambda\mathbf{I}$ no es invertible. Según Fundamentos 1, sección 14.6, eso ocurre si y solo si su determinante es cero.

:::definition Definición 6.2 (Polinomio característico)
<span class="anker" id="satz-6-2"></span>

Para $\mathbf{A}\in\mathbb{R}^{n\times n}$,

<span class="anker" id="gl-6-2"></span>
$$p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I}) \tag{6.2}$$

se llama __polinomio característico__ de $\mathbf{A}$.
:::

:::satz Teorema 6.3 (Los valores propios son raíces)
<span class="anker" id="satz-6-3"></span>

Un número $\lambda$ es un valor propio de $\mathbf{A}$ si y solo si $p(\lambda)=0$.
:::

El polinomio característico tiene grado $n$. Para una matriz $2\times2$ es

<span class="anker" id="gl-6-3"></span>
$$\det\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}=(a-\lambda)(d-\lambda)-bc=\lambda^2-(a+d)\,\lambda+(ad-bc) . \tag{6.3}$$

Según la subsección sobre números complejos, tiene, contadas con su multiplicidad, exactamente $n$ raíces complejas. Una matriz $n\times n$ tiene, por tanto, $n$ valores propios si se admiten los complejos y los múltiples se cuentan varias veces.

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ es $p(\lambda)=\lambda^2-7\lambda+(12-2)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. Los valores propios son $5$ y $2$, como en la subsección anterior. Para la matriz diagonal $\operatorname{diag}(3;\,-1)$ es $p(\lambda)=(3-\lambda)(-1-\lambda)$, con las raíces $3$ y $-1$: los valores propios de una matriz diagonal están en su diagonal, y los vectores propios son los vectores unitarios.

⁠**En resumen:** Los valores propios son las raíces del polinomio característico $\det(\mathbf{A}-\lambda\mathbf{I})$; una matriz $n\times n$ tiene, contados con su multiplicidad y como números complejos, $n$ valores propios.

### Cálculo de vectores propios

<span class="anker" id="stufe-6-4"></span>

Si se conoce un valor propio $\lambda$, los vectores propios correspondientes son las soluciones $\mathbf{v}\ne\mathbf{0}$ del sistema homogéneo $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. Se encuentran con la eliminación gaussiana. Junto con $\mathbf{v}$, también todo múltiplo $c\,\mathbf{v}$ con $c\ne0$ es un vector propio, pues $\mathbf{A}(c\mathbf{v})=c\lambda\mathbf{v}=\lambda(c\mathbf{v})$. Un vector propio nunca es, por tanto, único; solo lo es su dirección, y a veces ni siquiera ella.

:::definition Definición 6.4 (Espacio propio)
<span class="anker" id="satz-6-4"></span>

El núcleo de $\mathbf{A}-\lambda\mathbf{I}$ se llama __espacio propio__ de $\mathbf{A}$ asociado al valor propio $\lambda$.
:::

Contiene todos los vectores propios asociados a $\lambda$ y el vector nulo. Como núcleo, es un subespacio en el sentido de la sección [4.1](projektion-auf-einen-unterraum.html#stufe-4-1).

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ y $\lambda=5$ se tiene

$$\mathbf{A}-5\mathbf{I}=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}.$$

Ambas filas exigen lo mismo: $-v_1+v_2=0$. El espacio propio es la recta de todos los múltiplos de $(1,\,1)^{\top}$. Para $\lambda=2$ es $\mathbf{A}-2\mathbf{I}=\bigl(\begin{smallmatrix}2&1\\2&1\end{smallmatrix}\bigr)$, con la condición $2v_1+v_2=0$; el espacio propio es la recta en la dirección de $(1,\,-2)^{\top}$. Normalizados, los vectores propios son $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ y $\mathbf{v}_2=(1,\,-2)^{\top}/\sqrt5$, como en la fig. [17](#abb-17). No son perpendiculares entre sí: $(1,\,1)(1,\,-2)^{\top}=-1\ne0$.

⁠**En resumen:** Los vectores propios asociados a $\lambda$ son las soluciones $\mathbf{v}\ne\mathbf{0}$ de $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$; junto con el vector nulo forman el espacio propio.

### Traza y determinante

<span class="anker" id="stufe-6-5"></span>

En [(6.3)](#gl-6-3) aparecen dos números que se ven directamente en la matriz: $ad-bc$ es el determinante, y $a+d$ es la suma de las entradas diagonales. Esta suma tiene un nombre propio. Ambos números se relacionan de forma sencilla con los valores propios y sirven, por ello, como comprobación.

:::definition Definición 6.5 (Traza)
<span class="anker" id="satz-6-5"></span>

La __traza__ de una matriz cuadrada $\mathbf{A}\in\mathbb{R}^{n\times n}$ es la suma de sus entradas diagonales:

<span class="anker" id="gl-6-4"></span>
$$\operatorname{tr}\mathbf{A}=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^na_{ii} . \tag{6.4}$$
:::

:::satz Teorema 6.6 (Traza y determinante a partir de los valores propios)
<span class="anker" id="satz-6-6"></span>

Si $\lambda_1,\dots,\lambda_n$ son los valores propios de $\mathbf{A}$, contados con su multiplicidad y como números complejos, entonces

<span class="anker" id="gl-6-5"></span>
$$\operatorname{tr}\mathbf{A}=\lambda_1+\lambda_2+\dots+\lambda_n,\qquad \det\mathbf{A}=\lambda_1\cdot\lambda_2\cdots\lambda_n . \tag{6.5}$$

Además, $\operatorname{tr}(\mathbf{A}\mathbf{B})=\operatorname{tr}(\mathbf{B}\mathbf{A})$ para $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{B}\in\mathbb{R}^{n\times m}$.
:::

:::herleitung Traza y determinante
Para $n=2$: el polinomio $\lambda^2-(a+d)\lambda+(ad-bc)$ se descompone en $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$. Comparando los coeficientes se obtiene $a+d=\lambda_1+\lambda_2$ y $ad-bc=\lambda_1\lambda_2$.

Para $n$ cualquiera, $p(\lambda)$ se descompone igualmente en $(\lambda_1-\lambda)(\lambda_2-\lambda)\cdots(\lambda_n-\lambda)$; el signo es correcto porque en $\det(\mathbf{A}-\lambda\mathbf{I})$ aparece el sumando $(-\lambda)^n$. Si se pone $\lambda=0$, a la izquierda queda $\det\mathbf{A}$ y a la derecha $\lambda_1\cdots\lambda_n$. Para la traza se comparan los coeficientes de $\lambda^{n-1}$. A la derecha son $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$. A la izquierda, en el desarrollo de Laplace, solo el producto de las entradas diagonales $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$ da una potencia de $\lambda$ tan alta, con el coeficiente $(-1)^{n-1}(a_{11}+\dots+a_{nn})$.

Para la última afirmación: $\operatorname{tr}(\mathbf{A}\mathbf{B})=\sum_i(\mathbf{A}\mathbf{B})_{ii}=\sum_i\sum_la_{il}b_{li}$ y $\operatorname{tr}(\mathbf{B}\mathbf{A})=\sum_l\sum_ib_{li}a_{il}$. Es la misma doble suma, solo que ordenada de otra manera.
:::

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ es $\operatorname{tr}\mathbf{A}=7=5+2$ (fig. [18](#abb-18)) y $\det\mathbf{A}=10=5\cdot2$. Para $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ es $\operatorname{tr}=7$ y $\det=6$; los valores propios son, por tanto, las soluciones de $\lambda^2-7\lambda+6=0$, es decir, $6$ y $1$. Para $\mathbf{A}\in\mathbb{R}^{2\times3}$ con las filas $(1,0,2)$, $(0,1,1)$ y $\mathbf{B}=\mathbf{A}^{\top}$, el producto $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ tiene la traza $7$, y $\mathbf{B}\mathbf{A}$ es una matriz $3\times3$ con las entradas diagonales $1$, $1$ y $5$, también con la traza $7$.

:::abbildung ml/k2rspur 18
La traza de $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ como suma de las entradas diagonales; es igual a la suma de los valores propios $5$ y $2$.
:::

⁠**En resumen:** La traza es la suma de las entradas diagonales y la suma de los valores propios; el determinante es el producto de los valores propios.

### Valores propios complejos

<span class="anker" id="stufe-6-6"></span>

Una rotación de $90^\circ$ no deja ninguna flecha sobre su recta: cada una gira un ángulo recto. No puede tener, por tanto, ningún vector propio real. El polinomio característico muestra qué ocurre en su lugar.

⁠**Ejemplo numérico 1:** Para la rotación $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ es $p(\lambda)=\lambda^2+1$, con las raíces $\lambda=\mathrm j$ y $\lambda=-\mathrm j$. Los valores propios son imaginarios puros. A $\lambda=\mathrm j$ le corresponde el vector propio complejo $(1,\,-\mathrm j)^{\top}$, pues $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)(1,\,-\mathrm j)^{\top}=(\mathrm j,\,1)^{\top}=\mathrm j\,(1,\,-\mathrm j)^{\top}$.

⁠**Ejemplo numérico 2:** La rotación $\mathbf{Q}=\bigl(\begin{smallmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{smallmatrix}\bigr)$ de la sección [1.4](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-4) tiene $p(\lambda)=\lambda^2-1{,}2\lambda+1$ y, según el ejemplo numérico sobre los números complejos, los valores propios $0{,}6\pm\mathrm j\,0{,}8=\cos\alpha\pm\mathrm j\sin\alpha=\mathrm e^{\pm\mathrm j\alpha}$ con $\alpha\approx53{,}13^\circ$. En general, la rotación de ángulo $\alpha$ tiene los valores propios $\mathrm e^{\pm\mathrm j\alpha}$.

Una matriz real puede tener, por tanto, valores propios complejos. Como su polinomio característico tiene coeficientes reales, aparecen en pares conjugados. Un vector propio real solo corresponde a un valor propio real: si $\mathbf{v}$ fuera real y $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, entonces $\lambda\mathbf{v}$ sería real como imagen de un vector real y, por tanto, también $\lambda$. Los valores propios complejos indican que la matriz gira en un plano.

⁠**En resumen:** Una matriz real puede tener valores propios complejos, siempre en pares conjugados; una rotación de ángulo $\alpha$ tiene los valores propios $\mathrm e^{\pm\mathrm j\alpha}$.

:::hintergrund Girar es multiplicar por $\mathrm e^{\mathrm j\alpha}$
Para un ingeniero electrotécnico, el resultado es familiar. Se identifica la flecha $(x_1,\,x_2)^{\top}$ con el número complejo $z=x_1+\mathrm jx_2$, como en un fasor. Una rotación de ángulo $\alpha$ es entonces la multiplicación por $\mathrm e^{\mathrm j\alpha}$: $\mathrm e^{\mathrm j\alpha}z=(x_1\cos\alpha-x_2\sin\alpha)+\mathrm j\,(x_1\sin\alpha+x_2\cos\alpha)$, y estas son exactamente las dos componentes de $\mathbf{Q}\mathbf{x}$ para la matriz de rotación de Fundamentos 1, sección 8.3. En la notación compleja, la rotación es, por tanto, una multiplicación por un número, y ese número es un valor propio. El segundo valor propio, $\mathrm e^{-\mathrm j\alpha}$, corresponde a la notación conjugada $z^*$, que gira en sentido contrario.
:::

### Valores propios múltiples

<span class="anker" id="stufe-6-7"></span>

El polinomio característico puede tener una raíz doble. Entonces coinciden dos de los $n$ valores propios. Cuántas veces aparece un valor propio se recoge en un número aparte.

:::definition Definición 6.7 (Multiplicidad algebraica)
<span class="anker" id="satz-6-7"></span>

La __multiplicidad algebraica__ de un valor propio $\lambda$ es la multiplicidad de $\lambda$ como raíz del polinomio característico.
:::

⁠**Ejemplo numérico:** La matriz $2\mathbf{I}=\operatorname{diag}(2;\,2)$ tiene $p(\lambda)=(2-\lambda)^2$: el valor propio $2$ tiene multiplicidad algebraica $2$. La cizalladura $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ de Fundamentos 1, sección 8.3, tiene $p(\lambda)=(1-\lambda)^2$: el valor propio $1$ también tiene multiplicidad algebraica $2$. La matriz $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ tiene dos valores propios distintos, cada uno con multiplicidad algebraica $1$.

⁠**En resumen:** La multiplicidad algebraica cuenta cuántas veces aparece un valor propio como raíz del polinomio característico.

### Cuántos vectores propios hay

<span class="anker" id="stufe-6-8"></span>

Los dos ejemplos con un valor propio doble se comportan de manera muy distinta. La matriz $2\mathbf{I}$ estira cada flecha al doble; todo vector $\ne\mathbf{0}$ es un vector propio, y el espacio propio es todo el plano. La cizalladura desplaza cada punto hacia la derecha tanto como vale su altura; solo las flechas sobre el eje $x_1$ se quedan sobre su recta. Su espacio propio es $\ker\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, la recta en la dirección de $(1,\,0)^{\top}$. La diferencia está en la dimensión del espacio propio.

:::definition Definición 6.8 (Multiplicidad geométrica)
<span class="anker" id="satz-6-8"></span>

La __multiplicidad geométrica__ de un valor propio es la dimensión de su espacio propio.
:::

Es al menos $1$, pues para todo valor propio hay un vector propio, y como mucho igual a la multiplicidad algebraica; esta segunda parte no se demuestra en el capítulo. En $2\mathbf{I}$, ambas multiplicidades son $2$; en la cizalladura, la algebraica es $2$ y la geométrica, $1$: le falta un vector propio.

:::satz Teorema 6.9 (Valores propios distintos, vectores propios independientes)
<span class="anker" id="satz-6-9"></span>

Los vectores propios $\mathbf{v}_1,\dots,\mathbf{v}_k$ asociados a valores propios $\lambda_1,\dots,\lambda_k$ distintos dos a dos son linealmente independientes. Si una matriz $n\times n$ tiene $n$ valores propios distintos, sus vectores propios forman una base.
:::

:::beweis Vectores propios independientes
Para dos vectores propios: sea $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$. Aplicando $\mathbf{A}$ se obtiene $c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2=\mathbf{0}$. Si se resta de ello $\lambda_2$ veces la primera ecuación, queda $c_1(\lambda_1-\lambda_2)\mathbf{v}_1=\mathbf{0}$. Como $\lambda_1\ne\lambda_2$ y $\mathbf{v}_1\ne\mathbf{0}$, es $c_1=0$, y entonces también $c_2=0$. Para más vectores propios se procede del mismo modo: si hubiera una dependencia, se tomaría una con el menor número posible de coeficientes distintos de cero. Aplicar $\mathbf{A}$ y restar la dependencia multiplicada por uno de esos valores propios $\lambda$ daría una dependencia con todavía menos coeficientes distintos de cero, lo que es una contradicción.
:::

⁠**Ejemplo numérico:** Los vectores propios $(1,\,1)^{\top}$ y $(1,\,-2)^{\top}$ de $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ están asociados a los valores propios distintos $5$ y $2$; son linealmente independientes, pues $\det\bigl(\begin{smallmatrix}1&1\\1&-2\end{smallmatrix}\bigr)=-3\ne0$. La cizalladura, en cambio, solo tiene la dirección propia $(1,\,0)^{\top}$; no hay dos vectores propios independientes.

⁠**En resumen:** La multiplicidad geométrica cuenta los vectores propios independientes asociados a un valor propio; puede ser menor que la algebraica, pero valores propios distintos tienen siempre vectores propios independientes.

### Reglas de cálculo para valores propios

<span class="anker" id="stufe-6-9"></span>

Quien conoce los vectores propios de una matriz los conoce también para muchas matrices construidas a partir de ella. Todas las reglas se deducen directamente de [(6.1)](#gl-6-1).

:::satz Teorema 6.10 (Reglas de cálculo)
<span class="anker" id="satz-6-10"></span>

Sea $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ con $\mathbf{v}\ne\mathbf{0}$. Entonces se cumple:

<ol class="rm">

<li>

$\mathbf{A}^k\mathbf{v}=\lambda^k\mathbf{v}$ para todo número natural $k$;

</li>

<li>

$(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=(\lambda+\beta)\mathbf{v}$ para todo número $\beta$;

</li>

<li>

$\mathbf{A}$ es invertible si y solo si ningún valor propio es cero, y en ese caso $\mathbf{A}^{-1}\mathbf{v}=\frac1\lambda\mathbf{v}$;

</li>

<li>

$\mathbf{A}^{\top}$ tiene los mismos valores propios que $\mathbf{A}$, pero en general otros vectores propios.

</li>

</ol>
:::

:::beweis Reglas de cálculo
(i) $\mathbf{A}^2\mathbf{v}=\mathbf{A}(\lambda\mathbf{v})=\lambda\mathbf{A}\mathbf{v}=\lambda^2\mathbf{v}$, y así sucesivamente. (ii) $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=\lambda\mathbf{v}+\beta\mathbf{v}$. (iii) Según [(6.5)](#gl-6-5), $\det\mathbf{A}$ es el producto de los valores propios y, por tanto, es distinto de cero si y solo si ningún valor propio es cero. Si se multiplica $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ por $\mathbf{A}^{-1}$, se obtiene $\mathbf{v}=\lambda\mathbf{A}^{-1}\mathbf{v}$. (iv) Según Fundamentos 1, sección 14.5, es $\det(\mathbf{A}^{\top}-\lambda\mathbf{I})=\det\bigl((\mathbf{A}-\lambda\mathbf{I})^{\top}\bigr)=\det(\mathbf{A}-\lambda\mathbf{I})$; ambas tienen el mismo polinomio característico.
:::

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, la matriz $\mathbf{A}^2=\bigl(\begin{smallmatrix}18&7\\14&11\end{smallmatrix}\bigr)$ tiene los valores propios $25$ y $4$: $\mathbf{A}^2(1,\,1)^{\top}=(25,\,25)^{\top}$. La matriz $\mathbf{A}-5\mathbf{I}$ tiene los valores propios $0$ y $-3$ y no es invertible. La inversa $\mathbf{A}^{-1}=\tfrac1{10}\bigl(\begin{smallmatrix}3&-1\\-2&4\end{smallmatrix}\bigr)$ tiene los valores propios $\tfrac15$ y $\tfrac12$: $\mathbf{A}^{-1}(1,\,-2)^{\top}=\tfrac1{10}(5,\,-10)^{\top}=\tfrac12(1,\,-2)^{\top}$. La traspuesta $\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&2\\1&3\end{smallmatrix}\bigr)$ también tiene los valores propios $5$ y $2$, pero $\mathbf{A}^{\top}(1,\,1)^{\top}=(6,\,4)^{\top}$: sus vectores propios son $(2,\,1)^{\top}$ y $(1,\,-1)^{\top}$.

⁠**En resumen:** Las potencias, los desplazamientos por $\beta\mathbf{I}$ y la inversa conservan los vectores propios y cambian los valores propios de la misma manera; la traspuesta solo conserva los valores propios.

:::aufgabe Ejercicio 17 ★ Valores propios y vectores propios
<span class="anker" id="aufg-17"></span>

Determina los valores propios y los espacios propios de

$$\mathbf{A}_1=\begin{pmatrix}2&2\\1&3\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&1\end{pmatrix}.$$

Comprueba en cada caso la traza y el determinante. ¿En qué matriz son perpendiculares entre sí los vectores propios?

:::loesung
$\mathbf{A}_1$: traza $5$, determinante $6-2=4$; por tanto, $\lambda^2-5\lambda+4=(\lambda-4)(\lambda-1)$. Para $\lambda=4$: $\mathbf{A}_1-4\mathbf{I}=\bigl(\begin{smallmatrix}-2&2\\1&-1\end{smallmatrix}\bigr)$, espacio propio en la dirección de $(1,\,1)^{\top}$. Para $\lambda=1$: $\mathbf{A}_1-\mathbf{I}=\bigl(\begin{smallmatrix}1&2\\1&2\end{smallmatrix}\bigr)$, espacio propio en la dirección de $(2,\,-1)^{\top}$. Comprobación: $4+1=5$, $4\cdot1=4$. Los vectores propios no son perpendiculares: $(1,\,1)(2,\,-1)^{\top}=1$.

$\mathbf{A}_2=3\mathbf{I}$: $p(\lambda)=(3-\lambda)^2$, el valor propio $3$ es doble; el espacio propio es todo el plano. Comprobación: $3+3=6$, $3\cdot3=9$. Se pueden elegir dos vectores propios perpendiculares, por ejemplo $\mathbf{e}_1$ y $\mathbf{e}_2$, pero también dos oblicuos.

$\mathbf{A}_3$: traza $2$, determinante $1-9=-8$; por tanto, $\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$. Vectores propios: $(1,\,1)^{\top}$, asociado a $4$, y $(1,\,-1)^{\top}$, asociado a $-2$. Comprobación: $4-2=2$, $4\cdot(-2)=-8$. Son perpendiculares entre sí; $\mathbf{A}_3$ es simétrica, y la sección [7.5](diagonalisierung-und-spektralsatz.html#stufe-7-5) muestra que no es casualidad.
:::
:::

:::aufgabe Ejercicio 18 ★ Matrices triangulares
<span class="anker" id="aufg-18"></span>

Demuestra: los valores propios de una matriz triangular superior son sus entradas diagonales. Determina los valores propios y los vectores propios de $\Bigl(\begin{smallmatrix}2&1&0\\0&3&1\\0&0&5\end{smallmatrix}\Bigr)$.

:::loesung
Para una matriz triangular superior, $\mathbf{A}-\lambda\mathbf{I}$ es de nuevo una matriz triangular superior, con las entradas diagonales $a_{ii}-\lambda$. Según Fundamentos 1, sección 14.4, su determinante es el producto de las entradas diagonales: $p(\lambda)=(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$. Las raíces son las entradas diagonales.

Para la matriz dada, los valores propios son, por tanto, $2$, $3$ y $5$. Para $2$: $\mathbf{A}-2\mathbf{I}=\Bigl(\begin{smallmatrix}0&1&0\\0&1&1\\0&0&3\end{smallmatrix}\Bigr)$ exige $v_3=0$ y $v_2=0$; vector propio $(1,\,0,\,0)^{\top}$. Para $3$: $\Bigl(\begin{smallmatrix}-1&1&0\\0&0&1\\0&0&2\end{smallmatrix}\Bigr)$ exige $v_3=0$ y $v_2=v_1$; vector propio $(1,\,1,\,0)^{\top}$. Para $5$: $\Bigl(\begin{smallmatrix}-3&1&0\\0&-2&1\\0&0&0\end{smallmatrix}\Bigr)$ exige $v_2=3v_1$ y $v_3=2v_2$; vector propio $(1,\,3,\,6)^{\top}$. Comprobación: $\mathbf{A}(1,\,3,\,6)^{\top}=(2+3,\ 9+6,\ 30)^{\top}=5\,(1,\,3,\,6)^{\top}$.
:::
:::

:::aufgabe Ejercicio 19 ★★ Multiplicidades
<span class="anker" id="aufg-19"></span>

Determina para $\mathbf{B}_1=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$, $\mathbf{B}_2=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ y $\mathbf{B}_3=\Bigl(\begin{smallmatrix}1&0&0\\0&1&1\\0&0&1\end{smallmatrix}\Bigr)$ todos los valores propios con su multiplicidad algebraica y geométrica.

:::loesung
$\mathbf{B}_1=2\mathbf{I}$: valor propio $2$, multiplicidad algebraica $2$; el espacio propio es todo el plano, multiplicidad geométrica $2$.

$\mathbf{B}_2$: matriz triangular, valor propio $2$ con multiplicidad algebraica $2$. $\mathbf{B}_2-2\mathbf{I}=\bigl(\begin{smallmatrix}0&3\\0&0\end{smallmatrix}\bigr)$ exige $v_2=0$; el espacio propio es el eje $x_1$, multiplicidad geométrica $1$. Igual que a la cizalladura, a $\mathbf{B}_2$ le falta un vector propio.

$\mathbf{B}_3$: matriz triangular, valor propio $1$ con multiplicidad algebraica $3$. $\mathbf{B}_3-\mathbf{I}=\Bigl(\begin{smallmatrix}0&0&0\\0&0&1\\0&0&0\end{smallmatrix}\Bigr)$ exige solo $v_3=0$; el espacio propio es $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$, multiplicidad geométrica $2$. Aquí la multiplicidad geométrica está entre $1$ y la algebraica.
:::
:::

:::aufgabe Ejercicio 20 ★★ Una rotación y una reflexión
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

Calcula los valores propios de la rotación de $30^\circ$ y escríbelos en la forma $\mathrm e^{\pm\mathrm j\alpha}$.

</li>

<li>

La reflexión $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ de la sección [1.5](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-5) también es ortogonal. Determina sus valores propios y vectores propios e interprétalos geométricamente.

</li>

<li>

Demuestra: todo valor propio real de una matriz ortogonal es $1$ o $-1$.

</li>

</ol>

:::loesung
(a) La rotación de $30^\circ$ es $\bigl(\begin{smallmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{smallmatrix}\bigr)$, con traza $\sqrt3$ y determinante $1$. Por tanto, $p(\lambda)=\lambda^2-\sqrt3\,\lambda+1$ y

$$\lambda=\frac{\sqrt3\pm\sqrt{3-4}}2=\frac{\sqrt3}2\pm\mathrm j\,\frac12=\cos30^\circ\pm\mathrm j\sin30^\circ=\mathrm e^{\pm\mathrm j\,30^\circ} .$$

(b) Traza $0$, determinante $-0{,}36-0{,}64=-1$; por tanto, $p(\lambda)=\lambda^2-1$, con los valores propios $1$ y $-1$. Para $1$: $\bigl(\begin{smallmatrix}-0{,}4&0{,}8\\0{,}8&-1{,}6\end{smallmatrix}\bigr)$, vector propio $(2,\,1)^{\top}$. Para $-1$: $\bigl(\begin{smallmatrix}1{,}6&0{,}8\\0{,}8&0{,}4\end{smallmatrix}\bigr)$, vector propio $(1,\,-2)^{\top}$. Geométricamente: los puntos del eje de reflexión, que tiene la dirección de $(2,\,1)^{\top}$, quedan fijos, y el valor propio es $1$; la dirección perpendicular a él se invierte, y el valor propio es $-1$. Los dos vectores propios son perpendiculares, porque la matriz es simétrica.

(c) Sea $\mathbf{Q}\mathbf{v}=\lambda\mathbf{v}$ con $\lambda$ real y $\mathbf{v}\ne\mathbf{0}$ real. Según [(1.3)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-3), $\lVert\mathbf{v}\rVert=\lVert\mathbf{Q}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$; por tanto, $|\lambda|=1$ y $\lambda=\pm1$. Un movimiento rígido solo puede dejar una flecha sobre su recta tal como está o invertirla, no estirarla.
:::
:::
