---
title: Etapa 6: La energía almacenada
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El condensador
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Capítulo 3: El condensador
order: 1130700
summary: Cargar cuesta energía, porque cada carga adicional debe avanzar contra la tensión ya presente.
tags: densidad de energía
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Cargar cuesta energía, porque cada carga adicional debe avanzar contra la tensión ya presente. Esta etapa calcula cuánta es y dónde está después la energía.
:::

**La idea.** La tensión es energía por unidad de carga ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Llevar la pequeña carga $\Delta q$ de la placa negativa a la positiva cuesta $\Delta W=u\,\Delta q$. Las primeras cargas no cuestan casi nada, porque aún no hay campo. Las últimas cuestan el importe completo $U$ por culombio. De media, cada carga paga $U/2$. Esa es el área bajo la recta $u=q/C$ (fig. [6](#abb-6) izquierda).

:::satz Teorema 6.1 (Energía en el condensador)
<span class="anker" id="satz-6-1"></span>

Un condensador con la carga $Q$ y la tensión $U$ almacena

<span class="anker" id="gl-6-1"></span>
$$W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}=\frac12\,Q\,U=\frac12\,C\,U^2. \tag{6.1}$$

Esa energía reside en el campo entre las placas. En el condensador de placas, con el volumen $V=A\,d$, se cumple

<span class="anker" id="gl-6-2"></span>
$$W=\frac12\,\varepsilon\,E^2\cdot A\,d,\qquad w=\frac WV=\frac12\,\varepsilon\,E^2. \tag{6.2}$$

Aquí $w$ es la __densidad de energía__, la energía por unidad de volumen.
:::

⁠**Cómo leerlo:** $W$ en J, $C$ en F, $U$ en V, $w$ en J/m$^3$. La tensión entra al cuadrado: el doble de tensión significa el doble de carga, y esta avanza contra el doble de tensión. $q$ es la carga durante el proceso de carga, $Q$ su valor final. **Validez:** $C$ constante, sin corriente de fuga.

:::herleitung La energía a partir de fuerza y camino
La fuerza sobre $\Delta q$ en el campo es $F=\Delta q\,E$ ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). A lo largo de la distancia $\Delta s$ entre las placas, eso cuesta $\Delta W=F\,\Delta s=\Delta q\,E\,\Delta s$. Con $E\,\Delta s=u$ resulta $\Delta W=\Delta q\,u$, y con $u=q/C$ es $\Delta W=\frac qC\,\Delta q$. Para $\Delta q$ pequeñas, la suma de todas las porciones se convierte en la integral [(6.1)](#gl-6-1).

El lado del circuito da el mismo resultado. La potencia (energía por unidad de tiempo) es $p=u\,i$ ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Con $i=C\,\mathrm{d} u/\mathrm{d} t$ se obtiene $W=\int u\,i\,\mathrm{d} t=C\int_0^Uu\,\mathrm{d} u=\frac12CU^2$.

⁠**Del componente al campo:** Sustituyendo $C=\varepsilon A/d$ y $U=E\,d$ en [(6.1)](#gl-6-1) se obtiene [(6.2)](#gl-6-2).
:::

:::abbildung et1/k3energie 6
Izquierda: seis porciones de 150 µC cada una. Cada porción cuesta $u\,\Delta q$; su tensión es la del centro de la porción. El área de todas las barras es el área del triángulo bajo $u=q/C$, es decir, $W=\frac12QU=4{,}05$ mJ. Derecha: la energía reside en el espacio entre las placas, por unidad de volumen $w=\frac12\varepsilon E^2$. En el metal es $E=0$.
:::

**Dónde reside la energía.** El metal no puede contenerla, porque allí $E=0$ y los electrones solo están desplazados una minucia (etapa [2](die-kapazitat.html#stufe-2)). La ecuación [(6.2)](#gl-6-2) dice: cada metro cúbico de campo contiene $\frac12\varepsilon E^2$. Que esto es más que una forma de calcular lo muestra un experimento. Se desconecta la batería y se separan las placas. $Q$ se mantiene y, con ella, $E=Q/(\varepsilon A)$. Pero el campo llena más volumen, y la energía del campo crece en $\frac12\varepsilon E^2A\,\Delta d$. La energía procede de la mano que tira contra la atracción de las placas. Cada placa solo siente el campo de la otra, que es la mitad de $E$, es decir, $F=\frac12QE$. El trabajo es $F\,\Delta d=\frac12QE\,\Delta d=\frac12\varepsilon E^2A\,\Delta d$, exactamente el aumento. Que la energía del campo existe con independencia de las cargas lo muestra la luz: transporta energía por el espacio vacío.

::::beispiel
El condensador del circuito RC almacena a 9 V $W=\frac12\cdot100\,\mu\text{F}\cdot(9\,\mathrm{V})^2=4{,}05$ mJ; el par de placas, solo 1,20 nJ. Allí es $w=\frac12\varepsilon_0(3\,\mathrm{kV/m})^2=3{,}98\cdot10^{-5}$ J/m$^3$, y multiplicado por $V=3\cdot10^{-5}\,\mathrm{m^3}$ da los mismos 1,20 nJ. Un supercap de 100 F almacena a 2,7 V nada menos que 365 J, pero una batería rectangular de 9 V con 0,5 Ah almacena 16 kJ, cuatro millones de veces lo que el condensador de 100 µF. Los condensadores almacenan poca energía, pero la entregan muy deprisa, por ejemplo en el flash de una cámara.
::::

⁠**Caso límite:** Para $U\to0$, $W\to0$: sin campo no hay energía. **Comprobación:** $\mathrm{F\cdot V^2}=\frac{\mathrm{C}}{\mathrm V}\cdot\mathrm{V^2}=\mathrm{C\,V}=\mathrm J$.

:::frage ¿Por qué no $W=Q\,U$? Tensión por carga es energía.
$Q\,U$ es correcto cuando toda la carga recorre la tensión completa. Durante la carga, sin embargo, $U$ es el valor final; la tensión crece desde cero. La batería cede realmente $Q\,U$, porque por ella pasa cada carga a la tensión completa. El condensador solo recibe la mitad. Adónde va el resto lo aclara el ejercicio [11](aufladen-uber-einen-widerstand.html#aufg-11).
:::

:::aufgabe Ejercicio 7 ★★★ Separar las placas
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Un condensador de 470 µF está conectado a 12 V, luego a 24 V. ¿Cuánto vale $W$ en cada caso?

</li>

<li>

El par de placas se carga a 9 V y se desconecta. Después, $d$ se duplica hasta 6 mm. ¿Cuánto valen $C$, $U$, $E$ y $W$? Comprueba el aumento de $W$ con $F\,\Delta d$.

</li>

<li>

Lo mismo, pero la batería sigue conectada. Ahora $W$ disminuye, aunque la mano realiza trabajo. ¿Adónde va la energía? El trabajo mecánico es aquí de 0,60 nJ.

</li>

</ol>

:::loesung
(a) $W=\frac12\cdot470\,\mu\text{F}\cdot(12\,\mathrm{V})^2=33{,}8$ mJ; a 24 V, el cuádruple, 135 mJ.

(b) $Q=266$ pC se mantiene. $C=14{,}8$ pF, $U=Q/C=18$ V, $E=U/d=3$ kV/m como antes. $W=\frac12QU=2{,}39$ nJ; el aumento es de 1,20 nJ. La fuerza es $F=\frac12QE=0{,}398\,\mu\text{N}$, y $F\,\Delta d=0{,}398\,\mu\text{N}\cdot3\,\mathrm{mm}=1{,}20$ nJ. Ambos valores coinciden.

(c) $U=9$ V se mantiene. $C=14{,}8$ pF, $Q=133$ pC, $E=1{,}5$ kV/m, $W=0{,}60$ nJ. El campo pierde 0,60 nJ. A ello se suman 0,60 nJ de la mano. Ambas cantidades van a la batería, porque 133 pC regresan a 9 V: $133\,\mathrm{pC}\cdot9\,\mathrm{V}=1{,}20$ nJ. La batería se carga un poco.
:::
:::
