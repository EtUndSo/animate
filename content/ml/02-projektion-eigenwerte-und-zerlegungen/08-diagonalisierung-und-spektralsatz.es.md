---
title: Diagonalización y teorema espectral
pfad: Informática / Aprendizaje automático / Proyección, valores propios y descomposiciones
order: 6220800
summary: Si se describe una matriz en una base formada por sus vectores propios, se vuelve diagonal: cada coordenada solo se multiplica por su valor propio, y los cálculos acoplados se descomponen en cálculos independientes.
tags: cambio de base, diagonalizable, ejes principales
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Si se describe una matriz en una base formada por sus vectores propios, se vuelve diagonal: cada coordenada solo se multiplica por su valor propio, y los cálculos acoplados se descomponen en cálculos independientes. Esta sección muestra cuándo es posible y demuestra que en las matrices simétricas lo es siempre, incluso con una base ortonormal.
:::

### Cambio de base

<span class="anker" id="stufe-7-1"></span>

La misma flecha tiene coordenadas distintas en bases distintas. Del mismo modo, la misma aplicación lineal tiene matrices distintas en coordenadas distintas. Algunas bases hacen que la matriz sea especialmente sencilla.

Sea $\mathbf s_1,\dots,\mathbf s_n$ una base de $\mathbb{R}^n$, y sea $\mathbf{S}$ la matriz con estas columnas. Según la parte 1, sección 13.5, es invertible. Si $\mathbf{x}$ tiene en esta base las coordenadas $\mathbf{c}$, entonces $\mathbf{x}=\sum_ic_i\mathbf s_i=\mathbf{S}\mathbf{c}$ y, a la inversa, $\mathbf{c}=\mathbf{S}^{-1}\mathbf{x}$. Si se transforma $\mathbf{x}$ con $\mathbf{A}$, la imagen $\mathbf{A}\mathbf{x}$ tiene las coordenadas $\mathbf{S}^{-1}\mathbf{A}\mathbf{x}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}\,\mathbf{c}$. En las nuevas coordenadas, la aplicación actúa, por tanto, mediante la matriz $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$: primero se pasa a las coordenadas antiguas, después se aplica la transformación y, por último, se vuelve a las nuevas.

:::definition Definición 7.1 (Cambio de base)
<span class="anker" id="satz-7-1"></span>

Si $\mathbf{S}$ es invertible, $\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ se llama matriz de $\mathbf{A}$ en la base de las columnas de $\mathbf{S}$. El paso de $\mathbf{A}$ a $\mathbf{B}$ se llama __cambio de base__.
:::

Dos matrices relacionadas de este modo se llaman semejantes. Describen la misma aplicación, solo que en coordenadas distintas.

:::satz Teorema 7.2 (Lo que un cambio de base no cambia)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}$ y $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ tienen el mismo polinomio característico y, por tanto, los mismos valores propios, la misma traza y el mismo determinante.
:::

:::beweis Cambio de base
Se tiene $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}-\lambda\mathbf{I}=\mathbf{S}^{-1}(\mathbf{A}-\lambda\mathbf{I})\mathbf{S}$. Según las reglas de cálculo de la parte 1, sección 14.5, su determinante es $\det\mathbf{S}^{-1}\cdot\det(\mathbf{A}-\lambda\mathbf{I})\cdot\det\mathbf{S}=\det(\mathbf{A}-\lambda\mathbf{I})$. Según [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5), la traza y el determinante se obtienen de los valores propios.
:::

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ y la base $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ de la parte 1, sección 13.3, es $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ y $\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$. Entonces

$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}4&5\\2&5\end{pmatrix}=\begin{pmatrix}2&0\\2&5\end{pmatrix}.$$

La traza vuelve a ser $7$, el determinante vuelve a ser $10$, y los valores propios están ahora en la diagonal de una matriz triangular: $2$ y $5$.

⁠**En resumen:** En la base de las columnas de $\mathbf{S}$, la aplicación $\mathbf{A}$ tiene la matriz $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$; los valores propios, la traza y el determinante no cambian.

### Diagonalización

<span class="anker" id="stufe-7-2"></span>

La matriz más sencilla posible es una matriz diagonal: multiplica cada coordenada por su propio factor, sin mezclar las coordenadas. Si se toman como base los vectores propios, cada vector de la base solo se multiplica por su valor propio. En esta base, la matriz es, por tanto, diagonal.

:::satz Teorema 7.3 (Diagonalización)
<span class="anker" id="satz-7-3"></span>

Si $\mathbf{A}\in\mathbb{R}^{n\times n}$ tiene $n$ vectores propios linealmente independientes $\mathbf s_1,\dots,\mathbf s_n$ asociados a los valores propios $\lambda_1,\dots,\lambda_n$, y $\mathbf{S}$ es la matriz con estas columnas, entonces

<span class="anker" id="gl-7-1"></span>
$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad\text{es decir,}\qquad \mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1} . \tag{7.1}$$

A la inversa: si $\mathbf{A}$ puede escribirse así, las columnas de $\mathbf{S}$ son vectores propios.
:::

:::beweis Diagonalización
Según la parte 1, sección 9.2, la columna $i$ de $\mathbf{A}\mathbf{S}$ es el producto $\mathbf{A}\mathbf s_i=\lambda_i\mathbf s_i$, y la columna $i$ de $\mathbf{S}\boldsymbol{\Lambda}$ es también $\lambda_i\mathbf s_i$. Por tanto, $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$. Las columnas de $\mathbf{S}$ son independientes; luego $\mathbf{S}$ es invertible, y multiplicando por $\mathbf{S}^{-1}$ por la izquierda se obtiene [(7.1)](#gl-7-1). Si se lee la misma ecuación $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$ en sentido inverso, se obtiene el recíproco.
:::

Una matriz que puede escribirse así se llama __diagonalizable__. Según el teorema de la sección [6.8](eigenwerte-und-eigenvektoren.html#stufe-6-8), esto ocurre siempre, por ejemplo, cuando los $n$ valores propios son distintos. La cizalladura no es diagonalizable, pues le falta un vector propio. Tampoco la rotación de $90^\circ$ es diagonalizable con números reales, solo con complejos. Ambas son, aun así, invertibles: invertible y diagonalizable son dos propiedades distintas.

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, con los vectores propios $(1,\,1)^{\top}$ y $(1,\,-2)^{\top}$, se tiene

$$\mathbf{S}=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix},\qquad \mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}5&2\\5&-4\end{pmatrix}=\begin{pmatrix}5&0\\0&2\end{pmatrix}.$$

⁠**En resumen:** Una matriz con $n$ vectores propios independientes es diagonal en la base formada por ellos: $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$.

### Desacoplar: potencias y sucesiones

<span class="anker" id="stufe-7-3"></span>

Para qué sirve esto lo muestra una matriz que se aplica una y otra vez. Dos localidades, A y B, intercambian habitantes cada año: el $20\,\%$ de los habitantes de A se muda a B, el $30\,\%$ de los habitantes de B se muda a A, y todos los demás se quedan. Si $\mathbf{x}_k$ son las cifras de habitantes en el año $k$, entonces

$$\mathbf{x}_{k+1}=\mathbf M\mathbf{x}_k\qquad\text{con}\qquad \mathbf M=\begin{pmatrix}0{,}8&0{,}3\\0{,}2&0{,}7\end{pmatrix}.$$

Las dos cifras de habitantes están acopladas: cada cifra nueva depende de las dos antiguas. Al cabo de $k$ años es $\mathbf{x}_k=\mathbf M^k\mathbf{x}_0$. Calcular directamente la potencia $\mathbf M^k$ es laborioso y no muestra qué ocurre a largo plazo. En la base propia es sencillo.

:::satz Teorema 7.4 (Potencias y sucesiones en la base propia)
<span class="anker" id="satz-7-4"></span>

Si $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$, entonces $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$ con $\boldsymbol{\Lambda}^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$. Para la sucesión $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$ se cumple

<span class="anker" id="gl-7-2"></span>
$$\mathbf{x}_k=\sum_{i=1}^nc_i\,\lambda_i^k\,\mathbf s_i\qquad\text{con}\qquad \mathbf{c}=\mathbf{S}^{-1}\mathbf{x}_0 . \tag{7.2}$$
:::

:::beweis Potencias
$\mathbf{A}^2=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\mathbf{S}\boldsymbol{\Lambda}^2\mathbf{S}^{-1}$, porque $\mathbf{S}^{-1}\mathbf{S}=\mathbf{I}$ desaparece en el centro; lo mismo vale para cualquier potencia. Si se descompone $\mathbf{x}_0=\sum_ic_i\mathbf s_i$ en vectores propios, cada aplicación de $\mathbf{A}$ multiplica cada parte solo por su valor propio.
:::

En las coordenadas $\mathbf{c}$ de la base propia, cada paso consiste en multiplicar cada coordenada por su propio número: $c_i\mapsto\lambda_ic_i$. Un cálculo acoplado con $n$ incógnitas se convierte en $n$ cálculos separados con una incógnita cada uno. Estas coordenadas están desacopladas. A largo plazo predomina la parte con el valor propio de mayor módulo.

⁠**Ejemplo numérico:** $\mathbf M$ tiene la traza $1{,}5$ y el determinante $0{,}56-0{,}06=0{,}5$, es decir, los valores propios $1$ y $0{,}5$. Son vectores propios $\mathbf s_1=(3,\,2)^{\top}$, asociado al valor propio $1$, pues $\mathbf M\mathbf s_1=(2{,}4+0{,}6;\ 0{,}6+1{,}4)^{\top}=\mathbf s_1$, y $\mathbf s_2=(1,\,-1)^{\top}$, asociado al valor propio $0{,}5$. Si al principio viven $1000$ personas en A y nadie en B, entonces $\mathbf{x}_0=(1000,\,0)^{\top}=200\,\mathbf s_1+400\,\mathbf s_2$ y, según [(7.2)](#gl-7-2),

$$\mathbf{x}_k=200\begin{pmatrix}3\\2\end{pmatrix}+400\cdot0{,}5^k\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}600+400\cdot0{,}5^k\\400-400\cdot0{,}5^k\end{pmatrix}.$$

Al cabo de un año son $(800,\,200)^{\top}$; al cabo de dos años, $(700,\,300)^{\top}$, y a largo plazo se llega a $(600,\,400)^{\top}$. La parte asociada al valor propio $0{,}5$ se reduce a la mitad cada año; la asociada al valor propio $1$ se mantiene.

⁠**En resumen:** En la base propia, cada potencia de la matriz se convierte en potencias de los valores propios; las sucesiones acopladas se descomponen en sucesiones separadas, una por cada vector propio.

:::hintergrund El mismo principio que en los sistemas LTI y la transformada de Fourier
En el dominio del tiempo, un sistema LTI es una convolución: cada valor de salida depende de todos los valores de entrada; todo está acoplado. Si se descompone la señal de entrada en funciones exponenciales $\mathrm e^{pt}$, cada una solo se multiplica por su valor propio $H(p)$, y el acoplamiento desaparece. La transformada de Laplace y la de Fourier hacen con las señales lo que el cambio de base $\mathbf{S}^{-1}$ hace con los vectores: pasan a las coordenadas de las funciones propias.

Para señales muestreadas, la correspondencia es incluso, literalmente, una diagonalización. Una convolución cíclica $y_k=\sum_lh_{(k-l)\bmod n}\,x_l$ es una matriz cuya primera columna es la respuesta al impulso $(h_0,\dots,h_{n-1})^{\top}$ y cuyas columnas restantes son sus desplazamientos cíclicos. Sus vectores propios son las oscilaciones complejas muestreadas $\mathbf f_m=\bigl(1,\ \mathrm e^{\mathrm j2\pi m/n},\ \mathrm e^{\mathrm j2\pi\cdot2m/n},\dots\bigr)^{\top}$, y el valor propio asociado a $\mathbf f_m$ es el valor $H[m]=\sum_qh_q\,\mathrm e^{-\mathrm j2\pi mq/n}$ de la transformada discreta de Fourier de la respuesta al impulso. La matriz de la transformada discreta de Fourier es, por tanto, salvo el factor $1/n$, la $\mathbf{S}^{-1}$ que diagonaliza toda convolución cíclica, y además para todas las respuestas al impulso a la vez. Ejemplo con $n=3$ y $h=(1;\,0{,}5;\,0)$: la matriz $\Bigl(\begin{smallmatrix}1&0&0{,}5\\0{,}5&1&0\\0&0{,}5&1\end{smallmatrix}\Bigr)$ transforma $\mathbf f_0=(1,1,1)^{\top}$ en $1{,}5\,\mathbf f_0$, y $1{,}5=H[0]=h_0+h_1+h_2$.
:::

### Las matrices simétricas tienen valores propios reales

<span class="anker" id="stufe-7-4"></span>

En las matrices simétricas, muchas cosas son especialmente sencillas. La primera: sus valores propios son siempre reales. Una matriz simétrica no hace girar, por tanto, ningún plano sobre sí mismo, como hacen las rotaciones de la sección [6.6](eigenwerte-und-eigenvektoren.html#stufe-6-6).

:::satz Teorema 7.5 (Valores propios reales)
<span class="anker" id="satz-7-5"></span>

Todo valor propio de una matriz simétrica real es real.
:::

:::beweis Valores propios reales
Sea $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ con $\mathbf{v}\ne\mathbf{0}$, donde $\lambda$ y $\mathbf{v}$ pueden ser, en principio, complejos. Si se conjugan ambos lados, $\mathbf{A}$ no cambia, porque es real: $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$. Se calcula el número $(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}$ de dos maneras. Una vez con $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=\lambda\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Otra vez con $\mathbf{A}=\mathbf{A}^{\top}$ y $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=(\mathbf{A}^{\top}\mathbf{v}^*)^{\top}\mathbf{v}=(\mathbf{A}\mathbf{v}^*)^{\top}\mathbf{v}=\lambda^*\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Por tanto, $(\lambda-\lambda^*)\,(\mathbf{v}^*)^{\top}\mathbf{v}=0$. Según la sección [6.1](eigenwerte-und-eigenvektoren.html#stufe-6-1), $(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0$; por tanto, $\lambda=\lambda^*$, y $\lambda$ es real.
:::

Para un valor propio real hay entonces también vectores propios reales, pues $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ es un sistema de ecuaciones real.

⁠**Ejemplo numérico:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ tiene el polinomio característico $\lambda^2-7\lambda+6$, con el discriminante $49-24=25>0$ y los valores propios reales $6$ y $1$. Para una matriz simétrica $2\times2$ cualquiera $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$, el discriminante es $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$; los valores propios son, por tanto, siempre reales, como dice el teorema.

⁠**En resumen:** Una matriz simétrica solo tiene valores propios reales y vectores propios reales.

### Los vectores propios de las matrices simétricas son perpendiculares

<span class="anker" id="stufe-7-5"></span>

Los vectores propios de $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ eran oblicuos entre sí. En las matrices simétricas, esto no puede ocurrir.

:::satz Teorema 7.6 (Vectores propios ortogonales)
<span class="anker" id="satz-7-6"></span>

Los vectores propios de una matriz simétrica asociados a valores propios distintos son perpendiculares entre sí.
:::

:::beweis Vectores propios ortogonales
Sea $\mathbf{A}\mathbf{v}_1=\lambda_1\mathbf{v}_1$ y $\mathbf{A}\mathbf{v}_2=\lambda_2\mathbf{v}_2$ con $\lambda_1\ne\lambda_2$. Se calcula $\mathbf{v}_1^{\top}\mathbf{A}\mathbf{v}_2$ de dos maneras: como $\mathbf{v}_1^{\top}(\lambda_2\mathbf{v}_2)=\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2$ y, con $\mathbf{A}^{\top}=\mathbf{A}$, como $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\lambda_1\,\mathbf{v}_1^{\top}\mathbf{v}_2$. Por tanto, $(\lambda_1-\lambda_2)\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$, y como $\lambda_1\ne\lambda_2$, es $\mathbf{v}_1^{\top}\mathbf{v}_2=0$.
:::

⁠**Ejemplo numérico:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ tiene, asociado al valor propio $6$, el vector propio $(2,\,1)^{\top}$, pues $(10+2,\ 4+2)^{\top}=6\,(2,\,1)^{\top}$, y, asociado al valor propio $1$, el vector propio $(1,\,-2)^{\top}$, pues $(5-4,\ 2-4)^{\top}=(1,\,-2)^{\top}$. Su producto escalar es $2-2=0$ (fig. [19](#abb-19)).

:::abbildung ml/k2rsenkrecht 19
El producto escalar de los vectores propios $(2,1)^{\top}$, asociado al valor propio $6$, y $(1,-2)^{\top}$, asociado al valor propio $1$, de la matriz simétrica $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$: son perpendiculares entre sí.
:::

⁠**En resumen:** En una matriz simétrica, los vectores propios asociados a valores propios distintos son perpendiculares entre sí.

:::hintergrund Por qué precisamente la simetría hace perpendiculares las direcciones propias
La demostración usa la simetría en un único punto: $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\mathbf{v}_1^{\top}(\mathbf{A}\mathbf{v}_2)$. Para una matriz simétrica, esta ecuación se cumple para todos los vectores; se puede pasar $\mathbf{A}$ de un lado al otro del producto escalar. El producto escalar mide cuánto de $\mathbf{v}_2$ apunta en la dirección de $\mathbf{v}_1$. Si $\mathbf{A}$ estira una dirección por el factor $\lambda_1$ y la otra por el factor $\lambda_2$, esta parte se multiplica a la izquierda por $\lambda_1$ y a la derecha por $\lambda_2$. Ambos lados solo pueden ser iguales si no hay nada que multiplicar, es decir, si la parte es cero. En una matriz no simétrica, esta regla de pasar la matriz al otro lado no vale, y son posibles direcciones propias oblicuas.

De ello se deduce una segunda propiedad importante. Si $\mathbf{q}$ es un vector propio y $\mathbf{z}$ es perpendicular a $\mathbf{q}$, también $\mathbf{A}\mathbf{z}$ es perpendicular a $\mathbf{q}$: $(\mathbf{A}\mathbf{z})^{\top}\mathbf{q}=\mathbf{z}^{\top}\mathbf{A}\mathbf{q}=\lambda\,\mathbf{z}^{\top}\mathbf{q}=0$. Una matriz simétrica transforma, por tanto, el complemento ortogonal de un vector propio en sí mismo. Allí se puede buscar el siguiente vector propio, y así sucesivamente. Exactamente así funciona la demostración de la subsección siguiente.
:::

### El teorema espectral

<span class="anker" id="stufe-7-6"></span>

Los dos teoremas anteriores hacen sospechar que toda matriz simétrica es diagonal en una base ortonormal de vectores propios. Esto es cierto incluso cuando hay valores propios múltiples. El conjunto de los valores propios de una matriz se llama su espectro; de ahí el nombre del teorema.

:::satz Teorema 7.7 (Teorema espectral)
<span class="anker" id="satz-7-7"></span>

Para toda matriz simétrica $\mathbf{A}\in\mathbb{R}^{n\times n}$ existe una base ortonormal $\mathbf{q}_1,\dots,\mathbf{q}_n$ de vectores propios con valores propios reales $\lambda_1,\dots,\lambda_n$. Con la matriz ortogonal $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ y $\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ se tiene

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\sum_{i=1}^n\lambda_i\,\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{7.3}$$
:::

:::beweis Teorema espectral
Se procede paso a paso. Según la sección [6.3](eigenwerte-und-eigenvektoren.html#stufe-6-3), $\mathbf{A}$ tiene al menos un valor propio $\lambda_1$; según la sección [7.4](#stufe-7-4), es real y tiene un vector propio real, que una vez normalizado es $\mathbf{q}_1$. Se completa $\mathbf{q}_1$ hasta una base ortonormal de $\mathbb{R}^n$, por ejemplo con el proceso de Gram-Schmidt aplicado a $\mathbf{q}_1,\mathbf{e}_1,\dots,\mathbf{e}_n$, saltándose los vectores con $\tilde{\mathbf{q}}=\mathbf{0}$. Los vectores restantes de la base forman las columnas de una matriz $\mathbf{W}\in\mathbb{R}^{n\times(n-1)}$, y $\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1&\mathbf{W}\end{pmatrix}$ es ortogonal. Entonces

$$\mathbf{Q}_1^{\top}\mathbf{A}\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{q}_1^{\top}\mathbf{A}\mathbf{W}\\\mathbf{W}^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{W}^{\top}\mathbf{A}\mathbf{W}\end{pmatrix}=\begin{pmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{B}\end{pmatrix}$$

con la matriz simétrica $\mathbf{B}=\mathbf{W}^{\top}\mathbf{A}\mathbf{W}$, de tamaño $(n-1)\times(n-1)$. Los ceros aparecen porque $\mathbf{A}\mathbf{q}_1=\lambda_1\mathbf{q}_1$ es perpendicular a las columnas de $\mathbf{W}$, y arriba a la derecha igualmente, porque $\mathbf{A}$ es simétrica. Con $\mathbf{B}$ se repite lo mismo hasta que queda una matriz $1\times1$. Si de este modo se ha encontrado para $\mathbf{B}$ una matriz ortogonal $\mathbf{Q}_B$ con la que $\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B$ es diagonal, entonces $\mathbf{Q}=\mathbf{Q}_1\bigl(\begin{smallmatrix}1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B\end{smallmatrix}\bigr)$ es ortogonal como producto de matrices ortogonales, y $\mathbf{Q}^{\top}\mathbf{A}\mathbf{Q}=\bigl(\begin{smallmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B\end{smallmatrix}\bigr)=\boldsymbol{\Lambda}$ es diagonal. Como $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, se sigue $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. La forma de suma se deduce de la parte 1, sección 9.5, pues $\mathbf{Q}\boldsymbol{\Lambda}$ tiene las columnas $\lambda_i\mathbf{q}_i$.
:::

Cada sumando $\mathbf{q}_i\mathbf{q}_i^{\top}$ es, según la sección [2.3](projektion-auf-eine-gerade.html#stufe-2-3), la proyección sobre la recta en la dirección de $\mathbf{q}_i$. Una matriz simétrica es, por tanto, una suma de proyecciones sobre ejes perpendiculares, cada una ponderada con su valor propio. En un valor propio múltiple, la elección de los $\mathbf{q}_i$ en su espacio propio es libre: cualquier base ortonormal del espacio propio sirve. También el signo de cada $\mathbf{q}_i$ es libre. Algunos libros ordenan los valores propios de forma decreciente; otros no.

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ y $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$ son los vectores propios normalizados asociados a $6$ y $1$. Entonces

$$6\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}+1\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\frac15\begin{pmatrix}25&10\\10&10\end{pmatrix}=\begin{pmatrix}5&2\\2&2\end{pmatrix}.$$

⁠**En resumen:** Toda matriz simétrica es $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$: diagonal en un sistema de ejes convenientemente girado, una suma ponderada de proyecciones sobre ejes perpendiculares.

:::hintergrund De dónde salen las matrices simétricas
Las matrices simétricas aparecen siempre que una matriz describe relaciones entre pares que no dependen del orden. Las matrices de Gram $\mathbf{X}^{\top}\mathbf{X}$ y $\mathbf{X}\mathbf{X}^{\top}$ de la parte 1, sección 10, contienen productos escalares, y $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$. La matriz de una forma cuadrática puede elegirse siempre simétrica, según la sección [5.2](quadratische-formen.html#stufe-5-2). La matriz de inductancias de unas bobinas acopladas es simétrica, porque la inductancia mutua de la bobina 1 sobre la bobina 2 es la misma que a la inversa. Para todas estas matrices, el teorema espectral garantiza valores propios reales y direcciones propias perpendiculares.
:::

### Ejes principales

<span class="anker" id="stufe-7-7"></span>

En la sección [5.3](quadratische-formen.html#stufe-5-3), la forma de una forma cuadrática era fácil de reconocer mientras su matriz fuera diagonal. El teorema espectral hace diagonal toda matriz simétrica si se giran las coordenadas adecuadamente. Con ello desaparecen los términos cruzados.

:::satz Teorema 7.8 (Ejes principales de una forma cuadrática)
<span class="anker" id="satz-7-8"></span>

Si $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ y $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ son las coordenadas de $\mathbf{x}$ en la base propia, entonces

<span class="anker" id="gl-7-4"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_1c_1^2+\lambda_2c_2^2+\dots+\lambda_nc_n^2 . \tag{7.4}$$
:::

:::beweis Ejes principales
Con $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ es $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}\mathbf{x}=\mathbf{c}^{\top}\boldsymbol{\Lambda}\mathbf{c}=\sum_i\lambda_ic_i^2$.
:::

Por eso, las direcciones de los vectores propios se llaman __ejes principales__ de la forma cuadrática. Si todos los valores propios son positivos, la curva de nivel $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=1$ es una elipse; en $\mathbb{R}^3$, un elipsoide. Sus ejes están en las direcciones $\mathbf{q}_i$, y el semieje en la dirección de $\mathbf{q}_i$ tiene la longitud $1/\sqrt{\lambda_i}$, pues para $\mathbf{x}=t\,\mathbf{q}_i$ es $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_it^2=1$ exactamente cuando $t=\pm1/\sqrt{\lambda_i}$. Un valor propio grande corresponde a una dirección de mucha pendiente y a un semieje corto.

:::abbildung ml/k2ellipse 20
Las curvas de nivel $5x_1^2+4x_1x_2+2x_2^2=1$ (azul) y $=\tfrac14$ (azul claro) son elipses. Sus ejes (gris) están en las direcciones de los vectores propios $\mathbf{q}_1=(2,1)^{\top}/\sqrt5$, asociado al valor propio $6$, y $\mathbf{q}_2=(1,-2)^{\top}/\sqrt5$, asociado al valor propio $1$. Los semiejes de la elipse exterior son $1/\sqrt6\approx0{,}41$ (rojo) y $1/\sqrt1=1$ (verde): en la dirección del valor propio grande, la forma sube con más pendiente, y la elipse es allí más estrecha.
:::

⁠**Ejemplo numérico:** Para $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$, las coordenadas en la base propia son $c_1=(2x_1+x_2)/\sqrt5$ y $c_2=(x_1-2x_2)/\sqrt5$, y

$$5x_1^2+4x_1x_2+2x_2^2=6\,c_1^2+c_2^2=\tfrac65(2x_1+x_2)^2+\tfrac15(x_1-2x_2)^2 .$$

Desarrollado, el lado derecho da $\tfrac15\bigl(24x_1^2+24x_1x_2+6x_2^2+x_1^2-4x_1x_2+4x_2^2\bigr)=5x_1^2+4x_1x_2+2x_2^2$. La curva de nivel $f=1$ es la elipse de la fig. [20](#abb-20), con los semiejes $1/\sqrt6\approx0{,}408$ y $1$.

⁠**En resumen:** En la base propia, toda forma cuadrática se convierte en la suma $\sum_i\lambda_ic_i^2$, sin términos cruzados; los vectores propios son los ejes principales de sus elipses, y los semiejes son $1/\sqrt{\lambda_i}$.

:::hintergrund Dos maneras de completar cuadrados
En la sección [5.4](quadratische-formen.html#stufe-5-4), la misma forma podía escribirse también como $5(x_1+0{,}4x_2)^2+1{,}2x_2^2$. Los factores $5$ y $1{,}2$ de allí son números distintos de los valores propios $6$ y $1$ de aquí. Ambas descomposiciones son correctas, pero las nuevas coordenadas son distintas: al completar cuadrados, $x_1+0{,}4x_2$ y $x_2$ son coordenadas oblicuas; en el teorema espectral, $c_1,c_2$ son coordenadas en un sistema de ejes rectangular girado. Solo la segunda descomposición muestra los ejes de la elipse. Ambas tienen en común otra cosa: el número de factores positivos, negativos y nulos es el mismo. Esto vale para toda descomposición de una forma cuadrática en una suma de cuadrados de coordenadas independientes; el teorema se llama ley de inercia de Sylvester. Por eso, completar cuadrados y los valores propios llevan siempre al mismo veredicto sobre cuenco, canal o silla.
:::

:::aufgabe Ejercicio 21 ★ Diagonalizar
<span class="anker" id="aufg-21"></span>

Sea $\mathbf{A}=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$ del ejercicio [17](eigenwerte-und-eigenvektoren.html#aufg-17).

<ol class="al">

<li>

Da $\mathbf{S}$ y $\boldsymbol{\Lambda}$ con $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ y comprueba la ecuación.

</li>

<li>

Calcula $\mathbf{A}^3$ una vez directamente y otra como $\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}$.

</li>

</ol>

:::loesung
(a) Del ejercicio [17](eigenwerte-und-eigenvektoren.html#aufg-17): valores propios $4$ y $1$, con los vectores propios $(1,\,1)^{\top}$ y $(2,\,-1)^{\top}$. Por tanto,

$$\mathbf{S}=\begin{pmatrix}1&2\\1&-1\end{pmatrix},\qquad \boldsymbol{\Lambda}=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}1&2\\1&-1\end{pmatrix},$$

pues $\det\mathbf{S}=-3$. Comprobación: $\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}4&2\\4&-1\end{smallmatrix}\bigr)\cdot\tfrac13\bigl(\begin{smallmatrix}1&2\\1&-1\end{smallmatrix}\bigr)=\tfrac13\bigl(\begin{smallmatrix}6&6\\3&9\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$.

(b) Directamente: $\mathbf{A}^2=\bigl(\begin{smallmatrix}6&10\\5&11\end{smallmatrix}\bigr)$ y $\mathbf{A}^3=\mathbf{A}^2\mathbf{A}=\bigl(\begin{smallmatrix}12+10&12+30\\10+11&10+33\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}22&42\\21&43\end{smallmatrix}\bigr)$. A través de la base propia: $\boldsymbol{\Lambda}^3=\operatorname{diag}(64;\,1)$, $\mathbf{S}\boldsymbol{\Lambda}^3=\bigl(\begin{smallmatrix}64&2\\64&-1\end{smallmatrix}\bigr)$ y

$$\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}=\frac13\begin{pmatrix}64+2&128-2\\64-1&128+1\end{pmatrix}=\begin{pmatrix}22&42\\21&43\end{pmatrix}.$$

Para potencias grandes, el segundo camino es mucho más corto: solo se elevan a la potencia los valores propios.
:::
:::

:::aufgabe Ejercicio 22 ★★ Desacoplar una sucesión
<span class="anker" id="aufg-22"></span>

Los números de Fibonacci $0,1,1,2,3,5,\dots$ cumplen $F_{k+2}=F_{k+1}+F_k$. Con $\mathbf{x}_k=(F_{k+1},\,F_k)^{\top}$ es $\mathbf{x}_{k+1}=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\mathbf{x}_k$.

<ol class="al">

<li>

Determina los valores propios y los vectores propios de la matriz.

</li>

<li>

Deduce con [(7.2)](#gl-7-2) una fórmula para $F_k$ y compruébala para $k=5$.

</li>

<li>

¿Cómo se comporta $F_{k+1}/F_k$ para $k$ grande, y por qué?

</li>

</ol>

:::loesung
(a) $p(\lambda)=\lambda^2-\lambda-1$, con las raíces $\varphi=\tfrac{1+\sqrt5}2\approx1{,}618$ y $\psi=\tfrac{1-\sqrt5}2\approx-0{,}618$. La primera fila de $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ es $(1-\lambda)v_1+v_2=0$; la segunda, $v_1-\lambda v_2=0$, es equivalente a ella porque $p(\lambda)=0$. Son vectores propios $\mathbf s_1=(\varphi,\,1)^{\top}$ y $\mathbf s_2=(\psi,\,1)^{\top}$.

(b) $\mathbf{x}_0=(F_1,\,F_0)^{\top}=(1,\,0)^{\top}=c_1\mathbf s_1+c_2\mathbf s_2$ exige $c_1+c_2=0$ y $c_1\varphi+c_2\psi=1$; por tanto, $c_1=1/(\varphi-\psi)=1/\sqrt5$ y $c_2=-1/\sqrt5$. Según [(7.2)](#gl-7-2), $\mathbf{x}_k=\tfrac1{\sqrt5}(\varphi^k\mathbf s_1-\psi^k\mathbf s_2)$; la segunda componente es

$$F_k=\frac{\varphi^k-\psi^k}{\sqrt5} .$$

Para $k=5$: $\varphi^5=\tfrac{11+5\sqrt5}2$ y $\psi^5=\tfrac{11-5\sqrt5}2$; por tanto, $F_5=\tfrac{5\sqrt5}{\sqrt5}=5$. Numéricamente: $\varphi^5\approx11{,}090$, $\psi^5\approx-0{,}090$, $(11{,}090+0{,}090)/2{,}236\approx5{,}000$.

(c) Como $|\psi|<1$, $\psi^k$ tiende a cero, y $F_{k+1}/F_k$ tiende a $\varphi\approx1{,}618$, la razón áurea. Se impone la componente asociada al valor propio de mayor valor absoluto, como en la sección [7.3](#stufe-7-3); cada paso adicional la multiplica por $\varphi$.
:::
:::

:::aufgabe Ejercicio 23 ★★ Descomposición espectral
<span class="anker" id="aufg-23"></span>

<ol class="al">

<li>

Escribe $\mathbf{A}=\bigl(\begin{smallmatrix}3&4\\4&-3\end{smallmatrix}\bigr)$ como $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ y como suma $\lambda_1\mathbf{q}_1\mathbf{q}_1^{\top}+\lambda_2\mathbf{q}_2\mathbf{q}_2^{\top}$.

</li>

<li>

Determina los ejes principales de la forma $3x_1^2+8x_1x_2-3x_2^2$ y escríbela como $\lambda_1c_1^2+\lambda_2c_2^2$. ¿Qué forma básica de la sección [5.3](quadratische-formen.html#stufe-5-3) se tiene?

</li>

<li>

La matriz $\Bigl(\begin{smallmatrix}2&0&0\\0&3&1\\0&1&3\end{smallmatrix}\Bigr)$ tiene el valor propio $2$ doble. Da una base ortonormal de vectores propios. ¿Es única?

</li>

</ol>

:::loesung
(a) Traza $0$, determinante $-9-16=-25$; por tanto, $\lambda^2-25=0$ y $\lambda=\pm5$. Para $5$: $\bigl(\begin{smallmatrix}-2&4\\4&-8\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$. Para $-5$: $\bigl(\begin{smallmatrix}8&4\\4&2\end{smallmatrix}\bigr)$, $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$. Con $\mathbf{Q}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$ y $\boldsymbol{\Lambda}=\operatorname{diag}(5;\,-5)$ es $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$, y

$$5\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}-5\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\begin{pmatrix}3&4\\4&-3\end{pmatrix}.$$

(b) La forma tiene exactamente esta matriz. Con $c_1=(2x_1+x_2)/\sqrt5$ y $c_2=(x_1-2x_2)/\sqrt5$ es

$$3x_1^2+8x_1x_2-3x_2^2=5c_1^2-5c_2^2=(2x_1+x_2)^2-(x_1-2x_2)^2 ,$$

como se ve desarrollando los cuadrados: $4x_1^2+4x_1x_2+x_2^2-x_1^2+4x_1x_2-4x_2^2$. Los ejes principales apuntan en las direcciones $(2,\,1)^{\top}$ y $(1,\,-2)^{\top}$. Un valor propio positivo y otro negativo: una silla cuyos ejes están girados respecto a los ejes de coordenadas.

(c) $\mathbf{e}_1$ es un vector propio asociado a $2$. El bloque inferior $\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ tiene los valores propios $4$, con $(1,\,1)^{\top}$, y $2$, con $(1,\,-1)^{\top}$. Por tanto, una base ortonormal de vectores propios es

$$\mathbf{e}_1,\qquad \tfrac1{\sqrt2}(0,\,1,\,-1)^{\top}\quad\text{para }2,\qquad \tfrac1{\sqrt2}(0,\,1,\,1)^{\top}\quad\text{para }4 .$$

No es única. El espacio propio asociado a $2$ es el plano generado por $\mathbf{e}_1$ y $(0,\,1,\,-1)^{\top}$, y cualquier base ortonormal de este plano sirve, por ejemplo $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1+\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$ y $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1-\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$. Solo el vector propio asociado al valor propio simple $4$ es único salvo el signo.
:::
:::
