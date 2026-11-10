---
title: Etapa 5: Líneas de campo y conductores
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1110700
summary: Las líneas de campo muestran todo un campo de un vistazo.
tags: inducción electrostática, línea de campo, fuentes, sumideros, apantallamiento, uniforme, campo de borde
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Las líneas de campo muestran todo un campo de un vistazo. Con ellas también queda claro qué hace un metal con un campo.
:::

**La idea.** Al enlazar las flechas de campo surgen líneas (fig. [6](#abb-6)). Se hacen visibles con granos alargados en aceite: el campo desplaza un poco las cargas de cada grano, y el grano gira hacia la dirección del campo. En un metal, los electrones libres se desplazan hasta que ya no actúa ninguna fuerza sobre ellos. Este desplazamiento se llama __inducción electrostática__.

:::satz Teorema 5.1 (Líneas de campo de cargas en reposo)
<span class="anker" id="satz-5-1"></span>

Una __línea de campo__ es una curva cuya tangente tiene en cada punto la dirección de $\vec E$; su densidad indica la intensidad del campo. Se cumple:

<ol>

<li>

Las líneas de campo empiezan en cargas positivas (__fuentes__) y terminan en negativas (__sumideros__), nunca en el espacio vacío. En una carga aislada, el otro extremo se va al infinito.

</li>

<li>

Las líneas de campo no se cortan.

</li>

<li>

Son perpendiculares a la superficie de un conductor.

</li>

<li>

En el interior de un conductor, $\vec E=0$. Una cavidad sin carga rodeada por el conductor no tiene campo (__apantallamiento__).

</li>

</ol>
:::

⁠**Cómo leerlo:** Las reglas 1 y 2 valen en el espacio vacío; las reglas 3 y 4 dicen qué cambia el metal en el campo. En las fuentes y los sumideros no fluye nada: las palabras indican el principio y el final de las líneas. **Validez:** Todas las reglas suponen cargas en reposo; la etapa [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10) muestra campos con líneas cerradas.

:::abbildung et1/k1feldlinien 6
Líneas de campo calculadas. Arriba: con cargas de signo opuesto van de $+$ a $-$; con cargas del mismo signo se esquivan. Abajo a la izquierda: entre dos placas discurren paralelas y con la misma densidad; solo en el borde se curvan hacia fuera. Abajo a la derecha: tubo metálico en sección entre dos placas. A la izquierda se acumulan electrones, a la derecha quedan cargas positivas, y en el interior $E=0$.
:::

:::herleitung De dónde vienen las reglas
⁠**Regla 2.** En un punto de corte, $\vec E$ tendría dos direcciones, pero la fuerza sobre una carga de prueba es única.

⁠**Regla 4, metal.** Si hubiera campo en el metal, los electrones libres seguirían moviéndose. El reposo solo se alcanza cuando las cargas desplazadas anulan exactamente el campo exterior en el interior. Las cargas sobrantes quedan en la superficie.

⁠**Regla 3.** Una componente del campo a lo largo de la superficie empujaría los electrones por ella. En reposo solo queda la componente perpendicular.

⁠**Regla 4, cavidad.** El campo exterior termina en las cargas inducidas de la cara externa. Sin carga en la cavidad, una línea tendría que ir allí de pared a pared. Una carga podría ganar energía a lo largo de esa línea y volver gratis por el metal sin campo. Sería energía de la nada, algo que la etapa [6](arbeit-im-feld.html#stufe-6) excluye.
:::

::::beispiel
En el par de placas, la carga está en las caras interiores, y las líneas van paralelas y con la misma densidad de A a B. Igual densidad significa que $\vec E$ es igual en todas partes: el campo es __uniforme__. Esto vale mientras $d$ sea pequeña frente a la anchura de las placas; solo en el borde se curva hacia fuera un __campo de borde__ más débil. El tubo de la fig. [6](#abb-6) muestra las reglas 3 y 4; en su vértice el campo es aproximadamente el doble que sin el tubo. Una envolvente metálica cerrada protege su interior; por eso se está seguro dentro de un coche durante una tormenta.
::::

⁠**Comprobación:** La regla 1 encaja con la ley de Coulomb. De una carga salen $N$ líneas de manera uniforme en todas las direcciones y atraviesan una esfera de área $4\pi r^2$. La densidad $N/(4\pi r^2)$ disminuye con $1/r^2$, y de ahí también el factor $4\pi$ en $k=1/(4\pi\varepsilon_0)$. A la inversa, el apantallamiento solo es perfecto con el exponente exactamente 2. Así surgieron las medidas de la etapa [3](die-kraft-zwischen-ladungen.html#stufe-3): se buscaba un campo residual en una esfera hueca cargada.

:::frage ¿Vuela una carga a lo largo de la línea de campo?
En general, no. La línea de campo indica la dirección de la fuerza, es decir, de la aceleración, no la de la velocidad. Solo con líneas rectas y partiendo del reposo coinciden trayectoria y línea.
:::

:::aufgabe Ejercicio 5 ★ Predecir el apantallamiento
<span class="anker" id="aufg-5"></span>

Responde primero solo con líneas de campo, sin calcular.

<ol class="al">

<li>

Una caja metálica sin carga propia está en el campo de una varilla cargada. ¿Qué valor tiene el campo dentro de la caja? ¿Dónde están las cargas inducidas?

</li>

<li>

En el centro de una esfera metálica hueca, aislada y neutra, se coloca una carga $+Q$. ¿Hay campo en la cavidad? ¿Hay campo fuera?

</li>

</ol>

:::loesung
(a) En la caja, $E=0$. Las cargas inducidas están en el exterior: frente a la varilla con el signo contrario, en el lado opuesto con el mismo signo. (b) En la cavidad hay campo, porque de la carga salen líneas. Terminan en la pared interior, que por inducción electrostática se carga con $-Q$. La esfera es neutra, así que en el exterior queda $+Q$, y fuera hay el campo de una carga $+Q$. El apantallamiento solo protege el interior de los campos exteriores.
:::
:::
