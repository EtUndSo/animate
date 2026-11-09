---
title: Etapa 3: Axiomas de cuerpo
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1210500
summary: ¿Qué pocas reglas para la suma y el producto hay que suponer para que todas las demás reglas de cálculo se puedan demostrar?
tags: operación, ley distributiva, diferencia, cociente
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
¿Qué pocas reglas para la suma y el producto hay que suponer para que todas las demás reglas de cálculo se puedan demostrar?
:::

**La idea.** Cada sistema numérico surge porque en el anterior una ecuación no tiene solución (fig. [3](#abb-3)): $x+3=1$ no tiene solución en $\mathbb{N}$, $3x=1$ no la tiene en $\mathbb{Z}$. Un cuerpo es el sistema en el que ambos tipos de ecuación siempre se pueden resolver: la suma y el producto se pueden invertir. Los axiomas no exigen más. El único vínculo entre la suma y el producto es la ley distributiva, y casi todas las demostraciones de esta etapa pasan por ella.

:::abbildung hm1/k1zahlbereiche 3
Cada ecuación solo se puede resolver a partir del sistema en el que aparece.
:::

:::definition Definición 3.1 (Cuerpo)
<span class="anker" id="satz-3-1"></span>

Una __operación__ asigna a cada dos elementos un elemento del mismo conjunto. Un conjunto $\mathbb K$ con dos operaciones «$+$» y «$\cdot$» se llama cuerpo si para todos $x,y,z\in\mathbb K$ se cumple:

|  | Suma | Producto |
|---|---|---|
| conmutativa | (A1) $x+y=y+x$ | (M1) $x\cdot y=y\cdot x$ |
| asociativa | (A2) $x+(y+z)=(x+y)+z$ | (M2) $x\cdot(y\cdot z)=(x\cdot y)\cdot z$ |
| elemento neutro | (A3) Existe $0\in\mathbb K$ con $x+0=x$ para todo $x$. | (M3) Existe $1\in\mathbb K$ con $x\cdot1=x$ para todo $x$. |
| elemento inverso | (A4) Para cada $x$ existe $y$ con $x+y=0$, escrito $-x$. | (M4) Para cada $x\ne0$ existe $y$ con $x\cdot y=1$, escrito $x^{-1}$ o $\frac1x$. |

A esto se añaden (AM) $x\cdot(y+z)=(x\cdot y)+(x\cdot z)$ (__ley distributiva__) y (NNE) $0\ne1$.
:::

⁠**Cómo leerlo:** Aquí $0$ y $1$ son solo nombres de dos elementos distinguidos. La resta y la división no son operaciones propias: $x-y:=x+(-y)$ y $\frac yx:=y\cdot x^{-1}$. Se acuerda que el producto va antes que la suma y que $xy:=x\cdot y$. Lo que se sigue de los axiomas vale en todo cuerpo, y por tanto también para los números complejos de la [Parte 2](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Ejemplos son $\mathbb{Q}$ y $\mathbb{R}$. $\mathbb{N}$ no es un cuerpo (no tiene 0 ni $-1$), $\mathbb{Z}$ tampoco (2 no tiene inverso). El cuerpo más pequeño es $\{0,1\}$ con $1+1=0$, la suma de la electrónica digital (XOR). **Por qué las hipótesis:** Sin (NNE), $\{0\}$ sería un cuerpo. Sin $x\ne0$ en (M4) sería $1=0\cdot0^{-1}=0$ por (iii) más abajo.

:::satz Teorema 3.2 (Reglas de cálculo en un cuerpo)
<span class="anker" id="satz-3-2"></span>

Para todos $x,y,z,u,v\in\mathbb K$ se cumple:

<ol class="rm">

<li>

Los inversos son únicos: $(xy=1\wedge xz=1)\Rightarrow y=z$ y $(x+y=0\wedge x+z=0)\Rightarrow y=z$.

</li>

<li>

Las ecuaciones tienen solución única: $x+z=y$ tiene exactamente la solución $z=y-x$ (__diferencia__). $xz=y$ tiene, para $x\ne0$, exactamente la solución $z=y\cdot x^{-1}=\frac yx$ (__cociente__).

</li>

<li>

$x\cdot0=0$, y para $x\ne0$ es $(x^{-1})^{-1}=x$.

</li>

<li>

$-(-x)=x$ y $(-x)(-y)=xy$.

</li>

<li>

$xy=0\Rightarrow(x=0\vee y=0)$.

</li>

<li>

Para $u,v\ne0$ se cumple $\frac xu\cdot\frac yv=\frac{xy}{uv}$ y $\frac xu+\frac yv=\frac{xv+yu}{uv}$, y para $u,v,y\ne0$ se cumple $\frac xu:\frac yv=\frac{xv}{uy}$.

</li>

</ol>
:::

⁠**Cómo leerlo:** Solo (i) da sentido a las notaciones $-x$ y $x^{-1}$: si hubiera dos inversos, no se sabría cuál se quiere decir. (v) es la razón por la que se descompone una ecuación en factores y se iguala cada factor a cero. **Por qué $x\ne0$:** $0\cdot z=1$ no tiene solución por (iii), y $0\cdot z=0$ tiene como solución todo $z$. Dividir por cero falla por la existencia o por la unicidad.

:::beweis Reglas de cálculo, cada paso con su axioma
(i) De $xy=xz$ (ambos son 1) se sigue, multiplicando por $y$: $(xy)y=(xz)y$. A la izquierda queda $1\cdot y=y$ (M1, M3). A la derecha: $(xz)y\overset{\text{M2}}{=}x(zy)\overset{\text{M1}}{=}x(yz)\overset{\text{M2}}{=}(xy)z=1\cdot z=z$. Para la suma se procede igual (ejercicio [4](#aufg-4)).

(ii) Existencia: $x(yx^{-1})=x(x^{-1}y)=(xx^{-1})y=1\cdot y=y$ (M1, M2, M4, M3). Unicidad: de $xz=x\tilde z$ se sigue, multiplicando por $x^{-1}$ y con los mismos axiomas, $z=\tilde z$. Para la suma, igual con $-x$.

(iii) $x\cdot0\overset{\text{A3}}{=}(x\cdot0)+0\overset{\text{A4}}{=}(x\cdot0)+\bigl((x\cdot0)+(-(x\cdot0))\bigr)\overset{\text{A2}}{=}\bigl((x\cdot0)+(x\cdot0)\bigr)+(-(x\cdot0))\overset{\text{AM}}{=}x\cdot(0+0)+(-(x\cdot0))\overset{\text{A3}}{=}(x\cdot0)+(-(x\cdot0))\overset{\text{A4}}{=}0$. Para $x\ne0$ es $x^{-1}\ne0$ (indirectamente: de $x^{-1}=0$ se seguiría $1=xx^{-1}=x\cdot0=0$, en contra de NNE). Por tanto, $x^{-1}$ tiene un inverso. Es $(x^{-1})^{-1}x^{-1}=1$ y $x\,x^{-1}=1$; por (i), $x$ y $(x^{-1})^{-1}$ coinciden.

(iv) $x$ y $-(-x)$ son ambos inversos aditivos de $-x$, luego iguales por (i). Además, $x+(-1)x=(1+(-1))x=0\cdot x=0$, luego $(-1)x=-x$. De $(-1)+(-1)(-1)=(-1)(1+(-1))=(-1)\cdot0=0$ se sigue igualmente que $(-1)(-1)$ es inverso de $-1$, luego $(-1)(-1)=-(-1)=1$. Así, $(-x)(-y)=(-1)(-1)xy=xy$.

(v) Si $x\ne0$, entonces $y=x^{-1}(xy)=x^{-1}\cdot0=0$.

(vi) $\frac xu\cdot\frac yv=(xu^{-1})(yv^{-1})=(xy)(u^{-1}v^{-1})$, y $u^{-1}v^{-1}=(uv)^{-1}$, pues $(u^{-1}v^{-1})(uv)=1$ y el inverso es único. La regla de la división se sigue con $(y v^{-1})^{-1}=y^{-1}v$, la de la suma amplificando: $\frac xu=\frac{xv}{uv}$, $\frac yv=\frac{yu}{uv}$, y luego (AM).
:::

::::beispiel
$(-3)(-5)=15$, $\frac23+\frac57=\frac{14+15}{21}=\frac{29}{21}$, $\frac34:\frac58=\frac{3\cdot8}{4\cdot5}=\frac65$.
::::

⁠**Caso límite** $v=u=1$: La regla de la suma se convierte en $x+y=x+y$.

:::frage Eso ya lo sé de la escuela. ¿Para qué una demostración?
Para $\mathbb{Q}$ y $\mathbb{R}$ son conocidas. Pero no están en los axiomas, y solo la demostración muestra dónde valen: en todo cuerpo. La regla escolar «los cuadrados no son negativos», en cambio, no se sigue de esta lista y deja de valer en la [Parte 2](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Además, se practica el razonamiento con contenidos cuyo resultado se conoce.
:::

:::aufgabe Ejercicio 4 ★★ Demostrar en un cuerpo
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Demuestra: $(x+y=0\wedge x+z=0)\Rightarrow y=z$. Indica el axioma de cada paso.

</li>

<li>

Demuestra $(x+y)(x-y)=x^2-y^2$ e indica dónde se necesitan (AM) y (M1).

</li>

<li>

En el cuerpo $\{0,1\}$ con $1+1=0$ y $1\cdot1=1$: ¿qué es $-1$? Comprueba $(-1)(-1)=1$.

</li>

</ol>

:::loesung
(a) De $x+y=0=x+z$ se sigue $(-x)+(x+y)=(-x)+(x+z)$. Con (A2), (A1), (A4) esto se convierte en $0+y=0+z$, y con (A1), (A3) en $y=z$. (b) (AM) y (M1): $(x+y)(x-y)=(x+y)x+(x+y)(-y)=x^2+yx-xy-y^2=x^2-y^2$, donde $yx=xy$ por (M1) y $(x+y)(-y)=-(x+y)y$ por $(-1)x=-x$. (c) $1+1=0$ significa $-1=1$. Entonces $(-1)(-1)=1\cdot1=1$. Es la regla del teorema [3.2](#satz-3-2), que vale en todo cuerpo.
:::
:::
