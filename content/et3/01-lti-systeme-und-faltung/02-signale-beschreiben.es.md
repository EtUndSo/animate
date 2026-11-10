---
title: Etapa 1: Describir señales
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210200
summary: Antes de estudiar sistemas hace falta un lenguaje para las señales: algunas formas básicas y dos operaciones sobre el eje de tiempo, desplazar y escalar.
tags: señal, normalizadas, periodo, frecuencia
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Antes de estudiar sistemas hace falta un lenguaje para las señales: algunas formas básicas y dos operaciones sobre el eje de tiempo, desplazar y escalar.
:::

Una __señal__ es la evolución de una magnitud física en el tiempo, escrita como función $s(t)$. En teoría de sistemas se suele calcular con magnitudes __normalizadas__: tiempos en múltiplos de 1 s, tensiones en múltiplos de 1 V. Así, las ecuaciones entre magnitudes se convierten en ecuaciones entre valores numéricos, y $\mathrm{e}^{-t}$ puede escribirse sin problemas de unidades.

**Señales elementales.** Algunas señales pueden describirse con una expresión sencilla y aparecen una y otra vez (fig. [1](#abb-1)):

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{(gaussiana)},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

El escalón $\varepsilon(t)$ y el rectángulo $\operatorname{rect}(t)$ presentan saltos. Qué valor rige exactamente en el punto del salto es cuestión de convenio. A menudo se elige ahí $\tfrac12$: así, rectángulos colocados uno a continuación de otro dan exactamente 1 en todas partes.

:::abbildung et3/k1elementar 1
Señales elementales. Abajo a la derecha, un rectángulo desplazado y escalado: centro en $t_0=2$, anchura $T=2$, altura $a=0{,}8$.
:::

**Desplazar y escalar.** De una señal se obtienen otras nuevas transformando el eje de tiempo:

<ul>

<li>

⁠**Desplazar:** $t\to t-t_0$. Para $t_0>0$, la señal se *retrasa* $t_0$, es decir, se desplaza hacia la derecha.

</li>

<li>

⁠**Escalar:** $t\to t/T$. Para $|T|>1$ la señal se ensancha, para $0<|T|<1$ se estrecha, y para $T<0$ además se refleja.

</li>

</ul>

Ambas operaciones juntas, más una amplitud $a$, dan por ejemplo el pulso rectangular

<span class="anker" id="gl-1-1"></span>
$$s(t)=a\operatorname{rect}\Bigl(\frac{t-t_0}{T}\Bigr)=\begin{cases}a & |t-t_0|\le |T|/2\\ 0 & \text{en otro caso}\end{cases} \tag{1.1}$$

con centro $t_0$, duración $|T|$ y altura $a$. Se comprueba sustituyendo el argumento $(t-t_0)/T$ en la definición de $\operatorname{rect}$. Del mismo modo, $\sin(2\pi t/T)=\sin(2\pi Ft)$ es el seno escalado con __periodo__ $T$ y __frecuencia__ $F=1/T$.

:::frage ¿Por qué $t-t_0$ desplaza la señal hacia la derecha, si se está restando algo?
La nueva señal muestra en el instante $t$ el valor que la antigua tenía en el instante $t-t_0$, es decir, *antes*. Todo lo que hacía la señal antigua, la nueva lo hace $t_0$ más tarde. Lo más sencillo es comprobarlo en un punto característico: el flanco de $\varepsilon(t-t_0)$ está donde el argumento se anula, en $t=t_0$.
:::

**La exponencial compleja.** Lo más importante para la teoría de sistemas es

$$\mathrm{e}^{\mathrm{j}2\pi Ft}=\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft).$$

De un par complejo conjugado se obtienen, según Euler, las oscilaciones reales:

$$\cos(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2},\qquad \sin(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}-\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2\mathrm{j}}.$$

En una oscilación, un retardo $t_0$ aparece como un desfase:

<span class="anker" id="gl-1-2"></span>
$$\cos\bigl(2\pi F(t-t_0)\bigr)=\cos(2\pi Ft+\varphi)=\operatorname{Re}\bigl\{\mathrm{e}^{\mathrm{j}2\pi Ft}\,\mathrm{e}^{\mathrm{j}\varphi}\bigr\},\qquad\varphi=-2\pi Ft_0. \tag{1.2}$$

⁠**En resumen:** en una oscilación, retrasar es lo mismo que girar la fase, y en $\mathrm{e}^{\mathrm{j}2\pi Ft}$ es incluso lo mismo que multiplicar por el número $\mathrm{e}^{\mathrm{j}\varphi}$.

:::aufgabe Ejercicio 1 ★ Desplazar, escalar, fase
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

¿Dónde empieza y dónde termina $s(t)=2\operatorname{rect}\bigl(\frac{t-3}{4}\bigr)$, y qué altura tiene el pulso?

</li>

<li>

Escribe un pulso rectangular que tenga la altura 0,5 V desde $t=1$ s hasta $t=4$ s.

</li>

<li>

Esboza $s(-t)$ para $s(t)=\varepsilon(t-1)$. ¿Dónde está el flanco?

</li>

<li>

Un coseno con $F=50$ Hz se retrasa $t_0=5$ ms. ¿Qué fase $\varphi$ tiene después?

</li>

</ol>

:::loesung
(a) Centro $t_0=3$, duración $T=4$: de $t=1$ a $t=5$, altura 2.

(b) Centro 2,5 s, duración 3 s: $s(t)=0{,}5\operatorname{rect}\bigl(\frac{t-2{,}5}{3}\bigr)$.

(c) $s(-t)=\varepsilon(-t-1)$. El flanco está donde el argumento se anula: $-t-1=0$, es decir, $t=-1$. El valor es 1 donde el argumento es $\ge0$, es decir, para $t\le-1$. Un escalón reflejado: 1 a la izquierda de $-1$, 0 a la derecha.

(d) $\varphi=-2\pi Ft_0=-2\pi\cdot50\,\mathrm{Hz}\cdot5\,\mathrm{ms}=-\pi/2=-90^\circ$. Un retardo de un cuarto de periodo es un cuarto de vuelta.
:::
:::
