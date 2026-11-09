---
title: Etapa 1: Energía por carga multiplicada por carga por tiempo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170200
summary: La tensión dice cuánta energía cede una carga; la corriente, cuánta carga pasa.
tags: 
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
La tensión dice cuánta energía cede una carga; la corriente, cuánta carga pasa. Esta etapa une ambas en la energía por unidad de tiempo.
:::

**La idea.** Entre los terminales de un componente hay una tensión $U$. Según la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), cada culombio que pasa del potencial más alto al más bajo cede la energía $U$ en julios. La corriente $I$ cuenta cuántos culombios pasan por segundo. Por tanto, cada segundo se transforman $U\cdot I$ julios (fig. [1](#abb-1)). Hacen falta ambos factores: una tensión sin corriente no transforma nada, porque no se mueve carga. Una corriente sin tensión no transforma nada, porque ninguna carga cede nada.

:::abbildung et1/k7ladung 1
Carga con 8 V y 0,5 A. Abajo, la evolución del potencial: cada culombio pierde 8 J. Se dibujan cargas positivas en el sentido de la corriente. Los electrones se mueven en sentido contrario; el resultado es el mismo.
:::

:::definition Definición 1.1 (Energía y potencia)
<span class="anker" id="satz-1-1"></span>

Si la carga $\mathrm{d} Q$ atraviesa la tensión $u$, cede la energía $\mathrm{d} W=u\,\mathrm{d} Q$. Con la corriente $i=\mathrm{d} Q/\mathrm{d} t$ se obtiene

<span class="anker" id="gl-1-1"></span>
$$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t),\qquad W=\int u\,\mathrm{d} Q=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t. \tag{1.1}$$

Para magnitudes continuas, es decir, cuando $U$ e $I$ no dependen del tiempo, se tiene

<span class="anker" id="gl-1-2"></span>
$$W=U\,I\,\Delta t,\qquad P=\frac{W}{\Delta t}=U\,I. \tag{1.2}$$
:::

⁠**Cómo leerlo:** $u$ en V, $i$ en A, $p$ en vatios: $[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$. Un LED indicador transforma 20 mW, un hervidor eléctrico 2 kW, un grupo de una central eléctrica 1 GW. La expresión $W/\Delta t$ es, en general, el valor medio de la potencia durante el tiempo $\Delta t$; $p(t)$ es su valor instantáneo. Los aparatos suelen funcionar de forma continua; por eso se caracterizan por la potencia y no por la energía. Para la energía se cumple $1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m}$. La ingeniería eléctrica calcula sobre todo en vatios-segundo o kilovatios-hora, $1\,\mathrm{kWh}=3{,}6\,\mathrm{MJ}$. El julio es habitual en los procesos de combustión; el newton-metro, en el trabajo mecánico.

⁠**Signos:** En el convenio receptor (CR, [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), $p>0$ significa que el componente absorbe energía, y $p<0$, que la cede. En el convenio generador (CG) es al revés. **Validez:** $p=u\,i$ vale para todo monopuerto si $u$ e $i$ se cuentan en el mismo par de terminales. No se presupone nada sobre el interior del componente.

:::herleitung Por qué solo cuentan la tensión y la corriente
En el tiempo $\mathrm{d} t$ entra por el terminal 1 la carga $\mathrm{d} Q=i\,\mathrm{d} t$ y sale por el terminal 2 la misma carga (ley de los nudos, [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). El interior no cambia. Para el balance es como si $\mathrm{d} Q$ hubiera pasado directamente de $\varphi_1$ a $\varphi_2$. Según la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), la energía cedida es $\mathrm{d} W=(\varphi_1-\varphi_2)\,\mathrm{d} Q=u\,i\,\mathrm{d} t$. Al dividir por $\mathrm{d} t$ se obtiene [(1.1)](#gl-1-1). Los electrones se mueven en sentido contrario y tienen carga negativa. Ambos signos juntos dan el mismo producto.
:::

::::beispiel
En $R_\mathrm{L}=16\,\Omega$ hay 8 V y circulan 0,5 A ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Cada culombio cede 8 J y cada segundo llegan 0,5 C: $P=4$ W. En una hora son $W=4\,\mathrm{W}\cdot3600\,\mathrm{s}=14{,}4\,\mathrm{kJ}=4\,\mathrm{Wh}$. Contados uno a uno, pasan por segundo $I/e=3{,}12\cdot10^{18}$ electrones, y cada uno cede $e\cdot8\,\mathrm{V}=1{,}28\cdot10^{-18}$ J. El producto vuelve a ser 4 W.
::::

⁠**Casos límite:** Con los terminales abiertos hay 9 V y 0 A, es decir, $P=0$. Un hilo ideal tiene $U=0$, es decir, $P=0$ con cualquier corriente.

:::frage ¿Se consume corriente en el componente?
No. Antes y después del componente circula la misma corriente; la carga vuelve a salir por completo. Lo que se consume es energía: la carga sigue su camino a un potencial más bajo. Por eso, en la factura del «consumo de electricidad» aparecen kilovatios-hora.
:::

:::aufgabe Ejercicio 1 ★ Energía y signo
<span class="anker" id="aufg-1"></span>

(a) Una batería recargable de 3,7 V almacena la carga 2 Ah (2 A durante una hora). ¿Cuánta energía es en Wh y en kJ? ¿Cuánto tiempo alimenta un aparato de 0,74 W? (b) Un hervidor eléctrico de 2 kW funciona 3 minutos. ¿Cuántos kWh son y cuánto cuestan a 30 ct/kWh? (c) En un monopuerto se miden, en el convenio receptor, $U=12$ V e $I=-3$ A. ¿Absorbe potencia o la entrega?

:::loesung
(a) $Q=2\,\mathrm{A}\cdot3600\,\mathrm{s}=7200$ C, es decir, $W=3{,}7\,\mathrm{V}\cdot7200\,\mathrm{C}=26{,}64$ kJ $=7{,}4$ Wh. Con 0,74 W dura 10 h. (b) $W=2\,\mathrm{kW}\cdot0{,}05\,\mathrm{h}=0{,}1$ kWh, que cuestan 3 ct. (c) $P=12\,\mathrm{V}\cdot(-3\,\mathrm{A})=-36$ W. El monopuerto entrega 36 W.
:::
:::
