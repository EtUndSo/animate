---
title: Etapa 9: Ruido blanco y ruido térmico
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3271000
summary: El modelo más importante de las perturbaciones: ruido con la misma densidad espectral de potencia en todas las frecuencias.
tags: ruido blanco
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
El modelo más importante de las perturbaciones: ruido con la misma densidad espectral de potencia en todas las frecuencias.
:::

:::definition Definición 9.1 (Ruido blanco)
<span class="anker" id="satz-9-1"></span>

Un proceso de media nula con $\Phi_{ss}(f)=N_0$ para todo $f$ se llama __ruido blanco__. Su FAC es $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
:::

⁠**Cómo leerlo:** los valores en instantes distintos están incorrelados, por muy próximos que estén. La potencia $\int N_0\mathrm{d} f$ es infinita: el ruido blanco es un modelo límite, como el impulso de Dirac. Lo que se mide en realidad es siempre ruido filtrado, «coloreado»:

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

Tras un paso bajo ideal con $f_\mathrm g$: $L_g=2N_0f_\mathrm g$ y $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ (fig. [3](#abb-3)). La FAC es nula en los puntos $\tau=k/(2f_\mathrm g)$, $k\neq0$: las muestras separadas según la tasa de Nyquist están incorreladas.

:::abbildung et3/k7tp 3
FAC del ruido blanco tras un paso bajo ideal: $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$. En $\tau=0$, la potencia $2N_0f_\mathrm g$. En los puntos rojos ($\tau=k/(2f_\mathrm g)$) es nula.
:::

**Ruido térmico.** El movimiento térmico de los electrones genera en toda resistencia $R$ una tensión de ruido. En circuito abierto, medida en el rango de frecuencias $|f|\le f_\mathrm g$:

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

con la constante de Boltzmann $k=1{,}38\cdot10^{-23}$ W s/K. A temperatura ambiente (290 K), $kT\approx4\cdot10^{-21}$ W/Hz, es decir, 4 pW por GHz de ancho de banda. $L_{\max}$ es la potencia máxima que puede extraerse de la resistencia con adaptación de potencia. En el modelo de referencia ($1\,\mathrm{k\Omega}$, 20 kHz), el valor eficaz es $\sqrt{\mathrm E\{u^2\}}=0{,}57$ µ V. Este orden de magnitud limita la sensibilidad que puede tener un amplificador de micrófono. El espectro es plano hasta aproximadamente $10^{12}$ Hz.

:::ltspice Medir el ruido térmico
LTspice asigna a cada resistencia su ruido térmico. El análisis `.noise` calcula en un nodo la densidad de ruido `V(onoise)` en V$/\sqrt{\mathrm{Hz}}$. La medida `.meas noise urms INTEG V(onoise)` la integra cuadráticamente sobre el rango de frecuencias del análisis, como en [(8.3)](zufallssignale-in-lti-systemen-leistungsdichte.html#gl-8-3), y da el valor eficaz. `.temp 16.85` ajusta 290 K.

⁠**Resistencia:** `res` con `{Rx}` del nodo `a` a masa y, en paralelo, una fuente `current` con el valor 0 (nombre `I1`). No carga nada; `.noise` solo la necesita como fuente de referencia. Directivas `.param Rx=1k` y `.noise V(a) I1 lin 20001 1 20k`. Resultado: 4,0 nV$/\sqrt{\mathrm{Hz}}$ y `urms` $=0{,}57$ µ V, como arriba. Pon `Rx=1Meg` y compara con tu resultado del ejercicio [8](#aufg-8).

⁠**$kT/C$:** fuente `voltage` `V1` con el valor 0 y `AC 1`, `res` con `{Rx}` hacia `out`, `cap` con `1p` a masa. Directivas `.step param Rx list 1k 1Meg` y `.noise V(out) V1 dec 200 1 1T` y, de nuevo, `.temp 16.85` y la medida `urms`. `urms` es igual para ambas resistencias. Compara el valor con tu resultado del ejercicio [9](#aufg-9)(b).
:::

:::aufgabe Ejercicio 8 ★ Ruido de una resistencia
<span class="anker" id="aufg-8"></span>

Calcula el valor eficaz del ruido de una resistencia de $1\,\mathrm{M\Omega}$ a 290 K y con 20 kHz de ancho de banda. ¿En qué factor es mayor que en la resistencia de $1\,\mathrm{k\Omega}$ y por qué precisamente en ese?

:::loesung
El valor eficaz crece con $\sqrt R$: es $\sqrt{1000}=31{,}6$ veces mayor, es decir, $0{,}566\cdot31{,}6=17{,}9$ µ V.
:::
:::

:::aufgabe Ejercicio 9 ★★ El ruido $kT/C$
<span class="anker" id="aufg-9"></span>

El ruido térmico de la resistencia ($N_0=2kTR$) pasa por el circuito RC que forma con un condensador $C$ ($h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$).

<ol class="al">

<li>

Demuestra con [(9.1)](#gl-9-1) que la potencia de ruido en el condensador es $kT/C$, independientemente de $R$.

</li>

<li>

¿Cuánto vale el valor eficaz con $C=1$ pF y 290 K? ¿Por qué aquí no ayuda una resistencia más pequeña?

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$. Por tanto, $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$.

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V. Una resistencia más pequeña genera, es cierto, menos ruido por hercio, pero el circuito RC se vuelve de banda más ancha ($1/RC$ mayor). Ambos efectos se compensan exactamente. Solo un condensador mayor reduce el ruido.
:::
:::
