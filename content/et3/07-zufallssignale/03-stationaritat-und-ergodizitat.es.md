---
title: Etapa 2: Estacionariedad y ergodicidad
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3270300
summary: Nunca se dispone de un conjunto infinito; normalmente solo de una única señal.
tags: estacionario, ergódico
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Nunca se dispone de un conjunto infinito; normalmente solo de una única señal. ¿Cuándo basta con ella?
:::

Un proceso se llama __estacionario__ si ninguno de sus valores medios cambia cuando todos los instantes de observación se desplazan un mismo tiempo $t_0$:

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

Entonces el valor medio $m_s=\mathrm E\{s(t)\}$ es una constante, y la FAC solo depende ya de la separación $\tau=t_2-t_1$: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$. Un proceso estacionario se llama __ergódico__ si, además, toda media temporal de una función muestra es igual a la media de conjunto correspondiente:

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{para todo }k. \tag{2.2}$$

⁠**Cómo leerlo:** estacionario significa que la estadística no cambia con el tiempo. Ergódico significa que una única función muestra, observada durante mucho tiempo, muestra a lo largo del tiempo todo lo que muestra el conjunto entero. El ruido de una resistencia a temperatura constante es ergódico. Solo por eso se puede caracterizar el ruido con un único instrumento de medida.

:::frage ¿Todo proceso estacionario es también ergódico?
No. Ejemplo: cada función muestra es una constante cuyo valor se sortea una sola vez, ${}^ks(t)=c_k$. El proceso es estacionario, porque nada depende de $t$. Pero la media temporal de una función muestra es $c_k$, distinta para cada función muestra, y no la media de conjunto. Una función muestra aislada nunca «ve» los demás valores.
:::
