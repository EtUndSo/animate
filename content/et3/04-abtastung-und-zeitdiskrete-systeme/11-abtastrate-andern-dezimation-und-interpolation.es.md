---
title: Etapa 10: Remuestreo: diezmado e interpolación
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Muestreo y sistemas en tiempo discreto
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Capítulo 4: Muestreo y sistemas en tiempo discreto
order: 3241100
summary: Una secuencia puede representarse a posteriori con una frecuencia de muestreo menor o mayor.
tags: 
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Una secuencia puede representarse a posteriori con una frecuencia de muestreo menor o mayor. Para el espectro valen las mismas reglas que en el primer muestreo.
:::

**Submuestreo por el factor $c$.** Se conserva solo uno de cada $c$ valores. Conceptualmente, primero se multiplica por un peine de impulsos unitarios y después se suprimen los ceros:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

La multiplicación por el peine genera $c$ copias del espectro con separación $1/c$; la supresión de los ceros dilata el eje de frecuencias en un factor $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

Si el espectro llega hasta $f_\mathrm g$ (normalizada a la frecuencia de muestreo anterior), tras el submuestreo llega hasta $cf_\mathrm g$. Solo se evita el aliasing si $cf_\mathrm g\le\frac12$. En caso contrario, un paso bajo digital debe limitar antes la banda.

**Sobremuestreo por el factor $c$.** Se insertan $c-1$ ceros entre cada dos valores: $s_\uparrow(n)=s(n/c)$ para $n$ divisible por $c$, y 0 en otro caso. El espectro se comprime en un factor $c$, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, y contiene ahora $c-1$ réplicas espectrales en el periodo. Un paso bajo con frecuencia de corte $\frac{1}{2c}$ y ganancia $c$ las elimina. Al hacerlo, rellena los ceros con valores interpolados (la interpolación con funciones si de la etapa [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) en forma discreta), y los valores originales se conservan. El submuestreo y el sobremuestreo, uno tras otro, cambian la frecuencia de muestreo en un factor racional $c_1/c_2$.

:::abbildung et3/k4rate 7
Espectros (frecuencia normalizada a la respectiva frecuencia de muestreo) al cambiar la frecuencia de muestreo. El submuestreo dilata la banda; el sobremuestreo la comprime y genera réplicas espectrales, que un filtro de interpolación elimina.
:::

:::aufgabe Ejercicio 10 ★★ Submuestreo
<span class="anker" id="aufg-10"></span>

Una secuencia tiene un espectro hasta $f_\mathrm g=0{,}2$.

<ol class="al">

<li>

¿Puede submuestrearse sin filtro previo por $c=2$? ¿Y por $c=3$?

</li>

<li>

¿Qué debe hacerse antes de submuestrear por $c=3$, y qué se pierde con ello?

</li>

</ol>

:::loesung
(a) $c=2$: después, la banda llega hasta $0{,}4\le0{,}5$; no hay aliasing. $c=3$: hasta $0{,}6>0{,}5$; hay aliasing.

(b) Limitar antes la banda a $\frac{1}{2c}=\frac16\approx0{,}167$ con un paso bajo digital. Al hacerlo se pierden las componentes entre 0,167 y 0,2. Es el precio de la frecuencia de muestreo más baja.
:::
:::
