---
title: Etapa 6: Correlación de señales paso banda
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Funciones de correlación
order: 3260700
summary: También las funciones de correlación de las señales paso banda se calculan con las envolventes complejas (parte 5).
tags: 
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
También las funciones de correlación de las señales paso banda se calculan con las envolventes complejas ([parte 5](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)).
:::

La FCC de dos señales paso banda reales vuelve a ser una señal paso banda:

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

La señal reflejada tiene la envolvente $s_T^*(-t)$, porque

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

Con la regla de transmisión $g_T=\frac12s_T*h_T$ de la [parte 5](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html):

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**Cómo leerlo:** la correlación de dos señales paso banda es la mitad de la correlación de sus envolventes, modulada sobre la portadora. La energía de una señal paso banda es la mitad de la energía de su envolvente compleja: un coseno de amplitud $|s_T|$ solo tiene, en promedio, la mitad de la potencia.
