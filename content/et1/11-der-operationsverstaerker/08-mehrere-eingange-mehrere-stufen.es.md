---
title: Etapa 6: Varias entradas, varias etapas
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1210800
summary: La regla valía para una entrada y un AO.
tags: sumador, restador
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
La regla valía para una entrada y un AO. Esta etapa muestra que trata varias entradas y cadenas enteras sin ninguna idea nueva, porque todas las ecuaciones siguen siendo lineales.
:::

**La idea.** En el __sumador__, varias resistencias llevan a la entrada negativa (fig. [8](#abb-8)). El nudo se queda en 0 V, así que cada fuente ve solo su propia resistencia e impulsa $U_{\mathrm{E}i}/R_{\mathrm{E}i}$, independientemente de las demás. La masa virtual desacopla las fuentes. Todas las corrientes juntas circulan por $R_\mathrm{F}$, la resistencia de realimentación. En el __restador__, una tensión llega a cada entrada. Aquí ayuda la superposición de la [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): se calcula cada fuente por separado, y la otra se convierte en un cable.

:::satz Teorema 6.1 (Sumador, restador, cadena)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{A}=-R_\mathrm{F}\sum_i\frac{U_{\mathrm{E}i}}{R_{\mathrm{E}i}}, \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}. \tag{6.2}$$

Para $R_3=R_1$ y $R_4=R_2$ queda $U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$. Las etapas en cadena se multiplican: $G=G_1\,G_2$.
:::

⁠**Cómo leerlo:** En [(6.2)](#gl-6-2), $U_\mathrm{E1}$ está a través de $R_1$ en la entrada negativa y $U_\mathrm{E2}$ en el divisor $R_3$, $R_4$ antes de la entrada positiva; $R_2$ realimenta. **Validez:** AO en el rango lineal. En la superposición solo la suma tiene que quedar dentro de los límites; los resultados parciales son magnitudes de cálculo.

:::herleitung Restador por superposición
Con $U_\mathrm{E2}=0$ no circula corriente por $R_3$, $R_4$, y la entrada positiva está a 0 V. Es el inversor: $U_\mathrm{A1}=-(R_2/R_1)\,U_\mathrm{E1}$. Con $U_\mathrm{E1}=0$ la fuente se convierte en un cable, así que $R_1$ sigue conectada a masa y no se puede suprimir, porque la salida impulsa corriente a través de ella por $R_2$. Es el amplificador no inversor con $\varphi_+=U_\mathrm{E2}\,R_4/(R_3+R_4)$: $U_\mathrm{A2}=\bigl(1+R_2/R_1\bigr)\varphi_+$. La suma es [(6.2)](#gl-6-2).
:::

:::abbildung et1/k11addsub 8
A la izquierda, el sumador: las corrientes de las tres fuentes se encuentran en el nudo y circulan por $R_\mathrm{F}$. A la derecha, el restador con $R_1=R_3$ y $R_2=R_4$: con 2,00 V y 2,05 V, ambas entradas están a 1,64 V.
:::

**Ejemplos.** ⁠*Sumador* con $R_\mathrm{F}=40$ k$\Omega$, $R_\mathrm{E1}=R_\mathrm{E2}=10$ k$\Omega$, $R_\mathrm{E3}=20$ k$\Omega$ y $0{,}5$ V, $-0{,}2$ V, $0{,}1$ V: las corrientes son 50, $-20$ y 5 µ A, en total 35 µ A, así que $U_\mathrm{A}=-1{,}4$ V. *Restador* con $R_1=R_3=10$ k$\Omega$, $R_2=R_4=40$ k$\Omega$, $U_\mathrm{E1}=2{,}00$ V, $U_\mathrm{E2}=2{,}05$ V: $\varphi_+=0{,}8\cdot2{,}05\,\mathrm{V}=1{,}64$ V. Por $R_1$ circulan $(2{,}00-1{,}64)\,\mathrm{V}/10\,\mathrm{k\Omega}=36$ µ A, así que $U_\mathrm{A}=1{,}64\,\mathrm{V}-36\,\mu\text{A}\cdot40\,\mathrm{k\Omega}=0{,}2$ V. La superposición da $-8{,}0\,\mathrm{V}+8{,}2\,\mathrm{V}$, lo mismo. El modo común de unos 2 V ha desaparecido. *Cadena* de dos inversores con $G_1=-4$ y $G_2=-2$: 0,5 V se convierten en $-2$ V y luego en $+4$ V, así que $G=+8$. **Caso límite:** $U_\mathrm{E1}=U_\mathrm{E2}$ da 0.

**Procedimiento en circuitos mayores.** Primero se determinan los potenciales de las entradas; luego se calcula etapa por etapa de izquierda a derecha. En una cadena, cada salida es la entrada de la etapa siguiente, un potencial con un valor fijo.

:::frage En la Parte 6, los cuadripolos en cadena se cargaban mutuamente. ¿Por qué puedo multiplicar aquí?
Porque la resistencia de salida de la primera etapa es casi cero. Los 10 k$\Omega$ de la segunda etapa cargan 3,75 m$\Omega$, y la pérdida de tensión es $4\cdot10^{-7}$ del valor. El lazo de la primera etapa la compensa.
:::

:::aufgabe Ejercicio 6 ★★★ Sumador y resistencias desiguales
<span class="anker" id="aufg-6"></span>

(a) Un sumador tiene $R_\mathrm{F}=20$ k$\Omega$ y las resistencias de entrada 10, 20 y 5 k$\Omega$. ¿Cuánto vale $U_\mathrm{A}$ con 1 V, $-2$ V y 0,5 V? (b) En el restador del ejemplo, $R_4$ se desvía un 1 % hacia arriba (40,4 k$\Omega$). Calcula los factores delante de $U_\mathrm{E2}$ y $U_\mathrm{E1}$. (c) ¿Qué tensión de salida aparece con $U_\mathrm{E1}=U_\mathrm{E2}=2$ V? (d) ¿Qué valor tiene ahora $U_\mathrm{A}$ con 2,00 V y 2,05 V? ¿Por qué un restador necesita resistencias de tolerancia estrecha?

:::loesung
(a) $U_\mathrm{A}=-(2\cdot1+1\cdot(-2)+4\cdot0{,}5)\,\mathrm{V}=-2$ V. (b) Delante de $U_\mathrm{E2}$: $5\cdot40{,}4/50{,}4=4{,}0079$; delante de $U_\mathrm{E1}$: 4. (c) $2\,\mathrm{V}\cdot0{,}0079=15{,}9$ mV en lugar de 0. (d) $4{,}0079\cdot2{,}05\,\mathrm{V}-8\,\mathrm{V}=0{,}216$ V en lugar de 0,200 V. El 8 % de error procede casi por completo del modo común. Una resistencia con un 1 % de desviación hace que el rechazo sea $4/0{,}0079$, es decir, 54 dB, peor que el del propio AO.
:::
:::
