---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1121200
summary: Por qué los electrones se arrastran y la corriente está ahí al instante, y por qué las redes obedecen leyes de conservación
tags: velocidad de deriva, densidad de corriente, divisor de tensión
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

El campo en el conductor acelera los electrones libres, y las colisiones les quitan de nuevo la velocidad ganada. Queda una pequeña __velocidad de deriva__ (velocidad media a lo largo del conductor), proporcional al campo. Por eso la __densidad de corriente__, la corriente por unidad de sección, es proporcional al campo, y para el componente se deduce $U=R\,I$.

</li>

<li>

La ley de los nudos es la conservación de la carga; la ley de las mallas es la conservación de la energía.

</li>

<li>

Juntas, las tres leyes dan para cada red exactamente tantas ecuaciones como incógnitas tiene. En serie se reparte la tensión (__divisor de tensión__: dos resistencias cuya relación fija una tensión parcial); en paralelo se reparte la corriente.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Corriente: $i=\mathrm{d} Q/\mathrm{d} t$, $I=q\,v\,A$; densidad de corriente $\vec j=q\,\vec v$.

</li>

<li>

Deriva: $\vec v_\mathrm D=-\mu\,\vec E$, $v_\mathrm D=I/(n\,e\,A)$; corriente al instante, porque viaja el campo.

</li>

<li>

Material: $\vec j=\sigma\,\vec E$, $\sigma=n\,e\,\mu=1/\rho$.

</li>

<li>

Componente: $U=R\,I$, $R=\rho\,L/A$, $G=1/R$; potencia $P=U\,I$.

</li>

<li>

Serie E: $w=(\sqrt[N]{10})^i$; temperatura: $R(\vartheta)=R(\vartheta_0)(1+\alpha\,(\vartheta-\vartheta_0))$; PTC, NTC.

</li>

<li>

Dipolo: curva característica $I=f(U)$; CR mismo sentido, CG sentidos opuestos; los electrones se mueven contra la corriente convencional.

</li>

<li>

Red: $k$ nudos, $z$ ramas, $m=z-k+1$ mallas independientes; árbol de $k-1$ ramas.

</li>

<li>

Ley de los nudos: $\sum I=0$, $k-1$ ecuaciones; ley de las mallas: $\sum U=0$, $z-k+1$ ecuaciones.

</li>

<li>

Serie: $R_\mathrm{tot}=\sum R_i$, $U_\nu/U=R_\nu/\sum R_i$, solo sin carga.

</li>

<li>

Paralelo: $G_\mathrm{tot}=\sum G_i$, $R_1\parallel R_2=R_1R_2/(R_1+R_2)$, $I_1=I_\mathrm{tot}\,R_2/(R_1+R_2)$.

</li>

<li>

Con carga: $U_2/U=(R_2\parallel R_\mathrm L)/(R_1+R_2\parallel R_\mathrm L)$, error $R_\mathrm i/(R_\mathrm i+R_\mathrm L)$.

</li>

</ul>
:::

**Mirada al [capítulo 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html).** Un nudo casi no almacena carga. El condensador de dos placas grandes hace lo contrario: almacena carga y energía.

**Un principio detrás de todos los resultados.** Dos leyes de conservación y un equilibrio sostienen el capítulo: la carga no se pierde, la energía no se pierde, y en el conductor el impulso del campo y el frenado de las colisiones se compensan.

| Resultado | De dónde viene |
|---|---|
| $I=\mathrm{d} Q/\mathrm{d} t$, $j=q\,v$ | Carga que atraviesa un área en un tiempo dado (etapa [1](strom-ist-bewegte-ladung.html#stufe-1)) |
| deriva pequeña y constante | Equilibrio entre campo y colisiones, enorme densidad de electrones (etapa [2](langsame-elektronen-sofortiger-strom.html#stufe-2)) |
| La corriente está ahí al instante | Lo que viaja es el campo, no los electrones; el hilo ya está lleno (etapa [2](langsame-elektronen-sofortiger-strom.html#stufe-2)) |
| $U=R\,I$, $R=\rho L/A$ | Deriva proporcional al campo, campo proporcional a la tensión (etapa [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3)) |
| Dependencia de la temperatura | El calor cambia el tiempo de vuelo o el número de portadores de carga (etapa [4](reale-widerstande-werte-und-temperatur.html#stufe-4)) |
| Flechas de referencia, $m=z-k+1$ | Convenio y recuento antes de calcular (etapas [5](zweipole-und-zahlpfeile.html#stufe-5) y [6](knoten-zweige-maschen.html#stufe-6)) |
| Ley de los nudos | Conservación de la carga: un nudo no almacena nada (etapa [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7)) |
| Ley de las mallas | Conservación de la energía: una vuelta termina en el potencial inicial (etapa [8](die-maschenregel-ist-energieerhaltung.html#stufe-8)) |
| Divisor de tensión, divisor de corriente | Ambas leyes aplicadas a serie y paralelo (etapas [9](reihenschaltung-und-spannungsteiler.html#stufe-9) y [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10)) |
