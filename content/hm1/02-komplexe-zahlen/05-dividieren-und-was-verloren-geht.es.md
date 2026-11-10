---
title: Etapa 4: Dividir, y lo que se pierde
pfad: Ingeniería eléctrica / 1.er semestre / HöMa1 – Matemáticas superiores 1 / Números complejos
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Capítulo 2: Números complejos
order: 1220500
summary: La etapa 3 proporciona un producto real.
tags: 
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
La etapa [3](spiegeln-an-der-reellen-achse.html#stufe-3) proporciona un producto real. Esta etapa lo convierte en la división, muestra que $\mathbb{C}$ es un cuerpo y explica por qué falta el orden.
:::

**La idea.** Por un número real sí se puede dividir: la parte real y la parte imaginaria se dividen por separado. Así que se multiplica el numerador y el denominador de la fracción por el conjugado del denominador. El valor no cambia y el denominador se vuelve real. En el plano, $1/z$ se obtiene en dos pasos: reflejar en el eje real y dividir por $x^2+y^2$ (fig. [4](#abb-4)). Exactamente así descompone el cálculo de corriente alterna las fracciones de impedancias complejas en parte real y parte imaginaria.

:::abbildung hm1/k2kehrwert 4
El inverso de $z_2$ en dos pasos: reflejar y dividir por 5. El inverso está en la flecha de $\overline{z_2}$.
:::

:::satz Teorema 4.1 (Inverso y división)
<span class="anker" id="satz-4-1"></span>

Para todo $z=x+\mathrm{i}y\ne0$ existe el número

<span class="anker" id="gl-4-1"></span>
$$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}-\mathrm{i}\,\frac{y}{x^2+y^2}\qquad\text{con}\qquad z\cdot z^{-1}=1. \tag{4.1}$$

Para $w$ arbitrario se tiene entonces $\dfrac wz=w\cdot z^{-1}=\dfrac{w\,\overline{z}}{x^2+y^2}$.
:::

⁠**Cómo leerlo:** El denominador $x^2+y^2$ es real. **Validez:** Como $z\ne0$, es $x\ne0$ o $y\ne0$, luego $x^2+y^2>0$. Para $z=0$ no hay inverso, porque $0\cdot w=0\ne1$ para todo $w$. **Caso límite:** Para $y=0$, [(4.1)](#gl-4-1) se convierte en el inverso real $x/x^2=1/x$.

:::beweis Producto por el inverso
Sea $N:=x^2+y^2>0$. El inverso es el par $(x/N,\,-y/N)$. Por [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) se cumple

$$(x,y)\odot\Bigl(\frac xN,\frac{-y}N\Bigr)=\Bigl(\frac{x\cdot x}N-\frac{y\cdot(-y)}N,\;\frac{x\cdot(-y)}N+\frac{y\cdot x}N\Bigr)=\Bigl(\frac{x^2+y^2}N,\;0\Bigr)=(1,0).$$
:::

::::beispiel
Con el modelo de referencia, denominador $z_2\overline{z_2}=5$:

$$\frac{z_1}{z_2}=\frac{(3+\mathrm{i})(1-2\mathrm{i})}{(1+2\mathrm{i})(1-2\mathrm{i})}=\frac{3-6\mathrm{i}+\mathrm{i}-2\mathrm{i}^2}{5}=\frac{5-5\mathrm{i}}{5}=1-\mathrm{i}.$$

Comprobación: $(1-\mathrm{i})(1+2\mathrm{i})=1+2\mathrm{i}-\mathrm{i}-2\mathrm{i}^2=3+\mathrm{i}$. Además, $1/z_2=(1-2\mathrm{i})/5=0{,}2-0{,}4\mathrm{i}$ y $1/\mathrm{i}=-\mathrm{i}$.
::::

:::satz Teorema 4.2 ($\mathbb{C}$ es un cuerpo)
<span class="anker" id="satz-4-2"></span>

$\mathbb{C}$ con $+$ y $\cdot$ cumple todos los axiomas de cuerpo del [capítulo 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html): leyes conmutativa, asociativa y distributiva, elementos neutros $0\ne1$, para cada $z$ el opuesto $-z$ y para cada $z\ne0$ el inverso $1/z$.
:::

⁠**Cómo leerlo:** Lo que en el [capítulo 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) se deduce solo de los axiomas de cuerpo vale también en $\mathbb{C}$: el cálculo con fracciones, las identidades notables y la conclusión de $zw=0$ a $z=0$ o $w=0$.

:::beweis Idea
La suma se hace por separado y hereda todas las leyes de $\mathbb{R}$, con $-z=-x-\mathrm{i}y$. [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) no cambia al intercambiar los índices 1 y 2: la multiplicación es conmutativa. Las leyes asociativa y distributiva se demuestran calculando ambos miembros según [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2). $(1,0)\odot(x,y)=(x,y)$ muestra el elemento unidad, [(4.1)](#gl-4-1) el axioma (M4), el inverso.
:::

:::satz Teorema 4.3 ($\mathbb{C}$ no es ordenado)
<span class="anker" id="satz-4-3"></span>

No existe ninguna relación «$>0$» en $\mathbb{C}$ con los axiomas de orden del [capítulo 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html): (T1) Para cada $x$ se cumple exactamente una de $x>0$, $x=0$, $-x>0$. (T2) De $x>0$ e $y>0$ se deduce $x+y>0$. (T3) De $x>0$ e $y>0$ se deduce $x\cdot y>0$.
:::

⁠**Cómo leerlo:** Para números no reales, $z<w$ y $z>0$ no tienen significado. Solo se pueden comparar magnitudes reales como $\operatorname{Re}(z)$ o $|z|$.

:::beweis Contradicción
Supongamos que existiera tal relación. Entonces, para todo $x\ne0$ sería $x\cdot x>0$: si $x>0$, se deduce de (T3); si $-x>0$, de (T3) y $(-x)(-x)=x\cdot x$. En particular serían $1\cdot1>0$ e $\mathrm{i}\cdot\mathrm{i}>0$. Con (T2) se deduciría $1\cdot1+\mathrm{i}\cdot\mathrm{i}>0$. Eso es $1+(-1)=0>0$, una contradicción con (T1).
:::

:::frage ¿No se puede fijar un orden de clasificación, por ejemplo primero por la parte real y luego por la parte imaginaria?
Clasificar así sí se puede. Lo que pasa es que no es compatible con la multiplicación: daría $\mathrm{i}>0$, pero $\mathrm{i}\cdot\mathrm{i}=-1<0$, en contra de (T3). La demostración muestra que esto afecta a cualquier elección.
:::

:::aufgabe Ejercicio 4 ★ Dividir
<span class="anker" id="aufg-4"></span>

(a) Escribe $\dfrac{7+\mathrm{i}}{2-\mathrm{i}}$ en forma binómica. (b) Calcula $\dfrac{10}{1+3\mathrm{i}}+\dfrac{3-\mathrm{i}}{1+\mathrm{i}}$. (c) Resuelve $(2+\mathrm{i})z-3=-2+3\mathrm{i}$ y comprueba el resultado.

:::loesung
(a) $\dfrac{(7+\mathrm{i})(2+\mathrm{i})}{(2-\mathrm{i})(2+\mathrm{i})}=\dfrac{14+7\mathrm{i}+2\mathrm{i}+\mathrm{i}^2}{5}=\dfrac{13+9\mathrm{i}}5=2{,}6+1{,}8\mathrm{i}$.

(b) $\dfrac{10(1-3\mathrm{i})}{10}=1-3\mathrm{i}$ y $\dfrac{(3-\mathrm{i})(1-\mathrm{i})}{2}=\dfrac{3-3\mathrm{i}-\mathrm{i}+\mathrm{i}^2}2=\dfrac{2-4\mathrm{i}}2=1-2\mathrm{i}$. La suma es $2-5\mathrm{i}$.

(c) $(2+\mathrm{i})z=1+3\mathrm{i}$, así que $z=\dfrac{(1+3\mathrm{i})(2-\mathrm{i})}{5}=\dfrac{2-\mathrm{i}+6\mathrm{i}-3\mathrm{i}^2}5=\dfrac{5+5\mathrm{i}}5=1+\mathrm{i}$. Comprobación: $(2+\mathrm{i})(1+\mathrm{i})-3=1+3\mathrm{i}-3=-2+3\mathrm{i}$.
:::
:::

:::aufgabe Ejercicio 5 ★★ Un intento de ordenar $\mathbb{C}$
<span class="anker" id="aufg-5"></span>

Alguien llama positivo a $z$ si $\operatorname{Re}(z)>0$. Examina (T1), (T2) y (T3) y da un contraejemplo para cada axioma que no se cumpla.

:::loesung
(T1) no se cumple: para $\mathrm{i}$ se tiene $\operatorname{Re}(\mathrm{i})=0$ y $\operatorname{Re}(-\mathrm{i})=0$, así que ni $\mathrm{i}$ ni $-\mathrm{i}$ son positivos, aunque $\mathrm{i}\ne0$. (T2) se cumple, porque por la etapa [3](spiegeln-an-der-reellen-achse.html#stufe-3) es $\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)>0$. (T3) no se cumple: $z=1+2\mathrm{i}$ es positivo, pero $z\cdot z=-3+4\mathrm{i}$ tiene la parte real $-3$. La razón es el término $-y_1y_2$ en la parte real del producto.
:::
:::
