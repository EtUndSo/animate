---
title: Etapa 6: Paso bajo en tiempo discreto, diseño con ventanas
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3250700
summary: ¿Cómo se diseña un paso bajo digital?
tags: 
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
¿Cómo se diseña un paso bajo digital? Exactamente igual que el analógico causal: se toma el paso bajo ideal, se retrasa y se trunca con una ventana.
:::

El paso bajo ideal en tiempo discreto tiene la respuesta en frecuencia rectangular repetida periódicamente y la respuesta al impulso

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

es decir, en el modelo de referencia ($f_\mathrm g=0{,}2$), $h(0)=0{,}4$, $h(\pm1)=0{,}303$, $h(\pm2)=0{,}094$, $h(\pm3)=-0{,}062$. Tampoco este es causal. Se multiplica por una ventana $w(n)$ de $2N+1$ valores, se desplaza $N$ y se obtiene un filtro FIR de fase lineal. La ventana determina el resultado (fig. [4](#abb-4)):

<ul>

<li>

⁠**Ventana rectangular:** la transición más abrupta, pero lóbulos secundarios altos. En el modelo de referencia ($N=10$), la banda de rechazo a partir de $f=0{,}3$ todavía alcanza $-26{,}6$ dB, y la banda de paso fluctúa en aproximadamente $\pm0{,}5$ dB.

</li>

<li>

⁠**Ventana de Hann:** transición más suave, pero una banda de rechazo mucho más profunda: a partir de $f=0{,}3$ como máximo $-45{,}9$ dB; la banda de paso es plana con un margen de $0{,}05$ dB.

</li>

</ul>

La razón es la misma que en la transformada de Fourier de tiempo corto del [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): el espectro de la ventana se convoluciona con el ideal, y los bordes abruptos del rectángulo producen lóbulos secundarios que decrecen lentamente.

:::abbildung et3/k5fenster 4
Módulo de la respuesta en frecuencia de dos filtros FIR paso bajo con $f_\mathrm g=0{,}2$ y 21 coeficientes. Ventana rectangular: flanco abrupto, a partir de $f=0{,}3$ atenuación solo hasta $-26{,}6$ dB. Ventana de Hann: flanco más tendido, a partir de $f=0{,}3$ como máximo $-45{,}9$ dB.
:::

:::aufgabe Ejercicio 6 ★ Filtro de media banda
<span class="anker" id="aufg-6"></span>

Calcula los coeficientes $h(0)$ a $h(3)$ del paso bajo ideal en tiempo discreto con $f_\mathrm g=0{,}25$. ¿Qué llama la atención y por qué ahorra esto trabajo de cálculo en un filtro FIR?

:::loesung
$h(n)=0{,}5\operatorname{si}(\pi n/2)$: $h(0)=0{,}5$, $h(\pm1)=\frac1\pi=0{,}318$, $h(\pm2)=0$, $h(\pm3)=-\frac{1}{3\pi}=-0{,}106$. Todos los coeficientes pares, salvo $h(0)$, son nulos, porque $\sin(\pi n/2)=0$ para $n$ par. En el filtro FIR desaparecen estas multiplicaciones, casi la mitad.
:::
:::
