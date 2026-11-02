---
title: Etapa 2: Cuantificadores y demostración indirecta
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210400
summary: Todos los axiomas tienen la forma «para todo x existe un y ».
tags: cuantificador universal, cuantificador existencial, contraejemplo, hipótesis de contradicción, antinomia de Russell
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Todos los axiomas tienen la forma «para todo $x$ existe un $y$». Esta etapa aclara cómo se leen y se niegan tales oraciones, y cómo se convierte una negación en una demostración.
:::

**La idea.** «Para todo $x$ de $\{x_1,x_2,\dots\}$ se cumple $\mathcal A(x)$» es un largo y: $\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots$ «Existe un $x$» es un largo o. Al negar, De Morgan convierte y en o. Por eso, al negar, «para todo» se convierte en «existe».

:::definition Definición 2.1 (Cuantificadores)
<span class="anker" id="satz-2-1"></span>

$\forall$ significa «para todo» (__cuantificador universal__), $\exists$ «existe al menos un» (__cuantificador existencial__), $\exists_1$ «existe exactamente un», $\nexists$ «no existe ningún».
:::

⁠**Cómo leerlo:** Ejemplos verdaderos en el modelo de referencia son $\forall x\in A:x\le12$; $\exists x\in A:x>5$ (por ejemplo $x=6$); $\exists_1x\in A\cap B:x>2$ (a saber, $x=3$); $\nexists x\in B:x=9$. También la divisibilidad es una proposición con cuantificador: $m\mid p$ («$m$ divide a $p$») significa $\exists n\in\mathbb{N}:m\cdot n=p$, así que $6\mid12$ porque $6\cdot2=12$, y $7\nmid12$. El conjunto de los números primos es $\{p\in\mathbb{N}\setminus\{1\}:\nexists m\in\{2,\dots,p-1\}\text{ con }m\mid p\}$.

:::satz Teorema 2.2 (Regla de negación)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-1"></span>
$$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\neg\mathcal A(x)\bigr),\quad \neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\neg\mathcal B(y)\bigr). \tag{2.1}$$
:::

⁠**Cómo leerlo:** Cambiar el cuantificador, negar la proposición; con cuantificadores anidados, uno tras otro. En el modelo de referencia, la negación de $\forall n\in\mathbb{N}:\mathcal E(n)$ es la proposición falsa $\exists n\in\mathbb{N}:(n\ge7\wedge n\le5)$. **Idea de la demostración:** $\neg(\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots)$ es, por De Morgan, $\neg\mathcal A(x_1)\vee\neg\mathcal A(x_2)\vee\dots$; la segunda regla surge igual. **Caso límite** $M=\emptyset$: «Para todo $x\in\emptyset$» es siempre verdadera, «existe $x\in\emptyset$» siempre falsa.

:::frage ¿Bastan cinco ejemplos para demostrar «para todo»?
No. Un ejemplo solo comprueba un $x$. Según [(2.1)](#gl-2-1), en cambio, un solo __contraejemplo__ refuta la proposición «para todo». A la inversa, «existe» se demuestra con un ejemplo.
:::

**Ejemplo: cuantificadores anidados.** Sean $H$ los aparatos de un hogar, $F$ los fusibles, y $K(g,s)$ signifique «el aparato $g$ está conectado al fusible $s$». Entonces

$$\mathcal P:=\bigl(\forall g\in H\ \exists s\in F:K(g,s)\bigr),\qquad \mathcal Q:=\bigl(\exists s\in F\ \forall g\in H:K(g,s)\bigr)$$

dicen cosas distintas (fig. [2](#abb-2)): en $\mathcal P$, $s$ puede depender del aparato; en $\mathcal Q$, un fusible vale para todos. De $\mathcal Q$ se sigue $\mathcal P$; el recíproco es falso. **El orden de cuantificadores distintos no se puede intercambiar.** Las negaciones son $\neg\mathcal P=(\exists g\ \forall s:\neg K(g,s))$, un aparato no está conectado a ningún fusible, y $\neg\mathcal Q=(\forall s\ \exists g:\neg K(g,s))$, cada fusible deja fuera al menos un aparato.

:::abbildung hm1/k1quantoren 2
La imagen de la derecha cumple ambas proposiciones; la de la izquierda, solo la primera.
:::

:::satz Teorema 2.3 (Demostración indirecta)
<span class="anker" id="satz-2-3"></span>

Si $\neg\mathcal A\Rightarrow\mathcal B$ es verdadera y $\mathcal B$ es falsa, entonces $\mathcal A$ es verdadera.
:::

⁠**Cómo leerlo:** Se supone lo contrario de la afirmación (__hipótesis de contradicción__) y se razona hasta que sale algo falso. Una mirada a la tabla muestra el mecanismo: si $\neg\mathcal A$ fuera verdadera, también $\mathcal B$ tendría que ser verdadera. Por tanto, $\neg\mathcal A$ es falsa. Si hay que demostrar indirectamente una implicación $\mathcal A\Rightarrow\mathcal B$, la suposición es, por De Morgan, $\mathcal A\wedge\neg\mathcal B$. **Ejemplo:** No existe un número racional positivo mínimo. Suposición: $r$ sería el mínimo. Entonces $r/2$ es racional, positivo y menor que $r$. Eso es falso, así que no existe tal $r$.

**Por qué hacen falta axiomas.** Sea $M=\{N:N\notin N\}$ el conjunto de todos los conjuntos que no se contienen a sí mismos (__antinomia de Russell__, 1903). Si $M\in M$ es verdadera, $M$ no cumple la condición, luego $M\notin M$. Si $M\notin M$ es verdadera, $M$ cumple la condición, luego $M\in M$. Ambas cosas son imposibles; la construcción no es admisible. Igual de contradictoria es la frase «Esta frase es falsa». Tales hallazgos desencadenaron la crisis de los fundamentos de las matemáticas, desde la exigencia de Hilbert de una construcción sin contradicciones (1900) hasta los teoremas de incompletitud de Gödel (1931). La lección: la certeza solo existe en relación con supuestos establecidos. Por eso los números se construyen sobre axiomas.

:::aufgabe Ejercicio 3 ★★ Negar y demostrar indirectamente
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Niega: «Todo circuito contiene un componente que se calienta».

</li>

<li>

Niega $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\frac1n<\varepsilon$. ¿La proposición se vuelve verdadera o falsa si se intercambian los cuantificadores?

</li>

<li>

Demuestra indirectamente: si $n^2$ es impar, entonces $n$ es impar.

</li>

</ol>

:::loesung
(a) «Existe un circuito en el que ningún componente se calienta». (b) Negación: $\exists\varepsilon>0\ \forall n\in\mathbb{N}:\frac1n\ge\varepsilon$. Intercambiada: $\exists n\in\mathbb{N}\ \forall\varepsilon>0:\frac1n<\varepsilon$ es falsa, pues para $\varepsilon=\frac1n$ queda $\frac1n<\frac1n$. La proposición original, en cambio, es verdadera, como muestra la etapa [6](das-vollstandigkeitsaxiom.html#stufe-6). (c) Suposición: $n^2$ impar y $n$ par, $n=2k$. Entonces $n^2=2\cdot2k^2$ es par, contradicción.
:::
:::
