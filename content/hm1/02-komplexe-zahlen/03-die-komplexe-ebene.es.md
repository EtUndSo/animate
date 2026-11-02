---
title: Etapa 2: El plano complejo
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Números complejos
order: 1220300
summary: Un par es un punto.
tags: eje real, eje imaginario, imaginarios puros, plano de Gauss
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Un par es un punto. Esta etapa dibuja los números complejos en el plano y muestra qué significan allí la suma y la multiplicación por $\mathrm{i}$.
:::

**La idea.** Se lleva $x$ hacia la derecha e $y$ hacia arriba. El __eje real__ horizontal es $\mathbb{R}$; en el __eje imaginario__ vertical están los números __imaginarios puros__ $\mathrm{i}y$. Cada número complejo es un punto o, de forma equivalente, una flecha (vector) desde el origen hasta ese punto. La suma se hace por separado en cada coordenada: la flecha de $z_2$ se coloca en la punta de $z_1$. Los dos órdenes juntos forman un paralelogramo, y la suma es su cuarto vértice (fig. [2](#abb-2), izquierda). En el cálculo de corriente alterna estas flechas se llaman fasores, y las tensiones se suman exactamente así.

:::abbildung hm1/k2ebene 2
A la izquierda, $z_1$, $z_2$ y el paralelogramo, en naranja el eje real: $z_1+z_2=4+3\mathrm{i}$ está 3 más 1 a la derecha y 1 más 2 hacia arriba. A la derecha, cada multiplicación por $\mathrm{i}$ gira $90^\circ$. De $z_1$ salen los vértices de un cuadrado; de $1$, los puntos grises $\mathrm{i}$, $-1$, $-\mathrm{i}$.
:::

:::definition Definición 2.1 (Parte real, parte imaginaria, plano de Gauss)
<span class="anker" id="satz-2-1"></span>

Para $z=x+\mathrm{i}y$ con $x,y\in\mathbb{R}$, $x=:\operatorname{Re}(z)$ se llama parte real e $y=:\operatorname{Im}(z)$ parte imaginaria de $z$. El plano complejo con las coordenadas $\operatorname{Re}(z)$ e $\operatorname{Im}(z)$ se llama también __plano de Gauss__. Se cumple $z=w$ si y solo si $\operatorname{Re}(z)=\operatorname{Re}(w)$ e $\operatorname{Im}(z)=\operatorname{Im}(w)$.
:::

⁠**Cómo leerlo:** Las dos partes son reales: la parte imaginaria de $3+\mathrm{i}$ es 1, no $\mathrm{i}$. Por tanto, una ecuación en $\mathbb{C}$ equivale a dos ecuaciones reales. La diferencia $z-w$ es la flecha de $w$ a $z$, porque $w+(z-w)=z$. En el modelo de referencia es $z_1-z_2=2-\mathrm{i}$.

:::satz Teorema 2.2 (Multiplicación por $\mathrm{i}$)
<span class="anker" id="satz-2-2"></span>

Para $z=x+\mathrm{i}y$ es $\mathrm{i}z=-y+\mathrm{i}x$. Con ello, la flecha de $z$ gira $90^\circ$ en sentido antihorario alrededor del origen.
:::

⁠**Cómo leerlo:** El punto $(x,y)$ se convierte en $(-y,x)$. Dos giros dan media vuelta, es decir, el cambio de signo: ese es el mecanismo detrás de $\mathrm{i}^2=-1$. Un cuarto de vuelta abandona la recta numérica. Por eso $\mathrm{i}$ no podía estar en ella.

:::beweis Cuarto de vuelta
Es $\mathrm{i}(x+\mathrm{i}y)=\mathrm{i}x+\mathrm{i}^2y=-y+\mathrm{i}x$. La flecha de $z$ es la hipotenusa de un triángulo rectángulo con el cateto horizontal $x$ y el cateto vertical $y$, ambos con signo. El cuarto de vuelta convierte $x$ hacia la derecha en $x$ hacia arriba, e $y$ hacia arriba en $y$ hacia la izquierda. Por tanto la flecha girada termina en $(-y,x)$.
:::

**Ejemplo.** $\mathrm{i}z_1=-1+3\mathrm{i}$, $\mathrm{i}^2z_1=-3-\mathrm{i}=-z_1$, $\mathrm{i}^3z_1=1-3\mathrm{i}$, $\mathrm{i}^4z_1=z_1$ (fig. [2](#abb-2), derecha). **Caso límite:** Un factor real $r$ no gira, estira: $r(x+\mathrm{i}y)=rx+\mathrm{i}ry$. Para $r=-1$ invierte la flecha, como multiplicar dos veces por $\mathrm{i}$.

:::frage ¿No es el plano complejo simplemente el plano de coordenadas de siempre?
Como conjunto y al sumar, sí. La diferencia es la multiplicación: [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) convierte dos puntos de nuevo en un punto, y gracias a ella se puede dividir (etapa [4](dividieren-und-was-verloren-geht.html#stufe-4)). Solo eso hace del plano un sistema de números.
:::

:::aufgabe Ejercicio 2 ★★ Geometría con números
<span class="anker" id="aufg-2"></span>

Se dan $P=1+\mathrm{i}$, $Q=4+2\mathrm{i}$, $R=2+4\mathrm{i}$. (a) Calcula el cuarto vértice $S$ del paralelogramo de lados $PQ$ y $PR$. Demuestra que las dos diagonales tienen el mismo punto medio. (b) Gira $Q$ alrededor del punto $P$ un ángulo de $90^\circ$ en sentido antihorario. Pista: la flecha de $P$ a $Q$ es $Q-P$. (c) Caso límite: ¿qué da tu fórmula de (b) para $Q=P$?

:::loesung
(a) Desde $P$ salen las flechas $Q-P=3+\mathrm{i}$ y $R-P=1+3\mathrm{i}$. El cuarto vértice es $S=P+(Q-P)+(R-P)=Q+R-P=5+5\mathrm{i}$. Los puntos medios de las diagonales son $(P+S)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$ y $(Q+R)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$.

(b) Se gira la flecha $Q-P$ y se vuelve a colocar en $P$: $P+\mathrm{i}(Q-P)=1+\mathrm{i}+\mathrm{i}(3+\mathrm{i})=1+\mathrm{i}-1+3\mathrm{i}=4\mathrm{i}$. (c) $P+\mathrm{i}\cdot0=P$: el centro de giro se queda donde está.
:::
:::
