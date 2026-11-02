---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1211200
summary: Qué hay que suponer sobre los números y por qué la raíz cuadrada de 2 no es una fracción
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Todas las reglas de cálculo se siguen por razonamiento lógico de unos pocos axiomas: los axiomas de cuerpo para la suma y el producto y los axiomas de orden para «positivo».

</li>

<li>

Las fracciones también cumplen estos axiomas, pero tienen huecos: ninguna fracción $r$ resuelve $r^2=2$.

</li>

<li>

El axioma de completitud cierra los huecos: todo conjunto no vacío que tiene una cota inferior (un número menor o igual que todos los elementos) tiene también una máxima. Con él, los números reales quedan determinados de forma única, y $\sqrt2$ existe.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Los conjuntos y las proposiciones obedecen a las mismas reglas, demostradas por tabla. $\mathcal A\Rightarrow\mathcal B$ solo es falsa con $v\Rightarrow f$.

</li>

<li>

Negar intercambia $\forall$ y $\exists$. Los cuantificadores distintos no se pueden intercambiar.

</li>

<li>

Cuerpo: 10 axiomas, vínculo $x(y+z)=xy+xz$. Orden: $z<0$ invierte la desigualdad, $x\ne0\Rightarrow x^2>0$.

</li>

<li>

Inducción: caso base más paso.

</li>

<li>

$\sqrt2\notin\mathbb{Q}$. Completitud: todo conjunto no vacío acotado inferiormente tiene un ínfimo en el cuerpo. Eso separa $\mathbb{R}$ de $\mathbb{Q}$. Los intervalos encajados dan $\sqrt y$.

</li>

<li>

$|x+y|\le|x|+|y|$, $(1+x)^n>1+nx$, $\sqrt{xy}\le\frac{x+y}2$, $\sum|x_iy_i|\le\|\vec x\|\|\vec y\|$, $\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** Nada se acepta por fe: cada regla está al final de una cadena de razonamientos que empieza en un axioma.

| Resultado | De dónde viene |
|---|---|
| Reglas de De Morgan, contraposición | finitos casos: tabla de verdad (etapa [1](mengen-und-aussagen.html#stufe-1)) |
| Negación de «para todo» | «para todo» es un largo «y», De Morgan (etapa [2](quantoren-und-indirekter-beweis.html#stufe-2)) |
| $(-1)\cdot(-1)=1$, cálculo con fracciones | axiomas de cuerpo, sobre todo la ley distributiva (etapa [3](korperaxiome.html#stufe-3)) |
| La desigualdad se invierte con $z<0$ | axiomas de orden (etapa [4](anordnungsaxiome.html#stufe-4)) |
| Fórmulas de sumas, leyes de potencias | construcción de los números naturales: inducción (etapa [5](vollstandige-induktion-summe-und-produkt.html#stufe-5)) |
| Arquímedes, $\sqrt2$ existe | completitud (etapas [6](das-vollstandigkeitsaxiom.html#stufe-6) y [7](intervallschachtelung-und-wurzeln.html#stufe-7)) |
| Desigualdad triangular | posición en la recta numérica (etapa [8](abstand-und-betrag.html#stufe-8)) |
| Young, Cauchy-Schwarz | los cuadrados no son negativos (etapa [9](elementare-ungleichungen.html#stufe-9)) |
