---
title: Etapa 2: Una señal hecha solo de bloques elementales
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Transformada de Laplace
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Capítulo 2: Transformada de Laplace
order: 3220300
summary: La etapa 1 vale para un solo bloque elemental.
tags: absolutamente integrable, representación de Fourier, espectro
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
La etapa [1](warum-gerade.html#stufe-1) vale para un solo bloque elemental. Solo resulta útil si toda señal puede componerse de bloques $\mathrm{e}^{pt}$. Esta etapa muestra que es posible, cómo se llaman los pesos y dónde están los límites.
:::

### Punto de partida $\sigma=0$: oscilaciones puras

<span class="anker" id="stufe-2-1"></span>

Sobre el eje imaginario ($\sigma=0$), los bloques elementales son oscilaciones puras $\mathrm{e}^{\mathrm{j}2\pi ft}$. Una señal __absolutamente integrable__ ($\int|s(t)|\,\mathrm{d} t<\infty$, es decir, que decae con suficiente rapidez hacia ambos lados) puede componerse a partir de ellas. Es la __representación de Fourier__. Aquí basta con su fórmula. La función $\mathcal{F}\{s\}(f)$ se llama __espectro__ e indica el peso de la oscilación de frecuencia $f$:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Para muchas señales de la teoría de sistemas esto no basta. El escalón $\varepsilon(t)$ no decae, y $\mathrm{e}^{2t}\varepsilon(t)$ (la respuesta al impulso de un sistema inestable) incluso crece. Con oscilaciones de amplitud constante no se puede componer una señal que crece sin límite.
