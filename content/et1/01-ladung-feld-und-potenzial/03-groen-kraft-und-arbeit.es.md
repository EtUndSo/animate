---
title: Etapa 1: Magnitudes, fuerza y trabajo
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1110300
summary: La tensión resultará ser trabajo por unidad de carga.
tags: cualitativos, cuantitativo, ley de Ohm, magnitud física, sistema de unidades SI, magnitudes básicas, corriente, prefijos SI
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
La tensión resultará ser trabajo por unidad de carga. Para ello hacen falta magnitudes con unidades, la fuerza, el trabajo y la energía cinética.
:::

**La idea.** Quien viene de la nieve dice que una habitación está caliente; quien sale de la sauna, que está fresca. Estos juicios son __cualitativos__. Un termómetro les indica a ambos 21 °C; eso es __cuantitativo__: un número con una escala, independiente de quién mida. Con estas magnitudes formula la física sus leyes, por ejemplo la __ley de Ohm__ $U=R\cdot I$ ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). La magnitud mecánica más importante de este capítulo es el trabajo: una fuerza que actúa a lo largo de un camino transfiere energía, y solo cuenta su componente en la dirección del camino. Quien levanta una mochila trabaja contra la gravedad; quien la lleva en horizontal, no (fig. [2](#abb-2)).

:::definition Definición 1.1 (Magnitud física)
<span class="anker" id="satz-1-1"></span>

Una __magnitud física__ es una propiedad medible, el producto de valor numérico y unidad:

<span class="anker" id="gl-1-1"></span>
$$\text{magnitud}=\text{valor numérico}\cdot\text{unidad}. \tag{1.1}$$
:::

⁠**Cómo leerlo:** En $U=9$ V, $U$ es el símbolo (en cursiva), 9 el valor numérico, V la unidad (en redonda). Los corchetes preguntan por la unidad: $[U]=\mathrm V$. El valor numérico depende de la unidad; la magnitud, no: 72 km/h y 20 m/s son la misma velocidad.

**Unidades.** El __sistema de unidades SI__ tiene siete __magnitudes básicas__, que no pueden expresarse unas mediante otras: longitud (metro, m), masa (kilogramo, kg), tiempo (segundo, s), intensidad de corriente (amperio, A), temperatura absoluta (kelvin, K), intensidad luminosa (candela, cd) y cantidad de sustancia (mol, mol). Sus definiciones evolucionan con la técnica de medida. Las unidades de todas las demás magnitudes son productos de potencias de las unidades básicas. Una __corriente__ eléctrica es carga en movimiento; un amperio transporta un culombio por segundo. La potencia es energía por tiempo. Para este capítulo basta con:

| Magnitud | Unidad | en unidades básicas | también |
|---|---|---|---|
| Fuerza $F$ | newton, N | $\mathrm{kg\,m/s^2}$ | $\mathrm{J/m}$ |
| Energía, trabajo $W$ | julio, J | $\mathrm{kg\,m^2/s^2}$ | $\mathrm{N\,m}=\mathrm{W\,s}$ |
| Potencia $P$ | vatio, W | $\mathrm{kg\,m^2/s^3}$ | $\mathrm{V\,A}$ |
| Carga $Q$ | culombio, C | $\mathrm{A\,s}$ |  |
| Tensión $U$ | voltio, V | $\mathrm{kg\,m^2/(s^3\,A)}$ | $\mathrm{J/C}$ |

Los __prefijos SI__ escalan un valor numérico en potencias de diez. Los múltiplos se escriben en mayúscula y los submúltiplos en minúscula; solo deca, hecto y kilo se apartan de la regla por razones históricas. Delante de una unidad va siempre un solo prefijo, y forma con ella un único símbolo.

| Prefijo | Potencia | en palabras | Prefijo | Potencia | en palabras |
|---|---|---|---|---|---|
| Atto, a | $10^{-18}$ | trillonésima | Exa, E | $10^{18}$ | trillón |
| Femto, f | $10^{-15}$ | milbillonésima | Peta, P | $10^{15}$ | mil billones |
| Pico, p | $10^{-12}$ | billonésima | Tera, T | $10^{12}$ | billón |
| Nano, n | $10^{-9}$ | milmillonésima | Giga, G | $10^{9}$ | mil millones |
| Micro, µ | $10^{-6}$ | millonésima | Mega, M | $10^{6}$ | millón |
| Mili, m | $10^{-3}$ | milésima | Kilo, k | $10^{3}$ | mil |
| Centi, c | $10^{-2}$ | centésima | Hecto, h | $10^{2}$ | cien |
| Deci, d | $10^{-1}$ | décima | Deca, da | $10^{1}$ | diez |

**Calcular con unidades.**

<ol>

<li>

⁠**Sumar** solo se pueden magnitudes de la misma unidad; antes se igualan los prefijos: $2\,\mathrm{kV}+40\,\mathrm{V}=2{,}04\,\mathrm{kV}$, no 42 kV. Unidades distintas en una suma casi siempre delatan un error de cálculo.

</li>

<li>

⁠**Multiplicar** siempre se puede. Los valores numéricos, las unidades y los prefijos se multiplican por separado, y en las fracciones las unidades se simplifican como números: $\frac{6\,\mathrm{N\,m}}{3\,\mathrm{m}}=2\,\mathrm{N}$, $0{,}5\,\mathrm{A}\cdot9\,\mathrm{V}=4{,}5\,\mathrm{W}$, $\mathrm{k\cdot M}=\mathrm G$, $\mu\text{}\cdot\mathrm M=1$. En el modelo de referencia, $9\,\mathrm{V}/3\,\mathrm{mm}=3000\,\mathrm{V/m}=3\,\mathrm{kV/m}$.

</li>

<li>

⁠**Convertir** a veces requiere un factor: $1\,\mathrm{Wh}=3600\,\mathrm{W\,s}$, $1\,\mathrm{km/h}=\frac{1}{3{,}6}\,\mathrm{m/s}$. Como prefijo y unidad son un solo símbolo, $1\,\mathrm{km^2}=(1000\,\mathrm{m})^2=10^6\,\mathrm{m^2}$, no 1000 m$^2$.

</li>

<li>

⁠**La magnitud decide la unidad.** La energía se escribe, según el ámbito, en W s, N m o J. Pero unidades básicas iguales no demuestran que la magnitud sea la misma: el hercio (oscilaciones por segundo) y el becquerel (desintegraciones por segundo) son ambos $1/\mathrm s$, y N m es también el par (fuerza por brazo de palanca).

</li>

</ol>

**Fuerza y trabajo.** Una __fuerza__ deforma un cuerpo sujeto o acelera uno móvil. La __energía__ es la capacidad de realizar trabajo. La fuerza y el desplazamiento son __vectores__: magnitudes con módulo y dirección, escritas con una flecha, $\vec F$. La __velocidad__ es la variación del desplazamiento por tiempo, $v=\mathrm{d} s/\mathrm{d} t$; la __aceleración__, la variación de la velocidad por tiempo, $a=\mathrm{d} v/\mathrm{d} t$.

:::definition Definición 1.2 (Fuerza y trabajo)
<span class="anker" id="satz-1-2"></span>

La fuerza sobre un cuerpo de masa $m$ y aceleración $a$ y la fuerza entre dos masas $m$, $M$ a la distancia $r$ son

<span class="anker" id="gl-1-2"></span>
$$F=m\,a,\qquad F=\gamma\,\frac{m\,M}{r^2}. \tag{1.2}$$

El __trabajo__ de una fuerza a lo largo de un camino es

<span class="anker" id="gl-1-3"></span>
$$\Delta W=\vec F\cdot\Delta\vec s=F\,\Delta s\cos\alpha,\qquad W=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s. \tag{1.3}$$
:::

:::satz Teorema 1.3 (Aceleración constante y energía cinética)
<span class="anker" id="satz-1-3"></span>

Con los valores iniciales $s_0$ y $v_0$ en $t=0$, para $a$ constante se cumple

<span class="anker" id="gl-1-4"></span>
$$v(t)=v_0+a\,t,\qquad s(t)=s_0+v_0\,t+\tfrac12a\,t^2. \tag{1.4}$$

Un cuerpo con velocidad $v$ tiene la __energía cinética__ $W_\mathrm{kin}=\frac12m\,v^2$.
:::

⁠**Cómo leerlo:** $[F]=\mathrm N$; sobre 100 g actúa en la superficie terrestre aproximadamente 1 N. $\gamma=6{,}674\cdot10^{-11}\,\mathrm{N\,m^2/kg^2}$ es la __constante de gravitación__. $\alpha$ es el ángulo entre la fuerza y el tramo de camino. El producto $\vec F\cdot\Delta\vec s$ se llama __producto escalar__; su resultado es un número. La integral se llama __integral de línea__: el camino se divide en tramos rectos cortos y se suman sus contribuciones. $[W]=\mathrm J$; un julio eleva 102 g un metro. Para $\alpha<90^\circ$ la fuerza cede energía al cuerpo; para $\alpha>90^\circ$ se la quita. **Validez:** [(1.4)](#gl-1-4) solo vale para aceleración constante; la etapa [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9) necesita justo este caso.

:::herleitung Energía cinética
De [(1.4)](#gl-1-4) con $v_0=0$ y $s_0=0$ se obtiene $t=v/a$ y $s=\frac12a\,t^2=v^2/(2a)$. Una fuerza constante $F=m\,a$ realiza en este camino el trabajo $F\,s=m\,a\,v^2/(2a)=\frac12m\,v^2$.
:::

:::abbildung et1/k1wegarbeit 2
Una mochila de 2 kg se lleva de A a B, 8 m hacia un lado y 6 m hacia arriba. En la escalera solo cuentan los tramos rojos, en total 6 m. En la rampa el camino mide 10 m y $\cos\alpha=0{,}6$. Ambos caminos dan 117,7 J.
:::

::::beispiel
Sobre la mochila actúa el __peso__ $F_\mathrm{G}=m\,g=19{,}62\,\mathrm{N}$. Para elevarla de manera uniforme, la mano aplica la misma fuerza hacia arriba. Por la escalera, $W=19{,}62\,\mathrm{N}\cdot6\,\mathrm{m}=117{,}7\,\mathrm{J}$; por la rampa, $W=19{,}62\,\mathrm{N}\cdot10\,\mathrm{m}\cdot0{,}6=117{,}7\,\mathrm{J}$. La mano realiza $+117{,}7$ J; el peso, $-117{,}7$ J. La energía queda entonces en la altura, como __energía potencial__: si la mochila cae, se convierte en energía cinética. Este par, trabajo de la fuerza del campo y trabajo exterior, reaparece en la etapa [6](arbeit-im-feld.html#stufe-6).
::::

⁠**Casos límite:** $\alpha=0$ da $\Delta W=F\,\Delta s$; $\alpha=90^\circ$ da $\Delta W=0$.

:::frage Al llevar algo en horizontal, el brazo se cansa. ¿No se realiza ahí ningún trabajo?
Sobre la mochila, no: no gana ni altura ni velocidad. Aun así, el músculo consume energía, porque sus fibras se tensan una y otra vez. Esa energía se convierte en calor en el cuerpo y no llega a la mochila.
:::

:::aufgabe Ejercicio 1 ★ Unidades y prefijos
<span class="anker" id="aufg-1"></span>

Calcula y da el resultado en una unidad adecuada: (a) $3\,\mathrm{kN}+450\,\mathrm{N}$, (b) $2\,\mathrm{mA}\cdot4\,\mathrm{ks}$, (c) $6\,\mu\text{C}/3\,\mathrm{ms}$, (d) 1 kWh en julios, (e) 1,5 mm$^2$ en m$^2$, (f) la unidad V/m en unidades básicas.

:::loesung
(a) $3000\,\mathrm{N}+450\,\mathrm{N}=3{,}45\,\mathrm{kN}$. (b) Mili y kilo se anulan, $\mathrm{A\cdot s}=\mathrm C$: 8 C. (c) $\mu\text{}/\mathrm m=\mathrm m$ (mili) y $\mathrm{C/s}=\mathrm A$: 2 mA. (d) $1000\,\mathrm{W}\cdot3600\,\mathrm{s}=3{,}6\,\mathrm{MJ}$. (e) $1\,\mathrm{mm^2}=(10^{-3}\,\mathrm{m})^2=10^{-6}\,\mathrm{m^2}$, es decir, $1{,}5\cdot10^{-6}\,\mathrm{m^2}$. (f) $\frac{\mathrm V}{\mathrm m}=\frac{\mathrm{kg\,m^2}}{\mathrm{A\,s^3}\cdot\mathrm m}=\frac{\mathrm{kg\,m}}{\mathrm{A\,s^3}}$.
:::
:::
