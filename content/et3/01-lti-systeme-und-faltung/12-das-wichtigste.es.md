---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3211200
summary: Por qué la respuesta a un único impulso describe todo el sistema
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Toda señal es una superposición de infinitos impulsos cortos: en cada instante $\tau$, un impulso de peso $s(\tau)\,\mathrm{d}\tau$.

</li>

<li>

Un sistema LTI responde a un impulso desplazado con la respuesta al impulso desplazada $h(t-\tau)$ (invariancia en el tiempo), y a una suma de impulsos con la suma de las respuestas (linealidad).

</li>

<li>

Por eso la salida es la convolución $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$, y $h(t)$ describe el sistema por completo.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Desplazar $t\to t-t_0$ retrasa, escalar $t\to t/T$ ensancha; $a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$: centro $t_0$, duración $|T|$, altura $a$.

</li>

<li>

Paso bajo RC: $H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$, $|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$, $\varphi=-\arctan(2\pi FRC)$; respuesta al escalón $1-\mathrm{e}^{-t/RC}$.

</li>

<li>

LTI: principio de superposición y $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$.

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$ y $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$.

</li>

<li>

Calcular: reflejar, desplazar, multiplicar, integrar.

</li>

<li>

$s*\delta=s$; conmutativa, asociativa (cascada: $h_1*h_2$), distributiva (paralelo: $h_1+h_2$).

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$; $\delta(bt)=\delta(t)/|b|$; $\delta(t-t_0)*s=s(t-t_0)$; $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$.

</li>

<li>

Respuesta al escalón $=\int h$, respuesta al impulso $=\frac{\mathrm{d}}{\mathrm{d} t}$(respuesta al escalón).

</li>

<li>

Causal: $h(t)=0$ para $t<0$. Estable: $\int|h|\mathrm{d} t<\infty$.

</li>

</ul>
:::

**Qué sigue.** La convolución da mucho trabajo: cada instante $t$ necesita su propia integral. La parte siguiente descompone las señales de modo que la integral se convierte en una simple multiplicación.

**Un principio detrás de todos los resultados.** La tabla asigna los resultados de este capítulo al principio «descomponer, pasar un bloque por el sistema, recomponer».

| Resultado | De dónde viene |
|---|---|
| Integral de convolución | superponer impulsos, superponer respuestas al impulso desplazadas (etapa [4](das-faltungsintegral.html#stufe-4)) |
| Reflejar al calcular | $h(t-\tau)$ es la respuesta a un impulso que llegó hace $t-\tau$ segundos (etapa [5](die-faltung-ausrechnen.html#stufe-5)) |
| $\delta$ es el elemento neutro | una señal hecha de impulsos, a través de un sistema que deja cada impulso sin cambios (etapa [6](rechenregeln-der-faltung.html#stufe-6)) |
| Leyes conmutativa, asociativa y distributiva | intercambiar los papeles, sistemas en cascada, sistemas en paralelo (etapa [6](rechenregeln-der-faltung.html#stufe-6)) |
| Propiedad de muestreo (de criba), escalado del impulso de Dirac | $\delta$ solo está definido a través de su área (etapa [7](der-dirac-impuls.html#stufe-7)) |
| Respuesta al escalón = integral de la respuesta al impulso | un escalón es la suma de todos los impulsos hasta $t$ (etapa [8](integrieren-und-differenzieren.html#stufe-8)) |
| Causalidad, estabilidad | condiciones sobre $h(t)$: nula antes del impulso, área finita de $\vert h\vert $ (etapa [9](kausal-und-stabil.html#stufe-9)) |
| Convolución sin sistema | la misma superposición, por ejemplo en la suma de los dados al tirar dos dados (etapa [10](faltung-ganz-ohne-system.html#stufe-10)) |
