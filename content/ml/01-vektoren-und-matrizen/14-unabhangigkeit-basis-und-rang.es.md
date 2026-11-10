---
title: Independencia, base y rango
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Capítulo 1: Vectores y matrices
nachschlagen: ja
order: 15211400
summary: Algunos vectores de una lista no aportan nada nuevo, porque pueden componerse a partir de los demás.
tags: espacio generado, linealmente independientes, linealmente dependientes, base, dimensión, base canónica, rango, rango completo
lang: es
---

<span class="anker" id="stufe-13"></span>

:::zweck
Algunos vectores de una lista no aportan nada nuevo, porque pueden componerse a partir de los demás. Esta sección mide cuántas direcciones realmente distintas hay en una matriz y muestra qué significa para los datos que varias características lleven dos veces la misma información.
:::

### El espacio generado

<span class="anker" id="stufe-13-1"></span>

El espacio columna de una matriz es el conjunto de todas las combinaciones lineales de sus columnas. La misma construcción da un conjunto para cualquier lista de vectores, y este recibe un nombre propio (fig. [39](#abb-39)).

:::abbildung ml/k1spann 39
El espacio generado (azul) por tres listas de vectores en el plano, a escala $1:2$. (a) Un vector genera una recta que pasa por el origen. (b) Un segundo vector en la misma recta no cambia nada. (c) Dos vectores en direcciones distintas generan todo el plano.
:::

:::definition Definición 13.1 (Espacio generado)
<span class="anker" id="satz-13-1"></span>

El __espacio generado__ por los vectores $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ es el conjunto de todas sus combinaciones lineales:

<span class="anker" id="gl-13-1"></span>
$$\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}=\Bigl\{\sum_{l=1}^kc_l\,\mathbf{v}_l\ :\ c_1,\dots,c_k\in\mathbb{R}\Bigr\}. \tag{13.1}$$
:::

El espacio columna de una matriz es, por tanto, el espacio generado por sus columnas. Si dos vectores están en el espacio generado, también lo está cualquier combinación lineal de ellos; sumando y multiplicando por números nunca se sale de él.

::::beispiel [Ejemplo numérico]
$\operatorname{span}\{(1,\,2)^{\top}\}$ es la recta de todos los múltiplos $c\,(1,\,2)^{\top}$. El espacio generado por $(1,\,2)^{\top}$ y $(2,\,4)^{\top}$ es la misma recta, pues $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. El espacio generado por $(1,\,0)^{\top}$ y $(1,\,1)^{\top}$ es todo el plano: todo vector $(y_1,\,y_2)^{\top}$ es $(y_1-y_2)\,(1,\,0)^{\top}+y_2\,(1,\,1)^{\top}$. En $\mathbb{R}^3$, $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ es el plano de todos los vectores con $x_3=0$.
::::

⁠**En resumen:** El espacio generado por una lista de vectores es todo lo que puede obtenerse combinándolos linealmente.

### Independencia lineal

<span class="anker" id="stufe-13-2"></span>

En la fig. [39](#abb-39) (b), el segundo vector no aporta nada nuevo: ya está en el espacio generado por el primero. Un conjunto de datos puede tener la misma debilidad. Si contiene el número de dormitorios, el número de salones y el número total de habitaciones, la tercera columna es la suma de las dos primeras y no lleva información propia. Hace falta una palabra para decir que en una lista de vectores nada sobra.

:::definition Definición 13.2 (Independencia lineal)
<span class="anker" id="satz-13-2"></span>

Los vectores $\mathbf{v}_1,\dots,\mathbf{v}_k$ se llaman __linealmente independientes__ si

<span class="anker" id="gl-13-2"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\mathbf{0} \tag{13.2}$$

solo se cumple para $c_1=c_2=\dots=c_k=0$. En caso contrario se llaman __linealmente dependientes__.
:::

Que sean linealmente dependientes significa, de forma equivalente, que al menos uno de los vectores es una combinación lineal de los demás. En efecto, si se cumple [(13.2)](#gl-13-2) con un coeficiente $c_l\ne0$, se puede despejar $\mathbf{v}_l$: $\mathbf{v}_l=-\sum_{l'\ne l}(c_{l'}/c_l)\,\mathbf{v}_{l'}$. A la inversa, una representación así da de inmediato una combinación con el coeficiente $-1$ delante de $\mathbf{v}_l$.

::::beispiel [Ejemplo numérico]
$(1,\,2)^{\top}$ y $(2,\,4)^{\top}$ son linealmente dependientes: $2\,(1,\,2)^{\top}-(2,\,4)^{\top}=\mathbf{0}$. Los vectores $(1,\,0)^{\top}$ y $(1,\,1)^{\top}$ son linealmente independientes: de $c_1(1,\,0)^{\top}+c_2(1,\,1)^{\top}=(c_1+c_2,\ c_2)^{\top}=\mathbf{0}$ se sigue primero $c_2=0$ y luego $c_1=0$. Los tres vectores $(1,\,0,\,1)^{\top}$, $(0,\,1,\,1)^{\top}$ y $(1,\,1,\,2)^{\top}$ son linealmente dependientes, pues el tercero es la suma de los dos primeros.
::::

⁠**En resumen:** Linealmente independientes significa que ninguno de los vectores puede obtenerse combinando los demás: no hay redundancia.

### Base y dimensión

<span class="anker" id="stufe-13-3"></span>

Si se quiere describir un espacio generado de la forma más concisa posible, se toman tan pocos vectores como sea necesario, pero suficientes para alcanzarlo todo. Una lista así es como un sistema de coordenadas: cada vector del espacio generado tiene entonces exactamente una representación mediante ella.

:::definition Definición 13.3 (Base, dimensión)
<span class="anker" id="satz-13-3"></span>

Una lista de vectores linealmente independientes cuyo espacio generado es un conjunto $\mathcal S$ se llama una __base__ de $\mathcal S$. El número de vectores de una base se llama la __dimensión__ de $\mathcal S$ y se escribe $\dim\mathcal S$.
:::

Un conjunto $\mathcal S$ tiene muchas bases distintas, pero todas constan del mismo número de vectores; es un teorema del álgebra lineal en el que se basa la definición de la dimensión. Los vectores unitarios $\mathbf{e}_1,\dots,\mathbf{e}_d$ forman una base de $\mathbb{R}^d$, la __base canónica__; por eso, $\dim\mathbb{R}^d=d$.

:::satz Teorema 13.4 (Coordenadas únicas)
<span class="anker" id="satz-13-4"></span>

Si $\mathbf{v}_1,\dots,\mathbf{v}_k$ es una base de $\mathcal S$, todo vector $\mathbf{x}\in\mathcal S$ tiene exactamente una representación $\mathbf{x}=\sum_lc_l\mathbf{v}_l$.
:::

:::beweis Coordenadas únicas
Al menos una representación existe, porque la base genera $\mathcal S$. Si hubiera dos, $\sum_lc_l\mathbf{v}_l=\sum_lc_l'\mathbf{v}_l$, su diferencia sería $\sum_l(c_l-c_l')\mathbf{v}_l=\mathbf{0}$. Por la independencia lineal, entonces todos los $c_l-c_l'=0$.
:::

::::beispiel [Ejemplo numérico]
$(1,\,0)^{\top}$ y $(1,\,1)^{\top}$ forman una base de $\mathbb{R}^2$: son linealmente independientes y generan el plano. El vector $(3,\,2)^{\top}$ tiene en esta base las coordenadas $1$ y $2$, pues $(3,\,2)^{\top}=1\cdot(1,\,0)^{\top}+2\cdot(1,\,1)^{\top}$. La recta $\operatorname{span}\{(0,\,1)^{\top}\}$ tiene dimensión $1$, aunque sus vectores tienen dos componentes.
::::

⁠**En resumen:** Una base es una lista de vectores independientes que lo genera todo; su longitud es la dimensión.

### El rango de una matriz

<span class="anker" id="stufe-13-4"></span>

Una matriz con $n$ columnas puede contener menos de $n$ direcciones realmente distintas. El número de direcciones que quedan cuando se deja fuera todo lo superfluo dice lo que una matriz es capaz de hacer en realidad.

:::definition Definición 13.5 (Rango)
<span class="anker" id="satz-13-5"></span>

El __rango__ $\operatorname{rango}\mathbf{A}$ de una matriz $\mathbf{A}$ es el mayor número de columnas linealmente independientes de $\mathbf{A}$. Es igual a la dimensión de su espacio columna.
:::

:::satz Teorema 13.6 (Rango por columnas igual a rango por filas)
<span class="anker" id="satz-13-6"></span>

El mayor número de columnas linealmente independientes de una matriz es igual al mayor número de filas linealmente independientes. En particular, $\operatorname{rango}\mathbf{A}=\operatorname{rango}\mathbf{A}^{\top}\le\min(m,n)$ para $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

Si $\operatorname{rango}\mathbf{A}=\min(m,n)$, $\mathbf{A}$ tiene __rango completo__. En la práctica, el rango se determina con la eliminación gaussiana: las operaciones de filas no lo cambian, y en la forma escalonada es el número de filas que no constan solo de ceros.

::::beispiel [Ejemplo numérico]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ tiene rango $1$: la segunda columna es el doble de la primera, e igualmente la segunda fila es el doble de la primera. Para

$$\mathbf K=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$$

se restan la primera y la segunda fila de la tercera y se obtienen las filas $(1,0,1)$, $(0,1,1)$, $(0,0,0)$. Dos filas no son nulas, así que $\operatorname{rango}\mathbf K=2$; en efecto, la tercera columna es la suma de las dos primeras. La matriz de datos de las viviendas tiene rango completo, $3$.
::::

⁠**En resumen:** El rango cuenta cuántas direcciones realmente distintas hay en las columnas de una matriz, y son exactamente tantas como en sus filas.

:::hintergrund Por qué hay exactamente tantas filas independientes como columnas independientes
No es evidente: las filas y las columnas de una matriz $3\times5$ viven en espacios completamente distintos. Un argumento breve es el siguiente. Sean $r$ columnas de $\mathbf{A}$ linealmente independientes, y sea cada una de las demás columnas una combinación lineal de ellas. Estas $r$ columnas forman una matriz $\mathbf G\in\mathbb{R}^{m\times r}$. Cada columna $\mathbf{a}_j$ de $\mathbf{A}$ es entonces $\mathbf G$ por un vector de coeficientes con $r$ componentes. Si se escriben estos vectores de coeficientes como columnas de una matriz $\mathbf F\in\mathbb{R}^{r\times n}$, según [(9.2)](das-matrixprodukt.html#gl-9-2) se tiene $\mathbf{A}=\mathbf G\mathbf F$. Ahora se lee el mismo producto por filas: la fila $i$ de $\mathbf{A}$ es la fila $i$ de $\mathbf G$ por $\mathbf F$, es decir, una combinación lineal de las $r$ filas de $\mathbf F$. Todas las filas de $\mathbf{A}$ están, por tanto, en el espacio generado por las $r$ filas de $\mathbf F$, un conjunto de dimensión $r$ como mucho, y por eso no puede haber más de $r$ de ellas linealmente independientes. Las filas tienen, por tanto, como mucho tantas direcciones independientes como las columnas. Si se aplica el mismo argumento a $\mathbf{A}^{\top}$, cuyas columnas son las filas de $\mathbf{A}$, se sigue la desigualdad inversa. Ambos números son, por tanto, iguales.
:::

### El núcleo y el teorema del rango

<span class="anker" id="stufe-13-5"></span>

Una matriz con $n$ columnas recibe vectores de $n$ direcciones. Una parte de estas direcciones llega al resultado; el resto va a parar al vector nulo y se pierde. Las direcciones perdidas forman un conjunto propio.

:::definition Definición 13.7 (Núcleo)
<span class="anker" id="satz-13-7"></span>

El __núcleo__ de una matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ es el conjunto de todos los vectores que $\mathbf{A}$ lleva al vector nulo:

<span class="anker" id="gl-13-3"></span>
$$\ker\mathbf{A}=\{\mathbf{x}\in\mathbb{R}^n:\ \mathbf{A}\mathbf{x}=\mathbf{0}\} . \tag{13.3}$$
:::

El núcleo es el conjunto de soluciones del sistema homogéneo de la subsección [12.4](lineare-gleichungssysteme.html#stufe-12-4). Siempre contiene el vector nulo y, si contiene dos vectores, contiene también cualquier combinación lineal de ellos; se puede hablar, por tanto, de su dimensión.

:::satz Teorema 13.8 (Teorema del rango)
<span class="anker" id="satz-13-8"></span>

Para toda matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$ se cumple

<span class="anker" id="gl-13-4"></span>
$$\dim\ker\mathbf{A}+\operatorname{rango}\mathbf{A}=n . \tag{13.4}$$
:::

Las $n$ direcciones de la entrada se reparten: lo que no llega al resultado acaba en el núcleo. En la eliminación gaussiana se ve así: en la forma escalonada hay $\operatorname{rango}\mathbf{A}$ pivotes. Las $n-\operatorname{rango}\mathbf{A}$ incógnitas restantes no tienen pivote propio y pueden elegirse libremente en el sistema homogéneo. Cada una de ellas da una dirección del núcleo.

:::satz Teorema 13.9 (Cuándo es invertible una matriz cuadrada)
<span class="anker" id="satz-13-9"></span>

Para $\mathbf{A}\in\mathbb{R}^{n\times n}$ son equivalentes: (i) $\mathbf{A}$ es invertible; (ii) $\ker\mathbf{A}=\{\mathbf{0}\}$; (iii) $\operatorname{rango}\mathbf{A}=n$; (iv) las columnas de $\mathbf{A}$ son linealmente independientes.
:::

:::beweis Invertibilidad
De (i) se sigue (ii) según la subsección [11.5](einheitsmatrix-und-inverse.html#stufe-11-5). (ii), (iii) y (iv) son equivalentes según el teorema del rango y la definición del rango. Queda por ver que de (iii) y (ii) se sigue (i). Si $\operatorname{rango}\mathbf{A}=n$, el espacio columna es un espacio de dimensión $n$ en $\mathbb{R}^n$, es decir, todo $\mathbb{R}^n$. Por eso, todo sistema $\mathbf{A}\mathbf{c}_j=\mathbf{e}_j$ tiene solución, y las soluciones forman las columnas de una matriz $\mathbf{C}$ con $\mathbf{A}\mathbf{C}=\mathbf{I}$. Además, $\mathbf{A}(\mathbf{C}\mathbf{A}-\mathbf{I})=\mathbf{A}\mathbf{C}\mathbf{A}-\mathbf{A}=\mathbf 0$. Cada columna de $\mathbf{C}\mathbf{A}-\mathbf{I}$ está, por tanto, en el núcleo, que según (ii) solo contiene el vector nulo. Así que también $\mathbf{C}\mathbf{A}=\mathbf{I}$, y $\mathbf{C}=\mathbf{A}^{-1}$.
:::

::::beispiel [Ejemplo numérico]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ tiene el núcleo $\operatorname{span}\{(2,\,-1)^{\top}\}$, de dimensión $1$, y el rango $1$: $1+1=2$. La matriz $\mathbf K$ de antes tiene el núcleo $\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$, pues su tercera columna es la suma de las dos primeras; con $\operatorname{rango}\mathbf K=2$ se tiene $1+2=3$.
::::

**Rango y existencia de solución.** Con el rango y el núcleo, las preguntas de la sección [12](lineare-gleichungssysteme.html#stufe-12) se responden con números, también para matrices que no son cuadradas. ¿Hay alguna solución? ¿Es única? ¿Hay una para cada lado derecho?

:::satz Teorema 13.10 (Existencia de solución y rango)
<span class="anker" id="satz-13-10"></span>

Para $\mathbf{A}\in\mathbb{R}^{m\times n}$ y $\mathbf{y}\in\mathbb{R}^m$ se cumple:

<ol class="rm">

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ tiene solución si y solo si $\operatorname{rango}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rango}\mathbf{A}$;

</li>

<li>

si el sistema tiene solución, esta es única si y solo si $\operatorname{rango}\mathbf{A}=n$;

</li>

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ tiene solución para todo $\mathbf{y}\in\mathbb{R}^m$ si y solo si $\operatorname{rango}\mathbf{A}=m$.

</li>

</ol>
:::

:::beweis Existencia de solución y rango
(i) Según la subsección [12.2](lineare-gleichungssysteme.html#stufe-12-2), el sistema tiene solución si y solo si $\mathbf{y}$ está en el espacio columna de $\mathbf{A}$. Si $\mathbf{y}$ está en él, la columna adicional no aporta ninguna dirección nueva: las columnas de $(\mathbf{A}\,|\,\mathbf{y})$ generan el mismo espacio que las de $\mathbf{A}$, y ambos rangos son su dimensión. Si $\mathbf{y}$ no está en él, se toman $r=\operatorname{rango}\mathbf{A}$ columnas linealmente independientes $\mathbf g_1,\dots,\mathbf g_r$ de $\mathbf{A}$ y, además, $\mathbf{y}$. De $c_1\mathbf g_1+\dots+c_r\mathbf g_r+c\,\mathbf{y}=\mathbf{0}$ se sigue $c=0$, pues de lo contrario $\mathbf{y}$ sería una combinación lineal de los $\mathbf g_l$ y estaría en el espacio columna; entonces también todos los $c_l=0$. Así que $(\mathbf{A}\,|\,\mathbf{y})$ tiene al menos $r+1$ columnas linealmente independientes, y $\operatorname{rango}(\mathbf{A}\,|\,\mathbf{y})>\operatorname{rango}\mathbf{A}$.

(ii) Según la subsección [12.4](lineare-gleichungssysteme.html#stufe-12-4), todas las soluciones son una solución más los vectores del núcleo. La solución es, por tanto, única si y solo si $\ker\mathbf{A}=\{\mathbf{0}\}$, y según el teorema del rango eso significa $\operatorname{rango}\mathbf{A}=n$.

(iii) Todo $\mathbf{y}$ está en el espacio columna si y solo si el espacio columna es todo $\mathbb{R}^m$. Eso ocurre si y solo si tiene dimensión $m$, es decir, $\operatorname{rango}\mathbf{A}=m$.
:::

Para una matriz cuadrada con $\operatorname{rango}\mathbf{A}=n=m$, (ii) y (iii) se cumplen a la vez: exactamente una solución para cada lado derecho, de acuerdo con el teorema sobre la invertibilidad.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, $\operatorname{rango}\mathbf{A}=1$. Con $\mathbf{y}=(1,\,1)^{\top}$, la matriz ampliada tiene las filas $(1,\,2\,|\,1)$ y $(2,\,4\,|\,1)$; si se resta la primera dos veces de la segunda, queda $(0,\,0\,|\,-1)$, que no es una fila nula. Así que $\operatorname{rango}(\mathbf{A}\,|\,\mathbf{y})=2\ne1$, y el sistema no tiene solución, como en la subsección [12.2](lineare-gleichungssysteme.html#stufe-12-2). Con $\mathbf{y}=(3,\,6)^{\top}$ queda, en cambio, $(0,\,0\,|\,0)$, los rangos son iguales y el sistema tiene solución. Como $\operatorname{rango}\mathbf{A}=1<2=n$, la solución no es única: todas las soluciones son $(1,\,1)^{\top}+t\,(2,\,-1)^{\top}$. Y como $\operatorname{rango}\mathbf{A}=1<2=m$, hay lados derechos sin solución. En el sistema sobredeterminado de la subsección [12.5](lineare-gleichungssysteme.html#stufe-12-5), $\operatorname{rango}\mathbf{A}=2=n$: si hubiera una solución, sería única. Pero no la hay, así que allí, según (i), $\operatorname{rango}(\mathbf{A}\,|\,\mathbf{y})=3$.
::::

⁠**En resumen:** El núcleo reúne las direcciones que una matriz lleva a cero; el núcleo y el rango se reparten las $n$ direcciones de entrada. Un sistema $\mathbf{A}\mathbf{x}=\mathbf{y}$ tiene solución si y solo si el lado derecho no aumenta el rango, y la solución es única si y solo si el núcleo solo contiene el vector nulo.

### Características dependientes

<span class="anker" id="stufe-13-6"></span>

En conjuntos de datos reales, a veces varias características llevan dos veces la misma información. Un cuestionario registra el peso corporal en kilogramos y, para otra evaluación, otra vez en libras. La descripción de una casa indica la superficie de la planta baja, la de la planta superior y la superficie total. Para la matriz de datos esto significa: sus columnas son linealmente dependientes, y su rango es menor que el número de características.

::::beispiel [Ejemplo numérico] planta baja, planta superior, superficie total
Cuatro casas:

$$\mathbf{X}=\begin{pmatrix}50&40&90\\60&0&60\\45&45&90\\70&30&100\end{pmatrix}\qquad(\text{superficies en }\mathrm m^2).$$

La tercera columna es la suma de las dos primeras. Así que $\operatorname{rango}\mathbf{X}=2<3$, y el núcleo contiene $\mathbf k=(1,\,1,\,-1)^{\top}$, pues $\mathbf{X}\mathbf k=\mathbf{0}$. De ahí se siguen dos cosas.

<ul>

<li>

⁠**Los pesos no son únicos.** Para todo número $t$, $\mathbf{w}$ y $\mathbf{w}+t\,\mathbf k$ dan las mismas predicciones, pues $\mathbf{X}(\mathbf{w}+t\,\mathbf k)=\mathbf{X}\mathbf{w}+t\,\mathbf{X}\mathbf k=\mathbf{X}\mathbf{w}$. Los pesos $(3,\,3,\,0)^{\top}$, «$3$ por metro cuadrado de planta baja y de planta superior», y $(0,\,0,\,3)^{\top}$, «$3$ por metro cuadrado de superficie total», dan ambos $(270,\,180,\,270,\,300)^{\top}$. A partir de las predicciones solas no puede saberse qué pesos se usaron, y no tiene sentido interpretar uno solo de estos pesos.

</li>

<li>

⁠**La matriz de Gram de las características es singular.** De $\mathbf{X}\mathbf k=\mathbf{0}$ se sigue $\mathbf{X}^{\top}\mathbf{X}\mathbf k=\mathbf{X}^{\top}\mathbf{0}=\mathbf{0}$ con $\mathbf k\ne\mathbf{0}$. Según la subsección [11.5](einheitsmatrix-und-inverse.html#stufe-11-5), $\mathbf{X}^{\top}\mathbf{X}$ no tiene entonces inversa.

</li>

</ul>
::::

::::beispiel [Ejemplo numérico] kilogramos y libras
Una libra son exactamente $0{,}45359237$ kg, así que una masa en libras es $c=1/0{,}45359237\approx2{,}20462$ veces la misma masa en kilogramos. Tres personas con estatura (cm), masa (kg) y masa (libras):

$$\mathbf{X}=\begin{pmatrix}170&70&70\,c\\182&85&85\,c\\165&60&60\,c\end{pmatrix}\approx\begin{pmatrix}170&70&154{,}3\\182&85&187{,}4\\165&60&132{,}3\end{pmatrix}.$$

La tercera columna es $c$ veces la segunda, así que $\operatorname{rango}\mathbf{X}=2$ y $(0,\,c,\,-1)^{\top}$ está en el núcleo. La columna de las libras no aporta información nueva; solo duplica una que ya existe.
::::

⁠**En resumen:** Si varias características llevan dos veces la misma información, las columnas de la matriz de datos son linealmente dependientes; entonces el rango es menor que $d$, pesos distintos dan las mismas predicciones y $\mathbf{X}^{\top}\mathbf{X}$ no es invertible.

:::aufgabe Ejercicio 31 ★★ Rango y núcleo
<span class="anker" id="aufg-31"></span>

Determina el rango y el núcleo de

$$\mathbf{A}_1=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}\qquad\text{y}\qquad \mathbf{A}_2=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$$

y comprueba en cada caso el teorema del rango. ¿Cuál de las dos matrices es invertible?

:::loesung
$\mathbf{A}_1$: la segunda fila es el doble de la primera. Si se resta de la segunda fila el doble de la primera, y de la tercera la primera, quedan las filas $(1,2,3)$, $(0,0,0)$, $(0,-2,-2)$; tras intercambiar las dos filas inferiores, es una forma escalonada con dos pivotes; por tanto, $\operatorname{rango}\mathbf{A}_1=2$. El núcleo lo dan las ecuaciones $x_1+2x_2+3x_3=0$ y $-2x_2-2x_3=0$: con $x_3=t$ se tiene $x_2=-t$ y $x_1=-2(-t)-3t=-t$; por tanto, $\ker\mathbf{A}_1=\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$. Comprobación: la suma de las dos primeras columnas es $(3,\,6,\,1)^{\top}$, y la tercera columna es $(3,\,6,\,1)^{\top}$. Teorema del rango: $1+2=3$. $\mathbf{A}_1$ no es invertible.

$\mathbf{A}_2$: si se resta la primera fila de la tercera, se obtiene $(0,\,-1,\,1)$; si se le suma la segunda fila, $(0,\,0,\,2)$. Tres pivotes; por tanto, $\operatorname{rango}\mathbf{A}_2=3$ y $\ker\mathbf{A}_2=\{\mathbf{0}\}$. Teorema del rango: $0+3=3$. $\mathbf{A}_2$ es invertible; su determinante es $1\cdot(1-0)-1\cdot(0-1)+0=2\ne0$.
:::
:::

:::aufgabe Ejercicio 32 ★★ Kilogramos y libras
<span class="anker" id="aufg-32"></span>

Usa la matriz de datos de las personas de la subsección [13.6](#stufe-13-6).

<ol class="al">

<li>

Indica dos vectores de pesos distintos que den las mismas predicciones para las tres personas, de modo que uno use solo la columna de los kilogramos y el otro solo la columna de las libras.

</li>

<li>

La tabla da los valores en libras redondeados a un decimal. ¿Siguen siendo exactamente linealmente dependientes las columnas de la tabla redondeada? ¿Qué dice esto sobre el rango que se calcula a partir de datos redondeados?

</li>

</ol>

:::loesung
(a) Los pesos $(0,\,1,\,0)^{\top}$ predicen para cada persona su masa en kilogramos, es decir, $(70,\,85,\,60)^{\top}$. Las mismas predicciones las dan los pesos $(0,\,0,\,1/c)^{\top}\approx(0;\ 0;\ 0{,}4536)^{\top}$, que solo usan la columna de las libras, pues $\frac1c\cdot c\,x=x$. Los dos vectores de pesos se diferencian en $\frac1c\,(0,\,c,\,-1)^{\top}$, un vector del núcleo.

(b) Los cocientes entre los valores redondeados en libras y los valores en kilogramos son $154{,}3/70\approx2{,}20429$, $187{,}4/85\approx2{,}20471$ y $132{,}3/60=2{,}205$; no son exactamente iguales. Las columnas redondeadas ya no son, por tanto, exactamente proporcionales, y el rango calculado de la tabla redondeada es el rango completo $3$. En cuanto al contenido, nada ha cambiado: la columna de las libras sigue llevando casi solo la información de la columna de los kilogramos. El rango salta de $2$ a $3$ por redondeos minúsculos. Por eso, con datos medidos o redondeados, el rango por sí solo no dice si dos características llevan en la práctica la misma información.
:::
:::

:::aufgabe Ejercicio 33 ★★ Un barrio como número
<span class="anker" id="aufg-33"></span>

Las viviendas están o bien en el norte o bien en el sur. Esto se traduce en dos características: «Norte» vale $1$ para las viviendas del norte y $0$ en los demás casos, y «Sur», igual para el sur. Para un precio base se añade además una columna de unos (subsección [8.5](lineare-abbildungen.html#stufe-8-5)). Cuatro viviendas, alternando norte y sur, dan

$$\mathbf{X}=\begin{pmatrix}1&1&0\\1&0&1\\1&1&0\\1&0&1\end{pmatrix}\qquad(\text{columnas: unos, Norte, Sur}).$$

<ol class="al">

<li>

Determina el rango de $\mathbf{X}$ y un vector $\mathbf k\ne\mathbf{0}$ del núcleo. ¿Qué relación entre las columnas hay detrás?

</li>

<li>

Demuestra que los pesos $(100,\,20,\,0)^{\top}$ y $(80,\,40,\,20)^{\top}$ dan las mismas predicciones. ¿Cómo se elimina la dependencia sin perder información?

</li>

</ol>

:::loesung
(a) Cada vivienda está o bien en el norte o bien en el sur; por tanto, la columna «Norte» más la columna «Sur» vale $1$ en cada fila: es igual a la columna de unos. Las columnas son linealmente dependientes, y $\mathbf k=(1,\,-1,\,-1)^{\top}$ está en el núcleo: $\mathbf{X}\mathbf k=\mathbf{0}$. La primera y la segunda columna son independientes; por tanto, $\operatorname{rango}\mathbf{X}=2$.

(b) $\mathbf{X}\,(100,\,20,\,0)^{\top}=(120,\,100,\,120,\,100)^{\top}$ y $\mathbf{X}\,(80,\,40,\,20)^{\top}=(120,\,100,\,120,\,100)^{\top}$. Los dos vectores de pesos se diferencian en $(20,\,-20,\,-20)^{\top}=20\,\mathbf k$. La dependencia se elimina suprimiendo una de las dos columnas, «Norte» o «Sur», por ejemplo «Sur». Entonces el precio base es el precio en el sur, y el peso de «Norte» es el recargo por estar en el norte. No se pierde información, pues «Sur» es siempre $1-\text{Norte}$ y puede recuperarse en cualquier momento.
:::
:::
