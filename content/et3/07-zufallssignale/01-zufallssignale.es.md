---
title: Visión general: Señales aleatorias
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3270100
summary: Valores medios, distribuciones, densidad espectral de potencia, ruido en sistemas y el receptor óptimo
tags: 
lang: es
---

## De qué trata

El ruido de una resistencia, la voz, un flujo de datos: estas señales no se pueden predecir. No se conoce su evolución exacta, pero sí sus *propiedades en promedio*: qué tamaño tienen típicamente, con qué rapidez cambian, qué frecuencias contienen. Este capítulo muestra cómo se describen estas señales aleatorias, qué hace con ellas un sistema LTI y cómo se reconoce con la mayor seguridad una señal conocida en medio del ruido.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Números aleatorios con distribución uniforme** entre $-\frac12$ y $\frac12$ (varianza $\frac{1}{12}$), también como ruido blanco en tiempo discreto.

</li>

<li>

⁠**Resistencia** $R=1\,\mathrm{k\Omega}$ a 290 K, ancho de banda de 20 kHz (audio).

</li>

<li>

⁠**Sistema recursivo** $g(n)=s(n)+0{,}6\,g(n-1)$ de la [parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html).

</li>

</ul>

El script `rechnung_kap7.py` recalcula los números, en parte como control con números aleatorios simulados.
:::
