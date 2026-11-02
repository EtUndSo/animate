---
title: Etapa 10: Esquema en cuadratura y muestreo paso banda
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3251100
summary: ¿Cómo se obtienen técnicamente las componentes en cuadratura?
tags: 
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
¿Cómo se obtienen técnicamente las componentes en cuadratura? ¿Y cuántas muestras necesita una señal paso banda?
:::

**Esquema en cuadratura.** Si se multiplica una señal paso banda por $\cos(2\pi f_0t)$ y se filtra con un paso bajo, queda $\frac12s_{Tr}$. Con $-\sin(2\pi f_0t)$ queda $\frac12s_{Ti}$. La razón es trigonométrica:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{en }2f_0,\text{ los elimina el paso bajo}},$$

y, del mismo modo, $-s\sin=\frac12s_{Ti}+(\text{componentes en }2f_0)$. La condición es que la banda termine por debajo de $2f_0$. En el dominio paso bajo se filtra entonces con cuatro filtros paso bajo ($h_{Tr}$, $\pm h_{Ti}$) según [(9.1)](bandpasssignal-durch-bandpasssystem.html#gl-9-1). A la salida se vuelve a modular sobre la portadora según [(8.2)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-2), o se forma la envolvente $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (fig. [6](#abb-6)).

:::abbildung et3/k5quadratur 6
Demodulador en cuadratura: obtiene de una señal paso banda las dos componentes en cuadratura, es decir, la envolvente compleja.
:::

**Teorema de muestreo para señales paso banda.** Una señal paso banda de ancho de banda $\Delta f$ tiene, respecto a la frecuencia central, componentes en cuadratura que son señales paso bajo hasta $\Delta f/2$. Cada una puede muestrearse con $1/T=\Delta f$:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

En total hacen falta $2\Delta f$ valores por segundo, tantos como para una señal paso bajo con frecuencia de corte $\Delta f$. Por tanto, lo que importa es el ancho de banda, no la frecuencia más alta.

:::aufgabe Ejercicio 9 ★★ Muestrear una señal de radio
<span class="anker" id="aufg-9"></span>

Una señal ocupa la banda de 10,0 a 10,2 MHz.

<ol class="al">

<li>

¿Qué frecuencia de muestreo haría falta según el teorema de muestreo ordinario?

</li>

<li>

¿Cuántas muestras por segundo bastan en total con el esquema en cuadratura, y con qué frecuencia se muestrea cada rama?

</li>

</ol>

:::loesung
(a) Al menos $2\cdot10{,}2=20{,}4$ MHz.

(b) $\Delta f=0{,}2$ MHz. Cada rama se muestrea con 0,2 MHz ($T=5$ µ s); en total, 0,4 MHz, unas cincuenta veces menos.
:::
:::
