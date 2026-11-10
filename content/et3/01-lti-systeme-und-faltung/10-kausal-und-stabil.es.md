---
title: Etapa 9: Causal y estable
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3211000
summary: Dos propiedades que todo sistema real debe tener pueden leerse directamente en h(t) .
tags: causal, estable
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Dos propiedades que todo sistema real debe tener pueden leerse directamente en $h(t)$.
:::

:::definition Definición 9.1 (Causal, estable)
<span class="anker" id="satz-9-1"></span>

Un sistema se llama __causal__ si la salida no empieza antes que la entrada. Para un sistema LTI, esto significa

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{para }t<0. \tag{9.1}$$

Un sistema se llama __estable__ (más exactamente, estable BIBO, *bounded input, bounded output*) si responde a toda entrada acotada $|s(t)|\le A<\infty$ con una salida acotada.
:::

Causal: un impulso en el instante 0 no puede tener efecto antes. En la convolución solo contribuyen entonces los impulsos del pasado, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.

:::satz Teorema 9.2 (Condición de estabilidad)
<span class="anker" id="satz-9-2"></span>

Un sistema LTI es estable si y solo si su respuesta al impulso es absolutamente integrable:

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung Condición de estabilidad
⁠**Suficiente.** Con la desigualdad triangular para integrales y $|s|\le A$:

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

Si la integral es finita, $g$ está acotada.

⁠**Necesaria.** Si $\int|h|=\infty$, se elige la entrada acotada más desfavorable: $s(t_1-\tau)=\operatorname{sign}h(\tau)$, es decir, siempre $\pm1$ con el signo de $h$. Entonces $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, aunque $|s|\le1$.
:::

Ejemplos: el circuito RC tiene $\int|h|=1$ y es estable. El elemento de retardo ideal ($\int|\delta(t-t_0)|\mathrm{d} t=1$) es estable. El integrador tiene $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ y es inestable: al escalón acotado responde con la rampa no acotada $t\,\varepsilon(t)$.

:::aufgabe Ejercicio 10 ★★ ¿Causal? ¿Estable?
<span class="anker" id="aufg-10"></span>

Estudia (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$, (b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$, (c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$, (d) $h(t)=\mathrm{e}^{-|t|}$, (e) $h(t)=\delta(t+1)$. Para cada sistema inestable, indica una entrada acotada que produzca una salida no acotada.

:::loesung
(a) Causal, $\int|h|=\tfrac12$: estable.

(b) Causal, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$: inestable. El escalón $\varepsilon(t)$ produce $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$, no acotada.

(c) Causal, $\int|h|=1$: estable. El sistema forma la integral de la entrada sobre el último segundo (ventana deslizante).

(d) No causal, porque $h(t)\neq0$ para $t<0$. $\int\mathrm{e}^{-|t|}\mathrm{d} t=2$: estable.

(e) $\delta(t+1)$ actúa en $t=-1<0$: $g(t)=s(t+1)$; el sistema «ve» la entrada con un segundo de antelación. No causal, pero estable ($\int|h|=1$).
:::
:::
