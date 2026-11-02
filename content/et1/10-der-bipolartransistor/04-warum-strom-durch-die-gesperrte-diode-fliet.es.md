---
title: Etapa 2: Por qué circula corriente por el diodo bloqueado
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1200400
summary: El diodo CB bloquea y, sin embargo, por él circulan miliamperios.
tags: inyección, longitud de difusión, corriente de transferencia, región activa
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
El diodo CB bloquea y, sin embargo, por él circulan miliamperios. Esta etapa sigue el camino de los electrones y muestra por qué basta una pequeña corriente de base.
:::

**La idea.** Un diodo bloqueado no bloquea porque su frontera sea impermeable. Bloquea porque en el lado p casi no hay electrones libres disponibles. El campo de la zona de carga espacial empuja hacia la zona n a todo electrón que llega a la frontera desde el lado p. Para esos electrones, la frontera es una caída (fig. [2](#abb-2), abajo). El transistor aporta justo esos electrones que faltan, en cuatro pasos:

<ol>

<li>

⁠**Inyección.** $U_\mathrm{BE}$ reduce la barrera en la frontera BE. Los electrones del emisor pasan a la base. Esta aportación se llama __inyección__. La densidad de electrones en el borde de la base del lado del emisor crece con $\mathrm{e}^{U_\mathrm{BE}/U_T}$.

</li>

<li>

⁠**Cruce.** En la base p, los electrones son minoría entre muchos huecos. Difunden hacia el borde del lado del colector, donde su densidad es casi nula. La base es mucho más estrecha que la __longitud de difusión__, la distancia media hasta la recombinación, de varias decenas de µ m. Por eso casi todos pasan.

</li>

<li>

⁠**Barrido.** En el borde del lado del colector, el campo de la frontera CB captura cada electrón que llega y lo arrastra al colector. El valor de $U_\mathrm{CB}$ apenas importa: el campo siempre los recoge a todos. Por eso $I_\mathrm{C}$ apenas depende de $U_\mathrm{CE}$.

</li>

<li>

⁠**Reposición.** Quedan dos pequeñas pérdidas: huecos de la base pasan al emisor, y algunos electrones se recombinan en la base. Ambas consumen huecos. El terminal de base debe reponerlos. Esa reposición es la corriente de base. Es pequeña porque el emisor está mucho más dopado que la base y porque la base es muy estrecha.

</li>

</ol>

Los electrones van del emisor al colector. La corriente convencional $I_\mathrm{C}$ se cuenta en sentido opuesto, del colector al emisor ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::abbildung et1/k10basis 2
Arriba: camino de los electrones en el punto de trabajo. La corriente de emisor de 2,01 mA se divide en 2 mA hacia el colector y 10 µ A hacia la base. Abajo: energía de un electrón en función de la posición, esquemática. $U_\mathrm{BE}$ baja el escalón pequeño del emisor, $U_\mathrm{CB}$ aumenta la caída hacia el colector.
:::

:::satz Teorema 2.1 (Corrientes en funcionamiento normal)
<span class="anker" id="satz-2-1"></span>

Si el diodo BE conduce con $U_\mathrm{BE}\gg U_T$ y el colector está por encima de la base, se cumple

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T},\qquad I_\mathrm{B}=\frac{I_\mathrm{C}}{B},\qquad I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}. \tag{2.1}$$
:::

⁠**Cómo leerlo:** $I_\mathrm{C}$ se llama también __corriente de transferencia__, porque se transfiere a través de la base. $I_\mathrm{S}$ en A es diminuta, aquí $1{,}9\cdot10^{-13}$ A, y depende del área y del dopado. $U_T=k_\mathrm{B}T/e$ vale unos 26 mV a 300 K. $B$ no tiene unidad y está entre 10 y 1000. Su valor depende del dopado y de la geometría, y presenta dispersión: los ejemplares de un mismo tipo suelen diferir en un factor 2. **Validez:** la __región activa__ (etapa [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)), con corrientes no demasiado grandes.

:::herleitung Por qué $I_\mathrm{B}$ es proporcional a $I_\mathrm{C}$
Electrones y huecos cruzan la misma barrera. La densidad de electrones en el borde de la base del lado del emisor y la densidad de huecos en el borde del emisor del lado de la base crecen ambas con $\mathrm{e}^{U_\mathrm{BE}/U_T}$. La corriente de colector es proporcional a la primera densidad, igual que la recombinación en la base, y la corriente de huecos a la segunda. Todas las partes llevan el mismo factor, de modo que su cociente $B=I_\mathrm{C}/I_\mathrm{B}$ no depende de $U_\mathrm{BE}$.
:::

**¿Quién controla?** Físicamente controla $U_\mathrm{BE}$, porque solo la tensión reduce la barrera. La corriente de base es el precio que se paga por ello. Aun así, en los circuitos se calcula a menudo con $I_\mathrm{B}$: debido a $I_\mathrm{C}=B\,I_\mathrm{B}$, el transistor se comporta como una fuente de corriente controlada por corriente (CCCS, [Parte 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Ambas visiones describen la misma proporcionalidad. El control mediante $U_\mathrm{BE}$ explica la ley exponencial; la visión mediante $I_\mathrm{B}$ es cómoda cuando una resistencia fija la corriente de base.

**Ejemplo.** $U_\mathrm{BE}=0{,}6$ V da $I_\mathrm{C}=1{,}9\cdot10^{-13}\,\mathrm{A}\cdot\mathrm{e}^{23{,}08}=2{,}00$ mA, $I_\mathrm{B}=10$ µ A, $I_\mathrm{E}=2{,}01$ mA. Son $1{,}25\cdot10^{16}$ electrones por segundo en el colector, y allí llega el 99,5 % de la corriente de emisor. La función exponencial es sensible: $+18$ mV duplican la corriente ($U_T\ln2$), $+60$ mV la multiplican por diez ($U_T\ln10$), $+1$ mV aporta $+3{,}9$ %. **Casos límite:** con $U_\mathrm{BE}=0{,}4$ V circulan solo 0,9 µ A, y el transistor está prácticamente apagado. Para $B\to\infty$ desaparece $I_\mathrm{B}$, e $I_\mathrm{E}=I_\mathrm{C}$.

:::analogie
Un gran canal de agua está cerrado por una compuerta. Un chorro delgado que viene de un canal lateral empuja la compuerta y la abre. Sin chorro de control no pasa nada, cuanto más fuerte es, más agua fluye, y abajo se unen los dos caudales. La imagen sirve para tres afirmaciones: lo pequeño controla lo grande, sin control el transistor bloquea, $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$. No sirve para el mecanismo: en el transistor nada mueve una compuerta, la tensión reduce una barrera, y la relación es exponencial.
:::

:::frage ¿De dónde sale la potencia adicional en la salida?
De la alimentación $U_\mathrm{CC}$. La corriente de colector recorre todo el circuito de salida, y la fuente entrega con ello $U_\mathrm{CC}I_\mathrm{C}$. La señal de entrada solo paga $U_\mathrm{BE}I_\mathrm{B}$ y decide así cuánto entrega la fuente.
:::

:::aufgabe Ejercicio 2 ★★ Contar electrones
<span class="anker" id="aufg-2"></span>

Calcula con el transistor T. (a) ¿Cuántos electrones por segundo alcanzan el colector con $I_\mathrm{C}=2$ mA? (b) ¿Qué $U_\mathrm{BE}$ corresponden a 5 mA y a 0,5 mA? ¿Cuál es la diferencia y por qué no depende de $I_\mathrm{S}$? (c) Otro ejemplar tiene $B=50$. ¿Qué fracción de la corriente de emisor sale por la base?

:::loesung
(a) $2\,\mathrm{mA}/e=1{,}25\cdot10^{16}$ por segundo. (b) $U_\mathrm{BE}=U_T\ln(I_\mathrm{C}/I_\mathrm{S})$ da 0,624 V y 0,564 V. La diferencia es $U_T\ln10=59{,}9$ mV. En la diferencia de dos logaritmos, $I_\mathrm{S}$ se cancela. (c) $I_\mathrm{B}/I_\mathrm{E}=1/(1+B)=1/51=2{,}0$ %.
:::
:::
