---
title: Etapa 1: ¿Cuántas magnitudes son libres?
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1180300
summary: La Parte 2 mostró que una red tiene 2z incógnitas y 2z ecuaciones.
tags: 
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
La [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) mostró que una red tiene $2z$ incógnitas y $2z$ ecuaciones. Esta etapa muestra por qué para el cálculo bastan dos números mucho menores.
:::

**La idea.** Un árbol ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) une todos los nudos con $k-1$ ramas; las $m=z-k+1$ ramas restantes son ramas de enlace. Si se conocen las tensiones de las ramas del árbol, se conocen todas las tensiones: cada rama de enlace cierra exactamente una malla con ramas del árbol, y la ley de las mallas da su tensión. Si se conocen las corrientes de las ramas de enlace, se conocen todas las corrientes: en el extremo del árbol, una rama del árbol queda sola entre ramas de enlace, la ley de los nudos da su corriente, y así se sigue rama por rama. Por tanto, de $z$ corrientes solo se pueden fijar $m$, y de $z$ tensiones solo $k-1$.

:::satz Teorema 1.1 (Magnitudes libres de una red)
<span class="anker" id="satz-1-1"></span>

Las $z$ corrientes de rama de una red conexa deben cumplir $k-1$ ecuaciones de nudo independientes, y las $z$ tensiones de rama, $z-k+1$ ecuaciones de malla independientes. Por eso se pueden elegir libremente

<span class="anker" id="gl-1-1"></span>
$$m=z-k+1\ \text{corrientes}\qquad\text{y}\qquad k-1\ \text{tensiones}. \tag{1.1}$$

Todas las demás corrientes y tensiones se deducen de Kirchhoff.
:::

⁠**Cómo leerlo:** «Se pueden elegir libremente» significa: se pueden fijar los valores sin violar ninguna ley de Kirchhoff. $z$ cuenta las ramas como en la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html); en los libros en inglés el número suele llamarse $b$ (de *branch*). **Validez:** El recuento depende solo del grafo, no de los componentes. También vale para componentes no lineales.

:::abbildung et1/k8netz 1
La red modelo. Tres nudos (en rojo), seis ramas. La rama de la izquierda contiene la batería y $R_1$ en serie, porque entre ellas no se bifurca nada. El nudo 0 es toda la línea inferior.
:::

**Ejemplo.** La red de la fig. [1](#abb-1) tiene $k=3$ y $z=6$, es decir, $m=4$:

| Planteamiento | Incógnitas | Ecuaciones |
|---|---|---|
| todas las corrientes y tensiones | 12 | 6 componentes, 2 nudos, 4 mallas |
| ley de Ohm sustituida | 6 | 2 nudos, 4 mallas |
| corrientes de malla | 4 | 4 mallas; la fuente de corriente fija un valor, quedan 3 |
| potenciales de nudo | 2 | 2 nudos |

⁠**Casos límite:** Una conexión en serie en forma de anillo tiene $z=k$ y $m=1$: una sola corriente vale en todas partes, y esa es la esencia de la conexión en serie. Una conexión en paralelo tiene $k=2$ y $k-1=1$: una sola tensión vale en todas partes, y esa es la esencia de la conexión en paralelo.

:::frage ¿Se puede con aún menos incógnitas?
No sin cambiar la red, porque $m$ y $k-1$ cuentan exactamente lo que se puede fijar. Pero se puede simplificar antes. Si se agrupan conexiones en serie y en paralelo ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)), $z$ y $k$ se reducen. El recuento vale entonces para la red más pequeña.
:::

:::aufgabe Ejercicio 1 ★ Contar
<span class="anker" id="aufg-1"></span>

Da $k$, $z$, $m$ y $k-1$.

<ol class="al">

<li>

El puente de la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): fuente y cinco resistencias entre cuatro nudos.

</li>

<li>

Cinco nudos, cada uno unido con todos los demás por una resistencia.

</li>

<li>

La red modelo, una vez agrupadas la fuente de corriente y $R_5$ en una sola rama.

</li>

<li>

Un anillo de seis componentes.

</li>

</ol>

:::loesung
(a) $k=4$, $z=6$, $m=3$, $k-1=3$. (b) $k=5$, $z=10$ (cada uno de los 10 pares), $m=6$, $k-1=4$. (c) $k=3$, $z=5$, $m=3$, $k-1=2$. (d) $k=6$, $z=6$, $m=1$, $k-1=5$.
:::
:::
