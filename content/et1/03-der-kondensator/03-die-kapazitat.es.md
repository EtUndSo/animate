---
title: Etapa 2: La capacidad
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El condensador
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Capítulo 3: El condensador
order: 1130300
summary: ¿Cuánta carga mantiene una tensión dada en las placas?
tags: 
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
¿Cuánta carga mantiene una tensión dada en las placas? La respuesta es un solo número para cada componente.
:::

**La idea.** Si se duplica la carga en ambas placas, cada carga aporta su campo dos veces. Por la superposición del [capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), el campo se duplica en cada lugar y su forma no cambia (fig. [2](#abb-2) izquierda). La tensión es la integral del campo de placa a placa, así que también se duplica. Por eso, $Q$ y $U$ son proporcionales. Su cociente no depende de cuánta carga haya en ese momento, sino solo de la forma, la separación y el material.

:::definition Definición 2.1 (Capacidad)
<span class="anker" id="satz-2-1"></span>

La capacidad de un condensador es el cociente entre carga y tensión:

<span class="anker" id="gl-2-1"></span>
$$C=\frac{Q}{U},\qquad Q=C\,U,\qquad[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F\ \text{(faradio)}. \tag{2.1}$$
:::

⁠**Cómo leerlo:** $Q$ es la carga de la placa positiva en C (culombios), $U$ la tensión entre las placas en V, $C$ la capacidad en F. Con 1 F, un voltio mantiene un culombio. Eso es muchísimo. Los valores habituales están en fF, pF, nF y µF; los condensadores electrolíticos llegan hasta el rango de los mF. No hay que confundir los símbolos: $C$ en cursiva es la capacidad, C en redonda es el culombio. **Validez:** [(2.1)](#gl-2-1) supone que el material entre las placas no cambia con el campo. La cerámica de $\varepsilon_\mathrm{r}$ muy grande (etapa [4](plattenkondensator-und-dielektrikum.html#stufe-4)) pierde capacidad de forma apreciable a tensiones altas.

:::abbildung et1/k3qu 2
Izquierda: el doble de carga da líneas de campo el doble de densas y, por tanto, el doble de tensión. Derecha: la carga crece en proporción a la tensión; la pendiente de la recta es la capacidad. Los puntos corresponden a 9 V.
:::

::::beispiel
El par de placas tiene $C=29{,}5$ pF (etapa [4](plattenkondensator-und-dielektrikum.html#stufe-4)). A 9 V lleva $Q=29{,}5\,\mathrm{pF}\cdot9\,\mathrm{V}=266$ pC, es decir, $1{,}66\cdot10^{9}$ electrones. Una placa de cobre de 1 mm de grosor y esta área contiene $8{,}5\cdot10^{23}$ electrones libres. Por tanto, solo se desplaza uno de cada $5\cdot10^{14}$, y estos se sitúan en la cara interior de la placa. El metal permanece prácticamente inalterado. El condensador del circuito RC lleva a 9 V $Q=900\,\mu\text{C}$, 3,4 millones de veces más.
::::

⁠**Caso límite:** Para $U=0$ es $Q=0$: sin tensión no hay nada separado. Con la misma carga, el condensador más pequeño muestra la mayor tensión.

:::frage Capacidad suena a volumen de un recipiente. ¿Llega un condensador a estar lleno?
No en el sentido de un cubo. Más tensión siempre lleva más carga, y $C$ no cambia. El límite lo pone el dieléctrico: por encima de cierta intensidad de campo se produce su ruptura. En este capítulo, lleno solo significa: la tensión ha alcanzado la de la fuente.
:::

:::aufgabe Ejercicio 2 ★ Carga y tensión
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Un condensador de 470 nF está conectado a 12 V. ¿Cuál es su carga?

</li>

<li>

¿A qué tensión lleva 1 µC?

</li>

<li>

La tensión se reduce a la mitad. ¿Qué ocurre con $Q$ y con $C$?

</li>

<li>

Dos condensadores de 10 µF y 1 µF llevan 50 µC cada uno. ¿Qué tensiones tienen?

</li>

</ol>

:::loesung
(a) $Q=470\,\mathrm{nF}\cdot12\,\mathrm{V}=5{,}64\,\mu\text{C}$.

(b) $U=Q/C=1\,\mu\text{C}/470\,\mathrm{nF}=2{,}13$ V.

(c) $Q$ se reduce a la mitad, a 2,82 µC. $C$ no cambia, porque solo depende del componente.

(d) $U=Q/C$: 5 V en el condensador de 10 µF, 50 V en el de 1 µF. La misma carga produce la mayor tensión en el más pequeño.
:::
:::
