---
title: Etapa 8: Integrar y derivar
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas LTI y convolución
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Capítulo 1: Sistemas LTI y convolución
order: 3210900
summary: El integrador y el derivador son sistemas LTI.
tags: integrador, derivador, doblete
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
El integrador y el derivador son sistemas LTI. A través de ellos se relacionan la respuesta al escalón y la respuesta al impulso, y se puede obtener la respuesta al impulso del circuito RC a partir de su respuesta al escalón.
:::

**El integrador.** Si en [(7.6)](der-dirac-impuls.html#gl-7-6) se sustituye $\delta$ por una $s$ cualquiera, el mismo cálculo da:

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

Un sistema con la respuesta al impulso $\varepsilon(t)$ forma la integral acumulada de su entrada; se llama __integrador__. Si se lee [(8.1)](#gl-8-1) con los papeles intercambiados ($\varepsilon*s$), dice: **la respuesta al escalón de un sistema es la integral acumulada de su respuesta al impulso.** Comprobación en el circuito RC: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, exactamente [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5). Dos caminos independientes, la ecuación diferencial y la convolución, dan lo mismo.

**El derivador.** Un integrador y un __derivador__ uno tras otro dejan cualquier señal sin cambios; la cascada es idealmente libre de distorsión. Por eso la respuesta al impulso del derivador es la distribución $\delta'(t)$ (__doblete__), definida por

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

De forma aproximada, $\delta'$ es un pulso rectangular doble y estrecho: primero un rectángulo de altura $+1/T_0^2$, luego otro de altura $-1/T_0^2$, cada uno de anchura $T_0$. Se dibuja como un par de flechas, una hacia arriba y otra hacia abajo.

**Respuesta al impulso = derivada de la respuesta al escalón.** Como $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ y el sistema es lineal e invariante en el tiempo, se cumple $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{respuesta al escalón})$. Para el circuito RC, con la regla del producto:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

El segundo sumando desaparece por [(7.2)](der-dirac-impuls.html#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. El mecanismo detrás: la respuesta al escalón del circuito RC no salta; el condensador necesita tiempo para cargarse. Solo una respuesta al escalón con salto produce un impulso de Dirac en $h$ (ejercicio [9](#aufg-9)).

:::aufgabe Ejercicio 9 ★★ Paso alto: un impulso de Dirac en la respuesta al impulso
<span class="anker" id="aufg-9"></span>

Si se intercambian $R$ y $C$, la tensión se toma en $R$ (paso alto CR, $RC=1$ s). Su respuesta al escalón es $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Justifica la respuesta al escalón con el mecanismo: ¿qué tensión hay en $R$ en el primer instante y cuál al cabo de mucho tiempo?

</li>

<li>

Determina la respuesta al impulso derivando. ¿Qué significa físicamente la componente de Dirac?

</li>

<li>

Comprueba: integrar la respuesta al impulso tiene que devolver la respuesta al escalón.

</li>

</ol>

:::loesung
(a) En el primer instante el condensador está descargado y no hay tensión en él. El 1 V completo cae en $R$. Después, la corriente carga el condensador, su tensión crece como $1-\mathrm{e}^{-t}$ y en $R$ queda $\mathrm{e}^{-t}$. Al cabo de mucho tiempo, el condensador está cargado, no circula corriente y en $R$ ya no hay tensión.

(b) Regla del producto:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Aquí la respuesta al escalón salta en $t=0$ de 0 a 1; por eso se conserva la componente de Dirac. Físicamente: un impulso infinitamente corto pasa por completo, porque el condensador no puede crear tensión en un tiempo nulo. La carga que el impulso ha llevado al condensador se descarga después a través de $R$, en sentido contrario: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::
