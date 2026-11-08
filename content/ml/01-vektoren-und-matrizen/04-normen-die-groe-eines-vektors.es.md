---
title: Normas: el tamaño de un vector
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15210400
summary: ¿Qué tamaño tiene un vector?
tags: norma euclídea, longitud, normalizado, normalizar, norma 1, norma del máximo, norma, desigualdad triangular
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
¿Qué tamaño tiene un vector? Hay varias respuestas correctas. Esta sección presenta las tres más importantes, aclara qué tienen en común y muestra para qué se necesitan: para medir lo grande que es un error.
:::

### La norma euclídea

<span class="anker" id="stufe-3-1"></span>

El tamaño más evidente de una flecha es su longitud. En el plano, la da el teorema de Pitágoras: la flecha $(3,\,-4)^{\top}$ es la hipotenusa de un triángulo rectángulo con los catetos $3$ y $4$, así que mide $\sqrt{3^2+4^2}=5$. En el espacio se aplica Pitágoras dos veces y se obtiene la raíz de la suma de los tres cuadrados. La misma fórmula se usa en cualquier dimensión.

:::definition Definición 3.1 (Norma euclídea)
<span class="anker" id="satz-3-1"></span>

La __norma euclídea__ de un vector $\mathbf{x}\in\mathbb{R}^d$ es

<span class="anker" id="gl-3-1"></span>
$$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}=\sqrt{x_1^2+x_2^2+\dots+x_d^2} . \tag{3.1}$$

Sin índice, $\lVert\mathbf{x}\rVert$ designa en esta serie siempre la norma euclídea.
:::

Se llama también la __longitud__ del vector o, por los cuadrados, la norma $L_2$. Un vector de longitud $1$ se llama __normalizado__. Si se divide un vector $\mathbf{x}\ne\mathbf{0}$ por su longitud, $\mathbf{x}/\lVert\mathbf{x}\rVert$ está normalizado y apunta en la misma dirección. Este paso se llama __normalizar__.

⁠**Ejemplo numérico:** El vector $\mathbf{x}=(3,\,-4)^{\top}$ tiene la longitud $\lVert\mathbf{x}\rVert_2=5$ (fig. [12](#abb-12)). Normalizado es $\mathbf{x}/5=(0{,}6;\ -0{,}8)^{\top}$. En el espacio, $\lVert(1,\,2,\,2)^{\top}\rVert=\sqrt{1+4+4}=3$.

:::abbildung ml/k1rl2 12
La norma euclídea de $(3,\,-4)^{\top}$: elevar las componentes al cuadrado, sumar, extraer la raíz. El signo menos desaparece al elevar al cuadrado.
:::

⁠**En resumen:** La norma euclídea es la longitud de la flecha, la raíz de la suma de los cuadrados de las componentes.

### La norma 1

<span class="anker" id="stufe-3-2"></span>

En una ciudad con una red de calles en cuadrícula, un taxi no puede cruzar las manzanas en diagonal. Para ir del origen al punto $(3,\,-4)^{\top}$, recorre $3$ manzanas en una dirección y $4$ manzanas en la otra, en total $7$ manzanas. Esta longitud la mide la norma 1.

:::definition Definición 3.2 (Norma 1)
<span class="anker" id="satz-3-2"></span>

La __norma 1__ de un vector $\mathbf{x}\in\mathbb{R}^d$ es

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{x}\rVert_1=|x_1|+|x_2|+\dots+|x_d|=\sum_{j=1}^d|x_j| . \tag{3.2}$$
:::

Se llama también norma $L_1$ o, por la red de calles de Manhattan, norma Manhattan.

⁠**Ejemplo numérico:** Para $\mathbf{x}=(3,\,-4)^{\top}$ se tiene $\lVert\mathbf{x}\rVert_1=7$ (fig. [13](#abb-13)), y $\lVert(1,\,2,\,2)^{\top}\rVert_1=1+2+2=5$.

:::abbildung ml/k1rl1 13
La norma 1 de $\mathbf{x}=(3,\,-4)^{\top}$: sumar los valores absolutos de las componentes.
:::

Aquí, la norma 1 es mayor que la longitud euclídea, porque el rodeo por las calles es más largo que la línea recta.

⁠**En resumen:** La norma 1 suma los valores absolutos de las componentes; es el camino a través de una red de calles en cuadrícula.

### La norma del máximo

<span class="anker" id="stufe-3-3"></span>

En un control de calidad, a menudo solo interesa la peor desviación. Una pieza tiene tres medidas, y cada una puede desviarse como máximo $0{,}1$ mm del valor nominal. Si la pieza es correcta lo decide únicamente la mayor de las tres desviaciones.

:::definition Definición 3.3 (Norma del máximo)
<span class="anker" id="satz-3-3"></span>

La __norma del máximo__ de un vector $\mathbf{x}\in\mathbb{R}^d$ es el mayor valor absoluto de una componente:

<span class="anker" id="gl-3-3"></span>
$$\lVert\mathbf{x}\rVert_\infty=\max_{j=1,\dots,d}|x_j| . \tag{3.3}$$
:::

Se llama también norma $L_\infty$. La razón del símbolo de infinito está en la siguiente subsección.

⁠**Ejemplo numérico:** $\lVert(3,\,-4)^{\top}\rVert_\infty=4$ y $\lVert(1,\,2,\,2)^{\top}\rVert_\infty=2$. Si las desviaciones de una pieza son $(0{,}05;\ -0{,}08;\ 0{,}02)$ mm, su norma del máximo es $0{,}08$ mm, y la pieza es correcta.

⁠**En resumen:** La norma del máximo es el mayor valor absoluto de una componente, la peor desviación individual.

### Qué caracteriza a una norma

<span class="anker" id="stufe-3-4"></span>

Las tres normas miden de forma distinta, pero tienen en común tres propiedades que se esperan de cualquier medida de tamaño. Solo el vector nulo tiene tamaño cero. Un vector el doble de largo es el doble de grande. Y un rodeo nunca es más corto que el camino directo.

:::definition Definición 3.4 (Norma)
<span class="anker" id="satz-3-4"></span>

Una __norma__ en $\mathbb{R}^d$ asigna a cada vector $\mathbf{x}$ un número real $\lVert\mathbf{x}\rVert$ de modo que, para todos los $\mathbf{u},\mathbf{v},\mathbf{x}\in\mathbb{R}^d$ y todos los escalares $c$, se cumple:

<ol>

<li>

$\lVert\mathbf{x}\rVert\ge0$, y $\lVert\mathbf{x}\rVert=0$ solo para $\mathbf{x}=\mathbf{0}$;

</li>

<li>

$\lVert c\,\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$;

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ (__desigualdad triangular__).

</li>

</ol>
:::

La desigualdad triangular debe su nombre a un triángulo formado por las flechas $\mathbf{u}$, $\mathbf{v}$ y $\mathbf{u}+\mathbf{v}$: el lado $\mathbf{u}+\mathbf{v}$ nunca es más largo que los otros dos juntos.

**Las normas $p$.** La norma 1 y la norma euclídea son dos casos de toda una familia. Para cada número $p\ge1$, la __norma $p$__ es

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{x}\rVert_p=\Bigl(\sum_{j=1}^d|x_j|^p\Bigr)^{1/p} . \tag{3.4}$$

Para $p=1$ es la norma 1; para $p=2$, la norma euclídea. Cuanto mayor es $p$, más predomina en la suma la componente más grande. Para $p\to\infty$ solo queda ella; por eso la norma del máximo se denota $\lVert\cdot\rVert_\infty$.

**La esfera unidad.** Cómo mide una norma se ve en el conjunto de todos los vectores de tamaño $1$. Se llama __esfera unidad__ de la norma, aunque no tiene por qué ser una esfera (fig. [14](#abb-14)). Para la norma euclídea es, en el plano, la circunferencia de radio $1$. Para la norma 1 es el rombo $|x_1|+|x_2|=1$: en cada cuadrante es un segmento, por ejemplo $x_1+x_2=1$ para $x_1,x_2\ge0$. Para la norma del máximo es el cuadrado de vértices $(\pm1,\,\pm1)$, pues en él el mayor de los valores absolutos de las dos componentes es exactamente $1$.

:::abbildung ml/k1einheitskugeln 14
Las esferas unidad de tres normas en el plano: el rombo de la norma 1 (izquierda, naranja), la circunferencia de la norma euclídea (centro, azul) y el cuadrado de la norma del máximo (derecha, verde); en gris, en cada caso, las otras dos para comparar. Las tres pasan por los puntos $(\pm1,\,0)$ y $(0,\,\pm1)$.
:::

⁠**Ejemplo numérico:** Para $\mathbf{x}=(3,\,-4)^{\top}$ se tiene $\lVert\mathbf{x}\rVert_1=7$, $\lVert\mathbf{x}\rVert_2=5$, $\lVert\mathbf{x}\rVert_3=91^{1/3}\approx4{,}498$, $\lVert\mathbf{x}\rVert_{10}=1\,107\,625^{1/10}\approx4{,}022$ (fig. [15](#abb-15)) y $\lVert\mathbf{x}\rVert_\infty=4$. A medida que crece $p$, la norma $p$ se acerca al mayor valor absoluto de una componente, aquí $4$. La razón ya está en la suma: para $p=10$, $4^{10}$ es casi dieciocho veces mayor que $3^{10}$, y la raíz de la suma apenas es mayor que la raíz de solo $4^{10}$.

:::abbildung ml/k1rlp 15
Dos normas $p$ de $\mathbf{x}=(3,\,-4)^{\top}$, para $p=3$ y $p=10$. Cuanto mayor es $p$, más predomina el sumando de la componente más grande.
:::

Que la norma 1 cumple las condiciones (N1) a (N3) se comprueba directamente: (N1) y (N2) se cumplen porque $|x_j|\ge0$ y $|c\,x_j|=|c|\,|x_j|$. (N3) se deduce de la desigualdad triangular para números, $|u_j+v_j|\le|u_j|+|v_j|$, sumada sobre todos los $j$. Para la norma del máximo se procede igual. Para la norma euclídea, la desigualdad triangular es intuitivamente clara, porque el camino directo entre dos puntos nunca es más largo que un rodeo por un tercer punto.

⁠**En resumen:** Una norma mide el tamaño de un vector de modo que solo el vector nulo tiene tamaño cero, los múltiplos crecen en la misma proporción y se cumple la desigualdad triangular; las normas $p$ forman una familia a la que pertenecen $L_1$, $L_2$ y $L_\infty$.

:::hintergrund Por qué tiene que ser $p\ge1$ y por qué la «norma cero» no es una norma
Para $p<1$, la fórmula [(3.4)](#gl-3-4) viola la desigualdad triangular. Con $p=\tfrac12$, $\lVert(1,0)^{\top}\rVert_{1/2}=1$ y $\lVert(0,1)^{\top}\rVert_{1/2}=1$, pero $\lVert(1,1)^{\top}\rVert_{1/2}=(1+1)^2=4>1+1$. Su «esfera unidad» está abollada hacia dentro: tiene forma de estrella.

A menudo se lee sobre una «norma $L_0$»: el número de componentes que no son cero. Es una medida útil de cuántas características utiliza realmente un vector. Aun así, no es una norma, pues viola (N2): el vector $2\mathbf{x}$ tiene tantas componentes distintas de cero como $\mathbf{x}$, no el doble.
:::

:::hintergrund No toda norma proviene de un producto escalar
La norma euclídea está construida a partir del producto escalar, $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$. De ello se deduce una igualdad que se llama ley del paralelogramo. Si se desarrolla con las reglas de cálculo del producto escalar, se tiene

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,\qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,$$

y la suma de ambas líneas da $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$: en un paralelogramo, la suma de los cuadrados de las dos diagonales es igual a la suma de los cuadrados de los cuatro lados. Toda norma que proviene de un producto escalar tiene que cumplir esta igualdad. La norma 1 no la cumple: con $\mathbf{u}=\mathbf{e}_1$ y $\mathbf{v}=\mathbf{e}_2$, a la izquierda queda $\lVert(1,1)^{\top}\rVert_1^2+\lVert(1,-1)^{\top}\rVert_1^2=4+4=8$, pero a la derecha $2+2=4$. No hay, por tanto, ningún producto escalar cuya longitud sea la norma 1. Por eso, con ella no se pueden medir ángulos como los que proporciona el producto escalar.
:::

### El vector de error y su tamaño

<span class="anker" id="stufe-3-5"></span>

Un modelo da predicciones, y en algún momento se conocen los valores reales. Entonces se quiere saber lo buenas que eran las predicciones. Para cada ejemplo hay una desviación, y estas desviaciones forman un vector. Su norma es una medida del tamaño del error en conjunto.

:::definition Definición 3.5 (Vector de error)
<span class="anker" id="satz-3-5"></span>

Si $\hat y_1,\dots,\hat y_N$ son las predicciones de un modelo para $N$ ejemplos e $y_1,\dots,y_N$ los valores reales, el vector

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{y}}-\mathbf{y}=(\hat y_1-y_1,\,\dots,\,\hat y_N-y_N)^{\top} \tag{3.5}$$

se llama __vector de error__. Aquí, $\hat{\mathbf{y}}=(\hat y_1,\dots,\hat y_N)^{\top}$ es el vector de las predicciones e $\mathbf{y}=(y_1,\dots,y_N)^{\top}$ el vector de los valores reales.
:::

Qué norma se aplica al vector de error es una decisión sobre qué errores se temen más. El signo no importa, pues toda norma da a $\mathbf{y}-\hat{\mathbf{y}}$ el mismo tamaño que a $\hat{\mathbf{y}}-\mathbf{y}$.

⁠**Ejemplo numérico:** Las cuatro viviendas se han vendido; los precios reales fueron $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$, en miles de euros. Dos tasadores, A y B, habían hecho antes una estimación:

$$\hat{\mathbf{y}}_{\mathrm A}=(210,\,120,\,300,\,230)^{\top},\qquad \hat{\mathbf{y}}_{\mathrm B}=(200,\,130,\,290,\,280)^{\top}.$$

Sus vectores de error son $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}=(10,\,-10,\,10,\,-10)^{\top}$ y $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}=(0,\,0,\,0,\,40)^{\top}$. El tasador A siempre se equivoca un poco; el tasador B acierta exactamente tres veces y una vez se equivoca mucho. Las tres normas juzgan de forma distinta (tabla [2](#tab-2)). Las normas euclídeas están calculadas en la fig. [16](#abb-16).

:::abbildung ml/k1rfehler 16
Las normas euclídeas de los dos vectores de error, en miles de euros. El único error grande de B contribuye a la suma de cuadrados con $1\,600$, cuatro veces más que los cuatro errores pequeños de A juntos.
:::

<span class="anker" id="tab-2"></span>

**Tabla 2:** Las normas de los vectores de error de dos tasadores, en miles de euros.

|  | $\lVert\cdot\rVert_1$ | $\lVert\cdot\rVert_2$ | $\lVert\cdot\rVert_\infty$ |
|---|---|---|---|
| Tasador A, $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}$ | $40$ | $\sqrt{4\cdot100}=20$ | $10$ |
| Tasador B, $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}$ | $40$ | $\sqrt{1600}=40$ | $40$ |

Según la norma 1, ambos son igual de buenos: los dos se equivocan en total en $40$ mil euros. Según la norma euclídea, A es dos veces mejor; según la norma del máximo, cuatro veces mejor. Quien considera igual de grave cada mil euros de desviación, sea cual sea la vivienda, mide con $L_1$. Quien considera un gran valor atípico peor que muchos errores pequeños, mide con $L_2$. Quien solo teme el peor caso, mide con $L_\infty$.

⁠**En resumen:** El vector de error reúne las desviaciones de todas las predicciones; su norma mide el tamaño del error, y la elección de la norma determina qué errores cuentan especialmente.

:::hintergrund Por qué la suma de cuadrados castiga los errores grandes y casi pasa por alto los pequeños
En la norma euclídea, cada desviación entra al cuadrado. Una desviación de $0{,}1$ aporta $0{,}01$, pero una desviación de $10$ aporta $100$. El cuadrado hace más pequeños los números pequeños y más grandes los grandes. Por eso, un único error grande de $40$ aporta $1600$, cuatro veces más que cuatro errores de $10$ cada uno juntos. La norma 1, en cambio, crece igual de rápido en todas partes: cada unidad de desviación cuesta lo mismo, pertenezca a un error pequeño o a uno grande. Por eso distingue también claramente entre «exactamente cero» y «un poco desviado», mientras que la suma de cuadrados apenas hace diferencia entre ambos. Qué propiedad se quiere depende de la tarea, y precisamente por eso hay varias normas.
:::

### El valor eficaz

<span class="anker" id="stufe-3-6"></span>

La norma euclídea crece con el número de componentes. Si se evalúa a un tasador con cuatro viviendas y a otro con cuatrocientas, el segundo tiene un vector de error mucho más largo, aunque estime igual de bien en cada vivienda. Si se quieren comparar los errores por cada ejemplo, hay que descontar el número de componentes.

:::definition Definición 3.6 (Valor eficaz)
<span class="anker" id="satz-3-6"></span>

El __valor eficaz__ de un vector $\mathbf{x}\in\mathbb{R}^n$ es

<span class="anker" id="gl-3-6"></span>
$$\operatorname{rms}(\mathbf{x})=\frac{\lVert\mathbf{x}\rVert}{\sqrt n}=\sqrt{\frac1n\sum_{i=1}^nx_i^2} . \tag{3.6}$$
:::

La abreviatura rms significa *root mean square*: la raíz de la media de los cuadrados. El valor eficaz es un valor absoluto típico de una componente. Si todas las componentes tienen el mismo valor absoluto $a$, el valor eficaz es exactamente $a$.

El nombre se conoce de la electrotecnia: el valor eficaz de una tensión alterna es la raíz de la media temporal de su cuadrado. Para una señal muestreada, [(3.6)](#gl-3-6) es el mismo cálculo con muestras en lugar de una integral. Si se muestrea un seno a lo largo de exactamente un periodo en $n\ge3$ puntos equiespaciados, se obtiene incluso exactamente el valor eficaz $1/\sqrt2$ del seno.

⁠**Ejemplo numérico:** Los vectores de error de los tasadores de la subsección anterior tienen los valores eficaces $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y})=20/\sqrt4=10$ y $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y})=40/\sqrt4=20$ mil euros: A se equivoca típicamente en $10$ mil euros. Un seno de amplitud $1$, muestreado en cuatro puntos equiespaciados de un periodo, tiene las muestras $\mathbf{x}=(0,\,1,\,0,\,-1)^{\top}$ y el valor eficaz $1/\sqrt2\approx0{,}707$ (fig. [17](#abb-17)).

:::abbildung ml/k1rrms 17
El valor eficaz de un seno muestreado: sumar los cuadrados, dividir por el número de componentes, extraer la raíz.
:::

⁠**En resumen:** El valor eficaz $\lVert\mathbf{x}\rVert/\sqrt n$ es el valor absoluto típico de una componente y hace comparables vectores de distinta longitud.

:::hintergrund ¿Cuántas componentes pueden ser grandes?
El valor eficaz limita cuántas componentes pueden tener un valor absoluto grande. Si $k$ de las $n$ componentes tienen un valor absoluto de al menos $a>0$, solo estas $k$ componentes aportan ya al menos $k\,a^2$ a la suma de cuadrados. La suma de cuadrados completa es $n\operatorname{rms}(\mathbf{x})^2$, así que $k\,a^2\le n\operatorname{rms}(\mathbf{x})^2$, o bien

$$\frac kn\le\Bigl(\frac{\operatorname{rms}(\mathbf{x})}{a}\Bigr)^2 .$$

Como mucho la fracción $(\operatorname{rms}/a)^2$ de las componentes puede tener, por tanto, un valor absoluto de al menos $a$. Como mucho una cuarta parte de las componentes puede alcanzar el doble del valor eficaz, y como mucho un uno por ciento, diez veces el valor eficaz. En el tasador B, con $\operatorname{rms}=20$, como mucho un $(20/30)^2=4/9\approx44$ % de los errores puede ser de $30$ o más; en realidad es uno de cuatro, es decir, el $25$ %. Esta acotación se llama desigualdad de Chebyshov.
:::

:::aufgabe Ejercicio 7 ★ Calcular normas
<span class="anker" id="aufg-7"></span>

Sea $\mathbf{x}=(2,\,-1,\,0,\,2)^{\top}$.

<ol class="al">

<li>

Calcula $\lVert\mathbf{x}\rVert_1$, $\lVert\mathbf{x}\rVert_2$, $\lVert\mathbf{x}\rVert_3$ y $\lVert\mathbf{x}\rVert_\infty$, así como el vector normalizado $\mathbf{x}/\lVert\mathbf{x}\rVert$.

</li>

<li>

Comprueba $\lVert\mathbf{x}\rVert_\infty\le\lVert\mathbf{x}\rVert_2\le\lVert\mathbf{x}\rVert_1$. Justifica por qué este orden se cumple para todo vector.

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}\rVert_1=2+1+0+2=5$, $\lVert\mathbf{x}\rVert_2=\sqrt{4+1+0+4}=3$, $\lVert\mathbf{x}\rVert_3=(8+1+0+8)^{1/3}=17^{1/3}\approx2{,}571$ y $\lVert\mathbf{x}\rVert_\infty=2$. El vector normalizado es $\mathbf{x}/3=(\tfrac23,\,-\tfrac13,\,0,\,\tfrac23)^{\top}$, con la longitud $\sqrt{(4+1+4)/9}=1$.

(b) Se tiene $2\le3\le5$, y también $\lVert\mathbf{x}\rVert_3$, con $2{,}571$, queda entre ambas. En general: si $|x_k|$ es el mayor de los valores absolutos de las componentes, entonces $\lVert\mathbf{x}\rVert_\infty^2=x_k^2\le\sum_jx_j^2=\lVert\mathbf{x}\rVert_2^2$, pues la suma contiene $x_k^2$ y, por lo demás, solo sumandos no negativos. Y $\lVert\mathbf{x}\rVert_1^2=\bigl(\sum_j|x_j|\bigr)^2=\sum_jx_j^2+\sum_{j\ne l}|x_j|\,|x_l|\ge\lVert\mathbf{x}\rVert_2^2$, porque los productos cruzados no son negativos. Intuitivamente: la línea recta nunca es más larga que el camino por la red de calles ni más corta que el tramo individual más largo.
:::
:::

:::aufgabe Ejercicio 8 ★★ ¿Qué tal estima la agente inmobiliaria?
<span class="anker" id="aufg-8"></span>

La agente inmobiliaria de la subsección [2.2](das-skalarprodukt.html#stufe-2-2) hizo las predicciones $\hat{\mathbf{y}}=(188,\,126,\,286,\,232)^{\top}$; los precios reales fueron $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$, en miles de euros.

<ol class="al">

<li>

Calcula el vector de error, sus tres normas y su valor eficaz. ¿En qué vivienda se equivoca más?

</li>

<li>

¿Qué llama la atención en los signos? A partir de ahora, la agente inmobiliaria suma $7$ mil euros a cada predicción. Calcula el nuevo vector de error y sus normas. ¿Ha mejorado según las tres normas?

</li>

</ol>

:::loesung
(a) El vector de error es $\hat{\mathbf{y}}-\mathbf{y}=(188-200,\ 126-130,\ 286-290,\ 232-240)^{\top}=(-12,\,-4,\,-4,\,-8)^{\top}$. Sus normas: $\lVert\cdot\rVert_1=28$, $\lVert\cdot\rVert_2=\sqrt{144+16+16+64}=\sqrt{240}\approx15{,}49$, $\lVert\cdot\rVert_\infty=12$; valor eficaz, $\sqrt{240}/2\approx7{,}75$ mil euros. Donde más se equivoca es en la vivienda 1, en $12$ mil euros.

(b) Todos los errores son negativos: las estimaciones de la agente inmobiliaria son sistemáticamente demasiado bajas, y su error tiene una componente continua. Con un suplemento de $7$ mil euros, el vector de error pasa a ser $(-5,\,3,\,3,\,-1)^{\top}$, con $\lVert\cdot\rVert_1=12$, $\lVert\cdot\rVert_2=\sqrt{25+9+9+1}=\sqrt{44}\approx6{,}63$, $\lVert\cdot\rVert_\infty=5$ y el valor eficaz $\sqrt{44}/2\approx3{,}32$. Ha mejorado según las tres normas. El suplemento $7$ es exactamente la media de los valores absolutos de los errores, $(12+4+4+8)/4=7$: resta la componente continua del error y deja solo la componente alterna.
:::
:::
