---
title: Etapa 1: Pares en lugar de números sueltos
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Números complejos
order: 1220200
summary: En mathbb R , x 2=-1 no tiene solución.
tags: forma binómica
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
En $\mathbb{R}$, $x^2=-1$ no tiene solución. Esta etapa construye un conjunto mayor de números en el que la ecuación tiene solución y que contiene a $\mathbb{R}$ sin cambios.
:::

**La idea.** Cada ampliación de los números resuelve una ecuación que antes no tenía solución: $x+1=0$ lleva de $\mathbb{N}$ a $\mathbb{Z}$, $2x=1$ de $\mathbb{Z}$ a $\mathbb{Q}$, $x^2=2$ de $\mathbb{Q}$ a $\mathbb{R}$. Con $x^2=-1$ el caso es distinto. La parábola $y=x^2$ nunca alcanza la altura $-1$ (fig. [1](#abb-1)), porque en $\mathbb{R}$ se cumple $x^2\ge0$ ([Parte 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). No falta un punto entre otros puntos, como con $\sqrt2$, sino que todos los puntos de la recta numérica quedan descartados. La solución tiene que estar fuera de la recta. Por eso se añade una segunda coordenada: se calcula con pares $(x,y)$. Los pares $(x,0)$ deben seguir siendo los números reales, y $(0,1)$ debe tener por cuadrado $(-1,0)$.

:::abbildung hm1/k2parabel 1
La recta $y=2$ corta dos veces a la parábola, y las soluciones $\pm\sqrt2$ están en la recta numérica. La recta $y=-1$ no la corta nunca: ningún $x$ real resuelve $x^2=-1$.
:::

:::definition Definición 1.1 (Números complejos)
<span class="anker" id="satz-1-1"></span>

El conjunto de los números complejos es $\mathbb{C}:=\{(x,y):x,y\in\mathbb{R}\}$ con la suma $\oplus$ y la multiplicación $\odot$:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} (x_1,y_1)\oplus(x_2,y_2)&:=(x_1+x_2,\;y_1+y_2),\\ (x_1,y_1)\odot(x_2,y_2)&:=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1). \end{aligned} \tag{1.1|1.2}$$

El elemento cero es $(0,0)$, el elemento unidad es $(1,0)$, la unidad imaginaria es $\mathrm{i}:=(0,1)$.
:::

⁠**Cómo leerlo:** $x$ e $y$ son números reales sin unidades, $\oplus$ y $\odot$ son operaciones nuevas para pares. **Caso límite:** Para $y_1=y_2=0$, [(1.1)](#gl-1-1) y [(1.2)](#gl-1-2) dan los pares $(x_1+x_2,0)$ y $(x_1x_2,0)$. Así que los pares $(x,0)$ se calculan exactamente como los números reales $x$. Por eso se escribe $x$ en lugar de $(x,0)$, $+$ en lugar de $\oplus$, $\cdot$ en lugar de $\odot$, y se cumple $\mathbb{R}\subset\mathbb{C}$.

:::satz Teorema 1.2 (Unidad imaginaria y forma binómica)
<span class="anker" id="satz-1-2"></span>

<ol class="rm">

<li>

Se cumple $\mathrm{i}^2=-1$.

</li>

<li>

Todo número complejo tiene exactamente una __forma binómica__ $z=x+\mathrm{i}y$ con $x,y\in\mathbb{R}$.

</li>

<li>

En forma binómica se cumple $(x_1+\mathrm{i}y_1)+(x_2+\mathrm{i}y_2)=(x_1+x_2)+\mathrm{i}(y_1+y_2)$ y

</li>

</ol>

<span class="anker" id="gl-1-3"></span>
$$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1). \tag{1.3}$$
:::

⁠**Cómo leerlo:** Nadie tiene que aprender de memoria la fórmula [(1.3)](#gl-1-3): se desarrollan los paréntesis, se sustituye $\mathrm{i}^2=-1$ y se ordena. El signo menos de $x_1x_2-y_1y_2$ es el $\mathrm{i}^2$. En matemáticas la unidad imaginaria se llama $\mathrm{i}$; en electrotecnia, $\mathrm{j}$, porque allí $i$ es la corriente. Este capítulo escribe $\mathrm{i}$ en redonda. **Validez:** $x$ e $y$ tienen que ser reales. Si no, la representación no es única: $\mathrm{i}=\mathrm{i}+\mathrm{i}\cdot0=0+\mathrm{i}\cdot1$.

:::beweis Calcular con pares
(i) Por [(1.2)](#gl-1-2) es $\mathrm{i}\cdot\mathrm{i}=(0,1)\odot(0,1)=(0\cdot0-1\cdot1,\;0\cdot1+0\cdot1)=(-1,0)=-1$.

(ii) Para $y$ real es $\mathrm{i}y=(0,1)\odot(y,0)=(0\cdot y-1\cdot0,\;0\cdot0+y\cdot1)=(0,y)$, luego $x+\mathrm{i}y=(x,0)\oplus(0,y)=(x,y)$. El par determina $x$ e $y$ de forma única.

(iii) Por (ii), los segundos miembros son exactamente los pares de [(1.1)](#gl-1-1) y [(1.2)](#gl-1-2).
:::

**Ejemplo.** Suma y producto del modelo de referencia:

$$z_1+z_2=(3+1)+\mathrm{i}(1+2)=4+3\mathrm{i},\qquad z_1z_2=(3+\mathrm{i})(1+2\mathrm{i})=3+6\mathrm{i}+\mathrm{i}+2\mathrm{i}^2=1+7\mathrm{i}.$$

La fórmula de pares [(1.2)](#gl-1-2) da lo mismo: $(3\cdot1-1\cdot2,\;3\cdot2+1\cdot1)=(1,7)$. Las potencias de $\mathrm{i}$ se repiten con período 4: $\mathrm{i}^1=\mathrm{i}$, $\mathrm{i}^2=-1$, $\mathrm{i}^3=-\mathrm{i}$, $\mathrm{i}^4=1$. Por tanto solo cuenta el resto de dividir $n$ entre 4, por ejemplo $\mathrm{i}^{10}=\mathrm{i}^8\,\mathrm{i}^2=-1$.

:::frage ¿Existe $\mathrm{i}$ de verdad, o es un truco de cálculo?
En la recta numérica no existe $\mathrm{i}$; hasta ahí la duda es acertada. Pero $\mathrm{i}$ es el par $(0,1)$, y [(1.2)](#gl-1-2) es una regla inequívoca para pares. «Imaginario» es solo un nombre histórico.
:::

:::aufgabe Ejercicio 1 ★ Calcular en forma binómica
<span class="anker" id="aufg-1"></span>

Escribe en la forma $x+\mathrm{i}y$: (a) $(4-\mathrm{i})(2+3\mathrm{i})$, (b) $(1+\mathrm{i})^2$ y, con ello, $(1+\mathrm{i})^4$, (c) $\mathrm{i}^{27}+\mathrm{i}^{42}$.

:::loesung
(a) $8+12\mathrm{i}-2\mathrm{i}-3\mathrm{i}^2=11+10\mathrm{i}$. (b) $(1+\mathrm{i})^2=1+2\mathrm{i}+\mathrm{i}^2=2\mathrm{i}$, así que $(1+\mathrm{i})^4=(2\mathrm{i})^2=-4$. (c) $27=4\cdot6+3$ da $\mathrm{i}^{27}=\mathrm{i}^3=-\mathrm{i}$, y $42=4\cdot10+2$ da $\mathrm{i}^{42}=\mathrm{i}^2=-1$. La suma es $-1-\mathrm{i}$.
:::
:::
