---
title: Etapa 1: De la red de 4 polos al cuadripolo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1160300
summary: Una red con cuatro terminales tiene tres corrientes independientes y tres tensiones independientes.
tags: red de 4 polos, magnitudes de puerto, teoría de cuadripolos, entrada, salida, sentido directo, sentido inverso, cuadripolos elementales
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Una red con cuatro terminales tiene tres corrientes independientes y tres tensiones independientes. Esta etapa muestra qué condición convierte esto en dos corrientes y dos tensiones.
:::

**La idea.** Una __red de 4 polos__ es una red con cuatro terminales. Para toda la red vale la ley de los nudos ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) como para un gran nudo: una corriente de terminal queda fijada por las otras tres. La ley de las mallas liga del mismo modo las tensiones entre los terminales. Si ahora se conecta a los terminales 1 y 1$'$ un dipolo, por ejemplo una fuente, se añade un dato: un dipolo solo tiene dos conexiones. Toda carga que entrega por una la recoge por la otra. La corriente que entra en la red por el terminal 1 debe volver por el terminal 1$'$. El par de terminales se comporta como un único acceso con una corriente y una tensión (fig. [1](#abb-1), izquierda).

:::definition Definición 1.1 (Red de 4 polos, puerto, cuadripolo)
<span class="anker" id="satz-1-1"></span>

En una red de 4 polos con los terminales 1, 1$'$, 2, 2$'$, cuéntense todas las corrientes de terminal hacia la red. Siempre se cumple

<span class="anker" id="gl-1-1"></span>
$$I_1+I_{1'}+I_2+I_{2'}=0,\qquad U_{11'}+U_{1'2'}-U_{22'}+U_{21}=0. \tag{1.1}$$

Un par de terminales es un puerto si se cumple la condición de puerto. Una red de 4 polos con dos puertos es un cuadripolo:

<span class="anker" id="gl-1-2"></span>
$$I_{1'}=-I_1,\qquad I_{2'}=-I_2. \tag{1.2}$$

Sus __magnitudes de puerto__ son $U_1=U_{11'}$, $I_1$, $U_2=U_{22'}$ e $I_2$.
:::

⁠**Cómo leerlo:** [(1.1)](#gl-1-1) deja libres tres corrientes y tres tensiones. La primera ecuación es la ley de los nudos; la segunda, la ley de las mallas en el recorrido $1\to1'\to2'\to2\to1$. [(1.2)](#gl-1-2) quita una corriente en cada caso. También la tensión $U_{1'2'}$ desaparece de la descripción: entre los puertos no circula corriente por fuera, así que a través de ella no se transfiere potencia. Si una red de 4 polos se convierte en cuadripolo lo decide lo que se le conecta: si en cada par de terminales hay un dipolo, [(1.2)](#gl-1-2) se cumple por sí sola. Una rama exterior de puerto a puerto la rompe (fig. [1](#abb-1), derecha). El nombre histórico de cuatro polos sigue vivo en la __teoría de cuadripolos__.

:::abbildung et1/k6tor 1
Izquierda: fuente, cuadripolo y carga. En ambos puertos, cada corriente vuelve por el segundo terminal, y la energía fluye en sentido directo del puerto 1 al puerto 2. Derecha: una rama exterior del terminal 1 al terminal 2 lleva la corriente $I_\mathrm{x}$. Ahora entra por 1 una corriente distinta de la que sale por 1$'$, y los pares de terminales ya no son puertos.
:::

Un cuadripolo es una unidad conceptualmente cerrada, accesible solo a través de sus puertos. Sus propiedades quedan fijadas por las relaciones entre las magnitudes de puerto, y estas se pueden calcular o medir. Normalmente, en el puerto 1, la __entrada__, hay una fuente y en el puerto 2, la __salida__, una carga. La energía fluye entonces en el __sentido directo__ $1\to2$; el sentido contrario se llama __sentido inverso__. El cuadripolo es una estructura básica: las fuentes controladas son cuadripolos; el transformador, el amplificador y el transistor tienen tres o cuatro conexiones; los cuadripolos grandes se pueden construir a partir de __cuadripolos elementales__, y los cuadripolos unidos forman de nuevo un cuadripolo. Los ejemplos más sencillos son el divisor de tensión y el divisor de corriente ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

**Estructura y clasificación.** Si un cuadripolo tiene una línea continua del terminal 1$'$ al 2$'$, la __línea de masa__, se llama __asimétrico respecto a masa__ (fig. [2](#abb-2), izquierda). En realidad es un tripolo, una red de 4 polos impropia. Los modelos de red de transistores y amplificadores son de este tipo. Un cuadripolo que, como el circuito en puente, no tiene tal línea y está construido en espejo respecto a una línea central se llama __simétrico respecto a masa__. Por su comportamiento, los cuadripolos se dividen en lineales invariantes en el tiempo, variables en el tiempo y no lineales. Este capítulo trata los lineales invariantes en el tiempo.

:::abbildung et1/k6masse 2
Izquierda: el cuadripolo T del modelo de referencia es asimétrico respecto a masa; en rojo, la línea de masa de 1$'$ a 2$'$. Derecha: el circuito en puente de dos pares de resistencias no tiene línea continua entre los puertos; es simétrico respecto a masa. La etapa [3](impedanzform-und-leerlaufversuch.html#stufe-3) calcula ambos.
:::

**Ejemplo.** En el funcionamiento del cuadripolo T (etapa [4](das-zweitor-im-betrieb.html#stufe-4)) entran $I_1=250$ mA e $I_{1'}=-250$ mA; la carga toma 50 mA, es decir, $I_2=-50$ mA e $I_{2'}=+50$ mA. La suma en [(1.1)](#gl-1-1) es cero. **Caso límite:** Si el puerto 2 está abierto, $I_2=I_{2'}=0$, y hacia fuera el cuadripolo actúa como un dipolo en el puerto 1.

:::frage La línea de masa une 1$'$ y 2$'$. ¿No circula ahí, después de todo, corriente de puerto a puerto?
Sí, en el interior. Por la línea de masa del cuadripolo T circulan 50 mA de 2$'$ al pie de $R_\mathrm{b}$. Pero la condición de puerto solo dice lo que ocurre en los terminales. Dentro puede circular cualquier corriente, siempre que cada corriente de terminal vuelva por su terminal pareja.
:::

:::aufgabe Ejercicio 1 ★ Contar en los terminales
<span class="anker" id="aufg-1"></span>

En una red de 4 polos mides $I_1=30$ mA, $I_{1'}=-30$ mA, $I_2=-10$ mA, y además $U_{11'}=6$ V, $U_{1'2'}=0$ V, $U_{22'}=2$ V.

<ol class="al">

<li>

¿Cuánto vale $I_{2'}$? ¿Son puertos ambos pares de terminales?

</li>

<li>

¿Cuánto vale $U_{21}$?

</li>

<li>

¿Cuántas corrientes tendrías que medir como mínimo para conocer todas las corrientes de terminal, en la red de 4 polos y en el cuadripolo?

</li>

</ol>

:::loesung
(a) De [(1.1)](#gl-1-1): $I_{2'}=-(30-30-10)\,\mathrm{mA}=+10$ mA. Se cumplen $I_{1'}=-I_1$ e $I_{2'}=-I_2$; ambos pares son puertos. (b) $U_{21}=-U_{11'}-U_{1'2'}+U_{22'}=-6\,\mathrm{V}-0\,\mathrm{V}+2\,\mathrm{V}=-4$ V. (c) En la red de 4 polos, tres; la cuarta se obtiene de la ley de los nudos. En el cuadripolo, dos; las demás se obtienen de la condición de puerto.
:::
:::
