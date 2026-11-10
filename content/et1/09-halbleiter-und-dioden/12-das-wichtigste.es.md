---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1191200
summary: Cómo el silicio se convierte en una válvula para la corriente y cómo se calcula con ella
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

En la unión pn, las cargas móviles pasan a la otra región y dejan atrás iones fijos. El campo de estos iones crea en la zona de carga espacial una barrera que detiene la igualación.

</li>

<li>

El calor eleva solo la fracción $\mathrm{e}^{-W/(k_\mathrm BT)}$ de los portadores de carga por encima de una barrera de altura $W$. Una tensión en sentido directo reduce la barrera, así que la corriente crece exponencialmente, un factor 10 por cada 60 mV: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$. En sentido inverso solo queda la diminuta corriente $-I_\mathrm S$.

</li>

<li>

En un circuito, el punto de trabajo está en la intersección de la curva característica con la recta de carga (la recta que imponen la fuente y la resistencia). Para los cálculos a mano, el diodo se convierte en un interruptor con una tensión directa fija, y para pequeños cambios alrededor del punto de trabajo, en una resistencia $r=U_T/I$.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Bandas: $W_\mathrm g$ (silicio 1,12 eV), fracción $\mathrm{e}^{-W/(k_\mathrm BT)}$; los portadores son electrones en la BC y huecos en la BV.

</li>

<li>

Dopado: los donadores dan $n\approx N_\mathrm D$, los aceptores $p\approx N_\mathrm A$, en todas partes $n\,p=n_\mathrm i^2$. El cristal sigue siendo neutro.

</li>

<li>

Unión pn: difusión, recombinación, iones fijos, campo. $U_\mathrm{D0}=U_T\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$.

</li>

<li>

Curva característica: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$, $U_T=k_\mathrm BT/e=25{,}85$ mV a 300 K, 60 mV por década, sin umbral.

</li>

<li>

La ruptura es reversible mientras el calor siga limitado. Diodo Zener: $U_\mathrm Z$, $r_\mathrm Z$. Diodo varicap: $C_\mathrm{j}=\varepsilon A/w$. Fotodiodo: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)-I_\mathrm{Ph}$, célula solar $U_\mathrm L=U_T\ln(I_\mathrm{Ph}/I_\mathrm S+1)$.

</li>

<li>

Punto de trabajo: intersección de la curva característica y la recta de carga $I=(U_0-U_\mathrm D)/R$; iterar mediante $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$.

</li>

<li>

Modelos: en conducción $U_\mathrm D=0$ o $U_\mathrm F$, en bloqueo $I_\mathrm D=0$. Suponer, calcular, comprobar: $I_\mathrm D>0$ y $U_\mathrm D<U_\mathrm F$.

</li>

<li>

Pequeña señal: $r=U_T/I$ para $|u_\mathrm D|\ll U_T$. No confundir con $U_\mathrm D/I$.

</li>

<li>

Puente: pico $\hat u-2U_\mathrm F$, pausa con $|u_\mathrm e|<2U_\mathrm F$. Bomba de carga: $U_\mathrm a\to2U_\mathrm e-2U_\mathrm F$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** El calor reparte la energía al azar, y la fracción de partículas por encima de una energía cae exponencialmente con esa energía. Casi todo en este capítulo se deduce de ello en cuanto se pregunta qué energía cuenta en cada caso.

| Resultado | De dónde viene |
|---|---|
| El silicio puro apenas conduce | La brecha de banda (energía hasta el electrón libre) es 43 veces mayor que la energía térmica (etapa [1](warum-silizium-kaum-leitet.html#stufe-1)) |
| El dopado aporta un portador de carga por casi cada átomo de impureza | El electrón está ligado con solo 1,7 veces la energía térmica (etapa [2](dotierung.html#stufe-2)) |
| Tensión de difusión $U_\mathrm{D0}$ | La barrera crece hasta que la fracción por encima de ella iguala la relación de densidades (etapa [3](die-raumladungszone.html#stufe-3)) |
| $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$ | La tensión desplaza la barrera y con ella la fracción (etapa [4](warum-der-strom-exponentiell-wachst.html#stufe-4)) |
| $U_\mathrm D$ casi constante, modelo de interruptor | La corriente cambia un factor 10 por cada 60 mV (etapas [6](der-arbeitspunkt.html#stufe-6) y [7](lineare-ersatzschaltungen.html#stufe-7)) |
| $r=U_T/I$ | La derivada de la función exponencial es la propia función (etapa [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)) |
