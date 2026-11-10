---
title: Etapa 6: ¿Qué método y cuándo?
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Análisis por mallas y por nudos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Capítulo 8: Análisis por mallas y por nudos
order: 1180800
summary: Ambos métodos dan lo mismo.
tags: dualidad
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Ambos métodos dan lo mismo. Esta etapa aclara cuál da menos trabajo y qué no puede hacer cada uno.
:::

**La idea.** El trabajo de cálculo está en el tamaño de la matriz. El análisis por mallas necesita $z-k+1$ incógnitas; el análisis por nudos, $k-1$. Muchas ramas en pocos nudos significan muchas mallas, pero pocos nudos. Las cadenas largas significan lo contrario.

:::satz Teorema 6.1 (Comparación del número de ecuaciones)
<span class="anker" id="satz-6-1"></span>

El análisis por nudos necesita menos ecuaciones exactamente cuando $k-1<z-k+1$, es decir,

<span class="anker" id="gl-6-1"></span>
$$z>2k-2. \tag{6.1}$$
:::

⁠**Cómo leerlo:** En promedio, a un nudo llegan $2z/k$ extremos de rama, porque cada rama tiene dos extremos. En el límite son $4-4/k$, es decir, algo menos de cuatro. Si en promedio llegan más ramas a los nudos, gana el análisis por nudos (fig. [6](#abb-6)). **Validez:** Cada fuente real cuenta como una rama, porque para las mallas se convierte en fuente de tensión y resistencia en serie. La conversión no cambia $k-1$.

:::abbildung et1/k8zahl 6
Cada punto es una red. Por debajo de $z=k-1$ no sería conexa. Por encima de la recta roja $z=2k-2$, el análisis por nudos necesita menos ecuaciones; por debajo, el análisis por mallas; sobre la recta son iguales.
:::

|  | Análisis por mallas | Análisis por nudos |
|---|---|---|
| Incógnitas | $z-k+1$ corrientes de malla | $k-1$ potenciales de nudo |
| se cumple por sí sola | ley de los nudos | ley de las mallas |
| se plantean | leyes de las mallas | leyes de los nudos |
| Matriz | $\mathbf Z$ en $\Omega$ | $\mathbf Y$ en S |
| Diagonal | suma de las resistencias de la malla | suma de las conductancias del nudo |
| Fuera de la diagonal | $\pm$ resistencia común | $-$ conductancia de acoplamiento |
| lado derecho | tensiones de fuente | corrientes de fuente |
| estorba | fuente de corriente | fuente de tensión |
| caso más pequeño | conexión en serie, $m=1$ | conexión en paralelo, $k-1=1$ |
| Uso | cálculo a mano | cálculo a mano y simulador |

La tabla muestra una __dualidad__, una simetría especular: si se intercambian malla y nudo, corriente y tensión, serie y paralelo, resistencia y conductancia, un método se convierte en el otro. La razón está en Kirchhoff: ambas leyes dicen «la suma es cero», solo que sobre conjuntos distintos.

::::beispiel
Tras la conversión de la derecha, la red modelo tiene $k=3$ y $z=5$. Con $5>4$ queda por encima de la recta, y en efecto eran tres mallas frente a dos nudos.
::::

⁠**Caso límite:** El puente del [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), con $k=4$ y $z=6$, queda justo sobre la recta. Entonces deciden las fuentes: una fuente de tensión ideal habla a favor de las mallas, porque allí va en el lado derecho.

Los simuladores solo usan potenciales de nudo. Las mallas de una red, un programa tiene que buscarlas primero, y solo hay ventanas si la red se puede dibujar sin cruces. Los nudos, en cambio, ya están en la descripción del circuito (etapa [7](stempel-und-netzliste.html#stufe-7)).

:::frage ¿No es superfluo el análisis por mallas si los simuladores no lo usan?
Para redes grandes, sí. A mano suele ser más corto, y mantiene la vista en los circuitos de corriente: se ve qué corrientes comparten qué camino. Con pocas mallas y muchos nudos, por ejemplo en largas cadenas de conexiones en serie, gana claramente.
:::

:::aufgabe Ejercicio 8 ★ Elegir el método
<span class="anker" id="aufg-8"></span>

¿Qué método necesita menos ecuaciones? Da ambos números.

<ol class="al">

<li>

Tres fuentes de tensión reales están en paralelo con una carga, cada una como una rama.

</li>

<li>

Un anillo de seis componentes.

</li>

<li>

Cinco nudos, todos unidos entre sí.

</li>

<li>

Demuestra: si en una red se agrupan dos componentes en serie junto con el nudo intermedio, $k$ y $z$ bajan en 1, y $m$ no cambia.

</li>

</ol>

:::loesung
(a) $k=2$, $z=4$: $m=3$ frente a $k-1=1$, potenciales de nudo. Aquí $z=4>2$.

(b) $k=6$, $z=6$: $m=1$ frente a 5, corrientes de malla.

(c) $k=5$, $z=10$: $m=6$ frente a 4, potenciales de nudo.

(d) El nudo intermedio desaparece y dos ramas se convierten en una, es decir, $m'=(z-1)-(k-1)+1=z-k+1=m$. El recuento del [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) llega a la misma conclusión.
:::
:::
