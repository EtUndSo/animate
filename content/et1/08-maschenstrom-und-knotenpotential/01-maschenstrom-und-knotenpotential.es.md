---
title: Visión general: Análisis por mallas y por nudos
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Análisis por mallas y por nudos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Capítulo 8: Análisis por mallas y por nudos
order: 1180100
summary: Por qué a una red le bastan pocas incógnitas
tags: 
lang: es
---

## De qué trata

La red del [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) tiene seis ramas. Cada una lleva una corriente y una tensión, lo que da doce incógnitas, y solo tras largas sustituciones quedaron tres ecuaciones. Un circuito con transistores tiene cientos de ramas. La pregunta de este capítulo es: *¿Cuán pocas incógnitas bastan para una red entera, y cómo se escriben las ecuaciones sin tener que despejar?*



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke La red modelo de este capítulo
<ul>

<li>

⁠**La red** (fig. [1](wie-viele-groen-sind-frei.html#abb-1)) tiene tres nudos: la masa 0 y los nudos 1 y 2. A la izquierda alimenta una batería con $U_\mathrm q=9$ V y resistencia interna $R_1=1\,\mathrm{k\Omega}$ ([capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)); a la derecha, una fuente de corriente real con $I_\mathrm q=4$ mA y $R_5=5\,\mathrm{k\Omega}$ en paralelo. Entre ellas están $R_2=4\,\mathrm{k\Omega}$ de 1 a masa, $R_3=2\,\mathrm{k\Omega}$ de 1 a 2 y $R_4=10\,\mathrm{k\Omega}$ de 2 a masa.

</li>

<li>

⁠**El amplificador** (etapa [8](gesteuerte-quellen-und-verstarker.html#stufe-8)) es el modelo del [capítulo 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html): resistencia de entrada $R_\mathrm i=2\,\mathrm{k\Omega}$, fuente de corriente controlada con $g=50$ mS, resistencia de salida $R_\mathrm o=20\,\mathrm{k\Omega}$, carga $R_\mathrm L=5\,\mathrm{k\Omega}$.

</li>

<li>

⁠**Unidades:** Se calcula en V, mA, k$\Omega$ y mS. Como $\mathrm{k\Omega\cdot mA}=\mathrm V$ y $\mathrm{mS\cdot V}=\mathrm{mA}$, no aparecen potencias de diez. El script `rechnung_kap8.py` comprueba todos los números.

</li>

</ul>
:::
