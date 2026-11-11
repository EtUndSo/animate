---
title: Visión general: Corriente, resistencia y leyes de Kirchhoff
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1120100
summary: Por qué los electrones se arrastran y la corriente está ahí al instante, y por qué las redes obedecen leyes de conservación
tags: corriente, resistencia, ley de Ohm, ley de los nudos, ley de las mallas
lang: es
---

## De qué trata

Al cerrar un circuito, la lámpara se enciende en el mismo instante. Y eso que los electrones del hilo se arrastran unas 2000 veces más despacio que un caracol. Una __corriente__ es carga en movimiento, medida como carga por unidad de tiempo. Una __resistencia__ es un componente que frena este movimiento y convierte su energía en calor. La pregunta de este capítulo es: *¿Cómo se convierte una tensión en una corriente, y cómo se reparte esta en una red de muchos componentes?*

La respuesta consta de tres leyes. La __ley de Ohm__ relaciona la tensión y la corriente en un componente. La __ley de los nudos__ dice que en una bifurcación no desaparece corriente. La __ley de las mallas__ dice que las tensiones a lo largo de un camino cerrado suman cero.

**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Cadena:** la batería de 9 V del [capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) conectada a dos resistencias en serie, $R_1=2\,\mathrm{k\Omega}$ y $R_2=1\,\mathrm{k\Omega}$. Circulan 3 mA, en $R_1$ hay 6 V y en $R_2$ hay 3 V.

</li>

<li>

⁠**Hilo:** cobre, longitud $L=1$ m, sección $A=0{,}5\,\mathrm{mm^2}$, resistividad (constante del material, etapa [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3)) $\rho=1{,}7\cdot10^{-8}\,\mathrm{\Omega\,m}$, densidad de electrones libres $n=8{,}5\cdot10^{28}\,\mathrm{m^{-3}}$ (uno por átomo). Conduce los 3 mA de la cadena.

</li>

<li>

⁠**Red:** una fuente de 9 V y cinco resistencias entre cuatro puntos de bifurcación, $R_\mathrm a=2$, $R_\mathrm b=5$, $R_\mathrm c=3$, $R_\mathrm d=1$, $R_\mathrm e=2$ (todas en $\mathrm{k\Omega}$), fig. [7](knoten-zweige-maschen.html#abb-7).

</li>

<li>

⁠**Constantes:** $e=1{,}602\cdot10^{-19}$ C, $m_\mathrm e=9{,}109\cdot10^{-31}$ kg.

</li>

</ul>

:::
