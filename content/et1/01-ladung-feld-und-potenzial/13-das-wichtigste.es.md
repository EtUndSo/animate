---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1111300
summary: Por qué la tensión es una diferencia y qué hace con una carga
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

La carga es una propiedad de los electrones y los protones, los componentes cargados de los átomos. Las cargas del mismo signo se repelen, las de signo opuesto se atraen, y la suma de todas las cargas se conserva.

</li>

<li>

Toda carga crea un campo a su alrededor. El campo $\vec E$ determina en cada lugar la fuerza por unidad de carga: $\vec F=Q\,\vec E$.

</li>

<li>

En un campo estático, el trabajo sobre una carga solo depende del inicio y del final, no del camino. Por eso cada punto tiene un potencial $\varphi$, y la tensión $U_{12}=\varphi_1-\varphi_2$ es la energía por unidad de carga que el campo cede en el camino del punto 1 al punto 2.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Magnitud = valor numérico $\cdot$ unidad. $1\,\mathrm{V}=1\,\mathrm{J/C}$, $1\,\mathrm{C}=1\,\mathrm{A\,s}$, $1\,\mathrm{N}=1\,\mathrm{kg\,m/s^2}$.

</li>

<li>

Trabajo: $W=\int\vec F\cdot\mathrm{d}\vec s$, en línea recta $F\,s\cos\alpha$. Energía cinética: $\frac12mv^2$.

</li>

<li>

Carga: $Q=(N_\mathrm{p}-N_\mathrm{e})\,e$; se conserva.

</li>

<li>

Coulomb: $F=k\,|Q_\mathrm{A}Q_\mathrm{B}|/r^2$; las cargas del mismo signo se repelen y las de signo opuesto se atraen.

</li>

<li>

Campo: $\vec F=Q\vec E$, dirección como la fuerza sobre una carga positiva; carga puntual $E=k|Q_0|/r^2$.

</li>

<li>

Líneas de campo: de $+$ a $-$, nunca se cortan, perpendiculares a los conductores; en el metal $\vec E=0$.

</li>

<li>

Trabajo del campo: $W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$; irrotacional: $\oint\vec E\cdot\mathrm{d}\vec s=0$.

</li>

<li>

Potencial: $\varphi(P)=\int_P^{P_0}\vec E\cdot\mathrm{d}\vec s$; carga puntual $\varphi=kQ_0/r$; $\vec E$ apunta hacia $\varphi$ decreciente.

</li>

<li>

Tensión: $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=W_{12}/Q$, $U_{21}=-U_{12}$; campo uniforme $E=U/d$.

</li>

<li>

Masa: $\varphi:=0$; su posición no cambia ninguna tensión.

</li>

<li>

Carga en el campo: $\frac12mv^2+Q\varphi$ constante; desde el reposo $v=\sqrt{2|QU|/m}$.

</li>

<li>

Inducción: $u_\mathrm{ind}=-N\,\mathrm{d}\Phi/\mathrm{d} t$; entonces el campo ya no es irrotacional.

</li>

</ul>
:::

**Mirada al [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html).** En un cable, el campo impulsa muchísimas cargas a la vez: fluye carga, surge una corriente. El [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) muestra por qué la tensión y la corriente son proporcionales y cómo se reparten en una red.

**Un principio detrás de todos los resultados.** La fuerza y la energía de una carga dependen de las demás cargas de alrededor y de ella misma. Al dividir por la propia carga queda una propiedad del lugar: la fuerza se convierte en intensidad de campo; la energía, en potencial.

| Resultado | De dónde viene |
|---|---|
| Intensidad de campo $\vec E=\vec F/Q$ | Fuerza por unidad de carga: la carga de prueba desaparece al dividir (etapa [4](die-feldstarke.html#stufe-4)) |
| Líneas de campo, apantallamiento | Imagen de $\vec E$; los electrones libres del metal se colocan de modo que no quede ninguna fuerza (etapa [5](feldlinien-und-leiter.html#stufe-5)) |
| $W_{12}=Q\int\vec E\cdot\mathrm{d}\vec s$, independiente del camino | El trabajo es fuerza por camino; las fuerzas de Coulomb son radiales, solo cuenta la distancia (etapa [6](arbeit-im-feld.html#stufe-6)) |
| Potencial $\varphi$ | Trabajo por unidad de carga hasta el punto de referencia (etapa [7](das-potenzial.html#stufe-7)) |
| Tensión, masa | Trabajo por unidad de carga entre dos puntos; el cero se elige libremente (etapa [8](spannung-und-masse.html#stufe-8)) |
| Velocidad de una carga | La energía $QU$ se convierte en energía cinética (etapa [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9)) |
| Inducción | Límite del principio: si cambia un campo magnético, el trabajo depende del camino (etapa [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10)) |
