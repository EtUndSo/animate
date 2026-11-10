---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Análisis por mallas y por nudos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Capítulo 8: Análisis por mallas y por nudos
order: 1181200
summary: Por qué a una red le bastan pocas incógnitas
tags: análisis por mallas, corriente de malla, análisis por nudos, potencial de nudo, nudo de referencia, matriz de resistencias, matriz de conductancias, análisis por nudos modificado
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Una red con $z$ ramas y $k$ nudos tiene $m=z-k+1$ mallas independientes y $k-1$ nudos independientes. De las $z$ corrientes solo $m$ son libres; de las $z$ tensiones, solo $k-1$.

</li>

<li>

El __análisis por mallas__ calcula con la __corriente de malla__, una corriente circulante imaginada para cada malla. Entra en cada nudo y vuelve a salir, así que la ley de los nudos se cumple por sí sola. El __análisis por nudos__ calcula con el __potencial de nudo__, la tensión de cada nudo respecto a un __nudo de referencia__ elegido libremente. Toda tensión de rama es una diferencia, así que la ley de las mallas se cumple por sí sola.

</li>

<li>

Las ecuaciones restantes se leen del circuito en forma de matriz: en la __matriz de resistencias__, en la diagonal está la suma de las resistencias de una malla, y junto a ella las resistencias comunes de dos mallas. En la __matriz de conductancias__, en la diagonal está la suma de las conductancias de un nudo, y junto a ella la conductancia negativa entre dos nudos. El __análisis por nudos modificado__ toma además como incógnita la corriente de cada fuente de tensión, y así calcula SPICE.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

De $z$ corrientes son libres $m=z-k+1$; de $z$ tensiones, $k-1$. Esos son los tamaños de los dos métodos. El análisis por nudos es menor si $z>2k-2$.

</li>

<li>

Las corrientes de malla giran en círculo; la ley de los nudos se cumple por sí sola. Corriente de rama = suma de las corrientes de malla con signo. $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$: en la diagonal, la suma de las resistencias de la malla; junto a ella, $\pm$ las resistencias comunes; a la derecha, las tensiones impulsoras.

</li>

<li>

Los potenciales de nudo son alturas; la ley de las mallas se cumple por sí sola. Tensión de rama = diferencia. $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$: en la diagonal, la suma de las conductancias del nudo; junto a ella, la conductancia de acoplamiento negativa; a la derecha, las corrientes de fuente entrantes.

</li>

<li>

Las fuentes de corriente estorban a las mallas, las de tensión a los nudos: las fuentes reales se convierten antes. Las magnitudes internas de la fuente se calculan en la red original.

</li>

<li>

Cada componente estampa de forma independiente: $G$ en cuatro posiciones, la fuente de corriente solo a la derecha, $g$ en las columnas $p$, $q$. Tachar el nudo de referencia. La matriz es dispersa; las fuentes controladas rompen la simetría.

</li>

<li>

MNA: cada fuente de tensión aporta su corriente como incógnita y $U_i-U_k=U_\mathrm q$ como ecuación. Así calcula SPICE. Una fuente de 0 V mide corriente. La ganancia de tensión es menos transconductancia por resistencia de carga.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** Kirchhoff exige dos cosas: la ley de los nudos y la ley de las mallas. Si se eligen las incógnitas de modo que una de las dos leyes se cumpla para cualquier valor numérico, solo hay que escribir la otra. El número de incógnitas es entonces exactamente el número de ecuaciones restantes.

| Resultado | De dónde viene |
|---|---|
| $m$ corrientes libres, $k-1$ tensiones libres | Un árbol determina qué se puede fijar y qué se deduce de ello (etapa [1](wie-viele-groen-sind-frei.html#stufe-1)) |
| Corrientes de malla | Una corriente circulante no aporta nada a ningún nudo (etapa [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2)) |
| Matriz de resistencias $\mathbf Z$ | La corriente propia recorre todas las resistencias de la malla, una ajena solo las comunes (etapa [3](das-maschenstromverfahren.html#stufe-3)) |
| Potenciales de nudo | Una vuelta regresa al potencial inicial (etapa [4](potenziale-erfullen-die-maschenregel.html#stufe-4)) |
| Matriz de conductancias $\mathbf Y$ | El potencial propio impulsa corriente por todas las conductancias del nudo, uno ajeno solo por la común (etapa [5](das-knotenpotentialverfahren.html#stufe-5)) |
| Elección del método | Gana el menor de los dos números, es decir, $z>2k-2$ o no (etapa [6](welches-verfahren-wann.html#stufe-6)) |
| Estampas y lista de conexiones | Un componente solo toca sus dos nudos (etapa [7](stempel-und-netzliste.html#stufe-7)) |
| Matriz asimétrica | Una fuente controlada depende de nudos ajenos (etapa [8](gesteuerte-quellen-und-verstarker.html#stufe-8)) |
| Análisis por nudos modificado | Una fuente de tensión ideal no tiene conductancia, su corriente pasa a ser incógnita (etapa [9](die-modifizierte-knotenanalyse.html#stufe-9)) |
