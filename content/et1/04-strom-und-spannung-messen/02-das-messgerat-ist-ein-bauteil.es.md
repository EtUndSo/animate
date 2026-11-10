---
title: Etapa 1: El instrumento es un componente
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Medir corriente y tensión
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Capítulo 4: Medir corriente y tensión
order: 1140200
summary: Antes de poder calcular un error, hay que tener claro qué es eléctricamente un instrumento de medida: un componente con dos terminales y una resistencia entre ellos.
tags: valor de fondo de escala
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Antes de poder calcular un error, hay que tener claro qué es eléctricamente un instrumento de medida: un componente con dos terminales y una resistencia entre ellos.
:::

**La idea.** En un instrumento de aguja, una bobina giratoria de hilo fino está situada entre los polos de un imán permanente (fig. [1](#abb-1)). Cuando circula corriente, el campo magnético ejerce una fuerza sobre los electrones en movimiento en el hilo, y la bobina gira contra un muelle en espiral. El par crece con la corriente; la fuerza opuesta del muelle, con el ángulo. Por eso, la desviación es proporcional a la corriente. Dos cosas no se pueden evitar: sin corriente no hay desviación, y con corriente cae tensión en el hilo. Un multímetro digital (aparato con indicación numérica) convierte en un número la tensión en una resistencia interna. También allí circula corriente por una resistencia.

:::abbildung et1/k4messwerk 1
A la izquierda, el mecanismo de medida: la bobina gira en el campo magnético contra un muelle (no dibujado). A la derecha, los circuitos equivalentes: instrumento ideal más resistencia interna, en serie o en paralelo.
:::

:::definition Definición 1.1 (Rango de medida y resistencia interna)
<span class="anker" id="satz-1-1"></span>

El rango de medida llega hasta el __valor de fondo de escala__, el mayor valor que se puede mostrar (en la aguja, la desviación a fondo de escala). La resistencia interna $R_\mathrm i$ es la resistencia entre los terminales.

<ul>

<li>

Un amperímetro se conecta en serie. Lo ideal es $R_\mathrm i=0$; en la realidad, aproximadamente $R_\mathrm i\approx1\,\Omega$.

</li>

<li>

Un voltímetro se conecta en paralelo. Lo ideal es $R_\mathrm i\to\infty$; en la realidad, aproximadamente $R_\mathrm i\approx10\,\mathrm{M\Omega}$.

</li>

</ul>
:::

⁠**Cómo leerlo:** La corriente es carga que atraviesa una sección. Por eso se abre el circuito y se hace pasar toda la corriente por el amperímetro. En él no debe caer tensión, así que $R_\mathrm i$ debe ser pequeña. La tensión es la diferencia entre dos puntos. Por eso se conecta el voltímetro a ambos puntos sin abrir el circuito. Por él no debe circular corriente, así que $R_\mathrm i$ debe ser grande. Los valores numéricos son típicos de los multímetros digitales. **Validez:** $R_\mathrm i$ vale para un rango de medida y cambia al conmutarlo (etapa [2](den-messbereich-erweitern.html#stufe-2)).

::::beispiel
El mecanismo de medida del modelo de referencia ya es ambas cosas. A fondo de escala circulan 50 µ A por 2 k$\Omega$, así que hay $U_\mathrm M=R_\mathrm MI_\mathrm M=100$ mV. La escala podría rotularse con 50 µ A o con 100 mV: dos nombres para la misma desviación.
::::

⁠**Caso límite:** Para $R_\mathrm i=0$, el amperímetro actúa como un trozo de cable; para $R_\mathrm i\to\infty$, el voltímetro actúa como un punto abierto. Para el circuito, los instrumentos ideales no existen.

:::frage Si por un voltímetro ideal no circula corriente, ¿cómo puede mostrar algo?
Una aguja no podría, porque sin corriente no hay desviación. El caso ideal es un límite, no un aparato. Una resistencia interna grande hace pequeña la corriente, no nula. Los aparatos digitales se conforman con muy poca corriente porque la energía para la indicación procede de su propia batería, no del circuito medido.
:::

:::aufgabe Ejercicio 1 ★ Mal conectado
<span class="anker" id="aufg-1"></span>

Predice primero qué aparato está en peligro. (a) El amperímetro del modelo de referencia se conecta por error directamente a la fuente de 9 V. ¿Qué corriente circula? (b) El voltímetro se conecta por error en serie con $R$ a la fuente. ¿Qué muestra y qué corriente circula?

:::loesung
(a) El amperímetro está en peligro, porque su pequeña resistencia apenas limita la corriente: $I=9\,\mathrm{V}/10\,\Omega=0{,}9$ A, noventa veces el rango. Por el mecanismo de medida circulan 4,5 mA en lugar de 50 µ A, y en el shunt se liberan 8,06 W.

(b) $I=9\,\mathrm{V}/201{,}8\,\mathrm{k\Omega}=44{,}6$ µ A. El voltímetro muestra $44{,}6\,\mu\text{A}\cdot200\,\mathrm{k\Omega}=8{,}92$ V; en $R$ quedan 80 mV. No se rompe nada, pero el circuito deja de funcionar.
:::
:::
