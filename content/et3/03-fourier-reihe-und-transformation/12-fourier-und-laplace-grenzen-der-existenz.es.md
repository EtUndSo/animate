---
title: Etapa 11: Fourier y Laplace, límites de la existencia
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3231200
summary: ¿Cuándo existe la integral de Fourier y cómo se relaciona con la transformada de Laplace?
tags: teorema central del límite
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
¿Cuándo existe la integral de Fourier y cómo se relaciona con la transformada de Laplace?
:::

Una condición suficiente para la existencia es la integrabilidad absoluta, $\int|s(t)|\mathrm{d} t<\infty$. La transformada de Laplace amplía la clase ponderando antes con $\mathrm{e}^{-\sigma t}$ ([capítulo 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

Así, examina una señal en dos aspectos: sus componentes de frecuencia, como la transformada de Fourier, y su crecimiento o decrecimiento exponencial. Si $\sigma=0$ está en la región de convergencia, la transformada de Fourier es la transformada de Laplace en el eje imaginario. Sin embargo, con impulsos de Dirac (etapa [8](singulare-signale-und-linienspektren.html#stufe-8)), la transformada de Fourier abarca también señales que la transformada de Laplace no abarca: constantes y oscilaciones que se extienden a todo el eje temporal. En general, basta con que se cumpla $\int|s(t)|\mathrm{e}^{-c|t|}\mathrm{d} t<\infty$ para todo $c>0$. Entonces la señal puede crecer como una potencia $t^n$, pero no exponencialmente.

:::zusatz Por qué las convoluciones múltiples se vuelven gaussianas
Si se convolucionan entre sí $M$ rectángulos $\operatorname{rect}(t)$, el espectro es $\operatorname{si}^M(\pi f)$. Para valores pequeños de $f$, $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ y $\ln(1+w)\approx w$, por tanto

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

Para $M$ grande solo contribuye la zona de valores pequeños de $f$, y la aproximación es cada vez mejor. Para $M=4$, el valor exacto en $t=0$ es $0{,}667$; la curva de Gauss da $0{,}691$. Es un caso del __teorema central del límite__ (parte sobre estadística): la convolución de muchos pulsos positivos de área finita se aproxima a una curva de Gauss. Un ejemplo es la respuesta al impulso de una cadena de muchos integradores cortos.
:::

:::aufgabe Ejercicio 14 ★★★ (Para profundizar) Comprobar la aproximación gaussiana
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Compara, para $M=2$, el valor exacto $\Lambda(0)=1$ con la aproximación gaussiana.

</li>

<li>

Demuestra que la curva de Gauss $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ tiene área 1. ¿Por qué tiene que ser así?

</li>

</ol>

:::loesung
(a) $M=2$: $\sqrt{6/(2\pi)}=0{,}977$ en lugar de $\Lambda(0)=1$, es decir, un 2,3 % menos. Para $M=4$: 0,691 en lugar de 0,667, es decir, un 3,6 % más. Así pues, ya tras pocas convoluciones la curva de Gauss está cerca del resultado exacto. La aproximación solo se vuelve arbitrariamente buena para $M$ grande, porque solo entonces contribuyen al espectro únicamente los valores pequeños de $f$.

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$; multiplicado por $\sqrt{6/(\pi M)}$ da 1. Tiene que ser así: el área de una convolución es el producto de las áreas, aquí $1^M=1$. En el espectro, es el valor en $f=0$, $\operatorname{si}^M(0)=1$, y la aproximación $\mathrm{e}^{-M(\pi f)^2/6}$ también vale 1 ahí.
:::
:::
