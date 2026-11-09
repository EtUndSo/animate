---
title: Etapa 5: Valor absoluto y distancia
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Números complejos
order: 1220600
summary: Los números complejos no se pueden ordenar, pero sí medir.
tags: distancia, desigualdad triangular inversa
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Los números complejos no se pueden ordenar, pero sí medir. Esta etapa traslada al plano la distancia y el valor absoluto de la [Parte 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) y muestra qué reglas se conservan.
:::

**La idea.** En $\mathbb{R}$, $|x|$ mide la distancia al origen. En el plano se encarga de ello el teorema de Pitágoras: el segmento de 0 a $z$ es la hipotenusa de un triángulo rectángulo con los catetos $|x|$ e $|y|$ (fig. [5](#abb-5), izquierda). La distancia entre dos puntos es la hipotenusa sobre las diferencias de sus coordenadas. El resultado es real, y aquí «mayor que» vuelve a estar permitido.

:::abbildung hm1/k2betrag 5
A la izquierda, valor absoluto y distancia como hipotenusas: $|z_1|^2=3^2+1^2$ y $d(z_1,z_2)^2=2^2+1^2$. A la derecha, la desigualdad triangular: el camino por $z_1$ es más largo que el camino directo a $z_1+z_2$.
:::

:::definition Definición 5.1 (Distancia y valor absoluto)
<span class="anker" id="satz-5-1"></span>

Para $z=x+\mathrm{i}y$ y $w=u+\mathrm{i}v$ con $x,y,u,v$ reales, sea

<span class="anker" id="gl-5-1"></span>
$$d(z,w):=\sqrt{(x-u)^2+(y-v)^2},\qquad |z|:=d(z,0)=\sqrt{x^2+y^2}. \tag{5.1}$$
:::

⁠**Cómo leerlo:** Bajo la raíz hay un número real mayor o igual que cero, y $\sqrt a$ es la solución no negativa de $b^2=a$ ([Parte 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). La __distancia__ $d(z,w)$ solo depende de la diferencia: $d(z,w)=|z-w|$. **Caso límite:** Para $z$ real es $|z|=\sqrt{x^2}=|x|$, el valor absoluto de la [Parte 1](/wissen/es/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html).

:::satz Teorema 5.2 (Reglas de cálculo para valor absoluto y distancia)
<span class="anker" id="satz-5-2"></span>

Para todos los $z,w,\tilde z\in\mathbb{C}$ se cumple:

<ol class="rm">

<li>

$|z|\ge0$ y ($|z|=0\Leftrightarrow z=0$), e igualmente $d(z,w)\ge0$ y ($d(z,w)=0\Leftrightarrow z=w$),

</li>

<li>

$d(z,w)=d(w,z)$ y $|\overline{z}|=|{-z}|=|z|$,

</li>

<li>

$z\overline{z}=|z|^2$, luego para $z\ne0$ es $1/z=\overline{z}\cdot1/|z|^2$,

</li>

<li>

$|z\cdot w|=|z|\cdot|w|$,

</li>

<li>

$\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$,

</li>

<li>

$|z+w|\le|z|+|w|$ y $d(z,w)\le d(z,\tilde z)+d(\tilde z,w)$ (desigualdad triangular),

</li>

<li>

$|z-w|\le|z|+|w|$, $\bigl||z|-|w|\bigr|\le|z-w|$ y $\bigl||z|-|w|\bigr|\le|z+w|$ (__desigualdad triangular inversa__).

</li>

</ol>
:::

⁠**Cómo leerlo:** (iv): El valor absoluto de un producto es el producto de los valores absolutos. (v): La hipotenusa mide como mucho lo que los dos catetos juntos, y cada cateto mide como mucho lo que ella. (vi): Un rodeo por $\tilde z$ nunca es más corto. **Validez:** Las reglas valen sin restricciones, pero $|z+w|=|z|+|w|$ no es una regla: la igualdad se da cuando las flechas apuntan en la misma dirección, como con $z_2$ y $2z_2$: $3\sqrt5=\sqrt5+2\sqrt5$.

:::beweis Reglas de cálculo para el valor absoluto
(i), (ii): Una suma de cuadrados es cero si y solo si los dos cuadrados son cero, y los cambios de signo no la alteran.

(iii): Etapa [3](spiegeln-an-der-reellen-achse.html#stufe-3), regla (vi), y [(4.1)](dividieren-und-was-verloren-geht.html#gl-4-1).

(iv): $|zw|^2=zw\,\overline{zw}=z\overline{z}\,w\overline{w}=|z|^2|w|^2$ por (iii) y $\overline{zw}=\overline{z}\,\overline{w}$. Los dos valores absolutos son no negativos, así que se puede extraer la raíz.

(v): $x^2\le x^2+y^2$ e $y^2\le x^2+y^2$ dan la desigualdad de la izquierda, $x^2+y^2\le x^2+2|x||y|+y^2=(|x|+|y|)^2$ la de la derecha.

(vi): Con (iii) y las reglas de conjugación es

$$|z+w|^2=(z+w)(\overline{z}+\overline{w})=|z|^2+z\overline{w}+\overline{z}w+|w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2,$$

porque $\overline{z}w$ es el conjugado de $z\overline{w}$. Por (v) y (iv) es $\operatorname{Re}(z\overline{w})\le|z\overline{w}|=|z||w|$. Por tanto $|z+w|^2\le(|z|+|w|)^2$. La forma con distancias se deduce de $z-w=(z-\tilde z)+(\tilde z-w)$.

(vii): $-w$ en lugar de $w$ en (vi) da la primera desigualdad. De $|z|=|(z-w)+w|\le|z-w|+|w|$ se deduce $|z|-|w|\le|z-w|$; con los papeles intercambiados, $|w|-|z|\le|z-w|$; juntas dan la segunda. $-w$ en lugar de $w$ en ella da la tercera.
:::

::::beispiel
$|z_1|=\sqrt{10}\approx3{,}162$ y $|z_2|=\sqrt5\approx2{,}236$. La desigualdad triangular: $|z_1+z_2|=|4+3\mathrm{i}|=5\le5{,}398$. El producto: $|z_1z_2|=|1+7\mathrm{i}|=\sqrt{50}=\sqrt{10}\cdot\sqrt5$. La distancia: $d(z_1,z_2)=|2-\mathrm{i}|=\sqrt5$. La desigualdad inversa: $0{,}926\le2{,}236$. Regla (v) para $z_1$: $3\le3{,}162\le4$.
::::

**Conjuntos de puntos.** Como $|z-c|$ es la distancia de $z$ a $c$, $|z-c|=r$ describe la circunferencia de centro $c$ y radio $r$, y $|z-c|\le r$ el disco. Las condiciones sobre $\operatorname{Re}(z)$ o $\operatorname{Im}(z)$ recortan semiplanos. Estas desigualdades están permitidas porque ambos miembros son reales.

:::frage ¿Por qué bajo la raíz está $x^2+y^2$ y no $z^2$?
Para $z$ real es $|z|=\sqrt{z^2}$, y eso induce a error. En $\mathbb{C}$, $z^2$ en general no es real y puede ser negativo, por ejemplo $(2\mathrm{i})^2=-4$. El valor absoluto debe ser una longitud, y Pitágoras suma cuadrados de longitudes reales. Lo correcto es $|z|=\sqrt{z\overline{z}}$.
:::

:::aufgabe Ejercicio 6 ★★ Conjuntos de puntos
<span class="anker" id="aufg-6"></span>

Dibuja en el plano complejo: (a) $\{z:|z-1-\mathrm{i}|\le2\}$, (b) $\{z:|z-2|=|z+2\mathrm{i}|\}$, (c) $\{z:\operatorname{Re}((1+\mathrm{i})z)>1\}$. Pista para (b): eleva ambos miembros al cuadrado y sustituye $z=x+\mathrm{i}y$.

:::loesung
(a) $|z-(1+\mathrm{i})|\le2$ es el disco de centro $1+\mathrm{i}$ y radio 2, incluido el borde.

(b) $(x-2)^2+y^2=x^2+(y+2)^2$ da $-4x+4=4y+4$, es decir, $y=-x$. Es la recta que pasa por el origen con pendiente $-1$. Geométricamente son todos los puntos que equidistan de $2$ y de $-2\mathrm{i}$: la mediatriz del segmento que los une.

(c) $(1+\mathrm{i})(x+\mathrm{i}y)=(x-y)+\mathrm{i}(x+y)$. La condición es $x-y>1$, es decir, $y<x-1$. Es el semiplano situado debajo de la recta $y=x-1$, sin la recta.
:::
:::

:::aufgabe Ejercicio 7 ★★★ Paralelogramo y circunferencia unidad
<span class="anker" id="aufg-7"></span>

(a) Demuestra $|z+w|^2+|z-w|^2=2|z|^2+2|w|^2$ y comprueba la ecuación con $z_1$ y $z_2$. ¿Qué dice sobre las diagonales del paralelogramo? (b) Demuestra: de $|z|=1$ se deduce $1/z=\overline{z}$. Compruébalo con $z=0{,}6+0{,}8\mathrm{i}$. (c) Predice dónde está $1/(2z)$ para este $z$ y calcúlalo.

:::loesung
(a) Como en la demostración de la desigualdad triangular, $|z\pm w|^2=|z|^2\pm2\operatorname{Re}(z\overline{w})+|w|^2$. Al sumar desaparecen los términos cruzados. Comprobación: $25+5=30=2\cdot10+2\cdot5$. Los cuadrados de las dos diagonales de un paralelogramo suman juntos los cuadrados de los cuatro lados.

(b) De $z\overline{z}=|z|^2=1$ se deduce $1/z=\overline{z}$. Para $z=0{,}6+0{,}8\mathrm{i}$ es $|z|^2=0{,}36+0{,}64=1$ y $(0{,}6+0{,}8\mathrm{i})(0{,}6-0{,}8\mathrm{i})=0{,}36+0{,}64=1$.

(c) Predicción: reflejar y dividir por $|2z|^2=4$, así que el inverso está en la flecha de $\overline{z}$, con valor absoluto $0{,}5$. Cálculo: $1/(2z)=\overline{z}/2=0{,}3-0{,}4\mathrm{i}$.
:::
:::
