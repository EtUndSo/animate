---
title: Etapa 7: Estampas y lista de conexiones
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Análisis por mallas y por nudos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Capítulo 8: Análisis por mallas y por nudos
order: 1180900
summary: Un programa no ve mallas y no despeja nada.
tags: estampa, lista de conexiones, dispersa
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Un programa no ve mallas y no despeja nada. Esta etapa muestra cómo surge la matriz componente a componente, sin que ningún componente tenga que conocer a los demás.
:::

**La idea.** Un componente solo toca sus dos nudos. Por eso su corriente aparece exactamente en dos ecuaciones de nudo, en una con más, en la otra con menos. Así, cada componente tiene un patrón fijo de elementos, su __estampa__ (fig. [7](#abb-7)). Se empieza con una matriz llena de ceros y se suma componente a componente su estampa. El orden es indiferente.

:::abbildung et1/k8stempel 7
Patrones de elementos en las filas y columnas de los nudos. Izquierda: conductancia $G$ entre $i$ y $k$. Centro: fuente de corriente fija que empuja $I_\mathrm q$ de $k$ a $i$; solo escribe en el lado derecho. Derecha: fuente de corriente controlada por tensión $g\,U_{pq}$ de $i$ a $k$. Está en las filas $i$, $k$, pero en las columnas $p$, $q$ (etapa [8](gesteuerte-quellen-und-verstarker.html#stufe-8)).
:::

:::satz Teorema 7.1 (Estampas de conductancia y fuente de corriente)
<span class="anker" id="satz-7-1"></span>

Cada fila es la ley de los nudos «corrientes salientes = corrientes impuestas».

<ul>

<li>

Una conductancia $G$ entre $i$ y $k$ lleva la corriente $I_Y=G\,(U_i-U_k)$ de $i$ a $k$. Suma $+G$ en las posiciones $(i,i)$ y $(k,k)$ y $-G$ en $(i,k)$ y $(k,i)$.

</li>

<li>

Una fuente de corriente fija que empuja $I_\mathrm q$ a través de sí de $k$ a $i$ suma $+I_\mathrm q$ en la fila $i$ y $-I_\mathrm q$ en la fila $k$ del lado derecho. En $\mathbf Y$ no escribe nada, porque su corriente no depende de ninguna tensión.

</li>

</ul>
:::

⁠**Cómo leerlo:** Primero, cada uno de los $k$ nudos recibe una fila y una columna, también el nudo de referencia. Esta matriz completa tiene determinante cero, porque todas las filas suman cero: si se elevan todos los potenciales a la vez, no circula corriente adicional en ningún sitio. Físicamente, una red solo determina diferencias. Solo al fijar $U_0=0$ la solución se vuelve única: se tacha la columna 0, porque su incógnita es cero, y la fila 0, porque se deduce de las demás leyes de los nudos ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Lo que queda es la $\mathbf Y$ de la etapa [5](das-knotenpotentialverfahren.html#stufe-5). **Validez:** Las estampas valen para componentes lineales. Las fuentes de tensión siguen en la etapa [9](die-modifizierte-knotenanalyse.html#stufe-9).

**Lista de conexiones.** Un esquema se guarda como __lista de conexiones__: una línea por componente con nombre, nudos y valor. En SPICE, `R3 1 2 2k` significa: resistencia entre los nudos 1 y 2. `I2 0 2 4m` significa: 4 mA a través de la fuente del nudo 0 al nudo 2. El programa recorre la lista línea por línea y estampa. Si aparece un nombre de nudo nuevo, la matriz crece en una fila y una columna. Nadie tiene que conocer su tamaño de antemano. El formato rígido procede de la década de 1970, cuando SPICE estaba escrito en FORTRAN y cada línea ocupaba una tarjeta perforada.

::::beispiel
La red modelo con la batería convertida da esta lista:

| Línea | Valor | Elemento |
|---|---|---|
| `R1 1 0 1k` | $G_1=1$ | $+1$ en $(1,1)$, $(0,0)$; $-1$ en $(1,0)$, $(0,1)$ |
| `R2 1 0 4k` | $G_2=0{,}25$ | $+0{,}25$ en $(1,1)$, $(0,0)$; $-0{,}25$ en $(1,0)$, $(0,1)$ |
| `R3 1 2 2k` | $G_3=0{,}5$ | $+0{,}5$ en $(1,1)$, $(2,2)$; $-0{,}5$ en $(1,2)$, $(2,1)$ |
| `R4 2 0 10k` | $G_4=0{,}1$ | $+0{,}1$ en $(2,2)$, $(0,0)$; $-0{,}1$ en $(2,0)$, $(0,2)$ |
| `R5 2 0 5k` | $G_5=0{,}2$ | $+0{,}2$ en $(2,2)$, $(0,0)$; $-0{,}2$ en $(2,0)$, $(0,2)$ |
| `I1 0 1 9m` | $I=9$ | a la derecha $+9$ en la fila 1, $-9$ en la fila 0 |
| `I2 0 2 4m` | $I=4$ | a la derecha $+4$ en la fila 2, $-4$ en la fila 0 |

Con las filas y columnas en el orden 0, 1, 2 resulta

$$\begin{pmatrix}1{,}55&-1{,}25&-0{,}3\\-1{,}25&1{,}75&-0{,}5\\-0{,}3&-0{,}5&0{,}8\end{pmatrix} \begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-13\\9\\4\end{pmatrix}.$$

Cada fila suma cero. Si se tachan la fila y la columna 0, queda el sistema de la etapa [5](das-knotenpotentialverfahren.html#stufe-5). **Comprobación:** En la $\mathbf Y$ reducida, la suma de una fila es la conductancia a masa: $1{,}75-0{,}5=1{,}25=G_1+G_2$ y $0{,}8-0{,}5=0{,}3=G_4+G_5$.
::::

⁠**Caso límite:** Un nudo sin rama a masa tiene suma de fila cero.

**Redes grandes.** Un nudo suele estar unido solo a entre dos y cinco vecinos; por eso casi todas las posiciones de una matriz grande son cero. Se llama __dispersa__. El simulador guarda solo los elementos distintos de cero y resuelve el sistema por eliminación paso a paso. La regla de Cramer sería inútil para ello: un determinante de 20 filas tiene, según el patrón de [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1), unos $2{,}4\cdot10^{18}$ productos.

:::zusatz Corriente alterna, condensador, diodo
Con magnitudes sinusoidales se calcula con conductancias complejas, las admitancias. De ahí vienen las letras $Y$ y $Z$. Un condensador tiene la misma estampa que una conductancia. Una impedancia $Z$ solo se puede escribir como $Y=1/Z$ mientras no sea cero; una bobina a frecuencia cero rompe esto. La etapa [9](die-modifizierte-knotenanalyse.html#stufe-9) resuelve este problema. Los componentes no lineales como los diodos ([capítulo 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) el simulador los sustituye por la tangente de su curva característica, la estampa y lo repite hasta que ya no cambia nada.
:::

:::frage ¿Por qué se puede tachar precisamente la fila del nudo de referencia?
Cada una de las $k$ ecuaciones de nudo se deduce de las demás ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Se podría tachar cualquiera. Se tacha la fila del nudo de referencia porque, junto con su columna, vuelve a resultar una matriz simétrica y porque la corriente hacia masa rara vez interesa.
:::

:::aufgabe Ejercicio 9 ★★ De la lista de conexiones a la solución
<span class="anker" id="aufg-9"></span>

Se da la lista `R1 1 0 1k`, `R2 1 2 2k`, `R3 2 0 2k`, `I1 0 1 7m`, `I2 2 1 1m`.

<ol class="al">

<li>

Estampa la matriz completa de $3\times3$ y el lado derecho. Comprueba las sumas de fila.

</li>

<li>

Tacha el nudo de referencia y resuelve.

</li>

<li>

Comprobación: ¿Qué corriente fluye por las resistencias a masa y cuál sale de ella?

</li>

</ol>

:::loesung
(a) Con las conductancias 1, 0,5, 0,5 mS y las filas 0, 1, 2:

$$\begin{pmatrix}1{,}5&-1&-0{,}5\\-1&1{,}5&-0{,}5\\-0{,}5&-0{,}5&1\end{pmatrix}\begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-7\\8\\-1\end{pmatrix}.$$

`I2 2 1 1m` empuja 1 mA de 2 a 1, es decir, $+1$ en la fila 1 y $-1$ en la fila 2. Todas las sumas de fila son cero, y a la derecha la suma también es cero.

(b) $\begin{pmatrix}1{,}5&-0{,}5\\-0{,}5&1\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}8\\-1\end{pmatrix}$ con $D=1{,}25$, $D_1=7{,}5$, $D_2=2{,}5$. Por tanto, $U_1=6$ V, $U_2=2$ V.

(c) Por `R1` circulan 6 mA hacia masa, por `R3` 1 mA, en total 7 mA. De la masa, `I1` extrae exactamente 7 mA.
:::
:::
