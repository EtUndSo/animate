---
title: Etapa 7: La distribución gaussiana
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3270800
summary: ¿Por qué el ruido tiene tan a menudo una distribución gaussiana y cómo se calcula con ella?
tags: teorema central del límite, función de error
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
¿Por qué el ruido tiene tan a menudo una distribución gaussiana y cómo se calcula con ella?
:::

Si se convolucionan muchas densidades entre sí, el resultado se aproxima a una curva de Gauss (__teorema central del límite__, [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). El ruido es casi siempre la suma de muchísimas contribuciones pequeñas e independientes, por ejemplo de los movimientos de muchos electrones. Por eso tiene una distribución gaussiana.

:::satz Teorema 7.1 (Distribución gaussiana)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

con la __función de error__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$ y $\operatorname{erfc}=1-\operatorname{erf}$.
:::

⁠**Cómo leerlo:** el valor medio y la varianza determinan por completo la distribución gaussiana (o normal). Dentro de $\pm\sigma_s$ en torno al valor medio está el 68,3 % de los valores; dentro de $\pm2\sigma_s$, el 95,4 %; dentro de $\pm3\sigma_s$, el 99,73 %. La integral de la curva de Gauss no tiene forma cerrada; de ahí la función erf, que se tabula o se calcula numéricamente. Para $x$ grande, $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Reglas de cálculo.** La suma de dos variables gaussianas independientes es gaussiana con $m_s=m_1+m_2$ y $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Un proceso gaussiano sigue siendo gaussiano tras un sistema LTI, porque la integral de convolución es una suma ponderada (infinita). Y para dos variables conjuntamente gaussianas, «incorreladas» es lo mismo que «independientes»: si la covarianza cruzada normalizada $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ es nula, la densidad conjunta se descompone en un producto.

:::zusatz la densidad gaussiana bidimensional
Para $s,g$ de media nula y conjuntamente gaussianas con el coeficiente de correlación $\rho$:

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

Se obtiene a través de las variables normalizadas suma y diferencia $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$: están incorreladas, tienen las varianzas $2(1\pm\rho)$ y, al ser gaussianas, son independientes. Las líneas de igual densidad son elipses. En las coordenadas normalizadas $x/\sigma_s$, $y/\sigma_g$, sus ejes siguen la dirección de estas sumas y diferencias. Para $\rho=0$ se convierten en circunferencias (si $\sigma_s=\sigma_g$), y la densidad es el producto de las densidades individuales.
:::

:::aufgabe Ejercicio 6 ★ Calcular con la distribución gaussiana
<span class="anker" id="aufg-6"></span>

Una tensión de ruido tiene distribución gaussiana con $m=0$ y $\sigma=1$ mV.

<ol class="al">

<li>

¿Con qué probabilidad es mayor que 2 mV? (Pista: $\operatorname{erfc}(1{,}414)=0{,}0455$.)

</li>

<li>

Se suman dos de estas tensiones, independientes. ¿Qué distribución tiene la suma?

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1{,}414)=0{,}023$, es decir, el 2,3 %.

(b) Gaussiana con $m=0$ y $\sigma^2=2$ mV$^2$, $\sigma=1{,}41$ mV.
:::
:::
