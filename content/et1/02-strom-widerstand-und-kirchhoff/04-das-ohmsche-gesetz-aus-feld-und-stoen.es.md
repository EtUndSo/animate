---
title: Etapa 3: La ley de Ohm a partir del campo y las colisiones
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1120400
summary: La etapa 2 ha mostrado que la deriva es proporcional al campo.
tags: conductividad, resistividad, conductancia, lineal, homogéneo, potencia
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
La etapa [2](langsame-elektronen-sofortiger-strom.html#stufe-2) ha mostrado que la deriva es proporcional al campo. En pocos pasos, esta etapa convierte eso en la ley más importante de la técnica de circuitos.
:::

**La idea.** Más tensión significa un campo más intenso en el conductor, un campo más intenso significa una deriva más rápida, una deriva más rápida significa más corriente. Cada paso es una proporcionalidad, y por tanto también todo el camino de $U$ a $I$. El factor contiene el material y la forma (fig. [4](#abb-4)).

:::abbildung et1/k2ohm 4
Izquierda: conductor de longitud $L$ y sección $A$. El campo $E$ y la densidad de corriente $j$ son iguales en todas partes. Derecha: curvas características en el modelo de referencia. $I$ frente a $U$ es una recta que pasa por el origen; su pendiente es la conductancia $G=\Delta I/\Delta U$, el inverso de $R=\Delta U/\Delta I$. El punto corresponde a 9 V en $R_1+R_2=3\,\mathrm{k\Omega}$.
:::

:::satz Teorema 3.1 (Ley de Ohm)
<span class="anker" id="satz-3-1"></span>

Para un conductor con la densidad de electrones $n$ se cumple

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} \vec j&=\sigma\,\vec E,\qquad\sigma=n\,e\,\mu,\qquad\rho=\frac1\sigma,\\ U&=R\,I,\qquad R=\frac{L}{\sigma\,A}=\rho\,\frac LA,\qquad G=\frac1R=\frac IU. \end{aligned} \tag{3.1|3.2}$$
:::

⁠**Cómo leerlo:** $\sigma$ es la __conductividad__ en S/m, $\rho$ la __resistividad__ en $\Omega\,\mathrm m$. A menudo se da en $\Omega\,\mathrm{mm^2/m}$; el cobre tiene entonces 0,017. $R$ es la resistencia en $\Omega$ (ohmios), $1\,\Omega=1$ V/A: m$\Omega$ en un hilo, k$\Omega$ en circuitos. Su símbolo es un rectángulo (fig. [6](zweipole-und-zahlpfeile.html#abb-6)). $G$ es la __conductancia__ en S (siemens), $1\,\mathrm{S}=1\,\Omega^{-1}$. Las unidades llevan los nombres de Georg Simon Ohm y Werner von Siemens. **Validez:** El conductor debe ser __lineal__ ($\vec j$ proporcional a $\vec E$) y __homogéneo__ (el mismo material en todas partes). La temperatura debe ser constante (etapa [4](reale-widerstande-werte-und-temperatur.html#stufe-4)), y debe cumplirse $L\gg\sqrt A$ para que el campo en los extremos no influya. La linealidad se cumple con gran exactitud en los metales: el tiempo de vuelo $T$ no depende de $E$, porque la deriva es más de $10^{9}$ veces menor que el movimiento desordenado.

:::herleitung Del campo al componente
Densidad de corriente de los electrones, etapa [1](strom-ist-bewegte-ladung.html#stufe-1), con $q=-n\,e$ y [(2.1)](langsame-elektronen-sofortiger-strom.html#gl-2-1):

$$\vec j=q\,\vec v_\mathrm D=(-n\,e)(-\mu\,\vec E)=n\,e\,\mu\,\vec E=\sigma\,\vec E.$$

El campo es uniforme, así que $U=E\,L$ ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Con ello

$$I=j\,A=\sigma\,E\,A=\frac{\sigma\,A}{L}\,U\quad\Longrightarrow\quad U=\frac{L}{\sigma\,A}\,I=R\,I.$$
:::

| Conductor | $\rho$ en $10^{-8}\,\Omega\,\mathrm m$ | $\sigma$ en $10^{6}$ S/m | Conductor | $\rho$ en $10^{-8}\,\Omega\,\mathrm m$ | $\sigma$ en $10^{6}$ S/m |
|---|---|---|---|---|---|
| Plata | 1,6 | 62 | Latón | 7 a 9 | 14 a 11 |
| Cobre | 1,7 | 59 | Hierro | 10 a 15 | 10 a 7 |
| Oro | 2,3 | 43 | Platino | 11 | 9 |
| Aluminio | 2,8 | 36 | Constantán | 50 | 2 |
| Wolframio | 5,5 | 18 | Carbón | 5000 a 10000 | 0,02 a 0,01 |

::::beispiel
El hilo tiene $R=\rho\,L/A=34\,\mathrm{m\Omega}$. Con 3 mA caen en él 0,10 mV, es decir, $1{,}1\cdot10^{-5}$ de los 9 V. Esto justifica que los esquemas dibujen los hilos como ideales, sin tensión a lo largo del hilo. El mismo cálculo muestra por qué las resistencias no son de cobre: $2\,\mathrm{k\Omega}$ necesitarían, con $0{,}01\,\mathrm{mm^2}$ de sección, 1,2 km de cobre, pero solo 40 m de constantán.
::::

⁠**Casos límite:** El doble de longitud con la misma tensión reduce a la mitad el campo y, con él, la corriente. El doble de sección actúa como dos hilos uno junto a otro; la corriente se duplica. $U=0$ da $I=0$.

**Adónde va la energía.** En cada colisión, el electrón cede a la red cristalina la energía cinética ganada en el campo. La red vibra con más fuerza, y eso es calor. Cada culombio cede la energía $U$ en julios, y por segundo pasan $I$ culombios. La __potencia__, la energía por unidad de tiempo, es por tanto $P=U\,I=R\,I^2$. La cadena convierte $9\,\mathrm{V}\cdot3\,\mathrm{mA}=27$ mW. El [capítulo 7](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html) trata la potencia con más detalle.

:::frage $R=U/I$ siempre se puede calcular. ¿Qué dice entonces la ley de Ohm?
El cociente $U/I$ existe en todo componente. La ley dice más: es *constante*, independiente de $U$. Esa es una afirmación sobre el material y se deduce del tiempo de vuelo fijo. En una lámpara incandescente no se cumple (etapa [4](reale-widerstande-werte-und-temperatur.html#stufe-4)).
:::

:::aufgabe Ejercicio 3 ★★ Resistencia a partir de la geometría
<span class="anker" id="aufg-3"></span>

Una línea de alimentación consta de un conductor de ida y otro de vuelta, cada uno de 20 m de cobre con $1{,}5\,\mathrm{mm^2}$ de sección.

<ol class="al">

<li>

Calcula su resistencia y la tensión que cae en ella con 16 A.

</li>

<li>

¿Qué sección necesitaría el aluminio para la misma resistencia?

</li>

<li>

Predicción: Un hilo se estira hasta el doble de longitud y su volumen no cambia. ¿En qué factor cambia $R$?

</li>

</ol>

:::loesung
(a) $R=\rho\cdot40\,\mathrm{m}/1{,}5\,\mathrm{mm^2}=0{,}453\,\Omega$. Caen $0{,}453\,\Omega\cdot16\,\mathrm{A}=7{,}3$ V, el 3,2 % de 230 V. (b) Igual $R$ significa igual $\rho/A$: $A_\mathrm{Al}=1{,}5\,\mathrm{mm^2}\cdot2{,}8/1{,}7=2{,}5\,\mathrm{mm^2}$. (c) Volumen $L\,A$ constante: $L\to2L$ obliga a $A\to A/2$. Por tanto, $R\to4R$.
:::
:::
