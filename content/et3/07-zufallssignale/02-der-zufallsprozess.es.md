---
title: Etapa 1: El proceso aleatorio
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Señales aleatorias
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Capítulo 7: Señales aleatorias
order: 3270200
summary: ¿Cómo se describe una señal cuya evolución no se conoce?
tags: función muestra, proceso aleatorio, variable aleatoria, valor esperado, función de autocorrelación
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
¿Cómo se describe una señal cuya evolución no se conoce? Se imaginan muchas señales del mismo tipo y se promedia sobre ellas.
:::

**La idea.** Si se mide el ruido de muchas resistencias construidas de la misma manera y a la misma temperatura, se obtienen muchas curvas distintas ${}^ks(t)$, $k=1,2,\dots$ (fig. [1](#abb-1)). Cada una de ellas se llama __función muestra__ o realización. La totalidad imaginada de todas ellas se llama __proceso aleatorio__ $s(t)$. Los valores de todas las funciones muestra en un instante fijo $t_1$ forman una __variable aleatoria__ $s(t_1)$.

:::definition Definición 1.1 (Medias de conjunto)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**Cómo leerlo:** $\mathrm E\{\cdot\}$ se llama __valor esperado__ (esperanza) o media de conjunto: se promedia sobre todas las funciones muestra en el mismo instante, es decir, en vertical en la fig. [1](#abb-1). Con $F[x]=x^2$ se obtiene el valor cuadrático medio. La __función de autocorrelación__ promedia el producto de los valores en dos instantes. Indica en qué medida el valor en $t_2$ está relacionado con el valor en $t_1$.

:::abbildung et3/k7schar 1
Tres funciones muestra de un proceso aleatorio (simuladas, valor medio 1). La media de conjunto se forma en vertical, sobre todas las funciones muestra en el mismo $t_1$ (rojo discontinuo). La media temporal se forma en horizontal, a lo largo de una función muestra.
:::
