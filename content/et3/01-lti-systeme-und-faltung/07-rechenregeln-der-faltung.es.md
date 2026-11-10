---
title: Etapa 6: Reglas de cálculo de la convolución
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210700
summary: La convolución se comporta en muchos aspectos como una multiplicación.
tags: producto de convolución, idealmente libre de distorsión
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
La convolución se comporta en muchos aspectos como una multiplicación. Cada regla de cálculo tiene un significado para los sistemas.
:::

La integral de convolución se escribe abreviadamente como __producto de convolución__ $g(t)=s(t)*h(t)$. La ecuación [(4.1)](das-faltungsintegral.html#gl-4-1) queda entonces $s(t)=s(t)*\delta(t)$.

<ol class="al">

<li>

⁠**Elemento neutro.** $s*\delta=s$: el impulso de Dirac desempeña el papel del uno. Un sistema con $h(t)=\delta(t)$ transmite cualquier señal sin cambios; se dice que es __idealmente libre de distorsión__.

</li>

<li>

⁠**Ley conmutativa.** $s*h=h*s$. Significado: la entrada y la respuesta al impulso pueden intercambiar sus papeles. El sistema con la respuesta al impulso $s$ responde a la entrada $h$ igual que el sistema $h$ a la entrada $s$.

</li>

<li>

⁠**Ley asociativa.** $(f*s)*h=f*(s*h)$. Significado: dos sistemas en cascada actúan como un único sistema cuya respuesta al impulso es la convolución de las dos respuestas al impulso.

</li>

<li>

⁠**Ley distributiva.** $f*(s+h)=f*s+f*h$. Significado: dos sistemas conectados en paralelo cuyas salidas se suman actúan como un sistema con la suma de las respuestas al impulso.

</li>

<li>

⁠**Señales complejas.** Como la convolución es lineal, se descompone en partes reales e imaginarias:

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung Ley conmutativa
Sustitución $\tau'=t-\tau$, es decir, $\tau=t-\tau'$ y $\mathrm{d}\tau=-\mathrm{d}\tau'$. Los límites $\tau=\mp\infty$ pasan a ser $\tau'=\pm\infty$; al intercambiarlos se anula el signo menos:

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke 7
Arriba: conexión en cascada, respuesta al impulso $h_1*h_2$ (ley asociativa). Abajo: conexión en paralelo con suma, respuesta al impulso $h_1+h_2$ (ley distributiva).
:::

:::aufgabe Ejercicio 7 ★★ Dos circuitos RC en cascada
<span class="anker" id="aufg-7"></span>

Se conectan uno tras otro dos circuitos RC con $RC=1$ s. El segundo no carga al primero (por ejemplo, gracias a un seguidor de tensión entre ambos).

<ol class="al">

<li>

Calcula la respuesta al impulso de la cascada, $h*h$ con $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

</li>

<li>

¿Cuándo es máxima y cuánto vale su área?

</li>

<li>

¿Por qué hace falta la condición «no carga»?

</li>

</ol>

:::loesung
(a) Para $t\ge0$:

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

Por tanto, $h_{\text{cascada}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$.

(b) Derivada $(1-t)\mathrm{e}^{-t}=0$ en $t=1$ s, máximo $\mathrm{e}^{-1}=0{,}368$. Área $\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$ (producto de las áreas).

(c) Sin desacoplo, el segundo circuito RC extrae corriente del primer condensador. Entonces la tensión en el primer condensador ya no es la de un circuito RC sin carga, y la cascada no tiene $h*h$ como respuesta al impulso. Sigue siendo un sistema LTI, pero con otra respuesta al impulso. La convolución de las respuestas individuales presupone que ningún sistema influye de vuelta sobre su entrada.
:::
:::
