---
title: Ángulos y semejanza
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15210600
summary: Dos vectores pueden apuntar en direcciones parecidas aunque tengan longitudes distintas.
tags: ángulo, ortogonales, similitud coseno
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Dos vectores pueden apuntar en direcciones parecidas aunque tengan longitudes distintas. Esta sección mide el ángulo entre ellos. La base es una desigualdad que, además, dice exactamente cuándo una comparación con un patrón da su respuesta más fuerte.
:::

### La desigualdad de Cauchy-Schwarz

<span class="anker" id="stufe-5-1"></span>

¿Hasta dónde puede crecer el producto escalar de dos vectores si sus longitudes están fijadas? Un intento: $\mathbf{u}=(1,\,2,\,2)^{\top}$ tiene la longitud $3$; $\mathbf{v}=(2,\,0,\,1)^{\top}$, la longitud $\sqrt5\approx2{,}24$. Su producto escalar es $2+0+2=4$, claramente menos que el producto de las longitudes, $3\cdot2{,}24\approx6{,}71$. Si en su lugar se toma $\mathbf{v}=2\mathbf{u}$, un vector en la misma dirección con la longitud $6$, entonces $\mathbf{u}^{\top}(2\mathbf{u})=2\cdot9=18=3\cdot6$: exactamente el producto de las longitudes. Más no es posible.

:::satz Teorema 5.1 (Desigualdad de Cauchy-Schwarz)
<span class="anker" id="satz-5-1"></span>

Para todos los $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ se cumple

<span class="anker" id="gl-5-1"></span>
$$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert . \tag{5.1}$$

La igualdad se cumple si y solo si uno de los dos vectores es un múltiplo del otro.
:::

:::beweis Desigualdad de Cauchy-Schwarz
Si $\mathbf{v}=\mathbf{0}$, ambos lados son cero. Si no, se considera, para un número $t$ cualquiera, el vector $\mathbf{u}-t\,\mathbf{v}$. El cuadrado de su longitud nunca es negativo, y según las reglas de cálculo del producto escalar se tiene

$$0\le\lVert\mathbf{u}-t\,\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2t\,\mathbf{u}^{\top}\mathbf{v}+t^2\lVert\mathbf{v}\rVert^2 .$$

Esto vale para todo $t$, y por tanto también para $t=\mathbf{u}^{\top}\mathbf{v}/\lVert\mathbf{v}\rVert^2$, el punto en el que el lado derecho, como parábola en $t$, es mínimo. Sustituyendo:

$$0\le\lVert\mathbf{u}\rVert^2-2\,\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}+\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}=\lVert\mathbf{u}\rVert^2-\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}.$$

Multiplicado por $\lVert\mathbf{v}\rVert^2>0$, esto significa $(\mathbf{u}^{\top}\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$; su raíz es [(5.1)](#gl-5-1).

La igualdad se cumple si y solo si $\lVert\mathbf{u}-t\,\mathbf{v}\rVert=0$ para este $t$, es decir, si $\mathbf{u}=t\,\mathbf{v}$. A la inversa, para $\mathbf{u}=c\,\mathbf{v}$ se tiene efectivamente $|\mathbf{u}^{\top}\mathbf{v}|=|c|\,\lVert\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.
:::

::::beispiel [Ejemplo numérico]
Para $\mathbf{u}=(1,\,2,\,2)^{\top}$ y $\mathbf{v}=(2,\,0,\,1)^{\top}$ se tiene $|\mathbf{u}^{\top}\mathbf{v}|=4\le3\cdot\sqrt5\approx6{,}71$. La desigualdad es estricta porque $\mathbf{v}$ no es un múltiplo de $\mathbf{u}$.
::::

Con la desigualdad puede completarse lo que en la subsección [3.4](normen-die-groe-eines-vektors.html#stufe-3-4) solo se había justificado de forma intuitiva: la desigualdad triangular de la norma euclídea. Se tiene

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2\le\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2=\bigl(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert\bigr)^2 ,$$

y su raíz es (N3).

⁠**En resumen:** El producto escalar es, en valor absoluto, como mucho el producto de las longitudes, y es igual a él si y solo si los vectores están en una recta que pasa por el origen.

:::hintergrund Por qué el producto escalar reconoce patrones: el enunciado preciso
En la subsección [2.4](das-skalarprodukt.html#stufe-2-4), la comparación con un patrón era una idea intuitiva: el producto escalar $\mathbf{w}^{\top}\mathbf{x}$ es grande si la señal sigue al patrón. La desigualdad de Cauchy-Schwarz lo convierte en un enunciado preciso. Si solo se comparan señales con la misma longitud $\lVert\mathbf{x}\rVert$, $\mathbf{w}^{\top}\mathbf{x}$ está siempre entre $-\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ y $+\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$. El valor máximo lo alcanza exactamente la señal que es un múltiplo positivo del patrón; el mínimo, el múltiplo negativo. Entre todas las señales de la misma energía, la comparación responde, por tanto, con más fuerza al propio patrón.

⁠**Ejemplo numérico:** El patrón alternante $\mathbf{w}=(1,-1,1,-1)^{\top}$ tiene la longitud $2$. Entre todas las señales de longitud $2$, $\mathbf{x}=\mathbf{w}$ da el valor máximo $4=2\cdot2$; la señal $(2,0,0,0)^{\top}$, solo $2$; y $\mathbf{x}=-\mathbf{w}$, el valor mínimo $-4$.

En telecomunicaciones, esta es la base del receptor de correlación y del filtro adaptado (*matched filter*). Un filtro así tiene como respuesta al impulso la señal transmitida invertida en el tiempo; por ello, en el instante de muestreo calcula exactamente el producto escalar de la señal recibida y la señal transmitida. Que este filtro maximiza la relación señal-ruido se demuestra precisamente con esta desigualdad.
:::

### El ángulo entre dos vectores

<span class="anker" id="stufe-5-2"></span>

Dos flechas que parten del origen forman un ángulo. Este dice lo parecidas que son sus direcciones, independientemente de su longitud. En el plano puede medirse con el transportador. Para vectores con muchas componentes se necesita una fórmula, y la proporciona el producto escalar.

:::herleitung El producto escalar en el plano
Las flechas $\mathbf{u}$ y $\mathbf{v}$ y su flecha de unión $\mathbf{u}-\mathbf{v}$ forman un triángulo. Si $\varphi$ es el ángulo entre $\mathbf{u}$ y $\mathbf{v}$, el teorema del coseno de la geometría escolar dice

$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

Según [(4.1)](abstande-und-einheiten.html#gl-4-1), el mismo lado izquierdo es igual a $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}$. Si se comparan ambas líneas, queda

$$\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

En el plano y en el espacio, el producto escalar es, por tanto, el producto de las longitudes por el coseno del ángulo que forman.
:::

En dimensiones superiores no hay transportador. Por eso se invierte la deducción y se usa la fórmula como definición.

:::definition Definición 5.2 (Ángulo)
<span class="anker" id="satz-5-2"></span>

Para $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$, ambos distintos de $\mathbf{0}$, el __ángulo__ $\varphi$ entre $\mathbf{u}$ y $\mathbf{v}$ es el número $\varphi\in[0^\circ,180^\circ]$ con

<span class="anker" id="gl-5-2"></span>
$$\cos\varphi=\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert} . \tag{5.2}$$
:::

Esta definición solo es posible porque, según la desigualdad de Cauchy-Schwarz, el lado derecho está siempre entre $-1$ y $1$. Para cada uno de estos números hay exactamente un ángulo entre $0^\circ$ y $180^\circ$. En el signo del producto escalar se ve si el ángulo es agudo ($\mathbf{u}^{\top}\mathbf{v}>0$), recto ($\mathbf{u}^{\top}\mathbf{v}=0$) u obtuso ($\mathbf{u}^{\top}\mathbf{v}<0$).

::::beispiel [Ejemplo numérico]
Para $(1,\,0)^{\top}$ y $(1,\,1)^{\top}$ se tiene $\cos\varphi=1/\sqrt2$, es decir, $\varphi=45^\circ$. Para $(1,\,0,\,1)^{\top}$ y $(1,\,1,\,0)^{\top}$ se tiene $\cos\varphi=\tfrac12$, es decir, $\varphi=60^\circ$ (fig. [22](#abb-22)). Para $\mathbf{u}=(1,\,2,\,2)^{\top}$ y $\mathbf{v}=(2,\,0,\,1)^{\top}$ se tiene $\cos\varphi=4/(3\sqrt5)\approx0{,}596$, es decir, $\varphi\approx53{,}4^\circ$.

:::abbildung ml/k1rwinkel 22
El ángulo entre $(1,\,0,\,1)^{\top}$ y $(1,\,1,\,0)^{\top}$: en el numerador, el producto escalar; en el denominador, las dos longitudes.
:::
::::

⁠**En resumen:** El coseno del ángulo entre dos vectores es su producto escalar dividido por el producto de sus longitudes.

### Vectores ortogonales

<span class="anker" id="stufe-5-3"></span>

Si el producto escalar de dos vectores es cero, ninguno aporta nada en la dirección del otro. En el plano, las flechas son entonces perpendiculares. Este caso es tan importante que tiene un nombre propio.

:::definition Definición 5.3 (Ortogonal)
<span class="anker" id="satz-5-3"></span>

Dos vectores $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ se llaman __ortogonales__ si $\mathbf{u}^{\top}\mathbf{v}=0$.
:::

Si ambos vectores son distintos de $\mathbf{0}$, su ángulo es, según [(5.2)](#gl-5-2), exactamente $90^\circ$. El vector nulo es ortogonal a todo vector.

:::satz Teorema 5.4 (Teorema de Pitágoras)
<span class="anker" id="satz-5-4"></span>

Si $\mathbf{u}$ y $\mathbf{v}$ son ortogonales, entonces $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$.
:::

Esto se deduce inmediatamente de $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$, pues el sumando central es cero.

::::beispiel [Ejemplo numérico 1]
$(1,\,2,\,2)^{\top}$ y $(2,\,0,\,-1)^{\top}$ son ortogonales, pues $2+0-2=0$. Su suma $(3,\,2,\,1)^{\top}$ tiene el cuadrado de la longitud $14=9+5$.
::::

::::beispiel [Ejemplo numérico 2] dos patrones que no se estorban
El patrón constante $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ y el patrón alternante $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ de la subsección [2.4](das-skalarprodukt.html#stufe-2-4) son ortogonales, $\mathbf 1^{\top}\mathbf{w}=0$. Una señal que consta de $2$ veces el patrón constante y $1$ vez el patrón alternante es $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}=(3,\,1,\,3,\,1)^{\top}$. La comparación con el patrón constante da $\mathbf 1^{\top}\mathbf{x}=8=2\cdot4$; la comparación con el patrón alternante, $\mathbf{w}^{\top}\mathbf{x}=4=1\cdot4$ (fig. [23](#abb-23)). Cada comparación encuentra exactamente su propia parte, multiplicada por $\lVert\mathbf 1\rVert^2=\lVert\mathbf{w}\rVert^2=4$; la otra parte no la estorba.

:::abbildung ml/k1rortho 23
Los dos patrones son ortogonales (arriba). La comparación de la señal $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}$ con cada patrón da su parte multiplicada por $4$.
:::
::::

⁠**En resumen:** Ortogonal significa producto escalar cero; las flechas ortogonales son perpendiculares, y para ellas se cumple el teorema de Pitágoras.

:::hintergrund Por qué los patrones ortogonales no se estorban, y qué tiene que ver con los coeficientes de Fourier
Si una señal es una combinación lineal $\mathbf{x}=\alpha\,\mathbf 1+\beta\,\mathbf{w}$ de dos patrones ortogonales, según las reglas de cálculo se tiene

$$\mathbf 1^{\top}\mathbf{x}=\alpha\,\mathbf 1^{\top}\mathbf 1+\beta\,\mathbf 1^{\top}\mathbf{w}=\alpha\,\lVert\mathbf 1\rVert^2+0 ,\qquad\text{por tanto}\qquad \alpha=\frac{\mathbf 1^{\top}\mathbf{x}}{\lVert\mathbf 1\rVert^2} .$$

La comparación con un patrón mide, por tanto, solo su propia parte, porque la contribución del otro patrón desaparece con el factor $\mathbf 1^{\top}\mathbf{w}=0$. Si los patrones no fueran ortogonales, cada comparación contaría también un trozo de la otra parte.

Exactamente así están construidos los coeficientes de una serie de Fourier. Para una señal $s(t)$ con el periodo $T$ y $\omega_0=2\pi/T$ se tiene

$$a_k=\frac{2}{T}\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t=\frac{\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t}{\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t}\qquad(k\ge1),$$

pues $\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t=T/2$. La integral de un producto de dos funciones desempeña el papel del producto escalar, y las funciones coseno y seno de frecuencias distintas son ortogonales en este sentido: la integral de su producto a lo largo de un periodo es cero. Por eso cada coeficiente de Fourier puede calcularse por separado, sin conocer los demás.
:::

### La similitud coseno

<span class="anker" id="stufe-5-4"></span>

A veces la longitud de un vector es secundaria. Un texto puede describirse mediante un vector cuya componente $j$ cuenta cuántas veces aparece en el texto la palabra $j$ de una lista fija de palabras. Una crónica detallada de un partido de fútbol contiene las palabras «gol» y «balón» más veces que una breve noticia sobre el mismo partido, pero en la misma proporción. Los dos vectores tienen longitudes distintas, pero apuntan en la misma dirección. Para el contenido, lo que cuenta es la dirección.

:::definition Definición 5.5 (Similitud coseno)
<span class="anker" id="satz-5-5"></span>

La __similitud coseno__ de dos vectores $\mathbf{u},\mathbf{v}\ne\mathbf{0}$ es el número

<span class="anker" id="gl-5-3"></span>
$$\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}\in[-1,\,1] , \tag{5.3}$$

es decir, el coseno de su ángulo.
:::

Vale $1$ si los vectores apuntan en la misma dirección, $0$ si son ortogonales y $-1$ si apuntan en sentidos opuestos. Si se multiplica uno de los vectores por un número positivo, la similitud no cambia, pues el número se simplifica.

::::beispiel [Ejemplo numérico]
Tres textos y sus recuentos de las palabras «gol», «balón» y «elección»:

$$\mathbf{x}_1=(3,\,2,\,0)^{\top},\qquad \mathbf{x}_2=(6,\,4,\,0)^{\top},\qquad \mathbf{x}_3=(0,\,1,\,3)^{\top} .$$

El texto 2 es una crónica el doble de larga sobre el mismo partido; el texto 3 trata sobre todo de una elección. La similitud coseno de los textos 1 y 2 es $1$; la de los textos 1 y 3 es $2/\sqrt{130}\approx0{,}175$ (fig. [24](#abb-24)). Del mismo modo, la de los textos 2 y 3 es igual a $4/(\sqrt{52}\,\sqrt{10})=4/\sqrt{520}\approx0{,}175$.

:::abbildung ml/k1rkosinus 24
Dos similitudes coseno de los recuentos de palabras: en cada caso, un producto escalar en el numerador y dos longitudes en el denominador.
:::

Las distancias, en cambio, son $\lVert\mathbf{x}_1-\mathbf{x}_2\rVert=\sqrt{13}\approx3{,}61$, $\lVert\mathbf{x}_1-\mathbf{x}_3\rVert=\sqrt{19}\approx4{,}36$ y $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=\sqrt{54}\approx7{,}35$. Según la distancia, el texto 1 apenas está más lejos del texto 3 que del texto 2, aunque el texto 2 trata exactamente del mismo tema. La similitud coseno lo reconoce de inmediato: vale $1$, y el ángulo con el texto 3, de unos $79{,}9^\circ$, es casi recto.
::::

⁠**En resumen:** La similitud coseno compara solo las direcciones de dos vectores y pasa por alto sus longitudes.

:::hintergrund La similitud coseno no es lo mismo que la correlación
Si se centran antes dos vectores de la misma longitud (subsección [4.3](abstande-und-einheiten.html#stufe-4-3)), el coseno de su ángulo mide si las componentes de ambos quedan a la vez por encima o a la vez por debajo de sus respectivas medias. Este número se llama coeficiente de correlación. Sin centrar, a menudo sale algo completamente distinto. Ejemplo: $\mathbf{a}=(1,2,3)^{\top}$, $\mathbf{b}=(3,4,5)^{\top}$ y $\mathbf{c}=(3,2,1)^{\top}$. La similitud coseno de $\mathbf{a}$ y $\mathbf{b}$ es aproximadamente $0{,}983$; la de $\mathbf{a}$ y $\mathbf{c}$, nada menos que $0{,}714$; ambas, por tanto, claramente positivas. Centrados, $\tilde{\mathbf{a}}=(-1,0,1)^{\top}$, $\tilde{\mathbf{b}}=(-1,0,1)^{\top}$ y $\tilde{\mathbf{c}}=(1,0,-1)^{\top}$: el coeficiente de correlación de $\mathbf{a}$ y $\mathbf{b}$ es $1$, pero el de $\mathbf{a}$ y $\mathbf{c}$ es $-1$, pues $\mathbf{c}$ baja justo donde $\mathbf{a}$ sube. La similitud coseno sin centrar solo era positiva porque todos los números son positivos y, por eso, los tres vectores apuntan aproximadamente en la misma dirección.
:::

### El producto escalar como longitud de la sombra

<span class="anker" id="stufe-5-5"></span>

El producto escalar con un vector normalizado tiene un significado geométrico sencillo. Imagina una recta que pasa por el origen en la dirección del vector normalizado $\mathbf{u}$ y deja que la luz caiga perpendicularmente sobre esa recta. La flecha $\mathbf{x}$ proyecta entonces una sombra sobre la recta (fig. [25](#abb-25)). ¿Qué longitud tiene?

:::abbildung ml/k1schatten 25
La sombra de la flecha $\mathbf{x}=(3,1)^{\top}$ sobre la recta en la dirección del vector normalizado $\mathbf{u}=(0{,}6;\,0{,}8)^{\top}$. La luz cae perpendicularmente sobre la recta (a trazos). La sombra (azul claro) tiene la longitud $\mathbf{u}^{\top}\mathbf{x}=\lVert\mathbf{x}\rVert\cos\varphi=2{,}6$ y termina en el punto $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}=(1{,}56;\,2{,}08)^{\top}$.
:::

:::satz Teorema 5.6 (Longitud de la sombra)
<span class="anker" id="satz-5-6"></span>

Sea $\mathbf{u}\in\mathbb{R}^d$ normalizado, es decir, $\lVert\mathbf{u}\rVert=1$. Entonces $\mathbf{u}^{\top}\mathbf{x}$ es la longitud con signo de la sombra de $\mathbf{x}$ sobre la recta en la dirección $\mathbf{u}$: la sombra termina en el punto $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$, y la flecha de unión $\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ es ortogonal a $\mathbf{u}$.
:::

:::beweis Longitud de la sombra
Con $\mathbf{u}^{\top}\mathbf{u}=\lVert\mathbf{u}\rVert^2=1$ se tiene $\mathbf{u}^{\top}\bigl(\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}\bigr)=\mathbf{u}^{\top}\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}^{\top}\mathbf{u}=0$. La flecha de unión es, por tanto, perpendicular a la recta; esa es exactamente la dirección de la que viene la luz. El punto de la sombra $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ está a una distancia $|\mathbf{u}^{\top}\mathbf{x}|$ del origen, porque $\mathbf{u}$ tiene longitud $1$. Está en la dirección de $\mathbf{u}$ si $\mathbf{u}^{\top}\mathbf{x}>0$, y en la opuesta si $\mathbf{u}^{\top}\mathbf{x}<0$. En el triángulo rectángulo formado por $\mathbf{x}$, la sombra y la flecha de unión, $\mathbf{x}$ es la hipotenusa; por eso, la longitud de la sombra es también $\lVert\mathbf{x}\rVert\cos\varphi$.
:::

Si $\mathbf{u}$ no está normalizado, $\mathbf{u}^{\top}\mathbf{x}$ es la longitud de la sombra de $\mathbf{x}$ en la dirección $\mathbf{u}$, multiplicada por $\lVert\mathbf{u}\rVert$.

::::beispiel [Ejemplo numérico]
$\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ está normalizado, pues $0{,}36+0{,}64=1$. Para $\mathbf{x}=(3,\,1)^{\top}$, la longitud de la sombra es $\mathbf{u}^{\top}\mathbf{x}=2{,}6$ (fig. [26](#abb-26)), el punto de la sombra es $2{,}6\,\mathbf{u}=(1{,}56;\ 2{,}08)^{\top}$ y la flecha de unión es $\mathbf{x}-2{,}6\,\mathbf{u}=(1{,}44;\ -1{,}08)^{\top}$. Es ortogonal a $\mathbf{u}$: $0{,}6\cdot1{,}44-0{,}8\cdot1{,}08=0$. Con $\lVert\mathbf{x}\rVert=\sqrt{10}\approx3{,}162$ se tiene $\cos\varphi=2{,}6/3{,}162\approx0{,}822$, es decir, $\varphi\approx34{,}7^\circ$.

:::abbildung ml/k1rschatten 26
La longitud de la sombra de $\mathbf{x}$ en la dirección del vector normalizado $\mathbf{u}$ como producto escalar.
:::
::::

Para una suma ponderada, esto significa: si los pesos están normalizados, $\mathbf{w}^{\top}\mathbf{x}$ indica hasta dónde llega el ejemplo $\mathbf{x}$ en la dirección de $\mathbf{w}$. Todos los puntos que dan el mismo valor $\mathbf{w}^{\top}\mathbf{x}$ proyectan la misma sombra. En el plano están, por tanto, en una recta perpendicular a $\mathbf{w}$; en el espacio, en un plano perpendicular a $\mathbf{w}$.

⁠**En resumen:** Para un vector normalizado $\mathbf{u}$, $\mathbf{u}^{\top}\mathbf{x}$ es la longitud de la sombra que $\mathbf{x}$ proyecta sobre la recta en la dirección $\mathbf{u}$.

:::aufgabe Ejercicio 12 ★ Ángulos y ortogonalidad
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Calcula el ángulo entre $(2,\,1,\,2)^{\top}$ y $(1,\,0,\,1)^{\top}$ y comprueba la desigualdad de Cauchy-Schwarz.

</li>

<li>

¿Son ortogonales $(1,\,1,\,0)^{\top}$ y $(1,\,-1,\,3)^{\top}$?

</li>

<li>

Encuentra un vector $\mathbf{v}\ne\mathbf{0}$ que sea ortogonal a $\mathbf{u}=(1,\,2)^{\top}$ y comprueba el teorema de Pitágoras para $\mathbf{u}$ y $\mathbf{v}$.

</li>

</ol>

:::loesung
(a) El producto escalar es $2+0+2=4$, y las longitudes son $3$ y $\sqrt2$. Así que $\cos\varphi=4/(3\sqrt2)\approx0{,}943$ y $\varphi\approx19{,}5^\circ$. Cauchy-Schwarz: $4\le3\sqrt2\approx4{,}243$.

(b) $1\cdot1+1\cdot(-1)+0\cdot3=0$: sí, son ortogonales.

(c) Para $\mathbf{v}=(v_1,v_2)^{\top}$, la condición exige $v_1+2v_2=0$. Una solución es $\mathbf{v}=(2,\,-1)^{\top}$, y también lo es cualquier múltiplo suyo distinto de cero. Comprobación de Pitágoras: $\mathbf{u}+\mathbf{v}=(3,\,1)^{\top}$ tiene el cuadrado de la longitud $10$, y $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2=5+5=10$.
:::
:::

:::aufgabe Ejercicio 13 ★★ ¿Qué texto es parecido?
<span class="anker" id="aufg-13"></span>

Cuatro textos; de nuevo se han contado las palabras «gol», «balón» y «elección»: $\mathbf{x}_a=(2,\,0,\,1)^{\top}$, $\mathbf{x}_b=(0,\,3,\,0)^{\top}$, $\mathbf{x}_c=(4,\,0,\,2)^{\top}$ y $\mathbf{x}_d=(1,\,1,\,1)^{\top}$.

<ol class="al">

<li>

Calcula la similitud coseno y la distancia euclídea del texto $a$ a los otros tres textos.

</li>

<li>

¿Qué texto se parece más al texto $a$, según la distancia y según la similitud coseno? Explica la diferencia.

</li>

</ol>

:::loesung
(a) Con $\lVert\mathbf{x}_a\rVert=\sqrt5$, $\lVert\mathbf{x}_b\rVert=3$, $\lVert\mathbf{x}_c\rVert=\sqrt{20}$ y $\lVert\mathbf{x}_d\rVert=\sqrt3$:

<ul>

<li>

con el texto $b$: $\mathbf{x}_a^{\top}\mathbf{x}_b=0$, similitud coseno $0$; distancia $\sqrt{4+9+1}=\sqrt{14}\approx3{,}74$;

</li>

<li>

con el texto $c$: $\mathbf{x}_a^{\top}\mathbf{x}_c=8+0+2=10$, similitud coseno $10/(\sqrt5\sqrt{20})=1$; distancia $\sqrt{4+0+1}=\sqrt5\approx2{,}24$;

</li>

<li>

con el texto $d$: $\mathbf{x}_a^{\top}\mathbf{x}_d=3$, similitud coseno $3/(\sqrt5\sqrt3)\approx0{,}775$; distancia $\sqrt{1+1+0}=\sqrt2\approx1{,}41$.

</li>

</ul>

(b) Según la distancia, el más cercano es el texto $d$; según la similitud coseno, el texto $c$. El texto $c$ es $\mathbf{x}_c=2\mathbf{x}_a$: la misma distribución de palabras, solo que el doble de largo; en cuanto al contenido, el mismo tema. La distancia penaliza la mayor longitud; la similitud coseno solo ve la dirección. El texto $d$ es corto y por eso está cerca de cualquier texto corto, aunque no compartan tema. Para comparar contenidos, la medida adecuada es aquí la similitud coseno, y el texto $b$ no tiene nada en común con el texto $a$.
:::
:::

:::aufgabe Ejercicio 14 ★★★ Distancia y ángulo de vectores normalizados
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Demuestra: para vectores normalizados $\mathbf{u},\mathbf{v}$ con el ángulo $\varphi$ se cumple $\lVert\mathbf{u}-\mathbf{v}\rVert^2=2-2\cos\varphi$. ¿Qué se deduce de ello para el orden «parecido según la distancia» y «parecido según la similitud coseno» si se normalizan antes todos los ejemplos?

</li>

<li>

Comprueba la fórmula con los textos normalizados $\mathbf{x}_1$ y $\mathbf{x}_3$ de la subsección [5.4](#stufe-5-4).

</li>

<li>

Demuestra: $\lVert\mathbf{u}+\mathbf{v}\rVert=\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ se cumple si y solo si $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. ¿Cuándo ocurre esto?

</li>

</ol>

:::loesung
(a) Según [(4.1)](abstande-und-einheiten.html#gl-4-1), $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}=1+1-2\cos\varphi$, porque para vectores normalizados $\mathbf{u}^{\top}\mathbf{v}=\cos\varphi$. La distancia es, por tanto, una función decreciente de la similitud coseno: cuanto mayor es el coseno, menor es la distancia. Por eso, si se normalizan antes todos los ejemplos, la distancia y la similitud coseno ordenan los ejemplos exactamente igual.

(b) Los textos normalizados son $\mathbf{x}_1/\sqrt{13}$ y $\mathbf{x}_3/\sqrt{10}$, con el coseno $0{,}1754$. La fórmula da $2-2\cdot0{,}1754\approx1{,}649$. Directamente: $\mathbf{x}_1/\sqrt{13}-\mathbf{x}_3/\sqrt{10}\approx(0{,}832;\ 0{,}238;\ -0{,}949)^{\top}$, con el cuadrado de la longitud $0{,}692+0{,}057+0{,}900\approx1{,}649$.

(c) Ambos lados son no negativos, así que pueden compararse los cuadrados. Se tiene $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ y $(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2=\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2$. Ambos son iguales si y solo si $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. Según la desigualdad de Cauchy-Schwarz y su caso de igualdad, esto ocurre si y solo si uno de los vectores es un múltiplo del otro, y además con un factor $\ge0$, pues de lo contrario el producto escalar sería negativo. Intuitivamente: la desigualdad triangular solo se convierte en igualdad si el triángulo está aplastado y las dos flechas apuntan en la misma dirección.
:::
:::
