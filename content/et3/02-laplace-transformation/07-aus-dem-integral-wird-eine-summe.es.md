---
title: Etapa 4: La integral se convierte en una suma
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220700
summary: La suposición, al pie de la letra: para las señales de las que casi siempre se trata en teoría de sistemas, la señal es una suma finita de exponenciales complejas.
tags: descomposición en fracciones parciales, estabilidad, respuesta natural
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
La suposición, al pie de la letra: para las señales de las que casi siempre se trata en teoría de sistemas, la señal es una *suma finita* de exponenciales complejas. Los polos son los exponentes.
:::

**La idea.** En redes de $R$, $L$, $C$ y en todos los sistemas descritos por una ecuación diferencial, $S(p)$ es un cociente de polinomios. La __descomposición en fracciones parciales__ lo escribe, si los polos son simples, como

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

Cada sumando es la transformada de *un único bloque elemental*: según [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2), $A_r/(p-p_r)$ corresponde a $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$ si la región de convergencia está a la derecha del polo, y el sumando constante $A_0$ corresponde, según [(2.4)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-4), a $A_0\,\delta(t)$. Para una señal por la derecha se tiene, por tanto,

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**En resumen:** una señal por la derecha con transformada de Laplace racional es una suma finita de bloques elementales $\mathrm{e}^{p_r t}$. Los polos son los exponentes; los coeficientes de las fracciones parciales, los pesos.

Así, toda señal de este tipo puede leerse en sus polos, con el mapa de la figura [1](warum-gerade.html#abb-1): $\operatorname{Re} p_r$ dice si el bloque decae o crece, y $\operatorname{Im} p_r$, con qué rapidez oscila. Un par de polos conjugados $p_r,p_r^*$ da en conjunto una oscilación real amortiguada. Aquí está también el núcleo de la __estabilidad__: un bloque causal $\mathrm{e}^{p_r t}\varepsilon(t)$ decae si y solo si $\operatorname{Re} p_r<0$. Por eso un sistema causal es estable si todos los polos de $H(p)$ están en el semiplano izquierdo.

**Ejemplo.** La respuesta al escalón de la etapa [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) tiene los polos $0$ y $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{polo }0\text{ (de }S)}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{polo }-1\text{ (de }H)}\qquad(t>0).$$

El polo de la entrada aporta la parte que impone la entrada (la tensión final 1). El polo del sistema aporta la __respuesta natural__ del circuito RC, el decaimiento con $RC=1$ s. Esto vale en general: en la salida $G=SH$ están los polos de la entrada y los polos del sistema.

:::zusatz por qué la integral se reduce a una suma: el teorema de los residuos
Este apartado necesita el teorema de los residuos del análisis complejo. Explica por qué [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) y [(4.1)](#gl-4-1) son lo mismo y por qué la región de convergencia decide cuál es la señal.

Sea $S(p)$ un cociente de polinomios con grado del numerador menor que el del denominador y con polos simples.

<ul>

<li>

⁠**$t>0$:** se cierra la recta de integración con un gran semicírculo hacia la *izquierda*. Allí $\operatorname{Re} p\to-\infty$, por lo que $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$, y $S(p)\to0$. En el límite, el semicírculo no aporta nada (lema de Jordan). El camino cerrado se recorre en sentido antihorario, y el teorema de los residuos da

$$s(t)=\sum_{\text{polos a la izquierda de la recta}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{izquierda}}A_r\,\mathrm{e}^{p_r t}.$$

El residuo en un polo simple es $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$: exactamente el coeficiente de la fracción parcial.

</li>

<li>

⁠**$t<0$:** ahora $\mathrm{e}^{pt}$ se anula para $\operatorname{Re} p\to+\infty$. Se cierra hacia la *derecha*; el camino se recorre en sentido horario, lo que da un signo menos:

$$s(t)=-\sum_{\text{polos a la derecha de la recta}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**Consecuencia:** la posición de la recta, es decir, la región de convergencia, decide qué polos dan bloques causales (a la izquierda de la recta) y cuáles anticausales (a la derecha de la recta). Ejemplo: $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ (fig. [5](#abb-5)). Si la recta está entre los polos, $-2<\sigma<-1$, actúa $-2$ para $t>0$ y $-1$ para $t<0$:

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

Evaluado numéricamente sobre la recta $\sigma=-1{,}5/\mathrm s$: $s(1\,\mathrm{s})=-0{,}1353=-\mathrm{e}^{-2}$ y $s(-1\,\mathrm{s})=-2{,}7183=-\mathrm{e}^{1}$. Si la recta está a la derecha de ambos polos, la misma fórmula da la señal causal $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$; si está a la izquierda de ambos, la anticausal $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$.

:::abbildung et3/k2residuen 5
Recta de integración $\sigma=-1{,}5/\mathrm s$ en la franja $-2<\operatorname{Re} p<-1$ (azul) y los semicírculos con los que se cierra (rojo).
:::
:::

:::aufgabe Ejercicio 7 ★★★ (Para profundizar) La misma fórmula, dos señales
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$.

<ol class="al">

<li>

Región de convergencia $\operatorname{Re} p>-1$. Evalúa la fórmula de inversión con el teorema de los residuos, por separado para $t>0$ y $t<0$.

</li>

<li>

Lo mismo para la región de convergencia $\operatorname{Re} p<-1$.

</li>

<li>

Compara con los pares básicos [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) y [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3). ¿Qué aprendes de ello sobre el dato «$S(p)=1/(p+1)$» sin región de convergencia?

</li>

</ol>

:::loesung
(a) Recta a la derecha del polo, por ejemplo $\sigma=0$. Para $t>0$, se cierra por la izquierda: el polo $-1$ queda dentro, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, luego $s(t)=\mathrm{e}^{-t}$. Para $t<0$, se cierra por la derecha: a la derecha de la recta no hay ningún polo, $s(t)=0$. En conjunto, $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Recta a la izquierda del polo, por ejemplo $\sigma=-2$. Para $t>0$, se cierra por la izquierda: ningún polo, $s(t)=0$. Para $t<0$, se cierra por la derecha: el polo queda dentro, recorrido en sentido horario, $s(t)=-\mathrm{e}^{-t}$. En conjunto, $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) Son exactamente los pares básicos [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) y [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3) con $p_0=-1$. El dato «$S(p)=1/(p+1)$» por sí solo no determina la señal. Solo con la región de convergencia está claro a qué lado de la recta está el polo y si da un bloque elemental causal o uno anticausal.
:::
:::

:::frage ¿Hay detrás de la transformada de Laplace algo más que el cálculo que lleva de la integral de convolución con una función propia a $H(p)$, a saber, que cualquier función puede representarse como suma de exponenciales complejas?
Sí, y eso es justamente lo esencial. Sin ella, el cálculo con la función propia sería solo una curiosidad, porque en principio vale únicamente para la señal $\mathrm{e}^{pt}$. Solo porque (casi) toda señal puede componerse de tales bloques elementales se deduce de él una afirmación sobre *cualquier* señal de entrada. Tres precisiones hacen exacta la afirmación:

<ol>

<li>

En general no es una suma, sino una *integral*: infinitos bloques elementales $\mathrm{e}^{pt}$, cada uno con un peso infinitesimal. Los bloques están sobre una recta vertical $\operatorname{Re} p=\sigma$ del plano $p$ (etapa [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)).

</li>

<li>

No cualquier función, sino toda función para la que exista una región de convergencia: puede crecer como mucho exponencialmente a cada lado del eje temporal, y un único amortiguamiento debe dominar ambos lados a la vez (apartado [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)).

</li>

<li>

Si $S(p)$ es un cociente de polinomios, la integral se convierte realmente en una *suma finita* $\sum_r A_r\,\mathrm{e}^{p_r t}$. Los exponentes $p_r$ son los polos de $S(p)$ (etapa [4](#stufe-4)).

</li>

</ol>
:::
