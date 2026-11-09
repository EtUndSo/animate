---
title: Etapa 7: Intervalos encajados y raíces
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210900
summary: El axioma garantiza fronteras.
tags: intervalo, números no negativos, raíz cuadrada
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
El axioma garantiza fronteras. Esta etapa lo convierte en un procedimiento de construcción y demuestra con él que $x^2=2$ tiene en $\mathbb{R}$ exactamente una solución positiva.
:::

**La idea.** Se atrapa el número buscado entre dos fracciones y se divide el intervalo por la mitad una y otra vez hasta que sea tan pequeño como se quiera (fig. [7](#abb-7)). Cada intervalo está dentro del anterior. La completitud garantiza que existe un punto que está en todos. En $\mathbb{Q}$ este punto puede faltar. Un __intervalo__ es $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$; los __números no negativos__ son $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$.

:::satz Teorema 7.1 (Intervalos encajados)
<span class="anker" id="satz-7-1"></span>

Para números $a_n,b_n\in\mathbb{R}$, $n\in\mathbb{N}$, se cumplan $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ y

<span class="anker" id="gl-7-1"></span>
$$\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon. \tag{7.1}$$

Entonces existe exactamente un $x\in\mathbb{R}$ con $a_n\le x\le b_n$ para todo $n\in\mathbb{N}$.
:::

⁠**Cómo leerlo:** $\varepsilon$ (griego épsilon) es un número positivo tan pequeño como se quiera. [(7.1)](#gl-7-1) significa: los intervalos $[a_n,b_n]$ se hacen más pequeños que cualquier longitud dada. **Por qué las hipótesis:** Sin [(7.1)](#gl-7-1), $x$ no es único: para $a_n=-\frac1n$, $b_n=1+\frac1n$, todo $[0,1]$ está en todos los intervalos. En $\mathbb{Q}$ el teorema no vale: las fracciones $a_n,b_n$ de la fig. [7](#abb-7) cumplen todas las condiciones, pero ninguna fracción está en todos los intervalos.

:::beweis Intervalos encajados
⁠*Existencia.* Para $n,k$ arbitrarios, sea $m$ el mayor de los dos números. Entonces $a_n\le a_m\le b_m\le b_k$. Luego cada $b_k$ es cota superior de $A:=\{a_n:n\in\mathbb{N}\}$. Por el teorema [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (i) existe $x:=\sup A$. Se cumple $a_n\le x$ porque $x$ es cota superior, y $x\le b_k$ porque $x$ es la menor.

⁠*Unicidad.* Si $x<\tilde x$ estuvieran en todos los intervalos, sería $b_n-a_n\ge\tilde x-x=:\varepsilon>0$ para todo $n$, en contra de [(7.1)](#gl-7-1).
:::

:::abbildung hm1/k1schachtelung 7
Bisección para $x^2=2$: si el cuadrado del punto medio es menor que 2, este pasa a ser el nuevo extremo izquierdo; si no, el nuevo extremo derecho. La longitud es $b_n-a_n=2^{1-n}$.
:::

:::satz Teorema 7.2 (Raíz cuadrada)
<span class="anker" id="satz-7-2"></span>

Para cada $y\in\mathbb{R}_0^+$ existe exactamente un $x\in\mathbb{R}_0^+$ con $x^2=y$. Se escribe $x=\sqrt y$ («__raíz cuadrada__ de $y$»). Para $x,y\ge0$ se cumple $\sqrt{xy}=\sqrt x\sqrt y$.
:::

⁠**Cómo leerlo:** La raíz es la solución no negativa, $\sqrt{4}=2$ y no $-2$. La ecuación $z^2=2$ tiene dos soluciones: $\sqrt2$ y $-\sqrt2$, pues $(-1)(-1)=1$. La regla del producto necesita $x,y\ge0$: $\sqrt{(-1)(-1)}=1$, pero $\sqrt{-1}$ no existe en $\mathbb{R}$. **Caso límite** $y=0$: La única solución es $x=0$.

:::beweis Existencia para $y=2$, unicidad, regla del producto
Se empieza con $a_1=1$, $b_1=2$ y se divide por la mitad como en la fig. [7](#abb-7). Todos los $a_n$, $b_n$ son fracciones, así que por el teorema [6.1](das-vollstandigkeitsaxiom.html#satz-6-1) nunca es $a_n^2=2$ ni $b_n^2=2$. Eso da $a_n^2<2<b_n^2$ y $b_n-a_n=2^{1-n}\le\frac1n$ porque $2^{n-1}\ge n$ (ejercicio [10](elementare-ungleichungen.html#aufg-10)). Por el teorema [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (vi) se cumple [(7.1)](#gl-7-1), luego existe $x$ con $a_n\le x\le b_n$ para todo $n$.

Por qué $x^2=2$: de $a_n\le x\le b_n$ se sigue por el teorema [4.2](anordnungsaxiome.html#satz-4-2) (e) que $a_n^2\le x^2\le b_n^2$. También 2 está en $[a_n^2,b_n^2]$. Este intervalo tiene la longitud $(b_n-a_n)(b_n+a_n)\le4\cdot\frac1n$. Por tanto, la distancia entre $x^2$ y 2 es menor que cualquier número positivo y, en consecuencia, cero. Para otros $y>0$ se empieza con $[0,y+1]$; si un punto medio $m$ da exactamente $m^2=y$, es $x=m$. Para $y=0$ es $x=0$. *Unicidad:* de $u>v\ge0$ se sigue $u^2>v^2$; dos números no negativos distintos tienen cuadrados distintos.

⁠*Regla del producto:* $\sqrt x\sqrt y\ge0$ y $(\sqrt x\sqrt y)^2=xy$ (M1, M2), y la solución no negativa es única.
:::

::::beispiel
Tras seis pasos es $1{,}40625\le\sqrt2\le1{,}4375$, anchura $2^{-5}=0{,}03125$. Los números decimales son la misma idea con diez partes en lugar de dos: cada cifra reduce el intervalo a una décima parte. Por eso todo número real tiene una representación [(0.1)](von-grund-auf-zahlbereiche-und-dezimalzahlen.html#gl-0-1).
::::

:::frage Basta con leer $\sqrt2$ en la calculadora. ¿Para qué tanto esfuerzo?
Para cualquier valor numérico, basta. Pero la calculadora muestra una fracción, $1{,}414213562$, cuyo cuadrado no es 2. La pregunta aquí es: ¿existe siquiera un número con cuadrado exactamente 2? En $\mathbb{Q}$ no, en $\mathbb{R}$ sí, y esta diferencia sostiene después los límites y la continuidad.
:::

:::aufgabe Ejercicio 8 ★★★ La raíz cuadrada de 3
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Realiza tres pasos de bisección para $x^2=3$, empezando en $[1,2]$. ¿Qué anchura tiene el resultado?

</li>

<li>

Demuestra $\sqrt3\notin\mathbb{Q}$. Pista: un número que no es divisible por 3 tiene la forma $3k\pm1$.

</li>

<li>

¿En qué punto falla la misma demostración para $\sqrt4$?

</li>

</ol>

:::loesung
(a) Punto medio $1{,}5$: $2{,}25<3$, luego $[1{,}5;\,2]$. Punto medio $1{,}75$: $3{,}0625>3$, luego $[1{,}5;\,1{,}75]$. Punto medio $1{,}625$: $2{,}640625<3$, luego $[1{,}625;\,1{,}75]$. Anchura $\frac18=0{,}125$. (b) Suposición: $\sqrt3=\frac pq$, $p,q\in\mathbb{N}$, no ambos divisibles por 3. Entonces $p^2=3q^2$. Si fuera $p=3k\pm1$, sería $p^2=3(3k^2\pm2k)+1$, no divisible por 3. Luego $p=3k$, así que $q^2=3k^2$, e igualmente $q$ es divisible por 3. Contradicción. (c) De $p^2=4q^2$ se sigue $p=2k$ y $k^2=q^2$. Eso no dice nada sobre la divisibilidad de $q$: $\sqrt4=\frac21$.
:::
:::
