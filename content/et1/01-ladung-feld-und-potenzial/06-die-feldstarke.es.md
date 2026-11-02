---
title: Etapa 4: La intensidad de campo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Carga, campo y potencial
order: 1110600
summary: La ley de Coulomb da la fuerza, pero no dice cómo llega a través del espacio vacío.
tags: carga de prueba, intensidad de campo eléctrico
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
La ley de Coulomb da la fuerza, pero no dice cómo llega a través del espacio vacío. El concepto de campo responde a esto y separa la causa del efecto.
:::

**La idea.** En lugar de «B atrae a A a través de 3 cm», el proceso se descompone. Primero: la carga B modifica el espacio a su alrededor, crea un campo. Segundo: la carga A siente el campo en su propio lugar y allí experimenta una fuerza. Por qué las cargas crean campos no puede reducirse a algo más simple; es una ley fundamental. Pero esta imagen resuelve tres problemas. **Causa y efecto quedan separados:** El campo solo depende de las cargas que lo crean y vale para cualquier carga que se introduzca en él. **Muchas cargas se vuelven manejables:** Sus campos se suman una vez, y después se calcula con un vector por lugar. **El efecto necesita tiempo:** Si se desplaza B, la fuerza sobre A solo cambia cuando la variación del campo llega allí a la velocidad de la luz. En 3 cm tarda 100 ps; del Sol a la Tierra, 8,3 minutos. Mientras tanto, la variación está en el campo, que es por tanto algo más que una ayuda de cálculo.

:::analogie
La Tierra está rodeada de un campo gravitatorio: en cada lugar actúa sobre toda masa la fuerza $\vec F=m\,\vec g$. El campo $\vec g$ es fuerza por unidad de masa; el campo eléctrico, fuerza por unidad de carga. La imagen deja de valer en dos puntos: las masas siempre se atraen, y un campo gravitatorio no puede apantallarse.
:::

:::definition Definición 4.1 (Intensidad de campo eléctrico)
<span class="anker" id="satz-4-1"></span>

Si se lleva una pequeña __carga de prueba__ $Q$ a un lugar y se mide la fuerza $\vec F$ sobre ella, la __intensidad de campo eléctrico__ allí es

<span class="anker" id="gl-4-1"></span>
$$\vec E:=\lim_{Q\to0}\frac{\vec F}{Q},\qquad\text{es decir}\quad\vec F=Q\cdot\vec E. \tag{4.1}$$

La dirección de $\vec E$ es la de la fuerza sobre una carga de prueba positiva. El campo eléctrico asigna a cada lugar uno de estos vectores.
:::

⁠**Cómo leerlo:** La unidad es $[E]=\mathrm{N/C}=\mathrm{m\,kg\,A^{-1}\,s^{-3}}=\mathrm{V/m}$, porque $\mathrm V=\mathrm{J/C}=\mathrm{N\,m/C}$. Sobre una carga negativa, la fuerza actúa en sentido contrario a $\vec E$. Valores típicos: en un conductor por el que circula corriente 0,1 V/m, en la atmósfera con buen tiempo 100 a 200 V/m, en la superficie de una antena de radiodifusión 1 a 1000 V/m, en una línea de alta tensión $10^6$ V/m, en un condensador (componente de dos placas, [Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) $10^6$ a $10^8$ V/m. A $3\cdot10^6$ V/m el aire se perfora y salta una chispa. **Validez:** El límite $Q\to0$ es necesario porque una carga de prueba grande desplaza las cargas que crean el campo, por ejemplo los electrones libres de una placa metálica. Pero lo que se quiere medir es el campo sin la carga de prueba.

:::satz Teorema 4.2 (Campo de cargas puntuales)
<span class="anker" id="satz-4-2"></span>

Una carga puntual $Q_0$ crea a la distancia $r$ el campo

<span class="anker" id="gl-4-2"></span>
$$\vec E=k\,\frac{Q_0}{r^2}\cdot\frac{\vec r}{r},\qquad E=k\,\frac{|Q_0|}{r^2}, \tag{4.2}$$

donde $\vec r$ apunta de la carga al lugar. Varias cargas crean juntas la suma de sus campos: $\vec E=\sum_i\vec E_i$.
:::

:::herleitung Campo de una carga puntual
Según [(3.2)](die-kraft-zwischen-ladungen.html#gl-3-2), una carga de prueba $Q$ experimenta la fuerza $\vec F=k\,Q\,Q_0/r^2\cdot\vec r/r$. Al dividir por $Q$ desaparece $Q$, y el resultado solo depende de $Q_0$ y del lugar. La regla de la suma se deduce de la superposición de las fuerzas.
:::

:::abbildung et1/k1feldpfeile 5
Vectores de campo alrededor de una carga puntual positiva y una negativa. El campo se aleja de la carga positiva y apunta hacia la negativa. La longitud de las flechas es proporcional a $1/r^2$.
:::

**Ejemplo.** La esfera B ($-20$ nC) crea en el lugar de la esfera A el campo $E=k\cdot20\,\mathrm{nC}/(3\,\mathrm{cm})^2=2{,}0\cdot10^5$ V/m, que apunta hacia B. La fuerza sobre A es $F=10\,\mathrm{nC}\cdot2{,}0\cdot10^5\,\mathrm{V/m}=2{,}0$ mN, como en la etapa [3](die-kraft-zwischen-ladungen.html#stufe-3). A la inversa, A crea en el lugar de B solo $1{,}0\cdot10^5$ V/m, pero allí encuentra el doble de carga: de nuevo 2,0 mN.

⁠**En resumen:** la fuerza sobre una carga es su carga por el campo en su lugar.

⁠**Casos límite:** Para $r\to\infty$, $E\to0$. Para $r\to0$, $E$ crecería sin límite; eso muestra el límite del modelo de carga puntual.

:::frage ¿Siente una carga también su propio campo?
En $\vec F=Q\vec E$ solo figura el campo de las *otras* cargas. Una carga en reposo no ejerce ninguna fuerza sobre sí misma.
:::

:::aufgabe Ejercicio 4 ★★ Dos cargas, un punto sin campo
<span class="anker" id="aufg-4"></span>

En el eje $x$ están $Q_1=+4$ nC en $x=0$ y $Q_2=+1$ nC en $x=6$ cm.

<ol class="al">

<li>

Calcula el módulo y el sentido del campo en $x=3$ cm. ¿Qué fuerza experimenta allí un electrón?

</li>

<li>

¿Dónde, entre las cargas, es $E=0$?

</li>

<li>

Caso límite: ¿a dónde se desplaza este punto para $Q_2\to0$? ¿Encaja con el campo de una sola carga?

</li>

</ol>

:::loesung
(a) $E_1=k\cdot4\,\mathrm{nC}/(3\,\mathrm{cm})^2=40{,}0$ kV/m hacia la derecha, $E_2=k\cdot1\,\mathrm{nC}/(3\,\mathrm{cm})^2=9{,}99$ kV/m hacia la izquierda, en total $E=30{,}0$ kV/m hacia la derecha. Electrón: $F=e\,E=4{,}8\cdot10^{-15}$ N hacia la izquierda.

(b) $E=0$ exige $Q_1/x^2=Q_2/(a-x)^2$ con $a=6$ cm. De ahí $2/x=1/(a-x)$, es decir, $x=\frac23a=4$ cm. (c) En general, $x=a/(1+\sqrt{Q_2/Q_1})$. Para $Q_2\to0$, $x\to a$: el punto se desplaza al lugar de $Q_2$ y desaparece: una sola carga no tiene ningún punto sin campo.
:::
:::
