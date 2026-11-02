---
title: Etapa 10: Convolución sin ningún sistema
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas LTI y convolución
order: 3211100
summary: Por qué la respuesta a un único impulso describe todo el sistema
tags: 
lang: es
---

<span class="anker" id="stufe-10"></span>

:::frage La convolución tiene sentido cuando una señal pasa de verdad por un sistema. ¿Qué significa cuando no hay ningún sistema en juego?
La convolución es una operación de cálculo con un significado propio y general: *para cada forma de repartir un resultado en dos partes, se multiplican los pesos de ambas partes y se suma sobre todos los repartos.* El sistema es una interpretación de esto (primera parte: cuándo llegó el impulso; segunda parte: qué edad tiene), no la única.

⁠**Ejemplo sin sistema y sin tiempo: dos dados.** ¿Con qué probabilidad la suma de los dados es $k$? Cada reparto $k=i+(k-i)$ contribuye con la probabilidad $P_1(i)\,P_2(k-i)$:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

Esto es una convolución, con exactamente la misma estructura que $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ corresponde a los puntos del primer dado, $t$ a la suma y $t-\tau$ a los puntos del segundo. Dos dados con distribución uniforme («rectángulos») dan una distribución triangular, exactamente como $\operatorname{rect}*\operatorname{rect}=\Lambda$ en el ejercicio [5](die-faltung-ausrechnen.html#aufg-5). El 7 es el resultado más frecuente porque tiene más repartos (fig. [9](#abb-9)).

Otros ejemplos: una media móvil sobre valores medidos es una convolución con un rectángulo. Una foto desenfocada es la imagen nítida convolucionada con la mancha de luz que la óptica forma a partir de un punto. Y quien multiplica dos polinomios convoluciona sus coeficientes (ejercicio [11](#aufg-11)).
:::

:::abbildung et3/k1wuerfel 9
Probabilidades de la suma de los dados. Cada distribución es la convolución de la anterior con la de un solo dado. El rectángulo se convierte en un triángulo ($P(7)=6/36$), y este, en una curva acampanada ($P(10)=P(11)=27/216$).
:::

:::zusatz Por qué aparecen convoluciones tan a menudo
Si se convolucionan cada vez más distribuciones iguales, el resultado se aproxima a una curva de Gauss, casi con independencia de la forma de partida (teorema central del límite). Por eso el ruido, la suma de muchas influencias pequeñas e independientes, sigue tan a menudo una distribución gaussiana.
:::

:::aufgabe Ejercicio 11 ★ Convolución con dados y polinomios
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Calcula $P(7)$ y $P(4)$ para dos dados a partir de la suma de convolución. ¿Qué repartos contribuyen en cada caso?

</li>

<li>

Calcula $P(10)$ para tres dados convolucionando la distribución de dos con la de uno.

</li>

<li>

Desarrolla $(1+2x)(3+x)$. Demuestra que la sucesión de coeficientes del resultado es la convolución de las sucesiones $(1,2)$ y $(3,1)$.

</li>

</ol>

:::loesung
(a) $P(7)$: repartos $1+6,\,2+5,\dots,6+1$, seis en total, cada uno con $\frac16\cdot\frac16$: $P(7)=\frac{6}{36}=\frac16$. $P(4)$: $1+3,\,2+2,\,3+1$: $\frac{3}{36}=\frac{1}{12}$.

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$.

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$. El coeficiente de $x^k$ reúne todos los pares de potencias con $i+j=k$: $c_0=1\cdot3=3$, $c_1=1\cdot1+2\cdot3=7$, $c_2=2\cdot1=2$. Esta es la suma de convolución $c_k=\sum_ia_ib_{k-i}$, la misma estructura que en los dados.
:::
:::
