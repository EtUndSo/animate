---
title: Etapa 8: Envolvente compleja y componentes en cuadratura
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3250900
summary: Lo que vale para los sistemas vale también para las señales: una señal paso banda es una señal paso bajo sobre una portadora.
tags: envolvente compleja, portadora compleja, componentes en cuadratura, envolvente
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Lo que vale para los sistemas vale también para las señales: una señal paso banda es una señal paso bajo sobre una portadora. Esta etapa muestra las distintas formas de escribirlo.
:::

La transformada inversa de [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) da, con la regla de modulación, $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$; por tanto, como $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ se llama __envolvente compleja__, y $\mathrm{e}^{\mathrm{j}2\pi f_0t}$, __portadora compleja__. La mitad de su producto es la componente analítica del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$; es decir, $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Teorema 8.1 (Representación en cuadratura)
<span class="anker" id="satz-8-1"></span>

Con $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ y la transformada de Hilbert $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**Cómo leerlo:** $s_{Tr}$ y $s_{Ti}$ se llaman __componentes en cuadratura__ (en fase y en cuadratura): una modula el coseno de la portadora, y la otra, el seno. $|s_T|$ es la __envolvente__, que en un osciloscopio se ve como el «contorno» de la señal, y $\varphi_T$ es la desviación de fase de la portadora. Si la envolvente compleja es real (caso simétrico), $s(t)=s_T(t)\cos(2\pi f_0t)$: un coseno modulado en amplitud.

:::herleitung Componentes en cuadratura
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. Para [(8.3)](#gl-8-3), con $2s_+=s+\mathrm{j}\hat s$ ([capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Ejercicio 8 ★★ Determinar envolventes complejas
<span class="anker" id="aufg-8"></span>

Determina $s_T$, $s_{Tr}$, $s_{Ti}$ y $|s_T|$ respecto a $f_0=10$ Hz para (a) $s(t)=\bigl[1+0{,}5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0{,}3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Comprueba (c) con [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0{,}5\cos(2\pi t)$, real: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0{,}5\cos(2\pi t)$, entre 0,5 y 1,5. Un coseno modulado en amplitud.

(b) $s_T=\mathrm{e}^{\mathrm{j}0{,}3}$: $s_{Tr}=\cos0{,}3=0{,}955$, $s_{Ti}=\sin0{,}3=0{,}296$, $|s_T|=1$. La envolvente es constante; solo la fase está desplazada en 0,3.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$; por tanto, $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Comprobación: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::
