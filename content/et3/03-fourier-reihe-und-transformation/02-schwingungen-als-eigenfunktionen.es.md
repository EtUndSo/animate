---
title: Etapa 1: Las oscilaciones como funciones propias
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Serie y transformada de Fourier
order: 3230200
summary: De los bloques e pt se usan ahora solo las oscilaciones puras.
tags: respuesta en frecuencia
lang: es
---

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
