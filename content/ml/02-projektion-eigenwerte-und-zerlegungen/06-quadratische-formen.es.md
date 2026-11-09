---
title: Formas cuadráticas
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15220600
summary: Después de las funciones lineales, las cuadráticas son las funciones de varias variables más sencillas.
tags: forma cuadrática
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Después de las funciones lineales, las cuadráticas son las funciones de varias variables más sencillas. Describen energías, errores cuadráticos y superficies curvas. Esta sección las escribe con una matriz, muestra las tres formas básicas, cuenco, canal y silla, y explica cómo se reconoce en la matriz cuál de ellas se tiene, siempre que no haya términos cruzados.
:::

### Formas cuadráticas

<span class="anker" id="stufe-5-1"></span>

En [Fundamentos 1, sección 8.4](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-4), toda función lineal con una salida era una suma ponderada $\mathbf{w}^{\top}\mathbf{x}$ de las componentes. El siguiente tipo de función, en orden de sencillez, suma productos de dos componentes: cuadrados como $x_1^2$ y términos cruzados como $x_1x_2$. Un ejemplo de la electrotecnia es la energía magnética de dos bobinas acopladas con las inductancias $L_1$, $L_2$ y la inductancia mutua $M$, por las que circulan las corrientes $i_1$ e $i_2$:

$$W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2 .$$

Tales sumas pueden escribirse con una matriz en el centro.

:::definition Definición 5.1 (Forma cuadrática)
<span class="anker" id="satz-5-1"></span>

Dada una matriz cuadrada $\mathbf{A}\in\mathbb{R}^{n\times n}$, la función

<span class="anker" id="gl-5-1"></span>
$$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^na_{il}\,x_ix_l \tag{5.1}$$

se llama __forma cuadrática__ de $\mathbf{A}$.
:::

El resultado es un número: $\mathbf{A}\mathbf{x}$ es un vector, y $\mathbf{x}^{\top}(\mathbf{A}\mathbf{x})$ es el producto escalar de $\mathbf{x}$ con él. Desarrollada para $n=2$, es

$$\mathbf{x}^{\top}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\mathbf{x}=a_{11}x_1^2+(a_{12}+a_{21})\,x_1x_2+a_{22}x_2^2 .$$

Si se duplica $\mathbf{x}$, $f$ se cuadruplica: $f(c\,\mathbf{x})=c^2f(\mathbf{x})$. De ahí el nombre.

::::beispiel [Ejemplo numérico]
Para $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ es $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$. En el punto $\mathbf{x}=(1,\,-1)^{\top}$ es $f=5-4+2=3$; como control, $\mathbf{A}\mathbf{x}=(3,\,0)^{\top}$ y $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=3$. La fig. [14](#abb-14) calcula la doble suma [(5.1)](#gl-5-1) en este punto término a término. En el punto $(1,\,1)^{\top}$ es $f=11$; en el origen, $f=0$. La energía de las dos bobinas es $W=\tfrac12\,\mathbf i^{\top}\bigl(\begin{smallmatrix}L_1&M\\M&L_2\end{smallmatrix}\bigr)\,\mathbf i$ con el vector de corrientes $\mathbf i=(i_1,\,i_2)^{\top}$; la matriz se llama matriz de inductancias.

:::abbildung ml/k2rqf 14
La forma cuadrática de $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ en el punto $\mathbf{x}=(1,-1)^{\top}$ como doble suma: cuatro términos, uno por cada entrada de $\mathbf{A}$.
:::
::::

⁠**En resumen:** Una forma cuadrática $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ es una suma de cuadrados y productos cruzados de las componentes, con las entradas de $\mathbf{A}$ como pesos.

### Solo cuenta la parte simétrica

<span class="anker" id="stufe-5-2"></span>

En la expresión para $n=2$, $a_{12}$ y $a_{21}$ solo aparecen como suma. Por eso, las matrices $\bigl(\begin{smallmatrix}5&4\\0&2\end{smallmatrix}\bigr)$ y $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ tienen la misma forma cuadrática. Siempre se puede elegir la simétrica.

:::satz Teorema 5.2 (La parte simétrica)
<span class="anker" id="satz-5-2"></span>

Para toda matriz cuadrada $\mathbf{A}$ y todo $\mathbf{x}$ es

<span class="anker" id="gl-5-2"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\Bigl(\frac{\mathbf{A}+\mathbf{A}^{\top}}2\Bigr)\mathbf{x} . \tag{5.2}$$
:::

:::beweis La parte simétrica
El número $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ es igual a su propia traspuesta, es decir, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})^{\top}=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{x}$. La media de ambas expresiones es $\mathbf{x}^{\top}\frac{\mathbf{A}+\mathbf{A}^{\top}}2\mathbf{x}$.
:::

La matriz $\frac12(\mathbf{A}+\mathbf{A}^{\top})$ es simétrica. En este capítulo, una forma cuadrática tiene, por ello, siempre una matriz simétrica. Se obtiene de la forma así: en la diagonal están los coeficientes de los cuadrados, y fuera de ella, en cada caso, la mitad del coeficiente del término cruzado.

::::beispiel [Ejemplo numérico]
La forma $3x_1^2-6x_1x_2+x_2^2$ tiene la matriz simétrica $\bigl(\begin{smallmatrix}3&-3\\-3&1\end{smallmatrix}\bigr)$. La forma $x_1^2+2x_2^2+4x_3^2+2x_1x_3$ en $\mathbb{R}^3$ tiene la matriz $\Bigl(\begin{smallmatrix}1&0&1\\0&2&0\\1&0&4\end{smallmatrix}\Bigr)$; el término cruzado $2x_1x_3$ se reparte entre las entradas $(1,3)$ y $(3,1)$.
::::

⁠**En resumen:** Una forma cuadrática solo ve la parte simétrica de su matriz; por eso se escribe siempre con una matriz simétrica.

### Cuenco, canal y silla

<span class="anker" id="stufe-5-3"></span>

Con dos variables, la forma cuadrática puede dibujarse como una superficie sobre el plano, con $f(\mathbf{x})$ como altura, y, como en un mapa, pueden dibujarse sus curvas de nivel, las líneas de igual altura. Lo más sencillo es el caso en que la matriz es diagonal. Entonces no hay términos cruzados, y $f(\mathbf{x})=a_{11}x_1^2+a_{22}x_2^2$. Según los signos de las dos entradas, resultan tres formas básicas (fig. [15](#abb-15)).

:::abbildung ml/k2formen 15
Arriba, las gráficas de las formas cuadráticas $x_1^2+2x_2^2$ (cuenco), $x_1^2$ (canal) y $x_1^2-x_2^2$ (silla) sobre el cuadrado $|x_1|,|x_2|\le1$; abajo, sus curvas de nivel. En el cuenco son elipses ($f=\tfrac14,\tfrac12,1$); en el canal, pares de rectas paralelas, y a trazos la recta $x_1=0$, sobre la que el canal tiene altura cero. En la silla son hipérbolas, intensas para $f=\tfrac14,\tfrac12$ y pálidas para $f=-\tfrac14,-\tfrac12$; a trazos, las dos rectas con $f=0$.
:::

<ul>

<li>

⁠**Cuenco:** Las dos entradas diagonales son positivas, por ejemplo $f=x_1^2+2x_2^2$. Entonces $f(\mathbf{x})>0$ para todo $\mathbf{x}\ne\mathbf{0}$, y solo en el origen es $f=0$. Las curvas de nivel son elipses alrededor del origen, con los semiejes sobre los ejes de coordenadas.

</li>

<li>

⁠**Canal:** Una entrada es positiva y la otra es cero, por ejemplo $f=x_1^2$. Entonces $f\ge0$, pero en toda la recta $x_1=0$ es $f=0$: allí, el fondo del valle de la superficie es una recta. Las curvas de nivel son pares de rectas paralelas.

</li>

<li>

⁠**Silla:** Las entradas tienen signos distintos, por ejemplo $f=x_1^2-x_2^2$. A lo largo del eje $x_1$, la superficie sube hacia ambos lados; a lo largo del eje $x_2$, baja hacia ambos lados. Las curvas de nivel son hipérbolas.

</li>

</ul>

Si las dos entradas son negativas, el cuenco queda boca abajo: es una cúpula. Una entrada negativa y otra nula dan un canal invertido, una cresta. Con más de dos variables vale lo mismo: los signos de las entradas diagonales deciden la forma.

::::beispiel [Ejemplo numérico]
Para el cuenco $f=x_1^2+2x_2^2$, la curva de nivel $f=1$ es la elipse con los semiejes $1$ sobre el eje $x_1$ y $1/\sqrt2\approx0{,}707$ sobre el eje $x_2$: en $(1,\,0)^{\top}$ y en $(0,\,1/\sqrt2)^{\top}$ es $f=1$. En la silla $f=x_1^2-x_2^2$ es $f(1,\,0)=1$, $f(0,\,1)=-1$ y $f(1,\,1)=0$.
::::

⁠**En resumen:** Sin términos cruzados, la forma se lee en los signos de la diagonal: todos positivos, un cuenco; positivo y cero, un canal; signos distintos, una silla.

### Completar cuadrados

<span class="anker" id="stufe-5-4"></span>

Con términos cruzados, la forma ya no se ve a simple vista. ¿Es $5x_1^2+4x_1x_2+2x_2^2$ un cuenco? El término cruzado puede volverse negativo. Del colegio se conoce una herramienta que elimina los términos cruzados: completar cuadrados. Este método escribe la forma como suma de cuadrados, y en los coeficientes de los cuadrados se lee la forma como en la subsección anterior.

:::herleitung Completar cuadrados con dos variables
Sea $a\ne0$. Se saca $a$ factor común de los términos con $x_1$ y se completa un cuadrado:

$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1^2+\frac{2b}ax_1x_2\Bigr)+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2-\frac{b^2}ax_2^2+cx_2^2 .$$

Por tanto,

<span class="anker" id="gl-5-3"></span>
$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2+\Bigl(c-\frac{b^2}a\Bigr)x_2^2 . \tag{5.3}$$
:::

A la derecha hay una suma de dos cuadrados. Las nuevas variables $z_1=x_1+\frac bax_2$ y $z_2=x_2$ toman cualquier par de números cuando $\mathbf{x}$ recorre el plano. La forma en las variables $z_1,z_2$ ya no tiene, por tanto, términos cruzados, y los signos de $a$ y $c-b^2/a$ deciden entre cuenco, canal o silla.

::::beispiel [Ejemplo numérico 1]
$5x_1^2+4x_1x_2+2x_2^2$ tiene $a=5$, $b=2$, $c=2$:

$$5x_1^2+4x_1x_2+2x_2^2=5\,(x_1+0{,}4\,x_2)^2+1{,}2\,x_2^2 .$$

Ambos coeficientes son positivos: la forma es un cuenco. Comprobación en $\mathbf{x}=(1,\,-1)^{\top}$: $5\cdot0{,}36+1{,}2=3$.
::::

::::beispiel [Ejemplo numérico 2]
$x_1^2+6x_1x_2+x_2^2=(x_1+3x_2)^2-8x_2^2$. Los coeficientes tienen signos distintos: una silla. En efecto, $f(1,\,0)=1>0$ y $f(1,\,-1)=1-6+1=-4<0$.
::::

⁠**En resumen:** Completar cuadrados escribe una forma cuadrática como suma de cuadrados; los signos de los coeficientes de los cuadrados muestran si es un cuenco, un canal o una silla.

:::hintergrund Completar cuadrados es la eliminación gaussiana
Los números de [(5.3)](#gl-5-3) son los mismos que en la eliminación gaussiana de [Fundamentos 1, sección 12.3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3), aplicada a la matriz simétrica $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$. Para producir un cero debajo de la diagonal, se resta de la segunda fila $\frac ba$ veces la primera y se obtiene $\bigl(\begin{smallmatrix}a&b\\0&c-b^2/a\end{smallmatrix}\bigr)$. Las entradas diagonales de esta forma escalonada, los llamados pivotes, son exactamente los coeficientes de los cuadrados, y el factor de eliminación $\frac ba$ está en el primer paréntesis. Para la matriz $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$: factor $0{,}4$, pivotes $5$ y $1{,}2$. Con $n$ variables se continúa del mismo modo: cada paso de eliminación completa el cuadrado de una variable. La forma es un cuenco si y solo si todos los pivotes son positivos. El producto de los pivotes es, según las reglas de cálculo de [Fundamentos 1, sección 14.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), el determinante, aquí $5\cdot1{,}2=6=5\cdot2-2\cdot2$.
:::

:::aufgabe Ejercicio 14 ★ Formas y matrices
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Da la matriz simétrica de las formas $2x_1^2-2x_1x_2+3x_2^2$ y $x_1x_2$.

</li>

<li>

Calcula la forma de $\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)$ y su matriz simétrica.

</li>

<li>

Determina sin hacer cálculos si $3x_1^2+x_2^2$, $-x_1^2$ y $2x_1^2-x_2^2+x_3^2$ son un cuenco, un canal, una silla u otra cosa.

</li>

</ol>

:::loesung
(a) En la diagonal, los coeficientes de los cuadrados; fuera de ella, la mitad del coeficiente del término cruzado: $2x_1^2-2x_1x_2+3x_2^2$ tiene la matriz $\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$, y $x_1x_2$ tiene $\bigl(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\bigr)$.

(b) $\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)\mathbf{x}=x_1^2+(3-1)\,x_1x_2+2x_2^2=x_1^2+2x_1x_2+2x_2^2$. La matriz simétrica es $\tfrac12(\mathbf{A}+\mathbf{A}^{\top})=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)$.

(c) $3x_1^2+x_2^2$: ambos coeficientes positivos, un cuenco. $-x_1^2$: un coeficiente negativo y otro nulo; por tanto, un canal invertido, una cresta a lo largo del eje $x_2$. $2x_1^2-x_2^2+x_3^2$: signos mezclados, una silla; a lo largo de $x_1$ y de $x_3$ la forma sube, a lo largo de $x_2$ baja.
:::
:::

:::aufgabe Ejercicio 15 ★★ Completar cuadrados
<span class="anker" id="aufg-15"></span>

Completa cuadrados y decide de qué forma se trata:

$$f_1=2x_1^2+8x_1x_2+11x_2^2,\qquad f_2=x_1^2+4x_1x_2+4x_2^2,\qquad f_3=x_1^2+4x_1x_2+x_2^2 .$$

En el canal, da la recta sobre la que $f=0$, y en la silla, un punto con $f<0$.

:::loesung
Con [(5.3)](#gl-5-3):

<ul>

<li>

$f_1$: $a=2$, $b=4$, $c=11$; por tanto, $f_1=2(x_1+2x_2)^2+(11-8)\,x_2^2=2(x_1+2x_2)^2+3x_2^2$. Ambos coeficientes positivos: un cuenco.

</li>

<li>

$f_2=(x_1+2x_2)^2+0\cdot x_2^2$: un canal. Vale cero sobre la recta $x_1+2x_2=0$, es decir, en la dirección de $(2,\,-1)^{\top}$.

</li>

<li>

$f_3=(x_1+2x_2)^2-3x_2^2$: signos distintos, una silla. Si se eligen $x_2=1$ y $x_1=-2$, el primer cuadrado se anula: $f_3(-2,\,1)=4-8+1=-3<0$.

</li>

</ul>
:::
:::

:::aufgabe Ejercicio 16 ★★ Bobinas acopladas
<span class="anker" id="aufg-16"></span>

Dos bobinas acopladas tienen $L_1=4\,\mathrm{mH}$ y $L_2=1\,\mathrm{mH}$.

<ol class="al">

<li>

Completa cuadrados en la energía $W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2$.

</li>

<li>

¿Para qué valores de $M$ es $W>0$ para todas las corrientes $(i_1,\,i_2)\ne(0,\,0)$? ¿Qué se deduce de ello para el coeficiente de acoplamiento $k=M/\sqrt{L_1L_2}$?

</li>

</ol>

:::loesung
(a) En [(5.3)](#gl-5-3) es $a=\tfrac12L_1$, $2b=M$ y $c=\tfrac12L_2$; por tanto, $b/a=M/L_1$ y $b^2/a=M^2/(2L_1)$:

$$W=\tfrac12L_1\Bigl(i_1+\frac M{L_1}\,i_2\Bigr)^2+\tfrac12\Bigl(L_2-\frac{M^2}{L_1}\Bigr)i_2^2=2\,\mathrm{mH}\,\Bigl(i_1+\frac M{4\,\mathrm{mH}}\,i_2\Bigr)^2+\Bigl(\frac12\,\mathrm{mH}-\frac{M^2}{8\,\mathrm{mH}}\Bigr)i_2^2 .$$

(b) El primer coeficiente es positivo. Se cumple $W>0$ para todas las corrientes $\ne(0,\,0)$ si y solo si también el segundo es positivo: $L_2-M^2/L_1>0$, es decir, $M^2<L_1L_2=4\,(\mathrm{mH})^2$ y $|M|<2\,\mathrm{mH}$. Para el coeficiente de acoplamiento, esto significa $|k|=|M|/\sqrt{L_1L_2}<1$. Con $|k|=1$, el acoplamiento perfecto ideal, la forma sería solo un canal: para la relación de corrientes adecuada, $i_1=-\tfrac M{L_1}\,i_2$, la energía almacenada sería cero. Que la energía de un campo magnético nunca sea negativa obliga, por tanto, a que $|k|\le1$.
:::
:::
