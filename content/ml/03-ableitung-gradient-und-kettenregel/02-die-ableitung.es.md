---
title: La derivada
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230200
summary: La derivada mide con qué intensidad reacciona una función de una variable a una pequeña variación de su entrada.
tags: recta secante, cociente incremental, límite, derivable, derivada, recta tangente, punto anguloso, aproximación lineal
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
La derivada mide con qué intensidad reacciona una función de una variable a una pequeña variación de su entrada. Esta sección la introduce como límite de pendientes, la interpreta como la pendiente de la recta que mejor se ajusta a la curva y aporta las reglas de cálculo con las que se calculan derivadas sin tener que calcular un límite cada vez. Al final aparece la segunda derivada, que describe cómo cambia la propia pendiente.
:::

### Tasa de variación y cociente incremental

<span class="anker" id="stufe-1-1"></span>

Una función $f$ asigna a cada número $x$ un número $f(x)$. Si se aumenta $x$ en un pequeño trozo $h$, por lo general también cambia el valor, concretamente en $f(x+h)-f(x)$. Si eso es mucho o poco solo lo dice la comparación con $h$: una variación del valor de $0{,}1$ es grande si $x$ solo ha crecido $0{,}001$, y pequeña si $x$ ha crecido $100$. Por eso se dividen las dos variaciones una entre otra.

En la imagen de la gráfica, esto es una pendiente. Se traza una recta por los dos puntos $(x,\,f(x))$ y $(x+h,\,f(x+h))$ de la gráfica. Una recta así, que pasa por dos puntos de una curva, se llama __recta secante__. Su pendiente es la diferencia de altura entre los dos puntos dividida entre su distancia horizontal. Indica cuánto sube la gráfica, en promedio, entre los dos puntos.

:::definition Definición 1.1 (Cociente incremental)
<span class="anker" id="satz-1-1"></span>

Para una función $f$, un punto $x$ y un número $h\ne0$, se llama

<span class="anker" id="gl-1-1"></span>
$$\frac{f(x+h)-f(x)}{h} \tag{1.1}$$

__cociente incremental__ de $f$ en el punto $x$ con paso $h$. Es la pendiente de la recta secante que pasa por $(x,\,f(x))$ y $(x+h,\,f(x+h))$.
:::

El paso $h$ también puede ser negativo; entonces el segundo punto está a la izquierda de $x$. Para $h=0$, el cociente no está definido, porque no se puede dividir entre cero.

::::beispiel [Ejemplo numérico]
Sea $f(x)=x^3$ y $x=2$, es decir, $f(2)=8$. Para tres pasos se tiene

$$\frac{3^3-8}{1}=19,\qquad \frac{2{,}5^3-8}{0{,}5}=\frac{15{,}625-8}{0{,}5}=15{,}25,\qquad \frac{2{,}1^3-8}{0{,}1}=\frac{9{,}261-8}{0{,}1}=12{,}61 .$$

Las secantes se vuelven más planas cuanto más se acerca el segundo punto a $(2,\,8)$ (fig. [1](#abb-1)). Para un $h$ cualquiera se calcula con $(2+h)^3=8+12h+6h^2+h^3$:

<span class="anker" id="gl-1-2"></span>
$$\frac{(2+h)^3-8}{h}=\frac{12h+6h^2+h^3}{h}=12+6h+h^2 . \tag{1.2}$$

Con $h=1$, $h=0{,}5$ y $h=0{,}1$, esta fórmula vuelve a dar $19$, $15{,}25$ y $12{,}61$. Con $h=0{,}01$ da $12{,}0601$; con $h=-0{,}1$ da $12-0{,}6+0{,}01=11{,}41$.

:::abbildung ml/k3sekante 1
Rectas secantes de la gráfica de $f(x)=x^3$ que pasan por el punto $(2,\,8)$, con las pendientes $19$ para $h=1$ (rojo) y $15{,}25$ para $h=0{,}5$ (naranja). Con un paso $h$ más pequeño, el segundo punto se acerca, la secante se vuelve más plana y su pendiente $12+6h+h^2$ se aproxima a la pendiente $12$ de la recta tangente (discontinua).
:::
::::

⁠**En resumen:** El cociente incremental es la variación del valor de la función dividida entre la variación de la entrada: la pendiente media entre dos puntos de la gráfica.

### La derivada

<span class="anker" id="stufe-1-2"></span>

En el ejemplo numérico, las pendientes de las secantes están tanto más cerca de $12$ cuanto menor es $|h|$, y eso por ambos lados: $12{,}61$ para $h=0{,}1$, $11{,}41$ para $h=-0{,}1$. El valor $12$ mismo no lo alcanzan para ningún $h\ne0$, pero se acercan a él arbitrariamente. Por eso se llama a $12$ el límite de las pendientes de las secantes. En general, una magnitud que depende de $h$ tiene para $h\to0$ el __límite__ $c$ si está arbitrariamente cerca de $c$ en cuanto $h$ está lo bastante cerca de $0$ sin ser igual a $0$. Para ello cuentan por igual los $h$ positivos y los negativos.

:::definition Definición 1.2 (Derivada)
<span class="anker" id="satz-1-2"></span>

Una función $f$ se llama __derivable__ en el punto $x$ si el cociente incremental tiene un límite para $h\to0$. Este límite

<span class="anker" id="gl-1-3"></span>
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h} \tag{1.3}$$

se llama la __derivada__ de $f$ en el punto $x$. También se escribe $\frac{\mathrm{d} f}{\mathrm{d} x}(x)$. La recta que pasa por $(x,\,f(x))$ con pendiente $f'(x)$ se llama __recta tangente__ a la gráfica.
:::

Si $f$ es derivable en todos los puntos, $f'$ es a su vez una función: asigna a cada $x$ la pendiente de la gráfica en ese punto. Se llama función derivada o, abreviadamente, también derivada. La notación $\frac{\mathrm{d} f}{\mathrm{d} x}$ recuerda al cociente de [(1.1)](#gl-1-1), pero no es en sí una fracción, sino el símbolo del límite.

::::beispiel [Ejemplo numérico 1]
Según [(1.2)](#gl-1-2), el cociente incremental de $f(x)=x^3$ en el punto $2$ es igual a $12+6h+h^2$. Para $h\to0$, $6h$ y $h^2$ se hacen arbitrariamente pequeños; luego $f'(2)=12$. El mismo cálculo en un punto $x$ cualquiera da, con $(x+h)^3=x^3+3x^2h+3xh^2+h^3$, el cociente $3x^2+3xh+h^2$ y, por tanto, $f'(x)=3x^2$.
::::

No toda función es derivable en todas partes. Una excepción típica es un __punto anguloso__: un punto en el que la gráfica continúa sin salto, pero a su izquierda tiene una pendiente distinta que a su derecha. Allí, las pendientes de las secantes con $h>0$ se aproximan a la pendiente de la derecha, y las de $h<0$, a la de la izquierda. Como ambas son distintas, no hay un límite común y, por tanto, no hay derivada; ninguna recta se ajusta a la vez a ambos lados. El ejemplo más conocido es la función valor absoluto $|x|$ en el punto $0$.

::::beispiel [Ejemplo numérico 2]
La función valor absoluto $f(x)=|x|$ no tiene derivada en el punto $0$. Su cociente incremental es $|h|/h$, es decir, $1$ para todo $h>0$ y $-1$ para todo $h<0$. No hay ningún número al que se acerque por ambos lados. La gráfica tiene en $0$ un punto anguloso: a la izquierda su pendiente es $-1$; a la derecha, $+1$. En cualquier otro punto, $|x|$ es derivable, con derivada $1$ para $x>0$ y $-1$ para $x<0$.
::::

⁠**En resumen:** La derivada $f'(x)$ es el límite de las pendientes de las secantes, es decir, la pendiente de la recta tangente; en un punto anguloso no existe.

### La aproximación lineal

<span class="anker" id="stufe-1-3"></span>

¿Para qué se necesita la recta tangente? Si se observa una gráfica suave con una lupa cada vez más potente, se ve en ella cada vez menos curvatura. Con un aumento fuerte, de la curva solo queda un trozo recto, y ese trozo está sobre la recta tangente (fig. [2](#abb-2)). Por eso, cerca del punto $x$ se puede sustituir la función por su recta tangente. Con una recta se calcula mucho más fácilmente que con la propia función.

:::abbildung ml/k3lupe 2
La lupa: la gráfica de $f(x)=x^3$ (azul) y su recta tangente $8+12\,(x-2)$ en el punto $2$ (en rojo, discontinua) en tres ventanas, cada una diez veces más estrecha que la anterior. En la última ventana, la curva y la recta tangente ya no se distinguen.
:::

:::satz Teorema 1.3 (Aproximación lineal)
<span class="anker" id="satz-1-3"></span>

Si $f$ es derivable en el punto $x$, se cumple

<span class="anker" id="gl-1-4"></span>
$$f(x+h)=f(x)+f'(x)\,h+r(h)\qquad\text{con}\qquad \lim_{h\to0}\frac{r(h)}{h}=0 . \tag{1.4}$$

La expresión $f(x)+f'(x)\,h$ se llama la __aproximación lineal__ de $f$ en el punto $x$, y $r(h)$ es su error.
:::

:::beweis Aproximación lineal
Se define $r(h)=f(x+h)-f(x)-f'(x)\,h$; entonces la ecuación de la izquierda se cumple por construcción. Para $h\ne0$ es

$$\frac{r(h)}{h}=\frac{f(x+h)-f(x)}{h}-f'(x),$$

y, según [(1.3)](#gl-1-3), el primer sumando tiende a $f'(x)$, y la diferencia, por tanto, a $0$.
:::

La condición $r(h)/h\to0$ dice más que el simple hecho de que el error se haga pequeño. También $h$ mismo se hace pequeño; lo decisivo es que el error desaparece más rápido que $h$. Si se reduce $h$ a la mitad, la variación $f'(x)\,h$ se reduce a la mitad, pero el error se reduce bastante más que a la mitad. Ese es el significado preciso de la lupa.

La ecuación [(1.4)](#gl-1-4) proporciona también la interpretación más intuitiva de la derivada. Una pequeña variación $h$ de la entrada llega a la salida aproximadamente como $f'(x)\,h$. La derivada es, pues, el *factor* con el que la función transmite las pequeñas variaciones: su sensibilidad en el punto $x$. Un $|f'(x)|$ grande significa que ya pequeñas variaciones de la entrada cambian mucho el valor; un $f'(x)$ negativo significa que el valor disminuye cuando la entrada crece.

::::beispiel [Ejemplo numérico]
Para $f(x)=x^3$ en el punto $2$ y $h=0{,}01$, la aproximación lineal da

$$f(2{,}01)\approx8+12\cdot0{,}01=8{,}12 .$$

El valor exacto es $f(2{,}01)=2{,}01^3=8{,}120601$. El error es $r(0{,}01)=0{,}000601$; según el cálculo de [(1.2)](#gl-1-2), en general es $r(h)=6h^2+h^3$. El cociente $r(h)/h=6h+h^2$ vale $0{,}0601$ para $h=0{,}01$ y $0{,}006001$ para $h=0{,}001$: tiende a cero, como exige el teorema.
::::

⁠**En resumen:** Cerca de $x$, $f(x+h)\approx f(x)+f'(x)\,h$; la derivada es el factor con el que se transmiten las pequeñas variaciones, y el error desaparece más rápido que $h$.

:::hintergrund Por qué precisamente la recta tangente es la mejor recta
Toda recta que pasa por el punto $(x,\,f(x))$ proporciona una aproximación $f(x+h)\approx f(x)+m\,h$ con alguna pendiente $m$. Su error es $f(x+h)-f(x)-m\,h$. Si se divide entre $h$, se obtiene el cociente incremental menos $m$, y eso tiende, para $h\to0$, a $f'(x)-m$. Solo para $m=f'(x)$ este límite es cero. Para cualquier otra pendiente, el error sigue siendo a la larga del tamaño aproximado de $|f'(x)-m|\cdot|h|$, es decir, solo se reduce tan rápido como el propio $h$. La recta tangente es, por tanto, la única recta que pasa por el punto y cuyo error desaparece más rápido que $h$. En este sentido es la mejor aproximación lineal, y precisamente así puede definirse también la derivada: como el único número $m$ para el que $f(x+h)-f(x)-m\,h$ tiende a cero más rápido que $h$. Esta forma de la definición tiene la ventaja de que se traslada sin cambios a funciones con muchas entradas, donde ya no hay cociente, porque no se puede dividir entre un vector. La sección [3](partielle-ableitungen-und-der-gradient.html#stufe-3) hace uso de ello.
:::

### Reglas de derivación

<span class="anker" id="stufe-1-4"></span>

Calcular cada derivada mediante el límite es laborioso. Por suerte, bastan unas pocas derivadas elementales y cuatro reglas para derivar casi cualquier fórmula compuesta de operaciones aritméticas básicas y funciones conocidas. La tabla [1](#tab-1) reúne las derivadas elementales que utiliza este capítulo.

<span class="anker" id="tab-1"></span>

**Tabla 1:** Derivadas elementales. La regla de la potencia vale para todo exponente real $n$; para $n$ no entero, solo si $x>0$. Los ángulos en $\sin$ y $\cos$ se miden en radianes.

| Función $f(x)$ | Derivada $f'(x)$ | Ejemplo |
|---|---|---|
| $c$ (constante) | $0$ | $f(x)=7$: $f'(x)=0$ |
| $x^n$ | $n\,x^{n-1}$ | $x^3\mapsto3x^2$, $\ \tfrac1x=x^{-1}\mapsto-\tfrac1{x^2}$, $\ \sqrt x=x^{1/2}\mapsto\tfrac1{2\sqrt x}$ |
| $\mathrm{e}^x$ | $\mathrm{e}^x$ | en el punto $0$: pendiente $1$ |
| $\ln x$ ($x>0$) | $\tfrac1x$ | en el punto $1$: pendiente $1$ |
| $\sin x$ | $\cos x$ | en el punto $0$: pendiente $1$ |
| $\cos x$ | $-\sin x$ | en el punto $0$: pendiente $0$ |

:::satz Teorema 1.4 (Reglas de derivación)
<span class="anker" id="satz-1-4"></span>

Si $u$ y $v$ son derivables en el punto $x$ y $c$ es un número, en ese punto se cumple:

<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} (u+v)'&=u'+v' &&\text{(regla de la suma)}\\ (c\,u)'&=c\,u' &&\text{(regla del factor constante)}\\ (u\,v)'&=u'\,v+u\,v' &&\text{(regla del producto)}\\ \Bigl(\frac uv\Bigr)'&=\frac{u'\,v-u\,v'}{v^2}\quad\text{si }v(x)\ne0 &&\text{(regla del cociente)} \end{aligned} \tag{1.5}$$
:::

Las dos primeras reglas se siguen inmediatamente de la definición, porque los cocientes incrementales de sumas y de múltiplos se descomponen del mismo modo. La regla del producto es menos evidente. Una imagen la aclara: imagínese $u\,v$ como el área de un rectángulo de lados $u$ y $v$. Si los lados crecen en $\Delta u$ y $\Delta v$, se añaden tres franjas: $u\,\Delta v$, $v\,\Delta u$ y la pequeña pieza de la esquina $\Delta u\,\Delta v$. Con variaciones pequeñas, la pieza de la esquina es un producto de dos magnitudes pequeñas y desaparece más rápido que las dos franjas. Queda $\Delta(uv)\approx v\,\Delta u+u\,\Delta v$, y al dividir entre $h$ se obtiene la regla del producto.

:::beweis Regla del producto y regla de la potencia
Con $\Delta u=u(x+h)-u(x)$ y $\Delta v=v(x+h)-v(x)$ se tiene exactamente

$$u(x+h)\,v(x+h)-u(x)\,v(x)=v(x)\,\Delta u+u(x)\,\Delta v+\Delta u\,\Delta v .$$

Al dividir entre $h$, $\Delta u/h$ tiende a $u'(x)$ y $\Delta v/h$ tiende a $v'(x)$. El último sumando es $(\Delta u/h)\cdot\Delta v$; su primer factor tiende a $u'(x)$, y el segundo, a $0$, pues una función derivable cambia poco cuando $h$ es pequeño. Así pues, el cociente entero tiende a $u'(x)\,v(x)+u(x)\,v'(x)$.

Para la regla de la potencia con un número natural $n$ se desarrolla $(x+h)^n$. Según el teorema del binomio,

$$(x+h)^n=x^n+n\,x^{n-1}h+(\text{términos con }h^2,h^3,\dots,h^n),$$

por lo que el cociente incremental es $n\,x^{n-1}$ más términos que aún contienen al menos un $h$. Para $h\to0$ queda $n\,x^{n-1}$. La regla del cociente se sigue de la regla del producto, aplicada a $u=(u/v)\cdot v$.
:::

::::beispiel [Ejemplo numérico]
Sea $f(x)=(x^2+1)(x-3)$; se busca $f'(2)$. Con $u=x^2+1$, $u'=2x$, $v=x-3$, $v'=1$, la regla del producto da

$$f'(x)=2x\,(x-3)+(x^2+1)\cdot1,\qquad f'(2)=4\cdot(-1)+5\cdot1=1 .$$

Comprobación: desarrollando el producto, $f(x)=x^3-3x^2+x-3$, luego $f'(x)=3x^2-6x+1$ y $f'(2)=12-12+1=1$.
::::

⁠**En resumen:** Con las derivadas elementales de la tabla y las reglas para la suma, el múltiplo, el producto y el cociente se derivan fórmulas compuestas sin calcular ningún límite.

:::hintergrund Por qué la función exponencial es su propia derivada
Para toda base $a>0$ se cumple $a^{x+h}-a^x=a^x\,(a^h-1)$. Por eso, el cociente incremental de $a^x$ es $a^x$ por el cociente incremental de $a^x$ en el punto $0$, es decir, $a^x\cdot\frac{a^h-1}{h}$: la pendiente en cada punto es el valor de la función por la pendiente en el punto $0$. Para $a=2$, esta pendiente en el punto $0$ es aproximadamente $0{,}693$; para $a=3$, aproximadamente $1{,}099$. Entre ambas hay exactamente una base para la que vale $1$, y esa base es el número de Euler $\mathrm{e}\approx2{,}718$. Para ella, la pendiente es en todas partes igual al valor de la función. La derivada de $\ln x$ se sigue de ello, pues el logaritmo deshace la función exponencial: si $y=\ln x$, entonces $x=\mathrm{e}^y$, y una pequeña variación de $y$ cambia $x$ en $\mathrm{e}^y=x$ veces esa variación. A la inversa, una pequeña variación de $x$ cambia, por tanto, $y$ en $1/x$ veces esa variación.
:::

### La segunda derivada y la aproximación cuadrática

<span class="anker" id="stufe-1-5"></span>

La recta tangente da la dirección de la gráfica, pero no cómo se curva alejándose de ella. Si la curva se desvía de la recta tangente hacia arriba o hacia abajo, y cuánto, depende de cómo cambia la propia pendiente. Este cambio se mide de nuevo con una derivada, a saber, con la derivada de la derivada.

:::definition Definición 1.5 (Derivadas de orden superior)
<span class="anker" id="satz-1-5"></span>

Si la función derivada $f'$ es derivable en el punto $x$, $f''(x)=(f')'(x)$ se llama la __segunda derivada__ de $f$ en el punto $x$. Análogamente, $f'''=(f'')'$ es la tercera derivada y, en general, se escribe $f^{(k)}$ para la $k$-ésima derivada.
:::

Si $f''(x)>0$, la pendiente crece en $x$; la gráfica se curva hacia arriba alejándose de la recta tangente y, cerca de $x$, queda por encima de ella. Si $f''(x)<0$, se curva hacia abajo. La segunda derivada mide, pues, la __curvatura__ de la gráfica; más exactamente, lo rápido que cambia su pendiente.

Con la segunda derivada, la aproximación se vuelve más precisa. Se sustituye la recta tangente por la parábola que en el punto $x$ tiene el mismo valor, la misma pendiente y la misma segunda derivada que $f$. Una parábola $p(h)=a+b\,h+c\,h^2$ tiene $p(0)=a$, $p'(0)=b$ y $p''(0)=2c$. Para que estos tres números coincidan con $f(x)$, $f'(x)$ y $f''(x)$, debe ser $a=f(x)$, $b=f'(x)$ y $c=\tfrac12f''(x)$. De ahí viene el factor $\tfrac12$.

:::satz Teorema 1.6 (Aproximación cuadrática)
<span class="anker" id="satz-1-6"></span>

Si $f$ es dos veces derivable cerca de $x$ y $f''$ es continua en el punto $x$, se cumple

<span class="anker" id="gl-1-6"></span>
$$f(x+h)=f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2+r_2(h)\qquad\text{con}\qquad\lim_{h\to0}\frac{r_2(h)}{h^2}=0 . \tag{1.6}$$
:::

Continua significa aquí que $f''$ cambia poco ante pequeñas variaciones del punto, sin saltos. La demostración se hace de forma parecida a la de la aproximación lineal, con un paso más; el enunciado se llama teorema de Taylor. El error $r_2(h)$ desaparece ahora más rápido que $h^2$, es decir, con $h$ pequeño, mucho más rápido aún que el error de la aproximación lineal.

::::beispiel [Ejemplo numérico]
Para $f(x)=x^3$ se tiene $f'(x)=3x^2$, $f''(x)=6x$ y $f'''(x)=6$. En el punto $2$, $f''(2)=12>0$: la gráfica se curva hacia arriba alejándose de la recta tangente, como muestra el panel izquierdo de la fig. [2](#abb-2). La aproximación cuadrática para $h=0{,}01$ es

$$f(2{,}01)\approx8+12\cdot0{,}01+\tfrac12\cdot12\cdot0{,}01^2=8+0{,}12+0{,}0006=8{,}1206 .$$

El valor exacto es $8{,}120601$; el error es ya solo $0{,}000001=h^3$. La fig. [3](#abb-3) muestra la suma de los tres términos.

:::abbildung ml/k3rtaylor1 3
La aproximación cuadrática de $f(x)=x^3$ en el punto $2$ para $h=0{,}01$ como suma del valor, el término de pendiente y el término de curvatura.
:::
::::

⁠**En resumen:** La segunda derivada mide lo rápido que cambia la pendiente, es decir, la curvatura; con ella, la aproximación pasa a ser $f(x+h)\approx f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2$.

:::hintergrund Polinomios de Taylor de orden superior
Se puede ir más allá y ajustar también la tercera derivada y todas las siguientes. El polinomio

$$f(x)+f'(x)\,h+\frac{f''(x)}{2}\,h^2+\frac{f'''(x)}{6}\,h^3+\dots+\frac{f^{(k)}(x)}{k!}\,h^k$$

se llama polinomio de Taylor de orden $k$; aquí $k!=1\cdot2\cdots k$. Los denominadores $k!$ provienen, como el factor $\tfrac12$, de que la $k$-ésima derivada de $h^k$ es igual a $k!$. Para $f(x)=x^3$, ya el polinomio de Taylor de orden tres es exacto: $8+12h+6h^2+h^3$ es exactamente $(2+h)^3$. Para la mayoría de las funciones, la aproximación mejora con cada orden, siempre que $h$ sea lo bastante pequeño. Para este capítulo bastan los órdenes uno y dos.
:::

:::aufgabe Ejercicio 1 ★ Secantes y recta tangente
<span class="anker" id="aufg-1"></span>

Sea $f(x)=x^2$.

<ol class="al">

<li>

Calcula el cociente incremental en el punto $3$ para $h=1$, $h=0{,}1$ y $h=-0{,}1$.

</li>

<li>

Demuestra que el cociente incremental en el punto $3$ es igual a $6+h$ y determina $f'(3)$.

</li>

<li>

Da la recta tangente en el punto $3$ y calcula con ella una aproximación de $3{,}02^2$. ¿Cuál es el error?

</li>

</ol>

:::loesung
(a) Con $f(3)=9$ se tiene

$$\frac{4^2-9}{1}=7,\qquad \frac{3{,}1^2-9}{0{,}1}=\frac{9{,}61-9}{0{,}1}=6{,}1,\qquad \frac{2{,}9^2-9}{-0{,}1}=\frac{8{,}41-9}{-0{,}1}=5{,}9 .$$

La secante hacia la derecha es más empinada que la recta tangente, y la secante hacia la izquierda, más plana, porque la gráfica de la parábola se curva hacia arriba.

(b) $(3+h)^2=9+6h+h^2$, así que el cociente incremental es $\frac{6h+h^2}{h}=6+h$. Para $h\to0$ tiende a $6$ por ambos lados; se tiene $f'(3)=6$, de acuerdo con la regla $(x^2)'=2x$.

(c) La recta tangente es $t(x)=9+6\,(x-3)$. Con ella se obtiene $3{,}02^2\approx9+6\cdot0{,}02=9{,}12$. El valor exacto es $3{,}02^2=9{,}1204$. El error $0{,}0004=0{,}02^2$ es exactamente $h^2$, pues $f(3+h)-9-6h=h^2$. Se anula más rápido que $h$, como promete la aproximación lineal.
:::
:::

:::aufgabe Ejercicio 2 ★ Derivar con las reglas
<span class="anker" id="aufg-2"></span>

Deriva y evalúa en el punto indicado.

<ol class="al">

<li>

$f(x)=4x^3-2x+7$ en el punto $1$;

</li>

<li>

$f(x)=x^2\,\mathrm{e}^x$ en los puntos $0$ y $1$;

</li>

<li>

$f(x)=\dfrac{x}{1+x^2}$ en los puntos $0$ y $1$. ¿Qué significa el resultado en el punto $1$ para la gráfica?

</li>

</ol>

:::loesung
(a) Regla de la suma y regla del factor constante, con la regla de la potencia: $f'(x)=12x^2-2$, así que $f'(1)=10$.

(b) Regla del producto con $u=x^2$, $v=\mathrm{e}^x$: $f'(x)=2x\,\mathrm{e}^x+x^2\,\mathrm{e}^x=(2x+x^2)\,\mathrm{e}^x$. Por tanto, $f'(0)=0$ y $f'(1)=3\mathrm{e}\approx8{,}155$.

(c) Regla del cociente con $u=x$, $u'=1$, $v=1+x^2$, $v'=2x$:

$$f'(x)=\frac{1\cdot(1+x^2)-x\cdot2x}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2},\qquad f'(0)=1,\qquad f'(1)=0 .$$

En el punto $1$, la gráfica tiene una recta tangente horizontal. Allí está su punto más alto: para todo $x$ se tiene $\frac{x}{1+x^2}\le\frac12$, porque $1+x^2-2x=(x-1)^2\ge0$, y $f(1)=\tfrac12$.
:::
:::

:::aufgabe Ejercicio 3 ★★ Raíces con la lupa
<span class="anker" id="aufg-3"></span>

Sea $f(x)=\sqrt x$.

<ol class="al">

<li>

Calcula $f'(x)$ y $f''(x)$ con la regla de la potencia.

</li>

<li>

Calcula, con la aproximación lineal y con la cuadrática en el punto $4$, un valor aproximado de $\sqrt{4{,}1}$. Compara ambos con la calculadora.

</li>

<li>

¿Está la recta tangente por encima o por debajo de la gráfica? Justifícalo con el signo de $f''(4)$.

</li>

</ol>

:::loesung
(a) Con $\sqrt x=x^{1/2}$ se tiene $f'(x)=\tfrac12x^{-1/2}=\frac1{2\sqrt x}$ y $f''(x)=-\tfrac14x^{-3/2}$.

(b) En el punto $4$ se tiene $f(4)=2$, $f'(4)=\tfrac14$ y $f''(4)=-\tfrac14\cdot\tfrac18=-\tfrac1{32}$. Con $h=0{,}1$:

$$\text{lineal: }2+\tfrac14\cdot0{,}1=2{,}025,\qquad \text{cuadrática: }2{,}025-\tfrac12\cdot\tfrac1{32}\cdot0{,}01=2{,}025-0{,}00015625=2{,}02484375 .$$

La calculadora da $\sqrt{4{,}1}\approx2{,}0248457$. El error de la aproximación lineal es de unos $1{,}5\cdot10^{-4}$; el de la cuadrática, solo de unos $1{,}9\cdot10^{-6}$.

(c) Como $f''(4)<0$, la gráfica se curva hacia abajo, alejándose de la recta tangente; la recta tangente está por encima de la gráfica. Por eso, la aproximación lineal $2{,}025$ es demasiado grande.
:::
:::

:::aufgabe Ejercicio 4 ★★ ¿Punto anguloso o no?
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Demuestra con el cociente incremental que $g(x)=x\,|x|$ es derivable en el punto $0$ y determina $g'(0)$.

</li>

<li>

Determina $g'(x)$ para $x>0$ y para $x<0$. ¿Tiene $g'$, a su vez, derivada en el punto $0$?

</li>

<li>

La función $m(x)=\max(x,\,0)$ devuelve $x$ si $x$ es positivo, y $0$ en caso contrario. ¿Dónde es derivable y qué valores tienen allí sus derivadas?

</li>

</ol>

:::loesung
(a) Se tiene $g(0)=0$ y $\frac{g(h)-g(0)}{h}=\frac{h\,|h|}{h}=|h|$. Esto tiende a $0$ por ambos lados, así que $g'(0)=0$. El valor absoluto por sí solo tiene un punto anguloso, pero el factor $x$ aplana las dos ramas en el origen.

(b) Para $x>0$ se tiene $g(x)=x^2$ y $g'(x)=2x$; para $x<0$, $g(x)=-x^2$ y $g'(x)=-2x$. Junto con (a), $g'(x)=2|x|$ para todo $x$. Esta función tiene un punto anguloso en $0$; su cociente incremental $2|h|/h$ vale $\pm2$. Por tanto, $g$ es derivable una vez, pero no dos veces.

(c) Para $x>0$ se tiene $m(x)=x$, con $m'(x)=1$; para $x<0$, $m(x)=0$, con $m'(x)=0$. En el punto $0$, el cociente incremental es $1$ para $h>0$ y $0$ para $h<0$; allí no existe la derivada. La gráfica tiene un punto anguloso en $0$.
:::
:::
