---
title: Desde cero: Terminales, curva característica, linealidad
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Fuentes y fuentes equivalentes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Capítulo 5: Fuentes y fuentes equivalentes
order: 1150200
summary: Por qué dos números sustituyen a toda una red
tags: terminal, monopuerto, curva característica, Circuito abierto, lineal
lang: es
---

Un __terminal__ es un punto de conexión hacia el exterior. Un __monopuerto__ es una red con exactamente dos terminales que forman un par: la corriente que sale por A vuelve a entrar por B, porque la carga no se pierde (ley de los nudos, [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Por eso, un monopuerto solo tiene una corriente y una tensión. Es un dipolo del [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), aunque por dentro contenga muchos componentes. La __curva característica__ es la relación entre estas dos magnitudes. En este capítulo aparece siempre en el mismo diagrama: corriente en los terminales en horizontal, tensión en los terminales en vertical.

Las flechas de referencia valen para todo el capítulo: $U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ cuenta de A a B, $I_\mathrm{A}$ cuenta hacia fuera del terminal A. Para la carga conectada, ambas flechas apuntan en el mismo sentido (convenio receptor, [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)); para el propio monopuerto, en sentidos opuestos (convenio generador). Si ambas son positivas, el monopuerto entrega potencia. __Circuito abierto__ significa: los terminales están abiertos, $I_\mathrm{A}=0$. Cortocircuito significa: los terminales están unidos por un cable, $U_\mathrm{AB}=0$.

Un componente es __lineal__ si su corriente es proporcional a su tensión. Una resistencia lo es mientras $R$ no dependa de la corriente: su curva característica es una recta que pasa por el origen. Una lámpara incandescente o un diodo ([capítulo 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) no lo son. El signo $\parallel$ representa la resistencia de una conexión en paralelo, $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$ ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Tiene prioridad sobre el signo más, igual que la multiplicación.
