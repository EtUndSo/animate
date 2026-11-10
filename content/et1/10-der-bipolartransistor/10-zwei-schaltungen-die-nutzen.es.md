---
title: Etapa 8: Dos circuitos que aprovechan $U_\mathrm{BE}$
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El transistor bipolar
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Capítulo 10: El transistor bipolar
order: 1201000
summary: Hasta ahora, U BE era una molestia.
tags: espejo de corriente, corriente de referencia, rizado
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Hasta ahora, $U_\mathrm{BE}$ era una molestia. Esta etapa aprovecha sus dos propiedades: igual $U_\mathrm{BE}$ significa igual corriente, y al variar la corriente, $U_\mathrm{BE}$ permanece casi igual.
:::

**La idea: espejo de corriente.** Según [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1), $U_\mathrm{BE}$ fija la corriente. Dos transistores iguales con la misma tensión $U_\mathrm{BE}$ llevan, por tanto, la misma corriente. En el __espejo de corriente__ (fig. [9](#abb-9), izquierda), T1 está conectado como diodo: base y colector están unidos. La corriente $I_\mathrm{ref}$ por la resistencia ajusta en T1 justo la tensión $U_\mathrm{BE}$ que necesita esa corriente. T2 está conectado a la misma tensión y copia la corriente a otra rama, independientemente de su carga.

:::satz Teorema 8.1 (Espejo de corriente)
<span class="anker" id="satz-8-1"></span>

Con transistores iguales e $I_\mathrm{B1}=I_\mathrm{B2}$ se cumple

<span class="anker" id="gl-8-1"></span>
$$I_\mathrm{ref}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{ref}}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2},\qquad I_\mathrm{C2}=B\,I_\mathrm{B2}=\frac{I_\mathrm{ref}}{1+\frac2B}\approx I_\mathrm{ref}. \tag{8.1}$$
:::

⁠**Cómo leerlo:** $I_\mathrm{ref}$ es la __corriente de referencia__. Las dos corrientes de base se derivan de ella. De ahí el pequeño error $2/B$. **Validez:** T2 activo, transistores iguales e igual temperatura, por ejemplo en un chip. Debido a la pendiente de la curva característica, T2 entrega algo más con $U_\mathrm{CE2}$ grande.

::::beispiel
Con $R_\mathrm{ref}=5{,}7$ k$\Omega$ es $I_\mathrm{ref}=2$ mA e $I_\mathrm{C2}=1{,}98$ mA, con $R_\mathrm{L}$ arbitraria hasta $11{,}8\,\mathrm{V}/1{,}98\,\mathrm{mA}=5{,}96$ k$\Omega$. Más allá, T2 estaría saturado. Con [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1), a $U_\mathrm{CE2}=6$ V y $U_\mathrm{CE1}=0{,}6$ V la corriente en T2 sería un 7 % mayor.
::::

⁠**Caso límite:** para $B\to\infty$ es $I_\mathrm{C2}=I_\mathrm{ref}$.

**La idea: regulador de tensión.** Un rectificador con filtrado ([capítulo 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) entrega una tensión continua con una ondulación residual, el __rizado__. En el regulador (fig. [9](#abb-9), derecha), un diodo Zener mantiene la base en $U_\mathrm{Z}$. El emisor es la salida y está una tensión de diodo más abajo. Si la tensión de salida baja porque la carga pide más corriente, $U_\mathrm{BE}$ crece y el transistor aporta más. En $U_\mathrm{CE}$ cae el resto de la tensión de entrada. La corriente de carga no pasa por $R_1$; la base solo necesita la $B$-ésima parte. El diodo Zener apenas se carga, por tanto.

:::satz Teorema 8.2 (Regulador de tensión con diodo Zener)
<span class="anker" id="satz-8-2"></span>

De la malla por el diodo Zener, el tramo BE y la carga se deduce

<span class="anker" id="gl-8-2"></span>
$$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}. \tag{8.2}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{E,min}$ es el mínimo de la tensión de entrada $U_\mathrm{E}$ en el valle del rizado, $U_\mathrm{A}$ la tensión de salida. **Validez:** siempre debe cumplirse $U_\mathrm{E}>U_\mathrm{A}+U_\mathrm{CE,sat}$ para que T siga activo, y $R_1$ debe aportar suficiente corriente: $(U_\mathrm{E,min}-U_\mathrm{Z})/R_1>I_\mathrm{B}$. Si no, el diodo Zener sale de la ruptura y el rizado llega a la salida.

:::abbildung et1/k10spiegel 9
Izquierda, espejo de corriente: T1 como diodo genera $U_\mathrm{BE}$, T2 copia la corriente. Centro, regulador de tensión con diodo Zener, el emisor es la salida. Derecha, la evolución: la tensión de entrada oscila entre 10,5 V y 13,5 V, la salida se mantiene en 5,6 V.
:::

::::beispiel
$U_\mathrm{Z}=6{,}2$ V da $U_\mathrm{A}=5{,}6$ V. Con 50 mA de carga, la base necesita 0,25 mA. Con $R_1=1$ k$\Omega$ y $U_\mathrm{E}=12$ V$\,\pm1{,}5$ V circulan por el diodo Zener de 4,05 mA a 7,05 mA. Un diodo Zener con 10 $\Omega$ de resistencia de pequeña señal convierte 3 V de rizado en solo 30 mV. En el transistor se producen hasta $7{,}9\,\mathrm{V}\cdot50\,\mathrm{mA}=395$ mW, justo por debajo de $P_\mathrm{max}$. El regulador convierte en calor la tensión sobrante. Con 0,68 V en lugar de 0,6 V, el valor más exacto de $U_\mathrm{BE}$ con 50 mA, $U_\mathrm{A}$ sería 80 mV menor.
::::

⁠**Caso límite:** sin carga, $I_\mathrm{B}\approx0$, $U_\mathrm{A}$ sube ligeramente, $U_\mathrm{Z}$ se mantiene.

:::frage ¿Por qué no solo el diodo Zener?
Entonces la resistencia en serie tendría que aportar los 50 mA completos y además un resto para el diodo Zener con la tensión de entrada más baja. Con la tensión de pico, la diferencia circularía por el diodo Zener, y la resistencia en serie se calentaría con unos 0,7 W. El transistor separa ambas cosas: el diodo Zener impone la tensión, y la alimentación aporta la corriente a través del colector. Los transistores de potencia y los componentes derivados de ellos conmutan también grandes corrientes, por ejemplo en convertidores para motores eléctricos.
:::

:::aufgabe Ejercicio 10 ★★ Espejo y regulador
<span class="anker" id="aufg-10"></span>

(a) ¿Qué $R_\mathrm{ref}$ da la corriente de referencia de 1 mA con $U_\mathrm{CC}=12$ V? ¿Cuánto vale $I_\mathrm{C2}$ para $B=200$ y para $B=50$? (b) ¿Hasta qué $R_\mathrm{L}$ funciona el espejo con $B=200$? (c) Un regulador tiene $U_\mathrm{Z}=9{,}1$ V, $R_1=470\,\Omega$, 30 mA de carga, $U_\mathrm{E}$ de 12 V a 15 V. Determina $U_\mathrm{A}$, la menor corriente de Zener, la mayor potencia en el transistor y la reserva de tensión hacia abajo.

:::loesung
(a) $R_\mathrm{ref}=11{,}4\,\mathrm{V}/1\,\mathrm{mA}=11{,}4$ k$\Omega$. $I_\mathrm{C2}=1\,\mathrm{mA}/1{,}01=0{,}990$ mA, y con $B=50$ son $1\,\mathrm{mA}/1{,}04=0{,}962$ mA.

(b) $R_\mathrm{L}\le11{,}8\,\mathrm{V}/0{,}990\,\mathrm{mA}=11{,}9$ k$\Omega$.

(c) $U_\mathrm{A}=8{,}5$ V, $I_\mathrm{B}=0{,}15$ mA. A 12 V circulan entonces por $R_1$ $2{,}9\,\mathrm{V}/470\,\Omega=6{,}17$ mA, y por el diodo Zener 6,02 mA. A 15 V, $P=6{,}5\,\mathrm{V}\cdot30\,\mathrm{mA}=195$ mW. Reserva: $12\,\mathrm{V}-8{,}5\,\mathrm{V}-0{,}2\,\mathrm{V}=3{,}3$ V.
:::
:::
