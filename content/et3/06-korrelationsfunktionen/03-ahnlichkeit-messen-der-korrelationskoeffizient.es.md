---
title: Etapa 2: Medir la semejanza, el coeficiente de correlación
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Funciones de correlación
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Capítulo 6: Funciones de correlación
order: 3260300
summary: ¿Cómo se mide con un solo número cuánto se parecen dos señales?
tags: coeficiente de correlación, ortogonales
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
¿Cómo se mide con un solo número cuánto se parecen dos señales? Midiendo lo grande que es su diferencia.
:::

**La idea.** La energía de la diferencia $\Delta(t)=s(t)-g(t)$ es pequeña si las señales se parecen. Desarrollando el producto:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

Así pues, la diferencia reside únicamente en la integral del producto. Para que el tamaño de las señales no cuente, se normalizan ambas a energía 1. Entonces $E_\Delta=2-2\operatorname{Re}\,p_{sg}$, con el __coeficiente de correlación__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**Cómo leerlo:** $|p_{sg}|\le1$ (desigualdad de Cauchy-Schwarz). $p=1$ significa $s=a\,g$ con $a>0$: la misma forma. $p=-1$ significa $s=-a\,g$: la misma forma, con el signo invertido. $p=0$ significa $\int s^*g\,\mathrm{d} t=0$: las señales son __ortogonales__, como los armónicos de una serie de Fourier en el [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Ejemplo: $\operatorname{rect}(t)$ y $\Lambda(t)$ tienen $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0{,}75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$; por tanto, $p=0{,}919$.

:::aufgabe Ejercicio 2 ★★ Coeficientes de correlación
<span class="anker" id="aufg-2"></span>

Calcula $p$ para (a) $\operatorname{rect}(t)$ y $\operatorname{rect}(t-0{,}5)$, (b) $\operatorname{rect}(t)$ y $\Lambda(t)$ (resultado de arriba), (c) $\operatorname{rect}(t)$ y $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) Los rectángulos se solapan en una longitud de 0,5; por tanto, $\int=0{,}5$, y ambas energías valen 1: $p=0{,}5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0{,}75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0{,}75}{\sqrt{2/3}}=0{,}919$. Formas muy parecidas. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$; las señales son ortogonales, aunque coinciden en la mitad derecha.
:::
:::
