---
title: Visión general: Funciones de correlación
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Funciones de correlación
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Capítulo 6: Funciones de correlación
order: 3260100
summary: ¿Cuánto se parecen dos señales y cómo se reparte la energía en frecuencia?
tags: 
lang: es
---

## De qué trata

Un radar emite un pulso y busca su eco en la señal recibida. Un teléfono móvil busca en el ruido una secuencia de sincronización conocida. Ambos se plantean la misma pregunta: *¿Cuánto se parece una señal a otra y con qué desplazamiento se parecen más?* La respuesta la da la función de correlación. Su transformada de Fourier indica además cómo se reparte la energía de una señal entre las frecuencias.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
Pulso rectangular $\operatorname{rect}(t)$, triángulo $\Lambda(t)$, pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$ (la respuesta al impulso del circuito RC con $RC=1$ s) y la secuencia $(1,2,1)$. El script `rechnung_kap6.py` recalcula los números.
:::
