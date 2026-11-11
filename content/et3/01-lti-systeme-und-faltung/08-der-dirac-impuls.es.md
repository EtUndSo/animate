---
title: Etapa 7: El impulso de Dirac
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210800
summary: El impulso de Dirac es el objeto límite de la etapa 4.
tags: distribución, elemento de retardo ideal, derivación generalizada
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
El impulso de Dirac es el objeto límite de la etapa [4](das-faltungsintegral.html#stufe-4). No es una función ordinaria. Todas sus propiedades se deducen de que solo actúa a través de su área.
:::

**Qué es $\delta$ y qué no es.** Los rectángulos $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ se hacen cada vez más estrechos y altos para $T_0\to0$, y su área sigue siendo 1 (fig. [8](#abb-8)). No existe un límite en el sentido de las funciones ordinarias: una función que es nula en todas partes salvo en un punto tiene área cero, sea cual sea su valor en ese punto. Por eso $\delta(t)$ es una __distribución__: un objeto que solo queda determinado por su efecto bajo una integral, concretamente por [(4.1)](das-faltungsintegral.html#gl-4-1). Se dibuja como una flecha cuya altura indica el peso (el área).

:::abbildung et3/k1dirac 8
Izquierda: rectángulos de área 1, cada vez más estrechos y altos. Derecha: el símbolo del objeto límite. La altura de la flecha es el peso, no el valor de la función.
:::

:::satz Teorema 7.1 (Propiedades del impulso de Dirac)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Peso:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Muestreo:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Área:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Escalado:} && \delta(bt)=\frac{1}{|b|}\,\delta(t)\quad(b\neq0),\qquad \delta(-t)=\delta(t),\\ &\text{Desplazamiento:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**Cómo leerlo:** el producto $s(t)\,\delta(t-T)$ solo puede tener efecto en el punto $T$, así que solo cuenta $s(T)$. Un impulso comprimido $\delta(bt)$ es igual de «infinitamente alto», pero ya solo tiene área $1/|b|$. Un sistema con $h(t)=\delta(t-t_0)$ retrasa $t_0$ cualquier señal; se llama __elemento de retardo ideal__. Y como el escalón es la integral acumulada del impulso, se pueden derivar funciones con saltos: un salto de altura $A$ se convierte en $A\,\delta$. Esto se llama __derivación generalizada__. Cuidado: muchas operaciones, por ejemplo elevar al cuadrado, $\delta^2$, no están definidas para impulsos de Dirac.

:::herleitung Escalado y producto de muestreo
⁠**Escalado.** Para $b>0$, con $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

Para $b<0$, la sustitución invierte el sentido de integración y resulta $-\frac1b=\frac{1}{|b|}$. Por tanto, $\delta(bt)$ actúa como $\frac1{|b|}\delta(t)$. Con $b=-1$ se obtiene la simetría $\delta(-t)=\delta(t)$.

⁠**Producto de muestreo.** Si se convoluciona $s(t)\delta(t)$ con una $g(t)$ cualquiera, la propiedad de muestreo da

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Ambos actúan igual sobre cualquier $g$; por tanto, $s(t)\delta(t)=s(0)\delta(t)$. Con un desplazamiento se obtiene $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, y $\varepsilon(t-\tau)=1$ exactamente para $\tau\le t$.
:::

:::frage Pero $\delta(0)$ es infinito. Entonces $\delta(2t)$ es lo mismo que $\delta(t)$, ¿no?
No. «Infinitamente alto» no describe $\delta$, porque todos los valores de la función salvo en $0$ son iguales, y el valor en $0$ no es un número. Lo que caracteriza a $\delta$ es su área. Si se comprime el rectángulo de área 1 a la mitad de su anchura y se deja igual la altura, el área se reduce a la mitad. Por eso $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Ejercicio 8 ★ Calcular con $\delta$
<span class="anker" id="aufg-8"></span>

Calcula: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0{,}135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::
