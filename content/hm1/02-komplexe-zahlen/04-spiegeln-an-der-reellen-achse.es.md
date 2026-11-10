---
title: Etapa 3: Reflejar en el eje real
pfad: Ingeniería eléctrica / 1.er semestre / HöMa1 – Matemáticas superiores 1 / Números complejos
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Capítulo 2: Números complejos
order: 1220400
summary: Todavía no se puede dividir por x+iy .
tags: 
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Todavía no se puede dividir por $x+\mathrm{i}y$. Esta etapa introduce la imagen especular de $z$, que por multiplicación convierte cualquier número en uno real, y reúne las reglas de cálculo.
:::

**La idea.** También $-\mathrm{i}$ resuelve $x^2=-1$, porque $(-\mathrm{i})^2=\mathrm{i}^2=-1$. Las leyes del cálculo no pueden distinguir $\mathrm{i}$ de $-\mathrm{i}$. Por eso, un cálculo correcto sigue siendo correcto si se cambia $\mathrm{i}$ por $-\mathrm{i}$ en todas partes. En el plano, este cambio es la reflexión en el eje real (fig. [3](#abb-3)). Si se multiplica $z$ por su imagen especular, los términos cruzados con $\mathrm{i}$ se cancelan.

:::abbildung hm1/k2konjugiert 3
$z_1$ y su imagen especular $\overline{z_1}$. La suma está en el eje real porque las partes imaginarias se cancelan; la diferencia está en el eje imaginario porque las partes reales se cancelan.
:::

:::definition Definición 3.1 (Conjugado complejo)
<span class="anker" id="satz-3-1"></span>

Dado $z=x+\mathrm{i}y$, el número $\overline{z}:=x-\mathrm{i}y\in\mathbb{C}$ se llama conjugado de $z$.
:::

:::satz Teorema 3.2 (Reglas de cálculo en $\mathbb{C}$)
<span class="anker" id="satz-3-2"></span>

Para todos los $z=x+\mathrm{i}y$ y $w=u+\mathrm{i}v$ con $x,y,u,v$ reales se cumple:

<ol class="rm">

<li>

$\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)$,

</li>

<li>

$\operatorname{Im}(z+w)=\operatorname{Im}(z)+\operatorname{Im}(w)$,

</li>

<li>

$\overline{z+w}=\overline{z}+\overline{w}$,

</li>

<li>

$\overline{z\cdot w}=\overline{z}\cdot\overline{w}$,

</li>

<li>

$\overline{\overline{z}}=z$,

</li>

<li>

$z\overline{z}=x^2+y^2$, luego $\operatorname{Im}(z\overline{z})=0$ y $\operatorname{Re}(z\overline{z})=x^2+y^2$,

</li>

<li>

$z+\overline{z}=2\operatorname{Re}(z)$ y $z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$.

</li>

</ol>
:::

⁠**Cómo leerlo:** La parte real, la parte imaginaria y la conjugación se pueden aplicar término a término en las sumas. La conjugación también se puede aplicar factor a factor en los productos: eso es el cambio $\mathrm{i}\leftrightarrow-\mathrm{i}$. La parte real no: $\operatorname{Re}(z_1z_2)=1$, pero $\operatorname{Re}(z_1)\operatorname{Re}(z_2)=3$, porque en la parte real del producto entra también $-y_1y_2$. En electrotecnia se escribe a menudo $z^*$ en lugar de $\overline{z}$.

:::beweis Reglas de cálculo
(i), (ii): La suma se hace por separado, $z+w=(x+u)+\mathrm{i}(y+v)$.

(iii): $\overline{z+w}=(x+u)-\mathrm{i}(y+v)=(x-\mathrm{i}y)+(u-\mathrm{i}v)$.

(iv): Por [(1.3)](paare-statt-einzelner-zahlen.html#gl-1-3) es $zw=(xu-yv)+\mathrm{i}(xv+uy)$, luego $\overline{zw}=(xu-yv)-\mathrm{i}(xv+uy)$. La misma fórmula con $-y$ y $-v$ da $\overline{z}\,\overline{w}=(xu-yv)+\mathrm{i}(-xv-uy)$. Ambos coinciden.

(v): Cambiar dos veces el signo de $y$.

(vi): $(x+\mathrm{i}y)(x-\mathrm{i}y)=x^2-\mathrm{i}xy+\mathrm{i}xy-\mathrm{i}^2y^2=x^2+y^2$.

(vii): $(x+\mathrm{i}y)+(x-\mathrm{i}y)=2x$ y $(x+\mathrm{i}y)-(x-\mathrm{i}y)=2\mathrm{i}y$.
:::

::::beispiel
Para $z_1$ es $\overline{z_1}=3-\mathrm{i}$, $z_1\overline{z_1}=9+1=10$, $z_1+\overline{z_1}=6=2\cdot3$ y $z_1-\overline{z_1}=2\mathrm{i}=2\mathrm{i}\cdot1$. Comprobación de (iv): $\overline{z_1z_2}=1-7\mathrm{i}$ y $\overline{z_1}\,\overline{z_2}=(3-\mathrm{i})(1-2\mathrm{i})=3-6\mathrm{i}-\mathrm{i}+2\mathrm{i}^2=1-7\mathrm{i}$.
::::

⁠**Caso límite:** Para $y=0$ es $\overline{z}=z$ y $z\overline{z}=x^2$. Los números reales están en el eje de reflexión y no cambian.

:::frage ¿No es $z\overline{z}$ lo mismo que $z^2$?
Solo para $z$ real. En $z^2$ los términos cruzados se suman y dan $2\mathrm{i}xy$; en $z\overline{z}$ se cancelan. En el modelo de referencia es $z_2^2=-3+4\mathrm{i}$, pero $z_2\overline{z_2}=5$.
:::

:::aufgabe Ejercicio 3 ★ ¿Real o imaginario puro?
<span class="anker" id="aufg-3"></span>

Sea $z=2-5\mathrm{i}$. (a) Predice sin calcular cuáles de los números $z+\overline{z}$, $z-\overline{z}$, $z\overline{z}$, $z^2+\overline{z}^2$, $(z-\overline{z})^2$ son reales y cuáles imaginarios puros. Después compruébalo calculando. (b) Demuestra para todo $z\in\mathbb{C}$: $z$ es real si y solo si $\overline{z}=z$, e imaginario puro si y solo si $\overline{z}=-z$.

:::loesung
(a) Predicción: $z+\overline{z}$ es real, $z-\overline{z}$ imaginario puro, $z\overline{z}$ real, $z^2+\overline{z}^2=z^2+\overline{z^2}$ real (suma de un número y su imagen especular), $(z-\overline{z})^2$ real (cuadrado de un imaginario puro). Cálculo: $z+\overline{z}=4$, $z-\overline{z}=-10\mathrm{i}$, $z\overline{z}=4+25=29$. Con $z^2=4-20\mathrm{i}+25\mathrm{i}^2=-21-20\mathrm{i}$ resulta $z^2+\overline{z}^2=-42$, y $(z-\overline{z})^2=(-10\mathrm{i})^2=-100$.

(b) Por la regla (vii) de la etapa [3](#stufe-3), $\overline{z}=z$ equivale a $2\mathrm{i}\operatorname{Im}(z)=0$, es decir, a $\operatorname{Im}(z)=0$. Del mismo modo, $\overline{z}=-z$ equivale a $2\operatorname{Re}(z)=0$, es decir, a $\operatorname{Re}(z)=0$.
:::
:::
