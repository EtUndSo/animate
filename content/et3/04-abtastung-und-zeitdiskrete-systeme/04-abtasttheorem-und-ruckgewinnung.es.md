---
title: Etapa 3: Teorema de muestreo y reconstrucción
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3240400
summary: ¿Cuándo puede recuperarse exactamente el original a partir de las muestras, y cómo?
tags: señal paso bajo, tasa de Nyquist, alias, filtro antialiasing
lang: es
---

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

⁠**Cómo leerlo:** con $f_\mathrm A\ge2f_\mathrm g$, las copias de la fig. [1](das-spektrum-des-abgetasteten-signals.html#abb-1) están separadas. Un paso bajo extrae la copia en $f=0$, que tiene exactamente la forma del original. En el dominio del tiempo, esto significa: cada muestra se sustituye por una función si que vale 1 en su propio instante de muestreo y 0 en todos los demás (fig. [2](#abb-2)). Su suma pasa por todas las muestras y rellena los huecos de modo que no aparece ninguna frecuencia por encima de $f_\mathrm g$. La frecuencia de muestreo mínima $2f_\mathrm g$ se llama __tasa de Nyquist__.

:::herleitung reconstrucción
Para $|f|\le f_\mathrm g$ solo está la copia $k=0$, es decir, $S_\mathrm a(f)=\frac1TS(f)$. Con $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$ se tiene $S_\mathrm a\cdot H_\mathrm{TP}=S$. En el dominio del tiempo: $T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$ ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), rectángulo y si). Con [(1.2)](signalklassen-und-ideale-abtastung.html#gl-1-2) y $2f_\mathrm g=1/T$ resulta $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$.
:::

:::abbildung et3/k4siinterp 2
Interpolación con funciones si: muestras $0;\ 1;\ 0{,}6;\ -0{,}4;\ 0{,}8;\ 0$ (rojo), las funciones si ponderadas (gris) y su suma (azul). Cada función si es nula en los demás instantes de muestreo; por eso la suma pasa exactamente por todos los valores.
:::

**Aliasing.** Si se muestrea demasiado despacio, las copias se solapan. Una frecuencia por encima de $f_\mathrm A/2$ aparece tras la reconstrucción como una frecuencia falsa, más baja: su __alias__. En el modelo de referencia, con $f_\mathrm A=1$ kHz, un coseno de 700 Hz y uno de 300 Hz tienen exactamente las mismas muestras, porque $\cos(2\pi\cdot0{,}7n)=\cos(2\pi n-2\pi\cdot0{,}3n)=\cos(2\pi\cdot0{,}3n)$ (fig. [3](#abb-3)). A posteriori ya no se pueden separar. Por eso, delante de todo muestreador se filtra con un paso bajo (__filtro antialiasing__).

:::abbildung et3/k4alias 3
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
