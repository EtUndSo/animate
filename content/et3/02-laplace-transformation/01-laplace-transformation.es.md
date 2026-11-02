---
title: Visión general: La transformada de Laplace
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220100
summary: Toda señal como superposición de $\ee^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: 
lang: es
---

## De qué trata

:::frage He entendido el cálculo que lleva de la integral de convolución con una función propia a $H(p)$. Pero creo que detrás de la transformada de Laplace hay mucho más que esta regla de cálculo: que cualquier función puede representarse como suma de exponenciales complejas.
La suposición acierta en lo esencial. Sin ella, el cálculo con la función propia sería solo una curiosidad, porque en principio vale únicamente para la señal $\mathrm{e}^{pt}$. Solo porque (casi) toda señal puede componerse de tales bloques elementales se deduce de él una afirmación sobre *cualquier* señal de entrada. Tres precisiones hacen exacta la suposición:

<ol>

<li>

En general no es una suma, sino una *integral*: infinitos bloques elementales $\mathrm{e}^{pt}$, cada uno con un peso infinitesimal. Los bloques están sobre una recta vertical $\operatorname{Re} p=\sigma$ del plano $p$ (etapa [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)).

</li>

<li>

No cualquier función, sino toda función para la que exista una región de convergencia: puede crecer como mucho exponencialmente a cada lado del eje temporal, y un único amortiguamiento debe dominar ambos lados a la vez (apartado [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)).

</li>

<li>

Si $S(p)$ es un cociente de polinomios, la integral se convierte realmente en una *suma finita* $\sum_r A_r\,\mathrm{e}^{p_r t}$. Los exponentes $p_r$ son los polos de $S(p)$ (etapa [4](aus-dem-integral-wird-eine-summe.html#stufe-4)).

</li>

</ol>
:::



**Cómo trabajar con este capítulo.** Cada etapa es un artículo breve con la idea, preguntas típicas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio. Termina una etapa antes de pasar a la siguiente.

:::merke El modelo de cálculo de este capítulo
Todos los ejemplos usan los mismos dos componentes:

<ul>

<li>

un **filtro paso bajo RC** con $RC=1$ s (por ejemplo, $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Su respuesta al impulso y su función de transferencia son

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

con $t$ en s y $p$ en $1/\mathrm{s}$;

</li>

<li>

el **escalón unitario** $s(t)=\varepsilon(t)$ con $S(p)=1/p$ para $\operatorname{Re} p>0$.

</li>

</ul>

Los números y las curvas se comprueban con `rechnung_kap2.py`.
:::
