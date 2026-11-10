---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Fuentes y fuentes equivalentes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Capítulo 5: Fuentes y fuentes equivalentes
order: 1151300
summary: Por qué dos números sustituyen a toda una red
tags: superposición, tensión de circuito abierto, resistencia interna, fuente equivalente, cortocircuito
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

En una red lineal, los efectos de las fuentes se suman, porque todas las ecuaciones son lineales. Esto es la __superposición__, el solapamiento de los efectos.

</li>

<li>

Por eso, la tensión entre dos terminales A y B es una recta en función de la corriente en los terminales: $U_\mathrm{AB}=U_\mathrm{CA}-R_\mathrm{i}\,I_\mathrm{A}$. Las fuentes fijan la __tensión de circuito abierto__ $U_\mathrm{CA}$ (la tensión con los terminales abiertos); las resistencias, la __resistencia interna__ $R_\mathrm{i}$ (la pendiente).

</li>

<li>

Una recta tiene dos números. Así, la red se comporta como una __fuente equivalente__, una fuente con resistencia interna. El circuito abierto y el __cortocircuito__ (terminales unidos) proporcionan los números: $R_\mathrm{i}=U_\mathrm{CA}/I_\mathrm{CC}$.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Serie: sumar resistencias, misma corriente. Paralelo: sumar conductancias, misma tensión. Agrupar de dentro hacia fuera.

</li>

<li>

Los nudos de igual potencial se pueden unir, las ramas sin corriente se pueden cortar. La simetría muestra dónde es posible.

</li>

<li>

Estrella y triángulo son intercambiables en los terminales: $R_{10}=R_{12}R_{31}/(R_{12}+R_{23}+R_{31})$.

</li>

<li>

Las fuentes ideales mantienen fija una magnitud. Fuentes reales: $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}$. Conversión: $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$, misma resistencia.

</li>

<li>

Superposición: las fuentes de tensión se vuelven cables, las fuentes de corriente huecos, y los efectos parciales se suman. Las potencias no se suman.

</li>

<li>

Todo monopuerto lineal es una recta: $U_\mathrm{i}=U_\mathrm{CA}$, $I_\mathrm{i}=I_\mathrm{CC}$, $R_\mathrm{i}=U_\mathrm{CA}/I_\mathrm{CC}$. El punto de trabajo es la intersección con la recta de la carga.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** En dos terminales, una red lineal se comporta como una sola recta en el diagrama corriente-tensión; por eso bastan dos números. Desde fuera solo cuenta esta curva característica: dos circuitos con la misma recta son intercambiables, sea cual sea su aspecto por dentro. La tabla asigna los resultados a esta idea.

| Resultado | De dónde viene |
|---|---|
| Resistencia total | Sin fuente, la curva característica pasa por el origen y basta un número (etapa [1](widerstande-zusammenfassen.html#stufe-1)) |
| Simetría, semicircuito | Los potenciales iguales se pueden unir, las ramas sin corriente se pueden cortar (etapa [2](symmetrie-nutzen.html#stufe-2)) |
| Estrella y triángulo | Tres terminales, tres números, por tanto intercambiables (etapa [3](stern-und-dreieck.html#stufe-3)) |
| Fuentes ideales | Casos límite de la recta: horizontal y vertical (etapa [4](ideale-quellen.html#stufe-4)) |
| Punto de trabajo | Intersección de la recta de la fuente con la recta de carga (etapa [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5)) |
| Conversión de fuentes | La misma recta, leída desde el otro eje (etapa [6](spannungsquelle-oder-stromquelle.html#stufe-6)) |
| Conectar fuentes entre sí | Las rectas se suman en tensión o en corriente (etapa [7](quellen-zusammenschalten.html#stufe-7)) |
| Superposición | Ecuaciones lineales, cada fuente actúa por sí sola (etapa [8](uberlagerung.html#stufe-8)) |
| Thévenin y Norton | Superposición con la corriente en los terminales como causa adicional (etapa [9](thevenin-und-norton.html#stufe-9)) |
| Convertidor R-2R | Cada interruptor es una fuente, cada peldaño divide por dos (etapa [10](der-r-2r-wandler.html#stufe-10)) |
