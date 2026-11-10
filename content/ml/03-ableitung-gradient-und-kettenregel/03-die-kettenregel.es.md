---
title: La regla de la cadena
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230300
summary: Muchas funciones surgen al sustituir una función dentro de otra.
tags: composición, función logística
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Muchas funciones surgen al sustituir una función dentro de otra. La regla de la cadena dice cómo se obtiene la derivada de una composición así a partir de las derivadas de las partes: los factores de las distintas etapas se multiplican. Esto vale para cadenas de cualquier número de eslabones. Al final aparece la función logística, cuya derivada puede expresarse mediante la propia función.
:::

### Composición

<span class="anker" id="stufe-2-1"></span>

La función $(3x+1)^2$ se calcula en dos pasos: primero $u=3x+1$, después $u^2$. Muchas fórmulas están construidas así, como composición de pasos sencillos. Quien reconoce esta forma de construcción puede formar la derivada a partir de las derivadas de los pasos.

:::definition Definición 2.1 (Composición)
<span class="anker" id="satz-2-1"></span>

Si $g$ y $f$ son funciones y cada valor $g(x)$ está donde $f$ está definida, la función

$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$

se llama la __composición__ de $f$ y $g$, y se lee «$f$ compuesta con $g$». La función $g$, que se aplica primero, se llama función interior; $f$ se llama función exterior.
:::

::::beispiel [Ejemplo numérico]
Para $F(x)=(3x+1)^2$, la función interior es $g(x)=3x+1$ y la exterior es $f(u)=u^2$; así, $F=f\circ g$. En el punto $1$ se tiene $g(1)=4$ y $F(1)=f(4)=16$. El orden importa: $(g\circ f)(x)=g(f(x))=3x^2+1$ es otra función, con el valor $4$ en el punto $1$.
::::

⁠**En resumen:** Una composición $f\circ g$ aplica primero $g$ y después $f$; el orden no puede intercambiarse.

### La regla de la cadena

<span class="anker" id="stufe-2-2"></span>

¿Cómo reacciona $F=f\circ g$ ante una pequeña variación de $x$? Se sigue la variación a través de las dos etapas. La primera etapa transmite una pequeña variación $\Delta x$, según la aproximación lineal, aproximadamente como $\Delta u\approx g'(x)\,\Delta x$. La segunda etapa transmite esta variación como $\Delta y\approx f'(u)\,\Delta u$. En conjunto, $\Delta y\approx f'(u)\,g'(x)\,\Delta x$. Como en un tren de engranajes de dos etapas, los factores de las etapas se multiplican (fig. [4](#abb-4)).

:::abbildung ml/k3getriebe 4
La regla de la cadena como tren de engranajes para $y=(3x+1)^2$ en el punto $1$. Las tres rectas numéricas tienen la misma escala. El trozo $\Delta x=0{,}01$ (azul) lo estira la primera etapa hasta el triple, $\Delta u=0{,}03$ (naranja), y la segunda etapa hasta aproximadamente ocho veces eso, $\Delta y=0{,}2409\approx0{,}24$ (rojo).
:::

:::satz Teorema 2.2 (Regla de la cadena)
<span class="anker" id="satz-2-2"></span>

Si $g$ es derivable en el punto $x$ y $f$ es derivable en el punto $g(x)$, entonces $f\circ g$ es derivable en el punto $x$, y

<span class="anker" id="gl-2-1"></span>
$$(f\circ g)'(x)=f'\bigl(g(x)\bigr)\cdot g'(x). \tag{2.1}$$
:::

Es importante dónde se evalúan las derivadas: $g'$ en el punto $x$, pero $f'$ en el punto $u=g(x)$, es decir, allí donde la función exterior trabaja realmente. Con $u=g(x)$ y $y=f(u)$, la regla se escribe a menudo como $\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\mathrm{d} y}{\mathrm{d} u}\cdot\frac{\mathrm{d} u}{\mathrm{d} x}$. Parece como si $\mathrm{d} u$ se simplificara. Como regla mnemotécnica eso es útil; como justificación, no, pues los símbolos no son fracciones, sino límites.

:::beweis Regla de la cadena
Sea $u=g(x)$. Según la aproximación lineal [(1.4)](die-ableitung.html#gl-1-4), se tiene $g(x+h)=u+g'(x)\,h+r_g(h)$ con $r_g(h)/h\to0$ y $f(u+k)=f(u)+f'(u)\,k+r_f(k)$ con $r_f(k)/k\to0$; además se toma $r_f(0)=0$. Se pone $k=g(x+h)-u=g'(x)\,h+r_g(h)$. Entonces

$$f\bigl(g(x+h)\bigr)-f(u)=f'(u)\,k+r_f(k)=f'(u)\,g'(x)\,h+f'(u)\,r_g(h)+r_f(k).$$

Tras dividir entre $h$, el sumando central tiende a $0$. Para el último se escribe $r_f(k)/h=\bigl(r_f(k)/k\bigr)\cdot(k/h)$ mientras $k\ne0$; el primer factor tiende a $0$, porque con $h$ también $k$ tiende a $0$, y el segundo tiende a $g'(x)$. Si $k=0$, el sumando es $0$ de todos modos. Queda $f'(u)\,g'(x)$.
:::

::::beispiel [Ejemplo numérico]
Para $F(x)=(3x+1)^2$ se tiene $g'(x)=3$ y $f'(u)=2u$. En el punto $1$, $u=g(1)=4$; así,

$$F'(1)=f'(4)\cdot g'(1)=8\cdot3=24 .$$

Comprobación: desarrollando, $F(x)=9x^2+6x+1$, luego $F'(x)=18x+6$ y $F'(1)=24$. La fig. [4](#abb-4) muestra lo mismo con números: $F(1{,}01)=4{,}03^2=16{,}2409$, y la aproximación lineal predice $16+24\cdot0{,}01=16{,}24$.
::::

⁠**En resumen:** En una composición se multiplican las derivadas de las etapas, cada una evaluada en el punto en el que trabaja su etapa: $(f\circ g)'(x)=f'(g(x))\,g'(x)$.

### Cadenas de muchos eslabones

<span class="anker" id="stufe-2-3"></span>

La mayoría de los cálculos constan de más de dos pasos. La regla de la cadena puede aplicarse repetidamente: con tres etapas, $f_3\circ f_2\circ f_1=f_3\circ(f_2\circ f_1)$, y aplicada dos veces, [(2.1)](#gl-2-1) da un producto de tres factores. Con cualquier número de etapas ocurre lo mismo.

:::satz Teorema 2.3 (Regla de la cadena para muchos eslabones)
<span class="anker" id="satz-2-3"></span>

Sea $u_0=x$ y $u_k=f_k(u_{k-1})$ para $k=1,\dots,L$, y sea cada función $f_k$ derivable en el punto $u_{k-1}$. Entonces

<span class="anker" id="gl-2-2"></span>
$$\frac{\mathrm{d} u_L}{\mathrm{d} x}=f_L'(u_{L-1})\cdot f_{L-1}'(u_{L-2})\cdots f_1'(u_0). \tag{2.2}$$
:::

De aquí se sigue un orden para el cálculo. Cada factor necesita el valor en el que trabaja su etapa. Por eso se calculan primero los valores intermedios $u_1,u_2,\dots$, como en la evaluación ordinaria, y solo después los factores. En qué orden se multiplican luego los factores da igual cuando son números.

::::beispiel [Ejemplo numérico]
Sea $y=\dfrac1{(x^2+1)^3}$ en el punto $x=1$. La cadena tiene tres eslabones:

$$u_1=x^2+1=2,\qquad u_2=u_1^3=8,\qquad y=\frac1{u_2}=\frac18 .$$

Los factores son $\frac{\mathrm{d} u_1}{\mathrm{d} x}=2x=2$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=3u_1^2=12$ y $\frac{\mathrm{d} y}{\mathrm{d} u_2}=-\frac1{u_2^2}=-\frac1{64}$, luego

$$\frac{\mathrm{d} y}{\mathrm{d} x}=2\cdot12\cdot\Bigl(-\frac1{64}\Bigr)=-\frac{24}{64}=-0{,}375 .$$

Comprobación: $y=(x^2+1)^{-3}$ tiene, según las reglas de la potencia y de la cadena, la derivada $-3\,(x^2+1)^{-4}\cdot2x$; en el punto $1$, por tanto, $-6/16=-0{,}375$.
::::

⁠**En resumen:** En una cadena larga, la derivada es el producto de las derivadas de todos los eslabones; primero se calculan los valores intermedios, después los factores.

### La función logística

<span class="anker" id="stufe-2-4"></span>

Algunas magnitudes deben estar, de forma suave, entre dos cotas, por ejemplo una proporción entre $0$ y $1$. Una función que lleva cada número real a este rango, sin saltos, sin puntos angulosos y siempre creciente, es la función logística. Describe también el crecimiento con saturación: una magnitud crece primero de forma casi exponencial y después se aproxima a una cota superior. Su derivada es un bonito ejemplo de la regla de la cadena y tiene una forma notable.

:::definition Definición 2.4 (Función logística)
<span class="anker" id="satz-2-4"></span>

La función

<span class="anker" id="gl-2-3"></span>
$$\sigma(x)=\frac1{1+\mathrm{e}^{-x}} \tag{2.3}$$

se llama __función logística__.
:::

Para $x$ grandes y positivos, $\mathrm{e}^{-x}$ es casi $0$ y $\sigma(x)$ casi $1$. Para $x$ grandes y negativos, $\mathrm{e}^{-x}$ es enorme y $\sigma(x)$ casi $0$. En el punto $0$, $\sigma(0)=\tfrac12$. Además, $\sigma(-x)=1-\sigma(x)$, pues $\frac1{1+\mathrm{e}^{x}}=\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-x}+1}=1-\frac1{1+\mathrm{e}^{-x}}$; la gráfica es, por tanto, simétrica respecto del punto $(0,\,\tfrac12)$ (fig. [5](#abb-5)).

:::satz Teorema 2.5 (Derivada de la función logística)
<span class="anker" id="satz-2-5"></span>

Se cumple

<span class="anker" id="gl-2-4"></span>
$$\sigma'(x)=\sigma(x)\,\bigl(1-\sigma(x)\bigr). \tag{2.4}$$

La derivada es positiva en todas partes y vale como máximo $\tfrac14$; el valor máximo $\tfrac14$ lo alcanza en el punto $0$.
:::

:::herleitung La derivada de la función logística
La función es una cadena de tres eslabones: $u_1=-x$, $u_2=1+\mathrm{e}^{u_1}$, $\sigma=1/u_2$. Los factores son $-1$, $\mathrm{e}^{u_1}=\mathrm{e}^{-x}$ y $-1/u_2^2$. Según [(2.2)](#gl-2-2),

$$\sigma'(x)=-\frac1{(1+\mathrm{e}^{-x})^2}\cdot\mathrm{e}^{-x}\cdot(-1)=\frac{\mathrm{e}^{-x}}{(1+\mathrm{e}^{-x})^2}=\frac1{1+\mathrm{e}^{-x}}\cdot\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}} .$$

El primer factor es $\sigma(x)$. El segundo es $\frac{(1+\mathrm{e}^{-x})-1}{1+\mathrm{e}^{-x}}=1-\sigma(x)$. Como $\sigma(x)$ está entre $0$ y $1$, ambos factores son positivos. Para un número $p$ entre $0$ y $1$ se tiene $p\,(1-p)=\tfrac14-(p-\tfrac12)^2\le\tfrac14$, con igualdad exactamente para $p=\tfrac12$, es decir, para $x=0$.
:::

:::abbildung ml/k3logistisch 5
La función logística $\sigma$ (azul) sube de $0$ a $1$, con la máxima pendiente en el punto $0$. Su derivada (rojo) tiene allí su valor máximo $\tfrac14$ y se hace pequeña rápidamente a ambos lados. Están marcados los valores en los puntos $0$ y $2$ del ejemplo numérico.
:::

::::beispiel [Ejemplo numérico]
En el punto $2$, $\mathrm{e}^{-2}\approx0{,}1353$; así, $\sigma(2)\approx1/1{,}1353\approx0{,}8808$ y

$$\sigma'(2)=\sigma(2)\,\bigl(1-\sigma(2)\bigr)\approx0{,}8808\cdot0{,}1192\approx0{,}1050 .$$

Una vez calculado $\sigma(2)$, la derivada solo cuesta una resta y una multiplicación, ninguna función exponencial más. En el punto $10$, $\sigma(10)\approx0{,}99995$ y $\sigma'(10)\approx0{,}0000454$: lejos del origen, la función es casi horizontal, y las pequeñas variaciones de la entrada apenas llegan ya a la salida.
::::

⁠**En resumen:** La función logística $\sigma(x)=1/(1+\mathrm{e}^{-x})$ lleva cada número, de forma suave, al intervalo entre $0$ y $1$; su derivada es $\sigma(1-\sigma)$, vale como máximo $\tfrac14$ y puede calcularse solo a partir del valor de la función.

:::aufgabe Ejercicio 5 ★ Curva de campana
<span class="anker" id="aufg-5"></span>

Sea $f(x)=\mathrm{e}^{-x^2}$.

<ol class="al">

<li>

Determina la función interior y la exterior y calcula $f'(x)$.

</li>

<li>

Calcula $f'(0)$, $f'(1)$ y $f'(-1)$ e interpreta los signos en la gráfica.

</li>

</ol>

:::loesung
(a) La función interior es $u=-x^2$, con $u'=-2x$, y la exterior, $\mathrm{e}^u$, con la derivada $\mathrm{e}^u$. Según la regla de la cadena, $f'(x)=\mathrm{e}^{-x^2}\cdot(-2x)=-2x\,\mathrm{e}^{-x^2}$.

(b) $f'(0)=0$: la gráfica tiene en el punto $0$ una recta tangente horizontal; allí está su cima. $f'(1)=-2/\mathrm{e}\approx-0{,}7358$: a la derecha de la cima, la gráfica baja. $f'(-1)=2/\mathrm{e}\approx0{,}7358$: a la izquierda de la cima, sube. Como $f(-x)=f(x)$, las pendientes en los puntos $\pm1$ son iguales y de signo contrario.
:::
:::

:::aufgabe Ejercicio 6 ★★ Una cadena de tres eslabones
<span class="anker" id="aufg-6"></span>

Sea $y=\sqrt{1+x^4}$.

<ol class="al">

<li>

Descompón la función en tres eslabones $u_1$, $u_2$, $y$ y calcula en el punto $x=1$ primero todos los valores intermedios y después todos los factores.

</li>

<li>

Calcula $\frac{\mathrm{d} y}{\mathrm{d} x}$ en el punto $1$ como producto de los factores y compruébalo con la regla de la cadena en un solo paso.

</li>

</ol>

:::loesung
(a) Los eslabones son $u_1=x^4$, $u_2=1+u_1$ e $y=\sqrt{u_2}$. En el punto $1$, los valores intermedios son $u_1=1$, $u_2=2$ e $y=\sqrt2\approx1{,}4142$. Los factores son $\frac{\mathrm{d} u_1}{\mathrm{d} x}=4x^3=4$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=1$ y $\frac{\mathrm{d} y}{\mathrm{d} u_2}=\frac1{2\sqrt{u_2}}=\frac1{2\sqrt2}\approx0{,}3536$.

(b) El producto es $4\cdot1\cdot\frac1{2\sqrt2}=\frac2{\sqrt2}=\sqrt2\approx1{,}4142$. En un solo paso: $y'=\frac1{2\sqrt{1+x^4}}\cdot4x^3$; en el punto $1$, por tanto, $\frac4{2\sqrt2}=\sqrt2$.
:::
:::

:::aufgabe Ejercicio 7 ★★ Propiedades de la función logística
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Demuestra con [(2.4)](#gl-2-4) y $\sigma(-x)=1-\sigma(x)$ que $\sigma'(-x)=\sigma'(x)$. ¿Qué significa esto para la gráfica de $\sigma'$?

</li>

<li>

Calcula $\sigma(1)$ y $\sigma'(1)$ con cuatro decimales.

</li>

<li>

Calcula la segunda derivada $\sigma''$, expresada mediante $\sigma$, y determina su signo para $x>0$ y para $x<0$. ¿Qué dice eso sobre la curvatura de la gráfica de $\sigma$?

</li>

</ol>

:::loesung
(a) Con $\sigma(-x)=1-\sigma(x)$ se tiene $\sigma'(-x)=\sigma(-x)\,\bigl(1-\sigma(-x)\bigr)=\bigl(1-\sigma(x)\bigr)\,\sigma(x)=\sigma'(x)$. La gráfica de $\sigma'$ es simétrica respecto del eje vertical, como muestra la fig. [5](#abb-5).

(b) $\mathrm{e}^{-1}\approx0{,}3679$, así que $\sigma(1)=1/1{,}3679\approx0{,}7311$ y $\sigma'(1)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$.

(c) Con la regla del producto y la regla de la cadena: $\sigma''=(\sigma-\sigma^2)'=\sigma'-2\sigma\sigma'=\sigma'\,(1-2\sigma)=\sigma(1-\sigma)(1-2\sigma)$. Para $x>0$ se tiene $\sigma>\tfrac12$, así que $1-2\sigma<0$ y $\sigma''<0$: allí la gráfica se curva hacia abajo. Para $x<0$ se tiene $\sigma''>0$, y la gráfica se curva hacia arriba. En el punto $0$, la curvatura cambia de signo; allí la pendiente es máxima.
:::
:::

:::aufgabe Ejercicio 8 ★★★ La derivada de una función inversa
<span class="anker" id="aufg-8"></span>

Para $x>0$ se cumple $\mathrm{e}^{\ln x}=x$.

<ol class="al">

<li>

Deriva ambos lados respecto de $x$ con la regla de la cadena y deduce $(\ln x)'=1/x$, suponiendo que $\ln$ es derivable.

</li>

<li>

Procede del mismo modo con $(\sqrt x)^2=x$ y compara con la regla de la potencia.

</li>

<li>

La función inversa de la función logística es $\ell(p)=\ln\frac{p}{1-p}$ para $0<p<1$. Comprueba $\ell(\sigma(x))=x$ y calcula $\ell'(p)$ una vez directamente y otra a través de $\sigma'$.

</li>

</ol>

:::loesung
(a) El lado izquierdo es una composición con la función interior $\ln x$ y la exterior $\mathrm{e}^u$. Según la regla de la cadena, su derivada es $\mathrm{e}^{\ln x}\cdot(\ln x)'=x\cdot(\ln x)'$. El lado derecho tiene la derivada $1$. Por tanto, $x\,(\ln x)'=1$ y $(\ln x)'=1/x$.

(b) De $(\sqrt x)^2=x$ se sigue $2\sqrt x\cdot(\sqrt x)'=1$, es decir, $(\sqrt x)'=\frac1{2\sqrt x}=\tfrac12x^{-1/2}$: exactamente la regla de la potencia con $n=\tfrac12$.

(c) Se tiene $1-\sigma(x)=\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}}$, así que $\frac{\sigma(x)}{1-\sigma(x)}=\frac1{\mathrm{e}^{-x}}=\mathrm{e}^x$ y $\ell(\sigma(x))=\ln\mathrm{e}^x=x$. Directamente, $\ell(p)=\ln p-\ln(1-p)$ y

$$\ell'(p)=\frac1p+\frac1{1-p}=\frac{1}{p\,(1-p)} .$$

A través de $\sigma'$: derivar $\ell(\sigma(x))=x$ da $\ell'(\sigma(x))\cdot\sigma'(x)=1$, es decir, $\ell'(p)=\frac1{\sigma'(x)}=\frac1{p(1-p)}$ con $p=\sigma(x)$. Donde $\sigma$ es plana, su función inversa es empinada.
:::
:::
