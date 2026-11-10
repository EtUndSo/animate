---
title: Etapa 1: La corriente es carga en movimiento
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1120200
summary: El capítulo 1 trató cargas en reposo o que vuelan por separado.
tags: densidad de carga, intensidad de corriente, circuito, estacionaria
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
El [capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) trató cargas en reposo o que vuelan por separado. En un hilo se mueven juntas innumerables cargas. Esta etapa da a ese movimiento dos medidas.
:::

**La idea.** Uno se coloca en un punto del conductor y mide cuánta carga pasa por segundo. Eso depende de tres cosas: la densidad con que está la carga, la rapidez con que avanza y el tamaño de la sección. En el tiempo $\Delta t$ atraviesa el área exactamente la carga que antes estaba, como máximo, a la distancia $v\,\Delta t$ (fig. [1](#abb-1)).

:::abbildung et1/k2strom 1
Portadores de carga con la velocidad $v$ en un conductor. Toda la carga del tramo sombreado atraviesa el área $A$ en el tiempo $\Delta t$. El tramo tiene el volumen $A\,v\,\Delta t$.
:::

:::definition Definición 1.1 (Corriente y densidad de corriente)
<span class="anker" id="satz-1-1"></span>

La __densidad de carga__ $q=\Delta Q/\Delta V$ es la carga por unidad de volumen. La __intensidad de corriente__ (en breve, corriente) es la carga que atraviesa un área por unidad de tiempo. La densidad de corriente es la corriente por unidad de área:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} i&=\lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t}=\frac{\mathrm{d} Q}{\mathrm{d} t},\qquad I=q\,v\,A,\qquad [I]=\mathrm{C/s}=\mathrm A,\\ j&=\frac IA=q\,v,\qquad\vec j=q\,\vec v. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**Cómo leerlo:** $i$ es la corriente dependiente del tiempo, $I$ la constante, en amperios: 3 mA en el modelo de referencia, 20 mA en un diodo luminoso, 16 A en una línea doméstica. $q$ tiene la unidad $\mathrm{C/m^3}$. Para los electrones libres del cobre, $q=-n\,e=-1{,}36\cdot10^{10}\,\mathrm{C/m^3}$. $j$ tiene la unidad $\mathrm{A/m^2}$; las líneas domésticas llevan unos $10\,\mathrm{A/mm^2}$. El vector $\vec j$ apunta en el sentido de $\vec v$ para $q>0$ y en sentido contrario para $q<0$. **Validez:** $I=q\,v\,A$ supone que $q$ y $v$ son iguales en toda $A$ y que $v$ es perpendicular a $A$.

:::herleitung Corriente a partir de densidad y velocidad
Sea el área $A=\Delta x\,\Delta y$. El tramo sombreado tiene el volumen $\Delta V=\Delta x\,\Delta y\,\Delta z$ con $\Delta z=v\,\Delta t$. Contiene la carga $\Delta Q=q\,\Delta V=q\,A\,v\,\Delta t$, que atraviesa $A$ en el tiempo $\Delta t$. Por tanto, $\Delta Q/\Delta t=q\,v\,A$.
:::

**¿Cuándo circula corriente de forma permanente?** Deben cumplirse dos condiciones. Primero, el circuito necesita una fuente, por ejemplo una batería o una fuente de alimentación. Aporta energía, no carga: los portadores de carga ya están en el conductor; la fuente solo los impulsa alrededor del circuito. Segundo, el __circuito__ debe estar cerrado, es decir, ser un camino que vuelve sobre sí mismo. De lo contrario, en una interrupción se acumula carga, su campo anula el campo impulsor y la corriente cesa. Una corriente constante en el tiempo en un circuito cerrado se llama __estacionaria__.

::::beispiel
En el modelo de referencia pasan por el hilo 3 mC por segundo, es decir, $3\,\mathrm{mC}/e=1{,}87\cdot10^{16}$ electrones. La densidad de corriente es $j=3\,\mathrm{mA}/0{,}5\,\mathrm{mm^2}=6\,\mathrm{mA/mm^2}$. Un metro de hilo contiene la carga libre $n\,e\,A=6800$ C. Toda la carga que una batería rectangular mueve durante su vida (unos 1800 C) está, por tanto, ya en 26 cm de este hilo. **Comprobación:** Para $v=0$, $I=0$, sea cual sea la carga que hay en el hilo. El doble de área con la misma $v$ da el doble de corriente, porque son dos hilos uno junto a otro.
::::

:::frage ¿Se gastan los electrones en el receptor?
No. La carga se conserva: de un componente salen por segundo tantos electrones como entran. Lo que se gasta es energía: cada culombio cede al componente su energía por unidad de carga, la tensión, y sigue con un potencial más bajo.
:::

:::aufgabe Ejercicio 1 ★ Corriente, carga, densidad de corriente
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Un diodo luminoso conduce 20 mA durante 5 min. ¿Cuánta carga lo atraviesa y cuántos electrones son?

</li>

<li>

Un cable de $1{,}5\,\mathrm{mm^2}$ de sección conduce 16 A. ¿Cuánto vale $j$ en $\mathrm{A/mm^2}$?

</li>

<li>

¿Hacia dónde apunta $\vec j$ en un hilo en el que los electrones avanzan hacia la derecha?

</li>

</ol>

:::loesung
(a) $Q=I\,t=20\,\mathrm{mA}\cdot300\,\mathrm{s}=6$ C, es decir, $6\,\mathrm{C}/e=3{,}7\cdot10^{19}$ electrones. (b) $j=16\,\mathrm{A}/1{,}5\,\mathrm{mm^2}=10{,}7\,\mathrm{A/mm^2}$. (c) Hacia la izquierda: para los electrones, $q<0$, así que $\vec j=q\,\vec v$ apunta contra $\vec v$.
:::
:::
