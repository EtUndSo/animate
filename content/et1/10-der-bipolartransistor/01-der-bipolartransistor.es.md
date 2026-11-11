---
title: Visión general: El transistor bipolar
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El transistor bipolar
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Capítulo 10: El transistor bipolar
order: 1200100
summary: Cómo una pequeña tensión controla una gran corriente a través de un diodo bloqueado
tags: transistor bipolar
lang: es
---

## De qué trata

Un micrófono entrega milivoltios, un altavoz necesita voltios. Una salida de ordenador entrega miliamperios, un motor necesita amperios. Entre ambos se sitúa un componente que controla una gran corriente con una señal pequeña. Su representante clásico es el __transistor bipolar__, un componente semiconductor de tres capas con tres terminales. La energía procede de la tensión de alimentación; la señal solo ajusta la cantidad. El otro tipo importante, el MOSFET, domina la electrónica digital y no es tema de este capítulo. La pregunta es: *¿Cómo puede una tensión de 0,6 V controlar una corriente que circula por un diodo bloqueado?*

**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Transistor T:** un transistor npn de pequeña señal de silicio con $B=200$, $I_\mathrm{S}=1{,}9\cdot10^{-13}$ A (corriente inversa de saturación, [capítulo 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) y $U_T=26$ mV (tensión térmica a 300 K, redondeada desde 25,85 mV). Para calcular a mano se aproxima $U_\mathrm{BE}=0{,}6$ V cuando el transistor conduce y $U_\mathrm{CE,sat}=0{,}2$ V cuando está completamente activado. Valores límite: $U_\mathrm{CE,max}=40$ V, $I_\mathrm{C,max}=100$ mA, $P_\mathrm{max}=400$ mW.

</li>

<li>

⁠**Circuito:** alimentación $U_\mathrm{CC}=12$ V, resistencia de colector $R_\mathrm{C}=3$ k$\Omega$, resistencia de base $R_\mathrm{B}=440$ k$\Omega$, tensión de entrada $U_\mathrm{ent}=5$ V. Esto da el punto de trabajo $I_\mathrm{B}=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=6$ V.

</li>

<li>

⁠**Versión con realimentación negativa:** divisor de base $R_1=31$ k$\Omega$, $R_2=9$ k$\Omega$, resistencia de emisor $R_\mathrm{E}=1$ k$\Omega$ (etapa [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7)).

</li>

</ul>

:::
