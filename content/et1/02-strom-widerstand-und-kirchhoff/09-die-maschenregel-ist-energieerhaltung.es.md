---
title: Etapa 8: La ley de las mallas es conservación de la energía
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Corriente, resistencia y leyes de Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Capítulo 2: Corriente, resistencia y leyes de Kirchhoff
order: 1120900
summary: El segundo tipo de ecuación: ¿Qué exige la conservación de la energía a lo largo de un camino cerrado?
tags: 
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
El segundo tipo de ecuación: ¿Qué exige la conservación de la energía a lo largo de un camino cerrado? Con ella se puede resolver la red por completo.
:::

**La idea.** Cada punto de una red tiene un potencial ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Quien da una vuelta completa llega al mismo punto, es decir, al mismo potencial (fig. [9](#abb-9)). Para una carga, eso significa: la energía que gana en la fuente la cede de nuevo en las resistencias. En la batería, las fuerzas químicas elevan la carga contra el campo hasta el potencial más alto.

:::analogie
Una excursión circular termina en el punto de partida. Todas las subidas juntas son exactamente tan altas como todas las bajadas, sea cual sea el camino elegido. La analogía termina cuando cambia un campo magnético: entonces un lugar ya no tiene una «altura» fija ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)).
:::

:::satz Teorema 8.1 (Ley de las mallas, segunda ley de Kirchhoff)
<span class="anker" id="satz-8-1"></span>

La suma de todas las tensiones de rama a lo largo de una malla es cero en cualquier sentido de recorrido y en todo instante:

<span class="anker" id="gl-8-1"></span>
$$\sum_{\nu=1}^{N}U_\nu=0,\qquad U_\nu\text{ positiva a favor del recorrido, negativa en contra.} \tag{8.1}$$

Para una red, $z-k+1$ de estas ecuaciones son independientes; todas las demás se cumplen entonces.
:::

⁠**Cómo leerlo:** $U_\nu$ es la tensión de una rama, con su flecha. El sentido de recorrido es libre; solo cambia el signo global. **Validez:** El flujo magnético a través de la malla no debe cambiar, o el campo deja de ser irrotacional ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). En los circuitos, este flujo está casi por completo en las bobinas. La ley también vale para caminos por terminales abiertos, porque un camino no tiene que seguir un hilo.

:::herleitung La ley de las mallas a partir del potencial
Según el [capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$ no depende del camino, así que $\oint\vec E\cdot\mathrm{d}\vec s=0$. Para puntos $P_1,\dots,P_N$ a lo largo de una malla resulta

$$(\varphi_1-\varphi_2)+(\varphi_2-\varphi_3)+\dots+(\varphi_N-\varphi_1)=0.$$

Cada potencial aparece una vez con $+$ y otra con $-$. Multiplicado por la carga $Q$, esto es el balance de energía de una vuelta: la suma de todas las $Q\,U_\nu$ es cero.
:::

:::abbildung et1/k2masche 9
Potencial en la red resuelta a lo largo de dos mallas. Una tensión positiva baja el potencial si se sigue su flecha; contra la flecha lo sube. Izquierda: la fuente sube, $R_\mathrm a$ y $R_\mathrm b$ bajan $4+5=9$ V. A la derecha, la vuelta no pasa por ninguna fuente: el camino de regreso por $R_\mathrm b$ contra la corriente sube el potencial. Ambas vueltas terminan en el valor inicial.
:::

::::beispiel resolver la red
Las flechas de tensión de las resistencias están en el CR, es decir, de arriba abajo, y $U_\mathrm e$ de $K_2$ a $K_3$. $U_0=9$ V apunta de $K_1$ a $K_4$ (CG). Las tres mallas de la fig. [7](knoten-zweige-maschen.html#abb-7) dan

$$M_1:\ U_\mathrm a+U_\mathrm b-U_0=0,\qquad M_2:\ U_\mathrm c+U_\mathrm d-U_0=0,\qquad M_3:\ U_\mathrm e+U_\mathrm d-U_\mathrm b=0.$$

Con la ley de Ohm y las ecuaciones de nudo $I_\mathrm b=I_\mathrm a-I_\mathrm e$, $I_\mathrm d=I_\mathrm c+I_\mathrm e$ quedan tres incógnitas (en mA, $\mathrm{k\Omega}$, V):

$$7\,I_\mathrm a-5\,I_\mathrm e=9,\qquad4\,I_\mathrm c+I_\mathrm e=9,\qquad-5\,I_\mathrm a+I_\mathrm c+8\,I_\mathrm e=0.$$

Las dos primeras dan $I_\mathrm a=(9+5\,I_\mathrm e)/7$ e $I_\mathrm c=(9-I_\mathrm e)/4$. Sustituyendo en la tercera y multiplicando por 28 resulta $117\,I_\mathrm e=117$, es decir, $I_\mathrm e=1$ mA. Con ello

| Rama | 0 | a | b | c | d | e |
|---|---|---|---|---|---|---|
| $I$ en mA | 4 | 2 | 1 | 2 | 3 | 1 |
| $U$ en V | 9 | 4 | 5 | 6 | 3 | 2 |

Los potenciales respecto a $K_4$ son 9, 5, 3 y 0 V. **Comprobaciones:** Una cuarta malla por $K_1$, $K_2$, $K_3$ debe cumplirse por sí sola: $U_\mathrm a+U_\mathrm e-U_\mathrm c=4+2-6=0$. Energía: la fuente entrega $9\,\mathrm{V}\cdot4\,\mathrm{mA}=36$ mW, las resistencias absorben $8+5+12+9+2=36$ mW. Si hay dos caminos entre los mismos puntos, por ejemplo $R_1$, $R_2$ en serie junto a $R_3$, se obtiene $U_1+U_2-U_3=0$.
::::

:::ltspice Recalcular la red
⁠**Esquema:** fuente `voltage` con `9` de `k1` a masa, así que $K_4$ es la masa. `res`: `Ra 2k` de `k1` a `k2`, `Rb 5k` de `k2` a masa, `Rc 3k` de `k1` a `k3`, `Rd 1k` de `k3` a masa, `Re 2k` de `k2` a `k3`.

⁠**Directivas:** `.op`, y además `.meas op p2 FIND V(k2)`, `.meas op ie FIND I(Re)` y lo mismo para las demás magnitudes. Los resultados aparecen en el SPICE Error Log.

⁠**Lo que ves:** $\mathtt{V(k2)}=5$ V, $\mathtt{V(k3)}=3$ V, $\mathtt{I(Ra)}=\mathtt{I(Rc)}=2$ mA, $\mathtt{I(Rb)}=\mathtt{I(Re)}=1$ mA, $\mathtt{I(Rd)}=3$ mA. $\mathtt{I(V1)}=-4$ mA: SPICE cuenta la corriente de la fuente en el CR, por eso es negativa. Después monta el ejercicio [8](#aufg-8).
:::

:::frage ¿Cómo «sabe» la corriente cómo debe repartirse?
No sabe nada. Al encender, en los nudos se acumulan cargas diminutas que desplazan sus potenciales hasta que en ningún nudo queda nada retenido. Eso ocurre en nanosegundos. El resultado es la única solución que cumple ambas leyes a la vez.
:::

:::aufgabe Ejercicio 8 ★★ Malla y nudo juntos
<span class="anker" id="aufg-8"></span>

Una fuente de 12 V alimenta $R_1=1{,}5\,\mathrm{k\Omega}$; detrás están $R_2=3\,\mathrm{k\Omega}$ y una resistencia desconocida $R_3$ una junto a otra. Se mide $U_1=9$ V.

<ol class="al">

<li>

Determina $U_2$ y $U_3$ con la ley de las mallas.

</li>

<li>

Determina todas las corrientes y $R_3$.

</li>

<li>

Comprueba el balance de energía.

</li>

<li>

Predicción: Por la malla de la fuente, $R_1$ y $R_2$ pasa un imán de barra en movimiento. ¿Qué deja de cumplirse?

</li>

</ol>

:::loesung
(a) Malla de fuente, $R_1$, $R_2$: $U_2=12\,\mathrm{V}-9\,\mathrm{V}=3$ V. Malla de $R_2$, $R_3$: $U_3=U_2=3$ V.

(b) $I_1=9\,\mathrm{V}/1{,}5\,\mathrm{k\Omega}=6$ mA, $I_2=3\,\mathrm{V}/3\,\mathrm{k\Omega}=1$ mA. Ley de los nudos: $I_3=5$ mA, es decir, $R_3=3\,\mathrm{V}/5\,\mathrm{mA}=600\,\Omega$. Comprobación: $R_2\parallel R_3=500\,\Omega$, en total $2\,\mathrm{k\Omega}$, $12\,\mathrm{V}/2\,\mathrm{k\Omega}=6$ mA.

(c) La fuente entrega $12\,\mathrm{V}\cdot6\,\mathrm{mA}=72$ mW, las resistencias absorben $54+3+15=72$ mW.

(d) La ley de las mallas. El flujo variable crea a lo largo de la malla un campo rotacional, $\oint\vec E\cdot\mathrm{d}\vec s$ no es cero, y la suma de las tensiones pasa a ser igual a la tensión inducida. La ley de los nudos sigue siendo válida.
:::
:::
