---
title: Etapa 1: Por qué precisamente $\mathrm{e}^{pt}$
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220200
summary: Si se introduce e pt en la integral de convolución, se obtiene H(p)\,e pt : e pt es una función propia.
tags: tasa de crecimiento, frecuencia
lang: es
---

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

:::abbildung et3/k2bausteine 1
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
