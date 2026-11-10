---
title: Etapa 6: Nudos, ramas, mallas
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1120700
summary: Una red tiene muchas incógnitas.
tags: nudo, rama, grafo, malla, árbol, ramas de enlace, linealmente independientes, completo
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Una red tiene muchas incógnitas. Antes de calcular se cuenta: ¿Cuántas corrientes y tensiones hay, y cuántas ecuaciones independientes hay disponibles para ellas?
:::

**La idea.** Para el número de ecuaciones da igual qué componente hay en una rama. Si se sustituye cada rama por una línea, queda el esqueleto de la red (fig. [7](#abb-7)). Este esqueleto determina el cálculo.

:::abbildung et1/k2netz 7
Izquierda: la red del modelo de referencia con cuatro nudos y seis ramas. La rama de la fuente se llama 0; las demás llevan la letra de su resistencia. Derecha: su grafo. El árbol de las tres ramas negras deja tres ramas de enlace. Cada una cierra exactamente una malla a través de ramas del árbol (en rojo, la rama de enlace).
:::

:::definition Definición 6.1 (Conceptos topológicos básicos)
<span class="anker" id="satz-6-1"></span>

Cinco conceptos describen la estructura de una red:

<ul>

<li>

Un __nudo__ es un punto en el que la corriente se bifurca. $k$ es su número.

</li>

<li>

Una __rama__ une dos nudos a través de dipolos, y por ella circula una corriente. $z$ es su número.

</li>

<li>

El __grafo__ es la representación formada por nudos y ramas. Es conexo: desde cada nudo hay un camino hasta cualquier otro. Cada rama recibe el sentido de su flecha de corriente.

</li>

<li>

Una __malla__ es un camino cerrado en el que cada nudo está conectado con exactamente dos ramas vecinas. Ninguna rama ni ningún nudo se recorre más de una vez.

</li>

<li>

Un __árbol__ es un subgrafo conexo que contiene todos los nudos y no forma ninguna malla. Las ramas restantes se llaman __ramas de enlace__.

</li>

</ul>
:::

:::satz Teorema 6.2 (Número de mallas independientes)
<span class="anker" id="satz-6-2"></span>

Las mallas se llaman __linealmente independientes__ si se pueden ordenar de modo que cada una contenga al menos una rama que falte en las anteriores. Un grafo con $k$ nudos y $z$ ramas tiene exactamente

<span class="anker" id="gl-6-1"></span>
$$m=z-k+1 \tag{6.1}$$

mallas independientes. Forman un sistema __completo__: ninguna malla adicional aporta nada nuevo. Cada árbol fija un sistema así: cada rama de enlace cierra exactamente una malla a través de las ramas del árbol.
:::

⁠**Cómo leerlo:** $m$ cuenta las mallas cuyas ecuaciones aportan información nueva. Todas las demás mallas se componen de ellas. **Validez:** El grafo debe ser conexo.

:::herleitung Por qué $z-k+1$
Se construye un árbol: empezando por un nudo, cada rama nueva añade exactamente un nudo nuevo; de lo contrario surgiría una malla. Para $k$ nudos hacen falta $k-1$ ramas del árbol. Quedan $z-(k-1)$ ramas de enlace. En el árbol hay exactamente un camino entre dos nudos, así que cada rama de enlace cierra exactamente una malla. Esta no contiene ninguna otra rama de enlace, y por eso estas mallas son independientes.
:::

**Incógnitas y ecuaciones.** Cada rama lleva una corriente y una tensión: son $2z$ incógnitas. Frente a ellas hay $z$ ecuaciones de componente (una por rama), $k-1$ ecuaciones de nudo (etapa [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7)) y $z-k+1$ ecuaciones de malla (etapa [8](die-maschenregel-ist-energieerhaltung.html#stufe-8)). La suma es exactamente $2z$. **En resumen:** Toda red tiene exactamente tantas ecuaciones como incógnitas.

::::beispiel
La red tiene $k=4$, $z=6$, es decir, $m=3$. Su grafo tiene 16 árboles de tres ramas cada uno. La fig. [7](#abb-7) elige la estrella alrededor de $K_4$ con las ramas 0, b y d. Las ramas de enlace a, c y e cierran las mallas $M_1$, $M_2$ y $M_3$. El sistema comprende 12 incógnitas y 12 ecuaciones.
::::

⁠**Casos límite:** Un solo lazo tiene $z=k$, es decir, $m=1$. Un árbol solo tiene $z=k-1$, es decir, $m=0$: sin camino cerrado no circula corriente estacionaria.

:::frage ¿Es un nudo la unión de dos componentes sin derivación?
Según la definición, no, porque allí no se bifurca nada. Si aun así se cuenta, $m$ no cambia: un nudo adicional divide una rama en dos, y $k$ y $z$ aumentan ambos en 1.
:::

:::aufgabe Ejercicio 6 ★★ Contar
<span class="anker" id="aufg-6"></span>

Da en cada caso $k$, $z$, $m$ y el número de ramas del árbol.

<ol class="al">

<li>

Una fuente alimenta tres resistencias en paralelo.

</li>

<li>

De la red de la fig. [7](#abb-7) se quita $R_\mathrm e$.

</li>

<li>

Una red tiene 6 nudos y 10 ramas. ¿Cuántas ecuaciones de qué tipo hacen falta?

</li>

</ol>

:::loesung
(a) Las dos barras son los nudos: $k=2$, $z=4$, $m=3$, una rama del árbol. (b) $k=2$, $z=3$, $m=2$, una rama del árbol. Sin $R_\mathrm e$ la corriente ya no se bifurca en $K_2$ y $K_3$: $R_\mathrm a$ y $R_\mathrm b$ forman una rama, $R_\mathrm c$ y $R_\mathrm d$ la otra. (c) $m=10-6+1=5$. Hacen falta 5 ecuaciones de nudo, 5 ecuaciones de malla y 10 ecuaciones de componente para 20 incógnitas. Un árbol tiene 5 ramas.
:::
:::
