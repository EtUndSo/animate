---
title: La matriz hessiana y la aproximación cuadrática
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230900
summary: El gradiente describe la inclinación del terreno, pero no su curvatura.
tags: derivadas parciales segundas, matriz hessiana, diferencia mixta, segunda derivada direccional
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
El gradiente describe la inclinación del terreno, pero no su curvatura. Las derivadas parciales segundas las reúne la matriz hessiana. Es simétrica, y con ella la aproximación lineal pasa a ser cuadrática. Sus valores propios dicen con qué intensidad se curva el terreno en distintas direcciones, y enlazan esta sección con las formas cuadráticas del [capítulo 2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html).
:::

### Derivadas parciales segundas

<span class="anker" id="stufe-8-1"></span>

Las derivadas parciales $\partial_jf$ son a su vez funciones de $\mathbf{x}$. Se pueden derivar parcialmente otra vez, respecto de la misma variable o respecto de otra. Esto describe cómo cambia la pendiente en la dirección $x_j$ cuando se avanza en la dirección $x_i$.

:::definition Definición 8.1 (Derivadas parciales segundas)
<span class="anker" id="satz-8-1"></span>

Las __derivadas parciales segundas__ de $f:\mathbb{R}^d\to\mathbb{R}$ son

<span class="anker" id="gl-8-1"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial}{\partial x_i}\Bigl(\frac{\partial f}{\partial x_j}\Bigr), \tag{8.1}$$

es decir, se deriva primero respecto de $x_j$ y después respecto de $x_i$. Para $i=j$ se escribe $\partial^2f/\partial x_i^2$. Para $i\ne j$ se llaman derivadas cruzadas.
:::

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ se tiene $\partial_1f=2x_1x_2$ y $\partial_2f=x_1^2+2x_2$, es decir,

$$\begin{gathered} \frac{\partial^2f}{\partial x_1^2}=\frac{\partial}{\partial x_1}(2x_1x_2)=2x_2,\qquad \frac{\partial^2f}{\partial x_2\,\partial x_1}=\frac{\partial}{\partial x_2}(2x_1x_2)=2x_1,\\ \frac{\partial^2f}{\partial x_1\,\partial x_2}=\frac{\partial}{\partial x_1}(x_1^2+2x_2)=2x_1,\qquad \frac{\partial^2f}{\partial x_2^2}=\frac{\partial}{\partial x_2}(x_1^2+2x_2)=2 . \end{gathered}$$

En el punto $(1,\,2)$ valen $4$, $2$, $2$ y $2$. Las dos derivadas cruzadas son iguales, aunque han surgido por caminos distintos.
::::

⁠**En resumen:** Las derivadas parciales segundas vuelven a derivar parcialmente una derivada parcial; las cruzadas describen cómo cambia la pendiente en una dirección al avanzar en otra.

### La matriz hessiana

<span class="anker" id="stufe-8-2"></span>

Una función de $d$ variables tiene $d^2$ derivadas parciales segundas. Igual que las primeras derivadas en el gradiente, se reúnen en un solo objeto, aquí en una matriz cuadrada.

:::definition Definición 8.2 (Matriz hessiana)
<span class="anker" id="satz-8-2"></span>

La matriz $d\times d$

<span class="anker" id="gl-8-2"></span>
$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\cdots&\dfrac{\partial^2f}{\partial x_1\,\partial x_d}\\ \vdots&&\vdots\\ \dfrac{\partial^2f}{\partial x_d\,\partial x_1}&\cdots&\dfrac{\partial^2f}{\partial x_d^2}\end{pmatrix},\qquad \bigl(\mathbf{H}_f(\mathbf{x})\bigr)_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}), \tag{8.2}$$

se llama la __matriz hessiana__ de $f$ en el punto $\mathbf{x}$.
:::

La matriz debe su nombre al matemático Otto Hesse; algunos libros escriben $\nabla^2f$. Su columna $j$ es el gradiente de la función $\partial_jf$. Por ello está estrechamente emparentada con la matriz jacobiana del gradiente, la función vectorial $\mathbf{x}\mapsto\nabla f(\mathbf{x})$: la entrada $(i,j)$ de esta última es $\partial(\partial_if)/\partial x_j$, la derivada en el otro orden. La subsección siguiente muestra que ambos órdenes dan casi siempre lo mismo; entonces la matriz hessiana es la matriz jacobiana del gradiente.

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$, según la subsección anterior,

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}2x_2&2x_1\\2x_1&2\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}4&2\\2&2\end{pmatrix}.$$

Para una función cuadrática $f(\mathbf{x})=\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ con $\mathbf{A}$ simétrica, según la sección [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7), $\nabla f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ y, por tanto, $\mathbf{H}_f=\mathbf{A}$ en todos los puntos. Para el cuenco $x_1^2+4x_2^2$ de la sección [4](richtungsableitung-und-steilster-anstieg.html#stufe-4), $\mathbf{A}=\operatorname{diag}(2;\,8)$.
::::

⁠**En resumen:** La matriz hessiana reúne todas las derivadas parciales segundas; en una función cuadrática $\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ es $\mathbf{A}$ en todas partes.

### El teorema de Schwarz

<span class="anker" id="stufe-8-3"></span>

En el ejemplo numérico, las dos derivadas cruzadas eran iguales. No es casualidad, sino que vale para todas las funciones cuyas segundas derivadas no tienen saltos.

:::satz Teorema 8.3 (Teorema de Schwarz)
<span class="anker" id="satz-8-3"></span>

Si todas las derivadas parciales segundas de $f$ existen cerca de $\mathbf{x}$ y son continuas en el punto $\mathbf{x}$, entonces allí se cumple

<span class="anker" id="gl-8-3"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial^2f}{\partial x_j\,\partial x_i} \tag{8.3}$$

para todos los $i,j$. La matriz hessiana es entonces simétrica.
:::

La razón se ve en un cálculo en el que el orden ni siquiera aparece. Uno se desplaza desde $\mathbf{x}$ en $h$ en la dirección $x_1$ y en $k$ en la dirección $x_2$, y forma la __diferencia mixta__

$$\Delta(h,k)=f(x_1+h,\,x_2+k)-f(x_1+h,\,x_2)-f(x_1,\,x_2+k)+f(x_1,\,x_2).$$

Si se agrupa el primer sumando con el tercero y el segundo con el cuarto, $\Delta$ es la variación de la diferencia $f(x_1+h,\cdot)-f(x_1,\cdot)$ al dar el paso $k$ en la dirección $x_2$: ¿cómo cambia el incremento en la dirección $x_1$ cuando se avanza en la dirección $x_2$? Si se divide entre $hk$, para $h$ y $k$ pequeños esto se acerca a la derivada primero respecto de $x_1$ y después respecto de $x_2$. Si, en cambio, se agrupan los dos primeros y los dos últimos sumandos, el mismo número se lee como variación del incremento en la dirección $x_2$ al dar el paso en la dirección $x_1$, y el cociente se acerca a la derivada en el otro orden. Ambos límites pertenecen al mismo número $\Delta/(hk)$. La continuidad garantiza que el orden de los dos pasos al límite no importa.

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$ con $h=k=0{,}1$ se tiene

$$\Delta=f(1{,}1;\ 2{,}1)-f(1{,}1;\ 2)-f(1;\ 2{,}1)+f(1,2)=6{,}951-6{,}42-6{,}51+6=0{,}021,$$

es decir, $\Delta/(hk)=2{,}1$, cerca de la derivada cruzada $2x_1=2$. La desviación se debe a que $2x_1$ no es constante entre $x_1=1$ y $x_1=1{,}1$.
::::

⁠**En resumen:** Con segundas derivadas continuas, el orden de derivación es indiferente, y la matriz hessiana es simétrica.

:::hintergrund Cuando las segundas derivadas no son continuas
Sin continuidad, el teorema puede ser falso. El contraejemplo clásico es $f(x_1,x_2)=x_1x_2\,\frac{x_1^2-x_2^2}{x_1^2+x_2^2}$ con $f(0,0)=0$. Si se calculan las primeras derivadas parciales sobre los ejes, resulta $\partial_1f(0,x_2)=-x_2$ y $\partial_2f(x_1,0)=x_1$. Si se deriva la primera respecto de $x_2$, se obtiene $-1$ en el origen; si se deriva la segunda respecto de $x_1$, se obtiene $+1$. Las derivadas cruzadas en el origen son, pues, distintas, porque allí las segundas derivadas saltan. En las funciones de este capítulo sin puntos angulosos esto no ocurre; están construidas a partir de polinomios, funciones exponenciales y operaciones aritméticas básicas, y tienen derivadas continuas de cualquier orden en todos los puntos donde están definidas.
:::

### La aproximación cuadrática

<span class="anker" id="stufe-8-4"></span>

En una variable, la recta tangente se mejoró en la sección [1.5](die-ableitung.html#stufe-1-5) mediante una parábola. Con varias variables, el lugar del plano tangente lo ocupa una superficie curvada, cuya curvatura describe la matriz hessiana.

:::satz Teorema 8.4 (Aproximación cuadrática)
<span class="anker" id="satz-8-4"></span>

Si $f$ tiene derivadas parciales segundas continuas cerca de $\mathbf{x}$, se cumple

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{h}+r_2(\mathbf{h})\qquad\text{con}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{r_2(\mathbf{h})}{\lVert\mathbf{h}\rVert^2}=0 . \tag{8.4}$$
:::

:::herleitung La aproximación cuadrática a lo largo de una recta
Se restringe $f$ a la recta que pasa por $\mathbf{x}$ en la dirección $\mathbf{h}$: $\phi(t)=f(\mathbf{x}+t\,\mathbf{h})$. Es una función de una variable. Según [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), $\phi'(t)=\nabla f(\mathbf{x}+t\mathbf{h})^{\top}\mathbf{h}=\sum_jh_j\,\partial_jf(\mathbf{x}+t\mathbf{h})$. Cada sumando se deriva otra vez con [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), esta vez para la función $\partial_jf$:

$$\phi''(t)=\sum_{j=1}^dh_j\sum_{i=1}^d\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}+t\mathbf{h})\,h_i=\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x}+t\mathbf{h})\,\mathbf{h} .$$

La aproximación cuadrática [(1.6)](die-ableitung.html#gl-1-6) de $\phi$ en el punto $0$, evaluada en $t=1$, es $\phi(1)\approx\phi(0)+\phi'(0)+\tfrac12\phi''(0)$, y eso es [(8.4)](#gl-8-4). Que el error desaparezca más rápido que $\lVert\mathbf{h}\rVert^2$ se sigue de la continuidad de las segundas derivadas.
:::

El nuevo término $\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ es una forma cuadrática en el sentido del [capítulo 2, sección 5.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), con la matriz hessiana como matriz. Cerca de $\mathbf{x}$, la función tiene, pues, el aspecto de un plano más una forma cuadrática.

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$ y $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$, como en la sección [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4), se tiene

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(4\cdot0{,}01^2+2\cdot2\cdot0{,}01\cdot0{,}02+2\cdot0{,}02^2\bigr)=\tfrac12\,(0{,}0004+0{,}0008+0{,}0008)=0{,}001$$

(fig. [15](#abb-15)). La aproximación cuadrática es $6+0{,}14+0{,}001=6{,}141$; el valor exacto, $6{,}141002$. El error bajó de $0{,}001002$ a $0{,}000002$. El resto es el término de tercer orden: en $x_1^2x_2$ está el sumando $h_1^2h_2=0{,}0001\cdot0{,}02=0{,}000002$, que ninguna aproximación cuadrática recoge.

:::abbildung ml/k3rtaylor2 15
El término de curvatura de la aproximación cuadrática como suma doble; los dos sumandos cruzados $h_1\cdot2\cdot h_2$ y $h_2\cdot2\cdot h_1$ están agrupados en el término central.
:::
::::

⁠**En resumen:** Cerca de $\mathbf{x}$, $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{h}$: plano más forma cuadrática.

### La curvatura en una dirección

<span class="anker" id="stufe-8-5"></span>

¿Cuánto se curva el terreno si se avanza desde $\mathbf{x}$ en la dirección $\mathbf{u}$? La deducción de la subsección anterior ya ha dado la respuesta: la segunda derivada de $\phi(t)=f(\mathbf{x}+t\mathbf{u})$ en el punto $0$ es $\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{u}$.

:::definition Definición 8.5 (Curvatura en una dirección)
<span class="anker" id="satz-8-5"></span>

Para un vector $\mathbf{u}$ de longitud $1$, el número

<span class="anker" id="gl-8-5"></span>
$$\frac{\mathrm{d}^2}{\mathrm{d} t^2}f(\mathbf{x}+t\,\mathbf{u})\Big|_{t=0}=\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u} \tag{8.5}$$

se llama la __segunda derivada direccional__ de $f$ en el punto $\mathbf{x}$ en la dirección $\mathbf{u}$. Mide la curvatura de la curva de corte en esa dirección.
:::

Con los resultados del [capítulo 2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) puede decirse de inmediato cuánto vale esta curvatura como máximo y como mínimo. La matriz hessiana es simétrica y, según el teorema espectral del [capítulo 2, sección 7.6](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6), tiene valores propios reales y vectores propios perpendiculares entre sí.

:::satz Teorema 8.6 (Curvatura y valores propios)
<span class="anker" id="satz-8-6"></span>

Sean $\lambda_{\min}$ y $\lambda_{\max}$ el menor y el mayor valor propio de la matriz hessiana simétrica $\mathbf{H}_f(\mathbf{x})$. Entonces, para toda dirección $\mathbf{u}$ con $\lVert\mathbf{u}\rVert=1$, se cumple

<span class="anker" id="gl-8-6"></span>
$$\lambda_{\min}\le\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u}\le\lambda_{\max}. \tag{8.6}$$

En la dirección de un vector propio, la curvatura es exactamente el valor propio correspondiente. Si $\mathbf{H}_f(\mathbf{x})$ es definida positiva, la curvatura es positiva en todas las direcciones; si es indefinida, el terreno se curva hacia arriba en algunas direcciones y hacia abajo en otras.
:::

La desigualdad es el enunciado sobre el mayor y el menor valor de una forma cuadrática sobre la circunferencia unidad del [capítulo 2, sección 8.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5). Para un vector propio $\mathbf{u}$ del valor propio $\lambda$ se tiene $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\lambda\,\mathbf{u}^{\top}\mathbf{u}=\lambda$. Los conceptos de definida positiva e indefinida proceden del [capítulo 2, sección 8](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8); allí, el aspecto de una forma cuadrática se leía en sus valores propios: cuenco, canal o silla. A través de la aproximación cuadrática [(8.4)](#gl-8-4), esto se traslada al terreno cerca de $\mathbf{x}$: con una matriz hessiana definida positiva, las curvas de nivel del término de curvatura son elipses cuyos ejes principales, según el [capítulo 2, sección 7.7](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7), están en la dirección de los vectores propios y son cortos en la dirección de mayor curvatura.

::::beispiel [Ejemplo numérico 1]
Para el cuenco $f(\mathbf{x})=x_1^2+4x_2^2$ se tiene $\mathbf{H}_f=\operatorname{diag}(2;\,8)$, con los valores propios $2$ y $8$. En la dirección $x_1$ la curvatura es $2$; en la dirección $x_2$, $8$; y en la dirección $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$, $\tfrac12(2+8)=5$. Esto explica las curvas de nivel alargadas de la sección [4.4](richtungsableitung-und-steilster-anstieg.html#stufe-4-4): en la dirección $x_2$, el cuenco se curva cuatro veces más, sus paredes son allí más empinadas y las elipses son estrechas en esa dirección.
::::

::::beispiel [Ejemplo numérico 2]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$ se tiene $\mathbf{H}_f=\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$. La traza $6$ y el determinante $4$ dan, según el [capítulo 2, sección 6.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5), los valores propios $3\pm\sqrt5$, es decir, aproximadamente $5{,}236$ y $0{,}764$. Ambos son positivos, y la matriz hessiana es definida positiva: cerca de $(1,\,2)$, el terreno se curva hacia arriba en todas las direcciones. En la dirección $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$, la curvatura es

$$\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\tfrac12\,(4+2+2+2)=5,$$

y está entre $0{,}764$ y $5{,}236$ (fig. [16](#abb-16)).

:::abbildung ml/k3rkruemmung 16
La curvatura de $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$ en la dirección de la bisectriz; el factor $\tfrac12$ procede de $u_iu_j=\tfrac12$.
:::
::::

⁠**En resumen:** La curvatura en la dirección $\mathbf{u}$ es $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$; está entre el menor y el mayor valor propio de la matriz hessiana, y los signos de estos deciden si el terreno se curva como un cuenco o como una silla.

:::hintergrund Matriz hessiana por vector, sin la matriz hessiana
Con muchas variables, la matriz hessiana es enorme: con un millón de variables tiene $10^{12}$ entradas. Pero a menudo solo se necesita su producto por un vector $\mathbf{v}$. Este se obtiene sin construir la matriz. El número $\nabla f(\mathbf{x})^{\top}\mathbf{v}=\sum_jv_j\,\partial_jf(\mathbf{x})$ es una función de $\mathbf{x}$, y su gradiente tiene las componentes $\sum_jv_j\,\partial^2f/\partial x_i\partial x_j$; por tanto, $\nabla_{\mathbf{x}}\bigl(\nabla f(\mathbf{x})^{\top}\mathbf{v}\bigr)=\mathbf{H}_f(\mathbf{x})\,\mathbf{v}$. Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ y $\mathbf{v}=(1,\,1)^{\top}$ se tiene $\nabla f^{\top}\mathbf{v}=2x_1x_2+x_1^2+2x_2$, con el gradiente $(2x_2+2x_1,\ 2x_1+2)^{\top}$, es decir, $(6,\,4)^{\top}$ en el punto $(1,\,2)$, y esto es $\mathbf{H}_f\mathbf{v}=(4+2,\ 2+2)^{\top}$. Se calculan, pues, dos gradientes en lugar de una matriz con $d^2$ entradas.
:::

:::aufgabe Ejercicio 28 ★ Matrices hessianas
<span class="anker" id="aufg-28"></span>

Calcula la matriz hessiana en el punto indicado y comprueba la simetría.

<ol class="al">

<li>

$f(\mathbf{x})=x_1^3+x_1x_2^2$ en el punto $(1,\,2)$;

</li>

<li>

$f(\mathbf{x})=\mathrm{e}^{x_1+2x_2}$ en el punto $(0,\,0)$. ¿Qué rango tiene la matriz?

</li>

<li>

$f(\mathbf{x})=x_1x_2x_3$ en el punto $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3x_1^2+x_2^2$ y $\partial_2f=2x_1x_2$, así que

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}6x_1&2x_2\\2x_2&2x_1\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}6&4\\4&2\end{pmatrix};$$

las derivadas cruzadas $\partial_2(3x_1^2+x_2^2)=2x_2$ y $\partial_1(2x_1x_2)=2x_2$ son iguales.

(b) Con $f=\mathrm{e}^{x_1+2x_2}$ se tiene $\partial_1f=f$ y $\partial_2f=2f$, así que $\mathbf{H}_f=f\cdot\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ y, en el origen, $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$. La segunda fila es el doble de la primera; el rango es $1$, y los valores propios son $5$ y $0$. Esto encaja: $f$ solo depende de $x_1+2x_2$ y es constante a lo largo de la dirección $(2,\,-1)^{\top}$; en ella, por tanto, no está curvada.

(c) $\partial_1f=x_2x_3$, $\partial_2f=x_1x_3$, $\partial_3f=x_1x_2$, así que

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}0&x_3&x_2\\x_3&0&x_1\\x_2&x_1&0\end{pmatrix},\qquad \mathbf{H}_f(1,2,3)=\begin{pmatrix}0&3&2\\3&0&1\\2&1&0\end{pmatrix}.$$
:::
:::

:::aufgabe Ejercicio 29 ★★ Aproximación cuadrática
<span class="anker" id="aufg-29"></span>

Sea $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ como en el ejercicio [10](partielle-ableitungen-und-der-gradient.html#aufg-10).

<ol class="al">

<li>

Calcula $\mathbf{H}_f(2,0)$.

</li>

<li>

Calcula con la aproximación cuadrática en el punto $(2,\,0)$ un valor aproximado de $f(2{,}1;\ -0{,}05)$ y compáralo con la aproximación lineal del ejercicio [10](partielle-ableitungen-und-der-gradient.html#aufg-10) y con el valor exacto.

</li>

</ol>

:::loesung
(a) $\partial_1^2f=0$, $\partial_1\partial_2f=\mathrm{e}^{x_2}$, $\partial_2^2f=x_1\mathrm{e}^{x_2}$, así que $\mathbf{H}_f(2,0)=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$.

(b) Con $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$ se tiene

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(0+2\cdot1\cdot0{,}1\cdot(-0{,}05)+2\cdot0{,}05^2\bigr)=\tfrac12\,(-0{,}01+0{,}005)=-0{,}0025 .$$

La aproximación cuadrática es $2+0-0{,}0025=1{,}9975$; la lineal era $2{,}0$, y el valor exacto es $1{,}997582$. El error baja de $0{,}0024$ a $0{,}00008$. El término cruzado $-0{,}005$ es la interacción del ejercicio [10](partielle-ableitungen-und-der-gradient.html#aufg-10).
:::
:::

:::aufgabe Ejercicio 30 ★★ Curvaturas de un cuenco oblicuo
<span class="anker" id="aufg-30"></span>

Sea $f(\mathbf{x})=x_1^2+4x_2^2+x_1x_2$.

<ol class="al">

<li>

Escribe $f$ como $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ y da $\mathbf{H}$.

</li>

<li>

Calcula los valores propios de $\mathbf{H}$ y las curvaturas en las direcciones $\mathbf{e}_1$, $\mathbf{e}_2$ y $(1,\,-1)^{\top}/\sqrt2$. Comprueba [(8.6)](#gl-8-6).

</li>

<li>

¿En qué dirección es máxima la curvatura? Da un vector propio.

</li>

</ol>

:::loesung
(a) $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ con $\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&8\end{smallmatrix}\bigr)$ da $\tfrac12\,(2x_1^2+2x_1x_2+8x_2^2)=x_1^2+x_1x_2+4x_2^2$. Esta es también la matriz hessiana de $f$.

(b) Traza $10$, determinante $16-1=15$, así que $\lambda^2-10\lambda+15=0$ y $\lambda=5\pm\sqrt{10}$, aproximadamente $8{,}162$ y $1{,}838$. Las curvaturas son $\mathbf{e}_1^{\top}\mathbf{H}\mathbf{e}_1=2$, $\mathbf{e}_2^{\top}\mathbf{H}\mathbf{e}_2=8$ y, para $\mathbf{u}=(1,\,-1)^{\top}/\sqrt2$, $\tfrac12\,(2-1-1+8)=4$. Las tres están entre $1{,}838$ y $8{,}162$.

(c) La curvatura es máxima en la dirección de un vector propio de $\lambda=5+\sqrt{10}$. De la primera fila de $(\mathbf{H}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ se sigue $(2-\lambda)v_1+v_2=0$, es decir, $\mathbf{v}=(1;\ 3+\sqrt{10})^{\top}\approx(1;\ 6{,}162)^{\top}$; normalizado, aproximadamente $(0{,}160;\ 0{,}987)^{\top}$. Es casi la dirección $x_2$, girada un poco por el término cruzado $x_1x_2$.
:::
:::

:::aufgabe Ejercicio 31 ★★★ Derivadas cruzadas distintas
<span class="anker" id="aufg-31"></span>

Sea $f(x_1,x_2)=x_1x_2\,\dfrac{x_1^2-x_2^2}{x_1^2+x_2^2}$ para $\mathbf{x}\ne\mathbf{0}$ y $f(0,0)=0$.

<ol class="al">

<li>

Demuestra con el cociente incremental que $\partial_1f(0,x_2)=-x_2$ para $x_2\ne0$ y que $\partial_1f(0,0)=0$. Calcula del mismo modo $\partial_2f(x_1,0)$.

</li>

<li>

Deduce que las dos derivadas cruzadas en el origen son $-1$ y $+1$. ¿Qué hipótesis del teorema de Schwarz no se cumple?

</li>

</ol>

:::loesung
(a) Sobre el eje $x_1=0$ se tiene $f=0$. Para $x_2\ne0$ se tiene

$$\partial_1f(0,x_2)=\lim_{h\to0}\frac{f(h,x_2)-0}{h}=\lim_{h\to0}x_2\,\frac{h^2-x_2^2}{h^2+x_2^2}=x_2\cdot\frac{-x_2^2}{x_2^2}=-x_2 .$$

En el origen, $f(h,0)=0$, así que $\partial_1f(0,0)=0$; la fórmula $-x_2$ vale, por tanto, también para $x_2=0$. Del mismo modo, $\partial_2f(x_1,0)=\lim_k x_1\frac{x_1^2-k^2}{x_1^2+k^2}=x_1$.

(b) Derivando primero respecto de $x_1$ y después respecto de $x_2$: $\frac{\partial}{\partial x_2}(-x_2)=-1$. Primero respecto de $x_2$ y después respecto de $x_1$: $\frac{\partial}{\partial x_1}(x_1)=+1$. Las derivadas cruzadas en el origen son distintas. La hipótesis que no se cumple es la continuidad de las segundas derivadas en el origen: fuera del origen, la derivada cruzada vale $-1$ en todo el eje $x_2$ y $+1$ en todo el eje $x_1$. Por tanto, salta en el origen, y los dos órdenes de derivación se acercan a él desde lados distintos.
:::
:::
