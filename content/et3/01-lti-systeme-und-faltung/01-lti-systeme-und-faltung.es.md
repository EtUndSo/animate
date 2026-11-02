---
title: Visión general: Señales, sistemas LTI y convolución
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas LTI y convolución
order: 3210100
summary: Por qué la respuesta a un único impulso describe todo el sistema
tags: 
lang: es
---

## De qué trata

Un sistema recibe una señal y entrega otra: un circuito RC suaviza una tensión, la caja de un altavoz colorea un sonido, un amplificador de medida retrasa y amplifica. La pregunta de este capítulo es: *¿Qué hay que saber de un sistema para poder calcular la salida para cualquier señal de entrada?*

Para la amplia clase de los sistemas lineales e invariantes en el tiempo (sistemas LTI), la respuesta es sorprendentemente breve: la respuesta a un único impulso infinitamente corto. La herramienta que obtiene de esta única respuesta todas las demás es la convolución.



**Cómo trabajar con este capítulo.** Cada etapa es un artículo breve con la idea, preguntas típicas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio. Termina una etapa antes de pasar a la siguiente.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Paso bajo RC** con $T=RC=1$ s (por ejemplo $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Tiempos en s, tensiones en V; es decir, se calcula sin dimensiones.

</li>

<li>

⁠**Pulso rectangular** de altura $a=1$ V y duración $T_0=1$ s, que empieza en $t=0$.

</li>

</ul>

El script `rechnung_kap1.py` recalcula los números y las curvas.
:::
