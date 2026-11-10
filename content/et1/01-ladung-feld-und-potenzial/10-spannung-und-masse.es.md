---
title: Etapa 8: Tensión y masa
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1111000
summary: El valor de un potencial depende del punto de referencia; la diferencia de dos potenciales, no.
tags: tensión, masa, tierra, esquemas eléctricos, flecha de referencia, nudos
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
El valor de un potencial depende del punto de referencia; la diferencia de dos potenciales, no. Esta diferencia es la magnitud técnicamente importante. Esta etapa muestra cómo calcular con ella en un circuito.
:::

**La idea.** Sobre una carga solo actúa una fuerza si el potencial cambia con el lugar. Un potencial igual de alto en todas partes no produce nada, sea cual sea su valor. Por eso solo actúan las diferencias, y todo voltímetro tiene dos terminales. El cero se elige libremente: si un punto de un circuito se declara cero, cada uno de los demás puntos recibe un número. Si se desplaza el cero, todos los números se desplazan a la vez, y sus diferencias se mantienen.

:::definition Definición 8.1 (Tensión eléctrica y masa)
<span class="anker" id="satz-8-1"></span>

La __tensión__ entre $P_1$ y $P_2$ es

<span class="anker" id="gl-8-1"></span>
$$U_{12}=\varphi(P_1)-\varphi(P_2)=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\frac{W_{12}}{Q}, \tag{8.1}$$

con la unidad $[U]=[W]\cdot[Q]^{-1}=\mathrm{N\,m\,A^{-1}\,s^{-1}}=\mathrm{kg\,m^2\,A^{-1}\,s^{-3}}=\mathrm V$. El punto de un circuito al que se asigna $\varphi:=0$ V se llama __masa__ o potencial de referencia, en inglés GND (ground). Si está conectado con el suelo, se habla de __tierra__. A partir de ahí se cumple

<span class="anker" id="gl-8-2"></span>
$$\varphi_1=\varphi_2+U_{12}. \tag{8.2}$$
:::

:::satz Teorema 8.2 (Campo uniforme, libertad del punto de referencia)
<span class="anker" id="satz-8-2"></span>

Entre dos placas paralelas a la distancia $d$ con la tensión $U$ es $E=U/d$. Si se desplaza el punto de referencia, todos los potenciales cambian en la misma constante $c$, y todas las tensiones permanecen iguales:

<span class="anker" id="gl-8-3"></span>
$$E=\frac{U}{d},\qquad\varphi'(P)=\varphi(P)+c\quad\Longrightarrow\quad\varphi'_1-\varphi'_2=U_{12}. \tag{8.3}$$
:::

⁠**Cómo leerlo:** $U_{12}$ significa «tensión de 1 a 2», y el orden importa: $U_{21}=-U_{12}$. En los __esquemas eléctricos__, los dibujos de un circuito, se indica con una __flecha de referencia__ del punto 1 al punto 2 (fig. [9](#abb-9)). Esta fija el signo: si $U_{12}>0$, el punto 1 está más alto. Una carga positiva gana entonces energía cinética al avanzar en el sentido de la flecha; un electrón la pierde. La intensidad de campo indica cuánta tensión cae por metro de camino. Los potenciales pueden ser negativos; eso significa: más bajos que la masa.

Tensiones típicas: límite de medida de los voltímetros modernos 0,1 nV, antena de televisión 12 µ V a 10 mV, entre la mano y el corazón 1 mV, batería de coche 12 V, red eléctrica 230 V, línea de alta tensión 120 a 800 kV, generador de Van de Graaff (generador de correa para altas tensiones) 10 MV, rayo hasta 100 MV.

⁠**Validez:** La integral de [(8.1)](#gl-8-1) solo es independiente del camino en el campo electrostático. Un cable de un esquema se considera ideal: todos sus puntos tienen el mismo potencial. Está justificado: con 0,1 V/m, en 10 cm de cable solo caen 10 mV.

:::herleitung Par de placas y punto de referencia
⁠**Intensidad de campo.** Entre A y B, $\vec E$ es constante y apunta a lo largo del camino: $U_\mathrm{AB}=\int_0^dE\,\mathrm{d} x=E\,d$.

⁠**Punto de referencia.** Con [(7.1)](das-potenzial.html#gl-7-1) y la independencia del camino,

$$\varphi'(P)=\int_{P}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\varphi(P)+c.$$

La segunda integral no depende de $P$; en la diferencia desaparece.
:::

:::abbildung et1/k1symbole 9
Izquierda y centro: símbolos de una batería (trazo largo y fino: polo positivo) y de una fuente de tensión continua, que entrega una tensión fija. La flecha de referencia apunta del terminal positivo al negativo. Derecha: dos puntos, dos flechas de referencia, dos signos.
:::

:::abbildung et1/k1masse 10
El mismo circuito con la masa en tres lugares. Los potenciales son 9 V, 3 V, 0 V; luego 6 V, 0 V, $-3$ V; luego 0 V, $-6$ V, $-9$ V. Cada vez hay 6 V en la resistencia superior y 3 V en la inferior.
:::

::::beispiel
En el par de placas, $E=9\,\mathrm{V}/3\,\mathrm{mm}=3$ kV/m, 1000 veces menos que la intensidad de campo de ruptura del aire. Una batería rectangular entrega unos 0,5 Ah (amperios por horas), es decir, 1800 C. Su energía total es $W=Q\,U=1800\,\mathrm{C}\cdot9\,\mathrm{V}=16{,}2$ kJ $=4{,}5$ Wh. En el circuito, la masa está primero en el polo negativo (fig. [10](#abb-10), izquierda). Con [(8.2)](#gl-8-2), de abajo arriba resulta 0 V, $0+3$ V, $3+6$ V. Si la masa pasa al centro, cada potencial baja 3 V. La tensión en la resistencia superior es antes $9\,\mathrm{V}-3\,\mathrm{V}$ y después $6\,\mathrm{V}-0\,\mathrm{V}$. En los vehículos, el polo negativo de la batería suele estar conectado a la carrocería, que allí es la masa.
::::

⁠**En resumen:** la tensión es energía por unidad de carga entre dos puntos.

⁠**Casos límite:** Para $P_2=P_1$, $U=0$, y lo mismo para dos puntos de una misma pieza metálica en reposo. Con $d=3$ µ m, 9 V darían ya 3 MV/m.

:::frage ¿Por qué no le pasa nada a un pájaro en una línea de alta tensión?
La línea está a varios cientos de kilovoltios respecto a tierra, pero el pájaro solo toca la línea. Entre sus patas, con $E\approx0{,}1$ V/m y 5 cm de distancia, solo hay 5 mV. Cuenta la diferencia entre los puntos tocados, no el potencial en sí.
:::

:::frage ¿Se va la corriente por la masa?
Por una única conexión de masa, no. La corriente necesita un camino cerrado, y esa única conexión no ofrece camino de retorno. La masa es un acuerdo sobre el cero, no un desagüe.
:::

:::ltspice Desplazar la masa
⁠**Esquema:** fuente `voltage` con `9` de `a` a `b`, `res` con `2k` de `a` a `m`, `res` con `1k` de `m` a `b`. Coloca el símbolo de masa primero en `b`, luego en `m` y luego en `a`. LTspice siempre necesita una masa. Las resistencias se explican en el [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html); aquí solo sirven para el reparto en 6 V y 3 V.

⁠**Directivas:** `.op`, y para cada nudo sin masa una medida como `.meas op pa FIND V(a)`. El nudo con masa no tiene valor propio; para él pon 0.

⁠**Lo que ves:** Masa en `b`: $\mathtt{V(a)}=9$ V, $\mathtt{V(m)}=3$ V. Masa en `m`: $\mathtt{V(a)}=6$ V, $\mathtt{V(b)}=-3$ V. Masa en `a`: $\mathtt{V(m)}=-6$ V, $\mathtt{V(b)}=-9$ V. La diferencia entre `a` y `m` es siempre 6 V. Después monta la red del ejercicio [9](#aufg-9) con `5k`, `4k`, `3k` y comprueba tus potenciales.
:::

:::aufgabe Ejercicio 8 ★ Tensión y energía
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Un rayo transporta 5 C a través de 100 MV. ¿Qué energía es, en MJ y en kWh?

</li>

<li>

El aire se perfora a $3\cdot10^6$ V/m. ¿Qué tensión necesita una chispa de 1 cm?

</li>

<li>

Se tiene $U_{12}=+5$ V. ¿Cuánto vale $U_{21}$? ¿Qué punto está más alto?

</li>

</ol>

:::loesung
(a) $W=Q\,U=5\,\mathrm{C}\cdot100\,\mathrm{MV}=500$ MJ $=139$ kWh. (b) $U=E\,d=3\cdot10^6\,\mathrm{V/m}\cdot0{,}01\,\mathrm{m}=30$ kV. (c) $U_{21}=-5$ V; el punto 1 está 5 V más alto.
:::
:::

:::aufgabe Ejercicio 9 ★★ Potenciales en una cadena
<span class="anker" id="aufg-9"></span>

Una fuente de 12 V alimenta tres resistencias en serie. Los puntos de unión (__nudos__) se llaman 1 (polo positivo), 2, 3 y 4 (polo negativo). Se tiene $U_{12}=5$ V, $U_{23}=4$ V, $U_{34}=3$ V.

<ol class="al">

<li>

Da todos los potenciales con la masa en el nudo 4 y después con la masa en el nudo 3.

</li>

<li>

Calcula $U_{24}$ y $U_{13}$ en ambos casos. ¿Qué observas?

</li>

</ol>

:::loesung
(a) Masa en 4: $\varphi_4=0$, $\varphi_3=3$ V, $\varphi_2=7$ V, $\varphi_1=12$ V. Masa en 3: todos los valores bajan 3 V, $\varphi_4=-3$ V, $\varphi_3=0$, $\varphi_2=4$ V, $\varphi_1=9$ V. (b) Primer caso: $U_{24}=7$ V, $U_{13}=12\,\mathrm{V}-3\,\mathrm{V}=9$ V. Segundo caso: $U_{24}=4\,\mathrm{V}-(-3\,\mathrm{V})=7$ V, $U_{13}=9\,\mathrm{V}-0=9$ V. Las tensiones no cambian.
:::
:::
