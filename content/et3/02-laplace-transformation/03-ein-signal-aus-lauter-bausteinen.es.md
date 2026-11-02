---
title: Etapa 2: Una señal hecha solo de bloques elementales
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220300
summary: La etapa 1 vale para un solo bloque elemental.
tags: absolutamente integrable
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
La etapa [1](warum-gerade.html#stufe-1) vale para un solo bloque elemental. Solo resulta útil si toda señal puede componerse de bloques $\mathrm{e}^{pt}$. Esta etapa muestra que es posible, cómo se llaman los pesos y dónde están los límites.
:::

### Punto de partida $\sigma=0$: oscilaciones puras

<span class="anker" id="stufe-2-1"></span>

Sobre el eje imaginario ($\sigma=0$), los bloques elementales son oscilaciones puras $\mathrm{e}^{\mathrm{j}2\pi ft}$. Una señal __absolutamente integrable__ ($\int|s(t)|\,\mathrm{d} t<\infty$, es decir, que decae con suficiente rapidez hacia ambos lados) puede componerse a partir de ellas. Es la representación de Fourier, que se trata en detalle en la parte dedicada a la transformada de Fourier:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Para muchas señales de la teoría de sistemas esto no basta. El escalón $\varepsilon(t)$ no decae, y $\mathrm{e}^{2t}\varepsilon(t)$ (la respuesta al impulso de un sistema inestable) incluso crece. Con oscilaciones de amplitud constante no se puede componer una señal que crece sin límite.
