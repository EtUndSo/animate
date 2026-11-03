---
title: Lo esencial hasta aquí
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220900
summary: Toda señal como superposición de $\mathrm{e}^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Un sistema LTI solo puede multiplicar el bloque elemental $\mathrm{e}^{pt}$ por un número $H(p)$, porque para $\mathrm{e}^{pt}$ desplazar es lo mismo que multiplicar.

</li>

<li>

Toda señal con región de convergencia es una superposición de tales bloques. $S(p)$ indica con qué peso está contenido el bloque $\mathrm{e}^{pt}$ en la señal.

</li>

<li>

Por eso la convolución se convierte en una multiplicación, $G(p)=H(p)\,S(p)$. Si $S(p)$ es racional, la señal es una suma finita $\sum_r A_r\mathrm{e}^{p_r t}$ con los polos como exponentes.

</li>

</ol>
:::

:::kern Lo esencial hasta aquí
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$, de ahí $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$ con $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$.

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$: $\sigma$ es la tasa de crecimiento; $f$, la frecuencia del bloque elemental.

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$, $\sigma$ en la región de convergencia; toda recta de este tipo da la misma $s(t)$.

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$; para $\sigma=0$, la transformada de Fourier.

</li>

<li>

Región de convergencia: depende solo de $\sigma$; por la derecha, un semiplano derecho; por la izquierda, uno izquierdo; bilateral, una franja.

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$ para $\operatorname{Re} p>\operatorname{Re} p_0$; $-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$ para $\operatorname{Re} p<\operatorname{Re} p_0$.

</li>

<li>

$G(p)=S(p)H(p)$; derivar $\to p$, integrar $\to1/p$.

</li>

<li>

Racional y por la derecha: $s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$, polos = exponentes. Causal y estable: todos los polos a la izquierda.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** Casi todos los resultados sobre la transformada de Laplace son consecuencia de estas tres frases. La tabla los relaciona; las etapas los explican.

| Resultado | De dónde viene |
|---|---|
| Función propia $\mathrm{e}^{pt}$, función de transferencia $H(p)$ | desplazar $\mathrm{e}^{pt}$ es multiplicar por $\mathrm{e}^{-p\tau}$ (etapa [1](warum-gerade.html#stufe-1)) |
| Transformada de Laplace $S(p)$ | peso del bloque elemental $\mathrm{e}^{pt}$ en la señal (etapa [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)) |
| Región de convergencia | los amortiguamientos $\sigma$ con los que $s(t)\mathrm{e}^{-\sigma t}$ se vuelve absolutamente integrable (apartado [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)) |
| Convolución $\to$ producto, conexión en cascada | cada bloque elemental se multiplica por $H(p)$ (etapa [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Derivada $\to p$, integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ y $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (etapa [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Ecuación diferencial $\to$ cociente de polinomios | cada derivada se convierte en un factor $p$ (etapa [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Polos, fracciones parciales | los exponentes y los pesos de un número finito de bloques elementales (etapa [4](aus-dem-integral-wird-eine-summe.html#stufe-4)) |
| Estabilidad | un bloque causal $\mathrm{e}^{p_r t}$ solo decae si $\operatorname{Re} p_r<0$ (etapa [4](aus-dem-integral-wird-eine-summe.html#stufe-4)) |
| Transformada de Fourier | la misma superposición sobre la recta $\sigma=0$ (etapa [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)) |
