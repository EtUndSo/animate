---
title: El producto escalar
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15210300
summary: Dos vectores de la misma longitud dan un único número si se multiplican sus componentes por parejas y se suman los productos.
tags: producto escalar, peso, suma ponderada, modelo, predicción, vector de unos, media
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Dos vectores de la misma longitud dan un único número si se multiplican sus componentes por parejas y se suman los productos. Este cálculo es el más frecuente de todo el aprendizaje automático: convierte valores medidos en una estimación y compara datos con un patrón.
:::

### El producto escalar de dos vectores

<span class="anker" id="stufe-2-1"></span>

Una cuenta de la compra se hace así: cantidad por precio para cada artículo y, después, sumarlo todo. El mismo cálculo con dos vectores cualesquiera se llama producto escalar.

Puede imaginarse como el encuentro de una fila con una columna. El primer vector se escribe como fila; el segundo, como columna a su lado. Después se multiplica el primer elemento de la fila por el primero de la columna, el segundo por el segundo, y así sucesivamente, y se suma:

$$\begin{pmatrix}1&2&3\end{pmatrix}\begin{pmatrix}4\\-1\\2\end{pmatrix}=1\cdot4+2\cdot(-1)+3\cdot2=8 .$$

:::definition Definición 2.1 (Producto escalar)
<span class="anker" id="satz-2-1"></span>

El __producto escalar__ de dos vectores $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ es el número

<span class="anker" id="gl-2-1"></span>
$$\mathbf{u}^{\top}\mathbf{v}=\sum_{j=1}^{d}u_j\,v_j=u_1v_1+u_2v_2+\dots+u_dv_d . \tag{2.1}$$
:::

La notación $\mathbf{u}^{\top}\mathbf{v}$ dice exactamente lo que ocurre: $\mathbf{u}^{\top}$ es $\mathbf{u}$ como fila, y la fila se encuentra con la columna $\mathbf{v}$. El resultado es un escalar; de ahí el nombre.

:::satz Teorema 2.2 (Reglas de cálculo del producto escalar)
<span class="anker" id="satz-2-2"></span>

Para todos los $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ y todo escalar $c$ se cumple:

<ol class="rm">

<li>

$\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ (simétrico);

</li>

<li>

$(c\,\mathbf{u})^{\top}\mathbf{v}=c\,(\mathbf{u}^{\top}\mathbf{v})$ y $(\mathbf{u}+\mathbf{q})^{\top}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}+\mathbf{q}^{\top}\mathbf{v}$ (lineal, igualmente en el segundo vector);

</li>

<li>

$\mathbf{u}^{\top}\mathbf{u}=\sum_ju_j^2\ge0$, y $\mathbf{u}^{\top}\mathbf{u}=0$ solo para $\mathbf{u}=\mathbf{0}$.

</li>

</ol>
:::

:::beweis Reglas de cálculo del producto escalar
(i) se deduce de $u_jv_j=v_ju_j$ para cada componente. (ii) es la regla de las sumas [(1.2)](vektoren-daten-als-zahlenlisten.html#gl-1-2): $\sum_j(c\,u_j)v_j=c\sum_ju_jv_j$ y $\sum_j(u_j+q_j)v_j=\sum_ju_jv_j+\sum_jq_jv_j$. (iii) Ningún sumando $u_j^2$ es negativo. La suma solo es cero si cada sumando es cero, es decir, si cada $u_j=0$.
:::

⁠**Ejemplo numérico:** Para $\mathbf{u}=(1,\,2,\,3)^{\top}$ y $\mathbf{v}=(4,\,-1,\,2)^{\top}$ se tiene $\mathbf{u}^{\top}\mathbf{v}=8$ y $\mathbf{u}^{\top}\mathbf{u}=14$ (fig. [6](#abb-6)). En el orden inverso se obtiene el mismo número, $\mathbf{v}^{\top}\mathbf{u}=4\cdot1+(-1)\cdot2+2\cdot3=8$, como exige la simetría.

:::abbildung ml/k1rskp 6
Dos productos escalares paso a paso: componente por componente y, después, la suma de los productos. El producto escalar de un vector consigo mismo es la suma de los cuadrados de sus componentes.
:::

⁠**En resumen:** El producto escalar multiplica dos vectores componente por componente y suma los productos; es un número.

:::hintergrund Otras notaciones para lo mismo
En muchos libros aparece $\mathbf{u}\cdot\mathbf{v}$ o $\langle\mathbf{u},\mathbf{v}\rangle$ en lugar de $\mathbf{u}^{\top}\mathbf{v}$; en inglés se llama *dot product* o *inner product*. Se trata del mismo número. Esta serie escribe $\mathbf{u}^{\top}\mathbf{v}$ porque así se ve en la propia notación que una fila se encuentra con una columna. Esto compensa en cuanto entran en juego tablas de números.
:::

### Pesos y sumas ponderadas

<span class="anker" id="stufe-2-2"></span>

Una agente inmobiliaria estima mentalmente el precio de una vivienda más o menos así: cada metro cuadrado vale unos $3$ mil euros, cada habitación aporta otros $10$ mil euros y cada kilómetro de distancia al centro resta $4$ mil euros. Es decir, toma cada característica con un factor propio y lo suma todo.

El número con el que una característica entra en un cálculo así se llama su __peso__. Un peso grande y positivo significa que cada unidad de esa característica aumenta mucho el resultado. Un peso negativo significa que la característica reduce el resultado.

:::definition Definición 2.3 (Suma ponderada)
<span class="anker" id="satz-2-3"></span>

Para un vector de pesos $\mathbf{w}=(w_1,\dots,w_d)^{\top}$ y un ejemplo $\mathbf{x}\in\mathbb{R}^d$, la __suma ponderada__ es

<span class="anker" id="gl-2-2"></span>
$$\hat y=\mathbf{w}^{\top}\mathbf{x}=\sum_{j=1}^{d}w_j\,x_j . \tag{2.2}$$
:::

Una regla de cálculo fija que, a partir de las características de un ejemplo, calcula un número se llama un __modelo__. El número que el modelo da para un ejemplo se llama su __predicción__. El «sombrero» sobre la $y$ de $\hat y$ indica que se trata de un valor estimado mediante un cálculo y no de un valor medido. En este capítulo, los pesos siempre vienen dados; de dónde salen unos buenos pesos es una cuestión aparte.

⁠**Ejemplo numérico:** La agente inmobiliaria usa los pesos $\mathbf{w}=(3,\,10,\,-4)^{\top}$ en miles de euros por metro cuadrado, por habitación y por kilómetro. Para la vivienda 1 se tiene $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$ (fig. [7](#abb-7)), es decir, $188$ mil euros.

:::abbildung ml/k1rgewicht 7
La estimación de la agente inmobiliaria para la vivienda 1: cada característica por su peso y, después, la suma. Las contribuciones de las tres características son $180$, $20$ y $-12$ mil euros.
:::

Para las demás viviendas se obtiene igualmente $\hat y_2=126$, $\hat y_3=286$ y $\hat y_4=232$. Cada producto $w_jx_j$ tiene como unidad los miles de euros, porque la unidad de la característica se simplifica con la unidad del denominador del peso. Solo por eso pueden sumarse los tres productos.

⁠**En resumen:** Una suma ponderada es el producto escalar $\mathbf{w}^{\top}\mathbf{x}$ de pesos y características; es el modelo más sencillo que hace una predicción a partir de características.

:::hintergrund Un peso grande no significa que la característica sea importante
En el caso de la agente inmobiliaria, el peso de las habitaciones, $10$, es más del triple que el de la superficie, $3$. Aun así, en la vivienda 1 la superficie aporta $180$ mil euros y el número de habitaciones solo $20$. La razón: un peso vale por unidad de la característica, y la superficie tiene muchas unidades. Si se mide la superficie en unidades de $10\,\mathrm m^2$, la vivienda 1 mide solo $6$ unidades, y el mismo modelo necesita el peso de $30$ mil euros por $10\,\mathrm m^2$. La predicción sigue siendo la misma; solo el peso se ha hecho diez veces mayor. El tamaño de un peso depende, por tanto, de la unidad elegida. Si se quiere saber cuánto aporta una característica a la predicción, hay que mirar el producto $w_jx_j$, no el peso por sí solo.
:::

### Suma y media como producto escalar

<span class="anker" id="stufe-2-3"></span>

Muchos cálculos cotidianos son productos escalares con un segundo vector especialmente sencillo. Lo que más se necesita es la suma y el promedio de todas las componentes.

El __vector de unos__ $\mathbf 1\in\mathbb{R}^n$ tiene solo unos como componentes. El producto escalar con él simplemente suma todas las componentes: $\mathbf 1^{\top}\mathbf{v}=v_1+\dots+v_n$.

:::definition Definición 2.4 (Media)
<span class="anker" id="satz-2-4"></span>

La __media__ de las componentes de un vector $\mathbf{v}\in\mathbb{R}^n$ es

<span class="anker" id="gl-2-3"></span>
$$\bar v=\frac1n\sum_{i=1}^nv_i=\frac1n\,\mathbf 1^{\top}\mathbf{v} . \tag{2.3}$$
:::

Otros cálculos de este tipo: el producto escalar con un vector unitario selecciona una componente, $\mathbf{e}_j^{\top}\mathbf{v}=v_j$, pues todos los demás productos contienen un cero. El producto escalar de un vector consigo mismo es la suma de los cuadrados, $\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$. Las cantidades por los precios, sumadas, dan el importe de la factura. Y evaluar un polinomio $p(t)=c_1+c_2t+\dots+c_nt^{n-1}$ en un punto $t$ significa formar el producto escalar $\mathbf{c}^{\top}\mathbf{z}$ de sus coeficientes $\mathbf{c}=(c_1,\dots,c_n)^{\top}$ con las potencias $\mathbf{z}=(1,\,t,\,t^2,\dots,t^{n-1})^{\top}$. Para $p(t)=1+2t+3t^2$ en el punto $t=2$, esto es $(1,\,2,\,3)\,(1,\,2,\,4)^{\top}=1+4+12=17$.

⁠**Ejemplo numérico:** La vivienda 1 ha consumido de enero a marzo $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh de electricidad (subsección [1.4](vektoren-daten-als-zahlenlisten.html#stufe-1-4)). En total son $\mathbf 1^{\top}\mathbf{u}=750$ kWh, en promedio $\bar u=250$ kWh al mes (fig. [8](#abb-8)). El consumo de febrero es $\mathbf{e}_2^{\top}\mathbf{u}=250$ kWh.

:::abbildung ml/k1rmittel 8
Suma y media del consumo eléctrico como producto escalar con el vector de unos, en kWh.
:::

Si el kilovatio hora cuesta en los tres meses $\mathbf{p}=(0{,}32;\ 0{,}34;\ 0{,}28)^{\top}$ euros, la factura de la luz es el producto escalar de precios y cantidades: $\mathbf{p}^{\top}\mathbf{u}=233$ euros (fig. [9](#abb-9)). Cada producto $p_ju_j$ es el importe de un mes, en euros por kWh multiplicados por kWh, es decir, en euros.

:::abbildung ml/k1rstrom 9
La factura de la luz como producto escalar: precio por cantidad para cada mes y, después, la suma, en euros.
:::

⁠**En resumen:** La suma, la media, la selección de una componente y la suma de cuadrados son productos escalares con $\mathbf 1$, $\tfrac1n\mathbf 1$, $\mathbf{e}_j$ y el propio vector.

### El producto escalar como comparación con un patrón

<span class="anker" id="stufe-2-4"></span>

Se quiere comprobar si una señal medida salta arriba y abajo de una muestra a la siguiente. Para ello se escribe el patrón buscado como vector, aquí $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, y se forma el producto escalar con la señal.

Lo que ocurre lo muestra la fig. [10](#abb-10). Cada muestra se multiplica por el valor del patrón en la misma posición. Si la señal tiene en una posición el mismo signo que el patrón, el producto es positivo; si tiene el signo contrario, es negativo. Si la señal sigue al patrón en todas partes, se acumulan solo contribuciones positivas en una suma grande. Si la señal no tiene nada que ver con el patrón, las contribuciones positivas y negativas se compensan entre sí.

:::abbildung ml/k1muster 10
Comparación con un patrón mediante el producto escalar. Arriba, el patrón $\mathbf{w}=(1,-1,1,-1)^{\top}$; en el centro, dos señales; abajo, los productos $w_j\,x_j$ en cada posición $j$. A la izquierda, la señal $\mathbf{x}=(2,-1,3,-2)^{\top}$ salta al ritmo del patrón: todos los productos son positivos y la suma es $8$. A la derecha, $\mathbf{x}'=(2,2,3,3)^{\top}$ sube de forma regular: los productos se compensan y la suma es $0$.
:::

Dicho con precisión: la contribución de la posición $j$ al producto escalar $\mathbf{w}^{\top}\mathbf{x}$ es $w_jx_j$. Es positiva si $w_j$ y $x_j$ tienen el mismo signo, y negativa si tienen signos contrarios. Cuanto mayores sean los valores absolutos en las posiciones con signo coincidente, mayor será el producto escalar.

En procesamiento de señales, este cálculo se conoce como correlación. La correlación cruzada de dos secuencias reales $x[n]$ e $y[n]$ con desplazamiento cero es $\sum_nx[n]\,y[n]$. Si se escriben las muestras de dos señales de longitud finita como vectores $\mathbf{x}$ y $\mathbf{y}$, esto es exactamente el producto escalar $\mathbf{x}^{\top}\mathbf{y}$. La energía de una señal, $\sum_nx[n]^2$, es igualmente $\mathbf{x}^{\top}\mathbf{x}$. La comparación con un patrón no es, por tanto, una herramienta nueva, sino la misma con la que un correlador busca un patrón conocido en una señal.

⁠**Ejemplo numérico:** Con el patrón alternante $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ se tiene $\mathbf{w}^{\top}\mathbf{x}=8$ para $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ y $\mathbf{w}^{\top}\mathbf{x}'=0$ para $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$ (fig. [11](#abb-11)). Con el patrón constante $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ ocurre al revés: $\mathbf 1^{\top}\mathbf{x}=2$, pero $\mathbf 1^{\top}\mathbf{x}'=10$. La señal $\mathbf{x}$, por tanto, alterna sobre todo; $\mathbf{x}'$ es sobre todo constante.

:::abbildung ml/k1rmuster 11
El patrón alternante $\mathbf{w}$ con dos señales. Arriba, $\mathbf{x}$ sigue al patrón: los cuatro productos son positivos. Abajo, $\mathbf{x}'$ sube de forma regular: los productos se compensan por parejas.
:::

También la suma ponderada de la agente inmobiliaria es una comparación con un patrón. Su patrón $\mathbf{w}=(3,\,10,\,-4)^{\top}$ describe lo que hace valiosa una vivienda: mucha superficie, muchas habitaciones, poca distancia. Cuanto mejor encaja una vivienda con este patrón, mayor es su predicción.

⁠**En resumen:** El producto escalar $\mathbf{w}^{\top}\mathbf{x}$ es grande si $\mathbf{x}$ tiene valores grandes allí donde el patrón $\mathbf{w}$ tiene valores grandes del mismo signo; es la correlación con desplazamiento cero.

:::hintergrund La función de correlación consta solo de productos escalares
La correlación cruzada no compara una señal con un patrón en una sola posición, sino para cada desplazamiento posible. Para cada desplazamiento $k$, su valor es un producto escalar: la señal con el patrón desplazado $k$ pasos. La función de correlación entera es, por tanto, una sucesión de productos escalares, uno por desplazamiento. Donde el patrón está contenido en la señal, se acumulan las contribuciones positivas, y la función de correlación tiene allí su valor máximo. Así encuentra un receptor de radar el eco de su propio pulso, y un receptor de radio el comienzo de una trama de datos conocida. En el aprendizaje automático, el desplazamiento suele quedar fijo en cero: se compara un ejemplo en su conjunto con un patrón.
:::

:::aufgabe Ejercicio 4 ★ Comprobar las reglas de cálculo
<span class="anker" id="aufg-4"></span>

Sean $\mathbf{u}=(1,\,0,\,2)^{\top}$, $\mathbf{v}=(3,\,-1,\,1)^{\top}$ y $\mathbf{q}=(0,\,2,\,1)^{\top}$. Calcula $\mathbf{u}^{\top}\mathbf{v}$, $\mathbf{v}^{\top}\mathbf{u}$, $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})$, $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}$, $(3\mathbf{u})^{\top}\mathbf{v}$ y $\mathbf{u}^{\top}\mathbf{u}$. ¿Qué regla de cálculo muestra cada comparación?

:::loesung
Se tiene $\mathbf{u}^{\top}\mathbf{v}=3+0+2=5$ y $\mathbf{v}^{\top}\mathbf{u}=3+0+2=5$: el producto escalar es simétrico, la regla (i). Con $\mathbf{v}+\mathbf{q}=(3,\,1,\,2)^{\top}$ se tiene $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})=3+0+4=7$, y $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}=5+(0+0+2)=7$: linealidad en el segundo vector, la regla (ii). Además, $(3\mathbf{u})^{\top}\mathbf{v}=(3,0,6)\,(3,-1,1)^{\top}=9+0+6=15=3\cdot5$, también la regla (ii). Por último, $\mathbf{u}^{\top}\mathbf{u}=1+0+4=5>0$, como exige la regla (iii) para $\mathbf{u}\ne\mathbf{0}$.
:::
:::

:::aufgabe Ejercicio 5 ★★ La estimación de la agente inmobiliaria
<span class="anker" id="aufg-5"></span>

Usa los pesos $\mathbf{w}=(3,\,10,\,-4)^{\top}$ de la subsección [2.2](#stufe-2-2).

<ol class="al">

<li>

Calcula las predicciones para las cuatro viviendas. ¿Qué unidad tienen?

</li>

<li>

En la vivienda 2 se levanta un tabique; después tiene dos habitaciones con la misma superficie. ¿Cómo cambia la predicción, y por qué el cambio no depende de la superficie?

</li>

<li>

Un compañero dice: «Para la agente inmobiliaria, lo que más cuenta son las habitaciones; tienen el peso más grande». Comprueba la afirmación con la vivienda 1 comparando las tres contribuciones $w_jx_{1j}$.

</li>

</ol>

:::loesung
(a) Como en la subsección [2.2](#stufe-2-2): $188$, $126$, $286$ y $232$, en cada caso en miles de euros. La unidad son miles de euros, porque cada peso tiene la unidad «miles de euros por unidad de la característica», y la unidad de la característica se simplifica en el producto.

(b) La vivienda 2 pasa a ser $(40,\,2,\,1)^{\top}$. La predicción sube de $126$ a $120+20-4=136$, es decir, en $10$. En general, si la segunda característica cambia en $\Delta x_2$, la suma ponderada cambia en $w_2\,\Delta x_2$, pues $\mathbf{w}^{\top}(\mathbf{x}+\Delta x_2\,\mathbf{e}_2)=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,\mathbf{w}^{\top}\mathbf{e}_2=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,w_2$. Las demás características no influyen en ello. Esa es la linealidad del producto escalar: cada característica contribuye por sí sola, sin interacción con las demás.

(c) Las contribuciones en la vivienda 1 son $w_1x_{11}=180$, $w_2x_{12}=20$ y $w_3x_{13}=-12$. Con diferencia, la mayor contribución es la de la superficie, aunque su peso es, en valor absoluto, el menor. La afirmación del compañero confunde el peso por unidad con la contribución a la predicción; la superficie tiene muchísimas unidades.
:::
:::

:::aufgabe Ejercicio 6 ★★ Un patrón para señales crecientes
<span class="anker" id="aufg-6"></span>

Se quiere comprobar si una señal con cuatro muestras crece. Como patrón se propone $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$.

<ol class="al">

<li>

Calcula $\mathbf{w}^{\top}\mathbf{x}$ para $\mathbf{x}=(1,2,3,4)^{\top}$, $(4,3,2,1)^{\top}$, $(5,5,5,5)^{\top}$ y $(1,3,2,4)^{\top}$, e interpreta los resultados.

</li>

<li>

¿Por qué toda señal constante $c\,\mathbf1$ da exactamente cero? Usa $\mathbf 1^{\top}\mathbf{w}$.

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$: la señal crece, y el resultado es claramente positivo. $\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$: la señal decrece, y el resultado es igual de claramente negativo. $\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$: constante, sin subida. $\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$: la señal crece en conjunto, con un retroceso en el medio, y el resultado es algo menor que con la subida regular. El patrón pondera negativamente los valores tempranos y positivamente los tardíos; reacciona, por tanto, a si los valores tardíos son mayores que los tempranos.

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$. Por eso, para una señal constante, $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$. Como los pesos suman cero, el patrón ignora por completo una componente continua común: solo mide diferencias entre las muestras.
:::
:::
