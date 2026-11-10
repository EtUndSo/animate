---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Muestreo y sistemas en tiempo discreto
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Capítulo 4: Muestreo y sistemas en tiempo discreto
order: 3241300
summary: De la señal continua a la secuencia de números: teorema de muestreo, convolución discreta, DFT, FFT y transformada z
tags: 
lang: es
---

:::merke La respuesta en tres frases
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

**Un principio detrás de todos los resultados: discreto en un dominio significa periódico en el otro.**

| Resultado | De dónde viene |
|---|---|
| Espectro periódico tras el muestreo | tiempo discreto $\Rightarrow$ espectro periódico (etapa [2](das-spektrum-des-abgetasteten-signals.html#stufe-2)) |
| Teorema de muestreo, aliasing | si las copias periódicas se solapan o no (etapa [3](abtasttheorem-und-ruckgewinnung.html#stufe-3)) |
| Interpolación con funciones si | un paso bajo ideal extrae una copia (etapa [3](abtasttheorem-und-ruckgewinnung.html#stufe-3)) |
| Serie de Fourier | espectro discreto $\Rightarrow$ tiempo periódico (etapa [4](abtastung-im-frequenzbereich.html#stufe-4)) |
| Convolución discreta | integral de convolución sobre impulsos de Dirac ponderados con las muestras (etapa [5](zeitdiskrete-signale-und-die-diskrete-faltung.html#stufe-5)) |
| Transformada de Fourier de tiempo discreto | espectro de las muestras, periódico con periodo 1 (etapa [7](fourier-transformation-zeitdiskreter-signale.html#stufe-7)) |
| DFT | ambos discretos $\Rightarrow$ ambos periódicos (etapa [8](die-diskrete-fourier-transformation-dft.html#stufe-8)) |
| Diezmado, interpolación | muestrear una secuencia ya muestreada (etapa [10](abtastrate-andern-dezimation-und-interpolation.html#stufe-10)) |
| Transformada z | la idea de Laplace para secuencias: primero ponderar, después transformar (etapa [11](die-z-transformation.html#stufe-11)) |
