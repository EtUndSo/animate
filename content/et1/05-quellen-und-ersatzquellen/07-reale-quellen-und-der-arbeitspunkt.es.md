---
title: Etapa 5: Fuentes reales y el punto de trabajo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1150700
summary: Una batería no mantiene su tensión bajo carga.
tags: circuito equivalente, fuente de tensión real, fuente de corriente real, recta de carga, punto de trabajo
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Una batería no mantiene su tensión bajo carga. Esta etapa muestra por qué y halla el punto de la curva característica que establece una carga.
:::

**La idea.** En una batería, la química impulsa la carga y aporta para ello una energía fija por culombio, la tensión de fuente. Pero la corriente tiene que atravesar la propia batería: los iones migran por la solución electrolítica, los electrones por los electrodos y las conexiones. En ese recorrido se pierde energía en forma de calor, igual que en una resistencia. En los terminales solo queda el resto. Cuanto mayor es la corriente, más cae en el interior. Esta caída es proporcional a la corriente, así que la curva característica es una recta descendente.

:::abbildung et1/k5arbeitsgerade 6
A la izquierda, la fuente de tensión real con una carga. A la derecha, la curva característica de la fuente (azul) desde circuito abierto hasta cortocircuito y la recta de carga de cada carga. La intersección es el punto de trabajo: con 16 $\Omega$ en 0,5 A y 8 V, con 2 $\Omega$ en 2,25 A y 4,5 V.
:::

:::definition Definición 5.1 (Fuentes reales)
<span class="anker" id="satz-5-1"></span>

Un __circuito equivalente__ es un circuito de elementos ideales que en los terminales se comporta como el componente real. La __fuente de tensión real__ es una fuente de tensión ideal en serie con $R_\mathrm{q}$; la __fuente de corriente real__, una fuente de corriente ideal en paralelo con $G_\mathrm{q}$:

<span class="anker" id="gl-5-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}, \qquad\qquad I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}. \tag{5.1}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{q}$ es la tensión de circuito abierto. $R_\mathrm{q}$ es la resistencia interna o de fuente en $\Omega$: unos 2 $\Omega$ en una batería de 9 V, 10 m$\Omega$ en una batería de coche. $I_\mathrm{q}$ es la corriente de cortocircuito; $G_\mathrm{q}$, la conductancia de fuente en S. La primera ecuación es la ley de las mallas en el circuito equivalente; la segunda, la ley de los nudos: de $I_\mathrm{q}$ se deriva $G_\mathrm{q}U_\mathrm{AB}$, y el resto sale al exterior. **Validez:** La recta vale mientras $R_\mathrm{q}$ no dependa de la corriente. Las baterías reales se desvían con corrientes grandes y con la edad.

**La recta de carga.** Una carga impone una segunda ecuación, $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$. Esta recta que pasa por el origen se llama __recta de carga__. Ambas ecuaciones deben cumplirse a la vez. Eso solo es posible en la intersección, el __punto de trabajo__. Igualar $U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}=R_\mathrm{L}I_\mathrm{A}$ da:

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}},\qquad U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}. \tag{5.2}$$

El mecanismo detrás: si la fuente entregara más corriente de la que toma la carga, se acumularía carga en el terminal A y su potencial subiría. Entonces bajaría la corriente de la fuente y subiría la corriente de la carga. Esto continúa hasta que ambas corrientes son iguales.

::::beispiel
Con 16 $\Omega$ son $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0{,}5$ A y $U_\mathrm{AB}=8$ V, y en el interior cae 1 V. Con 2 $\Omega$ son 2,25 A y 4,5 V. Ambos puntos están en la recta: $9\,\mathrm{V}-2\,\Omega\cdot2{,}25\,\mathrm{A}=4{,}5$ V. Su separación muestra la resistencia interna como pendiente: $\Delta U_\mathrm{AB}/\Delta I_\mathrm{A}=3{,}5\,\mathrm{V}/(-1{,}75\,\mathrm{A})=-2\,\Omega$.
::::

⁠**Casos límite:** Para $R_\mathrm{L}\to\infty$, [(5.2)](#gl-5-2) da el circuito abierto $U_\mathrm{AB}=U_\mathrm{q}$; para $R_\mathrm{L}\to0$, la corriente de cortocircuito $I_\mathrm{CC}=U_\mathrm{q}/R_\mathrm{q}=4{,}5$ A. Para $R_\mathrm{q}\to0$ queda la fuente de tensión ideal. También una carga no lineal se puede tratar así: su curva característica es entonces una curva, y la intersección sigue siendo la solución ([Parte 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::ltspice La curva característica de la batería
⁠**Esquema:** `voltage` con 9 de `q` a masa, `res` con 2 de `q` a `a`. Como carga, una fuente de corriente `current` llamada `I1` de `a` a masa.

⁠**Directiva:** `.dc I1 0 4.5 0.05`

⁠**Lo que ves:** `V(a)` baja en línea recta de 9 V con 0 A a 0 V con 4,5 A. Con 0,5 A marca 8 V, con 2,25 A marca 4,5 V, los puntos de la fig. [6](#abb-6). Para el ejercicio [6](#aufg-6), ajusta los valores 12.6 y 0.01 y simula hasta 200 A (`.dc I1 0 200 1`). Con 150 A y con 20 A lees tus tensiones en los terminales.
:::

:::frage ¿Por qué el instrumento marca 9 V en una batería aunque tenga 2 $\Omega$ en su interior?
Porque casi no consume corriente ([Parte 4](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). Con 10 M$\Omega$ de resistencia de entrada circulan 0,9 µ A, y en el interior caen 1,8 µ V. Se mide prácticamente el circuito abierto. La resistencia interna solo se aprecia bajo carga.
:::

:::aufgabe Ejercicio 6 ★ Las luces durante el arranque
<span class="anker" id="aufg-6"></span>

Una batería de coche tiene 12,6 V y 10 m$\Omega$. El motor de arranque actúa como 74 m$\Omega$. (a) Calcula la corriente y la tensión en los terminales durante el arranque. (b) ¿Cuánto valdría la corriente de cortocircuito? (c) Las luces solas consumen 20 A. ¿Cuánto vale entonces la tensión en los terminales, y qué resistencia tienen, por tanto? (d) ¿Cuánto vale la tensión en los terminales cuando funcionan a la vez las luces y el motor de arranque? ¿Por qué se atenúan las luces?

:::loesung
(a) $I_\mathrm{A}=12{,}6\,\mathrm{V}/84\,\mathrm{m\Omega}=150$ A, $U_\mathrm{AB}=12{,}6\,\mathrm{V}-10\,\mathrm{m\Omega}\cdot150\,\mathrm{A}=11{,}1$ V.

(b) $I_\mathrm{CC}=12{,}6\,\mathrm{V}/10\,\mathrm{m\Omega}=1260$ A.

(c) $U_\mathrm{AB}=12{,}6\,\mathrm{V}-0{,}2\,\mathrm{V}=12{,}4$ V, es decir, $R=12{,}4\,\mathrm{V}/20\,\mathrm{A}=0{,}62\,\Omega$.

(d) Luces y motor de arranque en paralelo: $0{,}62\,\Omega\parallel74\,\mathrm{m\Omega}=66{,}1\,\mathrm{m\Omega}$. Divisor de tensión con 10 m$\Omega$: $U_\mathrm{AB}=10{,}94$ V. La batería entrega 165,6 A, y las luces reciben 17,65 A en lugar de 20 A. La gran corriente del motor de arranque produce en el interior una caída de 1,66 V, que también notan las luces. Su potencia baja de 248 W a 193 W.
:::
:::
