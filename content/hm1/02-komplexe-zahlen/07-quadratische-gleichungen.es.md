---
title: Etapa 6: Ecuaciones cuadráticas
pfad: Ingeniería eléctrica / 1.er semestre / HöMa1 – Matemáticas superiores 1 / Números complejos
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Capítulo 2: Números complejos
order: 1220700
summary: El objetivo era una solución de x 2=-1 .
tags: solución doble, discriminante, representación polar
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
El objetivo era una solución de $x^2=-1$. Esta etapa muestra que $\mathbb{C}$ da más de sí: allí toda ecuación cuadrática tiene solución, incluso con coeficientes complejos.
:::

**La idea.** Completar el cuadrado solo usa axiomas de cuerpo y por eso vale en $\mathbb{C}$. Queda una ecuación $w^2=D$. En $\mathbb{R}$ falla para $D<0$. En $\mathbb{C}$ no falla nunca: $w^2=D$ se descompone en parte real y parte imaginaria, es decir, en dos ecuaciones reales para las dos incógnitas reales de $w$.

:::satz Teorema 6.1 (Raíces cuadradas en $\mathbb{C}$)
<span class="anker" id="satz-6-1"></span>

Sea $D=s+\mathrm{i}t\ne0$ con $s,t\in\mathbb{R}$. Para $w=u+\mathrm{i}v$ con $u,v$ reales, $w^2=D$ equivale a $u^2-v^2=s$ y $2uv=t$. Hay exactamente dos soluciones $\pm w$, a saber, con

<span class="anker" id="gl-6-1"></span>
$$u^2=\frac{|D|+s}2,\qquad v^2=\frac{|D|-s}2. \tag{6.1}$$

Los signos de $u$ y $v$ deben elegirse de modo que se cumpla $2uv=t$. Para $D=0$, $w=0$ es la única solución.
:::

⁠**Cómo leerlo:** $s$ y $t$ son la parte real y la parte imaginaria de $D$. Si $t>0$, $u$ y $v$ tienen el mismo signo; si $t<0$, signos distintos. **Caso límite:** Para $D<0$ real resulta $u=0$ y $v^2=-D$: las soluciones son imaginarias puras, y para $D=-1$ son $w=\pm\mathrm{i}$.

:::beweis Dos ecuaciones reales
Es $w^2=u^2-v^2+2\mathrm{i}uv$. Comparar parte real y parte imaginaria da las dos ecuaciones. De $|w|^2=|w^2|=|D|$ se deduce además $u^2+v^2=|D|$. Sumar y restar con $u^2-v^2=s$ da [(6.1)](#gl-6-1). Los segundos miembros son no negativos, porque $|s|\le|D|$ (etapa [5](betrag-und-abstand.html#stufe-5), regla (v)). Recíprocamente, $u,v$ de [(6.1)](#gl-6-1) cumplen la ecuación $u^2-v^2=s$ y $(2uv)^2=(|D|+s)(|D|-s)=|D|^2-s^2=t^2$. Por tanto $2uv=\pm t$, y la elección de los signos fija $2uv=t$.
:::

:::satz Teorema 6.2 (Ecuación cuadrática en $\mathbb{C}$)
<span class="anker" id="satz-6-2"></span>

Sean $p,q\in\mathbb{C}$ y $D:=p^2/4-q$. La ecuación $z^2+pz+q=0$ tiene las soluciones

<span class="anker" id="gl-6-2"></span>
$$z=-\frac p2\pm w\qquad\text{con}\qquad w^2=D. \tag{6.2}$$

Para $D\ne0$ son dos soluciones $z_+\ne z_-$ con $z_++z_-=-p$ y $z_+z_-=q$. Para $D=0$ solo existe $z=-p/2$, una __solución doble__. Para $p,q$ reales: $D>0$ da dos soluciones reales, $D=0$ una real, $D<0$ las soluciones conjugadas entre sí $z=-\frac p2\pm\mathrm{i}\sqrt{-D}$.
:::

⁠**Cómo leerlo:** $D$ se llama __discriminante__. Las soluciones son simétricas respecto del centro $-p/2$ (fig. [6](#abb-6)). **Validez:** El coeficiente de $z^2$ tiene que ser 1. Si no, se divide antes por él; en $\mathbb{C}$ esto funciona también con un coeficiente complejo $\ne0$. Las ecuaciones reales de este tipo describen oscilaciones: un par de soluciones conjugadas corresponde a una oscilación amortiguada.

:::herleitung Completar el cuadrado
Se cumple $z^2+pz+q=(z+\frac p2)^2-\frac{p^2}4+q=(z+\frac p2)^2-w^2=(z+\frac p2-w)(z+\frac p2+w)$. Un producto solo es cero si lo es uno de sus factores (etapa [4](dividieren-und-was-verloren-geht.html#stufe-4)). Eso da [(6.2)](#gl-6-2), y se deduce $z_++z_-=-p$ y $z_+z_-=\frac{p^2}4-w^2=q$. Para $p,q$ reales, $D$ es real, y para $D<0$ es $w=\pm\mathrm{i}\sqrt{-D}$.
:::

:::abbildung hm1/k2loesungen 6
A la izquierda, la ecuación real del modelo de referencia: las soluciones $3\pm\mathrm{i}$ son imágenes especulares. A la derecha, la ecuación compleja: $z_1$ y $z_2$ son simétricos respecto del centro $2+1{,}5\mathrm{i}$.
:::

::::beispiel [Ejemplo 1] coeficientes reales
$z^2-6z+10=0$ tiene $p=-6$, $q=10$, $D=9-10=-1$, luego $z=3\pm\mathrm{i}$. Son $z_1$ y $\overline{z_1}$. Comprobación: suma $6=-p$, producto $|z_1|^2=10=q$.
::::

::::beispiel [Ejemplo 2] coeficientes complejos
Para $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$ es $-p/2=2+1{,}5\mathrm{i}$ y

$$D=(2+1{,}5\mathrm{i})^2-(1+7\mathrm{i})=1{,}75+6\mathrm{i}-1-7\mathrm{i}=0{,}75-\mathrm{i}.$$

Así, $s=0{,}75$, $t=-1$ y $|D|=\sqrt{0{,}5625+1}=1{,}25$. De [(6.1)](#gl-6-1) se deduce $u^2=1$ y $v^2=0{,}25$. Como $t<0$, $u$ y $v$ tienen signos distintos: $w=\pm(1-0{,}5\mathrm{i})$. Con ello $z=2+1{,}5\mathrm{i}\pm(1-0{,}5\mathrm{i})$, es decir, $z=3+\mathrm{i}$ o $z=1+2\mathrm{i}$. Comprobación: suma $4+3\mathrm{i}=-p$, producto $1+7\mathrm{i}=q$.
::::

⁠**Caso límite:** Para $q=0$, [(6.2)](#gl-6-2) da $z=-p/2\pm p/2$, es decir, $z=0$ y $z=-p$, en consonancia con $z(z+p)=0$.

:::frage ¿Por qué no se puede calcular $\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}=1$?
La regla $\sqrt{ab}=\sqrt a\sqrt b$ del [capítulo 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) solo vale para $a,b\ge0$. Para números negativos la raíz no está definida: $w^2=-1$ tiene dos soluciones equivalentes, y ninguna de ellas es «la» raíz. Por eso este capítulo escribe $w^2=D$ y no $w=\sqrt D$.
:::

:::aufgabe Ejercicio 8 ★★ Resolver ecuaciones cuadráticas
<span class="anker" id="aufg-8"></span>

(a) Resuelve $z^2+4z+13=0$ y comprueba la suma y el producto. (b) $z^2+pz+q=0$ con $p,q$ reales tiene la solución $2-5\mathrm{i}$. ¿Cuál es la segunda solución y cuánto valen $p$ y $q$? (c) Resuelve $z^2-3z+3-\mathrm{i}=0$ y comprueba el resultado. (d) Resuelve $\mathrm{i}z^2+2z-2\mathrm{i}=0$.

:::loesung
(a) $D=4-13=-9$, así que $z=-2\pm3\mathrm{i}$. Suma $-4=-p$, producto $4+9=13=q$. (b) Con coeficientes reales, la segunda solución es la conjugada, $2+5\mathrm{i}$. Entonces $p=-(2-5\mathrm{i})-(2+5\mathrm{i})=-4$ y $q=(2-5\mathrm{i})(2+5\mathrm{i})=29$.

(c) $p=-3$, $q=3-\mathrm{i}$, así que $D=2{,}25-3+\mathrm{i}=-0{,}75+\mathrm{i}$. Con $|D|=\sqrt{0{,}5625+1}=1{,}25$, [(6.1)](#gl-6-1) da $u^2=0{,}25$ y $v^2=1$. Como $t=1>0$, $u$ y $v$ tienen el mismo signo: $w=\pm(0{,}5+\mathrm{i})$. Por tanto $z=1{,}5\pm(0{,}5+\mathrm{i})$, es decir, $z=2+\mathrm{i}$ o $z=1-\mathrm{i}$. Comprobación: suma $3=-p$, producto $(2+\mathrm{i})(1-\mathrm{i})=2-2\mathrm{i}+\mathrm{i}-\mathrm{i}^2=3-\mathrm{i}=q$.

(d) Primero se lleva a 1 el coeficiente de $z^2$: dividir por $\mathrm{i}$ con $1/\mathrm{i}=-\mathrm{i}$ da $z^2-2\mathrm{i}z-2=0$. Así, $p=-2\mathrm{i}$, $q=-2$ y $D=(-2\mathrm{i})^2/4+2=-1+2=1$. Con $w=\pm1$ se obtiene $z=\mathrm{i}\pm1$. Comprobación para $z=1+\mathrm{i}$: $\mathrm{i}\cdot2\mathrm{i}+2+2\mathrm{i}-2\mathrm{i}=-2+2=0$. Comprobación para $z=-1+\mathrm{i}$: $\mathrm{i}\cdot(-2\mathrm{i})-2+2\mathrm{i}-2\mathrm{i}=2-2=0$.
:::
:::

**Perspectiva.** Un punto del plano también se puede indicar mediante valor absoluto y ángulo. Entonces, al multiplicar, se multiplican los valores absolutos y se suman los ángulos; el giro de la etapa [2](die-komplexe-ebene.html#stufe-2) es el caso particular $|\mathrm{i}|=1$ y ángulo $90^\circ$. Esta __representación polar__, la forma exponencial y las raíces $n$-ésimas necesitan el seno, el coseno y la función exponencial, y por eso llegan en el capítulo 7.
