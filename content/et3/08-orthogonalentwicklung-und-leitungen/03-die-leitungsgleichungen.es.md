---
title: Etapa 2: Las ecuaciones de la línea de transmisión
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Desarrollo ortogonal y líneas de transmisión
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Capítulo 8: Desarrollo ortogonal y líneas de transmisión
order: 3280300
summary: Hasta ahora, las líneas eran conexiones ideales.
tags: parámetros por unidad de longitud
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Hasta ahora, las líneas eran conexiones ideales. Si una línea es larga en comparación con la longitud de onda, una señal necesita un tiempo apreciable para recorrerla. Esta etapa plantea las ecuaciones que lo describen.
:::

**La idea.** La línea se divide en tramos cortos de longitud $\mathrm{d} s$. Cada tramo tiene una resistencia serie y una inductancia serie (los conductores de ida y de retorno), además de una capacidad en paralelo y una conductancia en paralelo (entre los conductores). En una línea uniforme, estas magnitudes son proporcionales a la longitud: $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$, $G'\mathrm{d} s$, con los __parámetros por unidad de longitud__ $R'$, $L'$, $C'$, $G'$ (valores por metro, fig. [1](#abb-1)).

:::abbildung et3/k8element 1
Circuito equivalente de un tramo corto de línea de longitud $\mathrm{d} s$, con los parámetros por unidad de longitud $R'$, $L'$, $G'$, $C'$.
:::

:::satz Teorema 2.1 (Ecuaciones de la línea de transmisión, ecuaciones del telegrafista)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung ecuaciones de la línea de transmisión
Ley de mallas a lo largo del tramo: $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, es decir, $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$. Ley de nudos: de la corriente $i$, una parte se deriva por $G'\mathrm{d} s$ y $C'\mathrm{d} s$, $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$. Dividir entre $\mathrm{d} s$. (En sentido estricto, en la ley de nudos aparece la tensión al final del tramo; la diferencia es de segundo orden en $\mathrm{d} s$.)
:::

⁠**Cómo leerlo:** la tensión cae a lo largo de la línea porque circula corriente por los elementos serie. La corriente disminuye porque se deriva por los elementos en paralelo, entre los conductores. Las dos ecuaciones acoplan $u$ e $i$ en la posición y en el tiempo.
