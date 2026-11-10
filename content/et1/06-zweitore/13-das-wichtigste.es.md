---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Cuadripolos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Capítulo 6: Cuadripolos
order: 1161300
summary: Por qué cuatro números sustituyen a toda una red y cada forma de parámetros es solo otra elección
tags: condición de puerto, parámetros del cuadripolo, forma de impedancia, forma de admitancia, forma híbrida, forma en cadena
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

En cada puerto, la corriente que entra por un terminal vuelve a salir por el otro (__condición de puerto__). Por eso, desde fuera quedan dos tensiones y dos corrientes.

</li>

<li>

En un cuadripolo lineal sin fuentes propias, dos de estas cuatro magnitudes determinan las otras dos. Cada magnitud dependiente es una suma de dos partes; por eso bastan cuatro números, los __parámetros del cuadripolo__.

</li>

<li>

La __forma de impedancia__ (corrientes dadas), la __forma de admitancia__ (tensiones dadas), la __forma híbrida__ (corriente de entrada y tensión de salida dadas) y la __forma en cadena__ (magnitudes de salida dadas) describen el mismo cuadripolo. El circuito abierto y el cortocircuito anulan una magnitud dada y así dejan al descubierto los parámetros uno a uno.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Cuadripolo: cuatro terminales, condición de puerto $I_{1'}=-I_1$, $I_{2'}=-I_2$. Magnitudes de puerto $U_1$, $I_1$, $U_2$, $I_2$; las flechas de corriente apuntan hacia dentro.

</li>

<li>

Lineal, sin fuentes propias: dos magnitudes fijan las otras, cuatro parámetros.

</li>

<li>

Z: $\mathbf U=\mathbf Z\,\mathbf I$, ensayos de circuito abierto. Y: $\mathbf I=\mathbf Y\,\mathbf U$, ensayos de cortocircuito. $\mathbf Y=\mathbf Z^{-1}$.

</li>

<li>

H: $(U_1,I_2)$ a partir de $(I_1,U_2)$. A: $(U_1,I_1)$ a partir de $(U_2,-I_2)$.

</li>

<li>

Un parámetro es un cociente de efecto y causa, con la otra causa anulada. $I=0$ significa circuito abierto; $U=0$, cortocircuito.

</li>

<li>

La corriente propia da una resistencia; la corriente o tensión ajena, una fuente controlada. Las tensiones se suman en serie; las corrientes, en paralelo.

</li>

<li>

Carga: $Z_1=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$, $Y_1=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}$.

</li>

<li>

T: $\mathbf Z$ con $R_\mathrm{a}+R_\mathrm{b}$, $R_\mathrm{b}$, $R_\mathrm{b}+R_\mathrm{c}$. $\pi$: $\mathbf Y$ con $G_1+G_2$, $-G_2$, $G_2+G_3$. Conversión estrella-triángulo.

</li>

<li>

Serie, serie: Z se suma. Paralelo, paralelo: Y se suma. Serie, paralelo: H se suma. Cadena: A se multiplica. Condición: se mantiene la condición de puerto.

</li>

<li>

Recíproco: $Z_{12}=Z_{21}$, $Y_{12}=Y_{21}$, $H_{12}=-H_{21}$, $\det\mathbf A=1$. Unilateral: $Z_{12}=Y_{12}=H_{12}=0$, $\det\mathbf A=0$.

</li>

<li>

Potencia: $P=U_1I_1+U_2I_2$; activo si es posible $P<0$.

</li>

</ul>
:::

**Mirada al [capítulo 7](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html).** La potencia $P$ de la etapa [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10) lleva a la siguiente pregunta: ¿con qué carga entrega una fuente o un cuadripolo la mayor potencia, y cuánto cuesta eso en rendimiento?

**Un principio detrás de todos los resultados.** De las cuatro magnitudes de puerto se eligen dos como causas; las otras dos son los efectos. Esta elección no cambia nada en el cuadripolo, solo en el cálculo, y de ella se sigue cada resultado.

| Resultado | De dónde viene |
|---|---|
| Cuatro magnitudes de puerto en lugar de seis | Un dipolo en cada par de terminales recoge por un terminal la carga que entrega por el otro (etapa [1](vom-vierpol-zum-zweitor.html#stufe-1)) |
| Cuatro parámetros | Superposición: dos causas por dos efectos (etapa [2](vier-groen-zwei-gleichungen-vier-zahlen.html#stufe-2)) |
| Parámetros Z a partir de ensayos de circuito abierto | Las causas son corrientes, y un puerto abierto anula una corriente (etapa [3](impedanzform-und-leerlaufversuch.html#stufe-3)) |
| La resistencia de entrada depende de la carga | La segunda causa $I_2$ actúa de vuelta sobre la entrada a través de $Z_{12}$ (etapa [4](das-zweitor-im-betrieb.html#stufe-4)) |
| Parámetros Y a partir de ensayos de cortocircuito | Las causas son tensiones, y un hilo anula una tensión (etapa [5](admittanzform-und-kurzschlussversuch.html#stufe-5)) |
| $\mathbf Y=\mathbf Z^{-1}$, T y $\pi$ | Las mismas dos ecuaciones, despejadas para las otras dos magnitudes (etapa [6](umrechnen-t-und.html#stufe-6)) |
| Forma híbrida | Causas mezcladas, adecuadas para componentes con entrada de corriente y salida de fuente de corriente (etapa [7](hybridform.html#stufe-7)) |
| Forma en cadena, producto de matrices | Las causas de una etapa son los efectos de la siguiente (etapa [8](kettenform.html#stufe-8)) |
| Z, Y, H se suman | Lo que comparten ambas partes pertenece a las causas; lo que se suma, a los efectos (etapa [9](zusammenschaltung.html#stufe-9)) |
| Recíproco, unilateral, activo | Relaciones entre los cuatro números y sus signos (etapa [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)) |
