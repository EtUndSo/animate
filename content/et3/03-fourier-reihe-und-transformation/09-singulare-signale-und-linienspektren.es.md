---
title: Etapa 8: Señales singulares y espectros de líneas
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3230900
summary: Las constantes, las oscilaciones, el escalón y las señales periódicas no son absolutamente integrables.
tags: espectro de líneas, peine de Dirac
lang: es
---

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

El __peine de Dirac__ (impulsos con separación $T$) tiene de nuevo un peine de Dirac como espectro, con separación $1/T$ y peso $1/|T|$ (fig. [7](#abb-7)).

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

:::abbildung et3/k3kamm 7
Peine de Dirac con $T=0{,}5$ s y su espectro: de nuevo un peine, con separación $1/T=2$ Hz y peso $1/T=2$. Cuanto más juntos están los impulsos en el tiempo, más separadas están las líneas.
:::

:::frage Pero de $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ se sigue $\mathrm{j}2\pi f\,S(f)=1$, es decir, $S(f)=\frac{1}{\mathrm{j}2\pi f}$. ¿De dónde sale el $\frac12\delta(f)$?
La ecuación $\mathrm{j}2\pi f\,S(f)=1$ solo determina $S$ para $f\neq0$. En $f=0$ queda a la izquierda $0\cdot S(0)$, y un sumando $c\,\delta(f)$ desaparece porque $f\delta(f)=0$. Es la contrapartida de que derivar «olvida» una constante: $\varepsilon(t)$ y $\varepsilon(t)+b$ tienen la misma derivada. Qué constante es la correcta lo decide la parte par: $\varepsilon$ tiene valor medio $\frac12$, así que $c=\frac12$.
:::

::::beispiel el coseno encendido
$\varepsilon(t)\cos(2\pi Ft)$. La multiplicación se convierte en convolución, y la convolución con un impulso de Dirac desplaza:

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

Además de las líneas reducidas a la mitad en $\pm F$, aparece un espectro ancho: el propio encendido contiene frecuencias próximas a $\pm F$.
::::

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

Comprueba con [(5.2)](symmetrien-im-signal-und-im-spektrum.html#gl-5-2) que el espectro de $\operatorname{sgn}(t)$ debe ser imaginario puro e impar.

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
