---
title: Etapa 7: Conectar fuentes entre sí
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1150900
summary: A menudo no basta una fuente.
tags: corriente de circulación
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
A menudo no basta una fuente. La conexión en serie aumenta la tensión; la conexión en paralelo, la corriente. Esta etapa calcula ambas y señala el peligro.
:::

**La idea.** En serie, por ambas fuentes circula la misma corriente, y sus tensiones en los terminales se suman para cualquier corriente. En paralelo, ambas tienen la misma tensión, y sus corrientes se suman para cualquier tensión. Por eso, la conexión en serie se calcula en la forma de fuente de tensión y la conexión en paralelo en la forma de fuente de corriente. De dos rectas sale de nuevo una recta, es decir, otra vez una fuente real.

:::satz Teorema 7.1 (Conexión de fuentes reales)
<span class="anker" id="satz-7-1"></span>

Dos fuentes en serie o en paralelo, respectivamente, actúan como una sola:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{eq}=U_\mathrm{q1}+U_\mathrm{q2},\quad R_\mathrm{eq}=R_\mathrm{q1}+R_\mathrm{q2} \qquad\text{o bien}\qquad I_\mathrm{eq}=I_\mathrm{q1}+I_\mathrm{q2},\quad G_\mathrm{eq}=G_\mathrm{q1}+G_\mathrm{q2}. \tag{7.1}$$

Para la conexión en paralelo, esto significa en forma de fuente de tensión

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{eq}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}},\qquad R_\mathrm{eq}=R_\mathrm{q1}\parallel R_\mathrm{q2}. \tag{7.2}$$
:::

⁠**Cómo leerlo:** La tensión de [(7.2)](#gl-7-2) es una media ponderada, y la fuente de menor resistencia cuenta más. Dos fuentes iguales dan $U_\mathrm{q}$ y $R_\mathrm{q}/2$ en paralelo, $2U_\mathrm{q}$ y $2R_\mathrm{q}$ en serie. **Validez:** Las conexiones en serie de fuentes de tensión y en paralelo de fuentes de corriente no son técnicamente críticas. Las fuentes de tensión en paralelo necesitan tensiones iguales o suficiente resistencia interna: con $U_\mathrm{q1}\neq U_\mathrm{q2}$, ya sin carga circula una __corriente de circulación__

<span class="anker" id="gl-7-3"></span>
$$I_\mathrm{circ}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}. \tag{7.3}$$

Sale de la fuente más fuerte y entra en la más débil. Dos fuentes de tensión ideales con tensiones distintas no se deben conectar en paralelo, ni dos fuentes de corriente ideales con corrientes distintas en serie: el modelo no tiene entonces solución.

:::herleitung En paralelo en la forma de fuente de corriente
Ambas fuentes tienen la tensión $U_\mathrm{AB}$, y la ley de los nudos suma sus corrientes: $I_\mathrm{A}=(I_\mathrm{q1}-G_\mathrm{q1}U_\mathrm{AB})+(I_\mathrm{q2}-G_\mathrm{q2}U_\mathrm{AB})=(I_\mathrm{q1}+I_\mathrm{q2})-(G_\mathrm{q1}+G_\mathrm{q2})U_\mathrm{AB}$. Esta es de nuevo la forma de [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1). Con [(6.1)](spannungsquelle-oder-stromquelle.html#gl-6-1) se deduce de ella [(7.2)](#gl-7-2). En serie, la ley de las mallas suma las tensiones de forma análoga. La corriente de circulación es la tensión de la malla $U_\mathrm{q1}-U_\mathrm{q2}$ dividida por la resistencia de la malla.
:::

:::abbildung et1/k5zusammen 8
A la izquierda, dos baterías iguales en paralelo. A la derecha, las curvas características: en paralelo se mantiene la tensión de circuito abierto y se duplica la corriente de cortocircuito. En serie se duplica la tensión de circuito abierto y se mantiene la corriente de cortocircuito. Los puntos muestran los puntos de trabajo con 16 $\Omega$.
:::

**Ejemplo.** Dos baterías del modelo de referencia. En paralelo: 9 V, 1 $\Omega$, $I_\mathrm{CC}=9$ A. Forma de corriente como comprobación: $4{,}5+4{,}5=9$ A y $0{,}5+0{,}5=1$ S. En serie: 18 V, 4 $\Omega$, $I_\mathrm{CC}=4{,}5$ A. En 16 $\Omega$, la conexión en paralelo entrega 8,47 V y 0,529 A; la conexión en serie, 14,4 V y 0,9 A (fig. [8](#abb-8)). La conexión en paralelo aporta aquí poco, porque 2 $\Omega$ son poco frente a 16 $\Omega$.

Si una de las baterías está descargada a 8 V, según [(7.3)](#gl-7-3) circulan en circuito abierto $1\,\mathrm{V}/4\,\Omega=0{,}25$ A. Ambos terminales están a 8,5 V, también según [(7.2)](#gl-7-2). **Caso límite:** Con solo 10 m$\Omega$ de resistencia interna cada una serían 50 A. Por eso, las celdas de batería grandes solo se conectan en paralelo con la misma tensión. Para $U_\mathrm{q1}=U_\mathrm{q2}$, la corriente de circulación desaparece.

:::frage ¿Dos baterías en paralelo dan más tensión?
En circuito abierto no, ambas dan 9 V. Bajo carga un poco, porque la corriente se reparte entre dos resistencias internas y en el interior cae solo la mitad. La verdadera ganancia es una corriente de cortocircuito el doble de grande y el doble de cantidad de carga.
:::

:::aufgabe Ejercicio 8 ★★ Batería vieja y batería nueva
<span class="anker" id="aufg-8"></span>

Una batería recargable nueva (12,6 V, 0,1 $\Omega$) se conecta en paralelo con una vieja (11,8 V, 0,3 $\Omega$). (a) ¿Cuánto vale la corriente de circulación? ¿Qué fuente equivalente resulta? (b) Una carga consume 10 A. ¿Qué tensión se establece y qué entrega cada batería? (c) ¿A partir de qué corriente de carga entrega corriente la batería vieja? ¿Qué ocurre por debajo?

:::loesung
(a) $I_\mathrm{circ}=\frac{0{,}8\,\mathrm{V}}{0{,}4\,\Omega}=2$ A. $U_\mathrm{eq}=\frac{10\,\mathrm{S}\cdot12{,}6\,\mathrm{V}+3{,}33\,\mathrm{S}\cdot11{,}8\,\mathrm{V}}{13{,}33\,\mathrm{S}}=12{,}4$ V, $R_\mathrm{eq}=0{,}1\,\Omega\parallel0{,}3\,\Omega=75$ m$\Omega$. Comprobación: $12{,}6\,\mathrm{V}-0{,}1\,\Omega\cdot2\,\mathrm{A}=12{,}4$ V.

(b) $U=12{,}4\,\mathrm{V}-75\,\mathrm{m\Omega}\cdot10\,\mathrm{A}=11{,}65$ V. Nueva: $\frac{12{,}6-11{,}65}{0{,}1}\,\mathrm{A}=9{,}5$ A. Vieja: $\frac{11{,}8-11{,}65}{0{,}3}\,\mathrm{A}=0{,}5$ A. Suma 10 A.

(c) La batería vieja solo entrega corriente cuando $U<11{,}8$ V, es decir, para $I_\mathrm{L}>\frac{12{,}4-11{,}8}{0{,}075}\,\mathrm{A}=8$ A. Por debajo, la corriente entra en ella, y la batería nueva la carga.
:::
:::
