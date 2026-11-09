---
title: Etapa 9: Desigualdades elementales
pfad: Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1 / Conjuntos, lógica y números reales
order: 1211100
summary: A menudo una expresión no se puede calcular, solo acotar.
tags: Bernoulli, Young, Medias, media geométrica, media aritmética, Cauchy-Schwarz, Minkowski, vector
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
A menudo una expresión no se puede calcular, solo acotar. Esta etapa aporta las cinco acotaciones estándar.
:::

**La idea.** Casi todo se sigue de un solo hecho: un cuadrado no es negativo. Si se desarrolla $(a-b)^2\ge0$, surge $2ab\le a^2+b^2$. Young, las medias y Cauchy-Schwarz son esta línea reescrita con habilidad. Solo Bernoulli necesita la inducción.

:::satz Teorema 9.1 (Cinco desigualdades)
<span class="anker" id="satz-9-1"></span>

En $\mathbb{R}$ se cumple:

<ol class="rm">

<li>

__Bernoulli__: Para $x>-1$, $x\ne0$ y $n\ge2$ se cumple $(1+x)^n>1+nx$.

</li>

<li>

__Young__: Para $\varepsilon>0$ y $x,y\in\mathbb{R}$ se cumple $|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$.

</li>

<li>

__Medias__: Para $x,y\ge0$ se cumple $\sqrt{xy}\le\frac{x+y}2$. A la izquierda está la __media geométrica__, a la derecha la __media aritmética__.

</li>

<li>

__Cauchy-Schwarz__: Para $x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}$ se cumple, con $\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i^2}\ge0$,

<span class="anker" id="gl-9-1"></span>
$$\sum_{i=1}^n|x_iy_i|\le\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|. \tag{9.1}$$

</li>

<li>

__Minkowski__: Con $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$ se cumple

<span class="anker" id="gl-9-2"></span>
$$\sqrt{\sum_{i=1}^n(x_i+y_i)^2}\le\sqrt{\sum_{i=1}^nx_i^2}+\sqrt{\sum_{i=1}^ny_i^2},\quad\text{es decir,}\quad\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|. \tag{9.2}$$

</li>

</ol>
:::

⁠**Cómo leerlo:** $\vec x=(x_1,\dots,x_n)$ es un __vector__, una lista de $n$ números, y $\|\vec x\|$ su __norma__. Para $n=2$ es, por Pitágoras, la longitud de la flecha del origen al punto $(x_1,x_2)$. Entonces [(9.2)](#gl-9-2) es la desigualdad triangular para flechas, y en la Parte 8 de [(9.1)](#gl-9-1) surge el producto escalar. En Young, $\varepsilon$ es un tipo de cambio: un término pequeño en $x$ cuesta un término grande en $y$. **Por qué las hipótesis:** Bernoulli: $x=-4$, $n=3$ da $-27>-11$, falso, así que hace falta $x>-1$. Para $x=0$ o $n=1$ hay igualdad. Medias: $x=y=-1$ da $1\le-1$, falso. Young: $\varepsilon=-1$ hace negativo el lado derecho.

:::abbildung hm1/k1mittel 9
A la izquierda, las medias como semicírculo: el radio es la media aritmética, la altura sobre el punto de división, la geométrica. La altura nunca es mayor que el radio. A la derecha, Bernoulli para $n=3$: la recta toca la curva en $x=0$ y queda por debajo para $x>-1$.
:::

:::beweis Las cinco desigualdades
⁠*Bernoulli*, inducción desde $n_0=2$. Caso base: $(1+x)^2=1+2x+x^2>1+2x$, pues $x^2>0$ por el teorema [4.2](anordnungsaxiome.html#satz-4-2) (d). Paso: como $1+x>0$, por (O4) se puede multiplicar la hipótesis por $1+x$: $(1+x)^{n+1}>(1+nx)(1+x)=1+(n+1)x+nx^2>1+(n+1)x$.

⁠*Young.* $\sqrt\varepsilon$ existe por el teorema [7.2](intervallschachtelung-und-wurzeln.html#satz-7-2), y $\sqrt\varepsilon>0$. Los cuadrados no son negativos:

$$0\le\Bigl(\sqrt\varepsilon\,x\pm\frac1{\sqrt\varepsilon}\,y\Bigr)^2=\varepsilon x^2\pm2xy+\frac1\varepsilon y^2.$$

Eso da $\mp2xy\le\varepsilon x^2+\frac1\varepsilon y^2$. Como $|xy|=\max\{xy,-xy\}$, la afirmación se sigue tras dividir por 2.

⁠*Medias.* Young con $\varepsilon=1$ para $\sqrt x$ y $\sqrt y$: $\sqrt x\sqrt y\le\frac12x+\frac12y$, y $\sqrt x\sqrt y=\sqrt{xy}$.

⁠*Cauchy-Schwarz.* Si todos los $x_i=0$ o todos los $y_i=0$, queda $0\le0$. Si no, $\|\vec x\|>0$ y $\|\vec y\|>0$, y se define $\xi_i:=x_i/\|\vec x\|$, $\eta_i:=y_i/\|\vec y\|$. Dividiendo [(9.1)](#gl-9-1) por $\|\vec x\|\|\vec y\|$, hay que demostrar $\sum_{i=1}^n|\xi_i\eta_i|\le1$. Se cumple $\sum_i\xi_i^2=\frac1{\|\vec x\|^2}\sum_ix_i^2=1$, e igualmente $\sum_i\eta_i^2=1$. Por las medias para $\xi_i^2$, $\eta_i^2$,

$$\sum_{i=1}^n|\xi_i\eta_i|=\sum_{i=1}^n\sqrt{\xi_i^2\eta_i^2}\le\sum_{i=1}^n\frac{\xi_i^2+\eta_i^2}2=\frac12+\frac12=1.$$

⁠*Minkowski.* Sea $s_i:=x_i+y_i$, es decir, $\vec s=\vec x+\vec y$. Con (AM), después $a\le|a|$, después [(9.1)](#gl-9-1) para las listas $x_i,s_i$ e $y_i,s_i$:

$$\|\vec s\|^2=\sum_ix_is_i+\sum_iy_is_i\le\sum_i|x_is_i|+\sum_i|y_is_i|\le\bigl(\|\vec x\|+\|\vec y\|\bigr)\|\vec s\|.$$

Para $\|\vec s\|=0$, a la izquierda de [(9.2)](#gl-9-2) queda 0. Si no, se divide por $\|\vec s\|$.
:::

::::beispiel
Bernoulli: $1{,}01^{10}>1{,}1$, exactamente $1{,}1046$. Para $x$ pequeño, $1+nx$ es una buena aproximación: un 1 % más de tensión significa en una resistencia aproximadamente un 2 % más de potencia, exactamente un 2,01 %. Para $x$ grande es tosca: $2^{10}=1024$ frente a 11. Young con $x=2$, $y=8$: para $\varepsilon=1$ queda $16\le34$, para $\varepsilon=4$ queda $16\le16$. Cauchy-Schwarz con $\vec x=(3,4)$, $\vec y=(1,2)$: $3+8=11\le5\sqrt5\approx11{,}18$. Minkowski: $\|(4,6)\|=\sqrt{52}\approx7{,}21\le5+\sqrt5\approx7{,}24$.
::::

⁠**Caso límite:** Con $x=y$ ambas medias son iguales; en el semicírculo, la altura está en el centro.

:::frage ¿Cuándo uso cada desigualdad?
Potencia de un número cercano a 1: Bernoulli. Acotar un producto: Young, medias. Suma de productos: Cauchy-Schwarz. Raíz de una suma: Minkowski.
:::

:::aufgabe Ejercicio 10 ★★★ Acotar
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Demuestra $2^{n-1}\ge n$ para todo $n\in\mathbb{N}$. (La etapa [7](intervallschachtelung-und-wurzeln.html#stufe-7) necesita esta desigualdad.)

</li>

<li>

Acota $0{,}995^{20}$ por abajo y compara con el valor exacto.

</li>

<li>

Un rectángulo tiene área 16. Demuestra con las medias que el perímetro es al menos 16. ¿Para qué lados hay igualdad?

</li>

<li>

Comprueba Cauchy-Schwarz y Minkowski para $\vec x=(1,2,2)$, $\vec y=(2,-1,2)$.

</li>

<li>

Demuestra: para $\vec y=t\,\vec x$ con $t\in\mathbb{R}$ hay igualdad en [(9.1)](#gl-9-1).

</li>

</ol>

:::loesung
(a) Para $n=1,2$ queda $1\ge1$ y $2\ge2$. Para $n\ge3$ es $2^{n-1}=(1+1)^{n-1}>1+(n-1)=n$ por Bernoulli. (b) $x=-0{,}005$, $n=20$: $0{,}995^{20}>1-0{,}1=0{,}9$. Exactamente $0{,}9046$; la cota queda un 0,5 % por debajo. (c) Lados $a,b>0$, $ab=16$: perímetro $2(a+b)\ge2\cdot2\sqrt{ab}=16$. Igualdad para $a=b=4$, el cuadrado. (d) $\|\vec x\|=\sqrt{1+4+4}=3$, $\|\vec y\|=\sqrt{4+1+4}=3$. Cauchy-Schwarz: $2+2+4=8\le9$. Minkowski: $\vec x+\vec y=(3,1,4)$, $\|\vec x+\vec y\|=\sqrt{26}\approx5{,}10\le6$. (e) $\sum_i|x_i\cdot tx_i|=|t|\sum_ix_i^2=|t|\,\|\vec x\|^2$. A la derecha: $\|t\vec x\|=\sqrt{t^2\sum_ix_i^2}=|t|\,\|\vec x\|$, luego $\|\vec x\|\,\|\vec y\|=|t|\,\|\vec x\|^2$.
:::
:::
