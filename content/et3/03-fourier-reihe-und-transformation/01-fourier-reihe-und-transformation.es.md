---
title: Serie de Fourier y transformada de Fourier
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Serie y transformada de Fourier
order: 3230100
summary: Toda señal como superposición de oscilaciones
tags: espectro, respuesta en frecuencia, frecuencia fundamental, armónicos, serie de Fourier, componente continua, ortogonales, potencia
lang: es
---

## De qué trata

La [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) ha mostrado que toda señal es una superposición de bloques $\mathrm{e}^{pt}$ y que un sistema LTI solo multiplica cada bloque por un número. La descripción de Fourier usa de ellos únicamente los bloques del eje imaginario, $p=\mathrm{j}2\pi f$: oscilaciones puras $\mathrm{e}^{\mathrm{j}2\pi ft}$, que ni crecen ni decaen. Esto tiene una gran ventaja. Una oscilación tiene una frecuencia que se puede oír, medir y filtrar. El __espectro__ $S(f)$ indica con qué amplitud y con qué fase está contenida cada frecuencia en la señal.

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Una señal periódica es una suma de oscilaciones en múltiplos de la frecuencia fundamental (serie de Fourier); una señal no periódica, una integral sobre todas las frecuencias (integral de Fourier).

</li>

<li>

Cada oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ es una función propia: un sistema LTI la multiplica por $H(f)$, y por eso la convolución se convierte en el producto $G(f)=S(f)\,H(f)$.

</li>

<li>

Todas las reglas de cálculo (desplazamiento, dilatación, modulación, simetría) se deducen de lo que cada operación hace con una única oscilación.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.**

| Resultado | De dónde viene |
|---|---|
| Respuesta en frecuencia $H(f)$ | valor propio de la oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ (etapa [1](#stufe-1)) |
| Serie de Fourier, solo múltiplos de $F$ | solo estas oscilaciones tienen el periodo $T$ (etapa [2](#stufe-2)) |
| Fórmula de análisis de la serie | las oscilaciones de frecuencias distintas son ortogonales (etapa [2](#stufe-2)) |
| Parseval, Gibbs, LTI con entrada periódica | cada armónico por separado (etapa [3](#stufe-3)) |
| Integral de Fourier | periodo $\to\infty$, las líneas se acercan entre sí (etapa [4](#stufe-4)) |
| $S(-f)=S^*(f)$ en señales reales | las oscilaciones aparecen en pares conjugados (etapa [5](#stufe-5)) |
| Desplazamiento, dilatación, derivación, modulación | lo que la operación hace con $\mathrm{e}^{\mathrm{j}2\pi ft}$ (etapa [6](#stufe-6)) |
| Simetría (dualidad) | la transformada directa y la inversa solo se diferencian en el signo (etapa [6](#stufe-6)) |
| Espectros de líneas, peine de Dirac, escalón | casos límite con impulsos de Dirac (etapa [8](#stufe-8)) |
| Transformada de Hilbert | una señal causal queda determinada por una mitad (etapa [9](#stufe-9)) |
| Fourier de tiempo corto | espectro de un fragmento (etapa [10](#stufe-10)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este artículo
<ul>

<li>

⁠**Onda cuadrada** entre 0 y 1 con periodo $T=2\pi$ s y ciclo de trabajo $\frac12$: 1 para $|t|\le T/4$, 0 para $T/4<|t|\le T/2$, prolongada periódicamente. Frecuencia fundamental $F=1/T=0{,}159$ Hz, es decir, $2\pi F=1/\mathrm s$.

</li>

<li>

⁠**Paso bajo RC** con $RC=1$ s, $H(f)=1/(1+\mathrm{j}2\pi f\,RC)$. En el $k$-ésimo armónico de la onda cuadrada, $2\pi kF\cdot RC=k$, es decir, $H(kF)=1/(1+\mathrm{j} k)$.

</li>

<li>

⁠**Pulso rectangular** $\operatorname{rect}(t)$ y $\operatorname{si}(x)=\sin(x)/x$.

</li>

</ul>

El script `rechnung_kap3.py` recalcula los números y las curvas.
:::

## Etapa 1: Las oscilaciones como funciones propias

<span class="anker" id="stufe-1"></span>

:::zweck
De los bloques $\mathrm{e}^{pt}$ se usan ahora solo las oscilaciones puras. Esta etapa muestra qué hace con ellas un sistema LTI.
:::

Para $p=\mathrm{j}2\pi f$ puramente imaginario, el bloque se convierte en una oscilación de amplitud constante:

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

Como todo bloque, es una función propia de todo sistema LTI (retrasar es multiplicar por $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$):

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ se llama __respuesta en frecuencia__ o función de transferencia. Su módulo indica cuánto se amplifica o se atenúa la oscilación de frecuencia $f$; su fase, cuánto se desplaza. Dos sistemas en cascada multiplican uno tras otro: $H(f)=H_1(f)H_2(f)$. Donde la transformada de Laplace $H(p)$ existe en el eje imaginario, $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

⁠**En resumen:** la respuesta en frecuencia es el número por el que un sistema LTI multiplica una oscilación pura.

## Etapa 2: Señales periódicas, la serie de Fourier

<span class="anker" id="stufe-2"></span>

:::zweck
Una señal periódica se repite al cabo de $T$. Se puede componer a partir de oscilaciones, pero solo de unas muy concretas. Esta etapa muestra de cuáles y cómo se hallan sus pesos.
:::

**La idea.** Una oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ se repite al cabo de $T$ si y solo si $fT$ es un número entero. Por tanto, en una señal de periodo $T$ solo aparecen las frecuencias $f_k=kF$, con la __frecuencia fundamental__ $F=1/T$; son los __armónicos__:

<span class="anker" id="gl-2-1"></span>
$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}. \tag{2.1}$$

Esta es la __serie de Fourier__ (síntesis). $S_p(k)$ es el peso complejo del $k$-ésimo armónico.

**Señales reales.** Para una señal real, $s_p=s_p^*$. Al conjugar [(2.1)](#gl-2-1), $\mathrm{e}^{\mathrm{j}2\pi kFt}$ se convierte en la oscilación con $-k$. Comparando los coeficientes se obtiene

$$S_p(-k)=S_p^*(k).$$

Cada par $k,-k$ da entonces $2\operatorname{Re}\{S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\}$, una oscilación cosenoidal real. Con $S_p(k)=|S_p(k)|\,\mathrm{e}^{\mathrm{j}\varphi_p(k)}$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} s_p(t)&=S_p(0)+2\sum_{k=1}^{\infty}|S_p(k)|\cos\bigl(2\pi kFt+\varphi_p(k)\bigr)\\ &=S_p(0)+2\sum_{k=1}^{\infty}\Bigl[\operatorname{Re}\{S_p(k)\}\cos(2\pi kFt)-\operatorname{Im}\{S_p(k)\}\sin(2\pi kFt)\Bigr]. \end{aligned} \tag{2.2|2.3}$$

La fase $\varphi_p(k)$ se determina como en cualquier número complejo, con $\arctan$ y la corrección de cuadrante ($+\pi$ si la parte real es negativa). $S_p(0)$ es la __componente continua__, el valor medio de la señal.

**Hallar los pesos: ortogonalidad.** ¿Cómo se extrae un único $S_p(n)$ de la suma? Se multiplica por $\mathrm{e}^{-\mathrm{j}2\pi nFt}$ y se promedia sobre un periodo. Al hacerlo desaparecen todos los demás armónicos:

<span class="anker" id="gl-2-4"></span>
$$\frac1T\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\,\mathrm{d} t=\begin{cases}1&k=n\\0&k\neq n\end{cases}. \tag{2.4}$$

Para $k\neq n$, el fasor $\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}$ da exactamente $|k-n|$ vueltas completas en el periodo, y su valor medio es cero. Para $k=n$ está quieto. Por eso, las oscilaciones de frecuencias distintas se llaman __ortogonales__. Queda:

:::satz Teorema 2.1 (Serie de Fourier)
<span class="anker" id="satz-2-1"></span>

Una señal de periodo $T=1/F$ y potencia finita tiene la representación [(2.1)](#gl-2-1) con

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

donde $t_1$ es arbitrario (análisis).
:::

⁠**Cómo leerlo:** $S_p(k)$ es el valor medio de la señal después de «girarla en sentido contrario» con el $k$-ésimo armónico. Si el armónico está en la señal, su fasor deja de girar y su contribución se conserva en el promedio. $S_p(0)$ es simplemente el valor medio.

:::herleitung Fórmula de análisis
Multiplicar [(2.1)](#gl-2-1) por $\mathrm{e}^{-\mathrm{j}2\pi nFt}$, integrar sobre un periodo e intercambiar suma e integral:

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

Para $k\neq n$, la integral vale $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$, porque $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$. Como el integrando tiene periodo $T$, se puede integrar sobre cualquier intervalo de longitud $T$.
:::

**Ejemplo: una serie finita.** $s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$. Con las fórmulas de Euler, los coeficientes se leen directamente, sin integrar:

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

es decir, $S_p(0)=1$, $S_p(\pm1)=1$, $S_p(2)=-\tfrac{\mathrm{j}}{2}$, $S_p(-2)=\tfrac{\mathrm{j}}{2}$, todos los demás nulos. Comprobación: $S_p(-2)=S_p^*(2)$.

**Ejemplo: la onda cuadrada.** Para el modelo de referencia (1 para $|t|\le T_1/2$, con $T_1=T/2$):

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

Con $T_1=T/2$: $S_p(0)=0{,}5$, $S_p(\pm1)=1/\pi=0{,}318$, $S_p(\pm2)=0$, $S_p(\pm3)=-0{,}106$, $S_p(\pm5)=0{,}064$. Faltan los armónicos pares, porque $\sin(\pi k/2)=0$ para $k$ par. Todos los coeficientes son reales porque la señal es par (etapa [5](#stufe-5)). La figura [1](#abb-1) los muestra para dos ciclos de trabajo: cuanto más estrecho es el pulso, más lentamente decrecen los coeficientes.

:::abbildung et3/k3koeff
Coeficientes de Fourier de la onda cuadrada (0/1) para dos anchuras de pulso. En trazo discontinuo, la envolvente $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$. Con $T_1=T/2$ faltan los armónicos pares; con $T_1=T/4$, uno de cada cuatro.
:::

:::frage ¿Por qué en una señal periódica no aparecen frecuencias entre los armónicos?
Porque cada oscilación de la suma tiene que tener ella misma el periodo $T$; si no, la suma no sería periódica. Una oscilación con $f=1{,}5F$ solo ha dado vuelta y media al cabo de $T$ y está en una posición distinta de la inicial. Ningún peso, por bien elegido que esté, puede compensarlo, porque las frecuencias distintas son ortogonales y no pueden anularse entre sí.
:::

:::aufgabe Ejercicio 1 ★ Leer los coeficientes
<span class="anker" id="aufg-1"></span>

$s_p(t)=\frac12+\cos\bigl(2\pi Ft+\frac\pi3\bigr)+\frac12\sin(6\pi Ft)$.

<ol class="al">

<li>

Determina todos los $S_p(k)$ con las fórmulas de Euler. Comprueba que $S_p(-k)=S_p^*(k)$.

</li>

<li>

Indica $|S_p(1)|$ y $\varphi_p(1)$ y compáralos con [(2.2)](#gl-2-2).

</li>

</ol>

:::loesung
(a) $\cos(x+\frac\pi3)=\frac12\mathrm{e}^{\mathrm{j}\pi/3}\mathrm{e}^{\mathrm{j} x}+\frac12\mathrm{e}^{-\mathrm{j}\pi/3}\mathrm{e}^{-\mathrm{j} x}$ y $\frac12\sin(3x)=\frac{1}{4\mathrm{j}}\mathrm{e}^{\mathrm{j}3x}-\frac{1}{4\mathrm{j}}\mathrm{e}^{-\mathrm{j}3x}$, con $x=2\pi Ft$:

$$S_p(0)=\tfrac12,\quad S_p(\pm1)=\tfrac12\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j},\quad S_p(3)=-\tfrac{\mathrm{j}}{4},\quad S_p(-3)=\tfrac{\mathrm{j}}{4},$$

todos los demás nulos. $S_p(-1)=S_p^*(1)$ y $S_p(-3)=S_p^*(3)$ se cumplen.

(b) $|S_p(1)|=\frac12$, $\varphi_p(1)=60^\circ$. En [(2.2)](#gl-2-2): $2\cdot\frac12\cos(2\pi Ft+60^\circ)$, exactamente el término coseno de la señal. (Potencia según Parseval: $\frac14+2\cdot\frac14+2\cdot\frac1{16}=0{,}875$.)
:::
:::

:::aufgabe Ejercicio 2 ★★ La onda cuadrada estrecha
<span class="anker" id="aufg-2"></span>

Onda cuadrada con $T_1=T/4$.

<ol class="al">

<li>

Calcula $S_p(0)$, $S_p(1)$, $S_p(2)$ y $S_p(4)$ a partir de [(2.6)](#gl-2-6).

</li>

<li>

¿Por qué $S_p(4)=0$? Interprétalo con la ortogonalidad: ¿cuántos periodos del cuarto armónico caben en el pulso?

</li>

</ol>

:::loesung
(a) $S_p(0)=\frac14$, $S_p(1)=\frac{\sin(\pi/4)}{\pi}=0{,}225$, $S_p(2)=\frac{\sin(\pi/2)}{2\pi}=0{,}159$, $S_p(4)=\frac{\sin\pi}{4\pi}=0$.

(b) El cuarto armónico tiene periodo $T/4$, exactamente la anchura del pulso. La fórmula de análisis integra $\mathrm{e}^{-\mathrm{j}2\pi4Ft}$ sobre el pulso, es decir, sobre exactamente una vuelta completa del fasor. El valor medio es cero. En general, $S_p(k)$ se anula cuando en el pulso cabe un número entero de periodos del $k$-ésimo armónico.
:::
:::

## Etapa 3: Potencia, convergencia y sistemas LTI

<span class="anker" id="stufe-3"></span>

:::zweck
¿Cuánto aporta cada armónico a la señal, con qué precisión aproxima una serie truncada la señal y qué hace un sistema LTI con una entrada periódica?
:::

:::satz Teorema 3.1 (Parseval para series de Fourier)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2. \tag{3.1}$$
:::

⁠**Cómo leerlo:** la __potencia__ media de la señal es la suma de las potencias de los armónicos individuales. Los términos cruzados desaparecen porque los armónicos distintos son ortogonales. Para la onda cuadrada, $L_s=\frac12$. La componente continua aporta $0{,}25$, es decir, el 50 %. Con $k=\pm1$ se llega al 90,5 %; con $|k|\le3$, al 95,0 %; con $|k|\le9$, al 98,0 %.

:::herleitung Parseval
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Al promediar sobre un periodo, según [(2.4)](#gl-2-4) solo queda $k=l$: $\sum_k|S_p(k)|^2$.
:::

**Serie truncada y fenómeno de Gibbs.** Si se toman solo los armónicos hasta $|k|\le N$, la __suma parcial__ es $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. La potencia del error $s_p-s_{p,N}$ es la suma de los $|S_p(k)|^2$ omitidos y tiende a cero para $N\to\infty$ si la señal tiene potencia finita. Sin embargo, en un salto queda una sobreoscilación (fig. [2](#abb-2)): se estrecha al crecer $N$, pero su altura tiende a aproximadamente el 9 % de la altura del salto (10,0 % con $N=3$, 9,1 % con $N=9$, 9,0 % con $N=27$, valor límite 8,95 %). Este es el __fenómeno de Gibbs__. No contradice la convergencia: el área bajo la sobreoscilación, y con ella la potencia del error, tiende igualmente a cero.

:::abbildung et3/k3gibbs
Sumas parciales de la onda cuadrada ($T=2\pi$ s) con los armónicos hasta $|k|\le N$. En los flancos queda una sobreoscilación de aproximadamente el 9 % de la altura del salto, que al crecer $N$ solo se vuelve más estrecha.
:::

**Entrada periódica en un sistema LTI.** Cada armónico es una función propia y se multiplica por $H(kF)$. Por eso la salida tiene el mismo periodo, y sus coeficientes son

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

En el modelo de referencia, $H(kF)=1/(1+\mathrm{j} k)$. La componente fundamental se transmite con $|H|=0{,}707$ y $-45^\circ$; el tercer armónico, con $0{,}316$ y $-71{,}6^\circ$; el quinto, con $0{,}196$ y $-78{,}7^\circ$. A la salida, el tercer armónico ya solo es el 15 % del primero, frente al 33 % a la entrada. El circuito RC redondea los flancos (fig. [3](#abb-3)). La salida oscila entre 0,041 y 0,959.

:::abbildung et3/k3rc
Onda cuadrada a través del paso bajo RC con $RC=1$ s, calculada como suma de armónicos con $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. La salida se carga y se descarga exponencialmente entre 0,041 y 0,959.
:::

:::frage ¿No es un cálculo con infinitos armónicos mucho más engorroso que la ecuación diferencial?
Para una única onda cuadrada a través de un circuito RC, sí: las curvas de carga y descarga pueden escribirse directamente. A cambio, la serie muestra *por qué* la salida tiene ese aspecto. Los flancos están formados por los armónicos altos, y son precisamente esos los que atenúa el circuito RC. Además, [(3.2)](#gl-3-2) funciona para cualquier sistema LTI, también para aquellos cuya ecuación diferencial ni siquiera se conoce, sino solo su respuesta en frecuencia medida.
:::

:::ltspice Onda cuadrada a través del circuito RC
⁠**Esquema:** circuito RC (`res` con `1Meg`, `cap` con `1u`) con la fuente `PULSE(0 1 0 1u 1u {pi} {2*pi})`: periodo $2\pi$ s, ciclo de trabajo $\frac12$.

⁠**Directivas:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` y `.options plotwinsize=0`. La última desactiva la compresión de datos; sin ella, `.four` calcula con poca precisión. `.four` descompone el último periodo en armónicos y escribe el resultado en el SPICE Error Log.

⁠**Lo que ves:** en régimen permanente, `V(out)` oscila entre 0,041 y 0,959. Para $k\ge1$, `.four` da las amplitudes $2|S_p(k)|$ de las oscilaciones cosenoidales de [(2.2)](#gl-2-2). En la entrada son 0,637; 0; 0,212; 0; 0,127: faltan los armónicos pares. En la salida, el tercer armónico ya solo es el 15 % del primero, en lugar del 33 %. Las fases en la salida son $45^\circ$, $71{,}6^\circ$ y $78{,}7^\circ$ mayores que en la entrada, porque `.four` cuenta un retraso como positivo. Divide por dos las amplitudes de salida y compara con tu resultado del ejercicio [3](#aufg-3)(b). La vista FFT (clic derecho en el diagrama, View, FFT) muestra las mismas líneas en los múltiplos impares de 0,159 Hz.
:::

:::aufgabe Ejercicio 3 ★★ Potencia y armónicos superiores
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Confirma con [(3.1)](#gl-3-1) que los armónicos $k=0,\pm1$ de la onda cuadrada aportan el 90,5 % de la potencia.

</li>

<li>

Calcula $|G_p(1)|$, $|G_p(3)|$, $|G_p(5)|$ para la salida del circuito RC. ¿Qué fracción de la potencia alterna de la salida (sin $k=0$) está en la componente fundamental si solo tienes en cuenta $k=\pm1,\pm3,\pm5$?

</li>

<li>

¿Por qué la salida ya parece «más sinusoidal» que la entrada?

</li>

</ol>

:::loesung
(a) $|S_p(0)|^2+2|S_p(1)|^2=0{,}25+2/\pi^2=0{,}25+0{,}2026=0{,}4526$, que es el 90,5 % de $0{,}5$.

(b) $|G_p(k)|=|S_p(k)|/\sqrt{1+k^2}$: $|G_p(1)|=0{,}2251$, $|G_p(3)|=0{,}0336$, $|G_p(5)|=0{,}0125$. Potencia alterna de estos armónicos: $2(0{,}0507+0{,}0011+0{,}0002)=0{,}1039$. La fracción de la componente fundamental es $0{,}0507/0{,}0519=97{,}5\,\%$. A la entrada, con los mismos armónicos, sería solo el 86,9 %.

(c) $|H(kF)|=1/\sqrt{1+k^2}\approx1/k$: los armónicos superiores se atenúan tanto más cuanto más altos son. Queda sobre todo la componente fundamental, y una señal que consiste casi solo en la componente fundamental es casi una senoide.
:::
:::

## Etapa 4: De la señal periódica a la no periódica

<span class="anker" id="stufe-4"></span>

:::zweck
Un pulso aislado no es periódico. Pero se puede entender como una señal periódica de periodo infinitamente largo. Al hacerlo, la suma se convierte en una integral.
:::

**La idea.** Se prolonga periódicamente un pulso $s(t)$ de duración menor que $T$. Los coeficientes de la serie son entonces valores de una función fija:

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

Si se duplica el periodo, la separación $F$ entre líneas se reduce a la mitad, y las líneas muestrean la misma envolvente $S(f)$ con el doble de densidad (fig. [4](#abb-4)). En el caso límite $T\to\infty$, la separación $F$ se convierte en el diferencial $\mathrm{d} f$, y la suma $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$, en la integral.

:::abbildung et3/k3grenz
Un pulso rectangular $\operatorname{rect}(t)$, prolongado periódicamente con $T=2$ s y $T=4$ s. Los coeficientes de Fourier multiplicados por $T$ están sobre la misma envolvente $S(f)=\operatorname{si}(\pi f)$, con separación $1/T$. Para $T\to\infty$ llenan la curva sin huecos.
:::

:::satz Teorema 4.1 (Transformada de Fourier)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

Notación abreviada: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ o $S(f)=\mathcal{F}\{s(t)\}$.
:::

⁠**Cómo leerlo:** $S(f)$ es una __densidad espectral__: peso por intervalo de frecuencia. Si $s$ es una tensión en V, $S$ tiene la unidad V/Hz. La transformada inversa compone la señal a partir de todas las oscilaciones, cada una con el peso $S(f)\,\mathrm{d} f$. Una condición suficiente para la existencia es $\int|s(t)|\mathrm{d} t<\infty$. La transformada de Fourier es la transformada de Laplace en el eje imaginario, $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$, siempre que el eje imaginario esté en la región de convergencia ([parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)).

⁠**La convolución se convierte en producto.** Como en la [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html): $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$. De $s*\delta=s$ se sigue $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, es decir, $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: el impulso de Dirac contiene todas las frecuencias con el mismo peso.

**Ejemplo: el pulso exponencial.** La respuesta al impulso del circuito RC, $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$:

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

Es la misma respuesta en frecuencia que da el cálculo de corriente alterna ([parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Por tanto, la respuesta al impulso contiene toda la información sobre el comportamiento en frecuencia.

:::frage ¿Qué diferencia hay entre $S_p(k)$ y $S(f)$, aparte de que una es discreta?
La unidad. $S_p(k)$ es una amplitud (V): el $k$-ésimo armónico tiene realmente esa intensidad. $S(f)$ es una densidad (V/Hz): en una señal no periódica, ninguna frecuencia aislada tiene una amplitud finita; solo una banda de frecuencias $\Delta f$ aporta aproximadamente $S(f)\,\Delta f$. Por eso $S_p(k)=F\cdot S(kF)$: cada línea representa una banda de anchura $F$.
:::

:::aufgabe Ejercicio 4 ★ El pulso exponencial bilateral
<span class="anker" id="aufg-4"></span>

Calcula $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$ para $a>0$ dividiendo la integral en $t<0$ y $t>0$. Demuestra que el resultado es real y par, y justifícalo con la simetría de la señal.

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

Real y par en $f$. Tiene que ser así: la señal es real y par; por tanto, su parte impar es nula, y con ella también $\operatorname{Im} S$ (etapa [5](#stufe-5)).
:::
:::

## Etapa 5: Simetrías en la señal y en el espectro

<span class="anker" id="stufe-5"></span>

:::zweck
Si una señal es real, par o impar se ve de inmediato en su espectro. Esta etapa deduce las reglas.
:::

**Partes par e impar.** Una función compleja se llama __par__ si $x(t)=x^*(-t)$, e __impar__ si $x(t)=-x^*(-t)$. (Para funciones reales, es la simetría habitual respecto al eje o respecto al origen, respectivamente.) Toda señal se descompone de forma única en ambas partes:

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz Teorema 5.1 (Simetrías)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

Para señales **reales**, $S(-f)=S^*(f)$: la parte real y el módulo $|S|$ son pares en $f$; la parte imaginaria y la fase, impares. Una señal real y par tiene un espectro real y par. Una señal real e impar tiene un espectro imaginario puro e impar.
:::

:::herleitung Simetrías
Primero: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$. Con $\tau=-t$, esto es $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$. Por tanto

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

Para $s$ real, $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$. En general, $\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$. Así pues, $S(f)=S^*(-f)$.
:::

⁠**En resumen:** en una señal real, la mitad negativa del espectro es la imagen especular conjugada de la positiva. No contiene información nueva.

**Ejemplo.** El pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$ (real) tiene la parte par $\frac12\mathrm{e}^{-|t|}$ y la impar $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Su espectro $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ tiene la parte real par $\frac{1}{1+(2\pi f)^2}$, la transformada de $\frac12\mathrm{e}^{-|t|}$, y la parte imaginaria impar $\frac{-2\pi f}{1+(2\pi f)^2}$ (fig. [5](#abb-5)).

:::abbildung et3/k3gerade
El pulso exponencial ($RC=1$ s), descompuesto en una parte par (azul) y una impar (roja). A la derecha, el espectro: la parte par da la parte real (par en $f$); la impar, la parte imaginaria (impar en $f$).
:::

:::aufgabe Ejercicio 5 ★ Leer la simetría
<span class="anker" id="aufg-5"></span>

¿Qué se puede decir del espectro sin hacer cálculos? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) una señal real con $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: ¿cuánto vale $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Real y par: espectro real y par ($\operatorname{si}(\pi f)$). (b) Real e impar: espectro imaginario puro e impar. (c) Compleja, pero $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: en el sentido de la definición, la señal es par; por tanto, su espectro es real. Según la regla de modulación, es $\operatorname{si}(\pi(f-1))$: real, pero no simétrico respecto a $f=0$, porque la señal no es real. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::

## Etapa 6: Las reglas de cálculo (teoremas)

<span class="anker" id="stufe-6"></span>

:::zweck
En lugar de calcular cada integral de nuevo, se usan reglas: ¿qué le ocurre al espectro si se desplaza, se comprime, se deriva o se modula la señal? Cada regla se deduce de lo que la operación hace con una única oscilación.
:::

:::satz Teorema 6.1 (Teoremas de la transformada de Fourier)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{Superposición:} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{Conjugación:} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{Escalado (semejanza):} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{Desplazamiento:} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{Derivación:} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{Simetría (dualidad):} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{Modulación:} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{Derivación en frecuencia:} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{Convolución, multiplicación:} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{Áreas:} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{Parseval:} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**Cómo leer los más importantes:**

<ul>

<li>

⁠**Escalado (semejanza):** una señal comprimida en el tiempo ($|b|>1$) tiene un espectro más ancho. Las señales cortas necesitan muchas frecuencias. La duración y el ancho de banda varían en sentido inverso.

</li>

<li>

⁠**Desplazamiento:** un retardo no cambia el módulo, solo la fase, y lo hace de forma lineal en $f$: cada oscilación se desplaza el mismo tiempo, lo que a mayor frecuencia supone un ángulo mayor.

</li>

<li>

⁠**Derivación:** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Derivar amplifica las frecuencias altas.

</li>

<li>

⁠**Simetría:** la transformada directa y la inversa solo se diferencian en el signo del exponente. Por eso cada par de transformadas da un segundo par con los papeles intercambiados.

</li>

<li>

⁠**Modulación:** multiplicar por $\mathrm{e}^{\mathrm{j}2\pi Ft}$ desplaza todo el espectro en $F$. Así funciona toda emisora de radio.

</li>

<li>

⁠**Multiplicación:** el producto de dos señales tiene como espectro la convolución de los espectros; es la contrapartida del teorema de convolución.

</li>

<li>

⁠**Parseval:** la energía es la misma en ambos dominios. $|S(f)|^2$ es la __densidad de energía__ en función de la frecuencia.

</li>

</ul>

:::herleitung Escalado, desplazamiento, derivación, simetría, modulación, multiplicación, Parseval
⁠**Escalado** ($b>0$, $\tau=bt$): $\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$. Para $b<0$ se invierten los límites; de ahí $1/|b|$.

⁠**Desplazamiento** ($\tau=t-t_0$): $\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$. Con $s=\delta$ se obtiene el par para $\delta(t-t_0)$.

⁠**Derivación:** derivar la transformada inversa respecto a $t$, $\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$.

⁠**Simetría:** en la transformada inversa, sustituir $t$ por $-t$: $s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$. Ahora intercambiar los nombres de las variables $t$ y $f$: $s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, que es la transformada directa de $S(t)$.

⁠**Modulación:** $\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$. La derivación en el dominio de la frecuencia se obtiene igualmente derivando la transformada directa respecto a $f$.

⁠**Multiplicación:** teorema de convolución para las señales $s_1(t)$ y $s_2(t)$, es decir, $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$; después, aplicar la simetría a este par: $S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$. Renombrando se obtiene [(6.9)](#gl-6-9).

⁠**Áreas:** sustituir $f=0$ en la transformada directa y $t=0$ en la inversa.

⁠**Parseval:** $\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ es el producto $s(t)s^*(t)$ integrado; por tanto, según la multiplicación, la conjugación y el teorema del área, $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$.
:::

:::frage ¿Por qué un retardo no cambia el módulo del espectro?
Porque un retardo no atenúa ni amplifica ninguna oscilación; solo desplaza cada una. Cada oscilación se desplaza el mismo tiempo $t_0$, lo que a la frecuencia $f$ corresponde al ángulo $2\pi ft_0$. Por eso la fase es una recta en $f$ con pendiente $-2\pi t_0$. Un sistema con $|H|=1$ y fase lineal retrasa una señal sin cambiar su forma.
:::

:::aufgabe Ejercicio 6 ★★ Aplicar los teoremas
<span class="anker" id="aufg-6"></span>

Usa $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$ (etapa [7](#stufe-7)) y los teoremas.

<ol class="al">

<li>

Determina el espectro de un pulso rectangular de altura 1 desde $t=0$ hasta $t=2$ s. ¿Cuánto vale su módulo en $f=0$ y dónde está el primer cero?

</li>

<li>

Determina el espectro de $\cos(2\pi F_0t)\operatorname{rect}(t)$ con $F_0=5$ Hz y esbózalo.

</li>

</ol>

:::loesung
(a) El pulso es $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$. Escalado ($T=2$) y desplazamiento ($t_0=1$ s): $2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$. Módulo en $f=0$: 2 (el área). Primer cero en $f=0{,}5$ Hz. El desplazamiento solo cambia la fase.

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$; modulación: $\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$. Dos lóbulos principales si de altura $\frac12$ en $\pm5$ Hz, con los primeros ceros a 1 Hz a cada lado.
:::
:::

:::aufgabe Ejercicio 7 ★★ La simetría como herramienta
<span class="anker" id="aufg-7"></span>

Por el ejercicio [4](#aufg-4) sabes que $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$. Con ello, determina sin integrales el espectro de $\frac{1}{1+t^2}$.

:::loesung
Aplicar la simetría al par: $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$. Ahora dilatar el tiempo. Con $x(t)=\frac{2}{1+(2\pi t)^2}$ se tiene $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$; por el teorema de escalado (semejanza) con $b=\frac1{2\pi}$, esto da $\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$. Dividir entre dos:

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

Comprobación con el teorema del área: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
:::
:::

## Etapa 7: Rectángulo, función si y triángulo

<span class="anker" id="stufe-7"></span>

:::zweck
Tres pares de transformadas aparecen constantemente. Con los teoremas se obtienen de un único cálculo.
:::

**Rectángulo.** Con $\operatorname{si}(x)=\sin(x)/x$:

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz Teorema 7.1 (Rectángulo, si y triángulo)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**Cómo leerlo:** un rectángulo de duración $T$ tiene un espectro de altura $T$ (su área) con ceros en todos los múltiplos no nulos de $1/T$. El doble de largo significa la mitad de ancho en el espectro (fig. [6](#abb-6)). [(7.2)](#gl-7-2) se deduce de la simetría; [(7.3)](#gl-7-3), del teorema de convolución; y [(7.4)](#gl-7-4) se cumple porque en el dominio de la frecuencia $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$: un paso bajo ideal no altera una señal que ya está limitada a su banda.

:::abbildung et3/k3rectsi
$\operatorname{rect}(t/T)$ y su espectro $|T|\operatorname{si}(\pi Tf)$ para $T=1$ s y $T=2$ s. Duración doble: altura doble ($=$ área), anchura mitad, primer cero en $1/T$.
:::

:::ltspice Espectro de un pulso rectangular
⁠**Esquema:** solo una fuente `voltage` con `PULSE(0 1 0 1u 1u {T0} 16)`: un rectángulo de duración $T_0$, repetido cada 16 s.

⁠**Directivas:** `.param T0=1`, `.step param T0 list 1 2`, `.tran 0 16 0 1m`, `.options plotwinsize=0`, `.four 0.0625 40 V(in)`.

⁠**Lo que ves:** la repetición cada 16 s convierte el espectro en líneas separadas $1/16$ Hz (etapa [4](#stufe-4)). `.four` da sus amplitudes $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$, es decir, muestras de la envolvente si. Con $T_0=1$ s son nulas las líneas en 1 Hz y 2 Hz; con $T_0=2$ s, ya las de 0,5 Hz, 1 Hz, 1,5 Hz y 2 Hz. La componente continua se duplica de 0,0625 a 0,125. Así pues, duración doble significa anchura mitad y altura doble, como en la fig. [6](#abb-6). En la vista FFT ves directamente la envolvente con sus ceros.
:::

:::aufgabe Ejercicio 8 ★ Áreas y energía de la función si
<span class="anker" id="aufg-8"></span>

Calcula sin integrar $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ y $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$. Usa el teorema del área y Parseval.

:::loesung
Teorema del área: $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$. Parseval: $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
:::
:::

:::aufgabe Ejercicio 9 ★★ Triángulo y convolución múltiple
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Determina el espectro de $\Lambda(t/2)$ (triángulo de semianchura 2 s). ¿Dónde están los ceros?

</li>

<li>

¿Qué espectro tiene $\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$? ¿Por qué los lóbulos secundarios decrecen tanto más rápido cuantas más veces se convoluciona?

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$ y escalado con $T=2$: $\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$. Ceros en $f=k/2$, $k\neq0$.

(b) $\operatorname{si}^3(\pi f)$. Cada convolución adicional multiplica el espectro por $\operatorname{si}(\pi f)$, que en los lóbulos secundarios decrece como $1/(\pi f)$. Con $M$ rectángulos convolucionados, los lóbulos secundarios decrecen como $1/f^M$. En el dominio del tiempo: el rectángulo tiene saltos (decrecimiento $1/f$), el triángulo tiene puntos angulosos ($1/f^2$) y la convolución triple tiene derivada continua ($1/f^3$). Cuanto más suave es una señal, más rápido decrece su espectro.
:::
:::

## Etapa 8: Señales singulares y espectros de líneas

<span class="anker" id="stufe-8"></span>

:::zweck
Las constantes, las oscilaciones, el escalón y las señales periódicas no son absolutamente integrables. Con impulsos de Dirac en el espectro pueden transformarse de todos modos. Así, la serie de Fourier y la integral de Fourier se unifican.
:::

:::satz Teorema 8.1 (Pares singulares)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
<span class="anker" id="gl-8-6"></span>
<span class="anker" id="gl-8-7"></span>
$$\begin{aligned} \delta(t)&\;\circ\!\!-\!\!\bullet\;1, & c&\;\circ\!\!-\!\!\bullet\;c\,\delta(f),\\ \mathrm{e}^{\mathrm{j}2\pi Ft}&\;\circ\!\!-\!\!\bullet\;\delta(f-F), & \cos(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F),\\ & & \sin(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F),\\ \textstyle\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}&\;\circ\!\!-\!\!\bullet\;\textstyle\sum_kS_p(k)\,\delta(f-kF),\\ \textstyle\sum_n\delta(t-nT)&\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\textstyle\sum_k\delta\Bigl(f-\frac kT\Bigr),\\ \varepsilon(t)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}, & \operatorname{sgn}(t)&\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f},\\ \int_{-\infty}^ts(\tau)\mathrm{d}\tau&\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f). \end{aligned} \tag{8.1|8.2|8.3|8.4|8.5|8.6|8.7}$$
:::

⁠**Cómo leerlo:**

<ul>

<li>

Una constante es una oscilación de frecuencia 0; su espectro es una única línea en $f=0$. Una oscilación $\mathrm{e}^{\mathrm{j}2\pi Ft}$ es una línea en $F$. Un coseno real tiene dos medias líneas en $\pm F$.

</li>

<li>

Una señal periódica tiene un __espectro de líneas__: impulsos de Dirac en los armónicos, con los coeficientes de Fourier como pesos. La serie de Fourier es, por tanto, un caso particular de la integral de Fourier.

</li>

<li>

El __peine de Dirac__ (impulsos con separación $T$) tiene de nuevo un peine de Dirac como espectro, con separación $1/T$ y peso $1/|T|$ (fig. [7](#abb-7)). Este par será decisivo en el muestreo ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

</li>

<li>

El escalón tiene una componente continua $\frac12$ (línea $\frac12\delta(f)$) y una componente alterna $\frac12\operatorname{sgn}(t)$, cuyo espectro decrece como $1/f$.

</li>

</ul>

:::herleitung Pares singulares
⁠**Constante, oscilación:** aplicar la simetría a $\delta(t)\circ\!\!-\!\!\bullet\,1$: $1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$. La modulación desplaza la línea: $\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$. El coseno y el seno se obtienen con las fórmulas de Euler.

⁠**Espectro de líneas:** superposición sobre todos los armónicos.

⁠**Peine de Dirac:** es periódico con periodo $T$. Sus coeficientes de Fourier son $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$ para todo $k$. Con el espectro de líneas se obtiene [(8.5)](#gl-8-5).

⁠**Signo:** $\operatorname{sgn}(t)$ es el caso límite de $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ para $a\to0$:

$$\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}\;\xrightarrow{a\to0}\;\frac{1}{\mathrm{j}\pi f}.$$

⁠**Escalón:** $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$, por tanto $\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

⁠**Integración:** $\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$, teorema de convolución y propiedad de muestreo $S(f)\delta(f)=S(0)\delta(f)$.
:::

:::abbildung et3/k3kamm
Peine de Dirac con $T=0{,}5$ s y su espectro: de nuevo un peine, con separación $1/T=2$ Hz y peso $1/T=2$. Cuanto más juntos están los impulsos en el tiempo, más separadas están las líneas.
:::

:::frage Pero de $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ se sigue $\mathrm{j}2\pi f\,S(f)=1$, es decir, $S(f)=\frac{1}{\mathrm{j}2\pi f}$. ¿De dónde sale el $\frac12\delta(f)$?
La ecuación $\mathrm{j}2\pi f\,S(f)=1$ solo determina $S$ para $f\neq0$. En $f=0$ queda a la izquierda $0\cdot S(0)$, y un sumando $c\,\delta(f)$ desaparece porque $f\delta(f)=0$. Es la contrapartida de que derivar «olvida» una constante: $\varepsilon(t)$ y $\varepsilon(t)+b$ tienen la misma derivada. Qué constante es la correcta lo decide la parte par: $\varepsilon$ tiene valor medio $\frac12$, así que $c=\frac12$.
:::

**Ejemplo: el coseno encendido.** $\varepsilon(t)\cos(2\pi Ft)$. La multiplicación se convierte en convolución, y la convolución con un impulso de Dirac desplaza:

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

Además de las líneas reducidas a la mitad en $\pm F$, aparece un espectro ancho: el propio encendido contiene frecuencias próximas a $\pm F$.

:::aufgabe Ejercicio 10 ★ Espectros de líneas
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Indica el espectro de $s(t)=3+2\cos(2\pi\cdot50\,\mathrm{Hz}\cdot t)$ y esbózalo.

</li>

<li>

Indica el espectro de la onda cuadrada del modelo de referencia para $|f|\le0{,}5$ Hz.

</li>

</ol>

:::loesung
(a) $3\,\delta(f)+\delta(f-50\,\mathrm{Hz})+\delta(f+50\,\mathrm{Hz})$: una línea de peso 3 en cero y dos de peso 1 en $\pm50$ Hz.

(b) $F=0{,}159$ Hz. Hasta 0,5 Hz están $k=0,\pm1,\pm2,\pm3$, pero $k=\pm2$ falta:

$$0{,}5\,\delta(f)+0{,}318\bigl[\delta(f-0{,}159)+\delta(f+0{,}159)\bigr]-0{,}106\bigl[\delta(f-0{,}477)+\delta(f+0{,}477)\bigr].$$
:::
:::

:::aufgabe Ejercicio 11 ★★ Signo e integración
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Comprueba con [(5.2)](#gl-5-2) que el espectro de $\operatorname{sgn}(t)$ debe ser imaginario puro e impar.

</li>

<li>

Calcula con [(8.7)](#gl-8-7) el espectro de $\int_{-\infty}^t\operatorname{rect}(\tau)\mathrm{d}\tau$. ¿De qué señal se trata?

</li>

</ol>

:::loesung
(a) $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$: imaginario puro, y $-\frac{\mathrm{j}}{\pi(-f)}=+\frac{\mathrm{j}}{\pi f}$, es decir, impar. Encaja con una señal real e impar.

(b) $\frac{\operatorname{si}(\pi f)}{\mathrm{j}2\pi f}+\frac12\delta(f)$. La señal es la integral acumulada del rectángulo: 0 para $t\le-\frac12$, luego una rampa hasta 1 en $t=\frac12$ y después constante igual a 1. El valor medio sobre todo el tiempo es $\frac12$; de ahí $\frac12\delta(f)$.
:::
:::

## Etapa 9: Transformada de Hilbert y señal analítica

<span class="anker" id="stufe-9"></span>

:::zweck
En una señal causal, las partes real e imaginaria del espectro están relacionadas: una determina la otra. El mismo cálculo proporciona una señal que solo contiene frecuencias positivas.
:::

**Señales causales.** Si $s(t)=0$ para $t<0$, las partes par e impar son iguales para $t>0$ ($\frac12s$) y opuestas para $t<0$. Por tanto, $s_u(t)=s_g(t)\operatorname{sgn}(t)$ y $s_g(t)=s_u(t)\operatorname{sgn}(t)$. En el dominio de la frecuencia, la multiplicación por $\operatorname{sgn}$ se convierte en la convolución con $\frac{1}{\mathrm{j}\pi f}$:

:::satz Teorema 9.1 (Relación de Hilbert de las señales causales)
<span class="anker" id="satz-9-1"></span>

Para una señal causal se cumple

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**Cómo leerlo:** la convolución con $\frac{1}{\pi f}$ se llama __transformada de Hilbert__. En un sistema causal basta con conocer la parte real de la respuesta en frecuencia; la parte imaginaria se deduce de ella. La causalidad es, por tanto, una restricción fuerte sobre el espectro.

**Componente analítica.** Con el escalón en el *dominio de la frecuencia* se eliminan las frecuencias negativas: $S_+(f)=S(f)\,\varepsilon(f)$. De la simetría se sigue $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, por tanto

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ se llama __componente analítica__, y $\hat s$, transformada de Hilbert de $s$. Para señales reales, $S_-(f)=S_+^*(-f)$, es decir, $s_-=s_+^*$ y $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. Las partes real e imaginaria de $s_+$ son, a su vez, transformadas de Hilbert la una de la otra.

**El transformador de Hilbert.** El sistema LTI con $h(t)=\frac{1}{\pi t}$ tiene $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: módulo 1 en todas las frecuencias (un __paso todo__), fase $-90^\circ$ para $f>0$ y $+90^\circ$ para $f<0$. A partir de $\cos(2\pi Ft)$ produce

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**En resumen:** el transformador de Hilbert desfasa cada oscilación $90^\circ$ sin cambiar su amplitud.

:::aufgabe Ejercicio 12 ★★ Transformador de Hilbert
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

¿Qué hace el transformador de Hilbert con $\sin(2\pi Ft)$? ¿Qué da aplicarlo dos veces?

</li>

<li>

Determina la componente analítica $s_+(t)$ de $\cos(2\pi Ft)$ y comprueba que $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

¿Por qué el transformador de Hilbert no es causal? Fíjate en $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplicación por $-\mathrm{j}\operatorname{sgn}(f)$: en $-F$ por $+\mathrm{j}$, en $+F$ por $-\mathrm{j}$. Resultado: $-\frac12\delta(f+F)-\frac12\delta(f-F)$, es decir, $-\cos(2\pi Ft)$. Aplicado dos veces: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$; la señal se invierte.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, por tanto $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. Esto concuerda con $\frac12(s+\mathrm{j}\hat s)$ con $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ es distinta de cero también para $t<0$. Por tanto, la salida en el instante $t$ depende de valores futuros de la entrada. En la práctica, el transformador de Hilbert se aproxima con una respuesta al impulso truncada, a cambio de aceptar un retardo.
:::
:::

## Etapa 10: Transformada de Fourier de tiempo corto

<span class="anker" id="stufe-10"></span>

:::zweck
El espectro $S(f)$ describe una señal a lo largo de todos los tiempos. Pero el habla o la música cambian sus frecuencias continuamente. La transformada de Fourier de tiempo corto pregunta: ¿qué frecuencias contiene la señal *en torno al instante $t$*?
:::

**La idea.** Se recorta un fragmento en torno a $t$ y solo se transforma ese fragmento. Con una ventana rectangular de anchura $T_0$:

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

El espectro del fragmento es el espectro verdadero, difuminado por el espectro si de la ventana. Una ventana corta localiza bien en el tiempo, pero difumina mucho en frecuencia (teorema de escalado). Además, los bordes abruptos del rectángulo producen lóbulos secundarios que decrecen lentamente. Por eso son mejores las ventanas suaves, por ejemplo la __ventana de Hann__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz Teorema 10.1 (Transformada de Fourier de tiempo corto)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

Si las ventanas desplazadas en $T$ suman una constante, $\sum_nw(\tau-nT)=c$, entonces se cumple

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**Cómo leerlo:** $S_T(f,t)$ es un espectro que depende del tiempo. Si se representa $|S_T|$ en función de $t$ y $f$, se obtiene un __espectrograma__. Con la ventana de Hann y un desplazamiento $T=T_0/2$, $c=1$, porque $\cos^2x+\sin^2x=1$ (fig. [8](#abb-8)): los fragmentos se recomponen sin huecos en la señal completa, y la suma de sus espectros es el espectro completo.

:::abbildung et3/k3hann
Ventanas de Hann de anchura $T_0=2$ s, desplazadas sucesivamente $T=1$ s (azul). Su suma vale exactamente 1 en todas partes (rojo).
:::

:::aufgabe Ejercicio 13 ★ Ventana de Hann
<span class="anker" id="aufg-13"></span>

Demuestra que, para $T=T_0/2$, $\sum_nw(\tau-nT)=1$. Pista: en cada punto se solapan exactamente dos ventanas. Escribe la segunda con $\cos^2(x-\frac\pi2)$.

:::loesung
Para $\tau$ entre $nT$ y $(n+1)T$, con $T=T_0/2$, exactamente las ventanas $n$ y $n+1$ son distintas de cero. Con $x=\pi(\tau-nT)/T_0$:

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::

## Etapa 11: Fourier y Laplace, límites de la existencia

<span class="anker" id="stufe-11"></span>

:::zweck
¿Cuándo existe la integral de Fourier y cómo se relaciona con la transformada de Laplace?
:::

Una condición suficiente para la existencia es la integrabilidad absoluta, $\int|s(t)|\mathrm{d} t<\infty$. La transformada de Laplace amplía la clase ponderando antes con $\mathrm{e}^{-\sigma t}$ ([parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

Así, examina una señal en dos aspectos: sus componentes de frecuencia, como la transformada de Fourier, y su crecimiento o decrecimiento exponencial. Si $\sigma=0$ está en la región de convergencia, la transformada de Fourier es la transformada de Laplace en el eje imaginario. Sin embargo, con impulsos de Dirac (etapa [8](#stufe-8)), la transformada de Fourier abarca también señales que la transformada de Laplace no abarca: constantes y oscilaciones que se extienden a todo el eje temporal. En general, basta con que se cumpla $\int|s(t)|\mathrm{e}^{-c|t|}\mathrm{d} t<\infty$ para todo $c>0$. Entonces la señal puede crecer como una potencia $t^n$, pero no exponencialmente.

:::zusatz Por qué las convoluciones múltiples se vuelven gaussianas
Si se convolucionan entre sí $M$ rectángulos $\operatorname{rect}(t)$, el espectro es $\operatorname{si}^M(\pi f)$. Para valores pequeños de $f$, $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ y $\ln(1+w)\approx w$, por tanto

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

Para $M$ grande solo contribuye la zona de valores pequeños de $f$, y la aproximación es cada vez mejor. Para $M=4$, el valor exacto en $t=0$ es $0{,}667$; la curva de Gauss da $0{,}691$. Es un caso del __teorema central del límite__ (parte sobre estadística): la convolución de muchos pulsos positivos de área finita se aproxima a una curva de Gauss. Un ejemplo es la respuesta al impulso de una cadena de muchos integradores cortos.
:::

:::aufgabe Ejercicio 14 ★★★ (Para profundizar) Comprobar la aproximación gaussiana
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Compara, para $M=2$, el valor exacto $\Lambda(0)=1$ con la aproximación gaussiana.

</li>

<li>

Demuestra que la curva de Gauss $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ tiene área 1. ¿Por qué tiene que ser así?

</li>

</ol>

:::loesung
(a) $M=2$: $\sqrt{6/(2\pi)}=0{,}977$ en lugar de $\Lambda(0)=1$, es decir, un 2,3 % menos. Para $M=4$: 0,691 en lugar de 0,667, es decir, un 3,6 % más. Así pues, ya tras pocas convoluciones la curva de Gauss está cerca del resultado exacto. La aproximación solo se vuelve arbitrariamente buena para $M$ grande, porque solo entonces contribuyen al espectro únicamente los valores pequeños de $f$.

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$; multiplicado por $\sqrt{6/(\pi M)}$ da 1. Tiene que ser así: el área de una convolución es el producto de las áreas, aquí $1^M=1$. En el espectro, es el valor en $f=0$, $\operatorname{si}^M(0)=1$, y la aproximación $\mathrm{e}^{-M(\pi f)^2/6}$ también vale 1 ahí.
:::
:::

:::kern Lo esencial
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$; $H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.

</li>

<li>

Serie: $s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$, $S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$; real: $S_p(-k)=S_p^*(k)$.

</li>

<li>

Parseval: $\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$; Gibbs: sobreoscilación de aproximadamente el 9 % en los saltos; LTI: $G_p(k)=S_p(k)H(kF)$.

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, $s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$; $s*h\leftrightarrow SH$, $s_1s_2\leftrightarrow S_1*S_2$.

</li>

<li>

Real: $S(-f)=S^*(f)$; par $\leftrightarrow\operatorname{Re} S$, impar $\leftrightarrow\mathrm{j}\operatorname{Im} S$.

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$; $s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$; $\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$; $\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$; $S(t)\leftrightarrow s(-f)$.

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$; $\Lambda\leftrightarrow\operatorname{si}^2$; $\delta\leftrightarrow1$; $1\leftrightarrow\delta(f)$; $\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$.

</li>

<li>

Peine $\leftrightarrow$ peine: $\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$; $\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

</li>

<li>

Hilbert: $h=\frac{1}{\pi t}$, $H=-\mathrm{j}\operatorname{sgn}(f)$; $s_+=\frac12(s+\mathrm{j}\hat s)$, $s=2\operatorname{Re} s_+$.

</li>

</ul>
:::
