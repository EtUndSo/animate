---
title: Etapa 4: Tres regiones, tres circuitos equivalentes
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1200600
summary: Con funciones exponenciales, los circuitos apenas se pueden resolver a mano.
tags: región de corte, región de saturación, tensión umbral, tensión de saturación, circuito equivalente
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Con funciones exponenciales, los circuitos apenas se pueden resolver a mano. Esta etapa sustituye la superficie por tres tramos lineales.
:::

**La idea.** Cada uno de los dos diodos puede conducir o bloquear. De ahí resultan los estados de funcionamiento. Si el diodo BE bloquea, no arranca ningún electrón y no circula nada. Es la __región de corte__. Si conduce y el diodo CB bloquea, el colector recoge todos los electrones y se cumple $I_\mathrm{C}=B\,I_\mathrm{B}$. Es la región activa. Si $U_\mathrm{CE}$ baja tanto que también el diodo CB conduce claramente, el colector devuelve electrones. Entonces ya no puede recogerlos todos, la base se llena de electrones e $I_\mathrm{C}$ queda por debajo de $B\,I_\mathrm{B}$. Es la __región de saturación__. Como en el diodo ([Parte 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)), las curvas se sustituyen por rectas: la curva característica de entrada recibe un codo en 0,6 V, la de control por corriente pasa a ser una recta de pendiente $B$ que se dobla a horizontal en la saturación, y las de salida se hacen horizontales a la derecha de 0,2 V (fig. [6](der-arbeitspunkt.html#abb-6)).

:::definition Definición 4.1 (Regiones de funcionamiento del transistor npn)
<span class="anker" id="satz-4-1"></span>

Con la __tensión umbral__ $U_\mathrm{BE,on}=0{,}6$ V y la __tensión de saturación__ $U_\mathrm{CE,sat}=0{,}2$ V se cumple:

<span class="anker" id="gl-4-1"></span>
<span class="anker" id="gl-4-2"></span>
<span class="anker" id="gl-4-3"></span>
$$\begin{aligned} \text{región de corte:}\quad & U_\mathrm{BE}<U_\mathrm{BE,on}\;\Rightarrow\; I_\mathrm{B}=I_\mathrm{C}=0,\\ \text{región activa:}\quad & U_\mathrm{BE}=U_\mathrm{BE,on},\ I_\mathrm{B}>0,\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}\ge U_\mathrm{CE,sat},\\ \text{región de saturación:}\quad & U_\mathrm{BE}=U_\mathrm{BE,on},\ I_\mathrm{B}>0,\quad U_\mathrm{CE}=U_\mathrm{CE,sat},\quad I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.1|4.2|4.3}$$
:::

⁠**Cómo leerlo:** Cada región tiene un __circuito equivalente__ lineal de elementos ideales, válido entre B, C y E (fig. [5](#abb-5)). En la región de corte, todos los terminales están abiertos. En las dos regiones de conducción hay entre B y E una fuente de tensión de 0,6 V; entre C y E hay una fuente de corriente controlada en la región activa y una fuente de tensión de 0,2 V en la saturación. En el nudo común siempre se cumple $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$. **Validez:** una aproximación burda, pero acreditada. El umbral no es un verdadero interruptor (etapa [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2)); los 0,6 V aciertan para T con 2 mA, con 20 mA serían 0,66 V. El valor 0,2 V depende del tipo.

:::abbildung et1/k10esb 5
Los tres circuitos equivalentes del transistor npn. Izquierda, abierto en la región de corte; centro, con fuente de corriente controlada en la región activa; derecha, con dos fuentes de tensión en la saturación. En el nudo situado sobre E se unen $I_\mathrm{B}$ e $I_\mathrm{C}$.
:::

**Ejemplo.** Para T ($B=200$) se tiene: $I_\mathrm{B}=10$ µ A con $U_\mathrm{CE}=6$ V es activa, así que $I_\mathrm{C}=2$ mA. $I_\mathrm{B}=30$ µ A con $I_\mathrm{C}=3{,}9$ mA es saturación, porque $B\,I_\mathrm{B}=6$ mA es mayor que la corriente que permite el circuito. $U_\mathrm{BE}=0{,}3$ V es región de corte. **Caso límite:** para $B\,I_\mathrm{B}=I_\mathrm{C}$ y $U_\mathrm{CE}=U_\mathrm{CE,sat}$, el transistor está justo en el límite entre activa y saturación. Allí los dos circuitos equivalentes dan lo mismo.

:::frage ¿Por qué se llama saturación si precisamente la corriente deja de seguir?
Lo que se satura no es la corriente, sino la base: está sobrellena de electrones. Por eso, en el transistor bipolar, la palabra designa la parte abrupta a la izquierda de la curva característica de salida. En el MOSFET se llama saturación a la parte plana. Las dos palabras significan cosas distintas.
:::

**El transistor pnp.** En el transistor pnp, n y p están intercambiados (fig. [1](drei-schichten-zwei-spannungen.html#abb-1)). Los mecanismos son los mismos, pero los huecos asumen el papel de los electrones. El emisor está al potencial más alto, y todos los signos se invierten. Con las denominaciones del npn, ahora $U_\mathrm{BE,on}=-0{,}6$ V y $U_\mathrm{CE,sat}=-0{,}2$ V son negativas. Si $I_\mathrm{B}$ e $I_\mathrm{C}$ se cuentan hacia fuera del componente, ambas son positivas, y se cumple:

<span class="anker" id="gl-4-4"></span>
$$\begin{aligned} &\text{región de corte: } U_\mathrm{BE}>-0{,}6\,\mathrm{V};\qquad \text{activa: } I_\mathrm{C}=B\,I_\mathrm{B},\ U_\mathrm{CE}\le-0{,}2\,\mathrm{V};\\ &\text{saturación: } U_\mathrm{CE}=-0{,}2\,\mathrm{V},\ I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.4}$$

En la práctica, el transistor npn es más frecuente porque en el silicio los electrones son unas tres veces más móviles que los huecos. La forma pnp sirve sobre todo cuando el emisor debe estar en la alimentación positiva.

:::aufgabe Ejercicio 4 ★ Reconocer la región
<span class="anker" id="aufg-4"></span>

Determina la región de T y la corriente o la tensión que falta. (a) $I_\mathrm{B}=20$ µ A, $U_\mathrm{CE}=5$ V. (b) $I_\mathrm{B}=40$ µ A, $I_\mathrm{C}=3$ mA. (c) $U_\mathrm{BE}=-1$ V, $U_\mathrm{CE}=12$ V. (d) Un transistor pnp con $B=200$: $U_\mathrm{CE}=-5$ V e $I_\mathrm{B}=10$ µ A.

:::loesung
(a) $I_\mathrm{B}>0$ y $U_\mathrm{CE}>0{,}2$ V: activa, $I_\mathrm{C}=4$ mA. (b) $B\,I_\mathrm{B}=8$ mA $>3$ mA: saturación, $U_\mathrm{CE}=0{,}2$ V. (c) $U_\mathrm{BE}<0{,}6$ V: región de corte, $I_\mathrm{B}=I_\mathrm{C}=0$. (d) $U_\mathrm{CE}\le-0{,}2$ V e $I_\mathrm{B}>0$: activa, $I_\mathrm{C}=2$ mA, $U_\mathrm{BE}=-0{,}6$ V.
:::
:::
