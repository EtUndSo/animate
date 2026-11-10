---
title: Etapa 2: El amplificador diferencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El amplificador operacional
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Capítulo 11: El amplificador operacional
order: 1210400
summary: Una perturbación en ambas líneas debe desaparecer, y la diferencia entre ellas debe amplificarse.
tags: tensión de modo común, entrada no inversora, entrada inversora
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Una perturbación en ambas líneas debe desaparecer, y la diferencia entre ellas debe amplificarse. Para eso hace falta un circuito cuya salida dependa solo de la diferencia de dos tensiones.
:::

**La idea.** Dos transistores iguales T1 y T2 cuelgan por sus emisores del nudo común E (fig. [2](#abb-2)). Debajo está T3. Su base está a la tensión fija $U_\mathrm{bias}$, por lo que actúa como fuente de corriente ([capítulo 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) y extrae del nudo la corriente fija $I_0$. Las corrientes de base son pequeñas, así que se cumple $I_\mathrm{C1}+I_\mathrm{C2}=I_0$. La suma está fijada; solo puede cambiar el reparto.

Si ambas bases suben lo mismo, E sube con ellas, porque T3 mantiene fija la corriente y con ella $U_\mathrm{BE}$. No cambia nada. Esta parte común se llama __tensión de modo común__, $U_\mathrm{mc}=(\varphi_++\varphi_-)/2$. Si solo sube la base de T2, T2 toma más corriente. T1 recibe exactamente esa cantidad menos. En la resistencia de colector derecha cae más tensión; en la izquierda, menos, y la tensión entre los colectores se desvía.

:::abbildung et1/k11diff 2
A la izquierda, el amplificador diferencial con $I_0=2$ mA y $R_\mathrm{C}=3$ k$\Omega$. T3 mantiene fija la suma. A la derecha, el reparto: en torno a $U_\mathrm{D}=0$ circula 1 mA por cada rama; con 100 mV, el 97,9 % circula por T2.
:::

:::satz Teorema 2.1 (Amplificador diferencial)
<span class="anker" id="satz-2-1"></span>

T1 tiene la base en la entrada $\varphi_-$; T2, en la entrada $\varphi_+$. Con $U_\mathrm{D}=\varphi_+-\varphi_-$ y $U_\mathrm{A}=U_\mathrm{a1}-U_\mathrm{a2}$ se cumple

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}},\qquad I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}},\qquad U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1}). \tag{2.1}$$

Para $|U_\mathrm{D}|\ll U_T$ esto es una recta:

<span class="anker" id="gl-2-2"></span>
$$U_\mathrm{A}=A_\mathrm{D}\,U_\mathrm{D},\qquad A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}=\frac{U_{R_\mathrm{C}}}{U_T}. \tag{2.2}$$
:::

⁠**Cómo leerlo:** $S=I_\mathrm{C}/U_T$ es la transconductancia de un transistor con $I_\mathrm{C}=I_0/2$. $U_{R_\mathrm{C}}=I_0R_\mathrm{C}/2$ es la tensión de reposo en una resistencia de colector. $\varphi_+$ se llama __entrada no inversora__ porque la salida la sigue en el mismo sentido; $\varphi_-$, __entrada inversora__. **Validez:** transistores iguales, ambos en la región activa, corrientes de base pequeñas frente a $I_0$.

:::herleitung Reparto y ganancia
Ambos emisores están al mismo potencial, así que $U_\mathrm{BE2}-U_\mathrm{BE1}=U_\mathrm{D}$. Con $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ se sigue $I_\mathrm{C2}/I_\mathrm{C1}=\mathrm{e}^{U_\mathrm{D}/U_T}$. Junto con $I_\mathrm{C1}+I_\mathrm{C2}=I_0$ esto da [(2.1)](#gl-2-1). Para cambios pequeños: la suma está fijada, así que $\Delta I_\mathrm{C1}=-\Delta I_\mathrm{C2}$. Ambos son $S$ por el cambio de su propia $U_\mathrm{BE}$, de modo que los cambios son iguales y opuestos. Su diferencia es $U_\mathrm{D}$, así que cada unión soporta $\pm U_\mathrm{D}/2$. Por tanto, $\Delta I_\mathrm{C2}=S\,U_\mathrm{D}/2$ y $U_\mathrm{A}=2R_\mathrm{C}\,\Delta I_\mathrm{C2}=S\,R_\mathrm{C}\,U_\mathrm{D}$.
:::

::::beispiel
En reposo circula 1 mA por cada rama, y los colectores están a $12\,\mathrm{V}-3\,\mathrm{V}=9$ V. $S=38{,}5$ mS, así que $A_\mathrm{D}=3\,\mathrm{V}/26\,\mathrm{mV}=115$. Con $U_\mathrm{D}=1$ mV pasan $\pm19{,}2$ µ A de una rama a otra, cada colector se mueve 57,7 mV, y juntos dan $U_\mathrm{A}=115$ mV. Una perturbación de 100 mV en ambas entradas no cambia nada de esto.
::::

⁠**Casos límite:** $U_\mathrm{D}=0$ da $I_0/2$ por rama. Con $|U_\mathrm{D}|\gg U_T$ todo circula por un transistor, $U_\mathrm{A}\to\pm R_\mathrm{C}I_0=\pm6$ V. El rango lineal solo tiene unas pocas $U_T$ de ancho: con 26 mV, la recta da 3,0 V; la curva exacta, 2,77 V.

**Entrada.** Una señal de entrada $U_\mathrm{D}$ está aplicada a dos uniones BE en serie, y la resistencia de entrada es $2\,r_\mathrm{BE}=2B/S=10{,}4$ k$\Omega$. Con una corriente total de 20 µ A en lugar de 2 mA son 1,04 M$\Omega$, y cada base toma solo 50 nA. De ahí proceden $r_\mathrm{e}$ e $I_\mathrm{B}$ del modelo de referencia.

**Del amplificador diferencial al AO.** $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$ se queda en unos pocos cientos, porque $U_{R_\mathrm{C}}$ no puede superar la alimentación. Un espejo de corriente ([capítulo 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) en lugar de las resistencias lleva ambos cambios de corriente a un solo lado y actúa allí como la conexión en paralelo de dos $r_\mathrm{CE}$. Eso da $S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)\approx1400$. Detrás siguen una etapa amplificadora de tensión y un seguidor de emisor para la baja resistencia de salida. En conjunto son de $10^5$ a $10^6$. Este valor depende de $B$, $U_\mathrm{Early}$ y la temperatura: grande, pero impreciso.

:::frage ¿Por qué hay en cada transistor solo la mitad de la diferencia si solo subo una base?
Porque el nudo E sube la mitad con ella. T2 quiere más corriente, pero la suma está fijada, así que E sube hasta que T1 cede justo eso. La suma fija exige cambios iguales y opuestos de $U_\mathrm{BE}$. Poner toda la diferencia en una sola unión da el doble del $A_\mathrm{D}$ real.
:::

:::ltspice El reparto de corriente
⁠**Esquema:** Dos `npn` Q1, Q2 con el modelo `T`. Los colectores, cada uno a través de una `res` 3k, a `voltage` 12, nudos `a1`, `a2`. Ambos emisores en el nudo `e`, desde allí `current` 2m hacia una `voltage` $-12$. Base de Q1 a masa, base de Q2 a `voltage` `VP`.

⁠**Directivas:** `.model T NPN(IS=1.55e-13 BF=186 VAF=74)`, `.dc VP -0.2 0.2 0.1m`, `.meas dc u1 FIND V(a1)-V(a2) AT=-0.5m`, `.meas dc u2 FIND V(a1)-V(a2) AT=0.5m`, `.meas dc ad PARAM (u2-u1)/1m`.

⁠**Lo que ves:** `Ic(Q1)` e `Ic(Q2)` se cruzan en 0; con 100 mV, Q2 conduce el 97,8 % de la corriente. `ad` da 111,4 frente a 115 en el cálculo, porque LTspice calcula con $U_T=25{,}85$ mV y tiene en cuenta $r_\mathrm{CE}$. Introduce los valores del ejercicio [2](#aufg-2).
:::

:::aufgabe Ejercicio 2 ★★ Etapa diferencial
<span class="anker" id="aufg-2"></span>

Una etapa diferencial con transistores T trabaja con $I_0=1$ mA, $R_\mathrm{C}=5$ k$\Omega$ y $U_\mathrm{CC}=12$ V. (a) Determina $S$, $A_\mathrm{D}$ y el potencial de reposo de los colectores. (b) ¿Cuánto vale $U_\mathrm{A}$ con $U_\mathrm{D}=2$ mV? ¿Cuánta corriente pasa de una rama a otra? (c) Ambas entradas suben 1 V. ¿Qué ocurre con E, las corrientes y $U_\mathrm{A}$? (d) Predice: ¿cambia $A_\mathrm{D}$ si $I_0$ se duplica y $R_\mathrm{C}$ se reduce a la mitad?

:::loesung
(a) $S=0{,}5\,\mathrm{mA}/26\,\mathrm{mV}=19{,}2$ mS, $A_\mathrm{D}=96{,}2$, colectores a $12\,\mathrm{V}-2{,}5\,\mathrm{V}=9{,}5$ V. (b) $U_\mathrm{A}=192$ mV. Pasan $S\,U_\mathrm{D}/2=19{,}2$ µ A de una rama a otra. (c) E sube 1 V; $U_\mathrm{BE}$ y las corrientes no cambian, $U_\mathrm{A}=0$. (d) No: $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$, y $U_{R_\mathrm{C}}=2{,}5$ V no cambia.
:::
:::
