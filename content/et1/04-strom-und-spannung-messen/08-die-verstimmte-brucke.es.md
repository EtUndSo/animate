---
title: Etapa 7: El puente desequilibrado
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Medir corriente y tensión
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Capítulo 4: Medir corriente y tensión
order: 1140800
summary: Si una resistencia cambia solo un poco o de forma continua, no se reajusta.
tags: galga extensométrica
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Si una resistencia cambia solo un poco o de forma continua, no se reajusta. La desviación de cero es entonces la señal de medida. Esta etapa muestra por qué así se hacen visibles cambios minúsculos.
:::

**La idea.** Un instrumento por sí solo tiene que mostrar toda la tensión, de la que el cambio es una parte ínfima. El puente resta la gran tensión común. Solo queda el cambio, y este cabe en un rango de medida pequeño. Como el error de lectura depende del valor de fondo de escala, disminuye con el rango.

:::satz Teorema 7.1 (Tensión del puente)
<span class="anker" id="satz-7-1"></span>

Entre los puntos medios hay $U_\mathrm d=U_4-U_2$, con las tensiones $U_2$ en $R_2$ y $U_4$ en $R_4$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm d=U_\mathrm q\left(\frac{R_4}{R_3+R_4}-\frac{R_2}{R_1+R_2}\right)=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}. \tag{7.1}$$

Para $R_1=R_2=R_3=R$ y $R_4=R+\Delta R$ se cumple

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}\qquad\text{para }\Delta R\ll R. \tag{7.2}$$
:::

⁠**Cómo leerlo:** El numerador de [(7.1)](#gl-7-1) se anula en el equilibrio. $\Delta R/R$ es el cambio relativo, sin unidad. **Validez:** El voltímetro no toma una corriente apreciable. **Casos límite:** $\Delta R=0$ da $U_\mathrm d=0$. $\Delta R\to\infty$ da $U_\mathrm d\to U_\mathrm q/2$: el punto medio derecho está entonces en el polo positivo.

:::herleitung Cambio pequeño
Con $U_2=U_\mathrm q/2$ y $U_4=U_\mathrm q(R+\Delta R)/(2R+\Delta R)$ resulta

$$U_\mathrm d=U_\mathrm q\,\frac{2(R+\Delta R)-(2R+\Delta R)}{2(2R+\Delta R)}=\frac{U_\mathrm q\,\Delta R}{4R+2\Delta R}=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}.$$
:::

:::abbildung et1/k4dms 9
A la izquierda, el puente con la $R_4$ variable. A la derecha, el mismo cambio en dos escalas: la línea roja es la lectura, la banda clara el error de lectura. En la escala de 10 V, un cambio de 9 mV se pierde en el error. En la escala de 100 mV, la desviación misma es la señal.
:::

::::beispiel galga extensométrica
Una __galga extensométrica__ es una fina pista metálica que se pega sobre una pieza. Si la pieza se estira, la pista se hace más larga y más delgada, y su resistencia $R=\rho\,l/A$ aumenta. El cambio relativo de resistencia es aproximadamente el doble del alargamiento. Con un alargamiento del 2 ‰, $R_4$ crece un 0,4 %, de 350 $\Omega$ a 351,4 $\Omega$. Entonces, $U_2=4{,}500$ V y $U_4=9\,\mathrm{V}\cdot351{,}4/701{,}4=4{,}509$ V, es decir, $U_\mathrm d=8{,}98$ mV. La aproximación da 9,00 mV, y se desvía un 0,2 %. Por el voltímetro de 10 M$\Omega$ circulan 0,9 nA; frente a los 12,9 mA de las ramas, una proporción de $7\cdot10^{-8}$: despreciable.
::::

**Por qué es más exacto.** Con una medición directa, el instrumento tendría que distinguir 4,509 V de 4,500 V, es decir, mostrar con seguridad tres decimales en el rango de 10 V. Pero su error de lectura de $\pm100$ mV es once veces el cambio buscado. En el puente basta el rango de 100 mV con $\pm1$ mV, una centésima parte (fig. [9](#abb-9)). A esto se suman dos ventajas. Si la fuente fluctúa un 1 %, $U_4$ cambia 45 mV, cinco veces la señal, mientras que $U_\mathrm d$ solo cambia 0,09 mV. Y si las cuatro resistencias cambian en el mismo factor, por ejemplo por el calor, $U_\mathrm d$ no varía.

:::frage ¿No se podría medir $U_4$ y restar 4,5 V de cabeza?
Se puede calcular, pero los $\pm100$ mV de error de lectura siguen en el resultado. El puente resta antes de que el instrumento mida. Por eso, este puede tener un rango pequeño.
:::

⁠**A partir de aquí:** Salvo indicación contraria, en todas las partes siguientes los instrumentos de medida se consideran ideales: amperímetros con $R_\mathrm i\to0$, voltímetros con $R_\mathrm i\to\infty$.

:::aufgabe Ejercicio 8 ★★★ Dos galgas
<span class="anker" id="aufg-8"></span>

En la rama derecha hay ahora dos galgas: $R_3=R-\Delta R$ se comprime, $R_4=R+\Delta R$ se estira, $R_1=R_2=R$. (a) Calcula $U_\mathrm d$ en general y para el ejemplo. (b) ¿Por qué el resultado es exactamente lineal en $\Delta R$? (c) ¿Qué cambia si las cuatro resistencias varían un 1 % por el calor?

:::loesung
(a) $R_3+R_4=2R$, así que $U_4=U_\mathrm q(R+\Delta R)/(2R)$. Con $U_2=U_\mathrm q/2$ se deduce $U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R=4{,}5\,\mathrm{V}\cdot0{,}004=18{,}0$ mV, el doble que con una galga.

(b) La suma $R_3+R_4$ sigue siendo $2R$. Por eso, la corriente en la rama derecha sigue siendo 12,9 mA, y $U_4$ crece exactamente con $R_4$. Con una galga, la suma también crece, y eso da el denominador de [(7.2)](#gl-7-2).

(c) Nada: en [(7.1)](#gl-7-1) se simplifica un factor común de todas las resistencias.
:::
:::
