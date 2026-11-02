---
title: Etapa 5: Simetrías en la señal y en el espectro
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Serie y transformada de Fourier
order: 3230600
summary: Si una señal es real, par o impar se ve de inmediato en su espectro.
tags: par, impar
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Si una señal es real, par o impar se ve de inmediato en su espectro. Esta etapa deduce las reglas.
:::

**Partes par e impar.** Una función compleja se llama __par__ si $x(t)=x^*(-t)$, e __impar__ si $x(t)=-x^*(-t)$. (Para funciones reales, es la simetría habitual respecto al eje o respecto al origen, respectivamente.) Toda señal se descompone de forma única en ambas partes:

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz Teorema 5.1 (Simetrías)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

Para señales **reales**, $S(-f)=S^*(f)$: la parte real y el módulo $|S|$ son pares en $f$; la parte imaginaria y la fase, impares. Una señal real y par tiene un espectro real y par. Una señal real e impar tiene un espectro imaginario puro e impar.
:::

:::herleitung Simetrías
Primero: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$. Con $\tau=-t$, esto es $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$. Por tanto

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

Para $s$ real, $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$. En general, $\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$. Así pues, $S(f)=S^*(-f)$.
:::

⁠**En resumen:** en una señal real, la mitad negativa del espectro es la imagen especular conjugada de la positiva. No contiene información nueva.

**Ejemplo.** El pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$ (real) tiene la parte par $\frac12\mathrm{e}^{-|t|}$ y la impar $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Su espectro $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ tiene la parte real par $\frac{1}{1+(2\pi f)^2}$, la transformada de $\frac12\mathrm{e}^{-|t|}$, y la parte imaginaria impar $\frac{-2\pi f}{1+(2\pi f)^2}$ (fig. [5](#abb-5)).

:::abbildung et3/k3gerade 5
El pulso exponencial ($RC=1$ s), descompuesto en una parte par (azul) y una impar (roja). A la derecha, el espectro: la parte par da la parte real (par en $f$); la impar, la parte imaginaria (impar en $f$).
:::

:::aufgabe Ejercicio 5 ★ Leer la simetría
<span class="anker" id="aufg-5"></span>

¿Qué se puede decir del espectro sin hacer cálculos? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) una señal real con $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: ¿cuánto vale $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Real y par: espectro real y par ($\operatorname{si}(\pi f)$). (b) Real e impar: espectro imaginario puro e impar. (c) Compleja, pero $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: en el sentido de la definición, la señal es par; por tanto, su espectro es real. Según la regla de modulación, es $\operatorname{si}(\pi(f-1))$: real, pero no simétrico respecto a $f=0$, porque la señal no es real. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::
