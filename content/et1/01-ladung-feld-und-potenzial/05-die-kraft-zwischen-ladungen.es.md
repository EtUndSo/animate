---
title: Etapa 3: La fuerza entre cargas
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1110500
summary: Los cuerpos cargados ejercen fuerzas entre sí.
tags: constante eléctrica, cargas puntuales, superposición
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Los cuerpos cargados ejercen fuerzas entre sí. Esta etapa convierte «se atraen» en una ley con números.
:::

**La idea.** Se cuelga de un hilo una esfera cargada y se coloca al lado una segunda con carga opuesta (fig. [4](#abb-4)). La atracción aparta la esfera de la vertical, la gravedad la devuelve, y la desviación revela la fuerza: $\tan\alpha=F/(m\,g)$. Variando las cargas y la distancia se observa que la fuerza crece proporcionalmente a cada una de las dos cargas y disminuye con el cuadrado de la distancia. La ley de la gravitación [(1.2)](groen-kraft-und-arbeit.html#gl-1-2) tiene la misma forma, con cargas en lugar de masas.

:::abbildung et1/k1pendel 4
Izquierda: esfera A en un hilo junto a la esfera B, fuerzas a escala. El peso $m\,g=9{,}81$ mN, la fuerza eléctrica $F=2{,}0$ mN y la fuerza del hilo $F_0=10{,}0$ mN se compensan, $\alpha=11{,}5^\circ$. Derecha: fuerza de Coulomb en el modelo de referencia. El doble de distancia da una cuarta parte de la fuerza.
:::

:::satz Teorema 3.1 (Ley de Coulomb)
<span class="anker" id="satz-3-1"></span>

A la distancia $r$, dos cargas puntuales en reposo ejercen fuerzas de módulo

<span class="anker" id="gl-3-1"></span>
$$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}} \tag{3.1}$$

una sobre otra. Como vector, la fuerza sobre A, donde $\vec r$ apunta de B a A, es

<span class="anker" id="gl-3-2"></span>
$$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}. \tag{3.2}$$
:::

⁠**Cómo leerlo:** $Q_\mathrm{A}$, $Q_\mathrm{B}$ son las cargas en C, en [(3.2)](#gl-3-2) con signo, y $r$ es la distancia en m. El vector $\vec r/r$ tiene longitud 1 y solo indica la dirección. $\varepsilon_0=8{,}854\cdot10^{-12}$ A s/(V m) se llama __constante eléctrica__. Con cargas del mismo signo, $Q_\mathrm{A}Q_\mathrm{B}>0$ y $\vec F_\mathrm{A}$ apunta alejándose de B: repulsión. Con cargas de signo opuesto apunta hacia B: atracción. **Validez:** Los cuerpos deben ser pequeños frente a $r$ (__cargas puntuales__) y estar en reposo. La ley vale en el vacío; en aire la fuerza solo es un 0,06 % menor. Varias cargas actúan de forma independiente, y sus fuerzas se suman como vectores (__superposición__).

:::herleitung Del experimento a la ley
La ley es un resultado de medida. Las series de ensayos dan por separado $F\sim Q_\mathrm{A}$, $F\sim Q_\mathrm{B}$, $F\sim1/r^2$ y $\vec F\parallel\vec r$, y juntas $F\sim Q_\mathrm{A}Q_\mathrm{B}/r^2$; el factor es $k$. Si se supone $F\sim1/r^{2\pm\delta}$, la cota de $\delta$ bajó de 0,02 con Cavendish (siglo XVIII) a $5\cdot10^{-5}$ con Maxwell (siglo XIX), y luego a $10^{-13}$ (Bartlett y otros, 1970) y $3\cdot10^{-16}$ (Williams y otros, 1971).
:::

::::beispiel
En el modelo de referencia,

$$F=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}\cdot\frac{10\cdot10^{-9}\,\mathrm{C}\cdot20\cdot10^{-9}\,\mathrm{C}}{(0{,}03\,\mathrm{m})^2}=2{,}0\,\mathrm{mN}.$$

El peso de la esfera A es 9,81 mN, así que $\tan\alpha=0{,}204$ y $\alpha=11{,}5^\circ$. Esta desviación la produce la falta de un electrón de cada $5\cdot10^{12}$. La gravitación entre dos esferas de 1 g a la misma distancia es solo $7{,}4\cdot10^{-14}$ N; es $2{,}7\cdot10^{10}$ veces menor y puede omitirse. Entre dos electrones, la fuerza eléctrica es incluso $4{,}2\cdot10^{42}$ veces mayor.
::::

⁠**Casos límite:** Para $r\to\infty$, $F\to0$. Para $Q_\mathrm{A}=0$, $F=0$. El doble de distancia da 0,5 mN; el doble de carga $Q_\mathrm{A}$ da 4,0 mN.

:::frage La esfera B tiene el doble de carga que la esfera A. ¿Siente A por eso la fuerza mayor?
No, ambas sienten los mismos 2,0 mN en sentidos opuestos, porque en [(3.1)](#gl-3-1) las dos cargas entran por igual. Lo que puede ser distinto es el efecto: la esfera más ligera se acelera más.
:::

:::aufgabe Ejercicio 3 ★★ Fuerza de Coulomb
<span class="anker" id="aufg-3"></span>

Dos pequeñas esferas metálicas tienen $+2$ nC y $+5$ nC a una distancia de 2 cm.

<ol class="al">

<li>

¿Qué valor tiene la fuerza y hacia dónde apunta en cada esfera?

</li>

<li>

¿Qué resulta con el triple de distancia? Responde primero sin calculadora.

</li>

<li>

Las esferas, de igual tamaño, se tocan brevemente y se vuelven a llevar a 2 cm. ¿Qué fuerza actúa ahora? ¿Por qué no ha permanecido igual, aunque la carga total sí?

</li>

</ol>

:::loesung
(a) $F=k\cdot2\,\mathrm{nC}\cdot5\,\mathrm{nC}/(2\,\mathrm{cm})^2=225$ µ N. Cargas del mismo signo: cada esfera es empujada lejos de la otra. (b) El triple de distancia da una novena parte: 25 µ N.

(c) Cada esfera tiene ahora $+3{,}5$ nC, así que $F=k\,(3{,}5\,\mathrm{nC})^2/(2\,\mathrm{cm})^2=275$ µ N. La fuerza depende del producto de las cargas, no de su suma: $3{,}5\cdot3{,}5=12{,}25$ frente a $2\cdot5=10$.
:::
:::
