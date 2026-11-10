---
title: Desde cero: Válvula, tensión alterna y energía térmica
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1190200
summary: Cómo el silicio se convierte en una válvula para la corriente y cómo se calcula con ella
tags: tensión alterna, valor de pico, frecuencia, rectificador de media onda, electronvoltio, energía térmica, constante de Boltzmann, distribución de Boltzmann
lang: es
---

Una __tensión alterna__ cambia de signo periódicamente. Aquí es senoidal, $u_\mathrm e(t)=\hat u\sin(2\pi ft)$, con el __valor de pico__ $\hat u$ (mayor valor absoluto) y la __frecuencia__ $f$ (oscilaciones por segundo, unidad Hz). Una oscilación dura $T=1/f$, es decir, 20 ms a 50 Hz. Las letras minúsculas designan magnitudes que dependen del tiempo.

:::abbildung et1/k9einweg 1
Izquierda: diodo con los terminales ánodo (A) y cátodo (K) en serie con una resistencia a una tensión alterna. Arriba a la derecha: en la resistencia aparece solo la semionda positiva, reducida en 0,7 V. Abajo a la derecha: el diodo mantiene 0,7 V al conducir y asume toda la tensión negativa al bloquear. $\hat u=12$ V, 50 Hz.
:::

La fig. [1](#abb-1) muestra el efecto de un diodo. La malla da $u_\mathrm e=u_\mathrm D+u_\mathrm a$. Si $u_\mathrm e$ es positiva, el diodo conduce, en él quedan unos 0,7 V y el resto cae en la resistencia. Si $u_\mathrm e$ es negativa, no circula corriente. Entonces $u_\mathrm a=0$ y el diodo soporta toda la tensión. La tensión alterna se convierte en una tensión con un solo signo. Este circuito se llama __rectificador de media onda__. Su pico es $12\,\mathrm{V}-0{,}7\,\mathrm{V}=11{,}3$ V.

Para explicar el porqué, el capítulo necesita dos magnitudes de energía. El __electronvoltio__ (eV) es la energía que gana un electrón al recorrer 1 V ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1{,}602\cdot10^{-19}$ J. La __energía térmica__ surge porque los átomos y los electrones se mueven de forma desordenada a cualquier temperatura. Su medida es $k_\mathrm BT$, con la temperatura absoluta $T$ en K y la __constante de Boltzmann__ $k_\mathrm B$. A 300 K, $k_\mathrm BT=4{,}14\cdot10^{-21}\,\mathrm{J}=25{,}85$ meV. Las colisiones reparten esta energía de forma desigual: pocas partículas tienen mucha, muchas tienen poca. En equilibrio rige la __distribución de Boltzmann__:

<span class="anker" id="gl-0-1"></span>
$$\text{fracción de partículas con al menos la energía }W=\mathrm{e}^{-W/(k_\mathrm BT)}. \tag{0.1}$$

Por cada $k_\mathrm BT$ más de energía, la fracción baja un factor 2,718; a $10\,k_\mathrm BT$ es $4{,}5\cdot10^{-5}$. La misma ley describe cómo el aire se enrarece con la altura.
