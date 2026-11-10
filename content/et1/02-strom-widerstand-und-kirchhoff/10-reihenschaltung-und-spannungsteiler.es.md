---
title: Etapa 9: Conexión en serie y divisor de tensión
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1121000
summary: Muchas redes se componen de dos patrones básicos.
tags: conexión en serie, resistencia total, sin carga, convertidor digital-analógico, bits, búfer, comparador, decodificador
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Muchas redes se componen de dos patrones básicos. Esta etapa agrupa resistencias en serie, muestra cómo se reparte la tensión y construye con ello un convertidor.
:::

**La idea.** Entre las resistencias no se deriva nada; la ley de los nudos impone la misma corriente en todas. El punto medio se ajusta al potencial en el que eso se cumple. La misma corriente necesita más impulso en una resistencia mayor: el campo realiza allí más trabajo por unidad de carga, y en ella cae más tensión.

:::satz Teorema 9.1 (Conexión en serie y divisor de tensión)
<span class="anker" id="satz-9-1"></span>

Para $N$ resistencias en __conexión en serie__ se cumple

<span class="anker" id="gl-9-1"></span>
<span class="anker" id="gl-9-2"></span>
$$\begin{aligned} I&=I_1=I_2=\dots=I_N,\qquad U=U_1+U_2+\dots+U_N,\qquad U_i=R_i\,I,\\ R_\mathrm{tot}&=\sum_{i=1}^{N}R_i,\qquad\frac{U_\nu}{U}=\frac{R_\nu}{\sum_{i=1}^NR_i}, \end{aligned} \tag{9.1|9.2}$$

para dos resistencias, por tanto, la regla del divisor de tensión

<span class="anker" id="gl-9-3"></span>
$$\frac{U_2}{U}=\frac{R_2}{R_1+R_2},\qquad\frac{U_1}{U_2}=\frac{R_1}{R_2}. \tag{9.3}$$
:::

⁠**Cómo leerlo:** $R_\mathrm{tot}$ es la __resistencia total__, la única resistencia que sustituye a la cadena. Las tensiones guardan la misma relación que las resistencias. **Validez:** La regla del divisor solo vale __sin carga__: en la toma no se debe extraer corriente, de lo contrario $I_1\neq I_2$ (etapa [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10)).

:::herleitung Resistencia total y regla del divisor
La ley de las mallas da $U=\sum U_i$, la ley de Ohm $U_i=R_i\,I$ con la misma $I$. Por tanto, $U=(R_1+\dots+R_N)\,I$. En el cociente de $U_\nu=R_\nu\,I$ y $U$ se cancela $I$.
:::

::::beispiel
La cadena tiene $R_\mathrm{tot}=3\,\mathrm{k\Omega}$, es decir, $I=3$ mA, $U_1=6$ V y $U_2=3$ V (fig. [10](#abb-10), izquierda). De [(9.3)](#gl-9-3): $U_2=9\,\mathrm{V}\cdot1/3=3$ V.
::::

⁠**Casos límite:** $R_2\to0$ da $U_2\to0$: un cortocircuito no soporta tensión. $R_2\to\infty$ da $U_2\to U$: un punto abierto soporta toda la tensión. $R_1=R_2$ reduce $U$ a la mitad.

:::abbildung et1/k2teiler 10
Izquierda: el divisor de tensión del modelo de referencia. Centro: cadena de un convertidor de 3 bits con $U_\mathrm{ref}=3{,}2$ V. Los extremos $R/2$ desplazan todas las tomas medio escalón. Derecha: salida frente al número $Z$. La escalera está centrada alrededor de la recta ideal discontinua; el error es como máximo de medio escalón.
:::

**Aplicación: convertidor digital-analógico.** Un __convertidor digital-analógico__ (convertidor D/A) convierte un número en una tensión. Tres __bits__ (dígitos binarios $b_0$, $b_1$, $b_2$) dan los números $Z=0$ a 7. Una cadena de $R/2$, siete $R$ y $R/2$ tiene la resistencia total $8R$ y divide $U_\mathrm{ref}$ en ocho escalones. En las tomas hay

<span class="anker" id="gl-9-4"></span>
$$U_Z=\Bigl(Z+\frac12\Bigr)\frac{U_\mathrm{ref}}{8}. \tag{9.4}$$

Un árbol de interruptores, con un nivel por bit, deja pasar exactamente una toma. Un __búfer__, un amplificador de factor 1, entrega la tensión sin extraer corriente de la cadena, para que el divisor siga sin carga. Con $U_\mathrm{ref}=3{,}2$ V, el escalón es de 0,4 V, y $Z=5$ da 2,2 V.

**Aplicación: convertidor analógico-digital flash.** La misma cadena funciona también a la inversa. Un __comparador__, un dispositivo que indica cuál de dos tensiones es mayor, compara la tensión de entrada con cada toma, todas a la vez. Un __decodificador__, un circuito lógico, convierte las indicaciones en el número de tres bits. Para los números 0 a 7 bastan siete umbrales, aquí de 0,2 a 2,6 V. Un octavo umbral puede indicar un desbordamiento. Con 1,3 V hay tres umbrales por debajo; el convertidor da $Z=3$, es decir, $3\cdot0{,}4\,\mathrm{V}=1{,}2$ V, el múltiplo del escalón más cercano.

:::frage ¿No frena la primera resistencia la corriente, de modo que a la segunda llega menos?
No, la corriente no se gasta (etapa [1](strom-ist-bewegte-ladung.html#stufe-1)). Los electrones no se acumulan delante de $R_2$: de lo contrario, el punto medio se cargaría hasta que ambas corrientes fueran iguales. $R_2$ actúa sobre todo el circuito, porque la única corriente común queda fijada por $R_1+R_2$.
:::

:::aufgabe Ejercicio 9 ★ Diseñar un divisor
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

De 12 V deben obtenerse 3,3 V, con $R_2=3{,}3\,\mathrm{k\Omega}$. Calcula $R_1$. ¿Qué valores E24 (8,2 y 9,1 k$\Omega$) hay al lado y qué tensión dan?

</li>

<li>

Una cadena de $1$, $2$, $3$ y $6\,\mathrm{k\Omega}$ está conectada a 24 V. Da la corriente y las tensiones parciales.

</li>

<li>

Un convertidor de 3 bits tiene $U_\mathrm{ref}=5$ V. ¿Qué tensión entrega con $Z=6$?

</li>

</ol>

:::loesung
(a) $R_1=R_2\,(12-3{,}3)/3{,}3=8{,}7\,\mathrm{k\Omega}$. Con $8{,}2\,\mathrm{k\Omega}$ resultan 3,44 V ($+4{,}3\,\%$), con $9{,}1\,\mathrm{k\Omega}$, 3,19 V ($-3{,}2\,\%$). (b) $R_\mathrm{tot}=12\,\mathrm{k\Omega}$, $I=2$ mA, tensiones parciales 2, 4, 6 y 12 V. (c) $U_6=6{,}5\cdot5\,\mathrm{V}/8=4{,}06$ V.
:::
:::
