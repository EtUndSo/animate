---
title: Visión general: Señales, sistemas LTI y convolución
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210100
summary: Por qué la respuesta a un único impulso describe todo el sistema
tags: 
lang: es
---

## De qué trata

Un sistema recibe una señal y entrega otra: un circuito RC suaviza una tensión, la caja de un altavoz colorea un sonido, un amplificador de medida retrasa y amplifica. La pregunta de este capítulo es: *¿Qué hay que saber de un sistema para poder calcular la salida para cualquier señal de entrada?*

Para la amplia clase de los sistemas lineales e invariantes en el tiempo (sistemas LTI), la respuesta es sorprendentemente breve: la respuesta a un único impulso infinitamente corto. La herramienta que obtiene de esta única respuesta todas las demás es la convolución.

**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Paso bajo RC** con $T=RC=1$ s (por ejemplo $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Tiempos en s, tensiones en V; es decir, se calcula sin dimensiones.

</li>

<li>

⁠**Pulso rectangular** de altura $a=1$ V y duración $T_0=1$ s, que empieza en $t=0$.

</li>

</ul>

:::
