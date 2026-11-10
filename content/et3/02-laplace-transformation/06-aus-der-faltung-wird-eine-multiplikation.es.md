---
title: Etapa 3: La convolución se vuelve una multiplicación
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Transformada de Laplace
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Capítulo 2: Transformada de Laplace
order: 3220600
summary: La etapa 1 dice qué hace el sistema con un bloque elemental.
tags: 
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
La etapa [1](warum-gerade.html#stufe-1) dice qué hace el sistema con un bloque elemental. La etapa [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) dice que toda señal está formada por bloques elementales. Juntas dan el teorema más importante de la transformada de Laplace.
:::

**La idea.** Un sistema LTI es lineal: procesa cada bloque elemental de la entrada por separado y suma los resultados. Cada bloque $\mathrm{e}^{pt}$ lo multiplica por $H(p)$. La salida consta, pues, de los *mismos* bloques que la entrada; solo que cada peso está multiplicado por $H(p)$. La figura [4](#abb-4) muestra los dos caminos hacia la salida.

:::abbildung et3/k2wege 4
Dos caminos de la entrada a la salida. Arriba, directamente con la integral de convolución. Abajo: descomponer la entrada en bloques elementales, multiplicar cada peso por $H(p)$ y recomponer. El camino de abajo funciona porque cada bloque elemental es una función propia.
:::

:::satz Teorema 3.1 (Teorema de convolución)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$g(t)=s(t)*h(t)\quad\Longleftrightarrow\quad G(p)=S(p)\,H(p), \tag{3.1}$$

válido para todo $p$ que esté en las regiones de convergencia de $S$ y de $H$.
:::

⁠**Cómo leerlo:** $S(p)$ es el peso del bloque elemental $\mathrm{e}^{pt}$ en la entrada; $H(p)$, el factor por el que el sistema multiplica ese bloque; $G(p)$, el peso en la salida. La condición sobre $p$ se debe a que la recta de la fórmula de inversión tiene que pasar por ambas regiones de convergencia: la entrada debe poder descomponerse en bloques elementales, y el sistema debe poder procesar cada uno de ellos.

:::herleitung teorema de convolución a partir de la superposición y la función propia
Se introduce la entrada como superposición [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) en la convolución, con una recta $\operatorname{Re} p=\sigma$ que esté en ambas regiones de convergencia:

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

Linealidad: la convolución puede entrar en la integral; actúa sobre cada bloque elemental por separado:

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

Función propia [(1.1)](warum-gerade.html#gl-1-1): $\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$.

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[S(p)H(p)\bigr]\,\mathrm{e}^{pt}\,\mathrm{d} p.$$

Es la fórmula de inversión para $g$ con el peso $S(p)H(p)$. Como los pesos de una señal son únicos, $G(p)=S(p)H(p)$.
:::

⁠**En resumen:** la convolución se convierte en multiplicación porque el sistema solo multiplica cada bloque elemental $\mathrm{e}^{pt}$ por el número $H(p)$.

:::analogie
Un ecualizador gráfico descompone la música en bandas de frecuencia, multiplica cada banda por la posición de su control y vuelve a juntar las bandas. Un sistema LTI hace lo mismo con los bloques elementales $\mathrm{e}^{pt}$, y la posición del control es $H(p)$. La analogía falla en dos puntos: un ecualizador gráfico tiene un número finito de bandas con controles reales. Aquí hay un continuo de bloques elementales, que además pueden crecer o decaer, y cada «control» es un número complejo que, además, desplaza la fase.
:::

**El mismo mecanismo explica la derivada, la integral y las ecuaciones diferenciales.**

<ul>

<li>

⁠**Derivar.** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$. El derivador es un sistema LTI, y cada bloque elemental es función propia suya con el valor propio $p$. Por tanto, cada peso se multiplica por $p$: $\mathcal{L}\{\dot s\}=p\,S(p)$.

</li>

<li>

⁠**Integrar.** $\int_{-\infty}^{t}\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$, pero solo para $\operatorname{Re} p>0$; si no, la integral diverge en $-\infty$. Por tanto, $\mathcal{L}\{\int_{-\infty}^t s\,\mathrm{d}\tau\}=S(p)/p$ con la condición adicional $\operatorname{Re} p>0$.

</li>

<li>

⁠**Cascada.** Dos sistemas en serie multiplican sucesivamente por $H_1(p)$ y $H_2(p)$, y en conjunto por $H_1H_2$. El orden da igual porque los números conmutan.

</li>

<li>

⁠**Ecuación diferencial.** Cada derivada se convierte en un factor $p$. Una ecuación diferencial lineal con coeficientes constantes

$$\sum_{r=0}^{R}\alpha_r\frac{\mathrm{d}^r g}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\frac{\mathrm{d}^q s}{\mathrm{d} t^q} \quad\text{se convierte en}\quad \Bigl(\sum_{r}\alpha_rp^r\Bigr)G(p)=\Bigl(\sum_q\beta_qp^q\Bigr)S(p),$$

es decir, en una ecuación algebraica, y $H(p)=G/S$ es un cociente de polinomios.

</li>

</ul>

**Ejemplo: la respuesta al escalón del filtro paso bajo RC.** Entrada $\varepsilon(t)$ con $S(p)=1/p$ ($\operatorname{Re} p>0$); sistema $H(p)=1/(p+1)$ ($\operatorname{Re} p>-1$). La región común es $\operatorname{Re} p>0$:

$$G(p)=\frac{1}{p}\cdot\frac{1}{p+1}=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

La transformada inversa de los dos sumandos se obtiene de [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) con $p_0=0$ y $p_0=-1$. Comprobación directa: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ para $t>0$. También la fórmula de inversión [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1), evaluada numéricamente sobre la recta $\sigma=0{,}5/\mathrm s$, da $g(0{,}5\,\mathrm{s})=0{,}3935$, $g(1\,\mathrm{s})=0{,}6321$, $g(3\,\mathrm{s})=0{,}9502$ y $g(-1\,\mathrm{s})=0$, exactamente $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$.

:::ltspice Introducir directamente la función de transferencia
⁠**Esquema:** el circuito RC (`1Meg`, `1u`) de `in` a `rc`. Al lado, una fuente de tensión controlada por tensión `e`: entrada de control en `in` y masa, salida en el nodo `lap`, valor `Laplace=1/(1+s)`. Esta fuente es un sistema LTI dado solo por $H$: a partir de $H$, LTspice calcula por sí mismo la respuesta al impulso y convoluciona la entrada con ella. LTspice escribe $s$ en lugar de $p$.

⁠**Fuente y directiva:** `PULSE(0 1 0 1u 1u 100)`, `.tran 0 5 0 1m`.

⁠**Lo que ves:** `V(rc)` y `V(lap)` quedan superpuestas (diferencia inferior a 0,001), con 0,3935 en 0,5 s, 0,6321 en 1 s y 0,9502 en 3 s. Con el valor de fuente `AC 1` y `.ac dec 100 0.01 100`, LTspice muestra $H(s)$ para $s=\mathrm{j}2\pi f$, es decir, solo sobre el eje imaginario: $-3{,}0$ dB y $-45^\circ$ en 0,159 Hz.

⁠**Para el ejercicio [6](#aufg-6):** fuente `PWL(0 0 10 10)`, la rampa $t\,\varepsilon(t)$ hasta 10 s, y `.tran 0 10 0 1m`. Compara `V(rc)` con tu resultado del ejercicio [6](#aufg-6)(b).
:::

:::aufgabe Ejercicio 5 ★★ Cascada y derivada a través de los bloques elementales
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Justifica con la imagen de los bloques elementales (sin la integral de convolución) por qué dos sistemas LTI en cascada tienen la función de transferencia $H_1(p)H_2(p)$. ¿Por qué se deduce de ello que la convolución es conmutativa?

</li>

<li>

Deduce $\mathcal{L}\{\dot s(t)\}=p\,S(p)$ a partir de la fórmula de inversión derivándola respecto a $t$.

</li>

</ol>

:::loesung
(a) La entrada consta de bloques elementales $\mathrm{e}^{pt}$ con pesos $S(p)$. El primer sistema multiplica cada bloque por $H_1(p)$; después, los pesos son $H_1S$. El segundo multiplica por $H_2(p)$: $G=H_2H_1S$. Así pues, la cascada tiene $H=H_1H_2$. Como $H_1H_2=H_2H_1$, el resultado no depende del orden, y como $h_1*h_2$ es la respuesta al impulso de la cascada, se deduce que $h_1*h_2=h_2*h_1$.

(b) Derivar bajo la integral solo actúa sobre $\mathrm{e}^{pt}$:

$$\dot s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}\,\mathrm{d} p=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[p\,S(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p.$$

Es la fórmula de inversión con el peso $pS(p)$; por tanto, $\mathcal{L}\{\dot s\}=pS(p)$.
:::
:::

:::aufgabe Ejercicio 6 ★★ Respuesta a la rampa del filtro paso bajo RC
<span class="anker" id="aufg-6"></span>

Entrada $s(t)=t\,\varepsilon(t)$ con $S(p)=1/p^2$ para $\operatorname{Re} p>0$, par básico [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5).

<ol class="al">

<li>

Determina $G(p)$ y su región de convergencia.

</li>

<li>

Comprueba la descomposición $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$ y determina $g(t)$.

</li>

<li>

Control: ¿cuánto vale $g(0)$ y por qué tiene que ser así? ¿Cuánto vale $\dot g(t)$?

</li>

<li>

¿Cómo se comporta $g(t)$ para $t\gg1$ s? Compáralo con el ejercicio [1](warum-gerade.html#aufg-1)c.

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ para $\operatorname{Re} p>0$ (intersección de $\operatorname{Re} p>0$ y $\operatorname{Re} p>-1$).

(b) Con denominador común: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Transformada inversa con [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5) y [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$: la tensión del condensador no puede saltar, y la entrada empieza en cero. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, exactamente la respuesta al escalón. Encaja: la rampa es la integral del escalón; por tanto, la respuesta a la rampa es la integral de la respuesta al escalón.

(d) Para $t\gg1$ s, $\mathrm{e}^{-t}\approx0$ y $g(t)\approx t-1$: la salida sigue a la rampa con un retardo de $RC=1$ s, igual que con la rampa bilateral del ejercicio [1](warum-gerade.html#aufg-1)c. La diferencia es el bloque elemental $\mathrm{e}^{-t}$ (polo $-1$ del sistema): el transitorio, porque aquí la rampa solo empieza en $t=0$.
:::
:::
