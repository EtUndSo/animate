---
title: Etapa 4: Axiomas de orden
pfad: Ingeniería eléctrica / 1.er semestre / HöMa1 – Matemáticas superiores 1 / Conjuntos, lógica y números reales
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Capítulo 1: Conjuntos, lógica y números reales
order: 1210600
summary: Los axiomas de cuerpo no dicen nada sobre «mayor».
tags: totalmente ordenado, Tricotomía
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Los axiomas de cuerpo no dicen nada sobre «mayor». ¿Qué supuestos hay detrás del cálculo con desigualdades?
:::

**La idea.** Los números reales están en una recta ordenados por tamaño. Solo hay que establecer qué números son positivos. Entonces «$x$ mayor que $y$» es lo mismo que «$x-y$ es positivo». La multiplicación por un número negativo refleja la recta respecto al cero; por eso el orden se invierte (fig. [4](#abb-4)).

:::definition Definición 4.1 (Cuerpo totalmente ordenado)
<span class="anker" id="satz-4-1"></span>

Un cuerpo $\mathbb K$ con una relación «$>0$» se llama __totalmente ordenado__ si se cumple:

<ul>

<li>

⁠**(T1)** Cada $x\in\mathbb K$ cumple exactamente una de las relaciones $x>0$, $x=0$, $(-x)>0$.

</li>

<li>

⁠**(T2)** $x>0\wedge y>0\Rightarrow x+y>0$.

</li>

<li>

⁠**(T3)** $x>0\wedge y>0\Rightarrow x\cdot y>0$.

</li>

</ul>

Se define $x>y:\Leftrightarrow x-y>0$, $x<y:\Leftrightarrow y>x$ y $x\ge y:\Leftrightarrow(x=y\vee x>y)$, y análogamente $x\le y$.
:::

⁠**Cómo leerlo:** $x>0$ significa «$x$ es positivo». (T2) y (T3): la suma y el producto de números positivos son positivos. $x<0$ equivale a $(-x)>0$: $x$ es negativo.

:::satz Teorema 4.2 (Cálculo con desigualdades)
<span class="anker" id="satz-4-2"></span>

En un cuerpo totalmente ordenado se cumple para todos $x,y,z,u,v$:

|  |  |
|---|---|
| (O1) __Tricotomía__ | se cumple exactamente una de las relaciones $x<y$, $x=y$, $x>y$ |
| (O2) Transitividad | $x<y\wedge y<z\Rightarrow x<z$ |
| (O3) Monotonía de la suma | $x<y\Rightarrow x+z<y+z$ |
| (O4) Monotonía del producto | $x<y\wedge z>0\Rightarrow xz<yz$ |
| (a) Reflejar | $x<y\Leftrightarrow-y<-x$ |
| (b) Sumar | $x<y\wedge u<v\Rightarrow x+u<y+v$ |
| (c) Signos | $xy>0\Leftrightarrow\bigl((x>0\wedge y>0)\vee(x<0\wedge y<0)\bigr)$ |
| (d) Cuadrados | $x\ne0\Rightarrow x\cdot x>0$; en particular $1>0$ |
| (e) Elevar al cuadrado | para $x\ge0$, $y\ge0$: $x^2\ge y^2\Leftrightarrow x\ge y$ |
:::

⁠**Cómo leerlo:** Una desigualdad admite cualquier suma, pero solo la multiplicación por números positivos. Para $z<0$ se invierte: $x<y\wedge z<0\Rightarrow xz>yz$. Para $z=0$, (O4) se convierte en $0<0$, falso. Si en un cuerpo ordenado existiera un $i$ con $i\cdot i=-1$, por (d) sería $-1>0$ y $1>0$, y por (T2) $0>0$. Por eso los números complejos del [capítulo 2](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) no se pueden ordenar. En lugar de (T1) a (T3) se podrían tomar, de forma equivalente, (O1) a (O4) como axiomas.

:::frage ¿Puedo elevar al cuadrado una desigualdad?
Solo si ambos lados no son negativos; eso es (e). Sin esta condición: $-3<2$, pero $9>4$. Elevar al cuadrado refleja la parte negativa de la recta en la positiva, como por $-1$ en la fig. [4](#abb-4).
:::

:::abbildung hm1/k1spiegel 4
Modelo de referencia $x=-3<y=2$. Por 2 estira la recta alejándola del cero; el orden se mantiene. Por $-1$ refleja respecto al cero; el orden se invierte: $3>-2$.
:::

:::beweis Reglas de orden a partir de (T1) a (T3)
(O1): (T1) para $x-y$. (O2): $(y-x)+(z-y)=z-x$ es positivo por (T2). (O3): $(y+z)-(x+z)=y-x$. (O4): $(y-x)z>0$ por (T3), es decir, con (AM), $yz-xz>0$. (a): $(-x)-(-y)=y-x$. (b): $x+u<y+u$ y $u+y<v+y$ por (O3), y luego (O2).

(c) «$\Leftarrow$»: Para $x,y>0$ es (T3). Para $x,y<0$ es $(-x)(-y)>0$, y $(-x)(-y)=xy$. «$\Rightarrow$» indirectamente: sea $xy>0$, pero supongamos que el par $(x,y)$ no pertenece a los dos casos de la derecha. Entonces quedan cuatro casos. Con $x=0$ o $y=0$ es $xy=0$, en contra de (T1). Con $x<0<y$ se sigue de (O4) que $xy<0\cdot y=0$, en contra de $xy>0$. Con $y<0<x$, igual. (d): Para $x\ne0$ es $x>0$ o $x<0$, y por (c) es $x\cdot x>0$. Con $x=1\ne0$ se sigue $1>0$.

(e) «$\Leftarrow$»: Para $x=y$ no hay nada que demostrar. De $x>y\ge0$ se sigue $x\cdot x>y\cdot x\ge y\cdot y$ por (O4) con $z=x$ y $z=y$. «$\Rightarrow$» por contraposición: de $0\le x<y$ se sigue igualmente $x\cdot x\le x\cdot y<y\cdot y$.
:::

::::beispiel
Para $x\ne0$, $x$ es positivo si y solo si $x^{-1}$ es positivo, pues $x\cdot x^{-1}=1>0$ y (c). Por tanto: resuelve $\frac1x>2$. Para $x>0$ se puede multiplicar por $x$: $1>2x$, luego $0<x<\frac12$. Para $x<0$ el lado izquierdo es negativo y no hay solución.
::::

⁠**Caso límite:** Con $x=\frac12$ queda $2>2$, falso; el extremo no pertenece a la solución.

:::aufgabe Ejercicio 5 ★★ Desigualdades
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Demuestra $x<y\wedge z<0\Rightarrow xz>yz$ a partir de (O4) y (a).

</li>

<li>

¿Para qué $x\ne1$ reales se cumple $\frac3{x-1}>1$? Distingue dos casos.

</li>

</ol>

:::loesung
(a) De $z<0$ se sigue $-z>0$, por (O4) $-xz<-yz$, por (a) $yz<xz$. (b) Caso $x>1$: multiplicar por $x-1>0$ da $3>x-1$, luego $1<x<4$. Caso $x<1$: el lado izquierdo es negativo, sin solución. Resultado: $1<x<4$.
:::
:::
