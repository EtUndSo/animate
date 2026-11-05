---
title: Proyección sobre una recta
pfad: Informática / Aprendizaje automático / Proyección, valores propios y descomposiciones
order: 6220300
summary: Un punto está junto a una recta.
tags: proyección ortogonal, matriz de proyección, proyección
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Un punto está junto a una recta. ¿Qué punto de la recta es el más cercano a él? Esta sección responde a la pregunta para rectas que pasan por el origen, en cualquier dimensión. La respuesta es el pie de la perpendicular, y la razón es el teorema de Pitágoras.
:::

### El pie de la perpendicular

<span class="anker" id="stufe-2-1"></span>

Una recta que pasa por el origen consta de todos los múltiplos $t\,\mathbf{a}$ de un vector director $\mathbf{a}\ne\mathbf{0}$. Se da un punto $\mathbf{y}$, que no tiene por qué estar sobre ella. Se busca el punto de la recta más cercano a $\mathbf{y}$.

En la parte 1, sección 5.5, una flecha proyectaba una sombra sobre una recta con luz que incidía perpendicularmente. El extremo de la sombra es el punto en el que la perpendicular trazada desde $\mathbf{y}$ corta a la recta, el *pie de la perpendicular*. El vector que va de este punto a $\mathbf{y}$ es perpendicular a la recta (fig. [4](#abb-4)). Que es el punto más cercano lo muestra la subsección siguiente. Aquí primero se calcula, y además también para el caso en que $\mathbf{a}$ no está normalizado.

:::herleitung El pie de la perpendicular
El punto buscado está sobre la recta, es decir, es $\hat x\,\mathbf{a}$ con un número $\hat x$ aún desconocido. El vector de unión $\mathbf{y}-\hat x\,\mathbf{a}$ debe ser perpendicular a $\mathbf{a}$:

$$\mathbf{a}^{\top}(\mathbf{y}-\hat x\,\mathbf{a})=0\qquad\Longleftrightarrow\qquad \mathbf{a}^{\top}\mathbf{y}-\hat x\,\mathbf{a}^{\top}\mathbf{a}=0\qquad\Longleftrightarrow\qquad \hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} .$$

Como $\mathbf{a}\ne\mathbf{0}$, es $\mathbf{a}^{\top}\mathbf{a}=\lVert\mathbf{a}\rVert^2>0$; la división está, pues, permitida, y existe exactamente un $\hat x$ así.
:::

:::definition Definición 2.1 (Proyección sobre una recta)
<span class="anker" id="satz-2-1"></span>

Sea $\mathbf{a}\in\mathbb{R}^n$, $\mathbf{a}\ne\mathbf{0}$. La __proyección ortogonal__ de $\mathbf{y}\in\mathbb{R}^n$ sobre la recta que pasa por el origen en la dirección de $\mathbf{a}$ es el punto

<span class="anker" id="gl-2-1"></span>
$$\hat{\mathbf{y}}=\hat x\,\mathbf{a}\qquad\text{con}\qquad\hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} . \tag{2.1}$$
:::

El punto $\hat{\mathbf{y}}$ es un vector de $\mathbb{R}^n$; el número $\hat x$ es su coordenada a lo largo de $\mathbf{a}$. No hay que confundir una cosa con la otra. Si $\mathbf{a}$ está normalizado, es $\mathbf{a}^{\top}\mathbf{a}=1$ y $\hat{\mathbf{y}}=(\mathbf{a}^{\top}\mathbf{y})\,\mathbf{a}$, exactamente el punto de sombra de la parte 1.

:::abbildung ml/k2lot 4
La proyección de $\mathbf{y}=(4,3)^{\top}$ sobre la recta en la dirección de $\mathbf{a}=(1,2)^{\top}$. El pie de la perpendicular es $\hat{\mathbf{y}}=2\mathbf{a}=(2,4)^{\top}$; el vector de unión $\mathbf{r}=(2,-1)^{\top}$ (azul) es perpendicular a la recta. Otro punto de la recta, por ejemplo $(1,2)^{\top}$, está más lejos de $\mathbf{y}$ (a trazos): el triángulo formado por $\mathbf{y}$, $\hat{\mathbf{y}}$ y $(1,2)^{\top}$ tiene un ángulo recto en $\hat{\mathbf{y}}$, y el lado a trazos es su hipotenusa.
:::

⁠**Ejemplo numérico 1:** Para $\mathbf{a}=(1,\,2)^{\top}$ y $\mathbf{y}=(4,\,3)^{\top}$ se tiene $\mathbf{a}^{\top}\mathbf{y}=4+6=10$ y $\mathbf{a}^{\top}\mathbf{a}=5$ (fig. [5](#abb-5)); por tanto, $\hat x=2$ y $\hat{\mathbf{y}}=(2,\,4)^{\top}$. El vector de unión $\mathbf{y}-\hat{\mathbf{y}}=(2,\,-1)^{\top}$ es perpendicular a $\mathbf{a}$: $2-2=0$.

:::abbildung ml/k2rproj 5
Los dos productos escalares de la proyección paso a paso: $\mathbf{a}^{\top}\mathbf{y}=10$ en el numerador y $\mathbf{a}^{\top}\mathbf{a}=5$ en el denominador de $\hat x$.
:::

⁠**Ejemplo numérico 2:** Para $\mathbf{a}=(3,\,4)^{\top}$ y $\mathbf{y}=(3,\,1)^{\top}$ se tiene $\hat x=(9+4)/25=0{,}52$ y $\hat{\mathbf{y}}=0{,}52\,(3,\,4)^{\top}=(1{,}56;\ 2{,}08)^{\top}$, el mismo punto de sombra que en la parte 1 con el vector normalizado $(0{,}6;\ 0{,}8)^{\top}=\mathbf{a}/5$. La longitud del vector director no importa: si se sustituye $\mathbf{a}$ por $c\,\mathbf{a}$ con $c\ne0$, $\hat x$ pasa a ser $\hat x/c$, y $\hat{\mathbf{y}}$ no cambia. Si, en cambio, se duplica $\mathbf{y}$, también se duplica $\hat{\mathbf{y}}$.

⁠**En resumen:** La proyección de $\mathbf{y}$ sobre la recta en la dirección de $\mathbf{a}$ es el pie de la perpendicular, $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$.

### El pie es el punto más cercano

<span class="anker" id="stufe-2-2"></span>

Hasta ahora solo se ha mostrado que el vector de unión con el pie es perpendicular a la recta. Que el pie es además el punto más cercano se deduce del teorema de Pitágoras: quien se aleja del pie a lo largo de la recta añade al vector perpendicular un tramo en la dirección de la recta, y eso solo puede aumentar la distancia.

:::satz Teorema 2.2 (El pie es el punto más cercano)
<span class="anker" id="satz-2-2"></span>

Sea $\hat{\mathbf{y}}=\hat x\,\mathbf{a}$ la proyección de $\mathbf{y}$ sobre la recta en la dirección de $\mathbf{a}$. Para todo número $t$ se cumple

<span class="anker" id="gl-2-2"></span>
$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2=\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2+(t-\hat x)^2\,\lVert\mathbf{a}\rVert^2 . \tag{2.2}$$

En particular, $\hat{\mathbf{y}}$ es el único punto de la recta con la menor distancia a $\mathbf{y}$.
:::

:::beweis El punto más cercano
Se escribe el vector que va de $t\,\mathbf{a}$ a $\mathbf{y}$ como suma de dos flechas:

$$\mathbf{y}-t\,\mathbf{a}=(\mathbf{y}-\hat{\mathbf{y}})+(\hat x-t)\,\mathbf{a} .$$

El primer sumando es, según la deducción, perpendicular a $\mathbf{a}$ y, por tanto, también al segundo. Según el teorema de Pitágoras de la parte 1, sección 5.3, el cuadrado de la longitud de la suma es la suma de los cuadrados de las longitudes, y eso es [(2.2)](#gl-2-2). El segundo sumando del lado derecho nunca es negativo y solo es cero para $t=\hat x$. Por tanto, la distancia es mínima exactamente para $t=\hat x$.
:::

Para la longitud del pie se cumple $\lVert\hat{\mathbf{y}}\rVert=|\hat x|\,\lVert\mathbf{a}\rVert=|\mathbf{a}^{\top}\mathbf{y}|/\lVert\mathbf{a}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$, donde $\varphi$ es el ángulo entre $\mathbf{a}$ y $\mathbf{y}$. Es el cateto contiguo del triángulo rectángulo de hipotenusa $\mathbf{y}$.

⁠**Ejemplo numérico:** En el primer ejemplo numérico de la subsección anterior es $\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2=\lVert(2,\,-1)^{\top}\rVert^2=5$. Para el punto $t=1$, es decir, $(1,\,2)^{\top}$, [(2.2)](#gl-2-2) predice el cuadrado de la distancia $5+1\cdot5=10$, y efectivamente $\lVert(3,\,1)^{\top}\rVert^2=10$. Para $t=3$, es decir, $(3,\,6)^{\top}$, también es $5+1\cdot5=10=\lVert(1,\,-3)^{\top}\rVert^2$. Ambos puntos están a la misma distancia del pie, a lados distintos.

⁠**En resumen:** El punto más cercano de una recta es el pie de la perpendicular, porque, según Pitágoras, cada paso a lo largo de la recta aumenta el cuadrado de la distancia.

:::hintergrund Por qué hay exactamente un punto más cercano y por qué eso se debe a la norma euclídea
La demostración usa el teorema de Pitágoras, y este solo vale para normas que provienen de un producto escalar. En la parte 1, sección 3.4, resultó que la norma 1 no es una norma de ese tipo. Con ella se pierde, en efecto, la unicidad. Ejemplo: la recta en la dirección de $\mathbf{a}=(1,\,1)^{\top}$ y el punto $\mathbf{y}=(1,\,0)^{\top}$. Para $0\le t\le1$ se tiene

$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert_1=|1-t|+|0-t|=(1-t)+t=1 ,$$

es decir, el mismo valor para todos los puntos entre $\mathbf{0}$ y $\mathbf{a}$; fuera de este segmento, la distancia es mayor. En esta norma hay todo un segmento de puntos más cercanos. En la norma euclídea hay exactamente uno: $\hat x=\tfrac12$, el punto $(\tfrac12,\,\tfrac12)^{\top}$. Que la proyección sea única y se calcule con una fórmula sencilla es una de las razones por las que tantos métodos usan la distancia euclídea.
:::

### La matriz de proyección

<span class="anker" id="stufe-2-3"></span>

La regla $\mathbf{y}\mapsto\hat{\mathbf{y}}$ es lineal: la suma de dos puntos se transforma en la suma de sus proyecciones, y un múltiplo, en el múltiplo. Según la parte 1, sección 8.2, tiene, por tanto, una matriz. Se lee directamente si se escribe el número $\mathbf{a}^{\top}\mathbf{y}$ al otro lado de $\mathbf{a}$ y se reagrupa el producto de matrices:

$$\hat{\mathbf{y}}=\mathbf{a}\,\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{y} .$$

En el numerador está el producto exterior de la parte 1, sección 9.5.

:::definition Definición 2.3 (Matriz de proyección de una recta)
<span class="anker" id="satz-2-3"></span>

Para $\mathbf{a}\ne\mathbf{0}$,

<span class="anker" id="gl-2-3"></span>
$$\mathbf{P}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}} \tag{2.3}$$

se llama __matriz de proyección__ sobre la recta en la dirección de $\mathbf{a}$. Se cumple $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$.
:::

:::satz Teorema 2.4 (Propiedades de la matriz de proyección de una recta)
<span class="anker" id="satz-2-4"></span>

Se cumple $\mathbf{P}^{\top}=\mathbf{P}$ y $\mathbf{P}^2=\mathbf{P}$. Los puntos de la recta se quedan donde están: $\mathbf{P}\mathbf{a}=\mathbf{a}$. Los vectores perpendiculares a $\mathbf{a}$ se transforman en $\mathbf{0}$. El rango de $\mathbf{P}$ es $1$.
:::

:::beweis Propiedades
$(\mathbf{a}\mathbf{a}^{\top})^{\top}=\mathbf{a}\mathbf{a}^{\top}$; por tanto, $\mathbf{P}$ es simétrica. Además, $\mathbf{P}^2=\mathbf{a}(\mathbf{a}^{\top}\mathbf{a})\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})^2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{P}$, porque $\mathbf{a}^{\top}\mathbf{a}$ es un número. $\mathbf{P}\mathbf{a}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{a})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{a}$. Si $\mathbf{a}^{\top}\mathbf{z}=0$, entonces $\mathbf{P}\mathbf{z}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{z})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{0}$. Cada columna de $\mathbf{P}$ es un múltiplo de $\mathbf{a}$; por tanto, el rango es $1$.
:::

La ecuación $\mathbf{P}^2=\mathbf{P}$ tiene un significado sencillo: lo que ya está sobre la recta se queda donde está al proyectar por segunda vez.

⁠**Ejemplo numérico:** Para $\mathbf{a}=(1,\,2)^{\top}$ se tiene

$$\mathbf{P}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad \mathbf{P}\begin{pmatrix}4\\3\end{pmatrix}=\frac15\begin{pmatrix}4+6\\8+12\end{pmatrix}=\begin{pmatrix}2\\4\end{pmatrix}.$$

Comprobación de $\mathbf{P}^2=\mathbf{P}$: $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)^2=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)=5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$; por tanto, $\mathbf{P}^2=\frac1{25}\cdot5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=\mathbf{P}$. La matriz $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ era en la parte 1, sección 11.5, el ejemplo de una matriz sin inversa. Ahora está claro lo que hace: es cinco veces una proyección y aplasta el plano sobre la recta en la dirección de $(1,\,2)^{\top}$.

⁠**En resumen:** La proyección sobre una recta es el producto matriz-vector con $\mathbf{P}=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$; esta matriz es simétrica y cumple $\mathbf{P}^2=\mathbf{P}$.

### Proyecciones en general

<span class="anker" id="stufe-2-4"></span>

También hay sombras cuando la luz incide oblicuamente. Entonces la sombra de un punto sobre una recta ya no es el pie de la perpendicular, pero sigue estando sobre la recta, y un punto que ya está sobre la recta es su propia sombra. La propiedad $\mathbf{P}^2=\mathbf{P}$ se conserva, por tanto; la simetría, no.

:::definition Definición 2.5 (Proyección)
<span class="anker" id="satz-2-5"></span>

Una matriz cuadrada $\mathbf{P}$ con $\mathbf{P}^2=\mathbf{P}$ se llama __proyección__. Se llama proyección ortogonal si, además, para todo $\mathbf{y}$ el vector de unión $\mathbf{y}-\mathbf{P}\mathbf{y}$ es perpendicular a todas las imágenes $\mathbf{P}\mathbf{z}$.
:::

:::satz Teorema 2.6 (Ortogonal significa simétrica)
<span class="anker" id="satz-2-6"></span>

Una proyección $\mathbf{P}$ es una proyección ortogonal si y solo si $\mathbf{P}^{\top}=\mathbf{P}$.
:::

:::beweis Ortogonal significa simétrica
Para todos los $\mathbf{y},\mathbf{z}$ se tiene $(\mathbf{y}-\mathbf{P}\mathbf{y})^{\top}\mathbf{P}\mathbf{z}=\mathbf{y}^{\top}(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}\mathbf{z}$. Si $\mathbf{P}^{\top}=\mathbf{P}$, entonces $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}=\mathbf{P}-\mathbf{P}^2=\mathbf 0$, y la expresión es cero. Si, a la inversa, la expresión es cero para todos los $\mathbf{y},\mathbf{z}$, la matriz $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}$ es la matriz nula; en efecto, con $\mathbf{y}=\mathbf{e}_i$ y $\mathbf{z}=\mathbf{e}_l$ la expresión selecciona su entrada $(i,l)$. Entonces $\mathbf{P}=\mathbf{P}^{\top}\mathbf{P}$, y $\mathbf{P}^{\top}\mathbf{P}$ es simétrica según la parte 1, sección 10.2.
:::

⁠**Ejemplo numérico:** La matriz $\mathbf{P}=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ transforma $(x_1,\,x_2)^{\top}$ en $(x_1+x_2,\,0)^{\top}$. Se tiene $\mathbf{P}^2=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$; por tanto, $\mathbf{P}$ es una proyección sobre el eje $x_1$. No es simétrica y, por tanto, no es ortogonal: el punto $(0,\,1)^{\top}$ se transforma en $(1,\,0)^{\top}$, y el vector de unión $(-1,\,1)^{\top}$ es oblicuo respecto al eje. La luz incide aquí en la dirección $(1,\,-1)^{\top}$. El punto más cercano del eje $x_1$, $(0,\,0)^{\top}$, no lo proporciona esta proyección.

⁠**En resumen:** Una proyección es una matriz con $\mathbf{P}^2=\mathbf{P}$; es ortogonal, es decir, lleva al pie de la perpendicular, si y solo si es simétrica.

:::aufgabe Ejercicio 4 ★ Una proyección a mano
<span class="anker" id="aufg-4"></span>

Proyecta $\mathbf{y}=(3,\,3,\,0)^{\top}$ sobre la recta en la dirección de $\mathbf{a}=(2,\,1,\,2)^{\top}$.

<ol class="al">

<li>

Calcula $\hat x$, $\hat{\mathbf{y}}$ y el vector de unión $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}$. Comprueba $\mathbf{a}^{\top}\mathbf{r}=0$. ¿A qué distancia de la recta está $\mathbf{y}$?

</li>

<li>

Escribe la matriz de proyección $\mathbf{P}$ y comprueba $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ y $\mathbf{P}\mathbf{a}=\mathbf{a}$.

</li>

</ol>

:::loesung
(a) Se tiene $\mathbf{a}^{\top}\mathbf{y}=6+3+0=9$ y $\mathbf{a}^{\top}\mathbf{a}=4+1+4=9$; por tanto, $\hat x=1$ y $\hat{\mathbf{y}}=\mathbf{a}=(2,\,1,\,2)^{\top}$. El vector de unión es $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(1,\,2,\,-2)^{\top}$, y $\mathbf{a}^{\top}\mathbf{r}=2+2-4=0$: es perpendicular a la recta. La distancia de $\mathbf{y}$ a la recta es $\lVert\mathbf{r}\rVert=\sqrt{1+4+4}=3$; según el teorema de la sección [2.2](#stufe-2-2), ningún punto de la recta está más cerca.

(b)

$$\mathbf{P}=\frac{\mathbf{a}\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}=\frac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\qquad \mathbf{P}\mathbf{y}=\frac19\begin{pmatrix}12+6\\6+3\\12+6\end{pmatrix}=\begin{pmatrix}2\\1\\2\end{pmatrix},\qquad \mathbf{P}\mathbf{a}=\frac19\begin{pmatrix}8+2+8\\4+1+4\\8+2+8\end{pmatrix}=\mathbf{a} .$$
:::
:::

:::aufgabe Ejercicio 5 ★★ Pitágoras sobre la recta
<span class="anker" id="aufg-5"></span>

Sean $\mathbf{a}=(1,\,2)^{\top}$ y $\mathbf{y}=(4,\,3)^{\top}$ como en el ejemplo numérico.

<ol class="al">

<li>

Calcula $\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2$ para $t=0$, $1$, $2$, $3$ y $4$ directamente y con [(2.2)](#gl-2-2).

</li>

<li>

Calcula el ángulo $\varphi$ entre $\mathbf{a}$ y $\mathbf{y}$ y comprueba $\lVert\hat{\mathbf{y}}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$.

</li>

</ol>

:::loesung
(a) Directamente: $t=0$: $\lVert(4,\,3)^{\top}\rVert^2=25$; $t=1$: $\lVert(3,\,1)^{\top}\rVert^2=10$; $t=2$: $\lVert(2,\,-1)^{\top}\rVert^2=5$; $t=3$: $\lVert(1,\,-3)^{\top}\rVert^2=10$; $t=4$: $\lVert(0,\,-5)^{\top}\rVert^2=25$. Con [(2.2)](#gl-2-2), $\hat x=2$, $\lVert\mathbf{r}\rVert^2=5$ y $\lVert\mathbf{a}\rVert^2=5$: $5+5(t-2)^2$ da $25$, $10$, $5$, $10$, $25$. Los valores son simétricos respecto al pie $t=2$, porque el cuadrado de la distancia crece con el cuadrado del desplazamiento respecto al pie a lo largo de la recta.

(b) $\cos\varphi=\mathbf{a}^{\top}\mathbf{y}/(\lVert\mathbf{a}\rVert\,\lVert\mathbf{y}\rVert)=10/(\sqrt5\cdot5)=2/\sqrt5\approx0{,}894$; por tanto, $\varphi\approx26{,}57^\circ$. Se tiene $\lVert\hat{\mathbf{y}}\rVert=\lVert(2,\,4)^{\top}\rVert=\sqrt{20}=2\sqrt5$ y $|\cos\varphi|\,\lVert\mathbf{y}\rVert=\tfrac2{\sqrt5}\cdot5=2\sqrt5$.
:::
:::

:::aufgabe Ejercicio 6 ★★ ¿Qué matrices son proyecciones?
<span class="anker" id="aufg-6"></span>

Comprueba para cada matriz si es una proyección y si es una proyección ortogonal. En las proyecciones, describe sobre qué se proyecta.

$$\mathbf{P}_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad \mathbf{P}_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad \mathbf{P}_3=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad \mathbf{P}_4=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad \mathbf{P}_5=\mathbf{I},\quad \mathbf{P}_6=\mathbf 0 .$$

:::loesung
Para cada matriz se comprueba primero $\mathbf{P}^2=\mathbf{P}$ y después $\mathbf{P}^{\top}=\mathbf{P}$.

<ul>

<li>

$\mathbf{P}_1$: $\mathbf{P}_1^2=\mathbf{P}_1$ y simétrica; por tanto, la proyección ortogonal sobre el eje $x_1$.

</li>

<li>

$\mathbf{P}_2$: $\mathbf{P}_2^2=\tfrac14\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)=\mathbf{P}_2$ y simétrica: la proyección ortogonal sobre la recta en la dirección de $(1,\,1)^{\top}$; se tiene $\mathbf{P}_2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ con $\mathbf{a}=(1,\,1)^{\top}$.

</li>

<li>

$\mathbf{P}_3$: $\mathbf{P}_3^2=\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)=\mathbf{P}_3$, pero no es simétrica. Es una proyección oblicua: transforma $(x_1,\,x_2)^{\top}$ en $x_1\,(1,\,1)^{\top}$, es decir, lleva todo a la recta en la dirección de $(1,\,1)^{\top}$, y transforma el vector $(0,\,1)^{\top}$ en cero. La luz incide en la dirección de $(0,\,1)^{\top}$, no perpendicularmente a la recta.

</li>

<li>

$\mathbf{P}_4$: $\mathbf{P}_4^2=\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)\ne\mathbf{P}_4$. No es una proyección, sino una cizalladura; aplicada dos veces, cizalla el doble.

</li>

<li>

$\mathbf{P}_5=\mathbf{I}$: $\mathbf{I}^2=\mathbf{I}$, simétrica. La proyección ortogonal sobre todo el plano; deja todo donde está.

</li>

<li>

$\mathbf{P}_6=\mathbf 0$: $\mathbf 0^2=\mathbf 0$, simétrica. La proyección ortogonal sobre el origen.

</li>

</ul>
:::
:::
