---
title: Etapa 3: El AO sin realimentación
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El amplificador operacional
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Capítulo 11: El amplificador operacional
order: 1210500
summary: Las etapas amplificadoras se convierten en un componente con pocos terminales.
tags: saturación, AO ideal, convertidor flash
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Las etapas amplificadoras se convierten en un componente con pocos terminales. Esta etapa fija su modelo y muestra qué hace sin circuito externo: compara.
:::

**La idea.** El AO tiene dos entradas, una salida y dos terminales para la alimentación, $U_\mathrm{B+}$ y $U_\mathrm{B-}$ (fig. [3](#abb-3)). No tiene terminal de masa: la salida se refiere al punto medio de la alimentación. Toda corriente de salida procede de los terminales de alimentación, que en los esquemas suelen omitirse. Por eso, los tres terminales visibles no cumplen la ley de los nudos.

La salida entrega $A$ veces $U_\mathrm{D}$, pero solo hasta sus límites. Con $\pm11$ V y $A=100000$, el tramo lineal termina ya en $\pm110$ µ V. Cualquier diferencia mayor lleva la salida a un tope, la __saturación__.

:::definition Definición 3.1 (Modelo del AO)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D}=\varphi_+-\varphi_-,\qquad U_\mathrm{A}=\begin{cases}U_\mathrm{A,max}&\text{para }A\,U_\mathrm{D}\ge U_\mathrm{A,max},\\A\,U_\mathrm{D}&\text{entre ambos},\\U_\mathrm{A,min}&\text{para }A\,U_\mathrm{D}\le U_\mathrm{A,min}.\end{cases} \tag{3.1}$$

El __AO ideal__ tiene $r_\mathrm{e}\to\infty$ (sin corriente de entrada), $A\to\infty$ a todas las frecuencias, $r_\mathrm{a}=0$ (la corriente de salida se ajusta de modo que se cumplan todas las ecuaciones de nudos y de mallas) y ningún ruido.
:::

⁠**Cómo leerlo:** $U_\mathrm{A,max}<U_\mathrm{B+}$ y $U_\mathrm{A,min}>U_\mathrm{B-}$, porque entre la salida y la alimentación hay transistores en los que cae tensión, aquí 1 V en cada uno. **Validez:** El modelo es estático; la inercia de la salida se trata en la etapa [4](gegenkopplung.html#stufe-4).

:::abbildung et1/k11opv 3
A la izquierda, el símbolo con los terminales de alimentación. A la derecha, la curva característica en el modelo de referencia. La pendiente es $A$, y el tramo lineal solo tiene $\pm110$ µ V de ancho. Fíjate en el eje: con una escala en voltios sería un escalón vertical.
:::

**El comparador.** Sin realimentación, $|U_\mathrm{D}|$ es casi siempre mayor que la ventana. El AO solo indica entonces qué entrada está más alta: $U_\mathrm{A,max}$ para $\varphi_+>\varphi_-$, $U_\mathrm{A,min}$ para $\varphi_+<\varphi_-$. Esto es el comparador. Una aplicación es el __convertidor flash__, un convertidor analógico-digital (fig. [4](#abb-4)). Un divisor de tensión genera tensiones de comparación, y cada comparador compara $U_\mathrm{E}$ con una de ellas. Todos trabajan a la vez, de ahí el nombre (flash, destello). $n$ bits necesitan $2^n-1$ comparadores; 8 bits, por tanto, 255.

:::abbildung et1/k11flash 4
Convertidor flash de 2 bits con $U_\mathrm{Ref}=6$ V y resistencias iguales. Las entradas no toman corriente, las resistencias están en serie y las tomas están a 6, 4 y 2 V. Con $U_\mathrm{E}=3{,}2$ V solo K3 conmuta hacia arriba.
:::

::::beispiel
Con $U_\mathrm{E}=3{,}2$ V es $U_\mathrm{D}=-2{,}8$ V en K1, $-0{,}8$ V en K2 y $+1{,}2$ V en K3. K1 y K2 están en $-11$ V; K3, en $+11$ V. Las tres salidas distinguen cuatro rangos: por debajo de 2 V, de 2 a 4 V, de 4 a 6 V, por encima de 6 V.
::::

⁠**Caso límite:** Para $A\to\infty$, la ventana se convierte en un punto y la curva característica en un escalón en $U_\mathrm{D}=0$.

:::aufgabe Ejercicio 3 ★ Comparadores
<span class="anker" id="aufg-3"></span>

(a) Un convertidor flash como el de la fig. [4](#abb-4) tiene $U_\mathrm{Ref}=9$ V. ¿Dónde están las tomas? ¿Qué comparadores están arriba con $U_\mathrm{E}=4$ V? (b) ¿Cuántos comparadores hacen falta para 3 bits? (c) En el AO V hay $U_\mathrm{D}=50$ µ V y luego 300 µ V. ¿Cuánto vale $U_\mathrm{A}$ en cada caso?

:::loesung
(a) 9, 6 y 3 V. Con 4 V, solo en K3 es $U_\mathrm{D}>0$ ($+1$ V); K1 y K2 tienen $-5$ V y $-2$ V. (b) $2^3-1=7$. (c) 5 V dentro de la ventana. Con 300 µ V serían 30 V; la salida está en 11 V.
:::
:::
