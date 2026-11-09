---
title: Etapa 4: De la señal periódica a la no periódica
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Serie y transformada de Fourier
order: 3230500
summary: Un pulso aislado no es periódico.
tags: densidad espectral
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Un pulso aislado no es periódico. Pero se puede entender como una señal periódica de periodo infinitamente largo. Al hacerlo, la suma se convierte en una integral.
:::

**La idea.** Se prolonga periódicamente un pulso $s(t)$ de duración menor que $T$. Los coeficientes de la serie son entonces valores de una función fija:

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

Si se duplica el periodo, la separación $F$ entre líneas se reduce a la mitad, y las líneas muestrean la misma envolvente $S(f)$ con el doble de densidad (fig. [4](#abb-4)). En el caso límite $T\to\infty$, la separación $F$ se convierte en el diferencial $\mathrm{d} f$, y la suma $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$, en la integral.

:::abbildung et3/k3grenz 4
Un pulso rectangular $\operatorname{rect}(t)$, prolongado periódicamente con $T=2$ s y $T=4$ s. Los coeficientes de Fourier multiplicados por $T$ están sobre la misma envolvente $S(f)=\operatorname{si}(\pi f)$, con separación $1/T$. Para $T\to\infty$ llenan la curva sin huecos.
:::

:::satz Teorema 4.1 (Transformada de Fourier)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

Notación abreviada: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ o $S(f)=\mathcal{F}\{s(t)\}$.
:::

⁠**Cómo leerlo:** $S(f)$ es una __densidad espectral__: peso por intervalo de frecuencia. Si $s$ es una tensión en V, $S$ tiene la unidad V/Hz. La transformada inversa compone la señal a partir de todas las oscilaciones, cada una con el peso $S(f)\,\mathrm{d} f$. Una condición suficiente para la existencia es $\int|s(t)|\mathrm{d} t<\infty$. La transformada de Fourier es la transformada de Laplace en el eje imaginario, $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$, siempre que el eje imaginario esté en la región de convergencia ([parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)).

⁠**La convolución se convierte en producto.** Como en la [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html): $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$. De $s*\delta=s$ se sigue $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, es decir, $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: el impulso de Dirac contiene todas las frecuencias con el mismo peso.

::::beispiel el pulso exponencial
La respuesta al impulso del circuito RC, $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$:

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

Es la misma respuesta en frecuencia que da el cálculo de corriente alterna ([parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Por tanto, la respuesta al impulso contiene toda la información sobre el comportamiento en frecuencia.
::::

:::frage ¿Qué diferencia hay entre $S_p(k)$ y $S(f)$, aparte de que una es discreta?
La unidad. $S_p(k)$ es una amplitud (V): el $k$-ésimo armónico tiene realmente esa intensidad. $S(f)$ es una densidad (V/Hz): en una señal no periódica, ninguna frecuencia aislada tiene una amplitud finita; solo una banda de frecuencias $\Delta f$ aporta aproximadamente $S(f)\,\Delta f$. Por eso $S_p(k)=F\cdot S(kF)$: cada línea representa una banda de anchura $F$.
:::

:::aufgabe Ejercicio 4 ★ El pulso exponencial bilateral
<span class="anker" id="aufg-4"></span>

Calcula $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$ para $a>0$ dividiendo la integral en $t<0$ y $t>0$. Demuestra que el resultado es real y par, y justifícalo con la simetría de la señal.

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

Real y par en $f$. Tiene que ser así: la señal es real y par; por tanto, su parte impar es nula, y con ella también $\operatorname{Im} S$ (etapa [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)).
:::
:::
