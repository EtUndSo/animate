---
title: Muestreo y sistemas en tiempo discreto
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3240100
summary: De la señal continua a la secuencia de números: teorema de muestreo, convolución discreta, DFT, FFT y transformada z
tags: muestras, analógica, en tiempo discreto, digital, muestreador ideal, réplicas espectrales, señal paso bajo, tasa de Nyquist
lang: es
---

## De qué trata

Un ordenador no puede almacenar una función $s(t)$, solo una secuencia de números. Por eso se mide la señal con un periodo de muestreo fijo $T$ y se trabaja con las __muestras__ $s(nT)$. Dos preguntas guían este artículo: *¿Se pierde información en el proceso?* Y: *¿cómo se calcula con secuencias de números del mismo modo en que las partes 1 a 3 calculaban con funciones?*

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Muestrear es multiplicar por un peine de Dirac. En el espectro resulta una convolución con un peine: el espectro se repite periódicamente con la frecuencia de muestreo.

</li>

<li>

Si las repeticiones no se superponen (frecuencia de muestreo mayor que el doble de la frecuencia más alta), la señal puede recuperarse exactamente con un paso bajo ideal. En caso contrario se produce aliasing (solapamiento espectral).

</li>

<li>

Para las secuencias de números valen las mismas herramientas que para las funciones: convolución como suma, transformada de Fourier con espectro periódico, DFT como muestras de esta y transformada z como equivalente de la transformada de Laplace.

</li>

</ol>
:::

**Un principio detrás de todos los resultados: discreto en un dominio significa periódico en el otro.**

| Resultado | De dónde viene |
|---|---|
| Espectro periódico tras el muestreo | tiempo discreto $\Rightarrow$ espectro periódico (etapa [2](#stufe-2)) |
| Teorema de muestreo, aliasing | si las copias periódicas se solapan o no (etapa [3](#stufe-3)) |
| Interpolación con funciones si | un paso bajo ideal extrae una copia (etapa [3](#stufe-3)) |
| Serie de Fourier | espectro discreto $\Rightarrow$ tiempo periódico (etapa [4](#stufe-4)) |
| Convolución discreta | integral de convolución sobre impulsos de Dirac ponderados con las muestras (etapa [5](#stufe-5)) |
| Transformada de Fourier de tiempo discreto | espectro de las muestras, periódico con periodo 1 (etapa [7](#stufe-7)) |
| DFT | ambos discretos $\Rightarrow$ ambos periódicos (etapa [8](#stufe-8)) |
| Diezmado, interpolación | muestrear una secuencia ya muestreada (etapa [10](#stufe-10)) |
| Transformada z | la idea de Laplace para secuencias: primero ponderar, después transformar (etapa [11](#stufe-11)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este artículo
<ul>

<li>

⁠**Frecuencia de muestreo** $f_\mathrm A=1/T=1$ kHz ($T=1$ ms). Señales de prueba: oscilaciones cosenoidales de 300 Hz y de 700 Hz.

</li>

<li>

En las secuencias, la frecuencia se normaliza a la frecuencia de muestreo: $f=1$ corresponde a $f_\mathrm A$. Con $f_\mathrm A=1$ kHz, $f=0{,}3$ significa, por tanto, 300 Hz.

</li>

<li>

⁠**Sistema recursivo** $g(n)=s(n)+0{,}6\,g(n-1)$.

</li>

<li>

⁠**Ejemplo de DFT** $s_d=(1,\,2,\,0,\,-1)$.

</li>

</ul>

El script `rechnung_kap4.py` recalcula los números y las curvas.
:::

## Etapa 1: Clases de señales y muestreo ideal

<span class="anker" id="stufe-1"></span>

:::zweck
¿Qué tipos de señales hay y cómo se describe matemáticamente el muestreo?
:::

**Cuatro clases.** El tiempo y la amplitud pueden ser, cada uno, continuos o discretos. Una señal __analógica__ es continua en ambos. Una señal __en tiempo discreto__ solo tiene valores en los instantes $nT$, pero estos con precisión arbitraria. Una señal __digital__ está además escalonada en amplitud (cuantizada), porque un ordenador solo puede representar una cantidad finita de números. Este artículo trata la discretización del tiempo. La cuantización de la amplitud es un tema aparte.

**Del muestreador real al ideal.** Un muestreador real cierra un interruptor en cada periodo de muestreo durante el breve tiempo $T_0$:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

Si $T_0$ se hace cada vez más corto, solo quedan los valores $s(nT)$. Matemáticamente, el rectángulo se sustituye por un impulso de Dirac. Este es el __muestreador ideal__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

La señal muestreada es un tren de impulsos de Dirac, cada uno con una muestra como peso. El segundo paso es la propiedad de muestreo (de criba) $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. De esta forma, las señales muestreadas pueden tratarse con todas las herramientas para señales continuas.

## Etapa 2: El espectro de la señal muestreada

<span class="anker" id="stufe-2"></span>

:::zweck
¿Qué le hace el muestreo al espectro? Esta etapa muestra que se repite periódicamente.
:::

**La idea.** Dos oscilaciones cuyas frecuencias difieren en un múltiplo de la frecuencia de muestreo $1/T$ tienen las mismas muestras:

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

Las muestras no pueden distinguirlas. Por eso, el espectro de las muestras tiene que ser igual en $f_0$ y en $f_0+k/T$. Es periódico.

:::satz Teorema 2.1 (Espectro de la señal muestreada idealmente)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**Cómo leerlo:** el espectro del original aparece con la forma intacta, pero con el factor $1/T$ y repetido en cada múltiplo de la frecuencia de muestreo. Las copias se llaman __réplicas espectrales__.

:::herleitung espectro de la señal muestreada
La multiplicación se convierte en convolución ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), y el espectro del peine de Dirac vuelve a ser un peine:

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

La convolución con un impulso de Dirac desplazado desplaza el espectro.
:::

:::abbildung et3/k4spektrum
Un espectro hasta $f_\mathrm g=300$ Hz (azul, triangular para mayor claridad), muestreado. Arriba, con 1 kHz: las copias en los múltiplos de 1 kHz están separadas. Abajo, con 500 Hz: las copias, separadas 500 Hz, se solapan, y la suma (rojo) ya no es el original. Se ha omitido el factor $1/T$.
:::

:::frage ¿Cómo «sabe» el espectro que se ha muestreado? La señal entre los instantes de muestreo simplemente ha desaparecido.
Precisamente por eso. Entre los instantes de muestreo, la señal muestreada es nula, salvo en los impulsos. Toda oscilación que tome los mismos valores en todos los puntos $nT$ describe esta señal igual de bien. El espectro no puede decidirse entre ellas y las contiene todas: el original y sus copias en cada múltiplo de $1/T$.
:::

## Etapa 3: Teorema de muestreo y reconstrucción

<span class="anker" id="stufe-3"></span>

:::zweck
¿Cuándo puede recuperarse exactamente el original a partir de las muestras, y cómo?
:::

:::satz Teorema 3.1 (Teorema de muestreo)
<span class="anker" id="satz-3-1"></span>

Una señal cuyo espectro se anula por encima de $f_\mathrm g$ (__señal paso bajo__ o señal de banda limitada) queda determinada unívocamente por sus muestras $s(nT)$ si

<span class="anker" id="gl-3-1"></span>
$$T\le\frac{1}{2f_\mathrm g}\qquad\text{es decir}\qquad f_\mathrm A=\frac1T\ge2f_\mathrm g. \tag{3.1}$$

Con el paso bajo ideal $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$ se cumple

<span class="anker" id="gl-3-2"></span>
$$s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr], \tag{3.2}$$

y para $T=1/(2f_\mathrm g)$:

<span class="anker" id="gl-3-3"></span>
$$s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr). \tag{3.3}$$
:::

⁠**Cómo leerlo:** con $f_\mathrm A\ge2f_\mathrm g$, las copias de la fig. [1](#abb-1) están separadas. Un paso bajo extrae la copia en $f=0$, que tiene exactamente la forma del original. En el dominio del tiempo, esto significa: cada muestra se sustituye por una función si que vale 1 en su propio instante de muestreo y 0 en todos los demás (fig. [2](#abb-2)). Su suma pasa por todas las muestras y rellena los huecos de modo que no aparece ninguna frecuencia por encima de $f_\mathrm g$. La frecuencia de muestreo mínima $2f_\mathrm g$ se llama __tasa de Nyquist__.

:::herleitung reconstrucción
Para $|f|\le f_\mathrm g$ solo está la copia $k=0$, es decir, $S_\mathrm a(f)=\frac1TS(f)$. Con $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$ se tiene $S_\mathrm a\cdot H_\mathrm{TP}=S$. En el dominio del tiempo: $T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$ ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), rectángulo y si). Con [(1.2)](#gl-1-2) y $2f_\mathrm g=1/T$ resulta $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$.
:::

:::abbildung et3/k4siinterp
Interpolación con funciones si: muestras $0;\ 1;\ 0{,}6;\ -0{,}4;\ 0{,}8;\ 0$ (rojo), las funciones si ponderadas (gris) y su suma (azul). Cada función si es nula en los demás instantes de muestreo; por eso la suma pasa exactamente por todos los valores.
:::

**Aliasing.** Si se muestrea demasiado despacio, las copias se solapan. Una frecuencia por encima de $f_\mathrm A/2$ aparece tras la reconstrucción como una frecuencia falsa, más baja: su __alias__. En el modelo de referencia, con $f_\mathrm A=1$ kHz, un coseno de 700 Hz y uno de 300 Hz tienen exactamente las mismas muestras, porque $\cos(2\pi\cdot0{,}7n)=\cos(2\pi n-2\pi\cdot0{,}3n)=\cos(2\pi\cdot0{,}3n)$ (fig. [3](#abb-3)). A posteriori ya no se pueden separar. Por eso, delante de todo muestreador se filtra con un paso bajo (__filtro antialiasing__).

:::abbildung et3/k4alias
Con $f_\mathrm A=1$ kHz, las muestras (negro) de 700 Hz y de 300 Hz coinciden. Los 700 Hz están por encima de $f_\mathrm A/2=500$ Hz y aparecen como alias en 300 Hz.
:::

:::frage ¿No basta con exactamente $f_\mathrm A=2f_\mathrm g$? Con un seno de frecuencia exactamente $f_\mathrm g$, eso sale mal.
Efectivamente, justo en el límite sale mal: con una fase desfavorable, un seno de $f_\mathrm g=f_\mathrm A/2$ puede muestrearse siempre en sus pasos por cero, y todas las muestras son nulas. Por eso, en sentido estricto, el teorema exige que el espectro no tenga ninguna línea *en* $f_\mathrm g$, o bien que $f_\mathrm A>2f_\mathrm g$. En la práctica se muestrea de todos modos más deprisa, porque los paso bajo reales no caen verticalmente y necesitan espacio para su banda de transición.
:::

:::ltspice Muestreo y retención: ver el aliasing
⁠**Esquema:** fuente `voltage` en el nodo `in` con `SINE(0 1 700 0 0 90)`, un coseno de 700 Hz. Un interruptor `sw` (valor `SW1`) de `in` a `sh`, y ahí `cap` con `100n` a masa. La entrada de control del interruptor la excita una segunda fuente con `PULSE(0 1 0 10n 10n 1u 1m)`: el interruptor se cierra cada milisegundo durante 1 µ s ($f_\mathrm A=1$ kHz), y entre medias el condensador retiene la muestra. Detrás de `sh` sigue, como paso bajo de reconstrucción, una fuente `e` con la salida `out`. Es un paso bajo de Butterworth de orden 4 (banda de paso lo más plana posible) con la frecuencia de corte 400 Hz y tiene el valor

`Laplace=1/(((s/wg)**2+0.7654*s/wg+1)*((s/wg)**2+1.8478*s/wg+1))`

⁠**Directivas:** `.model SW1 SW(Ron=1 Roff=1G Vt=0.5)`, `.param wg=2*pi*400`, `.tran 0 40m 0 1u`, `.options plotwinsize=0`, `.four 100 15 V(sh) V(out)`.

⁠**Lo que ves:** la escalera en `sh` sigue una oscilación de 300 Hz, y en `out` aparece un coseno de 300 Hz en lugar de 700 Hz. En `.four`, la línea de 300 Hz es la más intensa. Con `SINE(0 1 300 0 0 90)` se obtiene la misma escalera. Pon 1,2 kHz y compara con tu resultado del ejercicio [1](#aufg-1)(a).

⁠**Antialiasing:** coloca una segunda fuente `e` igual delante del interruptor. Con 700 Hz, la línea de 300 Hz en `out` baja a aproximadamente una décima parte, mientras que una entrada de 300 Hz pasa casi sin atenuar. Así pues, el alias debe evitarse antes de muestrear: después ya no se distingue de una señal real de 300 Hz.
:::

:::aufgabe Ejercicio 1 ★ Frecuencias alias
<span class="anker" id="aufg-1"></span>

$f_\mathrm A=1$ kHz.

<ol class="al">

<li>

¿Con qué frecuencia aparece un coseno de 1,2 kHz tras la reconstrucción?

</li>

<li>

¿Qué frecuencias dan las mismas muestras que un coseno de 50 Hz?

</li>

</ol>

:::loesung
(a) 1,2 kHz está por encima de $f_\mathrm A/2$. Tiene las mismas muestras que $1{,}2-1=0{,}2$ kHz y aparece como 200 Hz.

(b) Todas las $\pm50\,\mathrm{Hz}+k\cdot1\,\mathrm{kHz}$: 950 Hz, 1050 Hz, 1950 Hz, 2050 Hz, y así sucesivamente. En el coseno, la frecuencia negativa y la positiva cuentan igual; por eso también se incluye $1000-50$.
:::
:::

:::aufgabe Ejercicio 2 ★★ Frecuencias de muestreo en la práctica
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

La voz telefónica se limita a 3,4 kHz y se muestrea a 8 kHz. ¿Cuál es la tasa de Nyquist y para qué sirve el margen?

</li>

<li>

Un CD de audio muestrea a 44,1 kHz. ¿Hasta qué frecuencia puede almacenar sonidos y qué anchura tiene la banda de transición del filtro antialiasing, si la banda audible llega hasta 20 kHz?

</li>

</ol>

:::loesung
(a) Tasa de Nyquist $2\cdot3{,}4=6{,}8$ kHz. Con 8 kHz, $f_\mathrm A/2$ está en 4 kHz. Entre 3,4 y 4 kHz, el filtro antialiasing tiene espacio para pasar de la banda de paso a la banda eliminada.

(b) Hasta $f_\mathrm A/2=22{,}05$ kHz. La banda de transición, de 20 a 22,05 kHz, solo tiene 2,05 kHz de anchura. Por eso se necesitan filtros abruptos o sobremuestreo.
:::
:::

:::aufgabe Ejercicio 3 ★★ Interpolación con funciones si a mano
<span class="anker" id="aufg-3"></span>

Calcula con [(3.3)](#gl-3-3) el valor de la señal de la fig. [2](#abb-2) en $t=2{,}5T$. Pista: $\operatorname{si}(\pi\cdot0{,}5)=2/\pi$ y $\operatorname{si}(\pi\cdot1{,}5)=-2/(3\pi)$. ¿Qué muestras no contribuyen?

:::loesung
En $t=2{,}5T$, $\operatorname{si}(\pi(2{,}5-k))$ vale $\frac2\pi$ para $k\in\{2,3\}$ y $-\frac{2}{3\pi}$ para $k\in\{1,4\}$. Los valores en $k=0$ y $k=5$ son nulos y no contribuyen:

$$s(2{,}5T)=\frac2\pi\Bigl[-\tfrac13\cdot1+0{,}6-0{,}4-\tfrac13\cdot0{,}8\Bigr]=\frac2\pi\cdot(-0{,}4)=-0{,}255.$$
:::
:::

## Etapa 4: Muestreo en el dominio de la frecuencia

<span class="anker" id="stufe-4"></span>

:::zweck
El mismo principio vale con los papeles intercambiados: si se muestrea el espectro, la señal se vuelve periódica.
:::

Un espectro que solo se conoce en las frecuencias $kF$ es un peine de impulsos de Dirac ponderados. Con el factor $F$, los pesos son exactamente los coeficientes de Fourier de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

La señal correspondiente es el original repetido periódicamente con periodo $1/F$. Si la señal es más corta que $1/F$, las repeticiones no se solapan. Entonces se recupera con una ventana temporal, y el espectro, con funciones si:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**En resumen:** discreto en el tiempo significa periódico en el espectro; discreto en el espectro significa periódico en el tiempo. Lo segundo es la serie de Fourier de la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): sus coeficientes son muestras del espectro de un pulso aislado, $S_p(k)=F\cdot S(kF)$.

## Etapa 5: Señales en tiempo discreto y convolución discreta

<span class="anker" id="stufe-5"></span>

:::zweck
A partir de ahora solo se calcula con las secuencias de números $s(n)$. Esta etapa traslada a las secuencias la convolución, las señales elementales y los sistemas LTI.
:::

**Convolución de las muestras.** Si la entrada $s$ y la respuesta al impulso $h$ de un sistema son señales paso bajo y se muestrea a la tasa de Nyquist, cada una puede escribirse como serie de funciones si [(3.3)](#gl-3-3). Como $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), las muestras de la salida se obtienen solo a partir de las muestras:

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

Normalizada a $T=1$, es la __convolución discreta__:

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**Secuencias elementales.**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

El __impulso unitario__ $\delta(n)$ es una secuencia ordinaria, no una distribución: en $n=0$ vale 1. Es el elemento neutro de la convolución discreta, $s(n)*\delta(n)=s(n)$. Un rectángulo de $2M+1$ unos centrado en $n=0$ es $\varepsilon(n+M)-\varepsilon(n-M-1)$.

**Lineal e invariante al desplazamiento.** Un sistema en tiempo discreto se llama lineal si cumple el principio de superposición, e __invariante al desplazamiento__ si $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ para todo entero $m$. Si cumple ambas cosas, se llama __sistema LSI__. Con la __respuesta al impulso__ $h(n)=\operatorname{Tr}\{\delta(n)\}$ se obtiene, como en la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html):

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

Aquí no hace falta ningún paso al límite: una secuencia *ya es* una suma de impulsos unitarios ponderados y desplazados.

**Diferencia y suma.** El equivalente de la derivada es la __diferencia__ $g(n)=s(n)-s(n-1)$, es decir, $h(n)=\delta(n)-\delta(n-1)$. El equivalente de la integral es la __acumulación__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. Una deshace a la otra: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$.

**Ecuaciones en diferencias, FIR e IIR.** En lugar de ecuaciones diferenciales, los sistemas en tiempo discreto se describen mediante ecuaciones en diferencias:

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{parte FIR}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{parte IIR}}. \tag{5.2}$$

La salida es una suma ponderada de valores pasados de la entrada y de la salida. Si solo depende de valores de la entrada ($b_p=0$), la respuesta al impulso termina al cabo de $Q+1$ valores: es un __filtro FIR__ (*finite impulse response*, respuesta al impulso finita). Con realimentación ($b_p\neq0$), la respuesta al impulso puede ser infinitamente larga: es un __filtro IIR__ (*infinite impulse response*, respuesta al impulso infinita). Ambos se construyen con elementos de retardo (memoria para un periodo de muestreo), multiplicadores y sumadores (fig. [4](#abb-4)).

:::abbildung et3/k4block
Sistema de primer orden $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. El bloque $T$ almacena un valor durante un periodo de muestreo. A la izquierda, la parte no recursiva; a la derecha, la realimentación de la salida.
:::

:::aufgabe Ejercicio 4 ★ Convolución discreta a mano
<span class="anker" id="aufg-4"></span>

Convoluciona $s=(1,1,1)$ con $h=(1,2)$, ambas empezando en $n=0$. ¿Qué longitud tiene el resultado y por qué?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Longitud $3+2-1=4$: el último valor no nulo aparece cuando el último valor de $h$ coincide con el último valor de $s$.
:::
:::

## Etapa 6: Un sistema recursivo

<span class="anker" id="stufe-6"></span>

:::zweck
En el sistema IIR más sencillo se ve cómo la realimentación genera una respuesta al impulso infinitamente larga y cuándo es estable el sistema.
:::

El sistema $g(n)=s(n)+b\,g(n-1)$ suma a la entrada la última salida ponderada con $b$. Para $s=\delta$ y reposo antes de $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

El impulso recorre una y otra vez el lazo de realimentación y en cada vuelta se multiplica por $b$. El sistema es __causal__ ($h(n)=0$ para $n<0$). Es __estable__ si $\sum_n|h(n)|<\infty$ (el equivalente discreto de la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), es decir, aquí exactamente para $|b|<1$, con $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Respuesta a una secuencia rectangular.** Entrada $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ unos). Con la suma de convolución y la fórmula de la suma geométrica $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

En el modelo de referencia ($b=0{,}6$, $M=4$): $g=1;\ 1{,}6;\ 1{,}96;\ 2{,}176$, luego $1{,}306;\ 0{,}783;\ 0{,}470;\dots$, cada valor 0,6 veces el anterior (fig. [5](#abb-5)). Es el equivalente discreto de la respuesta del circuito RC al pulso rectangular de la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek
El sistema recursivo con $b=0{,}6$. A la izquierda, la respuesta al impulso. A la derecha, la respuesta a cuatro unos: crece hasta 2,176 y después decae con el factor 0,6 por periodo de muestreo.
:::

:::aufgabe Ejercicio 5 ★★ Estudiar el sistema recursivo
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Comprueba directamente con la recursión los cinco primeros valores de $g(n)$ del modelo de referencia.

</li>

<li>

¿Hacia qué valor tiende la salida con una secuencia infinitamente larga de unos ($M\to\infty$)? Compáralo con $\sum_nh(n)$.

</li>

<li>

¿Cómo es $h(n)$ para $b=-0{,}6$ y para $b=1{,}1$? ¿Qué sistema es estable?

</li>

</ol>

:::loesung
(a) $g(0)=1$, $g(1)=1+0{,}6=1{,}6$, $g(2)=1+0{,}96=1{,}96$, $g(3)=1+1{,}176=2{,}176$, $g(4)=0+0{,}6\cdot2{,}176=1{,}306$.

(b) $\frac{1}{1-b}=2{,}5$. Es $\sum_nh(n)=\sum0{,}6^n=2{,}5$: con entrada constante 1, la convolución suma todos los valores de la respuesta al impulso. También $H_\mathrm a(0)=2{,}5$.

(c) $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\ -0{,}216;\dots$, signo alterno, decreciente, estable. $b=1{,}1$: $1;\ 1{,}1;\ 1{,}21;\dots$, creciente, inestable.
:::
:::

:::aufgabe Ejercicio 6 ★★ Sistema de primer orden
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0{,}5\,s(n-1)+0{,}6\,g(n-1)$ (fig. [4](#abb-4) con $a_0=1$, $a_1=0{,}5$, $b_1=0{,}6$).

<ol class="al">

<li>

Calcula de $h(0)$ a $h(3)$ con la recursión.

</li>

<li>

Demuestra que $h(n)=\frac{11}{6}\,0{,}6^n\varepsilon(n)-\frac56\delta(n)$.

</li>

</ol>

:::loesung
(a) $h(0)=1$, $h(1)=0{,}5+0{,}6\cdot1=1{,}1$, $h(2)=0{,}6\cdot1{,}1=0{,}66$, $h(3)=0{,}396$.

(b) La fórmula da $h(0)=\frac{11}{6}-\frac56=1$ y $h(1)=\frac{11}{6}\cdot0{,}6=1{,}1$. A partir de $n=2$ la entrada es nula, la recursión es $h(n)=0{,}6\,h(n-1)$, y la fórmula la cumple, porque $\frac{11}{6}0{,}6^n=0{,}6\cdot\frac{11}{6}0{,}6^{n-1}$. (Con la transformada z, la fórmula se obtiene de la descomposición $H(z)=-\frac56+\frac{11/6}{1-0{,}6z^{-1}}$.)
:::
:::

## Etapa 7: Transformada de Fourier de tiempo discreto

<span class="anker" id="stufe-7"></span>

:::zweck
¿Qué espectro tiene una secuencia de números? Es el espectro de la señal muestreada idealmente, calculado directamente a partir de las muestras.
:::

Si se introduce $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ en la integral de Fourier, con la propiedad de muestreo queda una suma. Normalizada a $T=1$:

:::satz Teorema 7.1 (Transformada de Fourier de tiempo discreto)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**Cómo leerlo:** el espectro $S_\mathrm a(f)$ es periódico con periodo 1, que es la frecuencia de muestreo. Un periodo, $|f|\le\frac12$, lo contiene todo. Por eso la transformada inversa solo integra sobre un intervalo de longitud 1. La suma es una serie de Fourier en $f$, con las muestras como coeficientes.

**Ejemplo.** Para $s(n)=\varepsilon(n)\,b^n$ con $|b|<1$ (serie geométrica):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

Es a la vez la respuesta en frecuencia $H_\mathrm a(f)$ del sistema recursivo de la etapa [6](#stufe-6). Para $b=0{,}6$: $|H_\mathrm a|=2{,}5$ en $f=0$, $1{,}60$ en $f=0{,}1$, $0{,}86$ en $f=0{,}25$ y $0{,}625$ en $f=0{,}5$ (fig. [6](#abb-6)). El sistema es un paso bajo, pero con respuesta en frecuencia periódica: en $f=1$ vuelve a amplificar tanto como en $f=0$.

:::abbildung et3/k4dtft
Módulo de la respuesta en frecuencia del sistema recursivo con $b=0{,}6$. Es periódico con la frecuencia de muestreo. Entre las líneas rojas está el único periodo que lo describe todo.
:::

**Convolución y multiplicación.** Como con las funciones, se cumple $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. El producto de dos secuencias da la __convolución periódica__ de los espectros sobre un periodo:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Ejercicio 7 ★ Media móvil
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ promedia tres valores consecutivos.

<ol class="al">

<li>

Demuestra que $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

¿En qué frecuencia es $H_\mathrm a=0$? ¿Qué oscilación elimina, por tanto, el filtro por completo, y por qué (pista: suma de tres valores de una oscilación de periodo 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, es decir, $f=\frac13$ (con $f_\mathrm A=1$ kHz: 333 Hz). Una oscilación con tres valores por periodo consta de tres fasores separados $120^\circ$. Su suma es nula: el filtro ve en cada ventana exactamente un periodo completo.
:::
:::

## Etapa 8: La transformada discreta de Fourier (DFT)

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ es una función continua, pero un ordenador necesita una cantidad finita de números. Para una secuencia de longitud finita basta con un número finito de muestras del espectro.
:::

**La idea.** Si $s(n)$ está limitada a $M$ valores, según la etapa [4](#stufe-4) bastan muestras del espectro con separación $F=1/M$. A ellas les corresponde la señal $s_d(n)$, repetida periódicamente con periodo $M$. Como el espectro también es periódico (tiempo discreto), bastan $M$ valores espectrales. Ahora ambos lados son discretos y periódicos.

:::satz Teorema 8.1 (Transformada discreta de Fourier)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**Cómo leerlo:** $S_d(k)$ es el valor del espectro $S_\mathrm a(f)$ en $f=k/M$. El índice $k$ numera las oscilaciones que caben exactamente $k$ veces en los $M$ valores. La transformada inversa es una serie de Fourier de $M$ términos. Los teoremas valen de forma análoga, por ejemplo el desplazamiento $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$ (circular: lo que sale por el final vuelve a entrar por el principio) y Parseval $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$.

**Ejemplo.** $s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Comprobación: $S_d(3)=S_d^*(1)$, porque la señal es real ($k=3$ corresponde a $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.

:::aufgabe Ejercicio 8 ★★ DFT a mano
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Comprueba $S_d(1)$ para $s_d=(1,2,0,-1)$.

</li>

<li>

Determina con el teorema de desplazamiento la DFT de la secuencia desplazada circularmente $(-1,1,2,0)$ y comprueba $S_d(1)$ directamente.

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$, porque $(-\mathrm{j})^3=\mathrm{j}$.

(b) Desplazamiento en $m=1$: $S_d(k)\,(-\mathrm{j})^k$, es decir, $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$. Directamente: $S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$.
:::
:::

## Etapa 9: FFT y convolución rápida

<span class="anker" id="stufe-9"></span>

:::zweck
La DFT necesita $M^2$ multiplicaciones. A la FFT le bastan aproximadamente $M\,\mathrm{lb}\,M$. Con ello, también la convolución a través del dominio de la frecuencia se vuelve rápida.
:::

**La idea de la FFT.** Con $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$ se tiene $S_d(k)=\sum_ns_d(n)W_M^{kn}$. Para $M$ par se separan los valores de índice par y los de índice impar:

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

porque $W_M^{2kn}=W_{M/2}^{kn}$. En lugar de una DFT de longitud $M$ se necesitan dos de longitud $M/2$ y $M$ multiplicaciones por $W_M^k$, es decir, $2(M/2)^2+M$ en lugar de $M^2$. Las dos DFT parciales son periódicas con periodo $M/2$; por eso dan también los valores para $k\ge M/2$. Si $M$ es una potencia de dos, la división se repite $\mathrm{lb}\,M$ veces. El coste baja a aproximadamente $M\,\mathrm{lb}\,M$. Para $M=1024$ son 10 240 multiplicaciones en lugar de 1 048 576, unas cien veces menos. Es la __transformada rápida de Fourier__ (FFT).

**Convolución circular.** Para secuencias periódicas de periodo $M$ vale la convolución __circular__ (periódica)

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

Es el resultado de la convolución ordinaria repetido periódicamente. Si $M$ es demasiado pequeño, las repeticiones se solapan. Para $s=(1,1,1)$ y $h=(1,2)$, la convolución ordinaria es $(1,3,3,2)$, con cuatro valores. Con $M=3$, el último valor cae sobre el primero: $(3,3,3)$. Con $M=4$ es correcto: $(1,3,3,2)$. En general debe cumplirse $M\ge M_1+M_2-1$ ($M_1$, $M_2$: longitudes de las dos secuencias); para ello se rellena con ceros.

**Convolución rápida.** En lugar de calcular directamente la suma de convolución, se transforman ambas secuencias con la FFT, se multiplican y se aplica la transformada inversa. Una señal de longitud arbitraria se divide en bloques, se convoluciona cada bloque por separado y se suman los resultados. Esto es lícito porque la convolución es distributiva:

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe Ejercicio 9 ★★ Circular o lineal
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Calcula a mano la convolución circular de $(1,1,1)$ y $(1,2,0)$ con $M=3$. ¿Qué valor de la convolución lineal se ha desplazado, y adónde?

</li>

<li>

Una señal de 1000 valores debe convolucionarse con un filtro de 25 valores mediante la DFT. ¿Qué longitud mínima debe tener la DFT?

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$, $g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$, $g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$. El cuarto valor de la convolución lineal (2 en $n=3$) se ha desplazado circularmente a $n=0$: $1+2=3$.

(b) Como mínimo $1000+25-1=1024$. Convenientemente, es una potencia de dos.
:::
:::

## Etapa 10: Remuestreo: diezmado e interpolación

<span class="anker" id="stufe-10"></span>

:::zweck
Una secuencia puede representarse a posteriori con una frecuencia de muestreo menor o mayor. Para el espectro valen las mismas reglas que en el primer muestreo.
:::

**Submuestreo por el factor $c$.** Se conserva solo uno de cada $c$ valores. Conceptualmente, primero se multiplica por un peine de impulsos unitarios y después se suprimen los ceros:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

La multiplicación por el peine genera $c$ copias del espectro con separación $1/c$; la supresión de los ceros dilata el eje de frecuencias en un factor $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

Si el espectro llega hasta $f_\mathrm g$ (normalizada a la frecuencia de muestreo anterior), tras el submuestreo llega hasta $cf_\mathrm g$. Solo se evita el aliasing si $cf_\mathrm g\le\frac12$. En caso contrario, un paso bajo digital debe limitar antes la banda.

**Sobremuestreo por el factor $c$.** Se insertan $c-1$ ceros entre cada dos valores: $s_\uparrow(n)=s(n/c)$ para $n$ divisible por $c$, y 0 en otro caso. El espectro se comprime en un factor $c$, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, y contiene ahora $c-1$ réplicas espectrales en el periodo. Un paso bajo con frecuencia de corte $\frac{1}{2c}$ y ganancia $c$ las elimina. Al hacerlo, rellena los ceros con valores interpolados (la interpolación con funciones si de la etapa [3](#stufe-3) en forma discreta), y los valores originales se conservan. El submuestreo y el sobremuestreo, uno tras otro, cambian la frecuencia de muestreo en un factor racional $c_1/c_2$.

:::abbildung et3/k4rate
Espectros (frecuencia normalizada a la respectiva frecuencia de muestreo) al cambiar la frecuencia de muestreo. El submuestreo dilata la banda; el sobremuestreo la comprime y genera réplicas espectrales, que un filtro de interpolación elimina.
:::

:::aufgabe Ejercicio 10 ★★ Submuestreo
<span class="anker" id="aufg-10"></span>

Una secuencia tiene un espectro hasta $f_\mathrm g=0{,}2$.

<ol class="al">

<li>

¿Puede submuestrearse sin filtro previo por $c=2$? ¿Y por $c=3$?

</li>

<li>

¿Qué debe hacerse antes de submuestrear por $c=3$, y qué se pierde con ello?

</li>

</ol>

:::loesung
(a) $c=2$: después, la banda llega hasta $0{,}4\le0{,}5$; no hay aliasing. $c=3$: hasta $0{,}6>0{,}5$; hay aliasing.

(b) Limitar antes la banda a $\frac{1}{2c}=\frac16\approx0{,}167$ con un paso bajo digital. Al hacerlo se pierden las componentes entre 0,167 y 0,2. Es el precio de la frecuencia de muestreo más baja.
:::
:::

## Etapa 11: La transformada z

<span class="anker" id="stufe-11"></span>

:::zweck
Igual que la transformada de Laplace amplía la transformada de Fourier ([parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)), la transformada z amplía la transformada de Fourier de tiempo discreto: primero se pondera exponencialmente y después se transforma.
:::

**La idea.** Se multiplica la secuencia por $\rho^{-n}$ ($\rho>0$) y se transforma: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$. Con $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$, esto se convierte en una serie de potencias en $z^{-1}$. De forma equivalente: $z^n$ es una función propia de todo sistema LSI, porque $z^{n-k}=z^{-k}z^n$, y el valor propio es $H(z)$:

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz Teorema 11.1 (Transformada z)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

donde la integral de contorno recorre en sentido antihorario una circunferencia $|z|=\rho$ dentro de la región de convergencia.
:::

⁠**Cómo leerlo:** sobre la circunferencia $|z|=\rho$ se encuentra un periodo del espectro de la secuencia ponderada $s(n)\rho^{-n}$. Sobre la __circunferencia unidad__ $|z|=1$, $S(z)$ es el espectro ordinario $S_\mathrm a(f)$, siempre que esta esté dentro de la región de convergencia. Así, el plano de la transformada de Laplace se aplica sobre el plano $z$: el eje imaginario se convierte en la circunferencia unidad, y el semiplano izquierdo, en su interior.

**Pares básicos y región de convergencia.** Con la serie geométrica:

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

Como en Laplace, la misma expresión corresponde a dos señales; solo la región de convergencia decide. En las secuencias por la derecha está fuera de la circunferencia que pasa por el polo más exterior; en las secuencias por la izquierda, dentro de la circunferencia que pasa por el polo más interior; en las bilaterales es un anillo. Para $b^{|n|}$ con $0<b<1$, es el anillo $b<|z|<1/b$.

**Reglas de cálculo.** La convolución se convierte en producto: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. Un retardo de $n_0$ periodos de muestreo se convierte en una multiplicación por $z^{-n_0}$. Con ello, la ecuación en diferencias [(5.2)](#gl-5-2) da

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

Para el sistema del ejercicio [6](#aufg-6), $H(z)=\frac{1+0{,}5z^{-1}}{1-0{,}6z^{-1}}$: cero en $z=-0{,}5$, polo en $z=0{,}6$.

:::satz Teorema 11.2 (Estabilidad)
<span class="anker" id="satz-11-2"></span>

Un sistema LSI causal es estable si y solo si todos los polos de $H(z)$ están en el interior de la circunferencia unidad.
:::

⁠**Por qué:** causal significa región de convergencia fuera del polo más exterior. Estable significa $\sum|h(n)|<\infty$; entonces $H(z)$ converge sobre la circunferencia unidad, que pertenece, por tanto, a la región de convergencia. Ambas cosas a la vez solo son posibles si el polo más exterior está dentro de la circunferencia unidad. Para el sistema recursivo con $H(z)=\frac{1}{1-bz^{-1}}$, esto vuelve a significar $|b|<1$.

**Ejemplo.** $s(n)=0{,}5^n\cos(\pi n/3)\,\varepsilon(n)$. Con $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$ y [(11.2)](#gl-11-2) para $b=0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$:

$$S(z)=\frac12\Bigl[\frac{1}{1-0{,}5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0{,}5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0{,}25z^{-1}}{1-0{,}5z^{-1}+0{,}25z^{-2}},\qquad|z|>0{,}5.$$

Polos en $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j}$, ceros en $z=0$ y $z=0{,}25$ (fig. [8](#abb-8)). El módulo de los polos da el decaimiento por periodo de muestreo (0,5), y su ángulo, la oscilación ($\pi/3$ por periodo de muestreo, es decir, seis periodos de muestreo por periodo de la oscilación).

:::abbildung et3/k4zebene
Plano $z$ del ejemplo: polos (cruces) en $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$, ceros (círculos) en 0 y 0,25. La región de convergencia (azul) está fuera de la circunferencia que pasa por los polos y contiene la circunferencia unidad. Leída como respuesta al impulso, la secuencia describe un sistema causal y estable.
:::

:::aufgabe Ejercicio 11 ★★ Aplicar la transformada z
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Comprueba el numerador y el denominador de $S(z)$ del ejemplo reduciendo las dos fracciones a común denominador.

</li>

<li>

¿Tiene la señal del ejemplo un espectro $S_\mathrm a(f)$? Razónalo con la región de convergencia.

</li>

</ol>

:::loesung
(a) Denominador común $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$ con $a=0{,}5\mathrm{e}^{\mathrm{j}\pi/3}$: $a+a^*=2\cdot0{,}25=0{,}5$, $|a|^2=0{,}25$. Numerador $\frac12[2-(a+a^*)z^{-1}]=1-0{,}25z^{-1}$.

(b) Sí. La región de convergencia $|z|>0{,}5$ contiene la circunferencia unidad.
:::
:::

:::aufgabe Ejercicio 12 ★★ Causal o estable
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$.

<ol class="al">

<li>

¿Qué respuesta al impulso tiene la región de convergencia $|z|>2$, y cuál $|z|<2$?

</li>

<li>

¿Cuál de las dos es estable y cuál causal? ¿Hay alguna que sea ambas cosas?

</li>

</ol>

:::loesung
(a) $|z|>2$: $h(n)=2^n\varepsilon(n)$. $|z|<2$: $h(n)=-2^n\varepsilon(-n-1)$, es decir, $-\frac12,-\frac14,\dots$ para $n=-1,-2,\dots$

(b) La primera es causal, pero inestable (crece). La segunda es estable ($\sum_{n\le-1}2^n=1$), pero anticausal. Ambas cosas a la vez no son posibles: el polo en $z=2$ está fuera de la circunferencia unidad, y entonces la región de convergencia no puede estar a la vez fuera del polo y contener la circunferencia unidad.
:::
:::

:::kern Lo esencial
<ul>

<li>

Muestreo ideal: $s_\mathrm a=\sum s(nT)\delta(t-nT)$; espectro $\frac1T\sum_kS(f-k/T)$, periódico con periodo $1/T$.

</li>

<li>

Teorema de muestreo: $f_\mathrm A\ge2f_\mathrm g$; reconstrucción $s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$; si no, aliasing.

</li>

<li>

Discreto en un dominio significa periódico en el otro.

</li>

<li>

Convolución discreta $g(n)=\sum_ms(m)h(n-m)$; $h(n)=\operatorname{Tr}\{\delta(n)\}$; estable: $\sum|h(n)|<\infty$.

</li>

<li>

Recursivo $g(n)=s(n)+bg(n-1)$: $h(n)=b^n\varepsilon(n)$, $H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$.

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$, periodo 1; $s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$.

</li>

<li>

DFT: $S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$, $s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$; FFT $\approx M\,\mathrm{lb}\,M$; convolución circular $\leftrightarrow S_dH_d$.

</li>

<li>

El submuestreo dilata la banda (aliasing si $cf_\mathrm g>\frac12$); el sobremuestreo genera réplicas espectrales.

</li>

<li>

$S(z)=\sum s(n)z^{-n}$; $z^{-n_0}$ = retardo; $H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$; causal y estable: todos los polos en $|z|<1$.

</li>

</ul>
:::
