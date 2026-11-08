---
title: Matriz identidad e inversa
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
knoten: Fundamentos 1: Vectores y matrices
nachschlagen: ja
order: 15211200
summary: Algunas aplicaciones lineales pueden deshacerse; otras, no.
tags: matriz identidad, invertible, inversa, singular
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
Algunas aplicaciones lineales pueden deshacerse; otras, no. Esta sección introduce la matriz que no cambia nada y la matriz inversa, que invierte una aplicación, y aclara cuándo existe.
:::

### La matriz identidad

<span class="anker" id="stufe-11-1"></span>

Entre todas las aplicaciones lineales hay una que no hace nada en absoluto: lleva cada vector a sí mismo. Sus columnas son, según [(8.2)](lineare-abbildungen.html#gl-8-2), las imágenes de los vectores unitarios, es decir, los propios vectores unitarios.

:::definition Definición 11.1 (Matriz identidad)
<span class="anker" id="satz-11-1"></span>

La __matriz identidad__ $\mathbf{I}_n\in\mathbb{R}^{n\times n}$ es la matriz diagonal con solo unos en la diagonal. Sus columnas son $\mathbf{e}_1,\dots,\mathbf{e}_n$.
:::

Si el tamaño está claro, se escribe abreviadamente $\mathbf{I}$. Para todo vector $\mathbf{x}\in\mathbb{R}^n$, $\mathbf{I}\mathbf{x}=\mathbf{x}$, y para toda matriz $\mathbf{A}\in\mathbb{R}^{m\times n}$, $\mathbf{A}\mathbf{I}_n=\mathbf{A}$ y también $\mathbf{I}_m\mathbf{A}=\mathbf{A}$. La matriz identidad desempeña en el producto de matrices el papel del número $1$.

⁠**Ejemplo numérico:**

$$\mathbf{I}_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad \mathbf{I}_3\begin{pmatrix}60\\2\\3\end{pmatrix}=\begin{pmatrix}60\\2\\3\end{pmatrix}.$$

⁠**En resumen:** La matriz identidad tiene unos en la diagonal y ceros en el resto; como aplicación, deja cada vector sin cambios.

### La matriz inversa

<span class="anker" id="stufe-11-2"></span>

Una rotación de $90^\circ$ se deshace girando $90^\circ$ hacia atrás. Un estiramiento al doble se deshace comprimiendo a la mitad. En ambos casos existe una segunda aplicación que anula la primera: aplicadas una tras otra, las dos juntas no hacen nada.

:::definition Definición 11.2 (Matriz inversa)
<span class="anker" id="satz-11-2"></span>

Una matriz cuadrada $\mathbf{A}\in\mathbb{R}^{n\times n}$ se llama __invertible__ si existe una matriz $\mathbf{A}^{-1}\in\mathbb{R}^{n\times n}$ con

<span class="anker" id="gl-11-1"></span>
$$\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I} . \tag{11.1}$$

La matriz $\mathbf{A}^{-1}$ se llama la __inversa__ de $\mathbf{A}$.
:::

Existe como mucho una matriz así. En efecto, si $\mathbf{B}$ y $\mathbf{C}$ son ambas inversas de $\mathbf{A}$, entonces $\mathbf{B}=\mathbf{B}\mathbf{I}=\mathbf{B}(\mathbf{A}\mathbf{C})=(\mathbf{B}\mathbf{A})\mathbf{C}=\mathbf{I}\mathbf{C}=\mathbf{C}$. Por eso se puede hablar de *la* inversa. Si se conoce, cualquier resultado $\mathbf{y}=\mathbf{A}\mathbf{x}$ puede recalcularse hacia atrás: $\mathbf{A}^{-1}\mathbf{y}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{x}$.

⁠**Ejemplo numérico:**

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$

y lo mismo en el otro orden, así que $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. El estiramiento tiene la inversa $\operatorname{diag}(2;\,0{,}5)^{-1}=\operatorname{diag}(0{,}5;\,2)$; la rotación de $90^\circ$, la rotación de $-90^\circ$, $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$.

⁠**En resumen:** La inversa $\mathbf{A}^{-1}$ deshace la aplicación $\mathbf{A}$: $\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.

:::hintergrund La inversa de una matriz diagonal
Una matriz diagonal $\operatorname{diag}(\mathbf{v})$ multiplica cada componente por su propio factor $v_j$. Esto se deshace dividiendo cada componente por su factor: $\operatorname{diag}(\mathbf{v})^{-1}=\operatorname{diag}(1/v_1,\dots,1/v_n)$. Es posible si y solo si ningún factor es cero. Un factor $v_j=0$ borra la componente $j$, y lo que se ha borrado no puede recuperarlo ningún cálculo.
:::

### La inversa de una matriz $2\times2$

<span class="anker" id="stufe-11-3"></span>

Para las matrices $2\times2$ hay una fórmula sencilla. Se intercambian las dos entradas de la diagonal, se pone un signo menos delante de las otras dos y se divide por un número que se forma a partir de las cuatro entradas.

:::satz Teorema 11.3 (Inversa de una matriz $2\times2$)
<span class="anker" id="satz-11-3"></span>

La matriz $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ es invertible si y solo si $ad-bc\ne0$, y entonces

<span class="anker" id="gl-11-2"></span>
$$\mathbf{A}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}. \tag{11.2}$$
:::

:::herleitung Inversa de una matriz $2\times2$
Multiplicando se obtiene

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}=(ad-bc)\,\mathbf{I} ,$$

y lo mismo en el otro orden. Si $ad-bc\ne0$, se divide por este número y se obtiene [(11.1)](#gl-11-1). Si $ad-bc=0$, $\mathbf{A}$ lleva el vector $(d,\,-c)^{\top}$ a $(ad-bc,\ cd-dc)^{\top}=\mathbf{0}$, e igualmente $(b,\,-a)^{\top}$ a $\mathbf{0}$. Al menos uno de los dos no es el vector nulo, salvo que las cuatro entradas sean cero, y entonces $\mathbf{A}$ es de todos modos la matriz nula. Pero una matriz que lleva un vector $\mathbf{x}\ne\mathbf{0}$ a $\mathbf{0}$ no tiene inversa: si la tuviera, sería $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$.
:::

⁠**Ejemplo numérico:** Para $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$, $ad-bc=2-1=1$, así que la inversa es $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$, como antes. Para $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, $ad-bc=5$, y la inversa es $\tfrac15\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$.

⁠**En resumen:** Una matriz $2\times2$ es invertible si y solo si $ad-bc\ne0$; la inversa es $\frac{1}{ad-bc}\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$.

### Reglas de cálculo para inversas

<span class="anker" id="stufe-11-4"></span>

Quien ejecuta dos aplicaciones una tras otra y quiere deshacer el resultado tiene que anular primero la segunda. Por eso, al invertir un producto, el orden se invierte.

:::satz Teorema 11.4 (Reglas de cálculo para inversas)
<span class="anker" id="satz-11-4"></span>

Si $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ son invertibles y $c\ne0$, también $\mathbf{A}\mathbf{B}$, $\mathbf{A}^{\top}$, $\mathbf{A}^{-1}$ y $c\,\mathbf{A}$ son invertibles, y se cumple

$$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\qquad(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top},\qquad(\mathbf{A}^{-1})^{-1}=\mathbf{A},\qquad(c\,\mathbf{A})^{-1}=\tfrac1c\,\mathbf{A}^{-1}.$$
:::

:::herleitung Reglas de cálculo para inversas
En cada caso se comprueba que el producto con el candidato da la matriz identidad. Para el producto: $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})=\mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$, e igualmente $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{I}$. Para la traspuesta: $\mathbf{A}^{\top}(\mathbf{A}^{-1})^{\top}=(\mathbf{A}^{-1}\mathbf{A})^{\top}=\mathbf{I}^{\top}=\mathbf{I}$, y lo mismo en el otro orden. Las dos últimas reglas se siguen directamente de [(11.1)](#gl-11-1).
:::

Una regla que sería cómoda no se cumple: $(\mathbf{A}+\mathbf{B})^{-1}$ no es, en general, $\mathbf{A}^{-1}+\mathbf{B}^{-1}$. Ya con números, $\frac{1}{2+4}=\frac16$, pero $\frac12+\frac14=\frac34$.

⁠**Ejemplo numérico:** Para $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ y $\mathbf{B}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$, con $ad-bc=21-16=5$, así que $(\mathbf{A}\mathbf{B})^{-1}=\tfrac15\bigl(\begin{smallmatrix}3&-4\\-4&7\end{smallmatrix}\bigr)$. Lo mismo da

$$\mathbf{B}^{-1}\mathbf{A}^{-1}=\tfrac15\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\tfrac15\begin{pmatrix}3&-4\\-4&7\end{pmatrix}.$$

⁠**En resumen:** La inversa de un producto es el producto de las inversas en orden inverso, $(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$.

:::hintergrund Una imagen para el orden inverso
Quien por la mañana se pone primero un jersey y luego una chaqueta, por la noche se quita primero la chaqueta y luego el jersey. Deshacer recorre los pasos hacia atrás. La aplicación $\mathbf{A}\mathbf{B}$ es «primero $\mathbf{B}$, después $\mathbf{A}$»; para anularla hay que anular primero $\mathbf{A}$ y después $\mathbf{B}$, es decir, aplicar primero $\mathbf{A}^{-1}$ y después $\mathbf{B}^{-1}$. Escrito como matriz, con el paso ejecutado primero a la derecha, eso es $\mathbf{B}^{-1}\mathbf{A}^{-1}$. La imagen solo sirve en lo que se refiere al orden; no explica por qué existe una inversa.
:::

### Cuándo no hay inversa

<span class="anker" id="stufe-11-5"></span>

La matriz $\operatorname{diag}(1;\,0)$ aplasta el plano sobre el eje $x_1$ (fig. [32](lineare-abbildungen.html#abb-32)). Los puntos $(1,\,5)^{\top}$ y $(1,\,-2)^{\top}$ van a parar ambos a $(1,\,0)^{\top}$. Quien solo ve el resultado $(1,\,0)^{\top}$ no puede saber de qué punto procede. La segunda componente se ha perdido, y ningún cálculo la recupera.

:::satz Teorema 11.5 (Sin inversa)
<span class="anker" id="satz-11-5"></span>

Si existe un vector $\mathbf{x}\ne\mathbf{0}$ con $\mathbf{A}\mathbf{x}=\mathbf{0}$, $\mathbf{A}$ no es invertible.
:::

:::beweis Sin inversa
Si hubiera una inversa, sería $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$, en contradicción con $\mathbf{x}\ne\mathbf{0}$.
:::

Intuitivamente: con $\mathbf{A}\mathbf{x}=\mathbf{0}$, para todo $\mathbf{u}$ los dos vectores distintos $\mathbf{u}$ y $\mathbf{u}+\mathbf{x}$ van a parar al mismo lugar, pues $\mathbf{A}(\mathbf{u}+\mathbf{x})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{x}=\mathbf{A}\mathbf{u}$. Dos entradas con la misma salida no pueden distinguirse. Una matriz cuadrada que no es invertible se llama __singular__.

⁠**Ejemplo numérico:** Para $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, $ad-bc=4-4=0$. En efecto, $\mathbf{x}=(2,\,-1)^{\top}$ se lleva a $(2-2,\ 4-4)^{\top}=\mathbf{0}$, y los vectores distintos $(1,\,1)^{\top}$ y $(3,\,0)^{\top}$ van a parar ambos a $(3,\,6)^{\top}$.

Para los datos, esto significa: un cálculo que, por ejemplo, a partir del número de dormitorios y del de salones solo forma el número total de habitaciones ya no puede separar los dos números. En las matrices $2\times2$, este es exactamente el caso $ad-bc=0$ de la subsección [11.3](#stufe-11-3).

⁠**En resumen:** Si una matriz lleva un vector $\mathbf{x}\ne\mathbf{0}$ a $\mathbf{0}$, pierde información y no tiene inversa; se llama entonces singular.

:::aufgabe Ejercicio 26 ★ Calcular inversas
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Calcula las inversas de $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ y $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ y haz en cada caso la comprobación.

</li>

<li>

¿Para qué número $t$ no es invertible $\bigl(\begin{smallmatrix}2&t\\4&6\end{smallmatrix}\bigr)$? Indica para ese caso un vector $\mathbf{x}\ne\mathbf{0}$ con $\mathbf{A}\mathbf{x}=\mathbf{0}$.

</li>

<li>

Indica la inversa de $\operatorname{diag}(4;\,-1;\,0{,}5)$.

</li>

</ol>

:::loesung
(a) Para $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ se tiene $ad-bc=4-3=1$, y la inversa es $\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)$. Comprobación: $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4-3&-12+12\\1-1&-3+4\end{smallmatrix}\bigr)=\mathbf{I}$. Para $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ se tiene $ad-bc=4-6=-2$, y la inversa es $-\tfrac12\bigl(\begin{smallmatrix}4&-2\\-3&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$. Comprobación: $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2+3&1-1\\-6+6&3-2\end{smallmatrix}\bigr)=\mathbf{I}$.

(b) $ad-bc=12-4t=0$ para $t=3$. Entonces la matriz es $\bigl(\begin{smallmatrix}2&3\\4&6\end{smallmatrix}\bigr)$; su segunda fila es el doble de la primera. El vector $(3,\,-2)^{\top}$ va a parar a $(6-6,\ 12-12)^{\top}=\mathbf{0}$.

(c) $\operatorname{diag}(4;\,-1;\,0{,}5)^{-1}=\operatorname{diag}(0{,}25;\,-1;\,2)$: cada entrada diagonal se sustituye por su inverso.
:::
:::

:::aufgabe Ejercicio 27 ★★ Argumentar con inversas
<span class="anker" id="aufg-27"></span>

<ol class="al">

<li>

Comprueba $(\mathbf{C}^{\top})^{-1}=(\mathbf{C}^{-1})^{\top}$ para $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$.

</li>

<li>

Sea $\mathbf{A}$ invertible y $\mathbf{A}\mathbf{B}=\mathbf 0$. Demuestra que entonces $\mathbf{B}=\mathbf 0$.

</li>

<li>

Con números, de $ab=0$ se sigue que $a=0$ o $b=0$. Demuestra con $\mathbf{A}=\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ que para matrices esto no se cumple. ¿Por qué no contradice esto el apartado (b)?

</li>

</ol>

:::loesung
(a) $\mathbf{C}^{-1}=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$, del ejercicio anterior; por tanto, $(\mathbf{C}^{-1})^{\top}=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$. Por otro lado, $\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)$, con $ad-bc=-2$; por tanto, $(\mathbf{C}^{\top})^{-1}=-\tfrac12\bigl(\begin{smallmatrix}4&-3\\-2&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$. Ambas coinciden.

(b) Se multiplica $\mathbf{A}\mathbf{B}=\mathbf 0$ por la izquierda por $\mathbf{A}^{-1}$: $\mathbf{B}=\mathbf{I}\mathbf{B}=\mathbf{A}^{-1}\mathbf{A}\mathbf{B}=\mathbf{A}^{-1}\mathbf 0=\mathbf 0$.

(c) $\mathbf{A}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{smallmatrix}\bigr)=\mathbf 0$, aunque $\mathbf{A}\ne\mathbf 0$. Geométricamente, $\mathbf{A}$ envía el vector $\mathbf{e}_2$ a $\mathbf{e}_1$, y $\mathbf{e}_1$ a $\mathbf{0}$; aplicada dos veces, todo acaba en el vector nulo. Esto no contradice el apartado (b), pues $\mathbf{A}$ no es invertible: $ad-bc=0$. La conclusión de (b) necesita la inversa.
:::
:::
