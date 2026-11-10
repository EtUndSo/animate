---
title: Etapa 10: Transformada de Fourier de tiempo corto
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3231100
summary: El espectro S(f) describe una señal a lo largo de todos los tiempos.
tags: ventana de Hann, espectrograma
lang: es
---

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

:::abbildung et3/k3hann 8
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
