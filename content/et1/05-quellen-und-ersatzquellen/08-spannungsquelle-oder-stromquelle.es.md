---
title: Etapa 6: Fuente de tensión o fuente de corriente
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Fuentes y fuentes equivalentes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Capítulo 5: Fuentes y fuentes equivalentes
order: 1150800
summary: Para la misma fuente real hay dos esquemas.
tags: equivalentes
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
Para la misma fuente real hay dos esquemas. Esta etapa muestra que ambos describen la misma recta y cómo se convierte uno en el otro.
:::

**La idea.** Una recta se puede leer desde el eje de tensión (altura $U_\mathrm{q}$, pendiente $R_\mathrm{q}$) o desde el eje de corriente (ordenada $I_\mathrm{q}$, pendiente $G_\mathrm{q}$). Dos redes se llaman __equivalentes__ si tienen las mismas curvas características. Entonces ninguna medida en los terminales permite averiguar desde fuera cuál de las dos está conectada.

:::satz Teorema 6.1 (Equivalencia de fuentes reales)
<span class="anker" id="satz-6-1"></span>

Una fuente de tensión real y una fuente de corriente real son equivalentes si se cumple

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}\qquad\text{y}\qquad R_\mathrm{q}=\frac{1}{G_\mathrm{q}}. \tag{6.1}$$
:::

:::herleitung Igualar las rectas
Se despeja la tensión en la ecuación de la fuente de corriente de [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1), $U_\mathrm{AB}=(I_\mathrm{q}-I_\mathrm{A})/G_\mathrm{q}$, y se iguala con la ecuación de la fuente de tensión:

$$\frac{I_\mathrm{q}}{G_\mathrm{q}}-\frac{I_\mathrm{A}}{G_\mathrm{q}}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}.$$

Esto debe cumplirse para toda corriente. Por tanto, los términos sin $I_\mathrm{A}$ y los términos con $I_\mathrm{A}$ deben ser iguales por separado. Eso es [(6.1)](#gl-6-1).
:::

⁠**Cómo leerlo:** La corriente $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$ es la corriente de cortocircuito, y la resistencia sigue siendo la misma. En la forma de fuente de corriente, en circuito abierto toda la corriente de fuente pasa por $G_\mathrm{q}$ y produce allí la tensión de circuito abierto. Si la carga toma corriente, queda menos para $G_\mathrm{q}$ y la tensión baja. Es la misma caída, solo que como reparto de corriente en lugar de reparto de tensión. **Validez:** La equivalencia solo vale en los terminales y solo para $0<R_\mathrm{q}<\infty$.

:::abbildung et1/k5umwandlung 7
La misma batería en el mismo punto de trabajo. A la izquierda circulan 0,5 A por todo. A la derecha, la corriente de fuente de 4,5 A se reparte en 4 A por la conductancia y 0,5 A hacia la carga. En los terminales coinciden la tensión y la corriente.
:::

::::beispiel
La batería de 9 V y 2 $\Omega$ se convierte en $I_\mathrm{q}=4{,}5$ A y $G_\mathrm{q}=0{,}5$ S. En el punto de trabajo con 8 V, la conductancia toma $0{,}5\,\mathrm{S}\cdot8\,\mathrm{V}=4$ A, y para la carga quedan 0,5 A (fig. [7](#abb-7)).
::::

⁠**Caso límite:** Para $R_\mathrm{q}\to0$, $I_\mathrm{q}\to\infty$. Una fuente de tensión ideal no tiene forma de fuente de corriente, y una fuente de corriente ideal no tiene forma de fuente de tensión.

**¿Qué forma se elige?** Para calcular, las dos son igual de buenas. Se toma la forma que muestra mejor el comportamiento: las fuentes de tensión tienen baja resistencia (idealmente cero), las fuentes de corriente tienen alta resistencia (idealmente infinita). Si $R_\mathrm{q}$ es pequeña frente a la carga, la tensión apenas cambia y se elige la forma de fuente de tensión. Si $R_\mathrm{q}$ es grande frente a la carga, la corriente apenas cambia y se elige la forma de fuente de corriente.

:::frage Si las dos son iguales, ¿la batería disipa 40,5 W en circuito abierto?
No. A la derecha en la fig. [7](#abb-7), en circuito abierto circulan 4,5 A por 2 $\Omega$, lo que con $P=UI$ ([capítulo 7](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)) serían 40,5 W. La batería real se mantiene fría; aquí acierta la imagen de la fuente de tensión con 0 W. Los circuitos equivalentes son correctos en los terminales, no en el interior. Lo que ocurre dentro depende de la construcción, no de la curva característica. En el punto de trabajo pasa lo mismo: 0,5 W frente a 32 W en el interior, y fuera 4 W en ambos casos.
:::

:::aufgabe Ejercicio 7 ★ Convertir
<span class="anker" id="aufg-7"></span>

(a) Convierte 5 V con 100 $\Omega$ en una fuente de corriente. (b) Convierte 20 mA con 1 k$\Omega$ en paralelo en una fuente de tensión. (c) Conecta 400 $\Omega$ a las dos formas de (a) y compara tensión y corriente.

:::loesung
(a) $I_\mathrm{q}=5\,\mathrm{V}/100\,\Omega=50$ mA, $G_\mathrm{q}=10$ mS. (b) $U_\mathrm{q}=20\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=20$ V, $R_\mathrm{q}=1$ k$\Omega$.

(c) Fuente de tensión: divisor de tensión, $U=5\,\mathrm{V}\cdot\frac{400}{500}=4$ V, $I=10$ mA. Fuente de corriente: $50\,\mathrm{mA}\cdot(100\,\Omega\parallel400\,\Omega)=50\,\mathrm{mA}\cdot80\,\Omega=4$ V, $I=4\,\mathrm{V}/400\,\Omega=10$ mA. Iguales.
:::
:::
