---
title: La transformada de Laplace
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220100
summary: Toda señal como superposición de $\ee^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: tasa de crecimiento, frecuencia, absolutamente integrable, densidad, descomposición en fracciones parciales, estabilidad, respuesta natural
lang: es
---

## De qué trata

:::frage He entendido el cálculo que lleva de la integral de convolución con una función propia a $H(p)$. Pero creo que detrás de la transformada de Laplace hay mucho más que esta regla de cálculo: que cualquier función puede representarse como suma de exponenciales complejas.
La suposición acierta en lo esencial. Sin ella, el cálculo con la función propia sería solo una curiosidad, porque en principio vale únicamente para la señal $\mathrm{e}^{pt}$. Solo porque (casi) toda señal puede componerse de tales bloques elementales se deduce de él una afirmación sobre *cualquier* señal de entrada. Tres precisiones hacen exacta la suposición:

<ol>

<li>

En general no es una suma, sino una *integral*: infinitos bloques elementales $\mathrm{e}^{pt}$, cada uno con un peso infinitesimal. Los bloques están sobre una recta vertical $\operatorname{Re} p=\sigma$ del plano $p$ (etapa [2](#stufe-2)).

</li>

<li>

No cualquier función, sino toda función para la que exista una región de convergencia: puede crecer como mucho exponencialmente a cada lado del eje temporal, y un único amortiguamiento debe dominar ambos lados a la vez (apartado [2.3](#stufe-2-3)).

</li>

<li>

Si $S(p)$ es un cociente de polinomios, la integral se convierte realmente en una *suma finita* $\sum_r A_r\,\mathrm{e}^{p_r t}$. Los exponentes $p_r$ son los polos de $S(p)$ (etapa [4](#stufe-4)).

</li>

</ol>
:::

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Un sistema LTI solo puede multiplicar el bloque elemental $\mathrm{e}^{pt}$ por un número $H(p)$, porque para $\mathrm{e}^{pt}$ desplazar es lo mismo que multiplicar.

</li>

<li>

Toda señal con región de convergencia es una superposición de tales bloques. $S(p)$ indica con qué peso está contenido el bloque $\mathrm{e}^{pt}$ en la señal.

</li>

<li>

Por eso la convolución se convierte en una multiplicación, $G(p)=H(p)\,S(p)$. Si $S(p)$ es racional, la señal es una suma finita $\sum_r A_r\mathrm{e}^{p_r t}$ con los polos como exponentes.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** Casi todos los resultados sobre la transformada de Laplace son consecuencia de estas tres frases. La tabla los relaciona; las etapas los explican.

| Resultado | De dónde viene |
|---|---|
| Función propia $\mathrm{e}^{pt}$, función de transferencia $H(p)$ | desplazar $\mathrm{e}^{pt}$ es multiplicar por $\mathrm{e}^{-p\tau}$ (etapa [1](#stufe-1)) |
| Transformada de Laplace $S(p)$ | peso del bloque elemental $\mathrm{e}^{pt}$ en la señal (etapa [2](#stufe-2)) |
| Región de convergencia | los amortiguamientos $\sigma$ con los que $s(t)\mathrm{e}^{-\sigma t}$ se vuelve absolutamente integrable (apartado [2.3](#stufe-2-3)) |
| Convolución $\to$ producto, conexión en cascada | cada bloque elemental se multiplica por $H(p)$ (etapa [3](#stufe-3)) |
| Derivada $\to p$, integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ y $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (etapa [3](#stufe-3)) |
| Ecuación diferencial $\to$ cociente de polinomios | cada derivada se convierte en un factor $p$ (etapa [3](#stufe-3)) |
| Polos, fracciones parciales | los exponentes y los pesos de un número finito de bloques elementales (etapa [4](#stufe-4)) |
| Estabilidad | un bloque causal $\mathrm{e}^{p_r t}$ solo decae si $\operatorname{Re} p_r<0$ (etapa [4](#stufe-4)) |
| Transformada de Fourier | la misma superposición sobre la recta $\sigma=0$ (etapa [2](#stufe-2)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de cálculo de este artículo
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

## Etapa 1: Por qué precisamente $\mathrm{e}^{pt}$

<span class="anker" id="stufe-1"></span>

:::zweck
Si se introduce $\mathrm{e}^{pt}$ en la integral de convolución, se obtiene $H(p)\,\mathrm{e}^{pt}$: $\mathrm{e}^{pt}$ es una función propia. Aquí se trata de ver qué propiedad de $\mathrm{e}^{pt}$ obliga a ello y por qué los bloques elementales tienen que ser complejos.
:::

**La idea.** La integral de convolución

$$g(t)=\int_{-\infty}^{\infty}h(\tau)\,s(t-\tau)\,\mathrm{d}\tau$$

se lee así: la salida es una suma de *copias retardadas* de la entrada. La copia con retardo $\tau$ entra con el peso $h(\tau)\,\mathrm{d}\tau$. Con una forma de señal cualquiera, cada copia retardada tiene un aspecto distinto del original, y la suma tiene una forma nueva. Con $\mathrm{e}^{pt}$, no:

$$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\cdot\mathrm{e}^{pt}.$$

El retardo $\tau$ actúa como la multiplicación por el *número constante* $\mathrm{e}^{-p\tau}$. Todas las copias son múltiplos de la misma función $\mathrm{e}^{pt}$, y por tanto también lo es su suma:

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{pt}*h(t)=\mathrm{e}^{pt}\underbrace{\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau}_{H(p)}=H(p)\,\mathrm{e}^{pt}. \tag{1.1}$$

⁠**En resumen:** $\mathrm{e}^{pt}$ es una función propia porque, para $\mathrm{e}^{pt}$, desplazar es lo mismo que multiplicar.

**Qué significa $p$.** Con $p=\sigma+\mathrm{j}2\pi f$, el bloque elemental se descompone en dos factores:

$$\mathrm{e}^{pt}=\mathrm{e}^{\sigma t}\cdot\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{e}^{\sigma t}\bigl[\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)\bigr].$$

La parte real $\sigma$ (en $1/\mathrm s$) es la __tasa de crecimiento__: para $\sigma<0$ el bloque decae, para $\sigma=0$ oscila con amplitud constante y para $\sigma>0$ crece. La parte imaginaria $2\pi f$ fija la __frecuencia__ de la oscilación. Cada punto del plano $p$ es, por tanto, un bloque elemental, y la posición del punto dice qué aspecto tiene (fig. [1](#abb-1)).

:::abbildung et3/k2bausteine
El plano $p$ como mapa de los bloques elementales. A la izquierda, cuatro puntos $p$; a la derecha, para cada uno, la parte real $\operatorname{Re}\{\mathrm{e}^{pt}\}=\mathrm{e}^{\sigma t}\cos(2\pi ft)$ con la envolvente $\pm\mathrm{e}^{\sigma t}$ (a trazos). Los puntos b, c, d tienen $2\pi f=\pi/\mathrm s$, es decir, $f=0{,}5$ Hz. La distancia al eje imaginario determina si el bloque decae o crece; la altura, la frecuencia.
:::

:::frage ¿Por qué complejos? Un seno también es una señal sencilla.
Al desplazar un seno, no solo se escala. Con $\omega_0=2\pi f_0$ se cumple

$$\sin\bigl(\omega_0(t-\tau)\bigr)=\cos(\omega_0\tau)\,\sin(\omega_0t)-\sin(\omega_0\tau)\,\cos(\omega_0t).$$

Aparece un término en coseno: la copia retardada tiene otra forma. Por eso un sistema responde a $\sin(\omega_0t)$ con $|H|\sin(\omega_0t+\varphi)$: cambian la amplitud *y la fase*. Un desfase no puede escribirse como multiplicación por un número real, pero sí como multiplicación por el número complejo $\mathrm{e}^{\mathrm{j}\varphi}$. Por eso los bloques elementales son complejos: un solo número $H(p)$ lleva el módulo y la fase. Un seno real consta de dos bloques, $\sin(\omega_0t)=\bigl(\mathrm{e}^{\mathrm{j}\omega_0t}-\mathrm{e}^{-\mathrm{j}\omega_0t}\bigr)/(2\mathrm{j})$, y cada uno se multiplica por su propio número (ejercicio [1](#aufg-1)d).
:::

:::frage ¿Por qué $\mathrm{e}^{pt}$ es función propia de *todo* sistema LTI, aunque los sistemas sean tan distintos?
La forma de la función propia se deduce solo de la invariancia temporal (desplazar = multiplicar), y esta la tienen en común todos los sistemas LTI. Del sistema solo depende el factor $H(p)$, porque en él intervienen los pesos $h(\tau)$. Por eso *un mismo* conjunto de bloques elementales sirve a la vez para todos los sistemas LTI. Esto hace universal la transformada de Laplace.
:::

:::zusatz solo las funciones exponenciales tienen esta propiedad
Se busca una función derivable $x(t)$ con $x(0)=1$ cuyas copias desplazadas sean múltiplos de ella misma: $x(t+u)=c(u)\,x(t)$ para todo $t,u$. Con $t=0$ se obtiene $c(u)=x(u)$, es decir, $x(t+u)=x(t)\,x(u)$. Derivando respecto a $u$ en el punto $u=0$ resulta $x'(t)=x'(0)\,x(t)$. Es la ecuación diferencial $x'=p\,x$ con $p=x'(0)$, y su solución con $x(0)=1$ es $x(t)=\mathrm{e}^{pt}$. Por tanto, no hay otros bloques elementales con esta propiedad.
:::

:::frage ¿Son las funciones exponenciales las únicas funciones propias posibles de los sistemas LTI?
Hay que separar dos preguntas.

⁠**Función propia de *todos* los sistemas LTI a la vez: sí, solo $c\,\mathrm{e}^{pt}$.** El elemento de retardo ideal $g(t)=s(t-u)$ es él mismo un sistema LTI, para cualquier retardo $u$. Una función que sea función propia de todo sistema LTI debe, por tanto, convertirse en un múltiplo de sí misma con cualquier desplazamiento. Según el recuadro anterior, eso solo lo cumple $\mathrm{e}^{pt}$.

⁠**Función propia de un sistema *concreto*: no solo.** El sistema multiplica cada bloque elemental $\mathrm{e}^{p_kt}$ por su propio número $H(p_k)$. Una suma $\sum_kc_k\mathrm{e}^{p_kt}$ sigue siendo un múltiplo de sí misma exactamente cuando todos esos factores son iguales, $H(p_k)=\lambda$. El factor común $\lambda$ es entonces el valor propio. Dos ejemplos:

<ul>

<li>

Elemento de retardo ideal de $T$: $H(p)=\mathrm{e}^{-pT}$ tiene el mismo valor 1 en todos los puntos $p_k=\mathrm{j}2\pi k/T$. Toda señal de periodo $T$ es una función propia con valor propio 1, porque $s(t-T)=s(t)$.

</li>

<li>

Paso bajo ideal sin retardo, $H(f)=1$ en toda la banda de paso: toda señal cuyo espectro esté por completo dentro de la banda de paso sale sin cambios y es una función propia con valor propio 1.

</li>

</ul>

En el circuito RC, en cambio, $H(p)=1/(1+pRC)$ toma cada valor una sola vez. Allí las $c\,\mathrm{e}^{pt}$ individuales (con $p$ en la región de convergencia) son las únicas funciones propias que pueden formarse con bloques elementales.

⁠**En resumen:** $\mathrm{e}^{pt}$ es la única función propia que tiene *todo* sistema LTI. Un sistema concreto puede tener además mezclas de bloques elementales como funciones propias, si multiplica todos esos bloques por el mismo número.
:::

:::ltspice Una función propia en el experimento
⁠**Esquema:** circuito RC (`res` con `1Meg` de `in` a `out`, `cap` con `1u` a masa). Como fuente, una fuente de comportamiento `bv` con `V=exp(-time/2)`, el bloque elemental con $p=-0{,}5/\mathrm s$.

⁠**Directivas:** `.tran 0 10 0 1m` y `.ic V(out)=X`, con un número en lugar de $X$: el condensador empieza con $X$ voltios. Con «Add Traces», haz que se dibuje la expresión `V(out)/V(in)`.

⁠**Lo que ves:** si para $X$ tomas el valor que tiene en $t=0$ tu resultado del ejercicio [1](#aufg-1)(b), el cociente es constante desde el principio: la salida es un número por la entrada. Con $X=0$, el cociente solo se acerca a ese mismo número al cabo de unos segundos. La razón: una entrada aplicada desde siempre habría cargado el condensador en $t=0$ exactamente a ese valor. Cualquier otra tensión inicial la reduce el circuito RC con $\mathrm{e}^{-t}$, más deprisa de lo que decae la entrada con $\mathrm{e}^{-t/2}$.

⁠**Para (d):** fuente `voltage` con `SINE(0 1 {1/(2*pi)} 0 0 90)`, que es $\cos t$. Compara la amplitud y el retraso de `V(out)` tras el transitorio con tu resultado del ejercicio [1](#aufg-1)(d).
:::

:::aufgabe Ejercicio 1 ★ ¿Función propia o no?
<span class="anker" id="aufg-1"></span>

Usa el filtro paso bajo RC del modelo de cálculo, $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Calcula $H(p)=\int h(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. ¿Para qué $p$ converge la integral y por qué depende solo de $\operatorname{Re} p$?

</li>

<li>

Entrada $s(t)=\mathrm{e}^{-t/2}$ para todo $t$. Calcula la salida una vez directamente con la integral de convolución y otra vez con $H(p)$. ¿Qué $p$ tiene este bloque elemental?

</li>

<li>

Entrada $s(t)=t$ para todo $t$. Demuestra con la integral de convolución que se obtiene $g(t)=t-1$. ¿Por qué $t$ no es una función propia, aunque la salida se parezca? ¿Qué significa el $-1$ para el condensador?

</li>

<li>

Entrada $s(t)=\cos t$ (es decir, $\omega_0=1/\mathrm s$). Descompón el coseno en dos bloques elementales, multiplica cada uno por su $H(p)$ y vuelve a componerlos. Demuestra que $g(t)=A\cos(t+\varphi)$ y determina $A$ y $\varphi$. ¿Es $\cos t$ una función propia?

</li>

</ol>

⁠*Pista para (c):* $\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau=1$ y $\int_0^\infty\tau\,\mathrm{e}^{-\tau}\mathrm{d}\tau=1$.

:::loesung
(a) $H(p)=\int_0^\infty\mathrm{e}^{-\tau}\mathrm{e}^{-p\tau}\mathrm{d}\tau=\int_0^\infty\mathrm{e}^{-(p+1)\tau}\mathrm{d}\tau=\dfrac{1}{p+1}$. La integral converge si y solo si $|\mathrm{e}^{-(p+1)\tau}|=\mathrm{e}^{-(\sigma+1)\tau}$ decae, es decir, para $\operatorname{Re} p>-1$. El módulo depende solo de $\sigma$ porque $|\mathrm{e}^{-\mathrm{j}2\pi f\tau}|=1$.

(b) Directamente:

$$g(t)=\int_0^\infty\mathrm{e}^{-\tau}\,\mathrm{e}^{-(t-\tau)/2}\mathrm{d}\tau=\mathrm{e}^{-t/2}\int_0^\infty\mathrm{e}^{-\tau/2}\mathrm{d}\tau=2\,\mathrm{e}^{-t/2}.$$

Con $H(p)$: el bloque elemental tiene $p=-\tfrac12$ (real, sin oscilación). Este valor está en la región de convergencia, $H(-\tfrac12)=1/(\tfrac12)=2$, luego $g(t)=2\,\mathrm{e}^{-t/2}$. Ambos caminos coinciden (numéricamente: $g(1\,\mathrm{s})=1{,}2131$).

(c) $g(t)=\int_0^\infty\mathrm{e}^{-\tau}(t-\tau)\mathrm{d}\tau=t\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau-\int_0^\infty\tau\mathrm{e}^{-\tau}\mathrm{d}\tau=t-1$. Esto no es un múltiplo de $t$: las copias retardadas $t-\tau$ no son múltiplos de $t$ (el factor $1-\tau/t$ depende del propio $t$). La salida es la rampa *desplazada*: la tensión del condensador sigue a la rampa de entrada con un retardo de $RC=1$ s. Misma forma, pero desplazada en lugar de escalada; por tanto, no es función propia.

(d) $\cos t=\tfrac12\mathrm{e}^{\mathrm{j} t}+\tfrac12\mathrm{e}^{-\mathrm{j} t}$, bloques elementales en $p=\pm\mathrm{j}$, ambos en la región de convergencia ($\operatorname{Re} p=0>-1$).

$$H(\mathrm{j})=\frac{1}{1+\mathrm{j}}=\frac{1}{\sqrt2}\,\mathrm{e}^{-\mathrm{j}\pi/4},\qquad H(-\mathrm{j})=H(\mathrm{j})^*=\frac{1}{\sqrt2}\,\mathrm{e}^{+\mathrm{j}\pi/4}.$$

$$g(t)=\tfrac12H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}+\tfrac12H(-\mathrm{j})\mathrm{e}^{-\mathrm{j} t}=\operatorname{Re}\bigl\{H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}\bigr\}=\frac{1}{\sqrt2}\cos\Bigl(t-\frac\pi4\Bigr).$$

Así pues, $A=1/\sqrt2\approx0{,}707$ y $\varphi=-45^\circ$ (numéricamente: $g(1\,\mathrm{s})=0{,}6909$). Cada uno de los dos bloques complejos es una función propia; su suma $\cos t$, no: los dos bloques se multiplican por números *distintos*, $H(\mathrm{j})\neq H(-\mathrm{j})$. Por eso se desplaza la fase.
:::
:::

## Etapa 2: Una señal hecha solo de bloques elementales

<span class="anker" id="stufe-2"></span>

:::zweck
La etapa [1](#stufe-1) vale para un solo bloque elemental. Solo resulta útil si toda señal puede componerse de bloques $\mathrm{e}^{pt}$. Esta etapa muestra que es posible, cómo se llaman los pesos y dónde están los límites.
:::

### Punto de partida $\sigma=0$: oscilaciones puras

<span class="anker" id="stufe-2-1"></span>

Sobre el eje imaginario ($\sigma=0$), los bloques elementales son oscilaciones puras $\mathrm{e}^{\mathrm{j}2\pi ft}$. Una señal __absolutamente integrable__ ($\int|s(t)|\,\mathrm{d} t<\infty$, es decir, que decae con suficiente rapidez hacia ambos lados) puede componerse a partir de ellas. Es la representación de Fourier, que se trata en detalle en la parte dedicada a la transformada de Fourier:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Para muchas señales de la teoría de sistemas esto no basta. El escalón $\varepsilon(t)$ no decae, y $\mathrm{e}^{2t}\varepsilon(t)$ (la respuesta al impulso de un sistema inestable) incluso crece. Con oscilaciones de amplitud constante no se puede componer una señal que crece sin límite.

### El truco: amortiguar, descomponer, compensar

<span class="anker" id="stufe-2-2"></span>

**La idea.** Primero se hace descomponible la señal y después se deshace el cambio:

<ol>

<li>

⁠**Amortiguar.** Se multiplica por $\mathrm{e}^{-\sigma t}$. Si una señal por la derecha crece como mucho como $\mathrm{e}^{\alpha t}$, $s(t)\,\mathrm{e}^{-\sigma t}$ decae para todo $\sigma>\alpha$ y es absolutamente integrable.

</li>

<li>

⁠**Descomponer.** La señal amortiguada es una superposición de oscilaciones puras. Su espectro de Fourier es exactamente la transformada de Laplace $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ sobre la recta $\operatorname{Re} p=\sigma$ (ejercicio [2](#aufg-2)):

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma t}\bigr\}(f)=S(\sigma+\mathrm{j}2\pi f).$$

</li>

<li>

⁠**Compensar.** Se multiplica la descomposición por $\mathrm{e}^{\sigma t}$. El factor no depende de $f$ y puede entrar en la integral. Allí convierte cada oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ en el bloque elemental $\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}=\mathrm{e}^{pt}$.

</li>

</ol>

El resultado es la superposición que se suponía.

:::satz Teorema 2.1 (Fórmula de inversión de la transformada de Laplace)
<span class="anker" id="satz-2-1"></span>

Si $\sigma$ está en la región de convergencia de $S(p)$, se cumple

<span class="anker" id="gl-2-1"></span>
$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p =\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f. \tag{2.1}$$
:::

⁠**Cómo leerlo:**

<ul>

<li>

El camino de integración es la recta vertical $\operatorname{Re} p=\sigma$ del plano $p$, recorrida de abajo arriba ($f$ de $-\infty$ a $+\infty$, fig. [2](#abb-2)).

</li>

<li>

$\mathrm{e}^{pt}$ es el bloque elemental, y $S(p)\,\mathrm{d} p/(2\pi\mathrm{j})=S(\sigma+\mathrm{j}2\pi f)\,\mathrm{d} f$, su peso complejo. $S(p)$ misma es una __densidad__: peso por intervalo de frecuencia. Si $s$ es una tensión en V, $S$ tiene la unidad V s.

</li>

<li>

La integral se entiende como el límite $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$. Da $s(t)$ en todo punto en que $s$ es continua y, en un punto de salto, la media de los límites por la izquierda y por la derecha.

</li>

</ul>

⁠**Caso límite $\sigma=0$:** si el eje imaginario está en la región de convergencia, puede elegirse $\sigma=0$. Entonces $p=\mathrm{j}2\pi f$, y [(2.1)](#gl-2-1) se convierte en la fórmula de inversión de Fourier. La transformada de Laplace contiene la transformada de Fourier como caso particular.

:::herleitung fórmula de inversión a partir de la de Fourier
Según el paso 2, $S(\sigma+\mathrm{j}2\pi f)$ es el espectro de Fourier de $s(t)\mathrm{e}^{-\sigma t}$. La fórmula de inversión de Fourier da

$$s(t)\,\mathrm{e}^{-\sigma t}=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

Multiplicación por $\mathrm{e}^{\sigma t}$, que no depende de $f$:

$$s(t)=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

Cambio de variable $p=\sigma+\mathrm{j}2\pi f$ con $\sigma$ fijo: $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$, es decir, $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$. Los límites $f=\mp\infty$ pasan a ser $p=\sigma\mp\mathrm{j}\infty$:

$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p.$$
:::

**Ejemplo: el escalón a partir de bloques elementales.** Para $\varepsilon(t)$, $S(p)=1/p$ con $\operatorname{Re} p>0$. Se elige $\sigma=0{,}5/\mathrm s$ (fig. [2](#abb-2)). La figura [3](#abb-3) muestra lo que resulta si solo se superponen los bloques con $|f|\le F$. Ya con $F=0{,}25$ Hz se reconoce la forma del escalón. Al crecer $F$, el flanco se hace más abrupto; en $t=0$ la curva tiende al valor medio $\tfrac12$ (0,40; 0,47; 0,49), y en $t=-1$ s, a cero (0,053; 0,029; 0,008).

:::abbildung et3/k2linie
Plano $p$ para el escalón $\varepsilon(t)$, $S(p)=1/p$. La región de convergencia (fondo azul) está a la derecha del polo $p=0$. Cualquier recta vertical dentro de ella sirve como camino de integración; aquí, $\sigma=0{,}5/\mathrm s$. Cada punto de la recta es un bloque elemental $\mathrm{e}^{pt}$ con el peso $S(p)$.
:::

:::abbildung et3/k2sprung
El escalón, superpuesto a partir de los bloques elementales $\mathrm{e}^{pt}$ sobre la recta $\operatorname{Re} p=0{,}5/\mathrm s$, tomando solo los bloques con $|f|\le F$: $s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$ con $S(p)=1/p$. Cuantos más bloques, más exacto es el escalón; en $t=0$ la curva tiende a $\tfrac12$.
:::

:::frage Todos los bloques elementales son complejos. ¿Por qué sale una curva real?
Los bloques aparecen por parejas: a $f$ le corresponde $-f$, es decir, a $p$ el punto conjugado $p^*$. Para una señal real, el peso allí es el conjugado, $S(p^*)=S(p)^*$ (lo muestra el cálculo $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ con $s$ real). Cada pareja da $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$, es decir, una oscilación real, amortiguada o creciente. Las partes imaginarias se cancelan por parejas.
:::

:::frage Entonces, ¿es una suma o una integral?
En general, una integral: sobre la recta hay un continuo de bloques elementales, cada uno con un peso infinitesimal $S\,\mathrm{d} f$. Una suma propiamente dicha, con un número finito de términos, aparece en un caso importante: cuando $S(p)$ es un cociente de polinomios. Entonces la señal es una suma de bloques situados en los polos (etapa [4](#stufe-4)). Una suma con infinitos términos es la serie de Fourier de una señal periódica.
:::

### Región de convergencia: qué amortiguamientos funcionan

<span class="anker" id="stufe-2-3"></span>

**La idea.** El factor $\mathrm{e}^{-\sigma t}$ actúa a ambos lados del eje temporal, pero de forma opuesta. Para $t\to+\infty$ amortigua tanto más cuanto mayor es $\sigma$. Para $t\to-\infty$, $\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$, y allí un $\sigma$ grande amplifica. De ahí se siguen las tres formas de la región de convergencia:

<ul>

<li>

⁠**señal por la derecha (causal)**, $s(t)=0$ para $t<0$, que crece como mucho como $\mathrm{e}^{\alpha t}$: sirve cualquier $\sigma>\alpha$. Región de convergencia: el semiplano a la *derecha* de una frontera.

</li>

<li>

⁠**señal por la izquierda (anticausal)**: solo cuenta el lado $t\to-\infty$; ayudan los $\sigma$ pequeños. Región de convergencia: un semiplano a la *izquierda* de una frontera.

</li>

<li>

⁠**señal bilateral**: ambas condiciones deben cumplirse a la vez. Región de convergencia: una *franja*, que también puede estar vacía.

</li>

</ul>

¿Por qué las fronteras son siempre verticales? Se cumple $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$. Que $\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ sea finita depende solo de $\sigma$, nunca de $f$.

⁠**En resumen:** la región de convergencia es el conjunto de todos los amortiguamientos $\sigma$ con los que $s(t)\,\mathrm{e}^{-\sigma t}$ se vuelve absolutamente integrable.

:::merke Los pares básicos de transformadas (se usan en todo el artículo)
Para un número complejo $p_0$ cualquiera:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{todo }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

Con $p_0=0$, de [(2.2)](#gl-2-2) se obtiene el escalón: $\varepsilon(t)\leftrightarrow1/p$ para $\operatorname{Re} p>0$. Las dos primeras líneas tienen la *misma* expresión y distintas regiones de convergencia: solo las dos cosas juntas determinan la señal.
:::

:::herleitung pares básicos de transformadas
[(2.2)](#gl-2-2): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. El valor en el límite superior se anula si y solo si $\operatorname{Re}(p-p_0)>0$.

[(2.3)](#gl-2-3): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. El valor para $t\to-\infty$ se anula si y solo si $\operatorname{Re}(p-p_0)<0$.

[(2.4)](#gl-2-4): propiedad de selección, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.5)](#gl-2-5): integración por partes, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ para $\operatorname{Re} p>0$.
:::

:::frage Al calcular $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$, ¿por qué desaparecen los términos exponenciales y por qué sale $\frac{1}{b+p}$ y no $\frac{1}{-(b+p)}$?
Ambas cosas se deben a la evaluación en los límites. La primitiva de $\mathrm{e}^{-(b+p)t}$ es $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, con signo menos, porque al derivar aparece el factor $-(b+p)$. Después se calcula «límite superior menos límite inferior»:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**Límite superior:** $|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ tiende a cero si y solo si $\operatorname{Re} p>-\operatorname{Re} b$. Esta condición *es* la región de convergencia. Fuera de ella, el término exponencial no desaparecería y crecería sin límite.

</li>

<li>

⁠**Límite inferior:** $\mathrm{e}^0=1$; allí no queda ningún término exponencial.

</li>

<li>

⁠**Signo:** el menos de la primitiva se encuentra con el menos con el que se resta el límite inferior. Menos por menos da más.

</li>

</ul>

Con el pulso por la izquierda $\mathrm{e}^{-bt}\varepsilon(-t)$ ocurre lo contrario. Se integra de $-\infty$ a $0$; ahora $t=0$ es el límite *superior*. Su contribución $-\frac{1}{b+p}$ no se resta, y el signo menos se mantiene. El límite inferior $t\to-\infty$ solo se anula para $\operatorname{Re}(b+p)<0$; por eso esta región de convergencia está a la izquierda. Con $p_0=-b$, estos son los pares básicos [(2.2)](#gl-2-2) y [(2.3)](#gl-2-3).
:::

:::frage ¿Se miran las partes reales de $b$ y $p$ porque el decaimiento del integrando decide la integrabilidad? Para algunos $b$ la señal decae; para otros crece, no baja a cero, y la integral no converge porque siempre se sigue sumando algo.
Sí, exactamente. El módulo del integrando es

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

La parte imaginaria solo hace girar el integrando en el plano complejo; no cambia su módulo. Si crece o decae lo decide únicamente la parte real. Tres precisiones:

<ul>

<li>

Cuenta la *suma* $\operatorname{Re} b+\sigma$. La señal puede crecer por sí misma ($\operatorname{Re} b<0$), siempre que el amortiguamiento $\sigma$ sea más fuerte. Es el truco «amortiguar» del apartado 2.2.

</li>

<li>

«Tiende a cero» no basta por sí solo. También $1/t$ tiende a cero, pero $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, porque las contribuciones disminuyen demasiado despacio. El decaimiento exponencial es lo bastante rápido: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ es finita.

</li>

<li>

En la frontera $\operatorname{Re}(b+p)=0$, el integrando tiene módulo constante 1 y solo gira. La integral oscila entonces en lugar de acercarse a un valor, y justo en el polo incluso crece linealmente (ejercicio [3a](#aufg-3a)). Por eso la recta frontera no pertenece a la región de convergencia.

</li>

</ul>
:::

:::frage Entonces, ¿vale esto para cualquier función?
No, solo para funciones con región de convergencia no vacía. Tres contraejemplos:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ crece más rápido que cualquier función exponencial. $\mathrm{e}^{t^2-\sigma t}\to\infty$ para todo $\sigma$; ningún amortiguamiento basta.

</li>

<li>

$\mathrm{e}^{|t|}$: la mitad derecha exige $\sigma>1$, y la izquierda, $\sigma<-1$. Ambas cosas a la vez son imposibles.

</li>

<li>

Incluso la constante $s(t)=1$ para todo $t$: a la derecha $\sigma>0$, a la izquierda $\sigma<0$. La transformada de Fourier abarca aun así este tipo de señales, con un impulso de Dirac en el espectro.

</li>

</ul>

Para señales por la derecha con crecimiento como mucho exponencial, siempre funciona. Entre ellas está toda señal que se conecta en un circuito en $t=0$.
:::

:::frage ¿Por qué basta una sola recta, si el plano $p$ es bidimensional?
Toda recta de la región de convergencia da la misma $s(t)$: con un $\sigma$ mayor se amortigua más en el paso 1 y se compensa más en el paso 3; ambos efectos se anulan. Comprobado numéricamente: con $\sigma=0{,}2$ y $\sigma=1/\mathrm s$ se obtiene para el escalón en ambos casos $s(1\,\mathrm{s})\approx1{,}00$ y $s(-1\,\mathrm{s})\approx0{,}00$. Así pues, el plano contiene más de lo que hace falta para la superposición. Su utilidad está en otra parte: en el plano, $S(p)$ puede describirse con pocos números, los polos y los ceros. (Nota adicional: $S(p)$ es derivable en sentido complejo en la región de convergencia; por eso los valores sobre una recta determinan la función en toda la región.)
:::

:::aufgabe Ejercicio 2 ★ Laplace es Fourier de una señal amortiguada
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Demuestra que $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$ descomponiendo $\mathrm{e}^{-pt}$ en dos factores.

</li>

<li>

Compruébalo con el escalón: calcula directamente $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$ para $\sigma>0$ y compáralo con $S(p)=1/p$.

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$.

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$ para $\sigma>0$. Es $1/p$ en el punto $p=\sigma+\mathrm{j}2\pi f$.
:::
:::

:::aufgabe Ejercicio 3 ★★ Una señal creciente
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, por ejemplo la respuesta al impulso de un sistema inestable ($t$ en s).

<ol class="al">

<li>

¿Por qué no existe transformada de Fourier en sentido clásico?

</li>

<li>

¿Para qué $\sigma$ es $s(t)\,\mathrm{e}^{-\sigma t}$ absolutamente integrable?

</li>

<li>

Calcula $S(p)$ directamente a partir de la integral. Dibuja el polo y la región de convergencia en el plano $p$.

</li>

<li>

¿Qué $\sigma$ puedes usar en la fórmula de inversión? La expresión $S(\mathrm{j}2\pi f)$ es finita. ¿Por qué, aun así, no puedes elegir $\sigma=0$, y qué señal se obtendría con $\sigma=0$? (Pista: [(2.3)](#gl-2-3).)

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$: la señal no es absolutamente integrable. Intuitivamente: con oscilaciones de amplitud constante no puede componerse nada que crezca.

(b) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ para $t>0$, integrable si y solo si $\sigma>2/\mathrm s$.

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ para $\operatorname{Re} p>2$. Polo en $p=2$, región de convergencia a su derecha, como en toda señal por la derecha. Comprobación numérica: $S(3)=1$, $S(2{,}5+\mathrm{j})=0{,}4-0{,}8\mathrm{j}$.

(d) Cualquier $\sigma>2/\mathrm s$, por ejemplo $\sigma=3/\mathrm s$. $\sigma=0$ está a la izquierda del polo, es decir, fuera de la región de convergencia. La expresión $1/(\mathrm{j}2\pi f-2)$ es finita, pero corresponde a *otra* señal: según [(2.3)](#gl-2-3), también $-\mathrm{e}^{2t}\varepsilon(-t)$ tiene la transformada $1/(p-2)$, con región de convergencia $\operatorname{Re} p<2$. Con $\sigma=0$ se obtendría esta señal por la izquierda, que decae. Es la señal cuya transformada de Fourier es realmente $1/(\mathrm{j}2\pi f-2)$.
:::
:::

:::aufgabe Ejercicio 3a ★★ Qué ocurre en la frontera
<span class="anker" id="aufg-3a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$, es decir, $b=-1-3\mathrm{j}$ ($t$ en s).

<ol class="al">

<li>

¿Para qué $\sigma$ converge $\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$? ¿Qué papel desempeña el 3?

</li>

<li>

Toma $p=1+\mathrm{j}\omega$, es decir, justo sobre la frontera, y calcula $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. ¿Qué ocurre para $T\to\infty$? Distingue $\omega\neq3$ y $\omega=3$. ¿Dónde está el polo?

</li>

</ol>

:::loesung
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ con $p=\sigma+\mathrm{j}\omega$. El módulo del integrando es $\mathrm{e}^{-(\sigma-1)t}$; la integral converge si y solo si $\sigma>1$. El 3 (la frecuencia angular de la señal) no aparece en el módulo. Solo determina dónde está el polo sobre la recta frontera: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, polo en $p=1+3\mathrm{j}$.

(b) Con $p=1+\mathrm{j}\omega$, $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. Al crecer $T$, el numerador gira sobre una circunferencia centrada en 1 y no se acerca a ningún valor. La integral permanece acotada, pero no tiene límite.

</li>

<li>

$\omega=3$, es decir, justo en el polo $p=1+3\mathrm{j}$: el integrando vale constantemente 1, la integral vale $T$ y crece sin límite.

</li>

</ul>

Así pues, sobre la recta frontera la integral no converge en ningún punto. La región de convergencia es el semiplano abierto $\operatorname{Re} p>1$.
:::
:::

:::aufgabe Ejercicio 4 ★ ¿Verdadero o falso? Con justificación
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Toda función tiene transformada de Laplace.

</li>

<li>

Que $p$ esté en la región de convergencia depende solo de $\operatorname{Re} p$.

</li>

<li>

Si el eje imaginario está en la región de convergencia, $S(\mathrm{j}2\pi f)$ es la transformada de Fourier de $s(t)$.

</li>

<li>

En la fórmula de inversión, $\sigma=1/\mathrm s$ da una señal distinta de la que da $\sigma=2/\mathrm s$ si ambos valores están en la región de convergencia.

</li>

<li>

$\cos(2\pi f_0t)$ es función propia de todo sistema LTI.

</li>

</ol>

:::loesung
(a) Falso. Contraejemplos: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, la constante bilateral.

(b) Verdadero. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$; la frecuencia $f$ no aparece en el módulo. Por eso la región de convergencia está formada por rectas verticales completas.

(c) Verdadero. Con $\sigma=0$, $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) Falso. Toda recta de la región de convergencia da la misma señal, porque el amortiguamiento $\mathrm{e}^{-\sigma t}$ y la compensación con $\mathrm{e}^{\sigma t}$ se anulan.

(e) Falso. La salida es $|H|\cos(2\pi f_0t+\varphi)$ con $H=H(\mathrm{j}2\pi f_0)$. Solo es un múltiplo de $\cos(2\pi f_0t)$ si $\varphi=0$ o $\varphi=\pi$, es decir, si $H(\mathrm{j}2\pi f_0)$ es real. Para el filtro paso bajo RC esto no ocurre a ninguna frecuencia $f_0>0$.
:::
:::

## Etapa 3: La convolución se vuelve una multiplicación

<span class="anker" id="stufe-3"></span>

:::zweck
La etapa [1](#stufe-1) dice qué hace el sistema con un bloque elemental. La etapa [2](#stufe-2) dice que toda señal está formada por bloques elementales. Juntas dan el teorema más importante de la transformada de Laplace.
:::

**La idea.** Un sistema LTI es lineal: procesa cada bloque elemental de la entrada por separado y suma los resultados. Cada bloque $\mathrm{e}^{pt}$ lo multiplica por $H(p)$. La salida consta, pues, de los *mismos* bloques que la entrada; solo que cada peso está multiplicado por $H(p)$. La figura [4](#abb-4) muestra los dos caminos hacia la salida.

:::abbildung et3/k2wege
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
Se introduce la entrada como superposición [(2.1)](#gl-2-1) en la convolución, con una recta $\operatorname{Re} p=\sigma$ que esté en ambas regiones de convergencia:

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

Linealidad: la convolución puede entrar en la integral; actúa sobre cada bloque elemental por separado:

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

Función propia [(1.1)](#gl-1-1): $\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$.

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

La transformada inversa de los dos sumandos se obtiene de [(2.2)](#gl-2-2) con $p_0=0$ y $p_0=-1$. Comprobación directa: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ para $t>0$. También la fórmula de inversión [(2.1)](#gl-2-1), evaluada numéricamente sobre la recta $\sigma=0{,}5/\mathrm s$, da $g(0{,}5\,\mathrm{s})=0{,}3935$, $g(1\,\mathrm{s})=0{,}6321$, $g(3\,\mathrm{s})=0{,}9502$ y $g(-1\,\mathrm{s})=0$, exactamente $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$.

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

Entrada $s(t)=t\,\varepsilon(t)$ con $S(p)=1/p^2$ para $\operatorname{Re} p>0$, par básico [(2.5)](#gl-2-5).

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

¿Cómo se comporta $g(t)$ para $t\gg1$ s? Compáralo con el ejercicio [1](#aufg-1)c.

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ para $\operatorname{Re} p>0$ (intersección de $\operatorname{Re} p>0$ y $\operatorname{Re} p>-1$).

(b) Con denominador común: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Transformada inversa con [(2.5)](#gl-2-5) y [(2.2)](#gl-2-2):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$: la tensión del condensador no puede saltar, y la entrada empieza en cero. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, exactamente la respuesta al escalón. Encaja: la rampa es la integral del escalón; por tanto, la respuesta a la rampa es la integral de la respuesta al escalón.

(d) Para $t\gg1$ s, $\mathrm{e}^{-t}\approx0$ y $g(t)\approx t-1$: la salida sigue a la rampa con un retardo de $RC=1$ s, igual que con la rampa bilateral del ejercicio [1](#aufg-1)c. La diferencia es el bloque elemental $\mathrm{e}^{-t}$ (polo $-1$ del sistema): el transitorio, porque aquí la rampa solo empieza en $t=0$.
:::
:::

## Etapa 4: La integral se convierte en una suma

<span class="anker" id="stufe-4"></span>

:::zweck
La suposición, al pie de la letra: para las señales de las que casi siempre se trata en teoría de sistemas, la señal es una *suma finita* de exponenciales complejas. Los polos son los exponentes.
:::

**La idea.** En redes de $R$, $L$, $C$ y en todos los sistemas descritos por una ecuación diferencial, $S(p)$ es un cociente de polinomios. La __descomposición en fracciones parciales__ lo escribe, si los polos son simples, como

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

Cada sumando es la transformada de *un único bloque elemental*: según [(2.2)](#gl-2-2), $A_r/(p-p_r)$ corresponde a $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$ si la región de convergencia está a la derecha del polo, y el sumando constante $A_0$ corresponde, según [(2.4)](#gl-2-4), a $A_0\,\delta(t)$. Para una señal por la derecha se tiene, por tanto,

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**En resumen:** una señal por la derecha con transformada de Laplace racional es una suma finita de bloques elementales $\mathrm{e}^{p_r t}$. Los polos son los exponentes; los coeficientes de las fracciones parciales, los pesos.

Así, toda señal de este tipo puede leerse en sus polos, con el mapa de la figura [1](#abb-1): $\operatorname{Re} p_r$ dice si el bloque decae o crece, y $\operatorname{Im} p_r$, con qué rapidez oscila. Un par de polos conjugados $p_r,p_r^*$ da en conjunto una oscilación real amortiguada. Aquí está también el núcleo de la __estabilidad__: un bloque causal $\mathrm{e}^{p_r t}\varepsilon(t)$ decae si y solo si $\operatorname{Re} p_r<0$. Por eso un sistema causal es estable si todos los polos de $H(p)$ están en el semiplano izquierdo.

**Ejemplo.** La respuesta al escalón de la etapa [3](#stufe-3) tiene los polos $0$ y $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{polo }0\text{ (de }S)}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{polo }-1\text{ (de }H)}\qquad(t>0).$$

El polo de la entrada aporta la parte que impone la entrada (la tensión final 1). El polo del sistema aporta la __respuesta natural__ del circuito RC, el decaimiento con $RC=1$ s. Esto vale en general: en la salida $G=SH$ están los polos de la entrada y los polos del sistema.

:::zusatz por qué la integral se reduce a una suma: el teorema de los residuos
Este apartado necesita el teorema de los residuos del análisis complejo. Explica por qué [(2.1)](#gl-2-1) y [(4.1)](#gl-4-1) son lo mismo y por qué la región de convergencia decide cuál es la señal.

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

:::abbildung et3/k2residuen
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

Compara con los pares básicos [(2.2)](#gl-2-2) y [(2.3)](#gl-2-3). ¿Qué aprendes de ello sobre el dato «$S(p)=1/(p+1)$» sin región de convergencia?

</li>

</ol>

:::loesung
(a) Recta a la derecha del polo, por ejemplo $\sigma=0$. Para $t>0$, se cierra por la izquierda: el polo $-1$ queda dentro, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, luego $s(t)=\mathrm{e}^{-t}$. Para $t<0$, se cierra por la derecha: a la derecha de la recta no hay ningún polo, $s(t)=0$. En conjunto, $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Recta a la izquierda del polo, por ejemplo $\sigma=-2$. Para $t>0$, se cierra por la izquierda: ningún polo, $s(t)=0$. Para $t<0$, se cierra por la derecha: el polo queda dentro, recorrido en sentido horario, $s(t)=-\mathrm{e}^{-t}$. En conjunto, $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) Son exactamente los pares básicos [(2.2)](#gl-2-2) y [(2.3)](#gl-2-3) con $p_0=-1$. El dato «$S(p)=1/(p+1)$» por sí solo no determina la señal. Solo con la región de convergencia está claro a qué lado de la recta está el polo y si da un bloque elemental causal o uno anticausal.
:::
:::

## Etapa 5: Por qué se transforma también la entrada

<span class="anker" id="stufe-5"></span>

:::frage Tiene sentido transformar $h(t)$ para poder multiplicar $H(p)$ por funciones propias y determinar la salida. Pero transformar $s(t)$, en principio, no tiene sentido: desde la teoría de sistemas no se puede hacer nada con ello. Claro, $s*h=h*s$, pero $h(t)$ la mayoría de las veces no es una función propia, así que no se puede escribir $h(t)\cdot S(p)$. ¿Qué significado tiene, en relación con el sistema, transformar una señal cualquiera?
⁠**Qué es correcto en la pregunta:** $H(p)$ dice qué hace el sistema con un bloque elemental $\mathrm{e}^{pt}$. Y $h(t)\cdot S(p)$, efectivamente, no tiene sentido.

⁠**Dónde está el error de razonamiento:** la entrada tampoco es casi nunca una función propia. Un escalón, una señal de voz o un pulso rectangular no son bloques elementales $\mathrm{e}^{pt}$ aislados. Por eso $H(p)\cdot s(t)$ tiene tan poco sentido como $h(t)\cdot S(p)$: $H(p)$ solo puede aplicarse a un bloque elemental, y para una $s(t)$ cualquiera ni siquiera está claro a qué $p$ se refiere. Antes de que $H(p)$ pueda hacer algo, la entrada tiene que estar descompuesta en bloques elementales. Eso es exactamente lo que hace $S(p)$.

⁠**La visión correcta:** en el teorema de convolución $G(p)=H(p)\,S(p)$, cada factor tiene un significado propio relacionado con el sistema:

<ul>

<li>

$S(p)$ es la *receta de la entrada*: cuánto del bloque elemental $\mathrm{e}^{pt}$ contiene la entrada;

</li>

<li>

$H(p)$ es el *efecto del sistema*: por qué número multiplica ese bloque;

</li>

<li>

$G(p)$ es la receta de la salida.

</li>

</ul>

Sin $S(p)$ solo se conoce el efecto sobre bloques aislados, pero no qué bloques llegan. $H(p)$ por sí sola responde a la pregunta «¿Qué ocurre con la salida?» solo en el caso particular de que la entrada sea ella misma un único bloque elemental.

⁠**Con el ejemplo del escalón y el filtro paso bajo RC.** El escalón tiene la receta $S(p)=1/p$. Sobre la recta $\sigma=0{,}5/\mathrm s$, $|S|=2$ en $f=0$, $0{,}16$ en 1 Hz y $0{,}016$ en 10 Hz. Los bloques rápidos son débiles, pero están presentes, y forman el flanco abrupto (fig. [3](#abb-3): cuantos más bloques rápidos, más abrupto es el flanco). El filtro paso bajo RC los multiplica por $|H|=0{,}67$, $0{,}15$ y $0{,}016$. En la salida, los bloques rápidos son, por tanto, aproximadamente un factor $2\pi f\cdot RC$ más débiles todavía (para $f\gg1/(2\pi RC)=0{,}16$ Hz), y el flanco desaparece: $g(t)=1-\mathrm{e}^{-t}$ sube de forma continua. Esta explicación necesita las dos transformadas. $H$ por sí sola solo dice «los bloques rápidos se debilitan»; solo $S$ dice que el flanco está formado por bloques rápidos.

⁠**¿Y la simetría $s*h=h*s$?** Matemáticamente, ambas señales están en pie de igualdad: también puede leerse $h$ como entrada y $s$ como «sistema»; entonces $H(p)$ es la receta y $S(p)$, el efecto. La teoría de sistemas reparte los papeles solo según la física: una señal viene de fuera; la otra describe el circuito. En el dominio transformado se transforman siempre *las dos*.
:::

**Otras razones para transformar una señal por sí sola.**

<ul>

<li>

⁠**Medir un sistema.** Si se miden la entrada y la salida de un sistema desconocido, $H(p)=G(p)/S(p)$ da el sistema. Para ello se transforman dos señales, cada una por separado (ejercicio [9](#aufg-9)).

</li>

<li>

⁠**Entender la propia señal.** El sonido de una campana golpeada es una suma de oscilaciones amortiguadas, cada una un par de polos conjugados. $\operatorname{Im} p_r$ es la altura tonal de un parcial, y $-\operatorname{Re} p_r$, su tasa de decaimiento. Unos pocos polos describen todo el sonido. Un instrumento de medida que muestra un espectro hace lo mismo sobre la recta $\sigma=0$.

</li>

<li>

⁠**Convolución sin sistema.** La convolución superpone copias desplazadas y ponderadas de una señal. El sistema es una interpretación de esta operación, no la única. Un ejemplo sin ningún sistema es la suma de puntos de dos dados (artículo sobre la convolución).

</li>

</ul>

:::ltspice Una red para dos mediciones
⁠**Esquema:** la red que has encontrado en el ejercicio [9](#aufg-9)(c), con la fuente `PULSE(0 1 0 1u 1u 100)` en la entrada y la salida en el nodo `out`. Al lado, sin conexión con el circuito, una fuente de comportamiento `bv` en el nodo `mess` con `V=1-exp(-2*time)`. Hace el papel de la curva de salida medida.

⁠**Directivas:** `.tran 0 3 0 1m`, `.meas tran abw MAX abs(V(out)-V(mess))`.

⁠**Lo que ves:** si la red y los valores de los componentes son correctos, `V(out)` y `V(mess)` quedan superpuestas, y la mayor desviación, `abw`, es prácticamente nula (inferior a $10^{-5}$). Compara así las curvas con tu resultado del ejercicio [9](#aufg-9)(c).
:::

:::aufgabe Ejercicio 8 ★★ ¿Qué bloques elementales forman el flanco?
<span class="anker" id="aufg-8"></span>

Entrada $\varepsilon(t)$; sistema: filtro paso bajo RC con $RC=1$ s. Considera los bloques elementales sobre la recta $\sigma=0{,}5/\mathrm s$.

<ol class="al">

<li>

Calcula $|S(p)|$, $|H(p)|$ y $|G(p)|$ para $f=0$, $1$ Hz y $10$ Hz.

</li>

<li>

¿En qué factor debilita el sistema los bloques de 10 Hz más que los de 1 Hz?

</li>

<li>

Explica con (a) y la fig. [3](#abb-3) por qué la salida no tiene flanco. ¿Por qué no basta $H(p)$ por sí sola para esta explicación?

</li>

</ol>

:::loesung
(a) Con $p=0{,}5+\mathrm{j}2\pi f$ (en $1/\mathrm s$), $S=1/p$, $H=1/(p+1)$, $G=SH$:

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0,667 | 1,33 |
| 1 Hz | 0,159 | 0,155 | 0,0246 |
| 10 Hz | 0,0159 | 0,0159 | 0,000253 |

(b) $0{,}155/0{,}0159\approx9{,}7$, es decir, casi un factor 10, igual que la frecuencia. Para $|p|$ grande, $|H|\approx1/|p|\approx1/(2\pi f)$.

(c) El flanco del escalón está formado por los bloques rápidos: en la fig. [3](#abb-3) se hace más abrupto cuantos más de ellos se toman. En la entrada, sus pesos decrecen como $1/f$; en la salida, como $1/f^2$. En la salida, los bloques rápidos son tan débiles que ya no se forma ningún flanco, y $g(t)$ sube de forma continua. $H(p)$ por sí sola solo dice que los bloques rápidos se debilitan. Que el flanco esté formado precisamente por esos bloques es una afirmación sobre la entrada, y esa está en $S(p)$.
:::
:::

:::aufgabe Ejercicio 9 ★★ Un sistema desconocido a partir de dos mediciones
<span class="anker" id="aufg-9"></span>

A un sistema LTI causal desconocido se le aplica en el instante $t=0$ una tensión de 1 V, $s(t)=\varepsilon(t)$ en V. En la salida se mide $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ en V ($t$ en s).

<ol class="al">

<li>

Transforma las dos señales, cada una por separado.

</li>

<li>

Determina $H(p)$ y, a partir de ella, $h(t)$.

</li>

<li>

¿De qué red podría tratarse? ¿Qué valor se obtiene?

</li>

<li>

¿Qué polo de $G(p)$ procede de la entrada y cuál del sistema?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ para $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ para $\operatorname{Re} p>0$ (par básico [(2.2)](#gl-2-2) con $p_0=0$ y $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Como el sistema es causal, la región de convergencia está a la derecha del polo: $\operatorname{Re} p>-2$. Con [(2.2)](#gl-2-2): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ en $1/\mathrm s$.

(c) Un filtro paso bajo RC tiene $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. La comparación con $\dfrac{2}{p+2}$ da $RC=0{,}5$ s, por ejemplo $R=500\,\mathrm{k\Omega}$ y $C=1$ µ F. (Cualquier otra red con la misma función de transferencia se comportaría igual en los bornes. Con mediciones en la entrada y la salida solo se conoce $H$, no los componentes.)

(d) El polo $p=0$ procede de la entrada (escalón), y el polo $p=-2$, del sistema. Al dividir $G/S$ se cancela justamente el polo de la entrada.
:::
:::

:::merke Lo esencial hasta aquí
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$, de ahí $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$ con $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$.

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$: $\sigma$ es la tasa de crecimiento; $f$, la frecuencia del bloque elemental.

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$, $\sigma$ en la región de convergencia; toda recta de este tipo da la misma $s(t)$.

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$; para $\sigma=0$, la transformada de Fourier.

</li>

<li>

Región de convergencia: depende solo de $\sigma$; por la derecha, un semiplano derecho; por la izquierda, uno izquierdo; bilateral, una franja.

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$ para $\operatorname{Re} p>\operatorname{Re} p_0$; $-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$ para $\operatorname{Re} p<\operatorname{Re} p_0$.

</li>

<li>

$G(p)=S(p)H(p)$; derivar $\to p$, integrar $\to1/p$.

</li>

<li>

Racional y por la derecha: $s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$, polos = exponentes. Causal y estable: todos los polos a la izquierda.

</li>

</ul>
:::
