---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El condensador
order: 1131200
summary: Cómo entra corriente en un aislante y dónde está después la energía
tags: energía del campo, constante de tiempo
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Un condensador no deja pasar la carga, sino que la desplaza: los electrones abandonan una placa y llegan a la otra, y en ambos terminales circula en el mismo instante la misma corriente.

</li>

<li>

La carga separada $Q$ crea el campo entre las placas. Este campo determina la tensión $U=Q/C$, y en él reside la __energía del campo__ $\frac12CU^2$, almacenada en el espacio entre las placas.

</li>

<li>

La carga necesita corriente y tiempo, de modo que la tensión no salta. En el primer instante, el condensador vacío actúa como un cortocircuito (corriente con 0 V); el lleno, como un circuito abierto (tensión sin corriente). Entre ambos transcurre una curva exponencial con la __constante de tiempo__ $\tau=RC$, el tiempo que marca el ritmo del proceso de carga.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

El condensador separa carga: $+Q$ y $-Q$, carga total cero. En ambos terminales circula la misma corriente; por el hueco no pasa carga.

</li>

<li>

Capacidad: $C=Q/U$; $i=C\,\mathrm{d} u/\mathrm{d} t$; $u(t)=u(t_0)+\frac1C\int_{t_0}^ti\,\mathrm{d} t'$. $u$ no salta; la corriente continua se bloquea.

</li>

<li>

Condensador de placas: $C=\varepsilon A/d$ con $\varepsilon=\varepsilon_0\varepsilon_\mathrm{r}$, $\varepsilon_0=8{,}854\cdot10^{-12}$ A s/(V m).

</li>

<li>

Energía: $W=\frac12CU^2=\frac12QU=Q^2/(2C)$, en el campo con la densidad $w=\frac12\varepsilon E^2$.

</li>

<li>

En paralelo: $C_\mathrm{G}=\sum C_i$. En serie: $1/C_\mathrm{G}=\sum1/C_i$.

</li>

<li>

Isla: $Q_\mathrm{tot}=\sum C_iU_i=$ const. La energía no se conserva en el proceso.

</li>

<li>

Carga: $u_C=U_0(1-\mathrm{e}^{-t/\tau})$, $i=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Descarga: $u_C=U_0\,\mathrm{e}^{-t/\tau}$, $i=-\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Constante de tiempo $\tau=RC$.

</li>

<li>

En general: $u_C(t)=u_\infty+(u_C(0)-u_\infty)\,\mathrm{e}^{-t/\tau}$. Vacío actúa en el primer instante como un cortocircuito; lleno, como un circuito abierto.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** La tensión indica cuánta carga está separada, y la carga solo cambia mediante corriente. De estos dos hechos, $u=q/C$ e $i=\mathrm{d} q/\mathrm{d} t$, se derivan todos los resultados de este capítulo.

| Resultado | De dónde viene |
|---|---|
| Corriente a pesar del hueco | La carga se desplaza, no se transmite (etapa [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)) |
| $Q=CU$ | Doble carga, doble campo, doble tensión (etapa [2](die-kapazitat.html#stufe-2)) |
| $i=C\,\mathrm{d} u/\mathrm{d} t$, $u$ no salta | La corriente es carga por unidad de tiempo (etapa [3](strom-und-spannung-am-kondensator.html#stufe-3)) |
| $C=\varepsilon A/d$ | El campo por unidad de carga depende del área, la separación y el material (etapa [4](plattenkondensator-und-dielektrikum.html#stufe-4)) |
| Tipos constructivos | $A$ grande, $d$ pequeño, $\varepsilon$ grande (etapa [5](bauformen-und-selbstentladung.html#stufe-5)) |
| $W=\frac12CU^2$ | Cada carga adicional avanza contra la tensión ya presente (etapa [6](die-gespeicherte-energie.html#stufe-6)) |
| Conexión en paralelo y en serie | Misma tensión o misma carga (etapa [7](parallel-und-reihenschaltung.html#stufe-7)) |
| Redistribución de carga | La carga no puede abandonar una isla (etapa [8](ladungserhaltung-beim-umschalten.html#stufe-8)) |
| Cortocircuito, circuito abierto, curva exponencial | La corriente depende de la tensión que ella misma crea (etapa [9](aufladen-uber-einen-widerstand.html#stufe-9)) |
| Descarga, $\tau=RC$ | La misma realimentación con otro valor inicial (etapa [10](entladen-und-zeitkonstante.html#stufe-10)) |
