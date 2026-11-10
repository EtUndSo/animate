---
title: Etapa 3: Potencia, convergencia y sistemas LTI
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3230400
summary: ¿Cuánto aporta cada armónico a la señal, con qué precisión aproxima una serie truncada la señal y qué hace un sistema LTI con una entrada periódica?
tags: potencia, suma parcial, fenómeno de Gibbs
lang: es
---

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
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Al promediar sobre un periodo, según [(2.4)](periodische-signale-die-fourier-reihe.html#gl-2-4) solo queda $k=l$: $\sum_k|S_p(k)|^2$.
:::

**Serie truncada y fenómeno de Gibbs.** Si se toman solo los armónicos hasta $|k|\le N$, la __suma parcial__ es $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. La potencia del error $s_p-s_{p,N}$ es la suma de los $|S_p(k)|^2$ omitidos y tiende a cero para $N\to\infty$ si la señal tiene potencia finita. Sin embargo, en un salto queda una sobreoscilación (fig. [2](#abb-2)): se estrecha al crecer $N$, pero su altura tiende a aproximadamente el 9 % de la altura del salto (10,0 % con $N=3$, 9,1 % con $N=9$, 9,0 % con $N=27$, valor límite 8,95 %). Este es el __fenómeno de Gibbs__. No contradice la convergencia: el área bajo la sobreoscilación, y con ella la potencia del error, tiende igualmente a cero.

:::abbildung et3/k3gibbs 2
Sumas parciales de la onda cuadrada ($T=2\pi$ s) con los armónicos hasta $|k|\le N$. En los flancos queda una sobreoscilación de aproximadamente el 9 % de la altura del salto, que al crecer $N$ solo se vuelve más estrecha.
:::

**Entrada periódica en un sistema LTI.** Cada armónico es una función propia y se multiplica por $H(kF)$. Por eso la salida tiene el mismo periodo, y sus coeficientes son

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

En el modelo de referencia, $H(kF)=1/(1+\mathrm{j} k)$. La componente fundamental se transmite con $|H|=0{,}707$ y $-45^\circ$; el tercer armónico, con $0{,}316$ y $-71{,}6^\circ$; el quinto, con $0{,}196$ y $-78{,}7^\circ$. A la salida, el tercer armónico ya solo es el 15 % del primero, frente al 33 % a la entrada. El circuito RC redondea los flancos (fig. [3](#abb-3)). La salida oscila entre 0,041 y 0,959.

:::abbildung et3/k3rc 3
Onda cuadrada a través del paso bajo RC con $RC=1$ s, calculada como suma de armónicos con $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. La salida se carga y se descarga exponencialmente entre 0,041 y 0,959.
:::

:::frage ¿No es un cálculo con infinitos armónicos mucho más engorroso que la ecuación diferencial?
Para una única onda cuadrada a través de un circuito RC, sí: las curvas de carga y descarga pueden escribirse directamente. A cambio, la serie muestra *por qué* la salida tiene ese aspecto. Los flancos están formados por los armónicos altos, y son precisamente esos los que atenúa el circuito RC. Además, [(3.2)](#gl-3-2) funciona para cualquier sistema LTI, también para aquellos cuya ecuación diferencial ni siquiera se conoce, sino solo su respuesta en frecuencia medida.
:::

:::ltspice Onda cuadrada a través del circuito RC
⁠**Esquema:** circuito RC (`res` con `1Meg`, `cap` con `1u`) con la fuente `PULSE(0 1 0 1u 1u {pi} {2*pi})`: periodo $2\pi$ s, ciclo de trabajo $\frac12$.

⁠**Directivas:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` y `.options plotwinsize=0`. La última desactiva la compresión de datos; sin ella, `.four` calcula con poca precisión. `.four` descompone el último periodo en armónicos y escribe el resultado en el SPICE Error Log.

⁠**Lo que ves:** en régimen permanente, `V(out)` oscila entre 0,041 y 0,959. Para $k\ge1$, `.four` da las amplitudes $2|S_p(k)|$ de las oscilaciones cosenoidales de [(2.2)](periodische-signale-die-fourier-reihe.html#gl-2-2). En la entrada son 0,637; 0; 0,212; 0; 0,127: faltan los armónicos pares. En la salida, el tercer armónico ya solo es el 15 % del primero, en lugar del 33 %. Las fases en la salida son $45^\circ$, $71{,}6^\circ$ y $78{,}7^\circ$ mayores que en la entrada, porque `.four` cuenta un retraso como positivo. Divide por dos las amplitudes de salida y compara con tu resultado del ejercicio [3](#aufg-3)(b). La vista FFT (clic derecho en el diagrama, View, FFT) muestra las mismas líneas en los múltiplos impares de 0,159 Hz.
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
