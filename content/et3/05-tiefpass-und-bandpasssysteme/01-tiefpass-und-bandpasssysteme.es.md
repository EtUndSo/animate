---
title: Sistemas paso bajo y paso banda
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3250100
summary: Transmisión sin distorsión, paso bajo ideal, envolvente compleja y retardo de grupo
tags: retardo de fase, retardo de grupo, duración de la señal, seno integral, tiempo de subida, eco, filtro de coseno alzado, paso bajo equivalente
lang: es
---

## De qué trata

Casi toda transmisión debe hacer llegar una señal lo más inalterada posible, pero solo en un determinado rango de frecuencias: un paso bajo deja pasar las frecuencias bajas; un paso banda, una banda en torno a una frecuencia portadora. Este artículo se pregunta: *¿qué significa exactamente «inalterada», qué precio tiene una banda limitada de forma abrupta y cómo se calcula con señales que van montadas sobre una portadora de alta frecuencia?*

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Sin distorsión significa que la señal solo se amplifica y se retrasa. Para ello hacen falta un módulo constante y una fase que decrece linealmente con la frecuencia.

</li>

<li>

Un paso bajo con límite abrupto (ideal) no es causal, presenta en los saltos una sobreoscilación de aproximadamente el 9 % y necesita un tiempo de subida de $1/(2f_\mathrm g)$. Unos flancos más suaves reducen la sobreoscilación a costa de la selectividad.

</li>

<li>

Una señal paso banda es una señal paso bajo (la envolvente compleja) sobre una portadora. Con la envolvente se calcula como con una señal paso bajo: sufre el retardo de grupo, y la portadora, el retardo de fase.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.**

| Resultado | De dónde viene |
|---|---|
| Sistema sin distorsión | cada oscilación amplificada por igual y retrasada el mismo tiempo (etapa [1](#stufe-1)) |
| Retardo de fase y de grupo | retardo de la portadora y de la envolvente, respectivamente (etapas [1](#stufe-1), [11](#stufe-11)) |
| Duración de la señal $\cdot$ ancho de banda $=$ cte. | teorema de escalado o de semejanza (etapa [2](#stufe-2)) |
| Sobreoscilación del 21,7 % y del 8,95 % | lóbulos secundarios de la función si, Gibbs (etapas [2](#stufe-2), [3](#stufe-3)) |
| Aproximación causal, diseño con ventanas | truncar la respuesta al impulso = convolución en el espectro (etapas [4](#stufe-4), [6](#stufe-6)) |
| Filtro conformador de pulsos | flanco suave en el espectro, respuesta al impulso que decae rápidamente (etapa [5](#stufe-5)) |
| Paso bajo equivalente, envolvente compleja | desplazar las frecuencias positivas hacia cero (etapas [7](#stufe-7), [8](#stufe-8)) |
| Esquema en cuadratura, muestreo paso banda | calcular el paso banda en el dominio paso bajo (etapa [10](#stufe-10)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este artículo
<ul>

<li>

⁠**Paso bajo RC** con $RC=1$ s, como en las partes 1 a 3.

</li>

<li>

⁠**Paso bajo ideal** con $f_\mathrm g=1$ Hz (para comparar, también 2 Hz).

</li>

<li>

⁠**Paso banda ideal** con la frecuencia central $f_0=10$ Hz y el ancho de banda $\Delta f=2$ Hz.

</li>

<li>

⁠**Paso bajo en tiempo discreto** con $f_\mathrm g=0{,}2$ (normalizada a la frecuencia de muestreo) y 21 coeficientes.

</li>

</ul>

El script `rechnung_kap5.py` recalcula los números y las curvas. $\operatorname{si}(x)=\sin(x)/x$, como en la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::

## Etapa 1: El sistema sin distorsión

<span class="anker" id="stufe-1"></span>

:::zweck
¿Qué debe lograr exactamente una «buena» transmisión? ¿Y con qué magnitudes características se mide cuánto se aparta de ello un sistema?
:::

**La idea.** Una señal ha llegado sin distorsión si solo se ha vuelto más intensa o más débil y más tardía, pero conserva su forma:

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

En el espectro, esto significa: cada oscilación se multiplica por el mismo factor $h_0$, y cada una se desplaza el mismo tiempo $t_0$. A la frecuencia $f$, un desplazamiento temporal $t_0$ equivale al ángulo $2\pi ft_0$. Por eso la fase $\varphi(f)=-2\pi t_0f$ tiene que ser una recta que pasa por el origen.

:::definition Definición 1.1 (Magnitudes características de un sistema LTI)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{Atenuación:} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{o}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{Desfase:} && b(f)=-\varphi(f),\\ &\text{Retardo de fase:} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{Retardo de grupo:} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**Cómo leerlo:** el __retardo de fase__ es el retardo de una única oscilación de frecuencia $f$. El __retardo de grupo__ es el retardo de un grupo de frecuencias vecinas, es decir, de una envolvente (etapa [11](#stufe-11)). En el sistema sin distorsión, $a$, $t_\mathrm p$ y $t_\mathrm g$ son constantes y $t_\mathrm p=t_\mathrm g=t_0$.

**Ejemplo: el circuito RC.** Con $\varphi=-\arctan(2\pi f\,RC)$ y $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

Para $f\to0$, ambos valen $RC=1$ s. En $f=0{,}159$ Hz ($2\pi fRC=1$), $t_\mathrm p=0{,}785$ s, $t_\mathrm g=0{,}5$ s y $a=3{,}0$ dB. Así pues, el circuito RC no está libre de distorsión: su atenuación depende de la frecuencia, y las distintas frecuencias llegan en instantes distintos.

:::ltspice Leer la atenuación y los retardos del circuito RC
⁠**Esquema:** circuito RC (`res` con `1Meg`, `cap` con `1u`), valor de fuente `AC 1`, directiva `.ac dec 100 0.01 10`.

⁠**Lectura:** el eje izquierdo muestra $20\lg|H|=-a$ en dB. Lleva el ratón al eje derecho (fase) hasta que el puntero se convierta en una regla, haz clic y elige «Group Delay»: entonces el eje muestra $t_\mathrm g(f)$ según [(1.5)](#gl-1-5). El retardo de fase lo calculas a partir de la fase, $t_\mathrm p=-\varphi/(2\pi f)$, con $\varphi$ en radianes.

⁠**Lo que ves:** hacia las frecuencias bajas, $t_\mathrm g$ tiende a 1 s. En 0,159 Hz lees $a=3{,}0$ dB, $\varphi=-45^\circ$ y $t_\mathrm g=0{,}5$ s; de ahí, $t_\mathrm p=0{,}785$ s. Compara los valores en $2\pi fRC=10$ con tu resultado del ejercicio [1](#aufg-1)(b).
:::

:::aufgabe Ejercicio 1 ★ Retardos del circuito RC
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Deduce $t_\mathrm g$ del circuito RC a partir de [(1.5)](#gl-1-5).

</li>

<li>

Calcula $t_\mathrm p$, $t_\mathrm g$ y $a$ para $2\pi fRC=10$. ¿En qué rango de frecuencias está el circuito RC aproximadamente libre de distorsión?

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$, $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$; por tanto, $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$.

(b) Para $2\pi fRC=10$: $t_\mathrm p=\frac{\arctan10}{10}RC=0{,}147$ s, $t_\mathrm g=\frac{RC}{101}=0{,}0099$ s, $a=20{,}0$ dB. El circuito RC solo está aproximadamente libre de distorsión para $2\pi fRC\ll1$, es decir, muy por debajo de 0,16 Hz: ahí $|H|\approx1$ y $t_\mathrm p\approx t_\mathrm g\approx RC$.
:::
:::

## Etapa 2: El paso bajo ideal

<span class="anker" id="stufe-2"></span>

:::zweck
El paso bajo ideal deja pasar sin alteración todas las frecuencias hasta $f_\mathrm g$ y bloquea todas las superiores. Esta etapa muestra qué significa este corte abrupto en el dominio del tiempo.
:::

:::satz Teorema 2.1 (Paso bajo ideal)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**Cómo leerlo:** la respuesta al impulso se extiende hasta el infinito en ambas direcciones. Por tanto, el paso bajo ideal *no es causal*: tendría que responder a un impulso antes de que este llegue. Es un objeto matemático límite al que solo es posible aproximarse (etapas [4](#stufe-4), [6](#stufe-6)).

**Duración y ancho de banda.** Como __duración de la señal__ $t_m$ de una respuesta al impulso se toma la anchura de un rectángulo con la misma altura $h_{\max}$ y la misma área:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

En el paso bajo ideal, $H(0)=1$ y $h_{\max}=2f_\mathrm g$; por tanto, $t_m=\frac{1}{2f_\mathrm g}$ y $f_\mathrm g\cdot t_m=\frac12$. En general, para los filtros paso bajo se cumple $f_\mathrm g\cdot t_m=\text{cte.}$: el doble de ancho de banda significa la mitad de duración de la respuesta. Es el teorema de escalado (semejanza) de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

**Sobreoscilación.** En la función si, la relación entre el máximo secundario de mayor valor absoluto, $a_1$, y el máximo principal $a_0$ es

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21{,}7\,\%,$$

independiente de $f_\mathrm g$ (el primer mínimo secundario de $\operatorname{si}(\pi u)$ está en $u=1{,}43$ y vale $-0{,}217$). Un cambio de $f_\mathrm g$ solo comprime la curva; no cambia su forma.

:::aufgabe Ejercicio 2 ★ Paso bajo ideal para voz
<span class="anker" id="aufg-2"></span>

Un paso bajo ideal con $f_\mathrm g=4$ kHz. ¿Cuánto valen la duración de la señal de la respuesta al impulso y la sobreoscilación? ¿Qué cambia con $f_\mathrm g=8$ kHz?

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s, sobreoscilación del 21,7 %. Con 8 kHz, la duración se reduce a la mitad, a 62,5 µ s. La sobreoscilación sigue siendo del 21,7 %, porque la respuesta al impulso solo se comprime.
:::
:::

## Etapa 3: Respuesta al escalón y tiempo de subida

<span class="anker" id="stufe-3"></span>

:::zweck
¿Cómo reacciona el paso bajo ideal a un escalón? ¿Con qué rapidez sube y cuánto sobrepasa el valor final?
:::

La respuesta al escalón es la integral acumulada de la respuesta al impulso ([parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Con el __seno integral__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

se obtiene

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung Respuesta al escalón
La integral hasta $t$ se divide en 0. La parte de $-\infty$ a 0 es la mitad del área de $h$, es decir, $\frac12H(0)=\frac12$, porque $h$ es par. Para el resto se sustituye $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$: $\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$. El valor $\operatorname{Si}(\infty)=\frac\pi2$ se obtiene del teorema del área: $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$, por tanto $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$.
:::

⁠**Cómo leerlo:** en $t=0$, la respuesta vale exactamente $\frac12$; empieza ya antes (no es causal) y tiende a 1. El __tiempo de subida__ $t_e$ se define como el tiempo que tarda en subir una rampa con la pendiente máxima de la respuesta al escalón. La pendiente máxima es $h(0)=2f_\mathrm g$; por tanto,

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

La sobreoscilación de la respuesta al escalón es del $8{,}95\,\%$ (en $t=\frac{1}{2f_\mathrm g}$). Es el fenómeno de Gibbs de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): un $f_\mathrm g$ mayor acorta el tiempo de subida; la sobreoscilación se mantiene (fig. [1](#abb-1)).

:::abbildung et3/k5sprung
Respuesta al escalón del paso bajo ideal para $f_\mathrm g=1$ Hz y 2 Hz. En trazo discontinuo, la rampa con la pendiente máxima: su tiempo de subida es $t_e=1/(2f_\mathrm g)=0{,}5$ s. Las dos curvas tienen la misma sobreoscilación: llegan hasta 1,0895.
:::

:::frage Un paso bajo con más ancho de banda es «mejor», ¿no? Entonces, ¿por qué no disminuye la sobreoscilación?
Porque se debe a la *forma* de la respuesta en frecuencia, no a su anchura. La sobreoscilación surge en el flanco vertical en $f_\mathrm g$: todas las frecuencias hasta ahí llegan completas, y de las superiores no llega nada. Si se desplaza el flanco, sigue vertical, y la respuesta al escalón solo se comprime en el tiempo. La sobreoscilación solo disminuye si el flanco se vuelve suave (etapa [5](#stufe-5)).
:::

:::aufgabe Ejercicio 3 ★★ Seno integral
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Demuestra que $h_\varepsilon(0)=\frac12$ y $h_\varepsilon(\infty)=1$ con [(3.1)](#gl-3-1).

</li>

<li>

¿Dónde está el máximo de la respuesta al escalón? Pista: la derivada de la respuesta al escalón es la respuesta al impulso.

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$, $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$.

(b) La pendiente de la respuesta al escalón es $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$. Se anula por primera vez en $2\pi f_\mathrm gt=\pi$ y ahí pasa de positiva a negativa. Por tanto, el máximo está en $t=\frac{1}{2f_\mathrm g}$ y vale $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1{,}852}{\pi}=1{,}0895$.
:::
:::

## Etapa 4: Aproximación causal

<span class="anker" id="stufe-4"></span>

:::zweck
¿Cómo se construye algo que se acerque lo más posible al paso bajo ideal? Se retrasa la respuesta al impulso y se corta el resto.
:::

**La idea.** Se desplaza $h(t)$ hacia la derecha en $t_0$ hasta que la parte en $t<0$ sea despreciable, y se corta. La envolvente de la función si decrece como $1/(2\pi f_\mathrm g|t|)$. Si antes de $t=0$ debe ser inferior al 1 % del máximo, hace falta $t_0\approx16/f_\mathrm g$. Con una ventana simétrica de anchura $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**Cómo leerlo:** cortar es multiplicar por una ventana; en el espectro, por tanto, es una convolución con el espectro si de la ventana. El flanco abrupto se difumina y aparecen ondulaciones. El factor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ es el retardo: el filtro causal tiene fase lineal; retrasa todas las frecuencias por igual (fig. [2](#abb-2)). Cuanto mayor es $t_0$, más estrecha es la transición, pero más tarde llega la respuesta.

:::abbildung et3/k5kausal
Módulo del paso bajo causal enventanado con $f_\mathrm g=1$ Hz y $t_0=3$ s (azul); en trazo discontinuo, el ideal. En el flanco aparece una zona de transición con $|H_k(f_\mathrm g)|=0{,}49$, y antes de ella, ondulaciones de hasta 1,10.
:::

:::aufgabe Ejercicio 4 ★★ ¿Cuánto retardo cuesta la causalidad?
<span class="anker" id="aufg-4"></span>

Un paso bajo con $f_\mathrm g=1$ kHz debe aproximarse de forma causal. El paso bajo ideal desplazado debe quedar por debajo del 1 % de su máximo antes de $t=0$, es decir, en la parte cortada.

<ol class="al">

<li>

¿Qué valor mínimo debe tener $t_0$?

</li>

<li>

¿Qué supone esto para una llamada telefónica con diez de estos filtros en cadena?

</li>

</ol>

:::loesung
(a) La envolvente $\frac{1}{2\pi f_\mathrm g|t|}<0{,}01$ exige $|t|>\frac{100}{2\pi f_\mathrm g}=15{,}9$ ms. Por tanto, $t_0\approx16$ ms.

(b) Diez filtros retrasan unos 0,16 s. En la llamada, esto se nota como retardo. La causalidad de un filtro abrupto cuesta tiempo, y tanto más cuanto más estrecha es la banda.
:::
:::

## Etapa 5: Método de ecos y filtros conformadores de pulsos

<span class="anker" id="stufe-5"></span>

:::zweck
¿Cómo se diseña un paso bajo con menos sobreoscilación? Se compone la respuesta al impulso a partir de funciones si desplazadas y se eligen sus pesos.
:::

**Método de ecos.** Según el teorema de muestreo, toda respuesta al impulso de un paso bajo hasta $f_\mathrm g=\frac{1}{2T}$ es una serie de funciones si:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

Cada muestra $h(nT)$ es un __eco__: una función si desplazada en $nT$. En el espectro, esto se convierte en una serie de Fourier en $f$. Si $h$ es real y par, $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$.

**Filtro conformador de pulsos.** A la componente principal $\operatorname{si}(\pi t/T)$ se añaden dos ecos de amplitud $a$ a una distancia de $\pm T$. Con $a=\frac12$, las oscilaciones secundarias se cancelan en gran parte, y el espectro adquiere un flanco suave de forma cosenoidal:

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

Este es el __filtro de coseno alzado__. Su sobreoscilación es del 2,7 % en lugar del 21,7 %; a cambio, el lóbulo principal es el doble de ancho (primer cero en $2T$ en lugar de $T$). La figura [3](#abb-3) muestra ambas respuestas al impulso normalizadas a la misma área.

:::abbildung et3/k5pulsform
Respuestas al impulso del paso bajo ideal y del filtro conformador de pulsos (ambas con área $T$). El filtro conformador de pulsos decae mucho más rápido: su mayor máximo secundario es el 2,7 % del máximo principal, en lugar del 21,7 %.
:::

**Filtro transversal.** Una suma de copias retardadas y ponderadas se construye con una cadena de elementos de retardo cuyas tomas se ponderan y se suman. Para que ningún elemento deba acceder al futuro, se retrasa todo en bloque. Es la misma estructura que un filtro FIR ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

:::aufgabe Ejercicio 5 ★★ El filtro de coseno alzado
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Deduce $H(f)$ en [(5.3)](#gl-5-3) a partir de [(5.1)](#gl-5-1).

</li>

<li>

¿Qué valor tiene $H$ en $f=0$ y en $f=f_\mathrm g=\frac{1}{2T}$? ¿Por qué el flanco es suave ahí?

</li>

</ol>

:::loesung
(a) En $t=mT$, $\operatorname{si}(\pi(t\pm T)/T)$ solo vale 1 para $m=\mp1$; en los demás casos es nula. Por tanto, $h(0)=1$, $h(\pm T)=\frac12$ y todos los demás $h(nT)=0$. Según [(5.1)](#gl-5-1): $H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$.

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. También la pendiente $-2\pi T^2\sin(2\pi Tf)$ es nula en $f=\frac{1}{2T}$. La respuesta en frecuencia llega a cero sin salto y sin punto anguloso. Cuanto más suave es el espectro, más rápido decae la respuesta al impulso ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::

## Etapa 6: Paso bajo en tiempo discreto, diseño con ventanas

<span class="anker" id="stufe-6"></span>

:::zweck
¿Cómo se diseña un paso bajo digital? Exactamente igual que el analógico causal: se toma el paso bajo ideal, se retrasa y se trunca con una ventana.
:::

El paso bajo ideal en tiempo discreto tiene la respuesta en frecuencia rectangular repetida periódicamente y la respuesta al impulso

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

es decir, en el modelo de referencia ($f_\mathrm g=0{,}2$), $h(0)=0{,}4$, $h(\pm1)=0{,}303$, $h(\pm2)=0{,}094$, $h(\pm3)=-0{,}062$. Tampoco este es causal. Se multiplica por una ventana $w(n)$ de $2N+1$ valores, se desplaza $N$ y se obtiene un filtro FIR de fase lineal. La ventana determina el resultado (fig. [4](#abb-4)):

<ul>

<li>

⁠**Ventana rectangular:** la transición más abrupta, pero lóbulos secundarios altos. En el modelo de referencia ($N=10$), la banda de rechazo a partir de $f=0{,}3$ todavía alcanza $-26{,}6$ dB, y la banda de paso fluctúa en aproximadamente $\pm0{,}5$ dB.

</li>

<li>

⁠**Ventana de Hann:** transición más suave, pero una banda de rechazo mucho más profunda: a partir de $f=0{,}3$ como máximo $-45{,}9$ dB; la banda de paso es plana con un margen de $0{,}05$ dB.

</li>

</ul>

La razón es la misma que en la transformada de Fourier de tiempo corto de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): el espectro de la ventana se convoluciona con el ideal, y los bordes abruptos del rectángulo producen lóbulos secundarios que decrecen lentamente.

:::abbildung et3/k5fenster
Módulo de la respuesta en frecuencia de dos filtros FIR paso bajo con $f_\mathrm g=0{,}2$ y 21 coeficientes. Ventana rectangular: flanco abrupto, a partir de $f=0{,}3$ atenuación solo hasta $-26{,}6$ dB. Ventana de Hann: flanco más tendido, a partir de $f=0{,}3$ como máximo $-45{,}9$ dB.
:::

:::aufgabe Ejercicio 6 ★ Filtro de media banda
<span class="anker" id="aufg-6"></span>

Calcula los coeficientes $h(0)$ a $h(3)$ del paso bajo ideal en tiempo discreto con $f_\mathrm g=0{,}25$. ¿Qué llama la atención y por qué ahorra esto trabajo de cálculo en un filtro FIR?

:::loesung
$h(n)=0{,}5\operatorname{si}(\pi n/2)$: $h(0)=0{,}5$, $h(\pm1)=\frac1\pi=0{,}318$, $h(\pm2)=0$, $h(\pm3)=-\frac{1}{3\pi}=-0{,}106$. Todos los coeficientes pares, salvo $h(0)$, son nulos, porque $\sin(\pi n/2)=0$ para $n$ par. En el filtro FIR desaparecen estas multiplicaciones, casi la mitad.
:::
:::

## Etapa 7: El paso banda ideal y su paso bajo equivalente

<span class="anker" id="stufe-7"></span>

:::zweck
Un paso banda deja pasar una banda en torno a la frecuencia central $f_0$. Esta etapa muestra que se puede describir por completo mediante un paso bajo y la frecuencia $f_0$.
:::

**Paso banda ideal.** Dos rectángulos de anchura $\Delta f$ en $\pm f_0$ ($f_0>\Delta f/2$):

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

La respuesta al impulso es una oscilación de frecuencia $f_0$ cuya envolvente es la respuesta al impulso de un paso bajo de ancho de banda $\Delta f/2$. La regla de modulación de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) lo explica: es un paso bajo cuyo espectro se desplaza a $\pm f_0$.

**Paso bajo equivalente.** Con una respuesta al impulso real, $H(-f)=H^*(f)$: la mitad negativa no contiene nada nuevo. Se conservan solo las frecuencias positivas, se duplican y se desplazan hacia la izquierda una frecuencia portadora $f_0$. El resultado es el __paso bajo equivalente__ $H_T(f)$:

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{para}\ f\le-f_0. \tag{7.2}$$

$H_T$ no tiene por qué ser simétrico respecto a $f=0$; por tanto, su respuesta al impulso $h_T(t)$ puede ser compleja. Si existe un $f_0$ para el que se cumple $H_T(-f)=H_T^*(f)$ (y, por tanto, $h_T$ es real), el paso banda se llama __simétrico__. En el paso banda ideal con $f_0$ en el centro, $H_T(f)=2\operatorname{rect}(f/\Delta f)$ y $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, real y par. Es un caso especial: también los filtros paso banda simétricos tienen, por lo general, una parte imaginaria en el espectro.

:::aufgabe Ejercicio 7 ★★ Paso bajo equivalente con otra referencia
<span class="anker" id="aufg-7"></span>

Paso banda ideal de 9 a 11 Hz.

<ol class="al">

<li>

Determina $H_T$ y $h_T$ para $f_0=10$ Hz.

</li>

<li>

Determina $H_T$ y $h_T$ para $f_0=9$ Hz. ¿Por qué ahora $h_T$ es compleja? ¿Describen ambos el mismo paso banda?

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz: tras el desplazamiento, la banda queda simétrica, de $-1$ a $1$ Hz. $H_T=2\operatorname{rect}(f/2)$, $h_T=4\operatorname{si}(2\pi t)$, real.

(b) $f_0=9$ Hz: la banda va de 0 a 2 Hz. $H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$, $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$. Es compleja porque $H_T$ no es simétrico respecto a $f=0$. Ambos describen el mismo paso banda: $\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$, lo mismo que en (a) y que [(7.1)](#gl-7-1).
:::
:::

## Etapa 8: Envolvente compleja y componentes en cuadratura

<span class="anker" id="stufe-8"></span>

:::zweck
Lo que vale para los sistemas vale también para las señales: una señal paso banda es una señal paso bajo sobre una portadora. Esta etapa muestra las distintas formas de escribirlo.
:::

La transformada inversa de [(7.2)](#gl-7-2) da, con la regla de modulación, $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$; por tanto, como $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ se llama __envolvente compleja__, y $\mathrm{e}^{\mathrm{j}2\pi f_0t}$, __portadora compleja__. La mitad de su producto es la componente analítica de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$; es decir, $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Teorema 8.1 (Representación en cuadratura)
<span class="anker" id="satz-8-1"></span>

Con $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ y la transformada de Hilbert $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**Cómo leerlo:** $s_{Tr}$ y $s_{Ti}$ se llaman __componentes en cuadratura__ (en fase y en cuadratura): una modula el coseno de la portadora, y la otra, el seno. $|s_T|$ es la __envolvente__, que en un osciloscopio se ve como el «contorno» de la señal, y $\varphi_T$ es la desviación de fase de la portadora. Si la envolvente compleja es real (caso simétrico), $s(t)=s_T(t)\cos(2\pi f_0t)$: un coseno modulado en amplitud.

:::herleitung Componentes en cuadratura
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. Para [(8.3)](#gl-8-3), con $2s_+=s+\mathrm{j}\hat s$ ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Ejercicio 8 ★★ Determinar envolventes complejas
<span class="anker" id="aufg-8"></span>

Determina $s_T$, $s_{Tr}$, $s_{Ti}$ y $|s_T|$ respecto a $f_0=10$ Hz para (a) $s(t)=\bigl[1+0{,}5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0{,}3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Comprueba (c) con [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0{,}5\cos(2\pi t)$, real: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0{,}5\cos(2\pi t)$, entre 0,5 y 1,5. Un coseno modulado en amplitud.

(b) $s_T=\mathrm{e}^{\mathrm{j}0{,}3}$: $s_{Tr}=\cos0{,}3=0{,}955$, $s_{Ti}=\sin0{,}3=0{,}296$, $|s_T|=1$. La envolvente es constante; solo la fase está desplazada en 0,3.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$; por tanto, $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Comprobación: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::

## Etapa 9: Señal paso banda en un sistema paso banda

<span class="anker" id="stufe-9"></span>

:::zweck
La utilidad de las envolventes: el efecto de un paso banda sobre una señal paso banda se calcula por completo en el dominio paso bajo.
:::

:::satz Teorema 9.1 (Transmisión en el dominio paso bajo equivalente)
<span class="anker" id="satz-9-1"></span>

Si $S_T$ y $H_T$ cumplen ambos [(7.2)](#gl-7-2) (nada por debajo de $-f_0$), para la envolvente de la salida se cumple

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Transmisión
Al desarrollar $G=S\cdot H$ con ambas representaciones [(7.2)](#gl-7-2) se obtienen cuatro productos. Los cruzados, por ejemplo $S_T(f-f_0)H_T^*(-f-f_0)$, son nulos: el primer factor vive en las frecuencias positivas, y el segundo, en las negativas. Queda $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. La comparación con $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ da $G_T=\frac12S_TH_T$.
:::

⁠**Cómo leerlo:** el factor $\frac12$ compensa que $S_T$ y $H_T$ se hayan duplicado ambos. Por lo demás, es el teorema de convolución habitual, solo que para las envolventes. Ni siquiera hace falta incluir la portadora en el cálculo.

**Ejemplo: coseno conectado que atraviesa el paso banda ideal.** $s(t)=\varepsilon(t)\cos(2\pi f_0t)$ con $f_0=10$ Hz; paso banda con $\Delta f=2$ Hz en torno a $f_0$. La envolvente de la entrada es $s_T\approx\varepsilon(t)$. (Aproximación: el espectro del escalón no está limitado a $f>-f_0$, pero en la banda de paso, $|f|\le\Delta f/2\ll f_0$, es válida.) Con $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

La envolvente es la respuesta al escalón de un paso bajo ideal con $f_\mathrm g=\Delta f/2$: tiempo de subida $1/\Delta f=0{,}5$ s, sobreoscilación del 8,95 % (fig. [5](#abb-5)). Un paso banda estrecho tarda mucho en alcanzar el «régimen permanente».

:::abbildung et3/k5bandpass
Respuesta del paso banda ideal ($f_0=10$ Hz, $\Delta f=2$ Hz) a un coseno de la frecuencia central conectado en $t=0$. En azul, la señal de salida; en rojo, la envolvente $\pm g_T(t)$. Sube en aproximadamente 0,5 s y, con la sobreoscilación, llega hasta 1,09.
:::

:::ltspice Portadora conectada a través de un circuito resonante
Un paso banda ideal no se puede construir; un circuito resonante serie, sí. **Esquema:** fuente `voltage` en el nodo `in` y luego, en serie, `ind` con `{L}`, `cap` con `{1/((2*pi*f0)**2*L)}` y `res` con `{2*pi*df*L}` a masa. La salida `out` es la tensión en la resistencia. Con `.param f0=10 df=2 L=1`, la frecuencia central es 10 Hz, y el ancho de banda entre los puntos de $-3$ dB, 2 Hz.

⁠**Comprobación:** el valor de fuente `AC 1` y `.ac lin 2001 5 15` muestran el máximo 1 en 10 Hz y los puntos de $-3$ dB en 9,05 Hz y 11,05 Hz.

⁠**Experimento:** fuente `SINE(0 1 10 0 0 90)`, que es $\varepsilon(t)\cos(2\pi f_0t)$, y `.tran 0 3 0 0.1m`. La envolvente sube sin sobreoscilación: los picos de la portadora alcanzan 0,72 a los 0,2 s, 0,96 a los 0,5 s y prácticamente 1 al cabo de 1 s, casi exactamente como $1-\mathrm{e}^{-t/0{,}16\,\mathrm s}$. El paso banda ideal, en cambio, sobreoscila hasta 1,09 (fig. [5](#abb-5)). La razón es la misma que en el paso bajo de la etapa [3](#stufe-3): los flancos del circuito resonante son suaves; los del paso banda ideal, verticales.
:::

## Etapa 10: Esquema en cuadratura y muestreo paso banda

<span class="anker" id="stufe-10"></span>

:::zweck
¿Cómo se obtienen técnicamente las componentes en cuadratura? ¿Y cuántas muestras necesita una señal paso banda?
:::

**Esquema en cuadratura.** Si se multiplica una señal paso banda por $\cos(2\pi f_0t)$ y se filtra con un paso bajo, queda $\frac12s_{Tr}$. Con $-\sin(2\pi f_0t)$ queda $\frac12s_{Ti}$. La razón es trigonométrica:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{en }2f_0,\text{ los elimina el paso bajo}},$$

y, del mismo modo, $-s\sin=\frac12s_{Ti}+(\text{componentes en }2f_0)$. La condición es que la banda termine por debajo de $2f_0$. En el dominio paso bajo se filtra entonces con cuatro filtros paso bajo ($h_{Tr}$, $\pm h_{Ti}$) según [(9.1)](#gl-9-1). A la salida se vuelve a modular sobre la portadora según [(8.2)](#gl-8-2), o se forma la envolvente $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (fig. [6](#abb-6)).

:::abbildung et3/k5quadratur
Demodulador en cuadratura: obtiene de una señal paso banda las dos componentes en cuadratura, es decir, la envolvente compleja.
:::

**Teorema de muestreo para señales paso banda.** Una señal paso banda de ancho de banda $\Delta f$ tiene, respecto a la frecuencia central, componentes en cuadratura que son señales paso bajo hasta $\Delta f/2$. Cada una puede muestrearse con $1/T=\Delta f$:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

En total hacen falta $2\Delta f$ valores por segundo, tantos como para una señal paso bajo con frecuencia de corte $\Delta f$. Por tanto, lo que importa es el ancho de banda, no la frecuencia más alta.

:::aufgabe Ejercicio 9 ★★ Muestrear una señal de radio
<span class="anker" id="aufg-9"></span>

Una señal ocupa la banda de 10,0 a 10,2 MHz.

<ol class="al">

<li>

¿Qué frecuencia de muestreo haría falta según el teorema de muestreo ordinario?

</li>

<li>

¿Cuántas muestras por segundo bastan en total con el esquema en cuadratura, y con qué frecuencia se muestrea cada rama?

</li>

</ol>

:::loesung
(a) Al menos $2\cdot10{,}2=20{,}4$ MHz.

(b) $\Delta f=0{,}2$ MHz. Cada rama se muestrea con 0,2 MHz ($T=5$ µ s); en total, 0,4 MHz, unas cincuenta veces menos.
:::
:::

## Etapa 11: Retardo de fase y de grupo en el paso banda

<span class="anker" id="stufe-11"></span>

:::zweck
¿Por qué hay dos retardos? Porque la portadora y la envolvente pueden retrasarse de forma distinta.
:::

**La idea.** Supongamos que un paso banda tiene en la banda de paso un módulo constante y una fase ligeramente curvada. En torno a $f_0$, esta se aproxima por su tangente:

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

con $t_\mathrm p=t_\mathrm p(f_0)$ y $t_\mathrm g=t_\mathrm g(f_0)$ de [(1.4)](#gl-1-4) y [(1.5)](#gl-1-5). En el dominio paso bajo ($f-f_0\to f$), esto es $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$: una fase constante y un retardo.

:::satz Teorema 11.1 (Retardos en el paso banda)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**Cómo leerlo:** la envolvente, que transporta la información, sufre el *retardo de grupo*. La portadora sufre el *retardo de fase*. La transmisión solo está libre de distorsión en sentido estricto si ambos son iguales. Es decir, la recta de fase pasa por el origen (o por un múltiplo de $2\pi$ en $f=0$). Para la información suele bastar ya con un retardo de grupo constante: si $t_\mathrm g$ no es constante, las distintas componentes de frecuencia de la envolvente llegan en instantes distintos y los pulsos se ensanchan (__distorsión de retardo__).

:::ltspice La envolvente y la portadora llegan en instantes distintos
⁠**Esquema:** el circuito resonante del recuadro LTspice de la etapa [9](#stufe-9) ($f_0=10$ Hz, $\Delta f=2$ Hz). En el análisis `.ac`, su fase en 10 Hz es $0^\circ$; por tanto, $t_\mathrm p(f_0)=0$. Si cambias el eje de fase a «Group Delay», muestra en 10 Hz $t_\mathrm g(f_0)=0{,}16$ s.

⁠**Experimento:** como entrada, una fuente de comportamiento `bv`, una portadora con una envolvente que varía lentamente:

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

Directivas `.tran 0 20 0 0.2m` y `.options plotwinsize=0`.

⁠**Lo que ves:** dibuja `V(in)` y `V(out)` superpuestas y amplía el tramo de 14,5 s a 15,5 s. El máximo de la envolvente llega a la salida unos 0,16 s más tarde, pero los pasos por cero de la portadora están en los mismos sitios que en la entrada. Es exactamente lo que dice [(11.1)](#gl-11-1): la envolvente se retrasa $t_\mathrm g$, y la portadora, $t_\mathrm p$.
:::

:::aufgabe Ejercicio 10 ★★ Leer los retardos
<span class="anker" id="aufg-10"></span>

En $f_0=1$ MHz, un paso banda tiene la fase $\varphi(f_0)=-\pi/2$ y la pendiente $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$.

<ol class="al">

<li>

Calcula $t_\mathrm p$ y $t_\mathrm g$.

</li>

<li>

¿Cuánto se retrasa la envolvente de un pulso a la salida? ¿Está después la portadora todavía en la misma posición respecto a la envolvente?

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0{,}25$ µ s. $t_\mathrm g=2$ µ s.

(b) La envolvente llega 2 µ s más tarde. La portadora solo está desplazada 0,25 µ s. Respecto a la envolvente, está por tanto girada $2\pi f_0(t_\mathrm g-t_\mathrm p)=3{,}5\pi$, que módulo $2\pi$ es igual a $1{,}5\pi$, es decir, $-\pi/2$: un cuarto de periodo. La información de la envolvente se conserva sin distorsión mientras $t_\mathrm g$ sea constante en toda la banda.
:::
:::

## Etapa 12: Paso banda y paso alto en tiempo discreto

<span class="anker" id="stufe-12"></span>

:::zweck
Los filtros paso banda y paso alto digitales se obtienen a partir de un paso bajo mediante modulación.
:::

Si el paso bajo en tiempo discreto tiene una respuesta al impulso real, la multiplicación por $2\cos(2\pi f_0n)$ desplaza su banda de paso a $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

válido mientras las bandas desplazadas no se solapen: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Debido a la periodicidad, la banda en $f_0$ no puede tocar ni la banda en $-f_0$ ni su copia en $1-f_0$. En general, también para respuestas al impulso paso bajo complejas, se cumple, como en [(8.1)](#gl-8-1), $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$. El factor 2 corresponde al paso bajo equivalente duplicado, $H_T=2H_{\mathrm{TP}}$.

Un __paso alto__ es un paso bajo desplazado a la mitad de la frecuencia de muestreo, $f_0=\frac12$. Allí coinciden la banda y su imagen especular; por eso se desplaza solo una vez: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. Con $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**En resumen:** un paso alto digital se obtiene de un paso bajo invirtiendo uno de cada dos signos.

:::aufgabe Ejercicio 11 ★ Paso alto a partir de la media móvil
<span class="anker" id="aufg-11"></span>

La media móvil $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) es un paso bajo sencillo.

<ol class="al">

<li>

Forma $h_{\mathrm{HP}}$ según [(12.2)](#gl-12-2).

</li>

<li>

Calcula $H_{\mathrm{TP}}$ y $H_{\mathrm{HP}}$ en $f=0$ y en $f=\frac12$. ¿Encaja esto con un paso alto?

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$.

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$: $|H_{\mathrm{TP}}(0)|=1$, $|H_{\mathrm{TP}}(\frac12)|=\frac13$. El paso alto está desplazado $\frac12$: $|H_{\mathrm{HP}}(0)|=\frac13$, $|H_{\mathrm{HP}}(\frac12)|=1$. Deja pasar completa la secuencia más rápida $(+1,-1,+1,\dots)$ y atenúa la componente continua a un tercio. Un paso alto sencillo, no muy abrupto.
:::
:::

:::kern Lo esencial
<ul>

<li>

Sin distorsión: $h=h_0\delta(t-t_0)$, $H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: módulo constante, fase lineal.

</li>

<li>

$a=-20\lg|H|$ dB; $t_\mathrm p=-\frac{\varphi}{2\pi f}$; $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$.

</li>

<li>

Paso bajo ideal: $\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$, no causal; $f_\mathrm g t_m=\frac12$; sobreoscilación del 21,7 % (impulso) y del 8,95 % (escalón).

</li>

<li>

Respuesta al escalón $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$, $\operatorname{Si}(\infty)=\frac\pi2$, tiempo de subida $\frac{1}{2f_\mathrm g}$.

</li>

<li>

Truncar la respuesta al impulso $=$ convolución en el espectro; ventanas suaves: mayor rechazo, flanco más tendido.

</li>

<li>

Filtro conformador de pulsos: $T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$, poca sobreoscilación.

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$; $s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$; $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

</li>

<li>

$g_T=\frac12s_T*h_T$; la envolvente se retrasa $t_\mathrm g$, y la portadora, $t_\mathrm p$.

</li>

<li>

Muestreo paso banda: $2\Delta f$ valores por segundo; paso alto digital: $(-1)^nh_{\mathrm{TP}}(n)$.

</li>

</ul>
:::
