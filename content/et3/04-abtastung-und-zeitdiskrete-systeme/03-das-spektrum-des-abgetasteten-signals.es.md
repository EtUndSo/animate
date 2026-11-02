---
title: Etapa 2: El espectro de la señal muestreada
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Muestreo y sistemas en tiempo discreto
order: 3240300
summary: ¿Qué le hace el muestreo al espectro?
tags: réplicas espectrales
lang: es
---

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

:::abbildung et3/k4spektrum 1
Un espectro hasta $f_\mathrm g=300$ Hz (azul, triangular para mayor claridad), muestreado. Arriba, con 1 kHz: las copias en los múltiplos de 1 kHz están separadas. Abajo, con 500 Hz: las copias, separadas 500 Hz, se solapan, y la suma (rojo) ya no es el original. Se ha omitido el factor $1/T$.
:::

:::frage ¿Cómo «sabe» el espectro que se ha muestreado? La señal entre los instantes de muestreo simplemente ha desaparecido.
Precisamente por eso. Entre los instantes de muestreo, la señal muestreada es nula, salvo en los impulsos. Toda oscilación que tome los mismos valores en todos los puntos $nT$ describe esta señal igual de bien. El espectro no puede decidirse entre ellas y las contiene todas: el original y sus copias en cada múltiplo de $1/T$.
:::
