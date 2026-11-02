---
title: Etapa 5: El análisis por nudos
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1180700
summary: La ley de las mallas ya está resuelta; quedan k-1 leyes de los nudos con k-1 incógnitas.
tags: conductancia de acoplamiento
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
La ley de las mallas ya está resuelta; quedan $k-1$ leyes de los nudos con $k-1$ incógnitas. Esta etapa las plantea y resuelve la misma red por segunda vez.
:::

**La idea.** La corriente que sale por una conductancia $G$ del nudo $\mu$ al vecino $\nu$ es $G\,(U_\mu-U_\nu)$. Si se suman todas las corrientes salientes de un nudo y se ordena por potenciales, delante del potencial propio queda la suma de todas las conductancias del nudo. Delante de un potencial ajeno queda solo la conductancia hacia el nudo propio, con signo menos: si se eleva el vecino, sale menos. La fig. [5](#abb-5) lo muestra como experimento.

:::definition Definición 5.1 (Análisis por nudos)
<span class="anker" id="satz-5-1"></span>

El método tiene cuatro pasos:

<ol>

<li>

Convertir las fuentes de tensión reales en fuentes de corriente reales: $I_\mathrm q=U_\mathrm q/R$, la misma resistencia en paralelo ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

</li>

<li>

Fijar un nudo de referencia y anotar los potenciales de los demás nudos como tensiones respecto a él. Escribir las resistencias como conductancias.

</li>

<li>

Plantear la ley de los nudos para los $k-1$ nudos restantes o leer directamente la matriz.

</li>

<li>

Resolver el sistema para los potenciales de nudo y calcular a partir de ellos las tensiones y las corrientes de rama.

</li>

</ol>
:::

:::satz Teorema 5.2 (Forma matricial del análisis por nudos)
<span class="anker" id="satz-5-2"></span>

Con $n=k-1$, los potenciales de nudo cumplen $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$:

<span class="anker" id="gl-5-1"></span>
$$\begin{pmatrix}Y_{11}&Y_{12}&\dots&Y_{1n}\\Y_{21}&Y_{22}&\dots&Y_{2n}\\\vdots&\vdots&\ddots&\vdots\\Y_{n1}&Y_{n2}&\dots&Y_{nn}\end{pmatrix} \begin{pmatrix}U_1\\U_2\\\vdots\\U_n\end{pmatrix}= \begin{pmatrix}I_\mathrm{q1}\\I_\mathrm{q2}\\\vdots\\I_{\mathrm qn}\end{pmatrix}. \tag{5.1}$$

<ul>

<li>

$Y_{\mu\mu}$ es la suma de todas las conductancias conectadas al nudo $\mu$.

</li>

<li>

$Y_{\mu\nu}=Y_{\nu\mu}$ es la __conductancia de acoplamiento__ negativa, es decir, menos la suma de las conductancias situadas directamente entre los nudos $\mu$ y $\nu$. Sin conexión directa, ahí hay cero.

</li>

<li>

$I_{\mathrm q\mu}$ es la suma de las corrientes de fuente en el nudo, positiva si entran en el nudo.

</li>

</ul>
:::

:::herleitung De la ley de los nudos a la matriz
En el nudo $\mu$ sale por cada conductancia $G_a$ hacia el vecino $\nu$ la corriente $G_a\,(U_\mu-U_\nu)$, y hacia el nudo de referencia $G_a\,U_\mu$. La suma de estas corrientes es igual a la $I_{\mathrm q\mu}$ inyectada. Al ordenar queda delante de $U_\mu$ la suma de todos los $G_a$ y delante de $U_\nu$ menos la suma de las conductancias entre $\mu$ y $\nu$. El nudo $\nu$ recibe el mismo elemento, porque una conductancia no conoce dirección. Por eso $\mathbf Y$ es simétrica.
:::

⁠**Cómo leerlo:** La fila $\mu$ es la ley de los nudos: a la izquierda están todas las corrientes que salen por conductancias, a la derecha lo que las fuentes empujan hacia dentro. La columna $\nu$ dice: si se mantiene el nudo $\nu$ a 1 V y todos los demás a 0 V, hay que inyectar en el nudo $\nu$ la corriente $Y_{\nu\nu}$ y extraer en cada vecino $\mu$ la corriente $-Y_{\mu\nu}$. Eso es exactamente el ensayo de cortocircuito de la [Parte 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). **Validez:** La red contiene conductancias y fuentes de corriente fijas. Una fuente de tensión ideal no encaja, porque no tiene conductancia finita (etapa [9](die-modifizierte-knotenanalyse.html#stufe-9)).

:::abbildung et1/k8yspalte 5
Izquierda: la red modelo para el análisis por nudos; la batería se ha convertido en fuente de corriente. Derecha: se han quitado las fuentes, el nudo 1 está a 1 V y el nudo 2 a 0 V. Por $G_1$, $G_2$, $G_3$ salen $1+0{,}25+0{,}5=1{,}75$ mA, que es $Y_{11}$. Los 0,5 mA llegan al nudo 2 y hay que extraerlos allí, que es $Y_{21}=-0{,}5$ mS.
:::

**Ejemplo.** A la izquierda, $I_\mathrm{q1}=U_\mathrm q/R_1=9$ mA con $G_1=1$ mS en paralelo. Las conductancias son $G_2=0{,}25$ mS, $G_3=0{,}5$ mS, $G_4=0{,}1$ mS y $G_5=0{,}2$ mS (fig. [5](#abb-5)). Las leyes de los nudos son

$$\begin{aligned} \text{Nudo 1:}\quad&(G_1+G_2)\,U_1+G_3\,(U_1-U_2)-I_\mathrm{q1}=0,\\ \text{Nudo 2:}\quad&G_3\,(U_2-U_1)+(G_4+G_5)\,U_2-I_\mathrm q=0. \end{aligned}$$

Ordenado, en mS, V y mA:

$$\begin{pmatrix}G_1+G_2+G_3&-G_3\\-G_3&G_3+G_4+G_5\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}= \begin{pmatrix}1{,}75&-0{,}5\\-0{,}5&0{,}8\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}9\\4\end{pmatrix}.$$

Con $D=1{,}4-0{,}25=1{,}15$, $D_1=7{,}2+2=9{,}2$ y $D_2=7+4{,}5=11{,}5$ resultan $U_1=8$ V y $U_2=10$ V. Es el mismo resultado que con las tres mallas, con un cálculo de $2\times2$ en lugar de $3\times3$.

Las corrientes salen de las diferencias, y además en la red *original*: $(U_\mathrm q-U_1)/R_1=1$ mA, $U_1/R_2=2$ mA, $(U_2-U_1)/R_3=1$ mA, $U_2/R_4=1$ mA, $U_2/R_5=2$ mA. **Comprobaciones:** En el nudo 2, $4=1+1+2$ mA. Las fuentes entregan $9\,\mathrm{V}\cdot1\,\mathrm{mA}+10\,\mathrm{V}\cdot4\,\mathrm{mA}=49$ mW, las resistencias absorben $1+16+2+10+20=49$ mW. **Caso límite:** Para $G_3\to0$ desaparecen los elementos fuera de la diagonal, y ambos lados se calculan por separado (ejercicio [7](#aufg-7)).

:::frage En $\mathbf Z$ el signo depende de las flechas. ¿Por qué en $\mathbf Y$ siempre hay un menos?
Las corrientes de malla tienen un sentido que se elige, y por tanto también dos posibilidades en la rama común. Los potenciales de nudo no tienen sentido; todos se cuentan respecto al mismo nudo de referencia. En la conductancia entre dos nudos está por eso siempre la diferencia, y el potencial ajeno lleva siempre un menos.
:::

:::frage Tras la conversión, por $R_5$ circulan en el esquema de mallas 2 mA hacia arriba y en la red original 2 mA hacia abajo. ¿Qué es lo correcto?
La red original. Las fuentes equivalentes solo coinciden en los terminales ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). En el nudo 2 y en la masa ambas formas dan lo mismo; en el interior de la fuente la corriente significa cosas distintas. Por eso las magnitudes internas se calculan en la red original a partir de las tensiones en los terminales.
:::

:::aufgabe Ejercicio 6 ★★ Tres nudos y una referencia
<span class="anker" id="aufg-6"></span>

Una red tiene los nudos 0 (referencia), 1, 2, 3. Resistencias: 1 k$\Omega$ de 1 a 0, 1 k$\Omega$ de 1 a 2, 500 $\Omega$ de 2 a 0, 1 k$\Omega$ de 2 a 3, 1 k$\Omega$ de 3 a 0. Unas fuentes de corriente inyectan 6 mA en el nudo 1 y 3 mA en el nudo 2.

<ol class="al">

<li>

Lee $\mathbf Y$ e $\mathbf I_\mathrm q$. ¿Por qué $Y_{13}=0$?

</li>

<li>

Calcula los potenciales de nudo con la regla de Cramer.

</li>

<li>

Calcula todas las corrientes de las resistencias y comprueba el nudo 2.

</li>

<li>

¿Cuántas corrientes de malla hacen falta tras convertir las dos fuentes? ¿Qué método sería aquí más corto?

</li>

</ol>

:::loesung
(a) Con 1 mS, 1 mS, 2 mS, 1 mS, 1 mS:

$$\mathbf Y=\begin{pmatrix}2&-1&0\\-1&4&-1\\0&-1&2\end{pmatrix}\mathrm{mS},\qquad\mathbf I_\mathrm q=\begin{pmatrix}6\\3\\0\end{pmatrix}\mathrm{mA}.$$

$Y_{13}=0$, porque entre 1 y 3 no hay ninguna resistencia.

(b) $D=2\cdot7+1\cdot(-2)=12$, $D_1=48$, $D_2=24$, $D_3=12$. Por tanto, $U_1=4$ V, $U_2=2$ V, $U_3=1$ V.

(c) $I_{10}=4$ mA, $I_{12}=2$ mA, $I_{20}=4$ mA, $I_{23}=1$ mA, $I_{30}=1$ mA. Nudo 2: $3+2=4+1$ mA.

(d) Cada fuente de corriente forma con su resistencia en paralelo una rama. Entonces $z=5$ y $k=4$, es decir, $m=2$ frente a $k-1=3$. El análisis por mallas sería más corto, con dos ecuaciones. El nudo 3 no es en realidad un nudo, sino una conexión en serie.
:::
:::

:::aufgabe Ejercicio 7 ★★ Casos límite de la conductancia de acoplamiento
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Se elimina $R_3$ de la red modelo ($G_3=0$). ¿En qué se convierte $\mathbf Y$? Calcula $U_1$ y $U_2$.

</li>

<li>

Predicción: $R_3$ se sustituye por un hilo. ¿Por qué eso no funciona directamente en $\mathbf Y$? Une los nudos y determina la tensión común y la corriente en el hilo.

</li>

</ol>

:::loesung
(a) Los elementos fuera de la diagonal se anulan y las ecuaciones se desacoplan: $U_1=9\,\mathrm{mA}/1{,}25\,\mathrm{mS}=7{,}2$ V y $U_2=4\,\mathrm{mA}/0{,}3\,\mathrm{mS}=13{,}3$ V. Son dos redes separadas.

(b) $G_3\to\infty$ no se puede escribir como número. El hilo convierte ambos nudos en uno: $U=(9+4)\,\mathrm{mA}/(1+0{,}25+0{,}1+0{,}2)\,\mathrm{mS}=8{,}39$ V. La corriente en el hilo se obtiene del nudo 2: $4\,\mathrm{mA}-0{,}3\,\mathrm{mS}\cdot8{,}39\,\mathrm{V}=1{,}48$ mA de 2 a 1. La etapa [9](die-modifizierte-knotenanalyse.html#stufe-9) resuelve la misma situación con una fuente de 0 V.
:::
:::
