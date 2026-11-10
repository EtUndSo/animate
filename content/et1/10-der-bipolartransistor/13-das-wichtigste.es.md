---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El transistor bipolar
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Capítulo 10: El transistor bipolar
order: 1201300
summary: Cómo una pequeña tensión controla una gran corriente a través de un diodo bloqueado
tags: emisor, base, colector, ganancia de corriente, punto de trabajo, realimentación negativa, transconductancia
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

El __emisor__ cede electrones, la delgada __base__ los deja pasar y el __colector__ los recoge. La tensión $U_\mathrm{BE}$ decide cuántos electrones se ponen en marcha: $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$. El campo del diodo de colector bloqueado los barre, y solo un pequeño resto circula por la base, $I_\mathrm{B}=I_\mathrm{C}/B$. El factor $B$ se llama __ganancia de corriente__.

</li>

<li>

Tres terminales significan dos tensiones independientes. Por eso $I_\mathrm{C}$ es una superficie sobre $U_\mathrm{BE}$ y $U_\mathrm{CE}$, y cada curva característica es una sección de ella. Sobre esta superficie, el circuito externo elige el __punto de trabajo__, el estado de corriente continua del transistor. Una resistencia de emisor lo fija mediante __realimentación negativa__: el efecto debilita su propia causa.

</li>

<li>

Para señales pequeñas, la tangente sustituye a la curva. Su pendiente, la __transconductancia__ $S=I_\mathrm{C}/U_T$, convierte el transistor en una fuente de corriente controlada. La ganancia de tensión del circuito de emisor común, el circuito estándar con el emisor a masa, es la tensión continua en la resistencia de colector dividida por $U_T$.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$, $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$. Tres terminales significan dos tensiones libres, $I_\mathrm{C}$ es una superficie, cada curva característica una sección.

</li>

<li>

Mecanismo: $U_\mathrm{BE}$ reduce la barrera, los electrones cruzan la delgada base, el campo del diodo CB bloqueado los barre: $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{C}/B$. La corriente de base solo repone las pocas pérdidas.

</li>

<li>

Regiones: región de corte (abierto), activa ($I_\mathrm{C}=B\,I_\mathrm{B}$, $U_\mathrm{CE}\ge0{,}2$ V), saturación ($U_\mathrm{CE}=0{,}2$ V, $I_\mathrm{C}\le B\,I_\mathrm{B}$). Suponer, calcular, comprobar. Interruptor: extremos de la recta de carga. Amplificador: activa, en el centro.

</li>

<li>

Realimentación negativa: $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/\bigl(R_\mathrm{E}(1+1/B)+R_\mathrm{i}/B\bigr)$. Más corriente eleva el emisor y reduce $U_\mathrm{BE}$. Espejo de corriente: $I_\mathrm{C2}=I_\mathrm{ref}/(1+2/B)$. Regulador: $U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}$.

</li>

<li>

Pequeña señal: $S=I_\mathrm{C}/U_T$, $r_\mathrm{BE}=B/S$, $r_\mathrm{CE}\approx U_\mathrm{Early}/I_\mathrm{C}$. La tangente vale para $|u_\mathrm{be}|\ll U_T$.

</li>

<li>

Emisor común $A=-U_{R_\mathrm{C}}/U_T$, colector común $A\approx1$, base común $A=+S\,R_\mathrm{C}$. Con $R_\mathrm{E}$ es $A\approx-R_\mathrm{C}/R_\mathrm{E}$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** El transistor tiene dos fronteras con dos tareas. En la frontera base-emisor se controla: la tensión allí fija exponencialmente cuántos electrones arrancan. En la frontera colector-base solo se recoge: lo que llega es barrido, y la tensión allí apenas importa.

| Resultado | De dónde viene |
|---|---|
| $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$, dos tensiones libres | Tres terminales, leyes de los nudos y de las mallas (etapa [1](drei-schichten-zwei-spannungen.html#stufe-1)) |
| $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{C}/B$ | Arrancar, cruzar la delgada base, ser barrido (etapa [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2)) |
| Muchas curvas características | Secciones de una superficie: abrupta en $U_\mathrm{BE}$, plana en $U_\mathrm{CE}$ (etapa [3](eine-flache-viele-kennlinien.html#stufe-3)) |
| Tres regiones de funcionamiento | Cuál de las dos fronteras conduce (etapa [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)) |
| Punto de trabajo | La ecuación del transistor y la malla deben cumplirse a la vez (etapa [5](der-arbeitspunkt.html#stufe-5)) |
| Interruptor, inversor | Los dos extremos de la recta de carga: poca potencia en el transistor (etapa [6](der-transistor-als-schalter.html#stufe-6)) |
| Punto de trabajo estable | Más corriente eleva el emisor y reduce $U_\mathrm{BE}$ (etapa [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7)) |
| Espejo de corriente, regulador de tensión | Igual $U_\mathrm{BE}$ significa igual corriente, y $U_\mathrm{BE}$ permanece casi constante (etapa [8](zwei-schaltungen-die-nutzen.html#stufe-8)) |
| $S=I_\mathrm{C}/U_T$ | La pendiente de una función exponencial es su valor dividido por la escala $U_T$ (etapa [9](tangente-statt-kurve.html#stufe-9)) |
| $\vert A\vert =U_{R_\mathrm{C}}/U_T$ | Variación de corriente $S\,u_\mathrm{ent}$ por $R_\mathrm{C}$ (etapa [10](drei-grundschaltungen.html#stufe-10)) |
