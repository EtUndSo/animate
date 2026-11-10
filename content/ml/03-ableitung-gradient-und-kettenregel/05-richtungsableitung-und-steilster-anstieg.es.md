---
title: Derivada direccional y máximo ascenso
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230500
summary: Las derivadas parciales dicen cómo reacciona la función cuando se modifica una sola entrada.
tags: derivada direccional
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Las derivadas parciales dicen cómo reacciona la función cuando se modifica una sola entrada. Si se desplazan todas las entradas a la vez en una dirección, la derivada direccional mide la pendiente. Con ella, esta sección muestra que el gradiente apunta en la dirección de máximo ascenso y es perpendicular a las curvas de nivel. Un ejemplo muestra que, aun así, el camino más empinado cuesta abajo no conduce necesariamente al punto más bajo.
:::

### La derivada direccional

<span class="anker" id="stufe-4-1"></span>

En el terreno, rara vez se camina exactamente hacia el norte o exactamente hacia el este. Quien está en el punto $\mathbf{x}$ y echa a andar en cualquier dirección nota una pendiente que depende de la dirección. Una dirección se describe mediante un vector $\mathbf{u}$ de longitud $1$. La longitud tiene que estar fijada: quien da pasos el doble de grandes sube el doble en cada paso, sin que el terreno sea más empinado.

:::definition Definición 4.1 (Derivada direccional)
<span class="anker" id="satz-4-1"></span>

Para un vector $\mathbf{u}$ con $\lVert\mathbf{u}\rVert=1$, se llama

<span class="anker" id="gl-4-1"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\lim_{t\to0}\frac{f(\mathbf{x}+t\,\mathbf{u})-f(\mathbf{x})}{t} \tag{4.1}$$

__derivada direccional__ de $f$ en el punto $\mathbf{x}$ en la dirección $\mathbf{u}$, siempre que el límite exista.
:::

Para $\mathbf{u}=\mathbf{e}_j$, es la derivada parcial respecto de $x_j$. En la imagen del paisaje, se corta el terreno a lo largo de la recta que pasa por $\mathbf{x}$ en la dirección $\mathbf{u}$, y la derivada direccional es la pendiente de esa curva de corte. Pero no hace falta calcularla de nuevo para cada dirección.

:::satz Teorema 4.2 (Derivada direccional y gradiente)
<span class="anker" id="satz-4-2"></span>

Si $f$ es diferenciable en el punto $\mathbf{x}$, para todo vector $\mathbf{u}$ de longitud $1$ se cumple

<span class="anker" id="gl-4-2"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}\mathbf{u} . \tag{4.2}$$
:::

:::beweis Derivada direccional y gradiente
Se pone en [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5), en particular, $\mathbf{h}=t\,\mathbf{u}$ con $t\ne0$; entonces $\lVert\mathbf{h}\rVert=|t|$. El cociente $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})-t\,\nabla f(\mathbf{x})^{\top}\mathbf{u}}{|t|}$ tiende a $0$, y por tanto también $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})}{t}-\nabla f(\mathbf{x})^{\top}\mathbf{u}$.
:::

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$, con $\nabla f=(4,\,5)^{\top}$ y la dirección $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$, que tiene longitud $\sqrt{0{,}36+0{,}64}=1$, se tiene

$$D_{\mathbf{u}}f(1,2)=4\cdot0{,}6+5\cdot0{,}8=2{,}4+4{,}0=6{,}4$$

(fig. [8](#abb-8)). En la dirección opuesta $-\mathbf{u}$, la pendiente es $-6{,}4$, y en la dirección $(0{,}8;\ -0{,}6)^{\top}$, que es perpendicular a $\mathbf{u}$, es $3{,}2-3{,}0=0{,}2$.

:::abbildung ml/k3rrichtung 8
La derivada direccional como producto escalar del gradiente y la dirección, para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $\mathbf{x}=(1,\,2)^{\top}$.
:::
::::

⁠**En resumen:** La pendiente en la dirección de un vector unitario $\mathbf{u}$ es el producto escalar $\nabla f(\mathbf{x})^{\top}\mathbf{u}$.

### La dirección de máximo ascenso

<span class="anker" id="stufe-4-2"></span>

¿En qué dirección hay que ir para que la subida sea lo más empinada posible? Según [(4.2)](#gl-4-2), se busca el vector unitario $\mathbf{u}$ para el que el producto escalar $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ es máximo. El [capítulo 1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) proporcionó la herramienta para ello: la desigualdad de Cauchy-Schwarz.

:::satz Teorema 4.3 (Máximo ascenso)
<span class="anker" id="satz-4-3"></span>

Sea $f$ diferenciable en el punto $\mathbf{x}$ y $\nabla f(\mathbf{x})\ne\mathbf{0}$. Entonces, para todo vector $\mathbf{u}$ de longitud $1$, se cumple

<span class="anker" id="gl-4-3"></span>
$$-\lVert\nabla f(\mathbf{x})\rVert\le D_{\mathbf{u}}f(\mathbf{x})\le\lVert\nabla f(\mathbf{x})\rVert . \tag{4.3}$$

La cota superior solo se alcanza para $\mathbf{u}=\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$, y la inferior, solo para $\mathbf{u}=-\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. El gradiente apunta, pues, en la dirección de máximo ascenso, y su longitud es la pendiente en esa dirección; el gradiente negativo apunta en la dirección de máximo descenso.
:::

:::beweis Máximo ascenso
Según la desigualdad de Cauchy-Schwarz del [capítulo 1, sección 5.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1), $|\nabla f(\mathbf{x})^{\top}\mathbf{u}|\le\lVert\nabla f(\mathbf{x})\rVert\,\lVert\mathbf{u}\rVert=\lVert\nabla f(\mathbf{x})\rVert$, y la igualdad se da exactamente cuando $\mathbf{u}$ es un múltiplo de $\nabla f(\mathbf{x})$. Los múltiplos de longitud $1$ son $\pm\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. Sustituyéndolos se obtiene $\pm\nabla f(\mathbf{x})^{\top}\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert=\pm\lVert\nabla f(\mathbf{x})\rVert$.
:::

Con el ángulo $\varphi$ entre $\nabla f(\mathbf{x})$ y $\mathbf{u}$ del [capítulo 1, sección 5.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2), se tiene $D_{\mathbf{u}}f(\mathbf{x})=\lVert\nabla f(\mathbf{x})\rVert\cos\varphi$. Si se va en la dirección del gradiente, $\varphi=0$ y $\cos\varphi=1$. Si uno se desvía $90^\circ$, la pendiente es nula. Si se va en sentido contrario, es lo más negativa posible. Según el [capítulo 1, sección 5.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ es la longitud de la sombra del gradiente sobre la recta en la dirección $\mathbf{u}$, y una sombra es máxima cuando la recta apunta en la dirección de la propia flecha.

En el teorema hay tres hipótesis. Primera: debe ser $\nabla f(\mathbf{x})\ne\mathbf{0}$; si el gradiente es nulo, según [(4.2)](#gl-4-2) la pendiente es nula en todas las direcciones, y ninguna dirección es más empinada que otra. Segunda: $f$ debe ser diferenciable; de lo contrario, [(4.2)](#gl-4-2) no se cumple. Tercera: el teorema compara direcciones de la misma longitud euclídea; si los pasos se miden de otro modo, cambia la dirección de máxima pendiente (recuadro «Contexto» más abajo).

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$ se tiene $\lVert\nabla f\rVert=\sqrt{16+25}=\sqrt{41}\approx6{,}403$, y la dirección de máxima pendiente es $(4,\,5)^{\top}/\sqrt{41}\approx(0{,}625;\ 0{,}781)^{\top}$. Ninguna dirección tiene una pendiente mayor. La dirección $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ de la subsección anterior solo se desvía de ella unos $1{,}8^\circ$; por eso su pendiente $6{,}4$ ya estaba casi en el valor máximo. En la dirección $(5,\,-4)^{\top}/\sqrt{41}$, perpendicular al gradiente, la pendiente es $(20-20)/\sqrt{41}=0$.
::::

⁠**En resumen:** El gradiente apunta en la dirección de máximo ascenso, y su longitud es la pendiente en ella; en sentido contrario al gradiente, la bajada es la más empinada.

:::hintergrund La dirección de máxima pendiente depende de cómo se midan los pasos
El teorema compara todas las direcciones $\mathbf{u}$ con $\lVert\mathbf{u}\rVert=1$ en la norma euclídea. El [capítulo 1, sección 3](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3), conocía otras normas. Si se permiten todos los pasos con $\lVert\mathbf{u}\rVert_\infty\le1$, es decir, si cada componente puede estar entre $-1$ y $1$, entonces $\nabla f^{\top}\mathbf{u}=\sum_j\partial_jf\cdot u_j$ es máximo cuando cada componente $u_j$ tiene el valor $+1$ o $-1$ con el signo de $\partial_jf$. La dirección de máxima pendiente es entonces $\operatorname{sign}(\nabla f)$, componente a componente, y la pendiente es $\sum_j|\partial_jf|=\lVert\nabla f\rVert_1$. Si, en cambio, se permiten todos los pasos con $\lVert\mathbf{u}\rVert_1\le1$, se invierte todo el presupuesto en la componente con el mayor $|\partial_jf|$: la dirección de máxima pendiente es un eje de coordenadas, y la pendiente es $\lVert\nabla f\rVert_\infty$. Para $\nabla f=(4,\,5)^{\top}$, esto da las direcciones $(1,\,1)^{\top}$ con pendiente $9$ y $(0,\,1)^{\top}$ con pendiente $5$. «El gradiente es la dirección de máxima pendiente» es, por tanto, una afirmación sobre la longitud euclídea. Depende también de las unidades de las variables: si se mide $x_1$ en otras unidades, cambian las longitudes de los pasos y, con ellas, la dirección de máxima pendiente, igual que las distancias en el [capítulo 1, sección 4.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2).
:::

### El gradiente es perpendicular a las curvas de nivel

<span class="anker" id="stufe-4-3"></span>

Quien camina a lo largo de una curva de nivel ni sube ni baja. En la dirección de la curva de nivel, la pendiente es, por tanto, nula, y según la subsección anterior la pendiente es nula exactamente en las direcciones perpendiculares al gradiente. Por eso, el gradiente es perpendicular a la curva de nivel. Con más precisión, esto significa:

:::satz Teorema 4.4 (Gradiente y curva de nivel)
<span class="anker" id="satz-4-4"></span>

Sea $f$ diferenciable en el punto $\mathbf{x}$, $\nabla f(\mathbf{x})\ne\mathbf{0}$ y $c=f(\mathbf{x})$. El conjunto de nivel de la aproximación lineal que pasa por $\mathbf{x}$, es decir, el conjunto de los puntos $\mathbf{x}+\mathbf{h}$ con $\nabla f(\mathbf{x})^{\top}\mathbf{h}=0$, es, con dos variables, la recta que pasa por $\mathbf{x}$ perpendicular al gradiente. Es la recta tangente a la curva de nivel de $f$ para el valor $c$.
:::

Que la recta toque la curva de nivel se sigue de la lupa: cerca de $\mathbf{x}$, $f$ y su aproximación lineal solo se diferencian en un error que desaparece más rápido que $\lVert\mathbf{h}\rVert$, y por eso también sus curvas de nivel para el valor $c$ se diferencian tan poco que en $\mathbf{x}$ tienen la misma dirección. El ejercicio [22](die-kettenregel-fur-mehrere-variablen.html#aufg-22) ofrece una demostración con la regla de la cadena. Con más de dos variables, lo mismo vale para el conjunto de nivel, que entonces es una superficie: el gradiente es perpendicular a ella.

::::beispiel [Ejemplo numérico]
Para el cuenco $f(\mathbf{x})=x_1^2+4x_2^2$ se tiene $\nabla f(\mathbf{x})=(2x_1,\,8x_2)^{\top}$, que en el punto $(1,\,1)$ es igual a $(2,\,8)^{\top}$. La curva de nivel que pasa por este punto es la elipse $x_1^2+4x_2^2=5$. La dirección $\mathbf{t}=(4,\,-1)^{\top}$ es perpendicular al gradiente, pues $2\cdot4+8\cdot(-1)=0$. Si desde $(1,\,1)$ se avanza un trozo $s$ en esta dirección, se tiene

$$f(1+4s,\ 1-s)=(1+4s)^2+4\,(1-s)^2=5+20s^2 .$$

El valor solo cambia en $20s^2$, es decir, en algo que desaparece más rápido que $s$: la recta toca la curva de nivel y es su recta tangente. La fig. [9](#abb-9) muestra los gradientes en muchos puntos; cada uno es perpendicular a la curva de nivel que pasa por su punto de partida.

:::abbildung ml/k3hoehen 9
Gradientes (rojo, dibujados acortados) sobre curvas de nivel (gris). (a) En el cuenco redondo, todos los gradientes apuntan radialmente hacia fuera, alejándose del centro. (b) En el cuenco alargado también son perpendiculares a las curvas de nivel, pero solo sobre los ejes apuntan radialmente hacia fuera. En el punto $(1,\,1)$ (negro), la dirección de máximo descenso está dibujada en azul. En (a) apunta al punto más bajo; en (b) se desvía unos $31^\circ$ de la dirección hacia el punto más bajo (discontinua).
:::
::::

⁠**En resumen:** A lo largo de una curva de nivel, $f$ no cambia; por eso el gradiente es perpendicular a ella.

### Máximo descenso y el punto más bajo

<span class="anker" id="stufe-4-4"></span>

En un cuenco redondo es evidente que el camino más empinado cuesta abajo lleva al centro. En un cuenco alargado es falso, y esta diferencia es importante, porque es fácil esperar del gradiente más de lo que sabe.

Para $f(\mathbf{x})=x_1^2+x_2^2$ se tiene $\nabla f(\mathbf{x})=2\mathbf{x}$. El gradiente negativo $-2\mathbf{x}$ apunta, pues, desde cada punto exactamente al origen, el punto más bajo del cuenco. Para $f(\mathbf{x})=x_1^2+4x_2^2$ se tiene $-\nabla f(\mathbf{x})=(-2x_1,\,-8x_2)^{\top}$, y esto solo es un múltiplo de $-\mathbf{x}$ si $x_1=0$ o $x_2=0$, es decir, sobre los ejes. En todos los demás puntos, el máximo descenso pasa de largo del punto más bajo.

La razón está en la forma de las curvas de nivel. El gradiente solo sabe cómo está inclinado el terreno en su punto de partida; allí es perpendicular a la curva de nivel. Con curvas de nivel alargadas, la perpendicular queda oblicua respecto de la dirección hacia el centro. En el ejemplo, $f$ crece en la dirección $x_2$ cuatro veces más rápido que en la dirección $x_1$; las paredes del cuenco son más empinadas en la dirección $x_2$, y el máximo descenso discurre sobre todo transversalmente a ellas.

::::beispiel [Ejemplo numérico]
En el punto $(1,\,1)$, $-\nabla f=(-2,\,-8)^{\top}$, con longitud $\sqrt{68}\approx8{,}246$; la dirección de máximo descenso es, pues, $(-0{,}243;\ -0{,}970)^{\top}$. La dirección hacia el punto más bajo es $(-1,\,-1)^{\top}/\sqrt2\approx(-0{,}707;\ -0{,}707)^{\top}$. El ángulo entre ambas tiene el coseno

$$\frac{(-2)\cdot(-1)+(-8)\cdot(-1)}{\sqrt{68}\cdot\sqrt2}=\frac{10}{\sqrt{136}}\approx0{,}857,$$

es decir, mide unos $31^\circ$. En la dirección del punto más bajo, la pendiente es, según [(4.2)](#gl-4-2), solo $-10/\sqrt2\approx-7{,}07$; en la de máximo descenso, en cambio, $-8{,}246$.
::::

⁠**En resumen:** El gradiente negativo apunta cuesta abajo de la forma más empinada, pero solo con curvas de nivel redondas apunta al punto más bajo; con curvas de nivel alargadas pasa de largo.

:::aufgabe Ejercicio 13 ★ Pendientes en muchas direcciones
<span class="anker" id="aufg-13"></span>

Sea $f(\mathbf{x})=x_1^2+4x_2^2$ y $\mathbf{x}=(1,\,1)^{\top}$.

<ol class="al">

<li>

Calcula las derivadas direccionales en las direcciones $\mathbf{e}_1$, $\mathbf{e}_2$, $(1,\,1)^{\top}/\sqrt2$ y $(-1,\,1)^{\top}/\sqrt2$.

</li>

<li>

Compara con $\lVert\nabla f(\mathbf{x})\rVert$. ¿Cuál de las cuatro direcciones está más cerca de la de máxima pendiente?

</li>

</ol>

:::loesung
(a) Se tiene $\nabla f(1,1)=(2,\,8)^{\top}$. Según [(4.2)](#gl-4-2):

$$D_{\mathbf{e}_1}f=2,\qquad D_{\mathbf{e}_2}f=8,\qquad D_{(1,1)/\sqrt2}f=\frac{2+8}{\sqrt2}\approx7{,}071,\qquad D_{(-1,1)/\sqrt2}f=\frac{-2+8}{\sqrt2}\approx4{,}243 .$$

(b) $\lVert\nabla f\rVert=\sqrt{68}\approx8{,}246$; ninguna de las pendientes es mayor, como exige [(4.3)](#gl-4-3). La más cercana a la dirección de máxima pendiente es $\mathbf{e}_2$, con $8$. El ángulo entre $\mathbf{e}_2$ y $\nabla f$ tiene el coseno $8/\sqrt{68}\approx0{,}970$, es decir, mide unos $14^\circ$; para $(1,\,1)^{\top}/\sqrt2$ son unos $31^\circ$.
:::
:::

:::aufgabe Ejercicio 14 ★★ Una hipérbola como curva de nivel
<span class="anker" id="aufg-14"></span>

Sea $f(\mathbf{x})=x_1x_2$ y $\mathbf{x}=(2,\,1)^{\top}$.

<ol class="al">

<li>

Calcula $\nabla f(\mathbf{x})$, la dirección de máxima pendiente y la pendiente en ella.

</li>

<li>

La curva de nivel que pasa por $\mathbf{x}$ es $x_2=2/x_1$. Calcula la pendiente de esta curva en el punto $x_1=2$, escribe su dirección tangente como vector y comprueba que es perpendicular a $\nabla f(\mathbf{x})$.

</li>

</ol>

:::loesung
(a) $\nabla f(\mathbf{x})=(x_2,\,x_1)^{\top}$; en el punto $(2,\,1)$, por tanto, $(1,\,2)^{\top}$. La dirección de máxima pendiente es $(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$, y la pendiente en ella, $\sqrt5\approx2{,}236$.

(b) La curva de nivel $x_2=2/x_1$ tiene la pendiente $-2/x_1^2$; en $x_1=2$, por tanto, $-\tfrac12$. Una dirección tangente es $(1,\,-\tfrac12)^{\top}$ o, multiplicada por $2$, $(2,\,-1)^{\top}$. Se tiene $(1,\,2)(2,\,-1)^{\top}=2-2=0$: el gradiente es perpendicular a la curva de nivel.
:::
:::

:::aufgabe Ejercicio 15 ★★ Funciones lineales
<span class="anker" id="aufg-15"></span>

Sea $f(\mathbf{x})=\mathbf{a}^{\top}\mathbf{x}+b$ con $\mathbf{a}\in\mathbb{R}^d$ fijo, $\mathbf{a}\ne\mathbf{0}$, y un número $b$.

<ol class="al">

<li>

Demuestra que $\nabla f(\mathbf{x})=\mathbf{a}$ en todos los puntos. ¿Qué son las curvas de nivel para $d=2$?

</li>

<li>

Para las viviendas del [capítulo 1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), $\hat y=\mathbf{w}^{\top}\mathbf{x}+b$ con $\mathbf{w}=(3,\,10,\,-4)^{\top}$, donde $x_1$ es la superficie en $\mathrm m^2$, $x_2$ el número de habitaciones y $x_3$ la distancia al centro en km. ¿Qué variación $\mathbf{u}$ de las características con $\lVert\mathbf{u}\rVert=1$ aumenta más la predicción, y en cuánto?

</li>

<li>

Si se da la superficie en unidades de $10\,\mathrm m^2$, el peso $w_1=3$ pasa a ser $30$. ¿Cuál es ahora la dirección de máxima pendiente? ¿Qué se aprende de ello sobre el teorema del máximo ascenso?

</li>

</ol>

:::loesung
(a) $\partial_k(\mathbf{a}^{\top}\mathbf{x}+b)=a_k$, así que $\nabla f=\mathbf{a}$ en todas partes. Para $d=2$, las curvas de nivel son las rectas $a_1x_1+a_2x_2+b=c$; son paralelas entre sí y perpendiculares a $\mathbf{a}$.

(b) El gradiente respecto de $\mathbf{x}$ es $\mathbf{w}=(3,\,10,\,-4)^{\top}$, con $\lVert\mathbf{w}\rVert=\sqrt{9+100+16}=\sqrt{125}\approx11{,}18$. La variación de longitud $1$ con máxima pendiente es $\mathbf{u}=\mathbf{w}/\sqrt{125}\approx(0{,}268;\ 0{,}894;\ -0{,}358)^{\top}$, y aumenta la predicción en unos $11{,}18$ miles de euros: algo más de superficie, bastantes más habitaciones y algo más cerca del centro.

(c) En las nuevas unidades se tiene $\mathbf{w}'=(30,\,10,\,-4)^{\top}$, con $\lVert\mathbf{w}'\rVert=\sqrt{1016}\approx31{,}87$, y la dirección de máxima pendiente es $\mathbf{w}'/\lVert\mathbf{w}'\rVert\approx(0{,}941;\ 0{,}314;\ -0{,}125)^{\top}$: ahora está casi por completo en la superficie. La misma vivienda, los mismos precios, pero otra dirección de máxima pendiente. El teorema del máximo ascenso compara pasos de igual longitud euclídea en las coordenadas elegidas, y lo que significa «longitud $1$» depende de las unidades, exactamente igual que las distancias en el [capítulo 1, sección 4.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2). Con características en unidades distintas, la dirección de máxima pendiente solo es significativa tras la estandarización del [capítulo 1, sección 4.5](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5).
:::
:::

:::aufgabe Ejercicio 16 ★★★ ¿Cuándo apunta el máximo descenso al centro?
<span class="anker" id="aufg-16"></span>

Sea $f(\mathbf{x})=a\,x_1^2+b\,x_2^2$ con números $a,b>0$.

<ol class="al">

<li>

Demuestra: $-\nabla f(\mathbf{x})$ es un múltiplo positivo de $-\mathbf{x}$ si y solo si $a=b$ o $\mathbf{x}$ está sobre uno de los ejes ($\mathbf{x}\ne\mathbf{0}$).

</li>

<li>

Para $a=1$, $b=4$, calcula en los puntos $(1,\,1)$, $(2,\,1)$ y $(4,\,1)$ el ángulo entre $-\nabla f$ y $-\mathbf{x}$. ¿Cómo cambia cuando uno se desplaza hacia fuera sobre la recta $x_2=1$?

</li>

</ol>

:::loesung
(a) Se tiene $-\nabla f(\mathbf{x})=(-2ax_1,\,-2bx_2)^{\top}$. Este vector es igual a $c\,(-x_1,\,-x_2)^{\top}$ con algún $c>0$ si y solo si $2ax_1=c\,x_1$ y $2bx_2=c\,x_2$. Si ambas coordenadas son distintas de cero, se sigue $2a=c=2b$, es decir, $a=b$. Si $x_1=0$, basta $c=2b$; si $x_2=0$, basta $c=2a$. En un cuenco redondo, el máximo descenso apunta, por tanto, en todas partes hacia el origen; en uno alargado, solo sobre los ejes.

(b) Para $a=1$, $b=4$ se tiene $-\nabla f=(-2x_1,\,-8x_2)^{\top}$:

$$\begin{aligned} (1,\,1)&:\ \cos\varphi=\frac{2+8}{\sqrt{68}\,\sqrt2}\approx0{,}857,\ \varphi\approx31{,}0^\circ;\\ (2,\,1)&:\ \cos\varphi=\frac{8+8}{\sqrt{80}\,\sqrt5}=0{,}8,\ \varphi\approx36{,}9^\circ;\\ (4,\,1)&:\ \cos\varphi=\frac{32+8}{\sqrt{128}\,\sqrt{17}}\approx0{,}857,\ \varphi\approx31{,}0^\circ . \end{aligned}$$

Sobre la recta $x_2=1$, el ángulo crece primero desde $0^\circ$ en $x_1=0$ y después vuelve a disminuir; lejos, hacia fuera, el punto está casi en la dirección del eje $x_1$, y allí el máximo descenso vuelve a apuntar casi al centro.
:::
:::
