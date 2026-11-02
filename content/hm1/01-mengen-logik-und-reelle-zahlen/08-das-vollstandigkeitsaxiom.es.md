---
title: Etapa 6: El axioma de completitud
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210800
summary: mathbb Q cumple todos los axiomas vistos hasta ahora.
tags: acotado superiormente, cota superior, acotado inferiormente, cota inferior, acotado, supremo, ínfimo, máximo
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\mathbb{Q}$ cumple todos los axiomas vistos hasta ahora. Aun así falta algo: el número cuyo cuadrado es 2. Esta etapa lo muestra y nombra el axioma que separa $\mathbb{R}$ de $\mathbb{Q}$.
:::

**La idea.** $\mathbb{N}$ y $\mathbb{Z}$ tienen huecos visibles. $\mathbb{Q}$ parece no tenerlos: entre dos fracciones $p/q<u/v$ hay siempre otra, $\frac12(p/q+u/v)=p/q+\frac12(u/v-p/q)$. Aun así, hay puntos a los que ninguna fracción llega (fig. [6](#abb-6)). Completitud significa: cada una de esas fronteras es un número.

:::satz Teorema 6.1 (La raíz cuadrada de 2 no es una fracción)
<span class="anker" id="satz-6-1"></span>

No existe ningún $r\in\mathbb{Q}$ con $r^2=2$.
:::

:::beweis Indirecta
Suposición: $r=\frac pq$ con $p,q\in\mathbb{N}$ (el signo no importa), simplificada hasta que $p$ y $q$ no sean ambos pares. De $r^2=2$ se sigue $p^2=2q^2$, luego $p^2$ es par. Por la contraposición de la etapa [1](mengen-und-aussagen.html#stufe-1), $p$ es par, $p=2k$. Sustituyendo: $4k^2=2q^2$, luego $q^2=2k^2$, e igualmente $q$ es par. Entonces $p$ y $q$ son ambos pares, en contradicción con la simplificación.
:::

⁠**Cómo leerlo:** Por tanto, $r^2=2$ no tiene solución en $\mathbb{Q}$. Para $r^2=4$ la demostración falla, como debe ser (ejercicio [8](intervallschachtelung-und-wurzeln.html#aufg-8)).

:::abbildung hm1/k1luecke 6
Las fracciones de $D$ y las fracciones con $x^2>2$ están tan cerca unas de otras como se quiera, por ejemplo 1,414 y 1,415. El punto entre ellas no es una fracción.
:::

:::definition Definición 6.2 (Cota, supremo, ínfimo)
<span class="anker" id="satz-6-2"></span>

Sea $\mathbb K$ totalmente ordenado y $M\subset\mathbb K$.

<ol class="rm">

<li>

$M$ se llama __acotado superiormente__ si existe $S\in\mathbb K$ con $x\le S$ para todo $x\in M$. Cada uno de esos $S$ se llama __cota superior__. Análogamente, __acotado inferiormente__ y __cota inferior__ con $R\le x$. Ambas cosas juntas se llaman __acotado__.

</li>

<li>

$S$ se llama __supremo__ de $M$, $S=\sup M$, si $S$ es una cota superior y para toda cota superior $\tilde S$ se cumple $S\le\tilde S$ (la menor cota superior).

</li>

<li>

$R$ se llama __ínfimo__ de $M$, $R=\inf M$, si $R$ es una cota inferior y para toda cota inferior $\tilde R$ se cumple $\tilde R\le R$ (la mayor cota inferior).

</li>

<li>

Si $S$ está en $M$, se llama __máximo__ ($\max M$); si $R$ está en $M$, se llama __mínimo__ ($\min M$).

</li>

</ol>
:::

⁠**Cómo leerlo:** Las cotas están por fuera y no son únicas: $\{2,3,5,7\}$ tiene la cota superior 7, pero también 100. Aquí es $\sup=\max=7$, $\inf=\min=2$. $\mathbb{N}$ tiene la cota inferior 1 y ninguna superior (teorema [6.5](#satz-6-5)).

:::frage ¿El supremo no es el elemento más grande?
Solo si está en el conjunto. $M=\{2-\frac1n:n\in\mathbb{N}\}=\{1,\frac32,\frac53,\dots\}$ tiene $\min M=1$ y $\sup M=2$, pero ningún máximo, pues $2\notin M$. En el modelo de referencia, $D$ está acotado superiormente, por ejemplo por $1{,}5$. Aun así, en $\mathbb{Q}$ el conjunto $D$ no tiene supremo: para cada cota superior hay otra menor.
:::

:::definition Definición 6.3 (Axioma de completitud (V))
<span class="anker" id="satz-6-3"></span>

Un cuerpo totalmente ordenado $\mathbb K$ se llama __completo__ si todo conjunto no vacío $M\subset\mathbb K$ acotado inferiormente posee una mayor cota inferior $\inf M\in\mathbb K$.
:::

⁠**Cómo leerlo:** Lo decisivo es «$\in\mathbb K$». $\mathbb{Q}$ no es completo: $\{x\in\mathbb{Q}:x>0,\ x^2>2\}$ está acotado inferiormente y no es vacío, pero no tiene en $\mathbb{Q}$ una mayor cota inferior. La candidata sería $\sqrt2\notin\mathbb{Q}$. **Por qué «no vacío» y «acotado»:** Para $M=\emptyset$, todo número es cota inferior y no hay una mayor. $M=\mathbb{Z}$ no tiene cota inferior.

:::satz Teorema 6.4 (Teorema principal)
<span class="anker" id="satz-6-4"></span>

Existe esencialmente un solo cuerpo totalmente ordenado y completo que contiene a $\mathbb{Q}$. Es el __cuerpo de los números reales__ $\mathbb{R}$, y su orden coincide en $\mathbb{Q}$ con el habitual.
:::

⁠**Cómo leerlo:** La demostración nos llevaría demasiado lejos; aquí basta el significado: los tres grupos de axiomas fijan $\mathbb{R}$ de forma única salvo cambio de nombres, y por eso se puede hablar de *los* números reales. Esto sustituye a la definición provisional. El cuerpo $\{0,1\}$ cumple solo los axiomas de cuerpo, $\mathbb{Q}$ también el orden, y solo $\mathbb{R}$ los tres grupos. Equivalente a (V) es la exigencia de que toda sucesión de Cauchy converja (Parte 4).

:::satz Teorema 6.5 (Consecuencias de la completitud)
<span class="anker" id="satz-6-5"></span>

En $\mathbb{R}$ se cumple:

<ol class="rm">

<li>

Todo conjunto no vacío $M$ acotado superiormente tiene un supremo, y se cumple $\sup M=-\inf(-M)$ con $-M:=\{-x:x\in M\}$.

</li>

<li>

El supremo y el ínfimo de un conjunto son únicos.

</li>

<li>

Si $S=\sup M$, para cada $y<S$ existe un $x\in M$ con $y<x\le S$. Para el ínfimo vale lo análogo.

</li>

<li>

$\mathbb{N}$ no está acotado superiormente.

</li>

<li>

__Teorema de Arquímedes:__ Para todos $x,y>0$ existe un $n\in\mathbb{N}$ con $nx>y$.

</li>

<li>

Para cada $x>0$ existe un $n\in\mathbb{N}$ con $0<\frac1n<x$ (Eudoxo).

</li>

</ol>
:::

⁠**Cómo leerlo:** (iii): justo por debajo del supremo siempre hay un elemento del conjunto. (v): con suficientes pasos pequeños $x$ se supera cualquier altura $y$. Para $x=0{,}001$ e $y=1000$ basta $n=1\,000\,001$. Para $x=0$ no vale (v), pues $nx=0$. (vi): Para $x=0{,}003$ basta $n=334$. También se puede exigir (v) como axioma. Eso es menos que (V), pues $\mathbb{Q}$ lo cumple.

:::beweis Consecuencias
(i) Con $M$, también $-M$ es no vacío, y si $S$ es cota superior de $M$, $-S$ es cota inferior de $-M$ por el teorema [4.2](anordnungsaxiome.html#satz-4-2) (a). (V) da $R=\inf(-M)$. Como el reflejo convierte cotas superiores en inferiores e invierte el orden, $-R$ es la menor cota superior de $M$.

(ii) Si $S_1$, $S_2$ son supremos, ambos son cotas superiores. Luego $S_1\le S_2$, porque $S_1$ es la menor, e igualmente $S_2\le S_1$. Por (O1) es $S_1=S_2$.

(iii) Indirectamente: si existiera $y<S$ sin tal $x$, sería $x\le y$ para todo $x\in M$ (negación, [(2.1)](quantoren-und-indirekter-beweis.html#gl-2-1)). Entonces $y$ sería una cota superior menor que $S$, en contra de la definición de $\sup M$. Que $x\le S$ se debe a que $S$ es cota superior.

(iv) Indirectamente: si no, existiría $S=\sup\mathbb{N}$ por (i). Por (iii) existe $n\in\mathbb{N}$ con $S-1<n$. Entonces $n+1>S$ y $n+1\in\mathbb{N}$, en contra de «cota superior».

(v) Indirectamente: sea $nx\le y$ para todo $n$. Como $x^{-1}>0$, de (O4) se sigue $n\le yx^{-1}$ para todo $n$, en contra de (iv). (vi): $y:=1$ en (v) da $nx>1$, luego $x>\frac1n>0$.
:::

:::aufgabe Ejercicio 7 ★★ Determinar cotas
<span class="anker" id="aufg-7"></span>

Determina el supremo, el ínfimo, el máximo y el mínimo en $\mathbb{R}$, si existen, y justifícalo: (a) $M_1=\{x\in\mathbb{Q}:x^2\le4\}$, (b) $M_2=\{\frac{(-1)^n}n:n\in\mathbb{N}\}$, (c) $M_3=\{x\in\mathbb{Q}:x^2<3\}$. ¿Cuáles de estas magnitudes faltan en (c) si se busca solo en $\mathbb{Q}$?

:::loesung
(a) $M_1=\{x\in\mathbb{Q}:-2\le x\le2\}$: $\sup=\max=2$, $\inf=\min=-2$. (b) $M_2=\{-1,\frac12,-\frac13,\frac14,\dots\}$: $\sup=\max=\frac12$, $\inf=\min=-1$. (c) $\sup M_3=\sqrt3$, $\inf M_3=-\sqrt3$, sin máximo ni mínimo, porque $\sqrt3\notin\mathbb{Q}$ (ejercicio [8](intervallschachtelung-und-wurzeln.html#aufg-8)). En $\mathbb{Q}$ faltan también el supremo y el ínfimo: para cada cota superior racional hay otra menor.
:::
:::
