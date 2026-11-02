---
title: Etapa 8: Distancia y valor absoluto
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1211000
summary: Los límites miden lo cerca que están dos números.
tags: distancia, valor absoluto, desigualdad triangular, desigualdad triangular inversa
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Los límites miden lo cerca que están dos números. Para ello hacen falta la distancia y una regla para los rodeos.
:::

**La idea.** La distancia entre dos números es la longitud del segmento que los une en la recta. La longitud no depende de la dirección, y un rodeo por un tercer punto nunca es más corto (fig. [8](#abb-8)). El valor absoluto es la distancia al cero.

:::definition Definición 8.1 (Distancia y valor absoluto)
<span class="anker" id="satz-8-1"></span>

Para $x,y\in\mathbb{R}$,

<span class="anker" id="gl-8-1"></span>
$$d(x,y):=\begin{cases}x-y,&x\ge y\\y-x,&x<y\end{cases}\qquad\text{y}\qquad|x|:=d(x,0)=\begin{cases}x,&x\ge0\\-x,&x<0\end{cases} \tag{8.1}$$

se llaman __distancia__ entre $x$ e $y$ y __valor absoluto__ de $x$.
:::

⁠**Cómo leerlo:** $d$ de distancia. De la definición se sigue

<span class="anker" id="gl-8-2"></span>
$$d(x,y)=d(x-y,0)=|x-y|,\ \ -|x|\le x\le|x|,\ \ |x|=\max\{x,-x\},\ \ -|x|=\min\{x,-x\}. \tag{8.2}$$

En el modelo de referencia es $|x|=3$, $|y|=5$ y $d(x,y)=|{-3}-5|=8$. El signo menos en [(8.1)](#gl-8-1) engaña: para $x<0$, $-x$ es positivo; el valor absoluto nunca es negativo. Los valores con tolerancia se escriben así: $|U-5\,\mathrm V|\le0{,}1\,\mathrm V$ significa que $U$ está entre 4,9 V y 5,1 V.

:::satz Teorema 8.2 (Propiedades de la distancia y del valor absoluto)
<span class="anker" id="satz-8-2"></span>

Para todos $x,y,z\in\mathbb{R}$ se cumple:

|  | Distancia | Valor absoluto |
|---|---|---|
| positivo | $d(x,y)\ge0$ | $\vert x\vert \ge0$ |
| definido | $d(x,y)=0\Leftrightarrow x=y$ | $\vert x\vert =0\Leftrightarrow x=0$ |
| simétrico, producto | $d(x,y)=d(y,x)$ | $\vert xy\vert =\vert x\vert \vert y\vert $; para $z\ne0$: $\vert x/z\vert =\vert x\vert /\vert z\vert $ |
| __desigualdad triangular__ | $d(x,y)\le d(x,z)+d(z,y)$ | $\vert x+y\vert \le\vert x\vert +\vert y\vert $ |

Además se cumplen $|x-y|\le|x|+|y|$, la __desigualdad triangular inversa__ $\bigl||x|-|y|\bigr|\le|x\pm y|$ y $|x|=\sqrt{x^2}$.
:::

⁠**Cómo leerlo:** La desigualdad triangular acota una suma por arriba; la inversa, por abajo.

:::frage ¿Por qué no se cumple $|x+y|=|x|+|y|$?
Solo se cumple con signos iguales o si un sumando es cero. Con signos distintos, los sumandos se anulan en parte: $|-3+5|=2<8$. En el peor de los casos se suman dos errores; eso dice la desigualdad.
:::

:::abbildung hm1/k1betrag 8
Modelo de referencia $x=-3$, $y=5$. Directamente es $d(x,y)=8$. El rodeo por $z=7$ da $10+2=12$. Para cada $z$ entre $x$ e $y$, por ejemplo $z=1$, da exactamente 8 ($4+4$).
:::

:::beweis Desigualdad triangular y consecuencias
El carácter definido y la simetría están en [(8.1)](#gl-8-1). *Desigualdad triangular para $d$.* Sin pérdida de generalidad (abreviado s. p. d. g.: los demás casos se reducen a este cambiando los nombres) sea $x<y$; para $x=y$ a la izquierda queda 0. Para $z=x$ o $z=y$ un sumando es 0 y la desigualdad es una igualdad. Quedan tres casos. $x<y<z$: $d(x,z)+d(z,y)=2z-x-y>2y-x-y=y-x$. $x<z<y$: La suma es exactamente $y-x$. $z<x<y$: La suma es $x+y-2z>x+y-2x=y-x$.

⁠*Producto.* Si $xy=0$, por el teorema [3.2](korperaxiome.html#satz-3-2) (v) ambos lados son 0. Para $xy>0$, por el teorema [4.2](anordnungsaxiome.html#satz-4-2) (c) $x$, $y$ tienen el mismo signo, y $|x||y|$ es $xy$ o $(-x)(-y)$, ambos $xy$. $xy<0$ se trata igual. Para el cociente: $z\cdot\frac xz=x$ da $|z|\,|\frac xz|=|x|$.

⁠*Valor absoluto.* $|x+y|=|x-(-y)|=d(x,-y)\le d(x,0)+d(0,-y)=|x|+|y|$, pues $|-y|=|y|$. Con $-y$ en lugar de $y$ se sigue $|x-y|\le|x|+|y|$.

⁠*Desigualdad triangular inversa.* $|x|=|(x-y)+y|\le|x-y|+|y|$, luego $|x|-|y|\le|x-y|$. Intercambiando $x$ e $y$, también $|y|-|x|\le|x-y|$. Por [(8.2)](#gl-8-2), el máximo de ambos es $\bigl||x|-|y|\bigr|$. Con $-y$ en lugar de $y$ se sigue la variante con $+$.

⁠*Raíz.* $|x|\ge0$ y $|x|^2=x^2$, luego $|x|$ es la única solución no negativa de $z^2=x^2$.
:::

**Ejemplo.** Con $x=-3$, $y=5$: $|x+y|=2\le8=|x|+|y|$ y $\bigl||x|-|y|\bigr|=2\le|x+y|=2$. **Caso límite** $y=0$: Todas las desigualdades se convierten en $|x|=|x|$.

:::aufgabe Ejercicio 9 ★★ Desigualdades con valor absoluto
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Describe $\{x\in\mathbb{R}:|x-2|\le3\}$ como intervalo.

</li>

<li>

Resuelve $|x-2|+|x+1|\le5$ distinguiendo casos en los puntos $x=-1$ y $x=2$.

</li>

<li>

Dos tensiones cumplen $|U_1-5\,\mathrm V|\le0{,}1\,\mathrm V$, $|U_2-3\,\mathrm V|\le0{,}2\,\mathrm V$. ¿Cuánto puede desviarse como máximo $U_1+U_2$ de 8 V? Indica un par que alcance ese valor.

</li>

</ol>

:::loesung
(a) $-3\le x-2\le3$, luego $[-1,5]$. (b) Para $x\ge2$: $2x-1\le5$, luego $2\le x\le3$. Para $-1\le x<2$: $(2-x)+(x+1)=3\le5$, siempre verdadero. Para $x<-1$: $1-2x\le5$, luego $-2\le x<-1$. En conjunto: $[-2,3]$. (c) $|(U_1+U_2)-8\,\mathrm V|\le|U_1-5\,\mathrm V|+|U_2-3\,\mathrm V|\le0{,}3\,\mathrm V$. Se alcanza con $U_1=5{,}1\,\mathrm V$, $U_2=3{,}2\,\mathrm V$.
:::
:::
