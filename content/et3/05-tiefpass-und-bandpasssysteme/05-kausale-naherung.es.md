---
title: Etapa 4: Aproximación causal
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3250500
summary: ¿Cómo se construye algo que se acerque lo más posible al paso bajo ideal?
tags: 
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
¿Cómo se construye algo que se acerque lo más posible al paso bajo ideal? Se retrasa la respuesta al impulso y se corta el resto.
:::

**La idea.** Se desplaza $h(t)$ hacia la derecha en $t_0$ hasta que la parte en $t<0$ sea despreciable, y se corta. La envolvente de la función si decrece como $1/(2\pi f_\mathrm g|t|)$. Si antes de $t=0$ debe ser inferior al 1 % del máximo, hace falta $t_0\approx16/f_\mathrm g$. Con una ventana simétrica de anchura $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**Cómo leerlo:** cortar es multiplicar por una ventana; en el espectro, por tanto, es una convolución con el espectro si de la ventana. El flanco abrupto se difumina y aparecen ondulaciones. El factor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ es el retardo: el filtro causal tiene fase lineal; retrasa todas las frecuencias por igual (fig. [2](#abb-2)). Cuanto mayor es $t_0$, más estrecha es la transición, pero más tarde llega la respuesta.

:::abbildung et3/k5kausal 2
Módulo del paso bajo causal enventanado con $f_\mathrm g=1$ Hz y $t_0=3$ s (azul); en trazo discontinuo, el ideal. En el flanco aparece una zona de transición con $|H_k(f_\mathrm g)|=0{,}49$, y antes de ella, ondulaciones de hasta 1,10.
:::

:::aufgabe Ejercicio 4 ★★ ¿Cuánto retardo cuesta la causalidad?
<span class="anker" id="aufg-4"></span>

Un paso bajo con $f_\mathrm g=1$ kHz debe aproximarse de forma causal. El paso bajo ideal desplazado debe quedar por debajo del 1 % de su máximo antes de $t=0$, es decir, en la parte cortada.

<ol class="al">

<li>

¿Qué valor mínimo debe tener $t_0$?

</li>

<li>

¿Qué supone esto para una llamada telefónica con diez de estos filtros en cadena?

</li>

</ol>

:::loesung
(a) La envolvente $\frac{1}{2\pi f_\mathrm g|t|}<0{,}01$ exige $|t|>\frac{100}{2\pi f_\mathrm g}=15{,}9$ ms. Por tanto, $t_0\approx16$ ms.

(b) Diez filtros retrasan unos 0,16 s. En la llamada, esto se nota como retardo. La causalidad de un filtro abrupto cuesta tiempo, y tanto más cuanto más estrecha es la banda.
:::
:::
