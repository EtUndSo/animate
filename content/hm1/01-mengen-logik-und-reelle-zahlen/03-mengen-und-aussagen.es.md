---
title: Etapa 1: Conjuntos y proposiciones
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210300
summary: Los axiomas hablan de «todos los números con una propiedad» y de «si, entonces».
tags: diagrama de Venn, elementos, subconjunto, superconjunto, unión, intersección, diferencia, complemento
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Los axiomas hablan de «todos los números con una propiedad» y de «si, entonces». Esta etapa aporta el lenguaje para ello y un procedimiento seguro para demostrar reglas sobre conjuntos y proposiciones.
:::

**La idea.** En un conjunto solo cuenta una pregunta: ¿un objeto está en él o no? Lo mismo en una proposición: ¿verdadera o falsa? Por eso, con dos conjuntos o proposiciones hay cuatro casos, y con tres, ocho. Una regla se demuestra recorriendo todos los casos en una tabla. Un __diagrama de Venn__ (conjuntos dibujados como regiones) solo ilustra: muestra una posible disposición de los conjuntos (fig. [1](#abb-1)).

:::definition Definición 1.1 (Conjunto)
<span class="anker" id="satz-1-1"></span>

Un conjunto es una agrupación sin orden de objetos determinados y bien diferenciados, sus __elementos__. $x\in M$ significa «$x$ es elemento de $M$», $x\notin M$ lo contrario. Para conjuntos $A$, $B$ se establece:

| Signo | Nombre | Significado |
|---|---|---|
| $A\subset B$ | __subconjunto__ | todo elemento de $A$ está en $B$ (vale $A=B$); $B\supset A$: __superconjunto__ |
| $A=B$ | igualdad | $A\subset B$ y $B\subset A$; si no, se escribe $A\ne B$ |
| $A\cup B$ | __unión__ | todos los elementos que están en $A$ o en $B$, también en ambos |
| $A\cap B$ | __intersección__ | todos los elementos que están en $A$ y en $B$ |
| $A\setminus B$ | __diferencia__ | todos los elementos de $A$ que no están en $B$ |
| $A^c$ | __complemento__ | todos los elementos de un superconjunto fijo que no están en $A$ |
| $\emptyset=\{\,\}$ | __conjunto vacío__ | no contiene ningún elemento |
| $\mathcal P(A)$ | __conjunto potencia__ | conjunto de todos los subconjuntos de $A$ |

$A$ y $B$ se llaman __disjuntos__ si $A\cap B=\emptyset$.
:::

⁠**Cómo leerlo:** En el modelo de referencia es $A\cup B=\{1,2,3,4,5,6,7,11,12\}$, $A\cap B=\{2,3\}$, $A\setminus B=\{1,4,6,12\}$, $A^c=\{5,7,8,9,10,11\}$ respecto a $G$. Un conjunto se puede dar mediante una propiedad: $\{x\in G:x\text{ par}\}=\{2,4,6,8,10,12\}$. Es $\mathcal P(\{5,7\})=\{\emptyset,\{5\},\{7\},\{5,7\}\}$. Siempre se cumple $\emptyset\subset A$, $A\cup\emptyset=A$, $A\cap\emptyset=\emptyset$, $A\setminus B=A\cap B^c$.

:::abbildung hm1/k1venn 1
A la izquierda, los elementos de $G$ en las cuatro regiones. A la derecha está coloreado $(A\cap B)^c$, todo menos la lente.
:::

:::definition Definición 1.2 (Proposición y conectivas)
<span class="anker" id="satz-1-2"></span>

Una proposición es una afirmación que solo puede ser verdadera ($v$) o falsa ($f$). A partir de proposiciones $\mathcal A$, $\mathcal B$ surgen otras nuevas, definidas por esta __tabla de verdad__:

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\mathcal A\vee\mathcal B$ | $\mathcal A\wedge\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\mathcal A\Leftrightarrow\mathcal B$ |
|---|---|---|---|---|---|---|
| $v$ | $v$ | $f$ | $v$ | $v$ | $v$ | $v$ |
| $v$ | $f$ | $f$ | $v$ | $f$ | $f$ | $f$ |
| $f$ | $v$ | $v$ | $v$ | $f$ | $v$ | $f$ |
| $f$ | $f$ | $v$ | $f$ | $f$ | $v$ | $v$ |

Los nombres son __negación__, __disyunción__, __conjunción__, __implicación__ y __equivalencia__.
:::

⁠**Cómo leerlo:** «2 es primo» es una proposición verdadera; «¿Qué hora es?» no es una proposición. También «todo número par a partir de 4 es suma de dos primos» es una proposición, aunque nadie sabe si es verdadera (conjetura de Goldbach). Las proposiciones pueden depender de un __parámetro__: $\mathcal T(n):=(n\text{ divide a }12)$ es verdadera para $n=4$ y falsa para $n=5$. «O» incluye «ambos». $\neg$ es lo que liga con más fuerza: $\neg\mathcal A\vee\mathcal B$ significa $(\neg\mathcal A)\vee\mathcal B$. $\mathcal A\Leftrightarrow\mathcal B$ equivale a $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal A)$. Dos proposiciones con la misma columna en la tabla son *equivalentes*. Si $\mathcal A\Rightarrow\mathcal B$ es verdadera y $\mathcal A$ es verdadera, entonces $\mathcal B$ es verdadera. Si $\mathcal A$ es falsa, la implicación no dice nada sobre $\mathcal B$.

:::frage ¿Por qué $f\Rightarrow v$ es verdadera? De algo falso no se sigue nada.
Lo correcto es: una $\mathcal A$ falsa no dice nada sobre $\mathcal B$. Justo por eso la implicación no se viola en ese caso. La convención es forzosa: $\mathcal E(n)$ debe ser verdadera para todo $n$, y $n=6$ da $f\Rightarrow v$, $n\le5$ da $f\Rightarrow f$. Si estas filas fueran falsas, $\mathcal E(n)$ sería falsa ahí. Solo $v\Rightarrow f$ no aparece para ningún $n$, y esa es toda la afirmación: $\{n\ge7\}$ está contenido en $\{n>5\}$. Una implicación es una relación de subconjunto.
:::

:::satz Teorema 1.3 (Reglas de cálculo y tautologías)
<span class="anker" id="satz-1-3"></span>

Una __tautología__ es una proposición que es verdadera para todos los valores de verdad de sus componentes. Para conjuntos dentro de un superconjunto y para proposiciones se cumplen las reglas siguientes:

| Nombre | Conjuntos | Proposiciones |
|---|---|---|
| Doble negación | $(A^c)^c=A$ | $\neg(\neg\mathcal A)\Leftrightarrow\mathcal A$ |
| Conmutativa | $A\cap B=B\cap A$, $A\cup B=B\cup A$ | $(\mathcal A\wedge\mathcal B)\Leftrightarrow(\mathcal B\wedge\mathcal A)$, $(\mathcal A\vee\mathcal B)\Leftrightarrow(\mathcal B\vee\mathcal A)$ |
| Asociativa | $(A\cap B)\cap C=A\cap(B\cap C)$, igual con $\cup$ | $(\mathcal A\wedge(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\wedge\mathcal C)$, igual con $\vee$ |
| Distributiva | $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$, $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ | $(\mathcal A\wedge(\mathcal B\vee\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\vee(\mathcal A\wedge\mathcal C))$, $(\mathcal A\vee(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\vee\mathcal B)\wedge(\mathcal A\vee\mathcal C))$ |
| De Morgan | $(A\cap B)^c=A^c\cup B^c$, $(A\cup B)^c=A^c\cap B^c$ | $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$, $\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$ |
| Idempotencia | $A\cup A=A$, $A\cap A=A$ | $(\mathcal A\vee\mathcal A)\Leftrightarrow\mathcal A$, $(\mathcal A\wedge\mathcal A)\Leftrightarrow\mathcal A$ |
| Implicación | $A\subset B\Leftrightarrow A^c\cup B=G$ ($G$ superconjunto) | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\mathcal B)$ |
| Contraposición | $A\subset B\Leftrightarrow B^c\subset A^c$ | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$ |
| Transitividad | $(A\subset B\wedge B\subset C)\Rightarrow A\subset C$ | $((\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C))\Rightarrow(\mathcal A\Rightarrow\mathcal C)$ |
:::

⁠**Cómo leerlo:** A izquierda y derecha está la misma regla, porque toda relación entre conjuntos es una proposición sobre elementos: $A\subset B$ significa «para todo $x$: $(x\in A)\Rightarrow(x\in B)$», $A=B$ significa «para todo $x$: $(x\in A)\Leftrightarrow(x\in B)$», y $x\in A\cap B$, $x\in A\cup B$, $x\in A\setminus B$ significan $(x\in A)\wedge(x\in B)$, $(x\in A)\vee(x\in B)$, $(x\in A)\wedge(x\notin B)$. Las puertas lógicas de la electrónica digital son $\neg$, $\wedge$, $\vee$ como circuito, y De Morgan permite construir un Y a partir de O e inversores.

:::beweis De Morgan y contraposición por tabla
Se recorren los cuatro casos de los componentes. Si se lee $v$ como «$x$ está en el conjunto», esto es a la vez la demostración para conjuntos (__tabla de elementos__).

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\neg\mathcal B$ | $\neg(\mathcal A\wedge\mathcal B)$ | $\neg\mathcal A\vee\neg\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\neg\mathcal B\Rightarrow\neg\mathcal A$ |
|---|---|---|---|---|---|---|---|
| $v$ | $v$ | $f$ | $f$ | $f$ | $f$ | $v$ | $v$ |
| $v$ | $f$ | $f$ | $v$ | $v$ | $v$ | $f$ | $f$ |
| $f$ | $v$ | $v$ | $f$ | $v$ | $v$ | $v$ | $v$ |
| $f$ | $f$ | $v$ | $v$ | $v$ | $v$ | $v$ | $v$ |

Las columnas 5 y 6 coinciden, y también las columnas 7 y 8. Las demás reglas se demuestran igual. La transitividad de la inclusión se sigue de la de la implicación: de $x\in A$ se sigue $x\in B$, y de ahí $x\in C$.
:::

::::beispiel
$(A\cap B)^c=G\setminus\{2,3\}$ tiene 10 elementos. A la derecha está $A^c\cup B^c=\{5,7,8,9,10,11\}\cup\{1,4,6,8,9,10,12\}$, los mismos 10 elementos. La contraposición como herramienta de demostración: en lugar de «$n^2$ par $\Rightarrow$ $n$ par» se demuestra «$n$ impar $\Rightarrow$ $n^2$ impar»: $(2k+1)^2=2(2k^2+2k)+1$.
::::

⁠**Casos límite:** Para $B=\emptyset$, De Morgan se convierte en $G=G$. El dominio importa: $(n\ge7\Leftrightarrow n>6)$ se cumple en $\mathbb{N}$, pero para $n=13/2$ es $f\Leftrightarrow v$, es decir, falsa.

:::aufgabe Ejercicio 1 ★ Calcular con conjuntos
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Calcula en el modelo de referencia $(A\cup B)^c$ y $A\setminus(A\cap B)$.

</li>

<li>

Demuestra con una tabla de elementos: $(A\setminus B)\cup(B\setminus A)=(A\cup B)\setminus(A\cap B)$.

</li>

<li>

¿Cuántos elementos tiene $\mathcal P(A\cap B)$? Predice cuántos tiene $\mathcal P(M)$ si $M$ tiene exactamente $n$ elementos, y justifícalo.

</li>

</ol>

:::loesung
(a) $A\cup B=\{1,2,3,4,5,6,7,11,12\}$, luego $(A\cup B)^c=\{8,9,10\}$. $A\setminus(A\cap B)=A\setminus\{2,3\}=\{1,4,6,12\}$, que es $A\setminus B$. (b) Para los casos $(\in,\in)$, $(\in,\notin)$, $(\notin,\in)$, $(\notin,\notin)$ de $x$ en $A$, $B$, ambos lados dan $\notin,\in,\in,\notin$: $x$ pertenece si está en exactamente uno de los conjuntos. (c) $A\cap B=\{2,3\}$ tiene 2 elementos, $\mathcal P(A\cap B)$ tiene $2^2=4$. Con $n$ elementos se decide para cada uno por separado: dentro o fuera. Eso da $2^n$ subconjuntos.
:::
:::

:::aufgabe Ejercicio 2 ★★ Razonar con tablas
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Demuestra la transitividad de la implicación con una tabla de ocho filas.

</li>

<li>

Si el fusible está intacto ($\mathcal A$), la lámpara se enciende ($\mathcal B$). Esta implicación es verdadera, y la lámpara no se enciende. ¿Qué se sigue para el fusible? ¿Y si la lámpara se enciende?

</li>

<li>

¿Es $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\mathcal B\Rightarrow\mathcal A)$ una tautología?

</li>

</ol>

:::loesung
(a) La hipótesis $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C)$ solo es verdadera para $(\mathcal A,\mathcal B,\mathcal C)=(v,v,v)$, $(f,v,v)$, $(f,f,v)$, $(f,f,f)$. En las cuatro, $\mathcal A\Rightarrow\mathcal C$ es verdadera. En las otras cuatro filas es falsa, y la proposición completa es, por tanto, verdadera. (b) Contraposición: $\neg\mathcal B\Rightarrow\neg\mathcal A$, el fusible no está intacto. Si la lámpara se enciende, no se sigue nada: la fila $f\Rightarrow v$ está permitida. (c) No: para $\mathcal A=v$, $\mathcal B=f$, a la izquierda queda $f\Leftrightarrow v$, es decir, falsa.
:::
:::
