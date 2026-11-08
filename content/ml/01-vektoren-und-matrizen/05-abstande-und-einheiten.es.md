---
title: Distancias y unidades
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15210500
summary: Dos ejemplos son parecidos si sus vectores están cerca uno de otro.
tags: distancia, columna de la característica, centrado, desviación típica, estandariza
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Dos ejemplos son parecidos si sus vectores están cerca uno de otro. Esta sección mide distancias, muestra que el resultado depende de las unidades elegidas y presenta un procedimiento que hace comparables las características.
:::

### La distancia entre dos puntos de datos

<span class="anker" id="stufe-4-1"></span>

Dos viviendas son parecidas si se diferencian poco en todas las características. Las diferencias están en el vector diferencia $\mathbf{u}-\mathbf{v}$, la flecha de un punto al otro. Lo grande que es esta flecha lo dice una norma.

:::definition Definición 4.1 (Distancia)
<span class="anker" id="satz-4-1"></span>

La __distancia__ entre dos vectores $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ respecto de una norma es la norma de su diferencia, $\lVert\mathbf{u}-\mathbf{v}\rVert$. Si no se indica otra cosa, se trata de la distancia euclídea.
:::

De las propiedades de una norma se deducen las propiedades que se esperan de una distancia: nunca es negativa y solo es cero para puntos iguales; es igual de $\mathbf{u}$ a $\mathbf{v}$ que de $\mathbf{v}$ a $\mathbf{u}$, porque $\mathbf{v}-\mathbf{u}=-(\mathbf{u}-\mathbf{v})$; y el camino por un tercer punto $\mathbf{q}$ nunca es más corto, $\lVert\mathbf{u}-\mathbf{v}\rVert\le\lVert\mathbf{u}-\mathbf{q}\rVert+\lVert\mathbf{q}-\mathbf{v}\rVert$. Esta es la desigualdad triangular (N3), aplicada a $\mathbf{u}-\mathbf{v}=(\mathbf{u}-\mathbf{q})+(\mathbf{q}-\mathbf{v})$.

**Distancia y producto escalar.** Si se desarrolla el cuadrado de la distancia euclídea con las reglas de cálculo del producto escalar, se obtiene

<span class="anker" id="gl-4-1"></span>
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=(\mathbf{u}-\mathbf{v})^{\top}(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v} . \tag{4.1}$$

Con longitudes fijas se cumple, por tanto: cuanto mayor es el producto escalar, menor es la distancia. Ambos miden la semejanza, solo que en sentido opuesto.

⁠**Ejemplo numérico:** Las viviendas 1 y 2 se diferencian en $\mathbf{x}_1-\mathbf{x}_2=(20,\,1,\,2)^{\top}$. Su distancia euclídea es $\sqrt{405}\approx20{,}12$ (fig. [18](#abb-18)); en la norma 1 es $20+1+2=23$; en la norma del máximo, $20$.

:::abbildung ml/k1rabstand 18
La distancia euclídea entre las viviendas 1 y 2: primero la diferencia, después su longitud.
:::

Como comprobación de [(4.1)](#gl-4-1) con $\mathbf{u}=(1,\,2,\,2)^{\top}$ y $\mathbf{v}=(2,\,0,\,1)^{\top}$: a la izquierda, $\lVert(-1,\,2,\,1)^{\top}\rVert^2=6$; a la derecha, $9+5-2\cdot4=6$.

⁠**En resumen:** La distancia entre dos puntos de datos es la norma de su diferencia; estar cerca significa ser parecidos.

### Las distancias dependen de las unidades

<span class="anker" id="stufe-4-2"></span>

En el ejemplo numérico anterior, la distancia $20{,}12$ es casi exactamente la diferencia de superficie de $20\,\mathrm m^2$. De los $405$ del cuadrado de la distancia, $400$ proceden de la superficie. La diferencia de una habitación y dos kilómetros no desempeña prácticamente ningún papel, y ello solo porque las superficies en metros cuadrados son números grandes.

Otras tres viviendas muestran lo que se deduce de ello. La pregunta es cuál de las viviendas B y C se parece más a la vivienda A:

$$\text{A}=(60,\,2)^{\top},\qquad \text{B}=(63,\,4)^{\top},\qquad \text{C}=(54,\,2)^{\top}\qquad(\text{superficie en m}^2,\ \text{habitaciones}).$$

En metros cuadrados, $\lVert\text{A}-\text{B}\rVert=\sqrt{9+4}\approx3{,}61$ y $\lVert\text{A}-\text{C}\rVert=\sqrt{36+0}=6$: B está más cerca. Si se mide la superficie en unidades de $10\,\mathrm m^2$, se tiene $\text{A}=(6,\,2)^{\top}$, $\text{B}=(6{,}3;\ 4)^{\top}$, $\text{C}=(5{,}4;\ 2)^{\top}$ y $\lVert\text{A}-\text{B}\rVert=\sqrt{0{,}09+4}\approx2{,}02$, $\lVert\text{A}-\text{C}\rVert=0{,}6$: ahora C está más cerca. La figura [19](#abb-19) muestra ambas imágenes.

:::abbildung ml/k1einheiten 19
Las mismas tres viviendas: a la izquierda, con la superficie en $\mathrm m^2$; a la derecha, en unidades de $10\,\mathrm m^2$. Los dos ejes de cada imagen tienen la misma escala, de modo que la longitud de un segmento es la distancia euclídea. A la izquierda, B está más cerca de A (a trazos, la circunferencia de centro A que pasa por B); a la derecha, C.
:::

El mecanismo es sencillo. En el cuadrado de la distancia aparece, para cada característica, la diferencia al cuadrado. Si se mide una característica en otra unidad, sus números cambian en un factor $c$, y su contribución al cuadrado de la distancia cambia en $c^2$. Las contribuciones de las demás características no cambian. Una característica con números grandes determina la distancia casi por sí sola; una característica con números pequeños casi desaparece.

⁠**En resumen:** Las distancias entre ejemplos dependen de las unidades de las características; qué ejemplo se parece más a otro puede cambiar con un cambio de unidades.

:::hintergrund Toda elección de unidades es una ponderación
La distancia euclídea suma cuadrados de metros cuadrados, habitaciones y kilómetros. Numéricamente funciona, porque el ordenador solo ve números. Físicamente es una suma de magnitudes de distinta naturaleza, y las unidades deciden cuánto cuenta cada una. Quien da la superficie en $\mathrm m^2$ ha decidido con ello, sin quererlo, que $1\,\mathrm m^2$ de diferencia cuenta lo mismo que una habitación de diferencia. No hay ninguna elección correcta impuesta por la naturaleza. Hay que hacerla conscientemente, y el procedimiento siguiente es una de esas elecciones conscientes.
:::

### Desviaciones respecto de la media

<span class="anker" id="stufe-4-3"></span>

Para hacer comparables las características, se considera cada característica por separado a lo largo de todos los ejemplos. En la tabla [1](vektoren-daten-als-zahlenlisten.html#tab-1), son las columnas: las superficies de todas las viviendas forman el vector $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}\in\mathbb{R}^4$. Un vector así pertenece a una característica y tiene tantas componentes como ejemplos hay. Aquí se llama la __columna de la característica__.

Para la comparación no cuenta lo grandes que son las superficies, sino cuánto se diferencian. Por eso se mide cada superficie como desviación respecto del promedio. En electrotecnia, este paso consiste en restar la componente continua y quedarse solo con la componente alterna.

:::definition Definición 4.2 (Vector centrado)
<span class="anker" id="satz-4-2"></span>

Para $\mathbf{v}\in\mathbb{R}^N$ con la media $\bar v$, el vector

<span class="anker" id="gl-4-2"></span>
$$\tilde{\mathbf{v}}=\mathbf{v}-\bar v\,\mathbf 1=(v_1-\bar v,\,\dots,\,v_N-\bar v)^{\top} \tag{4.2}$$

se llama vector __centrado__. Sus componentes son las desviaciones respecto de la media.
:::

Las desviaciones siempre se compensan entre sí: $\mathbf 1^{\top}\tilde{\mathbf{v}}=\mathbf 1^{\top}\mathbf{v}-\bar v\,\mathbf 1^{\top}\mathbf 1=N\bar v-\bar v\,N=0$. El vector centrado tiene, por tanto, media cero.

⁠**Ejemplo numérico:** Las superficies $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}$ tienen la media $\bar v=65$. Centrado, el vector es $\tilde{\mathbf{v}}=(-5,\,-25,\,25,\,5)^{\top}$, y las desviaciones suman efectivamente cero (fig. [20](#abb-20)). Los números de habitaciones $(2,\,1,\,4,\,3)^{\top}$ tienen la media $2{,}5$ y, centrados, son $(-0{,}5;\ -1{,}5;\ 1{,}5;\ 0{,}5)^{\top}$; las distancias $(3,\,1,\,6,\,2)^{\top}$ tienen la media $3$ y, centradas, son $(0,\,-2,\,3,\,-1)^{\top}$.

:::abbildung ml/k1rzentriert 20
La media de las superficies y la suma de las desviaciones respecto de la media, en $\mathrm m^2$.
:::

⁠**En resumen:** Centrar resta a cada componente la media; quedan las desviaciones, que suman cero.

### La desviación típica

<span class="anker" id="stufe-4-4"></span>

Cuánto oscila una característica se ve en el tamaño de sus desviaciones. Un valor absoluto típico de una componente es el valor eficaz de la subsección [3.6](normen-die-groe-eines-vektors.html#stufe-3-6). Aplicado al vector centrado, da el tamaño típico de las desviaciones respecto de la media. En el lenguaje de la electrotecnia: el valor eficaz de la componente alterna.

:::definition Definición 4.3 (Desviación típica)
<span class="anker" id="satz-4-3"></span>

La __desviación típica__ de un vector $\mathbf{v}\in\mathbb{R}^N$ es el valor eficaz de su vector centrado:

<span class="anker" id="gl-4-3"></span>
$$\operatorname{std}(\mathbf{v})=\operatorname{rms}(\tilde{\mathbf{v}})=\frac{\lVert\mathbf{v}-\bar v\,\mathbf 1\rVert}{\sqrt N}=\sqrt{\frac1N\sum_{i=1}^N(v_i-\bar v)^2} . \tag{4.3}$$
:::

La desviación típica tiene la misma unidad que la característica. Es cero si y solo si todas las componentes son iguales. Muchos textos dividen en [(4.3)](#gl-4-3) por $N-1$ en lugar de por $N$. Con muchos ejemplos, la diferencia es pequeña. Esta serie divide por $N$ y lo indica cuando, en alguna ocasión, deba ser de otro modo.

⁠**Ejemplo numérico:** Las superficies centradas $(-5,\,-25,\,25,\,5)^{\top}$ tienen la suma de cuadrados $1\,300$, así que $\operatorname{std}(\mathbf{v})=\sqrt{325}\approx18{,}03\,\mathrm m^2$ (fig. [21](#abb-21)). Del mismo modo se obtiene para las habitaciones $\sqrt{5/4}\approx1{,}118$ y para las distancias $\sqrt{14/4}\approx1{,}871$ km.

:::abbildung ml/k1rstd 21
La desviación típica de las superficies: elevar las desviaciones al cuadrado, promediar, extraer la raíz. El resultado $\sqrt{325}\approx18{,}03$ tiene la unidad $\mathrm m^2$.
:::

⁠**En resumen:** La desviación típica es el valor eficaz de las desviaciones respecto de la media, la oscilación típica de una característica.

:::hintergrund La componente continua y la alterna se reparten la potencia
Un vector es la suma de su componente continua $\bar v\,\mathbf 1$ y su componente alterna $\tilde{\mathbf{v}}$. Para el cuadrado de la longitud se cumple, según las reglas de cálculo del producto escalar,

$$\lVert\bar v\,\mathbf 1+\tilde{\mathbf{v}}\rVert^2=\bar v^2\,\mathbf 1^{\top}\mathbf 1+2\,\bar v\,\mathbf 1^{\top}\tilde{\mathbf{v}}+\lVert\tilde{\mathbf{v}}\rVert^2=N\bar v^2+0+\lVert\tilde{\mathbf{v}}\rVert^2 ,$$

porque las desviaciones suman cero. Si se divide por $N$, resulta $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$. Es el mismo reparto que en una corriente mixta, cuya potencia en una resistencia se compone de la potencia de la componente continua y la de la componente alterna. Para las superficies: $\operatorname{rms}^2=(3600+1600+8100+4900)/4=4550=65^2+325$.
:::

### Estandarizar

<span class="anker" id="stufe-4-5"></span>

Ahora cada característica puede medirse en unidades de su propia oscilación típica. En lugar de «$25\,\mathrm m^2$ por encima del promedio» se dice «$1{,}39$ desviaciones típicas por encima del promedio». En este lenguaje, todas las características tienen el mismo orden de magnitud, independientemente de la unidad en la que se midieran originalmente.

:::definition Definición 4.4 (Estandarizar)
<span class="anker" id="satz-4-4"></span>

Una característica $j$, cuya columna tiene la media $\bar x_j$ y la desviación típica $s_j>0$, se __estandariza__ calculando para cada valor

<span class="anker" id="gl-4-4"></span>
$$z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad i=1,\dots,N, \tag{4.4}$$

y sustituyendo cada valor original por este número. Los números $z_{ij}$ se llaman los valores estandarizados.
:::

La columna estandarizada de la característica tiene media $0$ y desviación típica $1$, pues centrar hace cero la media y la división por $s_j$ hace que la desviación típica valga uno. Los valores ya no tienen unidad.

⁠**Ejemplo numérico 1: el conjunto de datos de viviendas.** Con las medias $65$, $2{,}5$, $3$ y las desviaciones típicas $18{,}03$, $1{,}118$, $1{,}871$, las cuatro viviendas se convierten en

$$\begin{aligned} \mathbf{z}_1&\approx(-0{,}28;\ -0{,}45;\ 0)^{\top}, & \mathbf{z}_2&\approx(-1{,}39;\ -1{,}34;\ -1{,}07)^{\top},\\ \mathbf{z}_3&\approx(1{,}39;\ 1{,}34;\ 1{,}60)^{\top}, & \mathbf{z}_4&\approx(0{,}28;\ 0{,}45;\ -0{,}53)^{\top}. \end{aligned}$$

Las tres características se mueven ahora en el mismo intervalo de valores.

⁠**Ejemplo numérico 2: A, B y C.** Las tres viviendas de la subsección [4.2](#stufe-4-2) tienen la superficie media $59\,\mathrm m^2$, con la desviación típica $\sqrt{14}\approx3{,}74\,\mathrm m^2$, y en promedio $8/3$ habitaciones, con la desviación típica $\sqrt{8/9}\approx0{,}943$. Tras estandarizar, $\lVert\text A-\text B\rVert\approx2{,}27$ y $\lVert\text A-\text C\rVert\approx1{,}60$. A se parece más, por tanto, a C, y este juicio ya no depende de la unidad de la superficie.

Que la unidad desaparezca vale en general:

:::satz Teorema 4.5 (Los valores estandarizados no dependen de la unidad)
<span class="anker" id="satz-4-5"></span>

Si se convierte una característica a otra unidad, $v_i'=\alpha\,v_i+\beta$ para todo $i$ con números $\alpha>0$ y $\beta$, sus valores estandarizados no cambian.
:::

:::beweis Independencia de la unidad
La media pasa a ser $\bar v'=\frac1N\sum_i(\alpha\,v_i+\beta)=\alpha\,\bar v+\beta$, y las desviaciones, $v_i'-\bar v'=\alpha\,(v_i-\bar v)$. Según [(4.3)](#gl-4-3), entonces $\operatorname{std}(\mathbf{v}')=|\alpha|\operatorname{std}(\mathbf{v})=\alpha\operatorname{std}(\mathbf{v})$. En el cociente [(4.4)](#gl-4-4) se simplifica $\alpha$, y $\beta$ ya ha desaparecido al centrar.
:::

El sumando $\beta$ cubre también conversiones con el cero desplazado, como de grados Celsius a grados Fahrenheit.

⁠**En resumen:** Estandarizar mide cada característica como desviación respecto de la media en múltiplos de su desviación típica; después, las distancias ya no dependen de las unidades.

:::hintergrund ¿Por qué precisamente la desviación típica como escala?
Para cada característica se necesita una escala que, en un cambio de unidades, cambie en el mismo factor que las diferencias entre los valores. Entonces se cancela. Toda magnitud que se calcula a partir de las diferencias entre los valores de la característica y tiene la unidad de la característica lo consigue: la desviación típica, pero también el recorrido del valor más pequeño al más grande. La desviación típica es la elección habitual porque tiene en cuenta todos los valores y no solo los dos extremos.

Lo que estandarizar hace con una distancia se ve si se restan dos ejemplos estandarizados $\mathbf{z}_a$ y $\mathbf{z}_b$. La media desaparece, $z_{aj}-z_{bj}=(x_{aj}-x_{bj})/s_j$, y queda

$$\lVert\mathbf{z}_a-\mathbf{z}_b\rVert^2=\sum_{j=1}^d\frac{(x_{aj}-x_{bj})^2}{s_j^2} .$$

La distancia entre los valores estandarizados es, por tanto, la distancia ordinaria en la que la diferencia al cuadrado en la característica $j$ cuenta con el peso $1/s_j^2$. Para las viviendas A y B es $3^2/14+2^2/(8/9)=9/14+9/2\approx5{,}14$, y su raíz, $2{,}27$, como antes.

Pero estandarizar es en sí mismo una decisión. Da a cada característica el mismo peso en la distancia, incluso a una característica que no desempeña ningún papel para la pregunta. Y una característica que tiene el mismo valor en todos los ejemplos tiene desviación típica cero y no puede estandarizarse; pero tampoco distingue los ejemplos ni contribuye a ninguna distancia.
:::

:::aufgabe Ejercicio 9 ★ Componente continua y componente alterna
<span class="anker" id="aufg-9"></span>

Una señal tiene las muestras $\mathbf{x}=(1,\,3,\,1,\,-1)^{\top}$. Calcula la media, el vector centrado, la desviación típica y el valor eficaz. Comprueba $\operatorname{rms}(\mathbf{x})^2=\bar x^2+\operatorname{std}(\mathbf{x})^2$.

:::loesung
La media es $\bar x=(1+3+1-1)/4=1$; el vector centrado, $\tilde{\mathbf{x}}=(0,\,2,\,0,\,-2)^{\top}$. La desviación típica es $\sqrt{(0+4+0+4)/4}=\sqrt2\approx1{,}414$; el valor eficaz, $\sqrt{(1+9+1+1)/4}=\sqrt3\approx1{,}732$. Comprobación: $\operatorname{rms}^2=3=1^2+(\sqrt2)^2=\bar x^2+\operatorname{std}^2$. La componente continua y la componente alterna se reparten la «potencia» $3$ en la proporción $1:2$.
:::
:::

:::aufgabe Ejercicio 10 ★★ ¿Qué vivienda se parece más a la vivienda 1?
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Calcula las distancias euclídeas de la vivienda 1 a las viviendas 2, 3 y 4 con los valores de la tabla [1](vektoren-daten-als-zahlenlisten.html#tab-1). ¿Qué fracción del cuadrado de la distancia a la vivienda 2 procede de la superficie?

</li>

<li>

Calcula las mismas distancias con los valores estandarizados de la subsección [4.5](#stufe-4-5). ¿Qué fracción del cuadrado de la distancia a la vivienda 2 procede ahora de la superficie?

</li>

<li>

¿Qué vivienda se parece más a la vivienda 1 en cada caso? ¿Qué ha cambiado aquí la estandarización, si no la respuesta?

</li>

</ol>

:::loesung
(a) Con los valores de la tabla:

$$\begin{aligned} \lVert\mathbf{x}_1-\mathbf{x}_2\rVert&=\sqrt{20^2+1^2+2^2}=\sqrt{405}\approx20{,}12,\\ \lVert\mathbf{x}_1-\mathbf{x}_3\rVert&=\sqrt{30^2+2^2+3^2}=\sqrt{913}\approx30{,}22,\\ \lVert\mathbf{x}_1-\mathbf{x}_4\rVert&=\sqrt{10^2+1^2+1^2}=\sqrt{102}\approx10{,}10 . \end{aligned}$$

De los $405$ del cuadrado de la distancia a la vivienda 2, $400$ proceden de la superficie, es decir, el $98{,}8$ %.

(b) Con los vectores estandarizados de la subsección [4.5](#stufe-4-5) se tiene $\mathbf{z}_1-\mathbf{z}_2\approx(1{,}109;\ 0{,}894;\ 1{,}069)^{\top}$, con los cuadrados $1{,}231$, $0{,}800$ y $1{,}143$. La distancia es $\sqrt{3{,}174}\approx1{,}78$. Del mismo modo se obtiene $\lVert\mathbf{z}_1-\mathbf{z}_3\rVert\approx2{,}92$ y $\lVert\mathbf{z}_1-\mathbf{z}_4\rVert\approx1{,}18$. La fracción del cuadrado de la distancia a la vivienda 2 que procede de la superficie es ahora $1{,}231/3{,}174\approx38{,}8$ %.

(c) En ambos casos, la vivienda más parecida es la vivienda 4, seguida de la vivienda 2 y la vivienda 3. Aquí el orden no cambia porque, en este pequeño conjunto de datos, las viviendas grandes también tienen más habitaciones y están más lejos del centro; las tres características cuentan aproximadamente la misma historia. Lo que ha cambiado es *por qué* la vivienda 4 es la más parecida: con los valores brutos decide casi solo la superficie; con los estandarizados, las tres características contribuyen aproximadamente por igual. Que la respuesta siga siendo la misma es una casualidad de estos datos; con las viviendas A, B y C de la subsección [4.2](#stufe-4-2), sí cambió.
:::
:::

:::aufgabe Ejercicio 11 ★★ Celsius o Fahrenheit
<span class="anker" id="aufg-11"></span>

En cuatro días se midieron a mediodía $10$, $20$, $15$ y $25$ $^\circ$C.

<ol class="al">

<li>

Convierte a grados Fahrenheit ($F=1{,}8\,C+32$). Calcula en ambas unidades la media y la desviación típica.

</li>

<li>

Calcula los valores estandarizados en ambas unidades y compáralos.

</li>

<li>

¿Qué ocurre con los valores estandarizados si se convierte una característica con un factor negativo, por ejemplo $v_i'=-v_i$?

</li>

</ol>

:::loesung
(a) En grados Fahrenheit, los valores son $1{,}8\cdot10+32=50$, $68$, $59$ y $77$. En grados Celsius, la media es $17{,}5$ y la desviación típica, $\sqrt{(56{,}25+6{,}25+6{,}25+56{,}25)/4}=\sqrt{31{,}25}\approx5{,}590$; en grados Fahrenheit, la media es $63{,}5=1{,}8\cdot17{,}5+32$ y la desviación típica, $\approx10{,}062=1{,}8\cdot5{,}590$. El sumando $32$ solo desplaza la media; el factor $1{,}8$ estira también la desviación típica.

(b) En ambas unidades, los valores estandarizados son $\approx(-1{,}342;\ 0{,}447;\ -0{,}447;\ 1{,}342)$. Así lo exige el teorema de la subsección [4.5](#stufe-4-5): el sumando desaparece al centrar, y el factor se simplifica con la desviación típica.

(c) Con $v_i'=-v_i$, todas las desviaciones respecto de la media se multiplican por $-1$, pero la desviación típica, por $|-1|=1$. Los valores estandarizados cambian, por tanto, de signo. Para las distancias entre ejemplos esto da igual, pues $\lVert-\mathbf{u}\rVert=\lVert\mathbf{u}\rVert$; el conjunto de datos solo se refleja.
:::
:::
