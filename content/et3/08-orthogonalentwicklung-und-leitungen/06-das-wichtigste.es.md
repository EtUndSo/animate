---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Desarrollo ortogonal y líneas de transmisión
order: 3280600
summary: Dos temas complementarios: señales como vectores, ondas en líneas eléctricas
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Con funciones base ortonormales, el mejor coeficiente de una función es su correlación con la función base, y la energía es la suma de los cuadrados de los coeficientes.

</li>

<li>

En una línea de transmisión, toda tensión es una superposición de una onda incidente (progresiva) y una onda reflejada (regresiva). La línea queda descrita por la constante de propagación $\gamma$ y la impedancia característica $Z$.

</li>

<li>

Si la línea se termina con su impedancia característica, la onda reflejada desaparece. En una línea sin pérdidas, todas las frecuencias se propagan igual de rápido, y las señales llegan sin distorsión.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Ortonormal: $\int s_is_j\mathrm{d} t=\delta_{ij}$; mejores coeficientes $b_i=\int fs_i\mathrm{d} t$; $E_r=E_f-\sum b_i^2$; completo: $E_f=\sum b_i^2$.

</li>

<li>

Ecuaciones de la línea: $\partial_su=-(R'+L'\partial_t)i$, $\partial_si=-(G'+C'\partial_t)u$.

</li>

<li>

Fasores (con $\omega=2\pi f$): $\underline U=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$; $\gamma=\sqrt{(R'+\mathrm{j}\omega L')(G'+\mathrm{j}\omega C')}=\alpha+\mathrm{j}\beta$; $Z=\sqrt{\frac{R'+\mathrm{j}\omega L'}{G'+\mathrm{j}\omega C'}}$.

</li>

<li>

Terminación con $Z$: sin reflexión; $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$.

</li>

<li>

Sin pérdidas: $Z=\sqrt{L'/C'}$, $v=1/\sqrt{L'C'}$, $u=u_\mathrm{prog}(s-vt)+u_\mathrm{reg}(s+vt)$.

</li>

</ul>
:::
