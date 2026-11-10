---
title: Etapa 2: Por qué se calienta la resistencia
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Potencia, adaptación y rendimiento
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Capítulo 7: Potencia, adaptación y rendimiento
order: 1170300
summary: En la resistencia, la energía abandona el circuito.
tags: potencia nominal, hipérbola
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
En la resistencia, la energía abandona el circuito. Esta etapa muestra el mecanismo y el límite que se deriva de él.
:::

**La idea.** Si una resistencia está sometida a una tensión, en su interior hay un campo. Este acelera cada electrón libre. Tras el tiempo de vuelo $T$, el electrón choca y pierde de nuevo la velocidad dirigida ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Su energía cinética pasa entonces a la red cristalina, los átomos vibran con más fuerza, y esa vibración es calor (fig. [2](#abb-2)). El electrón es solo el mensajero: detrás de la resistencia tiene la misma deriva que delante, porque la corriente y la sección son iguales. Ha perdido potencial sin hacerse más rápido. Así pues, toda la energía está en la red cristalina. La deriva en sí no cuenta: a 0,44 µ m/s ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), un electrón lleva $8{,}8\cdot10^{-44}$ J, y a 9 V cede $1{,}44\cdot10^{-18}$ J, $1{,}6\cdot10^{25}$ veces más.

:::abbildung et1/k7stoss 2
Modelo de choques para un electrón. Durante el vuelo crece el trabajo del campo (azul), que queda como energía cinética en el electrón. En el choque, el calor en la red salta en $W_1$ (rojo). Tras cada choque, ambas curvas están a la misma altura: todo pasa a la red.
:::

:::satz Teorema 2.1 (Calor de Joule y potencia nominal)
<span class="anker" id="satz-2-1"></span>

En una resistencia, toda la potencia eléctrica se convierte en calor:

<span class="anker" id="gl-2-1"></span>
$$P=U\,I=R\,I^2=\frac{U^2}{R}. \tag{2.1}$$

Un componente solo lo soporta hasta su __potencia nominal__ $P_\mathrm{max}$:

<span class="anker" id="gl-2-2"></span>
$$P\le P_\mathrm{max}. \tag{2.2}$$
:::

⁠**Cómo leerlo:** Una pequeña resistencia de película tiene $P_\mathrm{max}=250$ mW; un calefactor transforma 2 kW. La fórmula es cuadrática porque la corriente cuenta dos veces: el doble de corriente significa el doble de culombios por segundo, y por $U=R\,I$ cada uno cede el doble. A igual corriente (serie), el calor crece con $R$; a igual tensión (paralelo), disminuye con $R$. **Validez:** $P=U\,I$ vale siempre; las otras dos formas, solo para la resistencia óhmica ($R$ independiente de la corriente), y $U$ e $I$ deben corresponder a esa resistencia.

:::herleitung De los choques a $U^2/R$
En el modelo del [capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), un electrón se acelera con $a=e\,E/m_\mathrm e$ y alcanza $v_\mathrm{max}=a\,T$ en el trayecto $s=\frac12a\,T^2$. El campo realiza el trabajo $e\,E\,s=m_\mathrm e\,a\,s=\frac12m_\mathrm e(a\,T)^2=W_1$, exactamente la energía cinética en el choque. En el volumen $A\,L$ hay $n\,A\,L$ electrones libres, y cada uno choca $1/T$ veces por segundo:

$$P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L.$$

Aquí, $\sigma=n\,e\,\mu$ y $\mu=e\,T/(2\,m_\mathrm e)$ ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Con $U=E\,L$ y $R=L/(\sigma A)$ resulta $P=U^2/R$.
:::

**Potencia nominal.** La temperatura sube hasta que el componente cede al entorno por segundo tanto calor como se genera en su interior. Más potencia significa, por tanto, mayor temperatura, y una temperatura demasiado alta lo destruye. En el diagrama de la fig. [3](#abb-3), el límite es la __hipérbola__ $I=P_\mathrm{max}/U$, y cada resistencia es una recta por el origen. Su intersección está en $U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ e $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$.

:::abbildung et1/k7grenze 3
Límite de una resistencia de 250 mW. Cada valor de resistencia solo puede funcionar hasta la hipérbola: 25 $\Omega$ hasta 100 mA, 100 $\Omega$ hasta 50 mA, 400 $\Omega$ hasta 25 mA.
:::

::::beispiel
Con 100 $\Omega$ y 250 mW se permiten $U_\mathrm{max}=5$ V e $I_\mathrm{max}=50$ mA. Con 9 V ideales se generarían 810 mW, 3,24 veces el límite. Haría falta $R\ge(9\,\mathrm{V})^2/250\,\mathrm{mW}=324\,\Omega$.
::::

⁠**Casos límite:** $R\to\infty$ da $P\to0$. $R\to0$ da, con tensión fija, $P\to\infty$. Solo lo impide la resistencia interna de la fuente (etapa [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)).

:::frage El hilo calefactor y la línea de alimentación llevan la misma corriente. ¿Por qué solo se pone incandescente el hilo calefactor?
A igual corriente, el calor es proporcional a $R$. Una línea de alimentación de 10 m$\Omega$ solo transforma 2,5 mW con 0,5 A; la carga de 16 $\Omega$, en cambio, 4 W, 1600 veces más. En secadores de pelo y soldadores, el calor es el objetivo; en la línea es una pérdida (etapa [4](leitungsverluste.html#stufe-4)).
:::

:::aufgabe Ejercicio 2 ★★ ¿Cuál se calienta más?
<span class="anker" id="aufg-2"></span>

Dos resistencias de 100 $\Omega$ y 300 $\Omega$, ambas de 250 mW, están conectadas a 12 V. Predice primero cuál se calienta más en cada caso. (a) Están en serie. (b) Están en paralelo. Calcula todas las potencias. (c) ¿Dónde se supera la potencia nominal?

:::loesung
(a) Serie: $I=12\,\mathrm{V}/400\,\Omega=30$ mA, y $P=R\,I^2$ da 90 mW y 270 mW. Se calienta más la resistencia mayor: los mismos culombios, y cada uno cede allí el triple. (b) Paralelo: $P=U^2/R$ da 1,44 W y 0,48 W. Se calienta más la menor: la misma energía por culombio, pero el triple de culombios. (c) En serie, la resistencia de 300 $\Omega$ está sobrecargada con 270 mW; en paralelo lo están ambas.
:::
:::
