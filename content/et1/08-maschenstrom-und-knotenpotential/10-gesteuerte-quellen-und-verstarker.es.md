---
title: Etapa 8: Fuentes controladas y amplificadores
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Análisis por mallas y por nudos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Capítulo 8: Análisis por mallas y por nudos
order: 1181000
summary: Los amplificadores contienen fuentes controladas (capítulo 6).
tags: fuente de corriente controlada por tensión, transconductancia, ganancia de tensión, realimentación negativa, transimpedancia
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Los amplificadores contienen fuentes controladas ([capítulo 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Esta etapa les da una estampa y muestra qué significa eso para la matriz.
:::

**La idea.** Una __fuente de corriente controlada por tensión__ ([capítulo 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) es una conductancia generalizada. En una conductancia, su propia tensión $U_{ik}$ controla la corriente de $i$ a $k$. En la fuente la controla una tensión ajena $U_{pq}$. Las filas se mantienen, porque la corriente sale y entra por los mismos nudos. Las columnas pasan de $i$, $k$ a $p$, $q$, porque cuentan los potenciales que controlan. La simetría se pierde en el proceso. Eso es física: la entrada actúa sobre la salida, pero no al revés.

:::satz Teorema 8.1 (Estampa de la fuente de corriente controlada por tensión)
<span class="anker" id="satz-8-1"></span>

Una fuente con $I=g\,(U_p-U_q)$ de $i$ a $k$ suma $+g$ en $(i,p)$ y $(k,q)$ y $-g$ en $(i,q)$ y $(k,p)$.
:::

⁠**Cómo leerlo:** $g$ es la __transconductancia__, corriente por tensión de control en siemens, 50 mS en el modelo. **Validez:** La fuente debe ser lineal. Los transistores solo lo son para pequeños cambios en torno a un punto de trabajo ([capítulo 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).

::::beispiel sin realimentación negativa
Una fuente de corriente $I_\mathrm q=20$ µ A con $G_\mathrm q=0{,}5$ mS alimenta el nudo 1. Allí está $G_\mathrm i=0{,}5$ mS a masa. La fuente $g\,U_1$ extrae corriente del nudo 2 hacia masa; allí están también $G_\mathrm o=0{,}05$ mS y $G_\mathrm L=0{,}2$ mS. Las estampas dan

<span class="anker" id="gl-8-1"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0\\g&G_\mathrm o+G_\mathrm L\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\end{pmatrix}. \tag{8.1}$$

$Y_{12}=0$, pero $Y_{21}=g$. Con $D=(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)$, $D_1=(G_\mathrm o+G_\mathrm L)\,I_\mathrm q$ y $D_2=-g\,I_\mathrm q$ resulta

<span class="anker" id="gl-8-2"></span>
$$U_1=\frac{I_\mathrm q}{G_\mathrm q+G_\mathrm i},\qquad U_2=-\frac{g\,I_\mathrm q}{(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)},\qquad A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}. \tag{8.2}$$

En el modelo son $D=0{,}25$, $U_1=20$ mV, $U_2=-4$ V y la __ganancia de tensión__ $A_u=-200$, como en el [capítulo 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). El signo menos surge porque la corriente controlada sale del nudo 2.
::::

**Con realimentación negativa.** El punto inferior común de la entrada y la salida se llama punto base. Si se separa de la masa y se intercala ahí $R_\mathrm S=1\,\mathrm{k\Omega}$, surge el nudo 3 (fig. [8](#abb-8)). La corriente de salida pasa ahora por $R_\mathrm S$ y eleva $U_3$. Con ello baja la tensión de control $U_1-U_3$, y la corriente de salida disminuye. Esta acción de la salida sobre su propia entrada se llama __realimentación negativa__.

:::abbildung et1/k8verstaerker 8
Amplificador con realimentación negativa. La fuente $g\,(U_1-U_3)$ va del nudo 2 al nudo 3; $G_\mathrm i$ y $G_\mathrm o$ terminan en el nudo 3. El camino rojo muestra la corriente de salida: eleva el nudo 3 y así reduce la tensión de control. Para $G_\mathrm S\to\infty$, el nudo 3 cae a masa.
:::

Las estampas de $G_\mathrm q$, $G_\mathrm i$, $G_\mathrm S$, $G_\mathrm o$, $G_\mathrm L$ y $g\,(U_1-U_3)$ de 2 a 3 dan

<span class="anker" id="gl-8-3"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0&-G_\mathrm i\\g&G_\mathrm o+G_\mathrm L&-g-G_\mathrm o\\-g-G_\mathrm i&-G_\mathrm o&G_\mathrm S+g+G_\mathrm i+G_\mathrm o\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\\0\end{pmatrix}. \tag{8.3}$$

:::herleitung Los determinantes
Con $A=G_\mathrm q+G_\mathrm i$ y $B=G_\mathrm o+G_\mathrm L$, el desarrollo por la primera fila da

$$\begin{aligned} D&=A\,[B\,(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]-G_\mathrm i\,[B\,G_\mathrm i+G_\mathrm L\,g]\\ &=B\,[A\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[A\,G_\mathrm o+G_\mathrm q\,g]. \end{aligned}$$

$D_2$ se desarrolla por la columna 2, en la que solo está $I_\mathrm q$: $D_2=-I_\mathrm q\,[g\,(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)(g+G_\mathrm i)]=(G_\mathrm iG_\mathrm o-g\,G_\mathrm S)\,I_\mathrm q$.
:::

Con ello, la __transimpedancia__, la tensión de salida por corriente de entrada, es

<span class="anker" id="gl-8-4"></span>
$$\frac{U_2}{I_\mathrm q}=\frac{G_\mathrm iG_\mathrm o-g\,G_\mathrm S}{(G_\mathrm o+G_\mathrm L)\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm o+G_\mathrm q\,g]}. \tag{8.4}$$

En el modelo con $G_\mathrm S=1$ mS son $D=5{,}3225$ y $D_2/I_\mathrm q=-49{,}975$, es decir, $U_2/I_\mathrm q=-9{,}39\,\mathrm{k\Omega}$. De 20 µ A resultan $U_1=39{,}0$ mV, $U_2=-188$ mV y $A_u=-4{,}81$. **Caso límite:** Para $G_\mathrm S\to\infty$ solo quedan los términos con $G_\mathrm S$, y [(8.4)](#gl-8-4) pasa a $-g/[(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)]=-200\,\mathrm{k\Omega}$, el resultado de [(8.2)](#gl-8-2). El punto base vuelve entonces a estar en masa.

:::ltspice Amplificador con realimentación negativa
⁠**Esquema:** `current` con `20u` de masa a `1`, `Rq 2k` de `1` a masa, `Ri 2k` de `1` a `3`, `RS 1k` de `3` a masa. La fuente de corriente controlada `g` con `50m`: salida de `2` a `3`, entrada de control de `1` a `3`. `Ro 20k` de `2` a `3`, `RL 5k` de `2` a masa.

⁠**Directivas:** `.op`, `.meas op u1 FIND V(1)`, `.meas op u2 FIND V(2)`, `.meas op au PARAM u2/u1`.

⁠**Lo que ves:** $\mathtt{u1}=39{,}0$ mV, $\mathtt{u2}=-188$ mV, $\mathtt{au}=-4{,}81$. Pon `RS` a `1u`: entonces $\mathtt{u2}=-4$ V y $\mathtt{au}=-200$. Comprueba con `V(3)` tu resultado del ejercicio [10](#aufg-10).
:::

:::frage ¿Por qué se reduce voluntariamente la ganancia?
Porque entonces apenas depende de la transconductancia, y $g$ varía mucho en los transistores. Si en el modelo se duplica $g$, $A_u$ pasa de $-4{,}81$ solo a $-4{,}90$. Sin $R_\mathrm S$, en cambio, $-200$ se convertiría en $-400$. El resultado queda cerca de $-R_\mathrm L/R_\mathrm S=-5$, es decir, lo fijan dos resistencias precisas. El [capítulo 11](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html) lo aprovecha en el amplificador operacional.
:::

:::aufgabe Ejercicio 10 ★★★ La resistencia de entrada aumenta
<span class="anker" id="aufg-10"></span>

Considera el amplificador de la fig. [8](#abb-8) con $G_\mathrm S=1$ mS.

<ol class="al">

<li>

Demuestra $D_1=[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]\,I_\mathrm q$ y calcula $U_1/I_\mathrm q$.

</li>

<li>

La conductancia de entrada sin $G_\mathrm q$ es $Y_\mathrm{ent}=I_\mathrm q/U_1-G_\mathrm q$. ¿Cuánto vale la resistencia de entrada $1/Y_\mathrm{ent}$? Compara con 2 k$\Omega$ sin $R_\mathrm S$.

</li>

<li>

Explica el mecanismo: ¿Cuánto vale $U_3$, y qué corriente pasa entonces aún por $G_\mathrm i$?

</li>

</ol>

:::loesung
(a) Si se sustituye la columna 1 por $(I_\mathrm q,0,0)$, queda $D_1=I_\mathrm q\,[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)\,G_\mathrm o]$. Desarrollado, el corchete es el indicado. Números: $0{,}25\cdot1{,}5+0{,}2\cdot50{,}05=10{,}385$. Con $D=5{,}3225$ resulta $U_1/I_\mathrm q=1{,}95\,\mathrm{k\Omega}$.

(b) $Y_\mathrm{ent}=1/(1{,}951\,\mathrm{k\Omega})-0{,}5\,\mathrm{mS}=0{,}0125$ mS, es decir, $R_\mathrm{ent}=79{,}9\,\mathrm{k\Omega}$, cuarenta veces más.

(c) $U_3=38{,}05$ mV está solo 0,98 mV por debajo de $U_1=39{,}02$ mV. El potencial del otro extremo de $R_\mathrm i$ casi lo sigue. Por eso en $R_\mathrm i$ hay algo menos de 1 mV, y en lugar de 10 µ A circulan 0,49 µ A. Poca corriente con la misma tensión significa una resistencia de entrada grande.
:::
:::
