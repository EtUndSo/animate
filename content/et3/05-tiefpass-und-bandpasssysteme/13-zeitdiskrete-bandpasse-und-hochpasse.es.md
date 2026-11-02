---
title: Etapa 12: Paso banda y paso alto en tiempo discreto
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3251300
summary: Los filtros paso banda y paso alto digitales se obtienen a partir de un paso bajo mediante modulación.
tags: paso alto
lang: es
---

<span class="anker" id="stufe-12"></span>

:::zweck
Los filtros paso banda y paso alto digitales se obtienen a partir de un paso bajo mediante modulación.
:::

Si el paso bajo en tiempo discreto tiene una respuesta al impulso real, la multiplicación por $2\cos(2\pi f_0n)$ desplaza su banda de paso a $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

válido mientras las bandas desplazadas no se solapen: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Debido a la periodicidad, la banda en $f_0$ no puede tocar ni la banda en $-f_0$ ni su copia en $1-f_0$. En general, también para respuestas al impulso paso bajo complejas, se cumple, como en [(8.1)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-1), $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$. El factor 2 corresponde al paso bajo equivalente duplicado, $H_T=2H_{\mathrm{TP}}$.

Un __paso alto__ es un paso bajo desplazado a la mitad de la frecuencia de muestreo, $f_0=\frac12$. Allí coinciden la banda y su imagen especular; por eso se desplaza solo una vez: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. Con $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**En resumen:** un paso alto digital se obtiene de un paso bajo invirtiendo uno de cada dos signos.

:::aufgabe Ejercicio 11 ★ Paso alto a partir de la media móvil
<span class="anker" id="aufg-11"></span>

La media móvil $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) es un paso bajo sencillo.

<ol class="al">

<li>

Forma $h_{\mathrm{HP}}$ según [(12.2)](#gl-12-2).

</li>

<li>

Calcula $H_{\mathrm{TP}}$ y $H_{\mathrm{HP}}$ en $f=0$ y en $f=\frac12$. ¿Encaja esto con un paso alto?

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$.

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$: $|H_{\mathrm{TP}}(0)|=1$, $|H_{\mathrm{TP}}(\frac12)|=\frac13$. El paso alto está desplazado $\frac12$: $|H_{\mathrm{HP}}(0)|=\frac13$, $|H_{\mathrm{HP}}(\frac12)|=1$. Deja pasar completa la secuencia más rápida $(+1,-1,+1,\dots)$ y atenúa la componente continua a un tercio. Un paso alto sencillo, no muy abrupto.
:::
:::
