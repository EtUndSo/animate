---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / HöMa1 – Matemáticas superiores 1 / Números complejos
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Capítulo 2: Números complejos
order: 1220800
summary: Cómo un segundo eje hace resoluble $x^2=-1$ y qué se pierde por el camino
tags: número complejo, unidad imaginaria, plano complejo, cuerpo, conjugado complejo, valor absoluto, desigualdad triangular
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Un __número complejo__ es un par de números reales, escrito $z=x+\mathrm{i}y$. La __unidad imaginaria__ $\mathrm{i}$ es el par $(0,1)$ y cumple $\mathrm{i}^2=-1$. Todos los pares juntos forman el __plano complejo__, en el que $\mathbb{R}$ es el eje horizontal.

</li>

<li>

Se calcula como en $\mathbb{R}$ y se sustituye $\mathrm{i}^2$ por $-1$. Por eso $\mathbb{C}$ es un __cuerpo__ (un conjunto en el que las cuatro operaciones básicas cumplen las leyes habituales). Lo que se pierde es el orden: entre números complejos no existe «mayor que».

</li>

<li>

El __conjugado complejo__ $\overline{z}=x-\mathrm{i}y$ es la imagen especular de $z$ respecto del eje real, y $z\overline{z}=x^2+y^2$ es real. De ahí se deducen la división, el __valor absoluto__ $|z|=\sqrt{x^2+y^2}$ (distancia al origen) y la __desigualdad triangular__ $|z+w|\le|z|+|w|$ (un rodeo nunca es más corto).

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Un número complejo es un par: $z=x+\mathrm{i}y$ con $\mathrm{i}^2=-1$. Se calcula como en $\mathbb{R}$.

</li>

<li>

La suma es el paralelogramo; multiplicar por $\mathrm{i}$ gira $90^\circ$.

</li>

<li>

Conjugar refleja: $\overline{z}=x-\mathrm{i}y$, y $z\overline{z}=x^2+y^2=|z|^2$.

</li>

<li>

División: multiplicar arriba y abajo por el conjugado del denominador, $w/z=w\overline{z}/|z|^2$.

</li>

<li>

$\mathbb{C}$ es un cuerpo, pero no ordenado. Las desigualdades solo se dan entre magnitudes reales.

</li>

<li>

$|z|=\sqrt{x^2+y^2}$, $d(z,w)=|z-w|$, $|zw|=|z||w|$, $|z+w|\le|z|+|w|$.

</li>

<li>

$z^2+pz+q=0$ siempre tiene soluciones en $\mathbb{C}$: $z=-p/2\pm w$ con $w^2=p^2/4-q$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** Todo en este capítulo se deduce de una regla: calcula con $\mathrm{i}$ como con una letra y sustituye $\mathrm{i}^2$ por $-1$.

| Resultado | De dónde viene |
|---|---|
| Fórmula del producto | Desarrollar el producto, el signo menos es $\mathrm{i}^2$ (etapa [1](paare-statt-einzelner-zahlen.html#stufe-1)) |
| La suma como paralelogramo | Parte real y parte imaginaria se suman por separado (etapa [2](die-komplexe-ebene.html#stufe-2)) |
| Multiplicar por $\mathrm{i}$ gira $90^\circ$ | $\mathrm{i}(x+\mathrm{i}y)=-y+\mathrm{i}x$, girar dos veces es $-1$ (etapa [2](die-komplexe-ebene.html#stufe-2)) |
| $z\overline{z}=x^2+y^2$ | Suma por diferencia con $-\mathrm{i}^2=+1$ (etapa [3](spiegeln-an-der-reellen-achse.html#stufe-3)) |
| División | Multiplicar arriba y abajo por $\overline{z}$ hace real el denominador (etapa [4](dividieren-und-was-verloren-geht.html#stufe-4)) |
| Sin orden | $\mathrm{i}^2=-1$ es un cuadrado negativo (etapa [4](dividieren-und-was-verloren-geht.html#stufe-4)) |
| $\vert zw\vert =\vert z\vert \,\vert w\vert $, desigualdad triangular | $\vert z\vert ^2=z\overline{z}$ (etapa [5](betrag-und-abstand.html#stufe-5)) |
| Ecuaciones cuadráticas | Completar el cuadrado vale en todo cuerpo, todo número tiene raíz (etapa [6](quadratische-gleichungen.html#stufe-6)) |
