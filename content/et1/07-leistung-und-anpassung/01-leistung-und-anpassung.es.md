---
title: Visión general: Potencia, adaptación y rendimiento
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Potencia, adaptación y rendimiento
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Capítulo 7: Potencia, adaptación y rendimiento
order: 1170100
summary: Por qué en el máximo de potencia la mitad de la energía se queda en la fuente
tags: resistencia interna, carga, potencia
lang: es
---

## De qué trata

Una batería de 9 V tiene 2 $\Omega$ de __resistencia interna__, la resistencia que la corriente debe vencer dentro de la propia fuente. Alimenta una __carga__, el aparato conectado. ¿Qué valor debe tener la carga para que a ella llegue la mayor __potencia__ posible, es decir, la mayor energía por unidad de tiempo? La respuesta es 2 $\Omega$, y tiene un precio: la mitad de la energía se queda entonces como calor en la batería. La pregunta de este capítulo es: *¿De dónde viene la potencia, adónde va, y por qué el máximo está justo en un aprovechamiento del 50 %?*



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Batería:** la batería de 9 V del [capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html), con la tensión de fuente $U_\mathrm{q}=9$ V (la tensión que aporta la química) y la resistencia interna $R_\mathrm{i}=2\,\Omega$. El [capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) la llama $R_\mathrm{q}$ en una fuente individual. La corriente de cortocircuito es $I_\mathrm{CC}=4{,}5$ A.

</li>

<li>

⁠**Carga:** una resistencia $R_\mathrm{L}$ de 16, 8, 2 o 0,5 $\Omega$.

</li>

<li>

⁠**Otros:** $R=5\,\Omega$ con una tensión sinusoidal de 10 V de valor de pico (etapa [3](mittlere-leistung-bei-sinusspannung.html#stufe-3)), una línea con $R_\mathrm{cable}=1\,\Omega$ delante de una carga de 40 kW (etapa [4](leitungsverluste.html#stufe-4)).

</li>

</ul>

El script `rechnung_kap7.py` comprueba todos los números.
:::
