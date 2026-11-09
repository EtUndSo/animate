---
title: Etapa 5: Inducción matemática, suma y producto
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210700
summary: Las proposiciones sobre todos los ninmathbb N no se pueden demostrar probando.
tags: caso base, paso de inducción, hipótesis de inducción, conclusión de la inducción
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Las proposiciones sobre todos los $n\in\mathbb{N}$ no se pueden demostrar probando. Esta etapa aporta el método y, con él, una definición limpia de suma, producto y potencia.
:::

**La idea.** Todo número natural surge del 1 contando repetidamente. Si se demuestra una proposición para el 1 y se demuestra que se transmite de cada $n$ a $n+1$, la cadena alcanza todo número (fig. [5](#abb-5)).

:::satz Teorema 5.1 (Inducción matemática)
<span class="anker" id="satz-5-1"></span>

Sean $\mathcal A(n)$ proposiciones con $n\in\mathbb{N}$. Si (1) $\mathcal A(1)$ es verdadera (__caso base__) y (2) para $n$ arbitrario la implicación $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ es verdadera (__paso de inducción__, $\mathcal A(n)$ se llama __hipótesis de inducción__), entonces $\mathcal A(n)$ es verdadera para todo $n\in\mathbb{N}$ (__conclusión de la inducción__).

⁠**Segunda versión:** Sea $n_0\in\mathbb{N}$ fijo. Si $\mathcal A(n_0)$ es verdadera y para todo $n\ge n_0$ se cumple

$$\bigl(\mathcal A(n_0)\wedge\mathcal A(n_0+1)\wedge\dots\wedge\mathcal A(n)\bigr)\Rightarrow\mathcal A(n+1),$$

entonces $\mathcal A(n)$ es verdadera para todo $n\ge n_0$.
:::

⁠**Cómo leerlo:** La segunda versión permite un inicio posterior y todos los casos anteriores como hipótesis. **Por qué ambas partes:** Sin caso base: $\mathcal A(n):=(n=n+1)$ tiene un paso válido (sumar 1 en ambos lados), pero es siempre falsa. Sin paso: $n^2-n+41$ es primo para $n=1,\dots,40$, pero para $n=41$ es $41^2$.

:::frage ¿En el paso no se supone lo que se quiere demostrar?
No. Se supone $\mathcal A(n)$ para un $n$ arbitrario pero fijo y solo se demuestra la implicación $\mathcal A(n)\Rightarrow\mathcal A(n+1)$. Que $\mathcal A(n)$ sea verdadera se sigue solo del caso base y de la cadena.
:::

:::beweis Por qué vale la inducción
$\mathbb{N}$ tiene esta propiedad: si $M\subset\mathbb{N}$ con $1\in M$ y de $n\in M$ se sigue siempre $n+1\in M$, entonces $M=\mathbb{N}$. Esa es la construcción misma de $\mathbb{N}$. Se toma $M:=\{n\in\mathbb{N}:\mathcal A(n)\text{ verdadera}\}$. Para la segunda versión sea $\mathcal B(n):=\mathcal A(n_0)\wedge\dots\wedge\mathcal A(n)$. Entonces de la hipótesis se sigue $\mathcal B(n)\Rightarrow\mathcal B(n+1)$, y la misma propiedad de $\mathbb{N}$, empezando en $n_0$, da $\mathcal B(n)$ para todo $n\ge n_0$.
:::

:::definition Definición 5.2 (Suma, producto, potencia: recursivos)
<span class="anker" id="satz-5-2"></span>

Para $x_1,x_2,\ldots\in\mathbb K$ se define

<span class="anker" id="gl-5-1"></span>
$$\sum_{i=1}^{1}x_i:=x_1,\quad\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1},\qquad \prod_{i=1}^{1}x_i:=x_1,\quad\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}. \tag{5.1}$$

Si todos los $x_i=x$, entonces $x^n:=\prod_{i=1}^nx$. Para $x\ne0$ y $n\in\mathbb{N}$ se define $x^0:=1$ y $x^{-n}:=(x^n)^{-1}=(\frac1x)^n$. Además, $n!:=\prod_{i=1}^ni$ y $0^0:=1$.
:::

⁠**Cómo leerlo:** $\sum_{i=1}^nx_i=x_1+\dots+x_n$; los puntos suspensivos quedan ahora explicados por la recursión, y por el teorema [5.1](#satz-5-1) el valor está fijado para cada $n$. $x^0:=1$ es forzoso porque debe cumplirse $x^n\cdot x^0=x^{n+0}$. $0^0:=1$ es una convención: con ella, $x^0=1$ se extiende a $x=0$, y $(x+y)^2=x^2y^0+2x^1y^1+x^0y^2$ sigue siendo correcto para $x=0$ o $y=0$.

:::satz Teorema 5.3 (Reglas para suma, producto y potencia)
<span class="anker" id="satz-5-3"></span>

En todo cuerpo se cumple:

<ol class="rm">

<li>

El valor de $\sum_{i=1}^nx_i$ y $\prod_{i=1}^nx_i$ no depende del orden de los $x_i$.

</li>

<li>

Producto de sumas: $\Bigl(\sum_{i=1}^nx_i\Bigr)\Bigl(\sum_{j=1}^Ny_j\Bigr)=\sum_{i=1}^n\Bigl(\sum_{j=1}^Nx_iy_j\Bigr)$.

</li>

<li>

Leyes de potencias para $x,y\ne0$, $p,q\in\mathbb{Z}$: $x^px^q=x^{p+q}$, $(x^p)^q=x^{p\cdot q}$, $(xy)^p=x^py^p$.

</li>

</ol>
:::

⁠**Cómo leerlo:** (i) es la inducción sobre (A1), (A2), (M1), (M2). (ii) dice «cada uno con cada uno», es (AM) repetido. Para $p,q\in\mathbb{N}$, (iii) es renumerar: $x^px^q=\prod_{i=1}^{p+q}x=x^{p+q}$. **Por qué $x\ne0$:** $0^{-1}$ no existe; para $x=0$ solo se admiten exponentes $n\ge0$, y $0^n=0$ para $n\ge1$. Para $x,y>0$ las leyes valen también con exponentes racionales, por ejemplo $x^{1/2}=\sqrt x$ (Parte 5).

:::abbildung hm1/k1induktion 5
A la izquierda, cada color es una pieza en L. A la derecha, el paso de inducción: $n^2$ crece en $2n+1$ casillas.
:::

::::beispiel [Ejemplo 1] suma de los números impares
Afirmación: $\sum_{i=1}^n(2i-1)=n^2$. **Caso base:** $2\cdot1-1=1=1^2$. **Paso:** Si la fórmula vale para $n$, entonces $\sum_{i=1}^{n+1}(2i-1)=n^2+2(n+1)-1=n^2+2n+1=(n+1)^2$. **Conclusión:** Vale para todo $n$. Igualmente se demuestran $\sum_{i=1}^ni=\frac{n(n+1)}2$ y $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ (ejercicio [6](#aufg-6)).
::::

::::beispiel [Ejemplo 2] inicio posterior
$n!>2^n$ para $n\ge n_0=4$. Caso base: $24>16$. Paso: $(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n$, pues $n+1\ge2$.
::::

⁠**Caso límite:** Para $n=3$ es $6<8$; el inicio en 4 es necesario.

::::beispiel [Ejemplo 3] todos los casos anteriores
Todo $n\ge2$ es un producto de números primos. Caso base: 2 es primo. Paso: si $n+1$ no es primo, es $n+1=ab$ con $2\le a,b\le n$. Aquí no basta $\mathcal A(n)$ sola; hacen falta $\mathcal A(a)$ y $\mathcal A(b)$.
::::

:::aufgabe Ejercicio 6 ★★ Practicar la inducción
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Demuestra $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ y comprueba $n=3$.

</li>

<li>

Calcula $\prod_{i=1}^5(1+\frac1i)$. Predice la fórmula para $\prod_{i=1}^n(1+\frac1i)$ y demuéstrala.

</li>

<li>

Encuentra el error: «Todos los cables tienen el mismo color. Caso base: un cable tiene un color. Paso: de $n+1$ cables quita uno; los $n$ restantes son del mismo color. Quita otro distinto, igual. Por tanto, todos son del mismo color».

</li>

</ol>

:::loesung
(a) Caso base: $1=\frac{1\cdot4}4$. Paso: $\frac{n^2(n+1)^2}4+(n+1)^3=\frac{(n+1)^2(n^2+4n+4)}4=\frac{(n+1)^2(n+2)^2}4$. Comprobación: $1+8+27=36=\frac{9\cdot16}4$. (b) $2\cdot\frac32\cdot\frac43\cdot\frac54\cdot\frac65=6$. Conjetura: $n+1$. Caso base: $1+\frac11=2$. Paso: $(n+1)(1+\frac1{n+1})=n+2$. (c) El paso falla en $n=1$: de dos cables, al quitar uno queda cada vez otro distinto, y los restos no tienen ningún cable en común. El paso debe valer para todo $n$.
:::
:::
